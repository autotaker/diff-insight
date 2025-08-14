---
date: '2025-08-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ebf24ba...MicrosoftDocs:a697dec
summary: この報告書は、Azure AI Searchに関する最新のアップデートをまとめています。新機能として、ローカル環境でのAzureサブスクリプションとテナント管理の手順が追加され、BM25スコアリングアルゴリズムの具体的なパラメーター情報が加わりました。
  Azure AI Searchの機能リストにも新しい情報が盛り込まれています。重要な仕様変更はないものの、用語の改訂によって一部の表現が変更され、既存の理解に影響を与える可能性があります。また、ドキュメントは最新日付に更新され、説明の明確化が行われ、「indexer」から「connector」への用語変更が行われました。ユーザーに利用しやすいアクセス方法がもたらされたことによって、Azureサービスの利用体験が向上しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ebf24ba...MicrosoftDocs:a697dec){target="_blank"}

# Highlights

## New features
- 新たな手順の追加により、ローカル環境でのAzureサブスクリプションとテナントの管理が容易になりました。
- BM25スコアリングアルゴリズムに関する具体的なパラメーター情報が追加され、関連性スコアの理解が深まりました。
- Azure AI Searchの機能リストに新機能やプレビュー情報を追加。

## Breaking changes
- 特に重大な仕様変更や互換性の問題は発生していませんが、用語の改訂によって一部の表現が変更されたため、既存の理解に影響を与える可能性があります。

## Other updates
- ドキュメントの最新の日付への更新と、説明やセクションの明確化が行われました。
- 用語の一貫性を保つために「indexer」から「connector」への変更が行われました。

# Insights

Azure AI Searchに関連する複数のドキュメントが最新情報に基づいて更新されました。特に、RBACの利用手順やインデクシングに関する手順がユーザーの利便性を考慮して改訂され、新しい機能と連携方法に関する情報が追加されています。

RBACに関するクイックスタートでは、ユーザーがサブスクリプションとテナントを確認し、必要に応じて適切に設定を変更できるようになることで、初歩的な設定ミスが減少することが期待されます。具体的なAzure CLIのコマンド例が追加されたことにより、実務での活用がさらに促進されるでしょう。

また、BM25スコアリングアルゴリズムに関しては、スコアがどのようにフィールドに寄与するかの詳細情報が追加され、より精緻な検索結果を得るための手掛かりが提供されています。この機能拡張は、特に高度な検索機能を導入しようとしている企業にとって有用です。

さらに、Azure AI Searchの機能リスト更新により、新しいデータソースやAI機能に関する情報が追加され、利用可能なオプションがより具体的に示されるようになりました。特に、「OneLake (プレビュー)」の追加は、Azureのデータエコシステムを活用する新たな可能性を示唆しています。

最後に、Azure Logic Appsに関する用語の見直しが行われ、文書全体の明確性とユーザー理解が改善されました。これにより、Azureの機能を活用する上での誤解や混乱が減少することが期待されます。

