---
date: '2025-04-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b7568a1...MicrosoftDocs:b8a8182
summary: このコードの修正から、5つのドキュメントに軽微な更新が行われました。新しい機能や破壊的な変更はなく、主に日付の更新や文法、文脈の修正が含まれています。特に、「tool_choice」の項目が削除され、無効なレスポンス機能が整理されました。これにより、ユーザーが文書をより理解しやすくなり、正確に目的を達成できるようになります。全体的に、ユーザーエクスペリエンスの向上に寄与する品質管理が行われています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b7568a1...MicrosoftDocs:b8a8182){target="_blank"}

<format>
# ハイライト
このコードの修正から、5つのドキュメントに対して軽微な更新が行われたことがわかります。新しい機能や破壊的な変更は含まれておらず、主に日付の更新と文法、文脈の修正が中心となっています。

## 新機能
特に新しい機能の追加はありません。

## 破壊的な変更
特別に破壊的な変更は含まれていません。

## その他の更新
- 日付が2025年1月から2025年4月29日に更新されています。
- 一部文法的およびコンテキストの明確化が行われました。
- 「tool_choice」の項目が無効なレスポンス機能として削除されました。

# インサイト
この一連の変更は、ドキュメントを最新の情報に保ち、ユーザーが情報に全幅の信頼を寄せられるようにすることを目的としています。日付の更新は、主に文書が現時点で有効であることを示すために行われています。これに伴い、いくつかの文法やコンテキストに微調整が加えられ、読みやすさと理解のしやすさが向上しています。

特に「使い方」ドキュメントにおいて注目すべきは、「tool_choice」という項目の削除についてです。これは、レスポンスAPIにおけるサポートされていない機能の整理の一環であり、ユーザーが混乱することを避けるために非常に理にかなっています。同時に、他の無効な機能については引き続き明示されています。

