---
date: '2024-10-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7d913a4...MicrosoftDocs:1b56c27
summary: 今回のコード変更では、新機能の追加と既存チュートリアルの大幅な更新が行われ、特にRAG（Retrieval-Augmented Generation）ソリューション構築のためのサポートが強化されています。新たに「Maximize
  relevance」というチュートリアルが追加され、関連性を最大化する方法が詳しく説明されています。破壊的な変更はないものの、モデルの変更やタイトルの統一などが含まれており、後方互換性は維持されています。他にも、文書の明確化や最新技術に合わせたモデルの更新が行われ、全体的な精度と使いやすさが向上しました。特に、新しいチュートリアルの追加により、ユーザーは検索結果の精度向上に向けた具体的な手法を学ぶことができ、質の高い検索エクスペリエンスの提供が期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7d913a4...MicrosoftDocs:1b56c27){target="_blank"}

# Highlights
今回のコード変更には、新機能追加や既存チュートリアルの大幅な更新が含まれており、主にRAG（Retrieval-Augmented Generation）ソリューションを構築するためのサポート内容が強化されています。特に新たに追加されたチュートリアルがある一方、既存のファイルも日々の進化に応じて内容が改善されています。

## New features
- 新しいチュートリアル「Maximize relevance」が追加され、関連性を最大化する解説がなされています。このチュートリアルにより、ユーザーは実際に検索結果の精度向上方法を学ぶことができます。

## Breaking changes
特記すべき破壊的変更はありません。ただし、使用するモデルの変更やタイトルの統一など、後方互換性を損なわない程度の変更が含まれています。

## Other updates
- 記述内容の明確化、最新の技術に合わせたモデルの更新、効率化および効果的な検索を目的としたクエリ例やフィルタリング手法の改善が行われました。
- 多くのドキュメントで日付や文言の修正が行われ、ドキュメント全体の精度向上と使いやすさが改善されています。

# Insights
このコード変更は、主にAzure AI SearchとRAGソリューションの統合をより効果的にサポートすることを意図しています。特に、関連性を最大化する新しいチュートリアルの追加は、ユーザーが検索結果の精度を向上させるための具体的な手法を習得するのに役立ちます。これにより、ソリューションの構築者はより高品質な検索エクスペリエンスを提供できるでしょう。

また、細部にわたる更新が行われた既存のチュートリアル群では、使用モデルが最新のものにアップデートされ、技術的負債を減らすための措置が講じられています。例えば、埋め込みモデルやGPTモデルの新バージョンへのアップデートは、性能および応答品質の向上に寄与することでしょう。さらに、不要な説明を削除することで読みやすさが向上し、ユーザーが必要な情報に迅速にアクセスできるようになっています。

