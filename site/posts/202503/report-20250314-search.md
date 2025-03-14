---
date: '2025-03-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:32f7d9a...MicrosoftDocs:109c448
summary: この変更は、Azure AI関連ドキュメントのリンク先URLを最新のものに修正し、ユーザーが正確で最新の情報にアクセスできるようにすることを目的としています。新しい機能の追加はありませんが、リンクが更新され、Azure
  AI Foundryに移行しています。重大な互換性問題は発生せず、主にリンク修正によるものです。ユーザーエクスペリエンスが向上し、情報の信頼性が高まることで、開発者や技術者がAzure
  Technologiesを最適に利用できる環境が整います。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:32f7d9a...MicrosoftDocs:109c448){target="_blank"}

# Highlights
以下の変更は、Azure AI関連ドキュメントにおいて、リンク先のURLを最新のものに修正することで、ユーザーが正確かつ最新の情報にアクセスできるようにすることを目的としています。このアップデートは全体的に文書の整合性と情報の正確性を向上させるためのものです。

## 新機能
特に新しい機能の追加はありませんが、Azure AI Foundryのアップデートに伴い、リンクが最新のリソースを指すように変更されています。

## 破壊的な変更
重大な互換性の問題を生じさせるような変更はありません。主としてリンクの修正のため、以前のリンクを使用する場合にアクセスできないという例外を除き、機能性の破壊にはつながりません。

## その他の更新
- 各記事内で、Azure AI StudioからAzure AI Foundryへのリンクが変更されました。
- 検索記事に加えて、モデリング、デプロイ、ベクトライザーに関する記事のリンクも最新のものに修正されています。

# インサイト
このdiffには、Azure Technologienに関連するドキュメント内でのリンク更新が含まれています。特に注目すべきは、Azure AI StudioからAzure AI Foundryへとリンクが移行している点です。これはおそらく、Azure AI Foundryがより包括的で最新のプラットフォームとして機能をアップデートしたことを反映しています。

技術的には、この変更はリンクの修正にとどまりますが、ユーザーエクスペリエンスに大きく影響を与えます。リンクが正確であることは、ユーザーが必要なリソースにスムーズにアクセスできることを意味します。特に技術文書においては、リンクの正確性が情報の信頼性に直結します。

