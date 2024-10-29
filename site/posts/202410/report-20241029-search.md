---
date: '2024-10-29'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ceba2b5...MicrosoftDocs:d84fb33
summary: この差分では、主に2つのドキュメントに対してマイナーなアップデートが行われました。検索制限やクォータに関する情報が更新され、最大実行時間や日付の変更が反映されています。また、Azure
  AI Searchに関する文書には新しい定義と具体的なユースケースが追加され、エンタープライズ対応の検索システムとしての特徴が強調されています。特に、「RAGベースのアプリケーション」の具体的な使用例が紹介されています。重大な破壊的変更はありませんが、古い情報からの移行が求められる点があります。全体として、このアップデートはユーザーにとって正確で最新の情報を提供し、Azure
  AI Searchの利便性を向上させることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ceba2b5...MicrosoftDocs:d84fb33){target="_blank"}

# Highlights
この差分では、主に2つのドキュメントのマイナーアップデートが行われました。検索に関する制限やクォータにおいては、最大実行時間や日付の更新がなされ、Azure AI Searchに関しては新しい定義や具体的なユースケースが追加されています。

## New features
- 「Azure AI Search」の文書で新しい定義が追加され、エンタープライズ対応の検索システムとして強調されています。
- 具体的な使用例として「RAGベースのアプリケーション」が取り上げられています。

## Breaking changes
特に重大な破壊的変更は見られませんが、情報の更新によって古いデータに基づいた理解から最新のものへと移行する必要があります。

## Other updates
- 検索制限とクォータの文書で日付が変更され、最大実行時間の表記が更新されました。
- インデクサーに関する説明で無料プランの実行時間に関する記述が追加されています。

# Insights
このアップデートは、ユーザーがAzureサービスを利用する際により正確で最新の情報をもたらすためのものでしょう。検索制限とクォータに関する文書の更新は、特に運用上の細則（最大実行時間や日付変更）に関するものであり、ユーザーにとって明確な運用基準として役立ちます。以前の情報では具体的でなかった部分が「1-3または3-10分」として明確化されており、運用時の参考になります。

