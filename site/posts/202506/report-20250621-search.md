---
date: '2025-06-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fc0b900...MicrosoftDocs:fb526ea
summary: この一連の変更では、Azure AI Searchの文書に対して、特にベクトルインデックスおよび検索に関連する内容の修正と改善が行われました。新機能として、ベクトルインデックス作成やベクトル検索機能に関する詳細なガイドラインが追加され、使用方法が強化されました。また、目次構成の見直しによりアクセス性が向上し、文書全体の可読性と整合性が高まりました。さらに、「Vector
  store」という名称が「Vector index」に変更され、一部構成名が修正されましたが、これにより既存のユーザーが混乱する可能性もあります。全体的に、これらの変更はユーザーがベクトル検索機能をより効率的に活用できるようにすることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fc0b900...MicrosoftDocs:fb526ea){target="_blank"}

<format>
# ハイライト
この一連の変更では、Azure AI Searchの文書に対して主にベクトルインデックスおよび検索に関連する内容について細かな修正と改善が行われました。具体的な特徴としては、新機能の説明の強化、文書の構成改善、そしてユーザーの理解を助けるためのガイドラインの詳細化が挙げられます。特に、目次構成の見直しによるアクセス性の向上、ベクトルフィールドと非ベクトルフィールドの共存に関する新しい情報の追加が含まれます。

## 新機能
- ベクトルインデックス作成やベクトル検索機能の使用方法に関する詳細なガイドラインの追加。
- 「低スコアの結果を除外するための閾値」設定などのプレビュー機能が導入され、機能の使用方法が強化された。

## 破壊的変更
- 「Vector store」という名称が目次で「Vector index」に変更され、構成名が一部修正されています。これにより、既存のユーザーが混乱する可能性がありますが、文書全体として一貫性が増しました。

## その他の更新
- 文書全般での文法修正、日付の更新、構成改善が行われ、可読性と整合性が高まりました。
- インデックスやクエリの説明に関して具体性が増し、ユーザーガイドラインが改訂されています。

# インサイト
このドキュメントの一連の変更は、Azure AI Searchを利用するユーザーがより効率的かつ効果的にベクトル検索機能を活用できるようにするための計画的な改善を反映しています。検索インデックスおよびベクトル検索に関する文書の更新は、先進的な機能の利用に必要な詳細な技術情報とガイドラインを提供します。

まず、ベクトルインデックスの文書では、シェーマ定義やベクトルアルゴリズムの導入方法が改善され、開発者やデータサイエンティストがインデックスをより具体的に設定できるようになりました。これにより、ベクトル化戦略の策定やインデックス作成の効率が向上します。

ベクトル検索のクエリ文書でも、より明確で具体的な指針が提供され、AzureポータルやREST APIを活用した実装がしやすくなっています。新たなプレビュー機能の紹介により、将来的な機能拡張に備える意図も伺えます。

また、目次（toc.yml）の更新は、多様なユーザーのニーズに応えるものです。索引構成とセクションの調整により、重要な情報に迅速にアクセスできるようになり、学習曲線が緩和されます。

