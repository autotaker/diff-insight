---
date: '2025-06-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d0f373d...MicrosoftDocs:0496181
summary: このコードの変更は、会話型言語理解サービスに関連する文書の修正を行い、用語の改善や一貫性の向上、文法修正を含む細かなアップデートを行っています。新しい機能は追加されていませんが、リンクテキストや手順説明、APIドキュメントの表現が改善され、全体的な文書の品質が向上しました。大きな破壊的変更はなく、既存情報の可読性と明確さが高められています。また、著者情報が更新され、今後の維持管理がしやすくなるよう配慮されています。これにより、ユーザーは文書から正確な手順を理解しやすくなり、信頼性も強化されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d0f373d...MicrosoftDocs:0496181){target="_blank"}

<format>
# Highlights
このコードの変更は、会話型言語理解サービスに関連する文書の修正を行うものであり、主に用語の改善、一貫性の向上、文法修正などの細かなアップデートが行われています。詳細には、リンクテキストやタイトルの修正、手順説明やAPIドキュメントの表現調整が含まれています。

## New features
特に新しい機能の追加はなく、文書内の表現と整合性を改善することに焦点が当てられています。

## Breaking changes
大きな破壊的変更は含まれておらず、既存の情報の可読性と明確さを高めることが目的です。

## Other updates
文書内のリンクテキスト、手順説明、APIリクエストの文言などが改善されており、文書の全体的な品質が向上しています。また、著者情報の更新も行われました。

# Insights
このコードの変更は、言語サービス、特に会話型言語理解に関するドキュメントの品質を向上させることを目的としています。具体的な変更箇所として、リンクテキストの修正やプロジェクト作成、スキーマ構築、さらにはLUISからCLUへの移行に関する手順の明確化が挙げられます。これにより、ユーザーは文書を通じてより正確に手順を理解し、スムーズにプロジェクトを進められるようになっています。

プロジェクト作成や削除、データラベリングのベストプラクティスについても、表現がより明確にされていて、ユーザーの操作が容易になるように最適化されています。また、REST APIに関連するすべての文書において、コード表記や文体の一貫性が確保され、技術文書としての信頼性が高まりました。

