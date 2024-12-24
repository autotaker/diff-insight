---
date: '2024-12-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6a825e5...MicrosoftDocs:f98b838
summary: 今回の変更は、ドキュメント全体にわたって「AI Foundry」から「Azure AI Foundry」への用語統一を行ったマイナーアップデートです。これにより、Azureサービスに関する情報の一貫性と明確性が向上し、ユーザーへの正確な情報提供が可能になります。新機能の追加や破壊的変更はなく、ドキュメント内の用語の正確性を高めるための複数のマイナー修正が行われました。この修正は、用語の一致が技術的な文書において重要であり、Azureサービスを利用するユーザーの理解を助けるために有効です。全体として、この変更は「Azure
  AI Foundry」としてのブランド認知を高め、将来のサービス発展に寄与すると考えられます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6a825e5...MicrosoftDocs:f98b838){target="_blank"}

# ハイライト

今回の変更は、ドキュメント全体を通して「AI Foundry」から「Azure AI Foundry」に用語を統一するマイナーアップデートです。これにより、Azureサービスに関連する情報の一貫性と明確性が向上し、ユーザーへの正確な情報提供が可能になります。

## 新機能
- 特に新しい機能は追加されていません。

## 破壊的変更
- 破壊的な変更はありません。

## その他の更新
- ドキュメント内の用語を統一し、正確性を高めるためのマイナーな修正が複数のファイルに適用されました。

# インサイト

この差分の内容は、Azure関連のドキュメントにおける用語の一貫性を図るための修正です。この修正により、Azureサービスを利用するユーザーに対して、どのようなサービスが提供されているかを明確に示すことができます。

一般的に技術的な文書やガイドラインにおいて、用語の正確性と一貫性は非常に重要です。用語が統一されていないと、ユーザーに混乱を招く可能性があり、サービスの使い方やそれに関連する操作手順について誤解が生じることがあります。そのため、今回行われた「AI Foundry」から「Azure AI Foundry」への用語変更は、単なるマイナーアップデートであっても、非常に重要な役割を果たします。

Azureサービスは多岐にわたる機能を持っており、それぞれのサービスが提供する機能やサービスの名前が直感的に理解できることは、ユーザーエクスペリエンスの向上につながります。特に、技術者や開発者がドキュメントを参照する際には、用語の統一性が高いことがプロジェクトのスムーズな推進に寄与します。

また、この更新によって、ドキュメントはよりグローバルな観点から見ても一貫したものとなり、さまざまな国や地域のユーザーに対しても正確で信頼性の高い情報を提供することができます。将来的な機能追加やサービスの拡張を見据えたとき、こうした細かなアップデートを逐次反映させていくことが、長期的にはユーザー基盤の維持や拡大に寄与するものと言えるでしょう。

