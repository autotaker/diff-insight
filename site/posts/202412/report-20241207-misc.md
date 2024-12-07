---
date: '2024-12-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d62332b...MicrosoftDocs:d135a3a
summary: このコード変更では、Azure AI Foundryにおける複数の文書にアップデートが行われています。主なポイントは、Cohere Rerankモデルのバージョン表記が「3」から「v3」に変更されたことや、ブロックリストの使用に関する新しいインクルードファイルが追加された点です。また、その他の文書の更新も行われており、特にユーザーにとっての操作負担を軽減することが期待されています。全体として、ユーザードキュメントの最新化と一貫性の向上が図られています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d62332b...MicrosoftDocs:d135a3a){target="_blank"}

# Highlights
このコード変更では、Azure AI Foundryにおける複数の文書に対してさまざまなアップデートが行われました。特に、Cohere Rerankモデルのバージョンが「3」から「v3」に変更されるなどのマイナーアップデートが含まれています。また、ブロックリストの使用に関する新しいインクルードファイルが追加され、情報の統合と更新が行われています。

## New features
- ブロックリストの使用に関する新しいインクルードファイル（`use-blocklists.md`）が追加され、詳細な手順と設定方法が提供されました。

## Breaking changes
- 特に大きな互換性の問題になる変化は報告されていません。

## Other updates
- Cohere Rerankモデル名の表記変更と関連ドキュメントの更新。
- AzureのAdversarialSimulatorでの言語オプションに関する文書更新。
- Azureのオンライン評価でのワークブック共有の注意事項が追加。
- Cohereモデルのバージョン情報が地域別可用性情報内で更新されました。

# Insights
今回の変更は、Azure AI Foundryのユーザードキュメントを最新化し、一貫性を持たせるためのものでした。特に注目すべきは、ユーザーが具体的な操作をより分かりやすく理解できるようにするための表現変更や情報追加が行われたことです。

Cohere Rerankモデルにおいては、バージョンのバージョン情報の「v」が追加されていますが、これはおそらくバージョン管理上の透明性を向上させることを目的としています。この変更により、モデルの識別がより明確になり、文書全体での一貫性が高まります。

また、ブロックリスト機能に関する新しいインクルードファイルの追加は、ユーザーの操作負担を軽減し、特定の機能の利用を促進するためのもので、この分野でのユーザーエクスペリエンスの向上が期待されます。このファイルは、特定のタスクを実行するために必要な情報を詳しく提供します。

