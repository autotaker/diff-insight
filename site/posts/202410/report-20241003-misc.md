---
date: '2024-10-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b0599a2...MicrosoftDocs:94dabc3
summary: Azure AI Document Intelligenceに関する最新の文書更新では、情報提供の質を向上させることが主な目的とされています。具体的には、`install-run.md`の更新で最新の日付情報やコンテナサポートの詳細が追加され、ユーザーが利用する際の不明点を解消する助けとなっています。また、`secure-data-playground.md`では役割名の修正が行われ、誤解を招かないよう配慮されています。全体として、これらのアップデートは、ドキュメントの読みやすさや情報の正確さを向上させることに重点を置いており、ドキュメントの利便性が高まることが期待されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b0599a2...MicrosoftDocs:94dabc3){target="_blank"}

# Highlights

## New features
- Azure AI Document Intelligence に関するドキュメントである`install-run.md`が更新され、最新の日付情報（`ms.date`が2024年10月1日に更新）が追加されました。
- コンテナと関連するREST APIのサポート情報が整理され、各モデルについてのサポート内容がより詳細に記載されています。

## Breaking changes
- 特に重大な機能の破壊的変更は報告されていません。この更新では主に情報の明確化を狙っており、既存ユーザーに大きな影響を与える変更は含まれていないようです。

## Other updates
- `secure-data-playground.md`では、Azure Storage Accountのロール名「PrivilegedContributorRoleId」が「Privileged Contributor」に修正され、役割名の誤解が無くなるようにしています。
- 関連コンテンツのセクションで改行を追加し、ユーザーが関連情報に容易にアクセスできるように改善されています。

# Insights

Azure AI Document Intelligenceのコンテナに関する最新文書更新では、ユーザーに対する情報提供の質を向上させることが主目的とされています。具体的な更新内容としては、情報がより迅速に取得できるように日付情報やコンテナサポートの詳細が整理されています。これにより、自身の環境に応じたコンテナのバージョンや関連機能を使用する際に、ユーザーが抱える可能性のある不明点を解消する意図が感じられます。

一方で、セキュアなデータプレイグラウンドに関する文書の更新は、役割名を正確なものにすることでユーザーが権限設定に際し誤解をしないよう配慮されています。この種の変更は、小さな修正に見えるかもしれませんが、ユーザーがセキュリティやアクセス制御を管理する上で非常に重要です。

