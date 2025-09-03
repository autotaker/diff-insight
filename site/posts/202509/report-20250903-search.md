---
date: '2025-09-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4d69ee9...MicrosoftDocs:06ab90f
summary: Azure AI Searchに関する重要な2つのファイルが更新され、セキュリティとパフォーマンスの情報が改善されました。新機能として、プライベート実行環境の設定方法やIPファイアウォールの設定に関する詳細が追加されました。また、特定のスキルを持つインデクサーに関する制限も明示され、プライベート接続が利用できないケースが示されています。これにより、ユーザーはAzureのAIサービスを安全に最大限に活用できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4d69ee9...MicrosoftDocs:06ab90f){target="_blank"}

# Highlights
Azure AI Search のセキュリティとパフォーマンスに関する2つの主要なファイルが更新されました。「検索インデクサーのセキュリティ保護」と「検索の制限、クォータ、キャパシティ」に関する情報が細かに改善されました。

## New features
- Azure AI Searchインデクサーのプライベート実行環境に関する説明を強化し、プライベート接続設定方法に関する詳細情報を追加しました。
- インデクサーの実行環境に関するIPファイアウォール設定について新しいセクションが導入されました。

## Breaking changes
- 「Azure OpenAI Embedding」や「Azure AI Vision」のスキルを持つインデクサーに関連する制限が追加され、プライベート接続が利用できないケースが明示されました。

## Other updates
- 基本的なプライベート環境の制限に関する脚注や説明を充実させ、ユーザーがより良い理解を得られるようにしました。

# Insights
この更新は、Azure AI Searchの利用者にとって非常に重要です。クラウドサービスでのデータセキュリティの重要性が増す中、それに関連するインデクサーの設定は多くのIT管理者にとって関心事項です。今回の記事の更新は、ユーザーがプライベート環境で検索機能を実行する際に必要とする情報を提供し、負荷の軽減策を詳述しています。

特に、新たに追加されたIPファイアウォール設定は、セキュリティを管理するためのオプションとなり、組織のポリシー遵守に役立ちます。同時に、「Azure OpenAI Embedding」や「Azure AI Vision」などの高度な機能を利用する場合の制限についての情報提供は、リソース管理やパフォーマンスの最適化に寄与します。

このドキュメントの改善は、利用者がAzureのAIサービスを最大限に活用し、同時にリスクを最小限に抑えるための認識を深めるものです。更新された情報を基に、ユーザーはインデクサーの設定を適切に行い、実行環境の安定性を向上させることができます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-indexer-securing-resources.md](#item-c075c4) | minor update | リソースを保護するための検索インデクサーの更新 | modified | 3 | 1 | 4 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索の制限、クォータ、キャパシティに関する情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-indexer-securing-resources.md{#item-c075c4}

<details>
<summary>Diff</summary>
````diff
@@ -76,10 +76,12 @@ For any given indexer run, Azure AI Search determines the best environment in wh
 
 | Execution environment | Description |
 |-----------------------|-------------|
-| Private | Internal to a search service. Indexers running in the private environment share computing resources with other indexing and query workloads on the same search service. If you set up a private connection between an indexer and your data, such as a shared private link, this is the only execution environment you can use and it's used automatically. |
+| Private <sup>1</sup> | Internal to a search service. Indexers running in the private environment share computing resources with other indexing and query workloads on the same search service. If you set up a private connection between an indexer and your data, such as a shared private link, this is the only execution environment you can use and it's used automatically. |
 |  multitenant | Managed and secured by Microsoft at no extra cost. It isn't subject to any network provisions under your control. This environment is used to offload computationally intensive processing, leaving service-specific resources available for routine operations. Examples of resource-intensive indexer jobs include skillsets, processing large documents, or processing a high volume of documents. |
 
 
+<sup>1</sup> To prevent heavy load on the private execution environment, indexers with more than 2 Azure OpenAI Embedding or Azure AI Vision multimodal embeddings skills will be restricted from running in this environment.
+
 ### Setting up IP ranges for indexer execution
 
 This section explains IP firewall configuration for admitting requests from either execution environment.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースを保護するための検索インデクサーの更新"
}
```

### Explanation
この変更は、`articles/search/search-indexer-securing-resources.md`ファイルにおいて、Azure AI Searchのインデクサーに関連する情報を更新するもので、主に2つの新しい要素が追加されています。まず、プライベート実行環境の説明に脚注が追加され、特に「Azure OpenAI Embedding」や「Azure AI Vision」などのスキルを持つインデクサーの制限についての情報が提供されました。これにより、プライベート環境での負荷を軽減する措置が強調されています。さらに、インデクサーの実行環境に関するIPファイアウォール設定についての新しいセクションが導入され、利用者が要求を受け付けるための設定方法について説明しています。

この変更は、利用者がインデクサーを設定する際に必要な追加情報を提供することで、より良い理解を促進することを目的としています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -156,7 +156,7 @@ Indexers can access other Azure resources [over private endpoints](search-indexe
 | Maximum private endpoints | N/A | 10 or 30 | 100 | 400 | 400 | N/A | 20 | 20 |
 | Maximum distinct resource types <sup>3</sup> | N/A | 4 | 7 | 15 | 15 | N/A | 4 | 4 |
 
-<sup>1</sup> AI enrichment and image analysis are computationally intensive and consume disproportionate amounts of available processing power. For this reason, private connections are disabled on lower tiers to ensure the performance and stability of the search service itself. On Basic services, private connections to an Azure AI services multi-service resource are unsupported to preserve service stability. For the S1 tier, make sure the service was created with [higher limits](search-limits-quotas-capacity.md#partition-storage-gb) after April 3, 2024.
+<sup>1</sup> AI enrichment and image analysis are computationally intensive and consume disproportionate amounts of available processing power. For this reason, private connections are disabled on lower tiers to ensure the performance and stability of the search service itself. On Basic services, private connections to an Azure AI services multi-service resource are unsupported to preserve service stability. For the S1 tier, make sure the service was created with [higher limits](search-limits-quotas-capacity.md#partition-storage-gb) after April 3, 2024. Indexers with more than 2 Azure OpenAI Embedding or Azure AI Vision multimodal embeddings skills will be restricted from running in private environment, and private connections will not be available.
 
 <sup>2</sup> Private connections to an embedding model are supported on Basic and S1 high-capacity search services created after April 3, 2024, with the [higher limits](search-limits-quotas-capacity.md#partition-storage-gb) for storage and computational processing.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索の制限、クォータ、キャパシティに関する情報の更新"
}
```

### Explanation
この変更は、`articles/search/search-limits-quotas-capacity.md`ファイルにおいて、Azure AI Searchの検索制限、クォータ、およびキャパシティに関する情報を更新するものです。主に、プライベート接続に関する制限が追加されました。具体的には、2つ以上の「Azure OpenAI Embedding」や「Azure AI Vision」などのマルチモーダル埋め込みスキルを持つインデクサーは、プライベート環境での実行が制限され、プライベート接続が利用できなくなることが明記されました。この変更は、インデクサーのパフォーマンス向上と安定性を維持するための重要な情報を提供します。

また、プライベート接続が無効となる理由や、基本サービスにおける安定性を保つための措置についても引き続き説明されています。この更新によって、ユーザーはAzure AIサービスの利用に関する最新の制限を理解しやすくなります。


