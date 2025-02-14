---
date: '2025-02-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:81f79a9...MicrosoftDocs:f2b9798
summary: このコード変更では、いくつかの文書が更新され、主にデータ使用とファインチューニング、Azure Key Vaultに関する情報が改善されました。新機能として、Azure
  OpenAIのファインチューニングに「Provisioned Managed」という新しいデプロイメントタイプが追加されました。また、使用モデルに関する情報やAzure
  Key Vaultのリンクも更新され、ユーザーに対してより明確なガイダンスが提供されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:81f79a9...MicrosoftDocs:f2b9798){target="_blank"}


# Highlights
このコード変更では、いくつかの文書が更新され、主にデータ使用とファインチューニング、Azure Key Vault関連の情報が改善されています。新機能として、Azure OpenAIのファインチューニングに新しいデプロイメントタイプ「Provisioned Managed」が追加されました。また、使用モデルに関する情報とAzure Key Vaultのリンクも更新され、ユーザーにより明確なガイダンスを提供しています。

## New features
- ファインチューニングの「Provisioned Managed」デプロイメントタイプの追加。

## Breaking changes
特に記載なし。

## Other updates
- 日付情報の更新と使用できないモデルに関する情報の追加。
- Azure Key Vaultに関するリンクの変更。

# Insights
この記事では、Azure OpenAIの利用においてユーザーが直面する可能性のある課題に対する改善が行われています。主要な改善部分は以下の通りです：

まず、データ使用に関する文書では、日付情報が新たに更新され、最新の情報提供がされています。これにより、ユーザーはデータ使用に関する最新の方針や制限を知ることができ、より正確に製品を利用できるようになります。重要な追加情報として、Azure OpenAIで非対応であるモデル(o1モデルとo3モデル)が明示されており、データを使用する際に誤ったモデルを選択するリスクが減少します。

さらに、ファインチューニングに関する文書では、「Provisioned Managed」という新しいデプロイメントタイプが導入されました。これにより、ファインチューニングを実施する際の選択肢が増えるとともに、実際のAPI呼び出し方法も記載されています。これにより、ユーザーはより効率的にファインチューニングを行うための知識を得ることができます。

