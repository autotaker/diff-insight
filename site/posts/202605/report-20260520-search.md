---
date: '2026-05-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:cd7446e...MicrosoftDocs:da60fdf
summary: この更新では、ハイブリッド検索とエージェンティック検索に関するドキュメントの内容が更新され、情報が明確化されています。ハイブリッド検索では特定のパラメータの説明が強化され、エージェンティック検索には日付や詳細情報の更新が行われました。新機能は含まれていませんが、ドキュメントの詳細が追加され、ユーザーが検索クエリを最適化して期待通りの結果を得るための助けとなります。また、エージェンティック検索ではプレビュー版のREST
  APIのアクセスに関する具体的な情報も強調されています。これにより、ユーザーはリスクを理解し、技術的な判断を行いやすくなります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:cd7446e...MicrosoftDocs:da60fdf){target="_blank"}

# Highlights
この差分では、いくつかのドキュメントの内容が更新されています。それらは、ハイブリッド検索およびエージェンティック検索に関するもので、情報の明確化を目的としています。ハイブリッド検索では特定のパラメータの説明が強化され、エージェンティック検索に関しては発表および機能利用に関連する日付や詳細情報が更新されています。

## 新機能
- 特に新機能といえるものは今回の更新には含まれていませんが、情報の詳細が追加されています。

## 破壊的変更
- 破壊的変更はありません。

## その他のアップデート
- ハイブリッド検索のクエリで利用するパラメータについて、使用方法と影響の詳細な説明が追加されました。
- エージェンティック検索に関連する複数の文書で日付やプレビュー版機能の利用に関する情報が更新されました。

# Insights
この更新は、主にドキュメントの明確化と最新情報の提供を目的としています。特にハイブリッド検索のドキュメントでは、ユーザーが検索クエリを最適化し、期待通りの結果を得るために必要な情報がより細部まで説明されるようになりました。このように詳細が追加されることで、ユーザーは異なる検索クエリタイプによる影響を理解しやすくなり、結果としてより効果的に機能を利用できるようになります。

一方、エージェンティック検索に関連する更新は、プレビュー版のREST APIへのアクセスが可能であることや、一般利用開始に関する具体的な日付や情報が強調されています。これにより、ユーザーは新しい検索機能の利用や、プレビュー機能のリスクをより正確に理解することが可能です。特に製品環境での使用が推奨されない点が明確化されているため、開発者はリスクを踏まえた上で適切に機能を試用することができます。

