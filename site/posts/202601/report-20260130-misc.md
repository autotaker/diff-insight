---
date: '2026-01-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:cac9cb3...MicrosoftDocs:d1b059c
summary: このコード変更により、Azure Language StudioからMicrosoft Foundryへの移行に関するガイドが更新されました。主なポイントとして、移行開始日として2026年2月16日が明示され、移行プロセスの簡素化や新しいトラブルシューティングセクションの追加が行われています。特に破壊的な変更はないものの、指示が簡素化され、プロジェクトの再作成やリソース管理に関する注意点が追加されています。これにより、ユーザーは計画的かつ容易に移行を進めることができ、より良いユーザーエクスペリエンスが提供されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:cac9cb3...MicrosoftDocs:d1b059c){target="_blank"}

# Highlights
このコード変更では、Azure Language StudioからMicrosoft Foundryへの移行に関するガイドが更新されました。主な新機能と変更点として、移行の開始日が2026年2月16日と明記され、プロジェクトの再作成やリソース管理において重要な注意事項が追加されています。

## New features
- 移行開始日の強調表示（2026年2月16日）
- 移行プロセスの簡素化とわかりやすさの改善
- 新しいトラブルシューティングセクションの追加

## Breaking changes
特に破壊的な変更は報告されていませんが、ガイド内の指示が簡素化されているため、従来の手順とは異なる点があります。

## Other updates
- ステップバイステップの指示の再構築
- Microsoft Foundryとの接続方法および移行手順の詳細化
- 移行後に確認すべき事項の追加

# Insights
このコード変更は、Azure Language StudioからMicrosoft Foundryへの移行プロセスをスムーズにするための重要なアップデートです。従来のAzure Languageリソースを新しいプラットフォームであるMicrosoft Foundryに適応させるステップが明確化されたことによって、ユーザーは計画的かつ容易に移行を行える基盤が整いました。

特に、移行開始日をしっかりと明示し、ユーザーがその期限に向けて準備を整えやすくする工夫がなされています。また、プロジェクトの再作成やリソース管理における注意点を明確にすることで、ユーザーが移行中に遭遇する可能性のあるリスクを最小限に抑える内容となっています。

