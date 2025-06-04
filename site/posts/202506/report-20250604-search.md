---
date: '2025-06-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8d764d4...MicrosoftDocs:45b2d74
summary: このコード変更では、複数のMarkdownファイルでAzure AI Foundryポータルへのリンクが更新され、用語の一貫性と正確性が向上しました。主な改善点として、リンクが新しいURLに統一され、ユーザーが必要な学習リソースに迅速にアクセスできるようになっています。また、「requestor」が「requester」に修正され、文書全体の一貫性も強化されています。これらの変更は、ドキュメントの使いやすさを向上させ、技術情報へのアクセスを容易にするための重要な措置です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8d764d4...MicrosoftDocs:45b2d74){target="_blank"}

# Highlights
このコード変更では、複数のMarkdownファイルでAzure AI Foundryポータルへのリンクが更新されました。また、用語の表現が修正されており、これにより用語の一貫性と正確性が向上しています。

## New features
- Azure AI Foundryポータルのリンクが、「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」と、新しいリンクに統一されました。

## Breaking changes
- 特記される重大な変更はありません。

## Other updates
- 一部のファイルで、用語「requestor」が「requester」に修正され、文の一貫性が向上しています。

# Insights

このコード変更の主な目的は、ユーザーエクスペリエンスを向上させることにあります。これまでのリンクでは、Azure AI Foundryポータルにアクセスした際のランディングページが一般的なものであり、ユーザーが必要とする具体的な学習リソースに素早くアクセスできない可能性がありました。更新されたリンクでは、URLに含まれるクエリパラメータ「?cid=learnDocs」により、ユーザーはコンテンツがよりコンテキストに適合する可能性が高いページにリダイレクトされるため、必要な情報にたどり着くまでの時間が短縮されることが期待されます。

また、用語の修正については、技術文書における表現の一貫性を確保するための重要な措置です。特に、英語の用語に関しては、一貫した用語の使用が、異なるセクション間でユーザーが混乱を感じることのリスクを減らします。

