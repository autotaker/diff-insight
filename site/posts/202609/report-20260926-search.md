---
date: '2026-09-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b9ebc1d...MicrosoftDocs:d9568cd
summary: このドキュメントの変更では、Azure AIの検索リミットとクォータに関する情報が更新され、特にS3 HDサービスの制限が明示されました。また、知識ソースおよび知識ベースの最大値、新しいAPIバージョンに対する知識ソースの選択肢、リトリーブにおける理由付けについての詳細も追加されています。これにより、ユーザーはリソース使用計画を立てやすくなり、システムパフォーマンスの向上に寄与することが期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b9ebc1d...MicrosoftDocs:d9568cd){target="_blank"}

# ハイライト
このドキュメントの変更では、Azure AIの検索リミットとクォータに関する情報が更新されました。特に、S3 HD サービスにおける制限が明示され、知識ソースや知識ベースの最大値に関する情報が新たに追加されています。また、APIバージョンやリトリーブの理由付けに基づく知識ソースの選択肢についても詳細が追加されています。

## 新機能
- 知識ソースに関する最大値の更新: 知識ソースおよび知識ベースに関する最大数が変更され、それぞれのサービスに関連した制限が明確に説明されています。

## 破壊的変更
- 特に言及された破壊的変更はありませんが、新しい制限の明示化により、既存の構成の検討が必要な場合があります。

## その他の更新
- 異なるAPIバージョンによる知識ソースの選択肢について、具体的な説明が追加されています。
- リトリーブの際の理由付けに基づいた選択肢が詳述されています。

# インサイト
この差分では、Azure AIに関する技術仕様の詳細なアップデートが行われ、エンドユーザーにとってのドキュメントの正確性と実用性が向上しています。たとえば、これまで曖昧だったS3 HDサービスに関する制限が、明確な数値で説明されており、ユーザーがサービスリソースの使用計画を立てやすくなっています。

新たに追加されたAPIバージョンごとの知識ソース選択に関する情報は、開発者やエンジニアがどのバージョンを使用するかを評価する際に重要な要素となります。また、リトリーブの理由付けによる知識ソースの選択肢詳細は、より適切で効率的なデータアクセスと処理を可能にし、システム全体のパフォーマンス向上に寄与します。

このドキュメントの更新は、実際のリソース制約をより明確に把握したり、最適なリソース拡張戦略を立てたりする際に役立ちます。これにより、ユーザーはAzure AIプラットフォーム上での開発と管理における信頼性を一層向上させることができるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索リミットとクォータに関する更新 | modified | 9 | 7 | 16 | 


# Modified Contents
## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -318,22 +318,24 @@ A [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) specifies
 
 | Resource | Free | Basic | S1 | S2 | S3 | S3 HD | L1 | L2 | Serverless Developer |
 |--|--|--|--|--|--|--|--|--|--|
-| Maximum knowledge sources per service | 3 | 5 or 15 <sup>1</sup> | 50 | 200 | 200 | 0 | 10 | 10 | 30 |
-| Maximum knowledge bases per service | 3 | 5 or 15 <sup>1</sup> | 50 | 200 | 200 | 0 | 10 | 10 | 30 |
-| Maximum knowledge sources per knowledge base | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 0 | 10 | 10 | 10 |
+| Maximum knowledge sources per service | 3 | 5 or 15 <sup>1</sup> | 50 | 200 | 200 | 1000 per partition or 3000 per service <sup>2</sup> | 10 | 10 | 30 |
+| Maximum knowledge bases per service | 3 | 5 or 15 <sup>1</sup> | 50 | 200 | 200 | 1000 per partition or 3000 per service <sup>2</sup> | 10 | 10 | 30 |
+| Maximum knowledge sources per knowledge base | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 10 <sup>2</sup> | 10 | 10 | 10 |
 
 <sup>1</sup> Basic services created before April 3, 2024 have lower limits (5) on knowledge sources and knowledge bases.
 
+<sup>2</sup> These limits apply to S3 HD services that support knowledge bases and knowledge sources. Some older S3 HD services don't support these resources.
+
 ### Knowledge source selection during retrieval
 
 A knowledge base can contain up to the tier-specific maximum shown above, regardless of the API version or retrieval reasoning effort. The API version and reasoning effort instead affect how many knowledge sources can be selected during retrieval.
 
 | API version | Retrieval reasoning effort | Free | Basic | S1 | S2 | S3 | S3 HD | L1 | L2 |
 |--|--|--|--|--|--|--|--|--|--|
-| `2026-05-01-preview` and later | `minimal`, `low`, `medium` | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 0 | 10 | 10 |
-| `2026-04-01`, `2025-11-01-preview` | `minimal` <sup>2</sup> | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 0 | 10 | 10 |
-| `2025-11-01-preview` | `low` | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 |
-| `2025-11-01-preview` | `medium` | 3 | 5 | 5 | 5 | 5 | 0 | 5 | 5 |
+| `2026-05-01-preview` and later | `minimal`, `low`, `medium` | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 10 | 10 | 10 |
+| `2026-04-01`, `2025-11-01-preview` | `minimal` <sup>2</sup> | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 10 | 10 | 10 |
+| `2025-11-01-preview` | `low` | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
+| `2025-11-01-preview` | `medium` | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
 
 The `2025-08-01-preview` uses the legacy knowledge agent contract and doesn't support `retrievalReasoningEffort`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索リミットとクォータに関する更新"
}
```

### Explanation
この修正では、Azure AI における検索リミットとクォータに関する情報が更新されました。具体的には、知識ソースおよび知識ベースに関する最大値が変更されており、特に S3 HD サービスの制限が明示されています。また、異なる API バージョンとリトリーブの理由付けの努力に基づく知識ソースの選択肢についても詳細が追加されています。

変更点の中で、知識ソースごとの最大数が特定のサービスに関連した条件（たとえば、パーティションごとの制限やサービス全体の制限）と共に更新されました。加えて、いくつかの過去のサービスの制限についても言及されており、読者がどのようにリソースを使用できるかを理解するのに役立つ情報が補足されています。

この修正は、ドキュメントの信頼性を高め、エンドユーザーがリソースの使用を計画する際に必要な最新の情報を提供することを目的としています。


