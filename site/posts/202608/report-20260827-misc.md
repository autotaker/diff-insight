---
date: '2026-08-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:eaaa74d...MicrosoftDocs:d002f33
summary: この更新では、Azureの文書インテリジェンスに関する手順が改善され、特に仮想ネットワーク内でのデータサイエンスVMの設定に関する指示がよりシンプルになりました。外部リンクを省いたことで、ユーザーは手順をより理解しやすくなっています。また、新機能や破壊的変更はありませんが、全体としてユーザーエクスペリエンスが向上しています。こうした小さな改善が、Azureサービスの利用を一層容易にします。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:eaaa74d...MicrosoftDocs:d002f33){target="_blank"}

# ハイライト
この更新では、Azureの文書インテリジェンスのドキュメントにおける手順の一部が微修正され、特定の手順がよりシンプルに改良されました。特記すべきは、仮想ネットワーク内でのデータサイエンスVM構成の指示に関して、リンクを省いた形で説明が行われていることです。これにより、ユーザーが指示をよりシンプルに理解できるようになりました。

## 新機能
- 特に新しい機能の追加はありません。

## 破壊的変更
- 特に破壊的な変更はありません。

## その他の更新
- 仮想ネットワークにおけるデータサイエンスVM設定手順の記述が改良されました。

# インサイト
このドキュメントの更新は、ユーザーエクスペリエンスを向上させるために、指示がより簡潔に、かつ理解しやすくなるように行われています。これまでのドキュメントでは、外部リンクによって手順が複雑に見えたり、読者がリンクを辿る必要があったかもしれませんが、今回の改善でその点が解消されています。特に、仮想ネットワークでのVMの構成指示がわかりやすくなることで、設定における混乱や誤りが減少する可能性があります。

よりシンプルな形式での説明は、技術的な内容を扱うユーザーにとって重要であり、迅速な理解と実行を促進します。こうした小さな変更が積み重なることで、ドキュメント全体の品質が向上し、Azureサービスの活用がさらに容易に、そして確実になることが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [managed-identities-secured-access.md](#item-05ef7b) | minor update | 文書インテリジェンスの管理されたIDによるセキュアアクセスの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/authentication/managed-identities-secured-access.md{#item-05ef7b}

<details>
<summary>Diff</summary>
````diff
@@ -249,7 +249,7 @@ Great work! You now have all the connections between the Document Intelligence r
 
 To validate your deployment, you can deploy a virtual machine (VM) to the virtual network and connect to the resources.
 
-1. Configure a [Data Science VM](https://azuremarketplace.microsoft.com/marketplace/apps/microsoft-dsvm.dsvm-win-2019?tab=Overview) in the virtual network.
+1. Configure a Data Science VM in the virtual network.
 
 1. Remotely connect into the VM from your desktop and launch a browser session that accesses Document Intelligence Studio.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書インテリジェンスの管理されたIDによるセキュアアクセスの更新"
}
```

### Explanation
この変更は、文書インテリジェンスに関連するドキュメントにおいて、手順の一部を微修正しています。具体的には、仮想ネットワーク内でのデータサイエンスVMの構成に関する指示について、リンク付きの表現からリンクなしの単純な文に変更されています。この更新により、手順の記述がよりシンプルで読みやすくなりました。ドキュメントは引き続き[こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/d002f330ba477b9c1791b034c1b061c0aa15eb4f/articles%2Fai-services%2Fdocument-intelligence%2Fauthentication%2Fmanaged-identities-secured-access.md)で確認できます。


