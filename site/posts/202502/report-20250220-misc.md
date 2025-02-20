---
date: '2025-02-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f9aa01e...MicrosoftDocs:11dfa93
summary: このコード変更では、個人識別情報の新しいエンティティの追加、AIスタジオ関連のドキュメント更新、AI管理者ロールの導入が行われました。また、AIサービスに関する文書の削除が含まれています。これにより、ユーザー体験が向上しつつ、法的要件への対応も強化されました。しかし、文書削除により情報探査が不便になる可能性もあります。全体として、地域ごとの要件に応じたサービスの拡張を目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f9aa01e...MicrosoftDocs:11dfa93){target="_blank"}

<format>
# Highlights
このコード変更において、個人識別情報の新しいエンティティの追加やAIスタジオ関連のドキュメントの更新、AI管理者ロールの導入といった重要な修正が行われました。また、AIサービスに関する文書の削除といったbreaking changeも含まれています。

## New features
- 「JPResidentRegistrationNumber」として日本の居住者登録番号エンティティを追加。
- 新たに「Azure AI Administrator」ロールが導入され、RBACドキュメントで詳述。
- 「Stability AIモデルのデプロイ方法」という新しい文書が追加され、モデルの展開手順や詳細が記載。

## Breaking changes
- 「AIサービスに関する説明」文書が完全に削除され、36行の内容がなくなりました。これにより、以前の情報が利用できなくなる可能性があります。

## Other updates
- 多数のドキュメントの日付を更新し、最新情報に対応。
- 「Stability AIモデルの地域可用性情報」など、マイナーな情報追加や修正。

# Insights
このコードの変更は、いくつかの異なる目的を達成しようとしています。まず、個人識別情報エンティティの更新は、国ごとの法的要件への適応を示しており、データプライバシーの管理を強化する目的があります。特に日本の居住者登録番号をサポートする機能強化により、地域ユーザーに対するサービスの有用性が向上することでしょう。

AIスタジオにおける新しい「Azure AI Administrator」ロールの導入は、役割ベースのアクセス制御をより詳細に管理できるようにするための重要なステップです。このアップデートにより、ユーザーはより柔軟かつ細かくアクセス権限を設定でき、セキュリティおよびオペレーションの効率が向上します。

さらに、新しく追加された「Stability AIモデルのデプロイ方法」に関するドキュメントは、モデルをサーバーレスAPIとして活用するための具体的な手引きを提供しており、技術チームがAIモデルを迅速に統合・展開するのに役立ちます。これにより、ビジネス要件に応じてスケーラブルなAIソリューションを作成するための基盤が整います。

一方で、「AIサービスに関する説明」文書の削除は、ユーザーにとって情報探査において不便をもたらす可能性があります。別の新しいドキュメントに移行しているかどうかの情報は示されておらず、この点に関してはユーザーに影響を及ぼすかもしれません。

