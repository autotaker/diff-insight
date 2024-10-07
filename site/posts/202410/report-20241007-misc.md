---
date: '2024-10-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1b56c27...MicrosoftDocs:43a3b87
summary: この変更は、文書の内容を細かく更新し、特にユーザーの理解を助けることを目的としたものです。新機能として、コンテナのデータ処理と利用できるリソースに関する詳細が追加され、セキュリティおよびデータガバナンスへの説明が強化されています。特に破壊的な変更はなく、情報の明確化が図られています。また、モデルライフサイクルに関する見出しや表現の修正が行われ、情報の正確性が向上しています。これにより、Azure
  AIサービスのユーザーは、セキュリティ要件やコンプライアンス遵守の観点から、より信頼性のある情報を得ることができます。全体的に、このアップデートはユーザーエクスペリエンスの向上と製品戦略の一環として重要です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1b56c27...MicrosoftDocs:43a3b87){target="_blank"}

# Highlights
この変更に関連するハイライトは、2つのたとえにわたって文書の内容を細かく更新したことです。特に、新しい情報の追加や表現の修正によって、ユーザーの理解を助けることを目的としています。新機能としては、セキュリティおよびデータガバナンスへの説明が強化され、破壊的な変更は特に含まれていません。

## New features
- コンテナのデータ処理と利用できるリソースに関する詳細な説明が追加されました。

## Breaking changes
- 特に破壊的な変更はありませんでしたが、情報の明確化が行われています。

## Other updates
- 「モデルライフサイクル」ドキュメントにおける見出しや表現の修正が行われ、情報の正確性が向上しています。

# Insights
今回のコード変更は、Azure AIサービスを利用するユーザーにとって極めて重要なアップデートといえます。ドキュメントインテリジェンスサービスに関しては、セキュリティやデータガバナンスの観点からコンテナの動作がさらに明確にされており、企業のコンプライアンス遵守をサポートする情報が提供されています。多様化するセキュリティ要件に応える形で、特定のデータ処理に対する制限を明確にすることで、ユーザーの信頼性が向上することが期待されます。

モデルライフサイクルに関連する更新では、PII（個人情報検出）のプレビューが外れることで、機能が成熟してきたことを示しています。さらに、機能に対応するモデルバージョンの情報がアップデートされ、読み手にとっての理解度が向上する意図が感じられます。特に、大規模なAIモデルやサービシーズを扱うデベロッパーや企業の方々にとって、詳細かつ正確な情報は運用の効率化を助けるものになるでしょう。これらの小さいながらも重要な文書修正は、長期的な製品戦略やユーザーエクスペリエンスの向上に寄与しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [install-run.md](#item-e32e11) | minor update | インストールと実行に関する文書の更新 | modified | 1 | 1 | 2 | 
| [model-lifecycle.md](#item-417f3f) | minor update | モデルライフサイクルに関する文書の修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/document-intelligence/containers/install-run.md{#item-e32e11}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ ms.author: lajanuar
 
 **This content applies to:** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** ![checkmark](../media/yes-icon.png) **v3.1 (GA)**
 
-Azure AI Document Intelligence is an Azure AI service that lets you build automated data processing software using machine-learning technology. Document Intelligence enables you to identify and extract text, key/value pairs, selection marks, table data, and more from your documents. The results are delivered as structured data that ../includes the relationships in the original file.
+Azure AI Document Intelligence is an Azure AI service that lets you build automated data processing software using machine-learning technology. Document Intelligence enables you to identify and extract text, key/value pairs, selection marks, table data, and more from your documents. The results are delivered as structured data that ../includes the relationships in the original file. Containers process only the data provided to them and solely utilize the resources they are permitted to access. Containers cannot process data from other regions.
 
 In this article you can learn how to download, install, and run Document Intelligence containers. Containers enable you to run the Document Intelligence service in your own environment. Containers are great for specific security and data governance requirements.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インストールと実行に関する文書の更新"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスサービスのインストールと実行に関する説明を更新したものです。具体的には、Azure AI Document Intelligence の機能についての説明に新しい情報が追加されました。新しい内容では、コンテナが自身に提供されたデータのみを処理し、許可されたリソースだけを利用すること、また、コンテナが他の地域からのデータを処理できないことについて言及しています。この情報は、セキュリティやデータガバナンス要件に関連する重要な点を強調しています。全体として、この更新は、ユーザーに対してコンテナの利用における制限と目的をより明確に伝えることを目的としています。

## articles/ai-services/language-service/concepts/model-lifecycle.md{#item-417f3f}

<details>
<summary>Diff</summary>
````diff
@@ -43,11 +43,11 @@ Use the table below to find which model versions are supported by each feature:
 | Entity Linking                                      | `latest*`                                      |                                             |
 | Named Entity Recognition (NER)                      | `latest*`                                      | `2023-04-15-preview**`                      |
 | Personally Identifiable Information (PII) detection | `latest*`                                      | `2023-04-15-preview**`                      | 
-| PII detection for conversations (Preview)           | `latest*`                                      | `2023-04-15-preview**`                      |
+| PII detection for conversations                     | `latest*`                                      | `2023-04-15-preview**`                      |
 | Question answering                                  | `latest*`                                      |                                             |
 | Text Analytics for health                           | `latest*`                                      | `2022-08-15-preview`, `2023-01-01-preview**`|
 | Key phrase extraction                               | `latest*`                                      |                                             | 
-| Summarization                              |  `latest*`                                      |                       |
+| Summarization                                       |  `latest*`                                     |                                             |
 
 
 \* Latest Generally Available (GA) model version
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルに関する文書の修正"
}
```

### Explanation
この変更は、「モデルライフサイクル」ドキュメントの一部を修正したもので、特に言及されている機能に関連するモデルバージョンについての情報を更新しました。変更された部分では、会話における個人情報の検出（PII検出）の項目が簡潔に修正され、見出しが「PII detection for conversations (Preview)」から「PII detection for conversations」という表現に変更されています。また、要約機能に関するテーブルの説明も更新され、より明確な表現となりました。これにより、読者がさまざまな機能に対応するモデルバージョンを理解しやすくなっています。全体として、この更新は情報の正確性を高め、読者の理解を促進することを目指しています。


