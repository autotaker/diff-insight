---
date: '2026-04-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a8bf7fb...MicrosoftDocs:1d705b3
summary: このコードの変更は、複数のMarkdownファイルに対するマイナーな修正を行い、ドキュメンテーションの整合性と明確さを高めることを目的としています。各ファイルの情報が更新され、ユーザーが理解しやすくなるよう改善が施されています。大きな破壊的変更はありませんが、一部情報が削除され、情報構成が変更されています。また、文末にピリオドを追加し、非推奨情報に関する記述を明確にするなど文書全体の整合性が向上しました。これにより、ユーザーはAzureの機能をより効率的に利用できるようになり、信頼性の高いガイドラインが提供されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a8bf7fb...MicrosoftDocs:1d705b3){target="_blank"}

# Highlights
このコードの変更は、複数のMarkdownファイルに対するマイナーな修正を行い、ドキュメンテーションの整合性と明確さを高めることを目的としています。特に、日付や文言の更新、不要な情報の削除などが行われています。

## New features
- 各ファイルの内容を更新し、ユーザーがより理解しやすいように情報の明確さを改善しました。

## Breaking changes
- 特に大きな破壊的変更は含まれていませんが、一部の情報が削除され、情報構成が異なる形式になっています。

## Other updates
- 文書の整合性を向上させるため、いくつかの文末にピリオドを追加し、表現を統一しました。
- 非推奨情報に関する記述をより明確にし、ユーザーの理解をサポートするために修正しました。

# Insights
この一連の変更は、技術文書における情報の正確性と明瞭さを高めるために行われています。例えば、「エージェント知識ソースに関する検索インデックスの更新ガイド」では、冗長な情報を除去して必要な情報だけを残し、ガイドラインを簡潔に整理する努力が見られます。また、「検索APIバージョン」では、非推奨となったバージョンの情報について、ユーザーがそれに対するサポートが終了したことをより明確に認識できるように修正されています。これらのアップデートは、ユーザーがAzureの機能を効率よく利用できるよう、情報の透明性を高めることに寄与しています。

文法的な微調整と日付の更新が複数のドキュメントで行われており、これにより一貫性のある記述スタイルが保証され、読みやすさが向上しています。また、注意深い内容の調整によって、ユーザーはより正確な情報を基に判断を行うことが可能となります。最終的にこれらの改善は、Azureサービスを利用するユーザーに対して、信頼性の高いガイドラインを提供し続けることを目的としていると言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-search-index-rest.md](#item-e95367) | minor update | エージェント知識ソースに関する検索インデックスの更新ガイド | modified | 1 | 4 | 5 | 
| [search-api-versions.md](#item-69ca3e) | minor update | 検索APIバージョンの非推奨情報の修正 | modified | 1 | 1 | 2 | 
| [search-capacity-planning.md](#item-0dd6c9) | minor update | 検索容量計画に関するドキュメントの修正 | modified | 3 | 3 | 6 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | プライベートリソースへのアクセスに関するドキュメントの更新 | modified | 5 | 5 | 10 | 


# Modified Contents
## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-rest.md{#item-e95367}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 03/25/2026
+ms.date: 04/10/2026
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -66,9 +66,6 @@ Content-Type: application/json
         "sourceDataFields": [
           { "name": "description" },
           { "name": "category" }
-        ],
-        "searchFields": [
-          { "name": "*" }
         ]
     }
 }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースに関する検索インデックスの更新ガイド"
}
```

### Explanation
このコードの変更は、「エージェント知識ソースに関する検索インデックスの更新ガイド」に関連するMarkdownファイルの修正を示しています。具体的には、日付が「2026年3月25日」から「2026年4月10日」に更新されています。また、JSONオブジェクト内に存在した「searchFields」フィールドの情報が削除され、「sourceDataFields」フィールドのみが残っています。これにより、提供されるデータフィールド情報が明確になり、不要な情報が排除されることで、ガイドラインがより簡潔に整理されています。この変更は、文書の整合性と最新性を保持するための重要な措置です。

## articles/search/search-api-versions.md{#item-69ca3e}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ For more information about the deprecation path, see the [Azure SDK lifecycle an
 
 ## Deprecated versions
 
-**2023-07-01-preview** was deprecated on April 8, 2024 and won't be supported after July 8, 2024.
+**2023-07-01-preview** was deprecated on April 8, 2024 and is no longer supported as of July 8, 2024.
 
 This was the first REST API that offered vector search support. Newer API versions have a different vector configuration. You should [migrate to a newer version](search-api-migration.md) as soon as possible.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索APIバージョンの非推奨情報の修正"
}
```

