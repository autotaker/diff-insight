---
date: '2026-04-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:cca71eb...MicrosoftDocs:7563a01
summary: この変更では、`cognitive-search-common-errors-warnings.md`のドキュメントがマイナーに更新され、新しいセクションが追加されました。主な内容として、インデックススキーマの検出に関連するエラーの説明と解決策が含まれています。この更新により、ユーザーはエラー処理を迅速に行い、トラブルシューティングが容易になることを目指しています。特に破壊的な変更はなく、日付フィールドも更新されました。全体として、この変更はAzure
  Cognitive Searchのユーザーエクスペリエンスの向上に寄与します。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:cca71eb...MicrosoftDocs:7563a01){target="_blank"}

<format>
# ハイライト
この変更では、`cognitive-search-common-errors-warnings.md`のドキュメントに対するマイナーな更新が行われ、新しいセクションが追加されました。具体的には、日付の更新と、インデックススキーマの検出に関連するエラーの新しいセクションが取り入れられました。

## 新機能
- インデックススキーマの検出に関連するエラーのセクションが追加されました。これにより、データソースからのインデックススキーマを検出する際のエラーが発生する可能性のある理由とその解決策が詳細に記載され、ユーザーの問題解決をサポートします。

## 破壊的変更
- 特に破壊的な変更はなく、既存の機能を損なう変更は行われていません。

## その他の更新
- `ms.date`フィールドの日付が更新されました。

# 洞察
今回のドキュメントの更新では、Azure Cognitive Searchを利用するユーザーが直面するかもしれない、インデックススキーマの検出に関する問題について詳述されています。特に新しいセクションは、実際のエラー処理にかかる時間を減少させ、トラブルシューティングのプロセスを簡素化することを目的としています。これはAzure Cognitive Searchを活用する上で重要な改善といえます。この種のマイナーな更新は、ユーザーエクスペリエンスを向上させ、プロダクティビティを高めることに寄与します。エラーメッセージの改善によって、開発者は問題の原因を迅速に突き止め、効果的に解決することが可能になり、サービスの信頼性を向上させることが期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-common-errors-warnings.md](#item-a5c854) | minor update | マイナーな更新: 認識エラーと警告に関する文書の更新 | modified | 14 | 1 | 15 | 


# Modified Contents
## articles/search/cognitive-search-common-errors-warnings.md{#item-a5c854}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: error-reference
-ms.date: 10/14/2025
+ms.date: 04/23/2026
 ms.update-cycle: 180-days
 ---
 
@@ -440,3 +440,16 @@ This error occurs when the Azure AI Search indexer cannot authenticate using the
 | Managed identity not enabled or access not granted | The AI Search service [managed identity](search-how-to-managed-identities.md) is enabled but lacks the required access roles. | - Enable system or user-assigned [managed identity](search-how-to-managed-identities.md) on the search Service.<br>- Assign appropriate role(s) to the identity (for example, `Storage Blob Data Reader` for blob containers). Each [data source](search-data-sources-gallery.md) has its own permission requirements. |
 | Network/firewall blocks identity access | The resource contacted is configured to restrict network access. | Configure [network settings](search-indexer-howto-access-ip-restricted.md) to allow Azure AI Search access. |
 | Key authorization has been disabled | Shared key access removed on the source, but the Search service data source configuration still uses key-based authentication. | Use [managed identity](search-how-to-managed-identities.md) authentication and ensure role-based permissions are in place. From an Azure Storage perspective, this means that [shared key authorization functionality is blocked](/azure/storage/common/shared-key-authorization-prevent), either from the storage account itself, or enforced through enterprise-level Azure Policies. |
+
+## `Error: Error detecting index schema from data source`
+
+The Azure portal experience used to configure the indexer was unable to retrieve schema information from the data source. This can happen due to transient connectivity issues or network configuration restrictions that prevent Azure AI Search from accessing the source.
+
+| Reason | Details/Example | Resolution |
+| --- | --- | --- |
+| Transient communication issues | `Failed to fetch, this could be due to transient communication errors with the source` | Transient failures can occur due to temporary network interruptions or service timeouts. Retry the operation. If the issue is transient, it should resolve in subsequent calls. |
+| Private endpoint restrictions | The data source is protected by a virtual network or private endpoint, preventing access from the indexer. | If the data source is behind a private endpoint, configure a [shared private link](search-indexer-howto-access-private.md) so that Azure AI Search can connect privately to the resource. Ensure the private endpoint connection is approved. |
+| Firewall rules blocking access | The data source has firewall rules that block requests from Azure AI Search. | Update firewall settings to allow inbound traffic from Azure AI Search. See [configure firewall rules to allow indexer access](search-indexer-howto-access-ip-restricted.md). Ensure the search service IP or trusted service exceptions are allowed. |
+| Network configuration does not allow indexer access | The data source is configured to only allow selected networks without including Azure AI Search. | Verify that the data source network configuration allows access from Azure AI Search using one of the supported connectivity options: public endpoint with IP rules, shared private link, or trusted service access. |
+
+
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マイナーな更新: 認識エラーと警告に関する文書の更新"
}
```

### Explanation
このコードの変更は、`cognitive-search-common-errors-warnings.md`というドキュメントに対する更新を示しています。主な変更点は、日付の更新とエラーメッセージに関する新しいセクションの追加です。具体的には、`ms.date`フィールドが2025年10月14日から2026年4月23日に変更されました。また、新たに「データソースからのインデックススキーマを検出する際のエラー」というセクションが追加され、多くの可能性のある理由とそれに対する解決策が詳述されています。この更新により、ユーザーはAI検索サービスを使用した際に直面する可能性のあるエラーの解消方法についての理解を深めることができます。全体として、追加された情報は14行、削除された行は1行で、合計15行の変更が加えられています。