記事の更新は単なる情報の修正に留まらず、ユーザーが確実に最新の手法を実行できるためのノウハウを提供する観点から、文書の整合性や明確性を向上させるための重要な役割を担っていると言えます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [toc.yml](#item-c4768f) | minor update | 目次の更新: 重要な関連性を最大化するチュートリアルを追加 | modified | 2 | 0 | 2 | 
| [tutorial-rag-build-solution-index-schema.md](#item-9a17ca) | minor update | RAGチュートリアルの詳細更新 | modified | 9 | 9 | 18 | 
| [tutorial-rag-build-solution-maximize-relevance.md](#item-2fdb09) | new feature | RAGチュートリアル: 関連性を最大化する方法 | added | 317 | 0 | 317 | 
| [tutorial-rag-build-solution-models.md](#item-6796c9) | minor update | RAGソリューションモデルに関するドキュメントの更新 | modified | 17 | 12 | 29 | 
| [tutorial-rag-build-solution-pipeline.md](#item-25ce01) | minor update | RAGチュートリアルにおけるインデクシングパイプラインの更新 | modified | 34 | 37 | 71 | 
| [tutorial-rag-build-solution-query.md](#item-93965f) | minor update | RAGチュートリアルにおけるLLMを使用した検索の更新 | modified | 86 | 35 | 121 | 
| [tutorial-rag-build-solution.md](#item-c7eca4) | minor update | RAGソリューション構築チュートリアルの更新 | modified | 7 | 7 | 14 | 


# Modified Contents
## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -104,6 +104,8 @@ items:
       href: tutorial-rag-build-solution-pipeline.md
     - name: Search and generate answers
       href: tutorial-rag-build-solution-query.md
+    - name: Maximize relevance
+      href: tutorial-rag-build-solution-maximize-relevance.md
   - name: Skills tutorials
     items:
     - name: C#
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新: 重要な関連性を最大化するチュートリアルを追加"
}
```

### Explanation
この変更では、`articles/search/toc.yml`ファイルに2つの追加が行われました。具体的には、新しい項目「Maximize relevance」が追加され、そのリンクは「tutorial-rag-build-solution-maximize-relevance.md」に設定されています。この更新により、ユーザーは関連性を最大化するためのチュートリアルにアクセスできるようになります。全体として、目次が更新され、より充実した情報が提供されることとなります。

## articles/search/tutorial-rag-build-solution-index-schema.md{#item-9a17ca}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'RAG Tutorial: Design an index'
+title: 'RAG tutorial: Design an index'
 titleSuffix: Azure AI Search
 description: Design an index for RAG patterns in Azure AI Search.
 
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: tutorial
-ms.date: 10/01/2024
+ms.date: 10/04/2024
 
 ---
 
@@ -43,7 +43,7 @@ Chunks are the focus of the schema, and each chunk is the defining element of a
 
 ### Enhanced with generated data
 
-In this tutorial, sample data consists of PDFs and content from the [NASA Earth Book](https://www.nasa.gov/ebooks/earth/). This content is descriptive and informative, with numerous references to geographies, countries, and areas across the world. All of the textual content is captured in chunks, but these recurring instances of place names create an opportunity for adding structure to the index. Using skills, it's possible to recognize entities in the text and capture them in an index for use in queries and filters. In this tutorial, we include an [entity recognition skill](cognitive-search-skill-entity-recognition-v3.md) that recognizes and extracts location entities, loading it into a searchable and filterable `locations` field. Adding structured content to your index gives you more options for filtering, improved relevance, and more focused answers.
+In this tutorial, sample data consists of PDFs and content from the [NASA Earth Book](https://www.nasa.gov/ebooks/earth/). This content is descriptive and informative, with numerous references to geographies, countries, and areas across the world. All of the textual content is captured in chunks, but recurring instances of place names create an opportunity for adding structure to the index. Using skills, it's possible to recognize entities in the text and capture them in an index for use in queries and filters. In this tutorial, we include an [entity recognition skill](cognitive-search-skill-entity-recognition-v3.md) that recognizes and extracts location entities, loading it into a searchable and filterable `locations` field. Adding structured content to your index gives you more options for filtering, improved relevance, and more focused answers.
 
 ### Parent-child fields in one or two indexes?
 
@@ -61,11 +61,11 @@ In Azure AI Search, an index that works best for RAG workloads has these qualiti
 
 - Maintains a parent-child relationship between chunks of a document and the properties of the parent document, such as the file name, file type, title, author, and so forth. To answer a query, chunks could be pulled from anywhere in the index. Association with the parent document providing the chunk is useful for context, citations, and follow up queries.
 
-- Accommodates the queries you want create. You should have fields for vector and hybrid content, and those fields should be attributed to support specific query behaviors. You can only query one index at a time (no joins) so your fields collection should define all of your searchable content.
+- Accommodates the queries you want create. You should have fields for vector and hybrid content, and those fields should be attributed to support specific query behaviors, such as searchable or filterable. You can only query one index at a time (no joins) so your fields collection should define all of your searchable content.
 
 - Your schema should be flat (no complex types or structures). This requirement is specific to the RAG pattern in Azure AI Search.
 
-Although Azure AI Search can't join indexes, you can create indexes that preserve parent-child relationship, and then use sequential or parallel queries in your search logic to pull from both. This exercise includes templates for parent-child elements in the same index and in separate indexes, where information from the parent index is retrieved using a lookup query.
+<!-- Although Azure AI Search can't join indexes, you can create indexes that preserve parent-child relationship, and then use sequential queries in your search logic to pull from both (a query on the chunked data index, a lookup on the parent index). This exercise includes templates for parent-child elements in the same index and in separate indexes, where information from the parent index is retrieved using a lookup query. -->
 
 <!-- > [!NOTE]
 > Schema design affects storage and costs. This exercise is focused on schema fundamentals. In the [Minimize storage and costs](tutorial-rag-build-solution-minimize-storage.md) tutorial, you revisit schema design to consider narrow data types, attribution, and vector configurations that offer more efficient. -->
@@ -136,7 +136,7 @@ A minimal index for LLM is designed to store chunks of content. It typically inc
         SearchField(name="locations", type=SearchFieldDataType.Collection(SearchFieldDataType.String), filterable=True),
         SearchField(name="chunk_id", type=SearchFieldDataType.String, key=True, sortable=True, filterable=True, facetable=True, analyzer_name="keyword"),  
         SearchField(name="chunk", type=SearchFieldDataType.String, sortable=False, filterable=False, facetable=False),  
-        SearchField(name="text_vector", type=SearchFieldDataType.Collection(SearchFieldDataType.Single), vector_search_dimensions=1536, vector_search_profile_name="myHnswProfile")
+        SearchField(name="text_vector", type=SearchFieldDataType.Collection(SearchFieldDataType.Single), vector_search_dimensions=1024, vector_search_profile_name="myHnswProfile")
         ]  
       
     # Configure the vector search configuration  
@@ -157,8 +157,8 @@ A minimal index for LLM is designed to store chunks of content. It typically inc
                 kind="azureOpenAI",  
                 parameters=AzureOpenAIVectorizerParameters(  
                     resource_url=AZURE_OPENAI_ACCOUNT,  
-                    deployment_name="text-embedding-ada-002",
-                    model_name="text-embedding-ada-002"
+                    deployment_name="text-embedding-3-large",
+                    model_name="text-embedding-3-large"
                 ),
             ),  
         ], 
@@ -170,7 +170,7 @@ A minimal index for LLM is designed to store chunks of content. It typically inc
     print(f"{result.name} created")  
     ```
 
-1. For an index schema that more closely mimics structured content, you would have separate indexes for parent and child (chunked) fields. You would need index projections to coordinate the indexing of the two indexes simultaneously. Queries execute against the child index. Query logic includes a lookup query, using the parent_idto retrieve content from the parent index.
+1. For an index schema that more closely mimics structured content, you would have separate indexes for parent and child (chunked) fields. You would need [index projections](index-projections-concept-intro.md) to coordinate the indexing of the two indexes simultaneously. Queries execute against the child index. Query logic includes a lookup query, using the parent_idt  retrieve content from the parent index.
 
    Fields in the child index:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGチュートリアルの詳細更新"
}
```

### Explanation
この更新では、`articles/search/tutorial-rag-build-solution-index-schema.md`ファイルに対して、9行の追加と9行の削除が行われました。主な変更点は、ファイルのタイトルの表記を小文字に変更し、日付を2024年10月1日から2024年10月4日に更新したことです。また、いくつかの段落で文が整理され、内容の明確性が向上しています。

特に、ベクター検索の次元が1536から1024に変更され、他の関連する情報もアップデートされています。これにより、検索インデックスの設計や構成に関する指針が明確にされ、RAGワークロードに最適なスキーマ設計の理解が促進されます。全体として、この変更はチュートリアルの精度や使いやすさを高めることを目的としています。

## articles/search/tutorial-rag-build-solution-maximize-relevance.md{#item-2fdb09}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,317 @@
+---
+title: 'RAG tutorial: Tune relevance'
+titleSuffix: Azure AI Search
+description: Learn how to use the relevance tuning capabilities to return high quality results for generative search.
+
+manager: nitinme
+author: HeidiSteen
+ms.author: heidist
+ms.service: cognitive-search
+ms.topic: tutorial
+ms.date: 10/05/2024
+
+---
+
+# Tutorial: Maximize relevance (RAG in Azure AI Search)
+
+In this tutorial, learn how to improve the relevance of search results used in RAG solutions. Relevance tuning can be an important factor in delivering a RAG solution that meets user expectations. In Azure AI Search, relevance tuning includes L2 semantic ranking and scoring profiles. 
+
+To implement these capabilities, you revisit the index schema to add configurations for semantic ranking and scoring profiles. You then rerun the queries using the new constructs.
+
+In this tutorial, you modify the existing search index and queries to use:
+
+> [!div class="checklist"]
+> - L2 semantic ranking
+> - Scoring profile for document boosting
+
+This tutorial updates the search index created by the [indexing pipeline](tutorial-rag-build-solution-pipeline.md). Updates don't affect the existing content, so no rebuild is necessary and you don't need to rerun the indexer.
+
+> [!NOTE]
+> There are more relevance features in preview, including vector query weighting and setting minimum thresholds, but we omit them from this tutorial because they're in preview.
+
+## Prerequisites
+
+- [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and the [Jupyter package](https://pypi.org/project/jupyter/).
+
+- [Azure AI Search](search-create-service-portal.md), Basic tier or higher for managed identity and semantic ranking, in the same region as Azure OpenAI and Azure AI Services.
+
+- [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource), with a deployment of text-embedding-002 and gpt-35-turbo, in the same region as Azure AI Search.
+
+## Download the sample
+
+The [sample notebook](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Tutorial-RAG/Tutorial-rag.ipynb) includes an updated index and query request.
+
+## Run a baseline query for comparison
+
+Let's start with a new query, "Are there any cloud formations specific to oceans and large bodies of water?".
+
+To compare outcomes after adding relevance features, run the query against the existing index schema, before you add semantic ranking or a scoring profile.
+
+```python
+from azure.search.documents import SearchClient
+from openai import AzureOpenAI
+
+token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")
+openai_client = AzureOpenAI(
+     api_version="2024-06-01",
+     azure_endpoint=AZURE_OPENAI_ACCOUNT,
+     azure_ad_token_provider=token_provider
+ )
+
+deployment_name = "gpt-4o"
+
+search_client = SearchClient(
+     endpoint=AZURE_SEARCH_SERVICE,
+     index_name=index_name,
+     credential=credential
+ )
+
+GROUNDED_PROMPT="""
+You are an AI assistant that helps users learn from the information found in the source material.
+Answer the query using only the sources provided below.
+Use bullets if the answer has multiple points.
+If the answer is longer than 3 sentences, provide a summary.
+Answer ONLY with the facts listed in the list of sources below. Cite your source when you answer the question
+If there isn't enough information below, say you don't know.
+Do not generate answers that don't use the sources below.
+Query: {query}
+Sources:\n{sources}
+"""
+
+# Focused query on cloud formations and bodies of water
+query="Are there any cloud formations specific to oceans and large bodies of water?"
+vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=50, fields="text_vector")
+
+search_results = search_client.search(
+    search_text=query,
+    vector_queries= [vector_query],
+    select=["title", "chunk", "locations"],
+    top=5,
+)
+
+sources_formatted = "=================\n".join([f'TITLE: {document["title"]}, CONTENT: {document["chunk"]}, LOCATIONS: {document["locations"]}' for document in search_results])
+
+response = openai_client.chat.completions.create(
+    messages=[
+        {
+            "role": "user",
+            "content": GROUNDED_PROMPT.format(query=query, sources=sources_formatted)
+        }
+    ],
+    model=deployment_name
+)
+
+print(response.choices[0].message.content)
+```
+
+Output from this request might look like the following example.
+
+```
+Yes, there are cloud formations specific to oceans and large bodies of water. A notable example is "cloud streets," which are parallel rows of clouds that form over the Bering Strait in the Arctic Ocean. These cloud streets occur when wind blows from a cold surface like sea ice over warmer, moister air near the open ocean, leading to the formation of spinning air cylinders. Clouds form along the upward cycle of these cylinders, while skies remain clear along the downward cycle (Source: page-21.pdf).
+```
+
+## Update the index for semantic ranking and scoring profiles
+
+In a previous tutorial, you [designed an index schema](tutorial-rag-build-solution-index-schema.md) for RAG workloads. We purposely omitted relevance enhancements from that schema so that you could focus on the fundamentals. Deferring relevance to a separate exercise gives you a before-and-after comparison of the quality of search results after the updates are made.
+
+1. Update the import statements to include classes for semantic ranking and scoring profiles.
+
+   ```python
+    from azure.identity import DefaultAzureCredential
+    from azure.identity import get_bearer_token_provider
+    from azure.search.documents.indexes import SearchIndexClient
+    from azure.search.documents.indexes.models import (
+        SearchField,
+        SearchFieldDataType,
+        VectorSearch,
+        HnswAlgorithmConfiguration,
+        VectorSearchProfile,
+        AzureOpenAIVectorizer,
+        AzureOpenAIVectorizerParameters,
+        SearchIndex,
+        SemanticConfiguration,
+        SemanticPrioritizedFields,
+        SemanticField,
+        SemanticSearch,
+        ScoringProfile,
+        TagScoringFunction,
+        TagScoringParameters
+    )
+    ```
+
+1. Add the following semantic configuration to the search index. This example can be found in the update schema step in the notebook.
+
+    ```python
+    # New semantic configuration
+    semantic_config = SemanticConfiguration(
+        name="my-semantic-config",
+        prioritized_fields=SemanticPrioritizedFields(
+            title_field=SemanticField(field_name="title"),
+            keywords_fields=[SemanticField(field_name="locations")],
+            content_fields=[SemanticField(field_name="chunk")]
+        )
+    )
+    
+    # Create the semantic settings with the configuration
+    semantic_search = SemanticSearch(configurations=[semantic_config])
+    ```
+
+   A semantic configuration has a name and a prioritized list of fields to help optimize the inputs to semantic ranker. For more information, see [Configure semantic ranking](/azure/search/semantic-how-to-configure).
+
+1. Next, add a scoring profile definition. As with semantic configuration, a scoring profile can be added to an index schema at any time. This example is also in the update schema step in the notebook, following the semantic configuration.
+
+    ```python
+    # New scoring profile
+    scoring_profiles = [  
+        ScoringProfile(  
+            name="my-scoring-profile",
+            functions=[
+                TagScoringFunction(  
+                    field_name="locations",  
+                    boost=5.0,  
+                    parameters=TagScoringParameters(  
+                        tags_parameter="tags",  
+                    ),  
+                ) 
+            ]
+        )
+    ]
+    ```
+
+   This profile uses the tag function which boosts the scores of documents where a match was found in the locations field. Recall that the search index has a vector field, and multiple nonvector fields for title, chunks, and locations. The locations field is a string collection, and string collections can be boosted using the tags function in a scoring profile. For more information, see [Add a scoring profile](index-add-scoring-profiles.md) and [Enhancing Search Relevance with Document Boosting (blog post)](https://farzzy.hashnode.dev/enhance-azure-ai-search-document-boosting).
+
+1. Update the index definition on the search service.
+
+   ```python
+   # Update the search index with the semantic configuration
+    index = SearchIndex(name=index_name, fields=fields, vector_search=vector_search, semantic_search=semantic_search, scoring_profiles=scoring_profiles)  
+    result = index_client.create_or_update_index(index)  
+    print(f"{result.name} updated")  
+    ```
+
+## Update queries for semantic ranking and scoring profiles
+
+In a previous tutorial, you [ran queries](tutorial-rag-build-solution-query.md) that execute on the search engine, passing the response and other information to an LLM for chat completion.
+
+This example modifies the query request to include the semantic configuration and scoring profile.
+
+```python
+# Import libraries
+from azure.search.documents import SearchClient
+from openai import AzureOpenAI
+
+token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")
+openai_client = AzureOpenAI(
+     api_version="2024-06-01",
+     azure_endpoint=AZURE_OPENAI_ACCOUNT,
+     azure_ad_token_provider=token_provider
+ )
+
+deployment_name = "gpt-4o"
+
+search_client = SearchClient(
+     endpoint=AZURE_SEARCH_SERVICE,
+     index_name=index_name,
+     credential=credential
+ )
+
+# Prompt is unchanged in this update
+GROUNDED_PROMPT="""
+You are an AI assistant that helps users learn from the information found in the source material.
+Answer the query using only the sources provided below.
+Use bullets if the answer has multiple points.
+If the answer is longer than 3 sentences, provide a summary.
+Answer ONLY with the facts listed in the list of sources below.
+If there isn't enough information below, say you don't know.
+Do not generate answers that don't use the sources below.
+Query: {query}
+Sources:\n{sources}
+"""
+
+# Queries are unchanged in this update
+query="Are there any cloud formations specific to oceans and large bodies of water?"
+vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=50, fields="text_vector")
+
+# Add query_type semantic and semantic_configuration_name
+# Add scoring_profile and scoring_parameters
+search_results = search_client.search(
+    query_type="semantic",
+    semantic_configuration_name="my-semantic-config",
+    scoring_profile="my-scoring-profile",
+    scoring_parameters=["tags-ocean, 'sea surface', seas, surface"],
+    search_text=query,
+    vector_queries= [vector_query],
+    select="title, chunk, locations",
+    top=5,
+)
+sources_formatted = "=================\n".join([f'TITLE: {document["title"]}, CONTENT: {document["chunk"]}, LOCATIONS: {document["locations"]}' for document in search_results])
+
+response = openai_client.chat.completions.create(
+    messages=[
+        {
+            "role": "user",
+            "content": GROUNDED_PROMPT.format(query=query, sources=sources_formatted)
+        }
+    ],
+    model=deployment_name
+)
+
+print(response.choices[0].message.content)
+```
+
+Output from a semantically ranked and boosted query might look like the following example.
+
+```
+Yes, there are specific cloud formations influenced by oceans and large bodies of water:
+
+- **Stratus Clouds Over Icebergs**: Low stratus clouds can frame holes over icebergs, such as Iceberg A-56 in the South Atlantic Ocean, likely due to thermal instability caused by the iceberg (source: page-39.pdf).
+
+- **Undular Bores**: These are wave structures in the atmosphere created by the collision of cool, dry air from a continent with warm, moist air over the ocean, as seen off the coast of Mauritania (source: page-23.pdf).
+
+- **Ship Tracks**: These are narrow clouds formed by water vapor condensing around tiny particles from ship exhaust. They are observed over the oceans, such as in the Pacific Ocean off the coast of California (source: page-31.pdf).
+
+These specific formations are influenced by unique interactions between atmospheric conditions and the presence of large water bodies or objects within them.
+```
+
+Adding semantic ranking and scoring profiles positively affects the response from the LLM by promoting results that meet scoring criteria and are semantically relevant. 
+
+Now that you have a better understanding of index and query design, let's move on to optimizing for speed and concision. We revisit the schema definition to implement quantization and storage reduction, but the rest of the pipeline and models remain intact.
+
+<!-- ## Update queries for minimum thresholds ** NOT AVAILABLE IN PYTHON SDK
+
+Keyword search only returns results if there's match found in the index, up to a maximum of 50 results by default. In contrast, vector search returns `k`-results every time, even if the matching vectors aren't a close match.
+
+In the vector query portion of the request, add a threshold object and set a minimum value for including vector matches in the results.
+
+Vector scores range from 0.333 to 1.00. For more information, see [Set thresholds to exclude low-scoring results](vector-search-how-to-query.md#set-thresholds-to-exclude-low-scoring-results-preview) and [Scores in a vector search results](vector-search-ranking.md#scores-in-a-vector-search-results).
+
+```python
+# Update the vector_query to include a minimum threshold.
+query="how much of earth is covered by water"
+vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=1, fields="text_vector", threshold.kind="vectorSImiliarty", threshold.value=0.8, exhaustive=True) -->
+
+<!-- ## Update queries for vector weighting
+
+<!-- Using preview features, you can unpack a hybrid search score to review the individual component scores. Based on that information, you can set minimum thresholds to exclude any match that falls below it.
+
+Semantic ranking and scoring profiles operate on nonvector content, but you can tune the vector portion of a hybrid query to amplify or diminish its importance based on how much value it adds to the results. For example, if you run keyword search and vector search independently and find that one of them is outperforming the other, you can adjust the weight on the vector side to higher or lower. This approach gives you more control over query processing.
+ -->
+
+<!-- Key points:
+
+- How to measure relevance (?) to determine if changes are improving results
+- Try different algorithms (HNSW vs eKnn)
+- Change query structure (hybrid with vector/non over same content (double-down), hybrid over multiple fields)
+- semantic ranking
+- scoring profiles
+- thresholds for minimum score
+- set weights
+- filters
+- analyzers and normalizers
+- advanced query formats (regular expressions, fuzzy search) -->
+
+<!-- ## Next step
+
+> [!div class="nextstepaction"]
+> [Reduce vector storage and costs](tutorial-rag-build-solution-minimize-storage.md)
+ -->
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "RAGチュートリアル: 関連性を最大化する方法"
}
```

### Explanation
この変更では、新しいファイル`tutorial-rag-build-solution-maximize-relevance.md`が追加されました。このチュートリアルでは、RAGソリューションにおいて検索結果の関連性を向上させる方法について説明しています。具体的には、Azure AI SearchのL2セマンティックランキングやスコアリングプロファイルの設定を通して、ユーザーの期待に応える高品質な結果を返すための調整方法が紹介されています。

チュートリアルには、関連性を向上させるためのインデックススキーマの更新手順や、クエリの実行例が含まれており、ユーザーが具体的な手順に従って関連性を最大化するための具体的な指針を提供します。また、この更新により、検索インデックスの改善が行われることで、より効果的にユーザーのニーズに対応できるようになります。全体として、このファイルはRAGソリューションの重要なコンポーネントである関連性調整について、非常に詳細に解説しています。

## articles/search/tutorial-rag-build-solution-models.md{#item-6796c9}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.author: heidist
 ms.service: cognitive-search
 ms.topic: tutorial
 ms.custom: references_regions
-ms.date: 10/01/2024
+ms.date: 10/04/2024
 
 ---
 
@@ -48,7 +48,7 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
   - [Azure AI Studio](/azure/ai-studio/reference/region-support) regions. 
 
-  Azure AI Search is currently facing limited availability in some regions, such as West Europe and West US 2/3. Check the [Azure AI Search region list](search-region-support.md) to confirm region status.
+  Azure AI Search is currently facing limited availability in some regions, such as West Europe and West US 2/3. To confirm region status, check the [Azure AI Search region list](search-region-support.md).
 
 > [!TIP]
 > Currently, the following regions provide the most overlap among the model providers and have the most capacity: **East US2** and **South Central** in the Americas; **France Central** or **Switzerland North** in Europe; **Australia East** in Asia Pacific.
@@ -59,7 +59,7 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
 Vectorized content improves the query results in a RAG solution. Azure AI Search supports a built-in vectorization action in an indexing pipeline. It also supports vectorization at query time, converting text or image inputs into embeddings for a vector search. In this step, identify an embedding model that works for your content and queries. If you're providing raw vector data and raw vector queries, or if your RAG solution doesn't include vector data, skip this step.
 
-Vector queries that include a text-to-vector conversion step must use the same embedding model that was used during indexing. The search engine won't throw an error if you use different models, but you'll get poor results.
+Vector queries that include a text-to-vector conversion step must use the same embedding model that was used during indexing. The search engine doesn't throw an error if you use different models, but you get poor results.
 
 To meet the same-model requirement, choose embedding models that can be referenced through *skills* during indexing and through *vectorizers* during query execution. The following table lists the skill and vectorizer pairs. To see how the embedding models are used, skip ahead to [Create an indexing pipeline](tutorial-rag-build-solution-pipeline.md) for code that calls an embedding skill and a matching vectorizer. 
 
@@ -75,7 +75,7 @@ Azure AI Search provides skill and vectorizer support for the following embeddin
 
 <sup>2</sup> Deployed models in the model catalog are accessed over an AML endpoint. We use the existing AML skill for this connection.
 
-You can use other models besides those listed here. For more information, see [Use non-Azure models for embeddings](#use-non-azure-models-for-embeddings) in this article.
+You can use other models besides the ones listed here. For more information, see [Use non-Azure models for embeddings](#use-non-azure-models-for-embeddings) in this article.
 
 > [!NOTE]
 > Inputs to an embedding models are typically chunked data. In an Azure AI Search RAG pattern, chunking is handled in the indexer pipeline, covered in [another tutorial](tutorial-rag-build-solution-pipeline.md) in this series.
@@ -90,16 +90,18 @@ The following models are commonly used for a chat search experience:
 |--------|------------|
 | Azure OpenAI | GPT-35-Turbo, <br>GPT-4, <br>GPT-4o, <br>GPT-4 Turbo |
 
-GPT-35-Turbo and GPT-4 models are optimized to work with inputs formatted as a conversation. 
+GPT-35-Turbo and GPT-4 models are optimized to work with inputs formatted as a conversation.
+
+We use GPT-4o in this tutorial. During testing, we found that it's less likely to supplement with its own training data. For example, given the query "how much of the earth is covered by water?", GPT-35-Turbo answered using its built-in knowledge of earth to state that 71% of the earth is covered by water, even though the sample data doesn't provide that fact. In contrast, GPT-4o responded (correctly) with "I don't know".
 
 ## Deploy models and collect information
 
-Models must be deployed and accessible through an endpoint. Both embedding-related skills and vectorizers need the number of dimensions and the model name. Other details about your model might be required by the client used on the connection.
+Models must be deployed and accessible through an endpoint. Both embedding-related skills and vectorizers need the number of dimensions and the model name. 
 
 This tutorial series uses the following models and model providers:
 
-- Text-embedding-ada-02 on Azure OpenAI for embeddings
-- GPT-35-Turbo on Azure OpenAI for chat completion
+- Text-embedding-3-large on Azure OpenAI for embeddings
+- GPT-4o on Azure OpenAI for chat completion
 
 You must have [**Cognitive Services OpenAI Contributor**]( /azure/ai-services/openai/how-to/role-based-access-control#cognitive-services-openai-contributor) or higher to deploy models in Azure OpenAI.
 
@@ -109,17 +111,17 @@ You must have [**Cognitive Services OpenAI Contributor**]( /azure/ai-services/op
 
 1. Select **Deploy model** > **Deploy base model**.
 
-1. Select **text-embedding-ada-02** from the dropdown list and confirm the selection.
+1. Select **text-embedding-3-large** from the dropdown list and confirm the selection.
 
-1. Specify a deployment name. We recommend "text-embedding-ada-002".
+1. Specify a deployment name. We recommend "text-embedding-3-large".
 
 1. Accept the defaults.
 
 1. Select **Deploy**.
 
-1. Repeat the previous steps for **gpt-35-turbo**.
+1. Repeat the previous steps for **gpt-4o**.
 
-1. Make a note of the model names and endpoint. Embedding skills and vectorizers assemble the full endpoint internally, so you only need the resource URI. For example, given `https://MY-FAKE-ACCOUNT.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15`, the endpoint you should provide in skill and vectorizer definitions is `https://MY-FAKE-ACCOUNT.openai.azure.com`.
+1. Make a note of the model names and endpoint. Embedding skills and vectorizers assemble the full endpoint internally, so you only need the resource URI. For example, given `https://MY-FAKE-ACCOUNT.openai.azure.com/openai/deployments/text-embedding-3-large/embeddings?api-version=2024-06-01`, the endpoint you should provide in skill and vectorizer definitions is `https://MY-FAKE-ACCOUNT.openai.azure.com`.
 
 ## Configure search engine access to Azure models
 
@@ -138,10 +140,13 @@ Assign yourself and the search service identity permissions on Azure OpenAI. The
 1. Select **Add role assignment**.
 
 1. Select [**Cognitive Services OpenAI User**](/azure/ai-services/openai/how-to/role-based-access-control#cognitive-services-openai-userpermissions).
+
 1. Select **Managed identity** and then select **Members**. Find the system-managed identity for your search service in the dropdown list.
 
 1. Next, select **User, group, or service principal** and then select **Members**. Search for your user account and then select it from the dropdown list.
 
+1. Make sure you have two security principals assigned to the role.
+
 1. Select **Review and Assign** to create the role assignments.
 
 For access to models on Azure AI Vision, assign **Cognitive Services OpenAI User**. For Azure AI Studio, assign **Azure AI Developer**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションモデルに関するドキュメントの更新"
}
```

### Explanation
この変更では、`articles/search/tutorial-rag-build-solution-models.md`ファイルに対して修正が加えられました。具体的には、17行が追加され、12行が削除され、合計29行の変更が行われています。主な更新内容は以下の通りです。

1. **日付の更新**: 最終更新日が2024年10月1日から2024年10月4日に変更されています。
2. **文の明確化**: 一部の文が再構成され、より明確な表現に修正されています。例えば、Azure AI Searchの地域に関する記述が簡潔になっています。
3. **モデル名の変更**: 使用する埋め込みモデルが`text-embedding-ada-02`から`text-embedding-3-large`に変更され、これに伴い関連する推奨事項や手順も更新されています。
4. **GPTモデルの変更**: チャット完了に使用するモデルが`GPT-35-Turbo`から`GPT-4o`に変更され、その理由も説明されています。この変更により、モデルがユーザーからの質問に対して適切に応答する可能性が高まります。

全体として、これらの更新は、RAGソリューションに関連するモデル使用に関するドキュメントの精度を向上させ、最新の情報を反映しています。

## articles/search/tutorial-rag-build-solution-pipeline.md{#item-25ce01}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'RAG Tutorial: Build an indexing pipeline'
+title: 'RAG tutorial: Build an indexing pipeline'
 titleSuffix: Azure AI Search
 description: Create an indexer-driven pipeline that loads, chunks, embeds, and ingests content for RAG solutions on Azure AI Search.
 
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: tutorial
-ms.date: 10/01/2024
+ms.date: 10/04/2024
 
 ---
 
@@ -28,7 +28,7 @@ In this tutorial, you:
 If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
 
 > [!TIP]
-> You can use the [Import and vectorize data wizard](search-import-data-portal.md) to create your pipeline. For some quickstarts, see [Image search](search-get-started-portal-image-search.md) and [Vector search](search-get-started-portal-import-vectors.md).
+> You can use the [Import and vectorize data wizard](search-import-data-portal.md) to create your pipeline. Try some quickstarts: [Image search](search-get-started-portal-image-search.md) and [Vector search](search-get-started-portal-import-vectors.md).
 
 ## Prerequisites
 
@@ -38,9 +38,9 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
 - [Azure AI Search](search-create-service-portal.md), Basic tier or above for managed identity and semantic ranking. Choose a region that's shared with Azure OpenAI and Azure AI Services.
 
-- [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource), with a deployment of text-embedding-002, in the same region as Azure AI Search. For more information about embedding models used in RAG solutions, see [Choose embedding models for RAG in Azure AI Search](tutorial-rag-build-solution-models.md).
+- [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource), with a deployment of text-embedding-3-large, in the same region as Azure AI Search. For more information about embedding models used in RAG solutions, see [Choose embedding models for RAG in Azure AI Search](tutorial-rag-build-solution-models.md).
 
-- [Azure AI Services multiservice account](/azure/ai-services/multi-service-resource), in the same region as Azure AI Search. This resource is used for the Entity Recognition skill that detects locations in your content.
+- [Azure AI Service multiservice account](/azure/ai-services/multi-service-resource), in the same region as Azure AI Search. This resource is used for the Entity Recognition skill that detects locations in your content.
 
 ## Download the sample
 
@@ -78,7 +78,7 @@ fields = [
     SearchField(name="locations", type=SearchFieldDataType.Collection(SearchFieldDataType.String), filterable=True),
     SearchField(name="chunk_id", type=SearchFieldDataType.String, key=True, sortable=True, filterable=True, facetable=True, analyzer_name="keyword"),  
     SearchField(name="chunk", type=SearchFieldDataType.String, sortable=False, filterable=False, facetable=False),  
-    SearchField(name="text_vector", type=SearchFieldDataType.Collection(SearchFieldDataType.Single), vector_search_dimensions=1536, vector_search_profile_name="myHnswProfile")
+    SearchField(name="text_vector", type=SearchFieldDataType.Collection(SearchFieldDataType.Single), vector_search_dimensions=1024, vector_search_profile_name="myHnswProfile")
     ]  
   
 # Configure the vector search configuration  
@@ -99,8 +99,8 @@ vector_search = VectorSearch(
             kind="azureOpenAI",  
             parameters=AzureOpenAIVectorizerParameters(  
                 resource_url=AZURE_OPENAI_ACCOUNT,  
-                deployment_name="text-embedding-ada-002",
-                model_name="text-embedding-ada-002"
+                deployment_name="text-embedding-3-large",
+                model_name="text-embedding-3-large"
             ),
         ),  
     ], 
@@ -116,7 +116,7 @@ print(f"{result.name} created")
 
 In this step, set up the sample data and a connection to Azure Blob Storage. The indexer retrieves PDFs from a container. You create the container and upload files in this step.
 
-The original ebook is large, over 100 pages and 35 MB in size. We broke it up into smaller PDFs, one per page of text, to stay under the [API payload limit](search-limits-quotas-capacity.md#api-request-limits) of 16 MB per API call and also the [AI enrichment data limits](search-limits-quotas-capacity.md#data-limits-ai-enrichment). For simplicity, we omit image vectorization for this exercise.
+The original ebook is large, over 100 pages and 35 MB in size. We broke it up into smaller PDFs, one per page of text, to stay under the [document limit for indexers](search-limits-quotas-capacity.md#indexer-limits) of 16 MB per API call and also the [AI enrichment data limits](search-limits-quotas-capacity.md#data-limits-ai-enrichment). For simplicity, we omit image vectorization for this exercise.
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and find your Azure Storage account.
 
@@ -193,8 +193,8 @@ embedding_skill = AzureOpenAIEmbeddingSkill(
     description="Skill to generate embeddings via Azure OpenAI",  
     context="/document/pages/*",  
     resource_url=AZURE_OPENAI_ACCOUNT,  
-    deployment_name="text-embedding-ada-002",  
-    model_name="text-embedding-ada-002",
+    deployment_name="text-embedding-3-large",  
+    model_name="text-embedding-3-large",
     dimensions=1536,
     inputs=[  
         InputFieldMappingEntry(name="text", source="/document/pages/*"),  
@@ -290,7 +290,7 @@ print(f' {indexer_name} is created and running. Give the indexer a few minutes b
 
 ## Run a query to check results
 
-Send a query to confirm your index is operational. This request converts the text string "`where are the nasa headquarters located?`" into a vector for a vector search. Results consist of the fields in the select statement, some of which are printed as output.
+Send a query to confirm your index is operational. This request converts the text string "`what's NASA's website?`" into a vector for a vector search. Results consist of the fields in the select statement, some of which are printed as output.
 
 There's no chat or generative AI at this point. The results are verbatim content from your search index.
 
@@ -299,32 +299,28 @@ from azure.search.documents import SearchClient
 from azure.search.documents.models import VectorizableTextQuery
 
 # Vector Search using text-to-vector conversion of the querystring
-query = "where are NASA's headquarters located?"  
+query = "what's NASA's website?"  
 
 search_client = SearchClient(endpoint=AZURE_SEARCH_SERVICE, credential=credential, index_name=index_name)
-vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=1, fields="text_vector", exhaustive=True)
+vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=50, fields="text_vector")
   
 results = search_client.search(  
     search_text=query,  
     vector_queries= [vector_query],
-    select=["parent_id", "chunk_id", "title", "chunk", "locations"],
+    select=["chunk"],
     top=1
 )  
   
 for result in results:  
     print(f"Score: {result['@search.score']}")
-    print(f"Title: {result['title']}")
-    print(f"Locations: {result['locations']}")
-    print(f"Content: {result['chunk']}")
+    print(f"Chunk: {result['chunk']}")
 ```
 
 This query returns a single match (`top=1`) consisting of the one chunk determined by the search engine to be the most relevant. Results from the query should look similar to the following example:
 
 ```
-Score: 0.03306011110544205
-Title: page-178.pdf
-Locations: ['Headquarters', 'Washington']
-Content: national Aeronautics and Space Administration
+Score: 0.01666666753590107
+Chunk: national Aeronautics and Space Administration
 
 earth Science
 
@@ -339,35 +335,36 @@ www.nasa.gov
 np-2018-05-2546-hQ
 ```
 
-Try a few more queries to get a sense of what the search engine returns directly so that you can compare it with an LLM-enabled response. Rerun the previous script with this query: `"how much of the earth is covered in water"`?
+Try a few more queries to get a sense of what the search engine returns directly so that you can compare it with an LLM-enabled response. Rerun the previous script with this query: `"patagonia geography"` and set `top` to 3 to return more than one response.
 
-Results from this second query should look similar to the following results, which are lightly edited for concision. 
+Results from this second query should look similar to the following results, which are lightly edited for concision. The output is copied from the notebook, which truncates the response to what you see in this example. You can expand the cell output to review the complete answer.
 
 ```
-Score: 0.03333333507180214
-Content:
+Score: 0.03306011110544205
+Chunk: 
 
-Land of Lakes
-Canada
+Swirling Bloom off Patagonia
+Argentina
 
-During the last Ice Age, nearly all of Canada was covered by a massive ice sheet. Thousands of years later, the landscape still shows 
+Interesting art often springs out of the convergence of different ideas and influences. And so it is with nature. 
 
-the scars of that icy earth-mover. Surfaces that were scoured by retreating ice and flooded by Arctic seas are now dotted with 
+Off the coast of Argentina, two strong ocean currents converge and often stir up a colorful brew, as shown in this Aqua image from 
 
-millions of lakes, ponds, and streams. In this false-color view from the Terra satellite, water is various shades of blue, green, tan, and 
+December 2010. 
 
-black, depending on the amount of suspended sediment and phytoplankton; vegetation is red.
+This milky green and blue bloom formed on the continental shelf off of Patagonia, where warmer, saltier waters from the subtropics 
 
-The region of Nunavut Territory is sometimes referred to as the “Barren Grounds,” as it is nearly treeless and largely unsuitable for 
+meet colder, fresher waters flowing from the south. Where these currents collide, turbulent eddies and swirls form, pulling nutrients 
 
-agriculture. The ground is snow-covered for much of the year, and the soil typically remains frozen (permafrost) even during the 
+up from the deep ocean. The nearby Rio de la Plata also deposits nitrogen- and iron-laden sediment into the sea. Add in some 
+...
 
-summer thaw. Nonetheless, this July 2001 image shows plenty of surface vegetation in midsummer, including lichens, mosses, 
+while others terminate in water. The San Rafael and San Quintín glaciers (shown at the right) are the icefield’s largest. Both have 
 
-shrubs, and grasses. The abundant fresh water also means the area is teeming with flies and mosquitoes.
+been receding rapidly in the past 30 years.
 ```
 
-With this example, it's easier to spot how chunks are returned verbatim, and how keyword and similarity search identify top matches. This specific chunk definitely has information about water and coverage over the earth, but it's not exactly relevant to the query. Semantic ranker would find a better answer, but as a next step, let's see how to connect Azure AI Search to an LLM for conversational search.
+With this example, it's easier to spot how chunks are returned verbatim, and how keyword and similarity search identify top matches. This specific chunk definitely has information about Patagonia and geography, but it's not exactly relevant to the query. Semantic ranker would promote more relevant chunks for a better answer, but as a next step, let's see how to connect Azure AI Search to an LLM for conversational search.
 
 <!-- Objective:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGチュートリアルにおけるインデクシングパイプラインの更新"
}
```

### Explanation
この変更では、`articles/search/tutorial-rag-build-solution-pipeline.md`ファイルに対して修正が加えられました。具体的には、34行が追加され、37行が削除され、合計71行の変更が行われています。主な変更点は次の通りです。

1. **タイトルの修正**: タイトルが大文字から小文字に変更され、統一感が持たせられています。
2. **日付の更新**: 最終更新日が2024年10月1日から2024年10月4日に修正されました。
3. **埋め込みモデルの更新**: 使用する埋め込みモデルが`text-embedding-002`から`text-embedding-3-large`に変更され、これに伴って関連する説明や手順も更新されています。
4. **不要な行の削除**: 不要な説明や冗長な内容が削除され、情報がよりコンパクトに整理されています。
5. **クエリ内容の変更**: テスト用のクエリ内容が変更され、より具体的な質問に調整されています。

全体として、これらの更新は、インデクシングパイプラインに関するドキュメントの精度と使い勝手を向上させることを目的としています。执行する手順や推奨モデル情報が最新のものに反映されており、ユーザーがより効率的にRAGソリューションを構築できるようになっています。

## articles/search/tutorial-rag-build-solution-query.md{#item-93965f}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'RAG Tutorial: Search using an LLM'
+title: 'RAG tutorial: Search using an LLM'
 titleSuffix: Azure AI Search
 description: Learn how to build queries and engineer prompts for LLM-enabled search on Azure AI Search. Queries used in generative search provide the inputs to an LLM chat engine.
 
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: tutorial
-ms.date: 10/03/2024
+ms.date: 10/04/2024
 
 ---
 
@@ -32,7 +32,7 @@ This tutorial builds on the previous tutorials. It assumes you have a search ind
 
 - [Azure AI Search](search-create-service-portal.md), in a region shared with Azure OpenAI.
 
-- [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource), with a deployment of gpt-35-turbo. For more information, see [Choose models for RAG in Azure AI Search](tutorial-rag-build-solution-models.md)
+- [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource), with a deployment of gpt-4o. For more information, see [Choose models for RAG in Azure AI Search](tutorial-rag-build-solution-models.md)
 
 ## Download the sample
 
@@ -42,14 +42,14 @@ You use the same notebook from the previous indexing pipeline tutorial. Scripts
 
 The RAG pattern in Azure AI Search is a synchronized series of connections to a search index to obtain the grounding data, followed by a connection to an LLM to formulate a response to the user's question. The same query string is used by both clients.
 
-You're setting up two clients, so you need permissions on both resources. We use API keys for this exercise. The following endpoints and keys are used for queries:
+You're setting up two clients, so you need endpoints and permissions on both resources. This tutorial assumes you set up role assignments for authorized connections, but you should provide the endpoints in your sample notebook:
 
 ```python
 # Set endpoints and API keys for Azure services
 AZURE_SEARCH_SERVICE: str = "PUT YOUR SEARCH SERVICE ENDPOINT HERE"
 # AZURE_SEARCH_KEY: str = "DELETE IF USING ROLES, OTHERWISE PUT YOUR SEARCH SERVICE ADMIN KEY HERE"
 AZURE_OPENAI_ACCOUNT: str = "PUR YOUR AZURE OPENAI ENDPOINT HERE"
