---
date: '2024-10-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3cec18b...MicrosoftDocs:0a8084e
summary: このコード差分では、Azure AI Searchドキュメンテーションに対する一連のマイナーアップデートと新機能の追加が行われました。主な新機能として、新規ユーザー向けのAzure
  AI Searchを無料で試すためのガイドと関連画像が追加されました。他の更新内容には、スコアリングプロファイルや類似性に関するドキュメントの改善、地域サポートやSKUティアの情報更新が含まれ、ユーザーの利便性と理解度を高めることを目的としています。現時点で破壊的変更はなく、特にチュートリアルの更新が初心者にとって有益な情報源となっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3cec18b...MicrosoftDocs:0a8084e){target="_blank"}

# ハイライト
このコード差分 (diff) では、Azure AI Searchドキュメンテーションに対する一連のマイナーアップデートおよび新機能の追加が行われました。重要な新機能として、Azure AI Searchを無料で試すためのガイドおよび関連画像が追加されました。主な更新内容にはスコアリングプロファイル、類似性およびスコアリングに関するドキュメントの改善、地域サポートおよびSKUティアの情報更新などが含まれます。

## 新機能
- **Azure AI Searchを無料で試すためのガイドの追加**: 新規ユーザー向けにAzure AI Searchを無料で試すための詳細なガイド（`articles/search/search-try-for-free.md`）と関連画像（`articles/search/media/search-try-for-free/azure-ai-service-marketplace.png`）が追加されました。
- **目次に新セクションの追加**: `toc.yml`に「無料で検索を試す」セクションが追加されました。

## 破壊的変更
現時点では、差分に破壊的変更は含まれていません。

## その他の更新
- **スコアリングプロファイルに関する文書更新**: スコアリング機能やBM25ランク付けに関する詳細が強化。
- **類似性およびスコアリングに関する文書更新**: `featuresMode`パラメータおよびBM25スコアに関する詳細説明の追加。
- **検索地域サポート情報の更新**: 特定地域のサービス稼働状況に関する注釈の更新。
- **検索SKUティア情報の更新**: East US地域のSKUティアの利用可能性に関する情報の追加。
- **チュートリアルの更新および日時の修正**: 「RAGソリューションモデルを構築する」チュートリアルの更新、日付修正および説明文の改善。

# インサイト
今回のドキュメンテーション更新では、Azure AI Searchの各種機能についてユーザーフレンドリーな情報提供が強化されています。特に新規ユーザー向けの無料トライアルガイドとそれに関連する目次の整理は、迅速かつ効率的にサービスを試用できるようにするための重要なステップです。

スコアリングプロファイル関連の文書更新は、ユーザーが検索結果のランク付けやスコアリングの仕組みをより深く理解できるようにすることを目的としています。BM25ランク付けや`featuresMode`パラメータに関する詳細な説明は、関連性の高い検索結果をユーザーに提供する際の一助となるでしょう。さらに、地域サポートおよびSKUティア情報の更新は、ユーザーがリソースの選択や計画を行う際に重要な情報を提供し、サービスの利用において現実的な期待値を設定するのに役立ちます。

