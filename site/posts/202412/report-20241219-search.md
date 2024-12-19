---
date: '2024-12-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:aba0ab5...MicrosoftDocs:6ebedb4
summary: 最新の更新により、Azure AI SearchのCognitive Services接続に関するキーの種類が追加され、内容が更に明確になりました。新しいキータイプ「#Microsoft.Azure.Search.AIServicesByKey」が導入され、ユーザーにプライベートリンクや地域要件を気にせず利用できるよう指導しています。また、複数のドキュメントで日付の更新や説明文の修正がなされており、読者には正確で統一された情報が提供されています。これにより、Azure
  AI Searchの機能や使い方に対する理解が深まり、ユーザー体験が向上しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:aba0ab5...MicrosoftDocs:6ebedb4){target="_blank"}

# Highlights
最新の更新で、Azure AI SearchのCognitive Services接続に関するキーの種類が追加され、より細かく説明されました。また、複数のドキュメントにおいて日付の更新や説明文の調整がなされ、記事の内容が最新かつ明確になりました。

## New features
- 新しいキータイプ `#Microsoft.Azure.Search.AIServicesByKey` の追加。
  
## Breaking changes
- 特に破壊的な変更は報告されていません。

## Other updates
- 複数のドキュメントでの最終更新日の修正。
- 文章内容の明確化と説明の強化。

# Insights
この変更により、Azure AI SearchにおけるCognitive Servicesの統合がよりシンプルで効率的になり、推奨されるキータイプが明示されました。これにより、ユーザーはプライベートリンクの使用や特定の地域要件を気にせずに利用できるようになります。新しい内容が追加されたことに加え、APIバージョンも最新に更新されているため、ユーザーは常に最新の技術と最適なプラクティスにアクセスすることが可能になっています。

さらに、複数のドキュメントで記載されている日付の更新と文章の修正により、読者にはより正確で統一された情報が提供されており、Azure AI Searchの機能と使い方についての理解が向上します。特に言語解析に関する説明が改善されたことで、解析結果への期待値を明確にでき、より高度な利用方法を想定する際の誤解を減らす効果があります。

