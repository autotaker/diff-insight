---
date: '2025-12-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8007c7b...MicrosoftDocs:b290bf6
summary: |-
  この更新では、`articles/search/retrieval-augmented-generation-overview.md`ファイルに対して160行の追加と28行の削除が行われ、合計188の変更が加えられました。主に、強化生成（RAG）に関する情報が充実し、Azure AI Searchがこの技術をどのように使用しているかが詳述されています。

  新機能としては、「エージェンティックリトリーバル」手法の説明や、クエリ理解、データアクセス、応答時間に関するソリューションが紹介されています。破壊的変更は特にありませんが、情報のアップデートを反映した構成の変更が加えられています。

  また、コンテンツの準備セクションと関連トピックへのリンクが追加され、クラシックRAGアプローチとの比較が強調されています。この更新は、技術的な課題に対する解決策に焦点を当て、Azure AI Searchを利用するための具体的な手法を詳しく説明しています。特に、最新の機能を駆使して利用者が実用的な知識を得られるように設計されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8007c7b...MicrosoftDocs:b290bf6){target="_blank"}

<format>
# 注目点
この更新では、`articles/search/retrieval-augmented-generation-overview.md`ファイルに対し、160行の追加と28行の削除が行われ、合計188の変更が加えられました。この差分は、強化生成（Retrieval Augmented Generation, RAG）に関する内容を大幅に強化し、Azure AI Searchがどのようにこの技術を活用しているかを詳述するものです。

## 新機能
- Azure AI Searchによる「エージェンティックリトリーバル」手法の説明
- クエリ理解、データアクセス、応答時間など特定課題に焦点を当てたソリューションの紹介

## 破壊的変更
特に破壊的な変更は含まれていませんが、情報のアップデートに伴う構成変更が加えられています。

## その他の更新
- コンテンツの準備セクションと関連トピックへのリンクが追加
- クラシックRAGアプローチとの比較が加えられ、それぞれの利点が際立つように構成

# 洞察
この度の記事更新は、Azure AI Searchを活用した強化生成を深く理解するために必須の改善をもたらしており、特に技術的な課題に対する解決策に焦点を置いています。従来のRAGアプローチだけでなく、新たに採用された「エージェンティックリトリーバル」手法がどのように機能し、どのような利点を持つかについての詳細な説明が加わりました。

技術の進化に伴い、データアクセス、トークン制約、応答時間、安全性などの面で、より実践的で具体的なソリューションが求められています。本記事はそうしたニーズに応え、Azure AI Searchが提供する最新の機能をユーザーが最大限に活用できるよう案内しています。

新たな情報と比較のセクションを通じて、情報を採用しやすくする努力が見受けられ、特に Azure AI Searchと連携して強化生成を成功させる方法に関する理解を高めることができるでしょう。プラクティカルで実用的な知識を得ることが可能な、利用者にとって非常に有益なアップデートとなっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | 検索における強化生成の概要の更新 | modified | 160 | 28 | 188 | 


# Modified Contents
## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how generative AI and retrieval augmented generation (RAG) pa
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 12/12/2025
+ms.date: 12/15/2025
 ms.service: azure-ai-search
 ms.topic: article
 ms.custom:
@@ -16,6 +16,145 @@ ms.custom:
 
 # Retrieval-augmented Generation (RAG) in Azure AI Search
 