### Explanation
この変更は、「検索APIバージョン」に関するMarkdownファイルの修正を示しています。具体的には、**2023-07-01-preview**バージョンの非推奨に関する文言が更新され、「サポートが終了」という表現が「もはやサポートされていない」という表現に変更されました。この修正により、非推奨のフォーマットがより明確になり、ユーザーはサポート期間が終了したことをより具体的に理解できるようになります。このような更新は、ユーザーに対する重要な情報を正確に伝えるために不可欠です。

## articles/search/search-capacity-planning.md{#item-0dd6c9}

<details>
<summary>Diff</summary>
````diff
@@ -103,7 +103,7 @@ To increase or decrease the capacity of your service, you have two options:
 
    This operation can take several hours to complete. It occurs in the background, so your search service remains fully operational and available for read and write operations.
 
-   You can't cancel the operation or monitor its progress. However, the following message displays while changes are underway:
+   You can't cancel the operation or monitor its progress. However, the following message displays while changes are underway.
 
    :::image type="content" source="media/search-capacity-planning/updating-message.png" alt-text="Screenshot of the Updating message in the Azure portal." border="true" lightbox="media/search-capacity-planning/updating-message.png":::
 
@@ -112,7 +112,7 @@ To increase or decrease the capacity of your service, you have two options:
 > [!NOTE]
 > The Azure portal and [Services - Update (REST API)](/rest/api/searchmanagement/services/update) support changes between Basic and Standard (S1, S2, and S3) tiers. You can upgrade or downgrade tiers, provided your current service configuration doesn't exceed the [limits of the target tier](search-limits-quotas-capacity.md). Your region also can't have [capacity constraints on the target tier](search-region-support.md).
 
-Your [pricing tier](search-sku-tier.md) determines the maximum storage of your search service. If you need more or less capacity, you can switch to a different pricing tier that accommodates your storage needs.
+Your pricing tier determines the maximum storage of your search service. If you need more or less capacity, you can switch to a different pricing tier that accommodates your storage needs.
 
 In addition to capacity, pricing tiers determine limits on indexes, indexers, and other search objects. Compare the [service limits](search-limits-quotas-capacity.md) of your current tier and your desired tier before you proceed. Generally, switching to a higher tier increases your [storage limit](search-limits-quotas-capacity.md#service-limits) and [vector limit](search-limits-quotas-capacity.md#vector-index-size-limits), increases request throughput, and decreases latency, while switching to a lower tier has the opposite effect.
 
@@ -140,7 +140,7 @@ To change your pricing tier:
 
    This operation can take several hours to complete. It occurs in the background, so your search service remains fully operational and available for read and write operations.
 
-   You can't cancel the operation or monitor its progress. However, the following message displays while changes are underway:
+   You can't cancel the operation or monitor its progress. However, the following message displays while changes are underway.
 
    :::image type="content" source="media/search-capacity-planning/updating-message.png" alt-text="Screenshot of the Updating message in the Azure portal." border="true" lightbox="media/search-capacity-planning/updating-message.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索容量計画に関するドキュメントの修正"
}
```

### Explanation
この変更は、「検索容量計画」に関するMarkdownファイルの修正を示しています。主に、いくつかの文の末尾にピリオドを追加することにより、記述の整合性が向上しました。このような修正は、文書スタイルを一貫させ、読みやすさを向上させるために重要です。また、いくつかの内容において正確な情報の伝達を意識した微調整が行われており、ユーザーが容量変更に関する情報を明確に理解できるようになっています。これにより、ユーザーは操作の進行状況をモニタリングできないことや、メッセージ表示の内容についての理解を深めることができます。全体として、この更新はドキュメントの信頼性を高める重要な改良です。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Configure indexer connections to access content from other Azure re
 ms.reviewer: mcarter
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/17/2026
+ms.date: 04/10/2026
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
@@ -24,7 +24,7 @@ Shared private link is a premium feature billed by usage. For details, see [Azur
 
 ## Prerequisites
 
-+ [A supported Azure resource](#supported-resource-types), configured to run in a virtual network.
++ A [supported Azure resource](#supported-resource-types) configured to run in a virtual network.
 
 + An Azure AI Search service. Requirements vary by workload:
 
@@ -308,7 +308,7 @@ This would return a JSON, where the connection state shows up as "status" under
 }
 ```
 