全体として、この一連の変更は、「Azure AI Foundry」としてのブランドやサービスの認知を高めるための基盤づくりに有効なものであり、今後のAzureサービスの発展に寄与するものと考えられます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-azure-openai-embedding.md](#item-3eca57) | minor update | Azure AI Foundryポータルの言及の修正 | modified | 1 | 1 | 2 | 
| [index.yml](#item-c67121) | minor update | AI Foundryポータルの名称修正 | modified | 1 | 1 | 2 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | AI Foundryポータルの名称の一貫性向上 | modified | 2 | 2 | 4 | 
| [search-import-data-portal.md](#item-b804d1) | minor update | AI Foundryモデルカタログの名称修正 | modified | 1 | 1 | 2 | 
| [vector-search-integrated-vectorization-ai-studio.md](#item-353fcc) | minor update | Azure AI Foundry関連用語の修正 | modified | 11 | 11 | 22 | 
| [vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md](#item-ebe7a3) | minor update | Azure AI Foundry関連用語の修正 | modified | 3 | 3 | 6 | 
| [vector-search-vectorizer-azure-open-ai.md](#item-e75cee) | minor update | Azure AI Foundry関連用語の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/cognitive-search-skill-azure-openai-embedding.md{#item-3eca57}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ The **Azure OpenAI Embedding** skill connects to a deployed embedding model on y
 
 Your Azure OpenAI Service must have an associated [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains). If the service was created through the Azure portal, this subdomain is automatically generated as part of your service setup. Ensure that your service includes a custom subdomain before using it with the Azure AI Search integration.
 
-Azure OpenAI Service resources (with access to embedding models) that were created in AI Foundry portal aren't supported. Only the Azure OpenAI Service resources created in the Azure portal are compatible with the **Azure OpenAI Embedding** skill integration.
+Azure OpenAI Service resources (with access to embedding models) that were created in Azure AI Foundry portal aren't supported. Only the Azure OpenAI Service resources created in the Azure portal are compatible with the **Azure OpenAI Embedding** skill integration.
 
 The [Import and vectorize data wizard](search-get-started-portal-import-vectors.md) in the Azure portal uses the **Azure OpenAI Embedding** skill to vectorize content. You can run the wizard and review the generated skillset to see how the wizard builds the skill for embedding models. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルの言及の修正"
}
```

### Explanation
このコードの変更は、ドキュメント内の「Azure AI Foundry ポータル」への言及を修正するマイナーな更新です。具体的には、文中の表現を微調整し、「AI Foundry portal」という表記を「Azure AI Foundry portal」に変更したことで、読者に対してより明確な情報を提供しています。この変更は、全体の意味を変更するものではなく、正確性を改善するためのものです。ファイルは「cognitive-search-skill-azure-openai-embedding.md」であり、2つの行が変更され、1行が追加され、1行が削除されています。変更の影響は軽微ですが、正確な情報の提供は重要です。

## articles/search/index.yml{#item-c67121}

<details>
<summary>Diff</summary>
````diff
@@ -67,7 +67,7 @@ landingContent:
     linkLists:
       - linkListType: how-to-guide
         links:
-          - text: Create a vector index in AI Foundry portal
+          - text: Create a vector index in Azure AI Foundry portal
             url: /azure/ai-studio/how-to/index-add
           - text: Chat with your data using Azure OpenAI
             url: /azure/ai-services/openai/use-your-data-quickstart
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryポータルの名称修正"
}
```

### Explanation
このコードの変更は、「AI Foundry portal」という表現を「Azure AI Foundry portal」に修正するマイナーな更新です。この変更により、所定のリンクリスト内で、Azureサービスに関連する情報の正確性が向上します。具体的には、`index.yml`ファイルの一部で、ベクターインデックスを作成する方法に関するガイドがより明確に記載されるようになりました。この変更は、ドキュメントの内容に対する利用者の理解を助けるために重要です。全体として、ユーザーに提供される情報が正確かつ一貫性を持つように配慮されています。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -52,7 +52,7 @@ Use an embedding model on an Azure AI platform in the [same region as Azure AI S
 
 If you use the Azure OpenAI Service, the endpoint must have an associated [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains). A custom subdomain is an endpoint that includes a unique name (for example, `https://hereismyuniquename.cognitiveservices.azure.com`). If the service was created through the Azure portal, this subdomain is automatically generated as part of your service setup. Ensure that your service includes a custom subdomain before using it with the Azure AI Search integration.
 
-Azure OpenAI Service resources (with access to embedding models) that were created in AI Foundry portal aren't supported. Only the Azure OpenAI Service resources created in the Azure portal are compatible with the **Azure OpenAI Embedding** skill integration.
+Azure OpenAI Service resources (with access to embedding models) that were created in Azure AI Foundry portal aren't supported. Only the Azure OpenAI Service resources created in the Azure portal are compatible with the **Azure OpenAI Embedding** skill integration.
 
 ### Public endpoint requirements
 
@@ -323,7 +323,7 @@ Chunking is built in and nonconfigurable. The effective settings are:
 
    + For Azure OpenAI, choose an existing deployment of text-embedding-ada-002, text-embedding-3-large, or text-embedding-3-small.
 
-   + For AI Foundry catalog, choose an existing deployment of an Azure or Cohere embedding model.
+   + For Azure AI Foundry catalog, choose an existing deployment of an Azure or Cohere embedding model.
 
    + For AI Vision multimodal embeddings, select the account.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryポータルの名称の一貫性向上"
}
```

### Explanation
このコードの変更は、「AI Foundry portal」および「AI Foundry catalog」という表現を「Azure AI Foundry portal」および「Azure AI Foundry catalog」に修正することによって、一貫性を持たせるマイナーな更新です。具体的には、`search-get-started-portal-import-vectors.md`ファイルの中で、Azureサービスに関連した言及がより明確になりました。この変更により、利用者がそれぞれのサービスを識別しやすくなり、正確な情報提供が実現します。また、他の部分では文体や用語の整合性が保たれることで、全体の読解性が向上しています。変更行は合計で4行で、2行が追加され、2行が削除されています。

## articles/search/search-import-data-portal.md{#item-b804d1}

<details>
<summary>Diff</summary>
````diff
@@ -72,7 +72,7 @@ Here are some points to keep in mind about the skills in the following list:
 |------|--------------------|----------------------------------|
 | [AI Vision multimodal](cognitive-search-skill-vision-vectorize.md)  | ❌ | ✅ |
 | [Azure OpenAI embedding](cognitive-search-skill-azure-openai-embedding.md)  | ❌ | ✅ |
-| [Azure Machine Learning (AI Foundry model catalog)](cognitive-search-aml-skill.md)  | ❌ | ✅ |
+| [Azure Machine Learning (Azure AI Foundry model catalog)](cognitive-search-aml-skill.md)  | ❌ | ✅ |
 | [Document layout](cognitive-search-skill-document-intelligence-layout.md)  | ❌ | ✅ |
 | [Entity recognition](cognitive-search-skill-entity-recognition-v3.md)  | ✅ | ❌ |
 | [Image analysis (applies to blobs, default parsing, whole file indexing](cognitive-search-skill-image-analysis.md)  | ✅ | ❌ |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Foundryモデルカタログの名称修正"
}
```

### Explanation
このコードの変更は、「AI Foundry model catalog」という表現を「Azure AI Foundry model catalog」に修正する内容のマイナーな更新です。具体的には、`search-import-data-portal.md`ファイル内のスキルリストにおいて、Azureサービスに関する用語の一貫性が向上しました。この変更により、ユーザーはAzureのリソースをより正確に識別でき、関連する情報の理解が促進されます。変更は2行に及び、1行が追加され、1行が削除されています。全体として、この修正はドキュメントの明瞭性を高め、ユーザーの混乱を避けるために重要です。

## articles/search/vector-search-integrated-vectorization-ai-studio.md{#item-353fcc}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Integrated vectorization with models from Azure AI Foundry
 titleSuffix: Azure AI Search
-description: Learn  how to vectorize content during indexing on Azure AI Search with an AI Foundry model.
+description: Learn  how to vectorize content during indexing on Azure AI Search with an Azure AI Foundry model.
 author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
@@ -20,7 +20,7 @@ In this article, learn how to access the embedding models in the [Azure AI Found
 
 The workflow includes model deployment steps. The model catalog includes embedding models from Microsoft and other companies. Deploying a model is billable per the billing structure of each provider. 
 
-After the model is deployed, you can use it for [integrated vectorization](vector-search-integrated-vectorization.md) during indexing, or with the [AI Foundry vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) for queries.
+After the model is deployed, you can use it for [integrated vectorization](vector-search-integrated-vectorization.md) during indexing, or with the [Azure AI Foundry vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) for queries.
 
 > [!TIP]
 > Use the [**Import and vectorize data**](search-get-started-portal-import-vectors.md) wizard to generate a skillset that includes an AML skill for deployed embedding models on Azure AI Foundry. AML skill definition for inputs, outputs, and mappings are generated by the wizard, which gives you an easy way to test a model before writing any code.
@@ -65,7 +65,7 @@ For image embeddings:
 
     Optionally, you can change your endpoint to use **Token authentication** instead of **Key authentication**. If you enable token authentication, you only need to copy the URI and model name,  but make a note of which region the model is deployed to.
 
-    :::image type="content" source="media\vector-search-integrated-vectorization-ai-studio\ai-studio-fields-to-copy.png" lightbox="media\vector-search-integrated-vectorization-ai-studio\ai-studio-fields-to-copy.png" alt-text="Screenshot of a deployed endpoint in AI Foundry portal highlighting the fields to copy and save for later.":::
+    :::image type="content" source="media\vector-search-integrated-vectorization-ai-studio\ai-studio-fields-to-copy.png" lightbox="media\vector-search-integrated-vectorization-ai-studio\ai-studio-fields-to-copy.png" alt-text="Screenshot of a deployed endpoint in Azure AI Foundry portal highlighting the fields to copy and save for later.":::
 
 1. You can now configure a search index and indexer to use the deployed model. 
 
@@ -81,7 +81,7 @@ This section describes the AML skill definition and index mappings. It includes
 
 <!-- ### [**Text Input for "Inference" API**](#tab/inference-text)
 
-This AML skill payload works with the following models from AI Foundry:
+This AML skill payload works with the following models from Azure AI Foundry:
 
 + Cohere-embed-v3-english
 + Cohere-embed-v3-multilingual
@@ -126,7 +126,7 @@ The URI and key are generated when you deploy the model from the catalog. For mo
 
 ### [**Facebook embedding models**](#tab/inference-image)
 
-This AML skill payload works with the following image embedding models from AI Foundry:
+This AML skill payload works with the following image embedding models from Azure AI Foundry:
 
 + Facebook-DinoV2-Image-Embeddings-ViT-Base
 + Facebook-DinoV2-Image-Embeddings-ViT-Giant
@@ -172,14 +172,14 @@ The URI and key are generated when you deploy the model from the catalog. For mo
 
 ### [**Cohere embedding models**](#tab/cohere)
 
-This AML skill payload works with the following text embedding models from AI Foundry:
+This AML skill payload works with the following text embedding models from Azure AI Foundry:
 
 + Cohere-embed-v3-english
 + Cohere-embed-v3-multilingual
 
 It assumes that you're chunking your content using the Text Split skill and therefore your text to be vectorized is in the `/document/pages/*` path. If your text comes from a different path, update all references to the `/document/pages/*` path accordingly.
 
-You must add the `/v1/embed` path onto the end of the URL that you copied from your AI Foundry deployment. You might also change the values for the `input_type`, `truncate` and `embedding_types` inputs to better fit your use case. For more information on the available options, review the [Cohere Embed API reference](/azure/ai-studio/how-to/deploy-models-cohere-embed).
+You must add the `/v1/embed` path onto the end of the URL that you copied from your Azure AI Foundry deployment. You might also change the values for the `input_type`, `truncate` and `embedding_types` inputs to better fit your use case. For more information on the available options, review the [Cohere Embed API reference](/azure/ai-studio/how-to/deploy-models-cohere-embed).
 
 The URI and key are generated when you deploy the model from the catalog. For more information about these values, see [How to deploy Cohere Embed models with Azure AI Foundry](/azure/ai-studio/how-to/deploy-models-cohere-embed).
 
@@ -243,11 +243,11 @@ If you selected a different `embedding_types` in your skill definition that you
 
 ---
 
-## Sample AI Foundry vectorizer payload
+## Sample Azure AI Foundry vectorizer payload
 
-The [AI Foundry vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md), unlike the AML skill, is tailored to work only with those embedding models that are deployable via the AI Foundry model catalog. The main difference is that you don't have to worry about the request and response payload, but you do have to provide the `modelName`, which corresponds to the "Model ID" that you copied after deploying the model in AI Foundry portal. 
+The [Azure AI Foundry vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md), unlike the AML skill, is tailored to work only with those embedding models that are deployable via the Azure AI Foundry model catalog. The main difference is that you don't have to worry about the request and response payload, but you do have to provide the `modelName`, which corresponds to the "Model ID" that you copied after deploying the model in Azure AI Foundry portal. 
 
-Here's a sample payload of how you would configure the vectorizer on your index definition given the properties copied from AI Foundry.
+Here's a sample payload of how you would configure the vectorizer on your index definition given the properties copied from Azure AI Foundry.
 
 For Cohere models, you should NOT add the `/v1/embed` path to the end of your URL like you did with the skill.
 
@@ -267,7 +267,7 @@ For Cohere models, you should NOT add the `/v1/embed` path to the end of your UR
 
 ## Connect using token authentication
 
-If you can't use key-based authentication, you can instead configure the AML skill and AI Foundry vectorizer connection for [token authentication](../machine-learning/how-to-authenticate-online-endpoint.md) via role-based access control on Azure. The search service must have a [system or user-assigned managed identity](search-howto-managed-identities-data-sources.md), and the identity must have Owner or Contributor permissions for your AML project workspace. You can then remove the key field from your skill and vectorizer definition, replacing it with the resourceId field. If your AML project and search service are in different regions, also provide the region field.
+If you can't use key-based authentication, you can instead configure the AML skill and Azure AI Foundry vectorizer connection for [token authentication](../machine-learning/how-to-authenticate-online-endpoint.md) via role-based access control on Azure. The search service must have a [system or user-assigned managed identity](search-howto-managed-identities-data-sources.md), and the identity must have Owner or Contributor permissions for your AML project workspace. You can then remove the key field from your skill and vectorizer definition, replacing it with the resourceId field. If your AML project and search service are in different regions, also provide the region field.
 
 ```json
 "uri": "<YOUR_URL_HERE>",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundry関連用語の修正"
}
```

### Explanation
このコードの変更は、「AI Foundry」という表現を「Azure AI Foundry」に統一するためのマイナーな更新です。具体的には、`vector-search-integrated-vectorization-ai-studio.md`ファイル内で、Azureサービスに関する用語をより明確にするための修正が行われました。この変更により、ユーザーがAzureのリソースを誤解なく理解できるようになり、関連する情報の認識も向上します。変更は合計で22行に及び、11行が追加され、11行が削除されています。この更新によって、ドキュメントの全体的な一貫性と明瞭性が増し、使用者にとっての利便性が向上しています。

## articles/search/vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md{#item-ebe7a3}

<details>
<summary>Diff</summary>
````diff
@@ -27,7 +27,7 @@ Parameters are case-sensitive. Which parameters you choose to use depends on wha
 | Parameter name | Description |
 |--------------------|-------------|
 | `uri` | (Required) The [URI of the AML online endpoint](../machine-learning/how-to-authenticate-online-endpoint.md) to which the _JSON_ payload is sent. Only the **https** URI scheme is allowed. |
-| `modelName` | (Required) The model ID from the AI Foundry model catalog that is deployed at the provided endpoint. Supported models are: <ul><li>Facebook-DinoV2-Image-Embeddings-ViT-Base </li><li>Facebook-DinoV2-Image-Embeddings-ViT-Giant </li><li>Cohere-embed-v3-english </li><li>Cohere-embed-v3-multilingual</ul> |
+| `modelName` | (Required) The model ID from the Azure AI Foundry model catalog that is deployed at the provided endpoint. Supported models are: <ul><li>Facebook-DinoV2-Image-Embeddings-ViT-Base </li><li>Facebook-DinoV2-Image-Embeddings-ViT-Giant </li><li>Cohere-embed-v3-english </li><li>Cohere-embed-v3-multilingual</ul> |
 | `key` | (Required for [key authentication](#WhatParametersToUse)) The [key for the AML online endpoint](../machine-learning/how-to-authenticate-online-endpoint.md). |
 | `resourceId` | (Required for [token authentication](#WhatParametersToUse)). The Azure Resource Manager resource ID of the AML online endpoint. It should be in the format subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.MachineLearningServices/workspaces/{workspace-name}/onlineendpoints/{endpoint_name}. |
 | `region` | (Optional for [token authentication](#WhatParametersToUse)). The [region](https://azure.microsoft.com/global-infrastructure/regions/) the AML online endpoint is deployed in. Needed if the region is different from the region of the search service. |
@@ -47,7 +47,7 @@ Which authentication parameters are required depends on what authentication your
 
 ## Supported vector query types
 
-Which vector query types are supported by the AI Foundry model catalog vectorizer depends on the `modelName` that is configured.
+Which vector query types are supported by the Azure AI Foundry model catalog vectorizer depends on the `modelName` that is configured.
 
 | Embedding model | Supports `text` query | Supports `imageUrl` query | Supports `imageBinary` query |
 |--------------------|-------------|-------------|-------------|
@@ -58,7 +58,7 @@ Which vector query types are supported by the AI Foundry model catalog vectorize
 
 ## Expected field dimensions
 
-The expected field dimensions for a field configured with an AI Foundry model catalog vectorizer depend on the `modelName` that is configured.
+The expected field dimensions for a field configured with an Azure AI Foundry model catalog vectorizer depend on the `modelName` that is configured.
 
 | `modelName` | Expected dimensions |
 |--------------------|-------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundry関連用語の修正"
}
```

### Explanation
この変更は、`vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md`ファイル内の用語を「AI Foundry」から「Azure AI Foundry」に統一するためのマイナーな更新です。具体的には、モデルのIDに関連する説明とベクトルクエリタイプ、期待されるフィールド寸法のセクションで用語の修正が行われました。これにより、Azureに関連するリソースの一貫性が向上し、ユーザーに対して正確な情報を提供することが目的です。変更により6行が修正され、合計で3行が追加され、3行が削除されています。この更新は、ドキュメントがより明確で理解しやすくなることを意図しています。

## articles/search/vector-search-vectorizer-azure-open-ai.md{#item-e75cee}

<details>
<summary>Diff</summary>
````diff
@@ -29,7 +29,7 @@ Vectorizers are used at query time, but specified in index definitions, and refe
 
 Your Azure OpenAI Service must have an associated [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains). If the service was created through the Azure portal, this subdomain is automatically generated as part of your service setup. Ensure that your service includes a custom subdomain before using it with the Azure AI Search integration.
 
-Azure OpenAI Service resources (with access to embedding models) that were created in AI Foundry portal aren't supported. Only the Azure OpenAI Service resources created in the Azure portal are compatible with the **Azure OpenAI Embedding** skill integration. 
+Azure OpenAI Service resources (with access to embedding models) that were created in Azure AI Foundry portal aren't supported. Only the Azure OpenAI Service resources created in the Azure portal are compatible with the **Azure OpenAI Embedding** skill integration. 
 
 ## Vectorizer parameters
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundry関連用語の修正"
}
```

### Explanation
このコードの変更は、`vector-search-vectorizer-azure-open-ai.md`ファイルにおいて、用語の統一を目的としたマイナーな更新です。この更新では、「AI Foundry portal」という表現が「Azure AI Foundry portal」に修正され、Azure AIサービス関連の情報がより明確になりました。この修正は、正確な情報提供のために重要であり、ユーザーがリソースを正しく理解できるようにするために行われました。変更は合計で2行で、1行が追加され、1行が削除されています。この更新により、関連する用語の一貫性が保たれ、ドキュメント全体の明瞭性が向上しています。


