---
date: '2024-10-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2061c5e...MicrosoftDocs:9578344
summary: 今回の変更は、AIスタジオのロールベースのアクセス制御（RBAC）に関するドキュメントの更新です。特に「Azure AI Developer」ロールの詳細説明が追加され、新しいロールの権限やカスタムロール作成手順が明確になりました。また、関連画像が追加され、ユーザーガイドが視覚的にわかりやすくなっています。この改訂により、AIスタジオのユーザーはロールマネジメントをより効率的に行えるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2061c5e...MicrosoftDocs:9578344){target="_blank"}

# ハイライト
今回の変更は、AIスタジオにおけるロールベースのアクセス制御（RBAC）に関するドキュメントの更新です。特に、「Azure AI Developer」ロールの詳細説明が追加されました。新しいロールの権限やカスタムロールの作成手順が明確になり、関連画像も追加され、ユーザーガイドが視覚的にわかりやすくなっています。

## 新機能
- AIスタジオのリソースユーザー追加に関する新しい画像の追加。
- ハブ概要におけるユーザー追加の手順を示す画像の追加。

## 互換性を損なう変更
- 特に記載なし。

## その他の更新
- RBACのドキュメントに「Azure AI Developer」ロールの権限に関する詳細が追加。
- カスタムロール作成手順やロールの割り当て手順の説明が強化された。

