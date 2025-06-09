---
date: '2025-06-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0565698...MicrosoftDocs:35b42f4
summary: このコード変更は、Azure AI Searchに関連する複数の記事を微修正したもので、主に記事の日付の更新、技術用語の一貫性の向上、権限やAPI要件の明確化、トピック構成の再編成が含まれています。新しいトピックや詳細が追加され、API要件に関する説明が詳述化されています。用語の変更による破壊的変更は特にありませんが、表現が一部異なる可能性があります。日付更新や用語の一貫性を図るための表現修正、トピック構成ファイルの再編成も行われています。この変更は、ユーザーが必要な情報を迅速に見つけられるようにするためのもので、Azureユーザーの体験を向上させることに寄与しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0565698...MicrosoftDocs:35b42f4){target="_blank"}

<format>
# ハイライト
このコード変更は、Azure AI Searchに関連する複数の記事を微修正したものです。主なハイライトとして、記事の日付の更新、技術用語の一貫性の向上、権限やAPI要件の明確化、そしてトピック構成の再編成が挙げられます。

## 新機能
- 記事内の項目に新しいトピックや詳細が追加。
- API要件や権限に関する詳細が詳述化。

## 破壊的変更
- 特に無し。ただし、用語の変更により、表現が一部異なる場合あり。

## その他の更新
- 記事の日付更新。
- 用語の一貫性を図るための表現修正。
- トピック構成ファイル(toc.yml)の大幅な変更、セクションの再編成。

# インサイト
この変更はAzure AI Searchに関連する技術文書の微調整を目的としています。記事の日付や用語の修正を通じて、最新の技術動向やユーザーの混乱を避けるための改善を行っています。特に、複数の記事で「基本ティア」を「Basic pricing tier」に変更することで、読者がAzureの料金プランをより正確に理解できるようになっています。

トピック構成(toc.yml)の更新は、Azure Searchの最新情報を反映し、ユーザーが目的とする情報を効率的に検索できるよう構成されています。この更新は、単なる記事内容の修正にとどまらず、読者が必要とする情報を迅速に見つけるためのドキュメントナビゲーションの改善にも寄与しています。

さらに、API要件や権限に関する記述を詳細化し、ユーザーが必要なリソースの作成や利用方法を理解しやすくなるように工夫されています。このような細部の修正が、Azureユーザーの体験を向上させるためにどのように寄与するかが分かります。また、「Foundry Model」や「チャット完結モデル」といった用語の明確化は、専門用語に対する理解を深め、技術的な内容をよりユーザーに伝えることを目的としています。

