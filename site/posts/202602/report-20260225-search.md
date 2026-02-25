---
date: '2026-02-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6a204e3...MicrosoftDocs:7d59142
summary: |-
  このコード差分ドキュメントは、Azure AI Searchおよびエージェント的検索に関するドキュメンテーションの強化を目的とした複数の軽微な更新と重要な機能変更を含みます。具体的には、C#、Java、JavaScript、Python、REST APIにおけるエージェント的検索のクイックスタートガイドが大幅に改訂され、新しい機能や手順が追加されました。また、JavaおよびPythonにエージェント的検索の詳細が追加され、「quickstart-agentic-retrieval」サンプルが新たに含まれています。

  大規模な変更により、古い手順との互換性が失われる可能性がありますが、ユーザーは新機能をより直感的に使用できるようになります。文言の修正やリンクの更新なども行われ、ドキュメンテーションの正確性が向上しました。全体として、これらの更新はAzure AI Searchの機能を学びやすくし、ユーザーの生産性向上を目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6a204e3...MicrosoftDocs:7d59142){target="_blank"}

<format>
# ハイライト
このコード差分ドキュメントは、Azure AI Searchおよびエージェント的検索関連のドキュメンテーションを強化することを目的とした複数の軽微な更新と、いくつかの重要な機能変更を含みます。特に、エージェント的検索のクイックスタートガイドでの大幅な機能改訂がC#、Java、JavaScript、Python、およびREST APIで行われ、一部のガイドでは新しい機能や手順の追加が行われました。

## 新機能
- エージェント的検索の設定や使用方法に関する詳細がJavaおよびPythonに追加されました。
- 「quickstart-agentic-retrieval」サンプルがAzure AI Searchサンプルガイドに追加され、新しいクエリ計画と回答生成の機能が示されました。

## 破壊的変更
- エージェント的検索のC#、Java、Python、REST APIクイックスタートガイドの大規模な更新と手順の再構築。
- 古いコードや冗長な部分が削除され、最新機能に対応する情報が追加され、以前の使い方と互換性がない可能性があります。

## その他の更新
- 軽微な文言の修正、日付の更新、および古いリンクの新しいリソースへの更新が数多く含まれています。
- Azure SDKのPythonサンプルリンクの更新などの、ドキュメンテーションの正確性と最新性の向上。

# インサイト
この一連のコード差分ドキュメントは、Azureにおける新しい検索エージェント機能を強化する取り組みを示しています。複数のクイックスタートガイドが大幅に改訂されており、特にC#、Java、Python、JavaScript、REST APIのガイドが一新されています。これにより、開発者は最新の技術スタックを活用しやすくなり、Azureのエージェント的検索機能をより効率的に実装することが可能になります。

大規模な変更によって古い手順との互換性が失われる可能性はありますが、ユーザーがより直感的に新機能を使用できるように、新しい手順や機能の追加が強調されています。特に役割ベースのアクセス制御やMicrosoft Entra IDの認証に関する記述が整理されるなど、これらの改訂はAzureサービスのセキュリティ向上を目的としています。

加えて、今回の変更では、ユーザーが最新の情報にアクセスできるよう日付の更新やリンクの修正が頻繁に行われています。ユーザーが最新リソースにアクセスして直ちに実装に取りかかれることを重視した姿勢が伺え、これがユーザーエクスペリエンス向上に寄与しています。

