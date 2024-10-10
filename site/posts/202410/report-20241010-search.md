---
date: '2024-10-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:eb045a9...MicrosoftDocs:7341d04
summary: この変更は、Azureポータルにおける顧客管理キー（CMK）暗号化に関するリンクの修正を目的としたマイナーアップデートです。これにより、ユーザーは正確な情報にアクセスできるようになり、CMK暗号化の使用方法の理解が容易になります。新機能は追加されていませんが、既存機能の情報のアクセス性が向上しています。互換性に影響する変更もなく、ユーザーにとってのドキュメントの信頼性とユーザビリティが高まる結果となります。正確なリンク提供により、Azureのサービス利用に対する知識が正確であることが重要です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:eb045a9...MicrosoftDocs:7341d04){target="_blank"}

<format>
# ハイライト
この変更は、Azureポータルにおける顧客管理キー（CMK）暗号化のサポートに関するリンクの修正を含むマイナーアップデートです。これにより、ユーザーは正確な情報にアクセスできるようになりました。

## 新機能
特に新機能の追加はありません。ただし、既存機能に対する情報のアクセス性が向上しました。

## 互換性に影響する変更
互換性に影響する変更は特にありません。

## その他の更新
リンクのパスが正確なものに修正されました。

# インサイト
この変更は主にドキュメント内の参照リンクを正すことを目的としています。Azureのユーザーにとって、顧客管理キー（CMK）の正確な使用方法は非常に重要です。CMK暗号化は、顧客が自分の暗号化キーを管理し、データのセキュリティを強化するための重要な機能です。Azure Key Vaultを使用することで、キーの生成、管理、使用が可能となりますが、これには正しい情報が必要です。

修正前のドキュメントは、おそらく誤ったリンクや情報を提示していた可能性があり、ユーザーの混乱を招く可能性がありました。この修正によって、Azureポータル内でオブジェクトを作成し、CMK暗号化を指定する際に、ユーザーは適切な手順と情報を容易に確認できるようになります。結果として、ドキュメントの信頼性とユーザビリティが向上し、Azureのサービス利用全般に対して間違いのない知識が提供されます。ドキュメントの正確性は、技術的リソースの品質を高め、安全性やコンプライアンスの観点からも非常に重要です。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [whats-new.md](#item-fa71b4) | minor update | ポータルによる顧客管理キー暗号化のサポートの修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ ms.custom:
 | [**Target filters in a hybrid search to just the vector queries**](hybrid-search-how-to-query.md#hybrid-search-with-filters-targeting-vector-subqueries-preview) | Feature | A filter on a hybrid query involves all subqueries on the request, regardless of type. You can override the global filter to scope the filter to a specific subquery. The new `filterOverride` parameter is available on hybrid queries using the [2024-09-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
 | [**Text Split skill (token chunking)**](cognitive-search-skill-textsplit.md) | Applied AI (skills) | This skill has new parameters that improve data chunking for embedding models. A new `unit` parameter lets you specify token chunking. You can now chunk by token length, setting the length to a value that makes sense for your embedding model. You can also specify the tokenizer and any tokens that shouldn't be split during data chunking. The new `unit` parameter and query subscore definitions are found in the [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
 | [**2024-09-01-preview**](/rest/api/searchservice/search-service-api-versions?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | API | Preview release of REST APIs for truncated dimensions in text-embedding-3 models, targeted vector filtering for hybrid queries, RRF subscore details for debugging, and token chunking for Text Split skill.|
-| [**Portal support for customer-managed key encryption (CMK)**](/azure/search/search-security-manage-encryption-keys?tabs=portal#step-4-encrypt-content) | Feature | When you create new objects in the Azure portal, you can now specify CMK-encryption and select an Azure Key Vault to provide the key. |
+| [**Portal support for customer-managed key encryption (CMK)**](search-security-manage-encryption-keys.md#step-4-encrypt-content) | Feature | When you create new objects in the Azure portal, you can now specify CMK-encryption and select an Azure Key Vault to provide the key. |
 
 ## August 2024
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータルによる顧客管理キー暗号化のサポートの修正"
}
```

### Explanation
この変更は、MicrosoftのAzure AIドキュメントに関する「whats-new.md」ファイルの修正であり、ポータルでの顧客管理キー（CMK）暗号化のサポートに関するリンクの修正が含まれています。具体的には、リンクのパスが更新され、正しい文書を参照するようにしました。この修正により、ユーザーはAzure portalで新しいオブジェクトを作成する際に、CMK暗号化を指定し、キーを提供するAzure Key Vaultを選択できる機能について、正確な情報にアクセスできるようになります。全体で、1行が追加され、1行が削除され、合計で2行の変更が反映されています。


