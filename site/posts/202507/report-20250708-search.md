---
date: '2025-07-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2645652...MicrosoftDocs:1d05d59
summary: このコード差分では、Azure検索サービスに関連するドキュメントの軽微な更新が行われています。主な変更点には、リンクの正確性向上、新しい情報セクションの追加、目次の再構成、インテグレーションに関する重要な認証情報の追加が含まれています。特に破壊的な変更はなく、全体的にユーザーのアクセス性や利便性を向上させることを目的としています。更新により、ユーザーはより効率的に情報を取得できるようになり、全体的なドキュメントの品質が向上します。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2645652...MicrosoftDocs:1d05d59){target="_blank"}

# ハイライト
このコード差分では、Azure検索サービスに関連するドキュメントの軽微な更新が行われています。主な変更点として、リンク先の正確性の向上、新たな情報セクションの追加、目次の再構成、およびインテグレーションに関する重要な認証情報の追加が含まれています。

## 新機能
- 目次に新しく「概念」「適用されたAI」「検索」「関連性」「セキュリティ」などのセクションが追加され、それによりドキュメントがより整理されました。
- 検索サービスのアップグレード手順に新たに「アップグレード中の検索サービスの可用性に関する注意点」が追加されました。

## 破壊的変更
- 特に破壊的な変更は発生していません。ただし、新しいリンクや構成が部分的に導入され、ユーザーのアクセス方法が多少変わる可能性があります。

## その他の更新
- サンプルアプリのリンクがリポジトリに変更されました。
- いくつかの日付と細かい文章が最新の日付と内容に更新されました。

# 洞察
この差分に見られる変更は、Azure検索に関連するユーザードキュメントの整合性と利便性を向上させることを目的としています。具体的には、ドキュメント内のリンクを現在有効な情報に更新することで、ユーザーが必要な情報にスムーズにアクセスできるよう配慮されています。さらに、アップグレード手順における「サービスの可用性」についての注意点が追加され、実運用環境での影響を最小限にするための情報も提供されています。

また、目次の再構成によって、情報へのアクセス性が向上しました。特に、新しく加わったセクションはユーザーが異なる技術領域に迅速にアクセスできるよう設計されており、全体としてのユーザー体験をより良いものにすることが期待されます。インテグレーションとベクター化に関する新しい注意点の追加により、特定のモデルにおける認証方法について明確に記されているため、技術的実装における潜在的な問題を防ぐ手助けをしています。