全体として、ユーザーがドキュメントを利用して正確かつ迅速に目的を達成できるように、細部にわたる品質管理が行われています。これらの変更は見かけ上はマイナーに見えますが、長期的なユーザーエクスペリエンスの向上に寄与しています。文法と文脈の修正により、内容が改善され、その結果、ユーザーはより効率的にドキュメントを活用できるようになりました。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [assistant.md](#item-b12c67) | minor update | 日付と文の修正 | modified | 2 | 2 | 4 | 
| [assistants-logic-apps.md](#item-57ae37) | minor update | 日付と文法の修正 | modified | 2 | 2 | 4 | 
| [on-your-data-best-practices.md](#item-801589) | minor update | 日付と文脈の修正 | modified | 2 | 2 | 4 | 
| [responses.md](#item-b9757d) | minor update | ツール選択の削除 | modified | 0 | 1 | 1 | 
| [use-your-data-quickstart.md](#item-52c1f4) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/how-to/assistant.md{#item-b12c67}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: references_regions
 ms.topic: how-to
-ms.date: 01/28/2025
+ms.date: 04/29/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -118,7 +118,7 @@ assistant = client.beta.assistants.create(
 There are a few details you should note from the configuration above:
 
 - We enable this assistant to access code interpreter with the line `tools=[{"type": "code_interpreter"}],`. This gives the model access to a sand-boxed python environment to run and execute code to help formulating responses to a user's question.
-- In the instructions we remind the model that it can execute code. Sometimes the model needs help guiding it towards the right tool to solve a given query. If you know you want to use a particular library to generate a certain response that you know is part of code interpreter, it can help to provide guidance by saying something like "Use Matplotlib to do x."
+- In the instructions we remind the model that it can execute code. Sometimes the model needs help with guiding it towards the right tool to solve a given query. If you know you want to use a particular library to generate a certain response that you know is part of code interpreter, it can help to provide guidance by saying something like "Use Matplotlib to do x."
 - Since this is Azure OpenAI the value you enter for `model=` **must match the deployment name**.
 
 Next we're going to print the contents of assistant that we just created to confirm that creation was successful:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付と文の修正"
}
```

### Explanation
この変更は、ドキュメント内の日付を2025年1月28日から2025年4月29日に更新し、指示文の一部を微調整しました。具体的には、モデルが正しいツールを選ぶために必要なガイダンスを提供する際の文言が変更されました。この調整により、ユーザーが特定のライブラリを使用する際の説明がより明確になり、コードインタープリターの利用時に役立つ情報が強調されています。全体として、ユーザーに対して技術的な指示をより効果的に伝えようとする意図があります。

## articles/ai-services/openai/how-to/assistants-logic-apps.md{#item-57ae37}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 01/28/2025
+ms.date: 04/29/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -50,7 +50,7 @@ Here are the steps to create a new Logic Apps workflow for function calling.
 1. Your workflow is required to have a Request trigger to generate a REST endpoint, and a response action to return the response to Azure AI Foundry when this workflow is invoked.
 1. Add a trigger [(Request)](/azure/connectors/connectors-native-reqres?tabs=consumption)
 
-    Select **Add a trigger** and then search for request trigger. Select the **When a HTTP request is received** operation.
+    Select **Add a trigger** and then search for request trigger. Select the **When an HTTP request is received** operation.
 
     :::image type="content" source="..\media\how-to\assistants\logic-apps\create-logic-app-1.png" alt-text="A screenshot showing the Logic Apps designer." lightbox="..\media\how-to\assistants\logic-apps\create-logic-app-1.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付と文法の修正"
}
```

### Explanation
この変更では、ドキュメント内の日付が2025年1月28日から2025年4月29日に更新され、特定の文の文法が修正されました。具体的には、「HTTPリクエストが受信されるとき」という操作の名称において、「a」が追加され、「When an HTTP request is received」という表現が使用されています。この微修正により、文の明確さが向上し、ユーザーにとって理解しやすくなっています。全体として、ドキュメントの正確性と可読性を改善することを目的とした更新です。

## articles/ai-services/openai/how-to/on-your-data-best-practices.md{#item-801589}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI Service
 description: Learn about the best practices for using Azure OpenAI On Your Data, along with how to fix common problems.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 01/28/2025
+ms.date: 04/29/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: aahill
@@ -62,7 +62,7 @@ If the correct document chunks don't appear in the retrieved documents, you need
 
 * It's possible that a correct document chunk wasn't part of the `topNDocuments` parameter. In this case, increase the parameter.
 
-* It's possible that your index fields are incorrectly mapped, so retrieval might not work well. This mapping is particularly relevant if you're using a pre-existing data source. (That is, you didn't create the index by using the studio or offline scripts available on [GitHub](https://github.com/microsoft/sample-app-aoai-chatGPT/tree/main/scripts).) For more information on mapping index fields, see the [how-to article](../concepts/use-your-data.md?tabs=ai-search#index-field-mapping).
+* It's possible that your index fields are incorrectly mapped, so retrieval might not work well. This mapping is particularly relevant if you're using a preexisting data source. (That is, you didn't create the index by using the studio or offline scripts available on [GitHub](https://github.com/microsoft/sample-app-aoai-chatGPT/tree/main/scripts).) For more information on mapping index fields, see the [how-to article](../concepts/use-your-data.md?tabs=ai-search#index-field-mapping).
 
 * It's possible that the intent generation step isn't working well. In the API response, check the `intents` fields in the `tool` message.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付と文脈の修正"
}
```

### Explanation
この変更は、ドキュメントの日付を2025年1月28日から2025年4月29日に更新し、特定の表現の文法を微調整したものです。主な修正として、「pre-existing」の表現が「preexisting」に変更され、よりスムーズなディスコースが実現されています。また、文全体の流れを改善することが目的であり、特にインデックスフィールドのマッピングに関連する部分で、ユーザーが情報を理解しやすくなるように配慮されています。全体として、この更新はテクニカルドキュメントの可読性を向上させることを目的としています。

## articles/ai-services/openai/how-to/responses.md{#item-b9757d}

<details>
<summary>Diff</summary>
````diff
@@ -55,7 +55,6 @@ Not every model is available in the regions supported by the responses API. Chec
 > [!NOTE]
 > Not currently supported:
 > - Structured outputs
-> - tool_choice
 > - image_url pointing to an internet address
 > - The web search tool is also not supported, and is not part of the `2025-03-01-preview` API.  
 > 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ツール選択の削除"
}
```

### Explanation
この変更では、ドキュメント内の注記から「tool_choice」という項目が削除されました。この修正は、レスポンスAPIが現在サポートしていない機能のリストを整理するためのものであり、ユーザーにとってより明確な情報を提供することを目的としています。他のサポートされていない機能、例えば構造化出力やインターネットアドレスを指すimage_urlについての情報はそのまま残されています。このマイナーな更新により、ユーザーはサポートされていない機能に関する理解を深めることができます。

## articles/ai-services/openai/use-your-data-quickstart.md{#item-52c1f4}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom: devx-track-dotnet, devx-track-extended-java, devx-track-js, devx-trac
 ms.topic: quickstart
 author: aahill
 ms.author: aahi
-ms.date: 01/09/2025
+ms.date: 04/29/2025
 recommendations: false
 zone_pivot_groups: openai-use-your-data
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
この変更では、ドキュメントの日付が2025年1月9日から2025年4月29日に更新されています。このマイナーな更新は、書類の情報を最新のものに保つためのものであり、利用者が正確なデータを基に意思決定を行えるように配慮されています。改訂された日付は、文書の作成や改訂のタイムスタンプを反映しており、コンテンツの鮮度を高める効果があります。この変更は他のコンテンツの内容には影響を与えず、ユーザーへの情報提供を強化することを目的としています。


