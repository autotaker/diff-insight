---
date: '2025-02-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7db5cb6...MicrosoftDocs:5c1bed9
summary: この変更には、主にドキュメントのプレビュー日付と更新日に関するマイナーな更新が含まれています。PII検出機能やMistral Nemoモデル、オープンモデル、フローデプロイ、インデックス作成に関する文書の日付更新が行われました。また、手順の明確化や注意事項の追加があり、ユーザーの操作をサポートする内容が強化されています。ドキュメント全体の日付が更新され、チャットWebアプリのデプロイチュートリアルにも新しい手順が追加されました。破壊的変更は特に報告されていません。全体として、ユーザーが最新の技術やプロセスに適応できるようにすることに重点が置かれています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7db5cb6...MicrosoftDocs:5c1bed9){target="_blank"}

# ハイライト
この変更には主に、ドキュメントのプレビュー日付と更新日に関するマイナーな更新が含まれています。特に、PII検出機能のプレビュー日付の更新や、Mistral Nemoモデル、オープンモデル、フローデプロイ、およびインデックス作成に関する文書の日付更新が行われました。また、手順の明確化や注意事項の追加が行われ、ユーザーの操作をサポートする内容が加えられています。

## 新機能
- 「フローデプロイ」文書において、Microsoft.PolicyInsightsリソースプロバイダーが登録されている必要がある旨の記載が追加されました。
- Azure AI FoundryポータルでのRetrieval Augmented Generation (RAG) の実施方法について、新しい情報がインデックス追加の文書に追加されました。

## 破壊的変更
- 破壊的変更は特に報告されていません。更新はすべてドキュメントの改善と日付の更新に関するものです。

## その他の更新
- 全体的にドキュメントの日付が最新に更新されました。
- チャットWebアプリのデプロイチュートリアルに新しい手順が追加され、操作をスムーズにするための情報が追加されました。

# インサイト
このドキュメント更新の重点は、ユーザーが最新の技術とプロセスに適応できるようにすることです。特に、プレビューやリリースの日付を更新することで、最新の機能を利用するための情報を提供しています。新しい要件や手順の追加は、ユーザーが必要な事前準備を理解して、実行時にトラブルを避けるためのものであり、ドキュメントの信頼性と実用性を向上させています。

各文書での日付更新は、単なる形式的な変更ではなく、開発の実際の進行状況や機能の公開に伴うものです。例えば、PII検出機能のプレビュー日は更新されることで、その技術やアルゴリズムがアップデートされる可能性を示唆します。

また、フローデプロイやインデックス作成において具体的な新しい要件が追加されたことは、ユーザーがサービスを最大限に活用するための具体的なガイドラインを提供します。ドキュメントの手順を明確にすることで、チュートリアルの利用者が誤解や誤操作を可能な限り排除できるようにしています。

