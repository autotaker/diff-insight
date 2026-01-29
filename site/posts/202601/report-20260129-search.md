---
date: '2026-01-29'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:83988f2...MicrosoftDocs:cac9cb3
summary: この差分は、Azure AI Searchに関連するドキュメントのいくつかの更新を含んでおり、新機能として埋め込みモデルのサーバーレスデプロイメントの詳細な手順が追加されました。その他の更新には用語の変更、日付の更新、デプロイメント手順の現代化があり、アクセス制御リストに関連する制限事項の緩和も行われています。全体的に、ユーザビリティを向上させることを目的としており、特にAzure
  CLIを使用することにより、システムの管理がより効率的に、直感的に行えるようになっています。これらの変更により、Azure AI Searchの機能が一層洗練され、利用者が快適にAzure
  AIサービスを活用できることが期待されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:83988f2...MicrosoftDocs:cac9cb3){target="_blank"}

<format>
# ハイライト
この差分は、Azure AI Searchに関連するドキュメントのいくつかの更新を含んでいます。新機能として、Azure AI Searchでの埋め込みモデルのサーバーレスデプロイメントの詳細な手順が追加されました。その他の更新には、用語の変更、日付の更新、デプロイメント手順の現代化（Azure CLI を使用する方法への切り替え）などが含まれます。制限事項の緩和（ACL機能関連）も行われています。

## 新機能
- 埋め込みモデルのサーバーレスデプロイメントに関するセクションと具体的な手順が追加され、Azure CLIを利用した手法が提案されています。

## 重大な変更
なし。今回の更新は全てマイナーアップデートであり、既存の機能に影響を与えるものではありません。

## その他の更新
- 著者情報や文書の日付の更新。
- 用語の統一（例：「Foundry」から「Microsoft Foundry」）。
- サーバーレスAPIデプロイメント手法の現代化（Azure CLIの使用）。
- ACL設定でのuserIdsとgroupIdsの制限緩和。
- インデックス関連のドキュメントでの日付更新と説明内容の明確化。

# インサイト
このソースコードの変更は、Azure AI Searchの利用におけるユーザビリティを向上させることを意図しています。特に、サーバーレスデプロイメントの方法を最新のAzure CLIに基づく手法に統一することで、ユーザーがより効率的でシンプルにシステムを管理できるようになっています。これにより、従来のARM/Bicepテンプレートを用いた方法からの移行が促進され、デプロイメント手順が直感的で一貫性のあるものになります。

また、アクセス制御リストの制限緩和や、埋め込みモデルに関する新しい展開方法の追加は、システムの柔軟性と拡張性を強化し、ユーザーがより多くの機能を持つアプリケーションを構築しやすくしています。