+Retrieval-augmented Generation (RAG) is a pattern that extends LLM capabilities by grounding responses in your proprietary content. While conceptually simple, RAG implementations face significant challenges.
+
+## The challenges of RAG
+
+| Challenge | Description |
+|-----------|-------------|
+| **Query&nbsp;understanding** | Modern users ask complex, conversational, or vague questions with assumed context. Traditional keyword search fails when queries don't match document terminology. Your information retrieval system must understand intent, not just match words. |
+| **Multi-source&nbsp;data&nbsp;access** | Enterprise content spans SharePoint, databases, blob storage, and other platforms. Creating a unified search corpus without disrupting data operations is essential. |
+| **Token&nbsp;constraints** | LLMs accept limited token inputs. Your retrieval system must return highly relevant, concise results—not exhaustive document dumps. |
+| **Response&nbsp;time&nbsp;expectations** | Users expect AI-powered answers in seconds, not minutes. The retrieval system must balance thoroughness with speed.
+| **Security&nbsp;and&nbsp;governance** | Opening private content to LLMs requires granular access control. Users and agents must only retrieve authorized content. |
+
+## How Azure AI Search meets RAG challenges
+
+Azure AI Search provides two approaches designed specifically for these RAG challenges:
+
++ **[Agentic retrieval](#modern-rag-with-agentic-retrieval) (preview)**: A complete RAG pipeline with LLM-assisted query planning, multi-source access, and structured responses optimized for agent consumption.
+
++ **[Classic RAG pattern](#classic-rag-pattern-for-azure-ai-search)**: The proven approach using hybrid search and semantic ranking, ideal for simpler requirements or when generally available (GA) features are required.
+
+The following sections explain how each approach solves specific RAG challenges.
+
+### Solving query understanding challenges
+
+**The problem:** Users ask "What's our PTO policy for remote workers hired after 2023?" but documents say "time off," "telecommute," and "recent hires."
+
+**Agentic retrieval solution:**
+
++ LLM analyzes the question and generates multiple targeted subqueries
++ Decomposes complex questions into focused searches
++ Uses conversation history to understand context
++ Parallel execution across knowledge sources
+
+**Classic RAG solution:**
+
++ Hybrid queries combine keyword and vector search for better recall
++ Semantic ranking re-scores results based on meaning, not just keywords
++ Vector similarity search matches concepts, not exact terms
+
+[Learn more about query planning](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md).
+
+### Solving multi-source data challenges
+
+**The problem:** HR policies in SharePoint, benefits in databases, company news on web pages—creating copies disrupts governance and routine data operations.
+
+**Agentic retrieval solution:**
+
++ Knowledge bases unify multiple knowledge sources
++ Direct query against remote SharePoint and Bing (no indexing needed)
++ Automatic indexing pipeline generation for Azure Blob, OneLake, ingested SharePoint content, ingested other external content
++ Single query interface and query plan across all sources
+
+**Classic RAG solution:**
+
++ Indexers pull from over 10 Azure data sources
++ Skills pipeline for chunking, vectorization, image verbalization and analysis
++ Incremental indexing keeps content fresh
++ You control what's indexed and how
+
+[Learn more about knowledge sources](agentic-knowledge-source-overview.md).
+
+### Solving token constraint challenges
+
+**The problem:** GPT-4 accepts ~128k tokens, but you have 10,000 pages of documentation. Sending everything wastes tokens and degrades quality.
+
+**Agentic retrieval solution:**
+
++ Returns a structured response with only the most relevant chunks
++ Built-in citation tracking shows provenance
++ Query activity log explains what was searched
++ Optional answer synthesis reduces token usage further
+
+**Classic RAG solution:**
+
++ Semantic ranking identifies top 50 most relevant results
++ Configurable result limits (top-k for vectors, top-n for text) and minimum thresholds
++ Scoring profiles boost critical content
++ Select statement controls which fields are returned
+
+[Learn more about relevance tuning](#maximize-relevance-and-recall).
+
+### Solving response time challenges
+
+**The problem:** Users expect answers in 3-5 seconds, but you're querying multiple sources with complex processing.
+
+**Agentic retrieval solution:**
+
++ Parallel subquery execution (not sequential)
++ Adjustable reasoning effort (minimal/low/medium)
++ Pre-built semantic ranking (no extra orchestration)
+
+**Classic RAG solution:**
+
++ Millisecond query response times
++ Single-shot queries reduce complexity
++ You control timeout and retry logic
++ Simpler architecture with fewer failure points
+
+### Solving security challenges
+
+**The problem:** Finance data should only be accessible to finance team, even when an executive asks the chatbot.
+
+**Agentic retrieval solution:**
+
++ Knowledge source-level access control
++ Inherits SharePoint permissions for queries against remote SharePoint
++ Inherits Microsoft Entra ID permission metadata for indexed content from Azure Storage
++ Filter-based security at query time for other data sources
++ Network isolation via private endpoints
+
+**Classic RAG solution:**
+
++ Document-level security trimming
++ Inherits Microsoft Entra ID permission metadata for indexed content from Azure Storage
++ Filter-based security at query time for other data sources
++ Network isolation via private endpoints
+
+[Learn more about security](search-security-overview.md).
+
+<!-- OLD INTRO #2
+Retrieval-augmented Generation (RAG) is a design pattern in AI that augments the capabilities of a pretrained large language model (LLM) by adding newer, specialized, or proprietary content to help answer questions. To get that content, you typically need an information retrieval component. Azure AI Search is an information retrieval solution that's designed to solve the challenges of RAG implementations.
+
++ The first challenge: rising expectations for reasonable answers regardless of the quality of the question. The modern query consists of complex or convoluted questions, possibly vague or incomplete, with the assumption of context from the current chat. These become the inputs to the information retrieval system, against which the system must understand so that it can find relevant matches for LLM answer formulation.
+
++ The second challenge: The search domain consists of multiple data sources and platforms. Content might be in various locations and in heterogenous content types. Solving for data extraction and access across disparate systems is a key objective for RAG workloads. You need to be able to either access each data source directly, or easily consolidate content into a search corpus without disrupting data operations.
+
++ The third challenge: LLMs are constrained by the number of token inputs they can accept. The information retrieval system must be efficient in how it provides inputs to the LLM. The response must be designed for the constraints under which LLMs operate.
+
++ The fourth challenge: Turnaround should be fast. Users expect reasoning efforts to take longer than traditional web searches, but they still want answers in seconds. 
+
++ The fifth challenge: Data security and governance. When you open up private content to information retrieval workloads, users and LLMs must only have access to authorized content.
+
+Azure AI Search can meet *all* of these challenges with the new agentic retrieval pipeline currently in preview. It's designed for the entire problem space, connecting your agent and application code to the right data at the right time, and returning the most useful content to the LLM.
+
+It can meet *most* of these challenges with the classic search engine that accepts single-shot queries against a single search index. Classic search is generally available, and it supports a hybrid search capability with semantic ranking that produces high quality responses that help LLMs deliver their best answers using your content.
+
+This article explores modern RAG and classic RAG experiences that you can get with Azure AI Search. It speaks to the challenges of RAG implementations and how Azure AI Search solves for specific problems with each RAG pattern. -->
+
+<!-- OLD INTRO #1
 Retrieval-augmented Generation (RAG) is a design pattern that augments the capabilities of a pretrained large language model (LLM) by adding newer, specialized, or proprietary content to help answer questions. 
 
 RAG implementations typically include an information retrieval component. The decision about which information retrieval system to use is critical because LLMs are constrained by the number of token inputs they can accept, so you want the grounding data to be as relevant as possible. Criteria to consider include:
@@ -30,11 +169,11 @@ RAG implementations typically include an information retrieval component. The de
 
 Azure AI Search is a [proven solution for RAG workloads](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md). It provides indexing and query capabilities that meet common criteria, with the infrastructure and security of the Azure cloud. Through code and other components, you can design a full stack RAG architecture that includes all of the elements for generative AI over your proprietary content.
 
-You can choose between two approaches for RAG workloads: new **agentic retrieval** for modern RAG (currently in preview), or the original query architecture for **classic RAG**. If you're required to use only generally available features, you should consider classic RAG.
+You can choose between two approaches for RAG workloads: new **agentic retrieval** for modern RAG (currently in preview), or the original query architecture for **classic RAG**. If you're required to use only generally available features, you should consider classic RAG. -->
 
-## Modern RAG with agentic retrieval
+### Modern RAG with agentic retrieval
 
-Azure AI Search now provides [agentic retrieval](search-what-is-azure-search.md#what-is-agentic-retrieval), a specialized pipeline designed specifically for RAG patterns. This approach uses LLMs to intelligently break down complex user queries into focused subqueries, executes them in parallel, and returns structured responses optimized for chat completion models.
+Azure AI Search is a [proven solution for RAG workloads](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md). It now provides [agentic retrieval](search-what-is-azure-search.md#what-is-agentic-retrieval), a specialized pipeline designed specifically for RAG patterns. This approach uses LLMs to intelligently break down complex user queries into focused subqueries, executes them in parallel, and returns structured responses optimized for chat completion models.
 
 Agentic retrieval represents the evolution from traditional single-query RAG patterns to multi-query intelligent retrieval, providing:
 
@@ -48,40 +187,33 @@ You need new objects for this pipeline: one or more knowledge sources, a knowled
 
 For new RAG implementations, we recommend starting with [agentic retrieval](agentic-retrieval-overview.md). For existing solutions, consider migrating to take advantage of improved accuracy and context understanding.
 
-## Classic RAG pattern for Azure AI Search
+### Classic RAG pattern for Azure AI Search
 
 Classic RAG uses the [original query execution architecture](search-what-is-azure-search.md#what-is-classic-search) where your application sends a single query to Azure AI Search and orchestrates the handoff to an LLM separately. Your deployed LLM formulates an answer using the flattened result set from the query. This approach is simpler with fewer components, and faster because there's no LLM involvement in query planning.
 
 For detailed information about implementing classic RAG, see the [azure-search-classic-rag repository](https://github.com/Azure-Samples/azure-search-classic-rag/blob/main/README.md).
 
-## Searchable content in Azure AI Search
-
-Your searchable content is the cornerstone of a RAG solution. This section takes a closer look at what constitutes searchable content in Azure AI Search.
+## Content preparation for RAG
 
-Searchable content is either a [single search index](search-what-is-an-index.md) (classic RAG) or a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) that has multiple knowledge sources backed by multiple search indexes or remote data providers. Within an index, you have plain text content and vectorized content.
+RAG quality depends on how you prepare content for retrieval. Azure AI Search supports:
 
-+ Plain text content (tokenized) is essential because it's used for LLM inputs, scoring profiles, and semantic ranking.
+| Content challenge | How Azure AI Search helps |
+|-------------------|---------------------------|
+| **Large documents** | Automatic chunking (built-in or via skills) |
+| **Multiple languages** | 50+ language analyzers for text, multilingual vectors |
+| **Images and PDFs** | OCR, image analysis, document extraction skills |
+| **Need for similarity search** | Integrated vectorization (Azure OpenAI, Azure AI Vision, custom) |
+| **Terminology mismatches** | Synonym maps, semantic ranking |
 
-+ Vectors (embeddings) provide the best accommodation for dissimilar content (multiple file formats and languages) because content is expressed universally in mathematical representations. Vectors also support similarity search: matching on the coordinates that are most similar to the vector query. Compared to keyword search (or term search) that matches on tokenized terms, similarity search is more nuanced. It's a better choice if there's ambiguity or interpretation requirements in the content or in queries. 
+**For agentic retrieval:** Use [knowledge sources](agentic-knowledge-source-overview.md) that auto-generate chunking and vectorization pipelines.
 
-But you don't have to choose between vectors and plain text, because [hybrid search](hybrid-search-overview.md) lets you combine them. You can specify hybrid queries in classic RAG. Agentic retrieval creates them automatically if your index has both content types.
+**For classic RAG:** Use [indexers and skillsets](search-indexer-overview.md) to build custom pipelines, or push pre-processed content via the [push API](search-what-is-data-import.md).
 
-Azure AI Search indexes support multiple content types optimized for RAG:
+### Maximize relevance and recall
 
-| Content type | How it's indexed | Key features |
-|--------------|------------------|--------------|
-| Plain text | Tokens, raw text | [Indexers](search-indexer-overview.md) and [knowledge sources](agentic-knowledge-source-overview.md). Also, [analyzers](search-analyzers.md) and [normalizers](search-normalizers.md) to modify text in flight. [Synonym maps](search-synonyms.md) for query expansion. |
-| Vectorized text | [Embeddings](vector-search-how-to-create-index.md) | [Chunking and vectorization](vector-search-integrated-vectorization.md) via indexers  or external tools |
-| Images | Tokens via OCR and AI | OCR and Image Analysis [skills](cognitive-search-working-with-skillsets.md) (indexer required) |
-| Multimodal | Unified embeddings | [Azure Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) or [OpenAI CLIP](https://github.com/openai/CLIP/blob/main/README.md) for unified embedding space. |
+How do you provide the best grounding data for LLM answer formulation? It's a combination of having appropriate content, smart queries, and query logic that can identify the best chunks for answering a question.
 
-For agentic retrieval, you can also access remote sources (Bing, SharePoint) without indexing.
-
-For implementation details, see [integrated vectorization](vector-search-integrated-vectorization.md) and [skillsets](cognitive-search-working-with-skillsets.md).
-
-## Maximize relevance and recall
-
-How do you provide the best grounding data for LLM answer formulation? It's a combination of having appropriate content, smart queries, and query capabilities that can identify the best chunks.
+On the content, use chunking to subdivide large documents so that portions can be matched on independently. Use vectorization to create embeddings used for vector queries.
 
 On the query side, to ensure the most relevant results for your RAG implementation:
 
@@ -121,10 +253,10 @@ There are many ways to get started, including code-first solutions and demos.
 
 ### [**Videos**](#tab/videos)
 
-+ [Build agents with knowledge, agentic RAG and Azure AI Search](https://www.youtube.com/watch?v=lW47o2ss3Yg) 
-
 + [Foundry IQ: the future of RAG with knowledge retrieval and AI Search](https://www.youtube.com/watch?v=slDdNIQCJBQ)
 
++ [Build agents with knowledge, agentic RAG and Azure AI Search](https://www.youtube.com/watch?v=lW47o2ss3Yg) 
+
 + [(Classic RAG) Vector search and state of the art retrieval for Generative AI apps](https://www.youtube.com/watch?v=lSzc1MJktAo)
 
 ### [**Docs**](#tab/docs)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索における強化生成の概要の更新"
}
```

### Explanation
このコード差分では、`articles/search/retrieval-augmented-generation-overview.md`ファイルにおける大幅な更新が行われました。追加された160行と削除された28行により、合計188の変更がありました。主な更新内容は、強化生成（RAG）的手法の説明を補強し、その課題に対するAzure AI Searchのアプローチを詳細化した点です。

具体的には、RAGの挑戦やそれに対する解決策として、クエリ理解、複数ソースのデータアクセス、トークン制約、応答時間の期待、安全性とガバナンスの問題について詳しく記述されています。また、Azure AI Searchが新たに提供する「エージェンティックリトリーバル」という最新の手法と、従来の「クラシックRAG」アプローチを比較し、それぞれの利点を強調しています。

さらに、コンテンツの準備や関連トピックへのリンクが追加され、記事全体がより充実しており、利用者がAzure AI Searchを使用して強化生成を実現する方法に関する理解を深めることができる内容となっています。


