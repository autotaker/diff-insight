---
date: '2025-03-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ab648e8...MicrosoftDocs:bf9270b
summary: 今回のドキュメント更新では、新機能の追加やリンクの改善が行われ、ユーザーエクスペリエンスが向上しました。特に、Azure AI Foundryポータルへの直接リンクが追加され、アクセスが容易になっています。また、地域支援に関するセクションが削除され、ドキュメントが整理されて必要な情報が迅速に見つかるようになりました。他にも、精度と信頼性に関する情報が更新され、信頼性スコアの詳細が追加されています。全体として、これらの変更はユーザーにとって使いやすさと情報の最新性を強化することを目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ab648e8...MicrosoftDocs:bf9270b){target="_blank"}

# Highlights
今回のドキュメント更新においては、新機能の追加やリンクの改善が見られます。また、エリアサポートに関する破壊的変更も行われ、ユーザーエクスペリエンスが全体的に向上しました。

## New features
- Azure AI Foundryポータルへのリンクが追加され、ユーザーが容易にアクセスできるようになりました。

## Breaking changes
- 地域支援に関連するセクションが削除され、一部の機能説明が簡素化されました。これにより、ドキュメント全体が整理され、必要な情報がより迅速に見つかるようになっています。

## Other updates
- 精度と信頼性に関するドキュメントが更新され、信頼性スコアの詳細が追加されました。
- ドキュメントの日付更新が行われ、最新の情報が提供されるようになっています。
- プロンプトフローに関するチュートリアルでリンクの修正が行われ、アクセスが簡単になりました。

# Insights
Azure AI Document Intelligenceおよび言語サービスのドキュメント更新は、ユーザーの使いやすさと情報の最新性を強化することを目的としています。まず、Azure AI Foundryポータルへのリンクの追加は、ユーザーがより効率的に必要なリソースを利用できるようにする重要なステップです。ユーザーが直接ポータルにアクセスできることで、新しい機能や更新の詳細をすぐに確認できる利便性が向上します。

一方で、地域支援に関するセクションの削除は大胆な変更であり、これによりドキュメントの一貫性が保たれると同時に、ユーザーにとって重要な情報に焦点を絞ることができます。この変更は、あまり使用されない情報を排除し、主要なサービスとサポートの説明を簡潔にするための戦略的なものです。

また、精度と信頼性の文書において口語的な表現に修正された部分や、信頼性スコアの詳細なリスト化は、ユーザーがAIモデルのパフォーマンスを適切に評価するのに役立ちます。このようなドキュメント更新と修正を通じて、Azure AIサービスのユーザーは、利用時の選択と判断をより自信を持って行うことができるでしょう。

