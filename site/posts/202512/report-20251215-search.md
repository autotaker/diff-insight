---
date: '2025-12-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fa519a7...MicrosoftDocs:8007c7b
summary: この変更には、「Retrieval Augmented Generation（RAG）」に関する詳細な説明の追加が含まれており、プロプライエタリコンテンツの使用方法が明確になりました。また、用語の統一と文法的な改善により、文書の可読性も向上しました。この更新では、RAGを用いた質問応答に関する具体的な情報が追加され、既存の内容も改訂されています。古い情報や重複部分は削除され、文書全体の焦点が明確にされました。さらに、Azure
  AI Searchの最新情報も含まれ、ユーザーが最新の機能を活用できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fa519a7...MicrosoftDocs:8007c7b){target="_blank"}

<format>
# ハイライト
この変更には、新しい機能として「Retrieval Augmented Generation（RAG）」の詳細な説明の追加があります。これにより、プロプライエタリコンテンツの使用方法が明確化されました。統一された用語と改良された構文により、文書の全体的な可読性が向上しています。

## 新機能
- プロプライエタリ企業のコンテンツを使用した質問応答方法に関する詳細情報の追加。
- RAGの実装をサポートする具体的なリソースとドキュメントへのリンク。

## 破壊的変更
特に破壊的変更はありませんが、古い情報や冗長な部分が削除され、情報の焦点が絞られました。

## その他の更新
- RAGと関連するアプローチの説明が改定され、情報検索システムの重要度についての記述が追加。
- 統一された用語と、文法的に最適化された表現。

# 説明
この更新は、`retrieval-augmented-generation-overview.md` ドキュメントにおける重要な情報の追加と、既存の内容の改訂を中心に行われました。ユーザーにとって、最も重要なのは「Retrieval Augmented Generation（RAG）」の役割とその実用性をより深く理解できるようになったことです。

RAGは、特定データセットを使用してより効果的に質問に応答する新しいアプローチとして、多くのアプリケーションで注目されています。この更新では、プロプライエタリなデータを用いたアプローチについての詳細が追加され、エンドユーザーがどのようにデータから意味のある情報を引き出し、それを元にした応答を生成するかについての具体的なガイドラインが示されています。

また、古くなった情報や不必要な重複を削除することで、ドキュメント全体の焦点が明確になり、特定のアプローチ（エージェントによる取得、従来のRAGアプローチ）の理解が向上しました。これは、ユーザーが自らのプロジェクトにRAGを安全かつ効率的に実装するための道筋を提供することを目的としています。

さらに、Azure AI Searchの最新情報が含まれることで、ユーザーが最新の機能を活用し、情報検索システムが出力に与える影響を理解するのに役立ちます。これらの修正は、本ドキュメントを使用するユーザーに対して、より包括的かつ実践的な情報を提供しようとする意図を示しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | 検索機能の概要に関する文書の更新 | modified | 63 | 117 | 180 | 


# Modified Contents
## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how generative AI and retrieval augmented generation (RAG) pa
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 12/10/2025
+ms.date: 12/12/2025
 ms.service: azure-ai-search
 ms.topic: article
 ms.custom:
@@ -14,30 +14,27 @@ ms.custom:
   - build-2025
 ---
 
-# Retrieval Augmented Generation (RAG) in Azure AI Search
+# Retrieval-augmented Generation (RAG) in Azure AI Search
 
-Retrieval Augmented Generation (RAG) is a design pattern that augments the capabilities of a chat completion model like ChatGPT by adding an information retrieval step, incorporating your proprietary enterprise content for answer formulation. For an enterprise solution, it's possible to fully constrain generative AI to your enterprise content.
+Retrieval-augmented Generation (RAG) is a design pattern that augments the capabilities of a pretrained large language model (LLM) by adding newer, specialized, or proprietary content to help answer questions. 
 
-The decision about which information retrieval system to use is critical because it determines the inputs to the LLM. The information retrieval system should provide:
+RAG implementations typically include an information retrieval component. The decision about which information retrieval system to use is critical because LLMs are constrained by the number of token inputs they can accept, so you want the grounding data to be as relevant as possible. Criteria to consider include:
 
