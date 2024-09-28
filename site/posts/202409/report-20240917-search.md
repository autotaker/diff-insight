---
date: '2024-09-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:41463e4...MicrosoftDocs:135d681
summary: この変更は、Azure AI Searchに関する複数のドキュメントを更新し、文言や内容の改善を行いました。具体的な新機能の追加はありませんが、既存のガイドラインやチュートリアルが明確化され、使いやすさが向上しています。破壊的な変更もなく、ユーザーの設定や挙動には影響を与えません。主な目的は、ユーザーの利便性と理解を向上させることであり、特にRAGソリューションに関連する文書が改善されました。更新された文書には、検索開始ガイドやインデックススキーマ、スキルセット、クエリ構築に関する詳細が含まれています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:41463e4...MicrosoftDocs:135d681){target="_blank"}

# Highlights
この変更は、Azure AI Searchのドキュメントに関連するいくつかの更新を行いました。検索開始ガイドから、RAGソリューションの構築チュートリアルまで、多岐にわたる文書の文言や内容が改善されています。

## New features
特に新しい機能の追加はありませんが、既存のガイドラインとチュートリアルの内容が明確化され、ユーザーにとって利用しやすい形に修正されました。

## Breaking changes
破壊的な変更はありません。すべての変更は既存のコンテンツを改善するものであり、現在の設定や挙動に影響を与えるものではありません。

## Other updates
以下の文書が更新されました：
1. `articles/search/search-get-started-rag.md`
2. `articles/search/tutorial-rag-build-solution-index-schema.md`
3. `articles/search/tutorial-rag-build-solution-pipeline.md`
4. `articles/search/tutorial-rag-build-solution-query.md`
5. `articles/search/tutorial-rag-build-solution.md`

# Insights
これらの更新は、主にユーザーの利便性と理解を向上させることを目的としています。

## `search-get-started-rag.md`の更新
### 目的
この変更は、ユーザーがRAG（Retrieval-Augmented Generation）を使用して検索を開始する際に発生する可能性のあるエラーメッセージに対する対応を明確にするために行われました。
### 詳細
- 「Authorization error message」を「Forbidden error message」に変更。
- 役割ベースのアクセス設定が有効であることを確認するよう促す文言を追加。
- 「authorization failed」での言及が追加され、役割の割り当てが有効になるまで待つことを指示。

これにより、ユーザーはエラーメッセージの意味を正確に把握し、行動を起こしやすくなります。

## `tutorial-rag-build-solution-index-schema.md`の更新
### 目的
インデックススキーマ構築のチュートリアルを最新の情報に基づいて更新し、より効果的なデータ構造を説明するため。
### 詳細
- 「コンテンツ中心性」というセクション名が「生成データで強化」に変わり、その内容も一部変更。
- NASA地球ブックからのデータを使用して地理名のようなエンティティを認識し、インデックスに追加する方法を説明。

これにより、構造化データを活用する利点が強調され、より良い検索結果が得られることがユーザーに伝わります。

## `tutorial-rag-build-solution-pipeline.md`の更新
### 目的
スキルセットの作成に関する説明を詳細にして、ユーザーの理解を深めるため。
### 詳細
- スキルセットの作成に関する具体的な説明が強化。
- 元のEbookを100ページごとの小さなPDFに分割することの必要性を明記。

ユーザーはスキルセットの目的を理解しやすくなり、ファイルサイズの制約に注意を払うことができます。

## `tutorial-rag-build-solution-query.md`の更新
### 目的
クエリ構築に関する説明を明確にし、フィルタの使用に関する理解を深めるため。
### 詳細
- クエリ例の引用符の修正。
- フィルタの影響とメカニズムについての詳細な説明を追加。

これにより、検索エンジンの動作とフィルタの効果をユーザーがより理解しやすくなります。

