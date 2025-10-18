---
date: '2025-10-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a6b6823...MicrosoftDocs:d8a47a8
summary: |-
  この記事では、Azure AI Searchにおける文書のチャンク分割方法に関する更新が報告されています。主な変更点は、著者情報と更新日、推奨チャンクサイズの増加（256トークンから512トークン）、オーバーラップ推奨設定の25%への設定、統合ベクター化に関する詳細な説明の追加、ワークフローへのチャンク分割統合に関する最新情報の提供です。

  破壊的変更はなく、既存ユーザーへの影響は最小限ですが、推奨設定の変更には留意が必要です。新たな情報は、ベクター検索の効率向上に寄与し、特にチャンクサイズとオーバーラップ推奨により文書の関連性を保持しつつ、検索の精度を高めることが期待されます。この更新により、ユーザーはAzure AI Searchをより効果的に活用することが可能となります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a6b6823...MicrosoftDocs:d8a47a8){target="_blank"}

# Highlights
この記事の更新は、Azure AI Searchにおける文書のチャンク分割方法に関するものです。主に以下のような点が更新されました：
- **著者情報と更新日**の変更。
- **推奨されるチャンクサイズ**が512トークンに増加し、**オーバーラップ推奨設定**が25%に設定。
- 統合ベクター化に関する**詳細な説明**の追加。
- ワークフローへの**チャンク分割の統合に関する最新情報**の追加。

## New features
- 統合ベクター化に関する詳細な説明が追加され、組み込みのインデクサーやスキルセットに関する依存関係が詳述された。

## Breaking changes
特段の破壊的変更は含まれず、既存のユーザーに対する大幅な影響はありませんが、推奨設定の更新には注意が必要です。

## Other updates
- 著者名が「arv100kri」から「gmndrg」に変更され、更新日が2025年3月31日から2025年10月17日に変更されました。
- テキストチャンクの推奨サイズとオーバーラップ比に関する推奨が更新されました。

# Insights
Azure AI Searchのドキュメントにおけるこの更新は、特にベクター検索を効果的に行うための文書処理方法の改善に関するものです。チャンク分割は、検索精度を高めるための重要な前処理の一つであり、この記事の修正により、より効率的な検索を可能にするための実践が明確化されています。

特に、推奨チャンクサイズが256トークンから512トークンへと変更され、オーバーラップが25%として推奨されるようになった点は、文書のトピック間の関連性維持を意識した内容です。これにより、文書全体の意味やコンテキストをよりよく捉えつつ、個別の検索クエリへの対応力を高めることが可能となります。

