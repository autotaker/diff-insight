---
date: '2025-04-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b48656b...MicrosoftDocs:a4ad9b8
summary: |-
  今回の更新では、以下の主要な変更が行われました。日付の更新として「m.date」が2025年3月16日から2025年4月2日に変更され、用語の修正として「Azure AI multi-resource」が「Azure AI multi-service resource」に修正されました。また、プライベートエンドポイントに関する情報が追加されました。新しいガイドラインが追加され、プライベートエンドポイント使用時の接続要件が明確化されています。

  特定の用語が更新されましたが、これにより機能やAPIの動作には影響がなく、破壊的変更は含まれていません。一般的な用語や日付の更新が行われ、全体的に記事の内容がより最新のものとなっています。

  この更新は、記事の正確性とわかりやすさを向上させることを目的としたマイナーアップデートであり、特に新しいユーザーにとって理解しやすい資料になることが期待されています。プライベートエンドポイントに関連する情報の追加は、セキュリティと接続性の観点から重要なポイントとなっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b48656b...MicrosoftDocs:a4ad9b8){target="_blank"}

# Highlights
- 日付の更新: 「m.date」を2025年3月16日から2025年4月2日に変更
- 用語の修正: 「Azure AI multi-resource」が「Azure AI multi-service resource」に変更
- プライベートエンドポイントに関する情報の追加

## New features
- プライベートエンドポイントを使用する際の新しいガイドラインが追加され、接続要件が明確化されました。

## Breaking changes
- 特定の用語が更新されましたが、これは機能やAPIの動作には影響しないため、破壊的変更は含まれていません。

## Other updates
- 一般的な用語と日付の更新により、記事の内容全体がより最新のものになっています。

# Insights
今回の更新は、記事の正確性とわかりやすさを向上させることを目的としたマイナーアップデートです。特に、日付の修正と用語の変更により、ドキュメント全体の信頼性が高まっています。例えば、「Azure AI multi-resource」という表現を「Azure AI multi-service resource」としたことで、より具体的で一貫性のある内容になっています。これにより、読者はAzure AIの複数のサービスリソースを扱う際に混乱を減らせます。

また、プライベートエンドポイントを使用する際の情報が追加されたことで、セキュリティと接続の観点から非常に重要なポイントが強調されています。これは、Azure AIサービスを利用するシナリオにおいて、よりセキュアで信頼性の高いアプローチを提供することに寄与します。

これらの変更により、ユーザーがAzure AIのリソースを適切に扱うためのガイドラインが一層充実し、特に新しいユーザーにとって理解しやすくなっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | コグニティブ サービスへの接続に関する日付の更新と説明の改訂 | modified | 3 | 2 | 5 | 


# Modified Contents
## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: how-to
-ms.date: 3/16/2025
+ms.date: 04/02/2025
 ---
 
 # Attach an Azure AI services resource to a skillset in Azure AI Search
@@ -27,14 +27,15 @@ An Azure AI services multi-service resource provides a collection of Azure AI se
 
 Exceptions to billing through the multi-service resource include [AzureOpenAIEmbedding](cognitive-search-skill-azure-openai-embedding.md) or the [AML skill](cognitive-search-aml-skill.md) billing. Azure AI Search doesn't internally host models from Azure OpenAI or the Azure AI Foundry model catalog. Usage for AML and Azure OpenAI skills and vectorizers are through [Azure OpenAI pay-as-you-go pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing) and [Azure Machine Learning pay-as-you-go pricing](https://azure.microsoft.com/pricing/details/machine-learning/), respectively. A few other skills, such as Text Split and Text Merge, aren't billable.
 
-To attach an Azure AI multi-resource, you must provide connection information in the skillset. You can use a key on the connection, or implement a keyless approach that's currently in preview.
+To attach an Azure AI multi-service resource, you must provide connection information in the skillset. You can use a key on the connection, or implement a keyless approach that's currently in preview.
 
 > [!TIP]
 > Azure provides infrastructure for you to monitor billing and budgets. For more information about monitoring Azure AI services, see [Plan and manage costs for Azure AI services](/azure/ai-services/plan-manage-costs).
 
 ## Prerequisites
 
 + Connectivity over a public endpoint, unless your search service meets the creation date, tier, and region requirements for private connections to an Azure AI services multi-service resource.
++ [Azure AI multi-service resource](/azure/ai-services/multi-service-resource) created via the [Azure portal[(https://portal.azure.com) only.
 
 > [!NOTE]
 > If your Azure AI resource is configured to use a private endpoint, Azure AI Search can connect [using a shared private link](search-indexer-howto-access-private.md) For more information, see the [requirements and limits for using shared private links](search-limits-quotas-capacity.md#shared-private-link-resource-limits).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブ サービスへの接続に関する日付の更新と説明の改訂"
}
```

### Explanation
この変更は、`cognitive-search-attach-cognitive-services.md`という記事に対して行われたマイナーな更新です。主に、文中の「m.date」を2025年3月16日から2025年4月2日に変更し、文言を「Azure AI multi-resource」から「Azure AI multi-service resource」に修正しました。また、プライベートエンドポイントを使用する場合に関する新しい情報も追加し、接続要件の明確化を図っています。このような変更により、ユーザーは最新の情報に基づいてAzure AIサービスを効果的に利用できるようになります。


