---
date: '2026-09-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:83c7cb1...MicrosoftDocs:7e20d69
summary: この報告書では、Azureのサーバーレスドキュメントに関する重要な更新が紹介されています。新たにサーバーレスのスケールコストに関連する画像が追加され、視覚的にコスト管理の理解を促進します。また、サーバーレス開発者層の請求開始日が2026年8月10日から9月13日に延期され、ユーザーにとっての請求開始日時の理解が向上します。加えて、「serverless-cost-optimization.md」にコスト最適化に関する情報が追加され、Azureポータルの機能を利用したリソース管理とコスト削減の方法が強調されています。これらの変更により、ユーザーエクスペリエンスが向上し、技術的内容への理解が深まることを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:83c7cb1...MicrosoftDocs:7e20d69){target="_blank"}

<format>
# Highlights

## New features
- サーバーレスのスケールコストに関連する新しい画像（`serverless-scale-cost-in-portal.png`）が追加され、視覚的な理解を助ける。

## Breaking changes
- 特に破壊的な変更は記載されていません。

## Other updates
- サーバーレス開発者層の請求開始日が「2026年8月10日」から「2026年9月13日」へと更新。
- 「serverless-cost-optimization.md」にコスト最適化に関する追加情報と案内が追加され、特にAzureポータルの「スケール + コスト」タブの利便性を強調。

# Insights

今回の変更は、Azureのサーバーレスドキュメントをより正確で使いやすいものにするために、小規模ながら重要な更新が行われています。まず、サーバーレス開発者層の請求開始日が1ヶ月程度後に延期されており、この変更は顧客に対して請求開始日時の正確な理解を促すことを目的としています。これにより、利用者は保有リソースに対する今後の課金の計画を組みやすくなります。

また、新たに追加されたサーバーレススケールコストのポータル画像は、Azureポータルにおけるコスト管理の視覚的指導を目的としています。この画像の追加により、ユーザーは、Azureのさまざまなコストやスケーリングに関する設定を直感的に理解できるようになります。

最後に、コスト最適化に関する情報の更新は、Azureのサーバーレス環境における効率的なリソース管理と費用対効果の高い運用を支援するものです。ここでは、Azureポータルの機能を駆使してコスト構造を詳しく確認したり、ハイブリッド検索の最適化設定について案内が強化されました。これにより開発者は、より良いプラクティスを実行することでコストの無駄を最小化することができます。