全体として、これらのアップデートはユーザーのエクスペリエンス向上に焦点を当てており、Azure AI Searchの採用を促進するものと考えられます。今後も継続的にユーザーフィードバックを取り入れることで、さらなる改善が期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-what-is-an-index.md](#item-5a3344) | minor update | 検索インデックスに関する内容の更新 | modified | 23 | 22 | 45 | 
| [toc.yml](#item-c4768f) | minor update | 検索インデックスの目次構成の変更 | modified | 124 | 124 | 248 | 
| [vector-search-how-to-create-index.md](#item-97c769) | minor update | ベクトルインデックス作成に関するドキュメントの更新 | modified | 77 | 77 | 154 | 
| [vector-search-how-to-query.md](#item-9bb93c) | minor update | ベクトル検索クエリに関するドキュメントの更新 | modified | 76 | 75 | 151 | 
| [vector-search-overview.md](#item-56e5fa) | minor update | Azure AI Searchにおけるベクトル検索の概要の更新 | modified | 78 | 67 | 145 | 
| [vector-store.md](#item-db9b8c) | minor update | Azure AI Searchにおけるベクトルストレージの概要の更新 | modified | 99 | 67 | 166 | 


# Modified Contents
## articles/search/search-what-is-an-index.md{#item-5a3344}

<details>
<summary>Diff</summary>
````diff
@@ -11,20 +11,21 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 05/19/2025
+ms.date: 06/20/2025
 ---
 
 # Search indexes in Azure AI Search
 
-In Azure AI Search, a *search index* is your searchable content, available to the search engine for indexing, full text search, vector search, hybrid search, and filtered queries. An index is defined by a schema and saved to the search service, with data import following as a second step. This content exists within your search service, apart from your primary data stores, which is necessary for the millisecond response times expected in modern search applications. Except for indexer-driven indexing scenarios, the search service never connects to or queries your source data.
+In Azure AI Search, a *search index* is your searchable content, available to the search engine for indexing, full-text search, vector search, hybrid search, and filtered queries. An index is defined by a schema and saved to the search service, with data import following as a second step. This content exists within your search service, apart from your primary data stores, which is necessary for the millisecond response times expected in modern search applications. Except for indexer-driven indexing scenarios, the search service never connects to or queries your source data.
 
-If you want to create and manage a search index, this article helps you understand the following points:
+This article covers the key concepts for creating and managing a search index, including:
 
 + Content (documents and schema)
 + Physical data structure
 + Basic operations
 
-Prefer to be hands-on right away? See [Create a search index](search-how-to-create-search-index.md) instead.
+> [!TIP]
+> Want to get started right away? See [Create a search index](search-how-to-create-search-index.md).
 
 ## Schema of a search index
 
@@ -111,21 +112,21 @@ Although you can add new fields at any time, existing field definitions are lock
 
 ## Physical structure and size
 
-In Azure AI Search, the physical structure of an index is largely an internal implementation. You can access its schema, query its content, monitor its size, and manage capacity, but the clusters themselves (inverted indexes, vector indexes, [shards](index-similarity-and-scoring.md#sharding-effects-on-query-results), and other files and folders) are managed internally by Microsoft.
+In Azure AI Search, the physical structure of an index is largely an internal implementation. You can access its schema, load and query its content, monitor its size, and manage its capacity. However, Microsoft manages the infrastructure and physical data structures stored with your search service.
 
-You can monitor index size in the **Search management > Indexes** page in the Azure portal, or by issuing a [GET INDEX request](/rest/api/searchservice/indexes/get) against your search service. You can also issue a [Service Statistics request](/rest/api/searchservice/get-service-statistics/get-service-statistics) and check the value of storage size.
+You can monitor index size on the **Search management > Indexes** page in the Azure portal. Alternatively, you can issue a [GET INDEX request](/rest/api/searchservice/indexes/get) against your search service or a [Service Statistics request](/rest/api/searchservice/get-service-statistics/get-service-statistics) to check the value of storage size.
 
-The size of an index is determined by:
+The size of an index is determined by the:
 
-+ Quantity and composition of your documents
-+ Attributes on individual fields
-+ Index configuration (specifically, whether you include suggesters)
++ Quantity and composition of your documents.
++ Attributes on individual fields.
++ Index configuration. Specifically, whether you include suggesters.
 
-Document composition and quantity are determined by what you choose to import. Remember that a search index should only contain searchable content. If source data includes binary fields, omit those fields unless you're using AI enrichment to crack and analyze the content to create text searchable information.
+Document composition and quantity are determined by what you choose to import. Remember that a search index should only contain searchable content. If source data includes binary fields, omit those fields unless you're using AI enrichment to crack and analyze the content to create text-searchable information.
 
-Field attributes determine behaviors. To support those behaviors, the indexing process creates the necessary data structures. For example, for a field of type `Edm.String`, "searchable" invokes [full text search](search-lucene-query-architecture.md), which scans inverted indexes for the tokenized term. In contrast, a "filterable" or "sortable" attribute supports iteration over unmodified strings. The example in the next section shows variations in index size based on the selected attributes.
+Field attributes determine behaviors. To support those behaviors, the indexing process creates the necessary data structures. For example, for a field of type `Edm.String`, "searchable" invokes [full-text search](search-lucene-query-architecture.md), which scans inverted indexes for the tokenized term. In contrast, a "filterable" or "sortable" attribute supports iteration over unmodified strings. The example in the next section shows variations in index size based on the selected attributes.
 
-[**Suggesters**](index-add-suggesters.md) are constructs that support type-ahead or autocomplete queries. As such, when you include a suggester, the indexing process creates the data structures necessary for verbatim character matches. Suggesters are implemented at the field level, so choose only those fields that are reasonable for type-ahead.
+[**Suggesters**](index-add-suggesters.md) are constructs that support type-ahead or autocomplete queries. When you include a suggester, the indexing process creates the data structures necessary for verbatim character matches. Suggesters are implemented at the field level, so choose only those fields that are reasonable for type-ahead.
 
 ### Example demonstrating the storage implications of attributes and suggesters
 
@@ -143,33 +144,33 @@ Also not reflected in the previous table is the effect of [analyzers](search-ana
 
 ## Basic operations and interaction
 
-Now that you have a better idea of what an index is, this section introduces index run time operations, including connecting to and securing a single index.
+Now that you have a better idea of what an index is, this section introduces index runtime operations, including connecting to and securing a single index.
 
 > [!NOTE]
-> When managing an index, be aware that there is no portal or API support for moving or copying an index. Instead, customers typically point their application deployment solution at a different search service (if using the same index name), or revise the name to create a copy on the current search service, and then build it.
+> There's no portal or API support for moving or copying an index. Typically, you either point your application deployment to a different search service (using the same index name) or revise the name to create a copy on your current search service and then build it.
 
 ### Index isolation
   
-In Azure AI Search, you work with one index at a time, where all index-related operations target a single index. There's no concept of related indexes or the joining of independent indexes for either indexing or querying. 
+In Azure AI Search, you work with one index at a time. All index-related operations target a single index. There's no concept of related indexes or the joining of independent indexes for either indexing or querying.
 
 ### Continuously available
 
-An index is immediately available for queries as soon as the first document is indexed, but won't be fully operational until all documents are indexed. Internally, a search index is [distributed across partitions and executes on replicas](search-capacity-planning.md#concepts-search-units-replicas-partitions). The physical index is managed internally. The logical index is managed by you.
+An index is immediately available for queries as soon as the first document is indexed, but it's not fully operational until all documents are indexed. Internally, an index is [distributed across partitions and executes on replicas](search-capacity-planning.md#concepts-search-units-replicas-partitions). The physical index is managed internally. You manage the logical index.
 
-An index is continuously available, with no ability to pause or take it offline. Because it's designed for continuous operation, any updates to its content, or additions to the index itself, happen in real time. As a result, queries might temporarily return incomplete results if a request coincides with a document update.
+An index is continuously available and can't be paused or taken offline. Because it's designed for continuous operation, updates to its content and additions to the index itself happen in real time. If a request coincides with a document update, queries might temporarily return incomplete results.
 
-Notice that query continuity exists for document operations (refreshing or deleting) and for modifications that don't affect the existing structure and integrity of the current index (such as adding new fields). If you need to make structural updates (changing existing fields), those are typically managed using a drop-and-rebuild workflow in a development environment, or by creating a new version of the index on production service.
+Query continuity exists for document operations, such as refreshing or deleting, and for modifications that don't affect the existing structure or integrity of an index, such as adding new fields. Structural updates, such as changing existing fields, are typically managed using a drop-and-rebuild workflow in a development environment or by creating a new version of the index on the production service.
 
-To avoid an [index rebuild](search-howto-reindex.md), some customers who are making small changes choose to "version" a field by creating a new one that coexists alongside a previous version. Over time, this leads to orphaned content in the form of obsolete fields or obsolete custom analyzer definitions, especially in a production index that is expensive to replicate. You can address these issues on planned updates to the index as part of index lifecycle management.
+To avoid an [index rebuild](search-howto-reindex.md), some customers who are making small changes "version" a field by creating a new one that coexists with a previous version. Over time, this leads to orphaned content by way of obsolete fields and obsolete custom analyzer definitions, especially in a production index that's expensive to replicate. You can address these issues during planned updates to the index as part of index lifecycle management.
 
 ### Endpoint connection and security
 
 All indexing and query requests target an index. Endpoints are usually one of the following:
 
 | Endpoint | Connection and access control |
 |----------|-------------------------------|
-| `<your-service>.search.windows.net/indexes` | Targets the indexes collection. Used when creating, listing, or deleting an index. Admin rights are required for these operations, available through admin [API keys](search-security-api-keys.md) or a [Search Contributor role](search-security-rbac.md#built-in-roles-used-in-search). |
-| `<your-service>.search.windows.net/indexes/<your-index>/docs` | Targets the documents collection of a single index. Used when querying an index or data refresh. For queries, read rights are sufficient, and available through query API keys or a data reader role. For data refresh, admin rights are required. |
+| `<your-service>.search.windows.net/indexes` | Targets the indexes collection. Used when creating, listing, or deleting an index. Admin rights are required for these operations and available through admin [API keys](search-security-api-keys.md) or a [Search Contributor role](search-security-rbac.md#built-in-roles-used-in-search). |
+| `<your-service>.search.windows.net/indexes/<your-index>/docs` | Targets the documents collection of a single index. Used when querying an index or data refresh. For queries, read rights are sufficient and available through query API keys or a data reader role. For data refresh, admin rights are required. |
 
 #### How to connect to Azure AI Search
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスに関する内容の更新"
}
```

### Explanation
この変更では、Azure AI Searchにおける検索インデックスの文書に関するいくつかの修正と更新が行われました。修正内容には、情報の明確化、文法の改善、及び文章の組織に関する要素が含まれています。具体的には、日付の更新、文章のスタイルの統一、及びリスト形式の明確な説明がなされました。また、インデックスの物理構造とサイズに関する記述がより詳細になり、構文の一貫性を持たせるために複数の箇所で表現の修正が行われました。

全体として、この文書はユーザーにとっての理解を深めるために、情報が整理され、現代の検索アプリケーションに求められる情報が強調されています。更新内容は、特に検索インデックスの作成と管理に関する基本的な概念の理解を助けるものです。このように、文書の品質と正確性が向上することで、ユーザーはAzure AI Searchの機能をより効果的に利用できるようになります。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -154,7 +154,7 @@ items:
     items:
     - name: Search index
       href: search-what-is-an-index.md
-    - name: Vector store
+    - name: Vector index
       href: vector-store.md
     - name: Knowledge store
       href: knowledge-store-concept-intro.md
@@ -240,8 +240,6 @@ items:
         href: search-howto-move-across-regions.md
   - name: Indexing
     items:
-    - name: Index via portal wizards
-      href: search-import-data-portal.md
     - name: Create an index
       href: search-how-to-create-search-index.md
     - name: Load an index
@@ -252,6 +250,26 @@ items:
       href: search-how-to-alias.md
     - name: Import large data sets
       href: search-how-to-large-index.md
+    - name: Text indexing
+      items:
+      - name: Add synonyms
+        href: search-synonyms.md
+      - name: Add a suggester for typeahead
+        href: index-add-suggesters.md
+      - name: Design a multilingual index
+        href: search-language-support.md
+      - name: Model complex data types
+        href: search-howto-complex-data-types.md
+      - name: Model relational data
+        href: index-sql-relational-data.md
+      - name: Analyzers
+        items:
+        - name: Analyzers overview
+          href: search-analyzers.md
+        - name: Add a language analyzer
+          href: index-add-language-analyzers.md
+        - name: Add a custom analyzer
+          href: index-add-custom-analyzers.md
     - name: Vector indexing
       items:
       - name: Create a vector index
@@ -282,134 +300,116 @@ items:
           href: vector-search-how-to-storage-options.md
         - name: Truncate dimensions
           href: vector-search-how-to-truncate-dimensions.md
-    - name: Text indexing
+  - name: Indexer and enrichment pipelines
+    items:
+    - name: Index via portal wizards
+      href: search-import-data-portal.md
+    - name: Logic Apps workflows
       items:
-      - name: Add synonyms
-        href: search-synonyms.md
-      - name: Add a suggester for typeahead
-        href: index-add-suggesters.md
-      - name: Design a multilingual index
-        href: search-language-support.md
-      - name: Model complex data types
-        href: search-howto-complex-data-types.md
-      - name: Model relational data
-        href: index-sql-relational-data.md
-      - name: Analyzers
+      - name: Create a workflow
+        href: search-how-to-index-logic-apps-indexers.md
+    - name: Indexers
+      items:
+      - name: Create an indexer
+        href: search-howto-create-indexers.md
+      - name: Run or reset indexers
+        href: search-howto-run-reset-indexers.md
+      - name: Schedule an indexer
+        href: search-howto-schedule-indexers.md
+      - name: Define field mappings
+        href: search-indexer-field-mappings.md
+      - name: Indexing whole files
         items:
-        - name: Analyzers overview
-          href: search-analyzers.md
-        - name: Add a language analyzer
-          href: index-add-language-analyzers.md
-        - name: Add a custom analyzer
-          href: index-add-custom-analyzers.md
-    - name: Indexing and enrichment pipelines
+        - name: Content metadata properties
+          href: search-blob-metadata-properties.md
+        - name: Index one-to-many
+          href: search-howto-index-one-to-many-blobs.md
+        - name: Index plain text
+          href: search-howto-index-plaintext-blobs.md
+        - name: Index CSV
+          href: search-how-to-index-csv-blobs.md
+        - name: Index JSON
+          href: search-howto-index-json-blobs.md
+        - name: Index Markdown
+          href: search-how-to-index-markdown-blobs.md
+      - name: Troubleshooting guidance
+        href: search-indexer-troubleshooting.md
+      - name: Troubleshoot indexer errors and warnings
+        href: cognitive-search-common-errors-warnings.md
+    - name: Data sources (indexers)
       items:
-      - name: Logic Apps workflows
+      - name: Data sources gallery
+        href: search-data-sources-gallery.md
+      - name: Azure Storage
         items:
-        - name: Create a workflow
-          href: search-how-to-index-logic-apps-indexers.md
-      - name: Indexers
+        - name: Search over blobs
+          href: search-blob-storage-integration.md
+        - name: ADLS Gen2
+          href: search-howto-index-azure-data-lake-storage.md
+        - name: Blobs
+          href: search-howto-indexing-azure-blob-storage.md
+        - name: Files
+          href: search-file-storage-integration.md
+        - name: Tables
+          href: search-howto-indexing-azure-tables.md
+        - name: Index changed and deleted content
+          href: search-howto-index-changed-deleted-blobs.md
+      - name: Azure Cosmos DB
         items:
-        - name: Create an indexer
-          href: search-howto-create-indexers.md
-        - name: Run or reset indexers
-          href: search-howto-run-reset-indexers.md
-        - name: Schedule an indexer
-          href: search-howto-schedule-indexers.md
-        - name: Define field mappings
-          href: search-indexer-field-mappings.md
-        - name: Indexing whole files
-          items:
-          - name: Content metadata properties
-            href: search-blob-metadata-properties.md
-          - name: Index one-to-many
-            href: search-howto-index-one-to-many-blobs.md
-          - name: Index plain text
-            href: search-howto-index-plaintext-blobs.md
-          - name: Index CSV
-            href: search-how-to-index-csv-blobs.md
-          - name: Index JSON
-            href: search-howto-index-json-blobs.md
-          - name: Index Markdown
-            href: search-how-to-index-markdown-blobs.md
-        - name: Troubleshooting guidance
-          href: search-indexer-troubleshooting.md
-        - name: Troubleshoot indexer errors and warnings
-          href: cognitive-search-common-errors-warnings.md
-      - name: Data sources (indexers)
+        - name: Azure Cosmos DB for NoSQL
+          href: search-howto-index-cosmosdb.md
+        - name: Azure Cosmos DB for MongoDB
+          href: search-howto-index-cosmosdb-mongodb.md
+        - name: Azure Cosmos DB for Apache Gremlin
+          href: search-howto-index-cosmosdb-gremlin.md
+      - name: Azure DB for MySQL
+        href: search-howto-index-mysql.md
+      - name: Azure SQL
         items:
-        - name: Data sources gallery
-          href: search-data-sources-gallery.md
-        - name: Azure Storage
-          items:
-          - name: Search over blobs
-            href: search-blob-storage-integration.md
-          - name: ADLS Gen2
-            href: search-howto-index-azure-data-lake-storage.md
-          - name: Blobs
-            href: search-howto-indexing-azure-blob-storage.md
-          - name: Files
-            href: search-file-storage-integration.md
-          - name: Tables
-            href: search-howto-indexing-azure-tables.md
-          - name: Index changed and deleted content
-            href: search-howto-index-changed-deleted-blobs.md
-        - name: Azure Cosmos DB
-          items:
-          - name: Azure Cosmos DB for NoSQL
-            href: search-howto-index-cosmosdb.md
-          - name: Azure Cosmos DB for MongoDB
-            href: search-howto-index-cosmosdb-mongodb.md
-          - name: Azure Cosmos DB for Apache Gremlin
-            href: search-howto-index-cosmosdb-gremlin.md
-        - name: Azure DB for MySQL
-          href: search-howto-index-mysql.md
-        - name: Azure SQL
-          items:
-          - name: Azure SQL Databases
-            href: search-how-to-index-sql-database.md
-          - name: Azure SQL Managed Instances
-            href: search-how-to-index-sql-managed-instance.md
-          - name: Azure SQL Server VMs
-            href: search-how-to-index-sql-server.md
-        - name: OneLake files
-          href: search-how-to-index-onelake-files.md
-        - name: SharePoint Online
-          href: search-howto-index-sharepoint-online.md
-      - name: Skillsets (indexers)
+        - name: Azure SQL Databases
+          href: search-how-to-index-sql-database.md
+        - name: Azure SQL Managed Instances
+          href: search-how-to-index-sql-managed-instance.md
+        - name: Azure SQL Server VMs
+          href: search-how-to-index-sql-server.md
+      - name: OneLake files
+        href: search-how-to-index-onelake-files.md
+      - name: SharePoint Online
+        href: search-howto-index-sharepoint-online.md
+    - name: Skillsets (indexers)
+      items:
+      - name: Create a skillset
+        href: cognitive-search-defining-skillset.md
+      - name: Attach an Azure AI resource
+        href: cognitive-search-attach-cognitive-services.md
+      - name: Define an index projection
+        href: search-how-to-define-index-projections.md
+      - name: Debug sessions overview
+        href: cognitive-search-debug-session.md
+      - name: Debug a skillset
+        href: cognitive-search-how-to-debug-skillset.md
+      - name: Reference a skill output
+        href: cognitive-search-concept-annotations-syntax.md
+      - name: Map to index fields
+        href: cognitive-search-output-field-mapping.md
+      - name: Process image files
+        href: cognitive-search-concept-image-scenarios.md
+      - name: Cache (incremental) enrichment
+        href: search-howto-incremental-index.md
+      - name: Design tips
+        href: cognitive-search-concept-troubleshooting.md
+      - name: Best practices - GenAI Prompt skill
+        href: responsible-ai-best-practices-genai-prompt-skill.md
+      - name: GenAI Prompt Skill - Example Usage Guide
+        href: chat-completion-skill-example-usage.md
+      - name: Custom skills
         items:
-        - name: Create a skillset
-          href: cognitive-search-defining-skillset.md
-        - name: Attach an Azure AI resource
-          href: cognitive-search-attach-cognitive-services.md
-        - name: Define an index projection
-          href: search-how-to-define-index-projections.md
-        - name: Debug sessions overview
-          href: cognitive-search-debug-session.md
-        - name: Debug a skillset
-          href: cognitive-search-how-to-debug-skillset.md
-        - name: Reference a skill output
-          href: cognitive-search-concept-annotations-syntax.md
-        - name: Map to index fields
-          href: cognitive-search-output-field-mapping.md
-        - name: Process image files
-          href: cognitive-search-concept-image-scenarios.md
-        - name: Cache (incremental) enrichment
-          href: search-howto-incremental-index.md
-        - name: Design tips
-          href: cognitive-search-concept-troubleshooting.md
-        - name: Best practices - GenAI Prompt skill
-          href: responsible-ai-best-practices-genai-prompt-skill.md
-        - name: GenAI Prompt Skill - Example Usage Guide
-          href: chat-completion-skill-example-usage.md
-        - name: Custom skills
-          items:
-          - name: Integrate custom skills
-            href: cognitive-search-custom-skill-interface.md
-          - name: Scale out custom skills
-            href: cognitive-search-custom-skill-scale.md
-          - name: Example - Bing Entity Search
-            href: cognitive-search-create-custom-skill-example.md
+        - name: Integrate custom skills
+          href: cognitive-search-custom-skill-interface.md
+        - name: Scale out custom skills
+          href: cognitive-search-custom-skill-scale.md
+        - name: Example - Bing Entity Search
+          href: cognitive-search-create-custom-skill-example.md
   - name: Retrieval
     items:
     - name: Agentic retrieval
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスの目次構成の変更"
}
```

### Explanation
この変更では、Azure AI Searchに関する目次（toc.yml）の構成が大幅に更新されました。主な変更点には、項目名のさまざまな修正や、関連するドキュメントへのリンクの追加が含まれています。例えば、「Vector store」という名前が「Vector index」に変更され、新しいインデックス作成に関連する詳細なセクションが追加されました。

また、テキスト索引に関連するサブセクションが導入され、同義語の追加、タイプアヘッド用のサジェスターの追加、多言語インデックスの設計などに関するガイドが整備されました。さらに、インデクサーとエンリッチメントパイプラインに関する新しい情報や、ロジックアプリワークフローの作成に関する項目も新たに追加され、ユーザーに必要な情報を手に入れやすくすることが意図されています。

このような詳細な目次の更新により、ユーザーが検索インデックスをより効果的に理解し、利用できるような情報提供が強化されました。全体的に、この変更はドキュメントのナビゲーションを改善し、ユーザーエクスペリエンスを向上させることを目指しています。

## articles/search/vector-search-how-to-create-index.md{#item-97c769}

<details>
<summary>Diff</summary>
````diff
@@ -9,65 +9,65 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 06/11/2025
+ms.date: 06/20/2025
 ---
 
 # Create a vector index
 
-In Azure AI Search, you can store vectors in a search index and send vector queries for matching based on semantic similarity. A vector index is defined by an index schema that has: vector fields, nonvector fields, and a vector configuration section.
+In Azure AI Search, you can store vectors in a search index and send vector queries for matching based on semantic similarity. A vector index is defined by an index schema that has vector fields, nonvector fields, and a vector configuration section.
 
-[Create or Update Index API](/rest/api/searchservice/indexes/create-or-update) creates the vector store. Follow these steps to index vectors in Azure AI Search:
+The [Create or Update Index](/rest/api/searchservice/indexes/create-or-update) REST API creates the vector index. To index vectors in Azure AI Search, follow these steps:
 
 > [!div class="checklist"]
-> + Start with a basic schema definition
-> + Add vector algorithms and optional compression
-> + Add vector field definitions
-> + Load prevectorized data [as a separate step](#load-vector-data-for-indexing), or use [integrated vectorization](vector-search-integrated-vectorization.md) for data chunking and embedding during indexing
+> + Start with a basic schema definition.
+> + Add vector algorithms and optional compression.
+> + Add vector field definitions.
+> + Load prevectorized data as a [separate step](#load-vector-data-for-indexing) or use [integrated vectorization](vector-search-integrated-vectorization.md) for data chunking and embedding during indexing.
 
-This article explains the workflow using the REST API for illustration. Once you understand the basic workflow, continue with the Azure SDK code samples in the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) repository for guidance on using vectors in test and production code.
+This article uses REST for illustration. After you understand the basic workflow, continue with the Azure SDK code samples in the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) repo, which provides guidance on using vectors in test and production code.
 
 > [!TIP]
 > You can also use the Azure portal to [create a vector index](search-get-started-portal-import-vectors.md) and try out integrated data chunking and vectorization.
 
 ## Prerequisites
 
-+ Azure AI Search, in any region and on any tier. If you plan to use [integrated vectorization](vector-search-integrated-vectorization.md) with Azure AI skills and vectorizers, Azure AI Search must be in the same region as the embedding models hosted on Azure AI Vision.
++ An [Azure AI Search service](search-create-service-portal.md) in any region and on any tier. If you plan to use [integrated vectorization](vector-search-integrated-vectorization.md) with Azure AI skills and vectorizers, Azure AI Search must be in the same region as the embedding models hosted on Azure AI Vision.
 
-+ Your source documents must have [vector embeddings](vector-search-how-to-generate-embeddings.md) to upload to the index. Or, you can use [integrated vectorization](vector-search-integrated-vectorization.md) for this step.
++ Your source documents must have [vector embeddings](vector-search-how-to-generate-embeddings.md) to upload to the index. You can also use [integrated vectorization](vector-search-integrated-vectorization.md) for this step.
 
-+ You should know the dimensions limit of the model used to create the embeddings so that you can assign that limit to the vector field. For **text-embedding-ada-002**, dimensions are fixed at 1536. For **text-embedding-3-small** or **text-embedding-3-large**, dimensions range from 1 to 1536 and 3072, respectively. 
++ You should know the dimensions limit of the model that creates the embeddings so that you can assign that limit to the vector field. For **text-embedding-ada-002**, dimensions are fixed at 1536. For **text-embedding-3-small** or **text-embedding-3-large**, dimensions range from 1 to 1536 and from 1 to 3072, respectively.
 
-+ You should also know what similarity metric to use. For embedding models on Azure OpenAI, similarity is computed using [`cosine`](/azure/ai-services/openai/concepts/understand-embeddings#cosine-similarity). 
++ You should know what similarity metric to use. For embedding models on Azure OpenAI, similarity is computed using [`cosine`](/azure/ai-services/openai/concepts/understand-embeddings#cosine-similarity).
 
-+ You should be familiar with [creating an index](search-how-to-create-search-index.md). A schema always includes a field for the document key, fields used for search or filters, and other configurations for behaviors needed during indexing and queries. 
++ You should know how to [create an index](search-how-to-create-search-index.md). A schema always includes a field for the document key, fields for search or filters, and other configurations for behaviors needed during indexing and queries.
 
 ## Limitations
 
-For search services created before January 2019, there's a small subset that can't create a vector index. If this applies to you, create a new service to use vectors.
+Some search services created before January 2019 can't create a vector index. If this applies to you, create a new service to use vectors.
 
 ## Prepare documents for indexing
 
-Before indexing, assemble a document payload that includes fields of vector and nonvector data. The document structure must conform to the fields collection of index schema. 
+Before indexing, assemble a document payload that includes fields of vector and nonvector data. The document structure must conform to the fields collection of index schema.
 
 Make sure your source documents provide the following content:
 
 | Content | Description |
 |---------|-------------|
 | Unique identifier | A field or a metadata property that uniquely identifies each document. All search indexes require a document key. To satisfy document key requirements, a source document must have one field or property uniquely identifies it in the index. If you're indexing blobs, it might be the metadata_storage_path that uniquely identifies each blob. If you're indexing from a database, it might be primary key. This source field must be mapped to an index field of type `Edm.String` and `key=true` in the search index.|
-| Non-vector content | Provide other fields with human-readable content. Human readable content is useful for the query response, and for hybrid query scenarios that include full text search or semantic ranking in the same request. If you're using a chat completion model, most models like ChatGPT expect human-readable text and don't accept raw vectors as input. |
-| Vector content| A vectorized version of your non-vector content. Vectors are used at query time. A vector is an array of single-precision floating point numbers generated by an embedding model. Each vector field contains an array generated by an embedding model, one embedding per field, where the field is a top-level field (not part of a nested or complex type). For the simplest integration, we recommend the embedding models in [Azure OpenAI](https://aka.ms/oai/access), such as a **text-embedding-3** model for text documents or the [Image Retrieval REST API](/rest/api/computervision/image-retrieval) for images and multimodal embeddings. <br><br>If you can take a dependency on indexers and skillsets, consider using [integrated vectorization](vector-search-integrated-vectorization.md) that encodes images and textual content during indexing. Your field definitions are for vector fields, but incoming source data can be text or images, which are converted to vector arrays during indexing. |
+| Non-vector content | Provide other fields with human-readable content. Human-readable content is useful for the query response and for [hybrid queries](hybrid-search-overview.md) that include full-text search or semantic ranking in the same request. If you're using a chat completion model, most models like ChatGPT expect human-readable text and don't accept raw vectors as input. |
+| Vector content | A vectorized representation of your nonvector content for use at query time. A vector is an array of single-precision floating point numbers generated by an embedding model. Each vector field contains a model-generated array. There's one embedding per field, where the field is a top-level field (not part of a nested or complex type). For simple integration, we recommend embedding models in [Azure OpenAI](https://aka.ms/oai/access), such as **text-embedding-3** for text documents or the [Image Retrieval REST API](/rest/api/computervision/image-retrieval) for images and multimodal embeddings.<br><br>If you can use indexers and skillsets, consider [integrated vectorization](vector-search-integrated-vectorization.md), which encodes images and text during indexing. Your field definitions are for vector fields, but incoming source data can be text or images, which are converted to vector arrays during indexing. |
 
 Your search index should include fields and content for all of the query scenarios you want to support. Suppose you want to search or filter over product names, versions, metadata, or addresses. In this case, vector similarity search isn't especially helpful. Keyword search, geo-search, or filters that iterate over verbatim content would be a better choice. A search index that's inclusive of both vector and nonvector fields provides maximum flexibility for query construction and response composition.
 
-A short example of a documents payload that includes vector and nonvector fields is in the [load vector data](#load-vector-data-for-indexing) section of this article.
+For a short example of a documents payload that includes vector and nonvector fields, see the [load vector data](#load-vector-data-for-indexing) section of this article.
 
 ## Start with a basic index
 
-Start with a minimum schema so that you have a definition to work with before adding a vector configuration and vector fields. A simple index might look the following example. You can learn more about an index schema in [Create a search index](search-how-to-create-search-index.md).
+Start with a minimum schema so that you have a definition to work with before adding a vector configuration and vector fields. A simple index might look the following example. For more information about an index schema, see [Create a search index](search-how-to-create-search-index.md).
 
-Notice that it has a required name, a required document key (`"key": true`), and fields for human readable content in plain text. It's common to have a human-readable version of whatever content you intend to vectorize. For example, if you have a chunk of text from a PDF file, your index schema should have a field for plain text chunks and a second field for vectorized chunks.
+Notice that the index has a required name, a required document key (`"key": true`), and fields for human-readable content in plain text. It's common to have a human-readable version of whatever content you intend to vectorize. For example, if you have a chunk of text from a PDF file, your index schema should have a field for plain-text chunks and a second field for vectorized chunks.
 
-Here's a basic index with a "name", a "fields" collection, and a few other constructs for extra configuration.
+Here's a basic index with a `"name"`, a `"fields"` collection, and some other constructs for extra configuration:
 
 ```http
 POST https://[servicename].search.windows.net/indexes?api-version=[api-version] 
@@ -87,32 +87,32 @@ POST https://[servicename].search.windows.net/indexes?api-version=[api-version]
 
 ## Add a vector search configuration
 
-Next, add a "vectorSearch" configuration to your schema. It's useful to specify a configuration first, before field definitions, because the profiles you define here become part of the vector field's definition. In the schema, vector configuration is typically inserted after the fields collection, perhaps after `"analyzers"`, `"scoringProfiles"`, and `"suggesters"` (although order doesn't matter).
+Next, add a `"vectorSearch"` configuration to your schema. It's useful to specify a configuration before field definitions, because the profiles you define here become part of the vector field's definition. In the schema, vector configuration is typically inserted after the fields collection, perhaps after `"analyzers"`, `"scoringProfiles"`, and `"suggesters"`. However, order doesn't matter.
 
 A vector configuration includes:
 
 + `vectorSearch.algorithms` used during indexing to create "nearest neighbor" information among the vector nodes.
-+ `vectorSearch.compressions` for scalar or binary quantization, oversampling, and for reranking with original vectors.
++ `vectorSearch.compressions` for scalar or binary quantization, oversampling, and reranking with original vectors.
 + `vectorSearch.profiles` for specifying multiple combinations of algorithm and compression configurations.
 
 ### [**2024-07-01**](#tab/config-2024-07-01)
 
-[**2024-07-01**](/rest/api/searchservice/search-service-api-versions#2024-07-01) is generally available. It supports a vector configuration having:
+[**2024-07-01**](/rest/api/searchservice/search-service-api-versions#2024-07-01) is generally available. It supports a vector configuration that has:
 
-+ Hierarchical Navigable Small World (HNSW) algorithm
-+ Exhaustive k-Nearest Neighbor (KNN) algorithm
-+ Scalar compression
-+ Binary compression (available in 2024-07-01 only and in newer Azure SDK packages)
-+ Oversampling
-+ Reranking with original vectors
++ Hierarchical navigable small world (HNSW) algorithm.
++ Exhaustive k-nearest neighbor (KNN) algorithm.
++ Scalar compression.
++ Binary compression, which is available in 2024-07-01 only and in newer Azure SDK packages.
++ Oversampling.
++ Reranking with original vectors.
 
-If you choose HNSW on a field, you can opt in for exhaustive KNN at query time. But the other direction doesn’t work: if you choose exhaustive for indexing, you can’t later request HNSW search because the extra data structures that enable approximate search don’t exist.
+If you choose HNSW on a field, you can opt for exhaustive KNN at query time. However, the opposite doesn’t work. If you choose exhaustive for indexing, you can’t later request HNSW search because the extra data structures that enable approximate search don’t exist.
 
 Be sure to have a strategy for [vectorizing your content](vector-search-how-to-generate-embeddings.md). We recommend [integrated vectorization](vector-search-integrated-vectorization.md) and [query-time vectorizers](vector-search-how-to-configure-vectorizer.md) for built-in encoding.
 
-1. Use the [Create or Update Index](/rest/api/searchservice/indexes/create-or-update) API to create the index.
+1. Use the [Create or Update Index](/rest/api/searchservice/indexes/create-or-update) REST API to create the index.
 
-1. Add a `vectorSearch` section in the index that specifies the search algorithms used to create the embedding space. 
+1. Add a `vectorSearch` section in the index that specifies the search algorithms used to create the embedding space.
 
    ```json
     "vectorSearch": {
@@ -181,27 +181,27 @@ Be sure to have a strategy for [vectorizing your content](vector-search-how-to-g
 
    + `vectorSearch.compressions.rerankWithOriginalVectors` uses the original, uncompressed vectors to recalculate similarity and rerank the top results returned by the initial search query. The uncompressed vectors exist in the search index even if `stored` is false. This property is optional. Default is true.
 
-   + `vectorSearch.compressions.defaultOversampling` considers a broader set of potential results to offset the reduction in information from quantization. The formula for potential results consists of the `k` in the query, with an oversampling multiplier. For example, if the query specifies a `k` of 5, and oversampling is 20, then the query effectively requests 100 documents for use in reranking, using the original uncompressed vector for that purpose. Only the top `k` reranked results are returned. This property is optional. Default is 4.
+   + `vectorSearch.compressions.defaultOversampling` considers a broader set of potential results to offset the reduction in information from quantization. The formula for potential results consists of the `k` in the query, with an oversampling multiplier. For example, if the query specifies a `k` of 5, and oversampling is 20, the query effectively requests 100 documents for use in reranking, using the original uncompressed vector for that purpose. Only the top `k` reranked results are returned. This property is optional. Default is 4.
 
    + `vectorSearch.compressions.scalarQuantizationParameters.quantizedDataType` must be set to `int8`. This is the only primitive data type supported at this time. This property is optional. Default is `int8`.
 
-   + `vectorSearch.algorithms` are either `"hnsw"` or `"exhaustiveKnn"`. These are the Approximate Nearest Neighbors (ANN) algorithms used to organize vector content during indexing.
+   + `vectorSearch.algorithms` is either `hnsw` or `exhaustiveKnn`. These are the approximate nearest neighbors (ANN) algorithms used to organize vector content during indexing.
 
    + `vectorSearch.algorithms.m` is the bi-directional link count. Default is 4. The range is 4 to 10. Lower values should return less noise in the results.
- 
+
    + `vectorSearch.algorithms.efConstruction` is the number of nearest neighbors used during indexing. Default is 400. The range is 100 to 1,000.
 
    + `"vectorSearch.algorithms.efSearch` is the number of nearest neighbors used during search. Default is 500. The range is 100 to 1,000.
 
-   + `vectorSearch.algorithms.metric` should be "cosine" if you're using Azure OpenAI, otherwise use the similarity metric associated with the embedding model you're using. Supported values are `cosine`, `dotProduct`, `euclidean`, `hamming` (used for [indexing binary data](vector-search-how-to-index-binary-data.md)).
+   + `vectorSearch.algorithms.metric` should be `cosine` if you're using Azure OpenAI, otherwise use the similarity metric associated with the embedding model you're using. Supported values are `cosine`, `dotProduct`, `euclidean`, and `hamming` (used for [indexing binary data](vector-search-how-to-index-binary-data.md)).
 
-   + `vectorSearch.profiles` add a layer of abstraction for accommodating richer definitions. A profile is defined in `vectorSearch`, and then referenced by name on each vector field. It's a combination of compression and algorithm configurations. This is the property that you assign to a vector field, and it determines the fields' algorithm and compression.
+   + `vectorSearch.profiles` add a layer of abstraction for accommodating richer definitions. A profile is defined in `vectorSearch` and referenced by name in each vector field. It's a combination of compression and algorithm configurations. You assign this property to a vector field, and it determines the fields' algorithm and compression.
 
 ### [**2024-05-01-preview**](#tab/config-2024-05-01-Preview)
 
 [**2024-05-01-preview**](/rest/api/searchservice/search-service-api-versions#2024-05-01-preview) is the most recent preview version. It's inclusive of previous preview versions.
 
-Preview and stable API versions support the same `"vectorSearch"` configurations. You would choose the preview over the stable version for other reasons, such as [more compression options](vector-search-how-to-quantization.md) or [newer vectorizers](vector-search-how-to-configure-vectorizer.md) invoked at query time.
+Preview and stable API versions support the same `vectorSearch` configurations. You would choose the preview over the stable version for other reasons, such as [more compression options](vector-search-how-to-quantization.md) or [newer vectorizers](vector-search-how-to-configure-vectorizer.md) invoked at query time.
 
 1. Use the [Create or Update Index Preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true) to create the index.
 
@@ -265,37 +265,37 @@ Preview and stable API versions support the same `"vectorSearch"` configurations
 
    + `vectorSearch.compressions.rerankWithOriginalVectors` uses the original, uncompressed vectors to recalculate similarity and rerank the top results returned by the initial search query. The uncompressed vectors exist in the search index even if `stored` is false. This property is optional. Default is true.
 
-   + `vectorSearch.compressions.defaultOversampling` considers a broader set of potential results to offset the reduction in information from quantization. The formula for potential results consists of the `k` in the query, with an oversampling multiplier. For example, if the query specifies a `k` of 5, and oversampling is 20, then the query effectively requests 100 documents for use in reranking, using the original uncompressed vector for that purpose. Only the top `k` reranked results are returned. This property is optional. Default is 4.
+   + `vectorSearch.compressions.defaultOversampling` considers a broader set of potential results to offset the reduction in information from quantization. The formula for potential results consists of the `k` in the query, with an oversampling multiplier. For example, if the query specifies a `k` of 5, and oversampling is 20, the query effectively requests 100 documents for use in reranking, using the original uncompressed vector for that purpose. Only the top `k` reranked results are returned. This property is optional. Default is 4.
 
    + `vectorSearch.compressions.scalarQuantizationParameters.quantizedDataType` must be set to `int8`. This is the only primitive data type supported at this time. This property is optional. Default is `int8`.
 
-   + `vectorSearch.algorithms.kind` are either `"hnsw"` or `"exhaustiveKnn"`. These are the Approximate Nearest Neighbors (ANN) algorithms used to organize vector content during indexing.
+   + `vectorSearch.algorithms.kind` is either `hnsw` or `exhaustiveKnn`. These are the approximate nearest neighbors (ANN) algorithms used to organize vector content during indexing.
 
    + `vectorSearch.algorithms.m` is the bi-directional link count. Default is 4. The range is 4 to 10. Lower values should return less noise in the results.
- 
+
    + `vectorSearch.algorithms.efConstruction` is the number of nearest neighbors used during indexing. Default is 400. The range is 100 to 1,000.
 
-   + `"vectorSearch.algorithms.efSearch` is the number of nearest neighbors used during search. Default is 500. The range is 100 to 1,000.
+   + `vectorSearch.algorithms.efSearch` is the number of nearest neighbors used during search. Default is 500. The range is 100 to 1,000.
 
-   + `vectorSearch.algorithms.metric` should be "cosine" if you're using Azure OpenAI, otherwise use the similarity metric associated with the embedding model you're using. Supported values are `cosine`, `dotProduct`, `euclidean`, `hamming` (used for [indexing binary data](vector-search-how-to-index-binary-data.md)).
+   + `vectorSearch.algorithms.metric` should be `cosine` if you're using Azure OpenAI, otherwise use the similarity metric associated with the embedding model you're using. Supported values are `cosine`, `dotProduct`, `euclidean`, and `hamming` (used for [indexing binary data](vector-search-how-to-index-binary-data.md)).
 
-   + `vectorSearch.profiles` add a layer of abstraction for accommodating richer definitions. A profile is defined in `vectorSearch`, and then referenced by name on each vector field. It's a combination of compression and algorithm configurations. This is the property that you assign to a vector field, and it determines the fields' algorithm and compression.
+   + `vectorSearch.profiles` add a layer of abstraction for accommodating richer definitions. A profile is defined in `vectorSearch` and referenced by name in each vector field. It's a combination of compression and algorithm configurations. You assign this property to a vector field, and it determines the fields' algorithm and compression.
 
 For more information about new preview features, see [What's new in Azure AI Search](whats-new.md).
 
 ---
 
 ## Add a vector field to the fields collection
 
-Once you have a vector configuration, you can add a vector field to the fields collection. Recall that the fields collection must include a field for the document key, vector fields, and any other non-vector fields that you need for hybrid search scenarios or chat model completion in [RAG workloads](retrieval-augmented-generation-overview.md).
+Once you have a vector configuration, you can add a vector field to the fields collection. Recall that the fields collection must include a field for the document key, vector fields, and any other nonvector fields you need for [hybrid search scenarios](hybrid-search-overview.md) or chat model completion in [RAG workloads](retrieval-augmented-generation-overview.md).
 
 Vector fields are characterized by [their data type](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields), a `dimensions` property based on the embedding model used to output the vectors, and a vector profile that you created in a previous step.
 
 ### [**2024-07-01**](#tab/rest-2024-07-01)
 
-[**2024-07-01**](/rest/api/searchservice/search-service-api-versions#2024-07-01) is generally available. 
+[**2024-07-01**](/rest/api/searchservice/search-service-api-versions#2024-07-01) is generally available.
 
-1. Use the [Create or Update Index](/rest/api/searchservice/indexes/create-or-update) to create the index and add a vector field to the fields collection.
+1. Use the [Create or Update Index](/rest/api/searchservice/indexes/create-or-update) REST API to create the index and add a vector field to the fields collection.
 
     ```json
     {
@@ -316,19 +316,19 @@ Vector fields are characterized by [their data type](/rest/api/searchservice/sup
 
 1. Specify a vector field with the following attributes. You can store one generated embedding per field. For each vector field:
 
-   + `type` must be a [vector data types](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields). `Collection(Edm.Single)` is the most common for embedding models.
+   + `type` must be a [vector data type](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields). `Collection(Edm.Single)` is the most common for embedding models.
    + `dimensions` is the number of dimensions generated by the embedding model. For text-embedding-ada-002, it's fixed at 1536. For the text-embedding-3 model series, there's a range of values. If you're using integrated vectorization and an embedding skill to generate vectors, make sure this property is set to the [same dimensions value](cognitive-search-skill-azure-openai-embedding.md#supported-dimensions-by-modelname) used by the embedding skill.
    + `vectorSearchProfile` is the name of a profile defined elsewhere in the index.
    + `searchable` must be true.
    + `retrievable` can be true or false. True returns the raw vectors (1,536 of them) as plain text and consumes storage space. Set to true if you're passing a vector result to a downstream app.
    + `stored` can be true or false. It determines whether an extra copy of vectors is stored for retrieval. For more information, see [Reduce vector size](vector-search-how-to-storage-options.md).
-   + `filterable`, `facetable`, `sortable` must be false. 
+   + `filterable`, `facetable`, and `sortable` must be false.
 
-1. Add filterable nonvector fields to the collection, such as "title" with `filterable` set to true, if you want to invoke [prefiltering or postfiltering](vector-search-filters.md) on the [vector query](vector-search-how-to-query.md).
+1. Add filterable nonvector fields to the collection, such as `title` with `filterable` set to true, if you want to invoke [prefiltering or postfiltering](vector-search-filters.md) on the [vector query](vector-search-how-to-query.md).
 
-1. Add other fields that define the substance and structure of the textual content you're indexing. At a minimum, you need a document key. 
+1. Add other fields that define the substance and structure of the textual content you're indexing. At a minimum, you need a document key.
 
-   You should also add fields that are useful in the query or in its response. The following example shows vector fields for title and content ("titleVector", "contentVector") that are equivalent to vectors. It also provides fields for equivalent textual content ("title", "content") useful for sorting, filtering, and reading in a search result.
+   You should also add fields that are useful in the query or in its response. The following example shows vector fields for title and content (`titleVector` and `contentVector`) that are equivalent to vectors. It also provides fields for equivalent textual content (`title` and `content`) that are useful for sorting, filtering, and reading in a search result.
 
    The following example shows the fields collection:
 
@@ -426,21 +426,21 @@ Vector fields are characterized by [their data type](/rest/api/searchservice/sup
 
 1. Specify a vector field with the following attributes. You can store one generated embedding per document field. For each vector field:
 
-   + `type` can be `Collection(Edm.Single)`, `Collection(Edm.Half)`, `Collection(Edm.Int16)`, `Collection(Edm.SByte)`
+   + `type` can be `Collection(Edm.Single)`, `Collection(Edm.Half)`, `Collection(Edm.Int16)`, or `Collection(Edm.SByte)`.
    + `dimensions` is the number of dimensions generated by the embedding model. For text-embedding-ada-002, it's 1536.
    + `vectorSearchProfile` is the name of a profile defined elsewhere in the index.
    + `searchable` must be true.
    + `retrievable` can be true or false. True returns the raw vectors (1,536 of them) as plain text and consumes storage space. Set to true if you're passing a vector result to a downstream app. False is required if `stored` is false.
-   + `stored` is a new boolean property that applies to vector fields only. True stores a copy of vectors returned in search results. False discards that copy during indexing. You can search on vectors, but can't return vectors in results.
-   + `filterable`, `facetable`, `sortable` must be false. 
+   + `stored` is a new boolean property that applies to vector fields only. True stores a copy of vectors returned in search results. False discards that copy during indexing. You can search on vectors, but you can't return vectors in results.
+   + `filterable`, `facetable`, and `sortable` must be false.
 
 1. Add filterable nonvector fields to the collection, such as "title" with `filterable` set to true, if you want to invoke [prefiltering or postfiltering](vector-search-filters.md) on the [vector query](vector-search-how-to-query.md).
 
-1. Add other fields that define the substance and structure of the textual content you're indexing. At a minimum, you need a document key. 
+1. Add other fields that define the substance and structure of the textual content you're indexing. At a minimum, you need a document key.
 
-   You should also add fields that are useful in the query or in its response. The following example shows vector fields for title and content ("titleVector", "contentVector") that are equivalent to vectors. It also provides fields for equivalent textual content ("title", "content") useful for sorting, filtering, and reading in a search result.
+   You should also add fields that are useful in the query or in its response. The following example shows vector fields for title and content (`titleVector` and `contentVector`) that are equivalent to vectors. It also provides fields for equivalent textual content (`title` and `content`) that are useful for sorting, filtering, and reading in a search result.
 
-1. The following example shows the fields collection:
+   The following example shows the fields collection:
 
     ```http
     PUT https://my-search-service.search.windows.net/indexes/my-index?api-version=2024-05-01-preview&allowIndexDowntime=true
@@ -521,7 +521,7 @@ Vector fields are characterized by [their data type](/rest/api/searchservice/sup
 
 Content that you provide for indexing must conform to the index schema and include a unique string value for the document key. Prevectorized data is loaded into one or more vector fields, which can coexist with other fields containing nonvector content.
 
-You can use either [push or pull methodologies](search-what-is-data-import.md) for data ingestion. 
+For data ingestion, you can use [push or pull methodologies](search-what-is-data-import.md).
 
 ### [**Push APIs**](#tab/push)
 
@@ -572,38 +572,38 @@ POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/d
 
 ### [**Pull APIs (indexers)**](#tab/pull)
 
-Pull APIs refer to indexers, which automate multiple indexing steps, from data retrieval and refresh, to [integrated vectorization](vector-search-integrated-vectorization.md) that encodes content for vector search.
+Pull APIs refer to indexers that automate multiple indexing steps, from data retrieval and refresh to [integrated vectorization](vector-search-integrated-vectorization.md), which encodes content for vector search.
 
 + Data sources must be a [supported type](search-indexer-overview.md#supported-data-sources).
 
-+ Skillsets provide the Text Split skill for data chunking, plus skills that connect to embedding models. A few are generally available, others are still in preview. Skills and vectorizers are used to generate embeddings. The skill you choose for indexing should be paired with an [equivalent vectorizer](vector-search-integrated-vectorization.md#using-integrated-vectorization-in-queries) for queries. For vectorization during indexing, choose from the following skills:
++ Skillsets provide the [Text Split skill](cognitive-search-skill-textsplit.md) for data chunking, plus skills that connect to embedding models. Some skills are generally available, while others are still in preview. Skills and vectorizers are used to generate embeddings. The skill you choose for indexing should be paired with an [equivalent vectorizer](vector-search-integrated-vectorization.md#using-integrated-vectorization-in-queries) for queries. For vectorization during indexing, choose from the following skills:
 
   + [AzureOpenAIEmbedding skill](cognitive-search-skill-azure-openai-embedding.md)
   + [Custom Web API skill](cognitive-search-custom-skill-web-api.md)
   + [Azure AI Vision multimodal embeddings skill (preview)](cognitive-search-skill-vision-vectorize.md)
-  + [AML skill (preview)](cognitive-search-aml-skill.md) to generate embeddings for models hosted in the Azure AI Foundry model catalog. See [How to implement integrated vectorization using models from Azure AI Foundry](vector-search-integrated-vectorization-ai-studio.md) for details.
+  + [AML skill (preview)](cognitive-search-aml-skill.md) to generate embeddings for models hosted in the Azure AI Foundry model catalog. For more information, see [Use embedding models from Azure AI Foundry model catalog for integrated vectorization](vector-search-integrated-vectorization-ai-studio.md).
 
-+ Indexes provide the vector field definitions and vector search configurations. Those definitions are described in this article.
++ Indexes provide the vector field definitions and vector search configurations. This article describes those definitions.
 
 + Indexers drive the indexing pipeline. For more information, see [Create an indexer](search-howto-create-indexers.md).
 
 If you're familiar with indexers and skillsets:
 
 + Field mappings, output field mappings, and deletion detection settings apply to vector and nonvector fields equally.
 
-+ If vector data is sourced in files, we recommend a nondefault `parsingMode` such as `json`, `jsonLines`, or `csv` based on the shape of the data. 
++ If vector data is sourced in files, we recommend a nondefault `parsingMode`, such as `json`, `jsonLines`, or `csv` based on the shape of the data.
 
-+ For data sources, [Azure blob indexers](search-howto-indexing-azure-blob-storage.md) and [Azure Cosmos DB for NoSQL indexers](search-howto-index-cosmosdb.md) with one of the aforementioned parsingModes have been tested and confirmed to work. 
++ For data sources, [Azure blob indexers](search-howto-indexing-azure-blob-storage.md) and [Azure Cosmos DB for NoSQL indexers](search-howto-index-cosmosdb.md) with one of the aforementioned parsingModes have been tested and confirmed to work.
 
 + The dimensions of all vectors from the data source must be the same and match their index definition for the field they're mapping to. The indexer throws an error on any documents that don’t match.
 
 ---
 
 ## Query your index for vector content
 
-For validation purposes, you can query the index using Search Explorer in the Azure portal or a REST API call. Because Azure AI Search can't convert a vector to human-readable text, try to return fields from the same document that provide evidence of the match. For example, if the vector query targets the "titleVector" field, you could select "title" for the search results.
+For validation purposes, you can query the index using Search Explorer in the Azure portal or a REST API call. Because Azure AI Search can't convert a vector to human-readable text, try to return fields from the same document that provide evidence of the match. For example, if the vector query targets the `titleVector` field, you could select `title` for the search results.
 
-Fields must be attributed as "retrievable" to be included in the results.
+Fields must be attributed as `retrievable` to be included in the results.
 
 ### [**Azure portal**](#tab/portal-check-index)
 
@@ -613,15 +613,15 @@ Fields must be attributed as "retrievable" to be included in the results.
 
   + Set **Query options** > **Hide vector values in search results** for more readable results.
 
-  + [Use the JSON view for vector queries](vector-search-how-to-query.md). You can either paste in a JSON definition of the vector query you want to execute, or use the built-in text-to-vector or image-to-vector conversion if your index has a [vectorizer assignment](vector-search-how-to-configure-vectorizer.md). For more information about image search, see [Quickstart: Search for images in Search Explorer](search-get-started-portal-image-search.md).
+  + [Use the JSON view for vector queries](vector-search-how-to-query.md). You can paste a JSON definition of the vector query you want to execute. If your index has a [vectorizer assignment](vector-search-how-to-configure-vectorizer.md), you can also use the built-in text-to-vector or image-to-vector conversion. For more information about image search, see [Quickstart: Search for images in Search Explorer](search-get-started-portal-image-search.md).
 
-  + Use the default Query view for a quick confirmation that the index contains vectors. The query view is for full text search. Although you can't use it for vector queries, you can send an empty search (`search=*`) to check for content. The content of all fields, including vector fields, is returned as plain text.
+  + Use the default Query view for a quick confirmation that the index contains vectors. The query view is for full-text search. Although you can't use it for vector queries, you can send an empty search (`search=*`) to check for content. The content of all fields, including vector fields, is returned as plain text.
 
 For more information, see [Create a vector query](vector-search-how-to-query.md).
 
 ### [**REST API**](#tab/rest-check-index)
 
-The following REST API example is a vector query, but it returns only nonvector fields (title, content, category). Only fields marked as "retrievable" can be returned in search results.
+The following REST API example is a vector query, but it returns only nonvector fields (`title`, `content`, and `category`). Only fields marked as `retrievable` can be returned in search results.
 
 ```http
 POST https://my-search-service.search.windows.net/indexes/my-index/docs/search?api-version=2024-07-01
@@ -645,25 +645,25 @@ api-key: {{admin-api-key}}
 
 ---
 
-## Update a vector store
+## Update a vector index
 
-To update a vector store, modify the schema and reload documents to populate new fields. APIs for schema updates include [Create or Update Index (REST)](/rest/api/searchservice/indexes/create-or-update), [CreateOrUpdateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createorupdateindexasync) in the Azure SDK for .NET, [create_or_update_index](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient?view=azure-python#azure-search-documents-indexes-searchindexclient-create-or-update-index&preserve-view=true) in the Azure SDK for Python, and similar methods in other Azure SDKs.
+To update a vector index, modify the schema and reload documents to populate new fields. APIs for schema updates include [Create or Update Index (REST)](/rest/api/searchservice/indexes/create-or-update), [CreateOrUpdateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createorupdateindexasync) in the Azure SDK for .NET, [create_or_update_index](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient?view=azure-python#azure-search-documents-indexes-searchindexclient-create-or-update-index&preserve-view=true) in the Azure SDK for Python, and similar methods in other Azure SDKs.
 
-The standard guidance for updating an index is covered in [Update or rebuild an index](search-howto-reindex.md). 
+For standard guidance on updating an index, see [Update or rebuild an index](search-howto-reindex.md).
 
 Key points include:
 
 + Drop and full index rebuild is often required for updates to and deletion of existing fields.
 
-+ A few modifications can be made with no rebuild requirement:
++ You can make the following modifications with no rebuild requirement:
 
   + Add new fields to a fields collection.
   + Add new vector configurations, assigned to new fields but not existing fields that are already vectorized.
-  + Change "retrievable" (values are true or false) on an existing field. Vector fields must be searchable and retrievable, but if you want to disable access to a vector field in situations where drop and rebuild isn't feasible, you can set retrievable to false.
+  + Change `retrievable` (values are true or false) on an existing field. Vector fields must be searchable and retrievable, but if you want to disable access to a vector field in situations where drop and rebuild isn't feasible, you can set retrievable to false.
 
 ## Next steps
 
-As a next step, we recommend [Query vector data in a search index](vector-search-how-to-query.md).
+As a next step, we recommend [Create a vector query](vector-search-how-to-query.md).
 
 Code samples in the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) repository demonstrate end-to-end workflows that include schema definition, vectorization, indexing, and queries.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルインデックス作成に関するドキュメントの更新"
}
```

### Explanation
この変更では、Azure AI Searchにおけるベクトルインデックスの作成に関するドキュメントが更新され、様々な情報が整理され、明確化されました。主な更新内容としては、日付の修正、文言の改善、そして使い方のガイドラインの具体化が挙げられます。

具体的には、ドキュメントの構成と流れがより分かりやすくなり、REST APIの使用方法に関する手順が明確に示されています。さらに、シェーマ定義、ベクトルアルゴリズム、および圧縮の追加を含む、インデックス作成に必要なステップが詳細に説明されています。

また、ドキュメント全体を通して、ベクトルフィールドの定義、配置、および設定方法についての指示が更新されており、ユーザーがインデックスをより効率的に作成できるように配慮されています。特に、ベクトル化の戦略を把握することが強調され、統合ベクトル化についての情報も提供されています。

このように、更新された内容は、使用者がAzure AI Searchにおけるベクトルインデックスの作成と活用を行いやすくすることを目指しています。全体として、ユーザーエクスペリエンスが向上したことがこの変更の特徴です。

## articles/search/vector-search-how-to-query.md{#item-9bb93c}

<details>
<summary>Diff</summary>
````diff
@@ -9,41 +9,41 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 04/30/2025
+ms.date: 06/19/2025
 ---
 
 # Create a vector query in Azure AI Search
 
 In Azure AI Search, if you have a [vector index](vector-search-how-to-create-index.md), this article explains how to:
 
 > [!div class="checklist"]
-> + [Query vector fields](#vector-query-request)
-> + [Query multiple vector fields at once](#multiple-vector-fields)
-> + [Set vector weights](#vector-weighting)
-> + [Query with integrated vectorization](#query-with-integrated-vectorization)
-> + [Set thresholds to exclude low-scoring results (preview)](#set-thresholds-to-exclude-low-scoring-results-preview)
+> + [Query vector fields](#vector-query-request).
+> + [Query multiple vector fields at once](#multiple-vector-fields).
+> + [Set vector weights](#vector-weighting).
+> + [Query with integrated vectorization](#query-with-integrated-vectorization).
+> + [Set thresholds to exclude low-scoring results (preview)](#set-thresholds-to-exclude-low-scoring-results-preview).
 
-This article uses REST for illustration. For code samples in other languages, see the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) GitHub repository for end-to-end solutions that include vector queries. 
+This article uses REST for illustration. After you understand the basic workflow, continue with the Azure SDK code samples in the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) repo, which provides end-to-end solutions that include vector queries.
 
 You can also use [Search Explorer](search-explorer.md) in the Azure portal.
 
 ## Prerequisites
 
-+ Azure AI Search, in any region and on any tier.
++ An [Azure AI Search service](search-create-service-portal.md) in any region and on any tier.
 
-+ [A vector index on Azure AI Search](vector-search-how-to-create-index.md). Check for a `vectorSearch` section in your index to confirm a vector index.
++ A [vector index](vector-search-how-to-create-index.md). Check for a `vectorSearch` section in your index to confirm its presence.
 
 + Optionally, [add a vectorizer](vector-search-how-to-configure-vectorizer.md) to your index for built-in text-to-vector or image-to-vector conversion during queries.
 
-+ Visual Studio Code with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) and sample data if you want to run these examples on your own. To get started with the REST client, see [Quickstart: Azure AI Search using REST](search-get-started-rest.md).
++ Visual Studio Code with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) and sample data if you want to run these examples on your own. To get started with the REST client, see [Quickstart: Keyword search using REST](search-get-started-rest.md).
 
 ## Convert a query string input into a vector
 
-To query a vector field, the query itself must be a vector. 
+To query a vector field, the query itself must be a vector.
 
-One approach for converting a user's text query string into its vector representation is to call an embedding library or API in your application code. As a best practice, *always use the same embedding models used to generate embeddings in the source documents*. You can find code samples showing [how to generate embeddings](vector-search-how-to-generate-embeddings.md) in the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) repository.
+One approach for converting a user's text query string into its vector representation is to call an embedding library or API in your application code. As a best practice, *always use the same embedding models used to generate embeddings in the source documents*. You can find code samples showing [how to generate embeddings](vector-search-how-to-generate-embeddings.md) in the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) repo.
 
-A second approach is [using integrated vectorization](#query-with-integrated-vectorization), now generally available, to have Azure AI Search handle your query vectorization inputs and outputs.
+A second approach is to [use integrated vectorization](#query-with-integrated-vectorization), now generally available, to have Azure AI Search handle your query vectorization inputs and outputs.
 
 Here's a REST API example of a query string submitted to a deployment of an Azure OpenAI embedding model:
 
@@ -56,11 +56,11 @@ api-key: {{admin-api-key}}
 }
 ```
 
-The expected response is 202 for a successful call to the deployed model. 
+The expected response is 202 for a successful call to the deployed model.
 
-The "embedding" field in the body of the response is the vector representation of the  query string "input". For testing purposes, you would copy the value of the "embedding" array into "vectorQueries.vector" in a query request, using syntax shown in the next several sections. 
+The `embedding` field in the body of the response is the vector representation of the query string `input`. For testing purposes, you would copy the value of the `embedding` array into `vectorQueries.vector` in a query request, using the syntax shown in the next several sections.
 
-The actual response for this POST call to the deployed model includes 1536 embeddings, trimmed here to just the first few vectors for readability.
+The actual response to this POST call to the deployed model includes 1,536 embeddings. For readability, this example only shows the first few vectors.
 
 ```json
 {
@@ -89,22 +89,23 @@ In this approach, your application code is responsible for connecting to a model
 
 ## Vector query request
 
-This section shows you the basic structure of a vector query. You can use the Azure portal, REST APIs, or the Azure SDKs to formulate a vector query. If you're migrating from [**2023-07-01-Preview**](/rest/api/searchservice/index-preview), there are breaking changes. See [Upgrade to the latest REST API](search-api-migration.md) for details.
+This section shows you the basic structure of a vector query. You can use the Azure portal, REST APIs, or the Azure SDKs to formulate a vector query.
+
+If you're migrating from [**2023-07-01-Preview**](/rest/api/searchservice/index-preview), there are breaking changes. For more information, see [Upgrade to the latest REST API](search-api-migration.md).
 
 ### [**2024-07-01**](#tab/query-2024-07-01)
 
-[**2024-07-01**](/rest/api/searchservice/search-service-api-versions#2024-07-01) is the stable REST API version for [Search POST](/rest/api/searchservice/documents/search-post). This version supports:
+[**2024-07-01**](/rest/api/searchservice/search-service-api-versions#2024-07-01) is the stable REST API version of [Search POST](/rest/api/searchservice/documents/search-post). This version supports:
 
 + `vectorQueries` is the construct for vector search.
-+ `vectorQueries.kind` set to `vector` for a vector array, or set to `text` if the input is a string and [you have a vectorizer](#query-with-integrated-vectorization).
-+ `vectorQueries.vector` is query (a vector representation of text or an image).
++ `vectorQueries.kind` set to `vector` for a vector array or `text` if the input is a string and if you [have a vectorizer](#query-with-integrated-vectorization).
++ `vectorQueries.vector` is the query (a vector representation of text or an image).
 + `vectorQueries.exhaustive` (optional) invokes exhaustive KNN at query time, even if the field is indexed for HNSW.
 + `vectorQueries.fields` (optional) targets specific fields for query execution (up to 10 per query).
-+ `vectorQueries.weight` (optional) specifies the relative weight of each vector query included in search operations (see [Vector weighting](#vector-weighting)).
++ `vectorQueries.weight` (optional) specifies the relative weight of each vector query included in search operations. For more information, see [Vector weighting](#vector-weighting).
 + `vectorQueries.k` is the number of matches to return.
 
-
-In the following example, the vector is a representation of this string: "what Azure services support full text search". The query targets the `contentVector` field. The query returns `k` results. The actual vector has 1536 embeddings, so it's trimmed in this example for readability.
+In the following example, the vector is a representation of this string: `"what Azure services support full text search"`. The query targets the `contentVector` field and returns `k` results. The actual vector has 1,536 embeddings, which are trimmed in this example for readability.
 
 ```http
 POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-07-01
@@ -134,14 +135,14 @@ api-key: {{admin-api-key}}
 
 ### [**2024-05-01-preview**](#tab/query-2024-05-01-preview)
 
-[**2024-05-01-preview**](/rest/api/searchservice/search-service-api-versions#2024-05-01-preview) is the latest preview API version for [Search - POST](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&tabs=HTTP&preserve-view=true). It supports the same vector query syntax as **2024-07-01**, with extra parameters for hybrid search and minimum thresholds for excluding weaker results. 
+[**2024-05-01-preview**](/rest/api/searchservice/search-service-api-versions#2024-05-01-preview) is the latest preview API version of [Search - POST](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&tabs=HTTP&preserve-view=true). It supports the same vector query syntax as **2024-07-01**, but it has extra parameters for hybrid search and minimum thresholds for excluding weaker results.
 
 This preview adds:
 
-+ [`threshold`](#set-thresholds-to-exclude-low-scoring-results-preview) for excluding low scoring results.
++ [`threshold`](#set-thresholds-to-exclude-low-scoring-results-preview) for excluding low-scoring results.
 + [`Hybridsearch.MaxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) for more control over the inputs to a [hybrid query](hybrid-search-how-to-query.md).
 
-In the following example, the vector is a representation of this string: "what Azure services support full text search". The query targets the `contentVector` field. The query returns `k` results. The actual vector has 1536 embeddings, so it's trimmed in this example for readability.
+In the following example, the vector is a representation of this string: `"what Azure services support full text search"`. The query targets the `contentVector` field and returns `k` results. The actual vector has 1,536 embeddings, which are trimmed in this example for readability.
 
 ```http
 POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-05-01-preview
@@ -179,21 +180,21 @@ api-key: {{admin-api-key}}
 
 ### [**Azure portal**](#tab/portal-vector-query)
 
-Use Search Explorer to formulate a vector query. Search Explorer has a **Query view** and **JSON View**. If you have a vectorizer, you can use **Query view** (see [Query with integrated vectorization](#query-with-integrated-vectorization) for steps.)
+Use Search Explorer to formulate a vector query. Search Explorer has **Query view** and **JSON View**. If you have a vectorizer, you can use the query view, which is described in the [Query with integrated vectorization](#query-with-integrated-vectorization) section of this article.
 
-Otherwise, if you don't have a vectorizer, you must use **JSON view** and formulate the vector query in JSON, pasting in a vector array as the query input.
+Otherwise, if you don't have a vectorizer, you must use the JSON view and formulate the vector query in JSON by pasting a vector array as the query input.
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
 
-1. Under **Search management** and **Indexes**, select the index.
+1. From the left menu, select **Search management** > **Indexes**, and then select your index.
 
    :::image type="content" source="media/vector-search-how-to-query/select-index.png" alt-text="Screenshot of the indexes menu." border="true":::
 
-1. On Search Explorer, under **View**, select **JSON view**.
+1. On the **Search explorer** tab, select **View** > **JSON view**.
 
    :::image type="content" source="media/vector-search-how-to-query/select-json-view.png" alt-text="Screenshot of the index list." border="true":::
 
-1. By default, the search API is **2024-05-01-preview**. You can choose another API version.
+1. Choose your desired API version.
 
 1. Paste in a JSON vector query, and then select **Search**.
 
@@ -205,9 +206,9 @@ Otherwise, if you don't have a vectorizer, you must use **JSON view** and formul
 
 In Azure AI Search, query responses consist of all `retrievable` fields by default. However, it's common to limit search results to a subset of `retrievable` fields by listing them in a `select` statement.
 
-In a vector query, carefully consider whether you need to vector fields in a response. Vector fields aren't human readable, so if you're pushing a response to a web page, you should choose nonvector fields that are representative of the result. For example, if the query executes against `contentVector`, you could return `content` instead.
+In a vector query, carefully consider whether you need to vector fields in a response. Vector fields aren't human readable, so if you're pushing a response to a web page, you should choose nonvector fields that represent the result. For example, if the query executes against `contentVector`, you could return `content` instead.
 
-If you do want vector fields in the result, here's an example of the response structure. `contentVector` is a string array of embeddings, trimmed here for brevity. The search score indicates relevance. Other nonvector fields are included for context.
+If you want vector fields in the result, here's an example of the response structure. `contentVector` is a string array of embeddings, which are trimmed in this example for readability. The search score indicates relevance. Other nonvector fields are included for context.
 
 ```json
 {
@@ -252,17 +253,17 @@ If you do want vector fields in the result, here's an example of the response st
 
 **Key points:**
 
-+ `k` determines how many nearest neighbor results are returned, in this case, three. Vector queries always return `k` results, assuming at least `k` documents exist, even if there are documents with poor similarity, because the algorithm finds any `k` nearest neighbors to the query vector. 
++ `k` determines how many nearest neighbor results are returned, in this case, three. Vector queries always return `k` results, assuming at least `k` documents exist, even if some documents have poor similarity. This is because the algorithm finds any `k` nearest neighbors to the query vector.
 
-+ The **`@search.score`** is determined by the [vector search algorithm](vector-search-ranking.md). 
++ The [vector search algorithm](vector-search-ranking.md) determines the `@search.score`.
 
-+ Fields in search results are either all `retrievable` fields, or fields in a `select` clause. During vector query execution, the match is made on vector data alone. However, a response can include any `retrievable` field in an index. Because there's no facility for decoding a vector field result, the inclusion of nonvector text fields is helpful for their human readable values.
++ Fields in search results are either all `retrievable` fields or fields in a `select` clause. During vector query execution, matching is made on vector data alone. However, a response can include any `retrievable` field in an index. Because there's no facility for decoding a vector field result, the inclusion of nonvector text fields is helpful for their human-readable values.
 
 ## Multiple vector fields
 
-You can set the "vectorQueries.fields" property to multiple vector fields. The vector query executes against each vector field that you provide in the `fields` list. You can specify up to 10 fields.
+You can set the `vectorQueries.fields` property to multiple vector fields. The vector query executes against each vector field that you provide in the `fields` list. You can specify up to 10 fields.
 
-When querying multiple vector fields, make sure each one contains embeddings from the same embedding model, and that the query is also generated from the same embedding model.
+When querying multiple vector fields, ensure that each one contains embeddings from the same embedding model. The query should also be generated from the same embedding model.
 
 ```http
 POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-07-01
@@ -291,9 +292,9 @@ api-key: {{admin-api-key}}
 
 ## Multiple vector queries
 
-Multi-query vector search sends multiple queries across multiple vector fields in your search index. A common example of this query request is when using models such as [CLIP](https://openai.com/research/clip) for a multimodal vector search where the same model can vectorize image and text content.
+Multi-query vector search sends multiple queries across multiple vector fields in your search index. This type of query is commonly used with models such as [CLIP](https://openai.com/research/clip) for multimodal search, where the same model can vectorize both text and images.
 
-The following query example looks for similarity in both `myImageVector` and `myTextVector`, but sends in two different query embeddings respectively, each executing in parallel. This query produces a result that's scored using [Reciprocal Rank Fusion (RRF)](hybrid-search-ranking.md).
+The following query example looks for similarity in both `myImageVector` and `myTextVector` but sends two respective query embeddings, each executing in parallel. The result of this query is scored using [reciprocal rank fusion](hybrid-search-ranking.md) (RRF).
 
 + `vectorQueries` provides an array of vector queries.
 + `vector` contains the image vectors and text vectors in the search index. Each instance is a separate query.
@@ -332,42 +333,42 @@ The following query example looks for similarity in both `myImageVector` and `my
 }
 ```
 
-Search results would include a combination of text and images, assuming your search index includes a field for the image file (a search index doesn't store images).
+Search indexes can't store images. Assuming that your index includes a field for the image file, the search results would include a combination of text and images.
 
 ## Query with integrated vectorization
 
-This section shows a vector query that invokes the [integrated vectorization](vector-search-integrated-vectorization.md) that converts a text or [image query](search-get-started-portal-image-search.md) into a vector. We recommend the stable [**2024-07-01**](/rest/api/searchservice/documents/search-post) REST API, Search Explorer, or newer Azure SDK packages for this feature.
+This section shows a vector query that invokes the [integrated vectorization](vector-search-integrated-vectorization.md) to convert a text or [image query](search-get-started-portal-image-search.md) into a vector. We recommend the stable [**2024-07-01**](/rest/api/searchservice/documents/search-post) REST API, Search Explorer, or newer Azure SDK packages for this feature.
 
-A prerequisite is a search index having a [vectorizer configured and assigned](vector-search-how-to-configure-vectorizer.md) to a vector field. The vectorizer provides connection information to an embedding model used at query time. 
+A prerequisite is a search index that has a [vectorizer configured and assigned](vector-search-how-to-configure-vectorizer.md) to a vector field. The vectorizer provides connection information to an embedding model used at query time.
 
 ### [**Azure portal**](#tab/builtin-portal)
 
 Search Explorer supports integrated vectorization at query time. If your index contains vector fields and has a vectorizer, you can use the built-in text-to-vector conversion.
 
-1. Sign in to the [Azure portal](https://portal.azure.com/) with your Azure account, and go to your Azure AI Search service.
+1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
 
-1. From the left menu, expand **Search management** > **Indexes**, and select your index. Search Explorer is the first tab on the index page.
+1. From the left menu, select **Search management** > **Indexes**, and then select your index.
 
-1. Check **Vector profiles** to confirm you have a vectorizer.
+1. Select the **Vector profiles** tab to confirm that you have a vectorizer.
 
    :::image type="content" source="media/vector-search-how-to-query/check-vectorizer.png" alt-text="Screenshot of a vectorizer setting in a search index.":::
 
-1. In Search Explorer, you can enter a text string into the default search bar in query view. The built-in vectorizer converts your string into a vector, performs the search, and returns results.
+1. Select the **Search explorer** tab. Using the default query view, you can enter a text string into the search bar. The built-in vectorizer converts your string into a vector, performs the search, and returns results.
 
-   Alternatively, you can select **View** > **JSON view** to view or modify the query. If vectors are present, Search Explorer sets up a vector query automatically. You can use JSON view to select fields used in search and in the response, add filters, or construct more advanced queries like hybrid. A JSON example is provided in the REST API tab of this section.
+   Alternatively, you can select **View** > **JSON view** to view or modify the query. If vectors are present, Search Explorer sets up a vector query automatically. You can use the JSON view to select fields for use in the searche and response, add filters, and construct more advanced queries, such as [hybrid queries](hybrid-search-how-to-query.md). To see a JSON example, select the REST API tab in this section.
 
 ### [**REST API**](#tab/builtin-2024-07-01)
 
 1. Use [Index - GET](/rest/api/searchservice/indexes/get) to return the index definition and check for the presence of a vectorizer configuration. Look for `vectorizers` in your index definition. It should specify a deployed embedding model.
 
 1. Use [Search - POST](/rest/api/searchservice/documents/search-post) for the query request.
 
-    + `kind` must be set to `text` .
+    + `kind` must be set to `text`.
     + `text` must have a text string. It's passed to the vectorizer assigned to the vector field.
     + `fields` is the vector field to search.
     + `k` is the number of vector matches to return.
 
-Here's a simple example of a query that's vectorized at query time. The text string is vectorized and then used to query the descriptionVector field.
+Here's a simple example of a query that's vectorized at query time. The text string is vectorized and then used to query the `descriptionVector` field.
 
 ```http
 POST https://{{search-service}}.search.windows.net/indexes/{{index}}/docs/search?api-version=2024-07-01
@@ -384,9 +385,9 @@ POST https://{{search-service}}.search.windows.net/indexes/{{index}}/docs/search
 }
 ```
 
-Here's a [hybrid query](hybrid-search-how-to-query.md) using integrated vectorization of text queries. This query includes multiple query vector fields, multiple nonvector fields, a filter, and semantic ranking. Again, the differences are the `kind` of vector query and the `text` string instead of a `vector`.
+Here's a [hybrid query](hybrid-search-how-to-query.md) that uses integrated vectorization for text queries. This query includes multiple query vector fields, multiple nonvector fields, a filter, and semantic ranking. Again, the differences are the `kind` of vector query and the `text` string instead of a `vector`.
 
-In this example, the search engine makes three vectorization calls to the vectorizers assigned to `descriptionVector`, `synopsisVector`, and `authorBioVector` in the index. The resulting vectors are used to retrieve documents against their respective fields. The search engine also executes a keyword search on the `search` query, "mystery novel set in London". 
+In this example, the search engine makes three vectorization calls to the vectorizers assigned to `descriptionVector`, `synopsisVector`, and `authorBioVector` in the index. The resulting vectors are used to retrieve documents against their respective fields. The search engine also executes a keyword search on the `search` query, which is `"mystery novel set in London"`.
 
 ```http
 POST https://{{search-service}}.search.windows.net/indexes/{{index}}/docs/search?api-version=2024-07-01
@@ -417,9 +418,9 @@ api-key: {{admin-api-key}}
 }
 ```
 
-Whenever you use semantic ranking with vectors, make sure `k` is set to 50. Semantic ranker uses up to 50 matches as input. Specifying less than 50 deprives the semantic ranking models of necessary inputs.
+Whenever you use semantic ranking with vectors, set `k` to 50. Semantic ranker uses up to 50 matches as input. Specifying less than 50 deprives the semantic ranking models of necessary inputs.
 
-The scored results from all four queries are fused using [RRF ranking](hybrid-search-ranking.md). Secondary [semantic ranking](semantic-search-overview.md) is invoked over the fused search results, but on the `searchFields` only, boosting results that are the most semantically aligned to `"search":"mystery novel set in London"`.
+The scored results from all four queries are fused using [RRF ranking](hybrid-search-ranking.md). Secondary [semantic ranking](semantic-search-overview.md) is invoked over the fused search results on the `searchFields` only, boosting results that are the most semantically aligned to `"search":"mystery novel set in London"`.
 
 > [!NOTE]
 > Vectorization occurs during indexing and querying. If you don't need data chunking and vectorization in the index, you can skip steps like creating an indexer, skillset, and data source. In this workflow, vectorization is used only at query time to convert a text string or an image into an embedding. You can define a vectorizer in the search index for this step.
@@ -428,47 +429,47 @@ The scored results from all four queries are fused using [RRF ranking](hybrid-se
 
 ## Number of ranked results in a vector query response
 
-A vector query specifies the `k` parameter, which determines how many matches are returned in the results. The search engine always returns `k` number of matches. If `k` is larger than the number of documents in the index, then the number of documents determines the upper limit of what can be returned.
+A vector query specifies the `k` parameter, which determines how many matches are returned in the results. The search engine always returns `k` number of matches. If `k` is larger than the number of documents in the index, the number of documents determines the upper limit of what can be returned.
 
-If you're familiar with full text search, you know to expect zero results if the index doesn't contain a term or phrase. However, in vector search, the search operation is identifying nearest neighbors, and it will always return `k` results even if the nearest neighbors aren't that similar. So, it's possible to get results for nonsensical or off-topic queries, especially if you aren't using prompts to set boundaries. Less relevant results have a worse similarity score, but they're still the "nearest" vectors if there isn't anything closer. As such, a response with no meaningful results can still return `k` results, but each result's similarity score would be low. 
+If you're familiar with full-text search, you know to expect zero results if the index doesn't contain a term or phrase. However, in vector search, the search operation identifies nearest neighbors and always return `k` results, even if the nearest neighbors aren't that similar. It's possible to get results for nonsensical or off-topic queries, especially if you aren't using prompts to set boundaries. Less relevant results have a worse similarity score, but they're still the "nearest" vectors if there isn't anything closer. Therefore, a response with no meaningful results can still return `k` results, but each result's similarity score would be low.
 
-A [hybrid approach](hybrid-search-overview.md) that includes full text search can mitigate this problem. Another mitigation is to set a minimum threshold on the search score, but only if the query is a pure single vector query. Hybrid queries aren't conducive to minimum thresholds because the RRF ranges are so much smaller and volatile.
+A [hybrid approach](hybrid-search-overview.md) that includes full-text search can mitigate this problem. Another solution is to set a minimum threshold on the search score, but only if the query is a pure single vector query. Hybrid queries aren't conducive to minimum thresholds because the RRF ranges are much smaller and more volatile.
 
-Query parameters affecting result count include:
+Query parameters that affect result count include:
 
-+ `"k": n` results for vector-only queries
-+ `"top": n` results for hybrid queries that include a "search" parameter
++ `"k": n` results for vector-only queries.
++ `"top": n` results for hybrid queries that include a `search` parameter.
 
-Both "k" and "top" are optional. Unspecified, the default number of results in a response is 50. You can set "top" and "skip" to [page through more results](search-pagination-page-layout.md#paging-results) or change the default.
+Both `k` and `top` are optional. When unspecified, the default number of results in a response is 50. You can set `top` and `skip` to [page through more results](search-pagination-page-layout.md#paging-results) or change the default.
 
 ## Ranking algorithms used in a vector query
 
-Ranking of results is computed by either:
+The ranking of results is computed by either:
 
-+ Similarity metric
-+ Reciprocal Rank Fusion (RRF) if there are multiple sets of search results.
++ The similarity metric.
++ RRF if there are multiple sets of search results.
 
 ### Similarity metric
 
 The similarity metric specified in the index `vectorSearch` section for a vector-only query. Valid values are `cosine`, `euclidean`, and `dotProduct`.
 
 Azure OpenAI embedding models use cosine similarity, so if you're using Azure OpenAI embedding models, `cosine` is the recommended metric. Other supported ranking metrics include `euclidean` and `dotProduct`.
 
-### Using RRF
+### RRF
 
-Multiple sets are created if the query targets multiple vector fields, runs multiple vector queries in parallel, or if the query is a hybrid of vector and full text search, with or without [semantic ranking](semantic-search-overview.md). 
+Multiple sets are created if the query targets multiple vector fields, runs multiple vector queries in parallel, or is a hybrid of vector and full-text search, with or without [semantic ranking](semantic-search-overview.md).
 
-During query execution, a vector query can only target one internal vector index. So for [multiple vector fields](#multiple-vector-fields) and [multiple vector queries](#multiple-vector-queries), the search engine generates multiple queries that target the respective vector indexes of each field. Output is a set of ranked results for each query, which are fused using RRF. For more information, see [Relevance scoring using Reciprocal Rank Fusion (RRF)](hybrid-search-ranking.md).
+During query execution, a vector query can only target one internal vector index. For [multiple vector fields](#multiple-vector-fields) and [multiple vector queries](#multiple-vector-queries), the search engine generates multiple queries that target the respective vector indexes of each field. The output is a set of ranked results for each query, which are fused using RRF. For more information, see [Relevance scoring using Reciprocal Rank Fusion](hybrid-search-ranking.md).
 
 ## Vector weighting
 
 Add a `weight` query parameter to specify the relative weight of each vector query included in search operations. This value is used when combining the results of multiple ranking lists produced by two or more vector queries in the same request, or from the vector portion of a hybrid query.
 
-The default is 1.0 and the value must be a positive number larger than zero.
+The default is 1.0, and the value must be a positive number larger than zero.
 
-Weights are used when calculating the [reciprocal rank fusion](hybrid-search-ranking.md#weighted-scores) scores of each document. The calculation is multiplier of the `weight` value against the rank score of the document within its respective result set.
+Weights are used when calculating the [RRF scores](hybrid-search-ranking.md#weighted-scores) of each document. The calculation is a multiplier of the `weight` value against the rank score of the document within its respective result set.
 
-The following example is a hybrid query with two vector query strings and one text string. Weights are assigned to the vector queries. The first query is 0.5 or half the weight, reducing its importance in the request. The second vector query is twice as important. 
+The following example is a hybrid query with two vector query strings and one text string. Weights are assigned to the vector queries. The first query is 0.5 or half the weight, reducing its importance in the request. The second vector query is twice as important.
 
 ```http
 POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?api-version=2024-07-01
@@ -494,13 +495,13 @@ POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?
     } 
 ```
 
-Vector weighting applies to vectors only. The text query in this example ("hello world") has an implicit weight of 1.0 or neutral weight. However, in a hybrid query, you can increase or decrease the importance of text fields by setting [maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode).
+Vector weighting applies to vectors only. The text query in this example, `"hello world"`, has an implicit neutral weight of 1.0. However, in a hybrid query, you can increase or decrease the importance of text fields by setting [maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode).
 
 ## Set thresholds to exclude low-scoring results (preview)
 
-Because nearest neighbor search always returns the requested `k` neighbors, it's possible to get multiple low scoring matches as part of meeting the `k` number requirement on search results. To exclude low-scoring search result, you can add a `threshold` query parameter that filters out results based on a minimum score. Filtering occurs before [fusing results](hybrid-search-ranking.md) from different recall sets. 
+Because nearest neighbor search always returns the requested `k` neighbors, it's possible to get multiple low-scoring matches as part of meeting the `k` number requirement on search results. To exclude low-scoring search results, you can add a `threshold` query parameter that filters out results based on a minimum score. Filtering occurs before [fusing results](hybrid-search-ranking.md) from different recall sets.
 
-This parameter is still in preview. We recommend preview REST API version [2024-05-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true).
+This parameter is in preview. We recommend the  [2024-05-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true) REST API version.
 
 In this example, all matches that score below 0.8 are excluded from vector search results, even if the number of results falls below `k`.
 
@@ -529,9 +530,9 @@ POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?
 
 Vector queries are often used in hybrid constructs that include nonvector fields. If you discover that BM25-ranked results are over or under represented in a hybrid query results, you can [set `maxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) to increase or decrease the BM25-ranked results provided for hybrid ranking.
 
-You can only set this property in hybrid requests that include both "search" and "vectorQueries" components.
+You can only set this property in hybrid requests that include both `search` and `vectorQueries` components.
 
-This parameter is still in preview. We recommend preview REST API version [2024-05-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true).
+This parameter is in preview. We recommend the  [2024-05-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true) REST API version.
 
 For more information, see [Set maxTextRecallSize - Create a hybrid query](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索クエリに関するドキュメントの更新"
}
```

### Explanation
この変更では、Azure AI Searchにおけるベクトル検索クエリに関するドキュメントが更新され、情報が整理され、分かりやすさを向上させるための若干の修正が施されています。主な更新内容として、日付の変更、データ構造の明確化、文言の軽微な修正があり、全体の可読性が向上しています。

具体的には、ベクトルクエリの構造に関する記述が改良され、ユーザーがAzureポータルやREST API、Azure SDKを用いてクエリを形成する際の指示が明確になっています。また、プレビュー機能として「低スコアの結果を除外するための閾値」設定に関するセクションが追加され、この機能の使用方法に関する具体的な準備が整いました。

そのほか、クエリを行うための「ベクトル化」の手法や、クエリ応答に含まれるフィールドの選択肢に関する注意点も記載されています。このように、更新されたドキュメントは、ユーザーがベクトル検索をより効果的かつ効率的に利用できるよう設計されています。

全体として、この変更はAzure AI Searchにおけるベクトル検索に関する理解を深め、実装を容易にすることを目的としています。

## articles/search/vector-search-overview.md{#item-56e5fa}

<details>
<summary>Diff</summary>
````diff
@@ -9,86 +9,86 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 05/08/2025
+ms.date: 06/20/2025
 ---
 
-# Vectors in Azure AI Search
+# Vector search in Azure AI Search
 
-Vector search is an approach in information retrieval that supports indexing and query execution over numeric representations of content. Because the content is numeric rather than plain text, matching is based on vectors that are most similar to the query vector, which enables matching across:
+Vector search is an information retrieval approach that supports indexing and querying over numeric representations of content. Because the content is numeric rather than plain text, matching is based on vectors that are most similar to the query vector, which enables matching across:
 
-+ semantic or conceptual likeness ("dog" and "canine", conceptually similar yet linguistically distinct)
-+ multilingual content ("dog" in English and "hund" in German)
-+ multiple content types ("dog" in plain text and a photograph of a dog in an image file)
++ Semantic or conceptual likeness. For example, "dog" and "canine" are conceptually similar but linguistically distinct.
++ Multilingual content, such as "dog" in English and "hund" in German.
++ Multiple content types, such as "dog" in plain text and an image of a dog.
 
-This article provides [a high-level introduction to vector support](#vector-search-concepts) in Azure AI Search. It also explains integration with other Azure services and covers [terminology and concepts](#vector-search-concepts) related to vector search development.
+This article covers vector support in Azure AI Search, including its integration with other Azure services. It also introduces concepts and terminology related to vector search development.
 
-We recommend this article for background, but if you'd rather get started, follow these steps:
-
-> [!div class="checklist"]
-> + [Provide embeddings](vector-search-how-to-generate-embeddings.md) for your index or [generate embeddings](vector-search-integrated-vectorization.md) in an indexer pipeline
-> + [Create a vector index](vector-search-how-to-create-index.md)
-> + [Run vector queries](vector-search-how-to-query.md)
-
-You could also begin with the [vector quickstart](search-get-started-vector.md) or the [code samples on GitHub](https://github.com/Azure/azure-search-vector-samples). 
+> [!TIP]
+> Want to get started right away? Follow these steps:
+>
+> 1. [Provide embeddings](vector-search-how-to-generate-embeddings.md) for your index or [generate embeddings](vector-search-integrated-vectorization.md) in an indexer pipeline.
+> 1. [Create a vector index](vector-search-how-to-create-index.md).
+> 1. [Run vector queries](vector-search-how-to-query.md).
 
 ## What scenarios can vector search support?
 
-Scenarios for vector search include:
+Vector search supports the following scenarios:
 
-+ **Similarity search**. Encode text using embedding models such as OpenAI embeddings or open source models such as SBERT, and retrieve documents with queries that are also encoded as vectors.
++ **Similarity search**. Encode text using embedding models or open-source models, such as OpenAI embeddings or SBERT, respectively. You then retrieve documents using queries that are also encoded as vectors.
 
-+ **Search across different content types (multimodal)**. Encode images and text using multimodal embeddings (for example, with [OpenAI CLIP](https://github.com/openai/CLIP) or [GPT-4 Turbo with Vision](/azure/ai-services/openai/whats-new#gpt-4-turbo-with-vision-now-available) in Azure OpenAI) and query an embedding space composed of vectors from both content types.
++ **[Hybrid search](hybrid-search-overview.md)**. Azure AI Search defines hybrid search as the execution of vector search and [keyword search](search-lucene-query-architecture.md) in the same request. Vector support is implemented at the field level. If an index contains vector and nonvector fields, you can write a query that targets both. The queries execute in parallel, and the results are merged into a single response and ranked accordingly.
 
-+ [**Hybrid search**](hybrid-search-overview.md). In Azure AI Search, we define hybrid search as dual vector and keyword query execution in the same request. Vector support is implemented at the field level. If an index contains both vector and non-vector fields, you can write a query that targets both. The queries execute in parallel and the results are merged into a single response and ranked accordingly.
++ **[Multimodal search](multimodal-search-overview.md)**. Encode text and images using multimodal embeddings, such as [OpenAI CLIP](https://github.com/openai/CLIP) or [GPT-4 Turbo with Vision](/azure/ai-services/openai/whats-new#gpt-4-turbo-with-vision-now-available) in Azure OpenAI, and then query an embedding space composed of vectors from both content types.
 
-+ **Multilingual search**. Azure AI Search is designed for extensibility. If you have embedding models and chat models trained in multiple languages, you can call them through custom or built-in skills on the indexing side, or vectorizers on the query side. If you need more control over text translation, you can supplement with the [multi-language capabilities](search-language-support.md) that Azure AI Search supports for nonvector content, in hybrid search scenarios.
++ **Multilingual search**. Azure AI Search is designed for extensibility. If you have embedding models and chat models trained in multiple languages, you can call them through custom or built-in skills on the indexing side or vectorizers on the query side. For more control over text translation, use the [multi-language capabilities](search-language-support.md) supported by Azure AI Search for nonvector content in hybrid search scenarios.
 
-+ **Filtered vector search**. A query request can include a vector query and a [filter expression](search-filters.md). Filters apply to text and numeric fields, and are useful for metadata filters, and including or excluding search results based on filter criteria. Although a vector field isn't filterable itself, you can set up a filterable text or numeric field. The search engine can process the filter before or after the vector query executes.
++ **Filtered vector search**. A query request can include a vector query and a [filter expression](search-filters.md). Filters apply to text and numeric fields. They're useful for metadata filters and for including or excluding search results based on filter criteria. Although a vector field isn't filterable, you can set up a filterable text or numeric field. The search engine can process the filter before or after executing the vector query.
 
-+ **Vector database**. Azure AI Search stores the data that you query over. Use it as a [pure vector store](vector-store.md) any time you need long-term memory or a knowledge base, or grounding data for [Retrieval Augmented Generation (RAG) architecture](https://aka.ms/what-is-rag), or any app that uses vectors.
++ **Vector database**. Azure AI Search stores the data that you query over. Use it as a [pure vector index](vector-store.md) when you need long-term memory or a knowledge base, grounding data for the [retrieval-augmented generation (RAG)](retrieval-augmented-generation-overview.md) architecture, or an app that uses vectors.
 
 ## How vector search works in Azure AI Search
 
-Vector support includes indexing, storing, and querying of vector embeddings from a search index.
-
-The following diagram shows the indexing and query workflows for vector search.
+Azure AI Search supports indexing, storing, and querying vector embeddings from a search index. The following diagram shows the indexing and query workflows for vector search.
 
 :::image type="content" source="media/vector-search-overview/vector-search-architecture-diagram-3.svg" alt-text="Architecture of vector search workflow." border="false" lightbox="media/vector-search-overview/vector-search-architecture-diagram-3-high-res.png":::
 
-On the indexing side, Azure AI Search takes vector embeddings and uses a [nearest neighbors algorithm](vector-search-ranking.md) to place similar vectors close together in an index. Internally, it creates vector indexes for each vector field.
+On the indexing side, Azure AI Search uses a [nearest neighbors algorithm](vector-search-ranking.md) to place similar vectors close together in an index. Internally, it creates [vector indexes](vector-store.md) for each vector field.
 
-How you get embeddings from your source content into Azure AI Search depends on whether you want to perform the work within an Azure AI Search indexing pipeline, or externally.  Azure AI Search offers [integrated data chunking and vectorization](vector-search-integrated-vectorization.md) in an indexer pipeline. You still provide the resources (endpoints and connection information to Azure OpenAI), but Azure AI Search makes all of the calls and handles the transitions. This approach requires an indexer, a supported data source, and a skillset that drives chunking and embedding. If you don't want to use indexers, you can handle all vectorization externally, and then push prevectorized content into [vector fields](vector-search-how-to-create-index.md) in the search index.
+How you get embeddings from your source content into Azure AI Search depends on your processing approach:
 
-On the query side, in your client application, you collect the query input from a user, usually through a prompt workflow. You can then add an encoding step that converts the input into a vector, and then send the vector query to your index on Azure AI Search for a similarity search. As with indexing, you can deploy the [integrated vectorization](vector-search-integrated-vectorization.md) to convert the question into a vector. For either approach, Azure AI Search returns documents with the requested `k` nearest neighbors (kNN) in the results.
++ For internal processing, Azure AI Search offers [integrated data chunking and vectorization](vector-search-integrated-vectorization.md) in an indexer pipeline. You provide the necessary resources, such as endpoints and connection information for Azure OpenAI. Azure AI Search then makes the calls and handles the transitions. This approach requires an indexer, a supported data source, and a skillset that drives chunking and embedding.
 
-Azure AI Search supports [hybrid scenarios](hybrid-search-overview.md) that run vector and keyword search in parallel, returning a unified result set that often provides better results than just vector or keyword search alone. For hybrid, vector and non-vector content is ingested into the same index, for queries that run side by side.
++ For external processing, you can [generate embeddings](vector-search-how-to-generate-embeddings.md) outside of Azure AI Search and push the prevectorized content directly into [vector fields](vector-search-how-to-create-index.md) in your search index.
 
-## Availability and pricing
+On the query side, your client app collects user input, typically through a prompt. You can add an encoding step to vectorize the input and then send the vector query to your Azure AI Search index for similarity search. As with indexing, you can use [integrated vectorization](vector-search-integrated-vectorization.md) to encode the query. For either approach, Azure AI Search returns documents with the requested `k` nearest neighbors (kNN) in the results.
+
+Azure AI Search supports [hybrid scenarios](hybrid-search-overview.md) that run vector and keyword search in parallel and return a unified result set, which often provides better results than vector or keyword search alone. For hybrid search, both vector and nonvector content are ingested into the same index for queries that run simultaneously.
 
-Vector search is available as part of all Azure AI Search tiers in all regions at no extra charge.
+## Availability and pricing
 
-Newer services created after April 3, 2024 support [higher quotas for vector indexes](vector-search-index-size.md). If you have an older service, you might be able to [upgrade your service](search-how-to-upgrade.md) for higher vector quotas.
+Vector search is available in [all regions](search-region-support.md) and on [all tiers](search-sku-tier.md) at no extra charge.
 
-Vector search is available in:
+For portal and programmatic access to vector search, you can use:
 
-+ [Azure portal: Import and vectorize data wizard](search-get-started-portal-import-vectors.md)
-+ [Azure REST APIs](/rest/api/searchservice/operation-groups)
-+ [Azure SDKs for .NET](https://www.nuget.org/packages/Azure.Search.Documents), [Python](https://pypi.org/project/azure-search-documents), and [JavaScript](https://www.npmjs.com/package/@azure/search-documents)
-+ Other Azure offerings such as Azure AI Foundry.
++ The [Import and vectorize data wizard](search-get-started-portal-import-vectors.md) in the Azure portal.
++ The [Search Service REST APIs](/rest/api/searchservice).
++ The Azure SDKs for [.NET](https://www.nuget.org/packages/Azure.Search.Documents), [Python](https://pypi.org/project/azure-search-documents), and [JavaScript](https://www.npmjs.com/package/@azure/search-documents).
++ [Other Azure offerings](#azure-integration-and-related-services), such as Azure AI Foundry.
 
 > [!NOTE]
-> Some older search services created before January 1, 2019 are deployed on infrastructure that doesn't support vector workloads. If you try to add a vector field to a schema and get an error, it's a result of outdated services. In this situation, you must create a new search service to try out the vector feature.
+> + Some search services created before January 1, 2019 don't support vector workloads. If you try to add a vector field to a schema and get an error, it's a result of outdated services. In this situation, you must create a new search service to try out the vector feature.
+>
+> + Search services created after April 3, 2024 offer [higher quotas for vector indexes](vector-search-index-size.md). If you have an older service, you might be able to [upgrade your service](search-how-to-upgrade.md) for higher vector quotas.
 
 ## Azure integration and related services
 
-Azure AI Search is deeply integrated across the Azure AI platform. The following table lists several that are useful in vector workloads.
+Azure AI Search is deeply integrated across the Azure AI platform. The following table lists products that are useful in vector workloads.
 
 | Product | Integration |
 |---------|-------------|
-| Azure AI Foundry | In the chat with your data playground, **Add your own data** uses Azure AI Search for grounding data and conversational search. This is the easiest and fastest approach for chatting with your data. |
-| Azure OpenAI | Azure OpenAI provides embedding models and chat models. Demos and samples target the [text-embedding-ada-002](/azure/ai-services/openai/concepts/models#embeddings-models). We recommend Azure OpenAI for generating embeddings for text. |
-| Azure AI Services | [Image Retrieval Vectorize Image API(Preview)](/azure/ai-services/computer-vision/how-to/image-retrieval#call-the-vectorize-image-api) supports vectorization of image content. We recommend this API for generating embeddings for images. |
-| Azure data platforms: Azure Blob Storage, Azure Cosmos DB, Azure SQL, OneLake | You can use [indexers](search-indexer-overview.md) to automate data ingestion, and then use [integrated vectorization](vector-search-integrated-vectorization.md) to generate embeddings. Azure AI Search can automatically index vector data from [Azure blob indexers](search-howto-indexing-azure-blob-storage.md), [Azure Cosmos DB for NoSQL indexers](search-howto-index-cosmosdb.md), [Azure Data Lake Storage Gen2](search-howto-index-azure-data-lake-storage.md), [Azure Table Storage](search-howto-indexing-azure-tables.md), [Fabric OneLake](search-how-to-index-onelake-files.md). For more information, see [Add vector fields to a search index.](vector-search-how-to-create-index.md). |
+| Azure AI Foundry | In the chat playground, **Add your own data** uses Azure AI Search for grounding data and conversational search. The playground is the easiest and fastest way to [chat with your data](/azure/ai-services/openai/use-your-data-quickstart). |
+| Azure OpenAI | Azure OpenAI provides embedding models and chat models. Demos and samples target the [text-embedding-ada-002](/azure/ai-services/openai/concepts/models#embeddings-models) model. We recommend Azure OpenAI for generating embeddings for text. |
+| Azure AI Services | [Image Retrieval Vectorize Image API (preview)](/azure/ai-services/computer-vision/how-to/image-retrieval#call-the-vectorize-image-api) supports vectorization of image content. We recommend this API for generating embeddings for images. |
+| Azure data platforms: Azure Blob Storage, Azure Cosmos DB, Azure SQL, OneLake | You can use [indexers](search-indexer-overview.md) to automate data ingestion, and then use [integrated vectorization](vector-search-integrated-vectorization.md) to generate embeddings. Azure AI Search can automatically index vector data from [Azure blob indexers](search-howto-indexing-azure-blob-storage.md), [Azure Cosmos DB for NoSQL indexers](search-howto-index-cosmosdb.md), [Azure Data Lake Storage Gen2](search-howto-index-azure-data-lake-storage.md), [Azure Table Storage](search-howto-indexing-azure-tables.md), and [Fabric OneLake](search-how-to-index-onelake-files.md). For more information, see [Add vector fields to a search index.](vector-search-how-to-create-index.md). |
 
 It's also commonly used in open-source frameworks like [LangChain](https://js.langchain.com/docs/integrations/vectorstores/azure_aisearch).
 
@@ -98,60 +98,71 @@ If you're new to vectors, this section explains some core concepts.
 
 ### About vector search
 
-Vector search is a method of information retrieval where documents and queries are represented as vectors instead of plain text. In vector search, machine learning models generate the vector representations of source inputs, which can be text, images, or other content. Having a mathematic representation of content provides a common language for comparing disparate content. If everything is a vector, a query can find a match in vector space, even if the associated original content is in different media or language than the query.
+Vector search is a method of information retrieval where documents and queries are represented as vectors instead of plain text. In vector search, machine learning models generate the vector representations of source inputs, which can be text, images, or other content.
 
-### Why use vector search
+Having a mathematic representation of content provides a common language for comparing disparate content. If everything is a vector, a query can find a match in vector space, even if the associated original content is in different media or language than the query.
 
-When searchable content is represented as vectors, a query can find close matches in similar content. The embedding model used for vector generation knows which words and concepts are similar, and it places the resulting vectors close together in the embedding space. For example, vectorized source documents about "clouds" and "fog" are more likely to show up in a query about "mist" because they're semantically similar, even if they aren't a lexical match.
+### Why use vector search?
+
+When searchable content is represented as vectors, a query can find close matches in similar content. The embedding model used for vector generation knows which words and concepts are similar and places the resulting vectors close together in the embedding space.
+
+For example, vectorized source documents about "clouds" and "fog" are more likely to show up in a query about "mist" because they're semantically similar, even if they aren't a lexical match.
 
 ### Embeddings and vectorization
 
-*Embeddings* are a specific type of vector representation of content or a query, created by machine learning models that capture the semantic meaning of text or representations of other content such as images. Natural language machine learning models are trained on large amounts of data to identify patterns and relationships between words. During training, they learn to represent any input as a vector of real numbers in an intermediary step called the *encoder*. After training is complete, these language models can be modified so the intermediary vector representation becomes the model's output. The resulting embeddings are high-dimensional vectors, where words with similar meanings are closer together in the vector space, as explained in [Understand embeddings (Azure OpenAI)](/azure/ai-services/openai/concepts/understand-embeddings). 
+Machine learning models create *embeddings*, a specific type of vector representation of content or queries. These models capture the semantic meaning of text or representations of other content, such as images.
+
+Natural-language machine learning models are trained on large amounts of data to identify patterns and relationships between words. During training, the models learn to represent any input as a vector of real numbers in an intermediary step called the *encoder*. After training, the models can be modified so that the intermediary vector representation becomes their output. The resulting embeddings are high-dimensional vectors, where words with similar meanings are closer together in the vector space. For more information about embeddings, see [Understand embeddings in Azure OpenAI in Azure AI Foundry Models](/azure/ai-services/openai/concepts/understand-embeddings).
 
-The effectiveness of vector search in retrieving relevant information depends on the effectiveness of the embedding model in distilling the meaning of documents and queries into the resulting vector. The best models are well-trained on the types of data they're representing. You can evaluate existing models such as Azure OpenAI text-embedding-ada-002, bring your own model that's trained directly on the problem space, or fine-tune a general-purpose model. Azure AI Search doesn't impose constraints on which model you choose, so pick the best one for your data. 
+The effectiveness of vector search in retrieving relevant information depends on how effectively the embedding model distills the meaning of documents and queries into the resulting vector. The best models are well-trained on the types of data they represent. You can evaluate existing models, such as Azure OpenAI text-embedding-ada-002; bring your own model that's trained directly on the problem space; or fine-tune a general-purpose model. Azure AI Search doesn't impose constraints on which model you choose, so pick the best one for your data.
 
-In order to create effective embeddings for vector search, it's important to take input size limitations into account. We recommend following the [guidelines for chunking data](vector-search-how-to-chunk-documents.md) before generating embeddings. This best practice ensures that the embeddings accurately capture the relevant information and enable more efficient vector search.
+To create effective embeddings for vector search, it's important to consider input size limitations. We recommend following the [guidelines for chunking data](vector-search-how-to-chunk-documents.md) before generating embeddings. This best practice ensures that the embeddings accurately capture the relevant information and enable more efficient vector search.
 
-### What is the embedding space?
+### What is an embedding space?
 
-*Embedding space* is the corpus for vector queries. Within a search index, an embedding space is all of the vector fields populated with embeddings from the same embedding model. Machine learning models create the embedding space by mapping individual words, phrases, or documents (for natural language processing), images, or other forms of data into a representation comprised of a vector of real numbers representing a coordinate in a high-dimensional space. In this embedding space, similar items are located close together, and dissimilar items are located farther apart. 
+An *embedding space* is the corpus for vector queries. Within a [search index](search-what-is-an-index.md), the embedding space is all of the vector fields populated with embeddings from the same embedding model. Machine learning models create the embedding space by mapping individual words, phrases, documents (for natural-language processing), images, or other data into representations comprised of vectors of real numbers that act as coordinates in a high-dimensional space.
 
-For example, documents that talk about different species of dogs would be clustered close together in the embedding space. Documents about cats would be close together, but farther from the dogs cluster while still being in the neighborhood for animals. Dissimilar concepts such as cloud computing would be much farther away. In practice, these embedding spaces are abstract and don't have well-defined, human-interpretable meanings, but the core idea stays the same.
+In the embedding space, similar items are located close together, while dissimilar items are located farther apart. For example, documents about different species of dogs would be clustered close together. Documents about cats would be close together but farther from the dogs cluster, while still being in the neighborhood for animals. Dissimilar concepts, such as cloud computing, would be much farther away.
+
+In practice, embedding spaces are abstract and don't have well-defined, human-interpretable meanings, but the core idea stays the same.
 
 <a name="eknn"></a>
 
 ### Nearest neighbors search
 
-In vector search, the search engine scans vectors within the embedding space to identify vectors that are closest to the query vector. This technique is called [*nearest neighbor search*](https://en.wikipedia.org/wiki/Nearest_neighbor_search). Nearest neighbors help quantify the similarity between items. A high degree of vector similarity indicates that the original data was similar too. To facilitate fast nearest neighbor search, the search engine performs optimizations, or employs data structures and data partitioning, to reduce the search space. Each vector search algorithm solves the nearest neighbor problems in different ways as they optimize for minimum latency, maximum throughput, recall, and memory. To compute similarity, similarity metrics provide the mechanism for computing distance.
+In vector search, the search engine scans vectors within the embedding space to identify vectors that are closest to the query vector. This technique is called [*nearest neighbor search*](https://en.wikipedia.org/wiki/Nearest_neighbor_search).
+
+Nearest neighbors quantify the similarity between items. A high degree of vector similarity indicates that the original data is also similar. To expedite nearest neighbor search and reduce the search space, the search engine uses data structures and data partitioning. Each vector search algorithm solves the nearest neighbor problems differently, optimizing for minimum latency, maximum throughput, recall, and memory. To compute similarity, similarity metrics provide the mechanism for computing distance.
 
-Azure AI Search currently supports the following algorithms:
+Azure AI Search supports the following algorithms:
 
-+ Hierarchical Navigable Small World (HNSW): HNSW is a leading ANN algorithm optimized for high-recall, low-latency applications where data distribution is unknown or can change frequently. It organizes high-dimensional data points into a hierarchical graph structure that enables fast and scalable similarity search while allowing a tunable a trade-off between search accuracy and computational cost. Because the algorithm requires all data points to reside in memory for fast random access, this algorithm consumes [vector index size](vector-search-index-size.md) quota.
++ **Hierarchical navigable small world (HNSW)**. HNSW is a leading ANN algorithm optimized for high-recall, low-latency applications with unknown or volatile data distribution. It organizes high-dimensional data points into a hierarchical graph structure that enables fast, scalable similarity search and allows a tunable trade-off between search accuracy and computational cost. Because the algorithm requires all data points to reside in memory for fast random access, HNSW consumes [vector index size](vector-search-index-size.md) quota.
 
-+ Exhaustive K-nearest neighbors (KNN): Calculates the distances between the query vector and all data points. It's computationally intensive, so it works best for smaller datasets. Because the algorithm doesn't require fast random access of data points, this algorithm doesn't consume vector index size quota. However, this algorithm provides the global set of nearest neighbors.
++ **Exhaustive k-nearest neighbors (KNN)**. KNN calculates the distances between the query vector and all data points. It's computationally intensive and works best for smaller datasets. Because the algorithm doesn't require fast random access of data points, KNN doesn't consume vector index size quota. However, it provides the global set of nearest neighbors.
 
-To use these algorithms, see [Create a vector field](vector-search-how-to-create-index.md) for instructions on specifying the algorithm, vector profiles, and profile assignment.
+To learn how to specify the algorithm, vector profile, and profile assignment for HNSW or KNN, see [Create a vector field](vector-search-how-to-create-index.md).
 
-Algorithm parameters that are used to initialize the index during index creation are immutable and can't be changed after the index is built. However, parameters that affect the query-time characteristics (`efSearch`) can be modified. 
+Algorithm parameters that are used to initialize the index during index creation are immutable and can't be changed after the index is built. However, parameters that affect the query-time characteristics (`efSearch`) can be modified.
 
-In addition, fields that specify HNSW algorithm also support exhaustive KNN search using the [query request](vector-search-how-to-query.md) parameter `"exhaustive": true`. The opposite isn't true however. If a field is indexed for `exhaustiveKnn`, you can't use HNSW in the query because the extra data structures that enable efficient search don’t exist.
+Fields that specify the HNSW algorithm also support exhaustive KNN search using the [query request](vector-search-how-to-query.md) parameter `"exhaustive": true`. However, the opposite isn't true. If a field is indexed for `exhaustiveKnn`, you can't use HNSW in the query because the extra data structures that enable efficient search don't exist.
 
-### Approximate Nearest Neighbors
+### Approximate nearest neighbors
 
-Approximate Nearest Neighbor (ANN) search is a class of algorithms for finding matches in vector space. This class of algorithms employs different data structures or data partitioning methods to significantly reduce the search space to accelerate query processing. 
+Approximate nearest neighbor (ANN) is a class of algorithms for finding matches in vector space. This class of algorithms uses different data structures or data partitioning methods to significantly reduce the search space and accelerate query processing.
 
-ANN algorithms sacrifice some accuracy, but offer scalable and faster retrieval of approximate nearest neighbors, which makes them ideal for balancing accuracy against efficiency in modern information retrieval applications. You can adjust the parameters of your algorithm to fine-tune the recall, latency, memory, and disk footprint requirements of your search application.
+ANN algorithms sacrifice some accuracy but offer scalable and faster retrieval of approximate nearest neighbors, which makes them ideal for balancing accuracy and efficiency in modern information retrieval applications. You can adjust the parameters of your algorithm to fine-tune the recall, latency, memory, and disk footprint requirements of your search application.
 
-Azure AI Search uses HNSW for its ANN algorithm. 
+Azure AI Search uses HNSW for its ANN algorithm.
 
 <!-- > [!NOTE]
 > Finding the true set of [nearest neighbors](https://en.wikipedia.org/wiki/Nearest_neighbor_search) requires comparing the input vector exhaustively against all vectors in the dataset. While each vector similarity calculation is relatively fast, performing these exhaustive comparisons across large datasets is computationally expensive and slow due to the sheer number of comparisons. For example, if a dataset contains 10 million 1,000-dimensional vectors, computing the distance between the query vector and all vectors in the dataset would require scanning 37 GB of data (assuming single-precision floating point vectors) and a high number of similarity calculations.
 > 
 > To address this challenge, approximate nearest neighbor (ANN) search methods are used to trade off recall for speed. These methods can efficiently find a small set of candidate vectors that are similar to the query vector and have high likelihood to be in the globally most similar neighbors. Each algorithm has a different approach to reducing the total number of vectors comparisons, but they all share the ability to balance accuracy and efficiency by tweaking the algorithm configuration parameters. -->
 
-## Next steps
+## Related content
 
-+ [Try the quickstart](search-get-started-vector.md)
-+ [Learn more about vector indexing](vector-search-how-to-create-index.md)
-+ [Learn more about vector queries](vector-search-how-to-query.md)
++ [Quickstart: Vector search using REST](search-get-started-vector.md)
++ [Create a vector index](vector-search-how-to-create-index.md)
++ [Create a vector query](vector-search-how-to-query.md)
++ [azure-vector-search-samples](https://github.com/Azure-Samples/azure-vector-search-samples)
 + [Azure Cognitive Search and LangChain: A Seamless Integration for Enhanced Vector Search Capabilities](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-and-langchain-a-seamless-integration-for/ba-p/3901448)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおけるベクトル検索の概要の更新"
}
```

### Explanation
この変更では、Azure AI Searchにおけるベクトル検索の概要に関するドキュメントが更新され、内容がより明確かつ効率的に整理されています。主な更新ポイントには、日付の修正、文言の整理、セクションの構成改善が含まれています。

具体的には、「ベクトル検索」の定義や適用シナリオが整理され、セクション間の論理的な流れが強化されました。例えば、類似性検索、ハイブリッド検索、マルチモーダル検索などの具体的なシナリオについてより詳細に説明されています。また、ベクトルデータベースの利用方法の説明も強化されており、利用者がAzure AI Searchでのベクトル検索の活用方法をより理解しやすくなっています。

さらに、ドキュメントは「機能」「利用ステップ」「Azureとの統合」などの構成に分かれており、ナビゲーションが容易になっています。これにより、ユーザーは必要な情報にすぐにアクセスできるようになっています。

全体として、この変更はAzure AI Searchにおける最良の利用方法を促進し、ユーザーがベクトル検索の機能を効果的に活用できるようにすることを目指しています。

## articles/search/vector-store.md{#item-db9b8c}

<details>
<summary>Diff</summary>
````diff
@@ -9,39 +9,53 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 05/08/2025
+ms.date: 06/20/2025
 ---
 
-# Vector storage in Azure AI Search
+# Vector indexes in Azure AI Search
 
-Azure AI Search provides vector storage and configurations for [vector search](vector-search-overview.md) and [hybrid search](hybrid-search-overview.md). Support is implemented at the field level, which means you can combine vector and nonvector fields in the same search corpus.
+Vectors are high-dimensional embeddings that represent text, images, and other content mathematically. Azure AI Search stores vectors at the field level, allowing vector and nonvector content to coexist within the same [search index](search-what-is-an-index.md).
 
-Vectors are stored in a search index. Use the [Create Index REST API](/rest/api/searchservice/indexes/create) or an equivalent Azure SDK method to [create the vector store](vector-search-how-to-create-index.md).
+A search index becomes a *vector index* when you define vector fields and a vector configuration. To populate vector fields, you can push [precomputed embeddings](vector-search-how-to-generate-embeddings.md) into them or use [integrated vectorization](vector-search-integrated-vectorization.md), a built-in Azure AI Search capability that generates embeddings during indexing.
 
-Considerations for vector storage include the following points:
+At query time, the vector fields in your index enable similarity search, where the system retrieves documents whose vectors are most similar to the vector query. You can use [vector search](vector-search-overview.md) for similarity matching alone or [hybrid search](hybrid-search-overview.md) for a combination of similarity and keyword matching.
 
-+ Design a schema to fit your use case based on the intended vector retrieval pattern.
-+ Estimate index size and check search service capacity.
-+ Manage a vector store
-+ Secure a vector store
+This article covers the key concepts for creating and managing a vector index, including:
+
++ Vector retrieval patterns
++ Content (vector fields and configuration)
++ Physical data structure
++ Basic operations
+
+> [!TIP]
+> Want to get started right away? See [Create a vector index](vector-search-how-to-create-index.md).
 
 ## Vector retrieval patterns
 
-In Azure AI Search, there are two patterns for working with search results. 
+Azure AI Search supports two patterns for vector retrieval:
+
++ **Classic search**. This pattern uses a search bar, query input, and rendered results. During query execution, the search engine or your application code vectorizes the user input. The search engine then performs vector search over the vector fields in your index and formulates a response that you render in a client app.
+
+  In Azure AI Search, results are returned as a flattened row set, and you can choose which fields to include in the response. Although the search engine matches on vectors, your index should have nonvector, human-readable content to populate the search results. Classic search supports both [vector queries](vector-search-how-to-query.md) and [hybrid queries](hybrid-search-how-to-query.md).
+
++ **Generative search**. Language models use data from Azure AI Search to respond to user queries. An orchestration layer typically coordinates prompts and maintains context, feeding search results into chat models like GPT. This pattern is based on the [retrieval-augmented generation (RAG)](retrieval-augmented-generation-overview.md) architecture, where the search index provides grounding data.
 
-+ Generative search. Language models formulate a response to the user's query using grounding data from Azure AI Search. This pattern typically includes an orchestration layer to coordinate prompts and maintain context. In this pattern, search results are fed into prompt flows, received by chat models like GPT. This approach is based on [**Retrieval augmented generation (RAG)**](retrieval-augmented-generation-overview.md) architecture, where the search index provides the grounding data.
+## Schema of a vector index
 
-+ Classic search using a search bar, query input, and rendered results. The search engine formulates the response using verbatim content in the search index, with no extra reasoning or logic. At query time, your application code or the search engine vectorizes the user input into a vector. The search engine performs a vector search over vector fields and formulates a response. You render those results in a client app. In Azure AI Search, results are returned in a flattened row set, and you can choose which fields to include search results. Since there's no chat model, it's expected that you would populate the vector store (search index) with nonvector content that's human readable in your response. Although the search engine matches on vectors, you should use nonvector values to populate the search results. [**Vector queries**](vector-search-how-to-query.md) and [**hybrid queries**](hybrid-search-how-to-query.md) cover the types of query requests you can formulate for classic search scenarios.
+The schema of a vector index requires the following:
 
-Your index schema should reflect your primary use case. The following section highlights the differences in field composition for solutions built for generative AI or classic search.
++ Name
++ Key field (string)
++ One or more vector fields
++ Vector configuration
 
-## Schema of a vector store
+Nonvector fields aren't required, but we recommend including them for hybrid queries or for returning verbatim content that doesn't go through a language model. For more information, see [Create a vector index](vector-search-how-to-create-index.md).
 
-An index schema for a vector store requires a name, a key field (string), one or more vector fields, and a vector configuration. Nonvector fields are recommended for hybrid queries, or for returning verbatim human readable content that doesn't have to go through a language model. For instructions about vector configuration, see [Create a vector store](vector-search-how-to-create-index.md).
+Your index schema should reflect your [vector retrieval pattern](#vector-retrieval-patterns). This section mostly covers field composition for classic search, but it also provides schema guidance for generative search.
 
 ### Basic vector field configuration
 
-Vector fields are distinguished by their data type and vector-specific properties. Here's what a vector field looks like in a fields collection:
+Vector fields have unique data types and properties. Here's what a vector field looks like in a fields collection:
 
 ```json
 {
@@ -54,17 +68,17 @@ Vector fields are distinguished by their data type and vector-specific propertie
 }
 ```
 
-Vector fields have [specific data types](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields). Currently, `Collection(Edm.Single)` is the most common, but using narrow data types can save on storage.
+Only [certain data types](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields) are supported for vector fields. The most common type is `Collection(Edm.Single)`, but using narrow types can save on storage.
 
-Vector fields must be searchable and retrievable, but they can't be filterable, facetable, or sortable, or have analyzers, normalizers, or synonym map assignments. 
+Vector fields must be searchable and retrievable, but they can't be filterable, facetable, or sortable. They also can't have analyzers, normalizers, or synonym map assignments.
 
-Vector fields must have `dimensions` set to the number of embeddings generated by the embedding model. For example, text-embedding-ada-002 generates 1,536 embeddings for each chunk of text. 
+The `dimensions` property must be set to the number of embeddings generated by the embedding model. For example, text-embedding-ada-002 generates 1,536 embeddings for each chunk of text.
 
-Vector fields are indexed using algorithms indicated by a *vector search profile*, which is defined elsewhere in the index and thus not shown in the example. For more information, see [vector search configuration](vector-search-how-to-create-index.md).
+Vector fields are indexed using algorithms specified in a *vector search profile*, which is defined elsewhere in the index and not shown in this example. For more information, see [Add a vector search configuration](vector-search-how-to-create-index.md#add-a-vector-search-configuration).
 
 ### Fields collection for basic vector workloads
 
-Vector stores require more fields besides vector fields. For example, a key field (`"id"` in this example) is an index requirement. 
+Vector indexes require more than just vector fields. For example, all indexes must have a key field, which is `id` in the following example:
 
 ```json
 "name": "example-basic-vector-idx",
@@ -76,38 +90,47 @@ Vector stores require more fields besides vector fields. For example, a key fiel
 ]
 ```
 
-Other fields, such as the `"content"` field, provide the human readable equivalent of the `"content_vector"` field. If you're using language models exclusively for response formulation, you can omit nonvector content fields, but solutions that push search results directly to client apps should have nonvector content.
+Other fields, such as the `content` field, provide the human-readable equivalent of the `content_vector` field. If you're using language models exclusively for response formulation, you can omit nonvector content fields, but solutions that push search results directly to client apps should have nonvector content.
 
-Metadata fields are useful for filters, especially if metadata includes origin information about the source document. You can't filter on a vector field directly, but you can set prefilter or postfilter modes to filter before or after vector query execution.
+Metadata fields are useful for filters, especially if they include origin information about the source document. Although you can't filter directly on a vector field, you can set prefilter or postfilter modes to filter before or after vector query execution.
 
 ### Schema generated by the Import and vectorize data wizard
 
-We recommend the [Import and vectorize data wizard](search-get-started-portal-import-vectors.md) for evaluation and proof-of-concept testing. The wizard generates the example schema in this section.
+We recommend the [**Import and vectorize data** wizard](search-get-started-portal-import-vectors.md) for evaluation and proof-of-concept testing. The wizard generates the example schema in this section.
 
-The bias of this schema is that search documents are built around data chunks. If a language model formulates the response, as is typical for RAG apps, you want a schema designed around data chunks.
+The wizard chunks your content into smaller search documents, which benefits RAG apps that use language models to formulate responses. Chunking helps you stay within the input limits of language models and the token limits of semantic ranker. It also improves precision in similarity search by matching queries against chunks pulled from multiple parent documents. For more information, see [Chunk large documents for vector search solutions](vector-search-how-to-chunk-documents.md).
 
-Data chunking is necessary for staying within the input limits of language models, but it also improves precision in similarity search when queries can be matched against smaller chunks of content pulled from multiple parent documents. Finally, if you're using semantic ranker, the semantic ranker also has token limits, which are more easily met if data chunking is part of your approach.
+For each search document in the following example, there's one chunk ID, parent ID, chunk, title, and vector field. The wizard:
 
-In the following example, for each search document, there's one chunk ID, chunk, title, and vector field. The chunkID and parent ID are populated by the wizard, using base 64 encoding of blob metadata (path). Chunk and title are derived from blob content and blob name. Only the vector field is fully generated. It's the vectorized version of the chunk field. Embeddings are generated by calling an Azure OpenAI embedding model that you provide.
++ Populates the `chunk_id` and `parent_id` fields with base64-encoded blob metadata (path).
+
++ Extracts the `chunk` and `title` fields from the blob content and blob name, respectively.
+
++ Creates the `vector` field by calling an Azure OpenAI embedding model that you provide to vectorize the `chunk` field. Only the vector field is fully generated during this process.
 
 ```json
 "name": "example-index-from-import-wizard",
 "fields": [
-  {"name": "chunk_id",  "type": "Edm.String", "key": true, "searchable": true, "filterable": true, "retrievable": true, "sortable": true, "facetable": true, "analyzer": "keyword"},
+  { "name": "chunk_id", "type": "Edm.String", "key": true, "searchable": true, "filterable": true, "retrievable": true, "sortable": true, "facetable": true, "analyzer": "keyword"},
   { "name": "parent_id", "type": "Edm.String", "searchable": true, "filterable": true, "retrievable": true, "sortable": true},
   { "name": "chunk", "type": "Edm.String", "searchable": true, "filterable": false, "retrievable": true, "sortable": false},
   { "name": "title", "type": "Edm.String", "searchable": true, "filterable": true, "retrievable": true, "sortable": false},
   { "name": "vector", "type": "Collection(Edm.Single)", "searchable": true, "retrievable": true, "dimensions": 1536, "vectorSearchProfile": "vector-1707768500058-profile"}
 ]
 ```
 
-### Schema for RAG and chat-style apps
+### Schema for generative search
+
+If you're designing vector storage for RAG and chat-style apps, you can create two indexes:
 
-If you're designing storage for generative search, you can create separate indexes for the static content that you indexed and vectorized, and a second index for conversations that can be used in prompt flows. The following indexes are created from the [**chat-with-your-data-solution-accelerator**](https://github.com/Azure-Samples/azure-search-openai-solution-accelerator) accelerator.
++ One for static content that you indexed and vectorized.
++ One for conversations that can be used in prompt flows.
+
+For illustrative purposes, this section uses the [chat-with-your-data-solution-accelerator](https://github.com/Azure-Samples/azure-search-openai-solution-accelerator) to create the `chat-index` and `conversations` indexes.
 
 :::image type="content" source="media/vector-search-overview/accelerator-indexes.png" alt-text="Screenshot of the indexes created by the accelerator.":::
 
-Fields from the chat index that support generative search experience:
+The following fields from `chat-index` support generative search experiences:
 
 ```json
 "name": "example-index-from-accelerator",
@@ -123,7 +146,7 @@ Fields from the chat index that support generative search experience:
 ]
 ```
 
-Fields from the conversations index that supports orchestration and chat history:
+The following fields from `conversations` support orchestration and chat history:
 
 ```json
 "fields": [
@@ -140,83 +163,92 @@ Fields from the conversations index that supports orchestration and chat history
 ]
 ```
 
-Here's a screenshot showing search results in [Search Explorer](search-explorer.md) for the conversations index. The search score is 1.00 because the search was unqualified. Notice the fields that exist to support orchestration and prompt flows. A conversation ID identifies a specific chat. `"type"` indicates whether the content is from the user or the assistant. Dates are used to age out chats from the history.
+The following screenshot shows search results for `conversations` in [Search explorer](search-explorer.md):
 
 :::image type="content" source="media/vector-search-overview/vector-schema-search-results.png" alt-text="Screenshot of Search Explorer with results from an index designed for RAG apps.":::
 
+In our example, the search score is 1.00 because the search is unqualified. Several fields support orchestration and prompt flows:
+
++ `conversation_id` identifies each chat session.
++ `type` indicates whether the content is from the user or the assistant.
++ `created_at` and `updated_at` age out chats from the history.
+
 ## Physical structure and size
 
-In Azure AI Search, the physical structure of an index is largely an internal implementation. You can access its schema, load and query its content, monitor its size, and manage capacity, but the clusters themselves (inverted and vector indexes), and other files and folders are managed internally by Microsoft.
+In Azure AI Search, the physical structure of an index is largely an internal implementation. You can access its schema, load and query its content, monitor its size, and manage its capacity. However, Microsoft manages the infrastructure and physical data structures stored with your search service.
+
+The size and substance of an index are determined by the:
 
-The size and substance of an index is determined by:
++ Quantity and composition of your documents.
 
-+ Quantity and composition of your documents
 + Attributes on individual fields. For example, more storage is required for filterable fields.
-+ Index configuration, including vector configuration that specifies how the internal navigation structures are created based on whether you choose HNSW or exhaustive KNN for similarity search.
 
-Azure AI Search imposes limits on vector storage, which helps maintain a balanced and stable system for all workloads. To help you stay under the limits, vector usage is tracked and reported separately in the Azure portal, and programmatically through service and index statistics.  
++ Index configuration, including the vector configuration that specifies how the internal navigation structures are created. You can choose HNSW or exhaustive KNN for similarity search.
+
+Azure AI Search imposes limits on vector storage, which helps maintain a balanced and stable system for all workloads. To help you stay under the limits, vector usage is tracked and reported separately in the Azure portal and programmatically through service and index statistics.
 
-The following screenshot shows an S1 service configured with one partition and one replica. This particular service has 24 small indexes, with one vector field on average, each field consisting of 1536 embeddings. The second tile shows the quota and usage for vector indexes. A vector index is an internal data structure created for each vector field. As such, storage for vector indexes is always a fraction of the storage used by the index overall. Other nonvector fields and data structures consume the rest.
+The following screenshot shows an S1 service configured with one partition and one replica. This service has 24 small indexes, each with an average of one vector field consisting of 1,536 embeddings. The second tile shows the quota and usage for vector indexes. Because a vector index is an internal data structure created for each vector field, storage for vector indexes is always a fraction of the overall storage used by the index. Nonvector fields and other data structures consume the rest.
 
 :::image type="content" source="media/vector-search-overview/usage-tiles-storage-vector-index.png" alt-text="Screenshot of usage tiles showing storage, vector index, and index count.":::
 
-Vector index limits and estimations are covered in [another article](vector-search-index-size.md), but two points to emphasize are that maximum storage varies by service tier and by when the search service was created. Newer same-tier services have significantly more capacity for vector indexes. For these reasons, take the following actions:
+Vector index limits and estimations are covered in [another article](vector-search-index-size.md), but two points to emphasize are that maximum storage depends on the creation date and pricing tier of your search service. Newer same-tier services have significantly more capacity for vector indexes. For these reasons, you should:
 
-+ [Check the deployment date of your search service](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date). If it was created before April 3, 2024, you might be able to [upgrade your service](search-how-to-upgrade.md) for greater capacity.
++ [Check the creation date of your search service](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date). If it was created before April 3, 2024, you might be able to [upgrade your service](search-how-to-upgrade.md) for greater capacity.
 
-+ [Choose a scalable tier](search-sku-tier.md) if you anticipate fluctuations in vector storage requirements. The Basic tier is fixed at one partition on older search services. Consider Standard 1 (S1) and above for more flexibility and faster performance. In the 2025-02-01-preview, you can also [switch from a lower tier to a higher tier](search-capacity-planning.md#change-your-pricing-tier).
++ [Choose a scalable tier](search-sku-tier.md) if you anticipate fluctuations in vector storage requirements. For older search services, the Basic tier is fixed at one partition. Consider Standard 1 (S1) and higher for more flexibility and faster performance. In the 2025-02-01-preview, you can also [switch from a lower tier to a higher tier](search-capacity-planning.md#change-your-pricing-tier).
 
 ## Basic operations and interaction
 
-This section introduces vector run time operations, including connecting to and securing a single index.
+This section introduces vector runtime operations, including connecting to and securing a single index.
 
 > [!NOTE]
-> When managing an index, be aware that there's no portal or API support for moving or copying an index. Instead, customers typically point their application deployment solution at a different search service (if using the same index name), or revise the name to create a copy on the current search service, and then build it.
+> There's no portal or API support for moving or copying an index. Typically, you either point your application deployment to a different search service (using the same index name) or revise the name to create a copy on your current search service and then build it.
+
+### Index isolation
+  
+In Azure AI Search, you work with one index at a time. All index-related operations target a single index. There's no concept of related indexes or the joining of independent indexes for either indexing or querying.
 
 ### Continuously available
 
-An index is immediately available for queries as soon as the first document is indexed, but won't be fully operational until all documents are indexed. Internally, an index is [distributed across partitions and executes on replicas](search-capacity-planning.md#concepts-search-units-replicas-partitions). The physical index is managed internally. The logical index is managed by you.
+An index is immediately available for queries as soon as the first document is indexed, but it's not fully operational until all documents are indexed. Internally, an index is [distributed across partitions and executes on replicas](search-capacity-planning.md#concepts-search-units-replicas-partitions). The physical index is managed internally. You manage the logical index.
 
-An index is continuously available, with no ability to pause or take it offline. Because it's designed for continuous operation, any updates to its content, or additions to the index itself, happen in real time. As a result, queries might temporarily return incomplete results if a request coincides with a document update.
+An index is continuously available and can't be paused or taken offline. Because it's designed for continuous operation, updates to its content and additions to the index itself happen in real time. If a request coincides with a document update, queries might temporarily return incomplete results.
 
-Notice that query continuity exists for document operations (refreshing or deleting) and for modifications that don't affect the existing structure and integrity of the current index (such as adding new fields). If you need to make structural updates (changing existing fields), those are typically managed using a drop-and-rebuild workflow in a development environment, or by creating a new version of the index on production service.
+Query continuity exists for document operations, such as refreshing or deleting, and for modifications that don't affect the existing structure or integrity of an index, such as adding new fields. Structural updates, such as changing existing fields, are typically managed using a drop-and-rebuild workflow in a development environment or by creating a new version of the index on the production service.
 
-To avoid an [index rebuild](search-howto-reindex.md), some customers who are making small changes choose to "version" a field by creating a new one that coexists alongside a previous version. Over time, this leads to orphaned content in the form of obsolete fields or obsolete custom analyzer definitions, especially in a production index that is expensive to replicate. You can address these issues on planned updates to the index as part of index lifecycle management.
+To avoid an [index rebuild](search-howto-reindex.md), some customers who are making small changes "version" a field by creating a new one that coexists with a previous version. Over time, this leads to orphaned content by way of obsolete fields and obsolete custom analyzer definitions, especially in a production index that's expensive to replicate. You can address these issues during planned updates to the index as part of index lifecycle management.
 
 ### Endpoint connection
 
 All vector indexing and query requests target an index. Endpoints are usually one of the following:
 
 | Endpoint | Connection and access control |
 |----------|-------------------------------|
-| `<your-service>.search.windows.net/indexes` | Targets the indexes collection. Used when creating, listing, or deleting an index. Admin rights are required for these operations, available through admin [API keys](search-security-api-keys.md) or a [Search Contributor role](search-security-rbac.md#built-in-roles-used-in-search). |
-| `<your-service>.search.windows.net/indexes/<your-index>/docs` | Targets the documents collection of a single index. Used when querying an index or data refresh. For queries, read rights are sufficient, and available through query API keys or a data reader role. For data refresh, admin rights are required. |
+| `<your-service>.search.windows.net/indexes` | Targets the indexes collection. Used when creating, listing, or deleting an index. Admin rights are required for these operations and available through admin [API keys](search-security-api-keys.md) or a [Search Contributor role](search-security-rbac.md#built-in-roles-used-in-search). |
+| `<your-service>.search.windows.net/indexes/<your-index>/docs` | Targets the documents collection of a single index. Used when querying an index or data refresh. For queries, read rights are sufficient and available through query API keys or a data reader role. For data refresh, admin rights are required. |
 
 ### How to connect to Azure AI Search
 
-1. [Make sure you have permissions](search-security-rbac.md) or an [API access key](search-security-api-keys.md). Unless you're querying an existing index, you need admin rights or a contributor role assignment to manage and view content on a search service.
-
-1. [Start with the Azure portal](https://portal.azure.com). The person who created the search service can view and manage the search service, including granting access to others through the **Access control (IAM)** page.
+1. [Make sure you have permissions](search-security-rbac.md) or an [API access key](search-security-api-keys.md). Unless you're querying an existing index, you need admin rights or a Contributor role assignment to manage and view content on a search service.
 
-1. Move on to other clients for programmatic access. We recommend the quickstarts and samples for first steps:
+1. [Start with the Azure portal](https://portal.azure.com). The person who created the search service can view and manage it, including granting access to others on the **Access control (IAM)** page.
 
-   + [Quickstart: REST](search-get-started-vector.md)
-   + [Vector samples](https://github.com/Azure/azure-search-vector-samples/blob/main/README.md)
+1. Move on to other clients for programmatic access. For first steps, we recommend [Quickstart: Vector searching using REST](search-get-started-vector.md) and the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples/blob/main/README.md) repo.
 
-### Secure access to vector data
+### Manage vector stores
 
-Azure AI Search implements data encryption, private connections for no-internet scenarios, and role assignments for secure access through Microsoft Entra ID. The full range of enterprise security features are outlined in [Security in Azure AI Search](search-security-overview.md).
+Azure provides a [monitoring platform](monitor-azure-cognitive-search.md) that includes diagnostic logging and alerting. We recommend that you:
 
-### Manage vector stores
++ [Enable diagnostic logging](search-monitor-enable-logging.md).
++ [Set up alerts](/azure/azure-monitor/alerts/tutorial-metric-alert).
++ [Analyze query and index performance](search-performance-analysis.md).
 
-Azure provides a [monitoring platform](monitor-azure-cognitive-search.md) that includes diagnostic logging and alerting. We recommend the following best practices:
+### Secure access to vector data
 
-+ [Enable diagnostic logging](search-monitor-enable-logging.md)
-+ [Set up alerts](/azure/azure-monitor/alerts/tutorial-metric-alert)
-+ [Analyze query and index performance](search-performance-analysis.md)
+Azure AI Search implements data encryption, private connections for no-internet scenarios, and role assignments for secure access through Microsoft Entra ID. For more information about enterprise security features, see [Security in Azure AI Search](search-security-overview.md).
 
-## See also
+## Related content
 
-+ [Create a vector store using REST APIs (Quickstart)](search-get-started-vector.md)
-+ [Create a vector store](vector-search-how-to-create-index.md)
-+ [Query a vector index](vector-search-how-to-query.md)
\ No newline at end of file
++ [Quickstart: Vector search using REST](search-get-started-vector.md)
++ [Create a vector index](vector-search-how-to-create-index.md)
++ [Query a vector index](vector-search-how-to-query.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおけるベクトルストレージの概要の更新"
}
```

### Explanation
この変更では、Azure AI Searchにおけるベクトルストレージに関するドキュメントが更新され、内容が整理され、詳細が追加されました。主な変更点には、日付の修正、用語の明確化、ベクトルインデックスに関する新しいセクションが含まれています。

重要なポイントとして、ベクトルがテキストや画像などのコンテンツを数学的に表現する高次元の埋め込みであることが強調されており、ベクトルフィールドと非ベクトルフィールドが同じ検索インデックス内で共存できることが説明されています。これにより、検索エンジンが類似性検索を行う際の動作や、ハイブリッド検索を利用した検索方式について詳しく述べられています。

また、インデックススキーマ、ベクトルフィールドの構成、基本操作に関する新たな情報が追加され、ベクトルの取り扱いや管理方法がより具体的に説明されています。特に、データチャンクの処理方法や、リソースの使用に関するベストプラクティスも記載され、ユーザーが効率的にベクトルストレージを活用できるよう配慮されています。

全体として、このドキュメント更新は、Azure AI Searchにおけるベクトル関連の機能とその使用方法をより理解しやすくし、実装を容易にすることを目的としています。