一方、Azure AI Searchに関する文書の変更は、このサービスの新しい視点や用途を紹介する重要な役割を果たしています。「エンタープライズ対応の検索および情報取得システム」として再定義することで、ビジネスにおける活用範囲を広げています。また、新しいユースケースとしての「知識ベースの洞察、情報の発見、および取得拡張生成（RAG）」は、ビジネスプロセス自動化や高度な情報統合を可能にするための具体例として示されています。これにより、Azure AI Searchの利便性がより一層強調されました。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索制限とクォータに関する文書の更新 | modified | 3 | 4 | 7 | 
| [search-what-is-azure-search.md](#item-93853a) | minor update | Azure AI Searchに関する文書の内容更新 | modified | 7 | 3 | 10 | 


# Modified Contents
## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 10/24/2024
+ms.date: 10/28/2024
 ms.custom:
   - references_regions
   - build-2024
@@ -120,8 +120,7 @@ Maximum running times exist to provide balance and stability to the service as a
 | Maximum skillsets <sup>4</sup> |3 |5 or 15 |50 |200 |200 |N/A |10 |10 |
 | Maximum indexing load per invocation |10,000 documents |Limited only by maximum documents |Limited only by maximum documents |Limited only by maximum documents |Limited only by maximum documents |N/A |No limit |No limit |
 | Minimum schedule | 5 minutes |5 minutes |5 minutes |5 minutes |5 minutes |5 minutes |5 minutes | 5 minutes |
-| Maximum running time <sup>5</sup>| 1-3 minutes |2 or 24 hours |2 or 24 hours |2 or 24 hours |2 or 24 hours |N/A  |2 or 24 hours |2 or 24 hours |
-| Maximum running time for indexers with a skillset <sup>6</sup> | 3-10 minutes |2 or 24 hours |2 or 24 hours |2 or 24 hours |2 or 24 hours |N/A  |2 or 24 hours |2 or 24 hours |
+| Maximum running time <sup>5</sup>| 1-3 or 3-10 minutes |2 or 24 hours |2 or 24 hours |2 or 24 hours |2 or 24 hours |N/A  |2 or 24 hours |2 or 24 hours |
 | Blob indexer: maximum blob size, MB |16 |16 |128 |256 |256 |N/A  |256 |256 |
 | Blob indexer: maximum characters of content extracted from a blob <sup>6</sup> |32,000 |64,000 |4&nbsp;million |8&nbsp;million |16&nbsp;million |N/A |4&nbsp;million |4&nbsp;million |
 
@@ -133,7 +132,7 @@ Maximum running times exist to provide balance and stability to the service as a
 
 <sup>4</sup> Maximum of 30 skills per skillset.
 
-<sup>5</sup> Regarding the 2 or 24 hour maximum duration for indexers: a 2-hour maximum is the most common and it's what you should plan for. It refers to indexers that run in the [public environment](search-howto-run-reset-indexers.md#indexer-execution), used to offload computationally intensive processing and leave more resources for queries. The 24-hour limit applies if you configure the indexer to run in a private environment using only the infrastructure that's allocated to your search service. Note that some older indexers are incapable of running in the public environment, and those indexers always have a 24-hour processing range. If you have unscheduled indexers that run continuously for 24 hours, you can assume those indexers couldn't be migrated to the newer infrastructure. As a general rule, for indexing jobs that can't finish within two hours, put the indexer on a [5 minute schedule](search-howto-schedule-indexers.md) so that the indexer can quickly pick up where it left off.
+<sup>5</sup> Regarding the 2 or 24 hour maximum duration for indexers: a 2-hour maximum is the most common and it's what you should plan for. It refers to indexers that run in the [public environment](search-howto-run-reset-indexers.md#indexer-execution), used to offload computationally intensive processing and leave more resources for queries. The 24-hour limit applies if you configure the indexer to run in a private environment using only the infrastructure that's allocated to your search service. Note that some older indexers are incapable of running in the public environment, and those indexers always have a 24-hour processing range. If you have unscheduled indexers that run continuously for 24 hours, you can assume those indexers couldn't be migrated to the newer infrastructure. As a general rule, for indexing jobs that can't finish within two hours, put the indexer on a [5 minute schedule](search-howto-schedule-indexers.md) so that the indexer can quickly pick up where it left off. On the Free tier, the 3-10 minute maximum running time is for indexers with skillsets.
 
 <sup>6</sup> The maximum number of characters is based on Unicode code units, specifically UTF-16.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索制限とクォータに関する文書の更新"
}
```

### Explanation
この変更では、「検索制限とクォータに関する」文書が修正され、いくつかの情報が更新されました。具体的には、日付が2024年10月24日から2024年10月28日へと変更され、最大実行時間に関する情報が調整されました。新しい最大実行時間は「1-3または3-10分」として明確に記載され、旧情報がいくつか削除されています。また、インデクサーに関する説明が更新され、特に無料プランにおける実行時間の指定が追加されています。この文書の改定により、ユーザーは最新のサービス仕様に基づいた理解を得ることができます。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -8,14 +8,18 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: overview
-ms.date: 10/08/2024
+ms.date: 10/27/2024
 ---
 
 # What's Azure AI Search?
 
-Azure AI Search ([formerly known as "Azure Cognitive Search"](whats-new.md#new-service-name)) provides secure information retrieval at scale over user-owned content in traditional and generative AI search applications.
+Azure AI Search ([formerly known as "Azure Cognitive Search"](whats-new.md#new-service-name)) is an enterprise-ready search and retrieval system, with a comprehensive set of advanced search technology, built for high-performance applications at any scale.  
 
-Information retrieval is foundational to any app that surfaces text and vectors. Common scenarios include catalog or document search, data exploration, and increasingly feeding query results to prompts based on your proprietary grounding data for conversational and copilot search. When you create a search service, you work with the following capabilities:
+Azure AI Search is the primary recommended retrieval system when building RAG-based applications on Azure, with native LLM integrations between Azure OpenAI Service and Azure Machine Learning.
+
+Azure AI Search can be used in both traditional and GenAI scenarios. Common use cases include knowledge base insights (catalog or document search), information discovery (data exploration), retrieval-augmented generation (RAG), and automation.  
+
+When you create a search service, you work with the following capabilities:
 
 + A search engine for [vector search](vector-search-overview.md) and [full text](search-lucene-query-architecture.md) and [hybrid search](hybrid-search-overview.md) over a search index 
 + Rich indexing with [integrated data chunking and vectorization](vector-search-integrated-vectorization.md), [lexical analysis](search-analyzers.md) for text, and [optional applied AI](cognitive-search-concept-intro.md) for content extraction and transformation
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchに関する文書の内容更新"
}
```

### Explanation
この変更では、「Azure AI Search」についての文書が修正され、内容がアップデートされました。主な変更点として、日付が2024年10月8日から2024年10月27日へと更新され、Azure AI Searchを「エンタープライズ対応の検索および情報取得システム」として強調する新しい定義が追加されました。また、情報取得の重要性や具体的な使用例についても説明が改訂され、特に「RAGベースのアプリケーション」の構築におけるAzure AI Searchの推奨利用が示されています。新しいユースケースとしては、知識ベースの洞察、情報の発見、取得拡張生成（RAG）、および自動化が言及され、これによりサービスの利便性と適用範囲が視覚化されています。