これらの変更により、Azure AI Searchの機能が一層洗練され、開発者やユーザーにとっての有用性が高められることが期待されます。最新の情報を反映しつつ、使用手引きがより明快になることで、利用者がAzure AIサービスをより快適に活用できるようになります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | エンドツーエンドの検索ソリューションのチュートリアルの更新 | modified | 6 | 4 | 10 | 
| [cognitive-search-aml-skill.md](#item-51366c) | minor update | カスタムAMLスキルに関するドキュメントの更新 | modified | 3 | 3 | 6 | 
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | 画像検索のポータルに関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | ベクターインポートのポータルに関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [search-index-access-control-lists-and-rbac-push-api.md](#item-45e71e) | minor update | アクセス制御リストとRBACに関するAPIドキュメントの更新 | modified | 2 | 2 | 4 | 
| [search-what-is-an-index.md](#item-5a3344) | minor update | 検索インデックスに関するドキュメントの改善 | modified | 37 | 26 | 63 | 
| [vector-search-integrated-vectorization-ai-studio.md](#item-353fcc) | new feature | サーバーレスデプロイメントに対応した埋め込みモデルの展開方法 | modified | 64 | 3 | 67 | 
| [vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md](#item-ebe7a3) | minor update | サーバーレスデプロイメントのプロビジョニング手順の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -2,10 +2,10 @@
 title: 'Tutorial: Create an End-to-End Retrieval Solution'
 titleSuffix: Azure AI Search
 description: Learn how to design and build a custom agentic retrieval solution where Azure AI Search handles data retrieval for your custom agents in Microsoft Foundry.
-author: HeidiSteen
-ms.author: heidist
+author: haileytap
+ms.author: haileytapia
 manager: nitinme
-ms.date: 12/22/2025
+ms.date: 01/27/2026
 ms.service: azure-ai-search
 ms.topic: tutorial
 ms.custom:
@@ -413,7 +413,9 @@ print(f"AI agent '{agent_name}' created or updated successfully")
 
 #### Connect to a remote SharePoint knowledge source
 
-Optionally, if you create a [remote SharePoint knowledge source](agentic-knowledge-source-how-to-sharepoint-remote.md), you must also include the `x-ms-query-source-authorization` header in the MCP tool connection.
+[!INCLUDE [foundry-iq-limitation](../ai-foundry/default/includes/foundry-iq-limitation.md)]
+
+Optionally, if your knowledge base includes a [remote SharePoint knowledge source](agentic-knowledge-source-how-to-sharepoint-remote.md), you must also include the `x-ms-query-source-authorization` header in the MCP tool connection.
 
 ```python
 from azure.search.documents.indexes.models import RemoteSharePointKnowledgeSource, KnowledgeSourceReference
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンドツーエンドの検索ソリューションのチュートリアルの更新"
}
```

### Explanation
この変更は、Azure AI Searchのエンドツーエンドの検索ソリューションに関するチュートリアルの内容を更新したものです。主な修正点には、著者情報の更新（'heidisteen'から'haileytap'へ）や、文書の日付が更新されるため、2025年12月22日から2026年1月27日へ変更されています。また、一部のテキストが整理され、説明がより明確になるよう改善されています。具体的には、リモートSharePoint知識ソースに関連するオプションのテキストが変更され、説明が強調されるように、[!INCLUDE]マークアップが追加されています。

これにより、文書全体の可読性が向上し、Azure AI Searchの機能がより効果的に伝えられるようになっています。最終的に、この更新はユーザーがソリューションをより理解しやすくするために役立つでしょう。

## articles/search/cognitive-search-aml-skill.md{#item-51366c}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Custom AML skill in skillsets
+title: Custom AML Skill in Skillsets
 titleSuffix: Azure AI Search
 description: Learn how to extend the capabilities of Azure AI Search skillsets with Microsoft Foundry or Azure Machine Learning models.
 author: gmndrg
@@ -33,7 +33,7 @@ The indexer retries two times for the following HTTP status codes:
 + `503 Service Unavailable`
 + `429 Too Many Requests`
 
-## AML skill for models in Foundry
+## AML skill for models in Microsoft Foundry
 
 Azure AI Search provides the [Microsoft Foundry model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md), which is also available in the [**Import data (new)** wizard](search-import-data-portal.md#skills), for query-time connections to the model catalog. If you want to use this vectorizer for queries, the AML skill is the *indexing counterpart* for generating embeddings using a model from the model catalog.
 
@@ -45,7 +45,7 @@ We recommend using the [**Import data (new)** wizard](search-get-started-portal-
 
 + A [Microsoft Foundry hub-based project](/azure/ai-foundry/how-to/hub-create-projects) or an [AML workspace](../machine-learning/concept-workspace.md) for a custom model that you create.
 
-+ For hub-based projects only, a serverless deployment of a [supported model](#skill-parameters) from the Microsoft Foundry model catalog. You can use an [ARM/Bicep template](https://github.com/Azure-Samples/azure-ai-search-multimodal-sample/blob/42b4d07f2dd9f7720fdc0b0788bf107bdac5eecb/infra/ai/modules/project.bicep#L37C1-L38C1) to provision the serverless deployment.
++ For hub-based projects only, a serverless deployment of a [supported model](#skill-parameters) from the Microsoft Foundry model catalog. You can use [use the Azure CLI](vector-search-integrated-vectorization-ai-studio.md#deploy-an-embedding-model-as-a-serverless-deployment) to provision the serverless deployment.
 
 ## @odata.type
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムAMLスキルに関するドキュメントの更新"
}
```

### Explanation
この変更は、カスタムAMLスキルに関するドキュメントのいくつかの用語と説明を更新したものです。主な変更点はタイトルの表記スタイルを統一し、「Custom AML skill in skillsets」を「Custom AML Skill in Skillsets」に変更しました。また、いくつかのセクション見出しが明確化され、「Foundry」から「Microsoft Foundry」と具体化されました。

さらに、サーバーレスデプロイメントのプロビジョニングに関する説明の一部が更新され、ARM/Bicepテンプレートを使用する代わりにAzure CLIを使用する方法を示すように修正されました。これにより、ドキュメントの内容が最新の手法に基づくものとなり、ユーザーがスキルを効果的に活用できるようサポートしています。

これらの変更は、文書の明確さとユーザーの理解を助けるためのものであり、全体的な文書の品質を向上させています。

## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -64,7 +64,7 @@ The portal supports the following models for each method. Deployment instruction
 
 <sup>1</sup> For billing purposes, you must [attach your multi-service account](cognitive-search-attach-cognitive-services.md) to your Azure AI Search skillset. Currently, the wizard requires your search service and multi-service account to be in the [same supported region for the Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md#supported-regions), even when using keyless connections.
 
-<sup>2</sup> To use this model in the wizard, you must provision it as a serverless API deployment. You can use an [ARM/Bicep template](https://github.com/Azure-Samples/azure-ai-search-multimodal-sample/blob/42b4d07f2dd9f7720fdc0b0788bf107bdac5eecb/infra/ai/modules/project.bicep#L37C1-L38C1) for this task.
+<sup>2</sup> To use this model in the wizard, you must provision it as a serverless API deployment. You can use [use the Azure CLI](vector-search-integrated-vectorization-ai-studio.md#deploy-an-embedding-model-as-a-serverless-deployment) to provision the serverless deployment.
 
 <sup>3</sup> The endpoint of your Azure OpenAI resource must have a [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains), such as `https://my-unique-name.openai.azure.com`. If you created your resource in the [Azure portal](https://portal.azure.com/), this subdomain was automatically generated during resource setup.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像検索のポータルに関するドキュメントの更新"
}
```

### Explanation
この変更は、画像検索機能に関するドキュメントの一部表現を更新したものです。特に、サーバーレスAPIデプロイメントに関する説明が変更されました。元々はARM/Bicepテンプレートを使用してデプロイするという指示がありましたが、新しい指示ではAzure CLIを使用してサーバーレスデプロイメントをプロビジョニングする方法が提案されています。

この変更により、ユーザーは最新の手法を利用してデプロイメントを行うことができ、手順がより直感的になります。また、文書全体の一貫性が高まり、情報が最新の状態に保たれています。このように、変更はユーザーにとっての利便性向上に寄与しています。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -56,7 +56,7 @@ The portal supports the following embedding models for integrated vectorization.
 
 <sup>1</sup> For billing purposes, you must [attach your multi-service account](cognitive-search-attach-cognitive-services.md) to your Azure AI Search skillset. Currently, the wizard requires your search service and multi-service account to be in the [same supported region for the Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md#supported-regions), even when using keyless connections.
 
-<sup>2</sup> To use this model in the wizard, you must provision it as a serverless API deployment. You can use an [ARM/Bicep template](https://github.com/Azure-Samples/azure-ai-search-multimodal-sample/blob/42b4d07f2dd9f7720fdc0b0788bf107bdac5eecb/infra/ai/modules/project.bicep#L37C1-L38C1) for this task.
+<sup>2</sup> To use this model in the wizard, you must provision it as a serverless API deployment. You can use [use the Azure CLI](vector-search-integrated-vectorization-ai-studio.md#deploy-an-embedding-model-as-a-serverless-deployment) to provision the serverless deployment.
 
 <sup>3</sup> The endpoint of your Azure OpenAI resource must have a [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains), such as `https://my-unique-name.openai.azure.com`. If you created your resource in the [Azure portal](https://portal.azure.com/), this subdomain was automatically generated during resource setup.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクターインポートのポータルに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchのベクターインポートに関するドキュメントの一部を更新したものです。具体的には、サーバーレスAPIデプロイメントのプロビジョニング方法に関する指示が更新されています。元の指示ではARM/Bicepテンプレートの使用が推奨されていましたが、改訂後はAzure CLIを使用してサーバーレスデプロイメントを行う方法が示されています。

この更新により、ユーザーは最新の手法を利用してデプロイメントを実施できるようになり、手順がより簡潔で明確になります。また、情報の一貫性が保たれ、ドキュメントが最新の内容に整合されていることも重要なポイントです。この変更は、ユーザーの利便性を向上させるために寄与しています。

## articles/search/search-index-access-control-lists-and-rbac-push-api.md{#item-45e71e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how to use the REST API for indexing documents with ACLs and RBAC metadata.  
 ms.service: azure-ai-search  
 ms.topic: how-to 
-ms.date: 09/18/2025 
+ms.date: 01/28/2025 
 author: admayber
 ms.author: admayber  
 ---  
@@ -33,7 +33,7 @@ This article explains how to use the push REST API to index document-level permi
 
 ## Limitations
 
-- An ACL field with permission filter type `userIds` or `groupIds` can hold at most 32 values.
+- An ACL field with permission filter type `userIds` or `groupIds` can hold at most 1000 values.
 
 - An index can hold at most five unique values among fields of type `rbacScope` on all documents. There's no limit on the number of documents that share the same value of `rbacScope`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アクセス制御リストとRBACに関するAPIドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるアクセス制御リスト（ACL）とロールベースのアクセス制御（RBAC）に関連するAPIドキュメントを更新したものです。具体的には、日付情報と制限に関する内容が変更されています。

最初に、ドキュメントの日付が2025年9月18日から2025年1月28日に変更されました。これは、情報が更新されたことを反映しています。次に、ACLフィールドの制限に関する記述が更新され、`userIds` または `groupIds` の permission filter type において、最大32の値から最大1000の値へと増えました。この変更により、ユーザーはより多くの値を設定できるようになり、機能の柔軟性が向上します。

全体として、この更新は、ユーザーに対して最新の情報を提供し、ドキュメントの正確性と使いやすさを高めることを目的としています。

## articles/search/search-what-is-an-index.md{#item-5a3344}

<details>
<summary>Diff</summary>
````diff
@@ -1,21 +1,21 @@
 ---
 title: Search index overview
 titleSuffix: Azure AI Search
-description: Explains what is a search index in Azure AI Search and describes content, construction, physical expression, and the index schema.
+description: Explains index content, construction, physical expression, and schema.
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 06/20/2025
+ms.date: 01/27/2026
 ms.update-cycle: 365-days
 ---
 
 # Search indexes in Azure AI Search
 
-In Azure AI Search, a *search index* is your searchable content, available to the search engine for indexing, agentic search, full-text search, vector search, hybrid search, and filtered queries. An index is defined by a schema and saved to the search service, with data ingestion following as a second step. Indexed content exists within your search service, apart from your primary external data stores, which is necessary for the millisecond response times expected in modern search applications. Except for indexer-driven indexing scenarios, the search service never connects to or queries your external source data.
+In Azure AI Search, a *search index* is your searchable content on a search service, available to the local search engine for indexing, agentic retrieval, full-text search, vector search, hybrid search, and filtered queries. An index is defined by a schema that's saved to your search service, with data ingestion following as a second step. Indexed content exists on your search service, apart from your primary external data stores, which is necessary for the millisecond response times expected in modern search applications. Except for remote agentic retrieval and indexer-driven indexing scenarios, the search service never connects to or queries your external source data.
 
 This article covers the key concepts for creating and managing a search index, including:
 
@@ -24,18 +24,22 @@ This article covers the key concepts for creating and managing a search index, i
 + Basic operations
 
 > [!TIP]
-> Want to get started right away? See [Create a search index](search-how-to-create-search-index.md).
+> **Quick summary:**
+> - An index stores your searchable content
+> - Schema defines fields and their behaviors
+> - Documents are individual searchable items (similar to rows in a database)
+> - [Jump to creating an index →](search-how-to-create-search-index.md)
 
 ## Schema of a search index
 
 In Azure AI Search, indexes contain *search documents*. Conceptually, a document is a single unit of searchable data in your index. For example, a retailer might have a document for each product, a university might have a document for each class, a travel site might have a document for each hotel and destination, and so forth. Mapping these concepts to more familiar database equivalents: a *search index* equates to a *table*, and *documents* are roughly equivalent to *rows* in a table.
 
-The structure of a document is determined by the *index schema*, as illustrated in the following example. The "fields" collection is typically the largest part of an index, where each field is named, assigned a [data type](/rest/api/searchservice/Supported-data-types), and attributed with allowable behaviors that determine how it's used.
+Here's an example of what an index schema looks like.
 
 ```json
 {
   "name": "name_of_index, unique across the service",
-  "description" : "Health plan coverage for standard and premium plans for Northwind and Contoso employees."
+  "description" : "Health plan coverage for standard and premium plans for Northwind and Contoso employees.",
   "fields": [
     {
       "name": "name_of_field",
@@ -44,15 +48,15 @@ The structure of a document is determined by the *index schema*, as illustrated
       "filterable": true (default) | false,
       "sortable": true (default where applicable) | false (Collection(Edm.String) fields cannot be sortable),
       "facetable": true (default where applicable) | false (Edm.GeographyPoint fields cannot be facetable),
-      "key": true | false (default, only Edm.String fields can be keys),
+      "key": true (only Edm.String fields can be keys) | false (default where applicable),
       "retrievable": true (default) | false,
-      "analyzer": "name_of_analyzer_for_search_and_indexing", (only if 'searchAnalyzer' and 'indexAnalyzer' are not set)
-      "searchAnalyzer": "name_of_search_analyzer", (only if 'indexAnalyzer' is set and 'analyzer' is not set)
-      "indexAnalyzer": "name_of_indexing_analyzer", (only if 'searchAnalyzer' is set and 'analyzer' is not set)
-      "normalizer":  "name_of_normalizer", (applies to fields that are filterable)
-      "synonymMaps": "name_of_synonym_map", (optional, only one synonym map per field is currently supported)
-      "dimensions": "number of dimensions used by an embedding models", (applies to vector fields only, of type Collection(Edm.Single))
-      "vectorSearchProfile": "name_of_vector_profile" (indexes can have many configurations, a field can use just one)
+      "analyzer": "name_of_analyzer_for_search_and_indexing" (only if 'searchAnalyzer' and 'indexAnalyzer' are not set),
+      "searchAnalyzer": "name_of_search_analyzer" (only if 'indexAnalyzer' is set and 'analyzer' is not set),
+      "indexAnalyzer": "name_of_indexing_analyzer" (only if 'searchAnalyzer' is set and 'analyzer' is not set),
+      "normalizer":  "name_of_normalizer" (applies to fields that are filterable),
+      "synonymMaps": "name_of_synonym_map" (optional, only one synonym map per field is currently supported),
+      "dimensions": "number of dimensions used by an embedding models" (applies to vector fields of type Collection(Edm.Single)),
+      "vectorSearchProfile": "name_of_vector_profile" (indexes can have many configurations but a field can use just one)
     }
   ],
   "suggesters": [ ],
@@ -69,6 +73,8 @@ The structure of a document is determined by the *index schema*, as illustrated
 }
 ```
 
+The `fields` collection is typically the largest part. Each field has a name, [data type](/rest/api/searchservice/Supported-data-types), and attributes that determine usage at query time.
+
 Other elements are collapsed for brevity, but the following links provide details: 
 
 + [suggesters](index-add-suggesters.md) support type-ahead queries like autocomplete.
@@ -81,7 +87,7 @@ Other elements are collapsed for brevity, but the following links provide detail
 
 ### Field definitions
 
-A search document is defined by the "fields" collection in the body of [Create Index request](/rest/api/searchservice/indexes/create). You need fields for document identification (keys), storing searchable text, and fields for supporting filters, facets, and sorting. You might also need fields for data that a user never sees. For example, you might want fields for profit margins or marketing promotions that you can use in a scoring profile to boost a search score.
+A search document is defined by the `fields` collection in the body of [Create Index request](/rest/api/searchservice/indexes/create). You need fields for document identification (keys), storing searchable text, and fields for supporting filters, facets, and sorting. You might also need fields for data that a user never sees. For example, you might want fields for profit margins or marketing promotions that you can use in a [scoring profile](index-add-scoring-profiles.md) to boost a search score.
 
 If incoming data is hierarchical in nature, you can represent it within an index as a [complex type](search-howto-complex-data-types.md), used for nested structures. The sample data set, [Hotels](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/hotels), illustrates complex types using an Address (contains multiple subfields) that has a one-to-one relationship with each hotel, and a Rooms complex collection, where multiple rooms are associated with each hotel. 
 
@@ -91,21 +97,22 @@ If incoming data is hierarchical in nature, you can represent it within an index
 
 Field attributes determine how a field is used, such as whether it's used in full text search, faceted navigation, sort operations, and so forth. 
 
-String fields are often marked as "searchable" and "retrievable". Fields used to narrow search results include "sortable", "filterable", and "facetable".
++ String fields are often marked as `searchable` and `retrievable`. 
++ Fields used to narrow or order search results are marked as `sortable`, `filterable`, and `facetable`.
 
 |Attribute|Description|  
 |---------------|-----------------|  
-|"searchable" |Full-text or vector searchable. Text fields are subject to lexical analysis such as word-breaking during indexing. If you set a searchable field to a value like "sunny day", internally it's split into the individual tokens "sunny" and "day". For details, see [How full text search works](search-lucene-query-architecture.md).|  
-|"filterable" |Referenced in $filter queries. Filterable fields of type `Edm.String` or `Collection(Edm.String)` don't undergo word-breaking, so comparisons are for exact matches only. For example, if you set such a field f to "sunny day", `$filter=f eq 'sunny'` finds no matches, but `$filter=f eq 'sunny day'` will. |  
-|"sortable" |By default the system sorts results by score, but you can configure sort based on fields in the documents. Fields of type `Collection(Edm.String)` can't be "sortable". |  
-|"facetable" |Typically used in a presentation of search results that includes a hit count by category (for example, hotels in a specific city). This option can't be used with fields of type `Edm.GeographyPoint`. Fields of type `Edm.String` that are filterable, "sortable", or "facetable" can be at most 32 kilobytes in length. For details, see [Create Index (REST API)](/rest/api/searchservice/indexes/create).|  
-|"key" |Unique identifier for documents within the index. Exactly one field must be chosen as the key field and it must be of type `Edm.String`.|  
-|"retrievable" |Determines whether the field can be returned in a search result. This is useful when you want to use a field (such as *profit margin*) as a filter, sorting, or scoring mechanism, but don't want the field to be visible to the end user. This attribute must be `true` for `key` fields.|  
+|searchable |Full-text or vector searchable. Text fields are subject to lexical analysis such as word-breaking during indexing. For details, see [How full text search works](search-lucene-query-architecture.md).|  
+|filterable |Referenced in $filter queries. Filterable fields of type `Edm.String` or `Collection(Edm.String)` don't undergo word-breaking, so comparisons are for exact matches only. Given the string "sunny day", `$filter=f eq 'sunny'` finds no matches, but `$filter=f eq 'sunny day'` succeeds. |  
+|sortable |By default the system sorts by a search score, but you can configure an explicit sort based on fields in the documents. Fields of type `Collection(Edm.String)` can't be sortable. |  
+|facetable |Typically used in a presentation of search results that includes a hit count by category (for example, hotels in a specific city). This option can't be used with fields of type `Edm.GeographyPoint`. Fields of type `Edm.String` that are filterable, sortable, or facetable can be at most 32 kilobytes in length. For details, see [Create Index (REST API)](/rest/api/searchservice/indexes/create).|  
+|key |Unique identifier for documents within the index. Exactly one field must be chosen as the key field and it must be of type `Edm.String`.|  
+|retrievable |Determines whether the field can be returned in a search result. This is useful when you want to use a field (such as *profit margin*) as a filter, sorting, or scoring mechanism, but don't want the field to be visible to the end user. This attribute must be `true` for `key` fields.|  
 
 Although you can add new fields at any time, existing field definitions are locked in for the lifetime of the index. For this reason, developers typically use the Azure portal for creating simple indexes, testing ideas, or using the Azure portal pages to look up a setting. Frequent iteration over an index design is more efficient if you follow a code-based approach so that you can rebuild the index easily.
 
 > [!NOTE]
-> The APIs you use to build an index have varying default behaviors. For the [REST APIs](/rest/api/searchservice/indexes/create), most attributes are enabled by default (for example, "searchable" and "retrievable" are true for string fields) and you often only need to set them if you want to turn them off. For the .NET SDK, the opposite is true. On any property you do not explicitly set, the default is to disable the corresponding search behavior unless you specifically enable it.
+> The APIs you use to build an index have varying default behaviors. For the [REST APIs](/rest/api/searchservice/indexes/create), most attributes are enabled by default (for example, searchable and retrievable are true for string fields) and you often only need to set them if you want to turn them off. For the .NET SDK, the opposite is true. On any property you don't explicitly set, the default is to disable the corresponding search behavior unless you specifically enable it.
 
 <a name="index-size"></a>
 
@@ -115,10 +122,13 @@ In Azure AI Search, the physical structure of an index is largely an internal im
 
 You can monitor index size on the **Search management > Indexes** page in the Azure portal. Alternatively, you can issue a [GET INDEX request](/rest/api/searchservice/indexes/get) against your search service or a [Service Statistics request](/rest/api/searchservice/get-service-statistics/get-service-statistics) to check the value of storage size.
 
+> [!NOTE]
+> If you're actively [deleting content](search-how-to-delete-documents.md), index storage and size are updated every few minutes. Deletion runs as a background process. Expect a small delay on metric updates.
+
 The size of an index is determined by the:
 
 + Quantity and composition of your documents.
-+ Attributes on individual fields: "retrievable" doesn't bloat your index, but "filterable", "sortable", "facetable" consume more storage for storing non-tokenized text.
++ Attributes on individual fields: retrievable doesn't bloat your index, but filterable, sortable, and facetable consume more storage for storing non-tokenized text.
 + Index configuration. Specifically, whether you include suggesters or specialized [analyzers](search-analyzers.md). If you use the edgeNgram tokenizer to store verbatim sequences of characters (`a, ab, abc, abcd`), the index is larger than if you use the standard analyzer.
 
 Document composition and quantity are determined by what you choose to import. Remember that a search index should only contain content that's useful for your search application. If source data includes binary fields, omit those fields unless you're using AI enrichment to crack and analyze the content to create text-searchable information.
@@ -157,12 +167,13 @@ All indexing and query requests target an index. Endpoints are usually one of th
 | `<your-service>.search.windows.net/indexes` | Targets the indexes collection. Used when creating, listing, or deleting an index. Admin rights are required for these operations and available through admin [API keys](search-security-api-keys.md) or a [Search Contributor role](search-security-rbac.md#built-in-roles-used-in-search). |
 | `<your-service>.search.windows.net/indexes/<your-index>/docs` | Targets the documents collection of a single index. Used when querying an index or data refresh. For queries, read rights are sufficient and available through query API keys or a data reader role. For data refresh, admin rights are required. |
 
-#### How to connect to Azure AI Search
+#### How to connect to an index
 
-1. [Start with the Azure portal](https://portal.azure.com). Azure subscribers, or the person who created the search service, can manage the search service in the Azure portal. An Azure subscription requires Contributor or above permissions to create or delete services. This permission level is sufficient for fully managing a search service in the Azure portal.
+1. [Start with the Azure portal](https://portal.azure.com) and your search service dashboard.
 
 1. Try other clients for programmatic access. We recommend the quickstarts for first steps:
 
+   + [Quickstart: Connect to a search service](search-get-started-rbac.md)
    + [Quickstart: REST](search-get-started-text.md)
    + [Quickstart: Full-text search](search-get-started-text.md)
    + [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスに関するドキュメントの改善"
}
```

### Explanation
この変更は、Azure AI Searchにおける検索インデックスのドキュメントを改善し、内容を更新したものです。主な変更点は以下の通りです。

1. **説明の簡潔化**: ドキュメントの冒頭部分で、検索インデックスの説明が簡略化され、インデックスがどのように構築され、物理的に表現されるかについての説明が明確にされています。

2. **日付の更新**: ドキュメントの日付が2025年6月20日から2026年1月27日に変更され、最新の情報が反映されています。

3. **制限の変更**: ACLフィールドに関する制限が明確化され、フィールドの項目が4000ではなく1000に増加したことが記載されています。この更新により、ユーザーはより多くの値をインデックスに持たせられることが強調されています。

4. **フィールドの定義についての詳細化**: `fields` コレクションに関する説明が強化され、各フィールドの役割や利用方法について、より詳細に記載されています。

5. **インデックスサイズに関する注意書きの追加**: インデックスのサイズやストレージの更新についての注意事項が加えられ、ユーザーが削除操作を行った際のインデックスサイズの更新タイミングについても明記されています。

この変更全体により、ユーザーはインデックスの構造や機能を理解しやすくなり、より効果的にAzure AI Searchを利用できるようになります。

## articles/search/vector-search-integrated-vectorization-ai-studio.md{#item-353fcc}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 11/21/2025
+ms.date: 01/28/2026
 ---
 
 # Use embedding models from the Microsoft Foundry model catalog for integrated vectorization
@@ -41,11 +41,11 @@ Supported embedding models from the model catalog vary by usage method:
 
 ## Deploy an embedding model from the model catalog
 
-1. Follow [these instructions](/azure/ai-foundry/how-to/deploy-models-openai) to deploy a supported model to your project.
+1. Follow [these portal instructions](/azure/ai-foundry/how-to/deploy-models-openai) to deploy a supported model to your project.
 
 1. Make a note of the target URI, key, and model name. You need these values for the vectorizer definition in a search index and for the skillset that calls the model endpoints during indexing.
 
-    If you prefer [token authentication](#connect-using-token-authentication) to key-based authentication, you only need to copy the URI and model name. However, make a note of the region to which the model is deployed.
+    If you prefer [token authentication](#connect-using-token-authentication) to key-based authentication, you only need to copy the model name. However, make a note of the region to which the model is deployed.
 
 1. Configure a search index and indexer to use the deployed model.
 
@@ -81,6 +81,67 @@ Supported embedding models from the model catalog vary by usage method:
    + To use the model as a vectorizer at query time, see [Configure a vectorizer](vector-search-how-to-configure-vectorizer.md). Be sure to use the [Microsoft Foundry model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) for this step.
 -->
 
+## Deploy an embedding model as a serverless deployment
+
+The AML skill and Microsoft Foundry model catalog vectorizer only accept serverless deployments of Cohere embedding models. Serverless deployments via the Microsoft Foundry portal aren't supported for these models, so use the Azure CLI to create the deployment. For more information, see [Deploy models as serverless API deployments](/azure/ai-foundry/how-to/deploy-models-serverless).
+
+To create a Cohere serverless deployment:
+
+1. Install the Azure CLI with the `ml` extension.
+
+    ```azurecli
+    az extension add -n ml
+    ```
+
+1. Sign in to Azure and set your defaults.
+
+    ```azurecli
+    az login
+    az account set --subscription <subscription-id>
+    az configure --defaults workspace=<project-name> group=<resource-group>
+    ```
+
+1. Create a `subscribe.yaml` file to subscribe to the marketplace subscription for the model.
+
+    ```yaml
+    name: cohere-embed-v3-english-subscription
+    model_id: azureml://registries/azureml-cohere/models/Cohere-embed-v3-english
+    ```
+
+    For other supported models, replace the model ID with one of the following values.
+    
+    | Model | Model ID |
+    | ----- | -------- |
+    | Cohere-embed-v3-english | `azureml://registries/azureml-cohere/models/Cohere-embed-v3-english` |
+    | Cohere-embed-v3-multilingual | `azureml://registries/azureml-cohere/models/Cohere-embed-v3-multilingual` |
+    | Cohere-embed-v4 | `azureml://registries/azureml-cohere/models/Cohere-embed-v4` |
+
+1. Run the following command to create the subscription.
+
+    ```azurecli
+    az ml marketplace-subscription create --file subscribe.yaml
+    ```
+
+1. Create an `endpoint.yaml` file to create the serverless endpoint.
+
+    ```yaml
+    name: cohere-embed-v3-english-endpoint
+    model_id: azureml://registries/azureml-cohere/models/Cohere-embed-v3-english
+    ```
+
+1. Run the following command to create the endpoint.
+
+    ```azurecli
+    az ml serverless-endpoint create --file endpoint.yaml
+    ```
+
+1. For key-based authentication, get the endpoint URI and key for use in the skill or vectorizer.
+
+    ```azurecli
+    az ml serverless-endpoint show --name cohere-embed-v3-english-endpoint --query "scoring_uri"
+    az ml serverless-endpoint get-credentials --name cohere-embed-v3-english-endpoint
+    ```
+
 ## Sample AML skill payload
 
 When you deploy embedding models from the model catalog, you connect to them using the [AML skill](cognitive-search-aml-skill.md) in Azure AI Search for indexing workloads.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "サーバーレスデプロイメントに対応した埋め込みモデルの展開方法"
}
```

### Explanation
この変更は、Azure AI Searchにおける埋め込みモデルの展開方法について新しいセクションを追加し、サーバーレスデプロイメントに関する詳細な手順を提供しています。

主な変更点は以下の通りです。

1. **日付の更新**: ドキュメントの日付が2025年11月21日から2026年1月28日に変更され、最新の情報が確保されています。

2. **新しいセクションの追加**: サーバーレスデプロイメントとして埋め込みモデルを展開する方法に関するセクションが追加されました。これには、Azure CLIを使用してCohere埋め込みモデルのサーバーレスデプロイメントを作成するための一連の具体的な手順が含まれています。

3. **手順の詳細化**: デプロイメントのための前提条件や、Azure CLIのインストール手順、各種設定ファイルの作成手順が詳細に説明されています。このプロセスでは、サブスクリプションの作成、エンドポイントの設定、および認証情報の取得が含まれています。

4. **サポートモデルのリスト**: サーバーレスデプロイメントに対応した複数のモデルIDが表形式で示され、ユーザーがどのモデルを使用できるかを明確にしています。

この変更により、ユーザーはサーバーレス環境で効率的に埋め込みモデルをデプロイし、活用するための具体的な手順を追いやすくなります。これにより、Azure AI Searchの機能がさらに拡張され、ユーザーにとっての利便性が向上します。

## articles/search/vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md{#item-ebe7a3}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ If you're using integrated vectorization to create the vector arrays, the skills
 
 + A [Microsoft Foundry hub-based project](/azure/ai-foundry/how-to/hub-create-projects) or an [AML workspace](../machine-learning/concept-workspace.md) for a custom model that you create.
 
-+ For hub-based projects only, a serverless deployment of a [supported model](#vectorizer-parameters) from the Microsoft Foundry model catalog. You can use an [ARM/Bicep template](https://github.com/Azure-Samples/azure-ai-search-multimodal-sample/blob/42b4d07f2dd9f7720fdc0b0788bf107bdac5eecb/infra/ai/modules/project.bicep#L37C1-L38C1) to provision the serverless deployment.
++ For hub-based projects only, a serverless deployment of a [supported model](#vectorizer-parameters) from the Microsoft Foundry model catalog. You can use [use the Azure CLI](vector-search-integrated-vectorization-ai-studio.md#deploy-an-embedding-model-as-a-serverless-deployment) to provision the serverless deployment.
 
 ## Vectorizer parameters
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスデプロイメントのプロビジョニング手順の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるベクトライザーのドキュメントの一部を修正し、サーバーレスデプロイメントのプロビジョニング手順を更新したものです。

主な変更点は以下の通りです。

1. **手順の変更**: サーバーレスデプロイメントをプロビジョニングするための手順が、ARM/BicepテンプレートからAzure CLIに変更されました。これにより、より新しい手法に基づいてプロビジョニングを行うことができます。

2. **リンクの更新**: サーバーレスデプロイメントの手順に関連するリンクが更新され、ユーザーが使用する際に必要な情報にアクセスしやすくなっています。具体的には、Azure CLIを使用して埋め込みモデルをデプロイする方法にリンクしています。

この変更により、ユーザーはサーバーレス環境でベクトライザーをより効果的にプロビジョニングし、最新の手法を活用することができるようになります。全体的には、文書が最新の手法に対応する形で改善されています。


