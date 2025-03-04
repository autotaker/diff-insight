---
date: '2025-03-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ab648e8...MicrosoftDocs:bf9270b
summary: この記事の変更は、Azure AIサービスに関する複数のドキュメントに「Azure AI Foundryポータル」へのリンクを追加したことを目的としています。この変更により、ユーザーは関連情報にアクセスしやすくなり、特にAzure
  AI FoundryポータルやAzure OpenAIサービスの理解が向上しました。また、リンクの追加により、ドキュメントのユーザビリティが改善されています。破壊的変更はなく、主にリンクの追加と説明の明確化が行われました。この更新は、ユーザーが必要な情報に迅速にアクセスできるようにすることを目指しており、特に技術系のドキュメントにおいては、関連情報への迅速なアクセスが重要です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ab648e8...MicrosoftDocs:bf9270b){target="_blank"}

# ハイライト

この記事の一連の変更は、Azure AIサービスに関する複数のドキュメントに対し、「Azure AI Foundryポータル」へのリンクを追加し、ユーザーが関連情報にアクセスしやすくすることを目的としています。特に、新しいリンクはAzure AI FoundryポータルやAzure OpenAIサービスに関するユーザーの理解をサポートし、ポータルの詳細を明確にする役割を果たしています。これにより、情報への導線が整理され、ドキュメントのユーザビリティが向上しています。

## 新機能

- Azure AI Foundryポータルへのリンクが複数のセクションに追加され、ユーザーが関連情報や機能詳細にスムーズにアクセスできるようになりました。

## 破壊的な変更

- 重大な破壊的変更はありません。主にリンク追加と説明の改善が施されています。

## その他の更新

- 各ドキュメントの特定のセクションについて、不明瞭だった接続条件や利用可能なスキルセットに関する説明が改善されています。

# 洞察

今回のドキュメント更新は、Azure AIサービスを活用するユーザーが必要とする情報に迅速にアクセスできるよう、リソースへのリンクを強化することを目指しています。リンク追加が各ドキュメントにおいて行われたことで、ユーザーはAzure AI Foundryポータルに関する詳細情報や利用方法を直接確認でき、情報の関連性が明確化されました。

こうしたリンク追加は、特にAzureの複雑なサービスモデルを理解しようとしているユーザーに対して非常に有用です。特に技術系のドキュメントにおいては、関連情報への迅速なアクセスが成功の鍵となり得ます。そのため、リンクの挿入はUXの向上に寄与し、ユーザーの労力を削減します。

