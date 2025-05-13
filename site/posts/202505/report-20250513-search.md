---
date: '2025-05-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d064b0a...MicrosoftDocs:6d3cef9
summary: この変更では、`search-indexer-securing-resources.md`ファイルが更新され、主に日付の修正とテキストの調整が行われました。特に、Azureのネットワークセキュリティに関連するインデクサーの実行環境に関する情報が最新化されています。具体的には、公開日が2024年12月19日から2025年5月12日に更新され、インデクサーの実行環境に関する記述が修正されて、一部の情報が削除されています。この更新は、ユーザーが現在の推奨構成やセキュリティ要件を理解し、Azureのセキュリティの恩恵を最大限に享受できるようにすることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d064b0a...MicrosoftDocs:6d3cef9){target="_blank"}

# ハイライト
この変更では、`search-indexer-securing-resources.md`ファイルの内容が更新され、特に日付の修正とテキストの調整が行われました。主な焦点はAzureのネットワークセキュリティに関連したインデクサーの実行環境に関する情報の最新化です。

## 新機能
- なし

## 互換性に影響のある変更
- なし

## その他の更新
- ファイルの公開日が2024年12月19日から2025年5月12日に更新されました。
- インデクサーの実行環境に関連するテキストが修正され、特定の情報が削除されています。

# 洞察
この変更は主に情報の更新と整合性の維持に焦点を当てています。具体的には、Azure上でインデクサーをセキュアに実行するためのガイドラインを最新のものとするために、日付の更新と一部内容の精査が行われました。

更新された日付は、ドキュメントの有効性を示すもので、次回のレビュータイミングをユーザーに知らせる役割も果たしています。さらに、インデクサーの実行環境に関する記述が修正されたことは、ユーザーが現在の推奨構成やセキュリティ要件を理解し、それを導入できるよう支援するためです。これにより、Azureのネットワークセキュリティの恩恵を最大限に享受することができ、リソースのセキュリティ確保をさらに強化することが可能となります。

この更新は、Azureプラットフォームの進化に伴い、ユーザーが最適なセキュリティ設定を理解し、そのノウハウをすぐに活用できるようにすることを目的としています。これにより、ユーザーはセキュリティに関する最新の知識を有し、それを実際の運用に適用することが容易になります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-indexer-securing-resources.md](#item-c075c4) | minor update | リソースのセキュリティに関する検索インデクサーの更新 | modified | 1 | 2 | 3 | 


# Modified Contents
## articles/search/search-indexer-securing-resources.md{#item-c075c4}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 12/19/2024
+ms.date: 05/12/2025
 ---
 
 # Indexer access to content protected by Azure network security
@@ -79,7 +79,6 @@ For any given indexer run, Azure AI Search determines the best environment in wh
 | Private | Internal to a search service. Indexers running in the private environment share computing resources with other indexing and query workloads on the same search service. If you set up a private connection between an indexer and your data, such as a shared private link, this is the only execution environment you can use and it's used automatically. |
 |  multitenant | Managed and secured by Microsoft at no extra cost. It isn't subject to any network provisions under your control. This environment is used to offload computationally intensive processing, leaving service-specific resources available for routine operations. Examples of resource-intensive indexer jobs include skillsets, processing large documents, or processing a high volume of documents. |
 
-For Standard2 services and higher, you can configure an indexer to always use the private environment. However, skillset processing always executes in the multitenant environment, even if you configure your search service to use the private environment. For more information about indexer configuration, see [Create an indexer](search-how-to-create-indexers.md?tabs=indexer-rest#create-an-indexer).
 
 ### Setting up IP ranges for indexer execution
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースのセキュリティに関する検索インデクサーの更新"
}
```

### Explanation
この変更では、`search-indexer-securing-resources.md`ファイルにおいて、日付の更新といくつかの内容修正が行われました。具体的には、文書の最初にある日付が2024年12月19日から2025年5月12日に変更されました。また、インデクサーの実行環境に関するテキストが修正され、特定の情報が削除されました。これにより、ユーザーがインデクサーの設定と実行に関する最新のガイダンスを得られるようになります。この更新は、コンテンツを保護するためのAzureのネットワークセキュリティに関連しており、利用者の理解を助けることを目的としています。