結論として、これらのドキュメントの更新は、Azure AI Searchの新機能に対応した学習と実装を促進し、全体的なユーザーの生産性向上を目指したものです。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | エージェント的検索パイプラインの構成に関する修正 | modified | 1 | 1 | 2 | 
| [cognitive-search-skill-genai-prompt.md](#item-384bf9) | minor update | GenAIプロンプトスキルに関する内容の更新 | modified | 2 | 2 | 4 | 
| [get-started-portal-agentic-retrieval.md](#item-2bf1dc) | minor update | エージェント的検索ポータルのクイックスタートガイド更新 | modified | 12 | 34 | 46 | 
| [agentic-retrieval-csharp.md](#item-f93ed3) | breaking change | エージェント的検索C#クイックスタートの大幅な更新 | modified | 68 | 409 | 477 | 
| [agentic-retrieval-java.md](#item-4e2c55) | breaking change | エージェント的検索Javaクイックスタートの大幅な更新 | modified | 369 | 1220 | 1589 | 
| [agentic-retrieval-javascript.md](#item-715283) | minor update | エージェント的検索JavaScriptクイックスタートの更新 | modified | 44 | 94 | 138 | 
| [agentic-retrieval-python.md](#item-efee6a) | breaking change | エージェント的検索Pythonクイックスタートの大幅な更新 | modified | 39 | 321 | 360 | 
| [agentic-retrieval-rest.md](#item-3df373) | breaking change | エージェント的検索RESTクイックスタートの大幅な改訂 | modified | 30 | 235 | 265 | 
| [agentic-retrieval-setup.md](#item-e5e297) | minor update | エージェント的検索のセットアップガイドの一部修正 | modified | 18 | 50 | 68 | 
| [agentic-retrieval-typescript.md](#item-e6370b) | minor update | エージェント的検索のTypeScriptクイックスタートガイドの更新 | modified | 28 | 78 | 106 | 
| [full-text-java.md](#item-d659f9) | minor update | フルテキスト検索のJavaクイックスタートガイドの更新 | modified | 13 | 1 | 14 | 
| [search-get-started-vector-python.md](#item-53085f) | minor update | Vector検索のPythonクイックスタートガイドの更新 | modified | 1 | 1 | 2 | 
| [samples-java.md](#item-5992fd) | minor update | Javaサンプルガイドの更新 | modified | 2 | 1 | 3 | 
| [search-get-started-agentic-retrieval.md](#item-4a40f4) | minor update | エージェントリトリーバルのクイックスタートガイドの日付更新 | modified | 1 | 1 | 2 | 
| [search-how-to-index-onelake-files.md](#item-95f3db) | minor update | OneLakeファイルのインデックス作成に関するガイドの更新 | modified | 8 | 2 | 10 | 
| [search-howto-complex-data-types.md](#item-75a002) | minor update | 複雑なデータ型に関するガイドのサンプルリンク更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -125,7 +125,7 @@ To configure access for this solution:
 
    + `AZURE_OPENAI_ENDPOINT` is on the **Endpoints** page of your project's parent resource.
 
-1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Microsoft Foundry project.
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search and Microsoft Foundry resources.
 
     ```azurecli
     az login
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的検索パイプラインの構成に関する修正"
}
```

### Explanation
このコードの変更は、ドキュメント「エージェント的検索パイプラインの作成方法」に関するもので、Azure AI SearchサービスとMicrosoft Foundryプロジェクトに関連するリソースの説明を明確にするために行われました。具体的には、元の文章は「Azure AI SearchサービスとMicrosoft Foundryプロジェクト」を指していましたが、修正後は「Azure AI SearchおよびMicrosoft Foundryリソース」となり、リソースに関する説明がより包括的になっています。この変更により、ユーザーがリソースにアクセスする際の理解が促進されることが期待されます。

## articles/search/cognitive-search-skill-genai-prompt.md{#item-384bf9}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2025
 ms.topic: reference
-ms.date: 02/12/2026
+ms.date: 02/26/2026
 ---
 
 # GenAI Prompt skill
@@ -24,7 +24,7 @@ Here are some examples of how the GenAI prompt skill can help you create content
 - Simplify complex content
 - Perform any other task that you can articulate in a prompt
 
-The GenAI Prompt skill is available in the [latest preview REST API](/rest/api/searchservice/skillsets/create?view=rest-searchservice-2025-11-01-preview&preserve-view=true). This skill supports text, image, and multimodal content, such as a PDF that contains text and images.
+The GenAI Prompt skill is available in the [latest preview REST API](/rest/api/searchservice/skillsets/create?view=rest-searchservice-2025-11-01-preview&preserve-view=true). This skill supports text, image, and multimodal content, such as images with visuals and text extracted from PDF files.
 
 > [!TIP]
 > It's common to use this skill combined with a data chunking skill. The following tutorials demonstrate image verbalization with two different data chunking techniques:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GenAIプロンプトスキルに関する内容の更新"
}
```

### Explanation
このコードの変更は、ドキュメント「Cognitive Search Skill: GenAI Prompt」に関するもので、主に日付の更新と説明文の明確化が行われました。具体的には、ドキュメントの日付が2026年2月12日から2026年2月26日に変更されました。また、GenAIプロンプトスキルの説明も更新され、PDFファイルから抽出されたテキストと画像を含むビジュアルを指すようになりました。これにより、スキルの機能がより正確に表現されており、ユーザーがこのスキルの適用範囲をより理解しやすくなっています。

## articles/search/get-started-portal-agentic-retrieval.md{#item-2bf1dc}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2025
 ms.topic: quickstart
-ms.date: 02/05/2026
+ms.date: 02/23/2026
 ---
 
 # Quickstart: Agentic retrieval in the Azure portal
@@ -39,9 +39,9 @@ Afterwards, you test the knowledge base by submitting a complex query that requi
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
-+ For text-to-vector conversion, an embedding model [deployed to your project](/azure/ai-foundry/how-to/deploy-models-openai). You can use any `text-embedding` model, such as `text-embedding-3-large`.
++ An embedding model [deployed to your project](/azure/ai-foundry/how-to/deploy-models-openai) for text-to-vector conversion. You can use any `text-embedding` model, such as `text-embedding-3-large`.
 
-+ For query planning and answer generation, an LLM [deployed to your project](/azure/ai-foundry/how-to/deploy-models-openai). You can use any [portal-supported LLM](#supported-llms).
++ An LLM [deployed to your project](/azure/ai-foundry/how-to/deploy-models-openai) for query planning and answer generation. You can use any [portal-supported LLM](#supported-llms).
 
 ### Supported LLMs
 
@@ -55,45 +55,23 @@ Although agentic retrieval [programmatically supports several LLMs](agentic-retr
 
 ## Configure access
 
-Before you begin, make sure you have permissions to access content and operations. We recommend Microsoft Entra ID for authentication and role-based access for authorization. You must be an **Owner** or **User Access Administrator** to assign roles. If roles aren't feasible, use [key-based authentication](search-security-api-keys.md) instead.
+Before you begin, make sure you have permissions to access content and operations. This quickstart uses Microsoft Entra ID for authentication and role-based access for authorization. You must be an **Owner** or **User Access Administrator** to assign roles. If roles aren't feasible, use [key-based authentication](search-security-api-keys.md) instead.
 
-To configure access for this quickstart, select each of the following tabs.
+To configure access for this quickstart:
 
-### [Azure AI Search](#tab/search-perms)
+1. Sign in to the [Azure portal](https://portal.azure.com).
 
-Azure AI Search provides the agentic retrieval pipeline. Configure access for yourself and your search service to read and write data, interact with other Azure services, and run the pipeline.
+1. On your Azure AI Search service:
 
-On your Azure AI Search service:
+    1. [Enable role-based access](search-security-enable-roles.md).
 
-1. [Enable role-based access](search-security-enable-roles.md).
+    1. [Create a system-assigned managed identity](search-how-to-managed-identities.md#create-a-system-managed-identity).
 
-1. [Configure a system-assigned managed identity](search-how-to-managed-identities.md#create-a-system-managed-identity).
+    1. [Assign the following roles](search-security-rbac.md) to your user account: **Search Service Contributor**, **Search Index Data Contributor**, and **Search Index Data Reader**.
 
-1. [Assign the following roles](search-security-rbac.md) to yourself.
+1. On your Azure Blob Storage account, assign **Storage Blob Data Contributor** to the managed identity of your search service.
 
-   + **Search Service Contributor**
-
-   + **Search Index Data Contributor**
-
-   + **Search Index Data Reader**
-
-### [Azure Blob Storage](#tab/storage-perms)
-
-Azure Blob Storage stores your source documents for indexing and retrieval. Grant your search service permission to read, write, and delete the documents.
-
-On your Azure Blob Storage account:
-
-+ Assign **Storage Blob Data Reader** to your [search service identity](search-how-to-managed-identities.md#create-a-system-managed-identity).
-
-### [Microsoft Foundry](#tab/foundry-perms)
-
-Microsoft Foundry provides the Azure OpenAI models used for embeddings, query planning, and answer generation. Grant your search service permission to use these models.
-
-On your Microsoft Foundry resource:
-
-+ Assign **Cognitive Services User** to your [search service identity](search-how-to-managed-identities.md#create-a-system-managed-identity).
-
----
+1. On your Microsoft Foundry resource, assign **Cognitive Services User** to the managed identity of your search service.
 
 > [!IMPORTANT]
 > Agentic retrieval has two token-based billing models:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的検索ポータルのクイックスタートガイド更新"
}
```

### Explanation
このコードの変更は、Azureポータルにおけるエージェント的検索のクイックスタートガイドに関するもので、いくつかの重要な更新が行われました。主な変更点として、日付が2026年2月5日から2026年2月23日に変更され、情報が最新の状態に保たれています。また、リソースと関連する役割の説明が明確化され、手順が整理されています。特に、「Microsoft Entra IDによる認証」と「役割に基づくアクセス」の記述が簡略化され、手順が番号付きリストに整理されていることで、ユーザーがよりわかりやすく操作を進められるようになっています。さらに、役割の割り当てに関する情報が整頓され、実施する必要があるステップが明示されています。全体として、これにより、ユーザーはエージェント的検索の環境設定を効率的に行えるようになります。

## articles/search/includes/quickstarts/agentic-retrieval-csharp.md{#item-f93ed3}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 01/14/2026
+ms.date: 02/23/2026
 ms.custom: dev-focus
 ai-usage: ai-assisted
 ---
@@ -15,10 +15,10 @@ In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview
 
 A *knowledge base* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the knowledge base outputs raw content from your sources, but this quickstart uses the answer synthesis output mode for natural-language answer generation.
 
-Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
+Although you can use your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book.
 
 > [!TIP]
-> Want to get started right away? See the [azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) GitHub repository.
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) on GitHub.
 
 ## Prerequisites
 
@@ -28,372 +28,64 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
-+ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
-
-+ [Visual Studio Code](https://code.visualstudio.com/download).
++ An embedding model [deployed to your project](/azure/ai-foundry/how-to/deploy-models-openai) for text-to-vector conversion. You can use any `text-embedding` model, such as `text-embedding-3-large`.
 
-[!INCLUDE [Setup](./agentic-retrieval-setup.md)]
++ An LLM [deployed to your project](/azure/ai-foundry/how-to/deploy-models-openai) for query planning and answer generation. You can use any [supported LLM](../../agentic-retrieval-how-to-create-knowledge-base.md#supported-models), such as `gpt-5-mini`.
 
-## Set up the environment
++ [.NET 8](https://dotnet.microsoft.com/download/dotnet/8.0) or later.
 
-To set up the console application for this quickstart:
++ [Visual Studio Code](https://code.visualstudio.com/download).
 
-1. Create a folder named `quickstart-agentic-retrieval` to contain the application.
++ [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-1. Open the folder in Visual Studio Code.
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-1. Select **Terminal** > **New Terminal**, and then run the following command to create a console application.
+[!INCLUDE [agentic retrieval setup](agentic-retrieval-setup.md)]
 
-    ```console
-    dotnet new console
-    ```
+## Set up the environment
 
-1. Install the [Azure AI Search client library for .NET](/dotnet/api/overview/azure/search.documents-readme).
+1. Use Git to clone the sample repository.
 
-    ```console
-    dotnet add package Azure.Search.Documents --version 11.8.0-beta.1
+    ```bash
+    git clone https://github.com/Azure-Samples/azure-search-dotnet-samples
     ```
 
-1. Install the `dotenv.net` package to load environment variables from a `.env` file.
+1. Navigate to the quickstart folder and open it in Visual Studio Code.
 
-    ```console
-    dotnet add package dotenv.net
+    ```bash
+    cd azure-search-dotnet-samples/quickstart-agentic-retrieval
+    code .
     ```
 
-1. For keyless authentication with Microsoft Entra ID, install the [Azure.Identity](https://www.nuget.org/packages/Azure.Identity) package.
-
-    ```console
-    dotnet add package Azure.Identity
-    ```
+1. In `sample.env`, replace the placeholder values for `SEARCH_ENDPOINT` and `AOAI_ENDPOINT` with the URLs you obtained in [Get endpoints](#get-endpoints).
 
-1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Microsoft Foundry project.
+1. Rename `sample.env` to `.env`.
 
-    ```console
-    az login
+    ```bash
+    mv sample.env .env
     ```
 
-## Run the code
+1. Install the dependencies.
 
-To create and run the agentic retrieval pipeline:
+    ```bash
+    dotnet restore AgenticRetrievalQuickstart.csproj
+    ```
 
-1. Create a file named `.env` in the `quickstart-agentic-retrieval` folder.
+    When the restore completes, verify that no errors appear in the output.
 
-1. Paste the following environment variables into the `.env` file.
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search and Microsoft Foundry resources.
 
-    ```
-    SEARCH_ENDPOINT = PUT-YOUR-SEARCH-SERVICE-URL-HERE
-    AOAI_ENDPOINT = PUT-YOUR-AOAI-FOUNDRY-URL-HERE
+    ```bash
+    az login
     ```
 
-1. Set `SEARCH_ENDPOINT` and `AOAI_ENDPOINT` to the values you obtained in [Get endpoints](#get-endpoints).
-
-1. Paste the following code into the `Program.cs` file.
-
-    ```csharp
-    using dotenv.net;
-    using System.Text.Json;
-    using Azure.Identity;
-    using Azure.Search.Documents;
-    using Azure.Search.Documents.Indexes;
-    using Azure.Search.Documents.Indexes.Models;
-    using Azure.Search.Documents.KnowledgeBases;
-    using Azure.Search.Documents.KnowledgeBases.Models;
-    
-    namespace AzureSearch.Quickstart
-    {
-        class Program
-        {
-            static async Task Main(string[] args)
-            {
-                // Load environment variables from the .env file
-                // Ensure your .env file is in the same directory with the required variables
-                DotEnv.Load();
-    
-                string searchEndpoint = Environment.GetEnvironmentVariable("SEARCH_ENDPOINT")
-                    ?? throw new InvalidOperationException("SEARCH_ENDPOINT isn't set.");
-                string aoaiEndpoint = Environment.GetEnvironmentVariable("AOAI_ENDPOINT")
-                    ?? throw new InvalidOperationException("AOAI_ENDPOINT isn't set.");
-    
-                string aoaiEmbeddingModel = "text-embedding-3-large";
-                string aoaiEmbeddingDeployment = "text-embedding-3-large";
-                string aoaiGptModel = "gpt-5-mini";
-                string aoaiGptDeployment = "gpt-5-mini";
-    
-                string indexName = "earth-at-night";
-                string knowledgeSourceName = "earth-knowledge-source";
-                string knowledgeBaseName = "earth-knowledge-base";
-    
-                var credential = new DefaultAzureCredential();
-    
-                // Define fields for the index
-                var fields = new List<SearchField>
-                {
-                    new SimpleField("id", SearchFieldDataType.String) { IsKey = true, IsFilterable = true, IsSortable = true, IsFacetable = true },
-                    new SearchField("page_chunk", SearchFieldDataType.String) { IsFilterable = false, IsSortable = false, IsFacetable = false },
-                    new SearchField("page_embedding_text_3_large", SearchFieldDataType.Collection(SearchFieldDataType.Single)) { VectorSearchDimensions = 3072, VectorSearchProfileName = "hnsw_text_3_large" },
-                    new SimpleField("page_number", SearchFieldDataType.Int32) { IsFilterable = true, IsSortable = true, IsFacetable = true }
-                };
-    
-                // Define a vectorizer
-                var vectorizer = new AzureOpenAIVectorizer(vectorizerName: "azure_openai_text_3_large")
-                {
-                    Parameters = new AzureOpenAIVectorizerParameters
-                    {
-                        ResourceUri = new Uri(aoaiEndpoint),
-                        DeploymentName = aoaiEmbeddingDeployment,
-                        ModelName = aoaiEmbeddingModel
-                    }
-                };
-    
-                // Define a vector search profile and algorithm
-                var vectorSearch = new VectorSearch()
-                {
-                    Profiles =
-                    {
-                        new VectorSearchProfile(
-                            name: "hnsw_text_3_large",
-                            algorithmConfigurationName: "alg"
-                        )
-                        {
-                            VectorizerName = "azure_openai_text_3_large"
-                        }
-                    },
-                    Algorithms =
-                    {
-                        new HnswAlgorithmConfiguration(name: "alg")
-                    },
-                    Vectorizers =
-                    {
-                        vectorizer
-                    }
-                };
-    
-                // Define a semantic configuration
-                var semanticConfig = new SemanticConfiguration(
-                    name: "semantic_config",
-                    prioritizedFields: new SemanticPrioritizedFields
-                    {
-                        ContentFields = { new SemanticField("page_chunk") }
-                    }
-                );
-    
-                var semanticSearch = new SemanticSearch()
-                {
-                    DefaultConfigurationName = "semantic_config",
-                    Configurations = { semanticConfig }
-                };
-    
-                // Create the index
-                var index = new SearchIndex(indexName)
-                {
-                    Fields = fields,
-                    VectorSearch = vectorSearch,
-                    SemanticSearch = semanticSearch
-                };
-    
-                // Create the index client, deleting and recreating the index if it exists
-                var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
-                await indexClient.CreateOrUpdateIndexAsync(index);
-                Console.WriteLine($"Index '{indexName}' created or updated successfully.");
-    
-                // Upload sample documents from the GitHub URL
-                string url = "https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json";
-                var httpClient = new HttpClient();
-                var response = await httpClient.GetAsync(url);
-                response.EnsureSuccessStatusCode();
-                var json = await response.Content.ReadAsStringAsync();
-                var documents = JsonSerializer.Deserialize<List<Dictionary<string, object>>>(json);
-                var searchClient = new SearchClient(new Uri(searchEndpoint), indexName, credential);
-                var searchIndexingBufferedSender = new SearchIndexingBufferedSender<Dictionary<string, object>>(
-                    searchClient,
-                    new SearchIndexingBufferedSenderOptions<Dictionary<string, object>>
-                    {
-                        KeyFieldAccessor = doc => doc["id"].ToString(),
-                    }
-                );
-
-                await searchIndexingBufferedSender.UploadDocumentsAsync(documents);
-                await searchIndexingBufferedSender.FlushAsync();
-                Console.WriteLine($"Documents uploaded to index '{indexName}' successfully.");
-    
-                // Create a knowledge source
-                var indexKnowledgeSource = new SearchIndexKnowledgeSource(
-                    name: knowledgeSourceName,
-                    searchIndexParameters: new SearchIndexKnowledgeSourceParameters(searchIndexName: indexName)
-                    {
-                        SourceDataFields = { new SearchIndexFieldReference(name: "id"), new SearchIndexFieldReference(name: "page_chunk"), new SearchIndexFieldReference(name: "page_number") }
-                    }
-                );
-    
-                await indexClient.CreateOrUpdateKnowledgeSourceAsync(indexKnowledgeSource);
-                Console.WriteLine($"Knowledge source '{knowledgeSourceName}' created or updated successfully.");
-    
-                // Create a knowledge base
-                var openAiParameters = new AzureOpenAIVectorizerParameters
-                {
-                    ResourceUri = new Uri(aoaiEndpoint),
-                    DeploymentName = aoaiGptDeployment,
-                    ModelName = aoaiGptModel
-                };
-    
-                var model = new KnowledgeBaseAzureOpenAIModel(azureOpenAIParameters: openAiParameters);
-    
-                var knowledgeBase = new KnowledgeBase(
-                    name: knowledgeBaseName,
-                    knowledgeSources: new KnowledgeSourceReference[] { new KnowledgeSourceReference(knowledgeSourceName) }
-                )
-                {
-                    RetrievalReasoningEffort = new KnowledgeRetrievalLowReasoningEffort(),
-                    AnswerInstructions = "Provide a two sentence concise and informative answer based on the retrieved documents.",
-                    Models = { model }
-                };
-    
-                await indexClient.CreateOrUpdateKnowledgeBaseAsync(knowledgeBase);
-                Console.WriteLine($"Knowledge base '{knowledgeBaseName}' created or updated successfully.");
-    
-                // Set up messages
-                string instructions = @"A Q&A agent that can answer questions about the Earth at night.
-                If you don't have the answer, respond with ""I don't know"".";
-
-                var messages = new List<Dictionary<string, string>>
-                {
-                    new Dictionary<string, string>
-                    {
-                        { "role", "system" },
-                        { "content", instructions }
-                    }
-                };
-    
-                // Run agentic retrieval
-                var baseClient = new KnowledgeBaseRetrievalClient(
-                    endpoint: new Uri(searchEndpoint),
-                    knowledgeBaseName: knowledgeBaseName,
-                    tokenCredential: new DefaultAzureCredential()
-                );
-
-                string query = @"Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown? Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?";
-
-                messages.Add(new Dictionary<string, string>
-                {
-                    { "role", "user" },
-                    { "content", query }
-                });
-
-                Console.WriteLine($"Running the query...{query}");
-                var retrievalRequest = new KnowledgeBaseRetrievalRequest();
-                foreach (Dictionary<string, string> message in messages) {
-                    if (message["role"] != "system") {
-                        retrievalRequest.Messages.Add(new KnowledgeBaseMessage(content: new[] { new KnowledgeBaseMessageTextContent(message["content"]) }) { Role = message["role"] });
-                    }
-                }
-                retrievalRequest.RetrievalReasoningEffort = new KnowledgeRetrievalLowReasoningEffort();
-                var retrievalResult = await baseClient.RetrieveAsync(retrievalRequest);
-    
-                messages.Add(new Dictionary<string, string>
-                {
-                    { "role", "assistant" },
-                    { "content", (retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text }
-                });
-    
-                // Print the response, activity, and references
-                Console.WriteLine("Response:");
-                Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text);
-    
-                Console.WriteLine("Activity:");
-                foreach (var activity in retrievalResult.Value.Activity)
-                {
-                    Console.WriteLine($"Activity Type: {activity.GetType().Name}");
-                    string activityJson = JsonSerializer.Serialize(
-                        activity,
-                        activity.GetType(),
-                        new JsonSerializerOptions { WriteIndented = true }
-                    );
-                    Console.WriteLine(activityJson);
-                }
-    
-                Console.WriteLine("References:");
-                foreach (var reference in retrievalResult.Value.References)
-                {
-                    Console.WriteLine($"Reference Type: {reference.GetType().Name}");
-                    string referenceJson = JsonSerializer.Serialize(
-                        reference,
-                        reference.GetType(),
-                        new JsonSerializerOptions { WriteIndented = true }
-                    );
-                    Console.WriteLine(referenceJson);
-                }
-    
-                // Continue the conversation
-                string nextQuery = "How do I find lava at night?";
-                Console.WriteLine($"Continue the conversation with this query: {nextQuery}");
-                messages.Add(new Dictionary<string, string>
-                {
-                    { "role", "user" },
-                    { "content", nextQuery }
-                });
-    
-                retrievalRequest = new KnowledgeBaseRetrievalRequest();
-                foreach (Dictionary<string, string> message in messages) {
-                    if (message["role"] != "system") {
-                        retrievalRequest.Messages.Add(new KnowledgeBaseMessage(content: new[] { new KnowledgeBaseMessageTextContent(message["content"]) }) { Role = message["role"] });
-                    }
-                }
-                retrievalRequest.RetrievalReasoningEffort = new KnowledgeRetrievalLowReasoningEffort();
-                retrievalResult = await baseClient.RetrieveAsync(retrievalRequest);
-    
-                messages.Add(new Dictionary<string, string>
-                {
-                    { "role", "assistant" },
-                    { "content", (retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text }
-                });
-    
-                // Print the new response, activity, and references
-                Console.WriteLine("Response:");
-                Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text);
-    
-                Console.WriteLine("Activity:");
-                foreach (var activity in retrievalResult.Value.Activity)
-                {
-                    Console.WriteLine($"Activity Type: {activity.GetType().Name}");
-                    string activityJson = JsonSerializer.Serialize(
-                        activity,
-                        activity.GetType(),
-                        new JsonSerializerOptions { WriteIndented = true }
-                    );
-                    Console.WriteLine(activityJson);
-                }
-    
-                Console.WriteLine("References:");
-                foreach (var reference in retrievalResult.Value.References)
-                {
-                    Console.WriteLine($"Reference Type: {reference.GetType().Name}");
-                    string referenceJson = JsonSerializer.Serialize(
-                        reference,
-                        reference.GetType(),
-                        new JsonSerializerOptions { WriteIndented = true }
-                    );
-                    Console.WriteLine(referenceJson);
-                }
-    
-                // Clean up resources
-                await indexClient.DeleteKnowledgeBaseAsync(knowledgeBaseName);
-                Console.WriteLine($"Knowledge base '{knowledgeBaseName}' deleted successfully.");
-    
-                await indexClient.DeleteKnowledgeSourceAsync(knowledgeSourceName);
-                Console.WriteLine($"Knowledge source '{knowledgeSourceName}' deleted successfully.");
-    
-                await indexClient.DeleteIndexAsync(indexName);
-                Console.WriteLine($"Index '{indexName}' deleted successfully.");
-            }
-        }
-    }
-    ```
+## Run the code
 
-1. Build and run the application.
+Run the application to create an index, upload documents, configure a knowledge source and knowledge base, and run agentic retrieval queries.
 
-    ```console
-    dotnet run
-    ```
+```bash
+dotnet run --project AgenticRetrievalQuickstart.csproj
+```
 
 ### Output
 
@@ -404,91 +96,56 @@ Index 'earth-at-night' created or updated successfully.
 Documents uploaded to index 'earth-at-night' successfully.
 Knowledge source 'earth-knowledge-source' created or updated successfully.
 Knowledge base 'earth-knowledge-base' created or updated successfully.
+Running the query...Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown? Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?
 Response:
-Suburban belts show larger December brightening because holiday displays concentrate in suburbs and outskirts where there is more yard space and many single‑family homes [ref_id:5], while urban cores—already having higher absolute light levels—tend to show smaller relative increases (central areas typically brighten ~20–30%) [ref_id:8][ref_id:5]. Phoenix’s nighttime street grid is sharply visible because the metropolitan area is laid out on a regular, continuously lit grid with bright commercial and industrial nodes along major corridors like Grand Avenue [ref_id:0][ref_id:3], whereas long interstate stretches between Midwestern cities cross sparsely populated or rural regions with far fewer continuous roadside lights and so appear comparatively dim [ref_id:8].
+Suburban belts brighten more (in relative terms) in December because holiday lighting is concentrated in yards and single-family suburbs where extra decorative lights add a large percentage increase over baseline residential lighting, whereas dense urban cores already have high absolute light levels so the same added holiday lights produce a smaller relative change [ref_id:6][ref_id:2]. The documents note suburbs and outskirts show the biggest holiday increases and central urban areas show smaller percent increases (20-30% in cores, larger in suburbs) linked to available yard space and prevalence of single-family homes [ref_id:6][ref_id:2]. Phoenix's street grid appears very sharp from space because the city's regular, closely spaced north-south/east-west street lighting and bright nodes at intersections and commercial strips produce a strong, high-contrast patterned signal (grid and major corridors like Grand Avenue), while long Midwestern interstates are comparatively dim because roadway lighting is more sparse and continuous between cities and navigable rivers/long highways lack the dense, closely spaced light sources that produce visible nodes and grid patterns at night [ref_id:3][ref_id:7]. In addition, the Black Marble processing accounts for atmospheric, lunar, snow/seasonal and stray-light effects and isolates artificial emissions, so concentrated urban lighting (as in Phoenix) stands out more in the corrected radiance product than dispersed or spaced sources like isolated stretches of interstate or sparsely lit rivers and plains [ref_id:1][ref_id:4][ref_id:7].
 Activity:
 Activity Type: KnowledgeBaseModelQueryPlanningActivityRecord
 {
-  "InputTokens": 1350,
-  "OutputTokens": 1314,
+  "InputTokens": 1489,
+  "OutputTokens": 326,
   "Id": 0,
-  "ElapsedMs": 14162,
+  "ElapsedMs": 4558,
   "Error": null
 }
 Activity Type: KnowledgeBaseSearchIndexActivityRecord
 {
   "SearchIndexArguments": {
-    "Search": "Causes of December brightening in satellite nightlights: why suburban belts show larger relative December brightening than urban cores (roles of holiday residential lighting, snow albedo, urban heat island, commercial lighting patterns)",
+    "Search": "December brightening suburban belts vs urban cores light pollution causes seasonal variation \"December brightening\" satellite night lights",
     "Filter": null,
-    "SourceDataFields": [],
+    "SourceDataFields": [
+      {
+        "Name": "page_chunk"
+      },
+      {
+        "Name": "id"
+      },
+      {
+        "Name": "page_number"
+      }
+    ],
     "SearchFields": [],
-    "SemanticConfigurationName": null
+    "SemanticConfigurationName": "semantic_config"
   },
   "KnowledgeSourceName": "earth-knowledge-source",
-  "QueryTime": "2025-11-05T21:56:26.747+00:00",
-  "Count": 19,
+  "QueryTime": "2026-02-24T14:59:41.536+00:00",
+  "Count": 21,
   "Id": 1,
-  "ElapsedMs": 537,
-  "Error": null
-}
-Activity Type: KnowledgeBaseSearchIndexActivityRecord
-{
-  "SearchIndexArguments": {
-    "Search": "Why is Phoenix\u0019s nighttime street grid so sharply visible from space? (effects of streetlight density, luminaire type/aiming, spacing, urban grid layout, traffic vs roadway lighting)",
-    "Filter": null,
-    "SourceDataFields": [],
-    "SearchFields": [],
-    "SemanticConfigurationName": null
-  },
-  "KnowledgeSourceName": "earth-knowledge-source",
-  "QueryTime": "2025-11-05T21:56:27.182+00:00",
-  "Count": 7,
-  "Id": 2,
-  "ElapsedMs": 434,
+  "ElapsedMs": 623,
   "Error": null
 }
-Activity Type: KnowledgeBaseSearchIndexActivityRecord
-{
-  "SearchIndexArguments": {
-    "Search": "How do satellite nightlight sensor characteristics (VIIRS DNB, DMSP-OLS) \u2014 spatial resolution, dynamic range, saturation, blooming \u2014 affect observed brightness and structure of urban cores, suburbs, and long interstate stretches?",
-    "Filter": null,
-    "SourceDataFields": [],
-    "SearchFields": [],
-    "SemanticConfigurationName": null
-  },
-  "KnowledgeSourceName": "earth-knowledge-source",
-  "QueryTime": "2025-11-05T21:56:27.786+00:00",
-  "Count": 23,
-  "Id": 3,
-  "ElapsedMs": 604,
-  "Error": null
-}
-Activity Type: KnowledgeBaseAgenticReasoningActivityRecord
-{
-  "ReasoningTokens": 70232,
-  "RetrievalReasoningEffort": {},
-  "Id": 4,
-  "ElapsedMs": null,
-  "Error": null
-}
-Activity Type: KnowledgeBaseModelAnswerSynthesisActivityRecord
-{
-  "InputTokens": 7467,
-  "OutputTokens": 1710,
-  "Id": 5,
-  "ElapsedMs": 26663,
-  "Error": null
-}
-Results:
+... // Trimmed for brevity
+References:
 Reference Type: KnowledgeBaseSearchIndexReference
 {
-  "DocKey": "earth_at_night_508_page_104_verbalized",
+  "DocKey": "earth_at_night_508_page_105_verbalized",
   "Id": "0",
   "ActivitySource": 2,
   "SourceData": {},
-  "RerankerScore": 2.6344998
+  "RerankerScore": 2.7294974
 }
 ... // Trimmed for brevity
+Continue the conversation with this query: How do I find lava at night?
 Response:
 ... // Trimmed for brevity
 Activity:
@@ -502,6 +159,8 @@ Index 'earth-at-night' deleted successfully.
 
 ## Understand the code
 
+[!INCLUDE [understand code note](../understand-code-note.md)]
+
 Now that you've run the code, let's break down the key steps:
 
 1. [Create a search index](#create-a-search-index)
@@ -734,7 +393,7 @@ var retrievalResult = await baseClient.RetrieveAsync(retrievalRequest);
 messages.Add(new Dictionary<string, string>
 {
     { "role", "assistant" },
-    { "content", (retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent).Text }
+    { "content", (retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text }
 });
 ```
 
@@ -753,7 +412,7 @@ The following code displays the response, activity, and references from the retr
 ```csharp
 // Print the response, activity, and references
 Console.WriteLine("Response:");
-Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent).Text);
+Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text);
 
 Console.WriteLine("Activity:");
 foreach (var activity in retrievalResult.Value.Activity)
@@ -804,7 +463,7 @@ retrievalResult = await baseClient.RetrieveAsync(retrievalRequest);
 messages.Add(new Dictionary<string, string>
 {
     { "role", "assistant" },
-    { "content", (retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent).Text }
+    { "content", (retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text }
 });
 ```
 
@@ -815,7 +474,7 @@ The following code displays the new response, activity, and references from the
 ```csharp
 // Print the new response, activity, and references
 Console.WriteLine("Response:");
-Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent).Text);
+Console.WriteLine((retrievalResult.Value.Response[0].Content[0] as KnowledgeBaseMessageTextContent)!.Text);
 
 Console.WriteLine("Activity:");
 foreach (var activity in retrievalResult.Value.Activity)
@@ -846,7 +505,7 @@ foreach (var reference in retrievalResult.Value.References)
 
 [!INCLUDE [clean up resources (paid)](../resource-cleanup-paid.md)]
 
-Otherwise, the following code from `Program.cs` deleted the objects you created in this quickstart.
+Otherwise, the following code from `program.cs` deleted the objects you created in this quickstart.
 
 ### Delete the knowledge base
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エージェント的検索C#クイックスタートの大幅な更新"
}
```

### Explanation
このコードの変更は、Azureのエージェント的検索に関するC#クイックスタートガイドの大幅な更新を示しています。主な変更点は、古いコードと内容を整理し、新しい機能や手順を追加してわかりやすくすることです。具体的には、日付が2026年1月14日から2026年2月23日に更新され、サンプルデータやリソースの説明が明確化されています。

新しい手順では、必要な環境やリソースの作成に関する詳しい情報が整理され、また、C#コードの一部を削除し、新しいアプローチを反映させています。具体的には、エンベディングモデルや大規模言語モデルに関する情報が加わり、これによりユーザーが新機能を利用しやすくなりました。また、手順は番号付きリストへと整理されたため、状況に応じた情報の見つけやすさが向上しています。

さらに、以前のバージョンに比べて大量のコードが削除されており、全体としてより簡潔で使用しやすい形に改良されています。データの取得やインデックス作成方法についても新しい方針が適用され、新たな情報が統合されたことで、エージェント的検索の利用がよりスムーズになることが期待されます。

## articles/search/includes/quickstarts/agentic-retrieval-java.md{#item-4e2c55}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エージェント的検索Javaクイックスタートの大幅な更新"
}
```

### Explanation
このコードの変更は、Azureにおけるエージェント的検索のJavaクイックスタートガイドに対する大規模な更新を反映しています。変更の内容には、大きなボリュームの削除と追加が見られ、全体で特に凡庸な記述が大幅に削減されています。これにより、ユーザーが必要とする情報にすぐにアクセスできるよう、クイックスタートガイドの明確さと効率が向上しています。

主な変更点としては、具体的なコードサンプルの更新、関連する手順の整理、そして最新の機能に対応するための情報追加が含まれています。この改訂により、ユーザーはエージェント的検索の設定や使用にあたって、もはや古い記述に頼る必要がなくなり、より合理的に開発を進められるようになります。

結果的に、この更新は、Java開発者がAzureのエージェント的検索機能を迅速に取り入れ、効果的なアプリケーションを構築できることを目指したものです。全体として、ユーザーエクスペリエンスの向上が期待される内容になっています。

## articles/search/includes/quickstarts/agentic-retrieval-javascript.md{#item-715283}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 01/14/2026
+ms.date: 02/23/2026
 ms.custom: dev-focus
 ai-usage: ai-assisted
 ---
@@ -15,7 +15,10 @@ In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview
 
 A *knowledge base* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the knowledge base outputs raw content from your sources, but this quickstart uses the answer synthesis output mode for natural-language answer generation.
 
-Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
+Although you can use your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book.
+
+> [!TIP]
+> Source code for the JavaScript version of this quickstart isn't available. You can copy code directly from this article.
 
 ## Prerequisites
 
@@ -25,62 +28,60 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
-+ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
++ An embedding model [deployed to your project](/azure/ai-foundry/how-to/deploy-models-openai) for text-to-vector conversion. You can use any `text-embedding` model, such as `text-embedding-3-large`.
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) and the latest LTS version of [Node.js](https://nodejs.org/en/download/).
++ An LLM [deployed to your project](/azure/ai-foundry/how-to/deploy-models-openai) for query planning and answer generation. You can use any [supported LLM](../../agentic-retrieval-how-to-create-knowledge-base.md#supported-models), such as `gpt-5-mini`.
 
-[!INCLUDE [Setup](./agentic-retrieval-setup.md)]
++ [Node.js 20 LTS](https://nodejs.org/en/download/) or later.
 
-## Set up the environment
++ [Visual Studio Code](https://code.visualstudio.com/download).
+
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-To set up the console application for this quickstart:
+[!INCLUDE [agentic retrieval setup](agentic-retrieval-setup.md)]
+
+## Set up the environment
 
 1. Create a folder named `quickstart-agentic-retrieval` to contain the application.
 
 1. Open the folder in Visual Studio Code.
 
-1. Select **Terminal** > **New Terminal**, and then run the following commands to initialize the `package.json` file.
+1. Select **Terminal** > **New Terminal**, and then run the following commands to initialize `package.json`.
 
-    ```console
+    ```bash
     npm init -y
     npm pkg set type=module
     ```
 
 1. Install the [Azure AI Search client library for JavaScript](/javascript/api/overview/azure/search-documents-readme).
 
-    ```console
+    ```bash
     npm install @azure/search-documents@12.3.0-beta.1
     ```
 
 1. For keyless authentication with Microsoft Entra ID, install the [Azure Identity client library for JavaScript](/javascript/api/overview/azure/identity-readme).
 
-    ```console
+    ```bash
     npm install @azure/identity
     ```
 
-1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Microsoft Foundry project.
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search and Microsoft Foundry resources.
 
-    ```console
+    ```bash
     az login
     ```
 
 ## Run the code
 
-To create and run the agentic retrieval pipeline:
-
-1. Create a file named `.env` in the `quickstart-agentic-retrieval` folder.
-
-1. Paste the following environment variables into the `.env` file.
+1. Create a file named `.env` in the `quickstart-agentic-retrieval` folder, and then paste the following content. Replace the placeholder values with the URLs you obtained in [Get endpoints](#get-endpoints).
 
     ```
     AZURE_SEARCH_ENDPOINT = https://<your-search-service-name>.search.windows.net
-    AZURE_OPENAI_ENDPOINT = https://<your-ai-foundry-resource-name>.openai.azure.com/
+    AZURE_OPENAI_ENDPOINT = https://<your-foundry-resource-name>.openai.azure.com/
     AZURE_OPENAI_GPT_DEPLOYMENT = gpt-5-mini
     AZURE_OPENAI_EMBEDDING_DEPLOYMENT = text-embedding-3-large
     ```
 
-1. Set `AZURE_SEARCH_ENDPOINT` and `AZURE_OPENAI_ENDPOINT` to the values you obtained in [Get endpoints](#get-endpoints).
-
 1. Create a file named `index.js`, and then paste the following code into the file.
 
     ```javascript
@@ -401,15 +402,15 @@ To create and run the agentic retrieval pipeline:
 
 1. Build and run the application.
 
-    ```console
+    ```bash
     node --env-file=.env index.js
     ```
 
 ### Output
 
 The output of the application should be similar to the following:
 
-```console
+```output
 Waiting for indexing to complete...
 Expected documents: 194
 Current indexed count: 194
@@ -457,58 +458,7 @@ Activity Type: searchIndex
     "semanticConfigurationName": "semantic_config"
   }
 }
-Activity Type: searchIndex
-{
-  "id": 2,
-  "type": "searchIndex",
-  "elapsedMs": 538,
-  "knowledgeSourceName": "earth-knowledge-source",
-  "queryTime": "2025-12-19T15:38:24.001Z",
-  "count": 0,
-  "searchIndexArguments": {
-    "search": "factors that make Phoenix nighttime street grid highly visible from space reasons highway/interstate lighting visibility differences Midwestern interstates dim",
-    "filter": null,
-    "sourceDataFields": [
-      {
-        "name": "page_chunk"
-      },
-      {
-        "name": "id"
-      },
-      {
-        "name": "page_number"
-      }
-    ],
-    "searchFields": [],
-    "semanticConfigurationName": "semantic_config"
-  }
-}
-Activity Type: searchIndex
-{
-  "id": 3,
-  "type": "searchIndex",
-  "elapsedMs": 465,
-  "knowledgeSourceName": "earth-knowledge-source",
-  "queryTime": "2025-12-19T15:38:24.467Z",
-  "count": 2,
-  "searchIndexArguments": {
-    "search": "satellite nighttime lights seasonal variations suburban brightening studies December holiday lighting residential vs commercial lighting patterns",
-    "filter": null,
-    "sourceDataFields": [
-      {
-        "name": "page_chunk"
-      },
-      {
-        "name": "id"
-      },
-      {
-        "name": "page_number"
-      }
-    ],
-    "searchFields": [],
-    "semanticConfigurationName": "semantic_config"
-  }
-}
+... // Trimmed for brevity
 Activity Type: agenticReasoning
 {
   "id": 4,
@@ -570,7 +520,7 @@ Now that you have the code, let's break down the key components:
 1. [Create a knowledge source](#create-a-knowledge-source)
 1. [Create a knowledge base](#create-a-knowledge-base)
 1. [Run the retrieval pipeline](#run-the-retrieval-pipeline)
-1. [Review the response, activity, and references](#review-the-response-activity-and-results)
+1. [Review the response, activity, and references](#review-the-response-activity-and-references)
 1. [Continue the conversation](#continue-the-conversation)
 
 ### Create a search index
@@ -580,7 +530,7 @@ In Azure AI Search, an index is a structured collection of data. The following c
 The index schema contains fields for document identification and page content, embeddings, and numbers. The schema also includes configurations for semantic ranking and vector search, which uses your `text-embedding-3-large` deployment to vectorize text and match documents based on semantic similarity.
 
 ```javascript
-const index: SearchIndex = {
+const index = {
     name: 'earth_at_night',
     fields: [
         {
@@ -590,15 +540,15 @@ const index: SearchIndex = {
             filterable: true,
             sortable: true,
             facetable: true
-        } as SearchField,
+        },
         {
             name: "page_chunk",
             type: "Edm.String",
             searchable: true,
             filterable: false,
             sortable: false,
             facetable: false
-        } as SearchField,
+        },
         {
             name: "page_embedding_text_3_large",
             type: "Collection(Edm.Single)",
@@ -608,54 +558,54 @@ const index: SearchIndex = {
             facetable: false,
             vectorSearchDimensions: 3072,
             vectorSearchProfileName: "hnsw_text_3_large"
-        } as SearchField,
+        },
         {
             name: "page_number",
             type: "Edm.Int32",
             filterable: true,
             sortable: true,
             facetable: true
-        } as SearchField
+        }
     ],
     vectorSearch: {
         profiles: [
             {
                 name: "hnsw_text_3_large",
                 algorithmConfigurationName: "alg",
                 vectorizerName: "azure_openai_text_3_large"
-            } as VectorSearchProfile
+            }
         ],
         algorithms: [
             {
                 name: "alg",
                 kind: "hnsw"
-            } as HnswAlgorithmConfiguration
+            }
         ],
         vectorizers: [
             {
                 vectorizerName: "azure_openai_text_3_large",
                 kind: "azureOpenAI",
                 parameters: {
-                    resourceUrl: process.env.AZURE_OPENAI_ENDPOINT!,
-                    deploymentId: process.env.AZURE_OPENAI_EMBEDDING_DEPLOYMENT!,
-                    modelName: process.env.AZURE_OPENAI_EMBEDDING_DEPLOYMENT!
-                } as AzureOpenAIParameters
-            } as AzureOpenAIVectorizer
+                    resourceUrl: process.env.AZURE_OPENAI_ENDPOINT,
+                    deploymentId: process.env.AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
+                    modelName: process.env.AZURE_OPENAI_EMBEDDING_DEPLOYMENT
+                }
+            }
         ]
-    } as VectorSearch,
+    },
     semanticSearch: {
         defaultConfigurationName: "semantic_config",
         configurations: [
             {
                 name: "semantic_config",
                 prioritizedFields: {
                     contentFields: [
-                        { name: "page_chunk" } as SemanticField
+                        { name: "page_chunk" }
                     ]
-                } as SemanticPrioritizedFields
-            } as SemanticConfiguration
+                }
+            }
         ]
-    } as SemanticSearch
+    }
 };
 
 const credential = new DefaultAzureCredential();
@@ -714,7 +664,7 @@ console.log(`✓ All ${documents.length} documents indexed successfully!`);
 
 A knowledge source is a reusable reference to source data. The following code defines a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
 
-`source_data_fields` specifies which index fields are included in citation references. This example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+`sourceDataFields` specifies which index fields are included in citation references. This example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
 
 ```javascript
 await searchIndexClient.createKnowledgeSource({
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的検索JavaScriptクイックスタートの更新"
}
```

### Explanation
このコードの変更は、Azureにおけるエージェント的検索に関するJavaScriptクイックスタートガイドの小規模な更新を反映しています。主な変更は、全体での文書の整理と新しい情報の追加にあります。具体的には、いくつかの手順がより明確に定義され、新たな依存関係が追加されることで、ユーザーがエージェント的検索機能をより効果的に利用できるようになっています。

変更の中では、サンプルデータの使用方法や設定前提条件の説明が簡潔になり、ユーザーが自分のデータを使用することの重要性も強調されています。また、サンプルコードに直接アクセスできることを明示するヒントが追加されており、手順もよりシンプルな形に整理されています。

加えて、Node.jsやAzure CLIの設定に関する最新情報が反映されており、これにより新しい技術スタックに対応する形になっています。全体として、分かりやすさと使いやすさが改善され、ユーザーが迅速にエージェント的検索を実装できることを目指した内容になっています。

## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 01/14/2026
+ms.date: 02/23/2026
 ms.custom: dev-focus
 ai-usage: ai-assisted
 ---
@@ -15,10 +15,10 @@ In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview
 
 A *knowledge base* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the knowledge base outputs raw content from your sources, but this quickstart uses the answer synthesis output mode for natural-language answer generation.
 
-Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
+Although you can use your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book.
 
 > [!TIP]
-> Want to get started right away? See the [azure-search-python-samples](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval) GitHub repository.
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval) on GitHub.
 
 ## Prerequisites
 
@@ -28,327 +28,64 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
-+ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
++ An embedding model [deployed to your project](/azure/ai-foundry/how-to/deploy-models-openai) for text-to-vector conversion. You can use any `text-embedding` model, such as `text-embedding-3-large`.
 
-+ The latest version of [Python](https://www.python.org/downloads/).
++ An LLM [deployed to your project](/azure/ai-foundry/how-to/deploy-models-openai) for query planning and answer generation. You can use any [supported LLM](../../agentic-retrieval-how-to-create-knowledge-base.md#supported-models), such as `gpt-5-mini`.
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
++ [Python 3.8](https://www.python.org/downloads/) or later.
 
-[!INCLUDE [Setup](./agentic-retrieval-setup.md)]
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions.
 
-## Connect from your local system
++ [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-You configured role-based access to interact with Azure AI Search and Azure OpenAI in Foundry Models. Use the Azure CLI to sign in to the same subscription and tenant for both resources. For more information, see [Quickstart: Connect without keys](../../search-get-started-rbac.md).
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-To connect from your local system:
+[!INCLUDE [agentic retrieval setup](agentic-retrieval-setup.md)]
 
-1. Create a folder named `quickstart-agentic-retrieval`.
+## Set up the environment
 
-1. Open the folder in Visual Studio Code.
+1. Use Git to clone the sample repository.
 
-1. Select **Terminal** > **New Terminal**.
+    ```bash
+    git clone https://github.com/Azure-Samples/azure-search-python-samples
+    ```
 
-1. Run the following command to sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Foundry project.
+1. Navigate to the quickstart folder and open it in Visual Studio Code.
 
-    ```azurecli
-    az login
+    ```bash
+    cd azure-search-python-samples/Quickstart-Agentic-Retrieval
+    code .
     ```
 
-## Run the code
-
-To create and run the agentic retrieval pipeline:
+1. In `sample.env`, replace the placeholder values for `SEARCH_ENDPOINT` and `AOAI_ENDPOINT` with the URLs you obtained in [Get endpoints](#get-endpoints).
 
-1. Run the following command to install the required packages.
+1. Rename `sample.env` to `.env`.
 
-    ```console
-    pip install azure-identity requests azure-search-documents --pre
+    ```bash
+    mv sample.env .env
     ```
 
-1. Create a file named `agentic-retrieval.py` in the `quickstart-agentic-retrieval` folder.
+1. Open `quickstart-agentic-retrieval.ipynb`.
 
-1. Paste the following code into the file.
+1. Press **Ctrl+Shift+P**, select **Notebook: Select Notebook Kernel**, and follow the prompts to create a virtual environment. Select **requirements.txt** for the dependencies.
 
-    ```python
-    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
-    from azure.search.documents.indexes.models import SearchIndex, SearchField, VectorSearch, VectorSearchProfile, HnswAlgorithmConfiguration, AzureOpenAIVectorizer, AzureOpenAIVectorizerParameters, SemanticSearch, SemanticConfiguration, SemanticPrioritizedFields, SemanticField, SearchIndexKnowledgeSource, SearchIndexKnowledgeSourceParameters, SearchIndexFieldReference, KnowledgeBase, KnowledgeBaseAzureOpenAIModel, KnowledgeSourceReference, KnowledgeRetrievalOutputMode, KnowledgeRetrievalLowReasoningEffort
-    from azure.search.documents.indexes import SearchIndexClient
-    from azure.search.documents import SearchIndexingBufferedSender
-    from azure.search.documents.knowledgebases import KnowledgeBaseRetrievalClient
-    from azure.search.documents.knowledgebases.models import KnowledgeBaseRetrievalRequest, KnowledgeBaseMessage, KnowledgeBaseMessageTextContent, SearchIndexKnowledgeSourceParams
-    import requests
-    import json
-    
-    # Define variables
-    search_endpoint = "PUT-YOUR-SEARCH-SERVICE-URL-HERE"
-    aoai_endpoint = "PUT-YOUR-AOAI-FOUNDRY-URL-HERE"
-    aoai_embedding_model = "text-embedding-3-large"
-    aoai_embedding_deployment = "text-embedding-3-large"
-    aoai_gpt_model = "gpt-5-mini"
-    aoai_gpt_deployment = "gpt-5-mini"
-    index_name = "earth-at-night"
-    knowledge_source_name = "earth-knowledge-source"
-    knowledge_base_name = "earth-knowledge-base"
-    search_api_version = "2025-11-01-preview"
-    
-    credential = DefaultAzureCredential()
-    token_provider = get_bearer_token_provider(credential, "https://search.azure.com/.default")
-    
-    # Create an index
-    azure_openai_token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")
-
-    index = SearchIndex(
-        name=index_name,
-        fields=[
-            SearchField(name="id", type="Edm.String", key=True, filterable=True, sortable=True, facetable=True),
-            SearchField(name="page_chunk", type="Edm.String", filterable=False, sortable=False, facetable=False),
-            SearchField(name="page_embedding_text_3_large", type="Collection(Edm.Single)", stored=False, vector_search_dimensions=3072, vector_search_profile_name="hnsw_text_3_large"),
-            SearchField(name="page_number", type="Edm.Int32", filterable=True, sortable=True, facetable=True)
-        ],
-        vector_search=VectorSearch(
-            profiles=[VectorSearchProfile(name="hnsw_text_3_large", algorithm_configuration_name="alg", vectorizer_name="azure_openai_text_3_large")],
-            algorithms=[HnswAlgorithmConfiguration(name="alg")],
-            vectorizers=[
-                AzureOpenAIVectorizer(
-                    vectorizer_name="azure_openai_text_3_large",
-                    parameters=AzureOpenAIVectorizerParameters(
-                        resource_url=aoai_endpoint,
-                        deployment_name=aoai_embedding_deployment,
-                        model_name=aoai_embedding_model
-                    )
-                )
-            ]
-        ),
-        semantic_search=SemanticSearch(
-            default_configuration_name="semantic_config",
-            configurations=[
-                SemanticConfiguration(
-                    name="semantic_config",
-                    prioritized_fields=SemanticPrioritizedFields(
-                        content_fields=[
-                            SemanticField(field_name="page_chunk")
-                        ]
-                    )
-                )
-            ]
-        )
-    )
-    
-    index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
-    index_client.create_or_update_index(index)
-    print(f"Index '{index_name}' created or updated successfully.")
-    
-    # Upload documents
-    url = "https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json"
-    documents = requests.get(url).json()
-    
-    with SearchIndexingBufferedSender(endpoint=search_endpoint, index_name=index_name, credential=credential) as client:
-        client.upload_documents(documents=documents)
-    
-    print(f"Documents uploaded to index '{index_name}' successfully.")
-    
-    # Create a knowledge source
-    ks = SearchIndexKnowledgeSource(
-        name=knowledge_source_name,
-        description="Knowledge source for Earth at night data",
-        search_index_parameters=SearchIndexKnowledgeSourceParameters(
-            search_index_name=index_name,
-            source_data_fields=[SearchIndexFieldReference(name="id"), SearchIndexFieldReference(name="page_number")]
-        ),
-    )
-    
-    index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
-    index_client.create_or_update_knowledge_source(knowledge_source=ks)
-    print(f"Knowledge source '{knowledge_source_name}' created or updated successfully.")
-    
-    # Create a knowledge base
-    aoai_params = AzureOpenAIVectorizerParameters(
-        resource_url=aoai_endpoint,
-        deployment_name=aoai_gpt_deployment,
-        model_name=aoai_gpt_model,
-    )
-    
-    knowledge_base = KnowledgeBase(
-        name=knowledge_base_name,
-        models=[KnowledgeBaseAzureOpenAIModel(azure_open_ai_parameters=aoai_params)],
-        knowledge_sources=[
-            KnowledgeSourceReference(
-                name=knowledge_source_name
-            )
-        ],
-        output_mode=KnowledgeRetrievalOutputMode.ANSWER_SYNTHESIS,
-        answer_instructions="Provide a two sentence concise and informative answer based on the retrieved documents."
-    )
-    
-    index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
-    index_client.create_or_update_knowledge_base(knowledge_base)
-    print(f"Knowledge base '{knowledge_base_name}' created or updated successfully.")
-    
-    # Set up messages
-    instructions = """
-    A Q&A agent that can answer questions about the Earth at night.
-    If you don't have the answer, respond with "I don't know".
-    """
-    
-    messages = [
-        {
-            "role": "system",
-            "content": instructions
-        }
-    ]
-    
-    # Run agentic retrieval
-    agent_client = KnowledgeBaseRetrievalClient(endpoint=search_endpoint, knowledge_base_name=knowledge_base_name, credential=credential)
-    query_1 = """
-        Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown?
-        Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?
-        """
-    
-    messages.append({
-        "role": "user",
-        "content": query_1
-    })
-    
-    req = KnowledgeBaseRetrievalRequest(
-        messages=[
-            KnowledgeBaseMessage(
-                role=m["role"],
-                content=[KnowledgeBaseMessageTextContent(text=m["content"])]
-            ) for m in messages if m["role"] != "system"
-        ],
-        knowledge_source_params=[
-            SearchIndexKnowledgeSourceParams(
-                knowledge_source_name=knowledge_source_name,
-                include_references=True,
-                include_reference_source_data=True,
-                always_query_source=True
-            )
-        ],
-        include_activity=True,
-        retrieval_reasoning_effort=KnowledgeRetrievalLowReasoningEffort
-    )
-    
-    result = agent_client.retrieve(retrieval_request=req)
-    print(f"Retrieved content from '{knowledge_base_name}' successfully.")
-    
-    # Display the response, activity, and references
-    response_contents = []
-    activity_contents = []
-    references_contents = []
-    
-    response_parts = []
-    for resp in result.response:
-        for content in resp.content:
-            response_parts.append(content.text)
-    response_content = "\n\n".join(response_parts) if response_parts else "No response found on 'result'"
-    
-    response_contents.append(response_content)
-    
-    # Print the three string values
-    print("response_content:\n", response_content, "\n")
+   When complete, you should see a `.venv` folder in the project directory.
 
-    messages.append({
-        "role": "assistant",
-        "content": response_content
-    })
-    
-    if result.activity:
-        activity_content = json.dumps([a.as_dict() for a in result.activity], indent=2)
-    else:
-        activity_content = "No activity found on 'result'"
-        
-    activity_contents.append(activity_content)
-    print("activity_content:\n", activity_content, "\n")
-    
-    if result.references:
-        references_content = json.dumps([r.as_dict() for r in result.references], indent=2)
-    else:
-        references_content = "No references found on 'result'"
-        
-    references_contents.append(references_content)
-    print("references_content:\n", references_content)
-    
-    # Continue the conversation
-    query_2 = "How do I find lava at night?"
-    messages.append({
-        "role": "user",
-        "content": query_2
-    })
-    
-    req = KnowledgeBaseRetrievalRequest(
-        messages=[
-            KnowledgeBaseMessage(
-                role=m["role"],
-                content=[KnowledgeBaseMessageTextContent(text=m["content"])]
-            ) for m in messages if m["role"] != "system"
-        ],
-        knowledge_source_params=[
-            SearchIndexKnowledgeSourceParams(
-                knowledge_source_name=knowledge_source_name,
-                include_references=True,
-                include_reference_source_data=True,
-                always_query_source=True
-            )
-        ],
-        include_activity=True,
-        retrieval_reasoning_effort=KnowledgeRetrievalLowReasoningEffort
-    )
-    
-    result = agent_client.retrieve(retrieval_request=req)
-    print(f"Retrieved content from '{knowledge_base_name}' successfully.")
-    
-    # Display the new retrieval response, activity, and references
-    response_parts = []
-    for resp in result.response:
-        for content in resp.content:
-            response_parts.append(content.text)
-    response_content = "\n\n".join(response_parts) if response_parts else "No response found on 'result'"
-    
-    response_contents.append(response_content)
-    
-    # Print the three string values
-    print("response_content:\n", response_content, "\n")
-    
-    if result.activity:
-        activity_content = json.dumps([a.as_dict() for a in result.activity], indent=2)
-    else:
-        activity_content = "No activity found on 'result'"
-        
-    activity_contents.append(activity_content)
-    print("activity_content:\n", activity_content, "\n")
-    
-    if result.references:
-        references_content = json.dumps([r.as_dict() for r in result.references], indent=2)
-    else:
-        references_content = "No references found on 'result'"
-        
-    references_contents.append(references_content)
-    print("references_content:\n", references_content)
-    
-    # Clean up resources
-    index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
-    index_client.delete_knowledge_base(knowledge_base_name)
-    print(f"Knowledge base '{knowledge_base_name}' deleted successfully.")
-    
-    index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
-    index_client.delete_knowledge_source(knowledge_source=knowledge_source_name)
-    print(f"Knowledge source '{knowledge_source_name}' deleted successfully.")
-    
-    index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
-    index_client.delete_index(index_name)
-    print(f"Index '{index_name}' deleted successfully.")
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search and Microsoft Foundry resources.
+
+    ```azurecli
+    az login
     ```
 
-1. Set `search_endpoint` and `aoai_endpoint` to the values you obtained in [Get endpoints](#get-endpoints).
+## Run the code
 
-1. Run the following command to execute the code.
+1. Run the `Load connections` cell to install the required packages and load environment variables.
 
-    ```console
-    python agentic-retrieval.py
-    ```
+1. Run the remaining cells sequentially to create an index, upload documents, configure a knowledge source and knowledge base, and run agentic retrieval queries.
 
 ### Output
 
-The output of the code should look similar to the following:
+Each code cell prints its output to the notebook. The following example is the output after running all cells:
 
 ```
 Documents uploaded to index 'earth-at-night' successfully.
@@ -379,28 +116,7 @@ activity_content:
       "search": "December brightening in satellite nighttime lights: why do suburban belts show larger relative increases in December than urban cores despite higher absolute downtown light levels?"
     }
   },
-  {
-    "id": 2,
-    "type": "searchIndex",
-    "elapsed_ms": 632,
-    "knowledge_source_name": "earth-knowledge-source",
-    "query_time": "2025-11-05T16:17:48.985Z",
-    "count": 10,
-    "search_index_arguments": {
-      "search": "Why is Phoenix's nighttime street grid so sharply visible from space? factors: street-light layout, lamp type, urban form, light scattering, and satellite sensor characteristics in Phoenix, Arizona."
-    }
-  },
-  {
-    "id": 3,
-    "type": "searchIndex",
-    "elapsed_ms": 420,
-    "knowledge_source_name": "earth-knowledge-source",
-    "query_time": "2025-11-05T16:17:49.406Z",
-    "count": 11,
-    "search_index_arguments": {
-      "search": "Why are long stretches of interstate highways between Midwestern cities comparatively dim in satellite nighttime images? factors: highway lighting design, lamp spacing and type, vehicle headlights vs fixed lighting, and detection limits of nighttime sensors"
-    }
-  },
+  ... // Trimmed for brevity
   {
     "id": 4,
     "type": "agenticReasoning",
@@ -454,6 +170,8 @@ Index 'earth-at-night' deleted successfully.
 
 ## Understand the code
 
+[!INCLUDE [understand code note](../understand-code-note.md)]
+
 Now that you've run the code, let's break down the key steps:
 
 1. [Create a search index](#create-a-search-index)
@@ -582,7 +300,7 @@ knowledge_base = KnowledgeBase(
         )
     ],
     output_mode=KnowledgeRetrievalOutputMode.ANSWER_SYNTHESIS,
-    answer_instructions="Provide a two sentence concise and informative answer based on the retrieved documents."
+    answer_instructions="Provide a 2 sentence concise and informative answer based on the retrieved documents."
 )
 
 index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
@@ -783,7 +501,7 @@ print("references_content:\n", references_content)
 
 [!INCLUDE [clean up resources (paid)](../resource-cleanup-paid.md)]
 
-Otherwise, the following code from `agentic-retrieval.py` deleted the objects you created in this quickstart.
+Otherwise, the following code from `quickstart-agentic-retrieval.ipynb` deleted the objects you created in this quickstart.
 
 ### Delete the knowledge base
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エージェント的検索Pythonクイックスタートの大幅な更新"
}
```

### Explanation
この変更は、Azureにおけるエージェント的検索のPythonクイックスタートガイドに対する大規模な更新を含んでいます。主な変更点は、コンテンツの整理と最新の情報への適応が行われたことです。与えられたコードの変更には、使用される依存関係のアップデートや手順の簡素化が含まれています。

具体的には、古い部分が削除され、新しい情報が追加されることで、ユーザーが手続きに従いやすくなっています。また、環境設定や試用方法が具体的に明示され、よりスムーズに始められるように改善されています。特に、既存コードの重複が削除され、重要な情報に焦点が当てられるように合理化されました。

変更に伴い、インデックス作成、データのアップロード、知識源と知識ベースの設定、トラブルシューティングの手順が見直され、全体のストリームライン化が図られています。これにより、ユーザーは新しいモデルや仕組みを利用する際に、最新の情報に基づいて効果的に作業ができることを目指しています。

結論として、この更新は、Python開発者がAzureのエージェント的検索機能を迅速に習得し、エラーなく使用開始できることを目指した内容となっています。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エージェント的検索RESTクイックスタートの大幅な改訂"
}
```

### Explanation
この変更は、Azureにおけるエージェント的検索のREST APIクイックスタートガイドに対する大規模な改訂を示しています。主な改訂の内容は、コンテンツの削減と新しい情報の追加を通じて、ガイドの明確さおよび実用性を高めることに焦点を当てています。

具体的には、多くの冗長な部分が削除される一方で、新たな手順や推奨されるベストプラクティスが盛り込まれています。この変更により、ユーザーは必要な情報を迅速に見つけやすくなり、エージェント的検索機能を効果的に活用できるようになります。加えて、本ガイドでは、API呼び出しやレスポンス処理に関する詳細な説明が強調され、実装面での指針が提供されています。

更新内容は、開発者が容易に理解し、フォローできる構成となっており、新しいREST APIの使用方法への移行を支援する内容となっています。この結果、エンドユーザーは最新の機能に基づく改善された体験を享受できるようになっています。全体として、これらの変更は、ユーザーがエージェント的検索システムの導入を円滑に行うための重要なステップです。

## articles/search/includes/quickstarts/agentic-retrieval-setup.md{#item-e5e297}

<details>
<summary>Diff</summary>
````diff
@@ -4,42 +4,26 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 12/22/2025
+ms.date: 02/23/2026
 ---
 
 ## Configure access
 
-Before you begin, make sure you have permissions to access content and operations. We recommend Microsoft Entra ID for authentication and role-based access for authorization. You must be an **Owner** or **User Access Administrator** to assign roles. If roles aren't feasible, use [key-based authentication](../../search-security-api-keys.md) instead.
+Before you begin, make sure you have permissions to access content and operations. This quickstart uses Microsoft Entra ID for authentication and role-based access for authorization. You must be an **Owner** or **User Access Administrator** to assign roles. If roles aren't feasible, use [key-based authentication](../../search-security-api-keys.md) instead.
 
-To configure access for this quickstart, select both of the following tabs.
+To configure access for this quickstart:
 
-### [Azure AI Search](#tab/search)
+1. Sign in to the [Azure portal](https://portal.azure.com).
 
-Azure AI Search provides the agentic retrieval pipeline. Configure access for yourself and your search service to read and write data, interact with Foundry, and run the pipeline.
+1. On your Azure AI Search service:
 
-On your Azure AI Search service:
+    1. [Enable role-based access](../../search-security-enable-roles.md).
 
-1. [Enable role-based access](../../search-security-enable-roles.md).
+    1. [Create a system-assigned managed identity](../../search-how-to-managed-identities.md#create-a-system-managed-identity).
 
-1. [Create a system-assigned managed identity](../../search-how-to-managed-identities.md#create-a-system-managed-identity).
+    1. [Assign the following roles](../../search-security-rbac.md) to your user account: **Search Service Contributor**, **Search Index Data Contributor**, and **Search Index Data Reader**.
 
-1. [Assign the following roles](../../search-security-rbac.md) to yourself.
-
-    + **Search Service Contributor**
-
-    + **Search Index Data Contributor**
-
-    + **Search Index Data Reader**
-
-### [Microsoft Foundry](#tab/foundry)
-
-Microsoft Foundry provides the Azure OpenAI models used for embeddings, query planning, and answer generation. Grant your search service permission to use these models.
-
-On your Microsoft Foundry resource:
-
-+ Assign **Cognitive Services User** to the managed identity of your search service.
-
----
+1. On your Microsoft Foundry resource, assign **Cognitive Services User** to the managed identity of your search service.
 
 > [!IMPORTANT]
 > Agentic retrieval has two token-based billing models:
@@ -53,34 +37,18 @@ On your Microsoft Foundry resource:
 
 Each Azure AI Search service and Microsoft Foundry resource has an *endpoint*, which is a unique URL that identifies and provides network access to the resource. In a later section, you specify these endpoints to connect to your resources programmatically.
 
-To get the endpoints for this quickstart, select both of the following tabs.
-
-### [Azure AI Search](#tab/search)
+To get the endpoints for this quickstart:
 
-1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
-
-1. From the left pane, select **Overview**.
-
-1. Make a note of the endpoint, which should look like `https://my-service.search.windows.net`.
-
-### [Microsoft Foundry](#tab/foundry)
-
-1. Sign in to the [Azure portal](https://portal.azure.com/) and select your Microsoft Foundry resource.
-
-1. From the left pane, select **Resource Management** > **Keys and Endpoint**.
-
-1. Select the **OpenAI** tab.
-
-1. Make a note of the endpoint, which should look like `https://my-resource.openai.azure.com`.
-
----
+1. Sign in to the [Azure portal](https://portal.azure.com).
 
-## Deploy models
+1. On your Azure AI Search service:
 
-For this quickstart, you must deploy two Azure OpenAI models to your Microsoft Foundry project:
+    1. From the left pane, select **Overview**.
+    
+    1. Copy the URL, which should look like `https://my-service.search.windows.net`.
 
-+ An embedding model for text-to-vector conversion. This quickstart uses `text-embedding-3-large`, but you can use any `text-embedding` model.
+1. On your Microsoft Foundry resource:
 
-+ An LLM for query planning and answer generation. This quickstart uses `gpt-5-mini`, but you can use any [supported LLM for agentic retrieval](../../agentic-retrieval-how-to-create-knowledge-base.md#supported-models).
+    1. From the left pane, select **Resource Management** > **Keys and Endpoint**.
 
-For deployment instructions, see [Deploy Microsoft Foundry Models in the Foundry portal](/azure/ai-foundry/how-to/deploy-models-openai).
+    1. Copy the URL on the **OpenAI** tab, which should look like `https://my-resource.openai.azure.com/`.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的検索のセットアップガイドの一部修正"
}
```

### Explanation
この変更は、エージェント的検索のセットアップガイドに対する軽微な更新を反映しています。主な改訂内容には、手順の整理、文言の簡略化、および最新情報の追加があります。

具体的には、Microsoft Entra IDによる認証や役割ベースのアクセス権の設定についての手順が改善され、分かりやすい形で再構成されています。手順が数段階に分かりやすく示されており、特に各サービスへのアクセス設定に関する部分が強調されています。また、エンドポイントの取得手順も簡素化され、ユーザーが効率的に必要な情報を見つけることができるようになっています。

この更新により、Azure AI SearchとMicrosoft Foundryのサービスへスムーズにアクセスし、必要なモデルを容易にデプロイできるようにサポートされています。全体的に、この変更はエージェント的検索機能を利用するための導入手順をさらに明確にし、新規ユーザーがストレスなく始められることを目的としています。

## articles/search/includes/quickstarts/agentic-retrieval-typescript.md{#item-e6370b}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 01/14/2026
+ms.date: 02/23/2026
 ms.custom: dev-focus
 ai-usage: ai-assisted
 ---
@@ -15,7 +15,10 @@ In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview
 
 A *knowledge base* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the knowledge base outputs raw content from your sources, but this quickstart uses the answer synthesis output mode for natural-language answer generation.
 
-Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
+Although you can use your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book.
+
+> [!TIP]
+> Source code for the TypeScript version of this quickstart isn't available. You can copy code directly from this article.
 
 ## Prerequisites
 
@@ -25,68 +28,66 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
-+ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
++ An embedding model [deployed to your project](/azure/ai-foundry/how-to/deploy-models-openai) for text-to-vector conversion. You can use any `text-embedding` model, such as `text-embedding-3-large`.
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) and the latest LTS version of [Node.js](https://nodejs.org/en/download/).
++ An LLM [deployed to your project](/azure/ai-foundry/how-to/deploy-models-openai) for query planning and answer generation. You can use any [supported LLM](../../agentic-retrieval-how-to-create-knowledge-base.md#supported-models), such as `gpt-5-mini`.
 
-[!INCLUDE [Setup](./agentic-retrieval-setup.md)]
++ [Node.js 20 LTS](https://nodejs.org/en/download/) or later.
 
-## Set up the environment
++ [Visual Studio Code](https://code.visualstudio.com/download).
 
-To set up the console application for this quickstart:
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
+
+[!INCLUDE [agentic retrieval setup](agentic-retrieval-setup.md)]
+
+## Set up the environment
 
 1. Create a folder named `quickstart-agentic-retrieval` to contain the application.
 
 1. Open the folder in Visual Studio Code.
 
-1. Select **Terminal** > **New Terminal**, and then run the following commands to initialize the `package.json` file.
+1. Select **Terminal** > **New Terminal**, and then run the following commands to initialize `package.json`.
 
-    ```console
+    ```bash
     npm init -y
     npm pkg set type=module
     ```
 
 1. Install TypeScript as a development dependency.
 
-    ```console
+    ```bash
     npm install --save-dev typescript @types/node
     ```
 
 1. Install the [Azure AI Search client library for JavaScript](/javascript/api/overview/azure/search-documents-readme).
 
-    ```console
+    ```bash
     npm install @azure/search-documents@12.3.0-beta.1
     ```
 
 1. For keyless authentication with Microsoft Entra ID, install the [Azure Identity client library for JavaScript](/javascript/api/overview/azure/identity-readme).
 
-    ```console
+    ```bash
     npm install @azure/identity
     ```
 
-1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Microsoft Foundry project.
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search and Microsoft Foundry resources.
 
-    ```console
+    ```bash
     az login
     ```
 
 ## Run the code
 
-To create and run the agentic retrieval pipeline:
-
-1. Create a file named `.env` in the `quickstart-agentic-retrieval` folder.
-
-1. Paste the following environment variables into the `.env` file.
+1. Create a file named `.env` in the `quickstart-agentic-retrieval` folder, and then paste the following content. Replace the placeholder values with the URLs you obtained in [Get endpoints](#get-endpoints).
 
     ```
     AZURE_SEARCH_ENDPOINT = https://<your-search-service-name>.search.windows.net
-    AZURE_OPENAI_ENDPOINT = https://<your-ai-foundry-resource-name>.openai.azure.com/
+    AZURE_OPENAI_ENDPOINT = https://<your-foundry-resource-name>.openai.azure.com/
     AZURE_OPENAI_GPT_DEPLOYMENT = gpt-5-mini
     AZURE_OPENAI_EMBEDDING_DEPLOYMENT = text-embedding-3-large
     ```
 
-1. Set `AZURE_SEARCH_ENDPOINT` and `AZURE_OPENAI_ENDPOINT` to the values you obtained in [Get endpoints](#get-endpoints).
-
 1. Create a file named `index.ts`, and then paste the following code into the file.
 
     ```typescript
@@ -454,21 +455,21 @@ To create and run the agentic retrieval pipeline:
 
 1. Transpile the code from TypeScript to JavaScript.
 
-    ```console
+    ```bash
     npx tsc
     ```
 
 1. Build and run the application.
 
-    ```console
+    ```bash
     node --env-file ./.env dist/index.js
     ```
 
 ### Output
 
 The output of the application should be similar to the following:
 
-```console
+```output
 Waiting for indexing to complete...
 Expected documents: 194
 Current indexed count: 194
@@ -516,58 +517,7 @@ Activity Type: searchIndex
     "semanticConfigurationName": "semantic_config"
   }
 }
-Activity Type: searchIndex
-{
-  "id": 2,
-  "type": "searchIndex",
-  "elapsedMs": 538,
-  "knowledgeSourceName": "earth-knowledge-source",
-  "queryTime": "2025-12-19T15:38:24.001Z",
-  "count": 0,
-  "searchIndexArguments": {
-    "search": "factors that make Phoenix nighttime street grid highly visible from space reasons highway/interstate lighting visibility differences Midwestern interstates dim",
-    "filter": null,
-    "sourceDataFields": [
-      {
-        "name": "page_chunk"
-      },
-      {
-        "name": "id"
-      },
-      {
-        "name": "page_number"
-      }
-    ],
-    "searchFields": [],
-    "semanticConfigurationName": "semantic_config"
-  }
-}
-Activity Type: searchIndex
-{
-  "id": 3,
-  "type": "searchIndex",
-  "elapsedMs": 465,
-  "knowledgeSourceName": "earth-knowledge-source",
-  "queryTime": "2025-12-19T15:38:24.467Z",
-  "count": 2,
-  "searchIndexArguments": {
-    "search": "satellite nighttime lights seasonal variations suburban brightening studies December holiday lighting residential vs commercial lighting patterns",
-    "filter": null,
-    "sourceDataFields": [
-      {
-        "name": "page_chunk"
-      },
-      {
-        "name": "id"
-      },
-      {
-        "name": "page_number"
-      }
-    ],
-    "searchFields": [],
-    "semanticConfigurationName": "semantic_config"
-  }
-}
+... // Trimmed for brevity
 Activity Type: agenticReasoning
 {
   "id": 4,
@@ -773,7 +723,7 @@ console.log(`✓ All ${documents.length} documents indexed successfully!`);
 
 A knowledge source is a reusable reference to source data. The following code defines a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
 
-`source_data_fields` specifies which index fields are included in citation references. This example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+`sourceDataFields` specifies which index fields are included in citation references. This example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
 
 ```typescript
 await searchIndexClient.createKnowledgeSource({
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的検索のTypeScriptクイックスタートガイドの更新"
}
```

### Explanation
この変更は、エージェント的検索のTypeScriptクイックスタートガイドに関する軽微な更新を反映しています。主な内容としては、手順の修正、情報の追加、及び文言の明確化が含まれています。

具体的には、まずドキュメントの日付が更新され、ナビゲーションの改善がなされています。サンプルデータとしてのNASAのEarth at Night電子書籍に関連する情報は維持されつつ、自分のデータを使用する可能性についても簡潔に説明されています。また、ソースコードが記事内に直接コピーできることを示すためのヒントも追加され、ユーザーにとってアクセスしやすいリファレンスとなっています。

さらに、前提条件に関する情報が整理され、最新のNode.jsやAzure CLIのバージョンが推奨されています。セットアップ手順においても、環境設定が分かりやすく示され、ユーザーが必要な操作を迅速に実行できるよう工夫されています。

結果として、これらの変更により、Azure AI Search機能とその実装を学ぶ開発者に対して、よりスムーズで効率的な体験が提供されるようになっています。このクイックスタートガイドは、ユーザーがエージェント的検索パイプラインの実装を容易に行うことを支援する重要なリソースです。

## articles/search/includes/quickstarts/full-text-java.md{#item-d659f9}

<details>
<summary>Diff</summary>
````diff
@@ -71,17 +71,29 @@ Full-text search uses Apache Lucene for indexing and queries and the BM25 rankin
 
 Compile and run the application.
 
+### [Windows](#tab/windows)
+
 ```bash
 javac -d target/classes -cp "target/dependency/*" src/main/java/azure/search/sample/*.java
 java -cp "target/classes;target/dependency/*" azure.search.sample.App
 ```
 
-On macOS or Linux, use `:` instead of `;` as the classpath separator.
+### [macOS](#tab/macos)
+
+```bash
+javac -d target/classes -cp "target/dependency/*" src/main/java/azure/search/sample/*.java
+java -cp "target/classes:target/dependency/*" azure.search.sample.App
+```
+
+### [Linux](#tab/linux)
 
 ```bash
+javac -d target/classes -cp "target/dependency/*" src/main/java/azure/search/sample/*.java
 java -cp "target/classes:target/dependency/*" azure.search.sample.App
 ```
 
+---
+
 ### Output
 
 The output should be similar to the following:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フルテキスト検索のJavaクイックスタートガイドの更新"
}
```

### Explanation
この変更は、フルテキスト検索のJavaクイックスタートガイドに対する軽微な更新を含んでいます。具体的には、アプリケーションのコンパイルと実行に関する手順が改善されています。

主な改訂内容として、Windows、macOS、およびLinuxの環境ごとに異なるクラスパスの指定が追加され、ユーザーが自身のオペレーティングシステムに適したコマンドを容易に見つけられるようになっています。これにより、異なるプラットフォームに対応した実行方法が明示され、実行エラーのリスクを軽減しています。

さらに、出力に関するセクションが強調されていることで、ユーザーが期待される結果を簡単に確認できるようになっています。

全体として、この変更は、フルテキスト検索機能をJavaで利用するための手順を明確にし、新規ユーザーが効率的に学ぶためのサポートを強化することを目的としています。このような改訂は、ユーザー体験を向上させる重要な要素となります。

## articles/search/includes/quickstarts/search-get-started-vector-python.md{#item-53085f}

<details>
<summary>Diff</summary>
````diff
@@ -78,7 +78,7 @@ In Azure AI Search, a vector index has an index schema that defines vector and n
 
 ## Run the code
 
-1. Run the `Install packages and set variables` cell to load environment variables and verify the package installation.
+1. Run the `Install packages and set variables` cell to install the required packages and load environment variables.
 
 1. Run the remaining cells sequentially to create a vector index, upload documents, and run different types of vector queries.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Vector検索のPythonクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Vector検索に関するPythonクイックスタートガイドの軽微な更新を反映しています。変更された内容は、コードを実行する際の手順に関する文言の改善です。

具体的には、環境変数の読み込みとパッケージのインストールに関する説明が若干変更されました。元の文では環境変数を確認することに焦点を当てていたのに対し、新しい文では「必要なパッケージをインストールする」ことが明示的に強調されています。この修正により、ユーザーにとってどのステップが重要であるかがより明確になり、ユーザーが必要な操作を理解しやすくなっています。

このような変更は、クイックスタートガイド全体の可読性を向上させ、ユーザーが手順を実行する際の混乱を軽減する役割を果たします。結果的に、ユーザーはよりスムーズにVector検索を利用するための準備を進めることができるようになります。

## articles/search/samples-java.md{#item-5992fd}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.custom:
   - devx-track-extended-java
   - ignite-2023
 ms.topic: concept-article
-ms.date: 01/13/2026
+ms.date: 02/23/2026
 ---
 
 # Java samples for Azure AI Search
@@ -48,6 +48,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. T
 
 | Sample | Article | Description |
 |--|--|--|
+| [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart-agentic-retrieval) | [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md) | Integrate semantic ranking with LLM-powered query planning and answer generation. |
 | [quickstart-keyword-search](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart-keyword-search) | [Quickstart: Full-text search](search-get-started-text.md) | Create, load, and query a search index using sample data. |
 | [quickstart-semantic-ranking](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart-semantic-ranking) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
 | [quickstart-vector-search](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart-vector-search) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaサンプルガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchに関するJavaサンプルガイドに対する軽微な更新が行われたことを示しています。具体的には、日付の更新と新しいサンプルの追加が含まれています。

まず、メタデータの一部として、日付が「2026年1月13日」から「2026年2月23日」に変更されています。これにより、ガイドの最新性を反映しています。

次に、新しいコードサンプルである「quickstart-agentic-retrieval」が追加され、エージェントによるリトリーバルとLLM（大規模言語モデル）を活用したクエリ計画および回答生成の統合に関連する特徴が示されるようになります。この新しいサンプルは、ユーザーがより高度な機能を学ぶ機会を提供し、Azure AI Searchの使用を促進する役割を果たしています。

全体として、これらの更新は、ユーザーに最新の情報と実用的なリソースを提供し、JavaプログラミングにおけるAzure AI Searchの活用を一層促進することを目的としています。

## articles/search/search-get-started-agentic-retrieval.md{#item-4a40f4}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 01/14/2026
+ms.date: 02/23/2026
 ms.custom: dev-focus
 ai-usage: ai-assisted
 zone_pivot_groups: search-get-started-agentic-retrieval
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルのクイックスタートガイドの日付更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエージェントリトリーバルのクイックスタートガイドの軽微な更新を示しています。主な変更点は、文書のメタデータの日付が更新されたことです。

具体的には、元の投稿日「2026年1月14日」が「2026年2月23日」に変更されており、これはガイドの最新性を示すための通常の更新です。この日付変更により、ユーザーはリソースが最新の状態であることを理解でき、信頼性の高い情報を得ることができるようになります。

その他のメタデータは変更されておらず、ガイドの構成要素である著者やトピック、サービス情報がそのまま維持されています。このように小さな更新でも、ユーザーの利用体験を向上させる重要な役割を果たしています。

## articles/search/search-how-to-index-onelake-files.md{#item-95f3db}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: gimondra
 manager: nitinme
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 11/21/2025
+ms.date: 02/17/2026
 ms.custom:
   - build-2024
   - ignite-2024
@@ -44,7 +44,9 @@ This article uses the REST APIs to illustrate each step.
 
 + An AI Search service, basic pricing tier or higher, configured for either a [system managed identity](search-how-to-managed-identities.md#create-a-system-managed-identity) or [user-assigned assigned managed identity](search-how-to-managed-identities.md#create-a-user-assigned-managed-identity). The AI Search service must reside within the same tenant as the Microsoft Fabric workspace.
   
-+ A Contributor role assignment in the Microsoft Fabric workspace where the lakehouse is located. Steps are outlined in the [Grant permissions](#assign-service-permissions) section of this article.
++ An Administrator or Contributor role assignment in the Microsoft Fabric workspace where the lakehouse is located. Steps are outlined in the [Grant permissions](#assign-service-permissions) section of this article.
+
++ Allow [access to OneLake data from applications that are outside of the Fabric environment](/fabric/onelake/security/get-started-security#allow-apps-running-outside-of-fabric-to-access-data-via-onelake). 
 
 + A [REST client](search-get-started-text.md) to formulate REST calls similar to the ones shown in this article.
 
@@ -96,6 +98,10 @@ The following OneLake shortcuts are supported by the OneLake files indexer:
 
 + [Google Cloud Storage shortcut](/fabric/onelake/create-gcs-shortcut)
 
+
+> [!IMPORTANT]
+> Failing to meet any of the prerequisites, or attempting an operation covered by the documented limitations, will cause errors when listing items in the lakehouse.
+
 ## Prepare data for indexing
 
 Before you set up indexing, review your source data to determine whether any changes should be made to your data in the lakehouse. An indexer can index content from one container at a time. By default, all files in the container are processed. You have several options for more selective processing:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLakeファイルのインデックス作成に関するガイドの更新"
}
```

### Explanation
この変更は、OneLakeファイルのインデックス作成に関するガイドの軽微な更新を示しています。主な変更点として、日付の更新、役割の明確化、新しい情報の追加が含まれています。

まず、文書の日付が「2025年11月21日」から「2026年2月17日」に変更され、ガイドが最新の情報を反映していることが示されました。

次に、Microsoft Fabricワークスペースにおける役割の説明が「Contributor」から「AdministratorまたはContributor」に変更され、より明確な権限についての理解を提供しています。これにより、使用者が必要な権限を得るための手続きをよりスムーズに行えるようになっています。

また、OneLakeデータへの外部アプリケーションからのアクセスを許可する方法に関する新しい情報が追加され、ユーザーは外部環境からもデータにアクセスできる手続きを知ることができます。

最後に、「重要」な注意事項として、事前条件を満たさない場合や、制限に関する操作を試みた場合にエラーが発生することが明記されています。これにより、ユーザーは期待通りの結果が得られない可能性があることを事前に認識でき、トラブルを避ける手助けとなります。

全体を見ると、これらの更新はユーザー体験を向上させ、最新の情報を提供するための重要な役割を果たしています。

## articles/search/search-howto-complex-data-types.md{#item-75a002}

<details>
<summary>Diff</summary>
````diff
@@ -65,7 +65,7 @@ The following JSON document is composed of simple fields and complex fields. Com
 
 As with any index definition, you can use the Azure portal, [REST API](/rest/api/searchservice/indexes/create), or [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindex) to create a schema that includes complex types. 
 
-Other Azure SDKs provide samples in [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/samples/sample_index_crud_operations.py), [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateIndexExample.java), and [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/javascript/indexOperations.js).
+Other Azure SDKs provide samples in [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/samples/sample_index_crud.py), [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateIndexExample.java), and [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/javascript/indexOperations.js).
 
 ### [**Azure portal**](#tab/portal)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "複雑なデータ型に関するガイドのサンプルリンク更新"
}
```

### Explanation
この変更は、複雑なデータ型に関するガイドの軽微な更新を示しています。主な変更点は、Azure SDKに関するPythonサンプルのリンクが更新されたことです。

具体的には、以前のリンクが「sample_index_crud_operations.py」から「sample_index_crud.py」に変更されています。この変更により、ユーザーは最新のサンプルコードを参照できるようになり、正しい情報にアクセスできることが保証されます。

その他の部分については変更がなく、JavaおよびJavaScriptのサンプルリンクはそのまま維持されています。このような小さな更新でも、ドキュメントの正確性や信頼性を高め、開発者がリソースに素早くアクセスできるよう手助けしています。全体として、これらの更新はユーザーが効率的に開発を行うために重要な役割を果たしています。


