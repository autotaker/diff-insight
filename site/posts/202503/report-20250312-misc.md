---
date: '2025-03-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f35ae63...MicrosoftDocs:3791c10
summary: このコードの変更は、主にドキュメント内の画像説明を修正するもので、altテキストが「Azure AI Studio」から「Azure AI Foundry
  portal」へ変更されました。この修正により、ドキュメントの正確性と一貫性が向上し、ユーザーの理解を助けます。新機能は追加されていませんが、altテキストの修正が複数のセクションにわたって行われており、特にAIサービスに関連する情報に関して、一貫した理解を促進します。この変更はユーザーエクスペリエンスを向上させる重要な要素となっており、Microsoftはドキュメントの品質向上に積極的に取り組んでいることが見て取れます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f35ae63...MicrosoftDocs:3791c10){target="_blank"}

# ハイライト
このコードの変更は、主にドキュメント内の画像説明を修正するものであり、「Azure AI Studio」から「Azure AI Foundry portal」へのaltテキストの変更が行われました。これにより、ドキュメントの正確性と一貫性が向上しています。

## 新機能
- 特に新機能は追加されていませんが、ドキュメントの正確性が向上し、利用者の理解を助けます。

## 重大な変更
- 重大な変更は報告されていません。

## その他のアップデート
- altテキストの修正が、複数のドキュメントセクションで各種AIサービス（キー フレーズ抽出、言語検出、名前付きエンティティ認識、個人識別情報抽出、感情分析、要約、健康情報の抽出）にわたって行われました。

# インサイト
ドキュメント内のaltテキストの修正は、一見すると小さな変更に見えるかもしれませんが、実際にはユーザーエクスペリエンスの向上に大きく寄与します。今回の更新により、Microsoft のAIサービスを利用するユーザーが、どのプラットフォームやインターフェースに関連する情報を閲覧しているのかが明確に理解できるようになりました。これは、Azure AI Foundry portalが提供する機能や情報を、利用者が正確に読み解くための重要なポイントです。特に、新旧の名称が混在することによる混乱を避け、一貫性のある情報提供を可能にしています。

