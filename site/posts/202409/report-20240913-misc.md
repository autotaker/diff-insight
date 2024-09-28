---
date: '2024-09-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9392315...MicrosoftDocs:022de22
summary: このコード変更は、主にTOCファイルとチュートリアルファイルに対して行われ、最新のREST API情報を提供するための更新が含まれています。具体的には、APIおよびクライアントライブラリのエントリが最新のプレビューリリースに更新されました。重大な変更はありませんが、メタデータの追加やリンク修正によってユーザー体験が向上しています。特に、ドキュメントの検索性やアクセス性が強化されており、これによりユーザーが必要な情報にスムーズにアクセスできるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9392315...MicrosoftDocs:022de22){target="_blank"}

# ハイライト
このコード変更は、2つの主なファイルで更新が行われています。具体的には、TOCファイル (`toc.yml`) とチュートリアルファイル (`copilot-sdk-build-rag.md`) が影響を受けています。主な新機能や重要な変更点として以下が含まれます。

## 新機能
- REST APIおよびクライアントライブラリのエントリが最新のプレビューリリース (`2024-07-31-preview`) に更新されました。これにより、最新のAPI情報を提供します。

## 重大な変更
- 特筆すべき重大な変更はありませんが、メタデータの追加やリンクの修正により、ユーザー体験が向上しています。

## その他の更新
- `articles/ai-studio/tutorials/copilot-sdk-build-rag.md`ファイルで、ドキュメントのメタデータが追加され、リンク修正およびテキスト説明の改良が行われました。


# 洞察
このコード差分を詳しく見ると、更新の背景として、主にユーザー視点の向上が意図されていることがわかります。以下に、各変更が行われた理由とその影響について詳しく説明します。

`articles/ai-services/document-intelligence/toc.yml`の更新は、APIとクライアントライブラリが常に最新の情報をユーザーに提供するための取り組みです。プレビューバージョンは新機能やバグ修正が頻繁に行われるため、定期的な更新が必要です。今回の更新により、エントリが最新の「2024-07-31-preview」に変更され、3行の新規追加と5行の削除が行われています。これにより、古い情報が削除され、最新のAPI仕様書を参照できるようになりました。

`articles/ai-studio/tutorials/copilot-sdk-build-rag.md`の更新では、メタデータの追加とリンク修正が行われています。メタデータの追加 (`ms.custom: [copilot-learning-hub]`) は、ドキュメントの整理と検索性の向上を目的としています。このメタデータにより、ドキュメントが特定のカテゴリに紐付けられ、特定のユーザーグループや用途に対して最適化されます。

さらに、リンクの修正はユーザーが指定されたリソースに正確にアクセスできるようにするためのもので、複数のURLが最新のリポジトリパスに更新されています。これにより、リンク切れや古いリソースへのアクセスが防止されます。また、フォルダ名の具体化はユーザーガイドとしての精度を高め、手順をより明確に理解できるようにするためのものです。