また、新たに統合ベクター化に関しても詳細が追加され、これがインデクサーやスキルセットとの関連でどのように機能するのかが明確に説明されています。Azure AI Searchを用いて大規模な文書を処理するビジネス上のニーズに対し、この記事の情報は非常に価値のあるものと言えるでしょう。この情報の更新により、ユーザーはより効果的にAzure AI Searchを設定し、活用することが可能となるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [vector-search-how-to-chunk-documents.md](#item-b79133) | minor update | 文書をベクター検索用にチャンク分割する方法の更新 | modified | 11 | 23 | 34 | 


# Modified Contents
## articles/search/vector-search-how-to-chunk-documents.md{#item-b79133}

<details>
<summary>Diff</summary>
````diff
@@ -2,21 +2,21 @@
 title: Chunk documents in vector search
 titleSuffix: Azure AI Search
 description: Learn strategies for chunking PDFs, HTML files, and other large documents for vectors and search indexing and query workloads.
-author: arv100kri
-ms.author: arjagann
+author: gmndrg
+ms.author: gimondra
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 03/31/2025
+ms.date: 10/17/2025
 ---
 
 # Chunk large documents for vector search solutions in Azure AI Search
 
 Partitioning large documents into smaller chunks can help you stay under the maximum token input limits of embedding models. For example, the maximum length of input text for the [Azure OpenAI](/azure/ai-services/openai/how-to/embeddings) text-embedding-ada-002 model is 8,191 tokens. Given that each token is around four characters of text for common OpenAI models, this maximum limit is equivalent to around 6,000 words of text. If you're using these models to generate embeddings, it's critical that the input text stays under the limit. Partitioning your content into chunks helps you meet embedding model requirements and prevents data loss due to truncation.
 
-We recommend [integrated vectorization](vector-search-integrated-vectorization.md) for built-in data chunking and embedding. Integrated vectorization takes a dependency on indexers and skillsets that split text and generate embeddings. If you can't use integrated vectorization, this article describes some alternative approaches for chunking your content.
+We recommend [integrated vectorization](vector-search-integrated-vectorization.md) for built-in data chunking and embedding. Integrated vectorization takes a dependency on [built-in indexers](search-indexer-overview.md) and [skillsets](cognitive-search-working-with-skillsets.md) that enable text splitting and embeddings generation. If you can't use integrated vectorization, this article describes some alternative approaches for chunking your content.
 
 ## Common chunking techniques
 
@@ -33,7 +33,9 @@ Here are some common chunking techniques, associated with built-in features if y
 
 ### Content overlap considerations
 
-When you chunk data based on fixed size, overlapping a small amount of text between chunks can help preserve context. We recommend starting with an overlap of approximately 10%. For example, given a fixed chunk size of 256 tokens, you would begin testing with an overlap of 25 tokens. The actual amount of overlap varies depending on the type of data and the specific use case, but we find that 10-15% works for many scenarios.
+When you chunk data based on fixed size, overlapping a small amount of text between chunks can help maintaining continuity and context. We recommend starting with a chunk size of 512 tokens (approximately 2,000 characters) and an initial overlap of 25%, which equals 128 tokens. This overlap ensures smoother transitions between chunks without excessive duplication.
+
+The optimal overlap may vary depending on your content type and use case. For example, highly structured data may require less overlap, while conversational or narrative text may benefit from more.
 
 ### Factors for chunking data
 
@@ -47,7 +49,7 @@ When it comes to chunking data, think about these factors:
 
 ### How chunking fits into the workflow
 
-If you have large documents, insert a chunking step into indexing and query workflows that breaks up large text. When using [integrated vectorization](vector-search-integrated-vectorization.md), a default chunking strategy using the [Text Split skill](./cognitive-search-skill-textsplit.md) is common. You can also apply a custom chunking strategy using a [custom skill](cognitive-search-custom-skill-web-api.md). Some external libraries that provide chunking include:
+If you have large documents, insert a chunking step into indexing and query workflows that breaks up large text. When using [integrated vectorization](vector-search-integrated-vectorization.md), a default chunking strategy using the [Text Split skill](./cognitive-search-skill-textsplit.md) is common. You can also apply a custom chunking strategy using a [custom skill](cognitive-search-custom-skill-web-api.md). See [this code reference](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/indexers/document-intelligence-custom-skill/document-intelligence-custom-skill.ipynb) for a semantic chunking example using a custom skill. Some external libraries that provide chunking include:
 
 + [LangChain Text Splitters](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/)
 + [Semantic Kernel TextChunker](/dotnet/api/microsoft.semantickernel.text.textchunker)
@@ -80,9 +82,9 @@ The `pages` parameter adds extra parameters:
 + `pageOverlapLength` defines how many characters from the end of the previous page are included at the start of the next page. If set, this must be less than half the maximum page length.
 + `maximumPagesToTake` defines how many pages / chunks to take from a document. The default value is 0, which means to take all pages or chunks from the document.
 
-<sup>1</sup> Characters don't align to the definition of a [token](/azure/ai-services/openai/concepts/prompt-engineering#space-efficiency). The number of tokens measured by the LLM might be different than the character size measured by the Text Split skill.
+<sup>1</sup> Characters don't align to the definition of a [token](/azure/ai-services/openai/concepts/prompt-engineering#space-efficiency). The number of tokens measured by the LLM might be different than the character size measured by the Text Split skill with the character fixed-size.
 
-<sup>2</sup> Token chunking is available in the [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) and includes extra parameters for specifying a tokenizer and any tokens that shouldn't be split up during chunking.
+<sup>2</sup> Token chunking is available in the [2025-08-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) and includes extra parameters for specifying a tokenizer and any tokens that shouldn't be split up during chunking.
 
 The following table shows how the choice of parameters affects the total chunk count from the Earth at Night e-book:
 
@@ -98,21 +100,7 @@ The following table shows how the choice of parameters affects the total chunk c
 
 Using a `textSplitMode` of `pages` results in most chunks having total character counts close to `maximumPageLength`. Chunk character count varies due to differences on where sentence boundaries fall inside the chunk. Chunk token length varies due to differences in the contents of the chunk.
 
-The following histograms show how the distribution of chunk character length compares to chunk token length for [gpt-35-turbo](/azure/ai-services/openai/how-to/chatgpt) when using a `textSplitMode` of `pages`, a `maximumPageLength` of 2000, and a `pageOverlapLength` of 500 on the Earth at Night e-book:
-
-   :::image type="content" source="./media/vector-search-how-to-chunk-documents/maximumpagelength-2000-pageoverlap-500-characters.png" alt-text="Histogram of chunk character count for maximumPageLength 2000 and pageOverlapLength 500.":::
-
-   :::image type="content" source="./media/vector-search-how-to-chunk-documents/maximumpagelength-2000-pageoverlap-500-tokens.png" alt-text="Histogram of chunk token count for maximumPageLength 2000 and pageOverlapLength 500.":::
-
-Using a `textSplitMode` of `sentences` results in a large number of chunks consisting of individual sentences. These chunks are smaller than those produced by `pages`, and the token count of the chunks more closely matches the character counts.
-
-The following histograms show how the distribution of chunk character length compares to chunk token length for [gpt-35-turbo](/azure/ai-services/openai/how-to/chatgpt) when using a `textSplitMode` of `sentences` on the Earth at Night e-book:
-
-   :::image type="content" source="./media/vector-search-how-to-chunk-documents/sentences-characters.png" alt-text="Histogram of chunk character count for sentences.":::
-
-   :::image type="content" source="./media/vector-search-how-to-chunk-documents/sentences-tokens.png" alt-text="Histogram of chunk token count for sentences.":::
-
-The optimal choice of parameters depends on how the chunks are used. For most applications, it's recommended to start with the following default parameters:
+The optimal choice of parameters depends on how the chunks are used. For most applications, it's recommended to start with the following default parameters, when using number of characters:
 
 | `textSplitMode` | `maximumPageLength` | `pageOverlapLength` |
 |-----------------|-----------------|-----------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書をベクター検索用にチャンク分割する方法の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける文書のチャンク分割に関する記事 "Chunk documents in vector search" の修正を含んでいます。主な修正点は、著者情報や更新日、推奨されるチャンクサイズとオーバーラップの設定を変更することにより、内容の明確化および最新化を図っています。

具体的には、著者名が「arv100kri」から「gmndrg」に変更され、更新日は2025年3月31日から2025年10月17日に変更されました。また、テキストチャンクの推奨サイズは512トークンに増加され、オーバーラップは初期に25%の設定が推奨されるようになり、これにより文脈の維持がよりスムーズになることを強調しています。

さらに、統合ベクター化についての説明が加えられ、組み込みのインデクサーやスキルセットに関する依存関係が詳述されています。記事では、固定サイズのデータチャンクに関する考慮事項や、チャンク分割がワークフローにどのように組み込まれるかについても最新の情報が追加されています。

総じて、これによりユーザーは、Azure AI Searchで大規模な文書を効果的に扱うための新しい実践や方法論を理解しやすくなっています。


