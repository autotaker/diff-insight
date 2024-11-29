---
date: '2024-11-29'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:744c16a...MicrosoftDocs:b20ad3b
summary: このドキュメントの更新では、Azure AI SearchにおけるMicrosoft Entra ID認証およびロールベースのアクセス制御（RBAC）の設定手順が明確化されました。接続手順がより理解しやすくなり、実行しやすくなっています。特に新機能として、接続手順が詳述され、役割の割り当て手順も強化されました。既存の情報に破壊的な変更はなく、エラー防止のための注意喚起が追加されています。この更新は、ユーザーエクスペリエンスの向上を目指し、特にセキュアな認証とアクセス管理が重要な環境での利用をサポートします。これにより、技術者だけでなく一般のビジネスユーザーにとってもAzure
  AI Searchの活用が容易になります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:744c16a...MicrosoftDocs:b20ad3b){target="_blank"}

# ハイライト
このドキュメントの更新では、Azure AI SearchにおけるMicrosoft Entra ID認証およびロールベースのアクセス制御（RBAC）の設定手順が明確化および詳細化されました。この変更により、接続手順がより理解しやすく、実行しやすくなります。

## 新機能
- 接続手順に関する説明が明確化され、ユーザーが実際に接続を行う際の手順が詳細に記述されました。

## 破壊的変更
- 特に破壊的な変更はなく、既存の情報がアップデートされ、補完されています。

## その他の更新
- ドキュメントの日付が更新されました。
- RBACに関連する役割の割り当て手順が詳しく記述され、エラー防止の注意喚起が追加されました。

# 洞察
Azure AI Searchの接続手順に関するこのドキュメントの更新は、ユーザーエクスペリエンスの向上を目指したものであり、特にセキュアな認証とアクセス管理の設定が重要である環境において役立つ内容です。

今回の更新では、Microsoft Entra IDを利用した認証プロセスが強化され、ユーザーがより安全かつ効率的にAzureのサービスにアクセスできるように設計されています。具体的には、RBACの役割がより明確化され、設定手順が詳しく解説されています。これにより、設定ミスを未然に防ぎ、ユーザーが抱えるリスクを軽減することができます。

手順の細部にわたる改善、特に取得すべき情報や具体的なコマンドの提示は、ユーザーにとって手厚いサポートとなります。このため、技術者だけでなく、クラウドサービスを利用するビジネスユーザーにとっても、より簡便にAzure AI Searchを活用することが可能になります。

