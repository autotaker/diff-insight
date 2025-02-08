---
date: '2025-02-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:22af4d0...MicrosoftDocs:4912a73
summary: このコードディフは、Azureドキュメントに関するマイナーアップデートであり、特に日付やURLフォーマットの変更が含まれています。新機能として、Azure
  OpenAIとAzure AIマルチサービスアカウントへのプライベート接続がサポートされ、Azure Governmentが新たに対応することでセキュリティが向上しました。大きな互換性の破壊はなく、主にURLパラメータの修正や更新日付の最新化が行われています。この変更は、Azureの技術を利用する開発者や技術者向けに情報を提供し、ユーザーがサービスをより効率的に利用できるよう工夫されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:22af4d0...MicrosoftDocs:4912a73){target="_blank"}

# ハイライト
このコードディフは、Azureドキュメントに関するマイナーアップデートであり、特に日付とURLフォーマットの変更に焦点を当てています。一部のURLパラメータと、プライベートリンクに関するサポート範囲の拡張が更新の中心です。

## 新機能
新機能として、Azure OpenAIとAzure AIマルチサービスアカウントへのプライベート接続の対応が明記されました。これにより、Azure Governmentがサポートされることで、セキュリティ面での優位性が向上しました。

## 互換性を壊す変更
互換性を壊す大きな変更は見られません。変更は日付やURLパラメータに関する調整であり、既存の機能に直接影響するものではありません。

## その他の更新
- `ms.date` の更新：記事の更新日が最新のものに改訂されました。
- URLパラメータの修正：`experience=data-engineering` は `experience=power-bi` に変更され、対象が明確化されました。
- Azure OpenAIに関する詳細なサポート情報が追加されました。

# 洞察
この変更は、主にAzureの最先端技術を利用する開発者や技術者に向けたものであり、最新の情報を提供することを目的としています。特に、ベクトルデータのインポートやプライベートリンクの利用における新しい機能の追加によって、ユーザーがより効率的にサービスを活用できるように工夫されています。

日付の更新は、ドキュメントが最新の状態に保たれていることを示す一般的な管理の一環ですが、新しいURLパラメータの設定やサポート範囲の拡張は、サービスの進化にあわせてユーザーが適切な設定をすぐに適用できるようにする重要な一手です。特に、Azure Governmentのサポートが新たに追加されたことで、より広範囲のユーザーが安心してプライベートリンクを活用できるようになりました。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | 日付とURLフォーマットの更新 | modified | 2 | 2 | 4 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | 日付とプライベートリンクのサポートに関する更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: quickstart
-ms.date: 11/22/2024
+ms.date: 02/06/2025
 ---
 
 # Quickstart: Vectorize text and images by using the Azure portal
@@ -148,7 +148,7 @@ This section points you to the content that works for this quickstart.
 
    1. Select **Upload files**, and then upload the [health-plan PDF documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/health-plan) used for this quickstart.
 
-1. Before you leave the lakehouse, copy the URL, or get the workspace and lakehouse IDs, so that you can specify the lakehouse in the wizard. The URL is in this format: `https://msit.powerbi.com/groups/00000000-0000-0000-0000-000000000000/lakehouses/11111111-1111-1111-1111-111111111111?experience=data-engineering`.
+1. Before you leave the lakehouse, copy the URL, or get the workspace and lakehouse IDs, so that you can specify the lakehouse in the wizard. The URL is in this format: `https://msit.powerbi.com/groups/00000000-0000-0000-0000-000000000000/lakehouses/11111111-1111-1111-1111-111111111111?experience=power-bi`.
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付とURLフォーマットの更新"
}
```

### Explanation
この変更は、ドキュメント内の日付と特定のURLフォーマットに関する2つの修正を含んでいます。具体的には、`ms.date` の値が 2024年11月22日から2025年2月6日に更新されました。また、湖邊（lakehouse）のURLフォーマットが変更され、`experience=data-engineering`から`experience=power-bi`に置き換えられています。これにより、Azureポータルにおけるベクトルのインポートに関する情報が最新の内容に沿ったものとなっています。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 12/19/2024
+ms.date: 02/07/2025
 ---
 
 # Make outbound connections through a shared private link
@@ -124,7 +124,7 @@ You can create a shared private link for the following resources.
 
 <sup>6</sup> The `Microsoft.CognitiveServices/accounts` resource type is used for vectorizer and indexer connections to Azure OpenAI embedding models when implementing [integrated Vectorization](vector-search-integrated-vectorization.md). As of November 19, 2024, there's now support for shared private link to embedding models in the Azure AI Foundry model catalog or to the Azure AI Vision multimodal API.
 
-<sup>7</sup> Shared private link for Azure OpenAI is only supported in public cloud. Other cloud offerings such as [Microsoft Azure Government](https://azure.microsoft.com/explore/global-infrastructure/government/) don't have support for shared private links for `openai_account` Group ID.
+<sup>7</sup> Shared private link for Azure OpenAI is only supported in public cloud and [Microsoft Azure Government](https://azure.microsoft.com/explore/global-infrastructure/government/). Other cloud offerings don't have support for shared private links for `openai_account` Group ID.
 
 <sup>8</sup> Shared private links are now supported (as of November 2024) for connections to Azure AI multiservice accounts. Azure AI Search connects to Azure AI multiservice for [billing purposes](cognitive-search-attach-cognitive-services.md). These connections can now be private through a shared private link. Shared private link is only supported when configuring [a managed identity (keyless configuration)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) in the skillset definition. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付とプライベートリンクのサポートに関する更新"
}
```

### Explanation
この変更は、ドキュメント内の日付および共有プライベートリンクに関する情報を更新しています。具体的には、`ms.date` の値が2024年12月19日から2025年2月7日に改訂されました。また、Azure OpenAIの共有プライベートリンクについての表記が変更され、これによりMicrosoft Azure Governmentがサポートされることが明記されました。さらに、Azure AIマルチサービスアカウントへの接続がプライベートで行えるようになったことが再確認されています。これらの変更は、ユーザーに最新の情報を提供し、Azure AI Searchの利用に関する理解を深めることを目的としています。


