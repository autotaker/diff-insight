---
date: '2024-12-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2c6389f...MicrosoftDocs:04e3114
summary: このドキュメントの更新では、Azure Machine LearningやAzure AI Foundryモデルカタログに関する新機能が追加され、ユーザーの利便性が向上しました。具体的には、モデルカタログの詳細説明やCORS設定に関する新しい画像ファイルの追加、テキスト分割スキルのパラメーター説明の更新が行われました。大きな互換性の問題はありませんが、モデルリストの整理が実施されています。さらに、コンテンツの見直しが行われ、説明が明確化されました。この更新により、ユーザーはAMLスキルを使ったモデルのデプロイやテキストデータ管理が円滑に行えるようになり、開発者にとっても作業が視覚的に理解しやすくなっています。総じて、ユーザビリティが向上し、ビジネスの成果を高めるためのリソースが使いやすくなっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2c6389f...MicrosoftDocs:04e3114){target="_blank"}

# Highlights

このドキュメント更新では、Azure Machine LearningやAzure AI Foundryモデルカタログの新しい機能や利用方法についての説明が追加され、関連する構成要素との連携が強化されました。また、画像や文章の更新により、ユーザーの利便性を向上させることが目指されています。

## New features
- Azure AI Foundryモデルカタログの活用に関する詳細な説明を追加。
- CORS設定を有効にする新しい画像ファイルの追加。
- テキスト分割スキルの新しいパラメーター説明を追加。

## Breaking changes
- 特に大きな互換性の問題になる変更は見られていませんが、モデルリストの整理が行われています（例：OpenAI-CLIP関連のモデルの削除）。

## Other updates
- 様々な画像ファイルや日付の微調整が行われ、内容が最新情報を反映。
- 文書中の説明がより明確にされ、必要な手順や関連機能についての情報が整理されました。

# Insights

Azure AIプラットフォームの文書が包括的に更新され、ユーザーが最新の機能に対応しやすくなっています。特に、Azure Machine Learning（AML）やAzure AI Foundryモデルカタログの統合に関するガイドラインが充実し、システム間の相互運用性やエコシステム内での使い勝手が向上しています。ユーザーはこれにより、AMLスキルを用いたカスタムモデルのデプロイメントやテキストデータのトークン化に関連する作業が円滑に行えるようになります。

また、Azureポータルでのアプリケーション開発やCORS設定の有効化に関する視覚的なコンテンツの強化も行われており、これらのアップデートは開発者にとって、手順がより視覚的かつ直感的に理解できるようデザインされています。特に、CORS設定画像の追加やインポートウィザードの利用提案は、ネットワーク管理者や開発者が直面する典型的な課題に対する指針を提供します。

埋め込みモデルについては、Azure AI Foundryからのモデルを利用した多様な選択肢が具体的に示され、ユーザーが自身のニーズに合わせた最適なモデルを容易に選択できるよう設計されています。これにより、新しいAIモデル開発や実装速度が向上し、業務プロセスの最適化が期待されます。