このような改訂を通じて、Microsoftはドキュメントの品質向上に積極的に取り組んでおり、ユーザーにとっての使いやすさを常に改善し続けていることが窺えます。特に、視覚情報が重要なコンテンツでは、正確なaltテキストはアクセシビリティの観点からも重要であり、より幅広いユーザー層に対して包括的な体験を提供するための基盤となります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-ai-foundry.md](#item-5b0d88) | minor update | Azure AI Foundryポータルの画像説明の修正 | modified | 1 | 1 | 2 | 
| [azure-ai-foundry.md](#item-41c23c) | minor update | Azure AI Foundryポータルの言語検出画像説明の修正 | modified | 1 | 1 | 2 | 
| [azure-ai-foundry.md](#item-659662) | minor update | Azure AI Foundryポータルの名前付きエンティティ認識画像説明の修正 | modified | 1 | 1 | 2 | 
| [azure-ai-foundry.md](#item-ff89fc) | minor update | Azure AI Foundryポータルの個人識別情報抽出画像説明の修正 | modified | 2 | 2 | 4 | 
| [azure-ai-foundry.md](#item-23db96) | minor update | Azure AI Foundryポータルの感情分析画像説明の修正 | modified | 1 | 1 | 2 | 
| [azure-ai-foundry.md](#item-a63cc2) | minor update | Azure AI Foundryポータルの要約機能に関する画像説明の修正 | modified | 3 | 3 | 6 | 
| [azure-ai-foundry.md](#item-017ec5) | minor update | Azure AI Foundryポータルの健康情報抽出に関する画像説明の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/language-service/key-phrase-extraction/includes/quickstarts/azure-ai-foundry.md{#item-5b0d88}

<details>
<summary>Diff</summary>
````diff
@@ -46,4 +46,4 @@ After your operation is completed, each entity is underlined in the center pane
 |------|----------------------------|
 |Extracted key phrases|A list of the extracted key phrases.|
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/key-phrase-extraction.png" alt-text="A screenshot of an example of Extract key phrases in azure AI studio." lightbox="../../media/quickstarts/azure-ai-foundry/key-phrase-extraction.png":::
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/key-phrase-extraction.png" alt-text="A screenshot of an example of Extract key phrases in Azure AI Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/key-phrase-extraction.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルの画像説明の修正"
}
```

### Explanation
この変更は、ドキュメント内の画像の説明を修正するためのマイナーアップデートです。変更内容としては、画像に関連するaltテキストが「Azure AI Studio」から「Azure AI Foundry portal」に更新されました。これにより、画像のコンテキストがより正確に表現されています。具体的には、該当部分のコマンドは、元々のaltテキスト「例のExtract key phrasesのスクリーンショット」を、修正後には「Extract key phrasesの例のスクリーンショット in Azure AI Foundry portal」に変更しています。この変更は、ユーザーが文書をより適切に理解するのに寄与します。

## articles/ai-services/language-service/language-detection/includes/quickstarts/azure-ai-foundry.md{#item-41c23c}

<details>
<summary>Diff</summary>
````diff
@@ -50,4 +50,4 @@ After your operation is completed, the **Details** section contains the followin
 |Script Name| The name of the most detected script in the text.
 |Iso 15924 Script Code| The ISO 15924 script code for the most detected script.|
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/language-detection.png" alt-text="A screenshot of an example of detect language in azure AI studio." lightbox="../../media/quickstarts/azure-ai-foundry/language-detection.png":::
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/language-detection.png" alt-text="A screenshot of an example of detect language in Azure AI Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/language-detection.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルの言語検出画像説明の修正"
}
```

### Explanation
この変更は、ドキュメント内の言語検出に関する画像の説明を更新するためのマイナーアップデートです。具体的には、画像のaltテキストが「Azure AI Studio」に関する表現から「Azure AI Foundry portal」に修正されました。この変更により、画像が示す内容がより正確に表現され、ユーザーにとっての理解が向上します。該当部分のテキストは、"言語を検出する例のスクリーンショット" をより具体的に "Azure AI Foundry portalでの言語検出の例のスクリーンショット" に変更しています。このマイナーな修正は、文書の一貫性を保つのに役立ちます。

## articles/ai-services/language-service/named-entity-recognition/includes/quickstarts/azure-ai-foundry.md{#item-659662}

<details>
<summary>Diff</summary>
````diff
@@ -53,4 +53,4 @@ After your operation is completed, the type of entity is displayed beneath each
 |Length| The character length of the entity.|
 |Confidence| How confident the model is in the correctness of identification of entity's type.|
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/named-entity-recognition.png" alt-text="A screenshot of an example of extract named entities in azure AI studio." lightbox="../../media/quickstarts/azure-ai-foundry/named-entity-recognition.png":::
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/named-entity-recognition.png" alt-text="A screenshot of an example of extract named entities in Azure AI Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/named-entity-recognition.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルの名前付きエンティティ認識画像説明の修正"
}
```

### Explanation
この変更は、名前付きエンティティ認識に関するドキュメント内の画像説明を修正するためのマイナーアップデートです。具体的には、画像のaltテキストが「Azure AI Studio」から「Azure AI Foundry portal」へと更新されました。この変更により、画像がどのシステムを示しているのかが明確になり、利用者がベストな理解を得られるようになります。元のaltテキスト「抽出された名前付きエンティティの例のスクリーンショット」は、修正後には「Azure AI Foundry portalでの名前付きエンティティ抽出の例のスクリーンショット」となっています。このような修正は、ドキュメントの一貫性と正確性を高めるために重要です。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/azure-ai-foundry.md{#item-ff89fc}

<details>
<summary>Diff</summary>
````diff
@@ -54,7 +54,7 @@ After your operation is completed, the type of entity is displayed beneath each
 |Length| The character length of the entity.|
 |Confidence| How confident the model is in the correctness of identification of entity's type.|
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/conversation-pii.png" alt-text="A screenshot of an example of extract PII from conversation in azure AI studio." lightbox="../../media/quickstarts/azure-ai-foundry/conversation-pii.png":::
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/conversation-pii.png" alt-text="A screenshot of an example of extract PII from conversation in Azure AI Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/conversation-pii.png":::
 
 ### Extract PII from text
 
@@ -82,5 +82,5 @@ After your operation is completed, the type of entity is displayed beneath each
 |Confidence| How confident the model is in the correctness of identification of entity's type.|
 |Tags| How confident the model is in the correctness for each identified entity type.|
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/text-pii.png" alt-text="A screenshot of an example of extract PII from text in azure AI studio." lightbox="../../media/quickstarts/azure-ai-foundry/text-pii.png":::
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/text-pii.png" alt-text="A screenshot of an example of extract PII from text in Azure AI Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/text-pii.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルの個人識別情報抽出画像説明の修正"
}
```

### Explanation
この変更は、個人識別情報（PII）を抽出するドキュメントにおいて、画像のaltテキストを更新するためのマイナーアップデートです。二つの画像のaltテキストが、それぞれ「Azure AI Studio」から「Azure AI Foundry portal」に修正されました。この変更により、画像が示すシステムに関する情報が正確になり、ユーザーがより良い理解を得られるようになります。具体的には、会話からPIIを抽出する例およびテキストからPIIを抽出する例の説明が変更されており、「抽出された個人識別情報の例のスクリーンショット」が正確に「Azure AI Foundry portalでの抽出された個人識別情報の例のスクリーンショット」と表現されています。このようなマイナーな修正は、文書全体の一貫性を高めるために重要です。

## articles/ai-services/language-service/sentiment-opinion-mining/includes/quickstarts/azure-ai-foundry.md{#item-23db96}

<details>
<summary>Diff</summary>
````diff
@@ -56,4 +56,4 @@ The following fields are only present if opinion mining is enabled:
 |Target|The target of the detected opinion.|
 |Assessments| The detected opinion and the detected persuasion (positive, neutral, negative), as well as the percent of detected persuasion.|
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/sentiment-opinion-mining.png" alt-text="An example of Analyze sentiment in azure AI studio" lightbox="../../media/quickstarts/azure-ai-foundry/sentiment-opinion-mining.png":::
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/sentiment-opinion-mining.png" alt-text="An example of Analyze sentiment in Azure AI Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/sentiment-opinion-mining.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルの感情分析画像説明の修正"
}
```

### Explanation
この変更は、感情分析に関するドキュメント内の画像説明を更新するためのマイナーアップデートです。画像のaltテキストが「Azure AI Studio」から「Azure AI Foundry portal」へと修正されました。この変更により、表示される画像がどのプラットフォームを示しているのかが明確になり、ユーザーが正確に情報を理解できるようになります。具体的には、感情分析の例に関連する画像が、正確なプラットフォーム名「Azure AI Foundry portal」を反映する形で修正されています。こうした細やかな変更は、文書の一貫性と信頼性を向上させるために重要です。

## articles/ai-services/language-service/summarization/includes/quickstarts/azure-ai-foundry.md{#item-a63cc2}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ After your operation is completed, the **Details** section contains the followin
 |Chapter Title|  A list of titles for semantically segmented chapters with corresponding timestamps. The **Chapter title** Summarization aspect must be toggled on for this to appear.|
 |Narrative|  A list of narrative summaries for semantically segmented chapters with corresponding timestamps. The **Narrative** Summarization aspect must be toggled on for this to appear.|
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/conversation-summarization.png" alt-text="A screenshot of an example of summarize conversation in azure AI studio." lightbox="../../media/quickstarts/azure-ai-foundry/conversation-summarization.png":::
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/conversation-summarization.png" alt-text="A screenshot of an example of summarize conversation in Azure AI Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/conversation-summarization.png":::
 
 ### Use Summarize for call center
 
@@ -72,7 +72,7 @@ After your operation is completed, the **Details** section contains the followin
 |Issue|  A summary of the customer issue in the customer-and-agent conversation. The **Issue** Summarization aspect must be toggled on for this to appear.|
 |Resolution|  A summary of the solutions tried in the customer-and-agent conversation. The **Resolution** Summarization aspect must be toggled on for this to appear.|
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/call-center-summarization.png" alt-text="A screenshot of an example of summarize for call center in azure AI studio." lightbox="../../media/quickstarts/azure-ai-foundry/call-center-summarization.png":::
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/call-center-summarization.png" alt-text="A screenshot of an example of summarize for call center in Azure AI Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/call-center-summarization.png":::
 
 ### Use Summarize text
 
@@ -95,4 +95,4 @@ After your operation is completed, the **Details** section contains the followin
 |Extractive summary| Extracted sentences from the input text, ranked by detected relevance and prioritized for words in the **Defined keywords for summary focus** field, if any. Sentences are sorted by rank score of detected relevance (default) or order of appearance in the input text.|
 |Abstractive summary| A summary of the input text of the length chosen in the **Summary length** field and prioritized for words in the **Defined keywords for summary focus** field, if any.|
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/text-summarization.png" alt-text="A screenshot of an example of summarize text in azure AI studio." lightbox="../../media/quickstarts/azure-ai-foundry/text-summarization.png":::
\ No newline at end of file
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/text-summarization.png" alt-text="A screenshot of an example of summarize text in Azure AI Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/text-summarization.png":::
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルの要約機能に関する画像説明の修正"
}
```

### Explanation
この変更は、要約機能に関するドキュメントの中で、画像のaltテキストを更新することを目的としたマイナーアップデートです。具体的には、三つの異なるセクションで使用されている画像について、altテキストが「Azure AI Studio」から「Azure AI Foundry portal」へ修正されました。この更新により、画像が示すプラットフォームが正確に反映され、ユーザーはより明確に情報を理解できるようになります。変更されたセクションは、会話の要約、コールセンターの要約、およびテキストの要約に関するものであり、それぞれの例を示す画像が正確なプラットフォーム情報を提供しています。こうした小さな修正ながらも、ドキュメントの一貫性を高めるために重要な役割を果たします。

## articles/ai-services/language-service/text-analytics-for-health/includes/quickstarts/azure-ai-foundry.md{#item-017ec5}

<details>
<summary>Diff</summary>
````diff
@@ -49,4 +49,4 @@ After your operation is completed, the type of entity is displayed beneath each
 |Category| The type of entity that was detected.|
 |Confidence| How confident the model is in the correctness of identification of entity's type.|
 
-:::image type="content" source="../../media/quickstarts/azure-ai-foundry/text-analytics-for-health.png" alt-text="A screenshot of an example of extract health information in azure AI studio." lightbox="../../media/quickstarts/azure-ai-foundry/text-analytics-for-health.png":::
+:::image type="content" source="../../media/quickstarts/azure-ai-foundry/text-analytics-for-health.png" alt-text="A screenshot of an example of extract health information in Azure AI Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/text-analytics-for-health.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルの健康情報抽出に関する画像説明の修正"
}
```

### Explanation
この変更は、健康情報の抽出に関するドキュメント内の画像説明を更新するためのマイナーアップデートです。具体的には、画像のaltテキストが「Azure AI Studio」から「Azure AI Foundry portal」へ修正されました。この変更により、ユーザーは画像が示すプラットフォームの正確な情報を得ることができ、理解を深めることができます。このような小さな修正であっても、文書の正確性と一貫性を向上させるために重要です。