これらのマイナーな更新は、一見すると些細に思えるかもしれませんが、ドキュメントの品質と使いやすさに大きく寄与するものであり、ユーザーが技術情報に簡単かつ効率的にアクセスし、理解できるようにするための重要な改善策です。文章の一貫性とリンクの精度の向上は、特に大規模な技術文書セットにおいて、その効果が累積的に現れます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-python.md](#item-efee6a) | minor update | Azure AI Foundryポータルのリンク更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-rest.md](#item-3df373) | minor update | Azure AI Foundryポータルのリンク更新 | modified | 1 | 1 | 2 | 
| [search-agentic-retrieval-how-to-create.md](#item-310fbe) | minor update | Azure AI Foundryポータルのリンク更新 | modified | 1 | 1 | 2 | 
| [search-agentic-retrieval-how-to-pipeline.md](#item-1ad1c3) | minor update | Azure AI Foundryポータルのリンク更新 | modified | 1 | 1 | 2 | 
| [search-filters.md](#item-3f2a7a) | minor update | リクエスターの表記修正 | modified | 1 | 1 | 2 | 
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | Azure AI Foundryポータルのリンク更新 | modified | 1 | 1 | 2 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | Azure AI Foundryポータルのリンク修正 | modified | 5 | 5 | 10 | 
| [search-how-to-integrated-vectorization.md](#item-86fb1e) | minor update | Azure AI Foundryポータルのリンク訂正 | modified | 4 | 4 | 8 | 
| [search-import-data-portal.md](#item-b804d1) | minor update | Azure AI Foundryポータルのリンク修正 | modified | 1 | 1 | 2 | 
| [search-security-network-security-perimeter.md](#item-49c0d7) | minor update | Azure AI Foundryポータルのリンク修正 | modified | 1 | 1 | 2 | 
| [search-security-rbac.md](#item-a5d129) | minor update | リクエスター表現の修正 | modified | 1 | 1 | 2 | 
| [search-try-for-free.md](#item-36e28d) | minor update | Azure AI Foundryポータルのリンク修正 | modified | 2 | 2 | 4 | 
| [search-what-is-azure-search.md](#item-93853a) | minor update | Azure AI Foundryポータルのリンク修正 | modified | 1 | 1 | 2 | 
| [tutorial-rag-build-solution-models.md](#item-6796c9) | minor update | Azure AI Foundryポータルのリンク修正 | modified | 2 | 2 | 4 | 
| [vector-search-integrated-vectorization-ai-studio.md](#item-353fcc) | minor update | Azure AI Foundryポータルのリンク修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -39,7 +39,7 @@ Agentic retrieval [supports several models](../../search-agentic-retrieval-how-t
 
 To deploy the Azure OpenAI models:
 
-1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/) and select your Azure OpenAI resource.
+1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and select your Azure OpenAI resource.
 
 1. From the left pane, select **Model catalog**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク更新"
}
```

### Explanation
この変更では、`agentic-retrieval-python.md`ファイル内のAzure AI Foundryポータルへのリンクが更新されました。具体的には、元のリンクが単に「https://ai.azure.com/」だったのに対し、新しいリンクは「https://ai.azure.com/?cid=learnDocs」となっています。この更新は、ユーザーのリダイレクションを改善し、特定のコンテキストで役立つ情報へのアクセスを容易にすることを目的としています。変更行は38行目になり、全体で2行の変更がありました。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

<details>
<summary>Diff</summary>
````diff
@@ -40,7 +40,7 @@ Agentic retrieval [supports several models](../../search-agentic-retrieval-how-t
 
 To deploy the Azure OpenAI models:
 
-1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/) and select your Azure OpenAI resource.
+1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and select your Azure OpenAI resource.
 
 1. From the left pane, select **Model catalog**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク更新"
}
```

### Explanation
この変更では、`agentic-retrieval-rest.md`ファイルにおいて、Azure AI Foundryポータルへのリンクが更新されました。具体的には、元のリンクが「https://ai.azure.com/」だったのに対し、新しいリンクは「https://ai.azure.com/?cid=learnDocs」となっています。この変更により、ユーザーが必要な情報により簡単にアクセスできるように、指示が明確化されています。変更は40行目で行われ、全体で2行の変更が反映されています。

## articles/search/search-agentic-retrieval-how-to-create.md{#item-310fbe}

<details>
<summary>Diff</summary>
````diff
@@ -45,7 +45,7 @@ To follow the steps in this guide, we recommend [Visual Studio Code](https://cod
 
 Make sure you have a supported model that Azure AI Search can access. The following instruction assumes Azure AI Foundry Model as the provider.
 
-1. Sign in to [Azure AI Foundry portal](https://ai.azure.com/).
+1. Sign in to [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs).
 
 1. Deploy a supported model using [these instructions](/azure/ai-foundry/how-to/deploy-models-openai).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク更新"
}
```

### Explanation
この変更では、`search-agentic-retrieval-how-to-create.md`ファイルにおいて、Azure AI Foundryポータルへのリンクが更新されました。元のリンクは「https://ai.azure.com/」でしたが、新しいリンクは「https://ai.azure.com/?cid=learnDocs」となっています。この修正により、ユーザーがポータルにアクセスする際に特定の情報やリソースへ直接導かれることを意図しています。変更は45行目にあり、全体で2行の変更が行われています。

## articles/search/search-agentic-retrieval-how-to-pipeline.md{#item-1ad1c3}

<details>
<summary>Diff</summary>
````diff
@@ -128,7 +128,7 @@ You can find endpoints for Azure AI Search and Azure OpenAI in the [Azure portal
 
 You can find the project endpoint in the Azure AI Foundry portal:
 
-1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com) and open your project. 
+1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and open your project. 
 
 1. In the **Overview** tile, find and copy the Azure AI Foundry project endpoint.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク更新"
}
```

### Explanation
この変更では、`search-agentic-retrieval-how-to-pipeline.md`ファイルにおいて、Azure AI Foundryポータルへのリンクが修正されました。以前のリンク「https://ai.azure.com」は、新しいリンク「https://ai.azure.com/?cid=learnDocs」に置き換えられています。この更新により、ユーザーがポータルにアクセスした際に、特定のリソースや情報へよりスムーズに誘導されることを目的としています。変更は128行目で行われ、全体で2行の変更が含まれています。

## articles/search/search-filters.md{#item-3f2a7a}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ A filter is specified using [OData filter expression syntax](search-query-odata-
 
 ## When to use a filter
 
-Filters are foundational to several search experiences, including "find near me" geospatial search, faceted navigation, and security filters that show only  those documents a user is allowed to see. If you implement any one of these experiences, a filter is required. It's the filter attached to the search query that provides the geolocation coordinates, the facet category selected by the user, or the security ID of the requestor.
+Filters are foundational to several search experiences, including "find near me" geospatial search, faceted navigation, and security filters that show only  those documents a user is allowed to see. If you implement any one of these experiences, a filter is required. It's the filter attached to the search query that provides the geolocation coordinates, the facet category selected by the user, or the security ID of the requester.
 
 Common scenarios include:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リクエスターの表記修正"
}
```

### Explanation
この変更では、`search-filters.md`ファイル内の「リクエスター」という単語が「requestor」に修正されました。具体的には、フィルターに関連する説明の部分で、この用語が用いられています。この修正により、用語の一貫性と正確性が向上し、ユーザーが理解しやすくなります。変更は24行目で行われ、全体で2行にわたって変更が施されています。

## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -111,7 +111,7 @@ The wizard requires an LLM to verbalize images and an embedding model to generat
 
 To deploy the models for this quickstart:
 
-1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com) and select your Azure OpenAI resource.
+1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and select your Azure OpenAI resource.
 
 1. From the left pane, select **Model catalog**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク更新"
}
```

### Explanation
この変更では、`search-get-started-portal-image-search.md`ファイルにおいて、Azure AI Foundryポータルへのリンクが更新されました。具体的には、従来のリンク「https://ai.azure.com」が新しいリンク「https://ai.azure.com/?cid=learnDocs」に修正されています。この更新により、ユーザーがポータルにアクセスする際、特定のリソースや情報へより効率的にナビゲートできるようになります。変更は111行目で行われ、全体で2行の変更が含まれています。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -52,7 +52,7 @@ For integrated vectorization, you must use one of the following embedding models
 
 <sup>1</sup> The endpoint of your Azure OpenAI resource must have a [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains), such as `https://my-unique-name.openai.azure.com`. If you created your resource in the [Azure portal](https://portal.azure.com/), this subdomain was automatically generated during resource setup.
 
-<sup>2</sup> Azure OpenAI resources (with access to embedding models) that were created in the [Azure AI Foundry portal](https://ai.azure.com/) aren't supported. Only Azure OpenAI resources created in the Azure portal are compatible with the [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md) integration.
+<sup>2</sup> Azure OpenAI resources (with access to embedding models) that were created in the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) aren't supported. Only Azure OpenAI resources created in the Azure portal are compatible with the [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md) integration.
 
 <sup>3</sup> For billing purposes, you must [attach your Azure AI multi-service resource](cognitive-search-attach-cognitive-services.md) to the skillset in your Azure AI Search service. Unless you use a [keyless connection (preview)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) to create the skillset, both resources must be in the same region.
 
@@ -182,7 +182,7 @@ This section points you to the content that works for this quickstart. Before yo
 
 ## Prepare embedding model
 
-The wizard can use embedding models deployed from Azure OpenAI, Azure AI Vision, or from the model catalog in the [Azure AI Foundry portal](https://ai.azure.com/). Before you proceed, make sure you completed the prerequisites for [role-based access](#role-based-access).
+The wizard can use embedding models deployed from Azure OpenAI, Azure AI Vision, or from the model catalog in the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs). Before you proceed, make sure you completed the prerequisites for [role-based access](#role-based-access).
 
 ### [Azure OpenAI](#tab/model-aoai)
 
@@ -204,7 +204,7 @@ The wizard supports text-embedding-ada-002, text-embedding-3-large, and text-emb
 
 1. To deploy an embedding model:
 
-   1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/) and select your Azure OpenAI resource.
+   1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and select your Azure OpenAI resource.
 
    1. From the left pane, select **Model catalog**.
 
@@ -255,7 +255,7 @@ For the model catalog, you should have an [Azure AI Foundry project](/azure/ai-f
 
 1. To deploy an embedding model:
 
-   1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/) and select your project.
+   1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and select your project.
 
    1. From the left pane, select **Model catalog**.
 
@@ -413,7 +413,7 @@ However, if you work with content that includes useful images, you can apply AI
 
 Azure AI Search and your Azure AI resource must be in the same region or configured for [keyless billing connections](cognitive-search-attach-cognitive-services.md).
 
-1. On the **Vectorize your images** page, specify the kind of connection the wizard should make. For image vectorization, the wizard can connect to embedding models in the [Azure AI Foundry portal](https://ai.azure.com/) or Azure AI Vision.
+1. On the **Vectorize your images** page, specify the kind of connection the wizard should make. For image vectorization, the wizard can connect to embedding models in the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) or Azure AI Vision.
 
 1. Specify the subscription.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク修正"
}
```

### Explanation
この変更では、`search-get-started-portal-import-vectors.md`ファイルにおいて、Azure AI Foundryポータルへのリンクが更新されました。具体的には、各所で使用されているポータルのリンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に修正されています。この修正により、リンクをクリックした際に、ユーザーが特定のリソースや情報をより効率的に取得できるようになります。変更は文中のいくつかの箇所にわたって行われ、合計で10行の変更が含まれています。

## articles/search/search-how-to-integrated-vectorization.md{#item-86fb1e}

<details>
<summary>Diff</summary>
````diff
@@ -52,7 +52,7 @@ For integrated vectorization, you must use one of the following embedding models
 
 <sup>1</sup> The endpoint of your Azure OpenAI resource must have a [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains), such as `https://my-unique-name.openai.azure.com`. If you created your resource in the [Azure portal](https://portal.azure.com/), this subdomain was automatically generated during resource setup.
 
-<sup>2</sup> Azure OpenAI resources (with access to embedding models) that were created in the [Azure AI Foundry portal](https://ai.azure.com/) aren't supported. Only Azure OpenAI resources created in the Azure portal are compatible with the [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md) integration.
+<sup>2</sup> Azure OpenAI resources (with access to embedding models) that were created in the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) aren't supported. Only Azure OpenAI resources created in the Azure portal are compatible with the [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md) integration.
 
 <sup>3</sup> For billing purposes, you must [attach your Azure AI multi-service resource](cognitive-search-attach-cognitive-services.md) to the skillset in your Azure AI Search service. Unless you use a [keyless connection (preview)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) to create the skillset, both resources must be in the same region.
 
@@ -224,7 +224,7 @@ Azure AI Search supports text-embedding-ada-002, text-embedding-3-small, and tex
 
 1. To deploy an embedding model:
 
-   1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/) and select your Azure OpenAI resource.
+   1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and select your Azure OpenAI resource.
 
    1. From the left pane, select **Model catalog**.
 
@@ -261,7 +261,7 @@ Azure AI Search supports Azure AI Vision image retrieval through multimodal embe
 
 <!--### [Azure AI Foundry model catalog](#tab/prepare-model-catalog)
 
-Azure AI Search supports Azure, Cohere, and Facebook embedding models in the [Azure AI Foundry](https://ai.azure.com/) model catalog, but it doesn't currently support the OpenAI CLIP models. Internally, Azure AI Search calls the [Azure Machine Learning (AML) skill](cognitive-search-aml-skill.md) to connect to the catalog.
+Azure AI Search supports Azure, Cohere, and Facebook embedding models in the [Azure AI Foundry](https://ai.azure.com/?cid=learnDocs) model catalog, but it doesn't currently support the OpenAI CLIP models. Internally, Azure AI Search calls the [Azure Machine Learning (AML) skill](cognitive-search-aml-skill.md) to connect to the catalog.
 
 For the model catalog, you should have an [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects) with a [hub that's connected to an Azure OpenAI resource and an Azure AI Search service](/azure/ai-foundry/how-to/create-projects#create-a-project).
 
@@ -281,7 +281,7 @@ For the model catalog, you should have an [Azure AI Foundry project](/azure/ai-f
 
 1. To deploy an embedding model:
 
-   1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/) and select your project.
+   1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and select your project.
 
    1. From the left pane, select **Model catalog**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク訂正"
}
```

### Explanation
この変更では、`search-how-to-integrated-vectorization.md`ファイルにおいて、Azure AI Foundryポータルへのリンクが更新されました。具体的には、ポータルのリンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に修正されています。このリンク修正により、ユーザーがポータルにアクセスする際に、関連情報へよりスムーズにアクセスできるようになります。変更は文中のいくつかの箇所で行われ、合計で8行の変更が含まれています。

## articles/search/search-import-data-portal.md{#item-b804d1}

<details>
<summary>Diff</summary>
````diff
@@ -150,7 +150,7 @@ You can use the wizards over restricted public connections, but not all function
 
   The Azure resource must admit network requests from the IP address of the device used on the connection. You should also list Azure AI Search as a trusted service on the resource's network configuration. For example, in Azure Storage, you can list `Microsoft.Search/searchServices` as a trusted service.
 
-+ On connections to an Azure AI services multi-service account that you provide, or on connections to embedding models deployed in [Azure AI Foundry portal](https://ai.azure.com/) or Azure OpenAI, public internet access must be enabled unless your search service meets the creation date, tier, and region requirements for private connections. For more information about these requirements, see [Make outbound connections through a shared private link](search-indexer-howto-access-private.md).
++ On connections to an Azure AI services multi-service account that you provide, or on connections to embedding models deployed in [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) or Azure OpenAI, public internet access must be enabled unless your search service meets the creation date, tier, and region requirements for private connections. For more information about these requirements, see [Make outbound connections through a shared private link](search-indexer-howto-access-private.md).
 
   Connections to Azure AI services multi-service are for [billing purposes](cognitive-search-attach-cognitive-services.md). Billing occurs when API calls exceed the free transaction count (20 per indexer run) for built-in skills called by the **Import data** wizard or integrated vectorization in the **Import and vectorize data wizard**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク修正"
}
```

### Explanation
この変更では、`search-import-data-portal.md`ファイルにおいて、Azure AI Foundryポータルへのリンクが更新されました。具体的には、ポータルのリンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に修正されています。このリンクの更新により、ユーザーがポータルにアクセスする際に、関連する情報をより明確に取得できるようになります。変更は文中の1行の追加と1行の削除を伴い、合計で2行の変更が含まれています。

## articles/search/search-security-network-security-perimeter.md{#item-49c0d7}

<details>
<summary>Diff</summary>
````diff
@@ -167,7 +167,7 @@ Within the perimeter, all resources have mutual access at the network level. You
 
 For resources outside of the network security perimeter, you must specify inbound and outbound access rules. Inbound rules specify which connections to allow in, and outbound rules specify which requests are allowed out.
 
-A search service accepts inbound requests from apps like [Azure AI Foundry portal](https://ai.azure.com/), Azure Machine Learning prompt flow, and any app that sends indexing or query requests. A search service sends outbound requests during indexer-based indexing and skillset execution. This section explains how to set up inbound and outbound access rules for Azure AI Search scenarios.
+A search service accepts inbound requests from apps like [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs), Azure Machine Learning prompt flow, and any app that sends indexing or query requests. A search service sends outbound requests during indexer-based indexing and skillset execution. This section explains how to set up inbound and outbound access rules for Azure AI Search scenarios.
 
    > [!NOTE]
    > Any service associated with a network security perimeter implicitly allows inbound and outbound access to any other service associated with the same network security perimeter when that access is authenticated using [managed identities and role assignments](/entra/identity/managed-identities-azure-resources/overview). Access rules only need to be created when allowing access outside of the network security perimeter, or for access authenticated using API keys.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク修正"
}
```

### Explanation
この変更では、`search-security-network-security-perimeter.md`ファイルにおいて、Azure AI Foundryポータルへのリンクが更新されました。具体的には、ポータルのリンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に修正されています。このリンクの更新により、ユーザーがポータルにアクセスする際に、関連情報をより見つけやすくなります。変更は文中の1行の追加と1行の削除を伴い、合計で2行の変更が含まれています。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ In Azure AI Search, you can assign Azure roles for:
 + [Read-only access for queries](#assign-roles-for-read-only-queries)
 + [Scoped access to a single index](#grant-access-to-a-single-index)
 
-Per-user access over search results (sometimes referred to as *row-level security* or *document-level security*) isn't supported through role assignments. As a workaround, [create security filters](search-security-trimming-for-azure-search.md) that trim results by user identity, removing documents for which the requestor shouldn't have access. See this [Enterprise chat sample using RAG](/azure/developer/python/get-started-app-chat-template) for a demonstration.
+Per-user access over search results (sometimes referred to as *row-level security* or *document-level security*) isn't supported through role assignments. As a workaround, [create security filters](search-security-trimming-for-azure-search.md) that trim results by user identity, removing documents for which the requester shouldn't have access. See this [Enterprise chat sample using RAG](/azure/developer/python/get-started-app-chat-template) for a demonstration.
 
 Role assignments are cumulative and pervasive across all tools and client libraries. You can assign roles using any of the [supported approaches](/azure/role-based-access-control/role-assignments-steps) described in Azure role-based access control documentation.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リクエスター表現の修正"
}
```

### Explanation
この変更では、`search-security-rbac.md`ファイルにおいて、表現の微調整が行われました。具体的には、「requestor」が「requester」に修正され、文が一貫性を持つようになりました。この変更は、ユーザーが提供されたセキュリティフィルターの具体例を理解しやすくするためのもので、文中の1行の追加と1行の削除が含まれています。全体として、より明確で一貫性のある表現を目指したマイナーな更新です。

## articles/search/search-try-for-free.md{#item-36e28d}

<details>
<summary>Diff</summary>
````diff
@@ -31,13 +31,13 @@ Once you sign up, you can immediately use either of these links to access Azure
 
 + [Sign in to Azure portal](https://portal.azure.com/) to view, manage, and create more resources. You can also use the Azure portal to track your credits and projected costs.
 
-+ [Sign in to Azure AI Foundry](https://ai.azure.com) for a no-code approach to deploying models on Azure OpenAI and using Azure AI Search for information retrieval. **We recommend you start here first.**
++ [Sign in to Azure AI Foundry](https://ai.azure.com/?cid=learnDocs) for a no-code approach to deploying models on Azure OpenAI and using Azure AI Search for information retrieval. **We recommend you start here first.**
 
 ## Step two: "Day One" tasks
 
 [**How to build and consume vector indexes in Azure AI Foundry portal**](/azure/ai-foundry/how-to/index-add) is a great place to start.
 
-1. [Sign in to Azure AI Foundry](https://ai.azure.com).
+1. [Sign in to Azure AI Foundry](https://ai.azure.com/?cid=learnDocs).
 
 1. Create a new hub and project.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク修正"
}
```

### Explanation
この変更では、`search-try-for-free.md`ファイルにおいて、Azure AI Foundryへのリンクが更新されました。リンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に修正され、関連情報がより容易に見つけられるようになっています。この変更は、ユーザーがAzure AI Foundryの利用を開始する際の案内を一層明確にするためのもので、文中の追加と削除を含む合計4行の変更が行われています。全体として、利用者にとっての利便性向上を目的としたマイナーな更新です。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ On the search service itself, the two primary workloads are *indexing* and *quer
 
   [Applied AI](cognitive-search-concept-intro.md) through a [skillset](cognitive-search-working-with-skillsets.md) extends indexing with image and language models. If you have images or large unstructured text in source document, you can attach skills that perform OCR, analyze and describe images, infer structure, translate text, and more. Output is text that can be serialized into JSON and ingested into a search index.
 
-  Skillsets can also perform [data chunking and vectorization during indexing](vector-search-integrated-vectorization.md). Skills that attach to Azure OpenAI, the model catalog in [Azure AI Foundry portal](https://ai.azure.com/), or custom skills that attach to any external chunking and embedding model can be used during indexing to create vector data. Output is chunked vector content that can be ingested into a search index.
+  Skillsets can also perform [data chunking and vectorization during indexing](vector-search-integrated-vectorization.md). Skills that attach to Azure OpenAI, the model catalog in [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs), or custom skills that attach to any external chunking and embedding model can be used during indexing to create vector data. Output is chunked vector content that can be ingested into a search index.
 
 + [**Querying**](search-query-overview.md) can happen once an index is populated with searchable content, when your client app sends query requests to a search service and handles responses. All query execution is over a search index that you control.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク修正"
}
```

### Explanation
この変更では、`search-what-is-azure-search.md`ファイルにおいて、Azure AI Foundryポータルへのリンクが更新されました。具体的には、リンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に修正され、ユーザーが情報をより効果的に探せるようになっています。この変更は文中の1行の追加と1行の削除を含んでおり、全体として内容の明確化とユーザビリティ向上を目指したマイナーな更新です。

## articles/search/tutorial-rag-build-solution-models.md{#item-6796c9}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
 - An **Owner** or **User Access Administrator** role on your Azure subscription, necessary for creating role assignments. You use at least three Azure resources in this tutorial. The connections are authenticated using Microsoft Entra ID, which requires the ability to create roles. Role assignments for connecting to models are documented in this article. If you can't create roles, you can use [API keys](search-security-api-keys.md) instead.
 
-- A model provider, such as [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource), Azure AI Vision via an [Azure AI services multi-service resource](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills), or [Azure AI Foundry](https://ai.azure.com/).
+- A model provider, such as [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource), Azure AI Vision via an [Azure AI services multi-service resource](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills), or [Azure AI Foundry](https://ai.azure.com/?cid=learnDocs).
 
   We use Azure OpenAI in this tutorial. Other providers are listed so that you know your options for integrated vectorization.
 
@@ -99,7 +99,7 @@ This tutorial series uses the following models and model providers:
 
 You must have [**Cognitive Services OpenAI Contributor**]( /azure/ai-services/openai/how-to/role-based-access-control#cognitive-services-openai-contributor) or higher to deploy models in Azure OpenAI.
 
-1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/).
+1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs).
 
 1. From the left pane, select **Model catalog**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク修正"
}
```

### Explanation
この変更は、`tutorial-rag-build-solution-models.md`ファイルにおいて、Azure AI Foundryポータルへのリンクが更新されたことを示しています。リンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に修正され、ユーザーが必要な情報をより簡単に見つけやすくなることを目的としています。これには、2行の追加と2行の削除が含まれており、全体として内容の明確化とユーザーの利便性を向上させるためのマイナーな更新です。

## articles/search/vector-search-integrated-vectorization-ai-studio.md{#item-353fcc}

<details>
<summary>Diff</summary>
````diff
@@ -247,7 +247,7 @@ If you selected a different `embedding_types` in your skill definition that you
 
 ## Sample Azure AI Foundry vectorizer payload
 
-The [Azure AI Foundry vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md), unlike the AML skill, is tailored to work only with those embedding models that are deployable via the Azure AI Foundry model catalog. The main difference is that you don't have to worry about the request and response payload, but you do have to provide the `modelName`, which corresponds to the "Model ID" that you copied after deploying the model in [Azure AI Foundry portal](https://ai.azure.com/). 
+The [Azure AI Foundry vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md), unlike the AML skill, is tailored to work only with those embedding models that are deployable via the Azure AI Foundry model catalog. The main difference is that you don't have to worry about the request and response payload, but you do have to provide the `modelName`, which corresponds to the "Model ID" that you copied after deploying the model in [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs). 
 
 Here's a sample payload of how you would configure the vectorizer on your index definition given the properties copied from Azure AI Foundry.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク修正"
}
```

### Explanation
この変更では、`vector-search-integrated-vectorization-ai-studio.md`ファイルにおいて、Azure AI Foundryポータルへのリンクが更新されました。リンクが「https://ai.azure.com」から「https://ai.azure.com/?cid=learnDocs」に修正されており、これによりユーザーが必要な情報をより簡単に探せるように配慮されています。この修正は、1行の追加と1行の削除を伴っており、全体的には内容の明確化とユーザビリティの向上を意図したマイナーな更新です。


