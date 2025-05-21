---
date: '2025-05-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9b2c87c...MicrosoftDocs:f021165
summary: |-
  このコード差分における変更は、Azure AI Search関連のドキュメントに対する軽微な更新とフォーマット改善です。主な内容には新機能の追加、用語改善、視覚的支援の強化が含まれています。

  新機能として、インデックス編集を視覚化する画像やファイアウォール設定の視覚化画像が追加されました。また、「エージェント」という用語が「ナレッジエージェント」に変更され、用語の統一が図られた一方で、既存の認識との適応が必要となります。

  その他、パラメーター説明の明確化や関連イメージの更新により、ユーザビリティが向上しています。これらの更新は、Azure AI Searchの利用をより直感的にし、技術的支援を強化することを目的としています。全体として、ドキュメントの質が向上し、技術者がシステムを適切に設定するための重要な情報が提供されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9b2c87c...MicrosoftDocs:f021165){target="_blank"}

<format>
# Highlights
このコード差分における変更は、Azure AI Search関連のドキュメントに対して行われた複数の軽微な更新とフォーマット改善を中心としたものです。主な内容として新機能の追加や用語の改善、画像の追加による視覚的支援の強化が行われました。

## New features
- `search-how-to-index/edit-index-json.png`にインデックス編集を視覚化する新しい画像が追加されました。
- `exceptions.png`がファイアウォールの例外設定を視覚化するために追加されました。

## Breaking changes
特に重大な破壊的変更はありませんが、多くの文書で「エージェント」という用語が「ナレッジエージェント」に変更されています。これにより、用語が統一され、理解が向上する一方、既存の認識を新しい用語に適応させる必要があります。

## Other updates
- パラメーター説明の明確化や関連イメージの更新が多くのセクションで行われ、ユーザビリティが向上しています。

# Insights
Azure AI Search関連のドキュメントにおける今回の更新は、ユーザーフレンドリーなインターフェースを提供し、機能の正確な設定を促進することを目的としています。特に、「エージェント」という用語を「ナレッジエージェント」に変更したことは、その役割をより具体的に表現する意図があり、技術的ドキュメント全体での一貫性が強化されました。

インデックス編集やファイアウォール設定に関する新しい画像の追加は、文章だけで伝わりにくい設定手順を視覚的に示し、特に初心者や新しいユーザーにとっての理解を促進します。同時に、パラメーターの説明における明確化は、技術者がシステムの機能を正確に設定し、競争力を強化するための鍵となります。

フォーマットの改善は文章の読みやすさを向上させ、技術的な内容を迅速に理解し、適切な対応を取るための助けとなることでしょう。これらのドキュメント更新は、Azure AI Searchを利用するすべての技術者にとって有益な情報を提供し、その利用効率と正確性を高める重要な一歩と言えます。

