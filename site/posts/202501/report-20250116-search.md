---
date: '2025-01-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:36d0ff5...MicrosoftDocs:f3626a8
summary: このドキュメントの変更は、Azure AI Searchに関する3つの主要な分野での改善をもたらします。コグニティブサービスの接続における請求情報や無料トランザクションの明確化、検索サービスの信頼性向上に向けたAzure
  Load Balancerの導入、そしてベクトライザー設定手順についての詳しい情報が示されました。これにより、ユーザーはサービスをより理解しやすく、効率的に利用できるようになります。特に、請求情報の透明性や信頼性の向上、効果的なベクトライザー設定の手順が強調されており、企業がニーズに合った検索機能を迅速に構築する手助けとなります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:36d0ff5...MicrosoftDocs:f3626a8){target="_blank"}

# Highlights
このドキュメントの変更は、Azure AI Searchに関する3つの主要な分野における改善をもたらします。まず、コグニティブサービスの接続における請求情報やトランザクションの無料枠について明確化されました。次に、検索サービスの信頼性向上に関するロードバランシング技術についての詳細が追加されました。最後に、ベクトライザー設定手順に関する詳しい情報が提供されました。

## New features
- 「AIマルチサービスアカウント」という用語が追加され、請求情報の提供が必要である旨が説明されました。
- Azure Load Balancerが新たなロードバランス技術として紹介されました。
- ベクトライザーの定義が明確化され、具体的な設定手順が追加されました。

## Breaking changes
なし

## Other updates
- コグニティブサービス利用時のトランザクション無料枠についての説明が修正されました。
- 負荷分散に関する健康診断プローブの設定詳細が加わりました。
- 使用可能な埋め込みモデルのリストと使用方法が詳述されました。

# Insights
Azure AI Searchに関する文書の最近のアップデートは、ユーザーがサービスをより明確に理解し、効率的に利用できるようにするための重要な改善をもたらします。まず、コグニティブサービスの接続における請求情報やトランザクション制限情報が具体化され、この領域における透明性が向上しました。「AIマルチサービスアカウント」という新しい用語の導入により、サービス利用時に必要な手続きがわかりやすく示されています。これは、ユーザーがAzureの様々なサービスを利用する際に発生する可能性のある料金体系を把握する手助けになります。

次に、Azure Load Balancerの紹介は、信頼性を高めるための技術選定を行う際の重要な指針となります。ロードバランシングは、サービスの可用性を高め、障害に対する復元性を向上させるための戦略として欠かせない要素です。特に、健康診断プローブ使用時の具体的な設定（例：HTTPSプローブと`/ping`パスの指定）は、実務における上手な実装のカギを握ります。

