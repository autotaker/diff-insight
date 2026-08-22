---
date: '2026-08-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ff3e522...MicrosoftDocs:19bbfea
summary: この差分では、サーバーレス価格モデルに関する利用可能地域やコスト最適化の情報が更新され、ユーザーに最新かつ明確な情報を提供することを目的としています。具体的には、地域情報の拡張とコスト構造の詳細化が行われ、不必要な情報が削除されました。これにより、ユーザーはサービスの選択やコスト管理に自信を持つことができ、Azureのサーバーレスサービスをより効果的に活用できるようになります。また、ドキュメント全体の質が向上し、誤解を避けることで設定ミスやデータ損失のリスクも減少します。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ff3e522...MicrosoftDocs:19bbfea){target="_blank"}

<format>
# ハイライト
この差分では、サーバーレス価格モデルの利用可能地域やコスト最適化に関する情報の更新が含まれています。特定の文書において、地域情報の拡充やコスト要因の詳細化、不要な地域情報の削除が行われ、ユーザーには明確で最新の情報を提供することを目指しています。

## 新機能
- サーバーレス価格モデルの利用可能地域が大幅に拡張され、ユーザーにより多くの選択肢が提供されました。
- コスト構造に関する説明が詳細化され、ユーザーは価格モデルの理解を深められます。

## 破壊的変更
- 特定ファイルから不必要な地域情報が削除され、情報の簡素化が図られました。

## その他の更新
- ファイルの日付や説明文の明確化が行われ、ドキュメント全体の質が向上しています。

# インサイト
この差分は、クラウドサービスを利用するユーザーに正確な地域情報と明確な価格モデルを提供することを目指しています。情報の明確化により、ユーザーはサービスの選択やコスト管理に対するコンフィデンスを高めることができます。

特に、サーバーレスモデルの地域サポート情報の拡充は、多様な地域に展開する企業に対して価値があり、より柔軟な運用が可能となります。また、コスト最適化に関する詳細な情報は、費用対効果の高いサービス利用を促進します。

