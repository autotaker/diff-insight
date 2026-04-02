---
date: '2026-04-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:98210c1...MicrosoftDocs:72780de
summary: 今回のドキュメント更新では、エージェントリトリーバルソリューション、インデクサ、Azure役割による接続に関する重要な情報が追加されました。主な変更点には、Visual
  Studio Codeに関する新しいガイダンス、インデクサの権限に関する章の追加、Azure役割によるインデックス管理の戦略が含まれています。破壊的変更はありませんが、新しいガイドラインが既存の運用方針に影響を与える可能性があります。また、全体的な日付更新やネットワーク隔離環境に関する注意点が強調されています。これらの更新は、Azure
  AI Searchのデータ管理や権限管理に関する理解を深めるものであり、ユーザーのスムーズなエージェント展開をサポートし、データセキュリティの信頼性向上に寄与します。全体として、Azure
  AI Searchのベストプラクティスを提供する重要なステップとなっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:98210c1...MicrosoftDocs:72780de){target="_blank"}

<format>
# Highlights
今回のドキュメント更新では、エージェントリトリーバルソリューションやインデクサ、Azure役割による接続に関する重要な情報が追加されました。主な更新内容には、サンプルの日付変更、新しい機能の追加や特定状況での使用上の注意が含まれます。

## New features
- エージェントリトリーバルソリューションにおけるVisual Studio Codeのガイダンス追加。
- インデクサに関連する権限の動作に関するセクションの追加。
- Azure役割に基づくインデックス管理方法に関する戦略の提示。

## Breaking changes
特に破壊的変更は含まれていませんが、新しいガイドラインやセクションが追加されたことで、既存の運用方針に影響を与える可能性があります。

## Other updates
- 全体的に日付が新しく更新されました。
- ネットワーク隔離環境下での操作に関する注意が強調されています。

# Insights
今回の変更は、Azure AI Searchとその関連機能を使って業務を進める際の、特にデータ管理と権限管理に関する理解を深める更新となっています。まず、エージェントリトリーバルソリューションのチュートリアルでは、技術的なセットアップに関するより実践的なガイドが追加され、ユーザーがスムーズにエージェントを展開できるようにサポートしています。

次に、インデクサに関するドキュメントの更新では、インデクサがどのようにして各インデックスにアクセスを行うのか、その一連の動作内にある特別な権限レベルが明確化されました。これにより、Azure Searchプラットフォーム上でのデータセキュリティと管理手法に対する信頼性が向上します。

