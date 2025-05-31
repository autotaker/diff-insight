---
date: '2025-05-31'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:768223a...MicrosoftDocs:ca0291a
summary: 今回の修正では、Azure OpenAIモデルに関する手順の明確化を中心としたマイナーアップデートが行われました。新たに追加された画像ファイル「use-this-model.png」がユーザーの理解を助け、視覚的な情報提供が強化されています。文書内の手順や用語が改定され、全体的に使い勝手が向上しました。また、地域サポート情報の更新により、特定地域のキャパシティ制約についても注意が促されています。これらの変更は、ユーザーエクスペリエンスを向上させ、ドキュメントをより使いやすいリソースにしています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:768223a...MicrosoftDocs:ca0291a){target="_blank"}

# Highlights

## New features

- 新しい画像ファイル「use-this-model.png」が追加され、ベクター検索と統合ベクター化に関する手順や概念の理解を補助します。

## Breaking changes

- 特に注意が必要な破壊的変更はありませんが、手順や用語の変更があり、ユーザーは新しいドキュメントを熟読する必要があります。

## Other updates

- 複数のドキュメントが更新され、Azure OpenAIモデルのデプロイ手順や用語が明確化されました。
- REST APIを使用したデプロイメントの手順も改良されました。
- .NET、Python、REST用のAzure AI Searchサンプルが更新され、より明確な説明が追加されています。
- 地域サポート情報が更新され、一部地域のキャパシティ制約情報が補足されました。

# Insights

今回の修正は、多くの点でユーザーエクスペリエンスを向上させることを目的としたマイナーアップデートが中心となっています。特に、Azure OpenAIモデルに関する手順が明確化され、具体性が増しています。デプロイメント名の指定方法や、モデル選択に関する指示が追加されて、ユーザーが戸惑うことなくプロセスを進められるよう配慮されています。

REST APIを利用したデプロイメント手順も同様に、具体性が増し、初学者でも容易に理解できるよう工夫されています。また、Azure AI Search用の各種サンプルドキュメントも更新され、用語や手順が最新のものに合わせられています。「LLM駆動の知識エージェント」から「クエリ計画にLLM推論を統合する知識エージェント」への変更など、ユーザーが技術的背景を踏まえた設定を理解できるように詳細が補足されています。

「use-this-model.png」の追加は、視覚的情報を通じてユーザーがモデルの使い方を直感的に理解できる新しい試みです。これにより、全体としてのドキュメントの使いやすさと視覚的アピールが向上しました。

また、地域サポートに関する情報も更新され、一部地域でのキャパシティ制約に注意が促されています。これにより、ユーザーが使用制限下での意思決定をより適切に行えるようになっています。

