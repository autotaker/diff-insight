---
date: '2025-07-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3f50d3b...MicrosoftDocs:bd40fd4
summary: このコード差分では、いくつかのドキュメントに対する小規模な更新が行われ、新しいカスタムメタデータが追加されたほか、既存のメタデータのフォーマットが改善されました。大きな機能追加や破壊的変更はなく、メタデータは文書管理の支援や特定の機能の強調に役立ちます。特にメタデータがリスト形式に整理されたことにより、情報検索の精度が向上し、ユーザーのナビゲーションが簡素化されることが期待されます。これにより、文書のメンテナンスや情報ガバナンスが向上します。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3f50d3b...MicrosoftDocs:bd40fd4){target="_blank"}

<format>
# Highlights
このコード差分では、さまざまなドキュメントに対して小規模な更新が行われました。主な変更点としては、新しいカスタムメタデータの追加や、既存のメタデータのフォーマット改善が挙げられます。これらのメタデータは、文書の管理を支援し、特定の機能を強調するために使用されます。大きな機能追加や削除されるような破壊的な変更は含まれていません。

## 新機能
- カスタムメタデータ「ms.custom: sfi-image-nochange」「ms.custom: sfi-ropc-nochange」の追加。
- メタデータのリスト形式への改善や管理機能の強化。

## 破壊的変更
- 特にありません。

## その他の更新
- 複数のドキュメントにわたってメタデータの構造が改善され、特定のプロパティが明示的に追加されました。

# Insights
この差分は、複数のAIサービス関連ドキュメントに対する一貫したメタデータ更新を示しています。このようなメタデータは、ドキュメントを運用する上で重要な役割を果たしており、パフォーマンスの追跡、特定の機能の強調、さらにはカスタマイズの促進など、様々な管理機能をサポートします。

特に興味深いのは、メタデータがリスト形式になったことです。これは、異なるトピックや設定を明確に区別しやすくするための改善と捉えられます。この形式により、複数のカスタムプロパティが一つのフィールドに整理され、ユーザーが情報を検索する際の精度が向上します。

