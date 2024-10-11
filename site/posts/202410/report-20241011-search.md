---
date: '2024-10-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7341d04...MicrosoftDocs:576156f
summary: |-
  このドキュメントでは、「インデックスエイリアスの制限」に関する変更について説明しています。主な変更点は、「サービス作成日」に基づく新しい条件が追加され、これがインデックスエイリアスの最大数に影響を与えることを明確にしています。具体的には、2022年10月以降に作成されたサービスに対して、インデックスの最大数の2倍がエイリアスの最大数として設定される新たな条件が導入されました。

  破壊的な変更はありませんが、既存のサービスに対する理解に影響を与える可能性があります。また、情報の整理が改善されたことで、テーブル形式が変更され、情報の視認性が向上しました。この更新は、ユーザーが自身の構築環境の制限を理解するのに重要であり、新しい条件により、エイリアスの最大数に対する期待値が明確化され、特に大規模なデータセットを扱う際に役立つ情報が提供されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7341d04...MicrosoftDocs:576156f){target="_blank"}

# ハイライト
ドキュメント「インデックスエイリアスの制限」における変更は、新しい条件「サービス作成日」によるインデックスエイリアスの最大数への影響が追加されました。これは、新しいルールが適用され、特定の日付を境にエイリアスの数に違いが生じることを明確にしています。

## 新機能
- 2022年10月以降に作成されるサービスについては、インデックスの最大数の2倍がエイリアスの最大数となるという新規条件が追加されました。

## 破壊的変更
- 破壊的な変更は特にありませんが、既存のサービスの制限に対する理解に新しい条件が影響を与える可能性があります。

## その他の更新
- セクション内のテーブル形式が変更され、情報の整理が改善されました。

# 洞察
このドキュメントの更新では、ユーザーが自身の構築環境の制限を理解するにあたり、非常に重要な要素が持ち込まれています。特に、インデックスエイリアスの制限に関する新しい条件は、作成日という容易に確認できる指標に基づいており、ユーザーが自らの環境がどの条件に該当するのかを判断する際の手助けとなります。

この変更により、これから新しくサービスを立ち上げるユーザーと、すでに運用中のサービスを持つユーザーの双方に対して、エイリアスの最大数に対する期待値が明確化されます。特に、大規模なデータセットを扱う際には、この制限の理解がパフォーマンスや構成の最適化に直結するため、ドキュメントの役割は重要です。

また、テーブルの形式が改善されたことにより、情報の視認性が向上し、ユーザーが求める情報に迅速にアクセスできるようになり、効率的な利用が可能となります。このような改善はユーザーエクスペリエンスの向上に寄与します。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | インデックスエイリアスの制限の更新 | modified | 6 | 3 | 9 | 


# Modified Contents
## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -166,11 +166,14 @@ Maximum number of synonym maps varies by tier. Each rule can have up to 20 expan
 
 ## Index alias limits
 
-Maximum number of [index aliases](search-how-to-alias.md) varies by tier. In all tiers, the maximum number of aliases is double the maximum number of indexes allowed.
+Maximum number of [index aliases](search-how-to-alias.md) varies by tier and [service creation date](vector-search-index-size.md#how-to-check-service-creation-date). In all tiers, if the service was created after October 2022 the maximum number of aliases is double the maximum number of indexes allowed. If the service was created before October 2022, the limit is the number of indexes allowed.
 
-| Resource | Free | Basic | S1 | S2 | S3 | S3-HD |L1 | L2 |
+| Service Creation Date | Free | Basic | S1 | S2 | S3 | S3-HD |L1 | L2 |
 |----------|------|-------|----|----|----|-------|----|----|
-| Maximum aliases |6 |10 or 30 |100 |400 |400 |2000 per partition or 6000 per service |20 |20 |
+| Before October 2022 | 3 | 5 or 15 <sup>1</sup> | 50 | 200 | 200 | 1000 per partition or 3000 per service | 10 | 10 |
+| After October 2022 | 6 | 30 | 100 | 400 | 400 | 2000 per partition or 6000 per service | 20 | 20 |
+
+<sup>1</sup> Basic services created before December 2017 have lower limits (5 instead of 15) on indexes
 
 ## Data limits (AI enrichment)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスエイリアスの制限の更新"
}
```

### Explanation
この修正は、ドキュメントの「インデックスエイリアスの制限」に関するセクションを更新しています。具体的には、インデックスエイリアスの最大数に影響を与える新しい条件として、「サービス作成日」が追加されました。新しい説明では、サービスが2022年10月以降に作成された場合、インデックスの最大数の2倍がエイリアスの最大数となります。逆に、2022年10月以前に作成された場合、エイリアスの制限は許可されるインデックスの数と同じになります。この変更により、利用者はサービスの作成日による制限の違いを理解しやすくなります。また、テーブルの形式が幾分変更され、情報が明確に整理されています。