ドキュメントの日付更新については、特に目新しい情報を提供するわけではありませんが、公式な更新情報を正しく反映することで、利用者に常に最新の状況を伝える努力の一環となっています。これらの変更はユーザー体験を中心に考慮されたものであり、プロダクトへの信頼性を高める役割を果たしています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [accuracy-confidence.md](#item-56cda7) | minor update | 精度と信頼性に関するドキュメントの更新 | modified | 28 | 25 | 53 | 
| [studio-overview.md](#item-db8fa3) | minor update | Azure AI Foundryポータルのリンク追加 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-1ec8d3) | minor update | Azure AI Foundryポータルのリンク追加 | modified | 1 | 1 | 2 | 
| [regional-support.md](#item-5becd3) | breaking change | エリアサポートに関するセクションの削除 | modified | 1 | 50 | 51 | 
| [overview.md](#item-bdc923) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [index.yml](#item-c9444f) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [prompt-flow.md](#item-22c24b) | minor update | リンクの修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/document-intelligence/concept/accuracy-confidence.md{#item-56cda7}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 02/21/2025
+ms.date: 03/03/2025
 ms.author: lajanuar
 ---
 
@@ -50,7 +50,7 @@ After an analysis operation, review the JSON output. Examine the `confidence` va
 
 > [!NOTE]
 >
-> * **Custom neural and generative models** do not provide accuracy scores during training.
+> * **Custom neural and generative models** don't provide accuracy scores during training.
 
 The output of a `build` (v3.0 and onward) or `train` (v2.1) custom model operation includes the estimated accuracy score. This score represents the model's ability to accurately predict the labeled value on a visually similar document. Accuracy is measured within a percentage value range from 0% (low) to 100% (high). It's best to target a score of 80% or higher. For more sensitive cases, like financial or medical records, we recommend a score of close to 100%. You can also add a human review stage to validate for more critical automation workflows.
 
@@ -63,19 +63,22 @@ The output of a `build` (v3.0 and onward) or `train` (v2.1) custom model operati
 
 Custom template models generate an estimated accuracy score when trained. Documents analyzed with a custom model produce a confidence score for extracted fields. When interpreting the confidence score from a custom model, you should consider all the confidence scores returned from the model. Let's start with a list of all the confidence scores.
 
-1. **Document type confidence score**: The document type confidence is an indicator of closely the analyzed document resembles documents in the training dataset. When the document type confidence is low, it's indicative of template or structural variations in the analyzed document. To improve the document type confidence, label a document with that specific variation and add it to your training dataset. Once the model is retrained, it should be better equipped to handle that class of variations.
-2. **Field level confidence**: Each labeled field extracted has an associated confidence score. This score reflects the model's confidence on the position of the value extracted. While evaluating confidence scores, you should also look at the underlying extraction confidence to generate a comprehensive confidence for the extracted result. Evaluate the `OCR` results for text extraction or selection marks depending on the field type to generate a composite confidence score for the field.
-3. **Word confidence score** Each word extracted within the document has an associated confidence score. The score represents the confidence of the transcription. The pages array contains an array of words and each word has an associated span and confidence score. Spans from the custom field extracted values match the spans of the extracted words.
-4. **Selection mark confidence score**: The pages array also contains an array of selection marks. Each selection mark has a confidence score representing the confidence of the selection mark and selection state detection. When a labeled field has a selection mark, the custom field selection combined with the selection mark confidence is an accurate representation of overall confidence accuracy.
+* **Document type confidence score**: The document type confidence is an indicator of closely the analyzed document resembles documents in the training dataset. When the document type confidence is low, it's indicative of template or structural variations in the analyzed document. To improve the document type confidence, label a document with that specific variation and add it to your training dataset. Once the model is retrained, it should be better equipped to handle that class of variations.
+
+* **Field level confidence**: Each labeled field extracted has an associated confidence score. This score reflects the model's confidence on the position of the value extracted. While evaluating confidence scores, you should also look at the underlying extraction confidence to generate a comprehensive confidence for the extracted result. Evaluate the `OCR` results for text extraction or selection marks depending on the field type to generate a composite confidence score for the field.
+
+* **Word confidence score** Each word extracted within the document has an associated confidence score. The score represents the confidence of the transcription. The pages array contains an array of words and each word has an associated span and confidence score. Spans from the custom field extracted values match the spans of the extracted words.
+
+* **Selection mark confidence score**: The pages array also contains an array of selection marks. Each selection mark has a confidence score representing the confidence of the selection mark and selection state detection. When a labeled field has a selection mark, the custom field selection combined with the selection mark confidence is an accurate representation of overall confidence accuracy.
 
 The following table demonstrates how to interpret both the accuracy and confidence scores to measure your custom model's performance.
 
 | Accuracy | Confidence | Result |
 |--|--|--|
-| High| High | &bullet; The model is performing well with the labeled keys and document formats. <br>&bullet; You have a balanced training dataset. |
-| High | Low | &bullet; The analyzed document appears different from the training dataset.<br>&bullet; The model would benefit from retraining with at least five more labeled documents. <br>&bullet; These results could also indicate a format variation between the training dataset and the analyzed document. </br>Consider adding a new model.|
-| Low | High | &bullet; This result is most unlikely.<br>&bullet; For low accuracy scores, add more labeled data or split visually distinct documents into multiple models. |
-| Low | Low| &bullet; Add more labeled data.<br>&bullet; Split visually distinct documents into multiple models.|
+| High| High | &bullet; The model is performing well with the labeled keys and document formats. &bullet; You have a balanced training dataset. |
+| High | Low | &bullet; The analyzed document appears different from the training dataset.&bullet; The model would benefit from retraining with at least five more labeled documents. &bullet; These results could also indicate a format variation between the training dataset and the analyzed document. </br>Consider adding a new model.|
+| Low | High | &bullet; This result is most unlikely.&bullet; For low accuracy scores, add more labeled data or split visually distinct documents into multiple models. |
+| Low | Low| &bullet; Add more labeled data.&bullet; Split visually distinct documents into multiple models.|
 
 ## Ensure high model accuracy for custom models
 
@@ -97,35 +100,35 @@ Variances in the visual structure of your documents affect the accuracy of your
 
 Here are some common questions that should help with interpreting the table, row, and cell scores:
 
-**Q:** Is it possible to see a high confidence score for cells, but a low confidence score for the row?<br>
+##### Can cells have high confidence scores while the row has a low confidence score?
 
-**A:** Yes. The different levels of table confidence (cell, row, and table) are meant to capture the correctness of a prediction at that specific level. A correctly predicted cell that belongs to a row with other possible misses would have high cell confidence, but the row's confidence should be low. Similarly, a correct row in a table with challenges with other rows would have high row confidence whereas the table's overall confidence would be low.
+The different levels of table confidence (cell, row, and table) are meant to capture the correctness of a prediction at that specific level. A correctly predicted cell that belongs to a row with other possible misses would have high cell confidence, but the row's confidence should be low. Similarly, a correct row in a table with challenges with other rows would have high row confidence whereas the table's overall confidence would be low.
 
-**Q:** What is the expected confidence score when cells are merged? Since a merge results in the number of columns identified to change, how are scores affected?<br>
+##### How does merging cells affect confidence scores, given the change in the number of identified columns?
 
-**A:** Regardless of the type of table, the expectation for merged cells is that they should have lower confidence values. Furthermore, the cell that is missing (because it was merged with an adjacent cell) should have `NULL` value with lower confidence as well. How much lower these values might be depends on the training dataset, the general trend of both merged and missing cell having lower scores should hold.
+Regardless of the type of table, the expectation for merged cells is that they should have lower confidence values. Furthermore, the cell that is missing (because it was merged with an adjacent cell) should have `NULL` value with lower confidence as well. How much lower these values might be depends on the training dataset, the general trend of both merged and missing cell having lower scores should hold.
 
-**Q:** What is the confidence score when a value is optional? Should you expect a cell with a ``NULL`` value and high confidence score if the value is missing?<br>
+#####  What is the confidence score for optional values? Should you expect a cell with a "NULL" value to have a high confidence score since the value is absent?
 
-**A:** If your training dataset is representative of the optionality of cells, it helps the model know how often a value tends to appear in the training set, and thus what to expect during inference. This feature is used when computing the confidence of either a prediction or of making no prediction at all (`NULL`). You should expect an empty field with high confidence for missing values that are mostly empty in the training set too.
+If your training dataset is representative of the optionality of cells, it helps the model know how often a value tends to appear in the training set, and thus what to expect during inference. This feature is used when computing the confidence of either a prediction or of making no prediction at all (`NULL`). You should expect an empty field with high confidence for missing values that are mostly empty in the training set too.
 
-**Q:** How are confidence scores affected if a field is optional and not present or missed? Is the expectation that the confidence score answers that question?<br>
+##### Can confidence scores alter if an optional field is absent? Do the confidence scores reflect this change?
 
-**A:** When a value is missing from a row, the cell has a `NULL` value and confidence assigned. A high confidence score here should mean that the model prediction (of there not being a value) is more likely to be correct. In contrast, a low score should signal more uncertainty from the model (and thus the possibility of an error, like the value being missed).
+When a value is missing from a row, the cell has a `NULL` value and confidence assigned. A high confidence score here should mean that the model prediction (of there not being a value) is more likely to be correct. In contrast, a low score should signal more uncertainty from the model (and thus the possibility of an error, like the value being missed).
 
-**Q:** What should be the expectation for cell confidence and row confidence when extracting a multi-page table with a row split across pages?<br>
+##### What are the expectations for cell and row confidence when extracting a multi-page table with a row split across pages?
 
-**A:** Expect the cell confidence to be high and row confidence to be potentially lower than rows that aren't split. The proportion of split rows in the training data set can affect the confidence score. In general, a split row looks different than the other rows in the table (thus, the model is less certain that it's correct).
+Expect the cell confidence to be high and row confidence to be potentially lower than rows that aren't split. The proportion of split rows in the training data set can affect the confidence score. In general, a split row looks different than the other rows in the table (thus, the model is less certain that it's correct).
 
-**Q:** For cross-page tables with rows that cleanly end and start at the page boundaries, is it correct to assume that confidence scores are consistent across pages?
+##### For tables spanning multiple pages, can we assume confidence scores remain consistent if rows end and start cleanly at page boundaries?
 
-**A:** Yes. Since rows look similar in shape and contents, regardless of where they are in the document (or in which page), their respective confidence scores should be consistent.
+Since rows look similar in shape and contents, regardless of where they are in the document (or in which page), their respective confidence scores should be consistent.
 
-**Q:** What is the best way to utilize the new confidence scores?<br>
+##### What is the best way to utilize the new confidence scores?
 
-**A:** Look at all levels of table confidence starting in a top-to-bottom approach: begin by checking a table's confidence as a whole, then drill down to the row level and look at individual rows, finally look at cell-level confidences. Depending on the type of table, there are a couple of things of note:
+* Look at all levels of table confidence starting in a top-to-bottom approach: begin by checking a table's confidence as a whole, then drill down to the row level and look at individual rows, finally look at cell-level confidences. Depending on the type of table, there are a couple of things of note:
 
-For **fixed tables**, cell-level confidence already captures quite a bit of information on the correctness of things. This means that simply going over each cell and looking at its confidence can be enough to help determine the quality of the prediction.
+* For **fixed tables**, cell-level confidence already captures quite a bit of information on the correctness of things. This means that simply going over each cell and looking at its confidence can be enough to help determine the quality of the prediction.
 For **dynamic tables**, the levels are meant to build on top of each other, so the top-to-bottom approach is more important.
 
 ## Next step
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "精度と信頼性に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Document Intelligenceのドキュメントに関するもので、主に精度と信頼性に関する情報を更新しています。変更箇所には、文書の更新日付の修正や、文書内の特定の表現の修正が含まれています。また、信頼性スコアに関する詳細な説明が追加され、特定の条件下での期待される結果についての情報が強化されています。

具体的には、文中の「does not provide accuracy scores during training」という表現が「don't provide accuracy scores during training」と修正され、より口語的な表現に変更されました。また、信頼性スコアに関連する各項目がリスト形式で整備され、ユーザーが理解しやすくなるように調整されています。この変更により、ユーザーがモデルのパフォーマンスを評価する際の指針が明確になり、ドキュメントの内容がより一層利用しやすくなっています。

## articles/ai-services/document-intelligence/studio-overview.md{#item-db8fa3}

<details>
<summary>Diff</summary>
````diff
@@ -194,7 +194,7 @@ With Document Intelligence, you can quickly automate your data processing in app
 
 ### [**Azure AI Foundry portal**](#tab/ai-studio)
 
-Document Intelligence is part of the Azure AI services offerings in the Azure AI Foundry portal. Each of the Azure AI services helps developers and organizations rapidly create intelligent, cutting-edge, market-ready, and responsible applications with out-of-the-box and prebuilt and customizable APIs and models.
+Document Intelligence is part of the Azure AI services offerings in the [Azure AI Foundry portal](https://ai.azure.com/). Each of the Azure AI services helps developers and organizations rapidly create intelligent, cutting-edge, market-ready, and responsible applications with out-of-the-box and prebuilt and customizable APIs and models.
 
 Learn how to [connect your AI services hub](../../ai-studio/ai-services/how-to/connect-ai-services.md) with AI services and get started using Document Intelligence.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク追加"
}
```

### Explanation
この変更は、Azure AI Document Intelligenceに関するドキュメントの一部で、Azure AI Foundryポータルへのリンクが追加されました。具体的には、文中の「Azure AI Foundry portal」というフレーズが、ポータルへのURLを含むリンク形式に修正されています。これにより、ユーザーが直接ポータルにアクセスしやすくなり、Azure AIサービスの使用をより迅速かつ簡単に開始できるようになります。この変更は、情報の明確さとユーザビリティを向上させるための重要な改善点です。

## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -88,7 +88,7 @@ For more information, *see* client libraries for the following supported program
 
 The Document Intelligence [**2024-07-31-preview**](/rest/api/aiservices/document-models?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true) REST API is now available. This preview API introduces new and updated capabilities:
 
-* Public preview version [**2024-07-31-preview**](/rest/api/aiservices/operation-groups?view=rest-aiservices-2024-07-31-preview&preserve-view=true) is currently available only in the following Azure regions. The new document field extraction model in Azure AI Foundry portal is only available in North Central US region:
+* Public preview version [**2024-07-31-preview**](/rest/api/aiservices/operation-groups?view=rest-aiservices-2024-07-31-preview&preserve-view=true) is currently available only in the following Azure regions. The new document field extraction model in [Azure AI Foundry portal](https://ai.azure.com/) is only available in North Central US region:
 
 * **East US**
 * **West US2**
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのリンク追加"
}
```

### Explanation
この変更は、Azure AI Document Intelligenceの「What's New」ドキュメントに対するものであり、2024年7月31日のプレビューAPIに関連する情報にリンクが追加されました。具体的には、文中の「Azure AI Foundry portal」というフレーズが、ポータルへの直接リンクを含む形式に修正されています。この変更により、ユーザーは新しいドキュメントフィールド抽出モデルに関する情報を簡単に参照し、Azure AI Foundryポータルに迅速にアクセスできるようになります。情報の利便性が向上し、ユーザーエクスペリエンスが強化される重要な更新です。

## articles/ai-services/language-service/concepts/regional-support.md{#item-5becd3}

<details>
<summary>Diff</summary>
````diff
@@ -25,46 +25,7 @@ Typically you can refer to the [region support](https://azure.microsoft.com/expl
 
 ## Conversational language understanding and orchestration workflow
 
-Conversational language understanding, orchestration workflow, and custom sentiment analysis are only available in some Azure regions. Some regions are available for **both authoring and prediction**, while other regions are **prediction only**. Language resources in authoring regions allow you to create, edit, train, and deploy your projects. Language resources in prediction regions allow you to get [predictions from a deployment](./custom-features/multi-region-deployment.md).
-
-| Region             | Authoring | Prediction  |
-|--------------------|-----------|-------------|
-| Australia East     | ✓         | ✓           |
-| Brazil South       |           | ✓           |
-| Canada Central     |           | ✓           |
-| Central India      | ✓         | ✓           |
-| Central US         |           | ✓           |
-| China East 2       | ✓         | ✓           |
-| China North 2      |           | ✓           |
-| East Asia          |           | ✓           |
-| East US            | ✓         | ✓           |
-| East US 2          | ✓         | ✓           |
-| France Central     |           | ✓           |
-| Japan East         |           | ✓           |
-| Japan West         |           | ✓           |
-| Jio India West     |           | ✓           |
-| Korea Central      |           | ✓           |
-| North Central US   |           | ✓           |
-| North Europe       | ✓         | ✓           |
-| Norway East        |           | ✓           |
-| Qatar Central      |           | ✓           |
-| South Africa North |           | ✓           |
-| South Central US   | ✓         | ✓           |
-| Southeast Asia     |           | ✓           |
-| Sweden Central     |           | ✓           |
-| Switzerland North  | ✓         | ✓           |
-| UAE North          |           | ✓           |
-| UK South           | ✓         | ✓           |
-| West Central US    |           | ✓           |
-| West Europe        | ✓         | ✓           |
-| West US            |            | ✓           |
-| West US 2          | ✓         | ✓           |
-| West US 3          | ✓         | ✓           |
-
-
-## Custom sentiment analysis
-
-Custom sentiment analysis is only available in some Azure regions. Some regions are available for **both authoring and prediction**, while other regions are **prediction only**. Language resources in authoring regions allow you to create, edit, train, and deploy your projects. Language resources in prediction regions allow you to get [predictions from a deployment](./custom-features/multi-region-deployment.md).
+Conversational language understanding and orchestration workflow are only available in some Azure regions. Some regions are available for **both authoring and prediction**, while other regions are **prediction only**. Language resources in authoring regions allow you to create, edit, train, and deploy your projects. Language resources in prediction regions allow you to get [predictions from a deployment](./custom-features/multi-region-deployment.md).
 
 | Region             | Authoring | Prediction  |
 |--------------------|-----------|-------------|
@@ -203,16 +164,6 @@ Custom text classification is only available in some Azure regions. Some regions
 |West US               |✓                             |✓                                        |
 |West US 2             |✓                             |✓                                        |
 
-## Custom Text Analytics for health
-
-Custom Text Analytics for health is only available in some Azure regions since it is a preview service. Some regions may be available for **both authoring and prediction**, while other regions may be for **prediction only**. Language resources in authoring regions allow you to create, edit, train, and deploy your projects. Language resources in prediction regions allow you to get predictions from a deployment.
-
-| Region             | Authoring | Prediction  |
-|--------------------|-----------|-------------|
-| East US            | ✓         | ✓           |
-| UK South           | ✓         | ✓           |
-| North Europe       | ✓         | ✓           |
-
 ### Next steps
 
 * [Language support](./language-support.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エリアサポートに関するセクションの削除"
}
```

### Explanation
この変更は、Azure AIサービスの言語サービスに関する「地域支援」ドキュメントの大幅な修正を示しています。具体的には、「会話型言語理解」と「オーケストレーションワークフロー」に関連する地域サポートの説明が簡素化され、カスタムセンチメント分析とカスタムテキスト分析のセクションが削除されました。この変更は、情報をまとめるものであり、主要な機能に関する明確な焦点を維持しつつ、不要な情報を省いています。

結果として、地域ごとのサポートの情報がコンパクトに整理されており、ユーザーは必要な情報をより迅速に見つけやすくなっています。この削除は、新しい情報を強調するための戦略的な選択と考えられ、全体的なドキュメントの簡潔さと明瞭さを向上させます。

## articles/ai-services/language-service/conversational-language-understanding/overview.md{#item-bdc923}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 08/23/2024
+ms.date: 03/02/2025
 ms.author: jboback
 ms.custom: language-service-clu
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、「会話型言語理解」ドキュメントのメタデータにおける日付の更新を含んでいます。具体的には、`ms.date`フィールドが2024年8月23日から2025年3月2日に変更されています。この変更は、ドキュメントの更新日を正確に反映させるものであり、ユーザーに最新の情報を提供するために重要です。ドキュメントの日付を更新することで、コンテンツの新鮮さと関連性が向上し、読者が最新の情報にアクセスできることを保証します。

## articles/ai-services/language-service/index.yml{#item-c9444f}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ metadata:
   manager: nitinme
   ms.service: azure-ai-language
   ms.topic: hub-page
-  ms.date: 08/23/2024
+  ms.date: 03/02/2025
   ms.author: jboback
 highlightedContent:
 # itemType: architecture | concept | deploy | download | get-started | how-to-guide | learn | overview | quickstart | reference | tutorial | whats-new
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、言語サービスに関するインデックスYAMLファイルのメタデータセクションにおける日付の更新を示しています。`ms.date`フィールドが2024年8月23日から2025年3月2日に更新されており、これによりドキュメントの最新性が保たれています。この更新は、読者に対して最新のコンテンツを提供するために重要であり、正確な情報を持ち続けるための一環です。ドキュメントの日付を適切に反映させることで、ユーザーはコンテンツの新鮮さを確認でき、関連性のある情報にアクセスすることができます。

## articles/ai-services/language-service/tutorials/prompt-flow.md{#item-22c24b}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ Your project is used to organize your work and save state.
 
 You can create an Azure AI Language flow by either cloning the samples available in the gallery or creating a flow from scratch. If you already have flow files in local or file share, you can also import the files to create a flow. For the purposes of this tutorial we'll be using the prebuilt **Analyze Conversations** flow.
 
-To create a prompt flow from the gallery in Azure AI Foundry portal:
+To create a prompt flow from the gallery in [Azure AI Foundry portal](https://ai.azure.com/):
 
 1. Sign in to Azure AI Foundry and select your project.
 
@@ -66,4 +66,4 @@ To create a prompt flow from the gallery in Azure AI Foundry portal:
 
 * [Azure AI Language homepage](https://aka.ms/azure-language)
 * [Azure AI Language product demo videos](https://aka.ms/language-videos)
-* [Explore Azure AI Language in Azure AI Foundry portal](https://aka.ms/AzureAiLanguage)
\ No newline at end of file
+* [Explore Azure AI Language in Azure AI Foundry portal](https://aka.ms/AzureAiLanguage)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの修正"
}
```

### Explanation
この変更は、チュートリアル「プロンプトフロー」に関するドキュメント内のリンクの修正を含んでいます。具体的には、「Azure AI Foundry portal」という部分に直接リンクが追加され、ユーザーが関連リソースにアクセスしやすくなっています。また、リンクセクションの末尾にも改行が追加され、テキストの整形が改善されました。この修正は、ユーザーの利便性を向上させるためのものであり、チュートリアルが最新の情報を提供していることを示します。正確なリンクを通じて、読者は必要なリソースに簡単にアクセスできるため、学習の効率が向上します。


