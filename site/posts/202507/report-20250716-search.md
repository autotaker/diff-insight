---
date: '2025-07-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dbb4e58...MicrosoftDocs:ebd05f8
summary: 今回の変更では、Azure AI Searchサービスの地域サポートが更新され、インドネシア中央、マレーシア西、ニュージーランド北などの新しい地域が追加されました。既存のデータも修正され、特定の地域におけるエンリッチメントや検索機能の可用性が明確に示されるようになりました。破壊的な変更はないため、既存のユーザーにとっても安心して利用できる内容です。この更新により、ユーザーは地域ごとのサービス可用性をより具体的に把握でき、サービスを選ぶ際に柔軟な計画が可能になります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dbb4e58...MicrosoftDocs:ebd05f8){target="_blank"}

<format>
# ハイライト
今回の変更では、Azure AI Searchサービスにおける地域サポートが更新されました。具体的には、いくつかの地域に新しいデータが追加され、既存のデータが修正されています。これにより、主に特定の地域におけるエンリッチメント、可用性ゾーン、エージェンティック検索、セマンティックランカー、クエリリライトのサポート状況が明確に示されています。

## 新機能
- インドネシア中央、マレーシア西、ニュージーランド北などの地域が新たにサポート対象として追加。
  
## 破壊的変更
- 破壊的な変更は特に含まれていませんが、既存のデータの修正が行われました。

## その他の更新
- 既存のデータセクションに対する軽微な修正。

# インサイト
Azure AI Searchサービスにおける地域サポートの更新により、ユーザーは自身の利用する地域に対して、どの機能やサービスが利用可能かをより具体的に把握できるようになりました。この更新は、特定の地域におけるAzure AI Searchの機能可用性に関する詳細情報の提供を目的としており、テーブル形式でわかりやすく整理されています。

特に、今回の追加地域として「インドネシア中央」、「マレーシア西」、「ニュージーランド北」が挙げられ、アジア太平洋地域でのサービス利用オプションが拡充されています。これにより、これらの地域に拠点を置くユーザーや企業が、より利便性の高いサービスと機能を選択できるようになります。

この更新は、Azure AI Searchの拡張における継続的な取り組みの一環と捉えられ、地域ごとのサービス可用性に関する透明性を向上させています。結果として、ユーザーはより適切な判断に基づいてサービスを活用できる環境が整えられています。サービスの選定において、特定の機能の必要性に応じて最適な地域を選べるようになり、企業や個人プロジェクトの柔軟な計画立案が可能となるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-region-support.md](#item-25b0f1) | minor update | 検索リージョンのサポートの更新 | modified | 9 | 6 | 15 | 


# Modified Contents
## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -61,19 +61,19 @@ You can create an Azure AI Search service in any of the following Azure public r
 
 | Region | AI enrichment | Availability zones | Agentic retrieval | Semantic ranker | Query rewrite |
 |--|--|--|--|--|--|
-| North Europe​​ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| West Europe​​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | France Central​​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Germany West Central​ ​| ✅ | ✅ | ✅ | ✅ |  |
 | Italy North​​ |  | ✅ | ✅ | ✅ |  |
 | Norway East​​ | ✅ | ✅ |  |  |  |
+| North Europe​​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Poland Central​​ |  |  | ✅ | ✅ |  |
 | Spain Central <sup>1</sup> |  | ✅ |  |  |  |
 | Sweden Central​​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Switzerland North​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Switzerland West​ | ✅ | ✅ | ✅ | ✅ |  |
 | UK South​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | UK West​ ​|  |  | ✅ | ✅ |  |
+| West Europe​​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 
 <sup>1</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
 
@@ -99,16 +99,19 @@ You can create an Azure AI Search service in any of the following Azure public r
 |--|--|--|--|--|--|
 | Australia East​ ​| ✅ | ✅ | ✅ | ✅ | ✅ |
 | Australia Southeast​​​ |  |  | ✅ | ✅ |  |
-| East Asia​ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| Southeast Asia​​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Central India | ✅ | ✅ | ✅ | ✅ | ✅ |
+| East Asia​ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| Indonesia Central |  | ✅ |  |  |  |
 | Jio India West​​ | ✅ |  | ✅ | ✅ | ✅ |
-| South India |  | ✅ |  |  |  |
+| Jio India Central​​ |  |  |  |  |  |
 | Japan East | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Japan West​ | ✅ |  | ✅ | ✅ |  |
 | Korea Central | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Korea South​​ |  |  | ✅ | ✅ |  |
-| Indonesia Central |  | ✅ |  |  |  |
+| Malaysia West |  | ✅ |  |  |  |  |
+| New Zealand North |  | ✅ |  |  |  |
+| South India |  | ✅ |  |  |  |
+| Southeast Asia​​ | ✅ | ✅ | ✅ | ✅ | ✅ |
 
 ## Azure Government regions
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索リージョンのサポートの更新"
}
```

### Explanation
この変更では、Azure AI Searchサービスのサポートされる地域に関する情報が更新されました。具体的には、いくつかの地域の行に新しいデータが追加され、他の行の情報が修正されています。これにより、ユーザーが利用できる機能やサービスの可用性をより正確に把握できるようになっています。主な変更点は、特定の地域に対するエンリッチメントや可用性ゾーン、エージェンティック検索、セマンティックランカー、クエリリライトのサポートの有無がテーブル形式で明示されていることです。

追加された行には、「インドネシア中央」や「マレーシア西」、「ニュージーランド北」などが含まれており、地域間の選択肢が拡充されています。また、情報反映のために既存のデータセクションが若干修正され、全体としてより詳細で信頼性の高い情報が提供されるようになっています。これにより、ユーザーは自身のプロジェクトやニーズに最適なリージョンを選択する際の参考として役立てることができます。