チュートリアルの更新に関しては、具体的な操作手順やリソースの利用方法がより明確に示されており、特に初学者にとって有益な情報源となっています。こうした改善は、Azure AI Searchの利便性と理解度を高め、ユーザーの成功を支援する重要なツールです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | 検索スコアリングプロファイルの追加に関するドキュメントの更新 | modified | 11 | 6 | 17 | 
| [index-similarity-and-scoring.md](#item-75603d) | minor update | 類似性およびスコアリングに関するドキュメントの更新 | modified | 3 | 3 | 6 | 
| [scoring-over-ranked-results.png](#item-bee24f) | minor update | スコアリングプロファイルに関する画像の更新 | modified | 0 | 0 | 0 | 
| [azure-ai-service-marketplace.png](#item-2096ec) | new feature | Azure AIサービスのマーケットプレイスに関する画像の追加 | added | 0 | 0 | 0 | 
| [search-region-support.md](#item-25b0f1) | minor update | 検索地域サポートに関する情報の更新 | modified | 6 | 6 | 12 | 
| [search-sku-tier.md](#item-7686b8) | minor update | 検索SKUティアに関する情報の更新 | modified | 1 | 0 | 1 | 
| [search-try-for-free.md](#item-36e28d) | new feature | Azure AI Searchを無料で試すためのガイドの追加 | added | 163 | 0 | 163 | 
| [toc.yml](#item-c4768f) | minor update | 目次に「無料で検索を試す」セクションの追加 | modified | 2 | 0 | 2 | 
| [tutorial-rag-build-solution-models.md](#item-6796c9) | minor update | チュートリアルの更新と日時の修正 | modified | 9 | 9 | 18 | 


# Modified Contents
## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 09/23/2024
+ms.date: 10/01/2024
 ---
 
 # Add scoring profiles to boost search scores
@@ -89,14 +89,19 @@ See the [Extended example for vector and hybrid search](#extended-example-for-ve
 
 ## How search scoring works in Azure AI Search
 
-Scoring profiles supplement the default scoring algorithm by boosting the scores of matches that meet the profile's criteria. Scoring functions apply to keyword search, pure vector queries, and on hybrid queries. 
+Scoring profiles supplement the default scoring algorithm by boosting the scores of matches that meet the profile's criteria. Scoring functions apply to:
 
-When you use scoring profiles or any other boosting features in Azure AI Search, the [Reciprocal Ranking Function (RRF)](hybrid-search-ranking.md) algorithm assigns the score, including for standalone text and vector queries. Post-RRF, all scoring/boosting, [semantic ranking](semantic-search-overview.md), and [vector weighting](vector-search-how-to-query.md#vector-weighting) adjustments occur.
++ [Text (keyword) search](search-query-create.md)
++ [Pure vector queries](vector-search-how-to-query.md)
++ [Hybrid queries](hybrid-search-how-to-query.md), with text and vector subqueries execute in parallel
 
-:::image type="content" source="media/scoring-profiles/scoring-over-ranked-results.png" alt-text="Diagram showing which fields have a scoring profile and when ranking occurs.":::
+For standalone text queries, scoring profiles identify the maximum 1,000 matches in a [BM25-ranked search](index-similarity-and-scoring.md), and the top 50 are returned in results.
+
+For pure vectors, the query is vector-only, but the [*k*-matching documents](vector-search-ranking.md) include alphanumeric fields that a scoring profile can process. The scoring profile revised the result set by boosting documents that match criteria in the profile.
 
-> [!TIP]
-> You can use the [featuresMode (preview)](index-similarity-and-scoring.md#featuresmode-parameter-preview) parameter to request extra scoring details with the search results (including the field level scores).
+For text queries in a hybrid query, scoring profiles identify the maximum 1,000 matches in a BM25-ranked search. However, once those 1,000 results are identified, they're restored to their original BM25 order so that they can be rescored alongside vectors results in the final [Reciprocal Ranking Function (RRF)](hybrid-search-ranking.md) ordering, where the scoring profile (document boosting) is applied to the merged results, followed by [vector weighting](vector-search-how-to-query.md#vector-weighting), and [semantic ranking](semantic-search-overview.md) as the last step.
+
+:::image type="content" source="media/scoring-profiles/scoring-over-ranked-results.png" alt-text="Diagram showing which fields have a scoring profile and when ranking occurs.":::
 
 ## Add a scoring profile to a search index
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索スコアリングプロファイルの追加に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるスコアリングプロファイルの使用に関する文書を更新するものです。主な内容としては、ドキュメントの日付が2024年10月1日に変更され、スコアリングプロファイルの適用がより明確に説明されています。新たに追加された点としては、スコアリング関数が適用される具体的な検索タイプ（テキスト検索、純ベクタークエリ、ハイブリッドクエリ）が箇条書きで示されています。

また、スコアリングプロファイルがBM25ランク付けの検索で最大1,000の一致を特定する方法についても詳しく説明されており、検索結果の最終的な順位付けにおいてスコアリングプロファイルがどのように適用されるかに関する重要なポイントが強調されています。これにより、ユーザーはスコアリングプロファイルの利点をより理解しやすくなっています。

全体として、これらの変更は内容の明瞭性と有用性を向上させ、ユーザーが検索機能を最大限に活用できるようにすることを目的としています。

## articles/search/index-similarity-and-scoring.md{#item-75603d}

<details>
<summary>Diff</summary>
````diff
@@ -131,13 +131,13 @@ In Azure AI Search, you can configure BM25 algorithm parameters, and tune search
 | [Scoring algorithm configuration](index-ranking-similarity.md) | Search index |  |
 | [Scoring profiles](index-add-scoring-profiles.md) | Search index | Provide criteria for boosting the search score of a match based on content characteristics. For example, you might want to boost matches based on their revenue potential, promote newer items, or perhaps boost items that have been in inventory too long. A scoring profile is part of the index definition, composed of weighted fields, functions, and parameters. You can update an existing index with scoring profile changes, without incurring an index rebuild.|
 | [Semantic ranking](semantic-search-overview.md) | Query request | Applies machine reading comprehension to search results, promoting more semantically relevant results to the top. |
-| [featuresMode parameter](#featuresmode-parameter-preview) | Query request | This parameter is mostly used for unpacking a score, but it can be used for in code that provides a [custom scoring solution](https://github.com/Azure-Samples/search-ranking-tutorial). |
+| [featuresMode parameter](#featuresmode-parameter-preview) | Query request | This parameter is mostly used for unpacking a BM25-ranked score, but it can be used for in code that provides a [custom scoring solution](https://github.com/Azure-Samples/search-ranking-tutorial). |
 
 <a name="featuresMode-param"></a>
 
 ## featuresMode parameter (preview)
 
-[Search Documents](/rest/api/searchservice/documents/search-post) requests support a featuresMode parameter that provides more detail about a relevance score at the field level. Whereas the `@searchScore` is calculated for the document all-up (how relevant is this document in the context of this query), featuresMode reveals information about individual fields, as expressed in a `@search.features` structure. The structure contains all fields used in the query (either specific fields through **searchFields** in a query, or all fields attributed as **searchable** in an index). 
+[Search Documents](/rest/api/searchservice/documents/search-post) requests support a featuresMode parameter that provides more detail about a BM25 relevance score at the field level. Whereas the `@searchScore` is calculated for the document all-up (how relevant is this document in the context of this query), featuresMode reveals information about individual fields, as expressed in a `@search.features` structure. The structure contains all fields used in the query (either specific fields through **searchFields** in a query, or all fields attributed as **searchable** in an index). 
 
 For each field, `@search.features` give you the following values:
 
@@ -169,7 +169,7 @@ For a query that targets the "description" and "title" fields, a response that i
 
 You can consume these data points in [custom scoring solutions](https://github.com/Azure-Samples/search-ranking-tutorial) or use the information to debug search relevance problems.
 
-The featuresMode parameter isn't documented in the REST APIs, but you can use it on a preview REST API call to Search Documents.
+The featuresMode parameter isn't documented in the REST APIs, but you can use it on a preview REST API call to Search Documents for text (Keyword) search that's BM25-ranked.
 
 ## Number of ranked results in a full text query response
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "類似性およびスコアリングに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchの類似性およびスコアリングに関するドキュメントを更新するもので、特にBM25スコアの詳細に焦点を当てています。具体的には、`featuresMode`パラメータに関する説明が強化されました。このパラメータは、スコアの詳細をフィールドレベルで提供するもので、BM25ランク付きスコアに関して明確に言及されています。

変更内容には、`featuresMode`パラメータがBM25関連のスコアを扱うことが明記され、またスコアの解析方法や、カスタムスコアリングソリューションの利用方法についても言及されています。これにより、ユーザーはより詳細なスコアリング情報を得るための手法を理解しやすくなっています。

全体として、この更新はユーザーがスコアリング機能をより適切に利用できるようにし、検索の関連性問題をデバッグする際の助けとなることを目的としています。

## articles/search/media/scoring-profiles/scoring-over-ranked-results.png{#item-bee24f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリングプロファイルに関する画像の更新"
}
```

### Explanation
この変更は、Azure AI Searchに関連するドキュメント内の画像ファイルに関するもので、特に「ランキングされた結果に対するスコアリング」の図を対象としています。具体的な追加や削除は行われていませんが、画像の内容やメタデータに何らかの修正が行われた可能性があります。

画像はスコアリングプロファイルの理解を助けるために重要であり、この更新により、ユーザーは検索結果におけるスコアの仕組みを視覚的に把握しやすくなります。今後この図がドキュメント内でどのように利用されるかが、ユーザーに対する情報提供の質を向上させることにつながるでしょう。

## articles/search/media/search-try-for-free/azure-ai-service-marketplace.png{#item-2096ec}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AIサービスのマーケットプレイスに関する画像の追加"
}
```

### Explanation
この変更は、Azure AI Service Marketplaceに関連する新しい画像ファイルが追加されたことを示しています。この画像は、無料で試すための検索機能に関連しており、ユーザーがAzure AIサービスを視覚的に理解する手助けとなります。

新たに追加された画像は、Azureのサービスを利用する際のプロセスや利点を示す情報を提供する可能性があり、ユーザーがサービスの概要を把握しやすくなります。これにより、ドキュメントの内容がより充実し、利用者にとって魅力的な情報源となることでしょう。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.author: heidist
 ms.service: cognitive-search
 ms.topic: conceptual
 ms.custom: references_regions
-ms.date: 09/19/2024
+ms.date: 09/29/2024
 
 ---
 
@@ -40,19 +40,19 @@ You can create an Azure AI Search resource in any of the following Azure public
 | Brazil South​​ ​ | ✅ | ✅ | |
 | Canada Central​​ | ✅ | ✅ | ✅ |
 | Canada East​​ ​ |  | ✅ | |
-| East US​ | ✅ | ✅ | ✅ |
+| East US​ <sup>1</sup>| ✅ | ✅ | ✅ |
 | East US 2 ​ | ✅ | ✅ | ✅ |
-| ​Central US​​ <sup>1</sup> | ✅ | ✅ | ✅ |
+| ​Central US​​ <sup>2</sup> | ✅ | ✅ | ✅ |
 | North Central US​ ​ | ✅ | ✅ | |
 | South Central US​ <sup>2</sup>​ | ✅ | ✅ | ✅ |
 | West US​ ​ | ✅ | ✅ | |
 | West US 2​ ​ | ✅ | ✅ | ✅ |
-| West US 3​ <sup>2</sup>​ | ✅ | ✅ |✅ |
+| West US 3​ <sup>1</sup>​ | ✅ | ✅ |✅ |
 | West Central US​ ​ | ✅ | ✅ | |
 
-<sup>1</sup> This region has capacity, but some tiers are [not available](search-sku-tier.md#region-availability-by-tier). 
+<sup>1</sup> Currently, this region is at full capacity and not accepting new search services. 
 
-<sup>2</sup> Currently, this region is at full capacity and not accepting new search services. 
+<sup>2</sup> This region has capacity, but some tiers are [not available](search-sku-tier.md#region-availability-by-tier). 
 
 ### Europe
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索地域サポートに関する情報の更新"
}
```

### Explanation
この変更は、「検索地域サポート」に関するMarkdownファイルが修正されたことを示しています。具体的には、日付の更新や、特定の地域におけるサービスの稼働状況に関する注釈が更新されています。特に、いくつかの地域が満杯で新しい検索サービスを受け付けていないことが明記されています。

ファイル内では、Azure AI Searchリソースを作成できる地域のリストがあり、それぞれに対するサポート状況が記載されています。変更により、ユーザーは地域ごとのサービスの可用性や制限についての情報がより正確に把握できるようになります。この更新は、利用者にとって重要なものであり、Azureサービスの利用計画に役立つでしょう。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -60,6 +60,7 @@ Currently, several regions are at capacity for specific tiers and can't be used
 | Region | Disabled tier (SKU) due to over-capacity |
 |--------|------------------------------------------|
 | Central US | S2, S3, S3HD, L1, L2 |
+| East US| All tiers|
 | Japan East | S2, S3, S3HD, L1, L2 |
 | Qatar Central | All tiers|
 | South Central US | All tiers |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索SKUティアに関する情報の更新"
}
```

### Explanation
この変更は、「検索SKUティア」に関するMarkdownファイルにおいて、特定の地域でのSKUの可用性に関する情報が更新されたことを示しています。具体的には、East US地域のすべてのSKUティアがオーバーキャパシティで利用できないことが新たに追加されました。

この更新は、ユーザーがAzure AI Searchサービスを利用する際に、どの地域で特定のティアが使用できないかを正確に理解するのを助けるためのものです。これにより、利用者はリソースの選択や計画をより適切に行うことができます。このような情報は、サービスの運用において重要な考慮事項となるため、文書の精度を高めます。

## articles/search/search-try-for-free.md{#item-36e28d}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,163 @@
+---
+title: 'Try Azure AI Search for free'
+titleSuffix: Azure AI Search
+description: Learn how to create a trial subscription and use credits for trying advanced features.
+
+manager: nitinme
+author: HeidiSteen
+ms.author: heidist
+ms.service: cognitive-search
+ms.topic: conceptual
+ms.date: 09/18/2024
+ms.custom: references_regions
+---
+
+# Try Azure AI Search for free
+
+If you're new to Azure, you can set up a free trial subscription to explore Azure AI Search and other services at no charge. Information retrieval over your own content is useful for many scenarios including AI generative search.
+
+This article explains how to get the most value from your Azure trial subscription so that you can complete your evaluation of Azure AI Search quickly and efficiently.
+
+## Step one: Sign up for a free subscription
+
+To try Azure AI Search for free, [start a trial subscription](https://azure.microsoft.com/pricing/free-trial/?WT.mc_id=A261C142F). The trial subscription is nonrenewable, active for one month, and comes with free credits so that you can create billable services at no charge. 
+
+At this point in time, the credit is equivalent to USD 200. As always, the exact amount is subject to change, but you can verify the credit on the trial subscription sign-up page.
+
+> [!div class="nextstepaction"]
+> [Start your free trial subscription](https://azure.microsoft.com/pricing/free-trial/?WT.mc_id=A261C142F)
+
+Once you sign up, you can immediately use either of these links to access Azure resources and experiences:
+
++ [Sign in to Azure portal](https://portal.azure.com/) to view, manage, and create more resources. You can also use the portal to track your credits and projected costs.
+
++ [Sign in to Azure AI Studio](https://ai.azure.com) for a no-code approach to deploying models on Azure OpenAI and using Azure AI Search for information retrieval. **We recommend you start here first.**
+
+<!-- Although you can create a free search service that doesn't use up your credits, we recommend provisioning the **Basic** tier so that you can work with larger indexes, more indexes, and premium features like semantic ranking.
+
+The [Azure portal](https://portal.azure.com/) is the easiest approach for first-time users who want to create and use Azure resources. You can access and manage all of your subscriptions and resources from the portal. For Azure AI Search, you can use the portal to build components for classic search scenarios and generative search (RAG) workloads. -->
+
+## Step two: "Day One" tasks
+
+[**How to build and consume vector indexes in Azure AI Studio**](/azure/ai-studio/how-to/index-add) is a great place to start.
+
+1. [Sign in to Azure AI Studio](https://ai.azure.com).
+
+1. Create a new hub and project.
+
+1. On the left, under **Components**, select **Indexes**. The Create Index wizard guides you through the remaining tasks.
+
+   + On the **Source Data** page, if you have local files that you want to query using an LLM, upload them. 
+
+   + On the **Index Settings**, you can create a new Azure AI Search service. The wizard selects a matching region automatically, but you choose the pricing tier.
+
+     We recommend Basic for larger data files and more indexes, or Free if your files are less than 50 MB. Basic has more features and storage, but it's billable for the lifetime of the service and it might consume about one third of your available credits if you retain it for the entire trial period.
+
+> [!TIP]
+> Azure AI Search and Azure OpenAI must be in the same region. Currently, these regions provide the most overlap and capacity: **East US**, **East US2**, and **South Central** in the Americas; **France Central** or **Switzerland North** in Europe; **Australia East** in Asia Pacific.
+
+## Step three: Have a plan for next steps
+
+The trial period can go by quick. Having a plan of action can help you get the most out of your trial subscription. For Azure AI Search, most newer customers and developers are exploring RAG patterns.
+
+For a next step evaluation of [RAG scenarios](retrieval-augmented-generation-overview.md), you should have three or five Azure resources for:
+
+- Storing data
+- Deploying embedding and chat models (**Azure OpenAI**)
+- Applying AI services for creating AI-generated content during indexing (optional)
+- Adding information retrieval (**Azure AI Search**)
+- Adding a frontend app (optional)
+
+Many of our quickstarts and tutorials use Azure Storage, so we recommend creating an Azure Storage account for getting started.
+
+Generative search requires embedding and chat models. The Azure cloud provides Azure OpenAI, but you can also use Azure AI Vision for multimodal embeddings (but not chat). Another model provider is Azure AI Studio and deploying chat and embedding models into the model catalog. However, for initial exploration, we recommend Azure OpenAI for its familiarity and mainstream offerings.
+
+Application frontends are useful if you're prototyping a solution for a wider audience. You can use Azure Web apps or build an ASP.NET MVC application for this task. Otherwise, if you're working locally, you can view output in Jupyter notebooks in Visual Studio Code or another IDE. Or view results in console apps or other apps that run on localhost.
+
+<!-- ## Check regions
+
+Azure AI Search has integrated operations with applied AI in the Azure cloud. Integration depends on services running within the same region. This is a requirement for data residency and for efficient operations.
+
+Verifying region availability can save you time and frustration because you need to choose a region that supports all of the services you want to use.
+
+Start here:
+
+- [Azure AI Search region list](search-region-support.md). This list identifies region support for Azure AI Search, applied AI (Azure AI multiservice), and semantic ranking. You don't need a separate region check for applied AI.
+
+  West Europe and West US 2/3 are currently at capacity for Azure AI Search and aren't accepting new search services.
+
+Continue with the following links to review which regions also provide the model provider that you want to use.
+
+- [Azure OpenAI region list](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)
+- [Azure AI Vision region list](/azure/ai-services/computer-vision/overview-image-analysis?tabs=4-0#region-availability)
+- [Azure AI Studio region list](/azure/ai-studio/reference/region-support)
+
+> [!TIP]
+> Currently, these regions provide the most overlap and capacity: **East US**, **East US2**, and **South Central** in the Americas; **France Central** or **Switzerland North** in Europe; **Australia East** in Asia Pacific.
+>
+> For Azure AI Vision and AI Search interoperability, choose one of these regions: **East US**, **France Central**, **Korea Central**, **North Europe**, **South East Asia**, or **West US**. -->
+
+### Create services
+
+1. [Create a search service](search-create-service-portal.md) if you don't have one already, choosing the Basic tier and a region that also offers a model provider. Most Azure AI Search regions provide higher capacity storage limits. There are just a few that have older and lower limits. For the Basic tier, as you install, confirm that you have a 15-GB partition.
+
+   > [!div class="nextstepaction"]
+   > [Create a search service](search-create-service-portal.md)
+
+1. [Create an Azure Storage account](/azure/storage/common/storage-account-create?tabs=azure-portal), choosing a general purpose account and using default settings.
+
+1. [Create an Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource?pivots=web-portal) as your model provider.
+
+1. [Create an Azure AI multiservice account](/azure/ai-services/multi-service-resource?pivots=azportal) to use applied AI in your indexing workloads and Azure AI Vision multimodal APIs as an embedding model provider. You can create and transform content during indexing if applied AI can be attached. For multimodal APIs, make sure you choose a region that provides those APIs. Look for this tile in the Azure Marketplace:
+
+   :::image type="content" source="./media/search-try-for-free/azure-ai-service-marketplace.png" alt-text="Screenshot of the Azure AI Services offering in the Azure Marketplace.":::
+
+### Try the quickstarts
+
+Try the portal quickstarts for Azure AI Search or quickstarts that use Visual Studio Code with REST or Python extensions.  It's the fastest approach creating searchable content, and you don't need coding skills to complete the tasks.
+
+- [Quickstart: Vector search in the Azure portal](search-get-started-portal-import-vectors.md)
+- [Quickstart: Image search in the Azure portal](search-get-started-portal-image-search.md)
+- [Quickstart: Keyword in the Azure portal](search-get-started-portal.md)
+- [Quickstart: Generative search (RAG) using a Python client](search-get-started-rag.md)
+- [Quickstart: Vector search using a REST client](search-get-started-vector.md)
+
+Azure AI Studio and Azure OpenAI Studio support connecting to content in Azure AI Search
+
+- [Quickstart: Chat using your own data in Azure OpenAI Studio](/azure/ai-services/openai/use-your-data-quickstart)
+- [Tutorial: Build a custom chat app with the prompt flow SDK](/azure/ai-studio/tutorials/copilot-sdk-create-resources)
+
+Developers should review [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) repository or the solution accelerators. You can deploy and run any of these samples using the Azure trial subscription. 
+
+Many samples and [accelerators](resource-tools.md) come with bicep scripts that deploy all Azure resources and dependencies, so you can skip installation steps and explore an operational solution as soon as the development completes.
+
+## Step four: Track your credits 
+
+During the trial period, you want to stay under the USD 200 credit allocation. Most services are pay-as-you-go, so you won't be charged while they're not in use, but an Azure AI Search service on the Basic tier is provisioned on dedicated clusters and it can only be used by you. It's billable during its lifetime. If you provision a basic tier search service, expect Azure AI Search to consume about one third of your available credits during the trial period.
+
+During the trial period, the Azure portal provides a notification on the top right that tells you how many credits are used up and what remains. 
+
+You can also monitor billing by searching for *subscriptions* in the Azure portal to view subscription information at any time. The Overview page gives you spending rates, forecasts, and cost management. For more information, see [Check usage of free services included with your Azure free account](/azure/cost-management-billing/manage/check-free-service-usage).
+
+## Consider the free tier
+
+You can create a search service that doesn't consume credits. Here are some points about the free tier to keep in mind:
+
++ You can have one free search service per Azure subscription.
++ You can complete all of the quickstarts and most tutorials, except for those featuring semantic ranking and managed identities for Microsoft Entra ID authentication and authorization.
++ Storage is capped at 50 MB.
++ You can have up to three indexes, indexers, data sources, and skillset at one time.
+
+Review the [service limits](search-limits-quotas-capacity.md) for other constraints that apply to the free tier.
+
+## Next steps
+
+Sign up for an Azure trial subscription:
+
+> [!div class="nextstepaction"]
+> [Start your free trial subscription](https://azure.microsoft.com/pricing/free-trial/?WT.mc_id=A261C142F)
+
+When you're ready, add Azure AI Search as your first resource:
+
+> [!div class="nextstepaction"]
+> [Create a search service](search-create-service-portal.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Searchを無料で試すためのガイドの追加"
}
```

### Explanation
この変更は、「Azure AI Searchを無料で試す」という新しいガイドがMarkdownファイルとして追加されたことを示しています。この文書は、Azureの新規ユーザーが無料トライアルサブスクリプションを設定し、Azure AI Searchやその他のサービスを利用する方法を詳しく説明しています。

ガイドには、無料トライアルのサインアップ手順、Azureリソースへのアクセス方法、初期のアクションプラン、クレジットの管理方法、無料ティアの考慮点が含まれています。特に、ユーザーが試用期間中にAzure AI Searchを最大限に活用するための具体的なステップや推奨リソースが示されています。

この文書は、トライアルサブスクリプションの利点を活用できるように設計されており、特にサービスの利用を迅速かつ効率的に評価するための具体的な指針を提供しています。新規ユーザーはこの情報を活用して、Azure AI Searchや関連的なサービスを深く理解することが可能となります。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -10,6 +10,8 @@ items:
     href: whats-new.md
   - name: Features
     href: search-features-list.md
+  - name: Try search for free
+    href: search-try-for-free.md
   - name: FAQ
     href: search-faq-frequently-asked-questions.yml
 - name: Quickstarts
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次に「無料で検索を試す」セクションの追加"
}
```

### Explanation
この変更は、目次ファイル（toc.yml）に新しいセクション「無料で検索を試す」が追加されたことを示しています。このセクションは、Azure AI Search関連の情報を帳簿の中で見つけやすくするためのもので、特に新規ユーザー向けに無料トライアルの情報を提供することを目的としています。

具体的には、この変更により、ユーザーは新しく追加された「search-try-for-free.md」ファイルにアクセスできるようになります。この新しいセクションは、Azure AI Searchを無料で試す方法や手順に関する重要な情報を簡単に見つける手助けをします。

全体として、この更新は、文書構造を改善し、読者が必要な情報を迅速に見つけやすくするためのものです。

## articles/search/tutorial-rag-build-solution-models.md{#item-6796c9}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.author: heidist
 ms.service: cognitive-search
 ms.topic: tutorial
 ms.custom: references_regions
-ms.date: 09/12/2024
+ms.date: 09/30/2024
 
 ---
 
@@ -32,7 +32,7 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 
 - The Azure portal, used to deploy models and configure role assignments in the Azure cloud.
 
-- An **Owner** role on your Azure subscription, necessary for creating role assignments. Your model provider has more role requirements for deploying and accessing models. Those are noted in the following steps.
+- An **Owner** role on your Azure subscription, necessary for creating role assignments. You use at least three Azure resources in this tutorial. The connections are authenticated using Microsoft Entra ID, which requires the ability to create roles. Role assignments for connecting to models are documented in this article.
 
 - A model provider, such as [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource), Azure AI Vision via an [Azure AI multi-service account](/azure/ai-services/multi-service-resource), or [Azure AI Studio](https://ai.azure.com/).
 
@@ -51,25 +51,25 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
   Azure AI Search is currently facing limited availability in some regions, such as West Europe and West US 2/3. Check the [Azure AI Search region list](search-region-support.md) to confirm region status.
 
 > [!TIP]
-> Currently, the following regions provide the most overlap among the model providers and have the most capacity: **East US**, **East US2**, and **South Central** in the Americas; **France Central** or **Switzerland North** in Europe; **Australia East** in Asia Pacific.
+> Currently, the following regions provide the most overlap among the model providers and have the most capacity: **East US2** and **South Central** in the Americas; **France Central** or **Switzerland North** in Europe; **Australia East** in Asia Pacific.
 >
-> For Azure AI Vision and AI Search interoperability, choose one of these regions: **East US**, **France Central**, **Korea Central**, **North Europe**, **South East Asia**, or **West US**. 
+> For Azure AI Vision and AI Search interoperability, choose one of these regions: **France Central**, **Korea Central**, **North Europe**, **South East Asia**, or **West US**. 
 
 ## Review models supporting built-in vectorization
 
-Vectorized content improves the query results in a RAG solution. Azure AI Search supports an embedding action in an indexing pipeline. It also supports an embedding action at query time, converting text or image inputs into vectors for a vector search. In this step, identify an embedding model that works for your content and queries. If you're providing raw vector data and raw vector queries, or if your RAG solution doesn't include vector data, skip this step.
+Vectorized content improves the query results in a RAG solution. Azure AI Search supports a built-in vectorization action in an indexing pipeline. It also supports vectorization at query time, converting text or image inputs into embeddings for a vector search. In this step, identify an embedding model that works for your content and queries. If you're providing raw vector data and raw vector queries, or if your RAG solution doesn't include vector data, skip this step.
 
 Vector queries that include a text-to-vector conversion step must use the same embedding model that was used during indexing. The search engine won't throw an error if you use different models, but you'll get poor results.
 
-To meet the same-model requirement, choose embedding models that can be referenced through *skills* during indexing and through *vectorizers* during query execution. Review [Create an indexing pipeline](tutorial-rag-build-solution-pipeline.md) for code that calls an embedding skill and a matching vectorizer. 
+To meet the same-model requirement, choose embedding models that can be referenced through *skills* during indexing and through *vectorizers* during query execution. The following table lists the skill and vectorizer pairs. To see how the embedding models are used, skip ahead to [Create an indexing pipeline](tutorial-rag-build-solution-pipeline.md) for code that calls an embedding skill and a matching vectorizer. 
 
 Azure AI Search provides skill and vectorizer support for the following embedding models in the Azure cloud.
 
 | Client | Embedding models | Skill | Vectorizer |
 |--------|------------------|-------|------------|
-| Azure OpenAI | text-embedding-ada-002, text-embedding-3-large, text-embedding-3-small | [AzureOpenAIEmbedding](cognitive-search-skill-azure-openai-embedding.md) | [AzureOpenAIEmbedding](vector-search-vectorizer-azure-open-ai.md) |
+| Azure OpenAI | text-embedding-ada-002, <br>text-embedding-3-large, <br>text-embedding-3-small | [AzureOpenAIEmbedding](cognitive-search-skill-azure-openai-embedding.md) | [AzureOpenAIEmbedding](vector-search-vectorizer-azure-open-ai.md) |
 | Azure AI Vision | multimodal 4.0 <sup>1</sup> | [AzureAIVision](cognitive-search-skill-vision-vectorize.md) | [AzureAIVision](vector-search-vectorizer-ai-services-vision.md) |
-| Azure AI Studio model catalog | OpenAI-CLIP-Image-Text-Embeddings-vit-base-patch32, OpenAI-CLIP-Image-Text-Embeddings-ViT-Large-Patch14-336, Facebook-DinoV2-Image-Embeddings-ViT-Base, Facebook-DinoV2-Image-Embeddings-ViT-Giant, Cohere-embed-v3-english, Cohere-embed-v3-multilingual | [AML](cognitive-search-aml-skill.md) <sup>2</sup>  | [Azure AI Studio model catalog](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) |
+| Azure AI Studio model catalog | OpenAI-CLIP-Image-Text-Embeddings-vit-base-patch32, <br>OpenAI-CLIP-Image-Text-Embeddings-ViT-Large-Patch14-336, <br>Facebook-DinoV2-Image-Embeddings-ViT-Base, <br>Facebook-DinoV2-Image-Embeddings-ViT-Giant, <br>Cohere-embed-v3-english, <br>Cohere-embed-v3-multilingual | [AML](cognitive-search-aml-skill.md) <sup>2</sup>  | [Azure AI Studio model catalog](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) |
 
 <sup>1</sup> Supports image and text vectorization.
 
@@ -88,7 +88,7 @@ The following models are commonly used for a chat search experience:
 
 | Client | Chat models |
 |--------|------------|
-| Azure OpenAI | GPT-35-Turbo, GPT-4, GPT-4o, GPT-4 Turbo |
+| Azure OpenAI | GPT-35-Turbo, <br>GPT-4, <br>GPT-4o, <br>GPT-4 Turbo |
 
 GPT-35-Turbo and GPT-4 models are optimized to work with inputs formatted as a conversation. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルの更新と日時の修正"
}
```

### Explanation
この変更は、「RAGソリューションモデルを構築する」チュートリアルの内容が更新され、日付が修正されたことを示しています。具体的には、元の日付「09/12/2024」が「09/30/2024」に変更され、情報の鮮度が保たれています。

また、チュートリアルのいくつかの説明文が洗練され、明確さが増しています。例えば、「Azureのサブスクリプションに必要な役割」がより詳細に記述され、どのリソースを使用するかが明確になりました。また、モデル供給者の役割要件や権限割り当ての重要性についても言及されています。

さらに、テーブル形式での情報提供についても改善が見られ、埋め込みモデルや関連スキル、ベクトライザーの関係が視覚的に整理されているため、ユーザーが理解しやすくなっています。このチュートリアルは、Azureのリソースを使用したAIモデルのデプロイについて強調しており、ユーザーにとって有益な情報源となっています。