最後に、Azure役割とRBAC（ロールベースのアクセス制御）に関する説明では、ユーザーや開発者がどのようにして役割を効果的に管理し、データアクセスを制御するかが明確に示されています。ドキュメントのアップデートがいかにプロジェクトや運用におけるインデックス管理を強化するものであるかを示しています。まとめとして、これらの更新は共通の見通しと理解の向上に寄与し、Azure AI Searchを使用する際のベストプラクティス提供に向けた重要なステップを構成しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | エージェントリトリーバルソリューションのチュートリアルの更新 | modified | 4 | 1 | 5 | 
| [search-howto-run-reset-indexers.md](#item-fb10c8) | minor update | インデクサの実行またはリセットに関するドキュメントの更新 | modified | 4 | 1 | 5 | 
| [search-security-rbac.md](#item-a5d129) | minor update | Azure役割による接続に関するセクションの更新 | modified | 14 | 2 | 16 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: 'Tutorial: Build an Agentic Retrieval Solution'
 description: Build an agentic retrieval solution that connects Azure AI Search to Foundry Agent Service via MCP. Follow this tutorial to create a knowledge base and agent.
-ms.date: 03/11/2026
+ms.date: 04/01/2026
 ms.service: azure-ai-search
 ms.topic: tutorial
 ms.custom:
@@ -46,6 +46,9 @@ In this tutorial, you:
 
 + [Visual Studio Code](https://code.visualstudio.com/download) with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions.
 
+> [!IMPORTANT]
+> If you've disabled public network access for your search service and use it as an agent tool with a network-isolated Microsoft Foundry resource, you must use the Microsoft Foundry (new) portal, SDK, or CLI to build agents. The Microsoft Foundry (classic) portal doesn't support this scenario. For more information, see [Agent tools with network isolation](/azure/ai-foundry/how-to/configure-private-link#agent-tools-with-network-isolation).
+
 ## Understand the solution
 
 This solution combines Azure AI Search and Microsoft Foundry to create an end-to-end retrieval pipeline:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルソリューションのチュートリアルの更新"
}
```

### Explanation
このコードの変更は、エージェントリトリーバルソリューションのチュートリアルに関連するドキュメントの更新です。具体的には、サンプル文書の日時を「2026年3月11日」から「2026年4月1日」に変更し、新しいコンテンツを追加しています。

新たに追加された内容には、Visual Studio Codeとその関連拡張機能に関する情報、および検索サービスでのネットワーク隔離環境を使用する際の重要な注意事項が含まれています。特に、Microsoft Foundryリソースとの統合のための適切なポータルやツールの使用について詳述されています。この更新により、ユーザーはエージェントを構築する際の要件や重要な手順を把握しやすくなります。

## articles/search/search-howto-run-reset-indexers.md{#item-fb10c8}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Run or Reset Indexers
 description: Run indexers in full, or reset an indexer, skills, or individual documents to refresh all or part of a search index or knowledge store.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 10/02/2025
+ms.date: 03/26/2026
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
@@ -26,6 +26,9 @@ Indexers are one of the few subsystems that make overt outbound calls to other A
 
 In terms of Azure roles, indexers don't have separate identities: a connection from the search engine to another Azure resource is made using the [system or user-assigned managed identity](search-how-to-managed-identities.md) of a search service, plus a role assignment on the target Azure resource. If the indexer connects to an Azure resource on a virtual network, you should create a [shared private link](search-indexer-howto-access-private.md) for that connection.
 
+> [!NOTE]
+> Indexers operate with service-level permissions rather than user permissions. An indexer can write to any index on the search service, even if you assigned roles to restrict access to specific indexes. For more information, see [Per-index scope and indexer operations](search-security-rbac.md#per-index-scope-and-indexer-operations).
+
 ## Indexer execution
 
 A search service runs one indexer job per [search unit](search-capacity-planning.md#concepts-search-units-replicas-partitions). Every search service starts with one search unit, but each new partition or replica increases the search units of your service. You can check the search unit count in the Azure portal's Essential section of the **Overview** page. If you need concurrent processing, make sure your search units include sufficient replicas. Indexers don't run in the background, so you might experience more query throttling than usual if the service is under pressure.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサの実行またはリセットに関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、「インデクサの実行またはリセット」に関するドキュメントの更新を示しています。主な更新点は、文書の日付が「2025年10月2日」から「2026年3月26日」に変更されたことです。また、重要な情報が新たに追加されています。

新しく追加された内容には、インデクサの操作権限に関する重要な注意事項が含まれています。具体的には、インデクサがユーザーの権限ではなくサービスレベルの権限で動作することを明記し、特定のインデックスへのアクセスを制限する役割が割り当てられている場合でも、どのインデックスにも書き込みができることが説明されています。この変更により、ユーザーはインデクサの権限と機能に関する理解を深めることができ、特にインデクサの設定や運用において重要な考慮事項を把握しやすくなります。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Connect Using Azure Roles
 description: Learn how to assign Azure roles in Azure AI Search to manage permissions for service administration, development, and query access with Microsoft Entra ID.
-ms.date: 01/20/2026
+ms.date: 03/26/2026
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: how-to
@@ -93,7 +93,7 @@ Combine these roles to get sufficient permissions for your use case.
 |Configure private connections |❌|❌|✅|✅|❌|
 |Configure network security |❌|❌|✅|✅|❌|
 
-<sup>1</sup> In the Azure portal, an Owner or Contributor can run the [**Import data** wizard](search-import-data-portal.md) that creates and loads indexes, even though they can't upload documents in other clients. The search service itself, not individual users, makes data connections in the wizard. The wizard has the `Microsoft.Search/searchServices/indexes/documents/*` permission necessary for completing this task.
+<sup>1</sup> An Owner or Contributor can run the [**Import data** wizard](search-import-data-portal.md) to create and load indexes, even though they can't upload documents in other clients. Similarly, [indexers](search-indexer-overview.md) can write to any index on the search service, regardless of per-index role assignments. In both cases, the search service (not the user) performs the data plane actions using its `Microsoft.Search/searchServices/indexes/documents/*` permissions.
 
 <sup>2</sup> Use elevated read for debugging queries that obtain results by using the identity of the called. For more information, see [Investigate incorrect query results](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results).
 
@@ -525,6 +525,18 @@ In PowerShell, use [New-AzRoleAssignment](/powershell/module/az.resources/new-az
        -Scope  "/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.Search/searchServices/<search-service>/indexes/<index-name>"
    ```
 
+### Per-index scope and indexer operations
+
+Per-index role assignments apply to direct API operations only, such as queries or document uploads from users or applications. Indexers aren't restricted by per-index permissions because they operate with service-level credentials.
+
+A user with the **Search Service Contributor** role can create indexers that write to any index on the search service, even indexes where that user has no per-index role assignment.
+
+For strict data isolation between indexes, consider these approaches:
+
++ Use separate search services for teams or users who require index-level isolation.
++ Assign **Search Service Contributor** only to administrators who manage indexers.
++ Use [document-level access control](search-document-level-access-overview.md) with security filters to restrict query results within a shared index.
+
 ## Create a custom role
 
 If [built-in roles](#built-in-roles-used-in-search) don't provide the right combination of permissions, you can create a [custom role](/azure/role-based-access-control/custom-roles) to support the operations you require.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure役割による接続に関するセクションの更新"
}
```

### Explanation
この変更は、「Azure役割による接続」に関するドキュメントの更新を示しています。主な更新点は、文書の日付が「2026年1月20日」から「2026年3月26日」に変更されたことに加え、重要な情報が新たに追加されています。

この更新では、所有者や貢献者がインポートデータウィザードを使用してインデックスを作成および読み込むことができる点が強調されています。また、インデクサについての新しいセクションが追加されており、インデクサはサービスレベルの資格情報を使用して動作するため、個別のインデックスに対する役割の割り当てに制限されないことが説明されています。さらに、インデックスレベルの隔離を実現するための推奨される戦略が提示されており、ユーザーやチームがインデックス間でのデータが混在しないようにするための対策が提案されています。

この変更は、Azure AI Searchを使用する際の権限管理における重要な考慮事項を明確にし、ユーザーにとって有益な情報を提供することを目的としています。