この更新は、Azure検索のユーザーが効率的に最新情報を取得し、適切に機能を利用できるようになることを意図しており、全体としてドキュメントの品質とユーザー体験を向上させるものとなっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [samples-dotnet.md](#item-12f3fa) | minor update | サンプルDotNetの記事の更新 | modified | 1 | 1 | 2 | 
| [search-how-to-upgrade.md](#item-990225) | minor update | 検索サービスのアップグレード手順の更新 | modified | 5 | 5 | 10 | 
| [toc.yml](#item-c4768f) | minor update | 目次ファイルの再構成 | modified | 72 | 72 | 144 | 
| [vector-search-integrated-vectorization-ai-studio.md](#item-353fcc) | minor update | インテグレーションとベクター化に関する注意点の追加 | modified | 4 | 1 | 5 | 


# Modified Contents
## articles/search/samples-dotnet.md{#item-12f3fa}

<details>
<summary>Diff</summary>
````diff
@@ -79,7 +79,7 @@ A demo repo provides proof-of-concept source code for examples or scenarios show
 
 | Samples | Repository | Description |
 |---------|------------|-------------|
-| Covid-19 search app | [covid19search](https://github.com/liamca/covid19search) | Source code repository for the Azure AI Search based [Covid-19 Search App](https://covid19search.azurewebsites.net/). |
+| Covid-19 search app | [covid19search](https://github.com/liamca/covid19search) | Source code repository for the Azure AI Search based [Covid-19 Search App](https://github.com/liamca/covid19search). |
 | JFK demo | [AzureSearch JFK Files](https://github.com/Microsoft/AzureSearch_JFK_Files) | Learn more about the [JFK solution](https://www.microsoft.com/ai/ai-lab-jfk-files). |
 
 ## Other samples
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サンプルDotNetの記事の更新"
}
```

### Explanation
この変更は、`articles/search/samples-dotnet.md`というファイル内の内容に関する軽微な更新です。具体的には、Covid-19検索アプリの説明の一部が修正されました。以前はリンク先が「https://covid19search.azurewebsites.net/」として提供されていましたが、現在はリポジトリへのリンク「https://github.com/liamca/covid19search」に変更されています。この修正により、リンクの正確性が向上し、リポジトリへのアクセスがより便利になりました。変更内容は、行の削除と追加があり、合計で2つの変更が行われています。

## articles/search/search-how-to-upgrade.md{#item-990225}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.custom: references_regions
-ms.date: 04/29/2025
+ms.date: 07/07/2025
 ---
 
 # Upgrade your Azure AI Search service in the Azure portal
@@ -76,7 +76,9 @@ The date you created your service partially determines its [upgrade eligibility]
 
 ## Upgrade your service
 
-You can’t undo a service upgrade. Before you proceed, make sure that you want to permanently increase the [storage limit](#higher-storage-limits) and [vector index size](#higher-vector-limits) of your search service. We recommend that you test this operation in a nonproduction environment.
+You can't undo a service upgrade. Before you proceed, make sure that you want to permanently increase the [storage limit](#higher-storage-limits) and [vector index size](#higher-vector-limits) of your search service. We recommend that you test this operation in a nonproduction environment.
+
+The availability of your search service during an upgrade depends on how many replicas you've provisioned. With two or more replicas, your service remains available while one replica is updated. For more information, see [Reliability in Azure AI Search](search-reliability.md).
 
 To upgrade your service:
 
@@ -100,9 +102,7 @@ To upgrade your service:
 
 1. Check your notifications to confirm that the operation started.
 
-   The upgrade is an asynchronous operation, so you can continue using your service. Depending on the size of your service, the upgrade can take several hours to complete.
-
-   If the upgrade fails, your service returns to its original state.
+   Depending on the size of your service, this operation can take several hours to complete. If the upgrade fails, your service returns to its original state.
 
 ## Next step
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスのアップグレード手順の更新"
}
```

### Explanation
この変更は、`articles/search/search-how-to-upgrade.md`というファイルの内容に関する軽微な更新です。主な変更点は、文書の日付が「04/29/2025」から「07/07/2025」に修正されたことです。また、サービスのアップグレードに関する説明が明確になり、新たに「アップグレード中の検索サービスの可用性に関する注意点」が追加されました。この新しいセクションでは、レプリカの数によってアップグレード中のサービスの可用性が影響を受けることが説明されています。さらに、いくつかの文の構成が見直され、情報がより整理されています。修正は合計で10行におよび、5行の削除と5行の追加が行われました。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -14,6 +14,62 @@ items:
   - name: FAQ
     href: search-faq-frequently-asked-questions.yml
   expanded: true
+- name: Concepts
+  items:
+  - name: Data
+    items:
+    - name: Search index
+      href: search-what-is-an-index.md
+    - name: Vector index
+      href: vector-store.md
+    - name: Knowledge store
+      href: knowledge-store-concept-intro.md
+    - name: Data import strategies
+      href: search-what-is-data-import.md
+    - name: Indexers
+      href: search-indexer-overview.md
+  - name: Applied AI
+    items:
+    - name: Multimodal search
+      href: multimodal-search-overview.md
+    - name: Built-in vectorization
+      href: vector-search-integrated-vectorization.md
+    - name: AI enrichment during indexing
+      href: cognitive-search-concept-intro.md
+    - name: Enrichment cache
+      href: cognitive-search-incremental-indexing-conceptual.md
+    - name: Skillsets
+      href: cognitive-search-working-with-skillsets.md
+  - name: Retrieval
+    items:
+    - name: Agentic search
+      href: search-agentic-retrieval-concept.md
+    - name: Full-text search
+      href: search-lucene-query-architecture.md
+    - name: Vector search
+      href: vector-search-overview.md
+    - name: Hybrid search
+      href: hybrid-search-overview.md
+    - name: Retrieval Augmented Generation (RAG)
+      href: retrieval-augmented-generation-overview.md
+    - name: Other query types
+      href: search-query-overview.md
+  - name: Relevance
+    items:
+    - name: Semantic ranking
+      href: semantic-search-overview.md
+    - name: BM25 ranking
+      href: index-similarity-and-scoring.md
+    - name: Vector ranking
+      href: vector-search-ranking.md
+    - name: Hybrid ranking (RRF)
+      href: hybrid-search-ranking.md
+  - name: Security
+    items:
+    - name: Security overview
+      href: search-security-overview.md
+    - name: Secure access to external data
+      href: search-indexer-securing-resources.md
 - name: Quickstarts
   items:
   - name: Agentic search
@@ -130,76 +186,6 @@ items:
       href: cognitive-search-tutorial-blob.md
     - name: Debug a skillset
       href: cognitive-search-tutorial-debug-sessions.md
-- name: Samples
-  items:
-  - name: C# samples
-    href: samples-dotnet.md
-  - name: Java samples
-    href: samples-java.md
-  - name: JavaScript samples
-    href: samples-javascript.md
-  - name: Python samples
-    href: samples-python.md
-  - name: REST samples
-    href: samples-rest.md
-  - name: Vector samples
-    href: https://github.com/Azure/azure-search-vector-samples
-- name: Concepts
-  items:
-  - name: Data
-    items:
-    - name: Search index
-      href: search-what-is-an-index.md
-    - name: Vector index
-      href: vector-store.md
-    - name: Knowledge store
-      href: knowledge-store-concept-intro.md
-    - name: Data import strategies
-      href: search-what-is-data-import.md
-    - name: Indexers
-      href: search-indexer-overview.md
-  - name: Applied AI
-    items:
-    - name: Multimodal search
-      href: multimodal-search-overview.md
-    - name: Built-in vectorization
-      href: vector-search-integrated-vectorization.md
-    - name: AI enrichment during indexing
-      href: cognitive-search-concept-intro.md
-    - name: Enrichment cache
-      href: cognitive-search-incremental-indexing-conceptual.md
-    - name: Skillsets
-      href: cognitive-search-working-with-skillsets.md
-  - name: Retrieval
-    items:
-    - name: Agentic search
-      href: search-agentic-retrieval-concept.md
-    - name: Full-text search
-      href: search-lucene-query-architecture.md
-    - name: Vector search
-      href: vector-search-overview.md
-    - name: Hybrid search
-      href: hybrid-search-overview.md
-    - name: Retrieval Augmented Generation (RAG)
-      href: retrieval-augmented-generation-overview.md
-    - name: Other query types
-      href: search-query-overview.md
-  - name: Relevance
-    items:
-    - name: Semantic ranking
-      href: semantic-search-overview.md
-    - name: BM25 ranking
-      href: index-similarity-and-scoring.md
-    - name: Vector ranking
-      href: vector-search-ranking.md
-    - name: Hybrid ranking (RRF)
-      href: hybrid-search-ranking.md
-  - name: Security
-    items:
-    - name: Security overview
-      href: search-security-overview.md
-    - name: Secure access to external data
-      href: search-indexer-securing-resources.md
 - name: How-to guides
   items:
   - name: Service management
@@ -605,11 +591,25 @@ items:
       href: knowledge-store-projection-example-long.md
     - name: Connect with Power BI
       href: knowledge-store-connect-power-bi.md
+- name: Samples
+  items:
+  - name: C# samples
+    href: samples-dotnet.md
+  - name: Java samples
+    href: samples-java.md
+  - name: JavaScript samples
+    href: samples-javascript.md
+  - name: Python samples
+    href: samples-python.md
+  - name: REST samples
+    href: samples-rest.md
+  - name: Vector samples
+    href: https://github.com/Azure/azure-search-vector-samples
 - name: Responsible AI
   items:
   - name: Transparency note
     href: /azure/ai-foundry/responsible-ai/search/transparency-note
-- name: Reference
+- name: References
   items:
   - name: REST API reference
     items:
@@ -795,4 +795,4 @@ items:
     - name: Tools and accelerators
       href: resource-tools.md
     - name: Training
-      href: resource-training.md
+      href: resource-training.md
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次ファイルの再構成"
}
```

### Explanation
この変更は、`articles/search/toc.yml`というファイルの内容に関する大規模な更新です。具体的には、以前の項目が削除され、新たに「概念」「適用されたAI」「検索」「関連性」「セキュリティ」などのセクションが追加され、各セクション内に複数の項目が構成されています。また、サンプルに関するセクションも復活し、C#、Java、JavaScript、Python、REST、およびベクターサンプルが含まれるようになりました。これにより、目次がより整理され、情報へのアクセスが容易になっています。変更は合計で144行にわたり、72行の削除と72行の追加が行われ、全体の構成が一新されています。

## articles/search/vector-search-integrated-vectorization-ai-studio.md{#item-353fcc}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 05/30/2025
+ms.date: 07/07/2025
 ---
 
 # Use embedding models from Azure AI Foundry model catalog for integrated vectorization
@@ -277,6 +277,9 @@ If you can't use key-based authentication, you can instead configure the AML ski
 "region": "westus", // Only need if AML project lives in different region from search service
 ```
 
+> [!NOTE]
+> Token authentication is not currently supported for Cohere models for this integration; only key authentication is available at this time.  
+
 ## Next steps
 
 + [Configure a vectorizer in a search index](vector-search-how-to-configure-vectorizer.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インテグレーションとベクター化に関する注意点の追加"
}
```

### Explanation
この変更は、`articles/search/vector-search-integrated-vectorization-ai-studio.md`というファイルの軽微な更新です。主な変更点として、文書の日付が「05/30/2025」から「07/07/2025」に修正されました。さらに、Cohereモデルに関する注意事項が追加され、トークン認証がこのインテグレーションには現在サポートされておらず、キー認証のみが利用可能である旨が明記されました。この変更により、ユーザーはインテグレーションにおける認証方法についての重要な情報を得られるようになりました。全体として、変更は5行であり、4行の追加と1行の削除が行われました。


