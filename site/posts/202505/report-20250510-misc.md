---
date: '2025-05-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6987c76...MicrosoftDocs:c579297
summary: Azureの言語サービスにおいて、地域サポート情報が更新されました。新たにドイツ西部、イタリア北部、インド（ジオインディア中央および西部）、およびUK西部が追加され、一部地域のサポート状況も修正されました。特に、この更新により企業や個人が地域要件を満たしやすくなり、ユーザーエクスペリエンスとコンプライアンスの向上が期待されます。これにより、Azureはグローバル展開を進め、地域ごとのデータ保持や法令遵守に対応する能力を高めています。新しい地域は今後の市場拡大に貢献することが見込まれています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6987c76...MicrosoftDocs:c579297){target="_blank"}

# Highlights
Azureの言語サービスにおける地域サポート情報が更新されました。新しい地域が追加され、一部の既存地域のサポート状況が修正されています。

## New features
- ドイツ西部、イタリア北部、インド（ジオインディア中央および西部）、UK西部の地域が新たに追加。

## Breaking changes
- なし

## Other updates
- カナダ中央およびカナダ東の地域に関するサポート状況の修正。

# Insights
今回の更新により、Azureの言語サービスは地理的により幅広いサポートを提供できるようになりました。具体的には、ドイツ、イタリア、インド、イギリスといったユーザー基盤のある国の地域が新たにサポート対象となり、これによって企業や個人が地域要件を満たしやすくなっています。特に、多くの法人が拠点を持つこれらの地域への対応は、ユーザーエクスペリエンスを向上させるだけでなく、コンプライアンス面でも大きな利点を生むと言えるでしょう。

この更新は、Azureがグローバル展開をするにあたっての重要なステップであり、地域ごとのデータ保持や法令遵守のニーズへの対応力を示しています。特に新規に追加された地域は、今後の市場拡大において重要な役割を果たすことが予想され、ビジネスユーザーにとっても利用価値の高い情報となります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [regional-support.md](#item-5becd3) | minor update | 地域サポートの更新 | modified | 17 | 4 | 21 | 


# Modified Contents
## articles/ai-services/language-service/concepts/regional-support.md{#item-5becd3}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,8 @@ Conversational language understanding and orchestration workflow are only availa
 |--------------------|-----------|-------------|
 | Australia East     | ✓         | ✓           |
 | Brazil South       |           | ✓           |
-| Canada Central     |           | ✓           |
+| Canada Central     | ✓         | ✓           |
+| Canada East        |           | ✓           |
 | Central India      | ✓         | ✓           |
 | Central US         |           | ✓           |
 | China East 2       | ✓         | ✓           |
@@ -39,8 +40,11 @@ Conversational language understanding and orchestration workflow are only availa
 | East US            | ✓         | ✓           |
 | East US 2          | ✓         | ✓           |
 | France Central     |           | ✓           |
+| Germany West Central|           | ✓           |
+| Italy North        |           | ✓           |
 | Japan East         |           | ✓           |
 | Japan West         |           | ✓           |
+| Jio India Central  |           | ✓           |
 | Jio India West     |           | ✓           |
 | Korea Central      |           | ✓           |
 | North Central US   |           | ✓           |
@@ -54,6 +58,7 @@ Conversational language understanding and orchestration workflow are only availa
 | Switzerland North  | ✓         | ✓           |
 | UAE North          |           | ✓           |
 | UK South           | ✓         | ✓           |
+| UK West            |           | ✓           |
 | West Central US    |           | ✓           |
 | West Europe        | ✓         | ✓           |
 | West US            |            | ✓           |
@@ -68,15 +73,18 @@ Custom named entity recognition is only available in some Azure regions. Some re
 |--------------------|-----------|-------------|
 | Australia East     | ✓         | ✓           |
 | Brazil South       |           | ✓           |
-| Canada Central     |           | ✓           |
+| Canada Central     | ✓         | ✓           |
+| Canada East        |           | ✓           |
 | Central India      | ✓         | ✓           |
 | Central US         |           | ✓           |
 | East Asia          |           | ✓           |
 | East US            | ✓         | ✓           |
 | East US 2          | ✓         | ✓           |
 | France Central     |           | ✓           |
+| Germany West Central|           | ✓           |
 | Japan East         |           | ✓           |
 | Japan West         |           | ✓           |
+| Jio India Central  |           | ✓           |
 | Jio India West     |           | ✓           |
 | Korea Central      |           | ✓           |
 | North Central US   |           | ✓           |
@@ -90,6 +98,7 @@ Custom named entity recognition is only available in some Azure regions. Some re
 | Switzerland North  | ✓         | ✓           |
 | UAE North          |           | ✓           |
 | UK South           | ✓         | ✓           |
+| UK West            |           | ✓           |
 | West Central US    |           | ✓           |
 | West Europe        | ✓         | ✓           |
 | West US            |            | ✓           |
@@ -105,15 +114,18 @@ Custom text classification is only available in some Azure regions. Some regions
 |--------------------|-----------|-------------|
 | Australia East     | ✓         | ✓           |
 | Brazil South       |           | ✓           |
-| Canada Central     |           | ✓           |
+| Canada Central     | ✓         | ✓           |
+| Canada East        |           | ✓           |
 | Central India      | ✓         | ✓           |
 | Central US         |           | ✓           |
 | East Asia          |           | ✓           |
 | East US            | ✓         | ✓           |
 | East US 2          | ✓         | ✓           |
 | France Central     |           | ✓           |
+| Germany West Central|           | ✓           |
 | Japan East         |           | ✓           |
 | Japan West         |           | ✓           |
+| Jio India Central  |           | ✓           |
 | Jio India West     |           | ✓           |
 | Korea Central      |           | ✓           |
 | North Central US   |           | ✓           |
@@ -127,6 +139,7 @@ Custom text classification is only available in some Azure regions. Some regions
 | Switzerland North  | ✓         | ✓           |
 | UAE North          |           | ✓           |
 | UK South           | ✓         | ✓           |
+| UK West            |           | ✓           |
 | West Central US    |           | ✓           |
 | West Europe        | ✓         | ✓           |
 | West US            |            | ✓           |
@@ -166,4 +179,4 @@ Custom text classification is only available in some Azure regions. Some regions
 ### Next steps
 
 * [Language support](./language-support.md)
-* [Quotas and limits](./data-limits.md) 
\ No newline at end of file
+* [Quotas and limits](./data-limits.md) 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域サポートの更新"
}
```

### Explanation
この変更は、Azureの言語サービスにおける地域サポートに関する情報を更新したものです。具体的には、いくつかの新しい地域をテーブルに追加し、それに伴って既存の地域に関するサポート状況を修正しました。具体的には、カナダの地域（カナダ中央およびカナダ東）のサポート状況が更新され、ドイツ西部、イタリア北部、インドのジオ地域（ジオインディア中央と西部）、およびイギリスの地域（UK西部）が新たに追加されています。また、いくつかの行で既存の情報に対して小規模な修正が行われています。この変更は、言語サービスがより広範囲に対応することを意味しており、ユーザーへの情報提供を強化しています。


