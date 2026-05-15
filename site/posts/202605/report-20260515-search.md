---
date: '2026-05-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9027b1b...MicrosoftDocs:ca3a955
summary: このコード変更では、Azure AI Searchに関連する検索サービスポータルの文書がマイナーアップデートされました。無料トライアル申込先のリンクが新しいURLに更新され、非アクティブな無料サービスの削除に関する注意喚起が追加されました。これにより、ユーザーエクスペリエンスが向上し、より正確で有用な情報へのアクセスが提供されます。また、注意書きにより、ユーザーが選択したサービスを維持するための考慮事項が示されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9027b1b...MicrosoftDocs:ca3a955){target="_blank"}

# Highlights
このコード変更では、Azure AI Searchに関連する検索サービスポータルの文書がマイナーアップデートされました。特筆すべきは、無料トライアル申込先のリンクが更新された点と、非アクティブな無料サービスの削除に関する注意喚起の追加です。

## New features
- 無料トライアルの申込先リンクが新しいURLに更新されました。

## Breaking changes
- 特にありません。

## Other updates
- 無料サービスの非アクティブによる削除の可能性に関する注意喚起が追加されました。

# Insights
今回の変更は、主にユーザーエクスペリエンスの向上を目的とした小さな修正です。旧リンクが新しいリンクに更新された理由としては、リンク先の情報が最新であることを保証し、ユーザーがより正確で有用な情報にアクセスできるようにするためと考えられます。また、「他サービスのために非アクティブな無料サービスを削除する可能性」についての注意書きが追加されたことにより、ユーザーが選択したサービスの維持に注意を払う必要があることを提示し、テクニカルな運用における考慮事項を情報として提供しています。このような文書の更新は、開発者やサービス利用者に対する支援として非常に重要です。ユーザーが適切にサービスを試用し、効果的に評価するための手助けとなります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-create-service-portal.md](#item-f90159) | minor update | 検索サービスポータルに関する情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-create-service-portal.md{#item-f90159}

<details>
<summary>Diff</summary>
````diff
@@ -44,7 +44,7 @@ Some properties are fixed for the lifetime of the search service. Before you cre
 
 Azure AI Search requires a free or Standard Azure subscription.
 
-To try Azure AI Search for free, [start a trial subscription](https://azure.microsoft.com/pricing/free-trial/?WT.mc_id=A261C142F) and then [create your search service on the Free tier](#choose-a-tier). Each Azure subscription can have one free search service, which is intended for short-term, non-production evaluation of the product. You can complete all of our quickstarts and most of our tutorials on the Free tier. For more information, see [Try Azure AI Search for free](search-try-for-free.md).
+To try Azure AI Search for free, [start a trial subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) and then [create your search service on the Free tier](#choose-a-tier). Each Azure subscription can have one free search service, which is intended for short-term, non-production evaluation of the product. You can complete all of our quickstarts and most of our tutorials on the Free tier. For more information, see [Try Azure AI Search for free](search-try-for-free.md).
 
 > [!IMPORTANT]
 > To make room for other services, Microsoft might delete free services that are inactive for an extended period of time.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスポータルに関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchに関する検索サービスポータルの文書における情報の小さな更新を反映しています。具体的には、Azure AI Searchの無料トライアルの申込先リンクが変更されました。元のリンクは「[start a trial subscription](https://azure.microsoft.com/pricing/free-trial/?WT.mc_id=A261C142F)」でしたが、新しいリンクは「[start a trial subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)」です。この変更は、リンク先の情報を最新のものに保ち、ユーザーが正確な情報にアクセスできるようにするために行われました。また、他のサービスのために非アクティブな無料サービスを削除する可能性についての注意喚起も含まれています。


