---
date: '2024-12-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d62332b...MicrosoftDocs:d135a3a
summary: この記事では、Azure OpenAIサービスに関連する文書が更新され、「Azure OpenAI Studio」から「Azure AI Foundry」への名称変更を中心に多くの修正が行われたことが報告されています。これには地域要件やリスク管理、DALL-EやGPTモデルに関する情報の更新が含まれています。新たにセキュリティとガバナンスに関するセクションも追加され、各機能の説明が見直されました。特に、地域要件から特定の地域が削除された点も注目されています。この更新により、ユーザーは最新の情報を得て、サービスをより一貫して活用できるようになります。全体として、セキュリティ対策を強化しつつ、サービスのフレキシビリティ向上を目指しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d62332b...MicrosoftDocs:d135a3a){target="_blank"}

# ハイライト
この記事では、Azure OpenAIサービス関連のいくつかの文書が更新され、特に「Azure OpenAI Studio」から「Azure AI Foundry」への名称変更に関連する修正が多く行われました。この変更には、地域要件、リスクと安全性の管理、ブロックリストの使用方法、およびDALL-EやGPTモデルに関する情報の更新が含まれています。また、新たにセキュリティとガバナンスに関するセクションも追加されました。

## 新機能
- 「Azure AI Foundry」への改称に伴い、各機能に関する説明と使用方法が更新。
- DALL-EやGPTモデルのデプロイメントに関連する地域が拡張され、新しい地域が追加。
- セキュリティとガバナンスに関するセクションが目次に追加。

## 破壊的変更
- 地域要件における特定の地域がDALL-Eモデルの必要条件として削除された。
  
## その他の更新
- コンテンツフィルタリングやリスク＆安全管理のガイドの更新。
- 目次にセキュリティ関連の新たなセクションが追加。

# インサイト
今回のドキュメント更新により、Azure OpenAIサービスの利用者は最新のプラットフォームである「Azure AI Foundry」に基づいた情報を得ることができます。名称変更に伴う文章の修正によって、今後はより一貫したプラットフォーム名で取り扱うことができるため、可読性が向上しています。

特に、DALL-EモデルやGPTモデルの利用可能な地域の拡大は、これらのモデルをより広範囲に普及させるための重要なステップです。これにより、異なる地域のユーザーが多様なAI機能を活用しやすくなります。

さらに、セキュリティとガバナンスに関する項目の追加は、企業がAzure AIサービスを採用する際のセキュリティ対策を理解し、適切に実施するための指針を提供することを意図しています。仮想ネットワークの設定やデータの暗号化、RBACの導入などは、データ保護の強化に寄与します。

