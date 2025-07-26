---
date: '2025-07-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8ca03b4...MicrosoftDocs:9c5e8b4
summary: このコード差分では、Azureの会話型言語理解（CLU）関連の複数のドキュメントが更新され、新しい画像ファイルが追加されました。主な変更は、文章の明確化とユーザー体験の向上を目的としたもので、関連手順や目次の名称も具体的な内容に改善されています。新しい画像ファイルの追加により、視覚的な情報が提供され、ユーザーは手順をより理解しやすくなっています。特に破壊的な変更はないものの、文言の修正により過去の説明からのニュアンスの変化が考えられます。全体として、Azureのドキュメントがよりユーザーフレンドリーに進化していることが示されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8ca03b4...MicrosoftDocs:9c5e8b4){target="_blank"}

# Highlights
このコード差分では、Azureの会話型言語理解（CLU）に関連する複数のドキュメントが更新され、新しい画像ファイルが追加されました。主な変更は文書の明確化と理解を向上させるためのものです。また、関連する手順やTOCの項目名も具体的な内容に変更されており、ユーザー体験の向上が図られています。

## New features
- 複数の新しい画像ファイルが追加され、視覚的な情報を提供することでユーザーが手順をより理解しやすくなっています。

## Breaking changes
- 今回の変更では特に重要な破壊的変更は含まれていませんが、文言の修正が行われたため、過去の説明とは異なるニュアンスになっている箇所があるかもしれません。

## Other updates
- 既存のドキュメント全体で用語や文言の小規模な修正が行われ、より一貫した表現が用いられるようになりました。
- ドキュメント内のリンクや項目名の一部が変更され、ユーザーが必要な情報にアクセスしやすくなりました。

# Insights
今回のコード差分は、Azure AIサービスのドキュメントをよりユーザーフレンドリーにするための取り組みを示しています。特に、視覚的な情報を提供する画像ファイルの追加は、ユーザーが手順を直感的に理解しやすくなるための重要なステップです。

具体的な変更内容としては、データ形式やプロジェクトの作成、トレーニング手順に関するドキュメントで、プロジェクトファイルや設定方法の説明がよりクリアになったことが挙げられます。ユーザーが手順を簡単にフォローできるよう、見出しや用語が具体化されている点も注目すべきです。

また、Azure AI Foundryを通じたプロジェクトの作成やリソースの設定に関する説明では、ユーザーが必要な操作をスムーズに実行できるよう、必要な事前条件や役割が整理されています。このような修正は、ユーザーの理解を助け、ミスを減らすことに寄与しています。

新たに追加された画像は、特に設定や削除といった操作を視覚的に伝えるもので、これにより文章だけでは曖昧になりがちな操作やコンセプトを明快に伝えることが可能になります。ユーザーエクスペリエンスの向上が、結果として製品の使用効率や効果的なトレーニングに寄与するでしょう。

最後に、目次（TOC）の調整は、ナビゲーションのしやすさを向上させ、ユーザーが必要な情報に直ちにアクセスできるようにするためのものです。これは、大規模なプロジェクトや多くのリソースが関与する場合に特に有益です。

