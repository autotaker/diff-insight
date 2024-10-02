---
date: '2024-10-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0a8084e...MicrosoftDocs:b0599a2
summary: この修正は、検索インデックスおよびRAGソリューションに関するチュートリアルを最新の情報やベストプラクティスに更新することを目的としています。新機能として、Azure
  SDKの最新インポートステートメントを含むPythonコードの追加や、認証方法の明確化が行われています。重大な破壊的変更はありませんが、一部の変数名や引数名が変更されているため、注意が必要です。その他にも、日付の更新、誤字の修正、役割に関する説明が充実され、ユーザーエクスペリエンスが向上しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0a8084e...MicrosoftDocs:b0599a2){target="_blank"}

# ハイライト
本コードの修正は、主に検索インデックスの文書やRAG（Retrieval-Augmented Generation）ソリューションに関するチュートリアルを最新の情報やベストプラクティスに合わせて更新することを目的としています。新しい機能や既存の機能に対する重大な変更はなく、微調整や改善が中心です。

## 新機能
- RAGソリューションに関するチュートリアル文書の一部で、新しいPythonコードが追加されることで、Azure SDKの最新インポートステートメントが含まれるようになりました。
- 認証方法の明確化と統一が行われ、ユーザーが最新の認証手法を使用する助けとなっています。

## 破壊的変更
- 重大な破壊的変更は含まれていませんが、一部の変数名や引数名が変更されているため、既存のコードに依存している場合は注意が必要です。

## その他の更新
- 日付の更新、誤字の修正、変数名や引数名の改善が含まれます。
- 役割に関する説明や、APIキーに代わる新しい認証方法が追記されました。

# インサイト
このドキュメントの修正は、細かい点ではありますが、ユーザーエクスペリエンスを向上させるための重要なステップです。以下、各ドキュメントごとに変更点とその意義について詳しく解説します。

### 検索インデックス作成方法の文書修正
検索インデックスに関する文書のノートセクションでの誤字「searchin」を「searching」に修正することで、情報の正確性が向上しました。これにより、誤解を避け、ユーザーにとっての検索機能の理解が深まります。

### RAGソリューションのインデックススキーマに関するチュートリアルの更新
主な変更点として、日付の更新、Azure SDK関連のインポート追加、変数名や引数の修正が挙げられます。これにより、最新のAzure認証方法が明示的に示され、初心者でも理解しやすくなっています。特に、`AzureOpenAIVectorizer`や`SearchIndexClient`の使用方法に関する修正は、クリアな文脈を提供し、コードの実装がよりスムーズに行えるようになっています。

### RAGソリューションモデルに関するチュートリアルの情報更新
この文書では、日付の更新と役割に関する説明が強化されました。特に、「Owner」役割から「OwnerまたはUser Access Administrator」役割に変更されたことで、モデルへの接続に必要な役割についての理解が深まりました。また、「役割を作成できない場合にはAPIキーを使用できる」という新情報の追加も、ユーザーに多様なオプションを提供しています。

### RAGソリューションパイプラインに関するチュートリアルの更新
このチュートリアルの更新では、日付の修正、新しいコードの追加、既存コードの改善が行われました。`SearchIndexClient`や`SearchIndexerClient`を使用する際の認証方法の統一や変数名の変更は、コードの可読性と一貫性を向上させています。また、エンティティ認識スキルに関する詳細情報の追記やAzureのアクセス権に関する説明の充実も見逃せません。

### RAGソリューションクエリのチュートリアル内容の更新
日付の変更やコメントの調整、認証方法の改善が行われました。特に、役割ベースのアクセスコントロールを利用する場合にAPIキーを削除する指示が追加され、セキュリティが強化されています。また、OpenAIクライアントの設定についても、トークンプロバイダーを通じた新しい認証方式への切り替えが示されており、最新の認証手法に対応するようになっています。

