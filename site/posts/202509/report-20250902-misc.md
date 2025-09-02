---
date: '2025-09-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6863762...MicrosoftDocs:4d69ee9
summary: この差分では、Azure AI サービスのドキュメントに新機能の追加や更新、いくつかのガイドの削除が行われました。特に、Azure AI Foundryに新たなカスタム質問応答ガイドが追加され、利用者により良い視覚的サポートが提供される一方で、Azure
  Language Studioに関するガイドが削除されました。これにより、ユーザーは新しい手法を探す必要があります。本変更は、Azureのドキュメントの利便性を高め、ユーザーが最新技術を効果的に活用できるようにするものです。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6863762...MicrosoftDocs:4d69ee9){target="_blank"}

<format>
# ハイライト
この差分では、Azure AI サービスの様々なガイドやドキュメントに新機能の追加や小規模な更新、またいくつかの重要な削除が行われました。特に注目すべきは、Azure AI Foundryにおけるカスタム質問応答の新たなガイドの追加や、Azure Language Studioに関するガイドラインの削除です。

## 新機能
- Azure AI Foundryにおけるカスタム質問応答プロジェクトの作成とデプロイに関する新たなガイドが追加。
- 新しい画像が多くのドキュメントに追加され、ユーザーがより直感的に理解できるように視覚的なサポートが強化。

## 破壊的変更
- Azure Language Studioに関するガイドが削除。これにより、ユーザーは以前の方法での設定情報を失う可能性があり、代替手段や新しい推奨手法が必要。

## その他の更新
- 複数の文書において、文法的な改善や手順の文章がわかりやすく整理。
- 日付の更新と一部内容の削除によって、新しい情報を反映させつつ、古い情報が取り除かれている。

# 洞察
この変更によってAzure AIのドキュメントは、ユーザー体験を向上させるために重要なビジュアルサポートを追加する一方で、最新の技術アップデートを提供しています。Azure Language Studioに関するガイドの削除は、一見すると不便に思われるかもしれませんが、これは恐らくAzureが新たな基準やツールを推奨する過渡期にあることを示唆しています。これに伴いユーザーは、新しく追加されたAzure AI Foundryに関するガイドを活用することで、カスタム質問応答プロジェクトをより効率的に進めることが期待されます。