こうした更新と改善により、ユーザーはより直感的にAzure AI Searchサービスの利用方法を理解できるようになり、技術的な支援が強化されます。全体としては、見やすさと使いやすさという観点からドキュメントの質が底上げされる結果となっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-custom-skill-web-api.md](#item-5d1065) | minor update | 認証IDパラメーターの説明を更新 | modified | 1 | 1 | 2 | 
| [cognitive-search-skill-azure-openai-embedding.md](#item-3eca57) | minor update | authIdentityパラメーターの説明を更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-python.md](#item-efee6a) | minor update | エージェントの用語を変更 | modified | 3 | 3 | 6 | 
| [edit-index-json.png](#item-5780d0) | new feature | インデックス編集の画像を追加 | added | 0 | 0 | 0 | 
| [azure-portal-firewall-all.png](#item-8adb6b) | minor update | ファイアウォール設定画像の更新 | modified | 0 | 0 | 0 | 
| [exceptions.png](#item-f019d3) | new feature | ファイアウォール例外の画像を追加 | added | 0 | 0 | 0 | 
| [multimodal-search-overview.md](#item-d82192) | minor update | マルチモーダル検索概説の内容更新 | modified | 7 | 2 | 9 | 
| [search-agentic-retrieval-concept.md](#item-797a22) | minor update | エージェンティックリトリーバルの概念に関する更新 | modified | 11 | 11 | 22 | 
| [search-agentic-retrieval-how-to-create.md](#item-310fbe) | minor update | ナレッジエージェント作成に関するガイドの更新 | modified | 19 | 19 | 38 | 
| [search-agentic-retrieval-how-to-pipeline.md](#item-1ad1c3) | minor update | ナレッジリトリーバル用パイプラインの作成に関する更新 | modified | 7 | 7 | 14 | 
| [search-agentic-retrieval-how-to-retrieve.md](#item-5f7fc0) | minor update | ナレッジエージェントを使用したデータ取得に関する更新 | modified | 10 | 10 | 20 | 
| [search-get-started-agentic-retrieval.md](#item-4a40f4) | minor update | ナレッジエージェントを使用したクイックスタートの更新 | modified | 3 | 3 | 6 | 
| [search-how-to-create-search-index.md](#item-c4ff31) | minor update | 検索インデックス作成方法の更新 | modified | 3 | 1 | 4 | 
| [search-how-to-index-logic-apps-indexers.md](#item-64a12e) | minor update | Logic Appsインデクサーの更新 | modified | 2 | 1 | 3 | 
| [search-howto-index-one-to-many-blobs.md](#item-04ada2) | minor update | 一対多のBlobインデックス作成方法の更新 | modified | 10 | 5 | 15 | 
| [search-howto-reindex.md](#item-46738a) | minor update | インデックスの再構築および更新に関する情報の追加 | modified | 41 | 1 | 42 | 
| [search-index-access-control-lists-and-rbac-push-api.md](#item-45e71e) | minor update | アクセス制御リストとRBACに関するREST APIのドキュメントの更新 | modified | 6 | 6 | 12 | 
| [search-query-access-control-rbac-enforcement.md](#item-d24df7) | minor update | RBACの強制を伴うクエリのアクセス制御に関する文書の更新 | modified | 29 | 6 | 35 | 
| [search-what-is-an-index.md](#item-5a3344) | minor update | 検索インデックスに関する文書の更新 | modified | 4 | 2 | 6 | 
| [service-configure-firewall.md](#item-75be3f) | minor update | Azure AI Searchのファイアウォール設定に関する文書の更新 | modified | 19 | 14 | 33 | 
| [toc.yml](#item-c4768f) | minor update | エージェントによる検索に関する文書のタイトル更新 | modified | 2 | 2 | 4 | 
| [tutorial-adls-gen2-indexer-acls.md](#item-6881a0) | minor update | ADLS Gen2インデクサーとACLに関するチュートリアルの更新 | modified | 25 | 2 | 27 | 
| [vector-search-vectorizer-ai-services-vision.md](#item-942a3e) | minor update | AIサービスへの接続に関する文書のフォーマット更新 | modified | 1 | 1 | 2 | 
| [vector-search-vectorizer-azure-open-ai.md](#item-e75cee) | minor update | Azure OpenAIへの接続に関する文書のフォーマット更新 | modified | 1 | 1 | 2 | 
| [vector-search-vectorizer-custom-web-api.md](#item-d7c2f9) | minor update | カスタムWeb APIへの接続に関する文書のフォーマット更新 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-fa71b4) | minor update | インデックスの説明に関する情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/cognitive-search-custom-skill-web-api.md{#item-5d1065}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ Parameters are case-sensitive.
 |--------------------|-------------|
 | `uri` | The URI of the Web API to which the JSON payload is sent. Only the **https** URI scheme is allowed. |
 | `authResourceId` | (Optional) A string that if set, indicates that this skill should use a system managed identity on the connection to the function or app hosting the code. This property takes an application (client) ID or app's registration in Microsoft Entra ID, in any of these formats: `api://<appId>`, `<appId>/.default`, `api://<appId>/.default`. This value is used to scope the authentication token retrieved by the indexer, and is sent along with the custom Web skill API request to the function or app. Setting this property requires that your search service is [configured for managed identity](search-howto-managed-identities-data-sources.md) and your Azure function app is [configured for a Microsoft Entra sign in](/azure/app-service/configure-authentication-provider-aad). To use this parameter, call the API with `api-version=2023-10-01-Preview`. |
-| `authIdentity`   | (Optional) A user-managed identity used by the search service for connecting to the function or app hosting the code. You can use either a [system or user managed identity](search-howto-managed-identities-data-sources.md). To use a system manged identity, leave `authIdentity` blank. |
+| `authIdentity`   | (Optional) A user-managed identity used by the search service for connecting to the function or app hosting the code. You can use either a [system or user managed identity](search-howto-managed-identities-data-sources.md). To use a system managed identity, leave `authIdentity` blank. |
 | `httpMethod` | The method to use while sending the payload. Allowed methods are `PUT` or `POST` |
 | `httpHeaders` | A collection of key-value pairs where the keys represent header names and values represent header values that are sent to your Web API along with the payload. The following headers are prohibited from being in this collection:  `Accept`, `Accept-Charset`, `Accept-Encoding`, `Content-Length`, `Content-Type`, `Cookie`, `Host`, `TE`, `Upgrade`, `Via`. |
 | `timeout` | (Optional) When specified, indicates the timeout for the http client making the API call. It must be formatted as an XSD "dayTimeDuration" value (a restricted subset of an [ISO 8601 duration](https://www.w3.org/TR/xmlschema11-2/#dayTimeDuration) value). For example, `PT60S` for 60 seconds. If not set, a default value of 30 seconds is chosen. The timeout can be set to a maximum of 230 seconds and a minimum of 1 second. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "認証IDパラメーターの説明を更新"
}
```

### Explanation
この変更は、`cognitive-search-custom-skill-web-api.md`ファイル内の一部のパラメーターの説明を微調整したものです。具体的には、`authIdentity`パラメータの説明が改善され、ユーザー管理のアイデンティティに関する情報がより明確になりました。変更の内容は、システム管理アイデンティティの使用方法についての指示が補完され、ユーザー管理アイデンティティの説明が強調されました。また、`authResourceId`パラメータに関する文も更新されており、パラメータの使用に関する前提条件や設定手順が明示されています。このような修正は、ユーザーが機能を正しく設定し利用できるようにするための重要な情報提供を意図しています。

## articles/search/cognitive-search-skill-azure-openai-embedding.md{#item-3eca57}

<details>
<summary>Diff</summary>
````diff
@@ -44,7 +44,7 @@ Parameters are case-sensitive.
 | `resourceUri` | The URI of the model provider, in this case, an Azure OpenAI resource. This parameter only supports URLs with domain `openai.azure.com`, such as `https://<resourcename>.openai.azure.com`. If the Azure OpenAI endpoint has a URL with domain `cognitiveservices.azure.com`, like `https://<resourcename>.cognitiveservices.azure.com`, a [custom subdomain](/azure/ai-services/openai/how-to/use-your-data-securely#enabled-custom-subdomain) with `openai.azure.com` must be created first for the Azure OpenAI resource and use `https://<resourcename>.openai.azure.com` instead.  |
 | `apiKey`   |  The secret key used to access the model. If you provide a key, leave `authIdentity` empty. If you set both the `apiKey` and `authIdentity`, the `apiKey` is used on the connection. |
 | `deploymentId`   | The name of the deployed Azure OpenAI embedding model. The model should be an embedding model, such as text-embedding-ada-002. See the [List of Azure OpenAI models](/azure/ai-services/openai/concepts/models) for supported models.|
-| `authIdentity`   | A user-managed identity used by the search service for connecting to Azure OpenAI. You can use either a [system or user managed identity](search-howto-managed-identities-data-sources.md). To use a system manged identity, leave `apiKey` and `authIdentity` blank. The system-managed identity is used automatically. A managed identity must have [Cognitive Services OpenAI User](/azure/ai-services/openai/how-to/role-based-access-control#azure-openai-roles) permissions to send text to Azure OpenAI. |
+| `authIdentity`   | A user-managed identity used by the search service for connecting to Azure OpenAI. You can use either a [system or user managed identity](search-howto-managed-identities-data-sources.md). To use a system managed identity, leave `apiKey` and `authIdentity` blank. The system-managed identity is used automatically. A managed identity must have [Cognitive Services OpenAI User](/azure/ai-services/openai/how-to/role-based-access-control#azure-openai-roles) permissions to send text to Azure OpenAI. |
 | `modelName` | This property is required if your skillset is created using the 2024-05-01-preview or 2024-07-01 REST API. Set this property to the deployment name of an Azure OpenAI embedding model deployed on the provider specified through `resourceUri` and identified through `deploymentId`. Currently, the supported values are `text-embedding-ada-002`, `text-embedding-3-large`, and `text-embedding-3-small`.  |
 | `dimensions` | Optional, starting in the 2024-05-01-preview REST API, the dimensions of embeddings that you would like to generate, assuming the model supports a range of dimensions. Supported ranges are listed below, and currently only apply to the text-embedding-3 model series. The default is the maximum dimensions for each model. For skillsets created using earlier REST API versions dating back to the 2023-10-01-preview, dimensions are fixed at 1536. When setting the dimensions property on a skill, make sure to set the `dimensions` property on the [vector field definition](vector-search-how-to-create-index.md#add-a-vector-field-to-the-fields-collection) to the same value. |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "authIdentityパラメーターの説明を更新"
}
```

### Explanation
この変更は、`cognitive-search-skill-azure-openai-embedding.md`ファイル内の`authIdentity`パラメーターの説明を微調整したものです。具体的には、ユーザー管理のアイデンティティがAzure OpenAIに接続するためにどのように使用されるかの情報がより明確になりました。さらに、システム管理アイデンティティの使用方法についての指示が保持され、両方の`apiKey`と`authIdentity`が設定された場合にどのように動作するかについても言及されています。この変更は、ユーザーが正確なアイデンティティ管理手法を選択できるようにするために重要です。

## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -227,9 +227,9 @@ with SearchIndexingBufferedSender(endpoint=endpoint, index_name=index_name, cred
 print(f"Documents uploaded to index '{index_name}'")
 ```
 
-## Create a search agent
+## Create a knowledge agent
 
-To connect Azure AI Search to your `gpt-4o-mini` deployment and target the `earth_at_night` index at query time, you need a search agent. The following code defines an agent named `earth-search-agent`, which you specified using the `agent_name` variable in a previous section.
+To connect Azure AI Search to your `gpt-4o-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. The following code defines a knowledge agent named `earth-search-agent`, which you specified using the `agent_name` variable in a previous section.
 
 To ensure relevant and semantically meaningful responses, `default_reranker_threshold` is set to exclude responses with a reranker score of `2.5` or lower.
 
@@ -261,7 +261,7 @@ print(f"Knowledge agent '{agent_name}' created or updated successfully")
 
 ## Set up messages
 
-The next step is to define the agent instructions and conversation context using the `messages` array. Each message includes a `role`, such as `user` or `assistant`, and `content` in natural language. A user message represents the query to be processed, while an assistant message guides the agent on how to respond. During the retrieval process, these messages are sent to an LLM to extract relevant responses from indexed documents.
+The next step is to define the knowledge agent instructions and conversation context using the `messages` array. Each message includes a `role`, such as `user` or `assistant`, and `content` in natural language. A user message represents the query to be processed, while an assistant message guides the knowledge agent on how to respond. During the retrieval process, these messages are sent to an LLM to extract relevant responses from indexed documents.
 
 For now, create the following assistant message, which instructs `earth-search-agent` to answer questions about the Earth at night, cite sources using their `ref_id`, and respond with "I don't know" when answers are unavailable.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントの用語を変更"
}
```

### Explanation
この変更は、`agentic-retrieval-python.md`ファイル内で「エージェント」という用語を「ナレッジエージェント」に置き換えたものです。具体的には、Azure AI Searchの構成に関連するセクションでの用語が修正され、エージェントに関連するコードと説明がナレッジエージェントに言及されています。また、エージェントの説明も具体的に明確にされ、関連する文脈やメッセージ指示の設定においても同様の用語の変更が行われています。この変更は、読者にとってエージェントの役割をより効果的に理解できるようにするための重要な改善です。

## articles/search/media/search-how-to-index/edit-index-json.png{#item-5780d0}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "インデックス編集の画像を追加"
}
```

### Explanation
この変更では、`search-how-to-index`に関連する資料に新しい画像ファイル（`edit-index-json.png`）が追加されました。この画像は、インデックスを編集する手順を視覚的に示すためのものであり、ユーザーがAzureの検索機能を使用する際の理解を助けることを目的としています。画像の追加は、文章だけでは伝えきれない情報を補完し、ユーザーにとっての学習体験を向上させる重要な要素です。

## articles/search/media/service-configure-firewall/azure-portal-firewall-all.png{#item-8adb6b}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイアウォール設定画像の更新"
}
```

### Explanation
この変更は、`azure-portal-firewall-all.png`という画像ファイルの内容が更新されたことを示しています。この画像は、Azureポータルにおけるファイアウォールの設定手順を示しており、改善された視覚情報を提供することで、ユーザーがファイアウォール設定をより理解しやすくすることを目的としています。具体的な変更点は記載されていませんが、通常このような更新は、視認性の向上や手順の正確性の確保を目指して行われます。ユーザーにとって役立つリソースであることを意図した重要な改善です。

## articles/search/media/service-configure-firewall/exceptions.png{#item-f019d3}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファイアウォール例外の画像を追加"
}
```

### Explanation
この変更では、`exceptions.png`という新しい画像ファイルが追加されました。この画像は、Azureのファイアウォール設定における例外処理を視覚的に示すことを目的としています。ユーザーは、この画像を参考にすることで、ファイアウォールの例外設定がどのように機能するかを理解しやすくなります。新しいビジュアルリソースの追加は、ドキュメントの有用性を向上させ、特に新しいユーザーや初心者にとっての学習を支援する重要な要素です。この変更により、ユーザー体験が一層向上することが期待されます。

## articles/search/multimodal-search-overview.md{#item-d82192}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn what multimodal search is, how Azure AI Search supports it for text + image content, and where to find detailed concepts, tutorials, and samples.
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 05/12/2025
+ms.date: 05/19/2025
 author: gmndrg
 ms.author: gimondra
 ---
@@ -28,6 +28,9 @@ Azure AI Search simplifies the construction of a multimodal pipeline through a g
 The functionality behind the **Import and vectorize data** wizard's multimodality option is powered by managed, configurable AI skills and the Azure Search knowledge store:
 
 + [Document Intelligence layout skill](cognitive-search-skill-document-intelligence-layout.md) and [document extraction skill](cognitive-search-skill-document-extraction.md) obtain page text, inline images, and structural metadata. The Document Extraction skill doesn't support polygon extraction or page number extraction. Also, the range of supported file types may vary. To ensure optimal alignment with your specific use case, check each skill documentation for detailed information on compatibility and capabilities.
+The native document extraction mechanisms (document layout or document extraction skills) don't support either table extraction or the preservation of their structure. To extract tables and retain their structure, you can:
+  1. Build a [custom Web API skill](cognitive-search-custom-skill-web-api.md).
+  1. Use this skill to call the [Azure AI Content Understanding service](/azure/ai-services/content-understanding/tutorial/build-rag-solution), which supports content extraction, including tables.
 + [Split skill](cognitive-search-skill-textsplit.md) chunks the extracted text for utilization in the remaining pipeline functionality (such as embedding skills). 
 + [Gen AI prompt skill](cognitive-search-skill-genai-prompt.md) verbalizes images, producing concise natural-language descriptions suitable for text search and embedding using a Large Language Model (LLM). 
 + Text/image (or multimodal) embedding skills create embeddings for text and images, enabling similarity and hybrid retrieval. You can call [Azure OpenAI](cognitive-search-skill-azure-openai-embedding.md), [AI Foundry](cognitive-search-aml-skill.md), or [AI Vision](cognitive-search-skill-vision-vectorize.md) embedding models natively.
@@ -39,7 +42,9 @@ A multimodal pipeline begins by cracking each source document into chunks of tex
 
 | Characteristic | Document Intelligence layout skill | Document extraction skill |
 |----------------|------------------------------------|---------------------------|
-| Location metadata extraction (page, bounding polygon) | Yes | No |
+| Text location metadata extraction (page, bounding polygon) | Yes | No |
+| Image location metadata extraction (page, bounding polygon) | Yes | Yes |
+| Location metadata extraction based on file type  | Multiple file support according to [Azure AI Document Intelligence layout model (preview)](/azure/ai-services/document-intelligence/prebuilt/layout)  | PDF only |
 | Data-extraction billing | Billed according to [Document Intelligence layout-model pricing](https://azure.microsoft.com/pricing/details/ai-document-intelligence/). | Image extraction is billed as outlined in the [Azure AI Search pricing page](https://azure.microsoft.com/pricing/details/search/). |
 | Recommended scenarios | RAG pipelines and agent workflows that need precise page numbers, on-page highlights, or diagram overlays in client apps. | Rapid prototyping or production pipelines where the exact position or detailed layout information isn't required. |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダル検索概説の内容更新"
}
```

### Explanation
この変更では、`multimodal-search-overview.md`というマルチモーダル検索に関する文書が更新されています。具体的には、日付の修正や、新たに追加されたコンテンツが含まれています。主な追加内容には、ドキュメントインテリジェンスのレイアウトスキルとドキュメント抽出スキルについての詳細な情報が盛り込まれており、それらの機能や特性がより明確に説明されています。また、テーブル抽出機能の制約についての情報も追加されており、ユーザーがどのようにして最適な結果を得られるかについての指針が示されています。この更新は、ユーザーがマルチモーダル検索機能の使用を理解し、より効果的に活用できるようにするための重要な改善です。

## articles/search/search-agentic-retrieval-concept.md{#item-797a22}

<details>
<summary>Diff</summary>
````diff
@@ -16,9 +16,9 @@ ms.date: 05/19/2025
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-In Azure AI Search, *agentic retrieval* is a new parallel query processing architecture that incorporates user conversation history and Azure OpenAI models to plan, retrieve and synthesize queries for improved results. It produces high-quality grounding data for custom chat and generative AI solutions that include agents.
+In Azure AI Search, *agentic retrieval* is a new parallel query processing architecture that incorporates user conversation history and Azure OpenAI models to plan, retrieve and synthesize queries for improved results. It produces high-quality grounding data for custom chat and generative AI solutions that include knowledge agents.
 
-Programmatically, agentic retrieval is supported through a new Knowledge Agents object (also known as a search agent) in the 2025-05-01-preview data plane REST API and in Azure SDK prerelease packages that provide the feature. An agent's retrieval response is designed for downstream consumption by other agents and chat apps.
+Programmatically, agentic retrieval is supported through a new Knowledge Agents object in the 2025-05-01-preview data plane REST API and in Azure SDK prerelease packages that provide the feature. A knowledge agent's retrieval response is designed for downstream consumption by other agents and chat apps.
 
 ## Why use agentic retrieval
 
@@ -54,9 +54,9 @@ Agentic retrieval has these components:
 
 | Component | Resource | Usage |
 |-----------|----------|-------|
-| LLM (gpt-4o and gpt-4.1 series) | Azure OpenAI | An LLM has two functions. First, it formulates subqueries for the query plan and sends it back to the search agent. Second, after the query executes, the LLM receives grounding data from the query response and uses it for answer formulation. |
+| LLM (gpt-4o and gpt-4.1 series) | Azure OpenAI | An LLM has two functions. First, it formulates subqueries for the query plan and sends it back to the knowledge agent. Second, after the query executes, the LLM receives grounding data from the query response and uses it for answer formulation. |
 | Search index | Azure AI Search | Contains plain text and vector content, a semantic configuration, and other elements as needed. |
-| Search agent | Azure AI Search | Connects to your LLM, providing parameters and inputs to build a query plan. |
+| Knowledge agent | Azure AI Search | Connects to your LLM, providing parameters and inputs to build a query plan. |
 | Retrieval engine | Azure AI Search | Executes on the LLM-generated query plan and other parameters, returning a rich response that includes content and query plan metadata. Queries are keyword, vector, and hybrid. Results are merged and ranked. |
 | Semantic ranker | Azure AI Search | Provides L2 reranking, promoting the most relevant matches. Semantic ranker is required for agentic retrieval. |
 
@@ -65,12 +65,12 @@ Your solution should include a tool or app that drives the pipeline. An agentic
 <!-- Insert multiquery pipeline diagram here -->
 Agentic retrieval has these processes:
 
-+ Requests for agentic retrieval are initiated by calls to an agent on Azure AI Search.
-+ Agents connect to an LLM and provide conversation history as input. How much history is configurable by the number of messages you provide.
++ Requests for agentic retrieval are initiated by calls to a knowledge agent on Azure AI Search.
++ Knowledge agents connect to an LLM and provide conversation history as input. How much history is configurable by the number of messages you provide.
 + LLMs look at the conversation and determine whether to break it up into subqueries. The number of subqueries depends on what the LLM decides and whether the `maxDocsForReranker` parameter is higher than 50. A new subquery is defined for each 50-document batch sent to semantic ranker.
 + Subqueries execute simultaneously on Azure AI Search and generate structured results and extracted references.
 + Results are ranked and merged.
-+ Agent responses are formulated and returned as a three-part response consisting of a unified result (a long string), a reference array, and an activities array that enumerates all operations.
++ Knowledge agent responses are formulated and returned as a three-part response consisting of a unified result (a long string), a reference array, and an activities array that enumerates all operations.
 
 Your search index determines query execution and any optimizations that occur during query execution. This includes your semantic configuration, as well as optional scoring profiles, synonym maps, analyzers, and normalizers (if you add filters).
 
@@ -80,7 +80,7 @@ Agentic retrieval is available in [all regions that provide semantic ranker](sea
 
 Billing for agentic retrieval has two parts:
 
-+ Billing for query planning is pay-as-you-go in Azure OpenAI. It's token based for both input and output tokens. The model you assign to the agent is the one charged for token usage. For example, if you use gpt-4o, the token charge appears in the bill for gpt-4o.
++ Billing for query planning is pay-as-you-go in Azure OpenAI. It's token based for both input and output tokens. The model you assign to the knowledge agent is the one charged for token usage. For example, if you use gpt-4o, the token charge appears in the bill for gpt-4o.
 
 + Billing for semantic ranking during query execution. Billing is suspended during the initial roll-out phase but then transitions to pay-as-you-go on the Azure AI Search side through the semantic ranker. Semantic ranker, which is a premium billable feature, is an integral part of agentic retrieval. You're charged on the Azure AI Search side for token inputs to the semantic ranking models.
 
@@ -154,11 +154,11 @@ Choose any of these options for your next step.
 
 + How-to guides for a focused look at development tasks:
 
-  + [Create an agent](search-agentic-retrieval-how-to-create.md)
-  + [Use an agent to retrieve data](search-agentic-retrieval-how-to-retrieve.md)
+  + [Create a knowledge agent](search-agentic-retrieval-how-to-create.md)
+  + [Use a knowledge agent to retrieve data](search-agentic-retrieval-how-to-retrieve.md)
   + [Build an agent-to-agent retrieval solution](search-agentic-retrieval-how-to-pipeline.md).
 
-+ REST API reference, [Agents](/rest/api/searchservice/knowledge-agents?view=rest-searchservice-2025-05-01-preview&preserve-view=true) and [retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
++ REST API reference, [Knowledge Agents](/rest/api/searchservice/knowledge-agents?view=rest-searchservice-2025-05-01-preview&preserve-view=true) and [Knowledge Retrieval](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
 
 + [Azure OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo), updated to use agentic retrieval.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルの概念に関する更新"
}
```

### Explanation
この変更では、`search-agentic-retrieval-concept.md`という文書が修正され、エージェンティックリトリーバルに関する定義や使用方法が明確化されています。主な修正点としては、「エージェント」という用語が「ナレッジエージェント」に置き換えられ、ドキュメント全体でその一貫性が保たれています。この変更により、ドキュメントがより正確で理解しやすくなり、ユーザーがエージェンティックリトリーバルの機能や実装方法についての理解を深めることができます。

具体的には、エージェンティックリトリーバルのアーキテクチャ、プロセス、コンポーネントに関する説明が更新され、ナレッジエージェントがどのように動作するかや、Azure OpenAIとの連携についても詳述されています。これにより、ユーザーがエージェンティックリトリーバルを効果的に利用できるようになることを目的とした重要な情報が提供されています。また、FAQセクションやAPIリファレンスのリンクも整備され、実践的な情報へのアクセスが容易になっています。

## articles/search/search-agentic-retrieval-how-to-create.md{#item-310fbe}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: Create an agent
+title: Create a knowledge agent
 titleSuffix: Azure AI Search
-description: Learn how to create an agent for agentic retrieval workloads in Azure AI Search.
+description: Learn how to create a knowledge agent for agentic retrieval workloads in Azure AI Search.
 
 manager: nitinme
 author: HeidiSteen
@@ -11,13 +11,13 @@ ms.topic: how-to
 ms.date: 05/05/2025
 ---
 
-# Create an agent in Azure AI Search
+# Create a knowledge agent in Azure AI Search
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-In Azure AI Search, an *agent* is a top-level resource representing a connection to a conversational language model for use in agentic retrieval workloads. It specifies a model that provides reasoning capabilities, and it identifies the search index used at query time.
+In Azure AI Search, a *knowledge agent* is a top-level resource representing a connection to a conversational language model for use in agentic retrieval workloads. It specifies a model that provides reasoning capabilities, and it identifies the search index used at query time.
 
-After you can create an agent, you can update its properties at any time. If the agent is in use, updates take effect on the next job.
+After you can create a knowledge agent, you can update its properties at any time. If the knowledge agent is in use, updates take effect on the next job.
 
 ## Prerequisites
 
@@ -27,11 +27,11 @@ After you can create an agent, you can update its properties at any time. If the
 
 + Azure AI Search, in any [region that provides semantic ranker](search-region-support.md), on basic tier and above. Your search service must have a [managed identity](search-howto-managed-identities-data-sources.md) for role-based access to a chat model.
 
-+ Permission requirements on Azure AI Search. An **Owner/Contributor** or **Search Service Contributor** can create and manage an agent. **Search Index Data Contributor** uploads and indexes document. **Search Index Data Reader** runs queries. Instructions are provided in this article.
++ Permission requirements on Azure AI Search. An **Owner/Contributor** or **Search Service Contributor** can create and manage a knowledge agent. **Search Index Data Contributor** uploads and indexes document. **Search Index Data Reader** runs queries. Instructions are provided in this article.
 
 + A search index containing plain text or vectors. The index must [meet requirements for agentic retrieval](search-agentic-retrieval-how-to-index.md), including a [semantic configuration](semantic-how-to-configure.md) with the `defaultConfiguration` specified.
 
-+ API requirements. To create or use an agent, use 2025-05-01-preview data plane REST API or a prerelease package of an Azure SDK that provides Agent APIs.
++ API requirements. To create or use a knowledge agent, use 2025-05-01-preview data plane REST API or a prerelease package of an Azure SDK that provides knowledge agent APIs.
 
 To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending REST API calls to Azure AI Search. There's no portal support at this time.
 
@@ -100,31 +100,31 @@ You can use API keys if you don't have permission to create role assignments.
    api-key: {{search-api-key}}
    ```
 
-## Check for existing agents
+## Check for existing knowledge agents
 
-The following request lists agents by name. Within the agents collection, all agents must be uniquely named. It's helpful for knowing about existing agents for reuse or  naming purposes.
+The following request lists knowledge agents by name. Within the knowledge agents collection, all knowledge agents must be uniquely named. It's helpful for knowing about existing knowledge agents for reuse or  naming purposes.
 
 <!-- ### [**REST APIs**](#tab/rest-get) -->
 
 ```http
-# List Agents
+# List knowledge agents
 GET https://{{search-url}}/agents?api-version=2025-05-01-preview
 api-key: {{search-api-key}}
 ```
 
 You can also return a single agent by name.
 
 ```http
-# Get Agent
+# Get knowledge agent
 GET https://{{search-url}}/agents/{{agent-name}}?api-version=2025-05-01-preview
 api-key: {{search-api-key}}
 ```
 
 <!-- --- -->
 
-## Create an agent
+## Create a knowledge agent
 
-An agent represents a connection to a model that you've deployed. Parameters on the model establish the connection.
+A knowledge agent represents a connection to a model that you've deployed. Parameters on the model establish the connection.
 
 <!-- ### [**REST APIs**](#tab/rest-create) -->
 
@@ -138,7 +138,7 @@ To create an agent, use the 2025-05-01-preview data plane REST API or an Azure S
 @model-provider-url=<YOUR AZURE OPENAI RESOURCE URI>
 @model-api-key=<YOUR AZURE OPENAI API KEY>
 
-# Create Agent
+# Create knowledge agent
 PUT https://{{search-url}}/agents/{{agent-name}}?api-version=2025-05-01-preview
 api-key: {{search-api-key}}
 Content-Type: application/json
@@ -174,9 +174,9 @@ Content-Type: application/json
 
 **Key points**:
 
-+ `name` must be unique within the agents collection it must adhere to [naming rules](/rest/api/searchservice/naming-rules) for objects on Azure AI Search.
++ `name` must be unique within the knowledge agents collection it must adhere to [naming rules](/rest/api/searchservice/naming-rules) for objects on Azure AI Search.
 
-+ `targetIndexes` is required for agent creation. It lists the search indexes that can use the agent. Currently in this preview release, the `targetIndexes` array can contain only one index. *It must have a default semantic configuration* (`defaultConfiguration`). For more information, see [Design an index for agentic retrieval](search-agentic-retrieval-how-to-index.md).
++ `targetIndexes` is required for knowledge agent creation. It lists the search indexes that can use the knowledge agent. Currently in this preview release, the `targetIndexes` array can contain only one index. *It must have a default semantic configuration* (`defaultConfiguration`). For more information, see [Design an index for agentic retrieval](search-agentic-retrieval-how-to-index.md).
 
     ```json
     "semantic": {
@@ -204,9 +204,9 @@ Content-Type: application/json
 
 <!-- --- -->
 
-## Confirm agent operations
+## Confirm knowledge agent operations
 
-Call the **retrieve** action on the agent object to confirm the model connection and return a response. Use the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API or an Azure SDK prerelease package that provides equivalent functionality for this task.
+Call the **retrieve** action on the knowledge agent object to confirm the model connection and return a response. Use the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API or an Azure SDK prerelease package that provides equivalent functionality for this task.
 
 Replace "What are my vision benefits?" with a query string that's valid for your search index.
 
@@ -243,7 +243,7 @@ Content-Type: application/json
 }
 ```
 
-For more information about the **retrieve** API and the shape of the response, see [Retrieve data using an agent in Azure AI Search](search-agentic-retrieval-how-to-retrieve.md).
+For more information about the **retrieve** API and the shape of the response, see [Retrieve data using a knowledge agent in Azure AI Search](search-agentic-retrieval-how-to-retrieve.md).
 
 ## Delete an agent
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジエージェント作成に関するガイドの更新"
}
```

### Explanation
この変更では、`search-agentic-retrieval-how-to-create.md`という文書が修正され、エージェンティックリトリーバルにおける「エージェント」という用語が「ナレッジエージェント」に置き換わり、文書全体の一貫性が向上しています。主な変更点としては、タイトルや説明文、各セクションにおけるエージェントの定義が更新され、ナレッジエージェントがどのようにAzure AI Searchで利用されるかが明確に述べられています。

具体的には、ナレッジエージェントの作成方法、権限要件、API要件、既存のナレッジエージェントの確認方法、ナレッジエージェントの運用確認、削除方法など、全体にわたって用語が統一されています。この変更により、ナレッジエージェントに関する情報がより明確で理解しやすくなっており、Azure AI Searchを用いるユーザーがこの機能をより効果的に活用できるようになります。ドキュメントが最新の仕様に合わせて更新されたことで、ユーザーがナレッジエージェントを作成し、操作する際の手続きが容易になります。

## articles/search/search-agentic-retrieval-how-to-pipeline.md{#item-1ad1c3}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.date: 05/10/2025
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-This article describes an approach or pattern for building a solution that uses Azure AI Search for data retrieval and how to integrate the retrieval into a custom solution that includes Azure AI Agent.
+This article describes an approach or pattern for building a solution that uses Azure AI Search for knowledge retrieval, and how to integrate knowledge retrieval into a custom solution that includes Azure AI Agent.
 
 This article supports the [agentic-retrieval-pipeline-example](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/agentic-retrieval-pipeline-example) Python sample on GitHub.
 
@@ -47,7 +47,7 @@ Use Azure OpenAI or an equivalent open source model:
 
 Development tasks on the Azure AI Search side include:
 
-+ Create a search agent on Azure AI Search that maps to your deployed model in Azure AI Foundry Model.
++ Create a knowledge agent on Azure AI Search that maps to your deployed model in Azure AI Foundry Model.
 + Call the retriever and provide a query, conversation, and override parameters.
 + Parse the response for the parts you want to include in your chat application. For many scenarios, just the content portion of the response is sufficient. 
 
@@ -101,7 +101,7 @@ If you don't have an Azure OpenAI resource in your Foundry project, revisit the
 
 ### Add an agentic retrieval tool to AI Agent
 
-An end-to-end pipeline needs an orchestration mechanism for coordinating calls to the retriever and agent. You can use a [tool](/azure/ai-services/agents/how-to/tools/function-calling) for this task. The tool calls the Azure AI Search knowledge retrieval client and the Azure AI agent, and it drives the conversations with the user.
+An end-to-end pipeline needs an orchestration mechanism for coordinating calls to the retriever and knowledge agent. You can use a [tool](/azure/ai-services/agents/how-to/tools/function-calling) for this task. The tool calls the Azure AI Search knowledge retrieval client and the Azure AI agent, and it drives the conversations with the user.
 
 ## How to design a prompt
 
@@ -135,7 +135,7 @@ def agentic_retrieval() -> str:
     return retrieval_result.response[0].content[0].text
 ```
 
-To provide instructions used for building the query plan and the subqueries used to get the grounding data, set the message in the search agent:
+To provide instructions used for building the query plan and the subqueries used to get the grounding data, set the message in the knowledge agent:
 
 ```python
 project_client = AIProjectClient.from_connection_string(project_conn_str, credential=credential)
@@ -160,15 +160,15 @@ The LLM determines the quantity of subqueries based on these factors:
 + Chat history
 + Semantic ranker input constraints
 
-As the developer, the best way to control the number of subqueries is by setting the `defaultMaxDocsForReranker` in either the agent definition or as an override on the retrieve action. 
+As the developer, the best way to control the number of subqueries is by setting the `defaultMaxDocsForReranker` in either the knowledge agent definition or as an override on the retrieve action. 
 
 The semantic ranker processes up to 50 documents as an input, and the system creates subqueries to accommodate all of the inputs to semantic ranker. For example, if you only wanted two subqueries, you could set `defaultMaxDocsForReranker` to 100 to accommodate all documents in two batches.
 
 The [semantic configuration](semantic-how-to-configure.md) in the index determines whether the input is 50 or not. If the value is less, the query plan specifies however many subqueries are necessary to meet the `defaultMaxDocsForReranker` threshold.
 
 ## Control the number of threads in chat history
 
-An agent object in Azure AI Search acquires chat history through API calls to the Azure Evaluations SDK, which maintains the thread history. You can filter this list to get a subset of the messages, for example, the last five conversation turns.
+A knowledge agent object in Azure AI Search acquires chat history through API calls to the Azure Evaluations SDK, which maintains the thread history. You can filter this list to get a subset of the messages, for example, the last five conversation turns.
 
 ## Control costs and limit operations
 
@@ -180,7 +180,7 @@ Look at output tokens in the [activity array](search-agentic-retrieval-how-to-re
 
 + Use `gpt mini`.
 
-+ Set `maxOutputSize` in the [search agent](search-agentic-retrieval-how-to-create.md) to govern the size of the response, or `maxRuntimeInSeconds` for time-bound processing.
++ Set `maxOutputSize` in the [knowledge agent](search-agentic-retrieval-how-to-create.md) to govern the size of the response, or `maxRuntimeInSeconds` for time-bound processing.
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジリトリーバル用パイプラインの作成に関する更新"
}
```

### Explanation
この変更では、`search-agentic-retrieval-how-to-pipeline.md`という文書が修正され、エージェンティックリトリーバルに関する内容が「エージェント」から「ナレッジエージェント」に変更されています。この用語の統一により、文書全体の一貫性が向上し、ユーザーが理解しやすくなっています。

主な変更点としては、ナレッジリトリーバルソリューションの構築方法や、ナレッジエージェントとの統合方法が説明されています。また、ナレッジエージェントの使用を指示する部分、例えばエージェントからナレッジエージェントへの呼びかけや、呼び出し時のパラメーター設定方法が明確にされており、Azure AI Searchとの連携が強化されています。

さらに、開発者向けのガイダンスでは、ナレッジエージェントの定義やその操作に関する情報が提供され、ユーザーが効率的にナレッジリトリーバルの機能を活用できるよう、さまざまなプロンプトや設定方法が詳述されています。これにより、Azure AI Searchを使用したカスタムソリューションの開発が促進されることが期待されます。

## articles/search/search-agentic-retrieval-how-to-retrieve.md{#item-5f7fc0}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Use an agent to retrieve data
+title: Use a knowledge agent to retrieve data
 titleSuffix: Azure AI Search
 description: Set up a retrieval route for agentic retrieval workloads in Azure AI Search.
 
@@ -11,13 +11,13 @@ ms.topic: how-to
 ms.date: 05/05/2025
 ---
 
-# Retrieve data using an agent in Azure AI Search
+# Retrieve data using a knowledge agent in Azure AI Search
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
 In Azure AI Search, *agentic retrieval* is a new parallel query architecture that uses a conversational large language model (LLM) for query planning, generating subqueries that broaden the scope of what's searchable and relevant.
 
-This article explains how to use the [**retrieve** method](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-05-01-preview&preserve-view=true) that invokes an agent and parallel query processing. This article also explains the three components of the retrieval response: 
+This article explains how to use the [**retrieve** method](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-05-01-preview&preserve-view=true) that invokes a knowledge agent and parallel query processing. This article also explains the three components of the retrieval response: 
 
 + *extracted response for the LLM*
 + *referenced results*
@@ -28,17 +28,17 @@ This article explains how to use the [**retrieve** method](/rest/api/searchservi
 
 ## Prerequisites
 
-+ An [agent definition](search-agentic-retrieval-how-to-create.md) that represents a conversational language model.
++ A [knowledge agent definition](search-agentic-retrieval-how-to-create.md) that represents a conversational language model.
 
 + Azure AI Search, in any [region that provides semantic ranker](search-region-support.md), on basic tier and above. Your search service must have a [managed identity](search-howto-managed-identities-data-sources.md) for role-based access to a chat model.
 
-+ API requirements. Use 2025-05-01-preview data plane REST API or a prerelease package of an Azure SDK that provides Agent APIs.
++ API requirements. Use 2025-05-01-preview data plane REST API or a prerelease package of an Azure SDK that provides knowledge agent APIs.
 
 To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending REST API calls to Azure AI Search. There's no portal support at this time.
 
 ## Call the retrieve action
 
-Call the **retrieve** action on the agent object to invoke retrieval and return a response. Use the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API or an Azure SDK prerelease package that provides equivalent functionality for this task.
+Call the **retrieve** action on the knowledge agent object to invoke retrieval and return a response. Use the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API or an Azure SDK prerelease package that provides equivalent functionality for this task.
 
 The input for the retrieval route is chat conversation history in natural language, where the `messages` array contains the conversation.
 
@@ -87,9 +87,9 @@ Content-Type: application/json
 
   + `filterAddOn` lets you set an [OData filter expression](search-filters.md) for keyword or hybrid search.
 
-  + `IncludeReferenceSourceData` is initially set in the agent definition. You can override that setting in the retrieve action to return grounding data in the [references section](#review-the-references-array) of the response.
+  + `IncludeReferenceSourceData` is initially set in the knowledge agent definition. You can override that setting in the retrieve action to return grounding data in the [references section](#review-the-references-array) of the response.
 
-  + `rerankerThreshold` and `maxDocsForReranker` are also initially set in the agent definition as defaults. You can override them in the retrieve action to configure [semantic reranker](semantic-how-to-configure.md), setting minimum thresholds and the maximum number of inputs sent to the reranker.
+  + `rerankerThreshold` and `maxDocsForReranker` are also initially set in the knowledge agent definition as defaults. You can override them in the retrieve action to configure [semantic reranker](semantic-how-to-configure.md), setting minimum thresholds and the maximum number of inputs sent to the reranker.
 
     `rerankerThreshold` is the minimum semantic reranker score that's acceptable for inclusion in a response. [Reranker scores](semantic-search-overview.md#how-ranking-is-scored) range from 1 to 4. Plan on revising this value based on testing and what works for your content.
 
@@ -117,7 +117,7 @@ The body of the response is also structured in the chat message style format. Cu
 
 `content` is a JSON array. It's a single string composed of the most relevant documents (or chunks) found in the search index, given the query and chat history inputs. This array is your grounding data that a conversational language model uses to formulate a response to the user's question.
 
-The `maxOutputSize` property on the agent determines the length of the string. We recommend 5,000 tokens.
+The `maxOutputSize` property on the knowledge agent determines the length of the string. We recommend 5,000 tokens.
 
 Fields in the content `text` response string include the ref_id and semantic configuration fields: `title`, `terms`, `terms`.
 
@@ -216,7 +216,7 @@ Here's an example of the references array.
 <!-- This section is in progress. It needs a code sample for the simple case showing how to pipeline ground data to chat completions and responses -->
 ## Use data for grounding
 
-The `includeReferenceSourceData` parameter tells the search engine to provide grounding data to the search agent.
+The `includeReferenceSourceData` parameter tells the search engine to provide grounding data to the knowledge agent.
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジエージェントを使用したデータ取得に関する更新"
}
```

### Explanation
この変更では、`search-agentic-retrieval-how-to-retrieve.md`という文書が修正され、エージェンティックリトリーバルにおける「エージェント」という用語が「ナレッジエージェント」に変更されています。この更新により、文書内の用語が一貫性を持ち、読者が情報をより理解しやすくなっています。

具体的には、「ナレッジエージェントを使用してデータを取得する方法」について説明が加えられ、その内容には、ナレッジエージェントを介して取得アクションを呼び出す方法、必要な前提条件、API要件、さらにはレスポンスの内容に関する詳細が含まれています。また、重要なパラメーターや設定の初期値についても、ナレッジエージェントに基づく情報に合わせて更新されています。

ナレッジエージェントの利用により、会話の履歴に基づいた自然言語でのクエリ処理が可能となり、結果の構造も改善されています。全体として、文書はナレッジエージェントとその機能に関する理解を深めるための参考資料として強化されており、Azure AI Searchを用いる開発者にとって重要な更新となっています。

## articles/search/search-get-started-agentic-retrieval.md{#item-4a40f4}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: "Quickstart: Agentic Retrieval Using Python or REST APIs"
 titleSuffix: Azure AI Search
-description: Learn how to create a search agent that processes multi-turn conversations, retrieves relevant information from an Azure AI Search index, and extracts answers using an Azure OpenAI chat model.
+description: Learn how to create a knowledge agent that processes multi-turn conversations, retrieves relevant information from an Azure AI Search index, and extracts answers using an Azure OpenAI chat model.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
@@ -33,6 +33,6 @@ In the Azure portal, you can find and manage resources by selecting **All resour
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
-+ [Create a search agent](search-agentic-retrieval-how-to-create.md)
-+ [Use a search agent to retrieve data](search-agentic-retrieval-how-to-retrieve.md)
++ [Create a knowledge agent](search-agentic-retrieval-how-to-create.md)
++ [Use a knowledge agent to retrieve data](search-agentic-retrieval-how-to-retrieve.md)
 + [Build an agent-to-agent retrieval solution](search-agentic-retrieval-how-to-pipeline.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジエージェントを使用したクイックスタートの更新"
}
```

### Explanation
この変更では、`search-get-started-agentic-retrieval.md`という文書の解説文において、「エージェント」という表現から「ナレッジエージェント」への変更が行われました。また、関連コンテンツのリンクも同様に更新され、文中での用語の一貫性が強化されています。

具体的には、ドキュメントの説明部分が「ナレッジエージェントを使用してマルチターン会話を処理し、Azure AI Searchインデックスから関連情報を取得し、Azure OpenAIチャットモデルを使用して回答を抽出する方法を学ぶ」という内容に修正されました。これにより、ナレッジエージェントの機能と目的がより明確になります。

さらに、関連コンテンツセクションでは、「ナレッジエージェントを作成する」や「ナレッジエージェントを使用してデータを取得する」といった新しいリンクが追加され、ユーザーがナレッジエージェントを利用するためのリソースをすぐに見つけられるようになっています。このような更新により、文書全体の整合性が向上し、読者がナレッジエージェントを活用したシステムの設計と実装について理解しやすくなります。

## articles/search/search-how-to-create-search-index.md{#item-c4ff31}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/08/2025
+ms.date: 05/19/2025
 ---
 
 # Create an index in Azure AI Search
@@ -52,6 +52,8 @@ Use this checklist to assist the design decisions for your search index.
 
 1. Review [supported data types](/rest/api/searchservice/supported-data-types). The data type affects how the field is used. For example, numeric content is filterable but not full text searchable. The most common data type is `Edm.String` for searchable text, which is tokenized and queried using the full text search engine. The most common data type for a vector field is `Edm.Single` but you can use other types as well.
 
+1. Provide a description of the index (preview), 4,000 character maximum. This human-readable text is invaluable when a system must access several indexes and make a decision based on the description. Consider a Model Context Protocol (MCP) server that must pick the correct index at run time. The decision can be  based on the description rather than on index name alone. An index Description field is available in the [2025-05-01-preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true), the Azure portal, or a prerelease package of an Azure SDK that provides the feature. For more information, see [Add an index description](search-howto-reindex.md#add-an-index-description-preview).
+
 1. Identify a [document key](#document-keys). A document key is an index requirement. It's a single string field populated from a source data field that contains unique values. For example, if you're indexing from Blob Storage, the metadata storage path is often used as the document key because it uniquely identifies each blob in the container.
 
 1. Identify the fields in your data source that contribute searchable content in the index.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックス作成方法の更新"
}
```

### Explanation
この変更では、`search-how-to-create-search-index.md`という文書が更新され、検索インデックス作成の手順が改善されています。主な変更点は、文中の日付の更新と新しいチェック項目の追加です。

具体的には、記事の日付が「2025年5月8日」から「2025年5月19日」に変更され、最新の情報を反映しています。また、インデックスの説明を提供する新しいステップが追加されました。このステップでは、4,000文字までの説明を記載できることが説明されており、システムがインデックスを選択する際に役立つ情報を提供します。この機能は、[2025-05-01-preview REST API](https://rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true)やAzureポータルで利用可能であることも記載されています。

さらに、ドキュメントキーを特定するための手順も明記され、検索インデックスの作成における重要な要素が強調されています。このような修正により、読者はAzure AI Searchの検索インデックス作成に必要な具体的な情報と手順をより効果的に理解できるようになっています。全体として、文書は実用的なガイドとしての価値を増しています。

## articles/search/search-how-to-index-logic-apps-indexers.md{#item-64a12e}

<details>
<summary>Diff</summary>
````diff
@@ -41,7 +41,7 @@ After the wizard completes, you have the following components:
 | Component | Location | Description |
 |-----------|----------|------------|
 | Search index | Azure AI Search | Contains indexed content from a supported Logic Apps connector. The index schema is a default index created by the wizard. You can add extra elements, such as scoring profile or semantic configuration, but you can't change existing fields. You view, manage, and access the search index on Azure AI Search. |
-| Logic app resource and workflow | Azure Logic Apps | You can view the running workflow, or you can open the designer in Azure Logic Apps to edit the workflow, as you regularly do if you'd started from Azure Logic Apps instead. You can edit and extend the workflow, but exercise caution so as to not break the indexing pipeline. |
+| Logic app resource and workflow | Azure Logic Apps | You can view the running workflow, or you can open the designer in Azure Logic Apps to edit the workflow, as you regularly do if you'd started from Azure Logic Apps instead. You can edit and extend the workflow, but exercise caution so as to not break the indexing pipeline. The workflow created by the wizard uses the **Consumption** hosting option. |
 | Logic app templates | Azure Logic Apps | Up to two templates created per workflow: one for on-demand indexing, and a second template for scheduled indexing. You can modify the indexing schedule in the **Index multiple documents** step of the workflow. |
 
 ## Prerequisites
@@ -101,6 +101,7 @@ Currently, the public preview has these limitations:
 + Vectorization supports text embedding only.
 + Deletion detection isn't supported. You must manually [delete orphaned documents](search-howto-reindex.md#delete-orphan-documents) from the index.
 + Duplicate documents in the search index are a known issue in this preview. Consider deleting objects and starting over if this becomes an issue.
++ No support for private endpoints in the logic app workflow created by the portal wizard. The workflow is hosted using the [**Consumption** hosting option](/azure/logic-apps/single-tenant-overview-compare) and is subject to its constraints. To use the **Standard** hosting option, use a programmatic approach to creating the workflow. Use the [2025-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) or a prerelease Azure SDK package that provides the feature.
 
 ## Create a logic app workflow
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Logic Appsインデクサーの更新"
}
```

### Explanation
この変更では、`search-how-to-index-logic-apps-indexers.md`文書の内容が更新され、Logic Appsを使用したインデクサーに関する情報が強化されています。主な変更点は、Logic Appリソースとワークフローの説明の一部が拡充されたことと、プレビュー版の制約に関する新しい情報の追加です。

具体的には、Logic Appリソースとワークフローに関する記述において、ウィザードによって作成されたワークフローが「**Consumption**ホスティングオプション」を使用していることが明確にされ、これはその制約に従うことを示唆しています。これにより、ユーザーは作成されるワークフローのホスティング方法についての理解を深めることができます。

また、プレビュー版における制約として、「ポータルウィザードによって作成されたLogic Appワークフローにはプライベートエンドポイントのサポートがない」との情報が追加されました。この点は、ユーザーが特定のホスティングオプションの制約を認識し、適切なアプローチを取れるようにするために重要です。

全体として、これらの更新により、Logic Appsを使用してインデックスを作成する際の手続きや注意点がより明確になり、ユーザーがシステムを効果的に利用できるように助けています。

## articles/search/search-howto-index-one-to-many-blobs.md{#item-04ada2}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 01/18/2025
+ms.date: 05/19/2025
 ---
 
 # Indexing blobs and files to produce multiple search documents
@@ -24,11 +24,12 @@ When you use any of these parsing modes, the new search documents that emerge mu
 
 To address this problem, the blob indexer generates an `AzureSearch_DocumentKey` that uniquely identifies each child search document created from the single blob parent. This article explains how this feature works.
 
+
 ## One-to-many document key
 
-Each document in an index is uniquely identified by a document key. When no parsing mode is specified, and if there's no [explicit field mapping](search-indexer-field-mappings.md) in the indexer definition for the search document key, the blob indexer automatically maps the `metadata_storage_path property` as the document key. This default mapping ensures that each blob appears as a distinct search document, and it saves you the step of having to create this field mapping yourself (normally, only fields having identical names and types are automatically mapped).
+A document key uniquely identifies each document in an index. When no parsing mode is specified, and if there's no [explicit field mapping](search-indexer-field-mappings.md) in the indexer definition for the search document key, the blob indexer automatically maps the `metadata_storage_path property` as the document key. This default mapping ensures that each blob appears as a distinct search document. It also eliminates the need for you to manually create this field mapping. Normally, fields with identical names and types are the only ones mapped automatically.
 
-In a one-to-many search document scenario, an implicit document key based on `metadata_storage_path property` isn't possible. As a workaround, Azure AI Search can generate a document key for each individual entity extracted from a blob. The generated key is named `AzureSearch_DocumentKey` and it's added to each search document. The indexer keeps track of the "many documents" created from each blob, and can target updates to the search index when source data changes over time.
+In a one-to-many search document scenario, an implicit document key based on `metadata_storage_path property` isn't possible. As a workaround, Azure AI Search can generate a document key for each individual entity extracted from a blob. The system generates a key called `AzureSearch_DocumentKey` and adds it to each search document. The indexer keeps track of the "many documents" created from each blob, and can target updates to the search index when source data changes over time.
 
 By default, when no explicit field mappings for the key index field are specified, the `AzureSearch_DocumentKey` is mapped to it, using the `base64Encode` field-mapping function.
 
@@ -132,9 +133,13 @@ id, temperature, pressure, timestamp
 2, 120, 3,"2022-05-11T00:00:00Z" 
 ```
 
-Notice that each document contains the `id` field, which is defined as the `key` field in the index. In such a case, even though a document-unique `AzureSearch_DocumentKey` is generated, it isn't used as the "key" for the document. Rather, the value of the `id` field is mapped to the `key` field
+Each document contains the `id` field, which is defined as the `key` field in the index. In this situation, the system generates a unique AzureSearch_DocumentKey` for the document, but it isn't used as the "key." Instead, the value of the `id` field is mapped to the `key` field.
+
+Similar to the previous example, this mapping doesn't result in four documents showing up in the index because the `id` field isn't unique _across blobs_. When this situation occurs, any JSON entry that specifies an `id` causes a merge with the existing document instead of uploading a new one. The index then reflects the latest state of the entry with the specified `id`.
+
+## Limitations
 
-Similar to the previous example, this mapping doesn't result in four documents showing up in the index because the `id` field isn't unique _across blobs_. When this is the case, any json entry that specifies an `id` results in a merge on the existing document instead of an upload of a new document, and the state of the index reflects the latest read entry with the specified `id`.
+When a document entry in the index is created from a line in a file, as explained in this article, deleting that line from the file does'nt automatically remove the corresponding entry from the index. To delete the document entry, you must manually submit a deletion request to the index using the [REST API deletion operation](/rest/api/searchservice/addupdate-or-delete-documents).
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "一対多のBlobインデックス作成方法の更新"
}
```

### Explanation
この変更では、`search-howto-index-one-to-many-blobs.md`文書が更新され、Blobからの一対多の検索ドキュメント作成に関する説明が強化されています。今回の変更には、日付の更新、記述の明確化、新しいセクションの追加が含まれています。

主な内容として、Blobインデクサーが各子検索ドキュメントに対して一意のドキュメントキーである`AzureSearch_DocumentKey`を生成する方法が詳しく説明されています。従来の記述がより明確になり、デフォルトマッピングやドキュメントキーの自動生成に関する情報が追加されています。また、新たに「制限」セクションが導入され、インデックス内のエントリを手動で削除する必要があることや、`id`フィールドがユニークでない場合に起こりうるマージの挙動について説明されています。

これにより、ユーザーはBlobのインデクサーとそれが生成する検索ドキュメントに関する理解を深め、自身のインデックスの管理における制約や注意点を把握できるようになります。全体として、情報が整理され、実行可能な指針が提供されているため、実務における利用がしやすくなっています。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 04/28/2025
+ms.date: 05/19/2025
 ---
 
 # Update or rebuild an index in Azure AI Search
@@ -199,6 +199,7 @@ The index schema defines the physical data structures created on the search serv
 
 The following list enumerates the schema changes that can be introduced seamlessly into an existing index. Generally, the list includes new fields and functionality used during query execution.
 
++ Add an [index description (preview)]()
 + Add a new field
 + Set the `retrievable` attribute on an existing field
 + Update `searchAnalyzer` on a field having an existing `indexAnalyzer`
@@ -253,6 +254,45 @@ When you create the index, physical storage is allocated for each field in the i
 
 To minimize disruption to application code, consider [creating an index alias](search-how-to-alias.md). Application code references the alias, but you can update the name of the index that the alias points to.
 
+## Add an index description (preview)
+
+Beginning with REST API version 2025-05-01-preview, an `indexdescription` is now supported. This human-readable text is invaluable when a system must access several indexes and make a decision based on the description. Consider a Model Context Protocol (MCP) server that must pick the correct index at run time. The decision can be  based on the description rather than on the index name alone.
+
+An index description is a schema update, and you can add it without having to rebuild the entire index.
+
++ String length is 4,000 characters maximum.
++ Content must be human-readable, in Unicode. Your use-case should determine which language to use.
+
+Support for an index description is provided in the preview REST API, the Azure portal, or in a prerelease Azure SDK package that provides the feature.
+
+### [**Azure portal**](#tab/portal)
+
+The Azure portal supports the latest preview API.
+
+1. Sign in to the Azure portal and find your search service.
+
+1. Under **Search management** > **Indexes**, select an index.
+
+1. Select **Edit JSON**.
+
+1. Insert `"indexDescription"`, followed by the description.
+
+   :::image type="content" source="media/search-how-to-index/edit-index-json.png" alt-text="Screenshot of the JSON definition of an index in the Azure portal.":::
+
+1. Save the index.
+
+### [**REST**](#tab/rest)
+
+1. [GET an index definition](/rest/api/searchservice/indexes/get).
+
+1. Copy the JSON.
+
+1. [Formulate an index update PUT request](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) using the preview API, providing the *full* JSON of the existing schema, plus the new description field.
+
+1. To confirm the description, issue another [GET using the 2025-05-01-preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
+
+---
+
 ## Balancing workloads
 
 Indexing doesn't run in the background, but the search service will balance any indexing jobs against ongoing queries. During indexing, you can [monitor query requests](search-monitor-queries.md) in the Azure portal to ensure queries are completing in a timely manner.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスの再構築および更新に関する情報の追加"
}
```

### Explanation
この変更では、`search-howto-reindex.md`文書が修正され、Azure AI Searchのインデックスを更新または再構築する方法に関する情報が拡充されています。主な変更点として、日付の更新と新しい機能「インデックス説明 (プレビュー)」の追加が含まれています。

具体的には、REST APIバージョン2025-05-01-previewから、インデックスに人間が読み取れるテキストとしての説明を追加することができるようになりました。この説明は、システムが複数のインデックスにアクセスして意思決定を行う際に非常に役立ちます。インデックスの説明はスキーマの更新であり、インデックス全体を再構築することなく追加可能です。

また、インデックス説明の追加方法、AzureポータルおよびREST APIを使用した具体的な手順が詳細に説明されています。これにより、ユーザーはインデックスの管理をより効果的に行えるようになります。さらに、文字列の最大長や内容に関する要件についても触れられています。

全体として、この更新はユーザーにとってインデックスに関する理解を深め、具体的な手順を提供することで、実務でのインデックス管理を容易にすることを目的としています。

## articles/search/search-index-access-control-lists-and-rbac-push-api.md{#item-45e71e}

<details>
<summary>Diff</summary>
````diff
@@ -4,19 +4,19 @@ titleSuffix: Azure AI Search
 description: Learn how to use the REST API for indexing documents with ACLs and RBAC metadata.  
 ms.service: azure-ai-search  
 ms.topic: conceptual  
-ms.date: 05/09/2025  
+ms.date: 05/19/2025  
 author: admayber
 ms.author: admayber  
 ---  
 
-# Indexing Access Control Lists (ACLs) and Role-Based Access Control (RBAC) using REST API in Azure AI Search  
+# Indexing Access Control Lists (ACLs) and Role-Based Access Control (RBAC) using REST APIs in Azure AI Search  
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
 Indexing documents, along with their associated [Access Control Lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control) and container [Role-Based Access Control (RBAC) roles](/azure/role-based-access-control/overview), into an Azure AI Search index via the [REST API](/rest/api/searchservice/) offers fine-grained control over the indexing pipeline. This approach enables the inclusion of document entries with precise, document-level permissions directly within the index. This article explains how to use the REST API to index document-level permissions' metadata in Azure AI Search. This process prepares your index to query and enforce end-user permissions.
 
 ## Supported scenarios  
-- Indexing ACLs metadata from [ENTRA-based](/entra/fundamentals/whatis), POSIX-style ACL systems, such as [Azure Data Lake Storage (ADLS) Gen2].(/azure/storage/blobs/data-lake-storage-introduction)
+- Indexing ACLs metadata from [ENTRA-based](/entra/fundamentals/whatis), POSIX-style ACL systems, such as [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/data-lake-storage-introduction)
 - Indexing RBAC container metadata from ADLS Gen2.
 
 ### Limitations
@@ -107,9 +107,9 @@ This example illustrates how the document access rules are resolved based on the
 | 3 | ["none"] | ["group1", "group2"] | Empty | Members of group1 or group2 | |
 | 4 | ["all"] | ["none"] | Empty | Any user | Any querying user matches the ACL filter "all", so all users have access |
 | 5 | ["all"] | ["group1", "group2"] | scope/to/container1 | Any user | Since all users match the "all" filter for userID, the groupID and RBAC filters don't have any impact |
-| 5 | ["user1", "user2"] | ["group1"] | Empty | User1, user2, or any member of group1 | |
-| 5 | ["user1", "user2"] | [] | Empty | User1, user2, or any user with RBAC permissions to container1 | |
+| 6 | ["user1", "user2"] | ["group1"] | Empty | User1, user2, or any member of group1 | |
+| 7 | ["user1", "user2"] | [] | Empty | User1, user2, or any user with RBAC permissions to container1 | |
 
 ## Next steps
-- [How to query the index using end user ENTRA-token to enforce document-level permissions](https://aka.ms/azs-query-preserving-permissions)
+- [How to query the index using end user ENTRA-token to enforce document-level permissions](search-query-access-control-rbac-enforcement.md)
 - [How to index ADLS Gen2 document-level permission information using indexers](tutorial-adls-gen2-indexer-acls.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アクセス制御リストとRBACに関するREST APIのドキュメントの更新"
}
```

### Explanation
この変更では、`search-index-access-control-lists-and-rbac-push-api.md`の内容が更新され、Azure AI Searchにおけるアクセス制御リスト（ACL）とロールベースのアクセス制御（RBAC）を利用したドキュメントのインデックス作成方法に関する情報が改善されています。主な修正内容には、日付の更新、タイトルの微調整、いくつかの表現の修正及びリンクの更新が含まれています。

特に、インデックス作成の際にACLやRBACメタデータをREST APIを通じてどのように取り扱うか、及びこれによる詳細なアクセス制御の実施方法が解説されています。また、ドキュメントへのアクセス権限の管理がどのように行われるかに関する具体的なシナリオが提供されています。

限界に関する部分では、ドキュメントアクセスルールの解決方法についての具体例が明確に示され、RBACの影響についての情報も更新されています。最後に、次のステップとして、エンドユーザーのENTRAトークンを使用してドキュメントレベルの権限を強制するインデックスのクエリ方法に関するリンクが具体的な記事へのリンクに更新されています。

このような更新により、ユーザーはアクセス制御と権限管理に関する最新の情報を得て、より効果的なインデックス管理が可能になるでしょう。

## articles/search/search-query-access-control-rbac-enforcement.md{#item-d24df7}

<details>
<summary>Diff</summary>
````diff
@@ -29,7 +29,8 @@ Azure Data Lake Storage (ADLS) Gen2 provides an access model that makes fine-gra
 
 This section lists the order of operations for ACL enforcement at query time. Operations vary depending on whether you use Azure RBAC scope or Microsoft Entra ID group or user IDs.
 
-### 1. User permissions input  
+### 1. User permissions input
+
 The end-user application sends user permission as part of the search query request. The following table lists the source of the user permissions Azure AI Search uses for ACL enforcement:
 
 | Permission type | Source |
@@ -39,19 +40,41 @@ The end-user application sends user permission as part of the search query reque
 | rbacScope | Permissions the user from `x-ms-query-source-authorization` has on a storage container |
 
 ### 2. Security filter construction
+
 Azure AI Search dynamically constructs security filters based on the user permissions provided. These security filters are automatically appended to any filters that might come in with the query if the index has the permission filter option enabled.
 
-For Azure RBAC, permissions are list of resource ID strings, and there must an Azure role assignment (Storage Blob Data Reader) on the data the source that grants access to the security principal token in the authorization header. The filter excludes documents if there's no role assignment for the principal behind the access token on the request.
+For Azure RBAC, permissions are lists of resource ID strings, and there must be an Azure role assignment (Storage Blob Data Reader) on the data the source that grants access to the security principal token in the authorization header. The filter excludes documents if there's no role assignment for the principal behind the access token on the request.
 
-### 3. Results filtering  
+### 3. Results filtering
+  
 The security filter efficiently matches the userIds, groupIds, and rbacScope from the user against each list of ACLs in every document in the search index to limit the results returned to ones the user has access to. It's important to note that each filter is applied independently and a document is considered authorized if any filter succeeds. For example, if a user has access to a document through userIds but not through groupIds, the document is still considered valid and returned to the user.
 
 ## Limitations
+
 - If ACL evaluation fails (for example, Graph API is unavailable), the service returns **5xx** and does **not** return a partially filtered result set.
 - Document visibility requires both:
   - the calling application’s RBAC role (Authorization header), and  
   - the user identity carried by **x-ms-query-source-authorization**.
 
-## Next steps
-* [How to Index Permission Information](tutorial-adls-gen2-indexer-acls.md) provides a detailed walkthrough of how to set up an index with ACLs using Azure Search indexers.
-* [Indexing ACLs and RBAC using Push API in Azure AI Search](search-index-access-control-lists-and-rbac-push-api.md) provides a walkthrough of how to set up an index with ACLs using the push API.
+## Query example
+
+Here's an example of a query request from [sample code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-ACL). The query token is passed in the request header.
+
+```http
+POST  {{endpoint}}/indexes/stateparks/docs/search?api-version=2025-05-01-preview
+Authorization: Bearer {{search-token}}
+x-ms-query-source-authorization: {{search-token}}
+Content-Type: application/json
+
+{
+    "search": "*",
+    "select": "name,description,location,GroupIds",
+    "orderby": "name asc"
+}
+```
+
+## Related content
+
+- [Tutorial: Index ADLS Gen2 permission metadata](tutorial-adls-gen2-indexer-acls.md) provides a detailed walkthrough of how to set up an index with ACLs using Azure Search indexers.
+
+- [Indexing ACLs and RBAC using Push API in Azure AI Search](search-index-access-control-lists-and-rbac-push-api.md) provides a walkthrough of how to set up an index with ACLs using the push indexing approach with the REST APIs.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACの強制を伴うクエリのアクセス制御に関する文書の更新"
}
```

### Explanation
この変更では、`search-query-access-control-rbac-enforcement.md`の内容が更新され、Azure AI Searchにおけるクエリのアクセス制御およびRBACの強制に関する手続きが明確化されています。主な修正内容には、新しいセクションの追加や文書の構成の変更が含まれています。

変更の中で、ユーザ.permissionの入力に関する説明が追加され、エンドユーザーアプリケーションが検索クエリリクエストの一部としてユーザーの権限を送信する方法が詳述されています。また、セキュリティフィルターの構築についての説明も強化され、Azure RBACを使用する際の要件やフィルター適用のメカニズムがより詳細に説明されています。

結果フィルタリングのセクションでは、ユーザーIDやグループIDを基にドキュメントへのアクセス権限を判断する仕組みが明確になり、どのように適切なドキュメントが返されるかが具体的に記述されています。さらに、アクセス制御リストの評価が失敗した場合の処理に関する制限事項も追加されています。

新しいクエリの例と、そのリクエスト形式が具体的に示され、実際の使い方がより明瞭に理解できるようになりました。最後に、関連コンテンツへのリンクも更新され、ユーザーがACLを持つインデックスを設定する際のリソースが提供されています。

これにより、ユーザーは検索クエリにおけるアクセス制御の実装に関する最新の情報を得ることができ、より効果的にRBACを活用できるようになるでしょう。

## articles/search/search-what-is-an-index.md{#item-5a3344}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 04/14/2025
+ms.date: 05/19/2025
 ---
 
 # Search indexes in Azure AI Search
@@ -35,6 +35,7 @@ The structure of a document is determined by the *index schema*, as illustrated
 ```json
 {
   "name": "name_of_index, unique across the service",
+  "description" : "Health plan coverage for standard and premium plans for Northwind and Contoso employees."
   "fields": [
     {
       "name": "name_of_field",
@@ -50,7 +51,7 @@ The structure of a document is determined by the *index schema*, as illustrated
       "indexAnalyzer": "name_of_indexing_analyzer", (only if 'searchAnalyzer' is set and 'analyzer' is not set)
       "normalizer":  "name_of_normalizer", (applies to fields that are filterable)
       "synonymMaps": "name_of_synonym_map", (optional, only one synonym map per field is currently supported)
-      "dimensions": "number of dimensions used by an emedding models", (applies to vector fields only, of type Collection(Edm.Single))
+      "dimensions": "number of dimensions used by an embedding models", (applies to vector fields only, of type Collection(Edm.Single))
       "vectorSearchProfile": "name_of_vector_profile" (indexes can have many configurations, a field can use just one)
     }
   ],
@@ -187,6 +188,7 @@ You can get hands-on experience creating an index using almost any sample or wal
 But you'll also want to become familiar with methodologies for loading an index with data. Index definition and data import strategies are defined in tandem. The following articles provide more information about creating and loading an index.
 
 + [Create a search index](search-how-to-create-search-index.md)
++ [Update an index](search-howto-reindex.md)
 + [Create a vector store](vector-search-how-to-create-index.md)
 + [Create an index alias](search-how-to-alias.md)
 + [Data import overview](search-what-is-data-import.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスに関する文書の更新"
}
```

### Explanation
この変更では、`search-what-is-an-index.md`の内容が更新され、Azure AI Searchにおける検索インデックスの定義や構造に関する情報が改善されています。主な修正内容には、日付の更新、インデックスの説明の追加、用語の微調整が含まれています。

具体的には、ドキュメントの構造を示すJSONスキーマの例に新たにインデックスの説明フィールドが追加され、ユーザーに対してインデックスがどのような目的で使用されるのかより明確になっています。また、ベクトルフィールドに関連する次元の説明文からスペルミスが修正され、より正確な表現が用いられています。

さらに、検索インデックスの作成や更新に関する新しいリンクが追加され、ユーザーが具体的な手順を学ぶためのリソースが豊富になっています。これにより、インデックスの作成およびデータのインポートに関する理解が深まり、ユーザーはより効果的にAzure AI Searchを活用できるようになります。

この更新により、検索インデックスに関する知識をさらに充実させ、実際の操作に役立つ情報が提供されています。

## articles/search/service-configure-firewall.md{#item-75be3f}

<details>
<summary>Diff</summary>
````diff
@@ -10,12 +10,12 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 04/14/2025
+ms.date: 05/20/2025
 ---
 
 # Configure network access and firewall rules for Azure AI Search
 
-This article explains how to restrict network access to a search service's public endpoint. To block *all* data plane access to the public endpoint, use [private endpoints](service-create-private-endpoint.md) and an Azure virtual network.
+This article explains how to restrict network access to a search service's public endpoint. To block *all* data plane access to the public endpoint, use [private endpoints](service-create-private-endpoint.md) and connect from within an Azure virtual network.
 
 This article assumes the Azure portal for configuring network access options. You can also use the [Management REST API](/rest/api/searchmanagement/), [Azure PowerShell](/powershell/module/az.search), or the [Azure CLI](/cli/azure/search).
 
@@ -34,6 +34,7 @@ If you aren't hosting a public web site, you might want to configure network acc
 There are two mechanisms for restricting access to the public endpoint:
 
 + Inbound rules listing the IP addresses, ranges, or subnets from which requests are admitted
+
 + Exceptions to network rules, where requests are admitted with no checks, as long as the request originates from a [trusted service](#grant-access-to-trusted-azure-services)
 
 Network rules aren't required, but it's a security best practice to add them if you use Azure AI Search for surfacing private or internal corporate content.
@@ -46,7 +47,7 @@ There are a few drawbacks to locking down the public endpoint.
 
 + It takes time to fully identify IP ranges and set up firewalls, and if you're in early stages of proof-of-concept testing and investigation and using sample data, you might want to defer network access controls until you actually need them.
 
-+ Some workflows require access to a public endpoint. Specifically, the [**import wizards**](search-import-data-portal.md) in the Azure portal connect to built-in (hosted) sample data and embedding models over the public endpoint. You can switch to code or script to complete the same tasks when firewall rules in place, but if you want to run the wizards, the public endpoint must be available. For more information, see [Secure connections in the import wizards](search-import-data-portal.md#secure-connections).
++ Some workflows require access to a public endpoint. Specifically, the [**indexing wizards**](search-import-data-portal.md) in the Azure portal connect to built-in (hosted) sample data and embedding models over the public endpoint. You can switch to code or script to complete the same tasks when firewall rules in place, but if you want to run the wizards, the public endpoint must be available. For more information, see [Secure connections in the import wizards](search-import-data-portal.md#secure-connections).
 
 <a id="configure-ip-policy"></a> 
 
@@ -58,21 +59,23 @@ There are a few drawbacks to locking down the public endpoint.
 
 1. Choose **Selected IP addresses**. Avoid the **Disabled** option unless you're configuring a [private endpoint](service-create-private-endpoint.md).
 
-   :::image type="content" source="media/service-configure-firewall/azure-portal-firewall.png" alt-text="Screenshot showing the network access options in the Azure portal.":::
-
-1. More settings become available when you choose this option. 
+   :::image type="content" source="media/service-configure-firewall/azure-portal-firewall.png" alt-text="Screenshot showing the network access options in the Azure portal." lightbox="media/service-configure-firewall/azure-portal-firewall.png" :::
 
-   :::image type="content" source="media/service-configure-firewall/azure-portal-firewall-all.png" alt-text="Screenshot showing how to configure the IP firewall in the Azure portal.":::
+1. Under **IP Firewall**, select **Add your client IP address**. This step creates an inbound rule for the public IP address of your personal device to Azure AI Search. See [Allow access from the Azure portal IP address](#allow-access-from-the-azure-portal-ip-address) for details.
 
-1. Under **IP Firewall**, select **Add your client IP address** to create an inbound rule for the public IP address of your personal device. See [Allow access from the Azure portal IP address](#allow-access-from-the-azure-portal-ip-address) for details.
+   :::image type="content" source="media/service-configure-firewall/azure-portal-firewall-all.png" alt-text="Screenshot showing how to configure the IP firewall in the Azure portal." lightbox="media/service-configure-firewall/azure-portal-firewall-all.png":::
 
 1. Add other client IP addresses for other devices and services that send requests to a search service.
 
-   IP addresses and ranges are in the CIDR format. An example of CIDR notation is 8.8.8.0/24, which represents the IPs that range from 8.8.8.0 to 8.8.8.255.
+   Specify IP addresses and ranges in the CIDR format. An example of CIDR notation is 8.8.8.0/24, which represents the IPs that range from 8.8.8.0 to 8.8.8.255.
 
-   If your search client is a static web app on Azure, see [Inbound and outbound IP addresses in Azure App Service](/azure/app-service/overview-inbound-outbound-ips#find-outbound-ips). For Azure functions, see [IP addresses in Azure Functions](/azure/azure-functions/ip-addresses).
+   To get the public IP addresses of Azure services, see [Azure IP Ranges and Service Tags](https://www.microsoft.com/download/details.aspx?id=56519). If your search client is hosted within an Azure function, see [IP addresses in Azure Functions](/azure/azure-functions/ip-addresses).
 
-1. Under **Exceptions**, select **Allow Azure services on the trusted services list to access this search service**. The trusted service list includes:
+1. Under **Exceptions**, select **Allow Azure services on the trusted services list to access this search service**. 
+ 
+   :::image type="content" source="media/service-configure-firewall/exceptions.png" alt-text="Screenshot showing the exceptions checkbox on the network configuration page." lightbox="media/service-configure-firewall/exceptions.png":::
+
+   The trusted service list includes:
 
    + `Microsoft.CognitiveServices` for Azure OpenAI and Azure AI services
    + `Microsoft.MachineLearningServices` for Azure Machine Learning
@@ -92,9 +95,11 @@ When requests originate from IP addresses that aren't in the allowed list, a gen
 
 ## Allow access from the Azure portal IP address
 
-When IP rules are configured, some features of the Azure portal are disabled. You can view and manage service level information, but portal access to the import wizards, indexes, indexers, and other top-level resources are restricted. 
+The Azure portal has its own connection to Azure AI Search, separate from your local device and browser. If you use the Azure portal to manage your search service, you need to add the portal IP address as described in this section, and your client IP address as described in the previous section.
+
+When IP rules are configured, some features of the Azure portal are disabled. For example, you can view and manage service level information, but portal access to the import wizards, indexes, indexers, and other top-level resources are restricted. 
 
-You can restore portal access to the full range of search service operations by adding the Azure portal IP address.
+You can restore the Azure portal's access to the full range of search service operations by adding the Azure portal IP address to the restricted address range. 
 
 To get the Azure portal's IP address, perform `nslookup` (or `ping`) on:
 
@@ -122,7 +127,7 @@ For ping, the request times out, but the IP address is visible in the response.
 
 A banner informs you that IP rules affect the Azure portal experience. This banner remains visible even after you add the Azure portal's IP address. Remember to wait several minutes for network rules to take effect before testing.
 
-:::image type="content" source="media/service-configure-firewall/restricted-access.png" alt-text="Screenshot showing the restricted access banner.":::
+:::image type="content" source="media/service-configure-firewall/restricted-access.png" alt-text="Screenshot showing the restricted access banner." lightbox="media/service-configure-firewall/restricted-access.png" :::
 
 ## Grant access to trusted Azure services
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのファイアウォール設定に関する文書の更新"
}
```

### Explanation
この変更では、`service-configure-firewall.md`文書が更新され、Azure AI Searchサービスのファイアウォール設定とネットワークアクセスの構成に関する情報が改善されています。主な修正点には、日付の更新、表現の修正、情報の追加が含まれています。

具体的には、ファイアウォール設定に関する説明文において、「Azureバーチャルネットワークに接続する」という具体的な手順が追加され、より明確な指示が提供されています。アクセス制御のメカニズムとして新たにインバウンドルールや例外に関する説明が強化され、ネットワークルール設定の重要性が強調されています。

また、インポートウィザードからインデクシングウィザードへの用語変更が行われており、ユーザー向けの表記が統一されています。エラーメッセージや警告に関する説明がより具体的になり、AzureポータルのIPアドレスを追加する必要がある理由が詳しく説明されています。

新たに追加された画像には、Azureポータルの設定やエラーメッセージの例が含まれており、視覚的に理解を助ける情報が提供されています。これにより、セキュリティ設定やネットワーク構成に関する全体的な理解が向上し、Azure AI Searchを利用する上でのベストプラクティスが強化されています。

この更新により、ユーザーはAzure AI Searchのネットワークアクセス制御を効果的に管理し、セキュリティを強化するための最新のガイドラインを得ることができます。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -373,9 +373,9 @@ items:
           href: cognitive-search-create-custom-skill-example.md
   - name: Agentic retrieval
     items:
-    - name: Create an agent
+    - name: Create a knowledge agent
       href: search-agentic-retrieval-how-to-create.md
-    - name: Use an agent to retrieve data
+    - name: Use a knowledge agent to retrieve data
       href: search-agentic-retrieval-how-to-retrieve.md
     - name: Define an index for agentic retrieval
       href: search-agentic-retrieval-how-to-index.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントによる検索に関する文書のタイトル更新"
}
```

### Explanation
この変更では、`toc.yml`ファイルにおいて、エージェントによる検索に関連する文書のタイトルが更新されました。具体的には、「エージェント」という用語が「ナレッジエージェント」に変更され、より明確で関連性のある表現が用いられています。

変更点は以下の通りです：
- 「Create an agent」というタイトルが「Create a knowledge agent」に変更されました。
- 「Use an agent to retrieve data」というタイトルは「Use a knowledge agent to retrieve data」に修正され、同様にナレッジエージェントについての説明が強調されています。

これにより、ユーザーが文書を参照した際に、ナレッジエージェントに関する具体的な情報を明確に理解できるようになります。また、文書内の一貫性が保たれることで、より良いユーザー体験が提供されます。全体として、検索エージェントに関する情報がより具体的かつ正確になっており、ユーザーが関連するリソースを見つけやすくなっています。

## articles/search/tutorial-adls-gen2-indexer-acls.md{#item-6881a0}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how to index Access Control Lists (ACLs) and Azure Role-Based Access Control (RBAC) scope from ADLS Gen2 and query with permission-filtered results in Azure AI Search.
 ms.service: azure-ai-search  
 ms.topic: tutorial  
-ms.date: 05/08/2025
+ms.date: 05/20/2025
 author: wlifuture
 ms.author: wli
 ---  
@@ -26,7 +26,7 @@ In this tutorial, you learn how to:
 > + Create and run an indexer to ingest permission information into an index from a data source
 > + Search the index you just created
 
-You need a REST client to complete this tutorial. There's no currently no support for ACL indexing in the Azure portal.
+Use a REST client to complete this tutorial and the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) REST API. There's no currently no support for ACL indexing in the Azure portal.
 
 ## Prerequisites
 
@@ -181,3 +181,26 @@ Indexer configuration for permission ingestion is primarily about defining `fiel
 ```
 
 After indexer creation and immediate run, the file content along with permission metadata information are indexed into the index.
+
+## Run a query to check results
+
+Now that documents are loaded, you can issue queries against them by using [Documents - Search Post (REST)](/rest/api/searchservice/documents/search-post).
+
+The URI is extended to include a query input, which is specified by using the `/docs/search` operator. The query token is passed in the request header. For more information, see [Query-Time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md).
+
+```http
+POST  {{endpoint}}/indexes/stateparks/docs/search?api-version=2025-05-01-preview
+Authorization: Bearer {{search-token}}
+x-ms-query-source-authorization: {{search-token}}
+Content-Type: application/json
+
+{
+    "search": "*",
+    "select": "name,description,location,GroupIds",
+    "orderby": "name asc"
+}
+```
+
+## Related content
+
++ [https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-ACL](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-ACL)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ADLS Gen2インデクサーとACLに関するチュートリアルの更新"
}
```

### Explanation
この変更では、`tutorial-adls-gen2-indexer-acls.md`に対して更新が行われ、ADLS Gen2のアクセス制御リスト（ACL）をインデックス化し、Azure AI Searchで権限フィルタリングされた結果をクエリする方法に関する内容が強化されています。主な変更点は以下の通りです：

1. **日付の更新**: 文書の日付が「05/08/2025」から「05/20/2025」に変更され、最新の情報を反映しています。

2. **RESTクライアントの使用についての具体化**: 「RESTクライアントを使用してこのチュートリアルを完了する必要があります。」という記述に「[2025-05-01-preview] REST API」を参照するリンクが追加され、APIのバージョンに関する明確な情報が提供されています。

3. **新しいセクションの追加**: 
   - 「クエリを実行して結果を確認する」という新しいセクションが追加され、ドキュメントに対してクエリを発行する方法が具体的に説明されています。ここでは、使用するHTTPリクエストの例とともに、クエリトークンをリクエストヘッダーに渡す方法が示されています。
   - 「関連コンテンツ」セクションが追加され、ACLに関するGitHubサンプルへのリンクが提供されています。

これらの変更により、許可情報をインデクシングした後に、その結果を確認するプロセスについての理解が容易になり、ユーザーが関連するツールやリソースにアクセスしやすくなっています。また、チュートリアル全体がより具体的で実用的な情報に富むものとなり、ADLS Gen2のインデクサーの利用が促進されます。

## articles/search/vector-search-vectorizer-ai-services-vision.md{#item-942a3e}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,7 @@ Parameters are case-sensitive.
 | `resourceUri` | The URI of the AI Services resource.  |
 | `apiKey`   |  The API key of the AI Services resource. |
 | `modelVersion` | (Required) The model version to be passed to the Azure AI Vision API for generating embeddings. It's important that all embeddings stored in a given index field are generated using the same `modelVersion`. For information about version support for this model refer to [multimodal embeddings](/azure/ai-services/computer-vision/concept-image-retrieval#what-are-vector-embeddings). |
-| `authIdentity`   | A user-managed identity used by the search service for connecting to AI Services. You can use either a [system or user managed identity](search-howto-managed-identities-data-sources.md). To use a system manged identity, leave `apiKey` and `authIdentity` blank. The system-managed identity is used automatically. A managed identity must have Cognitive Services User permissions to use this vectorizer. |
+| `authIdentity`   | A user-managed identity used by the search service for connecting to AI Services. You can use either a [system or user managed identity](search-howto-managed-identities-data-sources.md). To use a system managed identity, leave `apiKey` and `authIdentity` blank. The system-managed identity is used automatically. A managed identity must have Cognitive Services User permissions to use this vectorizer. |
 
 ## Supported vector query types
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIサービスへの接続に関する文書のフォーマット更新"
}
```

### Explanation
この変更では、`vector-search-vectorizer-ai-services-vision.md`ファイルに対してフォーマットの更新が行われました。具体的には、`authIdentity`パラメータの説明において、テキストのレイアウトが改善され、より一貫した表現になっています。

主な変更点は以下の通りです：

- `authIdentity`の説明が、テキストのインデントやフォーマットに一貫性を持たせるために修正され、情報がより明確に提示されています。具体的には、情報の重要性は変わらないものの、内容が少し整理されて読みやすく改善されています。 

これにより、ユーザーがAIサービスと接続する際のユーザー管理されたアイデンティティの使い方についての理解が深まります。また、文書全体の整合性が向上し、技術的な説明がより明確に表現されています。全体として、内容の理解を助けるためにフォーマットが整えられたことで、ユーザー体験が向上しています。

## articles/search/vector-search-vectorizer-azure-open-ai.md{#item-e75cee}

<details>
<summary>Diff</summary>
````diff
@@ -40,7 +40,7 @@ Parameters are case-sensitive.
 | `resourceUri` | The URI of the model provider, in this case, an Azure OpenAI resource. This parameter only supports URLs with domain `openai.azure.com`, such as `https://<resourcename>.openai.azure.com`. If the Azure OpenAI endpoint has a URL with domain `cognitiveservices.azure.com`, like `https://<resourcename>.cognitiveservices.azure.com`, a [custom subdomain](/azure/ai-services/openai/how-to/use-your-data-securely#enabled-custom-subdomain) with `openai.azure.com` must be created first for the Azure OpenAI resource and use `https://<resourcename>.openai.azure.com` instead.  |
 | `apiKey`   |  The secret key used to access the model. If you provide a key, leave `authIdentity` empty. If you set both the `apiKey` and `authIdentity`, the `apiKey` is used on the connection. |
 | `deploymentId`   | The name of the deployed Azure OpenAI embedding model. The model should be an embedding model, such as text-embedding-ada-002. See the [List of Azure OpenAI models](/azure/ai-services/openai/concepts/models) for supported models.|
-| `authIdentity`   | A user-managed identity used by the search service for connecting to Azure OpenAI. You can use either a [system or user managed identity](search-howto-managed-identities-data-sources.md). To use a system manged identity, leave `apiKey` and `authIdentity` blank. The system-managed identity is used automatically. A managed identity must have [Cognitive Services OpenAI User](/azure/ai-services/openai/how-to/role-based-access-control#azure-openai-roles) permissions to send text to Azure OpenAI. |
+| `authIdentity`   | A user-managed identity used by the search service for connecting to Azure OpenAI. You can use either a [system or user managed identity](search-howto-managed-identities-data-sources.md). To use a system managed identity, leave `apiKey` and `authIdentity` blank. The system-managed identity is used automatically. A managed identity must have [Cognitive Services OpenAI User](/azure/ai-services/openai/how-to/role-based-access-control#azure-openai-roles) permissions to send text to Azure OpenAI. |
 | `modelName` | (Required in API version 2024-05-01-Preview and later). The name of the Azure OpenAI embedding model that is deployed at the provided `resourceUri` and `deploymentId`. Currently supported values are `text-embedding-ada-002`, `text-embedding-3-large`, and `text-embedding-3-small` |
 
 ## Supported vector query types
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIへの接続に関する文書のフォーマット更新"
}
```

### Explanation
この変更は、`vector-search-vectorizer-azure-open-ai.md`ファイルに対するフォーマットの改善を目的としています。具体的には、`authIdentity`パラメータの説明が視覚的に整理されており、以前と比べて情報が一貫性を持って提示されています。

主な変更点は以下の通りです：

- `authIdentity`の説明文が更新され、テキストのインデントが調整され、一貫性が持たされています。ここでは、ユーザー管理されたアイデンティティを使用してAzure OpenAIに接続する方法が再確認されており、この機能がどのように使用されるかに関する明確な指針が提供されています。

これにより、ユーザーがAzure OpenAIサービスに正しく接続するための要件や手順をより簡単に理解できるようになっています。また、文書全体の整合性が向上し、技術的な説明がより明確に表現されています。いずれにしても、ユーザー体験が向上し、Azure OpenAIと連携する際の理解が深まる結果となっています。

## articles/search/vector-search-vectorizer-custom-web-api.md{#item-d7c2f9}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ Parameters are case-sensitive.
 | `httpMethod` | The method to use while sending the payload. Allowed methods are `PUT` or `POST` |
 | `httpHeaders` | A collection of key-value pairs where the keys represent header names and values represent header values that are sent to your Web API along with the payload. The following headers are prohibited from being in this collection:  `Accept`, `Accept-Charset`, `Accept-Encoding`, `Content-Length`, `Content-Type`, `Cookie`, `Host`, `TE`, `Upgrade`, `Via`. |
 | `authResourceId` | (Optional) A string that if set, indicates that this vectorizer should use a managed identity on the connection to the function or app hosting the code. This property takes an application (client) ID or app's registration in Microsoft Entra ID, in any of these formats: `api://<appId>`, `<appId>/.default`, `api://<appId>/.default`. This value is used to scope the authentication token retrieved by the indexer, and is sent along with the custom Web API request to the function or app. Setting this property requires that your search service is [configured for managed identity](search-howto-managed-identities-data-sources.md) and your Azure function app is [configured for a Microsoft Entra sign in](/azure/app-service/configure-authentication-provider-aad). |
-| `authIdentity`   | (Optional) A user-managed identity used by the search service for connecting to the function or app hosting the code. You can use either a [system or user managed identity](search-howto-managed-identities-data-sources.md). To use a system manged identity, leave `authIdentity` blank. |
+| `authIdentity`   | (Optional) A user-managed identity used by the search service for connecting to the function or app hosting the code. You can use either a [system or user managed identity](search-howto-managed-identities-data-sources.md). To use a system managed identity, leave `authIdentity` blank. |
 | `timeout` | (Optional) When specified, indicates the timeout for the http client making the API call. It must be formatted as an XSD "dayTimeDuration" value (a restricted subset of an [ISO 8601 duration](https://www.w3.org/TR/xmlschema11-2/#dayTimeDuration) value). For example, `PT60S` for 60 seconds. If not set, a default value of 30 seconds is chosen. The timeout can be set to a maximum of 230 seconds and a minimum of 1 second. |
 
 ## Supported vector query types
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムWeb APIへの接続に関する文書のフォーマット更新"
}
```

### Explanation
この変更は、`vector-search-vectorizer-custom-web-api.md`ファイルに対する軽微なフォーマット更新を目的としています。具体的には、`authIdentity`パラメータの説明が視覚的に整理されており、以前の表現と比べてより明確になっています。

主な変更点は以下の通りです：

- `authIdentity`の説明が更新され、テキストのインデントが一貫性を持たせるために修正されました。内容自体の意味は変わっていませんが、このフォーマットの改善により、ユーザーがユーザー管理されたアイデンティティを使用してWeb APIに接続する方法がより理解しやすくなっています。

この変更は、ユーザーがカスタムWeb APIとの接続に関する要件をより簡単に理解できるようにすることを目的としています。また、文書全体の整合性が向上し、技術的な内容がより明確に表現されています。結果として、読み手は必要な情報を迅速に把握できるようになり、カスタムWeb APIとの連携に対する理解が深まります。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ Learn about the latest updates to Azure AI Search functionality, docs, and sampl
 | [GenAI prompt skill (preview)](cognitive-search-skill-genai-prompt.md) | Skills | A new skill that connects to a large language model (LLM) for information, using a prompt you provide. With this skill, you can populate a searchable field using content from an LLM. A primary use case for this skill is *image verbalization*, using an LLM to describe images and send the description to a searchable field in your index. |
 | [Document Layout skill (preview)](cognitive-search-skill-document-intelligence-layout.md)| Skills | New parameters are available for this skill if you use the 2025-05-01-preview API version. New parameters support image offset metadata that improves the image search experience. |
 | Import and vectorize data wizard enhancements | Portal | This wizard provides two paths for creating and populating vector indexes: [Retrieval Augmented Generation (RAG)](search-get-started-portal-import-vectors.md) and [Multimodal RAG](search-get-started-portal-image-search.md). Logic apps integration is through the RAG path. |
-| [Index "description" support (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true#request-body) | REST | The latest preview API adds a description to an index. A description is useful in agentic solutions, where the agent reads the description to decide whether to run a query or move on to another index. |
+| [Index "description" support (preview)](search-howto-reindex.md#add-an-index-description-preview) | REST | The latest preview API adds a description to an index. Consider a Model Context Protocol (MCP) server that must pick the correct index at run time. The decision can be  based on the description rather than on the index name alone. The description must be human readable and under four thousand characters.|
 | [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) | REST | New data plane preview REST API version providing programmatic access to the preview features announced in this release. |
 
 ## April 2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスの説明に関する情報の更新"
}
```

### Explanation
この変更は、`whats-new.md`ファイルに対する軽微な情報の更新を目的としています。具体的には、インデックスに関する「説明」サポートの詳細が修正されており、これにより使用方法の明確化が図られています。

主な変更点は以下の通りです：

- インデックスの「description」サポートに関するリンクが変更され、新しい参照先が指定されています。変更前は、リンクが古いAPIのドキュメントに向けられていましたが、変更後は新しいガイドラインが参照されており、ユーザーが最新の情報にアクセスしやすくなっています。
- 説明の内容が若干詳細化され、Model Context Protocol (MCP)サーバーがインデックスを選択する際に、インデックス名だけでなく、人間にとって読みやすい説明が必要であることが強調されています。

この更新により、インデックスを設定する際の背景や要件に関する理解が深まり、ユーザーがより適切に機能を利用できるようになっています。また、ドキュメント全体の整合性が向上し、新機能を活用するための指針がより具体的に示されています。