これにより、ユーザーはAzureのサーバーレスサービスを最大限に活用でき、適切な地域と価格モデルを選定しやすくなると言えます。さらに、ドキュメントの改善は、誤解を避けることにより、設定ミスやデータ損失のリスクを減らします。このようなアップデートは、ユーザーエクスペリエンスの向上につながり、Azureサービスの競争力を強化するでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [preview-serverless.md](#item-bbbf72) | minor update | プレビューの地域に関する情報の更新 | modified | 1 | 1 | 2 | 
| [search-capacity-planning.md](#item-0dd6c9) | minor update | サーバーレス価格モデルの利用可能地域に関する情報の更新 | modified | 1 | 1 | 2 | 
| [search-region-support.md](#item-25b0f1) | minor update | サーバーレス価格モデルのプレビュー地域情報の更新 | modified | 1 | 1 | 2 | 
| [search-sku-tier.md](#item-7686b8) | minor update | サーバーレス価格モデルのプレビュー地域に関する情報の削除 | modified | 0 | 6 | 6 | 
| [serverless-cost-optimization.md](#item-8dc21e) | minor update | サーバーレスモデルのコスト最適化に関する情報の更新 | modified | 5 | 3 | 8 | 
| [vector-search-how-to-storage-options.md](#item-ee1680) | minor update | ベクトル検索に関するストレージオプションの情報更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/includes/previews/preview-serverless.md{#item-bbbf72}

<details>
<summary>Diff</summary>
````diff
@@ -12,4 +12,4 @@ ms.date: 08/10/2026
 > The Serverless Developer tier is currently in preview. This preview is provided without a service-level agreement and isn't recommended for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).<br><br>
 > Billing for the Serverless Developer tier begins on September 13, 2026. Charges for usage on or after that date appear on your Azure bill. You aren't charged for usage before September 13, 2026. Serverless Developer is a paid tier once billing begins.
 > The Serverless Developer tier doesn't support migration to or from other pricing tiers and some features available on other tiers aren't supported during Public Preview. Service limits, supported features, and pricing details may change before general availability.<br><br>
-> The preview is currently only available in West Central US, Switzerland North, and Japan East.
\ No newline at end of file
+> During preview, the Serverless pricing model is supported only in [specific regions](../../search-region-support.md#features-subject-to-regional-availability).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビューの地域に関する情報の更新"
}
```

### Explanation
この変更は、`preview-serverless.md`ファイルにおける内容の更新を示しています。具体的には、サーバーレス開発者層のプレビューに関する文章が変更されました。元の文では、プレビューが「West Central US、Switzerland North、Japan East」でのみ利用可能であると述べられていましたが、新しい文では、プレビュー中のサーバーレス価格モデルが特定の地域でのみサポートされていることが言及され、地域に関する情報へのリンクが追加されました。この変更により、利用者にはサポートされる地域に関するより正確な情報が提供されることになります。

## articles/search/search-capacity-planning.md{#item-0dd6c9}

<details>
<summary>Diff</summary>
````diff
@@ -333,7 +333,7 @@ To learn more, see [Optimize costs with the Serverless pricing model in Azure AI
 Capacity and availability can vary by the [supported region](search-region-support.md). Some regions might have constraints on provisioning new services or scaling existing ones.
 
 > [!NOTE]
-> During public preview, the Serverless pricing model is available only in a limited set of regions. See the preview notice at the beginning of this article. 
+> During public preview, the Serverless pricing model is available only in [specific regions](./search-region-support.md#features-subject-to-regional-availability).
 
 If your preferred Azure AI Search region is unavailable due to capacity constraints, see [How to handle regional capacity constraints in Azure AI Search](search-region-capacity.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレス価格モデルの利用可能地域に関する情報の更新"
}
```

### Explanation
この変更は、`search-capacity-planning.md`ファイル内の内容を修正したものです。具体的には、サーバーレス価格モデルの利用可能地域についての記述が更新されました。以前は、「公開プレビュー中はサーバーレス価格モデルが限られた地域でしか利用できない」と記載されていましたが、新しい文では、利用可能地域が「特定の地域」であることが明記され、地域に関する情報へのリンクも追加されました。この変更により、読者はサポートされている地域についてのより明確な情報を得ることができます。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ When you create an Azure AI Search service, your region selection might depend o
 | [Confidential computing](search-security-best-practices.md#optional-enable-confidential-computing) | Deploys your search service on confidential VMs to process data in a hardware-based trusted execution environment.<p>Confidential computing disables or restricts certain features, including agentic retrieval, semantic ranker, query rewrite, and skillset execution. | Regional support is noted in this article. |
 | [Semantic ranker](semantic-search-overview.md) | Takes a dependency on Microsoft-hosted models in specific regions. | Regional support is noted in this article. |
 | [Query rewrite](semantic-how-to-query-rewrite.md) | Takes a dependency on Microsoft-hosted models in specific regions. | Regional support is noted in this article. |
-| [Serverless pricing model](serverless-cost-optimization.md) | Enables pay-per-request billing for search workloads. | Preview in West Central US, Switzerland North, and Japan East. |
+| [Serverless pricing model](serverless-cost-optimization.md) | Enables pay-per-request billing for search workloads. | Preview in Australia East, Central India, Central US, Japan East, North Central US, Sweden Central, Switzerland North, UK South, West Central US, West US, and West US 2. |
 | [Extra capacity](search-limits-quotas-capacity.md#service-limits) | Higher-capacity partitions became available in select regions starting in April 2024, with a second wave following in May 2024. Currently, there are just a few regions that *don't* offer higher-capacity partitions.<p>If you have an older search service in a supported region, check if you can [upgrade your service](search-how-to-upgrade.md). Otherwise, create a new search service to benefit from more capacity at the same billing rate. | Regional support is noted in the footnotes of this article. |
 | Capacity constraints | In some regions, insufficient capacity prevents you from creating search services on certain tiers. The Azure portal automatically hides regions and tiers that aren't available for new deployments. | Regional support is noted in the footnotes of this article. |
 | [Azure Vision in Foundry Tools 4.0 multimodal APIs](search-get-started-portal-image-search.md) | Refers to the Azure Vision multimodal embeddings skill and vectorizer that call the multimodal embedding API. | Check the [Azure Vision region list](/azure/ai-services/computer-vision/overview-image-analysis#region-availability) first, and then verify Azure AI Search is available in the same region.|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレス価格モデルのプレビュー地域情報の更新"
}
```

### Explanation
この変更は、`search-region-support.md`ファイルに対する修正を示しています。サーバーレス価格モデルのプレビューに関する情報が更新され、以前は「West Central US、Switzerland North、Japan East」と限定されていた地域が、新しい記述では「Australia East、Central India、Central US、Japan East、North Central US、Sweden Central、Switzerland North、UK South、West Central US、West US、West US 2」の合計11の地域に拡大されました。この修正により、ユーザーはサーバーレス価格モデルが利用可能な地域の最新情報を把握でき、サービスを利用する際の選択肢が広がります。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -53,12 +53,6 @@ The Serverless Developer tier is in Public Preview and doesn't currently support
 - Shared Private Link resources: No planned support for the Serverless model
 - Service-level agreement (SLA): Not available during Public Preview
 
-Available regions for the Serverless pricing model during preview include:
-
-- West Central US
-- Switzerland North
-- Japan East
-
 To learn more, see [Service Limits in Azure AI Search](./search-limits-quotas-capacity.md).
 
 For additional large-scale Serverless deployment options, contact Microsoft using the [Azure AI Search Serverless Private Preview Sign-up Form](https://aka.ms/FoundryIQ-serverless-contact).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレス価格モデルのプレビュー地域に関する情報の削除"
}
```

### Explanation
この変更は、`search-sku-tier.md`ファイルの内容を修正したものです。サーバーレス価格モデルに関する情報の一部が削除されています。具体的には、プレビュー中に利用可能な地域として「West Central US」「Switzerland North」「Japan East」という3つの地域の説明が削除されました。この更新により、サーバーレス価格モデルの利用可能地域に関する具体的な情報がなくなり、関連する注意書きが簡素化されました。この変更は、情報の明確化や最新情報の反映を目的としていると考えられます。

## articles/search/serverless-cost-optimization.md{#item-8dc21e}

<details>
<summary>Diff</summary>
````diff
@@ -26,14 +26,16 @@ For more information about pricing model and service tier differences, see [Choo
 
 ## How cost is determined in the Serverless model
 
-In the Serverless model, **performance optimization directly affects cost**. Cost is directly tied to workload execution:
+The Dedicated and Serverless pricing models account for work inside the search service differently. Dedicated services run queries, indexing, and result processing on provisioned capacity that you already purchased. Serverless services measure the compute, memory, and disk I/O that these operations consume and convert that usage into Compute Units (CUs). As a result, **performance optimization directly affects Serverless cost**.
+
+Serverless costs are tied to workload execution:
 
 - Queries and indexing consume compute, measured in Compute Units per hour (CU/h).
 - Active indexes consume compute based on their resource usage and how long they remain active.
 - An index stays active for 10 minutes after its last query or indexing request before it goes inactive.
 - Inactive indexes have no minimum or reserved compute charge. The compute usage for inactive indexes scales to zero. There's no minimum compute charge when an index is inactive.
 - Storage is billed separately based on index size on disk and continues whether or not an index is in use.
-- Agentic retrieval consumes compute for each query executed against knowledge sources backed by Azure AI Search indexes, plus a separate orchestration charge for generating those queries and merging the results into a single response.
+- Agentic retrieval consumes compute for search queries and orchestration performed inside the search service.
 
 Storage charges stop only when you delete the index.
 
@@ -51,7 +53,7 @@ To reduce active-index compute usage, identify which resource produces the highe
 The Serverless pricing model is most cost-effective for workloads with variable, intermittent, or unpredictable traffic, where provisioned capacity would be underutilized.
 
 > [!IMPORTANT]
-> Your Compute Unit per hour (CU/h) charges don't include semantic ranker, agentic retrieval, image extraction and skill execution. These capabilities are billed separately.
+> Serverless CU charges cover work performed inside the search service, including queries, indexing, result processing, and agentic retrieval orchestration. Model calls and other work performed outside the search service continue to use their existing billing meters. Examples include semantic ranking, agentic query rewriting, image extraction, and skill execution.
 
 ## Understand Compute Units (CUs)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスモデルのコスト最適化に関する情報の更新"
}
```

### Explanation
この変更は、`serverless-cost-optimization.md`ファイルに対する修正を示しています。サーバーレス価格モデルにおけるコストの決定要因についての説明が詳細に更新されました。具体的には、サーバーレスと専用価格モデルの違いが明確にされ、サーバーレスモデルでは「コンピューティングユニット（CU）」を使用して計測される計算、メモリ、およびディスクI/Oの使用に基づいてコストが算出されることが強調されています。

さらに、エージェントリトリーバルのコスト処理に関する記述が変更され、サーバーレスサービス内でのクエリとオーケストレーションに関連するコンピューティングの消費に特化した表現に見直されました。また、サーバーレスのCU料金に関する重要な情報も更新され、検索サービス内の業務に関連するコストに言及しています。これにより、ユーザーはサーバーレスモデルのコスト構造についてより明確な理解を得ることができます。

## articles/search/vector-search-how-to-storage-options.md{#item-ee1680}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 04/27/2026
+ms.date: 08/21/2026
 ai-usage: ai-assisted
 ---
 
@@ -45,7 +45,7 @@ Considerations for setting `"stored": false`:
 
 - Because vectors aren't human readable, you can generally omit them from results sent to LLMs in RAG scenarios or from results rendered on a search page. However, you should keep them if you're using vectors in a downstream process that consumes vector content.
 
-- If your indexing strategy uses [partial document updates](search-howto-reindex.md#update-content), such as `merge` or `mergeOrUpload` on an existing document, setting `"stored": false` prevents content updates to those fields during the merge. You must include the entire vector field (and nonvector fields you're updating) in each reindexing operation. Otherwise, the vector data is lost without an error or warning. To avoid this risk altogether, set `"stored": true`.
+- If your indexing strategy uses [partial document updates](search-howto-reindex.md#update-content), such as `merge` or `mergeOrUpload` on an existing document, setting `"stored": false` prevents Azure AI Search from preserving the existing vector when the vector field is omitted from the update request. You must include the entire vector field (and nonvector fields you're updating) in each reindexing operation. Otherwise, the vector data is lost without an error or warning. To avoid this risk altogether, set `"stored": true`.
 
 > [!IMPORTANT]
 > Setting the `"stored": false` attribution is irreversible. This property can only be set when you create the index and is only allowed on vector fields. Updating an existing index with new vector fields can't set this property to `false`. If you want retrievable vector content later, you must drop and rebuild the index or create and load a new field that has the new attribution.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索に関するストレージオプションの情報更新"
}
```

### Explanation
この変更は、`vector-search-how-to-storage-options.md`ファイルの更新を示しており、主に日付の更新と説明文の明確化が行われています。具体的には、文書の日付が2026年4月27日から2026年8月21日に変更されました。

また、ベクトルを更新のリクエストから除外する設定に関する注意点がより明確に説明されています。「stored」属性が`false`に設定されている場合、Azure AI Searchがベクトルフィールドを更新リクエストから除外すると、既存のベクトルが保持されないことが強調されています。この変更により、ユーザーは更新操作におけるベクトルデータの扱いについてより理解を深め、誤った設定によるデータ損失を回避できるようになっています。