さらに、新たに追加されたトラブルシューティングセクションは、移行作業中に生じうるさまざまな問題に迅速に対応できるようサポートしており、ユーザーエクスペリエンスの向上に繋がっています。ガイド全体の指示がより簡素化されていることで、新旧ユーザーを問わず、移行ガイドが利用しやすくなっている点も特筆すべきです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [migration-studio-to-foundry.md](#item-12d575) | minor update | Language StudioからMicrosoft Foundryへの移行に関するガイドの改訂 | modified | 119 | 112 | 231 | 


# Modified Contents
## articles/ai-services/language-service/migration-studio-to-foundry.md{#item-12d575}

<details>
<summary>Diff</summary>
````diff
@@ -12,145 +12,72 @@ ms.author: lajanuar
 <!-- markdownlint-disable MD025 -->
 # Migrate from Language Studio to Microsoft Foundry
 
-Azure Language Studio retires on February 16, 2026 and is no longer available after this date. All existing capabilities, along with new feature enhancements, are fully available in Microsoft Foundry. This guide provides step-by-step migration instructions to ensure uninterrupted access to Azure AI Language features and seamless project continuity within the Foundry environment.
-
-> [!IMPORTANT]
->
-> **Post-retirement project recreation**. After the February 16, 2026 retirement date, Language Studio export functionality is no longer available. However, you can recreate your custom projects directly in Microsoft Foundry:
->
-> * **Existing Azure Language resources**. You can access and continue to use your current Azure Language resources within the Microsoft Foundry portal by creating a **Foundry hub** and an associated **hub-based project**. For more information, *see* [Create a hub in the Azure portal](/azure/ai-foundry/how-to/create-azure-ai-resource?view=foundry-classic&preserve-view=true&tabs=portal#create-a-hub-in-the-azure-portal).
->
-> * **Existing Foundry resource-based projects**. You can access your current **Foundry projects** directly in the Microsoft Foundry portal. Alternatively, create a new project and transfer your project assets to the new environment. For more information, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects?view=foundry-classic&preserve-view=true&tabs=foundry).
+Azure Language Studio will migrate to Microsoft Foundry on February 16, 2026. All existing capabilities, along with new feature enhancements, are fully available in Microsoft Foundry. After February 16, 2026, Language Studio will no longer be available, but none of your existing projects, data, or service endpoints are impacted. This guide provides step-by-step migration instructions to ensure uninterrupted access to Azure AI Language features and seamless project continuity within the Foundry environment.
 
 ## Why migrate to Microsoft Foundry?
 
 Microsoft Foundry offers a unified platform for building, managing, and deploying AI solutions with a wide array of models and tools. Migrating to Foundry provides the following benefits:
 
 * **Unified development experience**. Access all Azure AI Language features alongside other AI services in one environment.
-* **Enhanced capabilities**. Use features like **Quick Deploy** for rapid fine-tuning and **Suggest Utterances** to expand training data with generative AI.
+* **Enhanced capabilities**. Use features like **Quick Deploy** for rapid fine-tuning with generative AI.
 * **Continuous updates**. Benefit from new features continually added to Foundry.
 * **Integration with Foundry Tools**. Build conversational AI applications using the Azure Language `MCP` server, Intent Routing agent, and Exact Question Answering agent.
 
-## Migration overview
-
-The migration process consists of the following steps:
-
-1. [**Export your custom projects from Language Studio.**](#step-1-export-your-projects-from-language-studio)
-1. [**Set up your Foundry environment.**](#step-2-set-up-your-foundry-environment)
-1. [**Import your projects into Foundry.**](#step-3-import-your-projects-into-foundry)
-1. [**Validate and test your migrated projects.**](#step-4-validate-and-test-your-migrated-projects)
-
 ## Prerequisites
 
-> [!NOTE]
-> In the Foundry, a **fine-tuning task** serves as your workspace when customizing your custom models. Previously, a **fine-tuning task** was referred to as a project. You might encounter both terms used interchangeably in some documentation.
-
 **Before you begin the migration process, ensure that the following resources and permissions are in place to complete the steps in this guide:**
 
 * **Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
 * **Azure account** with a role that allows you to create resources, such as **Contributor** or **Owner** at the subscription level.
 
-## Step 1: Export your projects from Language Studio
-
-Before migrating to Microsoft Foundry, export all custom projects you want to transfer. The export process preserves your project configuration, training data, and model settings for import into Foundry:
-
-:::image type="content" source="media/export-studio-project.png" alt-text="Screenshot of Export Studio Project button.":::
-
-### Export a Custom Question Answering project
-
-1. Sign in to [Language Studio](https://language.azure.com/).
-1. Select the Azure Language resource containing the project you want to export.
-1. Navigate to **Custom Question Answering**.
-1. On the **Projects** page, select the project to export.
-1. Choose the export format (**Excel** or **TSV**). The file is exported as a **`.zip`** file containing your project contents.
-
-### Export a Conversational Language Understanding, Custom Named Entity Recognition, Custom Text Classification, or Orchestration Workflow project
-
-1. Sign in to [Language Studio](https://language.azure.com/).
-1. Select the Azure Language resource containing your CLU project.
-1. Navigate to your project.
-1. On the project home page, select your project from the right page ribbon area.
-1. Select **Download config file** to download the project as a **`config.json`** file.
-
-## Step 2: Set up your Foundry environment
-
-Before migrating your Azure Language projects to Microsoft Foundry, you need to complete several configuration tasks:
-
-* **Configure Azure resources**. Create the required Foundry or Language resources in the Azure portal.
-* **Establish access control**. Assign the appropriate role-based access control (RBAC) permissions to your resources.
-* **Verify region availability**. Confirm that your target capabilities are supported in your chosen Azure region.
-
-The following sections outline the necessary prerequisites and permissions for both custom model training (fine-tuning) and pretrained model access.
-
-### Custom model training (fine-tuning) in Microsoft Foundry
-
-Microsoft Foundry supports custom model training (fine-tuning) for Azure AI Language capabilities using two resource configurations:
+## Migration overview
 
-* **Foundry resource (recommended)**. Create and use a Foundry resource directly, which provides access to both Foundry classic and new Foundry experiences.
-* **Language resource**. Use an existing Azure Language resource connected to a Foundry hub-based project, which is supported in Foundry classic only.
+You can migrate to Microsoft Foundry using one of two approaches:
 
-Choose the tab that matches your preferred resource configuration.
+* **[Option I: Use your existing Language resource](#option-i-start-using-foundry-with-an-existing-language-resource)**. Create a Foundry hub, connect your existing Azure Language resource, and access your projects directly in Foundry. This approach preserves your current resource configuration and requires no data export or import.
 
-### [**Foundry resource (recommended)**](#tab/foundry)
+* **[Option II: Migrate to a new Foundry resource](#option-ii-migrate-to-a-new-foundry-resource)**. Export your projects from Language Studio and import them into a new Foundry resource. This approach consolidates your AI capabilities into a single resource and provides access to both Foundry classic and the new Foundry experiences.
 
-> [!IMPORTANT]
-> This configuration is supported in both Foundry classic and new Foundry.
-> Microsoft Foundry can automatically provision and manage Foundry resources. However, manually configuring your Foundry resource for Language capabilities in the Azure portal ensures correct role-based access control (RBAC) assignments, managed identity configurations, and network security settings.
->
 
-### Create a Foundry resource
 
-To use Azure AI Language capabilities with a Foundry resource, you need both the resource and an associated Foundry project. Set up these resources using either of the following approaches:
-
-* **Azure portal**. Create a Foundry resource first, then create an associated Foundry project. This approach provides explicit control over resource configuration settings. For step-by-step instructions, *see* [Create a Foundry resource in the Azure portal](/azure/ai-services/multi-service-resource?pivots=azportal#create-a-new-microsoft-foundry-resource).
+---
 
-* **Microsoft Foundry portal**. Create a Foundry project directly, which automatically provisions the underlying Foundry resource. This approach streamlines setup by handling resource creation automatically. For step-by-step instructions, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects?view=foundry-classic&preserve-view=true&tabs=foundry).
 
-> [!IMPORTANT]
-> **Custom NER (CNER)** requires a storage account to be linked to the Foundry resource during initial resource creation. To establish this link, you must configure the Foundry resource in the [Azure portal](https://portal.azure.com/).
 
-|Capability|Required prerequisites|Region support|
-|---|---|---|
-|[**Conversational Language Understanding (CLU)**](conversational-language-understanding/quickstart.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for Conversational Language Understanding](concepts/regional-support.md#conversational-language-understanding-and-orchestration-workflow).|
-|[**Custom Question Answering (CQA)**](question-answering/quickstart/sdk.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.</br>&bullet; Azure AI Search resource connected to your project via the Foundry Management Center. For more information, *see* [Create a new connection](/azure/ai-foundry/how-to/connections-add?view=foundry-classic&preserve-view=true&tabs=foundry-portal#create-a-new-connection).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
-|[**Custom Question Answering agent**](question-answering/how-to/deploy-agent.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.</br>&bullet; Azure AI Search resource connected to your project via the Foundry Management Center. For more information, *see* [Create a new connection](/azure/ai-foundry/how-to/connections-add?view=foundry-classic&preserve-view=true&tabs=foundry-portal#create-a-new-connection).</br>&bullet; Deployed knowledge base.</br>&bullet; Deployed Azure OpenAI model in Microsoft Foundry.</br>&bullet; API key connected to your project.|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
-|[**Custom Named Entity Recognition (CNER)**](custom-named-entity-recognition/quickstart.md)|&bullet; Language resource with a storage account **linked during resource creation** in the Foundry portal.</br>&bullet; Foundry project created in the Azure portal.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for CNER](concepts/regional-support.md#custom-named-entity-recognition).|
-|[**Orchestration Workflow**](orchestration-workflow/quickstart.md)|&bullet; Foundry resource and Foundry project, or Language resource and Foundry hub-based project.</br>&bullet; A `CLU` or `CQA` project created in the same resource.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for Orchestration workflow](concepts/regional-support.md#conversational-language-understanding-and-orchestration-workflow).|
+## Option I: Start using Foundry with an existing Language resource
 
-### [**Language resource**](#tab/studio)
+If you have an existing Azure Language resource with custom projects, you can continue using it within Microsoft Foundry by creating a Foundry hub and connecting your resource. This approach preserves your current resource configuration and allows you to access your projects in Foundry without exporting or reimporting data.
 
 > [!IMPORTANT]
 > This configuration is supported only in Foundry classic.
 > Microsoft Foundry can automatically provision and manage Azure Language resources. However, manually configuring your hub-based Foundry resource in the Azure portal ensures correct role-based access control (RBAC) assignments, managed identity configurations, and network security settings.
 
-### Create a Foundry hub and project
+### Step 1: Create a Foundry hub and project
 
 To use Azure AI Language capabilities with a Language resource, you need a Foundry hub and an associated hub-based project. Set up these resources using either of the following approaches:
 
 * **Azure portal**. Create a hub first, then create an associated project. This approach provides explicit control over resource configuration settings. For step-by-step instructions, *see* [Create a hub in the Azure portal](/azure/ai-foundry/how-to/create-azure-ai-resource?view=foundry-classic&preserve-view=true&tabs=portal#create-a-hub-in-the-azure-portal). After creating your hub, navigate to your hub resource, select **Projects** or **Management center** under **Resource management**, and then select **+ New project**.
 
 * **Microsoft Foundry portal**. Create a hub-based project directly in Microsoft Foundry, which automatically provisions the underlying hub. This approach streamlines setup by handling hub creation automatically. For step-by-step instructions, *see* [Create a project](/azure/ai-foundry/how-to/create-projects?view=foundry-classic&preserve-view=true&tabs=foundry).
 
-### Confirm prerequisites and region support
+### Step 2: Confirm prerequisites and region support
 
 The following table lists the custom capabilities available in Microsoft Foundry along with their required prerequisites and supported regions. Ensure these prerequisites are in place before proceeding with the migration.
 
 |Capability|Required prerequisites|Region support|
 |---|---|---|
 |[**Conversational Language Understanding (CLU)**](conversational-language-understanding/quickstart.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for CLU](concepts/regional-support.md).|
 |[**Custom Question Answering (CQA)**](question-answering/quickstart/sdk.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.</br>&bullet; Azure AI Search resource connected to your hub or hub-based project via the Foundry Management Center. For more information, *see* [Create a new connection](/azure/ai-foundry/how-to/connections-add?view=foundry-classic&preserve-view=true&tabs=foundry-portal#create-a-new-connection).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
-|[**Custom Question Answering agent**](question-answering/how-to/deploy-agent.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.</br>&bullet; Azure AI Search resource connected to your hub or hub-based project via the Foundry Management Center. For more information, *see* [Create a new connection](/azure/ai-foundry/how-to/connections-add?view=foundry-classic&preserve-view=true&tabs=foundry-portal#create-a-new-connection).</br>&bullet; Deployed knowledge base.</br>&bullet; Deployed Azure OpenAI model in Microsoft Foundry.</br>&bullet; API key connected to your hub or hub-based project.|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
-|[**Custom Named Entity Recognition (CNER)**](custom-named-entity-recognition/quickstart.md)|&bullet; Language resource with a storage account linked during resource creation.</br>&bullet; Foundry hub-based project created in the Azure portal.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for CNER](concepts/regional-support.md).|
 |[**Orchestration workflow**](orchestration-workflow/quickstart.md)|&bullet; Foundry resource and Foundry project, or Language resource and Foundry hub-based project.</br>&bullet; A `CLU` or `CQA` project created in the same resource.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for Orchestration workflow](concepts/regional-support.md).|
+|[**Custom Named Entity Recognition (CNER)**](custom-named-entity-recognition/quickstart.md)|&bullet; Language resource with a storage account linked during resource creation.</br>&bullet; Foundry hub-based project created in the Azure portal.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for CNER](concepts/regional-support.md).|
 
-### Connect your Azure Language resource to your Foundry hub
+### Step 3: Connect your Azure Language resource to your Foundry hub
 
->[!IMPORTANT]
+> [!IMPORTANT]
 > This step is required only if you're using an existing Azure Language resource with a Foundry hub-based project.
->
 
-To access and manage your existing Language resource projects in Microsoft Foundry, you must establish a connection between your Azure Language resource and your Foundry Hub. This connection enables Microsoft Foundry to authenticate with your resources and provides access to your custom models, training data, and deployed endpoints.
+To access and manage your existing Language resource projects in Microsoft Foundry, you must establish a connection between your Azure Language resource and your Foundry hub. This connection enables Microsoft Foundry to authenticate with your resources and provides access to your custom models, training data, and deployed endpoints.
 
 1. Sign in to [**Microsoft Foundry**](https://ai.azure.com/) using your Azure account.
 1. Select or create the project where you want to connect your Language resource.
@@ -162,35 +89,72 @@ To access and manage your existing Language resource projects in Microsoft Found
 
 For more information, *see* [Connect Foundry Tools to a Foundry project](/azure/ai-foundry/how-to/connections-add?view=foundry-classic&preserve-view=true&tabs=foundry-portal).
 
+### Step 4: Validate and test your migrated projects
+
+After importing your projects, validate that the migration is successful:
+
+1. **Review project contents**. Verify that all intents, entities, question-answer pairs, and training data are correctly imported.
+1. **Test your models**. Use the Foundry test panel to validate model responses.
+1. **Deploy and monitor**. Deploy your models and monitor performance to ensure they function as expected.
+
 ---
 
-### Pretrained models (prebuilt) supported in Microsoft Foundry
+## Option II: Migrate to a new Foundry resource
 
-The following table lists the pretrained (prebuilt) capabilities available in Microsoft Foundry, required prerequisites, and supported regions. Ensure these prerequisites are in place before proceeding with the migration.
+This option enables you to create a new Foundry resource and migrate your projects by exporting them from Language Studio and importing them into the new environment. With a Foundry resource, you can access both Foundry classic and the new Foundry experiences, and take advantage of the latest features and unified resource management capabilities.
 
-|Capability|Input|Region support|
-|---|---|---|
-|**Language detection (Foundry classic)**|On the Playground tab, you can choose a text sample from the drop-down menu, choose the paperclip icon to upload your own text, or type your text directly into the sample window. For more information, *see* [**Language detection in Foundry**](language-detection/quickstart.md).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
-|**Language detection (Foundry new)**|On the Playground tab, you can choose a text sample from the drop-down menu, choose the paperclip icon to upload your own text, or type your text directly into the sample window. For more information, *see* [**Language detection in Foundry**](language-detection/quickstart.md).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
-|**Key phrase extraction (Foundry classic)**|On the Playground tab, you can upload a file or type text directly into the sample window. For more information, *see* [**Key phrase extraction**](key-phrase-extraction/quickstart.md).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
-|**Named Entity Recognition (Foundry classic)**|On the Playground tab, you can upload a file or type text directly into the sample window. For more information, *see* [**Named Entity Recognition in Foundry**](named-entity-recognition/quickstart.md).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
-|**PII detection for text or conversation (Foundry classic)**|On the Playground tab, you can choose a text sample from the drop-down menu, choose the paperclip icon to upload your own text, or type your text directly into the sample window. For more information, *see* [**PII detection in Foundry**](personally-identifiable-information/quickstart.md).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
-|**PII detection for text (Foundry new)**|On the Playground tab, you can choose a text sample from the drop-down menu, choose the paperclip icon to upload your own text, or type your text directly into the sample window. For more information, *see* [**PII detection in Foundry**](personally-identifiable-information/quickstart.md).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
-|**Sentiment analysis (Foundry classic)**|On the Playground tab, you can upload a file or type text directly into the sample window. For more information, *see* [**Sentiment analysis in Foundry**](sentiment-opinion-mining/quickstart.md).|Available in all [supported Azure regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=cognitive-services).|
-|**Summarization (Foundry classic)**</br></br>&bullet;    **Conversation**</br>&bullet;    **Call center**</br>&bullet;    **Text**|On the Playground tab, you can choose a text sample from the drop-down menu, choose the paperclip icon to upload your own text, or type your text directly into the sample window. For more information, *see* [**Summarization in Foundry**](summarization/quickstart.md).|Region support is limited to select Azure regions. For more information, *see* [Region support for summarization](concepts/regional-support.md#summarization)|
-|**Text Analytics for health (Foundry classic)**|On the Playground tab, you can upload a file or type text directly into the sample window. A storage account isn't required. For more information, *see* [**Text Analytics for health in Foundry**](text-analytics-for-health/quickstart.md).|Available in all [supported Azure regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=cognitive-services).|
+### Step 1: Export your projects from Language Studio
 
-> [!NOTE]
-> The following Azure AI Language features aren't available in the Microsoft Foundry portal. To use these capabilities, call the [**Azure Language REST API**](/rest/api/language/) directly:
->
-> * [**Custom Text Classification**](/azure/ai-services/language-service/custom-text-classification/quickstart?tabs=multi-classification). For regional availability, *see* [Region support for Custom Text Classification](concepts/regional-support.md).
-> * [**Entity linking**](/azure/ai-services/language-service/entity-linking/quickstart?tabs=windows&pivots=rest-api). Available in all [supported Azure regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=cognitive-services).
+Before migrating to Microsoft Foundry, export all custom projects you want to transfer. The export process preserves your project configuration, training data, and model settings for import into Foundry:
+
+:::image type="content" source="media/export-studio-project.png" alt-text="Screenshot of Export Studio Project button.":::
+
+#### Export a Custom Question Answering project
+
+1. Sign in to [Language Studio](https://language.azure.com/).
+1. Select the Azure Language resource containing the project you want to export.
+1. Navigate to **Custom Question Answering**.
+1. On the **Projects** page, select the project to export.
+1. Choose the export format (**Excel** or **TSV**). The file is exported as a **`.zip`** file containing your project contents.
+
+#### Export a Conversational Language Understanding, Custom Named Entity Recognition, Custom Text Classification, or Orchestration Workflow project
+
+1. Sign in to [Language Studio](https://language.azure.com/).
+1. Select the Azure Language resource containing your CLU project.
+1. Navigate to your project.
+1. On the project home page, select your project from the right page ribbon area.
+1. Select **Download config file** to download the project as a **`config.json`** file.
+
+### Step 2: Set up your Foundry environment
+
+Before migrating your Azure Language projects to Microsoft Foundry, you need to complete several configuration tasks:
+
+* **Configure Azure resources**. Create the required Foundry or Language resources in the Azure portal.
+* **Establish access control**. Assign the appropriate role-based access control (RBAC) permissions to your resources.
+* **Verify region availability**. Confirm that your target capabilities are supported in your chosen Azure region.
+
+The following sections outline the necessary prerequisites and permissions for custom model training (fine-tuning) in Microsoft Foundry.
+
+> [!IMPORTANT]
+> This configuration is supported in both Foundry classic and new Foundry.
+> Microsoft Foundry can automatically provision and manage Foundry resources. However, manually configuring your Foundry resource for Language capabilities in the Azure portal ensures correct role-based access control (RBAC) assignments, managed identity configurations, and network security settings.
+
+### Create a Foundry resource
+
+To use Azure AI Language capabilities with a Foundry resource, you need both the resource and an associated Foundry project. Set up these resources using either of the following approaches:
+
+* **Azure portal**. Create a Foundry resource first, then create an associated Foundry project. This approach provides explicit control over resource configuration settings. For step-by-step instructions, *see* [Create a Foundry resource in the Azure portal](/azure/ai-services/multi-service-resource?pivots=azportal#create-a-new-microsoft-foundry-resource).
+
+* **Microsoft Foundry portal**. Create a Foundry project directly, which automatically provisions the underlying Foundry resource. This approach streamlines setup by handling resource creation automatically. For step-by-step instructions, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects?view=foundry-classic&preserve-view=true&tabs=foundry).
+
+> [!IMPORTANT]
+> **Custom NER (CNER)** requires a storage account to be linked to the Foundry resource during initial resource creation. To establish this link, you must configure the Foundry resource in the [Azure portal](https://portal.azure.com/).
 
-## Step 3: Import your projects into Foundry
+### Step 3: Import your projects into Foundry
 
 After you connect your Language resource or Foundry resource, your existing projects are accessible within Foundry. For new projects or to import exported projects:
 
-### Import Custom Named Entity Recognition (CNER) project assets
+#### Import Custom Named Entity Recognition (CNER) project assets
 
 1. In the Azure portal, grant the Foundry managed identity permissions to the storage account by assigning the **Storage Blob Data Contributor** role under **Access Control (IAM)**.
 1. Sign in to the [Microsoft Foundry portal](https://ai.azure.com/) and select your project.
@@ -200,7 +164,7 @@ After you connect your Language resource or Foundry resource, your existing proj
 
 You can now train and deploy your `CNER` project using the **Getting started** workflow in Foundry.
 
-### Import a Custom Question Answering (CQA) project
+#### Import a Custom Question Answering (CQA) project
 
 1. In Foundry, navigate to your project.
 1. Select **Fine-tuning** from the left navigation pane.
@@ -214,7 +178,7 @@ You can now train and deploy your `CNER` project using the **Getting started** w
 
 After adding your source files, you can train and deploy the `CQA` project using the **Getting started** workflow in Foundry.
 
-### Import a Conversational Language Understanding (CLU) project
+#### Import a Conversational Language Understanding (CLU) project
 
 1. In Foundry, navigate to your project.
 1. Select **Fine-tuning** from the left navigation pane.
@@ -227,7 +191,7 @@ After adding your source files, you can train and deploy the `CQA` project using
 
 After importing, you can train and deploy your `CLU` project using the **Getting started** workflow in Foundry.
 
-### Import an Orchestration Workflow project
+#### Import an Orchestration Workflow project
 
 1. In Foundry, navigate to your project.
 1. Select **Fine-tuning** from the left navigation pane.
@@ -239,14 +203,57 @@ After importing, you can train and deploy your `CLU` project using the **Getting
 
 After importing, you can train and deploy the Orchestration project using the **Getting started** workflow in Foundry.
 
-## Step 4: Validate and test your migrated projects
+### Step 4: Validate and test your imported projects
 
 After importing your projects, validate that the migration is successful:
 
 1. **Review project contents**. Verify that all intents, entities, question-answer pairs, and training data are correctly imported.
 1. **Test your models**. Use the Foundry test panel to validate model responses.
 1. **Deploy and monitor**. Deploy your models and monitor performance to ensure they function as expected.
 
+> [!IMPORTANT]
+>
+> **Post-retirement project recreation**. After the February 16, 2026 retirement date, Language Studio export functionality is no longer available. However, you can recreate your custom projects directly in Microsoft Foundry:
+>
+> * **Existing Azure Language resources**. You can access and continue to use your current Azure Language resources within the Microsoft Foundry portal by creating a **Foundry hub** and an associated **hub-based project**. For more information, *see* [Create a hub in the Azure portal](/azure/ai-foundry/how-to/create-azure-ai-resource?view=foundry-classic&preserve-view=true&tabs=portal#create-a-hub-in-the-azure-portal).
+>
+> * **Existing Foundry resource-based projects**. You can access your current **Foundry projects** directly in the Microsoft Foundry portal. Alternatively, create a new project and transfer your project assets to the new environment. For more information, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects?view=foundry-classic&preserve-view=true&tabs=foundry).
+
+#### Pretrained models (prebuilt) supported in Microsoft Foundry
+
+The following table lists the pretrained (prebuilt) capabilities available in Microsoft Foundry, required prerequisites, and supported regions. Ensure these prerequisites are in place before proceeding with the migration.
+
+|Capability|Input|Region support|
+|---|---|---|
+|**Language detection (Foundry classic)**|On the Playground tab, you can choose a text sample from the drop-down menu, choose the paperclip icon to upload your own text, or type your text directly into the sample window. For more information, *see* [**Language detection in Foundry**](language-detection/quickstart.md).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
+|**Language detection (Foundry new)**|On the Playground tab, you can choose a text sample from the drop-down menu, choose the paperclip icon to upload your own text, or type your text directly into the sample window. For more information, *see* [**Language detection in Foundry**](language-detection/quickstart.md).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
+|**Key phrase extraction (Foundry classic)**|On the Playground tab, you can upload a file or type text directly into the sample window. For more information, *see* [**Key phrase extraction**](key-phrase-extraction/quickstart.md).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
+|**Named Entity Recognition (Foundry classic)**|On the Playground tab, you can upload a file or type text directly into the sample window. For more information, *see* [**Named Entity Recognition in Foundry**](named-entity-recognition/quickstart.md).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
+|**PII detection for text or conversation (Foundry classic)**|On the Playground tab, you can choose a text sample from the drop-down menu, choose the paperclip icon to upload your own text, or type your text directly into the sample window. For more information, *see* [**PII detection in Foundry**](personally-identifiable-information/quickstart.md).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
+|**PII detection for text (Foundry new)**|On the Playground tab, you can choose a text sample from the drop-down menu, choose the paperclip icon to upload your own text, or type your text directly into the sample window. For more information, *see* [**PII detection in Foundry**](personally-identifiable-information/quickstart.md).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
+|**Sentiment analysis (Foundry classic)**|On the Playground tab, you can upload a file or type text directly into the sample window. For more information, *see* [**Sentiment analysis in Foundry**](sentiment-opinion-mining/quickstart.md).|Available in all [supported Azure regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=cognitive-services).|
+|**Summarization (Foundry classic)**</br></br>&bullet;    **Conversation**</br>&bullet;    **Call center**</br>&bullet;    **Text**|On the Playground tab, you can choose a text sample from the drop-down menu, choose the paperclip icon to upload your own text, or type your text directly into the sample window. For more information, *see* [**Summarization in Foundry**](summarization/quickstart.md).|Region support is limited to select Azure regions. For more information, *see* [Region support for summarization](concepts/regional-support.md#summarization)|
+|**Text Analytics for health (Foundry classic)**|On the Playground tab, you can upload a file or type text directly into the sample window. A storage account isn't required. For more information, *see* [**Text Analytics for health in Foundry**](text-analytics-for-health/quickstart.md).|Available in all [supported Azure regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=cognitive-services).|
+
+#### Custom features supported in Microsoft Foundry
+
+> [!NOTE]
+> In the Foundry, a **fine-tuning task** serves as your workspace when customizing your custom models. Previously, a **fine-tuning task** was referred to as a project. You might encounter both terms used interchangeably in some documentation.
+
+|Capability|Required prerequisites|Region support|
+|---|---|---|
+|[**Conversational Language Understanding (CLU)**](conversational-language-understanding/quickstart.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for Conversational Language Understanding](concepts/regional-support.md#conversational-language-understanding-and-orchestration-workflow).|
+|[**Custom Question Answering (CQA)**](question-answering/quickstart/sdk.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.</br>&bullet; Azure AI Search resource connected to your project via the Foundry Management Center. For more information, *see* [Create a new connection](/azure/ai-foundry/how-to/connections-add?view=foundry-classic&preserve-view=true&tabs=foundry-portal#create-a-new-connection).|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
+|[**Custom Question Answering agent**](question-answering/how-to/deploy-agent.md)|&bullet; Foundry resource and Foundry project created in the Azure portal.</br>&bullet; Azure AI Search resource connected to your project via the Foundry Management Center. For more information, *see* [Create a new connection](/azure/ai-foundry/how-to/connections-add?view=foundry-classic&preserve-view=true&tabs=foundry-portal#create-a-new-connection).</br>&bullet; Deployed knowledge base.</br>&bullet; Deployed Azure OpenAI model in Microsoft Foundry.</br>&bullet; API key connected to your project.|Available in supported Azure regions. For more information, *see* [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).|
+|[**Custom Named Entity Recognition (CNER)**](custom-named-entity-recognition/quickstart.md)|&bullet; Language resource with a storage account **linked during resource creation** in the Foundry portal.</br>&bullet; Foundry project created in the Azure portal.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for CNER](concepts/regional-support.md#custom-named-entity-recognition).|
+|[**Orchestration Workflow**](orchestration-workflow/quickstart.md)|&bullet; Foundry resource and Foundry project, or Language resource and Foundry hub-based project.</br>&bullet; A `CLU` or `CQA` project created in the same resource.|Limited to select Azure regions. Some regions support both authoring and prediction; others support prediction only. For more information, *see* [Region support for Orchestration workflow](concepts/regional-support.md#conversational-language-understanding-and-orchestration-workflow).|
+
+> [!NOTE]
+> The following Azure AI Language features aren't available in the Microsoft Foundry portal. To use these capabilities, call the [**Azure Language REST API**](/rest/api/language/) directly:
+>
+> * [**Custom Text Classification**](/azure/ai-services/language-service/custom-text-classification/quickstart?tabs=multi-classification). For regional availability, *see* [Region support for Custom Text Classification](concepts/regional-support.md).
+> * [**Entity linking**](/azure/ai-services/language-service/entity-linking/quickstart?tabs=windows&pivots=rest-api). Available in all [supported Azure regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=cognitive-services).
+
 ## Troubleshooting
 
 If you encounter issues during the migration process, use the following guidance to diagnose and resolve common problems. For issues not covered here, consult the [Azure AI Language documentation](overview.md) or contact [Azure Support](https://azure.microsoft.com/support/).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Language StudioからMicrosoft Foundryへの移行に関するガイドの改訂"
}
```

### Explanation
この変更は、Azure Language StudioからMicrosoft Foundryへの移行ガイドに関する文書の更新を含んでいます。主な更新内容として、移行が2026年2月16日に始まることの強調、プロジェクトの再作成やリソースの管理に関する重要な注意事項が追加されました。文書全体で、ステップバイステップの指示が簡素化され、わかりやすくなるように再構築されています。具体的には、既存のAzure LanguageリソースをMicrosoft Foundryに接続する方法、新しいFoundryリソースを使用したプロジェクトの移行方法、および移行後に確認するべきステップが詳細に説明されています。また、移行の過程で遭遇する可能性のある問題に対処するためのトラブルシューティングセクションが追加されています。この一連の変更により、移行のプロセスがよりスムーズで理解しやすくなることを目的としています。


