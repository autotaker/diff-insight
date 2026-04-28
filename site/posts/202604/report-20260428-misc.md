---
date: '2026-04-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c00df72...MicrosoftDocs:6f9c768
summary: このコードの変更では、AzureのドキュメントインテリジェンスとAI Foundryサービスに関する最新の情報と機能が強化され、ユーザーが新しいAPIとポータルをより効果的に活用できるようにガイドが更新されました。主な内容として、新しいAPIバージョンのタイムラインや、新Foundryポータルの機能が詳述され、PII検出に関する視覚的なサポートが追加されています。また、古い情報が削除され、新ポータルへの移行が促され、全体的にユーザーの利用体験が向上しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c00df72...MicrosoftDocs:6f9c768){target="_blank"}

<format>
# ハイライト
このコードの変更では、AzureのドキュメントインテリジェンスとAI Foundryサービスに関する最新の情報および機能が強化され、ユーザーが新しいAPIとポータルをより効果的に活用できるようにガイドが更新されました。特に、新しいAPIバージョンのタイムラインや、新Foundryポータルの機能が詳述されています。また、新たに追加された画像によって、ユーザーの理解が深まるようになっています。

## 新機能
- Azure AI Foundryの新しい会話検出とテキスト検出に関する画像が追加され、ユーザーがPIIを視覚的に検出する方法が補完されました。

## 破壊的変更
- Azure AI Servicesの旧Foundryポータルに関する情報が削除され、新しいFoundryポータルへの移行が促されています。

## その他の更新
- ドキュメントインテリジェンスのAPIバージョンの引退に関する情報が追加され、最新のリリース情報が提供されています。
- PII検出に関する既存のドキュメントが改訂され、タイトルと説明がより簡潔に表現されています。
- 日付や細かい内容についても更新が行われています。

# 洞察
今回のアップデートは主に、Azure AIの機能をより最新の状態に保つためのマイナーな更新により、ユーザーがより直感的にサービスを利用できるようにガイドを整備したことにあります。

まず、ドキュメントインテリジェンスに関しては、古いプレビューAPIバージョンの引退スケジュールが明示され、新しいAPIバージョンへの移行を念頭に置いたガイドへと改訂されています。これにより、企業や開発者は長期的な計画を立てやすくなるでしょう。

次に、Azure AI Foundryポータルについては、クラシックポータルから新ポータルへの移行が進められています。特に、PIIの検出機能が強化されており、ユーザーはテキストおよび会話データから個人を特定できる情報を検出する手順を、既存の文書や追加された画像を通じて理解しやすくなっています。これにより、プライバシー保護を重視する現代の要件に沿った形で、技術的価値を提供しています。

また、クイックスタートガイドの更新は、複雑な手順を簡単に理解できるようにするため、タイトルや説明を簡潔にすると同時に、最新の日付情報を反映しており、ドキュメントの整合性とユーザー体験の向上を目的としています。