この更新は、特に管理機能の一環としてドキュメントのメンテナンスに役立ち、組織の情報ガバナンスの一助となるでしょう。ユーザーにとって、これらのメタデータによってドキュメントの利用やナビゲーションが容易になり、効率と可読性の両面で改善が期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [create-sas-tokens.md](#item-dc2ea3) | minor update | SFI画像に関するメタデータの追加 | modified | 1 | 0 | 1 | 
| [managed-identities-secured-access.md](#item-05ef7b) | minor update | SFI画像に関するメタデータの追加 | modified | 1 | 0 | 1 | 
| [managed-identities.md](#item-be183c) | minor update | SFI画像に関するメタデータの追加 | modified | 1 | 0 | 1 | 
| [disconnected.md](#item-c70d0b) | minor update | ROPに関するメタデータの追加 | modified | 1 | 0 | 1 | 
| [install-run.md](#item-e32e11) | minor update | ROPに関するメタデータの追加 | modified | 1 | 0 | 1 | 
| [compose-custom-models.md](#item-bfda06) | minor update | 画像に関するメタデータの追加 | modified | 1 | 0 | 1 | 
| [rest-api.md](#item-1a8bdb) | minor update | 複数のカスタムメタデータの追加 | modified | 3 | 1 | 4 | 
| [project-share-custom-models.md](#item-acd5dd) | minor update | カスタムメタデータの追加 | modified | 1 | 0 | 1 | 
| [model-overview.md](#item-768c0d) | minor update | カスタムメタデータの追加 | modified | 1 | 0 | 1 | 
| [azure-function.md](#item-e0ba8d) | minor update | カスタムメタデータの更新 | modified | 5 | 1 | 6 | 
| [label-tool.md](#item-2eeebd) | minor update | カスタムメタデータの追加 | modified | 1 | 0 | 1 | 
| [get-key-endpoint.md](#item-12e825) | minor update | カスタムメタデータの追加 | modified | 1 | 0 | 1 | 
| [integrate-power-bi.md](#item-20f71f) | minor update | メタデータのフォーマット改善と新しいカスタム項目の追加 | modified | 4 | 1 | 5 | 
| [managed-identities.md](#item-ddd66a) | minor update | カスタムメタデータの追加 | modified | 1 | 0 | 1 | 
| [entity-categories.md](#item-ba2623) | minor update | カスタムメタデータのフォーマット改善と新項目の追加 | modified | 3 | 1 | 4 | 
| [bot-service.md](#item-f8e773) | minor update | カスタムメタデータのフォーマット改善と新項目の追加 | modified | 4 | 1 | 5 | 


# Modified Contents
## articles/ai-services/document-intelligence/authentication/create-sas-tokens.md{#item-dc2ea3}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.date: 11/19/2024
 ms.author: lajanuar
+ms.custom: sfi-image-nochange
 ---
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SFI画像に関するメタデータの追加"
}
```

### Explanation
この変更は、ドキュメント「create-sas-tokens.md」に1行のメタデータを追加する小規模な更新です。追加された行は「ms.custom: sfi-image-nochange」であり、これは特定のカスタムプロパティを文書に設定するために使用されます。この変更は、ドキュメントの管理やカスタマイズに関連する情報を強化することを目的としています。全体として、他の内容に影響を及ぼすことなく、ドキュメントに付加的な情報を提供することで、整合性と可管理性を向上させることが期待されます。

## articles/ai-services/document-intelligence/authentication/managed-identities-secured-access.md{#item-05ef7b}

<details>
<summary>Diff</summary>
````diff
@@ -9,6 +9,7 @@ ms.topic: how-to
 ms.date: 11/19/2024
 ms.author: vikurpad
 monikerRange: '<=doc-intel-4.0.0'
+ms.custom: sfi-image-nochange
 ---
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SFI画像に関するメタデータの追加"
}
```

### Explanation
この変更は、「managed-identities-secured-access.md」ドキュメントに1行のメタデータを追加する小規模な更新です。追加された内容は「ms.custom: sfi-image-nochange」で、これは特定のカスタムプロパティを設定して、ドキュメントの管理を容易にするために使用されます。この変更は、ドキュメントの整合性を保ちながら、特定の管理機能に役立つ情報を提供することを目指しています。全体として、他の内容に影響を与えることなく、ドキュメントのカスタマイズ性と可管理性を強化することが期待されます。

## articles/ai-services/document-intelligence/authentication/managed-identities.md{#item-be183c}

<details>
<summary>Diff</summary>
````diff
@@ -9,6 +9,7 @@ ms.topic: how-to
 ms.date: 11/19/2024
 ms.author: lajanuar
 monikerRange: '<=doc-intel-4.0.0'
+ms.custom: sfi-image-nochange
 ---
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SFI画像に関するメタデータの追加"
}
```

### Explanation
この変更は、「managed-identities.md」ドキュメントに、新たに1行のメタデータを追加する小規模な更新です。追加された内容は「ms.custom: sfi-image-nochange」で、これは特定のカスタムプロパティを設定し、ドキュメントの管理を向上させる目的があります。この変更により、他の内容に影響を与えずに、ドキュメントの特定の管理機能やカスタマイズ性が強化されることが期待されます。全体的に見て、ドキュメントの一貫性を維持しながら、より良い情報管理を図るための手助けとなります。

## articles/ai-services/document-intelligence/containers/disconnected.md{#item-c70d0b}

<details>
<summary>Diff</summary>
````diff
@@ -8,6 +8,7 @@ manager: nitinme
 ms.topic: reference
 ms.date: 11/19/2024
 ms.author: lajanuar
+ms.custom: sfi-ropc-nochange
 ---
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ROPに関するメタデータの追加"
}
```

### Explanation
この変更は、「disconnected.md」ドキュメントに1行のメタデータを追加する小規模な更新です。追加された内容は「ms.custom: sfi-ropc-nochange」で、これは特定のカスタムプロパティを設定し、ドキュメントの管理やカスタマイズ性を向上させる目的があります。この変更により、ドキュメントの整合性を保ちながら、特定の管理機能に役立つ情報を提供することが期待されています。全体的に、他の内容に影響を与えることなく、ドキュメントの管理がより効率的になることが目指されています。

## articles/ai-services/document-intelligence/containers/install-run.md{#item-e32e11}

<details>
<summary>Diff</summary>
````diff
@@ -8,6 +8,7 @@ ms.service: azure-ai-document-intelligence
 ms.topic: how-to
 ms.date: 04/03/2025
 ms.author: lajanuar
+ms.custom: sfi-ropc-nochange
 ---
 
 # Install and run containers
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ROPに関するメタデータの追加"
}
```

### Explanation
この変更は、「install-run.md」ドキュメントに1行のメタデータを追加する小規模な更新です。追加された内容は「ms.custom: sfi-ropc-nochange」で、これは特定のカスタムプロパティを導入し、ドキュメントの管理やカスタマイズの効率を向上させることを目的としています。この更新により、ドキュメントの整合性を保持しつつ、特定の管理機能に関する情報を提供することが目指されています。全体として、他の内容に影響を与えることなく、ドキュメントの運用がより効率的になることが期待されています。

## articles/ai-services/document-intelligence/how-to-guides/compose-custom-models.md{#item-bfda06}

<details>
<summary>Diff</summary>
````diff
@@ -8,6 +8,7 @@ ms.service: azure-ai-document-intelligence
 ms.topic: how-to
 ms.date: 11/19/2024
 ms.author: lajanuar
+ms.custom: sfi-image-nochange
 ---
 
 # Compose custom models
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像に関するメタデータの追加"
}
```

### Explanation
この変更は、「compose-custom-models.md」ドキュメントに1行のメタデータを追加する小規模な更新です。追加された内容は「ms.custom: sfi-image-nochange」で、これは特定のカスタムプロパティを設定し、ドキュメントの管理やカスタマイズの効率を向上させることを目的としています。この更新により、ドキュメントの一貫性を保ちながら、ユーザーに対して特定の管理機能に関連する情報を提供することが期待されています。全体として、他の内容に影響を与えることなく、ドキュメントの運用がより効果的になることが目指されています。

## articles/ai-services/document-intelligence/how-to-guides/includes/v3-0/rest-api.md{#item-1a8bdb}

<details>
<summary>Diff</summary>
````diff
@@ -4,11 +4,13 @@ description: Use the Document Intelligence REST API v3.0 to create a forms proce
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom: linux-related-content
 ms.topic: include
 ms.date: 11/19/2024
 ms.author: lajanuar
 monikerRange: 'doc-intel-3.1.0 || doc-intel-3.0.0'
+ms.custom:
+  - linux-related-content
+  - sfi-image-nochange
 ---
 
 <!-- markdownlint-disable MD033 -->
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "複数のカスタムメタデータの追加"
}
```

### Explanation
この変更は、「rest-api.md」ドキュメントに対してメタデータの更新を行い、3行の情報を追加し、1行を削除するという小規模な修正です。新たに追加された「ms.custom」プロパティでは、複数のカスタム値を指定しており、「linux-related-content」と「sfi-image-nochange」が含まれています。この修正により、ドキュメントは特定の対象読者に向けた情報をより明確に示すことが可能になり、管理やカスタマイズの効率も向上することが期待されます。このように、ドキュメントが持つメタデータを強化し、他の内容に影響を与えることなく、運用の効率を改善することを目指しています。

## articles/ai-services/document-intelligence/how-to-guides/project-share-custom-models.md{#item-acd5dd}

<details>
<summary>Diff</summary>
````diff
@@ -9,6 +9,7 @@ ms.topic: how-to
 ms.date: 11/19/2024
 ms.author: jppark
 monikerRange: '>=doc-intel-3.0.0'
+ms.custom: sfi-image-nochange
 ---
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムメタデータの追加"
}
```

### Explanation
この変更は、「project-share-custom-models.md」ドキュメントに1行のメタデータを追加する小規模な更新です。追加された内容は「ms.custom: sfi-image-nochange」で、このプロパティは特定のカスタム設定を示しています。この追加により、ドキュメントはより具体的な管理機能を持ち、ユーザーに向けた情報提供が強化されます。このような修正は、ドキュメント全体の一貫性と運用効率を向上させる目的があります。全体として、ユーザーが必要とする情報にアクセスしやすくするための施策と考えられます。

## articles/ai-services/document-intelligence/model-overview.md{#item-768c0d}

<details>
<summary>Diff</summary>
````diff
@@ -8,6 +8,7 @@ ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
 ms.date: 03/14/2025
 ms.author: lajanuar
+ms.custom: sfi-image-nochange
 ---
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムメタデータの追加"
}
```

### Explanation
この変更は、「model-overview.md」ドキュメントに対して1行のメタデータを追加する小規模な修正です。追加された内容は「ms.custom: sfi-image-nochange」で、このプロパティは特定のカスタム設定を示しています。この更新により、ドキュメントがより適切に管理され、特定のコンテンツに関連する情報が強調されます。これにより、ユーザーがドキュメントを利用する際の明確さが増し、内容の理解が容易になることが期待されています。全体として、運用の効率と一貫性を高めるための施策と考えられます。

## articles/ai-services/document-intelligence/tutorial/azure-function.md{#item-e0ba8d}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,11 @@ ms.service: azure-ai-document-intelligence
 ms.topic: tutorial
 ms.date: 03/19/2025
 ms.author: lajanuar
-ms.custom: VS Code-azure-extension-update-completed, devx-track-python
+ms.custom:
+  - VS Code-azure-extension-update-completed
+  - devx-track-python
+  - sfi-image-nochange
+  - sfi-ropc-nochange
 ---
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムメタデータの更新"
}
```

### Explanation
この変更は、「azure-function.md」ドキュメントに対して、複数のカスタムメタデータを追加する小規模な更新です。具体的には、元のメタデータに新しいエントリ「sfi-image-nochange」と「sfi-ropc-nochange」を追加し、リスト形式に改良しています。この変更により、ドキュメントの管理がより柔軟に行えるようになります。追加された情報は、特定の機能やトラッキングの目的で使われ、ユーザーがリソースを使用する際の体験を向上させることにつながります。全体として、ドキュメントの内容が整理され、明確さが増すことを目指した改善と考えられます。

## articles/ai-services/document-intelligence/v21/label-tool.md{#item-2eeebd}

<details>
<summary>Diff</summary>
````diff
@@ -9,6 +9,7 @@ ms.topic: how-to
 ms.date: 11/19/2024
 ms.author: lajanuar
 monikerRange: 'doc-intel-2.1.0'
+ms.custom: sfi-image-nochange
 ---
 
 <!-- markdownlint-disable MD001 -->
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムメタデータの追加"
}
```

### Explanation
この変更は、「label-tool.md」ドキュメントに対して1行のカスタムメタデータを追加する小規模な更新です。具体的には、追加された内容は「ms.custom: sfi-image-nochange」であり、このメタデータは特定のカスタム設定を表示するために使用されます。この改良により、ドキュメントの文脈がより明確になり、管理や追跡が容易になることが期待されます。全体として、この変更はドキュメントの利便性を向上させることを目的としたものです。

## articles/ai-services/language-service/includes/get-key-endpoint.md{#item-12e825}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ ms.service: azure-ai-language
 ms.topic: include
 ms.date: 06/30/2025
 ms.author: lajanuar
+ms.custom: sfi-image-nochange
 ---
 
 ### Get your key and endpoint
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムメタデータの追加"
}
```

### Explanation
この変更は、「get-key-endpoint.md」ドキュメントに対する1行のカスタムメタデータを追加する小規模な更新です。具体的には、追加された内容は「ms.custom: sfi-image-nochange」であり、これはドキュメントの管理や特定の機能に関連する情報を示すために使用されます。この更新により、関連情報の整理が行われ、ドキュメントの可読性と利便性の向上が期待されます。全体として、この変更はドキュメントの品質を向上させることを目的としたものです。

## articles/ai-services/language-service/key-phrase-extraction/tutorials/integrate-power-bi.md{#item-20f71f}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,10 @@ ms.service: azure-ai-language
 ms.topic: tutorial
 ms.date: 06/04/2025
 ms.author: lajanuar
-ms.custom: language-service-key-phrase, cogserv-non-critical-language
+ms.custom:
+  - language-service-key-phrase
+  - cogserv-non-critical-language
+  - sfi-image-nochange
 ---
 
 # Tutorial: Extract key phrases from text stored in Power BI
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータのフォーマット改善と新しいカスタム項目の追加"
}
```

### Explanation
この変更は、「integrate-power-bi.md」ドキュメントに対して行われ、メタデータの形式が改善され、新しいカスタム項目が追加されています。具体的には、元の1行の「ms.custom」フィールドが、リスト形式になり、3つの項目「language-service-key-phrase」、「cogserv-non-critical-language」、及び新たに追加された「sfi-image-nochange」が含まれています。この変更により、メタデータが整理され、異なる情報をより明確に表現できるようになっています。これにより、ドキュメントの管理や理解が向上し、ユーザーに対して提供される情報の質が改善されることが期待されます。

## articles/ai-services/language-service/native-document-support/managed-identities.md{#item-ddd66a}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 ms.author: lajanuar
 author: laujan
 ms.date: 03/05/2025
+ms.custom: sfi-image-nochange
 ---
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムメタデータの追加"
}
```

### Explanation
この変更は、「managed-identities.md」ドキュメントに対する小規模な更新で、1行のカスタムメタデータが追加されました。具体的には、追加された内容は「ms.custom: sfi-image-nochange」であり、これはドキュメントに特定の管理情報を提供するために使用されます。このメタデータの追加により、文書の整理が進み、管理や参照を容易にすることが期待されます。この更新は、ドキュメントの品質を高めるための取り組みとして位置づけられます。

## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories.md{#item-ba2623}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,9 @@ ms.service: azure-ai-language
 ms.topic: conceptual
 ms.date: 06/04/2025
 ms.author: lajanuar
-ms.custom: language-service-pii
+ms.custom:
+  - language-service-pii
+  - sfi-ropc-nochange
 ---
 
 # Supported PII entities
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムメタデータのフォーマット改善と新項目の追加"
}
```

### Explanation
この変更は、「entity-categories.md」ドキュメントに対して行われたもので、カスタムメタデータの形式が改善され、新しい項目が追加されています。具体的には、元の1行の「ms.custom」フィールドがリスト形式に変更され、以前の項目「language-service-pii」に加え、追加された項目「sfi-ropc-nochange」が含まれています。この改善により、メタデータがより明確に表現され、異なる情報を整理しやすくなっています。この更新は、ドキュメントの理解を深め、ユーザーに対する情報提供の質を向上させることが期待されます。

## articles/ai-services/language-service/question-answering/tutorials/bot-service.md{#item-f8e773}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,10 @@ ms.topic: tutorial
 author: laujan
 ms.author: lajanuar
 ms.date: 06/04/2025
-ms.custom: language-service-question-answering, cogserv-non-critical-language
+ms.custom:
+  - language-service-question-answering
+  - cogserv-non-critical-language
+  - sfi-image-nochange
 ---
 
 # Tutorial: Create an FAQ bot
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムメタデータのフォーマット改善と新項目の追加"
}
```

### Explanation
この変更は、「bot-service.md」ドキュメントに対する小規模な更新で、カスタムメタデータの形式が改善され、新しい項目が追加されています。具体的には、元のカスタムメタデータがリスト形式に変更され、「language-service-question-answering」と「cogserv-non-critical-language」の項目に加え、新たに「sfi-image-nochange」が追加されています。この構造の改善により、メタデータがより明確に管理され、異なる情報を整理することが容易になります。この更新は、チュートリアルの内容をより理解しやすくすることを目的としており、ユーザーにとって有用な情報源となることでしょう。


