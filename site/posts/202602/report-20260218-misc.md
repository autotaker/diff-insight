---
date: '2026-02-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:43ce856...MicrosoftDocs:ff21499
summary: このドキュメントは、Microsoft Foundryのオーケストレーションワークフローに関するアップデートを含んでいます。新しい画像が追加され、既存の画像が更新され、ドキュメントには最新の情報を反映するための微細な修正が行われました。主要な新機能としては、新規画像ファイルの追加や発話アップロード機能を示す画像が含まれています。破壊的な変更は特に報告されていませんが、LUISサービスの廃止に関する注意が加えられています。さらに、ドキュメントの日付更新やTOCファイルの修正、自明な手順の改善など、小規模な変更も含まれています。全体的に、これらの変更はユーザー体験を向上させ、技術情報の整合性を高めることを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:43ce856...MicrosoftDocs:ff21499){target="_blank"}

```markdown
# Highlights
このドキュメントの変更には、Microsoft Foundryのオーケストレーションワークフローに関するアップデートが含まれています。ユーザーインターフェースのさらなる視覚化を可能にする新規画像の追加、および既存の画像の更新が行われました。また、ドキュメントの一部は最新の情報を反映するために微細な修正が行われています。

## New features
- オーケストレーションワークフローに関する複数の新規画像ファイルが追加されました。
- 発話アップロード機能を視覚的に示す画像が追加されました。

## Breaking changes
- 特に大きな破壊的変更は報告されていませんが、LUISサービスの廃止に関する注意喚起が文書に追加されています。

## Other updates
- ドキュメントの日付更新やTOCファイルの項目名修正、一部手順の明確化といった小規模な修正が含まれています。

# Insights
この変更は、Microsoft Foundryのオーケストレーションワークフローに関するユーザー体験を向上させるためのものであることがわかります。特に、視覚的な要素を増やすことで、初心者から上級者まで幅広いユーザーが直感的に操作を学べるように設計されています。新たに追加された画像は、プロセスの可視性を高め、ステップバイステップの操作手順を補完する役割を果たしており、結果としてユーザーの操作性を向上させます。

一方で、LUISサービスの廃止日が詳述されていることから、システム移行が求められるユーザーにとっては今後の対策が必要になります。このような情報は、ユーザーが計画的にシステムを更新するための重要な基盤を提供します。また、ドキュメントの日付やTOCファイルの修正に関しても、情報の整合性を高め、ユーザーが最新情報に迅速にアクセスできるように工夫されています。

全体として、ドキュメントの更新は、技術情報の提供を強化し、Azureの新機能を利用した効果的な開発を促進する重要な役割を担っています。
```

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [microsoft-foundry.md](#item-272dfd) | minor update | Microsoft Foundryにおけるオーケストレーションワークフローのアップデート | modified | 55 | 10 | 65 | 
| [orchestration-add-intent.png](#item-39d33d) | new feature | オーケストレーションワークフローの意図追加に関する画像の追加 | added | 0 | 0 | 0 | 
| [orchestration-link-tasks.png](#item-c1ee06) | minor update | オーケストレーションワークフローのタスクリンクに関する画像の更新 | modified | 0 | 0 | 0 | 
| [orchestration-linked-tasks.png](#item-41c832) | new feature | オーケストレーションワークフローのリンクされたタスクに関する画像の追加 | added | 0 | 0 | 0 | 
| [orchestration-no-tasks-warning.png](#item-0c5244) | new feature | オーケストレーションワークフローのタスクがないことを警告する画像の追加 | added | 0 | 0 | 0 | 
| [orchestration-workflow-overview.png](#item-2b3cfd) | minor update | オーケストレーションワークフローの概要画像の修正 | modified | 0 | 0 | 0 | 
| [upload-utterances.png](#item-14f259) | new feature | 発話アップロード機能の画像の追加 | added | 0 | 0 | 0 | 
| [quickstart.md](#item-bee292) | minor update | クイックスタートの日付の更新 | modified | 1 | 1 | 2 | 
| [migrate.md](#item-8a4128) | minor update | 移行ガイドの内容の更新 | modified | 63 | 9 | 72 | 
| [toc.yml](#item-12f1f0) | minor update | TOCファイルの項目名の変更 | modified | 4 | 4 | 8 | 
| [whats-new.md](#item-69b272) | minor update | Azure Languageの新機能の追加 | modified | 13 | 1 | 14 | 


# Modified Contents
## articles/ai-services/language-service/orchestration-workflow/includes/quickstarts/microsoft-foundry.md{#item-272dfd}

<details>
<summary>Diff</summary>
````diff
@@ -3,22 +3,42 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 01/09/2026
+ms.date: 02/03/2026
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD041 -->
 ## Prerequisites
 
 > [!NOTE]
 >
-> * If you already have an Azure Language in Foundry Tools or multi-service resource you can continue to use those existing Language resources within the Microsoft Foundry portal via a Foundry Hub project.
-> * For more information, see [How to use Foundry Tools in the Foundry portal](/azure/ai-services/connect-services-ai-foundry-portal).
+> * If you already have an Azure Language in Foundry Tools or multi-service resource, you can continue to use those existing Language resources within the Microsoft Foundry portal via a Foundry Hub project.
+> * For more information, see [How to use Foundry Tools in the Foundry portal](../../../../connect-services-foundry-portal.md)
 > * We highly recommended that you use a Foundry resource in the Foundry; however, you can also follow these instructions using a Language resource.
 
 <!-- markdownlint-disable MD032 -->
 [!INCLUDE [Foundry prerequisites](../../../includes/microsoft-foundry/prerequisites.md)]
 * A [**Conversational language understanding (CQA)**](../../../conversational-language-understanding/overview.md) or [**Custom question answering (CQA)**](../../../question-answering/overview.md) project created in the Foundry.
 
+## Migrate an existing orchestration workflow from Language Studio
+
+If you have an existing orchestration workflow in Language Studio that you want to use in Foundry, you have two migration options:
+
+### Option 1: Connect your Language resource to a Foundry Hub (recommended)
+
+Connect your existing Language resource to a Foundry Hub project. This approach automatically preserves all task linkages between your orchestration workflow and its associated CLU and CQA tasks.
+
+### Option 2: Import projects into a new Foundry resource
+
+If you want to use a new Foundry resource, import your projects individually. To preserve task linkages, import in the following order:
+
+1. Import your CLU and CQA tasks first.
+1. Import the orchestration workflow only after the dependent tasks are available in the Foundry resource.
+
+> [!IMPORTANT]
+> The import order matters. If you import the orchestration workflow before its dependent CLU and CQA tasks, the task linkages aren't preserved. You must then manually relink the tasks in the **Configure orchestration** section.
+
+For detailed migration steps, see [Migrate from Language Studio to Microsoft Foundry](../../../migration-studio-to-foundry.md).
+
 ## Get started
 
 After you create your Foundry resource, you can initiate an orchestration workflow project in the [Microsoft Foundry](https://ai.azure.com/). This project serves as a dedicated workspace for developing custom machine learning models using your data. Access to the project is restricted to you and others who have permissions for the associated Foundry resource.
@@ -45,7 +65,11 @@ Let's begin:
 
 1. From the window that appears, select **Conversational Orchestration Workflow** as the task type, then select **Next**.
 
-   :::image type="content" source="../../media/select-orchestration-workflow.png" alt-text="Screenshot of selecting orchestration workflow in the Foundry.":::
+    * If you don't have a CLU or CQA fine-tuning task in this Foundry resource, a warning appears indicating that no tasks are available to link.
+
+       :::image type="content" source="../../media/orchestration-no-tasks-warning.png" alt-text="Screenshot of no tasks warning in orchestration workflow creation in the Foundry.":::
+
+    * Create a [Conversational Language Understanding](../../../conversational-language-understanding/quickstart.md) or [Custom Question Answering](../../../question-answering/quickstart/sdk.md) task first, then return to create your orchestration workflow.
 
 1. In the **Create service fine-tuning window**, you can choose to create a new task or import an existing one. Complete all required fields, then select **Create**:
 
@@ -55,23 +79,44 @@ Let's begin:
 
 1. After creating the orchestration workflow project, you'll be directed to the project overview page. Here, you can manage your project settings, monitor training progress, and access various tools to enhance your model.
 
-## Link tasks
+## Configure orchestration
 
-1. To add existing **`CLU`** or **`CQA`** models to your orchestration workflow, navigate to the **Link tasks** button within your project. Here, you can add intents and entities from your existing models to the orchestration workflow.
+Connect your existing **Conversational Language Understanding** (CLU) and **Custom Question Answering** (CQA) fine-tuning tasks to create a unified orchestration layer that routes user inputs to the appropriate model. You can define more routing intents when user inputs are ambiguous and need extra logic to identify the correct task.
+
+> [!NOTE]
+> If the **Configure orchestration** page is empty, you don't have any CLU or CQA fine-tuning tasks in this Foundry resource. Create a [Conversational Language Understanding](../../../conversational-language-understanding/quickstart.md) or [Custom Question Answering](../../../question-answering/quickstart/sdk.md) task first, then return to this page and link it.
+
+1. To add existing **`CLU`** or **`CQA`** models to your orchestration workflow, navigate to your fine-tuning project and select the **Configure orchestration** section from the **Getting started** menu. There, you can link your fine-tuning tasks and add intents from your existing models to the orchestration workflow.
 
    :::image type="content" source="../../media/orchestration-workflow-overview.png" alt-text="Screenshot of orchestration workflow overview in the Foundry." lightbox="../../media/orchestration-workflow-overview.png":::
 
-1. Link your tasks by selecting from the **Task type** and **Fine-tuning task name** dropdown menus. The **Intent name** field automatically populates with the same name as the **fine-tuning task name** field. Once everything is set, select **Add** to continue.
+1. Link your tasks by selecting the radio button next to the task you want to link, and then selecting the **Link fine-tuning task** from the top navigation bar. The **Orchestration intent name** field automatically populates with the same name as the **Fine-tuning task name** field.
+
+   :::image type="content" source="../../media/orchestration-link-tasks.png" alt-text="Screenshot of linking tasks in orchestration workflow in the Foundry." lightbox="../../media/orchestration-link-tasks.png":::
+
+1. Once this step is complete, the status for your linked tasks changes from **Unlinked** to **Linked** in the **Configure orchestration** section.
+
+   :::image type="content" source="../../media/orchestration-linked-tasks.png" alt-text="Screenshot of linked tasks in orchestration workflow in the Foundry." lightbox="../../media/orchestration-linked-tasks.png":::
 
-   :::image type="content" source="../../media/orchestration-link-tasks.png" alt-text="Screenshot of linking tasks in orchestration workflow in the Foundry.":::
+1. To link multiple fine-tuning tasks at once, select one or more unlinked tasks, then select **Link fine-tuning task** from the top navigation bar.
+
+1. To unlink tasks, select one or more linked tasks, then select **Unlink fine-tuning task** from the top navigation bar.
+
+1. To add routing intents, select the **Intents** tab from the top navigation bar. In the window that appears, select the **+ Add intent** button, provide a unique name for your intent in the **Intent name** field, then select **Add** to continue.
+
+   :::image type="content" source="../../media/orchestration-add-intent.png" alt-text="Screenshot of adding intents in orchestration workflow in the Foundry." lightbox="../../media/orchestration-add-intent.png":::
 
 ## Add training data
 
-1. Navigate to the Manage Data tab and add your utterances file. For this project, you can download our [**sample utterances file**](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/language-service/CLU/clu_utterances.json) which comes preconfigured with labeled utterances.
+1. Navigate to the Manage Data tab. For this project, use one of your existing **Conversational Language Understanding** (CLU) projects. If your existing project doesn't include labeled utterances, you can download our [**sample utterances file**](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/language-service/CLU/clu_utterances.json) which comes preconfigured with labeled utterances.
+
+1. Select the **Upload utterances** button to upload your utterances file in JSON format.
+
+   :::image type="content" source="../../media/upload-utterances.png" alt-text="Screenshot of uploading utterances in orchestration workflow in the Foundry.":::
 
 1. After uploading your utterances file, select the **unlinked intents** from the Insights pane. This action allows you to map these intents to the appropriate linked tasks within your orchestration workflow.
 
-   :::image type="content" source="../../media/select-unlinked-intents.png" alt-text="Screenshot of unlinked intents in orchestration workflow in the Foundry." lightbox="../../media/select-unlinked-intents.png":::
+   :::image type="content" source="../../media/select-unlinked-intents.png" alt-text="Screenshot of unlinked intents in orchestration workflow in the Foundry.":::
 
 ## Train your model
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Foundryにおけるオーケストレーションワークフローのアップデート"
}
```

### Explanation
このコードの変更は、Microsoft Foundryにおけるオーケストレーションワークフローに関する文書のアップデートです。主に、既存のLanguage Studioからのワークフロー移行手順が追加され、特定の手順についての説明が強化されました。また、いくつかの文の修正、情報の明確化が行われています。

具体的には、次のような重要な変更が含まれています：
- 日付が更新され、「ms.date: 02/03/2026」となっています。
- 「Language Studio」からの既存のワークフローをFoundryに移行するための2つのオプションが追加され、各オプションの手順が詳述されています。
- ワークフロー内でタスクを追加する機能や、タスクのリンクとアンリンクの手順が新たに説明されています。
- サンプルデータの取得方法が明確化され、使いやすさが向上しています。

全体的に、文書は拡充され、ユーザーにとっての理解を促進するための情報が追加されています。

## articles/ai-services/language-service/orchestration-workflow/media/orchestration-add-intent.png{#item-39d33d}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "オーケストレーションワークフローの意図追加に関する画像の追加"
}
```

### Explanation
このコードの変更は、Microsoft Foundryのオーケストレーションワークフローに関する文書に新しい画像ファイルが追加されたことを示しています。具体的には、"orchestration-add-intent.png"という名前の画像ファイルが追加されており、これはオーケストレーションワークフローでの意図を追加する手順に関連していると考えられます。

この画像の追加によって、ユーザーは視覚的に手順を理解しやすくなり、文書の内容がより明確になります。特に、オーケストレーションワークフローの設定やタスクのリンク方法についての理解が深まることが期待されます。画像は実際の操作画面を示すものと推測され、プロセスの各ステップを分かりやすく補完する役割を果たします。

## articles/ai-services/language-service/orchestration-workflow/media/orchestration-link-tasks.png{#item-c1ee06}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オーケストレーションワークフローのタスクリンクに関する画像の更新"
}
```

### Explanation
このコードの変更は、Microsoft Foundryのオーケストレーションワークフローに関連する画像ファイル"orchestration-link-tasks.png"が修正されたことを示しています。この画像は、おそらくオーケストレーションワークフローにおけるタスクのリンク方法を説明するために使われているもので、更新が行われた結果、視覚的な情報が改善されたと考えられます。

画像の内容が変更されることで、ユーザーはタスクのリンク手順をより理解しやすくなり、オーケストレーションワークフローの設定における具体的な指示が明確になります。画像の更新により、文書全体の品質と情報の可視性が向上し、実際の操作における支援が強化されることが期待されます。

## articles/ai-services/language-service/orchestration-workflow/media/orchestration-linked-tasks.png{#item-41c832}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "オーケストレーションワークフローのリンクされたタスクに関する画像の追加"
}
```

### Explanation
このコードの変更は、Microsoft Foundryのオーケストレーションワークフローに新しい画像ファイル"orchestration-linked-tasks.png"が追加されたことを示しています。この画像は、オーケストレーションワークフロー内でのタスクのリンクに関する視覚的な説明を提供することを目的としています。

新たに追加された画像によって、ユーザーはタスクの関連付けやリンクの手順をより理解しやすくなり、具体的な操作が明確になります。この視覚的要素は、ドキュメントの内容を補完し、特に複雑なワークフローを扱う際に役立つことが期待されます。追加された画像がどのように活用されるかによって、オーケストレーションの設定や管理がよりスムーズになるでしょう。

## articles/ai-services/language-service/orchestration-workflow/media/orchestration-no-tasks-warning.png{#item-0c5244}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "オーケストレーションワークフローのタスクがないことを警告する画像の追加"
}
```

### Explanation
このコードの変更は、Microsoft Foundryのオーケストレーションワークフローに関連する新しい画像ファイル"orchestration-no-tasks-warning.png"が追加されたことを示しています。この画像は、システムがタスクを検出できなかった場合に表示される警告メッセージを視覚的に示すために用いられます。

追加された画像は、ユーザーがタスクが存在しない場合の状況を理解しやすくし、適切な対応を促すための重要な要素です。この警告が視覚的に表現されることで、ワークフローの設定や実行において、エラーや不備を早期に察知できるようになり、ユーザーの体験が改善されることが期待されます。

## articles/ai-services/language-service/orchestration-workflow/media/orchestration-workflow-overview.png{#item-2b3cfd}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オーケストレーションワークフローの概要画像の修正"
}
```

### Explanation
このコードの変更は、Microsoft Foundryのオーケストレーションワークフローに関する画像ファイル"orchestration-workflow-overview.png"が修正されたことを示しています。具体的には、この画像はオーケストレーションワークフローの全体像を提供するものであり、機能やプロセスの理解を助けるために視覚的な情報を提供します。

修正の内容は具体的には示されていませんが、通常、このような変更は画像の解像度、内容の明確さ、色合い、またはラベルの正確さに関連していることが考えられます。修正が適用されることにより、ユーザーはオーケストレーションワークフローの理解をさらに深め、効果的に利用できるようになることが期待されます。

## articles/ai-services/language-service/orchestration-workflow/media/upload-utterances.png{#item-14f259}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "発話アップロード機能の画像の追加"
}
```

### Explanation
このコードの変更は、Microsoft Foundryにおける新しい画像ファイル"upload-utterances.png"が追加されたことを示しています。この画像は、ユーザーが発話データをアップロードする機能を説明するための視覚的なリソースです。

追加された画像は、発話をいかにしてシステムに取り込むかのプロセスを示し、ユーザーがインターフェースを使用する上での理解を深める手助けをします。このような視覚材料の導入により、ユーザーは操作手順を迅速に把握でき、発話アップロード機能を効率的に使用できるようになることが期待されます。

## articles/ai-services/language-service/orchestration-workflow/quickstart.md{#item-bee292}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 01/09/2026
+ms.date: 02/03/2026
 ms.author: lajanuar
 ms.custom: language-service-clu, mode-other
 zone_pivot_groups: foundry-rest-api
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートの日付の更新"
}
```

### Explanation
このコードの変更は、マークダウンファイル"quickstart.md"内の更新を示しています。具体的には、ドキュメントの最終更新日が2026年1月9日から2026年2月3日に変更されました。この変更は、文書が最新の情報を反映するためのものであり、ユーザーが正確な日時情報を把握できるようにしています。

更新日を修正することで、ユーザーはこのクイックスタートガイドがどれだけ最近のものであるかを確認でき、新しい機能や改善点が含まれている可能性に気づくことができます。これは、ドキュメントの整合性を保ちつつ、使用する際の信頼性を向上させるための重要なステップです。

## articles/ai-services/language-service/reference/migrate.md{#item-8a4128}

<details>
<summary>Diff</summary>
````diff
@@ -1,31 +1,85 @@
 ---
-title: "Migrate to Azure Language in Foundry Tools from: Language Understanding (LUIS), QnA Maker, and Text Analytics"
+title: "Migrate to Azure Language from Language Understanding (LUIS) or QnA Maker"
 titleSuffix: Foundry Tools
 description: Use this article to learn if you need to migrate your applications from Language Understanding (LUIS), QnA Maker, and Text Analytics.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: concept-article
-ms.date: 11/18/2025
+ms.date: 02/09/2026
 ms.author: lajanuar
 ---
-# Migrating to Azure Language in Foundry Tools
+<!-- markdownlint-disable MD025 -->
+# Migrate to Azure Language in Foundry Tools
 
 On November 2, 2021, Azure Language in Foundry Tools was released into public preview. Azure Language unifies the Text Analytics, QnA Maker, and Language Understanding (LUIS) service offerings, and provides several new features as well.
 
-## Do I need to migrate to Azure Language if I'm using Text Analytics?
+> [!IMPORTANT]
+>
+> * You may experience intermittent interruptions when calling the Language Understanding (LUIS) service. Microsoft is in the final phase of retiring LUIS. These interruptions are temporary but expected during this retirement phase.
+> * Beginning March 31, 2026, LUIS runtime and authoring endpoints (including REST API calls) are fully retired, and all LUIS requests fail.
+> * To ensure uninterrupted operation, export all of your LUIS app data as soon as possible in order to:
+>   * Start using [Conversational Language Understanding (CLU)](../conversational-language-understanding/overview.md), or
+>   * Try out a [Microsoft Foundry](../conversational-language-understanding/quickstart.md).
+> * Use the following API to export your data: [LUIS Versions - Export](/rest/api/luis/versions/export?view=rest-luis-v2.0&preserve-view=true&tabs=HTTP).
 
-Text Analytics is incorporated into Azure Language, and its features are still available. If you're using Text Analytics features, your applications should continue to work without breaking changes. If you're using Text Analytics API (v2.x or v3), see the [Text Analytics migration guide](migrate-language-service-latest.md) to migrate your applications to the unified Language endpoint and the latest client library.
+## How do I migrate to Azure Language if I'm using Language Understanding (LUIS)?
 
-Consider using one of the available quickstart articles to see the latest information on service endpoints, and API calls.
+If you're using Language Understanding (LUIS), you can [import your Language Understanding (LUIS) JSON file](../conversational-language-understanding/how-to/fail-over.md#import-to-a-new-project) to the new Conversational language understanding feature:
 
-## How do I migrate to Azure Language if I'm using Language Understanding (LUIS)?
+1. Export the LUIS app
+
+   * Export your LUIS application as JSON by using the LUIS authoring APIs or the LUIS portal.
+   * LUIS Versions – [Export REST API](/rest/api/luis/versions/export?view=rest-luis-v2.0&preserve-view=true&tabs=HTTP)
+
+1. Map LUIS data to the CLU schema
+
+   * Update the exported JSON to align intents, entities, and utterances with the CLU project schema.
+   * [Conversational Language Understanding overview](../conversational-language-understanding/overview.md) provides details on the CLU schema and supported features.
 
-If you're using Language Understanding (Language Understanding (LUIS)), you can [import your Language Understanding (LUIS) JSON file](../conversational-language-understanding/how-to/migrate-from-Language Understanding (LUIS).md) to the new Conversational language understanding feature.
+1. Create a CLU project and import data
+
+   * Create a CLU project and import the prepared data by using Language Studio or the CLU authoring APIs.
+   * [CLU quickstart (REST API)](../conversational-language-understanding/quickstart.md?pivots=rest-api) provides instructions on creating a CLU project and importing data.
+
+1. Train the model
+
+   * Start a training job to build the CLU model from the imported data.
+   * [Train and evaluate a CLU model](../conversational-language-understanding/how-to/train-model.md) provides details on training and evaluating your CLU model.
+
+1. Test the model
+
+   * Send test utterances to the CLU prediction endpoint and verify intent and entity results.
+   * [Conversational Language Understanding overview](../conversational-language-understanding/how-to/call-api.md) provides details on querying your CLU model.
 
 ## How do I migrate to Azure Language if I'm using QnA Maker?
 
-If you're using QnA Maker, see the [migration guide](/previous-versions/azure/ai-services/qnamaker/overview/overview) for information on migrating knowledge bases from QnA Maker to question answering.
+If you're using QnA Maker, you can [import your QnA Maker knowledge base](../question-answering/how-to/migrate-knowledge-base.md#import-a-project) to the custom question answering (CQA) feature:
+
+1. Export the QnA Maker knowledge base
+
+   * Download your knowledge base by using the QnA Maker REST APIs with your endpoint key and knowledge base ID.
+   * [QnA Maker REST API reference](/rest/api/questionanswering/question-answering-projects/export?view=rest-questionanswering-2021-10-01&preserve-view=true&tabs=HTTP) provides instructions on exporting your knowledge base.
+
+1. Create a Custom Question Answering project
+
+   * Create a new Custom Question Answering project.
+   * [Create a Custom Question Answering project](../question-answering/quickstart/sdk.md) provides instructions on creating a CQA project.
+
+1. Import the knowledge base
+
+   * Import the exported knowledge base file into your Custom Question Answering project.
+   * [Import knowledge base](../question-answering/how-to/authoring.md#import-project) provides instructions on importing your knowledge base.
+   * For more information, see also, [Move projects and question answer pairs](../question-answering/how-to/migrate-knowledge-base.md).
+
+1. Create and test a knowledge base
+
+   * Create, test, and deploy a custom question answering knowledge base in the Microsoft Foundry (classic) Language playground.
+   * [Create, test, and deploy: CQA knowledge base](../question-answering/how-to/create-test-deploy.md) provides instructions on creating and testing your project.
+
+
+Consider using one of the available quickstart articles to see the latest information on service endpoints, and API calls.
+
 
 ## See also
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "移行ガイドの内容の更新"
}
```

### Explanation
このコードの変更は、"migrate.md"ファイルの内容が大幅に修正されたことを示しています。主な変更点には、記事のタイトルの簡略化、新しい移行手順の追加、重要な情報としてLUISサービスの廃止に関する注意喚起が含まれています。

具体的には、移行ガイドでは、Language Understanding (LUIS) や QnA MakerからAzure Languageへの移行方法についての詳細が提供され、具体的なステップや必要なアクションが示されています。また、LUISサービスの完全廃止日や中断の可能性についても明記され、ユーザーにとってのリスクを軽減する情報が強調されています。

この更新により、ユーザーは最新の情報を基に、スムーズにシステムを移行できるようにサポートされています。さらに、関連するリソースへのリンクも加えられており、ユーザーが必要な手順を簡単に追うことができるようになっています。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -816,7 +816,7 @@ items:
           href: ../speech-service/call-center-quickstart.md?context=%2fazure%2fai-services%2flanguage-service%2fcontext%2fcontext
         - name: Ingestion Client
           href: ../speech-service/ingestion-client.md?context=%2fazure%2fai-services%2flanguage-service%2fcontext%2fcontext
-- name: Reference
+- name: API reference
   items:
   - name: REST API
     href: /rest/api/language/
@@ -936,12 +936,12 @@ items:
         href: concepts/encryption-data-at-rest.md
       - name: Compliance and certification
         href: https://azure.microsoft.com/support/legal/cognitive-services-compliance-and-privacy/
-- name: Reference
+- name: Migration and release history
   items:
-    - name: Migrate from LUIS, QnA Maker, and Text Analytics
+    - name: Migrate from LUIS or QnA Maker to Language Service
       displayName: text analytics, luis, qna
       href: reference/migrate.md
-    - name: Migrate from Text Analytics API to Language Service API
+    - name: Migrate from Text Analytics API to Language Service
       displayName: api versions, versioning
       href: reference/migrate-language-service-latest.md
     - name: Azure Language release history
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCファイルの項目名の変更"
}
```

### Explanation
このコードの変更は、"toc.yml"ファイルのいくつかの項目名の修正を示しています。主な改訂内容は、セクションの名称を変更している点です。「Reference」という項目名が「API reference」に変更され、さらに新たに「Migration and release history」としてのセクションが追加されました。

具体的には、移行に関するドキュメントやAPIのバージョン管理に関連する情報がより明確に提示されるようになりました。項目名がより具体的になり、ユーザーが必要なリソースを迅速に見つけられるようにするための工夫が施されています。

これによって、ドキュメント全体の構造が改善され、利用者がトピックを素早く把握し、関連する情報へ容易にアクセスできるようになることが期待されます。このような小規模な更新は、ユーザーのナビゲーション体験を向上させるために重要です。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -6,14 +6,26 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: whats-new
-ms.date: 01/14/2026
+ms.date: 02/09/2026
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD025 -->
 # What's new in Azure Language in Foundry Tools?
 
 Stay informed about recent releases and enhancements designed to help you get the most out of Azure Language capabilities. Azure Language in Foundry Tools is updated on an ongoing basis. Bookmark this page and stay up to date with release notes, feature enhancements, and our newest documentation.
 
+## February 2026
+
+* **Text PII detection quality improvement**. Backend validation for the Phone Number entity type is updated to broaden detection coverage, resulting in improved recall across supported languages. This change is applied at the service level and requires no updates to your API calls or request parameters.
+
+* **Orchestration workflow playground update**. The Foundry playground experience for orchestration workflow introduces a redesigned task-linking interface. The **Schema definition** page previously available in Language Studio is replaced by the **Configure orchestration** page, which provides a streamlined way to associate fine-tuning tasks with an orchestration workflow task. For more information, see the [Orchestration workflow quickstart](orchestration-workflow/quickstart.md).
+
+* **Language Studio retirement**. Azure Language Studio is scheduled for retirement on **March 20, 2027**. After that date, the Language Studio portal is no longer accessible, but your existing projects, data, and service endpoints remain unaffected. All features and new enhancements are available in Microsoft Foundry. For step-by-step migration instructions, see [Migrate from Language Studio to Microsoft Foundry](migration-studio-to-foundry.md).
+
+* **Foundry (classic) Language playground card is generally available**. The Language playground card in [Microsoft Foundry (classic)](https://ai.azure.com/) exits preview and is now generally available. You can access all Language authoring, testing, and deployment capabilities directly from the playground without any feature restrictions.
+
+* **LUIS migration guidance**. To migrate from **LUIS** to [Conversational Language Understanding (CLU)](conversational-language-understanding/overview.md), see [Migrating to Azure Language in Foundry Tools](reference/migrate.md) for the latest instructions.
+
 ## January 2026
 
 * **Orchestration workflow available in [Microsoft Foundry (classic)](https://ai.azure.com/)**. [Orchestration workflow](orchestration-workflow/quickstart.md) is now supported in Microsoft Foundry (classic).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Languageの新機能の追加"
}
```

### Explanation
このコードの変更は、"whats-new.md"ファイルに新機能や更新情報が追加されたことを示しています。主な更新点は、2026年2月に行われた複数のリリースや拡張についての情報が含まれています。

具体的な変更点としては、以下の内容が新たに追加されています：
- **テキストPII（個人識別情報）検出の品質向上**：電話番号エンティティタイプの後方検証が更新され、言語全体での検出範囲が広がり、リコールが改善されました。
- **オーケストレーションワークフロープレイグラウンドの更新**：新しいタスクリンクインターフェースが導入され、効率的にタスクを関連付けるためのページが改良されています。
- **Language Studioの廃止予定**：2027年3月20日にLanguage Studioが廃止されることが告知され、その後も既存のプロジェクトやデータは影響を受けないことが述べられています。
- **Foundry (classic)のLanguageプレイグラウンドカードが一般公開**：プレイグラウンドでのすべての言語の作成、テスト、デプロイ機能に制限なしでアクセスできるようになりました。
- **LUISからの移行ガイダンスの提供**：LUISからConversational Language Understanding (CLU) への移行手順が最新情報として案内されています。

これにより、ユーザーはAzure Languageの最新の機能や変更点に迅速にアクセスでき、必要なアクションをとるための有用な情報が得られるようになっています。


