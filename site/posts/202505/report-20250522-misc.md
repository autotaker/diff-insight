---
date: '2025-05-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f021165...MicrosoftDocs:aedda49
summary: この更新では、ドキュメントインテリジェンスのサービス制限が拡大され、より大規模なデータセットに対応可能になりました。また、会話型言語理解に関するドキュメントの更新により、操作性が向上しています。新たに、ドキュメントインテリジェンスのトレーニング最大ページ数は10,000から25,000に、文書タイプは500から1000に増加しました。プラットフォーム名が「Language
  Studio」から「AI Foundry」に変更され、プロジェクトのスキーマ構築や発話のタグ付け手順も詳細に説明されています。これらの改善により、ユーザーの利便性が向上し、プロジェクトの精度向上が期待されます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f021165...MicrosoftDocs:aedda49){target="_blank"}

# ハイライト

ドキュメントインテリジェンスのサービス制限が更新され、より大規模なデータセットに対応できるようになりました。また、会話型言語理解に関連するドキュメントが更新され、スキーマ構築や発話のラベリング手順がより詳細に説明されています。これによりユーザーの操作性が向上し、プロジェクトの精度向上が期待されます。

## 新機能

- ドキュメントインテリジェンスのトレーニングにおける最大ページ数が10,000から25,000へ、文書タイプ（クラス）の数が500から1000へと増加しました。

## 破壊的変更

- なし

## その他の更新

- 会話型言語理解プロジェクトで使用されるプラットフォーム名が「Language Studio」から「AI Foundry」に変更されました。
- プロジェクトのスキーマ構築手順および発話のタグ付け手順が詳細に更新されました。

# インサイト

この更新は、主にAIサービスに対する機能の拡張と操作性の向上を目的としています。特にドキュメントインテリジェンスでは、トレーニングにおける最大ページ数とクラス数が増加したことで、大規模なデータセットに対応可能となり、より精緻なモデルの構築が可能です。これにより、ユーザーが抱える業務の多様性に対応しやすくなります。

一方で、会話型言語理解においては、プラットフォームの統一と操作手順の詳細化がされました。これにより、新旧のユーザーがサービスの使用方法において共通の理解を持つことができ、プロジェクトの開発時に迷うことが少なくなります。特に「AI Foundry」への変更は、プラットフォームの一貫性を持たせ、ユーザーにとってより直感的なインターフェースを提供するものと考えられます。

