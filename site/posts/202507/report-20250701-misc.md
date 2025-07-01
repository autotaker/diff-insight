---
date: '2025-07-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8f107da...MicrosoftDocs:5b7339b
summary: このコード変更では、Azure AIサービスに関連するドキュメントと画像が更新または追加され、内容の明確化、新機能の提供、信頼性の向上が図られています。「ロールベースのアクセス制御」や「多言語対応」の修正が施され、新たなガイドやビジュアルコンテンツも追加されました。一方でカスタム質問応答サービスに関する文書が削除され、その結果、既存ユーザーにとって情報の不足が懸念されます。全体としてはAzure
  AI文書の価値を高め、ユーザー体験を向上させることを目指していますが、削除された情報の代替が必要です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8f107da...MicrosoftDocs:5b7339b){target="_blank"}

<format>
# ハイライト
このコード変更におけるハイライトには、Azure AI サービスに関連する複数のドキュメントおよび画像が更新または追加されており、その内容の明確化、新機能の提供、信頼性の向上が見られます。「ロールベースのアクセス制御」や「多言語対応」などの既存ドキュメントに軽微な修正が施され、新しいガイドやビジュアルコンテンツが複数追加されたことが注目されます。また、一部のドキュメントでは著しい変更が行われ、関連情報が削除されています。

## 新機能
- 「Azure リソースの構成に関する新しいガイド」の追加。
- 関連リソースの設定をサポートする多くの画像ファイルの追加。
- AI Foundryの管理および検索リソースの接続に関する視覚的ガイドの追加。

## 重大な変更
- カスタム質問応答サービスの設定に関するドキュメントの削除。
- 一部のドキュメントに大幅な行削除があり、そのための代替リソースが提供されていない可能性。

## その他のアップデート
- 多くの文書での軽微なテキスト修正、日付の更新、表現の改善。
- toc.ymlファイルの大幅なアップデート、新項目の追加および古い項目の整理。

# インサイト
Azure AIサービスの文書更新および画像追加の一連の変更は、ドキュメントの利用しやすさと適用性を大幅に改善することを目的としています。技術者が直面する複雑な設定プロセスに対して、視覚的なサポートを強化する傾向が明確に見られました。これにより、ユーザーは単なるテキストの指示よりも直感的に製品の使用方法を理解しやすくなります。

特に、新たに追加されたガイドや画像は、Azure AIを初めて使用するユーザーがスムーズに環境を構築し、効果的に機能を活用するための強力なツールとなるでしょう。ビジュアルコンテンツの強化によって、技術的なドキュメントが受ける情報的なギャップを埋める取り組みが行われていることがわかります。

一方で、ドキュメントの削除や機能的な変更に伴う情報の不足は、既存ユーザーにとってチャレンジとなる可能性があります。これには特にカスタム質問応答サービスに関連する内容が含まれ、代替の情報が提供されない限り、潜在的なサポートリソースの欠落に直面する可能性があります。