-+ Indexing strategies that load and refresh at scale, for all of your content, at the frequency you require.
++ Ability to pull from a broad range of data sources and platforms.
 
-+ Query capabilities and relevance tuning. The system should return *relevant* results, in the short-form formats necessary for meeting the token length requirements of large language model (LLM) inputs. Query turnaround should be as fast as possible.
++ Query capabilities that can target all of your data and return synthesized and highly relevant results, in the short-form formats necessary for meeting the token length requirements of LLM inputs.
 
-+ Security, global reach, and reliability for both data and operations.
++ Ease of integration with agents and chat apps, and other models and processes that are part of your application.
 
-+ Integration with embedding models for indexing, and chat models or language understanding models for retrieval.
++ Built-in content preparation (chunking, vectorization, image verbalization). It's common to consolidate searchable data into separate physical data structures that are optimized for search. You can verbalize, recognize, or analyze images to get text-equivalent information into your index. More likely, you might want to chunk verbose source content so that it can be easily consumed, and vectorize that content if you want similarity search.
 
-Azure AI Search is a [proven solution for information retrieval](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md) in a RAG architecture. It provides indexing and query capabilities, with the infrastructure and security of the Azure cloud. Through code and other components, you can design a comprehensive RAG solution that includes all of the elements for generative AI over your proprietary content.
+Azure AI Search is a [proven solution for RAG workloads](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md). It provides indexing and query capabilities that meet common criteria, with the infrastructure and security of the Azure cloud. Through code and other components, you can design a full stack RAG architecture that includes all of the elements for generative AI over your proprietary content.
 
