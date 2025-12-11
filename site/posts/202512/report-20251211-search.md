---
date: '2025-12-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2bf50f0...MicrosoftDocs:b6de023
summary: |-
  この報告書の要約は以下の通りです。

  変更のハイライトには、Azure Searchに関連する2つの新しいアーキテクチャ画像の追加が含まれています。これにより、ユーザーはエージェント検索とクラシック検索のアーキテクチャを視覚的に理解しやすくなります。また、関連するドキュメントが更新され、情報の明確化や正確性が向上しました。特筆すべき重大な破壊的変更はありませんが、画像変更により以前の参照の確認が必要です。インデックスプロジェクションに関するドキュメントの具体性が向上し、Azure AI Searchの情報も最新に保たれています。これらの更新は、ユーザーが誤解なくシステムを活用できるようサポートし、ドキュメンテーションの品質向上を目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2bf50f0...MicrosoftDocs:b6de023){target="_blank"}

# Highlights
変更のハイライトとしては、Azure Searchのアーキテクチャに関する2つの新しい画像の追加があります。また、関連するドキュメントがアップデートされ、主要な情報の明確化や最新情報の反映が行われています。

## New features
1. **エージェント検索アーキテクチャ画像の追加**:
   - 画像「agentic-retrieval-architecture.png」が追加され、エージェントの検索アーキテクチャを視覚的に説明しています。
   
2. **クラシック検索アーキテクチャ画像の追加**:
   - 画像「classic-search-architecture.png」が追加され、クラシック検索アーキテクチャを視覚化しています。

## Breaking changes
特に重大な破壊的変更はありませんが、ドキュメント内の画像の変更によって、以前の参照が必要ならば確認する必要があります。

## Other updates
- **インデックスプロジェクションに関するドキュメント更新**:
  - フィールドマッピングの具体性を強化し、可読性を向上させるための修正が行われました。
  
- **Azure AI Searchドキュメントの更新**:
  - 日付のアップデート、画像の差し替え、新しいコンテンツの明確化が行われ、情報の正確性が向上しています。

# Insights
今回の更新は、Azure Searchに関連する情報の正確性と最新性を保つために行われました。特に、新たに追加された2つの画像は、ユーザーにとってアーキテクチャをより直感的に理解する手助けを提供します。視覚情報を通じて複雑なコンセプトが表現されており、開発者やエンジニアがこれらのアーキテクチャについて詳細に学ぶ際の一助となります。

インデックスプロジェクションに関するドキュメントの更新では、親子のインデックスフィールドの関係性をより具体的に表現し、実際にAzure Searchを活用しようとする際の指針を提供します。これにより、ユーザーが誤解なくシステムを設計・運用できるようサポートしています。

