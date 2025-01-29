---
date: '2025-01-29'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2067774...MicrosoftDocs:b5fac8b
summary: このコードの差分には、新機能はありませんが、複数のファイルでのAPIバージョンに関する記述の変更や削除が行われました。また、ドキュメントの更新日が「2025年1月28日」に統一され、内容が最新であることが確認されています。ElasticsearchおよびPineconeに関する説明が明確化され、誤解を避けるために修正されました。さらに、一部のコード例の構文が改善され、読みやすくなっています。全体として、これらの変更は情報の精度を高め、ドキュメントのユーザビリティを改善することを目指しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2067774...MicrosoftDocs:b5fac8b){target="_blank"}

# ハイライト

このコードの差分には、以下のような新機能や重大な変更点が含まれています。

## 新機能

- なし

## 重大な変更

- APIバージョンに関する記述が複数のファイルで変更または削除されました。

## その他の更新

- 複数のドキュメントファイルで更新日が「2025年1月28日」に変更され、内容が最新であることが保証されています。
- ElasticsearchおよびPineconeに関する説明が明確化され、誤解を避けるよう修正されました。
- 一部のファイルでコード例の構文が改善され、読みやすくなりました。

# 洞察

今回の差分は、ドキュメントの更新日とAPIバージョン情報の管理方法の変更に焦点を当てています。更新日はすべて「2025年1月28日」に統一されており、これによりドキュメント全体が最新かつ一貫性のある情報を提供していることが示されています。これは、情報の古さを原因とする信頼性低下を防ぐための重要なステップです。

APIバージョンに関しては、以前はリスト形式で明示されていたものが削除されたり、新たに表現が変更されたりしています。例えば、`code-interpreter.md` や `file-search.md` においては、APIバージョンの記述が簡略化され、APIの利用可能開始時期を明確に示すように調整されました。これにより、開発者やユーザーはドキュメントを読んで使用すべきAPIバージョンを識別しやすくなり、誤解や混乱を防ぐことができます。

ElasticsearchやPineconeのドキュメントでは、特にAPIサポートバージョンが明示され、より正確に情報を伝えるように微調整されています。これによって、利用者はどのバージョンから新しい機能を利用できるのかを正確に把握できるようになります。