-You can choose between two approaches for RAG workloads: agentic retrieval, or the original query architecture for classic RAG.
-
-> [!NOTE]
-> New to copilot and RAG concepts? Watch [Vector search and state of the art retrieval for Generative AI apps](https://www.youtube.com/watch?v=lSzc1MJktAo).
+You can choose between two approaches for RAG workloads: new **agentic retrieval** for modern RAG (currently in preview), or the original query architecture for **classic RAG**. If you're required to use only generally available features, you should consider classic RAG.
 
 ## Modern RAG with agentic retrieval
 
-Azure AI Search now provides **agentic retrieval**, a specialized pipeline designed specifically for RAG patterns. This approach uses large language models to intelligently break down complex user queries into focused subqueries, executes them in parallel, and returns structured responses optimized for chat completion models.
+Azure AI Search now provides [agentic retrieval](search-what-is-azure-search.md#what-is-agentic-retrieval), a specialized pipeline designed specifically for RAG patterns. This approach uses LLMs to intelligently break down complex user queries into focused subqueries, executes them in parallel, and returns structured responses optimized for chat completion models.
 
 Agentic retrieval represents the evolution from traditional single-query RAG patterns to multi-query intelligent retrieval, providing:
 
@@ -53,121 +50,92 @@ For new RAG implementations, we recommend starting with [agentic retrieval](agen
 
 ## Classic RAG pattern for Azure AI Search
 
-A RAG solution can be implemented on Azure AI Search using the original query execution architecture. With this approach, your application sends a single query request to Azure AI Search, the search engine processes the request, and returns search results to the caller. There's no side trip to an LLM for query planning or answer formulation. There's no query execution details in the response, and citations are built into the response only if you have fields in your index that provide a parent document name or page. This approach is faster and simpler with fewer components. Depending on your application requirements, it could be the best choice. 
-
-A high-level summary of classic RAG pattern built on Azure AI Search looks like this:
-
-+ Start with a user question or request (prompt).
-+ Send it as a query request to Azure AI Search to find relevant information.
-+ Return the top-ranked search results to an LLM.
-+ Use the natural language understanding and reasoning capabilities of the LLM to generate a response to the initial prompt.
-
-Azure AI Search provides inputs to the LLM prompt, but doesn't train the model. In a traditional RAG pattern, there's no extra training. The LLM is pretrained using public data, but it generates responses that are augmented by information from the retriever, in this case, Azure AI Search.
-
-RAG patterns that include Azure AI Search have the elements indicated in the following illustration.
-
-:::image type="content" source="media/retrieval-augmented-generation-overview/architecture-diagram.png" alt-text="Architecture diagram of information retrieval with search and ChatGPT." border="true" lightbox="media/retrieval-augmented-generation-overview/architecture-diagram.png":::
-
-+ App UX (web app) for the user experience
-+ App server or orchestrator (integration and coordination layer)
-+ Azure AI Search (information retrieval system)
-+ Azure OpenAI (LLM for generative AI)
-
-The web app provides the user experience, providing the presentation, context, and user interaction. Questions or prompts from a user start here. Inputs pass through the integration layer, going first to information retrieval to get the search results, but also go to the LLM to set the context and intent. 
+Classic RAG uses the [original query execution architecture](search-what-is-azure-search.md#what-is-classic-search) where your application sends a single query to Azure AI Search and orchestrates the handoff to an LLM separately. Your deployed LLM formulates an answer using the flattened result set from the query. This approach is simpler with fewer components, and faster because there's no LLM involvement in query planning.
 
-The app server or orchestrator is the integration code that coordinates the handoffs between information retrieval and the LLM. Common solutions include [Azure Semantic Kernel](/semantic-kernel/get-started/quick-start-guide) or [LangChain](https://python.langchain.com/docs/introduction/) to coordinate the workflow. [LangChain integrates with Azure AI Search](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/), making it easier to include Azure AI Search as a [retriever](https://python.langchain.com/docs/how_to/#retrievers) in your workflow. [LlamaIndex](https://github.com/run-llama/llama_index/tree/main/llama-index-integrations/vector_stores/llama-index-vector-stores-azureaisearch) and [Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/announcing-semantic-kernel-integration-with-azure-cognitive-search/) are other options.
-
-The information retrieval system provides the searchable index, query logic, and the payload (query response). The search index can contain vectors or nonvector content. Although most samples and demos include vector fields, it's not a requirement. The query is executed using the existing search engine in Azure AI Search, which can handle keyword (or term) and vector queries. The index is created in advance, based on a schema you define, and loaded with your content that's sourced from files, databases, or storage.
-
-The LLM receives the original prompt, plus the results from Azure AI Search. The LLM analyzes the results and formulates a response. If the LLM is ChatGPT, the user interaction might consist of multiple conversation turns. An Azure solution most likely uses Azure OpenAI, but there's no hard dependency on this specific service.
+For detailed information about implementing classic RAG, see the [azure-search-classic-rag repository](https://github.com/Azure-Samples/azure-search-classic-rag/blob/main/README.md).
 
 ## Searchable content in Azure AI Search
 
-In Azure AI Search, all searchable content is stored in a search index that's hosted on your search service. A search index is designed for fast queries with millisecond response times, so its internal data structures exist to support that objective. To that end, a search index stores *indexed content*, and not whole content files like entire PDFs or images. Internally, the data structures include inverted indexes of [tokenized text](https://lucene.apache.org/core/7_5_0/test-framework/org/apache/lucene/analysis/Token.html), vector indexes for embeddings, and unaltered plain text for cases where verbatim matching is required (for example, in filters, fuzzy search, regular expression queries).
-
-When you set up the data for your RAG solution, you use the features that create and load an index in Azure AI Search. An index includes fields that duplicate or represent your source content. An index field might be simple transference (a title or description in a source document becomes a title or description in a search index), or a field might contain the output of an external process, such as vectorization or skill processing that generates a representation or text description of an image.
-
-Since you probably know what kind of content you want to search over, consider the indexing features that are applicable to each content type:
-
-| Content type | Indexed as | Features |
-|--------------|------------|----------|
-| text | tokens, unaltered text | [Indexers](search-indexer-overview.md) can pull plain text from other Azure resources like Azure Storage and Cosmos DB. You can also [push any JSON content](search-what-is-data-import.md) to an index. To modify text in flight, use [analyzers](search-analyzers.md) and [normalizers](search-normalizers.md) to add lexical processing during indexing. [Synonym maps](search-synonyms.md) are useful if source documents are missing terminology that might be used in a query. |
-| text | vectors <sup>1</sup> | Text can be chunked and vectorized in an indexer pipeline, or handled externally and then [indexed as vector fields](vector-search-how-to-create-index.md) in your index. |
-| image | tokens, unaltered text <sup>2</sup> | [Skills](cognitive-search-working-with-skillsets.md) for OCR and Image Analysis can process images for text recognition or image characteristics. Skills have an indexer requirement. |
-| image | vectors <sup>1</sup> | Images can be vectorized in an indexer pipeline, or handled externally for a mathematical representation of image content and then [indexed as vector fields](vector-search-how-to-create-index.md) in your index. You can use [Azure Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) or an open source model like [OpenAI CLIP](https://github.com/openai/CLIP/blob/main/README.md) to vectorize text and images in the same embedding space.|
+Your searchable content is the cornerstone of a RAG solution. This section takes a closer look at what constitutes searchable content in Azure AI Search.
 
- <sup>1</sup> Azure AI Search provides [integrated data chunking and vectorization](vector-search-integrated-vectorization.md), but you must take a dependency on indexers and skillsets. If you can't use an indexer, Microsoft's [Semantic Kernel](/semantic-kernel/overview/) or other community offerings can help you with a full stack solution. For code samples showing both approaches, see [azure-search-vectors-sample repo](https://github.com/Azure/azure-search-vector-samples).
+Searchable content is either a [single search index](search-what-is-an-index.md) (classic RAG) or a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) that has multiple knowledge sources backed by multiple search indexes or remote data providers. Within an index, you have plain text content and vectorized content.
 
-<sup>2</sup> Image descriptions are converted to searchable text and added to the index. The images themselves are not stored in the index. [Skills](cognitive-search-working-with-skillsets.md) are built-in support for [applied AI](cognitive-search-concept-intro.md). For image descriptions and verbalizations, the indexing pipeline makes an internal call to the Azure OpenAI or Azure Vision. These skills pass an extracted image for processing, and receive the output as text that's indexed by Azure AI Search. Skills are also used for integrated data chunking and embedding. 
++ Plain text content (tokenized) is essential because it's used for LLM inputs, scoring profiles, and semantic ranking.
 
-Vectors provide the best accommodation for dissimilar content (multiple file formats and languages) because content is expressed universally in mathematic representations. Vectors also support similarity search: matching on the coordinates that are most similar to the vector query. Compared to keyword search (or term search) that matches on tokenized terms, similarity search is more nuanced. It's a better choice if there's ambiguity or interpretation requirements in the content or in queries.
++ Vectors (embeddings) provide the best accommodation for dissimilar content (multiple file formats and languages) because content is expressed universally in mathematical representations. Vectors also support similarity search: matching on the coordinates that are most similar to the vector query. Compared to keyword search (or term search) that matches on tokenized terms, similarity search is more nuanced. It's a better choice if there's ambiguity or interpretation requirements in the content or in queries. 
 
-## Content retrieval in Azure AI Search
+But you don't have to choose between vectors and plain text, because [hybrid search](hybrid-search-overview.md) lets you combine them. You can specify hybrid queries in classic RAG. Agentic retrieval creates them automatically if your index has both content types.
 
-Once your data is in a search index, you use the query capabilities of Azure AI Search to retrieve content. 
+Azure AI Search indexes support multiple content types optimized for RAG:
 
-In a non-RAG pattern, queries make a round trip from a search client. The query is submitted, it executes on a search engine, and the response returned to the client application. The response, or search results, consist exclusively of the verbatim content found in your index. 
+| Content type | How it's indexed | Key features |
+|--------------|------------------|--------------|
+| Plain text | Tokens, raw text | [Indexers](search-indexer-overview.md) and [knowledge sources](agentic-knowledge-source-overview.md). Also, [analyzers](search-analyzers.md) and [normalizers](search-normalizers.md) to modify text in flight. [Synonym maps](search-synonyms.md) for query expansion. |
+| Vectorized text | [Embeddings](vector-search-how-to-create-index.md) | [Chunking and vectorization](vector-search-integrated-vectorization.md) via indexers  or external tools |
+| Images | Tokens via OCR and AI | OCR and Image Analysis [skills](cognitive-search-working-with-skillsets.md) (indexer required) |
+| Multimodal | Unified embeddings | [Azure Vision multimodal](/azure/ai-services/computer-vision/how-to/image-retrieval) or [OpenAI CLIP](https://github.com/openai/CLIP/blob/main/README.md) for unified embedding space. |
 
-In a classic RAG pattern, queries and responses are coordinated between the search engine and the LLM. A user's question or query is forwarded to both the search engine and to the LLM as a prompt. The search results come back from the search engine and are redirected to an LLM. The response that makes it back to the user is generative AI, either a summation or answer from the LLM.
+For agentic retrieval, you can also access remote sources (Bing, SharePoint) without indexing.
 
-In a modern agentic retrieval RAG pattern, queries and responses integrate with LLMs for help with query planning and optional answer formulation. Query inputs can be richer, with chat history as well as the user's question. The LLM determines how to set up subqueries for the best coverage over your indexed content. The response includes not just search results, but the query execution details and source documents. You can optionally include answer formulation, which in other patterns occurs outside of the query pipeline.
+For implementation details, see [integrated vectorization](vector-search-integrated-vectorization.md) and [skillsets](cognitive-search-working-with-skillsets.md).
 
-Here are the capabilities in Azure AI Search that are used to formulate queries:
+## Maximize relevance and recall
 
-| Query feature | Purpose | Why use it |
-|---------------|---------|------------|
-| [Agentic search (preview)](agentic-retrieval-how-to-create-knowledge-base.md) | Parallel query execution pipeline of multiple subqueries, returning a response designed for RAG workloads and agent consumer. Queries can be vector or keyword search. Semantic ranking ensures the best results of subquery are included in the final response structure. **This is the recommended approach for RAG patterns based on Azure AI Search**. |
-| [Keyword search](search-query-create.md) | Query execution over text and nonvector numeric content | Full text search is best for exact matches, rather than similar matches. Full text search queries are ranked using the [BM25 algorithm](index-similarity-and-scoring.md) and support relevance tuning through scoring profiles. It also supports filters and facets. |
-  [Vector search](vector-search-how-to-query.md) | Query execution over vector fields for similarity search, where the query string is one or more vectors. | Vectors can represent all types of content, in any language. |
-| [Hybrid search](hybrid-search-how-to-query.md) | Combines any or all of the above query techniques. Vector and nonvector queries execute in parallel and are returned in a unified result set. | The most significant gains in precision and recall are through hybrid queries. |
-| [Filters](search-filters.md) and [facets](search-faceted-navigation.md) | Applies to text or numeric (nonvector) fields only. Reduces the search surface area based on inclusion or exclusion criteria. | Adds precision to your queries. |
+How do you provide the best grounding data for LLM answer formulation? It's a combination of having appropriate content, smart queries, and query capabilities that can identify the best chunks.
 
-### Structure the query response
+On the query side, to ensure the most relevant results for your RAG implementation:
 
-A query's response provides the input to the LLM, so the quality of your search results is critical to success. Results are a tabular row set. The composition or structure of the results depends on:
++ [Use hybrid queries](hybrid-search-overview.md) that combine keyword (nonvector) and vector search for maximum recall. In a hybrid query, if you double down on the same input, a text string and its vector equivalent generate parallel queries for keywords and similarity search, returning the most relevant matches from each query type in a unified result set.
 
-+ Fields that determine which parts of the index are included in the response.
-+ Rows that represent a match from index.
++ [Use semantic ranking](semantic-ranking.md), built into agentic retrieval, optional for classic RAG.
 
-Fields appear in search results when the attribute is "retrievable". A field definition in the index schema has attributes, and those determine whether a field is used in a response. Only "retrievable" fields are returned in full text or vector query results. By default all "retrievable" fields are returned, but you can use "select" to specify a subset. Besides "retrievable", there are no restrictions on the field. Fields can be of any length or type. Regarding length, there's no maximum field length limit in Azure AI Search, but there are limits on the [size of an API request](search-limits-quotas-capacity.md#api-request-limits).
++ [Apply scoring profiles](index-add-scoring-profiles.md) to boost specific fields or criteria.
 
-Rows are matches to the query, ranked by relevance, similarity, or both. By default, results are capped at the top 50 matches for full text search or k-nearest-neighbor matches for vector search. You can change the defaults to increase or decrease the limit up to the maximum of 1,000 documents. You can also use top and skip paging parameters to retrieve results as a series of paged results.
++ Fine-tune with vector query parameters for [vector weighting](vector-search-how-to-query.md#vector-weighting) and [minimum thresholds](vector-search-how-to-query.md#set-thresholds-to-exclude-low-scoring-results-preview).
 
-### Maximize relevance and recall
+Learn more about [hybrid search](hybrid-search-overview.md) and [semantic ranking](semantic-ranking.md).
 
-When you're working with complex processes, a large amount of data, and expectations for millisecond responses, it's critical that each step adds value and improves the quality of the end result. On the information retrieval side, *relevance tuning* is an activity that improves the quality of the results sent to the LLM. Only the most relevant or the most similar matching documents should be included in results.
+## Choose between agentic retrieval and classic RAG
 
-Here are some tips for maximizing relevance and recall:
+**Use agentic retrieval when:**
 
-+ [Hybrid queries](hybrid-search-how-to-query.md) that combine keyword (nonvector) search and vector search give you maximum recall when the inputs are the same. In a hybrid query, if you double down on the same input, a text string and its vector equivalent generate parallel queries for keywords and similarity search, returning the most relevant matches from each query type in a unified result set.
++ You need the highest possible relevance and accuracy
++ Your queries are complex or conversational
++ You want structured responses with citations and query details
++ You're building new RAG implementations
 
-+ Hybrid queries can also be expansive. You can run similarity search over verbose chunked content, and keyword search over names, all in the same request.
+**Use classic RAG when:**
 
-+ Relevance tuning is supported through:
++ You need generally available (GA) features only
++ Simplicity and speed are priorities over advanced relevance
++ You have existing orchestration code you want to preserve
++ You need fine-grained control over the query pipeline
 
-  + [Scoring profiles](index-add-scoring-profiles.md) that boost the search score if matches are found in a specific search field or on other criteria.
+A RAG solution that includes agents and Azure AI Search can benefit from [Foundry IQ](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-iq-unlocking-ubiquitous-knowledge-for-agents/4470812), as an agent's single endpoint to a knowledge layer that provides grounding data. Foundry IQ uses agentic retrieval.
 
-  + [Semantic ranker](semantic-ranking.md) that re-ranks an initial results set, using semantic models from Bing to reorder results for a better semantic fit to the original query.
+Learn more about [classic search](search-what-is-azure-search.md#what-is-classic-search), [agentic retrieval](search-what-is-azure-search.md#what-is-agentic-retrieval), and [how they compare](search-what-is-azure-search.md#how-they-compare).
 
-  + Query parameters for fine-tuning. You can [boost the importance of vector queries](vector-search-how-to-query.md#vector-weighting) or [adjust the amount of BM25-ranked results](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) in a hybrid query response. You can also [set minimum thresholds to exclude low scoring results](vector-search-how-to-query.md#set-thresholds-to-exclude-low-scoring-results-preview) from a vector query.
+## How to get started
 
-In comparison and benchmark testing, hybrid queries with text and vector fields, supplemented with semantic ranking, produce the most relevant results.
+There are many ways to get started, including code-first solutions and demos.
 
-## Integration code and LLMs
+### [**Videos**](#tab/videos)
 
-A RAG solution that includes Azure AI Search can leverage [built-in data chunking and vectorization capabilities](vector-search-integrated-vectorization.md), or you can build your own using platforms like Semantic Kernel, LangChain, or LlamaIndex.
++ [Build agents with knowledge, agentic RAG and Azure AI Search](https://www.youtube.com/watch?v=lW47o2ss3Yg) 
 
-We recommend the [Azure OpenAI demo](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md) for an example of a full stack RAG chat app with Azure OpenAI and Azure AI Search.
++ [Foundry IQ: the future of RAG with knowledge retrieval and AI Search](https://www.youtube.com/watch?v=slDdNIQCJBQ)
 
-## How to get started
-
-There are many ways to get started, including code-first solutions and demos.
++ [(Classic RAG) Vector search and state of the art retrieval for Generative AI apps](https://www.youtube.com/watch?v=lSzc1MJktAo)
 
 ### [**Docs**](#tab/docs)
 
++ [Retrieval augmented generation and indexes (Foundry)](/azure/ai-foundry/concepts/retrieval-augmented-generation)
+
 + [Try this agentic retrieval quickstart](search-get-started-agentic-retrieval.md) to walk through the new and recommended approach for RAG.
 
-+ [Try this tutorial](agentic-retrieval-how-to-create-pipeline.md) for a more comprehensive approach that includes an agent.
++ [Try this agentic retrieval tutorial](agentic-retrieval-how-to-create-pipeline.md) for a more comprehensive approach that includes an agent.
+
++ Interested in classic RAG? The [azure-search-classic-rag](https://github.com/Azure-Samples/azure-search-classic-rag/blob/main/README.md) repository has quickstarts and a tutorial.
 
 + [Review indexing concepts and strategies](search-what-is-an-index.md) to determine how you want to ingest and refresh data. Decide whether to use vector search, keyword search, or hybrid search. The kind of content you need to search over, and the type of queries you want to run, determines index design.
 
@@ -176,16 +144,14 @@ There are many ways to get started, including code-first solutions and demos.
 > [!NOTE]
 > Some Azure AI Search features are intended for human interaction and aren't useful in a RAG pattern. Specifically, you can skip features like autocomplete and suggestions. Other features like facets and orderby might be useful, but would be uncommon in a RAG scenario.
 
-### [**Demos and code**](#tab/demos)
+### [**Code**](#tab/demos)
 
-Check out the following GitHub repositories for code, documentation, and video demonstrations where applicable.
++ [RAG chat app with Azure OpenAI and Azure AI Search (Python)](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md), updated for agentic retrieval.
 
-+ [RAG chat app with Azure OpenAI and Azure AI Search (Python)](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md)
++ [azure-search-classic-rag](https://github.com/Azure-Samples/azure-search-classic-rag/blob/main/README.md) in REST, Python, Java, .NET, JavaScript, and TypeScript.
 
 + [Classic RAG Time Journeys](https://github.com/microsoft/rag-time)
 
-+ [azure-search-classic-rag](https://github.com/Azure-Samples/azure-search-classic-rag/blob/main/README.md)
-
 + [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples)
 
 ### [**Templates**](#tab/templates)
@@ -197,24 +163,4 @@ Check out the following GitHub repositories for code, documentation, and video d
 + [JavaScript](https://aka.ms/azai/js)
 + [Java](https://aka.ms/azai/javat)
 
-### [**Accelerators**](#tab/accelerators)
-
-+ [Chat with your data solution accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator)
-
-+ [Conversational Knowledge Mining solution accelerator](https://github.com/microsoft/Customer-Service-Conversational-Insights-with-Azure-OpenAI-Services)
-
-+ [Document Knowledge Mining accelerator](https://github.com/microsoft/Document-Knowledge-Mining-Solution-Accelerator)
-
-+ [Build your own copilot solution accelerator](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator)
-
-  + [Client Advisor](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator)
-
-  + [Research Assistant](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator)
-
-  + [Generic copilot](https://github.com/microsoft/Generic-Build-your-own-copilot-Solution-Accelerator)
-
----
-
-## See also
-
-+ [Retrieval augmented generation and indexes (Foundry)](/azure/ai-foundry/concepts/retrieval-augmented-generation)
+---
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索機能の概要に関する文書の更新"
}
```

### Explanation
この変更では、`retrieval-augmented-generation-overview.md` のドキュメントが更新されています。主な変更点として、テキストの改訂と特定のトピックへの言及が含まれます。具体的には、「Retrieval Augmented Generation（RAG）」の説明が更新され、プロプライエタリな企業のコンテンツを使用して質問に回答する方法についての詳しい情報が追加されました。また、「RAG」の用語の統一が行われ、文中における構文の改善がなされています。

ドキュメント内の情報検索システムの重要性についての記述がされ、選択基準としての「情報検索システム」がどのように出力に影響を与えるかが強調されました。この更新は、Azure AI Searchとそれに関連する機能に関する最新の情報を提供し、利用者に対してより明確な指針を示すことを目的としています。

変更には63行の追加と117行の削除が含まれ、全体で180行の変更が行われています。この更新により、具体的な機能やアプローチ（例えば、エージェントによる取得や従来のRAGアプローチ）に関する理解が深まります。さらに、ユーザーがRAGの実装を開始するための具体的なリソースとドキュメントへのリンクも追加されています。