最終的に、Azure AI Searchのガイドラインドキュメントの細かな更新は、製品の機能や構成理解を促進し、ユーザーが最新の状態でサービスを利用できるよう配慮されています。これらの変更は、単に新しさを追加するだけでなく、長期的な視点でのドキュメンテーション品質の向上を意図しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-architecture.png](#item-446b28) | new feature | エージェントの検索アーキテクチャ画像の追加 | added | 0 | 0 | 0 | 
| [classic-search-architecture.png](#item-88bec4) | new feature | クラシック検索アーキテクチャ画像の追加 | added | 0 | 0 | 0 | 
| [search-how-to-define-index-projections.md](#item-a7e2c5) | minor update | インデックスプロジェクションに関する説明の更新 | modified | 12 | 12 | 24 | 
| [search-what-is-azure-search.md](#item-93853a) | minor update | Azure AI Searchに関するコンテンツの更新 | modified | 4 | 6 | 10 | 


# Modified Contents
## articles/search/media/search-what-is-azure-search/agentic-retrieval-architecture.png{#item-446b28}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "エージェントの検索アーキテクチャ画像の追加"
}
```

### Explanation
この変更では、新たに画像ファイル「agentic-retrieval-architecture.png」が追加されました。この画像は、Azure Searchにおけるエージェントの検索アーキテクチャを視覚的に表現しており、文書内でのコンテンツの理解を深める助けとなります。画像のリンクはGitHubのリポジトリにホストされており、今後のリファレンスやドキュメントの改善に寄与することを目的としています。

## articles/search/media/search-what-is-azure-search/classic-search-architecture.png{#item-88bec4}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "クラシック検索アーキテクチャ画像の追加"
}
```

### Explanation
この変更では、新しい画像ファイル「classic-search-architecture.png」が追加されました。この画像は、Azure Searchにおけるクラシック検索アーキテクチャを説明するものであり、ユーザーがシステムの構成を視覚的に理解するのを助けます。画像はGitHubのリポジトリにてアクセス可能で、今後の文書作成や教育資材に役立つことを意図しています。

## articles/search/search-how-to-define-index-projections.md{#item-a7e2c5}

<details>
<summary>Diff</summary>
````diff
@@ -250,24 +250,24 @@ Now that you've seen several patterns for one-to-many indexings, lets compare ke
 
 - To avoid creating parent search documents and ensuring the index contains only child documents of a uniform grain, set the `targetIndexName` for both the indexer definition and the selector to the same index, but add an extra `parameters` object after `selectors`, with a `projectionMode` key set to `skipIndexingParentDocuments`, as shown here:
 
-    ```json
-    "indexProjections": {
-        "selectors": [
-            ...
-        ],
-        "parameters": {
-            "projectionMode": "skipIndexingParentDocuments"
-        }
-    }
-    ```
+   ```json
+   "indexProjections": {
+       "selectors": [
+           ...
+       ],
+       "parameters": {
+           "projectionMode": "skipIndexingParentDocuments"
+       }
+   }
+   ```
 
 ## Review field mappings
 
 Indexers are affiliated with three different types of field mappings. Before you run the indexer, check your field mappings and know when to use each type.
 
 [Field mappings](search-indexer-field-mappings.md) are defined in an indexer and used to map a source field to an index field. Field mappings are used for data paths that lift data from the source and pass it in for indexing, with no intermediate skills processing step. Typically, an indexer can automatically map fields that have the same name and type. Explicit field mappings are only required when there's discrepancies. In one-to-many indexing and the patterns discussed thus far, you might not need field mappings.
 
-[Output field mappings](cognitive-search-output-field-mapping.md) are defined in an indexer and used to map enriched content generated by a skillset to a field into the main index. In the one-to-many patterns covered in this article, this is the parent index in a [two-index solution](#example-of-separate-parent-child-indexes). In the examples shown in this article, the parent index is sparse, with just a title field, and that field isn't populated with content from the skillset processing, so we don't an output field mapping.
+[Output field mappings](cognitive-search-output-field-mapping.md) are defined in an indexer and used to map enriched content generated by a skillset to a field into the main index. In the one-to-many patterns covered in this article, it is a single index schema that includes parent and child fields. The parent index is sparse, with just a title field. The title field isn't populated with content from the skillset processing, so we don't need an output field mapping.
 
 Indexer projection field mappings are used to map skillset-generated content to fields in the child index. In cases where the child index also includes parent fields (as in the [consolidated index solution](#single-index-schema-inclusive-of-parent-and-child-fields)), you should set up field mappings for every field that has content, including the parent-level title field, assuming you want the title to show up in each chunked document. If you're using [separate parent and child indexes](#example-of-separate-parent-child-indexes), the indexer projections should have field mappings for just the child-level fields.
 
@@ -409,4 +409,4 @@ The indexer definition specifies the components of the pipeline. In the indexer
 Data chunking and one-to-many indexing are part of the RAG pattern in Azure AI Search. Continue on to the following tutorial and code sample to learn more about it.
 
 > [!div class="nextstepaction"]
-> [How to build a RAG solution using Azure AI Search](tutorial-rag-build-solution.md)
\ No newline at end of file
+> [How to build a RAG solution using Azure AI Search](tutorial-rag-build-solution.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスプロジェクションに関する説明の更新"
}
```

### Explanation
この変更では、ドキュメント「search-how-to-define-index-projections.md」に対して小規模な更新が行われました。具体的には、インデックスプロジェクションに関する情報の明確化が目的とされています。コードスニペットが整形され、エクスプレッションがより具体的に説明されています。また、出力フィールドマッピングのセクションでは、親インデックスと子インデックスの関係についての記述が改善され、利用者が各フィールドの役割を正しく理解できるようになっています。全体として、ドキュメントの可読性と理解を向上させるための修正が行われています。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: overview
-ms.date: 12/04/2025
+ms.date: 12/10/2025
 ---
 
 # What is Azure AI Search?
@@ -83,7 +83,7 @@ During indexing, you can use [AI enrichment](cognitive-search-concept-intro.md)
 
 ---
 
-:::image type="content" source="media/search-what-is-azure-search/azure-search.svg" alt-text="Diagram of the Azure AI Search architecture for classic search." lightbox="media/search-what-is-azure-search/azure-search.svg" :::
+:::image type="content" source="media/search-what-is-azure-search/classic-search-architecture.png" alt-text="Diagram of the Azure AI Search architecture for classic search." lightbox="media/search-what-is-azure-search/classic-search-architecture.png" :::
 
 > [!NOTE]
 > This diagram separates the indexing and query engines for clarity, but in Azure AI Search, they're the same component operating in read-write and read-only modes.
@@ -92,13 +92,11 @@ During indexing, you can use [AI enrichment](cognitive-search-concept-intro.md)
 
 [Agentic retrieval](agentic-retrieval-overview.md) is a multi-query pipeline designed for complex agent-to-agent workflows. Each query targets a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) that represents a complete domain of knowledge. Your agent references the knowledge base for *what* to ground on, while the knowledge base handles *how* to perform grounding.
 
-One knowledge base consists of one or more [knowledge sources](agentic-knowledge-source-overview.md), an optional LLM for query planning and answer synthesis, and parameters that govern retrieval behavior. Each query undergoes planning, decomposition into focused subqueries, parallel retrieval from knowledge sources, semantic reranking, and results merging. The three-pronged response is optimized for agent consumption.
+A knowledge base consists of one or more [knowledge sources](agentic-knowledge-source-overview.md), an optional LLM for query planning and answer synthesis, and parameters that govern retrieval behavior. Each query undergoes planning, decomposition into focused subqueries, parallel retrieval from knowledge sources, semantic reranking, and results merging. The three-pronged response is optimized for agent consumption.
 
 Under the hood, agentic retrieval builds on the classic search architecture by adding a context layer (knowledge base) that orchestrates multi-source retrieval. Knowledge sources can be indexed or remote: indexed sources use the same indexing and query engines as classic search, while remote sources bypass indexing and are queried live.
 
-<!--
-:::image type="content" source="media/search-what-is-azure-search/azure-search-agentic-retrieval.svg" alt-text="Diagram of the Azure AI Search architecture for agentic retrieval." lightbox="media/search-what-is-azure-search/azure-search-agentic-retrieval.svg" :::
--->
+:::image type="content" source="media/search-what-is-azure-search/agentic-retrieval-architecture.png" alt-text="Diagram of the Azure AI Search architecture for agentic retrieval." lightbox="media/search-what-is-azure-search/agentic-retrieval-architecture.png" :::
 
 ## How they compare
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchに関するコンテンツの更新"
}
```

### Explanation
この変更では、「search-what-is-azure-search.md」ドキュメントに対して数件の小規模な更新が行われました。主な変更点は以下の通りです：

1. **日付の更新**: ドキュメントの日付が「12/04/2025」から「12/10/2025」へと変更されました。

2. **画像の更新**: Azure AI Searchのアーキテクチャを示す図が、「azure-search.svg」から「classic-search-architecture.png」および「agentic-retrieval-architecture.png」へと置き換えられました。これにより、視覚的なコンテンツがよりわかりやすく、また新しい情報を反映しています。

3. **テキストの明確化**: 一部の文章が、整形や表現の修正により明確さが増しています。特に、知識ベースについての説明が簡潔に整理されています。

全体として、これらの更新はAzure AI Searchの理解を促進するために、情報の正確性とアップデートを目的としています。


