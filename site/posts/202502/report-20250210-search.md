---
date: '2025-02-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4912a73...MicrosoftDocs:879fbd3
summary: このコード修正では、Azure Search と関連サービスのドキュメントに対して多くの更新と改善が行われました。主な新機能として、フルテキスト検索のイントロダクションが追加され、Azure.Search.Documents
  を用いた検索インデックスの活用法が説明されています。既存のクイックスタートガイドの改訂や用語の修正、ファイル名の変更が行われ、ドキュメントの一貫性が強化されました。特に破壊的変更はありませんが、用語の微調整や構成の見直しにより、ユーザーが必要な情報を容易に見つけられるようになっています。この更新は、Azure
  AI サービスによる検索機能の実装を明確にし、教育的価値を提供することを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4912a73...MicrosoftDocs:879fbd3){target="_blank"}

# ハイライト
このコード修正では、Azure Search と関連サービスのドキュメントに対して複数の更新と改善が行われました。新機能としては、フルテキスト検索のイントロダクションの追加があります。その他の変更として、既存のクイックスタートガイドの改訂や、ファイル名の変更、表記の修正などが挙げられます。

## 新機能
- フルテキスト検索イントロダクションの新しいファイルが追加され、Azure.Search.Documents を使用した検索インデックスの活用法や関連アルゴリズムについて説明されています。

## 破壊的変更
- 特に大きな破壊的変更は言及されていませんが、用語の微調整やファイル名の変更によりドキュメントの整理と一貫性が強化されています。

## その他の更新
- Azure AI サービスに関連する用語の修正と説明の明確化。
- C#、Java、JavaScript、Python、TypeScript 用フルテキスト検索クイックスタートのファイル名変更と内容更新。
- 文書の構成修正、見出しのレベル調整、著者情報の更新、日付の修正。
  
# インサイト
このドキュメントの修正では、技術者向けのナビゲーション効率を高め、一貫性と正確性を維持することに重点を置かれています。変更により、Azure AI サービスを使用した検索機能の実装がより明確に、かつ実践的に記述されました。

各プログラミング言語に特化したクイックスタートガイドは、開発者が特定の技術スタックに合った情報を迅速に見つけるのを助け、より深い理解を促進します。ファイル名の変更や構成の見直しにより、視覚的に明確な区分けがされたことで、ユーザーが必要な情報を容易に取り出せるようになっています。

新たに追加されたフルテキスト検索イントロダクションは、特に学習が切望されているフルテキスト検索の基礎を提供し、Apache Lucene や BM25 ランキングアルゴリズムの原則の理解を深めるものです。この更新は、Azure 上での効率的な検索プロジェクトの構築を後押しし、最新の技術トレンドにも対応します。