## `tutorial-rag-build-solution.md`の更新
### 目的
文言の明確化により、ユーザーにとって読みやすさと理解しやすさを向上させるため。
### 詳細
- 「alternative approaches」の文言を「for exploring alternative approaches」に変更。
- サンプルコードの説明の改善。

この更新により、ユーザーはRAGソリューションの他の方法も考慮しやすくなり、全体の文書の一貫性が維持されています

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-rag.md](#item-05ff0e) | minor update | 検索を始めるためのRAGのクイックスタートガイドの更新 | modified | 5 | 3 | 8 | 
| [tutorial-rag-build-solution-index-schema.md](#item-9a17ca) | minor update | RAGソリューションのインデックススキーマ構築チュートリアルの更新 | modified | 6 | 12 | 18 | 
| [tutorial-rag-build-solution-pipeline.md](#item-25ce01) | minor update | RAGソリューションパイプライン構築チュートリアルの更新 | modified | 3 | 1 | 4 | 
| [tutorial-rag-build-solution-query.md](#item-93965f) | minor update | RAGソリューションのクエリ構築チュートリアルの更新 | modified | 4 | 4 | 8 | 
| [tutorial-rag-build-solution.md](#item-c7eca4) | minor update | RAGソリューション構築チュートリアルの更新 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/search/search-get-started-rag.md{#item-05ff0e}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: quickstart
-ms.date: 08/18/2024
+ms.date: 09/16/2024
 ---
 
 # Quickstart: Generative search (RAG) with grounding data from Azure AI Search
@@ -262,9 +262,11 @@ This section uses Visual Studio Code and Python to call the chat completion APIs
     Several other hotels have views and water features, but do not offer beach access or views of the ocean.
     ```
 
-    If you get an authorization error message, wait a few minutes and try again. It can take several minutes for role assignments to become operational.
+    If you get a **Forbidden** error message, check Azure AI Search configuration to make sure role-based access is enabled.
 
-    To experiment further, change the query and rerun the last step to better understand how the model works with the grounding data.
+    If you get an **Authorization failed** error message, wait a few minutes and try again. It can take several minutes for role assignments to become operational.
+
+    Otherwise, to experiment further, change the query and rerun the last step to better understand how the model works with the grounding data.
 
     You can also modify the prompt to change the tone or structure of the output.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索を始めるためのRAGのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchのドキュメントにおける「検索を始めるためのRAGのクイックスタートガイド」の更新を反映しています。主な変更点は、日付の更新とエラーメッセージの文言の修正です。具体的には、以前の文中で「Authorization error message」と記載されていた部分を「Forbidden error message」に変更し、役割ベースのアクセス設定が有効であることを確認するよう促しています。また、元々の「authorization failed」エラーメッセージへの言及を追加し、役割の割り当てが有効になるまで待つことを指示する内容に修正しました。これにより、ユーザーが遭遇する可能性のあるエラーへの対応方法が明確化され、ガイドの使いやすさが向上しています。

## articles/search/tutorial-rag-build-solution-index-schema.md{#item-9a17ca}

<details>
<summary>Diff</summary>
````diff
@@ -41,17 +41,11 @@ When LLMs generate a response, they operate on chunks of content for message inp
 
 Chunks are the focus of the schema, and each chunk is the defining element of a search document in a RAG pattern. You can think of your index as a large collection of chunks, as opposed to traditional search documents that probably have more structure, such as fields containing uniform content for a name, descriptions, categories, and addresses.
 
-### Content centricity and structured data
+### Enhanced with generated data
 
-In addition to structural considerations, like chunked content, you also want to consider the substance of your content because it also informs what fields are indexed.
+In this tutorial, sample data consists of PDFs and content from the [NASA Earth Book](https://www.nasa.gov/ebooks/earth/). This content is descriptive and informative, with numerous references to geographies, countries, and areas across the world. All of the textual content is captured in chunks, but these recurring instances of place names create an opportunity for adding structure to the index. Using skills, it's possible to recognize entities in the text and capture them in an index for use in queries and filters. In this tutorial, we include an [entity recognition skill](cognitive-search-skill-entity-recognition-v3.md) that recognizes and extracts location entities, loading it into a searchable and filterable `locations` field. Adding structured content to your index gives you more options for filtering, improved relevance, and more focused answers.
 
-In this tutorial, sample data consists of PDFs and content from the NASA Earth Book. This content is descriptive and informative, with numerous references to geographies, countries, and areas across the world. To capture this information in our index and potentially use it in queries, we include skills in our indexing pipeline that recognize and extract this information, loading it into a searchable and filterable `locations` field. Adding structured content to your index gives you more options for filtering, relevance tuning, and richer answers.
-
-The original ebook is large, over 100 pages and 35 MB in size. We broke it up into smaller PDFs, one per page of text, to stay under the REST API payload limit of 16 MB per API call.
-
-For simplicity, we omit image vectorization for this exercise.
-
-### Parent-child fields in one or two indexes
+### Parent-child fields in one or two indexes?
 
 Chunked content typically derives from a larger document. And although the schema is organized around chunks, you also want to capture properties and content at the parent level. Examples of these properties might include the parent file path, title, authors, publication date, or a summary.
 
@@ -104,11 +98,11 @@ A minimal index for LLM is designed to store chunks of content. It typically inc
     }
     ```
 
-   Fields must include key field (`"id"`) and should include vector chunks for similarity search, and nonvector chunks for inputs to the LLM. 
+   Fields must include key field (`"id"` in this example) and should include vector chunks for similarity search, and nonvector chunks for inputs to the LLM. 
 
-   Vector fields have [specific types](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields) and extra attributes for embedding model dimensions and configuration. `Edm.Single` is a data type that works for commonly used LLMs. For more information about vector fields, see [Create a vector index](vector-search-how-to-create-index.md).
+   Vector fields are associated with algorithms that determine the search paths at query time. The index has a vectorSearch section for specifying multiple algorithm configurations. Vector fields also have [specific types](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields) and extra attributes for embedding model dimensions. `Edm.Single` is a data type that works for commonly used LLMs. For more information about vector fields, see [Create a vector index](vector-search-how-to-create-index.md).
 
-   Metadata fields might be file path, creation date, or content type and are useful for [filters](vector-search-filters.md).
+   Metadata fields might be the parent file path, creation date, or content type and are useful for [filters](vector-search-filters.md).
 
 1. Here's the index schema for the [tutorial source code](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Tutorial-RAG/Tutorial-rag.ipynb) and the [Earth Book content](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth_book_2019_text_pages). 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションのインデックススキーマ構築チュートリアルの更新"
}
```

### Explanation
本変更は、Azure AI Searchにおける「RAGソリューションのインデックススキーマ構築」のチュートリアルを更新したものです。主な更新内容として、「コンテンツ中心性」と題されたセクションが「生成データで強化」に改名され、その内容も一部変更されました。具体的には、NASA地球ブックからのデータを使用しており、地理名のようなエンティティを認識し、インデックスに追加する方法が説明されています。これにより、検索やフィルタリングの際に構造化されたデータを活用することで、より良い結果が得られることが強調されています。

また、インデックスのメタデータフィールドについての記述が更新され、重要なフィールドや属性についての説明が強化されました。さらに、元の内容の重複が削除され、ページ数の制限についての情報が簡素化されています。このような変更により、ユーザーにとってのチュートリアルの明確さと利便性が向上しています。

## articles/search/tutorial-rag-build-solution-pipeline.md{#item-25ce01}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ In this tutorial, you:
 > - Provide the index schema from the previous tutorial 
 > - Create a data source connection
 > - Create an indexer
-> - Create a skillset
+> - Create a skillset that chunks, vectorizes, and recognizes entities
 > - Run the indexer and check results
 
 If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
@@ -99,6 +99,8 @@ print(f"{result.name} created")
 
 In this step, set up the sample data and a connection to Azure Blob Storage. The indexer retrieves PDFs from a container. You create the container and upload files in this step.
 
+The original ebook is large, over 100 pages and 35 MB in size. We broke it up into smaller PDFs, one per page of text, to stay under the REST API payload limit of 16 MB per API call. For simplicity, we omit image vectorization for this exercise.
+
 1. Sign in to the Azure portal and find your Azure Storage account.
 
 1. Create a container and upload the PDFs from [earth_book_2019_text_pages](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth_book_2019_text_pages).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションパイプライン構築チュートリアルの更新"
}
```

### Explanation
この変更は、Azure AI Searchに関する「RAGソリューションパイプライン構築チュートリアル」における内容の更新を示しています。主な変更内容は、スキルセットの作成に関する説明が強化され、「データをチャンク化し、ベクタライズし、エンティティを認識するスキルセットを作成する」という具体的な記述が追加されました。これにより、ユーザーはスキルセットの目的と操作についてより明確に理解できるようになります。

さらに、元のEbookが100ページを超える大きなファイルであるため、各ページを小さなPDFに分割したこと、及びREST APIのペイロード制限に従っていることが明記されました。この修正によって、ユーザーにはファイルサイズの制約を意識しながら作業することの重要性が伝えられ、より効果的にチュートリアルを進める手助けとなります。

## articles/search/tutorial-rag-build-solution-query.md{#item-93965f}

<details>
<summary>Diff</summary>
````diff
@@ -119,7 +119,7 @@ print(response.choices[0].message.content)
 
 In this response, the answer is based on a single input (`top=1`) consisting of the one chunk determined by the search engine to be the most relevant. Instructions in the prompt tell the LLM to use only the information in the `sources`, or formatted search results. 
 
-Results from the first query`"how much of earth is covered by water"` should look similar to the following example.
+Results from the first query `"how much of earth is covered by water"` should look similar to the following example.
 
 :::image type="content" source="media/tutorial-rag-solution/chat-results-1.png" alt-text="Screenshot of an LLM response to a simple question using a single match from search results.":::
 
@@ -130,7 +130,7 @@ It's expected for LLMs to return different answers, even if the prompt and queri
 
 ## Add a filter
 
-Recall that you created a `locations` field using applied AI, populated with places recognized by the Entity Recognition skill. The field definition for locations includes the `filterable` attribute. Let's repeat the previous request, but this time adding a filter that selects on the term *ice* in the locations field. For more information about filtering on string collections, see [text filter fundamentals](search-filters.md#text-filter-fundamentals) and [Understand collection filters](search-query-understand-collection-filters.md).
+Recall that you created a `locations` field using applied AI, populated with places recognized by the Entity Recognition skill. The field definition for locations includes the `filterable` attribute. Let's repeat the previous request, but this time adding a filter that selects on the term *ice* in the locations field. A filter introduces inclusion or exclusion criteria. The search engine is still doing a vector search on `"how much of earth is covered by water"`, but it's now excluding matches that don't include *ice*. For more information about filtering on string collections and on vector queries, see [text filter fundamentals](search-filters.md#text-filter-fundamentals),[Understand collection filters](search-query-understand-collection-filters.md), and [Add filters to a vector query](vector-search-filters.md).
 
 Replace the search_results definition with the following example that includes a filter:
 
@@ -142,7 +142,7 @@ search_results = search_client.search(
     select="title, chunk, locations"
 ```
 
-Results from the filtered query should now look similar to the following response.
+Results from the filtered query should now look similar to the following response. Notice the emphasis on ice cover.
 
 :::image type="content" source="media/tutorial-rag-solution/chat-results-filter.png" alt-text="Screenshot of an LLM response after a filter is added.":::
 
@@ -160,7 +160,7 @@ Because the model is bound to just the grounding data, the answer becomes more e
 
 You can also change the prompt to control the format of the output, tone, and whether you want the model to supplement the answer with its own training data by changing the prompt. 
 
-Here's another example of LLM output if we refocus the prompt.
+Here's another example of LLM output if we refocus the prompt on fact collection.
 
 ```python
 # Provide instructions to the model
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションのクエリ構築チュートリアルの更新"
}
```

### Explanation
この変更は、Azure AI Searchに関する「RAGソリューションのクエリ構築チュートリアル」の内容を更新するものです。主な変更点は、クエリの結果やフィルタの使用に関する説明を明確にするための文言改善です。具体的には、最初のクエリの結果例における引用符の配置が修正され、より正確に記述されています。

さらに、フィルタを適用する際の説明が強化され、フィルタが検索結果に与える影響と、そのメカニズムについての情報が追加されています。この点では、フィルタがどのように検索エンジンの動作を変化させるか、たとえば除外基準を設けるということに言及されています。これにより、ユーザーはフィルタの効果とその適用方法について理解を深めることができるようになります。

また、フィルタを使用した後のクエリ結果に関する記述において、強調点が追加されており、ユーザーが検索結果から特定の条件を反映した応答を得られることが強調されています。このような変更は、チュートリアルの明確さと実用性を高めており、ユーザーに対してより良い体験を提供できるものとなっています。

## articles/search/tutorial-rag-build-solution.md{#item-c7eca4}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ This tutorial series demonstrates a pattern for building RAG solutions on Azure
 
 Sample data is a [collection of PDFs](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth_book_2019_text_pages) uploaded to Azure Storage.
 
-Sample code can be found in [this Python notebook](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Tutorial-RAG/Tutorial-rag.ipynb), but we recommend using this series for context, insights, and alternative approaches.
+Sample code can be found in [this Python notebook](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Tutorial-RAG/Tutorial-rag.ipynb), but we recommend using this series for context, insights, and for exploring alternative approaches.
 
 ## Exercises in this series
 
@@ -38,9 +38,9 @@ Sample code can be found in [this Python notebook](https://github.com/Azure-Samp
 
 We omitted a few aspects of a RAG pattern to reduce complexity:
 
-- No chat history and context. Chat history must be stored and managed separately from your grounding data, which means extra steps and code. This tutorial assumes atomic question and answers from the LLM.
+- No management of chat history and context. Chat history is typically stored and managed separately from your grounding data, which means extra steps and code. This tutorial assumes atomic question and answers from the LLM.
 
-- No per-user user access controls over results (what we refer to as "security trimming"). For more information and resources, start with [Security trimming](search-security-trimming-for-azure-search.md) and make sure to review the links at the end of the article.
+- No per-user user security over results (what we refer to as "security trimming"). For more information and resources, start with [Security trimming](search-security-trimming-for-azure-search.md) and make sure to review the links at the end of the article.
 
 This series covers the fundamentals of RAG solution development. Once you understand the basics, continue with accelerators and other code samples that provide more abstraction or are otherwise better suited for production environments and more complex workloads.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューション構築チュートリアルの更新"
}
```

### Explanation
この変更は、AzureにおけるRAGソリューションの構築に関するチュートリアルにおいて、いくつかの文言が修正されたことを示しています。具体的には、サンプルコードに関する説明が改訂され、探索の部分を強調するために「alternative approaches」というフレーズが「for exploring alternative approaches」と改められています。これによって、ユーザーはこのシリーズが提供する比較の価値をより強く認識できるようになります。

また、RAGパターンの複雑さを減少させるために省略した要素についての説明においても、表現が改善されています。「チャット履歴とコンテキストの管理がない」から「チャット履歴とコンテキストの管理の不足」となり、より明確にその意味を伝えています。さらに、「ユーザー毎の結果に対するセキュリティ管理」についても同様に表現が変更され、読みやすさが向上しました。

全体として、この修正は説明をより明確にし、ユーザーにとっての読みやすさを向上させることを目的としています。これにより、チュートリアルを受けるユーザーはRAGソリューションの開発における基本的な理解を深めやすくなります。