このような文書の更新は、技術的な理解を深める上で重要であり、正確な情報に基づいた意思決定をサポートします。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [hybrid-search-how-to-query.md](#item-345ce6) | minor update | ハイブリッド検索のクエリに関する文書の更新 | modified | 13 | 3 | 16 | 
| [agentic-retrieval-ga-announcement.md](#item-4f2f62) | minor update | エージェンティック検索の一般利用開始に関する発表の更新 | modified | 3 | 1 | 4 | 
| [agentic-retrieval-ga-feature.md](#item-2de8dc) | minor update | エージェンティック検索機能の一般利用開始に関する更新 | modified | 3 | 1 | 4 | 
| [agentic-retrieval-preview-api-usage.md](#item-2442de) | minor update | エージェンティック検索プレビューAPI利用に関する内容の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/hybrid-search-how-to-query.md{#item-345ce6}

<details>
<summary>Diff</summary>
````diff
@@ -297,7 +297,17 @@ await foreach (SearchResult<SearchDocument> result in results.GetResultsAsync())
 
 A hybrid query can be tuned to control how much of each subquery contributes to the combined results. Setting `maxTextRecallSize` specifies how many BM25-ranked results are passed to the hybrid ranking model.
 
-If you use `maxTextRecallSize`, you might also want to set `CountAndFacetMode`. This parameter determines whether the `count` and `facets` should include all documents that matched the search query, or only those documents retrieved within the `maxTextRecallSize` window. The default value is "countAllResults".
+If your request includes facets, use nonvector fields that are marked as `facetable` in the index. Vector fields aren't facetable.
+
+Facet counts depend on the query type:
+
++ In a text-only query, facets count the documents that match the text query.
++ In a vector-only query, facets count the `k` documents returned by the vector query.
++ In a hybrid query, facets account for both vector and text results. The vector side contributes the `k` nearest documents. The text side contributes BM25-ranked documents. The `countAndFacetMode` parameter determines whether count and facet calculations use all text matches or only the text matches that are retrieved for ranking.
+
+If you use `maxTextRecallSize`, you might also want to set `countAndFacetMode`. This parameter determines whether `count` and `facets` include all documents that matched the text query, or only documents retrieved within the `maxTextRecallSize` window. The default value is `countAllResults`.
+
+With the default `countAllResults` mode, counts and facets can include text-side documents that aren't retrieved for RRF ranking because they fall outside the `maxTextRecallSize` window. Increasing `maxTextRecallSize` increases the number of BM25-ranked documents available for ranking, but doesn't increase the vector contribution beyond `k`. Use `countRetrievableResults` if you want count and facet calculations scoped to the documents retrieved for hybrid ranking.
 
 We recommend the [latest preview REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&preserve-view=true) for setting these options.
 
@@ -310,7 +320,7 @@ We recommend the [latest preview REST API](/rest/api/searchservice/documents/sea
 
    + `maxTextRecallSize` specifies the number of BM25-ranked results to provide to the Reciprocal Rank Fusion (RRF) ranker used in hybrid queries. The default is 1,000. The maximum is 10,000.
 
-   + `countAndFacetMode` reports the counts for the BM25-ranked results (and for facets if you're using them). The default is all documents that match the query. Optionally, you can scope "count" to the `maxTextRecallSize`.
+   + `countAndFacetMode` reports the count and facet scope for a hybrid query. The default, `countAllResults`, uses the full hybrid result set, including all documents that match the text query, even if some of those text matches aren't retrieved for RRF ranking because they fall outside the `maxTextRecallSize` window. Use `countRetrievableResults` to scope count and facets to the documents retrieved for ranking, including `maxTextRecallSize` BM25-ranked documents and the `k` vector matches.
 
 1. Set `maxTextRecallSize`:
 
@@ -320,7 +330,7 @@ We recommend the [latest preview REST API](/rest/api/searchservice/documents/sea
 
 The following REST examples show two use-cases for setting `maxTextRecallSize`. 
 
-The first example reduces `maxTextRecallSize` to 100, limiting the text side of the hybrid query to just 100 document. It also sets `countAndFacetMode` to include only those results from `maxTextRecallSize`.
+The first example reduces `maxTextRecallSize` to 100, limiting the text side of the hybrid query to just 100 documents. It also sets `countAndFacetMode` to include only retrievable documents in count and facet calculations.
 
 ```http
 POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?api-version=2025-11-01-preview 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索のクエリに関する文書の更新"
}
```

### Explanation
この変更は、「ハイブリッド検索の方法」についてのドキュメントに対するマイナーなアップデートであり、情報の明確化と詳細の追加が行われています。主に、ハイブリッドクエリにおける `maxTextRecallSize` および `countAndFacetMode` パラメータの使用に関する説明が強化され、ファセットカウントが異なるクエリタイプによってどのように影響を受けるかが詳述されています。具体的には、テキストのみ、ベクトルのみ、そしてハイブリッドクエリの場合におけるファセットのカウント方法の違いが説明されており、これによりドキュメントの利用者がこの機能をより理解しやすくなっています。さらに、`countAndFacetMode` パラメータがどのように機能するかに関する新しい情報が追加され、情報が更新されたことによってより正確なガイダンスが提供されています。

## articles/search/includes/previews/agentic-retrieval-ga-announcement.md{#item-4f2f62}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,10 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 04/16/2026
+ms.date: 05/19/2026
 ---
 
 > [!NOTE]
 > Some agentic retrieval features are generally available in the 2026-04-01 REST API version via programmatic access. The Azure portal and Microsoft Foundry portal continue to provide preview-only access to all agentic retrieval features. For migration guidance, including a breakdown of what's generally available and what remains in preview, see [Migrate agentic retrieval code to the latest version](../../agentic-retrieval-how-to-migrate.md).
+>
+> If you choose to use a preview REST API version, you can access agentic retrieval capabilities that aren't yet generally available. Preview features are provided without a service-level agreement and aren't recommended for production workloads. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティック検索の一般利用開始に関する発表の更新"
}
```

### Explanation
この変更は、エージェンティック検索に関する発表文書のマイナーな更新を反映しています。主な変更点は、ドキュメントの日付が2026年4月16日から2026年5月19日に更新されたことです。また、エージェンティック検索機能に関する新しい情報が追加され、プレビュー版のREST APIを使用する場合に、通常利用可能でない機能にアクセスできること、さらにプレビュー機能にはサービスレベル契約がないことが明記されています。そのため、この更新により利用者はプレビュー機能を使用する際のリスクをより理解できるようになります。これにより、ドキュメントの信頼性と最新性が向上しています。

## articles/search/includes/previews/agentic-retrieval-ga-feature.md{#item-2de8dc}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,10 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 04/16/2026
+ms.date: 05/19/2026
 ---
 
 > [!NOTE]
 > This agentic retrieval feature is generally available in the 2026-04-01 REST API version via programmatic access. The Azure portal and Microsoft Foundry portal continue to provide preview-only access to all agentic retrieval features. For migration guidance, see [Migrate agentic retrieval code to the latest version](../../agentic-retrieval-how-to-migrate.md).
+>
+> If you choose to use a preview REST API version, you can access capabilities that aren't yet generally available for this feature. Preview features are provided without a service-level agreement and aren't recommended for production workloads. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティック検索機能の一般利用開始に関する更新"
}
```

### Explanation
この変更は、エージェンティック検索機能に関する文書のマイナーな更新を示しており、主に情報の明確化がなされています。ドキュメントの日付が2026年4月16日から2026年5月19日に変更され、エージェンティック検索機能が2026年4月1日のREST APIバージョンで一般利用可能であることが強調されています。さらに、プレビュー版のREST APIを使用することで、まだ一般利用可能でない機能にもアクセスできることが追加情報として記載されており、これらのプレビュー機能がサービスレベル契約なしで提供されることと、製品環境での使用には推奨されない点も明確にされています。この更新により、利用者は新しい情報とリスクを理解しながら、エージェンティック検索機能の利用を検討できるようになります。

## articles/search/includes/previews/agentic-retrieval-preview-api-usage.md{#item-2442de}

<details>
<summary>Diff</summary>
````diff
@@ -9,4 +9,4 @@ ms.date: 04/16/2026
 ---
 
 > [!NOTE]
-> Some agentic retrieval features are generally available in the 2026-04-01 REST API version. However, this article uses the 2025-11-01-preview to demonstrate the full feature set, including features that remain in preview. Preview features are provided without a service-level agreement and aren't recommended for production workloads. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
\ No newline at end of file
+> Some agentic retrieval features are generally available in the 2026-04-01 REST API version. However, this article uses the latest preview REST API version to demonstrate the full feature set, including features that remain in preview. Preview features are provided without a service-level agreement and aren't recommended for production workloads. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティック検索プレビューAPI利用に関する内容の更新"
}
```

### Explanation
この変更は、エージェンティック検索プレビューAPIの利用に関する文書の内容をマイナーに更新しています。主なポイントは、プレビューAPIのバージョンが具体的に指定されていた部分が「2025-11-01-preview」から「最新のプレビューレストAPIバージョン」に変更されたことです。この変更により、読者は最新のプレビュー機能にアクセスできることを理解しやすくなります。また、エージェンティック検索の一般利用可能な機能は、2026年4月1日のREST APIバージョンで提供されることが引き続き明記されています。プレビューフィーチャーの利用に際しての注意事項や、製品環境での使用が推奨されないことについても変わりなく記載されており、利用者がリスクを理解しながらAPIを利用できるよう配慮されています。