さらに、役割割り当ての強調により、一度に必須の役割をまとめて設定可能とすることで、管理者の負担を減らし、運用のスムーズさを実現しています。このようなアップデートは、Azureの基盤を利用する業務が有するポテンシャルを最大限に引き出す手助けとなるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-rbac.md](#item-9d96c1) | minor update | RBACに基づくAzure AI Searchの接続手順の更新 | modified | 39 | 18 | 57 | 


# Modified Contents
## articles/search/search-get-started-rbac.md{#item-9d96c1}

<details>
<summary>Diff</summary>
````diff
@@ -7,14 +7,14 @@ ms.author: heidist
 ms.service: azure-ai-search
 
 ms.topic: quickstart
-ms.date: 11/26/2024
+ms.date: 11/28/2024
 ---
 
 # Quickstart: Connect without keys
 
-Configure Azure AI Search to use Microsoft Entra ID authentication and roles. Connect from your local system, running Jupyter notebooks, or using a REST client.
+Configure Azure AI Search to use Microsoft Entra ID authentication and role-based access control (RBAC). Connect from your local system using your personal identity, using Jupyter notebooks or a REST client to interact with your search service.
 
-If you stepped through other quickstarts that connect using API keys, this quickstart shows you how to switch to identity-based authentication so that you can avoid hard-coded API keys in your example code.
+If you stepped through other quickstarts that connect using API keys, this quickstart shows you how to switch to identity-based authentication so that you can avoid hard-coded keys in your example code.
 
 ## Prerequisites
 
@@ -24,43 +24,51 @@ If you stepped through other quickstarts that connect using API keys, this quick
 
 - A command line tool, such as the [Azure CLI](/cli/azure/install-azure-cli).
 
-## Step 1: Set up your Azure subscription and tenant
+## Step 1: Get your Azure subscription and tenant IDs
 
 This step is necessary if you have more than one subscription or tenant.
 
 1. Get the Azure subscription and tenant for your search service:
 
-   1. Sign into the Azure portal and navigate to your search service.
+   1. Sign into the [Azure portal](https://portal.azure.com) and navigate to your search service.
 
    1. Notice the subscription name and ID in **Overview** > **Essentials**.
 
-   1. Select the subscription name to view the parent management group (tenant ID).
+   1. Now select the subscription name to confirm the parent management group (tenant ID) on the next page.
 
       :::image type="content" source="media/search-get-started-rbac/select-subscription-name.png" lightbox="media/search-get-started-rbac/select-subscription-name.png" alt-text="Screenshot of the portal page providing the subscription name":::
 
-1. Identify the active Azure subscription and tenant on your local device:
+1. Switching to your local device and a command prompt, identify the active Azure subscription and tenant:
 
-   `az account show`
+   ```azurecli
+   az account show
+   ```
 
-1. Set your Azure subscription to the subscription and tenant:
+1. If the active subscription is different from the information obtained in the previous step, change the subscription ID. Next, sign in to Azure using the tenant ID also found in the previous step:
 
-   `az account set --subscription <your-subscription-id>`
+   ```azurecli
+    az account set --subscription <your-subscription-id>
 
-   `az login --tenant <your-tenant-id>`
+    az login --tenant <your-tenant-id>
+   ```
 
-1. Check your tenant ID:
+1. Verify your tenant ID:
 
-   `az account show --query tenantId --output tsv`
+   ```azurecli
+   az account show --query tenantId --output tsv
+   ```
 
-## Step 2: Configure Azure AI Search for Microsoft Entra ID authentication
+## Step 2: Configure Azure AI Search for RBAC
 
-1. Sign in to the Azure portal and navigate to your Azure AI Search service.
+1. Sign in to the [Azure portal](https://portal.azure.com) and navigate to your Azure AI Search service.
 
 1. Enable role-based access control (RBAC):
 
    1. Go to **Settings** > **Keys**.
 
-   1. Choose **Role-based control** or **Both** if you need time to transition clients to role-based access control1.
+   1. Choose **Role-based control** or **Both** if you need time to transition clients to role-based access control.
+
+      If you choose **Role-based control**, make sure that you assign yourself *all* roles named in the next instruction or you won't be able to complete tasks in the portal or through a  local client.
 
 1. Assign roles in the Azure portal:
 
@@ -70,10 +78,23 @@ This step is necessary if you have more than one subscription or tenant.
 
    1. Select **+ Add** > **Add role assignment**.
 
-   1. Choose a role (Search Service Contributor, Search Index Data Contributor, Search Index Data Reader) and assign it to your Microsoft Entra user or group identity. These three roles provide the full set of permissions for creating, loading, and querying objects on Azure AI Search. For more information, see [Connect using roles](search-security-rbac.md).
+   1. Choose a role (Search Service Contributor, Search Index Data Contributor, Search Index Data Reader) and assign it to your Microsoft Entra user or group identity.
+
+      Repeat for each role.
+
+      You need all three roles for creating, loading, and querying objects on Azure AI Search. For more information, see [Connect using roles](search-security-rbac.md).
+
+> [!TIP]
+> Later, if you get authentication failure errors, recheck the settings in this section. There could be policies at the subscription or resource group level that override any API settings you specify.
 
 ## Step 3: Connect from your local system
 
+If you haven't yet signed in to Azure:
+
+```azurecli
+az login
+```
+
 ### Using Python and Jupyter notebooks
 
 1. Install the Azure Identity and Azure Search libraries:
@@ -105,7 +126,7 @@ Several quickstarts and tutorials use a REST client, such as Visual Studio Code
 
 1. Get a personal identity token:
 
-   `az account get-access-token --resource https://<your-search-service-name>.search.windows.net`
+   `az account get-access-token --scope https://search.azure.com/.default`
 
 1. Extract the token from the output:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACに基づくAzure AI Searchの接続手順の更新"
}
```

### Explanation
今回の変更では、Azure AI SearchにおけるMicrosoft Entra ID認証およびロールベースのアクセス制御（RBAC）の設定手順が更新されました。主な変更点は以下のとおりです：

1. **日付の更新**: ドキュメントの日付が「2024年11月26日」から「2024年11月28日」に変更されました。
   
2. **内容の明確化**: 接続の説明において、「役割」から「ロールベースのアクセス制御」へと用語が変更され、さらに手順や説明が具体的に説明されています。例えば、JupyterノートブックやRESTクライアントを使用する際の接続方法が詳細化されました。

3. **手順の番号付けと説明の強化**: 手順が整理され、AzureサブスクリプションとテナントIDの取得や設定におけるコマンドの形式が具体的に示され、ユーザーが操作しやすくなるように配慮されています。また、エラーや設定についての注意喚起が新たに追加されました。

4. **役割の割り当て**: RBACに関連する役割の割り当て手順が明確にされ、すべての必要な役割を一度に割り当てる方法が強調されています。

これらの変更により、ユーザーは新しい手順に従ってAzure AI Searchをより効果的に接続し、設定できるようになります。


