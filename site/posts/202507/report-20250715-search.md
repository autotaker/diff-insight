---
date: '2025-07-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bd40fd4...MicrosoftDocs:dbb4e58
summary: このコード差分には、さまざまなドキュメントのマイナーアップデートが含まれています。主な変更点は、接続要件の明確化、エスケープシーケンスの拡張、プライベートリンクの使用方法の更新、スコアプロファイルの用語修正の4つに集約されます。エスケープシーケンスに関する新しい情報や、Azure
  AI Visionのマルチモーダル埋め込みに関連するプライベートリンクの説明が追加されました。また、互換性を破壊する変更はなく、リンク書式や用語の誤りの修正、文書の日付情報の更新も行われています。これらの更新は、ユーザーがAzure
  Cognitive Servicesを効果的に使うために重要なサポートとなります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bd40fd4...MicrosoftDocs:dbb4e58){target="_blank"}

# ハイライト

このコード差分には、さまざまなドキュメントのマイナーアップデートが含まれています。それぞれの変更は、接続要件の明確化、エスケープシーケンスの拡張、プライベートリンクの使用方法の更新、スコアプロファイルの用語修正の4つの主要なテーマです。

## 新機能

- エスケープシーケンスに関する情報の追加。
- Azure AI Visionのマルチモーダル埋め込みをサポートするプライベートリンクの説明。

## 互換性の破壊的変更

- 特に互換性を破壊する変更はありません。

## その他の更新

- リンク書式や用語の誤りの修正。
- 文書の日付情報の更新。

# インサイト

このドキュメントの更新は、ユーザーがAzure Cognitive ServicesおよびAzure AI関連サービスを効果的に利用するためのサポートとして重要です。

まず、「接続要件の明確化」に関する部分では、AzureのAIマルチサービスリソースに接続する際の手順が明確化されました。私たちが確認できるように、プライベート接続に関連する新しい情報が追加され、公共エンドポイントを経由せずに接続する必要があることが強調されています。これは、セキュリティを考慮した接続を行うための重要な情報です。

次に、「エスケープシーケンスの拡張と更新」では、特定の文字が特殊な意味を持つことを明確化し、それに関連するエスケープ方法が説明されています。これにより、異なる文脈での文字使用に対する理解が深まり、システムの誤動作を防ぐ助けとなります。

さらに、「プライベートリンクの接続に関する更新」では、新たにAzure AI Visionのマルチモーダル埋め込みをサポートするためのシェアードプライベートリンクについての情報が追加されました。これにより、ユーザーはプライベートリンクのさらなる可能性を活用できるようになります。

最後に、「スコアプロファイルに関する用語の修正」では、スコアリング結果がどのように順序付けされるかを説明する部分に誤記があり、これは迅速に修正されました。このような正確な情報提供は、ユーザーがシステムを正しく設定し、期待する結果を得るために必要です。

