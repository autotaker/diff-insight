---
date: '2025-09-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:36bd0d1...MicrosoftDocs:9fffe4d
summary: この変更は主にAPIバージョンの更新に焦点を当てており、ドキュメントが新しいAPIバージョン（2025-09-01）に切り替わりました。リスコアリングやベクター処理に関する詳細な説明が追加されており、ユーザーの理解を助ける内容となっています。また、過去のバージョンからのリンクや説明は新しい仕様に基づいて更新されており、より明確なガイドラインが提供されています。これにより、ユーザーは最新のAPI機能を効率的に利用し、操作の一貫性と信頼性が向上します。この更新は特に新しいユーザーや開発者がAzure
  AI Searchを導入しやすくすることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:36bd0d1...MicrosoftDocs:9fffe4d){target="_blank"}

<format>
# Highlights
この変更セットは主にAPIバージョンの更新を対象としており、多くのドキュメントが新しいAPIバージョン（2025-09-01）に切り替わっています。また、いくつかの文書では、特定の機能に関する説明やパラメータ設定についても更新が加えられています。ユーザーは最新のAPI機能を利用し、正確かつ効果的な操作を実行できるようになります。

## New features
- ドキュメント内のAPIバージョンが最新のバージョンで統一されました。
- リスコアリングやベクター処理に関する詳細な説明が追加され、利用者の理解を助けています。

## Breaking changes
- 過去のAPIバージョンからの変更により、リンクや説明が新しい仕様に従った形に更新されています。
- バイナリデータタイプのAPIバージョン情報が削除され、APIバージョン依存のない使用が明示されました。

## Other updates
- ベクター保存オプション、最適化手法、ストレージ設定に関するガイドラインが改訂され、より明確になっています。
- インデックスや検索におけるテキスト埋め込みの設定で新しいプレビュー版機能についての情報が提供されています。

# Insights
この更新は、Azure AI Searchの進化に対応し、すべてのドキュメントが最新版のAPIに準拠することを目的としています。特に、APIのバージョン管理により、ユーザーが開発を進める際の操作に関する一貫性と信頼性を向上させることに寄与しています。 

また、複数のドキュメントにわたって、具体的な手順や設定の選択についてのガイダンスが引き締められています。これによって、特に新しいユーザーや開発者が容易に最新の技術を利用して、効率的にAzure AI Searchを導入することが促進されます。