以上の変更を通じて、ドキュメントの正確さ、セ

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-how-to-create-search-index.md](#item-c4ff31) | minor update | 検索インデックス作成方法の文書修正 | modified | 1 | 1 | 2 | 
| [tutorial-rag-build-solution-index-schema.md](#item-9a17ca) | minor update | RAGソリューションのインデックススキーマに関するチュートリアルの更新 | modified | 25 | 8 | 33 | 
| [tutorial-rag-build-solution-models.md](#item-6796c9) | minor update | RAGソリューションモデルに関するチュートリアルの情報更新 | modified | 2 | 2 | 4 | 
| [tutorial-rag-build-solution-pipeline.md](#item-25ce01) | minor update | RAGソリューションパイプラインに関するチュートリアルの更新 | modified | 54 | 31 | 85 | 
| [tutorial-rag-build-solution-query.md](#item-93965f) | minor update | RAGソリューションクエリのチュートリアル内容の更新 | modified | 8 | 9 | 17 | 


# Modified Contents
## articles/search/search-how-to-create-search-index.md{#item-c4ff31}

<details>
<summary>Diff</summary>
````diff
@@ -77,7 +77,7 @@ Use this checklist to assist the design decisions for your search index.
    For hyphenated strings or special characters, consider [specialized analyzers](index-add-custom-analyzers.md#built-in-analyzers). One example is [keyword](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/core/KeywordAnalyzer.html) that treats the entire contents of a field as a single token. This behavior is useful for data like zip codes, IDs, and some product names. For more information, see [Partial term search and patterns with special characters](search-query-partial-matching.md).
 
 > [!NOTE]
-> Full text search is conducted over terms that are tokenized during indexing. If your queries fail to return the results you expect, [test for tokenization](/rest/api/searchservice/indexes/analyze) to verify the string you're searchin for actually exists. You can try different analyzers on strings to see how tokens are produced for various analyzers.
+> Full text search is conducted over terms that are tokenized during indexing. If your queries fail to return the results you expect, [test for tokenization](/rest/api/searchservice/indexes/analyze) to verify the string you're searching for actually exists. You can try different analyzers on strings to see how tokens are produced for various analyzers.
 
 ## Create an index
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックス作成方法の文書修正"
}
```

### Explanation
この変更は、検索インデックスに関する文書の中のテキストの微調整を目的としたものです。具体的には、7行目のノートセクションで「searchin」という誤字を「searching」に訂正しています。この修正により、文章の正確さと理解しやすさが向上しました。また、全体としての流れや意味に影響はありませんが、ユーザーにとっては検索機能の使用方法についての理解が深まるでしょう。この文書は、検索インデックスを効率的に作成する方法を説明しているため、重要な情報が正確に伝わることが求められます。

## articles/search/tutorial-rag-build-solution-index-schema.md{#item-9a17ca}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: tutorial
-ms.date: 09/12/2024
+ms.date: 10/01/2024
 
 ---
 
@@ -111,8 +111,25 @@ A minimal index for LLM is designed to store chunks of content. It typically inc
    The schema also includes a `locations` field for storing generated content that's created by the [indexing pipeline](tutorial-rag-build-solution-pipeline.md).
 
    ```python
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
+        SearchIndex
+    )
+    
+    credential = DefaultAzureCredential()
+    
+    # Create a search index  
     index_name = "py-rag-tutorial-idx"
-    index_client = SearchIndexClient(endpoint=AZURE_SEARCH_SERVICE, credential=AZURE_SEARCH_CREDENTIAL)  
+    index_client = SearchIndexClient(endpoint=AZURE_SEARCH_SERVICE, credential=credential)  
     fields = [
         SearchField(name="parent_id", type=SearchFieldDataType.String),  
         SearchField(name="title", type=SearchFieldDataType.String),
@@ -131,20 +148,20 @@ A minimal index for LLM is designed to store chunks of content. It typically inc
             VectorSearchProfile(  
                 name="myHnswProfile",  
                 algorithm_configuration_name="myHnsw",  
-                vectorizer="myOpenAI",  
+                vectorizer_name="myOpenAI",  
             )
         ],  
         vectorizers=[  
             AzureOpenAIVectorizer(  
-                name="myOpenAI",  
+                vectorizer_name="myOpenAI",  
                 kind="azureOpenAI",  
-                azure_open_ai_parameters=AzureOpenAIParameters(  
-                    resource_uri=AZURE_OPENAI_ACCOUNT,  
-                    deployment_id="text-embedding-ada-002",
+                parameters=AzureOpenAIVectorizerParameters(  
+                    resource_url=AZURE_OPENAI_ACCOUNT,  
+                    deployment_name="text-embedding-ada-002",
                     model_name="text-embedding-ada-002"
                 ),
             ),  
-        ],  
+        ], 
     )  
       
     # Create the search index
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションのインデックススキーマに関するチュートリアルの更新"
}
```

### Explanation
この変更は、RAG（Retrieval-Augmented Generation）ソリューションのインデックススキーマに関するチュートリアル文書のアップデートを含んでいます。主な修正点としては、日付の更新、Pythonコードの追加、および変数名や引数の修正が挙げられます。具体的には、日付を2024年9月12日から2024年10月1日へ変更し、Azure SDKに関連する新しいモジュールのインポートを追加しています。これにより、ドキュメントの最新性が保たれ、Azureの認証方法が明示的に示されることで、初心者でもより簡単に理解できる内容となっています。特に、`AzureOpenAIVectorizer`や`SearchIndexClient`の使用方法が修正され、クリアな文脈の中でコードが求められる実装を示しており、ユーザーにとっての有用性が向上しています。

## articles/search/tutorial-rag-build-solution-models.md{#item-6796c9}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.author: heidist
 ms.service: cognitive-search
 ms.topic: tutorial
 ms.custom: references_regions
-ms.date: 09/30/2024
+ms.date: 10/01/2024
 
 ---
 
@@ -32,7 +32,7 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
 - The Azure portal, used to deploy models and configure role assignments in the Azure cloud.
 
-- An **Owner** role on your Azure subscription, necessary for creating role assignments. You use at least three Azure resources in this tutorial. The connections are authenticated using Microsoft Entra ID, which requires the ability to create roles. Role assignments for connecting to models are documented in this article.
+- An **Owner** or **User Access Administrator** role on your Azure subscription, necessary for creating role assignments. You use at least three Azure resources in this tutorial. The connections are authenticated using Microsoft Entra ID, which requires the ability to create roles. Role assignments for connecting to models are documented in this article. If you can't create roles, you can use [API keys](search-security-api-keys.md) instead.
 
 - A model provider, such as [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource), Azure AI Vision via an [Azure AI multi-service account](/azure/ai-services/multi-service-resource), or [Azure AI Studio](https://ai.azure.com/).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションモデルに関するチュートリアルの情報更新"
}
```

### Explanation
この変更は、RAGソリューションモデルに関するチュートリアル文書の内容を更新したものです。主な修正点は、日付の変更と役割に関する説明の強化です。具体的には、日付を2024年9月30日から2024年10月1日に更新し、Azureサブスクリプションに必要な役割に関して「Owner」役割から「OwnerまたはUser Access Administrator」役割に変更しています。この変更は、ユーザーがモデルへの接続に必要な役割についての理解を深める手助けとなり、さらに「役割を作成できない場合にはAPIキーを使用できる」との新しい情報が追加されたことで、より多くの選択肢を提案しています。この文書は、Azure環境でのモデルのデプロイと役割の設定に関する実用的なガイダンスを提供しており、更新によりその内容が最新の実践を反映するものとなっています。

## articles/search/tutorial-rag-build-solution-pipeline.md{#item-25ce01}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: tutorial
-ms.date: 09/23/2024
+ms.date: 10/01/2024
 
 ---
 
@@ -19,7 +19,7 @@ Learn how to build an automated indexing pipeline for a RAG solution on Azure AI
 In this tutorial, you:
 
 > [!div class="checklist"]
-> - Provide the index schema from the previous tutorial 
+> - Provide the index schema from the previous tutorial
 > - Create a data source connection
 > - Create an indexer
 > - Create a skillset that chunks, vectorizes, and recognizes entities
@@ -53,8 +53,25 @@ Open or create a Jupyter notebook (`.ipynb`) in Visual Studio Code to contain th
 Let's start with the index schema from the [previous tutorial](tutorial-rag-build-solution-index-schema.md). It's organized around vectorized and nonvectorized chunks. It includes a `locations` field that stores AI-generated content created by the skillset.  
 
 ```python
+from azure.identity import DefaultAzureCredential
+from azure.identity import get_bearer_token_provider
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import (
+    SearchField,
+    SearchFieldDataType,
+    VectorSearch,
+    HnswAlgorithmConfiguration,
+    VectorSearchProfile,
+    AzureOpenAIVectorizer,
+    AzureOpenAIVectorizerParameters,
+    SearchIndex
+)
+
+credential = DefaultAzureCredential()
+
+# Create a search index  
 index_name = "py-rag-tutorial-idx"
-index_client = SearchIndexClient(endpoint=AZURE_SEARCH_SERVICE, credential=AZURE_SEARCH_CREDENTIAL)  
+index_client = SearchIndexClient(endpoint=AZURE_SEARCH_SERVICE, credential=credential)  
 fields = [
     SearchField(name="parent_id", type=SearchFieldDataType.String),  
     SearchField(name="title", type=SearchFieldDataType.String),
@@ -63,7 +80,7 @@ fields = [
     SearchField(name="chunk", type=SearchFieldDataType.String, sortable=False, filterable=False, facetable=False),  
     SearchField(name="text_vector", type=SearchFieldDataType.Collection(SearchFieldDataType.Single), vector_search_dimensions=1536, vector_search_profile_name="myHnswProfile")
     ]  
-    
+  
 # Configure the vector search configuration  
 vector_search = VectorSearch(  
     algorithms=[  
@@ -73,23 +90,23 @@ vector_search = VectorSearch(
         VectorSearchProfile(  
             name="myHnswProfile",  
             algorithm_configuration_name="myHnsw",  
-            vectorizer="myOpenAI",  
+            vectorizer_name="myOpenAI",  
         )
     ],  
     vectorizers=[  
         AzureOpenAIVectorizer(  
-            name="myOpenAI",  
+            vectorizer_name="myOpenAI",  
             kind="azureOpenAI",  
-            azure_open_ai_parameters=AzureOpenAIParameters(  
-                resource_uri=AZURE_OPENAI_ACCOUNT,  
-                deployment_id="text-embedding-ada-002",
+            parameters=AzureOpenAIVectorizerParameters(  
+                resource_url=AZURE_OPENAI_ACCOUNT,  
+                deployment_name="text-embedding-ada-002",
                 model_name="text-embedding-ada-002"
             ),
         ),  
-    ],  
+    ], 
 )  
-    
-# Create the search index on Azure AI Search
+  
+# Create the search index
 index = SearchIndex(name=index_name, fields=fields, vector_search=vector_search)  
 result = index_client.create_or_update_index(index)  
 print(f"{result.name} created")  
@@ -101,11 +118,11 @@ In this step, set up the sample data and a connection to Azure Blob Storage. The
 
 The original ebook is large, over 100 pages and 35 MB in size. We broke it up into smaller PDFs, one per page of text, to stay under the [API payload limit](search-limits-quotas-capacity.md#api-request-limits) of 16 MB per API call and also the [AI enrichment data limits](search-limits-quotas-capacity.md#data-limits-ai-enrichment). For simplicity, we omit image vectorization for this exercise.
 
-1. Sign in to the Azure portal and find your Azure Storage account.
+1. Sign in to the [Azure portal](https://portal.azure.com) and find your Azure Storage account.
 
 1. Create a container and upload the PDFs from [earth_book_2019_text_pages](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth_book_2019_text_pages).
 
-1. Make sure Azure AI Search has **Storage Blob Data Reader** permissions on the resource.
+1. Make sure Azure AI Search has [**Storage Blob Data Reader** permissions](/azure/role-based-access-control/role-assignments-portal) on the resource.
 
 1. Next, in Visual Studio Code, define an indexer data source that provides connection information during indexing.
 
@@ -117,8 +134,8 @@ The original ebook is large, over 100 pages and 35 MB in size. We broke it up in
     )
     
     # Create a data source 
-    indexer_client = SearchIndexerClient(endpoint=AZURE_SEARCH_SERVICE, credential=AZURE_SEARCH_CREDENTIAL)
-    container = SearchIndexerDataContainer(name="nasa-ebook-pdfs-all")
+    indexer_client = SearchIndexerClient(endpoint=AZURE_SEARCH_SERVICE, credential=credential)
+    container = SearchIndexerDataContainer(name="nasa-ebooks-pdfs-all")
     data_source_connection = SearchIndexerDataSourceConnection(
         name="py-rag-tutorial-ds",
         type="azureblob",
@@ -130,11 +147,15 @@ The original ebook is large, over 100 pages and 35 MB in size. We broke it up in
     print(f"Data source '{data_source.name}' created or updated")
     ```
 
+If you set up a managed identity for Azure AI Search for the connection, the connection string includes a `ResourceId=` suffix. It should look similar to the following example: `"ResourceId=/subscriptions/FAKE-SUBCRIPTION=ID/resourceGroups/FAKE-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/FAKE-ACCOUNT;"`
+
 ## Create a skillset
 
 Skills are the basis for integrated data chunking and vectorization. At a minimum, you want a Text Split skill to chunk your content, and an embedding skill that create vector representations of your chunked content.
 
-In this skillset, an extra skill is used to create structured data in the index. The Entity Recognition skill is used to identify locations, which can range from proper names to generic references, such as "ocean" or "mountain". Having structured data gives you more options for creating interesting queries and boosting relevance.
+In this skillset, an extra skill is used to create structured data in the index. The [Entity Recognition skill](cognitive-search-skill-entity-recognition-v3.md) is used to identify locations, which can range from proper names to generic references, such as "ocean" or "mountain". Having structured data gives you more options for creating interesting queries and boosting relevance.
+
+The AZURE_AI_MULTISERVICE_KEY is needed even if you're using role-based access control. Azure AI Search uses the key for billing purposes and it's required unless your workloads stay under the free limit.
 
 ```python
 from azure.search.documents.indexes.models import (
@@ -143,7 +164,7 @@ from azure.search.documents.indexes.models import (
     OutputFieldMappingEntry,
     AzureOpenAIEmbeddingSkill,
     EntityRecognitionSkill,
-    SearchIndexerIndexProjections,
+    SearchIndexerIndexProjection,
     SearchIndexerIndexProjectionSelector,
     SearchIndexerIndexProjectionsParameters,
     IndexProjectionMode,
@@ -171,8 +192,8 @@ split_skill = SplitSkill(
 embedding_skill = AzureOpenAIEmbeddingSkill(  
     description="Skill to generate embeddings via Azure OpenAI",  
     context="/document/pages/*",  
-    resource_uri=AZURE_OPENAI_ACCOUNT,  
-    deployment_id="text-embedding-ada-002",  
+    resource_url=AZURE_OPENAI_ACCOUNT,  
+    deployment_name="text-embedding-ada-002",  
     model_name="text-embedding-ada-002",
     dimensions=1536,
     inputs=[  
@@ -196,7 +217,7 @@ entity_skill = EntityRecognitionSkill(
     ]
 )
   
-index_projections = SearchIndexerIndexProjections(  
+index_projections = SearchIndexerIndexProjection(  
     selectors=[  
         SearchIndexerIndexProjectionSelector(  
             target_index_name=index_name,  
@@ -205,7 +226,7 @@ index_projections = SearchIndexerIndexProjections(
             mappings=[  
                 InputFieldMappingEntry(name="chunk", source="/document/pages/*"),  
                 InputFieldMappingEntry(name="text_vector", source="/document/pages/*/text_vector"),
-                InputFieldMappingEntry(name="locations", source="/document/pages/*/locations"),
+                InputFieldMappingEntry(name="locations", source="/document/pages/*/locations"),  
                 InputFieldMappingEntry(name="title", source="/document/metadata_storage_name"),  
             ],  
         ),  
@@ -223,13 +244,13 @@ skillset = SearchIndexerSkillset(
     name=skillset_name,  
     description="Skillset to chunk documents and generating embeddings",  
     skills=skills,  
-    index_projections=index_projections,
+    index_projection=index_projections,
     cognitive_services_account=cognitive_services_account
 )
   
-client = SearchIndexerClient(endpoint=AZURE_SEARCH_SERVICE, credential=AZURE_SEARCH_CREDENTIAL)  
+client = SearchIndexerClient(endpoint=AZURE_SEARCH_SERVICE, credential=credential)  
 client.create_or_update_skillset(skillset)  
-print(f"{skillset.name} created")  
+print(f"{skillset.name} created")
 ```
 
 ## Create and run the indexer
@@ -261,24 +282,26 @@ indexer = SearchIndexer(
 )  
 
 # Create and run the indexer  
-indexer_client = SearchIndexerClient(endpoint=AZURE_SEARCH_SERVICE, credential=AZURE_SEARCH_CREDENTIAL)  
+indexer_client = SearchIndexerClient(endpoint=AZURE_SEARCH_SERVICE, credential=credential)  
 indexer_result = indexer_client.create_or_update_indexer(indexer)  
 
-print(f' {indexer_name} is created and running. Give the indexer a few minutes before running a query.')  
+print(f' {indexer_name} is created and running. Give the indexer a few minutes before running a query.')    
 ```
 
 ## Run a query to check results
 
 Send a query to confirm your index is operational. This request converts the text string "`where are the nasa headquarters located?`" into a vector for a vector search. Results consist of the fields in the select statement, some of which are printed as output.
 
+There's no chat or generative AI at this point. The results are verbatim content from your search index.
+
 ```python
 from azure.search.documents import SearchClient
 from azure.search.documents.models import VectorizableTextQuery
 
-# Hybrid Search
-query = "where are the nasa headquarters located?"  
+# Vector Search using text-to-vector conversion of the querystring
+query = "where are NASA's headquarters located?"  
 
-search_client = SearchClient(endpoint=AZURE_SEARCH_SERVICE, credential=AZURE_SEARCH_CREDENTIAL, index_name=index_name)
+search_client = SearchClient(endpoint=AZURE_SEARCH_SERVICE, credential=credential, index_name=index_name)
 vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=1, fields="text_vector", exhaustive=True)
   
 results = search_client.search(  
@@ -292,7 +315,7 @@ for result in results:
     print(f"Score: {result['@search.score']}")
     print(f"Title: {result['title']}")
     print(f"Locations: {result['locations']}")
-    print(f"Content: {result['chunk']}") 
+    print(f"Content: {result['chunk']}")
 ```
 
 This query returns a single match (`top=1`) consisting of the one chunk determined by the search engine to be the most relevant. Results from the query should look similar to the following example:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションパイプラインに関するチュートリアルの更新"
}
```

### Explanation
この変更は、RAGソリューションのパイプラインに関するチュートリアル文書を更新するものであり、主に日付の修正、新しいコードの追加、既存コードの改善が含まれています。具体的には、日付を2024年9月23日から2024年10月1日へ更新し、新しいAzure SDKのインポートステートメントを追加しています。

変更点の中には、`SearchIndexClient`や`SearchIndexerClient`を使用する際の認証方法の統一、変数や引数の名称変更（例えば、`vectorizer`を`vectorizer_name`に変更）などがあり、全体的にコードの可読性と一貫性が向上しています。さらに、スキルセットの部分では、エンティティ認識スキルに関する詳細情報を追記し、Azureのアクセス権に関する説明も充実させています。

全体として、この更新はサンプルコードを最新のベストプラクティスに合わせて調整し、初めてのユーザーでも理解しやすくなるような具体的な情報を提供することで、RAGソリューションの実装をよりスムーズに進められるようになっています。

## articles/search/tutorial-rag-build-solution-query.md{#item-93965f}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: tutorial
-ms.date: 09/12/2024
+ms.date: 10/01/2024
 
 ---
 
@@ -46,10 +46,10 @@ You're setting up two clients, so you need permissions on both resources. We use
 
 ```python
 # Set endpoints and API keys for Azure services
-AZURE_SEARCH_SERVICE: str = "PUT YOUR SEARCH SERVICE URL HERE"
-AZURE_SEARCH_KEY: str = "PUT YOUR SEARCH SERVICE ADMIN KEY HERE"
-AZURE_OPENAI_ACCOUNT: str = "PUT YOUR AZURE OPENAI ACCOUNT URL HERE"
-AZURE_OPENAI_KEY: str = "PUT YOUR AZURE OPENAI KEY HERE"
+AZURE_SEARCH_SERVICE: str = "PUT YOUR SEARCH SERVICE ENDPOINT HERE"
+# AZURE_SEARCH_KEY: str = "DELETE IF USING ROLES, OTHERWISE PUT YOUR SEARCH SERVICE ADMIN KEY HERE"
+AZURE_OPENAI_ACCOUNT: str = "PUR YOUR AZURE OPENAI ENDPOINT HERE"
+# AZURE_OPENAI_KEY: str = "DELETE IF USING ROLES, OTHERWISE PPUT YOUR AZURE OPENAI KEY HERE"
 ```
 
 ## Example script for prompt and query
@@ -59,22 +59,21 @@ Here's the Python script that instantiates the clients, defines the prompt, and
 ```python
 # Import libraries
 from azure.search.documents import SearchClient
-from azure.core.credentials import AzureKeyCredential
 from openai import AzureOpenAI
 
-# Set up clients and specify the chat model
+token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")
 openai_client = AzureOpenAI(
      api_version="2024-06-01",
      azure_endpoint=AZURE_OPENAI_ACCOUNT,
-     api_key=AZURE_OPENAI_KEY
+     azure_ad_token_provider=token_provider
  )
 
 deployment_name = "gpt-35-turbo"
 
 search_client = SearchClient(
      endpoint=AZURE_SEARCH_SERVICE,
      index_name=index_name,
-     credential=AZURE_SEARCH_CREDENTIAL
+     credential=credential
  )
 
 # Provide instructions to the model
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションクエリのチュートリアル内容の更新"
}
```

### Explanation
この変更は、RAGソリューションのクエリに関するチュートリアル文書を更新したもので、主に日付の修正、コメントの調整、認証方法の改善が含まれています。日付は2024年9月12日から2024年10月1日に変更されました。

具体的な内容としては、Azureサービス用のエンドポイントやAPIキーに関する記載が明確化され、例えば「PUT YOUR SEARCH SERVICE URL HERE」といったプレースホルダーが「PUT YOUR SEARCH SERVICE ENDPOINT HERE」と修正されています。また、APIキーの使用に関しても、役割ベースのアクセスコントロールを利用する場合はキーを削除するように指示が追加されました。

さらに、OpenAIクライアントの設定において、従来のAPIキーの使用から、トークンプロバイダーを通じた認証方式への切り替えが示されています。これによって、セキュリティが向上し、最新の認証手法に対応する内容となっています。

全体として、この更新はコードの正確さとセキュリティを向上させ、ユーザーがよりスムーズにRAGソリューションを実装できるようにすることを目的としています。