最終的にこれらのアップデートは、ドキュメントの読みやすさや情報の正確さを向上させることを重視しており、ドキュメントの利便性を高める方向での改善が行われています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [install-run.md](#item-e32e11) | minor update | Document Intelligence コンテナのインストールと実行に関する更新 | modified | 12 | 17 | 29 | 
| [secure-data-playground.md](#item-b7fa5e) | minor update | セキュアなデータプレイグラウンドに関する更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/document-intelligence/containers/install-run.md{#item-e32e11}

<details>
<summary>Diff</summary>
````diff
@@ -5,10 +5,8 @@ description: Use the Docker containers for Document Intelligence on-premises to
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: how-to
-ms.date: 07/09/2024
+ms.date: 10/01/2024
 ms.author: lajanuar
 ---
 
@@ -18,30 +16,27 @@ ms.author: lajanuar
 <!-- markdownlint-disable MD024 -->
 <!-- markdownlint-disable MD051 -->
 
-:::moniker range="doc-intel-2.1.0 || doc-intel-4.0.0"
-Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models and `2023-07-31 (GA)` for Read, Layout, ID Document, Receipt, and Invoice models:
-
-* [REST API `2022-08-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
-* [REST API `2023-07-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.1%20(2023-07-31)&tabs=HTTP&preserve-view=true)
-* [Client libraries targeting `REST API 2022-08-31 (GA)`](../sdk-overview-v3-0.md)
-* [Client libraries targeting `REST API 2023-07-31 (GA)`](../sdk-overview-v3-1.md)
-
-✔️ See [**Install and run Document Intelligence containers**](?view=doc-intel-3.1.0&preserve-view=true) for supported container documentation.
-
-:::moniker-end
-
-:::moniker range="doc-intel-3.0.0 || doc-intel-3.1.0"
+:::moniker range=">=doc-intel-2.1.0"
 
 **This content applies to:** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** ![checkmark](../media/yes-icon.png) **v3.1 (GA)**
 
 Azure AI Document Intelligence is an Azure AI service that lets you build automated data processing software using machine-learning technology. Document Intelligence enables you to identify and extract text, key/value pairs, selection marks, table data, and more from your documents. The results are delivered as structured data that ../includes the relationships in the original file.
 
-In this article you learn how to download, install, and run Document Intelligence containers. Containers enable you to run the Document Intelligence service in your own environment. Containers are great for specific security and data governance requirements.
+In this article you can learn how to download, install, and run Document Intelligence containers. Containers enable you to run the Document Intelligence service in your own environment. Containers are great for specific security and data governance requirements.
 
 * **Read**, **Layout**,  **ID Document**,  **Receipt**, and **Invoice**  models are supported by Document Intelligence v3.1 containers.
 
 * **Read**, **Layout**, **General Document**, **Business Card**, and **Custom** models are supported by Document Intelligence v3.0 containers.
 
+## Version support
+
+Support for containers is currently available with Document Intelligence version `v3.0: 2022-08-31 (GA)` for all models and `v3.1 2023-07-31 (GA)` for Read, Layout, ID Document, Receipt, and Invoice models:
+
+* [REST API `v3.0: 2022-08-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
+* [REST API `v3.1: 2023-07-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.1%20(2023-07-31)&tabs=HTTP&preserve-view=true)
+* [Client libraries targeting `REST API v3.0: 2022-08-31 (GA)`](../sdk-overview-v3-0.md)
+* [Client libraries targeting `REST API v3.1: 2023-07-31 (GA)`](../sdk-overview-v3-1.md)
+
 ## Prerequisites
 
 To get started, you need an active [**Azure account**](https://azure.microsoft.com/free/cognitive-services/). If you don't have one, you can [**create a free account**](https://azure.microsoft.com/free/).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence コンテナのインストールと実行に関する更新"
}
```

### Explanation
この更新は、Azure AI Document Intelligenceのドキュメントにおける`install-run.md`ファイルに関するマイナーな変更を示しています。主な変更点は、新しい日付情報の追加とコンテナバージョンサポートに関する情報の整理です。具体的には、`ms.date`が2024年10月1日に更新され、ドキュメント内のコンテナバージョンの範囲指定が修正されています。

さらに、コンテナとそれに関連するREST APIのサポート情報が明確に整理され、各モデルのサポート内容が示されています。これにより、利用者は関連する情報に迅速にアクセスでき、ドキュメントインテリジェンスサービスを自分の環境で効率的に利用するための手順がより明確になります。

全体として、これらの変更はユーザーに対する情報の明確さと有用性を向上させることを目的としています。

## articles/ai-studio/how-to/secure-data-playground.md{#item-b7fa5e}

<details>
<summary>Diff</summary>
````diff
@@ -203,7 +203,7 @@ To enable your developers to use these resources to build applications, add the
 | Azure AI services/OpenAI | Contributor | Allows for calls to the control plane. |
 | Azure Storage Account | Contributor | List Account SAS to upload files from Azure OpenAI Studio. |
 | Azure Storage Account | Storage Blob Data Contributor | Needed for developers to read and write to blob storage. |
-| Azure Storage Account | Storage File Data PrivilegedContributorRoleId | Needed to Access File Share in Storage for Promptflow data. |
+| Azure Storage Account | Storage File Data Privileged Contributor | Needed to Access File Share in Storage for Promptflow data. |
 | The resource group or Azure subscription where the developer need to deploy the web app to | Contributor | Deploy web app to the developer's Azure subscription. |
 
 ## Use your data in AI Studio  
@@ -221,4 +221,4 @@ When using the Chat playground in Azure AI Studio, don't navigate to another tab
 ## Related content
 
 - [Tutorial: Deploy an enterprise chat web app](../tutorials/deploy-chat-web-app.md)
-- [How to configure a managed network](configure-managed-network.md)
\ No newline at end of file
+- [How to configure a managed network](configure-managed-network.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セキュアなデータプレイグラウンドに関する更新"
}
```

### Explanation
この更新は、「セキュアなデータプレイグラウンド」に関するドキュメント`secure-data-playground.md`におけるマイナーな変更を反映しています。具体的には、2行のテキストが修正され、特にAzure Storage Accountのロール名において「PrivilegedContributorRoleId」の部分が「Privileged Contributor」に変更されました。この変更は、役割名の正確性を向上させるものであり、ユーザーが適切な権限を理解しやすくするためのものです。

また、関連コンテンツのセクションにおいて、新たに改行が追加され、関連情報へのアクセスがよりスムーズになるよう整理されています。全体として、この変更はドキュメントの明確性を高め、ユーザーにとっての利便性が向上することを目的としています。