総じて、この文書更新はユーザビリティと機能理解の向上を重視したものであり、特にAzure AIプラットフォーム上でのビジネス成果を高めるために必要なリソースを利用しやすくなっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-aml-skill.md](#item-51366c) | minor update | AMLスキルに関するガイドの更新 | modified | 35 | 28 | 63 | 
| [cognitive-search-skill-textsplit.md](#item-9bf753) | minor update | テキスト分割認知スキルのドキュメントの更新 | modified | 2 | 2 | 4 | 
| [configure-results.png](#item-33a179) | minor update | 検索アプリケーションポータルの結果設定画像の更新 | modified | 0 | 0 | 0 | 
| [start-app-enable-cors.png](#item-77bbbb) | new feature | CORSを有効にするためのアプリ起動画像の追加 | added | 0 | 0 | 0 | 
| [suggestions.png](#item-b20dca) | minor update | 提案に関する画像の更新 | modified | 0 | 0 | 0 | 
| [ai-studio-catalog-embeddings-filter.png](#item-db0775) | minor update | AIスタジオのカタログ埋め込みフィルターに関する画像の更新 | modified | 0 | 0 | 0 | 
| [ai-studio-deploy-endpoint.png](#item-abf514) | minor update | AIスタジオのデプロイエンドポイントに関する画像の更新 | modified | 0 | 0 | 0 | 
| [ai-studio-fields-to-copy.png](#item-88ecf6) | minor update | AIスタジオのコピーするフィールドに関する画像の更新 | modified | 0 | 0 | 0 | 
| [search-create-app-portal.md](#item-19ab44) | minor update | Azureポータルでのデモアプリ作成に関するドキュメントの更新 | modified | 11 | 7 | 18 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | Azureポータルのベクターインポートに関するドキュメントの改善 | modified | 9 | 7 | 16 | 
| [tutorial-rag-build-solution-models.md](#item-6796c9) | minor update | RAGソリューションモデルビルドに関するチュートリアルの更新 | modified | 2 | 2 | 4 | 
| [vector-search-integrated-vectorization-ai-studio.md](#item-353fcc) | minor update | 統合ベクトル化のためのAzure AI Foundryの埋め込みモデルを利用する方法の更新 | modified | 46 | 24 | 70 | 
| [vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md](#item-ebe7a3) | minor update | Azure AI Foundryモデルカタログベクトライザーに関するドキュメントの更新 | modified | 10 | 12 | 22 | 


# Modified Contents
## articles/search/cognitive-search-aml-skill.md{#item-51366c}

<details>
<summary>Diff</summary>
````diff
@@ -18,27 +18,34 @@ ms.date: 08/05/2024
 > [!IMPORTANT]
 > Support for indexer connections to the Azure AI Foundry model catalog is in public preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). Preview REST APIs support this skill.
 
-The **AML** skill allows you to extend AI enrichment with a custom [Azure Machine Learning (AML)](../machine-learning/overview-what-is-azure-machine-learning.md) model. Once an AML model is [trained and deployed](../machine-learning/concept-azure-machine-learning-architecture.md#workspace), an **AML** skill integrates it into AI enrichment.
+The **AML** skill allows you to extend AI enrichment with a custom [Azure Machine Learning (AML)](../machine-learning/overview-what-is-azure-machine-learning.md) model or deployed base embedding model on Azure AI Foundry. Once an AML model is [trained and deployed](../machine-learning/concept-azure-machine-learning-architecture.md#workspace), an **AML** skill integrates it into a skillset.
 
-Like other built-in skills, an **AML** skill has inputs and outputs. The inputs are sent to your deployed AML online endpoint as a JSON object, which outputs a JSON payload as a response along with a success status code. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed. The response is expected to have the outputs specified by your **AML** skill. Any other response is considered an error and no enrichments are performed.
+## AML skill usage
 
-The **AML** skill can be called with the 2024-07-01 stable API version or the 2024-05-01-preview API version for connections to the model catalog in Azure AI Foundry portal.
-
-Starting in 2024-05-01-preview REST API and in the Azure portal (which also targets the 2024-05-01-preview), Azure AI Search introduced the [Azure AI Foundry model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) for query time connections to the model catalog in Azure AI Foundry portal. If you want to use that vectorizer for queries, the **AML** skill is the *indexing counterpart* for generating embeddings using a model in the Azure AI Foundry model catalog. 
-
-During indexing, the **AML** skill can connect to the model catalog to generate vectors for the index. At query time, queries can use a vectorizer to connect to the same model to vectorize text strings for a vector query. In this workflow, the **AML** skill and the model catalog vectorizer should be used together so that you're using the same embedding model for both indexing and queries. See [How to implement integrated vectorization using models from Azure AI Foundry](vector-search-integrated-vectorization-ai-studio.md) for details on this workflow.
+Like other built-in skills, a custom **AML** skill has inputs and outputs. The inputs are sent to a deployed AML online endpoint as a JSON object. The output of the endpoint must be a JSON payload in the response, along with a success status code. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed. The response is expected to provide the outputs specified by your **AML** skill definition. Any other response is considered an error and no enrichments are performed.
 
 > [!NOTE]
 > The indexer will retry twice for certain standard HTTP status codes returned from the AML online endpoint. These HTTP status codes are:
 > * `503 Service Unavailable`
 > * `429 Too Many Requests`
 
+The **AML** skill can be called with the 2024-07-01 stable API version or equivalent Azure SDK, or the 2024-05-01-preview API version for connections to the model catalog in Azure AI Foundry portal.
+
+## AML skill for models in Azure AI Foundry
+
+Starting in 2024-05-01-preview REST API and in the Azure portal (which also targets the 2024-05-01-preview), Azure AI Search provides the [Azure AI Foundry model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) for query time connections to the model catalog in Azure AI Foundry portal. If you want to use that vectorizer for queries, an **AML** skill is the *indexing counterpart* for generating embeddings using a model in the Azure AI Foundry model catalog. 
+
+During indexing, the **AML** skill can connect to the model catalog to generate vectors for the index. At query time, queries can use a vectorizer to connect to the same model to vectorize text strings for a vector query. In this workflow, the **AML** skill and the model catalog vectorizer should be used together so that you're using the same embedding model for both indexing and queries. See [Use embedding models from Azure AI Foundry model catalog](vector-search-integrated-vectorization-ai-studio.md) for details and for a list of the [supported embedding models](vector-search-integrated-vectorization-ai-studio.md#supported-embedding-models).
+
+We recommend using the [**Import and vectorize data**](search-get-started-portal-import-vectors.md) wizard to generate a skillset that includes an AML skill for deployed embedding models on Azure AI Foundry. AML skill definition for inputs, outputs, and mappings are generated by the wizard, which gives you an easy way to test a model before writing any code.
+
 ## Prerequisites
 
-* An [AML workspace](../machine-learning/concept-workspace.md)
-* An [Online endpoints (real-time)](../machine-learning/concept-endpoints-online.md) in this workspace.
+* An [AML workspace](../machine-learning/concept-workspace.md) for a custom model that you create, or a project in Azure AI Foundry if an embedding model is deployed from the catalog.
+* An [Online endpoints (real-time)](../machine-learning/concept-endpoints-online.md) in this workspace for a custom model, or the model endpoint for embedding models deployed from the catalog.
+
+## @odata.type
 
-## @odata.type  
 Microsoft.Skills.Custom.AmlSkill
 
 ## Skill parameters
@@ -47,40 +54,38 @@ Parameters are case-sensitive. Which parameters you choose to use depends on wha
 
 | Parameter name | Description |
 |--------------------|-------------|
-| `uri` | (Required for [key authentication](#WhatSkillParametersToUse)) The [scoring URI of the AML online endpoint](../machine-learning/how-to-authenticate-online-endpoint.md) to which the _JSON_ payload is sent. Only the **https** URI scheme is allowed. |
-| `key` | (Required for [key authentication](#WhatSkillParametersToUse)) The [key for the AML online endpoint](../machine-learning/how-to-authenticate-online-endpoint.md). |
-| `resourceId` | (Required for [token authentication](#WhatSkillParametersToUse)). The Azure Resource Manager resource ID of the AML online endpoint. It should be in the format subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.MachineLearningServices/workspaces/{workspace-name}/onlineendpoints/{endpoint_name}. |
+| `uri` | (Required for [key authentication](#WhatSkillParametersToUse)) The [scoring URI of the AML online endpoint](../machine-learning/how-to-authenticate-online-endpoint.md) to which the _JSON_ payload is sent. Only the **https** URI scheme is allowed. For embedding models in the Azure AI Foundry model catalog, this is the target URI.|
+| `key` | (Required for [key authentication](#WhatSkillParametersToUse)) The [key for the AML online endpoint](../machine-learning/how-to-authenticate-online-endpoint.md) or the  |
+| `resourceId` | (Required for [token authentication](#WhatSkillParametersToUse)). The Azure Resource Manager resource ID of the AML online endpoint. It should be in the format `subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.MachineLearningServices/workspaces/{workspace-name}/onlineendpoints/{endpoint_name}`. |
 | `region` | (Optional for [token authentication](#WhatSkillParametersToUse)). The [region](https://azure.microsoft.com/global-infrastructure/regions/) the AML online endpoint is deployed in. |
 | `timeout` | (Optional) When specified, indicates the timeout for the http client making the API call. It must be formatted as an XSD "dayTimeDuration" value (a restricted subset of an [ISO 8601 duration](https://www.w3.org/TR/xmlschema11-2/#dayTimeDuration) value). For example, `PT60S` for 60 seconds. If not set, a default value of 30 seconds is chosen. The timeout can be set to a maximum of 230 seconds and a minimum of 1 second. |
 | `degreeOfParallelism` | (Optional) When specified, indicates the number of calls the indexer makes in parallel to the endpoint you have provided. You can decrease this value if your endpoint is failing under too high of a request load. You can raise it if your endpoint is able to accept more requests and you would like an increase in the performance of the indexer.  If not set, a default value of 5 is used. The degreeOfParallelism can be set to a maximum of 10 and a minimum of 1.
 
 <a name="WhatSkillParametersToUse"></a>
 
-## What skill parameters to use
+## Authentication
+
+AML online endpoints provide two authentication options:
 
-Which AML skill parameters are required depends on what authentication your AML online endpoint uses, if any. AML online endpoints provide two authentication options:
+* [Key-based authentication](../machine-learning/how-to-authenticate-online-endpoint.md). A static key is provided to authenticate scoring requests from AML skills. Set the `uri` and `key` parameters for this connection.
 
-* [Key-Based Authentication](../machine-learning/how-to-authenticate-online-endpoint.md). A static key is provided to authenticate scoring requests from AML skills
-  * Use the _uri_ and _key_ parameters
-* [Token-Based Authentication](../machine-learning/how-to-authenticate-online-endpoint.md). The AML online endpoint is [deployed using token based authentication](../machine-learning/how-to-authenticate-online-endpoint.md). The Azure AI Search service's [managed identity](/azure/active-directory/managed-identities-azure-resources/overview) must be enabled. The AML skill then uses the service's managed identity to authenticate against the AML online endpoint, with no static keys required. The identity must be assigned owner or contributor role.
-  * Use the _resourceId_ parameter.
-  * If the search service is in a different region from the AML workspace, use the _region_ parameter to set the region the AML online endpoint was deployed in
+* [Token-Based Authentication](../machine-learning/how-to-authenticate-online-endpoint.md), where the AML online endpoint is [deployed using token based authentication](../machine-learning/how-to-authenticate-online-endpoint.md). The Azure AI Search service's [managed identity](/azure/active-directory/managed-identities-azure-resources/overview) must be enabled and have a role assignment on workspace. The AML skill then uses the service's managed identity to authenticate against the AML online endpoint, with no static keys required. The search service identity must be an **Owner** or **Contributor**. Set the `resourceId` parameter, and if the search service is in a different region from the AML workspace, set the `region` parameter.
 
 ## Skill inputs
 
-There are no "predefined" inputs for this skill. You can choose one or more fields that would be already available at the time of this skill's execution as inputs and the _JSON_ payload sent to the AML online endpoint will have different fields.
+Skill inputs are a node of the [enriched document](cognitive-search-working-with-skillsets.md#enrichment-tree) that's created during *document cracking*. For example, it might be the root document, a normalized image, or the content of a blob. There are no predefined inputs for this skill. For inputs, you should specify one or more nodes that are populated at the time of the AML skill's execution.
 
 ## Skill outputs
 
-There are no "predefined" outputs for this skill. Depending on the response your AML online endpoint returns, add output fields so that they can be picked up from the _JSON_ response.
+Skill outputs are new nodes of an enriched document created by the skill. There are no predefined outputs for this skill. For outputs, you should provide nodes that can be populated from the JSON response of your AML skill.
 
 ## Sample definition
 
 ```json
   {
     "@odata.type": "#Microsoft.Skills.Custom.AmlSkill",
-    "description": "A sample model that detects the language of sentence",
-    "uri": "https://contoso.count-things.com/score",
+    "description": "A custom model that detects the language in a document.",
+    "uri": "https://language-model.models.contoso.com/score",
     "context": "/document",
     "inputs": [
       {
@@ -122,7 +127,7 @@ The output corresponds to the response returned from your AML online endpoint. T
   {
     "@odata.type": "#Microsoft.Skills.Custom.AmlSkill",
     "description": "A sample model that detects the language of sentence",
-    "uri": "https://contoso.count-things.com/score",
+    "uri": "https://language-model.models.contoso.com/score",
     "context": "/document",
     "inputs": [
       {
@@ -161,12 +166,14 @@ The output corresponds to the response returned from your AML online endpoint. T
 ```
 
 ## Error cases
+
 In addition to your AML being unavailable or sending out nonsuccessful status codes, the following are considered erroneous cases:
 
-* If the AML online endpoint returns a success status code but the response indicates that it isn't `application/json`, then the response is considered invalid and no enrichments are performed.
-* If the AML online endpoint returns invalid json
+* The AML online endpoint returns a success status code, but the response indicates that it isn't `application/json`, then the response is considered invalid and no enrichments are performed.
+
+* The AML online endpoint returns invalid JSON.
 
-For cases when the AML online endpoint is unavailable or returns an HTTP error, a friendly error with any available details about the HTTP error will be added to the indexer execution history.
+For cases when the AML online endpoint is unavailable or returns an HTTP error, a friendly error with any available details about the HTTP error is added to the indexer execution history.
 
 ## See also
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AMLスキルに関するガイドの更新"
}
```

### Explanation
この変更は、Azure Machine Learning (AML) スキルに関する文書の内容を更新したものです。主に、AMLスキルの機能や利用方法、APIバージョンの情報を追加し、関連する構成要素との連携を強化しています。具体的には、AMLスキルがカスタムモデルやデプロイされたベースエンベディングモデルと連携できることを強調し、Azure AI Foundryモデルカタログとの接続方法に関する詳細な説明を加えました。

変更点には、スキルの入力と出力の定義、必要な前提条件、およびモデルカタログとの組み合わせ使用に関する情報の明確化が含まれています。また、エラーハンドリングの改善と、スキルを使用したデータインポートのためのウィザードの利用を推奨する旨が加えられています。このように、文書は特定の使用例や推奨事項を提供することで、ユーザーがAMLスキルを効果的に活用できるようにしています。

## articles/search/cognitive-search-skill-textsplit.md{#item-9bf753}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: reference
-ms.date: 10/29/2024
+ms.date: 12/03/2024
 ---
 
 # Text split cognitive skill
@@ -40,7 +40,7 @@ Parameters are case-sensitive.
 | `pageOverlapLength` | [2024-07-01](/rest/api/searchservice/skillsets/create-or-update) | Only applies if `textSplitMode` is set to `pages`. Each page starts with this number of characters or tokens from the end of the previous page. If this parameter is set to 0, there's no overlapping text on successive pages. This [example](#example-for-chunking-and-vectorization) includes the parameter. |
 | `maximumPagesToTake` | [2024-07-01](/rest/api/searchservice/skillsets/create-or-update) | Only applies if `textSplitMode` is set to `pages`. Number of pages to return. The default is 0, which means to return all pages. You should set this value if only a subset of pages are needed. This [example](#example-for-chunking-and-vectorization) includes the parameter.|
 | `unit` | [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | **New**. Only applies if `textSplitMode` is set to `pages`. Specifies whether to chunk by `characters` (default) or `azureOpenAITokens`. Setting the unit affects `maximumPageLength` and `pageOverlapLength`. |
-| `azureOpenAITokenizerParameters` | [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | **New**. An object providing extra parameters for the `azureOpenAITokens` unit. <br><br>`encoderModelName` is a designated tokenizer used for converting text into tokens, essential for natural language processing (NLP) tasks. Different models use different tokenizers. Valid values include cl100k_base (default) used by GPT-35-Turbo and GPT-4. Other valid values are r50k_base, p50k_base, and p50k_edit. The skill implements the tiktoken library by way of [SharpToken](https://www.nuget.org/packages/SharpToken) and `Microsoft.ML.Tokenizers` but doesn't support every encoder. For example, there's currently no support for o200k_base encoding used by GPT-4o. <br><br>`allowedSpecialTokens` defines a collection of special tokens that are permitted within the tokenization process. Special tokens are  string that you want to treat uniquely, ensuring they aren't split during tokenization. For example ["[START"], "[END]"].|
+| `azureOpenAITokenizerParameters` | [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | **New**. An object providing extra parameters for the `azureOpenAITokens` unit. <br><br>`encoderModelName` is a designated tokenizer used for converting text into tokens, essential for natural language processing (NLP) tasks. Different models use different tokenizers. Valid values include cl100k_base (default) used by GPT-35-Turbo and GPT-4. Other valid values are r50k_base, p50k_base, and p50k_edit. The skill implements the tiktoken library by way of [SharpToken](https://www.nuget.org/packages/SharpToken) and `Microsoft.ML.Tokenizers` but doesn't support every encoder. For example, there's currently no support for o200k_base encoding used by GPT-4o. <br><br>`allowedSpecialTokens` defines a collection of special tokens that are permitted within the tokenization process. Special tokens are  string that you want to treat uniquely, ensuring they aren't split during tokenization. For example ["[START"], "[END]"]. For languages in which the tiktoken library is not performing the tokenization as expected, it's recommended to use text splitting instead.|
 
 ## Skill Inputs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト分割認知スキルのドキュメントの更新"
}
```

### Explanation
このコードの変更では、テキスト分割認知スキルに関するドキュメントが更新されました。主な変更点は2つで、一つ目は日付の更新で、新しい日付が2024年12月03日に変更されました。二つ目の大きな変更として、`azureOpenAITokenizerParameters`という新しいパラメーターに関する説明が明確化されました。このパラメーターは、`azureOpenAITokens`ユニット用の追加パラメーターを提供するもので、テキストをトークンに変換するためのトークナイザや、トークン化プロセスで許可される特殊トークンの定義など、自然言語処理（NLP）タスクに必要な詳細が含まれています。

更新後の内容は、ユーザーがテキスト分割スキルをより深く理解し、適切に利用できるように設計されています。また、これにより、Azure AI Searchサービスの機能向上にも寄与しています。

## articles/search/media/search-create-app-portal/configure-results.png{#item-33a179}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索アプリケーションポータルの結果設定画像の更新"
}
```

### Explanation
この変更は、検索アプリケーションポータルにおける結果設定の画像ファイル（`configure-results.png`）に関するもので、ファイル自体には変更はありませんが、画像の更新や整理が行われた可能性があります。具体的には、画像に関連するメタデータや、画像の表示によって文書の視覚的なインパクトを向上させるための微調整があったと考えられます。

この画像は、ユーザーがポータル内での結果設定の手順を理解しやすくするために使用されており、視覚的な説明が文書の内容を補強する重要な要素となっています。画像の適切な更新は、より良いユーザー体験を提供するために重要です。

## articles/search/media/search-create-app-portal/start-app-enable-cors.png{#item-77bbbb}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "CORSを有効にするためのアプリ起動画像の追加"
}
```

### Explanation
このコードの変更は、CORS（Cross-Origin Resource Sharing）を有効にするプロセスを示す新しい画像ファイル（`start-app-enable-cors.png`）の追加に関するものです。この画像は、ユーザーがアプリを起動する際にCORS設定を有効にする方法を視覚的に示すために用いられます。

新たに追加されたこの画像は、特に開発者やシステム管理者にとって有用で、CORSに関する設定を理解しやすくする役割を果たします。画像を通じて手順が明確に示されることで、ユーザーは設定を自信を持って行えるようになります。このようなビジュアルコンテンツの追加は、ドキュメントの全体的な有用性とユーザー体験の向上に貢献します。

## articles/search/media/search-create-app-portal/suggestions.png{#item-b20dca}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "提案に関する画像の更新"
}
```

### Explanation
この変更は、アプリケーションポータルにおける提案機能を示す画像ファイル（`suggestions.png`）の更新に関するものです。具体的な変更内容は示されていないものの、画像自体の品質向上、情報の整理、または視覚的な明確さを増すための改良が行われた可能性があります。

更新された画像は、ユーザーが提案を理解しやすくするためのビジュアルコンテンツとして重要です。この変更により、ユーザーは提案機能をより効果的に利用できるようになることが期待されます。また、視覚的な要素が改善されることで、ドキュメント全体のプロフェッショナルな印象も向上します。このようなマイナーアップデートは、文書の価値を高め、ユーザー体験を向上させることに寄与します。

## articles/search/media/vector-search-integrated-vectorization-ai-studio/ai-studio-catalog-embeddings-filter.png{#item-db0775}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIスタジオのカタログ埋め込みフィルターに関する画像の更新"
}
```

### Explanation
この変更は、AIスタジオのカタログにおける埋め込みフィルターを示す画像ファイル（`ai-studio-catalog-embeddings-filter.png`）の更新に関するものです。具体的な変更内容は記載されていないため、画像の視覚的な調整や質の向上があったと考えられます。

更新された画像は、AIスタジオ内でのユーザー体験をよりスムーズにするために役立つもので、埋め込みフィルターの使用方法を明確に理解させるための重要なビジュアルリソースです。このようなマイナーアップデートにより、ユーザーがフィルター機能をより効果的に活用できる可能性が高まります。また、視覚的な改善は、ドキュメント全体の信頼性とプロフェッショナリズムを向上させ、ユーザーにとって使いやすいリソースを提供することに寄与します。

## articles/search/media/vector-search-integrated-vectorization-ai-studio/ai-studio-deploy-endpoint.png{#item-abf514}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIスタジオのデプロイエンドポイントに関する画像の更新"
}
```

### Explanation
この変更は、AIスタジオのデプロイエンドポイントを示す画像ファイル（`ai-studio-deploy-endpoint.png`）の更新に関するものです。具体的な変更内容は記載されていませんが、画像の改善や情報の明確化が行われた可能性があります。

更新された画像は、ユーザーがAIスタジオにおけるデプロイメントプロセスを理解しやすくするための重要な要素です。デプロイエンドポイントに関するビジュアル情報が改善されることで、ユーザーはその機能をより効果的に活用できるようになります。このようなマイナーアップデートは、ドキュメントの視覚的な品質を向上させ、ユーザー体験に貢献することが期待されます。全体として、視覚的なリソースの強化は、ユーザーにとっての利便性を高め、より良いサービス提供を目指すために重要なステップです。

## articles/search/media/vector-search-integrated-vectorization-ai-studio/ai-studio-fields-to-copy.png{#item-88ecf6}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIスタジオのコピーするフィールドに関する画像の更新"
}
```

### Explanation
この変更は、AIスタジオにおけるコピーするフィールドを示す画像ファイル（`ai-studio-fields-to-copy.png`）の更新に関連しています。具体的な変更内容については記載がありませんが、画像の質や情報の明確性に関する改善があったと推測されます。

更新された画像は、ユーザーがAIスタジオでコピーするフィールドの機能を理解しやすくするために役立ちます。このような視覚的なリソースの改善は、ユーザー体験を向上させ、特に新規ユーザーが機能を利用しやすくなることを目的としています。マイナーなアップデートではありますが、視覚情報の強化はドキュメント全体の信頼性を高め、ユーザーにとって膨大な情報を整理する手助けをします。総じて、これまでのリソースの更新は、より良いユーザーサポートを実現するための重要な要素となります。

## articles/search/search-create-app-portal.md{#item-19ab44}

<details>
<summary>Diff</summary>
````diff
@@ -1,21 +1,21 @@
 ---
-title: "Quickstart: Create a demo app in Azure portal"
+title: "Quickstart: Create a demo search app in Azure portal"
 titleSuffix: Azure AI Search
 description: Run the Create demo app wizard to generate HTML pages and script for an operational web app. The page includes a search bar, results area, sidebar, and typeahead support.
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 01/17/2024
+ms.date: 12/04/2024
 ms.custom:
   - mode-ui
   - ignite-2023
 ---
 
-# Quickstart: Create a demo app in the Azure portal
+# Quickstart: Create a demo search app in the Azure portal
 
-In this Azure AI Search quickstart, you'll use the Azure portal's **Create demo app** wizard to generate a downloadable, "localhost"-style web app that runs in a browser. Depending on its configuration, the generated app is operational on first use, with a live read-only connection to an index on your search service. A default app can include a search bar, results area, sidebar filters, and typeahead support.
+In this quickstart for Azure AI Search, learn how to use the Azure portal's **Create demo app** wizard to generate a downloadable, "localhost"-style web app that runs in a browser. Depending on how you configure it, the generated app is operational on first use, with a live read-only connection to an index on your search service. A default app can include a search bar, results area, sidebar filters, and typeahead support.
 
 A demo app can help you visualize how an index will function in a client app, but it isn't intended for production scenarios. Production apps should include security, error handling, and hosting logic that the demo app doesn't provide. 
 
@@ -39,16 +39,18 @@ When the index is ready to use, move on to the next step.
 
 ## Start the wizard
 
-1. Sign in to the [Azure portal](https://portal.azure.com/) with your Azure account.
+1. Sign in to the [Azure portal](https://portal.azure.com/) with your Azure account and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
 
-1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) and on the Overview page, from the links on the middle of the page, select **Indexes**. 
+1. Under **Search Management** > **Indexes**
 
 1. Choose *realestate-us-sample-index* from the list of existing indexes.
 
 1. On the index page, at the top, select **Create demo app** to start the wizard.
 
 1. On the first wizard page, select **Enable Cross Origin Resource Sharing (CORS)** to add CORS support to your index definition. This step is optional, but your local web app won't connect to the remote index without it.
 
+:::image type="content" source="media/search-create-app-portal/start-app-enable-cors.png" alt-text="Screenshot of the enable CORS option for the real estate sample index.":::
+
 ## Configure search results
 
 The wizard provides a basic layout for rendered search results that includes space for a thumbnail image, a title, and description. Backing each of these elements is a field in your index that provides the data. 
@@ -57,7 +59,7 @@ The wizard provides a basic layout for rendered search results that includes spa
 
 1. In Title, choose a field that conveys the uniqueness of each document. In this sample, the listing ID is a reasonable selection.
 
-1. In Description, choose a field that provides details that might help someone decide whether to click through to that particular document.
+1. In Description, choose a field that provides details that might help someone decide whether to drill down to that particular document.
 
    :::image type="content" source="media/search-create-app-portal/configure-results.png" alt-text="configure results for sample data" border="false":::
 
@@ -88,6 +90,8 @@ The following screenshot shows options in the wizard, juxtaposed with a rendered
 
 Suggestions refer to automated query prompts that are attached to the search box. Azure AI Search supports two: *autocompletion* of a partially entered search term, and *suggestions* for a dropdown list of potential matching documents based.
 
+Select fields for which suggested queries are provided. You should choose shorter string fields. Avoid verbose fields such as descriptions.
+
 The wizard supports suggestions, and the fields that can provide suggested results are derived from a [`Suggesters`](index-add-suggesters.md) construct in the index:
 
 ```JSON
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureポータルでのデモアプリ作成に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azureポータルでデモアプリを作成する方法に関するドキュメント（`search-create-app-portal.md`）の更新を示しています。主な変更点としては、ドキュメント内のタイトルや説明文が改善され、ユーザーがAI Searchをより理解しやすくなるよう修正が加えられています。

具体的には、タイトルが「Quickstart: Create a demo app in Azure portal」から「Quickstart: Create a demo search app in Azure portal」に変更され、デモアプリの生成に関する説明がより明確になりました。また、日付が変更され、最新情報が反映されています。手順の一部も修正され、特に検索サービスの位置を示すリンクが追加されることで、ユーザーがより効率的に作業を進められるようになっています。

このドキュメントの更新は、Azure AI Searchにおける初期設定プロセスの可視化を助け、ユーザーが機能を迅速に利用できるようにするための重要なステップです。全体として、ユーザーが理解しやすいフローを提供し、実際の利用を促進することを目的としています。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -46,9 +46,9 @@ Use an embedding model on an Azure AI platform in the [same region as Azure AI S
 
 | Provider | Supported models |
 |---|---|
-| [Azure OpenAI Service](https://aka.ms/oai/access) | text-embedding-ada-002, text-embedding-3-large, or text-embedding-3-small. |
-| [Azure AI Foundry model catalog](/azure/ai-studio/what-is-ai-studio) |  Azure, Cohere, and Facebook embedding models. |
-| [Azure AI services multi-service account](/azure/ai-services/multi-service-resource) | [Azure AI Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) for image and text vectorization. Azure AI Vision multimodal is available in selected regions. [Check the documentation](/azure/ai-services/computer-vision/how-to/image-retrieval?tabs=csharp) for an updated list. Depending on how you [attach the multi-service resource](cognitive-search-attach-cognitive-services.md), the account might need to be in the same region as Azure AI Search. |
+| [Azure OpenAI Service](https://aka.ms/oai/access) | text-embedding-ada-002 <br>text-embedding-3-large <br>text-embedding-3-small |
+| [Azure AI Foundry model catalog](/azure/ai-studio/what-is-ai-studio) | For text: <br>Cohere-embed-v3-english <br>Cohere-embed-v3-multilingual <br>For images: <br>Facebook-DinoV2-Image-Embeddings-ViT-Base <br>Facebook-DinoV2-Image-Embeddings-ViT-Giant |
+| [Azure AI services multi-service account](/azure/ai-services/multi-service-resource) | [Azure AI Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) for image and text vectorization, [available in selected regions](/azure/ai-services/computer-vision/how-to/image-retrieval?tabs=csharp). Depending on how you [attach the multi-service resource](cognitive-search-attach-cognitive-services.md), the multi-service account might need to be in the same region as Azure AI Search. |
 
 If you use the Azure OpenAI Service, the endpoint must have an associated [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains). A custom subdomain is an endpoint that includes a unique name (for example, `https://hereismyuniquename.cognitiveservices.azure.com`). If the service was created through the Azure portal, this subdomain is automatically generated as part of your service setup. Ensure that your service includes a custom subdomain before using it with the Azure AI Search integration.
 
@@ -202,13 +202,15 @@ After you finish these steps, you should be able to select the Azure AI Vision v
 
 ### [Azure AI Foundry model catalog](#tab/model-catalog)
 
-The wizard supports Azure, Cohere, and Facebook embedding models in the Azure AI Foundry model catalog, but it doesn't currently support the OpenAI CLIP model. Internally, the wizard calls the [AML skill](cognitive-search-aml-skill.md) to connect to the catalog.
+The wizard supports Azure, Cohere, and Facebook embedding models in the Azure AI Foundry model catalog, but it doesn't currently support the OpenAI CLIP models. Internally, the wizard calls the [AML skill](cognitive-search-aml-skill.md) to connect to the catalog.
 
 1. For the model catalog, you should have an [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource), a [hub in Azure AI Foundry portal](/azure/ai-studio/how-to/create-projects), and a [project](/azure/ai-studio/how-to/create-projects). Hubs and projects having the same name can share connection information and permissions.
 
-1. Deploy a supported embedding model to the model catalog in your project.
+1. Deploy an embedding model to the model catalog in your project.
 
-1. For role-based connections, create two role assignments: one for Azure AI Search, and another for the AI Foundry project. Assign the [Cognitive Services OpenAI User](/azure/ai-services/openai/how-to/role-based-access-control) role for embeddings and vectorization.
+    1. Select **Models + Endpoints**, and then select **Deploy a model**. Choose **Deploy base model**.
+    1. Filter by inference task set to *Embeddings*.
+    1. Deploy one of the [supported embedding models](#supported-embedding-models).
 
 ---
 
@@ -321,7 +323,7 @@ Chunking is built in and nonconfigurable. The effective settings are:
 
    + For Azure OpenAI, choose an existing deployment of text-embedding-ada-002, text-embedding-3-large, or text-embedding-3-small.
 
-   + For AI Foundry catalog, choose an existing deployment of an Azure, Cohere, and Facebook embedding model.
+   + For AI Foundry catalog, choose an existing deployment of an Azure or Cohere embedding model.
 
    + For AI Vision multimodal embeddings, select the account.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureポータルのベクターインポートに関するドキュメントの改善"
}
```

### Explanation
この変更は、Azureポータルでベクターをインポートする方法に関するドキュメント（`search-get-started-portal-import-vectors.md`）の更新を示しています。主な変更点は、埋め込みモデルに関する情報の詳細化および整理です。

具体的には、埋め込みモデルの提供元と対応モデルについての記述が改良されました。たとえば、「Azure OpenAI Service」や「Azure AI Foundryモデルカタログ」で利用可能な具体的なモデル名を列挙することで、ユーザーが必要な情報を迅速に見つけやすくなっています。また、「Azure AIサービスのマルチサービスアカウント」セクションも改善され、地域に関する重要な情報が明確にされました。

さらに、モデルカタログに関連する手順が整理され、新しいステップが追加されました。これにより、ユーザーが埋め込みモデルを展開するプロセスがより直感的になり、特定の手順を簡素化する効果があります。

この更新は、Azure AI Searchを利用したベクターのインポートに関する体験を向上させるための重要なステップであり、ユーザーが新しい機能をより効果的に活用できるよう支援しています。全体として、この変更がユーザーにとっての利便性を向上させ、Azureプラットフォームでの作業を効率的にすることを目的としています。

## articles/search/tutorial-rag-build-solution-models.md{#item-6796c9}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: tutorial
 ms.custom: references_regions
-ms.date: 10/25/2024
+ms.date: 12/03/2024
 
 ---
 
@@ -66,7 +66,7 @@ Azure AI Search provides skill and vectorizer support for the following embeddin
 |--------|------------------|-------|------------|
 | Azure OpenAI | text-embedding-ada-002, <br>text-embedding-3-large, <br>text-embedding-3-small | [AzureOpenAIEmbedding](cognitive-search-skill-azure-openai-embedding.md) | [AzureOpenAIEmbedding](vector-search-vectorizer-azure-open-ai.md) |
 | Azure AI Vision | multimodal 4.0 <sup>1</sup> | [AzureAIVision](cognitive-search-skill-vision-vectorize.md) | [AzureAIVision](vector-search-vectorizer-ai-services-vision.md) |
-| Azure AI Foundry model catalog | OpenAI-CLIP-Image-Text-Embeddings-vit-base-patch32, <br>OpenAI-CLIP-Image-Text-Embeddings-ViT-Large-Patch14-336, <br>Facebook-DinoV2-Image-Embeddings-ViT-Base, <br>Facebook-DinoV2-Image-Embeddings-ViT-Giant, <br>Cohere-embed-v3-english, <br>Cohere-embed-v3-multilingual | [AML](cognitive-search-aml-skill.md) <sup>2</sup>  | [Azure AI Foundry model catalog](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) |
+| Azure AI Foundry model catalog | Facebook-DinoV2-Image-Embeddings-ViT-Base, <br>Facebook-DinoV2-Image-Embeddings-ViT-Giant, <br>Cohere-embed-v3-english, <br>Cohere-embed-v3-multilingual | [AML](cognitive-search-aml-skill.md) <sup>2</sup>  | [Azure AI Foundry model catalog](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) |
 
 <sup>1</sup> Supports image and text vectorization.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションモデルビルドに関するチュートリアルの更新"
}
```

### Explanation
この変更は、RAG（Retrieval-Augmented Generation）ソリューションモデルのビルドに関するチュートリアル（`tutorial-rag-build-solution-models.md`）の更新を示しています。主な変更点は、日付の更新と埋め込みモデルのリストの改訂です。

具体的には、最初のメタデータである日付が「2024年10月25日」から「2024年12月3日」に更新されています。この変更により、ドキュメントが最新の情報を反映していることが分かります。

また、埋め込みモデルのリストにおいて、「Azure AI Foundry model catalog」に記載されているモデルが整理され、OpenAI-CLIP関連のエントリが削除されています。これにより、サポートされているモデルに関する情報がより簡潔になり、ユーザーが必要なモデルを特定しやすくなっています。

全体として、これらの変更はユーザーにとっての利便性を高めることを目的としており、RAGソリューションモデルに対する理解を深める助けとなる情報を提供しています。

## articles/search/vector-search-integrated-vectorization-ai-studio.md{#item-353fcc}

<details>
<summary>Diff</summary>
````diff
@@ -8,39 +8,62 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 10/29/2024
+ms.date: 12/03/2024
 ---
 
-# How to implement integrated vectorization using models from Azure AI Foundry
+# Use embedding models from Azure AI Foundry model catalog for integrated vectorization
 
 > [!IMPORTANT] 
 > This feature is in public preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [2024-05-01-Preview REST API](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true) supports this feature.
 
 In this article, learn how to access the embedding models in the [Azure AI Foundry model catalog](/azure/ai-studio/how-to/model-catalog) for vector conversions during indexing and in queries in Azure AI Search.
 
-The workflow includes model deployment steps. The model catalog includes embedding models from Azure OpenAI, Cohere, Facebook, and OpenAI. Deploying a model is billable per the billing structure of each provider. 
+The workflow includes model deployment steps. The model catalog includes embedding models from Microsoft and other companies. Deploying a model is billable per the billing structure of each provider. 
 
 After the model is deployed, you can use it for [integrated vectorization](vector-search-integrated-vectorization.md) during indexing, or with the [AI Foundry vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) for queries.
 
+> [!TIP]
+> Use the [**Import and vectorize data**](search-get-started-portal-import-vectors.md) wizard to generate a skillset that includes an AML skill for deployed embedding models on Azure AI Foundry. AML skill definition for inputs, outputs, and mappings are generated by the wizard, which gives you an easy way to test a model before writing any code.
+
+## Prerequisites
+
++ Azure AI Search, any region and tier.
+
++ Azure AI Foundry and an [Azure AI Foundry project](/azure/ai-studio/how-to/create-projects).
+
+## Supported embedding models
+
+Integrated vectorization and the [Import and vectorize data wizard](search-import-data-portal.md) supports the following embedding models in the model catalog:
+
+For text embeddings:
+
++ Cohere-embed-v3-english
++ Cohere-embed-v3-multilingual
+
+For image embeddings:
+
++ Facebook-DinoV2-Image-Embeddings-ViT-Base
++ Facebook-DinoV2-Image-Embeddings-ViT-Giant
+
 ## Deploy an embedding model from the Azure AI Foundry model catalog
 
-1. Open the [Azure AI Foundry model catalog](https://ai.azure.com/explore/models). 
+1. Open the [Azure AI Foundry model catalog](https://ai.azure.com/explore/models). Create a project if you don't have one already.
 
 1. Apply a filter to show just the embedding models. Under **Inference tasks**, select **Embeddings**:
 
    :::image type="content" source="media\vector-search-integrated-vectorization-ai-studio\ai-studio-catalog-embeddings-filter.png" lightbox="media\vector-search-integrated-vectorization-ai-studio\ai-studio-catalog-embeddings-filter.png" alt-text="Screenshot of the Azure AI Foundry model catalog page highlighting how to filter by embeddings models.":::
 
-1. Select the model you would like to vectorize your content with. Then select **Deploy** and pick a deployment option.
+1. Select a supported model, then select **Deploy**.
 
    :::image type="content" source="media\vector-search-integrated-vectorization-ai-studio\ai-studio-deploy-endpoint.png" lightbox="media\vector-search-integrated-vectorization-ai-studio\ai-studio-deploy-endpoint.png" alt-text="Screenshot of deploying an endpoint via the Azure AI Foundry model catalog.":::
 
-1. Fill in the requested details. Select or [create a new AI project](/azure/ai-studio/how-to/create-projects), and then select **Deploy**. The deployment details vary depending on which model you select. 
+1. Accept the defaults or modify as needed, and then select **Deploy**. The deployment details vary depending on which model you select. 
 
 1. Wait for the model to finish deploying by monitoring the **Provisioning State**. It should change from "Provisioning" to "Updating" to "Succeeded". You might need to select **Refresh** every few minutes to see the status update.
 
-1. Copy the URL, Primary key, and Model ID fields and set them aside for later. You need these values for the vectorizer definition in a search index, and for the skillset that calls the model endpoints during indexing.
+1. Make a note of the target URI, key, and model name. You need these values for the vectorizer definition in a search index, and for the skillset that calls the model endpoints during indexing.
 
-    Optionally, you can change your endpoint to use **Token authentication** instead of **Key authentication**. If you enable token authentication, you only need to copy the URL and Model ID, and also make a note of which region the model is deployed to.
+    Optionally, you can change your endpoint to use **Token authentication** instead of **Key authentication**. If you enable token authentication, you only need to copy the URI and model name,  but make a note of which region the model is deployed to.
 
     :::image type="content" source="media\vector-search-integrated-vectorization-ai-studio\ai-studio-fields-to-copy.png" lightbox="media\vector-search-integrated-vectorization-ai-studio\ai-studio-fields-to-copy.png" alt-text="Screenshot of a deployed endpoint in AI Foundry portal highlighting the fields to copy and save for later.":::
 
@@ -56,12 +79,12 @@ When you deploy embedding models from the [Azure AI Foundry model catalog](https
 
 This section describes the AML skill definition and index mappings. It includes sample payloads that are already configured to work with their corresponding deployed endpoints. For more technical details on how these payloads work, read about the [Skill context and input annotation language](cognitive-search-skill-annotation-language.md).
 
-### [**Text Input for "Inference" API**](#tab/inference-text)
+<!-- ### [**Text Input for "Inference" API**](#tab/inference-text)
 
 This AML skill payload works with the following models from AI Foundry:
 
-+ OpenAI-CLIP-Image-Text-Embeddings-vit-base-patch32
-+ OpenAI-CLIP-Image-Text-Embeddings-ViT-Large-Patch14-336
++ Cohere-embed-v3-english
++ Cohere-embed-v3-multilingual
 
 It assumes that you're chunking your content using the [Text Split skill](cognitive-search-skill-textsplit.md) and that the text to be vectorized is in the `/document/pages/*` path. If your text comes from a different path, update all references to the `/document/pages/*` path accordingly.
 
@@ -99,14 +122,12 @@ The URI and key are generated when you deploy the model from the catalog. For mo
     }
   ]
 }
-```
+``` -->
 
-### [**Image Input for "Inference" API**](#tab/inference-image)
+### [**Facebook embedding models**](#tab/inference-image)
 
-This AML skill payload works with the following models from AI Foundry:
+This AML skill payload works with the following image embedding models from AI Foundry:
 
-+ OpenAI-CLIP-Image-Text-Embeddings-vit-base-patch32
-+ OpenAI-CLIP-Image-Text-Embeddings-ViT-Large-Patch14-336
 + Facebook-DinoV2-Image-Embeddings-ViT-Base
 + Facebook-DinoV2-Image-Embeddings-ViT-Giant
 
@@ -118,8 +139,9 @@ The URI and key are generated when you deploy the model from the catalog. For mo
 {
   "@odata.type": "#Microsoft.Skills.Custom.AmlSkill",
   "context": "/document/normalized_images/*",
-  "uri": "<YOUR_MODEL_URL_HERE>",
-  "key": "<YOUR_MODEL_HERE>",
+  "uri": "https://myproject-1a1a-abcd.eastus.inference.ml.azure.com/score",
+  "timeout": "PT1M",
+  "key": "bbbbbbbb-1c1c-2d2d-3e3e-444444444444",
   "inputs": [
     {
       "name": "input_data",
@@ -148,27 +170,27 @@ The URI and key are generated when you deploy the model from the catalog. For mo
 }
 ```
 
-### [**Cohere**](#tab/cohere)
+### [**Cohere embedding models**](#tab/cohere)
 
-This AML skill payload works with the following models from AI Foundry:
+This AML skill payload works with the following text embedding models from AI Foundry:
 
 + Cohere-embed-v3-english
 + Cohere-embed-v3-multilingual
 
-It assumes that you're chunking your content using the SplitSkill and therefore your text to be vectorized is in the `/document/pages/*` path. If your text comes from a different path, update all references to the `/document/pages/*` path according.
+It assumes that you're chunking your content using the Text Split skill and therefore your text to be vectorized is in the `/document/pages/*` path. If your text comes from a different path, update all references to the `/document/pages/*` path accordingly.
 
 You must add the `/v1/embed` path onto the end of the URL that you copied from your AI Foundry deployment. You might also change the values for the `input_type`, `truncate` and `embedding_types` inputs to better fit your use case. For more information on the available options, review the [Cohere Embed API reference](/azure/ai-studio/how-to/deploy-models-cohere-embed).
 
 The URI and key are generated when you deploy the model from the catalog. For more information about these values, see [How to deploy Cohere Embed models with Azure AI Foundry](/azure/ai-studio/how-to/deploy-models-cohere-embed).
 
-Note that image URIs are not supported by this integration at this time.
+Note that image URIs aren't supported by this integration at this time.
 
 ```json
 {
   "@odata.type": "#Microsoft.Skills.Custom.AmlSkill",
   "context": "/document/pages/*",
-  "uri": "<YOUR_MODEL_URL_HERE>/v1/embed",
-  "key": "<YOUR_MODEL_KEY_HERE>",
+  "uri": "https://cohere-embed-v3-multilingual-hin.eastus.models.ai.azure.com/v1/embed",
+  "key": "aaaaaaaa-0b0b-1c1c-2d2d-333333333333",
   "inputs": [
     {
       "name": "texts",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "統合ベクトル化のためのAzure AI Foundryの埋め込みモデルを利用する方法の更新"
}
```

### Explanation
この変更は、Azure AI Foundryからのモデルを使用した統合ベクトル化の実装方法に関するドキュメント（`vector-search-integrated-vectorization-ai-studio.md`）の更新を示しています。主な変更内容には、日付の更新、タイトルの修正、コンテンツの追加および一部の情報の削除が含まれています。

まず、メタデータの日付が「2024年10月29日」から「2024年12月3日」に変更されており、ドキュメントが最新の情報を反映しています。また、ドキュメントのタイトルが「Azure AI Foundryのモデルを使用した統合ベクトル化の実装方法」から「Azure AI Foundryモデルカタログの埋め込みモデルを使用して統合ベクトル化を行う方法」に変更され、内容がより明確になっています。

新たに導入された内容には、埋め込みモデルの使用に関する前提条件、サポートされる埋め込みモデルのリスト、そして「**データをインポートしてベクトル化**」ウィザードを使用することに関するアドバイスが含まれています。また、複数の埋め込みモデルのサポート（特にCohereやFacebookのモデル）についての記述が強化され、ユーザーが利用できる選択肢が明示されています。

一部の情報が更新されたことで、ユーザーがモデルをデプロイする際のプロセスが簡略化されており、必要なフィールドのメモ取りや、エンドポイントの認証方法についても詳しく説明されています。

全体として、これらの変更は文書の使い勝手を向上させ、ユーザーがAzure AI Foundryを利用して統合ベクトル化を行うための具体的な手順を理解しやすくすることを目的としています。

## articles/search/vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md{#item-ebe7a3}

<details>
<summary>Diff</summary>
````diff
@@ -8,12 +8,12 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: reference
-ms.date: 08/05/2024
+ms.date: 12/03/2024
 ---
 
 #	Azure AI Foundry model catalog vectorizer
 
-> [!IMPORTANT] 
+> [!IMPORTANT]
 > This vectorizer is in public preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [2024-05-01-Preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-05-01-Preview&preserve-view=true) supports this feature.
 
 The **Azure AI Foundry model catalog** vectorizer connects to an embedding model that was deployed via [the Azure AI Foundry model catalog](/azure/ai-studio/how-to/model-catalog) to an Azure Machine Learning endpoint. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed. 
@@ -27,7 +27,7 @@ Parameters are case-sensitive. Which parameters you choose to use depends on wha
 | Parameter name | Description |
 |--------------------|-------------|
 | `uri` | (Required) The [URI of the AML online endpoint](../machine-learning/how-to-authenticate-online-endpoint.md) to which the _JSON_ payload is sent. Only the **https** URI scheme is allowed. |
-| `modelName` | (Required) The model ID from the AI Foundry model catalog that is deployed at the provided endpoint. Currently supported values are <ul><li>OpenAI-CLIP-Image-Text-Embeddings-vit-base-patch32 </li><li>OpenAI-CLIP-Image-Text-Embeddings-ViT-Large-Patch14-336 </li><li>Facebook-DinoV2-Image-Embeddings-ViT-Base </li><li>Facebook-DinoV2-Image-Embeddings-ViT-Giant </li><li>Cohere-embed-v3-english </li><li>Cohere-embed-v3-multilingual</ul> |
+| `modelName` | (Required) The model ID from the AI Foundry model catalog that is deployed at the provided endpoint. Supported models are: <ul><li>Facebook-DinoV2-Image-Embeddings-ViT-Base </li><li>Facebook-DinoV2-Image-Embeddings-ViT-Giant </li><li>Cohere-embed-v3-english </li><li>Cohere-embed-v3-multilingual</ul> |
 | `key` | (Required for [key authentication](#WhatParametersToUse)) The [key for the AML online endpoint](../machine-learning/how-to-authenticate-online-endpoint.md). |
 | `resourceId` | (Required for [token authentication](#WhatParametersToUse)). The Azure Resource Manager resource ID of the AML online endpoint. It should be in the format subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.MachineLearningServices/workspaces/{workspace-name}/onlineendpoints/{endpoint_name}. |
 | `region` | (Optional for [token authentication](#WhatParametersToUse)). The [region](https://azure.microsoft.com/global-infrastructure/regions/) the AML online endpoint is deployed in. Needed if the region is different from the region of the search service. |
@@ -49,10 +49,8 @@ Which authentication parameters are required depends on what authentication your
 
 Which vector query types are supported by the AI Foundry model catalog vectorizer depends on the `modelName` that is configured.
 
-| `modelName` | Supports `text` query | Supports `imageUrl` query | Supports `imageBinary` query |
+| Embedding model | Supports `text` query | Supports `imageUrl` query | Supports `imageBinary` query |
 |--------------------|-------------|-------------|-------------|
-| OpenAI-CLIP-Image-Text-Embeddings-vit-base-patch32 | X | X | X |
-| OpenAI-CLIP-Image-Text-Embeddings-ViT-Large-Patch14-336 | X | X | X |
 | Facebook-DinoV2-Image-Embeddings-ViT-Base |  | X | X |
 | Facebook-DinoV2-Image-Embeddings-ViT-Giant |  | X | X |
 | Cohere-embed-v3-english | X |  |  |
@@ -64,25 +62,25 @@ The expected field dimensions for a field configured with an AI Foundry model ca
 
 | `modelName` | Expected dimensions |
 |--------------------|-------------|
-| OpenAI-CLIP-Image-Text-Embeddings-vit-base-patch32 | 512 |
-| OpenAI-CLIP-Image-Text-Embeddings-ViT-Large-Patch14-336 | 768 |
 | Facebook-DinoV2-Image-Embeddings-ViT-Base | 768 |
 | Facebook-DinoV2-Image-Embeddings-ViT-Giant | 1536 |
 | Cohere-embed-v3-english | 1024 |
 | Cohere-embed-v3-multilingual | 1024 |
 
 ## Sample definition
 
+Suggested model names in the Azure AI Foundry model catalog consist of the base model plus a random three-letter suffix. The name of your model will be different from the one shown in this example.
+
 ```json
 "vectorizers": [
     {
-        "name": "my-ai-studio-catalog-vectorizer",
+        "name": "my-model-catalog-vectorizer",
         "kind": "aml",
         "amlParameters": {
-            "uri": "https://my-aml-endpoint.eastus.inference.ml.azure.com/score",
-            "key": "0000000000000000000000000000000000000",
+            "uri": "https://Cohere-embed-v3-multilingual-hin.eastus.models.ai.azure.com",
+            "key": "aaaaaaaa-0b0b-1c1c-2d2d-333333333333",
             "timeout": "PT60S",
-            "modelName": "OpenAI-CLIP-Image-Text-Embeddings-vit-base-patch3",
+            "modelName": "Cohere-embed-v3-multilingual-hin",
             "resourceId": null,
             "region": null,
         },
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryモデルカタログベクトライザーに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Foundryモデルカタログにおけるベクトライザーに関するドキュメント（`vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md`）の更新を示しています。主な変更点には、日付の更新、サポートされるモデルのリストの改訂、主要パラメータの説明の修正が含まれています。

ドキュメントの日付が「2024年8月5日」から「2024年12月3日」に変更され、最新の情報が反映されています。また、重要な注意事項に関するセクションが強調されており、プレビュー中の機能に関する情報へのリンクが提供されています。

サポートされる埋め込みモデルのリストが整理され、特に現在サポートされているモデル名が新たに追加されています。具体的には、モデルIDには「OpenAI-CLIP」関連のものが削除され、「Facebook-DinoV2」と「Cohere」モデルのみに更新されています。この変更により、利用可能なモデルに関する理解が明確になります。

また、APIパラメータの説明も改訂され、`modelName`の指定方法についての記述が更新されています。特に、提案されたモデル名がベースモデルにランダムな3文字のサフィックスを含むことが説明され、具体的な例も示されています。

全体として、これらの変更は、ユーザーがAzure AI Foundryモデルカタログを通じてベクトライザーをより適切に活用できるようサポートすることを目的としており、ドキュメントの使い勝手と明瞭さを向上させています。


