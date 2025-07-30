---
date: '2025-07-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e0fd9e5...MicrosoftDocs:c2bb090
summary: このドキュメントの変更では、Azure AI Foundry関連のセクションが更新され、新機能の追加や内容の簡潔化が行われました。ファインチューニングタスクに関する新しい画像が追加され、プロジェクト設定のインポート・エクスポート方法が明示化されることで利便性が向上しています。特に破壊的な変更はなく、情報の削除により内容が整理されています。全体として、ユーザビリティの向上と新規ユーザーのナビゲーション改善が狙いです。この更新により、必要な情報にアクセスしやすくなり、Azure
  AI Foundryの利用が効率的になることが期待されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e0fd9e5...MicrosoftDocs:c2bb090){target="_blank"}

<format>
# ハイライト
このドキュメントの変更では、Azure AI Foundry関連のいくつかのセクションで説明や手順が更新されました。新機能としては、画像の追加やファインチューニング関連の内容充実があります。一部情報の削除により内容の簡潔化も進められています。

## 新機能
- ファインチューニングタスクの開始に関する新しい画像が追加。
- プロジェクト設定のインポート・エクスポート方法が明示され、利便性が向上。

## 破壊的変更
この更新には特に破壊的変更はありませんが、情報の削除により内容が簡潔化されています。

## その他の更新
- Azureリソース構成方法やプロジェクト作成、モデル訓練手順の具体化。
- エージェント関連情報の削除により情報が精査され、読み手の負担を軽減。

# インサイト
このコード変更は、Azure AI Foundryのドキュメントにおけるユーザビリティの向上を目指したものです。Azureリソースとその関連機能をより直感的に理解できるように、各セクションの内容が整理されました。

新たに追加された画像や、ファインチューニングタスク関連の更新により、特に新規ユーザーにとってのナビゲーションが改善されています。手順を視覚的に支持するためのビジュアルコンテンツは、ユーザーエクスペリエンスを向上させる重要な要素です。この点で、新しい画像や具体化された説明が大いに助けになるでしょう。

また、エージェントテンプレートや特定ユースケースに関する情報削除は文書全体をシンプルにし、核心部分へのアクセスを容易にしています。結果として、情報が整理され、ユーザーが必要な情報にすぐ辿りつけるようサポートされています。

プロジェクトやスキーマ名の変更により、用語の統一性が図られ、ユーザーが編集意図をより直感的に理解できるようになりました。これにより、Azure AI Foundryを用いたプロジェクトの設定や管理がさらに効率的になることが期待されています。

