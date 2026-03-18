---
date: '2026-03-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:117898a...MicrosoftDocs:91b94fa
summary: この差分は、Azure AI Search サービスの地域サポートに関する文書の更新を含み、地域名に関連したサポートアイコンの表示が修正されました。新しい数値タグが追加され、異なる地域の詳細なサポート状況が反映されるようになりました。破壊的な変更はなく、既存情報に補完的な更新が施されています。地域サポートアイコン表記はより詳細で正確な情報を提供するように改訂されており、これは地域マーケティングや技術計画において重要な役割を果たします。ユーザーはサービス展開や計画において、より良い判断が下せるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:117898a...MicrosoftDocs:91b94fa){target="_blank"}

<format>
# ハイライト
この差分は、Azure AI Search サービスの地域サポートに関する文書の更新を含んでおり、地域名に関連したサポートアイコンの表示に修正が加えられました。

## 新機能
新しい数値タグが既存の地域サポートに追加され、異なる地域における詳細なサポート状況を反映するように更新されました。

## 破壊的変更
特に破壊的な変更はありません。既存の情報に補完的な更新が加えられたのみです。

## その他の更新
地域サポートアイコン表記が、より詳細で正確な情報を伝えるように更新されました。

# インサイト
このドキュメントの更新は、小規模であるにも関わらず、地域マーケティングおよび技術計画において重要な役割を果たします。Azure AI Search サービスが提供されている地域での機能の可用性や制限をより正確に把握できるようになるため、ユーザーはサービスポートフォリオの展開や計画において、より良い判断を下せるようになります。

具体的には、East US 2 および South Central US の地域において、サポートされる機能やその制約を示す数値タグが「<sup>1</sup>」から「<sup>1, 2</sup>」に変わり、サポートアイコンにおいてより多段階の情報を提供しています。これは、例えば特定の機能が一部のデプロイメントフェーズにおいてのみ利用可能であることを示しているかもしれません。

この情報更新は、Azure AI Search サービスに関するエンジニアリングと製品戦略において、地域ごとのサービス能力を見直し、再評価するための重要な手段となります。さらに、このようなドキュメントの正確性向上は、ユーザーエクスペリエンスの向上と直接結びついており、信頼性の高い情報に基づく意思決定をサポートします。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-region-support.md](#item-25b0f1) | minor update | Azure AI Search サービスの地域サポートに関する更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -44,10 +44,10 @@ You can create an Azure AI Search service in any of the following Azure public r
 | Canada East​​ ​<sup>1</sup> |  |  | ✅ |  | ✅ |  |
 | ​Central US​​ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | East US​ <sup>1, 2</sup> | ✅ | ✅ | ✅ |  | ✅ |  |
-| East US 2 <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| East US 2 <sup>1, 2</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Mexico Central |  | ✅ |  |  |  |  |
 | North Central US​ <sup>1</sup> ​| ✅ |  | ✅ |  | ✅ | ✅ |
-| South Central US​ <sup>1</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| South Central US​ <sup>1, 2</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | West US​​ <sup>1, 2</sup> | ✅ |  | ✅ |  | ✅ | ✅ |
 | West US 2​ <sup>3</sup> ​| ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | West US 3​ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search サービスの地域サポートに関する更新"
}
```

### Explanation
この変更は、Azure AI Searchサービスがサポートする地域に関する文書の修正を含んでいます。特に、地域名におけるサポートアイコンの表記が更新されました。具体的には、以下の2つの地域に*sup*タグが追加されました：

1. **East US 2**: 以前は「<sup>1</sup>」のみでしたが、新たに「<sup>2</sup>」が追加され、「<sup>1, 2</sup>」に変更されました。
2. **South Central US**: 同様に、ここでも*sup*タグが「<sup>1</sup>」から「<sup>1, 2</sup>」に更新されました。

これにより、これらの地域での機能やサービスのサポートに関する情報がより明確に示されるようになりました。全体として、この修正はドキュメントの正確性を向上させるためのマイナーな更新と見なされます。