総じて、この差分は、Azure AIのドキュメントが多様なユーザーのニーズに応えるために進化し続けていることを示しており、コミュニティに対して価値ある技術文書を提供し続ける姿勢を示しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [data-formats.md](#item-8559f6) | minor update | データ形式に関するドキュメントの更新 | modified | 5 | 5 | 10 | 
| [create-project.md](#item-58b2dd) | minor update | Azure AI Foundryプロジェクト作成に関するドキュメントの更新 | modified | 52 | 39 | 91 | 
| [tag-utterances.md](#item-3d1b2f) | minor update | 発話のタグ付け手順の更新 | modified | 5 | 5 | 10 | 
| [train-model.md](#item-f5b164) | minor update | モデルのトレーニング手順の更新 | modified | 2 | 2 | 4 | 
| [delete-hub.png](#item-19b921) | new feature | プロジェクト削除に関する画像の追加 | added | 0 | 0 | 0 | 
| [delete-project.png](#item-0a59d7) | new feature | プロジェクト削除に関する画像の追加 | added | 0 | 0 | 0 | 
| [download-config-json.png](#item-1aee3b) | new feature | 設定JSONファイルのダウンロードに関する画像の追加 | added | 0 | 0 | 0 | 
| [hub-details.png](#item-8a10c9) | new feature | ハブ詳細に関する画像の追加 | added | 0 | 0 | 0 | 
| [project-details.png](#item-88e11b) | new feature | プロジェクト詳細に関する画像の追加 | added | 0 | 0 | 0 | 
| [toc.yml](#item-12f1f0) | minor update | TOCの項目名の変更 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/ai-services/language-service/conversational-language-understanding/concepts/data-formats.md{#item-8559f6}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ If you're uploading your data into conversational language understanding, it mus
 
 ## Import project file format
 
-If you're [importing a project](../how-to/create-project.md#import-a-project) into conversational language understanding, the file uploaded must be in the following format:
+If you're [importing a project](../how-to/create-project.md#import-an-existing-azure-ai-project) into conversational language understanding, the file uploaded must be in the following format:
 
 ```json
 {
@@ -101,7 +101,7 @@ If you're [importing a project](../how-to/create-project.md#import-a-project) in
 |Key  |Placeholder  |Value  | Example |
 |---------|---------|----------|--|
 |`{API-VERSION}`     | The [version](../../concepts/model-lifecycle.md#api-versions) of the API you're calling. | `2023-04-01` |
-|`confidenceThreshold`|`{CONFIDENCE-THRESHOLD}`|This is the threshold score below which the intent is predicted as [None intent](none-intent.md). Values are from `0` to `1`.|`0.7`|
+|`confidenceThreshold`|`{CONFIDENCE-THRESHOLD}`|The threshold score for which the intent is predicted as [None intent](none-intent.md). Values are from `0` to `1`.|`0.7`|
 | `projectName` | `{PROJECT-NAME}` | The name of your project. This value is case sensitive. | `EmailApp` |
 | `multilingual` | `true`| A Boolean value that enables you to have utterances in multiple languages in your dataset. When your model is deployed, you can query the model in any supported language (not necessarily included in your training documents. For more information about supported language codes, see [Language support](../language-support.md#multi-lingual-option). | `true`|
 |`sublists`|`[]`|Array that contains sublists. Each sublist is a key and its associated values.|`[]`|
@@ -110,7 +110,7 @@ If you're [importing a project](../how-to/create-project.md#import-a-project) in
 | `language` | `{LANGUAGE-CODE}` |  A string specifying the language code for the utterances, synonyms, and regular expressions used in your project. If your project is a multilingual project, choose the [language code](../language-support.md) of most the utterances. |`en-us`|
 | `intents` | `[]` | Array that contains all the intents you have in the project. These intents are classified from your utterances.| `[]` |
 | `entities` | `[]` | Array that contains all the entities in your project. These entities are extracted from your utterances. Every entity can have other optional components defined with them: list, prebuilt, or regex. | `[]` |
-| `dataset` | `{DATASET}` |  The test set to which this utterance goes to when it's split before training. To learn more about data splitting, see [Train your conversational language understanding model](../how-to/train-model.md#data-splitting). Possible values for this field are `Train` and `Test`.      |`Train`|
+| `dataset` | `{DATASET}` |  The test set that this utterance is assigned to when the data is split before training. To learn more about data splitting, see [Train your conversational language understanding model](../how-to/train-model.md#data-splitting). Possible values for this field are `Train` and `Test`.      |`Train`|
 | `category` | ` ` |  The type of entity associated with the span of text specified. | `Entity1`|
 | `offset` | ` ` |  The inclusive character position of the start of the entity.      |`5`|
 | `length` | ` ` |  The character length of the entity.      |`5`|
@@ -166,7 +166,7 @@ Conversational language understanding offers the option to upload your utterance
 |---------|---------|----------|--|
 |`text`|`{Utterance-Text}`|Your utterance text.|Testing|
 | `language` | `{LANGUAGE-CODE}` |  A string that specifies the language code for the utterances used in your project. If your project is a multilingual project, choose the language code of most of the utterances. For more information about supported language codes, see [Language support](../language-support.md). |`en-us`|
-| `dataset` | `{DATASET}` |  The test set to which this utterance goes to when it's split before training. To learn more about data splitting, see [Train your conversational language understanding model](../how-to/train-model.md#data-splitting). Possible values for this field are `Train` and `Test`.      |`Train`|
+| `dataset` | `{DATASET}` |  The test set that this utterance is assigned to when the data is split before training. To learn more about data splitting, see [Train your conversational language understanding model](../how-to/train-model.md#data-splitting). Possible values for this field are `Train` and `Test`.      |`Train`|
 |`intent`|`{intent}`|The assigned intent.| intent1|
 |`entity`|`{entity}`|The entity to be extracted.| entity1|
 | `category` | ` ` |  The type of entity associated with the span of text specified. | `Entity1`|
@@ -175,5 +175,5 @@ Conversational language understanding offers the option to upload your utterance
 
 ## Related content
 
-* For more information on importing your labeled data into your project directly, see [Import project](../how-to/create-project.md#import-a-project).
+* For more information on importing your labeled data into your project directly, see [Import project](../how-to/create-project.md#import-an-existing-azure-ai-project).
 * For more information about labeling your data, see [Label your utterances in Language Studio](../how-to/tag-utterances.md). After you label your data, you can [train your model](../how-to/train-model.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ形式に関するドキュメントの更新"
}
```

### Explanation
この変更は、会話型言語理解に関連するデータ形式に関するドキュメントの一部に関するものです。具体的には、プロジェクトファイルのインポートに関するセクションで、文言の変更が行われました。元々の「既存のプロジェクトのインポート」という表現が「プロジェクトのインポート」に修正され、他の部分でも説明が明確化されています。

変更点の中で特に注目すべきは該当項目の説明の修正です。例えば、`confidenceThreshold` の定義が改訂され、意図が「None intent」と予測される閾値スコアの説明がより明確になっています。また、`dataset` に関する説明も同様に調整され、データがどのようにトレーニング中に分割されるかについての説明が強調されています。これにより、ユーザーはデータ形式の使用方法をより理解しやすくなります。

全体として、この変更は文書の明確さと理解を向上させるためのものです。

## articles/ai-services/language-service/conversational-language-understanding/how-to/create-project.md{#item-58b2dd}

<details>
<summary>Diff</summary>
````diff
@@ -6,64 +6,45 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 05/01/2025
+ms.date: 07/23/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
 ---
 
-# Create a CLU fine-tuning task
+# Create a CLU project in Azure AI Foundry
 
-Use this article to learn how to set up these requirements and create a project.
+Azure AI Foundry projects help you organize your work when exploring new ideas or developing prototypes for specific use cases. A Foundry project is created on an Azure AI Foundry resource. This type of project offers an easy setup and provides access to agents and Azure AI models.
+
+If you already have an Azure AI Language or multi-service resource—whether used on its own or through Language Studio—you can continue to use those existing Language resources within the Azure AI Foundry portal. For more information, see [How to use Azure AI services in the Azure AI Foundry portal](../../../../ai-services/connect-services-ai-foundry-portal.md).
 
 ## Prerequisites
 
 * An Azure subscription. If you don't have one, you can [create one for free](https://azure.microsoft.com/free/cognitive-services).
-* An Azure AI Language resource.
-
-### Create a Language resource
-
-Before you start using conversational language understanding (CLU), you need an Azure AI Language resource.
-
-> [!NOTE]
-> You need to have an Owner role assigned for the resource group to create a Language resource.
-
-[!INCLUDE [create a new resource from the Azure portal](../includes/resource-creation-azure-portal.md)]
-
-[!INCLUDE [create a new resource from Language Studio](../includes/resource-creation-language-studio.md)]
-
-## Sign in to Language Studio
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+* An [Azure AI Foundry resource](../../../multi-service-resource.md)
+  * For more information, *see* [Configure an Azure AI Foundry resource](configure-azure-resources.md#option-1-configure-an-azure-ai-foundry-resource).
+* After you create an Azure AI Foundry resource, [create a CLU project](#create-a-clu-project).
 
-[!INCLUDE [Sign in to Language studio](../includes/language-studio/sign-in-studio.md)]
+## Create a CLU project
 
-## Create a conversation project
-
-After you create a Language resource, create a CLU project.
+ An Azure AI Foundry project is created using an Azure AI Foundry resource. Projects are designed to help you organize your work. They offer various tools and resources that support the development, customization, and management of AI applications all within a centralized environment.
 
 ### [Azure AI Foundry](#tab/azure-ai-foundry)
 
-[!INCLUDE [Create project](../includes/language-studio/create-project.md)]
+ To learn how to create a CLU Foundry project, *see* [Create an AI Foundry project](../../../../ai-foundry/how-to/create-projects.md).
+
 
 ### [REST APIs](#tab/rest-api)
 
 [!INCLUDE [create project](../includes/rest-api/create-project.md)]
 
 ---
 
-## Import a project
+## Import an existing Azure AI project
 
 ### [Azure AI Foundry](#tab/azure-ai-foundry)
 
-You can export a CLU project as a JSON file at any time. On the conversation projects page, select a project, and on the top menu, select **Export**.
-
-:::image type="content" source="../media/export.png" alt-text="A screenshot that shows the CLU Export button." lightbox="../media/export.png":::
-
-You can reimport that project as a new project. If you import a project with the exact same name, it replaces the project's data with the newly imported project's data.
-
-If you have an existing Language Understanding (LUIS) application, you can _import_ the LUIS application JSON to CLU directly. It creates a Conversation project with all the pieces that are currently available: intents, machine learning entities, and utterances. For more information, see [Migrate from Language Understanding (LUIS) to conversational language understanding (CLU)](../how-to/migrate-from-luis.md).
-
-To import a project, select the arrow button next to **Create a new project** and select **Import**. Then select the LUIS or CLU JSON file.
-
-:::image type="content" source="../media/import.png" alt-text="A screenshot that shows the CLU Import button." lightbox="../media/import.png":::
+To import an existing Azure AI services project with Azure AI Foundry, you need to create a connection to the Azure AI services resource within your Azure AI Foundry project. For more information, *see* [Connect Azure AI Services projects to Azure AI Foundry](../../../../ai-services/connect-services-ai-foundry-portal.md)
 
 ### [REST APIs](#tab/rest-api)
 
@@ -77,7 +58,13 @@ You can import a CLU JSON into the service.
 
 ### [Azure AI Foundry](#tab/azure-ai-foundry)
 
-You can export a CLU project as a JSON file at any time. On the conversation projects page, select a project, and then select **Export**.
+You can download a CLU project as a **config.json** file:
+
+1. Navigate to your project home page.
+1. At the top of the page, select your project from the right page ribbon area.
+1. Select **Download config file**.
+
+    :::image type="content" source="../media/create-project/download-config-json.png" alt-text="Screenshot of project drop-down menu with the download config file hyperlink in the Azure AI Foundry.":::
 
 ### [REST APIs](#tab/rest-api)
 
@@ -87,11 +74,18 @@ You can export a CLU project as a JSON file at any time.
 
 ---
 
-## Get CLU project details
+## View and manage project details
 
 ### [Azure AI Foundry](#tab/azure-ai-foundry)
 
-[!INCLUDE [Language Studio project details](../includes/language-studio/project-details.md)]
+* On the project Home page, information about the project is found in the **Project details** section.
+* To view project settings, select **Management center** from the bottom of the left navigation pane, then select one of the following tabs:
+   *  **Overview** to view project details.
+   *  **Users** to manage users and roles.
+   *  **Models + endpoints** to manage deployments of your models and services.
+   *  **Connected resources** to manage connected resources for the project.
+
+   :::image type="content" source="../media/create-project/project-details.png" alt-text="Screenshot of the project details list in the Azure AI Foundry.":::
 
 ### [REST APIs](#tab/rest-api)
 
@@ -103,11 +97,30 @@ You can export a CLU project as a JSON file at any time.
 
 ### [Azure AI Foundry](#tab/azure-ai-foundry)
 
-[!INCLUDE [Delete project](../includes/language-studio/delete-project.md)]
+
+If you no longer need your project, you can delete it from the Azure AI Foundry.
+
+1. Navigate to the [Azure AI Foundry](https://ai.azure.com/) home page. Initiate the authentication process by signing in, unless you already completed this step and your session is active.
+1. Select the project that you want to delete from the **Keep building with Azure AI Foundry**
+1. Select **Management center**.
+1. Select **Delete project**.
+
+   :::image type="content" source="../media/create-project/delete-project.png" alt-text="Screenshot of the Delete project button in the Azure AI Foundry.":::
+
+To delete the hub along with all its projects:
+
+1. Navigate to the **Overview** tab inn the **Hub** section.
+
+   :::image type="content" source="../media/create-project/hub-details.png" alt-text="Screenshot of the hub details list in the Azure AI Foundry.":::
+
+1. On the right, select **Delete hub**. 
+1. The link opens the Azure portal for you to delete the hub there.
+
+   :::image type="content" source="../media/create-project/delete-hub.png" alt-text="Screenshot of the Delete hub button in the Azure AI Foundry.":::
 
 ### [REST APIs](#tab/rest-api)
 
-When you don't need your project anymore, you can use the APIs to delete your project.
+If you no longer need your project, delete it using the REST API.
 
 [!INCLUDE [Delete project](../includes/rest-api/delete-project.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryプロジェクト作成に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Foundryを使用して会話型言語理解（CLU）プロジェクトを作成するための手順に関するドキュメントの修正です。主な変更点として、ドキュメントのタイトルが「CLUファインチューニングタスクの作成」から「Azure AI FoundryでのCLUプロジェクトの作成」に変更され、内容も大幅に更新されています。

新しい部分では、Azure AI Foundryにおけるプロジェクトの重要性や、独自のリソースを使用した場合の操作方法について説明されています。また、プロジェクトを作成するための前提条件が明確化され、Azure AI Foundryリソースの設定や関連する役割について詳しく述べられています。

さらに、プロジェクトのインポートとエクスポートに関する手順も更新され、特に新しい「**config.json**」ファイルとしてのダウンロード方法が明示されました。これにより、ユーザーがプロジェクトを効率的に管理できるようになります。

全体として、この変更はAzure AI Foundryの利用を向上させるために必要な情報と手順の可視化を図っています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/tag-utterances.md{#item-3d1b2f}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.custom: language-service-clu
 
 After you [build a schema](build-schema.md) for your fine-tuning task, you add training utterances to your project. The utterances should be similar to what your users use when they interact with the project. When you add an utterance, you have to assign which intent it belongs to. After the utterance is added, label the words within your utterance that you want to extract as entities.
 
-Data labeling is a crucial step in the conversational language understanding (CLU) trained development lifecycle. This data is used in the next step when you train your model so that your model can learn from the labeled data. If you already labeled utterances, you can directly [import them into your project](create-project.md#import-a-project), if your data follows the [accepted data format](../concepts/data-formats.md). To learn more about importing labeled data, see [Create a CLU fine-tuning task](create-project.md#import-a-project). Labeled data informs the model about how to interpret text and is used for training and evaluation.
+Data labeling is a crucial step in the conversational language understanding (CLU) trained development lifecycle. This data is used in the next step when you train your model so that your model can learn from the labeled data. If you already labeled utterances, you can directly [import them into your project](create-project.md#import-an-existing-azure-ai-project), if your data follows the [accepted data format](../concepts/data-formats.md). To learn more about importing labeled data, see [Create a CLU fine-tuning task](create-project.md#import-an-existing-azure-ai-project). Labeled data informs the model about how to interpret text and is used for training and evaluation.
 
 > [!TIP]
 > Use the **Quick Deploy** option to implement custom CLU intent routing, which is powered by your own large language model deployment without adding or labeling any training data.
@@ -43,9 +43,9 @@ As you add utterances and label them, keep in mind:
 
 * For [multilingual projects](../language-support.md#multi-lingual-option), adding utterances in other languages increases the model's performance in these languages. Avoid duplicating your data across all the languages that you want to support. For example, to improve a calender bot's performance with users, a developer might add examples mostly in English and a few in Spanish or French. They might add utterances such as:
 
-  * "Set a meeting with **Matt** and **Kevin** **tomorrow** at **12 PM**." (English)
-  * "Reply as **tentative** to the **weekly update** meeting." (English)
-  * "Cancelar mi **próxima** reunión." (Spanish)
+  * `Set a meeting with **Matt** and **Kevin** **tomorrow** at **12 PM**.` (English)
+  * `Reply as **tentative** to the **weekly update** meeting.` (English)
+  * `Cancelar mi **próxima** reunión.` (Spanish)
 
 ## Label your utterances
 
@@ -111,7 +111,7 @@ Before you get started, the suggested utterances feature is available only if yo
 
 On the **Data labeling** page:
 
-1. Select **Suggest utterances**. A pane opens on the right and prompts you to select your Azure OpenAI resource and deployment.
+1. Select **Suggest utterances**. A pane opens and prompts you to select your Azure OpenAI resource and deployment.
 1. After you select an Azure OpenAI resource, select **Connect** so that your Language resource has direct access to your Azure OpenAI resource. It assigns your Language resource the **Cognitive Services User** role to your Azure OpenAI resource. Now your current Language resource has access to Azure OpenAI. If the connection fails, follow [these steps](#add-required-configurations-to-azure-openai-resource) to manually add the correct role to your Azure OpenAI resource.
 1. After the resource is connected, select the deployment. The model that we recommend for the Azure OpenAI deployment is `gpt-35-turbo-instruct`.
 1. Select the intent for which you want to get suggestions. Make sure the intent that you selected has at least five saved utterances to be enabled for utterance suggestions. The suggestions provided by Azure OpenAI are based on the most recent utterances that you added for that intent.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "発話のタグ付け手順の更新"
}
```

### Explanation
この変更は、会話型言語理解（CLU）における発話のタグ付けに関する手順を記述したドキュメントの更新を含んでいます。主な修正点は、インポートに関するリンクと部分的な文言の変更です。

具体的には、すでにタグ付けされた発話をプロジェクトに直接インポートする際のリンクが「プロジェクトのインポート」から「既存のAzure AIプロジェクトのインポート」に変更されました。これにより、ユーザーが正しい手順にアクセスしやすくなっています。また、一部の発話例の文言が強調され、コードブロック形式で表示されるようになりました。これにより、一貫性が増し、視覚的にもわかりやすくなっています。

ドキュメント内の他のセクションでも、Azure OpenAIリソースとの接続プロセスに関する説明がわかりやすく修正されています。これにより、ユーザーが発話を効果的にタグ付けし、モデルをより正確にトレーニングできるよう支援されています。

全体として、この変更はユーザーの理解を深め、効率的な作業ができるよう改善を図ったものです。

## articles/ai-services/language-service/conversational-language-understanding/how-to/train-model.md{#item-f5b164}

<details>
<summary>Diff</summary>
````diff
@@ -28,8 +28,8 @@ Model evaluation is triggered automatically after training is completed successf
 ## Prerequisites
 
 * **An active Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/free/cognitive-services).
-* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor)
-* **A project created in the Azure AI Foundry**. For more information, *see* [Create an AI Foundry project](../../../../ai-foundry/how-to/create-projects.md)
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+* **A project created in the Azure AI Foundry**. For more information, *see* [Create an AI Foundry project](../../../../ai-foundry/how-to/create-projects.md).
 * [**Your labeled utterances**](tag-utterances.md) tagged for your fine tuning task.
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのトレーニング手順の更新"
}
```

### Explanation
この変更は、会話型言語理解（CLU）モデルのトレーニング手順に関するドキュメントの一部に対する更新です。具体的には、前提条件セクションの内容が修正されています。

主な変更点として、二つの項目が強調された点は見逃せませんが、その内容自体には実質的な変更はなく、表現の一貫性を保つための小規模な調整が行われています。前提条件の各項目がインデントスタイルを統一するために若干の文言が追加または調整されています。

このドキュメントは、Azure AI Foundryプロジェクトの設定や要求される権限についての正確な情報を提供することで、ユーザーがスムーズにモデルをトレーニングできるようにサポートしています。全体として、これはユーザーフレンドリーさを向上させるための軽微な更新といえます。

## articles/ai-services/language-service/conversational-language-understanding/media/create-project/delete-hub.png{#item-19b921}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "プロジェクト削除に関する画像の追加"
}
```

### Explanation
この変更は、会話型言語理解（CLU）のプロジェクト作成に関するドキュメントに新しい画像ファイルが追加されたことを示しています。具体的には、「delete-hub.png」という画像が、新たにメディアフォルダーに追加されました。

この画像は、プロジェクトを削除する手順に関連していると考えられ、ユーザーが視覚的に理解しやすくなることを目的としているでしょう。画像の追加により、手順や重要な情報をより効果的に伝えることができ、ユーザー体験の向上が期待されます。全体として、この変更はコンテンツの視覚的な補強を図るための重要なステップです。

## articles/ai-services/language-service/conversational-language-understanding/media/create-project/delete-project.png{#item-0a59d7}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "プロジェクト削除に関する画像の追加"
}
```

### Explanation
この変更は、会話型言語理解（CLU）のプロジェクト作成に関連する重要な画像ファイルが新たに追加されたことを示しています。「delete-project.png」という画像が、プロジェクト削除の手順を視覚的に示すために、メディアフォルダーに追加されました。

この画像は、ユーザーがプロジェクトを削除する際の手順を理解しやすくするために役立ちます。視覚的な要素が加わることで、文章だけでは把握しづらい情報を効果的に補完し、全体的なユーザーエクスペリエンスの向上を促進します。この変更は、新機能として文書の内容を強化するための一環となります。

## articles/ai-services/language-service/conversational-language-understanding/media/create-project/download-config-json.png{#item-1aee3b}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "設定JSONファイルのダウンロードに関する画像の追加"
}
```

### Explanation
この変更では、会話型言語理解（CLU）のプロジェクト作成に関連する新しい画像ファイルが追加されました。「download-config-json.png」という画像は、設定JSONファイルのダウンロード手順を視覚的に示すためにメディアフォルダーに追加されています。

この画像は、ユーザーが設定ファイルをダウンロードする際のプロセスを理解しやすくすることを目的としており、テキスト情報だけでは伝わりづらい内容を補完する役割を果たします。その結果、ドキュメントの内容がより明確になり、ユーザーが必要な操作をスムーズに行えるようにサポートします。全体として、この変更はドキュメントの体験を向上させるための重要な追加と言えます。

## articles/ai-services/language-service/conversational-language-understanding/media/create-project/hub-details.png{#item-8a10c9}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ハブ詳細に関する画像の追加"
}
```

### Explanation
この変更は、会話型言語理解（CLU）のプロジェクト作成に関連する新しい画像ファイルが追加されたことを示しています。「hub-details.png」という画像は、プロジェクトのハブ詳細を視覚的に示すためにメディアフォルダーに追加されています。

この画像は、ユーザーがプロジェクトのハブ情報を理解する助けとなり、文書内の説明を補完する役割を果たします。ビジュアル要素を盛り込むことで、複雑な情報を効果的に伝え、ユーザーエクスペリエンスを向上させることが期待されます。この新機能は、ドキュメントの内容をより分かりやすくするための重要な追加となります。

## articles/ai-services/language-service/conversational-language-understanding/media/create-project/project-details.png{#item-88e11b}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "プロジェクト詳細に関する画像の追加"
}
```

### Explanation
この変更では、会話型言語理解（CLU）プロジェクトの作成に関連する新しい画像ファイル「project-details.png」が追加されました。この画像はプロジェクトの詳細情報を視覚的に表現するためにメディアフォルダーに加えられました。

この新しい画像は、ユーザーがプロジェクトの詳細を理解しやすくするために役立ち、テキスト情報だけでは伝わりづらい内容を補強する役割を果たします。ビジュアルコンテンツを追加することによって、ドキュメント全体の分かりやすさが向上し、ユーザーが必要な情報を迅速に把握できるようになることが期待されます。この変更は、ユーザーエクスペリエンスの向上に寄与する重要な追加です。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -148,7 +148,7 @@ items:
             href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
           - name: Azure AI containers overview
             href: ../cognitive-services-container-support.md
-        - name: Create projects
+        - name: Create a CLU Foundry project 
           href: conversational-language-understanding/how-to/create-project.md
           displayName: creation, clu project, setup
         - name: Build a schema
@@ -160,7 +160,7 @@ items:
         - name: Train a model
           href: conversational-language-understanding/how-to/train-model.md
           displayName: training, clu training, conversational model training
-        - name: Configure Azure resources
+        - name: Configure Azure and CLU resources
           href: conversational-language-understanding/how-to/configure-azure-resources.md
           displayName: configuration, fine-tuning, azure ai foundry, azure portal 
         - name: View your model's performance
@@ -564,7 +564,7 @@ items:
         href: question-answering/how-to/chit-chat.md
       - name: Change default answer
         href: question-answering/how-to/change-default-answer.md
-      - name: Configure Azure resources
+      - name: Configure your environment and Azure resources
         href: question-answering/how-to/configure-azure-resources.md
         displayName: configuration, fine-tuning, azure ai foundry, azure portal 
       - name: Analytics
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCの項目名の変更"
}
```

### Explanation
この変更は、目次ファイル（toc.yml）のいくつかの項目名が更新されたことを示しています。具体的には、プロジェクトの作成に関連するタイトルやリソースの設定に関する項目名が変更され、より具体的でわかりやすくなりました。 

例えば、「Create projects」という項目は「Create a CLU Foundry project」に変更され、より明確な指示を提供しています。また、「Configure Azure resources」は「Configure Azure and CLU resources」に、さらに「Configure Azure resources」は「Configure your environment and Azure resources」に修正されました。これにより、ユーザーは各項目の内容を一目で理解しやすくなり、ナビゲーションがより直感的になります。

この変更は、文書の整合性を高め、ユーザーが必要な情報を見つけやすくなることを目的としています。