最後に、Azure Key Vaultのリンクがより適切な情報源に更新されました。新しいリンクはセキュリティとアクセス管理に関する最新情報を提供し、環境変数の設定とそのセキュリティを向上させる目的があります。これにより、ユーザーはAzure Key Vaultをより安全かつ効率的に利用できるようになり、全体的にAzure OpenAIのユーザー体験が改善されました。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [use-your-data.md](#item-455d6e) | minor update | データの使用に関する情報の更新 | modified | 6 | 1 | 7 | 
| [fine-tuning.md](#item-5c0e85) | minor update | ファインチューニングに関する情報の追加 | modified | 80 | 1 | 81 | 
| [environment-variables.md](#item-ee5a34) | minor update | Azure Key Vaultに関するリンクの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/use-your-data.md{#item-455d6e}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-openai
 ms.topic: quickstart
 author: aahill
 ms.author: aahi
-ms.date: 10/25/2024
+ms.date: 02/13/2025
 recommendations: false
 ms.custom: references_regions, ignite-2024
 ---
@@ -41,6 +41,11 @@ Typically, the development process you'd use with Azure OpenAI On Your Data is:
 
 To get started, [connect your data source](../use-your-data-quickstart.md) using Azure AI Foundry portal and start asking questions and chatting on your data.
 
+> [!NOTE]
+> The following models are not supported by Azure OpenAI On Your Data:
+> * o1 models
+> * o3 models
+
 ## Azure Role-based access controls (Azure RBAC) for adding data sources
 
 To use Azure OpenAI On Your Data fully, you need to set one or more Azure RBAC roles. See [Azure OpenAI On Your Data configuration](../how-to/on-your-data-configuration.md#role-assignments) for more information.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データの使用に関する情報の更新"
}
```

### Explanation
この変更は、文書「データの使用」に関するいくつかの重要な更新を行っています。最初に、日付情報が2024年10月25日から2025年2月13日へと変更されています。この更新は、文書の内容がより具体的で正確な情報を反映するために必要でした。

さらに、Azure OpenAIを使用してデータを扱う際に注意が必要な点を明確にするための新しい情報が追加されました。具体的には、以下のモデルがAzure OpenAIで使用するデータに対応していないことが記されています：
- o1モデル
- o3モデル

これにより、ユーザーは対応していないモデルを知ることで、適切なデータの使用方法を理解しやすくなります。この更新は、全体的なユーザー体験の向上を目的としており、より明確なガイダンスを提供することによって、Azure OpenAIを効果的に利用できるようにするものです。

## articles/ai-services/openai/how-to/fine-tuning.md{#item-5c0e85}

<details>
<summary>Diff</summary>
````diff
@@ -44,19 +44,98 @@ We use LoRA, or low rank approximation, to fine-tune models in a way that reduce
 
 ::: zone-end
 
-## Global Standard (preview)
+## Other Deployment Types
 
 Azure OpenAI fine-tuning supports [global standard deployments](./deployment-types.md#global-standard) in East US2, North Central US, and Sweden Central for:
 
 - `gpt-4o-mini-2024-07-18`
 - `gpt-4o-2024-08-06`
 
+And supports [regional provisioned managed](./deployment-types.md#provisioned) in North Central US and Switzerland West for:
+
+- `gpt-4o-mini-2024-07-18`
+- `gpt-4o-2024-08-06`
+
+### Global Standard (preview)
+
 Global standard fine-tuned deployments offer [cost savings](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/), but custom model weights may temporarily be stored outside the geography of your Azure OpenAI resource.
 
 :::image type="content" source="../media/fine-tuning/global-standard.png" alt-text="Screenshot of the global standard deployment user experience with a fine-tuned model." lightbox="../media/fine-tuning/global-standard.png":::
 
 Global Standard fine-tuning deployments currently do not support vision and structured outputs.
 
+### Provisioned Managed (preview)
+
+Provisioned managed fine-tuned deployments offer [predictable performance](../concepts/provisioned-throughput.md#what-do-the-provisioned-deployment-types-provide) for fine-tuned deployments. As part of public preview, provisioned managed deployments may be created regionally via the data-plane [REST API](../reference.md#data-plane-inference) version `2024-10-01` or newer. See below for examples.
+
+Provisioned Managed fine-tuning deployments currently do not support vision and structured outputs.
+
+#### Creating a Provisioned Managed deployment
+
+To create a new deployment, make an HTTP PUT call via the [Deployments - Create or Update REST API](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true). The approach is similar to performing [cross region deployment](#cross-region-deployment) with the following exceptions:
+
+- You must provide a sku name of `ProvisionedStandard`.
+- The capacity must be declared in PTUs.
+- The `api-version` must be `2024-10-01` or newer.
+- The HTTP method should be `PUT`.
+
+For example, to deploy a gpt-4o-mini model:
+
+```bash
+curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-01" \
+  -H "Authorization: Bearer <TOKEN>" \
+  -H "Content-Type: application/json" \
+  -d '{
+    "sku": {"name": "ProvisionedStandard", "capacity": 25},
+    "properties": {
+        "model": {
+            "format": "OpenAI",
+            "name": "gpt-4omini-ft-model-name",
+            "version": "1",
+            "source": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/{SourceResourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{SourceAOAIAccountName}"
+        }
+    }
+  }'
+```
+
+#### Scaling a fine-tuned model on Provisioned Managed
+
+To scale a fine-tuned provision managed deployment to increase or decrease PTU capacity, perform the same `PUT` REST API call as you did when [creating the deployment](#creating-a-provisioned-managed-deployment) and provide an updated `capacity` value for the `sku`. Keep in mind, provisioned deployments must scale in [minimum increments](../concepts/provisioned-throughput.md#how-much-throughput-per-ptu-you-get-for-each-model).
+
+For example, to scale the model deployed in the previous section from 25 to 40 PTU, make another `PUT` call and increase the capacity:
+
+```bash
+curl -X PUT "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-01" \
+  -H "Authorization: Bearer <TOKEN>" \
+  -H "Content-Type: application/json" \
+  -d '{
+    "sku": {"name": "ProvisionedStandard", "capacity": 40},
+    "properties": {
+        "model": {
+            "format": "OpenAI",
+            "name": "gpt-4omini-ft-model-name",
+            "version": "1",
+            "source": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/{SourceResourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{SourceAOAIAccountName}"
+        }
+    }
+  }'
+```
+
+#### Deleting a Provisioned Managed deployment
+
+To delete a deployment, use the [Deployments - Delete REST API(/rest/api/aiservices/accountmanagement/deployments/delete?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) and send an HTTP DELETE to the deployment resource. Like with creating deployments, you must include the following parameters:
+
+- Azure subscription id
+- Azure resource group name
+- Azure OpenAI resource name
+- Name of the PTU deployment to delete
+
+For example, to delete the model created and modified in the previous sections:
+
+```bash
+curl -X DELETE "https://management.azure.com/subscriptions/<SUBSCRIPTION>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.CognitiveServices/accounts/<RESOURCE_NAME>/deployments/<MODEL_DEPLOYMENT_NAME>api-version=2024-10-01" \
+  -H "Authorization: Bearer <TOKEN>"
+```
 
 ## Vision fine-tuning
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングに関する情報の追加"
}
```

### Explanation
この変更は、Azure OpenAIのファインチューニングに関する文書に大幅な情報の追加を行っています。主な変更点は、ファインチューニングの異なるデプロイメントタイプに関する説明が強化され、新たに「Provisioned Managed」デプロイメントタイプが紹介されたことです。また、関連するプレミア予告が追加され、これによりユーザーが利用可能な選択肢を理解しやすくなりました。

具体的には、ドキュメント内でファインチューニングがサポートする「グローバルスタンダードデプロイメント」について詳細が述べられた後、新たに「プロビジョニング管理デプロイメント」セクションが設けられました。このセクションでは、プロビジョニングされた管理型ファインチューニングデプロイメントの特性、作成方法、スケールアップ方法、そして削除方法が具体的な手順とともに説明されています。

ファインチューニングのデプロイメントに関する具体的なAPI呼び出しの例も提供されており、ユーザーは実際にどのようにデプロイメントを管理できるかを具体的に理解できるようになっています。これにより、Azure OpenAIのファインチューニング機能をより効果的に利用できるようになります。

## articles/ai-services/openai/includes/environment-variables.md{#item-ee5a34}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.date: 08/28/2023
 
 Create and assign persistent environment variables for your key and endpoint.
 
-[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv-expanded.md)]
 
 # [Command Line](#tab/command-line)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Key Vaultに関するリンクの更新"
}
```

### Explanation
この変更では、ファイル「environment-variables.md」内のAzure Key Vaultに関するリンクが更新されました。具体的には、以前は「azure-key-vault.md」というパスが使用されていましたが、新たに「microsoft-entra-id-akv-expanded.md」というパスへと変更されています。

この変更は、Azure Key Vaultに関連する構成やセキュリティの情報がある新しいリソースへのリンクを提供することで、ユーザーに対してより適切な情報を提供することを目的としています。環境変数の設定において、最新の情報を利用できるようにし、セキュリティとアクセス管理を強化するために役立ちます。この更新により、ユーザーはその関連する内容にアクセスすることで、Azure OpenAIの利用をよりスムーズに行うことができるようになります。