このようなアップデートを実施することで、ユーザーがAzure AI Searchを活用する際の障壁が下がり、よりスムーズな体験を得ることができます。リリースごとの細かな変更が、全体的なユーザー体験の向上につながっていると言えます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | Cognitive Servicesを接続するためのキーの種類の更新 | modified | 9 | 3 | 12 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [search-language-support.md](#item-a7979b) | minor update | テキスト分析の説明の更新 | modified | 1 | 1 | 2 | 
| [search-what-is-azure-search.md](#item-93853a) | minor update | 文章内容の明確化と拡張 | modified | 3 | 3 | 6 | 
| [tutorial-rag-build-solution-index-schema.md](#item-9a17ca) | minor update | インデックス設計チュートリアルの調整 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -110,7 +110,9 @@ POST https://[service-name].search.windows.net/skillsets/[skillset-name]?api-ver
 
 Azure AI Search can also charge for transaction using the Azure AI multi-service resource key. This approach is the default and is generally available. You can use the Azure portal, REST API, or an Azure SDK to add the key to a skillset.
 
-You only need to add the key, not the subdomain or endpoint. If you leave the `cognitiveServices` property unspecified, your search service attempts to use the free enrichments available to your indexer on a daily basis. Execution of billable skills stops at 20 transactions per indexer invocation and a "Time Out" message appears in indexer execution history.
+There are two supported key types: `#Microsoft.Azure.Search.CognitiveServicesByKey` which calls the regional endpoint and `"#Microsoft.Azure.Search.AIServicesByKey` which calls the subdomain. We recommend using `AIServicesByKey` for its shared private link support and ability to function with no regional requirements relative to the search service.
+
+If you leave the `cognitiveServices` property unspecified, your search service attempts to use the free enrichments available to your indexer on a daily basis. Execution of billable skills stops at 20 transactions per indexer invocation and a "Time Out" message appears in indexer execution history.
 
 ### [**Azure portal**](#tab/portal)
 
@@ -128,12 +130,15 @@ You only need to add the key, not the subdomain or endpoint. If you leave the `c
 
   :::image type="content" source="media/cognitive-search-attach-cognitive-services/attach-existing2.png" alt-text="Screenshot of the key page." border="true":::
 
+> [!NOTE]
+> Azure portal currently automatically attaches key of type `#Microsoft.Azure.Search.CognitiveServicesByKey`.
+
 ### [**REST**](#tab/cogkey-rest)
 
 1. Use the [Create or Update Skillset](/rest/api/searchservice/skillsets/create-or-update) API, specifying `cognitiveServices` section in the body of the request:
 
 ```http
-PUT https://[servicename].search.windows.net/skillsets/[skillset name]?api-version=2024-07-01
+PUT https://[servicename].search.windows.net/skillsets/[skillset name]?api-version=2024-11-01-Preview
 api-key: [admin key]
 Content-Type: application/json
 {
@@ -157,8 +162,9 @@ Content-Type: application/json
       }
     ],
     "cognitiveServices": {
-        "@odata.type": "#Microsoft.Azure.Search.CognitiveServicesByKey",
+        "@odata.type": "#Microsoft.Azure.Search.AIServicesByKey",
         "description": "mycogsvcs",
+        "subdomainUrl": “https://[subdomain-name].cognitiveservices.azure.com",
         "key": "<your key goes here>"
     }
 }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cognitive Servicesを接続するためのキーの種類の更新"
}
```

### Explanation
この変更では、Azure AI SearchにおけるCognitive Services接続のためのキーに関する情報が更新されました。具体的には、二つのキータイプが追加され、推奨されるタイプとして`"#Microsoft.Azure.Search.AIServicesByKey"`が示されています。この新しいキーは、共有プライベートリンクのサポートや、検索サービスに対する地域要件がない点が特徴です。更新により、`cognitiveServices`プロパティを指定しない場合の動作についての説明も繰り返し記載されました。

具体的には、変更により次の内容が追加されました：
- 新しいキータイプの説明
- Azureポータルが自動的にキーを添付することを通知する注釈
- APIバージョンを`2024-11-01-Preview`に更新する変更

このように、Cognitive Servicesの使用法とその接続方法に関する情報がより明確に更新されています。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: conceptual
-ms.date: 09/03/2024
+ms.date: 12/18/2024
 ---
 
 # Retrieval Augmented Generation (RAG) in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更では、Azure AI Searchに関するドキュメントの最終更新日が修正されました。具体的には、`ms.date`の値が「2024年09月03日」から「2024年12月18日」に変更されました。これにより、文書の内容がより最新であることを示しています。この修正は、コンテンツが最新の情報を反映していることを保障するために行われたものです。他の内容には変更はなく、文書のトピックやカスタムタグはそのままとなっています。

## articles/search/search-language-support.md{#item-a7979b}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.date: 12/10/2024
 
 # Create an index for multiple languages in Azure AI Search
 
-If you have strings in multiple languages, you can attach [language analyzers](index-add-language-analyzers.md#supported-language-analyzers) that analyze strings using linguistic rules of a specific language during indexing and query execution. With a language analyzer, you get better handling of character variations, punctuation, and word root forms. 
+If you have strings in multiple languages, you can attach [language analyzers](index-add-language-analyzers.md#supported-language-analyzers) that analyze strings using linguistic rules of a specific language during indexing and query execution. With a language analyzer, you get better handling of diacritics, character variants, punctuation, and word root forms.
 
 Azure AI Search supports Microsoft and Lucene analyzers. By default, the search engine uses Standard Lucene, which is language agnostic. If testing indicates that the default analyzer is insufficient, replace it with a language analyzer.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト分析の説明の更新"
}
```

### Explanation
この変更では、Azure AI Searchに関する文書内のテキスト分析に関する説明が修正されました。具体的には、言語解析器を使用した文字列の分析に関する文の一部が変更されました。元の文では「character variations」という表現が使われていましたが、これが「diacritics, character variants」というより正確な表現に置き換えられています。

この修正により、言語解析の機能の説明がより明確になり、さまざまな文字や記号の扱いに関する理解が深まることが期待されます。その他の情報は変更されておらず、文書自体の構造や目的はそのまま保持されています。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -15,11 +15,11 @@ ms.date: 12/10/2024
 
 # What's Azure AI Search?
 
-Azure AI Search ([formerly known as "Azure Cognitive Search"](whats-new.md#new-service-name)) is an enterprise-ready information retrieval system for your heterogeneous content that you ingest into a search index. It comes with a comprehensive set of advanced search technologies, built for high-performance applications at any scale.
+Azure AI Search ([formerly known as "Azure Cognitive Search"](whats-new.md#new-service-name)) is an enterprise-ready information retrieval system for your heterogeneous content that you ingest into a search index, and surface to users through queries and apps. It comes with a comprehensive set of advanced search technologies, built for high-performance applications at any scale.
 
-Azure AI Search is the recommended retrieval system for building RAG-based applications on Azure, with native LLM integrations between Azure OpenAI Service and Azure Machine Learning, and multiple strategies for relevance tuning.
+Azure AI Search is the recommended retrieval system for building RAG-based applications on Azure, with native LLM integrations between Azure OpenAI Service and Azure Machine Learning, an integration mechanism for non-native models and processes, and multiple strategies for relevance tuning.
 
-Azure AI Search can be used in both traditional and GenAI scenarios. Common use cases include catalog or document search, information discovery (data exploration), and retrieval-augmented generation (RAG) for conversational search.  
+Azure AI Search can be used in both traditional and GenAI search scenarios. Common use cases include catalog or document search, information discovery (data exploration), and retrieval-augmented generation (RAG) for conversational search.  
 
 When you create a search service, you work with the following capabilities:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文章内容の明確化と拡張"
}
```

### Explanation
この変更では、Azure AI Searchに関する文書の内容がより明確で詳細になるように修正されました。具体的には、以下の点が更新されています。

1. Azure AI Searchの説明文に「and surface to users through queries and apps」というフレーズが追加され、検索結果をユーザーにどのように提供するかを明示的に示しています。
2. RAGベースのアプリケーション構築のための推奨情報検索システムとしての説明が強化され、「non-native models and processes」の統合メカニズムが追加され、従来のモデル以外の統合に関する情報が明記されています。
3. 最後に「traditional and GenAI scenarios」の表記が一部修正され、より正確な説明となっています。

これらの変更により、Azure AI Searchの機能と用途についての理解が深まることを目指しています。その他の内容については変更はなく、文書自体の構造は保持されています。

## articles/search/tutorial-rag-build-solution-index-schema.md{#item-9a17ca}

<details>
<summary>Diff</summary>
````diff
@@ -8,19 +8,19 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 10/04/2024
+ms.date: 12/18/2024
 
 ---
 
 # Tutorial: Design an index for RAG in Azure AI Search
 
-An index contains searchable text and vector content, plus configurations. In a RAG pattern that uses a chat model for responses, you want an index that contains chunks of content that can be passed to an LLM at query time. 
+An index contains searchable text and vector content, plus configurations. In a RAG pattern that uses a chat model for responses, you want an index designed around chunks of content that can be passed to an LLM at query time. 
 
 In this tutorial, you:
 
 > [!div class="checklist"]
 > - Learn the characteristics of an index schema built for RAG
-> - Create an index that accommodate vectors and hybrid queries
+> - Create an index that accommodates vector and hybrid queries
 > - Add vector profiles and configurations
 > - Add structured data
 > - Add filtering
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス設計チュートリアルの調整"
}
```

### Explanation
この変更では、Azure AI SearchにおけるRAG（Retrieval-Augmented Generation）用インデックス設計に関するチュートリアル文書が修正されました。主な変更点は以下の通りです。

1. ドキュメントの更新日が「10/04/2024」から「12/18/2024」へと変更され、最新の情報を反映するようになりました。
   
2. インデックスの内容についての記述が微調整され、「index designed around chunks of content」という表現に書き換えられました。これにより、インデックスの設計意図がより明確になっています。

3. チェックリストの項目も修正され、「accommodate vectors」という表現が「accommodates vector」となり、文法的に正しい形に整えられています。

これらの変更により、チュートリアルの内容がより明確に、かつ読みやすくなり、ユーザーがRAGインデックスの設計方法を理解しやすくなることを目的としています。その他の文書内容は変更されておらず、全体的な構造はそのまま維持されています。