新しい画像の追加によって、文書の視覚的理解が深まり、ユーザーは操作をより直感的に行えるようになります。これらの更新により、AzureのAIサービスは、より使いやすく、柔軟性が増した内容となり、ユーザーは最新技術を効果的に利用することが可能になると考えられます。この変更は、Azureサービスを利用するユーザーにとって全体的にプラスの影響をもたらすものであるといえるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [create-project.md](#item-58b2dd) | minor update | プロジェクト作成ガイドの更新 | modified | 5 | 6 | 11 | 
| [azure-ai-foundry.md](#item-3076ad) | minor update | Azure AI Foundryに関する記述の修正 | modified | 1 | 1 | 2 | 
| [best-practices.md](#item-0cd3cc) | minor update | 質問応答のベストプラクティスに関する内容の更新 | modified | 19 | 20 | 39 | 
| [export-import-refresh.md](#item-2d1b56) | minor update | QnAプロジェクトに関する説明の修正 | modified | 0 | 1 | 1 | 
| [azure-ai-foundry.md](#item-bb6666) | new feature | Azure AI Foundry におけるカスタム質問応答プロジェクトの作成とデプロイに関する新しいガイド | added | 116 | 0 | 116 | 
| [studio.md](#item-e095ff) | breaking change | Language Studioに関するガイドの削除 | removed | 0 | 95 | 95 | 
| [add-source-menu.png](#item-50863a) | new feature | ソース追加メニューの画像の追加 | added | 0 | 0 | 0 | 
| [custom-question-answering-tab.png](#item-0d3bd7) | new feature | カスタム質問応答タブの画像の追加 | added | 0 | 0 | 0 | 
| [fine-tune-button.png](#item-df42bd) | new feature | ファインチューニングボタンの画像の追加 | added | 0 | 0 | 0 | 
| [fine-tuning-selection.png](#item-d4a3f9) | new feature | ファインチューニング選択の画像の追加 | added | 0 | 0 | 0 | 
| [inspection-interface.png](#item-f766c0) | new feature | インスペクションインターフェースの画像の追加 | added | 0 | 0 | 0 | 
| [manage-sources-list.png](#item-e741e0) | new feature | ソース管理リストの画像の追加 | added | 0 | 0 | 0 | 
| [manage-sources.png](#item-e343cc) | new feature | ソース管理の画像の追加 | added | 0 | 0 | 0 | 
| [select-source-type.png](#item-b1bf89) | new feature | ソースタイプ選択の画像の追加 | added | 0 | 0 | 0 | 
| [sdk.md](#item-a86876) | minor update | カスタム質問応答のクイックスタートガイドの更新 | modified | 7 | 14 | 21 | 


# Modified Contents
## articles/ai-services/language-service/conversational-language-understanding/how-to/create-project.md{#item-58b2dd}

<details>
<summary>Diff</summary>
````diff
@@ -43,19 +43,18 @@ A Conversational Language Understanding (CLU) fine-tuning task is a workspace pr
 
    :::image type="content" source="../media/select-fine-tuning.png" alt-text="Screenshot of fine-tuning selector in the Azure AI Foundry.":::
 
-1. Select **the AI Service fine-tuning** tab and then **+ Fine-tune** button.
+1. From the main window, select **the AI Service fine-tuning** tab and then the **+ Fine-tune** button.
 
-   :::image type="content" source="../media/fine-tune-button.png" alt-text="Screenshot of fine-tuning button in the Azure AI Foundry.":::
+   :::image type="content" source="../media/fine-tune-button.png" alt-text="Screenshot of fine-tune button in the Azure AI Foundry.":::
 
-1. From **Create service fine-tuning** window, choose the **Conversational language understanding** tab then select **Next**.
+1. From the **Create service fine-tuning** window, choose the **Conversational language understanding** tab and then select **Next**.
 
    :::image type="content" source="../media/select-project.png" alt-text="Screenshot of conversational language understanding tab in the Azure AI Foundry.":::
 
-1. In **Create CLU fine-tuning task** window, complete the **Name** and **Language** fields. If you're planning to fine-tune a model using the free **Standard Training** mode, select **English** for the language field.
+1. In the **Create CLU fine-tuning task** window, complete the **Name** and **Language** fields. If you're planning to fine-tune a model using the free **Standard Training** mode, select **English** for the language field.
 
 1. Select the  **Create** button. It can take a few minutes for the *creating* operation to complete.
 
-
    > [!NOTE]
    >
    > * **Standard training** enables faster training times and quicker iterations; however it's only available for English.
@@ -178,4 +177,4 @@ If your project is no longer required, you can delete it using the REST API. To
 After you create your fine-tuning workspace, start your fine-tuning task by defining your intents and entities and adding them to your schema:
 
 * [Build your fine-tuning schema](build-schema.md)
-* [Label utterances](tag-utterances.md)
+* [Label utterances](tag-utterances.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト作成ガイドの更新"
}
```

### Explanation
このコードの変更は、Azure AIサービスのファインチューニングプロセスに関する「プロジェクト作成」ガイドラインの小規模な更新です。具体的には、手順に関する文言の明確化や整理が行われました。主な変更点は次の通りです：

1. 手順の一部で、動作の説明がより具体的になり、「From the main window, select...」のように、最初のウィンドウに触れつつ手順を記述しています。
2. タスクリストの項番スタイルが統一され、手順番号が一貫性を持つように修正されています。
3. 不要な改行が削除され、視認性の向上が図られています。

こうした修正により、ユーザーがファインチューニング作業を行う際のガイドが、一層理解しやすく、使いやすくなっています。

## articles/ai-services/language-service/conversational-language-understanding/includes/quickstarts/azure-ai-foundry.md{#item-3076ad}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ Use this article to get started with Conversational Language understanding using
 * **Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/free/cognitive-services).
 * **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control#cognitive-services-contributor).
 *  [Azure AI Foundry multi-service resource](/azure/ai-services/multi-service-resource). For more information, *see* [Configure an Azure AI Foundry resource](../../how-to/configure-azure-resources.md#option-1-configure-an-azure-ai-foundry-resource). Alternately, you can use an [Azure AI Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
-* Foundry project created in the Azure AI Foundry. For more information, *see* [Create an AI Foundry project](/azure/ai-foundry/how-to/create-projects).
+* A Foundry project created in the Azure AI Foundry. For more information, *see* [Create an AI Foundry project](/azure/ai-foundry/how-to/create-projects).
 
 ## Get started with Azure AI Foundry
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryに関する記述の修正"
}
```

### Explanation
このコードの変更は、Azure AI Foundryに関連する「クイックスタート」ガイドの内容に関する小規模な修正です。主な変更点は次の通りです：

1. プロジェクトの説明がより明確になるように、文言が「Foundry project created in the Azure AI Foundry」から「A Foundry project created in the Azure AI Foundry」に変更されました。この修正により、英語の文法が改善され、より自然な表現になっています。
2. 全体の文の構成が維持されており、ユーザーには必要な情報を簡潔かつ明確に提供します。

この変更によって、読者がAzure AI Foundryのプロジェクト作成要件を理解しやすくなり、より良い利用体験が促進されています。

## articles/ai-services/language-service/question-answering/how-to/best-practices.md{#item-0cd3cc}

<details>
<summary>Diff</summary>
````diff
@@ -2,17 +2,16 @@
 title: Project best practices
 description: Best practices for custom question answering
 ms.service: azure-ai-language
-ms.subservice: azure-ai-qna-maker
 ms.topic: how-to
 author: laujan
 ms.author: lajanuar
 recommendations: false
-ms.date: 06/21/2025
+ms.date: 08/29/2025
 ---
 
 # Project best practices
 
-The following list of QnA pairs will be used to represent a project to highlight best practices when authoring in custom question answering. 
+The following list of QnA pairs are used to represent a project to highlight best practices when authoring in custom question answering. 
 
 |Question                             |Answer                                                 | 
 |-------------------------------------|-------------------------------------------------------|
@@ -30,9 +29,9 @@ The following list of QnA pairs will be used to represent a project to highlight
 
 - Custom question answering employs a transformer-based ranker that takes care of user queries that are semantically similar to questions in the project. For example, consider the following question answer pair:
 
-   **Question: “What is the price of Microsoft Stock?”**
+   **Question: "What is the price of Microsoft Stock?"**
 
-   **Answer: “$200”.**
+   **Answer: "$200".**
 
    The service can return expected responses for semantically similar queries such as:
 
@@ -46,51 +45,51 @@ The following list of QnA pairs will be used to represent a project to highlight
 
    "What is the market value of a Microsoft share?"
 
-   However, please note that the confidence score with which the system returns the correct response will vary based on the input query and how different it is from the original question answer pair.
+   The system's confidence score depends on the input query and how closely it matches the original question-answer pair. Greater differences between them can lead to changes in the confidence level.
 
-- There are certain scenarios which require the customer to add an alternate question. When a query does not return the correct answer despite it being present in the project, we advise adding that query as an alternate question to the intended QnA pair.
+- There are certain scenarios that require the customer to add an alternate question. When a query doesn't return the correct answer despite it being present in the project, we advise adding that query as an alternate question to the intended QnA pair.
 
 ## How many alternate questions per QnA is optimal?
 
-- Users can add up to 10 alternate questions depending on their scenario. Alternate questions beyond the first 10 aren’t considered by our core ranker. However, they are evaluated in the other processing layers resulting in better output overall. All the alternate questions will be considered in the preprocessing step to look for an exact match.
+- Users can add up to 10 alternate questions depending on their scenario. Alternate questions beyond the first 10 aren't considered via our core ranker. However, they're evaluated in the other processing layers resulting in better output overall. All the alternate questions are considered in the preprocessing step to look for an exact match.
 
 - Semantic understanding in custom question answering should be able to take care of similar alternate questions.
 
-- The return on investment will start diminishing once you exceed 10 questions. Even if you’re adding more than 10 alternate questions, try to make the initial 10 questions as semantically dissimilar as possible so that all intents for the answer are captured by these 10 questions. For the project above, in QNA #1, adding alternate questions such as "How can I buy a car?", "I wanna buy a car." are not required. Whereas adding alternate questions such as "How to purchase a car.", "What are the options for buying a vehicle?" can be useful.
+- The return on investment starts diminishing once you exceed 10 questions. Even if you're adding more than 10 alternate questions, try to make the initial 10 questions as semantically dissimilar as possible so that all intents for the answer are captured via these 10 questions. For the project in QNA #1, adding alternate questions such as "How can I buy a car?", "I wanna buy a car." aren't required. Whereas adding alternate questions such as "How to purchase a car.", "What are the options for buying a vehicle?" can be useful.
 
 ## When to add synonyms to a project
 
 - Custom question answering provides the flexibility to use synonyms at the project level, unlike QnA Maker where synonyms are shared across projects for the entire service.
 
-- For better relevance, the customer needs to provide a list of acronyms that the end user intends to use interchangeably. For instance, the following is a list of acceptable acronyms:
+- For better relevance, the customer needs to provide a list of acronyms that the end user intends to use interchangeably. For instance, the following list provides acceptable acronyms:
 
-   MSFT – Microsoft
+   * MSFT – Microsoft
 
-   ID – Identification
+   * ID – Identification
 
-   ETA – Estimated time of Arrival
+   * ETA – Estimated time of Arrival
 
-- Apart from acronyms, if you think your words are similar in context of a particular domain and generic language models won’t consider them similar, it’s better to add them as synonyms. For instance, if an auto company producing a car model X receives queries such as "my car’s audio isn’t working" and the project has questions on "fixing audio for car X", then we need to add "X" and "car" as synonyms.
+- Apart from acronyms, if you think your words are similar in context of a particular domain and generic language models don't consider them similar, it's better to add them as synonyms. For instance, if an auto company producing a car model X receives queries such as "my car's audio isn't working" and the project has questions on "fixing audio for car X," then we need to add "X" and "car" as synonyms.
 
-- The Transformer based model already takes care of most of the common synonym cases, for e.g.- Purchase – Buy, Sell - Auction, Price – Value. For example, consider the following QnA pair: Q: "What is the price of Microsoft Stock?" A: "$200".
+- The Transformer based model already takes care of most of the common synonym cases, for example- Purchase – Buy, Sell - Auction, Price – Value. For example, consider the following QnA pair: Q: "What is the price of Microsoft Stock?" A: "$200".
 
-If we receive user queries like "Microsoft stock value", "Microsoft share value", "Microsoft stock worth", "Microsoft share worth", "stock value", etc., they should be able to get correct answer even though these queries have words like share, value, worth which are not originally present in the knowledge base.
+Users should receive accurate answers to queries like "Microsoft stock value," "Microsoft share value," or "stock worth," even if terms such as "share," "value," or "worth" aren't present in the knowledge base.
 
 ## How are lowercase/uppercase characters treated?
 
-Custom question answering takes casing into account but it's intelligent enough to understand when it is to be ignored. You should not be seeing any perceivable difference due to wrong casing.
+Custom question answering takes casing into account but it's intelligent enough to understand when it's to be ignored. You shouldn't be seeing any perceivable difference due to wrong casing.
 
 ## How are QnAs prioritized for multi-turn questions?
 
-When a KB has hierarchical relationships (either added manually or via extraction) and the previous response was an answer related to other QnAs, for the next query we give slight preference to all the children QnAs, sibling QnAs and grandchildren QnAs in that order. Along with any query, the [custom question Answering API] (/rest/api/cognitiveservices/questionanswering/question-answering/get-answers) expects a "context" object with the property "previousQnAId" which denotes the last top answer. Based on this previous QnA ID, all the related QnAs are boosted.
+When a knowledge base has hierarchical relationships, and the previous answer related to other QnAs, the system slightly favors, in order: child QnAs, sibling QnAs, then grandchild QnAs for the next query. Along with any query, the [custom question Answering API] (/rest/api/cognitiveservices/questionanswering/question-answering/get-answers) expects a "context" object with the property "previousQnAId" that denotes the last top answer. Based on this previous QnA ID, all the related QnAs are boosted.
 
 ## How are accents treated?
 
-Accents are supported for all major European languages. If the query has an incorrect accent, confidence score might be slightly different, but the service still returns the relevant answer and takes care of minor errors by leveraging fuzzy search.
+Accents are supported for all major European languages. If the query has an incorrect accent, confidence score might be slightly different, but the service still returns the relevant answer and takes care of minor errors by using fuzzy search.
 
 ## How is punctuation in a user query treated?
 
-Punctuation is ignored in user query before sending it to the ranking stack. Ideally it should not impact the relevance scores. Punctuation that are ignored are as follows:  ,?:;\"'(){}[]-+。./!*؟
+Punctuation is ignored in user query before sending it to the ranking stack. Ideally it shouldn't impact the relevance scores. Punctuation that is ignored:  ,?:;\"'(){}[]-+。./!*؟
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "質問応答のベストプラクティスに関する内容の更新"
}
```

### Explanation
このコードの変更は、Azureの質問応答サービスに関する「ベストプラクティス」ガイドの内容を小規模に更新するもので、以下の点が改善されています：

1. 日付の更新が行われ、最初の「ms.date」値が2025年6月21日から2025年8月29日に変更されました。これにより、コンテンツの新しさが保たれます。
2. 文法や表現がいくつかの箇所で修正され、より自然な文章に改善されています。例えば、「are used to represent」や「doesn’t」などの形式的な主語や動詞が適切に調整されています。
3. 「ユーザーが正確な答えを受け取る」などの表現が明確にされ、情報が一貫して提供されるようになっています。

この変更によって、質問応答を実施する際の指針が一層明確で理解しやすくなり、ユーザーにとっての利便性が向上しています。

## articles/ai-services/language-service/question-answering/how-to/export-import-refresh.md{#item-2d1b56}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Export/import/refresh | custom question answering projects and projects
 description: Learn about backing up your custom question answering projects and projects
 ms.service: azure-ai-language
-ms.subservice: azure-ai-qna-maker
 ms.topic: how-to
 author: laujan
 ms.author: lajanuar
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "QnAプロジェクトに関する説明の修正"
}
```

### Explanation
このコードの変更は、Azureの質問応答に関する「エクスポート/インポート/更新」ガイドの内容を小規模に修正するもので、具体的には以下の点が修正されています：

1. 不要な「ms.subservice」フィールドが削除されました。これにより、ドキュメント内の情報が簡潔になり、より明確に焦点が定まります。
2. 他のメタデータやドキュメント情報はそのまま維持されており、全体の構成に悪影響を及ぼさないよう配慮されています。

この変更により、ユーザーはカスタム質問応答プロジェクトに関するバックアップや管理手法について、より明確で整理された情報を得ることができます。

## articles/ai-services/language-service/question-answering/includes/azure-ai-foundry.md{#item-bb6666}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,116 @@
+---
+title: Create, test, and deploy your custom question answering project in Azure AI Foundry
+description: Create a custom question answering project from your own content, such as FAQs or product manuals. This article includes an example of creating a custom question answering project from a simple FAQ webpage, to answer questions.
+ms.service: azure-ai-language
+ms.topic: include
+ms.date: 08/30/2025
+---
+
+This quickstart guides you through the essential steps needed to create, test, and deploy a custom question answering (CQA) project in the Azure AI Foundry. Whether you're transitioning from Language Studio or starting from scratch, this quickstart is for you. It provides clear and actionable instructions to achieve a fast and successful CQA project deployment.
+
+> [!NOTE]
+>
+> * If you already have an Azure AI Language or multi-service resource—whether used on its own or through Language Studio—you can continue to use those existing Language resources within the Azure AI Foundry portal. For more information, see [How to use Azure AI services in the Azure AI Foundry portal](../../../../ai-services/connect-services-ai-foundry-portal.md).
+> * We highly recommend that you use an Azure AI Foundry resource in the AI Foundry; however, you can also follow these instructions using a Language resource.
+>
+
+## Prerequisites
+
+Before you get started, you need the following resources and permissions:
+
+* **An active Azure subscription**. If you don't have one, [create one for free](https://azure.microsoft.com/free/cognitive-services).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+*   An [Azure AI Foundry multi-service resource](../../../multi-service-resource.md) or an [Azure AI Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
+*   An [Azure AI Search resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.Search) (required for accessing CQA). For more information on how to connect your Azure AI Search resource, *see* [Configure connections in AI Foundry](../../conversational-language-understanding/how-to/configure-azure-resources.md#step-2-configure-connections-in-ai-foundry)
+* A Foundry project created in the Azure AI Foundry. For more information, *see* [Create an AI Foundry project](/azure/ai-foundry/how-to/create-projects).
+
+## Get started
+
+1. Navigate to the [Azure AI Foundry](https://ai.azure.com/).
+
+1. If you aren't already signed in, the portal prompts you to do so with your Azure credentials.
+
+1. Once signed in, you can create or access your existing projects within Azure AI Foundry.
+
+1. If you're not already at your project for this task, select it.
+
+## Create your CQA fine tuning task
+
+In the Azure AI Foundry, a fine-tuning task serves as your workspace for your CQA solutions. Previously, a **fine-tuning task** was referred to as a **CQA project**. You might encounter both terms used interchangeably in older CQA documentation.
+
+1. After you select the Azure AI Foundry project to use for this quickstart, select **fine-tuning** from the left navigation menu.
+
+     :::image type="content" source="../media/agents/fine-tuning-selection.png" alt-text="Screenshot of the fine-tuning menu selection in the Azure AI Foundry.":::
+
+1. From the main window, select the **AI Service fine-tuning** tab and then the **+ Fine-tune button**.
+
+     :::image type="content" source="../media/agents/fine-tune-button.png" alt-text="Screenshot of fine-tune button in the Azure AI Foundry.":::
+
+1. From the **Create service fine-tuning** window, choose the **Custom question answering** tab and then select **Next**.
+
+     :::image type="content" source="../media/agents/custom-question-answering-tab.png" alt-text="Screenshot of custom question answering tab in the Azure AI Foundry.":::
+
+1. Select your **Connected Azure AI Search resource** from the **Create CQA fine tuning task** window. For more information, *see* [Configure Azure resource connections](../../conversational-language-understanding/how-to/configure-azure-resources.md#step-2-configure-connections-in-ai-foundry).
+
+1. Next, complete the **Name** and **Language** fields. For this project, you can leave the **Default answer when no answer is returned** field as is (**No answer found**).
+
+1. Select the **Create** button.
+
+## Add a CQA knowledge base source
+
+A CQA knowledge base is a structured set of question-and-answer pairs optimized for conversational AI. The knowledge base uses natural language processing to interpret user queries and return context-aware, accurate answers from a specific dataset.
+
+1. From the **Getting Started** menu, select **Manage sources**.
+
+     :::image type="content" source="../media/agents/manage-sources.png" alt-text="Screenshot of manage sources selection in the Azure AI Foundry.":::
+
+1. From the main window, select the **+ Add source** drop-down menu.
+
+1. From the drop-down menu you can select **Add chit chat**, **Add URLs**, or **Add Files**.
+
+     :::image type="content" source="../media/agents/add-source-menu.png" alt-text="Screenshot of add source drop-down menu in the Azure AI Foundry.":::
+
+1. For this project, let's choose **Add chitchat**.
+
+1. From the **Add new source** window, let's choose **Friendly**.
+
+     :::image type="content" source="../media/agents/select-source-type.png" alt-text="Screenshot of the select source selection and add button in the Azure AI Foundry.":::
+
+1. Finally, select **Add**. It may take a few minutes for the source to be created.
+
+1. Once created, the source is listed in the **Manage sources** window.
+
+     :::image type="content" source="../media/agents/manage-sources-list.png" alt-text="Screenshot of manage sources list in the Azure AI Foundry.":::
+
+## Test your knowledge base
+
+1. Select **Test knowledge base** from the **Getting Started** menu.
+
+1. Type the following in the **Type your question** field and then select **Run**.
+
+     ```text
+       Hello! How are you doing today?
+
+     ```
+
+1. In the inspection interface, you can review the response confidence level and choose the most suitable answer.
+
+    :::image type="content" source="../media/agents/inspection-interface.png" alt-text="Screenshot of the inspection interface in the Azure AI Foundry.":::
+
+
+## Deploy your knowledge base
+
+Deploying a CQA knowledge base means publishing your curated question-and-answer content as a live, searchable endpoint. This process moves your project from a testing phase to a production environment enabling client applications to use it for various projects and solutions, including chatbots.
+
+1. Once your inspection is complete, choose the **Deploy knowledge base** section from the **Getting Started** menu.
+
+1. Select the **Deploy** button first from the **Deploy knowledge base** main window and then from the **Deploy this project** pop-up window. It takes a few minutes to deploy.
+
+1. After deployment is complete, your deployed project is listed in the **Deploy knowledge base** window.
+
+That's it! Your Custom Question Answering (CQA) knowledge base provides a natural language interface to your data, allowing users to interact with information in a conversational manner. By deploying this solution, you can create advanced chatbots and interactive agents that comprehend user questions, supply precise answers, and adjust to changing informational requirements.
+
+
+
+
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Foundry におけるカスタム質問応答プロジェクトの作成とデプロイに関する新しいガイド"
}
```

### Explanation
このコードの変更は、Azure AI Foundryでのカスタム質問応答（CQA）プロジェクトの作成、テスト、デプロイに関する新しいガイドを追加するもので、以下の内容が含まれています：

1. 新しいドキュメントは、Azure AI Foundryプラットフォームを利用してカスタム質問応答プロジェクトを迅速に立ち上げるための手順を詳細に説明しています。これには、既存のコンテンツを利用したプロジェクト作成の例も含まれています。
2. ユーザーが必要とするリソースや権限に関する情報が明記されており、Azureサブスクリプションや適切な役割の確認が必要であることが強調されています。
3. プロジェクトの段階を追って手順が示されており、具体的な操作手順や注意事項（例：リソースの接続方法、知識ベースのテストとデプロイ方法など）が提供されています。
4. ドキュメント全体に、視覚的な補助としてスニペットや画像が含まれており、ユーザーが理解しやすいように配慮されています。

この変更により、Azure AI Foundryを初めて利用するユーザーに対して、有益で実用的な情報源が提供され、彼らが自信を持ってプロジェクトを進められるようになります。

## articles/ai-services/language-service/question-answering/includes/studio.md{#item-e095ff}

<details>
<summary>Diff</summary>
````diff
@@ -1,95 +0,0 @@
----
-title: Create, test, and deploy your custom question answering project
-description: You can create a custom question answering project from your own content, such as FAQs or product manuals. This article includes an example of creating a custom question answering project from a simple FAQ webpage, to answer questions.
-ms.service: azure-ai-language
-ms.subservice: azure-ai-qna-maker
-ms.topic: include
-ms.date: 06/30/2025
----
-
-You can create a custom question answering project from your own content, such as FAQs or product manuals. This article includes an example of creating a custom question answering project from a product manual, to answer questions.
-
-## Prerequisites
-
-> [!div class="checklist"]
-> * If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/cognitive-services/) before you begin.
-> * A [language resource](https://aka.ms/create-language-resource) with the custom question answering feature enabled. Remember your Microsoft Entra ID, Subscription, language resource name you selected when you created the resource.
-
-
-
-## Create your first custom question answering project
-
-1. Sign in to the [Language Studio](https://language.azure.com/) with your Azure credentials.
-
-2. Scroll down to the **Answer questions** section and select **Open custom question answering**.
-
-    > [!div class="mx-imgBorder"]
-    > ![Open custom question answering](../media/create-test-deploy/open-custom-question-answering.png)
-
-3. If your resource is not yet connected to Azure Search select **Connect to Azure Search**. This will open a new browser tab to **Features** pane of your resource in the Azure portal.
-
-    > [!div class="mx-imgBorder"]
-    > ![Connect to Azure Search](../media/create-test-deploy/connect-to-azure-search.png)
-
-4. Select **Enable custom question answering**, choose the Azure Search resource to link to, and then select **Apply**.
-
-    > [!div class="mx-imgBorder"]
-    > ![Enable custom question answering](../media/create-test-deploy/enable-custom-question-answering.png)
-
-5. Return to the Language Studio tab. You might need to refresh this page for it to register the change to your resource. Select **Create new project**.
-
-6. Choose the option **I want to set the language for all projects created in this resource** > select **English** > Select **Next**.
-
-7. Enter a project name of **Sample-project**, a description of **My first question answering project**, and leave the default answer with a setting of **No answer found**.
-
-8. Review your choices and select **Create project**
-
-9. From the **Manage sources** page select **Add source** > **URLS**.
-
-10. Select **Add url** enter the following values and then select **Add all**:
-
-    |URL Name|URL Value|
-    |--------|---------|
-    |Surface Book User Guide |https://download.microsoft.com/download/7/B/1/7B10C82E-F520-4080-8516-5CF0D803EEE0/surface-book-user-guide-EN.pdf |
-
-    The extraction process takes a few moments to read the document and identify questions and answers.
-
-    After successfully adding the source, you can then edit the source contents to add more custom question answer sets.
-
-
-
-## Test your project
-
-1. Select the link to your source, this will open the edit project page.
-
-2. Select **Test** from the menu bar > Enter the question **How do I setup my surface book?**. An answer will be generated based on the question answer pairs that were automatically identified and extracted from your source URL:
-
-    > [!div class="mx-imgBorder"]
-    > ![Test question chat interface](../media/create-test-deploy/test-question.png)
-
-    If you check the box for **include short answer response** you will also see a precise answer, if available, along with the answer passage in the test pane when you ask a question.
-
-3. Select **Inspect** to examine the response in more detail. The test window is used to test your changes to your project before deploying your project.
-
-    > [!div class="mx-imgBorder"]
-    > ![See the confidence interval](../media/create-test-deploy/inspect-test.png)
-
-    From the **Inspect** interface, you can see the level of confidence that this response will answer the question and directly edit a given question and answer response pair.
-
-
-
-## Deploy your project
-
-1. Select the Deploy project icon to enter the deploy project menu.
-
-    > [!div class="mx-imgBorder"]
-    > ![Deploy project](../media/create-test-deploy/deploy-knowledge-base.png)
-
-    When you deploy a project, the contents of your project move from the `test` index to a `prod` index in Azure Search.
-
-2. Select **Deploy** > and then when prompted select **Deploy** again.
-
-    > [!div class="mx-imgBorder"]
-    > ![Successful deployment](../media/create-test-deploy/successful-deployment.png)
-
-    Your project is now successfully deployed. You can use the endpoint to answer questions in your own custom application to answer or in a bot.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioに関するガイドの削除"
}
```

### Explanation
このコードの変更は、Azure Language Studioに関するガイドを完全に削除するもので、具体的には以下の内容が該当します：

1. **全体の削除**: 95行にわたるコンテンツが削除されており、これにはカスタム質問応答プロジェクトを作成、テスト、デプロイするための手順が含まれていました。
2. **ドキュメント内容**: 削除されたガイドには、Azureへのサインイン、プロジェクトの作成手順、ソースの追加方法、プロジェクトのテスト、デプロイの手順など、具体的な作業手順が詳述されていました。
3. **影響**: この変更により、Azure Language Studioを使用するユーザーは、以前の方法でのカスタム質問応答プロジェクトの作成やデプロイに関する情報を失うことになります。これは、新しいプロジェクトや手法に過渡するための重要な情報が欠如することを意味し、特にAzureが推奨する最新の移行先や代替手段に関する明確なガイダンスが求められます。

この変更は、ユーザーにとって大きな影響を与える可能性があり、今後のドキュメントの更新や代わりの情報源を整備する必要性が高まります。

## articles/ai-services/language-service/question-answering/media/agents/add-source-menu.png{#item-50863a}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ソース追加メニューの画像の追加"
}
```

### Explanation
このコードの変更は、AzureのLanguage Serviceに関連する新しい画像ファイルを追加するもので、具体的には「ソース追加メニュー」の画像が新たに追加されました。以下はその詳細です：

1. **画像の役割**: この画像は、ユーザーがカスタム質問応答プロジェクトでソースを追加する際に使用するメニューの視覚的な表示を提供します。視覚的な情報は、ユーザーにとって理解を助け、操作をスムーズにする重要な要素です。
   
2. **ユーザー体験の向上**: 新しい画像は、ガイドや文書に表示されることで、特定の手順を視覚的にサポートし、ユーザーが自分のプロジェクトに正しいリソースを追加する際の助けとなります。

3. **技術的詳細**: 変更内容は画像ファイルの追加であり、実際のコードの変更や削除は行われていません。これは、ドキュメントやチュートリアルの情報をより充実させるための措置の一部です。

この変更により、Azure Language Serviceに関連するドキュメントは、ユーザーに対する視覚的な補助が加わり、より使いやすく、理解しやすいものになることが期待されます。

## articles/ai-services/language-service/question-answering/media/agents/custom-question-answering-tab.png{#item-0d3bd7}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "カスタム質問応答タブの画像の追加"
}
```

### Explanation
このコードの変更は、AzureのLanguage Serviceに関連する新しい画像ファイルを追加するもので、具体的には「カスタム質問応答タブ」の画像が新たに追加されました。以下はその詳細です：

1. **画像の役割**: この画像は、ユーザーがカスタム質問応答機能を使用する際にアクセスするタブの視覚的な表示を提供します。視覚的な資料は、ユーザーがインターフェイスをより理解しやすくするための重要な要素です。

2. **ユーザー体験の向上**: 新しい画像は、ドキュメントやガイドにおいて、カスタム質問応答機能に関連する操作手順を視覚的にサポートし、ユーザーが正確にナビゲートできるよう助けます。これにより、特定の機能の利用が容易になります。

3. **技術的詳細**: 変更内容は画像ファイルの追加であり、実際の文書の内容やコードの変更はありません。この画像の追加は、Azure Language Serviceに関するドキュメントの充実を図るために行われています。

この変更によって、ユーザーに対する視覚的なサポートが強化され、Azure Language Serviceを利用したカスタム質問応答機能の理解と操作がより円滑になることが期待されます。

## articles/ai-services/language-service/question-answering/media/agents/fine-tune-button.png{#item-df42bd}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニングボタンの画像の追加"
}
```

### Explanation
このコードの変更は、AzureのLanguage Serviceに関連する新しい画像ファイルを追加するものであり、具体的には「ファインチューニングボタン」の画像が新たに追加されました。以下はその詳細です：

1. **画像の役割**: この画像は、ユーザーがモデルをファインチューニングする際に使用するボタンの視覚的な表現を提供します。ファインチューニング機能は、ユーザーが自分のニーズに合わせてAIモデルを調整するために重要です。

2. **ユーザー体験の向上**: 新しい画像は、ドキュメントやチュートリアルに表示されることで、ユーザーがファインチューニングのプロセスを視覚的に理解しやすくなります。これにより、操作性が向上し、ユーザーが自信を持って機能を利用できるようになります。

3. **技術的詳細**: 変更は画像ファイルの追加のみであり、実際のコードや文書内のテキストの変更はありません。この追加は、Azure Language Serviceのドキュメントのビジュアルコンテンツを強化するために行われています。

この変更によって、ファインチューニング機能に関するユーザーの理解が深まり、AzureのAIサービスを利用したカスタマイズがより容易になります。

## articles/ai-services/language-service/question-answering/media/agents/fine-tuning-selection.png{#item-d4a3f9}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニング選択の画像の追加"
}
```

### Explanation
このコードの変更は、AzureのLanguage Serviceに関連する新しい画像ファイルを追加するものであり、具体的には「ファインチューニング選択」の画像が新たに追加されました。以下はその詳細です：

1. **画像の役割**: この画像は、ユーザーがファインチューニングの選択肢を操作する際に表示される視覚的な要素です。ファインチューニングの選択は、AIモデルを特定のタスクやニーズに合わせて調整するために不可欠です。

2. **ユーザー体験の向上**: 新しい画像の追加により、ユーザーはファインチューニングに関する選択肢をより直感的に理解できるようになります。ドキュメントに視覚的要素が加わることで、ユーザーが複雑な設定やオプションを把握しやすくなります。

3. **技術的詳細**: この変更は画像ファイルの追加にのみ関連しており、コードやテキストの変更はありません。この更新は、Azure Language Serviceに関する情報をより魅力的かつ分かりやすくするためのものです。

この変更により、ファインチューニング機能を利用する際のユーザーの理解が深まり、AzureのAIサービスを効果的に活用する手助けが期待されます。

## articles/ai-services/language-service/question-answering/media/agents/inspection-interface.png{#item-f766c0}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "インスペクションインターフェースの画像の追加"
}
```

### Explanation
この変更は、AzureのLanguage Serviceに関連する新たな画像ファイルを追加するもので、具体的には「インスペクションインターフェース」の画像が追加されました。以下はその概要です：

1. **画像の役割**: インスペクションインターフェースは、ユーザーがモデルの応答や動作を確認・評価するための視覚的な要素です。このインターフェースによって、ユーザーはAIモデルの出力を円滑に分析できます。

2. **ユーザー体験の向上**: 新しい画像の追加により、ユーザーはインスペクションプロセスを直感的に理解しやすくなります。視覚的なサポートがあることで、ユーザーはインターフェースの機能を把握しやすくなり、操作性が向上します。

3. **技術的詳細**: この変更は画像ファイルの追加のみであり、コードやテキストの変更は行われていません。ドキュメントのビジュアルコンテンツが強化され、ユーザーにとってより魅力的な形で情報が提供されるようになります。

この変更によって、ユーザーはインスペクションインターフェースをより効果的に利用できるようになり、AzureのAIサービスにおける応答の評価が促進されることが期待されます。

## articles/ai-services/language-service/question-answering/media/agents/manage-sources-list.png{#item-e741e0}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ソース管理リストの画像の追加"
}
```

### Explanation
この変更は、AzureのLanguage Serviceに関連する新しい画像ファイルを追加するものであり、具体的には「ソース管理リスト」の画像が新たに追加されました。以下はその概要です：

1. **画像の役割**: ソース管理リストは、ユーザーが質問応答システムに対して利用するデータソースを管理するための視覚的な要素です。この画像は、どのようにソースを追加または管理するかを示す際に役立ちます。

2. **ユーザー体験の向上**: 新しい画像の追加により、ユーザーはソース管理リストの操作をより簡単に理解できるようになります。視覚的な説明があることで、ユーザーは具体的な操作手順を把握しやすくなり、全体的な使いやすさが向上します。

3. **技術的詳細**: この変更は、画像ファイルの追加に関連しており、コードやテキストの変更は行われていません。情報の視覚的サポートが強化されることで、ユーザーはAzure AIの機能をより効果的に利用できるようになります。

この変更により、ユーザーはソース管理リストをより効果的に使用でき、質問応答システムの設定や運用においてさらなる理解を得ることが期待されます。

## articles/ai-services/language-service/question-answering/media/agents/manage-sources.png{#item-e343cc}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ソース管理の画像の追加"
}
```

### Explanation
この変更は、AzureのLanguage Serviceに関連する新しい画像ファイルを追加するものであり、具体的には「ソース管理」の画像が新たに追加されました。以下はその概要です：

1. **画像の役割**: ソース管理は、ユーザーが質問応答システムで使用するデータソースを整理・管理するための重要な機能です。この画像は、ユーザーがソースを管理する方法を視覚的に示すものです。

2. **ユーザー体験の向上**: 新しい画像の追加により、ユーザーはソースをどのように管理するかを直感的に理解しやすくなります。視覚資料が提供されることで、操作の手順や方法をスムーズに把握でき、全体的な体験が向上します。

3. **技術的詳細**: この変更は、画像ファイルの追加に関するものであり、ソースコードやテキストの変更は含まれていません。ドキュメントの視覚的な要素が補完されることで、情報がより豊かになり、ユーザーの理解を助けることが期待されます。

この変更によって、ユーザーはソース管理機能をより効果的に利用し、AzureのAIサービスでの質問応答システムの設定や運用においてさらなる理解を得ることができるでしょう。

## articles/ai-services/language-service/question-answering/media/agents/select-source-type.png{#item-b1bf89}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ソースタイプ選択の画像の追加"
}
```

### Explanation
この変更は、Azure Language Serviceに関連する新しい画像ファイルを追加するもので、特に「ソースタイプ選択」の画像が新たに追加されました。以下はその概要です：

1. **画像の役割**: ソースタイプの選択は、ユーザーが質問応答システムに対して使用したいデータソースのタイプを指定するための重要なステップです。この画像は、その選択プロセスを視覚的に示す役割を果たします。

2. **ユーザー体験の向上**: 新しい画像の追加によって、ユーザーはどのようにしてソースのタイプを選ぶべきかをより直感的に理解できるようになります。視覚的なガイドがあることで、手続きが明確になり、全体の操作体験が向上します。

3. **技術的詳細**: 変更は画像ファイルの追加に関連し、コードやテキストの直接的な変更はありません。この新しい視覚資料によって、ドキュメントの内容がより充実し、ユーザーに対する情報の伝達がより効果的になります。

この変更により、ユーザーはソースタイプの選択をよりスムーズに行い、Azure AIサービスを用いた質問応答システムの設定や管理をより効果的に行えるようになることが期待されます。

## articles/ai-services/language-service/question-answering/quickstart/sdk.md{#item-a86876}

<details>
<summary>Diff</summary>
````diff
@@ -1,27 +1,23 @@
 ---
-title: "Quickstart: Use SDK to create and manage project - custom question answering"
-description: This quickstart shows you how to create and manage your project using custom question answering.
+title: "Quickstart: custom question answering"
+description: This quickstart shows you how to create and manage your  custom question answering projects.
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 03/24/2025
+ms.date: 08/29/2025
 author: laujan
 ms.author: lajanuar
 recommendations: false
 ms.devlang: csharp
 # ms.devlang: csharp, python
 ms.custom: devx-track-python, devx-track-csharp, language-service-question-answering, mode-api, devx-track-dotnet
-zone_pivot_groups: custom-qna-quickstart
+zone_pivot_groups: custom-cqa-quickstart
 ---
 
-# Quickstart: custom question answering
+# Quickstart: custom question answering (CQA)
 
-> [!NOTE]
-> Are you looking to migrate your workloads from QnA Maker? See our [migration guide](../how-to/migrate-qnamaker-to-question-answering.md) for information on feature comparisons and migration steps.
 
-Get started with the custom question answering client library. Follow these steps to install the package and try out the example code for basic tasks.
-
-::: zone pivot="studio"
-[!INCLUDE [Studio quickstart](../includes/studio.md)]
+::: zone pivot="foundry"
+[!INCLUDE [Azure AI Foundry quickstart](../includes/azure-ai-foundry.md)]
 ::: zone-end
 
 ::: zone pivot="rest"
@@ -44,11 +40,8 @@ If you want to clean up and remove an Azure AI services subscription, you can de
 * [Azure CLI](../../../multi-service-resource.md?pivots=azcli#clean-up-resources)
 
 
-
 ## Explore the REST API
 
-To learn about automating your custom question answering pipeline consult the REST API documentation. Currently authoring functionality is only available via REST API:
-
 * [Authoring API reference](/rest/api/questionanswering/question-answering-projects)
 * [Authoring API cURL examples](../how-to/authoring.md)
 * [Runtime API reference](/rest/api/questionanswering/question-answering)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム質問応答のクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azureのカスタム質問応答に関するクイックスタートガイドのドキュメントを更新するもので、以下の重要な変更点があります。

1. **タイトルと説明の簡略化**: ドキュメントのタイトルが「Quickstart: Use SDK to create and manage project - custom question answering」から「Quickstart: custom question answering」に短縮され、説明も「custom question answering projectsを作成し、管理する方法を示します」といった明確で簡潔な表現に変更されました。

2. **日付の更新**: ドキュメントの更新日時が「03/24/2025」から「08/29/2025」に変更され、新しい情報が反映されたことを示しています。

3. **ゾーンの変更**: 使用されるゾーンが「studio」から「foundry」に変更され、最新の環境設定に適応しています。これにより、ユーザーはAzure AI Foundryに関するクイックスタートガイドを参照できるようになります。

4. **一部内容の削除**: 古い内容が削除され、新たな情報が加わっています。特にREST APIに関するガイドラインが省略されていますが、これは最新の使用法に合わせて整理されていることを反映しています。

この更新により、ユーザーはカスタム質問応答のセットアップをより明確に理解し、最新の利用方法に従って手順を進めることができるようになります。全体的に、ドキュメントはよりユーザーフレンドリーで、直感的に使いやすくなっています。


