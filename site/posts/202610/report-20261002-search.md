---
date: '2026-10-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a5c5c51...MicrosoftDocs:b7b13a9
summary: このコードの変更では、「articles/search/search-region-support.md」に対してマイナーなアップデートが行われ、Azureの特定地域に関する情報が最新のものに更新されました。注釈が追加され、地域選択の理解が深まるよう工夫されています。今回の更新は破壊的変更を伴わず、表や注釈の改善により情報の正確性が向上しています。この変更は、ユーザーが最新の地域サポート情報を容易に把握できるようにし、サービス選択においてより良い決定を下せるよう支援します。地域情報の正確さがユーザーエクスペリエンスの向上につながることが期待されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a5c5c51...MicrosoftDocs:b7b13a9){target="_blank"}

<format>
# ハイライト
このコードの変更では、「articles/search/search-region-support.md」へのマイナーなアップデートが行われ、Azureの特定の地域に関する情報が更新されました。特に、新しい注釈が追加され、地域選択の理解を促進しています。情報がより明確になり、利用可能な地域に関する最新データが反映されています。

## 新機能
- 更新により、各Azure地域に関する具体的な注釈が追加され、ユーザーにより明確な指針が提供されています。

## 重大な変更
- 今回の更新には、破壊的変更は含まれていません。

## その他の更新
- 表や注釈が改良され、利用可能な地域情報が最新化され、情報の正確性が向上しました。

# 洞察
この変更は、Azureのサービスを利用するユーザーにとって重要な地域情報の更新に特化しています。多くの場合、地域情報はユーザーが特定のサービスを利用する能力や効率に影響を及ぼすため、こうした情報の正確さは極めて重要です。この変更によって、ユーザーは最新の地域サポート情報に基づいてサービスを選択できるため、より最適化された決定を行うことができます。さらに、変更は注釈の形式で行われているため、ドキュメントを読みやすくし、特定の地域に関する理解を深める手助けをしている点が評価できます。Azureを利用する際の地域選択のプロセスが、より簡便になり、ユーザーエクスペリエンスの向上につながっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-region-support.md](#item-25b0f1) | minor update | 検索地域のサポートの更新 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -54,7 +54,7 @@ You can create an Azure AI Search service in any of the following Azure public r
 | South Central US​ <sup>1 </sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | West US​​ <sup>1, 2</sup> | ✅ | ✅ | ✅ | ✅ |  | ✅ |
 | West US 2​ <sup>3</sup> ​| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| West US 3​ <sup>2</sup>| ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| West US 3​ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | West Central US​ ​<sup>1</sup>| ✅ | ✅ | ✅ | ✅ |  |  |
 
 <sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
@@ -74,12 +74,12 @@ You can create an Azure AI Search service in any of the following Azure public r
 | North Europe​ <sup>2</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | Poland Central​​ <sup>1</sup> |  | ✅ | ✅ |  |  | ✅ |
 | Spain Central <sup>3</sup> |  |  | ✅ |  | ✅ | ✅ |
-| Sweden Central​​ <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| Sweden Central​​ <sup>1,2</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Switzerland North​ <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Switzerland West​ | ✅ | ✅ | ✅ |  | ✅ |  |
 | UK South​ <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | UK West​ ​|  | ✅ | ✅ |  |  |  |
-| West Europe​​ <sup>1</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| West Europe​​ <sup>1,2</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 
 <sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索地域のサポートの更新"
}
```

### Explanation
この変更では、「articles/search/search-region-support.md」ファイルに対して、いくつかの小さな修正が行われました。具体的には、特定のAzure地域に関する情報が更新され、各行に追加の注釈が加えられています。これにより、ユーザーがサービスを利用する際に地域選択の理解を深めることができるようになりました。変更点は、地域のサポート情報をより明確にするための微修正であり、全体的に表や注釈が更新されています。これにより、利用可能な地域やその特徴に関する最新情報が提供されています。


