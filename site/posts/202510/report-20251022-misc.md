---
date: '2025-10-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a411aa0...MicrosoftDocs:46d1709
summary: このドキュメントの変更は、AIサービスの「モデルライフサイクル」に関する情報のマイナーアップデートです。特に、APIの機能とサポートされるバージョンに関するテーブルが改訂され、新たに「その他のサポートバージョン」カラムが追加されました。これにより、各機能に対する詳細なバージョン情報が提供され、開発者が適切なバージョンを選ぶ際のガイダンスが強化されました。破壊的変更はなく、今後の開発効率と精度向上が期待されます。また、具体的なAPI機能に関する最新のプレビューバージョン情報も更新されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a411aa0...MicrosoftDocs:46d1709){target="_blank"}

# Highlights
このドキュメントの変更は、「AIサービス: 言語サービス」の「モデルライフサイクル」に関する情報のマイナーアップデートであり、特にAPIの機能とサポートされるバージョンについてのテーブルが改訂されました。新たなカラム「その他のサポートバージョン」が追加され、機能ごとの詳細なバージョン情報が提供されるようになりました。

## New features
- API各機能のテーブルに「その他のサポートバージョン」カラムが追加されました。
- 各機能に新しいサポートバージョンが追加され、バージョン情報がより詳細になりました。

## Breaking changes
変更に伴う破壊的変更はありません。今回のアップデートは情報の追加と精度向上に主眼を置いています。

## Other updates
- Named Entity RecognitionやPII検出といった具体的API機能について最新のプレビューバージョン情報が追加されました。

# Insights
この更新は、AIサービスのユーザーにとって実用的な情報を提供するものです。特に、APIの各機能にどのバージョンがサポートされているかを詳しく知ることができるため、新たに「その他のサポートバージョン」カラムが追加された点が注目されます。これにより、開発者やエンジニアが特定のAPI機能を利用する際に、適切なバージョンを選択するための明確なガイダンスを得ることができます。また、最新の情報に基づいて機能を利用することで、開発の効率化や精度向上が期待できるでしょう。

今回のマイナーアップデートは、情報の追加と更新がメインであり、破壊的変更は含まれていません。このことは、既存のシステムやプロジェクトに対する影響を最小限に抑えつつ、最新のリソースにアクセスしやすくする目的で行われたと考えられます。特に重要なのは、Named Entity RecognitionやPII検出の新たなプレビューバージョン情報が追加されたことで、開発者が次に何をサポートするかを予測する助けとなる点です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-lifecycle.md](#item-417f3f) | minor update | モデルライフサイクルに関する情報の更新 | modified | 15 | 12 | 27 | 


# Modified Contents
## articles/ai-services/language-service/concepts/model-lifecycle.md{#item-417f3f}

<details>
<summary>Diff</summary>
````diff
@@ -35,18 +35,18 @@ By default, API and SDK requests use the latest Generally Available model. To us
 
 Use the following table to find which model versions support each feature:
 
-| Feature | Supported generally available (GA) version | Latest supported preview versions |
-|--|--|--|
-| Sentiment Analysis and opinion mining | `latest` |  |
-| Language Detection | `latest` |  |
-| Entity Linking | `latest` |  |
-| Named Entity Recognition (NER) | `latest` | `2025-08-01-preview` |
-| Personally Identifiable Information (PII) detection | `latest` | `2025-08-01-preview` |
-| PII detection for conversations | `latest` | `2024-11-01-preview` |
-| Question answering | `latest` |  |
-| Text Analytics for health | `latest` | `2023-04-15-preview` |
-| Key phrase extraction | `latest` |  |
-| Summarization | `latest` | `2025-06-10-preview` (only available for `issue` and `resolution` aspects in conversation summarization) |
+| Feature | Supported generally available (GA) version | Latest supported preview versions | Other supported verision |
+|--|--|--|--|
+| Sentiment Analysis and opinion mining | `latest` |  |  |
+| Language Detection | `latest` |  |  |
+| Entity Linking | `latest` |  |  |
+| Named Entity Recognition (NER) | `latest` | `2025-08-01-preview` | `2025-04-15-preview` |
+| Personally Identifiable Information (PII) detection | `latest` | `2025-08-01-preview` | `2025-04-15-preview` |
+| PII detection for conversations | `latest` | `2024-11-01-preview` | `2023-04-15-preview` |
+| Question answering | `latest` |  |  |
+| Text Analytics for health | `latest` | `2023-04-15-preview` |  |
+| Key phrase extraction | `latest` |  |  |
+| Summarization | `latest` | `2025-06-10-preview` (only available for `issue` and `resolution` aspects in conversation summarization) |  |
 
 
 ## Custom features
@@ -90,6 +90,9 @@ Use the following table to find which API versions support each feature:
 | Conversational language understanding| `2022-05-01`, `2022-10-01-preview`, `2023-04-01`                                    |`2023-04-01`                      |`2022-10-01-preview`  |
 | Custom named entity recognition      | `2022-05-01`, `2022-10-01-preview`, `2023-04-01`, `2023-04-15`, `2023-04-15-preview`|`2023-04-15`                      |`2023-04-15-preview`  |
 | Orchestration workflow               | `2022-05-01`, `2022-10-01-preview`, `2023-04-01`                                    |`2023-04-01`                      |`2022-10-01-preview`  |
+| Named Entity Recognition (NER) | `2025-05-15-preview`, `2024-11-01 (GA)`,`2024-11-15-preview` | `2024-11-01 (GA)` | `2025-05-15-preview` |
+| Personally Identifiable Information (PII) detection  | `2025-05-15-preview`,`2024-11-01 (GA)`,`2024-11-15-preview` | `2024-11-01 (GA)` | `2025-05-15-preview` |
+| PII detection for conversations  | `2025-05-15-preview`,`2024-11-01 (GA)`,`2024-11-15-preview` | `2024-11-01 (GA)` | `2025-05-15-preview` |
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルに関する情報の更新"
}
```

### Explanation
この変更は、「モデルライフサイクル」に関するドキュメント内の情報を更新したもので、主にAPIの各機能とそのサポートされているバージョンに関するテーブルの改訂が含まれています。具体的には、新しいカラム「その他のサポートバージョン」が追加され、各機能に対するより多くのバージョン情報が提供されるようになりました。これにより、ユーザーは利用可能な機能がどのモデルバージョンでサポートされているかについて、より詳細な情報にアクセスできるようになります。

変更の具体的な内容としては、以下の要素が含まれています：
- テーブルに「その他のサポートバージョン」カラムの追加
- 各機能に対して新たに追加されたサポートバージョンの記載（例：Named Entity RecognitionやPII検出の新しいプレビューバージョンなど）
- 各機能のサポート情報が最新のもので更新され、ユーザーが現在利用可能なリソースを正確に把握できるようになっています。

全体として、このマイナーアップデートは、ユーザーがモデルのライフサイクルに関する最新情報を得るための重要な改訂となっています。