全体として、今回の更新はドキュメントの利便性を強化し、Azureサービスを利用するユーザーのサポートを充実する内容となっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [configure-azure-resources.md](#item-1fbf48) | minor update | Azureリソースの構成方法に関する説明の更新 | modified | 19 | 1 | 20 | 
| [create-project.md](#item-58b2dd) | minor update | CLTファインチューニングタスク作成に関する情報の更新 | modified | 108 | 36 | 144 | 
| [train-model.md](#item-f5b164) | minor update | モデル訓練手順の改善 | modified | 3 | 1 | 4 | 
| [getting-started-fine-tuning.png](#item-6c3006) | new feature | ファインチューニング開始のための画像の追加 | added | 0 | 0 | 0 | 
| [overview.md](#item-bdc923) | minor update | 概要セクションの簡略化 | modified | 0 | 4 | 4 | 
| [overview.md](#item-f138b4) | minor update | エージェントテンプレートに関する情報の削除 | modified | 0 | 5 | 5 | 
| [overview.md](#item-631b23) | minor update | エージェントに関する説明の簡略化 | modified | 0 | 1 | 1 | 
| [toc.yml](#item-12f1f0) | minor update | プロジェクトおよびスキーマに関する名称の変更 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/language-service/conversational-language-understanding/how-to/configure-azure-resources.md{#item-1fbf48}

<details>
<summary>Diff</summary>
````diff
@@ -118,7 +118,25 @@ Azure AI Foundry offers a unified platform where you can easily build, manage, a
 
    :::image type="content" source="../media/configure-resources/connect-language-resource.png" alt-text="Screenshot of connect search resource selector in the Azure AI Foundry.":::
 
-1. Your resources are now set up properly. Continue with setting up the fine-tuning task and customizing your CLU project.
+## Import an existing Azure AI project
+
+Azure AI Foundry allows you to connect to your existing Azure AI services resources. This means you can establish a connection within your Azure AI Foundry project to the Azure AI Language resource where your custom models are stored.
+
+To import an existing Azure AI services project with Azure AI Foundry, you need to create a connection to the Azure AI services resource within your Azure AI Foundry project. For more information, *see* [Connect Azure AI Services projects to Azure AI Foundry](../../../../ai-services/connect-services-ai-foundry-portal.md)
+
+## Export a project
+
+You can download a CLU project as a **config.json** file:
+
+1. Navigate to your project home page.
+1. At the top of the page, select your project from the right page ribbon area.
+1. Select **Download config file**.
+
+    :::image type="content" source="../media/create-project/download-config-json.png" alt-text="Screenshot of project drop-down menu with the download config file hyperlink in the Azure AI Foundry.":::
+
+
+
+That's it! Your resources are now set up properly. Continue with setting up the fine-tuning task and customizing your CLU project.
 
 ## Next Steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureリソースの構成方法に関する説明の更新"
}
```

### Explanation
このコードの変更は、Azure AI Foundryの文書に関するもので、特に「Azureリソースの構成方法」ページの内容が更新されました。主に、既存のAzure AIプロジェクトのインポート手順やプロジェクトのエクスポート方法に関する新しいセクションが追加されています。

具体的には、ユーザーはAzure AI Foundry内でAzure AIサービスリソースへの接続を確立し、そこで保存されたカスタムモデルを使用する方法を学ぶことができるようになっています。また、CLUプロジェクトを**config.json**ファイルとしてダウンロードする手順も詳述されています。このように、全体としてユーザーがリソースを設定し、CLUプロジェクトをカスタマイズするためのプロセスが明確になります。

変更された内容は、リソースを正しく設定した後に続けるべき具体的なアクションへの指示を補足し、ユーザビリティを向上させています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/create-project.md{#item-58b2dd}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: Create Projects in Conversational Language Understanding
+title: Create a CLU fine-tuning task in Azure AI Foundry or with the REST API
 titleSuffix: Azure AI services
-description: This article shows you how to create projects in conversational language understanding (CLU).
+description: This article shows you how to create CLU fine-tuning task projects the Azure AI Foundry or using the REST API.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
@@ -11,73 +11,100 @@ ms.author: lajanuar
 ms.custom: language-service-clu
 ---
 
-# Create a CLU project in Azure AI Foundry
+# Create a fine-tuning task project
 
-Azure AI Foundry projects help you organize your work when exploring new ideas or developing prototypes for specific use cases. A Foundry project is created on an Azure AI Foundry resource. This type of project offers an easy setup and provides access to agents and Azure AI models.
+A Conversational Language Understanding (CLU) fine-tuning task is a workspace project where you customize a language model to identify user intent and extract key information (entities) from user input (utterances). In this workspace, you define the intents and entities relevant to your application, label sample user utterances accordingly, and use this labeled data to fine-tune the model. This process tailors the model to better understand the specific needs and nuances of your conversational application. In this guide, we walk you through configuring a fine-tuning workspace in the Azure AI Foundry or using the REST API.
 
-If you already have an Azure AI Language or multi-service resource—whether used on its own or through Language Studio—you can continue to use those existing Language resources within the Azure AI Foundry portal. For more information, see [How to use Azure AI services in the Azure AI Foundry portal](../../../../ai-services/connect-services-ai-foundry-portal.md).
+> [!NOTE]
+>
+> If you already have an Azure AI Language or multi-service resource—whether used on its own or through Language Studio—you can continue to use those existing Language resources within the Azure AI Foundry portal. For more information, see [How to use Azure AI services in the Azure AI Foundry portal](../../../../ai-services/connect-services-ai-foundry-portal.md).
+>
+> In Azure AI Foundry, you set up a fine-tuning task to serve as your workspace when customizing your CLU model. Previously, a **fine-tuning task** was referred to as a **CLU project**. You might encounter both terms used interchangeably in older CLU documentation.
+>
 
 ## Prerequisites
 
 * An Azure subscription. If you don't have one, you can [create one for free](https://azure.microsoft.com/free/cognitive-services).
 * **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
-* An [Azure AI Foundry resource](../../../multi-service-resource.md)
-  * For more information, *see* [Configure an Azure AI Foundry resource](configure-azure-resources.md#option-1-configure-an-azure-ai-foundry-resource).
-* After you create an Azure AI Foundry resource, [create a CLU project](#create-a-clu-project).
+*  An [Azure AI Foundry multi-service resource](../../../multi-service-resource.md). For more information, *see* [Configure an Azure AI Foundry resource](configure-azure-resources.md#option-1-configure-an-azure-ai-foundry-resource). Alternately, you can use an [Azure AI Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
+* A Foundry project created in the Azure AI Foundry. For more information, *see* [Create an AI Foundry project](../../../../ai-foundry/how-to/create-projects.md).
 
-## Create a CLU project
+> [!NOTE]
+>
+> We highly recommend that you use an Azure AI Foundry resource in the AI Foundry; however, you can also follow these instructions using a Language resource.
 
- An Azure AI Foundry project is created using an Azure AI Foundry resource. Projects are designed to help you organize your work. They offer various tools and resources that support the development, customization, and management of AI applications all within a centralized environment.
+## Create a CLU fine-tuning task project
+
+ To create a CLU fine-tuning task project, you first configure your environment and then create a fine-tuning task, which serves as your workspace for customizing your CLU model.
 
 ### [Azure AI Foundry](#tab/azure-ai-foundry)
 
- To learn how to create a CLU Foundry project, *see* [Create an AI Foundry project](../../../../ai-foundry/how-to/create-projects.md).
+1. Navigate to the [Azure AI Foundry](https://ai.azure.com/).
+1. If you aren't already signed in, the portal prompts you to do so with your Azure credentials.
+1. Once signed in, you can create or access your existing projects within Azure AI Foundry.
+1. If you're not already at your project for this task, select it.
+1. Select Fine-tuning from the left navigation panel.
 
+   :::image type="content" source="../media/select-fine-tuning.png" alt-text="Screenshot of fine-tuning selector in the Azure AI Foundry.":::
 
-### [REST APIs](#tab/rest-api)
+1. Select **the AI Service fine-tuning** tab and then **+ Fine-tune** button.
 
-[!INCLUDE [create project](../includes/rest-api/create-project.md)]
+   :::image type="content" source="../media/fine-tune-button.png" alt-text="Screenshot of fine-tuning button in the Azure AI Foundry.":::
 
----
+1. From **Create service fine-tuning** window, choose the **Conversational language understanding** tab then select **Next**.
 
-## Import an existing Azure AI project
+   :::image type="content" source="../media/select-project.png" alt-text="Screenshot of conversational language understanding tab in the Azure AI Foundry.":::
 
-### [Azure AI Foundry](#tab/azure-ai-foundry)
+1. In **Create CLU fine-tuning task** window, complete the **Name** and **Language** fields. If you're planning to fine-tune a model using the free **Standard Training** mode, select **English** for the language field.
 
-To import an existing Azure AI services project with Azure AI Foundry, you need to create a connection to the Azure AI services resource within your Azure AI Foundry project. For more information, *see* [Connect Azure AI Services projects to Azure AI Foundry](../../../../ai-services/connect-services-ai-foundry-portal.md)
+1. Navigate to the [Azure AI Foundry](https://ai.azure.com/).
+1. If you aren't already signed in, the portal prompts you to do so with your Azure credentials.
+1. Once signed in, you can create or access your existing projects within Azure AI Foundry.
+1. If you're not already at your project for this task, select it.
+1. Select Fine-tuning from the left navigation panel.
 
-### [REST APIs](#tab/rest-api)
+    :::image type="content" source="../media/select-fine-tuning.png" alt-text="Screenshot of fine-tuning selector in the Azure AI Foundry.":::
 
-You can import a CLU JSON into the service.
+1. Select **the AI Service fine-tuning** tab and then **+ Fine-tune** button.
 
-[!INCLUDE [Import project](../includes/rest-api/import-project.md)]
+    :::image type="content" source="../media/fine-tune-button.png" alt-text="Screenshot of fine-tuning button in the Azure AI Foundry.":::
 
----
+1. From **Create service fine-tuning** window, choose the **Conversational language understanding** tab then select **Next**.
 
-## Export a project
+    :::image type="content" source="../media/select-project.png" alt-text="Screenshot of conversational language understanding tab in the Azure AI Foundry.":::
 
-### [Azure AI Foundry](#tab/azure-ai-foundry)
+1. In **Create CLU fine tuning task** window, select your **Connected service** from the drop-down menu, then complete the **Name** and **Language** fields. If you're using the free **Standard Training** mode, select **English** for the language field.
 
-You can download a CLU project as a **config.json** file:
+1. Select the  **Create** button. It can take a few minutes for the *creating* operation to complete.
 
-1. Navigate to your project home page.
-1. At the top of the page, select your project from the right page ribbon area.
-1. Select **Download config file**.
 
-    :::image type="content" source="../media/create-project/download-config-json.png" alt-text="Screenshot of project drop-down menu with the download config file hyperlink in the Azure AI Foundry.":::
+   > [!NOTE]
+   >
+   > * **Standard training** enables faster training times and quicker iterations; however it's only available for English.
+   > * **Advanced training** includes longer training durations and is supported for English, other languages, and multilingual projects.
+   > * For more information, *see* [Training modes](train-model.md#training-modes).
 
-### [REST APIs](#tab/rest-api)
+1. Once the task creation is complete, select the task from the AI Service fine-tuning window to arrive at the Getting started with fine-tuning page.
 
-You can export a CLU project as a JSON file at any time.
+   :::image type="content" source="../media/create-project/getting-started-fine-tuning.png" alt-text="Screenshot of the getting started with fine-tuning page in the Azure AI Foundry." lightbox="../media/create-project/getting-started-fine-tuning.png":::
 
-[!INCLUDE [Export project](../includes/rest-api/export-project.md)]
+### [REST APIs](#tab/rest-api)
+
+[!INCLUDE [create project](../includes/rest-api/create-project.md)]
 
 ---
 
+
+That's it! You can get started on your fine-tuning task project. For more information, *see* [Next steps](#next-steps).
+
 ## View and manage project details
 
+You can retrieve up-to-date information about your projects, make any necessary changes, and oversee project management tasks efficiently through the Azure AI Foundry or REST API endpoints.
+
 ### [Azure AI Foundry](#tab/azure-ai-foundry)
 
+Your Azure AI Foundry project overview page displays information about your fine-tuning task project, including its name, subscription, resource group, and connected resources. You can also access the project's resources in the Azure portal by selecting **Manage in Azure portal** on the overview page.
+
 * On the project Home page, information about the project is found in the **Project details** section.
 * To view project settings, select **Management center** from the bottom of the left navigation pane, then select one of the following tabs:
    *  **Overview** to view project details.
@@ -89,14 +116,56 @@ You can export a CLU project as a JSON file at any time.
 
 ### [REST APIs](#tab/rest-api)
 
+You can access, view, and manage all of your project details via the REST API.
+
 [!INCLUDE [REST APIs project details](../includes/rest-api/project-details.md)]
 
 ---
 
-## Delete a project
+## Import an existing Azure AI project
+
+Importing the configuration file allows you to bring your existing settings directly into the platform, making it easier to set up and customize your service based on your predefined preferences.
 
 ### [Azure AI Foundry](#tab/azure-ai-foundry)
 
+To import an existing Azure AI services project with Azure AI Foundry, you need to create a connection to the Azure AI services resource within your Azure AI Foundry project. For more information, *see* [Connect Azure AI Services projects to Azure AI Foundry](../../../../ai-services/connect-services-ai-foundry-portal.md)
+
+### [REST APIs](#tab/rest-api)
+
+You can import your CLU config.json file using the REST API
+
+[!INCLUDE [Import project](../includes/rest-api/import-project.md)]
+
+---
+
+## Export a fine-tuning project
+
+Exporting your configuration file enables you to save the current state of your project's settings and structure, making it easy to back up or transfer your project as needed.
+
+### [Azure AI Foundry](#tab/azure-ai-foundry)
+
+You can download an Azure Foundry fine fine-tuning task project as a **config.json** file:
+
+1. Navigate to your project home page.
+1. At the top of the page, select your project from the right page ribbon area.
+1. Select **Download config file**.
+
+    :::image type="content" source="../media/create-project/download-config-json.png" alt-text="Screenshot of project drop-down menu with the download config file hyperlink in the Azure AI Foundry.":::
+
+### [REST APIs](#tab/rest-api)
+
+You can export a CLU project as a config.json file.
+
+[!INCLUDE [Export project](../includes/rest-api/export-project.md)]
+
+---
+
+
+## Delete a project
+
+Deleting a project ensures that it and all of its associated data are permanently removed from the system.
+
+### [Azure AI Foundry](#tab/azure-ai-foundry)
 
 If you no longer need your project, you can delete it from the Azure AI Foundry.
 
@@ -113,19 +182,22 @@ To delete the hub along with all its projects:
 
    :::image type="content" source="../media/create-project/hub-details.png" alt-text="Screenshot of the hub details list in the Azure AI Foundry.":::
 
-1. On the right, select **Delete hub**. 
+1. On the right, select **Delete hub**.
 1. The link opens the Azure portal for you to delete the hub there.
 
    :::image type="content" source="../media/create-project/delete-hub.png" alt-text="Screenshot of the Delete hub button in the Azure AI Foundry.":::
 
 ### [REST APIs](#tab/rest-api)
 
-If you no longer need your project, delete it using the REST API.
+If your project is no longer required, you can delete it using the REST API. To proceed, access the REST API and follow the documented steps for project deletion to complete this action.
 
 [!INCLUDE [Delete project](../includes/rest-api/delete-project.md)]
 
 ---
 
-## Related content
+## Next steps
+
+After you create your fine-tuning workspace, start your fine-tuning task by defining your intents and entities and adding them to your schema:
 
-- [Build schema](./build-schema.md)
+* [Build your fine-tuning schema](build-schema.md)
+* [Label utterances](tag-utterances.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "CLTファインチューニングタスク作成に関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure AI Foundryにおけるコンversational Language Understanding (CLU) プロジェクトの作成に関するドキュメントを大幅に更新したものです。文章のタイトル、説明、内容が見直され、特にファインチューニングタスクの作成方法に焦点が当てられています。

主な変更点としては、以下の内容が含まれます。

1. **タイトルと説明の改訂**: プロジェクトは「CLUプロジェクト」から「CLUファインチューニングタスクプロジェクト」にリブランドされ、作成ガイドの目的が明確化されました。

2. **手順の整理**: ファインチューニングタスクを設定する過程が詳細に説明され、Azure AI FoundryまたはREST APIを使用してプロジェクトを作成する手順が具体的に述べられています。

3. **新たな重要情報の追加**: ファインチューニングタスクのノートが追加され、既存のAzure AI Languageリソースを用いた場合の注意点が記載されました。

4. **プロジェクト管理セクションの強化**: プロジェクトの詳細情報の表示や管理に関する手順が追加され、ユーザーがAzure AI FoundryまたはREST APIを通じてプロジェクトをより効率的に管理できるようになっています。

5. **新規機能の紹介**: プロジェクト設定をインポートまたはエクスポートする手順が新たに示され、ユーザーにとっての利便性が向上しています。

全体的に、この変更はユーザーがファインチューニングタスクを設定し、管理するためのプロセスを簡素化し、最新のインターフェースに適応した内容となっています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/train-model.md{#item-f5b164}

<details>
<summary>Diff</summary>
````diff
@@ -103,7 +103,9 @@ Use the evaluation scores to guide your decisions. There may be times where a sp
 
    :::image type="content" source="../media/select-project.png" alt-text="Screenshot of conversational language understanding tab in the Azure AI Foundry.":::
 
-1. In **Create CLU fine tuning task** window, complete the **Name** and **Language** fields. If you're using the free **Standard Training** mode, select **English** for the language field.
+1. In **Create CLU fine tuning task** window, select your **Connected service** from the drop-down menu, then complete the **Name** and **Language** fields. If you're using the free **Standard Training** mode, select **English** for the language field.
+
+1. Select the  **Create** button. It may take a few minutes for the create operation to complete.
 
     > [!NOTE]
     >
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル訓練手順の改善"
}
```

### Explanation
このコードの変更は、Azure AI Foundryにおけるコンversational Language Understanding (CLU) モデルの訓練手順の一部を改訂したものです。具体的には、モデル作成プロセスの指示が更新され、ユーザーにとっての手順がより明確になっています。

主な変更点は以下の通りです：

1. **手順の詳細化**: 「Create CLU fine tuning task」ウィンドウにおいて、最初に「Connected service」を選択するように指示が追加されました。これにより、ユーザーは正しいサービスと接続された状態で作業を始めることができます。

2. **新しいステップの追加**: 訓練タスク作成の最後に「Create」ボタンを選択する手順が追加されました。これにより、タスク作成が完了するまでの時間を考慮した指示が提供され、ユーザーが次に取るべきアクションが明確になります。

この変更により、手順がよりわかりやすくなり、ユーザーの操作ミスを減少させる効果が期待されます。全体として、コン versational Language Understanding プロジェクトのセットアッププロセスが強化されています。

## articles/ai-services/language-service/conversational-language-understanding/media/create-project/getting-started-fine-tuning.png{#item-6c3006}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニング開始のための画像の追加"
}
```

### Explanation
このコードの変更は、Azure AI Foundryにおけるコンversational Language Understanding (CLU) プロジェクトのファインチューニングに関する新しい画像ファイルを追加したものです。具体的には、ユーザーがファインチューニングタスクを開始する際の手順を視覚的に示す画像が含まれています。

追加された画像の主な目的は、以下の通りです：

1. **視覚的サポート**: 手順を説明する際に、画像を用いることでユーザーが内容をより理解しやすくすることを狙っています。具体的には、インターフェースの操作や設定手順が視覚的に示されることで、ユーザーガイドの効果が高まります。

2. **ユーザーエクスペリエンスの向上**: ビジュアルコンテンツを含めることで、特に非技術的なユーザーが手順を追いやすくなり、作業の流れをスムーズにする効果があります。

3. **ドキュメントの完全性を向上**: 新しい画像は、ファインチューニングの開始手順に関する情報を補完し、全体的なドキュメントの内容を強化します。

この変更により、ユーザーはファインチューニングタスクを開始する際の手順をより明確に理解しやすくなると期待されます。

## articles/ai-services/language-service/conversational-language-understanding/overview.md{#item-bdc923}

<details>
<summary>Diff</summary>
````diff
@@ -44,10 +44,6 @@ When you integrate a client application with a speech to text component, users c
 
 In a large corporation, an enterprise chat bot may handle various employee affairs. It might handle frequently asked questions served by a custom question answering knowledge base, a calendar specific skill served by conversational language understanding, and an interview feedback skill served by LUIS. Use Orchestration workflow to connect all these skills together and appropriately route the incoming requests to the correct service.
 
-### Agents
-
-CLU is utilized by the [intent routing](https://github.com/azure-ai-foundry/foundry-samples/tree/main/samples/agent-catalog/msft-agent-samples/foundry-agent-service-sdk/intent-routing-agent) agent template, which detects user intent and provides exact answering. Perfect for deterministically intent routing and exact question answering with human control.
-
 ## Project development lifecycle
 
 Creating a CLU project typically involves several different steps.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "概要セクションの簡略化"
}
```

### Explanation
このコード変更は、Azure AI Foundryのコンversational Language Understanding (CLU) に関する概要セクションを簡略化したものです。具体적으로、情報の明確化を図るために、特定の部分が削除されました。

主な変更点は以下の通りです：

1. **エージェントに関する文の削除**: 「Agents」という見出しが削除され、CLUが意図的ルーティングエージェントテンプレートとして使用される例や詳細についての記述がなくなりました。この部分は、特定のユースケースに焦点を当てていましたが、より簡潔な情報提供が意図されています。

2. **内容の簡素化**: 概要が短縮されることで、CLUの全体像がよりシンプルで理解しやすくなりました。これにより、新しいユーザーがドキュメントを読む際に感じる負担が軽減されます。

3. **文脈の焦点化**: 残された内容により、プロジェクトの開発ライフサイクルに関する情報に焦点を当てた形になり、ユーザーが探している情報により早くアクセスできるようになっています。

この変更により、概要セクションが明確化され、読者は各項目に迅速かつ効率的にアクセスできるようになります。全体として、情報が整理され、ユーザー体験が向上しています。

## articles/ai-services/language-service/overview.md{#item-f138b4}

<details>
<summary>Diff</summary>
````diff
@@ -23,11 +23,6 @@ The Language service also provides several new features as well, which can eithe
 * Preconfigured, which means the AI models that the feature uses aren't customizable. You just send your data, and use the feature's output in your applications.
 * Customizable, which means you train an AI model using our tools to fit your data specifically.
 
-Language features are also utilized in [agent templates](https://github.com/azure-ai-foundry/foundry-samples/tree/main/samples/agent-catalog):
-
-* [Intent routing agent](https://github.com/azure-ai-foundry/foundry-samples/tree/main/samples/agent-catalog/msft-agent-samples/foundry-agent-service-sdk/intent-routing-agent) detects user intent and provides exact answering. Perfect for deterministically intent routing and exact question answering with human controls.
-* [Exact question answering agent](https://github.com/azure-ai-foundry/foundry-samples/tree/main/samples/agent-catalog/msft-agent-samples/foundry-agent-service-sdk/exact-qna-agent) answers high-value predefined questions deterministically to ensure consistent and accurate responses.
-
 > [!TIP]
 > Unsure which feature to use? See [Which Language service feature should I use](#which-language-service-feature-should-i-use) to help you decide.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントテンプレートに関する情報の削除"
}
```

### Explanation
このコード変更は、Azure AI FoundryのLanguage serviceに関する概要ドキュメントから特定の情報が削除されたことを示しています。具体的には、エージェントテンプレートに関連した情報が取り除かれています。

主な変更点は以下の通りです：

1. **エージェントテンプレート情報の削除**: 「Language features are also utilized in agent templates」という文が削除され、それに続く「意図ルーティングエージェント」と「正確な質問応答エージェント」に関する詳細な説明も削除されました。これにより、以前の文脈が省かれ、情報が簡略化されています。

2. **情報のコンパクト化**: 上記の削除により、概要セクションがよりコンパクトになり、主要な機能や特徴の説明に焦点が当たるようになりました。この形式は、情報過多を防ぎ、ユーザーが必要な情報にアクセスしやすくすることが目指されています。

3. **ユーザビリティの向上**: エージェントに関する具体的な情報が削除されたため、残された内容が読者にとってより関連性が高く、機能の理解を助けるものになっています。

この変更は、Language serviceの機能に関連する情報を明確に整理し、ユーザーが必要な情報にすぐにアクセスできるようにするためのものです。全体として、内容が簡潔化され、読者が理解しやすくなることが期待されます。

## articles/ai-services/language-service/question-answering/overview.md{#item-631b23}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,6 @@ This documentation contains the following article types:
 * **When you want to provide the same answer to a request, question, or command** - when different users submit the same question, the same answer is returned.
 * **When you want to filter static information based on meta-information** - add [metadata](./tutorials/multiple-domains.md) tags to provide added filtering options relevant to your client application's users and the information. Common metadata information includes [chit-chat](./how-to/chit-chat.md), content type or format, content purpose, and content freshness. <!--TODO: Fix Link-->
 * **When you want to manage a bot conversation that includes static information** - your project takes a user's conversational text or command and answers it. If the answer is part of a predetermined conversation flow, represented in your project with [multi-turn context](./tutorials/guided-conversations.md), the bot can easily provide this flow.
-* **When you want to use an agent to get an exact answer** - Use the [exact question answering](https://github.com/azure-ai-foundry/foundry-samples/tree/main/samples/agent-catalog/msft-agent-samples/foundry-agent-service-sdk/customer-service-agent) agent template answers high-value predefined questions deterministically to ensure consistent and accurate responses or the [intent routing](https://github.com/azure-ai-foundry/foundry-samples/tree/main/samples/agent-catalog/msft-agent-samples/foundry-agent-service-sdk/intent-routing-agent) agent template, which detects user intent and provides exact answering. Perfect for deterministically intent routing and exact question answering with human control.
 
 ## What is a project?
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントに関する説明の簡略化"
}
```

### Explanation
このコード変更は、Azure AIのQuestion Answeringサービスに関する概要ドキュメント内で特定の情報が削除されたことを示しています。具体的には、「正確な質問応答」に関連するエージェントに関する説明部分が削除されました。

主な変更点は以下の通りです：

1. **エージェントに関する具体的な説明の削除**: 「正確な質問応答エージェント」と「意図ルーティングエージェント」に関する詳細が削除されました。これにより、エージェントを使用して高価値の事前定義された質問に対する応答を得る方法についての具体的な情報がなくなりました。

2. **情報の簡潔化**: 上記の削除により、他の記述と比較してテキストが簡潔になりました。この変更は、文書全体をより読みやすくし、利用者が異なる機能の概要を素早く把握できるようにすることを目的としています。

3. **ユーザビリティの向上**: エージェントに関する具体的な説明が削除されたため、残された他の情報がより重要で関連性が高く感じられるようになっています。これにより、利用者はドキュメントを通じて重要な情報へと迅速にアクセスできるようになります。

この変更は、Question Answeringの各機能の理解を助けるために、全体的に文書内容が整理され、読みやすさが向上することを目的としています。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -148,10 +148,10 @@ items:
             href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
           - name: Azure AI containers overview
             href: ../cognitive-services-container-support.md
-        - name: Create a CLU Foundry project 
+        - name: Create a fine-tuning task project
           href: conversational-language-understanding/how-to/create-project.md
           displayName: creation, clu project, setup
-        - name: Build a schema
+        - name: Build a fine-tuning schema
           href: conversational-language-understanding/how-to/build-schema.md
           displayName: design, intents, entities, conversational model
         - name: Label utterances
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクトおよびスキーマに関する名称の変更"
}
```

### Explanation
このコード変更は、Azure AI Language Serviceの目次（toc.yml）において、プロジェクトおよびスキーマに関連する名称が変更されたことを示しています。

主な変更点は以下の通りです：

1. **プロジェクト名の変更**: 「Create a CLU Foundry project」が「Create a fine-tuning task project」に変更されました。この変更により、プロジェクトの内容がより具体的に表現されています。

2. **スキーマ名の変更**: 「Build a schema」が「Build a fine-tuning schema」に変更されました。この変更も、スキーマの具体的な役割や用途をより明確に伝えるものとなっています。

3. **全体的な構成の整備**: 名称の変更が行われた部分に関連するデスクリプション（表示名）も自動的に更新され、ドキュメント全体の整合性が保たれています。

これらの変更は、ユーザーがプロジェクトやスキーマの内容をより理解しやすくするためのものであり、具体的なタスクや成果物に関連する名称を採用することで、文書の明瞭性と使いやすさが向上することを目的としています。


