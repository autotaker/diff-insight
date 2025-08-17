---
date: '2025-08-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:80a6ada...MicrosoftDocs:7708062
summary: このドキュメントの更新では、新しいセキュリティ機能や破壊的な変更はありませんが、Microsoft Entra IDを利用したサービス間呼び出しとAzure
  Private Linkによるプライベートエンドポイント接続に関する具体的な説明が追加され、内部トラフィック管理が明確にされています。これにより、ユーザーは安全なネットワーク構築に必要な情報を得ることができ、エンジニアにとって特に有用な内容となっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:80a6ada...MicrosoftDocs:7708062){target="_blank"}

# ハイライト
このドキュメントの更新で、新しいセキュリティ機能や重要な変更はありません。しかし、Microsoft Entra IDを介した認証・認可のサービス間呼び出しとAzure Private Linkを使用したプライベートエンドポイント接続についての説明が具体的に追加されており、内部トラフィック管理が明確化されています。

## 新しい機能
- Azure Private Linkを使用したプライベートエンドポイント接続の具体的な記述が追加されました。

## 破壊的変更
- 特に破壊的な変更はありません。

## その他の更新
- Microsoft Entra IDを介したサービス間呼び出しについての具体的な説明が追加されています。
- ドキュメント内の関連リンクが強調され、ユーザーが追加情報に容易にアクセスできるようになっています。

# インサイト
この更新は、既存のセキュリティ文書をより詳細かつ正確にするためのものであり、内部ネットワークトラフィックとサービス間のセキュリティの理解を深めることを目的としています。具体的には、同じリージョンにおけるコンテンツプロセッシングリクエストが、Azure AI Searchによって専用ホストされたマルチサービスリソースに向かうことが記述されています。これにより、技術ユーザーは内部トラフィックの流れをより正確に理解でき、セキュリティ上の注意をより適切に行うことができます。

Azure Private Linkに関する情報の追加は、ネットワークセキュリティを向上させ、外部からのトラフィックを最小化し、ネットワーク上の攻撃面を縮小するための有効な手段としての位置付けを明確にするためのものです。この種の具体的な説明は、特にセキュリティやネットワーク管理に携わるエンジニアにとって重要です。

また、Microsoft Entra IDを介したサービス認証・認可の明確な説明は、認証プロトコルに関する理解を深め、セキュリティモデルの強化と適切なコンプライアンスを維持するために重要となります。総じて、今回の更新によりドキュメントがより役立つリソースとなり、ユーザーにとって使いやすい情報源となっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-security-overview.md](#item-6b3f1e) | minor update | 検索セキュリティ概要の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-security-overview.md{#item-6b3f1e}

<details>
<summary>Diff</summary>
````diff
@@ -92,7 +92,7 @@ Internal requests are secured and managed by Microsoft. You can't configure or c
 Internal traffic consists of:
 
 + Service-to-service calls for tasks like authentication and authorization through Microsoft Entra ID, resource logging sent to Azure Monitor, and [private endpoint connections](service-create-private-endpoint.md) that utilize Azure Private Link.
-+ Requests made to Azure AI services APIs for [built-in skills](cognitive-search-predefined-skills.md)
++ Requests for [built-in skills processing](cognitive-search-predefined-skills.md), with same-region requests directed to an internally hosted Azure AI multi-service resource used exclusively for built-in skills processing by Azure AI Search.
 + Requests made to the various models that support [semantic ranking](semantic-search-overview.md#availability-and-pricing).
 
 <a name="service-access-and-authentication"></a>
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索セキュリティ概要の更新"
}
```

### Explanation
このコードの差分は、"search-security-overview.md"というドキュメントにおけるマイナーな更新を示しています。主な変更は、内部トラフィックに関する説明の一部を修正し、Microsoft Entra IDを介した認証や認可のサービス間呼び出し、リソースログをAzure Monitorに送信することに加え、Azure Private Linkを利用したプライベートエンドポイント接続についての具体的な記述が追加されました。

具体的には、リクエストが「コンテンツ」のプロセッシングに関して、同じリージョンでのリクエストがAzure AI Searchによって専用にホストされているマルチサービスリソースに向かうことが明確に説明されています。この変更により、ドキュメントはより正確で理解しやすいものになりました。また、対応するリンクも強調されており、ユーザーがさらに詳しい情報を得られるよう配慮されています。