さらに、ドキュメントにおける新たなリンクの組み込みは、ユーザーが一貫して最新の情報を入手できるよう、関連ポータルや機能のアップデートに素早く対応できる柔軟性を持たせています。企業が提供するツールやリソースが変わることは少なくありませんが、ドキュメントに正確なリンクが組み込まれていることで、その変化にうまく追随することが可能です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | リンクの追加と表現の改善 | modified | 3 | 3 | 6 | 
| [search-import-data-portal.md](#item-b804d1) | minor update | ポータルリンクの追加と説明の改善 | modified | 1 | 1 | 2 | 
| [search-security-network-security-perimeter.md](#item-49c0d7) | minor update | ポータルリンクの追加 | modified | 1 | 1 | 2 | 
| [search-what-is-azure-search.md](#item-93853a) | minor update | ポータルリンクの追加 | modified | 1 | 1 | 2 | 
| [vector-search-integrated-vectorization-ai-studio.md](#item-353fcc) | minor update | ポータルリンクの追加 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -52,7 +52,7 @@ Use an embedding model on an Azure AI platform in the [same region as Azure AI S
 
 If you use the Azure OpenAI Service, the endpoint must have an associated [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains). A custom subdomain is an endpoint that includes a unique name (for example, `https://hereismyuniquename.cognitiveservices.azure.com`). If the service was created through the Azure portal, this subdomain is automatically generated as part of your service setup. Ensure that your service includes a custom subdomain before using it with the Azure AI Search integration.
 
-Azure OpenAI Service resources (with access to embedding models) that were created in Azure AI Foundry portal aren't supported. Only the Azure OpenAI Service resources created in the Azure portal are compatible with the **Azure OpenAI Embedding** skill integration.
+Azure OpenAI Service resources (with access to embedding models) that were created in [Azure AI Foundry portal](https://ai.azure.com/) aren't supported. Only the Azure OpenAI Service resources created in the Azure portal are compatible with the **Azure OpenAI Embedding** skill integration.
 
 ### Public endpoint requirements
 
@@ -157,7 +157,7 @@ This section points you to the content that works for this quickstart.
 
 ## Set up embedding models
 
-The wizard can use embedding models deployed from Azure OpenAI, Azure AI Vision, or from the model catalog in Azure AI Foundry portal.
+The wizard can use embedding models deployed from Azure OpenAI, Azure AI Vision, or from the model catalog in [Azure AI Foundry portal](https://ai.azure.com/).
 
 ### [Azure OpenAI](#tab/model-aoai)
 
@@ -351,7 +351,7 @@ However, if you work with content that includes useful images, you can apply AI
 
 Azure AI Search and your Azure AI resource must be in the same region or configured for [keyless billing connections](cognitive-search-attach-cognitive-services.md).
 
-1. On the **Vectorize your images** page, specify the kind of connection the wizard should make. For image vectorization, the wizard can connect to embedding models in Azure AI Foundry portal or Azure AI Vision.
+1. On the **Vectorize your images** page, specify the kind of connection the wizard should make. For image vectorization, the wizard can connect to embedding models in [Azure AI Foundry portal](https://ai.azure.com/) or Azure AI Vision.
 
 1. Specify the subscription.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの追加と表現の改善"
}
```

### Explanation
この変更は、Azure AIサービスに関するドキュメントの内容を改善するために行われました。具体的には、いくつかのリンクが追加され、特定のポータルに関する説明が明確化されています。具体的には、Azure AI Foundryポータルへのリンクがテキスト内に追加され、ユーザーがより簡単に関連する情報にアクセスできるように修正されています。

変更点の詳細は以下の通りです：
1. Azure OpenAIサービスリソースがAzure AI Foundryポータルで作成された場合にサポートされないことを明確にするために、「[Azure AI Foundry portal](https://ai.azure.com/)」へのリンクが追加されました。 
2. ウィザードが利用できる埋め込みモデルに関する説明で、同様に「[Azure AI Foundry portal](https://ai.azure.com/)」へのリンクが追加されました。
3. 画像ベクトル化のページにおいて、ウィザードが接続できる埋め込みモデルを指定する際にも、Azure AI Foundryポータルへのリンクが挿入されました。

これにより、ユーザーは関連するポータルにスムーズにアクセスでき、情報の理解が促進されることを目的としています。

## articles/search/search-import-data-portal.md{#item-b804d1}

<details>
<summary>Diff</summary>
````diff
@@ -150,7 +150,7 @@ You can use the wizards over restricted public connections, but not all function
 
   The Azure resource must admit network requests from the IP address of the device used on the connection. You should also list Azure AI Search as a trusted service on the resource's network configuration. For example, in Azure Storage, you can list `Microsoft.Search/searchServices` as a trusted service.
 
-+ On connections to an Azure AI multi-service account that you provide, or on connections to embedding models deployed in Azure AI Foundry portal or Azure OpenAI, public internet access must be enabled unless your search service meets the creation date, tier, and region requirements for private connections. For more information about these requirements, see [Make outbound connections through a shared private link](search-indexer-howto-access-private.md).
++ On connections to an Azure AI multi-service account that you provide, or on connections to embedding models deployed in [Azure AI Foundry portal](https://ai.azure.com/) or Azure OpenAI, public internet access must be enabled unless your search service meets the creation date, tier, and region requirements for private connections. For more information about these requirements, see [Make outbound connections through a shared private link](search-indexer-howto-access-private.md).
 
   Connections to Azure AI multi-service are for [billing purposes](cognitive-search-attach-cognitive-services.md). Billing occurs when API calls exceed the free transaction count (20 per indexer run) for built-in skills called by the **Import data** wizard or integrated vectorization in the **Import and vectorize data** wizard. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータルリンクの追加と説明の改善"
}
```

### Explanation
この変更は、データインポートに関するドキュメントの一部を更新するもので、主にAzure AI Foundryポータルへのリンクが追加されています。このことにより、関連情報へのアクセスがより容易になり、ユーザーが必要なリソースを迅速に見つけることができるようになります。

具体的な変更内容は以下の通りです：
1. アクセスに関する説明が明確になり、Azure AI FoundryポータルおよびAzure OpenAIに関する接続条件について具体的に言及されています。
2. 特に、「[Azure AI Foundry portal](https://ai.azure.com/)」へのリンクが追加され、ユーザーが直接アクセスできるようになっています。このリンクによって、Azure AI Foundryポータルの詳細情報や機能について、すぐに確認できる利点があります。

全体として、この変更はユーザビリティを向上させ、文書の情報提供の精度を高めることを目的としています。

## articles/search/search-security-network-security-perimeter.md{#item-49c0d7}

<details>
<summary>Diff</summary>
````diff
@@ -167,7 +167,7 @@ Within the perimeter, all resources have mutual access at the network level. You
 
 For resources outside of the network security perimeter, you must specify inbound and outbound access rules. Inbound rules specify which connections to allow in, and outbound rules specify which requests are allowed out.
 
-A search service accepts inbound requests from apps like Azure AI Foundry portal, Azure Machine Learning prompt flow, and any app that sends indexing or query requests. A search service sends outbound requests during indexer-based indexing and skillset execution. This section explains how to set up inbound and outbound access rules for Azure AI Search scenarios.
+A search service accepts inbound requests from apps like [Azure AI Foundry portal](https://ai.azure.com/), Azure Machine Learning prompt flow, and any app that sends indexing or query requests. A search service sends outbound requests during indexer-based indexing and skillset execution. This section explains how to set up inbound and outbound access rules for Azure AI Search scenarios.
 
    > [!NOTE]
    > Any service associated with a network security perimeter implicitly allows inbound and outbound access to any other service associated with the same network security perimeter when that access is authenticated using [managed identities and role assignments](/entra/identity/managed-identities-azure-resources/overview). Access rules only need to be created when allowing access outside of the network security perimeter, or for access authenticated using API keys.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータルリンクの追加"
}
```

### Explanation
この変更は、ネットワークセキュリティ境界に関するドキュメントの一部を更新するもので、特にAzure AI Foundryポータルへのリンクが追加されています。このリンクにより、関連するリソースに対するアクセスが容易になり、ユーザーが必要な情報を迅速に見つけることができるようになります。

具体的には、以下の変更点があります：
1. 検索サービスが受け入れるインバウンドリクエストの説明において、Azure AI Foundryポータルへのリンクが追加されました。このリンクは、ユーザーがAzure AI Foundryポータルに直接アクセスできるようにするもので、情報の導線が整理されています。
2. その他のサービスとのインバウンドおよびアウトバウンドアクセスルールについての説明はそのままであり、変更後の文書でも引き続き、ネットワークセキュリティ境界におけるリソース間のアクセスに関する要件が説明されています。

この変更により、ドキュメントはユーザーフレンドリーになり、必要な情報をより簡単に取得できるようにすることを目的としています。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ On the search service itself, the two primary workloads are *indexing* and *quer
 
   [Applied AI](cognitive-search-concept-intro.md) through a [skillset](cognitive-search-working-with-skillsets.md) extends indexing with image and language models. If you have images or large unstructured text in source document, you can attach skills that perform OCR, analyze and describe images, infer structure, translate text, and more. Output is text that can be serialized into JSON and ingested into a search index.
 
-  Skillsets can also perform [data chunking and vectorization during indexing](vector-search-integrated-vectorization.md). Skills that attach to Azure OpenAI, the model catalog in Azure AI Foundry portal, or custom skills that attach to any external chunking and embedding model can be used during indexing to create vector data. Output is chunked vector content that can be ingested into a search index.
+  Skillsets can also perform [data chunking and vectorization during indexing](vector-search-integrated-vectorization.md). Skills that attach to Azure OpenAI, the model catalog in [Azure AI Foundry portal](https://ai.azure.com/), or custom skills that attach to any external chunking and embedding model can be used during indexing to create vector data. Output is chunked vector content that can be ingested into a search index.
 
 + [**Querying**](search-query-overview.md) can happen once an index is populated with searchable content, when your client app sends query requests to a search service and handles responses. All query execution is over a search index that you control.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータルリンクの追加"
}
```

### Explanation
この変更は、Azure Searchに関するドキュメントの一部を更新するもので、特にAzure AI Foundryポータルへのリンクが追加されています。このリンクにより、関連するリソースへのアクセスが向上し、ユーザーが必要な情報を素早く確認できるようになっています。

具体的には、以下の変更点があります：
1. スキルセットが対応できる機能の説明において、Azure AI Foundryポータルへのリンクが追加されました。この変更により、ユーザーは、スキルセットが活用するモデルカタログの詳細を直接確認できるため、情報の提供が強化されています。
2. 他の部分については、特に変更はなく、従来の情報提供が継続されていますが、クエリの実行に関するセクションも含まれており、インデックスが検索可能なコンテンツで埋められた後のリクエストの処理についての説明がなされています。

この変更は、ドキュメントのアクセシビリティを向上させ、情報の見つけやすさを改善することを目的としています。

## articles/search/vector-search-integrated-vectorization-ai-studio.md{#item-353fcc}

<details>
<summary>Diff</summary>
````diff
@@ -245,7 +245,7 @@ If you selected a different `embedding_types` in your skill definition that you
 
 ## Sample Azure AI Foundry vectorizer payload
 
-The [Azure AI Foundry vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md), unlike the AML skill, is tailored to work only with those embedding models that are deployable via the Azure AI Foundry model catalog. The main difference is that you don't have to worry about the request and response payload, but you do have to provide the `modelName`, which corresponds to the "Model ID" that you copied after deploying the model in Azure AI Foundry portal. 
+The [Azure AI Foundry vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md), unlike the AML skill, is tailored to work only with those embedding models that are deployable via the Azure AI Foundry model catalog. The main difference is that you don't have to worry about the request and response payload, but you do have to provide the `modelName`, which corresponds to the "Model ID" that you copied after deploying the model in [Azure AI Foundry portal](https://ai.azure.com/). 
 
 Here's a sample payload of how you would configure the vectorizer on your index definition given the properties copied from Azure AI Foundry.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータルリンクの追加"
}
```

### Explanation
この変更は、Azure AI Foundryのベクターライザーに関するドキュメントの一部を更新するもので、特にAzure AI Foundryポータルへのリンクが追加されています。このリンクにより、ユーザーは関連するリソースに直接アクセスし、利用方法を簡単に確認できるようになります。

具体的には、以下の変更点があります：
1. Azure AI FoundryベクターライザーがAMLスキルとどのように異なるかの説明において、Azure AI Foundryポータルへのリンクが組み込まれました。このリンクにより、モデルのデプロイ後にコピーした"Model ID"について、ユーザーが容易に参照できるようにされています。
2. それ以外の文言は変更されておらず、ベクターライザーの設定方法についてのサンプルペイロードの説明が引き続き行われています。

この変更は、ドキュメントの明確性を向上させ、ユーザーが必要な情報を迅速に見つけられるようにすることを目的としています。