-# AZURE_OPENAI_KEY: str = "DELETE IF USING ROLES, OTHERWISE PPUT YOUR AZURE OPENAI KEY HERE"
+# AZURE_OPENAI_KEY: str = "DELETE IF USING ROLES, OTHERWISE PUT YOUR AZURE OPENAI KEY HERE"
 ```
 
 ## Example script for prompt and query
@@ -68,7 +68,7 @@ openai_client = AzureOpenAI(
      azure_ad_token_provider=token_provider
  )
 
-deployment_name = "gpt-35-turbo"
+deployment_name = "gpt-4o"
 
 search_client = SearchClient(
      endpoint=AZURE_SEARCH_SERVICE,
@@ -82,27 +82,33 @@ You are an AI assistant that helps users learn from the information found in the
 Answer the query using only the sources provided below.
 Use bullets if the answer has multiple points.
 If the answer is longer than 3 sentences, provide a summary.
-Answer ONLY with the facts listed in the list of sources below.
+Answer ONLY with the facts listed in the list of sources below. Cite your source when you answer the question
 If there isn't enough information below, say you don't know.
 Do not generate answers that don't use the sources below.
 Query: {query}
 Sources:\n{sources}
 """
 
-# Provide the query. Notice it's sent to both the search engine and the LLM.
-# The query sent to the search engine is hybrid. Keyword search on "query". Text-to-vector conversion for vector search.
-query="how much of earth is covered by water"
-vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=1, fields="text_vector", exhaustive=True)
+# Provide the search query. 
+# It's hybrid: a keyword search on "query", with text-to-vector conversion for "vector_query".
+# The vector query finds 50 nearest neighbor matches in the search index
+query="What's the NASA earth book about?"
+vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=50, fields="text_vector")
 
 # Set up the search results and the chat thread.
 # Retrieve the selected fields from the search index related to the question.
+# Search results are limited to the top 5 matches. Limiting top can help you stay under LLM quotas.
 search_results = search_client.search(
     search_text=query,
     vector_queries= [vector_query],
-    select="title, chunk, locations",
-    top=1,
+    select=["title", "chunk", "locations"],
+    top=5,
 )
-sources_formatted = "\n".join([f'{document["title"]}:{document["chunk"]}:{document["locations"]}' for document in search_results])
+
+# Newlines could be in the OCR'd content or in PDFs, as is the case for the sample PDFs used for this tutorial.
+# Use a unique separator to make the sources distinct. 
+# We chose repeated equal signs (=) followed by a newline because it's unlikely the source documents contain this sequence.
+sources_formatted = "=================\n".join([f'TITLE: {document["title"]}, CONTENT: {document["chunk"]}, LOCATIONS: {document["locations"]}' for document in search_results])
 
 response = openai_client.chat.completions.create(
     messages=[
@@ -119,11 +125,15 @@ print(response.choices[0].message.content)
 
 ## Review results
 
-In this response, the answer is based on a single input (`top=1`) consisting of the one chunk determined by the search engine to be the most relevant. Instructions in the prompt tell the LLM to use only the information in the `sources`, or formatted search results. 
+In this response, the answer is based on five inputs (`top=5`) consisting of chunks determined by the search engine to be the most relevant. Instructions in the prompt tell the LLM to use only the information in the `sources`, or formatted search results. 
+
+Results from the first query `"What's the NASA earth book about?"` should look similar to the following example.
 
-Results from the first query `"how much of earth is covered by water"` should look similar to the following example.
+```
+The NASA Earth book is about the intricate and captivating science of our planet, studied through NASA's unique perspective and tools. It presents Earth as a dynamic and complex system, observed through various cycles and processes such as the water cycle and ocean circulation. The book combines stunning satellite images with detailed scientific insights, portraying Earth’s beauty and the continuous interaction of land, wind, water, ice, and air seen from above. It aims to inspire and demonstrate that the truth of our planet is as compelling as any fiction.
 
