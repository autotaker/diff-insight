---
date: '2025-04-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:11d129c...MicrosoftDocs:63f4fcb
summary: このドキュメントでは、Azure AI Searchにおける検索セキュリティとロールベースのアクセス制御（RBAC）に関する重要な情報が追加・改訂されました。主な変更点は、RBACの機能に関する詳細説明と日付の更新です。新機能として、RBACに関するテーブルへの注釈追加や権限設定の具体的な説明が行われ、データインポートウィザードの利用制限が明確化されました。互換性を壊す変更はありませんが、アクセス制御の説明が強化され、理解が深まります。また、ドキュメントの日付更新によって内容が最新化され、インデックス作成やデータ読み取りに関する役割も明示されました。この更新により、セキュリティ管理の透明性が向上し、システム管理者はより効果的なセキュリティポリシーの設定が可能になります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:11d129c...MicrosoftDocs:63f4fcb){target="_blank"}

# Highlights
このドキュメントの更新では、Azure AI Searchにおける検索セキュリティとRBAC（ロールベースのアクセス制御）に関する重要な情報の追記と改訂が行われました。主な変更点としては、RBACの機能の詳細説明と日時の更新が含まれています。

## 新機能
- RBACに関するテーブルに注釈が追加され、データインポートウィザードの使用制限がより明確になりました。
- 権限の具体的な設定方法がより詳細に説明されました。

## 互換性を壊す変更
特に互換性を壊すような変更はありませんが、アクセス制御に関する説明が強化されているため、読み手の理解が深まります。

## その他のアップデート
- ドキュメントの日付が更新され、内容が最新のものにリフレッシュされました。
- インデックス作成やデータ読み取りに関する貢献者とオーナーの役割が明示されました。

# インサイト
この更新は、Azure AI Searchにおけるセキュリティ管理の透明性を向上させるためのものです。特に、RBACにおける役割と権限の境界がより明確にされたことで、システム管理者がセキュリティポリシーを効果的に設定できるようになります。特にオーナーが唯一役割を割り当てられる存在であることが強調されることで、より安全な操作が可能となっています。また、ドキュメントが最新の日付に更新されることで、ユーザーにとっての情報の信頼性が高まりました。このドキュメント更新は、管理が必要なリソースが増加する中で、Azure AI SearchのRBAC機能を効果的に活用するための重要なステップといえるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-security-rbac.md](#item-a5d129) | minor update | 検索セキュリティRBACのドキュメント更新 | modified | 4 | 2 | 6 | 


# Modified Contents
## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 01/27/2025
+ms.date: 03/31/2025
 ms.custom: subject-rbac-steps, devx-track-azurepowershell
 ---
 
@@ -90,7 +90,7 @@ Combine these roles to get sufficient permissions for your use case.
 |List all objects on the resource |❌|❌|✅|✅|✅|
 |Access quotas and service statistics |❌|❌|✅|✅|❌|
 |Read/query an index |✅|✅|❌|❌|❌|
-|Upload data for indexing |❌|✅|❌|✅|❌|
+|Upload data for indexing <sup>1</sup>|❌|✅|❌|❌|❌|
 |Create or edit indexes/aliases |❌|❌|✅|✅|❌|
 |Create, edit and run indexers/data sources/skillsets |❌|❌|✅|✅|❌|
 |Create or edit synonym maps |❌|❌|✅|✅|❌|
@@ -103,6 +103,8 @@ Combine these roles to get sufficient permissions for your use case.
 |Configure private connections |❌|❌|✅|✅|❌|
 |Configure network security |❌|❌|✅|✅|❌|
 
+<sup>1</sup> In the Azure portal, an Owner or Contributor can run the Import data wizards that create and load indexes, even though they can't upload documents in other clients. Data connections in the wizard are made by the search service itself and not individual users. The wizards have the `Microsoft.Search/searchServices/indexes/documents/*` permission necessary for completing this task.
+
 Owners and Contributors grant the same permissions, except that only Owners can assign roles.
 
 <!-- Owners and Contributors can create, read, update, and delete objects in the Azure portal *if API keys are enabled*. the Azure portal uses keys on internal calls to data plane APIs. In you subsequently configure Azure AI Search to use "roles only", then Owner and Contributor won't be able to manage objects in the Azure portal using just those role assignments. The solution is to assign more roles, such as Search Index Data Reader, Search Index Data Contributor, and Search Service Contributor. -->
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索セキュリティRBACのドキュメント更新"
}
```

### Explanation
この修正は、Azure AI Searchの検索セキュリティに関するRBAC（ロールベースのアクセス制御）ドキュメントの更新を含んでいます。具体的には、ドキュメントの日付が2025年1月27日から2025年3月31日に変更されています。また、RBACに関するテーブルの一部に注釈が追加され、データのインポートウィザードについての情報が明確に説明されています。この情報は、オーナーまたは貢献者がインデックスを作成・読み込みできるが、他のクライアントでは文書をアップロードできないことを示しています。さらに、オーナーが役割を割り当てる唯一の存在であることが強調され、ドキュメントの内容がより説明的になっています。これにより、ユーザーはどのように役割や権限が機能するのかをより理解できるようになります。


