---
date: '2026-08-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:431b414...MicrosoftDocs:a8ff591
summary: このコードの変更は、Azure AIサービス関連のドキュメントの軽微な更新を含んでおり、主な新機能として`ai-usage`フィールドの追加があります。このフィールドはAIの使用を示す「ai-assisted」と設定されました。破壊的変更は特にありませんが、サービス名の更新が行われており、`ms.service`フィールドの値が変更されています。また、文書の日付が最新に更新され、新たに「ドイツ語」がサポート言語に追加されました。SDKドキュメントのサービス名も「azure-ai-language」から「azure-language-foundry-tools」に変更されています。全体として、これらの更新はAzureの最新情報提供に対するコミットメントを示しており、ユーザー体験の向上が図られています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:431b414...MicrosoftDocs:a8ff591){target="_blank"}

# ハイライト

このコードの変更は、Azure AIサービス関連の様々なドキュメントの軽微な更新を含んでいます。主な新機能および重要な変更点は以下の通りです。

## 新機能
- 文書に`ai-usage`フィールドが追加され、AIの使用を明示するために「ai-assisted」と設定されました。

## 破壊的変更
- 特に破壊的な変更はありませんが、サービス名の更新が行われており、これにより利用者が混乱する可能性があります。具体的には、`ms.service`フィールドの値が変更されました。

## その他の更新
- 複数の文書の日付が最新のものに更新されました。
- 言語サポート情報が更新され、「ドイツ語」が新たにサポートされる言語リストに追加されました。
- 各SDK（C#, Java, Node.js, Python）に関するドキュメントのサービス名が「azure-ai-language」から「azure-language-foundry-tools」に更新されました。

# インサイト

このドキュメントの更新では、Azure AIサービスに関する情報を最新化し、ユーザーエクスペリエンスを向上させるための複数の軽微な調整が行われています。

例えば、`ai-usage`フィールドの追加は、ドキュメント利用者に対してAIがどのように用いられているかを明確に伝えるための重要なステップです。この変更は、サービスを利用する際の信頼性を高め、利用者がAI機能の恩恵を明確に理解する手助けとなります。

日付の更新は、ドキュメントの最新性を保証するためのものであり、ユーザーに対して最新かつ正確な情報を提供することができます。また、言語サポートの拡充により、さらなる多様な言語に対応可能になったことで、国際化を推進し、ユーザーの利便性を向上させています。

サービス名の変更については、Azureのサービスが進化し続ける中で、一貫性を保ち、正確な情報を提供するために重要な調整です。この変更により、最新のサービス構造に合わせた正確な利用が見込めます。

