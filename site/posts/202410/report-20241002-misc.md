---
date: '2024-10-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0a8084e...MicrosoftDocs:b0599a2
summary: 文書「デプロイメントの概要」と「プロジェクト作成ガイド」に関するマイナーな更新が行われました。主な変更点は、日付の更新や新しいリンクの追加、セクションのタイトル変更などです。また、特に「create-projects.md」には「Prerequisites」セクションが追加されており、プロジェクト作成の手順がより明確になっています。今回の更新は、Azure
  AI Studioのドキュメントを最新かつユーザーフレンドリーに保つことを目的としており、ユーザーが必要な情報に迅速にアクセスできるようにする重要な改良が含まれています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0a8084e...MicrosoftDocs:b0599a2){target="_blank"}

# ハイライト

文書「デプロイメントの概要」と「プロジェクト作成ガイド」に関するマイナーな更新が行われました。特に新しいリンクの追加や日付の更新、セクションのタイトル変更などが含まれています。

## 新機能

- 「create-projects.md」に「Prerequisites」セクションが追加。
- 新しいリンクが「deployments-overview.md」に追加。

## 破壊的変更

- なし。

## その他の更新

- メタデータの更新。
- タイトルやリンクの変更。
- プロジェクト作成手順の明確化。

# 詳細

この差分には、Azureのドキュメントを最新かつユーザーフレンドリーに保つための一連のマイナー更新が含まれています。それぞれの変更について詳しく見ていきましょう。

## デプロイメントの概要の更新

### 内容と変更理由
文書「deployments-overview.md」の更新は、以下の2つの主要な変更を含んでいます。

1. **メタデータの変更**: `ms.topic`が`conceptual`から`concept-article`に変更されました。この修正により、文書がどのような情報を提供しているのかをより正確に示すことができます。特に、読み手に対する文書の位置づけが明確になります。
   
2. **リンクの変更**: 
   - 削除されたリンク: `Azure AI Studio FAQ`
   - 追加されたリンク: `Model catalog and collections in Azure AI Studio`

これにより、読者はより最新かつ関連性の高い情報にアクセスできます。

## プロジェクト作成ガイドの更新

### 内容と変更理由
文書「create-projects.md」の更新は、次の点でユーザー体験を向上させます：

1. **日付の更新**: `ms.date`が最新の日付に更新されました（`2024年5月21日`から`2024年10月1日`）。これにより、文書の新鮮さと信頼性が保証されます。

2. **前提条件の追加**: 
   - 新規セクション「Prerequisites」において、AzureサブスクリプションやAzure AI Studioハブの日必要性について説明。これにより、ユーザーが何が必要かをあらかじめ理解し、スムーズにプロジェクトを開始できます。

3. **手順の明確化**: 
   - プロジェクト作成の手順やコードスニペットの説明がより詳細かつ明確になりました。特に、変数名や使用パラメータの説明が具体化されています。

4. **セクションのタイトル変更**:
   - `Project settings`が`View project settings`に変更され、より具体的なセクション名となりました。

5. **関連コンテンツのセクション名変更**:
   - `Next steps`が`Related content`に変更されました。この変更により、次に読むべき関連資料がより明確に提供されます。

## 通しての影響と意義

