---
date: '2025-09-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3a8933d...MicrosoftDocs:212d966
summary: このコード差分では、Azure のドキュメントに軽微なアップデートと新機能が追加されました。主要な変更点には、メタデータの日付更新、新しいSVG画像の追加、ガイドラインやチュートリアルの内容修正が含まれます。特に、エージェントリトリーバルのC#クイックスタートガイドにおいては、大規模な修正が行われ、最新の技術に対応した構成に刷新されました。全体として、この更新はユーザーがAzureの機能を最大限に活用できるようにするための重要な取り組みです。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3a8933d...MicrosoftDocs:212d966){target="_blank"}

<format>
# Highlights
このコード差分では、Azure のドキュメント内で多岐にわたる軽微なアップデートと新機能の追加が行われました。主要な変更点には、メタデータの日付更新、新しいSVG画像の追加、ガイドラインやチュートリアル内の内容修正が含まれます。特に、エージェントリトリーバルのC#クイックスタートガイドにおいては大規模な修正が加えられ、最新の技術を活かせる構成に刷新されました。

## New features
- 新たに`agent-to-agent-pipeline.svg`というSVG画像が追加され、エージェント間の通信を視覚的に表現しています。

## Breaking changes
- `agentic-retrieval-csharp.md`では、クイックスタートガイドに大幅な改訂が行われ、特にコードや使用方法の部分が最新の仕様に合わせて更新されました。

## Other updates
- ほとんどのドキュメントで日付の更新が行われ、最新情報に同期しています。
- エージェントリトリーバルのガイドラインで、他言語バージョン（C#、Python、REST）への参照がより明確に書き直されました。
- ベクトル検索に関連したチュートリアルで、重要なプロパティに対する説明が改善されました。

# Insights
最近行われた変更は、主にAzure のドキュメンテーションのアップデートに焦点を当てています。これらの更新は、ユーザーがより正確で信頼性の高い最新情報に基づいて技術を利用できるようにするために重要です。視覚的な資料の改善、ドキュメント内のガイドラインの強化、サンプルコードの最新化が主な議題でした。

特筆すべきは、エージェントリトリーバルのC#ガイドの大規模な変更です。新しい手法によるクエリ処理の流れが詳述されており、特に並行処理の仕様が強調されている点は、複雑なクエリに対応するための設計を理解するうえで役立ちます。

さらに、SVGファイルの利点は、特に高解像度での視覚的な明瞭さやスケーラビリティに寄与しており、ユーザーの学習体験を向上させています。日付の更新といった軽微な変更も、編集履歴を一貫して管理するために重要です。

