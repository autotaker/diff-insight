---
date: '2025-04-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0fdb6d4...MicrosoftDocs:bb349ba
summary: このコード差分では、Azureのドキュメントインテリジェンスと言語サービスに関連するリンクとテキストの微調整が行われ、利便性が向上しました。新しいサンプルリンクに更新されたり、不要なリンクが削除された結果、開発者や読者のための文書の保守性と可読性が高まっています。新機能の追加や重大な変更はなく、主にリンクの更新と内容の簡潔化が図られています。これにより、最新の実装例に基づいて学ぶことができ、読者が集中しやすくなっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0fdb6d4...MicrosoftDocs:bb349ba){target="_blank"}

# ハイライト
このコード差分では、Azureのドキュメントインテリジェンスと言語サービス関連のドキュメントにおけるいくつかのリンクとテキストの微調整が行われています。新しいサンプルリンクへの更新や不要なリンクの削除が含まれており、開発者や読者への利便性が向上しています。

## 新機能
特に新しい機能は追加されていません。

## 重大な変更
重大な変更はなく、既存の機能や構造に影響を与える更新はありません。

## その他の更新
- JavaScriptサンプルリンクが最新のものに更新されました。
- Python SDKのドキュメントにおいて、特定の用語のリンクが削除され、シンプルなテキストに変わりました。

# インサイト
この変更は主にドキュメントの保守性と可読性を高めることを目的としています。Azureのドキュメントインテリジェンスに関するカスタムモデル作成ガイドでは、開発者が旧式のサンプルコードに惑わされずに、最新の実装例に基づいて学べるようにサンプルリンクが更新されています。これにより、開発者は安心して最新のベストプラクティスを活用することができるでしょう。

一方、言語サービスにおける質問応答機能のPython SDKドキュメントでは、リンクが削除されることでドキュメントが簡潔になり、読者が集中力を保ちやすく、内容の理解がスムーズになります。特にリンクが頻繁に壊れる可能性がある場合、リンクを削除して直接的なテキストにすることで文書保守における複雑さが軽減されます。こうした変更は、ユーザーエクスペリエンスを向上させるための重要なステップであり、リアルタイムのフィードバックを基に迅速に対応できるドキュメント管理の柔軟性を示しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [compose-custom-models.md](#item-bfda06) | minor update | カスタムモデル作成ガイドのJavaScriptリンク更新 | modified | 2 | 2 | 4 | 
| [sdk-python.md](#item-33436a) | minor update | Python SDKドキュメントのテキスト修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/document-intelligence/how-to-guides/compose-custom-models.md{#item-bfda06}

<details>
<summary>Diff</summary>
````diff
@@ -434,7 +434,7 @@ Use the programming language code of your choice to create a composed model that
 
 * [**Java**](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/ComposeDocumentModel.java).
 
-* [**JavaScript**](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v3/javascript/createComposedModel.js).
+* [**JavaScript**](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/composeModel.js).
 
 * [**Python**](https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-formrecognizer_3.3.0/sdk/formrecognizer/azure-ai-formrecognizer/samples/v3.1/sample_create_composed_model.py)
 
@@ -468,7 +468,7 @@ Using the programming language of your choice to analyze a form or document with
 
 * [**Java**](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeCustomDocumentFromUrl.java)
 
-* [**JavaScript**](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v3/javascript/recognizeCustomForm.js)
+* [**JavaScript**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript)
 
 * [**Python**](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/samples/v3.1/sample_recognize_custom_forms.py)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムモデル作成ガイドのJavaScriptリンク更新"
}
```

### Explanation
この変更は、Azureのドキュメントインテリジェンスに関連するカスタムモデル作成ガイドのJavaScriptサンプルリンクを更新しています。具体的には、以下の２つの部分が修正されました：

1. 以前のJavaScriptサンプルリンク `createComposedModel.js` が更新され、新しいリンク `composeModel.js` に置き換えられました。
2. `recognizeCustomForm.js` のリンクが更新され、JavaScriptサンプルディレクトリへの新しいパスに変更されました。

これにより、最新のサンプルコードへのアクセスが提供され、開発者が最新の実装方法に基づいて作業できるようにサポートされています。

## articles/ai-services/language-service/question-answering/includes/sdk-python.md{#item-33436a}

<details>
<summary>Diff</summary>
````diff
@@ -112,7 +112,7 @@ Confidence Score: 0.9185
 
 The confidence score returns a value between 0 and 1. You can think of this like a percentage and multiply by 100 so a confidence score of 0.9185 means custom question answering is 91.85% confident this is the correct answer to the question based on the project.
 
-If you want to exclude answers where the confidence score falls below a certain threshold, you can modify the [AnswerOptions](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-language-questionanswering/1.0.0/azure.ai.language.questionanswering.models.html#azure.ai.language.questionanswering.models.AnswersOptions) to add the `confidence_threshold` parameter.
+If you want to exclude answers where the confidence score falls below a certain threshold, you can modify the AnswerOptions to add the `confidence_threshold` parameter.
 
 ```python
         output = client.get_answers(
@@ -182,5 +182,5 @@ A: Power and charging. It takes two to four hours to charge the Surface Pro 4 ba
 Confidence Score: 0.9254655838012695
 ```
 
-In this case, we iterate through all responses and only return the response with the highest confidence score that is greater than 0.9. To understand more about the options available with get_answers_from_text, review the [AnswersFromTextOptions parameters](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-language-questionanswering/1.0.0/azure.ai.language.questionanswering.models.html#azure.ai.language.questionanswering.models.AnswersFromTextOptions).
+In this case, we iterate through all responses and only return the response with the highest confidence score that is greater than 0.9. To understand more about the options available with get_answers_from_text, review the AnswersFromTextOptions parameters.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKドキュメントのテキスト修正"
}
```

### Explanation
この変更は、Azureの言語サービスにおける質問応答機能のPython SDKに関連するドキュメントの修正です。具体的には以下の2つの文が編集されました：

1. `AnswerOptions` という言葉のリンクが削除され、単なるテキストに修正されました。これにより、読者がこの用語をクリックして詳細を確認するオプションがなくなりますが、説明自体は引き続き理解可能です。

2. `AnswersFromTextOptions` へのリンクも削除され、対象の文はリンクなしの通常のテキストになりました。

これらの変更は、ドキュメントの表現を一貫性のあるものにし、リンクの混乱を避けるための微調整です。これにより、読者がドキュメントを読みやすくなっています。