今回の変更で特に注目すべきは、著者の更新作業です。これは、新しい著者に文書の管理を移管することで、今後のメンテナンスやアップデートを一貫して行うための準備であると言えます。このように細部にわたる文書の改善と著者情報の更新を行うことで、全体としてのユーザーエクスペリエンスが向上し、ドキュメントの信頼性が強化されました。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [data-formats.md](#item-8559f6) | minor update | データフォーマットに関する文書の修正 | modified | 2 | 2 | 4 | 
| [build-schema.md](#item-623a8b) | minor update | 会話型言語理解プロジェクトスキーマの構築に関する文書の修正 | modified | 36 | 40 | 76 | 
| [create-project.md](#item-58b2dd) | minor update | 会話型言語理解プロジェクト作成に関する文書の修正 | modified | 25 | 28 | 53 | 
| [migrate-from-luis.md](#item-fdb6bf) | minor update | LUISからCLUへの移行文書の修正 | modified | 1 | 1 | 2 | 
| [tag-utterances.md](#item-3d1b2f) | minor update | 会話型言語理解における発話のタグ付けに関する文書の修正 | modified | 81 | 75 | 156 | 
| [label-data-best-practices.md](#item-f8f29d) | minor update | データラベリングのベストプラクティスに関する文書の修正 | modified | 3 | 3 | 6 | 
| [create-project.md](#item-0172b6) | minor update | 言語スタジオでのプロジェクト作成に関する文書の修正 | modified | 12 | 13 | 25 | 
| [delete-project.md](#item-01c6cb) | minor update | 言語スタジオでのプロジェクト削除手順の文言修正 | modified | 1 | 1 | 2 | 
| [project-details.md](#item-4baebc) | minor update | プロジェクト詳細の文書修正 | modified | 5 | 6 | 11 | 
| [sign-in-studio.md](#item-6f8bd7) | minor update | 言語スタジオへのサインイン手順の文言修正 | modified | 3 | 3 | 6 | 
| [resource-creation-azure-portal.md](#item-0d0001) | minor update | Azureポータルでのリソース作成手順の文言修正 | modified | 6 | 6 | 12 | 
| [resource-creation-language-studio.md](#item-7527a9) | minor update | Language Studioからのリソース作成手順の文言修正 | modified | 9 | 12 | 21 | 
| [create-project.md](#item-ffc2cd) | minor update | プロジェクト作成APIリクエストの文言修正 | modified | 10 | 11 | 21 | 
| [delete-project.md](#item-a99e1e) | minor update | プロジェクト削除APIリクエストの文言修正 | modified | 5 | 6 | 11 | 
| [export-project.md](#item-3e1856) | minor update | プロジェクトエクスポートAPIリクエストの文言修正 | modified | 7 | 10 | 17 | 
| [import-project.md](#item-6d0c87) | minor update | プロジェクトインポートAPIリクエストの文言修正 | modified | 13 | 13 | 26 | 
| [project-details.md](#item-308330) | minor update | プロジェクト詳細取得APIリクエストの文言修正 | modified | 7 | 7 | 14 | 
| [create-project.md](#item-915621) | minor update | カスタム命名エンティティ認識プロジェクト作成APIの文言修正 | modified | 15 | 17 | 32 | 
| [smart-url-refresh.md](#item-d248fb) | minor update | 著者情報の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/language-service/conversational-language-understanding/concepts/data-formats.md{#item-8559f6}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ If you're uploading your data into conversational language understanding, it mus
 
 ## Import project file format
 
-If you're [importing a project](../how-to/create-project.md#import-project) into conversational language understanding, the file uploaded must be in the following format:
+If you're [importing a project](../how-to/create-project.md#import-a-project) into conversational language understanding, the file uploaded must be in the following format:
 
 ```json
 {
@@ -175,5 +175,5 @@ Conversational language understanding offers the option to upload your utterance
 
 ## Related content
 
-* For more information on importing your labeled data into your project directly, see [Import project](../how-to/create-project.md#import-project).
+* For more information on importing your labeled data into your project directly, see [Import project](../how-to/create-project.md#import-a-project).
 * For more information about labeling your data, see [Label your utterances in Language Studio](../how-to/tag-utterances.md). After you label your data, you can [train your model](../how-to/train-model.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データフォーマットに関する文書の修正"
}
```

### Explanation
この変更は、会話型言語理解に関連するデータフォーマットに関する文書でのマイナーな更新です。具体的には、プロジェクトをインポートする際のリンクテキストが修正されました。以前は「import-project」となっていたものが「import-a-project」に変更され、関連する情報セクションでのリンクも同様に修正されています。この更新により、読みやすさと一貫性が向上しています。ファイル内の関連コンテンツリンクに対しても同じ修正が行われ、同じリンクの更新が反映されています。全体として、わずかではありますが、文書の正確性が改善されました。

## articles/ai-services/language-service/conversational-language-understanding/how-to/build-schema.md{#item-623a8b}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: How to build a Conversational Language Understanding project schema
+title: Build a Conversational Language Understanding Project Schema
 titleSuffix: Azure AI services
-description: Use this article to start building a Conversational Language Understanding project schema
+description: Use this article to start building a conversational language understanding project schema.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
@@ -11,25 +11,24 @@ ms.author: lajanuar
 ms.custom: language-service-clu
 ---
 
-# How to build your fine-tuning schema
+# Build your fine-tuning schema
 
-In conversational language understanding projects, the *schema* is defined as the combination of intents and entities within your project. Schema design is a crucial part of your project's success. When creating a schema, think about which intents and entities should be included in your project.
+In conversational language understanding projects, the *schema* is defined as the combination of intents and entities within your project. Schema design is a crucial part of your project's success. When you create a schema, think about which intents and entities should be included in your project.
 
 ## Guidelines and recommendations
 
-Consider the following guidelines when picking intents for your project:
+Consider the following guidelines when you choose intents for your project:
 
-  1. Create distinct, separable intents. An intent is best described as action the user wants to perform. Think of the project you're building and identify all the different actions your users may take when interacting with your project. Sending, calling, and canceling are all actions that are best represented as different intents. "Canceling an order" and "canceling an appointment" are similar, with the distinction being *what* they're canceling. Those two actions should be represented under the same intent, *Cancel*.
+  - **Create distinct, separable intents.** An intent is best described as action that the user wants to perform. Think of the project you're building and identify all the different actions that your users might take when they interact with your project. Sending, calling, and canceling are all actions that are best represented as different intents. "Canceling an order" and "canceling an appointment" are similar, with the distinction being *what* they're canceling. Those two actions should be represented under the same intent, *cancel*.
+  - **Create entities to extract relevant pieces of information within your text.** The entities should be used to capture the relevant information that's needed to fulfill your user's action. For example, *order* or *appointment* could be different things that a user is trying to cancel, and you should create an entity to capture that piece of information.
 
-  1. Create entities to extract relevant pieces of information within your text. The entities should be used to capture the relevant information needed to fulfill your user's action. For example, *order* or *appointment* could be different things a user is trying to cancel, and you should create an entity to capture that piece of information.
+You can "send a message," "send an email," or "send a package." Creating an intent to capture each of those requirements won't scale over time, and you should use entities to identify *what* the user was sending. The combination of intents and entities should determine your conversation flow.
 
-You can *"send"* a *message*, *"send"* an *email*, or *"send"* a package. Creating an intent to capture each of those requirements won't scale over time, and you should use entities to identify *what* the user was sending. The combination of intents and entities should determine your conversation flow.
+For example, consider a company where the bot developers identified the three most common actions that their users take when they use a calendar:
 
-For example, consider a company where the bot developers identified the three most common actions their users take when using a calendar:
-
-* Setup new meetings
-* Respond to meeting requests
-* Cancel meetings
+* Set up new meetings.
+* Respond to meeting requests.
+* Cancel meetings.
 
 They might create an intent to represent each of these actions. They might also include entities to help complete these actions, such as:
 
@@ -41,61 +40,58 @@ They might create an intent to represent each of these actions. They might also
 
 To build a project schema within [AI Foundry](https://ai.azure.com/?cid=learnDocs):
 
-1. Select **Define schema** from the left side menu.
-
-1. From the top pivots, you can change the view to be **Intents** or **Entities**.
+1. On the left pane, select **Define schema**.
 
-1. To create an intent, select **+ Add intent**. You're prompted to type in names and descriptions for as many intents as you'd like to create. Descriptions are only required for using Quick Deploy to help Azure OpenAI better understand the context of your intents.
+1. Select the **Intents** or **Entities** tabs.
 
-1. Repeat the steps to develop intents that encompass all the actions the user is likely to perform while interacting with the project.
+1. To create an intent, select **+ Add intent**. You're prompted to enter names and descriptions for as many intents as you want to create. Descriptions are required only for using the **Quick Deploy** option to help Azure OpenAI better understand the context of your intents.
 
+1. Repeat the steps to develop intents that encompass all the actions that the user is likely to perform while interacting with the project.
 
+    :::image type="content" source="../media/build-schema-page.png" alt-text="A screenshot that shows the schema creation page for conversation projects in Language Studio." lightbox="../media/build-schema-page.png":::
 
-    :::image type="content" source="../media/build-schema-page.png" alt-text="A screenshot showing the schema creation page for conversation projects in Language Studio." lightbox="../media/build-schema-page.png":::
-
-1. If you'd like to continue with [data labeling](tag-utterances.md) and advanced training a custom `CLU` model, you can select **Manage data** from the left side menu to add examples for intents and label them with entities, if desired.
+1. If you want to continue with [data labeling](tag-utterances.md) and advanced training a custom `CLU` model, on the left pane, select **Manage data** to add examples for intents and label them with entities, if desired.
 
 ## Add entities
 
-1. Move to **Entities** pivot from the top of the page.
+1. Select the **Entities** tab.
 
-1. To add an entity, select **+ Add entity** from the top. You're prompted to type in a name to create the entity.
+1. To add an entity, select **+ Add entity**. You're prompted to enter a name to create the entity.
 
-1. After creating an entity, you can select the entity name to change the **Entity components** type. Multiple components—learned, list, regex, or prebuilt—define every entity. A learned component is added to all your entities once you label them in your utterances.
+1. After you create an entity, you can select the entity name to change the **Entity components** type. Multiple components like learned, list, regex, or prebuilt are used to define every entity. A learned component is added to all your entities after you label them in your utterances.
 
-   :::image type="content" source="../media/entity-details.png" alt-text="A screenshot showing the entity details page for conversation projects in Language Studio." lightbox="../media/entity-details.png":::
+   :::image type="content" source="../media/entity-details.png" alt-text="A screenshot that shows the Entity components page for conversation projects in Language Studio." lightbox="../media/entity-details.png":::
 
 1. You can also add a [list](../concepts/entity-components.md#list-component), [regex](../concepts/entity-components.md#regex-component), or [prebuilt](../concepts/entity-components.md#prebuilt-component) component to each entity.
 
-### Add prebuilt component
+### Add a prebuilt component
 
-To add a **prebuilt** component, select the prebuilt type from the drop-down menu in the Entity options section.
+To add a prebuilt component, select the prebuilt type from the dropdown menu in the **Entity options** section.
 
-   <!--:::image type="content" source="../media/add-prebuilt-component.png" alt-text="A screenshot showing a prebuilt-component in Language Studio." lightbox="../media/add-prebuilt-component.png":::-->
+   <!--:::image type="content" source="../media/add-prebuilt-component.png" alt-text="A screenshot that shows a prebuilt component in Language Studio." lightbox="../media/add-prebuilt-component.png":::-->
 
-### Add list component
+### Add a list component
 
-To add a **list** component, select **Add list**. You can add multiple lists to each entity:
+To add a list component, select **Add list**. You can add multiple lists to each entity:
 
-1. Create a new list, in the *List key* text box, enter the normalized value that is returned when any of the synonyms values is extracted.
+1. Create a new list, and in the **List key** text box, enter the normalized value that was returned when any of the synonyms values were extracted.
 
-1. Start typing in your synonyms and hit enter after each one. We recommend having a synonym list in multiple languages.
+1. Enter your synonyms and select Enter after each one. We recommend having a synonym list in multiple languages.
 
-   <!--:::image type="content" source="../media/add-list-component.png" alt-text="A screenshot showing a list component in Language Studio." lightbox="../media/add-list-component.png":::-->
+   <!--:::image type="content" source="../media/add-list-component.png" alt-text="A screenshot that shows a list component in Language Studio." lightbox="../media/add-list-component.png":::-->
 
-### Add regex component
+### Add a regex component
 
-To add a regex component, select Add expression. Name the regex key and type a regular expression that matches the entity to be extracted.
+To add a regex component, select **Add expression**. Name the regex key, and enter a regular expression that matches the entity to be extracted.
 
 ### Define entity options
 
-Change to the **Entity options** pivot in the entity details page. When multiple components are defined for an entity, their predictions may overlap. When an overlap occurs, each entity's final prediction is determined based on the [entity option](../concepts/entity-components.md#entity-options) you select in this step. Select the one that you want to apply to this entity and select the **Save** button.
-
-   <!--:::image type="content" source="../media/entity-options.png" alt-text="A screenshot showing an entity option in Language Studio." lightbox="../media/entity-options.png":::-->
+Select the **Entity Options** tab on the entity details page. When multiple components are defined for an entity, their predictions might overlap. When an overlap occurs, each entity's final prediction is determined based on the [entity option](../concepts/entity-components.md#entity-options) that you select in this step. Select the option that you want to apply to this entity, and then select **Save**.
 
+   <!--:::image type="content" source="../media/entity-options.png" alt-text="A screenshot that shows an entity option in Language Studio." lightbox="../media/entity-options.png":::-->
 
-After you create your entities, you can come back and edit them. You can **edit entity components** or **delete** them by selecting this option from the top menu.
+After you create your entities, you can come back and edit them. You can edit entity components or delete them by selecting **Edit** or **Delete**.
 
-## Next Steps
+## Related content
 
 * [Add utterances and label your data](tag-utterances.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話型言語理解プロジェクトスキーマの構築に関する文書の修正"
}
```

### Explanation
この変更では、「会話型言語理解プロジェクトスキーマの構築」に関する文書に大幅な更新が加えられました。主な変更点は、タイトルや説明文の文言を改良し、文全体の表現をより明確にした点です。具体的には、タイトルを「How to build a Conversational Language Understanding project schema」から「Build a Conversational Language Understanding Project Schema」に変更し、説明文の内容も少し修正しました。

さらに、スキーマ設計のガイドラインとして述べられていた点が箇条書き形式に分けられ、可読性が向上するとともに、重要な情報が強調されました。また、手順の説明も一部改善され、利用者にとってより理解しやすくなっています。

加えて、ビジュアル要素や各ステップの説明が明確にされ、具体的な操作手順がわかりやすくなっています。この更新により、文書の一貫性と有用性が向上しました。全体として、内容が整理され、多くの文法上の修正が行われたことで、読者により良い体験を提供することを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/create-project.md{#item-58b2dd}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: How to create projects in Conversational Language Understanding
+title: Create Projects in Conversational Language Understanding
 titleSuffix: Azure AI services
-description: Use this article to learn how to create projects in Conversational Language Understanding.
+description: This article shows you how to create projects in conversational language understanding (CLU).
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
@@ -11,36 +11,33 @@ ms.author: lajanuar
 ms.custom: language-service-clu
 ---
 
-# How to create a CLU fine-tuning task
+# Create a CLU fine-tuning task
 
-Use this article to learn how to set up these requirements and create a project. 
+Use this article to learn how to set up these requirements and create a project.
 
 ## Prerequisites
 
-Before you start using CLU, you will need a few items:
+* An Azure subscription. If you don't have one, you can [create one for free](https://azure.microsoft.com/free/cognitive-services).
+* An Azure AI Language resource.
 
-* An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services).
-* An Azure AI Language resource 
+### Create a Language resource
 
-### Create a Language resource 
-
-Before you start using CLU, you will need an Azure AI Language resource.
+Before you start using conversational language understanding (CLU), you need an Azure AI Language resource.
 
 > [!NOTE]
->  * You need to have an **owner** role assigned on the resource group to create a Language resource.
+> You need to have an Owner role assigned for the resource group to create a Language resource.
 
 [!INCLUDE [create a new resource from the Azure portal](../includes/resource-creation-azure-portal.md)]
 
 [!INCLUDE [create a new resource from Language Studio](../includes/resource-creation-language-studio.md)]
 
-
 ## Sign in to Language Studio
 
 [!INCLUDE [Sign in to Language studio](../includes/language-studio/sign-in-studio.md)]
 
 ## Create a conversation project
 
-Once you have a Language resource created, create a Conversational Language Understanding project. 
+After you create a Language resource, create a CLU project.
 
 ### [Azure AI Foundry](#tab/azure-ai-foundry)
 
@@ -52,39 +49,39 @@ Once you have a Language resource created, create a Conversational Language Unde
 
 ---
 
-## Import project
+## Import a project
 
 ### [Azure AI Foundry](#tab/azure-ai-foundry)
 
-You can export a Conversational Language Understanding project as a JSON file at any time by going to the conversation projects page, selecting a project, and from the top menu, clicking on **Export**.
+You can export a CLU project as a JSON file at any time. On the conversation projects page, select a project, and on the top menu, select **Export**.
 
-:::image type="content" source="../media/export.png" alt-text="A screenshot showing the Conversational Language Understanding export button." lightbox="../media/export.png":::
+:::image type="content" source="../media/export.png" alt-text="A screenshot that shows the CLU Export button." lightbox="../media/export.png":::
 
-That project can be reimported as a new project. If you import a project with the exact same name, it replaces the project's data with the newly imported project's data.
+You can reimport that project as a new project. If you import a project with the exact same name, it replaces the project's data with the newly imported project's data.
 
-If you have an existing LUIS application, you can _import_ the LUIS application JSON to Conversational Language Understanding directly, and it will create a Conversation project with all the pieces that are currently available: Intents, ML entities, and utterances. See [the LUIS migration article](../how-to/migrate-from-luis.md) for more information.
+If you have an existing Language Understanding (LUIS) application, you can _import_ the LUIS application JSON to CLU directly. It creates a Conversation project with all the pieces that are currently available: intents, machine learning entities, and utterances. For more information, see [Migrate from Language Understanding (LUIS) to conversational language understanding (CLU)](../how-to/migrate-from-luis.md).
 
-To import a project, select the arrow button next to **Create a new project** and select **Import**, then select the LUIS or Conversational Language Understanding JSON file.
+To import a project, select the arrow button next to **Create a new project** and select **Import**. Then select the LUIS or CLU JSON file.
 
-:::image type="content" source="../media/import.png" alt-text="A screenshot showing the Conversational Language Understanding import button." lightbox="../media/import.png":::
+:::image type="content" source="../media/import.png" alt-text="A screenshot that shows the CLU Import button." lightbox="../media/import.png":::
 
 ### [REST APIs](#tab/rest-api)
 
-You can import a CLU JSON into the service
+You can import a CLU JSON into the service.
 
 [!INCLUDE [Import project](../includes/rest-api/import-project.md)]
 
 ---
 
-## Export project
+## Export a project
 
 ### [Azure AI Foundry](#tab/azure-ai-foundry)
 
-You can export a Conversational Language Understanding project as a JSON file at any time by going to the conversation projects page, selecting a project, and pressing **Export**.
+You can export a CLU project as a JSON file at any time. On the conversation projects page, select a project, and then select **Export**.
 
 ### [REST APIs](#tab/rest-api)
 
-You can export a Conversational Language Understanding project as a JSON file at any time.
+You can export a CLU project as a JSON file at any time.
 
 [!INCLUDE [Export project](../includes/rest-api/export-project.md)]
 
@@ -102,20 +99,20 @@ You can export a Conversational Language Understanding project as a JSON file at
 
 ---
 
-## Delete project 
+## Delete a project
 
 ### [Azure AI Foundry](#tab/azure-ai-foundry)
 
 [!INCLUDE [Delete project](../includes/language-studio/delete-project.md)]
 
 ### [REST APIs](#tab/rest-api)
 
-When you don't need your project anymore, you can delete your project using the APIs.
+When you don't need your project anymore, you can use the APIs to delete your project.
 
 [!INCLUDE [Delete project](../includes/rest-api/delete-project.md)]
 
 ---
 
-## Next Steps
+## Related content
 
-[Build schema](./build-schema.md)
+- [Build schema](./build-schema.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話型言語理解プロジェクト作成に関する文書の修正"
}
```

### Explanation
本変更は、会話型言語理解（CLU）プロジェクトの作成に関する文書におけるマイナーな更新です。主に文言の改善が行われ、タイトルの変更や説明文の明確化を通じて、より直感的で分かりやすい表現が採用されています。

文書の中で、プロジェクトに関する手順や要件が整理され、重要なポイントが強調されました。例えば、「CLTファインチューニングタスクの作成」というセクションが、「CLUファインチューニングタスクの作成」にリネームされ、より明確に意図が伝わるようになりました。

また、Azure リソースの作成に関する説明が簡素化され、文法の修正や不必要な冗長性が排除されています。これにより、読者が手順を追いやすくなり、プロジェクト作成の流れが改善されています。全体として、内容が一貫性を持ち、ユーザーにとっての有用性が増しています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/migrate-from-luis.md{#item-fdb6bf}

<details>
<summary>Diff</summary>
````diff
@@ -41,7 +41,7 @@ The following table presents a side-by-side comparison between the features of L
 |Intents and utterances| Intents and utterances |All intents and utterances are transferred. Utterances are labeled with their transferred entities. |
 |Application GUIDs |Project names| A project is created for each migrating application with the application name. Any special characters in the application names are removed in CLU.|
 |Versioning| Every time you train, a model is created and acts as a version of your [project](#how-do-i-manage-versions-in-clu). | A project is created for the selected application version. |
-|Evaluation using batch testing |Evaluation using testing sets | [Adding your testing dataset](../how-to/tag-utterances.md#how-to-label-your-utterances) is required.|  
+|Evaluation using batch testing |Evaluation using testing sets | [Adding your testing dataset](../how-to/tag-utterances.md#label-your-utterances) is required.|  
 |Role-Based Access Control (RBAC) for LUIS resources |Role-Based Access Control (RBAC) available for Language resources |Language resource RBAC must be [manually added after migration](../../concepts/role-based-access-control.md). |
 |Single training mode| Standard and advanced [training modes](#how-are-the-training-times-different-in-clu-how-is-standard-training-different-from-advanced-training) | Training is required after application migration. |
 |Two publishing slots and version publishing |Ten deployment slots with custom naming | Deployment is required after the application’s migration and training. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "LUISからCLUへの移行文書の修正"
}
```

### Explanation
この変更では、LUISから会話型言語理解（CLU）への移行に関する文書において、細かい更新が行われました。具体的には、テーブル内の情報が修正され、一貫性を持たせるためにリンクの表現がわずかに調整されています。

変更された内容では、評価に関する部分でのリンクテキストが、「how-to-label-your-utterances」から「label-your-utterances」に変更されました。この修正により、読者は追加のテストデータセットのラベル付け方法へ容易にアクセスできるようになっています。また、全体としては、この変更は文書の明瞭さを高め、LUISからCLUへスムーズに移行できるような情報提供を目的としています。

これにより、利用者は必要な情報に迅速にアクセスでき、全体の利便性が向上しています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/tag-utterances.md{#item-3d1b2f}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: How to tag utterances in Conversational Language Understanding
+title: Tag Utterances in Conversational Language Understanding
 titleSuffix: Azure AI services
-description: Use this article to tag your utterances in Conversational Language Understanding projects
+description: This article shows you how to tag your utterances in conversational language understanding projects.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
@@ -11,152 +11,158 @@ ms.author: lajanuar
 ms.custom: language-service-clu
 ---
 
-# Label your utterances in AI Foundry
+# Label your utterances in Azure AI Foundry
 
-Once you [build a schema](build-schema.md) for your fine-tuning task, you should add training utterances to your project. The utterances should be similar to what your users use when interacting with the project. When you add an utterance, you have to assign which intent it belongs to. After the utterance is added, label the words within your utterance that you want to extract as entities.
+After you [build a schema](build-schema.md) for your fine-tuning task, you add training utterances to your project. The utterances should be similar to what your users use when they interact with the project. When you add an utterance, you have to assign which intent it belongs to. After the utterance is added, label the words within your utterance that you want to extract as entities.
 
-Data labeling is a crucial step in the conversational language understanding `CLU` trained development lifecycle; this data are used in the next step when training your model so that your model can learn from the labeled data. If you already labeled utterances, you can directly [import it into your project](create-project.md#import-project), IF your data follows the [accepted data format](../concepts/data-formats.md). See [create fine-tuning task](create-project.md#import-project) to learn more about importing labeled data. Labeled data informs the model how to interpret text and is used for training and evaluation.
+Data labeling is a crucial step in the conversational language understanding (CLU) trained development lifecycle. This data is used in the next step when you train your model so that your model can learn from the labeled data. If you already labeled utterances, you can directly [import them into your project](create-project.md#import-a-project), if your data follows the [accepted data format](../concepts/data-formats.md). To learn more about importing labeled data, see [Create a CLU fine-tuning task](create-project.md#import-a-project). Labeled data informs the model about how to interpret text and is used for training and evaluation.
 
-   > [!TIP]
-  > Use the `Quick Deploy` option to implement custom `CLU` intent routing, powered by your own `LLM` model deployment without adding or labeling any training data.
+> [!TIP]
+> Use the **Quick Deploy** option to implement custom CLU intent routing, which is powered by your own large language model deployment without adding or labeling any training data.
 
 ## Prerequisites
 
-Before you can label your data, you need:
-
 * A successfully [created project](create-project.md).
 
-For more information, see the [conversational language understanding development lifecycle](../overview.md#project-development-lifecycle).
+For more information, see the [CLU development lifecycle](../overview.md#project-development-lifecycle).
 
 ## Data labeling guidelines
 
-After [building your schema](build-schema.md) and [creating your project](create-project.md), you need to label your data. Labeling your data is important so your model knows which sentences and words are associated with the intents and entities in your project. Spend time labeling your utterances - introducing and refining the data that is used in training your models.
+After you [build your schema](build-schema.md) and [create your project](create-project.md), you need to label your data. Labeling your data is important so that your model knows which sentences and words are associated with the intents and entities in your project. Spend time labeling your utterances to introduce and refine the data that's used in training your models.
 
 As you add utterances and label them, keep in mind:
 
-* The machine learning models generalize based on the labeled examples you provide it; the more examples you provide, the more data points the model has to make better generalizations.
-
-* The precision, consistency, and completeness of your labeled data are key factors to determining model performance.
+* The machine learning models generalize based on the labeled examples that you provide. The more examples that you provide, the more data points the model has to make better generalizations.
+* The precision, consistency, and completeness of your labeled data are key factors to determining model performance:
 
-    * **Label precisely**: Label each intent and entity to its right type always. Only include what you want classified and extracted, avoid unnecessary data in your labels.
-    * **Label consistently**:  The same entity should have the same label across all the utterances.
-    * **Label completely**: Provide varied utterances for every intent. Label all the instances of the entity in all your utterances.
+    * **Label precisely:** Label each intent and entity to its right type always. Only include what you want classified and extracted. Avoid unnecessary data in your labels.
+    * **Label consistently:** The same entity should have the same label across all the utterances.
+    * **Label completely:** Provide varied utterances for every intent. Label all the instances of the entity in all your utterances.
 
 [!INCLUDE [Label data best practices](../includes/label-data-best-practices.md)]
 
-* For [Multilingual projects](../language-support.md#multi-lingual-option), adding utterances in other languages increases the model's performance in these languages, but avoid duplicating your data across all the languages you would like to support. For example, to improve a calender bot's performance with users, a developer might add examples mostly in English, and a few in Spanish or French as well. They might add utterances such as:
+* For [multilingual projects](../language-support.md#multi-lingual-option), adding utterances in other languages increases the model's performance in these languages. Avoid duplicating your data across all the languages that you want to support. For example, to improve a calender bot's performance with users, a developer might add examples mostly in English and a few in Spanish or French. They might add utterances such as:
 
-  * "_Set a meeting with **Matt** and **Kevin** **tomorrow** at **12 PM**._" (English)
-  * "_Reply as **tentative** to the **weekly update** meeting._" (English)
-  * "_Cancelar mi **próxima** reunión_." (Spanish)
+  * "Set a meeting with **Matt** and **Kevin** **tomorrow** at **12 PM**." (English)
+  * "Reply as **tentative** to the **weekly update** meeting." (English)
+  * "Cancelar mi **próxima** reunión." (Spanish)
 
-## How to label your utterances
+## Label your utterances
 
 Use the following steps to label your utterances:
 
-1. Go to your project page in [AI Foundry](https://ai.azure.com/?cid=learnDocs).
+1. Go to your project page in [Azure AI Foundry](https://ai.azure.com/?cid=learnDocs).
 
-1. From the left side menu, select `Manage data`. In this page, you can start adding your utterances and labeling them. You can also upload your utterances directly by clicking on `Upload utterance file` from the top menu. Make sure it follows the [accepted format](../concepts/data-formats.md#utterance-file-format).
+1. On the left pane, select **Manage data**. On this page, you can add your utterances and label them. You can also upload your utterances directly by selecting **Upload utterance file** from the top menu. Make sure to follow the [accepted format](../concepts/data-formats.md#utterance-file-format).
 
-1. From the top pivots, you can change the view to be `training set` or `testing set`. Learn more about [training and testing sets](train-model.md#data-splitting) and how they're used for model training and evaluation.
+1. By using the top tabs, you can change the view to **Training set** or **Testing set**. Learn more about [training and testing sets](train-model.md#data-splitting) and how they're used for model training and evaluation.
 
-    :::image type="content" source="../media/tag-utterances.png" alt-text="A screenshot of the page for tagging utterances in Language Studio." lightbox="../media/tag-utterances.png":::
+    :::image type="content" source="../media/tag-utterances.png" alt-text="A screenshot that shows the page for tagging utterances in Language Studio." lightbox="../media/tag-utterances.png":::
 
     > [!TIP]
-    > If you're planning on using `Automatically split the testing set from training data` splitting, add all your utterances to the training set.
-
+    > If you plan to use **Automatically split the testing set from training data** splitting, add all your utterances to the training set.
 
-1.  From the `Select intent` dropdown menu, select one of the intents, the language of the utterance (for multilingual projects), and the utterance itself. Press enter key in the utterance's text box and add the utterance.
+1. From the **Select intent** dropdown menu, select one of the intents, the language of the utterance (for multilingual projects), and the utterance itself. Press the Enter key in the utterance's text box and add the utterance.
 
 1. You have two options to label entities in an utterance:
 
     |Option |Description  |
     |---------|---------|
-    |Label using a brush     | Select the brush icon next to an entity in the right pane, then highlight the text in the utterance you want to label.           |
-    |Label using inline menu     | Highlight the word you want to label as an entity, and a menu appears. Select the entity you want to label these words with. |
+    |Label by using a brush     | Select the brush icon next to an entity in the pane on the right, and then highlight the text in the utterance that you want to label.           |
+    |Label by using inline menu     | Highlight the word that you want to label as an entity, and a menu appears. Select the entity that you want to label these words with. |
 
-1. In the right side pane, under the `Labels` pivot, you can find all the entity types in your project and the count of labeled instances per each.
+1. In the pane on the right, on the **Labels** tab, you can find all the entity types in your project and the count of labeled instances per each one.
 
-1. Under the `Distribution` pivot, you can view the distribution across training and testing sets. You have two options for viewing:
-    * *Total instances per labeled entity* where you can view count of all labeled instances of a specific entity.
-    * *Unique utterances per labeled entity* where each utterance is counted if it contains at least one labeled instance of this entity.
-    * *Utterances per intent* where you can view count of utterances per intent.
-
-    :::image type="content" source="../media/label-distribution.png" alt-text="A screenshot showing entity distribution in Language Studio." lightbox="../media/label-distribution.png":::
+1. On the **Distribution** tab, you can view the distribution across training and testing sets. You have these options for viewing:
+    * **Total instances per labeled entity:** You can view the count of all labeled instances of a specific entity.
+    * **Unique utterances per labeled entity:** Each utterance is counted if it contains at least one labeled instance of this entity.
+    * **Utterances per intent:** You can view the count of utterances per intent.
 
+    :::image type="content" source="../media/label-distribution.png" alt-text="A screenshot that shows entity distribution in Language Studio." lightbox="../media/label-distribution.png":::
 
   > [!NOTE]
-  > List, regex, and prebuilt components aren't shown in the data labeling page, and all labels here only apply to the **learned component**.
+  > List, regex, and prebuilt components aren't shown on the data labeling page. All labels here apply to the learned component only.
 
 To remove a label:
-  1. From within your utterance, select the entity you want to remove a label from.
+
+  1. From within your utterance, select the entity from which you want to remove a label.
   1. Scroll through the menu that appears, and select **Remove label**.
 
 To delete an entity:
-  1. Select the garbage bin icon next to the entity you want to edit in the right side pane. Then select **Delete** to confirm.
+
+  1. Select the garbage bin icon next to the entity that you want to edit in the pane on the right.
+  1. Select **Delete** to confirm.
 
 ## Suggest utterances with Azure OpenAI
 
-In `CLU`, use Azure OpenAI to suggest utterances to add to your project using generative language models. We recommended that you use an AI Foundry resource while using `CLU`, so you don't need to connect multiple resources. In order to use the AI Foundry resource, you need to provide your AI Foundry resource with elevated access. To do so, access the Azure portal. Within your Azure AI resource, provide access as a *Cognitive Services User* to itself. This step ensures that all parts of your resource are communicating correctly.
+In CLU, use Azure OpenAI to suggest utterances to add to your project by using generative language models. We recommend that you use an Azure AI Foundry resource while you use CLU so that you don't need to connect multiple resources. 
 
-### Connect with separate Language and Azure OpenAI Resources
+To use the Azure AI Foundry resource, you need to provide your Azure AI Foundry resource with elevated access. To do so, access the Azure portal. Within your Azure AI resource, provide access as a **Cognitive Services User** to itself. This step ensures that all parts of your resource are communicating correctly.
 
-You first need to get access and create a resource in Azure OpenAI. Next, create a connection to the Azure OpenAI resource within the same AI Foundry project in the `Management center` in the left panel of the Azure AI Foundry page. You then need to create a deployment for the AOAI models within the connected AOAI resource. Follow the prerequisite steps [here](../../../openai/how-to/create-resource.md) to create a new resource.
+### Connect with separate Language and Azure OpenAI resources
+
+You first need to get access and create a resource in Azure OpenAI. Next, create a connection to the Azure OpenAI resource within the same Azure AI Foundry project in the **Management center** on the left pane of the Azure AI Foundry page. You then need to create a deployment for the Azure OpenAI models within the connected Azure OpenAI resource. To create a new resource, follow the steps in [Create and deploy an Azure OpenAI in Azure AI Foundry Models resource](../../../openai/how-to/create-resource.md).
+
+Before you get started, the suggested utterances feature is available only if your Language resource is in the following regions:
 
-Before you get started, the suggested utterances feature is only available if your Language resource is in the following regions:
 * East US
 * South Central US
 * West Europe
 
-In the Data Labeling page:
+On the **Data labeling** page:
+
+1. Select **Suggest utterances**. A pane opens on the right and prompts you to select your Azure OpenAI resource and deployment.
+1. After you select an Azure OpenAI resource, select **Connect** so that your Language resource has direct access to your Azure OpenAI resource. It assigns your Language resource the **Cognitive Services User** role to your Azure OpenAI resource. Now your current Language resource has access to Azure OpenAI. If the connection fails, follow [these steps](#add-required-configurations-to-azure-openai-resource) to manually add the correct role to your Azure OpenAI resource.
+1. After the resource is connected, select the deployment. The model that we recommend for the Azure OpenAI deployment is `gpt-35-turbo-instruct`.
+1. Select the intent for which you want to get suggestions. Make sure the intent that you selected has at least five saved utterances to be enabled for utterance suggestions. The suggestions provided by Azure OpenAI are based on the most recent utterances that you added for that intent.
+1. Select **Generate utterances**.
 
-1. Select the `Suggest utterances` button. A pane opens up on the right side prompting you to select your Azure OpenAI resource and deployment.
-1. On selection of an Azure OpenAI resource, select `Connect`, which allows your Language resource to have direct access to your Azure OpenAI resource. It assigns your Language resource the role of `Cognitive Services User` to your Azure OpenAI resource, which allows your current Language resource to have access to Azure OpenAI's service. If the connection fails, the following [steps](#add-required-configurations-to-azure-openai-resource) enable you to manually add the correct role to your Azure OpenAI resource.
-1. Once the resource is connected, select the deployment. The recommended model for the Azure OpenAI deployment is `gpt-35-turbo-instruct`.
-1. Select the intent you'd like to get suggestions for. Make sure the intent you selected has at least five saved utterances to be enabled for utterance suggestions. The suggestions provided by Azure OpenAI are based on the `most recent utterances` you added for that intent.
-1. Select `Generate utterances`. Once complete, the suggested utterances  show up with a dotted line around it, with the note *Generated by AI*. Those suggestions need to be accepted or rejected. Accepting a suggestion simply adds it to your project, as if you had added it yourself. Rejecting it deletes the suggestion entirely. Only accepted utterances are part of your project and used for training or testing. You can accept or reject by clicking on the green check or red cancel buttons beside each utterance. You can also use the `Accept all` and `Reject all` buttons in the toolbar.
+   The suggested utterances show up with a dotted line around them and the note **Generated by AI**. Those suggestions must be accepted or rejected. Accepting a suggestion adds it to your project, as if you had added it yourself. Rejecting a suggestion deletes it entirely. Only accepted utterances are part of your project and used for training or testing.
 
-    :::image type="content" source="../media/suggest-utterances.png" alt-text="A screenshot showing suggested utterances." lightbox="../media/suggest-utterances.png":::
+    To accept or reject, select the green check mark or red cancel buttons beside each utterance. You can also use **Accept all** and **Reject all** on the toolbar.
 
-Using this feature entails a charge to your Azure OpenAI resource for a similar number of tokens to the suggested utterances generated. Details for Azure OpenAI's pricing can be found [here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/).
+    :::image type="content" source="../media/suggest-utterances.png" alt-text="A screenshot that shows suggested utterances." lightbox="../media/suggest-utterances.png":::
+
+Use of this feature entails a charge to your Azure OpenAI resource for a similar number of tokens to the suggested utterances that are generated. For information on Azure OpenAI pricing, see [Azure OpenAI Service pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/).
 
 ### Add required configurations to Azure OpenAI resource
 
-Enable identity management for your Language resource using the following options:
+Enable identity management for your Language resource by using the following options.
 
 #### [Azure portal](#tab/portal)
 
-Your Language resource must have identity management, to enable it using the [Azure portal](https://portal.azure.com):
+Your Language resource must have identity management. To enable it by using the [Azure portal](https://portal.azure.com):
 
 1. Go to your Language resource.
-1. From left hand menu, under `Resource Management` section, select `Identity`.
-1. From `System assigned` tab, make sure to set `Status` to `On`.
+1. On the left pane, under the **Resource Management** section, select **Identity**.
+1. On the **System assigned** tab, set **Status** to **On**.
 
 #### [Language Studio](#tab/studio)
 
-Your Language resource must have identity management, to enable it using [Language Studio](https://aka.ms/languageStudio):
+Your Language resource must have identity management. To enable it by using [Language Studio](https://aka.ms/languageStudio):
 
-1. Select the settings icon in the top right corner of the screen.
-1. Select *`Resources`.
-1. Select the check box `Managed Identity` for your Language resource.
+1. Select the settings icon in the upper-right corner of the screen.
+1. Select **Resources**.
+1. Select the **Managed Identity** check box for your Language resource.
 
 ---
 
-After enabling managed identity, assign the role `Cognitive Services User` to your Azure OpenAI resource using the managed identity of your Language resource.
+After you enable managed identity, assign the **Cognitive Services User** role to your Azure OpenAI resource by using the managed identity of your Language resource.
+
+  1. Sign in to the [Azure portal](https://portal.azure.com) and go to your Azure OpenAI resource.
+  1. Select the **Access Control (IAM)** tab.
+  1. Select **Add** > **Add role assignment**.
+  1. Select **Job function roles** and select **Next**.
+  1. Select **Cognitive Services User** from the list of roles, and select **Next**.
+  1. Select **Assign access to: Managed identity** and choose **Select members**.
+  1. Under **Managed identity**, select **Language**.
+  1. Search for your resource and select it. Then select **Next** and complete the process.
+  1. Review the details and select **Review + assign**.
 
-  1. Sign in to the [Azure portal](https://portal.azure.com) and navigate to your Azure OpenAI resource.
-  1. Select the `Access Control (IAM)` tab.
-  1. Select `Add` > Add role assignment.
-  1. Select `Job function roles` and select `Next`.
-  1. Select `Cognitive Services User` from the list of roles and select `Next`.
-  1. Select Assign access to "Managed identity" and select `Select members`.
-  1. Under `Managed identity` select `Language`.
-  1. Search for your resource and select it. Then select `Next` and complete the process.
-  1. Review the details and select `Review + Assign`.
+     :::image type="content" source="../media/add-role-azure-openai.gif" alt-text="Multiple screenshots that show the steps to add the required role to your Azure OpenAI resource." lightbox="../media/add-role-azure-openai.gif":::
 
-     :::image type="content" source="../media/add-role-azure-openai.gif" alt-text="Multiple screenshots showing the steps to add the required role to your Azure OpenAI resource." lightbox="../media/add-role-azure-openai.gif":::
+After a few minutes, refresh Azure AI Foundry, and you can successfully connect to Azure OpenAI.
 
-After a few minutes, refresh the AI Foundry, and you can successfully connect to Azure OpenAI.
+## Related content
 
-## Next Steps
-* [Train Model](./train-model.md)
+* [Train your conversational language understanding model](./train-model.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話型言語理解における発話のタグ付けに関する文書の修正"
}
```

### Explanation
この変更は、会話型言語理解（CLU）プロジェクトにおける発話のタグ付けに関する文書の更新を反映しています。主な変更点は、文言の改善や整合性の確保、内容の明確化です。具体的には、各セクションでの用語の統一や文章構造の見直しが行われ、読者が手順を追いやすくなっています。

文書のタイトルが「How to tag utterances in Conversational Language Understanding」から「Tag Utterances in Conversational Language Understanding」に変更され、よりダイレクトな表現となっています。また、内容の一部では、説明文がより詳細で明確になり、特にデータラベリングに関する重要なポイントが強調されています。例えば、データラベリングのプロセスや、意図とエンティティを関連付ける際の指針が具体的に示されています。

さらに、Azure OpenAIとの連携や、そのための設定手順も詳細に説明され、ユーザーが必要なリソースや手続きを理解しやすくなっています。全体として、これらの変更は文書の有用性を高め、ユーザーの理解を助けることを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/includes/label-data-best-practices.md{#item-f8f29d}

<details>
<summary>Diff</summary>
````diff
@@ -9,10 +9,10 @@ ms.author: lajanuar
 
 ## Clearly label utterances 
 
-* Ensure that the concepts that your entities refer to are well defined and separable. Check if you can easily determine the differences reliably. If you can't, this lack of distinction might indicate that the learned component will also have difficulty.
-* If there's a similarity between entities, ensure that there's some aspect of your data that provides a signal for the difference between them.
+* Ensure that the concepts that your entities refer to are well defined and separable. Check if you can easily determine the differences reliably. If you can't, this lack of distinction might indicate difficulty for the learned component.
+* Ensure that some aspect of your data can provide a signal for differences when there's a similarity between entities.
 
     For example, if you built a model to book flights, a user might use an utterance like "I want a flight from Boston to Seattle." The *origin city* and *destination city* for such utterances would be expected to be similar. A signal to differentiate *origin city* might be that the word *from* often precedes it.
 
 * Ensure that you label all instances of each entity in both your training and testing data. One approach is to use the search function to find all instances of a word or phrase in your data to check if they're correctly labeled.
-* Label test data for entities that have no [learned component](../concepts/entity-components.md#learned-component) and also for the entities that do. This practice helps to ensure that your evaluation metrics are accurate.
\ No newline at end of file
+* Ensure that you label test data for entities without [learned components](../concepts/entity-components.md#learned-component) and also for the entities with them. This practice helps to ensure that your evaluation metrics are accurate.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データラベリングのベストプラクティスに関する文書の修正"
}
```

### Explanation
この変更では、会話型言語理解に関連するデータラベリングのベストプラクティスに関する文書が更新されました。主な変更点は、表現の明確化と冗長な文の削除です。

具体的には、エンティティが指す概念の定義や、類似エンティティ間の信号の説明が直感的で分かりやすい表現に改訂されました。例えば、エンティティの類似性がある場合は、それらの違いを提供するデータの側面が明確に示される必要があることが強調されています。

さらに、トレーニングデータやテストデータにおけるエンティティのすべてのインスタンスをラベリングする重要性も強調されています。これにより、学習コンポーネントが存在するエンティティと存在しないエンティティの両方の評価指標の正確性が確保されます。全体として、これらの修正は文書の明瞭さを高め、ユーザーが効果的にデータをラベリングできるよう支援することを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/create-project.md{#item-0172b6}

<details>
<summary>Diff</summary>
````diff
@@ -7,22 +7,21 @@ ms.date: 11/21/2024
 ms.author: lajanuar
 ---
 
-1. In [Language Studio](https://aka.ms/languageStudio), find the section named **Understand questions and conversational language** and select **Conversational language understanding**.  
-    :::image type="content" source="../../media/select-custom-clu.png" alt-text="A screenshot showing the location of Custom Language Understanding in the Language Studio landing page." lightbox="../../media/select-custom-clu.png"::: 
-    
+1. In [Language Studio](https://aka.ms/languageStudio), find the section named **Understand questions and conversational language** and select **Conversational Language Understanding**.
 
-2. This will bring you to the **Conversational language understanding projects** page. Select **Create new project**. 
+    :::image type="content" source="../../media/select-custom-clu.png" alt-text="A screenshot that shows the location of Custom Language Understanding on the Language Studio landing page." lightbox="../../media/select-custom-clu.png":::
 
-    :::image type="content" source="../../media/projects-page.png" alt-text="A screenshot showing the conversation project page in Language Studio." lightbox="../../media/projects-page.png":::
+1. When the **Conversational Language Understanding projects** page opens, select **Create new project**.
 
+    :::image type="content" source="../../media/projects-page.png" alt-text="A screenshot that shows the conversation project page in Language Studio." lightbox="../../media/projects-page.png":::
 
-To create a new project you need to provide the following details:
+1. To create a new project, provide the following information:
 
-|Value  | Description  |
-|---------|---------|
-|Name     | A name for your project. Once it's created, it can't be changed  |
-|Description    | Optional project description.        |
-|Utterances primary language     | The primary language of your project. Your training data should primarily be in this language.        |
-|Enable multiple languages    |  Whether you would like to enable your project to support [multiple languages](../../language-support.md#multi-lingual-option) at once.       |
+    |Value  | Description  |
+    |---------|---------|
+    |Name     | A name for your project. After you create it, the name can't be changed.  |
+    |Description    | Optional project description.        |
+    |Utterances primary language     | The primary language of your project. Your training data should primarily be in this language.        |
+    |Enable multiple languages    |  Whether you want to enable your project to support [multiple languages](../../language-support.md#multi-lingual-option) at once.       |
 
-Once you're done, select **Create**. You should now see the Getting started landing page in your project.
\ No newline at end of file
+1. After you finish, select **Create**. You should now see the **Getting started** landing page for your project.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語スタジオでのプロジェクト作成に関する文書の修正"
}
```

### Explanation
この変更は、言語スタジオにおけるプロジェクト作成に関する文書を更新し、手順をより明確にすることを目的としています。主な修正点は、手順の構造を整え、読みやすさを向上させるために文言を整理したことです。

具体的には、手順番号のフォーマットが統一され、各ステップの説明が簡潔で明確に提示されています。特に、プロジェクトの作成に必要な情報のリストが表形式に整理され、プロジェクト名や説明、主要言語、複数言語のサポートを有効にするかどうかについての説明が分かりやすく示されています。

また、手順終わりの文もリフレーズされ、「Getting started」ページが表示されることが明確に記述されています。これにより、ユーザーが言語スタジオでのプロジェクト作成の流れをよりスムーズに理解できるようになっています。全体として、これらの変更は文書の品質を向上させ、ユーザー体験を強化することを目指しています。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/delete-project.md{#item-01c6cb}

<details>
<summary>Diff</summary>
````diff
@@ -7,4 +7,4 @@ ms.date: 11/21/2024
 ms.author: lajanuar
 ---
 
-When you don't need your project anymore, you can delete your project using Language Studio. Select **Projects** from the left pane, select the project you want to delete, and then select **Delete** from the top menu.
+When you don't need your project anymore, you can use Language Studio to delete your project. On the left pane, select **Projects**, select the project that you want to delete, and then select **Delete** from the top menu.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語スタジオでのプロジェクト削除手順の文言修正"
}
```

### Explanation
この変更では、言語スタジオでのプロジェクト削除に関する手順の文言が改善されました。具体的には、手順の表現を若干修正し、より自然な流れで伝わるようにしています。

修正点としては、「Language Studioを使用してプロジェクトを削除する」との表現が導入され、手順の説明がより明確になりました。また、左のペインから「プロジェクト」を選択するという操作に関しても、文体が整えられています。

これにより、ユーザーが手順を理解しやすくなり、プロジェクト削除の際の操作がスムーズに行えることを目的としています。全体として、この変更は文書の可読性を向上させ、利用者にとっての使いやすさを強化しています。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/project-details.md{#item-4baebc}

<details>
<summary>Diff</summary>
````diff
@@ -8,13 +8,12 @@ ms.date: 11/21/2024
 ms.author: lajanuar
 ---
 
-1. Go to your project settings page in [Language Studio](https://aka.ms/languageStudio).
+1. Go to your **Project settings** page in [Language Studio](https://aka.ms/languageStudio).
 
-2. You can see project details.
+1. Review your project details.
 
-3. In this page you can update project description and enable/disable Multi-lingual dataset in project settings.
+1. On this page, you can update your project description and enable or disable **Multi-lingual dataset** in project settings.
 
-4. You can also retrieve your resource primary key from this page.
-
-    :::image type="content" source="../../media/project-details.png" alt-text="A screenshot of the project settings page." lightbox="../../media/project-details.png":::
+1. You can also retrieve your resource primary key from this page.
 
+    :::image type="content" source="../../media/project-details.png" alt-text="A screenshot that shows the Project settings page." lightbox="../../media/project-details.png":::
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト詳細の文書修正"
}
```

### Explanation
この変更は、言語スタジオのプロジェクト詳細に関する文書の内容を更新し、手順の表現を明確にすることを目的としています。具体的には、手順の番号付けが統一され、各ステップの文言が改善されました。

主な修正点は以下の通りです：
1. 「プロジェクト設定」ページに移動することが明示され、より具体的な指示が与えられています。
2. プロジェクトの詳細を確認する際の表現が「レビューする」に修正され、内容の確認が強調されています。
3. プロジェクト説明の更新や「多言語データセット」のオン/オフの設定についての説明が、より分かりやすい言い回しに整えられています。
4. スクリーンショットの説明文も、一貫した表現に改められています。

これにより、ユーザーがプロジェクト設定を適切に管理できるようになり、手順の理解が容易になります。全体として、この修正は文書の可読性を向上させ、ユーザー体験を強化することを目指しています。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/sign-in-studio.md{#item-6f8bd7}

<details>
<summary>Diff</summary>
````diff
@@ -9,14 +9,14 @@ ms.author: lajanuar
 
 1. Go to the [Language Studio](https://aka.ms/languageStudio) and sign in with your Azure account. 
 
-2. In the **Choose a language resource** window that appears, find your Azure subscription, and choose your Language resource. If you don't have a resource, you can create a new one.
+1. In the **Choose a language resource** window that appears, find your Azure subscription, and choose your Language resource. If you don't have a resource, you can create a new one.
 
     |Instance detail  |Required value  |
     |---------|---------|
     |Azure subscription | Your Azure subscription.           |
     |Azure resource group | Your Azure resource group name. |
     |Azure resource name |  Your Azure resource name.        |
-    |Location | One of the [supported regions](../../service-limits.md#regional-availability) for your Language resource. For example "West US 2".     |
+    |Location | One of the [supported regions](../../service-limits.md#regional-availability) for your Language resource. An example is West US 2.     |
     |Pricing tier     | One of the valid [pricing tiers](../../service-limits.md#language-resource-limits) for your Language resource. You can use the Free (F0) tier to try the service.  |
     
-    :::image type="content" source="../../media/quickstart-language-resource.png" alt-text="A screenshot showing the resource selection screen in Language Studio." lightbox="../../media/quickstart-language-resource.png":::
+    :::image type="content" source="../../media/quickstart-language-resource.png" alt-text="A screenshot that shows the resource selection screen in Language Studio." lightbox="../../media/quickstart-language-resource.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語スタジオへのサインイン手順の文言修正"
}
```

### Explanation
この変更は、言語スタジオへのサインイン手順に関連する文書の表現を改善することを目的としています。具体的には、手順の番号付けの修正や、いくつかの文言の調整が行われました。

主な修正内容は次の通りです：
1. 最初の手順番号がされています。これにより、手順がより明確に呼び出されるようになっています。
2. 「Location」に関する説明文が若干の言い回しの変更が加えられ、例えばが具体的に「West US 2」として提示されています。
3. スクリーンショットの説明文も、もう少し具体的であるかのように修正されています。

これらの修正により、ユーザーは言語スタジオにアクセスする際の手順をより正確に理解できるようになり、実際の操作が円滑に進められることを目的としています。また、全体として文書の可読性が向上し、利用者の体験が強化されることにもつながっています。

## articles/ai-services/language-service/conversational-language-understanding/includes/resource-creation-azure-portal.md{#item-0d0001}

<details>
<summary>Diff</summary>
````diff
@@ -9,18 +9,18 @@ ms.author: lajanuar
 
 ### Create a new resource from the Azure portal
 
-1. Sign in to the [Azure portal](https://portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics) to create a new Azure AI Language resource. 
+1. Sign in to the [Azure portal](https://portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics) to create a new Azure AI Language resource.
 
-2. Select **Create a new resource**
+1. Select **Create a new resource**.
 
-3. In the window that appears, search for **Language service**  
+1. In the window that appears, search for **Language service**.
 
-4. Select **Create** 
+1. Select **Create**.
 
-5. Create a Language resource with following details.
+1. Create a Language resource with the following information:
 
     |Instance detail  |Required value  |
     |---------|---------|
     |Region | One of the [supported regions](../service-limits.md#regional-availability) for your Language resource.          |
-    |Name| Required name for your Language resource|
+    |Name| Required name for your Language resource.|
     |Pricing tier     | One of the [supported pricing tiers](../service-limits.md#language-resource-limits) for your Language resource.       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureポータルでのリソース作成手順の文言修正"
}
```

### Explanation
この変更は、Azureポータルを使用した新しいリソースの作成手順に関する文書の内容を改善するために行われました。文言の明確化と一貫性を図るために、手順説明に関していくつかの調整が施されています。

主な修正内容は以下の通りです：
1. 手順の番号付けが一貫性を持たせるために変更され、全ての手順に明確な句点が追加されました。
2. 「Create a Language resource with following details.」が「Create a Language resource with the following information:」に修正され、より正確な表現が使用されています。
3. 表内のフィールドにおいて、「Required name for your Language resource」が「Required name for your Language resource.」に修正され、文法的に整合性が取れています。

これらの改善を通じて、ユーザーがAzureポータルでのリソース作成手順をより容易に理解し、正確に実行できるようにすることを目指しています。全体として、文書の可読性が向上し、ユーザー体験の向上に寄与するものとなっています。

## articles/ai-services/language-service/conversational-language-understanding/includes/resource-creation-language-studio.md{#item-7527a9}

<details>
<summary>Diff</summary>
````diff
@@ -11,21 +11,18 @@ ms.author: lajanuar
 
 ### Create a new Language resource from Language Studio
 
-If it's your first time logging in, you'll see a window in [Language Studio](https://aka.ms/languageStudio) that will let you choose an existing Language resource or create a new one. You can also create a resource by clicking the settings icon in the top-right corner, selecting **Resources**, then clicking **Create a new resource**.
+If it's your first time to sign in, you see a window in [Language Studio](https://aka.ms/languageStudio) that you can use to choose an existing Language resource or create a new one. You can also create a resource by selecting the settings icon in the upper-right corner, selecting **Resources**, and then selecting **Create a new resource**.
 
-Create a Language resource with following details.
+Create a Language resource with the following information:
 
 |Instance detail  |Required value  |
 |---------|---------|
-|Azure subscription| Your Azure subscription|
-|Azure resource group| Your Azure resource group|
-|Azure resource name| Your Language resource name|
-|Location | A [supported regions](../service-limits.md#regional-availability) for your Language resource.        |
-|Pricing tier     | A [supported pricing tiers](../service-limits.md#language-resource-limits) for your Language resource.        |
+|Azure subscription| Your Azure subscription.|
+|Azure resource group| Your Azure resource group.|
+|Azure resource name| Your Language resource name.|
+|Location | [Supported regions](../service-limits.md#regional-availability) for your Language resource.        |
+|Pricing tier     | [Supported pricing tiers](../service-limits.md#language-resource-limits) for your Language resource.        |
 
 > [!IMPORTANT]
-> * Make sure to enable **Managed Identity** when you create a Language resource. 
-> * Read and confirm Responsible AI notice
-
-
-
+> - Make sure to enable managed identity when you create a Language resource.
+> - Read and confirm the Responsible AI notice.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Language Studioからのリソース作成手順の文言修正"
}
```

### Explanation
この変更は、Language Studioから新しい言語リソースを作成する手順に関する文書に加えられた改善を反映しています。文言の明確化や一貫性を高めるために、いくつかの表現の調整がなされました。

主な修正内容は以下の通りです：
1. ユーザーが初めてサインインする際の表現がより明確になり、「first time logging in」から「first time to sign in」へ変更されています。これにより、ユーザーに対する指示が明瞭になります。
2. 「Create a Language resource with following details.」が「Create a Language resource with the following information:」に修正され、より正確な表現が用いられています。
3. 表内の各項目に対して、文末に句点が追加され、統一された形式が維持されています。
4. 注意事項の書き方も、リスト形式に統一され、より読みやすくなりました。

これらの変更により、ユーザーはLanguage Studioを使用して言語リソースを作成する際の手順をより分かりやすく理解できるようになり、その結果、実際の操作が円滑に進むことが期待されます。全体として、文書の可読性とユーザー体験の向上が図られています。

## articles/ai-services/language-service/conversational-language-understanding/includes/rest-api/create-project.md{#item-ffc2cd}

<details>
<summary>Diff</summary>
````diff
@@ -7,30 +7,30 @@ ms.date: 11/21/2024
 ms.author: lajanuar
 ---
 
-Submit a **PATCH** request using the following URL, headers, and JSON body to create a new project.
+Submit a `PATCH` request by using the following URL, headers, and JSON body to create a new project.
 
 ### Request URL
 
-Use the following URL when creating your API request. Replace the placeholder values below with your own values. 
+Use the following URL when you create your API request. Replace the placeholder values with your own values.
 
 ```rest
 {ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}?api-version={API-VERSION}
 ```
 
 |Placeholder  |Value  | Example |
 |---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `myProject` |
-|`{API-VERSION}`     | The [version](../../../concepts/model-lifecycle.md#api-versions) of the API you are calling. | `2023-04-01` |
+|`{ENDPOINT}`     | The endpoint for authenticating your API request. | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
+|`{PROJECT-NAME}`     | The name for your project. This value is case sensitive. | `myProject` |
+|`{API-VERSION}`     | The [version](../../../concepts/model-lifecycle.md#api-versions) of the API you're calling. | `2023-04-01` |
 
 ### Headers
 
-Use the following header to authenticate your request. 
+Use the following header to authenticate your request.
 
 |Key|Value|
 |--|--|
 |`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-|`Content-Type`| 'application/merge-patch+json' |
+|`Content-Type`| `application/merge-patch+json` |
 
 ### Body
 
@@ -48,7 +48,6 @@ Use the following sample JSON as your body.
 
 |Key  |Placeholder  |Value  | Example |
 |---------|---------|----------|--|
-| `projectName` | `{PROJECT-NAME}` | The name of your project. This value is case-sensitive. | `EmailApp` |
-| `language` | `{LANGUAGE-CODE}` |  A string specifying the language code for the utterances used in your project. If your project is a multilingual project, choose the [language code](../../language-support.md) of the majority of the utterances. |`en-us`|
-| `multilingual` | `true`| A boolean value that enables you to have documents in multiple languages in your dataset and when your model is deployed you can query the model in any supported language (not necessarily included in your training documents). See [Language support](../../language-support.md#multi-lingual-option) to learn more about multilingual support.  | `true`|
-
+| `projectName` | `{PROJECT-NAME}` | The name of your project. This value is case sensitive. | `EmailApp` |
+| `language` | `{LANGUAGE-CODE}` | A string that specifies the language code for the utterances used in your project. If your project is a multilingual project, choose the [language code](../../language-support.md) of most of the utterances. |`en-us`|
+| `multilingual` | `true`| A Boolean value that enables you to have documents in multiple languages in your dataset. When your model is deployed, you can query the model in any supported language (not necessarily included in your training documents). To learn more about multilingual support, see [Language support](../../language-support.md#multi-lingual-option). | `true`|
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト作成APIリクエストの文言修正"
}
```

### Explanation
この変更は、言語サービスのREST APIを利用して新しいプロジェクトを作成する際の手順に関する文書の見直しを反映しています。特に、文法や表現の明確化が行われ、利用しやすさが向上しています。

主な修正点は以下の通りです：
1. 用語の統一が図られ、「**PATCH**」が「`PATCH`」に修正され、コード要素がより明確に示されています。また、文中の「when creating your API request」が「when you create your API request」に変更され、表現の一貫性が強化されています。
2. プレースホルダーの説明において、「case-sensitive」が「case sensitive」という文言の修正や、それに伴う他の表現の調整が行われ、可読性が向上しています。
3. ボディのサンプルに関するセクションでは、用語が整合性のある形で修正され、情報がより簡潔に伝わるようになっています。
4. 不要な文言が削除され、情報がすっきりと整理されています。

これらの更新により、ユーザーはプロジェクトを作成するためのAPIリクエストをより理解しやすくなり、操作しやすくなっています。全体として、ドキュメントの体験が改善され、利便性が向上しています。

## articles/ai-services/language-service/conversational-language-understanding/includes/rest-api/delete-project.md{#item-a99e1e}

<details>
<summary>Diff</summary>
````diff
@@ -7,8 +7,7 @@ ms.date: 11/21/2024
 ms.author: lajanuar
 ---
 
-Create a **DELETE** request using the following URL, headers, and JSON body to delete a conversational language understanding project.
-
+Create a `DELETE` request by using the following URL, headers, and JSON body to delete a conversational language understanding project.
 
 ### Request URL
 
@@ -19,15 +18,15 @@ Create a **DELETE** request using the following URL, headers, and JSON body to d
 |Placeholder  |Value  | Example |
 |---------|---------|---------|
 |`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `myProject` |
-|`{API-VERSION}`     | The [version](../../../concepts/model-lifecycle.md#api-versions) of the API you are calling. | `2023-04-01` |
+|`{PROJECT-NAME}`     | The name for your project. This value is case sensitive.   | `myProject` |
+|`{API-VERSION}`     | The [version](../../../concepts/model-lifecycle.md#api-versions) of the API that you're calling. | `2023-04-01` |
 
 ### Headers
 
-Use the following header to authenticate your request. 
+Use the following header to authenticate your request.
 
 |Key|Value|
 |--|--|
 |`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
 
-Once you send your API request, you will receive a `202` response indicating success, which means your project has been deleted.
+After you send your API request, you receive a `202` response that indicates success, which means that your project was deleted.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト削除APIリクエストの文言修正"
}
```

### Explanation
この変更は、会話型言語理解プロジェクトを削除するためのREST APIリクエストに関する文書の微調整を反映しています。主に、用語の統一や表現の明確化が行われ、ドキュメントの可読性が向上しています。

主な修正点は以下の通りです：
1. 「**DELETE**」が「`DELETE`」に修正され、コード形式での表示に変更されました。この変更により、技術的なアプローチがより明確に示されています。
2. プレースホルダーの説明が一貫して修正され、「case-sensitive」が「case sensitive」に変更されるなど、文体の整合性が強化されています。
3. 「the API you are calling」が「the API that you're calling」に変更され、自然な英語表現に改善されています。
4. 成功応答に関する説明文が、「Once you send your API request, you will receive a `202` response indicating success, which means your project has been deleted.」から「After you send your API request, you receive a `202` response that indicates success, which means that your project was deleted.」に修正され、時制が統一され、より簡潔に表現されています。

これらの変更により、ユーザーはプロジェクトを削除するためのAPIリクエストの手続きをよりスムーズに理解できるようになり、全体的なユーザーエクスペリエンスが向上しています。

## articles/ai-services/language-service/conversational-language-understanding/includes/rest-api/export-project.md{#item-3e1856}

<details>
<summary>Diff</summary>
````diff
@@ -7,11 +7,11 @@ ms.date: 11/21/2024
 ms.author: lajanuar
 ---
 
-Create a **POST** request using the following URL, headers, and JSON body to export your project.
+Create a `POST` request by using the following URL, headers, and JSON body to export your project.
 
 ### Request URL
 
-Use the following URL when creating your API request. Replace the placeholder values below with your own values. 
+Use the following URL when you create your API request. Replace the placeholder values with your own values.
 
 ```rest
 {ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/:export?stringIndexType=Utf16CodeUnit&api-version={API-VERSION}
@@ -20,24 +20,21 @@ Use the following URL when creating your API request. Replace the placeholder va
 |Placeholder  |Value  | Example |
 |---------|---------|---------|
 |`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `EmailApp` |
-|`{API-VERSION}`     | The [version](../../../concepts/model-lifecycle.md#api-versions) of the API you are calling. | `2023-04-01` |
+|`{PROJECT-NAME}`     | The name for your project. This value is case sensitive.   | `EmailApp` |
+|`{API-VERSION}`     | The [version](../../../concepts/model-lifecycle.md#api-versions) of the API that you're calling. | `2023-04-01` |
 
 ### Headers
 
-Use the following header to authenticate your request. 
+Use the following header to authenticate your request.
 
 |Key|Value|
 |--|--|
 |`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
 
-
-Once you send your API request, you will receive a `202` response indicating success. In the response headers, extract the `operation-location` value. It will be formatted like this: 
+After you send your API request, you receive a `202` response that indicates success. In the response headers, extract the `operation-location` value. The value is formatted like this example:
 
 ```rest
 {ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/jobs/{JOB-ID}?api-version={API-VERSION}
 ``` 
 
-`JOB-ID` is used to identify your request, since this operation is asynchronous. Use this URL to get the exported project JSON, using the same authentication method.
-
-
+`JOB-ID` is used to identify your request because this operation is asynchronous. Use this URL to get the exported project JSON by using the same authentication method.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクトエクスポートAPIリクエストの文言修正"
}
```

### Explanation
この変更は、会話型言語理解プロジェクトをエクスポートするためのREST APIリクエストに関連する文書の更新を反映しています。具体的には、用語の変更や表現の明確化が行われ、ドキュメントの一貫性と可読性が向上しています。

主な修正点は以下の通りです：
1. 「**POST**」が「`POST`」に修正され、技術的な表現が明確になりました。
2. 「when creating your API request」が「when you create your API request」に変更され、文の流れが自然に改善されました。
3. プレースホルダーの説明において「case-sensitive」が「case sensitive」に直され、表現が統一されました。また、「the API you are calling」が「the API that you're calling」に修正され、一貫性が高まっています。
4. APIリクエストの結果としての成功応答の記述が「you will receive a `202` response indicating success.」から「you receive a `202` response that indicates success.」に改められ、簡潔で直訳から解放された表現になっています。
5. 引用のフォーマットについても、以前より明瞭になり、応答ヘッダー内の「operation-location」の値の抽出に関する説明が密接にリンクされる形で整備されました。

これらの変更により、ユーザーはプロジェクトをエクスポートするためのAPIリクエストの手続きをより理解しやすくなり、ドキュメントが全体的に使いやすくなっています。ユーザーエクスペリエンスが向上することで、より円滑な操作が可能になります。

## articles/ai-services/language-service/conversational-language-understanding/includes/rest-api/import-project.md{#item-6d0c87}

<details>
<summary>Diff</summary>
````diff
@@ -7,33 +7,33 @@ ms.date: 11/21/2024
 ms.author: lajanuar
 ---
 
-Submit a **POST** request using the following URL, headers, and JSON body to import your project.
+Submit a `POST` request by using the following URL, headers, and JSON body to import your project.
 
 ### Request URL
 
-Use the following URL when creating your API request. Replace the placeholder values with your own values. 
+Use the following URL when you create your API request. Replace the placeholder values with your own values.
 
 ```rest
 {ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/:import?api-version={API-VERSION}
 ```
 
 |Placeholder  |Value  | Example |
 |---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive, and must match the project name in the JSON file you're importing.   | `EmailAppDemo` |
-|`{API-VERSION}`     | The [version](../../../concepts/model-lifecycle.md#api-versions) of the API you're calling. | `2023-04-01` |
+|`{ENDPOINT}`     | The endpoint for authenticating your API request. | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
+|`{PROJECT-NAME}`     | The name for your project. This value is case sensitive and must match the project name in the JSON file that you're importing. | `EmailAppDemo` |
+|`{API-VERSION}`     | The [version](../../../concepts/model-lifecycle.md#api-versions) of the API that you're calling. | `2023-04-01` |
 
 ### Headers
 
-Use the following header to authenticate your request. 
+Use the following header to authenticate your request.
 
 |Key|Value|
 |--|--|
 |`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
 
 ### Body
 
-The JSON body you send is similar to the following example. See the [reference documentation](/rest/api/language/2023-04-01/conversational-analysis-authoring/import?tabs=HTTP#successful-import-project) for more details about the JSON object.
+The JSON body you send is similar to the following example. For more information about the JSON object, see the [reference documentation](/rest/api/language/2023-04-01/conversational-analysis-authoring/import?tabs=HTTP#successful-import-project).
 
 ```json
 {
@@ -92,13 +92,13 @@ The JSON body you send is similar to the following example. See the [reference d
 
 |Key  |Placeholder  |Value  | Example |
 |---------|---------|----------|--|
-|`{API-VERSION}`     | The [version](../../../concepts/model-lifecycle.md#api-versions) of the API you're calling. | `2023-04-01` |
-| `projectName` | `{PROJECT-NAME}` | The name of your project. This value is case-sensitive. | `EmailAppDemo` |
-| `language` | `{LANGUAGE-CODE}` |  A string specifying the language code for the utterances used in your project. If your project is a multilingual project, choose the [language code](../../language-support.md) of the majority of the utterances. |`en-us`|
-| `multilingual` | `true`| A boolean value that enables you to have documents in multiple languages in your dataset. When your model is deployed, you can query the model in any [supported language](../../language-support.md#multi-lingual-option) including languages that aren't included in your training documents.  | `true`|
-| `dataset` | `{DATASET}` |  See [how to train a model](../../how-to/tag-utterances.md) for information on splitting your data between a testing and training set. Possible values for this field are `Train` and `Test`.      |`Train`|
+|`{API-VERSION}`     | The [version](../../../concepts/model-lifecycle.md#api-versions) of the API that you're calling. | `2023-04-01` |
+| `projectName` | `{PROJECT-NAME}` | The name of your project. This value is case sensitive. | `EmailAppDemo` |
+| `language` | `{LANGUAGE-CODE}` |  A string that specifies the language code for the utterances used in your project. If your project is a multilingual project, choose the [language code](../../language-support.md) of most of the utterances. |`en-us`|
+| `multilingual` | `true`| A Boolean value that enables you to have documents in multiple languages in your dataset. When your model is deployed, you can query the model in any [supported language](../../language-support.md#multi-lingual-option), including languages that aren't included in your training documents. | `true`|
+| `dataset` | `{DATASET}` |  For information on how to split your data between a testing and training set, see [Label your utterances in AI Foundry](../../how-to/tag-utterances.md). Possible values for this field are `Train` and `Test`. |`Train`|
 
-Upon a successful request, the API response will contain an `operation-location` header with a URL you can use to check the status of the import job. It is formatted like this: 
+After a successful request, the API response contains an `operation-location` header with a URL that you can use to check the status of the import job. The header is formatted like this example:
 
 ```http
 {ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/import/jobs/{JOB-ID}?api-version={API-VERSION}
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクトインポートAPIリクエストの文言修正"
}
```

### Explanation
この変更は、会話型言語理解プロジェクトをインポートするためのREST APIリクエストに関する文書の更新を反映しています。主に、用語の明確化や文体の一貫性が向上しており、情報がよりわかりやすく整理されています。

主な修正点は以下の通りです：
1. 「**POST**」が「`POST`」に修正され、コード形式の表記に統一されました。
2. APIリクエストに関する記述が「when creating your API request」から「when you create your API request」に変更され、より自然な表現となっています。
3. プレースホルダーの説明で「case-sensitive」が「case sensitive」に修正され、表現の一貫性が増しました。また、APIのバージョンの引用でもより正確な表現が用いられています。
4. JSONボディの説明が「see the [reference documentation]」に対してより具体的に「For more information about the JSON object, see the [reference documentation]」に変更され、情報の探索がスムーズになります。
5. APIリクエスト成功時の応答について、「you will receive a `operation-location` header」から「the API response contains an `operation-location` header」に修正され、時制が統一されてより簡潔な表現になっています。

これらの変更により、ユーザーがプロジェクトをインポートするためのAPIリクエストの全体的な流れをよりスムーズに理解しやすくなり、ドキュメントが全体的に使いやすく整理されています。ユーザーエクスペリエンスの向上に寄与することが期待されます。

## articles/ai-services/language-service/conversational-language-understanding/includes/rest-api/project-details.md{#item-308330}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.author: lajanuar
 ---
 
 
-To get your project details, submit a **GET** request using the following URL and headers. Replace the placeholder values with your own values.   
+To get your project details, submit a `GET` request by using the following URL and headers. Replace the placeholder values with your own values.
 
 ```rest
 {ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}?api-version={API-VERSION}
@@ -18,20 +18,20 @@ To get your project details, submit a **GET** request using the following URL an
 |Placeholder  |Value  | Example |
 |---------|---------|---------|
 |`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.  | `myProject` |
-|`{API-VERSION}`     | The [version](../../../concepts/model-lifecycle.md#api-versions) of the API you are calling. | `2023-04-01` |
+|`{PROJECT-NAME}`     | The name for your project. This value is case sensitive.  | `myProject` |
+|`{API-VERSION}`     | The [version](../../../concepts/model-lifecycle.md#api-versions) of the API that you're calling. | `2023-04-01` |
 
 ### Headers
 
-Use the following header to authenticate your request. 
+Use the following header to authenticate your request.
 
 |Key|Value|
 |--|--|
 |`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
 
-### Response Body
+### Response body
 
-Once you send the request, you will get the following response.
+After you send the request, you get the following response:
 
 ```json
 {
@@ -47,4 +47,4 @@ Once you send the request, you will get the following response.
 }
 ```
 
-Once you send your API request, you will receive a `200` response indicating success and JSON response body with your project details.
+After you send your API request, you receive a `200` response that indicates success and includes a JSON response body with your project details.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト詳細取得APIリクエストの文言修正"
}
```

### Explanation
この変更は、会話型言語理解プロジェクトに関するプロジェクト詳細を取得するためのREST APIリクエストに関連する文書の更新を反映しています。具体的には、表現の明確化や一貫性の向上が行われています。

主な修正点は以下の通りです：
1. 「**GET**」が「`GET`」に修正され、コード形式の表記に統一されています。
2. 文の構造が改善され、「submit a **GET** request using the following URL and headers」から「submit a `GET` request by using the following URL and headers」に変更され、より自然な流れになりました。
3. プレースホルダーの説明において、「case-sensitive」が「case sensitive」に修正され、用語の一貫性が強調されています。また、APIのバージョンに関する表現もやや改善され、正確性が増しています。
4. レスポンスボディのセクションタイトルが「Response Body」から「Response body」に変更され、よりスタイルガイドに準拠した表現となっています。
5. APIリクエスト成功時の説明が「you will get the following response」から「you get the following response」に修正され、動詞の活用が統一され、表現が簡潔になりました。

これらの変更により、ユーザーはプロジェクト詳細を取得するためのAPIリクエストの手続きに関する理解を深めることが可能になります。また、文書全体の明瞭さと使いやすさが向上し、ユーザーエクスペリエンスの改善が期待されます。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/rest-api/create-project.md{#item-915621}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.topic: include
 ms.date: 11/21/2024
 ms.author: lajanuar
 ---
-To start creating a custom named entity recognition model, you need to create a project. Creating a project will let you label data, train, evaluate, improve, and deploy your models.
+To start creating a custom named entity recognition model, you need to create a project. Creating a project lets you label data, train, evaluate, improve, and deploy your models.
 
 > [!NOTE]
 > The project name is case-sensitive for all operations.
@@ -15,7 +15,7 @@ Create a **PATCH** request using the following URL, headers, and JSON body to cr
 
 ### Request URL
 
-Use the following URL to create a project. Replace the placeholder values below with your own values. 
+Use the following URL to create a project. Replace the following placeholders with your own values. 
 
 ```rest
 {Endpoint}/language/authoring/analyze-text/projects/{projectName}?api-version={API-VERSION}
@@ -25,20 +25,21 @@ Use the following URL to create a project. Replace the placeholder values below
 |---------|---------|---------|
 |`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
 |`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `myProject` |
-|`{API-VERSION}`     | The version of the API you are calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
+|`{API-VERSION}`     | The version of the API you're calling. The value referenced is for the latest released version. For more information, see [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
 
 
-### Headers
+### Request headers
 
 Use the following header to authenticate your request. 
 
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
+|Key|Required|Type|Value|
+|--|--|--|--|
+|`Ocp-Apim-Subscription-Key`|True|string| The key to your resource. Used for authenticating your API requests.|
+|`Content-Type`|True|string|**application/merge-patch+json**|
 
-### Body
+### Request body
 
-Use the following JSON in your request. Replace the placeholder values below with your own values.
+Use the following JSON in your request. Replace the following placeholders with your own values.
 
 ```json
 {
@@ -55,17 +56,14 @@ Use the following JSON in your request. Replace the placeholder values below wit
 |Key  |Placeholder|Value  | Example |
 |---------|---------|---------|--|
 | projectName | `{PROJECT-NAME}` | The name of your project. This value is case-sensitive. | `myProject` |
-| language | `{LANGUAGE-CODE}` |  A string specifying the language code for the documents used in your project. If your project is a multilingual project, choose the language code of the majority of the documents. See [language support](../../language-support.md) to learn more about supported language codes. |`en-us`|
+| language | `{LANGUAGE-CODE}` |  A string specifying the language code for the documents used in your project. If your project is a multilingual project, select the code for the language most frequently represented in the documents. See [language support](../../language-support.md) to learn more about supported language codes. |`en-us`|
 | projectKind | `CustomEntityRecognition` | Your project kind. | `CustomEntityRecognition` |
-| multilingual | `true`| A boolean value that enables you to have documents in multiple languages in your dataset and when your model is deployed you can query the model in any supported language (not necessarily included in your training documents. See [language support](../../language-support.md#multi-lingual-option) to learn more about multilingual support.  | `true`|
-| storageInputContainerName | `{CONTAINER-NAME` | The name of your Azure storage container where you have uploaded your documents.   | `myContainer` |
+| multilingual | `true`| A boolean value that enables you to have documents in multiple languages in your dataset and when your model is deployed you can query the model in any supported language (not necessarily included in your training documents). See [language support](../../language-support.md#multi-lingual-option) to learn more about multilingual support. | `true`|
+| storageInputContainerName | `{CONTAINER-NAME` | The name of your Azure storage container your documents were uploaded.   | `myContainer` |
 
+This request returns a 201 response, which means that the project is created.
 
 
-
-This request will return a 201 response, which means that the project is created.
-
-
-This request will return an error if:
+This request returns an error if:
 * The selected resource doesn't have proper permission for the storage account. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム命名エンティティ認識プロジェクト作成APIの文言修正"
}
```

### Explanation
この変更は、カスタム命名エンティティ認識モデルを作成するためのプロジェクト作成に関連するREST APIリクエストに関する文書の更新を示しています。主に、表現の明確化や一貫性を目的とした修正が行われています。

主な修正点は以下のようになります：
1. 「Creating a project will let you label data, train, evaluate, improve, and deploy your models.」から「Creating a project lets you label data, train, evaluate, improve, and deploy your models.」へと修正され、文が簡潔かつ直接的になりました。
2. プレースホルダーの説明が「replace the placeholder values below with your own values.」から「replace the following placeholders with your own values.」に変更され、より自然な表現となっています。
3. APIバージョンの説明が改善され、「The value referenced here is for the latest version released.」から「The value referenced is for the latest released version.」に修正され、より流暢な英語表現になりました。
4. ヘッダー情報が「Headers」から「Request headers」に変更され、セクションタイトルがより明確に示されています。さらに、ヘッダーの構造が整えられ、必須項目や型情報が追加されています。
5. ボディのセクションタイトルが「Body」から「Request body」に変更され、より一貫したスタイルが保たれています。
6. レスポンスに関する説明が改善され、成功応答が得られることがより明確に示されています。また、エラーメッセージに関する言及が整理され、より分かりやすくなっています。

これらの変更により、ユーザーはカスタム命名エンティティ認識プロジェクトを作成するためのAPIリクエストに関する手順をより理解しやすくなり、全体的に文書の明瞭さが改善されることが期待されます。

## articles/ai-services/language-service/question-answering/how-to/smart-url-refresh.md{#item-d248fb}

<details>
<summary>Diff</summary>
````diff
@@ -3,8 +3,8 @@ title: Smart URL refresh - custom question answering
 titleSuffix: Azure AI services
 description: Use the custom question answering smart URL refresh feature to keep your project up to date.
 ms.service: azure-ai-language
-author: PatrickFarley
-ms.author: pafarley
+author: laujan
+ms.author: lajanuar
 ms.topic: how-to
 ms.date: 11/21/2024
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報の更新"
}
```

### Explanation
このコードの変更は、「スマートURLリフレッシュ」機能に関するドキュメントにおいて、著者情報を更新することを目的としています。具体的には、元の著者「PatrickFarley」から「lajan」に代わり、その関連情報「ms.author」も「pafarley」から「lajanuar」に変更されています。この修正は、文書の著作権や責任の所在を明確にするためによく行われるものであり、現在の著者に正確に反映されています。

全体として、この変更は2行の追加と2行の削除から成り、文書のタイトルや説明、サービス情報などの内容には影響を与えていません。これにより、読者は最新の著者情報に基づいてドキュメントを参照できるようになります。