全体的に、これらの更新はAIサービスの提供を拡張し、地域ごとの法規制や管理体制に対応したものとなっています。使用するユーザーにとって馴染みやすさを維持しつつ、新しい機能性を追加することで、強化されたユーザー体験の提供を目指しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [identification-entities.md](#item-9bf762) | minor update | 個人識別情報のエンティティの更新 | modified | 1 | 1 | 2 | 
| [ai-resources.md](#item-14adb9) | minor update | AIリソースに関する日付及び注意事項の更新 | modified | 2 | 2 | 4 | 
| [rbac-ai-studio.md](#item-c2a11a) | new feature | Azure AI Administrator ロールの追加と役割の説明 | modified | 116 | 1 | 117 | 
| [what-are-ai-services.md](#item-addaca) | breaking change | AIサービスに関する文書の削除 | removed | 0 | 36 | 36 | 
| [built-in-policy-model-deployment.md](#item-5d38b0) | minor update | 日付の更新：ビルトインポリシーモデルデプロイメント | modified | 1 | 1 | 2 | 
| [costs-plan-manage.md](#item-6d5c73) | minor update | 日付の更新：コストの計画と管理 | modified | 1 | 1 | 2 | 
| [deploy-stability-models.md](#item-9fcddb) | new feature | Stability AIモデルのデプロイ方法 | added | 122 | 0 | 122 | 
| [quota.md](#item-39c866) | minor update | リソースのクォータ管理と増加 | modified | 3 | 2 | 5 | 
| [region-availability-maas.md](#item-35d79c) | minor update | Stability AIモデルの地域可用性情報追加 | modified | 6 | 0 | 6 | 
| [toc.yml](#item-2745cd) | minor update | Stability AIモデルの展開に関するセクション追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/ai-services/language-service/personally-identifiable-information/includes/identification-entities.md{#item-9bf762}

<details>
<summary>Diff</summary>
````diff
@@ -1328,7 +1328,7 @@ The following entities are grouped and listed by country/region:
     :::column-end:::
     :::column span="2":::
 
-        To get this entity category, add `ITValueAddedTaxNumber` to the `piiCategories` parameter. `ITValueAddedTaxNumber` will be returned in the API response if detected.
+        To get this entity category, add `JPResidentRegistrationNumber` to the `piiCategories` parameter. `JPResidentRegistrationNumber` will be returned in the API response if detected.
       
         Also returned with `domain=phi`.
     :::column-end:::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人識別情報のエンティティの更新"
}
```

### Explanation
このコードの変更は、個人識別情報（PII）に関連するエンティティの定義におけるマイナーな更新を示しています。具体的には、従来の「ITValueAddedTaxNumber」というエンティティに代わって、「JPResidentRegistrationNumber」が追加されました。この変更により、日本の居住者登録番号の情報がAPIレスポンスに正しく含まれるようになります。この更新は、データを処理する際の国固有の要件に対応するためになされました。

## articles/ai-studio/concepts/ai-resources.md{#item-14adb9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ai-learning-hub
   - ignite-2024
 ms.topic: conceptual
-ms.date: 11/19/2024
+ms.date: 02/19/2025
 ms.reviewer: deeikele
 ms.author: larryfr
 author: Blackmist
@@ -72,7 +72,7 @@ Projects also have specific settings that only hold for that project:
 | Prompt flow runtime | Prompt flow is a feature that can be used to generate, customize, or run a flow. To use prompt flow, you need to create a runtime on top of a compute instance. |
 
 > [!NOTE]
-> In Azure AI Foundry portal you can also manage language and notification settings that apply to all projects that you can access regardless of the hub or project.
+> In Azure AI Foundry portal, you can also manage language and notification settings that apply to all projects that you can access regardless of the hub or project.
 
 ## Azure AI services API access keys
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIリソースに関する日付及び注意事項の更新"
}
```

### Explanation
このコードの変更は、AIリソースに関する文書内のマイナーな更新を示しています。主な変更点は、ドキュメントの日付が「2024年11月19日」から「2025年2月19日」へと変更されたことです。この更新により、情報が最新のものに保たれるようになっています。また、注意事項のテキストにおいても、文の構成が軽微に修正され、より読みやすくなっています。この変更は、ユーザーがAzure AI Foundryポータルでの言語や通知設定を調整する方法に関する指示を明確にするためになされています。

## articles/ai-studio/concepts/rbac-ai-studio.md{#item-c2a11a}

<details>
<summary>Diff</summary>
````diff
@@ -39,7 +39,8 @@ Here's a table of the built-in roles and their permissions for the hub:
 | Role | Description | 
 | --- | --- |
 | Owner | Full access to the hub, including the ability to manage and create new hubs and assign permissions. This role is automatically assigned to the hub creator|
-| Contributor |    User has full access to the hub, including the ability to create new hubs, but isn't able to manage hub permissions on the existing resource. |
+| Contributor | User has full access to the hub, including the ability to create new hubs, but isn't able to manage hub permissions on the existing resource. |
+| Azure AI Administrator (preview) | This role is automatically assigned to the system-assigned managed identity for the hub. The Azure AI Administrator role has the minimum permissions needed for the managed identity to perform its tasks. For more information, see [Azure AI Administrator role preview](#azure-ai-administrator-role-preview). |
 | Azure AI Developer |     Perform all actions except create new hubs and manage the hub permissions. For example, users can create projects, compute, and connections. Users can assign permissions within their project. Users can interact with existing Azure AI resources such as Azure OpenAI, Azure AI Search, and Azure AI services. |
 | Azure AI Inference Deployment Operator | Perform all actions required to create a resource deployment within a resource group. |
 | Reader |     Read only access to the hub. This role is automatically assigned to all project members within the hub. |
@@ -48,6 +49,94 @@ The key difference between Contributor and Azure AI Developer is the ability to
 
 Only the Owner and Contributor roles allow you to make a hub. At this time, custom roles can't grant you permission to make hubs.
 
+### Azure AI Administrator role preview
+
+Prior to 11/19/2024, the system-assigned managed identity created for the hub was automatically assigned the __Contributor__ role for the resource group that contains the hub and projects. Hubs created after this date have the system-assigned managed identity assigned to the __Azure AI Administrator__ role. This role is more narrowly scoped to the minimum permissions needed for the managed identity to perform its tasks.
+
+The __Azure AI Administrator__ role is currently in public preview.
+
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
+
+The __Azure AI Administrator__ role has the following permissions:
+
+```json
+{
+    "permissions": [
+        {
+            "actions": [
+                "Microsoft.Authorization/*/read",
+                "Microsoft.CognitiveServices/*",
+                "Microsoft.ContainerRegistry/registries/*",
+                "Microsoft.DocumentDb/databaseAccounts/*",
+                "Microsoft.Features/features/read",
+                "Microsoft.Features/providers/features/read",
+                "Microsoft.Features/providers/features/register/action",
+                "Microsoft.Insights/alertRules/*",
+                "Microsoft.Insights/components/*",
+                "Microsoft.Insights/diagnosticSettings/*",
+                "Microsoft.Insights/generateLiveToken/read",
+                "Microsoft.Insights/logDefinitions/read",
+                "Microsoft.Insights/metricAlerts/*",
+                "Microsoft.Insights/metricdefinitions/read",
+                "Microsoft.Insights/metrics/read",
+                "Microsoft.Insights/scheduledqueryrules/*",
+                "Microsoft.Insights/topology/read",
+                "Microsoft.Insights/transactions/read",
+                "Microsoft.Insights/webtests/*",
+                "Microsoft.KeyVault/*",
+                "Microsoft.MachineLearningServices/workspaces/*",
+                "Microsoft.Network/virtualNetworks/subnets/joinViaServiceEndpoint/action",
+                "Microsoft.ResourceHealth/availabilityStatuses/read",
+                "Microsoft.Resources/deployments/*",
+                "Microsoft.Resources/deployments/operations/read",
+                "Microsoft.Resources/subscriptions/operationresults/read",
+                "Microsoft.Resources/subscriptions/read",
+                "Microsoft.Resources/subscriptions/resourcegroups/deployments/*",
+                "Microsoft.Resources/subscriptions/resourceGroups/read",
+                "Microsoft.Resources/subscriptions/resourceGroups/write",
+                "Microsoft.Storage/storageAccounts/*",
+                "Microsoft.Support/*",
+                "Microsoft.Search/searchServices/write",
+                "Microsoft.Search/searchServices/read",
+                "Microsoft.Search/searchServices/delete",
+                "Microsoft.Search/searchServices/indexes/*",
+                "Microsoft.DataFactory/factories/*"
+            ],
+            "notActions": [],
+            "dataActions": [],
+            "notDataActions": []
+        }
+    ]
+}
+```
+
+> [!TIP]
+> We recommend that you convert hubs created before 11/19/2024 to use the Azure AI Administrator role. The Azure AI Administrator role is more narrowly scoped than the previously used Contributor role and follows the principal of least privilege.
+
+You can convert hubs created before 11/19/2024 to use the new Azure AI Administrator role by using one of the following methods:
+
+- Azure REST API: Use a `PATCH` request to the Azure REST API for the workspace. The body of the request should set `{"properties":{"allowRoleAssignmeentOnRG":true}}`. The following example shows a `PATCH` request using `curl`. Replace `<your-subscription>`, `<resource-group-name>`, `<workspace-name>`, and `<YOUR-ACCESS-TOKEN>` with the values for your scenario. For more information on using REST APIs, visit the [Azure REST API documentation](/rest/api/azure/).
+
+    ```bash
+    curl -X PATCH https://management.azure.com/subscriptions/<your-subscription>/resourcegroups/<resource-group-name>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name>?api-version=2024-04-01-preview -H "Authorization:Bearer <YOUR-ACCESS-TOKEN>"
+    ```
+
+- Azure CLI: Use the `az ml workspace update` command with the `--allow-roleassignment-on-rg true` parameter. The following example updates a workspace named `myworkspace`. This command requires the Azure Machine Learning CLI extension version 2.27.0 or later.
+
+    ```azurecli
+    az ml workspace update --name myworkspace --allow-roleassignment-on-rg true
+    ```
+
+- Azure Python SDK: Set the `allow_roleassignment_on_rg` property of the Workspace object to `True` and then perform an update operation. The following example updates a workspace named `myworkspace`. This operation requires the Azure Machine Learning SDK version 1.17.0 or later.
+
+    ```python
+    ws = ml_client.workspaces.get(name="myworkspace")
+    ws.allow_roleassignment_on_rg = True
+    ws = ml_client.workspaces.begin_update(workspace=ws).result()
+    ```
+
+If you encounter problems with the Azure AI Administrator role, you can revert to the Contributor role as a troubleshooting step. For more information, see [Revert to the Contributor role](#revert-to-the-contributor-role).
+
 ### Azure AI Developer role
 
 The full set of permissions for the new "Azure AI Developer" role are as follows:
@@ -100,6 +189,7 @@ Here's a table of the built-in roles and their permissions for the project:
 | --- | --- |
 | Owner | Full access to the project, including the ability to assign permissions to project users. |
 | Contributor |    User has full access to the project but can't assign permissions to project users. |
+| Azure AI Administrator (preview) | This role is automatically assigned to the system-assigned managed identity for the hub. The Azure AI Administrator role has the minimum permissions needed for the managed identity to perform its tasks. For more information, see [Azure AI Administrator role preview](#azure-ai-administrator-role-preview). |
 | Azure AI Developer |     User can perform most actions, including create deployments, but can't assign permissions to project users. |
 | Azure AI Inference Deployment Operator | Perform all actions required to create a resource deployment within a resource group. |
 | Reader |     Read only access to the project. |
@@ -416,6 +506,31 @@ Assign the following roles to the user or service principal. The role you assign
 | Azure AI Search | Search Index Data Contributor | Required for indexing scenarios. |
 | Azure AI Search| Search Index Data Reader | Inference service queries the data from the index. Only used for inference scenarios. |
 
+### Revert to the Contributor role
+
+If you create a new hub and encounter errors with the new default role assignment of Azure AI Administrator for the managed identity, use the following steps to change the hub to the Contributor role:
+
+> [!IMPORTANT]
+> We don't recommend reverting a hub to the Contributor role unless you encounter problems. If reverting does solve the problems that you are encountering, please open a support incident with information on the problems that reverting solved so that we can invesitage further.
+>
+> If you would like to revert to the Contributor role as the _default_ for new hubs, open a [support request](https://ms.portal.azure.com/#view/Microsoft_Azure_Support/NewSupportRequestV3Blade) with your Azure subscription details and request that your subscription be changed to use the Contributor role as the default for the system-assigned managed identity of new hubs.
+
+1. Delete the role assignment for the hub's managed-identity. The scope for this role assignment is the __resource group__ that contains the hub, so the role must be deleted from the resource group. 
+
+    > [!TIP]
+    > The system-assigned managed identity for the hub is the same as the hub name.
+
+    From the Azure portal, navigate to the __resource group__ that contains the hub. Select __Access control (IAM)__, and then select __Role assignments__. In the list of role assignments, find the role assignment for the managed identity. Select it, and then select __Delete__.
+
+    For information on deleting a role assignment, see [Remove role assigngments](/azure/role-based-access-control/role-assignments-remove).
+
+1. Create a new role assignment on the __resource group__ for the __Contributor__ role. When adding this role assignment, select the managed-identity for the hub as the assignee. The name of the system-assigned managed identity is same as the hub name.
+
+    1. From the Azure portal, navigate to the __resource group__ that contains the hub. Select __Access control (IAM)__, and then select __Add role assignment__. 
+    1. From the __Role__ tab, select __Contributor__. 
+    1. From the __Members__ tab, select __Managed identity__, __+ Select members__, ans set the __Managed identity__ dropdown to __Azure AI hub__. In the __Select__ field, enter the name of the hub. Select the hub from the list, and then select __Select__.
+    1. From the __Review + assign__ tab, select __Review + assign__.
+
 ## Next steps
 
 - [How to create an Azure AI Foundry hub](../how-to/create-azure-ai-resource.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Administrator ロールの追加と役割の説明"
}
```

### Explanation
このコードの変更は、RBAC（ロールベースのアクセス制御）に関する文書において、新しい「Azure AI Administrator」ロールの導入と詳細な説明を含む大規模な更新を示しています。主な変更点は、既存のロールに新しい管理者ロールが追加されたことです。このロールは、システムに自動的に割り当てられ、最小限の権限を持つように設計されており、特にマネージドアイデンティティによるタスクの実行に必要な権限が付与されます。

さらに、以前の「Contributor」ロールとの違いが詳述されており、Azure AI Administratorロールには特定の操作に対する具体的な許可がJSON形式で示されていることが特徴です。加えて、既存のハブを新しいロールに移行する手順や、何か問題が発生した際にContributorロールに戻す際の手順も記載されています。この更新は、Azure AI Studioにおける役割と権限管理の明確化を目的としており、ユーザーがアクセス権限を効果的に管理できるように設計されています。

## articles/ai-studio/concepts/what-are-ai-services.md{#item-addaca}

<details>
<summary>Diff</summary>
````diff
@@ -1,36 +0,0 @@
----
-title: What are AI services?
-description: Learn about the various Azure AI services and their capabilities that you can use in Azure AI Foundry.
-author: sdgilley
-ms.author: sgilley
-ms.service: azure-ai-studio
-ms.topic: concept-article  
-ms.date: 1/30/2025
-
-#CustomerIntent: I want to understand what AI services are and how they can help me build AI solutions.
----
-
-# What are AI services?
-
-[Azure AI Foundry](../what-is-ai-studio.md) is a comprehensive platform for AI development that provides a wide range of tools and services to help you build AI solutions. You can explore the [model catalog](../how-to/model-catalog-overview.md) to find the right model for your use case. 
-
-[Azure AI services](../../ai-services/what-are-ai-services.md) are a collection of task and general purpose models in Azure AI Foundry. These services are designed to help you build AI solutions quickly and easily, without needing to build and train your own models from scratch. In some cases, you can customize these models to better fit your specific needs. 
-
-> [!TIP]
-> While some articles from each service are available in the [Azure AI Foundry documentation](../ai-services/how-to/connect-ai-services.md), explore each service in more depth in their individual service documentation.
-
-| Service | Description |
-| --- | --- |
-| ![Azure OpenAI Service icon](~/reusable-content/ce-skilling/azure/media/ai-services/azure-openai.svg) [Azure OpenAI](../../ai-services/openai/index.yml) | Perform a wide variety of natural language tasks. |
-| ![Content Safety icon](~/reusable-content/ce-skilling/azure/media/ai-services/content-safety.svg) [Content Safety](../../ai-services/content-safety/index.yml) | An AI service that detects unwanted contents. |
-| ![Content Understanding icon](~/reusable-content/ce-skilling/azure/media/ai-services/content-understanding.svg) [Content Understanding](../../ai-services/content-understanding/index.yml) | Analyze various media content—such as audio, video, text, and images— and transform it into structured, organized, and searchable data for your applications. |
-| ![Document Intelligence icon](~/reusable-content/ce-skilling/azure/media/ai-services/document-intelligence.svg) [Document Intelligence](../../ai-services/document-intelligence/index.yml) | Turn documents into intelligent data-driven solutions. |
-| ![Language icon](~/reusable-content/ce-skilling/azure/media/ai-services/language.svg) [Language](../../ai-services/language-service/index.yml) | Build apps with industry-leading natural language understanding capabilities. |
-| ![Speech icon](~/reusable-content/ce-skilling/azure/media/ai-services/speech.svg) [Speech](../../ai-services/speech-service/index.yml) | Speech to text, text to speech, translation, and speaker recognition. |
-| ![Translator icon](~/reusable-content/ce-skilling/azure/media/ai-services/translator.svg) [Translator](../../ai-services/translator/index.yml) | Use AI-powered translation technology to translate more than 100 in-use, at-risk, and endangered languages and dialects. |
-| ![Vision icon](~/reusable-content/ce-skilling/azure/media/ai-services/vision.svg) [Vision](../../ai-services/computer-vision/index.yml) | Analyze content in images and videos. | 
-
-## Related content
-
-- [Use Azure OpenAI Service in Azure AI Foundry portal](../ai-services/how-to/connect-azure-openai.md)
-- [Use Azure AI services in Azure AI Foundry portal](../ai-services/how-to/connect-ai-services.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "AIサービスに関する文書の削除"
}
```

### Explanation
この変更は、「AIサービスに関する説明」文書が完全に削除されたことを示しています。具体的には、AIサービスの定義、機能、関連するサービスのリストなど、合計36行の内容が削除されました。この文書は、Azure AI FoundryにおけるAIサービスの概要を説明するものであり、ユーザーが必要なAIモデルを見つけたり、サービスを利用してAIソリューションを構築する上での指針を提供していました。この削除は、AIサービスに関する情報を別の場所に移行するか、更新するために行われた可能性が考えられますが、具体的な理由はコードの変更には示されていません。ユーザーにとっては、AIサービスに関連する情報が提供されなくなるため、別のソースを探す必要があるかもしれません。

## articles/ai-studio/how-to/built-in-policy-model-deployment.md{#item-5d38b0}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: Blackmist
 ms.author: larryfr
 ms.service: azure-ai-foundry
 ms.topic: how-to #Don't change
-ms.date: 10/25/2024
+ms.date: 02/19/2025
 
 #customer intent: As an admin, I want control what Managed AI Services (MaaS) and Model-as-a-Platform (MaaP) AI models can be deployed by my developers.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新：ビルトインポリシーモデルデプロイメント"
}
```

### Explanation
この変更は、「ビルトインポリシーモデルデプロイメント」に関する文書の日付を更新したことを示しています。具体的には、文書の最終更新日が2024年10月25日から2025年2月19日に変更されました。この更新は、情報の鮮度を保つために行われたものであり、ユーザーにとって関連性のある最新の情報を提供することを目的としています。変更内容は1行の追加と1行の削除であり、内容のクリティカルな変更はなく、主に文書のメンテナンスに関するものです。このような日付更新は、ユーザーが最新のガイダンスや変更を把握する上で重要です。

## articles/ai-studio/how-to/costs-plan-manage.md{#item-6d5c73}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: conceptual
-ms.date: 11/19/2024
+ms.date: 02/19/2025
 ms.reviewer: siarora
 ms.author: larryfr
 author: Blackmist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新：コストの計画と管理"
}
```

### Explanation
この変更は、「コストの計画と管理」に関する文書の日付を更新したことを示しています。具体的には、文書の最終更新日が2024年11月19日から2025年2月19日に変更されました。このような日付更新は、文書が最新の情報を反映していることを保証するために行われており、ユーザーが常に正確かつ関連性の高い情報にアクセスできるようにします。変更内容は、追加と削除がそれぞれ1行ずつ行われたシンプルなものであり、内容自体に大きな変更は見られません。主に文書のメンテナンス的な目的に沿った更新です。

## articles/ai-studio/how-to/deploy-stability-models.md{#item-9fcddb}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,122 @@
+---
+title: How to deploy Stability AI family of models with AI Foundry
+titleSuffix: Azure AI Foundry
+description: How to deploy Stability AI family of models with AI Foundry
+manager: scottpolly
+ms.service: azure-machine-learning
+ms.topic: how-to
+ms.date: 01/23/2025
+ms.author: timanghn
+author: tinaem
+ms.reviewer: ssalgado
+reviewer: ssalgadodev
+ms.custom: references_regions
+---
+
+# How to deploy Stability AI family of models with AI Foundry
+
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
+
+In this article, you learn how to use Azure AI Foundry to deploy Stability AI collection of models as a serverless API with pay-as-you-go billing.
+
+The Stability AI collection of models include Stable Image Core, Stable Image Ultra and Stable Diffusion 3.5 Large. 
+
+### Stable Diffusion 3.5 Large
+
+At 8.1 billion parameters, with superior quality and prompt adherence, this base model is the most powerful in the Stable Diffusion family and is ideal for professional use cases at 1 megapixel resolution. 
+
+Stable Diffusion 3.5 large supports text and image prompt inputs for image generations. 
+
+### Stable Image Core
+
+Leveraging an enhanced version of SDXL, Stable Image Core, delivers exceptional speed and efficiency while maintaining the high-quality output synonymous with Stable Diffusion models.
+
+Stable Image Core supports text prompt inputs only for image generations.
+
+### Stable Image Ultra
+
+Powered by the advanced capabilities of Stable Diffusion 3.5 Large, Stable Image Ultra sets a new standard in photorealism. Stable Image Ultra is ideal for product imagery in marketing and advertising. It also excels in typography, dynamic lighting, and vibrant color rendering.
+
+Stable Image Ultra supports text prompt inputs only for image generations.
+
+[!INCLUDE [models-preview](../includes/models-preview.md)]
+
+
+## Deploy a Stability AI model as a serverless API
+
+Stability AI models in the model catalog can be deployed as a serverless API with pay-as-you-go billing, providing a way to consume them as an API without hosting them on your subscription, while keeping the enterprise security and compliance organizations need. This deployment option doesn't require quota from your subscription. 
+
+
+### Prerequisites
+
+To use Stability AI models with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to serverless APIs**
+
+Stability AI models can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Foundry portal, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
+### Consume Stability AI models as a serverless API
+
+1. In the **workspace**, select **Endpoints** > **Serverless endpoints**.
+1. Find and select the `Stable Diffusion 3.5 Large` deployment you created.
+1. Copy the **Target** URL and the **Key** token values.
+1. Make an API request based on the type of model you deployed. To see an example request, see the [reference section](#reference-for-stability-ai-models-deployed-as-a-serverless-api). 
+
+### Reference for Stability AI models deployed as a serverless API
+
+Stability AI models on Models as a Service implement the [Azure AI Model Inference API](../reference/reference-model-inference-api.md) on the route `/image/generations` 
+
+#### Request example 
+
+```
+{
+      "prompt": "A photo of a cat",
+      "negative_prompt": "A photo of a dog",
+      "image_prompt": {
+        "image": "puqkvvlvgcjyzughesnkena",
+        "strength": 1
+        },
+      "size": "1024x1024",
+      "output_format": "png",
+      "seed": 26
+}
+```
+
+#### Response
+
+```
+{
+    "image": "iVBORw0KGgoAAAANSUhEUgAABgA...",
+    "created": 1739161682
+}
+```
+
+Follow this link for a full encoded [image generation response](https://github.com/MicrosoftDocs/azure-ai-docs-pr/pull/2896/$0). 
+
+## Cost and quotas
+
+### Cost and quota considerations for Stability AI models deployed as a serverless API
+
+The Stability AI models are deployed as a serverless API and is offered by Stability AI through Azure Marketplace and integrated with AI Foundry for use. You can find Azure Marketplace pricing when deploying or fine-tuning models.
+
+Each time a workspace subscribes to a given model offering from Azure Marketplace, a new resource is created to track the costs associated with its consumption. The same resource is used to track costs associated with inference and fine-tuning; however, multiple meters are available to track each scenario independently.
+
+For more information on how to track costs, see [Monitor costs for models offered through the Azure Marketplace](./costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace).
+
+Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
+
+## Content filtering
+
+Models deployed as a serverless API are protected by Azure AI content safety. When deployed to managed compute, you can opt out of this capability. With Azure AI content safety enabled, both the prompt and completion pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions. Learn more about [Azure AI Content Safety](/azure/ai-services/content-safety/overview).
+
+## Related content
+
+- [Model Catalog and Collections](./model-catalog-overview.md)
+- [Plan and manage costs for Azure AI Foundry](./costs-plan-manage.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Stability AIモデルのデプロイ方法"
}
```

### Explanation
この変更は、「Stability AIモデルのデプロイ方法」という新しい文書を追加するものです。この文書では、Azure AI Foundryを使用してStability AIファミリーのモデルをサーバーレスAPIとして展開する方法について詳しく説明されています。文書には、各モデルの概要、サーバーレスAPIとしてのデプロイ手順、コストとクォータに関する考慮事項、コンテンツフィルタリング機能などの情報が含まれており、ユーザーがこれらのモデルを効率的に使用できるようにサポートします。

具体的には、Stable Diffusion 3.5 Large、Stable Image Core、Stable Image Ultraといったモデルについての情報も豊富に盛り込まれており、実際のAPIリクエストやレスポンスの例も提示されています。この新機能の追加により、ユーザーは新たなAIモデルの活用方法を学び、利用できるようになります。全体で122行の内容が追加されており、詳細なガイドとしての役割が期待されています。

## articles/ai-studio/how-to/quota.md{#item-39c866}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Manage and increase quotas for resources with Azure AI Foundry
+title: Manage and increase quotas for resources
 titleSuffix: Azure AI Foundry
 description: This article provides instructions on how to manage and increase quotas for resources with Azure AI Foundry.
 manager: scottpolly
@@ -9,10 +9,11 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 02/19/2025
 ms.reviewer: siarora
 ms.author: larryfr
 author: Blackmist
+# Customer intent: As an Azure AI Foundry user, I want to know how to manage and increase quotas for resources with Azure AI Foundry.
 ---
 
 # Manage and increase quotas for resources with Azure AI Foundry
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースのクォータ管理と増加"
}
```

### Explanation
この変更は「リソースのクォータ管理と増加」に関する文書のタイトルやメタデータを更新したものです。新しいタイトルは「リソースのクォータ管理と増加」となり、Azure AI Foundryに特有な部分が取り除かれましたが、文書の主なテーマはそのまま残されています。また、最終更新日が2024年11月19日から2025年2月19日に更新されています。

さらに、文書には新しく顧客の意図に関する説明が追加されており、「Azure AI Foundryユーザーとして、リソースのクォータを管理および増加する方法を知りたい」という情報が含まれています。これにより、ユーザーがこの文書を参照する目的がより明確になりました。全体として、この変更は情報の明確化と日付の更新を行うことを目的とした軽微な変更と言えます。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -105,3 +105,9 @@ AI21-Jamba-1.5-Large | [Microsoft Managed countries/regions](/partner-center/mar
 |Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
 Bria-2.3-Fast   | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  | East US 2   | Not available       |
+
+### Stability AI models
+
+|Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
+|---------|---------|---------|---------|
+Stable Diffusion 3.5 Large <br> Stable Image Core <br> Stable Image Ultra   | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3   | Not available       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Stability AIモデルの地域可用性情報追加"
}
```

### Explanation
この変更は、Stability AIモデルに関する地域可用性情報を追加したものです。具体的には、「Stability AI models」という新しいセクションが文書に追加され、Stable Diffusion 3.5 Large、Stable Image Core、Stable Image Ultraといったモデルの提供される地域に関する詳細が記載されています。

新しいテーブルには、モデルの名称、提供可用性地域、デプロイメントのためのハブ/プロジェクト地域、およびファインチューニングのためのハブ/プロジェクト地域が含まれています。提供可用性地域としては、Microsoft管理国のリストが参照され、デプロイメントのためのハブ地域には、East US、East US 2、North Central US、South Central US、West US、West US 3が挙げられています。

この更新により、ユーザーはStability AIモデルの地域別の可用性をより理解しやすくなるため、利用者の利便性が向上します。全体として、この変更はマイナーな更新ですが、重要な情報の補足が行われました。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -175,6 +175,8 @@ items:
       href: how-to/deploy-models-tsuzumi.md
     - name: Fine-tune tsuzumi model
       href: how-to/fine-tune-models-tsuzumi.md
+    - name: Stability AI models
+      href: ./how-to/deploy-stability-models.md
   - name: Deploy AI models
     items:
       - name: Deployments overview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Stability AIモデルの展開に関するセクション追加"
}
```

### Explanation
この変更は、AI Studioのテーブルオブコンテンツ（toc.yml）に「Stability AI models」というセクションを追加したものです。具体的には、Stability AIモデルに関する展開方法を説明する新しい文書へのリンクが追加されました。このリンクには、`how-to/deploy-stability-models.md`というパスが指定されています。

この更新により、ユーザーがStability AIモデルを展開するための情報をより簡単に見つけられるようになり、関連するリソースへのアクセスが向上します。全体として、この変更はコンテンツの明確さと可用性を高めるための軽微な更新です。


