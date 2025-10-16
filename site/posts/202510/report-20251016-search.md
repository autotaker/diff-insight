---
date: '2025-10-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c693aca...MicrosoftDocs:0191f09
summary: この報告書では、リソース管理に関する指示を明確化するために「Prerequisites」および「Clean up resources」セクションが追加されたことが主な変更点として挙げられています。特に破壊的変更はなく、チュートリアルのタイトルやメタデータが明確化され、ユーザーにとって内容が理解しやすく調整されました。また、RAGに関する記事やサンプルコードも更新され、クラシックRAGとエージェントによる取得の違いが強調されています。全体的に、情報の最新性と一貫性を保つために細かな表現が改善されました。このアップデートは、Azure
  AI Searchを用いるエージェントによる生成的検索チュートリアルおよびガイド文書の改訂を通じて、ユーザーがよりスムーズに導入プロセスを進められるように設計されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c693aca...MicrosoftDocs:0191f09){target="_blank"}

<format>
# Highlights

## New Features
- 追加された「Prerequisites」および「Clean up resources」セクションで、リソース管理に関する指示が明確化。

## Breaking Changes
- 特になし。

## Other Updates
- チュートリアルのタイトルやメタデータが明確化され、ユーザーが内容を理解しやすいように調整。
- RAGに関する記事やサンプルコードも細かく更新され、クラシックRAGとエージェントによる取得の違いが強調されている。
- ドキュメント全体において、情報の最新性と一貫性を保つために、日付の更新と細かな表現の改善が行われた。

# Insights

このコードの差分による更新は、Azure AI Searchを用いたエージェントによる取得と生成的検索 (RAG) のチュートリアル及びガイド文書を一新しています。それにより、ユーザーがAzure AI Searchを利用する際の導入プロセスがより滑らかになります。

特に、「Prerequisites」や「Clean up resources」セクションの追加で、ユーザーは必要な準備と後処理についてすぐに把握しやすくなりました。このような細かい更新は、エージェントによる取得に初めて取り組む開発者にとって有用です。

一方、古くからあるRAGの手法はクラシックRAGとして明示され、ユーザーに二つの異なる取得アプローチを比較して選択できる柔軟性を提供しています。この文書修正は、ユーザーが自分のプロジェクトの要求に最も適した手法を見つける手助けとなるでしょう。