最後に、ベクトライザーの設定について、詳細な手順とモデルの使い方が提示されているのは、AIを活用した検索機能の改善に直結します。ベクトライザー機能は、テキストや画像を効果的に処理するために不可欠であり、今回の更新により、よりスムーズな導入と運用が可能になります。特に、使用するモデルの選定において、一貫性をもたせるためのガイドは、モデルの選定や変更に関わるリスクを最小化します。これにより、Azure AI Searchを活用する企業は、より迅速にニーズに合った検索機能を構築できます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | Azure AI Searchでのコグニティブサービスの接続の改善 | modified | 22 | 12 | 34 | 
| [search-reliability.md](#item-3e9b1a) | minor update | 検索サービスの信頼性の向上に関する説明の追加 | modified | 4 | 0 | 4 | 
| [vector-search-how-to-configure-vectorizer.md](#item-30ffd8) | minor update | ベクトライザーの設定手順の詳細追加 | modified | 16 | 5 | 21 | 


# Modified Contents
## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -14,18 +14,20 @@ ms.date: 01/09/2025
 
 # Attach an Azure AI multi-service resource to a skillset in Azure AI Search
 
-When configuring an optional [AI enrichment pipeline](cognitive-search-concept-intro.md) in Azure AI Search, you can enrich a small number of documents free of charge, limited to 20 transactions daily per index. For larger and more frequent workloads, you should attach a billable [Azure AI multi-service resource](/azure/ai-services/multi-service-resource?pivots=azportal). 
+If you're using built-in skills for optional [AI enrichment](cognitive-search-concept-intro.md) in Azure AI Search, you can enrich a small number of documents free of charge, limited to 20 transactions daily per index. For larger and more frequent workloads, you should attach a billable [Azure AI multi-service account](/azure/ai-services/multi-service-resource?pivots=azportal). 
+
+Azure AI Search uses dedicated, internally hosted Azure AI multi-service resources for built-in skills execution, but needs your multi-service account for billing purposes. 
 
 A multi-service account provides a collection of Azure AI services, rather than individual services. Providing an account in an Azure AI Search [skillset](/rest/api/searchservice/skillsets/create) allows Microsoft to charge you for using these services:
 
-+ [Azure AI Vision](/azure/ai-services/computer-vision/overview) for image analysis, optical character recognition (OCR), and multimodal text and image embedding.
++ [Azure AI Vision](/azure/ai-services/computer-vision/overview) for image analysis, optical character recognition (OCR), and multimodal embeddings
 + [Azure AI Language](/azure/ai-services/language-service/overview) for language detection, entity recognition, sentiment analysis, and key phrase extraction
 + [Azure AI Speech](/azure/ai-services/speech-service/overview) for speech to text and text to speech
 + [Azure AI Translator](/azure/ai-services/translator/translator-overview) for machine text translation
 
-You must provide connection information to the Azure AI multi-resource in the skillset. Azure AI Search doesn't use the connection for skillset workloads, but it does use the connection to access the billing meters on the resource. As such, your Azure AI services account is used for billing, not skills processing. Azure AI Search uses separate dedicated resources for skills processing.
+Exceptions to billing through the multi-service account include [AzureOpenAIEmbedding](cognitive-search-skill-azure-openai-embedding.md) or the [AML skill](cognitive-search-aml-skill.md) billing. Azure AI Search doesn't internally host models from Azure OpenAI or the Azure AI Foundry model catalog. Usage for AML and Azure OpenAI skills and vectorizers are through [Azure OpenAI pay-as-you-go pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing) and [Azure Machine Learning pay-as-you-go pricing](https://azure.microsoft.com/pricing/details/machine-learning/), respectively. A few other skills, such as Text Split and Text Merge, aren't billable.
 
-You can use a key on the connection, or implement a keyless approach that's currently in preview.
+To attach an Azure AI multi-resource, you must provide connection information in the skillset. You can use a key on the connection, or implement a keyless approach that's currently in preview.
 
 > [!TIP]
 > Azure provides infrastructure for you to monitor billing and budgets. For more information about monitoring Azure AI services, see [Plan and manage costs for Azure AI services](/azure/ai-services/plan-manage-costs).
@@ -49,15 +51,15 @@ Using the Azure portal or newer preview REST APIs and beta SDK packages, you can
 
 1. Using the Azure portal, or the [Skillset 2024-11-01-preview REST API](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true), or an Azure SDK beta package that provides the syntax, configure a skillset to use an identity:
 
-   + The managed identity used on the connection belongs to the search service.
-   + The identity can be system managed or user assigned.
+   + The managed identity used on the connection belongs to the search service. It can be system managed or user assigned.
+
    + The identity must have **Cognitive Services User** permissions on the Azure AI resource.
+
    + `@odata.type` is always `#Microsoft.Azure.Search.AIServicesByIdentity`.
-   + `subdomainUrl` is the endpoint of your Azure AI multi-service resource. It can be in [any region that's jointly supported](search-region-support.md#azure-public-regions) by Azure AI Search and Azure AI services.
 
-As with keys, the details you provide about the Azure AI Services resource are used for billing, not connections.  All API requests made by Azure AI Search to Azure AI services for built-in skills processing continue to be internal and managed by Microsoft.
+   + `subdomainUrl` is the endpoint of your Azure AI multi-service resource. The subdomain URL must include a unique name (for example, `https://hereismyuniquename.cognitiveservices.azure.com`). If the service was created through the Azure portal, a unique subdomain is automatically generated as part of your service setup. Ensure that your service includes a unique subdomain before using it with the Azure AI Search integration.
 
-The subdomain URL must include a unique name (for example, `https://hereismyuniquename.cognitiveservices.azure.com`). If the service was created through the Azure portal, a unique subdomain is automatically generated as part of your service setup. Ensure that your service includes a unique subdomain before using it with the Azure AI Search integration.
+As with keys, the details you provide about the Azure AI Services resource are used for billing, not connections.  All API requests made by Azure AI Search to Azure AI services for built-in skills processing continue to be internal and managed by Microsoft.
 
 ### Example: system-assigned managed identity
 
@@ -110,10 +112,12 @@ POST https://[service-name].search.windows.net/skillsets/[skillset-name]?api-ver
 
 ## Bill through a resource key
 
-Azure AI Search can also charge for transaction using the Azure AI multi-service resource key. This approach is the default and is generally available. You can use the Azure portal, REST API, or an Azure SDK to add the key to a skillset.
+Azure AI Search can also charge for transactions using the Azure AI multi-service resource key. This approach is the default and is generally available. You can use the Azure portal, REST API, or an Azure SDK to add the key to a skillset.
 
 There are two supported key types: `#Microsoft.Azure.Search.CognitiveServicesByKey` which calls the regional endpoint and `"#Microsoft.Azure.Search.AIServicesByKey` which calls the subdomain. We recommend using `AIServicesByKey` for its shared private link support and ability to function with no regional requirements relative to the search service.
 
+The Azure AI multi-service account must be in the same region as Azure AI Search. For more information, see [Regions supported by Azure AI Search](search-region-support.md#azure-public-regions) and choose a region that provides AI services integration.
+
 If you leave the `cognitiveServices` property unspecified, your search service attempts to use the free enrichments available to your indexer on a daily basis. Execution of billable skills stops at 20 transactions per indexer invocation and a "Time Out" message appears in indexer execution history.
 
 ### [**Azure portal**](#tab/portal)
@@ -274,7 +278,11 @@ Enrichments are billable operations. If you no longer need to call Azure AI serv
 
 Billing goes into effect when API calls to Azure AI services resources exceed 20 API calls per indexer, per day. You can [reset the indexer](search-howto-run-reset-indexers.md) to reset the API count.
 
-Keyless and key-based connections are used for billing, but not for enrichment operations' connections. For connections, a search service [connects over the internal network](search-security-overview.md#internal-traffic) to an Azure AI services resource that's located in the [same physical region](search-region-support.md). Most regions that offer Azure AI Search also offer other Azure AI services such as Language. If you attempt AI enrichment in a region that doesn't have both services, you'll see this message: "Provided key isn't a valid CognitiveServices type key for the region of your search service."
+Keyless and key-based connections are used for billing, but not for enrichment operations' connections. 
+
+For key-based connections, a search service [connects over the internal network](search-security-overview.md#internal-traffic) to an Azure AI services resource that's located in the [same physical region](search-region-support.md). Most regions that offer Azure AI Search also offer other Azure AI services such as Language. If you attempt AI enrichment in a region that doesn't have both services, you'll see this message: "Provided key isn't a valid CognitiveServices type key for the region of your search service."
+
+For keyless connections, a search service authenticates using its identity and role assignment, targeting an Azure AI multi-service resource that's specified as a fully-qualified URI, having a unique subdomain in that URI.
 
 Indexers can be configured to run in a [private execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment) for dedicated processing using just the search nodes of your own search service. Even if you're using private execution environment, Azure AI Search still uses its internally provisioned Azure AI multiservice resource to perform all skill enrichments.
 
@@ -305,7 +313,9 @@ Some enrichments are always free:
 
  During AI enrichment, Azure AI Search calls the Azure AI services APIs for [built-in skills](cognitive-search-predefined-skills.md) that are based on Azure AI Vision, Translator, and Azure AI Language. 
 
-Billable built-in skills that make backend calls to Azure AI services include [Entity Linking](cognitive-search-skill-entity-linking-v3.md), [Entity Recognition](cognitive-search-skill-entity-recognition-v3.md), [Image Analysis](cognitive-search-skill-image-analysis.md), [Key Phrase Extraction](cognitive-search-skill-keyphrases.md), [Language Detection](cognitive-search-skill-language-detection.md), [OCR](cognitive-search-skill-ocr.md), [Personally Identifiable Information (PII) Detection](cognitive-search-skill-pii-detection.md), [Sentiment](cognitive-search-skill-sentiment-v3.md), and [Text Translation](cognitive-search-skill-text-translation.md).
+Billable built-in skills that make backend calls to Azure AI services include [Entity Linking](cognitive-search-skill-entity-linking-v3.md), [Entity Recognition](cognitive-search-skill-entity-recognition-v3.md), [Image Analysis](cognitive-search-skill-image-analysis.md), [Key Phrase Extraction](cognitive-search-skill-keyphrases.md), [Language Detection](cognitive-search-skill-language-detection.md), [OCR](cognitive-search-skill-ocr.md), [Personally Identifiable Information (PII) Detection](cognitive-search-skill-pii-detection.md), [Sentiment](cognitive-search-skill-sentiment-v3.md), [Text Translation](cognitive-search-skill-text-translation.md), and [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md). 
+
+A [query-time vectorizer](vector-search-how-to-configure-vectorizer.md) backed by the Azure AI Vision multimodal embedding model is also a billable enrichment.
 
 Image extraction is an Azure AI Search operation that occurs when documents are cracked prior to enrichment. Image extraction is billable on all tiers, except for 20 free daily extractions on the free tier. Image extraction costs apply to image files inside blobs, embedded images in other files (PDF and other app files), and for images extracted using [Document Extraction](cognitive-search-skill-document-extraction.md). For image extraction pricing, see the [Azure AI Search pricing page](https://azure.microsoft.com/pricing/details/search/).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchでのコグニティブサービスの接続の改善"
}
```

### Explanation
この変更は、Azure AI Searchにおけるコグニティブサービスの接続方法に関するドキュメントを更新したものです。主な変更点として、エンリッチメントパイプラインの構成における無償のトランザクション制限や請求に関連する情報が明確化されています。また、「AIマルチサービスアカウント」という用語が導入され、利用者が請求情報を提供する必要がある旨が説明されています。

具体的には、以下のような点が改善されています：
- AIエンリッチメントを利用する際のトランザクションの無料枠についての説明の修正・明確化。
- Azure AI Searchが内部でホスティングするリソースと、マーケティング目的の請求情報の提供の要件の分離。
- 一部の特定スキル（Azure OpenAIやAMLスキルを含む）における請求の例外についての説明。

これらの改善により、ユーザーはコグニティブサービスの使用に関連する設定や請求プロセスをより理解しやすくなります。ドキュメント全体で、AIマルチサービスアカウントやエンリッチメント操作の請求に関する詳細が整然と整理され、理解を助ける内容が追加されました。

## articles/search/search-reliability.md{#item-3e9b1a}

<details>
<summary>Diff</summary>
````diff
@@ -147,6 +147,7 @@ If you need redundancy at the request level, Azure provides several [load balanc
 + [Azure Traffic Manager](/azure/traffic-manager/traffic-manager-overview), used to route requests to multiple geo-located websites that are then backed by multiple search services. 
 + [Application Gateway](/azure/application-gateway/overview), used to load balance between servers in a region at the application layer.
 + [Azure Front Door](/azure/frontdoor/front-door-overview), used to optimize global routing of web traffic and provide global failover.
++ [Azure Load Balancer](/azure/load-balancer/load-balancer-overview), used to load balance between services in a backend pool.
 
 Some points to keep in mind when evaluating load balancing options:
 
@@ -164,6 +165,9 @@ Azure Traffic Manager is primarily used for routing network traffic across diffe
 
 Traffic Manager doesn't provide an endpoint for a direct connection to Azure AI Search, which means you can't put a search service directly behind Traffic Manager. Instead, the assumption is that requests flow to Traffic Manager, then to a search-enabled web client, and finally to a search service on the backend. The client and service are located in the same region. If one search service goes down, the search client starts failing, and Traffic Manager redirects to the remaining client.
 
+> [!NOTE]
+> If you are using Azure Load Balancer [health probes](/azure/load-balancer/load-balancer-custom-probe-overview) on a search service, you must use a HTTPS probe with `/ping` as the path.
+
 ![Diagram of search apps connecting through Azure Traffic Manager.][4]
 
 ## Data residency in a multi-region deployment
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスの信頼性の向上に関する説明の追加"
}
```

### Explanation
この変更は、Azure AI Searchに関連する検索サービスの信頼性を向上させるための情報を更新したものです。具体的には、ロードバランシングオプションに関する説明が強化されています。

主な更新内容は以下の通りです：
- Azureのロードバランシング技術として、**Azure Load Balancer**が新たに紹介されています。このツールは、バックエンドプールのサービス間で負荷分散を行うためのものであり、より堅牢なインフラストラクチャを提供します。
- **Azure Load Balancer**を使用する際の注意点として、健康診断プローブを使用する場合は、HTTPSプローブを用い、パスには`/ping`を指定する必要があることが明記されています。

これらの変更により、ユーザーはAzure検索サービスの冗長性や負荷分散技術について、より深く理解できるようになります。また、新しい情報は、検索サービスを利用する際の信頼性を向上させるための選択肢を明確に提供します。

## articles/search/vector-search-how-to-configure-vectorizer.md{#item-30ffd8}

<details>
<summary>Diff</summary>
````diff
@@ -9,14 +9,14 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 08/05/2024
+ms.date: 01/14/2025
 ---
 
 # Configure a vectorizer in a search index
 
-In Azure AI Search a *vectorizer* is software that performs vectorization, such as a deployed embedding model on Azure OpenAI, that converts text (or images) to vectors during query execution.
+In Azure AI Search a *vectorizer* is a component that performs vectorization using a deployed embedding model on Azure OpenAI or Azure AI Vision. It converts text (or images) to vectors during query execution.
 
-It's defined in a [search index](search-what-is-an-index.md), it applies to searchable vector fields, and it's used at query time to generate an embedding for a text or image query input. If instead you need to vectorize content as part of the indexing process, refer to [Integrated Vectorization (Preview)](vector-search-integrated-vectorization.md). For built-in vectorization during indexing, you can configure an indexer and skillset that calls an embedding model for your raw text content.
+It's defined in a [search index](search-what-is-an-index.md), it applies to searchable vector fields, and it's used at query time to generate an embedding for a text or image query input. If instead you need to vectorize content as part of the indexing process, refer to [integrated vectorization](vector-search-integrated-vectorization.md). For built-in vectorization during indexing, you can configure an indexer and skillset that calls an embedding model for your raw text or image content.
 
 To add a vectorizer to search index, you can use the index designer in Azure portal, or call the [Create or Update Index](/rest/api/searchservice/indexes/create-or-update) REST API, or use any Azure  SDK package that's updated to provide this feature.
 
@@ -28,14 +28,25 @@ Vectorizers are now generally available as long as you use a generally available
 
 + [An index with searchable vector fields](vector-search-how-to-create-index.md) on Azure AI Search.
 
-+ A deployed embedding model, such as **text-embedding-ada-002**, **text-embedding-3-small**, or **text-embedding-3-large** on Azure OpenAI. It's used to vectorize a query. It must be [identical to the embedding model used for the vector field](vector-search-integrated-vectorization.md#using-integrated-vectorization-in-queries) in your index. You can also use [models deployed from the Azure AI Foundry model catalog](vector-search-integrated-vectorization-ai-studio.md) or an [Azure AI Vision model](/azure/ai-services/computer-vision/concept-image-retrieval).
++ A deployed embedding model (see the next section).
 
-+ Permissions to use the embedding model. If you're using Azure OpenAI, the caller must have [Cognitive Services OpenAI User](/azure/ai-services/openai/how-to/role-based-access-control#azure-openai-roles) permissions. Or, you can provide an API key.
++ Permissions to use the embedding model. On Azure OpenAI, the caller must have [Cognitive Services OpenAI User](/azure/ai-services/openai/how-to/role-based-access-control#azure-openai-roles) permissions. Or, you can provide an API key.
 
 + [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) to send the query and accept a response.
 
 We recommend that you enable diagnostic logging on your search service to confirm vector query execution.
 
+## Supported embedding models
+
+The following table lists the embedding models that can be used with a vectorizer. Because you must use the [same embedding model for indexing and queries](vector-search-integrated-vectorization.md#using-integrated-vectorization-in-queries), vectorizers are paired with skills that generate embeddings during indexing. The table lists the skill associated with a particular vectorizer.
+
+| Vectorizer kind | Model names | Model provider | Associated skill |
+|-----------------|------------|----------------|------------------|
+| [`azureOpenAI`](vector-search-vectorizer-azure-open-ai.md) | text-embedding-ada-002, text-embedding-3 | Azure OpenAI | [AzureOpenAIEmbedding skill](cognitive-search-skill-azure-openai-embedding.md) |
+| [`aml`](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) | Facebook-DinoV2-Image-Embeddings, Cohere-embed-v3 | [Azure AI Foundry model catalog](vector-search-integrated-vectorization-ai-studio.md)  | [AML skill](cognitive-search-aml-skill.md) |
+| [`aiServicesVision`](vector-search-vectorizer-ai-services-vision.md) | [Multimodal embeddings 4.0 API](/azure/ai-services/computer-vision/concept-image-retrieval) | Azure AI Vision (through an Azure AI multi-service account) | [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) |
+| [`customWebApi`](vector-search-vectorizer-custom-web-api.md) | Any embedding model | Hosted externally | [Custom Web API skill](cognitive-search-custom-skill-web-api.md) |
+
 ## Try a vectorizer with sample data
 
 The [Import and vectorize data wizard](search-get-started-portal-import-vectors.md) reads files from Azure Blob storage, creates an index with chunked and vectorized fields, and adds a vectorizer. By design, the vectorizer that's created by the wizard is set to the same embedding model used to index the blob content.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトライザーの設定手順の詳細追加"
}
```

### Explanation
この変更では、Azure AI Searchにおけるベクトライザーの設定手順に関するドキュメントが更新されました。主に、ベクトライザーの定義や、利用する埋め込みモデルに関連する情報が強化されています。

主な変更点は以下の通りです：
- ベクトライザーの定義が明確になり、Azure OpenAIまたはAzure AI Visionにデプロイされた埋め込みモデルを使用して、クエリ実行時にテキストや画像をベクトルに変換することが強調されています。
- ベクトライザーの追加に必要な詳細ステップが記載され、AzureポータルのインデックスデザイナーやREST APIを用いてベクトライザーを追加する方法が説明されています。
- 使用可能な埋め込みモデルのリストが追加され、特定のベクトライザーに対してどのモデルが関連しているかが示されています。この情報は、モデルのペアリングがインデックス作成とクエリで同じ埋め込みモデルを使用する必要があることを補足しています。

これにより、ユーザーはベクトライザーの設定と埋め込みモデルの使用に関する理解を深め、より効果的にAzure AI Searchを活用できるようになります。また、新しい情報は、実際の使用シナリオにおける具体的な手法を示しており、実践的なガイダンスを提供します。


