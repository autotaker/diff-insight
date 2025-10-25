---
date: '2025-10-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:782e48d...MicrosoftDocs:671a785
summary: このコードの変更は、Azure AI関連のモデルについてのドキュメントに軽微な修正を行い、主に最新のモデル情報を反映させることに重点が置かれています。重大な破壊的変更はありませんが、モデルの選択を促すための更新が行われています。具体的には、特定のモデルが削除され、その結果、ユーザーは利用状況に注意が必要です。また、全体的に情報の明確化やサンプルコードの更新が含まれ、Azure
  AI Foundryのユーザーにとって有用な内容となっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:782e48d...MicrosoftDocs:671a785){target="_blank"}

# Highlights
このコードの変更は、いくつかのドキュメントに対して軽微な修正を行い、特にAzure AI関連のモデルの記述や使用方法に焦点を当てています。主要な新機能としては、最新のモデル情報の反映や読者にとっての明瞭さの向上があります。重要な破壊的な変更は含まれていませんが、情報の整理と適切なモデル選択を促すための更新が行われています。

## New features
- 各ドキュメントにおける最新のモデル情報の反映。
- ベクトライザーやAIモデルの選択に関連する情報の明確化。
- 統合ベクトル化に関するガイドラインの最新化。

## Breaking changes
特に破壊的な変更は見られませんが、特定のモデル（Facebook-DinoV2-Image-Embeddings-ViT-Base/Giant）の削除があったため、これらを利用しているユーザーは注意が必要です。

## Other updates
- いくつかのドキュメントでは、日付の更新や文章の整合性に関する小規模な修正が含まれています。
- サンプルコードや参考リンクの更新。

# Insights
この一連の変更は、Azure AI Foundryのユーザーに向けた情報の正確性と関連性を高める狙いがあります。具体的には、Facebook-DinoV2系のモデルがいくつかリストから削除され、Cohereに関連するモデルの記載が強化されています。これは、最新のモデル状況を反映し、ユーザーが有効活用しやすくするためです。