総じて、今回の変更はAzure AI文書全体の価値を高める改良であり、その結果、ユーザーの利用体験を向上させると考えられます。しかし、削除された情報については、周知される代替情報が必要です。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [role-based-access-control.md](#item-9f68fe) | minor update | ロールベースのアクセス制御に関する文書の更新 | modified | 4 | 4 | 8 | 
| [multiple-languages.md](#item-5de532) | minor update | 多言語対応に関する文書の更新 | modified | 1 | 1 | 2 | 
| [configure-azure-resources.md](#item-1fbf48) | new feature | Azure リソースの構成に関する新しいガイドの追加 | added | 126 | 0 | 126 | 
| [deploy-model.md](#item-b64101) | minor update | モデルのデプロイに関する文書の修正 | modified | 5 | 5 | 10 | 
| [train-model.md](#item-f5b164) | minor update | モデルのトレーニングに関するドキュメントの更新 | modified | 106 | 29 | 135 | 
| [balance-training-data.md](#item-768433) | minor update | トレーニングデータのバランスに関する文の修正 | modified | 1 | 1 | 2 | 
| [add-role-assignment.png](#item-3efc05) | new feature | 役割割り当てを追加するための画像の追加 | added | 0 | 0 | 0 | 
| [ai-foundry-management-center.png](#item-084dfd) | new feature | AIファウンドリ管理センターの画像の追加 | added | 0 | 0 | 0 | 
| [cognitive-services-user.png](#item-0a9def) | new feature | 認知サービスユーザーの画像の追加 | added | 0 | 0 | 0 | 
| [connect-language-resource.png](#item-25a810) | new feature | 言語リソースを接続するための画像の追加 | added | 0 | 0 | 0 | 
| [managed-identity.png](#item-2998de) | new feature | 管理されたアイデンティティに関する画像の追加 | added | 0 | 0 | 0 | 
| [new-connection.png](#item-3f47f6) | new feature | 新しい接続に関する画像の追加 | added | 0 | 0 | 0 | 
| [data-splitting.png](#item-d14f85) | new feature | データ分割に関する画像の追加 | added | 0 | 0 | 0 | 
| [fine-tune-button.png](#item-e38384) | new feature | ファインチューニングボタンに関する画像の追加 | added | 0 | 0 | 0 | 
| [my-assets.png](#item-4bed5a) | new feature | マイアセットに関する画像の追加 | added | 0 | 0 | 0 | 
| [select-fine-tuning.png](#item-745dc5) | new feature | ファインチューニング選択に関する画像の追加 | added | 0 | 0 | 0 | 
| [select-mode.png](#item-b0b2a0) | new feature | モード選択に関する画像の追加 | added | 0 | 0 | 0 | 
| [select-project.png](#item-0e6492) | new feature | プロジェクト選択に関する画像の追加 | added | 0 | 0 | 0 | 
| [train-fine-tuning-model.png](#item-1912bc) | new feature | ファインチューニングモデルのトレーニングに関する画像の追加 | added | 0 | 0 | 0 | 
| [tag-data.md](#item-e70f6f) | minor update | データタグ付けに関するドキュメントの修正 | modified | 10 | 10 | 20 | 
| [triage-email.md](#item-47cadc) | minor update | メールのトリアージに関するチュートリアルの修正 | modified | 3 | 3 | 6 | 
| [language-support.md](#item-2c8ef2) | minor update | 言語サポートに関するドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-bee292) | minor update | クイックスタートガイドの日付更新 | modified | 1 | 1 | 2 | 
| [azure-resources.md](#item-34fc37) | minor update | Azureリソースに関するドキュメントのテキスト修正 | modified | 3 | 3 | 6 | 
| [authoring.md](#item-855d84) | minor update | 著作に関するドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [chit-chat.md](#item-fe639e) | minor update | チットチャットに関するドキュメントのテキスト修正 | modified | 4 | 4 | 8 | 
| [configure-azure-resources.md](#item-a2ea5c) | new feature | Azureリソースの設定に関する新しいガイド | added | 125 | 0 | 125 | 
| [configure-resources.md](#item-304b9b) | breaking change | カスタム質問応答サービスの設定ガイドの削除 | removed | 0 | 37 | 37 | 
| [language-support.md](#item-b1f267) | minor update | 言語サポートに関するドキュメントの更新 | modified | 74 | 76 | 150 | 
| [add-role-assignment.png](#item-37c411) | new feature | 役割割り当ての画像の追加 | added | 0 | 0 | 0 | 
| [ai-foundry-management-center.png](#item-8cf696) | new feature | AIファウンドリ管理センターの画像の追加 | added | 0 | 0 | 0 | 
| [api-access-control.png](#item-677baf) | new feature | APIアクセス制御の画像の追加 | added | 0 | 0 | 0 | 
| [azure-ai-administrator.png](#item-919814) | new feature | Azure AI管理者の画像の追加 | added | 0 | 0 | 0 | 
| [azure-ai-search-resource.png](#item-28942c) | new feature | Azure AI検索リソースの画像の追加 | added | 0 | 0 | 0 | 
| [connect-azure-search.png](#item-f291f5) | new feature | Azure検索への接続方法を示す画像の追加 | added | 0 | 0 | 0 | 
| [fine-tuning.png](#item-e6295d) | new feature | ファインチューニング手法を示す画像の追加 | added | 0 | 0 | 0 | 
| [go-to-project.png](#item-cda578) | new feature | プロジェクトへの移動を示す画像の追加 | added | 0 | 0 | 0 | 
| [new-connection.png](#item-931bb0) | new feature | 新しい接続を示す画像の追加 | added | 0 | 0 | 0 | 
| [user-group-service-principal.png](#item-394a5f) | new feature | ユーザーグループとサービス プリンシパルを示す画像の追加 | added | 0 | 0 | 0 | 
| [adding-synonyms.md](#item-ccf9ee) | minor update | 同義語追加チュートリアルの更新 | modified | 7 | 7 | 14 | 
| [use-containers.md](#item-887deb) | minor update | コンテナ使用に関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [toc.yml](#item-12f1f0) | minor update | トピック構成ファイルの更新 | modified | 89 | 16 | 105 | 


# Modified Contents
## articles/ai-services/language-service/concepts/role-based-access-control.md{#item-9f68fe}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/21/2024
+ms.date: 06/30/2025
 ms.author: lajanuar
 ---
 
@@ -51,7 +51,7 @@ These custom roles only apply to Language resources.
 
 ### Cognitive Services Language Reader
 
-A user that should only be validating and reviewing the Language apps, typically a tester to ensure the application is performing well before deploying the project. They may want to review the application’s assets to notify the app developers of any changes that need to be made, but do not have direct access to make them. Readers will have access to view the evaluation results.
+A user that should only be validating and reviewing the Language apps, typically a tester to ensure the application is performing well before deploying the project. They might want to review the application’s assets to notify the app developers of any changes that need to be made, but do not have direct access to make them. Readers will have access to view the evaluation results.
 
 
 :::row:::
@@ -85,7 +85,7 @@ A user that should only be validating and reviewing the Language apps, typically
 
 ### Cognitive Services Language Writer
 
-A user that is responsible for building and modifying an application, as a collaborator in a larger team. The collaborator can modify the Language apps in any way, train those changes, and validate/test those changes in the portal. However, this user shouldn’t have access to deploying this application to the runtime, as they may accidentally reflect their changes in production. They also shouldn’t be able to delete the application or alter its prediction resources and endpoint settings (assigning or unassigning prediction resources, making the endpoint public). This restricts this role from altering an application currently being used in production. They may also create new applications under this resource, but with the restrictions mentioned.
+A user that is responsible for building and modifying an application, as a collaborator in a larger team. The collaborator can modify the Language apps in any way, train those changes, and validate/test those changes in the portal. However, this user shouldn’t have access to deploying this application to the runtime, as they might accidentally reflect their changes in production. They also shouldn’t be able to delete the application or alter its prediction resources and endpoint settings (assigning or unassigning prediction resources, making the endpoint public). This restricts this role from altering an application currently being used in production. They might also create new applications under this resource, but with the restrictions mentioned.
 
 :::row:::
     :::column span="":::
@@ -104,7 +104,7 @@ A user that is responsible for building and modifying an application, as a colla
     :::column-end:::
     :::column span="":::
       * All APIs under Language reader
-      * All POST, PUT and PATCH APIs under:
+      * All POST, PUT, and PATCH APIs under:
          * [Language conversational language understanding APIs](/rest/api/language/2023-04-01/conversational-analysis-authoring)
          * [Language text analysis APIs](/rest/api/language/2023-04-01/text-analysis-authoring)
          * [question answering projects](/rest/api/questionanswering/question-answering-projects)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ロールベースのアクセス制御に関する文書の更新"
}
```

### Explanation
この変更は、Azure AI サービスの「ロールベースのアクセス制御」に関するドキュメントの更新を含んでいます。主な変更点は、文書の日付を2024年11月21日から2025年6月30日に更新したことです。また、テキストの一部で「typically」を「typically a tester」と「typically」の表現を微修正し、より自然な文章にするために「might」を「may」に変更しています。

さらに、APIの説明で「POST, PUT and PATCH」を「POST, PUT, and PATCH」のようにカンマの使用を明確にするための小さな修正も行われています。全体として、この変更は文書の明瞭性と正確性を向上させることを目的としたマイナーな更新です。

## articles/ai-services/language-service/conversational-language-understanding/concepts/multiple-languages.md{#item-5de532}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/21/2024
+ms.date: 06/30/2025
 ms.author: lajanuar
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "多言語対応に関する文書の更新"
}
```

### Explanation
この変更は、Azure AI サービスの「多言語対応」に関するドキュメントの更新を表しています。具体的には、文書の日付が2024年11月21日から2025年6月30日に変更されました。この小さな更新は、コンテンツが最新の情報を反映するためのものであり、文書の信頼性を向上させる効果があります。全体的に、この修正は文書の管理と整合性を保つために重要です。

## articles/ai-services/language-service/conversational-language-understanding/how-to/configure-azure-resources.md{#item-1fbf48}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,126 @@
+---
+title: Configure the conversational language understanding  service for fine-tune models
+description: This article details Azure AI resource configurations for conversational language understanding fine-tune models.
+ms.service: azure-ai-language
+ms.topic: how-to
+author: laujan
+ms.author: lajanuar
+ms.date: 06/25/2025
+ms.custom: language-service-question-answering
+---
+
+# Configure your environment for Azure AI resources and permissions
+
+In this guide, we walk you through configuring your Azure AI resources and permissions for conversational language understanding (CLU) projects. We present two options:
+
+* [**Option 1: Configure an Azure AI Foundry resource**](#option-1-configure-an-azure-ai-foundry-resource). Azure AI Foundry offers a unified environment for building generative AI applications and using Azure AI services. All essential tools are together in one environment for all stages of AI app development.
+
+* [**Option 2: Configure Azure Language and Azure OpenAI resources**](#option-2-configure-azure-language-resource-and-azure-openai-resources). Azure OpenAI allows users to access OpenAI's language models within the Azure platform, providing security, regulatory compliance, and integration with other Azure services.
+
+Completing these setups is essential for fully integrating your environment with Azure AI Services. You only need to perform this setup once—afterward, you have seamless access to advanced, AI-powered conversational language understanding capabilities.
+
+In addition, we show you how to assign the correct roles and permissions within the Azure portal. These steps help you get started quickly and effectively with Azure AI Language.
+
+## Prerequisites
+
+Before you can set up your resources, you need:
+
+* **An active Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/free/cognitive-services).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+* An [Azure AI Foundry multi-service resource](../../../multi-service-resource.md) or an [Azure AI Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
+
+* An [Azure OpenAI resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI) (optional but required for [option 2](#option-2-configure-azure-language-resource-and-azure-openai-resources))
+
+> [!NOTE]
+>
+> We highly recommend that you use an Azure AI Foundry resource in the AI Foundry; however, you can also follow these instructions using a Language resource.
+
+## Option 1: Configure an Azure AI Foundry resource
+
+Azure AI Foundry offers a unified platform for building, managing, and deploying AI solutions with a wide array of models and tools. With this integration, you gain access to features like **Quick Deploy** for rapid model **fine-tuning** and **suggest utterances** to expand your training data with generative AI. New features are continually added, making Azure AI Foundry the recommended choice for scalable CLU solutions.
+
+1. Navigate to the [Azure portal](https://azure.microsoft.com/#home).
+
+1. Go to your Azure AI Foundry resource (select **All resources** to locate your resource).
+
+1. Next, select **Access Control (IAM)** on the left panel, then select **Add role assignment**.
+
+   :::image type="content" source="../media/configure-resources/add-role-assignment.png" alt-text="Screenshot of add role assignment selector in the Azure portal.":::
+
+1. Search and select the **Cognitive Services User** role. Select **Next**.
+
+   :::image type="content" source="../media/configure-resources/cognitive-services-user.png" alt-text="Screenshot of Cognitive Services User from the job function roles list in the Azure portal.":::
+
+1. Navigate to the **Members** tab and then select **Managed Identity**.
+
+   :::image type="content" source="../media/configure-resources/managed-identity.png" alt-text="Screenshot of assign member access selector in the Azure portal.":::
+
+1. Select **Select members**, then in the right panel, search for and choose your Azure AI Foundry resource (the one you're using for this project), and choose **Select**.
+
+1. Finally, select **Review + assign** to confirm your selection.
+
+1. Your resources are now set up properly. Continue with setting up the fine-tuning task and continue customizing your CLU project.
+
+## Option 2: Configure Azure Language resource and Azure OpenAI resources
+
+Azure OpenAI is a cloud-based solution that brings the advanced capabilities of OpenAI's language models to the Azure platform. With this service, you can easily incorporate natural language processing features into your applications without extensive AI or machine learning expertise. 
+
+##### Step 1: Assign the correct role to the Azure OpenAI resource
+
+1. Navigate to the [Azure portal](https://azure.microsoft.com/#home).
+
+1. Go to your Azure OpenAI resource. (select **All resources** to locate your resource).
+
+1. Next, select **Access Control (IAM)** on the left panel, then select **Add role assignment**.
+
+   :::image type="content" source="../media/configure-resources/add-role-assignment.png" alt-text="Screenshot of add role assignment selector in the Azure portal.":::
+
+1. Search and select the **Cognitive Services User** role, then select **Next**.
+
+   :::image type="content" source="../media/configure-resources/cognitive-services-user.png" alt-text="Screenshot of Cognitive Services User from the job function roles list in the Azure portal.":::
+
+1. Navigate to the **Members** tab and then select **Managed Identity**.
+
+   :::image type="content" source="../media/configure-resources/managed-identity.png" alt-text="Screenshot of assign member access selector in the Azure portal.":::
+
+1. Select **Select members**, then in the right panel, search for and choose your Azure AI Foundry resource (the one you're using for this project), and choose **Select**.
+
+1. Finally, select **Review + assign** to confirm your selection.
+
+
+##### Step 2: Configure connections in AI Foundry
+
+Azure AI Foundry offers a unified platform where you can easily build, manage, and deploy AI solutions using a wide range of models and tools. Connections enable authentication and access to both Microsoft and external resources within your Azure AI Foundry projects.
+
+1. Sign into [Azure AI Foundry](https://ai.azure.com/) using your account and required subscription. Then, select the project containing your desired Azure AI Foundry resource.
+
+1. Next, navigate to the **Management Center** in the bottom left corner of the page.
+
+1. Scroll to the **Connected resources** section of the Management center.
+
+    :::image type="content" source="../media/configure-resources/ai-foundry-management-center.png" alt-text="Screenshot of the management center selector in the Azure AI Foundry.":::
+
+
+1. Select the  **+ New connection** button.
+
+   :::image type="content" source="../media/configure-resources/new-connection.png" alt-text="Screenshot of the new connection button in the Azure AI Foundry.":::
+
+
+1. In the new window, select **Azure AI Language** as the resource type, then find your Azure AI Language resource.
+
+1. Select **Add connection** in the corner of your selected Azure AI Language resource.
+
+1. Select **Azure OpenAI** as the resource type, then find your desired Azure OpenAI resource.
+
+1. Ensure **Authentication** is set to **API key**.
+
+1. Select **Add connection**, then select **Close**.
+
+   :::image type="content" source="../media/configure-resources/connect-language-resource.png" alt-text="Screenshot of connect search resource selector in the Azure AI Foundry.":::
+
+1. Your resources are now set up properly. Continue with setting up the fine-tuning task and customizing your CLU project.
+
+## Next Steps
+
+[Create a CLU fine-tuning task](train-model.md#train-your-model)
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure リソースの構成に関する新しいガイドの追加"
}
```

### Explanation
この変更は、Azure AI サービスの「会話型言語理解」の一環として、Azure リソースを構成する方法についての新しいガイドを追加するものです。このガイドでは、会話型言語理解（CLU）プロジェクト向けに Azure AI リソースとその権限を設定する手順を詳細に説明しています。

新しい記事には、Azure AI Foundry リソースの設定や、Azure Language および Azure OpenAI リソースの構成に関する2つのオプションが含まれています。また、このガイドでは、必要な前提条件や役割の割り当ての方法についても説明しています。

記事は、特に新機能や最新の手法を取り入れており、ユーザーが Azure AI サービスを効果的に活用できるように設計されています。このガイドを参照することで、ユーザーはよりシームレスに高度な会話型言語理解機能にアクセスできるようになります。全体として、この変更はユーザーにとって有用な新機能を提供し、文書の充実を図っています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/deploy-model.md{#item-b64101}

<details>
<summary>Diff</summary>
````diff
@@ -6,18 +6,18 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/21/2024
+ms.date: 06/30/2025
 ms.author: lajanuar
 ms.custom: language-service-clu,
 ---
 
 # Deploy a model 
 
-Once you are satisfied with how your model performs, it's ready to be deployed, and query it for predictions from utterances. Deploying a model makes it available for use through the [prediction API](/rest/api/language/2023-04-01/conversation-analysis-runtime/analyze-conversation).
+Once you're satisfied with how your model performs, it's ready to be deployed, and query it for predictions from utterances. Deploying a model makes it available for use through the [prediction API](/rest/api/language/2023-04-01/conversation-analysis-runtime/analyze-conversation).
 
 ## Prerequisites
 
-* A successfully [created project](create-project.md) 
+* A [created project](create-project.md) 
 * [Labeled utterances](tag-utterances.md) and successfully [trained model](train-model.md)
 * Reviewed the [model performance](view-model-evaluation.md) to determine how your model is performing.
 
@@ -45,7 +45,7 @@ After you have reviewed the model's performance and decide it's fit to be used i
 
 ## Swap deployments
 
-After you are done testing a model assigned to one deployment, you might want to assign it to another deployment. Swapping deployments involves:
+After you're done testing a model assigned to one deployment, you might want to assign it to another deployment. Swapping deployments involves:
 * Taking the model assigned to the first deployment, and assigning it to the second deployment. 
 * taking the model assigned to second deployment and assign it to the first deployment. 
 
@@ -89,7 +89,7 @@ You can [deploy your project to multiple regions](../../concepts/custom-features
 
 ## Unassign deployment resources
 
-When unassigning or removing a deployment resource from a project, you will also delete all the deployments that have been deployed to that resource's region.
+When unassigning or removing a deployment resource from a project, you'll also delete all the deployments that have been deployed to the resource's region.
 
 # [Language Studio](#tab/language-studio)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのデプロイに関する文書の修正"
}
```

### Explanation
この変更は、Azure AI サービスにおける「モデルのデプロイ」についてのドキュメントの修正を示しています。具体的には、日付の更新やテキストの軽微な修正が行われています。

変更内容には、モデルがどのようにデプロイされ、予測を取得するためにどのように活用されるかについての説明が含まれています。また、モデルのパフォーマンスを確認するための事前条件や展開の交換方法についての情報も更新されています。特に、文章の一部がより明瞭に修正され、ユーザーが必要とする関連情報が理解しやすくなっています。

全体として、この変更はドキュメントの正確性を向上させ、最新の情報を提供することを目的としています。ユーザーにとってより良い利用体験を提供するための重要な更新となっています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/train-model.md{#item-f5b164}

<details>
<summary>Diff</summary>
````diff
@@ -6,68 +6,141 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 04/29/2025
+ms.date: 06/23/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
 ---
 
-# Train your conversational language understanding model
+# Train a conversational language understanding model
 
-After you have completed [labeling your utterances](tag-utterances.md), you can start training a model. Training is the process where the model learns from your [labeled utterances](tag-utterances.md). <!--After training is completed, you will be able to [view model performance](view-model-evaluation.md).-->
+After you complete [labeling your utterances](tag-utterances.md), you can start training a model. Training is the process where the model learns from your [labeled utterances](tag-utterances.md). <!--After training is completed, you will be able to [view model performance](view-model-evaluation.md).-->
 
-To train a model, start a training job. Only successfully completed jobs create a model. Training jobs expire after seven days, after this time you will no longer be able to retrieve the job details. If your training job completed successfully and a model was created, it won't be affected by the job expiring. You can only have one training job running at a time, and you can't start other jobs in the same project. 
+To train a model, start a training job. Only successfully completed jobs create a model. Training jobs expire after seven days, then you can no longer retrieve the job details. If your training job completed successfully and a model was created, the job doesn't expire. You can only have one training job running at a time, and you can't start other jobs in the same fine tuning task.
 
-The training times can be anywhere from a few seconds when dealing with simple projects, up to a couple of hours when you reach the [maximum limit](../service-limits.md) of utterances.
+> [!NOTE]
+>
+> When using the **Quick Deploy** option, Conversational Language Understanding (CLU) automatically creates an instant training job to set up your CLU intent router using your selected `LLM` deployment.
 
-Model evaluation is triggered automatically after training is completed successfully. The evaluation process starts by using the trained model to run predictions on the utterances in the testing set, and compares the predicted results with the provided labels (which establishes a baseline of truth). <!--The results are returned so you can review the [model’s performance](view-model-evaluation.md).-->
+The training times can be anywhere from a few seconds for simple projects, up to several hours when you reach the [maximum limit](../service-limits.md) of utterances.
+
+Model evaluation is triggered automatically after training is completed successfully. The evaluation process starts by using the trained model to run predictions on the utterances in the testing set, and compares the predicted results with the provided labels (which establishes a baseline of truth). <!--The results are returned so you can review the [model's performance](view-model-evaluation.md).-->
 
 ## Prerequisites
 
-* A successfully [created project](create-project.md) with a configured Azure blob storage account
-* [Labeled utterances](tag-utterances.md)
+* **An active Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/free/cognitive-services).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor)
+* **A project created in the Azure AI Foundry**. For more information, *see* [Create an AI Foundry project](../../../../ai-foundry/how-to/create-projects.md)
+* [**Your labeled utterances**](tag-utterances.md) tagged for your fine tuning task.
+
 
 <!--See the [project development lifecycle](../overview.md#project-development-lifecycle) for more information.-->
 
-[!INCLUDE [Balance training data](../includes/balance-training-data.md)]
+## Balance training data
+
+When it comes to training data, try to keep your schema well-balanced. Including large quantities of one intent and few of another results in a model with bias towards particular intents.
+
+To address this scenario, you might need to down sample your training set. Or you might need to add to it. To down sample, you can:
 
+* Get rid of a certain percentage of the training data randomly.
+* Analyze the dataset and remove overrepresented duplicate entries, which is a more systematic manner.
 
+To add to the training set, in Language Studio, on the **Data labeling** tab, select **Suggest utterances**. Conversational Language Understanding sends a call to [Azure OpenAI](../../../openai/overview.md) to generate similar utterances.
+
+:::image type="content" source="../media/suggest-utterances.png" alt-text="Screenshot that shows an utterance suggestion in Language Studio." lightbox="../media/suggest-utterances.png":::
+
+You should also look for unintentional patterns in the training set. For example, look to see if the training set for a particular intent is all lowercase or starts with a particular phrase. In such cases, the model you train might learn these unintended biases in the training set instead of being able to generalize.
+
+We recommend that you introduce casing and punctuation diversity in the training set. If your model is expected to handle variations, be sure to have a training set that also reflects that diversity. For example, include some utterances in proper casing and some in all lowercase.
 
 ## Data splitting
 
 Before you start the training process, labeled utterances in your project are divided into a training set and a testing set. Each one of them serves a different function.
-The **training set** is used in training the model, this is the set from which the model learns the labeled utterances. 
-The **testing set** is a blind set that isn't introduced to the model during training but only during evaluation. 
+The **training set** is used in training the model, the set from which the model learns the labeled utterances.
+The **testing set** is a blind set that isn't introduced to the model during training but only during evaluation.
 
-After the model is trained successfully, the model can be used to make predictions from the utterances in the testing set. These predictions are used to calculate [evaluation metrics](../concepts/evaluation-metrics.md). 
-It is recommended to make sure that all your intents and entities are adequately represented in both the training and testing set.
+After the model is trained successfully, the model can be used to make predictions from the utterances in the testing set. These predictions are used to calculate [evaluation metrics](../concepts/evaluation-metrics.md).
+We recommend that you make sure that all your intents and entities are adequately represented in both the training and testing set.
 
 Conversational language understanding supports two methods for data splitting:
 
-* **Automatically splitting the testing set from training data**: The system will split your tagged data between the training and testing sets, according to the percentages you choose. The recommended percentage split is 80% for training and 20% for testing. 
+* **Automatically splitting the testing set from training data**: The system splits your tagged data between the training and testing sets, according to the percentages you choose. The recommended percentage split is 80% for training and 20% for testing.
 
  > [!NOTE]
- > If you choose the **Automatically splitting the testing set from training data** option, only the data assigned to training set will be split according to the percentages provided.
+ > If you choose the **Automatically splitting the testing set from training data** option, only the data assigned to a training set is split according to the percentages provided.
 
-* **Use a manual split of training and testing data**: This method enables users to define which utterances should belong to which set. This step is only enabled if you have added utterances to your testing set during [labeling](tag-utterances.md).
+* **Use a manual split of training and testing data**: This method enables users to define which utterances should belong to which set. This step is only enabled if you added utterances to your testing set during [labeling](tag-utterances.md).
 
 ## Training modes
 
-CLU supports two modes for training your models
+Conversational Language Understanding (CLU) supports two modes for training your models
 
-* **Standard training** uses fast machine learning algorithms to train your models relatively quickly. This is currently only available for **English** and is disabled for any project that doesn't use English (US), or English (UK) as its primary language. This training option is free of charge. Standard training allows you to add utterances and test them quickly at no cost. The evaluation scores shown should guide you on where to make changes in your project and add more utterances. Once you’ve iterated a few times and made incremental improvements, you can consider using advanced training to train another version of your model.
+* **Standard training** uses fast machine learning algorithms to quickly train your models. This training level is currently only available for **English** and is disabled for any project that doesn't use English (US), or English (UK) as its primary language. This training option is free of charge. Standard training allows you to add utterances and test them quickly free of charge. The evaluation scores shown should guide you on where to make changes in your project and add more utterances. While standard training is best for testing and updating your model quickly, you should see better model quality when using advanced training. While standard training is best for testing and updating your model quickly, you should see better model quality when using advanced training. Once you iterate a few times and made incremental improvements, you can consider using advanced training to train another version of your model.
 
-* **Advanced training** uses the latest in machine learning technology to customize models with your data. This is expected to show better performance scores for your models and will enable you to use the [multilingual capabilities](../language-support.md#multi-lingual-option) of CLU as well. Advanced training is priced differently. See the [pricing information](https://azure.microsoft.com/pricing/details/cognitive-services/language-service) for details.
+* **Advanced training** uses the latest in machine learning technology to customize models with your data. This training level is expected to show better performance scores for your models and enables you to use the [multilingual capabilities](../language-support.md#multi-lingual-option) of CLU as well. Advanced training is priced differently. See the [pricing information](https://azure.microsoft.com/pricing/details/cognitive-services/language-service) for details.
 
-Use the evaluation scores to guide your decisions. There might be times where a specific example is predicted incorrectly in advanced training as opposed to when you used standard training mode. However, if the overall evaluation results are better using advanced, then it is recommended to use your final model. If that isn’t the case and you are not looking to use any multilingual capabilities, you can continue to use model trained with standard mode.
+Use the evaluation scores to guide your decisions. There may be times where a specific example is predicted incorrectly in advanced training as opposed to when you used standard training mode. However, if the overall evaluation results are better using advanced training, then we recommend that you use that model as your final model. If that isn't the case and you aren't looking to use any multilingual capabilities, you can continue to use model trained with standard mode.
 
 > [!Note]
-> You should expect to see a difference in behaviors in intent confidence scores between the training modes as each algorithm calibrates their scores differently. 
+> You should expect to see a difference in behaviors in intent confidence scores between the training modes as each algorithm calibrates their scores differently.
+
+## Train your model
+
+# [Azure AI Foundry](#tab/ai-foundry)
+
+1. Navigate to the [Azure AI Foundry](https://ai.azure.com/).
+1. If you aren't already signed in, the portal prompts you to do so with your Azure credentials.
+1. Once signed in, you can create or access your existing projects within Azure AI Foundry.
+1. If you're not already at your project for this task, select it.
+1. Select Fine-tuning from the left navigation panel.
+
+   :::image type="content" source="../media/select-fine-tuning.png" alt-text="Screenshot of fine-tuning selector in the Azure AI Foundry.":::
+
+1. Select **the AI Service fine-tuning** tab and then **+ Fine-tune** button.
+
+   :::image type="content" source="../media/fine-tune-button.png" alt-text="Screenshot of fine-tuning button in the Azure AI Foundry.":::
+
+1. From **Create service fine-tuning** window, choose the **Conversational language understanding** tab then select **Next**.
+
+   :::image type="content" source="../media/select-project.png" alt-text="Screenshot of conversational language understanding tab in the Azure AI Foundry.":::
 
-## Train model 
+1. In **Create CLU fine tuning task** window, complete the **Name** and **Language** fields. If you're using the free **Standard Training** mode, select **English** for the language field.
 
-# [Language Studio](#tab/language-studio)
+    > [!NOTE]
+    >
+    > * **Standard training** enables faster training times and quicker iterations; however it's only available for English.
+    > * **Advanced training** includes longer training durations and is supported for English, other languages, and multilingual projects.
+    > * For more information, *see* [Training modes](#training-modes).
 
-[!INCLUDE [Train model](../includes/language-studio/train-model.md)]
+1. From the immediate left navigation panel, choose **Train model**.
+
+   :::image type="content" source="../media/train-fine-tuning-model.png" alt-text="Screenshot of the train model selection in the Azure AI Foundry.":::
+
+1. Next, select the **+ Train model** button from the main window.
+1. In the **Train a new model** window, select one of the following:
+
+   * **Create a new training model**. Enter a new **Model name**
+   * **Overwrite an existing model name**. Replace an existing model trained on the new data.
+1. Select **Your current training version**. The training version is the algorithm that determines how your model learns from your data. The machine learning used to train models is regularly updated. We recommend using the latest version for training, as it underwent thorough testing and provides the most balanced model predictions from your data.
+
+   :::image type="content" source="../media/select-mode.png" alt-text="Screenshot of select a mode options in the Azure AI Foundry." :::
+
+1. Select **Next**.
+
+1. Select one of the **Data splitting** methods presented in the **Train a new model** window:
+
+   * **Automatically split the testing set from training data** enables the system to split your utterances between the training and testing sets, according to the specified percentages.
+   * **Use a manual split of training and testing data** enables the system to use the training and testing sets that you assigned and labeled to create your custom model. ***This option is only available if you have added utterances to your testing set when you labeled your utterances**.
+
+      :::image type="content" source="../media/data-splitting.png" alt-text="Screenshot of data splitting option in the Azure AI Foundry.":::
+
+1. Select **Next** and then select **Create**.
+
+1. Choose the training job ID from the list. A panel appears that details the training progress, job status, and other details for this job.
+
+> [!NOTE]
+> * Only successfully completed training jobs generate models.
+> * Training can take from a few minutes to a few hours based on the count of utterances.
+> * You can only have one training job running at a time. You can't start other training jobs within the same project until the running job is completed.
 
 # [REST APIs](#tab/rest-api)
 
@@ -77,26 +150,30 @@ Use the evaluation scores to guide your decisions. There might be times where a
 
 ### Get training job status
 
-Training could take sometime depending on the size of your training data and complexity of your schema. You can use the following request to keep polling the status of the training job until it is successfully completed.
+Training could take some time depending on the size of your training data and complexity of your schema. You can use the following request to keep polling the status of the training job until it successfully completes.
 
 [!INCLUDE [get training model status](../includes/rest-api/get-training-status.md)]
 
 ---
 
 ### Cancel training job
 
-# [Language Studio](#tab/language-studio)
+# [Azure AI Foundry](#tab/ai-foundry)
 
-[!INCLUDE [Cancel training](../includes/language-studio/cancel-training.md)]
+When you're done with your custom model, you can delete the deployment and model. You can also delete the training and validation files you uploaded to the service, if needed:
+
+* To delete your custom model, on the left navigation pane select **My assets** → **Models + endpoints**. Choose the custom model to delete from the **Model deployments** tab, and then select **Delete**.
+* To delete your training and validation files uploaded for training, on the left navigation pane select **Data + indexes**. Choose the file to delete, and then select **Delete**.
+
+  :::image type="content" source="../media/my-assets.png" alt-text="Screenshot of my assets section in the Azure AI Foundry.":::
 
 # [REST APIs](#tab/rest-api)
 
 [!INCLUDE [Cancel training](../includes/rest-api/cancel-training.md)]
 
 ---
 
-
 ## Next steps
 
-* [Model evaluation metrics](../concepts/evaluation-metrics.md)
+Review your model's performance with [model evaluation metrics](../concepts/evaluation-metrics.md).
 <!--* [Deploy and query the model](./deploy-model.md)-->
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのトレーニングに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI サービスにおける「会話型言語理解モデルのトレーニング」に関するドキュメントを更新したものです。主に、文書の内容を改善し、新情報を追加することで、ユーザーがモデルをトレーニングする際のプロセスや要件をより明確に理解できるようにしています。

変更の一部には、新しい前提条件の追加や、トレーニングモードに関する具体的な情報が含まれています。たとえば、トレーニングの際のデータのバランスを保つ方法や、自動データ分割の手法についての説明が強化されました。また、Azure AI Foundryを使用してモデルをトレーニングする手順が詳細に記載されており、ユーザーが実行手順に従いやすくなっています。

修正された内容は、トレーニングプロセスを簡単に理解し、効果的に利用できるようにするためのものであり、全体としてドキュメントの信頼性を向上させています。この更新により、ユーザーがモデルのトレーニングをよりスムーズに実施できることを期待しています。

## articles/ai-services/language-service/conversational-language-understanding/includes/balance-training-data.md{#item-768433}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.author: lajanuar
 
 ## Balance training data
 
-When it comes to training data, try to keep your schema well balanced. Including large quantities of one intent and very few of another results in a model that's biased toward particular intents.
+When it comes to training data, try to keep your schema well balanced. Including large quantities of one intent and few of another results in a model with bias towards particular intents.
 
 To address this scenario, you might need to downsample your training set. Or you might need to add to it. To downsample, you can:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トレーニングデータのバランスに関する文の修正"
}
```

### Explanation
この変更は、トレーニングデータのバランスに関するドキュメントの一節を修正したものです。特に、特定の意図の数が多く、他の意図が非常に少ない状態がモデルに与える影響についての説明が調整されています。

具体的には、「モデルが特定の意図に偏る」から「モデルが特定の意図に偏りを持つ」に表現が変更されており、言葉の明確さが向上しました。これにより、トレーニングデータをバランス良く保つことの重要性がより強調されています。

この修正は、ユーザーがモデルのトレーニングを行う際に、データの偏りを理解し、適切なトレーニングデータの準備を行うために役立つ情報を提供することを目的としています。全体として、ドキュメントの品質と明瞭さが向上しています。

## articles/ai-services/language-service/conversational-language-understanding/media/configure-resources/add-role-assignment.png{#item-3efc05}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "役割割り当てを追加するための画像の追加"
}
```

### Explanation
この変更は、「役割割り当てを追加する」ための手順を示す画像ファイルが新たに追加されたことを示しています。この画像は、Azure AI サービスの会話型言語理解におけるリソース設定を行う際に役立つビジュアルコンテンツであり、ユーザーが役割を正しく割り当てるための具体的な手順を視覚的に理解するのを助けます。

追加された画像は、設定プロセスの明確化に寄与しており、ドキュメントの全体的な使いやすさを向上させる要素となります。特に技術的な文書においては、文字情報だけでなく図や画像があることで、内容をより直感的に理解できるようになります。この更新は、ユーザーの利便性を向上させるための重要なステップです。

## articles/ai-services/language-service/conversational-language-understanding/media/configure-resources/ai-foundry-management-center.png{#item-084dfd}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "AIファウンドリ管理センターの画像の追加"
}
```

### Explanation
この変更は、AIファウンドリ管理センターを示す新しい画像ファイルが追加されたことを示しています。この画像は、Azure AI サービスにおける会話型言語理解のリソース設定や管理に関する情報を視覚的に提供することを目的としています。

追加された画像は、ユーザーがAIファウンドリ管理センターのインターフェースや機能を直感的に理解できるようにするための重要なコンポーネントです。ビジュアルを用いた手順の説明は、文章だけでは理解が難しい部分を補完し、ユーザーの操作性や学習を助ける効果があります。この更新により、ドキュメント全体の情報価値が向上し、利用者にとって役立つリソースとなるでしょう。

## articles/ai-services/language-service/conversational-language-understanding/media/configure-resources/cognitive-services-user.png{#item-0a9def}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "認知サービスユーザーの画像の追加"
}
```

### Explanation
この変更は、認知サービスユーザーを示す新しい画像ファイルが追加されたことを示しています。この画像は、Azure AI サービスの会話型言語理解の設定過程において、認知サービスの利用者に関するビジュアル情報を提供するためのものです。

追加されたこの画像によって、ユーザーは認知サービスのユーザーインターフェースや操作方法をより視覚的に理解できるようになります。特に技術的な文書では、画像や図があることで情報の受け取りやすさが向上し、ユーザーが手順を確実に実行するために必要なコンテキストを提供します。この更新は、ドキュメントの価値を高め、使用者に対するサポートを強化するものです。

## articles/ai-services/language-service/conversational-language-understanding/media/configure-resources/connect-language-resource.png{#item-25a810}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "言語リソースを接続するための画像の追加"
}
```

### Explanation
この変更は、言語リソースを接続するプロセスを示す新しい画像ファイルが追加されたことを示しています。この画像は、Azure AI サービスの会話型言語理解において、リソースの接続方法に関するビジュアルガイドを提供するためのものです。

新たに追加された画像により、ユーザーは言語リソースの設定や接続手順を視覚的に把握でき、その理解が深まります。テキストだけで情報を伝えるのが難しい場合、画像を利用することで手順を直感的に理解できるようになります。この更新は、ユーザーエクスペリエンスを向上させ、利用者が手順をスムーズに実行できるようにするための重要な要素となります。

## articles/ai-services/language-service/conversational-language-understanding/media/configure-resources/managed-identity.png{#item-2998de}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "管理されたアイデンティティに関する画像の追加"
}
```

### Explanation
この変更は、管理されたアイデンティティに関連する新しい画像ファイルが追加されたことを示しています。この画像は、Azure AI サービスの会話型言語理解の設定において、管理されたアイデンティティの利用方法を視覚的に説明するためのものです。

この追加により、ユーザーは管理されたアイデンティティの設定および使用方法をより直感的に理解できるようになります。複雑な手順を伴う技術的な操作について、画像を通じて具体的なビジュアルサポートを提供することは、ユーザーがステップを容易に追えるようにし、最終的には全体のユーザーエクスペリエンスを向上させることに寄与します。この変更は、ドキュメントの有用性を高めるとともに、利用者の理解を深めることを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/media/configure-resources/new-connection.png{#item-3f47f6}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい接続に関する画像の追加"
}
```

### Explanation
この変更は、新しい接続に関する画像ファイルが追加されたことを示しています。この画像は、Azure AI サービスの会話型言語理解における新しい接続の設定手順を視覚的に支援するために設計されています。

新しく追加された画像により、ユーザーは新しい接続の手続きをより容易に理解できるようになります。操作手順を視覚的に示すことで、ユーザーは複雑な設定を直感的に把握でき、円滑な導入が可能となります。この更新は、具体的なビジュアルガイドを提供し、利用者が手順をスムーズに実行できるようにするために重要です。全体として、この変更はドキュメントの効果を高め、ユーザー体験を向上させることを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/media/data-splitting.png{#item-d14f85}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "データ分割に関する画像の追加"
}
```

### Explanation
この変更は、データ分割に関連する新しい画像ファイルが追加されたことを示しています。この画像は、Azure AI サービスの会話型言語理解においてデータをどのように分割するかを視覚的に表現するもので、ユーザーにとっての理解を容易にすることを目的としています。

追加された画像により、ユーザーはデータ分割のプロセスを視覚的に把握しやすくなります。データを効果的に分割することは、モデルのトレーニングやテストにおいて非常に重要なステップであり、ビジュアルサポートがあることで事例を具体的に理解できるようになるでしょう。この変更は、ユーザーが手順や概念をより良く理解できるようにサポートすることを目指しており、ドキュメント全体の質を向上させる役割を果たします。

## articles/ai-services/language-service/conversational-language-understanding/media/fine-tune-button.png{#item-e38384}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニングボタンに関する画像の追加"
}
```

### Explanation
この変更は、ファインチューニングボタンに関する新しい画像ファイルが追加されたことを示しています。この画像は、Azure AI サービスの会話型言語理解機能において、ユーザーがモデルをファインチューニングするための操作を視覚的に支援することを目的としています。

追加された画像によって、ユーザーはファインチューニングボタンの位置や使用方法を一目で理解できます。このビジュアルサポートは、初心者や非技術者にとって特に有用であり、操作手順をより簡単に実行できるようになるでしょう。この変更は、全体的なユーザー体験を向上させ、ドキュメントが提供する情報のクリアさを高める役割を果たします。

## articles/ai-services/language-service/conversational-language-understanding/media/my-assets.png{#item-4bed5a}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "マイアセットに関する画像の追加"
}
```

### Explanation
この変更は、「マイアセット」に関連する新しい画像ファイルが追加されたことを示しています。この画像は、Azure AI サービスの会話型言語理解機能において、ユーザーが自分のアセットを管理する方法を視覚的に表現することを目的としています。

追加された画像により、ユーザーは自分のアセットの表示方法や管理の仕方を容易に理解できるようになります。視覚的なガイダンスが提供されることで、特に新しいユーザーに対して操作がより直感的になり、効率的にアセットを扱う手助けとなります。この変更は、ドキュメントの有用性を向上させ、ユーザーが機能を効果的に活用できるようにすることを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/media/select-fine-tuning.png{#item-745dc5}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニング選択に関する画像の追加"
}
```

### Explanation
この変更は、ファインチューニングを選択するための新しい画像ファイルが追加されたことを示しています。この画像は、Azure AI サービスの会話型言語理解機能において、ユーザーがファインチューニングのプロセスを視覚的に理解できるようサポートすることが目的です。

追加された画像は、ユーザーがファインチューニングオプションを選択する際のインターフェースまたは手順を示しており、特に初心者にとって使い方が明確になります。この視覚的素材があれば、ユーザーは手続きに対する理解を深めることができ、よりスムーズな操作が可能となります。この変更は、ドキュメントの可読性を向上させ、ユーザーが必要な情報を容易に得られるようにするための重要な要素となります。

## articles/ai-services/language-service/conversational-language-understanding/media/select-mode.png{#item-b0b2a0}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "モード選択に関する画像の追加"
}
```

### Explanation
この変更は、モードを選択するための新しい画像ファイルが追加されたことを示しています。この画像は、Azure AI サービスの会話型言語理解機能において、ユーザーが異なるモードを選択する際の手助けをすることを目的としています。

追加された画像は、利用可能なモードやそれぞれのモードに関する情報を視覚的に提示するもので、ユーザーが選択の過程での理解を深めることができます。視覚的なガイドラインが提供されることで、特に初心者や新しいユーザーに対して、インターフェースの操作がより直感的になり、効率的に機能を利用できるようになります。この変更によって、ドキュメントのアクセシビリティが向上し、ユーザーがモード選択に関する情報を迅速に獲得できるようになることが期待されます。

## articles/ai-services/language-service/conversational-language-understanding/media/select-project.png{#item-0e6492}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "プロジェクト選択に関する画像の追加"
}
```

### Explanation
この変更は、プロジェクトを選択するための新しい画像ファイルが追加されたことを示しています。この画像は、Azure AI サービスの会話型言語理解機能において、ユーザーがプロジェクトを選択する際に役立つ視覚的なガイドです。

追加された画像は、ユーザーが複数のプロジェクトから適切なものを選択する手順を視覚化しており、特に新しいユーザーや経験の浅いユーザーに対して操作を簡単に理解できるようにしています。これにより、プロジェクト選択に関する情報を直感的に把握できるため、ユーザーがよりスムーズに機能を利用できるようになります。この変更は、ドキュメント全体の理解を助け、ユーザー体験の向上に寄与する重要な要素となります。

## articles/ai-services/language-service/conversational-language-understanding/media/train-fine-tuning-model.png{#item-1912bc}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニングモデルのトレーニングに関する画像の追加"
}
```

### Explanation
この変更は、ファインチューニングモデルをトレーニングするための新しい画像ファイルが追加されたことを示しています。この画像は、Azure AI サービスの会話型言語理解機能において、ユーザーがモデルのファインチューニングプロセスを理解しやすくするためのビジュアルガイドとして機能します。

追加された画像は、モデルのトレーニングに必要な手順やポイントを視覚的に示しており、特に初めてこのプロセスを行うユーザーにとって参考になる内容です。画像を通じて、ユーザーはトレーニングの流れや重要なステップを直感的に把握でき、作業の効率を高めることが期待されます。この変更は、ドキュメントのアクセシビリティを改善し、ユーザーの学習体験を豊かにすることを目的としています。

## articles/ai-services/language-service/custom-text-classification/how-to/tag-data.md{#item-e70f6f}

<details>
<summary>Diff</summary>
````diff
@@ -7,14 +7,14 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/21/2024
+ms.date: 06/30/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
 ---
 
 # Label text data for training your model 
 
-Before training your model you need to label your documents with the classes you want to categorize them into. Data labeling  is a crucial step in development lifecycle; in this step you can create the classes you want to categorize your data into and label your documents with these classes. This data will be used in the next step when training your model so that your model can learn from the labeled data. If you already have labeled data, you can directly [import](create-project.md) it into your project but you need to make sure that your data follows the [accepted data format](../concepts/data-formats.md).
+Before training your model, you need to label your documents with the classes you want to categorize them into. Data labeling  is a crucial step in development lifecycle; in this step you can create the classes you want to categorize your data into and label your documents with these classes. This data will be used in the next step when training your model so that your model can learn from the labeled data. If you already labeled your data, you can directly [import](create-project.md) it into your project but you need to make sure that your data follows the [accepted data format](../concepts/data-formats.md).
 
 Before creating a custom text classification model, you need to have labeled data first. If your data isn't labeled already, you can label it in the [Language Studio](https://aka.ms/languageStudio). Labeled data informs the model how to interpret text, and is used for training and evaluation.
 
@@ -23,19 +23,19 @@ Before creating a custom text classification model, you need to have labeled dat
 Before you can label data, you need:
 
 * [A successfully created project](create-project.md) with a configured Azure blob storage account, 
-* Documents containing text data that have [been uploaded](design-schema.md#data-preparation) to your storage account.
+* Documents containing the [uploaded](design-schema.md#data-preparation) text data in your storage account.
 
 See the [project development lifecycle](../overview.md#project-development-lifecycle) for more information.
 
 ## Data labeling guidelines
 
-After [preparing your data, designing your schema](design-schema.md) and [creating your project](create-project.md), you will need to label your data. Labeling your data is important so your model knows which documents will be associated with the classes you need. When you label your data in [Language Studio](https://aka.ms/languageStudio) (or import labeled data), these labels will be stored in the JSON file in your storage container that you've connected to this project. 
+After [preparing your data, designing your schema](design-schema.md) and [creating your project](create-project.md), you will need to label your data. Labeling your data is important so your model knows which documents will be associated with the classes you need. When you label your data in [Language Studio](https://aka.ms/languageStudio) (or import labeled data), these labels are stored in the JSON file in your storage container that you've connected to this project. 
 
 As you label your data, keep in mind:
 
 * In general, more labeled data leads to better results, provided the data is labeled accurately.
 
-* There is no fixed number of labels that can guarantee your model will perform the best. Model performance on possible ambiguity in your [schema](design-schema.md), and the quality of your labeled data. Nevertheless, we recommend 50 labeled documents per class.
+* There is no fixed number of labels that can guarantee your model performs the best. Model performance on possible ambiguity in your [schema](design-schema.md), and the quality of your labeled data. Nevertheless, we recommend 50 labeled documents per class.
 
 ## Label your data
 
@@ -61,7 +61,7 @@ Use the following steps to label your data:
 
     # [Multi label classification](#tab/multi-classification)
     
-    **Multi label classification**: your file can be labeled with multiple classes, you can do so by selecting all applicable check boxes next to the classes you want to label this document with.
+    **Multi label classification**: your file can be labeled with multiple classes. You can do so by selecting all applicable check boxes next to the classes you want to label this document with.
     
     :::image type="content" source="../media/multiple.png" alt-text="A screenshot showing the multiple label classification tag page." lightbox="../media/multiple.png":::
     
@@ -77,24 +77,24 @@ Use the following steps to label your data:
 
 6. In the right side pane under the **Labels** pivot you can find all the classes in your project and the count of labeled instances per each.
 
-7. In the bottom section of the right side pane you can add the current file you are viewing to the training set or the testing set. By default all the documents are added to your training set. Learn more about [training and testing sets](train-model.md#data-splitting) and how they are used for model training and evaluation.
+7. In the bottom section of the right side pane you can add the current file you're viewing to the training set or the testing set. By default all the documents are added to your training set. Learn more about [training and testing sets](train-model.md#data-splitting) and how they're used for model training and evaluation.
 
     > [!TIP]
-    > If you are planning on using **Automatic** data splitting use the default option of assigning all the documents into your training set.
+    > If you're planning on using **Automatic** data splitting, use the default option of assigning all the documents into your training set.
 
 8. Under the **Distribution** pivot you can view the distribution across training and testing sets. You have two options for viewing:
    * *Total instances* where you can view count of all labeled instances of a specific class.
    * *documents with at least one label* where each document is counted if it contains at least one labeled instance of this class.
 
-9. While you're labeling, your changes will be synced periodically, if they have not been saved yet you will find a warning at the top of your page. If you want to save manually, select **Save labels** button at the bottom of the page.
+9. While you're labeling, your changes are synced periodically, if they have not been saved yet you will find a warning at the top of your page. If you want to save manually, select **Save labels** button at the bottom of the page.
 
 ## Remove labels
 
 If you want to remove a label, uncheck the button next to the class.
 
 ## Delete or classes
 
-To delete a class, select the delete icon next to the class you want to remove. Deleting a class will remove all its labeled instances from your dataset.
+To delete a class, select the icon next to the class you want to remove. Deleting a class will remove all its labeled instances from your dataset.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データタグ付けに関するドキュメントの修正"
}
```

### Explanation
この変更は、データタグ付けに関するドキュメントに対する小規模な修正を示しています。テキストが10行追加され、同じ数だけ削除されており、全体として20行の変更が行われました。この更新は、文章の文法や明確さを改善し、読者が内容をより理解しやすくすることを目的としています。

具体的な変更点には、文中の冗長な表現の修正や、言い回しの調整が含まれています。例えば、「あなたのデータがまだラベル付けされていない場合」という文が、「あなたのデータが既にラベル付けされている場合」に変更され、より簡潔で明瞭な表現に改善されています。

また、いくつかの文では、「あなたが現在閲覧しているファイル」や「自動データ分割を使用する場合」という部分が、より自然な口語表現にアップデートされています。これにより、ドキュメント全体が一層利用しやすくなり、特に新しいユーザーに対するサポートが強化されることが期待されます。この変更は、情報の伝達力を向上させ、ユーザーの体験を円滑にするための重要なステップです。

## articles/ai-services/language-service/custom-text-classification/tutorials/triage-email.md{#item-47cadc}

<details>
<summary>Diff</summary>
````diff
@@ -7,11 +7,11 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: tutorial
-ms.date: 11/21/2024
+ms.date: 06/30/2025
 ms.author: lajanuar
 ---
 
-# Tutorial: Triage incoming emails with power automate
+# Tutorial: Triage incoming emails with Power Automate
 
 In this tutorial you will categorize and triage incoming email using custom text classification. Using this [Power Automate](/power-automate/getting-started) flow, when a new email is received, its contents will have a classification applied, and depending on the result, a message will be sent to a designated channel on [Microsoft Teams](https://www.microsoft.com/microsoft-teams).
 
@@ -27,7 +27,7 @@ In this tutorial you will categorize and triage incoming email using custom text
 
 ## Create a Power Automate flow
 
-1. [Sign in to power automate](https://make.powerautomate.com/)
+1. [Sign in to Power Automate](https://make.powerautomate.com/)
 
 2. From the left side menu, select **My flows** and create a **Automated cloud flow**
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メールのトリアージに関するチュートリアルの修正"
}
```

### Explanation
この変更は、メールのトリアージに関するチュートリアルドキュメントの表現を向上させるための小規模な修正を示しています。この修正では、合計6行が変更され、3行が追加および削除されています。

具体的には、タイトルや見出しのスタイルを統一するために「Power Automate」の誤った表記が削除され、正しい表記に修正されています。また、日付の更新が行われており、作成日が新しい日付に変更されています。これにより、ドキュメントが最新の情報を反映するようになり、より一貫性のあるフォーマットで提供されています。

全体として、この更新はチュートリアルの可読性と明確さを向上させ、ユーザーがメールのトリアージを実施する方法を理解しやすくすることを目的としています。特に、ユーザーがPower Automateを利用する際の指針として、より信頼性の高い情報源となることが期待されます。

## articles/ai-services/language-service/language-detection/language-support.md{#item-2c8ef2}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/21/2024
+ms.date: 06/30/2025
 ms.author: lajanuar
 ms.custom: language-service-language-detection, ignite-2024
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サポートに関するドキュメントの日付更新"
}
```

### Explanation
この変更は、言語サポートに関するドキュメントの日付を更新するための小規模な修正を示しています。具体的には、1行の追加と1行の削除が行われ、全体で2行が変更されています。

主な変更点は、文書の日付が「2024年11月21日」から「2025年6月30日」に変更されたことです。この更新により、ドキュメントが最新の情報を反映し、読者に対して正確な時点での情報を提供することが可能になります。

この修正は、特に文書の利用者にとって重要であり、更新情報を知ることで、彼らは提供されているリソースが最新であることを認識し、信頼性を高めることが期待されます。全体として、この変更は簡潔であるものの、ドキュメントの関連性と信頼性を維持するために重要です。

## articles/ai-services/language-service/orchestration-workflow/quickstart.md{#item-bee292}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 11/21/2024
+ms.date: 06/30/2025
 ms.author: lajanuar
 ms.custom: language-service-clu, mode-other
 zone_pivot_groups: usage-custom-language-features
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートガイドの日付更新"
}
```

### Explanation
この変更は、オーケストレーションワークフローのクイックスタートガイドに関する文書の日付を更新するための小規模な修正を示しています。今回の変更では、1行が追加され、1行が削除され、合計で2行の修正が行われました。

具体的には、ドキュメントの日付が「2024年11月21日」から「2025年6月30日」に変更されています。この更新により、文書が最新の情報を反映し、読者が利用可能なリソースの信頼性を理解しやすくなります。

このような小さな変更であっても、ドキュメントの整合性と信頼性を保つために重要です。読者にとって、最新の日付は情報の新鮮さを示すものであり、使用する際の安心感を与えることが期待されます。全体として、この修正は、ユーザーが必要な情報を適切に把握する手助けをするために重要な役割を果たします。

## articles/ai-services/language-service/question-answering/concepts/azure-resources.md{#item-34fc37}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-language
 ms.topic: conceptual
 author: laujan
 ms.author: lajanuar
-ms.date: 11/21/2024
+ms.date: 06/30/2025
 ms.custom: language-service-question-answering
 ---
 
@@ -34,7 +34,7 @@ Typically there are three parameters you need to consider:
 
     * The throughput for custom question answering is currently capped at 10 text records per second for both management APIs and prediction APIs.
 
-    * This should also influence your **Azure AI Search** SKU selection, see more details [here](/azure/search/search-sku-tier). Additionally, you might need to adjust Azure AI Search [capacity](/azure/search/search-capacity-planning) with replicas.
+    * This should also influence your **Azure AI Search** selection, see more details [here](/azure/search/search-sku-tier). Additionally, you might need to adjust Azure AI Search [capacity](/azure/search/search-capacity-planning) with replicas.
 
 * **Size and the number of projects**: Choose the appropriate [Azure search SKU](https://azure.microsoft.com/pricing/details/search/) for your scenario. Typically, you decide the number of projects you need based on number of different subject domains. One subject domain (for a single language) should be in one project.
 
@@ -58,7 +58,7 @@ The following table gives you some high-level guidelines.
 ## Recommended settings
 
 
-The throughput for custom question answering is currently capped at 10 text records per second for both management APIs and prediction APIs. To target 10 text records per second for your service, we recommend the S1 (one instance) SKU of Azure AI Search.
+The throughput for custom question answering is currently capped at 10 text records per second for both management APIs and prediction APIs. To target 10 text records per second for your service, we recommend the S1 (one instance) tier of Azure AI Search.
 
 
 ## Keys in custom question answering
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureリソースに関するドキュメントのテキスト修正"
}
```

### Explanation
この変更は、質問応答の概念に関する「Azureリソース」ドキュメント内のテキストを修正するための小規模な更新を示しています。具体的には、3行の追加と3行の削除が行われ、全体で6行が変更されています。

主な修正点としては、以下の内容が挙げられます：

1. 文書の日付が「2024年11月21日」から「2025年6月30日」に更新されました。これは、ドキュメントの有効性を確保するため的重要です。
2. 「Azure AI Search SKU選択」という表現が「Azure AI Search選択」と変更され、意味が明確になっています。
3. 「S1 (one instance) SKU」が「S1 (one instance) tier」に変更され、用語の一貫性が保たれました。

これにより、文書全体の明瞭さと整合性が向上し、読者が必要な情報をより理解しやすくなります。また、文書の信頼性や関連性を維持するために、最新の情報に基づく更新が行われていることが示されています。この修正は、情報提供の質を向上させるために重要な役割を果たします。

## articles/ai-services/language-service/question-answering/how-to/authoring.md{#item-855d84}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.service: azure-ai-language
 author: laujan
 ms.author: lajanuar
 ms.topic: how-to
-ms.date: 11/21/2024
+ms.date: 06/30/2025
 ---
 
 # Authoring API
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著作に関するドキュメントの日付更新"
}
```

### Explanation
この変更は、著作に関するドキュメントの「著作API」に関する部分の日付を更新するための小規模な修正を示しています。具体的には、1行が追加され、1行が削除され、合計で2行の修正が行われました。

主な修正点は、ドキュメントの日付が「2024年11月21日」から「2025年6月30日」に変更されたことです。この更新は、文書が最新の情報を反映していることを示し、利用者に対して信頼性を提供します。

こうした小さな変更は、情報の正確性と関連性を保つために重要であり、読者が文書を利用する際に安心感を与えます。全体として、この修正は、文書が常に最新の状態を維持し、利用者にとって価値のある情報源であることを目指しています。

## articles/ai-services/language-service/question-answering/how-to/chit-chat.md{#item-fe639e}

<details>
<summary>Diff</summary>
````diff
@@ -1,20 +1,20 @@
 ---
 title: Adding chitchat to a custom question answering project
 titleSuffix: Azure AI services
-description: Adding personal chitchat to your bot makes it more conversational and engaging when you create a project. Custom question answering allows you to easily add a pre-populated set of the top chitchat, into your projects.
+description: Adding personal chitchat to your bot makes it more conversational and engaging when you create a project. Custom question answering allows you to easily add a prepopulated set of the top chitchat, into your projects.
 #services: cognitive-services
 manager: nitinme
 author: laujan
 ms.author: lajanuar
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/21/2024
+ms.date: 06/30/2025
 ms.custom: language-service-question-answering
 ---
 
 # Use chitchat with a project
 
-Adding chitchat to your bot makes it more conversational and engaging. The chitchat feature in custom question answering allows you to easily add a pre-populated set of the top chitchat, into your project. This can be a starting point for your bot's personality, and it will save you the time and cost of writing them from scratch.
+Adding chitchat to your bot makes it more conversational and engaging. The chitchat feature in custom question answering allows you to easily add a prepopulated set of the top chitchat, into your project. This can be a starting point for your bot's personality, and it will save you the time and cost of writing them from scratch.
 
 This dataset has about 100 scenarios of chitchat in the voice of multiple personas, like Professional, Friendly and Witty. Choose the persona that most closely resembles your bot's voice. Given a user query, custom question answering tries to match it with the closest known chitchat question and answer.
 
@@ -70,7 +70,7 @@ To turn the views for context and metadata on and off, select **Show columns** i
 
 ## Add more chitchat questions and answers
 
-You can add a new chitchat question pair that is not in the predefined data set. Ensure that you are not duplicating a question pair that is already covered in the chitchat set. When you add any new chitchat question pair, it gets added to your **Editorial** source. To ensure the ranker understands that this is chitchat, add the metadata key/value pair "Editorial: chitchat", as seen in the following image:
+You can add a new chitchat question pair that is not in the predefined data set. Ensure that you are not duplicating a question pair that is already covered in the chitchat set. When you add any new chitchat question pair, it gets added to your **Editorial** source. To ensure the ranker understands that this is chitchat, add the metadata key/value pair "Editorial: chitchat," as seen in the following image:
 
 :::image type="content" source="../media/chit-chat/add-new-chit-chat.png" alt-text="Add chitchat question answer pairs" lightbox="../media/chit-chat/add-new-chit-chat.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チットチャットに関するドキュメントのテキスト修正"
}
```

### Explanation
この変更は、「チットチャット」に関するドキュメントの内容を更新するための小規模な修正を示しています。計4行の追加と4行の削除があり、全体で8行の変更が行われました。

主な修正点は以下の通りです：

1. 文書の説明文の中で「pre-populated」が「prepopulated」に変更され、用語が一貫した形で統一されています。この修正により、文書全体の明瞭さが増します。
2. ドキュメントの日付が「2024年11月21日」から「2025年6月30日」に最新化され、情報の鮮度が維持されています。
3. 説明文内の同様のフレーズに関しても、同じように「pre-populated」から「prepopulated」に修正され、表現の整合性が強化されています。

これらの修正により、文書の可読性と信頼性が向上し、ユーザーがチットチャット機能を理解しやすくなります。全体として、この変更はチットチャット機能に関する情報提供の質を高め、利用者にとっての価値を向上させることを目的としています。

## articles/ai-services/language-service/question-answering/how-to/configure-azure-resources.md{#item-a2ea5c}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,125 @@
+---
+title: Configure the custom question answering service for fine-tune models
+description: This article details Azure AI resource configurations for custom question answering fine-tune models.
+ms.service: azure-ai-language
+ms.topic: how-to
+author: laujan
+ms.author: lajanuar
+ms.date: 06/24/2025
+ms.custom: language-service-question-answering
+---
+
+# Configure your environment for Azure AI resources
+
+In this guide, we walk you through configuring your Azure AI resources and permissions for custom question and answering projects, enabling you to fine-tune models with Azure AI Search and Custom Question Answering (CQA). Completing this setup is essential for fully integrating your environment with Azure AI Services. You only need to perform this setup once—afterward, you have seamless access to advanced, AI-powered question answering capabilities.
+
+In addition, we show you how to assign the correct roles and permissions within the Azure portal. These steps help you get started quickly and effectively with Azure AI Language.
+
+## Prerequisites
+
+Before you can set up your resources, you need:
+
+* **An active Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/free/cognitive-services).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+*   An [Azure AI Foundry multi-service resource](../../../multi-service-resource.md) or an [Azure AI Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
+*   An [Azure AI Search resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.Search) (required for accessing CQA)
+
+
+> [!NOTE]
+>
+> We highly recommend that you use an Azure AI Foundry resource in the AI Foundry; however,  you can also follow these instructions using a Language resource.
+
+## Step 1: Assign the correct role to your Search resource
+
+Azure RBAC is an authorization system built on Azure Resource Manager. It provides fine-grained access management to Azure resources.
+
+1. Navigate to the [Azure portal](https://azure.microsoft.com/#home).
+
+1. Go to your Azure Search resource. (See **All resources** to find your Search resource.)
+
+1. In the Settings section on the left panel, select **Keys**.
+
+1. Make sure the **API Access control** button is set to **API keys**.
+
+   :::image type="content" source="../media/configure-resources/api-access-control.png" alt-text="Screenshot of API access control selector in the Azure portal."::: 
+
+1. Next, select **Access Control (IAM)** on the left panel, then select **Add role assignment**.
+
+   :::image type="content" source="../media/configure-resources/add-role-assignment.png" alt-text="Screenshot of add role assignment selector in the Azure portal.":::
+
+1. Search and select the **Azure AI Administrator** role. Select **Next**.
+
+   :::image type="content" source="../media/configure-resources/azure-ai-administrator.png" alt-text="Screenshot of Azure AI Administrator from the job function roles list in the Azure portal." lightbox="../media/configure-resources/azure-ai-administrator.png":::
+
+1. Navigate to the **Members** tab and then select **Assign access to User, group, or service principal**.
+
+   :::image type="content" source="../media/configure-resources/user-group-service-principal.png" alt-text="Screenshot of assign member access selector in the Azure portal.":::
+
+1. Select **Select members**, then add your account name, and choose **Select**.
+
+1. Finally, select **Review + assign** to confirm your selection.
+
+## Step 2: Configure connections in AI Foundry
+
+Azure AI Foundry offers a unified platform where you can easily build, manage, and deploy AI solutions using a wide range of models and tools. Connections enable authentication and access to both Microsoft and external resources within your Azure AI Foundry projects.
+
+1. Sign **into** [Azure AI Foundry](https://ai.azure.com/) using your account and required subscription. Then, select the project containing your Azure AI Foundry resource.
+
+1. Next, navigate to the **Management Center** in the bottom left corner of the page.
+
+1. Scroll to the **Connected resources** section of the Management center.
+
+   :::image type="content" source="../media/configure-resources/ai-foundry-management-center.png" alt-text="Screenshot of the management center selector in the Azure AI Foundry.":::
+
+1. Select the  **+ New connection** button.
+
+   :::image type="content" source="../media/configure-resources/new-connection.png" alt-text="Screenshot of the new connection button in the Azure AI Foundry.":::
+
+1. In the new window, select **Azure AI Search** as the resource type.
+
+1. Search for and display the Azure AI Search resource you connected in [Step 1](#step-1-assign-the-correct-role-to-your-search-resource).
+
+1. Ensure the Authentication is set to **API key**.
+
+1. Select **Add connection** then select **Close**.
+
+   :::image type="content" source="../media/configure-resources/connect-azure-search.png" alt-text="Screenshot of connect search resource selector in the Azure AI Foundry.":::
+
+## Step 3: Create a fine-tuning task with connected resources
+
+1. Navigate to **Go to project** at the end of the left navigation panel.
+
+   :::image type="content" source="../media/configure-resources/go-to-project.png" alt-text="Screenshot the go-to-project button in the Azure AI Foundry.":::
+
+1. Select **Fine-tuning** from the left navigation panel, choose the **AI Service fine-tuning** tab, and then select the **+ Fine-tune** button.
+
+   :::image type="content" source="../media/configure-resources/fine-tuning.png" alt-text="Screenshot of the fine tuning selector in the Azure AI Foundry.":::
+
+1. Choose **Custom question answering** as the task type from the new window, then select **Next**.
+
+1. Under **Connected service**, select your selected Azure AI Foundry resource. Then select your newly connected search resource.
+
+1. Your resources are now set up properly. Continue with setting up the fine-tuning task and customizing your CQA project.
+
+## Change Azure AI Search resource
+
+> [!WARNING]
+> If you change the Azure Search service associated with your language resource, you lose access to all the projects already present in it. Make sure you export the existing projects before you change the Azure Search service.
+
+If you create a language resource and its dependencies (such as Search) through the Azure portal, a Search service is created for you and linked to the language resource. After these resources are created, you can update the Search resource in the **Features** tab.
+
+1.  Go to your language resource in the Azure portal.
+
+1.  Select **Features** and select the Azure AI Search service you want to link with your language resource.
+
+    > [!NOTE]
+    > Your Language resource retains your Azure AI Search keys. If you update your search resource (for example, regenerating your keys), you need to select **Update Azure AI Search keys for the current search service**.
+
+    > [!div class="mx-imgBorder"]
+    > ![Add QnA to TA](../media/configure-resources/update-custom-feature.png)
+
+1.  Select **Save**.
+
+## Next Steps
+
+[Create, test, and deploy a custom question answering project](create-test-deploy.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azureリソースの設定に関する新しいガイド"
}
```

### Explanation
この変更は、「Azureリソースの設定」に関する新しいドキュメントを追加するもので、累計125行の内容が新たに含まれています。この新しいガイドは、カスタム質問応答サービスを構成し、モデルを微調整するためのAzure AIリソースの設定に関する詳細な情報を提供します。

主な内容は以下の通りです：

1. **新しいガイドの概要**: Azure AIリソースと権限の設定手順を説明し、ユーザーがカスタム質問応答プロジェクトを効率的に開始できるように支援します。
2. **前提条件**: Azureのアクティブなサブスクリプションや必要な権限についての情報を含め、どのようにAzure環境を準備するかが詳細に説明されています。
3. **役割の割り当て**: Azureポータル内での適切な役割と権限の割り当て手順を示しています。これにより、ユーザーはAzure AI Languageの機能をスムーズに利用できます。
4. **接続設定**: Azure AI Foundryの管理センターでのリソース接続の設定方法が含まれており、AIソリューションの構築を容易にします。
5. **微調整タスクの作成**: 接続されたリソースを使ってどのように微調整タスクを作成するかについても詳述されています。

このドキュメントの追加により、ユーザーはAzure AIサービスを効果的に利用できるようになり、特にカスタム質問応答機能が必要なプロジェクトに対しての理解が深まります。全体として、この新しいガイドは、Azure AIリソースを完全に統合するための重要な手順を提示し、ユーザーの作業を支援します。

## articles/ai-services/language-service/question-answering/how-to/configure-resources.md{#item-304b9b}

<details>
<summary>Diff</summary>
````diff
@@ -1,37 +0,0 @@
----
-title: Configure the custom question answering service
-description: This document outlines advanced configurations for custom question answering enabled resources.
-ms.service: azure-ai-language
-ms.topic: how-to
-author: laujan
-ms.author: lajanuar
-ms.date: 11/21/2024
-ms.custom: language-service-question-answering
----
-
-# Configure custom question answering enabled resources
-
-You can configure custom question answering to use a different Azure AI Search resource.
-
-## Change Azure AI Search resource
-
-> [!WARNING]
-> If you change the Azure Search service associated with your language resource, you will lose access to all the projects already present in it. Make sure you export the existing projects before you change the Azure Search service.
-
-If you create a language resource and its dependencies (such as Search) through the Azure portal, a Search service is created for you and linked to the language resource. After these resources are created, you can update the Search resource in the **Features** tab.
-
-1.  Go to your language resource in the Azure portal.
-
-2.  Select **Features** and select the Azure AI Search service you want to link with your language resource.
-    
-    > [!NOTE]
-    > Your Language resource will retain your Azure AI Search keys. If you update your search resource (for example, regenerating your keys), you will need to select **Update Azure AI Search keys for the current search service**.
-    
-    > [!div class="mx-imgBorder"]
-    > ![Add QnA to TA](../media/configure-resources/update-custom-feature.png)
-    
-3.  Select **Save**.
-
-## Next steps
-
-* [Encrypt data at rest](./encrypt-data-at-rest.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタム質問応答サービスの設定ガイドの削除"
}
```

### Explanation
この変更は、「カスタム質問応答サービスの設定」に関するドキュメントを削除するもので、累計37行の内容が削除されました。この削除は重要な変更であり、それにより関連する情報が利用できなくなります。

具体的な削除内容は以下の通りです：

1. **タイトルと説明**: 設定に関するタイトルと詳細説明が削除され、このガイドの存在そのものが消失しました。
2. **リソース設定の手順**: Azure AI Searchリソースを変更する手順が含まれていましたが、これもすべて削除されました。具体的には、リソースの変更に関する警告や手順が削除されており、ユーザーが誤ってリソースを変更してしまうリスクが増加します。
3. **次のステップへのリンク**: データを静止状態で暗号化するための次のステップに関するリンクも削除されています。

この変更により、ユーザーはカスタム質問応答サービスを構成するためのガイダンスを失い、これに関連するリソースへのアクセスが難しくなります。この変更は、特にAzureのリソース設定について学びたいと考えているユーザーにとって、情報の空白を生じさせる重大な影響があります。

## articles/ai-services/language-service/question-answering/language-support.md{#item-b1f267}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.author: lajanuar
 recommendations: false
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/21/2024
+ms.date: 06/30/2025
 ms.custom: language-service-question-answering
 ---
 
@@ -25,15 +25,15 @@ In custom question answering, you have the option to either select the language
 > ![Multi-lingual project selection](./media/language-support/choose-language.png)
 
 * When you are creating the first project in your service, you get a choice pick the language each time you create a new project. Select this option, to create projects belonging to different languages within one service.
-* Language setting option cannot be modified for the service, once the first project is created.
+* The language setting option cannot be modified for the service once the first project is created.
 * If you enable multiple languages for the project, then instead of having one test index for the service you will have one test index per project.
 
 ## Supporting multiple languages in one project
 
 If you need to support a project system, which includes several languages, you can:
 
 * Use the [Translator service](../../translator/translator-overview.md) to translate a question into a single language before sending the question to your project. This allows you to focus on the quality of a single language and the quality of the alternate questions and answers.
-* Create a custom question answering enabled language resource, and a project inside that resource, for every language. This allows you to manage separate alternate questions and answer text that is more nuanced for each language. This gives you much more flexibility but requires a much higher maintenance cost when the questions or answers change across all languages.
+* Create a custom question answering enabled language resource, and a project inside that resource, for every language. This allows you to manage separate alternate questions and answer text that is more nuanced for each language. This provides more flexibility but requires a much higher maintenance cost when the questions or answers change across all languages.
 
 ## Single language per resource
 
@@ -47,84 +47,82 @@ If you **select the option to set the language used by all projects associated w
 
 The following list contains the languages supported for a custom question answering resource.
 
-| Language |
-|--|
-| Arabic |
-| Armenian |
-| Bangla |
-| Basque |
-| Bulgarian |
-| Catalan |
-| Chinese_Simplified |
-| Chinese_Traditional |
-| Croatian |
-| Czech |
-| Danish |
-| Dutch |
-| English |
-| Estonian |
-| Finnish |
-| French |
-| Galician |
-| German |
-| Greek |
-| Gujarati |
-| Hebrew |
-| Hindi |
-| Hungarian |
-| Icelandic |
-| Indonesian |
-| Irish |
-| Italian |
-| Japanese |
-| Kannada |
-| Korean |
-| Latvian |
-| Lithuanian |
-| Malayalam |
-| Malay |
-| Norwegian |
-| Polish |
-| Portuguese |
-| Punjabi |
-| Romanian |
-| Russian |
-| Serbian_Cyrillic |
-| Serbian_Latin |
-| Slovak |
-| Slovenian |
-| Spanish |
-| Swedish |
-| Tamil |
-| Telugu |
-| Thai |
-| Turkish |
-| Ukrainian |
-| Urdu |
-| Vietnamese |
+- Arabic
+- Armenian
+- Bangla
+- Basque
+- Bulgarian
+- Catalan
+- Chinese_Simplified
+- Chinese_Traditional
+- Croatian
+- Czech
+- Danish
+- Dutch
+- English
+- Estonian
+- Finnish
+- French
+- Galician
+- German
+- Greek
+- Gujarati
+- Hebrew
+- Hindi
+- Hungarian
+- Icelandic
+- Indonesian
+- Irish
+- Italian
+- Japanese
+- Kannada
+- Korean
+- Latvian
+- Lithuanian
+- Malayalam
+- Malay
+- Norwegian
+- Polish
+- Portuguese
+- Punjabi
+- Romanian
+- Russian
+- Serbian_Cyrillic
+- Serbian_Latin
+- Slovak
+- Slovenian
+- Spanish
+- Swedish
+- Tamil
+- Telugu
+- Thai
+- Turkish
+- Ukrainian
+- Urdu
+- Vietnamese
 
 ## Query matching and relevance
 Custom question answering depends on [Azure AI Search language analyzers](/rest/api/searchservice/language-support) for providing results.
 
 While the Azure AI Search capabilities are on par for supported languages, custom question answering has an additional ranker that sits above the Azure search results. In this ranker model, we use some special semantic and word-based features in the following languages.
 
-|Languages with additional ranker|
-|--|
-|Chinese|
-|Czech|
-|Dutch|
-|English|
-|French|
-|German|
-|Hungarian|
-|Italian|
-|Japanese|
-|Korean|
-|Polish|
-|Portuguese|
-|Spanish|
-|Swedish|
-
-This additional ranking is an internal working of the custom question answering's ranker.
+- Chinese
+- Czech
+- Dutch
+- English
+- French
+- German
+- Hungarian
+- Italian
+- Japanese
+- Korean
+- Polish
+- Portuguese
+- Spanish
+- Swedish
+
+This ranking is an internal working of the custom question answering's ranker.
 
 ## Next steps
+
+* [Question answering quickstart](./quickstart/sdk.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サポートに関するドキュメントの更新"
}
```

### Explanation
この変更は、「言語サポート」に関するドキュメントの更新を表しており、合計で150行の内容が変更されています。具体的には、74行が追加され、76行が削除されています。この変更により、文書内容が明確になり、表現も改善されています。

主な更新内容は以下の通りです：

1. **日付の更新**: ドキュメントの日付が2024年11月21日から2025年6月30日に変更されました。これにより、最新版であることを示します。
2. **文の明確化**: 一部の文に対して言い回しの修正が行われ、より自然な表現が使用されています（例： "This gives you much more flexibility"から"This provides more flexibility"への変更）。
3. **サポートされる言語リストの形式**: 言語リストのフォーマットが変更され、テーブル形式から箇条書きの形式に改善されました。これにより、見やすさが向上しています。
4. **クエリマッチングと関連性の詳細**: カスタム質問応答機能に関連する言語のランキングに関する説明が修正され、重要な情報が強調されました。

全体として、この更新は文書の可読性と正確性を向上させ、利用者がカスタム質問応答サービスに関する情報をより良く理解できるようにしています。また、次のステップへのリンクが追加されており、ユーザーがさらに進んで学習できるポイントが提供されています。

## articles/ai-services/language-service/question-answering/media/configure-resources/add-role-assignment.png{#item-37c411}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "役割割り当ての画像の追加"
}
```

### Explanation
この変更は、「役割割り当て」を示す画像が新たに追加されたことを意味しています。この画像は、Azureのカスタム質問応答サービスにおいて役割を適切に割り当てる手順を視覚的にサポートするために使用されます。

具体的には、以下のポイントが挙げられます：

- **画像のファイル名**: `add-role-assignment.png`というファイル名から、役割割り当ての操作にフォーカスした内容であることが示唆されています。
- **フォルダ構成**: 画像は`media/configure-resources`フォルダ内に追加されており、関連するリソースの設定と整合性を保つ形で配置されています。
- **視覚的サポート**: 文章に新たに追加された画像は、ユーザーが役割を割り当てる際の理解を助けるために利用されることが期待されます。

この画像の追加により、ドキュメント全体の情報提供が向上し、ユーザーが役割割り当てを行う際のプロセスがより明確になるでしょう。対応するビジュアルがあることで、手順が視覚的に補完され、読者にとっての利便性が高まります。

## articles/ai-services/language-service/question-answering/media/configure-resources/ai-foundry-management-center.png{#item-8cf696}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "AIファウンドリ管理センターの画像の追加"
}
```

### Explanation
この変更は、「AIファウンドリ管理センター」を示す画像が新たに追加されたことを意味しています。この画像は、Azureのカスタム質問応答サービスに関連するリソースの設定や管理を視覚的にサポートすることを目的としています。

具体的なポイントは以下のとおりです：

- **画像のファイル名**: `ai-foundry-management-center.png`というファイル名から、AIファウンドリの管理センターに関する内容であることが示されています。
- **配置場所**: 画像は`media/configure-resources`フォルダ内に追加されており、リソースの設定手順に関連付けられた形で整理されています。
- **視覚的サポートの強化**: 新たに追加されたこの画像は、ユーザーがAIファウンドリの管理センターを利用する際の理解を深めるために役立ちます。視覚的な要素があることで、文章だけでは伝わりにくい操作手順や配置を明確に理解しやすくすることが期待されます。

このように、画像の追加により、ユーザーに対する情報提供が強化され、カスタム質問応答サービスの利用がさらにスムーズになるでしょう。

## articles/ai-services/language-service/question-answering/media/configure-resources/api-access-control.png{#item-677baf}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "APIアクセス制御の画像の追加"
}
```

### Explanation
この変更は、「APIアクセス制御」を示す画像が新たに追加されたことを意味しています。この画像は、Azureのカスタム質問応答サービスにおいてAPIのアクセス管理や制御を視覚的に補完するために使用されます。

具体的なポイントは以下のとおりです：

- **画像のファイル名**: `api-access-control.png`というファイル名から、APIのアクセス制御に特化した内容であることが示されています。
- **フォルダ位置**: 画像は`media/configure-resources`フォルダに追加されており、関連するリソース設定の文脈で位置付けられています。
- **視覚的支援**: 新たに追加された画像は、ユーザーがAPIアクセス制御の設定や管理方法を理解する際の助けになることを目指しています。視覚的要素は、手順や設定方法をより直感的に理解できるようにサポートします。

この改訂により、ドキュメントの情報提供がさらに充実し、ユーザーがAPIアクセス制御を効果的に扱うことができるようになるでしょう。

## articles/ai-services/language-service/question-answering/media/configure-resources/azure-ai-administrator.png{#item-919814}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI管理者の画像の追加"
}
```

### Explanation
この変更は、「Azure AI管理者」を示す画像が新たに追加されたことを意味しています。この画像は、Azureのカスタム質問応答サービスに関連する管理者の役割や機能を視覚的に提示することを目的としています。

具体的なポイントは以下のとおりです：

- **画像のファイル名**: `azure-ai-administrator.png`というファイル名から、Azure AIの管理者に特化した内容であることが明らかです。
- **フォルダの位置**: 画像は`media/configure-resources`フォルダに追加されており、リソースの設定に関連する情報を整理されています。
- **視覚的な向上**: 新規追加されたこの画像は、ユーザーがAzure AI管理者の役割や操作を理解する際に役立つことを目指しています。視覚的要素があることで、管理者に必要な情報を効果的に伝えることができるようになります。

この改訂により、関連情報が充実し、ユーザーがAzure AI管理者の機能やその利用方法をよりスムーズに理解できるようになることが期待されます。

## articles/ai-services/language-service/question-answering/media/configure-resources/azure-ai-search-resource.png{#item-28942c}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI検索リソースの画像の追加"
}
```

### Explanation
この変更は、「Azure AI検索リソース」を示す画像が新たに追加されたことを意味しています。この画像は、Azureのカスタム質問応答サービスにおけるAI検索機能とそのリソースの設定を視覚的に補完するために使用されます。

具体的なポイントは以下のとおりです：

- **画像のファイル名**: `azure-ai-search-resource.png`というファイル名は、Azure AIの検索リソースに特化した内容であることを表しています。
- **フォルダ位置**: 画像は`media/configure-resources`フォルダに追加されており、リソース設定に関連するコンテキストで整理されています。
- **視覚的支援**: 新たに追加されたこの画像は、ユーザーがAzure AIの検索リソースを理解し、適切に設定する手助けになることを目指しています。視覚的情報は、手順や設定方法の理解をより直感的にする役割を果たします。

この改訂によって、ドキュメントの情報がさらに豊かになり、ユーザーがAzure AI検索リソースの機能と利用方法を効果的に理解できるようになることが期待されます。

## articles/ai-services/language-service/question-answering/media/configure-resources/connect-azure-search.png{#item-f291f5}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure検索への接続方法を示す画像の追加"
}
```

### Explanation
この変更は、「Azure検索への接続方法」を示す画像が新たに追加されたことを意味しています。この画像は、Azure AIのカスタム質問応答サービスにおけるAzure検索との接続手順を視覚的に説明するために役立つものです。

具体的なポイントは以下のとおりです：

- **画像のファイル名**: `connect-azure-search.png`というファイル名は、Azure検索機能への接続方法を直感的に理解できるように設計されていることを示しています。
- **フォルダ位置**: 受け取った画像は`media/configure-resources`ディレクトリに追加されており、リソースの設定に関する情報と一緒に配置されています。
- **視覚的サポート**: 新たに追加されたこの画像は、ユーザーがAzure検索と接続し、その機能を効果的に活用するための手助けを行います。視覚的要素によって、手順がよりわかりやすくなり、ユーザーの理解を促進します。

この改訂により、関連情報がさらに強化され、ユーザーがAzure検索を利用する際のプロセスを効率的に理解できることが期待されます。

## articles/ai-services/language-service/question-answering/media/configure-resources/fine-tuning.png{#item-e6295d}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニング手法を示す画像の追加"
}
```

### Explanation
この変更は、「ファインチューニング手法」を示す画像が新たに追加されたことを意味しています。この画像は、Azure AIのカスタム質問応答サービスにおけるファインチューニングのプロセスを視覚的に表現し、ユーザーがその手法を理解するのに役立ちます。

具体的なポイントは以下のとおりです：

- **画像のファイル名**: `fine-tuning.png`というファイル名は、モデルのファインチューニングに関する情報を強調しています。
- **フォルダ位置**: 画像は`media/configure-resources`フォルダに追加されており、リソース設定に関連する情報と一緒に整理されています。
- **視覚的サポートの重要性**: 新たに追加されたこの画像は、ユーザーがAIモデルのファインチューニングに関する手順やベストプラクティスをより明確に理解できるようにし、実装を容易にします。視覚情報は、情報の消化を助け、学習曲線を緩和する効果があります。

この改訂によって、ユーザーはファインチューニングの手法をより効果的に学び、実用的なスキルを身につけることが期待されます。

## articles/ai-services/language-service/question-answering/media/configure-resources/go-to-project.png{#item-cda578}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "プロジェクトへの移動を示す画像の追加"
}
```

### Explanation
この変更は、「プロジェクトへの移動」を示す画像が新たに追加されたことを示しています。この画像は、Azure AIのカスタム質問応答サービスにおいて、プロジェクトにアクセスする手順を視覚的に説明するために使用されます。

具体的なポイントは以下のとおりです：

- **画像のファイル名**: `go-to-project.png`というファイル名は、ユーザーがプロジェクトに移動するための簡潔なガイドとして設計されています。
- **フォルダ位置**: 画像は`media/configure-resources`フォルダに追加されており、リソース設定に関連する内容と一緒に整理されています。
- **視覚的サポートの役割**: 新たに追加されたこの画像は、ユーザーがプロジェクトを効率的にナビゲートする手助けをし、全体的な体験を向上させることを目的としています。視覚化された情報により、手順の理解が促進され、ユーザーの操作が容易になります。

この改訂により、ユーザーはプロジェクトセクションへのナビゲーションをより迅速かつ正確に行えるようになることが期待されます。

## articles/ai-services/language-service/question-answering/media/configure-resources/new-connection.png{#item-931bb0}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい接続を示す画像の追加"
}
```

### Explanation
この変更は、「新しい接続」を示す画像が新たに追加されたことを示しています。この画像は、Azure AIのカスタム質問応答サービスにおける接続設定に関連しており、ユーザーが新しい接続を確立する手順を視覚的に支援することを目的としています。

具体的なポイントは以下のとおりです：

- **画像のファイル名**: `new-connection.png`というファイル名は、新しい接続を作成するための具体的なプロセスに重点を置いています。
- **フォルダ位置**: 画像は`media/configure-resources`フォルダに追加されており、リソース設定に関連する内容の一部として整理されています。
- **視覚的情報の提供**: 新たに追加されたこの画像は、接続を設定する手順を視覚的に示すことで、ユーザーがこのプロセスを直感的に理解できるようにします。視覚的な指導は、複雑な手順を簡略化し、学習を助ける効果があります。

この改訂により、ユーザーは新しい接続の設定をより迅速かつ効果的に行えるようになることが期待されます。

## articles/ai-services/language-service/question-answering/media/configure-resources/user-group-service-principal.png{#item-394a5f}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ユーザーグループとサービス プリンシパルを示す画像の追加"
}
```

### Explanation
この変更は、「ユーザーグループとサービスプリンシパル」を示す画像が新たに追加されたことを示しています。この画像は、Azure AIのカスタム質問応答サービスにおけるユーザーとサービスの設定に関連しており、ユーザーが適切にサービスプリンシパルを構成する手順を視覚的に認識できるよう支援することを目的としています。

具体的なポイントは以下のとおりです：

- **画像のファイル名**: `user-group-service-principal.png`というファイル名は、ユーザーグループとサービスプリンシパルの関係を示す内容であることを示しています。
- **フォルダ位置**: 画像は`media/configure-resources`フォルダに追加されており、リソース設定に関連する情報の一部として整理されています。
- **視覚的なサポート**: この新しい画像は、ユーザーがサービスプリンシパルを正しく設定する手順を理解しやすくするために役立ちます。視覚情報は、複雑なプロセスをシンプルにし、ユーザーのナビゲーションを容易にします。

この改訂によって、ユーザーはユーザーグループとサービスプリンシパルの設定をよりスムーズに行えるようになり、全体的な体験が向上することが期待されます。

## articles/ai-services/language-service/question-answering/tutorials/adding-synonyms.md{#item-ccf9ee}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-language
 ms.topic: tutorial
 author: laujan
 ms.author: lajanuar
-ms.date: 11/21/2024
+ms.date: 06/30/2025
 ms.custom: language-service-question-answering
 ---
 
@@ -17,11 +17,11 @@ In this tutorial, you learn how to:
 > * Add synonyms to improve the quality of your responses
 > * Evaluate the response quality via the inspect option of the Test pane
 
-This tutorial will show you how you can improve the quality of your responses by using synonyms. Let's assume that users are not getting an accurate response to their queries, when they use alternate forms, synonyms or acronyms of a word. So, they decide to improve the quality of the response by using [Authoring API](../how-to/authoring.md) to add synonyms for keywords.
+This tutorial shows you how you can improve the quality of your responses by using synonyms. Let's assume that users aren't getting an accurate response to their queries, when they use alternate forms, synonyms or acronyms of a word. So, they decide to improve the quality of the response by using [Authoring API](../how-to/authoring.md) to add synonyms for keywords.
 
 ## Add synonyms using Authoring API
 
-Let’s us add the following words and their alterations to improve the results:
+Let improve the results by adding the following words and their alterations:
 
 |Word | Alterations|
 |--------------|--------------------------------|
@@ -58,7 +58,7 @@ Let’s us add the following words and their alterations to improve the results:
 
 ```
 
-For the question and answer pair “Fix problems with Surface Pen”, we compare the response for a query made using its synonym “troubleshoot”.
+For the question and answer pair “Fix problems with Surface Pen,” we compare the response for a query made using its synonym “troubleshoot.”
 
 ## Response before addition of synonym
 
@@ -70,7 +70,7 @@ For the question and answer pair “Fix problems with Surface Pen”, we compare
 > [!div class="mx-imgBorder"]
 > [ ![Screenshot with a confidence score of .97 highlighted in red]( ../media/adding-synonyms/score-improvement.png) ]( ../media/adding-synonyms/score-improvement.png#lightbox)
 
-As you can see, when `troubleshoot` was not added as a synonym, we got a low confidence response to the query “How to troubleshoot your surface pen”. However, after we add `troubleshoot` as a synonym to “fix problems”, we received the correct response to the query with a higher confidence score. Once, these synonyms were added, the relevance of results improved thereby improving user experience.
+As you can see, when `troubleshoot` was not added as a synonym, we got a low confidence response to the query “How to troubleshoot your surface pen.” However, after we add `troubleshoot` as a synonym to “fix problems”, we received the correct response to the query with a higher confidence score. Once these synonyms were added, the relevance of results is improved.
 
 > [!IMPORTANT]
 > Synonyms are case insensitive. Synonyms also might not work as expected if you add stop words as synonyms. The list of stop words can be found here: [List of stop words](https://github.com/Azure-Samples/azure-search-sample-data/blob/master/STOPWORDS.md).
@@ -80,8 +80,8 @@ As you can see, when `troubleshoot` was not added as a synonym, we got a low con
 * Synonyms can be added in any order. The ordering is not considered in any computational logic.
 * Synonyms can only be added to a project that has at least one question and answer pair.
 * Synonyms can be added only when there is at least one question and answer pair present in a project.
-* In case of overlapping synonym words between 2 sets of alterations, it may have unexpected results and it is not recommended to use overlapping sets.
-* Special characters are not allowed for synonyms. For hyphenated words like "COVID-19", they are treated the same as "COVID 19", and "space" can be used as a term separator. Following is the list of special characters **not allowed**:
+* In case of overlapping synonym words between two sets of alterations, it can have unexpected results and it isn't recommended to use overlapping sets.
+* Special characters are not allowed for synonyms. For hyphenated words like "COVID-19," they are treated the same as "COVID 19," and "space" can be used as a term separator. Following is the list of special characters **not allowed**:
 
 |Special character | Symbol|
 |--------------|--------------------------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "同義語追加チュートリアルの更新"
}
```

### Explanation
この変更は、同義語を追加するチュートリアルに関する文書が更新されたことを示しています。主にいくつかの文言が修正され、説明が明確化されています。

具体的なポイントは以下のとおりです：

- **日付の更新**: ドキュメントの最終更新日が「2024年11月21日」から「2025年6月30日」に変更されました。
- **表現の明確化**: 一部の文がより流暢かつ明確に修正されており、ユーザーが同義語を使用して応答の質を向上させる方法をより理解しやすくなっています。例えば、「Let’s us add」から「Let improve」に文言が変更されました。
- **文法の修正**: 不定冠詞と名詞の一致、コンマの位置に関する文法的な修正が行われました。例えば、「troubleshoot」の前後の文のコンマ位置が修正され、整った文法にされました。
- **内容の強化**: 同義語の特性や制限に関する説明が改善され、リスト内の表現がより一貫性を持ったものになっています。

この改訂により、ユーザーは同義語を追加するプロセスに関する理解を深め、効果的に支援が得られることが期待されます。全体として、説明が具体的になり、実際の使用シナリオにおける助けとなる内容になっています。

## articles/ai-services/language-service/sentiment-opinion-mining/how-to/use-containers.md{#item-887deb}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/21/2024
+ms.date: 06/30/2025
 ms.author: lajanuar
 ms.custom: language-service-sentiment-opinion-mining
 keywords: on-premises, Docker, container, sentiment analysis, natural language processing
@@ -130,7 +130,7 @@ In this article, you learned concepts and workflow for downloading, installing,
 * You must specify billing information when instantiating a container.
 
 > [!IMPORTANT]
-> Azure AI containers are not licensed to run without being connected to Azure for metering. Customers need to enable the containers to communicate billing information with the metering service at all times. Azure AI containers do not send customer data (e.g. text that is being analyzed) to Microsoft.
+> Azure AI containers are not licensed to run without being connected to Azure for metering. Customers need to enable the containers to communicate billing information with the metering service at all times. Azure AI containers do not send customer data (for example, text that is being analyzed) to Microsoft.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテナ使用に関するドキュメントの更新"
}
```

### Explanation
この変更は、感情分析や意見マイニングのためのコンテナの使用方法に関する文書が修正されたことを示しています。文書内の一部の表現が更新され、明確性が向上しています。

具体的なポイントは以下のとおりです：

- **日付の更新**: 最終更新日が「2024年11月21日」から「2025年6月30日」へと変更され、最新の情報を反映しています。
- **文言の修正**: コンテナに関する重要な注意事項の表現が若干修正されており、特に「customer data (e.g. text that is being analyzed)」から「customer data (for example, text that is being analyzed)」への変更が行われ、より流れるような自然な文になっています。
- **内容の整合性向上**: 注意喚起のセクションで明確さを増すために、用語の整合性が高められ、情報が一貫して伝わるように配慮されています。

この改訂により、ユーザーはAzure AIコンテナの使用に関する要件や注意点をより理解しやすくなり、実際の利用において重要な情報が強調された結果、全体的な体験が向上することが期待されます。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -6,28 +6,37 @@ items:
   items:
   - name: What is Azure AI Language?
     href: overview.md
+    displayName: overview, introduction
   - name: Pricing
     href: https://aka.ms/unifiedLanguagePricing
   - name: Language support
     href: concepts/language-support.md
+    displayName: multilingual
   - name: Region support
     href: ./concepts/regional-support.md
+    displayName: availability, azure regions, geographic availability
   - name: Quotas and limits
     href: concepts/data-limits.md
+    displayName: service limits, rate, usage
   - name: What's new
     href: whats-new.md
+    displayName: release notes, updates, new features, changelog
 - name: Azure AI Language capabilities
   items:
   - name: Custom text classification
     items:
     - name: Custom text classification overview
       href: custom-text-classification/overview.md
+      displayName: ctc
     - name: Custom text classification quickstart
       href: custom-text-classification/quickstart.md
+      displayName: ctc setup
     - name: Custom text classification language support
       href: custom-text-classification/language-support.md
+      displayName: ctc languages, multilingual
     - name: Custom text classification FAQ
       href: custom-text-classification/faq.md
+      displayName: ctc faq, troubleshooting
     - name: Responsible use of AI
       items:
       - name: Transparency note for custom text classification
@@ -46,95 +55,140 @@ items:
       items:
       - name: Create projects
         href: custom-text-classification/how-to/create-project.md
+        displayName: project creation, setup project
       - name: Data selection and schema design
         href: custom-text-classification/how-to/design-schema.md
-        displayName: Best practices
+        displayName: best practices
       - name: Label data
         href: custom-text-classification/how-to/tag-data.md
+        displayName: tag data, annotate text, training data
       - name: Auto label your data (preview)
         href: custom-text-classification/how-to/use-autolabeling.md
+        displayName: automatic annotation, smart labeling, ai assisted labeling
       - name: Label data with Azure Machine Learning
         href: custom/azure-machine-learning-labeling.md
+        displayName: azure ml labeling, aml annotation
       - name: Train a model
         href: custom-text-classification/how-to/train-model.md
+        displayName: training, classifier, build model
       - name: Model performance (preview)
         href: custom-text-classification/how-to/view-model-evaluation.md
+        displayName: evaluation, performance metrics, accuracy, precision, recall
       - name: Deploy a model
         href: custom-text-classification/how-to/deploy-model.md
+        displayName: deployment, classifier, production deployment
       - name: Classify text
         href: custom-text-classification/how-to/call-api.md
+        displayName: classification, prediction
       - name: Back up and recover your models
         href: custom-text-classification/fail-over.md
+        displayName: backup, disaster recovery, failover
       - name: Deploy to multiple regions
         href: concepts/custom-features/multi-region-deployment.md
+        displayName: multi-region, global deployment, regional distribution
     - name: Concepts
       items:
       - name: Evaluation metrics
         href: custom-text-classification/concepts/evaluation-metrics.md
+        displayName: performance evaluation, accuracy, f1 score, confusion matrix
       - name: Accepted data formats
         href: custom-text-classification/concepts/data-formats.md
-        displayName: Data representation
+        displayName: data representation
       - name: Project versioning
         href: concepts/custom-features/project-versioning.md
+        displayName: version control, model versions
     - name: Tutorials
       items:
-      - name: Triage incoming emails with power automate
+      - name: Triage incoming emails with Power Automate
         href: custom-text-classification/tutorials/triage-email.md
+        displayName: power automate, email classification, automation
     - name: Reference
       items:
       - name: Glossary
         href: custom-text-classification/glossary.md
-        displayName: Model, Project, Class
+        displayName: model, project, class
       - name: Service limits
         href: custom-text-classification/service-limits.md
+        displayName: quotas, restrictions, service boundaries
   - name: Conversational language understanding
     items:
     - name: Conversational language understanding overview
       href: conversational-language-understanding/overview.md
+      displayName: clu, conversational ai, intent recognition, entity extraction
     - name: Conversational language understanding quickstart
       href: conversational-language-understanding/quickstart.md
+      displayName: getting started, tutorial, conversational ai setup
     - name: Conversational language understanding language support
       href: conversational-language-understanding/language-support.md
+      displayName: clu languages, supported languages, multilingual, international support
     - name: Conversational language understanding FAQ
       href: conversational-language-understanding/faq.md
+      displayName: frequently asked questions, troubleshooting, common issues
+    - name: Responsible use of AI
+      items:
+      - name: Transparency note for conversational language understanding
+        href: /legal/cognitive-services/language-service/clu-transparency-note?context=/azure/ai-services/language-service/context/context
+      - name: Integration and responsible use
+        href: /legal/cognitive-services/language-service/guidance-integration-responsible-use?context=/azure/ai-services/language-service/context/context
+      - name: Characteristics and limitations
+        href: /legal/cognitive-services/language-service/clu-characteristics-and-limitations?context=/azure/ai-services/language-service/context/context
+      - name: Data, privacy, and security
+        href: /legal/cognitive-services/language-service/data-privacy?context=/azure/ai-services/language-service/context/context
     - name: How-to guides
       items:
         - name: Use containers
           items:
           - name: Use Docker Containers
             href: conversational-language-understanding/how-to/use-containers.md
+            displayName: containerization, container deployment, clu containers
           - name: Configure containers
             href: concepts/configure-containers.md
+            displayName: container setup
           - name: Use container instances
             href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
           - name: Azure AI containers overview
             href: ../cognitive-services-container-support.md
         - name: Create projects
           href: conversational-language-understanding/how-to/create-project.md
+          displayName: creation, clu project, setup
         - name: Build a schema
           href: conversational-language-understanding/how-to/build-schema.md
+          displayName: design, intents, entities, conversational model
         - name: Label utterances
           href: conversational-language-understanding/how-to/tag-utterances.md
+          displayName: labeling, tag utterances, training data, annotation
         - name: Train a model
           href: conversational-language-understanding/how-to/train-model.md
+          displayName: training, clu training, conversational model training
+        - name: Configure Azure resources
+          href: conversational-language-understanding/how-to/configure-azure-resources.md
+          displayName: configuration, fine-tuning, azure ai foundry, azure portal 
         - name: View your model's performance
           href: conversational-language-understanding/how-to/view-model-evaluation.md
+          displayName: evaluation, performance metrics, clu accuracy, testing
         - name: Deploy a model
           href: conversational-language-understanding/how-to/deploy-model.md
-        - name: Call the API to make predictions
+          displayName: deployment, clu, production
+        - name: Call the API and make predictions
           href: conversational-language-understanding/how-to/call-api.md
+          displayName: predictions, clu api, intent recognition, entity extraction
         - name: Back up and recover your models
           href: conversational-language-understanding/how-to/fail-over.md
+          displayName: disaster recovery, failover, clu
         - name: Migrate from LUIS
           href: conversational-language-understanding/how-to/migrate-from-luis.md
+          displayName: language understanding, luis to clu
     - name: Concepts
       items:
         - name: Best practices
           href: conversational-language-understanding/concepts/best-practices.md
+          displayName: recommendations, guidelines, optimization
         - name: Multilingual projects
           href: conversational-language-understanding/concepts/multiple-languages.md
+          displayName: multiple languages, international, localization
         - name: Entity components
           href: conversational-language-understanding/concepts/entity-components.md
+          displayName: entities, extraction, ner components
         - name: Evaluation metrics
           href: conversational-language-understanding/concepts/evaluation-metrics.md
         - name: Data formats
@@ -145,22 +199,26 @@ items:
           href: concepts/custom-features/multi-region-deployment.md
         - name: Choosing between conversational apps
           href: conversational-language-understanding/concepts/app-architecture.md
+          displayName: architecture, clu, qna, comparison
     - name: Tutorials
       items:
         - name: Use Bot Framework
           href: conversational-language-understanding/tutorials/bot-framework.md
+          displayName: integration, chatbot, conversational, bot, clu
     - name: Reference
       items:
       - name: Prebuilt component reference
         href: conversational-language-understanding/prebuilt-component-reference.md
       - name: Service limits
         href: conversational-language-understanding/service-limits.md
+        displayName: limits, quotas, restrictions, boundaries, clu
       - name: Glossary
         href: conversational-language-understanding/glossary.md
   - name: Entity linking
     items:
     - name: Entity linking overview
       href: entity-linking/overview.md
+      displayName: knowledge base linking, disambiguation
     - name: Entity linking quickstart
       href: entity-linking/quickstart.md
     - name: Entity linking language support
@@ -177,10 +235,12 @@ items:
       items:
         - name: How to call the API
           href: entity-linking/how-to/call-api.md
+          displayName: entity linking, entity recognition
   - name: Language detection
     items:
     - name: Language detection overview
       href: language-detection/overview.md
+      displayName: language identification, automatic detection
     - name: Language detection quickstart
       href: language-detection/quickstart.md
     - name: Language detection language support
@@ -216,6 +276,7 @@ items:
     items:
     - name: Key phrase extraction overview
       href: key-phrase-extraction/overview.md
+      displayName: keyword extraction, key terms
     - name: Key phrase extraction quickstart
       href: key-phrase-extraction/quickstart.md
     - name: Key phrase extraction language support
@@ -251,10 +312,12 @@ items:
       items:
       - name: Integrate Power BI
         href: key-phrase-extraction/tutorials/integrate-power-bi.md
+        displayName: business intelligence, data visualization
   - name: Named Entity Recognition (NER)
     items:
     - name: NER overview
       href: named-entity-recognition/overview.md
+      displayName: ner introduction, entity extraction
     - name: NER quickstart
       href: named-entity-recognition/quickstart.md
     - name: NER language support
@@ -302,6 +365,7 @@ items:
         items:
         - name: Extract information in Excel using Power Automate
           href: named-entity-recognition/tutorials/extract-excel-information.md
+          displayName: excel integration, power automate, ner automation, extract entities
     - name: Custom
       items:
       - name: Custom NER overview
@@ -402,6 +466,7 @@ items:
       items:
         - name: Connect conversational language understanding and custom question answering
           href: orchestration-workflow/tutorials/connect-services.md
+          displayName: clu integration, qna integration, orchestration workflow, connect services
     - name: Reference
       items:
       - name: Service limits
@@ -412,7 +477,7 @@ items:
     items:
     - name: PII overview
       href: personally-identifiable-information/overview.md
-      displayName: native, native document
+      displayName: native document
     - name: PII quickstart
       href: personally-identifiable-information/quickstart.md
     - name: PII language support
@@ -460,6 +525,7 @@ items:
     items:
     - name: Custom question answering overview
       href: question-answering/overview.md
+      displayName: qna, faq, knowledge base
     - name: Custom question answering quickstart
       href: question-answering/quickstart/sdk.md
     - name: Custom question answering language support
@@ -479,13 +545,16 @@ items:
       items:
       - name: Migrate from QnA Maker to custom question Answering
         href: question-answering/how-to/migrate-qnamaker-to-question-answering.md
+        displayName: migration, custom question answering
       - name: Migrate projects from QnA Maker
         href: question-answering/how-to/migrate-qnamaker.md
+        displayName: migration, transfer
       - name: Getting started with custom question answering
         href: question-answering/how-to/create-test-deploy.md
+        displayName: knowledge base, test deploy
       - name: Export/import/refresh
         href: question-answering/how-to/export-import-refresh.md
-      - name: Smart URL refresh
+      - name: Use smart URL refresh
         href: question-answering/how-to/smart-url-refresh.md
       - name: Encrypt data at rest
         href: question-answering/how-to/encrypt-data-at-rest.md
@@ -495,8 +564,9 @@ items:
         href: question-answering/how-to/chit-chat.md
       - name: Change default answer
         href: question-answering/how-to/change-default-answer.md
-      - name: Configure resources
-        href: question-answering/how-to/configure-resources.md
+      - name: Configure Azure resources
+        href: question-answering/how-to/configure-azure-resources.md
+        displayName: configuration, fine-tuning, azure ai foundry, azure portal 
       - name: Analytics
         href: question-answering/how-to/analytics.md
       - name: Manage projects
@@ -533,8 +603,9 @@ items:
         href: conversational-language-understanding/concepts/app-architecture.md
     - name: Tutorials
       items:
-      - name: Create a FAQ Bot
+      - name: Create an FAQ Bot
         href: question-answering/tutorials/bot-service.md
+        displayName: bot framework, chatbot
       - name: Guided conversations
         href: question-answering/tutorials/guided-conversations.md
       - name: Active learning
@@ -545,8 +616,9 @@ items:
         href: question-answering/tutorials/multiple-languages.md
       - name: Multiple domains
         href: question-answering/tutorials/multiple-domains.md
-      - name: Add your custom question answering project to Power Virtual Agents
+      - name: Add your custom question answering project to Microsoft Copilot Studios
         href: question-answering/tutorials/power-virtual-agents.md
+        displayName: power virtual agents, pva integration, chatbot, virtual assistant
     - name: Reference
       items:
       - name: General
@@ -598,6 +670,7 @@ items:
     items:
     - name: Text Analytics for health overview
       href: text-analytics-for-health/overview.md
+      displayName: healthcare nlp, medical text analysis, clinical text, health entities
     - name: Text Analytics for health quickstart
       href: text-analytics-for-health/quickstart.md
     - name: Text Analytics for health language support
@@ -641,7 +714,7 @@ items:
     items:
     - name: Summarization overview
       href: summarization/overview.md
-      displayName: native, native document
+      displayName: native document
     - name: Summarization quickstart
       href: summarization/quickstart.md
     - name: Summarization language support
@@ -679,15 +752,16 @@ items:
       - name: Data, privacy, and security
         href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
         displayName: Data privacy, logging, data retention
-
 - name: Concepts
   items:
   - name: Developer guide
     href: concepts/developer-guide.md
+    displayName: development, sdk guide, programming
   - name: Role-based-access-control
     href: concepts/role-based-access-control.md
   - name: Multilingual and emoji support
     href: concepts/multilingual-emoji-support.md
+    displayName: international, characters
   - name: Model lifecycle
     href: concepts/model-lifecycle.md
   - name: Send requests asynchronously
@@ -703,15 +777,14 @@ items:
   - name: Data, privacy, and security
     href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
     displayName: Data privacy, logging, data retention
-
 - name: How-tos
   items:
   - name: Migrate from LUIS, QnA Maker, and Text Analytics
     displayName: text analytics, luis, qna
     href: concepts/migrate.md
   - name: Use Azure Kubernetes Service
     href: tutorials/use-kubernetes-service.md
-  - name: Use language in power automate flows
+  - name: Use language in Power Automate flows
     href: tutorials/power-automate.md
   - name: Native document support
     items:
@@ -726,7 +799,7 @@ items:
       - name: Call Center
         items:
         - name: Overview
-          displayName: IVRs, IVR, Telephony Data, Transcription for Telephony Data, Real-time Transcription for Call Centers, Post-Call Analytics
+          displayName: ivrs, ivr, telephony data, transcription for telephony data, real-time transcription for call centers, post-call analytics
           href: ../speech-service/call-center-overview.md?context=%2fazure%2fai-services%2flanguage-service%2fcontext%2fcontext
         - name: Post-call transcription and analytics quickstart
           href: ../speech-service/call-center-quickstart.md?context=%2fazure%2fai-services%2flanguage-service%2fcontext%2fcontext
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピック構成ファイルの更新"
}
```

### Explanation
この変更は、Azure AI Languageサービスに関連するトピック構成ファイル（`toc.yml`）の内容が大幅に更新されたことを示しています。この更新により、新しい項目が追加され、既存の項目が整理され、情報がより明確になっています。

具体的なポイントは以下のとおりです：

- **新しい項目の追加**: 89件の新しいエントリが追加され、コンテンツの網羅性が向上しています。これにより、ユーザーはさまざまなトピックについての情報に容易にアクセスできるようになりました。
- **削除された項目**: 16件の項目が削除され、全体の構造が整理されました。これによって、古くなった情報や重複したエントリが排除されています。
- **表示名の追加**: 各エントリに対して表示名（`displayName`）が追加され、ユーザーがトピックの内容をより直感的に理解できるようになりました。これにより、検索やナビゲーションが改善され、用途に応じた情報を簡単に見つけやすくなっています。
- **トピックの統合と整理**: さまざまなトピックがより論理的に整理されることにより、ユーザーは関心のある分野に関連する情報を一目で見つけやすくなっています。

これらの変更により、Azure AI Languageサービスに関する学習や実装を行うユーザーにとって、より効果的で使いやすいリソースが提供されることが期待されます。全体的に、ドキュメントの質が向上し、ユーザーの体験が強化されています。