全体として、これらの変更は情報の精度を高め、ドキュメントのユーザビリティを改善することを目的としており、さらなる利用者の理解促進と効率的な利用をサポートしています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [assistant.md](#item-b12c67) | minor update | 日付の更新とAPIバージョンの削除 | modified | 1 | 6 | 7 | 
| [assistants-logic-apps.md](#item-57ae37) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [code-interpreter.md](#item-95efbd) | minor update | 日付の更新とAPIバージョンの表現変更 | modified | 3 | 4 | 7 | 
| [file-search.md](#item-f9d6d7) | minor update | 日付の更新とAPIバージョン表現の変更 | modified | 2 | 2 | 4 | 
| [on-your-data-best-practices.md](#item-801589) | minor update | 更新日の変更 | modified | 1 | 1 | 2 | 
| [azure-machine-learning.md](#item-940a2b) | minor update | 更新日の変更 | modified | 1 | 1 | 2 | 
| [elasticsearch.md](#item-bb82ea) | minor update | 更新日の変更および説明の修正 | modified | 2 | 2 | 4 | 
| [pinecone.md](#item-4d8746) | minor update | 更新日の変更および説明の修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/openai/how-to/assistant.md{#item-b12c67}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: references_regions
 ms.topic: how-to
-ms.date: 05/20/2024
+ms.date: 01/28/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -26,11 +26,6 @@ Azure OpenAI Assistants (Preview) allows you to create AI assistants tailored to
 
 Code interpreter is available in all regions supported by Azure OpenAI Assistants. The [models page](../concepts/models.md#assistants-preview) contains the most up-to-date information on regions/models where Assistants are currently supported.
 
-### API Versions
-
-- `2024-02-15-preview`
-- `2024-05-01-preview`
-
 ### Supported file types
 
 |File format|MIME Type|Code Interpreter |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新とAPIバージョンの削除"
}
```

### Explanation
この変更は、ファイル `assistant.md` において、日付の更新とAPIバージョンに関するセクションの削除を行ったものです。具体的には、元の更新日である「2024年5月20日」が「2025年1月28日」に変更されています。また、以前存在していたAPIバージョンの情報が削除されました。この変更により、ドキュメントがより最新の情報に基づいて更新され、より明確で簡潔な内容になります。

## articles/ai-services/openai/how-to/assistants-logic-apps.md{#item-57ae37}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 05/21/2024
+ms.date: 01/28/2025
 author: aahill
 ms.author: aahi
 recommendations: false
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
この変更は、ファイル `assistants-logic-apps.md` において、更新日を変更したものです。具体的には、元の更新日である「2024年5月21日」が「2025年1月28日」に修正されました。この修正により、ドキュメントが最新の情報を反映したものになり、読者に対する情報の信頼性が向上します。

## articles/ai-services/openai/how-to/code-interpreter.md{#item-95efbd}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 10/15/2024
+ms.date: 01/28/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -32,8 +32,7 @@ We recommend using assistants with the latest models to take advantage of the ne
 
 ### API Versions
 
-- `2024-02-15-preview`
-- `2024-05-01-preview`
+- Starting in `2024-02-15-preview`
 
 ### Supported file types
 
@@ -94,7 +93,7 @@ assistant = client.beta.assistants.create(
 # [REST](#tab/rest)
 
 > [!NOTE]
-> With Azure OpenAI the `model` parameter requires model deployment name. If your model deployment name is different than the underlying model name then you would adjust your code to ` "model": "{your-custom-model-deployment-name}"`.
+> With Azure OpenAI the `model` parameter requires model deployment name. If your model deployment name is different than the underlying model name, then you would adjust your code to ` "model": "{your-custom-model-deployment-name}"`.
 
 ```console
 curl https://YOUR_RESOURCE_NAME.openai.azure.com/openai/assistants?api-version=2024-05-01-preview \
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新とAPIバージョンの表現変更"
}
```

### Explanation
この変更は、ファイル `code-interpreter.md` において、更新日とAPIバージョンに関する表現を修正したものです。具体的には、元の更新日である「2024年10月15日」が「2025年1月28日」に変更されています。また、APIバージョンの記述方法が「`2024-02-15-preview`」と「`2024-05-01-preview`」のリストから、「`2024-02-15-preview`」から始まるという形に変更されました。このような修正により、情報が明確化され、最新の状況に適応しています。さらに、コード例中の文章において、カンマの位置が調整され、文が読みやすくなりました。

## articles/ai-services/openai/how-to/file-search.md{#item-f9d6d7}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 06/03/2024
+ms.date: 01/28/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -30,7 +30,7 @@ File search is available in [regions](../concepts/models.md#assistants-preview)
 
 ### API Version
 
-* 2024-05-01-preview
+* Starting in 2024-05-01-preview
 
 ### Supported file types
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新とAPIバージョン表現の変更"
}
```

### Explanation
この変更は、ファイル `file-search.md` において、更新日とAPIバージョンの表現を修正したものです。具体的には、更新日が「2024年6月3日」から「2025年1月28日」に変更され、最新の情報が反映されました。また、APIバージョンの記述が「2024-05-01-preview」という形式から、「Starting in 2024-05-01-preview」という形に変更され、より明確になりました。これにより、読者がAPIの利用可能開始時期について理解しやすくなります。全体として、文書が最新の情報を明確に伝えるように改善されています。

## articles/ai-services/openai/how-to/on-your-data-best-practices.md{#item-801589}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI Service
 description: Learn about the best practices for using Azure OpenAI On Your Data, along with how to fix common problems.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 04/08/2024
+ms.date: 01/28/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: aahill
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新日の変更"
}
```

### Explanation
この変更は、ファイル `on-your-data-best-practices.md` において、更新日を修正したものです。具体的には、元の更新日である「2024年4月8日」が「2025年1月28日」に変更されました。この修正により、文書の情報が最新の状況を反映したものとなります。全体として、ドキュメントの信頼性を高めるために重要な更新です。

## articles/ai-services/openai/references/azure-machine-learning.md{#item-940a2b}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI on your Azure Machine Learning index
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 03/14/2024
+ms.date: 01/28/2025
 author: aahill
 ms.author: aahi
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新日の変更"
}
```

### Explanation
この変更は、ファイル `azure-machine-learning.md` において、文書の更新日を修正したものです。具体的には、旧更新日「2024年3月14日」が新たに「2025年1月28日」に変更されました。このような更新は、情報が最新の状態であることを確保し、ユーザーに正確なデータを提供するために重要です。全体として、この修正は文書の信頼性を高めることに寄与しています。

## articles/ai-services/openai/references/elasticsearch.md{#item-bb82ea}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI on your Elasticsearch data Python & R
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 03/14/2024
+ms.date: 01/28/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -14,7 +14,7 @@ ms.custom: devx-track-python
 
 # Data source - Elasticsearch (preview)
 
-The configurable options for Elasticsearch when using Azure OpenAI On Your Data. This data source is supported in API version `2024-02-15-preview`.
+The configurable options for Elasticsearch when using Azure OpenAI On Your Data. This data source is supported starting in API version `2024-02-15-preview`.
 
 |Name | Type | Required | Description |
 |--- | --- | --- | --- |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新日の変更および説明の修正"
}
```

### Explanation
この変更は、ファイル `elasticsearch.md` における2つの主な修正を含んでいます。まず、文書の更新日が「2024年3月14日」から「2025年1月28日」へと変更されました。次に、Elasticsearchに関する説明文がわずかに修正され、「このデータソースはAPIバージョン `2024-02-15-preview` からサポートされています」という文言に修正されています。これにより、ユーザーに対して最新の情報を提供し、誤解を避けるために重要な内容が明確にされています。全体として、この変更は文書の正確性と信頼性を向上させます。

## articles/ai-services/openai/references/pinecone.md{#item-4d8746}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI on your Pinecone data Python & REST A
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 03/14/2024
+ms.date: 01/28/2025
 author: aahill
 ms.author: aahi
 recommendations: false
@@ -14,7 +14,7 @@ ms.custom: devx-track-python
 
 # Data source - Pinecone (preview)
 
-The configurable options of Pinecone when using Azure OpenAI On Your Data. This data source is supported in API version `2024-02-15-preview`.
+The configurable options of Pinecone when using Azure OpenAI On Your Data. This data source is supported starting in API version `2024-02-15-preview`.
 
 |Name | Type | Required | Description |
 |--- | --- | --- | --- |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新日の変更および説明の修正"
}
```

### Explanation
この変更は、ファイル `pinecone.md` において、主に2つの修正が行われています。まず、文書の更新日が「2024年3月14日」から「2025年1月28日」へと変更されました。次に、Pineconeに関する説明文が修正され、「このデータソースはAPIバージョン `2024-02-15-preview` からサポートされています」という表現に変更されています。このような修正は文書の正確性を向上させ、ユーザーへの情報提供の信頼性を確保するために重要です。総じて、この更新は文書の整合性を保つために寄与しています。


