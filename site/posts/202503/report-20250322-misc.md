---
date: '2025-03-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:34ecec7...MicrosoftDocs:3341d93
summary: この変更では、ドキュメントの可読性と明確さを向上させるための微調整が行われました。新しい機能の追加や破壊的変更はなく、既存の内容の説明文やフォーマットが修正されています。具体的には、`azure-ai-foundry.md`では国と地域を考慮した表現に改善され、`sdk-python.md`では冗長な表現の削除とリンクの簡略化が行われました。これにより、ユーザー体験が向上し、ドキュメントの利便性が増しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:34ecec7...MicrosoftDocs:3341d93){target="_blank"}

# Highlights
以下の変更では、ドキュメントの可読性と明確さを向上させるための微調整が加えられました。特に、新しい機能の追加や破壊的変更はなく、既存の内容に対しての説明文やフォーマットの修正が中心です。

## New features
特に新機能の追加は行われていません。

## Breaking changes
破壊的な変更はありません。

## Other updates
- `azure-ai-foundry.md`では、"Select country hint"に関する説明が改善され、国に加えて地域を含む表現に変更されました。
- `sdk-python.md`では、リンクと説明文の簡略化が行われ、冗長な表現が削除されました。

# Insights
このドキュメントにおける微調整は、ユーザー体験を向上させるための良い例です。まず、`azure-ai-foundry.md`において「国」だけでなく「地域」も考慮に入れた表現に変更されたことは、特に多言語・多地域に対応したサービスを提供する上で重要です。具体的に国と地域を選択するよう指示することで、サービス利用者がより精確なデータを入力でき、それによって結果の信頼性も向上します。

一方、`sdk-python.md`の更新では、冗長な表現が削除されリンクのフォーマットが統一されたことで、ドキュメントの可読性が向上しています。特に関数名が明示されている箇所などで、リンクを削除することでシンプルになり、読者がよりスムーズに情報を受け取ることができます。