これらすべての変更は、Azure AI Searchのユーザーがサービスを最大限に活用するために不可欠な情報を提供しやすくするためのものであり、技術的な正確さと文書の一貫性を向上させています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index-add-custom-analyzers.md](#item-11325e) | minor update | カスタムアナライザーの使用に関する記事の更新 | modified | 4 | 2 | 6 | 
| [index-add-language-analyzers.md](#item-004ac0) | minor update | 言語アナライザーに関する記事の更新 | modified | 7 | 5 | 12 | 
| [search-agentic-retrieval-how-to-create.md](#item-310fbe) | minor update | 知識エージェントの作成に関する記事の更新 | modified | 6 | 7 | 13 | 
| [search-agentic-retrieval-how-to-index.md](#item-a078ea) | minor update | エージェント的検索取得に関する記事の用語修正 | modified | 1 | 1 | 2 | 
| [search-agentic-retrieval-how-to-pipeline.md](#item-1ad1c3) | minor update | エージェント的検索取得パイプラインに関する記事の用語修正 | modified | 1 | 1 | 2 | 
| [search-agentic-retrieval-how-to-retrieve.md](#item-5f7fc0) | minor update | エージェント的検索取得を用いた検索方法に関する記事の更新 | modified | 7 | 7 | 14 | 
| [search-how-to-index-logic-apps-indexers.md](#item-64a12e) | minor update | Logic Apps インデクサーに関する記事の用語修正 | modified | 1 | 1 | 2 | 
| [search-try-for-free.md](#item-36e28d) | minor update | 無料トライアルに関する記事の用語修正 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c4768f) | minor update | トピック構成の更新 | modified | 144 | 138 | 282 | 
| [tutorial-document-extraction-image-verbalization.md](#item-398a90) | minor update | Azure AI Searchの価格プランについての修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/index-add-custom-analyzers.md{#item-11325e}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 01/16/2025
+ms.date: 06/16/2025
 ---
 
 # Add custom analyzers to string fields in an Azure AI Search index
@@ -20,7 +20,9 @@ In a custom analyzer, character filters prepare the input text before it's proce
 
 ## Why use a custom analyzer?
 
-A custom analyzer gives you control over the process of converting plain text into indexable and searchable tokens by allowing you to choose which types of analysis or filtering to invoke, and the order in which they occur. 
+You should consider a custom analyzer in classic search workflows that don't include large language models and their ability to handle content anomalies.
+
+In class search, a custom analyzer gives you control over the process of converting plain text into indexable and searchable tokens by allowing you to choose which types of analysis or filtering to invoke, and the order in which they occur. 
 
 Create and assign a custom analyzer if none of default (Standard Lucene), built-in, or language analyzers are sufficient for your needs. You might also create a custom analyzer if you want to use a built-in analyzer with custom options. For example, if you wanted to change the `maxTokenLength` on Standard Lucene, you would create a custom analyzer, with a user-defined name, to set that option.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムアナライザーの使用に関する記事の更新"
}
```

### Explanation
このコード変更は、Azure AI Searchのカスタムアナライザーに関する記事の一部を更新しています。主な変更点は、記事の日付が2025年1月16日から2025年6月16日に変更されたことです。また、カスタムアナライザーの使用に関する説明が更新され、従来の検索ワークフローにおいて、特に大規模言語モデルを使用しない場合にカスタムアナライザーを考慮すべき理由が追加されました。この変更により、読者はカスタムアナライザーの利点がより明確に理解できるようになっています。

## articles/search/index-add-language-analyzers.md{#item-004ac0}

<details>
<summary>Diff</summary>
````diff
@@ -1,15 +1,15 @@
 ---
 title: Add language analyzers to string fields
 titleSuffix: Azure AI Search
-description: Configure multi-lingual lexical analysis for non-English queries and indexes in Azure AI Search.
+description: Configure multi-lingual lexical analysis for non-English text queries and indexes in Azure AI Search.
 author: HeidiSteen
 manager: nitinme
 ms.author: heidist
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 01/16/2025
+ms.date: 06/16/2025
 ---
 
 # Add language analyzers to string fields in an Azure AI Search index
@@ -18,9 +18,11 @@ A *language analyzer* is a specific type of [text analyzer](search-analyzers.md)
 
 ## When to use a language analyzer
 
-You should consider a language analyzer when awareness of word or sentence structure adds value to text parsing. A common example is the association of irregular verb forms ("bring" and "brought) or plural nouns ("mice" and "mouse"). Without linguistic awareness, these strings are parsed on physical characteristics alone, which fails to catch the connection. Since large chunks of text are more likely to have this content, fields consisting of descriptions, reviews, or summaries are good candidates for a language analyzer.
+You should consider a language analyzer in classic search workflows that don't include large language models and their awareness of linguistic rules and multilingual content.
 
-You should also consider language analyzers when content consists of non-Western language strings. While the [default analyzer (Standard Lucene)](search-analyzers.md#default-analyzer) is language-agnostic, the concept of using spaces and special characters (hyphens and slashes) to separate strings is more applicable to Western languages than non-Western ones. 
+In class search, you might add a language analyzer when awareness of word or sentence structure adds value to text parsing. A common example is the association of irregular verb forms ("bring" and "brought) or plural nouns ("mice" and "mouse"). Without linguistic awareness, these strings are parsed on physical characteristics alone, which fails to catch the connection. Since large chunks of text are more likely to have this content, fields consisting of descriptions, reviews, or summaries are good candidates for a language analyzer.
+
+You might also consider language analyzers when content consists of non-Western language strings. While the [default analyzer (Standard Lucene)](search-analyzers.md#default-analyzer) is language-agnostic, the concept of using spaces and special characters (hyphens and slashes) to separate strings is more applicable to Western languages than non-Western ones. 
 
 For example, in Chinese, Japanese, Korean (CJK), and other Asian languages, a space isn't necessarily a word delimiter. Consider the following Japanese string. Because it has no spaces, a language-agnostic analyzer would likely analyze the entire string as one token, when in fact the string is actually a phrase.
 
@@ -37,7 +39,7 @@ A better experience is to search for individual words: 明るい (Bright), 私
 
 Azure AI Search supports 35 language analyzers backed by Lucene, and 50 language analyzers backed by proprietary Microsoft natural language processing technology used in Office and Bing.
 
-Some developers might prefer the more familiar, simple, open-source solution of Lucene. Lucene language analyzers are faster, but the Microsoft analyzers have advanced capabilities, such as lemmatization, word decompounding (in languages like German, Danish, Dutch, Swedish, Norwegian, Estonian, Finnish, Hungarian, Slovak) and entity recognition (URLs, emails, dates, numbers). If possible, you should run comparisons of both the Microsoft and Lucene analyzers to decide which one is a better fit. You can use [Analyze API](/rest/api/searchservice/indexes/analyze) to see the tokens generated from a given text using a specific analyzer.
+Some developers might prefer the open-source solution of Lucene. Lucene language analyzers are faster, but the Microsoft analyzers have advanced capabilities, such as lemmatization, word decompounding (in languages like German, Danish, Dutch, Swedish, Norwegian, Estonian, Finnish, Hungarian, Slovak) and entity recognition (URLs, emails, dates, numbers). If possible, you should run comparisons of both the Microsoft and Lucene analyzers to decide which one is a better fit. You can use [Analyze API](/rest/api/searchservice/indexes/analyze) to see the tokens generated from a given text using a specific analyzer.
 
 Indexing with Microsoft analyzers is on average two to three times slower than their Lucene equivalents, depending on the language. Search performance shouldn't be significantly affected for average size queries. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語アナライザーに関する記事の更新"
}
```

### Explanation
このコード変更は、Azure AI Searchにおける言語アナライザーに関する記事の内容を更新しています。変更点には、記事の説明が「非英語のクエリとインデックス」に関連する文に具体性を持たせる形で修正され、日付が2025年1月16日から2025年6月16日に変更されました。さらに、言語アナライザーを使用すべき条件に関する説明が更新され、伝統的な検索ワークフローにおいて大規模言語モデルを含まない場面における言語アナライザーの重要性が強調されています。この更新により、読者は多言語テキストに対してフェーズ構造を意識することの重要性や具体的な例が適切に示されています。

## articles/search/search-agentic-retrieval-how-to-create.md{#item-310fbe}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,7 @@ A knowledge agent specifies:
 + A target search index used at query time
 + Parameters on the index for setting default behaviors and response shaping
 
-After you can create a knowledge agent, you can update its properties at any time. If the knowledge agent is in use, updates take effect on the next job.
+After you create a knowledge agent, you can update its properties at any time. If the knowledge agent is in use, updates take effect on the next job.
 
 ## Prerequisites
 
@@ -37,7 +37,7 @@ After you can create a knowledge agent, you can update its properties at any tim
 
 + A search index containing plain text or vectors. The index must [meet the requirements for agentic retrieval](search-agentic-retrieval-how-to-index.md), including a [semantic configuration](semantic-how-to-configure.md) with the `defaultConfiguration` specified.
 
-+ API requirements. To create or use a knowledge agent, use [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API. Or, use a prerelease package of an Azure SDK that provides knowledge agent APIs: [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta3-2025-03-25), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
++ API requirements. To create or use a knowledge agent, use the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API. Or, use a prerelease package of an Azure SDK that provides knowledge agent APIs: [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta3-2025-03-25), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
 
 To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending preview REST API calls to Azure AI Search. There's no portal support at this time.
 
@@ -75,7 +75,7 @@ In Azure, you must have **Owner** or **User Access Administrator** permissions o
 
 1. [Configure Azure AI Search to use a managed identity](search-howto-managed-identities-data-sources.md).
 
-1. On your model provider, such Foundry Model, create a role assignment that gives the search service managed identity **Cognitive Services User** permissions. If you're testing locally, assign yourself to the same role. 
+1. On your model provider, such as Foundry Model, create a role assignment that gives the search service managed identity **Cognitive Services User** permissions. If you're testing locally, assign yourself to the same role. 
 
 1. For local testing, follow the steps in [Quickstart: Connect without keys](search-get-started-rbac.md) to get a personal access token and to ensure you're logged in to a specific subscription and tenant. Paste your personal identity token into the `@accessToken` variable. A request that connects using your personal identity should look similar to the following example:
 
@@ -111,7 +111,7 @@ You can use API keys if you don't have permission to create role assignments.
 
 ## Check for existing knowledge agents
 
-The following request lists knowledge agents by name on your search service. Within the knowledge agents collection, all knowledge agents are uniquely named. It's helpful for knowing about existing knowledge agents for reuse or naming purposes.
+The following request lists knowledge agents by name. Within the knowledge agents collection, all knowledge agents must be uniquely named. It's helpful to know about existing knowledge agents for reuse or for naming new agents.
 
 <!-- ### [**REST APIs**](#tab/rest-get) -->
 
@@ -143,7 +143,6 @@ To create an agent, use the 2025-05-01-preview data plane REST API or an Azure S
 
 ```http
 @search-url=<YOUR SEARCH SERVICE URL>
-@search-api-key=<YOUR SEARCH SERVICE ADMIN API KEY>
 @agent-name=<YOUR AGENT NAME>
 @index-name=<YOUR INDEX NAME>
 @model-provider-url=<YOUR AZURE OPENAI RESOURCE URI>
@@ -222,7 +221,7 @@ Call the **retrieve** action on the knowledge agent object to confirm the model
 Replace "What are my vision benefits?" with a query string that's valid for your search index.
 
 ```http
-# Send Grounding Request
+# Send grounding request
 POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-05-01-preview
    Content-Type: application/json
    Authorization: Bearer {{accessToken}}
@@ -261,7 +260,7 @@ For more information about the **retrieve** API and the shape of the response, s
 If you no longer need the agent, or if you need to rebuild it on the search service, use this request to delete the current object.
 
 ```http
-# Delete Agent
+# Delete agent
 DELETE https://{{search-url}}/agents/{{agent-name}}?api-version=2025-05-01-preview
    Authorization: Bearer {{accessToken}}
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識エージェントの作成に関する記事の更新"
}
```

### Explanation
このコード変更は、知識エージェントの作成に関するAzureのガイド記事に対する修正です。主な変更点には、知識エージェントの作成後にプロパティを更新するプロセスについての記述の微調整が含まれています。また、API要件や役割割り当てに関する具体的な文言が一部修正され、より明確な表現となりました。特に、「モデルプロバイダー」の記述が具体的に「Foundry Model」と修正され、また、知識エージェントのリストアップに関する説明が改善され、エージェント名の一意性がより強調されています。これらの変更により、読者は知識エージェント作成のプロセスや要件をより理解しやすくなります。

## articles/search/search-agentic-retrieval-how-to-index.md{#item-a078ea}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.date: 05/05/2025
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-In Azure AI Search, *agentic retrieval* is a new parallel query architecture that uses a conversational language model for query planning, generating subqueries that broaden the scope of what's searchable and relevant.
+In Azure AI Search, *agentic retrieval* is a new parallel query architecture that uses a chat completion model for query planning, generating subqueries that broaden the scope of what's searchable and relevant.
 
 Queries are created internally. Certain aspects of those generated queries are determined by your search index. This article explains which index elements affect agentic retrieval. None of the required elements are new or specific to agentic retrieval, which means you can use an existing index if it meets the criteria identified in this article, even if it was created using earlier API versions.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的検索取得に関する記事の用語修正"
}
```

### Explanation
このコード変更は、Azure AI Searchにおける「エージェント的検索取得」に関する記事の文言を修正しています。具体的には、「会話型言語モデル」という表現が「チャット完結モデル」に変更され、より正確な用語が使用されるようになりました。この修正により、エージェント的検索取得のアーキテクチャについての理解が進み、より明確に技術的な内容が伝わることを目的としています。記事全体の流れや内容には大きな変更はなく、元の情報はそのまま保持されています。この微調整は技術的な正確性を高めるものであり、読者にとってより有意義な情報を提供するための改訂です。

## articles/search/search-agentic-retrieval-how-to-pipeline.md{#item-1ad1c3}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ This exercise differs from the [Agentic Retrieval Quickstart](search-get-started
 
 The following resources are required for this design pattern:
 
-+ Azure AI Search, basic tier or higher, in a [region that provides semantic ranking](search-region-support.md).
++ Azure AI Search, Basic pricing tier or higher, in a [region that provides semantic ranking](search-region-support.md).
 
 + A search index that satisfies the [index criteria for agentic retrieval](search-agentic-retrieval-how-to-index.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的検索取得パイプラインに関する記事の用語修正"
}
```

### Explanation
このコード変更は、エージェント的検索取得に関するパイプラインの設計パターンを説明する記事に対する微小な修正を行っています。主な変更点は、「基本ティア」という表現が「Basic pricing tier」に修正されたことで、用語の一貫性が向上しました。この修正により、Azure AI Searchの料金体系についての理解がより明確になり、読者が正確な情報を得やすくなります。また、エージェント的検索取得に必要なリソースに関する情報も更新され、特定の条件を満たす検索インデックスが求められることが強調されました。この改訂は内容を正確に保ちながら、読者に対する情報の質を高めることを目的としています。

## articles/search/search-agentic-retrieval-how-to-retrieve.md{#item-5f7fc0}

<details>
<summary>Diff</summary>
````diff
@@ -32,27 +32,27 @@ The retrieve request can include instructions for query processing that override
 
 + A [knowledge agent](search-agentic-retrieval-how-to-create.md) that represents the chat completion model and a valid target index.
 
-+ Azure AI Search, in any [region that provides semantic ranker](search-region-support.md), on basic tier and higher. Your search service must have a [managed identity](search-howto-managed-identities-data-sources.md) for role-based access to a chat completion model.
++ Azure AI Search, in any [region that provides semantic ranker](search-region-support.md), on Basic pricing tier and higher. Your search service must have a [managed identity](search-howto-managed-identities-data-sources.md) for role-based access to a chat completion model.
 
 + Permissions on Azure AI Search. **Search Index Data Reader** can run queries on Azure AI Search, but the search service managed identity must have **Cognitive Services User** permissions on the Azure OpenAI resource. For more information about local testing and obtaining access tokens, see [Quickstart: Connect without keys](search-get-started-rbac.md).
 
-+ API requirements. To create or use a knowledge agent, use [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API. Or, use a prerelease package of an Azure SDK that provides knowledge agent APIs: [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta3-2025-03-25), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
++ API requirements. To create or use a knowledge agent, use the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API. Or, use a prerelease package of an Azure SDK that provides knowledge agent APIs: [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta3-2025-03-25), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
 
 To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending REST API calls to Azure AI Search. There's no portal support at this time.
 
 ## Call the retrieve action
 
 Call the **retrieve** action on the knowledge agent object to invoke retrieval and return a response. Use the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API or an Azure SDK prerelease package that provides equivalent functionality for this task.
 
-All `searchable` fields in the search index are in-scope for query execution. If the index includes vector fields, your index should have a valid vectorizer definition so that it can vectorize the query inputs. Otherwise, vector fields are ignored. The implied query type is `semantic`, and there's no search mode or selection of search fields.
+All `searchable` fields in the search index are in-scope for query execution. If the index includes vector fields, your index should have a valid [vectorizer definition](vector-search-how-to-configure-vectorizer.md) so that it can vectorize the query inputs. Otherwise, vector fields are ignored. The implied query type is `semantic`, and there's no search mode or selection of search fields.
 
 The input for the retrieval route is chat conversation history in natural language, where the `messages` array contains the conversation.
 
 ```http
 @search-url=<YOUR SEARCH SERVICE URL>
 @accessToken=<YOUR PERSONAL ID>
 
-# Send Grounding Request
+# Send grounding request
 POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-05-01-preview
     Content-Type: application/json
     Authorization: Bearer {{accessToken}}
@@ -77,7 +77,7 @@ POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-05-0
     "targetIndexParams" :  [
         { 
             "indexName" : "{{index-name}}",
-            "filterAddOn" : "page_number eq 105'",
+            "filterAddOn" : "page_number eq '105'",
             "IncludeReferenceSourceData": true, 
             "rerankerThreshold" : 2.5,
             "maxDocsForReranker": 50
@@ -130,9 +130,9 @@ The body of the response is also structured in the chat message style format. Cu
 
 **Key points**:
 
-+ `content` is a JSON array. It's a single string composed of the most relevant documents (or chunks) found in the search index, given the query and chat history inputs. This array is your grounding data that a conversational language model uses to formulate a response to the user's question.
++ `content` is a JSON array. It's a single string composed of the most relevant documents (or chunks) found in the search index, given the query and chat history inputs. This array is your grounding data that a chat completion model uses to formulate a response to the user's question.
 
-+ text is the only valid value for type, and the text consists of the reference ID of the chunk (used for citation purposes), and any fields specified in the semantic configuration of the target index. In this example, you should assume the semantic configuration in the target index has a "title" field, a "terms" field, and a "content" filed. 
++ "text" is the only valid value for `type`, and it consists of the reference ID of the chunk (used for citation purposes), and any fields specified in the semantic configuration of the target index. In this example, you should assume the semantic configuration in the target index has a "title" field, a "terms" field, and a "content" field. 
 
 > [!NOTE]
 > The `maxOutputSize` property on the [knowledge agent](search-agentic-retrieval-how-to-create.md) determines the length of the string. We recommend 5,000 tokens.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント的検索取得を用いた検索方法に関する記事の更新"
}
```

### Explanation
このコード変更は、エージェント的検索取得を使用してデータを取得する方法に関する記事の内容を更新しています。主な変更点には、以下のような修正が含まれています。

1. **用語の一貫性**: 「基本ティア」を「Basic pricing tier」に変更し、用語の統一を図っています。
2. **新しいリソースの追加**: 記事に「知識エージェント」の項目が追加され、チャット完結モデルを表す知識エージェントが必要であることが明記されました。
3. **権限に関する詳細**: Azure AI Searchに必要な権限について、具体的なユーザー権限に関する情報が追加されました。
4. **API要件の明確化**: 知識エージェントを作成または使用するためのAPI要件が更新され、バージョン表記が明確化されました。
5. **フィルター条件の修正**: フィルターの条件に関する記述が修正され、より正確な記述に改善されました。
6. **出力データの説明の強化**: レスポンスデータのフォーマットに関する説明が強化され、チャット完結モデルがどのようにユーザーの質問に応答を生成するかが明確に示されています。

これらの修正は、技術文書の理解を深めるために重要であり、読者にとっての情報価値を向上させることを目指しています。全体として、内容の正確性と明瞭さが向上しています。

## articles/search/search-how-to-index-logic-apps-indexers.md{#item-64a12e}

<details>
<summary>Diff</summary>
````diff
@@ -52,7 +52,7 @@ Review the following requirements before you start:
 
 + You must be an **Owner** or **Contributor** in your Azure subscription, with permissions to create resources.
 
-+ Azure AI Search, basic tier or higher if you want to use a search service identity for connections to an Azure data source, otherwise you can use any tier, subject to tier limits. 
++ Azure AI Search, Basic pricing tier or higher if you want to use a search service identity for connections to an Azure data source, otherwise you can use any tier, subject to tier limits. 
 
 + Azure OpenAI, with a [supported embedding model](#supported-models) deployment. Vectorization is integrated into the workflow. If you don't need vectors, you can ignore the fields or try another indexing strategy.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Logic Apps インデクサーに関する記事の用語修正"
}
```

### Explanation
このコード変更は、Logic Appsインデクサーに関する記事の一部を微修正しています。主な変更点は以下の通りです。

1. **権限の明確化**: 「オーナーまたは貢献者である必要があります」という文が追加され、Azureサブスクリプション内でリソースを作成するための権限が明確に示されました。これは、読者に対して必要な権限を理解させるために重要です。

2. **用語の一貫性**: 「基本ティア」という表現が「Basic pricing tier」に変更され、テキスト全体における用語の統一が図られました。これにより、Azureの料金プランに対する理解がよりスムーズになります。

これらの微調整は、文書の読みやすさを向上させ、正確な情報を提供するために寄与しています。全体として、利用者がAzureのサービスを使用する際に遵守すべき要件がより明確に理解できるようになりました。

## articles/search/search-try-for-free.md{#item-36e28d}

<details>
<summary>Diff</summary>
````diff
@@ -127,7 +127,7 @@ Many samples and [accelerators](resource-tools.md) come with bicep scripts that
 
 ## Step four: Track your credits 
 
-During the trial period, you want to stay under the USD 200 credit allocation. Most services are Standard, so you won't be charged while they're not in use, but an Azure AI Search service on the Basic tier is provisioned on dedicated clusters and it can only be used by you. It's billable during its lifetime. If you provision a basic tier search service, expect Azure AI Search to consume about one third of your available credits during the trial period.
+During the trial period, you want to stay under the USD 200 credit allocation. Most services are Standard, so you won't be charged while they're not in use, but an Azure AI Search service on the Basic tier is provisioned on dedicated clusters and it can only be used by you. It's billable during its lifetime. If you provision a basic search service, expect Azure AI Search to consume about one third of your available credits during the trial period.
 
 During the trial period, the Azure portal provides a notification on the top right that tells you how many credits are used up and what remains. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "無料トライアルに関する記事の用語修正"
}
```

### Explanation
このコード変更は、Azureの無料トライアルに関する記事の一部を微調整しています。主な変更点は以下の通りです。

1. **用語の一貫性の向上**: 「基本ティア」という表現が「基本検索サービス」に修正され、用語が統一されました。これにより、読者はサービスの内容についてより明確に理解できるようになります。

この更新は、読者に対する情報の明瞭さを高め、Azureのリソースの使用やトライアル期間中の費用に関する理解をさらに容易にする目的があります。また、誤解を避けるためにも重要な修正です。全体として、記事の内容が利用者にとってより正確かつ理解しやすくなっています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -259,125 +259,7 @@ items:
       href: search-how-to-alias.md
     - name: Import large data sets
       href: search-how-to-large-index.md
-    - name: Logic Apps workflows
-      items:
-      - name: Create a workflow
-        href: search-how-to-index-logic-apps-indexers.md
-    - name: Indexers
-      items:
-      - name: Create an indexer
-        href: search-howto-create-indexers.md
-      - name: Run or reset indexers
-        href: search-howto-run-reset-indexers.md
-      - name: Schedule an indexer
-        href: search-howto-schedule-indexers.md
-      - name: Define field mappings
-        href: search-indexer-field-mappings.md
-      - name: Indexing whole files
-        items:
-        - name: Content metadata properties
-          href: search-blob-metadata-properties.md
-        - name: Index one-to-many
-          href: search-howto-index-one-to-many-blobs.md
-        - name: Index plain text
-          href: search-howto-index-plaintext-blobs.md
-        - name: Index CSV
-          href: search-how-to-index-csv-blobs.md
-        - name: Index JSON
-          href: search-howto-index-json-blobs.md
-        - name: Index Markdown
-          href: search-how-to-index-markdown-blobs.md
-      - name: Troubleshooting guidance
-        href: search-indexer-troubleshooting.md
-      - name: Troubleshoot indexer errors and warnings
-        href: cognitive-search-common-errors-warnings.md
-    - name: Data sources (indexers)
-      items:
-      - name: Data sources gallery
-        href: search-data-sources-gallery.md
-      - name: Azure Storage
-        items:
-        - name: Search over blobs
-          href: search-blob-storage-integration.md
-        - name: ADLS Gen2
-          href: search-howto-index-azure-data-lake-storage.md
-        - name: Blobs
-          href: search-howto-indexing-azure-blob-storage.md
-        - name: Files
-          href: search-file-storage-integration.md
-        - name: Tables
-          href: search-howto-indexing-azure-tables.md
-        - name: Index changed and deleted content
-          href: search-howto-index-changed-deleted-blobs.md
-      - name: Azure Cosmos DB
-        items:
-        - name: Azure Cosmos DB for NoSQL
-          href: search-howto-index-cosmosdb.md
-        - name: Azure Cosmos DB for MongoDB
-          href: search-howto-index-cosmosdb-mongodb.md
-        - name: Azure Cosmos DB for Apache Gremlin
-          href: search-howto-index-cosmosdb-gremlin.md
-      - name: Azure DB for MySQL
-        href: search-howto-index-mysql.md
-      - name: Azure SQL
-        items:
-        - name: Azure SQL Databases
-          href: search-how-to-index-sql-database.md
-        - name: Azure SQL Managed Instances
-          href: search-how-to-index-sql-managed-instance.md
-        - name: Azure SQL Server VMs
-          href: search-how-to-index-sql-server.md
-      - name: OneLake files
-        href: search-how-to-index-onelake-files.md
-      - name: SharePoint Online
-        href: search-howto-index-sharepoint-online.md
-    - name: Skillsets (indexers)
-      items:
-      - name: Create a skillset
-        href: cognitive-search-defining-skillset.md
-      - name: Attach an Azure AI resource
-        href: cognitive-search-attach-cognitive-services.md
-      - name: Define an index projection
-        href: search-how-to-define-index-projections.md
-      - name: Debug sessions overview
-        href: cognitive-search-debug-session.md
-      - name: Debug a skillset
-        href: cognitive-search-how-to-debug-skillset.md
-      - name: Reference a skill output
-        href: cognitive-search-concept-annotations-syntax.md
-      - name: Map to index fields
-        href: cognitive-search-output-field-mapping.md
-      - name: Process image files
-        href: cognitive-search-concept-image-scenarios.md
-      - name: Cache (incremental) enrichment
-        href: search-howto-incremental-index.md
-      - name: Design tips
-        href: cognitive-search-concept-troubleshooting.md
-      - name: Best practices - GenAI Prompt skill
-        href: responsible-ai-best-practices-genai-prompt-skill.md
-      - name: GenAI Prompt Skill - Example Usage Guide
-        href: chat-completion-skill-example-usage.md
-      - name: Custom skills
-        items:
-        - name: Integrate custom skills
-          href: cognitive-search-custom-skill-interface.md
-        - name: Scale out custom skills
-          href: cognitive-search-custom-skill-scale.md
-        - name: Example - Bing Entity Search
-          href: cognitive-search-create-custom-skill-example.md
-  - name: Retrieval
-    items:
-    - name: Agentic retrieval
-      items:
-      - name: Design an index for agentic retrieval
-        href: search-agentic-retrieval-how-to-index.md
-      - name: Create a knowledge agent
-        href: search-agentic-retrieval-how-to-create.md
-      - name: Retrieve data using a knowledge agent
-        href: search-agentic-retrieval-how-to-retrieve.md
-      - name: Build a retrieval pipeline
-        href: search-agentic-retrieval-how-to-pipeline.md
-    - name: Vector search
+    - name: Vector indexing
       items:
       - name: Create a vector index
         href: vector-search-how-to-create-index.md
@@ -407,6 +289,148 @@ items:
           href: vector-search-how-to-storage-options.md
         - name: Truncate dimensions
           href: vector-search-how-to-truncate-dimensions.md
+    - name: Text indexing
+      items:
+      - name: Add synonyms
+        href: search-synonyms.md
+      - name: Add a suggester for typeahead
+        href: index-add-suggesters.md
+      - name: Design a multilingual index
+        href: search-language-support.md
+      - name: Model complex data types
+        href: search-howto-complex-data-types.md
+      - name: Model relational data
+        href: index-sql-relational-data.md
+      - name: Analyzers
+        items:
+        - name: Analyzers overview
+          href: search-analyzers.md
+        - name: Add a language analyzer
+          href: index-add-language-analyzers.md
+        - name: Add a custom analyzer
+          href: index-add-custom-analyzers.md
+    - name: Indexing and enrichment pipelines
+      items:
+      - name: Logic Apps workflows
+        items:
+        - name: Create a workflow
+          href: search-how-to-index-logic-apps-indexers.md
+      - name: Indexers
+        items:
+        - name: Create an indexer
+          href: search-howto-create-indexers.md
+        - name: Run or reset indexers
+          href: search-howto-run-reset-indexers.md
+        - name: Schedule an indexer
+          href: search-howto-schedule-indexers.md
+        - name: Define field mappings
+          href: search-indexer-field-mappings.md
+        - name: Indexing whole files
+          items:
+          - name: Content metadata properties
+            href: search-blob-metadata-properties.md
+          - name: Index one-to-many
+            href: search-howto-index-one-to-many-blobs.md
+          - name: Index plain text
+            href: search-howto-index-plaintext-blobs.md
+          - name: Index CSV
+            href: search-how-to-index-csv-blobs.md
+          - name: Index JSON
+            href: search-howto-index-json-blobs.md
+          - name: Index Markdown
+            href: search-how-to-index-markdown-blobs.md
+        - name: Troubleshooting guidance
+          href: search-indexer-troubleshooting.md
+        - name: Troubleshoot indexer errors and warnings
+          href: cognitive-search-common-errors-warnings.md
+      - name: Data sources (indexers)
+        items:
+        - name: Data sources gallery
+          href: search-data-sources-gallery.md
+        - name: Azure Storage
+          items:
+          - name: Search over blobs
+            href: search-blob-storage-integration.md
+          - name: ADLS Gen2
+            href: search-howto-index-azure-data-lake-storage.md
+          - name: Blobs
+            href: search-howto-indexing-azure-blob-storage.md
+          - name: Files
+            href: search-file-storage-integration.md
+          - name: Tables
+            href: search-howto-indexing-azure-tables.md
+          - name: Index changed and deleted content
+            href: search-howto-index-changed-deleted-blobs.md
+        - name: Azure Cosmos DB
+          items:
+          - name: Azure Cosmos DB for NoSQL
+            href: search-howto-index-cosmosdb.md
+          - name: Azure Cosmos DB for MongoDB
+            href: search-howto-index-cosmosdb-mongodb.md
+          - name: Azure Cosmos DB for Apache Gremlin
+            href: search-howto-index-cosmosdb-gremlin.md
+        - name: Azure DB for MySQL
+          href: search-howto-index-mysql.md
+        - name: Azure SQL
+          items:
+          - name: Azure SQL Databases
+            href: search-how-to-index-sql-database.md
+          - name: Azure SQL Managed Instances
+            href: search-how-to-index-sql-managed-instance.md
+          - name: Azure SQL Server VMs
+            href: search-how-to-index-sql-server.md
+        - name: OneLake files
+          href: search-how-to-index-onelake-files.md
+        - name: SharePoint Online
+          href: search-howto-index-sharepoint-online.md
+      - name: Skillsets (indexers)
+        items:
+        - name: Create a skillset
+          href: cognitive-search-defining-skillset.md
+        - name: Attach an Azure AI resource
+          href: cognitive-search-attach-cognitive-services.md
+        - name: Define an index projection
+          href: search-how-to-define-index-projections.md
+        - name: Debug sessions overview
+          href: cognitive-search-debug-session.md
+        - name: Debug a skillset
+          href: cognitive-search-how-to-debug-skillset.md
+        - name: Reference a skill output
+          href: cognitive-search-concept-annotations-syntax.md
+        - name: Map to index fields
+          href: cognitive-search-output-field-mapping.md
+        - name: Process image files
+          href: cognitive-search-concept-image-scenarios.md
+        - name: Cache (incremental) enrichment
+          href: search-howto-incremental-index.md
+        - name: Design tips
+          href: cognitive-search-concept-troubleshooting.md
+        - name: Best practices - GenAI Prompt skill
+          href: responsible-ai-best-practices-genai-prompt-skill.md
+        - name: GenAI Prompt Skill - Example Usage Guide
+          href: chat-completion-skill-example-usage.md
+        - name: Custom skills
+          items:
+          - name: Integrate custom skills
+            href: cognitive-search-custom-skill-interface.md
+          - name: Scale out custom skills
+            href: cognitive-search-custom-skill-scale.md
+          - name: Example - Bing Entity Search
+            href: cognitive-search-create-custom-skill-example.md
+  - name: Retrieval
+    items:
+    - name: Agentic retrieval
+      items:
+      - name: Design an index for agentic retrieval
+        href: search-agentic-retrieval-how-to-index.md
+      - name: Create a knowledge agent
+        href: search-agentic-retrieval-how-to-create.md
+      - name: Retrieve data using a knowledge agent
+        href: search-agentic-retrieval-how-to-retrieve.md
+      - name: Build a retrieval pipeline
+        href: search-agentic-retrieval-how-to-pipeline.md
+    - name: Vector search
+      items:
       - name: Query vectors
         href: vector-search-how-to-query.md
       - name: Use multi-vector fields
@@ -427,24 +451,6 @@ items:
         href: search-query-simple-examples.md
       - name: Add spell check
         href: speller-how-to-add.md
-      - name: Add synonyms
-        href: search-synonyms.md
-      - name: Add a suggester for typeahead
-        href: index-add-suggesters.md
-      - name: Design a multilingual index
-        href: search-language-support.md
-      - name: Model complex data types
-        href: search-howto-complex-data-types.md
-      - name: Model relational data
-        href: index-sql-relational-data.md
-      - name: Analyzers
-        items:
-        - name: Analyzers overview
-          href: search-analyzers.md
-        - name: Add a language analyzer
-          href: index-add-language-analyzers.md
-        - name: Add a custom analyzer
-          href: index-add-custom-analyzers.md
       - name: Filters and facets
         items:
         - name: Filters in text queries
@@ -504,7 +510,7 @@ items:
         href: service-create-private-endpoint.md
       - name: Troubleshoot private connections
         href: troubleshoot-shared-private-link-resources.md
-      - name: Connect using Network Security Perimeter
+      - name: Join a network security perimeter
         href: search-security-network-security-perimeter.md
     - name: Authentication and authorization
       items:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピック構成の更新"
}
```

### Explanation
このコード変更は、Azureに関するトピック構成ファイル（toc.yml）を大幅に改訂しています。主要な変更点は以下の通りです。

1. **セクションの再編成**: いくつかのセクションが統合、削除、または新設され、ドキュメントの構成がより整理されました。特に、「インデクシングとエンリッチメントパイプライン」や「テキストインデクシング」などの新しいセクションが追加され、より多様なトピックがカバーされています。

2. **コンテンツの削減と追加**: 多くのリンクが削除される一方で、新しいトピックやサブトピックが追加され、全体的に282の変更が行われました。これにより、各トピックについての情報が最新のものへと更新され、一貫性が高まっています。

3. **新しいキーワードの導入**: 「ベクトルインデクシング」や「エージェント的検索」などの新しい機能に対応するための項目が追加され、最新の技術動向にも対応しています。

このような変更により、サービスの利用者に対して、Azureの機能やサービスに関するより効率的で組織化された情報を提供することが可能となります。全体として、ユーザーが関連情報を探しやすくなり、利便性が向上します。

## articles/search/tutorial-document-extraction-image-verbalization.md{#item-398a90}

<details>
<summary>Diff</summary>
````diff
@@ -51,7 +51,7 @@ Using a REST client and the [Search REST APIs](/rest/api/searchservice/) you wil
 
 + [Azure Storage](/azure/storage/common/storage-account-create).
 
-+ [Azure AI Search](search-what-is-azure-search.md), basic tier or higher, with a managed identity. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription.  
++ [Azure AI Search](search-what-is-azure-search.md), Basic pricing tier or higher, with a managed identity. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription.  
 
 + [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchの価格プランについての修正"
}
```

### Explanation
このコード変更は、ドキュメント抽出と画像のバーバライゼーションに関するチュートリアル記事の内容を微調整しています。主な変更点は以下の通りです。

1. **価格プランの明確化**: 「basic tier」という表現が「Basic pricing tier」に修正され、価格体系に関する記述がより明確になりました。この修正により、読者がAzure AI Searchの利用における価格体系をより理解しやすくしています。

2. **文言の修正**: 一部の文言が微調整され、読みやすさが向上しました。この小さな変更が、全体的な理解を助ける結果となります。

この更新は、ユーザーが適切なサービスを選択する際に必要な情報を分かりやすく提供することを目指しています。全体として、チュートリアルの信頼性と一貫性が向上し、ユーザーにとっての利便性が増しています。