さらにプロジェクトのスキーマ構築や発話のラベリング手順が新たに詳細化されたことで、ユーザーはより明確なガイドラインに基づいて高品質なAIモデルを育成できるようになります。これらの変更は、システムの柔軟性を高めるだけでなく、プロジェクト全体の効率を向上させるための重要なステップといえます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [service-limits.md](#item-5ceae5) | minor update | ドキュメントインテリジェンスのサービス制限の更新 | modified | 2 | 2 | 4 | 
| [build-schema.md](#item-623a8b) | minor update | 会話型言語理解プロジェクトのスキーマ構築手順の更新 | modified | 40 | 36 | 76 | 
| [tag-utterances.md](#item-3d1b2f) | minor update | 会話型言語理解における発話のタグ付け手順の更新 | modified | 65 | 61 | 126 | 


# Modified Contents
## articles/ai-services/document-intelligence/service-limits.md{#item-5ceae5}

<details>
<summary>Diff</summary>
````diff
@@ -144,9 +144,9 @@ Document Intelligence billing is calculated monthly based on the model type and
 | Adjustable | No | No |
 | **Custom neural model train** | 10 hours per month <sup>5</sup> | no limit (pay by the hour), start with 10 free hours each month |
 | Adjustable | No |Yes <sup>3</sup>|
-| **Max number of pages (Training) * Classifier** | 10,000 | 10,000 (default value) |
+| **Max number of pages (Training) * Classifier** | 25,000 | 25,000 (default value) |
 | Adjustable | No | No |
-| **Max number of document types (classes) * Classifier** | 500 | 500 (default value) |
+| **Max number of document types (classes) * Classifier** | 1000 | 1000 (default value) |
 | Adjustable | No | No |
 | **Training dataset size * Classifier** | 1GB | 2GB (default value) |
 | Adjustable | No | No |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのサービス制限の更新"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスに関するサービス制限を更新するもので、いくつかのパラメータの上限値が引き上げられました。具体的には、トレーニング時の最大ページ数と文書タイプ（クラス）の数がそれぞれ10,000から25,000、500から1000に増加しました。この更新により、ユーザーはより大規模なデータセットを扱うことができ、文書分類の精度を向上させることが期待されます。全体として、これらの変更はユーザーがより柔軟にサービスを利用できるようにするためのものです。

## articles/ai-services/language-service/conversational-language-understanding/how-to/build-schema.md{#item-623a8b}

<details>
<summary>Diff</summary>
````diff
@@ -2,34 +2,34 @@
 title: How to build a Conversational Language Understanding project schema
 titleSuffix: Azure AI services
 description: Use this article to start building a Conversational Language Understanding project schema
-author: jboback
+author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
+ms.date: 05/20/2025
+ms.author: lajanuar
 ms.custom: language-service-clu
 ---
 
-# How to build your project schema
- 
-In conversational language understanding projects, the *schema* is defined as the combination of intents and entities within your project. Schema design is a crucial part of your project's success. When creating a schema, you want think about which intents and entities should be included in your project.
+# How to build your fine-tuning schema
+
+In conversational language understanding projects, the *schema* is defined as the combination of intents and entities within your project. Schema design is a crucial part of your project's success. When creating a schema, think about which intents and entities should be included in your project.
 
 ## Guidelines and recommendations
 
 Consider the following guidelines when picking intents for your project:
 
-  1. Create distinct, separable intents. An intent is best described as action the user wants to perform. Think of the project you're building and identify all the different actions your users may take when interacting with your project. Sending, calling, and canceling are all actions that are best represented as different intents. "Canceling an order" and "canceling an appointment" are very similar, with the distinction being *what* they are canceling. Those two actions should be represented under the same intent, *Cancel*.
-  
-  2. Create entities to extract relevant pieces of information within your text. The entities should be used to capture the relevant information needed to fulfill your user's action. For example, *order* or *appointment* could be different things a user is trying to cancel, and you should create an entity to capture that piece of information.
+  1. Create distinct, separable intents. An intent is best described as action the user wants to perform. Think of the project you're building and identify all the different actions your users may take when interacting with your project. Sending, calling, and canceling are all actions that are best represented as different intents. "Canceling an order" and "canceling an appointment" are similar, with the distinction being *what* they're canceling. Those two actions should be represented under the same intent, *Cancel*.
+
+  1. Create entities to extract relevant pieces of information within your text. The entities should be used to capture the relevant information needed to fulfill your user's action. For example, *order* or *appointment* could be different things a user is trying to cancel, and you should create an entity to capture that piece of information.
 
-You can *"send"* a *message*, *"send"* an *email*, or *"send"* a package. Creating an intent to capture each of those requirements will not scale over time, and you should use entities to identify *what* the user was sending. The combination of intents and entities should determine your conversation flow. 
+You can *"send"* a *message*, *"send"* an *email*, or *"send"* a package. Creating an intent to capture each of those requirements won't scale over time, and you should use entities to identify *what* the user was sending. The combination of intents and entities should determine your conversation flow.
 
-For example, consider a company where the bot developers have identified the three most common actions their users take when using a calendar: 
+For example, consider a company where the bot developers identified the three most common actions their users take when using a calendar:
 
-* Setup new meetings 
-* Respond to meeting requests 
-* Cancel meetings 
+* Setup new meetings
+* Respond to meeting requests
+* Cancel meetings
 
 They might create an intent to represent each of these actions. They might also include entities to help complete these actions, such as:
 
@@ -39,59 +39,63 @@ They might create an intent to represent each of these actions. They might also
 
 ## Add intents
 
-To build a project schema within [Language Studio](https://aka.ms/languageStudio):
+To build a project schema within [AI Foundry](https://ai.azure.com):
+
+1. Select **Define schema** from the left side menu.
 
-1. Select **Schema definition** from the left side menu.
+1. From the top pivots, you can change the view to be **Intents** or **Entities**.
 
-2. From the top pivots, you can change the view to be **Intents** or **Entities**.
+1. To create an intent, select **+ Add intent**. You're prompted to type in names and descriptions for as many intents as you'd like to create. Descriptions are only required for using Quick Deploy to help Azure OpenAI better understand the context of your intents.
+
+1. Repeat the steps to develop intents that encompass all the actions the user is likely to perform while interacting with the project.
 
-2. To create an intent, select **Add** from the top menu. You will be prompted to type in a name before completing creating the intent.
 
-3. Repeat the above step to create all the intents to capture all the actions that you think the user will want to perform while using the project.
 
     :::image type="content" source="../media/build-schema-page.png" alt-text="A screenshot showing the schema creation page for conversation projects in Language Studio." lightbox="../media/build-schema-page.png":::
 
-4. When you select the intent, you will be directed to the [Data labeling](tag-utterances.md) page,  with a filter set for the intent you selected. You can add examples for intents and label them with entities.
-    
+1. If you'd like to continue with [data labeling](tag-utterances.md) and advanced training a custom `CLU` model, you can select **Manage data** from the left side menu to add examples for intents and label them with entities, if desired.
+
 ## Add entities
 
 1. Move to **Entities** pivot from the top of the page.
 
-2. To add an entity, select **Add** from the top menu. You will be prompted to type in a name before completing creating the entity.
-
-3. After creating an entity, you'll be routed to the entity details page where you can define the composition settings for this entity.
+1. To add an entity, select **+ Add entity** from the top. You're prompted to type in a name to create the entity.
 
-4. Every entity can be defined by multiple components: learned, list or prebuilt. A learned component is added to all your entities once you label them in your utterances.
+1. After creating an entity, you can select the entity name to change the **Entity components** type. Multiple components—learned, list, regex, or prebuilt—define every entity. A learned component is added to all your entities once you label them in your utterances.
 
    :::image type="content" source="../media/entity-details.png" alt-text="A screenshot showing the entity details page for conversation projects in Language Studio." lightbox="../media/entity-details.png":::
-   
-5.You can add a [list](../concepts/entity-components.md#list-component) or [prebuilt](../concepts/entity-components.md#prebuilt-component) component to each entity. 
+
+1. You can also add a [list](../concepts/entity-components.md#list-component), [regex](../concepts/entity-components.md#regex-component), or [prebuilt](../concepts/entity-components.md#prebuilt-component) component to each entity.
 
 ### Add prebuilt component
 
-To add a **prebuilt** component, select **Add new prebuilt** and from the drop-down menu, select the prebuilt type to you want to add to this entity.
+To add a **prebuilt** component, select the prebuilt type from the drop-down menu in the Entity options section.
 
    <!--:::image type="content" source="../media/add-prebuilt-component.png" alt-text="A screenshot showing a prebuilt-component in Language Studio." lightbox="../media/add-prebuilt-component.png":::-->
-   
+
 ### Add list component
 
-To add a **list** component, select **Add new list**. You can add multiple lists to each entity.
+To add a **list** component, select **Add list**. You can add multiple lists to each entity:
 
-1. To create a new list, in the *Enter value* text box enter this is the normalized value that will be returned when any of the synonyms values is extracted.
+1. Create a new list, in the *List key* text box, enter the normalized value that is returned when any of the synonyms values is extracted.
 
-2. From the *language* drop-down menu, select the language of the synonyms list and start typing in your synonyms and hit enter after each one. It is recommended to have synonyms lists in multiple languages.
+1. Start typing in your synonyms and hit enter after each one. We recommend having a synonym list in multiple languages.
 
    <!--:::image type="content" source="../media/add-list-component.png" alt-text="A screenshot showing a list component in Language Studio." lightbox="../media/add-list-component.png":::-->
-   
+
+### Add regex component
+
+To add a regex component, select Add expression. Name the regex key and type a regular expression that matches the entity to be extracted.
+
 ### Define entity options
 
-Change to the **Entity options** pivot in the entity details page. When multiple components are defined for an entity, their predictions may overlap. When an overlap occurs, each entity's final prediction is determined based on the [entity option](../concepts/entity-components.md#entity-options) you select in this step. Select the one that you want to apply to this entity and select the **Save** button at the top.
+Change to the **Entity options** pivot in the entity details page. When multiple components are defined for an entity, their predictions may overlap. When an overlap occurs, each entity's final prediction is determined based on the [entity option](../concepts/entity-components.md#entity-options) you select in this step. Select the one that you want to apply to this entity and select the **Save** button.
 
    <!--:::image type="content" source="../media/entity-options.png" alt-text="A screenshot showing an entity option in Language Studio." lightbox="../media/entity-options.png":::-->
 
 
-After you create your entities, you can come back and edit them. You can **Edit entity components** or **delete** them by selecting this option from the top menu.
- 
+After you create your entities, you can come back and edit them. You can **edit entity components** or **delete** them by selecting this option from the top menu.
+
 ## Next Steps
 
 * [Add utterances and label your data](tag-utterances.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話型言語理解プロジェクトのスキーマ構築手順の更新"
}
```

### Explanation
この変更は、会話型言語理解プロジェクトに関するスキーマ構築手順を更新したもので、記事の内容が強化されています。具体的には、著者名の変更、日付の更新、セクションタイトルの修正、新しい情報の追加が含まれています。

新たに「微調整スキーマを構築する方法」というタイトルが追加され、プロジェクトのスキーマの定義に関する説明やガイドラインが明確にされています。また、プロジェクトを構築するために必要な手順が整理され、ユーザーは「AI Foundry」の機能を通じてスキーマを定義できるように指示されています。さらに、エンティティのコンポーネントに関する情報が豊富になり、正規表現を用いたコンポーネントの追加方法が新たに説明されています。

これらの変更により、ユーザーは会話型言語理解プロジェクトのスキーマ構築に関して、より分かりやすく、具体的な手順を理解できるようになります。

## articles/ai-services/language-service/conversational-language-understanding/how-to/tag-utterances.md{#item-3d1b2f}

<details>
<summary>Diff</summary>
````diff
@@ -2,38 +2,41 @@
 title: How to tag utterances in Conversational Language Understanding
 titleSuffix: Azure AI services
 description: Use this article to tag your utterances in Conversational Language Understanding projects
-author: jboback
+author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
+ms.date: 05/20/2025
+ms.author: lajanuar
 ms.custom: language-service-clu
 ---
 
-# Label your utterances in Language Studio
+# Label your utterances in AI Foundry
 
-Once you have [built a schema](build-schema.md) for your project, you should add training utterances to your project. The utterances should be similar to what your users use when interacting with the project. When you add an utterance, you have to assign which intent it belongs to. After the utterance is added, label the words within your utterance that you want to extract as entities. 
+Once you [build a schema](build-schema.md) for your fine-tuning task, you should add training utterances to your project. The utterances should be similar to what your users use when interacting with the project. When you add an utterance, you have to assign which intent it belongs to. After the utterance is added, label the words within your utterance that you want to extract as entities.
 
-Data labeling is a crucial step in development lifecycle; this data are used in the next step when training your model so that your model can learn from the labeled data. If you already have labeled utterances, you can directly [import it into your project](create-project.md#import-project), but you need to make sure that your data follows the [accepted data format](../concepts/data-formats.md). See [create project](create-project.md#import-project) to learn more about importing labeled data into your project. Labeled data informs the model how to interpret text, and is used for training and evaluation.
+Data labeling is a crucial step in the conversational language understanding `CLU` trained development lifecycle; this data are used in the next step when training your model so that your model can learn from the labeled data. If you already labeled utterances, you can directly [import it into your project](create-project.md#import-project), IF your data follows the [accepted data format](../concepts/data-formats.md). See [create fine-tuning task](create-project.md#import-project) to learn more about importing labeled data. Labeled data informs the model how to interpret text and is used for training and evaluation.
+
+   > [!TIP]
+  > Use the `Quick Deploy` option to implement custom `CLU` intent routing, powered by your own `LLM` model deployment without adding or labeling any training data.
 
 ## Prerequisites
 
 Before you can label your data, you need:
 
 * A successfully [created project](create-project.md).
 
-See the [project development lifecycle](../overview.md#project-development-lifecycle) for more information.
+For more information, see the [conversational language understanding development lifecycle](../overview.md#project-development-lifecycle).
 
 ## Data labeling guidelines
 
-After [building your schema](build-schema.md) and [creating your project](create-project.md), you need to label your data. Labeling your data is important so your model knows which words and sentences are associated with the intents and entities in your project. Spend time labeling your utterances - introducing and refining the data that is used in training your models.
+After [building your schema](build-schema.md) and [creating your project](create-project.md), you need to label your data. Labeling your data is important so your model knows which sentences and words are associated with the intents and entities in your project. Spend time labeling your utterances - introducing and refining the data that is used in training your models.
 
 As you add utterances and label them, keep in mind:
 
-* The machine learning models generalize based on the labeled examples you provide it; the more examples you provide, the more data points the model has to make better generalizations. 
+* The machine learning models generalize based on the labeled examples you provide it; the more examples you provide, the more data points the model has to make better generalizations.
 
-* The precision, consistency and completeness of your labeled data are key factors to determining model performance. 
+* The precision, consistency, and completeness of your labeled data are key factors to determining model performance.
 
     * **Label precisely**: Label each intent and entity to its right type always. Only include what you want classified and extracted, avoid unnecessary data in your labels.
     * **Label consistently**:  The same entity should have the same label across all the utterances.
@@ -51,108 +54,109 @@ As you add utterances and label them, keep in mind:
 
 Use the following steps to label your utterances:
 
-1. Go to your project page in [Language Studio](https://aka.ms/languageStudio).
+1. Go to your project page in [AI Foundry](https://ai.azure.com).
+
+1. From the left side menu, select `Manage data`. In this page, you can start adding your utterances and labeling them. You can also upload your utterances directly by clicking on `Upload utterance file` from the top menu. Make sure it follows the [accepted format](../concepts/data-formats.md#utterance-file-format).
 
-2. From the left side menu, select **Data labeling**. In this page, you can start adding your utterance and labeling them. You can also upload your utterance directly by clicking on **Upload utterance file** from the top menu, make sure it follows the [accepted format](../concepts/data-formats.md#utterance-file-format).
+1. From the top pivots, you can change the view to be `training set` or `testing set`. Learn more about [training and testing sets](train-model.md#data-splitting) and how they're used for model training and evaluation.
 
-3. From the top pivots, you can change the view to be **training set** or **testing set**.  Learn more about [training and testing sets](train-model.md#data-splitting) and how they're used for model training and evaluation.
-    
     :::image type="content" source="../media/tag-utterances.png" alt-text="A screenshot of the page for tagging utterances in Language Studio." lightbox="../media/tag-utterances.png":::
-     
+
     > [!TIP]
-    > If you are planning on using **Automatically split the testing set from training data** splitting, add all your utterances to the training set.
-    
-  
-4.  From the **Select intent** dropdown menu, select one of the intents, the language of the utterance (for multilingual projects), and the utterance itself. Press the enter key in the utterance's text box to add the utterance.
+    > If you're planning on using `Automatically split the testing set from training data` splitting, add all your utterances to the training set.
+
+
+1.  From the `Select intent` dropdown menu, select one of the intents, the language of the utterance (for multilingual projects), and the utterance itself. Press enter key in the utterance's text box and add the utterance.
+
+1. You have two options to label entities in an utterance:
 
-5. You have two options to label entities in an utterance:
-    
     |Option |Description  |
     |---------|---------|
     |Label using a brush     | Select the brush icon next to an entity in the right pane, then highlight the text in the utterance you want to label.           |
     |Label using inline menu     | Highlight the word you want to label as an entity, and a menu appears. Select the entity you want to label these words with. |
-    
-6. In the right side pane, under the **Labels** pivot, you can find all the entity types in your project and the count of labeled instances per each.
 
-7. Under the **Distribution** pivot you can view the distribution across training and testing sets. You have two options for viewing:
+1. In the right side pane, under the `Labels` pivot, you can find all the entity types in your project and the count of labeled instances per each.
+
+1. Under the `Distribution` pivot, you can view the distribution across training and testing sets. You have two options for viewing:
     * *Total instances per labeled entity* where you can view count of all labeled instances of a specific entity.
     * *Unique utterances per labeled entity* where each utterance is counted if it contains at least one labeled instance of this entity.
     * *Utterances per intent* where you can view count of utterances per intent.
 
-:::image type="content" source="../media/label-distribution.png" alt-text="A screenshot showing entity distribution in Language Studio." lightbox="../media/label-distribution.png":::
+    :::image type="content" source="../media/label-distribution.png" alt-text="A screenshot showing entity distribution in Language Studio." lightbox="../media/label-distribution.png":::
 
 
   > [!NOTE]
-  > List and prebuilt components are not shown in the data labeling page, and all labels here only apply to the **learned component**.
+  > List, regex, and prebuilt components aren't shown in the data labeling page, and all labels here only apply to the **learned component**.
 
 To remove a label:
   1. From within your utterance, select the entity you want to remove a label from.
-  3. Scroll through the menu that appears, and select **Remove label**.
+  1. Scroll through the menu that appears, and select **Remove label**.
 
 To delete an entity:
-  1. Select the entity you want to edit in the right side pane.
-  2. Select the three dots next to the entity, and select the option you want from the drop-down menu.
+  1. Select the garbage bin icon next to the entity you want to edit in the right side pane. Then select **Delete** to confirm.
 
 ## Suggest utterances with Azure OpenAI
 
-In CLU, use Azure OpenAI to suggest utterances to add to your project using GPT models. You first need to get access and create a resource in Azure OpenAI. You'll then need to create a deployment for the GPT models. Follow the pre-requisite steps [here](../../../openai/how-to/create-resource.md).
+In `CLU`, use Azure OpenAI to suggest utterances to add to your project using generative language models. We recommended that you use an AI Foundry resource while using `CLU`, so you don't need to connect multiple resources. In order to use the AI Foundry resource, you need to provide your AI Foundry resource with elevated access. To do so, access the Azure portal. Within your Azure AI resource, provide access as a *Cognitive Services User* to itself. This step ensures that all parts of your resource are communicating correctly.
+
+### Connect with separate Language and Azure OpenAI Resources
 
-Before you get started, the suggest utterances feature is only available if your Language resource is in the following regions:
+You first need to get access and create a resource in Azure OpenAI. Next, create a connection to the Azure OpenAI resource within the same AI Foundry project in the `Management center` in the left panel of the Azure AI Foundry page. You then need to create a deployment for the AOAI models within the connected AOAI resource. Follow the prerequisite steps [here](../../../openai/how-to/create-resource.md) to create a new resource.
+
+Before you get started, the suggested utterances feature is only available if your Language resource is in the following regions:
 * East US
 * South Central US
 * West Europe
 
-In the Data Labeling page: 
+In the Data Labeling page:
 
-1. Select the **Suggest utterances** button. A pane opens up on the right side prompting you to select your Azure OpenAI resource and deployment. 
-2. On selection of an Azure OpenAI resource, select **Connect**, which allows your Language resource to have direct access to your Azure OpenAI resource. It assigns your Language resource the role of `Cognitive Services User` to your Azure OpenAI resource, which allows your current Language resource to have access to Azure OpenAI's service. If the connection fails, follow these [steps](#add-required-configurations-to-azure-openai-resource) below to add the right role to your Azure OpenAI resource manually. 
-3. Once the resource is connected, select the deployment. The recommended model for the Azure OpenAI deployment is `gpt-35-turbo-instruct`.
-4. Select the intent you'd like to get suggestions for. Make sure the intent you have selected has at least 5 saved utterances to be enabled for utterance suggestions. The suggestions provided by Azure OpenAI are based on the **most recent utterances** you've added for that intent. 
-5. Select **Generate utterances**. Once complete, the suggested utterances  show up with a dotted line around it, with the note *Generated by AI*. Those suggestions need to be accepted or rejected. Accepting a suggestion simply adds it to your project, as if you had added it yourself. Rejecting it deletes the suggestion entirely. Only accepted utterances are part of your project and used for training or testing. You can accept or reject by clicking on the green check or red cancel buttons beside each utterance. You can also use the `Accept all` and `Reject all` buttons in the toolbar. 
+1. Select the `Suggest utterances` button. A pane opens up on the right side prompting you to select your Azure OpenAI resource and deployment.
+1. On selection of an Azure OpenAI resource, select `Connect`, which allows your Language resource to have direct access to your Azure OpenAI resource. It assigns your Language resource the role of `Cognitive Services User` to your Azure OpenAI resource, which allows your current Language resource to have access to Azure OpenAI's service. If the connection fails, the following [steps](#add-required-configurations-to-azure-openai-resource) enable you to manually add the correct role to your Azure OpenAI resource.
+1. Once the resource is connected, select the deployment. The recommended model for the Azure OpenAI deployment is `gpt-35-turbo-instruct`.
+1. Select the intent you'd like to get suggestions for. Make sure the intent you selected has at least five saved utterances to be enabled for utterance suggestions. The suggestions provided by Azure OpenAI are based on the `most recent utterances` you added for that intent.
+1. Select `Generate utterances`. Once complete, the suggested utterances  show up with a dotted line around it, with the note *Generated by AI*. Those suggestions need to be accepted or rejected. Accepting a suggestion simply adds it to your project, as if you had added it yourself. Rejecting it deletes the suggestion entirely. Only accepted utterances are part of your project and used for training or testing. You can accept or reject by clicking on the green check or red cancel buttons beside each utterance. You can also use the `Accept all` and `Reject all` buttons in the toolbar.
 
-:::image type="content" source="../media/suggest-utterances.png" alt-text="A screenshot showing utterance suggestions in Language Studio." lightbox="../media/suggest-utterances.png":::
+    :::image type="content" source="../media/suggest-utterances.png" alt-text="A screenshot showing suggested utterances." lightbox="../media/suggest-utterances.png":::
 
 Using this feature entails a charge to your Azure OpenAI resource for a similar number of tokens to the suggested utterances generated. Details for Azure OpenAI's pricing can be found [here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/).
 
 ### Add required configurations to Azure OpenAI resource
 
-If connecting your Language resource to an Azure OpenAI resource fails, follow these steps:
-
 Enable identity management for your Language resource using the following options:
 
-### [Azure portal](#tab/portal)
+#### [Azure portal](#tab/portal)
 
 Your Language resource must have identity management, to enable it using the [Azure portal](https://portal.azure.com):
 
-1. Go to your Language resource
-2. From left hand menu, under **Resource Management** section, select **Identity**
-3. From **System assigned** tab, make sure to set **Status** to **On**
+1. Go to your Language resource.
+1. From left hand menu, under `Resource Management` section, select `Identity`.
+1. From `System assigned` tab, make sure to set `Status` to `On`.
 
-### [Language Studio](#tab/studio)
+#### [Language Studio](#tab/studio)
 
 Your Language resource must have identity management, to enable it using [Language Studio](https://aka.ms/languageStudio):
 
-1. Select the settings icon in the top right corner of the screen
-2. Select **Resources**
-3. Select the check box **Managed Identity** for your Language resource.
+1. Select the settings icon in the top right corner of the screen.
+1. Select *`Resources`.
+1. Select the check box `Managed Identity` for your Language resource.
 
 ---
 
-After enabling managed identity, assign the role `Cognitive Services User` to your Azure OpenAI resource using the managed identity of your Language resource. 
+After enabling managed identity, assign the role `Cognitive Services User` to your Azure OpenAI resource using the managed identity of your Language resource.
 
   1. Sign in to the [Azure portal](https://portal.azure.com) and navigate to your Azure OpenAI resource.
-  2. Select the Access Control (IAM) tab on the left. 
-  3. Select Add > Add role assignment. 
-  4. Select "Job function roles" and click Next.
-  5. Select `Cognitive Services User` from the list of roles and click Next.
-  6. Select Assign access to "Managed identity" and select "Select members". 
-  7. Under "Managed identity" select "Language".
-  8. Search for your resource and select it. Then select the Select button below and next to complete the process.
-  9. Review the details and select Review + Assign.
-
-:::image type="content" source="../media/add-role-azure-openai.gif" alt-text="Multiple screenshots showing the steps to add the required role to your Azure OpenAI resource." lightbox="../media/add-role-azure-openai.gif":::
-
-After a few minutes, refresh the Language Studio and you are able to successfully connect to Azure OpenAI.
+  1. Select the `Access Control (IAM)` tab.
+  1. Select `Add` > Add role assignment.
+  1. Select `Job function roles` and select `Next`.
+  1. Select `Cognitive Services User` from the list of roles and select `Next`.
+  1. Select Assign access to "Managed identity" and select `Select members`.
+  1. Under `Managed identity` select `Language`.
+  1. Search for your resource and select it. Then select `Next` and complete the process.
+  1. Review the details and select `Review + Assign`.
+
+     :::image type="content" source="../media/add-role-azure-openai.gif" alt-text="Multiple screenshots showing the steps to add the required role to your Azure OpenAI resource." lightbox="../media/add-role-azure-openai.gif":::
+
+After a few minutes, refresh the AI Foundry, and you can successfully connect to Azure OpenAI.
 
 ## Next Steps
 * [Train Model](./train-model.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話型言語理解における発話のタグ付け手順の更新"
}
```

### Explanation
この変更は、会話型言語理解プロジェクトにおける発話のタグ付け手順に関する内容の更新です。著者名、日付の更新に加え、プロジェクトで使用されるプラットフォーム名が「Language Studio」から「AI Foundry」に変更されています。また、発話のラベリング手順に関する説明が強化され、ユーザーがデータをどのようにラベル付けし、管理するかについての手順が明確化されています。

データラベリングがモデルのトレーニングに不可欠であることが強調され、既にラベル付けされた発話をインポートする手順も説明されています。加えて、新たにAI Foundryでの「Quick Deploy」オプションの利用を提案するヒントが追加され、エンティティとしてラベリングするための手順も詳細に説明されています。

全体として、更新により、ユーザーは発話のラベリングプロセスの理解を深め、プロジェクト内での具体的な操作方法が一層明瞭に示されています。また、Azure OpenAIを使用して発話の提案を行う手順も明記され、リソースの接続方法や必要な設定に関する情報が整理されています。これにより、ユーザーは会話型AIシステムをより効果的に構築・運用できるでしょう。