-If the provisioning state (`properties.provisioningState`) of the resource is "Succeeded" and connection state(`properties.status`) is "Approved", it means that the shared private link resource is functional and the indexer can be configured to communicate over the private endpoint.
+If the provisioning state (`properties.provisioningState`) of the resource is "Succeeded" and connection state (`properties.status`) is "Approved", it means that the shared private link resource is functional and the indexer can be configured to communicate over the private endpoint.
 
 ## 4 - Configure the indexer to run in the private environment
 
@@ -423,9 +423,9 @@ When evaluating shared private links for your scenario, remember these constrain
 
 + Indexer execution must use the [private execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment) that's specific to your search service. Private endpoint connections aren't supported from the multitenant content processing environment. The configuration setting for this requirement is covered in this article.
 
-+ Review shared private link [resource limits for each tier](search-limits-quotas-capacity.md#shared-private-link-resource-limits).
++ Shared private link [resource limits](search-limits-quotas-capacity.md#shared-private-link-resource-limits) vary by pricing tier.
 
-+ The resource type `Microsoft.CognitiveServices/accounts` for kind `AIServices` isn't currently supported. This means that shared private link for Foundry resources with this kind can't be created at this time. If you require to use an Azure OpenAI embedding model for your skill or vectorizer, and need private communication, create an Azure OpenAI resource and a shared private link with the `Microsoft.CognitiveServices/accounts` with subtype `openai_account` as a workaround.
++ When you [change your pricing tier](search-capacity-planning.md#change-your-pricing-tier), shared private link resources are evaluated against the target tier's limits. If your shared private link count exceeds the target tier's maximum, the tier change is blocked. If the tier change succeeds, existing shared private link resources aren't recreated and don't require reapproval. Private indexer connectivity continues to work after the search service returns to a "Succeeded" provisioning state and "Running" status, provided the shared private link provisioning state remains "Succeeded" and the connection status remains "Approved."
 
 ## Troubleshooting
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートリソースへのアクセスに関するドキュメントの更新"
}
```

### Explanation
この変更は、「プライベートリソースにアクセスする方法」に関するMarkdownファイルの修正を示しています。主な修正点は、日付の更新や文言の微調整を含んでおり、特にリソースの接続状態やプライベートリンクの説明に重点が置かれています。具体的には、記述の表現を一貫させたり、一部の文に関しては文法的な正確さを向上させたりするための修正が行われています。これにより、プライベートリンクに関する機能や制約、価格帯ごとのリソースの制限について、ユーザーがより理解しやすくなっています。全体として、この更新は情報の正確性と明快さを高め、ユーザーがAzureのリソースを効果的に活用できるようにするためのものです。