全体として、この変更は単なる技術情報の更新以上に、ユーザーエクスペリエンスを向上させ、ユーザーがより一貫性を持ってシステムを利用できるようにするためのものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-lifecycle.md](#item-417f3f) | minor update | モデルライフサイクルにおけるPII検出のプレビュー日付の更新 | modified | 1 | 1 | 2 | 
| [deploy-models-mistral-nemo.md](#item-e7b729) | minor update | Mistral Nemoモデルの展開に関する文書の日付更新 | modified | 1 | 1 | 2 | 
| [deploy-models-mistral-open.md](#item-84e005) | minor update | Mistralオープンモデルの展開に関する文書の日付更新 | modified | 1 | 1 | 2 | 
| [flow-deploy.md](#item-e7fc64) | minor update | フローデプロイに関する文書の更新 | modified | 2 | 1 | 3 | 
| [index-add.md](#item-1b013b) | minor update | インデックス作成に関する文書の内容更新 | modified | 11 | 8 | 19 | 
| [copilot-sdk-create-resources.md](#item-552960) | minor update | Copilot SDK リソース作成チュートリアルの注意事項追加 | modified | 2 | 0 | 2 | 
| [deploy-chat-web-app.md](#item-987845) | minor update | チャットWebアプリデプロイチュートリアルの手順更新 | modified | 2 | 1 | 3 | 


# Modified Contents
## articles/ai-services/language-service/concepts/model-lifecycle.md{#item-417f3f}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ Use the table below to find which model versions are supported by each feature:
 | Entity Linking                                      | `latest*`                                      |                                             |
 | Named Entity Recognition (NER)                      | `latest*`                                      | `2023-04-15-preview**`                      |
 | Personally Identifiable Information (PII) detection | `latest*`                                      | `2023-04-15-preview**`                      | 
-| PII detection for conversations                     | `latest*`                                      | `2023-04-15-preview**`                      |
+| PII detection for conversations                     | `latest*`                                      | `2024-11-01-preview**`                      |
 | Question answering                                  | `latest*`                                      |                                             |
 | Text Analytics for health                           | `latest*`                                      | `2022-08-15-preview`, `2023-01-01-preview**`|
 | Key phrase extraction                               | `latest*`                                      |                                             | 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルにおけるPII検出のプレビュー日付の更新"
}
```

### Explanation
この修正は、AIサービスに関する文書の「モデルライフサイクル」において、PII（個人を特定できる情報）検出機能のカラムのプレビュー日付を更新するものです。具体的には、従来の日付「2023-04-15-preview」が「2024-11-01-preview」に変更されました。この更新は、PII検出機能がより新しいバージョンで利用可能になることを反映しています。また、変更は1行の追加と1行の削除から成り立っており、全体の構成においてマイナーな更新と位置づけられます。データに基づくすべての情報は、スプレッドシート形式で整理され、各機能のモデルバージョンのサポート状況を明示しています。

## articles/ai-studio/how-to/deploy-models-mistral-nemo.md{#item-e7b729}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Mistral Nemo chat model with Azure AI Foundry.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 09/13/2024
+ms.date: 01/31/2025
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistral Nemoモデルの展開に関する文書の日付更新"
}
```

### Explanation
この修正は、「Mistral Nemoモデルの展開」に関する文書において、最終更新日を変更するものです。具体的には、以前の更新日である「2024年9月13日」が「2025年1月31日」に更新されました。この修正は文書の管理やレビュー情報の一環として行われており、内容自体には大きな変更はありませんが、公開予定日を最新の情報に合わせて調整しています。このような更新は、リリーススケジュールの反映やドキュメントの整合性を保つために重要です。

## articles/ai-studio/how-to/deploy-models-mistral-open.md{#item-84e005}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Mistral-7B and Mixtral chat models with Azure AI F
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 09/13/2024
+ms.date: 01/31/2025
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralオープンモデルの展開に関する文書の日付更新"
}
```

### Explanation
この修正は、「Mistralオープンモデルの展開」に関する文書において、最終更新日を変更するものです。具体的には、以前の更新日「2024年9月13日」が「2025年1月31日」に訂正されました。この変更は、文書が最新のリリーススケジュールに対応するよう整合性を図るために行われました。内容自体には大きな変更はなく、文書の管理やレビューに関する情報を反映することを目的としています。このようなマイナーな更新は、文書の信頼性を高めるために重要です。

## articles/ai-studio/how-to/flow-deploy.md{#item-e7fc64}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 01/27/2025
 ms.reviewer: gmuthukumar
 ms.author: lagayhar
 author: lgayhardt
@@ -37,6 +37,7 @@ To deploy a prompt flow as an online endpoint, you need:
 
 * An Azure subscription. If you don't have one, create a free account before you begin.
 * An Azure AI Foundry project.
+* A **Microsoft.PolicyInsights** resource provider registered in the selected subscription. For more information on registering a resource provide, see [Register resource provider](/azure/azure-resource-manager/management/resource-providers-and-types#register-resource-provider-1).
 
 ## Create an online deployment
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フローデプロイに関する文書の更新"
}
```

### Explanation
この修正は、「フローデプロイ」に関する文書に対していくつかの小さな変更を加えたものです。主な変更点は、更新日が「2024年5月21日」から「2025年1月27日」に変更された点です。また、必要な要件に「Microsoft.PolicyInsightsリソースプロバイダーが登録されていること」という新しい項目が追加されました。この変更は、リソースプロバイダーの登録に関する詳細情報を提供するためのものであり、ドキュメントの内容を最新の情報に合わせています。これにより、ユーザーが必要なリソースを確実に準備できるようになります。全体として、文書は依然として「ハウツー」トピックとして維持されており、利用者にとって役立つ情報を提供することを目的としています。

## articles/ai-studio/how-to/index-add.md{#item-1b013b}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: how-to
-ms.date: 12/11/2024
+ms.date: 01/31/2025
 ms.reviewer: estraight
 ms.author: ssalgado
 author: ssalgadodev
@@ -19,24 +19,26 @@ author: ssalgadodev
 
 [!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
-In this article, you learn how to create and use a vector index for performing [Retrieval Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md).
+In this article, you learn how to create and use a vector index for performing [Retrieval Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) in the Azure AI Foundry portal.
+
+A vector index isn't required for RAG, but a vector query can match on semantically similar content, which is useful for RAG workloads.
 
 ## Prerequisites
 
 You must have:
 - An Azure AI Foundry project
-- An Azure AI Search resource
+- An [Azure AI Search resource](/azure/search/search-create-service-portal)
+- You should have content in a supported format that provides sufficient information for a chat experience. It can be an existing index on Azure AI Search, or create a new index using content files in Azure Blob Storage, your local system, or data in Azure AI Foundry.
 
 ## Create an index from the Chat playground
 
 1. Sign in to [Azure AI Foundry](https://ai.azure.com).
 1. Go to your project or [create a new project](../how-to/create-projects.md) in Azure AI Foundry portal.
-1. From the menu on the left, select **Playgrounds**.
-
+1. From the menu on the left, select **Playgrounds**. Select the **Chat Playground**.
 
     :::image type="content" source="../media/index-retrieve/project-left-menu.png" alt-text="Screenshot of Project Left Menu." lightbox="../media/index-retrieve/project-left-menu.png":::
 
-1. Select a deployed model. If you have not done so already, deploy a model by selecting **Create new deployment**.
+1. Select a deployed chat completion model. If you have not done so already, deploy a model by selecting **Create new deployment**.
 
    :::image type="content" source="../media/index-retrieve/create-deployment.png" alt-text="Screenshot of create a deployment button." lightbox="../media/index-retrieve/create-deployment.png":::
    
@@ -46,11 +48,13 @@ You must have:
    
 1. Choose your **Source data**. You can choose source data from a list of your recent data sources, a storage URL on the cloud, or upload files and folders from the local machine. You can also add a connection to another data source such as Azure Blob Storage.
 
+   If you don't have sample data, you can [download these PDFs](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/health-plan) to your local system, and then upload them as your source data.
+
     :::image type="content" source="../media/index-retrieve/select-source-data.png" alt-text="Screenshot of select source data." lightbox="../media/index-retrieve/select-source-data.png":::
 
 1. Select **Next** after choosing source data
 1. Choose the **Index Storage** - the location where you want your index to be stored in the **Index configuration** tab. 
-1. If you already have an Azure AI Search resource, you can choose that from the dropdown.
+1. If you already have an Azure AI Search resource, you can browse the list of search service resources for your subscription and then select **Connect** for the one you want to use. If you're connecting with API keys, confirm your search service [uses API keys](/azure/search/search-security-api-keys).
 
     :::image type="content" source="../media/index-retrieve/index-storage.png" alt-text="Screenshot of select index store." lightbox="../media/index-retrieve/index-storage.png":::
 
@@ -62,7 +66,6 @@ You must have:
 1. Review the details you entered and select **Create**
 1. You're taken to the index details page where you can see the status of your index creation.
 
-
 ## Use an index in prompt flow
 
 1. Sign in to [Azure AI Foundry](https://ai.azure.com) and select your project. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス作成に関する文書の内容更新"
}
```

### Explanation
この修正は、「インデックス追加」に関する文書に対する更新で、主に内容の明確化と日付の変更を含んでいます。最終更新日は「2024年12月11日」から「2025年1月31日」に変更され、新しい情報として、「Azure AI FoundryポータルにおけるRetrieval Augmented Generation (RAG)」の実施方法について詳しく説明が加えられました。また、インデックス作成の要件に「Azure AI Searchリソース」が具体的なリンクを伴って説明され、必要なデータのアップロード方法やサンプルデータの入手方法についても詳細が記載されています。これにより、ユーザーはインデックス作成のプロセスをより理解しやすくなり、実際に手順を追いやすくなっています。このような小さな更新は、文書の利用価値を高め、最新の技術やプロセスに対応するのに役立ちます。

## articles/ai-studio/tutorials/copilot-sdk-create-resources.md{#item-552960}

<details>
<summary>Diff</summary>
````diff
@@ -138,6 +138,8 @@ Create a folder for your work. Create a file called **config.py** in this folder
 
 :::code language="python" source="~/azureai-samples-main/scenarios/rag/custom-rag-app/config.py":::
 
+> [!NOTE]
+> This script also uses a package you haven't installed yet, `azure.monitor.opentelemetry`.  You'll install this package in the next part of the tutorial series.
 
 ## Configure environment variables
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Copilot SDK リソース作成チュートリアルの注意事項追加"
}
```

### Explanation
この修正は、「Copilot SDKを使用したリソース作成」に関するチュートリアルにおいて、注意事項を追加する内容です。具体的には、ユーザーが作成する「config.py」ファイルに関する補足情報が追加されました。このスクリプトで使用するパッケージ「azure.monitor.opentelemetry」がまだインストールされていないことが明示されており、このパッケージは次のチュートリアル部でインストールすることが説明されます。この更新により、ユーザーは必要なパッケージを事前に理解し、適切な準備をすることができるため、全体の学習体験が向上します。

## articles/ai-studio/tutorials/deploy-chat-web-app.md{#item-987845}

<details>
<summary>Diff</summary>
````diff
@@ -41,7 +41,7 @@ The steps in this tutorial are:
 
 - A local copy of product data. The [Azure-Samples/rag-data-openai-python-promptflow repository on GitHub](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/) contains sample retail product information that's relevant for this tutorial scenario. Specifically, the `product_info_11.md` file contains product information about the TrailWalker hiking shoes that's relevant for this tutorial example. [Download the example Contoso Trek retail product data in a ZIP file](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/raw/refs/heads/main/tutorial/data/product-info.zip) to your local machine.
 
-- A **Microsoft.Web** resource provider registered in the selected subscription, to be able to deploy to a web app. For more information on registering a resource provide, see [Register resource provider](/azure/azure-resource-manager/management/resource-providers-and-types#register-resource-provider-1).
+- A **Microsoft.Web** resource provider registered in the selected subscription, to be able to deploy to a web app. For more information on registering a resource provider, see [Register resource provider](/azure/azure-resource-manager/management/resource-providers-and-types#register-resource-provider-1).
 
 - Necessary permissions to add role assignments in your Azure subscription. Granting permissions by role assignment is only allowed by the Owner of the specific Azure resources.
 
@@ -207,6 +207,7 @@ You're almost there. Now you can test the web app.
 1. If you changed settings, wait 10 minutes or so for the authentication settings to take effect.
 1. Return to the browser tab containing the chat playground page in the Azure AI Foundry portal.
 1. Select **Launch** to launch the deployed web app. If prompted, accept the permissions request.
+1. If you don't see **Launch** in the playground, select **Web apps** from the left pane, then select your app from the list to launch it.
 
     *If the authentication settings haven't yet taken effect, close the browser tab for your web app and return to the chat playground in the Azure AI Foundry portal. Then wait a little longer and try again.*
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットWebアプリデプロイチュートリアルの手順更新"
}
```

### Explanation
この修正は、「チャットWebアプリのデプロイ」に関するチュートリアルにおいて、手順の明確化と重要な情報の追加を含んでいます。具体的には、Webアプリをデプロイするために必要な「Microsoft.Webリソースプロバイダー」の登録に関する説明が若干明確化されました。また、アプリが見つからない場合の対処方法として、チャットプレイグラウンドで**Launch**ボタンが表示されない場合の手順が追加されました。ユーザーは左側のメニューから**Web apps**を選択し、アプリのリストから対象のアプリを選択することで起動できることが明示されています。このような小さな更新は、ユーザーが手順を誤ることを防ぎ、スムーズに作業を進められるようにすることを目的としています。