# インサイト
今回の更新により、AIスタジオユーザーはロールマネジメントをさらに効率良く行えるようになります。「Azure AI Developer」ロールの具体的な権限が文書に追加されたことで、ユーザーはどのような権限があるのかを明確に理解することができます。また、カスタムロールの作成手順が加わったことで、自社に最適化されたロール設定が行いやすくなります。加えて、関連する新しい画像の追加により、視覚的に理解しやすくなり、特に初心者やAIスタジオを初めて使用するユーザーにとって非常に有益です。このような視覚的な改善は、ドキュメンテーションの質を向上させ、ユーザーの体験を向上させる重要な要素となります。今回の変更は、ユーザーが自信を持ってRBACの設定を行えるようにするための一歩であり、企業のセキュリティや権限管理を効率化する役割を果たすでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [rbac-ai-studio.md](#item-c2a11a) | minor update | RBAC（ロールベースのアクセス制御）に関するアップデート | modified | 42 | 16 | 58 | 
| [add-resource-users.png](#item-3e8748) | new feature | リソースユーザーの追加に関する画像の追加 | added | 0 | 0 | 0 | 
| [hub-overview-add-user.png](#item-3e92b6) | new feature | ハブ概要のユーザー追加に関する画像の追加 | added | 0 | 0 | 0 | 


# Modified Contents
## articles/ai-studio/concepts/rbac-ai-studio.md{#item-c2a11a}

<details>
<summary>Diff</summary>
````diff
@@ -43,33 +43,36 @@ Here's a table of the built-in roles and their permissions for the hub:
 | Azure AI Inference Deployment Operator | Perform all actions required to create a resource deployment within a resource group. |
 | Reader |     Read only access to the hub. This role is automatically assigned to all project members within the hub. |
 
-
 The key difference between Contributor and Azure AI Developer is the ability to make new hubs. If you don't want users to make new hubs (due to quota, cost, or just managing how many hubs you have), assign the Azure AI Developer role.
 
 Only the Owner and Contributor roles allow you to make a hub. At this time, custom roles can't grant you permission to make hubs.
 
+### Azure AI Developer role
+
 The full set of permissions for the new "Azure AI Developer" role are as follows:
 
 ```json
 {
     "Permissions": [ 
         { 
-        "Actions": [ 
-    
-            "Microsoft.MachineLearningServices/workspaces/*/read", 
-            "Microsoft.MachineLearningServices/workspaces/*/action", 
-            "Microsoft.MachineLearningServices/workspaces/*/delete", 
-            "Microsoft.MachineLearningServices/workspaces/*/write" 
-        ], 
+        "Actions": [
+            "Microsoft.MachineLearningServices/workspaces/*/read",
+            "Microsoft.MachineLearningServices/workspaces/*/action",
+            "Microsoft.MachineLearningServices/workspaces/*/delete",
+            "Microsoft.MachineLearningServices/workspaces/*/write",
+            "Microsoft.MachineLearningServices/locations/*/read",
+            "Microsoft.Authorization/*/read",
+            "Microsoft.Resources/deployments/*"
+        ],
     
-        "NotActions": [ 
-            "Microsoft.MachineLearningServices/workspaces/delete", 
-            "Microsoft.MachineLearningServices/workspaces/write", 
-            "Microsoft.MachineLearningServices/workspaces/listKeys/action", 
-            "Microsoft.MachineLearningServices/workspaces/hubs/write", 
-            "Microsoft.MachineLearningServices/workspaces/hubs/delete", 
-            "Microsoft.MachineLearningServices/workspaces/featurestores/write", 
-            "Microsoft.MachineLearningServices/workspaces/featurestores/delete" 
+        "NotActions": [
+            "Microsoft.MachineLearningServices/workspaces/delete",
+            "Microsoft.MachineLearningServices/workspaces/write",
+            "Microsoft.MachineLearningServices/workspaces/listKeys/action",
+            "Microsoft.MachineLearningServices/workspaces/hubs/write",
+            "Microsoft.MachineLearningServices/workspaces/hubs/delete",
+            "Microsoft.MachineLearningServices/workspaces/featurestores/write",
+            "Microsoft.MachineLearningServices/workspaces/featurestores/delete"
         ], 
         "DataActions": [ 
             "Microsoft.CognitiveServices/accounts/OpenAI/*", 
@@ -83,6 +86,9 @@ The full set of permissions for the new "Azure AI Developer" role are as follows
     ] 
 }
 ```
+
+If the built-in Azure AI Developer role doesn't meet your needs, you can create a [custom role](#create-custom-roles).
+
 ## Default roles for projects 
 
 Projects in AI Studio have built-in roles that are available by default. 
@@ -197,6 +203,26 @@ The following JSON example defines a custom AI Studio developer role at the subs
 }
 ```
 
+For steps on creating a custom role, use one of the following articles:
+- [Azure portal](/azure/role-based-access-control/custom-roles-portal)
+- [Azure CLI](/azure/role-based-access-control/custom-roles-cli)
+- [Azure PowerShell](/azure/role-based-access-control/custom-roles-powershell)
+
+For more information on creating custom roles in general, visit the [Azure custom roles](/azure/role-based-access-control/custom-roles) article.
+
+## Assigning roles in AI Studio
+
+You can add users and assign roles directly from Azure AI Studio at either the hub or project level. From a hub or project overview page, select **New user** to add a user. 
+
+> [!NOTE]
+> You are limited to selecting built-in roles. If you need to assign custom roles, you must use the [Azure portal](/azure/role-based-access-control/role-assignments-portal), [Azure CLI](/azure/role-based-access-control/role-assignments-cli), or [Azure PowerShell](/azure/role-based-access-control/role-assignments-powershell).
+
+:::image type="content" source="../media/concepts/hub-overview-add-user.png" lightbox="../media/concepts/hub-overview-add-user.png" alt-text="Screenshot of the Azure AI Studio hub overview with the new user button highlighted.":::
+
+You are then prompted to enter the user information and select a built-in role.
+
+:::image type="content" source="../media/concepts/add-resource-users.png" lightbox="../media/concepts/add-resource-users.png" alt-text="Screenshot of the add users prompt with the role set to Azure AI Developer.":::
+
 ## Scenario: Use a customer-managed key
 
 When configuring a hub to use a customer-managed key (CMK), an Azure Key Vault is used to store the key. The user or service principal used to create the workspace must have owner or contributor access to the key vault.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBAC（ロールベースのアクセス制御）に関するアップデート"
}
```

### Explanation
この変更は、AIスタジオにおける「Azure AI Developer」ロールの詳細情報の追加を含む、RBAC（ロールベースのアクセス制御）に関するドキュメントの更新です。主に42行が追加され、16行が削除され、全体で58行の変更が行われました。新しいロールの権限に関する詳細やカスタムロールの作成手順が追加され、使い方が明確になっています。

具体的には、「Azure AI Developer」ロールが持つ権限の詳細が記載され、ユーザーがカスタムロールを作成するためのリンクや手順が追加されています。また、AIスタジオ内でユーザーを追加し、ロールを割り当てる手順についても説明が強化されました。この変更により、ユーザーは役割の管理をより効果的に行えるようになります。また、関連する画像の追加により、指示が視覚的にわかりやすくなっています。

## articles/ai-studio/media/concepts/add-resource-users.png{#item-3e8748}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "リソースユーザーの追加に関する画像の追加"
}
```

### Explanation
この変更は、AIスタジオにおいてリソースユーザーを追加する手順を説明するための新しい画像「add-resource-users.png」が追加されたことを示しています。この画像は、ユーザーがAIスタジオ内で新しいユーザーを追加する際のインターフェースを視覚的にサポートするものであり、ユーザーガイドの質を向上させる役割を果たします。

画像の追加により、ドキュメントの内容がより具体的で理解しやすくなり、ユーザーは実際の操作を容易に把握できるようになります。この更新によって、機能の利用方法を説明する際に、視覚的な手がかりが提供されるため、特に初心者にとって有益です。

## articles/ai-studio/media/concepts/hub-overview-add-user.png{#item-3e92b6}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ハブ概要のユーザー追加に関する画像の追加"
}
```

### Explanation
この変更は、AIスタジオにおけるハブの概要においてユーザーを追加する手順を示す新しい画像「hub-overview-add-user.png」が追加されたことを示しています。この画像は、ユーザーがAIスタジオ内でどのようにして新しいユーザーをハブに追加するかを視覚的に説明するもので、ドキュメントの内容を補完する重要な要素です。

新しい画像の追加により、ユーザーは操作手順をより理解しやすくなり、特に初心者や新規ユーザーにとっては、曖昧さを減らす手助けとなります。この視覚的なサポートにより、ユーザーが求める情報を効率的に得ることができ、全体的なユーザビリティが向上します。