これにより、ドキュメントの一貫性が維持され、ユーザーは最新の情報にアクセスしやすくなり、Azure AI Foundryの新しい機能や更新情報を迅速に活用できる環境が整えられることになります。また、情報の更新は、開発者や技術者がAzure Technologiesの利用を最適化するために不可欠な要素であり、それが文書更新の背後にあるモチベーションと考えられます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index.yml](#item-c67121) | minor update | 検索記事のリンク更新 (Locale: ja_JP) | modified | 3 | 3 | 6 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | リンクの更新と一貫性向上 (Locale: ja_JP) | modified | 2 | 2 | 4 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | リンクの修正と一貫性の向上 (Locale: ja_JP) | modified | 2 | 2 | 4 | 
| [search-get-started-rag.md](#item-05ff0e) | minor update | リンクの修正 (Locale: ja_JP) | modified | 1 | 1 | 2 | 
| [search-region-support.md](#item-25b0f1) | minor update | リンクの修正 (Locale: ja_JP) | modified | 2 | 2 | 4 | 
| [search-try-for-free.md](#item-36e28d) | minor update | リンクの修正 (Locale: ja_JP) | modified | 3 | 3 | 6 | 
| [tutorial-rag-build-solution-models.md](#item-6796c9) | minor update | リンクの修正 (Locale: ja_JP) | modified | 1 | 1 | 2 | 
| [vector-search-integrated-vectorization-ai-studio.md](#item-353fcc) | minor update | リンクの修正 (Locale: ja_JP) | modified | 6 | 6 | 12 | 
| [vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md](#item-ebe7a3) | minor update | リンクの修正 (Locale: ja_JP) | modified | 2 | 2 | 4 | 
| [whats-new.md](#item-fa71b4) | minor update | リンクの修正 (Locale: ja_JP) | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/index.yml{#item-c67121}

<details>
<summary>Diff</summary>
````diff
@@ -68,11 +68,11 @@ landingContent:
       - linkListType: how-to-guide
         links:
           - text: Create a vector index in Azure AI Foundry portal
-            url: /azure/ai-studio/how-to/index-add
+            url: /azure/ai-foundry/how-to/index-add
           - text: Chat with your data using Azure OpenAI
             url: /azure/ai-services/openai/use-your-data-quickstart
-          - text: Build a question and answer copilot
-            url: /azure/ai-studio/tutorials/deploy-copilot-ai-studio
+          - text: Build a custom RAG app using Azure AI Foundry SDK
+            url: /azure/ai-foundry/tutorials/copilot-sdk-build-rag
 
   # Card
   - title: Index data
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索記事のリンク更新 (Locale: ja_JP)"
}
```

### Explanation
このコードの差分では、`articles/search/index.yml`ファイルにおいて、いくつかのリンクが更新されています。具体的には、Azure AI Foundryに関連するリンクが新しいURLに修正されており、これによりより正確な情報を提供することが目的です。変更された部分には、Azure AI StudioからAzure AI Foundryへのリンクの移行が含まれており、具体的には「Create a vector index in Azure AI Foundry portal」と「Build a custom RAG app using Azure AI Foundry SDK」に関連するリンクが追加されています。この更新は利用者が最新の情報を得られるようにするためのマイナーな調整と見なされます。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ Azure AI Search is a [proven solution for information retrieval](/azure/develope
 
 Microsoft has several built-in implementations for using Azure AI Search in a RAG solution.
 
-+ Azure AI Foundry, [use a vector index and retrieval augmentation](/azure/ai-studio/concepts/retrieval-augmented-generation). 
++ Azure AI Foundry, [use a vector index and retrieval augmentation](/azure/ai-foundry/concepts/retrieval-augmented-generation). 
 + Azure OpenAI, [use a search index with or without vectors](/azure/ai-services/openai/concepts/use-your-data).
 + Azure Machine Learning, [use a search index as a vector store in a prompt flow](/azure/machine-learning/how-to-create-vector-index).
 
@@ -78,7 +78,7 @@ The information retrieval system provides the searchable index, query logic, and
 
 The LLM receives the original prompt, plus the results from Azure AI Search. The LLM analyzes the results and formulates a response. If the LLM is ChatGPT, the user interaction might be a back and forth conversation. If you're using Davinci, the prompt might be a fully composed answer. An Azure solution most likely uses Azure OpenAI, but there's no hard dependency on this specific service.
 
-Azure AI Search doesn't provide native LLM integration for prompt flows or chat preservation, so you need to write code that handles orchestration and state. You can review demo source ([Azure-Samples/azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo)) for a blueprint of what a full solution entails. We also recommend [Azure AI Foundry](/azure/ai-studio/concepts/retrieval-augmented-generation) to create RAG-based Azure AI Search solutions that integrate with LLMs.
+Azure AI Search doesn't provide native LLM integration for prompt flows or chat preservation, so you need to write code that handles orchestration and state. You can review demo source ([Azure-Samples/azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo)) for a blueprint of what a full solution entails. We also recommend [Azure AI Foundry](/azure/ai-foundry/concepts/retrieval-augmented-generation) to create RAG-based Azure AI Search solutions that integrate with LLMs.
 
 ## Searchable content in Azure AI Search
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの更新と一貫性向上 (Locale: ja_JP)"
}
```

### Explanation
このコードの差分では、`articles/search/retrieval-augmented-generation-overview.md`ファイルにおいて、いくつかのリンクが最新の情報に更新されています。主に、Azure AI Foundryに関連するリンクが新しいURLに修正され、整合性が向上しています。具体的には、「/azure/ai-studio/concepts/retrieval-augmented-generation」から「/azure/ai-foundry/concepts/retrieval-augmented-generation」への変更が行われており、これによってユーザーが最新のリソースにアクセスできるようになっています。また、情報検索システムの説明部分でも変更は行われておらず、リンクの更新により内容の一貫性が維持されています。この変更は、文書の正確性と信頼性を高めるためのマイナーな調整と考えられます。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -47,7 +47,7 @@ Use an embedding model on an Azure AI platform in the [same region as Azure AI S
 | Provider | Supported models |
 |---|---|
 | [Azure OpenAI Service](https://aka.ms/oai/access) | text-embedding-ada-002 <br>text-embedding-3-large <br>text-embedding-3-small |
-| [Azure AI Foundry model catalog](/azure/ai-studio/what-is-ai-studio) | For text: <br>Cohere-embed-v3-english <br>Cohere-embed-v3-multilingual <br>For images: <br>Facebook-DinoV2-Image-Embeddings-ViT-Base <br>Facebook-DinoV2-Image-Embeddings-ViT-Giant |
+| [Azure AI Foundry model catalog](/azure/ai-foundry/what-is-ai-foundry) | For text: <br>Cohere-embed-v3-english <br>Cohere-embed-v3-multilingual <br>For images: <br>Facebook-DinoV2-Image-Embeddings-ViT-Base <br>Facebook-DinoV2-Image-Embeddings-ViT-Giant |
 | [Azure AI services multi-service account](/azure/ai-services/multi-service-resource) | [Azure AI Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) for image and text vectorization, [available in selected regions](/azure/ai-services/computer-vision/how-to/image-retrieval?tabs=csharp). Depending on how you [attach the multi-service resource](cognitive-search-attach-cognitive-services.md), the multi-service account might need to be in the same region as Azure AI Search. |
 
 If you use the Azure OpenAI Service, the endpoint must have an associated [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains). A custom subdomain is an endpoint that includes a unique name (for example, `https://hereismyuniquename.cognitiveservices.azure.com`). If the service was created through the Azure portal, this subdomain is automatically generated as part of your service setup. Ensure that your service includes a custom subdomain before using it with the Azure AI Search integration.
@@ -204,7 +204,7 @@ After you finish these steps, you should be able to select the Azure AI Vision v
 
 The wizard supports Azure, Cohere, and Facebook embedding models in the Azure AI Foundry model catalog, but it doesn't currently support the OpenAI CLIP models. Internally, the wizard calls the [AML skill](cognitive-search-aml-skill.md) to connect to the catalog.
 
-1. For the model catalog, you should have an [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource), a [hub in Azure AI Foundry portal](/azure/ai-studio/how-to/create-projects), and a [project](/azure/ai-studio/how-to/create-projects). Hubs and projects having the same name can share connection information and permissions.
+1. For the model catalog, you should have an [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource), a [hub in Azure AI Foundry portal](/azure/ai-foundry/how-to/create-projects), and a [project](/azure/ai-foundry/how-to/create-projects). Hubs and projects having the same name can share connection information and permissions.
 
 1. Deploy an embedding model to the model catalog in your project.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの修正と一貫性の向上 (Locale: ja_JP)"
}
```

### Explanation
このコードの差分では、`articles/search/search-get-started-portal-import-vectors.md`ファイルにおいて、Azure AI Foundryに関連するいくつかのリンクが最新のURLに修正されています。具体的には、リンクが「/azure/ai-studio/what-is-ai-studio」から「/azure/ai-foundry/what-is-ai-foundry」に変更され、これにより正確な情報が提供されるようになっています。また、モデルカタログの説明においても、同様にリンクが修正されており、既存の文脈との一貫性が向上しています。この更新は、ユーザーが最新のリソースに正しくアクセスできるようにするためのマイナーな調整と考えられます。全体として、文書の信頼性を向上させる改良が行われています。

## articles/search/search-get-started-rag.md{#item-05ff0e}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ In this quickstart, you send queries to a chat completion model for a conversati
 
 - An [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource).
   - [Choose a region](/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) that supports the chat completion model you want to use (gpt-4o, gpt-4o-mini, or an equivalent model).
-  - [Deploy the chat completion model](/azure/ai-studio/how-to/deploy-models-openai) in Azure AI Foundry or [use another approach](/azure/ai-services/openai/how-to/working-with-models).
+  - [Deploy the chat completion model](/azure/ai-foundry/how-to/deploy-models-openai) in Azure AI Foundry or [use another approach](/azure/ai-services/openai/how-to/working-with-models).
 
 - An [Azure AI Search resource](search-create-service-portal.md).
   - Use the same region as your Azure OpenAI resource.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの修正 (Locale: ja_JP)"
}
```

### Explanation
このコードの差分では、`articles/search/search-get-started-rag.md`ファイルにおいて、モデルのデプロイに関連するリンクが更新されています。具体的には、Azure AI Foundryにおけるチャット完了モデルのデプロイに関するリンクが「/azure/ai-studio/how-to/deploy-models-openai」から「/azure/ai-foundry/how-to/deploy-models-openai」に修正されており、これにより最新の情報にアクセスできるようになっています。この更新は、リソースのリンクを正確に保ち、ユーザーが必要な情報に迅速にたどり着けるようにするためのマイナーな調整です。全体として、文書の正確性と有用性が向上する改良が行われています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ Some features take a dependency on other Azure services or infrastructure that a
 | [Semantic ranker](semantic-search-overview.md) | Takes a dependency on Microsoft-hosted models in specific regions. | Regional support is noted in this article. |
 | [AI service integration](cognitive-search-concept-intro.md) | Refers to [built-in skills](cognitive-search-predefined-skills.md) that make internal calls to Azure AI for enrichment and transformation during indexing. Integration requires that Azure AI Search coexists with an [Azure AI multi-service account](/azure/ai-services/multi-service-resource) in the same physical region. You can bypass region requirements if you use [identity-based connections](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection), currently in public review. | Regional support is noted in this article. |
 | [Azure OpenAI integration](vector-search-integrated-vectorization.md)  | Refers to the AzureOpenAIEmbedding skill and vectorizer that make internal calls to deployed embedding models on Azure OpenAI. | Check [Azure OpenAI model region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability) for the most current list of regions for each embedding and chat model. Specific Azure OpenAI models are in fewer regions, so check for model availability first, and then verify Azure AI Search is available in the same region.|
-| [Azure AI Foundry integration](vector-search-integrated-vectorization-ai-studio.md) | Refers to skills and vectorizers that make internal calls to the models hosted in the model catalog. | Check [Azure AI Foundry region availability](/azure/ai-studio/reference/region-support) for the most current list of regions. |
+| [Azure AI Foundry integration](vector-search-integrated-vectorization-ai-studio.md) | Refers to skills and vectorizers that make internal calls to the models hosted in the model catalog. | Check [Azure AI Foundry region availability](/azure/ai-foundry/reference/region-support) for the most current list of regions. |
 | [Azure AI Vision 4.0 multimodal APIs](search-get-started-portal-image-search.md) | Refers to the Azure AI Vision multimodal embeddings skill and vectorizer that call the multimodal embedding API. | Check the [Azure AI Vision region list](/azure/ai-services/computer-vision/overview-image-analysis#region-availability) first, and then verify Azure AI Search is available in the same region.|
 
 ## Azure Public regions
@@ -131,7 +131,7 @@ AI service integration refers to internal connections to an Azure AI multi-servi
 
 ## See also
 
-- [Azure AI Foundry region availability](/azure/ai-studio/reference/region-support)
+- [Azure AI Foundry region availability](/azure/ai-foundry/reference/region-support)
 - [Azure OpenAI model region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)
 - [Azure AI Vision region list](/azure/ai-services/computer-vision/overview-image-analysis#region-availability)
 - [Availability zone region availability](/azure/reliability/availability-zones-region-support)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの修正 (Locale: ja_JP)"
}
```

### Explanation
このコードの差分では、`articles/search/search-region-support.md`ファイル内のいくつかのリンクが更新されています。具体的には、Azure AI Foundryに関連するリンクが「/azure/ai-studio/reference/region-support」から「/azure/ai-foundry/reference/region-support」に変更されており、これによって最新の情報へのアクセスが可能になります。この変更は、文書内の一貫性と正確性を向上させるためのマイナーな調整として位置づけられます。また、全体的なコンテンツの可読性やナビゲーションの利便性を高めるために、関連情報が正しくリンクされるように改善されています。

## articles/search/search-try-for-free.md{#item-36e28d}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ Once you sign up, you can immediately use either of these links to access Azure
 
 ## Step two: "Day One" tasks
 
-[**How to build and consume vector indexes in Azure AI Foundry portal**](/azure/ai-studio/how-to/index-add) is a great place to start.
+[**How to build and consume vector indexes in Azure AI Foundry portal**](/azure/ai-foundry/how-to/index-add) is a great place to start.
 
 1. [Sign in to Azure AI Foundry](https://ai.azure.com).
 
@@ -80,7 +80,7 @@ Start here if you want to use built-in vectorization or chat models:
 
 - [Azure OpenAI region list](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)
 - [Azure AI Vision region list](/azure/ai-services/computer-vision/overview-image-analysis?tabs=4-0#region-availability)
-- [Azure AI Foundry region list](/azure/ai-studio/reference/region-support)
+- [Azure AI Foundry region list](/azure/ai-foundry/reference/region-support)
 
 Continue with the following link to confirm region and tier availability for AI Search:
 
@@ -119,7 +119,7 @@ Try the Azure portal quickstarts for Azure AI Search or quickstarts that use Vis
 Azure AI Foundry supports connecting to content in Azure AI Search.
 
 - [Quickstart: Chat using your own data with Azure OpenAI](/azure/ai-services/openai/use-your-data-quickstart)
-- [Tutorial: Build a custom chat app with the prompt flow SDK](/azure/ai-studio/tutorials/copilot-sdk-create-resources)
+- [Tutorial: Build a custom chat app with the prompt flow SDK](/azure/ai-foundry/tutorials/copilot-sdk-create-resources)
 
 Developers should review [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) repository or the solution accelerators. You can deploy and run any of these samples using the Azure trial subscription. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの修正 (Locale: ja_JP)"
}
```

### Explanation
このコードの差分では、`articles/search/search-try-for-free.md`ファイル内のリンクがいくつか修正されています。具体的には、Azure AI Foundryに関連するリンクが「/azure/ai-studio/how-to/index-add」から「/azure/ai-foundry/how-to/index-add」に、また「/azure/ai-studio/reference/region-support」から「/azure/ai-foundry/reference/region-support」に変更されています。さらに、カスタムチャットアプリのチュートリアルリンクも同様に修正されています。これらの変更は、ユーザーが正確で最新の情報にアクセスできるようにするためのものであり、ドキュメントの情報の整合性を向上させるためのマイナーな調整です。これにより、ユーザーは必要なリソースを正しく見つけ、利用することが可能になります。

## articles/search/tutorial-rag-build-solution-models.md{#item-6796c9}

<details>
<summary>Diff</summary>
````diff
@@ -45,7 +45,7 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
   - [Azure AI Vision regions](/azure/ai-services/computer-vision/overview-image-analysis?tabs=4-0#region-availability)
 
-  - [Azure AI Foundry](/azure/ai-studio/reference/region-support) regions. 
+  - [Azure AI Foundry](/azure/ai-foundry/reference/region-support) regions. 
 
   Azure AI Search is currently facing limited availability in some regions. To confirm region status, check the [Azure AI Search region list](search-region-support.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの修正 (Locale: ja_JP)"
}
```

### Explanation
このコードの差分では、`articles/search/tutorial-rag-build-solution-models.md`ファイル内のリンクに関して、Azure AI Foundryに関連する情報が更新されています。具体的には、Azure AI Foundryの地域に関するリンクが「/azure/ai-studio/reference/region-support」から「/azure/ai-foundry/reference/region-support」に修正されています。これにより、ユーザーは最新の情報にアクセスできるようになり、文書の正確性が向上します。この変更は、Azure AI Foundryに関する情報の整合性を確保するためのマイナーな調整であり、ユーザーにより良い体験を提供することを目的としています。

## articles/search/vector-search-integrated-vectorization-ai-studio.md{#item-353fcc}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.date: 12/03/2024
 > [!IMPORTANT] 
 > This feature is in public preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [2024-05-01-Preview REST API](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true) supports this feature.
 
-In this article, learn how to access the embedding models in the [Azure AI Foundry model catalog](/azure/ai-studio/how-to/model-catalog) for vector conversions during indexing and in queries in Azure AI Search.
+In this article, learn how to access the embedding models in the [Azure AI Foundry model catalog](/azure/ai-foundry/how-to/model-catalog-overview) for vector conversions during indexing and in queries in Azure AI Search.
 
 The workflow includes model deployment steps. The model catalog includes embedding models from Microsoft and other companies. Deploying a model is billable per the billing structure of each provider. 
 
@@ -29,7 +29,7 @@ After the model is deployed, you can use it for [integrated vectorization](vecto
 
 + Azure AI Search, any region and tier.
 
-+ Azure AI Foundry and an [Azure AI Foundry project](/azure/ai-studio/how-to/create-projects).
++ Azure AI Foundry and an [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects).
 
 ## Supported embedding models
 
@@ -88,7 +88,7 @@ This AML skill payload works with the following models from Azure AI Foundry:
 
 It assumes that you're chunking your content using the [Text Split skill](cognitive-search-skill-textsplit.md) and that the text to be vectorized is in the `/document/pages/*` path. If your text comes from a different path, update all references to the `/document/pages/*` path accordingly.
 
-The URI and key are generated when you deploy the model from the catalog. For more information about these values, see [How to deploy large language models with Azure AI Foundry](/azure/ai-studio/how-to/deploy-models-open).
+The URI and key are generated when you deploy the model from the catalog. For more information about these values, see [How to deploy large language models with Azure AI Foundry](/azure/ai-foundry/how-to/deploy-models-open).
 
 ```json
 {
@@ -133,7 +133,7 @@ This AML skill payload works with the following image embedding models from Azur
 
 It assumes that your images come from the `/document/normalized_images/*` path that is created by enabling [built in image extraction](cognitive-search-concept-image-scenarios.md). If your images come from a different path or are stored as URLs, update all references to the `/document/normalized_images/*` path according.
 
-The URI and key are generated when you deploy the model from the catalog. For more information about these values, see [How to deploy large language models with Azure AI Foundry](/azure/ai-studio/how-to/deploy-models-open).
+The URI and key are generated when you deploy the model from the catalog. For more information about these values, see [Add and configure models to Azure AI model inference](/azure/ai-foundry/model-inference/how-to/create-model-deployments).
 
 ```json
 {
@@ -179,9 +179,9 @@ This AML skill payload works with the following text embedding models from Azure
 
 It assumes that you're chunking your content using the Text Split skill and therefore your text to be vectorized is in the `/document/pages/*` path. If your text comes from a different path, update all references to the `/document/pages/*` path accordingly.
 
-You must add the `/v1/embed` path onto the end of the URL that you copied from your Azure AI Foundry deployment. You might also change the values for the `input_type`, `truncate` and `embedding_types` inputs to better fit your use case. For more information on the available options, review the [Cohere Embed API reference](/azure/ai-studio/how-to/deploy-models-cohere-embed).
+You must add the `/v1/embed` path onto the end of the URL that you copied from your Azure AI Foundry deployment. You might also change the values for the `input_type`, `truncate` and `embedding_types` inputs to better fit your use case. For more information on the available options, review the [Cohere Embed API reference](/azure/ai-foundry/how-to/deploy-models-cohere-embed).
 
-The URI and key are generated when you deploy the model from the catalog. For more information about these values, see [How to deploy Cohere Embed models with Azure AI Foundry](/azure/ai-studio/how-to/deploy-models-cohere-embed).
+The URI and key are generated when you deploy the model from the catalog. For more information about these values, see [How to deploy Cohere Embed models with Azure AI Foundry](/azure/ai-foundry/how-to/deploy-models-cohere-embed).
 
 Note that image URIs aren't supported by this integration at this time.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの修正 (Locale: ja_JP)"
}
```

### Explanation
このコードの差分では、`articles/search/vector-search-integrated-vectorization-ai-studio.md`ファイル内のリンクがいくつか修正されています。主に、Azure AI Foundryに関連するリンクが「/azure/ai-studio/」から「/azure/ai-foundry/」に変更されています。この変更により、正確で最新のリソースへアクセスできるようにし、ユーザーが必要とする情報を適切に取得できるようにしています。また、全体的な文書の整合性を確保するためのマイナーな調整が行われました。これにより、Azure AI Foundryのモデルの使用やデプロイに関する情報がより明確になります。

## articles/search/vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md{#item-ebe7a3}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.date: 12/03/2024
 > [!IMPORTANT]
 > This vectorizer is in public preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [2024-05-01-Preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-05-01-Preview&preserve-view=true) supports this feature.
 
-The **Azure AI Foundry model catalog** vectorizer connects to an embedding model that was deployed via [the Azure AI Foundry model catalog](/azure/ai-studio/how-to/model-catalog) to an Azure Machine Learning endpoint. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed. 
+The **Azure AI Foundry model catalog** vectorizer connects to an embedding model that was deployed via [the Azure AI Foundry model catalog](/azure/ai-foundry/how-to/model-catalog-overview) to an Azure Machine Learning endpoint. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed. 
 
 If you used integrated vectorization to create the vector arrays, the skillset should include an [AML skill pointing to the model catalog in Azure AI Foundry portal](cognitive-search-aml-skill.md).
 
@@ -94,4 +94,4 @@ Suggested model names in the Azure AI Foundry model catalog consist of the base
 + [Integrated vectorization with models from Azure AI Foundry](vector-search-integrated-vectorization-ai-studio.md)
 + [How to configure a vectorizer in a search index](vector-search-how-to-configure-vectorizer.md)
 + [Azure Machine Learning skill](cognitive-search-aml-skill.md)
-+ [Azure AI Foundry model catalog](/azure/ai-studio/how-to/model-catalog)
\ No newline at end of file
++ [Azure AI Foundry model catalog](/azure/ai-foundry/how-to/model-catalog-overview)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの修正 (Locale: ja_JP)"
}
```

### Explanation
このコードの差分では、`articles/search/vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md`ファイル内のリンクが修正されています。特に、Azure AI Foundryモデルカタログに関連するリンクが「/azure/ai-studio/」から「/azure/ai-foundry/」に更新されています。この修正によって、最新の情報にアクセスできるようになり、ユーザーが正確なリソースを参照できるようにすることが目的です。ファイルの内容は、Azure AI Foundryのベクトライザーに関する情報を明確にし、文書全体の整合性を高めるためのマイナーな調整を行っています。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -99,7 +99,7 @@ ms.custom:
 | [Binary vectors support](/rest/api/searchservice/supported-data-types) | Feature | `Collection(Edm.Byte)` is a new supported data type. This data type opens up integration with the [Cohere v3 binary embedding models](https://cohere.com/blog/int8-binary-embeddings) and custom binary quantization. Narrow data types lower the cost of large vector datasets. See [Index binary data for vector search](vector-search-how-to-index-binary-data.md) for more information.| 
 | [Azure AI Vision multimodal embeddings skill (preview)](cognitive-search-skill-vision-vectorize.md) | Skill | New skill that's bound to the [multimodal embeddings API of Azure AI Vision](/azure/ai-services/computer-vision/concept-image-retrieval). You can generate embeddings for text or images during indexing. This skill is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true).|
 | [Azure AI Vision vectorizer (preview)](vector-search-vectorizer-ai-services-vision.md) | Vectorizer | New vectorizer connects to an Azure AI Vision resource using the [multimodal embeddings API](/azure/ai-services/computer-vision/concept-image-retrieval) to generate embeddings at query time. This vectorizer is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
-| [Azure AI Foundry model catalog vectorizer (preview)](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) | Vectorizer | New vectorizer connects to an embedding model deployed from the [Azure AI Foundry model catalog](/azure/ai-studio/how-to/model-catalog). This vectorizer is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true). <br><br>[**How to implement integrated vectorization using models from Azure AI Foundry**](vector-search-integrated-vectorization-ai-studio.md).|
+| [Azure AI Foundry model catalog vectorizer (preview)](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) | Vectorizer | New vectorizer connects to an embedding model deployed from the [Azure AI Foundry model catalog](/azure/ai-foundry/how-to/model-catalog-overview). This vectorizer is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true). <br><br>[**How to implement integrated vectorization using models from Azure AI Foundry**](vector-search-integrated-vectorization-ai-studio.md).|
 | [AzureOpenAIEmbedding skill (preview) supports more models on Azure OpenAI](cognitive-search-skill-azure-openai-embedding.md) | Skill | Now supports text-embedding-3-large and text-embedding-3-small, along with text-embedding-ada-002 from the previous update. New `dimensions` and `modelName` properties make it possible to specify the various embedding models on Azure OpenAI. Previously, the dimensions limits were fixed at 1,536 dimensions, applicable to text-embedding-ada-002 only. The updated skill is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true).|
 | Azure portal updates | Portal | [Import and vectorize data wizard](search-get-started-portal-import-vectors.md) now supports OneLake indexers as a data source. For embeddings, it also supports connections to Azure AI Vision multimodal, Azure AI Foundry model catalog, and more embedding models on Azure OpenAI. <br><br>When adding a field to an index, you can choose a [binary data type](vector-search-how-to-index-binary-data.md). <br><br>[Search explorer](search-explorer.md) now defaults to 2024-05-01-preview and supports the new preview features for vector and hybrid queries.  |
 | [2024-05-01-preview](/rest/api/searchservice/search-service-api-versions#2024-05-01-preview) | API | New preview version of the Search REST APIs provides new skills and vectorizers, new binary data type, OneLake files indexer, and new query parameters for more relevant results. See [Upgrade REST APIs](search-api-migration.md) if you have existing code written against the 2023-07-01-preview and need to migrate to this version.|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの修正 (Locale: ja_JP)"
}
```

### Explanation
このコードの差分では、`articles/search/whats-new.md`ファイル内のAzure AI Foundryに関連するリンクが修正されています。具体的には、ベクトライザーに関する記述が「/azure/ai-studio/」から「/azure/ai-foundry/」に変更されています。この修正により、ユーザーが最新のリソースにアクセスできるようになり、正確な情報を得られるようになります。また、この変更はAzure AI Foundryモデルカタログを使用した新しいベクトライザーの機能に関連しており、文章全体の整合性と正確性を高めるために重要です。