全体として、これらの更新はAzureユーザーの体験を向上させ、新しい技術の統合を円滑に進めるための基盤を強化するものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-rbac-rest.md](#item-fd8ef4) | minor update | QuickstartのRBAC RESTの更新: 日付と手順の変更 | modified | 11 | 3 | 14 | 
| [index-similarity-and-scoring.md](#item-75603d) | minor update | BM25スコアリングアルゴリズムに関するドキュメントの修正 | modified | 68 | 20 | 88 | 
| [search-features-list.md](#item-d34448) | minor update | Azure AI Search機能リストの更新 | modified | 36 | 34 | 70 | 
| [search-how-to-index-logic-apps-indexers.md](#item-64a12e) | minor update | Azure Logic Appsインデクサーに関する用語の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/includes/quickstarts/search-get-started-rbac-rest.md{#item-fd8ef4}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 07/09/2025
+ms.date: 08/13/2025
 ---
 
 In this quickstart, you use role-based access control (RBAC) and Microsoft Entra ID to establish a keyless connection to your Azure AI Search service. You then use REST in Visual Studio Code to interact with your service.
@@ -33,10 +33,18 @@ To get your token:
 
 1. On your local system, open a command-line tool.
 
-1. Sign in to Azure. If you have multiple subscriptions, select the one whose ID you obtained in [Get service information](#get-service-information).
+1. Check for the active tenant and subscription in your local environment.
 
    ```azurecli
-   az login
+   az account show
+   ```
+
+1. If the active subscription and tenant aren't valid for your search service, change the variables. You can check for the subscription ID on the search service overview page in the Azure portal. You can check for the tenant ID by clicking through to the subscription. Make a note of the values that are valid for your search service and run the following commands to update your local environment.
+
+   ```azurecli
+    az account set --subscription <your-subscription-id>
+
+    az login --tenant <your-tenant-id>
    ```
 
 1. Generate an access token.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "QuickstartのRBAC RESTの更新: 日付と手順の変更"
}
```

### Explanation
この変更は、Azure AI SearchサービスにおけるRBAC（ロールベースのアクセス制御）の利用方法に関するクイックスタートガイドの更新です。主な変更点として、ドキュメントの日付が2025年7月9日から2025年8月13日に更新され、手順の一部が改訂されました。

具体的には、ローカル環境でのアクティブテナントとサブスクリプションの確認方法が追加され、ユーザーがサブスクリプションとテナントが有効でない場合に行うべき変更を取り扱った新しい手順が加えられました。これにより、利用者はより明確に、自分の環境を正しく設定する方法を理解できるようになります。

ドキュメント内では、`az account show` コマンドを用いてアクティブなサブスクリプションとテナントを確認した後、該当する情報に基づいてサブスクリプションとテナントの変更を行う指示が追加され、具体的なコマンド例も示されています。これにより、ユーザーはAzure CLIを簡単に使用してサブスクリプション情報を管理できるようになります。この変更は、ドキュメントの正確性と使いやすさを向上させるために重要です。

## articles/search/index-similarity-and-scoring.md{#item-75603d}

<details>
<summary>Diff</summary>
````diff
@@ -8,12 +8,12 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 01/17/2025
+ms.date: 08/13/2025
 ---
 
 # Relevance in keyword search (BM25 scoring)
 
-This article explains the BM25 relevance scoring algorithm used to compute search scores for [full text search](search-lucene-query-architecture.md). BM25 relevance is exclusive to full text search. Filter queries, autocomplete and suggested queries, wildcard search, and fuzzy search queries aren't scored or ranked for relevance.
+This article explains the BM25 relevance scoring algorithm used to compute search scores for [full text search](search-lucene-query-architecture.md). BM25 relevance applies to full text search only. Filter queries, autocomplete and suggested queries, wildcard search, and fuzzy search queries aren't scored or ranked for relevance.
 
 ## Scoring algorithms used in full text search
 
@@ -133,40 +133,88 @@ In Azure AI Search, for keyword search and the text portion of a hybrid query, y
 
 ## featuresMode parameter (preview)
 
-[Search Documents](/rest/api/searchservice/documents/search-post) requests support a featuresMode parameter that provides more detail about a BM25 relevance score at the field level. Whereas the `@searchScore` is calculated for the document all-up (how relevant is this document in the context of this query), featuresMode reveals information about individual fields, as expressed in a `@search.features` structure. The structure contains all fields used in the query (either specific fields through **searchFields** in a query, or all fields attributed as **searchable** in an index). 
+> [!NOTE]
+> The `featuresMode` parameter isn't documented in the REST APIs, but you can use it on a preview REST API call to Search Documents for text (Keyword) search that's BM25-ranked.
+
+[Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&preserve-view=true) requests support a `featuresMode` parameter that provides more detail about a BM25 relevance score at the field level. Whereas the `@searchScore` is calculated for the document all-up (how relevant is this document in the context of this query), featuresMode reveals information about individual fields, as expressed in a `@search.features` structure. The structure contains all fields used in the query (either specific fields through **searchFields** in a query, or all fields attributed as **searchable** in an index).
+
+Valid values for featuresMode:
+
++ "none" (default). No feature-level scoring details are returned.
++ "enabled". Returns detailed scoring breakdowns per field
 
 For each field, `@search.features` give you the following values:
 
 + Number of unique tokens found in the field
 + Similarity score, or a measure of how similar the content of the field is, relative to the query term
 + Term frequency, or the number of times the query term was found in the field
 
-For a query that targets the "description" and "title" fields, a response that includes `@search.features` might look like this:
+This parameter is especially useful when you're trying to understand why certain documents rank higher or lower in search results. It helps explain how different fields contribute to the overall score.
+
+For a query that targets a "description" field, a request might look like this:
+
+```http
+POST {{baseUrl}}/indexes/hotels-sample-index/docs/search?api-version=2025-05-01-preview  HTTP/1.1
+  Content-Type: application/json
+  Authorization: Bearer {{accessToken}}
+
+    {
+        "search": "lake view",
+        "select": "HotelId, HotelName, Tags, Description",
+        "featuresMode": "enabled",
+        "searchFields": "Description, Tags",
+        "count": true
+    }
+```
+
+A response that includes `@search.features` might look like the following example.
 
 ```json
-"value": [
- {
-    "@search.score": 5.1958685,
-    "@search.features": {
-        "description": {
-            "uniqueTokenMatches": 1.0,
-            "similarityScore": 0.29541412,
-            "termFrequency" : 2
+  "value": [
+    {
+      "@search.score": 3.0860271,
+      "@search.features": {
+        "Description": {
+          "uniqueTokenMatches": 2.0,
+          "similarityScore": 3.0860272,
+          "termFrequency": 2.0
+        }
+      },
+      "HotelName": "Downtown Mix Hotel",
+      "Description": "Mix and mingle in the heart of the city. Shop and dine, mix and mingle in the heart of downtown, where fab lake views unite with a cheeky design.",
+      "Tags": [
+        "air conditioning",
+        "laundry service",
+        "free wifi"
+      ]
+    },
+    {
+      "@search.score": 2.7294855,
+      "@search.features": {
+        "Description": {
+          "uniqueTokenMatches": 1.0,
+          "similarityScore": 1.6023184,
+          "termFrequency": 1.0
         },
-        "title": {
-            "uniqueTokenMatches": 3.0,
-            "similarityScore": 1.75451557,
-            "termFrequency" : 6
+        "Tags": {
+          "uniqueTokenMatches": 1.0,
+          "similarityScore": 1.1271671,
+          "termFrequency": 1.0
         }
+      },
+      "HotelName": "Ocean Water Resort & Spa",
+      "Description": "New Luxury Hotel for the vacation of a lifetime. Bay views from every room, location near the pier, rooftop pool, waterfront dining & more.",
+      "Tags": [
+        "view",
+        "pool",
+        "restaurant"
+      ]
     }
- }
-]
+  ]
 ```
 
 You can consume these data points in [custom scoring solutions](https://github.com/Azure-Samples/search-ranking-tutorial) or use the information to debug search relevance problems.
 
-The featuresMode parameter isn't documented in the REST APIs, but you can use it on a preview REST API call to Search Documents for text (Keyword) search that's BM25-ranked.
-
 ## Number of ranked results in a full text query response
 
 By default, if you aren't using pagination, the search engine returns the top 50 highest ranking matches for full text search. You can use the `top` parameter to return a smaller or larger number of items (up to 1,000 in a single response). You can use `skip` and `next` to page results. Paging determines the number of results on each logical page and supports content navigation. For more information, see [Shape search results](search-pagination-page-layout.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "BM25スコアリングアルゴリズムに関するドキュメントの修正"
}
```

### Explanation
この変更は、Azure AI SearchにおけるBM25スコアリングアルゴリズムに関する文書の更新です。主な修正内容は、ドキュメントの日付が2025年1月17日から2025年8月13日に変更されたこと、そしていくつかの説明が明確化された点です。

特に、BM25の関連性スコアがフルテキスト検索のみに適用されることが強調され、関連のないクエリ（フィルタークエリ、オートコンプリート、サジェストクエリなど）がスコアリングの対象外であることが再確認されました。

さらに、`featuresMode`パラメーターに関する詳細な情報が追加されました。このパラメーターは、BM25スコアのフィールドレベルでの詳細を提供するもので、特にどのフィールドがスコアにどのように寄与しているかを理解するために役立ちます。新たに有効化された値の選択肢として、「none」（デフォルト）および「enabled」（詳細スコアリングを返す）が紹介されました。

また、具体的なリクエストとレスポンスの例も提供され、ユーザーが実際にどのようにこのパラメーターを使用できるかが示されています。この更新により、ユーザーはより効果的に検索結果の関連性を理解し、デバッグ方法を改善できるようになります。ドキュメント全体が整理され、情報の明確性が向上したことも特徴的です。

## articles/search/search-features-list.md{#item-d34448}

<details>
<summary>Diff</summary>
````diff
@@ -10,27 +10,43 @@ ms.update-cycle: 90-days
 ms.custom:
   - ignite-2024
 ms.topic: conceptual
-ms.date: 05/08/2025
+ms.date: 08/13/2025
 ---
 
 # Features of Azure AI Search
 
 Azure AI Search provides information retrieval and uses optional AI integration to extract more value from text and vector content.
 
-The following table summarizes features by category. There's feature parity in all Azure public, private, and sovereign clouds, but some features aren't supported in specific regions. For more information, see [Choose a region](search-region-support.md).
+The following table summarizes features by category. There's feature parity in all Azure public, private, and sovereign clouds, but some features aren't supported in [specific regions](search-region-support.md) or [specific tiers](search-sku-tier.md#feature-availability-by-tier).
 
 > [!NOTE]
 > Looking for preview features? See the [preview features list](search-api-preview.md).
 
-## Indexing features
+## Indexing and data extraction
 
 | Category&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Features |
 |-------------------|----------|
-| Data sources | Search indexes can accept text from any source, provided it's submitted as a JSON document. <br/><br/> [**Indexers**](search-indexer-overview.md) are a feature that automates data import from supported data sources to extract searchable content in primary data stores. Indexers handle JSON serialization for you and most support some form of change and deletion detection. You can connect to a [variety of data sources](search-data-sources-gallery.md), including [OneLake](search-how-to-index-onelake-files.md), [Azure SQL Database](search-how-to-index-sql-database.md), [Azure Cosmos DB](search-howto-index-cosmosdb.md), or [Azure Blob storage](search-howto-indexing-azure-blob-storage.md). |
+| Data sources | Search indexes can accept text from any source, provided it's submitted as a JSON document. </br></br> [**Indexers**](search-indexer-overview.md) are a feature that automates data import from supported data sources to extract searchable content in primary data stores. Indexers handle JSON serialization for you and most support some form of change and deletion detection. You can connect to a [variety of data sources](search-data-sources-gallery.md), including [OneLake (preview)](search-how-to-index-onelake-files.md), [Azure SQL Database](search-how-to-index-sql-database.md), [Azure Cosmos DB](search-howto-index-cosmosdb.md), or [Azure Blob storage](search-howto-indexing-azure-blob-storage.md).  </br></br>[**Logic Apps connectors (preview)**](search-how-to-index-logic-apps-indexers.md) give you access to a broader range of data sources, including data on other cloud platforms. This indexing and enrichment pipeline is created in Azure AI Search but managed in Azure Logic Apps.|
 | Hierarchical and nested data structures | [**Complex types**](search-howto-complex-data-types.md) and collections allow you to model virtually any type of JSON structure within a search index. One-to-many and many-to-many cardinality can be expressed natively through collections, complex types, and collections of complex types.|
-| Linguistic analysis | Analyzers are components used for text processing during indexing and search operations. By default, you can use the general-purpose Standard Lucene analyzer, or override the default with a language analyzer, a custom analyzer that you configure, or another predefined analyzer that produces tokens in the format you require. <br/><br/>[**Language analyzers**](index-add-language-analyzers.md) from Lucene or Microsoft are used to intelligently handle language-specific linguistics including verb tenses, gender, irregular plural nouns (for example, 'mouse' vs. 'mice'), word decompounding, word-breaking (for languages with no spaces), and more. <br/><br/>[**Custom lexical analyzers**](index-add-custom-analyzers.md) are used for complex query forms such as phonetic matching and regular expressions.<br/><br/> |
+| Linguistic analysis | Analyzers are components used for text processing during indexing and search operations. By default, you can use the general-purpose Standard Lucene analyzer, or override the default with a language analyzer, a custom analyzer that you configure, or another predefined analyzer that produces tokens in the format you require. </br></br>[**Language analyzers**](index-add-language-analyzers.md) from Lucene or Microsoft are used to intelligently handle language-specific linguistics including verb tenses, gender, irregular plural nouns (for example, 'mouse' vs. 'mice'), word decompounding, word-breaking (for languages with no spaces), and more. </br></br>[**Custom lexical analyzers**](index-add-custom-analyzers.md) are used for complex query forms such as phonetic matching and regular expressions.</br></br> |
 
-## Vector and hybrid search
+## Chat model and agent integration
+
+| Category&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Features |
+|-------------------|----------|
+| Chat completion models used during indexing | [**GenAI prompt skill (preview)**](cognitive-search-skill-genai-prompt.md) is a skill that calls a large language model during indexing and provides a prompt that determines the task. You decide what the task is. It might describing an image, summarizing or manipulating content, or any task the model can perform. Output is added as a new field in a searchable index. |
+| Chat completion models used at query time | [**Agentic retrieval (preview)**](search-agentic-retrieval-concept.md) uses a large language model for query planning, decomposing and paraphrasing complex queries for better query coverage over your index. Responses from agentic retrieval are designed for agent-to-agent workflows. You can pass search results as single large string, which simplifies agent consumption of your proprietary content. The response also includes citations and query execution information. </br></br>[**RAG patterns**](retrieval-augmented-generation-overview.md) can be implemented using existing capabilities. The ability to [tune for relevance](search-relevance-overview.md) and construct hybrid queries improve the quality of the content sent to chat bots for answer generation. |
+
+## Applied AI and AI enriched content
+
+| Category&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Features |
+|-------------------|----------|
+| AI processing during indexing | [**AI enrichment**](cognitive-search-concept-intro.md) refers to embedded image and natural language processing in an indexer pipeline that extracts text and information from content that can't otherwise be indexed for full text search. AI processing is achieved by adding and combining skills in a skillset, which is then attached to an indexer. AI can be either [built-in skills](cognitive-search-predefined-skills.md) from Microsoft, such as text translation or Optical Character Recognition (OCR), or [custom skills](cognitive-search-create-custom-skill-example.md) that you provide. </p>[**Integrated data chunking and vectorization**](vector-search-integrated-vectorization.md) splits up larger passages into smaller chunks that can be vectorized, with vectors routed to dedicated fields in an index for vector and hybrid search.|
+| AI processing during query execution | [**Vectorizers**](vector-search-how-to-configure-vectorizer.md) are used to encode user query strings into vectors for vector search. You can use the same embedding models for queries that you used for indexing. </p>|
+| Storing enriched content for analysis and consumption in non-search scenarios | [**Knowledge store**](knowledge-store-concept-intro.md) is persistent storage of AI enriched or AI generated content, intended for non-search scenarios like knowledge mining and data science workloads. A knowledge store is defined in a skillset, but created in Azure Storage as objects or tabular rowsets.|
+| Cached enrichments | [**Enrichment caching (preview)**](enrichment-cache-how-to-configure.md) refers to cached enrichments that can be reused during skillset execution. Caching is valuable in skillsets that include OCR and image analysis, which are expensive to process. |
+
+## Vector and hybrid retrieval
 
 | Category&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Features |
 |-------------------|----------|
@@ -42,52 +58,38 @@ The following table summarizes features by category. There's feature parity in a
 | Integrated data chunking and vectorization | Native data chunking through [Text Split skill](cognitive-search-skill-textsplit.md). Native vectorization through [vectorizers](vector-search-how-to-configure-vectorizer.md) and embedding skills such as [AzureOpenAIEmbeddingModel](cognitive-search-skill-azure-openai-embedding.md), [Azure AI Vision multimodal](cognitive-search-skill-vision-vectorize.md), and the [AML skill](cognitive-search-aml-skill.md) that you can use to connect to endpoints in the Azure AI Foundry model catalog. </p>[**Integrated vectorization**](vector-search-integrated-vectorization.md) provides an end-to-end indexing pipeline from source files to queries.|
 | Integrated vector compression and quantization | Use [built-in scalar and binary quantization](vector-search-how-to-quantization.md) to reduce vector index size in memory and on disk. You can also forego storage of vectors you don't need, or assign narrow data types to vector fields for reduced storage requirements. |
 
-## Applied AI and knowledge mining
-
-| Category&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Features |
-|-------------------|----------|
-|AI processing during indexing | [**AI enrichment**](cognitive-search-concept-intro.md) refers to embedded image and natural language processing in an indexer pipeline that extracts text and information from content that can't otherwise be indexed for full text search. AI processing is achieved by adding and combining skills in a skillset, which is then attached to an indexer. AI can be either [built-in skills](cognitive-search-predefined-skills.md) from Microsoft, such as text translation or Optical Character Recognition (OCR), or [custom skills](cognitive-search-create-custom-skill-example.md) that you provide. |
-| Storing enriched content for analysis and consumption in non-search scenarios | [**Knowledge store**](knowledge-store-concept-intro.md) is persistent storage of enriched content, intended for non-search scenarios like knowledge mining and data science processing. A knowledge store is defined in a skillset, but created in Azure Storage as objects or tabular rowsets.|
-| Cached enrichments | [**Enrichment caching (preview)**](enrichment-cache-how-to-configure.md) refers to cached enrichments that can be reused during skillset execution. Caching is particularly valuable in skillsets that include OCR and image analysis, which are expensive to process. |
-
 ## Full text and other query forms
 
 | Category&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Features |
 |-------------------|----------|
-|Free-form text search | [**Full-text search**](search-lucene-query-architecture.md) is a primary use case for most search-based apps. Queries can be formulated using a supported syntax. <br/><br/>[**Simple query syntax**](query-simple-syntax.md) provides logical operators, phrase search operators, suffix operators, precedence operators. <br/><br/>[**Full Lucene query syntax**](query-lucene-syntax.md) includes all operations in simple syntax, with extensions for fuzzy search, proximity search, term boosting, and regular expressions.|
-| Relevance | [**Simple scoring**](index-add-scoring-profiles.md) is a key benefit of Azure AI Search. Scoring profiles are used to model relevance as a function of values in the documents themselves. For example, you might want newer products or discounted products to appear higher in the search results. You can also build scoring profiles using tags for personalized scoring based on customer search preferences you've tracked and stored separately. <br/><br/>[**Semantic ranker**](semantic-search-overview.md) is premium feature that reranks results based on semantic relevance to the query. Depending on your content and scenario, it can significantly improve search relevance with almost minimal configuration or effort. |
+|Free-form text search | [**Full-text search**](search-lucene-query-architecture.md) is a primary use case for most search-based apps. Queries can be formulated using a supported syntax. </br></br>[**Simple query syntax**](query-simple-syntax.md) provides logical operators, phrase search operators, suffix operators, precedence operators. </br></br>[**Full Lucene query syntax**](query-lucene-syntax.md) includes all operations in simple syntax, with extensions for fuzzy search, proximity search, term boosting, and regular expressions.|
+| Relevance | [**Simple scoring**](index-add-scoring-profiles.md) is a key benefit of Azure AI Search. Scoring profiles are used to model relevance as a function of values in the documents themselves. For example, you might want newer products or discounted products to appear higher in the search results. You can also build scoring profiles using tags for personalized scoring based on customer search preferences you've tracked and stored separately. </br></br>[**Semantic ranker**](semantic-search-overview.md) is premium feature that reranks results based on semantic relevance to the query. Depending on your content and scenario, it can significantly improve search relevance with almost minimal configuration or effort. |
 | Geospatial search | [**Geospatial functions**](search-query-odata-geo-spatial-functions.md) filter over and match on geographic coordinates. You can [match on distance](search-query-simple-examples.md#example-6-geospatial-search) or by inclusion in a polygon shape. |
-| Filters and facets | [**Faceted navigation**](search-faceted-navigation.md) is enabled through a single query parameter. Azure AI Search returns a faceted navigation structure you can use as the code behind a categories list, for self-directed filtering (for example, to filter catalog items by price-range or brand). <br/><br/> [**Filters**](query-odata-filter-orderby-syntax.md) can be used to incorporate faceted navigation into your application's UI, enhance query formulation, and filter based on user- or developer-specified criteria. Create filters using the OData syntax. |
-| User experience | [**Autocomplete**](search-add-autocomplete-suggestions.md) can be enabled for type-ahead queries in a search bar. <br/><br/>[**Search suggestions**](/rest/api/searchservice/suggesters) also works off of partial text inputs in a search bar, but the results are actual documents in your index rather than query terms. <br/><br/>[**Synonyms**](search-synonyms.md) associates equivalent terms that implicitly expand the scope of a query, without the user having to provide the alternate terms. <br/><br/>[**Hit highlighting**](/rest/api/searchservice/documents/search-post) applies text formatting to a matching keyword in search results. You can choose which fields return highlighted snippets.<br/><br/>[**Sorting**](/rest/api/searchservice/documents/search-post) is offered for multiple fields via the index schema and then toggled at query-time with a single search parameter.<br/><br/> [**Paging**](search-pagination-page-layout.md) and throttling your search results is straightforward with the finely tuned control that Azure AI Search offers over your search results.  <br/><br/>|
+| Filters and facets | [**Faceted navigation**](search-faceted-navigation.md) is enabled through a single query parameter. Azure AI Search returns a faceted navigation structure you can use as the code behind a categories list, for self-directed filtering (for example, to filter catalog items by price-range or brand). </br></br> [**Filters**](query-odata-filter-orderby-syntax.md) can be used to incorporate faceted navigation into your application's UI, enhance query formulation, and filter based on user- or developer-specified criteria. Create filters using the OData syntax. |
+| User experience | [**Autocomplete**](search-add-autocomplete-suggestions.md) can be enabled for type-ahead queries in a search bar. </br></br>[**Search suggestions**](/rest/api/searchservice/suggesters) also works off of partial text inputs in a search bar, but the results are actual documents in your index rather than query terms. </br></br>[**Synonyms**](search-synonyms.md) associates equivalent terms that implicitly expand the scope of a query, without the user having to provide the alternate terms. </br></br>[**Hit highlighting**](/rest/api/searchservice/documents/search-post) applies text formatting to a matching keyword in search results. You can choose which fields return highlighted snippets.</br></br>[**Sorting**](/rest/api/searchservice/documents/search-post) is offered for multiple fields via the index schema and then toggled at query-time with a single search parameter.</br></br> [**Paging**](search-pagination-page-layout.md) and throttling your search results is straightforward with the finely tuned control that Azure AI Search offers over your search results.  </br></br>|
 
 ## Security features
 
 | Category&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Features |
 |-------------------|----------|
-| Data encryption | [**Microsoft-managed encryption-at-rest**](search-security-overview.md#encryption) is built into the internal storage layer and is irrevocable. <br/><br/>[**Customer-managed encryption keys**](search-security-manage-encryption-keys.md) that you create and manage in Azure Key Vault can be used for supplemental encryption of indexes and synonym maps. For services created after August 1 2020, CMK encryption extends to data on temporary disks, for full double encryption of indexed content.|
-| Endpoint protection | [**IP rules for inbound firewall support**](service-configure-firewall.md) allows you to set up IP ranges over which the search service will accept requests.<br/><br/>[**Create a private endpoint**](service-create-private-endpoint.md) using Azure Private Link to force all requests through a virtual network. |
-| Inbound access | [**Role-based access control**](search-security-rbac.md) assigns roles to users and groups in Microsoft Entra ID for controlled access to search content and operations. You can also use [**key-based authentication**](search-security-api-keys.md) if you don't want to use role assignments.|
-| Outbound security (indexers) | [**Data access through private endpoints**](search-indexer-howto-access-private.md) allows an indexer to connect to Azure resources that are protected through Azure Private Link.<br/><br/>[**Data access using a trusted identity**](search-how-to-managed-identities.md) means that connection strings to external data sources can omit user names and passwords. When an indexer connects to the data source, the resource allows the connection if the search service was previously registered as a trusted service. |
+| Network security | [**IP rules for inbound firewall support**](service-configure-firewall.md) allows you to set up IP ranges over which the search service accepts requests. </br></br>[**Create a private endpoint**](service-create-private-endpoint.md) using Azure Private Link to force all requests through a virtual network. </br></br>[**Network security perimeter**](search-security-network-security-perimeter.md) support allows you to join Azure AI Search to a network security perimeter that includes other Azure resources so that you can manage network access holistically. |
+| Data encryption | [**Microsoft-managed encryption-at-rest**](search-security-overview.md#encryption) is built into the internal storage layer and is irrevocable. </br></br>[**Customer-managed encryption keys (CMK)**](search-security-manage-encryption-keys.md) that you create and manage in Azure Key Vault can be used for supplemental encryption of indexes and synonym maps. For services created after August 1 2020, CMK encryption extends to data on temporary disks, for full double encryption of indexed content.|
+| Inbound access | [**Role-based access control**](search-security-rbac.md) assigns roles to users and groups in Microsoft Entra ID for controlled access to search content and operations. You can also use [**key-based authentication**](search-security-api-keys.md) if you don't want to use role assignments. </br></br>[**Document-level access control (preview)**](search-document-level-access-overview.md) filters out search results that a user isn't authorized to see. For several data sources, if the data source provides an access control model, you can configure an index to inherit the user permission metadata. |
+| Outbound security (indexers) | [**Data connections through private endpoints**](search-indexer-howto-access-private.md) allows an indexer to connect to Azure resources that are protected through Azure Private Link. </br></br>[**Data connections through managed identities**](search-how-to-managed-identities.md) authenticates connections to Azure resources using a Microsoft Entra security principal, which eliminates storage and passing of hardcoded API keys.</br></br>[**Data access using a trusted identity**](search-how-to-managed-identities.md) means that connection strings to external data sources can omit user names and passwords. When an indexer connects to the data source, the resource allows the connection if the search service was previously registered as a trusted service (applies to Azure Storage only). |
 
 ## Portal features
 
 | Category&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Features |
 |-------------------|----------|
-| Tools for prototyping and inspection | [**Add index**](search-what-is-an-index.md) is an index designer in the Azure portal that you can use to create a basic schema consisting of attributed fields and a few other settings. After saving the index, you can populate it using an SDK or the REST API to provide the data. <br/><br/>[**Import data wizard**](search-import-data-portal.md) creates indexes, indexers, skillsets, and data source definitions. If your data exists in Azure, this wizard can save you significant time and effort, especially for proof-of-concept investigation and exploration. <br/><br/>[**Import and vectorize data wizard**](search-get-started-portal-import-vectors.md) creates a full indexing pipeline that includes data chunking and vectorization. The wizard creates all of the objects and configuration settings. <br/><br/>[**Search explorer**](search-explorer.md) is used to test queries and refine scoring profiles.<br/><br/>[**Create demo app**](search-create-app-portal.md) is used to generate an HTML page that can be used to test the search experience.  <br/><br/>[**Debug Sessions**](cognitive-search-debug-session.md) is a visual editor that lets you debug a skillset interactively. It shows you dependencies, output, and transformations. |
+| Tools for prototyping and inspection | [**Add index**](search-what-is-an-index.md) is an index designer in the Azure portal that you can use to create a basic schema consisting of attributed fields and a few other settings. After saving the index, you can populate it using an SDK or the REST API to provide the data. </br></br>[**Import data wizard**](search-import-data-portal.md) creates indexes, indexers, skillsets, and data source definitions. If your data exists in Azure, this wizard can save you significant time and effort, especially for proof-of-concept investigation and exploration. </br></br>[**Import and vectorize data wizard**](search-get-started-portal-import-vectors.md) creates a full indexing pipeline that includes data chunking and vectorization. The wizard creates all of the objects and configuration settings. </br></br>[**Search explorer**](search-explorer.md) is used to test queries and refine scoring profiles.</br></br>[**Create demo app**](search-create-app-portal.md) is used to generate an HTML page that can be used to test the search experience.  </br></br>[**Debug Sessions**](cognitive-search-debug-session.md) is a visual editor that lets you debug a skillset interactively. It shows you dependencies, output, and transformations. |
 | Monitoring and diagnostics | [**Enable monitoring features**](monitor-azure-cognitive-search.md) to go beyond the metrics-at-a-glance that are always visible in the Azure portal. Metrics on queries per second, latency, and throttling are captured and reported in portal pages with no extra configuration required.|
 
 ## Programmability
 
 | Category&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Features |
 |-------------------|----------|
-| REST | [**Service REST API**](/rest/api/searchservice/) is for data plane operations, including all operations related to indexing, queries, and AI enrichment. You can also use this client library to retrieve system information and statistics. <br/><br/>[**Management REST API**](/rest/api/searchmanagement/) is for service creation and provisioning through Azure Resource Manager. You can also use this API to manage keys and capacity.|
-| Azure SDK for .NET | [**Azure.Search.Documents**](/dotnet/api/overview/azure/search.documents-readme) is for data plane operations, including all operations related to indexing, queries, and AI enrichment. You can also use this client library to retrieve system information and statistics. <br/><br/>[**Microsoft.Azure.Management.Search**](/dotnet/api/microsoft.azure.management.search) is for service creation and provisioning through Azure Resource Manager. You can also use this API to manage keys and capacity.|
-| Azure SDK for Java | [**com.azure.search.documents**](/java/api/com.azure.search.documents) is for data plane operations, including all operations related to indexing, queries, and AI enrichment. You can also use this client library to retrieve system information and statistics. <br/><br/>[**com.microsoft.azure.management.search**](/java/api/overview/azure/search/management) is for service creation and provisioning through Azure Resource Manager. You can also use this API to manage keys and capacity.|
-| Azure SDK for Python | [**azure-search-documents**](/python/api/overview/azure/search-documents-readme) is for data plane operations, including all operations related to indexing, queries, and AI enrichment. You can also use this client library to retrieve system information and statistics. <br/><br/>[**azure-mgmt-search**](/python/api/azure-mgmt-search/) is for service creation and provisioning through Azure Resource Manager. You can also use this API to manage keys and capacity. |
-| Azure SDK for JavaScript/TypeScript | [**azure/search-documents**](/javascript/api/@azure/search-documents/) is for data plane operations, including all operations related to indexing, queries, and AI enrichment. You can also use this client library to retrieve system information and statistics. <br/><br/>[**azure/arm-search**](/javascript/api/@azure/arm-search/) is for service creation and provisioning through Azure Resource Manager. You can also use this API to manage keys and capacity. |
-
-## See also
-
-+ [What's new in Azure AI Search](whats-new.md)
-
-+ [Preview features in Azure AI Search](search-api-preview.md)
+| REST | [**Service REST API**](/rest/api/searchservice/) is for data plane operations, including all operations related to indexing, queries, and AI enrichment. You can also use this client library to retrieve system information and statistics. </br></br>[**Management REST API**](/rest/api/searchmanagement/) is for service creation and provisioning through Azure Resource Manager. You can also use this API to manage keys and capacity.|
+| Azure SDK for .NET | [**Azure.Search.Documents**](/dotnet/api/overview/azure/search.documents-readme) is for data plane operations, including all operations related to indexing, queries, and AI enrichment. You can also use this client library to retrieve system information and statistics. </br></br>[**Microsoft.Azure.Management.Search**](/dotnet/api/microsoft.azure.management.search) is for service creation and provisioning through Azure Resource Manager. You can also use this API to manage keys and capacity.|
+| Azure SDK for Java | [**com.azure.search.documents**](/java/api/com.azure.search.documents) is for data plane operations, including all operations related to indexing, queries, and AI enrichment. You can also use this client library to retrieve system information and statistics. </br></br>[**com.microsoft.azure.management.search**](/java/api/overview/azure/search/management) is for service creation and provisioning through Azure Resource Manager. You can also use this API to manage keys and capacity.|
+| Azure SDK for Python | [**azure-search-documents**](/python/api/overview/azure/search-documents-readme) is for data plane operations, including all operations related to indexing, queries, and AI enrichment. You can also use this client library to retrieve system information and statistics. </br></br>[**azure-mgmt-search**](/python/api/azure-mgmt-search/) is for service creation and provisioning through Azure Resource Manager. You can also use this API to manage keys and capacity. |
+| Azure SDK for JavaScript/TypeScript | [**azure/search-documents**](/javascript/api/@azure/search-documents/) is for data plane operations, including all operations related to indexing, queries, and AI enrichment. You can also use this client library to retrieve system information and statistics. </br></br>[**azure/arm-search**](/javascript/api/@azure/arm-search/) is for service creation and provisioning through Azure Resource Manager. You can also use this API to manage keys and capacity. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search機能リストの更新"
}
```

### Explanation
この変更は、Azure AI Searchの機能リストに関するドキュメントの更新です。主な修正には、ドキュメントの日付が2025年5月8日から2025年8月13日に変更され、機能のカテゴリや説明の一部が改訂されました。

特に、インデクシング機能のセクションは「インデクシングとデータ抽出」に名称が変更され、関連する情報が統合されました。また、データソースの項目に「OneLake (プレビュー)」が追加され、データソースの接続に関する新しい情報が提供されています。さらに、インデクシングおよびクエリ時のAI処理に関する新しい機能や、チャットモデルやエージェントとの統合についての詳細が追加されて、より包括的な情報が整備されました。

ドキュメントの構造も見直され、セクション間の明瞭さが向上しています。たとえば、セキュリティ機能のセクションが強化され、ネットワークセキュリティ、データ暗号化、ロールベースのアクセス制御に関する新情報が加わりました。

最後に、APIとSDKに関する情報が整理されており、各言語ごとのSDKへのリンクも明示されています。この全体的な更新により、ユーザーはAzure AI Searchのさまざまな機能をより効果的に理解しやすくなっています。

## articles/search/search-how-to-index-logic-apps-indexers.md{#item-64a12e}

<details>
<summary>Diff</summary>
````diff
@@ -111,7 +111,7 @@ Follow these steps to create a logic app workflow for indexing content in Azure
 
 1. Start the Import and vectorize data wizard in the Azure portal.
 
-1. Choose a [supported Azure Logic Apps indexer](#supported-connectors).
+1. Choose a [supported Azure Logic Apps connector](#supported-connectors).
 
    :::image type="content" source="media/logic-apps-connectors/choose-data-source.png" alt-text="Screenshot of the chosen data source page in the Import and vectorize data wizard." lightbox="media/logic-apps-connectors/choose-data-source.png" :::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Logic Appsインデクサーに関する用語の修正"
}
```

### Explanation
この変更は、Azure Logic Appsに関するドキュメント内での用語の修正を含んでいます。具体的には、「supported Azure Logic Apps indexer」という表現が「supported Azure Logic Apps connector」に変更されました。この修正は、文書の明確性と正確性を向上させるために行われたものです。

ドキュメントの中でインデクサーという用語の代わりにコネクターという用語を使用することで、Azure Logic Appsでのデータのインデクシング処理に関するより適切な表現が提供されます。このような用語の一貫性は、読者がサポートされている機能を理解しやすくするのに役立ちます。全体として、小規模な変更ですが、文書の品質を高めるための重要な一歩と言えます。


