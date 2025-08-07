---
date: '2025-08-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:10d2435...MicrosoftDocs:09b644a
summary: 今回の変更では、Azure AI Searchに関連するドキュメント全般に軽微な更新や修正が行われ、特に新機能の詳細や既存情報の正確性が強化されました。新たに「生成検索」と「ベクトル検索」についてのクイックスタートやサンプルが追加され、ベクトル検索に関するセクションも大きく更新されました。また、特定のAPIキーやデータフィールドに関する誤記が修正され、ドキュメントの正確性が向上しました。さらには、リソースやサンプルリンクの追加、表現の改善が行われ、全体の可読性と一貫性も向上しています。これは、ユーザー体験の向上を目指し、より信頼性のあるデータを基にAzure
  AI Searchの機能を実装できるようにするためのものであり、ユーザーにとっての利便性が高まる内容となっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:10d2435...MicrosoftDocs:09b644a){target="_blank"}

<format>
# ハイライト
今回の変更では、Azure AI Searchに関連するドキュメント全般にわたる軽微な更新や修正が行われました。特に、新しい機能の詳細や既存情報の正確性強化が各文書において実施されています。

## 新機能
- 「生成検索（RAG）」や「ベクトル検索」に関する新しいクイックスタートやサンプルが追加され、ユーザーがより深くAzure AI Searchの機能を理解するための手助けとなっています。
- ベクトル検索と埋め込み生成に関するセクションが大幅に更新され、統合ベクトル化に関する詳細な情報が提供されています。

## 重大な変更
- 特定のAPIキーやデータフィールドに関する誤記の修正が行われ、ドキュメントの正確性が向上しました。

## その他の更新
- リソースやサンプルリンクの追加により、アクセス可能な情報源と資料が増加しています。
- 表現や専門用語の改善により、ドキュメント全体の可読性と一貫性が向上しました。

# インサイト
Azure AI Searchのドキュメントに対する今回の更新は、主にユーザー体験の向上と情報の正確性を意図したものです。これにより、ユーザーはより信頼性の高いデータを元にAzure AI Searchの機能を実装できるようになっています。具体的には、生成検索とベクトル検索に関する最新のサンプルやクイックスタートが追加され、実践的な実装スキルの向上が期待されます。また、ベクトル検索の埋め込み生成マニュアルは完全に刷新され、ベクトルの正規化やモデルの微調整に関する実用的なアドバイスが充実しており、ユーザーはこれらを活用して検索機能の精度と効率を高めることが可能です。

加えて、誤記やリンクの修正は、ユーザーが開発する際の混乱を減少させ、作業をスムーズに行うための基盤を提供しています。さらに、サンプルコードとそのドキュメントの整理は、デベロッパーが自分の技術レベルに合った情報を簡単に見つけ出し、学習を継続できるようサポートしています。