これらの変更によって、Azure Cognitive Servicesの実装において、より正確で意味のある文書が提供され、ユーザーがサービスを適切に利用するための重要な情報が強化されました。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | 接続要件の明確化: 公共エンドポイントへの接続 | modified | 1 | 1 | 2 | 
| [cognitive-search-skill-annotation-language.md](#item-aaedc7) | minor update | エスケープシーケンスの拡張と更新 | modified | 9 | 3 | 12 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | プライベートリンクの接続に関する更新 | modified | 3 | 3 | 6 | 
| [semantic-how-to-enable-scoring-profiles.md](#item-e8d524) | minor update | スコアプロファイルに関する用語の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ To attach an Azure AI multi-service resource, you must provide connection inform
 ## Prerequisites
 
 + Connectivity over a public endpoint, unless your search service meets the creation date, tier, and region requirements for private connections to an Azure AI services multi-service resource.
-+ [Azure AI multi-service resource](/azure/ai-services/multi-service-resource) created via the [Azure portal[(https://portal.azure.com) only.
++ [Azure AI multi-service resource](/azure/ai-services/multi-service-resource) created via the [Azure portal](https://portal.azure.com) only.
 
 > [!NOTE]
 > If your Azure AI resource is configured to use a private endpoint, Azure AI Search can connect [using a shared private link](search-indexer-howto-access-private.md) For more information, see the [requirements and limits for using shared private links](search-limits-quotas-capacity.md#shared-private-link-resource-limits).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "接続要件の明確化: 公共エンドポイントへの接続"
}
```

### Explanation
この変更は、Azure AI マルチサービスリソースに接続する際の要件に関する文書の一部を修正しています。具体的には、プライベート接続の条件に関する情報を追加し、公共エンドポイントを通じた接続が必要であることを強調しています。また、リンクの書式を修正し、正確なリンクとして機能するように改善されました。この変更により、読者はAzure AIサービスに接続する際の要件をより明確に理解できるようになります。

## articles/search/cognitive-search-skill-annotation-language.md{#item-aaedc7}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: reference
-ms.date: 04/15/2025
+ms.date: 07/14/2025
 ---
 # Skill context and input annotation language
 
@@ -106,8 +106,14 @@ Specific elements of an array can be referenced by using their numeric index lik
 
 ### Escape sequences
 
-There are two characters that have special meaning and need to be escaped if they appear in an expression and must be interpreted as is instead of as their special meaning: `'/'` and `'~'`.
-Those characters must be escaped respectively as `'~0'` and `'~1'`. 
+There are several characters that have a special meaning and need to be escaped if they are to be interpreted as-is instead of a syntax element. These characters include `#`, `/`, and `~` among others.
+
+| Escape sequence | Special meaning (usage in path syntax)  | Example |
+|---|---|
+| `~0` | Used for escaping `~` | "~0" for `~`, where "~/documents" becomes "~0~1documents"|
+| `~1` | Used for escaping `/` | "~1" for `/`, where "~/documents" becomes "~0~1documents" |
+| `~2` | Used for generically to escape arbitrary sequences (including but not limited to `#` and `*`) | "~2#~2" where "readme#requirements" becomes "readme~2#~2requirements" |
+
 
 ## Array enumeration
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エスケープシーケンスの拡張と更新"
}
```

### Explanation
この更新では、コグニティブ サーチのスキルアノテーション言語に関する文書が修正され、エスケープシーケンスに関する情報が追加されました。具体的には、特殊な意味を持つ文字（`#`、`/`、`~` など）が明確にリスト化され、これらの文字をエスケープする方法が詳述されています。また、エスケープシーケンスに関する表が追加され、具体的な使用例が提示されています。加えて、文書の日付情報も更新されています。この変更は、ユーザーがエスケープシーケンスを適切に使用するのに役立ち、文書全体の明確性を向上させます。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: mrcarter8
 ms.author: mcarter
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/01/2025
+ms.date: 07/14/2025
 ms.custom:
   - ignite-2024
   - sfi-image-nochange
@@ -30,7 +30,7 @@ Shared private link is a premium feature that's billed by usage. When you set up
 Azure AI Search makes outbound calls to other Azure resources in the following scenarios:
 
 + Knowledge agent connections to Azure OpenAI for agentic retrieval workflows
-+ Indexer or query connections to Azure OpenAI, Azure AI Vision, or the Azure AI Foundry model catalog for vectorization
++ Indexer or query connections to Azure OpenAI or Azure AI Vision for vectorization
 + Indexer connections to supported data sources
 + Indexer (skillset) connections to Azure Storage for caching enrichments, debug session sate, or writing to a knowledge store
 + Indexer (skillset) connections to Azure AI services for billing purposes
@@ -127,7 +127,7 @@ You can create a shared private link for the following resources.
 
 <sup>5</sup> See [Create a shared private link for a SQL Managed Instance](search-indexer-how-to-access-private-sql.md) for instructions.
 
-<sup>6</sup> The `Microsoft.CognitiveServices/accounts` resource type is used for vectorizer and indexer connections to Azure OpenAI embedding models when implementing [integrated Vectorization](vector-search-integrated-vectorization.md). As of November 19, 2024, there's now support for shared private link to embedding models in the Azure AI Foundry model catalog or to the Azure AI Vision multimodal API.
+<sup>6</sup> The `Microsoft.CognitiveServices/accounts` resource type is used for vectorizer and indexer connections to Azure OpenAI embedding models when implementing [integrated Vectorization](vector-search-integrated-vectorization.md). As of November 19, 2024, there's now support for shared private link to support the Azure AI Vision multimodal embeddings via [AI Services multi-service account](/azure/ai-services/multi-service-resource).
 
 <sup>7</sup> Shared private link for Azure OpenAI is only supported in public cloud and [Microsoft Azure Government](https://azure.microsoft.com/explore/global-infrastructure/government/). Other cloud offerings don't have support for shared private links for `openai_account` Group ID.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートリンクの接続に関する更新"
}
```

### Explanation
この修正では、Azure AI Searchのプライベートリンクに関する文書が更新されています。主な変更点は、文書の日付が更新されたことと、Azure OpenAIとの接続に関する説明の簡略化です。具体的には、インデクサーやクエリの接続に関して、Azure OpenAIだけでなく、Azure AI Visionに対しても言及されている部分が明確化されました。また、新しい情報として、Azure AI Vision のマルチモーダル埋め込みをサポートするための共有プライベートリンクについての説明が追加されています。これにより、ユーザーはプライベートリンクの使用方法とその機能がより理解しやすくなります。

## articles/search/semantic-how-to-enable-scoring-profiles.md{#item-e8d524}

<details>
<summary>Diff</summary>
````diff
@@ -92,7 +92,7 @@ POST https://{service-name}.search.windows.com/indexes/{index-name}/docs/search?
 }
 ```
 
-The response includes the new `rerankerBoostedScore`, alongside the L1 `@search.score` and the L2 `@search.rerankerSocre`. Results are ordered by `@search.rerankerBoostedScore`.
+The response includes the new `rerankerBoostedScore`, alongside the L1 `@search.score` and the L2 `@search.rerankerScore`. Results are ordered by `@search.rerankerBoostedScore`.
 
 ```json
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアプロファイルに関する用語の修正"
}
```

### Explanation
この変更では、セマンティック検索におけるスコアプロファイルの設定に関する文書が微修正されています。具体的には、レスポンスの説明部分において、`@search.rerankerSocre` という誤記が修正され、正しくは `@search.rerankerScore` と表記されています。この修正は、ユーザーが正確な情報を得るために重要です。また、この文書では、レスポンスに含まれるスコアに関する情報が整理され、結果がどのように order されるかについての正確な記述が強調されています。この変更により、ユーザーはスコアリングの仕組みをより明確に理解しやすくなります。