設定ガイドやトラブルシューティングのガイドも含むこれらのドキュメントは、Azure AIを利用する際のハンドブックとして機能しますが、頻繁な技術更新に従って情報がアップデートされる必要があります。特にAIモデルの場合、モデルの選択肢が変わることで、ユーザーが直面する技術的課題やベストプラクティスのガイドラインも変化する可能性があります。そのため、これらのドキュメントを常に最新の状況に適応させることは、企業ユーザーなどの実務の現場でAzure AIサービスを利用する際に重要です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-setup.md](#item-e5e297) | minor update | エージェントリトリーバル設定の更新 | modified | 1 | 1 | 2 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | ベクトルインポートに関するドキュメントの修正 | modified | 2 | 2 | 4 | 
| [search-indexer-troubleshooting.md](#item-087365) | minor update | インデクサートラブルシューティングに関するガイドの更新 | modified | 15 | 5 | 20 | 
| [tutorial-rag-build-solution-models.md](#item-6796c9) | minor update | RAGソリューションモデルビルドチュートリアルの更新 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-configure-vectorizer.md](#item-30ffd8) | minor update | ベクトライザー設定方法に関するガイドの更新 | modified | 1 | 1 | 2 | 
| [vector-search-integrated-vectorization-ai-studio.md](#item-353fcc) | minor update | 統合ベクトル化に関するガイドの更新 | modified | 10 | 12 | 22 | 
| [vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md](#item-ebe7a3) | minor update | Azure Machine Learning ベクトライザーに関するガイドの更新 | modified | 11 | 5 | 16 | 


# Modified Contents
## articles/search/includes/quickstarts/agentic-retrieval-setup.md{#item-e5e297}

<details>
<summary>Diff</summary>
````diff
@@ -81,7 +81,7 @@ To get the endpoints for this quickstart, select both of the following tabs.
 
 ## Deploy models
 
-To use agentic retrieval, you must deploy two Azure OpenAI models to your Azure AI Foundry resource:
+To use agentic retrieval, you must deploy two Azure OpenAI models to your Azure AI Foundry project:
 
 + An embedding model for text-to-vector conversion. This quickstart uses `text-embedding-3-large`, but you can use any `text-embedding` model.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバル設定の更新"
}
```

### Explanation
この変更は、`agentic-retrieval-setup.md`ファイルにおける軽微な修正です。具体的には、エージェントリトリーバルを使用する際のAzure オープンAIモデルのデプロイメントに関する表現が改訂されています。元の文章では「Azure AI Foundry resource」と記されていましたが、新しい文では「Azure AI Foundry project」に変更されています。この修正は、サービスの用語をより正確に反映することを目的としています。また、テキストからベクトルへの変換を行う埋め込みモデルに関する情報も引き続き明記されています。全体として、この修正は内容の明瞭性と整合性を高めることを意図しています。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: quickstart
-ms.date: 10/08/2025
+ms.date: 10/24/2025
 ---
 
 # Quickstart: Vectorize text in the Azure portal
@@ -47,7 +47,7 @@ For integrated vectorization, use one of the following embedding models. Deploym
 | Provider | Supported models |
 |--|--|
 | [Azure OpenAI in Azure AI Foundry Models resource](/azure/ai-services/openai/how-to/create-resource) <sup>1, 2</sup> | For text:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large |
-| [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects) | For text:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large<br><br>For images:<br>Facebook-DinoV2-Image-Embeddings-ViT-Base<br>Facebook-DinoV2-Image-Embeddings-ViT-Giant |
+| [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects) | For text:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large |
 | [Azure AI Foundry hub-based project](/azure/ai-foundry/how-to/hub-create-projects) | For text:<br>text-embedding-ada-002<br>text-embedding-3-small<br>text-embedding-3-large<br><br>For text and images:<br>Cohere-embed-v3-english <sup>3</sup><br>Cohere-embed-v3-multilingual <sup>3</sup> |
 | [Azure AI services multi-service resource](/azure/ai-services/multi-service-resource#azure-ai-multi-services-resource-for-azure-ai-search-skills) <sup>4</sup> | For text and images: [Azure AI Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) <sup>5</sup></li> |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルインポートに関するドキュメントの修正"
}
```

### Explanation
この変更は、`search-get-started-portal-import-vectors.md`ファイルにおいて、小規模な修正を行ったものです。主な修正内容は、日付の更新といくつかのテキスト表現の整合性に関するものです。具体的には、ドキュメントの発行日が「10/08/2025」から「10/24/2025」に変更され、提案されたモデルのセクションにおける情報が明確化されています。特に、Azure AI Foundryプロジェクトに関連するモデルについての記述が整理され、より一貫したフォーマットが適用されています。この更新は、読者がドキュメントの内容をより理解しやすくすることを目指しています。

## articles/search/search-indexer-troubleshooting.md{#item-087365}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 10/06/2025
+ms.date: 10/23/2025
 ms.update-cycle: 365-days
 ---
 
@@ -19,10 +19,20 @@ Occasionally, indexers run into problems that don't produce errors or that occur
 > [!NOTE]
 > If you have an Azure AI Search error to investigate, see [Troubleshooting common indexer errors and warnings](cognitive-search-common-errors-warnings.md) instead.
 
-## Best practice: indexers are designed to run on a schedule
-> For reliable indexing, configure your indexers to run on a [regular schedule](search-howto-schedule-indexers.md). Scheduled runs automatically pick up any documents missed in previous runs due to transient errors, network interruptions, or temporary service issues. This approach helps maintain data consistency and minimizes the need for manual intervention.  
->  
-> For [large data sources](search-how-to-large-index.md), the initial enumeration and indexing can take hours or even days. Running your indexer on a schedule allows that progress continues and errors are retried automatically. Avoid relying solely on manual or on-demand indexer runs, as these do not provide the same reliability or transient error recovery.  
+## Best practices
+
+These are some best practices and recommendations when working with indexers:
+
+### Indexers are designed to run on a schedule
+
+- For reliable indexing, configure your indexers to run on a [regular schedule](search-howto-schedule-indexers.md). Scheduled runs automatically pick up any documents missed in previous runs due to transient errors, network interruptions, or temporary service issues. This approach helps maintain data consistency and minimizes the need for manual intervention.  
+- For [large data sources](search-how-to-large-index.md), the initial enumeration and indexing can take hours or even days. Running your indexer on a schedule allows that progress continues and errors are retried automatically. Avoid relying solely on manual or on-demand indexer runs, as these do not provide the same reliability or transient error recovery.
+
+### Indexers provide best-effort indexing over time
+
+- Built-in indexers are designed to process all documents without permanent errors over time, if not in the current run, then in subsequent scheduled runs. They offer a convenient, low/no-code way to index data for common scenarios, enabling faster development and easier maintenance. However, if they have AI enrichment capabilities, they are not optimized for very large-scale workloads. For guidance on handling large datasets, see [how to index large data sets](search-how-to-large-index.md).
+- If your solution requires strict control over indexing timelines, use the Push APIs instead, such as the [Documents Index REST API](/rest/api/searchservice/documents) or the [IndexDocuments method (Azure SDK for .NET)](/dotnet/api/azure.search.documents.searchclient.indexdocuments). These options give you full control of the indexing pipeline.
+- Indexers can occasionally fall out of schedule. While this is uncommon and auto-recovery mechanisms exist, recovery may take time. This behavior is expected.
 
 <a name="connection-errors"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサートラブルシューティングに関するガイドの更新"
}
```

### Explanation
この変更は、`search-indexer-troubleshooting.md`ファイルにおける更新です。主な修正点として、日付の更新に加え、インデクサーに関するベストプラクティスのセクションが新たに導入されています。具体的には、インデクサーのスケジュール設定に関するポイントが強調されており、定期的な実行がデータの一貫性を維持し、手動介入の必要性を最小限に抑えることが説明されています。また、大規模なデータソースにおける初期インデクシングの時間がかかることや、インデクサーが時にはスケジュールから外れることも記載されています。

加えて、インデクサーが持つ利点として、時間をかけてすべてのドキュメントを処理することができる設計であること、AIエンリッチメント機能を搭載した場合は非常に大規模なワークロードに最適化されていないこと、また厳密なインデクシングのタイムライン管理が必要な場合はPush APIを利用するべきことも説明されています。この情報は、ユーザーがインデクサーを効果的に活用するためのガイドラインを提供しています。

## articles/search/tutorial-rag-build-solution-models.md{#item-6796c9}

<details>
<summary>Diff</summary>
````diff
@@ -57,7 +57,7 @@ Azure AI Search provides skill and vectorizer support for the following embeddin
 |--------|------------------|-------|------------|
 | Azure OpenAI | text-embedding-ada-002<br>text-embedding-3-large<br>text-embedding-3-small | [AzureOpenAIEmbedding](cognitive-search-skill-azure-openai-embedding.md) | [AzureOpenAIEmbedding](vector-search-vectorizer-azure-open-ai.md) |
 | Azure AI Vision | multimodal 4.0 <sup>1</sup> | [AzureAIVision](cognitive-search-skill-vision-vectorize.md) | [AzureAIVision](vector-search-vectorizer-ai-services-vision.md) |
-| Azure AI Foundry model catalog | Facebook-DinoV2-Image-Embeddings-ViT-Base<br>Facebook-DinoV2-Image-Embeddings-ViT-Giant<br>Cohere-embed-v3-english<br>Cohere-embed-v3-multilingual<br>Cohere-embed-v4 <sup>1, 2</sup> | [AML](cognitive-search-aml-skill.md) <sup>3</sup> | [Azure AI Foundry model catalog](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) |
+| Azure AI Foundry model catalog | Cohere-embed-v3-english <sup>1</sup><br>Cohere-embed-v3-multilingual <sup>1</sup><br>Cohere-embed-v4 <sup>1, 2</sup> | [AML](cognitive-search-aml-skill.md) <sup>3</sup> | [Azure AI Foundry model catalog](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) |
 
 <sup>1</sup> Supports text and image vectorization.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションモデルビルドチュートリアルの更新"
}
```

### Explanation
この変更は、`tutorial-rag-build-solution-models.md`ファイルに対する小規模な修正です。主に、Azure AI Foundryモデルカタログに関する部分が更新されました。具体的には、"Facebook-DinoV2-Image-Embeddings-ViT-Base"と"Facebook-DinoV2-Image-Embeddings-ViT-Giant"がリストから削除され、"Cohere-embed-v3-english"、"Cohere-embed-v3-multilingual"、"Cohere-embed-v4"の記載が残る形となっています。

この更新は、ドキュメント内のモデル情報を整理し、ユーザーにより関連性の高い情報を提供することを目的としています。表形式での記載内容が明確にし、関連リンクも保持されているため、読者が必要なリソースに簡単にアクセスできるようになっています。

## articles/search/vector-search-how-to-configure-vectorizer.md{#item-30ffd8}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ The following table lists the embedding models that can be used with a vectorize
 | Vectorizer kind | Model names | Model provider | Associated skill |
 |-----------------|------------|----------------|------------------|
 | [`azureOpenAI`](vector-search-vectorizer-azure-open-ai.md) | text-embedding-ada-002<br>text-embedding-3 | Azure OpenAI | [AzureOpenAIEmbedding skill](cognitive-search-skill-azure-openai-embedding.md) |
-| [`aml`](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) | Facebook-DinoV2-Image-Embeddings<br>Cohere-embed-v3<br>Cohere-embed-v4 <sup>1</sup> | [Azure AI Foundry model catalog](vector-search-integrated-vectorization-ai-studio.md)  | [AML skill](cognitive-search-aml-skill.md) |
+| [`aml`](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) | Cohere-embed-v3<br>Cohere-embed-v4 <sup>1</sup> | [Azure AI Foundry model catalog](vector-search-integrated-vectorization-ai-studio.md)  | [AML skill](cognitive-search-aml-skill.md) |
 | [`aiServicesVision`](vector-search-vectorizer-ai-services-vision.md) | [Multimodal embeddings 4.0 API](/azure/ai-services/computer-vision/concept-image-retrieval) | Azure AI Vision (through an Azure AI services multi-service account) | [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) |
 | [`customWebApi`](vector-search-vectorizer-custom-web-api.md) | Any embedding model | Hosted externally | [Custom Web API skill](cognitive-search-custom-skill-web-api.md) |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトライザー設定方法に関するガイドの更新"
}
```

### Explanation
この変更は、`vector-search-how-to-configure-vectorizer.md`ファイルにおける軽微な更新です。更新の内容は、使われるベクトライザーのモデル名に関するテーブルの情報の修正です。具体的には、`aml`ベクトライザーに関連するモデル名から"Facebook-DinoV2-Image-Embeddings"が削除され、"Cohere-embed-v3"と"Cohere-embed-v4"が残されました。

この修正により、ドキュメントがより正確で関連性の高い情報を提供することになります。変更された情報は、Azure AIのユーザーがベクトライザーの設定を行う際に、利用可能なモデルを理解しやすくしており、適切な選択をする手助けとなります。

## articles/search/vector-search-integrated-vectorization-ai-studio.md{#item-353fcc}

<details>
<summary>Diff</summary>
````diff
@@ -33,15 +33,11 @@ After the model is deployed, you can use it for [integrated vectorization](vecto
 
 ## Supported embedding models
 
-Integrated vectorization and the [**Import data (new)** wizard](search-import-data-portal.md) support the following embedding models in the model catalog:
+Supported embedding models from the Azure AI Foundry model catalog vary by usage method:
 
-| Embedding type | Supported models |
-|--|--|
-| Text | Cohere-embed-v3-english<br>Cohere-embed-v3-multilingual |
-| Image | Facebook-DinoV2-Image-Embeddings-ViT-Base<br>Facebook-DinoV2-Image-Embeddings-ViT-Giant |
-| Text and image (multimodal) | Cohere-embed-v4 <sup>1</sup> |
++ For the latest list of models supported programmatically, see the [AML skill](cognitive-search-aml-skill.md) and [Azure AI Foundry model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) references.
 
-<sup>1</sup> At this time, you can only specify `embed-v-4-0` programmatically through the [AML skill](cognitive-search-aml-skill.md) or [Azure AI Foundry model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md), not through the Azure portal. However, you can use the portal to manage the skillset or vectorizer afterward.
++ For the latest list of models supported in the Azure portal, see [Quickstart: Vector search in the Azure portal](search-get-started-portal-import-vectors.md) and [Quickstart: Multimodal search in the Azure portal](search-get-started-portal-image-search.md).
 
 ## Deploy an embedding model from the Azure AI Foundry model catalog
 
@@ -75,9 +71,9 @@ Integrated vectorization and the [**Import data (new)** wizard](search-import-da
 
 ## Sample AML skill payloads
 
-When you deploy embedding models from the [Azure AI Foundry model catalog](https://ai.azure.com/explore/models) you connect to them using the [AML skill](cognitive-search-aml-skill.md) in Azure AI Search for indexing workloads.
+When you deploy embedding models from the Azure AI Foundry model catalog, you connect to them using the [AML skill](cognitive-search-aml-skill.md) in Azure AI Search for indexing workloads.
 
-This section describes the AML skill definition and index mappings. It includes sample payloads that are already configured to work with their corresponding deployed endpoints. For more technical details on how these payloads work, read about the [Skill context and input annotation language](cognitive-search-skill-annotation-language.md).
+This section describes the AML skill definition and index mappings. It includes sample payloads that are already configured to work with their corresponding deployed endpoints. For more technical details on how these payloads work, see the [Skill context and input annotation language](cognitive-search-skill-annotation-language.md).
 
 <!-- ### [**Text Input for "Inference" API**](#tab/inference-text)
 
@@ -124,6 +120,7 @@ The URI and key are generated when you deploy the model from the catalog. For mo
 }
 ``` -->
 
+<!--
 ### [**Facebook embedding models**](#tab/inference-image)
 
 This AML skill payload works with the following image embedding models from Azure AI Foundry:
@@ -171,8 +168,11 @@ The URI and key are generated when you deploy the model from the catalog. For mo
 ```
 
 ### [**Cohere embedding models**](#tab/cohere)
+-->
 
-This AML skill payload works with the following embedding models from Azure AI Foundry:
+### Cohere embedding models
+
+This AML skill payload works with the following embedding models:
 
 + Cohere-embed-v3-english
 + Cohere-embed-v3-multilingual
@@ -240,8 +240,6 @@ If you selected a different `embedding_types` in your skill definition, change `
 }
 ```
 
----
-
 ## Sample Azure AI Foundry vectorizer payload
 
 The [Azure AI Foundry vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md), unlike the AML skill, is tailored to work only with those embedding models that are deployable via the Azure AI Foundry model catalog. The main difference is that you don't have to worry about the request and response payload, but you do have to provide the `modelName`, which corresponds to the "Model ID" that you copied after deploying the model in [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs). 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "統合ベクトル化に関するガイドの更新"
}
```

### Explanation
この変更は、`vector-search-integrated-vectorization-ai-studio.md`ファイルに対する軽微な修正です。主に、サポートされている埋め込みモデルに関する表の説明が更新され、Azure AI Foundryモデルカタログにおける利用方法に焦点が当てられています。

具体的には、"Embedding type"と"Supported models"のセクションが再構成され、特定のモデル名のリストから"Facebook-DinoV2-Image-Embeddings"が削除され、Cohere関連のモデルランクがクリーンアップされました。また、最新のモデルリストへの参照が追加され、プログラム的にサポートされているモデルの最新情報を得るためにいくつかのリファレンスリンクが提供されています。

この修正により、ドキュメントは最新の情報を提供し、ユーザーがAzure AI Foundryモデルカタログを利用する際に必要なガイダンスを向上させています。さらに、サンプルのAMLスキルペイロードに関するセクションも改善され、文書全体の明瞭さが増しています。

## articles/search/vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md{#item-ebe7a3}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ Parameters are case-sensitive. Which parameters you choose to use depends on wha
 | Parameter name | Description |
 |--------------------|-------------|
 | `uri` | (Required) The [URI of the AML online endpoint](../machine-learning/how-to-authenticate-online-endpoint.md) to which the _JSON_ payload is sent. Only the **https** URI scheme is allowed. |
-| `modelName` | (Required) The model ID from the Azure AI Foundry model catalog that is deployed at the provided endpoint. Supported models are:<p><ul><li>Facebook-DinoV2-Image-Embeddings-ViT-Base </li><li>Facebook-DinoV2-Image-Embeddings-ViT-Giant </li><li>Cohere-embed-v3-english </li><li>Cohere-embed-v3-multilingual</li><li>Cohere-embed-v4</li></ul> |
+| `modelName` | (Required) The model ID from the Azure AI Foundry model catalog that is deployed at the provided endpoint. Supported models are:<p><ul><li></li><li>Cohere-embed-v3-english </li><li>Cohere-embed-v3-multilingual</li><li>Cohere-embed-v4</li></ul> |
 | `key` | (Required for [key authentication](#WhatParametersToUse)) The [key for the AML online endpoint](../machine-learning/how-to-authenticate-online-endpoint.md). |
 | `resourceId` | (Required for [token authentication](#WhatParametersToUse)). The Azure Resource Manager resource ID of the AML online endpoint. It should be in the format subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.MachineLearningServices/workspaces/{workspace-name}/onlineendpoints/{endpoint_name}. |
 | `region` | (Optional for [token authentication](#WhatParametersToUse)). The [region](https://azure.microsoft.com/global-infrastructure/regions/) the AML online endpoint is deployed in. Needed if the region is different from the region of the search service. |
@@ -52,24 +52,30 @@ Which vector query types are supported by the Azure AI Foundry model catalog vec
 
 | Embedding model | Supports `text` query | Supports `imageUrl` query | Supports `imageBinary` query |
 |--------------------|-------------|-------------|-------------|
-| Facebook-DinoV2-Image-Embeddings-ViT-Base |  | X | X |
-| Facebook-DinoV2-Image-Embeddings-ViT-Giant |  | X | X |
 | Cohere-embed-v3-english | X |  | X |
 | Cohere-embed-v3-multilingual | X |  | X |
 | Cohere-embed-v4 | X |  | X |
 
+<!--
+| Facebook-DinoV2-Image-Embeddings-ViT-Base |  | X | X |
+| Facebook-DinoV2-Image-Embeddings-ViT-Giant |  | X | X |
+-->
+
 ## Expected field dimensions
 
 The expected field dimensions for a vector field configured with an Azure AI Foundry model catalog vectorizer depend on the `modelName` that is configured.
 
 | `modelName` | Expected dimensions |
 |--------------------|-------------|
-| Facebook-DinoV2-Image-Embeddings-ViT-Base | 768 |
-| Facebook-DinoV2-Image-Embeddings-ViT-Giant | 1536 |
 | Cohere-embed-v3-english | 1024 |
 | Cohere-embed-v3-multilingual | 1024 |
 | Cohere-embed-v4 | 256–1536 |
 
+<!--
+| Facebook-DinoV2-Image-Embeddings-ViT-Base | 768 |
+| Facebook-DinoV2-Image-Embeddings-ViT-Giant | 1536 |
+-->
+
 ## Sample definition
 
 Suggested model names in the Azure AI Foundry model catalog consist of the base model plus a random three-letter suffix. The name of your model will be different from the one shown in this example.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Machine Learning ベクトライザーに関するガイドの更新"
}
```

### Explanation
この変更は、`vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md`ファイルにおける軽微な更新です。主な変更点は、サポートされているモデルに関する情報と期待されるフィールド次元の表です。

具体的には、`modelName`のセクションからFacebook-DinoV2モデルが削除され、Cohereモデルのみが残されています。この変更により、選択肢が絞られ、最新の情報に基づいた明確な指針が提供されます。また、これに続くサポートされるベクトルクエリタイプの表や、期待されるフィールド次元に関する表の一部も更新されていますが、Facebook-DinoV2に関する情報はコメントアウトされています。

最後に、サンプル定義のセクションが残されており、Azure AI Foundryモデルカタログでのモデル名の命名規則が説明されています。これによって、ユーザーは適切なモデルの選択と使用方法をより理解しやすくなっています。