-:::image type="content" source="media/tutorial-rag-solution/chat-results-1.png" alt-text="Screenshot of an LLM response to a simple question using a single match from search results.":::
+Source: page-8.pdf
+```
 
 It's expected for LLMs to return different answers, even if the prompt and queries are unchanged. Your result might look very different from the example. For more information, see [Learn how to use reproducible output](/azure/ai-services/openai/how-to/reproducible-output).
 
@@ -132,11 +142,27 @@ It's expected for LLMs to return different answers, even if the prompt and queri
 
 ## Add a filter
 
-Recall that you created a `locations` field using applied AI, populated with places recognized by the Entity Recognition skill. The field definition for locations includes the `filterable` attribute. Let's repeat the previous request, but this time adding a filter that selects on the term *ice* in the locations field. A filter introduces inclusion or exclusion criteria. The search engine is still doing a vector search on `"how much of earth is covered by water"`, but it's now excluding matches that don't include *ice*. For more information about filtering on string collections and on vector queries, see [text filter fundamentals](search-filters.md#text-filter-fundamentals),[Understand collection filters](search-query-understand-collection-filters.md), and [Add filters to a vector query](vector-search-filters.md).
+Recall that you created a `locations` field using applied AI, populated with places recognized by the Entity Recognition skill. The field definition for locations includes the `filterable` attribute. Let's repeat the previous request, but this time adding a filter that selects on the term *ice* in the locations field. 
+
+A filter introduces inclusion or exclusion criteria. The search engine is still doing a vector search on `"What's the NASA earth book about?"`, but it's now excluding matches that don't include *ice*. For more information about filtering on string collections and on vector queries, see [text filter fundamentals](search-filters.md#text-filter-fundamentals), [Understand collection filters](search-query-understand-collection-filters.md), and [Add filters to a vector query](vector-search-filters.md).
 
 Replace the search_results definition with the following example that includes a filter:
 
 ```python
