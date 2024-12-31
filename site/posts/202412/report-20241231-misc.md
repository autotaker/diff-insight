---
date: '2024-12-31'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c18cb3f...MicrosoftDocs:5abf9d6
summary: このコードの変更は、新しい機能の追加とマイナーアップデートを含んでいます。特に、新しいRBAC割り当て手順を示す`assign-rbac.md`の追加や、チャットウェブアプリケーションのデプロイチュートリアルの改善が挙げられます。重要な破壊的変更はなく、既存の流れに若干の影響を与える可能性があります。また、ドキュメントの日付更新、SDK評価方法の改善、不要な画像ファイルの削除などの整理も行われました。全体的に、ユーザビリティの向上と情報提供の明確化を目指しており、特に手順の整理やナビゲーションの向上が意図されています。変更の詳細はGitHubのリポジトリで確認できます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c18cb3f...MicrosoftDocs:5abf9d6){target="_blank"}

# Highlights
このコードの変更には、いくつかの新しい機能追加とマイナーアップデートが含まれています。特に注目すべきは、新しいRBAC割り当て手順の追加と、チャットウェブアプリケーションデプロイチュートリアルの改善です。

## New features
- `assign-rbac.md`が新たに追加され、AzureポータルでのRBAC割り当て手順が明確に記載される。
- 新しい画像ファイル`resources.png`が追加され、デプロイ手順を視覚的にサポート。

## Breaking changes
特に重大な破壊的変更はないが、新しい手順や機能によって既存の流れが変わる可能性がある。

## Other updates
- ドキュメントの日付の更新。
- SDK評価方法やAzure AI Searchサービスの説明の改善。
- 必要のない画像ファイルが削除され、ドキュメントが整理された。

# Insights
今回の変更の背後にある考え方は、主にユーザビリティの向上と情報の明確化に重点を置いていることである。`assign-rbac.md`のような新しいドキュメントの追加は、具体的な操作手順をユーザーに提供することで、Azureのリソース管理をより直感的に行えるようにするためである。また、ドキュメントおよびチュートリアルの更新は、新機能の導入に応じた最新の情報を提供し、ユーザーがシステムを効率よく利用できるようにする目的がある。

特に、`deploy-chat-web-app.md`の改善は、手順の明確化と整理によってユーザーが必要な作業を追跡しやすくするためである。チェックリスト形式での手順整理や、前提条件と操作手順の区別など、ユーザーの視点に立った改良が見られる。さらに、特定のセクションに対するリンクの追加は、ナビゲーションを容易にし、特定の情報を素早く見つけるサポートをする。

