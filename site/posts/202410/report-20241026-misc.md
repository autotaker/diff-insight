---
date: '2024-10-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:edd8070...MicrosoftDocs:0bc728f
summary: この報告書では、Azure AI Studioに関する新しい機能と更新について述べています。新たに、「組み込みポリシー」と「カスタムポリシー」に関するドキュメントが追加され、ユーザーがAIモデルのデプロイメントをAzureポリシーを通じて制御できるようになりました。破壊的な変更は特に報告されていません。また、AI
  Studioの目次に「Azureポリシー」セクションが追加され、関連するガイドへのリンクも提供されています。これにより、ユーザーはモデルデプロイメントの管理がより簡潔になり、サービスの信頼性と効率が向上することが期待されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:edd8070...MicrosoftDocs:0bc728f){target="_blank"}

# Highlights

## New features
- Azure AI Studioにおけるモデルデプロイメントを制御するための「組み込みポリシー」と「カスタムポリシー」に関する新しいドキュメントが追加されました。これにより、ユーザーはAIモデルのデプロイメントをAzureポリシーの適用を通じて制御できます。

## Breaking changes
- 特に破壊的な変更は報告されていません。

## Other updates
- AI Studioの目次に「Azureポリシー」セクションが追加され、それに関連するガイドへのリンクが設けられました。

# Insights

このコードの変更は、Azure AI StudioでAIモデルのデプロイメントを管理するための新たなガイドラインを導入しています。新たに「組み込みポリシー」を用いてモデルデプロイメントを制御する方法のドキュメントが追加され、また「カスタムポリシー」を使用することによって、開発者が自分の組織の独自要件に合ったポリシーを定義し、適用できるようにしています。これにより、デプロイメントのプロセスが標準化されたフレームワークを通じて管理され、リスクの軽減と一貫性のある運用が可能になります。

組み込みポリシーガイドでは、Managed AI Services (MaaS) や Model-as-a-Platform (MaaP)においてポリシーの設定を通じてモデルの展開を管理する手法が述べられています。具体的には、Azureポータルを利用したポリシーの作成と割り当ての手順、コンプライアンスのモニタリング、そしてポリシーの更新と最良の手法について詳細に説明されています。

一方、カスタムポリシーは、固有のニーズに応じて独自のポリシー定義を作成し、適用するためのガイドラインを提供します。これによって、特定のビジネスニーズにマッチするポリシーを作成し、コンプライアンスの確認と管理が可能になり、特にデプロイメントが不適合となる場合の柔軟な管理や通知もサポートされます。

