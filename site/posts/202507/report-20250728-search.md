---
date: '2025-07-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a24e358...MicrosoftDocs:c91b816
summary: この差分は、Azure AI Searchに関連するドキュメントの小規模な更新を含んでおり、新しい見出しの追加やリンクの修正が主な変更点です。各ドキュメントには「参照」という新しい見出しが追加され、関連リンクが充実しました。また、「検索の関連性」に関する情報や「行レベルセキュリティ」に関する更新も行われています。破壊的な変更は特にありませんが、既存の文書の見出しやリンクが整理され、一貫性が保たれました。これらの更新により、ユーザーは関連情報へのアクセスが容易になり、検索結果の質が向上し、ドキュメントの体系的な学びの道筋が整備されました。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a24e358...MicrosoftDocs:c91b816){target="_blank"}

<format>
# ハイライト
この差分は、Azure AI Searchに関連するさまざまなドキュメントの小規模な更新を含んでいます。新しい見出しの追加やリンクの修正が主な変更点です。

## 新機能
- 各ドキュメントに「参照」という新しい見出しが追加され、関連リンクが充実しました。
- 「検索の関連性」に関する情報が追加され、検索結果の質を向上させるための提案がなされています。
- 「行レベルセキュリティ」に関する情報が更新されました。

## 破壊的変更
- 破壊的な変更は特にありませんが、既存のドキュメントの見出しやリンクが整理され、表記の一貫性が持たせられました。

## その他の更新
- 各ドキュメントにおいて、見出しの変更と関連コンテンツへのリンクが強化されています。
- 目次ファイル「toc.yml」での項目の整理と追加が行われました。

# インサイト
これらの更新は、Azure AI Searchのドキュメントがユーザーにとってより使いやすく、役立つものとなることを目的としており、以下の点で特に有意義です。

まず、関連情報へのアクセスが容易になりました。各文書に新設された「参照」セクションは、ユーザーが求める関連情報やリソースに迅速にアクセスするための効果的なナビゲーションを提供します。たとえば、Azure AI Searchに関する役割ベースのアクセス制御や、クエリ中のACL、RBAC施行に関するガイドは、管理者や開発者がAzure環境におけるインデックス制御とセキュリティを強化するために不可欠です。

次に、「行レベルセキュリティ」に関する更新は、Azure AI Searchのデータ保護機能を高めます。プレビューとして導入されたこの機能は、ユーザーの権限に基づいて検索結果をフィルタリングする新たなアプローチを提供し、機密情報の取り扱いにおける柔軟性を向上させます。特に、権限メタデータを保持し、クエリ時に適用可能である点は、より厳格なセキュリティ要件を満たすための強力なツールです。

また、Azure AI Searchの関連性チューニングに関する情報は、小さな調整であっても検索体験の向上に繋がる可能性を示しています。ユーザーは、ベクトルコンテンツの関連性向上の手段を探求することで、検索結果の精度を高めることができます。

最後に、目次の整理と項目追加は、ユーザーがドキュメントを通じて体系的に学ぶための道筋を明確にします。情報の構成を再調整することで、Azure AI Searchの各コンポーネントや機能に迅速にアクセスできるようになるため、学習曲線が緩和され、製品の効果的な活用を促進します。