さらに、AdversarialSimulatorやオンライン評価の文書の更新も見逃せません。これらは、ユーザーに正確かつ具体的な情報を提供し、日常の業務における効率性を向上させる助けとなるでしょう。全体的に、これらのアップデートは、機能の理解を深めるとともに、サービスをより効果的に用いるための基盤を提供する改良であるといえます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [deploy-models-cohere-rerank.md](#item-5047f8) | minor update | Cohere Rerankモデルのバージョン変更 | modified | 25 | 30 | 55 | 
| [simulator-interaction-data.md](#item-c753d1) | minor update | シミュレーターの言語オプションの更新 | modified | 6 | 2 | 8 | 
| [online-evaluation.md](#item-d9591b) | minor update | ワークブック共有時の注意事項の追加 | modified | 4 | 1 | 5 | 
| [use-blocklists.md](#item-8cd4f8) | minor update | ブロックリストの使用に関する情報の統合 | modified | 1 | 17 | 18 | 
| [region-availability-maas.md](#item-35d79c) | minor update | Cohereモデルのバージョン情報の更新 | modified | 4 | 4 | 8 | 
| [use-blocklists.md](#item-8c4403) | new feature | ブロックリストの使用に関する新しいインクルードファイルの追加 | added | 30 | 0 | 30 | 


# Modified Contents
## articles/ai-studio/how-to/deploy-models-cohere-rerank.md{#item-5047f8}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn to deploy and use Cohere Rerank models with Azure AI Foundry.
 manager: scottpolly
 ms.service: azure-ai-studio
 ms.topic: how-to
-ms.date: 07/24/2024
+ms.date: 12/06/2024
 ms.reviewer: shubhiraj
 ms.author: mopeakande
 author: msakande
@@ -24,12 +24,12 @@ In this article, you learn about the Cohere Rerank models, how to use Azure AI F
 
 Cohere offers two Rerank models in [Azure AI Foundry](https://ai.azure.com). These models are available in the model catalog for deployment as serverless APIs:
 
-* Cohere Rerank 3 - English
-* Cohere Rerank 3 - Multilingual
+* Cohere Rerank v3 - English
+* Cohere Rerank v3 - Multilingual
 
 You can browse the Cohere family of models in the [Model Catalog](model-catalog.md) by filtering on the Cohere collection.
 
-### Cohere Rerank 3 - English
+### Cohere Rerank v3 - English
 
 Cohere Rerank English is a reranking model used for semantic search and retrieval-augmented generation (RAG). Rerank enables you to significantly improve search quality by augmenting traditional keyword-based search systems with a semantic-based reranking system that can contextualize the meaning of a user's query beyond keyword relevance. Cohere's Rerank delivers higher quality results than embedding-based search, lexical search, and even hybrid search, and it requires only adding a single line of code into your application.
 
@@ -42,7 +42,7 @@ Rerank supports JSON objects as documents where users can specify, at query time
 
 Rerank English works well for code retrieval, semi-structured data retrieval, and long context.
 
-### Cohere Rerank 3 - Multilingual
+### Cohere Rerank v3 - Multilingual
 
 Cohere Rerank Multilingual is a reranking model used for semantic search and retrieval-augmented generation (RAG). Rerank Multilingual supports more than 100 languages and can be used to search within a language (for example, to search with a French query on French documents) and across languages (for example, to search with an English query on Chinese documents). Rerank enables you to significantly improve search quality by augmenting traditional keyword-based search systems with a semantic-based reranking system that can contextualize the meaning of a user's query beyond keyword relevance. Cohere's Rerank delivers higher quality results than embedding-based search, lexical search, and even hybrid search, and it requires only adding a single line of code into your application.
 
@@ -64,49 +64,44 @@ You can deploy the previously mentioned Cohere models as a service with pay-as-y
 ### Prerequisites
 
 - An Azure subscription with a valid payment method. Free or trial Azure subscriptions won't work. If you don't have an Azure subscription, create a [paid Azure account](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) to begin.
-- An [AI Foundry hub](../how-to/create-azure-ai-resource.md). The serverless API model deployment offering for Cohere Rerank is only available with hubs created in these regions:
-
-     * East US
-     * East US 2
-     * North Central US
-     * South Central US
-     * West US
-     * West US 3
-     * Sweden Central
-    
-    For a list of  regions that are available for each of the models supporting serverless API endpoint deployments, see [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md).
+
+- An [Azure AI Foundry hub](../how-to/create-azure-ai-resource.md). The serverless API model deployment offering for Cohere Rerank is only available with hubs created in specific regions. For a list of regions that are available for each of the Cohere models that support serverless API endpoint deployments, see [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md#cohere-models).
 
 - An [Azure AI Foundry project](../how-to/create-projects.md).
+
 - Azure role-based access controls are used to grant access to operations in Azure AI Foundry portal. To perform the steps in this article, your user account must be assigned the __Azure AI Developer role__ on the resource group. For more information on permissions, see [Role-based access control in Azure AI Foundry portal](../concepts/rbac-ai-studio.md).
 
 
 ### Create a new deployment
 
-The following steps demonstrate the deployment of Cohere Rerank 3 - English, but you can use the same steps to deploy Cohere Rerank 3 - Multilingual by replacing the model name.
+The following steps demonstrate the deployment of Cohere Rerank v3 - English, but you can use the same steps to deploy Cohere Rerank v3 - Multilingual by replacing the model name.
 
 To create a deployment:
 
-1. Sign in to [Azure AI Foundry](https://ai.azure.com).
-1. Select **Model catalog** from the left sidebar.
-1. Search for *Cohere*.
-1. Select **cohere-rerank-3-english** to open the Model Details page.
+[!INCLUDE [open-catalog](../includes/open-catalog.md)]
+
+4. Select the model card of the model you want to deploy. In this article, you select **Cohere-rerank-v3-english** to open the Model Details page.
+
 1. Select **Deploy** to open a serverless API deployment window for the model.
-1. Alternatively, you can initiate a deployment by starting from your project in AI Foundry portal. 
+1. Alternatively, you can initiate a deployment from your project in the AI Foundry portal as follows: 
 
     1. From the left sidebar of your project, select **Models + Endpoints**.
-    1. Select **+ Deploy model**.
-    1. Search for and select **Cohere-rerank-3-english**. to open the Model Details page.
+    1. Select **+ Deploy model** > **Deploy base model**.
+    1. Search for and select **Cohere-rerank-v3-english** to open the Model Details page.
     1. Select **Confirm** to open a serverless API deployment window for the model.
 
-1. Select the project in which you want to deploy your model.
 1. In the deployment wizard, select the link to **Azure Marketplace Terms** to learn more about the terms of use.
 1. Select the **Pricing and terms** tab to learn about pricing for the selected model.
-1. Select the **Subscribe and Deploy** button. If this is your first time deploying the model in the project, you have to subscribe your project for the particular offering. This step requires that your account has the **Azure AI Developer role** permissions on the resource group, as listed in the prerequisites. Each project has its own subscription to the particular Azure Marketplace offering of the model, which allows you to control and monitor spending. Currently, you can have only one deployment for each model within a project.
+1. Select the **Subscribe and Deploy** button. If this is your first time deploying the model in the project, you have to subscribe your project for the particular offering.
+
+    > [!NOTE]
+    > This step requires that your account has the **Azure AI Developer role** permissions on the resource group, as listed in the prerequisites. Models that are offered by non-Microsoft providers (for example, Cohere models) are billed through the Azure Marketplace. For such models, you're required to subscribe your project to the particular model offering. Each project has its own subscription to the particular Azure Marketplace offering of the model, which allows you to control and monitor spending. Currently, you can have only one deployment for each model within a project.
+
 1. Once you subscribe the project for the particular Azure Marketplace offering, subsequent deployments of the _same_ offering in the _same_ project don't require subscribing again. If this scenario applies to you, there's a **Continue to deploy** option to select.
 
 1. Give the deployment a name. This name becomes part of the deployment API URL. This URL must be unique in each Azure region.
 
-1. Select **Deploy**. Wait until the deployment is ready and you're redirected to the Deployments page.
+1. Select **Deploy**. Wait until the deployment is ready and you're redirected to the **Model deployments** page.
 1. On the Deployments page, select the deployment, and note the endpoint's **Target** URL and the Secret **Key**. For more information on using the APIs, see the [reference](#rerank-api-reference-for-cohere-rerank-models-deployed-as-a-service) section.
 1. [!INCLUDE [Find your deployment details](../includes/find-deployments.md)]
 
@@ -122,11 +117,11 @@ Cohere Rerank models deployed as serverless APIs can be consumed using the Reran
 
 1. Copy the **Target** URL and the **Key** value.
 
-1. Cohere currently exposes `v1/rerank` for inference with the Rerank 3 - English and Rerank 3 - Multilingual models schema. For more information on using the APIs, see the [reference](#rerank-api-reference-for-cohere-rerank-models-deployed-as-a-service) section.
+1. Cohere currently exposes `v1/rerank` for inference with the Rerank v3 - English and Rerank v3 - Multilingual models schema. For more information on using the APIs, see the [reference](#rerank-api-reference-for-cohere-rerank-models-deployed-as-a-service) section.
 
 ## Rerank API reference for Cohere Rerank models deployed as a service
 
-Cohere Rerank 3 - English and Rerank 3 - Multilingual accept the native Cohere Rerank API on `v1/rerank`. This section contains details about the Cohere Rerank API.
+Cohere Rerank v3 - English and Rerank v3 - Multilingual accept the native Cohere Rerank API on `v1/rerank`. This section contains details about the Cohere Rerank API.
 
 #### v1/rerank request
 
@@ -139,7 +134,7 @@ Cohere Rerank 3 - English and Rerank 3 - Multilingual accept the native Cohere R
 
 #### v1/rerank request schema
 
-Cohere Rerank 3 - English and Rerank 3 - Multilingual accept the following parameters for a `v1/rerank` API call:
+Cohere Rerank v3 - English and Rerank v3 - Multilingual accept the following parameters for a `v1/rerank` API call:
 
 | Property | Type | Default | Description |
 | --- | --- | --- | --- |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cohere Rerankモデルのバージョン変更"
}
```

### Explanation
この変更は、Azure AI FoundryでのCohere Rerankモデルに関する文書の更新を含んでいます。主な変更点は、「Cohere Rerank 3」という表記を「Cohere Rerank v3」に変更したことです。また、日付の更新が行われ、手順に関する明確さが向上しました。具体的には、モデル名の表記が一貫性を持つように更新され、導入の手順がより明確になっています。全体で25行が追加され、30行が削除され、55行に変更が加えられました。これにより、ユーザがCohere Rerankモデルをより的確に理解し、利用できるようになります。

## articles/ai-studio/how-to/develop/simulator-interaction-data.md{#item-c753d1}

<details>
<summary>Diff</summary>
````diff
@@ -398,7 +398,7 @@ The `AdversarialSimulator` supports a range of scenarios, hosted in the service,
 | Grounded Content Generation (single turn only)  | `ADVERSARIAL_CONTENT_GEN_GROUNDED`   |475 |Hateful and unfair content, Sexual content, Violent content, Self-harm-related content, Direct Attack (UPIA) Jailbreak |
 | Protected Material (single turn only) | `ADVERSARIAL_PROTECTED_MATERIAL` | 306 | Protected Material |
 
-- For testing groundedness scenarios (single or multi-turn), see the section on [simulating and evaluating for groundendess](#simulating-and-evaluating-for-groundendess).
+- For testing groundedness scenarios (single or multi-turn), see the section on [simulating and evaluating for groundedness](#simulating-and-evaluating-for-groundendess).
 - For simulating direct attack (UPIA) and indirect attack (XPIA) scenarios, see section on [simulating jailbreak attacks](#simulating-jailbreak-attacks).
 
 ### Simulating jailbreak attacks
@@ -510,13 +510,17 @@ Using the [ISO standard](https://www.andiamo.co.uk/resources/iso-language-codes/
 | Simplified Chinese | zh-cn             |
 | German             | de                |
 
+The language options can be passed in as an optional parameter to the `AdversarialSimulator` class using the [`SupportedLanguages` class](/python/api/azure-ai-evaluation/azure.ai.evaluation.simulator.supportedlanguages).
+
 Usage example below:
 
 ```python
+from azure.ai.evaluation.simulator import SupportedLanguages
+
 outputs = await simulator(
         scenario=scenario, # required, adversarial scenario to simulate
         target=callback, # required, callback function to simulate against
-        language=es # optional, default english
+        language=SupportedLanguages.Spanish # optional, default english
     )
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "シミュレーターの言語オプションの更新"
}
```

### Explanation
この変更は、AzureのAdversarialSimulatorに関連する文書のマイナーアップデートであり、言語オプションに関する情報が追加されています。具体的には、シミュレータークラスに対して使用可能な言語オプションを指定できることが明記されており、その例も示されています。また、文中の一部表現が適切に修正され、読みやすさが向上しています。全体で6行が追加され、2行が削除され、8行に変更が加えられました。これにより、ユーザーがシミュレーション機能をより効果的に活用できるようになります。

## articles/ai-studio/how-to/online-evaluation.md{#item-d9591b}

<details>
<summary>Diff</summary>
````diff
@@ -360,10 +360,13 @@ You can also share this workbook with your team so they stay informed with the l
 
 :::image type="content" source="../media/how-to/online-evaluation/share-azure-workbook.png" alt-text="Screenshot of an Azure Workbook showing the share button and share tab." lightbox="../media/how-to/online-evaluation/share-azure-workbook.png":::
 
+> [!NOTE]
+> When sharing this workbook with your team members, they must have atleast 'Reader' role to the connected Application Insights resource to view the displayed information.
+
 ## Related content
 
 - [Trace your application with Azure AI Inference SDK](./develop/trace-local-sdk.md)
 - [Visualize your traces](./develop/visualize-traces.md)
 - [Evaluation of Generative AI Models & Applications](../concepts/evaluation-approach-gen-ai.md)
 - [Azure Monitor Application Insights](/azure/azure-monitor/app/app-insights-overview)
-- [Azure Workbooks](/azure/azure-monitor/visualize/workbooks-overview)
\ No newline at end of file
+- [Azure Workbooks](/azure/azure-monitor/visualize/workbooks-overview)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ワークブック共有時の注意事項の追加"
}
```

### Explanation
この変更は、Azureのオンライン評価に関する文書において、ワークブックをチームと共有する際の注意事項が追加されたことを示しています。具体的には、共有したワークブックを表示するためには、チームメンバーが接続されたApplication Insightsリソースに対して「Reader」ロールを持っている必要があるという情報が強調されています。さらに、関連コンテンツのセクションにも若干の編集が加えられています。全体で4行が追加され、1行が削除され、5行に変更が加えられました。これにより、ユーザーがワークブックの共有に関する重要な情報を理解しやすくなります。

## articles/ai-studio/how-to/use-blocklists.md{#item-8cd4f8}

<details>
<summary>Diff</summary>
````diff
@@ -17,20 +17,4 @@ author: PatrickFarley
 
 You can create custom blocklists in the Azure AI Foundry portal as part of your content filtering configurations. The following steps show how to create custom blocklists as part of your content filters in Azure AI Foundry portal.
 
-## Create a blocklist
-
-1. Go to [Azure AI Foundry](https://ai.azure.com/) and navigate to your project/hub. Then select the **Safety+ Security** page on the left nav and select the **Blocklists** tab.
-    :::image type="content" source="../media/content-safety/content-filter/select-blocklists.png" lightbox="../media/content-safety/content-filter/select-blocklists.png" alt-text="Screenshot of the Blocklists page tab.":::
-1. Select **Create a blocklist**. Enter a name for your blocklist, add a description, and select an Azure OpenAI resource to connect it to. Then select **Create Blocklist**.
-1. Select your new blocklist once it's created. On the blocklist's page, select **Add new term**.
-1. Enter the term that should be filtered and select **Add term**. You can also use a regex.
-    You can delete each term in your blocklist.
-
-## Attach a blocklist to a content filter configuration
-
-1. Once the blocklist is ready, go back to the **Safety+ Security** page and select the **Content filters** tab. Create a new content filter configuration. This opens a wizard with several AI content safety components.
-    :::image type="content" source="../media/content-safety/content-filter/create-content-filter.png" lightbox="../media/content-safety/content-filter/create-content-filter.png" alt-text="Screenshot of the Create content filter button.":::
-1. On the **Input filter** and **Output filter** screens, toggle the **Blocklist** button on. You can then select a blocklist from the list. 
-    There are two types of blocklists: the custom blocklists you created, and prebuilt blocklists that Microsoft provides&mdash;in this case a Profanity blocklist (English).
-1. You can now decide which of the available blocklists you want to include in your content filtering configuration. The last step is to review and finish the content filtering configuration by selecting **Next**.
-    You can always go back and edit your configuration. Once it’s ready, select a **Create content filter**. The new configuration that includes your blocklists can now be applied to a deployment.
\ No newline at end of file
+[!INCLUDE [use-blocklists](../includes/use-blocklists.md)]
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ブロックリストの使用に関する情報の統合"
}
```

### Explanation
この変更は、Azure AI Foundryでのブロックリストの使用に関する文書を更新したもので、主に内容の整理が行われました。具体的には、以前の詳細な手順が削除され、代わりに別の共有可能なインクルードファイル（`use-blocklists.md`）が追加されました。これにより、ブロックリストの作成と設定に関する情報がより一元化され、文書の簡潔さが向上しています。全体で1行が追加され、17行が削除され、合計で18行に変更が加えられました。この変更は、ユーザーがブロックリストを使用する際の情報へのアクセスを簡素化し、より効果的に内容を管理できるようにすることを目的としています。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -19,10 +19,10 @@ Cohere Command R+ 08-2024     |  [Microsoft Managed Countries](/partner-center/m
 Cohere Command R 08-2024     |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available        |
 Cohere Command R+     |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available        |
 Cohere Command R      | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3       | Not available        |
-Cohere Rerank 3 - English   |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available       |
-Cohere Rerank 3 - Multilingual   |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available       |
-Cohere Embed 3 - English    |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar   |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3    | Not available       |
-Cohere Embed 3 -  Multilingual    |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar   |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3    | Not available       |
+Cohere Rerank v3 - English   |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available       |
+Cohere Rerank v3 - Multilingual   |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available       |
+Cohere Embed v3 - English    |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar   |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3    | Not available       |
+Cohere Embed v3 -  Multilingual    |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar   |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3    | Not available       |
 
 
 ### JAIS models
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cohereモデルのバージョン情報の更新"
}
```

### Explanation
この変更は、「Cohere」モデルに関する地域別の可用性情報を更新するもので、特にモデルのバージョン番号が変更され、新たに「v3」のバージョンが追加されました。具体的には、「Cohere Rerank」および「Cohere Embed」に関連するエントリが、新しいバージョンを反映する形で編集され、旧バージョンのエントリが削除されています。この更新により、ユーザーは最新のモデルバージョンに関する正確な情報を得ることができるようになります。全体で4行の追加と4行の削除があり、合計で8行に変更が加えられました。これにより、ドキュメントの最新性が保たれ、利用者が必要な情報を簡単に見つけられるようになります。

## articles/ai-studio/includes/use-blocklists.md{#item-8c4403}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,30 @@
+---
+title: include file
+description: include file
+author: PatrickFarley
+ms.reviewer: pafarley
+ms.author: pafarley
+ms.service: azure-ai-studio
+ms.topic: include
+ms.date: 12/05/2024
+ms.custom: include
+---
+
+
+## Create a blocklist
+
+1. Go to [Azure AI Foundry](https://ai.azure.com/) and navigate to your project/hub. Then select the **Safety+ Security** page on the left nav and select the **Blocklists** tab.
+    :::image type="content" source="../media/content-safety/content-filter/select-blocklists.png" lightbox="../media/content-safety/content-filter/select-blocklists.png" alt-text="Screenshot of the Blocklists page tab.":::
+1. Select **Create a blocklist**. Enter a name for your blocklist, add a description, and select an Azure OpenAI resource to connect it to. Then select **Create Blocklist**.
+1. Select your new blocklist once it's created. On the blocklist's page, select **Add new term**.
+1. Enter the term that should be filtered and select **Add term**. You can also use a regex.
+    You can delete each term in your blocklist.
+
+## Attach a blocklist to a content filter configuration
+
+1. Once the blocklist is ready, go back to the **Safety+ Security** page and select the **Content filters** tab. Create a new content filter configuration. This opens a wizard with several AI content safety components.
+    :::image type="content" source="../media/content-safety/content-filter/create-content-filter.png" lightbox="../media/content-safety/content-filter/create-content-filter.png" alt-text="Screenshot of the Create content filter button.":::
+1. On the **Input filter** and **Output filter** screens, toggle the **Blocklist** button on. You can then select a blocklist from the list. 
+    There are two types of blocklists: the custom blocklists you created, and prebuilt blocklists that Microsoft provides&mdash;in this case a Profanity blocklist (English).
+1. You can now decide which of the available blocklists you want to include in your content filtering configuration. The last step is to review and finish the content filtering configuration by selecting **Next**.
+    You can always go back and edit your configuration. Once it’s ready, select a **Create content filter**. The new configuration that includes your blocklists can now be applied to a deployment.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ブロックリストの使用に関する新しいインクルードファイルの追加"
}
```

### Explanation
この変更は、Azure AI Foundryにおけるブロックリストの使用方法を説明するための新しいインクルードファイル（`use-blocklists.md`）を追加したものです。このファイルには、ブロックリストを作成する手順と、コンテンツフィルター設定にブロックリストを適用する方法が詳細に記載されています。

具体的には、次のような内容が含まれています：
- ユーザーがAzure AI Foundryでブロックリストを作成するための手順
- 新しいブロックリストを作成し、用語を追加する方法
- 作成したブロックリストをコンテンツフィルター構成に接続するための手順

この新しいファイルの追加により、ユーザーはブロックリストの設定や利用に関する情報に簡単にアクセスできるようになり、より効率的にコンテンツフィルタリングを行うことが可能となります。全体で30行が追加され、変更内容はすべて新規の情報です。ユーザーエクスペリエンスの向上を目指した重要な追加といえます。