これらの変更は全体として、Azureドキュメントの質を向上させ、ユーザーエクスペリエンスを高めることに貢献しています。特にビジュアルコンテンツの追加は、技術的な内容を理解する上での障壁を低くする役割を果たします。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [preview-serverless.md](#item-bbbf72) | minor update | サーバーレス開発者層の請求開始日を更新 | modified | 3 | 3 | 6 | 
| [serverless-scale-cost-in-portal.png](#item-4553ad) | new feature | サーバーレススケールコストのポータル画像を追加 | added | 0 | 0 | 0 | 
| [serverless-cost-optimization.md](#item-8dc21e) | minor update | コスト最適化に関する情報の更新 | modified | 12 | 3 | 15 | 


# Modified Contents
## articles/search/includes/previews/preview-serverless.md{#item-bbbf72}

<details>
<summary>Diff</summary>
````diff
@@ -5,11 +5,11 @@ ms.topic: include
 ms.service: azure-ai-search
 author: mattwojo
 ms.author: mattwoj
-ms.date: 08/10/2026
+ms.date: 09/13/2026
 ---
 
 > [!IMPORTANT]
 > The Serverless Developer tier is currently in preview. This preview is provided without a service-level agreement and isn't recommended for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).<br><br>
-> Billing for the Serverless Developer tier begins on September 13, 2026. Charges for usage on or after that date appear on your Azure bill. You aren't charged for usage before September 13, 2026. Serverless Developer is a paid tier once billing begins.
+> Billing for the Serverless Developer tier began on September 13, 2026. Charges for usage on or after that date appear on your Azure invoice. You aren't charged for usage before September 13, 2026.
 > The Serverless Developer tier doesn't support migration to or from other pricing tiers and some features available on other tiers aren't supported during Public Preview. Service limits, supported features, and pricing details may change before general availability.<br><br>
-> During preview, the Serverless pricing model is supported only in [specific regions](../../search-region-support.md#features-subject-to-regional-availability).
\ No newline at end of file
+> During preview, the Serverless pricing model is supported only in [specific regions](../../search-region-support.md#features-subject-to-regional-availability).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレス開発者層の請求開始日を更新"
}
```

### Explanation
この変更は、`preview-serverless.md`ファイルに対するマイナーな更新を反映しています。特に、サーバーレス開発者層の請求開始日が更新されました。以前は「2026年8月10日」と記載されていましたが、現在は「2026年9月13日」に変更されています。この修正に加えて、請求に関連する情報の一部が改訂されており、Azureの請求書に表示される方法が明確にされています。全体として、この変更は文書の正確性を高め、ユーザーが未来の料金発生のタイミングを正しく理解できるようにすることを目的としています。

## articles/search/media/serverless/serverless-scale-cost-in-portal.png{#item-4553ad}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "サーバーレススケールコストのポータル画像を追加"
}
```

### Explanation
この変更は、`serverless-scale-cost-in-portal.png`という画像ファイルが新たに追加されたことを示しています。この画像は、サーバーレス環境におけるスケーリングとコストに関連する概念を視覚的に表現しており、ユーザーがAzureポータル内での操作や情報を理解するのに役立つことを目的としています。画像の追加は、ドキュメントの内容を強化し、ユーザーエクスペリエンスを向上させるための重要な要素となります。

## articles/search/serverless-cost-optimization.md{#item-8dc21e}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: mattwojo
 ms.author: mattwoj
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 06/02/2026
+ms.date: 09/09/2026
 ai-usage: ai-assisted
 # customer intent: As a developer or product engineer, I want to understand the details behind how the Azure AI Search Serverless pricing model works so that I can optimize my search service to use the most efficient pricing model suited to my needs and only pay for what I use.
 ---
@@ -39,6 +39,10 @@ Serverless costs are tied to workload execution:
 
 Storage charges stop only when you delete the index.
 
+To view the cost breakdown and usage rates for your current billing cycle, view the **Scale + Cost** tab in your [Azure portal](https://portal.azure.com/).
+
+:::image type="content" source="media/serverless/serverless-scale-cost-in-portal.png" alt-text="Screenshot of the Scale + Cost tab in the Azure Portal showing the time range for the current billing cycle, cost breakdown, usage details for Compute Units and Storage usage and rates." lightbox="media/serverless/serverless-scale-cost-in-portal.png":::
+
 ### How index size affects compute usage
 
 While an index is active, Azure AI Search evaluates two finite resources to determine its compute usage:
@@ -210,7 +214,7 @@ Query design is a primary driver of variable cost:
 
 - **Use lookups instead of searches when possible**: Retrieving a document by ID is more efficient than running a search query. If you know the document ID, use a lookup instead of a search query. Lookups are more efficient because they retrieve a document directly by key, while search queries invoke the full query pipeline (parsing, index traversal, scoring, and ranking), which increases compute cost.
 
-- **Avoid deep paging (`$skip`)**: Large `$skip` values increase compute because the engine must process and rank all preceding results (for example, `$skip=5000` requires scoring at least 5,000 documents that aren’t returned). This wastes compute (CUs) and increases cost. Instead, use filters to narrow results and limit the number returned with `$top`. Right-size `$top` to match your UI display. For example, `$top=10` costs less than `$top=50` because fewer results are scored and returned. Only request as many results as your application needs, and avoid patterns that require the engine to process large numbers of unused results.
+- **Avoid deep paging (`$skip`)**: Large `$skip` values increase compute because the engine must process, score, and rank the results that precede the requested page. For example, `$skip=5000` requires the engine to process at least 5,000 results that aren't returned. This choice consumes extra compute units (CUs) and can increase cost. Instead, use filters to narrow the result `set` and `$top` to limit the number of results returned. Right-size `$top` for your application or UI. Although `$top` doesn't change how many matching documents are scored, a smaller value reduces the number of results that must be collected, sorted, and serialized. Request only as many results as your application needs, and avoid paging patterns that require the engine to process large numbers of unused results.
 
 - **Minimize facet count and facet scope**: Request only the facets that are displayed in your UI, and keep each facet `count` value as low as practical. Facets require per-query aggregations, and high counts increase compute cost.
 
@@ -242,7 +246,12 @@ Vector queries are compute-intensive because they require similarity calculation
 
 - **Use hybrid search selectively**: Hybrid queries run both keyword and vector retrieval. Use only when necessary for relevance.
 
-- **Tune `maxTextRecallSize` for hybrid queries**: Set `hybridSearch.maxTextRecallSize` to control how many BM25-ranked text results are available to Reciprocal Rank Fusion (RRF). The default is 1,000, and the supported range is 1 through 10,000. Lowering the value can reduce text retrieval and result-fusion work, which can reduce resource utilization and latency. However, it can exclude relevant keyword results, including exact terms, IDs, and acronyms that vector search might miss. Test representative queries, and compare relevance, latency, and the `x-ms-azs-compute-units-consumed` response header before selecting a value. Control vector candidates separately by setting `k` on each vector query.
+- **Lower maxTextRecallSize for hybrid queries**: The `hybridSearch.maxTextRecallSize` setting controls how many BM25-ranked results feed into Reciprocal Rank Fusion. The default is 1,000 (range 1 through 10,000). Compute consumption scales roughly linearly with this value, so lowering it is one of the most direct cost levers for hybrid workloads.
+
+- Values around 500 often cut compute meaningfully with little relevance loss.
+- Going lower can drop keyword matches that vector search misses, such as exact terms, IDs, and acronyms.
+- Control vector candidates separately with k on each vector query.
+- Test representative queries and compare relevance, latency, and the `x-ms-azs-compute-units-consumed` header before settling on a value.
 
 - **Apply filters before vector queries**: Narrow the candidate set before vector search to reduce the amount of data processed. See [How filtering works in vector queries](./vector-search-filters.md#how-filtering-works-in-vector-queries).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コスト最適化に関する情報の更新"
}
```

### Explanation
この変更は、`serverless-cost-optimization.md`ファイルに対して行われたマイナーな更新を示しています。主な改訂内容には、文の修正や新しい情報の追加が含まれています。特に、請求サイクルにおけるコストの内訳と使用率を確認するためのAzureポータルの「スケール + コスト」タブについての案内が追加されました。また、ハイブリッド検索におけるコンピュートリソースに関する推奨設定についても具体的なアドバイスが強化されています。これにより、開発者や製品エンジニアがAzureのサーバーレス価格モデルを効果的に最適化できるようになることが期待されます。