以上のように、これらのドキュメント更新は、ユーザーの体験を向上させるための戦略的な取り組みであり、Azure AI Searchの性能や安全性を強化し、製品に対する理解を深める契機となります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-blob-indexer-role-based-access.md](#item-887e42) | minor update | 検索ブロブインデクサーの役割ベースのアクセスに関する記事の更新 | modified | 4 | 3 | 7 | 
| [search-index-access-control-lists-and-rbac-push-api.md](#item-45e71e) | minor update | インデックスアクセス制御リストとRBACに関する記事の更新 | modified | 2 | 1 | 3 | 
| [search-indexer-access-control-lists-and-role-based-access.md](#item-67b42f) | minor update | インデクサーアクセス制御リストと役割ベースのアクセスに関する記事の更新 | modified | 5 | 0 | 5 | 
| [search-query-access-control-rbac-enforcement.md](#item-d24df7) | minor update | クエリアクセス制御とRBAC施行に関する記事の更新 | modified | 1 | 1 | 2 | 
| [search-relevance-overview.md](#item-cb0e09) | minor update | 検索の関連性に関する記事の更新 | modified | 8 | 3 | 11 | 
| [search-security-overview.md](#item-6b3f1e) | minor update | Azure AI Searchのセキュリティに関する記事の更新 | modified | 5 | 3 | 8 | 
| [search-what-is-an-index.md](#item-5a3344) | minor update | Azure AI Searchにおけるインデックスの説明の更新 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c4768f) | minor update | 目次の更新 | modified | 10 | 10 | 20 | 


# Modified Contents
## articles/search/search-blob-indexer-role-based-access.md{#item-887e42}

<details>
<summary>Diff</summary>
````diff
@@ -168,9 +168,10 @@ JSON schema example:
 
 To effectively manage blob deletion, ensure that you have enabled [deletion tracking](search-howto-index-changed-deleted-blobs.md) before your indexer runs for the first time. This feature allows the system to detect deleted blobs from your source and have them deleted from the index.  
 
-## Related content
+## See also
 
++ [Connect to Azure AI Search using roles](search-security-rbac.md)
+- [Query-Time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md)
+- [azure-search-python-samples/Quickstart-Document-Permissions-Push-API](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Document-Permissions-Push-API)
 + [Search over Azure Blob Storage content](search-blob-storage-integration.md)
 + [Configure a blob indexer](search-howto-indexing-azure-blob-storage.md)
-+ [Change and delete detection using indexers for Azure Storage](search-howto-index-changed-deleted-blobs.md)
-+ [Connect to Azure AI Search using roles](search-security-rbac.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索ブロブインデクサーの役割ベースのアクセスに関する記事の更新"
}
```

### Explanation
この変更は、「検索ブロブインデクサーの役割ベースのアクセス」に関するドキュメントの小規模な更新です。主に追加された情報として、「見出し」が「関連コンテンツ」から「参照」に変更され、さらに関連するリンクが追加されました。具体的には、Azure AI Searchに役割を使って接続する方法や、Azure Blob Storage内のコンテンツの検索に関する文書、役割ベースのアクセス制御(RBAC)に関連する情報が含まれています。この更新は、情報の組織を改善し、ユーザーが関連リソースをより簡単に見つけられるようにすることを目的としています。

## articles/search/search-index-access-control-lists-and-rbac-push-api.md{#item-45e71e}

<details>
<summary>Diff</summary>
````diff
@@ -122,7 +122,8 @@ This example illustrates how the document access rules are resolved based on the
 | 6 | ["user1", "user2"] | ["group1"] | Empty | User1, user2, or any member of group1 | |
 | 7 | ["user1", "user2"] | [] | Empty | User1, user2, or any user with RBAC permissions to container1 | |
 
-## Next steps
+## See also
 
+- [Connect to Azure AI Search using roles](search-security-rbac.md)
 - [Query-Time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md)
 - [azure-search-python-samples/Quickstart-Document-Permissions-Push-API](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Document-Permissions-Push-API)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスアクセス制御リストとRBACに関する記事の更新"
}
```

### Explanation
この更新は、「インデックスアクセス制御リストとRBACに関するドキュメント」の小規模な変更です。主に、「次のステップ」という見出しが「参照」に変更され、さらに関連情報へのリンクが追加されました。具体的には、Azure AI Searchに役割を使って接続する方法や、クエリ時のACLおよびRBACの施行に関する情報、ドキュメント権限を設定するためのPythonサンプルへのリンクが追加されています。この変更により、ユーザーは関連するリソースを見つけやすくなり、アクセス制御の設定に関する理解を深めることができます。

## articles/search/search-indexer-access-control-lists-and-role-based-access.md{#item-67b42f}

<details>
<summary>Diff</summary>
````diff
@@ -298,3 +298,8 @@ Choose one of the following mechanisms, depending on how many items changed:
 
 To effectively manage blob deletion, ensure that you have enabled [deletion tracking](search-howto-index-changed-deleted-blobs.md) before your indexer runs for the first time. This feature allows the system to detect deleted blobs from your source and have them deleted from the index.
 
+## See also
+
++ [Connect to Azure AI Search using roles](search-security-rbac.md)
++ [Query-Time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md)
++ [azure-search-python-samples/Quickstart-Document-Permissions-Push-API](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Document-Permissions-Push-API)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーアクセス制御リストと役割ベースのアクセスに関する記事の更新"
}
```

### Explanation
この変更は、「インデクサーアクセス制御リストと役割ベースのアクセス」に関するドキュメントの小規模な更新です。新たに「参照」という見出しが追加され、いくつかの関連情報へのリンクが記載されました。追加されたリンクには、Azure AI Searchに役割を使って接続する方法、クエリ時のACLとRBACの施行に関するガイド、およびドキュメント権限をプッシュAPIで設定するためのPythonサンプルが含まれています。この更新により、ユーザーは関連するリソースをより簡単に見つけることができ、インデクサーアクセス制御に関する知識が深まることを目的としています。

## articles/search/search-query-access-control-rbac-enforcement.md{#item-d24df7}

<details>
<summary>Diff</summary>
````diff
@@ -76,7 +76,7 @@ Content-Type: application/json
 }
 ```
 
-## Related content
+## See also
 
 - [Tutorial: Index ADLS Gen2 permission metadata](tutorial-adls-gen2-indexer-acls.md) 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリアクセス制御とRBAC施行に関する記事の更新"
}
```

### Explanation
この更新は、「クエリアクセス制御とRBAC施行」に関するドキュメントの小規模な変更です。具体的には、「関連コンテンツ」という見出しが「参照」に変更され、その後に続くリンクが変更されていません。このリンクは、ADLS Gen2の権限メタデータをインデックス化するためのチュートリアルに関するもので、ユーザーが関連情報を見つけやすくなります。この変更により、ドキュメントの表記が一貫性を持つことが目指されています。

## articles/search/search-relevance-overview.md{#item-cb0e09}

<details>
<summary>Diff</summary>
````diff
@@ -13,14 +13,19 @@ ms.date: 07/23/2025
 
 # Relevance in Azure AI Search
 
-In a query operation, the relevance of any given result is measured by a ranking algorithm that determines the strength of a match based on how closely the result aligns with the query’s content or characteristics. An algorithm assigns a score, and results are rank ordered by that score, with the most relevant matches returned in the response. 
+In a query operation, the relevance of any given result is determined by a ranking algorithm that evaluates the strength of a match based on how closely the indexed content and the query align. An algorithm assigns a score, and results are ranked by that score and returned in the response. 
 
 Ranking occurs whenever the query request includes full text or vector queries. It doesn't occur if the query invokes strict pattern matching, such as a filter-only query or a specialized query form like autocomplete, suggestions, geospatial search, fuzzy search, or regular expression search. A uniform search score of 1.0 indicates the absence of a ranking algorithm.
 
-The query engine in Azure AI Search supports a multi-level approach to ranking search results, where there's a built-in ranking modality for each query type, plus extra ranking capabilities for extended relevance tuning.
+You can enhance the quality of ranked results through ***relevance tuning*** that boosts search scores based on extra criteria or analysis. In Azure AI Search, relevance tuning is primarily directed at textual and numeric (nonvector) content when you apply a [scoring profile](#custom-boosting-logic-using-scoring-profiles) or invoke the [semantic ranker](semantic-search-overview.md). 
+
+> [!NOTE]
+> In Azure AI Search, there's no explicit relevance tuning capabilities for vector content, but you can experiment between Hierarchical Navigable Small World (HNSW) and exhaustive K-nearest neighbors (KNN) to see if one algorithm outperforms the other for your scenario. HNSW graphing with an exhaustive KNN override at query time is the most flexible approach for comparison testing. You can also experiment with various embedding models to see which ones produce higher quality results.
 
 ## Levels of ranking
 
+The query engine in Azure AI Search supports a multi-level approach to ranking search results, where there's a built-in ranking modality for each query type, plus extra ranking capabilities for extended relevance tuning.
+
 This section describes the levels of scoring operations. For an illustration of how they work together, see the [diagram](#diagram-of-ranking-algorithms) in this article. A [comparison of all search score types and ranges](#types-of-search-scores) is also provided in this article.
 
 | Level | Description |
@@ -31,7 +36,7 @@ This section describes the levels of scoring operations. For an illustration of
 
 ## Custom boosting logic using scoring profiles
 
-[Scoring profiles](index-add-scoring-profiles.md) are an optional feature for boosting scores based on extra user-defined criteria. Criteria can include weighted fields, or functions that boost by freshness, proximity, magnitude, or range. There's no extra charge for using a scoring profile. To use a scoring profile, you define it in an index and then specify it on a query. 
+[Scoring profiles](index-add-scoring-profiles.md) are an optional feature for boosting scores based on extra user-defined criteria. Criteria can include weighted fields where a match found in a specific field is given more weight than the same match found in a different field. Criteria can also be defined through functions that boost by freshness, proximity, magnitude, or range. There's no extra costs associated with scoring profiles. To use a scoring profile, you define it in an index and then specify it on a query. 
 
 Scoring logic applies to text and numeric nonvector content. You can use scoring profiles with:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索の関連性に関する記事の更新"
}
```

### Explanation
この変更は、「Azure AI Searchにおける検索の関連性」に関するドキュメントに対する小規模な更新です。文中の内容が一部修正され、関連性の評価についての説明がより明確になりました。また、関連性チューニングに関する情報が追加され、どのように検索スコアを向上させるかについて具体的に述べられています。特に、ベクトルコンテンツの明示的な関連性チューニング機能はないことが強調され、その代わりに異なるアルゴリズムを比較する手法が提案されています。これにより、ユーザーは検索結果の質を向上させるための新たなアプローチを理解し、活用できるようになります。また、スコアリングプロファイルの定義と使用方法についての詳細も更新されました。

## articles/search/search-security-overview.md{#item-6b3f1e}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 02/28/2025
+ms.date: 07/26/2025
 ---
 
 # Security in Azure AI Search
@@ -155,9 +155,11 @@ For multitenancy solutions requiring security boundaries at the index level, it'
 
 ### Restricting access to documents
 
-User permissions at the document level, also known as *row-level security*, isn't natively supported in Azure AI Search. If you import data from an external system that provides row-level security, such as Azure Cosmos DB, those permissions won't transfer with the data as its being indexed by Azure AI Search.
+User permissions at the document level, also known as *row-level security*, is available as a preview feature and depends on the data source. If content originates from [Azure Data Lake Storage (ADLS) Gen2](search-indexer-access-control-lists-and-role-based-access.md) or [Azure blobs](search-blob-indexer-role-based-access.md), user permission metadata that originates in Azure Storage is preserved in indexer-generated indexes and enforced at query time so that only authorized content is included in search results.
 
-If you require permissioned access over content in search results, there's a technique for applying filters that include or exclude documents based on user identity. This workaround adds a string field in the data source that represents a group or user identity, which you can make filterable in your index. For more information about this pattern, see [Security trimming based on identity filters](search-security-trimming-for-azure-search.md).
+For other data sources, you can [push a document payload that includes user or group permission metadata](search-index-access-control-lists-and-rbac-push-api.md), and those permissions are retained in indexed content and also enforced at query time. This capability is also in preview.
+
+If you can't use preview features and you require permissioned access over content in search results, there's a technique for applying filters that include or exclude documents based on user identity. This workaround adds a string field in the data source that represents a group or user identity, which you can make filterable in your index. For more information about this pattern, see [Security trimming based on identity filters](search-security-trimming-for-azure-search.md). For more information about document access, see [Document-level access control](search-document-level-access-overview.md).
 
 ## Data residency
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのセキュリティに関する記事の更新"
}
```

### Explanation
この変更は、「Azure AI Searchにおけるセキュリティ」の概要に関するドキュメントに対する小規模な更新です。主な変更点は、ドキュメントレベルのユーザー権限、つまり「行レベルセキュリティ」についての情報が更新されたことです。行レベルセキュリティはプレビュー機能として利用可能になり、特定のデータソースにおいてユーザーの権限メタデータが保持され、クエリ時に適用されることが説明されています。さらに、他のデータソースにおいても、ユーザーやグループの権限を含むドキュメントペイロードをプッシュし、それらの権限がインデックス化されたコンテンツで保持されることができる点が導入されています。プレビュー機能を使用できない場合には、フィルターを適用してユーザーのアイデンティティに基づいてドキュメントを含めたり除外したりするワークアラウンド手法が再確認されています。これにより、ユーザーの承認に基づいた検索結果の制御が可能となります。

## articles/search/search-what-is-an-index.md{#item-5a3344}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.date: 06/20/2025
 
 # Search indexes in Azure AI Search
 
-In Azure AI Search, a *search index* is your searchable content, available to the search engine for indexing, full-text search, vector search, hybrid search, and filtered queries. An index is defined by a schema and saved to the search service, with data import following as a second step. This content exists within your search service, apart from your primary data stores, which is necessary for the millisecond response times expected in modern search applications. Except for indexer-driven indexing scenarios, the search service never connects to or queries your source data.
+In Azure AI Search, a *search index* is your searchable content, available to the search engine for indexing, agentic search, full-text search, vector search, hybrid search, and filtered queries. An index is defined by a schema and saved to the search service, with data ingestion following as a second step. Indexed content exists within your search service, apart from your primary external data stores, which is necessary for the millisecond response times expected in modern search applications. Except for indexer-driven indexing scenarios, the search service never connects to or queries your external source data.
 
 This article covers the key concepts for creating and managing a search index, including:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおけるインデックスの説明の更新"
}
```

### Explanation
この変更は、「Azure AI Searchにおけるインデックスとは何か」に関するドキュメントに対する小規模な更新です。文中の「検索インデックス」の定義において、用語が一部修正されました。具体的には、「エージェント検索（agentic search）」という新しい表現が導入され、データの取り込み（data ingestion）の言葉でデータインポートが置き換えられました。また、インデックス化されたコンテンツが保存される場所についての説明が「主要なデータストア」から「外部データストア」に変更され、Azure AI Searchの機能をより明確に伝える内容となっています。この修正により、ユーザーがAzure AI Searchのインデックスに関する理解を深められることを意図しています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -18,28 +18,22 @@ items:
   items:
   - name: Data
     items:
+    - name: Data import strategies
+      href: search-what-is-data-import.md
     - name: Search index
       href: search-what-is-an-index.md
     - name: Vector index
       href: vector-store.md
     - name: Knowledge store
       href: knowledge-store-concept-intro.md
-    - name: Data import strategies
-      href: search-what-is-data-import.md
     - name: Indexers
       href: search-indexer-overview.md
   - name: Applied AI
     items:
-    - name: Multimodal search
-      href: multimodal-search-overview.md
-    - name: Built-in vectorization
-      href: vector-search-integrated-vectorization.md
     - name: AI enrichment during indexing
       href: cognitive-search-concept-intro.md
-    - name: Enrichment cache
-      href: cognitive-search-incremental-indexing-conceptual.md
-    - name: Skillsets
-      href: cognitive-search-working-with-skillsets.md
+    - name: Built-in vectorization
+      href: vector-search-integrated-vectorization.md
   - name: Retrieval
     items:
     - name: Agentic search
@@ -50,6 +44,8 @@ items:
       href: vector-search-overview.md
     - name: Hybrid search
       href: hybrid-search-overview.md
+    - name: Multimodal search
+      href: multimodal-search-overview.md
     - name: Retrieval Augmented Generation (RAG)
       href: retrieval-augmented-generation-overview.md
     - name: Other query types
@@ -348,6 +344,8 @@ items:
         href: search-howto-index-sharepoint-online.md
     - name: Skillsets (indexers)
       items:
+      - name: Skillsets overview
+        href: cognitive-search-working-with-skillsets.md
       - name: Create a skillset
         href: cognitive-search-defining-skillset.md
       - name: Attach an Azure AI resource
@@ -364,6 +362,8 @@ items:
         href: cognitive-search-output-field-mapping.md
       - name: Process image files
         href: cognitive-search-concept-image-scenarios.md
+      - name: Enrichment cache
+        href: cognitive-search-incremental-indexing-conceptual.md
       - name: Cache (incremental) enrichment
         href: search-howto-incremental-index.md
       - name: Design tips
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新"
}
```

### Explanation
この変更は、「toc.yml」ファイルに対する小規模な更新であり、目次の項目に関する整理と追加が行われています。主要な変更点としては、「データインポート戦略」が再配置され、一部の項目が削除されたり新たに追加されたりしています。具体的には、「適用されたAI」セクションにおいて「マルチモーダル検索」が戻ってきており、他の関連項目も見直しが行われています。また、「スキルセット」の概要が新たに追加され、この情報が容易にアクセス可能になっています。また、同様に「エンリッチメントキャッシュ」もリストに加わりました。これらの変更は、情報の構成を改善し、ユーザーが関連情報を見つけやすくするために行われています。