これらの変更は外からは小さく見えるかもしれませんが、ユーザーがドキュメントを参照する際の利便性を向上させるための重要なステップであり、結果的により良いユーザー体験に貢献するものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-ai-foundry.md](#item-41c23c) | minor update | 説明の微調整: 'Select country hint'の変更 (Locale: ja_JP) | modified | 1 | 1 | 2 | 
| [sdk-python.md](#item-33436a) | minor update | テキストリンクの簡略化と説明文の修正 (Locale: ja_JP) | modified | 4 | 6 | 10 | 


# Modified Contents
## articles/ai-services/language-service/language-detection/includes/quickstarts/azure-ai-foundry.md{#item-41c23c}

<details>
<summary>Diff</summary>
````diff
@@ -38,7 +38,7 @@ In **Configuration** there are the following options:
 |--------------------|-----------------------------------------|
 |Select API version  | Select which version of the API to use.    |
 |Select model version| Select which version of the model to use.|
-|Select country hint| Select the origin country of the input text. |
+|Select country hint| Select the origin country/region of the input text. |
 
 After your operation is completed, the **Details** section contains the following fields for the most detected language and script:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "説明の微調整: 'Select country hint'の変更 (Locale: ja_JP)"
}
```

### Explanation
この変更では、`azure-ai-foundry.md`というファイル内のテキストに対してマイナーな更新が行われました。具体的には、"Select country hint"に関する説明が改善され、"Select the origin country of the input text."から"Select the origin country/region of the input text."に変更されました。この修正により、入力テキストの出所に対する情報が、国だけでなく地域も含まれることを反映しています。この変更は、既存の情報をより明確にし、ユーザーに対して包括的な理解を提供することを目的としています。

## articles/ai-services/language-service/question-answering/includes/sdk-python.md{#item-33436a}

<details>
<summary>Diff</summary>
````diff
@@ -13,12 +13,10 @@ Use this quickstart for the custom question answering client library for Python
 * Get an answer from a body of text that you send along with your question.
 * Get the confidence score for the answer to your question.
 
-[Reference documentation][questionanswering_refdocs] | [Package (PyPI)][questionanswering_pypi_package] | [Additional samples][questionanswering_samples] | [Library source code][questionanswering_client_src] 
+[Package (PyPI)][questionanswering_pypi_package] | [Additional samples][questionanswering_samples] | [Library source code][questionanswering_client_src] 
 
-[questionanswering_client_class]: https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-language-questionanswering/1.0.0/azure.ai.language.questionanswering.html#azure.ai.language.questionanswering.QuestionAnsweringClient
 [questionanswering_client_src]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/cognitivelanguage/azure-ai-language-questionanswering/
 [questionanswering_pypi_package]: https://pypi.org/project/azure-ai-language-questionanswering/
-[questionanswering_refdocs]: https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-language-questionanswering/1.0.0/azure.ai.language.questionanswering.html
 [questionanswering_samples]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/cognitivelanguage/azure-ai-language-questionanswering/samples/README.md
 
 ## Prerequisites
@@ -48,7 +46,7 @@ pip install azure-ai-language-questionanswering
 
 ### Generate an answer from a project
 
-The example below will allow you to query a project using [get_answers](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-language-questionanswering/1.0.0/azure.ai.language.questionanswering.html#azure.ai.language.questionanswering.QuestionAnsweringClient.get-answers) to get an answer to your question. You can copy this code into a dedicated .py file or into a cell in [Jupyter Notebook/Lab](https://jupyter.org/).
+The example below will allow you to query a project using get_answers to get an answer to your question. You can copy this code into a dedicated .py file or into a cell in [Jupyter Notebook/Lab](https://jupyter.org/).
 
 You need to update the code below and provide your own values for the following variables.
 
@@ -137,7 +135,7 @@ Confidence Score: 0.0
 
 ## Query text without a project
 
-You can also use custom question answering without a project with [get_answers_from_text](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-language-questionanswering/1.0.0/azure.ai.language.questionanswering.html#azure.ai.language.questionanswering.QuestionAnsweringClient.get-answers-from-text). In this case, you provide custom question answering with both a question and the associated text records you would like to search for an answer at the time the request is sent.
+You can also use custom question answering without a project with get_answers_from_text. In this case, you provide custom question answering with both a question and the associated text records you would like to search for an answer at the time the request is sent.
 
 For this example, you only need to modify the variables for `endpoint` and `credential`.
 
@@ -184,5 +182,5 @@ A: Power and charging. It takes two to four hours to charge the Surface Pro 4 ba
 Confidence Score: 0.9254655838012695
 ```
 
-In this case, we iterate through all responses and only return the response with the highest confidence score that is greater than 0.9. To understand more about the options available with [get_answers_from_text](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-language-questionanswering/1.0.0/azure.ai.language.questionanswering.html#azure.ai.language.questionanswering.QuestionAnsweringClient.get-answers-from-text), review the [AnswersFromTextOptions parameters](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-language-questionanswering/1.0.0/azure.ai.language.questionanswering.models.html#azure.ai.language.questionanswering.models.AnswersFromTextOptions).
+In this case, we iterate through all responses and only return the response with the highest confidence score that is greater than 0.9. To understand more about the options available with get_answers_from_text, review the [AnswersFromTextOptions parameters](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-language-questionanswering/1.0.0/azure.ai.language.questionanswering.models.html#azure.ai.language.questionanswering.models.AnswersFromTextOptions).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキストリンクの簡略化と説明文の修正 (Locale: ja_JP)"
}
```

### Explanation
この変更は、`sdk-python.md`ファイルに対するマイナーな更新を含んでいます。主な内容は、リンクの前の説明文やコード例からの冗長な表現を削除して、より簡潔で明瞭な表現に修正することです。具体的には、特定の関数名前のリンク記述を削除し、フォーマットを統一しています。また、コード内の関数名をテキスト内で明示した際に、特にリンク形式を用いずにそのままの形で示すようにしています。これにより、ドキュメントの可読性が向上し、ユーザーが直感的に理解しやすくなることを目的としています。