APIバージョンの更新がドキュメントの主要な内容であることから、従来のドキュメントを利用していた開発者に対しては、迅速な適応が求められるかもしれませんが、それによって得られるメリットは大きく、最新の機能を最大限に活用できます。また、良く文書化された情報により、より高度な設定や最適化手法が導入しやすくなっています。これに伴って、ユーザーの検索クエリ動作やデータ処理の効率が向上し、より高度な検索解析やデータ統合が可能になります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-aml-skill.md](#item-51366c) | minor update | APIバージョンに関する修正 | modified | 1 | 1 | 2 | 
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [cognitive-search-skill-azure-openai-embedding.md](#item-3eca57) | minor update | パラメータの必須性に関する明確化 | modified | 4 | 4 | 8 | 
| [cognitive-search-skill-textsplit.md](#item-9bf753) | minor update | パラメータの説明の整備 | modified | 8 | 8 | 16 | 
| [hybrid-search-how-to-query.md](#item-345ce6) | minor update | APIバージョンの更新 | modified | 4 | 4 | 8 | 
| [hybrid-search-overview.md](#item-6987b4) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [full-text-powershell.md](#item-1b28d3) | minor update | APIバージョンの更新 | modified | 8 | 8 | 16 | 
| [full-text-rest.md](#item-5d3419) | minor update | APIバージョンの更新 | modified | 4 | 4 | 8 | 
| [search-get-started-rbac-rest.md](#item-fd8ef4) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-get-started-vector-rest.md](#item-c7d261) | minor update | APIバージョンの更新 | modified | 8 | 8 | 16 | 
| [skillset-rest.md](#item-a9668d) | minor update | APIバージョンの更新 | modified | 7 | 7 | 14 | 
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | 日付とAPIバージョンの更新 | modified | 4 | 4 | 8 | 
| [index-add-suggesters.md](#item-28ed57) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [index-ranking-similarity.md](#item-ba07fa) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [index-similarity-and-scoring.md](#item-75603d) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [knowledge-store-create-rest.md](#item-2643dd) | minor update | APIバージョンの更新 | modified | 6 | 6 | 12 | 
| [monitor-azure-cognitive-search-data-reference.md](#item-561425) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [query-lucene-syntax.md](#item-736436) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [query-simple-syntax.md](#item-ab3c96) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-add-autocomplete-suggestions.md](#item-0a43e0) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-blob-storage-integration.md](#item-bbdaa6) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-faq-frequently-asked-questions.yml](#item-eab2ba) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-file-storage-integration.md](#item-d20e26) | minor update | APIバージョンの更新 | modified | 3 | 3 | 6 | 
| [search-filters.md](#item-3f2a7a) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-how-to-define-index-projections.md](#item-a7e2c5) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-how-to-index-csv-blobs.md](#item-2c3f3e) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-how-to-index-sql-database.md](#item-86d873) | minor update | APIバージョンの更新 | modified | 6 | 6 | 12 | 
| [search-how-to-integrated-vectorization.md](#item-86fb1e) | minor update | APIバージョンの更新 | modified | 6 | 6 | 12 | 
| [search-how-to-load-search-index.md](#item-a72573) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-howto-index-azure-data-lake-storage.md](#item-c21e43) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-howto-index-changed-deleted-blobs.md](#item-32a688) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-howto-index-cosmosdb.md](#item-568fab) | minor update | APIバージョンの更新 | modified | 5 | 5 | 10 | 
| [search-howto-index-json-blobs.md](#item-b8230c) | minor update | APIバージョンの更新 | modified | 3 | 3 | 6 | 
| [search-howto-index-plaintext-blobs.md](#item-63efcb) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-howto-indexing-azure-blob-storage.md](#item-dc4668) | minor update | APIバージョンの更新 | modified | 6 | 6 | 12 | 
| [search-howto-indexing-azure-tables.md](#item-7655b0) | minor update | APIバージョンの更新 | modified | 4 | 4 | 8 | 
| [search-howto-managed-identities-cosmos-db.md](#item-a74464) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-howto-managed-identities-sql.md](#item-2af8aa) | minor update | APIバージョンの更新 | modified | 3 | 3 | 6 | 
| [search-howto-managed-identities-storage.md](#item-8209c4) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-howto-powerapps.md](#item-92d1c0) | minor update | APIバージョンの更新 | modified | 3 | 3 | 6 | 
| [search-howto-reindex.md](#item-46738a) | minor update | APIバージョンの更新 | modified | 6 | 6 | 12 | 
| [search-howto-schedule-indexers.md](#item-d57e7b) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-index-azure-sql-managed-instance-with-managed-identity.md](#item-a4ec86) | minor update | APIバージョンの更新 | modified | 3 | 3 | 6 | 
| [search-indexer-field-mappings.md](#item-0e4628) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-indexer-how-to-access-private-sql.md](#item-1bd4cc) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-indexer-troubleshooting.md](#item-087365) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-language-support.md](#item-a7979b) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-lucene-query-architecture.md](#item-b0d568) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-monitor-indexers.md](#item-5235df) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-monitor-queries.md](#item-279569) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-pagination-page-layout.md](#item-115902) | minor update | APIバージョンの更新 | modified | 8 | 8 | 16 | 
| [search-query-create.md](#item-532822) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-query-fuzzy.md](#item-a130e3) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-query-lucene-examples.md](#item-ce3624) | minor update | APIバージョンの更新 | modified | 8 | 8 | 16 | 
| [search-query-overview.md](#item-dcd5d6) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-query-simple-examples.md](#item-834766) | minor update | APIバージョンの更新 | modified | 11 | 11 | 22 | 
| [search-security-api-keys.md](#item-d8c908) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-security-get-encryption-keys.md](#item-7aed9d) | minor update | APIバージョンの更新 | modified | 4 | 4 | 8 | 
| [search-security-rbac.md](#item-a5d129) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-security-trimming-for-azure-search.md](#item-d8ae51) | minor update | APIバージョンの更新 | modified | 3 | 3 | 6 | 
| [search-semi-structured-data.md](#item-d3388d) | minor update | APIバージョンの更新 | modified | 10 | 10 | 20 | 
| [search-synapseml-cognitive-services.md](#item-dcc36f) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-synonyms.md](#item-2d5d63) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [semantic-how-to-query-request.md](#item-85530d) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [tutorial-create-custom-analyzer.md](#item-ad5520) | minor update | APIバージョンの更新 | modified | 8 | 8 | 16 | 
| [vector-search-how-to-configure-compression-storage.md](#item-c653c3) | minor update | REST APIの更新 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-configure-vectorizer.md](#item-30ffd8) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-create-index.md](#item-97c769) | minor update | APIバージョンの更新 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-index-binary-data.md](#item-b233b9) | minor update | バイナリデータタイプのAPIバージョン情報の更新 | modified | 2 | 2 | 4 | 
| [vector-search-how-to-quantization.md](#item-744f48) | minor update | リスコアリングとオーバーサンプリングに関する情報の更新 | modified | 6 | 4 | 10 | 
| [vector-search-how-to-query.md](#item-9bb93c) | minor update | APIバージョンの更新と説明の修正 | modified | 13 | 13 | 26 | 
| [vector-search-how-to-storage-options.md](#item-ee1680) | minor update | ベクター保存オプションに関する情報の更新 | modified | 28 | 40 | 68 | 
| [vector-search-index-size.md](#item-bb2846) | minor update | APIバージョンの更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/cognitive-search-aml-skill.md{#item-51366c}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,7 @@ Like other built-in skills, a custom **AML** skill has inputs and outputs. The i
 > * `503 Service Unavailable`
 > * `429 Too Many Requests`
 
-You can call the **AML** skill with the 2024-07-01 stable API version or an equivalent Azure SDK. For connections to the model catalog in the Azure AI Foundry portal, use the 2024-05-01-preview API version or later.
+You can call the **AML** skill with the stable REST API version or an equivalent Azure SDK. For connections to the model catalog in the Azure AI Foundry portal, use a preview API version.
 
 ## AML skill for models in Azure AI Foundry
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンに関する修正"
}
```

### Explanation
この変更は、ドキュメント 'cognitive-search-aml-skill.md' の内容を更新するもので、APIの呼び出しに関する情報を修正しています。具体的には、**AML**スキルを呼び出す際に使用するAPIバージョンの記述が変更されました。以前は「2024-07-01安定版APIバージョンまたは同等のAzure SDK」を使用するとされていましたが、更新後は「安定したREST APIバージョンまたは同等のAzure SDK」と記載されています。また、Azure AI Foundryポータル内のモデルカタログへの接続に関する注意事項も、「2024-05-01プレリリースAPIバージョンまたはそれ以降」とから「プレリリースAPIバージョン」に簡略化されています。この変更は、より明確で簡潔な表現を目指したものです。

## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -235,7 +235,7 @@ Enrichments are billable operations. If you no longer need to call Azure AI serv
 1. Remove the key in the body of the definition, and then send the request:
 
     ```http
-    PUT https://[servicename].search.windows.net/skillsets/[skillset name]?api-version=2024-07-01
+    PUT https://[servicename].search.windows.net/skillsets/[skillset name]?api-version=2025-09-01
     api-key: [admin key]
     Content-Type: application/json
     {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、ドキュメント 'cognitive-search-attach-cognitive-services.md' におけるAPIのバージョン情報を更新するものです。具体的には、HTTP PUTリクエストを使用してスキルセットを更新する際のAPIバージョンが「2024-07-01」から「2025-09-01」に変更されています。この修正により、最新のAPIを使用するように促す意図があります。他の部分に変更はありませんが、APIバージョンの指定は、ドキュメントの正確性と最新の情報を維持する上で重要です。

## articles/search/cognitive-search-skill-azure-openai-embedding.md{#item-3eca57}

<details>
<summary>Diff</summary>
````diff
@@ -45,12 +45,12 @@ Parameters are case-sensitive.
 
 | Inputs | Description |
 |---------------------|-------------|
-| `resourceUri` | The URI of the model provider. This parameter only supports URLs with the `openai.azure.com` domain, such as `https://<resourcename>.openai.azure.com`. If your Azure OpenAI endpoint has a URL with the `cognitiveservices.azure.com` domain, such as `https://<resourcename>.cognitiveservices.azure.com`, you must create a [custom subdomain](/azure/ai-services/openai/how-to/use-your-data-securely#enabled-custom-subdomain) with `openai.azure.com` for the Azure OpenAI resource and use `https://<resourcename>.openai.azure.com` instead. This field is required if your Azure OpenAI resource is deployed behind a private endpoint or uses Virtual Network (VNet) integration. [Azure API Management](/azure/api-management/api-management-key-concepts) endpoints are supported with URL `https://<resourcename>.azure-api.net `. Shared private links aren't supported for API Management endpoints.
+| `resourceUri` | Required. The URI of the model provider. This parameter only supports URLs with the `openai.azure.com` domain, such as `https://<resourcename>.openai.azure.com`. If your Azure OpenAI endpoint has a URL with the `cognitiveservices.azure.com` domain, such as `https://<resourcename>.cognitiveservices.azure.com`, you must create a [custom subdomain](/azure/ai-services/openai/how-to/use-your-data-securely#enabled-custom-subdomain) with `openai.azure.com` for the Azure OpenAI resource and use `https://<resourcename>.openai.azure.com` instead. This field is required if your Azure OpenAI resource is deployed behind a private endpoint or uses Virtual Network (VNet) integration. [Azure API Management](/azure/api-management/api-management-key-concepts) endpoints are supported with URL `https://<resourcename>.azure-api.net `. Shared private links aren't supported for API Management endpoints.
 | `apiKey`   |  The secret key used to access the model. If you provide a key, leave `authIdentity` empty. If you set both the `apiKey` and `authIdentity`, the `apiKey` is used on the connection. |
-| `deploymentId`   | The name of the deployed Azure OpenAI embedding model. The model should be an embedding model, such as text-embedding-ada-002. See the [List of Azure OpenAI models](/azure/ai-services/openai/concepts/models) for supported models.|
+| `deploymentId`   | Required. The name of the deployed Azure OpenAI embedding model. The model should be an embedding model, such as text-embedding-ada-002. See the [List of Azure OpenAI models](/azure/ai-services/openai/concepts/models) for supported models.|
 | `authIdentity`   | A user-managed identity used by the search service for connecting to Azure OpenAI. You can use either a [system or user managed identity](search-how-to-managed-identities.md). To use a system managed identity, leave `apiKey` and `authIdentity` blank. The system-managed identity is used automatically. A managed identity must have [Cognitive Services OpenAI User](/azure/ai-services/openai/how-to/role-based-access-control#azure-openai-roles) permissions to send text to Azure OpenAI. |
-| `modelName` | This property is required if your skillset is created using the 2024-05-01-preview or 2024-07-01 REST API. Set this property to the deployment name of an Azure OpenAI embedding model deployed on the provider specified through `resourceUri` and identified through `deploymentId`. Currently, the supported values are `text-embedding-ada-002`, `text-embedding-3-large`, and `text-embedding-3-small`.  |
-| `dimensions` | Optional, starting in the 2024-05-01-preview REST API, the dimensions of embeddings that you would like to generate, assuming the model supports a range of dimensions. Supported ranges are listed below, and currently only apply to the text-embedding-3 model series. The default is the maximum dimensions for each model. For skillsets created using earlier REST API versions dating back to the 2023-10-01-preview, dimensions are fixed at 1536. When setting the dimensions property on a skill, make sure to set the `dimensions` property on the [vector field definition](vector-search-how-to-create-index.md#add-a-vector-field-to-the-fields-collection) to the same value. |
+| `modelName` | Required. Set this property to the deployment name of an Azure OpenAI embedding model deployed on the provider specified through `resourceUri` and identified through `deploymentId`. Currently, the supported values are `text-embedding-ada-002`, `text-embedding-3-large`, and `text-embedding-3-small`.  |
+| `dimensions` | Optional. The dimensions of embeddings that you would like to generate, assuming the model supports a range of dimensions. Supported ranges are listed below, and currently only apply to the text-embedding-3 model series. The default is the maximum dimensions for each model. For skillsets created using earlier REST API versions dating back to the 2023-10-01-preview, dimensions are fixed at 1536. When setting the dimensions property on a skill, make sure to set the `dimensions` property on the [vector field definition](vector-search-how-to-create-index.md#add-a-vector-field-to-the-fields-collection) to the same value. |
 
 ## Supported dimensions by `modelName`
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "パラメータの必須性に関する明確化"
}
```

### Explanation
この変更は、ドキュメント 'cognitive-search-skill-azure-openai-embedding.md' のパラメータに関する説明を更新し、いくつかの入力フィールドの必須性を明確にしたものです。具体的には、`resourceUri`と`deploymentId`のフィールドが「Required」とされ、これらのフィールドが必須であることが強調されています。これにより、ユーザーが必要な情報を正確に把握し、リクエストを適切に構成できるようになります。また、その他のフィールドに関する説明文も一部修正されており、特にオプションとして扱われる`dimensions`フィールドの説明が追加されています。この修正によって、ユーザーが各パラメータの役割や必要性をより理解しやすくなっています。

## articles/search/cognitive-search-skill-textsplit.md{#item-9bf753}

<details>
<summary>Diff</summary>
````diff
@@ -33,15 +33,15 @@ Microsoft.Skills.Text.SplitSkill
 
 Parameters are case-sensitive. 
 
-| Parameter name     | Version   | Description |
+| Parameter name     | Description |
 |--------------------|-------------|-------------|
-| `textSplitMode`    | All versions | Either `pages` or `sentences`. Pages have a configurable maximum length, but the skill attempts to avoid truncating a sentence so the actual length might be smaller. Sentences are a string that terminates at sentence-ending punctuation, such as a period, question mark, or exclamation point, assuming the language has sentence-ending punctuation. | 
-| `maximumPageLength` | All versions | Only applies if `textSplitMode` is set to `pages`. For `unit` set to `characters`, this parameter refers to the maximum page length in characters as measured by `String.Length`. The minimum value is 300, the maximum is 50000, and the default value is 5000.  The algorithm does its best to break the text on sentence boundaries, so the size of each chunk might be slightly less than `maximumPageLength`. <br><br>For `unit` set to `azureOpenAITokens`, the maximum page length is the token length limit of the model. For text embedding models, a general recommendation for page length is 512 tokens. |
-| `defaultLanguageCode`	| All versions | (optional) One of the following language codes: `am, bs, cs, da, de, en, es, et, fr, he, hi, hr, hu, fi, id, is, it, ja, ko, lv, no, nl, pl, pt-PT, pt-BR, ru, sk, sl, sr, sv, tr, ur, zh-Hans`. Default is English (en). A few things to consider: <ul><li>Providing a language code is useful to avoid cutting a word in half for nonwhitespace languages such as Chinese, Japanese, and Korean.</li><li>If you don't know the language  in advance (for example, if you're using the [LanguageDetectionSkill](cognitive-search-skill-language-detection.md) to detect language), we recommend the `en` default. </li></ul>  |
-| `pageOverlapLength` | [2024-07-01](/rest/api/searchservice/skillsets/create-or-update) | Only applies if `textSplitMode` is set to `pages`. Each page starts with this number of characters or tokens from the end of the previous page. If this parameter is set to 0, there's no overlapping text on successive pages. This [example](#example-for-chunking-and-vectorization) includes the parameter. |
-| `maximumPagesToTake` | [2024-07-01](/rest/api/searchservice/skillsets/create-or-update) | Only applies if `textSplitMode` is set to `pages`. Number of pages to return. The default is 0, which means to return all pages. You should set this value if only a subset of pages are needed. This [example](#example-for-chunking-and-vectorization) includes the parameter.|
-| `unit` | [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | **New**. Only applies if `textSplitMode` is set to `pages`. Specifies whether to chunk by `characters` (default) or `azureOpenAITokens`. Setting the unit affects `maximumPageLength` and `pageOverlapLength`. |
-| `azureOpenAITokenizerParameters` | [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | **New**. An object providing extra parameters for the `azureOpenAITokens` unit. <br><br>`encoderModelName` is a designated tokenizer used for converting text into tokens, essential for natural language processing (NLP) tasks. Different models use different tokenizers. Valid values include cl100k_base (default) used by GPT-35-Turbo and GPT-4. Other valid values are r50k_base, p50k_base, and p50k_edit. The skill implements the tiktoken library by way of [SharpToken](https://www.nuget.org/packages/SharpToken) and `Microsoft.ML.Tokenizers` but doesn't support every encoder. For example, there's currently no support for o200k_base encoding used by GPT-4o. <br><br>`allowedSpecialTokens` defines a collection of special tokens that are permitted within the tokenization process. Special tokens are  string that you want to treat uniquely, ensuring they aren't split during tokenization. For example ["[START"], "[END]"]. If the `tiktoken` library doesn't perform tokenization as expected, either due to language-specific limitations or other unexpected behaviors, it's recommended to use text splitting instead.|
+| `textSplitMode`    | Either `pages` or `sentences`. Pages have a configurable maximum length, but the skill attempts to avoid truncating a sentence so the actual length might be smaller. Sentences are a string that terminates at sentence-ending punctuation, such as a period, question mark, or exclamation point, assuming the language has sentence-ending punctuation. | 
+| `maximumPageLength` | Only applies if `textSplitMode` is set to `pages`. For `unit` set to `characters`, this parameter refers to the maximum page length in characters as measured by `String.Length`. The minimum value is 300, the maximum is 50000, and the default value is 5000.  The algorithm does its best to break the text on sentence boundaries, so the size of each chunk might be slightly less than `maximumPageLength`. <br><br>For `unit` set to `azureOpenAITokens`, the maximum page length is the token length limit of the model. For text embedding models, a general recommendation for page length is 512 tokens. |
+| `defaultLanguageCode`	| (optional) One of the following language codes: `am, bs, cs, da, de, en, es, et, fr, he, hi, hr, hu, fi, id, is, it, ja, ko, lv, no, nl, pl, pt-PT, pt-BR, ru, sk, sl, sr, sv, tr, ur, zh-Hans`. Default is English (en). A few things to consider: <ul><li>Providing a language code is useful to avoid cutting a word in half for nonwhitespace languages such as Chinese, Japanese, and Korean.</li><li>If you don't know the language  in advance (for example, if you're using the [LanguageDetectionSkill](cognitive-search-skill-language-detection.md) to detect language), we recommend the `en` default. </li></ul>  |
+| `pageOverlapLength` | Only applies if `textSplitMode` is set to `pages`. Each page starts with this number of characters or tokens from the end of the previous page. If this parameter is set to 0, there's no overlapping text on successive pages. This [example](#example-for-chunking-and-vectorization) includes the parameter. |
+| `maximumPagesToTake` | Only applies if `textSplitMode` is set to `pages`. Number of pages to return. The default is 0, which means to return all pages. You should set this value if only a subset of pages are needed. This [example](#example-for-chunking-and-vectorization) includes the parameter.|
+| `unit` | Only applies if `textSplitMode` is set to `pages`. Specifies whether to chunk by `characters` (default) or `azureOpenAITokens`. Setting the unit affects `maximumPageLength` and `pageOverlapLength`. |
+| `azureOpenAITokenizerParameters` An object providing extra parameters for the `azureOpenAITokens` unit. <br><br>`encoderModelName` is a designated tokenizer used for converting text into tokens, essential for natural language processing (NLP) tasks. Different models use different tokenizers. Valid values include cl100k_base (default) used by GPT-35-Turbo and GPT-4. Other valid values are r50k_base, p50k_base, and p50k_edit. The skill implements the tiktoken library by way of [SharpToken](https://www.nuget.org/packages/SharpToken) and `Microsoft.ML.Tokenizers` but doesn't support every encoder. For example, there's currently no support for o200k_base encoding used by GPT-4o. <br><br>`allowedSpecialTokens` defines a collection of special tokens that are permitted within the tokenization process. Special tokens are  string that you want to treat uniquely, ensuring they aren't split during tokenization. For example ["[START"], "[END]"]. If the `tiktoken` library doesn't perform tokenization as expected, either due to language-specific limitations or other unexpected behaviors, it's recommended to use text splitting instead.|
 
 ## Skill Inputs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "パラメータの説明の整備"
}
```

### Explanation
この変更は、ドキュメント 'cognitive-search-skill-textsplit.md' のパラメータ説明を見直し、情報を整理したものです。具体的には、テーブルの構造を変更し、すべてのパラメータに関する説明を簡潔に示しています。また、いくつかのパラメータの詳細な説明を明確にし、特に新規に追加された`azureOpenAITokenizerParameters`や、ページ分割に関連するパラメータについての情報が整備されています。これにより、ユーザーは各パラメータの役割や使用方法を理解しやすくなり、テキストをより効果的に分割するための設定ができるようになります。全体として、ドキュメントの明瞭さと利用価値が向上しています。

## articles/search/hybrid-search-how-to-query.md{#item-345ce6}

<details>
<summary>Diff</summary>
````diff
@@ -105,7 +105,7 @@ The following example shows a hybrid query request using the REST API.
 This example is from the [vector quickstart](https://raw.githubusercontent.com/Azure-Samples/azure-search-rest-samples/refs/heads/main/Quickstart-vectors/az-search-quickstart-vectors.rest) that has vector and nonvector content, and several query examples. For brevity, the vector is truncated in this article. 
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-07-01
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2025-09-01
 Content-Type: application/json
 api-key: {{admin-api-key}}
 {
@@ -240,7 +240,7 @@ This section has multiple query examples that illustrate hybrid query patterns.
 This example adds a filter, which is applied to the `filterable` nonvector fields of the search index.
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-07-01
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2025-09-01
 Content-Type: application/json
 api-key: {{admin-api-key}}
 {
@@ -324,7 +324,7 @@ Assuming that you [have semantic ranker](semantic-how-to-enable-disable.md) and
 Whenever you use semantic ranking with vectors, make sure `k` is set to 50. Semantic ranker uses up to 50 matches as input. Specifying less than 50 deprives the semantic ranking models of necessary inputs.
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-07-01
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2025-09-01
 Content-Type: application/json
 api-key: {{admin-api-key}}
 {
@@ -365,7 +365,7 @@ api-key: {{admin-api-key}}
 Here's the last query in the collection. It's the same semantic hybrid query as the previous example, but with a filter.
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-07-01
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2025-09-01
 Content-Type: application/json
 api-key: {{admin-api-key}}
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更では、'hybrid-search-how-to-query.md' ドキュメント内のすべてのAPIリクエストに関連するバージョン番号が2024-07-01から2025-09-01に更新されています。これにより、最新のAPI機能や改善点を利用できることが示されます。また、同じ内容のリクエストが複数の箇所で修正されており、それに応じて文書の整合性が保たれています。ユーザーにとっては、新しいバージョンのAPIを使用する際のリクエスト構造が一貫しており、混乱を避けつつ最新情報にアクセスできるようになっています。全体として、APIの変更に適応した内容の整備が行われています。

## articles/search/hybrid-search-overview.md{#item-6987b4}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ Hybrid search is predicated on having a search index that contains fields of var
 A representative hybrid query might be as follows (notice that the vector queries have placeholder values for brevity):
 
 ```http
-POST https://{{searchServiceName}}.search.windows.net/indexes/hotels-vector-quickstart/docs/search?api-version=2024-07-01
+POST https://{{searchServiceName}}.search.windows.net/indexes/hotels-vector-quickstart/docs/search?api-version=2025-09-01
   content-type: application/JSON
 {
     "count": true,
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'hybrid-search-overview.md' ドキュメント内の代表的なハイブリッドクエリの例において、APIのバージョン番号を2024-07-01から2025-09-01に更新したものです。これにより、最新のAPI機能に対応することが明示され、ユーザーは新しいバージョンを使用したリクエスト方法を正確に理解できるようになります。この更新により、ドキュメントは最新の技術に適応し、整合性を保ちつつ信頼性が向上します。全体として、APIの変更に即した無駄のない情報提供が行われています。

## articles/search/includes/quickstarts/full-text-powershell.md{#item-1b28d3}

<details>
<summary>Diff</summary>
````diff
@@ -92,7 +92,7 @@ To connect to your search service:
 1. Create a `$url` object that targets the indexes collection on your search service. Replace `<YOUR-SEARCH-SERVICE>` with the value you obtained in [Get endpoint](#get-endpoint).
 
     ```powershell
-    $url = "<YOUR-SEARCH-SERVICE>/indexes?api-version=2024-07-01&`$select=name"
+    $url = "<YOUR-SEARCH-SERVICE>/indexes?api-version=2025-09-01&`$select=name"
     ```
 
 1. Run `Invoke-RestMethod` to send a GET request to your search service. Include `ConvertTo-Json` to view responses from the service.
@@ -152,7 +152,7 @@ To create an index:
 2. Update the `$url` object to target the new index. Replace `<YOUR-SEARCH-SERVICE>` with the value you obtained in [Get endpoint](#get-endpoint).
 
     ```powershell
-    $url = "<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart?api-version=2024-07-01"
+    $url = "<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart?api-version=2025-09-01"
     ```
 
 3. Run `Invoke-RestMethod` to create the index on your search service.
@@ -275,7 +275,7 @@ To upload documents to your index:
 2. Update the `$url` object to target the indexing endpoint. Replace `<YOUR-SEARCH-SERVICE>` with the value you obtained in [Get endpoint](#get-endpoint).
 
     ```powershell
-    $url = "<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs/index?api-version=2024-07-01"
+    $url = "<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs/index?api-version=2025-09-01"
     ```
 
 3. Run `Invoke-RestMethod` to send the upload request to your search service.
@@ -301,7 +301,7 @@ To run a full-text query against your index:
 1. Update the `$url` object to specify search parameters. Replace `<YOUR-SEARCH-SERVICE>` with the value you obtained in [Get endpoint](#get-endpoint).
 
     ```powershell
-    $url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2024-07-01&search=attached restaurant&searchFields=Description,Tags&$select=HotelId,HotelName,Tags,Description&$count=true'
+    $url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2025-09-01&search=attached restaurant&searchFields=Description,Tags&$select=HotelId,HotelName,Tags,Description&$count=true'
     ```
 
 2. Run `Invoke-RestMethod` to send the query request to your search service.
@@ -344,20 +344,20 @@ Run the following commands to explore the query syntax. You can perform string s
 # Query example 1
 # Search the index for the terms 'restaurant' and 'wifi'
 # Return only the HotelName, Description, and Tags fields
-$url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2024-07-01&search=restaurant wifi&$count=true&$select=HotelName,Description,Tags'
+$url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2025-09-01&search=restaurant wifi&$count=true&$select=HotelName,Description,Tags'
 
 # Query example 2 
 # Use a filter to find hotels rated 4 or higher
 # Return only the HotelName and Rating fields
-$url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2024-07-01&search=*&$filter=Rating gt 4&$select=HotelName,Rating'
+$url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2025-09-01&search=*&$filter=Rating gt 4&$select=HotelName,Rating'
 
 # Query example 3
 # Take the top two results
 # Return only the HotelName and Category fields
-$url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2024-07-01&search=boutique&$top=2&$select=HotelName,Category'
+$url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2025-09-01&search=boutique&$top=2&$select=HotelName,Category'
 
 # Query example 4
 # Sort by a specific field (Address/City) in ascending order
 # Return only the HotelName, Address/City, Tags, and Rating fields
-$url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2024-07-01&search=pool&$orderby=Address/City asc&$select=HotelName, Address/City, Tags, Rating'
+$url = '<YOUR-SEARCH-SERVICE>/indexes/hotels-quickstart/docs?api-version=2025-09-01&search=pool&$orderby=Address/City asc&$select=HotelName, Address/City, Tags, Rating'
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'full-text-powershell.md' ドキュメントにおいて、PowerShellを使用して検索サービスに接続するためのURLに含まれるAPIバージョンを2024-07-01から2025-09-01に更新したものです。具体的には、検索インデックスやドキュメントのアップロード、およびフルテキストクエリに関連するコードスニペットが修正されています。これにより、ユーザーは最新のAPIバージョンを使用して、正確で有効なリクエストを行うことができるようになります。この更新は、 APIの進化に伴い、適切な情報を提供するために行われ、文書の整合性と信頼性を高めています。全体として、ドキュメントは最新の技術に即しており、ユーザーの利便性を向上させています。

## articles/search/includes/quickstarts/full-text-rest.md{#item-5d3419}

<details>
<summary>Diff</summary>
````diff
@@ -89,7 +89,7 @@ To set up your request file:
     @token = PUT-YOUR-PERSONAL-IDENTITY-TOKEN-HERE
 
     ### List existing indexes by name
-    GET {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
+    GET {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
         Authorization: Bearer {{token}}
     ```
 
@@ -111,7 +111,7 @@ To create an index:
 
     ```http
     ### Create a new index
-    POST {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
         Content-Type: application/json
         Authorization: Bearer {{token}}
     
@@ -169,7 +169,7 @@ To upload documents to your index:
 
     ```http
     ### Upload documents
-    POST {{baseUrl}}/indexes/hotels-quickstart/docs/index?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexes/hotels-quickstart/docs/index?api-version=2025-09-01  HTTP/1.1
         Content-Type: application/json
         Authorization: Bearer {{token}}
     
@@ -275,7 +275,7 @@ To run a full-text query against your index:
 
     ```http
     ### Run a query
-    POST {{baseUrl}}/indexes/hotels-quickstart/docs/search?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexes/hotels-quickstart/docs/search?api-version=2025-09-01  HTTP/1.1
       Content-Type: application/json
       Authorization: Bearer {{token}}
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'full-text-rest.md' ドキュメントにおける複数のREST APIリクエストの例を更新することを目的としています。具体的には、各リクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。この更新は、次のリクエストタイプに適用されています：既存のインデックスのリスト、インデックスの作成、ドキュメントのアップロード、およびフルテキストクエリの実行。これにより、ユーザーは最新のAPIバージョンを利用して、正確で効果的なリクエストを行うことができるようになります。この修正は、APIの変更に適応し、ドキュメントの整合性を保つことで、ユーザーに対する信頼性のある情報提供を確保しています。全体として、これによりユーザー体験が向上し、最新の技術に基づく正しいガイダンスが提供されます。

## articles/search/includes/quickstarts/search-get-started-rbac-rest.md{#item-fd8ef4}

<details>
<summary>Diff</summary>
````diff
@@ -75,7 +75,7 @@ To connect using REST:
    @token = PUT-YOUR-PERSONAL-IDENTITY-TOKEN-HERE
 
    ### List existing indexes
-   GET {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
+   GET {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
       Content-Type: application/json
       Authorization: Bearer {{token}}
    ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-get-started-rbac-rest.md' ドキュメントにおけるREST APIリクエストの例を更新するものです。具体的には、既存のインデックスをリストするためのAPIリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。この更新により、ユーザーは最新のAPIを利用して、正確かつ効果的なリクエストを送信できるようになります。APIのバージョンを最新のものに更新することで、ドキュメントはより信頼性のあるものとなり、新しい機能や改善を独自に活用できるようになります。全体として、この小規模な変更は文書の整合性を保ち、ユーザーに対する正確な情報提供を確保することに寄与しています。

## articles/search/includes/quickstarts/search-get-started-vector-rest.md{#item-c7d261}

<details>
<summary>Diff</summary>
````diff
@@ -109,7 +109,7 @@ The index schema in this example is organized around hotel content. Sample data
 
     ```http
     ### Create a new index
-    POST  {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
+    POST  {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{token}}
 
@@ -402,7 +402,7 @@ In Azure AI Search, the index contains all searchable data and queries run on th
 
     ```http
     ### Upload documents
-    POST {{baseUrl}}/indexes/hotels-quickstart-vectors/docs/index?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexes/hotels-quickstart-vectors/docs/index?api-version=2025-09-01  HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{token}}
 
@@ -673,7 +673,7 @@ The vector query string is semantically similar to the search string, but it inc
 
     ```http
     ### Run a single vector query
-    POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2025-09-01  HTTP/1.1
         Content-Type: application/json
         Authorization: Bearer {{token}}
         
@@ -784,7 +784,7 @@ You can add filters, but the filters are applied to the nonvector content in you
 
     ```http
     ### Run a vector query with a filter
-    POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2025-09-01  HTTP/1.1
         Content-Type: application/json
         Authorization: Bearer {{token}}
     
@@ -847,7 +847,7 @@ You can add filters, but the filters are applied to the nonvector content in you
 
     ```http
     ### Run a vector query with a geo filter
-    POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2025-09-01  HTTP/1.1
         Content-Type: application/json
         Authorization: Bearer {{token}}
     
@@ -917,7 +917,7 @@ Hybrid search consists of keyword queries and vector queries in a single search
 
     ```http
     ### Run a hybrid query
-    POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2025-09-01  HTTP/1.1
         Content-Type: application/json
         Authorization: Bearer {{token}}
         
@@ -1033,7 +1033,7 @@ Here's the last query in the collection. This hybrid query adds L2 semantic rank
 
     ```http
     ### Run a hybrid query with semantic reranking
-    POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search?api-version=2025-09-01  HTTP/1.1
         Content-Type: application/json
         Authorization: Bearer {{token}}
 
@@ -1127,7 +1127,7 @@ If you want to keep the search service, but delete the index and documents, you
 
 ```http
 ### Delete an index
-DELETE  {{baseUrl}}/indexes/hotels-vector-quickstart?api-version=2024-07-01 HTTP/1.1
+DELETE  {{baseUrl}}/indexes/hotels-vector-quickstart?api-version=2025-09-01 HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{token}}
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-get-started-vector-rest.md' ドキュメントにおいて、複数のREST APIリクエストの例を最新のAPIバージョンに更新するものです。具体的には、インデックスの作成、ドキュメントのアップロード、ベクターベースの検索リクエスト、およびインデックスの削除に使用されるAPIバージョンを2024-07-01から2025-09-01に変更しています。この修正により、ユーザーは最新のAPI仕様に従ったリクエストを送信でき、より新しい機能や改善点を利用することが可能になります。また、このような変更は、文書による情報の正確性や整合性を保つためにも重要です。全体として、これによりユーザーの体験が向上し、AzureのAI検索サービスでの操作が円滑になります。

## articles/search/includes/tutorials/skillset-rest.md{#item-a9668d}

<details>
<summary>Diff</summary>
````diff
@@ -97,7 +97,7 @@ Call [Create Data Source](/rest/api/searchservice/data-sources/create) to set th
 
 ```http
 ### Create a data source
-POST {{baseUrl}}/datasources?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/datasources?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
 
@@ -124,7 +124,7 @@ Call [Create Skillset](/rest/api/searchservice/skillsets/create) to specify whic
 
 ```http
 ### Create a skillset
-POST {{baseUrl}}/skillsets?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/skillsets?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
 
@@ -313,7 +313,7 @@ The largest component of an index is the fields collection, where data type and
 
 ```http
 ### Create an index
-POST {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
 
@@ -406,7 +406,7 @@ Expect this step to take several minutes to complete. Even though the data set i
 
 ```http
 ### Create and run an indexer
-POST {{baseUrl}}/indexers?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexers?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
 
@@ -497,7 +497,7 @@ To find out whether the indexer is still running, call [Get Indexer Status](/res
 
 ```http
 ### Get Indexer Status (wait several minutes for the indexer to complete)
-GET {{baseUrl}}/indexers/cog-search-demo-idxr/status?api-version=2024-07-01  HTTP/1.1
+GET {{baseUrl}}/indexers/cog-search-demo-idxr/status?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
 ```
@@ -514,7 +514,7 @@ Now that you've created an index that contains AI-generated content, call [Searc
 
 ```http
 ### Query the index\
-POST {{baseUrl}}/indexes/cog-search-demo-idx/docs/search?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexes/cog-search-demo-idx/docs/search?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
   
@@ -529,7 +529,7 @@ Filters can help you narrow results to items of interest:
 
 ```http
 ### Filter by organization
-POST {{baseUrl}}/indexes/cog-search-demo-idx/docs/search?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexes/cog-search-demo-idx/docs/search?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
   
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'skillset-rest.md' ドキュメントにおいて、複数のREST APIリクエストの例を最新のAPIバージョンに更新することを目的としています。具体的には、データソースの作成、スキルセットの作成、インデックスの作成、インデクサの作成と実行、インデクサのステータス取得、インデックスのクエリ生成に関連する全てのAPIリクエストを2024-07-01から2025-09-01に更新しています。この修正によれば、ユーザーは最新のAPI機能や変更を考慮した上でコンテンツを操作できるため、より効果的にAzureのAIサービスを利用できるようになります。また、これによりドキュメントの整合性と信頼性が向上し、ユーザーが正確な情報を利用できる環境を提供します。全体として、これらの小規模な更新はユーザーの利用体験を改善し、Azure AIの機能を最大限に活用する手助けとなります。

## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 07/25/2025
+ms.date: 09/29/2025
 ms.update-cycle: 365-days
 ---
 
@@ -31,11 +31,11 @@ You can add a scoring profile to an index by editing its JSON definition in the
 
 ## Rules for scoring profiles
 
-You can use scoring profiles in [keyword search](search-lucene-query-architecture.md), [vector search](vector-search-overview.md), [hybrid search](hybrid-search-overview.md), and [semantic search (reranking)](semantic-search-overview.md). However, scoring profiles only apply to nonvector fields, so make sure your index has text or numeric fields that can be boosted or weighted. 
+You can use scoring profiles in [keyword search](search-lucene-query-architecture.md), [vector search](vector-search-overview.md), [hybrid search](hybrid-search-overview.md), and [semantic reranking)](semantic-search-overview.md). However, scoring profiles only apply to nonvector fields, so make sure your index has text or numeric fields that can be boosted or weighted. 
 
 You can have up to 100 scoring profiles within an index (see [service Limits](search-limits-quotas-capacity.md)), but you can only specify one profile at time in any given query.
 
-You can use [semantic ranker](semantic-how-to-query-request.md) with scoring profiles. Currently in preview, you can apply a [scoring profile after semantic ranking](semantic-how-to-enable-scoring-profiles.md). Otherwise, when multiple ranking or relevance features are in play, semantic ranking is the last step. [How search scoring works](search-relevance-overview.md#diagram-of-ranking-algorithms) provides an illustration.
+You can use [semantic ranker](semantic-how-to-query-request.md) with scoring profiles and apply a [scoring profile after semantic ranking](semantic-how-to-enable-scoring-profiles.md). Otherwise, when multiple ranking or relevance features are in play, semantic ranking is the last step. [How search scoring works](search-relevance-overview.md#diagram-of-ranking-algorithms) provides an illustration.
 
 [Extra rules](#rules-for-using-functions) apply specifically to functions.
 
@@ -77,7 +77,7 @@ The following definition shows a simple profile named "geo". This example boosts
 To use this scoring profile, your query is formulated to specify `scoringProfile` parameter in the request. If you're using the REST API, queries are specified through GET and POST requests. In the following example, "currentLocation" has a delimiter of a single dash (`-`). It's followed by longitude and latitude coordinates, where longitude is a negative value.
 
 ```http
-POST /indexes/hotels/docs&api-version=2024-07-01
+POST /indexes/hotels/docs&api-version=2025-09-01
 {
     "search": "inn",
     "scoringProfile": "geo",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付とAPIバージョンの更新"
}
```

### Explanation
この変更は、'index-add-scoring-profiles.md' ドキュメントにおいて、日付情報と一部のAPIバージョンを更新することを目的としています。具体的には、ドキュメントの最終更新日を2025年7月25日から2025年9月29日に変更し、APIバージョンを2024-07-01から2025-09-01に更新しました。これにより、ユーザーは最新の情報と仕様に基づいてスコアリングプロファイルを使用することができます。また、文書内容内の一部の表現も修正されており、特に「semantic search (reranking)」が「semantic reranking」と表記されることで、用語の一貫性が向上しています。このような修正は、ユーザーに対して最新かつ正確な情報を提供するために不可欠です。全体として、この小規模な更新は、ドキュメントの整合性を改善し、Azureのスコアリングプロファイル機能の利用を促進することに寄与します。

## articles/search/index-add-suggesters.md{#item-28ed57}

<details>
<summary>Diff</summary>
````diff
@@ -161,7 +161,7 @@ In a search application, client code should use a library like [jQuery UI Autoco
 API usage is illustrated in the following call to the Autocomplete REST API. There are two takeaways from this example. First, as with all queries, the operation is against the documents collection of an index and the query includes a `search` parameter, which in this case provides the partial query. Second, you must add `suggesterName` to the request. If a suggester isn't defined in the index, calls to autocomplete or suggestions fail.
 
 ```http
-POST /indexes/myxboxgames/docs/autocomplete?search&api-version=2024-07-01
+POST /indexes/myxboxgames/docs/autocomplete?search&api-version=2025-09-01
 {
   "search": "minecraf",
   "suggesterName": "sg"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'index-add-suggesters.md' ドキュメント内で、Autocomplete REST APIのサンプル呼び出しに関するAPIバージョンを更新することを目的としています。具体的には、APIバージョンを2024-07-01から2025-09-01に変更しています。この更新により、ユーザーは最新のAPI機能を利用し、提案機能をより効果的に活用できるようになります。POSTリクエストの具体例も同様に更新されており、'suggesterName'パラメータについての説明が強調されています。全体として、この小規模な更新は、ドキュメントの正確性を向上させ、ユーザーが最新の情報に基づいて動作を実行できるように支援します。

## articles/search/index-ranking-similarity.md{#item-ba07fa}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ BM25 ranking provides two parameters for tuning the relevance score calculation.
 1. Use a [Create or Update Index](/rest/api/searchservice/indexes/create) request to set BM25 parameters:
 
     ```http
-    PUT [service-name].search.windows.net/indexes/[index-name]?api-version=2024-07-01&allowIndexDowntime=true
+    PUT [service-name].search.windows.net/indexes/[index-name]?api-version=2025-09-01&allowIndexDowntime=true
     {
         "similarity": {
             "@odata.type": "#Microsoft.Azure.Search.BM25Similarity",
@@ -84,7 +84,7 @@ The following links describe the Similarity property in the Azure SDKs.
 You can also use the [REST API](/rest/api/searchservice/indexes/create). The following example creates a new index with the "similarity" property set to BM25:
 
 ```http
-PUT [service-name].search.windows.net/indexes/[index name]?api-version=2024-07-01
+PUT [service-name].search.windows.net/indexes/[index name]?api-version=2025-09-01
 {
     "name": "indexName",
     "fields": [
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'index-ranking-similarity.md' ドキュメント内のBM25類似性に関するAPIバージョンを更新することを目的としています。具体的には、APIバージョンを2024-07-01から2025-09-01に変更しています。この更新により、ユーザーは最新のAPI仕様に基づいてBM25関連のパラメータを設定できるようになります。また、ドキュメント内の具体的なHTTP PUTリクエストの例も更新され、適切なAPIバージョンを参照するように変更されています。全体として、この小規模な更新は、ドキュメントの正確性を高め、ユーザーが最新の情報を元に操作を行えるようにサポートします。

## articles/search/index-similarity-and-scoring.md{#item-75603d}

<details>
<summary>Diff</summary>
````diff
@@ -97,7 +97,7 @@ By default, the score of a document is calculated based on statistical propertie
 If you prefer to compute the score based on the statistical properties across all shards, you can do so by adding `scoringStatistics=global` as a [query parameter](/rest/api/searchservice/documents/search-post) (or add `"scoringStatistics": "global"` as a body parameter of the [query request](/rest/api/searchservice/documents/search-post)).
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels/docs/search?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexes/hotels/docs/search?api-version=2025-09-01
 {
     "search": "<query string>",
     "scoringStatistics": "global"
@@ -107,7 +107,7 @@ POST https://[service name].search.windows.net/indexes/hotels/docs/search?api-ve
 Using `scoringStatistics` will ensure that all shards in the same replica provide the same results. That said, different replicas can be slightly different from one another as they're always getting updated with the latest changes to your index. In some scenarios, you might want your users to get more consistent results during a "query session". In such scenarios, you can provide a `sessionId` as part of your queries. The `sessionId` is a unique string that you create to refer to a unique user session.
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels/docs/search?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexes/hotels/docs/search?api-version=2025-09-01
 {
     "search": "<query string>",
     "sessionId": "<string>"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'index-similarity-and-scoring.md' ドキュメントでのスコア計算に関するAPIバージョンを更新することを目的としています。具体的には、検索APIのバージョンを2024-07-01から2025-09-01に変更しています。この更新により、ユーザーは最新のAPI機能にアクセスでき、特に`scoringStatistics`および`sessionId`パラメータを使用した検索リクエストを適切に実行できるようになります。ドキュメント内の具体的なHTTP POSTリクエストの例も更新され、適切なAPIバージョンを指し示すようになっています。この小規模な更新は、ドキュメントの正確性を向上させ、ユーザーが最新情報を元に迅速に対応できることを助けます。

## articles/search/knowledge-store-create-rest.md{#item-2643dd}

<details>
<summary>Diff</summary>
````diff
@@ -92,7 +92,7 @@ A valid API key establishes trust, on a per request basis, between the applicati
 
     ```http
     ### Create a new index
-    POST {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
         Content-Type: application/json
         api-key: {{apiKey}}
     
@@ -124,7 +124,7 @@ A valid API key establishes trust, on a per request basis, between the applicati
 
     ```http
     ### Create a data source
-    POST {{baseUrl}}/datasources?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/datasources?api-version=2025-09-01  HTTP/1.1
       Content-Type: application/json
       api-key: {{apiKey}}
     
@@ -155,7 +155,7 @@ A skillset defines enrichments (skills) and your knowledge store. [Create Skills
 
     ```http
     ### Create a skillset
-    POST {{baseUrl}}/skillsets?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/skillsets?api-version=2025-09-01  HTTP/1.1
         Content-Type: application/json
         api-key: {{apiKey}}
     
@@ -322,7 +322,7 @@ A skillset defines enrichments (skills) and your knowledge store. [Create Skills
 
     ```http
     ### Create indexer
-    POST {{baseUrl}}/indexers?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexers?api-version=2025-09-01  HTTP/1.1
         Content-Type: application/json
         api-key: {{apiKey}}
     
@@ -370,7 +370,7 @@ After you send each request, the search service should respond with a 201 succes
 
 ```http
 ### Get Indexer Status (wait several minutes for the indexer to complete)
-GET {{baseUrl}}/indexers/hotel-reviews-kstore-idxr/status?api-version=2024-07-01  HTTP/1.1
+GET {{baseUrl}}/indexers/hotel-reviews-kstore-idxr/status?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
 ```
@@ -379,7 +379,7 @@ After several minutes, you can query the index to inspect the content. Even if y
 
 ```http
 ### Query the index (indexer status must be "success" before querying the index)
-POST {{baseUrl}}/indexes/hotel-reviews-kstore-idxr/docs/search?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexes/hotel-reviews-kstore-idxr/docs/search?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
   
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'knowledge-store-create-rest.md' ドキュメント内の複数のAPIリクエストにおいて、APIバージョンを更新することを目的としています。具体的には、すべてのHTTP POSTおよびGETリクエストにて、APIバージョンを2024-07-01から2025-09-01に変更しています。この更新により、ユーザーは最新のAPI機能にアクセスでき、データソース、インデックス、スキルセット、インデクサーを作成する際の正確なリクエストを使用できるようになります。ドキュメント中のリクエスト例が適切に更新されており、これによりユーザーは最新の仕様に基づいて操作を行うことができるようになります。この小規模な更新は、ドキュメントの正確性を向上させ、開発者が新しいAPIバージョンに基づいた作業を行うためのサポートを提供します。

## articles/search/monitor-azure-cognitive-search-data-reference.md{#item-561425}

<details>
<summary>Diff</summary>
````diff
@@ -160,7 +160,7 @@ The following example illustrates a resource log that includes common properties
 | Resource | String | Resource ID. For example: `/subscriptions/<your-subscription-id>/resourceGroups/<your-resource-group-name>/providers/Microsoft.Search/searchServices/<your-search-service-name>` |
 | Category | String | "OperationLogs". This value is a constant. OperationLogs is the only category used for resource logs. |
 | OperationName | String |  The name of the operation (see the [full list of operations](#resource-log-search-ops)). An example is `Query.Search` |
-| OperationVersion | String | The api-version used on the request. For example: `2024-07-01` |
+| OperationVersion | String | The api-version used on the request. For example: `2025-09-01` |
 | ResultType | String |"Success". Other possible values: Success or Failure |
 | ResultSignature | Int | An HTTP result code. For example: `200` |
 | DurationMS | Int | Duration of the operation in milliseconds. |
@@ -177,7 +177,7 @@ The following properties are specific to Azure AI Search.
 | Description_s | String | The operation's endpoint. For example: `GET /indexes('content')/docs` |
 | Documents_d | Int | Number of documents processed. |
 | IndexName_s | String | Name of the index associated with the operation. |
-| Query_s | String | The query parameters used in the request. For example: `?search=beach access&$count=true&api-version=2024-07-01` |
+| Query_s | String | The query parameters used in the request. For example: `?search=beach access&$count=true&api-version=2025-09-01` |
 
 <a name="resource-log-search-ops"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'monitor-azure-cognitive-search-data-reference.md' ドキュメント内のリソースログに関する詳細において、APIバージョンを更新することを目的としています。具体的には、`OperationVersion` および `Query_s` のフィールドにおけるAPIバージョンの例を2024-07-01から2025-09-01に変更しています。この更新により、ユーザーは最新のAPIバージョンを参照し、リソースログの構造をより正確に理解できるようになります。ドキュメントの正確性と関連性が向上し、開発者が最新の仕様に基づいて運用を行う際に役立ちます。この小規模な更新は、情報の整合性を保つための重要なステップです。

## articles/search/query-lucene-syntax.md{#item-736436}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ To use full Lucene syntax, set the queryType to `full` and pass in a query expre
 The following example is a search request constructed using the full syntax. This particular example shows in-field search and term boosting. It looks for hotels where the category field contains the term `budget`. Any documents containing the phrase `"recently renovated"` are ranked higher as a result of the term boost value (3).  
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 {
   "queryType": "full",
   "search": "category:budget AND \"recently renovated\"^3",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'query-lucene-syntax.md' ドキュメント内のHTTPリクエスト例において、APIバージョンを更新することを目的としています。具体的には、検索リクエストの例において、APIバージョンを2024-07-01から2025-09-01に変更しています。この更新により、ユーザーは最新のAPI仕様を反映した正確なリクエスト形式を参照でき、Lucene構文を使用した検索を適切に実行できるようになります。ドキュメントのこれらの変更は、利用者がスムーズに最新の機能を活用できるようにするためのものであり、機能の整合性を確保するための重要な手順となります。

## articles/search/query-simple-syntax.md{#item-ab3c96}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ Although the simple parser is based on the [Apache Lucene Simple Query Parser](h
 This example shows a simple query, distinguished by `"queryType": "simple"` and valid syntax. Although query type is set below, it's the default and can be omitted unless you're reverting from an alternative type. The following example is a search over independent terms, with a requirement that all matching documents include "pool".
 
 ```http
-POST https://{{service-name}}.search.windows.net/indexes/hotel-rooms-sample/docs/search?api-version=2024-07-01
+POST https://{{service-name}}.search.windows.net/indexes/hotel-rooms-sample/docs/search?api-version=2025-09-01
 {
   "queryType": "simple",
   "search": "budget hotel +pool",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'query-simple-syntax.md' ドキュメントにおけるHTTPリクエストの例に関するもので、APIバージョンを更新しています。具体的には、検索リクエストのURLに含まれるAPIバージョンを2024-07-01から2025-09-01に変更しました。この更新により、ユーザーは最新のAPI仕様に基づいた正確なリクエストを参照でき、シンプルなクエリを実行する際に必要な最新の情報を得ることができます。ドキュメントのこの小規模な更新は、利用者が機能を正常に利用できるようにするための重要なステップであり、情報の整合性を保つ助けとなります。

## articles/search/search-add-autocomplete-suggestions.md{#item-0a43e0}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ The remainder of this article is focused on queries and client code. It uses Jav
 Elements of a request include one of the search-as-you-type APIs, a partial query, and a suggester. The following script illustrates components of a request, using the Autocomplete REST API as an example.
 
 ```http
-POST /indexes/myxboxgames/docs/autocomplete?search&api-version=2024-07-01
+POST /indexes/myxboxgames/docs/autocomplete?search&api-version=2025-09-01
 {
   "search": "minecraf",
   "suggesterName": "sg"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-add-autocomplete-suggestions.md' ドキュメント内のHTTPリクエストの例に関するもので、APIバージョンを更新しています。具体的には、Autocomplete REST APIにおけるリクエストのURLに含まれるAPIバージョンを2024-07-01から2025-09-01に変更しました。この更新により、ユーザーは最新のAPIの仕様に基づく正確なリクエストを参照することができ、オートコンプリート機能を適切に利用するために必要な情報が提供されます。この小規模な更新は、利用者が機能を活用する際の正確性を高め、ドキュメントの整合性を保つために重要です。

## articles/search/search-blob-storage-integration.md{#item-bbdaa6}

<details>
<summary>Diff</summary>
````diff
@@ -98,7 +98,7 @@ You can control which blobs are indexed, and which are skipped, by the blob's fi
 Include specific file extensions by setting `"indexedFileNameExtensions"` to a comma-separated list of file extensions (with a leading dot). Exclude specific file extensions by setting `"excludedFileNameExtensions"` to the extensions that should be skipped. If the same extension is in both lists, it's excluded from indexing.
 
 ```http
-PUT /indexers/[indexer name]?api-version=2024-07-01
+PUT /indexers/[indexer name]?api-version=2025-09-01
 {
     "parameters" : { 
         "configuration" : { 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-blob-storage-integration.md' ドキュメントにおけるHTTPリクエストの例に関するもので、APIバージョンを更新しています。具体的には、Blobインデクサーの設定に関連するPUTリクエストのURLに含まれるAPIバージョンを2024-07-01から2025-09-01に変更しました。この更新により、ユーザーは最新のAPI仕様に基づいた正確なリクエストを参照でき、Blobストレージをインデックスする際に必要な情報が得られます。この小規模な更新は、ユーザーが機能を正しく利用できるようにするための重要な調整であり、ドキュメントの明確さを向上させる役割も果たします。

## articles/search/search-faq-frequently-asked-questions.yml{#item-eab2ba}

<details>
<summary>Diff</summary>
````diff
@@ -158,7 +158,7 @@ sections:
           
           * Add a "vectorSearch" section to the index schema specifying the configuration used by vector search fields, including the parameters of the Approximate Nearest Neighbor algorithm used, like HNSW.
           
-          * Use the latest stable version, [**2024-07-01**](/rest/api/searchservice), or an Azure SDK to create or update the index, load documents, and issue queries. For more information, see [Create a vector index](vector-search-how-to-create-index.md).
+          * Use the latest stable version, [**2025-09-01**](/rest/api/searchservice), or an Azure SDK to create or update the index, load documents, and issue queries. For more information, see [Create a vector index](vector-search-how-to-create-index.md).
 
   - name: Queries
     questions:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-faq-frequently-asked-questions.yml' ファイル内にあるFAQに関する記述の一部を修正しています。具体的には、ベクトル検索のインデックスを作成または更新する際に使用される最新のAPIバージョンを2024-07-01から2025-09-01に更新しました。この更新により、ユーザーは最新の安定版APIを参照して正しい手順でインデックスを作成し、ドキュメントをロードし、クエリを発行することができるようになります。この小さな変更は、ユーザーが最新の情報にアクセスでき、ドキュメントの信頼性を高めるために重要です。

## articles/search/search-file-storage-integration.md{#item-d20e26}

<details>
<summary>Diff</summary>
````diff
@@ -109,7 +109,7 @@ In the [search index](search-what-is-an-index.md), add fields to accept the cont
 1. [Create or update an index](/rest/api/searchservice/indexes/create-or-update) to define search fields that will store file content and metadata.
 
     ```http
-    POST /indexes?api-version=2024-07-01
+    POST /indexes?api-version=2025-09-01
     {
       "name" : "my-search-index",
       "fields": [
@@ -150,7 +150,7 @@ Once the index and data source have been created, you're ready to create the ind
 1. [Create or update an indexer](/rest/api/searchservice/indexers/create-or-update) by giving it a name and referencing the data source and target index:
 
     ```http
-    POST /indexers?api-version=2024-07-01
+    POST /indexers?api-version=2025-09-01
     {
       "name" : "my-file-indexer",
       "dataSourceName" : "my-file-datasource",
@@ -186,7 +186,7 @@ An indexer runs automatically when it's created. You can prevent this by setting
 To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) request:
 
 ```http
-GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2024-07-01
+GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2025-09-01
   Content-Type: application/json  
   api-key: [admin key]
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-file-storage-integration.md' ドキュメントにおけるAPIリクエストの例を修正するもので、特にインデックスとインデクサーの作成に関するAPIバージョンを2024-07-01から2025-09-01に更新しています。具体的には、インデックスを作成するためのPOSTリクエストやインデクサーの作成、インデクサーのステータスを取得するためのGETリクエストに対して新しいAPIバージョンが適用されています。この更新は、ユーザーが最新のAPI機能を利用するために必要な情報を正確に反映し、ドキュメントの信頼性を向上させる役割を果たします。

## articles/search/search-filters.md{#item-3f2a7a}

<details>
<summary>Diff</summary>
````diff
@@ -57,7 +57,7 @@ One of the limits on a filter expression is the maximum size limit of the reques
 The following examples represent prototypical filter definitions in several APIs.
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels/docs/search?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexes/hotels/docs/search?api-version=2025-09-01
 {
     "search": "*",
     "filter": "Rooms/any(room: room/BaseRate lt 150.0)",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-filters.md' ドキュメント内におけるAPIリクエストの例の修正です。具体的には、ホテルのインデックスに対する検索リクエストのAPIバージョンを2024-07-01から2025-09-01に更新しました。この更新は、最新のAPIの使用を促進し、ユーザーが正しいバージョンのAPIを使用してフィルタリング機能を活用できるようにするために重要です。ドキュメントの内容が最新の状態に保たれることで、利用者は正確かつ効率的に情報を取得することが可能となります。

## articles/search/search-how-to-define-index-projections.md{#item-a7e2c5}

<details>
<summary>Diff</summary>
````diff
@@ -149,7 +149,7 @@ Choose a tab for the various API syntax. There's currently no portal support for
 
 Index projections are generally available. We recommend the most recent stable API:
 
-- [Create Skillset (api-version=2024-07-01)](/rest/api/searchservice/skillsets/create)
+- [Create Skillset (api-version=2025-09-01)](/rest/api/searchservice/skillsets/create)
 
 Here's an example payload for an index projections definition that you might use to project individual pages output by the [Text Split skill](cognitive-search-skill-textsplit.md) as their own documents in the search index.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-how-to-define-index-projections.md' ドキュメントにおけるAPIリクエスト例の修正です。具体的には、スキルセットを作成するためのAPIバージョンを2024-07-01から2025-09-01に更新しました。この更新は、最新の安定版APIを使用することを推奨するものであり、ユーザーが新しい機能や改善された動作を活用できるようにするために重要です。ドキュメントの内容を最新のAPIバージョンに整えることで、利用者は正確かつ適切な情報をもとに操作を行うことができます。

## articles/search/search-how-to-index-csv-blobs.md{#item-2c3f3e}

<details>
<summary>Diff</summary>
````diff
@@ -73,7 +73,7 @@ Putting it all together, here are the complete payload examples.
 Datasource: 
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
+POST https://[service name].search.windows.net/datasources?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 {
@@ -87,7 +87,7 @@ api-key: [admin key]
 Indexer:
 
 ```http
-POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexers?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-how-to-index-csv-blobs.md' ドキュメントにおけるAPIリクエストの例の修正です。具体的には、データソースとインデクサーの作成を行うためのAPIバージョンを2024-07-01から2025-09-01に更新しました。この変更により、最新のAPIバージョンを使用することが推奨され、ユーザーが新しい機能や改善を利用できるようになります。これにより、ドキュメントは常に最新の情報に基づいており、ユーザーは正確で効果的な操作を行うことができます。

## articles/search/search-how-to-index-sql-database.md{#item-86d873}

<details>
<summary>Diff</summary>
````diff
@@ -159,7 +159,7 @@ The data source definition specifies the data to index, credentials, and policie
 1. [Create Data Source](/rest/api/searchservice/data-sources/create) or [Create or Update Data Source](/rest/api/searchservice/data-sources/create-or-update) to set its definition: 
 
    ```http
-    POST https://myservice.search.windows.net/datasources?api-version=2024-07-01
+    POST https://myservice.search.windows.net/datasources?api-version=2025-09-01
     Content-Type: application/json
     api-key: admin-key
 
@@ -201,7 +201,7 @@ In a [search index](search-what-is-an-index.md), add fields that correspond to t
 1. [Create or update an index](/rest/api/searchservice/indexes/create) to define search fields that store data:
 
     ```http
-    POST https://[service name].search.windows.net/indexes?api-version=2024-07-01
+    POST https://[service name].search.windows.net/indexes?api-version=2025-09-01
     Content-Type: application/json
     api-key: [Search service admin key]
     {
@@ -254,7 +254,7 @@ Once the index and data source have been created, you're ready to create the ind
 1. [Create or update an indexer](/rest/api/searchservice/indexers/create) by giving it a name and referencing the data source and target index:
 
     ```http
-    POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
+    POST https://[service name].search.windows.net/indexers?api-version=2025-09-01
     Content-Type: application/json
     api-key: [search service admin key]
     {
@@ -310,7 +310,7 @@ To monitor the indexer status and execution history, check the indexer execution
 ### [**REST**](#tab/rest-check-indexer)
 
 ```http
-GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2024-07-01
+GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2025-09-01
   Content-Type: application/json  
   api-key: [admin key]
 ```
@@ -384,7 +384,7 @@ Database requirements:
 Change detection policies are added to data source definitions. To use this policy, edit the data source definition in the Azure portal, or use REST to update your data source like this:
 
 ```http
-POST https://myservice.search.windows.net/datasources?api-version=2024-07-01
+POST https://myservice.search.windows.net/datasources?api-version=2025-09-01
 Content-Type: application/json
 api-key: admin-key
     {
@@ -422,7 +422,7 @@ The high water mark column must meet the following requirements:
 Change detection policies are added to data source definitions. To use this policy, create or update your data source like this:
 
 ```http
-POST https://myservice.search.windows.net/datasources?api-version=2024-07-01
+POST https://myservice.search.windows.net/datasources?api-version=2025-09-01
 Content-Type: application/json
 api-key: admin-key
     {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-how-to-index-sql-database.md' ドキュメント内のAPIリクエストのバージョンを更新する内容です。具体的には、データソース、インデックス、インデクサーの各作成に関するAPIバージョンを2024-07-01から2025-09-01に変更しています。この更新により、ユーザーは最新のAPIによる機能や改善を活用できるようになります。APIバージョンの明確な更新は、正しい動作を確保し、ドキュメントの一貫性を保つために重要です。これにより、利用者はより適切な情報を基に操作を行うことが可能になります。

## articles/search/search-how-to-integrated-vectorization.md{#item-86fb1e}

<details>
<summary>Diff</summary>
````diff
@@ -332,7 +332,7 @@ In this section, you specify the connection information for your Azure AI Search
 
    ```HTTP
    ### List existing indexes by name
-   GET {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
+   GET {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
      Content-Type: application/json
      Authorization: Bearer {{token}}
    ```
@@ -379,7 +379,7 @@ In this section, you connect to a [supported data source](#supported-data-source
 
    ```HTTP
    ### Create a data source
-   POST {{baseUrl}}/datasources?api-version=2024-07-01  HTTP/1.1
+   POST {{baseUrl}}/datasources?api-version=2025-09-01  HTTP/1.1
      Content-Type: application/json
      Authorization: Bearer {{token}}
 
@@ -454,7 +454,7 @@ For built-in data chunking, Azure AI Search offers the [Text Split skill](cognit
 
    ```HTTP
    ### Create a skillset
-   POST {{baseUrl}}/skillsets?api-version=2024-07-01  HTTP/1.1
+   POST {{baseUrl}}/skillsets?api-version=2025-09-01  HTTP/1.1
      Content-Type: application/json
      Authorization: Bearer {{token}}
 
@@ -632,7 +632,7 @@ In addition to vector fields, the sample index in the following steps contains n
 
    ```HTTP
    ### Create a vector index
-   POST {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
+   POST {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
      Content-Type: application/json
      Authorization: Bearer {{token}}
 
@@ -810,7 +810,7 @@ In this section, you create an [indexer](search-indexer-overview.md) to drive th
 
    ```HTTP
    ### Create an indexer
-   POST {{baseUrl}}/indexers?api-version=2024-07-01  HTTP/1.1
+   POST {{baseUrl}}/indexers?api-version=2025-09-01  HTTP/1.1
      Content-Type: application/json
      Authorization: Bearer {{token}}
 
@@ -847,7 +847,7 @@ In this section, you verify that your content was successfully indexed by [creat
 
    ```HTTP
    ### Run a vector query
-   POST {{baseUrl}}/indexes('my-vector-index')/docs/search.post.search?api-version=2024-07-01  HTTP/1.1
+   POST {{baseUrl}}/indexes('my-vector-index')/docs/search.post.search?api-version=2025-09-01  HTTP/1.1
      Content-Type: application/json
      Authorization: Bearer {{token}}
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-how-to-integrated-vectorization.md' ドキュメントにおける複数のAPIリクエストのバージョンを更新したものです。具体的には、データソースやインデックス、インデクサーの作成を含むリクエストにおいて、APIバージョンを2024-07-01から2025-09-01に変更しています。このアップデートにより、ユーザーは最新のAPI機能を利用することができ、性能や新機能の恩恵を受けることができます。また、これによりドキュメントは最新の状態を保ち、ユーザーが正確で信頼性のある情報に基づいて操作を行えるようになります。

## articles/search/search-how-to-load-search-index.md{#item-a72573}

<details>
<summary>Diff</summary>
````diff
@@ -57,7 +57,7 @@ In the Azure portal, use an [import wizard](search-import-data-portal.md) to cre
 1. Formulate a POST call specifying the index name, the "docs/index" endpoint, and a request body that includes the `@search.action` parameter.
 
     ```http
-    POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/index?api-version=2024-07-01
+    POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/index?api-version=2025-09-01
     Content-Type: application/json   
     api-key: [admin key] 
     {
@@ -95,7 +95,7 @@ In the Azure portal, use an [import wizard](search-import-data-portal.md) to cre
 1. [Look up the documents](/rest/api/searchservice/documents/get) you just added as a validation step:
 
     ```http
-    GET https://[service name].search.windows.net/indexes/hotel-sample-index/docs/1111?api-version=2024-07-01
+    GET https://[service name].search.windows.net/indexes/hotel-sample-index/docs/1111?api-version=2025-09-01
     ```
 
 When the document key or ID is new, **null** becomes the value for any field that is unspecified in the document. For actions on an existing document, updated values replace the previous values. Any fields that weren't specified in a "merge" or "mergeUpload" are left intact in the search index.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-how-to-load-search-index.md' ドキュメント内でのAPIリクエストのバージョンを更新するものです。具体的には、データをインデックスにロードするためのPOST呼び出しと、追加した文書を確認するためのGET呼び出しのAPIバージョンを2024-07-01から2025-09-01に変更しています。この更新は、最新の機能や改善を利用するために重要であり、ユーザーが最新のAPI仕様を反映した操作を行えるようにする役割を果たします。この修正により、ユーザーは正しい情報に基づいてインデックスのロードや文書の検索を実行することが可能になります。

## articles/search/search-howto-index-azure-data-lake-storage.md{#item-c21e43}

<details>
<summary>Diff</summary>
````diff
@@ -232,7 +232,7 @@ An indexer runs automatically when it's created. You can prevent this by setting
 To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) request:
 
 ```http
-GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2024-07-01
+GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2025-09-01
   Content-Type: application/json  
   api-key: [admin key]
 ```
@@ -284,7 +284,7 @@ By default, the blob indexer stops as soon as it encounters a blob with an unsup
 There are five indexer properties that control the indexer's response when errors occur. 
 
 ```http
-PUT /indexers/[indexer name]?api-version=2024-07-01
+PUT /indexers/[indexer name]?api-version=2025-09-01
 {
   "parameters" : { 
     "maxFailedItems" : 10, 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-howto-index-azure-data-lake-storage.md' ドキュメントにおけるAPIバージョンを更新するものです。具体的には、インデクサーのステータスを取得するためのGETリクエストと、インデクサーのプロパティを更新するためのPUTリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。この更新により、ユーザーは最新のAPI機能を利用できるようになり、より安定したインデクサーの管理を促進します。また、これによってドキュメントが最新の仕様に即した内容となり、ユーザーが正しい手順に従って操作を行うことが可能になります。

## articles/search/search-howto-index-changed-deleted-blobs.md{#item-32a688}

<details>
<summary>Diff</summary>
````diff
@@ -78,7 +78,7 @@ In Azure AI Search, set a native blob soft deletion detection policy on the data
 Set the soft deletion detection policy in the data source definition. Specify the API version when creating or updating the data source.
 
 ```http
-PUT https://[service name].search.windows.net/datasources/blob-datasource?api-version=2024-07-01
+PUT https://[service name].search.windows.net/datasources/blob-datasource?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 {
@@ -117,7 +117,7 @@ There are steps to follow in both Azure Storage and Azure AI Search, but there a
 1. In Azure AI Search, edit the data source definition to include a "dataDeletionDetectionPolicy" property. For example, the following policy considers a file to be deleted if it has a metadata property `IsDeleted` with the value `true`:
 
     ```http
-    PUT https://[service name].search.windows.net/datasources/file-datasource?api-version=2024-07-01
+    PUT https://[service name].search.windows.net/datasources/file-datasource?api-version=2025-09-01
     {
         "name" : "file-datasource",
         "type" : "azurefile",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-howto-index-changed-deleted-blobs.md' ドキュメントにおけるAPIバージョンを更新するものです。具体的には、データソースを作成または更新する際に使用されるPUTリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。この更新により、ユーザーは最新の機能や改善にアクセスできるようになり、ソフト削除検出ポリシーを正しく設定するための手順が最新の仕様に即して情報が提供されます。また、これによりユーザーは正確な操作方法に基づいてデータソースの定義を修正することができます。

## articles/search/search-howto-index-cosmosdb.md{#item-568fab}

<details>
<summary>Diff</summary>
````diff
@@ -104,7 +104,7 @@ The data source definition specifies the data to index, credentials, and policie
 1. [Create or update a data source](/rest/api/searchservice/data-sources/create-or-update) to set its definition: 
 
     ```http
-    POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
+    POST https://[service name].search.windows.net/datasources?api-version=2025-09-01
     Content-Type: application/json
     api-key: [Search service admin key]
     {
@@ -234,7 +234,7 @@ In a [search index](search-what-is-an-index.md), add fields to accept the source
 1. [Create or update an index](/rest/api/searchservice/indexes/create) to define search fields that store data:
 
     ```http
-    POST https://[service name].search.windows.net/indexes?api-version=2024-07-01
+    POST https://[service name].search.windows.net/indexes?api-version=2025-09-01
     Content-Type: application/json
     api-key: [Search service admin key]
     {
@@ -282,7 +282,7 @@ Once the index and data source have been created, you're ready to create the ind
 1. [Create or update an indexer](/rest/api/searchservice/indexers/create) by giving it a name and referencing the data source and target index:
 
     ```http
-    POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
+    POST https://[service name].search.windows.net/indexers?api-version=2025-09-01
     Content-Type: application/json
     api-key: [search service admin key]
     {
@@ -323,7 +323,7 @@ To monitor the indexer status and execution history, check the indexer execution
 
 ### [**REST**](#tab/rest-check-indexer)
 ```http
-GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2024-07-01
+GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2025-09-01
   Content-Type: application/json  
   api-key: [admin key]
 ```
@@ -427,7 +427,7 @@ The `softDeleteColumnName` must be a top-level field in the index. Using nested
 The following example creates a data source with a soft-deletion policy:
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
+POST https://[service name].search.windows.net/datasources?api-version=2025-09-01
 Content-Type: application/json
 api-key: [Search service admin key]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-howto-index-cosmosdb.md' ドキュメントにおけるAPIバージョンを更新するものです。具体的には、データソース、インデックス、およびインデクサーを作成または更新するために使用されるPOSTリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。また、インデクサーのステータスを取得するGETリクエストのAPIバージョンも同様に更新されています。この変更は、ユーザーが最新のAPI機能を活用できるようにし、適切な操作手順を反映させることで、Azure AI Searchの使用体験を向上させます。ドキュメントの内容が最新の仕様に準拠することで、ユーザーはより正確で効果的なデータインデクシングのプロセスを実現できるようになります。

## articles/search/search-howto-index-json-blobs.md{#item-b8230c}

<details>
<summary>Diff</summary>
````diff
@@ -61,7 +61,7 @@ The blob indexer parses the JSON document into a single search document, loading
 Although the default behavior is one search document per JSON blob, setting the **`json`** parsing mode changes the internal field mappings for content, promoting fields inside `content` to actual fields in the search index. An example indexer definition for the **`json`** parsing mode might look like this:
 
 ```http
-POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexers?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 
@@ -100,7 +100,7 @@ Alternatively, you can use the JSON array option. This option is useful when blo
 The `parameters` property on the indexer contains parsing mode values. For a JSON array, the indexer definition should look similar to the following example.
 
 ```http
-POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexers?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 
@@ -159,7 +159,7 @@ If your blob contains multiple JSON entities separated by a newline, and you wan
 For JSON lines, the indexer definition should look similar to the following example.
 
 ```http
-POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexers?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-howto-index-json-blobs.md' ドキュメントにおいて、Azure Searchのインデクサ定義に関するAPIバージョンを更新するものです。具体的には、JSON形式のデータをインデックスするために使用されるPOSTリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。この変更により、ユーザーは最新のAPI機能を利用でき、インデクサの定義に関する情報が新しい仕様に合わせて更新されるため、より正確な設定が可能になります。これにより、ユーザーはJSONドキュメントを効果的にインデクスし、検索機能を強化することができるようになります。

## articles/search/search-howto-index-plaintext-blobs.md{#item-63efcb}

<details>
<summary>Diff</summary>
````diff
@@ -38,7 +38,7 @@ An alternative third option for breaking content into multiple parts requires ad
 To index plain text blobs, create or update an indexer definition with the `parsingMode` configuration property set to `text` on a [Create Indexer](/rest/api/searchservice/indexers/create) request:
 
 ```http
-PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2024-07-01
+PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 
@@ -62,7 +62,7 @@ By default, the `UTF-8` encoding is assumed. To specify a different encoding, us
 Parsing modes are specified in the indexer definition.
 
 ```http
-POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexers?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-howto-index-plaintext-blobs.md' ドキュメントにおけるインデクサ定義のAPIバージョンを更新するものです。具体的には、プレーンテキストのBlobをインデックスするために利用されるPUTおよびPOSTリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。この更新により、ユーザーは最新のインデクサ設定を使用して、テキストのパーシングモードを適切に指定できるようになります。これにより、Azureの検索サービスを利用する際、よりスムーズで効果的なインデクシングプロセスを実現し、インデクサの設定設定が現在の仕様に従う形で最新に保たれます。

## articles/search/search-howto-indexing-azure-blob-storage.md{#item-dc4668}

<details>
<summary>Diff</summary>
````diff
@@ -178,7 +178,7 @@ In a [search index](search-what-is-an-index.md), add fields to accept the conten
 1. [Create or update an index](/rest/api/searchservice/indexes/create-or-update) to define search fields that will store blob content and metadata:
 
     ```http
-    POST https://[service name].search.windows.net/indexes?api-version=2024-07-01
+    POST https://[service name].search.windows.net/indexes?api-version=2025-09-01
     {
         "name" : "my-search-index",
         "fields": [
@@ -214,7 +214,7 @@ Once the index and data source have been created, you're ready to create the ind
 1. [Create or update an indexer](/rest/api/searchservice/indexers/create-or-update) by giving it a name and referencing the data source and target index:
 
     ```http
-    POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
+    POST https://[service name].search.windows.net/indexers?api-version=2025-09-01
     {
       "name" : "my-blob-indexer",
       "dataSourceName" : "my-blob-datasource",
@@ -271,7 +271,7 @@ To illustrate, let's consider an example of two indexers, pulling data from two
 First indexer definition example:
 
 ```http
-POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexers?api-version=2025-09-01
 {
   "name" : "my-blob-indexer1",
   "dataSourceName" : "my-blob-datasource1",
@@ -294,7 +294,7 @@ POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
 Second indexer definition that runs in parallel example:
 
 ```http
-POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexers?api-version=2025-09-01
 {
   "name" : "my-blob-indexer2",
   "dataSourceName" : "my-blob-datasource2",
@@ -320,7 +320,7 @@ POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
 To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) request:
 
 ```http
-GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2024-07-01
+GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2025-09-01
   Content-Type: application/json  
   api-key: [admin key]
 ```
@@ -372,7 +372,7 @@ By default, the blob indexer stops as soon as it encounters a blob with an unsup
 There are five indexer properties that control the indexer's response when errors occur. 
 
 ```http
-PUT /indexers/[indexer name]?api-version=2024-07-01
+PUT /indexers/[indexer name]?api-version=2025-09-01
 {
   "parameters" : { 
     "maxFailedItems" : 10, 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-howto-indexing-azure-blob-storage.md' ドキュメントにおいて、Azure Blob Storageのインデクシングに関連するAPIバージョンを更新するものです。具体的には、新しいインデクサやインデックスを作成するために用いるPOSTリクエストや、インデクサのステータスを取得するためのGETリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。この更新により、ユーザーは最新の機能や仕様を活用でき、Blobストレージからのデータインデクシングがよりスムーズになります。これは、検索インデックスを効率的に管理し、最新のAPIの特性を活かすために重要な修正です。

## articles/search/search-howto-indexing-azure-tables.md{#item-7655b0}

<details>
<summary>Diff</summary>
````diff
@@ -89,7 +89,7 @@ The data source definition specifies the source data to index, credentials, and
 1. [Create or update a data source](/rest/api/searchservice/data-sources/create-or-update) to set its definition:
 
    ```http
-    POST https://[service name].search.windows.net/datasources?api-version=2024-07-01 
+    POST https://[service name].search.windows.net/datasources?api-version=2025-09-01 
     {
         "name": "my-table-storage-ds",
         "description": null,
@@ -175,7 +175,7 @@ In a [search index](search-what-is-an-index.md), add fields to accept the conten
 1. [Create or update an index](/rest/api/searchservice/indexes/create) to define search fields that will store content from entities:
 
     ```http
-    POST https://[service name].search.windows.net/indexes?api-version=2024-07-01 
+    POST https://[service name].search.windows.net/indexes?api-version=2025-09-01 
     {
       "name" : "my-search-index",
       "fields": [
@@ -215,7 +215,7 @@ Once you have an index and data source, you're ready to create the indexer. Inde
 1. [Create or update an indexer](/rest/api/searchservice/indexers/create) by giving it a name and referencing the data source and target index:
 
     ```http
-    POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
+    POST https://[service name].search.windows.net/indexers?api-version=2025-09-01
     {
         "name" : "my-table-indexer",
         "dataSourceName" : "my-table-storage-ds",
@@ -264,7 +264,7 @@ To monitor the indexer status and execution history, check the indexer execution
 ### [**REST**](#tab/rest-check-indexer)
 
 ```http
-GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2024-07-01
+GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2025-09-01
   Content-Type: application/json  
   api-key: [admin key]
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-howto-indexing-azure-tables.md' ドキュメントにおいて、Azure Tablesのインデクシングに関連するAPIバージョンを更新するものです。具体的には、データソースの作成やインデックス、インデクサの作成に用いるPOSTリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。また、インデクサのステータスを確認するためのGETリクエストのAPIバージョンも同様に更新されています。この修正により、ユーザーは最新のAPI仕様に基づいて、Azure Tablesとのインデクシングのプロセスをより効果的に行うことができるようになります。これにより、安定性や機能向上が期待される重要な更新です。

## articles/search/search-howto-managed-identities-cosmos-db.md{#item-a74464}

<details>
<summary>Diff</summary>
````diff
@@ -105,7 +105,7 @@ When you're connecting with a system-assigned managed identity, the only change
 Here's an example using the [Create Data Source](/rest/api/searchservice/data-sources/create) REST API that exercises the _modern_ approach.
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
+POST https://[service name].search.windows.net/datasources?api-version=2025-09-01
 {
     "name": "my-cosmosdb-ds",
     "type": "cosmosdb",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-howto-managed-identities-cosmos-db.md' ドキュメントにおいて、Cosmos DBとの接続に関するAPIバージョンを更新するものです。具体的には、データソースを作成するために使用されるPOSTリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。この修正により、ユーザーは最新のAPIの機能や改善点を利用して、Cosmos DBとの連携をより効率的に行うことができるようになります。このような小さな更新でも、ドキュメントの正確性を保ち、最新の技術トレンドに適合させるために重要です。

## articles/search/search-howto-managed-identities-sql.md{#item-2af8aa}

<details>
<summary>Diff</summary>
````diff
@@ -100,7 +100,7 @@ When you're connecting with a system-assigned managed identity, the only change
 Here's an example of how to create a data source to index data from a storage account using the [Create Data Source](/rest/api/searchservice/data-sources/create) REST API and a managed identity connection string. The managed identity connection string format is the same for the REST API, .NET SDK, and the Azure portal.
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
+POST https://[service name].search.windows.net/datasources?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 
@@ -154,7 +154,7 @@ The index specifies the fields in a document, attributes, and other constructs t
 Here's a [Create Index](/rest/api/searchservice/indexes/create) REST API call with a searchable `booktitle` field:   
 
 ```http
-POST https://[service name].search.windows.net/indexes?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexes?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 
@@ -174,7 +174,7 @@ An indexer connects a data source with a target search index, and provides a sch
 Here's a [Create Indexer](/rest/api/searchservice/indexers/create) REST API call with an Azure SQL indexer definition. The indexer runs when you submit the request.
 
 ```http
-POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexers?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-howto-managed-identities-sql.md' ドキュメントにおける、Azure SQL データベースとの接続に関連するAPIバージョンを更新するものです。具体的には、データソース、インデックス、およびインデクサを作成するために使用されるPOSTリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。この修正により、最新のAPI仕様に基づいて、ユーザーはAzure SQLとのインデクシングのプロセスをより適切に行えるようになります。こうした更新は、ドキュメントの整合性を維持し、新しい機能や改善点を利用できるようにするために重要です。

## articles/search/search-howto-managed-identities-storage.md{#item-8209c4}

<details>
<summary>Diff</summary>
````diff
@@ -74,7 +74,7 @@ For connections made using a system-assigned managed identity, the only change t
 Provide a connection string that contains a `ResourceId`, with no account key or password. The `ResourceId` must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name.
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
+POST https://[service name].search.windows.net/datasources?api-version=2025-09-01
 
 {
     "name" : "blob-datasource",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-howto-managed-identities-storage.md' ドキュメント内で、Azure Storage アカウントとの接続方法に関するAPIバージョンを更新するものです。具体的には、Storage データソースを作成するために使用されるPOSTリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。この修正により、ユーザーは最新のAPI機能を利用して、システム管理のマネージドアイデンティティを使用した接続設定を行うことができます。こうした小さな更新は、ドキュメントの正確性と最新性を維持するために重要な要素です。

## articles/search/search-howto-powerapps.md{#item-92d1c0}

<details>
<summary>Diff</summary>
````diff
@@ -74,7 +74,7 @@ A connector in Power Apps is a data source connection. In this step, create a cu
    * For the URL, enter a sample query for your search index (`search=*` returns all documents, `$select=` lets you choose fields). The API version is required. Fully specified, a URL might look like the following example. Notice that the `https://` prefix is omitted.
 
      ```http
-     mydemo.search.windows.net/indexes/hotels-sample-index/docs?search=*&$select=HotelName,Description,Address/City&api-version=2024-07-01
+     mydemo.search.windows.net/indexes/hotels-sample-index/docs?search=*&$select=HotelName,Description,Address/City&api-version=2025-09-01
      ```
 
    * For Headers, type `Content-Type application/json`.
@@ -95,7 +95,7 @@ A connector in Power Apps is a data source connection. In this step, create a cu
 
     :::image type="content" source="./media/search-howto-powerapps/1-10-4-parameter-metadata-select.png" alt-text="Select parameter metadata" border="true":::
 
-1. For *api-version*: Set `2024-07-01` as the **default value**, set **required** to *True*, and set **visibility** as *internal*.  
+1. For *api-version*: Set `2025-09-01` as the **default value**, set **required** to *True*, and set **visibility** as *internal*.  
 
     :::image type="content" source="./media/search-howto-powerapps/1-10-2-parameter-metadata-version.png" alt-text="Version parameter metadata" border="true":::
 
@@ -107,7 +107,7 @@ A connector in Power Apps is a data source connection. In this step, create a cu
     parameters:
       - {name: search, in: query, required: false, type: string, default: '*'}
       - {name: $select, in: query, required: false, type: string, default: 'HotelName,Description,Address/City'}
-      - {name: api-version, in: query, required: true, type: string, default: '2024-07-01',
+      - {name: api-version, in: query, required: true, type: string, default: '2025-09-01',
         x-ms-visibility: internal}
       - {name: Content-Type, in: header, required: false, type: string}
     ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-howto-powerapps.md' ドキュメントにおいて、Power Apps のコネクタに関連するAPIバージョンを更新するものです。具体的には、検索インデックスに対するクエリを実行するために必要なURLと、APIバージョンのデフォルト値が2024-07-01から2025-09-01に変更されています。この変更により、ユーザーは最新のAPIに基づいてコネクタを設定し、正確なデータ取得を行うことができるようになります。また、APIバージョンの更新は、サービスの利用に際して重要な要素であり、ドキュメントの整合性を保つために必要です。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -161,12 +161,12 @@ Here's a [REST API example](search-get-started-text.md) demonstrating these tips
 
 ```rest
 ### Get Stay-Kay City Hotel by ID
-GET  {{baseUrl}}/indexes/hotels-vector-quickstart/docs('1')?api-version=2024-07-01  HTTP/1.1
+GET  {{baseUrl}}/indexes/hotels-vector-quickstart/docs('1')?api-version=2025-09-01  HTTP/1.1
     Content-Type: application/json
     api-key: {{apiKey}}
 
 ### Change the description, city, and tags for Stay-Kay City Hotel
-POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search.index?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search.index?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
 
@@ -185,7 +185,7 @@ POST {{baseUrl}}/indexes/hotels-vector-quickstart/docs/search.index?api-version=
     }
        
 ### Retrieve the same document, confirm the overwrites and retention of all other values
-GET  {{baseUrl}}/indexes/hotels-vector-quickstart/docs('1')?api-version=2024-07-01  HTTP/1.1
+GET  {{baseUrl}}/indexes/hotels-vector-quickstart/docs('1')?api-version=2025-09-01  HTTP/1.1
     Content-Type: application/json
     api-key: {{apiKey}}
 ```
@@ -329,17 +329,17 @@ Deleting a document doesn't immediately free up space in the index. Every few mi
 1. [Look up the document](/rest/api/searchservice/documents/get) to verify the value of the document ID and to review its content before deleting it. Specify the key or document ID in the request. The following examples illustrate a simple string for the [Hotels sample index](search-get-started-portal.md) and a base-64 encoded string for the metadata_storage_path key of the [cog-search-demo index](tutorial-skillset.md).
 
     ```http
-    GET https://[service name].search.windows.net/indexes/hotel-sample-index/docs/1111?api-version=2024-07-01
+    GET https://[service name].search.windows.net/indexes/hotel-sample-index/docs/1111?api-version=2025-09-01
     ```
 
     ```http
-    GET https://[service name].search.windows.net/indexes/cog-search-demo/docs/aHR0cHM6Ly9oZWlkaWJsb2JzdG9yYWdlMi5ibG9iLmNvcmUud2luZG93cy5uZXQvY29nLXNlYXJjaC1kZW1vL2d1dGhyaWUuanBn0?api-version=2024-07-01
+    GET https://[service name].search.windows.net/indexes/cog-search-demo/docs/aHR0cHM6Ly9oZWlkaWJsb2JzdG9yYWdlMi5ibG9iLmNvcmUud2luZG93cy5uZXQvY29nLXNlYXJjaC1kZW1vL2d1dGhyaWUuanBn0?api-version=2025-09-01
     ```
 
 1. [Delete the document](/rest/api/searchservice/documents) using a delete `@search.action` to remove it from the search index.
 
     ```http
-    POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/index?api-version=2024-07-01
+    POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/index?api-version=2025-09-01
     Content-Type: application/json   
     api-key: [admin key] 
     {  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-howto-reindex.md' ドキュメントにおいて、検索インデックスを再構築するためのAPIバージョンを2024-07-01から2025-09-01に更新する内容です。具体的には、例示されているREST APIのリクエストにおいて、GETおよびPOSTリクエストに使用されるAPIバージョンをすべて新しいものに変更しています。この修正は、最新のAPI機能に対応し、ユーザーが正確にリクエストを行えるようにします。また、ドキュメントの整合性を保つために重要な更新であり、利用者にとって利便性が向上します。

## articles/search/search-howto-schedule-indexers.md{#item-d57e7b}

<details>
<summary>Diff</summary>
````diff
@@ -71,7 +71,7 @@ Switch to the **Indexer Definition (JSON)** tab at the top of the index to view
 1. Set the schedule property in the body of the request:
 
     ```http
-    PUT /indexers/<indexer-name>?api-version=2024-07-01
+    PUT /indexers/<indexer-name>?api-version=2025-09-01
     {
         "dataSourceName" : "myazuresqldatasource",
         "targetIndexName" : "my-target-index-name",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-howto-schedule-indexers.md' ドキュメントにおいて、インデクサーのスケジュールを設定するためのAPIバージョンを更新するものです。具体的には、HTTP PUTリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。この更新により、最新のAPIが反映され、ユーザーが新しい機能や改善点を利用できるようになります。また、この種の更新は、ドキュメントの一貫性と信頼性を保つために重要であり、コンテンツの正確性を確保します。

## articles/search/search-index-azure-sql-managed-instance-with-managed-identity.md{#item-a4ec86}

<details>
<summary>Diff</summary>
````diff
@@ -101,7 +101,7 @@ When you're connecting with a system-assigned managed identity, the only change
 Here's an example of how to create a data source to index data from a storage account using the [Create Data Source](/rest/api/searchservice/data-sources/create) REST API and a managed identity connection string. The managed identity connection string format is the same for the REST API, .NET SDK, and the Azure portal.  
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
+POST https://[service name].search.windows.net/datasources?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 
@@ -124,7 +124,7 @@ The index specifies the fields in a document, attributes, and other constructs t
 Here's a [Create Index](/rest/api/searchservice/indexes/create) REST API call with a searchable `booktitle` field:
 
 ```http
-POST https://[service name].search.windows.net/indexes?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexes?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 
@@ -144,7 +144,7 @@ An indexer connects a data source with a target search index, and provides a sch
 Here's a [Create Indexer](/rest/api/searchservice/indexers/create) REST API call with an Azure SQL indexer definition. The indexer runs when you submit the request.
 
 ```http
-POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexers?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-index-azure-sql-managed-instance-with-managed-identity.md' ドキュメントにおいて、Azure SQL マネージドインスタンスとマネージドアイデンティティを使用してデータをインデックス化するためのAPIバージョンを更新するものです。具体的には、HTTP POSTリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。この更新により、最新のAPIの機能が反映され、ユーザーが新しい改善や機能を利用しやすくなります。ドキュメントの正確性を保持し、ユーザーに信頼性のある情報を提供するために重要です。

## articles/search/search-indexer-field-mappings.md{#item-0e4628}

<details>
<summary>Diff</summary>
````diff
@@ -177,7 +177,7 @@ Only URL-safe characters can appear in an Azure AI Search document key (so that
 The following example specifies the base64Encode function on `metadata_storage_name` to handle unsupported characters.
 
 ```http
-PUT /indexers?api-version=2024-07-01
+PUT /indexers?api-version=2025-09-01
 {
   "dataSourceName" : "my-blob-datasource ",
   "targetIndexName" : "my-search-index",
@@ -201,7 +201,7 @@ A document key (both before and after conversion) can't be longer than 1,024 cha
 There are times when you need to use an encoded version of a field like `metadata_storage_path` as the key, but also need an unencoded version for full text search. To support both scenarios, you can map `metadata_storage_path` to two fields: one for the key (encoded), and a second for a path field that we can assume is attributed as `searchable` in the index schema.
 
 ```http
-PUT /indexers/blob-indexer?api-version=2024-07-01
+PUT /indexers/blob-indexer?api-version=2025-09-01
 {
     "dataSourceName" : " blob-datasource ",
     "targetIndexName" : "my-target-index",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-indexer-field-mappings.md' ドキュメントにおけるAPIバージョンを更新するものです。具体的には、HTTP PUTリクエストのAPIバージョンを2024-07-01から2025-09-01に変更しています。この更新は、Azure AI Searchのインデクサーに関連する機能を最新のものに保つために重要です。主に、`metadata_storage_name`や`metadata_storage_path`フィールドに関する設定例に対するAPI呼び出しのバージョンを更新することで、ユーザーが新しい改善点や機能を適切に利用できるようにしています。このような変更は、ドキュメントの正確性を保ち、開発者に信頼できる情報を提供するために不可欠です。

## articles/search/search-indexer-how-to-access-private-sql.md{#item-1bd4cc}

<details>
<summary>Diff</summary>
````diff
@@ -133,7 +133,7 @@ This article assumes a [REST client](search-get-started-text.md) and uses the RE
     Provide the connection string that you copied earlier with an Initial Catalog set to your database name.
 
     ```http
-    POST https://myservice.search.windows.net/datasources?api-version=2024-07-01
+    POST https://myservice.search.windows.net/datasources?api-version=2025-09-01
      Content-Type: application/json
      api-key: admin-key
      {
@@ -158,7 +158,7 @@ This article assumes a [REST client](search-get-started-text.md) and uses the RE
    [Indexer execution](search-howto-run-reset-indexers.md#indexer-execution-environment) occurs in either a private execution environment that's specific to your search service, or a multitenant environment hosted by Microsoft and used to offload expensive skillset processing for multiple customers. **When connecting over a private endpoint, indexer execution must be private.**
 
    ```http
-    POST https://myservice.search.windows.net/indexers?api-version=2024-07-01
+    POST https://myservice.search.windows.net/indexers?api-version=2025-09-01
      Content-Type: application/json
      api-key: admin-key
        {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-indexer-how-to-access-private-sql.md' ドキュメントにおいて、Azure検索サービスのプライベートSQLへのアクセス方法に関するAPIバージョンを更新したものです。具体的には、HTTP POSTリクエストで使用されるAPIバージョンが2024-07-01から2025-09-01に変更されています。この更新は、ユーザーが最新のAPI機能を利用できるようにするためのものであり、ドキュメントが現在の仕様に一致することを保証します。変更された部分には、データソースの作成およびインデクサーの実行に関連するリクエストが含まれており、正確なAPIバージョンを指定することで、信頼性と一致性のある情報を提供しています。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -346,7 +346,7 @@ On the Azure AI Search side, you can confirm request approval by revisiting the
 Alternatively, you can also obtain connection state by using the [Shared Private Link Resources - Get](/rest/api/searchmanagement/shared-private-link-resources/get).
 
 ```dotnetcli
-az rest --method get --uri https://management.azure.com/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/contoso/providers/Microsoft.Search/searchServices/contoso-search/sharedPrivateLinkResources/blob-pe?api-version=2024-07-01
+az rest --method get --uri https://management.azure.com/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/contoso/providers/Microsoft.Search/searchServices/contoso-search/sharedPrivateLinkResources/blob-pe?api-version=2025-09-01
 ```
 
 This would return a JSON, where the connection state shows up as "status" under the "properties" section. Following is an example for a storage account.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-indexer-howto-access-private.md' ドキュメントにおけるAPIバージョンのアップデートを示しています。具体的には、AzureのREST APIに対するリクエストのAPIバージョンが2024-07-01から2025-09-01に変更されています。この更新により、ユーザーは最新のエンドポイントを利用して、Azure AI Searchのプライベートリンクリソースの接続状態を確認する際に必要な正しい情報を得ることができます。変更内容は、Azure CLIのコマンドに表れており、ドキュメントが最新の仕様に準拠していることを保証するために重要です。これによって、ユーザーは新しい機能や改善点を正確かつ効果的に活用できるようになります。

## articles/search/search-indexer-troubleshooting.md{#item-087365}

<details>
<summary>Diff</summary>
````diff
@@ -180,7 +180,7 @@ If you're indexing content from Azure Blob Storage, and the container includes b
 In this situation, you can [set configuration options](search-howto-indexing-azure-blob-storage.md#DealingWithErrors) to allow indexer processing to continue if there are problems with individual documents.
 
 ```http
-PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2024-07-01
+PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 
@@ -212,7 +212,7 @@ The blob indexer [finds and extracts text from blobs in a container](search-howt
 
 
 ```http
-PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2024-07-01
+PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2025-09-01
 Content-Type: application/json
 api-key: [admin key]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-indexer-troubleshooting.md' ドキュメントにおけるAPIバージョンのアップデートを示しています。具体的には、Azure検索サービスのインデクサーに関連するHTTP PUTリクエストのAPIバージョンが2024-07-01から2025-09-01に変更されています。この修正により、ユーザーは最新のAPIに基づいた正確なリクエストを実行できるようになり、インデックス作成時のトラブルシューティングにおいてより適切な手順を踏むことができます。該当箇所には、Azure Blobストレージを用いたインデクサー設定に関する情報が含まれており、新しいAPIバージョンに対応することで、利用者は改善された機能やパフォーマンスを活用できるようになります。ドキュメントの内容が最新の仕様に一致することを確保するために、この更新は重要です。

## articles/search/search-language-support.md{#item-a7979b}

<details>
<summary>Diff</summary>
````diff
@@ -114,7 +114,7 @@ By default, a search returns all fields that are marked as retrievable. As such,
 #### Example in REST
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 {
     "search": "animaux acceptés",
     "searchFields": "Tags, Description_fr",
@@ -167,7 +167,7 @@ Sometimes the language of the agent issuing a query isn't known, in which case t
 You would then include the scoring profile in the search request:
 
 ```http
-POST /indexes/hotels/docs/search?api-version=2024-07-01
+POST /indexes/hotels/docs/search?api-version=2025-09-01
 {
   "search": "pets allowed",
   "searchFields": "Tags, Description_fr",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-language-support.md' ドキュメントにおけるAPIバージョンのアップデートを示しています。具体的には、Azure検索サービスに対するHTTP POSTリクエストのAPIバージョンが2024-07-01から2025-09-01に変更されています。この更新により、Azure検索機能の利用者は最新のAPIを使用して、サンプルインデックスにクエリを送信するための正しいリクエストを行うことができます。例として示されているリクエストには、検索語や検索フィールドも含まれており、効果的な検索結果を得るために重要な要素となっています。ドキュメントの内容が最新の仕様に従うことを保証するために、このアップデートは重要であり、ユーザーは改良された機能やパフォーマンスを活用できるようになります。

## articles/search/search-lucene-query-architecture.md{#item-b0d568}

<details>
<summary>Diff</summary>
````diff
@@ -51,7 +51,7 @@ A search request is a complete specification of what should be returned in a res
 The following example is a search request you might send to Azure AI Search using the [REST API](/rest/api/searchservice/documents/search-post):
 
 ```
-POST /indexes/hotels/docs/search?api-version=2024-07-01
+POST /indexes/hotels/docs/search?api-version=2025-09-01
 {
     "search": "Spacious, air-condition* +\"Ocean view\"",
     "searchFields": "description, title",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-lucene-query-architecture.md' ドキュメントにおいてAPIバージョンのアップデートを反映しています。具体的には、Azure AI Searchに対するHTTP POSTリクエストのAPIバージョンが2024-07-01から2025-09-01に変更されています。この変更により、最新のAPI仕様に基づいた正確な検索リクエストを構成することができ、Azure AI Searchの機能が正しく利用されることを保証します。例示されているリクエストでは、検索語や検索フィールドが指定されており、ユーザーはこの情報をもとに効果的な検索を行えるようになります。このアップデートは、ドキュメントの正確性を向上させ、ユーザーが最新の機能を利用できるようにするために重要です。

## articles/search/search-monitor-indexers.md{#item-5235df}

<details>
<summary>Diff</summary>
````diff
@@ -69,7 +69,7 @@ You can also configure the graph to see the number of skill invocations over the
 You can retrieve the status and execution history of an indexer using the [Get Indexer Status command](/rest/api/searchservice/indexers/get-status):
 
 ```http
-GET https://[service name].search.windows.net/indexers/[indexer name]/status?api-version=2024-07-01
+GET https://[service name].search.windows.net/indexers/[indexer name]/status?api-version=2025-09-01
 api-key: [Search service admin key]
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-monitor-indexers.md' ドキュメントにおけるAPIバージョンの更新を示しています。具体的には、インデクサのステータスを取得するためのHTTP GETリクエストのAPIバージョンが2024-07-01から2025-09-01に変更されました。この更新により、ユーザーは最新のAPIに基づいた正確なリクエストを行うことができ、インデクサの状態や実行履歴を取得することが容易になります。ドキュメント内で示されたリクエストには、サービス名やインデクサ名、APIキーが必要であり、この情報をもってインデクサの情報を取得できることを目的としています。この変更は、ユーザーが最新のサービス機能を利用しやすくするために重要です。

## articles/search/search-monitor-queries.md{#item-279569}

<details>
<summary>Diff</summary>
````diff
@@ -87,11 +87,11 @@ When you enable resource logging, the system captures query requests in the **Az
       AzureDiagnostics
    | project OperationName, Query_s, IndexName_s, Documents_d
    | where OperationName == "Query.Search"
-   | where Query_s != "?api-version=2024-07-01&search=*"
+   | where Query_s != "?api-version=2025-09-01&search=*"
    | where IndexName_s != "hotels-sample-index"
    ```
 
-1. Optionally, set a Column filter on *Query_s* to search over a specific syntax or string. For example, you could filter over *is equal to* `?api-version=2024-07-01&search=*&%24filter=HotelName`.
+1. Optionally, set a Column filter on *Query_s* to search over a specific syntax or string. For example, you could filter over *is equal to* `?api-version=2025-09-01&search=*&%24filter=HotelName`.
 
    ![Logged query strings](./media/search-monitor-usage/log-query-strings.png "Logged query strings")
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-monitor-queries.md' ドキュメントにおけるAPIバージョンの更新を反映しています。具体的には、リソースロギングを有効にした際にキャプチャされるクエリリクエストの例が、APIバージョン2024-07-01から2025-09-01に変更されています。この変更によって、ユーザーは最新のAPIバージョンに基づいたフィルタリングを行うことができ、より正確なクエリの監視が可能になります。クエリのフィルタリング条件として提供されている例も同様にアップデートされ、ユーザーが特定のシンタックスや文字列を用いた検索を行いやすくなっています。この更新は、Azureの検索機能の利用を向上させ、ユーザーが最新の仕様に基づいて正確に操作を行う手助けをします。

## articles/search/search-pagination-page-layout.md{#item-115902}

<details>
<summary>Diff</summary>
````diff
@@ -47,7 +47,7 @@ You can choose which fields are in search results. While a search document might
 Pick fields that offer contrast and differentiation among documents, providing sufficient information to invite a clickthrough response on the part of the user. On an e-commerce site, it might be a product name, description, brand, color, size, price, and rating. For the built-in hotels-sample index, it might be the "select" fields in the following example:
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01 
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01 
     {  
       "search": "sandy beaches",
       "select": "HotelId, HotelName, Description, Rating, Address/City",
@@ -85,7 +85,7 @@ Azure AI Search uses server-side paging to prevent queries from retrieving too m
 The default page size is 50, while the maximum page size is 1,000. If you specify a value greater than 1,000 and there are more than 1,000 results found in your index, only the first 1,000 results are returned. If the number of matches exceed the page size, the response includes information to retrieve the next page of results. For example:
 
 ```json
-"@odata.nextLink": "https://contoso-search-eastus.search.windows.net/indexes/realestate-us-sample-index/docs/search?api-version=2024-07-01"
+"@odata.nextLink": "https://contoso-search-eastus.search.windows.net/indexes/realestate-us-sample-index/docs/search?api-version=2025-09-01"
 ```
 
 The top matches are determined by search score, assuming the query is full text search or semantic. Otherwise, the top matches are an arbitrary order for exact match queries (where uniform `@search.score=1.0` indicates arbitrary ranking).
@@ -95,7 +95,7 @@ Set `top` to override the default of 50. In newer preview APIs, if you're using
 To control the paging of all documents returned in a result set, use `top` and `skip` together. This query returns the first set of 15 matching documents plus a count of total matches.
 
 ```http
-POST https://contoso-search-eastus.search.windows.net/indexes/realestate-us-sample-index/docs/search?api-version=2024-07-01
+POST https://contoso-search-eastus.search.windows.net/indexes/realestate-us-sample-index/docs/search?api-version=2025-09-01
 
 {
     "search": "condos with a view",
@@ -108,7 +108,7 @@ POST https://contoso-search-eastus.search.windows.net/indexes/realestate-us-samp
 This query returns the second set, skipping the first 15 to get the next 15 (16 through 30):
 
 ```http
-POST https://contoso-search-eastus.search.windows.net/indexes/realestate-us-sample-index/docs/search?api-version=2024-07-01
+POST https://contoso-search-eastus.search.windows.net/indexes/realestate-us-sample-index/docs/search?api-version=2025-09-01
 
 {
     "search": "condos with a view",
@@ -154,7 +154,7 @@ In this workaround, sort and filter are applied to a document ID field or anothe
 1. Issue a query to return a full page of sorted results.
 
     ```http
-    POST /indexes/good-books/docs/search?api-version=2024-07-01
+    POST /indexes/good-books/docs/search?api-version=2025-09-01
         {  
           "search": "divine secrets",
           "top": 50,
@@ -173,7 +173,7 @@ In this workaround, sort and filter are applied to a document ID field or anothe
 1. Use that ID value in a range query to fetch the next page of results. This ID field should have unique values, otherwise pagination might include duplicate results.
 
     ```http
-    POST /indexes/good-books/docs/search?api-version=2024-07-01
+    POST /indexes/good-books/docs/search?api-version=2025-09-01
         {  
           "search": "divine secrets",
           "top": 50,
@@ -251,7 +251,7 @@ To return highlighted terms, include the highlight parameter in the query reques
 By default, the format mark up is `<em>`, but you can override the tag using `highlightPreTag` and `highlightPostTag` parameters. Your client code handles the response (for example, applying a bold font or a yellow background).
 
 ```http
-POST /indexes/good-books/docs/search?api-version=2024-07-01
+POST /indexes/good-books/docs/search?api-version=2025-09-01
     {  
       "search": "divine secrets",  
       "highlight": "title, original_title",
@@ -324,7 +324,7 @@ Within a highlighted field, formatting is applied to whole terms. For example, o
 Whole-term formatting applies even on a phrase search, where multiple terms are enclosed in double quotation marks. The following example is the same query, except that "divine secrets" is submitted as a quotation-enclosed phrase (some REST clients require that you escape the interior quotation marks with a backslash `\"`):
 
 ```http
-POST /indexes/good-books/docs/search?api-version=2024-07-01 
+POST /indexes/good-books/docs/search?api-version=2025-09-01 
     {  
       "search": "\"divine secrets\"",
       "select": "title,original_title",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-pagination-page-layout.md' ドキュメント内でのAPIバージョンの更新に関するものです。具体的には、いくつかのHTTP POSTリクエストのAPIバージョンが2024-07-01から2025-09-01に変更されています。この更新は、ユーザーが最新のAPIバージョンを使用して、検索要求を正確に行うためのものであり、特にページネーションや検索結果の取得に関する記述が含まれています。

変更された部分には、インデクサのドキュメントを検索するためのリクエスト、次ページの結果を取得するためのリンク、検索時にハイライト表示するフィールドの指定が含まれており、いずれも新しいAPIバージョンに合わせて調整されています。この更新により、ユーザーは最新の機能を利用し、検索をより効果的に行うことが可能になります。また、これにより、ドキュメント内の全体的な整合性が保たれ、APIの利用に関する明確な指示が提供されることになります。

## articles/search/search-query-create.md{#item-532822}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ A full text query is specified in a `search` parameter and consists of terms, qu
 The following [Search POST REST API](/rest/api/searchservice/documents/search-post) call illustrates a query request using `search` and other parameters.
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 {
     "search": "NY +view",
     "queryType": "simple",
@@ -105,7 +105,7 @@ Use a REST client to set up a request. If you need help with getting started, se
 The following example calls the REST API for full text search:
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 {
     "search": "NY +view",
     "queryType": "simple",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-query-create.md' ドキュメントにおけるAPIバージョンの更新を反映しています。具体的には、複数のHTTP POSTリクエスト例において、APIバージョンが2024-07-01から2025-09-01に修正されています。この更新により、ユーザーは最新のAPIバージョンを使用して、検索リクエストを実行することができ、より正確なデータを取得できるようになります。

変更された部分では、全文検索のリクエストが示されており、`search` パラメーターや他のパラメーターが適切に構成されています。この更新は、Azure Searchサービスに対する最新の仕様を反映しており、ユーザーが最新の機能を活用して検索を実行する際の指針を提供します。また、技術的な整合性を保ち、より良いユーザー体験を提供するために重要です。

## articles/search/search-query-fuzzy.md{#item-a130e3}

<details>
<summary>Diff</summary>
````diff
@@ -60,7 +60,7 @@ Fuzzy queries are constructed using the full Lucene query syntax, invoking the [
 Here's an example of a query request that invokes fuzzy search. It includes four terms, two of which are misspelled:
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 {
     "search": "seatle~ waterfront~ view~ hotle~",
     "queryType": "full",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-query-fuzzy.md' ドキュメントにおけるAPIバージョンの更新に関するものです。具体的には、HTTP POSTリクエストの例においてAPIバージョンが2024-07-01から2025-09-01に修正されており、最新のAPI仕様を反映しています。

変更された部分では、ファジー検索を実行するクエリリクエストが提示されており、いくつかの検索用語が含まれています。クエリには、誤字が含まれた用語も指定されており、ファジー検索の機能を活用する方法が示されています。この更新により、ユーザーは新しいAPIバージョンを用いて、より効果的に検索を行うことができるようになります。また、これによりドキュメントの整合性が保たれ、最新の機能にアクセスできることが強調されています。

## articles/search/search-query-lucene-examples.md{#item-ce3624}

<details>
<summary>Diff</summary>
````diff
@@ -39,7 +39,7 @@ Request headers must have the following values:
 URI parameters must include your search service endpoint with the index name, docs collections, search command, and API version, similar to the following example:
 
 ```http
-https://{{service-name}}.search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+https://{{service-name}}.search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 ```
 
 The request body should be formed as valid JSON:
@@ -68,7 +68,7 @@ Fielded search scopes individual, embedded search expressions to a specific fiel
 When you use this query syntax, you can omit the `searchFields` parameter when the fields you want to query are in the search expression itself. If you include `searchFields` with fielded search, the `fieldName:searchExpression` always takes precedence over `searchFields`.
 
 ```http
-POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
+POST /indexes/hotel-samples-index/docs/search?api-version=2025-09-01
 {
     "search": "HotelName:(hotel NOT motel) AND Category:'Boutique'",
     "queryType": "full",
@@ -127,7 +127,7 @@ The field specified in `fieldName:searchExpression` must be a searchable field.
 Fuzzy search matches on terms that are similar, including misspelled words. To do a fuzzy search, append the tilde `~` symbol at the end of a single word with an optional parameter, a value between 0 and 2, that specifies the edit distance. For example, `blue~` or `blue~1` would return blue, blues, and glue.
 
 ```http
-POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
+POST /indexes/hotel-samples-index/docs/search?api-version=2025-09-01
 {
     "search": "Tags:conserge~",
     "queryType": "full",
@@ -191,7 +191,7 @@ Proximity search finds terms that are near each other in a document. Insert a ti
 This query searches for the terms *hotel* and  *airport* within five words of each other in a document. The quotation marks are escaped (`\"`) to preserve the phrase:
 
 ```http
-POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
+POST /indexes/hotel-samples-index/docs/search?api-version=2025-09-01
 {
     "search": "Description: \"hotel airport\"~5",
     "queryType": "full",
@@ -223,7 +223,7 @@ Term boosting refers to ranking a document higher if it contains the boosted ter
 In this *before* query, search for *beach access* and notice that there are six documents that match on one or both terms.
 
 ```http
-POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
+POST /indexes/hotel-samples-index/docs/search?api-version=2025-09-01
 {
     "search": "beach access",
     "queryType": "full",
@@ -306,7 +306,7 @@ In fact, only two documents match on *access*. The first instance is in second p
 In the *after* query, repeat the search, this time boosting results with the term *beach* over the term *access*. A human readable version of the query is `search=Description:beach^2 access`. Depending on your client, you might need to express `^2` as `%5E2`.
 
 ```http
-POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
+POST /indexes/hotel-samples-index/docs/search?api-version=2025-09-01
 {
     "search": "Description:beach^2 access",
     "queryType": "full",
@@ -393,7 +393,7 @@ After you boost the term *beach*, the match on Campus Commander Hotel moves down
 A regular expression search finds a match based on the contents between forward slashes `/` and lower-case strings, as documented in the [RegExp class](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/util/automaton/RegExp.html).
 
 ```http
-POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
+POST /indexes/hotel-samples-index/docs/search?api-version=2025-09-01
 {
     "search": "HotelName:/(Mo|Ho)tel/",
     "queryType": "full",
@@ -448,7 +448,7 @@ You can use generally recognized syntax for multiple (`*`) or single (`?`) chara
 In this query, search for hotel names that contain the prefix *sc*. You can't use a `*` or `?` symbol as the first character of a search.
 
 ```http
-POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
+POST /indexes/hotel-samples-index/docs/search?api-version=2025-09-01
 {
     "search": "HotelName:sc*",
     "queryType": "full",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-query-lucene-examples.md' ドキュメントにおけるAPIバージョンの更新を示しています。具体的には、複数のHTTP POSTリクエストの例において、APIバージョンが2024-07-01から2025-09-01に修正されています。この更新は、Azure Searchサービスに対する最新のAPI仕様を反映しており、ユーザーが新しい機能や改善点を活用できるようにするものです。

変更された部分では、Luceneクエリ構文を用いた検索リクエストの例が示されています。APIバージョンの更新により、リクエストの形式が整ったと見なされるため、ユーザーは正確かつ効率的に検索リクエストを行うことが可能になります。この修正は、ドキュメントの整合性を保ちながら、Azure Searchの最新機能を利用するために重要です。

## articles/search/search-query-overview.md{#item-dcd5d6}

<details>
<summary>Diff</summary>
````diff
@@ -60,7 +60,7 @@ Geospatial search uses kilometers for distance. Coordinates are specified in thi
 Here's an example of a filter for geospatial search. This filter finds other `Location` fields in the search index that have coordinates within a 300-kilometer radius of the geography point (in this example, Washington D.C.). It returns address information in the result, and includes an optional `facets` clause for self-navigation based on location.
 
 ```http
-POST https://{{searchServiceName}}.search.windows.net/indexes/hotels-vector-quickstart/docs/search?api-version=2024-07-01
+POST https://{{searchServiceName}}.search.windows.net/indexes/hotels-vector-quickstart/docs/search?api-version=2025-09-01
 {
     "count": true,
     "search": "*",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-query-overview.md' ドキュメントにおけるAPIバージョンの更新を目的としています。具体的には、HTTP POSTリクエストの例においてAPIバージョンが2024-07-01から2025-09-01に修正されており、最新のAzure検索サービスに対応しています。

変更された部分では、地理空間検索のフィルタ例として、特定の地理座標（この例ではワシントンD.C.）を基に300キロメートル半径内の他の`Location`フィールドを検索するリクエストが示されています。APIバージョンの更新により、リクエストの整合性が確保され、ユーザーは新しい機能を利用しやすくなります。この更新は、ユーザーに対して最新の機能を反映した正確な情報を提供するために重要です。

## articles/search/search-query-simple-examples.md{#item-834766}

<details>
<summary>Diff</summary>
````diff
@@ -36,7 +36,7 @@ Request headers must have the following values:
 URI parameters must include your search service endpoint with the index name, docs collections, search command, and API version, similar to the following example:
 
 ```http
-https://{{service-name}}.search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+https://{{service-name}}.search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 ```
 
 The request body should be formed as valid JSON:
@@ -63,7 +63,7 @@ The request body should be formed as valid JSON:
 Full text search can be any number of standalone terms or quote-enclosed phrases, with or without Boolean operators. 
 
 ```http
-POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
+POST /indexes/hotel-samples-index/docs/search?api-version=2025-09-01
 {
     "search": "pool spa +airport",
     "searchMode": "any",
@@ -122,7 +122,7 @@ Uniform scores of *1.0* occur when there's no rank, either because the search wa
 After search results are returned, a logical next step is to provide a details page that includes more fields from the document. This example shows you how to return a single document using [Get Document](/rest/api/searchservice/documents/get) by passing in the document ID.
 
 ```http
-GET /indexes/hotels-sample-index/docs/41?api-version=2024-07-01
+GET /indexes/hotels-sample-index/docs/41?api-version=2025-09-01
 ```
 
 All documents have a unique identifier. If you're using the Azure portal, select the index from the **Indexes** tab and then look at the field definitions to determine which field is the key. In the REST API, the [GET Index](/rest/api/searchservice/indexes/get) call returns the index definition in the response body.
@@ -174,7 +174,7 @@ The response for the preceding query consists of the document whose key is *41*.
 Filters can be defined on any field marked as `filterable` in the index definition. For hotels-sample-index, filterable fields include *Category*, *Tags*, *ParkingIncluded*, *Rating*, and most *Address* fields.
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 {
     "search": "art tours",
     "queryType": "simple",
@@ -204,7 +204,7 @@ The response for the preceding query is scoped to only those hotels categorized
 Filter expressions can include [search.ismatch and search.ismatchscoring functions](search-query-odata-full-text-search-functions.md), allowing you to build a search query within the filter. This filter expression uses a wildcard on *free* to select amenities including free wifi, free parking, and so forth.
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
   {
     "search": "",
     "filter": "search.ismatch('free*', 'Tags', 'full', 'any')",
@@ -258,7 +258,7 @@ Range filtering is supported through filters expressions for any data type. The
 The following query is a numeric range. In hotels-sample-index, the only filterable numeric field is `Rating`.
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 {
     "search": "*",
     "filter": "Rating ge 2 and Rating lt 4",
@@ -297,7 +297,7 @@ The response for this query should look similar to the following example, trimme
 The next query is a range filter over a string field (Address/StateProvince):
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 {
     "search": "*",
     "filter": "Address/StateProvince ge 'A*' and Address/StateProvince lt 'D*'",
@@ -360,7 +360,7 @@ The response for this query should look similar to the following example, trimme
 The hotels-sample-index includes a *Location* field with latitude and longitude coordinates. This example uses the [geo.distance function](search-query-odata-geo-spatial-functions.md#examples) that filters on documents within the circumference of a starting point, out to an arbitrary distance (in kilometers) that you provide. You can adjust the last value in the query (10) to reduce or enlarge the surface area of the query.
 
 ```http
-POST /indexes/v/docs/search?api-version=2024-07-01
+POST /indexes/v/docs/search?api-version=2025-09-01
 {
     "search": "*",
     "filter": "geo.distance(Location, geography'POINT(-122.335114 47.612839)') le 10",
@@ -419,7 +419,7 @@ The following example provides an illustration. The query looks for matches on *
 Notice that there's no space between the boolean operator (`-`) and the phrase *air conditioning*. The quotation marks are escaped (`\"`).
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 {
     "search": "restaurant -\"air conditioning\"",
     "searchMode": "any",
@@ -479,7 +479,7 @@ By default, a search service returns the top 50 matches. To control the number o
 The following example uses a filter and sort order on the `Rating` field (Rating is both filterable and sortable) because it's easier to see the effects of paging on sorted results. In a regular full search query, the top matches are ranked and paged by `@search.score`.
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 {
     "search": "*",
     "filter": "Rating gt 4",
@@ -495,7 +495,7 @@ The query finds 21 matching documents, but because you specified `top`, the resp
 To get the next five, skip the first batch:
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 {
     "search": "*",
     "filter": "Rating gt 4",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-query-simple-examples.md' ドキュメントにおけるAPIバージョンの更新を目的としています。具体的には、複数のHTTPリクエストの例においてAPIバージョンが2024-07-01から2025-09-01に修正されています。この変更により、Azureの検索サービスに関する最新のAPIの仕様が反映され、ユーザーは新しい機能や最適化を活用できるようになります。

変更された部分では、サンプルクエリ、フィルタ、及び範囲検索に関するリクエストの例が示されており、新しいAPIバージョンに基づいてそれぞれのリクエストが更新されています。この修正は、APIを使用するユーザーが正確で効果的にリクエストを行うために重要なものです。更新された情報により、利用者は最新の機能に基づいた正しいクエリの書き方を理解しやすくなります。

## articles/search/search-security-api-keys.md{#item-d8c908}

<details>
<summary>Diff</summary>
````diff
@@ -58,7 +58,7 @@ Here's an example of admin API key usage on a create index request:
 
 ```http
 ### Create an index
-POST {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{adminApiKey}}
 
@@ -77,7 +77,7 @@ Here's an example of query API key usage on a Search Documents (GET) request:
 
 ```http
 ### Query an index
-GET /indexes/my-new-index/docs?search=*&api-version=2024-07-01&api-key={{queryApiKey}}
+GET /indexes/my-new-index/docs?search=*&api-version=2025-09-01&api-key={{queryApiKey}}
 ```
 
 > [!NOTE]  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-security-api-keys.md' ドキュメントにおけるAPIバージョンの更新を目的としています。具体的には、管理APIキーとクエリAPIキーを使用したリクエストの例において、それぞれのAPIバージョンが2024-07-01から2025-09-01に修正されています。

変更内容には、インデックスの作成リクエスト及び検索ドキュメントリクエストのためのHTTPメソッドが含まれており、新しいAPIバージョンに対応した正しい構文が示されています。この更新により、利用者は最新のAPI機能とその使用法を正確に理解し、効果的に利用できるようになります。更新された情報は、APIキーのセキュリティに関連する重要な要素を正確に文書化するために不可欠です。

## articles/search/search-security-get-encryption-keys.md{#item-7aed9d}

<details>
<summary>Diff</summary>
````diff
@@ -73,28 +73,28 @@ $headers = @{
 To return a list of all search indexes, set the endpoint to the indexes collection.
 
 ```powershell
-$uri= 'https://<YOUR-SEARCH-SERVICE>.search.windows.net/indexes?api-version=2024-07-01&$select=name'
+$uri= 'https://<YOUR-SEARCH-SERVICE>.search.windows.net/indexes?api-version=2025-09-01&$select=name'
 Invoke-RestMethod -Uri $uri -Headers $headers | ConvertTo-Json
 ```
 
 To return a specific index definition, provide its name in the path. The encryptionKey property is at the end.
 
 ```powershell
-$uri= 'https://<YOUR-SEARCH-SERVICE>.search.windows.net/indexes/<YOUR-INDEX-NAME>?api-version=2024-07-01'
+$uri= 'https://<YOUR-SEARCH-SERVICE>.search.windows.net/indexes/<YOUR-INDEX-NAME>?api-version=2025-09-01'
 Invoke-RestMethod -Uri $uri -Headers $headers | ConvertTo-Json
 ```
 
 To return synonym maps, set the endpoint to the synonyms collection and then send the request.
 
 ```powershell
-$uri= 'https://<YOUR-SEARCH-SERVICE>.search.windows.net/synonyms?api-version=2024-07-01&$select=name'
+$uri= 'https://<YOUR-SEARCH-SERVICE>.search.windows.net/synonyms?api-version=2025-09-01&$select=name'
 Invoke-RestMethod -Uri $uri -Headers $headers | ConvertTo-Json
 ```
 
 The following example returns a specific synonym map definition, including the encryptionKey property is towards the end of the definition.
 
 ```powershell
-$uri= 'https://<YOUR-SEARCH-SERVICE>.search.windows.net/synonyms/<YOUR-SYNONYM-MAP-NAME>?api-version=2024-07-01'
+$uri= 'https://<YOUR-SEARCH-SERVICE>.search.windows.net/synonyms/<YOUR-SYNONYM-MAP-NAME>?api-version=2025-09-01'
 Invoke-RestMethod -Uri $uri -Headers $headers | ConvertTo-Json
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-security-get-encryption-keys.md' ドキュメントにおけるAPIバージョンの更新を目的としています。具体的には、PowerShellコードの例において、複数のAPIリクエストのURLが2024-07-01から2025-09-01に修正されています。

変更に含まれるのは、検索インデックスの一覧取得、特定のインデックス定義の取得、及び同義語マップの取得に関連するリクエストの例です。これらのリクエストは、指定されたAPIバージョンに基づいて更新されており、最新のAPIの仕様に準拠しています。このアップデートにより、利用者は新しい機能や改良点を活用しやすくなり、正しい構文でリクエストを行うことができます。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -328,7 +328,7 @@ This approach assumes Visual Studio Code with a REST client extension.
 1. Paste and then send a request that uses the variables you've specified. For the "Search Index Data Reader" role, you can send a query. You can use any [supported API version](/rest/api/searchservice/search-service-api-versions).
 
    ```http
-   POST https://{{baseUrl}}/indexes/{{index-name}}/docs/search?api-version=2024-07-01 HTTP/1.1
+   POST https://{{baseUrl}}/indexes/{{index-name}}/docs/search?api-version=2025-09-01 HTTP/1.1
      Content-type: application/json
      Authorization: Bearer {{token}}
 
@@ -431,7 +431,7 @@ If you're already a Contributor or Owner of your search service, you can present
 1. Paste in and then send a request to confirm access. Here's one that queries the hotels-quickstart index
 
    ```http
-   POST https://{{baseUrl}}/indexes/{{index-name}}/docs/search?api-version=2024-07-01 HTTP/1.1
+   POST https://{{baseUrl}}/indexes/{{index-name}}/docs/search?api-version=2025-09-01 HTTP/1.1
      Content-type: application/json
      Authorization: Bearer {{token}}
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-security-rbac.md' ドキュメントにおけるAPIバージョンの更新を含んでいます。具体的には、"Search Index Data Reader" 役割に関連するHTTPリクエストの構文が、APIバージョン2024-07-01から2025-09-01に更新されています。

更新されたリクエストは、特定のインデックスからデータを検索するためのPOSTメソッドを使用したものです。ドキュメント内の2つの異なるセクションで同様の変更が行われており、最新のAPIのバージョンを反映する形になっています。この更新により、利用者は最新のAPI機能を効果的に利用できるようになり、ドキュメントの信頼性も向上します。

## articles/search/search-security-trimming-for-azure-search.md{#item-d8ae51}

<details>
<summary>Diff</summary>
````diff
@@ -77,7 +77,7 @@ In the search index, within the fields collection, you need one field that conta
    The following index schema satisfies the field requirements. Documents that you index on Azure AI Search should have values for all of these fields, including the "group_ids". For the document with `file_name` "secured_file_b", only users that belong to group IDs "group_id1" or "group_id2" have read access to the file.
 
    ```https
-   POST https://[search service].search.windows.net/indexes/securedfiles/docs/index?api-version=2024-07-01
+   POST https://[search service].search.windows.net/indexes/securedfiles/docs/index?api-version=2025-09-01
    {
         "name": "securedfiles",  
         "fields": [
@@ -101,7 +101,7 @@ In Azure AI Search, the approaches for loading data are:
 The following example shows a single HTTP POST request to the docs collection of your index's URL endpoint (see [Documents - Index](/rest/api/searchservice/documents/)). The body of the HTTP request is a JSON rendering of the documents to be indexed:
 
 ```http
-POST https://[search service].search.windows.net/indexes/securedfiles/docs/index?api-version=2024-07-01
+POST https://[search service].search.windows.net/indexes/securedfiles/docs/index?api-version=2025-09-01
 {
     "value": [
         {
@@ -155,7 +155,7 @@ This sample shows how to set up query using a POST request.
 Issue the HTTP POST request, specifying the filter in the request body:
 
 ```http
-POST https://[service name].search.windows.net/indexes/securedfiles/docs/search?api-version=2024-07-01
+POST https://[service name].search.windows.net/indexes/securedfiles/docs/search?api-version=2025-09-01
 
 {
    "filter":"group_ids/any(g:search.in(g, 'group_id1, group_id2'))"  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-security-trimming-for-azure-search.md' ドキュメントにおけるAPIバージョンの更新を目的としています。具体的には、Azure AI Searchにおけるドキュメントのインデックス作成と検索リクエストのURIが、APIバージョン2024-07-01から2025-09-01に変更されています。

3つの異なる場所でPOSTリクエストのURLが更新されており、これにはインデックスへのドキュメント追加や、特定のフィルタを使用した検索が含まれます。これにより、利用者は新しいAPIバージョンに基づいた正確で最新のリクエストを行うことが可能になります。この変更は、ドキュメントの使用者にとって、最新版の機能や改善を活用する上で重要です。

## articles/search/search-semi-structured-data.md{#item-d3388d}

<details>
<summary>Diff</summary>
````diff
@@ -137,7 +137,7 @@ For help with the REST client, see [Quickstart: Full-text search using REST](sea
 
 ```http
 ### Create a data source
-POST {{baseUrl}}/datasources?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/datasources?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
 
@@ -165,7 +165,7 @@ HTTP/1.1 201 Created
 Transfer-Encoding: chunked
 Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
 ETag: "0x8DC43A5FDB8448F"
-Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net:443/datasources('ny-philharmonic-ds')?api-version=2024-07-01
+Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net:443/datasources('ny-philharmonic-ds')?api-version=2025-09-01
 Server: Microsoft-IIS/10.0
 Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
 Preference-Applied: odata.include-annotations="*"
@@ -203,7 +203,7 @@ For nested JSON, the index fields must be identical to the source fields. Curren
 
 ```http
 ### Create an index
-POST {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
 
@@ -251,7 +251,7 @@ The indexer configuration includes the `jsonArray` parsing mode and a `documentR
 
 ```http
 ### Create and run an indexer
-POST {{baseUrl}}/indexers?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexers?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
 
@@ -280,7 +280,7 @@ You can start searching as soon as the first document is loaded.
 
 ```http
 ### Query the index
-POST {{baseUrl}}/indexes/ny-philharmonic-index/docs/search?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexes/ny-philharmonic-index/docs/search?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
   
@@ -317,15 +317,15 @@ Connection: close
   },
   "value": [
   ],
-  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/ny-philharmonic-index/docs/search?api-version=2024-07-01"
+  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/ny-philharmonic-index/docs/search?api-version=2025-09-01"
 }
 ```
 
 Add a `search` parameter to search on a string, a `select` parameter to limit the results to fewer fields, and a `filter` to further narrow the search.
 
 ```http
 ### Query the index
-POST {{baseUrl}}/indexes/ny-philharmonic-index/docs/search?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexes/ny-philharmonic-index/docs/search?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
   
@@ -350,19 +350,19 @@ Indexers can be reset to clear execution history, which allows a full rerun. The
 
 ```http
 ### Reset the indexer
-POST {{baseUrl}}/indexers/ny-philharmonic-indexer/reset?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexers/ny-philharmonic-indexer/reset?api-version=2025-09-01  HTTP/1.1
   api-key: {{apiKey}}
 ```
 
 ```http
 ### Run the indexer
-POST {{baseUrl}}/indexers/ny-philharmonic-indexer/run?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexers/ny-philharmonic-indexer/run?api-version=2025-09-01  HTTP/1.1
   api-key: {{apiKey}}
 ```
 
 ```http
 ### Check indexer status 
-GET {{baseUrl}}/indexers/ny-philharmonic-indexer/status?api-version=2024-07-01  HTTP/1.1
+GET {{baseUrl}}/indexers/ny-philharmonic-indexer/status?api-version=2025-09-01  HTTP/1.1
   api-key: {{apiKey}}
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-semi-structured-data.md' ドキュメントにおけるAPIバージョンの更新に関連しています。具体的には、さまざまなHTTPリクエストのURIが、旧バージョンのAPI（2024-07-01）から新しいバージョン（2025-09-01）に変更されています。

変更対象は、データソースの作成、インデックスの作成、インデクサーの作成と実行、インデクサーのリセット、インデクサーの状態確認などのプロセスに関連するリクエストです。それぞれのHTTPリクエストで、APIバージョンの指定が変更されており、ドキュメントが最新の機能を反映しています。この更新により、ユーザーは新しいAPIの機能を利用できるようになり、より効果的にデータを処理することが可能になります。

## articles/search/search-synapseml-cognitive-services.md{#item-dcc36f}

<details>
<summary>Diff</summary>
````diff
@@ -262,7 +262,7 @@ This particular example is searching for the word "door" (`"search": "door"`). I
 ```python
 import requests
 
-url = "https://{}.search.windows.net/indexes/{}/docs/search?api-version=2024-07-01".format(search_service, search_index)
+url = "https://{}.search.windows.net/indexes/{}/docs/search?api-version=2025-09-01".format(search_service, search_index)
 requests.post(url, json={"search": "door", "count": "true", "select": "Description, Translations"}, headers={"api-key": search_key}).json()
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-synapseml-cognitive-services.md' ドキュメントにおけるAPIバージョンの更新を反映しています。具体的には、Pythonのコードスニペット内で使用されているURLが、旧バージョンのAPI（2024-07-01）から新しいバージョン（2025-09-01）に更新されています。

この更新により、ユーザーは最新のAPI機能にアクセスできるようになり、リクエストの互換性が維持されます。文書内のこの変更は、Azure Searchサービスを利用する際に必要な正確なAPIへの呼び出しを確保するために重要です。

## articles/search/search-synonyms.md{#item-2d5d63}

<details>
<summary>Diff</summary>
````diff
@@ -36,7 +36,7 @@ To create a synonym map, do so programmatically. the Azure portal doesn't suppor
 Use the [Create Synonym Map (REST API)](/rest/api/searchservice/synonym-maps/create) to create a synonym map.
 
 ```http
-POST /synonymmaps?api-version=2024-07-01
+POST /synonymmaps?api-version=2025-09-01
 {
     "name": "geo-synonyms",
     "format": "solr",
@@ -155,7 +155,7 @@ If the synonym map exists on the search service, it's used on the next query, wi
 Use the [Create or Update Index (REST API)](/rest/api/searchservice/indexes/create-or-update) to modify a field definition.
 
 ```http
-PUT /indexes?api-version=2024-07-01
+PUT /indexes?api-version=2025-09-01
 {
     "name":"hotels-sample-index",
     "fields":[
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'search-synonyms.md' ドキュメントにおけるAPIバージョンの更新に関するものです。具体的には、同様のリクエストのURIにおいて、旧バージョンのAPI（2024-07-01）から新しいバージョン（2025-09-01）への変更が行われています。

変更された部分は、シノニムマップの作成に関するリクエストおよびインデックスの作成・更新に関するリクエストです。この更新により、ユーザーは最新のAPI機能を利用することができ、新しい指定が反映された状態でサービスを利用できるようになります。これにより、Azureの検索サービスを効果的に活用するための正確なAPI呼び出しが確保されています。

## articles/search/semantic-how-to-query-request.md{#item-85530d}

<details>
<summary>Diff</summary>
````diff
@@ -125,7 +125,7 @@ The following examples in this section use the [hotels-sample-index](search-get-
 If you want to set `queryType` to `semantic`, paste the following request into a web client as a template. Replace `search-service-name` with your search service name and replace `hotels-sample-index` if you have a different index name.
 
 ```http
-POST https://[search-service-name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST https://[search-service-name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 {
       "search": "interesting hotel with restaurant on site and cozy lobby or shared area",
       "count": true,
@@ -168,7 +168,7 @@ By using `semanticQuery`, you can explicitly apply [simple text syntax](query-si
 Adjust your request to the following JSON to use `semanticQuery`.
 
 ```http
-POST https://[search-service-name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2024-07-01
+POST https://[search-service-name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
 {
     "search": "Description:breakfast",
     "semanticQuery": "interesting hotel with restaurant on site and cozy lobby or shared area",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'semantic-how-to-query-request.md' ドキュメントにおけるAPIバージョンの更新を示しています。具体的には、HTTPリクエストのURIで使用されるAPIバージョンが、従来のバージョン（2024-07-01）から最新のバージョン（2025-09-01）に変更されています。

変更が行われたのは、SMTPリクエストのテンプレートおよび`semanticQuery`を使用したリクエストに関する部分です。この更新により、ユーザーは最新のAPI仕様に基づいてリクエストを行うことができ、Azure Searchサービスの機能をフルに活用するための正確な情報が提供されます。これにより、サービスの利用者は、より効率的かつ効果的に検索機能を実装できるようになります。

## articles/search/tutorial-create-custom-analyzer.md{#item-ad5520}

<details>
<summary>Diff</summary>
````diff
@@ -67,7 +67,7 @@ A valid API key establishes trust, on a per-request basis, between the applicati
 
     ```http
     ### Create a new index
-    POST {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
       Content-Type: application/json
       api-key: {{apiKey}}
 
@@ -101,7 +101,7 @@ A valid API key establishes trust, on a per-request basis, between the applicati
 
     ```http
     ### Load documents
-    POST {{baseUrl}}/indexes/phone-numbers-index/docs/index?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexes/phone-numbers-index/docs/index?api-version=2025-09-01  HTTP/1.1
       Content-Type: application/json
       api-key: {{apiKey}}
     
@@ -155,7 +155,7 @@ A valid API key establishes trust, on a per-request basis, between the applicati
 
     ```http  
     ### Search for a phone number
-    GET {{baseUrl}}/indexes/phone-numbers-index/docs/search?api-version=2024-07-01&search=(425) 555-0100  HTTP/1.1
+    GET {{baseUrl}}/indexes/phone-numbers-index/docs/search?api-version=2025-09-01&search=(425) 555-0100  HTTP/1.1
       Content-Type: application/json
       api-key: {{apiKey}}
     ```
@@ -193,7 +193,7 @@ A valid API key establishes trust, on a per-request basis, between the applicati
 
    ```http  
     ### Search for a phone number
-    GET {{baseUrl}}/indexes/phone-numbers-index/docs/search?api-version=2024-07-01&search=4255550100  HTTP/1.1
+    GET {{baseUrl}}/indexes/phone-numbers-index/docs/search?api-version=2025-09-01&search=4255550100  HTTP/1.1
       Content-Type: application/json
       api-key: {{apiKey}}
     ```
@@ -255,7 +255,7 @@ Azure AI Search provides an [Analyze API](/rest/api/searchservice/indexes/analyz
 Call the Analyze API using the following request:
 
 ```http
-POST {{baseUrl}}/indexes/phone-numbers-index/analyze?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexes/phone-numbers-index/analyze?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}}
 
@@ -440,15 +440,15 @@ All of the tokens in the output column exist in the index. If your query include
 
    ```http
     ### Delete the index
-    DELETE {{baseUrl}}/indexes/phone-numbers-index?api-version=2024-07-01 HTTP/1.1
+    DELETE {{baseUrl}}/indexes/phone-numbers-index?api-version=2025-09-01 HTTP/1.1
         api-key: {{apiKey}}
     ```
 
 1. Recreate the index using the new analyzer. This index schema adds a custom analyzer definition and a custom analyzer assignment on the phone number field.
 
     ```http
     ### Create a new index
-    POST {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
+    POST {{baseUrl}}/indexes?api-version=2025-09-01  HTTP/1.1
       Content-Type: application/json
       api-key: {{apiKey}}
     
@@ -517,7 +517,7 @@ All of the tokens in the output column exist in the index. If your query include
 After you recreate the index, test the analyzer using the following request:
 
 ```http
-POST {{baseUrl}}/indexes/tutorial-first-analyzer/analyze?api-version=2024-07-01  HTTP/1.1
+POST {{baseUrl}}/indexes/tutorial-first-analyzer/analyze?api-version=2025-09-01  HTTP/1.1
   Content-Type: application/json
   api-key: {{apiKey}} 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'tutorial-create-custom-analyzer.md' ドキュメントにおけるAPIバージョンの更新を示しています。具体的には、HTTPリクエストのURIにおいて使用されるAPIバージョンが、2024-07-01から最新のバージョンである2025-09-01に変更されています。

更新内容には、新しいインデックスの作成、ドキュメントの読み込み、電話番号の検索、インデックスの削除および解析APIの呼び出しを含む複数のリクエストが含まれており、これによりユーザーは最新のAPIを用いてAzureのサービスを正確に利用できるようになります。この変更は、APIの仕様や機能が進化していることを反映しており、開発者が最新の実装を適切に行えるよう支援しています。

## articles/search/vector-search-how-to-configure-compression-storage.md{#item-c653c3}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ Embeddings, or the numerical representation of heterogeneous content, are the ba
 
 This article covers all of the optimization techniques in Azure AI Search that can help you reduce vector size and query processing times.
 
-Vector optimization settings are specified in vector field definitions in a search index. Most of the features described in this article are generally available in the [2024-07-01 REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-07-01&preserve-view=true) and Azure SDK packages targeting that version. The [latest preview version](/rest/api/searchservice/search-service-api-versions#preview-versions) adds support for truncated dimensions if you're using text-embedding-3-large or text-embedding-3-small for vectorization.
+Vector optimization settings are specified in vector field definitions in a search index. Most of the features described in this article are generally available in the [@search.rerankerBoostedScore REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-@search.rerankerBoostedScore&preserve-view=true) and Azure SDK packages targeting that version. The [latest preview version](/rest/api/searchservice/search-service-api-versions#preview-versions) adds support for truncated dimensions if you're using text-embedding-3-large or text-embedding-3-small for vectorization.
 
 ## Evaluate the options
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIの更新"
}
```

### Explanation
この変更は、'vector-search-how-to-configure-compression-storage.md' ドキュメントにおいて、設定されたREST APIのバージョンに関する情報を更新しています。より具体的には、ベクトル最適化設定は検索インデックス内のベクトルフィールド定義に指定され、従来の2024-07-01 REST APIから新しいメソッドである`@search.rerankerBoostedScore` REST APIへのリンクに変更されています。

この更新により、ユーザーは新しいAPIの機能から恩恵を受けることができ、Azure AI Searchの最適化手法や機能について、より正確かつ最新の情報に基づいて理解できるようになります。また、最新のプレビュー版がテキスト埋め込みにおける切り詰めた次元のサポートを追加していることに関する情報はそのまま保持されており、技術的な進歩が反映されています。

## articles/search/vector-search-how-to-configure-vectorizer.md{#item-30ffd8}

<details>
<summary>Diff</summary>
````diff
@@ -197,7 +197,7 @@ Use a search client to send a query through a vectorizer. This example assumes V
 
    ```http
     ### Run a query
-    POST {{baseUrl}}/indexes/vector-nasa-ebook-txt/docs/search?api-version=2024-07-01 HTTP/1.1
+    POST {{baseUrl}}/indexes/vector-nasa-ebook-txt/docs/search?api-version=2025-09-01 HTTP/1.1
         Content-Type: application/json
         api-key: {{queryApiKey}}
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'vector-search-how-to-configure-vectorizer.md' ドキュメントにおいてAPIバージョンを更新しています。具体的には、ベクトル化処理を通じてクエリを送信するためのHTTPリクエストのURIに記載されているAPIバージョンが、2024-07-01から最新の2025-09-01に変更されています。

この更新により、ユーザーは新しいバージョンのAPIを使用できるようになり、最新の機能や最適化手法にアクセスすることが可能になります。この変更は、Azure AI Searchの利用において最新情報を維持するために重要であり、ユーザーが最新の技術に対応したリクエストを行えるようにするためのものです。

## articles/search/vector-search-how-to-create-index.md{#item-97c769}

<details>
<summary>Diff</summary>
````diff
@@ -237,7 +237,7 @@ Vector fields are characterized by [their data type](/rest/api/searchservice/sup
    The following example shows the fields collection:
 
     ```http
-    PUT https://my-search-service.search.windows.net/indexes/my-index?api-version=2024-07-01&allowIndexDowntime=true
+    PUT https://my-search-service.search.windows.net/indexes/my-index?api-version=2025-09-01&allowIndexDowntime=true
     Content-Type: application/json
     api-key: {{admin-api-key}}
     {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'vector-search-how-to-create-index.md' ドキュメントにおいて、インデックスを作成するためのHTTPリクエストに含まれるAPIバージョンを更新しています。具体的には、PUTリクエストのURIのAPIバージョンが2024-07-01から2025-09-01に変更されています。

この更新により、ユーザーは最新のAPIバージョンを利用したインデックス作成の手順を正確に把握できるようになり、新しい機能や改善点を活用できます。Azure AI Searchの利用者にとって、最新バージョンのAPIを使うことは、より良いパフォーマンスと機能を享受するために重要です。

## articles/search/vector-search-how-to-index-binary-data.md{#item-b233b9}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ There are three steps to configuring an index for binary vectors:
 
 This article assumes you're familiar with [creating an index in Azure AI Search](search-how-to-create-search-index.md) and [adding vector fields](vector-search-how-to-create-index.md). It uses the REST APIs to illustrate each step, but you could also add a binary field to an index in the Azure portal or Azure SDK.
 
-The binary data type is generally available starting with API version 2024-07-01 and is assigned to fields using the [Create Index](/rest/api/searchservice/indexes/create) or [Create Or Update Index](/rest/api/searchservice/indexes/create-or-update) APIs.
+The binary data type is assigned to fields using the [Create Index](/rest/api/searchservice/indexes/create) or [Create Or Update Index](/rest/api/searchservice/indexes/create-or-update) APIs.
 
 > [!TIP]
 > If you're investigating binary vector support for its smaller footprint, you might also consider the vector quantization and storage reduction features in Azure AI Search. Inputs are float32 or float16 embeddings. Output is stored data in a much smaller format. For more information, see [Compress using binary or scalar quantization](vector-search-how-to-quantization.md) and [Assign narrow data types](vector-search-how-to-assign-narrow-data-types.md).
@@ -44,7 +44,7 @@ The binary data type is generally available starting with API version 2024-07-01
 
 Vector search algorithms are used to create the query navigation structures during indexing. For binary vector fields, vector comparisons are performed using the Hamming distance metric. 
 
-1. To add a binary field to an index, set up a [`Create or Update Index`](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-07-01&preserve-view=true) request using the REST API or the Azure portal.
+1. To add a binary field to an index, set up a [`Create or Update Index`](/rest/api/searchservice/indexes/create-or-update) request using the REST API or the Azure portal.
 
 1. In the index schema, add a `vectorSearch` section that specifies profiles and algorithms.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バイナリデータタイプのAPIバージョン情報の更新"
}
```

### Explanation
この変更は、'vector-search-how-to-index-binary-data.md' ドキュメントにおいて、バイナリデータタイプの利用状況に関する文言を修正しています。具体的には、バイナリデータ型が一般的に利用可能となるAPIバージョンに関する情報が削除されています。

元々は「APIバージョン2024-07-01から一般的に利用可能」と記載されていましたが、これが削除されたことで、ユーザーに対してはバイナリデータ型が任意のAPIバージョンで使用可能であることを示唆する形になっています。これにより、バイナリフィールドをインデックスに追加する手順は、APIのバージョンに関係なく実行できることがより明確になりました。

さらに、インデックスの作成や更新に関するリンクも情報が最新のものに更新されており、ユーザーは最新のAPIを参照しながら作業できるようになっています。この変更は、ユーザーがバイナリデータタイプをより簡単に活用できるようにすることを目的としています。

## articles/search/vector-search-how-to-quantization.md{#item-744f48}

<details>
<summary>Diff</summary>
````diff
@@ -64,14 +64,14 @@ It's particularly effective for embeddings with dimensions greater than 1024. Fo
 
 Rescoring is an optional technique used to offset information loss due to vector quantization. During query execution, it uses oversampling to pick up extra vectors, and supplemental information to rescore initial results found by the query. Supplemental information is either uncompressed original full-precision vectors - or for binary quantization only - you have the option of rescoring using the binary quantized document candidates against the query vector. 
 
-Only HNSW graphs allow rescoring. Exhaustive KNN doesn't support rescoring because by definition, all vectors are scanned at query time, which makes oversampling irrelevant.
+Only HNSW graphs allow rescoring. Exhaustive KNN doesn't support rescoring because by definition, all vectors are scanned at query time, which makes rescoring and oversampling irrelevant.
 
 Rescoring options are specified in the index, but you can invoke rescoring at query time by adding the oversampling query parameter.
 
 | Object | Properties |
 |--------|------------|
-| Index | Add [`RescoringOptions`](/rest/api/searchservice/indexes/create-or-update#rescoringoptions) to the vector compressions section: `rescoringOptions.enableRescoring` (true or false), `rescoringOptions.defaultOversampling` (an integer), `rescoringOptions.rescoreStorageMethod` (preserveOriginals or discardOriginals). We recommend preserveOriginals for scalar quantization and discardOriginals for binary quantization. |
-| Query | Add `oversampling` on [`RawVectorQuery`](/rest/api/searchservice/documents/search-post#rawvectorquery) or [`VectorizableTextQuery`](/rest/api/searchservice/documents/search-post#vectorizabletextquery) definitions. |
+| Index | Add [`RescoringOptions`](/rest/api/searchservice/indexes/create-or-update#rescoringoptions) to the vector compressions section. The examples in this article use `RescoringOptions`. |
+| Query | Add `oversampling` on [`RawVectorQuery`](/rest/api/searchservice/documents/search-post#rawvectorquery) or [`VectorizableTextQuery`](/rest/api/searchservice/documents/search-post#vectorizabletextquery) definitions. Adding `oversampling` invokes rescoring at query time. |
 
 > [!NOTE]
 > Rescoring parameter names have changed over the last several releases. If you're using an older preview API, review the [upgrade instructions](search-api-migration.md#upgrade-to-2024-11-01-preview) for addressing breaking changes.
@@ -80,9 +80,11 @@ The generalized process for rescoring is:
 
 1. The vector query executes over compressed vector fields.
 1. The vector query returns the top k oversampled candidates.
-1. Oversampled k candidates are rescored using either the uncompressed original vectors, or the dot product of binary quantization.
+1. Oversampled k candidates are rescored using either the uncompressed original vectors for scalar quantization, or the dot product of binary quantization.
 1. After rescoring, results are adjusted so that more relevant matches appear first.
 
+Oversampling for scalar quantized vectors requires the availability of the original full precision vectors. Oversampling for binary quantized vectors can use either full precision vectors (`preserveOriginals`) or the dot product of the binary vector (`discardOriginals`). If you're optimizing vector storage, make sure to keep the full precision vectors in the index if you need them for rescoring purposes. For more information, see [Eliminate optional vector instances from storage](vector-search-how-to-storage-options.md).
+
 ## Add "compressions" to a search index
 
 This section explains how to specify a `vectorsSearch.compressions` section in the index. The following example shows a partial index definition with a fields collection that includes a vector field.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リスコアリングとオーバーサンプリングに関する情報の更新"
}
```

### Explanation
この変更は、'vector-search-how-to-quantization.md' ドキュメントににおいて、リスコアリングとオーバーサンプリングに関する情報を更新しています。具体的には、リスコアリングの手法に関する説明がより明確になり、リスコアリングで使用されるオプションや、インデックスおよびクエリにおけるパラメータの設定方法が詳しく示されています。

主な変更点には、リスコアリングの条件が明確にされ、HNSWグラフのみがリスコアリングを許可し、Exhaustive KNNがリスコアリングをサポートしない理由が明記されています。また、リスコアリングオプションの設定方法が整理され、具体的な例を通じてユーザーが理解しやすくなっています。さらに、スカラー量子化およびバイナリ量子化の各ケースでのリスコアリングの利用法について具体的な指示が付加されています。

最後に、オーバーサンプリングの実行に必要な条件や、ストレージ最適化に関する注意点が加えられており、ユーザーがリスコアリングを効果的に実施するための理解を深めることができる情報が提供されています。

## articles/search/vector-search-how-to-query.md{#item-9bb93c}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 06/19/2025
+ms.date: 09/29/2025
 ---
 
 # Create a vector query in Azure AI Search
@@ -93,9 +93,9 @@ This section shows you the basic structure of a vector query. You can use the Az
 
 If you're migrating from [**2023-07-01-Preview**](/rest/api/searchservice/index-preview), there are breaking changes. For more information, see [Upgrade to the latest REST API](search-api-migration.md).
 
-### [**2024-07-01**](#tab/query-2024-07-01)
+### [**2025-09-01**](#tab/query-2025-09-01)
 
-[**2024-07-01**](/rest/api/searchservice/search-service-api-versions#2024-07-01) is the stable REST API version of [Search POST](/rest/api/searchservice/documents/search-post). This version supports:
+The stable version supports:
 
 + `vectorQueries` is the construct for vector search.
 + `vectorQueries.kind` set to `vector` for a vector array or `text` if the input is a string and if you [have a vectorizer](#query-with-integrated-vectorization).
@@ -108,7 +108,7 @@ If you're migrating from [**2023-07-01-Preview**](/rest/api/searchservice/index-
 In the following example, the vector is a representation of this string: `"what Azure services support full text search"`. The query targets the `contentVector` field and returns `k` results. The actual vector has 1,536 embeddings, which are trimmed in this example for readability.
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-07-01
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2025-09-01
 Content-Type: application/json
 api-key: {{admin-api-key}}
 {
@@ -133,9 +133,9 @@ api-key: {{admin-api-key}}
 }
 ```
 
-### [**2024-05-01-preview**](#tab/query-2024-05-01-preview)
+### [**2025-08-01-preview**](#tab/query-2025-08-01-preview)
 
-[**2024-05-01-preview**](/rest/api/searchservice/search-service-api-versions#2024-05-01-preview) is the latest preview API version of [Search - POST](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&tabs=HTTP&preserve-view=true). It supports the same vector query syntax as **2024-07-01**, but it has extra parameters for hybrid search and minimum thresholds for excluding weaker results.
+[**2025-08-01-preview**](/rest/api/searchservice/search-service-api-versions#2025-08-01-preview) is the latest preview API version of [Search - POST](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-08-01-preview&tabs=HTTP&preserve-view=true). It supports the same vector query syntax as **2025-09-01**, but it has extra parameters for hybrid search and minimum thresholds for excluding weaker results.
 
 This preview adds:
 
@@ -145,7 +145,7 @@ This preview adds:
 In the following example, the vector is a representation of this string: `"what Azure services support full text search"`. The query targets the `contentVector` field and returns `k` results. The actual vector has 1,536 embeddings, which are trimmed in this example for readability.
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-05-01-preview
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2025-08-01-preview
 Content-Type: application/json
 api-key: {{admin-api-key}}
 {
@@ -267,7 +267,7 @@ You can set the `vectorQueries.fields` property to multiple vector fields. The v
 When querying multiple vector fields, ensure that each one contains embeddings from the same embedding model. The query should also be generated from the same embedding model.
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-07-01
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2025-09-01
 Content-Type: application/json
 api-key: {{admin-api-key}}
 {
@@ -338,7 +338,7 @@ Search indexes can't store images. Assuming that your index includes a field for
 
 ## Query with integrated vectorization
 
-This section shows a vector query that invokes the [integrated vectorization](vector-search-integrated-vectorization.md) to convert a text or [image query](search-get-started-portal-image-search.md) into a vector. We recommend the stable [**2024-07-01**](/rest/api/searchservice/documents/search-post) REST API, Search Explorer, or newer Azure SDK packages for this feature.
+This section shows a vector query that invokes the [integrated vectorization](vector-search-integrated-vectorization.md) to convert a text or [image query](search-get-started-portal-image-search.md) into a vector. We recommend the stable [**2025-09-01**](/rest/api/searchservice/documents/search-post) REST API, Search Explorer, or newer Azure SDK packages for this feature.
 
 A prerequisite is a search index that has a [vectorizer configured and assigned](vector-search-how-to-configure-vectorizer.md) to a vector field. The vectorizer provides connection information to an embedding model used at query time.
 
@@ -358,7 +358,7 @@ Search Explorer supports integrated vectorization at query time. If your index c
 
    Alternatively, you can select **View** > **JSON view** to view or modify the query. If vectors are present, Search Explorer sets up a vector query automatically. You can use the JSON view to select fields for use in the searche and response, add filters, and construct more advanced queries, such as [hybrid queries](hybrid-search-how-to-query.md). To see a JSON example, select the REST API tab in this section.
 
-### [**REST API**](#tab/builtin-2024-07-01)
+### [**REST API**](#tab/builtin-2025-09-01)
 
 1. Use [Index - GET](/rest/api/searchservice/indexes/get) to return the index definition and check for the presence of a vectorizer configuration. Look for `vectorizers` in your index definition. It should specify a deployed embedding model.
 
@@ -372,7 +372,7 @@ Search Explorer supports integrated vectorization at query time. If your index c
 Here's a simple example of a query that's vectorized at query time. The text string is vectorized and then used to query the `descriptionVector` field.
 
 ```http
-POST https://{{search-service}}.search.windows.net/indexes/{{index}}/docs/search?api-version=2024-07-01
+POST https://{{search-service}}.search.windows.net/indexes/{{index}}/docs/search?api-version=2025-09-01
 {
     "select": "title, genre, description",
     "vectorQueries": [
@@ -391,7 +391,7 @@ Here's a [hybrid query](hybrid-search-how-to-query.md) that uses integrated vect
 In this example, the search engine makes three vectorization calls to the vectorizers assigned to `descriptionVector`, `synopsisVector`, and `authorBioVector` in the index. The resulting vectors are used to retrieve documents against their respective fields. The search engine also executes a keyword search on the `search` query, which is `"mystery novel set in London"`.
 
 ```http
-POST https://{{search-service}}.search.windows.net/indexes/{{index}}/docs/search?api-version=2024-07-01
+POST https://{{search-service}}.search.windows.net/indexes/{{index}}/docs/search?api-version=2025-09-01
 Content-Type: application/json
 api-key: {{admin-api-key}}
 {
@@ -473,7 +473,7 @@ Weights are used when calculating the [RRF scores](hybrid-search-ranking.md#weig
 The following example is a hybrid query with two vector query strings and one text string. Weights are assigned to the vector queries. The first query is 0.5 or half the weight, reducing its importance in the request. The second vector query is twice as important.
 
 ```http
-POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?api-version=2024-07-01
+POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?api-version=2025-09-01
 
     { 
       "vectorQueries": [ 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新と説明の修正"
}
```

### Explanation
この変更は、'vector-search-how-to-query.md' ドキュメント内で、Azure AI Searchのベクタークエリに関連する情報を更新しています。最も注目すべきは、関連するAPIバージョンが2024-07-01から2025-09-01に変更され、これに伴いAPIエンドポイントや関連する説明も適切に修正された点です。

具体的には、ドキュメント中のいくつかのセクションで、APIのバージョン情報が古くなっている部分を新しいものに置き換えています。また、リスコアリングやハイブリッド検索などの新機能に関する記述も見直され、ユーザーが最新のREST APIを使用した際の機能を正確に理解できるよう工夫されています。

この更新により、ユーザーはより新しいAPIを参照しながら、ベクタークエリの構造や実装方法についての理解を深められるようになります。また、APIの変更に伴う注意事項やマイグレーションガイドへのリンクも含まれており、過去のバージョンからの移行をサポートしています。

## articles/search/vector-search-how-to-storage-options.md{#item-ee1680}

<details>
<summary>Diff</summary>
````diff
@@ -9,12 +9,17 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 09/19/2025
+ms.date: 09/29/2025
 ---
 
 # Eliminate optional vector instances from storage
 
-Azure AI Search stores multiple copies of vector fields that are used in specific workloads. If you don't need to support a specific behavior, like returning raw vectors in a query response, you can set properties in the index that omit storage for that workload.
+Azure AI Search stores multiple copies of vector fields that are used in specific workloads. If your search scenarios don't require all of these copies, you can omit storage for that workload. 
+
+Use cases where an extra copy is used include:
+
+- Returning raw vectors in a query response or supporting incremental updates to vector content.
+- Rescoring compressed (quantized) vectors as a query optimization technique.
 
 Removing storage is irreversible and requires reindexing if you want it back.
 
@@ -24,33 +29,21 @@ Removing storage is irreversible and requires reindexing if you want it back.
 
 ## How vector fields are stored
 
-For every vector field, there are up to three copies of the vectors, each serving a different purpose:
-
-| Instance | Usage | Controlled using |
-|----------|-------|------------------|
-| Source vectors received during document indexing (JSON data) | Used for incremental data refresh with `merge` or `mergeOrUpload` indexing action. Also used to return "retrievable" vectors in the query response. | `stored` property on vector fields |
-| Original full-precision vectors (binary data) | Used for internal index operations and for exhaustive KNN search in older API versions. For compressed vectors, it's also used for `preserveOriginals` rescoring on an oversampled candidate set of results from ANN search. This applies to vector fields that undergo [scalar or binary quantization](vector-search-how-to-quantization.md). | `rescoringOptions.rescoreStorageMethod` property in `vectorSearch.compressions`. |
-| Vectors in the [HNSW graph for Approximate Nearest Neighbors (ANN) search](vector-search-overview.md) (HNSW graph) or vectors for exhaustive K-Nearest Neighbors (eKNN index) | Used for query execution. Consists of either full-precision vectors (when no compression is applied) or quantized vectors. | Essential. There are no parameters for removing this instance. |
-
-You can set properties that permanently discard the first two instances (JSON data and binary data) from vector storage, but not the last instance.
-
-To offset lossy compression for HNSW, you can keep the second instance (binary data) for rescoring purposes to improve ANN search quality. For eKNN, only scalar quantization is supported, and rescoring isn't an option. In newer API versions like the latest preview, the second instance isn't kept for eKNN because the third instance provides full-precision vectors in an eKNN index.
-
-### Indexes created with 2024-11-01-preview or later API versions
+| Instance | Usage | Required for search | How removed |
+|----------|-------|---------------------|-------------|
+| Vectors in the [HNSW graph for Approximate Nearest Neighbors (ANN) search](vector-search-overview.md) (HNSW graph) or vectors for exhaustive K-Nearest Neighbors (eKNN index) | Used for query execution. Consists of either full-precision vectors (when no compression is applied) or quantized vectors. | Essential | There are no parameters for removing this instance. |
+| Source vectors received during document indexing (JSON data) | Used for incremental data refresh with `merge` or `mergeOrUpload` indexing actions. Also used to return "retrievable" vectors in the query response. | No | Set `stored` property to false. |
+| Original full-precision vectors (binary data) <sup>1</sup> | For compressed vectors, it's used for `preserveOriginals` rescoring on an oversampled candidate set of results from ANN search. This applies to vector fields that undergo [scalar or binary quantization](vector-search-how-to-quantization.md), and it applies to queries using the HNSW graph. If you're using eKNN, all vectors are in scope for the query, so rescoring has no effect and thus not supported. | No | Set `rescoringOptions.rescoreStorageMethod` property to `discardOriginals` in `vectorSearch.compressions`. |
 
-For indexes created with the 2024-11-01-preview or a later API with uncompressed vector fields, the second and third instances (binary data and HNSW graph) are combined as part of our cost reduction investments, reducing overall storage. A newer generation index with consolidated vectors is functionally equivalent to older indexes, but uses less storage. Physical data structures are established on a Create Index request, so you must delete and recreate the index to realize the storage reductions.
-
-If you choose [vector compression](vector-search-how-to-configure-compression-storage.md), AI Search compresses (quantizes) the in-memory portion of the vector index. Since memory is often a primary constraint for vector indexes, this practice allows you to store more vectors within the same search service. However, lossy compression equates to less information in the index, which can affect search quality.
-
-To mitigate the loss in information, you can [enable "rescoring" and "oversampling" options](vector-search-how-to-quantization.md#supported-rescoring-techniques) to help maintain quality. The effect is retrieval of a larger set of candidate documents from the compressed index, with recomputation of similarity scores using the original vectors or the dot product. For rescoring to work, original vectors must be retained in storage for certain scenarios. As a result, while quantization reduces memory usage (vector index size usage), it slightly increases storage requirements since both compressed and original vectors are stored. The extra storage is approximately equal to the size of the compressed index.
+<sup>1</sup> This copy is also for internal index operations and for exhaustive KNN search in older API versions, on indexes created using the 2023 APIs. On newer indexes, an eKNN-configured field consists of full-precision vectors so no extra copy is needed.
 
 ## Remove source vectors (JSON data)
 
 In a vector field definition, `stored` is a boolean property that determines whether storage is allocated for retrievable vector content obtained during indexing (the source instance). By default, `stored` is set to `true`. If you don't need raw vector content in a query response, changing `stored` to `false` can save up to 50% storage per field.
 
 Considerations for setting `"stored": false`:
 
-- Because vectors aren't human readable, you can omit them from results sent to LLMs in RAG scenarios or from results rendered on a search page. However, keep them if you're using vectors in a downstream process that consumes vector content.
+- Because vectors aren't human readable, you can generally omit them from results sent to LLMs in RAG scenarios or from results rendered on a search page. However, you should keep them if you're using vectors in a downstream process that consumes vector content.
 
 - If your indexing strategy uses [partial document updates](search-howto-reindex.md#update-content), such as `merge` or `mergeOrUpload` on an existing document, setting `"stored": false` prevents content updates to those fields during the merge. You must include the entire vector field (and nonvector fields you're updating) in each reindexing operation. Otherwise, the vector data is lost without an error or warning. To avoid this risk altogether, set `"stored": true`.
 
@@ -60,7 +53,7 @@ Considerations for setting `"stored": false`:
 For new vector fields in a search index, set `"stored": false` to permanently remove retrievable storage for the vector field. The following example shows a vector field definition with the `stored` property.
 
 ```http
-PUT https://[service-name].search.windows.net/indexes/demo-index?api-version=2024-07-01 
+PUT https://[service-name].search.windows.net/indexes/demo-index?api-version=2025-09-01@search.rerankerBoostedScore 
   Content-Type: application/json  
   api-key: [admin key]  
 
@@ -89,44 +82,37 @@ PUT https://[service-name].search.windows.net/indexes/demo-index?api-version=202
 
 - Defaults are `"stored": true` and `"retrievable": false`. In a default configuration, a retrievable copy is stored but isn't automatically returned in results. When `stored` is `true`, you can toggle `retrievable` between `true` and `false` at any time without having to rebuild an index. When `stored` is `false`, `retrievable` must be `false` and can't be changed.
 
-## Remove full-precision vectors (binary data)
+## Remove full-precision vectors
 
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+Original full-precision vectors are used in rescoring operations over compressed (quantized) vectors. The intent of rescoring is to mitigate the loss in information due to compression. The effect of rescoring is retrieval of a larger set of candidate documents from the compressed index, with recomputation of similarity scores using the original vectors or the dot product. For rescoring to work, original vectors must be retained in storage for certain scenarios. As a result, while quantization reduces memory usage (vector index size usage), it slightly increases storage requirements since both compressed and original vectors are stored. The extra storage is approximately equal to the size of the compressed index.
 
-When you compress vectors using either scalar or binary quantization, query execution is over the quantized vectors. In this case, you only need the original full-precision vectors (binary data) if you want to rescore.
+Rescoring requirements by quantization approach:
 
-If you use newer preview APIs *and* binary quantization, you can safely discard full-precision vectors because rescoring strategies now use the dot product of a binary embedding, which produces high quality search results, without having to reference full-precision vectors in the index.
+- Rescoring of scalar quantized vectors requires retention of the original full-precision vectors.
 
-The `rescoreStorageMethod` property controls whether full-precision vectors are stored. The guidance for whether to retain full-precision vectors is:
+- Rescoring of binary quantized vectors can use either the original full-precision vectors, or the dot product of the binary embedding, which produces high quality search results, without having to reference full-precision vectors in the index.
 
-- For scalar quantization, preserve original full-precision vectors in the index because they're required for rescore.
-- For binary quantization, preserve original full-precision vectors for the highest quality of rescoring, or discard full-precision vectors (requires 2025-03-01-preview) if you want to rescore based on the dot product of the binary embeddings.
+Rescoring recommendations:
 
-Vector storage strategies have been evolving over the last several releases. Index creation date and API version determine your storage options.
-
-| API version | Applies to | Remove full-precision vectors |
-|--|--|--|
-| 2024-07-01 and earlier | Not applicable. | There's no mechanism for removing full-precision vectors. |
-| 2024-11-01-preview | Binary embeddings | Use `rescoreStorageMethod.discardOriginals` to remove full-precision vectors, but doing so prevents rescoring. `enableRescoring` must be false if originals are gone.|
-| 2025-03-01-preview | Binary embeddings | Use `rescoreStorageMethod.discardOriginals` to remove full-precision vectors in the index while still retaining rescore options. In this preview, rescoring is possible because the technique changed. The dot product of the binary embeddings is used on the rescore, producing high quality search results equivalent to or better than earlier techniques based on full-precision vectors. |
+- For scalar quantization, preserve original full-precision vectors in the index because they're required for rescore.
 
-Notice that scalar isn't listed in the table. If you use scalar quantization, you must retain original full-precision vectors if you want to rescore.
+- For binary quantization, either preserve original full-precision vectors for the highest quality of rescoring, or discard full-precision vectors if you want to rescore based on the dot product of the binary embeddings.
 
-In `vectorSearch.compressions`, the `rescoreStorageMethod` property is set to `preserveOriginals` by default, which retains full-precision vectors for [oversampling and rescoring capabilities](vector-search-how-to-quantization.md#add-compressions-to-a-search-index) to reduce the effect of lossy compression on the HNSW graph. If you don't need full-precision vectors, you can reduce vector storage by setting `rescoreStorageMethod` to `discardOriginals`.
+The `rescoreStorageMethod` property controls whether full-precision vectors are stored. In `vectorSearch.compressions`, the `rescoreStorageMethod` property is set to `preserveOriginals` by default, which retains full-precision vectors for [oversampling and rescoring capabilities](vector-search-how-to-quantization.md#add-compressions-to-a-search-index) to reduce the effect of lossy compression on the HNSW graph. If you don't need rescoring, of if you used binary quantization and the dot product for rescoring, you can reduce vector storage by setting `rescoreStorageMethod` to `discardOriginals`.
 
 > [!IMPORTANT]
 > Setting the `rescoreStorageMethod` property is irreversible and can adversely affect search quality, although the degree depends on the compression method and any mitigations you apply.
 
 To set this property:
 
-1. Use [Create Index (preview)](/rest/api/searchservice/indexes/create?view=rest-searchservice-2025-03-01-preview&preserve-view=true) or [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true) REST APIs, or an Azure SDK beta package providing the feature.
+1. Use [Create Index](/rest/api/searchservice/indexes/create) or [Create or Update Index](/rest/api/searchservice/indexes/create-or-update) REST APIs, or an Azure SDK.
 
 1. Add a `vectorSearch` section to your index with profiles, algorithms, and compressions.
 
 1. Under `vectorSearch.compressions`, add `rescoringOptions` with `enableRescoring` set to true, `defaultOversampling` set to a positive integer, and `rescoreStorageMethod` set to `discardOriginals` for binary quantization and `preserveOriginals` for scalar quantization.
 
     ```http
-    PUT https://[service-name].search.windows.net/indexes/demo-index?api-version=2025-03-01-preview
+    PUT https://[service-name].search.windows.net/indexes/demo-index?api-version=2025-09-01
     
     {
         "name": "demo-index",
@@ -186,3 +172,5 @@ To set this property:
         }
     }
     ```
+> [!NOTE]
+> Vector storage strategies have been evolving over the last several releases. Index creation date and API version determine your storage options. For example, in the 2024-11-01-preview, if you set `discardOriginals` to remove full-precision vectors, there was no rescoring for binary quantization because the dot product approach wasn't available. We recommend using the latest APIs for the best mitigation options.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクター保存オプションに関する情報の更新"
}
```

### Explanation
この変更は、'vector-search-how-to-storage-options.md' ドキュメント内のベクター保存に関する情報を更新しています。主な変更点は、ベクターのインスタンスの管理やストレージオプションに関する説明を明確化し、最新のAPIバージョンに合わせた指針を提供していることです。

具体的には、ベクターのストレージ戦略が改良され、不要なデータの保存を省く方法が強調されています。特定のワークロードに必要のないベクターのコピーを削除するオプションが追加されており、リスコアリングや検索におけるベクターの扱い方に関するガイドラインが最新の情報に基づいて整理されています。

特に、フルプレシジョンベクターのストレージがリスコアリングや検索の品質に及ぼす影響について詳しい説明が加えられ、ユーザーが適切なストレージオプションを選択するための情報が提供されています。また、不要なベクターを削除する手順や、ストレージ設定の変更が不可逆的であることが注意喚起されています。

最後に、リリースバージョンの進化に伴い、最新のAPIを使用することが求められており、さまざまな新機能や最適化オプションが使用できる点も強調されています。これにより、ユーザーは効率的にベクターを管理し、ストレージを最適化するための具体的な手順を習得できるようになっています。

## articles/search/vector-search-index-size.md{#item-bb2846}

<details>
<summary>Diff</summary>
````diff
@@ -92,7 +92,7 @@ Usage and quota are reported in bytes.
 Here's GET Service Statistics:
 
 ```http
-GET {{baseUrl}}/servicestats?api-version=2024-07-01  HTTP/1.1
+GET {{baseUrl}}/servicestats?api-version=2025-09-01  HTTP/1.1
     Content-Type: application/json
     api-key: {{apiKey}}
 ```
@@ -134,7 +134,7 @@ Response includes metrics for `storageSize`, which doesn't distinguish between v
 You can also send a GET Index Statistics to get the physical size of the index on disk, plus the in-memory size of the vector fields.
 
 ```http
-GET {{baseUrl}}/indexes/vector-healthplan-idx/stats?api-version=2024-07-01  HTTP/1.1
+GET {{baseUrl}}/indexes/vector-healthplan-idx/stats?api-version=2025-09-01  HTTP/1.1
     Content-Type: application/json
     api-key: {{apiKey}}
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新"
}
```

### Explanation
この変更は、'vector-search-index-size.md' ドキュメント内において、いくつかのAPIエンドポイントのバージョン番号を更新したものです。具体的には、`servicestats`エンドポイントおよび`indexes`エンドポイントに関するリクエストのAPIバージョンが、2024-07-01から2025-09-01に変更されています。

この修正により、最新のAPIバージョンに合わせたリクエストが可能となり、ユーザーは最新の機能および統計情報を取得するための正しいエンドポイントを利用できます。これにより、ストレージサイズやインデックスの物理的なサイズに関する統計情報を正確に取得することが促進され、Azure AI Searchの使用がよりスムーズになります。

全体として、この変更はAPIの持続的な更新に伴うものであり、ドキュメントの正確性と信頼性を向上させる重要な手続きです。ユーザーはこの更新によって、最新の情報に基づいた適切なリクエストを行うことができるようになります。