全体的に、このアップデートはユーザー教育に貢献し、Azure Search の機能を最大限に活用するための基礎を提供することを目的としています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | Azure AI サービスリソースの説明の更新 | modified | 14 | 14 | 28 | 
| [full-text-csharp.md](#item-2e943a) | minor update | C# フルテキスト検索クイックスタートのリネームと更新 | renamed | 12 | 11 | 23 | 
| [full-text-intro.md](#item-f655a1) | new feature | フルテキスト検索のイントロダクションの追加 | added | 26 | 0 | 26 | 
| [full-text-java.md](#item-d659f9) | minor update | Java フルテキスト検索クイックスタートのリネームと更新 | renamed | 14 | 13 | 27 | 
| [full-text-javascript.md](#item-568e3a) | minor update | JavaScript フルテキスト検索クイックスタートのリネームと更新 | renamed | 14 | 13 | 27 | 
| [full-text-python.md](#item-9bba1c) | minor update | Python フルテキスト検索クイックスタートのリネームと更新 | renamed | 18 | 17 | 35 | 
| [full-text-typescript.md](#item-6630e8) | minor update | TypeScript フルテキスト検索クイックスタートのリネームと更新 | renamed | 14 | 13 | 27 | 
| [search-get-started-text.md](#item-935941) | minor update | Azure SDKを使用したフルテキスト検索のクイックスタートの更新 | modified | 20 | 40 | 60 | 


# Modified Contents
## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -1,31 +1,31 @@
 ---
 title: Attach Azure AI services to a skillset
 titleSuffix: Azure AI Search
-description: Learn how to attach an Azure AI multi-service resource to an AI enrichment pipeline in Azure AI Search.
+description: Learn how to attach an Azure AI services resource to an AI enrichment pipeline in Azure AI Search.
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: how-to
-ms.date: 01/22/2025
+ms.date: 2/8/2025
 ---
 
-# Attach an Azure AI multi-service resource to a skillset in Azure AI Search
+# Attach an Azure AI services resource to a skillset in Azure AI Search
 
-If you're using built-in skills for optional [AI enrichment](cognitive-search-concept-intro.md) in Azure AI Search, you can enrich a small number of documents free of charge, limited to 20 transactions daily per index. For larger and more frequent workloads, you should attach a billable [Azure AI multi-service account](/azure/ai-services/multi-service-resource?pivots=azportal). 
+If you're using built-in skills for optional [AI enrichment](cognitive-search-concept-intro.md) in Azure AI Search, you can enrich a small number of documents free of charge, limited to 20 transactions daily per index. For larger and more frequent workloads, you should attach a billable [Azure AI multi-service resource](/azure/ai-services/multi-service-resource?pivots=azportal). 
 
-Azure AI Search uses dedicated, internally hosted Azure AI multi-service resources for built-in skills execution, but needs your multi-service account for billing purposes. 
+Azure AI Search uses dedicated, internally hosted Azure AI multi-service resources for built-in skills execution, but needs your multi-service resource for billing purposes. 
 
-A multi-service account provides a collection of Azure AI services, rather than individual services. Providing an account in an Azure AI Search [skillset](/rest/api/searchservice/skillsets/create) allows Microsoft to charge you for using these services:
+An Azure AI multi-service resource provides a collection of Azure AI services, rather than individual services. Providing a multi-service resource in an Azure AI Search [skillset](/rest/api/searchservice/skillsets/create) allows Microsoft to charge you for using these services:
 
 + [Azure AI Vision](/azure/ai-services/computer-vision/overview) for image analysis, optical character recognition (OCR), and multimodal embeddings
 + [Azure AI Language](/azure/ai-services/language-service/overview) for language detection, entity recognition, sentiment analysis, and key phrase extraction
 + [Azure AI Speech](/azure/ai-services/speech-service/overview) for speech to text and text to speech
 + [Azure AI Translator](/azure/ai-services/translator/translator-overview) for machine text translation
 
-Exceptions to billing through the multi-service account include [AzureOpenAIEmbedding](cognitive-search-skill-azure-openai-embedding.md) or the [AML skill](cognitive-search-aml-skill.md) billing. Azure AI Search doesn't internally host models from Azure OpenAI or the Azure AI Foundry model catalog. Usage for AML and Azure OpenAI skills and vectorizers are through [Azure OpenAI pay-as-you-go pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing) and [Azure Machine Learning pay-as-you-go pricing](https://azure.microsoft.com/pricing/details/machine-learning/), respectively. A few other skills, such as Text Split and Text Merge, aren't billable.
+Exceptions to billing through the multi-service resource include [AzureOpenAIEmbedding](cognitive-search-skill-azure-openai-embedding.md) or the [AML skill](cognitive-search-aml-skill.md) billing. Azure AI Search doesn't internally host models from Azure OpenAI or the Azure AI Foundry model catalog. Usage for AML and Azure OpenAI skills and vectorizers are through [Azure OpenAI pay-as-you-go pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing) and [Azure Machine Learning pay-as-you-go pricing](https://azure.microsoft.com/pricing/details/machine-learning/), respectively. A few other skills, such as Text Split and Text Merge, aren't billable.
 
 To attach an Azure AI multi-resource, you must provide connection information in the skillset. You can use a key on the connection, or implement a keyless approach that's currently in preview.
 
@@ -34,7 +34,7 @@ To attach an Azure AI multi-resource, you must provide connection information in
 
 ## Prerequisites
 
-+ Connectivity over a public endpoint, unless your search service meets the creation date, tier, and region requirements for private connections to an Azure AI multi-service account.
++ Connectivity over a public endpoint, unless your search service meets the creation date, tier, and region requirements for private connections to an Azure AI multi-service resource.
 
 > [!NOTE]
 > If your Azure AI resource is configured to use a private endpoint, Azure AI Search can connect [using a shared private link](search-indexer-howto-access-private.md) For more information, see the [requirements and limits for using shared private links](search-limits-quotas-capacity.md#shared-private-link-resource-limits).
@@ -116,7 +116,7 @@ Azure AI Search can also charge for transactions using the Azure AI multi-servic
 
 There are two supported key types: `#Microsoft.Azure.Search.CognitiveServicesByKey` which calls the regional endpoint and `"#Microsoft.Azure.Search.AIServicesByKey` which calls the subdomain. We recommend using `AIServicesByKey` for its shared private link support and ability to function with no regional requirements relative to the search service.
 
-The Azure AI multi-service account must be in the same region as Azure AI Search. For more information, see [Regions supported by Azure AI Search](search-region-support.md#azure-public-regions) and choose a region that provides AI services integration.
+The Azure AI multi-service resource must be in the same region as Azure AI Search. For more information, see [Regions supported by Azure AI Search](search-region-support.md#azure-public-regions) and choose a region that provides AI services integration.
 
 If you leave the `cognitiveServices` property unspecified, your search service attempts to use the free enrichments available to your indexer on a daily basis. Execution of billable skills stops at 20 transactions per indexer invocation and a "Time Out" message appears in indexer execution history.
 
@@ -130,14 +130,14 @@ If you leave the `cognitiveServices` property unspecified, your search service a
 
 1. Add the key to a skillset definition:
 
-   + If using an [Import data wizard](search-import-data-portal.md), create or select the Azure AI account. The wizard adds the resource key to your skillset definition. 
+   + If using an [Import data wizard](search-import-data-portal.md), create or select the Azure AI services resource. The wizard adds the resource key to your skillset definition. 
 
    + For a new or existing skillset, provide the key in skillset definition.
 
   :::image type="content" source="media/cognitive-search-attach-cognitive-services/attach-existing2.png" alt-text="Screenshot of the key page." border="true":::
 
 > [!NOTE]
-> Azure portal currently automatically attaches key of type `#Microsoft.Azure.Search.CognitiveServicesByKey`.
+> Azure portal automatically attaches the key of type `#Microsoft.Azure.Search.CognitiveServicesByKey`.
 
 ### [**REST**](#tab/cogkey-rest)
 
@@ -208,7 +208,7 @@ SearchIndexerSkillset skillset = CreateOrUpdateDemoSkillSet(indexerClient, skill
 
 ## Remove the key
 
-Enrichments are billable operations. If you no longer need to call Azure AI services, follow these instructions to remove the multi-service key and prevent use of the external resource. Without the key, the skillset reverts to the default allocation of 20 free transactions per indexer, per day. Execution of billable skills stops at 20 transactions and a "Time Out" message appears in indexer execution history when the allocation is used up.
+Enrichments are billable operations. If you no longer need to call Azure AI services, follow these instructions to remove the multi-service key and prevent use of the external resource. Without the key, the skillset reverts to the default allocation of 20 free transactions per indexer, per day. Execution of billable skills stops at 20 transactions and a "Time Out" message appears in indexer execution history when the allocation is used.
 
 ### [**Azure portal**](#tab/portal-remove)
 
@@ -280,9 +280,9 @@ Billing goes into effect when API calls to Azure AI services resources exceed 20
 
 Keyless and key-based connections are used for billing, but not for enrichment operations' connections. 
 
-For key-based connections, a search service [connects over the internal network](search-security-overview.md#internal-traffic) to an Azure AI services resource that's located in the [same physical region](search-region-support.md). Most regions that offer Azure AI Search also offer other Azure AI services such as Language. If you attempt AI enrichment in a region that doesn't have both services, you'll see this message: "Provided key isn't a valid CognitiveServices type key for the region of your search service."
+For key-based connections, a search service [connects over the internal network](search-security-overview.md#internal-traffic) to an Azure AI services resource located in the [same physical region](search-region-support.md). Most regions that offer Azure AI Search also offer other Azure AI services such as Language. If you attempt AI enrichment in a region that doesn't have both services, you see this message: "Provided key isn't a valid CognitiveServices type key for the region of your search service."
 
-For keyless connections, a search service authenticates using its identity and role assignment, targeting an Azure AI multi-service resource that's specified as a fully-qualified URI, having a unique subdomain in that URI.
+For keyless connections, a search service authenticates using its identity and role assignment, targeting an Azure AI multi-service resource specified as a fully-qualified URI, having a unique subdomain in that URI.
 
 Indexers can be configured to run in a [private execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment) for dedicated processing using just the search nodes of your own search service. Even if you're using private execution environment, Azure AI Search still uses its internally provisioned Azure AI multiservice resource to perform all skill enrichments.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI サービスリソースの説明の更新"
}
```

### Explanation
この変更は、Azure AI サービスを Azure AI Search のスキルセットに接続する方法に関する文書の内容を更新するものです。特に、"multi-service account" という用語を "multi-service resource" に変更し、関連する説明を明確にしました。また、日付のフォーマットも修正され、新しい日付が提供されています。これにより、ドキュメントの正確性と一貫性が向上し、ユーザーに対する情報提供が強化されています。

具体的には、Azure AI サービスリソースの機能や、リソースをスキルセットに提供する際の料金などについての記述が見直されています。これらの変更は、Azure AI サービスを利用する際の最新の情報を反映しており、ユーザーがより正確にリソースを管理できるようにしています。また、文章の流れや表記も改善されており、情報へのアクセスが容易になっています。

## articles/search/includes/quickstarts/full-text-csharp.md{#item-2e943a}

<details>
<summary>Diff</summary>
````diff
@@ -1,18 +1,19 @@
 ---
-author: HeidiSteen
-ms.author: heidist
+manager: nitinme
+author: eric-urban
+ms.author: eur
 ms.service: azure-ai-search
-ms.custom:
-  - ignite-2023
 ms.topic: include
-ms.date: 10/07/2024
+ms.date: 2/8/2025
 ---
 
+[!INCLUDE [Full text introduction](full-text-intro.md)]
+
 Build a console application using the [Azure.Search.Documents](/dotnet/api/overview/azure/search.documents-readme) client library to create, load, and query a search index.
 
 Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/v11) to start with a finished project or follow these steps to create your own.
 
-#### Set up your environment
+## Set up your environment
 
 1. Start Visual Studio and create a new project for a console app.
 
@@ -24,7 +25,7 @@ Alternatively, you can [download the source code](https://github.com/Azure-Sampl
 
 1. Select **Install** to add the assembly to your project and solution.
 
-#### Create a search client
+## Create a search client
 
 1. In *Program.cs*, change the namespace to `AzureSearch.SDK.Quickstart.v11` and then add the following `using` directives.
 
@@ -58,7 +59,7 @@ Alternatively, you can [download the source code](https://github.com/Azure-Sampl
     }
     ```
 
-#### Create an index
+## Create an index
 
 This quickstart builds a Hotels index that you'll load with hotel data and execute queries against. In this step, define the fields in the index. Each field definition includes a name, data type, and attributes that determine how the field is used.
 
@@ -167,7 +168,7 @@ In this example, synchronous methods of the *Azure.Search.Documents* library are
     }
    ```
 
-#### Load documents
+## Load documents
 
 Azure AI Search searches over content stored in the service. In this step, you'll load JSON documents that conform to the hotel index you just created.
 
@@ -303,7 +304,7 @@ When uploading documents, you must use an [IndexDocumentsBatch](/dotnet/api/azur
 
     The 2-second delay compensates for indexing, which is asynchronous, so that all documents can be indexed before the queries are executed. Coding in a delay is typically only necessary in demos, tests, and sample applications.
 
-#### Search an index
+## Search an index
 
 You can get query results as soon as the first document is indexed, but actual testing of your index should wait until all documents are indexed.
 
@@ -461,7 +462,7 @@ The previous queries show multiple [ways of matching terms in a query](/azure/se
 
 Full text search and filters are performed using the [SearchClient.Search](/dotnet/api/azure.search.documents.searchclient.search) method. A search query can be passed in the `searchText` string, while a filter expression can be passed in the [Filter](/dotnet/api/azure.search.documents.searchoptions.filter) property of the [SearchOptions](/dotnet/api/azure.search.documents.searchoptions) class. To filter without searching, just pass `"*"` for the `searchText` parameter of the [Search](/dotnet/api/azure.search.documents.searchclient.search) method. To search without filtering, leave the `Filter` property unset, or don't pass in a `SearchOptions` instance at all.
 
-#### Run the program
+## Run the program
 
 Press **F5** to rebuild the app and run the program in its entirety.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# フルテキスト検索クイックスタートのリネームと更新"
}
```

### Explanation
この変更は、C# 言語を使用したフルテキスト検索のクイックスタートガイドのファイル名を変更し、いくつかの更新を加えるものです。元のファイル名は「dotnet.md」から「full-text-csharp.md」に変更され、これにより内容が明確に C# に特化したものであることが示されています。

さらに、文書の著者やマネージャー名が新しいものに更新され、更新日も修正されています。文中の見出しが「####」から「##」に変更されており、これにより構造が改善され、セクションがより視覚的に目立つようになっています。これらの変更は、ユーザーのナビゲーション体験を向上させ、最新の情報を提供するためのものです。

全体として、これらの更新は、ドキュメントの一貫性と正確性を保ちながら、C# を使用する開発者にとっての利便性を向上させています。

## articles/search/includes/quickstarts/full-text-intro.md{#item-f655a1}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,26 @@
+---
+manager: nitinme
+author: eric-urban
+ms.author: eur
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 2/8/2025
+---
+
+Learn how to use the *Azure.Search.Documents* client library in an Azure SDK to create, load, and query a search index using sample data for [full text search](../../search-lucene-query-architecture.md). Full text search uses Apache Lucene for indexing and queries, and a BM25 ranking algorithm for scoring results.
+
+This quickstart creates and queries a small hotels-quickstart index containing data about 4 hotels.
+
+## Prerequisites
+
++ An Azure account with an active subscription. You can [create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?icid=azurefreeaccount).
+
++ An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
+
++ An API key and service endpoint for your service. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch).
+
+  In the **Overview** section, copy the URL and save it to a text editor for a later step. An example endpoint might look like `https://mydemo.search.windows.net`.
+
+  In the **Settings** > **Keys** section, copy and save an admin key for full rights to create and delete objects. There are two interchangeable primary and secondary keys. Choose either one.
+
+  :::image type="content" source="../../media/search-get-started-rest/get-url-key.png" alt-text="Screenshot that shows the HTTP endpoint and the primary and secondary API key locations.":::
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "フルテキスト検索のイントロダクションの追加"
}
```

### Explanation
この変更は、「full-text-intro.md」という新しいファイルを追加するもので、Azureのクライアントライブラリである *Azure.Search.Documents* を使用し、検索インデックスを作成、読み込み、クエリを実行する方法を学ぶためのリソースを提供します。このクイックスタートは、フルテキスト検索に関するサンプルデータを用いて、小規模な「hotels-quickstart」インデックスを作成してクエリを実行します。

新しいドキュメントには、フルテキスト検索の基礎として Apache Lucene を利用したインデックス作成とクエリ実行、BM25 ランキングアルゴリズムについての情報が含まれています。準備が整ったユーザーがこのクイックスタートを実行できるように、Azure アカウント、Azure AI Search サービス、および API キーとエンドポイントに関する前提条件も詳述されています。

前提条件には、Azure アカウントの作成方法や、サービスエンドポイントの取得手順が含まれています。また、ビジュアルリソースとしてスクリーンショットが提供され、ユーザーが必要な情報を容易に見つけられるようサポートされています。この追加により、ユーザーはフルテキスト検索を使用するための基礎を理解し、Azure のサービスを活用するための第一歩を踏み出すことができます。

## articles/search/includes/quickstarts/full-text-java.md{#item-d659f9}

<details>
<summary>Diff</summary>
````diff
@@ -1,26 +1,27 @@
 ---
-author: HeidiSteen
-ms.author: heidist
+manager: nitinme
+author: eric-urban
+ms.author: eur
 ms.service: azure-ai-search
-ms.custom:
-  - ignite-2023
 ms.topic: include
-ms.date: 01/07/2025
+ms.date: 2/8/2025
 ---
 
+[!INCLUDE [Full text introduction](full-text-intro.md)]
+
 Build a Java console application using the [Azure.Search.Documents](/java/api/overview/azure/search) library to create, load, and query a search index. 
 
 Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
 
-#### Set up your environment
+## Set up your environment
 
 Use the following tools to create this quickstart.
 
 + [Visual Studio Code with the Java extension](https://code.visualstudio.com/docs/java/extensions)
 
 + [Java 11 SDK](/java/azure/jdk/)
 
-#### Create the project
+## Create the project
 
 1. Start Visual Studio Code.
 
@@ -56,7 +57,7 @@ Use the following tools to create this quickstart.
 
 1. Open the folder you created the project in.
 
-#### Specify Maven dependencies
+## Specify Maven dependencies
 
 1. Open the *pom.xml* file and add the following dependencies.
 
@@ -88,7 +89,7 @@ Use the following tools to create this quickstart.
     <maven.compiler.target>1.11</maven.compiler.target>
     ```
 
-#### Create a search client
+## Create a search client
 
 1. Open the `App` class under **src**, **main**, **java**, **azure**, **search**, **sample**. Add the following import directives.
 
@@ -137,7 +138,7 @@ Use the following tools to create this quickstart.
     }
     ```
 
-#### Create an index
+## Create an index
 
 This quickstart builds a Hotels index that you'll load with hotel data and execute queries against. In this step, define the fields in the index. Each field definition includes a name, data type, and attributes that determine how the field is used.
 
@@ -324,7 +325,7 @@ Whether you use the basic `SearchField` API or either one of the helper models,
         .setSuggesters(new SearchSuggester("sg", Arrays.asList("HotelName"))));
     ```
 
-#### Load documents
+## Load documents
 
 Azure AI Search searches over content stored in the service. In this step, you'll load JSON documents that conform to the hotel index you just created.
 
@@ -453,7 +454,7 @@ Once you initialize the `IndexDocumentsBatch` object, you can send it to the ind
 
 The 2-second delay compensates for indexing, which is asynchronous, so that all documents can be indexed before the queries are executed. Coding in a delay is typically only necessary in demos, tests, and sample applications.
 
-#### Search an index
+## Search an index
 
 You can get query results as soon as the first document is indexed, but actual testing of your index should wait until all documents are indexed.
 
@@ -583,7 +584,7 @@ The previous queries show multiple ways of matching terms in a query: full-text
 
 Full text search and filters are performed using the [SearchClient.search](/java/api/com.azure.search.documents.searchclient#com-azure-search-documents-searchclient-search(java-lang-string)) method. A search query can be passed in the `searchText` string, while a filter expression can be passed in the `filter` property of the [SearchOptions](/java/api/com.azure.search.documents.models.searchoptions) class. To filter without searching, just pass "*" for the `searchText` parameter of the `search` method. To search without filtering, leave the `filter` property unset, or don't pass in a `SearchOptions` instance at all.
 
-### Run the program
+## Run the program
 
 Press F5 to rebuild the app and run the program in its entirety.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java フルテキスト検索クイックスタートのリネームと更新"
}
```

### Explanation
この変更は、Java 言語を使用したフルテキスト検索のクイックスタートガイドのファイル名を「java.md」から「full-text-java.md」に変更し、いくつかの内容を更新したものです。これにより、ドキュメントがより特化したものとなり、Java に関する情報が強調されます。

変更された内容には、著者やマネージャーの名前、更新日が新しいものに修正されています。また、文中の見出しが「####」から「##」に変更されており、これにより構成が改善され、セクションがよりはっきりと区分しやすくなっています。さらに、クイックスタートの導入部分に新しく「フルテキスト検索のイントロダクション」というリンクが追加され、ユーザーが関連情報に容易にアクセスできるようになっています。

全体として、これらの変更は、Java 開発者にとっての文書の一貫性と使いやすさを向上させ、最新の情報を提供することを目的としています。これにより、ユーザーは Java 環境でのフルテキスト検索の実装に必要な手続きを正確に理解することができるでしょう。

## articles/search/includes/quickstarts/full-text-javascript.md{#item-568e3a}

<details>
<summary>Diff</summary>
````diff
@@ -1,26 +1,27 @@
 ---
-author: HeidiSteen
-ms.author: heidist
+manager: nitinme
+author: eric-urban
+ms.author: eur
 ms.service: azure-ai-search
-ms.custom:
-  - ignite-2023
 ms.topic: include
-ms.date: 10/07/2024
+ms.date: 2/8/2025
 ---
 
+[!INCLUDE [Full text introduction](full-text-intro.md)]
+
 Build a Node.js application using the [@azure/search-documents](/javascript/api/overview/azure/search-documents-readme) library to create, load, and query a search index. 
 
 Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
 
-#### Set up your environment
+## Set up your environment
 
 We used the following tools to create this quickstart.
 
 + [Visual Studio Code](https://code.visualstudio.com), which has built-in support for creating JavaScript apps
 
 + [Node.js](https://nodejs.org) and [npm](https://www.npmjs.com)
 
-#### Create the project
+## Create the project
 
 1. Start Visual Studio Code.
 
@@ -84,7 +85,7 @@ We used the following tools to create this quickstart.
 
 Replace the `YOUR-SEARCH-SERVICE-URL` value with the name of your search service endpoint URL. Replace `<YOUR-SEARCH-ADMIN-API-KEY>` with the admin key you recorded earlier. 
 
-#### Create index.js file
+## Create index.js file
 
 Next we create an *index.js* file, which is the main file that hosts our code.
 
@@ -127,7 +128,7 @@ main().catch((err) => {
 
 With that in place, we're ready to create an index.
 
-#### Create index 
+## Create index 
 
 Create a file *hotels_quickstart_index.json*. This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
 
@@ -310,7 +311,7 @@ let index = await indexClient.createIndex(indexDefinition);
 console.log(`Index named ${index.name} has been created.`);
 ```
 
-#### Run the sample
+## Run the sample
 
 At this point, you're ready to run the sample. Use a terminal window to run the following command:
 
@@ -328,7 +329,7 @@ Open the **Overview** of your search service in the Azure portal. Select the **I
 
 In the next step, you'll add data to index. 
 
-#### Load documents 
+## Load documents 
 
 In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this case, we'll programatically push the documents to the index.
 
@@ -458,7 +459,7 @@ To have the program wait for one second, call the `sleep` function like below:
 sleep(1000);
 ```
 
-#### Search an index
+## Search an index
 
 With an index created and documents uploaded, you're ready to send queries to the index. In this section, we send five different queries to the search index to demonstrate different pieces of query functionality available to you.
 
@@ -551,6 +552,6 @@ let documentResult = await searchClient.getDocument(key='3')
 console.log(`HotelId: ${documentResult.HotelId}; HotelName: ${documentResult.HotelName}`)
 ```
 
-#### Run the sample
+## Run the sample again
 
 Run the program by using `node index.js`. Now, in addition to the previous steps, the queries are sent and the results written to the console.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript フルテキスト検索クイックスタートのリネームと更新"
}
```

### Explanation
この変更は、JavaScript に基づくフルテキスト検索のクイックスタートガイドのファイル名を「javascript.md」から「full-text-javascript.md」に変更し、いくつかの内容を更新したものです。これにより、ファイル名がより明確になり、JavaScript 利用者に特化した内容であることが強調されています。

具体的な変更には、著者情報や更新日が新たに設定され、文書の構成が改良されています。また、セクション見出しが「####」から「##」に変わり、より可読性が高く、視覚的に整理されています。新たに追加された「フルテキスト検索のイントロダクション」というセクションが、関連情報へのリンクとして盛り込まれています。

内容的には、Node.js アプリケーションを構築する手順や、インデックスの作成、ドキュメントのアップロード、検索クエリの実行手法が詳しく解説されています。これにより、開発者はこのクイックスタートを通じて、Azure AI Search サービスの利用方法について深く理解できるようになります。

全体的に、このリファクタリングにより、ユーザーが JavaScript 環境でフルテキスト検索を効果的に利用できるようにすることを目指しています。

## articles/search/includes/quickstarts/full-text-python.md{#item-9bba1c}

<details>
<summary>Diff</summary>
````diff
@@ -1,18 +1,19 @@
 ---
-author: HeidiSteen
-ms.author: heidist
+manager: nitinme
+author: eric-urban
+ms.author: eur
 ms.service: azure-ai-search
-ms.custom:
-  - ignite-2023
 ms.topic: include
-ms.date: 10/07/2024
+ms.date: 2/8/2025
 ---
 
+[!INCLUDE [Full text introduction](full-text-intro.md)]
+
 Use a Jupyter notebook and the [azure-search-documents](/python/api/overview/azure/search-documents-readme) library in the Azure SDK for Python to create, load, and query a search index. 
 
 Alternatively, you can download and run a [finished notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart).
 
-#### Set up your environment
+## Set up your environment
 
 Use [Visual Studio Code with the Python extension](https://code.visualstudio.com/docs/languages/python), or an equivalent IDE, with Python 3.10 or later.
 
@@ -30,7 +31,7 @@ We recommend a virtual environment for this quickstart:
 
 It can take a minute to set up. If you run into problems, see [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments).
 
-#### Install packages and set variables
+## Install packages and set variables
 
 1. Install packages, including [azure-search-documents](/python/api/azure-search-documents). 
 
@@ -48,7 +49,7 @@ It can take a minute to set up. If you run into problems, see [Python environmen
     index_name: str = "hotels-quickstart"
     ```
 
-#### Create an index
+## Create an index
 
 ```python
 from azure.core.credentials import AzureKeyCredential
@@ -98,7 +99,7 @@ result = index_client.create_or_update_index(index)
 print(f' {result.name} created')
 ```
 
-#### Create a documents payload
+## Create a documents payload
 
 Use an [index action](/python/api/azure-search-documents/azure.search.documents.models.indexaction) for the operation type, such as upload or merge-and-upload. Documents originate from the [HotelsData](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toAzureSearch.JSON) sample on GitHub.
 
@@ -184,7 +185,7 @@ documents = [
 ]
 ```
 
-#### Upload documents
+## Upload documents
 
 ```python
 # Upload documents to the index
@@ -201,7 +202,7 @@ except Exception as ex:
     endpoint=search_endpoint, credential=credential)
 ```
 
-#### Run your first query
+## Run your first query
 
 Use the *search* method of the [search.client class](/python/api/azure-search-documents/azure.search.documents.searchclient).
 
@@ -221,7 +222,7 @@ for result in results:
     print(f"Description: {result['Description']}")
 ```
 
-#### Run a term query
+## Run a term query
 
 The next query adds whole terms to the search expression ("wifi"). This query specifies that results contain only those fields in the `select` statement. Limiting the fields that come back minimizes the amount of data sent back over the wire and reduces search latency.
 
@@ -238,7 +239,7 @@ for result in results:
     print(f"Description: {result['Description']}")
 ```
 
-#### Add a filter
+## Add a filter
 
 Add a filter expression, returning only those hotels with a rating greater than four, sorted in descending order.
 
@@ -254,7 +255,7 @@ for result in results:
     print("{}: {} - {} rating".format(result["HotelId"], result["HotelName"], result["Rating"]))
 ```
 
-#### Add field scoping
+## Add field scoping
 
 Add `search_fields` to scope query execution to specific fields.
 
@@ -269,7 +270,7 @@ for result in results:
     print("{}: {}".format(result["HotelId"], result["HotelName"]))
 ```
 
-#### Add facets
+## Add facets
 
 Facets are generated for positive matches found in search results. There are no zero matches. If search results don't include the term *wifi*, then *wifi* doesn't appear in the faceted navigation structure.
 
@@ -283,7 +284,7 @@ for facet in facets["Category"]:
     print("    {}".format(facet))
 ```
 
-#### Look up a document
+## Look up a document
 
 Return a document based on its key. This operation is useful if you want to provide drill through when a user selects an item in a search result.
 
@@ -297,7 +298,7 @@ print("Rating: {}".format(result["Rating"]))
 print("Category: {}".format(result["Category"]))
 ```
 
-#### Add autocomplete
+## Add autocomplete
 
 Autocomplete can provide potential matches as the user types into the search box.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python フルテキスト検索クイックスタートのリネームと更新"
}
```

### Explanation
この変更は、Python を使用したフルテキスト検索のクイックスタートガイドのファイル名を「python.md」から「full-text-python.md」に変更し、いくつかの内容を更新したものです。ファイル名の変更により、Python 開発者向けの特化した情報がより明確に示されています。

具体的には、著者や管理者に関する情報、更新日が更新され、初めに「フルテキスト検索のイントロダクション」というリンクを追加することで、関連情報へのアクセスが容易になっています。また、セクション見出しの形式が「####」から「##」に変更されており、文書の構造がより整理され、視覚的な可読性も向上しています。

変更内容としては、Jupyter ノートブックを用いてクイックスタートを進める手順や、Azure SDK for Pythonを利用したインデックスの作成、ドキュメントのアップロード方法、クエリの実行手法が詳述されています。これにより、ユーザーは Python 環境で Azure AI Search サービスを効果的に利用できるように、より具体的な手順とコーディング例が提供されています。

この更新は、Python 開発者がフルテキスト検索機能を最大限に活用できるような支援を目的としており、ドキュメント全体の整合性を高め、最新の情報を提供するものです。

## articles/search/includes/quickstarts/full-text-typescript.md{#item-6630e8}

<details>
<summary>Diff</summary>
````diff
@@ -1,18 +1,19 @@
 ---
-author: HeidiSteen
-ms.author: heidist
+manager: nitinme
+author: eric-urban
+ms.author: eur
 ms.service: azure-ai-search
-ms.custom:
-  - ignite-2023
 ms.topic: include
-ms.date: 10/07/2024
+ms.date: 2/8/2025
 ---
 
+[!INCLUDE [Full text introduction](full-text-intro.md)]
+
 Build a Node.js application using the [@azure/search-documents](/javascript/api/overview/azure/search-documents-readme) library to create, load, and query a search index. 
 
 Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
 
-#### Set up your environment
+## Set up your environment
 
 We used the following tools to create this quickstart.
 
@@ -22,7 +23,7 @@ We used the following tools to create this quickstart.
 
 * [TypeScript](https://www.typescriptlang.org/download/)
 
-#### Create the project
+## Create the project
 
 1. Start Visual Studio Code.
 
@@ -86,7 +87,7 @@ We used the following tools to create this quickstart.
 
 Replace the `YOUR-SEARCH-SERVICE-URL` value with the name of your search service endpoint URL. Replace `<YOUR-SEARCH-ADMIN-API-KEY>` with the admin key you recorded earlier. 
 
-#### Create index.ts file
+## Create index.ts file
 
 Next we create an *index.ts* file, which is the main file that hosts our code.
 
@@ -140,7 +141,7 @@ main().catch((err) => {
 
 With that in place, we're ready to create an index.
 
-#### Create index
+## Create index
 
 Create a file *hotels_quickstart_index.json*. This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
 
@@ -332,7 +333,7 @@ let index = await indexClient.createIndex(hotelIndexDefinition);
 console.log(`Index named ${index.name} has been created.`);
 ```
 
-#### Run the sample
+## Run the sample
 
 At this point, you're ready to build and run the sample. Use a terminal window to run the following commands to build your source with `tsc` then run your source with `node`:
 
@@ -351,7 +352,7 @@ Open the **Overview** of your search service in the Azure portal. Select the **I
 
 In the next step, you'll add data to index. 
 
-#### Load documents 
+## Load documents 
 
 In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this case, we'll programatically push the documents to the index.
 
@@ -497,7 +498,7 @@ To have the program wait for one second, call the `sleep` function:
 sleep(1000);
 ```
 
-#### Search an index
+## Search an index
 
 With an index created and documents uploaded, you're ready to send queries to the index. In this section, we send five different queries to the search index to demonstrate different pieces of query functionality available to you.
 
@@ -597,6 +598,6 @@ let documentResult = await searchClient.getDocument('3')
 console.log(`HotelId: ${documentResult.HotelId}; HotelName: ${documentResult.HotelName}`)
 ```
 
-#### Rerun the sample
+## Rerun the sample
 
 Build and run the program with `tsc && node index.ts`. Now, in addition to the previous steps, the queries are sent and the results written to the console.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScript フルテキスト検索クイックスタートのリネームと更新"
}
```

### Explanation
この変更は、TypeScript を使用したフルテキスト検索のクイックスタートガイドのファイル名を「typescript.md」から「full-text-typescript.md」に変更し、いくつかの内容を更新したものです。ファイル名の変更により、TypeScript に特化したガイドであることがより明確に示されています。

具体的な変更内容としては、著者や管理者に関する情報の刷新、更新日が変更され、「フルテキスト検索のイントロダクション」というリンクが追加されています。また、セクション見出しが「####」から「##」に変更されており、文書の読みやすさが向上しています。

内容的には、Node.js アプリケーションを構築する手法や、インデックスの作成、ドキュメントのアップロード、クエリの実行手順が詳述されています。これにより、開発者はこのクイックスタートを通じて、Azure AI Search サービスを TypeScript 環境で効果的に利用するための具体的な手順とコーディング例を確認できるようになります。

全体として、この文書の更新は、TypeScript 利用者が Azure AI Search の機能を最大限に活用できるよう支援することを目的としています。変更により、ドキュメントの整合性が高まり、最新の情報が提供されています。

## articles/search/search-get-started-text.md{#item-935941}

<details>
<summary>Diff</summary>
````diff
@@ -3,8 +3,8 @@ title: 'Quickstart: Full text search using the Azure SDKs'
 titleSuffix: Azure AI Search
 description: "Learn how to create, load, and query a search index using the Azure SDKs for .NET, Python, Java, and JavaScript."
 manager: nitinme
-author: HeidiSteen
-ms.author: heidist
+author: eric-urban
+ms.author: eur
 ms.service: azure-ai-search
 ms.custom:
   - devx-track-dotnet
@@ -14,63 +14,43 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: quickstart
-ms.date: 01/07/2025
+zone_pivot_groups: search-quickstart-full-text
+ms.date: 2/8/2025
 ---
 
 # Quickstart: Full text search using the Azure SDKs
 
-Learn how to use the *Azure.Search.Documents* client library in an Azure SDK to create, load, and query a search index using sample data for [full text search](search-lucene-query-architecture.md). Full text search uses Apache Lucene for indexing and queries, and a BM25 ranking algorithm for scoring results.
+::: zone pivot="programming-language-csharp"
 
-This quickstart creates and queries a small hotels-quickstart index containing data about 4 hotels.
+[!INCLUDE [C# quickstart](includes/quickstarts/full-text-csharp.md)]
 
-This quickstart has steps for the following SDKs:
+::: zone-end
 
-+ [Azure SDK for .NET](?tabs=dotnet#create-load-and-query-an-index)
-+ [Azure SDK for Python](?tabs=python#create-load-and-query-an-index)
-+ [Azure SDK for Java](?tabs=java#create-load-and-query-an-index)
-+ [Azure SDK for JavaScript/TypeScript](?tabs=javascript#create-load-and-query-an-index)
+::: zone pivot="programming-language-java"
 
-## Prerequisites
+[!INCLUDE [Java quickstart](includes/quickstarts/full-text-java.md)]
 
-+ An Azure account with an active subscription. You can [create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?icid=azurefreeaccount).
+::: zone-end
 
-+ An Azure AI Search service. [Create a service](search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
+::: zone pivot="programming-language-javascript"
 
-+ An API key and service endpoint for your service. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch).
+[!INCLUDE [JavaScript quickstart](includes/quickstarts/full-text-javascript.md)]
 
-  In the **Overview** section, copy the URL and save it to a text editor for a later step. An example endpoint might look like `https://mydemo.search.windows.net`.
+::: zone-end
 
-  In the **Settings** > **Keys** section, copy and save an admin key for full rights to create and delete objects. There are two interchangeable primary and secondary keys. Choose either one.
+::: zone pivot="programming-language-python"
 
-  :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot that shows the HTTP endpoint and the primary and secondary API key locations.":::
+[!INCLUDE [Python SDK quickstart](includes/quickstarts/full-text-python.md)]
 
-## Create, load, and query an index
+::: zone-end
 
-Choose a programming language for the next step. The **Azure.Search.Documents** client libraries are available in Azure SDKs for .NET, Python, Java, and JavaScript/TypeScript.
+::: zone pivot="programming-language-typescript"
 
-## [**.NET**](#tab/dotnet)
+[!INCLUDE [TypeScript quickstart](includes/quickstarts/full-text-typescript.md)]
 
-[!INCLUDE [dotnet-sdk-quickstart](includes/quickstarts/dotnet.md)]
+::: zone-end
 
-## [**Python**](#tab/python)
-
-[!INCLUDE [python-sdk-quickstart](includes/quickstarts/python.md)]
-
-## [**Java**](#tab/java)
-
-[!INCLUDE [java-sdk-quickstart](includes/quickstarts/java.md)]
-
-## [**JavaScript**](#tab/javascript)
-
-[!INCLUDE [javascript-sdk-quickstart](includes/quickstarts/javascript.md)]
-
-## [**TypeScript**](#tab/typescript)
-
-[!INCLUDE [typescript-sdk-quickstart](includes/quickstarts/typescript.md)]
-
----
-
-## Clean up resources
+## Clean-up resources
 
 When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure SDKを使用したフルテキスト検索のクイックスタートの更新"
}
```

### Explanation
この変更は、「Azure SDKを使用したフルテキスト検索のクイックスタート」に関する文書の改訂です。主な更新点として、著者情報の更新、アップデート日付の変更、および内容の整理が行われています。

文書の構造が改善され、特定のプログラミング言語に関するクイックスタートが個別に示されるようになりました。具体的には、C#、Java、JavaScript、TypeScript、およびPythonの各言語ごとのリンクが新たに追加され、それぞれのクイックスタートが別に紹介される形式になっています。

この変更により、読者は特定のプログラミング言語に対して必要な情報を効率的に得られるようになり、学習の流れがスムーズに進むことが期待されます。また、リソースの整理や使用の際のベストプラクティスが改めて強調されており、ユーザーにとって利便性が向上しています。

全体として、この更新はユーザーが Azure AI Search を活用しやすくなるよう、文書の内容と構成を見直したものです。