今回の更新は、Azure AI Studioのドキュメントがより分かりやすく、かつ最新の情報を提供することを目的としています。特に、手順の明確化やリンクの更新は、ユーザーが必要な情報に迅速にアクセスできるようにするための重要な改良です。これにより、Azure AI Studioを利用するユーザーの学習曲線が緩和され、実際の使用においても効率が向上するでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [deployments-overview.md](#item-d00d7c) | minor update | デプロイメントの概要の更新 | modified | 2 | 2 | 4 | 
| [create-projects.md](#item-cb10b3) | minor update | プロジェクト作成ガイドの更新 | modified | 20 | 17 | 37 | 


# Modified Contents
## articles/ai-studio/concepts/deployments-overview.md{#item-d00d7c}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-studio
 ms.custom:
   - ignite-2023
   - build-2024
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 5/21/2024
 ms.reviewer: fasantia
 ms.author: mopeakande
@@ -96,4 +96,4 @@ Optimizing LLMs requires a careful consideration of several factors, including o
 - [Deploy Azure OpenAI models with Azure AI Studio](../how-to/deploy-models-openai.md)
 - [Deploy Meta Llama 3.1 models with Azure AI Studio](../how-to/deploy-models-llama.md)
 - [Deploy large language models with Azure AI Studio](../how-to/deploy-models-open.md)
-- [Azure AI Studio FAQ](../faq.yml)
+- [Model catalog and collections in Azure AI Studio](../how-to/model-catalog-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントの概要の更新"
}
```

### Explanation
このコードの差分は、文書「deployments-overview.md」に対するマイナーな更新を示しています。具体的には、以下の変更が含まれています：

1. **メタデータの変更**: `ms.topic`の値が`conceptual`から`concept-article`に変更されました。これは、この文書の内容がより具体的に「概念に関する記事」であることを示しています。

2. **リンクの変更**: 文書内のリンクも更新されており、`Azure AI Studio FAQ`のリンクが削除され、代わりに`Model catalog and collections in Azure AI Studio`に関するリンクが追加されました。これにより、読者が最新の情報やリソースにアクセスしやすくなっています。

この変更により、文書の内容がより明確になり、読者に対する情報の提供が改善されました。

## articles/ai-studio/how-to/create-projects.md{#item-cb10b3}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 10/01/2024
 ms.reviewer: deeikele
 ms.author: sgilley
 author: sdgilley
@@ -21,6 +21,11 @@ This article describes how to create an Azure AI Studio project. A project is us
 
 Projects are hosted by an Azure AI Studio hub that provides enterprise-grade security and a collaborative environment. For more information about the projects and resources model, see [Azure AI Studio hubs](../concepts/ai-resources.md).
 
+## Prerequisites
+
+- An Azure subscription. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/).
+- An Azure AI Studio hub. If you don't have a hub, see [How to create and manage an Azure AI Studio hub](create-azure-ai-resource.md).
+
 ## Create a project
 
 Use the following tabs to select the method you plan to use to create a project:
@@ -37,18 +42,17 @@ Use the following tabs to select the method you plan to use to create a project:
 
     ```Python
     from azure.ai.ml.entities import Project
-
+    
     my_project_name = "myexampleproject"
-    my_location = "East US"
     my_display_name = "My Example Project"
-    hub_id = "" # Azure resource manager ID of the hub
-
-    my_project = Project(name=my_hub_name, 
-                    location=my_location,
+    hub_name = "myhubname" # Azure resource manager ID of the hub
+    hub_id=f"/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{hub_name}"
+    
+    my_project = Project(name=my_project_name, 
                     display_name=my_display_name,
-                    hub_id=created_hub.id)
-
-    created_project = ml_client.workspaces.begin_create(workspace=my_hub).result() 
+                    hub_id=hub_id)
+    
+    created_project = ml_client.workspaces.begin_create(workspace=my_project).result()
     ```
 
 # [Azure CLI](#tab/azurecli)
@@ -71,7 +75,7 @@ Use the following tabs to select the method you plan to use to create a project:
 
 ---
 
-## Project settings
+## View project settings
 
 # [Azure AI Studio](#tab/ai-studio)
 
@@ -92,7 +96,7 @@ Select **Manage in the Azure portal** to navigate to the project resources in th
 To manage or use the new project, include it in the `MLClient`:
 
 ```python
-ml_client = MLClient(workspace_name=my_project_name, resource_group_name=my_resource_group, subscription_id=my_subscription_id,credential=DefaultAzureCredential())
+ml_client = MLClient(workspace_name=my_project_name, resource_group_name=resource_group, subscription_id=subscription_id,credential=DefaultAzureCredential())
 ```
 
 # [Azure CLI](#tab/azurecli)
@@ -105,27 +109,26 @@ az ml workspace show --name {my_project_name} --resource-group {my_resource_grou
 
 ---
 
-## Project resource access
+## Access project resources
 
 Common configurations on the hub are shared with your project, including connections, compute instances, and network access, so you can start developing right away.
 
 In addition, a number of resources are only accessible by users in your project workspace:
 
 1. Components including datasets, flows, indexes, deployed model API endpoints (open and serverless).
-1. Connections created by you under 'project settings'.
+1. Connections created by you under 'project settings.'
 1. Azure Storage blob containers, and a fileshare for data upload within your project. Access storage using the following connections:
    
    | Data connection | Storage location | Purpose |
    | --- | --- | --- |
-   | workspaceblobstore | {project-GUID}-azureml-blobstore | Default container for data upload |
+   | workspaceblobstore | {project-GUID}-azureml-blobstore | Default container for data uploads |
    | workspaceartifactstore | {project-GUID}-azureml | Stores components and metadata for your project such as model weights |
    | workspacefilestore | {project-GUID}-code | Hosts files created on your compute and using prompt flow |
 
 > [!NOTE]
 > Storage connections are not created directly with the project when your storage account has public network access set to disabled. These are created instead when a first user accesses AI Studio over a private network connection. [Troubleshoot storage connections](troubleshoot-secure-connection-project.md#troubleshoot-missing-storage-connections)
 
-
-## Next steps
+## Related content
 
 - [Deploy an enterprise chat web app](../tutorials/deploy-chat-web-app.md)
 - [Learn more about Azure AI Studio](../what-is-ai-studio.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト作成ガイドの更新"
}
```

### Explanation
このコードの差分は、文書「create-projects.md」に対するマイナーな更新を示しています。変更点は以下の通りです：

1. **日付の更新**: `ms.date`が`2024年5月21日`から`2024年10月1日`に変更されており、文書が最新の情報に基づいていることを示しています。

2. **前提条件の追加**: 新しいセクション「Prerequisites」が追加され、AzureサブスクリプションやAzure AI Studioハブの必要性について説明されています。

3. **手順の明確化**: コードスニペット内の変数名や手順が改善され、特にプロジェクト作成の際に使用するパラメータの記述がわかりやすくなっています。

4. **セクションのタイトル変更**: `Project settings`というタイトルが`View project settings`に変更され、セクションの内容により適したタイトルとなっています。

5. **関連コンテンツのセクションへ名称変更**: `Next steps`セクションが`Related content`に変更され、今後読むべき関連資料へのリンクが提供されています。

これらの変更により、文書がより明確で、読者が必要な情報を簡単に見つけられるようになっています。