このように、これらの変更はすべてユーザー体験の向上を意図しており、特に最新情報へのアクセス性とドキュメントの使いやすさを重視していることがわかります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [toc.yml](#item-81aa7b) | minor update | TOCファイルの更新 (2024年のプレビューバージョンへの変更) | modified | 3 | 5 | 8 | 
| [copilot-sdk-build-rag.md](#item-b77dba) | minor update | チュートリアルファイルの更新 (リンク修正とメタデータ追加) | modified | 4 | 3 | 7 | 


# Modified Contents
## articles/ai-services/document-intelligence/toc.yml{#item-81aa7b}

<details>
<summary>Diff</summary>
````diff
@@ -295,10 +295,8 @@ items:
   items:
   - name: REST APIs
     items:
-    - name: 2024-02-29-preview (v4.0)
-      href: /rest/api/aiservices/document-models/build-model?view=rest-aiservices-2024-02-29-preview&preserve-view=true&branch=docintelligence&tabs=HTTP
-    - name: 2023-10-31-preview (v4.0)
-      href: /rest/api/aiservices/operation-groups?view=rest-aiservices-2023-10-31-preview&preserve-view=true&tabs=HTTP
+    - name: 2024-07-31-preview (v4.0)
+      href: /rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true
     - name: 2023-07-31 (v3.1)
       href: /rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP
     - name: 2022-08-31 (v3.0)
@@ -307,7 +305,7 @@ items:
       href: v3-error-guide.md
     - name: v2.1
       href: /rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true
-  - name: Client libraries (2023-10-31-preview)
+  - name: Client libraries (2024-07-31-preview)
     items:
     - name: C# / .NET
       href: /dotnet/api/overview/azure/ai.documentintelligence-readme?view=azure-dotnet-preview&preserve-view=true
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCファイルの更新 (2024年のプレビューバージョンへの変更)"
}
```

### Explanation
この変更は、`articles/ai-services/document-intelligence/toc.yml`ファイルに対するマイナー更新です。具体的には、REST APIのバージョンとクライアントライブラリのエントリが新しいプレビューリリースに合わせて更新されました。特に、「2024-02-29-preview」と「2023-10-31-preview」というエントリが、「2024-07-31-preview」に変更され、また、クライアントライブラリのセクションでも同様に最新のプレビュー日付に変更されています。これにより、最新のAPI情報が反映された形となります。全体で3行が新規追加され、5行が削除されており、合計で8行の変更が行われています。

## articles/ai-studio/tutorials/copilot-sdk-build-rag.md{#item-b77dba}

<details>
<summary>Diff</summary>
````diff
@@ -9,6 +9,7 @@ ms.date: 08/29/2024
 ms.reviewer: lebaro
 ms.author: sgilley
 author: sdgilley
+ms.custom: [copilot-learning-hub]
 #customer intent: As a developer, I want to learn how to use the prompt flow SDK so that I can build a RAG-based chat app.
 ---
 
@@ -29,7 +30,7 @@ This tutorial is part two of a three-part tutorial.
 
 * Complete [Tutorial:  Part 1 - Create resources for building a custom chat application with the prompt flow SDK](copilot-sdk-create-resources.md).
 
-* You need a local copy of product data. The [Azure-Samples/rag-data-openai-python-promptflow repository on GitHub](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/) contains sample retail product information that's relevant for this tutorial scenario. [Download the example Contoso Trek retail product data in a ZIP file](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/tree/main/tutorial/data) to your local machine.
+* You need a local copy of product data. The [Azure-Samples/rag-data-openai-python-promptflow repository on GitHub](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/) contains sample retail product information that's relevant for this tutorial scenario. [Download the example Contoso Trek retail product data in a ZIP file](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/blob/main/tutorial/data/product-info.zip) to your local machine.
 
 ## Application code structure
 
@@ -114,7 +115,7 @@ These steps deploy a model to a real-time endpoint from the AI Studio [model cat
 When you deploy the `gpt-3.5-turbo` model, find the following values in the **View Code** section, and add them to your **.env** file:
 
 ```env
-AZURE_OPENAI_ENDPOINT=<chat_model_endpoint_value>
+AZURE_OPENAI_ENDPOINT=<endpoint_value>
 AZURE_OPENAI_CHAT_DEPLOYMENT=<chat_model_deployment_name>
 AZURE_OPENAI_API_VERSION=<api_version>
 ```
@@ -155,7 +156,7 @@ The goal with this RAG-based application is to ground the model responses in you
 
 If you don't have an Azure AI Search index already created, we walk through how to create one. If you already have an index to use, you can skip to the [set the search environment variable](#set-search-index) section. The search index is created on the Azure AI Search service that was either created or referenced in the previous step.
 
-1. Use your own data or [download the example Contoso Trek retail product data in a ZIP file](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/tree/main/tutorial/data) to your local machine. Unzip the file into your **rag-tutorial** folder. This data is a collection of markdown files that represent product information. The data is structured in a way that is easy to ingest into a search index. You build a search index from this data.
+1. Use your own data or [download the example Contoso Trek retail product data in a ZIP file](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/blob/main/tutorial/data/product-info.zip) to your local machine. Unzip the file into your **rag-tutorial/data** folder. This data is a collection of markdown files that represent product information. The data is structured in a way that is easy to ingest into a search index. You build a search index from this data.
 
 1. The prompt flow RAG package allows you to ingest the markdown files, locally create a search index, and register it in the cloud project. Install the prompt flow RAG package:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルファイルの更新 (リンク修正とメタデータ追加)"
}
```

### Explanation
この変更は、`articles/ai-studio/tutorials/copilot-sdk-build-rag.md`ファイルに対するマイナー更新です。主に、以下の内容が含まれています。

1. **メタデータの追加**: `ms.custom`フィールドに新たに`[copilot-learning-hub]`の属性が追加されました。これにより、ドキュメントのカスタム情報をカテゴリに紐付けることができます。
  
2. **リンクの修正**: 複数の場所で、製品データをダウンロードするためのURLが修正されました。具体的には、「Azure-Samples/rag-data-openai-python-promptflow」リポジトリへのリンクが、以前のパスから新しいパスに更新されています。

3. **説明の修正**: 一部のテキストにおいて、データを解凍する際のフォルダ名がより具体的に定義され、明確さが向上しました。

全体として、4行が新規追加され、3行が削除され、その結果として7行の変更が行われました。これらの更新により、ユーザーが必要な情報にアクセスしやすくなっています。