全体として、このアップデートはAzure環境でのAIサービスの整合性と安全性を高めつつ、開発者や企業がサービスを活用する際のフレキシビリティを向上させることを目指しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [content-filters.md](#item-6f0627) | minor update | Azure AI Foundryへのコンテンツフィルターの更新 | modified | 12 | 8 | 20 | 
| [dall-e.md](#item-ac9616) | minor update | DALL-Eモデルの地域要件の更新 | modified | 3 | 3 | 6 | 
| [risks-safety-monitor.md](#item-b2be0b) | minor update | リスク＆安全モニタリングに関する名称および場所の変更 | modified | 13 | 11 | 24 | 
| [use-blocklists.md](#item-e99db7) | minor update | ブロックリストの使用に関する更新 | modified | 11 | 25 | 36 | 
| [dall-e-studio.md](#item-439729) | minor update | DALL-Eスタジオに関するドキュメントの更新 | modified | 9 | 27 | 36 | 
| [gpt-v-studio.md](#item-dcd50e) | minor update | Azure AI Foundryにおける画像およびビデオの利用に関するガイド更新 | modified | 11 | 18 | 29 | 
| [datazone-provisioned-managed.md](#item-ae7f5b) | minor update | モデルマトリックスの地域更新 | modified | 10 | 6 | 16 | 
| [global-batch.md](#item-929e6a) | minor update | グローバルバッチのモデルマトリックス地域の更新 | modified | 23 | 19 | 42 | 
| [toc.yml](#item-c945af) | minor update | セキュリティとガバナンスに関するセクションの追加 | modified | 16 | 0 | 16 | 


# Modified Contents
## articles/ai-services/openai/how-to/content-filters.md{#item-6f0627}

<details>
<summary>Diff</summary>
````diff
@@ -1,22 +1,26 @@
 ---
-title: 'Use content filters (preview) with Azure OpenAI Service'
+title: 'Use content filters (preview) with Azure AI Foundry'
 titleSuffix: Azure OpenAI
-description: Learn how to use and configure the content filters that come with Azure OpenAI Service, including getting approval for gated modifications.
+description: Learn how to use and configure the content filters that come with Azure AI Foundry, including getting approval for gated modifications.
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 10/04/2024
+ms.date: 12/05/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
 ms.custom: FY25Q1-Linter
-# customer intent: As a developer, I want to learn how to configure content filters with Azure OpenAI Service so that I can ensure that my applications comply with our Code of Conduct.
+# customer intent: As a developer, I want to learn how to configure content filters with Azure AI Foundry so that I can ensure that my applications comply with our Code of Conduct.
 ---
 
-# How to configure content filters with Azure OpenAI Service
+# How to configure content filters with Azure AI Foundry
 
-The content filtering system integrated into Azure OpenAI Service runs alongside the core models, including DALL-E image generation models. It uses an ensemble of multi-class classification models to detect four categories of harmful content (violence, hate, sexual, and self-harm) at four severity levels respectively (safe, low, medium, and high), and optional binary classifiers for detecting jailbreak risk, existing text, and code in public repositories. The default content filtering configuration is set to filter at the medium severity threshold for all four content harms categories for both prompts and completions. That means that content that is detected at severity level medium or high is filtered, while content detected at severity level low or safe is not filtered by the content filters. Learn more about content categories, severity levels, and the behavior of the content filtering system [here](../concepts/content-filter.md). Jailbreak risk detection and protected text and code models are optional and off by default. For jailbreak and protected material text and code models, the configurability feature allows all customers to turn the models on and off. The models are by default off and can be turned on per your scenario. Some models are required to be on for certain scenarios to retain coverage under the [Customer Copyright Commitment](/legal/cognitive-services/openai/customer-copyright-commitment?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext).
+The content filtering system integrated into Azure AI Foundry runs alongside the core models, including DALL-E image generation models. It uses an ensemble of multi-class classification models to detect four categories of harmful content (violence, hate, sexual, and self-harm) at four severity levels respectively (safe, low, medium, and high), and optional binary classifiers for detecting jailbreak risk, existing text, and code in public repositories. 
+
+The default content filtering configuration is set to filter at the medium severity threshold for all four content harms categories for both prompts and completions. That means that content that is detected at severity level medium or high is filtered, while content detected at severity level low or safe is not filtered by the content filters. Learn more about content categories, severity levels, and the behavior of the content filtering system [here](../concepts/content-filter.md). 
+
+Jailbreak risk detection and protected text and code models are optional and off by default. For jailbreak and protected material text and code models, the configurability feature allows all customers to turn the models on and off. The models are by default off and can be turned on per your scenario. Some models are required to be on for certain scenarios to retain coverage under the [Customer Copyright Commitment](/legal/cognitive-services/openai/customer-copyright-commitment?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext).
 
 > [!NOTE]
 > All customers have the ability to modify the content filters and configure the severity thresholds (low, medium, high). Approval is required for turning the content filters partially or fully off. Managed customers only may apply for full content filtering control via this form: [Azure OpenAI Limited Access Review: Modified Content Filters](https://ncv.microsoft.com/uEfCgnITdR). At this time, it is not possible to become a managed customer.
@@ -37,7 +41,7 @@ You can configure the following filter categories in addition to the default har
 
 |Filter category  |Status |Default setting  |Applied to prompt or completion?  |Description  |
 |---------|---------|---------|---------|---|
-|Prompt Shields for direct attacks (jailbreak)     |GA|    On     |   User prompt      |   Filters / annotates user prompts that might present a Jailbreak Risk. For more information about annotations, visit [Azure OpenAI Service content filtering](/azure/ai-services/openai/concepts/content-filter?tabs=python#annotations-preview). |
+|Prompt Shields for direct attacks (jailbreak)     |GA|    On     |   User prompt      |   Filters / annotates user prompts that might present a Jailbreak Risk. For more information about annotations, visit [Azure AI Foundry content filtering](/azure/ai-services/openai/concepts/content-filter?tabs=python#annotations-preview). |
 |Prompt Shields for indirect attacks  | GA| Off | User prompt | Filter / annotate Indirect Attacks, also referred to as Indirect Prompt Attacks or Cross-Domain Prompt Injection Attacks, a potential vulnerability where third parties place malicious instructions inside of documents that the generative AI system can access and process. Requires: [Document embedding and formatting](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cuser-prompt%2Cpython-new#embedding-documents-in-your-prompt). |
 | Protected material - code |GA| On | Completion | Filters protected code or gets the example citation and license information in annotations for code snippets that match any public code sources, powered by GitHub Copilot. For more information about consuming annotations, see the [content filtering concepts guide](/azure/ai-services/openai/concepts/content-filter#annotations-preview) |
 | Protected material - text | GA| On | Completion | Identifies and blocks known text content from being displayed in the model output (for example, song lyrics, recipes, and selected web content).  |
@@ -60,5 +64,5 @@ We recommend informing your content filtering configuration decisions through an
 ## Related content
 
 - Learn more about Responsible AI practices for Azure OpenAI: [Overview of Responsible AI practices for Azure OpenAI models](/legal/cognitive-services/openai/overview?context=/azure/ai-services/openai/context/context).
-- Read more about [content filtering categories and severity levels](../concepts/content-filter.md) with Azure OpenAI Service.
+- Read more about [content filtering categories and severity levels](../concepts/content-filter.md) with Azure AI Foundry.
 - Learn more about red teaming from our: [Introduction to red teaming large language models (LLMs) article](../concepts/red-teaming.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryへのコンテンツフィルターの更新"
}
```

### Explanation
この変更は、「Azure OpenAI Service」から「Azure AI Foundry」へのコンテンツフィルターに関する記事のタイトルや説明の更新を含んでいます。また、日付や顧客の意図に関する記述も同様に更新されています。具体的には、フィルターの設定やそれに関する内容が変更され、Azure AI Foundryに特有の情報が強調されるように修正されています。この更新によって、Azureの新しいプラットフォームに関する情報が明確化され、開発者がコンテンツフィルターの使用方法をより理解しやすくなります。フィルタリングシステムの動作や設定についての詳細も引き続き説明されていますが、文中の用語が変更されたため、これからは特にAzure AI Foundryに関するコンテンツとして認識されることになるでしょう。

## articles/ai-services/openai/how-to/dall-e.md{#item-ac9616}

<details>
<summary>Diff</summary>
````diff
@@ -24,13 +24,13 @@ OpenAI's DALL-E models generate images based on user-provided text prompts. This
 #### [DALL-E 3](#tab/dalle3)
 
 - An Azure subscription. You can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?icid=ai-services).
-- An Azure OpenAI resource created in the *Sweden Central* region. For more information, see [Create and deploy an Azure OpenAI Service resource](../how-to/create-resource.md).
-- Deploy a *dall-e-3* model with your Azure OpenAI resource.
+- An Azure OpenAI resource created in a supported region. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
+- - Deploy a *dall-e-3* model with your Azure OpenAI resource.
 
 #### [DALL-E 2 (preview)](#tab/dalle2)
 
 - An Azure subscription. You can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?icid=ai-services).
-- An Azure OpenAI resource created in the *East US* region. For more information, see [Create and deploy an Azure OpenAI Service resource](../how-to/create-resource.md).
+- An Azure OpenAI resource created in a supported region. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability). For more information, see [Create and deploy an Azure OpenAI Service resource](../how-to/create-resource.md).
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL-Eモデルの地域要件の更新"
}
```

### Explanation
この変更は、DALL-Eモデルを使用する際のAzure OpenAIリソースの地域に関する要件を更新しています。具体的には、DALL-E 3およびDALL-E 2の必要条件から、「スウェーデンセンター」および「米国東部」の地域を削除し、代わりに「サポートされている地域に作成されたAzure OpenAIリソース」が必要であることを明記しています。この更新により、ユーザーがDALL-Eモデルをデプロイする際に、利用可能な地域についての理解が深まり、最新の情報に基づいてリソースを作成できるようになります。また、地域に関する情報を参照できる新しいリンクが追加されており、Azureのサービスを利用する際の手続きがよりスムーズになることを意図しています。

## articles/ai-services/openai/how-to/risks-safety-monitor.md{#item-b2be0b}

<details>
<summary>Diff</summary>
````diff
@@ -1,30 +1,28 @@
 ---
-title: How to use Risks & Safety monitoring in Azure OpenAI Studio
+title: How to use Risks & Safety monitoring in Azure AI Foundry
 titleSuffix: Azure OpenAI Service
 description: Learn how to check statistics and insights from your Azure OpenAI content filtering activity.
 author: PatrickFarley 
 ms.author: pafarley 
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 10/03/2024
+ms.date: 12/05/2024
 manager: nitinme
 ---
 
-# Use Risks & Safety monitoring in Azure OpenAI Studio (preview) 
+# Use Risks & Safety monitoring in Azure AI Foundry (preview) 
 
-When you use an Azure OpenAI model deployment with a content filter, you may want to check the results of the filtering activity. You can use that information to further adjust your filter configuration to serve your specific business needs and Responsible AI principles.  
+When you use an Azure OpenAI model deployment with a content filter, you may want to check the results of the filtering activity. You can use that information to further adjust your [filter configuration](/azure/ai-services/openai/how-to/content-filters) to serve your specific business needs and Responsible AI principles.  
 
-[Azure OpenAI Studio](https://oai.azure.com/) provides a Risks & Safety monitoring dashboard for each of your deployments that uses a content filter configuration.
+[Azure AI Foundry](https://oai.azure.com/) provides a Risks & Safety monitoring dashboard for each of your deployments that uses a content filter configuration.
 
 ## Access Risks & Safety monitoring
 
 To access Risks & Safety monitoring, you need an Azure OpenAI resource in one of the supported Azure regions: East US, Switzerland North, France Central, Sweden Central, Canada East. You also need a model deployment that uses a content filter configuration.
 
-Go to [Azure OpenAI Studio](https://oai.azure.com/) and sign in with the credentials associated with your Azure OpenAI resource. Select the **Deployments** tab on the left and then select your model deployment from the list. On the deployment's page, select the **Risks & Safety** tab at the top.
+Go to [Azure AI Foundry](https://oai.azure.com/) and sign in with the credentials associated with your Azure OpenAI resource. Select a project. Then select the **Models + endpoints** tab on the left and then select your model deployment from the list. On the deployment's page, select the **Metrics** tab at the top. Then select **Open in Azure Monitor** to view the full report in the Azure portal.
 
-## Content detection   
-
-The **Content detection** pane shows information about content filter activity. Your content filter configuration is applied as described in the [Content filtering documentation](/azure/ai-services/openai/how-to/content-filters).
+## Configure metrics   
 
 ### Report description
 
@@ -35,7 +33,9 @@ Content filtering data is shown in the following ways:
 - **Severity distribution by category**: This view shows the severity levels detected for each harm category, across the whole selected time range. This is not limited to _blocked_ content but rather includes all content that was flagged by the content filters.
 - **Severity rate distribution over time by category**: This view shows the rates of detected severity levels over time, for each harm category. Select the tabs to switch between supported categories.
 
+<!--
 :::image type="content" source="../media/how-to/content-detection.png" alt-text="Screenshot of the content detection pane in the Risks & Safety monitoring page." lightbox="../media/how-to/content-detection.png":::
+-->
 
 ### Recommended actions
 
@@ -56,7 +56,7 @@ To use Potentially abusive user detection, you need:
 ### Set up your Azure Data Explorer database
 
 In order to protect the data privacy of user information and manage the permission of the data, we support the option for our customers to bring their own storage to get the detailed potentially abusive user detection insights (including user GUID and statistics on harmful request by category) stored in a compliant way and with full control. Follow these steps to enable it:
-1. In Azure OpenAI Studio, navigate to the model deployment that you'd like to set up user abuse analysis with, and select **Add a data store**. 
+1. In Azure AI Foundry, navigate to the model deployment that you'd like to set up user abuse analysis with, and select **Add a data store**. 
 1. Fill in the required information and select **Save**. We recommend you create a new database to store the analysis results.
 1. After you connect the data store, take the following steps to grant permission to write analysis results to the connected database:
     1. Go to your Azure OpenAI resource's page in the Azure portal, and choose the **Identity** tab.
@@ -81,14 +81,16 @@ The potentially abusive user detection relies on the user information that custo
     - **Total abuse request ratio/count**
     - **Abuse ratio/count by category** 
 
+<!--
 :::image type="content" source="../media/how-to/potentially-abusive-user.png" alt-text="Screenshot of the Potentially abusive user detection pane in the Risks & Safety monitoring page." lightbox="../media/how-to/potentially-abusive-user.png":::
+-->
 
 ### Recommended actions
 
 Combine this data with enriched signals to validate whether the detected users are truly abusive or not. If they are, then take responsive action such as throttling or suspending the user to ensure the responsible use of your application.
 
 ## Next steps
 
-Next, create or edit a content filter configuration in Azure OpenAI Studio.
+Next, create or edit a content filter configuration in Azure AI Foundry.
 
 - [Configure content filters with Azure OpenAI Service](/azure/ai-services/openai/how-to/content-filters)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リスク＆安全モニタリングに関する名称および場所の変更"
}
```

### Explanation
この変更は、「Azure OpenAI Studio」という名称を「Azure AI Foundry」に更新し、それに伴う文書の内容を調整しています。また、リスク＆安全モニタリングの使用方法に関連する情報が最新のAzureプラットフォームに合わせて修正されました。具体的には、Azure OpenAIリソースの作成手順や、利用可能な地域に関する表現が柔軟に対応されていることが示されています。さらに、ユーザーがリスク＆安全モニタリングにアクセスするための手順やダッシュボードの構成が明確化され、特にAzure AI Foundryでの利用方法が強調されています。この更新により、開発者はAzure AI Foundryを介してリスクと安全性のモニタリングを効果的に実施できるようになり、コンテンツフィルタリングの活動に基づいた分析が容易になります。

## articles/ai-services/openai/how-to/use-blocklists.md{#item-e99db7}

<details>
<summary>Diff</summary>
````diff
@@ -6,12 +6,12 @@ description: Learn how to use blocklists with Azure OpenAI Service
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 10/03/2024
+ms.date: 12/05/2024
 author: PatrickFarley
 ms.author: pafarley
 ---
 
-# Use a blocklist in Azure OpenAI
+# Use a blocklist with Azure OpenAI
 
 The configurable content filters are sufficient for most content moderation needs. However, you may need to filter terms specific to your use case. 
 
@@ -25,6 +25,8 @@ The configurable content filters are sufficient for most content moderation need
 
 ## Use blocklists
 
+#### [Azure OpenAI API](#tab/api)
+
 You can create blocklists with the Azure OpenAI API. The following steps help you get started. 
 
 ### Get your token
@@ -61,7 +63,7 @@ The response code should be `201` (created a new list) or `200` (updated an exis
 
 ### Apply a blocklist to a content filter
 
-If you haven't yet created a content filter, you can do so in the Studio in the Content Filters tab on the left hand side. In order to use the blocklist, make sure this Content Filter is applied to an Azure OpenAI deployment. You can do this in the Deployments tab on the left hand side. 
+If you haven't yet created a content filter, you can do so in Azure AI Foundry. See [Content filtering](/azure/ai-services/openai/how-to/content-filters#create-a-content-filter-in-azure-ai-foundry).
 
 To apply a **completion** blocklist to a content filter, use the following cURL command: 
 
@@ -132,9 +134,7 @@ The response code should be `200`.
 
 ### Analyze text with a blocklist
 
-Now you can test out your deployment that has the blocklist. The easiest way to do this is in the [Azure OpenAI Studio](https://oai.azure.com/portal/). If the content was blocked either in prompt or completion, you should see an error message saying the content filtering system was triggered.
-
-For instruction on calling the Azure OpenAI endpoints, visit the [Quickstart](/azure/ai-services/openai/quickstart). 
+Now you can test out your deployment that has the blocklist. For instructions on calling the Azure OpenAI endpoints, visit the [Quickstart](/azure/ai-services/openai/quickstart). 
 
 In the below example, a GPT-35-Turbo deployment with a blocklist is blocking the prompt. The response returns a `400` error. 
 
@@ -249,26 +249,12 @@ If the completion itself is blocked, the response returns `200`, as the completi
 } 
 ```
 
-## Use blocklists in Azure OpenAI Studio
-
-You can also create custom blocklists in the Azure OpenAI Studio as part of your content filtering configurations (public preview). Instructions on how to create custom content filters can be found [here](/azure/ai-services/openai/how-to/content-filters). The following steps show how to create custom blocklists as part of your content filters via Azure OpenAI Studio. 
-
-1. Select Content Filters from the left menu. Select the Blocklists tab next to Content filters tab. Then select Create Blocklist.
-    :::image type="content" source="../media/content-filters/blocklist-select-create.png" alt-text="Screenshot of blocklist create selection." lightbox="../media/content-filters/blocklist-select-create.png":::
-1. Create a name for your blocklist, add a description and select on Create Blocklist.
-    :::image type="content" source="../media/content-filters/create-blocklist.png" alt-text="Screenshot of blocklist name and description." lightbox="../media/content-filters/create-blocklist.png":::
-1. Select your custom blocklist once it's created, and select Add new term. 
-    :::image type="content" source="../media/content-filters/custom-blocklist-add.png" alt-text="Screenshot of custom blocklist add term." lightbox="../media/content-filters/custom-blocklist-add.png":::
-1. Add a term that should be filtered, and select Add term. You can also create a regex.
-    :::image type="content" source="../media/content-filters/custom-blocklist-add-item.png" alt-text="Screenshot of custom blocklist add item." lightbox="../media/content-filters/custom-blocklist-add-item.png":::
-1. You can delete each term in your blocklist. 
-    :::image type="content" source="../media/content-filters/custom-blocklist-edit.png" alt-text="Screenshot of custom blocklist edit screen." lightbox="../media/content-filters/custom-blocklist-edit.png":::
-1. Once the blocklist is ready, navigate to the Content filters (Preview) section and create a new customized content filter configuration. This opens a wizard with several AI content safety components. You can find more information on how to configure the main filters and optional models [here](/azure/ai-services/openai/how-to/content-filters). Go to Add blocklist (Optional).
-1. You'll now see all available blocklists. There are two types of blocklists – the blocklists you created, and prebuilt blocklists that Microsoft provides, in this case a Profanity blocklist (English)
-1. You can now decide which of the available blocklists you would like to include in your content filtering configuration. In the below example, we apply CustomBlocklist1 that we just created. The last step is to review and finish the content filtering configuration by clicking on Next.
-    :::image type="content" source="../media/content-filters/filtering-configuration-manage.png" alt-text="Screenshot of filtering configuration management." lightbox="../media/content-filters/filtering-configuration-manage.png":::
-1. You can always go back and edit your configuration. Once it’s ready, select on Create content filter. The new configuration that includes your blocklists can now be applied to a deployment. Detailed instructions can be found [here](/azure/ai-services/openai/how-to/content-filters).
 
+#### [Azure AI Foundry](#tab/foundry)
+
+[!INCLUDE [use-blocklists](../../../ai-studio/includes/use-blocklists.md)]
+
+---
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ブロックリストの使用に関する更新"
}
```

### Explanation
この変更は、Azure OpenAIにおけるブロックリストの使用方法に関する文書の更新を含んでいます。主な変更点は、Azure OpenAI Studioの名称がAzure AI Foundryに変更されたことです。この修正により、新しいプラットフォームでのブロックリストの作成および適用手順が明確化され、ユーザーは最新のインターフェースを使用してブロックリストを管理できるようになります。

さらに、APIを通じてブロックリストを作成する手順が追加され、具体的な実装手法が強調されています。テスト手順や結果の分析についても言及されており、エラーメッセージの確認方法が具体的に示されています。また、Azure AI Foundryにおけるコンテンツフィルタリングのガイドラインが強化され、ユーザーは新たに追加されたセクションから、ブロックリストの使用に関する具体的な手順や設定方法を探すことができます。

全体として、この更新はAzure OpenAIのユーザーに対し、より一貫した情報と便利なリソースを提供することを目的としています。

## articles/ai-services/openai/includes/dall-e-studio.md{#item-439729}

<details>
<summary>Diff</summary>
````diff
@@ -1,47 +1,31 @@
 ---
-title: 'Quickstart: Generate images with Azure OpenAI Service and Azure OpenAI Studio'
+title: 'Quickstart: Generate images with Azure OpenAI Service and Azure AI Foundry'
 titleSuffix: Azure OpenAI
-description: Learn how to generate images with Azure OpenAI Service in the DALL-E playground (Preview) in Azure OpenAI Studio.
+description: Learn how to generate images with Azure OpenAI Service in the DALL-E playground (Preview) in Azure AI Foundry.
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 08/08/2023
+ms.date: 12/05/2024
 ---
 
-Use this guide to get started generating images with Azure OpenAI in your browser.
+Use this guide to get started generating images with Azure OpenAI in your browser with Azure AI Foundry.
 
 ## Prerequisites
 
-#### [DALL-E 3](#tab/dalle3)
-
-- An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
-- An Azure OpenAI resource created in a supported region. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
-- Then, you need to deploy a `dalle3` model with your Azure resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
-
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
-- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
-
----
+- An Azure OpenAI resource created in a supported region. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
 
-## Go to Azure OpenAI Studio
+## Go to Azure AI Foundry
 
-Browse to [Azure OpenAI Studio](https://oai.azure.com/) and sign in with the credentials associated with your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
+Browse to [Azure AI Foundry](https://oai.azure.com/) and sign in with the credentials associated with your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
 
-#### [DALL-E 3](#tab/dalle3)
+From the Azure AI Foundry landing page, create or select a new project. Navigate to the **Models + endpoints** page on the left nav. Select **Deploy model** and then choose one of the DALL-E models from the list. Complete the deployment process. 
 
-From the Azure OpenAI Studio landing page, select **Images playground** to use the image generation APIs. Select **Settings** near the top of the page and confirm that the **Deployment** dropdown has your DALL-E 3 deployment selected.
-
-#### [DALL-E 2 (preview)](#tab/dalle2)
-
-From the Azure OpenAI Studio landing page, select **Images playground** to use the image generation APIs. Select **Settings** near the top of the page and confirm that the **Deployment** dropdown has the default **DALL-E 2** choice selected.
-
----
+On the model's page, select **Open in playground**.
 
 ## Try out image generation
 
@@ -50,8 +34,6 @@ Start exploring Azure OpenAI capabilities with a no-code approach through the **
 > [!NOTE]
 > The image generation APIs come with a content moderation filter. If Azure OpenAI recognizes your prompt as harmful content, it doesn't return a generated image. For more information, see [Content filtering](../concepts/content-filter.md).
 
-:::image type="content" source="../media/quickstarts/dall-e-studio-new.png" alt-text="Screenshot of the Azure OpenAI Studio landing page showing the DALL-E playground (Preview) with generated images of polar bears." lightbox="../media/quickstarts/dall-e-studio-new.png":::
-
 In the **Images playground**, you can also view Python and cURL code samples, which are prefilled according to your settings. Select **View code** near the top of the page. You can use this code to write an application that completes the same task.
 
 ## Clean up resources
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL-Eスタジオに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるDALL-Eの画像生成に関するガイドラインを更新したものです。主な修正点は、文書内の「Azure OpenAI Studio」が「Azure AI Foundry」に名称変更されたことです。これにより、ユーザーは新しいプラットフォーム上で画像生成機能を利用する方法が示されています。

さらに、DALL-Eモジュールのデプロイ手順が整理され、Azure AI Foundryにおけるプロジェクトの作成やモデルのデプロイに関する具体的な手順が追加されました。各セクションでは、要件や手順が明確に記載され、ユーザーはスムーズにDALL-Eの機能を試すことができるようになっています。また、画像生成APIに関する注意事項や、コンテンツモデレーションフィルターについての情報も更新されています。

最後に、リソースのクリーンアップに関するセクションが含まれており、使用後のリソース管理の重要性が示されています。全体として、このドキュメントの更新は、Azure AI Foundryを介してDALL-Eの機能を活用するためのより明確で使いやすいガイドを提供することを目的としています。

## articles/ai-services/openai/includes/gpt-v-studio.md{#item-dcd50e}

<details>
<summary>Diff</summary>
````diff
@@ -1,32 +1,29 @@
 ---
-title: 'Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the Azure OpenAI Service'
+title: 'Quickstart: Use images and videos in chats with the Azure OpenAI Service'
 titleSuffix: Azure OpenAI
-description: Use this article to get started using Azure AI Foundry to deploy and use the GPT-4 Turbo with Vision model.
+description: Use this article to get started using Azure AI Foundry to deploy and use an image-capable model.
 services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions, ignite-2024
-ms.date: 10/03/2024
+ms.date: 12/05/2024
 ---
 
-Start exploring GPT-4 Turbo with Vision capabilities with a no-code approach through Azure AI Foundry.
+Start using images in your AI chats with a no-code approach through Azure AI Foundry.
 
 ## Prerequisites
 
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
-- An Azure OpenAI Service resource with a GPT-4 Turbo with Vision model deployed. See [GPT-4 and GPT-4 Turbo Preview model availability](../concepts/models.md#gpt-4-and-gpt-4-turbo-model-availability) for available regions. For more information about resource creation, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).
-
-> [!NOTE]
-> It is currently not supported to turn off content filtering for the GPT-4 Turbo with Vision model.
+- An Azure OpenAI Service resource. For more information about resource creation, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).
 
 ## Go to Azure AI Foundry
 
 Browse to [Azure AI Foundry](https://ai.azure.com/) and sign in with the credentials associated with your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
 
-Under **Management** select **Deployments** and **Create** a GPT-4 Turbo with Vision deployment by selecting model name: **"gpt-4"** and model version **"vision-preview"**. For more information about model deployment, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).  
+Create a project or select an existing one. Navigate to the **Models + endpoints** option on the left, and select **Deploy model**. Choose an image-capable deployment by selecting model name: **gpt-4o** or **gpt-4o-mini**. For more information about model deployment, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).  
 
-Under the **Playground** section select **Chat**.
+Select the new deployment and select **Open in playground**.
 
 ## Playground
 
@@ -35,23 +32,19 @@ From this page, you can quickly iterate and experiment with the model's capabili
 For general help with assistant setup, chat sessions, settings, and panels, refer to the [Chat quickstart](/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line&pivots=programming-language-studio). 
 
 
-## Start a chat session to analyze images or video
-
-#### [Image prompts](#tab/image)
+## Start a chat session to analyze images
 
 In this chat session, you're instructing the assistant to aid in understanding images that you input. 
-1. To start, select your GPT-4 Turbo with Vision deployment from the dropdown.
-2. In the **Assistant setup** pane, provide a System Message to guide the assistant. The default System Message is: "You are an AI assistant that helps people find information." You can tailor the System Message to the image or scenario that you're uploading. 
+1. To start, make sure your image-capable deployment is selected in the **Deployment** dropdown.
+2. In the **Setup** pane, provide a System Message to guide the assistant. The default System Message is: "You are an AI assistant that helps people find information." You can tailor the System Message to the image or scenario that you're uploading. 
 
    > [!NOTE]
-    > It is recommended to update the System Message to be specific to the task in order to avoid unhelpful responses from the model.
+    > We recommend you update the System Message to be specific to the task in order to avoid unhelpful responses from the model.
 
 1. Save your changes, and when prompted to confirm updating the system message, select **Continue**.
 1. In the **Chat session** pane, enter a text prompt like "Describe this image," and upload an image with the attachment button. You can use a different text prompt for your use case. Then select **Send**. 
 1. Observe the output provided. Consider asking follow-up questions related to the analysis of your image to learn more.
 
-:::image type="content" source="../media/quickstarts/studio-vision.png" lightbox="../media/quickstarts/studio-vision.png" alt-text="Screenshot of AI Foundry chat playground.":::
-
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryにおける画像およびビデオの利用に関するガイド更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスを使用した画像およびビデオチャット機能に関するガイドの更新を含んでいます。文書のタイトルと説明が改訂され、GPT-4 Turbo with Visionモデルの機能がより一般的な「画像キャパビリティを持つモデル」に焦点を当てるように変更されました。

具体的には、事前条件としてのリソース要件が簡素化され、特定のモデルに対する依存が減少しました。ユーザーは、既存のプロジェクトを使用するか、新しいプロジェクトを作成してモデルのデプロイを選択する際に、より柔軟な選択肢を持つことができます。また、Azure AI Foundryでのデプロイメントの手順がスムーズになり、指定されたモデル名を選択することで、画像分析機能を持つ新しいデプロイメントをすぐに利用できます。

さらに、チャットセッションの設定手順が明確化され、ユーザーが画像を分析する際のフローと注意事項が更新されています。「システムメッセージ」の設定に関する推奨事項も強調されており、モデルの応答の質を向上させるための具体的なアドバイスが含まれています。また、リソースのクリーンアップに関するセクションも維持され、使用後の管理が奨励されています。

全体として、このガイドの更新は、Azure AI Foundryを活用して、画像およびビデオを含むチャット体験をさらに充実させることを目的としています。

## articles/ai-services/openai/includes/model-matrix/datazone-provisioned-managed.md{#item-ae7f5b}

<details>
<summary>Diff</summary>
````diff
@@ -8,9 +8,13 @@ ms.topic: include
 ms.date: 12/05/2024
 ---
 
-| **Region**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-----------------|:--------------------------:|:--------------------------:|:-------------------------------:|
-| eastus2          | ✅                       | ✅                       | ✅                            |
-| spaincentral     | ✅                       | ✅                       | ✅                            |
-| westeurope       | ✅                       | ✅                       | ✅                            |
-| westus3          | ✅                       | ✅                       | ✅                            |
+| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|
+| eastus2            | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                       | ✅                       | ✅                            |
+| northcentralus     | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリックスの地域更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるモデルマトリックスの表を更新したものです。具体的には、GPT-4モデルとGPT-4o-miniモデルのサポートされている地域のリストに新たに2つの地域（フランス中部とドイツ西部）を追加しました。この更新により、ユーザーは新しい地域でもこれらのモデルを利用可能であることが示されています。

表の形式は維持されており、それぞれの地域に対する各モデルの利用可能性が確認できるようになっています。これにより、より多くの地域のユーザーがAzure OpenAIサービスを活用できるようになり、サービスのアクセスビリティが向上します。

また、リージョン名の配置が整えられ、全体的な可読性が改善されました。これは、ユーザーが必要な情報を迅速かつ簡単に見つけられるようにするための重要な改良です。

## articles/ai-services/openai/includes/model-matrix/global-batch.md{#item-929e6a}

<details>
<summary>Diff</summary>
````diff
@@ -9,22 +9,26 @@ ms.date: 11/07/2024
 ---
 
 
-| **Region**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
-|:-----------------|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
-| australiaeast    | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| canadaeast       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| eastus           | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| eastus2          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| francecentral    | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| japaneast        | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| koreacentral     | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| northcentralus   | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| norwayeast       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southcentralus   | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southindia       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| swedencentral    | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| switzerlandnorth | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| uksouth          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westeurope       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus           | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus3          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
\ No newline at end of file
+| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
+|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
+| australiaeast      | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| brazilsouth        | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| canadaeast         | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| eastus             | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| eastus2            | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| francecentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| germanywestcentral | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| japaneast          | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| koreacentral       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| northcentralus     | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| norwayeast         | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| polandcentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southafricanorth   | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southcentralus     | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| southindia         | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| swedencentral      | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| switzerlandnorth   | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| uksouth            | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westeurope         | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westus             | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| westus3            | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルバッチのモデルマトリックス地域の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連するグローバルバッチのモデルマトリックスにおける地域サポートの更新を示しています。具体的には、新たにポーランド中部、南アフリカ北部、ブラジル南部などの地域が追加され、これにより各モデル（如くgpt-4o、gpt-4o-mini、gpt-4等）の利用可能な地域が拡大されました。

表のフォーマットは一貫したまま保たれていますが、追加された地域により、ユーザーはより多くの選択肢を持ち、これらのモデルをグローバルに利用できるようになります。各地域ごとにモデルの対応状況がチェックマーク（✅）で示されており、利便性が向上しました。

全体として、この更新はAzure OpenAIサービスの利用可能性を高め、多様な地域のユーザーが最新のAIモデルを活用できるようにすることを目的としています。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -233,6 +233,22 @@ items:
       href: ./tutorials/embeddings.md
     - name: Fine-tuning GPT-4o mini
       href: ./tutorials/fine-tune.md
+- name: Security & Governance
+  items:
+    - name: Use virtual networks
+      href: ../cognitive-services-virtual-networks.md?context=/azure/ai-services/openai/context/context
+    - name: Encryption of data at rest
+      href: encrypt-data-at-rest.md
+    - name: Managed identity
+      href: ./how-to/managed-identity.md
+    - name: Role-based access control (Azure RBAC)
+      href: ./how-to/role-based-access-control.md
+    - name: Business continuity & disaster recovery (BCDR)
+      href: ./how-to/business-continuity-disaster-recovery.md
+    - name: Use your data
+      items:
+      - name: Network and access configuration
+        href: ./how-to/on-your-data-configuration.md
 - name: Responsible AI
   items:
     - name: Overview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セキュリティとガバナンスに関するセクションの追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連する目次ファイル（toc.yml）に「セキュリティとガバナンス」という新しいセクションを追加したものです。このセクションには、以下のような項目が含まれています。

- **仮想ネットワークの使用**: Azure OpenAIサービスの仮想ネットワーク設定に関するガイド。
- **データの暗号化**: 従来のデータ保存の暗号化方法について。
- **マネージドアイデンティティ**: Azureにおけるマネージドアイデンティティの使用法。
- **ロールベースのアクセス制御（Azure RBAC）**: アクセス管理とセキュリティに関する方法。
- **事業継続とディザスタリカバリ（BCDR）**: システムの継続性を確保するための戦略。
- **データの使用**: データのネットワークおよびアクセス設定に関する詳細。

このように新たに項目が追加されることで、ユーザーはAzure OpenAIサービスの利用に関するセキュリティおよびガバナンスの観点を理解しやすくなります。目次の変更はこの分野における重要な情報提供を強化し、ユーザーに対してより多くのサポートを提供することを目的としています。