全体として、このアップデートにより、ユーザーがAzure AIサービスをより効果的に活用できるようになり、技術の採用と移行がスムーズになったと言えるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [whats-new.md](#item-1ec8d3) | minor update | ドキュメントインテリジェンスのアップデートについての変更 | modified | 1 | 11 | 12 | 
| [azure-ai-foundry.md](#item-ff89fc) | minor update | Azure AI Foundryに関するクイックスタートの更新 | modified | 149 | 111 | 260 | 
| [new-foundry-conversation-detection.png](#item-e850af) | new feature | 新しいFoundryの会話検出に関する画像の追加 | added | 0 | 0 | 0 | 
| [new-foundry-text-detection.png](#item-9d2951) | new feature | 新しいFoundryのテキスト検出に関する画像の追加 | added | 0 | 0 | 0 | 
| [quickstart.md](#item-94affd) | minor update | PII検出に関するクイックスタートのタイトルと説明の修正 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -25,18 +25,8 @@ ms.custom:
 Document Intelligence service is updated on an ongoing basis. Bookmark this page to stay up to date with release notes, feature enhancements, and our newest documentation.
 
 > [!IMPORTANT]
-> Preview API versions are retired once the GA API is released. The 2023-02-28-preview API version is retiring. If you're still using the preview API or the associated SDK versions, update your code to target the latest API version `2024-11-30 (GA)`. </br>
+> Preview API versions will be retired by 06/30/2026, and v3.0 `2022-08-31 (GA)` API will be retired by 03/30/2029. If you're still using a preview API or the associated SDK versions, update your code to target the latest API version `2024-11-30 (GA)`. </br>
 
-**Content Understanding: The Next Step Forward for Document Intelligence**
-</br>
-In November 2025, the GA version of **Content Understanding** was released (**2025-11-01** API version). Content Understanding is an evolution of Document Intelligence that expands multimodal processing capabilities to support text, images, audio, and video content types.
-
-Key features include:
-
-* **Multimodal content analysis**. Process and extract insights from text, images, audio, and video within a unified API framework.
-* **Enhanced AI integration**. Seamlessly integrate with Azure AI services for intelligent content processing and decision-making workflows.
-* **Flexible deployment options**. Build applications, automate document workflows, or enable AI-driven analytics with scalable cloud infrastructure.
-* **Unified content extraction**. Utilize a single service to handle diverse content types, reducing complexity and improving operational efficiency.
 
 ## March 2026
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのアップデートについての変更"
}
```

### Explanation
このコードの変更は、ドキュメントインテリジェンスに関する最新情報の文書を更新することを目的としています。主な変更点は、プレビューAPIバージョンの引退に関する情報の更新です。具体的には、古いプレビューAPIバージョンが2026年6月30日までに引退し、2022年8月31日公開版のAPIが2029年3月30日に引退することを明記しています。また、内容理解機能に関する旧情報を削除し、主要な機能やリリース情報に関して最新の情報を反映させています。この修正は、ユーザーが最新のAPIバージョンへアップデートする際のガイダンスを明確にするためのものであり、ドキュメントの内容を簡潔かつ効果的に保つことを目的としています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/azure-ai-foundry.md{#item-ff89fc}

<details>
<summary>Diff</summary>
````diff
@@ -3,17 +3,16 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 02/06/2026
+ms.date: 04/27/2026
 ms.author: lajanuar
-ms.custom: language-service-pii
-ai-usage: ai-assisted
+ms.custom: doc-kit-assisted
 ---
 
 ## Prerequisites
 
 > [!TIP]
 >
-> * If you already have an Azure Language in Foundry Tools or multi-service resource—whether used on its own or through Language Studio—you can continue to use those existing Language resources within the Microsoft Foundry portal. 
+> * If you already have an Azure Language in Foundry Tools or multi-service resource—whether used on its own or through Language Studio—you can continue to use those existing Language resources within the Microsoft Foundry portal.
 > * For more information, see [Connect services in the Microsoft Foundry portal](../../../../connect-services-foundry-portal.md).
 > * Consider using a Foundry resource for the best experience. You can also follow these instructions with a Language resource.
 
@@ -22,171 +21,210 @@ ai-usage: ai-assisted
 * **Foundry resource**. Create a [Foundry resource](../../../../multi-service-resource.md) or see [Configure a Foundry resource](../../../concepts/configure-azure-resources.md). Alternatively, you can use a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
 * **A Foundry project**. For more information, see [Create a Foundry project](../../../../../ai-foundry/how-to/create-projects.md).
 
-
-### [Foundry (classic)](#tab/foundry-classic)
+### [Foundry (new)](#tab/foundry-new)
 
 > [!NOTE]
-> This content refers to the [Foundry (classic)](https://ai.azure.com/) portal, which supports hub-based projects and other resource types. To confirm that you're using Foundry (classic), make sure the version toggle in the portal banner is in the **off** position. :::image type="icon" source="../../media/quickstarts/azure-ai-foundry/classic-foundry.png" border="false":::
-
+> This content refers to the [Foundry (new)](https://ai.azure.com/) portal, which supports only [Foundry projects](../../../../../ai-foundry/what-is-foundry.md) and provides streamlined access to models, agents, and tools. To confirm that you're using Foundry (new), make sure the version toggle in the portal banner is in the **on** position. :::image type="icon" source="../../media/quickstarts/azure-ai-foundry/new-foundry.png" border="false":::
 
-You can use [Foundry (classic)](https://ai.azure.com/) to:
+You can use [Foundry (new)](https://ai.azure.com/) to:
 
 > [!div class="checklist"]
-> * Extract PII from conversations
-> * Extract PII from text
-> * Configure redaction policies
+>
+> * Extract personally identifiable information (PII) from text
+> * Configure redaction policies and excluded values
 > * Review detected entities and confidence scores
 
+## Navigate to the Foundry (new) playground
 
-## Navigate to the Foundry (classic) playground
+The active project appears in the upper-left corner. To create a new project:
 
-1. In the left pane, select **Playgrounds**.
-1. Select the **Try Azure Language Playground** button.
+1. Open the project drop-down menu.
+1. Enter a project name or select an existing one.
+1. Select **Create project**.
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/foundry-playground-navigation.png" alt-text="Screenshot showing the Playgrounds navigation and the Try Azure Language Playground button in Foundry (classic)." lightbox="../../media/quickstarts/azure-ai-foundry/foundry-playground-navigation.png":::
+   :::image type="content" source="../../../media/new-foundry-homepage.png" alt-text="Screenshot of the Foundry (new) homepage.":::
 
-## Detect PII in the Foundry playground
+There are two ways to access the personally identifiable information (PII) interface:
 
-The **Language Playground** consists of four sections:
+1. Select the **Discover** tab from the upper right navigation bar to go to the **Models** page.
+   * In the search bar under models, enter **Azure** and press enter.
+   * Next, select **Azure-Language-Text-PII redaction** from the search results.
+   * Finally, select the **Open in Playground** button.
 
-| Section | Purpose |
-| --- | --- |
-| **Top banner** | Select the input language and choose a PII detection capability. |
-| **Left pane** | Set **Configuration** options such as API version, model version, and redaction policy. |
-| **Center pane** | Enter text for processing and review highlighted results. |
-| **Right pane** | View **Details** for each detected entity. |
+1. Select the  **Build** tab from the upper right navigation bar.
+   * From the left navigation bar, select  **Models**.
+   * Select the **AI services** tab.
+   * Next, select **Azure-Language-Text-PII redaction** to go to the playground.
 
-Select either **Extract PII from conversation** or **Extract PII from text** from the top banner tiles. Each capability targets a different scenario.
+## Extract  PII from text
 
-### Extract PII from conversation
+The **Azure-Language-Text-PII redaction** model is used to identify and redact personally identifiable information in text. The interface provides configuration options to customize your detection and redaction preferences, as well as detailed output to review the detected entities and their confidence scores.
 
-**Extract PII from conversation** is designed to identify and mask personally identifiable information in conversational text.
+1. On the **Playground** tab, select **Azure Language—Text PII redaction** from the drop-down menu.
 
-In **Configuration** there are the following options:
+1. Select the sample text, use the paperclip icon to upload your text, or enter your own text.
 
-|Option              |Description                              |
-|--------------------|-----------------------------------------|
-|Select API version  | Select which version of the API to use.    |
-|Select model version| Select which version of the model to use.|
-|Select text language| Select the language of your input text.|
-|Select types to include| Select the types of information you want to redact.|
-|Specify redaction policy| Select the method of redaction.|
-|Specify redaction character| Select the character used for redaction. Only available with the **CharacterMask** redaction policy.|
+1. In the **Configure** side panel, you can set the following options:
 
-After the operation completes, each detected entity is highlighted in the center pane with its type label displayed beneath it.
+    | Option | Description |
+    | --- | --- |
+    | **API version** | Select the API version that you prefer to use. |
+    | **Model version** | Select the model version that you prefer to use. |
+    | **Language** | Select the language in which your source text is written. |
+    | **Select types to include** | Select the PII types you want to redact. |
+    | **Value to exclude** | Specify values that you want to exclude from detection. For example, if you want to redact email addresses but want to exclude ones from a specific domain, you can enter that domain as an excluded value. |
+    | **Synonyms** | Provide alternative names for specific entity types. For example, if you select enter "Microsoft" as an excluded value, you can also specify specific synonyms such as `MSFT` and `Microsoft Corporation`. |
+    | **Policy type** | Choose the type of redaction policy to apply (character mask, entity mask, or no mask). |
 
-The **Details** section contains the following fields for each entity:
+1. After you make your selections, choose the **Detect** button. Detected entities are highlighted in the text and you can review the accompanying details in formatted text or as a JSON response.
 
-|Field | Description                |
-|------|----------------------------|
-|Entity|The detected entity.|
-|Category| The entity type that was detected.|
-|Offset| The number of characters from the beginning of the line to the entity.|
-|Length| The character length of the entity.|
-|Confidence| The model's level of certainty that the entity type is correct.|
+    :::image type="content" source="../../media/quickstarts/azure-ai-foundry/new-foundry-text-detection.png" alt-text="Screenshot of PII text detection output in the Foundry playground." lightbox="../../media/quickstarts/azure-ai-foundry/new-foundry-text-detection.png":::
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/conversation-pii.png" alt-text="A screenshot showing detected PII entities highlighted in a conversation with entity details displayed in the right pane of the Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/conversation-pii.png":::
+    | Field | Description |
+    | --- | --- |
+    | **Type** | The detected type. |
+    | **Confidence** | The model's level of certainty regarding whether it correctly identified an entity type. |
+    | **Offset** | The number of characters that the entity was detected from the beginning of the text. |
+    | **Length** | The character length of the entity. |
 
-Verify that each PII entity appears highlighted with the correct category label. If no entities appear, check that the input text contains recognizable PII patterns and that the **Types** filter includes the expected categories.
+Verify that the detected entities match the PII in your input text. You can use the **Edit** button to modify the **Configure** parameters and rerun detection as needed.
 
-### Extract PII from text
+## Extract  PII from conversations 🆕
 
-**Extract PII from text** is designed to identify and mask personally identifiable information in text.
+The **extract PII from conversations** feature detects and masks personally identifying information within conversational text. This feature is designed to handle the unique structure and context of conversations, such as dialogues or chat logs.
 
-In **Configuration** you can select from the following options:
+1. On the **Playground** tab, select **Azure Language—Conversational PII redaction** from the drop-down menu.
 
-|Option              |Description                              |
-|--------------------|-----------------------------------------|
-|Select API version  | Select which version of the API to use.    |
-|Select model version| Select which version of the model to use.|
-|Select text language| Select the language of your input text.|
-|Select types to include| Select the types of information you want to redact.|
-|Specify redaction policy| Select the method of redaction.|
-|Specify redaction character| Select the character used for redaction. Only available with the **CharacterMask** redaction policy.|
+1. Select a sample transcript, use the paperclip icon to upload your transcript, or input conversation turn text.
 
-After the operation completes, each detected entity is highlighted in the center pane with its type label displayed beneath it.
+1. Format your conversation with each turn on a new line and include speaker labels if possible. If participant ID, colon, message, or new line are not used consistently, the output may be unexpected. Here's an example of well-formatted conversation text:
 
-The **Details** section contains the following fields for each entity:
+    ```text
+    Speaker 1: Hello, how are you?
+    Speaker 2: I'm good, thank you! How about you?
+    Speaker 1: I'm doing well, thanks for asking.
+    ```
 
-|Field | Description                |
-|------|----------------------------|
-|Entity|The detected entity.|
-|Category| The entity type that was detected.|
-|Offset| The number of characters from the beginning of the line to the entity.|
-|Length| The character length of the entity.|
-|Confidence| The model's level of certainty that the entity type is correct.|
-|Tags| The model's confidence scores for each identified entity subtype.|
+1. In the **Configure** side panel, set your preferred options for API version, model version, language, types, redaction policy, and excluded values.
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/text-pii.png" alt-text="A screenshot showing detected PII entities highlighted in text with entity details and confidence scores displayed in the right pane of the Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/text-pii.png":::
+    | Option | Description |
+    | --- | --- |
+    | **API version** | Select the API version that you prefer to use. |
+    | **Model version** | Select the model version that you prefer to use. |
+    | **Language** | Select the language in which your source text is written. |
+    | **Select types to include** | Select the PII types you want to redact. |
+    | **Specify redaction character** | Choose the character used to mask sensitive text. |
 
-Verify that each PII entity appears highlighted with the correct category label. The **Tags** column shows subcategory confidence scores when applicable.
+1. After you make your selections, choose the **Detect** button. Detected entities are highlighted in the text and you can review the accompanying details in formatted text or as a JSON response.
 
-### [Foundry (new)](#tab/foundry-new)
+    :::image type="content" source="../../media/quickstarts/azure-ai-foundry/new-foundry-conversation-detection.png" alt-text="Screenshot of PII conversation detection output in the Foundry playground." lightbox="../../media/quickstarts/azure-ai-foundry/new-foundry-conversation-detection.png":::
 
-> [!NOTE]
-> This content refers to the [Foundry (new)](https://ai.azure.com/) portal, which supports only [Foundry projects](../../../../../ai-foundry/what-is-foundry.md) and provides streamlined access to models, agents, and tools. To confirm that you're using Foundry (new), make sure the version toggle in the portal banner is in the **on** position. :::image type="icon" source="../../media/quickstarts/azure-ai-foundry/new-foundry.png" border="false":::
+    | Field | Description |
+    | --- | --- |
+    | **Type** | The detected type. |
+    | **Confidence** | The model's level of certainty regarding whether it correctly identified an entity type. |
+    | **Offset** | The number of characters that the entity was detected from the beginning of the text. |
+    | **Length** | The character length of the entity. |
 
+Verify that the detected entities match the PII in your input conversation. You can use the **Edit** button to modify the **Configure** parameters and rerun detection as needed.
 
-You can use [Foundry (new)](https://ai.azure.com/) to:
+### [Foundry (classic)](#tab/foundry-classic)
+
+> [!NOTE]
+> This content refers to the [Foundry (classic)](https://ai.azure.com/) portal, which supports hub-based projects and other resource types. To confirm that you're using Foundry (classic), make sure the version toggle in the portal banner is in the **off** position. :::image type="icon" source="../../media/quickstarts/azure-ai-foundry/classic-foundry.png" border="false":::
+
+You can use [Foundry (classic)](https://ai.azure.com/) to:
 
 > [!div class="checklist"]
+>
+> * Extract PII from conversations
 > * Extract PII from text
-> * Configure redaction policies and excluded values
+> * Configure redaction policies
 > * Review detected entities and confidence scores
 
+## Navigate to the Foundry (classic) playground
 
-## Navigate to the Foundry (new) playground
+1. In the left pane, select **Playgrounds**.
+1. Select the **Try Azure Language Playground** button.
 
-The active project appears in the upper-left corner. To create a new project:
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/foundry-playground-navigation.png" alt-text="Screenshot showing the Playgrounds navigation and the Try Azure Language Playground button in Foundry (classic)." lightbox="../../media/quickstarts/azure-ai-foundry/foundry-playground-navigation.png":::
 
-1. Open the project drop-down menu.
-1. Enter a project name or select an existing one.
-1. Select **Create project**.
+## Detect  PII in the Foundry playground
 
-   :::image type="content" source="../../../media/new-foundry-homepage.png" alt-text="Screenshot of the Foundry (new) homepage":::
+The **Language Playground** consists of four sections:
 
+| Section | Purpose |
+| --- | --- |
+| **Top banner** | Select the input language and choose a  PII detection capability. |
+| **Left pane** | Set **Configuration** options such as API version, model version, and redaction policy. |
+| **Center pane** | Enter text for processing and review highlighted results. |
+| **Right pane** | View **Details** for each detected entity. |
 
-There are two ways to access the PII interface:
+Select either **Extract PII from conversation** or **Extract PII from text** from the top banner tiles. Each capability targets a different scenario.
 
-1. Select the **Discover** tab from the upper right navigation bar to go to the **Models** page.
-   * In the search bar under models, enter **Azure** and press enter.
-   * Next, select **Azure-Language-Text-PII redaction** from the search results.
-   * Finally, select the **Open in Playground** button.
+### Extract  PII text
 
-1. Select the  **Build** tab from the upper right navigation bar.
-   * From the left navigation bar, select  **Models**.
-   * Select the **AI services** tab.
-   * Next, select **Azure-Language-Text-PII redaction** to go to the playground.
+**Extract PII from text** is designed to identify and mask personally identifying information in text.
+
+In **Configuration** you can select from the following options:
+
+| Option | Description |
+| --- | --- |
+| Select API version | Select which version of the API to use. |
+| Select model version | Select which version of the model to use. |
+| Select text language | Select the language of your input text. |
+| Select types to include | Select the types of information you want to redact. |
+| Specify redaction policy | Select the method of redaction. |
+| Specify redaction character | Select the character used for redaction. Only available with the **CharacterMask** redaction policy. |
+
+After the operation completes, each detected entity is highlighted in the center pane with its type label displayed beneath it.
 
+The **Details** section contains the following fields for each entity:
 
-## Detect PII in the Foundry playground
+| Field | Description |
+| --- | --- |
+| Entity | The detected entity. |
+| Category | The entity type that was detected. |
+| Offset | The number of characters from the beginning of the line to the entity. |
+| Length | The character length of the entity. |
+| Confidence | The model's level of certainty that the entity type is correct. |
+| Tags | The model's confidence scores for each identified entity subtype. |
 
-The **extract PII from text** feature detects and masks personally identifiable information within written content.
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/text-pii.png" alt-text="A screenshot showing detected PII entities in text displayed in the Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/text-pii.png":::
 
-1. On the **Playground** tab, select the sample text, use the paperclip icon to upload your text, or enter your own text.
+Verify that each PII entity appears highlighted with the correct category label. The **Tags** column shows subcategory confidence scores when applicable.
+
+### Extract  PII conversations
 
-1. Select the **Configure** button. In the **Configure** side panel, set the following options:
+**Extract PII from conversation** is designed to identify and mask personally identifying information in conversational text.
+
+In **Configuration** there are the following options:
 
 | Option | Description |
-|--|--|
-| **API version** | Select the API version that you prefer to use. |
-| **Model version** | Select the model version that you prefer to use. |
-| **Language** | Select the language in which your source text is written. |
-| **Types** | Select the types of information you want to redact. |
-| **Specify redaction policy** | Select the method of redaction. |
-| **Excluded values** | Select the values that you want to exclude. |
-| **Synonyms** | Select a category for your redaction type values to target related synonyms. |
+| --- | --- |
+| Select API version | Select which version of the API to use. |
+| Select model version | Select which version of the model to use. |
+| Select text language | Select the language of your input text. |
+| Select types to include | Select the types of information you want to redact. |
+| Specify redaction policy | Select the method of redaction. |
+| Specify redaction character | Select the character used for redaction. Only available with the **CharacterMask** redaction policy. |
 
-After you make your selections, choose the **Detect** button. Detected entities are highlighted in the text and you can review the accompanying details in formatted text or as a JSON response:
+After the operation completes, each detected entity is highlighted in the center pane with its type label displayed beneath it.
 
-> [!NOTE]
-> The Foundry (new) playground currently supports **text PII** detection. For **conversation PII**, use the **Foundry (classic)** tab.
+The **Details** section contains the following fields for each entity:
 
 | Field | Description |
-|--|--|
-| **Type** | The detected type. |
-| **Confidence** | The model's level of certainty regarding whether it correctly identified an entity type. |
-| **Offset** | The number of characters that the entity was detected from the beginning of the text. |
-| **Length** | The character length of the entity. |
+| --- | --- |
+| Entity | The detected entity. |
+| Category | The entity type that was detected. |
+| Offset | The number of characters from the beginning of the line to the entity. |
+| Length | The character length of the entity. |
+| Confidence | The model's level of certainty that the entity type is correct. |
 
-Verify that the detected entities match the PII in your input text. You can use the **Edit** button to modify the **Configure** parameters and rerun detection as needed.
\ No newline at end of file
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/conversation-pii.png" alt-text="A screenshot showing detected PII entities highlighted in a conversation with entity details displayed in the right pane of the Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/conversation-pii.png":::
+
+Verify that each PII entity appears highlighted with the correct category label. If no entities appear, check that the input text contains recognizable PII patterns and that the **Types** filter includes the expected categories.
+
+
+
+---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryに関するクイックスタートの更新"
}
```

### Explanation
このコードの変更は、Azure AI Foundryに関するクイックスタートガイドの内容を更新することを意図しています。大きな変更点としては、日付の更新、コンテンツの整理、及び新しいFoundryポータルに関連する情報が追加されています。古いFoundry（クラシック）ポータルに関する情報は削除され、新しいFoundryポータルの機能と使用方法に焦点が当てられています。また、プライバシーに配慮した情報（PII）検出に関する手順が明確化され、テキストだけでなく会話からのPIIの抽出方法も詳しく説明されています。

具体的には、ユーザーが新しいFoundryポータルを使用して、各種設定を行い、PIIを検出する方法が詳細に述べられており、特に会話形式でのデータ処理に関する手順が重要なポイントとなっています。新しい構成オプションや各種設定が充実しており、ユーザーがより効果的にAzure AIの機能を活用できるようになっています。

## articles/ai-services/language-service/personally-identifiable-information/media/quickstarts/azure-ai-foundry/new-foundry-conversation-detection.png{#item-e850af}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しいFoundryの会話検出に関する画像の追加"
}
```

### Explanation
このコードの変更は、Azure AI Foundryの新しい会話検出機能に関連する画像を追加することを目的としています。追加された画像は、ユーザーが会話データ内の個人を特定できる情報（PII）を検出する際のインターフェースを視覚的に示しています。この画像は、クイックスタートガイドや関連するドキュメント内での説明を補完し、ユーザーが新しい機能をより直感的に理解できるようにするためのものです。この変更により、関連する内容がより具体的で視覚的に理解しやすくなり、ユーザーエクスペリエンスが向上します。

## articles/ai-services/language-service/personally-identifiable-information/media/quickstarts/azure-ai-foundry/new-foundry-text-detection.png{#item-9d2951}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しいFoundryのテキスト検出に関する画像の追加"
}
```

### Explanation
このコードの変更は、Azure AI Foundryの新しいテキスト検出機能に関連する画像を追加することを目的としています。この画像は、ユーザーがテキストデータ内の個人を特定できる情報（PII）を検出するためのインターフェースを視覚的に示しており、クイックスタートガイドや関連ドキュメントの内容を補完します。この変更によって、ユーザーは新しい機能をより直感的に理解できるようになり、システムの利用が容易になります。画像の追加は、文書全体の有用性を向上させるための重要な要素です。

## articles/ai-services/language-service/personally-identifiable-information/quickstart.md{#item-94affd}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ---
-title: "Quickstart: Detect personally identifiable information (PII) in text"
+title: "Quickstart: Detect personally identifiable information (PII)"
 titleSuffix: Foundry Tools
-description: Use Azure Language in Foundry Tools to detect and redact personally identifiable information (PII) in text with client libraries, the REST API, or the Microsoft Foundry portal.
+description: Use Azure Language in Foundry Tools to detect and redact personally identifiable information (PII) with client libraries, the REST API, or the Microsoft Foundry portal.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 02/06/2026
+ms.date: 04/27/2026
 ms.author: lajanuar
 ms.devlang: csharp
 # ms.devlang: csharp, java, javascript, python
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PII検出に関するクイックスタートのタイトルと説明の修正"
}
```

### Explanation
このコードの変更は、「個人を特定できる情報（PII）」の検出に関するクイックスタートガイドのタイトルと説明を修正することを目的としています。具体的には、ガイドのタイトルが「テキスト内の個人を特定できる情報（PII）を検出するクイックスタート」から「個人を特定できる情報（PII）を検出するクイックスタート」に変更され、説明文も若干簡略化されています。この修正により、内容がより簡潔になり、利用者にとって理解しやすくなることを目指しています。さらに、日付が2026年2月6日から2026年4月27日に更新され、最新の情報が反映されています。このように、文書の正確性と可読性が向上しています。