最終的に、これらの更新により、Azure AI Searchに関するドキュメントはより多くのユーザーにとって利用しやすく、実践可能なリソースとなりました。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-python.md](#item-efee6a) | minor update | エージェント検索のクイックスタートに関する更新 | modified | 8 | 9 | 17 | 
| [agentic-retrieval-rest.md](#item-3df373) | minor update | REST APIを使用したエージェント検索のクイックスタートに関する更新 | modified | 8 | 9 | 17 | 
| [use-this-model.png](#item-b16f9c) | new feature | 新しいモデル使用に関する画像の追加 | added | 0 | 0 | 0 | 
| [samples-dotnet.md](#item-12f3fa) | minor update | .NET用のAzure AI Searchサンプルの更新 | modified | 3 | 3 | 6 | 
| [samples-python.md](#item-d2bf09) | minor update | Python用のAzure AI Searchサンプルの更新 | modified | 2 | 2 | 4 | 
| [samples-rest.md](#item-198ebc) | minor update | REST用のAzure AI Searchサンプルの更新 | modified | 3 | 3 | 6 | 
| [search-region-support.md](#item-25b0f1) | minor update | Azure AI Search地域サポート情報の更新 | modified | 5 | 5 | 10 | 
| [tutorial-rag-build-solution-models.md](#item-6796c9) | minor update | RAGソリューションモデル構築チュートリアルの更新 | modified | 5 | 7 | 12 | 
| [vector-search-integrated-vectorization-ai-studio.md](#item-353fcc) | minor update | 統合ベクトル化に関するAIスタジオガイドの更新 | modified | 7 | 5 | 12 | 


# Modified Contents
## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 05/29/2025
+ms.date: 05/30/2025
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -39,20 +39,19 @@ Agentic retrieval [supports several models](../../search-agentic-retrieval-how-t
 
 To deploy the Azure OpenAI models:
 
-1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/).
+1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/) and select your Azure OpenAI resource.
 
-1. On the home page, find the Azure OpenAI tile and select **Let's go**.
+1. From the left pane, select **Model catalog**.
 
-    :::image type="content" source="../../media/search-get-started-agentic-retrieval/azure-openai-lets-go-tile.png" alt-text="Screenshot of the Azure OpenAI tile in the Azure AI Foundry portal." border="true" lightbox="../../media/search-get-started-agentic-retrieval/azure-openai-lets-go-tile.png":::
+1. Select **gpt-4o-mini**, and then select **Use this model**.
 
-   Your most recently used Azure OpenAI resource appears. If you have multiple Azure OpenAI resources, select **All resources** to switch between them.
+1. Specify a deployment name. To simplify your code, we recommend **gpt-4o-mini**.
 
-1. From the left pane, select **Model catalog**.
+1. Accept the defaults.
 
-1. Deploy `gpt-4o-mini` and `text-embedding-3-large` to your Azure OpenAI resource.
+1. Select **Deploy**.
 
-   > [!NOTE]
-   > To simplify your code, don't use a custom deployment name for either model. This quickstart assumes the deployment and model names are the same.
+1. Repeat the previous steps for **text-embedding-3-large**.
 
 ## Configure role-based access
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索のクイックスタートに関する更新"
}
```

### Explanation
この修正は、Azure OpenAIモデルのデプロイメントに関する手順を更新することを目的としています。主に、手順の改善と具体性の向上を図り、ユーザーがプロセスをより理解しやすくするために変更が行われました。具体的には、デプロイメント名の指定についての推奨事項や操作手順が明確化され、Azure AI Foundryポータルでのモデル選択に関する指示が追加されました。また、日付の更新も行われています。この更新により、ユーザーは最新の手順に従ってAzure OpenAIリソースを効率的にデプロイできるようになります。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 05/29/2025
+ms.date: 05/30/2025
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -40,20 +40,19 @@ Agentic retrieval [supports several models](../../search-agentic-retrieval-how-t
 
 To deploy the Azure OpenAI models:
 
-1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/).
+1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/) and select your Azure OpenAI resource.
 
-1. On the home page, find the Azure OpenAI tile and select **Let's go**.
+1. From the left pane, select **Model catalog**.
 
-    :::image type="content" source="../../media/search-get-started-agentic-retrieval/azure-openai-lets-go-tile.png" alt-text="Screenshot of the Azure OpenAI tile in the Azure AI Foundry portal." border="true" lightbox="../../media/search-get-started-agentic-retrieval/azure-openai-lets-go-tile.png":::
+1. Select **gpt-4o-mini**, and then select **Use this model**.
 
-   Your most recently used Azure OpenAI resource appears. If you have multiple Azure OpenAI resources, select **All resources** to switch between them.
+1. Specify a deployment name. To simplify your code, we recommend **gpt-4o-mini**.
 
-1. From the left pane, select **Model catalog**.
+1. Accept the defaults.
 
-1. Deploy `gpt-4o-mini` and `text-embedding-3-large` to your Azure OpenAI resource.
+1. Select **Deploy**.
 
-   > [!NOTE]
-   > To simplify your code, don't use a custom deployment name for either model. This quickstart assumes the deployment and model names are the same.
+1. Repeat the previous steps for **text-embedding-3-large**.
 
 ## Configure role-based access
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIを使用したエージェント検索のクイックスタートに関する更新"
}
```

### Explanation
この修正は、REST APIを使用してAzure OpenAIモデルをデプロイする手順の更新を目的としています。主な変更点は、手順の明確化であり、ユーザーがより簡単にデプロイできるように、具体的な操作手順が追加されています。具体的には、Azure AI Foundryポータルでのリソース選択や、モデルの指定方法についての詳細が改良されています。また、デプロイメント名の設定に関する推奨事項も強調されています。この更新により、ユーザーは最新の手順に従い、より簡単にエージェント検索モデルを設定できるようになります。

## articles/search/media/vector-search-integrated-vectorization-ai-studio/use-this-model.png{#item-b16f9c}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しいモデル使用に関する画像の追加"
}
```

### Explanation
この修正は、新しい画像ファイル「use-this-model.png」の追加を示しています。この画像は、ベクター検索と統合ベクター化に関連する手順やコンセプトの理解を助けるために使用されることを目的としています。画像が追加されたことで、ユーザーは視覚的な情報を元に、モデルの使用方法やデプロイメント手順をよりスムーズに理解できるようになります。この変更は、ドキュメント全体の使いやすさと有用性を向上させる役割を果たします。

## articles/search/samples-dotnet.md{#item-12f3fa}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - devx-track-dotnet
   - ignite-2023
 ms.topic: concept-article
-ms.date: 05/29/2025
+ms.date: 05/30/2025
 ---
 
 # C# samples for Azure AI Search
@@ -52,15 +52,15 @@ Code samples from the Azure AI Search team demonstrate features and workflows. A
 |-------------|------------------|---------|
 | [create-mvc-app](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/create-mvc-app) |  [Tutorial: Add search to an ASP.NET Core (MVC) app](tutorial-csharp-create-mvc-app.md) | While most samples are console applications, this MVC sample uses a web page to front the sample Hotels index, demonstrating basic search, pagination, and other server-side behaviors.|
 | [quickstart](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/v11) | [Quickstart: Full-text search using the Azure SDKs](search-get-started-text.md) | Covers the basic workflow for creating, loading, and querying a search index in C# using sample data. |
-| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) | [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md) | Creates an LLM-powered knowledge agent that retrieves and synthesizes information from your search index. |
+| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) | [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md) | Creates a knowledge agent in Azure AI Search to integrate LLM reasoning into query planning. |
 | [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | [Quickstart: Semantic ranking using the Azure SDKs](search-get-started-semantic.md) | Shows the index schema and query request for invoking semantic ranker. |
 | [search-website](https://github.com/Azure-Samples/azure-search-static-web-app) | [Tutorial: Add search to web apps](tutorial-csharp-overview.md) | Demonstrates an end-to-end search app that includes bulk upload using the push APIs and a rich client for hosting the app and handling search requests.|
 | [tutorial-ai-enrichment](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/tutorial-ai-enrichment)  | [Tutorial: AI-generated searchable content from Azure blobs](cognitive-search-tutorial-blob-dotnet.md) | Shows how to configure an indexer and skillset. |
 | [multiple-data-sources](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources)  | [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md) | Merges content from two data sources into one search index. |
 | [Optimize-data-indexing](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/optimize-data-indexing) | [Tutorial: Optimize indexing with the push API](tutorial-optimize-indexing-push-api.md) | Demonstrates optimization techniques for pushing data into a search index. |
 | [DotNetHowTo](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowTo)  | [How to use the .NET client library](search-howto-dotnet-sdk.md) | Steps through the basic workflow, but in more detail and with discussion of API usage.  |
 | [DotNetToIndexers](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToIndexers) | [Tutorial: Index Azure SQL data](search-indexer-tutorial.md) | Shows how to configure an Azure SQL indexer that has a schedule, field mappings, and parameters.  |
-| [DotNetHowToEncryptionUsingCMK](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToEncryptionUsingCMK)  | [How to configure customer-managed keys for data encryption](search-security-manage-encryption-keys.md) | Shows how to create objects that are encrypted with a Customer Key. |
+| [DotNetHowToEncryptionUsingCMK](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToEncryptionUsingCMK) | [How to configure customer-managed keys for data encryption](search-security-manage-encryption-keys.md) | Shows how to create objects that are encrypted with a Customer Key. |
 | [DotNetVectorDemo](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetVectorDemo)  | [readme](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetVectorDemo/readme.md) | Create, load, and query a vector index. |
 | [DotNetIntegratedVectorizationDemo](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetIntegratedVectorizationDemo)  | [readme](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetIntegratedVectorizationDemo/readme.md) | Extends the vector workflow to include skills-based automation for data chunking and embedding. |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": ".NET用のAzure AI Searchサンプルの更新"
}
```

### Explanation
この修正では、Azure AI Searchに関する.NETのサンプルドキュメントが更新されました。主な変更点は、数か所のテキストが修正され、説明や手順がより明確にされていることです。特に、クイックスタートの一部が「LLM駆動の知識エージェント」を作成する方法から「クエリ計画にLLM推論を統合する知識エージェントを作成する方法」に変更され、具体的な機能の強調が見られます。また、日付の更新なども行われています。この変更により、ユーザーが提供されるサンプルをより理解しやすく、活用しやすくすることが目的です。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: concept-article
-ms.date: 05/29/2025
+ms.date: 05/30/2025
 ---
 
 # Python samples for Azure AI Search
@@ -41,7 +41,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 | [Quickstart-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-RAG) | Source code for the Python portion of [Quickstart: Generative search (RAG) with grounding data from Azure AI Search](search-get-started-rag.md). |
 | [Quickstart-Semantic-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) | Source code for the Python portion of [Quickstart: Semantic ranking using the Azure SDKs](search-get-started-semantic.md). This sample shows the index schema and query request for invoking semantic ranker. |
 | [Tutorial-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Tutorial-RAG) | Source code for the Python portion of [How to build a RAG solution using Azure AI Search](tutorial-rag-build-solution.md).|
-| [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) | Source code for the Python portion of [Build an agent-to-agent retrieval solution using Azure AI Search](search-agentic-retrieval-how-to-pipeline.md). Unlike the [quickstart](search-get-started-agentic-retrieval.md), this sample incorporates Azure AI Foundry Agent Service for data retrieval and orchestration. |
+| [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) | Source code for the Python portion of [Build an agent-to-agent retrieval solution using Azure AI Search](search-agentic-retrieval-how-to-pipeline.md). Unlike [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md), this sample incorporates Azure AI Agent for request orchestration. |
 | [azure-function-search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/azure-function-search) | Source code for the Python example of an Azure function that sends queries to a search service. You can substitute this Python version of the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
 | [bulk-insert](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/bulk-insert) | Source code for the Python example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python用のAzure AI Searchサンプルの更新"
}
```

### Explanation
この修正では、Azure AI Searchに関するPythonサンプルドキュメントが更新されました。変更点としては、いくつかのテキストの修正と日付の更新があります。具体的には、「エージェント対エージェントの検索ソリューションを構築するためのサンプル」がAzure AI Foundry Agent Serviceから「Azure AI Agent」に変更され、より正確な用語が使用されています。また、日付が2025年5月29日から5月30日に更新されています。これにより、サンプル内容がより明確になり、ユーザーがAzure AI Searchを活用するためのガイダンスが向上しています。

## articles/search/samples-rest.md{#item-198ebc}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 05/29/2025
+ms.date: 05/30/2025
 ---
 
 # REST samples for Azure AI Search
@@ -28,7 +28,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 |---------|---------|
 | [quickstart](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart) | Source code for [Quickstart: Text search using REST](search-get-started-rest.md). This sample covers the basic workflow for creating, loading, and querying a search index using sample data. |
 | [quickstart-vectors](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) | Source code for [Quickstart: Vector search using REST APIs](search-get-started-vector.md). This sample covers the basic workflow for indexing and querying vector data. |
-| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/agentic-retrieval) | Source code for the REST portion of [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md). This sample shows you how to create an LLM-powered knowledge agent that retrieves and synthesizes information from your search index. |
+| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/agentic-retrieval) | Source code for the REST portion of [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md). This sample shows you how to create a knowledge agent in Azure AI Search to integrate LLM reasoning into query planning. |
 | [skillset-tutorial](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial) | Source code for [Tutorial: Use REST and AI to generate searchable content from Azure blobs](cognitive-search-tutorial-blob.md). This sample shows you how to create a skillset that iterates over Azure blobs to extract information and infer structure.|
 | [skill examples](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skill-examples) | Skillset examples in indexer pipelines that include indexes and indexers so that you can follow field mappings, output field mappings, and source paths. |
 | [debug-sessions](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Debug-sessions) | Source code for [Tutorial: Diagnose, repair, and commit changes to your skillset](cognitive-search-tutorial-debug-sessions.md). This sample shows you how to use a skillset debug session in the Azure portal. REST is used to create the objects used during debug.|
@@ -38,4 +38,4 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 | [projections](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/projections) | Source code for [Define projections in a knowledge store](knowledge-store-projections-examples.md). This sample explains how to specify the physical data structures in a knowledge store.|
 
 > [!TIP]
-> Try the [Samples browser](/samples/browse/?expanded=azure&languages=http&products=azure-cognitive-search) to search for Microsoft code samples in GitHub, filtered by product, service, and language.
\ No newline at end of file
+> Try the [Samples browser](/samples/browse/?expanded=azure&languages=http&products=azure-cognitive-search) to search for Microsoft code samples in GitHub, filtered by product, service, and language.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST用のAzure AI Searchサンプルの更新"
}
```

### Explanation
この修正では、Azure AI Searchに関連するRESTサンプルドキュメントが更新されました。主な変更点は、いくつかのテキストの修正と日付の更新です。「エージェント駆動の検索」を構築するためのサンプルの説明が、「LLM推論をクエリ計画に統合する知識エージェントを作成する方法」に変更され、内容がより明確になりました。また、日付が2025年5月29日から5月30日に更新され、サンプルの関連性が維持されています。これにより、ユーザーは最新の情報をもとにAzure AI Searchを活用しやすくなっています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -53,6 +53,8 @@ You can create an Azure AI Search service in any of the following Azure public r
 | West US 3​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | West Central US​ ​ | ✅ |  | ✅ | ✅ |  |
 
+<sup>1</sup> This region has capacity constraints on all tiers.
+
 ### Europe
 
 | Region | AI enrichment | Availability zones | Agentic retrieval | Semantic ranker | Query rewrite |
@@ -64,16 +66,14 @@ You can create an Azure AI Search service in any of the following Azure public r
 | Italy North​​ |  | ✅ | ✅ | ✅ |  |
 | Norway East​​ | ✅ | ✅ |  |  |  |
 | Poland Central​​ |  |  | ✅ | ✅ |  |
-| Spain Central <sup>2</sup> |  | ✅ |  |  |  |
+| Spain Central <sup>1</sup> |  | ✅ |  |  |  |
 | Sweden Central​​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Switzerland North​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Switzerland West​ | ✅ | ✅ | ✅ | ✅ |  |
 | UK South​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | UK West​ ​|  |  | ✅ | ✅ |  |
 
-<sup>1</sup> This region has capacity constraints on the following tiers: S2, S3, L1, and L2.
-
-<sup>2</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
+<sup>1</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
 
 ### Middle East
 
@@ -108,7 +108,7 @@ You can create an Azure AI Search service in any of the following Azure public r
 | Korea South​​ |  |  | ✅ | ✅ |  |
 | Indonesia Central |  | ✅ |  |  |  |
 
-<sup>1</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
+<sup>1</sup> This region has capacity constraints on all tiers.
 
 ## Azure Government regions
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search地域サポート情報の更新"
}
```

### Explanation
この修正では、Azure AI Searchの地域サポートに関するドキュメントが更新されました。具体的には、地域ごとのキャパシティ制約に関する情報が明確にされました。特に、「スペイン中央」および「韓国南部」について、キャパシティ制約があることを示す注釈が追加され、ユーザーに対する注意喚起が強化されています。また、これに伴い、注釈番号が変更され、内容が整理されました。この修正により、ユーザーはサービスの制限や利用可能な地域についてより理解しやすくなります。

## articles/search/tutorial-rag-build-solution-models.md{#item-6796c9}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: tutorial
 ms.custom: references_regions
-ms.date: 05/29/2025
+ms.date: 05/30/2025
 
 ---
 
@@ -99,15 +99,13 @@ This tutorial series uses the following models and model providers:
 
 You must have [**Cognitive Services OpenAI Contributor**]( /azure/ai-services/openai/how-to/role-based-access-control#cognitive-services-openai-contributor) or higher to deploy models in Azure OpenAI.
 
-1. Go to [Azure AI Foundry](https://ai.azure.com/).
+1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/).
 
-1. Select **Deployments** on the left menu.
+1. From the left pane, select **Model catalog**.
 
-1. Select **Deploy model** > **Deploy base model**.
+1. Select **text-embedding-3-large**, and then select **Use this model**.
 
-1. Select **text-embedding-3-large** from the dropdown list and confirm the selection.
-
-1. Specify a deployment name. We recommend "text-embedding-3-large".
+1. Specify a deployment name. We recommend **text-embedding-3-large**.
 
 1. Accept the defaults.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションモデル構築チュートリアルの更新"
}
```

### Explanation
この修正では、「RAGソリューションモデルを構築する」チュートリアルドキュメントが更新されました。主な変更点は、手順の言語が明確化され、ユーザーが操作をより理解しやすくなるように改善されています。具体的には、Azure AI Foundryへのサインインの手順と、モデルのデプロイ方法が明確にされました。これにより、ユーザーは操作をスムーズに進められるようになります。また、日付が2025年5月29日から5月30日に更新され、情報の最新性が保たれています。全体として、修正はユーザーエクスペリエンスの向上を目的としたものです。

## articles/search/vector-search-integrated-vectorization-ai-studio.md{#item-353fcc}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 05/08/2025
+ms.date: 05/30/2025
 ---
 
 # Use embedding models from Azure AI Foundry model catalog for integrated vectorization
@@ -49,15 +49,17 @@ For image embeddings:
 
 1. Open the [Azure AI Foundry model catalog](https://ai.azure.com/explore/models). Create a project if you don't have one already.
 
-1. Apply a filter to show just the embedding models. Under **Inference tasks**, select **Embeddings**:
+1. From the left pane, select **Model catalog**.
+
+1. Apply a filter to show just the embedding models. Under **Inference tasks**, select **Embeddings**.
 
    :::image type="content" source="media\vector-search-integrated-vectorization-ai-studio\ai-studio-catalog-embeddings-filter.png" lightbox="media\vector-search-integrated-vectorization-ai-studio\ai-studio-catalog-embeddings-filter.png" alt-text="Screenshot of the Azure AI Foundry model catalog page highlighting how to filter by embeddings models.":::
 
-1. Select a supported model, then select **Deploy**.
+1. Select a supported model, and then select **Use this model**.
 
-   :::image type="content" source="media\vector-search-integrated-vectorization-ai-studio\ai-studio-deploy-endpoint.png" lightbox="media\vector-search-integrated-vectorization-ai-studio\ai-studio-deploy-endpoint.png" alt-text="Screenshot of deploying an endpoint via the Azure AI Foundry model catalog.":::
+   :::image type="content" source="media\vector-search-integrated-vectorization-ai-studio\use-this-model.png" lightbox="media\vector-search-integrated-vectorization-ai-studio\use-this-model.png" alt-text="Screenshot of deploying a model via the Azure AI Foundry model catalog.":::
 
-1. Accept the defaults or modify as needed, and then select **Deploy**. The deployment details vary depending on which model you select. 
+1. Accept the defaults or modify as needed, and then select **Deploy**. The deployment details vary depending on which model you select.
 
 1. Wait for the model to finish deploying by monitoring the **Provisioning State**. It should change from "Provisioning" to "Updating" to "Succeeded". You might need to select **Refresh** every few minutes to see the status update.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "統合ベクトル化に関するAIスタジオガイドの更新"
}
```

### Explanation
この修正では、「統合ベクトル化におけるベクトル検索」のドキュメントが更新されました。主な変更点は、Azure AI Foundryのモデルカタログにおける手順がより明確になり、操作の説明が改善されたことです。特に、モデルの選択やデプロイに関する手順が整理され、「Use this model」という表現に変更されました。これにより、ユーザーはモデルをデプロイするプロセスをよりスムーズに理解できるようになります。また、日付が2025年5月8日から5月30日へと更新され、情報の正確性が維持されています。全体として、修正は利用者にとってのガイドラインの明確さを高めることを目的としています。


