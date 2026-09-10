---
date: '2026-09-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e6b3e61...MicrosoftDocs:0d6f6ab
summary: この更新では、Azure Document Intelligenceのサービス制限に関するドキュメントが改定され、新しいドキュメントタイプが追加されました。新機能として、APIバージョンや価格帯に応じたモデル使用制限の情報を含む詳細テーブルが導入され、ユーザーはサービスの仕様についてより詳しく把握できるようになっています。特に破壊的な変更はなく、無料プランと標準プランのモデル使用量クォータを比較するための情報も追加されています。この改訂により、ユーザーは自分のニーズに合った最適な利用プランを選定できることが期待されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e6b3e61...MicrosoftDocs:0d6f6ab){target="_blank"}

# ハイライト
この更新では、Azure Document Intelligenceのサービス制限に関するドキュメントが改定され、新しいドキュメントタイプが追加されました。これにより、ユーザーはサービスの仕様について、より詳細で最新の情報を得ることができるようになっています。

## 新機能
- ドキュメントタイプの追加。
- APIバージョンや価格帯に応じたモデル使用制限などの情報を含む詳細テーブルの追加。

## 破壊的変更
- 特にありません。

## その他の更新
- 無料プラン（F0）と標準プラン（S0）のモデル使用量クォータを比較することでユーザーが正確な利用プランを選択できるようにするための情報追加。

# インサイト
Azure Document Intelligenceは、ドキュメントの処理能力を高めるためのAIサービスであり、多くのビジネスユーザーにとって重要なツールです。今回のドキュメント更新では、サービスの使用に関連する制限事項が明確化されています。具体的には、異なる価格プラン間のリソース使用制限を明示的に比較できるようにすることで、ユーザーが最適なプランを選択するための判断材料を得ることができます。

また、サポートされるドキュメントタイプの追加は、Azure Document Intelligenceの対応範囲の拡大を示しており、ユーザーの多様なニーズに応えるための機能強化といえます。今回の更新は、単なる情報のアップデートというだけでなく、ユーザーが自分のニーズに合った最適な利用方法を見つけられるよう、実践的で役立つ情報を提供することを目的としています。このような情報の提供は、Azure Document Intelligenceをより効果的に活用するためのものであり、ユーザーエクスペリエンスの向上につながると言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [service-limits.md](#item-5ceae5) | minor update | サービス制限の更新とドキュメントタイプの追加 | modified | 15 | 1 | 16 | 


# Modified Contents
## articles/ai-services/document-intelligence/service-limits.md{#item-5ceae5}

<details>
<summary>Diff</summary>
````diff
@@ -27,7 +27,13 @@ This article contains both a quick reference and detailed description of Azure D
 
 ## Model usage
 
+Model usage limits vary by API version and pricing tier. Review the supported document types and service quotas that apply to your resource.
+
 :::moniker range="doc-intel-4.0.0"
+### Supported document types
+
+The following table shows the document types that each model supports in API version 4.0.
+
 |Document types supported|Read|Layout|Prebuilt models|Custom models|Add-on capabilities|
 |--|--|--|--|--|----|
 | PDF | ✔️ | ✔️ | ✔️ | ✔️ |✔️|
@@ -45,6 +51,10 @@ For Document Intelligence v4.0 `2024-11-30` (GA) supports page and line features
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
+### Supported document types
+
+The following table shows the document types that each model supports in API version 3.1.
+
 |Document types supported|Read|Layout|Prebuilt models|Custom models|
 |--|--|--|--|--|
 | PDF | ✔️ | ✔️ | ✔️ | ✔️ |
@@ -97,6 +107,10 @@ Document Intelligence billing is calculated monthly based on the model type and
 
 ::: moniker-end
 
+### Service quotas
+
+The following table compares model usage quotas for the Free (F0) and Standard (S0) pricing tiers.
+
 |Quota|Free (F0)<sup>1</sup>|Standard (S0)|
 |--|--|--|
 | **Analyze transactions Per Second limit** | 1 | 15 (default value) |
@@ -107,7 +121,7 @@ Document Intelligence billing is calculated monthly based on the model type and
 | Adjustable | No | Yes <sup>2</sup> |
 | **List operations Per Second limit** | 1 | 10 (default value) |
 | Adjustable | No | Yes <sup>2</sup> |
-| **Maximum number of Document Intelligence resources per region** | 20 | 20 |
+| **Maximum number of Document Intelligence resources per region** | 1 | 20 |
 | Adjustable | No | No |
 | **Max document size** | 4 MB | 500 MB |
 | Adjustable | No | No |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス制限の更新とドキュメントタイプの追加"
}
```

### Explanation
このコードの変更は、Azure Document Intelligenceに関するサービス制限とサポートされるドキュメントタイプに関する情報を更新することを目的としています。具体的には、APIバージョンや価格帯に応じたモデル使用制限、サポートされるドキュメントタイプ、およびそれぞれのモデルがサポートする機能に関するテーブルを追加しています。また、無料プラン（F0）と標準プラン（S0）のモデル使用量クォータを比較するためのテーブルも新たに追加されています。

変更による影響として、Azure Document Intelligenceを使用するユーザーが現在のサービス仕様をよりよく理解できるようになり、適切なプランや仕様を選択するための情報が強化されています。この変更は、ドキュメントの可読性を向上させ、すべてのユーザーに対して最新かつ正確な情報を提供することを目的としています。


