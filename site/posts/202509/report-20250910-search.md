---
date: '2025-09-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:501869d...MicrosoftDocs:bf48e40
summary: この差分では、複数のドキュメントファイルに多数の小規模な変更が行われ、特に新機能や改善が追加されました。主な新機能として、JavaでAzure Searchのベクトル検索を利用するためのガイドラインと、Javaクイックスタートへのリンクが追加され、Javaユーザー向けの情報が強化されました。大きな破壊的変更はなく、主にリンクの修正やフォーマットの改善が行われました。この更新の目的は、Azure
  Searchのユーザビリティを向上させることで、特にJava開発者にとって有用なリソースとなっています。また、ドキュメントの整合性を保ち、情報への迅速なアクセスを可能にする改善も行われています。各ドキュメントは、特定の開発者コミュニティにターゲットを絞り、開発をスムーズにすることを意図しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:501869d...MicrosoftDocs:bf48e40){target="_blank"}

# ハイライト

この差分では、複数のドキュメントファイルに対する多数の小規模な変更が行われましたが、特筆すべきはいくつかの新機能と改善です。

## 新機能
- **Java用ベクトル検索入門ガイドの追加**：JavaでAzure Searchのベクトル検索を利用するための詳細なガイドラインが新たに追加されました。
- **Javaクイックスタートへのリンク追加**：ベクトル検索ガイドにJava関連のリンクが追加され、Javaユーザー向けの情報アクセスが改善されました。

## ブレイキングチェンジ
特に大きな破壊的変更は見当たりません。多くの変更はリンクの修正やフォーマットの改善に留まります。

## その他の更新
- 複数のリンクが絶対パスから相対パスに変更されました。
- データサンプルリンクの拡張子が大文字から小文字に変更され、一貫性が向上しました。
- セマンティックランカーガイドやベクトル検索ガイドの内容の修正が行われ、出力形式の一貫性が向上しました。

# 洞察

この更新は、特にAzure Searchのユーザビリティを高めることを目的とした小規模な改良が中心です。特にJava用のガイドが新たに追加されたことは、Javaを使用する開発者にとって非常に有用です。このガイドラインは、Azure Searchのベクトル検索機能をJava環境でどのように実装し、活用できるのかをステップバイステップで理解するための強力なリソースとなります。

他の記載の改善も文書の整合性を保ち、ユーザーが必要な情報に迅速にアクセスできることを支援するものです。たとえば、リンクの相対パスへの変更は、サイト構造の変更にもかかわらずリンク切れのリスクを減少させます。

