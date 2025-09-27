---
date: '2025-09-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:58a2b83...MicrosoftDocs:8df9d90
summary: この差分では、`search-capacity-planning.md`の記事の軽微な更新が行われ、最終更新日の日付変更や価格層に関する説明の具体化が主な内容です。新機能は追加されていないものの、既存の説明が詳細になり、ユーザー体験が向上しています。重大な変更はなく、情報の明確化が目的です。また、更新された情報に基づいて、ユーザーが利用可能なプランを判断しやすくなっています。このような更新はユーザーの混乱を避け、迅速な情報提供に寄与します。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:58a2b83...MicrosoftDocs:8df9d90){target="_blank"}

# Highlights
この差分では、`search-capacity-planning.md`の記事に対する軽微な更新が行われています。主に、最終更新日の日付変更と価格層に関する説明の具体化が行われました。

## New features
特筆すべき新機能は追加されていませんが、既存の説明がより詳細になっている点で、ユーザー体験の向上が図られています。

## Breaking changes
特に重大な変更はなく、既存の情報を明確化するための修正です。

## Other updates
- `ms.date`が最新の日付にアップデートされました。
- 価格層に関する情報がより具体的になりました。

# Insights
今回の更新は、日常的に使われる記事を最新の情報に保つための定期的なアップデートと理解できます。特に、価格層に関する詳細な情報は、サービス選択時に役立つものであり、ユーザーがどのプランが利用可能かを実際のオプションに基づいて判断できるように、よりクリアに定義されています。このような更新は、ユーザーの混乱を避け、必要な情報を迅速に提供する上で重要な役割を果たします。よって、技術的な内容に直接影響を与えることはないものの、ユーザーエクスペリエンスの面で一段と親切になったと言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-capacity-planning.md](#item-0dd6c9) | minor update | 検索容量計画に関する記事の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/search-capacity-planning.md{#item-0dd6c9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: conceptual
-ms.date: 09/15/2025
+ms.date: 09/26/2025
 ms.update-cycle: 180-days
 ---
 
@@ -130,7 +130,7 @@ To change your pricing tier:
 
 1. On the **Select Pricing Tier** page, choose a different tier from the list.
 
-   Currently, you can switch between Basic, S1, S2, and S3 only. Other pricing tiers are unavailable and appear dimmed.
+   You can switch between Basic, S1, S2, and S3, but you can't switch to or from Free, S3HD, L1, or L2. These tiers aren't selectable and appear dimmed.
 
    :::image type="content" source="media/search-capacity-planning/pricing-tier-list.png" alt-text="Screenshot of the Select Pricing Tier page and the list of available tiers in the Azure portal." border="true" lightbox="media/search-capacity-planning/pricing-tier-list.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索容量計画に関する記事の更新"
}
```

### Explanation
この変更は、`search-capacity-planning.md`というファイルの内容を更新し、主に日付と価格層の選択に関する情報が修正されています。具体的には、以下の2つの変更が行われました：

1. `ms.date`が09/15/2025から09/26/2025に更新されました。これは、コンテンツの最終更新日を反映しています。
   
2. 価格層の説明が具体化され、ユーザーが選択可能な価格層についての情報が修正されました。「現在はBasic、S1、S2、およびS3の間で切り替え可能」との表記が「Basic、S1、S2、およびS3の間で切り替え可能だが、Free、S3HD、L1、またはL2への切り替えはできない」と具体的な情報を加える形で更新されています。

この変更により、ユーザーが理解しやすい形で価格層の選択肢が示されています。