全体として、これらの更新は、常に最新の情報を提供し続けるというAzureのコミットメントを示しており、利用者が最新の機能とサービスの進化を継続的に享受できるよう設計されています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [language-support.md](#item-45bafd) | minor update | 言語サポートの更新 | modified | 5 | 4 | 9 | 
| [service-limits.md](#item-6df7a9) | minor update | サービス情報の更新 | modified | 1 | 1 | 2 | 
| [conversation-pii-overview.md](#item-e1dc30) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [redact-conversation-pii.md](#item-0d6332) | minor update | 言語サポート情報の更新 | modified | 3 | 2 | 5 | 
| [language-support.md](#item-d332b1) | minor update | 言語サポート情報の拡充 | modified | 3 | 1 | 4 | 
| [csharp-sdk.md](#item-041480) | minor update | サービス情報の更新 | modified | 1 | 1 | 2 | 
| [java-sdk.md](#item-c604e9) | minor update | サービス情報の更新 | modified | 1 | 1 | 2 | 
| [nodejs-sdk.md](#item-8bd4c1) | minor update | サービス情報の更新 | modified | 1 | 1 | 2 | 
| [python-sdk.md](#item-c8a5f8) | minor update | サービス情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/language-service/concepts/language-support.md{#item-45bafd}

<details>
<summary>Diff</summary>
````diff
@@ -6,8 +6,9 @@ author: laujan
 manager: mcleans
 ms.service: azure-language-foundry-tools
 ms.topic: concept-article
-ms.date: 04/09/2026
+ms.date: 08/17/2026
 ms.author: lajanuar
+ai-usage: ai-assisted
 ---
 # Language support for Language features
 
@@ -47,10 +48,10 @@ Use this article to learn about the languages currently supported by different f
 | Fijian                | `fj`          |                                                                                 |                                                                                                |                                                                                                       |                                                         | &check;                                                         |                                                                       |                                                                                  |                                                                         |                                                                                                                        |                                                                                                   |                                                                 |                                                                                                           |                                                                                                   |                                                                               |                                                                                   |                                                                                                    |
 | Filipino              | `tl`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               |                                                                                  |                                                                         |                                                                                                                        |                                                                                                   |                                                                 | &check;                                                                                                   |  &check;                                                                                          |                                                                               |                                                                                   |                                                                                                    |
 | Finnish               | `fi`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               | &check;                                                                          |                                                                         | &check;                                                                                                                |                                                                                                   | &check;                                                         | &check;                                                                                                   | &check;                                                                                           |                                                                               |                                                                                   |                                                                                                    |
-| French                | `fr`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               | &check;                                                                          | &check;                                                                 | &check;                                                                                                                |                                                                                                   | &check;                                                         | &check;                                                                                                   | &check;                                                                                           | &check;                                                                       | &check;                                                                           |                                                                                                    |
+| French                | `fr`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               | &check;                                                                          | &check;                                                                 | &check;                                                                                                                | &check;                                                                                           | &check;                                                         | &check;                                                                                                   | &check;                                                                                           | &check;                                                                       | &check;                                                                           |                                                                                                    |
 | Galician              | `gl`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               |                                                                                  |                                                                         | &check;                                                                                                                |                                                                                                   | &check;                                                         | &check;                                                                                                   |  &check;                                                                                          |                                                                               |                                                                                   |                                                                                                    |
 | Georgian              | `ka`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               |                                                                                  |                                                                         | &check;                                                                                                                |                                                                                                   |                                                                 | &check;                                                                                                   | &check;                                                                                           |                                                                               |                                                                                   |                                                                                                    |
-| German                | `de`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               | &check;                                                                          | &check;                                                                 | &check;                                                                                                                |                                                                                                   | &check;                                                         | &check;                                                                                                   | &check;                                                                                           | &check;                                                                       | &check;                                                                           |                                                                                                    |
+| German                | `de`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               | &check;                                                                          | &check;                                                                 | &check;                                                                                                                | &check;                                                                                           | &check;                                                         | &check;                                                                                                   | &check;                                                                                           | &check;                                                                       | &check;                                                                           |                                                                                                    |
 | Greek                 | `el`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               |                                                                                  |                                                                         | &check;                                                                                                                |                                                                                                   | &check;                                                         | &check;                                                                                                   | &check;                                                                                           |                                                                               |                                                                                   |                                                                                                    |
 | Gujarati              | `gu`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               |                                                                                  |                                                                         | &check;                                                                                                                |                                                                                                   | &check;                                                         | &check;                                                                                                   | &check;                                                                                           |                                                                               |                                                                                   |                                                                                                    |
 | Haitian               | `ht`          |                                                                                 |                                                                                                |                                                                                                       |                                                         | &check;                                                         |                                                                       |                                                                                  |                                                                         |                                                                                                                        |                                                                                                   |                                                                 |                                                                                                           |                                                                                                   |                                                                               |                                                                                   |                                                                                                    |
@@ -112,7 +113,7 @@ Use this article to learn about the languages currently supported by different f
 | Slovak                | `sk`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               |                                                                                  |                                                                         | &check;                                                                                                                |                                                                                                   | &check;                                                         | &check;                                                                                                   | &check;                                                                                           |                                                                               |                                                                                   |                                                                                                    |
 | Slovenian             | `sl`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               |                                                                                  |                                                                         | &check;                                                                                                                |                                                                                                   | &check;                                                         | &check;                                                                                                   | &check;                                                                                           |                                                                               |                                                                                   |                                                                                                    |
 | Somali                | `so`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               |                                                                                  |                                                                         | &check;                                                                                                                |                                                                                                   |                                                                 | &check;                                                                                                   | &check;                                                                                           |                                                                               |                                                                                   |                                                                                                    |
-| Spanish               | `es`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               | &check;                                                 | &check;                                                         | &check;                                                               | &check;                                                                          | &check;                                                                 | &check;                                                                                                                |                                                                                                   | &check;                                                         | &check;                                                                                                   | &check;                                                                                           | &check;                                                                       |                                                                                   |                                                                                                    |
+| Spanish               | `es`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               | &check;                                                 | &check;                                                         | &check;                                                               | &check;                                                                          | &check;                                                                 | &check;                                                                                                                | &check;                                                                                           | &check;                                                         | &check;                                                                                                   | &check;                                                                                           | &check;                                                                       |                                                                                   |                                                                                                    |
 | Sundanese             | `su`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               |                                                                                  |                                                                         |                                                                                                                        |                                                                                                   |                                                                 | &check;                                                                                                   | &check;                                                                                           |                                                                               |                                                                                   |                                                                                                    |
 | Swahili               | `sw`          | &check;                                                                         | &check;                                                                                        | &check;                                                                                               |                                                         | &check;                                                         | &check;                                                               |                                                                                  |                                                                         | &check;                                                                                                                |                                                                                                   |                                                                 | &check;                                                                                                   | &check;                                                                                           |                                                                               |                                                                                   |                                                                                                    |
 | Swati                 | `ss`          |                                                                                 |                                                                                                |                                                                                                       |                                                         |                                                                 |                                                                       |                                                                                  |                                                                         | &check;                                                                                                                |                                                                                                   |                                                                 |                                                                                                           |                                                                                                   |                                                                               |                                                                                   |                                                                                                    |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サポートの更新"
}
```

### Explanation
この変更は、言語サポートに関するドキュメントの軽微な更新を含んでいます。具体的には、以下の内容が修正されています。

1. 日付の更新: 文書の日付が2026年4月9日から2026年8月17日に変更されました。これにより、情報がより最新のものになりました。

2. AI使用関連の情報追加: `ai-usage`という新しいフィールドが追加され、`ai-assisted`と設定されています。これにより、このサービスのAI機能に関する詳細な情報が提供されるようになりました。

3. 言語一覧の整合性: 幾つかの言語（フランス語、ドイツ語、スペイン語など）の行が修正されていますが、これらの修正は主にフォーマットや整合性に関するもので、実際の言語情報には変更がありません。

この変更は、全体的な文書の一貫性を保ちつつ、日付や新しいAI機能の内容を反映させるために行われました。

## articles/ai-services/language-service/custom-text-classification/service-limits.md{#item-6df7a9}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ description: Learn about the data and rate limits when using custom text classif
 author: laujan
 manager: mcleans
 ms.date: 06/30/2026
-ms.service: azure-ai-language
+ms.service: azure-language-foundry-tools
 ms.topic: limits-and-quotas
 ms.author: lajanuar
 ms.custom: language-service-custom-classification, references_regions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス情報の更新"
}
```

### Explanation
この変更は、カスタムテキスト分類サービスの制限に関するドキュメントにおける軽微な更新を示しています。以下の点が修正されています。

1. サービス名の更新: `ms.service`フィールドの値が「azure-ai-language」から「azure-language-foundry-tools」に変更されました。この修正により、リソースに関連するサービス名が最新のものに更新されています。

2. 簡単な文の修正: 他のメタデータには変更はありませんが、文書の説明や内容が引き続き関連性を持っていることを考慮すると、サービス名の更新が主な変更内容となります。

この変更により、ドキュメントが最新のサービスに即した内容となり、正確性が向上しました。

## articles/ai-services/language-service/personally-identifiable-information/conversation-pii-overview.md{#item-e1dc30}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: mcleans
 ms.service: azure-language-foundry-tools
 ms.topic: overview
-ms.date: 06/02/2026
+ms.date: 08/12/2026
 ms.author: lajanuar
 ms.custom: language-service-pii
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
この変更は、個人を特定可能な情報（PII）に関する会話概要のドキュメントの日付を更新する軽微な変更を示しています。具体的な修正内容は以下の通りです。

1. 日付の更新: 文書の日付が2026年6月2日から2026年8月12日に変更されました。これにより、使用される情報がより新しいものになり、読者にとって最新のコンテンツを提供することが可能になります。

この変更は、他のドキュメントのメタデータには影響を与えず、主に記録の整合性を保つために行われました。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-conversation-pii.md{#item-0d6332}

<details>
<summary>Diff</summary>
````diff
@@ -6,9 +6,10 @@ author: laujan
 manager: mcleans
 ms.service: azure-language-foundry-tools
 ms.topic: how-to
-ms.date: 06/02/2026
+ms.date: 08/17/2026
 ms.author: lajanuar
 ms.custom: language-service-pii
+ai-usage: ai-assisted
 ---
 # Detect and redact Personally Identifiable Information in conversations
 
@@ -25,7 +26,7 @@ By default, this feature uses the latest available AI model on your input. You c
 
 ### Language support
 
-For more information, *see* the [PII Language Support page](../language-support.md). Currently the conversational PII GA model only supports the English language. The preview model and API support the [same list languages](../../concepts/language-support.md) as the other Languages.
+For the languages supported by the GA and preview versions, see [Conversation PII language support](../language-support.md?tabs=conversation-pii#conversation-pii-language-support).
 
 ### Region support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サポート情報の更新"
}
```

### Explanation
この変更は、会話における個人を特定可能な情報（PII）の検出および修正に関するドキュメントの軽微な更新を示しています。以下の点が修正されています。

1. 日付の更新: 文書の日付が2026年6月2日から2026年8月17日に変更され、最新の情報へと更新されました。

2. 新しいメタデータの追加: `ai-usage`フィールドが追加され、値は「ai-assisted」となりました。これは、AIを利用した機能の使用を明示的に示しています。

3. 言語サポートのリンクの更新: 言語サポートに関する説明が修正され、具体的には「PII Language Support page」へのリンクが変更されました。新しいリンクでは、GA（一般提供版）およびプレビュー版の言語サポートが明確に示されています。

これらの変更により、ドキュメントはより正確で読みやすくなり、最新の情報を反映しています。

## articles/ai-services/language-service/personally-identifiable-information/language-support.md{#item-d332b1}

<details>
<summary>Diff</summary>
````diff
@@ -6,9 +6,10 @@ author: laujan
 manager: mcleans
 ms.service: azure-language-foundry-tools
 ms.topic: concept-article
-ms.date: 06/10/2026
+ms.date: 08/17/2026
 ms.author: lajanuar
 ms.custom: language-service-pii, build-2024
+ai-usage: ai-assisted
 ---
 <!-- markdownlint-disable MD025 -->
 # Personally Identifiable Information (PII) detection language support
@@ -120,6 +121,7 @@ Conversation PII generally available (GA) version currently supports the followi
 
 * English
 * French
+* German
 * Spanish
 
 # [Document-based PII](#tab/document-based-pii)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サポート情報の拡充"
}
```

### Explanation
この変更は、個人を特定可能な情報（PII）の検出に関する言語サポート情報の軽微な更新を示しています。主な修正点は以下の通りです。

1. 日付の更新: 文書の日付が2026年6月10日から2026年8月17日に変更され、最新の情報に更新されました。

2. 新しいメタデータの追加: `ai-usage`フィールドが追加され、値は「ai-assisted」となりました。これにより、AIを利用した機能の使用が明示的に示されています。

3. 言語サポートの更新: 対応言語のリストに「ドイツ語」が追加されました。これにより、利用可能な言語の選択肢が広がり、ユーザーにとっての利便性が向上します。

これらの変更は、全体的に情報の正確性と利便性を高めるものとなっています。

## articles/ai-services/language-service/summarization/includes/quickstarts/csharp-sdk.md{#item-041480}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ author: laujan
 ms.author: lajanuar
 manager: mcleans
 ms.date: 06/30/2026
-ms.service: azure-ai-language
+ms.service: azure-language-foundry-tools
 ms.topic: include
 ms.custom:
   - build-2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス情報の更新"
}
```

### Explanation
この変更は、C# SDKに関するドキュメントの軽微な更新を示しています。主な修正点は以下の通りです。

1. 日付の更新: 文書の日付は変更されていませんが、他のメタデータが更新されました。

2. サービス情報の更新: `ms.service`フィールドが「azure-ai-language」から「azure-language-foundry-tools」に変更されました。この変更は、使用するサービスの名称を正確に反映させるためのものです。

これにより、ユーザーに提供される情報が最新のものになり、適切なサービスの使用に貢献します。全体として、これらの修正は文書の正確性を向上させるものとなっています。

## articles/ai-services/language-service/summarization/includes/quickstarts/java-sdk.md{#item-c604e9}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ author: laujan
 ms.author: lajanuar
 manager: mcleans
 ms.date: 06/30/2026
-ms.service: azure-ai-language
+ms.service: azure-language-foundry-tools
 ms.topic: include
 ms.custom:
   - devx-track-java
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス情報の更新"
}
```

### Explanation
この変更は、Java SDKに関するドキュメントの軽微な更新を示しています。主な修正点は以下の通りです。

1. 日付の更新: 文書の日付は変更されていませんが、他のメタデータが調整されています。

2. サービス情報の更新: `ms.service`フィールドが「azure-ai-language」から「azure-language-foundry-tools」に変更されました。この変更は、正確なサービス名を反映させるために行われました。

この変更により、利用者は最新のサービス情報にアクセスできるようになり、正確な情報に基づいて技術的な決定を行うことが可能になります。全体として、これらの修正は文書の精度向上に寄与しています。

## articles/ai-services/language-service/summarization/includes/quickstarts/nodejs-sdk.md{#item-8bd4c1}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ author: laujan
 ms.author: lajanuar
 manager: mcleans
 ms.date: 06/30/2026
-ms.service: azure-ai-language
+ms.service: azure-language-foundry-tools
 ms.topic: include
 ms.custom:
   - devx-track-js
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス情報の更新"
}
```

### Explanation
この変更は、Node.js SDKに関するドキュメントの軽微な更新を示しています。主な修正点は次の通りです。

1. 日付の更新: 文書の日付はそのままですが、その他のメタデータが調整されています。

2. サービス情報の更新: `ms.service`フィールドが「azure-ai-language」から「azure-language-foundry-tools」に変更されました。この調整は、最新のサービス名を反映するために行われました。

これにより、利用者は正確かつ最新の情報に基づいて、技術的な意思決定を行うことができるようになります。全体として、これらの修正は文書の信頼性を向上させることに寄与しています。

## articles/ai-services/language-service/summarization/includes/quickstarts/python-sdk.md{#item-c8a5f8}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,7 @@
 author: laujan
 ms.author: lajanuar
 ms.date: 06/30/2026
-ms.service: azure-ai-language
+ms.service: azure-language-foundry-tools
 ms.topic: include
 ms.custom:
   - build-2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス情報の更新"
}
```

### Explanation
この変更は、Python SDKに関するドキュメントの軽微な更新を示しています。主な修正点は以下の通りです。

1. 日付の更新: ドキュメントの日付は変更されていませんが、他の情報が更新されています。

2. サービス情報の更新: `ms.service`フィールドが「azure-ai-language」から「azure-language-foundry-tools」に変更されました。この変更は、最新のサービス名に合わせるために行われました。

これにより、利用者は正確な最新情報にアクセスでき、より良い技術的決定を行うことができるようになります。全体的に、この修正はドキュメントの信頼性を向上させることに寄与しています。