各ドキュメントは特定の開発者コミュニティ（Python、JavaScript、Java）にターゲティングされており、それぞれのプラットフォームでの開発をスムーズにすることを意図しています。このようにガイドラインの具体性と一貫性を向上させることは、開発者がAzure Searchの高度な機能をより適切に利用する助けとなるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-create-custom-skill-example.md](#item-24ed00) | minor update | カスタムスキルの例のリンク更新 | modified | 1 | 1 | 2 | 
| [full-text-python.md](#item-9bba1c) | minor update | ホテルデータサンプルのリンク修正 | modified | 1 | 1 | 2 | 
| [search-get-started-vector-java.md](#item-a3db97) | new feature | Java用のベクトル検索入門ガイドの追加 | added | 1483 | 0 | 1483 | 
| [search-get-started-vector-javascript.md](#item-d0387c) | minor update | JavaScript用のベクトル検索入門ガイドの修正 | modified | 34 | 31 | 65 | 
| [semantic-ranker-java.md](#item-93a05a) | minor update | Java用セマンティックランカーガイドの修正 | modified | 3 | 3 | 6 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | 情報取得拡張生成の概要の修正 | modified | 1 | 1 | 2 | 
| [search-get-started-vector.md](#item-4984d9) | new feature | Javaクイックスタートへのリンク追加 | modified | 6 | 0 | 6 | 
| [search-howto-index-cosmosdb.md](#item-568fab) | minor update | ファイル名の表記修正 | modified | 2 | 2 | 4 | 
| [search-howto-indexing-azure-tables.md](#item-7655b0) | minor update | サンプルデータリポジトリのリンク修正 | modified | 1 | 1 | 2 | 
| [search-region-support.md](#item-25b0f1) | minor update | マレーシア西部のサポート状況の調整 | modified | 1 | 1 | 2 | 
| [search-security-overview.md](#item-6b3f1e) | minor update | セキュリティ関連のリンク修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/cognitive-search-create-custom-skill-example.md{#item-24ed00}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.custom:
 
 # Example: Create a custom skill using the Bing Entity Search API
 
-In this example, learn how to create a web API custom skill. This skill will accept locations, public figures, and organizations, and return descriptions for them. The example uses an [Azure Function](https://azure.microsoft.com/services/functions/) to wrap the [Bing Entity Search API](https://azure.microsoft.com/services/cognitive-services/bing-entity-search-api/) so that it implements the custom skill interface.
+In this example, learn how to create a web API custom skill. This skill will accept locations, public figures, and organizations, and return descriptions for them. The example uses an [Azure Function](https://azure.microsoft.com/services/functions/) to wrap the [Bing Entity Search API](/previous-versions/bing/search-apis/bing-entity-search/overview) so that it implements the custom skill interface.
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムスキルの例のリンク更新"
}
```

### Explanation
この変更では、`articles/search/cognitive-search-create-custom-skill-example.md` ファイルにおけるリンクが更新されています。具体的には、Bing Entity Search APIへのリンクが完全なURLから相対パス形式に変更されました。これにより、文書内のリンクがより適切に機能し、コンテンツの更新や管理が容易になります。ファイル内では、他にも小さな修正が加えられていますが、主な変更点はこのリンクの更新です。このような変更は通常、リソースの可用性を向上させるために行われます。

## articles/search/includes/quickstarts/full-text-python.md{#item-9bba1c}

<details>
<summary>Diff</summary>
````diff
@@ -147,7 +147,7 @@ Each field also has a series of index attributes that specify whether Azure AI S
 
 ### Create a documents payload and upload documents
 
-Use an [index action](/python/api/azure-search-documents/azure.search.documents.models.indexaction) for the operation type, such as upload or merge-and-upload. Documents originate from the [HotelsData](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toAzureSearch.JSON) sample on GitHub.
+Use an [index action](/python/api/azure-search-documents/azure.search.documents.models.indexaction) for the operation type, such as upload or merge-and-upload. Documents originate from the [HotelsData](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toAzureSearch.json) sample on GitHub.
 
 ### Search an index
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ホテルデータサンプルのリンク修正"
}
```

### Explanation
この変更では、`articles/search/includes/quickstarts/full-text-python.md` ファイル内のリンクが一部修正されています。具体的には、GitHub上のホテルデータサンプルへのリンクの末尾の拡張子が大文字から小文字に変更されました。この修正によって、リンクが正しく動作する可能性が高まり、ユーザーが必要なリソースにアクセスしやすくなります。この変更は、特にURLの整合性を保つために重要です。ファイル内の他の部分には影響がなく、全体として軽微な更新と見なされます。

## articles/search/includes/quickstarts/search-get-started-vector-java.md{#item-a3db97}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Java用のベクトル検索入門ガイドの追加"
}
```

### Explanation
この変更では、`articles/search/includes/quickstarts/search-get-started-vector-java.md` という新しいファイルが追加されました。このファイルは、Javaを使用したベクトル検索の入門ガイドとして機能します。1483行にわたる内容が含まれており、Java開発者がAzure Searchのベクトル検索機能を利用する方法を詳しく説明しています。

新しいガイドには、必要な準備、使用するサンプルコード、具体的な実装手順などが含まれており、開発者がAzureのサービスを最大限に活用できるよう支援しています。この追加は、Javaユーザーにとって非常に有益なリソースとなるでしょう。

## articles/search/includes/quickstarts/search-get-started-vector-javascript.md{#item-d0387c}

<details>
<summary>Diff</summary>
````diff
@@ -19,6 +19,7 @@ In Azure AI Search, a [vector store](../../vector-store.md) has an index schema
 - An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
 - An Azure AI Search service. [Create a service](../../search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch) in your current subscription.
+    - The `Search Index Data Contributor` role assigned at the scope of the service.
     - You can use a free search service for most of this quickstart, but we recommend the Basic tier or higher for larger data files.
     - To run the query example that invokes [semantic reranking](../../semantic-search-overview.md), your search service must be at the Basic tier or higher with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
 
@@ -111,14 +112,14 @@ In this section, you create a vector index in Azure AI Search with [SearchIndexC
 
 1. Run the file:
 
-    ```console
+    ```bash
     node -r dotenv/config src/createIndex.js
     ```
 1. The output of this code shows that the index is created successfully:
 
-    ```console
-    Using Azure Search endpoint: https://my-service.search.windows.net
-    Using index name: hotels-vector-quickstart
+    ```output
+    Using Azure Search endpoint: https://<search-service-name>.search.windows.net
+    Using Azure Search index: <vector-index-name>
     Creating index...
     hotels-vector-quickstart created
     ```
@@ -142,7 +143,7 @@ Creating and loading the index are separate steps. You created the index schema
 
 In Azure AI Search, the index stores all searchable content, while the search engine executes queries against that index.
 
-1. Create a `uploadDocuments.js` file in the `src` directory.
+1. Create an `uploadDocuments.js` file in the `src` directory.
 1. Copy the following code into the file.
 
     :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/uploadDocuments.js" :::
@@ -153,12 +154,14 @@ In Azure AI Search, the index stores all searchable content, while the search en
 
 1. Build and run the file:
 
-    ```console
+    ```bash
     node -r dotenv/config src/uploadDocuments.js
     ```
 1. The output of this code shows that the documents are indexed and ready for search:
 
-    ```console
+    ```output
+    Using Azure Search endpoint: https://<search-service-name>.search.windows.net
+    Using Azure Search index: <vector-index-name>
     Uploading documents...
     Key: 1, Succeeded: true, ErrorMessage: none
     Key: 2, Succeeded: true, ErrorMessage: none
@@ -171,7 +174,7 @@ In Azure AI Search, the index stores all searchable content, while the search en
     All documents indexed successfully.
     ```
 
-    Key takeaways about the upload_documents() method and this example:
+    Key takeaways about the uploadDocuments() method and this example:
     
     * Your code interacts with a specific search index hosted in your Azure AI Search service through the SearchClient, which is the main object provided by the @azure/search-documents package. The SearchClient provides access to index operations such as:
         * Data ingestion - uploadDocuments(), mergeDocuments(), deleteDocuments(), etc.
@@ -211,15 +214,15 @@ The first example demonstrates a basic scenario where you want to find document
 
 1. Build and run the file:
 
-    ```console
+    ```bash
     node -r dotenv/config src/searchSingle.js
     ```
 
 1. The output of this code shows the relevant docs for the query `quintessential lodging near running trails, eateries, retail`. 
 
-    ```console
-    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
-    Using index name: hotels-vector-quickstart-0627-4
+    ```output
+    Using Azure Search endpoint: https://<search-service-name>.search.windows.net
+    Using Azure Search index: <vector-index-name>
     
     
     Single Vector search found 5
@@ -247,14 +250,14 @@ You can add filters, but the filters are applied to the nonvector content in you
 
 1. Build and run the file:
 
-    ```console
+    ```bash
     node -r dotenv/config src/searchSingleWithFilter.js
     ```
 1. The output of this code shows the relevant documents for the query with the filter for `free wifi` applied:
 
-    ```console
-    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
-    Using index name: hotels-vector-quickstart-0627-4
+    ```output
+    Using Azure Search endpoint: https://<search-service-name>.search.windows.net
+    Using Azure Search index: <vector-index-name>
     
     
     Single Vector search found 2
@@ -273,15 +276,15 @@ You can specify a geospatial filter to limit results to a specific geographic ar
     :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/searchSingleWithFilterGeo.js" :::
 1. Build and run the file:
 
-    ```console
+    ```bash
     node -r dotenv/config src/searchSingleWithFilterGeo.js
     ```
 
 1. The output of this code shows the relevant documents for the query with the geospatial post-processing exclusion filter applied:
 
-    ```console
-    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
-    Using index name: hotels-vector-quickstart-0627-4
+    ```output
+    Using Azure Search endpoint: https://<search-service-name>.search.windows.net
+    Using Azure Search index: <vector-index-name>
     
     
     Single Vector search found 2
@@ -305,14 +308,14 @@ This search uses [SearchClient](/javascript/api/@azure/search-documents/searchcl
     :::code language="javascript" source="~/azure-search-javascript-samples/quickstart-vector-js/src/searchHybrid.js" :::
 1. Build and run the file:
 
-    ```console
+    ```bash
     node -r dotenv/config src/searchHybrid.js
     ```
 1. The output of this code shows the relevant documents for the hybrid search:
 
-    ```console
-    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
-    Using index name: hotels-vector-quickstart-0627-4
+    ```output
+    Using Azure Search endpoint: https://<search-service-name>.search.windows.net
+    Using Azure Search index: <vector-index-name>
     
     
     Hybrid search found 7 then limited to top 5
@@ -417,7 +420,7 @@ This search uses [SearchClient](/javascript/api/@azure/search-documents/searchcl
            "@search.score": 0.8133763,
            "HotelId": "3",
            "HotelName": "Gastronomic Landscape Hotel",
-           "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+           "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services.",
            "Category": "Resort and Spa"
        }
    ]
@@ -436,15 +439,15 @@ This search uses [SearchClient](/javascript/api/@azure/search-documents/searchcl
 
 1. Build and run the file:
 
-    ```console
+    ```bash
     node -r dotenv/config src/searchSemanticHybrid.js
     ```
 
 1. The output of this code shows the relevant documents for the semantic hybrid search:
 
-    ```console
-    Using Azure Search endpoint: https://ai-search-dib-2.search.windows.net
-    Using index name: hotels-vector-quickstart-0627-4
+    ```output
+    Using Azure Search endpoint: https://<search-service-name>.search.windows.net
+    Using Azure Search index: <vector-index-name>
 
     
     Semantic hybrid search found 7 then limited to top 5
@@ -480,7 +483,7 @@ This search uses [SearchClient](/javascript/api/@azure/search-documents/searchcl
       Re-ranker Score: 2.0582215785980225
       HotelId: 3
       HotelName: Gastronomic Landscape Hotel
-      Description: The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.
+      Description: The Gastronomic Hotel stands out for its culinary excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services.
       Category: Suite
     ```
 
@@ -509,7 +512,7 @@ If you want to keep the search service, but delete the index and documents, you
 
 1. Build and run the file:
 
-    ```console
+    ```bash
     node -r dotenv/config src/deleteIndex.js
     ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript用のベクトル検索入門ガイドの修正"
}
```

### Explanation
この変更では、`articles/search/includes/quickstarts/search-get-started-vector-javascript.md` ファイルが修正され、いくつかの重要な更新が行われました。全体で65行の変更があり、新たに34行が追加され、31行が削除されています。主な内容の変更は次の通りです。

1. **サービスロールの追加**：Azure AI Searchサービスに対して、`Search Index Data Contributor`という役割が必要であることが明記されました。これにより、ユーザーは適切な権限で作業を行うことができます。

2. **出力形式の統一**：コンソール出力の例やコードブロックが「console」から「bash」、「output」に変更されており、整合性が向上しています。これにより、ユーザーが期待する出力形式が一貫して示されるようになりました。

3. **プレースホルダーの明示化**：一部の出力例において、サービス名やインデックス名をプレースホルダーとして示すように変更され、ユーザーが自分の環境に合わせやすくなっています。

これらの修正により、JavaScriptを使用したベクトル検索の手順がより明確で、実用的なガイドになっています。ユーザーの理解を深めるための重要な更新と言えるでしょう。

## articles/search/includes/quickstarts/semantic-ranker-java.md{#item-93a05a}

<details>
<summary>Diff</summary>
````diff
@@ -89,7 +89,7 @@ If you signed in to the [Azure portal](https://portal.azure.com), you're signed
 
 ## Create a common configuration class
 
-Create a file in `src/main/java/com/azure/search/quickstart` called `SearchConfig.java` to read the properties file and hold the environment variables and authentication credential.
+Create a file in `src/main/java/com/azure/search/quickstart` called `SearchConfig.java` to read the properties file and hold the configuration values and authentication credential.
 
 ```java
 package com.azure.search.quickstart;
@@ -476,7 +476,7 @@ Optionally, you can add captions to extract portions of the text and apply hit h
 
 1. Output should include a new caption element alongside search field. Captions are the most relevant passages in a result. If your index includes larger chunks of text, a caption is helpful for extracting the most interesting sentences.
 
-    ```console
+    ```output
     Search result #1:
       Re-ranker Score: 2.613231658935547
       HotelName: Uptown Chic Hotel
@@ -604,7 +604,7 @@ To produce a semantic answer, the question and answer must be closely aligned, a
 
     Recall that answers are *verbatim content* pulled from your index and might be missing phrases that a user would expect to see. To get *composed answers* as generated by a chat completion model, considering using a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../search-agentic-retrieval-concept.md).
 
-    ```console
+    ```output
     Semantic answer result #1:
     Semantic Answer: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
     Semantic Answer Score: 0.9829999804496765
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java用セマンティックランカーガイドの修正"
}
```

### Explanation
この変更では、`articles/search/includes/quickstarts/semantic-ranker-java.md` ファイルが修正されました。全体で6行の変更があり、3行が追加され、3行が削除されています。主な更新内容は次の通りです。

1. **用語の修正**：ファイル内の説明文において、「環境変数」という表現が「設定値」に変更されました。これにより、ユーザーにとって理解しやすい表現になっています。

2. **出力形式の統一**：各出力例において、「console」から「output」というラベルに変更されました。これによって、ユーザーは期待する出力形式がより明確に示され、一貫性が向上しています。

これらの変更により、Java用のセマンティックランカーに関するガイドがより分かりやすくなり、ユーザーが具体的な手順を容易に理解できるよう配慮されています。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -70,7 +70,7 @@ The information retrieval system provides the searchable index, query logic, and
 
 The LLM receives the original prompt, plus the results from Azure AI Search. The LLM analyzes the results and formulates a response. If the LLM is ChatGPT, the user interaction might consist of multiple conversation turns. An Azure solution most likely uses Azure OpenAI, but there's no hard dependency on this specific service.
 
-Except for features currently in previewAzure AI Search doesn't provide native LLM integration for prompt flows or chat preservation, so you need to write code that handles orchestration and state. You can review demo source ([Azure-Samples/azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo)), updated for agentic retrieval, for a blueprint of what a full solution entails. We also recommend [Azure AI Foundry](/azure/ai-foundry/concepts/retrieval-augmented-generation) to create RAG-based Azure AI Search solutions that integrate with LLMs.
+Except for features currently in preview, Azure AI Search doesn't provide native LLM integration for prompt flows or chat preservation, so you need to write code that handles orchestration and state. You can review demo source ([Azure-Samples/azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo)), updated for agentic retrieval, for a blueprint of what a full solution entails. We also recommend [Azure AI Foundry](/azure/ai-foundry/concepts/retrieval-augmented-generation) to create RAG-based Azure AI Search solutions that integrate with LLMs.
 
 ## Searchable content in Azure AI Search
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "情報取得拡張生成の概要の修正"
}
```

### Explanation
この変更では、`articles/search/retrieval-augmented-generation-overview.md` ファイルが修正されました。全体で2行の変更があり、1行が追加され、1行が削除されています。変更内容は主にテキストのフォーマット改善に関するもので、以下の点が挙げられます。

1. **文の区切り修正**：元の文において、「Except for features currently in preview」の後に必要だったコンマが追加されることで、文が読みやすくなり、文の構造が向上しています。この修正により、条件とそれに続く主文の関連が明確になります。

2. **内容の一貫性の保持**：全体の文脈や情報は変わっていませんが、文の流れが改善され、ユーザーが内容を理解しやすくなるように配慮されています。

この修正により、情報取得拡張生成に関するガイドがより明確で、ユーザーが必要な情報を簡単に見つけられるようになっています。

## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -20,6 +20,12 @@ zone_pivot_groups: search-get-started-vector-search
 
 ::: zone-end
 
+::: zone pivot="java"
+
+[!INCLUDE [Java quickstart](includes/quickstarts/search-get-started-vector-java.md)]
+
+::: zone-end
+
 ::: zone pivot="javascript"
 
 [!INCLUDE [JavaScript quickstart](includes/quickstarts/search-get-started-vector-javascript.md)]
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Javaクイックスタートへのリンク追加"
}
```

### Explanation
この変更では、`articles/search/search-get-started-vector.md` ファイルに6行が追加され、新たにJavaに関連するコンテンツへのリンクが追加されました。具体的な変更内容は以下の通りです。

1. **Javaゾーンの追加**：新たに「java」というpivotを持つゾーンが追加され、Java用のクイックスタートガイドへのリンクが挿入されました。このリンクにより、ユーザーはJavaを使用したベクター検索の導入方法を簡単に参照できるようになります。

2. **情報の拡充**：以前はJavaに関する情報がなかったため、この追加により、Java開発者向けに必要な情報が充実し、より幅広いユーザーが利用できる内容となっています。

この修正によって、ベクター検索に関するガイドの有用性が向上し、異なるプログラミング言語での実装が可能なことを示しています。

## articles/search/search-howto-index-cosmosdb.md{#item-568fab}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ To work through the examples in this article, you need the Azure portal or a [RE
 
 Use these instructions to create a container and database in Cosmos DB for testing purposes.
 
-1. [Download HotelsData_toCosmosDB.JSON](https://github.com/HeidiSteen/azure-search-sample-data/blob/main/hotels/HotelsData_toCosmosDB.JSON) from GitHub to create a container in Cosmos DB that contains a subset of the sample hotels data set.
+1. [Download HotelsData_toCosmosDB.json](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toCosmosDB.json) from GitHub to create a container in Cosmos DB that contains a subset of the sample hotels data set.
 
 1. Sign in to the Azure portal and [create an account, database, and container](/azure/cosmos-db/nosql/quickstart-portal) on Cosmos DB. 
 
@@ -55,7 +55,7 @@ Use these instructions to create a container and database in Cosmos DB for testi
 
 1. In **Data Explorer**, expand *hotelsdb* and *hotels*, and then select **Items**.
 
-1. Select **Upload Item** and then select *HotelsData_toCosmosDB.JSON* file that you downloaded from GitHub.
+1. Select **Upload Item** and then select *HotelsData_toCosmosDB.json* file that you downloaded from GitHub.
 
 1. Right-click **Items** and select **New SQL query**. The default query is `SELECT * FROM c`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイル名の表記修正"
}
```

### Explanation
この変更では、`articles/search/search-howto-index-cosmosdb.md` ファイルにおいて、2行が追加され、2行が削除され、合計で4行が変更されました。具体的には、ファイル名の表記を変更することで、一貫性を持たせています。以下の点が挙げられます。

1. **ファイル名の表記変更**：元々の表記である「HotelsData_toCosmosDB.JSON」から、「HotelsData_toCosmosDB.json」へ変更されました。この変更により、ファイル名が小文字の拡張子で統一され、一貫性が向上しています。

2. **指示の明確化**：ファイル名が正確に記載されることで、ユーザーが正しいファイルを見つけやすくなり、実行時の混乱を避けることができます。

この修正は、ユーザーの利便性を高めるためのものであり、特に複数の手順を踏む際に、正確なファイル名の提示が重要であることを反映しています。

## articles/search/search-howto-indexing-azure-tables.md{#item-7655b0}

<details>
<summary>Diff</summary>
````diff
@@ -38,7 +38,7 @@ Use these instructions to create a table in Azure Storage for testing purposes.
 
 1. [Install Azure Storage Explorer](https://azure.microsoft.com/products/storage/storage-explorer/#Download-4).
 
-1. [Download HotelsData_toAzureSearch.csv](https://github.com/HeidiSteen/azure-search-sample-data/blob/main/hotels/HotelsData_toAzureSearch.csv) from GitHub. This file is a subset of the built-in hotels sample dataset. It omits the rooms collection, translated descriptions, and geography coordinates.
+1. [Download HotelsData_toAzureSearch.csv](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toAzureSearch.csv) from GitHub. This file is a subset of the built-in hotels sample dataset. It omits the rooms collection, translated descriptions, and geography coordinates.
 
 1. In Azure Storage Explorer, sign in to Azure, select your subscription, and then select your storage account.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サンプルデータリポジトリのリンク修正"
}
```

### Explanation
この変更では、`articles/search/search-howto-indexing-azure-tables.md` ファイルにおいて、1行が追加され、1行が削除され、合計で2行が変更されました。主な内容は以下の通りです。

1. **リンクの修正**：元々のリンク先が「HeidiSteen」リポジトリから、「Azure-Samples」リポジトリに変更されました。これにより、サンプルデータへのアクセスがより標準化され、Microsoftが公式に管理しているリポジトリに切り替わりました。

2. **データセットの説明はそのまま**：リンクの変更に伴い、説明文は変更がなく、元のデータセットについての情報がそのまま維持されています。このため、ユーザーは引き続き同じ内容のデータを利用できることがわかります。

この修正により、ユーザーは最新の、より信頼性の高いデータソースから情報を取得できるようになり、ドキュメントの精度が向上しています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -105,7 +105,7 @@ You can create an Azure AI Search service in any of the following Azure public r
 | Japan West​ | ✅ |  | ✅ | ✅ |  |
 | Korea Central | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Korea South​​ |  |  | ✅ | ✅ |  |
-| Malaysia West |  | ✅ |  |  |  |  |
+| Malaysia West |  | ✅ |  |  |  |  
 | New Zealand North |  | ✅ |  |  |  |
 | South India |  | ✅ |  |  |  |
 | Southeast Asia​​ | ✅ | ✅ | ✅ | ✅ | ✅ |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マレーシア西部のサポート状況の調整"
}
```

### Explanation
この変更では、`articles/search/search-region-support.md` ファイルにおいて、1行が追加され、1行が削除され、合計で2行が変更されました。主なポイントは以下の通りです。

1. **テーブルの更新**：特に「マレーシア西部」地域におけるサポート状況についての情報が微調整されました。この地域がサポートされる条件に未設定の部分があったため、それに対して適切な表示方法が適用されています。

2. **表記の一貫性**：同じテーブル内の他の地域と一貫性が保たれるよう、設定が整えられたことで、視覚的な情報の一貫性が向上しました。この変更により、マレーシア西部に関する情報が正確かつ明確になっています。

この修正により、ユーザーは地域ごとのAzure AI Searchサービスのサポート状況について、より正確で明瞭な情報を得ることができ、適切な情報をもとに利用判断ができるようになります。

## articles/search/search-security-overview.md{#item-6b3f1e}

<details>
<summary>Diff</summary>
````diff
@@ -119,7 +119,7 @@ The private endpoint uses an IP address from the virtual network address space f
 
 :::image type="content" source="media/search-security-overview/inbound-private-link-azure-cog-search.png" alt-text="sample architecture diagram for private endpoint access":::
 
-While this solution is the most secure, using more services is an added cost so be sure you have a clear understanding of the benefits before diving in. For more information about costs, see the [pricing page](https://azure.microsoft.com/pricing/details/private-link/). For more information about how these components work together, [watch this video](https://learn.microsoft.com/Shows/AI-Show/Azure-Cognitive-Search-Whats-new-in-security). Coverage of the private endpoint option starts at 5:48 into the video. For instructions on how to set up the endpoint, see [Create a Private Endpoint for Azure AI Search](service-create-private-endpoint.md).
+While this solution is the most secure, using more services is an added cost so be sure you have a clear understanding of the benefits before diving in. For more information about costs, see the [pricing page](https://azure.microsoft.com/pricing/details/private-link/). For more information about how these components work together, [watch this video](/Shows/AI-Show/Azure-Cognitive-Search-Whats-new-in-security). Coverage of the private endpoint option starts at 5:48 into the video. For instructions on how to set up the endpoint, see [Create a Private Endpoint for Azure AI Search](service-create-private-endpoint.md).
 
 ### Network security perimeter
 
@@ -300,4 +300,4 @@ Apply metadata tags to categorize search services based on data sensitivity and
 + [Azure Security](https://azure.microsoft.com/overview/security)
 + [Microsoft Defender for Cloud](/azure/security-center/)
 
-We also recommend the following [video on security features](https://learn.microsoft.com/Shows/AI-Show/Azure-Cognitive-Search-Whats-new-in-security). It's several years old and doesn't cover newer features, but it covers these features: CMK, IP firewalls, and private link. If you use those features, you might find this video helpful.
+We also recommend the following [video on security features](/Shows/AI-Show/Azure-Cognitive-Search-Whats-new-in-security). It's several years old and doesn't cover newer features, but it covers these features: CMK, IP firewalls, and private link. If you use those features, you might find this video helpful.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セキュリティ関連のリンク修正"
}
```

### Explanation
この変更では、`articles/search/search-security-overview.md` ファイルにおいて、2行が追加され、2行が削除され、合計で4行が変更されました。主な内容は以下の通りです。

1. **リンクの修正**：セキュリティ機能に関するビデオへのリンクが修正されました。以前は絶対URLが使用されていましたが、相対URLに変更され、URLの構成が一貫性を持たせるようになりました。これにより、新たなリンクが文書全体で統一感を持つようになっています。

2. **ビデオの説明の一貫性**：ビデオの推奨に関しての表現が改善され、ユーザーが参考にすべきポイントがより明確になりました。このビデオは数年前のものであり、新しい機能は含まれていませんが、それでも特定の重要なセキュリティ機能について知見を得るのに役立ちます。

これらの修正により、自信を持ってリンクを利用し、セキュリティに関する情報をユーザーが簡単にアクセスできるようになります。また、情報の整合性が向上し、ドキュメント全体のクオリティが高まります。