+query="what is the NASA earth book about?"
+vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=50, fields="text_vector")
+
+# Add a filter that selects documents based on whether locations includes the term "ice".
+search_results = search_client.search(
+    search_text=query,
+    vector_queries= [vector_query],
+    filter="search.ismatch('ice*', 'locations', 'full', 'any')",
+    select=["title", "chunk", "locations"],
+    top=5,
+)
+
+sources_formatted = "=================\n".join([f'TITLE: {document["title"]}, CONTENT: {document["chunk"]}, LOCATIONS: {document["locations"]}' for document in search_results])
+
 search_results = search_client.search(
     search_text=query,
     top=10,
@@ -146,28 +172,45 @@ search_results = search_client.search(
 
 Results from the filtered query should now look similar to the following response. Notice the emphasis on ice cover.
 
-:::image type="content" source="media/tutorial-rag-solution/chat-results-filter.png" alt-text="Screenshot of an LLM response after a filter is added.":::
+```
+The NASA Earth book showcases various geographic and environmental features of Earth through satellite imagery, highlighting remarkable landscapes and natural phenomena. 
+
+- It features extraordinary views like the Holuhraun Lava Field in Iceland, captured by Landsat 8 during an eruption in 2014, with false-color images illustrating different elements such as ice, steam, sulfur dioxide, and fresh lava ([source](page-43.pdf)).
+- Other examples include the North Patagonian Icefield in South America, depicted through clear satellite images showing glaciers and their changes over time ([source](page-147.pdf)).
+- It documents melt ponds in the Arctic, exploring their effects on ice melting and heat absorption ([source](page-153.pdf)).
+  
+Overall, the book uses satellite imagery to give insights into Earth's dynamic systems and natural changes.
+```
 
 ## Change the inputs
 
-Increasing or decreasing the number of inputs to the LLM can have a large effect on the response. Try running the same query again after setting `top=3`. When you increase the inputs, the model returns different results each time, even if the query doesn't change. 
+Increasing or decreasing the number of inputs to the LLM can have a large effect on the response. Try running the same query again after setting `top=8`. When you increase the inputs, the model returns different results each time, even if the query doesn't change. 
+
+Here's one example of what the model returns after increasing the inputs to 8.
 
-Here's one example of what the model returns after increasing the inputs to 3.
+```
+The NASA Earth book features a range of satellite images capturing various natural phenomena across the globe. These include:
+
+- The Holuhraun Lava Field in Iceland documented by Landsat 8 during a 2014 volcanic eruption (Source: page-43.pdf).
+- The North Patagonian Icefield in South America, highlighting glacial landscapes captured in a rare cloud-free view in 2017 (Source: page-147.pdf).
+- The impact of melt ponds on ice sheets and sea ice in the Arctic, with images from an airborne research campaign in Alaska during July 2014 (Source: page-153.pdf).
+- Sea ice formations at Shikotan, Japan, and other notable geographic features in various locations recorded by different Landsat missions (Source: page-168.pdf).
 
-:::image type="content" source="media/tutorial-rag-solution/chat-results-2.png" alt-text="Screenshot of an LLM response to a simple question using a larger result set.":::
+Summary: The book showcases satellite images of diverse Earth phenomena, such as volcanic eruptions, icefields, and sea ice, to provide insights into natural processes and landscapes.
+```
 
-Because the model is bound to just the grounding data, the answer becomes more expansive as you increase size of the input. You can use relevance tuning to potentially generate more focused answers.
+Because the model is bound to the grounding data, the answer becomes more expansive as you increase size of the input. You can use relevance tuning to potentially generate more focused answers.
 
 ## Change the prompt
 
 You can also change the prompt to control the format of the output, tone, and whether you want the model to supplement the answer with its own training data by changing the prompt. 
 
-Here's another example of LLM output if we refocus the prompt on fact collection.
+Here's another example of LLM output if we refocus the prompt on identifying locations for scientific study.
 
 ```python
 # Provide instructions to the model
 GROUNDED_PROMPT="""
-You are an AI assistant that helps users pull facts from the source material.
+You are an AI assistant that helps scientists identify locations for future study.
 Answer the query cocisely, using bulleted points.
 Answer ONLY with the facts listed in the list of sources below.
 If there isn't enough information below, say you don't know.
@@ -178,25 +221,33 @@ Sources:\n{sources}
 """
 ```
 
-Output from changing just the prompt, retaining `top=3` from the previous query, might look like this example. 
+Output from changing just the prompt, otherwise retaining all aspects of the previous query, might look like this example. 
 
-:::image type="content" source="media/tutorial-rag-solution/chat-results-3.png" alt-text="Screenshot of an LLM response to a change in prompt composition.":::
+```
+The NASA Earth book appears to showcase various locations on Earth captured through satellite imagery, highlighting natural phenomena and geographic features. For instance, the book includes:
+
+- The Holuhraun Lava Field in Iceland, detailing volcanic activity and its observation via Landsat 8.
+- The North Patagonian Icefield in South America, covering its glaciers and changes over time as seen by Landsat 8.
+- Melt ponds in the Arctic and their impacts on the heat balance and ice melting.
+- Iceberg A-56 in the South Atlantic Ocean and its interaction with cloud formations.
 
-In this tutorial, assessing the quality of the answer is subjective, but since the model is working with the same results as the previous query, the answer feels less focused, and some bullets seem only tangential to a question about the surface area of water on earth. Let's try the request one last time, increasing `top=10`.
+(Source: page-43.pdf, page-147.pdf, page-153.pdf, page-39.pdf)
+```
 
-:::image type="content" source="media/tutorial-rag-solution/chat-results-4.png" alt-text="Screenshot of an LLM response to a simple question using top set to 10.":::
+> [!TIP]
+> If you're continuing on with the tutorial, remember to restore the prompt to its previous value (`You are an AI assistant that helps users learn from the information found in the source material`).
 
-There are several observations to note:
+Changing parameters and prompts affects the response from the LLM. As you explore on your own, keep the following tips in mind:
 
-- Raising the `top` value can exhaust available quota on the model. If there's no quota, an error message is returned.
+- Raising the `top` value can exhaust available quota on the model. If there's no quota, an error message is returned or the model might return "I don't know".
 
-- Raising the `top` value doesn't necessarily improve the outcome. The answer isn't the same as `top=3`, but it's similar. This observation underscores an important point that might be counter-intuitive to expections. Throwing more content at an LLM doesn't always yield better results.
+- Raising the `top` value doesn't necessarily improve the outcome. In testing with top, we sometimes notice that the answers aren't dramatically better.
 
 - So what might help? Typically, the answer is relevance tuning. Improving the relevance of the search results from Azure AI Search is usually the most effective approach for maximizing the utility of your LLM.
 
 In the next series of tutorials, the focus shifts to maximizing relevance and optimizing query performance for speed and concision. We revisit the schema definition and query logic to implement relevance features, but the rest of the pipeline and models remain intact.
 
-<!-- In this tutorial, learn how to send queries and prompts to a chat model for generative search. The queries that you create for a conversational search are built for prompts and the orchestration layer. The query response is fed into message prompts sent to an LLM like GPT-35-Turbo.
+<!-- In this tutorial, learn how to send queries and prompts to a chat model for generative search. The queries that you create for a conversational search are built for prompts and the orchestration layer. The query response is fed into message prompts sent to an LLM like gpt-4o.
 
 Objective:
 
@@ -230,7 +281,7 @@ Tasks:
 - H2 Query using vectors and text-to-vector conversion at query time (not sure what the code looks like for this)
 - H2 Query parent-child two indexes (unclear how to do this, Carey said query on child, do a lookup query on parent) -->
 
-<!-- ## Next step
+## Next step
 
 > [!div class="nextstepaction"]
-> [Maximize relevance](tutorial-rag-build-solution-maximize-relevance.md) -->
+> [Maximize relevance](tutorial-rag-build-solution-maximize-relevance.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGチュートリアルにおけるLLMを使用した検索の更新"
}
```

### Explanation
この変更では、`articles/search/tutorial-rag-build-solution-query.md`ファイルに対して修正が加えられました。具体的には、86行が追加され、35行が削除され、合計121行の変更が行われています。主な変更点は次の通りです。

1. **タイトルの修正**: タイトルが大文字から小文字に変更され、統一感が持たせられています。
2. **日付の更新**: 最終更新日が2024年10月3日から2024年10月4日に修正されました。
3. **モデルのバージョン変更**: 使用するAzure OpenAIモデルが`gpt-35-turbo`から`gpt-4o`に変更され、最新の技術に合わせた情報が反映されています。
4. **クエリ内容の強化**: 新しいクエリの例やその意味がより明確に説明され、複数の入力を使用することでLLMの応答が改善されることが示されています。
5. **フィルタ機能の追加**: `locations`フィールドを使用して、検索結果にフィルタを追加する方法が詳述されています。これにより、より具体的な検索結果を得られるようになっています。

全体として、これらの更新は、Azure AI SearchとLLMのインテグレーションを強化し、ユーザーがより効果的に情報を検索・取得できるよう促進することを目的としています। 具体的なクエリサンプルやフィルタリング手法の説明が強化され、実用的な情報が提供されています。

## articles/search/tutorial-rag-build-solution.md{#item-c7eca4}

<details>
<summary>Diff</summary>
````diff
@@ -8,17 +8,17 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: overview
-ms.date: 09/12/2024
+ms.date: 10/04/2024
 
 ---
 
 # How to build a RAG solution using Azure AI Search
 
-This tutorial series demonstrates a pattern for building RAG solutions on Azure AI Search. It covers the components built in Azure AI Search, dependencies, optimizations, and deployment tasks.
+This tutorial series demonstrates a pattern for building RAG solutions on Azure AI Search. It covers the components built in Azure AI Search, dependencies, and optimizations for maximizing relevance and minimizing costs.
 
-Sample data is a [collection of PDFs](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth_book_2019_text_pages) uploaded to Azure Storage.
+Sample data is a [collection of PDFs](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth_book_2019_text_pages) uploaded to Azure Storage. The content is from [NASA's Earth free e-book](https://www.nasa.gov/ebooks/earth/).
 
-Sample code can be found in [this Python notebook](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Tutorial-RAG/Tutorial-rag.ipynb), but we recommend using this series for context, insights, and for exploring alternative approaches.
+Sample code can be found in [this Python notebook](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Tutorial-RAG/Tutorial-rag.ipynb), but we recommend using the articles in this series for context, insights, and for exploring alternative approaches.
 
 ## Exercises in this series
 
@@ -34,15 +34,15 @@ Sample code can be found in [this Python notebook](https://github.com/Azure-Samp
 
 - Minimize storage and costs
 
-- Deploy and secure an app
+<!-- - Deploy and secure an app -->
 
 We omitted a few aspects of a RAG pattern to reduce complexity:
 
-- No management of chat history and context. Chat history is typically stored and managed separately from your grounding data, which means extra steps and code. This tutorial assumes atomic question and answers from the LLM.
+- No management of chat history and context. Chat history is typically stored and managed separately from your grounding data, which means extra steps and code. This tutorial assumes atomic question and answers from the LLM and the default LLM experience.
 
 - No per-user user security over results (what we refer to as "security trimming"). For more information and resources, start with [Security trimming](search-security-trimming-for-azure-search.md) and make sure to review the links at the end of the article.
 
-This series covers the fundamentals of RAG solution development. Once you understand the basics, continue with accelerators and other code samples that provide more abstraction or are otherwise better suited for production environments and more complex workloads.
+This series covers the fundamentals of RAG solution development. Once you understand the basics, continue with [accelerators](resource-tools.md) and other [code samples](https://github.com/Azure/azure-search-vector-samples) that provide more abstraction or are otherwise better suited for production environments and more complex workloads.
 
 ## Why use Azure AI Search for RAG?
 
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
この変更では、`articles/search/tutorial-rag-build-solution.md`ファイルに対して修正が加えられました。具体的には、7行が追加され、7行が削除され、合計14行の変更が行われています。主な変更点は次の通りです。

1. **日付の更新**: 最終更新日が2024年9月12日から2024年10月4日に修正されました。
2. **コンテンツの明確化**: `依存関係`に関する説明が少し具体化され、コストを最小限に抑える最適化の重要性が強調されています。
3. **データソースの明示化**: サンプルデータに関する説明文にNASAの地球無料電子書籍のリンクが追加され、データの出所が明確になっています。
4. **コードサンプルの文言修正**: コードサンプルについての文言が修正され、記事シリーズがより有用であることが強調されています。
5. **アプリケーションの展開に関する内容のコメント化**: `アプリを展開し、セキュリティを確保する`という項目がコメント化され、目立たなくなっています。

全体として、この更新は、Azure AI Searchを使用したRAGソリューションの開発をより分かりやすくし、最新の情報を反映することを目的としています。また、リソースへのリンクが強調され、読者がさらに深い理解を得られるよう配慮されています。