総合的に、このアップデートはドキュレーションの明確化と一貫性の強化を目的としており、新たなエージェント機能と既存の技術的知識を繋げる位置づけとなっています。開発者はスムーズに学習し、実践に活かせる情報を手に入れることができるため、デプロイが効率的に進むでしょう。この結果、Azure AI Searchの活用幅が大きく広がり、より多様なソリューションを構築するための基盤が築かれています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | チュートリアル: エージェントを用いた取得ソリューションの構築 | modified | 18 | 5 | 23 | 
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | minor update | エージェント間取得ソリューションのチュートリアル | modified | 1 | 1 | 2 | 
| [agentic-retrieval-overview.md](#item-d1f354) | minor update | エージェントによる取得の概要 | modified | 19 | 12 | 31 | 
| [cognitive-search-common-errors-warnings.md](#item-a5c854) | minor update | コグニティブサーチの一般的なエラーと警告 | modified | 12 | 1 | 13 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | 情報検索と生成AIの強化に関する概要 | modified | 40 | 30 | 70 | 
| [samples-python.md](#item-d2bf09) | minor update | Python サンプルコードに関する更新 | modified | 1 | 1 | 2 | 
| [search-get-started-agentic-retrieval.md](#item-4a40f4) | minor update | エージェントによる取得に関するガイドの更新 | modified | 1 | 1 | 2 | 
| [search-get-started-rag.md](#item-05ff0e) | minor update | RAGに関するクイックスタートガイドの更新 | modified | 5 | 2 | 7 | 
| [toc.yml](#item-c4768f) | minor update | 目次の更新に関する変更 | modified | 5 | 5 | 10 | 
| [tutorial-rag-build-solution-index-schema.md](#item-9a17ca) | minor update | クラシックRAGチュートリアルのタイトルと内容の更新 | modified | 6 | 3 | 9 | 
| [tutorial-rag-build-solution-maximize-relevance.md](#item-2fdb09) | minor update | クラシックRAGチュートリアルのタイトルと内容の更新 | modified | 9 | 9 | 18 | 
| [tutorial-rag-build-solution-minimize-storage.md](#item-088ad8) | minor update | クラシックRAGチュートリアルのタイトルと内容の更新 | modified | 6 | 3 | 9 | 
| [tutorial-rag-build-solution-models.md](#item-6796c9) | minor update | クラシックRAGチュートリアルのタイトルと内容の更新 | modified | 9 | 6 | 15 | 
| [tutorial-rag-build-solution-pipeline.md](#item-25ce01) | minor update | クラシックRAGチュートリアルのタイトルと内容の更新 | modified | 6 | 3 | 9 | 
| [tutorial-rag-build-solution-query.md](#item-93965f) | minor update | クラシックRAGチュートリアルのタイトルと内容の更新 | modified | 6 | 3 | 9 | 
| [tutorial-rag-build-solution.md](#item-c7eca4) | minor update | クラシックRAGソリューションのタイトルと内容の更新 | modified | 12 | 5 | 17 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -1,29 +1,30 @@
 ---
-title: Build an agentic retrieval solution
+title: 'Tutorial: Build an agentic retrieval solution'
 titleSuffix: Azure AI Search
 description: Learn how to design and build a custom agentic retrieval solution where Azure AI Search handles data retrieval for your custom agents in AI Foundry.
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
 ms.date: 09/10/2025
 ms.service: azure-ai-search
-ms.topic: how-to
+ms.topic: tutorial
 ms.custom:
   - build-2025
 ---
 
-# Build an agent-to-agent retrieval solution using Azure AI Search
+# Tutorial: Build an agent-to-agent retrieval solution using Azure AI Search
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
 This article describes an approach or pattern for building a solution that uses Azure AI Search for knowledge retrieval, and how to integrate knowledge retrieval into a custom solution that includes Azure AI Agent. This pattern uses an agent tool to invoke an agentic retrieval pipeline in Azure AI Search.
 
 :::image type="content" source="media/agentic-retrieval/agent-to-agent-pipeline.svg" alt-text="Diagram of Azure AI Search integration with Azure AI Agent service." lightbox="media/agentic-retrieval/agent-to-agent-pipeline.png" :::
 
-This article supports the [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) Python sample on GitHub.
-
 This exercise differs from the [Agentic Retrieval Quickstart](search-get-started-agentic-retrieval.md) in how it uses Azure AI Agent to retrieve data from the index, and how it uses an agent tool for orchestration. If you want to understand the retrieval pipeline in its simplest form, begin with the quickstart.
 
+> [!TIP]
+> To run the code for this tutorial, download the [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) Python sample on GitHub.
+
 ## Prerequisites
 
 The following resources are required for this design pattern:
@@ -315,6 +316,18 @@ Look at output tokens in the [activity array](agentic-retrieval-how-to-retrieve.
 
 + Set `maxOutputSize` in the [knowledge agent](agentic-retrieval-how-to-create-knowledge-base.md) to govern the size of the response, or `maxRuntimeInSeconds` for time-bound processing.
 
+## Clean up resources
+
+When you're working in your own subscription, at the end of a project, it's a good idea to remove the resources that you no longer need. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
+
+You can also delete individual objects:
+
++ [Delete a knowledge agent](agentic-retrieval-how-to-create-knowledge-base.md#delete-an-agent)
+
++ [Delete a knowledge source](agentic-knowledge-source-how-to-search-index.md#delete-a-knowledge-source)
+
++ [Delete an index](search-how-to-manage-index.md#delete-an-index)
+
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアル: エージェントを用いた取得ソリューションの構築"
}
```

### Explanation
この変更は、Azure AI Searchを使用してエージェントによる取得ソリューションを構築するためのチュートリアルに関連するもので、いくつかの重要な更新が含まれています。タイトルの変更により、内容がより明確に「Tutorial: Build an agentic retrieval solution」となり、読者が目的をすぐに理解できるようになっています。

具体的には、ドキュメントのメタデータにおける`ms.topic`の値が「how-to」から「tutorial」に変更され、さらに新たなセクション「## Prerequisites」が追加されました。このセクションでは、デザインパターンに必要なリソースについて述べています。また、リソースを削除する方法を案内する「## Clean up resources」セクションも新たに追加され、プロジェクトが完了した後のリソース管理についての指示がより明確になっています。

このように、全体として文書の構造が整えられ、ユーザーにとっての使いやすさが向上しています。

## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

<details>
<summary>Diff</summary>
````diff
@@ -27,7 +27,7 @@ This article also explains the three components of the retrieval response:
 The retrieve request can include instructions for query processing that override the defaults set on the knowledge agent.
 
 > [!NOTE]
-> By default, there's no model-generated "answer" in the response and you should pass the extracted response to an LLM so that it can ground its answer based on the search results. For an end-to-end example that includes this step, see [Build an agent-to-agent retrieval solution ](agentic-retrieval-how-to-create-pipeline.md) or [Azure OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo).
+> By default, there's no model-generated "answer" in the response and you should pass the extracted response to an LLM so that it can ground its answer based on the search results. For an end-to-end example that includes this step, see [Tutorial: Build an agent-to-agent retrieval solution ](agentic-retrieval-how-to-create-pipeline.md) or [Azure OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo).
 >
 >Alternatively, you can use [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md) to bring answer formulation into the agentic pipeline. In this workflow, the retriever response consists of LLM-formulated answers instead of the raw search results.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント間取得ソリューションのチュートリアル"
}
```

### Explanation
この変更は、Azure AI Searchのエージェントによる取得方法に関するドキュメントの一部で、説明文中のタイトルが更新されました。具体的には、エージェント間の取得ソリューションに関するリンクのテキストが「Build an agent-to-agent retrieval solution」から「Tutorial: Build an agent-to-agent retrieval solution」に変更されました。この変更により、タイトルがより明確にチュートリアルの形式であることを示し、読者が内容を理解しやすくなっています。

この部分は、リトリーブリクエストに関する注意事項を示すセクションの一部であり、モデル生成された「回答」がデフォルトではないこと、抽出された応答をLLM（大規模言語モデル）に渡す必要があることを説明しています。全体として、リンクの表現をチュートリアル形式に整えることで、ユーザーに対しての情報提供が一層親しみやすくなっています。

## articles/search/agentic-retrieval-overview.md{#item-d1f354}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about agentic retrieval concepts, architecture, and use cases
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 09/02/2025
+ms.date: 10/14/2025
 ms.service: azure-ai-search
 ms.topic: concept-article
 ms.custom:
@@ -17,15 +17,19 @@ ms.custom:
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-In Azure AI Search, *agentic retrieval* is a new multi-query pipeline designed for complex questions posed by users or agents in chat and copilot apps. It's intended for [Retrieval Augmented Generation (RAG)](retrieval-augmented-generation-overview.md) patterns. Here's how it works:
+What is agentic retrieval? In Azure AI Search, *agentic retrieval* is a new multi-query pipeline designed for complex questions posed by users or agents in chat and copilot apps. It's intended for [Retrieval Augmented Generation (RAG)](retrieval-augmented-generation-overview.md) patterns and agent-to-agent workflows. 
+
+Here's what it does:
 
 + Uses a large language model (LLM) to break down a complex query into smaller, focused subqueries for better coverage over your indexed content. Subqueries can include chat history for extra context.
 
 + Runs subqueries in parallel. Each subquery is semantically reranked to promote the most relevant matches.
 
 + Combines the best results into a unified response that an LLM can use to generate answers with your proprietary content.
 
-This high-performance pipeline helps you generate high quality grounding data for your chat application, with the ability to answer complex questions quickly.
++ The response is modular yet comprehensive in how it also includes a query plan and source documents. You can choose to use just the search results as grounding data, or invoke the LLM to formulate an answer.
+
+This high-performance pipeline helps you generate high quality grounding data (or an answer) for your chat application, with the ability to answer complex questions quickly.
 
 Programmatically, agentic retrieval is supported through a new [Knowledge Agents object](/rest/api/searchservice/knowledge-agents?view=rest-searchservice-2025-08-01-preview&preserve-view=true) in the 2025-08-01-preview and 2025-05-01-preview data plane REST APIs and in Azure SDK preview packages that provide the feature. A knowledge agent's retrieval response is designed for downstream consumption by other agents and chat apps.
 
@@ -63,29 +67,31 @@ Agentic retrieval is designed for conversational search experiences that use an
 
 ### How it works
 
-The agentic retrieval process follows three main phases:
+The agentic retrieval process works as follows:
+
+1. **Workflow initiation**: Your application calls a knowledge agent with retrieve action that provides a query and conversation history.
 
-1. **Query planning**: A knowledge agent sends your query and conversation history to an LLM (gpt-4o, gpt-4.1, and gpt-5 series), which analyzes the context and breaks down complex questions into focused subqueries. This step is automated and not customizable. The number of subqueries depends on what the LLM decides and whether the `maxDocsForReranker` parameter is higher than 50. A new subquery is defined for each 50-document batch sent to semantic ranker.
+1. **Query planning**: A knowledge agent sends your query and conversation history to an LLM, which analyzes the context and breaks down complex questions into focused subqueries. This step is automated and not customizable.
 
-2. **Query execution**: All subqueries run simultaneously against your knowledge sources, using keyword, vector, and hybrid search. Each subquery undergoes semantic reranking to find the most relevant matches. References are extracted and retained for citation purposes.
+1. **Query execution**: The knowledge agent sends the subqueries to your knowledge sources. All subqueries run simultaneously and can be keyword, vector, and hybrid search. Each subquery undergoes semantic reranking to find the most relevant matches. References are extracted and retained for citation purposes.
 
-3. **Result synthesis**: The system merges and ranks all results, then returns a unified response containing grounding data, source references, and execution metadata.
+1. **Result synthesis**: The system combines all results into a unified response with three parts: merged content, source references, and execution details.
 
-Your search index determines query execution and any optimizations that occur during query execution. Specifically, if your index includes searchable text and vector fields, a hybrid query executes. The index semantic configuration, plus optional scoring profiles, synonym maps, analyzers, and normalizers (if you add filters) are all used during query execution. You must have named defaults for a semantic configuration and a scoring profile.
+Your search index determines query execution and any optimizations that occur during query execution. Specifically, if your index includes searchable text and vector fields, a hybrid query executes. If the only searchable field is a vector field, then only pure vector search is used. The index semantic configuration, plus optional scoring profiles, synonym maps, analyzers, and normalizers (if you add filters) are all used during query execution. You must have named defaults for a semantic configuration and a scoring profile.
 
 ### Required components
 
 | Component | Service | Role |
 |-----------|---------|------|
 | **LLM** | Azure OpenAI | Creates subqueries from conversation context and later uses grounding data for answer generation |
 | **Knowledge agent** | Azure AI Search | Orchestrates the pipeline, connecting to your LLM and managing query parameters |
+| **Knowledge source** | Azure AI Search | Wraps the search index with properties pertaining to knowledge agent usage |
 | **Search index** | Azure AI Search | Stores your searchable content (text and vectors) with semantic configuration |
 | **Semantic ranker** | Azure AI Search | Required component that reranks results for relevance (L2 reranking) |
-| **Knowledge source** | Azure AI Search | Wraps the search index with properties pertaining to knowledge agent usage |
 
 ### Integration requirements
 
-Your application drives the pipeline by calling the knowledge agent and handling the response. The pipeline returns grounding data that you pass to an LLM for answer generation in your conversation interface. For implementation details, see [Build an agent-to-agent retrieval solution](agentic-retrieval-how-to-create-pipeline.md).
+Your application drives the pipeline by calling the knowledge agent and handling the response. The pipeline returns grounding data that you pass to an LLM for answer generation in your conversation interface. For implementation details, see [Tutorial: Build an agent-to-agent retrieval solution](agentic-retrieval-how-to-create-pipeline.md).
 
 > [!NOTE]
 > Only gpt-4o, gpt-4.1, and gpt-5 series models are supported for query planning. You can use any model for final answer generation.
@@ -109,8 +115,9 @@ Choose any of these options for your next step.
 
   + [Create a search index knowledge source](agentic-knowledge-source-how-to-search-index.md) or a [blob knowledge source](agentic-knowledge-source-how-to-blob.md)
   + [Create a knowledge agent](agentic-retrieval-how-to-create-knowledge-base.md)
+  + [Use answer synthesis for citation-backed responses](agentic-retrieval-how-to-answer-synthesis.md)
   + [Use a knowledge agent to retrieve data](agentic-retrieval-how-to-retrieve.md)
-  + [Build an agent-to-agent retrieval solution](agentic-retrieval-how-to-create-pipeline.md)
+  + [Tutorial: Build an agent-to-agent retrieval solution](agentic-retrieval-how-to-create-pipeline.md)
 
 + REST API reference:
 
@@ -146,7 +153,7 @@ Semantic ranking is performed for every subquery in the plan. Semantic ranking c
 
 Agentic retrieval has two billing models: billing from Azure OpenAI (query planning and, if enabled, answer synthesis) and billing from Azure AI Search for semantic ranking (query execution).
 
-This example omits answer synthesis and uses hypothetical prices to illustrate the estimation process. Your costs could be lower. For the actual price of transactions, see [Azure OpenAI pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing). For query execution, there's no charge for semantic ranking for agentic retrieval in the initial public preview.
+This pricing example omits answer synthesis, but helps illustrate the estimation process. Your costs could be lower. For the actual price of transactions, see [Azure OpenAI pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing). For query execution, there's no charge for semantic ranking for agentic retrieval in the initial public preview.
 
 #### Estimated billing costs for query planning
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントによる取得の概要"
}
```

### Explanation
この変更は、Azure AI Search におけるエージェントによる取得に関するドキュメントの内容を更新したもので、複数の重要なポイントが追加されています。最初に、文章の構造や第1段落の内容が変更され、「agentic retrieval」の定義に新たにエージェント間のワークフローが追加されました。また、問い合わせの処理をより具体的に説明する新しいセクションが加わり、複雑なクエリを小さなサブクエリに分割して検索カバレッジを向上させる方法や、并列実行されるサブクエリの結果を統合して応答を生成するプロセスの詳細が提供されています。

さらに、修正された部分には「チュートリアル」という表現が含まれ、関連するリソースの説明が改善されています。特に、ユーザーにとって重要な管理や構成の詳細が統合され、開発者がこの機能を利用しやすくなっています。これにより、エージェントによる取得の機能や実装の仕組みがより明確に伝わるようになっています。全体として、高性能なパイプラインの説明が充実し、利用者が機能を活用する際の理解が深まる内容となっています。

## articles/search/cognitive-search-common-errors-warnings.md{#item-a5c854}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 09/21/2025
+ms.date: 10/14/2025
 ms.update-cycle: 180-days
 ---
 
@@ -433,3 +433,14 @@ This error typically occurs due to one of the following:
 Ensure that the indexer has access to your setup components by reviewing your resource configurations to confirm they allow traffic to all required services:
 - [Firewall and IP restriction settings](search-indexer-howto-access-ip-restricted.md)
 - [Shared private link setup](search-indexer-howto-access-private.md)
+
+## `Error: Credentials provided in the connection string are invalid or have expired.`
+
+This error occurs when the Azure AI Search indexer cannot authenticate using the provided connection string or it has issues accessing the storage account to verify the credentials. 
+
+| Possible Cause | Details/Example | Resolution |
+|---|---|---|
+| Expired or rotated key | A connection string contains an outdated key that no longer works. | Go to the resource that is being contacted (for example, Azure Storage or Azure SQL) and copy the latest access keys if using key-based authentication, then update the data source or connection string accordingly. |
+| Managed identity not enabled or access not granted | The AI Search service [managed identity](search-how-to-managed-identities.md) is enabled but lacks the required access roles. | - Enable system or user-assigned [managed identity](search-how-to-managed-identities.md) on the search Service.<br>- Assign appropriate role(s) to the identity (for example, `Storage Blob Data Reader` for blob containers). Each [data source](search-data-sources-gallery.md) has its own permission requirements. |
+| Network/firewall blocks identity access | The resource contacted is configured to restrict network access. | Configure [network settings](search-indexer-howto-access-ip-restricted.md) to allow Azure AI Search access. |
+| Key authorization has been disabled | Shared key access removed on the source, but the Search service data source configuration still uses key-based authentication. | Use [managed identity](search-how-to-managed-identities.md) authentication and ensure role-based permissions are in place. From an Azure Storage perspective, this means that [shared key authorization functionality is blocked](/azure/storage/common/shared-key-authorization-prevent), either from the storage account itself, or enforced through enterprise-level Azure Policies. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブサーチの一般的なエラーと警告"
}
```

### Explanation
この変更は、コグニティブサーチに関する一般的なエラーと警告に関するドキュメントを更新し、特定のエラーメッセージとその原因、解決策を詳述した新しいセクションを追加したものです。具体的には、「`Error: Credentials provided in the connection string are invalid or have expired.`」という新しいエラー項目を追加しており、このエラーが発生する状況や解消方法についての詳細なガイドが提供されています。

追加された内容には、無効または期限切れの接続文字列に関する情報、潜在的な原因、具体例、解決策が含まれており、それぞれの原因に対して具体的な対応策が提案されているため、ユーザーは問題を特定しやすくなっています。この更新は、コグニティブサーチのユーザーがエラーをより迅速に解決できるようにすることを目的としており、ドキュメント全体の利用価値を高めるものとなっています。全体として、エラー管理における親切で実用的なリソースの提供が強化された内容です。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how generative AI and retrieval augmented generation (RAG) pa
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 08/18/2025
+ms.date: 10/14/2025
 ms.service: azure-ai-search
 ms.topic: conceptual
 ms.custom:
@@ -22,33 +22,44 @@ The decision about which information retrieval system to use is critical because
 
 + Indexing strategies that load and refresh at scale, for all of your content, at the frequency you require.
 
-+ Query capabilities and relevance tuning. The system should return *relevant* results, in the short-form formats necessary for meeting the token length requirements of large language model (LLM) inputs.
++ Query capabilities and relevance tuning. The system should return *relevant* results, in the short-form formats necessary for meeting the token length requirements of large language model (LLM) inputs. Query turnaround should be as fast as possible.
 
 + Security, global reach, and reliability for both data and operations.
 
 + Integration with embedding models for indexing, and chat models or language understanding models for retrieval.
 
-Azure AI Search is a [proven solution for information retrieval](/azure/developer/python/get-started-app-chat-template?tabs=github-codespaces) in a RAG architecture. It provides indexing and query capabilities, with the infrastructure and security of the Azure cloud. Through code and other components, you can design a comprehensive RAG solution that includes all of the elements for generative AI over your proprietary content. 
+Azure AI Search is a [proven solution for information retrieval](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md) in a RAG architecture. It provides indexing and query capabilities, with the infrastructure and security of the Azure cloud. Through code and other components, you can design a comprehensive RAG solution that includes all of the elements for generative AI over your proprietary content.
+
+You can choose between two approaches for RAG workloads: agentic retrieval, or the original query architecture for classic RAG.
 
 > [!NOTE]
 > New to copilot and RAG concepts? Watch [Vector search and state of the art retrieval for Generative AI apps](https://www.youtube.com/watch?v=lSzc1MJktAo).
 
-## Approaches for RAG with Azure AI Search
+## Modern RAG with Agentic Retrieval
+
+Azure AI Search now provides **agentic retrieval**, a specialized pipeline designed specifically for RAG patterns. This approach uses large language models to intelligently break down complex user queries into focused subqueries, executes them in parallel, and returns structured responses optimized for chat completion models.
+
+Agentic retrieval represents the evolution from traditional single-query RAG patterns to multi-query intelligent retrieval, providing:
+
++ Context-aware query planning using conversation history
++ Parallel execution of multiple focused subqueries  
++ Structured responses with grounding data, citations, and execution metadata
++ Built-in semantic ranking for optimal relevance
++ Optional answer synthesis that uses an LLM-formulated answer in the query response.
 
-Microsoft has several built-in implementations for using Azure AI Search in a RAG solution.
+You need new objects for this pipeline: one or more knowledge sources, a knowledge agent, and the retrieve action that you call from application code, such as a tool that works with your agent.
 
-+ Azure AI Search, [build an agentic retrieval pipeline](agentic-retrieval-overview.md) in a custom solution. The agentic pipeline is designed specifically for the RAG pattern. You write code that calls Azure AI Search APIs designed for chat completion model integration with your indexed contet.
-+ Azure AI Foundry, [use a vector index and retrieval augmentation](/azure/ai-foundry/concepts/retrieval-augmented-generation). 
-+ Azure OpenAI, [use a search index with or without vectors](/azure/ai-services/openai/concepts/use-your-data).
-+ Azure Machine Learning, [use a search index as a vector store in a prompt flow](/azure/machine-learning/how-to-create-vector-index).
+For new RAG implementations, we recommend starting with [agentic retrieval](agentic-retrieval-overview.md). For existing solutions, consider migrating to take advantage of improved accuracy and context understanding.
 
-## Custom RAG pattern for Azure AI Search
+## Classic RAG pattern for Azure AI Search
 
-A high-level summary of a RAG pattern based on Azure AI Search looks like this:
+A RAG solution can be implemented on Azure AI Search using the original query execution architecture. With this approach, your application sends a single query request to Azure AI Search, the search engine processes the request, and returns search results to the caller. There's no side trip to an LLM query planning or LLM integration in the query pipeline. There's no query execution details in the response, and citations are built into the response only if you have fields in your index that provide a parent document name or page. This approach is faster and simpler with fewer components. Depending on your application requirements, it can be the best choice. 
+
+A high-level summary of classic RAG pattern built on Azure AI Search looks like this:
 
 + Start with a user question or request (prompt).
-+ Send it to Azure AI Search to find relevant information.
-+ Return the top ranked search results to an LLM.
++ Send it as a query request to Azure AI Search to find relevant information.
++ Return the top-ranked search results to an LLM.
 + Use the natural language understanding and reasoning capabilities of the LLM to generate a response to the initial prompt.
 
 Azure AI Search provides inputs to the LLM prompt, but doesn't train the model. In a traditional RAG pattern, there's no extra training. The LLM is pretrained using public data, but it generates responses that are augmented by information from the retriever, in this case, Azure AI Search.
@@ -70,8 +81,6 @@ The information retrieval system provides the searchable index, query logic, and
 
 The LLM receives the original prompt, plus the results from Azure AI Search. The LLM analyzes the results and formulates a response. If the LLM is ChatGPT, the user interaction might consist of multiple conversation turns. An Azure solution most likely uses Azure OpenAI, but there's no hard dependency on this specific service.
 
-Except for features currently in preview, Azure AI Search doesn't provide native LLM integration for prompt flows or chat preservation, so you need to write code that handles orchestration and state. You can review demo source ([Azure-Samples/azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo)), updated for agentic retrieval, for a blueprint of what a full solution entails. We also recommend [Azure AI Foundry](/azure/ai-foundry/concepts/retrieval-augmented-generation) to create RAG-based Azure AI Search solutions that integrate with LLMs.
-
 ## Searchable content in Azure AI Search
 
 In Azure AI Search, all searchable content is stored in a search index that's hosted on your search service. A search index is designed for fast queries with millisecond response times, so its internal data structures exist to support that objective. To that end, a search index stores *indexed content*, and not whole content files like entire PDFs or images. Internally, the data structures include inverted indexes of [tokenized text](https://lucene.apache.org/core/7_5_0/test-framework/org/apache/lucene/analysis/Token.html), vector indexes for embeddings, and unaltered plain text for cases where verbatim matching is required (for example, in filters, fuzzy search, regular expression queries).
@@ -87,9 +96,9 @@ Since you probably know what kind of content you want to search over, consider t
 | image | tokens, unaltered text <sup>2</sup> | [Skills](cognitive-search-working-with-skillsets.md) for OCR and Image Analysis can process images for text recognition or image characteristics. Skills have an indexer requirement. |
 | image | vectors <sup>1</sup> | Images can be vectorized in an indexer pipeline, or handled externally for a mathematical representation of image content and then [indexed as vector fields](vector-search-how-to-create-index.md) in your index. You can use [Azure AI Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) or an open source model like [OpenAI CLIP](https://github.com/openai/CLIP/blob/main/README.md) to vectorize text and images in the same embedding space.|
 
- <sup>1</sup> Azure AI Search provides [integrated data chunking and vectorization](vector-search-integrated-vectorization.md), but you must take a dependency on indexers and skillsets. If you can't use an indexer, Microsoft's [Semantic Kernel](/semantic-kernel/overview/) or other community offerings can help you with a full stack solution. For code samples showing both approaches, see [azure-search-vectors repo](https://github.com/Azure/azure-search-vector-samples).
+ <sup>1</sup> Azure AI Search provides [integrated data chunking and vectorization](vector-search-integrated-vectorization.md), but you must take a dependency on indexers and skillsets. If you can't use an indexer, Microsoft's [Semantic Kernel](/semantic-kernel/overview/) or other community offerings can help you with a full stack solution. For code samples showing both approaches, see [azure-search-vectors-sample repo](https://github.com/Azure/azure-search-vector-samples).
 
-<sup>2</sup> Image descriptions are converted to searchable text and added to the index. The images themselves are not stored in the index. [Skills](cognitive-search-working-with-skillsets.md) are built-in support for [applied AI](cognitive-search-concept-intro.md). For OCR and Image Analysis, the indexing pipeline makes an internal call to the Azure AI Vision APIs. These skills pass an extracted image to Azure AI for processing, and receive the output as text that's indexed by Azure AI Search. Skills are also used for integrated data chunking (Text Split skill) and integrated embedding (skills that call Azure AI Vision multimodal, Azure OpenAI, and models in the Azure AI Foundry model catalog.) 
+<sup>2</sup> Image descriptions are converted to searchable text and added to the index. The images themselves are not stored in the index. [Skills](cognitive-search-working-with-skillsets.md) are built-in support for [applied AI](cognitive-search-concept-intro.md). For image descriptions and verbalizations, the indexing pipeline makes an internal call to the Azure OpenAI or Azure AI Vision. These skills pass an extracted image for processing, and receive the output as text that's indexed by Azure AI Search. Skills are also used for integrated data chunking and embedding. 
 
 Vectors provide the best accommodation for dissimilar content (multiple file formats and languages) because content is expressed universally in mathematic representations. Vectors also support similarity search: matching on the coordinates that are most similar to the vector query. Compared to keyword search (or term search) that matches on tokenized terms, similarity search is more nuanced. It's a better choice if there's ambiguity or interpretation requirements in the content or in queries.
 
@@ -99,18 +108,19 @@ Once your data is in a search index, you use the query capabilities of Azure AI
 
 In a non-RAG pattern, queries make a round trip from a search client. The query is submitted, it executes on a search engine, and the response returned to the client application. The response, or search results, consist exclusively of the verbatim content found in your index. 
 
-In a RAG pattern, queries and responses are coordinated between the search engine and the LLM. A user's question or query is forwarded to both the search engine and to the LLM as a prompt. The search results come back from the search engine and are redirected to an LLM. The response that makes it back to the user is generative AI, either a summation or answer from the LLM.
+In a classic RAG pattern, queries and responses are coordinated between the search engine and the LLM. A user's question or query is forwarded to both the search engine and to the LLM as a prompt. The search results come back from the search engine and are redirected to an LLM. The response that makes it back to the user is generative AI, either a summation or answer from the LLM.
+
+In a modern agentic retrieval RAG pattern, queries and responses integrate with LLMs for help with query planning and optional answer formulation. Query inputs can be richer, with chat history as well as the user's question. The LLM determines how to set up subqueries for the best coverage over your indexed content. The response includes not just search results, but the query execution details and source documents. You can optionally include answer formulation, which in other patterns occurs outside of the query pipeline.
 
-There's no query type in Azure AI Search - not even semantic or vector search - that composes new answers. Only the LLM provides generative AI. Here are the capabilities in Azure AI Search that are used to formulate queries:
+Here are the capabilities in Azure AI Search that are used to formulate queries:
 
 | Query feature | Purpose | Why use it |
 |---------------|---------|------------|
-| [Simple or full Lucene syntax](search-query-create.md) | Query execution over text and nonvector numeric content | Full text search is best for exact matches, rather than similar matches. Full text search queries are ranked using the [BM25 algorithm](index-similarity-and-scoring.md) and support relevance tuning through scoring profiles. It also supports filters and facets. |
-| [Filters](search-filters.md) and [facets](search-faceted-navigation.md) | Applies to text or numeric (nonvector) fields only. Reduces the search surface area based on inclusion or exclusion criteria. | Adds precision to your queries. |
-| [Semantic ranker](semantic-how-to-query-request.md) | Re-ranks a BM25 result set using semantic models. Produces short-form captions and answers that are useful as LLM inputs. | Easier than scoring profiles, and depending on your content, a more reliable technique for relevance tuning. |
+| [Agentic search (preview)](agentic-retrieval-how-to-create-knowledge-base.md) | Parallel query execution pipeline of multiple subqueries, returning a response designed for RAG workloads and agent consumer. Queries can be vector or keyword search. Semantic ranking ensures the best results of subquery are included in the final response structure. **This is the recommended approach for RAG patterns based on Azure AI Search**. |
+| [Keyword search](search-query-create.md) | Query execution over text and nonvector numeric content | Full text search is best for exact matches, rather than similar matches. Full text search queries are ranked using the [BM25 algorithm](index-similarity-and-scoring.md) and support relevance tuning through scoring profiles. It also supports filters and facets. |
   [Vector search](vector-search-how-to-query.md) | Query execution over vector fields for similarity search, where the query string is one or more vectors. | Vectors can represent all types of content, in any language. |
 | [Hybrid search](hybrid-search-how-to-query.md) | Combines any or all of the above query techniques. Vector and nonvector queries execute in parallel and are returned in a unified result set. | The most significant gains in precision and recall are through hybrid queries. |
-| [Agentic search (preview)](agentic-retrieval-how-to-create-knowledge-base.md) | Parallel query execution pipeline of multiple subqueries, returning a response designed for RAG workloads and agent consumer. Queries can be vector or keyword search. Semantic ranking ensures the best results of subquery are included in the final response structure. **This is the recommended approach for RAG patterns based on Azure AI Search**. |
+| [Filters](search-filters.md) and [facets](search-faceted-navigation.md) | Applies to text or numeric (nonvector) fields only. Reduces the search surface area based on inclusion or exclusion criteria. | Adds precision to your queries. |
 
 ### Structure the query response
 
@@ -143,7 +153,7 @@ Here are some tips for maximizing relevance and recall:
 
 In comparison and benchmark testing, hybrid queries with text and vector fields, supplemented with semantic ranking, produce the most relevant results.
 
-### Example code for a RAG workflow
+<!-- ### Example code for a classic RAG workflow
 
 The following Python code demonstrates the essential components of a basic RAG workflow in Azure AI Search. You need to set up the clients, define a system prompt, and provide a query. The prompt tells the LLM to use just the results from the query, and how to return the results. For more steps based on this example, see this [RAG quickstart](search-get-started-rag.md).
 
@@ -205,25 +215,25 @@ response = openai_client.chat.completions.create(
 )
 
 print(response.choices[0].message.content)
-```
+``` -->
 
 ## Integration code and LLMs
 
-A RAG solution that includes Azure AI Search can leverage [built-in data chunking and vectorization capabilities](vector-search-integrated-vectorization.md), or you can build your own using platforms like Semantic Kernel, LangChain, or LlamaIndex. 
+A RAG solution that includes Azure AI Search can leverage [built-in data chunking and vectorization capabilities](vector-search-integrated-vectorization.md), or you can build your own using platforms like Semantic Kernel, LangChain, or LlamaIndex.
 
-[Notebooks in the demo repository](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/community-integration) are a great starting point because they show patterns for LLM integration. Much of the code in a RAG solution consists of calls to the LLM so you need to develop an understanding of how those APIs work, which is outside the scope of this article.
+We recommend the [Azure OpenAI demo](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md) for an example of a full stack RAG chat app with Azure OpenAI and Azure AI Search.
 
 ## How to get started
 
 There are many ways to get started, including code-first solutions and demos.
 
-### [**Docs**](#tab/docs)
+For help with choosing between agentic retrieval and classic RAG, try a few quickstarts using your own data to understand the development effort and compare outcomes.
 
-+ [Try this RAG quickstart](search-get-started-rag.md) for a demonstration of query integration with chat models over a search index.
+### [**Docs**](#tab/docs)
 
 + [Try this agentic retrieval quickstart](search-get-started-rag.md) to walk through the new and recommended approach for RAG.
 
-+ [Tutorial: How to build a RAG solution in Azure AI Search](tutorial-rag-build-solution.md) for focused coverage on the features and pattern for RAG solutions that obtain grounding data from a search index.
++ [Try this classic RAG quickstart](search-get-started-rag.md) for a demonstration of query integration with chat models over a search index.
 
 + [Review indexing concepts and strategies](search-what-is-an-index.md) to determine how you want to ingest and refresh data. Decide whether to use vector search, keyword search, or hybrid search. The kind of content you need to search over, and the type of queries you want to run, determines index design.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "情報検索と生成AIの強化に関する概要"
}
```

### Explanation
この変更は、「情報検索と生成AIの強化（RAG）」に関する記事の内容を更新し、より明確で具体的な情報を提供しています。主に、Azure AI Searchが提供する機能についての説明が強化され、特に新たに「エージェントによる取得」というパイプラインが紹介されています。このパイプラインは、ユーザーの複雑なクエリを知的に分解して並行処理し、構造化された応答を返すことができるため、高度な情報検索のアプローチを可能にします。

また、エージェントによる取得のメリットや、従来のRAGパターンとの違いが説明され、セマンティックランク付けやオプションとしての応答合成等の機能も細かく記載されています。さらに、RAGソリューションの構築において、どのようにAzure AI Searchが役立つかについての具体的な事例や推奨されるアプローチが示されており、ユーザーが新たにこの機能を導入する際のサポートが提供されています。

全体として、内容の整理が行われ、最新のベストプラクティスや推奨事項が強調されることで、開発者がAzure AI Searchを利用したRAGを活用し易くなっています。また、実装や統合に必要な情報へのリンクも新たに追加されており、ユーザーが必要なリソースへのアクセスが容易になっています。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -42,7 +42,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. T
 | [Quickstart-Semantic-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
 | [Quickstart-Vector-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Vector-Search) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
 | [Tutorial-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Tutorial-RAG) | [Build a RAG solution using Azure AI Search](tutorial-rag-build-solution.md) | Create an indexing pipeline that loads, chunks, embeds, and ingests searchable content for RAG. |
-| [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) | [Build an agent-to-agent retrieval solution using Azure AI Search](agentic-retrieval-how-to-create-pipeline.md) | Unlike [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval), this sample incorporates Azure AI Agent for request orchestration. |
+| [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) | [Tutorial: Build an agent-to-agent retrieval solution using Azure AI Search](agentic-retrieval-how-to-create-pipeline.md) | Unlike [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval), this sample incorporates Azure AI Agent for request orchestration. |
 
 ## Accelerators
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python サンプルコードに関する更新"
}
```

### Explanation
この変更は、Azure AI Searchに関連するPythonサンプルコードのリストにおいて、特定のエントリーの説明部分を更新しました。具体的には、「エージェントによる取得パイプラインの例」に関する記述が、「チュートリアル: Azure AI Searchを使用してエージェントからエージェントへの取得ソリューションを構築する」という文言に変更されました。この修正により、より明確で一貫性のあるタイトル表現が実現され、ユーザーがサンプルを見つけやすくなっています。

全体として、この更新は、サンプルコードの内容を明確にし、ユーザーが必要とするリソースを簡単に特定できるようにすることを目的としています。ドキュメントの明瞭化は、特に新規ユーザーや学習者にとって有益です。コードサンプルの目的や使用方法がより直感的に理解できるようになっており、より良いユーザーエクスペリエンスを提供します。

## articles/search/search-get-started-agentic-retrieval.md{#item-4a40f4}

<details>
<summary>Diff</summary>
````diff
@@ -42,4 +42,4 @@ zone_pivot_groups: search-get-started-agentic-retrieval
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
 + [Create a knowledge agent](agentic-retrieval-how-to-create-knowledge-base.md)
 + [Use a knowledge agent to retrieve data](agentic-retrieval-how-to-retrieve.md)
-+ [Build an agent-to-agent retrieval solution](agentic-retrieval-how-to-create-pipeline.md)
++ [Tutorial: Build an agent-to-agent retrieval solution](agentic-retrieval-how-to-create-pipeline.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントによる取得に関するガイドの更新"
}
```

### Explanation
この変更は、「エージェントによる取得の開始ガイド」において、特定のリンクのタイトルが更新されました。具体的には、「エージェントからエージェントへの取得ソリューションを構築する」というタイトルが「チュートリアル: エージェントからエージェントへの取得ソリューションを構築する」に変更されました。この修正により、ドキュメントがより明確になり、学習者や開発者が内容を理解しやすくなるよう配慮されています。

更新されたタイトルは、ユーザーがそのリンク先の内容がチュートリアルであることを直感的に理解できるようにすることを目的としており、特に新たにエージェントによる取得を学ぼうとしているユーザーにとって、役立つ情報が提供されています。このような軽微な更新は、全体の文書の一貫性を保ち、ナビゲーションの利便性を向上させる役割を果たしています。

## articles/search/search-get-started-rag.md{#item-05ff0e}

<details>
<summary>Diff</summary>
````diff
@@ -8,14 +8,17 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: quickstart
-ms.date: 07/09/2025
+ms.date: 10/15/2025
 zone_pivot_groups: programming-languages-ai-search-rag-qs
 ---
 
-# Quickstart: Generative search (RAG) using grounding data from Azure AI Search
+# Quickstart: Classic generative search (RAG) using grounding data from Azure AI Search
 
 In this quickstart, you send queries to a chat completion model for a conversational search experience over your indexed content on Azure AI Search. After setting up Azure OpenAI and Azure AI Search resources in the Azure portal, you run code to call the APIs.
 
+> [!NOTE]
+> We now recommend [agentic retrieval](search-get-started-agentic-retrieval.md) for RAG workflows, but classic RAG is simpler. If it meets your application requirements, it's still a good choice.
+
 ::: zone pivot="csharp"
 
 [!INCLUDE [.NET quickstart](includes/quickstarts/search-get-started-rag-dotnet.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGに関するクイックスタートガイドの更新"
}
```

### Explanation
この変更は、「RAG（生成的検索）を使用したAzure AI Searchのクイックスタートガイド」に関して行われました。具体的には、以下の点が更新されています。

1. **日付の変更**: ドキュメントの日付が「2025年7月9日」から「2025年10月15日」に変更されました。

2. **タイトルの更新**: ガイドのタイトルが「クイックスタート: Azure AI Searchからのデータを使用した生成的検索 (RAG)」から「クイックスタート: クラシック生成的検索 (RAG) を使用したAzure AI Searchからのデータ」に変更されました。この変更は、より具体的に旧来のアプローチを強調しています。

3. **新しいノートの追加**: エージェントによる取得がRAGワークフローに対して推奨されることを知らせるノートが追加されました。これにより、ユーザーは新しいアプローチを考慮しつつも、クラシックRAGが依然として使える選択肢であることが示されています。

このような修正により、ドキュメントは最新情報に基づき、ユーザーが最適な選択をするための支援を提供しています。また、RAGに関する理解を深めるための文脈を与えています。全体として、利用者が適切なリソースを選択しやすくするために重要な更新となっています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -68,7 +68,7 @@ items:
     href: search-get-started-agentic-retrieval.md
   - name: Vector search
     href: search-get-started-vector.md
-  - name: Generative search (RAG)
+  - name: Classic RAG
     href: search-get-started-rag.md
   - name: Full-text search
     href: search-get-started-text.md
@@ -152,9 +152,11 @@ items:
       href: tutorial-document-extraction-image-verbalization.md
     - name: Verbalize images from a structured document layout
       href: tutorial-document-layout-image-verbalization.md
-  - name: RAG tutorials
+  - name: Agentic retrieval tutorial
+    href: agentic-retrieval-how-to-create-pipeline.md
+  - name: Classic RAG tutorials
     items:
-    - name: Build a RAG solution
+    - name: Build a classic RAG solution
       href: tutorial-rag-build-solution.md
     - name: Choose models
       href: tutorial-rag-build-solution-models.md
@@ -410,8 +412,6 @@ items:
         href: agentic-retrieval-how-to-answer-synthesis.md
       - name: Retrieve data using an agent
         href: agentic-retrieval-how-to-retrieve.md
-      - name: Build a retrieval pipeline
-        href: agentic-retrieval-how-to-create-pipeline.md
       - name: Migrate agentic retrieval code
         href: agentic-retrieval-how-to-migrate.md
     - name: Vector search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新に関する変更"
}
```

### Explanation
この変更は、「目次 (toc.yml)」ファイルの更新に関するもので、主にセクション名の変更やリファレンスの整理が行われました。具体的な修正内容には以下の点が含まれます。

1. **セクション名の変更**: 「生成的検索 (RAG)」という項目が「クラシックRAG」に変更され、関連するリンクが適切に更新されました。これにより、ユーザーはコンテンツをより正確に理解できるようになります。

2. **チュートリアルの追加と項目名の変更**: 新たに「エージェントによる取得チュートリアル」という項目が追加され、そのリンクが「agentic-retrieval-how-to-create-pipeline.md」に設定されました。これにより、エージェント関連の内容が目立つようになり、開発者にとっての利便性が向上しています。

3. **クラシックRAGチュートリアルの明確化**: 既存の「RAGチュートリアル」という項目も「クラシックRAGチュートリアル」に変更され、ユーザーが具体的にどの種類のチュートリアルを参照しているのかを明示する形になっています。

4. **不要な重複の削除**: いくつかの項目が整理され、重複が削除されています。このことは、目次をよりコンパクトにし、ユーザーにとってのナビゲーションを向上させます。

全体として、この変更はドキュメントの整合性を高め、利用者が必要な情報に迅速にアクセスできるようにするための重要な更新です。

## articles/search/tutorial-rag-build-solution-index-schema.md{#item-9a17ca}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'RAG tutorial: Design an index'
+title: 'Classic RAG tutorial: Design an index'
 titleSuffix: Azure AI Search
 description: Design an index for RAG patterns in Azure AI Search.
 manager: nitinme
@@ -8,14 +8,17 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: tutorial
-ms.date: 05/29/2025
+ms.date: 10/14/2025
 
 ---
 
-# Tutorial: Design an index for RAG in Azure AI Search
+# Tutorial: Design an index for classic RAG in Azure AI Search
 
 An index contains searchable text and vector content, plus configurations. In a RAG pattern that uses a chat model for responses, you want an index designed around chunks of content that can be passed to an LLM at query time. 
 
+> [!NOTE]
+> We now recommend [agentic retrieval](agentic-retrieval-overview.md) for RAG workflows, but classic RAG is simpler. If it meets your application requirements, it's still a good choice.
+
 In this tutorial, you:
 
 > [!div class="checklist"]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クラシックRAGチュートリアルのタイトルと内容の更新"
}
```

### Explanation
この変更は、「RAGチュートリアル: インデックス設計」に関する内容の更新です。主に、タイトルの修正と日付の更新が行われています。以下のポイントが主な変更点です。

1. **タイトルの変更**: チュートリアルのタイトルが「RAGチュートリアル: インデックス設計」から「クラシックRAGチュートリアル: インデックス設計」に更新されました。この変更により、ユーザーはこのチュートリアルが従来のRAGアプローチに関するものであることが明確になります。

2. **日付の更新**: ドキュメントの日付が「2025年5月29日」から「2025年10月14日」に変更され、情報が最新の状態であることが示されています。

3. **チュートリアル内容の明確化**: チュートリアルの具体的な内容も、クラシックRAGのテクニックに適した情報として更新されています。また、ノートが追加され、RAGワークフローにおいてエージェントによる取得が推奨されることも明記されています。ただし、クラシックRAGが依然として適切な選択肢であることを強調しています。

全体として、この変更はチュートリアルの明確性を高め、ユーザーが求めている情報により迅速にアクセスできるようにするための重要な更新となっています。

## articles/search/tutorial-rag-build-solution-maximize-relevance.md{#item-2fdb09}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'RAG tutorial: Tune relevance'
+title: 'Classic RAG tutorial: Tune relevance'
 titleSuffix: Azure AI Search
 description: Learn how to use the relevance tuning capabilities to return high quality results for generative search.
 manager: nitinme
@@ -10,14 +10,17 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: tutorial
-ms.date: 06/11/2025
+ms.date: 10/14/2025
 ---
 
-# Tutorial: Maximize relevance (RAG in Azure AI Search)
+# Tutorial: Maximize relevance (classic RAG in Azure AI Search)
 
-In this tutorial, learn how to improve the relevance of search results used in RAG solutions. Relevance tuning can be an important factor in delivering a RAG solution that meets user expectations. In Azure AI Search, relevance tuning includes L2 semantic ranking and scoring profiles. 
+Azure AI Search provides relevance tuning strategies for improving the relevance of search results in classic RAG solutions.  Relevance tuning can be an important factor in delivering a RAG solution that meets user expectations. 
 
-To implement these capabilities, you revisit the index schema to add configurations for semantic ranking and scoring profiles. You then rerun the queries using the new constructs.
+> [!NOTE]
+> We now recommend [agentic retrieval](agentic-retrieval-overview.md) for RAG workflows, but classic RAG is simpler. If it meets your application requirements, it's still a good choice.
+
+In Azure AI Search, relevance tuning includes L2 semantic ranking and scoring profiles. To implement these capabilities, you revisit the index schema to add configurations for semantic ranking and scoring profiles. You then rerun the queries using the new constructs.
 
 In this tutorial, you modify the existing search index and queries to use:
 
@@ -27,16 +30,13 @@ In this tutorial, you modify the existing search index and queries to use:
 
 This tutorial updates the search index created by the [indexing pipeline](tutorial-rag-build-solution-pipeline.md). Updates don't affect the existing content, so no rebuild is necessary and you don't need to rerun the indexer.
 
-> [!NOTE]
-> There are more relevance features in preview, including vector query weighting and setting minimum thresholds, but we omit them from this tutorial because they're in preview.
-
 ## Prerequisites
 
 - [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and the [Jupyter package](https://pypi.org/project/jupyter/).
 
 - [Azure AI Search](search-create-service-portal.md), Basic tier or higher for managed identity and semantic ranking.
 
-- [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource), with a deployment of text-embedding-002 and gpt-35-turbo.
+- [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource), with a deployment of text-embedding-3-small and gpt-4o.
 
 ## Download the sample
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クラシックRAGチュートリアルのタイトルと内容の更新"
}
```

### Explanation
この変更は、「RAGチュートリアル: 関連性の調整」に関する内容の更新で、主にタイトルの変更と内容の整理が行われています。具体的な変更点は以下の通りです。

1. **タイトルの変更**: チュートリアルのタイトルが「RAGチュートリアル: 関連性の調整」から「クラシックRAGチュートリアル: 関連性の調整」に変更されました。これにより、従来のRAG手法に焦点を当てていることが明確になります。

2. **日付の更新**: ドキュメントの日付が「2025年6月11日」から「2025年10月14日」に変更され、最新の情報が反映される形となっています。

3. **内容の整理と明確化**: チュートリアルの内容が整理され、「クラシックRAGソリューションでの検索結果の関連性を向上させる戦略」が明示されています。また、エージェントによる取得が推奨されつつも、クラシックRAGは依然として適切な選択肢であることが強調されています。

4. **新しい構文の使用**: チュートリアルの実行手順において、さらに具体的な情報が追加され、検索インデックスとクエリの改修の必要性に関する記載が明確になっています。

5. **依存関係の変更**: Azure OpenAIに関連する依存関係が更新され、使用されるモデルが「text-embedding-002」から「text-embedding-3-small」となりました。

このように、全体としての変更は、ユーザーがチュートリアルの内容をより明確に理解し、最新の情報に基づいて関連性の調整を行えるようにするためのものです。

## articles/search/tutorial-rag-build-solution-minimize-storage.md{#item-088ad8}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'RAG tutorial: Minimize storage and costs'
+title: 'Classic RAG tutorial: Minimize storage and costs'
 titleSuffix: Azure AI Search
 description: Compress vectors using narrow data types and scalar quantization. Remove extra copies of stored vectors to further save on space.
 manager: nitinme
@@ -8,15 +8,18 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: tutorial
-ms.date: 09/23/2025
+ms.date: 10/14/2025
 ms.custom: sfi-ropc-nochange
 
 ---
 
-# Tutorial: Minimize storage and costs (RAG in Azure AI Search)
+# Tutorial: Minimize storage and costs (classic RAG in Azure AI Search)
 
 Azure AI Search offers several approaches for reducing the size of vector indexes. These approaches range from vector compression, to being more selective over what you store on your search service.
 
+> [!NOTE]
+> We now recommend [agentic retrieval](agentic-retrieval-overview.md) for RAG workflows, but classic RAG is simpler. If it meets your application requirements, it's still a good choice.
+
 In this tutorial, you modify the existing search index to use:
 
 > [!div class="checklist"]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クラシックRAGチュートリアルのタイトルと内容の更新"
}
```

### Explanation
この変更は、「RAGチュートリアル: ストレージとコストの削減」に関する内容の更新です。主な変更点は以下の通りです。

1. **タイトルの変更**: チュートリアルのタイトルが「RAGチュートリアル: ストレージとコストの削減」から「クラシックRAGチュートリアル: ストレージとコストの削減」に更新されました。これにより、従来のRAG手法に関連する内容であることが強調されています。

2. **日付の更新**: ドキュメントの日付が「2025年9月23日」から「2025年10月14日」に変更され、情報の最新性が確保されています。

3. **内容の明確化**: Azure AI Searchにおけるベクターインデックスのサイズ削減手法に関する記述が整理され、ベクター圧縮や検索サービスにおけるストレージの選択的使用方法が具体的に示されています。

4. **ノートの追加**: RAGワークフローにおけるエージェントによる取得が推奨される旨のノートが追加され、クラシックRAGが簡便であることが言及されています。

5. **チュートリアルの構成**: チュートリアルの文脈に関連して、既存の検索インデックスを調整するための手順が示されることになります。

全体として、この変更は、ユーザーがストレージとコストを削減するためのアプローチを理解しやすくすることを目指しています。また、最新の情報が反映され、関連性の高い手法が強調されています。

## articles/search/tutorial-rag-build-solution-models.md{#item-6796c9}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'RAG tutorial: Set up models'
+title: 'CLassic RAG tutorial: Set up models'
 titleSuffix: Azure AI Search
 description: Set up an embedding model and chat model for generative search (RAG).
 manager: nitinme
@@ -9,14 +9,17 @@ ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: tutorial
 ms.custom: references_regions
-ms.date: 07/17/2025
+ms.date: 10/14/2025
 
 ---
 
-# Tutorial: Choose embedding and chat models for RAG in Azure AI Search
+# Tutorial: Choose embedding and chat models for classic RAG in Azure AI Search
 
 A RAG solution built on Azure AI Search takes a dependency on embedding models for vectorization, and on chat completion models for conversational search over your data.
 
+> [!NOTE]
+> We now recommend [agentic retrieval](agentic-retrieval-overview.md) for RAG workflows, but classic RAG is simpler. If it meets your application requirements, it's still a good choice.
+
 In this tutorial, you:
 
 > [!div class="checklist"]
@@ -75,11 +78,11 @@ The following models are commonly used for a chat search experience:
 
 | Client | Chat models |
 |--------|------------|
-| Azure OpenAI | GPT-35-Turbo, <br>GPT-4, <br>GPT-4o, <br>GPT-4 Turbo |
+| Azure OpenAI | <br>GPT-4, <br>GPT-4o, <br>GPT-4.1. <br>GPT-5 |
 
-GPT-35-Turbo and GPT-4 models are optimized to work with inputs formatted as a conversation.
+GPT-4 and GPT-5 models are optimized to work with inputs formatted as a conversation.
 
-We use GPT-4o in this tutorial. During testing, we found that it's less likely to supplement with its own training data. For example, given the query "how much of the earth is covered by water?", GPT-35-Turbo answered using its built-in knowledge of earth to state that 71% of the earth is covered by water, even though the sample data doesn't provide that fact. In contrast, GPT-4o responded (correctly) with "I don't know".
+We use GPT-4o in this tutorial.
 
 ## Deploy models and collect information
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クラシックRAGチュートリアルのタイトルと内容の更新"
}
```

### Explanation
この変更は、「RAGチュートリアル: モデルの設定」に関する内容の更新です。主な変更点は以下の通りです。

1. **タイトルの変更**: チュートリアルのタイトルが「RAGチュートリアル: モデルの設定」から「クラシックRAGチュートリアル: モデルの設定」に更新されました。これにより、従来のRAG手法に関連する内容であることが強調されています。

2. **日付の更新**: ドキュメントの日付が「2025年7月17日」から「2025年10月14日」に変更されており、情報が最新であることが示されています。

3. **内容の明確化**: チュートリアルの内容が整理され、Azure AI Search上での埋め込みモデル及びチャットモデルの重要性について具体的に触れられています。

4. **ノートの追加**: RAGワークフローにおいてエージェントによる取得が推奨されることが強調されており、従来のRAGが依然として適切な選択肢であることが述べられています。

5. **モデルの変更**: サポートされるチャットモデルの情報が更新され、「GPT-35-Turbo」がリストから外され、「GPT-5」が追加されました。また、使用するモデルに関する説明も整理され、GPT-4oがこのチュートリアルで使用されることが明確に言及されています。

この変更全体として、ユーザーに対してモデル設定の最新情報を提供し、クラシックRAGのアプローチを強調することを目的としています。これにより、利用者が適切なモデルを選択できるよう支援しています。

## articles/search/tutorial-rag-build-solution-pipeline.md{#item-25ce01}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'RAG tutorial: Build an indexing pipeline'
+title: 'Classic RAG tutorial: Build an indexing pipeline'
 titleSuffix: Azure AI Search
 description: Create an indexer-driven pipeline that loads, chunks, embeds, and ingests content for RAG solutions on Azure AI Search.
 manager: nitinme
@@ -8,16 +8,19 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: tutorial
-ms.date: 06/11/2025
+ms.date: 10/14/2025
 ms.custom:
   - ignite-2024
   - sfi-ropc-nochange
 ---
 
-# Tutorial: Build an indexing pipeline for RAG on Azure AI Search
+# Tutorial: Build an indexing pipeline for classic RAG on Azure AI Search
 
 Learn how to build an automated indexing pipeline for a RAG solution on Azure AI Search. Indexing automation is through an indexer that drives indexing and skillset execution, providing [integrated data chunking and vectorization](vector-search-integrated-vectorization.md) on a one-time or recurring basis for incremental updates.
 
+> [!NOTE]
+> We now recommend [agentic retrieval](agentic-retrieval-overview.md) for RAG workflows, but classic RAG is simpler. If it meets your application requirements, it's still a good choice.
+
 In this tutorial, you:
 
 > [!div class="checklist"]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クラシックRAGチュートリアルのタイトルと内容の更新"
}
```

### Explanation
この変更は、「RAGチュートリアル: インデックスパイプラインの構築」に関連する内容の更新です。主な変更点は以下の通りです。

1. **タイトルの変更**: チュートリアルのタイトルが「RAGチュートリアル: インデックスパイプラインの構築」から「クラシックRAGチュートリアル: インデックスパイプラインの構築」に更新され、クラシックRAGの手法に特化していることが明確になりました。

2. **日付の更新**: ドキュメントの日付が「2025年6月11日」から「2025年10月14日」に変更され、最新の情報が反映されています。

3. **内容の明確化**: 自動化されたインデクシングパイプラインの構築に関する説明が整理され、インデクサーがインデクシングとスキルセットの実行をドライブする仕組みについて詳しく説明されています。

4. **ノートの追加**: RAGワークフローにおいて、エージェントによる取得が推奨されることが強調されており、クラシックRAGが依然として有力な選択肢であることが説明されています。

5. **チュートリアルの構成**: チュートリアルの内容が段階的に整理され、ユーザーがインデックスパイプラインを構築する際に必要なステップが明確に示されています。

全体として、この変更は、クラシックRAGに基づくインデクシングパイプラインの構築方法を学ぶための情報を提供し、ユーザーの理解を助けることを目的としています。最新の手法とアプローチの明確な説明がなされることで、実践的なガイドが強化されています。

## articles/search/tutorial-rag-build-solution-query.md{#item-93965f}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'RAG tutorial: Search using an LLM'
+title: 'Classic RAG tutorial: Search using an LLM'
 titleSuffix: Azure AI Search
 description: Learn how to build queries and engineer prompts for LLM-enabled search on Azure AI Search. Queries used in generative search provide the inputs to an LLM chat engine.
 manager: nitinme
@@ -10,13 +10,16 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: tutorial
-ms.date: 06/17/2025
+ms.date: 10/14/2025
 ---
 
-# Tutorial: Search your data using a chat model (RAG in Azure AI Search)
+# Tutorial: Search your data using a chat model (classic RAG in Azure AI Search)
 
 The defining characteristic of a RAG solution on Azure AI Search is sending queries to a Large Language Model (LLM) for a conversational search experience over your indexed content. It can be surprisingly easy if you implement just the basics.
 
+> [!NOTE]
+> We now recommend [agentic retrieval](agentic-retrieval-overview.md) for RAG workflows, but classic RAG is simpler. If it meets your application requirements, it's still a good choice.
+
 In this tutorial, you:
 
 > [!div class="checklist"]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クラシックRAGチュートリアルのタイトルと内容の更新"
}
```

### Explanation
この変更は、「RAGチュートリアル: LLMを使用した検索」に関する内容の更新です。主な変更点は以下の通りです。

1. **タイトルの変更**: チュートリアルのタイトルが「RAGチュートリアル: LLMを使用した検索」から「クラシックRAGチュートリアル: LLMを使用した検索」に変更され、従来のRAG手法に特化した内容であることが強調されています。

2. **日付の更新**: ドキュメントの日付が「2025年6月17日」から「2025年10月14日」に変更され、最新の情報に更新されています。

3. **内容の明確化**: このチュートリアルでは、Azure AI Search上でのLLMを活用した検索クエリの構築とプロンプトの設計が説明されており、ユーザーに対して具体的な指示が提供されています。

4. **ノートの追加**: RAGワークフローにおいてエージェントによる取得が推奨される旨が明記されており、クラシックRAGの手法が依然として適切な選択肢であることが強調されています。

5. **チュートリアルの構成**: ユーザーがチャットモデルを使用してデータを検索するために必要な手順が明確に示されており、初心者でも取り組みやすい内容になっています。

この変更は、クラシックRAGに基づく検索体験の理解を助け、ユーザーが効果的にLLMを利用した検索を実現するための情報を提供することを目的としています。また、最新の情報が反映されることで、利用者にとっての信頼性が向上しています。

## articles/search/tutorial-rag-build-solution.md{#item-c7eca4}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Build a RAG solution
+title: Build a classic RAG solution
 titleSuffix: Azure AI Search
 description: Learn how to build a generative search (RAG) app using LLMs and your proprietary grounding data in Azure AI Search.
 manager: nitinme
@@ -8,19 +8,26 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: overview
-ms.date: 05/29/2025
+ms.date: 10/14/2025
 
 ---
 
-# How to build a RAG solution using Azure AI Search
+# How to build a classic RAG solution using Azure AI Search
 
-This tutorial series demonstrates a pattern for building RAG solutions on Azure AI Search. It explains the components that you need to build, enumerates the dependencies, and provides optimizations for maximizing relevance and minimizing costs.
+This tutorial series demonstrates the classic pattern for building RAG solutions on Azure AI Search. Classic RAG uses the original query pipeline, with no LLM integration except for at the end of the pipeline when you pass the search results to an LLM for answer formulation.
+
+> [!NOTE]
+> We now recommend [agentic retrieval](agentic-retrieval-overview.md) for RAG workflows, but classic RAG is simpler. If it meets your application requirements, it's still a good choice.
+
+## In this series
+
+In this series, you learn about the components, dependencies, and optimizations for maximizing relevance and minimizing costs.
 
 Sample data is a [collection of PDFs](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth_book_2019_text_pages) uploaded to Azure Storage. The content is from [NASA's Earth free e-book](https://www.nasa.gov/ebooks/earth/).
 
 Sample code can be found in [this Python notebook](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Tutorial-RAG/Tutorial-rag.ipynb), but we recommend using the articles in this series for context, insights, and for exploring alternative approaches.
 
-## Exercises in this series
+### Exercises in this series
 
 - Choose your models for embeddings and chat
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クラシックRAGソリューションのタイトルと内容の更新"
}
```

### Explanation
この変更は、「RAGソリューションの構築」に関連する内容の更新です。主な変更点は以下の通りです。

1. **タイトルの変更**: チュートリアルのタイトルが「RAGソリューションを構築する」から「クラシックRAGソリューションを構築する」に変更され、クラシックなアプローチに特化していることが明確になりました。

2. **日付の更新**: ドキュメントの日付が「2025年5月29日」から「2025年10月14日」に変更され、最新の情報が反映されています。

3. **内容の明確化**: このチュートリアルシリーズでは、クラシックRAGのパターンを用いてAzure AI SearchでのRAGソリューションの構築方法を説明しています。具体的には、元のクエリパイプラインを使用し、パイプラインの最後に検索結果をLLMに渡して回答を生成するアプローチに重点が置かれています。

4. **ノートの追加**: RAGワークフローにおいてエージェントによる取得が推奨されることが記載されており、クラシックRAGがシンプルであるため、アプリケーションの要件を満たすならば依然として良い選択肢であることが強調されています。

5. **構成の更新**: チュートリアルシリーズ内で学ぶ内容として、コンポーネント、依存関係、関連性を最大化しコストを最小化するための最適化について説明されています。また、データサンプルとしてNASAの電子書籍が挙げられ、実用的なリソースへのリンクも提供されています。

6. **演習の形式変更**: 「演習」の見出しが「演習シリーズ」から「このシリーズの演習」に変更され、より具体的な情報を提供する方向に修正されました。

この変更は、クラシックRAGソリューションに関する実用的なガイドを提供し、ユーザーが効果的にAzure AI Searchを活用できるようにすることを目的としています。また、最新の情報と最適化が反映されたことで、ユーザーにとっての実用性が向上しています。