総じて、Azure AI Searchのドキュメントの精度と使用感が向上したことにより、ユーザーが即座に利益を享受でき、Azure AI Searchの実装において一層の成果を出すための助けとなるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-aml-skill.md](#item-51366c) | minor update | Cognitive Search AML Skill Document Update | modified | 26 | 25 | 51 | 
| [samples-dotnet.md](#item-12f3fa) | minor update | Azure AI Search .NET Samples Document Update | modified | 4 | 2 | 6 | 
| [samples-javascript.md](#item-82e67e) | minor update | Azure AI Search JavaScript Samples Document Update | modified | 15 | 2 | 17 | 
| [samples-python.md](#item-d2bf09) | minor update | Azure AI Search Python Samples Document Update | modified | 3 | 2 | 5 | 
| [search-agentic-retrieval-how-to-create.md](#item-310fbe) | minor update | Correction of API Key Placeholder in Agentic Retrieval Document | modified | 1 | 1 | 2 | 
| [search-lucene-query-architecture.md](#item-b0d568) | minor update | Correction of Inverted Index Count in Lucene Query Architecture Document | modified | 1 | 1 | 2 | 
| [vector-search-how-to-generate-embeddings.md](#item-e98f7b) | minor update | Comprehensive Update to Vector Search and Embedding Generation Document | modified | 185 | 41 | 226 | 


# Modified Contents
## articles/search/cognitive-search-aml-skill.md{#item-51366c}

<details>
<summary>Diff</summary>
````diff
@@ -9,56 +9,57 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: reference
-ms.date: 05/08/2025
+ms.date: 08/04/2025
 ---
 
 # AML skill in an Azure AI Search enrichment pipeline
 
 > [!IMPORTANT]
-> Support for indexer connections to the Azure AI Foundry model catalog is in public preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). Preview REST APIs support this skill.
+> Support for indexer connections to the Azure AI Foundry model catalog is in public preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). Preview REST APIs support this capability.
 
-The **AML** skill allows you to extend AI enrichment with a custom [Azure Machine Learning (AML)](../machine-learning/overview-what-is-azure-machine-learning.md) model or deployed base embedding model in the Azure AI Foundry model catalog. Once an AML model is [trained and deployed](../machine-learning/concept-azure-machine-learning-architecture.md#workspace), an **AML** skill integrates it into a skillset.
+Use the **AML** skill to extend AI enrichment with a deployed base embedding model from the [Azure AI Foundry model catalog](vector-search-integrated-vectorization-ai-studio.md) or a custom [Azure Machine Learning](../machine-learning/overview-what-is-azure-machine-learning.md) (AML) model. After an AML model is [trained and deployed](../machine-learning/concept-azure-machine-learning-architecture.md#workspace), the **AML** skill integrates the model into a skillset.
 
 ## AML skill usage
 
-Like other built-in skills, a custom **AML** skill has inputs and outputs. The inputs are sent to a deployed AML online endpoint as a JSON object. The output of the endpoint must be a JSON payload in the response, along with a success status code. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed. The response is expected to provide the outputs specified by your **AML** skill definition. Any other response is considered an error and no enrichments are performed.
+Like other built-in skills, a custom **AML** skill has inputs and outputs. The inputs are sent to a deployed AML online endpoint as a JSON object. The output of the endpoint must be a JSON payload in the response, along with a success status code. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed. The response should provide the outputs specified by your **AML** skill definition. Any other response is considered an error, and no enrichments are performed.
 
 > [!NOTE]
-> The indexer will retry twice for certain standard HTTP status codes returned from the AML online endpoint. These HTTP status codes are:
+> The indexer retries two times for certain standard HTTP status codes returned from the AML online endpoint. These HTTP status codes are:
+>
 > * `503 Service Unavailable`
 > * `429 Too Many Requests`
 
-The **AML** skill can be called with the 2024-07-01 stable API version or equivalent Azure SDK, or the 2024-05-01-preview API version for connections to the model catalog in Azure AI Foundry portal.
+You can call the **AML** skill with the 2024-07-01 stable API version or an equivalent Azure SDK. For connections to the model catalog in the Azure AI Foundry portal, use the 2024-05-01-preview API version or later.
 
 ## AML skill for models in Azure AI Foundry
 
-Starting in 2024-05-01-preview REST API and in the Azure portal (which also targets the 2024-05-01-preview), Azure AI Search provides the [Azure AI Foundry model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) for query time connections to the model catalog in Azure AI Foundry portal. If you want to use that vectorizer for queries, an **AML** skill is the *indexing counterpart* for generating embeddings using a model in the Azure AI Foundry model catalog. 
+Starting in the 2024-05-01-preview REST API and the Azure portal, which also targets the 2024-05-01-preview, Azure AI Search provides the [Azure AI Foundry model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) for query-time connections to the model catalog in the Azure AI Foundry portal. If you want to use that vectorizer for queries, the **AML** skill is the *indexing counterpart* for generating embeddings using a model from the model catalog.
 
-During indexing, the **AML** skill can connect to the model catalog to generate vectors for the index. At query time, queries can use a vectorizer to connect to the same model to vectorize text strings for a vector query. In this workflow, the **AML** skill and the model catalog vectorizer should be used together so that you're using the same embedding model for both indexing and queries. See [Use embedding models from Azure AI Foundry model catalog](vector-search-integrated-vectorization-ai-studio.md) for details and for a list of the [supported embedding models](vector-search-integrated-vectorization-ai-studio.md#supported-embedding-models).
+During indexing, the **AML** skill can connect to the model catalog to generate vectors for the index. At query time, queries can use a vectorizer to connect to the same model to vectorize text strings for a vector query. In this workflow, you should use the **AML** skill and the model catalog vectorizer together so that the same embedding model is used for indexing and queries. For more information, including a list of supported embedding models, see [Use embedding models from Azure AI Foundry model catalog](vector-search-integrated-vectorization-ai-studio.md).
 
-We recommend using the [**Import and vectorize data wizard**](search-get-started-portal-import-vectors.md) to generate a skillset that includes an AML skill for deployed embedding models on Azure AI Foundry. AML skill definition for inputs, outputs, and mappings are generated by the wizard, which gives you an easy way to test a model before writing any code.
+We recommend using the [**Import and vectorize data wizard**](search-get-started-portal-import-vectors.md) to generate a skillset that includes an AML skill for deployed embedding models in Azure AI Foundry. The wizard generates the AML skill definition for inputs, outputs, and mappings, providing an easy way to test a model before writing any code.
 
 ## Prerequisites
 
-* An [AML workspace](../machine-learning/concept-workspace.md) for a custom model that you create, or a project in Azure AI Foundry if an embedding model is deployed from the catalog.
-* An [Online endpoints (real-time)](../machine-learning/concept-endpoints-online.md) in this workspace for a custom model, or the model endpoint for embedding models deployed from the catalog.
+* An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects?tabs=ai-foundry&pivots=fdp-project) for an embedding model deployed from the catalog, or an [AML workspace](../machine-learning/concept-workspace.md) for a custom model that you create.
+* The model endpoint for an embedding model deployed from the catalog, or an [online endpoint (real-time)](../machine-learning/concept-endpoints-online.md) of your AML workspace for a custom model.
 
 ## @odata.type
 
 Microsoft.Skills.Custom.AmlSkill
 
 ## Skill parameters
 
-Parameters are case-sensitive. Which parameters you choose to use depends on what [authentication your AML online endpoint requires, if any](#WhatSkillParametersToUse)
+Parameters are case sensitive. The parameters you use depend on what [authentication your AML online endpoint requires](#WhatSkillParametersToUse), if any.
 
 | Parameter name | Description |
 |--------------------|-------------|
 | `uri` | (Required for [key authentication](#WhatSkillParametersToUse)) The [scoring URI of the AML online endpoint](../machine-learning/how-to-authenticate-online-endpoint.md) to which the _JSON_ payload is sent. Only the **https** URI scheme is allowed. For embedding models in the Azure AI Foundry model catalog, this is the target URI.|
 | `key` | (Required for [key authentication](#WhatSkillParametersToUse)) The [key for the AML online endpoint](../machine-learning/how-to-authenticate-online-endpoint.md) or the  |
-| `resourceId` | (Required for [token authentication](#WhatSkillParametersToUse)). The Azure Resource Manager resource ID of the AML online endpoint. It should be in the format `subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.MachineLearningServices/workspaces/{workspace-name}/onlineendpoints/{endpoint_name}`. |
+| `resourceId` | (Required for [token authentication](#WhatSkillParametersToUse)). The Azure Resource Manager resource ID of the AML online endpoint. Use the format `subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.MachineLearningServices/workspaces/{workspace-name}/onlineendpoints/{endpoint_name}`. |
 | `region` | (Optional for [token authentication](#WhatSkillParametersToUse)). The [region](https://azure.microsoft.com/global-infrastructure/regions/) the AML online endpoint is deployed in. |
-| `timeout` | (Optional) When specified, indicates the timeout for the http client making the API call. It must be formatted as an XSD "dayTimeDuration" value (a restricted subset of an [ISO 8601 duration](https://www.w3.org/TR/xmlschema11-2/#dayTimeDuration) value). For example, `PT60S` for 60 seconds. If not set, a default value of 30 seconds is chosen. The timeout can be set to a maximum of 230 seconds and a minimum of 1 second. |
-| `degreeOfParallelism` | (Optional) When specified, indicates the number of calls the indexer makes in parallel to the endpoint you have provided. You can decrease this value if your endpoint is failing under too high of a request load. You can raise it if your endpoint is able to accept more requests and you would like an increase in the performance of the indexer.  If not set, a default value of 5 is used. The degreeOfParallelism can be set to a maximum of 10 and a minimum of 1.
+| `timeout` | (Optional) When specified, indicates the timeout for the http client making the API call. It must be formatted as an XSD "dayTimeDuration" value, which is a restricted subset of an [ISO 8601 duration](https://www.w3.org/TR/xmlschema11-2/#dayTimeDuration) value. For example, `PT60S` for 60 seconds. If not set, a default value of 30 seconds is chosen. You can set the timeout to a minimum of 1 second and a maximum of 230 seconds. |
+| `degreeOfParallelism` | (Optional) When specified, indicates the number of calls the indexer makes in parallel to the endpoint you provide. You can decrease this value if your endpoint is failing under too high of a request load. You can raise it if your endpoint is able to accept more requests and you would like an increase in the performance of the indexer. If not set, a default value of 5 is used. You can set the degreeOfParallelism to a minimum of 1 and a maximum of 10. |
 
 <a name="WhatSkillParametersToUse"></a>
 
@@ -68,11 +69,11 @@ AML online endpoints provide two authentication options:
 
 * [Key-based authentication](../machine-learning/how-to-authenticate-online-endpoint.md). A static key is provided to authenticate scoring requests from AML skills. Set the `uri` and `key` parameters for this connection.
 
-* [Token-Based Authentication](../machine-learning/how-to-authenticate-online-endpoint.md), where the AML online endpoint is [deployed using token based authentication](../machine-learning/how-to-authenticate-online-endpoint.md). The Azure AI Search service's [managed identity](/azure/active-directory/managed-identities-azure-resources/overview) must be enabled and have a role assignment on workspace. The AML skill then uses the service's managed identity to authenticate against the AML online endpoint, with no static keys required. The search service identity must be an **Owner** or **Contributor**. Set the `resourceId` parameter, and if the search service is in a different region from the AML workspace, set the `region` parameter.
+* [Token-based authentication](../machine-learning/how-to-authenticate-online-endpoint.md), where the AML online endpoint is deployed using token-based authentication. The Azure AI Search service must have a [managed identity](/azure/active-directory/managed-identities-azure-resources/overview) and a role assignment on the AML workspace. The AML skill then uses the service's managed identity to authenticate against the AML online endpoint, with no static keys required. The search service identity must have the **Owner** or **Contributor** role. Set the `resourceId` parameter, and if the search service is in a different region from the AML workspace, set the `region` parameter.
 
 ## Skill inputs
 
-Skill inputs are a node of the [enriched document](cognitive-search-working-with-skillsets.md#enrichment-tree) that's created during *document cracking*. For example, it might be the root document, a normalized image, or the content of a blob. There are no predefined inputs for this skill. For inputs, you should specify one or more nodes that are populated at the time of the AML skill's execution.
+Skill inputs are a node of the [enriched document](cognitive-search-working-with-skillsets.md#enrichment-tree) created during *document cracking*. For example, it might be the root document, a normalized image, or the content of a blob. There are no predefined inputs for this skill. For inputs, you should specify one or more nodes that are populated at the time of the AML skill's execution.
 
 ## Skill outputs
 
@@ -102,7 +103,7 @@ Skill outputs are new nodes of an enriched document created by the skill. There
 
 ## Sample input JSON structure
 
-This _JSON_ structure represents the payload that is sent to your AML online endpoint. The top-level fields of the structure correspond to the "names" specified in the `inputs` section of the skill definition. The values of those fields are from the `source` of those fields (which could be from a field in the document, or potentially from another skill)
+This _JSON_ structure represents the payload sent to your AML online endpoint. The top-level fields of the structure correspond to the "names" specified in the `inputs` section of the skill definition. The values of those fields are from the "sources" of those fields, which could be from a field in the document or another skill.
 
 ```json
 {
@@ -112,7 +113,7 @@ This _JSON_ structure represents the payload that is sent to your AML online end
 
 ## Sample output JSON structure
 
-The output corresponds to the response returned from your AML online endpoint. The AML online endpoint should only return a _JSON_ payload (verified by looking at the `Content-Type` response header) and should be an object where the fields are enrichments matching the "names" in the `output` and whose value is considered the enrichment.
+The output corresponds to the response from your AML online endpoint. The AML online endpoint should only return a _JSON_ payload (verified by looking at the `Content-Type` response header) and should be an object where the fields are enrichments matching the "names" in the `output` and whose value is considered the enrichment.
 
 ```json
 {
@@ -166,16 +167,16 @@ The output corresponds to the response returned from your AML online endpoint. T
 
 ## Error cases
 
-In addition to your AML being unavailable or sending out nonsuccessful status codes, the following are considered erroneous cases:
+In addition to your AML being unavailable or sending nonsuccessful status codes, the following cases are considered errors:
 
-* The AML online endpoint returns a success status code, but the response indicates that it isn't `application/json`, then the response is considered invalid and no enrichments are performed.
+* The AML online endpoint returns a success status code, but the response indicates that it isn't `application/json`. The response is thus invalid, and no enrichments are performed.
 
 * The AML online endpoint returns invalid JSON.
 
-For cases when the AML online endpoint is unavailable or returns an HTTP error, a friendly error with any available details about the HTTP error is added to the indexer execution history.
+If the AML online endpoint is unavailable or returns an HTTP error, a friendly error with any available details about the HTTP error is added to the indexer execution history.
 
 ## See also
 
-+ [How to define a skillset](cognitive-search-defining-skillset.md)
-+ [AML online endpoint troubleshooting](../machine-learning/how-to-troubleshoot-online-endpoints.md)
-+ [Integrated vectorization with models from Azure AI Foundry](vector-search-integrated-vectorization-ai-studio.md)
++ [Create a skillset in Azure AI Search](cognitive-search-defining-skillset.md)
++ [Use embedding models from Azure AI Foundry model catalog](vector-search-integrated-vectorization-ai-studio.md)
++ [Troubleshoot Azure Machine Learning online endpoint deployment and scoring](../machine-learning/how-to-troubleshoot-online-endpoints.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cognitive Search AML Skill Document Update"
}
```

### Explanation
この変更は、Azure AI SearchのAMLスキルに関するドキュメントの更新を反映しています。主な追加点として、ドキュメント内での表現の明確化や表現の一貫性を保つための文言の修正が行われています。特に、AMLスキルの使用に関する重要な情報が正確かつわかりやすく説明されており、更新された日付や、プレビューAPIの使用に関する詳細も含まれています。

この変更により、ユーザーはAMLスキルの機能性や使用方法に関する最新の情報を得ることができ、文書の可読性が向上しています。また、いくつかの文で専門用語の使用が改良され、誤解を招く可能性のある表現が修正されています。全体として、ドキュメントはより使いやすく、情報が明確に伝わるものとなっています。

## articles/search/samples-dotnet.md{#item-12f3fa}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - devx-track-dotnet
   - ignite-2023
 ms.topic: concept-article
-ms.date: 05/30/2025
+ms.date: 08/06/2025
 ---
 
 # C# samples for Azure AI Search
@@ -54,7 +54,9 @@ Code samples from the Azure AI Search team demonstrate features and workflows. A
 | [create-mvc-app](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/create-mvc-app) |  [Tutorial: Add search to an ASP.NET Core (MVC) app](tutorial-csharp-create-mvc-app.md) | While most samples are console applications, this MVC sample uses a web page to front the sample Hotels index, demonstrating basic search, pagination, and other server-side behaviors.|
 | [quickstart](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/v11) | [Quickstart: Full-text search](search-get-started-text.md) | Covers the basic workflow for creating, loading, and querying a search index in C# using sample data. |
 | [quickstart-agentic-retrieval](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) | [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md) | Creates a knowledge agent in Azure AI Search to integrate LLM reasoning into query planning. |
-| [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | [Quickstart: Semantic ranking using the Azure SDKs](search-get-started-semantic.md) | Shows the index schema and query request for invoking semantic ranker. |
+| [quickstart-rag](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-rag) | [Quickstart: Generative search (RAG)](search-get-started-rag.md) | Uses grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
+| [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/blob/main/quickstart-semantic-search/) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Shows the index schema and query request for invoking semantic ranker. |
+| [quickstart-vector-search](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-vector-search) | [Quickstart: Vector search](search-get-started-vector.md) | Covers the basic workflow for indexing and querying vector data. |
 | [search-website](https://github.com/Azure-Samples/azure-search-static-web-app) | [Tutorial: Add search to web apps](tutorial-csharp-overview.md) | Demonstrates an end-to-end search app that includes bulk upload using the push APIs and a rich client for hosting the app and handling search requests.|
 | [tutorial-ai-enrichment](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/tutorial-ai-enrichment)  | [Tutorial: AI-generated searchable content from Azure blobs](tutorial-skillset.md) | Shows how to configure an indexer and skillset. |
 | [multiple-data-sources](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/multiple-data-sources)  | [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md) | Merges content from two data sources into one search index. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search .NET Samples Document Update"
}
```

### Explanation
この変更は、Azure AI Search用のC#サンプルに関するドキュメントの軽微な更新を示しています。主な変更点は、いくつかのサンプルリンクの追加および既存のリンクの順序を変更し、サンプルのバリエーションを豊かにすることを目的としています。また、ドキュメントの日付が更新され、新しいサンプルやチュートリアルの内容が加わることによって、使用者がアクセス可能なリソースの最新情報を提供しています。

具体的には、生成検索に関する新たなクイックスタートである「RAG（Retrieval-Augmented Generation）」が追加され、ベクトル検索に関するクイックスタートも含まれました。これにより、ユーザーはAzure AI Searchの機能をより深く理解し、さまざまなユースケースに応じた検索機能を実装するための具体例を得ることができるようになります。全体的に、この更新は、ユーザーが最新のサンプルとリソースを利用できるようにするための重要な改善となっています。

## articles/search/samples-javascript.md{#item-82e67e}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.custom:
   - devx-track-js
   - ignite-2023
 ms.topic: concept-article
-ms.date: 03/10/2025
+ms.date: 08/06/2025
 ---
 
 # JavaScript samples for Azure AI Search
@@ -31,7 +31,7 @@ Learn about the JavaScript code samples that demonstrate the functionality and w
 
 Code samples from the Azure SDK development team demonstrate API usage. You can find these samples in [**azure-sdk-for-js/tree/main/sdk/search/search-documents/samples**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples) on GitHub.
 
-### JavaScript SDK samples
+### JavaScript samples
 
 | Samples | Description |
 |---------|-------------|
@@ -57,11 +57,24 @@ Code samples from the Azure SDK development team demonstrate API usage. You can
 
 Code samples from the Azure AI Search team demonstrate features and workflows. Many of these samples are referenced in tutorials, quickstarts, and how-to articles. You can find these samples in [**Azure-Samples/azure-search-javascript-samples**](https://github.com/Azure-Samples/azure-search-javascript-samples) on GitHub.
 
+### JavaScript samples
+
 | Samples | Article |
 |---------|---------|
 | [quickstart](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) | Source code for the JavaScript portion of [Quickstart: Full-text search](search-get-started-text.md). Covers the basic workflow for creating, loading, and querying a search index using sample data. |
+| [quickstart-rag-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-rag-js) | Source code for the JavaScript portion of [Quickstart: Generative search (RAG)](search-get-started-rag.md). Uses grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
+| [quickstart-semantic-ranking-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-js) | Source code for the JavaScript portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). Shows the index schema and query request for invoking semantic ranker. |
+| [quickstart-vector-js](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-vector-js) | Source code for the JavaScript portion of [Quickstart: Vector search](search-get-started-vector.md). Covers the basic workflow for indexing and querying vector data. |
 | [bulk-insert](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/bulk-insert) | Source code for the JavaScript example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
 | [azure-functions](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/azure-function-search) | Source code for the JavaScript example of an Azure function that sends queries to a search service. You can substitute this JavaScript version of the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
+
+### TypesScript samples
+
+| Samples | Article |
+|---------|---------|
+| [quickstart-rag-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-rag-ts) | Source code for the TypeScript portion of [Quickstart: Generative search (RAG)](search-get-started-rag.md). Uses grounding data from Azure AI Search with a chat completion model from Azure OpenAI. |
+| [quickstart-semantic-ranking-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-ts) | Source code for the TypeScript portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). Shows the index schema and query request for invoking semantic ranker. |
+| [quickstart-vector-ts](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-vector-ts) | Source code for the TypeScript portion of [Quickstart: Vector search](search-get-started-vector.md). Covers the basic workflow for indexing and querying vector data. |
 > [!TIP]
 > Try the [Samples browser](/samples/browse/?languages=javascript&products=azure-cognitive-search) to search for Microsoft code samples in GitHub, filtered by product, service, and language.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search JavaScript Samples Document Update"
}
```

### Explanation
この変更は、Azure AI Search向けのJavaScriptサンプルに関するドキュメントの軽微な更新を示しています。主な目的は、サンプルの構造を改善し、更新された情報を反映させることです。更新された日付が示され、JavaScript SDKに関するサンプル群が整理され、特に生成検索やセマンティックランキングに関連する新しいクイックスタートが追加されました。

具体的には、JavaScriptおよびTypeScript用のサンプルが明確に区分され、各サンプルがどのようにAzure AI Searchの機能を示すかについてのリンクが強化されています。これにより、開発者は自らのニーズに適したサンプルコードにアクセスしやすくなり、Azure AI Searchの使用方法をより効果的に学ぶことができるようになります。また、サンプルブラウザへのリンクが追加され、ユーザーが他のMicrosoftコードサンプルを探しやすくするための便利なリソースも提供されています。全体として、この更新は、ページの可読性とユーザビリティを向上させるために重要な改善となっています。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: concept-article
-ms.date: 05/30/2025
+ms.date: 08/06/2025
 ---
 
 # Python samples for Azure AI Search
@@ -40,7 +40,8 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 | [Quickstart](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart) | Source code for the Python portion of [Quickstart: Full-text search](search-get-started-text.md). This sample covers the basic workflow for creating, loading, and querying a search index using sample data. |
 | [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval) | Source code for the Python portion of [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md). |
 | [Quickstart-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-RAG) | Source code for the Python portion of [Quickstart: Generative search (RAG) with grounding data from Azure AI Search](search-get-started-rag.md). |
-| [Quickstart-Semantic-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) | Source code for the Python portion of [Quickstart: Semantic ranking using the Azure SDKs](search-get-started-semantic.md). This sample shows the index schema and query request for invoking semantic ranker. |
+| [Quickstart-Semantic-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) | Source code for the Python portion of [Quickstart: Semantic ranking](search-get-started-semantic.md). This sample shows the index schema and query request for invoking semantic ranker. |
+| [Quickstart-Vector-Search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Vector-Search) | Source code for the Python portion of [Quickstart: Vector search](search-get-started-vector.md). Covers the basic workflow for indexing and querying vector data. |
 | [Tutorial-RAG](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Tutorial-RAG) | Source code for the Python portion of [How to build a RAG solution using Azure AI Search](tutorial-rag-build-solution.md).|
 | [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) | Source code for the Python portion of [Build an agent-to-agent retrieval solution using Azure AI Search](search-agentic-retrieval-how-to-pipeline.md). Unlike [Quickstart: Run agentic retrieval in Azure AI Search](search-get-started-agentic-retrieval.md), this sample incorporates Azure AI Agent for request orchestration. |
 | [azure-function-search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/azure-function-search) | Source code for the Python example of an Azure function that sends queries to a search service. You can substitute this Python version of the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search Python Samples Document Update"
}
```

### Explanation
この変更は、Azure AI Search向けのPythonサンプルに関するドキュメントの軽微な更新を示しています。主な変更点は、いくつかのサンプルの情報を更新し、関連するクイックスタートのリンクを追加したことです。また、ドキュメントの日付が更新され、より最新の情報を反映しています。

具体的には、生成検索（RAG）に関するクイックスタートやベクトル検索に関する新しいサンプルが追加され、これによりユーザーはAzure AI Searchのさまざまな機能にアクセスしやすくなります。今後の開発に役立つように、サンプルの説明も細かく記載されており、ユーザーが自分のプロジェクトに適したサンプルを選択しやすくなっています。全体的に、この更新は文書の明確性と有用性を向上させるための重要な改善をもたらしています。

## articles/search/search-agentic-retrieval-how-to-create.md{#item-310fbe}

<details>
<summary>Diff</summary>
````diff
@@ -106,7 +106,7 @@ You can use API keys if you don't have permission to create role assignments.
    # List Indexes
    GET https://{{search-url}}/indexes?api-version=2025-05-01-preview
       Content-Type: application/json
-      @api-key: {{search-api-ke}}
+      @api-key: {{search-api-key}}
    ```
 
 ## Check for existing knowledge agents
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Correction of API Key Placeholder in Agentic Retrieval Document"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエージェントリトリーバルの作成方法に関するドキュメントの軽微な修正を示しています。具体的には、APIキーのプレースホルダーに誤植があったため、その部分を修正しました。旧表記の「{{search-api-ke}}」が正しい表記「{{search-api-key}}」に変更されており、これによりユーザーが正確な情報を使用できるようになります。

この修正は、エージェントリトリーバル機能を実装する際に、APIキーを正しく示す重要な箇所であるため、文書の正確性を向上させるために重要です。全体として、この更新はユーザーの実装プロセスをスムーズにし、誤解を防ぐための措置となっています。

## articles/search/search-lucene-query-architecture.md{#item-b0d568}

<details>
<summary>Diff</summary>
````diff
@@ -266,7 +266,7 @@ Returning to our example, for the **title** field, the inverted index looks like
 | hotel | 1, 3 |
 | ocean | 4  |
 | playa | 3 |
-| resort | 3 |
+| resort | 2 |
 | retreat | 4 |
 
 In the title field, only *hotel* shows up in two documents: 1 and 3.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Correction of Inverted Index Count in Lucene Query Architecture Document"
}
```

### Explanation
この変更は、Luceneクエリアーキテクチャに関するドキュメントの軽微な修正を示しています。具体的には、逆インデックスの「resort」フィールドの出現回数が修正されました。点数が「3」から「2」に変更され、実際に「resort」という単語が出現するドキュメントが2つであることが正確に反映されています。

この修正は、文書内のデータの正確性と整合性を向上させ、ユーザーがLuceneを使用する際により正確な情報に基づいて理解を深める助けとなります。全体として、この更新は、文書の信頼性を強化するための重要な手続きであり、検索クエリのアーキテクチャを学ぶ際に役立つ内容を提供しています。

## articles/search/vector-search-how-to-generate-embeddings.md{#item-e98f7b}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Generate embeddings
+title: Generate Embeddings
 titleSuffix: Azure AI Search
 description: Learn how to generate embeddings for downstream indexing into an Azure AI Search index.
 author: haileytap
@@ -9,38 +9,196 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 06/11/2025
+ms.date: 08/06/2025
 ---
 
 # Generate embeddings for search queries and documents
 
-Azure AI Search doesn't host embedding models, so one of your challenges is creating vectors for query inputs and outputs. You can use any supported embedding model, but this article assumes Azure OpenAI embedding models for illustration.
+Azure AI Search doesn't host embedding models, so you're responsible for creating vectors for query inputs and outputs. Choose one of the following approaches:
 
-We recommend [integrated vectorization](vector-search-integrated-vectorization.md), which provides built-in data chunking and vectorization. Integrated vectorization takes a dependency on indexers, skillsets, and built-in or custom skills that point to a model that executes externally from Azure AI Search. Several built-in skills point to embedding models in Azure AI Foundry, which makes integrated vectorization your easiest solution for solving the embedding challenge.
+| Approach | Description |
+| --- | --- |
+| [Integrated vectorization](vector-search-integrated-vectorization.md) | Use built-in data chunking and vectorization in Azure AI Search. This approach takes a dependency on indexers, skillsets, and built-in or custom skills that point to external embedding models, such as those in Azure AI Foundry. |
+| Manual vectorization | Manage data chunking and vectorization yourself. For indexing, you [push prevectorized documents](vector-search-how-to-create-index.md#load-vector-data-for-indexing) into vector fields in a search index. For querying, you [provide precomputed vectors](#generate-an-embedding-for-an-improvised-query) to the search engine. For demos of this approach, see the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples/tree/main) GitHub repository. |
 
-If you want to handle data chunking and vectorization yourself, we provide demos in the [sample repository](https://github.com/Azure/azure-search-vector-samples/tree/main) that show you how to integrate with other community solutions.
+We recommend integrated vectorization for most scenarios. Although you can use any supported embedding model, this article uses Azure OpenAI models for illustration.
 
 ## How embedding models are used in vector queries
 
-+ Query inputs are either vectors, or text or images that are converted to vectors during query processing. The built-in solution in Azure AI Search is to use a vectorizer. 
+Embedding models generate vectors for both query inputs and query outputs. Query inputs include:
 
-  Alternatively, you can also handle the conversion yourself by passing the query input to an embedding model of your choice. To avoid [rate limiting](/azure/ai-services/openai/quotas-limits), you can implement retry logic in your workload. For the Python demo, we used [tenacity](https://pypi.org/project/tenacity/).
++ **Text or images that are converted to vectors during query processing**. As part of integrated vectorization, a [vectorizer](vector-search-how-to-configure-vectorizer.md) performs this task.
 
-+ Query outputs are any matching documents found in a search index. Your search index must have been previously loaded with documents having one or more vector fields with embeddings. Whatever embedding model you used for indexing, use that same model for queries.
++ **Precomputed vectors**. You can generate these vectors by passing the query input to an embedding model of your choice. To avoid [rate limiting](/azure/ai-services/openai/quotas-limits), implement retry logic in your workload. Our [Python demo](https://github.com/Azure/azure-search-vector-samples/tree/93c839591bf92c2f10001d287871497b0f204a7c/demo-python) uses [tenacity](https://pypi.org/project/tenacity/).
+
+Based on the query input, the search engine retrieves matching documents from your search index. These documents are the query outputs.
+
+Your search index must already contain documents with one or more vector fields populated by embeddings. You can create these embeddings through integrated or manual vectorization. To ensure accurate results, use the same embedding model for indexing and querying.
+
+## Tips for embedding model integration
+
++ **Identify use cases**. Evaluate specific use cases where embedding model integration for vector search features adds value to your search solution. Examples include [multimodal search](multimodal-search-overview.md) or matching image content with text content, multilingual search, and similarity search.
+
++ **Design a chunking strategy**. Embedding models have limits on the number of tokens they accept, so [data chunking](vector-search-how-to-chunk-documents.md) is necessary for large files.
+
++ **Optimize cost and performance**. Vector search is resource intensive and subject to maximum limits, so vectorize only the fields that contain semantic meaning. [Reduce vector size](vector-search-how-to-configure-compression-storage.md) to store more vectors for the same price.
+
++ **Choose the right embedding model**. Select a model for your use case, such as word embeddings for text-based searches or image embeddings for visual searches. Consider pretrained models, such as text-embedding-ada-002 from OpenAI or the Image Retrieval REST API from [Azure AI Vision](/azure/ai-services/computer-vision/how-to/image-retrieval).
+
++ **Normalize vector lengths**. To improve the accuracy and performance of similarity search, normalize vector lengths before you store them in a search index. Most pretrained models are already normalized.
+
++ **Fine-tune the model**. If needed, fine-tune the model on your domain-specific data to improve its performance and relevance to your search application.
+
++ **Test and iterate**. Continuously test and refine the embedding model integration to achieve your desired search performance and user satisfaction.
 
 ## Create resources in the same region
 
 Although integrated vectorization with Azure OpenAI embedding models doesn't require resources to be in the same region, using the same region can improve performance and reduce latency.
 
-1. [Check regions for a text embedding model](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+To use the same region for your resources:
+
+1. Check the [regional availability of text embedding models](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+
+1. Check the [regional availability of Azure AI Search](search-region-support.md).
 
-1. [Find the same region for Azure AI Search](search-region-support.md). 
+1. Create an Azure OpenAI resource and Azure AI Search service in the same region.
+
+> [!TIP]
+> Want to use [semantic ranking](semantic-how-to-query-request.md) for [hybrid queries](hybrid-search-overview.md) or a machine learning model in a [custom skill](cognitive-search-custom-skill-interface.md) for [AI enrichment](cognitive-search-concept-intro.md)? Choose an Azure AI Search region that provides those features.
+
+## Choose an embedding model in Azure AI Foundry
+
+When you add knowledge to an agent workflow in the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs), you have the option of creating a search index. A wizard guides you through the steps.
+
+One step involves selecting an embedding model to vectorize your plain text content. The following models are supported:
+
++ text-embedding-3-small
++ text-embedding-3-large
++ text-embedding-ada-002
++ Cohere-embed-v3-english
++ Cohere-embed-v3-multilingual
 
-1. To support hybrid queries that include [semantic ranking](semantic-how-to-query-request.md), or if you want to try machine learning model integration using a [custom skill](cognitive-search-custom-skill-interface.md) in an [AI enrichment pipeline](cognitive-search-concept-intro.md), select an Azure AI Search region that provides those features.
+Your model must already be deployed, and you must have permission to access it. For more information, see [Deployment overview for Azure AI Foundry Models](/azure/ai-foundry/concepts/deployments-overview).
 
 ## Generate an embedding for an improvised query
 
-The following Python code generates an embedding that you can paste into the "values" property of a vector query.
+If you don't want to use integrated vectorization, you can manually generate an embedding and paste it into the `vectorQueries.vector` property of a vector query. For more information, see [Create a vector query in Azure AI Search](vector-search-how-to-query.md).
+
+The following examples assume the text-embedding-ada-002 model. Replace `YOUR-API-KEY` and `YOUR-OPENAI-RESOURCE` with your Azure OpenAI resource details.
+
+### [.NET](#tab/dotnet)
+
+```csharp
+using System;
+using System.Net.Http;
+using System.Text;
+using System.Threading.Tasks;
+using Newtonsoft.Json;
+
+class Program
+{
+    static async Task Main(string[] args)
+    {
+        var apiKey = "YOUR-API-KEY";
+        var apiBase = "https://YOUR-OPENAI-RESOURCE.openai.azure.com";
+        var apiVersion = "2024-02-01";
+        var engine = "text-embedding-ada-002";
+
+        var client = new HttpClient();
+        client.DefaultRequestHeaders.Add("Authorization", $"Bearer {apiKey}");
+
+        var requestBody = new
+        {
+            input = "How do I use C# in VS Code?"
+        };
+
+        var response = await client.PostAsync(
+            $"{apiBase}/openai/deployments/{engine}/embeddings?api-version={apiVersion}",
+            new StringContent(JsonConvert.SerializeObject(requestBody), Encoding.UTF8, "application/json")
+        );
+
+        var responseBody = await response.Content.ReadAsStringAsync();
+        Console.WriteLine(responseBody);
+    }
+}
+```
+
+### [Java](#tab/java)
+
+```java
+import java.net.HttpURLConnection;
+import java.net.URL;
+import java.io.OutputStream;
+import java.io.BufferedReader;
+import java.io.InputStreamReader;
+
+public class Main {
+    public static void main(String[] args) {
+        String apiKey = "YOUR-API-KEY";
+        String apiBase = "https://YOUR-OPENAI-RESOURCE.openai.azure.com";
+        String engine = "text-embedding-ada-002";
+        String apiVersion = "2024-02-01";
+
+        try {
+            URL url = new URL(String.format("%s/openai/deployments/%s/embeddings?api-version=%s", apiBase, engine, apiVersion));
+            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
+            connection.setRequestMethod("POST");
+            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
+            connection.setRequestProperty("Content-Type", "application/json");
+            connection.setDoOutput(true);
+
+            String requestBody = "{\"input\": \"How do I use Java in VS Code?\"}";
+
+            try (OutputStream os = connection.getOutputStream()) {
+                os.write(requestBody.getBytes());
+            }
+
+            try (BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
+                StringBuilder response = new StringBuilder();
+                String line;
+                while ((line = br.readLine()) != null) {
+                    response.append(line);
+                }
+                System.out.println(response);
+            }
+        } catch (Exception e) {
+            e.printStackTrace();
+        }
+    }
+}
+```
+
+### [JavaScript](#tab/javascript)
+
+```javascript
+const apiKey = "YOUR-API-KEY";
+const apiBase = "https://YOUR-OPENAI-RESOURCE.openai.azure.com";
+const engine = "text-embedding-ada-002";
+const apiVersion = "2024-02-01";
+
+async function generateEmbedding() {
+  const response = await fetch(
+    `${apiBase}/openai/deployments/${engine}/embeddings?api-version=${apiVersion}`,
+    {
+      method: "POST",
+      headers: {
+        "Authorization": `Bearer ${apiKey}`,
+        "Content-Type": "application/json",
+      },
+      body: JSON.stringify({
+        input: "How do I use JavaScript in VS Code?",
+      }),
+    }
+  );
+
+  const data = await response.json();
+  console.log(data.data[0].embedding);
+}
+
+generateEmbedding();
+```
+
+### [Python](#tab/python)
 
 ```python
 !pip install openai
@@ -60,39 +218,25 @@ embeddings = response['data'][0]['embedding']
 print(embeddings)
 ```
 
-Output is a vector array of 1,536 dimensions.
+### [REST API](#tab/rest-api)
 
-## Choose an embedding model in Azure AI Foundry
-
-In the Azure AI Foundry portal, you have the option of creating a search index when you add knowledge to your agent workflow. A wizard guides you through the steps. When asked to provide an embedding model that vectorizes your plain text content, you can use one of the following supported models:
-
-+ text-embedding-3-large
-+ text-embedding-3-small
-+ text-embedding-ada-002
-+ Cohere-embed-v3-english
-+ Cohere-embed-v3-multilingual
-
-Your model must already be deployed and you must have permission to access it. For more information, see [Deploy AI models in Azure AI Foundry portal](/azure/ai-foundry/concepts/deployments-overview).
-
-## Tips and recommendations for embedding model integration
-
-+ **Identify use cases**: Evaluate the specific use cases where embedding model integration for vector search features can add value to your search solution. This can include multimodal or matching image content with text content, multilingual search, or similarity search.
-
-+ **Design a chunking strategy**: Embedding models have limits on the number of tokens they can accept, which introduces a data chunking requirement for large files. For more information, see [Chunk large documents for vector search solutions](vector-search-how-to-chunk-documents.md).
-
-+ **Optimize cost and performance**: Vector search can be resource-intensive and is subject to maximum limits, so consider only vectorizing the fields that contain semantic meaning. [Reduce vector size](vector-search-how-to-configure-compression-storage.md) so that you can store more vectors for the same price.
-
-+ **Choose the right embedding model:** Select an appropriate model for your specific use case, such as word embeddings for text-based searches or image embeddings for visual searches. Consider using pretrained models like **text-embedding-ada-002** from OpenAI or **Image Retrieval** REST API from [Azure AI Computer Vision](/azure/ai-services/computer-vision/how-to/image-retrieval).
-
-+ **Normalize Vector lengths**: Ensure that the vector lengths are normalized before storing them in the search index to improve the accuracy and performance of similarity search. Most pretrained models already are normalized but not all. 
+```http
+POST https://YOUR-OPENAI-RESOURCE.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2024-02-01
+  Authorization: Bearer YOUR-API-KEY
+  Content-Type: application/json
+    
+  {
+    "input": "How do I use REST APIs in VS Code?"
+  }
+```
 
-+ **Fine-tune the model**: If needed, fine-tune the selected model on your domain-specific data to improve its performance and relevance to your search application.
+---
 
-+ **Test and iterate**: Continuously test and refine your embedding model integration to achieve the desired search performance and user satisfaction.
+The output is a vector array of 1,536 dimensions.
 
-## Next steps
+## Related content
 
-+ [Understanding embeddings in Azure OpenAI in Azure AI Foundry Models](/azure/ai-services/openai/concepts/understand-embeddings)
-+ [Learn how to generate embeddings](/azure/ai-services/openai/how-to/embeddings?tabs=console)
++ [Understand embeddings in Azure OpenAI in Azure AI Foundry Models](/azure/ai-services/openai/concepts/understand-embeddings)
++ [Generate embeddings with Azure OpenAI](/azure/ai-services/openai/how-to/embeddings?tabs=console)
 + [Tutorial: Explore Azure OpenAI embeddings and document search](/azure/ai-services/openai/tutorials/embeddings?tabs=command-line)
 + [Tutorial: Choose a model (RAG solutions in Azure AI Search)](tutorial-rag-build-solution-models.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Comprehensive Update to Vector Search and Embedding Generation Document"
}
```

### Explanation
この変更は、Azure AI Searchにおけるベクトル検索と埋め込み生成に関するドキュメントの大幅な更新を示しています。主要な修正ポイントには、タイトルの形式変更、日付の更新、情報の追加、及び表形式での要約が含まれています。特に、埋め込みの生成方法についての説明が強化されており、ユーザーにとって明確で実用的な情報が提供されています。

新たに導入されたアプローチに関するセクションでは、埋め込みモデルを使用した「統合ベクトル化」と「手動ベクトル化」の2つのアプローチが詳述されています。また、様々な埋め込みモデルの選択肢、効果的なデータチャンク戦略、コスト最適化、正確性向上のためのベクトルの正規化、モデルの微調整などの推奨事項が追加されています。

この変更は、ドキュメントの質を向上させ、ユーザーがベクトル検索を成功させるために必要な情報を得られるようにするための重要なステップとなります。出力結果のフォーマットも整えられ、ユーザーが使用する際の利便性はさらに高まっています。全体として、情報が豊富で実用的なリソースに仕上げられています。