これらの変更は、全体としてAzureのAIリソースを効果的に利用するためのガイドラインを再編成しユーザー体験を向上させることを目的としている。変更の細部はGitHubのリポジトリで確認でき、ここで紹介したドキュメントや機能の改定は、まさにそれらを支える役割を果たしている。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [evaluation-approach-gen-ai.md](#item-ac9697) | minor update | 日付の更新: evaluation-approach-gen-ai.md | modified | 1 | 1 | 2 | 
| [evaluate-sdk.md](#item-9d5197) | minor update | SDK評価方法のコード修正: evaluate-sdk.md | modified | 3 | 5 | 8 | 
| [flow-deploy.md](#item-e7fc64) | minor update | 権限関連の文言修正: flow-deploy.md | modified | 2 | 2 | 4 | 
| [assign-rbac.md](#item-8e21c7) | new feature | RBAC割り当て手順の追加: assign-rbac.md | added | 28 | 0 | 28 | 
| [chat-with-data.md](#item-0c0cfc) | minor update | チャットプレイグラウンドのデータ追加手順の改訂: chat-with-data.md | modified | 2 | 8 | 10 | 
| [add-your-data-connect-search-add.png](#item-cb2d7a) | minor update | 不必要な画像ファイルの削除: add-your-data-connect-search-add.png | removed | 0 | 0 | 0 | 
| [add-your-data-connect-search.png](#item-dcc838) | minor update | 不要な画像ファイルの削除: add-your-data-connect-search.png | removed | 0 | 0 | 0 | 
| [resources.png](#item-669fb8) | new feature | 新しい画像ファイルの追加: resources.png | added | 0 | 0 | 0 | 
| [copilot-sdk-create-resources.md](#item-552960) | minor update | Azure AI Searchサービスの見出しの修正 | modified | 1 | 1 | 2 | 
| [deploy-chat-web-app.md](#item-987845) | minor update | チャットウェブアプリデプロイチュートリアルの改善 | modified | 118 | 33 | 151 | 


# Modified Contents
## articles/ai-studio/concepts/evaluation-approach-gen-ai.md{#item-ac9697}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: conceptual
-ms.date: 5/21/2024
+ms.date: 12/23/2024
 ms.reviewer: mithigpe
 ms.author: lagayhar
 author: lgayhardt
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新: evaluation-approach-gen-ai.md"
}
```

### Explanation
この変更は、`evaluation-approach-gen-ai.md`というファイルの最終更新日を変更しています。具体的には、元々の更新日であった「2024年5月21日」が「2024年12月23日」に更新されています。この変更はマイナーな更新と見なされ、文書の内容に大きな影響を与えるものではありませんが、正確な日付を反映させるために重要です。変更の詳細は、GitHub上のリポジトリで確認できます。

## articles/ai-studio/how-to/develop/evaluate-sdk.md{#item-9d5197}

<details>
<summary>Diff</summary>
````diff
@@ -444,20 +444,18 @@ Sometimes a large language model isn't needed for certain evaluation metrics. Th
 class AnswerLengthEvaluator:
     def __init__(self):
         pass
-
+    # A class is made a callable my implementing the special method __call__
     def __call__(self, *, answer: str, **kwargs):
         return {"answer_length": len(answer)}
 ```
 
 Then run the evaluator on a row of data by importing a callable class:
 
 ```python
-with open("answer_len/answer_length.py") as fin:
-    print(fin.read())
-
 from answer_len.answer_length import AnswerLengthEvaluator
 
-answer_length = AnswerLengthEvaluator()(answer="What is the speed of light?")
+answer_length_evaluator = AnswerLengthEvaluator()
+answer_length = answer_length_evaluator(answer="What is the speed of light?")
 
 print(answer_length)
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SDK評価方法のコード修正: evaluate-sdk.md"
}
```

### Explanation
この変更は、`evaluate-sdk.md`ファイル内のコードスニペットに対する修正を行っています。具体的には、クラス `AnswerLengthEvaluator` の使用方法が改良され、コードの可読性が向上しています。具体的には、`__call__`メソッドの実装内容の前にコメントが追加され、クラスのインスタンス化と呼び出し方法の記述が変更されました。

変更前は、直接ファイルを開いてコードを読み込む方法が示されていましたが、現在は `AnswerLengthEvaluator` クラスのインスタンスを作成してから呼び出す方式に変更されています。このように、言語モデルの評価においてクラスを使ったより明確なアプローチを示すようになっており、使い方がわかりやすくなっています。詳細な変更内容はGitHubリポジトリで確認できます。

## articles/ai-studio/how-to/flow-deploy.md{#item-e7fc64}

<details>
<summary>Diff</summary>
````diff
@@ -142,12 +142,12 @@ If you created the associated endpoint with **User Assigned Identity**, the user
 |Azure AI Foundry project|**Azure Machine Learning Workspace Connection Secrets Reader** role **OR** a customized role with `Microsoft.MachineLearningServices/workspaces/connections/listsecrets/action` | Get project connections|
 |Azure AI Foundry project container registry |**ACR pull** |Pull container image |
 |Azure AI Foundry project default storage| **Storage Blob Data Reader**| Load model from storage |
-|Azure AI Foundry project|**Workspace metrics writer**| After you deploy then endpoint, if you want to monitor the endpoint related metrics like CPU/GPU/Disk/Memory utilization, you need to give this permission to the identity.<br/><br/>Optional|
+|Azure AI Foundry project|**AzureML Metrics Writer (preview)**| After you deploy then endpoint, if you want to monitor the endpoint related metrics like CPU/GPU/Disk/Memory utilization, you need to give this permission to the identity.<br/><br/>Optional|
 
 See detailed guidance about how to grant permissions to the endpoint identity in [Grant permissions to the endpoint](#grant-permissions-to-the-endpoint).
 
 > [!IMPORTANT]
-> If your flow uses Microsoft Entra ID based authentication connections, no matter you use system-assigned identity or user-assigned identity, you always need to grant the managed identity appropriate roles of the corresponding resources so that it can make API calls to that resource. For example, if your Azure OpenAI connection uses Microsoft Entra ID based authentication, you need to grant your endpoint managed identity **Cognitive Services OpenAI User or Cognitive Services OpenAI Contributor role** of the corresponding Azure OpenAI resources.
+> If your flow uses Microsoft Entra ID based authentication connections, whether you use system-assigned identity or user-assigned identity, you always need to grant the managed identity appropriate roles of the corresponding resources so that it can make API calls to that resource. For example, if your Azure OpenAI connection uses Microsoft Entra ID based authentication, you need to grant your endpoint managed identity **Cognitive Services OpenAI User or Cognitive Services OpenAI Contributor role** of the corresponding Azure OpenAI resources.
 
 ### Advanced settings - Outputs & Connections
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "権限関連の文言修正: flow-deploy.md"
}
```

### Explanation
この変更は、`flow-deploy.md`ファイル内の権限に関する文言を修正することを目的としています。具体的には、Azure AI Foundryプロジェクトに必要な権限のリストが更新され、特に「Workspace metrics writer」という役割が「AzureML Metrics Writer (preview)」に名前が変更されています。この変更は、ユーザーに対してより直感的で理解しやすい表現を提供するためのものであり、機能に関する説明が明確になっています。

また、「Microsoft Entra IDベースの認証接続を使用する場合」の注意書きの文が若干わかりやすく変更され、ユーザーが必要な権限を理解しやすくするための工夫がなされています。具体的な変更はGitHubリポジトリで確認することができます。

## articles/ai-studio/includes/assign-rbac.md{#item-8e21c7}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,28 @@
+---
+title: Include file
+description: Include file
+author: sdgilley
+ms.reviewer: sgilley
+ms.author: sgilley
+ms.service: azure-ai-studio
+ms.topic: include
+ms.date: 12/27/2024
+ms.custom: include
+---
+
+The general pattern for assigning role-based access control (RBAC) for any resource is:
+
+1. Navigate to the Azure portal for the given resource. 
+1. From the left page in the Azure portal, select **Access control (IAM)**. 
+1. Select **+ Add** > **Add role assignment**.
+1. Search for the role you need to assign and select it. Then select **Next**.
+1. When assigning a role to yourself: 
+    1. Select **User, group, or service principal**. 
+    1. Select **Select members**.
+    1. Search for your name and select it.
+1. When assigning a role to another resource: 
+    1. Select **Managed identity**. 
+    1. Select **Select members**.
+    1. Use the dropdown to find the type of resource you want to assign. For example, **Azure AI services** or **Search service**.
+    1. Select the resource from the list that appears. There might only be one, but you still need to select it.
+1. Continue through the wizard and select **Review + assign** to add the role assignment.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "RBAC割り当て手順の追加: assign-rbac.md"
}
```

### Explanation
この変更は、`assign-rbac.md`という新しいファイルが追加されたことを示しています。このファイルには、Azureポータルでのリソースの役割ベースのアクセス制御（RBAC）を割り当てるための一般的な手順が詳細に記載されています。

具体的には、RBACを割り当てる際のステップバイステップのガイドが含まれており、Azureポータルにおける操作手順が明瞭に説明されています。手順には、アクセス制御のセクションに移動し、役割の割り当てを追加するプロセスが含まれています。また、自分自身または他のリソースに役割を割り当てる際の具体的な手順が提示されています。

この詳細なガイドは、ユーザーがAzureリソースにおける役割の管理を容易に理解し、適切にアクセス制御を実施できるよう支援するために追加されました。ファイルのコントentはGitHubリポジトリで確認できます。

## articles/ai-studio/includes/chat-with-data.md{#item-0c0cfc}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ Follow these steps to add your data in the chat playground to help the assistant
 
     :::image type="content" source="../media/tutorials/chat/playground-chat.png" alt-text="Screenshot of the chat playground with the chat mode and model selected." lightbox="../media/tutorials/chat/playground-chat.png":::
  
-1. On the left side of the chat playground, select **Add your data** > **+ Add a new data source**.
+1. On the left side of the chat playground, select **Add your data (PREVIEW)** > **+ Add a new data source**.
 
     :::image type="content" source="../media/tutorials/chat/add-your-data.png" alt-text="Screenshot of the chat playground with the option to add a data source visible." lightbox="../media/tutorials/chat/add-your-data.png":::
 
@@ -37,13 +37,7 @@ Follow these steps to add your data in the chat playground to help the assistant
 
    :::image type="content" source="../media/tutorials/chat/add-your-data-uploaded.png" alt-text="Screenshot of the dialog to select and upload files." lightbox="../media/tutorials/chat/add-your-data-uploaded.png":::
 
-1. Select an Azure AI Search service. In this example we select **Connect other Azure AI Search resource** from the **Select Azure AI Search service** dropdown. If you don't have a search resource, you can create one by selecting **Create a new Azure AI Search resource**. Then return to this step to connect and select it.
-
-    :::image type="content" source="../media/tutorials/chat/add-your-data-connect-search.png" alt-text="Screenshot of the search resource selection options." lightbox="../media/tutorials/chat/add-your-data-connect-search.png":::
-
-1. Browse for your Azure AI Search service, and select **Add connection**. 
-
-    :::image type="content" source="../media/tutorials/chat/add-your-data-connect-search-add.png" alt-text="Screenshot of the page to add a search service connection." lightbox="../media/tutorials/chat/add-your-data-connect-search-add.png":::
+1. Select your **Azure AI Search** service.
 
 1. For the **Vector index name**, enter *product-info* and select **Next**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットプレイグラウンドのデータ追加手順の改訂: chat-with-data.md"
}
```

### Explanation
この変更は、`chat-with-data.md`ファイル内のチャットプレイグラウンドへのデータの追加手順を更新したものです。主な変更点として、「Add your data」というオプションのテキストが「Add your data (PREVIEW)」に変更され、機能がプレビューモードであることが明示されています。

また、一部の手順が簡素化され、複数行にわたる説明が削除されています。その結果、ユーザーはAzure AI Searchサービスを選択し、必要な接続を設定するステップをスムーズに進めることができるようになりました。新しい手順では、サービスの選択後、直接Azure AI Searchサービスを選ぶようになっており、取扱が簡略化されています。

この改訂は、ユーザー体験を向上させることを目的としており、手順の明確さと簡潔さを重視しています。詳細はGitHubリポジトリで確認できます。

## articles/ai-studio/media/tutorials/chat/add-your-data-connect-search-add.png{#item-cb2d7a}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "不必要な画像ファイルの削除: add-your-data-connect-search-add.png"
}
```

### Explanation
この変更は、`add-your-data-connect-search-add.png`という画像ファイルがリポジトリから削除されたことを示しています。このファイルは、チャットのデータ追加手順に関連していたと思われますが、現在のドキュメントや手順において必要ないと判断されたため、削除されました。

この削除は、使用されていないリソースを減らすことによってプロジェクトの整理や効率化を図るためのものであり、ファイルサイズを小さくすることで管理を容易にする意図があります。

具体的なビジュアルコンテンツの更新に関する背景情報は提供されていないため、ユーザーには他の関連画像や情報を参照しながら、引き続き手順を進めてほしいと思われます。変更の詳細はGitHubリポジトリで確認できます。

## articles/ai-studio/media/tutorials/chat/add-your-data-connect-search.png{#item-dcc838}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "不要な画像ファイルの削除: add-your-data-connect-search.png"
}
```

### Explanation
この変更は、`add-your-data-connect-search.png`という画像ファイルがリポジトリから削除されたことを示しています。この画像は、チャットでデータを追加するプロセスに関連していたと考えられますが、最新版のドキュメントには必要な情報が他の手段で補完されているため、削除された可能性があります。

この削除は、ドキュメントを整理し、不要なリソースを取り除くことによって、リポジトリの清潔さとメンテナンスの容易さを向上させる意図があります。また、関連する情報が他の画像やテキストでカバーされている場合、利用者にとって混乱を避けることができる利点もあります。

このファイルの削除に関する具体的な理由は明示されていませんが、変更の詳細はGitHubリポジトリで確認できます。

## articles/ai-studio/media/tutorials/deploy-chat-web-app/resources.png{#item-669fb8}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像ファイルの追加: resources.png"
}
```

### Explanation
この変更は、`resources.png`という新しい画像ファイルがリポジトリに追加されたことを示しています。この画像は、チャットウェブアプリケーションのデプロイに関するチュートリアルで使用されるリソースを視覚的に示す目的で追加されたと考えられます。

新たに追加された画像は、ユーザーがアプリケーションのセットアップやデプロイメントプロセスを理解しやすくするための補足情報として機能します。視覚的なリソースがあることで、手順の理解を助け、実施すべき作業を明確にする効果が期待されます。

この変更は、ユーザー体験を向上させるためのものであり、具体的な内容はGitHubリポジトリで確認することができます。新しいリソースは、関連するチュートリアルの文脈で重要な役割を果たすでしょう。

## articles/ai-studio/tutorials/copilot-sdk-create-resources.md{#item-552960}

<details>
<summary>Diff</summary>
````diff
@@ -70,7 +70,7 @@ These steps deploy a model to a real-time endpoint from the Azure AI Foundry por
 
 After you deploy the **gpt-4o-mini**, repeat the steps to deploy the **text-embedding-ada-002** model.
 
-## Create an Azure AI Search service
+## <a name="create-search"></a> Create an Azure AI Search service
 
 The goal with this application is to ground the model responses in your custom data. The search index is used to retrieve relevant documents based on the user's question.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchサービスの見出しの修正"
}
```

### Explanation
この変更は、`copilot-sdk-create-resources.md`というファイル内の特定の見出しを修正する内容です。具体的には、「Azure AI Searchサービスを作成する」セクションの見出しが、より明確にするために変更されました。

修正内容としては、見出しの前にHTMLのアンカー要素 `<a name="create-search"></a>` が追加されました。この変更により、ユーザーがこのセクションに直接リンクできるようになり、ドキュメント内のナビゲーションが向上します。これにより、特定の情報をすぐに見つけられる利便性が高まります。

全体的に、この変更は文書の可読性と使いやすさを向上させることを目的としており、具体的な変更点はGitHubリポジトリで確認することができます。

## articles/ai-studio/tutorials/deploy-chat-web-app.md{#item-987845}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: tutorial
-ms.date: 11/14/2024
+ms.date: 12/27/2024
 ms.reviewer: tgokal
 ms.author: sgilley
 author: sdgilley
@@ -26,92 +26,173 @@ Your data source is used to help ground the model with specific data. Grounding
 
 The steps in this tutorial are:
 
-1. Deploy and test a chat model without your data.
-1. Add your data.
-1. Test the model with your data.
-1. Deploy your web app.
+> [!div class="checklist"]
+> * Configure resources.
+> * Add your data.
+> * Test the model with your data.
+> * Deploy your web app.
 
 ## Prerequisites
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
 - A [deployed Azure OpenAI](../how-to/deploy-models-openai.md) chat model. Complete the [Azure AI Foundry playground quickstart](../quickstarts/get-started-playground.md) to create this resource if you haven't already.
 
-- An [Azure AI Search service connection](../how-to/connections-add.md#create-a-new-connection) to index the sample product data.
+- A Search service connection to index the sample product data.  If you don't have one, follow the steps to [create](copilot-sdk-create-resources.md#create-search) and [connect](copilot-sdk-create-resources.md#connect) a search service.
 
 - A local copy of product data. The [Azure-Samples/rag-data-openai-python-promptflow repository on GitHub](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/) contains sample retail product information that's relevant for this tutorial scenario. Specifically, the `product_info_11.md` file contains product information about the TrailWalker hiking shoes that's relevant for this tutorial example. [Download the example Contoso Trek retail product data in a ZIP file](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/raw/refs/heads/main/tutorial/data/product-info.zip) to your local machine.
 
-- A **Microsoft.Web** resource provider registered in the selected subscription, to be able to deploy to a web app.
+- A **Microsoft.Web** resource provider registered in the selected subscription, to be able to deploy to a web app. For more information on registering a resource provide, see [Register resource provider](/azure/azure-resource-manager/management/resource-providers-and-types#register-resource-provider-1).
+
+- Necessary permissions to add role assignments in your Azure subscription. Granting permissions by role assignment is only allowed by the Owner of the specific Azure resources.
+
+## Azure AI Foundry portal and Azure portal 
+
+In this tutorial, you perform some tasks in the Azure AI Foundry portal and some tasks in the Azure portal.
+
+The Azure AI Foundry portal is a web-based environment for building, training, and deploying AI models. As a developer, it's where you will build and deploy your chat web application.
+
+The Azure portal allows an administrator to manage and monitor Azure resources. As an administrator, you'll use the portal to configure settings for various Azure services required for access from the web app.
+
+## Configure resources
+
+> [!IMPORTANT]
+> You must have the necessary permissions to add role assignments in your Azure subscription. Granting permissions by role assignment is only allowed by the Owner of the specific Azure resources. You might need to ask your Azure subscription owner (who might be your IT admin) to complete this section for you.
+
+In order for the resources to work correctly inside a web app, you need to configure them with the correct permissions. This work is done in the Azure portal.
+
+To start, identify the resources you need to configure from the Azure AI Foundry portal.
+
+1. Open the [Azure AI Foundry portal](https://ai.azure.com) and select the project you used to deploy the Azure OpenAI chat model.
+1. Select **Management center** from the left pane.
+1. Select **Connected resources** under your project.
+1. Identify the three resources you need to configure:  the **Azure OpenAI**, the **Azure AI Search**, and the **Azure Blob storage** that corresponds to your **workspaceblobstore**.
+
+    :::image type="content" source="../media/tutorials/deploy-chat-web-app/resources.png" alt-text="Screenshot shows the connected resources that need to be configured.":::
+
+    > [!TIP]
+    > If you have multiple **Azure OpenAI** resources, use the one that contains your deployed chat model.
+
+1. For each resource, select the link to open the resource details.  From the details page, select the resource name to open the resource in the Azure portal.  (For the workspaceblobstore, select **View in Azure Portal**). 
+1. After the browser tab opens, go back to the Azure AI Foundry portal and repeat the process for the next resource. 
+1. When you're done, you should have three new browser tabs open, for **Search service**, **Azure AI services**, and **blobstore Container**. Keep all three new tabs open as you'll go back and forth between them to configure the resources.
+
+### Enable managed identity
+
+On the browser tab for the **Search service** resource in the Azure portal, enable the managed identity:
+
+1. From the left pane, under **Settings**, select **Identity**.
+1. Switch **Status** to **On**.
+1. Select **Save**.
+
+On the browser tab for the **Azure AI services** resource in the Azure portal, enable the managed identity:
+
+1. From the left pane, under **Resource Management**, select **Identity**.
+1. Switch **Status** to **On**.
+1. Select **Save**.
+
+### Set access control for search
+
+On the browser tab for the **Search service** resource in the Azure portal, set the API Access policy:
+
+1. From the left pane, under **Settings**, select **Keys**.
+1. Under **API Access control**, select **Both**.
+1. When prompted, select **Yes** to confirm the change.
+
+### Assign roles
+
+You'll repeat this pattern multiple times in the bulleted items below.
+
+[!INCLUDE [Assign RBAC](../includes/assign-rbac.md)]
+
+Use these steps to assign roles for the resources you're configuring in this tutorial:
+
+* Assign the following roles on the browser tab for **Search service** in the Azure portal:
+    * **Search Index Data Reader** to the **Azure AI services** managed identity
+    * **Search Service Contributor** to the **Azure AI services** managed identity
+    * **Contributor** to yourself (to find **Contributor**, switch to the **Privileged administrator roles** tab at the top.  All other roles are in the **Job function roles** tab.)
+
+* Assign the following roles on the browser tab for **Azure AI services** in the Azure portal:
+
+    * **Cognitive Services OpenAI Contributor** to the **Search service** managed identity
+    * **Contributor** to yourself.
+
+* Assign the following roles on the browser tab for **Azure Blob storage** in the Azure portal:
+
+    * **Storage Blob Data Contributor** to the **Azure AI services** managed identity
+    * **Storage Blob Data Reader** to the **Search service** managed identity
+    * **Contributor** to yourself
+
+You're done configuring resources. You can close the Azure portal browser tabs now if you wish.
 
 ## Add your data and try the chat model again
 
-In the [Azure AI Foundry playground quickstart](../quickstarts/get-started-playground.md) (that's a prerequisite for this tutorial), observe how your model responds without your data. Now you add your data to the model to help it answer questions about your products.
+In the [Azure AI Foundry playground quickstart](../quickstarts/get-started-playground.md) (that's a prerequisite for this tutorial), observe how your model responds without your data. Now add your data to the model to help it answer questions about your products.
 
 [!INCLUDE [Chat with your data](../includes/chat-with-data.md)] 
 
 ## Deploy your web app
 
-Once you're satisfied with the experience in Azure AI Foundry portal, you can deploy the model as a standalone web application. 
+Once you're satisfied with the experience in the Azure AI Foundry portal, you can deploy the model as a standalone web application. 
 
 ### Find your resource group in the Azure portal
 
 In this tutorial, your web app is deployed to the same resource group as your [Azure AI Foundry hub](../how-to/create-secure-ai-hub.md). Later you configure authentication for the web app in the Azure portal.
 
-Follow these steps to navigate from Azure AI Foundry to your resource group in the Azure portal:
+Follow these steps to navigate to your resource group in the Azure portal:
 
 1. Go to your project in [Azure AI Foundry](https://ai.azure.com). Then select **Management center** from the left pane.
 1. Under the **Project** heading, select **Overview**.
-1. Select the resource group name to open the resource group in the Azure portal. In this example, the resource group is named `rg-contoso`.
+1. Select the resource group name to open the resource group in the Azure portal. In this example, the resource group is named `rg-sdg-ai`.
 
     :::image type="content" source="../media/tutorials/chat/resource-group-manage-page.png" alt-text="Screenshot of the resource group in the Azure AI Foundry portal." lightbox="../media/tutorials/chat/resource-group-manage-page.png":::
 
-1. You should now be in the Azure portal, viewing the contents of the resource group where you deployed the hub. Keep this page open in a browser tab. You return to it later.
+1. You should now be in the Azure portal, viewing the contents of the resource group where you deployed the hub. Notice the resource group name and location, you'll use this information in the next section.
+1. Keep this page open in a browser tab. You'll return to it later.
 
 ### Deploy the web app
 
 Publishing creates an Azure App Service in your subscription. It might incur costs depending on the [pricing plan](https://azure.microsoft.com/pricing/details/app-service/windows/) you select. When you're done with your app, you can delete it from the Azure portal.
 
 To deploy the web app:
 
-> [!NOTE]
-> You need to have **Microsoft.Web** resource provider registered in the selected subscription, to be able to deploy to a web app.
-
-1. Complete the steps in the previous section to [add your data](#add-your-data-and-try-the-chat-model-again) to the playground. 
+> [!IMPORTANT]
+> You need to [register **Microsoft.Web** as a resource provider](/azure/azure-resource-manager/management/resource-providers-and-types#register-resource-provider-1) before you can deploy to a web app. 
 
-    > [!NOTE]
-    > You can deploy a web app with or without your own data, but at least you need a deployed model as described in the [Azure AI Foundry playground quickstart](../quickstarts/get-started-playground.md).
+1. Complete the steps in the previous section to [add your data](#add-your-data-and-try-the-chat-model-again) to the playground.  (You can deploy a web app with or without your own data, but at least you need a deployed model as described in the [Azure AI Foundry playground quickstart](../quickstarts/get-started-playground.md)).
 
 1. Select **Deploy > ...as a web app**.
 
     :::image type="content" source="../media/tutorials/chat/deploy-web-app.png" alt-text="Screenshot of the deploy new web app button." lightbox="../media/tutorials/chat/deploy-web-app.png":::
 
 1. On the **Deploy to a web app** page, enter the following details:
     - **Name**: A unique name for your web app.
-    - **Subscription**: Your Azure subscription.
-    - **Resource group**: Select a resource group in which to deploy the web app. You can use the same resource group as the hub.
-    - **Location**: Select a location in which to deploy the web app. You can use the same location as the hub.
+    - **Subscription**: Your Azure subscription. If you don't see any available subscriptions, first [register **Microsoft.Web** as a resource provider](/azure/azure-resource-manager/management/resource-providers-and-types#register-resource-provider-1).
+    - **Resource group**: Select a resource group in which to deploy the web app. Use the same resource group as the hub.
+    - **Location**: Select a location in which to deploy the web app. Use the same location as the hub.
     - **Pricing plan**: Choose a pricing plan for the web app.
-    - **Enable chat history in the web app**: For the tutorial, the chat history box isn't selected. If you enable the feature, your users will have access to their individual previous queries and responses. For more information, see [chat history remarks](#understand-chat-history).
+    - **Enable chat history in the web app**: For the tutorial, the chat history box isn't selected. If you enable the feature, your users have access to their individual previous queries and responses. For more information, see [chat history remarks](#understand-chat-history).
 
 1. Select **Deploy**.
 
 1. Wait for the app to be deployed, which might take a few minutes. 
 
-1. When it's ready, the **Launch** button is enabled on the toolbar. But don't launch the app yet and don't close the chat playground page - you return to it later.
+1. When it's ready, the **Launch** button is enabled on the toolbar. But don't launch the app yet and don't close the chat playground page - you'll return to it later.
 
 ### Configure web app authentication
 
-By default, the web app will only be accessible to you. In this tutorial, you add authentication to restrict access to the app to members of your Azure tenant. Users are asked to sign in with their Microsoft Entra account to be able to access your app. You can follow a similar process to add another identity provider if you prefer. The app doesn't use the user's sign in information in any other way other than verifying they're a member of your tenant.
+By default, the web app is only accessible to you. In this tutorial, you add authentication to restrict access to the app to members of your Azure tenant. Users are asked to sign in with their Microsoft Entra account to be able to access your app. You can follow a similar process to add another identity provider if you prefer. The app doesn't use the user's sign in information in any other way other than verifying they're a member of your tenant.
 
-1. Return to the browser tab containing the Azure portal (or re-open the [Azure portal](https://portal.azure.com?azure-portal=true) in a new browser tab) and view the contents of the resource group where you deployed the hub and web app (you might need to refresh the view the see the web app).
+1. Return to the browser tab containing the Azure portal (or reopen the [Azure portal](https://portal.azure.com?azure-portal=true) in a new browser tab) and view the contents of the resource group where you deployed the web app (you might need to refresh the view the see the web app).
 
 1. Select the **App Service** resource from the list of resources in the resource group.
 
 1. From the collapsible left menu under **Settings**, select **Authentication**. 
 
     :::image type="content" source="../media/tutorials/chat/azure-portal-app-service.png" alt-text="Screenshot of web app authentication menu item under settings in the Azure portal." lightbox="../media/tutorials/chat/azure-portal-app-service.png":::
 
+1. If you see **Microsoft** listed an Identity provider on this page, nothing further is needed.  You can skip the next step.
 1. Add an identity provider with the following settings:
-    - **Identity provider**: Select Microsoft as the identity provider. The default settings on this page restrict the app to your tenant only, so you don't need to change anything else here. 
+    - **Identity provider**: Select Microsoft as the identity provider. The default settings on this page restrict the app to your tenant only, so you don't need to change anything else here.
     - **Tenant type**: Workforce
     - **App registration**: Create a new app registration
     - **Name**: *The name of your web app service*
@@ -121,21 +202,21 @@ By default, the web app will only be accessible to you. In this tutorial, you ad
 
 ### Use the web app
 
-You're almost there! Now you can test the web app.
+You're almost there. Now you can test the web app.
 
-1. Wait 10 minutes or so for the authentication settings to take effect.
-1. Return to the browser tab containing the chat playground page in Azure AI Foundry portal.
+1. If you changed settings, wait 10 minutes or so for the authentication settings to take effect.
+1. Return to the browser tab containing the chat playground page in the Azure AI Foundry portal.
 1. Select **Launch** to launch the deployed web app. If prompted, accept the permissions request.
 
-    *If the authentication settings haven't yet taken effect, close the browser tab for your web app and return to the chat playground in Azure AI Foundry portal. Then wait a little longer and try again.*
+    *If the authentication settings haven't yet taken effect, close the browser tab for your web app and return to the chat playground in the Azure AI Foundry portal. Then wait a little longer and try again.*
 
 1. In your web app, you can ask the same question as before ("How much are the TrailWalker hiking shoes"), and this time it uses information from your data to construct the response. You can expand the **reference** button to see the data that was used.
 
    :::image type="content" source="../media/tutorials/chat/chat-with-data-web-app.png" alt-text="Screenshot of the chat experience via the deployed web app." lightbox="../media/tutorials/chat/chat-with-data-web-app.png":::
 
 ## Understand chat history
 
-With the chat history feature, your users will have access to their individual previous queries and responses.
+With the chat history feature, your users have access to their individual previous queries and responses.
 
 You can enable chat history when you [deploy the web app](#deploy-the-web-app). Select the **Enable chat history in the web app** checkbox.
 
@@ -145,9 +226,13 @@ You can enable chat history when you [deploy the web app](#deploy-the-web-app).
 > Enabling chat history will create a [Cosmos DB instance](/azure/cosmos-db/introduction) in your resource group, and incur [additional charges](https://azure.microsoft.com/pricing/details/cosmos-db/autoscale-provisioned/) for the storage used.
 > Deleting your web app does not delete your Cosmos DB instance automatically. To delete your Cosmos DB instance, along with all stored chats, you need to navigate to the associated resource in the Azure portal and delete it.
 
-Once you've enabled chat history, your users will be able to show and hide it in the top right corner of the app. When the history is shown, they can rename, or delete conversations. As they're logged into the app, conversations will be automatically ordered from newest to oldest, and named based on the first query in the conversation.
+Once you enable chat history, your users are able to show and hide it in the top right corner of the app. When the history is shown, they can rename, or delete conversations. As they're logged into the app, conversations are automatically ordered from newest to oldest, and named based on the first query in the conversation.
+
+If you delete the Cosmos DB resource but keep the chat history option enabled on the studio, your users are notified of a connection error, but can continue to use the web app without access to the chat history.
+
+## Update the web app
 
-If you delete the Cosmos DB resource but keep the chat history option enabled on the studio, your users will be notified of a connection error, but can continue to use the web app without access to the chat history.
+Use the playground to add more data or test the model with different scenarios. When you're ready to update the web app with the new model, select **Deploy > ...as a web app** again. Select **Update an existing web app** and choose the existing web app from the list. The new model deploys to the existing web app.
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットウェブアプリデプロイチュートリアルの改善"
}
```

### Explanation
この変更は、`deploy-chat-web-app.md`というファイルの内容が大幅に更新されたもので、チャットウェブアプリケーションのデプロイに関するチュートリアルの改善が含まれています。追加された情報として、リソースの構成や必要な権限についての詳細な指示が含まれ、手順が視覚的にわかりやすくなるように整理されています。

主な更新点は以下の通りです：
- チェックリスト形式で手順が整理され、ユーザーが追跡しやすくなりました。
- 前提条件セクションが強化され、必要なリソースや設定が具体的に示されています。
- Azure AI FoundryポータルとAzureポータルの操作が区別され、各操作における注意事項や設定手順が明確に説明されています。
- 管理されたIDの有効化やアクセス制御の設定手順が追加され、セキュリティ設定の重要性が強調されています。
- チャット履歴機能やアプリケーションの更新手順についても詳細が追加され、ユーザーが新しい機能を活用しやすくなっています。

この変更は、ユーザーがAzure環境でチャットウェブアプリケーションを利用するためのガイダンスを向上させることを目的としており、実装に必要な情報が凝縮された形で整理されています。具体的な変更は、GitHubリポジトリで確認可能です。