これらの新しい機能により、AI Studioユーザーはモデルデプロイメントのより厳格な制御と管理を行えるようになり、結果的にサービスの信頼性と効率が向上することが期待されます。加えて、目次にAzureポリシーのセクションを新設することで、ユーザーは関連リソースへのアクセスを簡素化し、必要な知識を容易に取得できるようになります。これによって、AI Studio内での学習と運用の一貫性を高めています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [built-in-policy-model-deployment.md](#item-5d38b0) | new feature | Azure AI Studioにおける組み込みポリシーを使用したモデルデプロイメントの制御 | added | 88 | 0 | 88 | 
| [custom-policy-model-deployment.md](#item-1ea809) | new feature | カスタムポリシーを使用したAIモデルデプロイメントの制御 | added | 128 | 0 | 128 | 
| [toc.yml](#item-2745cd) | minor update | AI Studioの目次にAzureポリシーセクションを追加 | modified | 6 | 0 | 6 | 


# Modified Contents
## articles/ai-studio/how-to/built-in-policy-model-deployment.md{#item-5d38b0}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,88 @@
+---
+title: Control AI model deployment with built-in policies
+titleSuffix: Azure AI Studio
+description: "Learn how to use built-in Azure policies to control what managed AI Services (MaaS) and Model-as-a-Platform (MaaP) AI models can be deployed in Azure AI Studio."
+author: Blackmist
+ms.author: larryfr
+ms.service: azure-ai-studio
+ms.topic: how-to #Don't change
+ms.date: 10/25/2024
+
+#customer intent: As an admin, I want control what Managed AI Services (MaaS) and Model-as-a-Platform (MaaP) AI models can be deployed by my developers.
+
+---
+
+# Control AI model deployment with built-in policies in Azure AI Studio
+
+Azure Policy provides built-in policy definitions that help you govern the deployment of AI models in Managed AI Services (MaaS) and Model-as-a-Platform (MaaP). You can use these policies to control what models your developers can deploy in Azure AI Studio.
+
+## Prerequisites
+
+- An Azure subscription. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/) before you begin.
+- Permissions to create and assign policies. To create and assign policies, you must be an [Owner](/azure/role-based-access-control/built-in-roles#owner) or [Resource Policy Contributor](/azure/role-based-access-control/built-in-roles#resource-policy-contributor) at the Azure subscription or resource group level.
+- Familiarity with Azure Policy. To learn more, see [What is Azure Policy?](/azure/governance/policy/overview).
+
+## Enable the policy
+
+1. From the [Azure portal](https://portal.azure.com), select **Policy** from the left side of the page. You can also search for **Policy** in the search bar at the top of the page.
+1. From the left side of the Azure Policy Dashboard, select **Authoring**, **Definition**, and then search for "[Preview]: Azure Machine Learning Deployments should only use approved Registry Models" in the search bar within the page. You can also directly navigate to [policy definition creation page](https://portal.azure.com/#blade/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F12e5dd16-d201-47ff-849b-8454061c293d).
+1. Select on **Assign** to assign the policy to the management group:
+
+    - **Scope**: Select the scope where you want to assign the policy. The scope can be a management group, subscription, or resource group.
+    - **Policy definition**: this section should already have a value of "**[Preview]: Azure Machine Learning Deployments should only use approved Registry Models**".
+    - **Assignment name**: Enter a unique name for the assignment.
+
+    The rest of the fields can be left as their default values or you can customize as needed for your organization.
+
+1. Select **Next** at the bottom of the page or the **Parameters** tab at the top of the page.
+1. In the **Parameters** tab, deselect **Only show parameters that needs input or review** to see all fields:
+
+    - **Effect**: Set to [**Deny**](/azure/governance/policy/concepts/effect-deny).
+        > [!NOTE]
+        > Using the [audit](/azure/governance/policy/concepts/effect-audit) option allows you to configure the policy to log information to your own compliance dashboard.
+    - **Allowed Models Publishers**: This field expects a list of **publisher's name** in quotation and separated by commas.
+    - **Allowed Asset Ids**: This field expects a list of **model asset ids** in quotation and separated by commas.
+
+        To get the model asset ID strings and model publishers' name use the following steps:
+
+        1. Go to the [Azure AI Studio model catalog](model-catalog-overview.md).
+
+
+        1. For each model you want to allow, select the model to view the details. In the model detail information, copy the **Model ID** value. For example, the value might look like `azureml://registries/azure-openai/models/gpt-35-turbo/versions/3` for GPT-3.5-Turbo model. The provided names are also *Collections* in model catalog. For example, the publisher for "Meta-Llama-3.1-70B-Instruct" model is Meta. 
+        
+            > [!IMPORTANT]
+            > The model ID value must be an exact match for the model. If the model ID is not an exact match, the model won't be allowed.
+
+
+1. Select **Review + create** tab and verify that the policy assignment is correct. When ready, select **Create** to assign the policy.
+1. Notify your developers that the policy is in place. They receive an error message if they try to deploy a model that isn't in the list of allowed models.
+
+## Monitor compliance
+
+To monitor compliance with the policy, follow these steps:
+
+1. From the [Azure portal](https://portal.azure.com), select **Policy** from the left side of the page. You can also search for **Policy** in the search bar at the top of the page.
+1. From the left side of the Azure Policy Dashboard, select **Compliance**. Each policy assignment is listed with the compliance status. To view more details, select the policy assignment.
+
+## Update the policy assignment
+
+To update an existing policy assignment with new models, follow these steps:
+
+1. From the [Azure portal](https://portal.azure.com), select **Policy** from the left side of the page. You can also search for **Policy** in the search bar at the top of the page.
+1. From the left side of the Azure Policy Dashboard, select **Assignments** and find the existing policy assignment. Select the ellipsis (...) next to the assignment and select **Edit assignment**.
+1. From the **Parameters** tab, update the **Allowed models** parameter with the new model IDs.
+1. From the **Review + Save** tab, select **Save** to update the policy assignment.
+
+## Best practices
+
+- **Granular scoping**: Assign policies at the appropriate scope to balance control and flexibility. For example, apply at the subscription level to control all resources in the subscription, or apply at the resource group level to control resources in a specific group.
+- **Policy naming**: Use a consistent naming convention for policy assignments to make it easier to identify the purpose of the policy. Include information such as the purpose and scope in the name.
+- **Documentation**: Keep records of policy assignments and configurations for auditing purposes. Document any changes made to the policy over time.
+- **Regular reviews**: Periodically review policy assignments to ensure they align with your organization's requirements.
+- **Testing**: Test policies in a nonproduction environment before applying them to production resources.
+- **Communication**: Make sure developers are aware of the policies in place and understand the implications for their work.
+
+## Related content
+
+- [Azure Policy overview](/azure/governance/policy/overview)
+- [Azure AI Studio model catalog](model-catalog-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Studioにおける組み込みポリシーを使用したモデルデプロイメントの制御"
}
```

### Explanation
この変更は、Azure AI Studioでのモデルデプロイメントを制御するための新しいガイドラインを追加するものです。新たに追加されたドキュメントは、「組み込みポリシーを使用したAIモデルデプロイメントの制御」というタイトルを持ち、ユーザーがManaged AI Services (MaaS)やModel-as-a-Platform (MaaP)において、開発者が展開可能なAIモデルを管理できるようにする方法を説明しています。

ガイドは、Azure Policyを利用し、これらのポリシーを適用することで、どのモデルがデプロイメントの対象となるかを制御できることを強調しています。具体的な手順には、Azureポータルでのポリシーの作成および割り当て方法、コンプライアンスの監視、ポリシーの更新、ベストプラクティスなどが含まれています。

このドキュメントは、チュートリアル形式で構成されており、前提条件、ポリシーの有効化、コンプライアンスの監視、ポリシーの更新や管理に関する実践的な手順を提供しています。これにより、管理者はAIモデルのデプロイメントに関するリスクを低減し、組織内での一貫性を確保することが可能になります。

## articles/ai-studio/how-to/custom-policy-model-deployment.md{#item-1ea809}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,128 @@
+---
+title: Control AI model deployment with custom policies
+titleSuffix: Azure AI Studio
+description: "Learn how to use custom Azure Policies to control Azure AI services and Azure OpenAI model deployment with Azure AI Studio."
+author: Blackmist
+ms.author: larryfr
+ms.service: azure-ai-studio
+ms.topic: how-to #Don't change
+ms.date: 10/25/2024
+
+#customer intent: As an admin, I want control what Azure AI services and Azure OpenAI models can be deployed by my developers.
+
+---
+
+# Control AI model deployment with custom policies in Azure AI Studio
+
+When using models from Azure AI services and Azure OpenAI with Azure AI Studio, you might need to use custom policies to control what models your developers can deploy. Custom Azure Policies allow you to create policy definitions that meet your organization's unique requirements. This article shows you how to create and assign an example custom policy to control model deployment.
+
+## Prerequisites
+
+- An Azure subscription. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/) before you begin.
+- Permissions to create and assign policies. To create and assign policies, you must be an [Owner](/azure/role-based-access-control/built-in-roles#owner) or [Resource Policy Contributor](/azure/role-based-access-control/built-in-roles#resource-policy-contributor) at the Azure subscription or resource group level.
+- Familiarity with Azure Policy. To learn more, see [What is Azure Policy?](/azure/governance/policy/overview).
+
+## Create a custom policy
+
+1. From the [Azure portal](https://portal.azure.com), select **Policy** from the left side of the page. You can also search for **Policy** in the search bar at the top of the page.
+1. From the left side of the Azure Policy Dashboard, select **Authoring**, **Definitions**, and then select **+ Policy definition** from the top of the page.
+1. In the **Policy Definition** form, use the following values:
+
+    - **Definition location**: Select the subscription or management group where you want to store the policy definition.
+    - **Name**: Enter a unique name for the policy definition. For example, `Custom allowed Azure AI services and Azure OpenAI models`.
+    - **Description**: Enter a description for the policy definition.
+    - **Category**: You can either create a new category or use an existing one. For example, "AI model governance."
+    - **Policy rule**: Enter the policy rule in JSON format. The following example shows a policy rule that allows the deployment of specific Azure AI services and Azure OpenAI models:
+
+        > [!TIP]
+        > Azure AI services was originally named Azure Cognitive Services. This name is still used internally by Azure, such as this custom policy where you see a value of `Microsoft.CognitiveServices`. Azure OpenAI is part of Azure AI services, so this policy also applies to Azure OpenAI models.
+
+        ```json
+        {
+              "mode": "All",
+              "policyRule": {
+                "if": {
+                  "allOf": [
+                    {
+                      "field": "type",
+                      "equals": "Microsoft.CognitiveServices/accounts/deployments"
+                    },
+                    {
+                      "not": {
+                        "value": "[concat(field('Microsoft.CognitiveServices/accounts/deployments/model.name'), ',', field('Microsoft.CognitiveServices/accounts/deployments/model.version'))]",
+                        "in": "[parameters('allowedModels')]"
+                      }
+                    }
+                  ]
+                },
+                "then": {
+                  "effect": "deny"
+                }
+              },
+              "parameters": {
+                "allowedModels": {
+                  "type": "Array",
+                  "metadata": {
+                    "displayName": "Allowed AI models",
+                    "description": "The list of allowed models to be deployed."
+                  }
+                }
+              }
+        }
+        ```
+
+1. Select **Save** to save the policy definition. After saving, you arrive at the policy definition's overview page.
+1. From the policy definition's overview page, select **Assign policy** to assign the policy definition.
+1. From the **Assign policy** page, use the following values on the **Basics** tab:
+
+    - **Scope**: Select the scope where you want to assign the policy. The scope can be a management group, subscription, or resource group.
+    - **Policy definition**: This field is prepopulated with the title of policy definition you created previously.
+    - **Assignment name**: Enter a unique name for the assignment.
+    - **Policy enforcement**: Make sure that the **Policy enforcement** field is set to **Enabled**. If it isn't enabled, the policy isn't enforced.
+
+    Select **Next** at the bottom of the page, or the **Parameters** tab at the top of the page.
+1. From the **Parameters** tab, set **Allowed AI models** to the list of models that you want to allow. The list should be a comma-separated list of model names and approved versions, surrounded by square brackets. For example, `["gpt-4,0613", "gpt-35-turbo,0613"]`.
+
+    > [!TIP]
+    > You can find the model names and their versions in the [Azure AI Studio Model Catalog](https://ai.azure.com/explore/models). Select the model to view the details, and then copy the model name and their version in the title.
+
+1. Optionally, select the **Non-compliance messages** tab at the top of the page and set a custom message for noncompliance.
+1. Select **Review + create** tab and verify that the policy assignment is correct. When ready, select **Create** to assign the policy.
+1. Notify your developers that the policy is in place. They receive an error message if they try to deploy a model that isn't in the list of allowed models.
+
+## Verify policy assignment
+
+To verify that the policy is assigned, navigate to **Policy** in the Azure portal, and then select **Assignments** under **Authoring**. You should see the policy listed.
+
+## Monitor compliance
+
+To monitor compliance with the policy, follow these steps:
+
+1. From the [Azure portal](https://portal.azure.com), select **Policy** from the left side of the page. You can also search for **Policy** in the search bar at the top of the page.
+1. From the left side of the Azure Policy Dashboard, select **Compliance**. Each policy assignment is listed with the compliance status. To view more details, select the policy assignment.
+
+## Update the policy assignment
+
+To update an existing policy assignment with new models, follow these steps:
+
+1. From the [Azure portal](https://portal.azure.com), select **Policy** from the left side of the page. You can also search for **Policy** in the search bar at the top of the page.
+1. From the left side of the Azure Policy Dashboard, select **Assignments** and find the existing policy assignment. Select the ellipsis (...) next to the assignment and select **Edit assignment**.
+1. From the **Parameters** tab, update the **Allowed models** parameter with the new models.
+1. From the **Review + Save** tab, select **Save** to update the policy assignment.
+
+## Best practices
+
+- **Obtaining model names**: Use the [Azure AI Studio Model Catalog](https://ai.azure.com/explore/models), then select the model to view details. Use the model name in the title with the policy.
+- **Granular scoping**: Assign policies at the appropriate scope to balance control and flexibility. For example, apply at the subscription level to control all resources in the subscription, or apply at the resource group level to control resources in a specific group.
+- **Policy naming**: Use a consistent naming convention for policy assignments to make it easier to identify the purpose of the policy. Include information such as the purpose and scope in the name.
+- **Documentation**: Keep records of policy assignments and configurations for auditing purposes. Document any changes made to the policy over time.
+- **Regular reviews**: Periodically review policy assignments to ensure they align with your organization's requirements.
+- **Testing**: Test policies in a nonproduction environment before applying them to production resources.
+- **Communication**: Make sure developers are aware of the policies in place and understand the implications for their work.
+
+## Related content
+
+- [Azure Policy overview](/azure/governance/policy/overview)
+- [Azure AI Studio model catalog](model-catalog-overview.md)
+- [Azure AI services documentation](/azure/ai-services)
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "カスタムポリシーを使用したAIモデルデプロイメントの制御"
}
```

### Explanation
この変更では、Azure AI Studioにおいてカスタムポリシーを使用してAIモデルのデプロイメントを制御する方法を説明する新しいガイドラインが追加されました。この文書では、開発者が展開できるモデルを管理するためのカスタムAzureポリシーの作成および割り当ての手順が具体的に説明されています。

ガイドは、カスタムポリシーを使用して独自の要件に基づいたポリシー定義を作成する方法を示しており、Azureポータルを通じての操作手順が詳しく記載されています。主な内容には、ポリシーの作成、割り当て、コンプライアンスの監視、ポリシーの更新に関する手順が含まれています。

また、ポリシーを適用する際の最適なプラクティスや、ポリシーの確認方法、デプロイメントに不適合な場合のメッセージ設定についても触れ、組織のニーズに応じた柔軟な管理ができることを強調しています。この新しいガイドにより、管理者はAzure AIサービスやAzure OpenAIモデルの選択的なデプロイメントをより厳密に制御できるようになります。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -341,6 +341,12 @@ items:
       href: concepts/encryption-keys-portal.md
     - name: Rotate keys
       href: ../ai-services/rotate-keys.md?context=/azure/ai-studio/context/context
+  - name: Azure policies
+    items:
+    - name: Built-in policy to allow specific models
+      href: how-to/built-in-policy-model-deployment.md
+    - name: Custom policy to allow specific models
+      href: how-to/custom-policy-model-deployment.md
   - name: Vulnerability management
     href: concepts/vulnerability-management.md
   - name: Disaster recovery
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Studioの目次にAzureポリシーセクションを追加"
}
```

### Explanation
この変更は、AI Studioに関する目次ファイル（toc.yml）に新しいセクションを追加するもので、特に「Azureポリシー」というカテゴリが新設されました。この新しいセクションには、次の2つの項目が含まれています。

1. **特定のモデルを許可する組み込みポリシー**に関するガイドへのリンク
2. **特定のモデルを許可するカスタムポリシー**に関するガイドへのリンク

これにより、ユーザーはAIモデルのデプロイメントに関するポリシーの情報を簡単に見つけられるようになります。この更新は、AI Studioのユーザーがモデルの展開におけるポリシーの重要性を理解し、効果的に管理するためのリソースへのアクセスを向上させることを目的としています。目次の変更は、全体の構成をより一貫性のあるものにし、関連する資料を整理する役割を果たしています。