全体として、この更新は、Azure のユーザーが機能を最大限に活用しやすくするための取り組みと位置づけられています。これは優れたドキュメント管理と最新テクノロジーの質の向上を示すものであり、ユーザーにより良い体験を提供するための重要なステップです。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-concept-intro.md](#item-bf9ed7) | minor update | 日付の更新: 概念の紹介 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-csharp.md](#item-f93ed3) | breaking change | エージェントリトリーバルのC#クイックスタートの大規模な修正 | modified | 483 | 497 | 980 | 
| [agentic-retrieval-java.md](#item-4e2c55) | minor update | Javaエージェントリトリーバルのクイックスタートの更新 | modified | 6 | 5 | 11 | 
| [agentic-retrieval-javascript.md](#item-715283) | minor update | JavaScriptエージェントリトリーバルのクイックスタートの更新 | modified | 5 | 5 | 10 | 
| [agentic-retrieval-typescript.md](#item-e6370b) | minor update | TypeScriptエージェントリトリーバルのクイックスタートの更新 | modified | 5 | 5 | 10 | 
| [index.yml](#item-c67121) | minor update | メタデータの日付の更新 | modified | 1 | 1 | 2 | 
| [agent-to-agent-pipeline.png](#item-9f1346) | minor update | 画像ファイルのメタデータの更新 | modified | 0 | 0 | 0 | 
| [agent-to-agent-pipeline.svg](#item-2fd4e1) | new feature | エージェントからエージェントへのパイプラインのSVG画像の追加 | added | 279 | 0 | 279 | 
| [samples-dotnet.md](#item-12f3fa) | minor update | C#サンプルドキュメントの更新 | modified | 20 | 20 | 40 | 
| [samples-java.md](#item-5992fd) | minor update | Javaサンプルドキュメントの更新 | modified | 5 | 5 | 10 | 
| [samples-javascript.md](#item-82e67e) | minor update | JavaScriptサンプルドキュメントの更新 | modified | 18 | 18 | 36 | 
| [samples-python.md](#item-d2bf09) | minor update | Pythonサンプルドキュメントの更新 | modified | 14 | 14 | 28 | 
| [samples-rest.md](#item-198ebc) | minor update | REST APIサンプルドキュメントの更新 | modified | 14 | 14 | 28 | 
| [search-agentic-retrieval-how-to-pipeline.md](#item-1ad1c3) | minor update | エージェントリトリーバルパイプラインの画像更新 | modified | 1 | 1 | 2 | 
| [search-indexer-field-mappings.md](#item-0e4628) | minor update | インデクサーフィールドマッピングドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [search-what-is-data-import.md](#item-d73ef5) | minor update | データインポートに関するドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [service-configure-firewall.md](#item-75be3f) | minor update | ファイアウォール設定に関するドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [service-create-private-endpoint.md](#item-65e817) | minor update | プライベートエンドポイント作成に関するドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [tutorial-csharp-deploy-static-web-app.md](#item-a2300f) | minor update | C# チュートリアルのドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [tutorial-csharp-overview.md](#item-57fa0d) | minor update | C# チュートリアルの概要ドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [tutorial-csharp-search-query-integration.md](#item-8ad6b5) | minor update | C# 検索クエリ統合チュートリアルのドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [tutorial-rag-build-solution-minimize-storage.md](#item-088ad8) | minor update | RAG構築ソリューションに関するチュートリアルの日付更新 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-storage-options.md](#item-ee1680) | minor update | ベクトル検索のストレージオプションに関するチュートリアルの内容更新 | modified | 13 | 13 | 26 | 
| [vector-search-how-to-truncate-dimensions.md](#item-8350a3) | minor update | 次元の切り捨てに関するチュートリアルの内容更新 | modified | 5 | 2 | 7 | 


# Modified Contents
## articles/search/cognitive-search-concept-intro.md{#item-bf9ed7}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 02/24/2025
+ms.date: 09/23/2025
 ms.update-cycle: 180-days
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新: 概念の紹介"
}
```

### Explanation
この変更は、`cognitive-search-concept-intro.md`ファイル内のメタデータにある日付を更新する内容です。具体的には、`ms.date`の値が2025年2月24日から2025年9月23日に変更されています。これは、ドキュメントの更新日を適切に反映させるためのマイナーな更新です。この変更は全体の機能やデータに大きな影響を与えるものではありませんが、情報の正確さを保つためには必要な修正です。

## articles/search/includes/quickstarts/agentic-retrieval-csharp.md{#item-f93ed3}

<details>
<summary>Diff</summary>
````diff
@@ -4,170 +4,145 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 08/28/2025
+ms.date: 09/23/2025
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
 
-In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-concept.md) to create a conversational search experience powered by large language models (LLMs) and your proprietary data. Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries in parallel, and extracts grounding data from documents indexed in Azure AI Search. The output is intended for integration with agentic and custom chat solutions.
+In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-concept.md) to create a conversational search experience powered by documents indexed in Azure AI Search and large language models (LLMs) from Azure OpenAI in Azure AI Foundry Models.
 
-Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
+A *knowledge agent* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the agent outputs raw content from your sources, but this quickstart uses the answer synthesis modality for natural-language answer generation.
 
-To get started with a Jupyter notebook instead, see the [Azure-Samples/azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) repository on GitHub.
+Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
 > [!TIP]
-> The C# version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST or Python version.
+> Want to get started right away? See the [azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) repository on GitHub.
 
 ## Prerequisites
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
 + An [Azure AI Search service](../../search-create-service-portal.md) on the Basic tier or higher with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
 
-+ An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects). You get an Azure AI Foundry resource (that you need for model deployments) when you create an Azure AI Foundry project.
++ An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects) and Azure AI Foundry resource. When you create a project, the resource is automatically created.
 
 + The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
 [!INCLUDE [Setup](./agentic-retrieval-setup.md)]
 
-## Setup
+## Set up the environment
 
-1. Create a new folder `quickstart-agentic-retrieval` to contain the application and open Visual Studio Code in that folder with the following command:
+To set up the console application for this quickstart:
 
-    ```shell
-    mkdir quickstart-agentic-retrieval && cd quickstart-agentic-retrieval
-    ```
+1. Create a folder named `quickstart-agentic-retrieval` to contain the application.
 
-1. Create a new console application with the following command:
+1. Open the folder in Visual Studio Code.
 
-    ```shell
-    dotnet new console
-    ```
+1. Select **Terminal** > **New Terminal**, and then run the following command to create a console application.
 
-1. Install the Azure AI Search client library ([Azure.Search.Documents](/dotnet/api/overview/azure/search.documents-readme)) for .NET with:
-
-    ```console
-    dotnet add package Azure.Search.Documents --version 11.7.0-beta.4
+    ```powershell
+    dotnet new console
     ```
 
-1. Install the Azure OpenAI client library ([Azure.AI.OpenAI](/dotnet/api/azure.ai.openai)) for .NET with:
+1. Install the [Azure AI Search client library](/dotnet/api/overview/azure/search.documents-readme) for .NET.
 
     ```console
-    dotnet add package Azure.AI.OpenAI --version 2.1.0
+    dotnet add package Azure.Search.Documents --version 11.7.0-beta.7
     ```
 
-1. Install the `dotenv` package to load environment variables from a `.env` file with:
+1. Install the `dotenv.net` package to load environment variables from a `.env` file.
 
     ```console
     dotnet add package dotenv.net
     ```
 
-1. For the **recommended** keyless authentication with Microsoft Entra ID, install the [Azure.Identity](https://www.nuget.org/packages/Azure.Identity) package with:
+1. For keyless authentication with Microsoft Entra ID, install the [Azure.Identity](https://www.nuget.org/packages/Azure.Identity) package.
 
     ```console
     dotnet add package Azure.Identity
     ```
 
-1. For the **recommended** keyless authentication with Microsoft Entra ID, sign in to Azure with the following command:
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Azure AI Foundry project.
 
     ```console
     az login
     ```
 
+## Run the code
 
-## Create the index and knowledge agent
+To create and run the agentic retrieval pipeline:
 
-1. Create a new file named `.env` in the `quickstart-agentic-retrieval` folder and add the following environment variables:
+1. Create a file named `.env` in the `quickstart-agentic-retrieval` folder.
 
-    ```plaintext
-    AZURE_OPENAI_ENDPOINT=https://<your-ai-foundry-resource-name>.openai.azure.com/
-    AZURE_OPENAI_GPT_DEPLOYMENT=gpt-4.1-mini
-    AZURE_SEARCH_ENDPOINT=https://<your-search-service-name>.search.windows.net
-    AZURE_SEARCH_INDEX_NAME=agentic-retrieval-sample
+1. Add the following environment variables to the `.env` file.
+
+    ```
+    SEARCH_ENDPOINT = PUT-YOUR-SEARCH-SERVICE-URL-HERE
+    AOAI_ENDPOINT = PUT-YOUR-AOAI-FOUNDRY-URL-HERE
     ```
 
-    Replace `<your-search-service-name>` and `<your-ai-foundry-resource-name>` with your actual Azure AI Search service name and Azure AI Foundry resource name.
+1. Set `SEARCH_ENDPOINT` and `AOAI_ENDPOINT` to the values you obtained in [Get endpoints](#get-endpoints).
 
-1. In *Program.cs*, paste the following code.
+1. Paste the following code into the `Program.cs` file.
 
     ```csharp
     using dotenv.net;
+    using System.Text.Json;
     using Azure.Identity;
+    using Azure.Search.Documents;
     using Azure.Search.Documents.Indexes;
     using Azure.Search.Documents.Indexes.Models;
-    using System.Net.Http;
-    using System.Text.Json;
-    using Azure.Search.Documents;
     using Azure.Search.Documents.Models;
     using Azure.Search.Documents.Agents;
     using Azure.Search.Documents.Agents.Models;
-    using Azure.AI.OpenAI;
-    using OpenAI.Chat;
     
     namespace AzureSearch.Quickstart
     {
         class Program
         {
             static async Task Main(string[] args)
             {
-                // Load environment variables from .env file
-                // Ensure you have a .env file in the same directory with the required variables.
+                // Load environment variables from the .env file
+                // Ensure your .env file is in the same directory with the required variables
                 DotEnv.Load();
     
-                string endpoint = Environment.GetEnvironmentVariable("AZURE_SEARCH_ENDPOINT") 
-                    ?? throw new InvalidOperationException("AZURE_SEARCH_ENDPOINT is not set.");
-                string azureOpenAIEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT") 
-                    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
-                
-                string azureOpenAIGptDeployment = "gpt-4.1-mini";
-                string azureOpenAIGptModel = "gpt-4.1-mini";
-                string azureOpenAIEmbeddingDeployment = "text-embedding-3-large";
-                string azureOpenAIEmbeddingModel = "text-embedding-3-large";
-                
-                string indexName = "earth_at_night";
-                string agentName = "earth-search-agent";
+                string searchEndpoint = Environment.GetEnvironmentVariable("SEARCH_ENDPOINT")
+                    ?? throw new InvalidOperationException("SEARCH_ENDPOINT isn't set.");
+                string aoaiEndpoint = Environment.GetEnvironmentVariable("AOAI_ENDPOINT")
+                    ?? throw new InvalidOperationException("AOAI_ENDPOINT isn't set.");
     
-                var credential = new DefaultAzureCredential();            
-                
-                // Define the fields for the index
+                string aoaiEmbeddingModel = "text-embedding-3-large";
+                string aoaiEmbeddingDeployment = "text-embedding-3-large";
+                string aoaiGptModel = "gpt-4.1-mini";
+                string aoaiGptDeployment = "gpt-4.1-mini";
+    
+                string indexName = "earth-at-night";
+                string knowledgeSourceName = "earth-knowledge-source";
+                string knowledgeAgentName = "earth-knowledge-agent";
+    
+                var credential = new DefaultAzureCredential();
+    
+                // Define fields for the index
                 var fields = new List<SearchField>
                 {
-                    new SimpleField("id", SearchFieldDataType.String) 
-                    { 
-                        IsKey = true, 
-                        IsFilterable = true, 
-                        IsSortable = true, 
-                        IsFacetable = true 
-                    },
-                    new SearchField("page_chunk", SearchFieldDataType.String) 
-                    { 
-                        IsFilterable = false, 
-                        IsSortable = false, 
-                        IsFacetable = false 
-                    },
-                    new SearchField("page_embedding_text_3_large", SearchFieldDataType.Collection(SearchFieldDataType.Single)) 
-                    { 
-                        VectorSearchDimensions = 3072, 
-                        VectorSearchProfileName = "hnsw_text_3_large" 
-                    },
-                    new SimpleField("page_number", SearchFieldDataType.Int32) 
-                    { 
-                        IsFilterable = true, 
-                        IsSortable = true, 
-                        IsFacetable = true 
-                    }
-                };// Define the vectorizer
+                    new SimpleField("id", SearchFieldDataType.String) { IsKey = true, IsFilterable = true, IsSortable = true, IsFacetable = true },
+                    new SearchField("page_chunk", SearchFieldDataType.String) { IsFilterable = false, IsSortable = false, IsFacetable = false },
+                    new SearchField("page_embedding_text_3_large", SearchFieldDataType.Collection(SearchFieldDataType.Single)) { VectorSearchDimensions = 3072, VectorSearchProfileName = "hnsw_text_3_large" },
+                    new SimpleField("page_number", SearchFieldDataType.Int32) { IsFilterable = true, IsSortable = true, IsFacetable = true }
+                };
+    
+                // Define a vectorizer
                 var vectorizer = new AzureOpenAIVectorizer(vectorizerName: "azure_openai_text_3_large")
                 {
                     Parameters = new AzureOpenAIVectorizerParameters
                     {
-                        ResourceUri = new Uri(azureOpenAIEndpoint),
-                        DeploymentName = azureOpenAIEmbeddingDeployment,
-                        ModelName = azureOpenAIEmbeddingModel
+                        ResourceUri = new Uri(aoaiEndpoint),
+                        DeploymentName = aoaiEmbeddingDeployment,
+                        ModelName = aoaiEmbeddingModel
                     }
                 };
     
-                // Define the vector search profile and algorithm
+                // Define a vector search profile and algorithm
                 var vectorSearch = new VectorSearch()
                 {
                     Profiles =
@@ -190,7 +165,7 @@ To get started with a Jupyter notebook instead, see the [Azure-Samples/azure-sea
                     }
                 };
     
-                // Define semantic configuration
+                // Define a semantic configuration
                 var semanticConfig = new SemanticConfiguration(
                     name: "semantic_config",
                     prioritizedFields: new SemanticPrioritizedFields
@@ -202,10 +177,7 @@ To get started with a Jupyter notebook instead, see the [Azure-Samples/azure-sea
                 var semanticSearch = new SemanticSearch()
                 {
                     DefaultConfigurationName = "semantic_config",
-                    Configurations =
-                    {
-                        semanticConfig
-                    }
+                    Configurations = { semanticConfig }
                 };
     
                 // Create the index
@@ -216,111 +188,124 @@ To get started with a Jupyter notebook instead, see the [Azure-Samples/azure-sea
                     SemanticSearch = semanticSearch
                 };
     
-                // Create the index client. Delete the index if it exists and then recreate it.
-                var indexClient = new SearchIndexClient(new Uri(endpoint), credential);
-                try
-                {
-                    await indexClient.DeleteIndexAsync(indexName);
-                    Console.WriteLine($"Index '{indexName}' deleted successfully (if it existed).");
-                }
-                catch (Exception ex)
-                {
-                    Console.WriteLine($"Index '{indexName}' could not be deleted or did not exist: {ex.Message}");
-                }            
+                // Create the index client, deleting and recreating the index if it exists
+                var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
                 await indexClient.CreateOrUpdateIndexAsync(index);
-                Console.WriteLine($"Index '{indexName}' created or updated successfully");
+                Console.WriteLine($"Index '{indexName}' created or updated successfully.");
     
-                // Download the documents from the GitHub URL
+                // Upload sample documents from the GitHub URL
                 string url = "https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json";
                 var httpClient = new HttpClient();
                 var response = await httpClient.GetAsync(url);
                 response.EnsureSuccessStatusCode();
                 var json = await response.Content.ReadAsStringAsync();
-    
                 var documents = JsonSerializer.Deserialize<List<Dictionary<string, object>>>(json);
-                var searchClient = new SearchClient(new Uri(endpoint), indexName, credential);
+                var searchClient = new SearchClient(new Uri(searchEndpoint), indexName, credential);
                 var searchIndexingBufferedSender = new SearchIndexingBufferedSender<Dictionary<string, object>>(
                     searchClient,
                     new SearchIndexingBufferedSenderOptions<Dictionary<string, object>>
                     {
                         KeyFieldAccessor = doc => doc["id"].ToString(),
                     }
-                );            
+                );
                 await searchIndexingBufferedSender.UploadDocumentsAsync(documents);
                 await searchIndexingBufferedSender.FlushAsync();
-                Console.WriteLine($"Documents uploaded to index '{indexName}'");
+                Console.WriteLine($"Documents uploaded to index '{indexName}' successfully.");
+    
+                // Create a knowledge source
+                var indexKnowledgeSource = new SearchIndexKnowledgeSource(
+                    name: knowledgeSourceName,
+                    searchIndexParameters: new SearchIndexKnowledgeSourceParameters(searchIndexName: indexName)
+                    {
+                        SourceDataSelect = "id,page_chunk,page_number"
+                    }
+                );
+                await indexClient.CreateOrUpdateKnowledgeSourceAsync(indexKnowledgeSource);
+                Console.WriteLine($"Knowledge source '{knowledgeSourceName}' created or updated successfully.");
     
+                // Create a knowledge agent
                 var openAiParameters = new AzureOpenAIVectorizerParameters
                 {
-                    ResourceUri = new Uri(azureOpenAIEndpoint),
-                    DeploymentName = azureOpenAIGptDeployment,
-                    ModelName = azureOpenAIGptModel
+                    ResourceUri = new Uri(aoaiEndpoint),
+                    DeploymentName = aoaiGptDeployment,
+                    ModelName = aoaiGptModel
                 };
     
                 var agentModel = new KnowledgeAgentAzureOpenAIModel(azureOpenAIParameters: openAiParameters);
-    
-                var targetIndex = new KnowledgeAgentTargetIndex(indexName)
+                var outputConfig = new KnowledgeAgentOutputConfiguration
                 {
-                    DefaultRerankerThreshold = 2.5f
-                };            
-                // Create the knowledge agent
+                    Modality = KnowledgeAgentOutputConfigurationModality.AnswerSynthesis,
+                    IncludeActivity = true
+                };
+    
                 var agent = new KnowledgeAgent(
-                    name: agentName,
+                    name: knowledgeAgentName,
                     models: new[] { agentModel },
-                    targetIndexes: new[] { targetIndex });
-                await indexClient.CreateOrUpdateKnowledgeAgentAsync(agent);
-                Console.WriteLine($"Search agent '{agentName}' created or updated successfully");
+                    knowledgeSources: new KnowledgeSourceReference[] {
+                    new KnowledgeSourceReference(knowledgeSourceName) {
+                            IncludeReferences = true,
+                            IncludeReferenceSourceData = true,
+                            RerankerThreshold = (float?)2.5
+                        }
+                    }
+                )
     
-                string instructions = @"
-                A Q&A agent that can answer questions about the Earth at night.
-                Sources have a JSON format with a ref_id that must be cited in the answer.
-                If you do not have the answer, respond with ""I don't know"".
-                ";
+                {
+                    OutputConfiguration = outputConfig
+                };
+    
+                await indexClient.CreateOrUpdateKnowledgeAgentAsync(agent);
+                Console.WriteLine($"Knowledge agent '{knowledgeAgentName}' created or updated successfully.");
     
-                var messages = new List<Dictionary<string, object>>
+                // Set up messages
+                string instructions = @"A Q&A agent that can answer questions about the Earth at night.
+                If you don't have the answer, respond with ""I don't know"".";
+
+                var messages = new List<Dictionary<string, string>>
                 {
-                    new Dictionary<string, object>
+                    new Dictionary<string, string>
                     {
                         { "role", "system" },
                         { "content", instructions }
                     }
-                };            
+                };
+    
+                // Use agentic retrieval to fetch results
                 var agentClient = new KnowledgeAgentRetrievalClient(
-                    endpoint: new Uri(endpoint),
-                    agentName: agentName,
+                    endpoint: new Uri(searchEndpoint),
+                    agentName: knowledgeAgentName,
                     tokenCredential: new DefaultAzureCredential()
                 );
     
-                messages.Add(new Dictionary<string, object>
+                messages.Add(new Dictionary<string, string>
                 {
                     { "role", "user" },
-                    { "content", @"
-                    Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown?
-                    Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?
-                    " }
-                });            
+                    { "content", @"Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown?
+                    Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?" }
+                });
+    
                 var retrievalResult = await agentClient.RetrieveAsync(
                     retrievalRequest: new KnowledgeAgentRetrievalRequest(
                         messages: messages
-                            .Where(message => message["role"].ToString() != "system")
-                            .Select(message => new KnowledgeAgentMessage(
-                                role: message["role"].ToString(),
-                                content: new[] { new KnowledgeAgentMessageTextContent(message["content"].ToString()) }))
+                            .Where(message => message["role"] != "system")
+                            .Select(
+                                message => new KnowledgeAgentMessage(content: new[] { new KnowledgeAgentMessageTextContent(message["content"]) }) { Role = message["role"] }
+                            )
                             .ToList()
                     )
-                    {
-                        TargetIndexParams = { new KnowledgeAgentIndexParams { IndexName = indexName, RerankerThreshold = 2.5f } }
-                    }
-                );            
-                messages.Add(new Dictionary<string, object>
+                );
+    
+                messages.Add(new Dictionary<string, string>
                 {
                     { "role", "assistant" },
                     { "content", (retrievalResult.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text }
                 });
     
+                // Print the response, activity, and results
+                Console.WriteLine("Response:");
                 Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text);
     
-                Console.WriteLine("Activities:");
+                Console.WriteLine("Activity:");
                 foreach (var activity in retrievalResult.Value.Activity)
                 {
                     Console.WriteLine($"Activity Type: {activity.GetType().Name}");
@@ -332,7 +317,7 @@ To get started with a Jupyter notebook instead, see the [Azure-Samples/azure-sea
                     Console.WriteLine(activityJson);
                 }
     
-                Console.WriteLine("Results");
+                Console.WriteLine("Results:");
                 foreach (var reference in retrievalResult.Value.References)
                 {
                     Console.WriteLine($"Reference Type: {reference.GetType().Name}");
@@ -341,303 +326,306 @@ To get started with a Jupyter notebook instead, see the [Azure-Samples/azure-sea
                         reference.GetType(),
                         new JsonSerializerOptions { WriteIndented = true }
                     );
-                    Console.WriteLine(referenceJson);            }
-    
-                AzureOpenAIClient azureClient = new(
-                    new Uri(azureOpenAIEndpoint),
-                    new DefaultAzureCredential());
-                ChatClient chatClient = azureClient.GetChatClient(azureOpenAIGptDeployment);
+                    Console.WriteLine(referenceJson);
+                }
     
-                List<ChatMessage> chatMessages = messages
-                    .Select<Dictionary<string, object>, ChatMessage>(m => m["role"].ToString() switch
-                    {
-                        "user" => new UserChatMessage(m["content"].ToString()),
-                        "assistant" => new AssistantChatMessage(m["content"].ToString()),
-                        "system" => new SystemChatMessage(m["content"].ToString()),
-                        _ => null
-                    })                
-                    .Where(m => m != null)
-                    .ToList();
-    
-                var result = await chatClient.CompleteChatAsync(chatMessages);
-                Console.WriteLine($"[ASSISTANT]: {result.Value.Content[0].Text.Replace(".", "\n")}");
-    
-                messages.Add(new Dictionary<string, object>
+                // Continue the conversation
+                messages.Add(new Dictionary<string, string>
                 {
                     { "role", "user" },
-                    { "content", "How do I find lava at night?" }            
+                    { "content", "How do I find lava at night?" }
                 });
     
-                var retrievalResult2 = await agentClient.RetrieveAsync(
+                retrievalResult = await agentClient.RetrieveAsync(
                     retrievalRequest: new KnowledgeAgentRetrievalRequest(
                         messages: messages
-                            .Where(message => message["role"].ToString() != "system")
-                            .Select(message => new KnowledgeAgentMessage(
-                                role: message["role"].ToString(),
-                                content: new[] { new KnowledgeAgentMessageTextContent(message["content"].ToString()) }))
+                            .Where(message => message["role"] != "system")
+                            .Select(
+                                message => new KnowledgeAgentMessage(content: new[] { new KnowledgeAgentMessageTextContent(message["content"]) }) { Role = message["role"] }
+                            )
                             .ToList()
                     )
-                    {
-                        TargetIndexParams = { new KnowledgeAgentIndexParams { IndexName = indexName, RerankerThreshold = 2.5f } }
-                    }
                 );
     
-                messages.Add(new Dictionary<string, object>
+                messages.Add(new Dictionary<string, string>
                 {
                     { "role", "assistant" },
-                    { "content", (retrievalResult2.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text }
+                    { "content", (retrievalResult.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text }
                 });
+        
+                // Print the new response, activity, and results
+                Console.WriteLine("Response:");
+                Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text);
     
-                Console.WriteLine((retrievalResult2.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text);
-    
-                Console.WriteLine("Activities:");
-                foreach (var activity in retrievalResult2.Value.Activity)
+                Console.WriteLine("Activity:");
+                foreach (var activity in retrievalResult.Value.Activity)
                 {
                     Console.WriteLine($"Activity Type: {activity.GetType().Name}");
-                    string activityJson2 = JsonSerializer.Serialize(
+                    string activityJson = JsonSerializer.Serialize(
                         activity,
                         activity.GetType(),
                         new JsonSerializerOptions { WriteIndented = true }
                     );
-                    Console.WriteLine(activityJson2);
+                    Console.WriteLine(activityJson);
                 }
     
-                Console.WriteLine("Results");
-                foreach (var reference in retrievalResult2.Value.References)
+                Console.WriteLine("Results:");
+                foreach (var reference in retrievalResult.Value.References)
                 {
                     Console.WriteLine($"Reference Type: {reference.GetType().Name}");
-                    string referenceJson2 = JsonSerializer.Serialize(
+                    string referenceJson = JsonSerializer.Serialize(
                         reference,
                         reference.GetType(),
                         new JsonSerializerOptions { WriteIndented = true }
                     );
-                    Console.WriteLine(referenceJson2);
+                    Console.WriteLine(referenceJson);
                 }
     
-                List<ChatMessage> chatMessages2 = messages
-                    .Select<Dictionary<string, object>, ChatMessage>(m => m["role"].ToString() switch
-                    {
-                        "user" => new UserChatMessage(m["content"].ToString()),
-                        "assistant" => new AssistantChatMessage(m["content"].ToString()),
-                        "system" => new SystemChatMessage(m["content"].ToString()),
-                        _ => null
-                    })                
-                    .Where(m => m != null)
-                    .ToList();
-    
-                var result2 = await chatClient.CompleteChatAsync(chatMessages2);
-                Console.WriteLine($"[ASSISTANT]: {result2.Value.Content[0].Text.Replace(".", "\n")}");
-    
-                await indexClient.DeleteKnowledgeAgentAsync(agentName);
-                System.Console.WriteLine($"Search agent '{agentName}' deleted successfully");
-    
-                await indexClient.DeleteIndexAsync(indexName);            
-                System.Console.WriteLine($"Index '{indexName}' deleted successfully");
+                // Clean up resources
+                await indexClient.DeleteKnowledgeAgentAsync(knowledgeAgentName);
+                Console.WriteLine($"Knowledge agent '{knowledgeAgentName}' deleted successfully.");
+                
+                await indexClient.DeleteKnowledgeSourceAsync(knowledgeSourceName);
+                Console.WriteLine($"Knowledge source '{knowledgeSourceName}' deleted successfully.");
+    
+                await indexClient.DeleteIndexAsync(indexName);
+                Console.WriteLine($"Index '{indexName}' deleted successfully.");
             }
         }
     }
     ```
 
-1. Build and run the application with the following command:
+1. Build and run the application.
 
     ```shell
     dotnet run
     ```
 
-## Output
+### Output
 
-The output of the application should look similar to the following:
+The output of the application should be similar to the following:
 
-```plaintext
-Index 'earth_at_night' deleted successfully (if it existed).
-Index 'earth_at_night' created or updated successfully
-Documents uploaded to index 'earth_at_night'
-Search agent 'earth-search-agent' created or updated successfully
-[]
-Activities:
-Activity Type: KnowledgeAgentModelQueryPlanningActivityRecord
+```
+Index 'earth-at-night' created or updated successfully.
+Documents uploaded to index 'earth-at-night' successfully.
+Knowledge source 'earth-knowledge-source' created or updated successfully.
+Knowledge agent 'earth-knowledge-agent' created or updated successfully.
+Response:
+Suburban belts display larger December brightening than urban cores because holiday lights increase most dramatically in the suburbs and outskirts of major cities, where there is more yard space and a prevalence of single-family homes. Central urban areas, despite having higher absolute light levels, do not see as large an increase in lighting but still experience a brightening of 20 to 30 percent during the holidays [ref_id:2][ref_id:7].
+
+The Phoenix nighttime street grid is sharply visible from space because the metropolitan area is laid out along a regular grid of city blocks and streets, with street lighting clearly visible from low-Earth orbit. The grid pattern is especially evident at night, with major street grids oriented north-south and diagonal corridors like Grand Avenue cutting across cities. The urban grid encourages outward growth along city borders, with extensive surface streets and freeways linking multiple municipalities. In contrast, large stretches of interstate highways between Midwestern cities remain comparatively dim because, although the interstate highways are major transportation corridors, the lighting along these highways is less intense and less continuous than the dense urban street lighting seen in Phoenix. Additionally, navigable rivers and less densely populated areas show less light, indicating that the brightness corresponds closely to urban density and street lighting patterns rather than just the presence of transportation routes [ref_id:0][ref_id:1][ref_id:4].
+Activity:
+Activity type: KnowledgeAgentModelQueryPlanningActivityRecord
 {
-  "InputTokens": 1265,
-  "OutputTokens": 536,
-  "ElapsedMs": null,
-  "Id": 0
+  "InputTokens": 2062,
+  "OutputTokens": 121,
+  "Id": 0,
+  "ElapsedMs": 2435
 }
-Activity Type: KnowledgeAgentSearchActivityRecord
+Activity type: KnowledgeAgentSearchIndexActivityRecord
 {
-  "TargetIndex": "earth_at_night",
-  "Query": {
-    "Search": "Reasons for larger December brightening in suburban belts compared to urban cores despite higher absolute light levels downtown",
+  "SearchIndexArguments": {
+    "Search": "Reasons for larger December brightening in suburban belts compared to urban cores despite higher downtown light levels",      
     "Filter": null
   },
-  "QueryTime": "2025-06-19T14:02:27.504+00:00",
-  "Count": 0,
-  "ElapsedMs": 768,
-  "Id": 1
+  "KnowledgeSourceName": "earth-knowledge-source",
+  "QueryTime": "2025-09-22T15:54:56.528+00:00",
+  "Count": 4,
+  "Id": 1,
+  "ElapsedMs": 1921
 }
-Activity Type: KnowledgeAgentSearchActivityRecord
+Activity type: KnowledgeAgentSearchIndexActivityRecord
 {
-  "TargetIndex": "earth_at_night",
-  "Query": {
-    "Search": "Why is the Phoenix nighttime street grid sharply visible from space while large stretches of interstate between Midwestern cities are comparatively dim?",
+  "SearchIndexArguments": {
+    "Search": "Factors making Phoenix nighttime street grid sharply visible from space",
     "Filter": null
   },
-  "QueryTime": "2025-06-19T14:02:27.817+00:00",
-  "Count": 0,
-  "ElapsedMs": 292,
-  "Id": 2
+  "KnowledgeSourceName": "earth-knowledge-source",
+  "QueryTime": "2025-09-22T15:55:06.991+00:00",
+  "Count": 5,
+  "Id": 2,
+  "ElapsedMs": 10451
 }
-Activity Type: KnowledgeAgentSemanticRankerActivityRecord
+Activity type: KnowledgeAgentSearchIndexActivityRecord
 {
-  "InputTokens": 52609,
-  "ElapsedMs": null,
-  "Id": 3
+  "SearchIndexArguments": {
+    "Search": "Reasons why large stretches of interstate between Midwestern cities appear comparatively dim at night from space",
+    "Filter": null
+  },
+  "KnowledgeSourceName": "earth-knowledge-source",
+  "QueryTime": "2025-09-22T15:55:07.504+00:00",
+  "Count": 13,
+  "Id": 3,
+  "ElapsedMs": 512
 }
-Results
-[ASSISTANT]: The suburban belts display larger December brightening than urban cores because suburban areas often have more residential lighting that increases during December holidays, such as decorative lights, leading to a noticeable rise in brightness
- In contrast, urban cores already have very high absolute light levels, so the relative increase from additional lighting is less significant
-
-
-Regarding Phoenix's nighttime street grid visibility from space, it is sharply visible because the city has a distinctive, well-lit, and uniformly spaced street grid pattern that emits consistent light
- In contrast, large stretches of interstate highways between Midwestern cities remain comparatively dim because highways have less continuous lighting, with fewer lights spread over longer distances, making them less prominent from space [ref_id: night_earth_study_2021]
-
-[{"ref_id":0,"content":"<!-- PageHeader=\"Volcanoes\" -->\n\n## Volcanoes\n\n### The Infrared Glows of Kilauea's Lava Flows—Hawaii\n\nIn early May 2018, an eruption on Hawaii's Kilauea volcano began to unfold. The eruption took a dangerous turn on May 3, 2018, when new fissures opened in the residential neighborhood of Leilani Estates. During the summer-long eruptive event, other fissures emerged along the East Rift Zone. Lava from vents along the rift zone flowed downslope, reaching the ocean in several areas, and filling in Kapoho Bay.\n\nA time series of Landsat 8 imagery shows the progression of the lava flows from May 16 to August 13. The night view combines thermal, shortwave infrared, and near-infrared wavelengths to tease out the very hot lava (bright white), cooling lava (red), and lava flows obstructed by clouds (purple).\n\n#### Figure: Location of Kilauea Volcano, Hawaii\n\nA globe is shown centered on North America, with a marker placed in the Pacific Ocean indicating the location of Hawaii, to the southwest of the mainland United States.\n\n<!-- PageFooter=\"Earth at Night\" -->\n<!-- PageNumber=\"44\" -->"},{"ref_id":1,"content":"<!-- PageHeader=\"Volcanoes\" -->\n\n### Nighttime Glow at Mount Etna - Italy\n\nAt about 2:30 a.m. local time on March 16, 2017, the VIIRS DNB on the Suomi NPP satellite captured this nighttime image of lava flowing on Mount Etna in Sicily, Italy. Etna is one of the world's most active volcanoes.\n\n#### Figure: Location of Mount Etna\nA world globe is depicted, with a marker indicating the location of Mount Etna in Sicily, Italy, in southern Europe near the center of the Mediterranean Sea.\n\n<!-- PageFooter=\"Earth at Night\" -->\n<!-- PageNumber=\"48\" -->"},{"ref_id":2,"content":"For the first time in perhaps a decade, Mount Etna experienced a \"flank eruption\"—erupting from its side instead of its summit—on December 24, 2018. The activity was accompanied by 130 earthquakes occurring over three hours that morning. Mount Etna, Europe’s most active volcano, has seen periodic activity on this part of the mountain since 2013. The Operational Land Imager (OLI) on the Landsat 8 satellite acquired the main image of Mount Etna on December 28, 2018.\n\nThe inset image highlights the active vent and thermal infrared signature from lava flows, which can be seen near the newly formed fissure on the southeastern side of the volcano. The inset was created with data from OLI and the Thermal Infrared Sensor (TIRS) on Landsat 8. Ash spewing from the fissure cloaked adjacent villages and delayed aircraft from landing at the nearby Catania airport. Earthquakes occurred in the subsequent days after the initial eruption and displaced hundreds of people from their homes.\n\nFor nighttime images of Mount Etna’s March 2017 eruption, see pages 48–51.\n\n---\n\n### Hazards of Volcanic Ash Plumes and Satellite Observation\n\nWith the help of moonlight, satellite instruments can track volcanic ash plumes, which present significant hazards to airplanes in flight. The volcanic ash—composed of tiny pieces of glass and rock—is abrasive to engine turbine blades, and can melt on the blades and other engine parts, causing damage and even engine stalls. This poses a danger to both the plane’s integrity and passenger safety. Volcanic ash also reduces visibility for pilots and can cause etching of windshields, further reducing pilots’ ability to see. Nightlight images can be combined with thermal images to provide a more complete view of volcanic activity on Earth’s surface.\n\nThe VIIRS Day/Night Band (DNB) on polar-orbiting satellites uses faint light sources such as moonlight, airglow (the atmosphere’s self-illumination through chemical reactions), zodiacal light (sunlight scattered by interplanetary dust), and starlight from the Milky Way. Using these dim light sources, the DNB can detect changes in clouds, snow cover, and sea ice:\n\n#### Table: Light Sources Used by VIIRS DNB\n\n| Light Source         | Description                                                        
-          |\n|----------------------|------------------------------------------------------------------------------|\n| Moonlight            | Reflected sunlight from the Moon, illuminating Earth's surface at night      |\n| Airglow              | Atmospheric self-illumination from chemical reactions                        |\n| Zodiacal Light       | Sunlight scattered by interplanetary dust                                    |\n| Starlight/Milky Way  | Faint illumination provided by stars in the Milky Way                        |\n\nGeostationary Operational Environmental Satellites (GOES), managed by NOAA, orbit over Earth’s equator and offer uninterrupted observations of North America. High-latitude areas such as Alaska benefit from polar-orbiting satellites like Suomi NPP, which provide overlapping coverage at the poles, enabling more data collection in these regions. During polar darkness (winter months), VIIRS DNB data allow scientists to:\n\n- Observe sea ice formation\n- Monitor snow cover extent at the highest latitudes\n- Detect open water for ship navigation\n\n#### Table: Satellite Coverage Overview\n\n| Satellite Type          | Orbit           | Coverage Area         | Special Utility                              |\n|------------------------|-----------------|----------------------|----------------------------------------------|\n| GOES              
-     | Geostationary   | Equatorial/North America | Continuous regional monitoring              |\n| Polar-Orbiting (e.g., Suomi NPP) | Polar-orbiting    | Poles/high latitudes      | Overlapping passes; useful during polar night|\n\n---\n\n### Weather Forecasting and Nightlight Data\n\nThe use of nightlight data by weather forecasters is growing as the VIIRS instrument enables observation of clouds at night illuminated by sources such as moonlight and lightning. Scientists use these data to study the nighttime behavior of weather systems, including severe storms, which can develop and strike populous areas at night as well as during the day. Combined with thermal data, visible nightlight data allow the detection of clouds at various heights in the atmosphere, such as dense marine fog. This capability enables weather forecasters to issue marine advisories with higher confidence, leading to greater utility. (See \"Marine Layer Clouds—California\" on page 56.)\n\nIn this section of the book, you will see how nightlight data are used to observe nature’s spectacular light shows across a wide range of sources.\n\n---\n\n#### Notable Data from Mount Etna Flank Eruption (December 2018)\n\n| Event/Observation                  | Details                                        
-                            |\n|-------------------------------------|----------------------------------------------------------------------------|\n| Date of Flank Eruption              | December 24, 2018                                                          |\n| Number of Earthquakes               | 130 earthquakes within 3 hours                                              |\n| Image Acquisition                   | December 28, 2018 by Landsat 8 OLI                                   
-      |\n| Location of Eruption                | Southeastern side of Mount Etna                   
-                         |\n| Thermal Imaging Data                | From OLI and TIRS (Landsat 8), highlighting active vent and lava flows     |\n| Impact on Villages/Air Transport    | Ash covered villages; delayed aircraft at Catania airport                  |\n| Displacement                   
-     | Hundreds of residents displaced                                            |\n| Ongoing Seismic Activity            | Earthquakes continued after initial eruption                             
-  |\n\n---\n\n<!-- PageFooter=\"Earth at Night\" -->\n<!-- PageNumber=\"30\" -->"},{"ref_id":3,"content":"# Volcanoes\n\n---\n\n### Mount Etna Erupts - Italy\n\nThe highly active Mount Etna in Italy sent red lava rolling down its flank on March 19, 2017. An astronaut onboard the ISS took the photograph below of the volcano and its environs that night. City lights surround the mostly dark volcanic area.\n\n---\n\n#### Figure 1: Location of Mount Etna, Italy\n\nA world map highlighting the location of Mount Etna in southern Italy. The marker indicates its geographic placement on the east coast of Sicily, Italy, in the Mediterranean region, south of mainland Europe and north of northern Africa.\n\n---\n\n#### Figure 2: Nighttime View of Mount Etna's Eruption and Surrounding Cities\n\nThis is a nighttime satellite image taken on March 19, 2017, showing the eruption of Mount Etna (southeastern cone) with visible bright red and orange coloring indicating flowing lava from a lateral vent. The surrounding areas are illuminated by city lights, with the following geographic references labeled:\n\n| Location        | Position in Image         | Visible Characteristics             
-       |\n|-----------------|--------------------------|--------------------------------------------|\n| Mt. Etna (southeastern cone) | Top center-left | Bright red/orange lava flow                |\n| Lateral vent    | Left of the volcano       | Faint red/orange flow extending outwards   |\n| Resort          | Below the volcano, to the left   | Small cluster of lights                    |\n| Giarre          | Top right                 | Bright cluster of city lights              |\n| Acireale        | Center right              | Large, bright area of city lights          |\n| Biancavilla     | Bottom left               | Smaller cluster of city lights             |\n\nAn arrow pointing north is shown on the image for orientation.\n\n---\n\n<!-- Earth at Night Page Footer -->\n<!-- Page Number: 50 -->"},{"ref_id":4,"content":"# Volcanoes\n\n## Figure: Satellite Image of Sicily and Mount Etna Lava, March 16, 2017\n\nThe annotated satellite image below shows the island of Sicily and the surrounding region at night, highlighting city lights and volcanic activity.\n\n**Description:**\n\n- **Date of image:** March 16, 2017\n- **Geographical locations labeled:**\n    - Major cities: Palermo (northwest Sicily), Marsala (western Sicily), Catania (eastern Sicily)\n    - Significant feature: Mount Etna, labeled with an adjacent \"hot lava\" region showing the glow from active lava flows\n    - Surrounding water body: Mediterranean Sea\n    - Island: Malta to the south of Sicily\n- **Other details:** \n    - The image is shown at night, with bright spots indicating city lights.\n    - The position of \"hot lava\" near Mount Etna is distinctly visible as a bright spot different from other city lights, indicating volcanic activity.\n    - A scale bar is included showing a reference length of 50 km.\n    - North direction is indicated with an arrow.\n    - Cloud cover is visible in the southwest part of the image, partially obscuring the view near Marsala and Malta.\n\n**Summary of Features Visualized:**\n\n| Feature          | Description                 
-                          |\n|------------------|------------------------------------------------------|\n| Cities           | Bright clusters indicating locations: Palermo, Marsala, Catania |\n| Mount Etna       | Marked on the map, located on the eastern side of Sicily, with visible hot lava activity |\n| Malta            | Clearly visible to the south of Sicily               |\n| Water bodies     | Mediterranean Sea labeled                            |\n| Scale & Direction| 50 km scale bar and North indicator                  |\n| Date             | March 16, 2017                     
-                  |\n| Cloud Cover      | Visible in the lower left (southern) part of the image |\n\nThis figure demonstrates the visibility of volcanic activity at Mount Etna from space at night, distinguishing the light from hot lava against the background city lights of Sicily and Malta."},{"ref_id":5,"content":"## Nature's Light Shows\n\nAt night, with the light of the Sun removed, nature's brilliant glow from Earth's surface becomes visible to the naked eye from space. Some of Earth's most spectacular light shows are natural, like the aurora borealis, or Northern Lights, in the Northern Hemisphere (aurora australis, or Southern Lights, in the Southern Hemisphere). The auroras are natural electrical phenomena caused by charged particles that race from the Sun toward Earth, inducing chemical reactions in the upper atmosphere and creating the appearance of streamers of reddish or greenish light in the sky, usually near the northern or southern magnetic pole. Other natural lights can indicate danger, like a raging forest fire encroaching on a city, town, or community, or lava spewing from an erupting volcano.\n\nWhatever the source, the ability of humans to monitor nature's light shows at night has practical applications for society. For example, tracking fires during nighttime hours allows for continuous monitoring and enhances our ability to protect humans and other animals, plants, and infrastructure. Combined with other data sources, our ability to observe the light of fires at night allows emergency managers to more efficiently and accurately issue warnings and evacuation orders and allows firefighting efforts to continue through the night. With enough moonlight (e.g., full-Moon phase), it's even possible to track the movement of smoke plumes at night, which can impact air quality, regardless of time of day.\n\nAnother natural source of light at night is emitted from glowing lava flows at the site of active volcanoes. Again, with enough moonlight, these dramatic scenes can be tracked and monitored for both scientific research and public safety.\n\n\n### Figure: The Northern Lights Viewed from Space\n\n**September 17, 2011**\n\nThis photo, taken from the International Space Station on September 17, 2011, shows a spectacular display of the aurora borealis (Northern Lights) as green and reddish light in the night sky above Earth. In the foreground, part of a Soyuz spacecraft is visible, silhouetted against the bright auroral light. The green glow is generated by energetic charged particles from the Sun interacting with Earth's upper atmosphere, exciting oxygen and nitrogen atoms, and producing characteristic colors. The image demonstrates the vividness and grandeur of natural night-time light phenomena as seen from orbit."}]
-Activities:
-Activity Type: KnowledgeAgentModelQueryPlanningActivityRecord
-{
-  "InputTokens": 1289,
-  "OutputTokens": 116,
-  "ElapsedMs": null,
-  "Id": 0
+Activity type: KnowledgeAgentSemanticRerankerActivityRecord
+{
+  "InputTokens": 68754,
+  "Id": 4,
+  "ElapsedMs": null
 }
-Activity Type: KnowledgeAgentSearchActivityRecord
+Activity type: KnowledgeAgentModelAnswerSynthesisActivityRecord
 {
-  "TargetIndex": "earth_at_night",
-  "Query": {
-    "Search": "How to locate lava flows at night?",
-    "Filter": null
+  "InputTokens": 7231,
+  "OutputTokens": 279,
+  "Id": 5,
+  "ElapsedMs": 6429
+}
+Results:
+Reference type: KnowledgeAgentSearchIndexReference
+{
+  "DocKey": "earth_at_night_508_page_104_verbalized",
+  "Id": "0",
+  "ActivitySource": 2,
+  "SourceData": {
+    "id": "earth_at_night_508_page_104_verbalized",
+    "page_chunk": "\u003C!-- PageHeader=\u0022Urban Structure\u0022 --\u003E\n\n### Location of Phoenix, Arizona\n\nThe image depicts a globe highlighting the location of Phoenix, Arizona, in the southwestern United States, marked with a blue pinpoint on the map of North America. Phoenix is situated in the central part of Arizona, which is in the southwestern region of the United States.\n\n---\n\n### Grid of City Blocks-Phoenix, Arizona\n\nLike many large urban areas of the central and western United States, the Phoenix metropolitan area is laid out along a regular grid of city blocks and streets. While visible during the day, this grid is most evident at night, when the pattern of street lighting is clearly visible from the low-Earth-orbit vantage point of the ISS.\n\nThis astronaut photograph, taken on March 16, 2013, includes parts of several cities in the metropolitan area, including Phoenix (image right), Glendale (center), and Peoria (left). While the major street grid is oriented north-south, the northwest-southeast oriented Grand Avenue cuts across the three cities at image center. Grand Avenue is a major transportation corridor through the western metropolitan area; the lighting patterns of large industrial and commercial properties are visible along its length. Other brightly lit properties include large shopping centers, strip malls, and gas stations, which tend to be located at the intersections of north-south and east-west trending streets.\n\nThe urban grid encourages growth outwards along a city\u0027s borders by providing optimal access to new real estate. Fueled by the adoption of widespread personal automobile use during the twentieth century, the Phoenix metropolitan area today includes 25 other municipalities (many of them largely suburban and residential) linked by a network of surface streets and freeways.\n\nWhile much of the land area highlighted in this image is urbanized, there are several noticeably dark areas. The Phoenix Mountains are largely public parks and recreational land. To the west, agricultural fields provide a sharp contrast to the lit streets of residential developments. The Salt River channel appears as a dark ribbon within the urban grid.\n\n\n\u003C!-- PageFooter=\u0022Earth at Night\u0022 --\u003E\n\u003C!-- PageNumber=\u002288\u0022 --\u003E",
+    "page_number": 104
   },
-  "QueryTime": "2025-06-19T14:02:44.67+00:00",
-  "Count": 6,
-  "ElapsedMs": 235,
-  "Id": 1
+  "RerankerScore": 2.6642752
 }
-Activity Type: KnowledgeAgentSemanticRankerActivityRecord
+Reference type: KnowledgeAgentSearchIndexReference
 {
-  "InputTokens": 24807,
-  "ElapsedMs": null,
-  "Id": 2
+  "DocKey": "earth_at_night_508_page_105_verbalized",
+  "Id": "3",
+  "ActivitySource": 2,
+  "SourceData": {
+    "id": "earth_at_night_508_page_105_verbalized",
+    "page_chunk": "# Urban Structure\n\n## March 16, 2013\n\n### Phoenix Metropolitan Area at Night\n\nThis figure presents a nighttime satellite view of the Phoenix metropolitan area, highlighting urban structure and transport corridors. City lights illuminate the layout of several cities and major thoroughfares.\n\n**Labeled Urban Features:**\n\n- **Phoenix:** Central and brightest area in the right-center of the image.\n- **Glendale:** Located to the west of Phoenix, this city is also brightly lit.\n- **Peoria:** Further northwest, this area is labeled and its illuminated grid is seen.\n- **Grand Avenue:** Clearly visible as a diagonal, brightly lit thoroughfare running from Phoenix through Glendale and Peoria.\n- **Salt River Channel:** Identified in the southeast portion, running through illuminated sections.\n- **Phoenix Mountains:** Dark, undeveloped region to the northeast of Phoenix.\n- **Agricultural Fields:** Southwestern corner of the image, grid patterns are visible but with much less illumination, indicating agricultural land use.\n\n**Additional Notes:**\n\n- The overall pattern shows a grid-like urban development typical of western U.S. cities, with scattered bright nodes at major intersections or city centers.\n- There is a clear transition from dense urban development to sparsely populated or agricultural land, particularly evident towards the bottom and left of the image.\n- The illuminated areas follow the existing road and street grids, showcasing the extensive spread of the metropolitan area.\n\n**Figure Description:**  \nA satellite nighttime image captured on March 16, 2013, showing Phoenix and surrounding areas (including Glendale and Peoria). Major landscape and infrastructural features, such as the Phoenix Mountains, Grand Avenue, the Salt River Channel, and agricultural fields, are labeled. The image reveals the extent of urbanization and the characteristic street grid illuminated by city lights.\n\n---\n\nPage 89",
+    "page_number": 105
+  },
+  "RerankerScore": 2.5905457
 }
-Results
-Reference Type: KnowledgeAgentAzureSearchDocReference
+... // Trimmed for brevity
+Response:
+Lava can be found at night by using satellite imagery that captures thermal infrared and near-infrared wavelengths, which highlight the heat emitted by active lava flows. For example, the Landsat 8 satellite's night view combines thermal, shortwave infrared, and near-infrared data to distinguish very hot lava (appearing bright white), cooling lava (red), and lava flows obscured by clouds (purple), as demonstrated in the monitoring of Kilauea's lava flows in Hawaii [ref_id:0]. Similarly, the Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS) on Landsat 8 have been used to detect the thermal infrared signature of lava flows during Mount Etna's flank eruption in Italy, highlighting active vents and lava flows at night [ref_id:1]. Additionally, the VIIRS Day/Night Band (DNB) on polar-orbiting satellites can detect faint light sources such as moonlight, which, combined with thermal data, allows for the observation of glowing lava flows at active volcanoes during nighttime [ref_id:1][ref_id:3]. Thus, by using satellite instruments sensitive to thermal and near-infrared wavelengths and leveraging natural illumination sources like moonlight, lava can be effectively located and monitored at night from space.
+Activity:
+Activity type: KnowledgeAgentModelQueryPlanningActivityRecord
 {
-  "DocKey": "earth_at_night_508_page_60_verbalized",
-  "SourceData": {},
-  "Id": "0",
-  "ActivitySource": 1
+  "InputTokens": 2357,
+  "OutputTokens": 88,
+  "Id": 0,
+  "ElapsedMs": 1917
 }
-Reference Type: KnowledgeAgentAzureSearchDocReference
+Activity type: KnowledgeAgentSearchIndexActivityRecord
 {
-  "DocKey": "earth_at_night_508_page_64_verbalized",
-  "SourceData": {},
-  "Id": "1",
-  "ActivitySource": 1
+  "SearchIndexArguments": {
+    "Search": "How to locate lava flows at night",
+    "Filter": null
+  },
+  "KnowledgeSourceName": "earth-knowledge-source",
+  "QueryTime": "2025-09-22T15:55:16.919+00:00",
+  "Count": 16,
+  "Id": 1,
+  "ElapsedMs": 433
 }
-Reference Type: KnowledgeAgentAzureSearchDocReference
+Activity type: KnowledgeAgentSearchIndexActivityRecord
 {
-  "DocKey": "earth_at_night_508_page_46_verbalized",
-  "SourceData": {},
-  "Id": "2",
-  "ActivitySource": 1
+  "SearchIndexArguments": {
+    "Search": "Methods for detecting lava at night",
+    "Filter": null
+  },
+  "KnowledgeSourceName": "earth-knowledge-source",
+  "QueryTime": "2025-09-22T15:55:17.389+00:00",
+  "Count": 13,
+  "Id": 2,
+  "ElapsedMs": 468
 }
-Reference Type: KnowledgeAgentAzureSearchDocReference
+Activity type: KnowledgeAgentSearchIndexActivityRecord
 {
-  "DocKey": "earth_at_night_508_page_66_verbalized",
-  "SourceData": {},
-  "Id": "3",
-  "ActivitySource": 1
+  "SearchIndexArguments": {
+    "Search": "Safety tips for finding lava at night",
+    "Filter": null
+  },
+  "KnowledgeSourceName": "earth-knowledge-source",
+  "QueryTime": "2025-09-22T15:55:17.801+00:00",
+  "Count": 3,
+  "Id": 3,
+  "ElapsedMs": 411
 }
-Reference Type: KnowledgeAgentAzureSearchDocReference
+Activity type: KnowledgeAgentSemanticRerankerActivityRecord
 {
-  "DocKey": "earth_at_night_508_page_65_verbalized",
-  "SourceData": {},
-  "Id": "4",
-  "ActivitySource": 1
+  "InputTokens": 67218,
+  "Id": 4,
+  "ElapsedMs": null
 }
-Reference Type: KnowledgeAgentAzureSearchDocReference
+Activity type: KnowledgeAgentModelAnswerSynthesisActivityRecord
 {
-  "DocKey": "earth_at_night_508_page_44_verbalized",
-  "SourceData": {},
-  "Id": "5",
-  "ActivitySource": 1
+  "InputTokens": 7345,
+  "OutputTokens": 267,
+  "Id": 5,
+  "ElapsedMs": 6044
 }
-[ASSISTANT]: You can find lava at night primarily by using satellite imagery that captures the thermal and visible light emissions from active volcanoes
- Very hot lava emits strong infrared radiation and glows visibly, which can be detected from space, especially when combined with moonlight or other faint light sources
- For example, satellites like Landsat 8 and VIIRS on Suomi NPP have captured nighttime images of lava flows on volcanoes such as Kilauea in Hawaii and Mount Etna in Italy
- These images show bright white-hot areas indicating very hot lava and reddish areas for cooling lava flows (ref_id 0, 1, 3, 4)
-
-
-Lava glows visibly due to its intense heat, which makes it stand out even at night against the darkness and city lights
- Nighttime satellite images combine thermal infrared wavelengths and near-infrared to distinguish active lava from surrounding cooler ground
- Monitoring these nighttime glows allows scientists to study volcanic activity and also helps with hazard assessment
-
-
-So, at night, the best way to find lava is through thermal and infrared satellite imagery that detects the glow and heat signatures of lava flows from active volcanoes
-
-
-References: 0, 1, 3, 4
-Search agent 'earth-search-agent' deleted successfully
-Index 'earth_at_night' deleted successfully
+Results:
+Reference type: KnowledgeAgentSearchIndexReference
+{
+  "DocKey": "earth_at_night_508_page_60_verbalized",
+  "Id": "0",
+  "ActivitySource": 1,
+  "SourceData": {
+    "id": "earth_at_night_508_page_60_verbalized",
+    "page_chunk": "\u003C!-- PageHeader=\u0022Volcanoes\u0022 --\u003E\n\n## Volcanoes\n\n### The Infrared Glows of Kilauea\u0027s Lava Flows\u2014Hawaii\n\nIn early May 2018, an eruption on Hawaii\u0027s Kilauea volcano began to unfold. The eruption took a dangerous turn on May 3, 2018, when new fissures opened in the residential neighborhood of Leilani Estates. During the summer-long eruptive event, other fissures emerged along the East Rift Zone. Lava from vents along the rift zone flowed downslope, reaching the ocean in several areas, and filling in Kapoho Bay.\n\nA time series of Landsat 8 imagery shows the progression of the lava flows from May 16 to August 13. The night view combines thermal, shortwave infrared, and near-infrared wavelengths to tease out the very hot lava (bright white), cooling lava (red), and lava flows obstructed by clouds (purple).\n\n#### Figure: Location of Kilauea Volcano, Hawaii\n\nA globe is shown centered on North America, with a marker placed in the Pacific Ocean indicating the location of Hawaii, to the southwest of the mainland United States.\n\n\u003C!-- PageFooter=\u0022Earth at Night\u0022 --\u003E\n\u003C!-- PageNumber=\u002244\u0022 --\u003E",
+    "page_number": 60
+  },
+  "RerankerScore": 2.779123
+}
+Reference type: KnowledgeAgentSearchIndexReference
+{
+  "DocKey": "earth_at_night_508_page_64_verbalized",
+  "Id": "2",
+  "ActivitySource": 1,
+  "SourceData": {
+    "id": "earth_at_night_508_page_64_verbalized",
+    "page_chunk": "\u003C!-- PageHeader=\u0022Volcanoes\u0022 --\u003E\n\n### Nighttime Glow at Mount Etna - Italy\n\nAt about 2:30 a.m. local time on March 16, 2017, the VIIRS DNB on the Suomi NPP satellite captured this nighttime image of lava flowing on Mount Etna in Sicily, Italy. Etna is one of the world\u0027s most active volcanoes.\n\n#### Figure: Location of Mount Etna\nA world globe is depicted, with a marker indicating the location of Mount Etna in Sicily, Italy, in southern Europe near the center of the Mediterranean Sea.\n\n\u003C!-- PageFooter=\u0022Earth at Night\u0022 --\u003E\n\u003C!-- PageNumber=\u002248\u0022 --\u003E",
+    "page_number": 64
+  },
+  "RerankerScore": 2.7684891
+}
+... // Trimmed for brevity
+Knowledge agent 'earth-knowledge-agent' deleted successfully.
+Knowledge source 'earth-knowledge-source' deleted successfully.
+Index 'earth-at-night' deleted successfully.
 ```
 
-## Explanation of the code
+## Understand the code
 
-Now that you have the code, let's break down the key components:
+Now that you've run the code, let's break down the key steps:
 
-- [Create a search index](#create-a-search-index)
-- [Upload documents to the index](#upload-documents-to-the-index)
-- [Create a knowledge agent](#create-a-knowledge-agent)
-- [Set up messages](#set-up-messages)
-- [Run the retrieval pipeline](#run-the-retrieval-pipeline)
-- [Review the response, activity, and results](#review-the-response-activity-and-results)
-- [Create the Azure OpenAI client](#create-the-azure-openai-client)
-- [Use the Chat Completions API to generate an answer](#use-the-chat-completions-api-to-generate-an-answer)
-- [Continue the conversation](#continue-the-conversation)
+1. [Create a search index](#create-a-search-index)
+1. [Upload documents to the index](#upload-documents-to-the-index)
+1. [Create a knowledge source](#create-a-knowledge-source)
+1. [Create a knowledge agent](#create-a-knowledge-agent)
+1. [Set up messages](#set-up-messages)
+1. [Run the retrieval pipeline](#run-the-retrieval-pipeline)
+1. [Continue the conversation](#continue-the-conversation)
 
 ### Create a search index
 
-In Azure AI Search, an index is a structured collection of data. The following code defines an index named `earth_at_night` to contain plain text and vector content. You can use an existing index, but it must meet the criteria for [agentic retrieval workloads](../../search-agentic-retrieval-how-to-index.md). 
+In Azure AI Search, an index is a structured collection of data. The following code defines an index named `earth-at-night`, which you previously specified using the `indexName` variable.
 
+The index schema contains fields for document identification and page content, embeddings, and numbers. The schema also includes configurations for semantic ranking and vector search, which uses your `text-embedding-3-large` deployment to vectorize text and match documents based on semantic or conceptual similarity.
 ```csharp
-// Define the fields for the index
+// Define fields for the index
 var fields = new List<SearchField>
 {
     new SimpleField("id", SearchFieldDataType.String) { IsKey = true, IsFilterable = true, IsSortable = true, IsFacetable = true },
     new SearchField("page_chunk", SearchFieldDataType.String) { IsFilterable = false, IsSortable = false, IsFacetable = false },
     new SearchField("page_embedding_text_3_large", SearchFieldDataType.Collection(SearchFieldDataType.Single)) { VectorSearchDimensions = 3072, VectorSearchProfileName = "hnsw_text_3_large" },
     new SimpleField("page_number", SearchFieldDataType.Int32) { IsFilterable = true, IsSortable = true, IsFacetable = true }
-};            
-// Define the vectorizer
+};
+
+// Define a vectorizer
 var vectorizer = new AzureOpenAIVectorizer(vectorizerName: "azure_openai_text_3_large")
 {
     Parameters = new AzureOpenAIVectorizerParameters
     {
-        ResourceUri = new Uri(azureOpenAIEndpoint),
-        DeploymentName = azureOpenAIEmbeddingDeployment,
-        ModelName = azureOpenAIEmbeddingModel
+        ResourceUri = new Uri(aoaiEndpoint),
+        DeploymentName = aoaiEmbeddingDeployment,
+        ModelName = aoaiEmbeddingModel
     }
 };
 
-// Define the vector search profile and algorithm
+// Define a vector search profile and algorithm
 var vectorSearch = new VectorSearch()
 {
     Profiles =
@@ -660,7 +648,7 @@ var vectorSearch = new VectorSearch()
     }
 };
 
-// Define semantic configuration
+// Define a semantic configuration
 var semanticConfig = new SemanticConfiguration(
     name: "semantic_config",
     prioritizedFields: new SemanticPrioritizedFields
@@ -672,10 +660,7 @@ var semanticConfig = new SemanticConfiguration(
 var semanticSearch = new SemanticSearch()
 {
     DefaultConfigurationName = "semantic_config",
-    Configurations =
-    {
-        semanticConfig
-    }
+    Configurations = { semanticConfig }
 };
 
 // Create the index
@@ -686,100 +671,111 @@ var index = new SearchIndex(indexName)
     SemanticSearch = semanticSearch
 };
 
-// Create the index client and delete the index if it exists, then create it
-var indexClient = new SearchIndexClient(new Uri(endpoint), credential);
-try
-{
-    await indexClient.DeleteIndexAsync(indexName);
-    Console.WriteLine($"Index '{indexName}' deleted successfully (if it existed).");
-}
-catch (Exception ex)
-{
-    Console.WriteLine($"Index '{indexName}' could not be deleted or did not exist: {ex.Message}");
-}
+// Create the index client, deleting and recreating the index if it exists
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
 await indexClient.CreateOrUpdateIndexAsync(index);
-
-Console.WriteLine($"Index '{indexName}' created or updated successfully");
+Console.WriteLine($"Index '{indexName}' created or updated successfully.");
 ```
 
-The index schema contains fields for document identification and page content, embeddings, and numbers. It also includes configurations for semantic ranking and vector queries, which use the `text-embedding-3-large` model you previously deployed.
-
 ### Upload documents to the index
 
-Currently, the `earth_at_night` index is empty. Run the following code to populate the index with JSON documents from [NASA's Earth at Night e-book](https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json). As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
+Currently, the `earth-at-night` index is empty. The following code populates the index with JSON documents from [NASA's Earth at Night e-book](https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json). As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
 
 ```csharp
-// Download the documents from the GitHub URL
+// Upload sample documents from the GitHub URL
 string url = "https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json";
 var httpClient = new HttpClient();
 var response = await httpClient.GetAsync(url);
 response.EnsureSuccessStatusCode();
 var json = await response.Content.ReadAsStringAsync();
-
 var documents = JsonSerializer.Deserialize<List<Dictionary<string, object>>>(json);
-var searchClient = new SearchClient(new Uri(endpoint), indexName, credential);
+var searchClient = new SearchClient(new Uri(searchEndpoint), indexName, credential);
 var searchIndexingBufferedSender = new SearchIndexingBufferedSender<Dictionary<string, object>>(
     searchClient,
     new SearchIndexingBufferedSenderOptions<Dictionary<string, object>>
     {
         KeyFieldAccessor = doc => doc["id"].ToString(),
     }
 );
-
 await searchIndexingBufferedSender.UploadDocumentsAsync(documents);
 await searchIndexingBufferedSender.FlushAsync();
+Console.WriteLine($"Documents uploaded to index '{indexName}' successfully.");
+```
+
+### Create a knowledge source
+
+A knowledge source is a reusable reference to your source data. The following code defines a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
 
-Console.WriteLine($"Documents uploaded to index '{indexName}'");
+`SourceDataSelect` specifies which index fields are accessible for retrieval and citations. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+
+```csharp
+// Create a knowledge source
+var indexKnowledgeSource = new SearchIndexKnowledgeSource(
+    name: knowledgeSourceNames,
+    searchIndexParameters: new SearchIndexKnowledgeSourceParameters(searchIndexName: indexName)
+    {
+        SourceDataSelect = "id,page_chunk,page_number"
+    }
+);
+await indexClient.CreateOrUpdateKnowledgeSourceAsync(indexKnowledgeSource);
+Console.WriteLine($"Knowledge source '{knowledgeSourceName}' created or updated successfully.");
 ```
 
 ### Create a knowledge agent
 
-To connect Azure AI Search to your `gpt-4.1-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. The following code defines a knowledge agent named `earth-search-agent` that uses the `KnowledgeAgentAzureOpenAIModel` to process queries and retrieve relevant documents from the `earth_at_night` index.
+To target `earth-knowledge-source` and your `gpt-4.1-mini` deployment at query time, you need a knowledge agent. Add and run a code cell with the following code to define a knowledge agent named `earth-knowledge-agent`, which you previously specified using the `knowledgeAgentName` variable.
 
-To ensure relevant and semantically meaningful responses, `DefaultRerankerThreshold` is set to exclude responses with a reranker score of `2.5` or lower.
+`RerankerThreshold` ensures semantic relevance by excluding responses with a reranker score of `2.5` or lower. Meanwhile, `Modality` is set to `AnswerSynthesis`, enabling natural-language answers that cite the retrieved documents.
 
 ```csharp
+// Create a knowledge agent
 var openAiParameters = new AzureOpenAIVectorizerParameters
 {
-    ResourceUri = new Uri(azureOpenAIEndpoint),
-    DeploymentName = azureOpenAIGptDeployment,
-    ModelName = azureOpenAIGptModel
+    ResourceUri = new Uri(aoaiEndpoint),
+    DeploymentName = aoaiGptDeployment,
+    ModelName = aoaiGptModel
 };
 
 var agentModel = new KnowledgeAgentAzureOpenAIModel(azureOpenAIParameters: openAiParameters);
-
-var targetIndex = new KnowledgeAgentTargetIndex(indexName)
+var outputConfig = new KnowledgeAgentOutputConfiguration
 {
-    DefaultRerankerThreshold = 2.5f
+    Modality = KnowledgeAgentOutputConfigurationModality.AnswerSynthesis,
+    IncludeActivity = true
 };
 
-// Create the knowledge agent
 var agent = new KnowledgeAgent(
-    name: agentName,
+    name: knowledgeAgentName,
     models: new[] { agentModel },
-    targetIndexes: new[] { targetIndex });
+    knowledgeSources: new KnowledgeSourceReference[] {
+        new KnowledgeSourceReference(knowledgeSourceName) {
+            IncludeReferences = true,
+            IncludeReferenceSourceData = true,
+            RerankerThreshold = (float?)2.5
+        }
+    }
+)
+{
+    OutputConfiguration = outputConfig
+};
+
 await indexClient.CreateOrUpdateKnowledgeAgentAsync(agent);
-Console.WriteLine($"Search agent '{agentName}' created or updated successfully");
+Console.WriteLine($"Knowledge agent '{knowledgeAgentName}' created or updated successfully.");
 ```
 
 ### Set up messages
 
-Messages are the input for the retrieval route and contain the conversation history. Each message includes a role that indicates its origin, such as assistant or user, and content in natural language. The LLM you use determines which roles are valid.
-
-A user message represents the query to be processed, while an assistant message guides the knowledge agent on how to respond. During the retrieval process, these messages are sent to an LLM to extract relevant responses from indexed documents.
+Messages are the input for the retrieval route and contain the conversation history. Each message includes a role that indicates its origin, such as `system` or `user`, and content in natural language. The LLM you use determines which roles are valid.
 
-This assistant message instructs `earth-search-agent` to answer questions about the Earth at night, cite sources using their `ref_id`, and respond with "I don't know" when answers are unavailable.
+The following code creates a system message, which instructs `earth-knowledge-agent` to answer questions about the Earth at night and respond with "I don't know" when answers are unavailable.
 
 ```csharp
-string instructions = @"
-A Q&A agent that can answer questions about the Earth at night.
-Sources have a JSON format with a ref_id that must be cited in the answer.
-If you do not have the answer, respond with ""I don't know"".
-";
+// Set up messages
+string instructions = @"A Q&A agent that can answer questions about the Earth at night.
+If you don't have the answer, respond with ""I don't know"".";
 
-var messages = new List<Dictionary<string, object>>
+var messages = new List<Dictionary<string, string>>
 {
-    new Dictionary<string, object>
+    new Dictionary<string, string>
     {
         { "role", "system" },
         { "content", instructions }
@@ -789,68 +785,63 @@ var messages = new List<Dictionary<string, object>>
 
 ### Run the retrieval pipeline
 
-This step runs the retrieval pipeline to extract relevant information from your search index. Based on the messages and parameters on the retrieval request, the LLM:
-1. Analyzes the entire conversation history to determine the underlying information need.
-1. Breaks down the compound user query into focused subqueries.
-1. Runs each subquery simultaneously against text fields and vector embeddings in your index.
-1. Uses semantic ranker to rerank the results of all subqueries.
-1. Merges the results into a single string.
+You're ready to run agentic retrieval by sending a two-part user query to `earth-knowledge-agent`. Given the conversation history and retrieval parameters, the agent:
 
-The following code sends a two-part user query to `earth-search-agent`, which deconstructs the query into subqueries, runs the subqueries against both text fields and vector embeddings in the `earth_at_night` index, and ranks and merges the results. The response is then appended to the `messages` list.
+1. Analyzes the entire conversation to infer the user's information need.
+1. Decomposes the compound query into focused subqueries.
+1. Runs the subqueries concurrently against your knowledge source.
+1. Uses semantic ranker to rerank and filter the results.
+1. Synthesizes the top results into a natural-language answer.
 
 ```csharp
+// Use agentic retrieval to fetch results
 var agentClient = new KnowledgeAgentRetrievalClient(
-    endpoint: new Uri(endpoint),
-    agentName: agentName,
+    endpoint: new Uri(searchEndpoint),
+    agentName: knowledgeAgentName,
     tokenCredential: new DefaultAzureCredential()
-);            
+);
 
-messages.Add(new Dictionary<string, object>
+messages.Add(new Dictionary<string, string>
 {
     { "role", "user" },
-    { "content", @"
-Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown?
-Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?
-" }
+    { "content", @"Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown?
+    Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?" }
 });
 
 var retrievalResult = await agentClient.RetrieveAsync(
     retrievalRequest: new KnowledgeAgentRetrievalRequest(
-            messages: messages
-                .Where(message => message["role"].ToString() != "system")
-                .Select(
-                message => new KnowledgeAgentMessage(
-                    role: message["role"].ToString(),
-                    content: new[] { new KnowledgeAgentMessageTextContent(message["content"].ToString()) }))
-                .ToList()
+        messages: messages
+            .Where(message => message["role"] != "system")
+            .Select(
+                message => new KnowledgeAgentMessage(content: new[] { new KnowledgeAgentMessageTextContent(message["content"]) }) { Role = message["role"] }
             )
-        {
-            TargetIndexParams = { new KnowledgeAgentIndexParams { IndexName = indexName, RerankerThreshold = 2.5f } }
-        }
-    );
+            .ToList()
+    )
+);
 
-messages.Add(new Dictionary<string, object>
+messages.Add(new Dictionary<string, string>
 {
     { "role", "assistant" },
     { "content", (retrievalResult.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text }
 });
 ```
 
-### Review the response, activity, and results
-
-Now you want to display the response, activity, and results of the retrieval pipeline.
+#### Review the response, activity, and results
 
-Each retrieval response from Azure AI Search includes:
+The following code displays the response, activity, and results of the retrieval pipeline, where:
 
-+ A unified string that represents grounding data from the search results.
++ `Response` provides a synthesized, LLM-generated answer to the query that cites the retrieved documents. When answer synthesis isn't enabled, this section contains content extracted directly from the documents.
 
-+ The query plan.
++ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for semantic ranking, query planning, and answer synthesis.
 
-+ Reference data that shows which chunks of the source documents contributed to the unified string.
++ `Results` lists the documents that contributed to the response, each one identified by their `DocKey`.
 
 ```csharp
+// Print the response, activity, and results
+Console.WriteLine("Response:");
 Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text);
-Console.WriteLine("Activities:");
+
+Console.WriteLine("Activity:");
 foreach (var activity in retrievalResult.Value.Activity)
 {
     Console.WriteLine($"Activity Type: {activity.GetType().Name}");
@@ -862,7 +853,7 @@ foreach (var activity in retrievalResult.Value.Activity)
     Console.WriteLine(activityJson);
 }
 
-Console.WriteLine("Results");
+Console.WriteLine("Results:");
 foreach (var reference in retrievalResult.Value.References)
 {
     Console.WriteLine($"Reference Type: {reference.GetType().Name}");
@@ -875,101 +866,96 @@ foreach (var reference in retrievalResult.Value.References)
 }
 ```
 
-The output should include:
-
-+ `Response` provides a text string of the most relevant documents (or chunks) in the search index based on the user query. As shown later in this quickstart, you can pass this string to an LLM for answer generation.
-
-+ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for query planning and execution.
-
-+ `Results` lists the documents that contributed to the response, each one identified by their `DocKey`.
-
-### Create the Azure OpenAI client
-
-To extend the retrieval pipeline from answer *extraction* to answer *generation*, set up the Azure OpenAI client to interact with your `gpt-4.1-mini` deployment, which you specified using the `answer_model` variable in a previous section.
-
-```csharp
-AzureOpenAIClient azureClient = new(
-    new Uri(azureOpenAIEndpoint),
-    new DefaultAzureCredential());
-```
-
-### Use the Chat Completions API to generate an answer
-
-One option for answer generation is the Chat Completions API, which passes the conversation history to the LLM for processing.
-
-```csharp
-ChatClient chatClient = azureClient.GetChatClient(azureOpenAIGptDeployment);            
-List<ChatMessage> chatMessages = messages
-    .Select<Dictionary<string, object>, ChatMessage>(m => m["role"].ToString() switch
-    {
-        "user" => new UserChatMessage(m["content"].ToString()),
-        "assistant" => new AssistantChatMessage(m["content"].ToString()),
-        "system" => new SystemChatMessage(m["content"].ToString()),
-        _ => null
-    })
-    .Where(m => m != null)
-    .ToList();
-
-
-var result = await chatClient.CompleteChatAsync(chatMessages);
-
-Console.WriteLine($"[ASSISTANT]: {result.Value.Content[0].Text.Replace(".", "\n")}");
-```
-
 ### Continue the conversation
 
-Continue the conversation by sending another user query to `earth-search-agent`. The following code reruns the retrieval pipeline, fetching relevant content from the `earth_at_night` index and appending the response to the `messages` list. However, unlike before, you can now use the Azure OpenAI client to generate an answer based on the retrieved content.
+The following code continues the conversation with `earth-knowledge-agent`. After you send this user query, the agent fetches relevant content from `earth-knowledge-source` and appends the response to the messages list.
 
 ```csharp
-messages.Add(new Dictionary<string, object>
+// Continue the conversation
+messages.Add(new Dictionary<string, string>
 {
     { "role", "user" },
     { "content", "How do I find lava at night?" }
 });
 
-var retrievalResult2 = await agentClient.RetrieveAsync(
+retrievalResult = await agentClient.RetrieveAsync(
     retrievalRequest: new KnowledgeAgentRetrievalRequest(
-            messages: messages
-                .Where(message => message["role"].ToString() != "system")
-                .Select(
-                message => new KnowledgeAgentMessage(
-                    role: message["role"].ToString(),
-                    content: new[] { new KnowledgeAgentMessageTextContent(message["content"].ToString()) }))
-                .ToList()
+        messages: messages
+            .Where(message => message["role"] != "system")
+            .Select(
+                message => new KnowledgeAgentMessage(content: new[] { new KnowledgeAgentMessageTextContent(message["content"]) }) { Role = message["role"] }
             )
-        {
-            TargetIndexParams = { new KnowledgeAgentIndexParams { IndexName = indexName, RerankerThreshold = 2.5f } }
-        }
-    );
+            .ToList()
+    )
+);
 
-messages.Add(new Dictionary<string, object>
+messages.Add(new Dictionary<string, string>
 {
     { "role", "assistant" },
-    { "content", (retrievalResult2.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text }
+    { "content", (retrievalResult.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text }
 });
 ```
 
+#### Review the new response, activity, and results
+
+The following code displays the new response, activity, and results of the retrieval pipeline.
+
+```csharp
+// Print the response, activity, and results
+Console.WriteLine("Response:");
+Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeAgentMessageTextContent).Text);
+
+Console.WriteLine("Activities:");
+foreach (var activity in retrievalResult.Value.Activity)
+{
+    Console.WriteLine($"Activity Type: {activity.GetType().Name}");
+    string activityJson = JsonSerializer.Serialize(
+        activity,
+        activity.GetType(),
+        new JsonSerializerOptions { WriteIndented = true }
+    );
+    Console.WriteLine(activityJson);
+}
+
+Console.WriteLine("Results:");
+foreach (var reference in retrievalResult.Value.References)
+{
+    Console.WriteLine($"Reference Type: {reference.GetType().Name}");
+    string referenceJson = JsonSerializer.Serialize(
+        reference,
+        reference.GetType(),
+        new JsonSerializerOptions { WriteIndented = true }
+    );
+    Console.WriteLine(referenceJson);
+}
+```
+
 ## Clean up resources
 
-When working in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money. You can delete resources individually, or you can delete the resource group to delete the entire set of resources.
+When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
+
+In the Azure portal, you can manage your Azure AI Search and Azure AI Foundry resources by selecting **All resources** or **Resource groups** from the left pane.
 
-In the Azure portal, you can find and manage resources by selecting **All resources** or **Resource groups** from the left pane. You can also run the following code to delete the objects you created in this quickstart.
+Otherwise, the following code from `Program.cs` deleted the objects you created in this quickstart.
 
 ### Delete the knowledge agent
 
-The knowledge agent created in this quickstart was deleted using the following code snippet from *Program.cs*:
+```csharp
+await indexClient.DeleteKnowledgeAgentAsync(knowledgeAgentName);
+Console.WriteLine($"Knowledge agent '{knowledgeAgentName}' deleted successfully.");
+```
+
+### Delete the knowledge source
 
 ```csharp
-await indexClient.DeleteKnowledgeAgentAsync(agentName);
-Console.WriteLine($"Search agent '{agentName}' deleted successfully");
+await indexClient.DeleteKnowledgeSourceAsync(knowledgeSourceName);
+Console.WriteLine($"Knowledge source '{knowledgeSourceName}' deleted successfully.");
 ```
 
 ### Delete the search index
 
-The search index created in this quickstart was deleted using the following code snippet from *Program.cs*:
-
 ```csharp
 await indexClient.DeleteIndexAsync(indexName);
-Console.WriteLine($"Index '{indexName}' deleted successfully");        
+Console.WriteLine($"Index '{indexName}' deleted successfully.");     
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エージェントリトリーバルのC#クイックスタートの大規模な修正"
}
```

### Explanation
この変更は、`agentic-retrieval-csharp.md`ファイルに対して大規模な修正を行い、C#でのエージェントリトリーバルのクイックスタートガイドを更新しています。主な変更点は以下の通りです。

1. **日付の更新**: 文書の更新日が2025年8月28日から2025年9月23日に変更されました。
   
2. **コンテンツの修正と改善**: 文書内の説明が更新され、エージェントリトリーバルのプロセスや使用される知識エージェントに関する情報が具体化されました。特に、エージェントリトリーバルがどのように複雑なクエリを分解し、サブクエリを並行して処理するかが詳述されています。

3. **コードの改訂**: コード例が修正され、特に環境を設定する手順や、新しいライブラリの名称、メソッド名に変更が加えられました。また、knowledge sourceやknowledge agentの作成に必要な情報も明確になりました。

4. **メッセージの形式変更**: メッセージの構造や役割を表すためのデータ型や辞書が更新され、より適切な形式でエージェントに情報が提供されています。

このような変更は、ユーザーがより直感的に情報を使用できるようにし、最新の機能を活かせるように設計されています。全体として、ドキュメントの質と使いやすさを向上させるための大規模な改訂です。

## articles/search/includes/quickstarts/agentic-retrieval-java.md{#item-4e2c55}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-c
 Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
 > [!TIP]
-> The Java version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST or Python version.
+> The Java version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the C#, Python, or REST version.
 
 ## Prerequisites
 
@@ -27,7 +27,8 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 + The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
 [!INCLUDE [Setup](./agentic-retrieval-setup.md)]
-## Set up
+
+## Set up the environment
 
 The sample in this quickstart works with the Java Runtime. Install a Java Development Kit such as [Azul Zulu OpenJDK](https://www.azul.com/downloads/?package=jdk). The [Microsoft Build of OpenJDK](https://www.microsoft.com/openjdk) or your preferred JDK should also work.
 
@@ -110,7 +111,7 @@ The sample in this quickstart works with the Java Runtime. Install a Java Develo
    mvn clean dependency:copy-dependencies
    ```
 
-## Create the index and knowledge agent
+## Run the code
 
 1. Create a new file named `.env` in the `quickstart-agentic-retrieval` folder and add the following environment variables:
 
@@ -802,7 +803,7 @@ The sample in this quickstart works with the Java Runtime. Install a Java Develo
     java -cp ".;target\dependency\*" App
     ```
 
-## Output
+### Output
 
 The output of the application should look similar to the following:
 
@@ -1005,7 +1006,7 @@ References: [1], [2], [3], [4], [5]
 [DONE] Quickstart completed successfully!
 ```
 
-## Explaining the code
+## Understand the code
 
 Now that you have the code, let's break down the key components:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaエージェントリトリーバルのクイックスタートの更新"
}
```

### Explanation
この変更は、`agentic-retrieval-java.md`ファイルに対するマイナーな更新を行い、Javaでのエージェントリトリーバルのクイックスタートガイドを見直しています。具体的な変更内容は以下の通りです。

1. **TIPセクションの更新**: 提供されるTIPが修正され、Javaバージョンが“C#、Python、またはRESTバージョン”のいずれかを参照するように変更されました。これにより、他の言語バージョンへの参照が明確になりました。

2. **環境構築のセクション改名**: "Set up"セクションが "Set up the environment" に変更され、環境設定の重要性が強調されました。

3. **手順の見直し**: 手順の見出しが "Create the index and knowledge agent" から "Run the code" に変更され、実行の流れをより明確にしています。

4. **出力セクションの改名**: "Output"が "Output" に変更され、出力結果のセクションの重要性が明確になりました。

5. **コードの解説セクションタイトルの変更**: "Explaining the code" が "Understand the code" に変更され、コード内容の理解を促す表現となりました。

これらの変更は、ユーザーがクイックスタートをより効果的に利用できるように、ドキュメントのクリアさと一貫性を高めるために行われています。

## articles/search/includes/quickstarts/agentic-retrieval-javascript.md{#item-715283}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-c
 Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
 > [!TIP]
-> The JavaScript version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST or Python version.
+> The JavaScript version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the C#, Python, or REST version.
 
 ## Prerequisites
 
@@ -28,7 +28,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 [!INCLUDE [Setup](./agentic-retrieval-setup.md)]
 
-## Setup
+## Set up the environment
 
 1. Create a new folder `quickstart-agentic-retrieval` to contain the application and open Visual Studio Code in that folder with the following command:
 
@@ -65,7 +65,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
     npm install @azure/identity
     ```
 
-## Create the index and knowledge agent
+## Run the code
 
 1. Create a new file named `.env` in the `quickstart-agentic-retrieval` folder and add the following environment variables:
 
@@ -572,7 +572,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
     node index.js
     ```
 
-## Output
+### Output
 
 The output of the application should look similar to the following:
 
@@ -749,7 +749,7 @@ To find lava at night, satellite instruments like the VIIRS Day/Night Band (DNB)
 ✅ Quickstart completed successfully!
 ```
 
-## Explaining the code
+## Understand the code
 
 Now that you have the code, let's break down the key components:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptエージェントリトリーバルのクイックスタートの更新"
}
```

### Explanation
この変更は、`agentic-retrieval-javascript.md`ファイルに対するマイナーな更新を行い、JavaScriptでのエージェントリトリーバルのクイックスタートガイドを見直しています。具体的な変更内容は以下の通りです。

1. **TIPセクションの内容更新**: 提供されるTIPが修正され、JavaScriptバージョンが“C#、Python、またはRESTバージョン”のいずれかを参照するように変更されました。これにより、他の言語バージョンへの参照が明確になりました。

2. **環境設定のセクション改名**: "Setup"セクションが "Set up the environment" に変更され、環境設定の重要性が強調されました。

3. **手順の見直し**: 手順の見出しが "Create the index and knowledge agent" から "Run the code" に変更され、実行の流れをより明確にしています。

4. **出力セクションの改名**: "Output"が "Output" に変更され、出力結果のセクションの重要性が明確になりました。

5. **コードの解説セクションの名称変更**: "Explaining the code" が "Understand the code" に変更され、コード内容の理解を促す表現となりました。

これらの変更によって、ユーザーがクイックスタートをより効果的に利用できるように、ドキュメントの明確さと一貫性が高められています。

## articles/search/includes/quickstarts/agentic-retrieval-typescript.md{#item-e6370b}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-c
 Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
 > [!TIP]
-> The TypeScript version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST or Python version.
+> The TypeScript version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the C#, Python, or REST version.
 
 ## Prerequisites
 
@@ -28,7 +28,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 [!INCLUDE [Setup](./agentic-retrieval-setup.md)]
 
-## Setup
+## Set up the environment
 
 1. Create a new folder `quickstart-agentic-retrieval` to contain the application and open Visual Studio Code in that folder with the following command:
 
@@ -71,7 +71,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
     npm install @azure/identity
     ```
 
-## Create the index and knowledge agent
+## Run the code
 
 1. Create a new file named `.env` in the `quickstart-agentic-retrieval` folder and add the following environment variables:
 
@@ -760,7 +760,7 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
     node index.js
     ```
 
-## Output
+### Output
 
 The output of the application should look similar to the following:
 
@@ -937,7 +937,7 @@ To find lava at night, satellite instruments like the VIIRS Day/Night Band (DNB)
 ✅ Quickstart completed successfully!
 ```
 
-## Explaining the code
+## Understand the code
 
 Now that you have the code, let's break down the key components:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptエージェントリトリーバルのクイックスタートの更新"
}
```

### Explanation
この変更は、`agentic-retrieval-typescript.md`ファイルに対するマイナーな更新を行い、TypeScriptでのエージェントリトリーバルのクイックスタートガイドを見直しています。具体的な変更内容は以下の通りです。

1. **TIPセクションの更新**: TIPの内容が修正され、TypeScriptバージョンが“C#、Python、またはRESTバージョン”のいずれかを参照するように変更されました。これにより、他の言語バージョンへの参照が明確になりました。

2. **環境設定のセクション名の変更**: "Setup"セクションが "Set up the environment" に変更され、環境設定の重要性が強調されました。

3. **手順の見直し**: 手順の見出しが "Create the index and knowledge agent" から "Run the code" に変更され、実行の流れをより明確にしています。

4. **出力セクションの改名**: "Output"が "Output" に変更され、出力結果のセクションの重要性が明確になりました。

5. **コードの解説セクションの名称変更**: "Explaining the code" が "Understand the code" に変更され、コード内容の理解を促す表現となりました。

これらの変更によって、ユーザーがクイックスタートをより効果的に利用できるように、ドキュメントの明確さと一貫性が高められています。

## articles/search/index.yml{#item-c67121}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ metadata:
   description: Information retrieval at scale for agentic retrieval, with vector and text content in traditional or generative search scenarios.
   author: HeidiSteen
   ms.author: heidist
-  ms.date: 05/12/2025
+  ms.date: 09/23/2025
   ms.service: azure-ai-search
   ms.topic: landing-page
   ms.custom:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの日付の更新"
}
```

### Explanation
この変更は、`index.yml`ファイルに対するマイナーな更新であり、メタデータに含まれる日付が修正されています。具体的な変更内容は以下の通りです。

1. **日付の更新**: `ms.date`フィールドの値が“05/12/2025”から“09/23/2025”に変更されました。この変更は、コンテンツの公開日や更新日を反映させるために行われました。

これにより、ドキュメントのメタデータが最新の情報を反映しており、ユーザーに正確なコンテンツの提供が行われるようになっています。その他のメタデータには変更はありません。

## articles/search/media/agentic-retrieval/agent-to-agent-pipeline.png{#item-9f1346}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルのメタデータの更新"
}
```

### Explanation
この変更は、`agent-to-agent-pipeline.png`という画像ファイルに対するマイナーな更新です。具体的には、ファイル自体には変更が加えられていませんが、ファイルに関連するメタデータの修正や更新がある可能性があります。以下の点が注目されます。

1. **ファイルの状態**: 変更は0であるため、画像自体に新しい内容や修正は行われていません。ただし、リポジトリの他の部分との整合性を保つために、異なるメタデータの更新やリンクの変更が行われることがあります。

この変更によって、画像自体に影響はありませんが、ドキュメント全体のコンテンツが最新の状態に維持されることが重要です。

## articles/search/media/agentic-retrieval/agent-to-agent-pipeline.svg{#item-2fd4e1}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,279 @@
+<?xml version="1.0" encoding="UTF-8"?>
+<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 800.8 277.2">
+  <defs>
+    <linearGradient id="linear-gradient" x1="-91" y1="1991.5806" x2="-91" y2="1961.664" gradientTransform="translate(564 2092.8) scale(1 -1)" gradientUnits="userSpaceOnUse">
+      <stop offset=".18" stop-color="#5ea0ef"/>
+      <stop offset="1" stop-color="#0078d4"/>
+    </linearGradient>
+    <radialGradient id="radial-gradient" cx="58.568" cy="1983.5966" fx="58.568" fy="1983.5966" r="7.2808" gradientTransform="translate(581.1847 1821.7585) scale(.8628 -.8628)" gradientUnits="userSpaceOnUse">
+      <stop offset=".225" stop-color="#32d4f5"/>
+      <stop offset=".59" stop-color="#32d2f2"/>
+      <stop offset=".825" stop-color="#32caea"/>
+      <stop offset="1" stop-color="#32bedd"/>
+    </radialGradient>
+    <linearGradient id="linear-gradient-2" x1="73.2318" y1="221.9867" x2="73.2318" y2="209.4151" gradientUnits="userSpaceOnUse">
+      <stop offset="0" stop-color="#5c2e91"/>
+      <stop offset="1" stop-color="#c239b3"/>
+    </linearGradient>
+    <linearGradient id="linear-gradient-3" x1="49.8832" y1="1642.1132" x2="61.4722" y2="1617.4641" gradientTransform="translate(0 1858.8) scale(1 -1)" gradientUnits="userSpaceOnUse">
+      <stop offset="0" stop-color="#c239b3"/>
+      <stop offset="1" stop-color="#5c2e91"/>
+    </linearGradient>
+    <linearGradient id="linear-gradient-4" x1="192.7538" y1="1788.1132" x2="204.3428" y2="1763.4641" xlink:href="#linear-gradient-3"/>
+    <linearGradient id="linear-gradient-5" x1="618.6178" y1="1778.1394" x2="618.6178" y2="1798.1394" gradientTransform="translate(0 1858.8) scale(1 -1)" gradientUnits="userSpaceOnUse">
+      <stop offset="0" stop-color="#0078d4"/>
+      <stop offset="1" stop-color="#5ea0ef"/>
+    </linearGradient>
+    <linearGradient id="linear-gradient-6" x1="614.9694" y1="1795.1961" x2="614.9694" y2="1781.8928" gradientTransform="translate(0 1858.8) scale(1 -1)" gradientUnits="userSpaceOnUse">
+      <stop offset="0" stop-color="#50e6ff"/>
+      <stop offset="1" stop-color="#32bedd"/>
+    </linearGradient>
+  </defs>
+  <g id="Shapes">
+    <rect width="800.8" height="277.2" fill="#fff"/>
+    <g>
+      <g>
+        <rect x="382.8" y="8.4" width="409" height="150" fill="#fff"/>
+        <rect x="382.8" y="8.4" width="409" height="150" fill="#fff"/>
+        <rect x="382.8" y="8.4" width="409" height="150" fill="#fff"/>
+      </g>
+      <g opacity=".2">
+        <g>
+          <rect x="382.8" y="8.4" width="409" height="150" fill="#83b9f9"/>
+          <rect x="382.8" y="8.4" width="409" height="150" fill="#83b9f9"/>
+          <rect x="382.8" y="8.4" width="409" height="150" fill="#83b9f9"/>
+        </g>
+      </g>
+      <g>
+        <rect x="382.8" y="8.4" width="409" height="150" fill="#fff"/>
+        <rect x="382.8" y="8.4" width="409" height="150" fill="#83b9f9" opacity=".2"/>
+        <rect x="382.8" y="8.4" width="409" height="150" fill="none" stroke="#1b93eb" stroke-miterlimit="10" stroke-width=".25"/>
+      </g>
+      <g>
+        <rect x="382.8" y="8.4" width="409" height="150" fill="none" stroke="#1b93eb" stroke-miterlimit="10" stroke-width=".25"/>
+        <rect x="382.8" y="8.4" width="409" height="150" fill="none" stroke="#1b93eb" stroke-miterlimit="10" stroke-width=".25"/>
+        <rect x="382.8" y="8.4" width="409" height="150" fill="none" stroke="#1b93eb" stroke-miterlimit="10" stroke-width=".25"/>
+      </g>
+    </g>
+    <g>
+      <rect x="8.8" y="8.4" width="106" height="119" fill="#fff"/>
+      <rect x="8.8" y="8.4" width="106" height="119" fill="#e1ddd8" opacity=".4"/>
+      <rect x="8.8" y="8.4" width="106" height="119" fill="none" stroke="#8e8278" stroke-width=".25"/>
+    </g>
+    <g>
+      <rect x="8.8" y="149.4" width="106" height="119" fill="#fff"/>
+      <rect x="8.8" y="149.4" width="106" height="119" fill="#e1ddd8" opacity=".4"/>
+      <rect x="8.8" y="149.4" width="106" height="119" fill="none" stroke="#8e8278" stroke-width=".25"/>
+    </g>
+    <g>
+      <g>
+        <rect x="144.8" y="8.4" width="106" height="119" fill="#fff"/>
+        <rect x="144.8" y="8.4" width="106" height="119" fill="#fff"/>
+        <rect x="144.8" y="8.4" width="106" height="119" fill="#fff"/>
+      </g>
+      <g opacity=".2">
+        <g>
+          <rect x="144.8" y="8.4" width="106" height="119" fill="#83b9f9"/>
+          <rect x="144.8" y="8.4" width="106" height="119" fill="#83b9f9"/>
+          <rect x="144.8" y="8.4" width="106" height="119" fill="#83b9f9"/>
+        </g>
+      </g>
+      <g>
+        <rect x="144.8" y="8.4" width="106" height="119" fill="#fff"/>
+        <rect x="144.8" y="8.4" width="106" height="119" fill="#83b9f9" opacity=".2"/>
+        <rect x="144.8" y="8.4" width="106" height="119" fill="none" stroke="#1b93eb" stroke-miterlimit="10" stroke-width=".25"/>
+      </g>
+      <g>
+        <rect x="144.8" y="8.4" width="106" height="119" fill="none" stroke="#1b93eb" stroke-miterlimit="10" stroke-width=".25"/>
+        <rect x="144.8" y="8.4" width="106" height="119" fill="none" stroke="#1b93eb" stroke-miterlimit="10" stroke-width=".25"/>
+        <rect x="144.8" y="8.4" width="106" height="119" fill="none" stroke="#1b93eb" stroke-miterlimit="10" stroke-width=".25"/>
+      </g>
+    </g>
+    <path d="M73.7394,80.999c0-6.6269-5.3722-11.999-11.999-11.999-3.2703,0-6.235,1.3083-8.3993,3.43v-1.3302c0-.497-.4029-.8999-.8999-.8999s-.8999.4029-.8999.8999v4.1996c0,.497.4029.8999.8999.8999h4.1996c.497,0,.8999-.4029.8999-.8999s-.4029-.8999-.8999-.8999h-2.6769c1.8708-2.2023,4.6605-3.5997,7.7765-3.5997,5.6328,0,10.1991,4.5663,10.1991,10.1991s-4.5663,10.1991-10.1991,10.1991c-1.7612,0-3.4556-.4462-4.9591-1.2845l-.3234-.1803-4.7835,1.3345,1.3352-4.7806-.1808-.3236c-.8402-1.5048-1.2875-3.2012-1.2875-4.9646,0-.8101.0944-1.5981.2729-2.3537.0945-.3617.0772-1.0655-.6432-1.2238-.736-.1617-1.0455.4248-1.1229.8616l.0019.0004c-.2019.8726-.3086,1.7815-.3086,2.7156,0,1.9442.4636,3.8229,1.3374,5.5102l-1.2811,4.5871c-.0737.2637-.0738.543,0,.8069.2228.7978,1.0502,1.264,1.848,1.0412l4.5906-1.2807c1.6858.8718,3.5623,1.3343,5.5041,1.3343,6.6268,0,11.999-5.3722,11.999-11.999ZM61.7404,77.0993c0-.497-.4029-.8999-.8999-.8999s-.8999.4029-.8999.8999v5.3995c0,.497.4029.8999.8999.8999h3.5997c.497,0,.8999-.4029.8999-.8999s-.4029-.8999-.8999-.8999h-2.6998v-4.4996Z" fill="#212121"/>
+    <rect x="400.8" y="52.8" width="145" height="88" fill="#fff" stroke="#1b93eb" stroke-width=".25"/>
+    <rect x="571.8" y="52.8" width="202" height="88" fill="#fff" stroke="#1b93eb" stroke-width=".25"/>
+    <g>
+      <rect x="589.8" y="91.8" width="167" height="40" fill="#fff"/>
+      <rect x="589.8" y="91.8" width="167" height="40" fill="#edf6f3" opacity=".65"/>
+      <rect x="589.8" y="91.8" width="167" height="40" fill="none" stroke="#9dd6c9" stroke-width=".25"/>
+    </g>
+    <g>
+      <line x1="114.273" y1="39.6" x2="139.8178" y2="39.6" fill="none" stroke="#3c3c41" stroke-miterlimit="10"/>
+      <polygon points="138.7236 43.3398 145.2 39.6 138.7236 35.8603 138.7236 43.3398" fill="#3c3c41"/>
+    </g>
+    <g>
+      <path d="M198.4369,127.6v74.2c0,2.75-2.25,5-5,5h-73.6547" fill="none" stroke="#3c3c41" stroke-miterlimit="10"/>
+      <polygon points="120.8764 203.0602 114.4 206.8 120.8764 210.5398 120.8764 203.0602" fill="#3c3c41"/>
+    </g>
+    <g>
+      <line x1="250.8" y1="39.6" x2="377.4178" y2="39.6" fill="none" stroke="#3c3c41" stroke-miterlimit="10"/>
+      <polygon points="376.3236 43.3398 382.8 39.6 376.3236 35.8603 376.3236 43.3398" fill="#3c3c41"/>
+    </g>
+    <g>
+      <line x1="545.6" y1="92.2" x2="566.6178" y2="92.2" fill="none" stroke="#3c3c41" stroke-miterlimit="10"/>
+      <polygon points="565.5236 95.9397 572 92.2 565.5236 88.4603 565.5236 95.9397" fill="#3c3c41"/>
+    </g>
+    <g>
+      <line x1="382.8" y1="92.2" x2="256.1822" y2="92.2" fill="none" stroke="#3c3c41" stroke-miterlimit="10"/>
+      <polygon points="257.2764 88.4602 250.8 92.2 257.2764 95.9397 257.2764 88.4602" fill="#3c3c41"/>
+    </g>
+    <g>
+      <path d="M488,119.486c-.0608-3.3525-2.5339-6.1708-5.85-6.6667-.1363-4.708-4.0409-8.4268-8.75-8.3333-3.7345-.0382-7.0815,2.2981-8.3333,5.8167-4.0155.5163-7.0331,3.9182-7.0667,7.9667.1627,4.5304,3.9171,8.0997,8.45,8.0333h14.4167c.1216.0173.2451.0173.3667,0,3.7301-.0631,6.7311-3.0862,6.7667-6.8167Z" fill="url(#linear-gradient)"/>
+      <path d="M478.55,111.6027c-1.4589-2.4202-4.6034-3.1995-7.0236-1.7406-1.164.7017-2.0011,1.8376-2.3264,3.1573-.297,1.2855-.1007,2.6356.55,3.7833l-3.9,3.95c-.5155.5129-.5175,1.3466-.0046,1.862.0015.0015.0031.0031.0046.0046.2468.2482.5833.3864.9333.3833.3508.007.6887-.1318.9333-.3833l3.8833-3.9333c.4221.2454.8765.4305,1.35.55,2.7567.662,5.5281-1.036,6.1901-3.7927.3141-1.3081.1022-2.6872-.5901-3.8406ZM477.65,115.1027c-.3908,1.6085-1.8281,2.7432-3.4833,2.75-.2875.0023-.5738-.037-.85-.1167-.4217-.095-.819-.2766-1.1667-.5333-.3667-.25-.6833-.5666-.9333-.9333-.5712-.8452-.7588-1.8924-.5167-2.8833.3719-1.616,1.8085-2.7624,3.4667-2.7667.2917.0004.5825.0339.8667.1.924.2445,1.7144.8434,2.2,1.6667.498.8129.6482,1.7919.4167,2.7167Z" fill="#f2f2f2"/>
+      <ellipse cx="474.15" cy="114.2527" rx="3.5833" ry="3.6" fill="#83b9f9"/>
+    </g>
+    <g id="e958cf41-a31a-426c-90ab-58b20591ece8">
+      <g>
+        <rect x="621.3625" y="115.3863" width="9.157" height="2.0855" rx=".975" ry=".975" transform="translate(101.0061 476.7084) rotate(-45)" fill="#198ab3"/>
+        <circle cx="631.7181" cy="110.2819" r="6.2819" fill="url(#radial-gradient)"/>
+        <circle cx="631.7049" cy="110.1699" r="4.9343" fill="#fff"/>
+        <path d="M626.924,111.3906s1.3505-6.7591,7.6616-5.226c-1.7332-1.2854-4.1082-1.2674-5.8217.0442-1.6351,1.1736-2.3688,3.2398-1.8399,5.1818Z" fill="#c3f1ff"/>
+      </g>
+    </g>
+    <g>
+      <path d="M73.2318,209.4151c3.4716,0,6.2858,2.8142,6.2858,6.2858s-2.8142,6.2858-6.2858,6.2858-6.2858-2.8142-6.2858-6.2858,2.8142-6.2858,6.2858-6.2858ZM73.4783,212.3736l-.0792.0661-.0661.0791c-.135.1949-.135.455,0,.6499l.0661.0791,1.8807,1.8817h-6.0481l-.1027.0092c-.2333.0423-.4171.2263-.4594.4595l-.0093.1027.0093.1027c.0423.2332.2262.4172.4594.4595l.1027.0092h6.0481l-1.8807,1.8817-.0661.0791c-.1543.2227-.1322.5306.0661.729.1984.1984.5063.2204.729.0661l.0792-.0661,2.9045-2.9115.0378-.0543.039-.077.0242-.0719.0166-.0936.0024-.0529-.0032-.061-.0158-.0854-.0344-.0952-.0481-.0837-.0521-.0645-2.8709-2.8714-.0792-.0661c-.1949-.135-.455-.135-.6498,0Z" fill="url(#linear-gradient-2)"/>
+      <path d="M63.5463,223.2951c.0627.0443.1229.0919.18.1425.0035-.0601.0053-.1208.0053-.1818v-6.1428c0-1.6946-1.3738-3.0683-3.0683-3.0683l-4.7735-.0007.0011-1.0214-.0093-.1388c-.0678-.4992-.4957-.8839-1.0135-.8839l-.1388.0093c-.4991.0678-.8839.4957-.8839,1.0135l-.0011,1.0214-4.7722.0007c-1.6946,0-3.0683,1.3736-3.0683,3.0683v6.1428c0,1.6945,1.3736,3.0683,3.0683,3.0683h10.6151c.0089-.0236.0175-.0473.0256-.0712l.0121-.036.6139-1.8877.0056-.016c.1451-.411.4141-.7667.7698-1.0181.3556-.2515.7806-.3865,1.216-.3865s.8603.135,1.216.3865ZM51.7986,218.1358c.9408,0,1.7036.7627,1.7036,1.7036s-.7628,1.7036-1.7036,1.7036-1.7036-.7628-1.7036-1.7036.7627-1.7036,1.7036-1.7036ZM57.9251,218.1358c.9409,0,1.7036.7627,1.7036,1.7036s-.7627,1.7036-1.7036,1.7036-1.7036-.7628-1.7036-1.7036.7627-1.7036,1.7036-1.7036ZM56.2893,228.4131l.1535-.0499h-9.4113c-1.6945,0-3.0683,1.3738-3.0683,3.0683v1.2373c0,1.4902.6501,2.9062,1.78,3.8777,2.1313,1.8324,5.1843,2.7277,9.1246,2.7277,2.8308,0,5.2047-.4623,7.1085-1.4018-.2951-.0559-.5766-.1745-.8243-.3498-.3556-.2515-.6247-.6071-.7698-1.0181l-.0057-.016-.6142-1.8887-.0007-.0022c-.0893-.2701-.2238-.5224-.3972-.7465-.0638-.0825-.133-.161-.2069-.2354l-.4893-.3569-.4894-.2501-1.8895-.6137-.016-.0056c-.4107-.1448-.7667-.4135-1.0184-.769-.2519-.3556-.3871-.7806-.3871-1.2165s.1353-.8607.3871-1.2164c.2517-.3556.6077-.6241,1.0184-.769l.016-.0056ZM60.1231,232.653c.1144.1147.2212.2362.3198.3636.2684.3468.4766.7377.6146,1.1565l.6105,1.8774c.0511.1447.1459.27.2712.3586s.2752.1362.4287.1362.3033-.0476.4286-.1362c.1118-.0791.1994-.1874.2532-.3126.0065-.0151.0125-.0305.018-.0461l.6106-1.8774c.1898-.5708.5104-1.0894.936-1.5148.4256-.4253.9446-.7457,1.5159-.9353l1.8789-.6101c.1448-.0511.2703-.1458.3589-.271.0886-.1253.1364-.2749.1364-.4285,0-.1534-.0477-.303-.1364-.4283-.0886-.1252-.2141-.22-.3589-.271l-.0376-.0094-1.8787-.6101c-.5712-.1898-1.0903-.51-1.516-.9353-.4256-.4253-.7461-.9439-.936-1.5148l-.6106-1.8774c-.051-.1447-.1458-.27-.2711-.3586-.1253-.0886-.2752-.1362-.4287-.1362s-.3033.0476-.4286.1362c-.1255.0886-.2201.214-.2712.3586l-.6107,1.8774-.0155.0465c-.1879.5485-.4968,1.048-.9041,1.4614-.4189.4249-.9304.7474-1.4947.9422l-1.8789.6101c-.1447.051-.2701.1458-.3588.271-.0888.1253-.1364.2749-.1364.4283,0,.1535.0476.3031.1364.4285.0886.1252.2141.2198.3588.271l1.8789.6101c.5723.1906,1.092.5123,1.5176.9394ZM69.892,237.8607l1.0438.339.0209.0052c.0805.0284.1501.081.1994.1506.0494.0695.0758.1527.0758.238s-.0265.1684-.0758.238c-.0492.0696-.1189.1222-.1994.1506l-1.0438.339c-.3173.1054-.6057.2834-.8422.5196-.2365.2363-.4146.5245-.52.8415l-.3393,1.0431c-.0284.0803-.081.15-.1507.1992-.0695.0492-.1529.0757-.2381.0757-.0854,0-.1685-.0265-.2382-.0757-.0695-.0492-.1222-.1189-.1505-.1992l-.3393-1.0431c-.1049-.318-.2826-.6072-.519-.8444-.2366-.2373-.5253-.4161-.8432-.5219l-1.0439-.339c-.0805-.0284-.15-.081-.1994-.1506-.0492-.0695-.0757-.1527-.0757-.238s.0265-.1684.0757-.238c.0494-.0697.1189-.1222.1994-.1506l1.0439-.339c.3135-.1081.5977-.2873.8303-.5234.2326-.2362.4076-.5228.511-.8377l.3391-1.0431c.0285-.0805.0811-.15.1507-.1992.0697-.0492.1529-.0757.2382-.0757.0852,0,.1684.0265.2381.0757.0697.0492.1223.1188.1507.1992l.3393,1.0431c.1054.3171.2835.6052.52.8415.2365.2362.5249.4141.8422.5196Z" fill="url(#linear-gradient-3)"/>
+    </g>
+    <path d="M206.4169,77.2951c.0627.0443.1229.0919.18.1425.0035-.0601.0053-.1208.0053-.1818v-6.1428c0-1.6946-1.3738-3.0683-3.0683-3.0683l-4.7735-.0007.0011-1.0214-.0093-.1388c-.0678-.4992-.4957-.8839-1.0135-.8839l-.1388.0093c-.4991.0678-.8839.4957-.8839,1.0135l-.0011,1.0214-4.7722.0007c-1.6946,0-3.0683,1.3736-3.0683,3.0683v6.1428c0,1.6945,1.3736,3.0683,3.0683,3.0683h10.6151c.0089-.0236.0175-.0473.0256-.0712l.0121-.036.6139-1.8877.0056-.016c.1451-.411.4141-.7667.7698-1.0181.3556-.2515.7806-.3865,1.216-.3865s.8603.135,1.216.3865ZM194.6692,72.1358c.9408,0,1.7036.7627,1.7036,1.7036s-.7628,1.7036-1.7036,1.7036-1.7036-.7628-1.7036-1.7036.7627-1.7036,1.7036-1.7036ZM200.7957,72.1358c.9409,0,1.7036.7627,1.7036,1.7036s-.7627,1.7036-1.7036,1.7036-1.7036-.7628-1.7036-1.7036.7627-1.7036,1.7036-1.7036ZM199.1599,82.4131l.1535-.0499h-9.4113c-1.6945,0-3.0683,1.3738-3.0683,3.0683v1.2373c0,1.4902.6501,2.9062,1.78,3.8777,2.1313,1.8324,5.1843,2.7277,9.1246,2.7277,2.8308,0,5.2047-.4623,7.1085-1.4018-.2951-.0559-.5766-.1745-.8243-.3498-.3556-.2515-.6247-.6071-.7698-1.0181l-.0057-.016-.6142-1.8887-.0007-.0022c-.0893-.2701-.2238-.5224-.3972-.7465-.0638-.0825-.133-.161-.2069-.2354l-.4893-.3569-.4894-.2501-1.8895-.6137-.016-.0056c-.4107-.1448-.7667-.4135-1.0184-.769-.2519-.3556-.3871-.7806-.3871-1.2165s.1353-.8607.3871-1.2164c.2517-.3556.6077-.6241,1.0184-.769l.016-.0056ZM202.9937,86.653c.1144.1147.2212.2362.3198.3636.2684.3468.4766.7377.6146,1.1565l.6105,1.8774c.0511.1447.1459.27.2712.3586s.2752.1362.4287.1362.3033-.0476.4286-.1362c.1118-.0791.1994-.1874.2532-.3126.0065-.0151.0125-.0305.018-.0461l.6106-1.8774c.1898-.5708.5104-1.0894.936-1.5148.4256-.4253.9446-.7457,1.5159-.9353l1.8789-.6101c.1448-.0511.2703-.1458.3589-.271.0886-.1253.1364-.2749.1364-.4285,0-.1534-.0477-.303-.1364-.4283-.0886-.1252-.2141-.22-.3589-.271l-.0376-.0094-1.8787-.6101c-.5712-.1898-1.0903-.51-1.516-.9353-.4256-.4253-.7461-.9439-.936-1.5148l-.6106-1.8774c-.051-.1447-.1458-.27-.2711-.3586-.1253-.0886-.2752-.1362-.4287-.1362s-.3033.0476-.4286.1362c-.1255.0886-.2201.214-.2712.3586l-.6107,1.8774-.0155.0465c-.1879.5485-.4968,1.048-.9041,1.4614-.4189.4249-.9304.7474-1.4947.9422l-1.8789.6101c-.1447.051-.2701.1458-.3588.271-.0888.1253-.1364.2749-.1364.4283,0,.1535.0476.3031.1364.4285.0886.1252.2141.2198.3588.271l1.8789.6101c.5723.1906,1.092.5123,1.5176.9394ZM212.7626,91.8607l1.0438.339.0209.0052c.0805.0284.1501.081.1994.1506.0494.0695.0758.1527.0758.238s-.0265.1684-.0758.238c-.0492.0696-.1189.1222-.1994.1506l-1.0438.339c-.3173.1054-.6057.2834-.8422.5196-.2365.2363-.4146.5245-.52.8415l-.3393,1.0431c-.0284.0803-.081.15-.1507.1992-.0695.0492-.1529.0757-.2381.0757-.0854,0-.1685-.0265-.2382-.0757-.0695-.0492-.1222-.1189-.1505-.1992l-.3393-1.0431c-.1049-.318-.2826-.6072-.519-.8444-.2366-.2373-.5253-.4161-.8432-.5219l-1.0439-.339c-.0805-.0284-.15-.081-.1994-.1506-.0492-.0695-.0757-.1527-.0757-.238s.0265-.1684.0757-.238c.0494-.0697.1189-.1222.1994-.1506l1.0439-.339c.3135-.1081.5977-.2873.8303-.5234.2326-.2362.4076-.5228.511-.8377l.3391-1.0431c.0285-.0805.0811-.15.1507-.1992.0697-.0492.1529-.0757.2382-.0757.0852,0,.1684.0265.2381.0757.0697.0492.1223.1188.1507.1992l.3393,1.0431c.1054.3171.2835.6052.52.8415.2365.2362.5249.4141.8422.5196Z" fill="url(#linear-gradient-4)"/>
+    <g>
+      <rect x="610.4511" y="63.0072" width="16.3333" height="20" rx=".6667" ry=".6667" fill="url(#linear-gradient-5)"/>
+      <rect x="607.2" y="65.0817" width="15.5389" height="8.1011" rx=".6011" ry=".6011" fill="url(#linear-gradient-6)"/>
+      <path d="M620.2,67.9217h-7.5756c-.0749.0012-.1365-.0584-.1378-.1333h0v-.4478c0-.0755.0612-.1367.1367-.1367h7.5756c.0757,0,.1372.061.1378.1367v.4444c.0006.0749-.0596.136-.1344.1367-.0004,0-.0007,0-.0011,0h-.0011ZM611.4222,68.245v-1.3622c0-.1301-.1055-.2356-.2356-.2356h-1.3644c-.1297,0-.2349.1048-.2356.2344h0v1.3633c0,.1295.105.2344.2344.2344h1.3633c.1295.0006.2349-.1039.2356-.2333,0-.0004,0-.0007,0-.0011h.0022Z" fill="#fff"/>
+      <path d="M620.1989,70.8106h-7.5744c-.0757,0-.1372-.061-.1378-.1367h0v-.4511c0-.0761.0617-.1378.1378-.1378h7.5733c.0758.0006.1372.0619.1378.1378v.4444c0,.0758-.0608.1377-.1367.1389v.0044ZM611.0811,69.8895h-1.1367v1.1333h1.1367v-1.1333M611.2,69.5328c.1304.0018.2355.1074.2367.2378v1.37c-.0006.1309-.1069.2367-.2378.2367h-1.3733c-.1307,0-.2367-.106-.2367-.2367v-1.3744c0-.1307.106-.2367.2367-.2367h0l1.3744.0033Z" fill="#fff" isolation="isolate" opacity=".8"/>
+      <path d="M621.8611,75.3495c-.0249-.0246-.0583-.0386-.0933-.0389-.0724.0006-.1306.0598-.13.1322h0v1.5167h0v.1356h-11.1867v1.97h11.1867v1.5389c.0005.0724.0596.1307.1321.1302.0337-.0002.066-.0134.0902-.0368l2.5822-2.5789h0c.0509-.0506.0512-.1329.0006-.1838-.0002-.0002-.0004-.0004-.0006-.0006l-2.5811-2.5844Z" fill="#83b9f9"/>
+    </g>
+  </g>
+  <g id="Text">
+    <g>
+      <rect x="268.4" y="50.8" width="92.9492" height="34.7865" fill="none"/>
+      <path d="M300.4982,61.1637h-1.2715l-1.0391-2.748h-4.1562l-.9775,2.748h-1.2783l3.7598-9.8027h1.1895l3.7734,9.8027ZM297.8117,57.3834l-1.5381-4.1768c-.0498-.1367-.0996-.3555-.1504-.6562h-.0273c-.0449.2778-.0977.4966-.1572.6562l-1.5244,4.1768h3.3975Z" fill="#2f2f2f"/>
+      <path d="M307.6057,60.6031c0,2.5703-1.2305,3.8555-3.6914,3.8555-.8662,0-1.623-.1641-2.2695-.4922v-1.1211c.7881.4375,1.54.6562,2.2559.6562,1.7227,0,2.584-.916,2.584-2.748v-.7656h-.0273c-.5332.8931-1.3359,1.3398-2.4062,1.3398-.8711,0-1.5713-.311-2.1025-.9331-.5303-.6221-.7959-1.457-.7959-2.5054,0-1.1895.2861-2.1353.8574-2.8369.5723-.7017,1.3545-1.0527,2.3486-1.0527.9434,0,1.6426.3784,2.0986,1.1348h.0273v-.9707h1.1211v6.4395ZM306.4846,57.9986v-1.0322c0-.5562-.1885-1.0322-.5645-1.4287s-.8438-.5947-1.4043-.5947c-.6934,0-1.2354.252-1.627.7554-.3926.5034-.5879,1.209-.5879,2.1157,0,.7793.1875,1.4023.5635,1.8696s.874.7007,1.4941.7007c.6289,0,1.1406-.2231,1.5342-.6699.3945-.4468.5918-1.0186.5918-1.7158Z" fill="#2f2f2f"/>
+      <path d="M315.427,57.9439h-4.9424c.0176.7793.2275,1.3809.6289,1.8047.4004.4238.9521.6357,1.6543.6357.7881,0,1.5127-.2598,2.1738-.7793v1.0527c-.6152.4468-1.4287.6699-2.4404.6699-.9893,0-1.7666-.3179-2.3311-.9536-.5654-.6357-.8477-1.5303-.8477-2.6831,0-1.0894.3086-1.9766.9258-2.6626.6182-.686,1.3848-1.0288,2.3008-1.0288s1.624.2964,2.126.8887c.501.5923.752,1.415.752,2.4678v.5879ZM314.2785,56.9937c-.0049-.647-.1611-1.1509-.4688-1.5107s-.7344-.54-1.2812-.54c-.5293,0-.9775.189-1.3467.5674s-.5977.8726-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+      <path d="M322.9201,61.1637h-1.1211v-3.9922c0-1.4858-.543-2.2285-1.627-2.2285-.5605,0-1.0244.2109-1.3916.6323-.3662.4214-.5498.9536-.5498,1.5962v3.9922h-1.1211v-7h1.1211v1.1621h.0273c.5283-.8843,1.2939-1.3262,2.2969-1.3262.7656,0,1.3506.2471,1.7568.7417.4053.4946.6084,1.209.6084,2.1431v4.2793Z" fill="#2f2f2f"/>
+      <path d="M328.1496,61.0953c-.2646.146-.6133.2188-1.0459.2188-1.2266,0-1.8389-.6836-1.8389-2.0508v-4.1426h-1.2031v-.957h1.2031v-1.709l1.1211-.3623v2.0713h1.7637v.957h-1.7637v3.9443c0,.4692.0791.8042.2393,1.0049.1592.2007.4238.3008.793.3008.2822,0,.5264-.0776.7314-.2324v.957Z" fill="#2f2f2f"/>
+      <path d="M330.1047,52.3863c-.2012,0-.3721-.0684-.5127-.2051-.1416-.1367-.2119-.3101-.2119-.5195s.0703-.3838.2119-.5229c.1406-.1392.3115-.2085.5127-.2085.2051,0,.3789.0693.5225.2085s.2158.3135.2158.5229c0,.2007-.0723.3716-.2158.5127s-.3174.2119-.5225.2119ZM330.6516,61.1637h-1.1211v-7h1.1211v7Z" fill="#2f2f2f"/>
+      <path d="M337.5637,60.8424c-.5381.3237-1.1758.4854-1.9141.4854-.998,0-1.8037-.3247-2.417-.9741-.6123-.6494-.9189-1.4912-.9189-2.5259,0-1.1528.3301-2.0791.9912-2.7788.6602-.6997,1.542-1.0493,2.6455-1.0493.6152,0,1.1572.1138,1.627.3418v1.1484c-.5195-.3647-1.0762-.5469-1.668-.5469-.7158,0-1.3027.2563-1.7607.769s-.6865,1.186-.6865,2.02c0,.8203.2148,1.4673.6455,1.9414s1.0088.7109,1.7334.7109c.6104,0,1.1846-.2026,1.7227-.6084v1.0664Z" fill="#2f2f2f"/>
+      <path d="M280.966,72.0982c-.1953-.1504-.4785-.2256-.8477-.2256-.4785,0-.8779.2256-1.1992.6768s-.4824,1.0664-.4824,1.8457v3.5684h-1.1211v-7h1.1211v1.4424h.0273c.1602-.4922.4033-.876.7314-1.1519s.6953-.4136,1.1006-.4136c.292,0,.5156.0317.6699.0957v1.1621Z" fill="#2f2f2f"/>
+      <path d="M287.8088,74.7437h-4.9424c.0186.7793.2285,1.3809.6289,1.8047.4014.4238.9531.6357,1.6543.6357.7891,0,1.5137-.2598,2.1738-.7793v1.0527c-.6152.4468-1.4287.6699-2.4404.6699-.9883,0-1.7656-.3179-2.3311-.9536-.5645-.6357-.8477-1.5303-.8477-2.6831,0-1.0894.3086-1.9766.9268-2.6626.6172-.686,1.3838-1.0288,2.2998-1.0288s1.625.2964,2.126.8887c.502.5923.752,1.415.752,2.4678v.5879ZM286.6604,73.7936c-.0039-.647-.1602-1.1509-.4678-1.5107s-.7354-.54-1.2822-.54c-.5283,0-.9775.189-1.3467.5674s-.5967.8726-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+      <path d="M292.7336,77.8951c-.2646.146-.6133.2188-1.0459.2188-1.2266,0-1.8389-.6836-1.8389-2.0508v-4.1426h-1.2031v-.957h1.2031v-1.709l1.1211-.3623v2.0713h1.7637v.957h-1.7637v3.9443c0,.4692.0791.8042.2393,1.0049.1592.2007.4238.3008.793.3008.2822,0,.5264-.0776.7314-.2324v.957Z" fill="#2f2f2f"/>
+      <path d="M297.7648,72.0982c-.1963-.1504-.4785-.2256-.8477-.2256-.4785,0-.8789.2256-1.2002.6768s-.4814,1.0664-.4814,1.8457v3.5684h-1.1211v-7h1.1211v1.4424h.0273c.1592-.4922.4033-.876.7314-1.1519s.6943-.4136,1.1006-.4136c.291,0,.5146.0317.6699.0957v1.1621Z" fill="#2f2f2f"/>
+      <path d="M299.5822,69.1861c-.2012,0-.3721-.0684-.5127-.2051-.1416-.1367-.2119-.3101-.2119-.5195s.0703-.3838.2119-.5229c.1406-.1392.3115-.2085.5127-.2085.2051,0,.3789.0693.5225.2085s.2158.3135.2158.5229c0,.2007-.0723.3716-.2158.5127s-.3174.2119-.5225.2119ZM300.1291,77.9635h-1.1211v-7h1.1211v7Z" fill="#2f2f2f"/>
+      <path d="M307.924,74.7437h-4.9424c.0176.7793.2275,1.3809.6289,1.8047.4004.4238.9521.6357,1.6543.6357.7881,0,1.5127-.2598,2.1738-.7793v1.0527c-.6152.4468-1.4287.6699-2.4404.6699-.9893,0-1.7666-.3179-2.3311-.9536-.5654-.6357-.8477-1.5303-.8477-2.6831,0-1.0894.3086-1.9766.9258-2.6626.6182-.686,1.3848-1.0288,2.3008-1.0288s1.624.2964,2.126.8887c.501.5923.752,1.415.752,2.4678v.5879ZM306.7756,73.7936c-.0049-.647-.1611-1.1509-.4688-1.5107s-.7344-.54-1.2812-.54c-.5293,0-.9775.189-1.3467.5674s-.5977.8726-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+      <path d="M315.0617,70.9635l-2.7891,7h-1.1006l-2.6523-7h1.2305l1.7773,5.0859c.1318.3735.2139.6997.2461.9775h.0273c.0449-.3511.1182-.6675.2188-.9502l1.8594-5.1133h1.1826Z" fill="#2f2f2f"/>
+      <path d="M321.1789,77.9635h-1.1211v-1.0938h-.0273c-.4873.8384-1.2051,1.2578-2.1533,1.2578-.6973,0-1.2432-.1846-1.6367-.5537-.3945-.3691-.5918-.8589-.5918-1.4697,0-1.3081.7705-2.0688,2.3105-2.2832l2.0986-.2939c0-1.1895-.4805-1.7842-1.4424-1.7842-.8428,0-1.6035.2871-2.2832.8613v-1.1484c.6885-.4375,1.4814-.6562,2.3789-.6562,1.6455,0,2.4678.8706,2.4678,2.6113v4.5527ZM320.0578,74.4225l-1.6885.2324c-.5195.0728-.9111.2017-1.1758.3862-.2637.1846-.3965.5117-.3965.981,0,.3418.1221.6211.3662.8374.2432.2163.5684.3247.9736.3247.5566,0,1.0156-.1948,1.3779-.5845s.543-.8828.543-1.48v-.6973Z" fill="#2f2f2f"/>
+      <path d="M324.3156,77.9635h-1.1211v-10.3633h1.1211v10.3633Z" fill="#2f2f2f"/>
+      <path d="M333.6672,77.8951c-.2637.146-.6123.2188-1.0459.2188-1.2256,0-1.8389-.6836-1.8389-2.0508v-4.1426h-1.2031v-.957h1.2031v-1.709l1.1211-.3623v2.0713h1.7637v.957h-1.7637v3.9443c0,.4692.0801.8042.2393,1.0049.1602.2007.4238.3008.793.3008.2832,0,.5264-.0776.7314-.2324v.957Z" fill="#2f2f2f"/>
+      <path d="M337.925,78.1275c-1.0352,0-1.8604-.3271-2.4785-.981-.6172-.6538-.9258-1.521-.9258-2.6011,0-1.1758.3213-2.0942.9639-2.7549s1.5107-.9912,2.6045-.9912c1.043,0,1.8584.3213,2.4434.9639.5859.6426.8789,1.5337.8789,2.6729,0,1.1167-.3154,2.0107-.9473,2.6831-.6309.6724-1.4775,1.0083-2.5391,1.0083ZM338.007,71.7428c-.7207,0-1.29.2451-1.709.7349-.4199.4897-.6289,1.1655-.6289,2.0269,0,.8296.2119,1.4834.6357,1.9619s.9912.7178,1.7021.7178c.7246,0,1.2812-.2349,1.6709-.7041s.585-1.1372.585-2.0029c0-.875-.1953-1.5493-.585-2.0234s-.9463-.7109-1.6709-.7109Z" fill="#2f2f2f"/>
+      <path d="M346.1174,78.1275c-1.0352,0-1.8604-.3271-2.4785-.981-.6172-.6538-.9258-1.521-.9258-2.6011,0-1.1758.3213-2.0942.9639-2.7549s1.5107-.9912,2.6045-.9912c1.043,0,1.8584.3213,2.4434.9639.5859.6426.8789,1.5337.8789,2.6729,0,1.1167-.3154,2.0107-.9473,2.6831-.6309.6724-1.4775,1.0083-2.5391,1.0083ZM346.1994,71.7428c-.7207,0-1.29.2451-1.709.7349-.4199.4897-.6289,1.1655-.6289,2.0269,0,.8296.2119,1.4834.6357,1.9619s.9912.7178,1.7021.7178c.7246,0,1.2812-.2349,1.6709-.7041s.585-1.1372.585-2.0029c0-.875-.1953-1.5493-.585-2.0234s-.9463-.7109-1.6709-.7109Z" fill="#2f2f2f"/>
+      <path d="M352.4328,77.9635h-1.1211v-10.3633h1.1211v10.3633Z" fill="#2f2f2f"/>
+    </g>
+    <g>
+      <rect x="639.6664" y="104.64" width="84.6673" height="18.36" fill="none"/>
+      <path d="M644.0627,114.6065v-1.3535c.1553.1367.3408.2598.5576.3691.2158.1094.4434.2017.6836.2769.2383.0752.4785.1333.7207.1743s.4648.0615.6699.0615c.707,0,1.2344-.1309,1.582-.3931.3496-.2622.5234-.6392.5234-1.1313,0-.2642-.0586-.4946-.1738-.6904-.1172-.1958-.2773-.375-.4824-.5366s-.4473-.3169-.7285-.4648c-.2793-.1479-.582-.3042-.9053-.4683-.3418-.1733-.6611-.3486-.957-.5264s-.5537-.3735-.7725-.5879-.3906-.457-.5156-.728c-.126-.271-.1885-.5889-.1885-.9536,0-.4468.0986-.835.2939-1.1655s.4531-.6025.7725-.8169.6826-.3735,1.0908-.4785c.4072-.105.8232-.1572,1.2471-.1572.9658,0,1.6709.1162,2.1123.3486v1.292c-.5781-.4009-1.3223-.6016-2.2285-.6016-.25,0-.502.0264-.752.0786s-.4746.1377-.6699.2563-.3555.271-.4785.458-.1846.4146-.1846.6836c0,.2505.0469.4673.1396.6494.0938.1821.2324.3486.4141.499s.4043.2964.666.4375c.2627.1411.5645.2964.9062.4648.3516.1733.6836.3555.998.5469s.5898.4033.8271.6357.4248.4897.5635.7725c.1396.2827.209.606.209.9707,0,.4829-.0947.8921-.2832,1.2271-.1895.335-.4453.6074-.7656.8169-.3223.2095-.6914.3613-1.1113.4546s-.8613.1401-1.3262.1401c-.1543,0-.3457-.0127-.5742-.0376s-.4609-.0615-.6973-.1094-.4609-.1069-.6738-.1777c-.2109-.0708-.3809-.1494-.5088-.2358Z" fill="#2f2f2f"/>
+      <path d="M657.385,111.7833h-4.9424c.0176.7793.2285,1.3809.6289,1.8047s.9531.6357,1.6543.6357c.7891,0,1.5137-.2598,2.1738-.7793v1.0527c-.6152.4468-1.4287.6699-2.4404.6699-.9893,0-1.7666-.3179-2.3311-.9536s-.8477-1.5303-.8477-2.6831c0-1.0894.3086-1.9766.9258-2.6626.6182-.686,1.3848-1.0288,2.3008-1.0288s1.625.2964,2.126.8887.752,1.415.752,2.4678v.5879ZM656.2365,110.8331c-.0049-.647-.1611-1.1509-.4678-1.5107-.3086-.3599-.7354-.54-1.2822-.54-.5283,0-.9775.189-1.3467.5674s-.5977.8726-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+      <path d="M664.0236,115.003h-1.1211v-1.0938h-.0273c-.4873.8384-1.2061,1.2578-2.1533,1.2578-.6973,0-1.2432-.1846-1.6367-.5537-.3945-.3691-.5918-.8589-.5918-1.4697,0-1.3081.7695-2.0688,2.3105-2.2832l2.0986-.2939c0-1.1895-.4814-1.7842-1.4424-1.7842-.8438,0-1.6035.2871-2.2832.8613v-1.1484c.6875-.4375,1.4805-.6562,2.3789-.6562,1.6445,0,2.4678.8706,2.4678,2.6113v4.5527ZM662.9025,111.462l-1.6885.2324c-.5195.0728-.9121.2017-1.1758.3862s-.3965.5117-.3965.981c0,.3418.1221.6211.3652.8374.2441.2163.5684.3247.9746.3247.5566,0,1.0156-.1948,1.377-.5845.3633-.3896.5439-.8828.5439-1.48v-.6973Z" fill="#2f2f2f"/>
+      <path d="M669.6955,109.1378c-.1963-.1504-.4785-.2256-.8477-.2256-.4785,0-.8779.2256-1.2002.6768-.3203.4512-.4814,1.0664-.4814,1.8457v3.5684h-1.1211v-7h1.1211v1.4424h.0273c.1592-.4922.4033-.876.7314-1.1519s.6953-.4136,1.1006-.4136c.292,0,.5146.0317.6699.0957v1.1621Z" fill="#2f2f2f"/>
+      <path d="M675.6535,114.6817c-.5381.3237-1.1758.4854-1.9141.4854-.998,0-1.8047-.3247-2.417-.9741s-.9189-1.4912-.9189-2.5259c0-1.1528.3301-2.0791.9902-2.7788.6611-.6997,1.543-1.0493,2.6465-1.0493.6152,0,1.1572.1138,1.627.3418v1.1484c-.5195-.3647-1.0762-.5469-1.668-.5469-.7158,0-1.3027.2563-1.7607.769s-.6865,1.186-.6865,2.02c0,.8203.2148,1.4673.6455,1.9414s1.0088.7109,1.7334.7109c.6104,0,1.1846-.2026,1.7227-.6084v1.0664Z" fill="#2f2f2f"/>
+      <path d="M682.9514,115.003h-1.1211v-4.0332c0-1.4585-.542-2.1875-1.627-2.1875-.5469,0-1.0068.2109-1.3809.6323s-.5605.9629-.5605,1.6235v3.9648h-1.1211v-10.3633h1.1211v4.5254h.0273c.5381-.8843,1.3037-1.3262,2.2969-1.3262,1.5771,0,2.3652.9502,2.3652,2.8506v4.3135Z" fill="#2f2f2f"/>
+      <path d="M689.4729,106.2257c-.2002,0-.3721-.0684-.5127-.2051s-.2119-.3101-.2119-.5195.0713-.3838.2119-.5229.3125-.2085.5127-.2085c.2051,0,.3799.0693.5225.2085.1445.1392.2158.3135.2158.5229,0,.2007-.0713.3716-.2158.5127-.1426.1411-.3174.2119-.5225.2119ZM690.0197,115.003h-1.1211v-7h1.1211v7Z" fill="#2f2f2f"/>
+      <path d="M697.9484,115.003h-1.1211v-3.9922c0-1.4858-.542-2.2285-1.627-2.2285-.5605,0-1.0234.2109-1.3906.6323s-.5508.9536-.5508,1.5962v3.9922h-1.1211v-7h1.1211v1.1621h.0273c.5293-.8843,1.2949-1.3262,2.2969-1.3262.7656,0,1.3516.2471,1.7578.7417.4053.4946.6074,1.209.6074,2.1431v4.2793Z" fill="#2f2f2f"/>
+      <path d="M706.0227,115.003h-1.1211v-1.1895h-.0273c-.5195.9023-1.3213,1.3535-2.4062,1.3535-.8789,0-1.582-.3135-2.1084-.9399s-.79-1.48-.79-2.5601c0-1.1577.292-2.085.875-2.7822.584-.6973,1.3613-1.0459,2.332-1.0459.9609,0,1.6602.3784,2.0977,1.1348h.0273v-4.334h1.1211v10.3633ZM704.9016,111.838v-1.0322c0-.5649-.1865-1.0435-.5605-1.4355-.373-.3921-.8477-.5879-1.4219-.5879-.6836,0-1.2207.2505-1.6133.752-.3916.5015-.5879,1.1938-.5879,2.0781,0,.8066.1885,1.4434.5645,1.9106s.8809.7007,1.5137.7007c.625,0,1.1318-.2256,1.5215-.6768s.584-1.021.584-1.709Z" fill="#2f2f2f"/>
+      <path d="M713.8449,111.7833h-4.9434c.0186.7793.2285,1.3809.6289,1.8047.4014.4238.9531.6357,1.6543.6357.7891,0,1.5137-.2598,2.1738-.7793v1.0527c-.6152.4468-1.4277.6699-2.4395.6699-.9893,0-1.7666-.3179-2.332-.9536-.5645-.6357-.8477-1.5303-.8477-2.6831,0-1.0894.3086-1.9766.9268-2.6626s1.3838-1.0288,2.2998-1.0288,1.625.2964,2.127.8887c.501.5923.752,1.415.752,2.4678v.5879ZM712.6965,110.8331c-.0049-.647-.1611-1.1509-.4688-1.5107s-.7344-.54-1.2812-.54c-.5293,0-.9785.189-1.3477.5674s-.5967.8726-.6836,1.4834h3.7812Z" fill="#2f2f2f"/>
+      <path d="M720.5852,108.003l-2.3516,3.541,2.3105,3.459h-1.3047l-1.375-2.2695c-.0859-.1411-.1885-.3188-.3066-.5332h-.0273c-.0234.041-.1309.2188-.3223.5332l-1.4004,2.2695h-1.293l2.3867-3.4316-2.2832-3.5684h1.3047l1.3535,2.3926c.1006.1777.1992.3599.2949.5469h.0273l1.75-2.9395h1.2363Z" fill="#2f2f2f"/>
+    </g>
+    <g>
+      <path d="M541.3396,36.3873v-2.1875c.3965.3325.8271.582,1.292.7485s.9341.2495,1.4082.2495c.2778,0,.5205-.0249.728-.0752s.3804-.1196.5195-.2085.2427-.1938.311-.3145.1025-.252.1025-.3931c0-.1914-.0547-.3623-.1641-.5127s-.2588-.2896-.4478-.417-.4136-.2505-.6733-.3691-.54-.2393-.8408-.3623c-.7656-.3188-1.3364-.7085-1.7124-1.1689s-.564-1.0161-.564-1.668c0-.5103.1025-.9492.3076-1.3159s.4844-.6689.8374-.9058.7622-.4111,1.2271-.5229.957-.1675,1.4766-.1675c.5103,0,.9629.0308,1.3569.0923s.7578.1562,1.0903.2837v2.0439c-.1641-.1138-.3428-.2144-.5366-.3008s-.3931-.1582-.5981-.2153-.4092-.0991-.6118-.1265-.3955-.041-.5776-.041c-.2505,0-.4785.0239-.6836.0718s-.3784.1152-.5195.2017-.2505.1904-.3281.311-.1162.2563-.1162.4067c0,.1641.0435.311.1299.4409s.2095.2529.3691.3691.353.23.5811.3418.4854.2266.7725.3452c.3921.1641.7441.3384,1.0562.5229s.5801.3931.8032.6255.394.498.5127.7964.1777.646.1777,1.0425c0,.5469-.1035,1.0059-.311,1.3774s-.4888.6724-.8442.9023-.769.3955-1.2407.4956-.9697.1504-1.4937.1504c-.5376,0-1.0493-.0454-1.5347-.1367s-.9058-.228-1.2612-.4102Z" fill="#2f2f2f"/>
+      <path d="M555.7155,33.8785h-4.5664c.0728,1.0161.7134,1.5244,1.9209,1.5244.77,0,1.4468-.1821,2.0303-.5469v1.5586c-.647.3462-1.4878.5195-2.5225.5195-1.1304,0-2.0073-.3135-2.6318-.9399s-.9365-1.5005-.9365-2.6216c0-1.1621.3374-2.0825,1.0117-2.7617s1.5039-1.0186,2.4883-1.0186c1.021,0,1.8105.3032,2.3687.9092s.8374,1.4287.8374,2.4678v.9092ZM553.7126,32.5523c0-1.0024-.4058-1.5039-1.2168-1.5039-.3462,0-.646.1436-.8989.4307s-.4067.645-.4614,1.0732h2.5771Z" fill="#2f2f2f"/>
+      <path d="M562.8811,36.7633h-2.0439v-1.0049h-.0273c-.4697.7837-1.165,1.1758-2.085,1.1758-.6797,0-1.2139-.1924-1.603-.5776-.3896-.3853-.5845-.8989-.5845-1.5415,0-1.3579.8037-2.1421,2.4131-2.3516l1.9004-.2529c0-.7656-.415-1.1484-1.2441-1.1484-.834,0-1.627.2485-2.3789.7451v-1.627c.3008-.1548.7119-.2915,1.2334-.4102.5225-.1187.9971-.1777,1.4258-.1777,1.9961,0,2.9941.9956,2.9941,2.9873v4.1836ZM560.8508,33.9195v-.4717l-1.2715.1641c-.7021.0913-1.0527.4077-1.0527.9502,0,.2461.085.4478.2559.605s.4023.2358.6943.2358c.4053,0,.7354-.1401.9912-.4204.2549-.2803.3828-.6348.3828-1.063Z" fill="#2f2f2f"/>
+      <path d="M569.1438,31.7115c-.2598-.1411-.5635-.2119-.9092-.2119-.4697,0-.8369.1719-1.1006.5161-.2646.3442-.3965.8125-.3965,1.4048v3.3428h-2.1602v-7h2.1602v1.2988h.0273c.3418-.9478.957-1.4219,1.8457-1.4219.2275,0,.4053.0273.5332.082v1.9893Z" fill="#2f2f2f"/>
+      <path d="M575.5178,36.5104c-.4883.2827-1.1924.4238-2.1123.4238-1.0762,0-1.9463-.3257-2.6113-.9775-.666-.6519-.998-1.4927-.998-2.5225,0-1.1895.3564-2.127,1.0693-2.813.7139-.686,1.667-1.0288,2.8613-1.0288.8242,0,1.4219.1094,1.791.3281v1.832c-.4512-.3374-.9551-.5059-1.5107-.5059-.6201,0-1.1113.1812-1.4736.5435s-.543.8623-.543,1.5005c0,.6196.1729,1.1064.5195,1.4595.3457.353.8223.5298,1.4287.5298.5371,0,1.0635-.1685,1.5791-.5059v1.7363Z" fill="#2f2f2f"/>
+      <path d="M583.7541,36.7633h-2.1533v-3.9785c0-1.0254-.373-1.5381-1.1211-1.5381-.3828,0-.6924.1436-.9297.4307-.2363.2871-.3555.6519-.3555,1.0938v3.9922h-2.1602v-10.3633h2.1602v4.4023h.0273c.5293-.8066,1.2471-1.21,2.1533-1.21,1.5859,0,2.3789.957,2.3789,2.8711v4.2998Z" fill="#2f2f2f"/>
+      <path d="M588.8674,36.5787v-1.75c.3555.2144.71.3735,1.0635.4785.3525.105.6865.1572,1.001.1572.3828,0,.6846-.0522.9062-.1572.2207-.105.3311-.2642.3311-.4785,0-.1367-.0498-.2505-.1504-.3418-.0996-.0913-.2285-.1709-.3857-.2393s-.3291-.1299-.5166-.1846c-.1865-.0547-.3662-.1162-.54-.1846-.2773-.105-.5225-.2178-.7344-.3384s-.3896-.2607-.5332-.4204-.2529-.3442-.3281-.5537-.1133-.458-.1133-.7451c0-.3921.0859-.729.2568-1.0117s.3984-.5137.6836-.6938c.2842-.1802.6104-.312.9775-.3965.3662-.0845.748-.1265,1.1445-.1265.3105,0,.625.0239.9434.0718.3193.0479.6338.1172.9434.2085v1.668c-.2734-.1597-.5664-.2793-.8779-.3589-.3125-.0796-.6191-.1196-.9199-.1196-.1406,0-.2744.0127-.3994.0376-.126.0249-.2363.0615-.332.1094s-.1709.1094-.2256.1846-.082.1606-.082.2563c0,.1274.041.2368.123.3281s.1895.1699.3213.2358c.1328.0659.2793.1255.4414.1777.1611.0522.3223.106.4814.1606.2871.1001.5469.2095.7793.3281s.4316.2573.5986.417c.166.1597.2939.3462.3828.5605s.1328.4692.1328.7656c0,.4146-.0898.769-.2695,1.063-.1807.2939-.4199.5332-.7178.7178-.2988.1846-.6426.3188-1.0322.4033s-.7939.1265-1.2139.1265c-.7695,0-1.4834-.1187-2.1396-.3555Z" fill="#2f2f2f"/>
+      <path d="M601.8176,33.8785h-4.5664c.0723,1.0161.7129,1.5244,1.9209,1.5244.7695,0,1.4463-.1821,2.0303-.5469v1.5586c-.6475.3462-1.4883.5195-2.5225.5195-1.1309,0-2.0078-.3135-2.6318-.9399-.625-.6265-.9365-1.5005-.9365-2.6216,0-1.1621.3369-2.0825,1.0117-2.7617.6738-.6792,1.5039-1.0186,2.4883-1.0186,1.0205,0,1.8105.3032,2.3682.9092.5586.606.8379,1.4287.8379,2.4678v.9092ZM599.8146,32.5523c0-1.0024-.4062-1.5039-1.2168-1.5039-.3467,0-.6465.1436-.8994.4307s-.4062.645-.4609,1.0732h2.5771Z" fill="#2f2f2f"/>
+      <path d="M607.7482,31.7115c-.2598-.1411-.5625-.2119-.9092-.2119-.4688,0-.8359.1719-1.1006.5161-.2637.3442-.3965.8125-.3965,1.4048v3.3428h-2.1602v-7h2.1602v1.2988h.0273c.3418-.9478.957-1.4219,1.8457-1.4219.2285,0,.4062.0273.5332.082v1.9893Z" fill="#2f2f2f"/>
+      <path d="M615.8469,29.7633l-2.6045,7h-2.4609l-2.4814-7h2.3105l1.2168,4.3135c.1367.4878.2168.9023.2393,1.2441h.0273c.0322-.3237.1162-.7246.2529-1.2031l1.2441-4.3545h2.2559Z" fill="#2f2f2f"/>
+      <path d="M617.8928,28.6559c-.3643,0-.6631-.1084-.8955-.3247s-.3486-.4819-.3486-.7964c0-.3237.1162-.5879.3486-.793s.5312-.3076.8955-.3076c.3691,0,.6689.1025.8994.3076.2295.2051.3447.4692.3447.793,0,.3281-.1152.5972-.3447.8066-.2305.2095-.5303.3145-.8994.3145ZM618.9592,36.7633h-2.1602v-7h2.1602v7Z" fill="#2f2f2f"/>
+      <path d="M626.0393,36.5104c-.4883.2827-1.1924.4238-2.1123.4238-1.0762,0-1.9463-.3257-2.6113-.9775-.666-.6519-.998-1.4927-.998-2.5225,0-1.1895.3564-2.127,1.0693-2.813.7139-.686,1.667-1.0288,2.8613-1.0288.8242,0,1.4219.1094,1.791.3281v1.832c-.4512-.3374-.9551-.5059-1.5107-.5059-.6201,0-1.1113.1812-1.4736.5435s-.543.8623-.543,1.5005c0,.6196.1729,1.1064.5195,1.4595.3457.353.8223.5298,1.4287.5298.5371,0,1.0635-.1685,1.5791-.5059v1.7363Z" fill="#2f2f2f"/>
+      <path d="M633.7541,33.8785h-4.5664c.0732,1.0161.7139,1.5244,1.9209,1.5244.7705,0,1.4473-.1821,2.0303-.5469v1.5586c-.6465.3462-1.4873.5195-2.5225.5195-1.1299,0-2.0068-.3135-2.6318-.9399-.624-.6265-.9365-1.5005-.9365-2.6216,0-1.1621.3379-2.0825,1.0117-2.7617.6748-.6792,1.5039-1.0186,2.4883-1.0186,1.0215,0,1.8105.3032,2.3691.9092.5576.606.8369,1.4287.8369,2.4678v.9092ZM631.7512,32.5523c0-1.0024-.4053-1.5039-1.2168-1.5039-.3457,0-.6455.1436-.8984.4307s-.4072.645-.4619,1.0732h2.5771Z" fill="#2f2f2f"/>
+    </g>
+    <g>
+      <rect x="15.2658" y="29.5396" width="92.9492" height="34.7865" fill="none"/>
+      <path d="M29.6091,39.4928c-.7246.3828-1.627.5742-2.707.5742-1.3945,0-2.5112-.4487-3.3496-1.3467s-1.2578-2.0757-1.2578-3.5342c0-1.5679.4717-2.8345,1.415-3.8008s2.1396-1.4492,3.5889-1.4492c.9297,0,1.6997.1343,2.3105.4033v1.2236c-.7017-.3921-1.4766-.5879-2.3242-.5879-1.1255,0-2.0381.376-2.7378,1.1279s-1.0493,1.7568-1.0493,3.0146c0,1.1938.3271,2.1455.981,2.854s1.5117,1.063,2.5737,1.063c.9844,0,1.8364-.2188,2.5566-.6562v1.1143Z" fill="#2f2f2f"/>
+      <path d="M34.1579,40.067c-1.0347,0-1.8604-.3271-2.478-.981s-.9263-1.521-.9263-2.6011c0-1.1758.3213-2.0942.9639-2.7549s1.5107-.9912,2.6045-.9912c1.0435,0,1.8584.3213,2.4438.9639s.8784,1.5337.8784,2.6729c0,1.1167-.3154,2.0107-.9468,2.6831s-1.4775,1.0083-2.5396,1.0083ZM34.2399,33.6822c-.7202,0-1.2896.2451-1.709.7349s-.6289,1.1655-.6289,2.0269c0,.8296.2119,1.4834.6357,1.9619s.9912.7178,1.7021.7178c.7246,0,1.2817-.2349,1.6714-.7041s.5845-1.1372.5845-2.0029c0-.875-.1948-1.5493-.5845-2.0234s-.9468-.7109-1.6714-.7109Z" fill="#2f2f2f"/>
+      <path d="M45.1701,39.9029h-1.1211v-3.9922c0-1.4858-.5425-2.2285-1.627-2.2285-.5605,0-1.0244.2109-1.3911.6323s-.5503.9536-.5503,1.5962v3.9922h-1.1211v-7h1.1211v1.1621h.0273c.5288-.8843,1.2944-1.3262,2.2969-1.3262.7656,0,1.3511.2471,1.7568.7417s.6084,1.209.6084,2.1431v4.2793Z" fill="#2f2f2f"/>
+      <path d="M52.591,32.9029l-2.7891,7h-1.1006l-2.6523-7h1.2305l1.7773,5.0859c.1323.3735.2144.6997.2461.9775h.0273c.0454-.3511.1187-.6675.2188-.9502l1.8594-5.1133h1.1826Z" fill="#2f2f2f"/>
+      <path d="M59.2326,36.6832h-4.9424c.0181.7793.228,1.3809.6289,1.8047s.9526.6357,1.6543.6357c.7886,0,1.5132-.2598,2.1738-.7793v1.0527c-.6152.4468-1.4287.6699-2.4404.6699-.9888,0-1.7661-.3179-2.3311-.9536s-.8477-1.5303-.8477-2.6831c0-1.0894.3086-1.9766.9263-2.6626s1.3843-1.0288,2.3003-1.0288,1.6245.2964,2.126.8887.752,1.415.752,2.4678v.5879ZM58.0842,35.733c-.0044-.647-.1606-1.1509-.4683-1.5107s-.7349-.54-1.2817-.54c-.5288,0-.9775.189-1.3467.5674s-.5972.8726-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+      <path d="M64.5656,34.0377c-.1958-.1504-.4785-.2256-.8477-.2256-.4785,0-.8784.2256-1.1997.6768s-.4819,1.0664-.4819,1.8457v3.5684h-1.1211v-7h1.1211v1.4424h.0273c.1597-.4922.4033-.876.7314-1.1519s.6948-.4136,1.1006-.4136c.2915,0,.5151.0317.6699.0957v1.1621Z" fill="#2f2f2f"/>
+      <path d="M65.5671,39.65v-1.2031c.6108.4512,1.2827.6768,2.0166.6768.9844,0,1.4766-.3281,1.4766-.9844,0-.187-.042-.3452-.1265-.4751s-.1982-.2451-.3418-.3452-.312-.1904-.5059-.27-.4023-.1631-.6255-.2495c-.3101-.123-.582-.2471-.8169-.3726s-.4307-.2666-.5879-.4238-.2759-.3359-.3555-.5366-.1196-.4351-.1196-.7041c0-.3281.0752-.6187.2256-.8716s.3511-.4648.6016-.6357.5366-.2998.8579-.3862.6528-.1299.9946-.1299c.606,0,1.1484.105,1.627.3145v1.1348c-.5151-.3374-1.1074-.5059-1.7773-.5059-.2095,0-.3989.0239-.5674.0718s-.3135.1152-.4341.2017-.2144.1904-.2803.311-.0991.2539-.0991.3999c0,.1821.0332.335.0991.458s.1631.2324.2905.3281.2827.1821.4648.2598.3896.1616.6221.2529c.3101.1187.5879.2402.834.3657s.4556.2666.6289.4238.3066.3384.3999.5435.1401.4487.1401.7314c0,.3462-.0762.647-.229.9023s-.3564.4673-.6118.6357-.5493.2939-.8818.376-.6812.123-1.0459.123c-.7202,0-1.3442-.1392-1.873-.417Z" fill="#2f2f2f"/>
+      <path d="M76.9841,39.9029h-1.1211v-1.0938h-.0273c-.4878.8384-1.2056,1.2578-2.1533,1.2578-.6973,0-1.2432-.1846-1.6372-.5537s-.5913-.8589-.5913-1.4697c0-1.3081.77-2.0688,2.3105-2.2832l2.0986-.2939c0-1.1895-.481-1.7842-1.4424-1.7842-.8433,0-1.604.2871-2.2832.8613v-1.1484c.688-.4375,1.481-.6562,2.3789-.6562,1.645,0,2.4678.8706,2.4678,2.6113v4.5527ZM75.863,36.3619l-1.6885.2324c-.5195.0728-.9116.2017-1.1758.3862s-.3965.5117-.3965.981c0,.3418.1221.6211.3657.8374s.5684.3247.9741.3247c.5562,0,1.0151-.1948,1.3774-.5845s.5435-.8828.5435-1.48v-.6973Z" fill="#2f2f2f"/>
+      <path d="M82.2429,39.8346c-.2642.146-.6128.2188-1.0459.2188-1.2261,0-1.8389-.6836-1.8389-2.0508v-4.1426h-1.2031v-.957h1.2031v-1.709l1.1211-.3623v2.0713h1.7637v.957h-1.7637v3.9443c0,.4692.0796.8042.2393,1.0049s.4238.3008.793.3008c.2827,0,.5264-.0776.7314-.2324v.957Z" fill="#2f2f2f"/>
+      <path d="M84.1979,31.1256c-.2007,0-.3716-.0684-.5127-.2051s-.2119-.3101-.2119-.5195.0708-.3838.2119-.5229.312-.2085.5127-.2085c.2051,0,.3794.0693.5229.2085s.2153.3135.2153.5229c0,.2007-.0718.3716-.2153.5127s-.3179.2119-.5229.2119ZM84.7448,39.9029h-1.1211v-7h1.1211v7Z" fill="#2f2f2f"/>
+      <path d="M89.8391,40.067c-1.0347,0-1.8604-.3271-2.478-.981s-.9263-1.521-.9263-2.6011c0-1.1758.3213-2.0942.9639-2.7549s1.5107-.9912,2.6045-.9912c1.0435,0,1.8584.3213,2.4438.9639s.8784,1.5337.8784,2.6729c0,1.1167-.3154,2.0107-.9468,2.6831s-1.4775,1.0083-2.5396,1.0083ZM89.9211,33.6822c-.7202,0-1.2896.2451-1.709.7349s-.6289,1.1655-.6289,2.0269c0,.8296.2119,1.4834.6357,1.9619s.9912.7178,1.7021.7178c.7246,0,1.2817-.2349,1.6714-.7041s.5845-1.1372.5845-2.0029c0-.875-.1948-1.5493-.5845-2.0234s-.9468-.7109-1.6714-.7109Z" fill="#2f2f2f"/>
+      <path d="M100.8513,39.9029h-1.1211v-3.9922c0-1.4858-.5425-2.2285-1.627-2.2285-.5605,0-1.0244.2109-1.3911.6323s-.5503.9536-.5503,1.5962v3.9922h-1.1211v-7h1.1211v1.1621h.0273c.5288-.8843,1.2944-1.3262,2.2969-1.3262.7656,0,1.3511.2471,1.7568.7417s.6084,1.209.6084,2.1431v4.2793Z" fill="#2f2f2f"/>
+      <path d="M47.7028,56.7027h-1.1211v-4.0332c0-1.4585-.5425-2.1875-1.627-2.1875-.5469,0-1.0073.2109-1.3809.6323s-.5605.9629-.5605,1.6235v3.9648h-1.1211v-10.3633h1.1211v4.5254h.0273c.5376-.8843,1.3032-1.3262,2.2969-1.3262,1.5767,0,2.3652.9502,2.3652,2.8506v4.3135Z" fill="#2f2f2f"/>
+      <path d="M50.2873,47.9254c-.2007,0-.3716-.0684-.5127-.2051s-.2119-.3101-.2119-.5195.0708-.3838.2119-.5229.312-.2085.5127-.2085c.2051,0,.3794.0693.5229.2085s.2153.3135.2153.5229c0,.2007-.0718.3716-.2153.5127s-.3179.2119-.5229.2119ZM50.8342,56.7027h-1.1211v-7h1.1211v7Z" fill="#2f2f2f"/>
+      <path d="M52.551,56.4498v-1.2031c.6108.4512,1.2827.6768,2.0166.6768.9844,0,1.4766-.3281,1.4766-.9844,0-.187-.042-.3452-.1265-.4751s-.1982-.2451-.3418-.3452-.312-.1904-.5059-.27-.4023-.1631-.6255-.2495c-.3101-.123-.582-.2471-.8169-.3726s-.4307-.2666-.5879-.4238-.2759-.3359-.3555-.5366-.1196-.4351-.1196-.7041c0-.3281.0752-.6187.2256-.8716s.3511-.4648.6016-.6357.5366-.2998.8579-.3862.6528-.1299.9946-.1299c.606,0,1.1484.105,1.627.3145v1.1348c-.5151-.3374-1.1074-.5059-1.7773-.5059-.2095,0-.3989.0239-.5674.0718s-.3135.1152-.4341.2017-.2144.1904-.2803.311-.0991.2539-.0991.3999c0,.1821.0332.335.0991.458s.1631.2324.2905.3281.2827.1821.4648.2598.3896.1616.6221.2529c.3101.1187.5879.2402.834.3657s.4556.2666.6289.4238.3066.3384.3999.5435.1401.4487.1401.7314c0,.3462-.0762.647-.229.9023s-.3564.4673-.6118.6357-.5493.2939-.8818.376-.6812.123-1.0459.123c-.7202,0-1.3442-.1392-1.873-.417Z" fill="#2f2f2f"/>
+      <path d="M62.2043,56.6344c-.2642.146-.6128.2188-1.0459.2188-1.2261,0-1.8389-.6836-1.8389-2.0508v-4.1426h-1.2031v-.957h1.2031v-1.709l1.1211-.3623v2.0713h1.7637v.957h-1.7637v3.9443c0,.4692.0796.8042.2393,1.0049s.4238.3008.793.3008c.2827,0,.5264-.0776.7314-.2324v.957Z" fill="#2f2f2f"/>
+      <path d="M66.4621,56.8668c-1.0347,0-1.8604-.3271-2.478-.981s-.9263-1.521-.9263-2.6011c0-1.1758.3213-2.0942.9639-2.7549s1.5107-.9912,2.6045-.9912c1.0435,0,1.8584.3213,2.4438.9639s.8784,1.5337.8784,2.6729c0,1.1167-.3154,2.0107-.9468,2.6831s-1.4775,1.0083-2.5396,1.0083ZM66.5441,50.482c-.7202,0-1.2896.2451-1.709.7349s-.6289,1.1655-.6289,2.0269c0,.8296.2119,1.4834.6357,1.9619s.9912.7178,1.7021.7178c.7246,0,1.2817-.2349,1.6714-.7041s.5845-1.1372.5845-2.0029c0-.875-.1948-1.5493-.5845-2.0234s-.9468-.7109-1.6714-.7109Z" fill="#2f2f2f"/>
+      <path d="M75.3142,50.8375c-.1958-.1504-.4785-.2256-.8477-.2256-.4785,0-.8784.2256-1.1997.6768s-.4819,1.0664-.4819,1.8457v3.5684h-1.1211v-7h1.1211v1.4424h.0273c.1597-.4922.4033-.876.7314-1.1519s.6948-.4136,1.1006-.4136c.2915,0,.5151.0317.6699.0957v1.1621Z" fill="#2f2f2f"/>
+      <path d="M82.655,49.7027l-3.2197,8.1211c-.5742,1.4492-1.3809,2.1738-2.4199,2.1738-.2915,0-.5356-.0298-.7314-.0889v-1.0049c.2417.082.4624.123.6631.123.5649,0,.9888-.3374,1.2715-1.0117l.5605-1.3262-2.7344-6.9863h1.2441l1.8936,5.3867c.0229.0684.0708.2461.1436.5332h.041c.0229-.1094.0684-.2827.1367-.5195l1.9893-5.4004h1.1621Z" fill="#2f2f2f"/>
+    </g>
+    <g>
+      <rect x="15.6889" y="171.4517" width="92.103" height="30.9483" fill="none"/>
+      <path d="M52.1706,181.8146h-1.2715l-1.0391-2.748h-4.1562l-.9775,2.748h-1.2783l3.7598-9.8027h1.1895l3.7734,9.8027ZM49.4841,178.0343l-1.5381-4.1768c-.0503-.1367-.1001-.3555-.1504-.6562h-.0273c-.0454.2778-.0981.4966-.1572.6562l-1.5244,4.1768h3.3975Z" fill="#2f2f2f"/>
+      <path d="M59.2775,181.254c0,2.5703-1.2305,3.8555-3.6914,3.8555-.8657,0-1.6226-.1641-2.2695-.4922v-1.1211c.7886.4375,1.5405.6562,2.2559.6562,1.7227,0,2.584-.916,2.584-2.748v-.7656h-.0273c-.5332.8931-1.3354,1.3398-2.4062,1.3398-.8706,0-1.5713-.311-2.1021-.9331s-.7964-1.457-.7964-2.5054c0-1.1895.2861-2.1353.8579-2.8369s1.3545-1.0527,2.3481-1.0527c.9434,0,1.6431.3784,2.0986,1.1348h.0273v-.9707h1.1211v6.4395ZM58.1564,178.6495v-1.0322c0-.5562-.188-1.0322-.564-1.4287s-.8442-.5947-1.4048-.5947c-.6929,0-1.2349.252-1.627.7554s-.5879,1.209-.5879,2.1157c0,.7793.188,1.4023.564,1.8696s.874.7007,1.4937.7007c.6289,0,1.1406-.2231,1.5347-.6699s.5913-1.0186.5913-1.7158Z" fill="#2f2f2f"/>
+      <path d="M67.0988,178.5948h-4.9424c.0181.7793.228,1.3809.6289,1.8047s.9526.6357,1.6543.6357c.7886,0,1.5132-.2598,2.1738-.7793v1.0527c-.6152.4468-1.4287.6699-2.4404.6699-.9888,0-1.7661-.3179-2.3311-.9536s-.8477-1.5303-.8477-2.6831c0-1.0894.3086-1.9766.9263-2.6626s1.3843-1.0288,2.3003-1.0288,1.6245.2964,2.126.8887.752,1.415.752,2.4678v.5879ZM65.9504,177.6446c-.0044-.647-.1606-1.1509-.4683-1.5107s-.7349-.54-1.2817-.54c-.5288,0-.9775.189-1.3467.5674s-.5972.8726-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+      <path d="M74.592,181.8146h-1.1211v-3.9922c0-1.4858-.5425-2.2285-1.627-2.2285-.5605,0-1.0244.2109-1.3911.6323s-.5503.9536-.5503,1.5962v3.9922h-1.1211v-7h1.1211v1.1621h.0273c.5288-.8843,1.2944-1.3262,2.2969-1.3262.7656,0,1.3511.2471,1.7568.7417s.6084,1.209.6084,2.1431v4.2793Z" fill="#2f2f2f"/>
+      <path d="M79.8215,181.7462c-.2642.146-.6128.2188-1.0459.2188-1.2261,0-1.8389-.6836-1.8389-2.0508v-4.1426h-1.2031v-.957h1.2031v-1.709l1.1211-.3623v2.0713h1.7637v.957h-1.7637v3.9443c0,.4692.0796.8042.2393,1.0049s.4238.3008.793.3008c.2827,0,.5264-.0776.7314-.2324v.957Z" fill="#2f2f2f"/>
+      <path d="M38.8176,192.7491c-.1958-.1504-.4785-.2256-.8477-.2256-.4785,0-.8784.2256-1.1997.6768s-.4819,1.0664-.4819,1.8457v3.5684h-1.1211v-7h1.1211v1.4424h.0273c.1597-.4922.4033-.876.7314-1.1519s.6948-.4136,1.1006-.4136c.2915,0,.5151.0317.6699.0957v1.1621Z" fill="#2f2f2f"/>
+      <path d="M45.6604,195.3946h-4.9424c.0181.7793.228,1.3809.6289,1.8047s.9526.6357,1.6543.6357c.7886,0,1.5132-.2598,2.1738-.7793v1.0527c-.6152.4468-1.4287.6699-2.4404.6699-.9888,0-1.7661-.3179-2.3311-.9536s-.8477-1.5303-.8477-2.6831c0-1.0894.3086-1.9766.9263-2.6626s1.3843-1.0288,2.3003-1.0288,1.6245.2964,2.126.8887.752,1.415.752,2.4678v.5879ZM44.5119,194.4444c-.0044-.647-.1606-1.1509-.4683-1.5107s-.7349-.54-1.2817-.54c-.5288,0-.9775.189-1.3467.5674s-.5972.8726-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+      <path d="M46.9025,198.3614v-1.2031c.6108.4512,1.2827.6768,2.0166.6768.9844,0,1.4766-.3281,1.4766-.9844,0-.187-.042-.3452-.1265-.4751s-.1982-.2451-.3418-.3452-.312-.1904-.5059-.27-.4023-.1631-.6255-.2495c-.3101-.123-.582-.2471-.8169-.3726s-.4307-.2666-.5879-.4238-.2759-.3359-.3555-.5366-.1196-.4351-.1196-.7041c0-.3281.0752-.6187.2256-.8716s.3511-.4648.6016-.6357.5366-.2998.8579-.3862.6528-.1299.9946-.1299c.606,0,1.1484.105,1.627.3145v1.1348c-.5151-.3374-1.1074-.5059-1.7773-.5059-.2095,0-.3989.0239-.5674.0718s-.3135.1152-.4341.2017-.2144.1904-.2803.311-.0991.2539-.0991.3999c0,.1821.0332.335.0991.458s.1631.2324.2905.3281.2827.1821.4648.2598.3896.1616.6221.2529c.3101.1187.5879.2402.834.3657s.4556.2666.6289.4238.3066.3384.3999.5435.1401.4487.1401.7314c0,.3462-.0762.647-.229.9023s-.3564.4673-.6118.6357-.5493.2939-.8818.376-.6812.123-1.0459.123c-.7202,0-1.3442-.1392-1.873-.417Z" fill="#2f2f2f"/>
+      <path d="M54.2766,197.6026h-.0273v4.2314h-1.1211v-10.2197h1.1211v1.2305h.0273c.5513-.9297,1.3579-1.3945,2.4199-1.3945.9023,0,1.6064.3135,2.1123.9399s.7588,1.4663.7588,2.519c0,1.1714-.2847,2.1089-.8545,2.813s-1.3491,1.0562-2.3379,1.0562c-.9067,0-1.6064-.3921-2.0986-1.1758ZM54.2492,194.7794v.9775c0,.5786.188,1.0698.564,1.4731s.8535.605,1.4321.605c.6792,0,1.2109-.2598,1.5962-.7793s.5776-1.2417.5776-2.167c0-.7793-.1802-1.3901-.54-1.832s-.8477-.6631-1.4629-.6631c-.6519,0-1.1758.2266-1.5723.6802s-.5947,1.022-.5947,1.7056Z" fill="#2f2f2f"/>
+      <path d="M64.2731,198.7784c-1.0347,0-1.8604-.3271-2.478-.981s-.9263-1.521-.9263-2.6011c0-1.1758.3213-2.0942.9639-2.7549s1.5107-.9912,2.6045-.9912c1.0435,0,1.8584.3213,2.4438.9639s.8784,1.5337.8784,2.6729c0,1.1167-.3154,2.0107-.9468,2.6831s-1.4775,1.0083-2.5396,1.0083ZM64.3552,192.3937c-.7202,0-1.2896.2451-1.709.7349s-.6289,1.1655-.6289,2.0269c0,.8296.2119,1.4834.6357,1.9619s.9912.7178,1.7021.7178c.7246,0,1.2817-.2349,1.6714-.7041s.5845-1.1372.5845-2.0029c0-.875-.1948-1.5493-.5845-2.0234s-.9468-.7109-1.6714-.7109Z" fill="#2f2f2f"/>
+      <path d="M75.2854,198.6144h-1.1211v-3.9922c0-1.4858-.5425-2.2285-1.627-2.2285-.5605,0-1.0244.2109-1.3911.6323s-.5503.9536-.5503,1.5962v3.9922h-1.1211v-7h1.1211v1.1621h.0273c.5288-.8843,1.2944-1.3262,2.2969-1.3262.7656,0,1.3511.2471,1.7568.7417s.6084,1.209.6084,2.1431v4.2793Z" fill="#2f2f2f"/>
+      <path d="M76.9333,198.3614v-1.2031c.6108.4512,1.2827.6768,2.0166.6768.9844,0,1.4766-.3281,1.4766-.9844,0-.187-.042-.3452-.1265-.4751s-.1982-.2451-.3418-.3452-.312-.1904-.5059-.27-.4023-.1631-.6255-.2495c-.3101-.123-.582-.2471-.8169-.3726s-.4307-.2666-.5879-.4238-.2759-.3359-.3555-.5366-.1196-.4351-.1196-.7041c0-.3281.0752-.6187.2256-.8716s.3511-.4648.6016-.6357.5366-.2998.8579-.3862.6528-.1299.9946-.1299c.606,0,1.1484.105,1.627.3145v1.1348c-.5151-.3374-1.1074-.5059-1.7773-.5059-.2095,0-.3989.0239-.5674.0718s-.3135.1152-.4341.2017-.2144.1904-.2803.311-.0991.2539-.0991.3999c0,.1821.0332.335.0991.458s.1631.2324.2905.3281.2827.1821.4648.2598.3896.1616.6221.2529c.3101.1187.5879.2402.834.3657s.4556.2666.6289.4238.3066.3384.3999.5435.1401.4487.1401.7314c0,.3462-.0762.647-.229.9023s-.3564.4673-.6118.6357-.5493.2939-.8818.376-.6812.123-1.0459.123c-.7202,0-1.3442-.1392-1.873-.417Z" fill="#2f2f2f"/>
+      <path d="M88.8884,195.3946h-4.9424c.0181.7793.228,1.3809.6289,1.8047s.9526.6357,1.6543.6357c.7886,0,1.5132-.2598,2.1738-.7793v1.0527c-.6152.4468-1.4287.6699-2.4404.6699-.9888,0-1.7661-.3179-2.3311-.9536s-.8477-1.5303-.8477-2.6831c0-1.0894.3086-1.9766.9263-2.6626s1.3843-1.0288,2.3003-1.0288,1.6245.2964,2.126.8887.752,1.415.752,2.4678v.5879ZM87.7399,194.4444c-.0044-.647-.1606-1.1509-.4683-1.5107s-.7349-.54-1.2817-.54c-.5288,0-.9775.189-1.3467.5674s-.5972.8726-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+    </g>
+    <g>
+      <path d="M188.2492,46.9327h-2.4062l-.6973-2.1807h-3.4863l-.6904,2.1807h-2.3926l3.5684-9.8027h2.6182l3.4863,9.8027ZM184.6398,43.0567l-1.0527-3.2949c-.0776-.2461-.1323-.54-.1641-.8818h-.0547c-.0229.2871-.0796.5718-.1709.8545l-1.0664,3.3223h2.5088Z" fill="#2f2f2f"/>
+      <path d="M195.9899,46.1329c0,1.2988-.376,2.3047-1.1279,3.0181s-1.8413,1.0698-3.2676,1.0698c-.9434,0-1.6909-.1343-2.2422-.4033v-1.8184c.7202.4194,1.4468.6289,2.1807.6289.729,0,1.2944-.1924,1.6953-.5776s.6016-.9082.6016-1.5688v-.5537h-.0273c-.4922.7837-1.2192,1.1758-2.1807,1.1758-.8931,0-1.6021-.3145-2.126-.9434s-.7861-1.4722-.7861-2.5293c0-1.1851.2915-2.126.875-2.8232s1.3511-1.0459,2.3037-1.0459c.8521,0,1.4902.3281,1.9141.9844h.0273v-.8135h2.1602v6.2002ZM193.8571,43.5694v-.5537c0-.4419-.1309-.8193-.3931-1.1313s-.6025-.4683-1.022-.4683c-.4785,0-.8545.187-1.1279.5605s-.4102.8999-.4102,1.5791c0,.5835.1299,1.0449.3896,1.3843s.6152.5093,1.0664.5093c.4468,0,.8076-.1719,1.0835-.5161s.4136-.7988.4136-1.3638Z" fill="#2f2f2f"/>
+      <path d="M204.0837,44.0479h-4.5664c.0728,1.0161.7134,1.5244,1.9209,1.5244.77,0,1.4468-.1821,2.0303-.5469v1.5586c-.647.3462-1.4878.5195-2.5225.5195-1.1304,0-2.0073-.3135-2.6318-.9399s-.9365-1.5005-.9365-2.6216c0-1.1621.3374-2.0825,1.0117-2.7617s1.5039-1.0186,2.4883-1.0186c1.021,0,1.8105.3032,2.3687.9092s.8374,1.4287.8374,2.4678v.9092ZM202.0808,42.7218c0-1.0024-.4058-1.5039-1.2168-1.5039-.3462,0-.646.1436-.8989.4307s-.4067.645-.4614,1.0732h2.5771Z" fill="#2f2f2f"/>
+      <path d="M212.2092,46.9327h-2.1533v-3.8896c0-1.0845-.3872-1.627-1.1621-1.627-.3735,0-.6812.1436-.9229.4307s-.3623.6519-.3623,1.0938v3.9922h-2.1602v-7h2.1602v1.1074h.0273c.5151-.8521,1.2646-1.2783,2.249-1.2783,1.5493,0,2.3242.9614,2.3242,2.8848v4.2861Z" fill="#2f2f2f"/>
+      <path d="M218.0588,46.8507c-.3188.1685-.7998.2529-1.4424.2529-1.522,0-2.2832-.7905-2.2832-2.3721v-3.2061h-1.1348v-1.5928h1.1348v-1.5107l2.1533-.6152v2.126h1.5723v1.5928h-1.5723v2.8301c0,.729.2896,1.0938.8682,1.0938.228,0,.4624-.0659.7041-.1982v1.5996Z" fill="#2f2f2f"/>
+    </g>
+    <g>
+      <rect x="425.5378" y="63.4" width="94.9243" height="33.2" fill="none"/>
+      <path d="M446.8015,73.7633h-1.5996l-3.7871-4.4844c-.1411-.1685-.228-.2827-.2598-.3418h-.0273v4.8262h-1.1484v-9.8027h1.1484v4.6074h.0273c.064-.1001.1504-.2119.2598-.335l3.6641-4.2725h1.4287l-4.2041,4.7031,4.498,5.0996Z" fill="#2f2f2f"/>
+      <path d="M453.819,73.7633h-1.1211v-3.9922c0-1.4858-.5425-2.2285-1.627-2.2285-.5605,0-1.0244.2109-1.3911.6323s-.5503.9536-.5503,1.5962v3.9922h-1.1211v-7h1.1211v1.1621h.0273c.5288-.8843,1.2944-1.3262,2.2969-1.3262.7656,0,1.3511.2471,1.7568.7417s.6084,1.209.6084,2.1431v4.2793Z" fill="#2f2f2f"/>
+      <path d="M458.8225,73.9273c-1.0347,0-1.8604-.3271-2.478-.981s-.9263-1.521-.9263-2.6011c0-1.1758.3213-2.0942.9639-2.7549s1.5107-.9912,2.6045-.9912c1.0435,0,1.8584.3213,2.4438.9639s.8784,1.5337.8784,2.6729c0,1.1167-.3154,2.0107-.9468,2.6831s-1.4775,1.0083-2.5396,1.0083ZM458.9045,67.5426c-.7202,0-1.2896.2451-1.709.7349s-.6289,1.1655-.6289,2.0269c0,.8296.2119,1.4834.6357,1.9619s.9912.7178,1.7021.7178c.7246,0,1.2817-.2349,1.6714-.7041s.5845-1.1372.5845-2.0029c0-.875-.1948-1.5493-.5845-2.0234s-.9468-.7109-1.6714-.7109Z" fill="#2f2f2f"/>
+      <path d="M472.781,66.7633l-2.0986,7h-1.1621l-1.4424-5.0107c-.0547-.1914-.0913-.4077-.1094-.6494h-.0273c-.0137.1641-.0615.376-.1436.6357l-1.5654,5.0244h-1.1211l-2.1191-7h1.1758l1.4492,5.2637c.0454.1597.0776.3691.0957.6289h.0547c.0137-.2007.0547-.4146.123-.6426l1.6133-5.25h1.0254l1.4492,5.2773c.0454.1685.0796.3784.1025.6289h.0547c.0093-.1777.0479-.3872.1162-.6289l1.4219-5.2773h1.1074Z" fill="#2f2f2f"/>
+      <path d="M475.1838,73.7633h-1.1211v-10.3633h1.1211v10.3633Z" fill="#2f2f2f"/>
+      <path d="M483.0222,70.5436h-4.9424c.0181.7793.228,1.3809.6289,1.8047s.9526.6357,1.6543.6357c.7886,0,1.5132-.2598,2.1738-.7793v1.0527c-.6152.4468-1.4287.6699-2.4404.6699-.9888,0-1.7661-.3179-2.3311-.9536s-.8477-1.5303-.8477-2.6831c0-1.0894.3086-1.9766.9263-2.6626s1.3843-1.0288,2.3003-1.0288,1.6245.2964,2.126.8887.752,1.415.752,2.4678v.5879ZM481.8737,69.5934c-.0044-.647-.1606-1.1509-.4683-1.5107s-.7349-.54-1.2817-.54c-.5288,0-.9775.189-1.3467.5674s-.5972.8726-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+      <path d="M490.7536,73.7633h-1.1211v-1.1895h-.0273c-.5195.9023-1.3218,1.3535-2.4062,1.3535-.8794,0-1.5825-.3135-2.1089-.9399s-.7896-1.48-.7896-2.5601c0-1.1577.2915-2.085.875-2.7822s1.3604-1.0459,2.3311-1.0459c.9614,0,1.6611.3784,2.0986,1.1348h.0273v-4.334h1.1211v10.3633ZM489.6325,70.5982v-1.0322c0-.5649-.187-1.0435-.5605-1.4355s-.8477-.5879-1.4219-.5879c-.6836,0-1.2212.2505-1.6133.752s-.5879,1.1938-.5879,2.0781c0,.8066.188,1.4434.564,1.9106s.8809.7007,1.5142.7007c.6245,0,1.1313-.2256,1.521-.6768s.5845-1.021.5845-1.709Z" fill="#2f2f2f"/>
+      <path d="M498.9235,73.2027c0,2.5703-1.2305,3.8555-3.6914,3.8555-.8657,0-1.6226-.1641-2.2695-.4922v-1.1211c.7886.4375,1.5405.6562,2.2559.6562,1.7227,0,2.584-.916,2.584-2.748v-.7656h-.0273c-.5332.8931-1.3354,1.3398-2.4062,1.3398-.8706,0-1.5713-.311-2.1021-.9331s-.7964-1.457-.7964-2.5054c0-1.1895.2861-2.1353.8579-2.8369s1.3545-1.0527,2.3481-1.0527c.9434,0,1.6431.3784,2.0986,1.1348h.0273v-.9707h1.1211v6.4395ZM497.8024,70.5982v-1.0322c0-.5562-.188-1.0322-.564-1.4287s-.8442-.5947-1.4048-.5947c-.6929,0-1.2349.252-1.627.7554s-.5879,1.209-.5879,2.1157c0,.7793.188,1.4023.564,1.8696s.874.7007,1.4937.7007c.6289,0,1.1406-.2231,1.5347-.6699s.5913-1.0186.5913-1.7158Z" fill="#2f2f2f"/>
+      <path d="M506.7448,70.5436h-4.9424c.0181.7793.228,1.3809.6289,1.8047s.9526.6357,1.6543.6357c.7886,0,1.5132-.2598,2.1738-.7793v1.0527c-.6152.4468-1.4287.6699-2.4404.6699-.9888,0-1.7661-.3179-2.3311-.9536s-.8477-1.5303-.8477-2.6831c0-1.0894.3086-1.9766.9263-2.6626s1.3843-1.0288,2.3003-1.0288,1.6245.2964,2.126.8887.752,1.415.752,2.4678v.5879ZM505.5964,69.5934c-.0044-.647-.1606-1.1509-.4683-1.5107s-.7349-.54-1.2817-.54c-.5288,0-.9775.189-1.3467.5674s-.5972.8726-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+      <path d="M461.5852,90.5631h-1.1211v-1.0938h-.0273c-.4878.8384-1.2056,1.2578-2.1533,1.2578-.6973,0-1.2432-.1846-1.6372-.5537s-.5913-.8589-.5913-1.4697c0-1.3081.77-2.0688,2.3105-2.2832l2.0986-.2939c0-1.1895-.481-1.7842-1.4424-1.7842-.8433,0-1.604.2871-2.2832.8613v-1.1484c.688-.4375,1.481-.6562,2.3789-.6562,1.645,0,2.4678.8706,2.4678,2.6113v4.5527ZM460.4641,87.0221l-1.6885.2324c-.5195.0728-.9116.2017-1.1758.3862s-.3965.5117-.3965.981c0,.3418.1221.6211.3657.8374s.5684.3247.9741.3247c.5562,0,1.0151-.1948,1.3774-.5845s.5435-.8828.5435-1.48v-.6973Z" fill="#2f2f2f"/>
+      <path d="M469.654,90.0025c0,2.5703-1.2305,3.8555-3.6914,3.8555-.8657,0-1.6226-.1641-2.2695-.4922v-1.1211c.7886.4375,1.5405.6562,2.2559.6562,1.7227,0,2.584-.916,2.584-2.748v-.7656h-.0273c-.5332.8931-1.3354,1.3398-2.4062,1.3398-.8706,0-1.5713-.311-2.1021-.9331s-.7964-1.457-.7964-2.5054c0-1.1895.2861-2.1353.8579-2.8369s1.3545-1.0527,2.3481-1.0527c.9434,0,1.6431.3784,2.0986,1.1348h.0273v-.9707h1.1211v6.4395ZM468.5329,87.398v-1.0322c0-.5562-.188-1.0322-.564-1.4287s-.8442-.5947-1.4048-.5947c-.6929,0-1.2349.252-1.627.7554s-.5879,1.209-.5879,2.1157c0,.7793.188,1.4023.564,1.8696s.874.7007,1.4937.7007c.6289,0,1.1406-.2231,1.5347-.6699s.5913-1.0186.5913-1.7158Z" fill="#2f2f2f"/>
+      <path d="M477.4753,87.3434h-4.9424c.0181.7793.228,1.3809.6289,1.8047s.9526.6357,1.6543.6357c.7886,0,1.5132-.2598,2.1738-.7793v1.0527c-.6152.4468-1.4287.6699-2.4404.6699-.9888,0-1.7661-.3179-2.3311-.9536s-.8477-1.5303-.8477-2.6831c0-1.0894.3086-1.9766.9263-2.6626s1.3843-1.0288,2.3003-1.0288,1.6245.2964,2.126.8887.752,1.415.752,2.4678v.5879ZM476.3269,86.3932c-.0044-.647-.1606-1.1509-.4683-1.5107s-.7349-.54-1.2817-.54c-.5288,0-.9775.189-1.3467.5674s-.5972.8726-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+      <path d="M484.9685,90.5631h-1.1211v-3.9922c0-1.4858-.5425-2.2285-1.627-2.2285-.5605,0-1.0244.2109-1.3911.6323s-.5503.9536-.5503,1.5962v3.9922h-1.1211v-7h1.1211v1.1621h.0273c.5288-.8843,1.2944-1.3262,2.2969-1.3262.7656,0,1.3511.2471,1.7568.7417s.6084,1.209.6084,2.1431v4.2793Z" fill="#2f2f2f"/>
+      <path d="M490.1975,90.4947c-.2642.146-.6128.2188-1.0459.2188-1.2261,0-1.8389-.6836-1.8389-2.0508v-4.1426h-1.2031v-.957h1.2031v-1.709l1.1211-.3623v2.0713h1.7637v.957h-1.7637v3.9443c0,.4692.0796.8042.2393,1.0049s.4238.3008.793.3008c.2827,0,.5264-.0776.7314-.2324v.957Z" fill="#2f2f2f"/>
+    </g>
+    <g>
+      <path d="M640.7277,76.7633h-1.5996l-3.7871-4.4844c-.1406-.168-.2275-.2822-.2598-.3418h-.0273v4.8262h-1.1484v-9.8027h1.1484v4.6074h.0273c.0645-.0996.1504-.2119.2598-.335l3.6641-4.2725h1.4287l-4.2041,4.7031,4.498,5.0996Z" fill="#2f2f2f"/>
+      <path d="M647.7453,76.7633h-1.1211v-3.9922c0-1.4854-.542-2.2285-1.627-2.2285-.5605,0-1.0244.2109-1.3906.6328-.3672.4209-.5508.9531-.5508,1.5957v3.9922h-1.1211v-7h1.1211v1.1621h.0273c.5293-.8838,1.2949-1.3262,2.2969-1.3262.7656,0,1.3516.2471,1.7568.7422.4062.4941.6084,1.209.6084,2.1426v4.2793Z" fill="#2f2f2f"/>
+      <path d="M652.7492,76.9273c-1.0352,0-1.8604-.3271-2.4785-.9805-.6172-.6543-.9258-1.5215-.9258-2.6016,0-1.1758.3213-2.0938.9639-2.7549.6426-.6602,1.5107-.9912,2.6045-.9912,1.043,0,1.8584.3213,2.4434.9639.5859.6426.8789,1.5342.8789,2.6729,0,1.1172-.3154,2.0107-.9473,2.6836-.6309.6719-1.4775,1.0078-2.5391,1.0078ZM652.8313,70.5426c-.7207,0-1.29.2451-1.709.7354-.4199.4893-.6289,1.165-.6289,2.0264,0,.8301.2119,1.4834.6357,1.9619s.9912.7178,1.7021.7178c.7246,0,1.2812-.2344,1.6709-.7041.3896-.4688.585-1.1367.585-2.0029,0-.875-.1953-1.5488-.585-2.0234-.3896-.4736-.9463-.7109-1.6709-.7109Z" fill="#2f2f2f"/>
+      <path d="M666.7072,69.7633l-2.0986,7h-1.1621l-1.4424-5.0107c-.0547-.1914-.0908-.4072-.1094-.6494h-.0273c-.0137.1641-.0615.376-.1436.6357l-1.5654,5.0244h-1.1211l-2.1191-7h1.1758l1.4492,5.2637c.0459.1602.0781.3691.0957.6289h.0547c.0137-.2002.0547-.4141.123-.6426l1.6133-5.25h1.0254l1.4492,5.2773c.0459.1689.0801.3789.1025.6289h.0547c.0098-.1777.0479-.3867.1162-.6289l1.4219-5.2773h1.1074Z" fill="#2f2f2f"/>
+      <path d="M669.1105,76.7633h-1.1211v-10.3633h1.1211v10.3633Z" fill="#2f2f2f"/>
+      <path d="M676.9484,73.5436h-4.9424c.0186.7793.2285,1.3809.6289,1.8047.4014.4238.9531.6357,1.6543.6357.7891,0,1.5137-.2598,2.1738-.7793v1.0527c-.6152.4473-1.4287.6699-2.4404.6699-.9883,0-1.7656-.3174-2.3311-.9531-.5645-.6357-.8477-1.5303-.8477-2.6836,0-1.0889.3086-1.9766.9268-2.6621.6172-.6865,1.3838-1.0293,2.2998-1.0293s1.625.2969,2.126.8887c.502.5928.752,1.415.752,2.4678v.5879ZM675.8,72.5934c-.0039-.6465-.1602-1.1504-.4678-1.5107-.3076-.3594-.7354-.54-1.2822-.54-.5283,0-.9775.1895-1.3467.5674-.3691.3789-.5967.873-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+      <path d="M684.6799,76.7633h-1.1211v-1.1895h-.0273c-.5195.9023-1.3213,1.3535-2.4062,1.3535-.8789,0-1.582-.3135-2.1084-.9395-.5264-.627-.79-1.4805-.79-2.5605,0-1.1572.292-2.085.875-2.7822.584-.6973,1.3604-1.0459,2.3311-1.0459.9619,0,1.6611.3789,2.0986,1.1348h.0273v-4.334h1.1211v10.3633ZM683.5588,73.5982v-1.0322c0-.5645-.1865-1.043-.5605-1.4355-.373-.3916-.8477-.5879-1.4219-.5879-.6836,0-1.2207.251-1.6133.752-.3916.502-.5879,1.1943-.5879,2.0781,0,.8066.1885,1.4434.5645,1.9111.376.4668.8809.7002,1.5137.7002.625,0,1.1318-.2256,1.5215-.6768s.584-1.0205.584-1.709Z" fill="#2f2f2f"/>
+      <path d="M692.8498,76.2027c0,2.5703-1.2305,3.8555-3.6914,3.8555-.8652,0-1.6221-.1641-2.2695-.4922v-1.1211c.7891.4375,1.541.6562,2.2559.6562,1.7227,0,2.584-.916,2.584-2.748v-.7656h-.0273c-.5332.8936-1.335,1.3398-2.4062,1.3398-.8701,0-1.5713-.3105-2.1016-.9326-.5312-.6221-.7969-1.457-.7969-2.5059,0-1.1895.2861-2.1348.8584-2.8369.5713-.7012,1.3545-1.0527,2.3477-1.0527.9434,0,1.6436.3789,2.0986,1.1348h.0273v-.9707h1.1211v6.4395ZM691.7287,73.5982v-1.0322c0-.5557-.1875-1.0322-.5635-1.4287s-.8447-.5947-1.4053-.5947c-.6924,0-1.2344.252-1.627.7559-.3916.5029-.5879,1.209-.5879,2.1152,0,.7793.1885,1.4023.5645,1.8701.376.4668.874.7002,1.4932.7002.6289,0,1.1406-.2227,1.5352-.6699.3936-.4463.5908-1.0186.5908-1.7158Z" fill="#2f2f2f"/>
+      <path d="M700.6711,73.5436h-4.9424c.0186.7793.2285,1.3809.6289,1.8047.4014.4238.9531.6357,1.6543.6357.7891,0,1.5137-.2598,2.1738-.7793v1.0527c-.6152.4473-1.4287.6699-2.4404.6699-.9883,0-1.7656-.3174-2.3311-.9531-.5645-.6357-.8477-1.5303-.8477-2.6836,0-1.0889.3086-1.9766.9268-2.6621.6172-.6865,1.3838-1.0293,2.2998-1.0293s1.625.2969,2.126.8887c.502.5928.752,1.415.752,2.4678v.5879ZM699.5227,72.5934c-.0039-.6465-.1602-1.1504-.4678-1.5107-.3076-.3594-.7354-.54-1.2822-.54-.5283,0-.9775.1895-1.3467.5674-.3691.3789-.5967.873-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+      <path d="M705.7775,76.5104v-1.2031c.6113.4512,1.2832.6768,2.0166.6768.9844,0,1.4766-.3281,1.4766-.9844,0-.1865-.042-.3447-.126-.4746-.085-.1299-.1982-.2451-.3418-.3457-.1436-.0996-.3125-.1904-.5059-.2695-.1943-.0801-.4023-.1631-.626-.25-.3096-.123-.582-.2471-.8164-.3721-.2354-.126-.4307-.2666-.5879-.4238s-.2764-.3359-.3555-.5371c-.0801-.2002-.1201-.4346-.1201-.7041,0-.3281.0752-.6182.2256-.8711s.3516-.4648.6016-.6357c.251-.1709.5371-.2998.8584-.3867.3213-.0859.6523-.1299.9941-.1299.6064,0,1.1484.1055,1.627.3145v1.1348c-.5146-.3369-1.1074-.5059-1.7773-.5059-.209,0-.3984.0244-.5674.0723-.168.0479-.3135.1152-.4336.2012-.1211.0869-.2148.1904-.2803.3115-.0664.1201-.0996.2539-.0996.3994,0,.1826.0332.335.0996.458.0654.123.1631.2324.29.3281.1279.0957.2832.1826.4648.2598.1826.0781.3896.1621.6221.2529.3105.1191.5879.2402.834.3662.2461.125.4561.2666.6289.4238.1738.1572.3066.3379.4004.543.0928.2051.1396.4492.1396.7314,0,.3467-.0762.6475-.2285.9023-.1533.2559-.3564.4678-.6123.6357-.2549.1689-.5488.2939-.8818.376-.332.082-.6807.123-1.0459.123-.7197,0-1.3438-.1387-1.873-.417Z" fill="#2f2f2f"/>
+      <path d="M715.0324,76.9273c-1.0342,0-1.8604-.3271-2.4775-.9805-.6182-.6543-.9268-1.5215-.9268-2.6016,0-1.1758.3213-2.0938.9639-2.7549.6426-.6602,1.5107-.9912,2.6045-.9912,1.0439,0,1.8584.3213,2.4443.9639.585.6426.8779,1.5342.8779,2.6729,0,1.1172-.3154,2.0107-.9463,2.6836-.6318.6719-1.4775,1.0078-2.54,1.0078ZM715.1145,70.5426c-.7197,0-1.2891.2451-1.709.7354-.4189.4893-.6289,1.165-.6289,2.0264,0,.8301.2119,1.4834.6357,1.9619s.9912.7178,1.7021.7178c.7246,0,1.2822-.2344,1.6719-.7041.3896-.4688.584-1.1367.584-2.0029,0-.875-.1943-1.5488-.584-2.0234-.3896-.4736-.9473-.7109-1.6719-.7109Z" fill="#2f2f2f"/>
+      <path d="M725.9279,76.7633h-1.1211v-1.1074h-.0273c-.4648.8477-1.1846,1.2715-2.1602,1.2715-1.668,0-2.502-.9932-2.502-2.9805v-4.1836h1.1143v4.0059c0,1.4766.5654,2.2148,1.6953,2.2148.5469,0,.9971-.2012,1.3506-.6045.3525-.4033.5293-.9307.5293-1.583v-4.0332h1.1211v7Z" fill="#2f2f2f"/>
+      <path d="M731.6857,70.898c-.1953-.1504-.4785-.2256-.8477-.2256-.4785,0-.8779.2256-1.1992.6768s-.4824,1.0664-.4824,1.8457v3.5684h-1.1211v-7h1.1211v1.4424h.0273c.1602-.4922.4033-.876.7314-1.1514.3281-.2764.6953-.4141,1.1006-.4141.292,0,.5156.0322.6699.0957v1.1621Z" fill="#2f2f2f"/>
+      <path d="M737.6438,76.442c-.5381.3242-1.1758.4854-1.9141.4854-.998,0-1.8037-.3242-2.417-.9736-.6123-.6494-.9189-1.4912-.9189-2.5264,0-1.1523.3301-2.0791.9912-2.7783.6602-.7002,1.542-1.0498,2.6455-1.0498.6152,0,1.1572.1143,1.627.3418v1.1484c-.5195-.3643-1.0762-.5469-1.668-.5469-.7158,0-1.3027.2568-1.7607.7695s-.6865,1.1855-.6865,2.0195c0,.8203.2148,1.4678.6455,1.9414.4307.4746,1.0088.7109,1.7334.7109.6104,0,1.1846-.2021,1.7227-.6084v1.0664Z" fill="#2f2f2f"/>
+      <path d="M744.8137,73.5436h-4.9424c.0176.7793.2275,1.3809.6289,1.8047.4004.4238.9521.6357,1.6543.6357.7881,0,1.5127-.2598,2.1738-.7793v1.0527c-.6152.4473-1.4287.6699-2.4404.6699-.9893,0-1.7666-.3174-2.3311-.9531-.5654-.6357-.8477-1.5303-.8477-2.6836,0-1.0889.3086-1.9766.9258-2.6621.6182-.6865,1.3848-1.0293,2.3008-1.0293s1.624.2969,2.126.8887c.501.5928.752,1.415.752,2.4678v.5879ZM743.6652,72.5934c-.0049-.6465-.1611-1.1504-.4688-1.5107-.3076-.3594-.7344-.54-1.2812-.54-.5293,0-.9775.1895-1.3467.5674-.3691.3789-.5977.873-.6836,1.4834h3.7803Z" fill="#2f2f2f"/>
+    </g>
+  </g>
+</svg>
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "エージェントからエージェントへのパイプラインのSVG画像の追加"
}
```

### Explanation
この変更は、新しいSVG画像ファイルである`agent-to-agent-pipeline.svg`がリポジトリに追加されたことを示しています。この画像は、エージェントからエージェントへのパイプラインに関する内容を視覚的に表現していると考えられます。具体的な変更点は以下の通りです。

1. **新規ファイルの追加**: 279行のSVGコンテンツが新たに追加されました。これにより、ダイアグラムやビジュアルコンテンツを通じて、エージェント間の通信やデータの流れを視覚的に理解できるようになります。

このSVGファイルは、ドキュメントの理解を助け、読者に対して視覚的に分かりやすい説明を提供するための重要なリソースとなります。これにより、より良いユーザー体験の向上が期待されます。

## articles/search/samples-dotnet.md{#item-12f3fa}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - devx-track-dotnet
   - ignite-2023
 ms.topic: concept-article
-ms.date: 09/19/2025
+ms.date: 09/23/2025
 ---
 
 # C# samples for Azure AI Search
@@ -43,25 +43,23 @@ Code samples from the Azure SDK development team demonstrate API usage. You can
 
 ## Doc samples
 
-Code samples from the Azure AI Search team demonstrate features and workflows. Many of the following samples are referenced in tutorials, quickstarts, and how-to articles that explain the code in detail. You can find these samples in [Azure-Samples/azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples) and [Azure-Samples/search-dotnet-getting-started](https://github.com/Azure-Samples/search-dotnet-getting-started/) on GitHub.
-
-| Sample | Description |
-|--|--|
-| [quickstart](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/AzureSearchQuickstart) | Source code for the C# portion of [Quickstart: Full-text search](search-get-started-text.md). Create, load, and query an index using sample data. |
-| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) | Source code for the C# portion of [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md). Integrate semantic ranking with LLM-powered query planning and answer generation. |
-| [quickstart-rag](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-rag) | Source code for the C# portion of [Quickstart: Generative search (RAG)](search-get-started-rag.md). Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
-| [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | Source code for the C# portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). Add semantic ranking to an index schema and run semantic queries. |
-| [quickstart-vector-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-vector-search) | Source code for the C# portion of [Quickstart: Vector search](search-get-started-vector.md). Index and query vector content. |
-| [create-mvc-app](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/create-mvc-app) | Source code for [Tutorial: Add search to an ASP.NET Core (MVC) app](tutorial-csharp-create-mvc-app.md). Add basic search, pagination, and other server-side behaviors to an MVC web app, unlike the console applications used in most samples. |
-| [search-website](https://github.com/Azure-Samples/azure-search-static-web-app) | Source code for [Tutorial: Add search to web apps](tutorial-csharp-overview.md). Build an end-to-end search app that uses the push API for bulk upload and a rich client for hosting the app and handling search requests. |
-| [tutorial-ai-enrichment](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/tutorial-ai-enrichment) | Source code for [Tutorial: AI-generated searchable content from Azure blobs](tutorial-skillset.md). Create a skillset that iterates over Azure blobs to extract information and infer structure. |
-| [multiple-data-sources](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources) | Source code for [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md). Merge content from two data sources into one index. |
-| [optimize-data-indexing](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/optimize-data-indexing) | Source code for [Tutorial: Optimize indexing with the push API](tutorial-optimize-indexing-push-api.md). Use optimization techniques for pushing data into an index. |
-| [DotNetHowTo](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowTo) | Source code for [Use the .NET client library](search-howto-dotnet-sdk.md). Create and manage multiple search objects while learning about the APIs. |
-| [DotNetToIndexers](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToIndexers) | Source code for [Tutorial: Index Azure SQL data](search-indexer-tutorial.md). Configure an Azure SQL indexer with a schedule, field mappings, and parameters. |
-| [DotNetHowToEncryptionUsingCMK](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToEncryptionUsingCMK) | Source code for [Configure customer-managed keys for data encryption](search-security-manage-encryption-keys.md). Create objects that are encrypted with a customer-managed key. |
-| [DotNetVectorDemo](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetVectorDemo) | Create, load, and query a vector index. |
-| [DotNetIntegratedVectorizationDemo](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetIntegratedVectorizationDemo) | Extend the vector workflow to include skills-based automation for data chunking and embedding. |
+Code samples from the Azure AI Search team demonstrate features and workflows. The following samples are referenced in tutorials, quickstarts, and how-to articles that explain the code in detail. You can find these samples in [Azure-Samples/azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples) and [Azure-Samples/search-dotnet-getting-started](https://github.com/Azure-Samples/search-dotnet-getting-started/) on GitHub.
+
+| Sample | Article | Description |
+|--|--|--|
+| [quickstart](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/AzureSearchQuickstart) | [Quickstart: Full-text search](search-get-started-text.md) | Create, load, and query an index using sample data. |
+| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) | [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md) | Integrate semantic ranking with LLM-powered query planning and answer generation. |
+| [quickstart-rag](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-rag) | [Quickstart: Generative search (RAG)](search-get-started-rag.md) | Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
+| [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
+| [quickstart-vector-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-vector-search) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
+| [create-mvc-app](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/create-mvc-app) | [Tutorial: Add search to an ASP.NET Core (MVC) app](tutorial-csharp-create-mvc-app.md) | Add basic search, pagination, and other server-side behaviors to an MVC web app, unlike the console applications used in most samples. |
+| [search-website](https://github.com/Azure-Samples/azure-search-static-web-app) | [Tutorial: Add search to web apps](tutorial-csharp-overview.md) | Build an end-to-end search app that uses the push API for bulk upload and a rich client for hosting the app and handling search requests. |
+| [tutorial-ai-enrichment](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/tutorial-ai-enrichment) | [Tutorial: AI-generated searchable content from Azure blobs](tutorial-skillset.md) | Create a skillset that iterates over Azure blobs to extract information and infer structure. |
+| [multiple-data-sources](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources) | [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md) | Merge content from two data sources into one index. |
+| [optimize-data-indexing](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/optimize-data-indexing) | [Tutorial: Optimize indexing with the push API](tutorial-optimize-indexing-push-api.md) | Use optimization techniques for pushing data into an index. |
+| [DotNetHowTo](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowTo) | [Use the .NET client library](search-howto-dotnet-sdk.md) | Create and manage multiple search objects while learning about the APIs. |
+| [DotNetToIndexers](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToIndexers) | [Tutorial: Index Azure SQL data](search-indexer-tutorial.md) | Configure an Azure SQL indexer with a schedule, field mappings, and parameters. |
+| [DotNetHowToEncryptionUsingCMK](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToEncryptionUsingCMK) | [Configure customer-managed keys for data encryption](search-security-manage-encryption-keys.md) | Create objects that are encrypted with a customer-managed key. |
 
 ## Accelerators
 
@@ -93,6 +91,8 @@ The following samples are also published by the Azure AI Search team but aren't
 | [multiple-search-services](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-search-services) | Query multiple search services and combine results into a single page. |
 | [search-aggregations](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/search-aggregations) | Obtain and filter aggregations from an index. |
 | [azure-search-power-skills](https://github.com/Azure-Samples/azure-search-power-skills/blob/main) | Incorporate consumable custom skills into your own solutions. |
+| [DotNetVectorDemo](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetVectorDemo) | Create, load, and query a vector index. |
+| [DotNetIntegratedVectorizationDemo](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetIntegratedVectorizationDemo) | Extend the vector workflow to include skills-based automation for data chunking and embedding. |
 
 > [!TIP]
 > Use the [samples browser](/samples/browse/?languages=csharp&products=azure-cognitive-search) to search for Microsoft code samples on GitHub. You can filter your search by product, service, and language.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#サンプルドキュメントの更新"
}
```

### Explanation
この変更は、`samples-dotnet.md`というC#サンプルに関するドキュメントに対して行われたマイナーな更新を示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの最終更新日が`09/19/2025`から`09/23/2025`に変更されました。

2. **コンテンツの調整**: コードサンプルの説明が整理され、いくつかのサンプルが表形式で新たに整理されました。具体的には、サンプル名、関連する記事、およびその説明が表にまとめられました。これにより、ユーザーがサンプルの使い方やその目的をより簡単に理解できるようになっています。

3. **新しいサンプルの追加**: 新しく以下のサンプルが追加されました。
   - [DotNetVectorDemo](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetVectorDemo): ベクターインデックスの作成、ロード、クエリ。
   - [DotNetIntegratedVectorizationDemo](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-dotnet/DotNetIntegratedVectorizationDemo): データチャンク化と埋め込みのためのスキルベースの自動化を含むワークフローを拡張。

この変更により、ドキュメントはより最新の情報に更新され、利用者がサンプルを通じて機能やワークフローを学びやすくなることが期待されます。

## articles/search/samples-java.md{#item-5992fd}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.custom:
   - devx-track-extended-java
   - ignite-2023
 ms.topic: concept-article
-ms.date: 09/19/2025
+ms.date: 09/23/2025
 ---
 
 # Java samples for Azure AI Search
@@ -44,11 +44,11 @@ Code samples from the Azure SDK development team demonstrate API usage. You can
 
 ## Doc samples
 
-Code samples from the Azure AI Search team demonstrate features and workflows. Many of the following samples are referenced in tutorials, quickstarts, and how-to articles that explain the code in detail. You can find these samples in [Azure-Samples/azure-search-java-samples](https://github.com/Azure-Samples/azure-search-java-samples) on GitHub.
+Code samples from the Azure AI Search team demonstrate features and workflows. The following samples are referenced in tutorials, quickstarts, and how-to articles that explain the code in detail. You can find these samples in [Azure-Samples/azure-search-java-samples](https://github.com/Azure-Samples/azure-search-java-samples) on GitHub.
 
-| Sample | Article |
-|--|--|
-| [quickstart](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart) | Source code for the Java portion of [Quickstart: Full-text search](search-get-started-text.md). Create, load, and query an index using sample data. |
+| Sample | Article | Description |
+|--|--|--|
+| [quickstart](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart) | [Quickstart: Full-text search](search-get-started-text.md) | Create, load, and query an index using sample data. |
 
 > [!TIP]
 > Use the [samples browser](/samples/browse/?languages=java&products=azure-cognitive-search) to search for Microsoft code samples on GitHub. You can filter your search by product, service, and language.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaサンプルドキュメントの更新"
}
```

### Explanation
この変更は、`samples-java.md`というJavaに関するサンプルドキュメントに対して行われた軽微な更新を示しています。具体的な変更内容は次の通りです。

1. **日付の更新**: ドキュメントの最終更新日が`09/19/2025`から`09/23/2025`に変更されました。これにより、最新の情報であることが示されます。

2. **コンテンツの調整**: サンプル紹介の部分で、表の形式が変更されました。以前は「サンプル」と「記事」という2つの列がありましたが、これを「サンプル」、「記事」、および「説明」の3つの列を持つ新しい表に更新しました。これにより、各サンプルの内容や目的を特に分かりやすく示すことができるようになっています。

3. **サンプルのリンクと説明**: リンクはそのままですが、サンプルごとの説明が加えられ、どのような機能が実装されているかが明確に示されるようになりました。

この変更により、ドキュメントがより利用者フレンドリーになり、特に新しいユーザーがサンプルの使用方法を理解しやすくなったと期待されます。

## articles/search/samples-javascript.md{#item-82e67e}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - devx-track-js
   - ignite-2023
 ms.topic: concept-article
-ms.date: 09/19/2025
+ms.date: 09/23/2025
 ---
 
 # JavaScript samples for Azure AI Search
@@ -35,7 +35,7 @@ Code samples from the Azure SDK development team demonstrate API usage. You can
 | Sample | Description |
 |--|--|
 | [indexes](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Create, update, get, list, and delete [indexes](search-what-is-an-index.md). This sample category also includes a service statistic sample. |
-| [indexers](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Create, update, get, list, reset, and delete [indexers](search-indexer-overview.md).|
+| [indexers](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Create, update, get, list, reset, and delete [indexers](search-indexer-overview.md). |
 | [dataSourceConnections (for indexers)](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/javascript/dataSourceConnectionOperations.js) | Create, update, get, list, and delete data source connections, which are required for indexer-based indexing of [supported data sources](search-indexer-overview.md#supported-data-sources). |
 | [skillsets](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Create, update, get, list, and delete [skillsets](cognitive-search-working-with-skillsets.md) that are attached to indexers and perform AI-based enrichment during indexing. |
 | [synonymMaps](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) | Create, update, get, list, and delete [synonym maps](search-synonyms.md). |
@@ -46,42 +46,42 @@ Code samples from the Azure SDK development team demonstrate API usage. You can
 | Sample | Description |
 |--|--|
 | [indexes](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/typescript/src) | Create, update, get, list, and delete [indexes](search-what-is-an-index.md). This sample category also includes a service statistic sample. |
-| [indexers](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/typescript/src) | Create, update, get, list, reset, and delete [indexers](search-indexer-overview.md).|
+| [indexers](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/typescript/src) | Create, update, get, list, reset, and delete [indexers](search-indexer-overview.md). |
 | [dataSourceConnections (for indexers)](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/dataSourceConnectionOperations.ts) | Create, update, get, list, and delete data source connections, which are required for indexer-based indexing of [supported data sources](search-indexer-overview.md#supported-data-sources). |
 | [skillsets](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/skillSetOperations.ts) | Create, update, get, list, and delete [skillsets](cognitive-search-working-with-skillsets.md) that are attached to indexers and perform AI-based enrichment during indexing. |
 | [synonymMaps](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/typescript/src/synonymMapOperations.ts) | Create, update, get, list, and delete [synonym maps](search-synonyms.md). |
 | [vectorSearch](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v12/typescript/src/vectorSearch.ts) | Create, update, get, list, and delete [vector search](vector-search-how-to-query.md). |
 
 ## Doc samples
 
-Code samples from the Azure AI Search team demonstrate features and workflows. Many of the following samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [Azure-Samples/azure-search-javascript-samples](https://github.com/Azure-Samples/azure-search-javascript-samples) on GitHub.
+Code samples from the Azure AI Search team demonstrate features and workflows. The following samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [Azure-Samples/azure-search-javascript-samples](https://github.com/Azure-Samples/azure-search-javascript-samples) on GitHub.
 
 ### JavaScript samples
 
-| Sample | Description |
-|--|--|
-| [quickstart](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) | Source code for the JavaScript portion of [Quickstart: Full-text search](search-get-started-text.md). Create, load, and query a search index using sample data. |
-| [quickstart-rag-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-rag-js) | Source code for the JavaScript portion of [Quickstart: Generative search (RAG)](search-get-started-rag.md). Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
-| [quickstart-semantic-ranking-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-js) | Source code for the JavaScript portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). Add semantic ranking to an index schema and run semantic queries. |
-| [quickstart-vector-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-vector-js) | Source code for the JavaScript portion of [Quickstart: Vector search](search-get-started-vector.md). Index and query vector content. |
-| [azure-functions](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/azure-function-search) | JavaScript example of an Azure function that sends queries to a search service. You can substitute this JavaScript version for the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
-| [bulk-insert](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/bulk-insert) | JavaScript example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
+| Sample | Article | Description |
+|--|--|--|
+| [quickstart](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) | [Quickstart: Full-text search](search-get-started-text.md) | Create, load, and query a search index using sample data. |
+| [quickstart-rag-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-rag-js) | [Quickstart: Generative search (RAG)](search-get-started-rag.md) | Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
+| [quickstart-semantic-ranking-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-js) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
+| [quickstart-vector-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-vector-js) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
 
 ### TypeScript samples
 
-| Sample | Description |
-|--|--|
-| [quickstart-rag-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-rag-ts) | Source code for the TypeScript portion of [Quickstart: Generative search (RAG)](search-get-started-rag.md). Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
-| [quickstart-semantic-ranking-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-ts) | Source code for the TypeScript portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). Add semantic ranking to an index schema and run semantic queries. |
-| [quickstart-vector-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-vector-ts) | Source code for the TypeScript portion of [Quickstart: Vector search](search-get-started-vector.md). Index and query vector content. |
+| Sample | Article | Description |
+|--|--|--|
+| [quickstart-rag-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-rag-ts) | [Quickstart: Generative search (RAG)](search-get-started-rag.md) | Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
+| [quickstart-semantic-ranking-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-ts) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
+| [quickstart-vector-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-vector-ts) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
 
 ## Other samples
 
 The following samples are also published by the Azure AI Search team but aren't referenced in documentation. Associated README files provide usage instructions.
 
 | Sample | Description |
 |--|--|
-| [azure-search-vector-sample.js](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript/readme.md) | Perform vector search using the Azure SDK for JavaScript. |
+| [azure-search-vector-sample.js](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-javascript/readme.md) | JavaScript example of how to perform vector search. |
+| [azure-function-search](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/azure-function-search) | JavaScript example of an Azure function that sends queries to a search service. You can substitute this JavaScript version for the `api` code used in [Add search to web sites with .NET](tutorial-csharp-overview.md). |
+| [bulk-insert](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/bulk-insert) | JavaScript example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
 
 > [!TIP]
 > Use the [samples browser](/samples/browse/?languages=javascript&products=azure-cognitive-search) to search for Microsoft code samples on GitHub. You can filter your search by product, service, and language.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptサンプルドキュメントの更新"
}
```

### Explanation
この変更は、`samples-javascript.md`というJavaScriptサンプルに関するドキュメントに対して行われた軽微な更新を示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの最終更新日が`09/19/2025`から`09/23/2025`に変更され、情報が最新であることが反映されています。

2. **コンテンツの整理**: サンプルの一覧で、説明が追加され、各サンプルの目的や機能がより明確に示されています。例えば、各サンプルに対して「説明」という列が追加され、どのような操作が行えるかが明記されています。

3. **サンプル名の更新**: いくつかのサンプル名のコンテンツに小さな変更が加えられ、説明のスタイルが統一されました。これにより、利用者が各サンプルの特徴を理解しやすくなるように配慮されています。

4. **新しいサンプルの情報**: Azureの新しい機能やベストプラクティスを反映するために、新しいサンプルやそれに関連するリンクが適切に配置されています。特に、クイックスタート用のサンプルがよりわかりやすく構成されています。

これらの変更により、このドキュメントがより利用者に優しくなり、新しいユーザーでもサンプルを通じて機能を理解しやすくなる効果が期待されます。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: concept-article
-ms.date: 09/19/2025
+ms.date: 09/23/2025
 ---
 
 # Python samples for Azure AI Search
@@ -32,19 +32,17 @@ Code samples from the Azure SDK development team demonstrate API usage. You can
 
 ## Doc samples
 
-Code samples from the Azure AI Search team demonstrate features and workflows. Many of the following samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [Azure-Samples/azure-search-python-samples](https://github.com/Azure-Samples/azure-search-python-samples) on GitHub.
+Code samples from the Azure AI Search team demonstrate features and workflows. The following samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [Azure-Samples/azure-search-python-samples](https://github.com/Azure-Samples/azure-search-python-samples) on GitHub.
 
-| Sample | Description |
-|--|--|
-| [Quickstart](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart) | Source code for the Python portion of [Quickstart: Full-text search](search-get-started-text.md). Create, load, and query a search index using sample data. |
-| [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval) | Source code for the Python portion of [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md). Integrate semantic ranking with LLM-powered query planning and answer generation. |
-| [Quickstart-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-RAG) | Source code for the Python portion of [Quickstart: Generative search (RAG)](search-get-started-rag.md). Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
-| [Quickstart-Semantic-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) | Source code for the Python portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). Add semantic ranking to an index schema and run semantic queries. |
-| [Quickstart-Vector-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Vector-Search) | Source code for the Python portion of [Quickstart: Vector search](search-get-started-vector.md). Index and query vector content. |
-| [Tutorial-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Tutorial-RAG) | Source code for the Python portion of [Build a RAG solution using Azure AI Search](tutorial-rag-build-solution.md).|
-| [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) | Source code for the Python portion of [Build an agent-to-agent retrieval solution using Azure AI Search](search-agentic-retrieval-how-to-pipeline.md). Unlike [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md), this sample incorporates Azure AI Agent for request orchestration. |
-| [azure-function-search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/azure-function-search) | Python example of an Azure function that sends queries to a search service. You can substitute this Python version for the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
-| [bulk-insert](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/bulk-insert) | Python example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
+| Sample | Article | Description |
+|--|--|--|
+| [Quickstart](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart) | [Quickstart: Full-text search](search-get-started-text.md) | Create, load, and query a search index using sample data. |
+| [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval) | [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md) | Integrate semantic ranking with LLM-powered query planning and answer generation. |
+| [Quickstart-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-RAG) | [Quickstart: Generative search (RAG)](search-get-started-rag.md) | Use grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
+| [Quickstart-Semantic-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
+| [Quickstart-Vector-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Vector-Search) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
+| [Tutorial-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Tutorial-RAG) | [Build a RAG solution using Azure AI Search](tutorial-rag-build-solution.md) | Create an indexing pipeline that loads, chunks, embeds, and ingests searchable content for RAG. |
+| [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) | [Build an agent-to-agent retrieval solution using Azure AI Search](search-agentic-retrieval-how-to-pipeline.md) | Unlike [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval), this sample incorporates Azure AI Agent for request orchestration. |
 
 ## Accelerators
 
@@ -70,8 +68,10 @@ The following samples are also published by the Azure AI Search team but aren't
 
 | Sample | Description |
 |--|--|
+| [azure-function-search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/azure-function-search) | Use an Azure function to send queries to a search service. You can substitute this Python version for the `api` code used in [Add search to web sites with .NET](tutorial-csharp-overview.md). |
+| [bulk-insert](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/bulk-insert) | [Use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
 | [index-backup-and-restore.ipynb](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) | Make a local copy of retrievable fields in an index and push those fields to a new index. |
-| [resumable-index-backup-restore](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/resumable-index-backup-restore/backup-and-restore.ipynb) | Back up and restore larger indexes that exceed 100,000 documents.|
+| [resumable-index-backup-restore](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/resumable-index-backup-restore/backup-and-restore.ipynb) | Back up and restore larger indexes that exceed 100,000 documents. |
 
 > [!TIP]
 > Use the [samples browser](/samples/browse/?languages=python&products=azure-cognitive-search) to search for Microsoft code samples on GitHub. You can filter your search by product, service, and language.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonサンプルドキュメントの更新"
}
```

### Explanation
この変更は、`samples-python.md`というPythonに関するサンプルドキュメントに対して行われた軽微な更新を示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの最終更新日が`09/19/2025`から`09/23/2025`に変更され、最新の情報が反映されています。

2. **コンテンツの整理**: サンプルの一覧が整理され、各サンプルに対して「説明」という列が追加されました。これにより、利用者がサンプルの目的や機能を理解しやすくなっています。

3. **サンプルリンクの整備**: 各サンプルのリンクが更新され、説明文が加えられています。たとえば、クイックスタートに関するリンクの下に、それぞれのサンプルが何を実現するためのものかを明記しています。これにより、ユーザーが必要な情報を迅速に見つけることができるようになっています。

4. **追加のサンプルと情報**: 新しいサンプルが追加され、特にRAG（Retrieval-Augmented Generation）を使用したソリューションやエージェント間のリトリーバルソリューション構築に関する例が詳しく説明されています。また、Azure Functionを使用したクエリ送信の例も含まれており、総合的に情報が豊かになっています。

これらの変更により、ドキュメントがより利用者に優しくなり、特に新しいユーザーがサンプルを通じて機能や実装方法を理解しやすくなる効果が期待されます。

## articles/search/samples-rest.md{#item-198ebc}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 09/19/2025
+ms.date: 09/23/2025
 ---
 
 # REST samples for Azure AI Search
@@ -22,27 +22,27 @@ You can use any client that supports HTTP calls. To learn how to formulate the H
 
 ## Doc samples
 
-Code samples from the Azure AI Search team demonstrate features and workflows. Many of the following samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [Azure-Samples/azure-search-rest-samples](https://github.com/Azure-Samples/azure-search-rest-samples) on GitHub.
+Code samples from the Azure AI Search team demonstrate features and workflows. The following samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [Azure-Samples/azure-search-rest-samples](https://github.com/Azure-Samples/azure-search-rest-samples) on GitHub.
 
-| Sample | Description |
-|--|--|
-| [quickstart](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart) | Source code for the REST portion of [Quickstart: Full-text search](search-get-started-text.md). Create, load, and query a search index using sample data. |
-| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-agentic-retrieval) | Source code for the REST portion of [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md). Integrate semantic ranking with LLM-powered query planning and answer generation. |
-| [quickstart-vectors](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) | Source code for the REST portion of [Quickstart: Vector search](search-get-started-vector.md). Index and query vector content. |
-| [skillset-tutorial](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial) | Source code for [Tutorial: AI-generated searchable content from Azure blobs](tutorial-skillset.md). Create a skillset that iterates over Azure blobs to extract information and infer structure.|
-| [debug-sessions](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Debug-sessions) | Source code for [Tutorial: Fix a skillset using Debug Sessions](cognitive-search-tutorial-debug-sessions.md). Use REST to create search objects that you later debug in the Azure portal. |
-| [custom-analyzers](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/custom-analyzers) | Source code for [Tutorial: Create a custom analyzer for phone numbers](tutorial-create-custom-analyzer.md). Use an analyzer to preserve patterns and special characters in searchable content.|
-| [index-json-blobs](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/index-json-blobs) | Source code for [Tutorial: Index JSON blobs from Azure Storage](search-semi-structured-data.md). Create an indexer, data source, and index for nested JSON within a JSON array. Demonstrates the jsonArray parsing model and documentRoot parameters. |
-| [knowledge-store](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/knowledge-store) | Source code for [Create a knowledge store using REST](knowledge-store-create-rest.md). Populate a knowledge store for knowledge mining workflows. |
-| [projections](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/projections) | Source code for [Define projections in a knowledge store](knowledge-store-projections-examples.md). Specify the physical data structures in a knowledge store.|
+| Sample | Article | Description |
+|--|--|--|
+| [quickstart](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart) | [Quickstart: Full-text search](search-get-started-text.md) | Create, load, and query a search index using sample data. |
+| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-agentic-retrieval) | [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md) | Integrate semantic ranking with LLM-powered query planning and answer generation. |
+| [quickstart-vectors](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
+| [skillset-tutorial](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial) | [Tutorial: AI-generated searchable content from Azure blobs](tutorial-skillset.md) | Create a skillset that iterates over Azure blobs to extract information and infer structure. |
+| [debug-sessions](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Debug-sessions) | [Tutorial: Fix a skillset using Debug Sessions](cognitive-search-tutorial-debug-sessions.md) | Use REST to create search objects that you later debug in the Azure portal. |
+| [custom-analyzers](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/custom-analyzers) | [Tutorial: Create a custom analyzer for phone numbers](tutorial-create-custom-analyzer.md) | Use an analyzer to preserve patterns and special characters in searchable content. |
+| [index-json-blobs](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/index-json-blobs) | [Tutorial: Index JSON blobs from Azure Storage](search-semi-structured-data.md) | Create an indexer, data source, and index for nested JSON within a JSON array. Demonstrates the jsonArray parsing model and documentRoot parameters. |
+| [knowledge-store](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/knowledge-store) | [Create a knowledge store using REST](knowledge-store-create-rest.md) | Populate a knowledge store for knowledge mining workflows. |
+| [projections](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/projections) | [Define projections in a knowledge store](knowledge-store-projections-examples.md) | Specify the physical data structures in a knowledge store. |
 
 ## Other samples
 
 The following samples are also published by the Azure AI Search team but aren't referenced in documentation. Associated README files provide usage instructions.
 
 | Sample | Description |
 |--|--|
-| [skill examples](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skill-examples) | Skillset examples in indexer pipelines that include indexes and indexers so you can follow field mappings, output field mappings, and source paths. |
+| [skill-examples](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skill-examples) | Skillset examples in indexer pipelines that include indexes and indexers so you can follow field mappings, output field mappings, and source paths. |
 
 > [!TIP]
 > Use the [samples browser](/samples/browse/?expanded=azure&languages=http&products=azure-cognitive-search) to search for Microsoft code samples on GitHub. You can filter your search by product, service, and language.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIサンプルドキュメントの更新"
}
```

### Explanation
この変更は、`samples-rest.md`というREST APIに関するサンプルドキュメントに対して行われた軽微な更新を示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの最終更新日が`09/19/2025`から`09/23/2025`に変更され、最新情報が反映されています。

2. **コンテンツの整理**: サンプルリストのフォーマットが改良され、各サンプルに対して「説明」という列が追加されました。これにより、利用者がそれぞれのサンプルが何を提供するのかを理解しやすくなっています。

3. **サンプルリンクの整備**: 各サンプルに関連するリンクが更新され、追加の文脈情報が提供されています。リンクテキストがより明確になり、利用者がどのような情報を得られるかを易しく把握できるようになりました。

4. **新しい情報の追加**: 新しいサンプルとそれに関する説明が追加され、特にスキルセットやナレッジストアに関するタスクを扱ったチュートリアルが強調されています。これにより、このドキュメントが提供する情報がさらに豊かになり、ユーザーがより多くの機能を利用したり理解したりする手助けとなります。

これらの変更により、文書が全体としてよりユーザーフレンドリーになり、特に新しい利用者がREST APIの実装方法や機能を通じて学習しやすくなる効果が期待されます。

## articles/search/search-agentic-retrieval-how-to-pipeline.md{#item-1ad1c3}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ ms.custom:
 
 This article describes an approach or pattern for building a solution that uses Azure AI Search for knowledge retrieval, and how to integrate knowledge retrieval into a custom solution that includes Azure AI Agent. This pattern uses an agent tool to invoke an agentic retrieval pipeline in Azure AI Search.
 
-:::image type="content" source="media/agentic-retrieval/agent-to-agent-pipeline.png" alt-text="Diagram of Azure AI Search integration with Azure AI Agent service." lightbox="media/agentic-retrieval/agent-to-agent-pipeline.png" :::
+:::image type="content" source="media/agentic-retrieval/agent-to-agent-pipeline.svg" alt-text="Diagram of Azure AI Search integration with Azure AI Agent service." lightbox="media/agentic-retrieval/agent-to-agent-pipeline.png" :::
 
 This article supports the [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) Python sample on GitHub.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルパイプラインの画像更新"
}
```

### Explanation
この変更は、`search-agentic-retrieval-how-to-pipeline.md`というドキュメント内で行われた軽微な更新を示しています。具体的な変更点は以下の通りです。

1. **画像ファイル形式の変更**: エージェントリトリーバルパイプラインを示す画像の形式が、PNG形式からSVG形式に変更されました。新しいSVG形式の画像は、スケーラブルなベクターグラフィックスとして、異なる解像度でも鮮明さを保つことができるため、ユーザーにとってより視覚的に優れた体験を提供します。

2. **画像の参照更新**: 画像のソースパスが更新され、表示される内容が最新の情報を反映するようになっています。altテキストはそのまま維持されており、画像がどのような内容を示しているかを明確にしています。

この変更により、視覚的なコンテンツが改善され、読者がAzure AI SearchとAzure AI Agentの統合についてより良い理解を得る手助けとなります。全体として、ドキュメントの内容が更新・強化されることで、より効果的な情報提供が実現されています。

## articles/search/search-indexer-field-mappings.md{#item-0e4628}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 02/24/2025
+ms.date: 09/23/2025
 ms.update-cycle: 180-days
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーフィールドマッピングドキュメントの日付更新"
}
```

### Explanation
この変更は、`search-indexer-field-mappings.md`というドキュメントの軽微な更新を示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの最終更新日が`02/24/2025`から`09/23/2025`に変更されました。この日付の更新は、読者に最新の情報が提供されていることを示し、情報の信頼性を高めます。

この変更は比較的単純ですが、ドキュメントが最新の日付であることを反映させることで、ユーザーが新しい情報を期待できるようになります。全体として、ユーザー体験が向上し、コンテンツの管理が適切に行われていることを示しています。

## articles/search/search-what-is-data-import.md{#item-d73ef5}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 05/08/2025
+ms.date: 09/23/2025
 ---
 
 # Data import in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データインポートに関するドキュメントの日付更新"
}
```

### Explanation
この変更は、`search-what-is-data-import.md`というドキュメントの軽微な更新を示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの最終更新日が`05/08/2025`から`09/23/2025`に変更されました。この日付の変更は、文書が最新の情報を反映していることを示唆し、利用者が情報に信頼を寄せるのに役立ちます。

この軽微な変更は、ドキュメント管理において重要であり、読者が最新の知識を得られるようにするためのステップです。全体として、コンテンツが最新の情報であることを示し、ユーザー体験の向上に寄与します。

## articles/search/service-configure-firewall.md{#item-75be3f}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/20/2025
+ms.date: 09/23/2025
 ms.custom:
   - ignite-2023
   - sfi-image-nochange
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイアウォール設定に関するドキュメントの日付更新"
}
```

### Explanation
この変更は、`service-configure-firewall.md`というドキュメントの軽微な更新を示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの最終更新日が`05/20/2025`から`09/23/2025`に変更されました。この更新により、文書が最新の情報を反映し、ユーザーに信頼性の高い内容を提供していることを示します。

この変更は、情報が新鮮であることを保障する重要なステップであり、利用者が信頼できる情報源としてこのドキュメントを利用できるようにします。全体として、コンテンツの適時性が保たれ、ユーザー体験が向上するでしょう。

## articles/search/service-create-private-endpoint.md{#item-65e817}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 04/14/2025
+ms.date: 09/23/2025
 ---
 
 # Create a private endpoint for a secure connection to Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートエンドポイント作成に関するドキュメントの日付更新"
}
```

### Explanation
この変更は、`service-create-private-endpoint.md`というドキュメントの軽微な更新を示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの最終更新日が`04/14/2025`から`09/23/2025`に変更されました。この変更により、文書が最新の情報を反映し、読者に対して信頼できる情報を提供していることが示されます。

このような軽微な更新は、コンテンツの整合性を保つために重要であり、ユーザーが最新の情報にアクセスできるようにするための措置です。全体として、ドキュメントの適時性が向上し、読者の信頼感も増すでしょう。

## articles/search/tutorial-csharp-deploy-static-web-app.md{#item-a2300f}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: tutorial
-ms.date: 01/17/2025
+ms.date: 09/23/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# チュートリアルのドキュメントの日付更新"
}
```

### Explanation
この変更は、`tutorial-csharp-deploy-static-web-app.md`というドキュメントの軽微な更新を示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの最終更新日が`01/17/2025`から`09/23/2025`に変更されました。この変更により、ドキュメントが最新の情報を反映し、読者に信頼性のある内容を提供することが強調されています。

このような更新は、読者がコンテンツを利用する際に、最新の情報に基づいて判断できるようにするために重要です。従って、全体として、このドキュメントはより信頼性を増し、ユーザー体験の向上に寄与すると考えられます。

## articles/search/tutorial-csharp-overview.md{#item-57fa0d}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: tutorial
-ms.date: 01/17/2025
+ms.date: 09/23/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# チュートリアルの概要ドキュメントの日付更新"
}
```

### Explanation
この変更は、`tutorial-csharp-overview.md`というドキュメントの軽微な更新を示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの最終更新日が`01/17/2025`から`09/23/2025`に変更されました。このアップデートにより、文書が最新の情報を反映し、読者に対して信頼できるデータを提供していることが強調されています。

このような軽微な更新は、ドキュメントの信頼性を高めるだけでなく、読者が最新の情報を利用できるようにするためにも重要です。この更新により、コンテンツの整合性が保たれ、全体的なユーザー体験の向上に寄与することでしょう。

## articles/search/tutorial-csharp-search-query-integration.md{#item-8ad6b5}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: tutorial
-ms.date: 01/21/2025
+ms.date: 09/23/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# 検索クエリ統合チュートリアルのドキュメントの日付更新"
}
```

### Explanation
この変更は、`tutorial-csharp-search-query-integration.md`というドキュメントの軽微な更新を示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの最終更新日が`01/21/2025`から`09/23/2025`に変更されました。この変更により、文書が最新の情報を反映し、ユーザーに信頼性の高い内容を提供していることが強調されています。

このような更新は、コンテンツの精度を保つために重要であり、読者が最新の情報に基づいて判断できるようにするために寄与します。この変更により、全体的なユーザー体験の向上が期待されます。

## articles/search/tutorial-rag-build-solution-minimize-storage.md{#item-088ad8}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: tutorial
-ms.date: 02/05/2025
+ms.date: 09/23/2025
 ms.custom: sfi-ropc-nochange
 
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAG構築ソリューションに関するチュートリアルの日付更新"
}
```

### Explanation
この変更は、`tutorial-rag-build-solution-minimize-storage.md`というドキュメントの軽微な更新を示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの最終更新日が`02/05/2025`から`09/23/2025`に変更されました。この更新により、内容が最新の情報を反映し、読者に正確なデータが提供されることになります。

このようなアップデートは、ドキュメントの整合性を保つために重要です。読者が信頼性のある情報に基づいて判断できるようにするために、この変更は全体的なユーザー体験の向上に寄与します。

## articles/search/vector-search-how-to-storage-options.md{#item-ee1680}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 03/31/2025
+ms.date: 09/19/2025
 ---
 
 # Eliminate optional vector instances from storage
@@ -46,18 +46,18 @@ To mitigate the loss in information, you can [enable "rescoring" and "oversampli
 
 ## Remove source vectors (JSON data)
 
-The `stored` property is a boolean property on a vector field definition that determines whether storage is allocated for retrievable vector field content obtained during indexing (the source instance). The `stored` property is true by default. If you don't need raw vector content in a query response, you can save up to 50 percent storage per field by changing `stored` to false.
+In a vector field definition, `stored` is a boolean property that determines whether storage is allocated for retrievable vector content obtained during indexing (the source instance). By default, `stored` is set to `true`. If you don't need raw vector content in a query response, changing `stored` to `false` can save up to 50% storage per field.
 
-Considerations for setting `stored` to false:
+Considerations for setting `"stored": false`:
 
-- Because vectors aren't human readable, you can omit them from results sent to LLMs in RAG scenarios, and from results that are rendered on a search page. Keep them, however, if you're using vectors in a downstream process that consumes vector content.
+- Because vectors aren't human readable, you can omit them from results sent to LLMs in RAG scenarios or from results rendered on a search page. However, keep them if you're using vectors in a downstream process that consumes vector content.
 
-- However, if your indexing strategy includes [partial document updates](search-howto-reindex.md#update-content), such as "merge" or "mergeOrUpload" on an existing document, setting `stored=false` prevents content updates to those fields during the merge. On each "merge" or "mergeOrUpload" operation to a search document, you must provide the vector fields in its entirety, along with the nonvector fields that you're updating, or the vector is dropped.
+- If your indexing strategy uses [partial document updates](search-howto-reindex.md#update-content), such as `merge` or `mergeOrUpload` on an existing document, setting `"stored": false` prevents content updates to those fields during the merge. You must include the entire vector field (and nonvector fields you're updating) in each reindexing operation. Otherwise, the vector data is lost without an error or warning. To avoid this risk altogether, set `"stored": true`.
 
 > [!IMPORTANT]
-> Setting the `stored=false` attribution is irreversible. This property can only be set when you create the index and is only allowed on vector fields. Updating an existing index with new vector fields can't set this property to `false`. If you want retrievable vector content later, you must drop and rebuild the index, or create and load a new field that has the new attribution.
+> Setting the `"stored": false` attribution is irreversible. This property can only be set when you create the index and is only allowed on vector fields. Updating an existing index with new vector fields can't set this property to `false`. If you want retrievable vector content later, you must drop and rebuild the index or create and load a new field that has the new attribution.
 
-For new vector fields in a search index, set `stored` to false to permanently remove retrievable storage for the vector field. The following example shows a vector field definition with the `stored` property.
+For new vector fields in a search index, set `"stored": false` to permanently remove retrievable storage for the vector field. The following example shows a vector field definition with the `stored` property.
 
 ```http
 PUT https://[service-name].search.windows.net/indexes/demo-index?api-version=2024-07-01 
@@ -81,13 +81,13 @@ PUT https://[service-name].search.windows.net/indexes/demo-index?api-version=202
 
 ### Summary of key points
 
-- Applies to fields having a [vector data type](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields).
+- Applies to fields that have a [vector data type](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields).
 
-- Affects storage on disk, not memory, and it has no effect on queries. Query execution uses a separate vector index that's unaffected by the `stored` property because that copy of the vector is always stored.
+- Affects storage on disk, not memory, and has no effect on queries. Query execution uses a separate vector index that's unaffected by the `stored` property because that copy of the vector is always stored.
 
-- The `stored` property is set during index creation on vector fields and is irreversible. If you want retrievable content later, you must drop and rebuild the index, or create and load a new field that has the new attribution.
+- The `stored` property is set during index creation on vector fields and is irreversible. If you want retrievable content later, you must drop and rebuild the index or create and load a new field that has the new attribution.
 
-- Defaults are `stored` set to true and `retrievable` set to false. In a default configuration, a retrievable copy is stored, but it's not automatically returned in results. When `stored` is true, you can toggle `retrievable` between true and false at any time without having to rebuild an index. When `stored` is false, `retrievable` must be false and can't be changed.
+- Defaults are `"stored": true` and `"retrievable": false`. In a default configuration, a retrievable copy is stored but isn't automatically returned in results. When `stored` is `true`, you can toggle `retrievable` between `true` and `false` at any time without having to rebuild an index. When `stored` is `false`, `retrievable` must be `false` and can't be changed.
 
 ## Remove full-precision vectors (binary data)
 
@@ -102,10 +102,10 @@ The `rescoreStorageMethod` property controls whether full-precision vectors are
 - For scalar quantization, preserve original full-precision vectors in the index because they're required for rescore.
 - For binary quantization, preserve original full-precision vectors for the highest quality of rescoring, or discard full-precision vectors (requires 2025-03-01-preview) if you want to rescore based on the dot product of the binary embeddings.
 
-Vector storage strategies have been evolving over the last several releases. Index creation date and API version determine your storage options. 
+Vector storage strategies have been evolving over the last several releases. Index creation date and API version determine your storage options.
 
 | API version | Applies to | Remove full-precision vectors |
-|-------------|-------------------------------|
+|--|--|--|
 | 2024-07-01 and earlier | Not applicable. | There's no mechanism for removing full-precision vectors. |
 | 2024-11-01-preview | Binary embeddings | Use `rescoreStorageMethod.discardOriginals` to remove full-precision vectors, but doing so prevents rescoring. `enableRescoring` must be false if originals are gone.|
 | 2025-03-01-preview | Binary embeddings | Use `rescoreStorageMethod.discardOriginals` to remove full-precision vectors in the index while still retaining rescore options. In this preview, rescoring is possible because the technique changed. The dot product of the binary embeddings is used on the rescore, producing high quality search results equivalent to or better than earlier techniques based on full-precision vectors. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のストレージオプションに関するチュートリアルの内容更新"
}
```

### Explanation
この変更は、`vector-search-how-to-storage-options.md`というドキュメントの内容を更新したことを示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: 最終更新日が`03/31/2025`から`09/19/2025`に変更され、文書が最新の情報を反映しています。

2. **テキストの改訂**: ドキュメント内の文章が明確に表現され、重要な点が強調されています。例えば、`stored` プロパティの説明が、より簡潔で理解しやすい形に書き直されています。また、重要な注意事項や条件に関する記述も、さらなる明確化が施されています。

3. **コードブロックの修正**: コードの例において、プロパティの表記が統一され、`stored`が真である場合や偽である場合の動作がより明確に記述されています。また、リスクに関する注意も詳しく説明されています。

この変更は、ユーザーがベクトル検索に関連するストレージオプションを理解しやすくするために重要です。更新された内容により、開発者はより効果的にこの技術を利用できるようになることが期待されます。

## articles/search/vector-search-how-to-truncate-dimensions.md{#item-8350a3}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 06/12/2025
+ms.date: 09/19/2025
 ---
 
 # Truncate dimensions using MRL compression (preview)
@@ -21,7 +21,10 @@ Exercise the ability to use fewer dimensions on text-embedding-3 models. On Azur
 
 In Azure AI Search, MRL support supplements [scalar and binary quantization](vector-search-how-to-quantization.md). When you use either quantization method, you can specify a `truncationDimension` property on your vector fields to reduce the dimensionality of text embeddings.
 
-MRL multilevel compression saves on vector storage and improves query response times for vector queries based on text embeddings. In Azure AI Search, MRL support is only offered together with another method of quantization. Using binary quantization with MRL provides the maximum vector index size reduction. To achieve maximum storage reduction, use binary quantization with MRL and set `stored` to false.
+MRL multilevel compression saves on vector storage and improves query response times for vector queries based on text embeddings. In Azure AI Search, MRL support is only offered together with another method of quantization. Using binary quantization with MRL provides the maximum vector index size reduction. To achieve maximum storage reduction, use binary quantization with MRL and set `stored` to `false`.
+
+> [!WARNING]
+> If you set `stored` to `false`, vector data is lost during partial document updates unless you provide the entire vector in each update. Set `stored` to `true` to avoid this issue. For more information, see [Eliminate optional vector instances from storage](vector-search-how-to-storage-options.md).
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "次元の切り捨てに関するチュートリアルの内容更新"
}
```

### Explanation
この変更は、`vector-search-how-to-truncate-dimensions.md`というドキュメントに軽微な更新が行われたことを示しています。具体的な変更点は以下の通りです。

1. **日付の更新**: 最終更新日が`06/12/2025`から`09/19/2025`に変更され、文書の内容が最新の情報を反映するようにされています。

2. **テキストの改訂**: ドキュメント内のテキストが若干の修正を受け、明確さを増しています。特に、`stored` プロパティの値を`false`に設定することに関する警告が追加されました。この警告により、部分的な文書更新の際にベクトルデータが失われるリスクについて注意が喚起されています。

3. **新しい警告メッセージ**: 
   - `stored`を`false`に設定する場合、各更新においてベクトル全体を提供しない限りデータが失われる可能性があることを警告するメッセージが追加されました。また、問題を回避するために`stored`を`true`に設定することが推奨されています。

この変更は、ユーザーが次元を切り捨てる際に注意すべき重要なポイントを明確にするものであり、ドキュメントをより信頼性のあるものにしています。情報の更新により、読者はAzure AI Searchにおけるベクトル処理について、より安全かつ効果的に理解できるようになります。


