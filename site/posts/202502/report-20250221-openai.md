---
date: '2025-02-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:11dfa93...MicrosoftDocs:6d12544
summary: この差分では、Azure OpenAI サービスに関するドキュメントがマイナーに更新され、新しいモデルのリリースや利用可能性、セットアップ手順、利用ガイドライン、デプロイメント条件についての情報が追加または更新されています。具体的な変更点として、`o1-preview`
  モデルの延期、`o3-mini` モデルの制限付きアクセスの顧客への提供、`gpt-4o-mini-audio-preview` モデルの紹介が含まれています。また、全てのモデルにコンテンツフィルタが適用可能になったことが大きなポリシーの変更とされています。この更新により、ユーザーは新たな機能と改善された情報の鮮度を享受でき、サービス利用の効率が高まると期待されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:11dfa93...MicrosoftDocs:6d12544){target="_blank"}

# ハイライト

この差分では、Azure OpenAI サービスに関するいくつかのドキュメントがマイナーに更新されました。主な変更点として、新しいモデルやその利用可能性、セットアップ手順、利用ガイドライン、そしてデプロイメント条件などについての情報が追加または更新されています。

## 新機能
- `o1-preview` モデルのリリースの延期と利用可能性の追加。
- `o3-mini` モデルのグローバル標準およびデータゾーン標準デプロイメントが制限付きアクセスの顧客に利用可能に。
- `gpt-4o-mini-audio-preview` モデルの紹介により、音声生成に関する新たな案内が提供。

## 重大な変更
特に重大な変更はありませんが、コンテンツフィルタの設定が全ての Azure OpenAI モデルに適用可能となった点は、以前のドキュメントと比べて大きなポリシー変更となるかもしれません。

## その他の更新
- 文書の最終更新日が一部変更。
- モデルの地域情報やアクセス条件が整理され、より明確に。
- データ利用におけるベストプラクティスとアップロード方法に関する指針が追加。
- Azure Developer CLIの利用のための新たな権限要件。

# 洞察

このコード差分では、Azure OpenAI サービスを利用する上での様々な側面が細かく更新されており、ユーザーに提供される情報の鮮度と信頼性が向上しています。例えば、新モデルや機能の追加により、ユーザーにとっての選択肢が広がり、サービスの柔軟な活用が促進されています。また、可視性やアクセス条件の改善により、ユーザーは自身の利用状況をより正確に把握し、それに応じた計画を立てるための材料を得ることができます。

さらに、データの取り扱いやセットアップ手順が明確化されていることで、ユーザーは自分のプロセスを最適化しやすく、効率的な操作を行うことが可能となります。特に、新規ユーザーや技術知識に乏しい利用者にとっては、これらのガイドラインに従うことで、Azure OpenAI サービスをストレスフリーで利用できるでしょう。

全体として、このドキュメントの更新は、ユーザーエクスペリエンスの向上を直接的に目的としたものであり、Azure OpenAI サービスの利用のしやすさを増進する方向に寄与しています。ユーザーは、今回の更新を通じてより豊富で最新の機能を享受できると期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルの廃止および退職に関するドキュメントの更新 | modified | 6 | 1 | 7 | 
| [models.md](#item-db2c37) | minor update | モデルに関するドキュメントの更新 | modified | 9 | 4 | 13 | 
| [use-your-data.md](#item-455d6e) | minor update | データ利用に関するガイドラインの更新 | modified | 3 | 1 | 4 | 
| [azure-developer-cli.md](#item-3d4cfb) | minor update | Azure Developer CLIに関する要件の追加 | modified | 1 | 0 | 1 | 
| [reasoning.md](#item-a54b2f) | minor update | モデル利用可能性に関する情報の更新 | modified | 5 | 5 | 10 | 
| [assistants-javascript.md](#item-ad3627) | minor update | セットアップ手順のフォーマット修正 | modified | 1 | 1 | 2 | 
| [content-filter-configurability.md](#item-11f064) | minor update | コンテンツフィルタの可用性に関する情報の更新 | modified | 1 | 12 | 13 | 
| [datazone-standard.md](#item-188333) | minor update | モデルマトリックスの更新 | modified | 15 | 15 | 30 | 
| [monitor-openai-reference.md](#item-8d8887) | minor update | 監視データ参照の更新日付修正 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-53303b) | minor update | 2月の新機能の更新 | modified | 7 | 1 | 8 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 02/12/2025
+ms.date: 02/20/2025
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -111,6 +111,7 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-4o-mini` | 2024-07-18 | No earlier than July 18, 2025  | |
 | `gpt-4o-realtime-preview` | 2024-10-01 | No earlier than September 30, 2025  | `gpt-4o-realtime-preview` (version 2024-12-17) or `gpt-4o-mini-realtime-preview` (version 2024-12-17) |
 | `gpt-3.5-turbo-instruct` | 0914 | No earlier than May 31, 2025 |  |
+| `o1-preview` | 2024-09-12 | No earlier than April 2, 2025 | `o1` |
 | `o1` | 2024-12-17 | No earlier than December 17, 2025 | |
 | `text-embedding-ada-002` | 2 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
 | `text-embedding-ada-002` | 1 | No earlier than October 3, 2025 | `text-embedding-3-small` or `text-embedding-3-large` |
@@ -170,6 +171,10 @@ If you're an existing customer looking for information about these models, see [
 
 ## Retirement and deprecation history
 
+## February 20, 2025
+
+- `o1-preview` updated to no earlier than April 2, 2025.
+
 ## February 12, 2025
 
 - Updates to `gpt-35-turbo-16k` (0613), (1106), `gpt-35-turbo-instruct`, `gpt-4` (turbo-2024-04-09)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの廃止および退職に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関する「モデルの廃止および退職」に関するドキュメントに対するマイナーな更新です。具体的には、文書の最終更新日が2025年2月12日から2025年2月20日に変更され、さらに新しいモデル `o1-preview` のリリース日が2025年4月2日以降に延長されたことが記載されました。また、この変更では、`o1-preview` モデルが新たにリストに追加され、利用可能なモデルの更新情報も提供されています。これにより、ユーザーは最新のモデル情報を把握しやすくなります。全体として、ドキュメントの情報が最新のものに保たれ、ユーザーにとっての価値が向上しています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 2/14/2025
+ms.date: 2/19/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -53,9 +53,9 @@ To learn more about the advanced `o-series` models see, [getting started with re
 
 | Model | Region |
 |---|---|
-|`o3-mini` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
-|`o1` | East US2 (Global Standard) <br> Sweden Central (Global Standard) |
-| `o1-preview` | See the [models table](#model-summary-table-and-region-availability). This model is only available for customers who were granted access as part of the original limited access release. |
+|`o3-mini` | See the [models table](#model-summary-table-and-region-availability). |
+|`o1` | See the [models table](#model-summary-table-and-region-availability). |
+| `o1-preview` | See the [models table](#model-summary-table-and-region-availability). This model is only available for customers who were granted access as part of the original limited access |
 | `o1-mini` | See the [models table](#model-summary-table-and-region-availability). |
 
 ## GPT-4o audio
@@ -244,6 +244,11 @@ All deployments can perform the exact same inference operations, however the bil
 
 [!INCLUDE [Data zone standard](../includes/model-matrix/datazone-standard.md)]
 
+> [!NOTE]
+> **Most o-series models are limited access**. Request access: [limited access model application](https://aka.ms/OAI/o1access). `o1-mini` is currently available to all customers for global standard deployment.
+>
+> Select customers were granted standard (regional) deployment access to `o1-mini` as part of the `o1-preview` limited access release. At this time access to `o1-mini` standard (regional) deployments is not being expanded.
+
 # [Data Zone Provisioned Managed](#tab/datazone-provisioned-managed)
 
 ### Data zone provisioned managed model availability
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルに関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAI サービスに関連する「モデル」に関するドキュメントのマイナーな更新を示しています。主な変更点として、文書の最終更新日が2025年2月14日から2025年2月19日に変更されたことがあります。また、モデルに関する情報が整理され、`o3-mini` と `o1` モデルの地域情報が更新されました。

具体的には、これらのモデルへのアクセスが「モデルのサマリーテーブル」へのリンクを通じて提供され、元々の限定アクセスリリースの一環としてこれらのモデルにアクセスできる顧客に関する情報が明記されています。さらに、新たに追加された情報として、ほとんどの `o-series` モデルは限定アクセスであることが注記され、アクセスリクエストのリンクも提供されています。この変更により、利用可能なモデルの理解が深まり、ユーザーは自身の利用状況を把握しやすくなります。全体として、ドキュメントの最新情報が反映され、ユーザーへの価値が向上しています。

## articles/ai-services/openai/concepts/use-your-data.md{#item-455d6e}

<details>
<summary>Diff</summary>
````diff
@@ -71,6 +71,9 @@ There's an [upload limit](../quotas-limits.md), and there are some caveats about
 
 You need to connect to a data source to upload your data. When you want to use your data to chat with an Azure OpenAI model, your data is chunked in a search index so that relevant data can be found based on user queries.
 
+> [!NOTE]
+> Your data should be unstructured text for best results. If you have non-textual semi-structured or structured data consider converting it to text. If your files have special formatting, such as tables and columns, or bullet points, prepare your data with the data preparation script available on [GitHub](https://github.com/microsoft/sample-app-aoai-chatGPT/tree/main/scripts#optional-crack-pdfs-to-text).
+
 The [Integrated Vector Database in vCore-based Azure Cosmos DB for MongoDB](/azure/cosmos-db/mongodb/vcore/vector-search) natively supports integration with Azure OpenAI On Your Data.
 
 For some data sources such as uploading files from your local machine (preview) or data contained in a blob storage account (preview), Azure AI Search is used. When you choose the following data sources, your data is ingested into an Azure AI Search index.
@@ -82,7 +85,6 @@ For some data sources such as uploading files from your local machine (preview)
 |URL/Web address (preview)        | Web content from the URLs is stored in Azure Blob Storage.         |
 |Azure Blob Storage (preview) | Upload files from Azure Blob Storage to be ingested into an Azure AI Search index.         |
 
-If you choose to upload files or connect Azure Blob Storage, your data should be unstructured text for best results. If you have non-textual semi-structured or structured data consider converting it to text. If your files have special formatting, such as tables and columns, or bullet points, prepare your data with the data preparation script available on [GitHub](https://github.com/microsoft/sample-app-aoai-chatGPT/tree/main/scripts#optional-crack-pdfs-to-text).
 
 :::image type="content" source="../media/use-your-data/azure-databases-and-ai-search.png" lightbox="../media/use-your-data/azure-databases-and-ai-search.png" alt-text="Diagram of vector indexing services.":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ利用に関するガイドラインの更新"
}
```

### Explanation
この変更は、Azure OpenAI モデルとデータを使用する際のガイドラインに関する文書のマイナーな更新を示しています。主な変更点は、データをアップロードする際のベストプラクティスについての注意事項を追加したことです。具体的には、「最良の結果を得るためには、データは非構造化テキストであるべきであり、非テキストの半構造化または構造化データがある場合はテキストに変換することを検討する」という内容が強調されています。

さらに、特別なフォーマット（例えば、表や列、箇条書きなど）を持つファイルの場合は、データ準備スクリプトを使ってデータを準備することを勧める情報も追加されました。これにより、ユーザーがより効果的に自分のデータを加工し、Azure OpenAI モデルを活用する助けとなる内容が充実しました。この変更によって、データを使用する際の理解が深まり、ユーザーにとっての利便性が向上しています。

## articles/ai-services/openai/how-to/azure-developer-cli.md{#item-3d4cfb}

<details>
<summary>Diff</summary>
````diff
@@ -19,6 +19,7 @@ Use this article to learn how to automate resource deployment for Azure OpenAI S
 
 - An Azure subscription. [Create one for free](https://azure.microsoft.com/free/cognitive-services).
 - The Azure Developer CLI [installed](/azure/developer/azure-developer-cli/install-azd) on your machine.
+- Ability to assign permissions at the Subscription level (Owner or User Access Administrator).
 
 ## Clone and initialize the Azure Developer CLI template
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Developer CLIに関する要件の追加"
}
```

### Explanation
この変更は、Azure OpenAI サービスのリソース展開を自動化するための Azure Developer CLI に関する文書における要件のマイナーな更新を示しています。具体的には、Azure Developer CLI を使用するための新しい要件として、「サブスクリプションレベル（オーナーまたはユーザーアクセス管理者）で権限を割り当てる能力」が追加されました。

この変更により、ユーザーはAzure Developer CLIを使用する際に必要な権限管理の理解が深まります。この情報は、リソースの自動展開を行う上での重要な要素となるため、特に新規ユーザーや、まだ権限設定について詳しくない利用者にとって有用です。この更新によって、Azure Developer CLI の利用に際しての前提条件がクリアになるため、よりスムーズな操作が期待されます。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's advanced o3-mini, o1, & o1-mini rea
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 02/06/2025
+ms.date: 02/19/2025
 author: mrbullwinkle    
 ms.author: mbullwin
 ---
@@ -34,10 +34,10 @@ Request access: [limited access model application](https://aka.ms/OAI/o1access)
 
 | Model | Region | Limited access |
 |---|---|---|
-| `o3-mini` | East US2 (Global Standard) <br> Sweden Central (Global Standard) | [Limited access model application](https://aka.ms/OAI/o1access) |
-|`o1` | East US2 (Global Standard) <br> Sweden Central (Global Standard) | [Limited access model application](https://aka.ms/OAI/o1access) |
-| `o1-preview` | See [models page](../concepts/models.md#global-standard-model-availability). |This model is only available for customers who were granted access as part of the original limited access release. We're currently not expanding access to `o1-preview`. |
-| `o1-mini` | See [models page](../concepts/models.md#global-standard-model-availability). | No access request needed for Global Standard deployments.<br><br>Standard (regional) deployments are currently only available to select customers who were previously granted access as part of the `o1-preview` release.|
+| `o3-mini` | [Model availability](../concepts/models.md#global-standard-model-availability).  | [Limited access model application](https://aka.ms/OAI/o1access) |
+|`o1` | [Model availability](../concepts/models.md#global-standard-model-availability).  | [Limited access model application](https://aka.ms/OAI/o1access) |
+| `o1-preview` | [Model availability](../concepts/models.md#global-standard-model-availability). |This model is only available for customers who were granted access as part of the original limited access release. We're currently not expanding access to `o1-preview`. |
+| `o1-mini` | [Model availability](../concepts/models.md#global-standard-model-availability). | No access request needed for Global Standard deployments.<br><br>Standard (regional) deployments are currently only available to select customers who were previously granted access as part of the `o1-preview` release.|
 
 ## API & feature support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル利用可能性に関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAI のモデルに関するまでの情報を含む文書のマイナーな更新を示しています。具体的には、モデルの利用可能性に関連するテーブルの内容が修正され、モデルの地域や制限付きアクセスの情報がより明確に示されるようになりました。

主な変更点として、各モデルの利用可能性に「モデルの利用可能性」というリンクが追加され、リンクをクリックすることでモデルの詳細情報にアクセスできるようになっています。また、日付情報も更新され、最新の内容が反映されています。これにより、ユーザーはモデルの地域ごとの展開やアクセス条件について、より容易に情報を取得できるようになり、Azure OpenAI サービスの利用が向上することが期待されます。全体的に、この更新はユーザーの利便性を高めるための重要な改善といえます。

## articles/ai-services/openai/includes/assistants-javascript.md{#item-ad3627}

<details>
<summary>Diff</summary>
````diff
@@ -29,7 +29,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 - Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
 ## Set up
-
+ 
 1. Create a new folder `assistants-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セットアップ手順のフォーマット修正"
}
```

### Explanation
この変更は、Azure OpenAI に関する文書内の JavaScript アシスタントに関連するセットアップ手順のマイナーな更新を示しています。具体的には、セットアップセクションのテキストにおいて、冒頭の行が削除され、空白行が追加されました。

これにより、手順がより明確に区切られるようになり、ユーザーが手順に従いやすくなります。また、読みやすさの向上が図られており、特にコードスニペットの前に余計な情報がなくなることで、ユーザーは手順に集中できるようになります。全体として、この更新はドキュメントの可読性を高め、利用者にとっての理解を容易にする重要な調整を行っていると評価できます。

## articles/ai-services/openai/includes/content-filter-configurability.md{#item-11f064}

<details>
<summary>Diff</summary>
````diff
@@ -26,18 +26,7 @@ All customers can also configure content filters and create custom safety polici
 
 <sup>1</sup> For Azure OpenAI models, only customers who have been approved for modified content filtering have full content filtering control and can turn off content filters. Apply for modified content filters via this form: [Azure OpenAI Limited Access Review: Modified Content Filters](https://ncv.microsoft.com/uEfCgnITdR). For Azure Government customers, apply for modified content filters via this form: [Azure Government - Request Modified Content Filtering for Azure OpenAI Service](https://aka.ms/AOAIGovModifyContentFilter).
 
-Configurable content filters for inputs (prompts) and outputs (completions) are available for the following Azure OpenAI models:
-* GPT model series
-* GPT-4 Turbo Vision GA<sup>*</sup> (`turbo-2024-04-09`)
-* GPT-4o
-* GPT-4o mini
-* DALL-E 2 and 3
-
-Configurable content filters are not available for 
-- o1-preview
-- o1-mini 
-
-<sup>*</sup>Only available for GPT-4 Turbo Vision GA, does not apply to GPT-4 Turbo Vision preview 
+Configurable content filters for inputs (prompts) and outputs (completions) are available for all Azure OpenAI models.
 
 Content filtering configurations are created within a Resource in Azure AI Foundry portal, and can be associated with Deployments. [Learn more about configurability here](../how-to/content-filters.md).  
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタの可用性に関する情報の更新"
}
```

### Explanation
この変更は、Azure OpenAI のコンテンツフィルタの設定可能性に関する文書におけるマイナーな更新を示しています。主な変更点は、設定可能なコンテンツフィルタが特定のモデルに制限されていた情報が削除され、全ての Azure OpenAI モデルに対して設定可能であることが明記されたことです。

具体的には、以前は特定の GPT モデルシリーズと DALL-E に対してのみ適用されていた設定可能なコンテンツフィルタの情報が、現在は全てのモデルに対して利用できる旨に修正されています。この変更により、ユーザーはどのモデルにおいてもコンテンツフィルタの設定を行えることが明確となり、より一層の利用促進が期待されます。また、ドキュメント全体がより正確かつユーザーフレンドリーなものとなるよう改善されています。

## articles/ai-services/openai/includes/model-matrix/datazone-standard.md{#item-188333}

<details>
<summary>Diff</summary>
````diff
@@ -6,20 +6,20 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 10/31/2024
+ms.date: 02/19/2025
 ---
 
-| **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|
-| eastus             | ✅                       | ✅                       | ✅                            |
-| eastus2            | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | ✅                       | ✅                       | ✅                            |
-| northcentralus     | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                       | ✅                       | ✅                            |
-| southcentralus     | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | ✅                       | ✅                       | ✅                            |
-| westeurope         | ✅                       | ✅                       | ✅                            |
-| westus             | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                       | ✅                       | ✅                            |
+| **Region**     | **o3-mini**, **2025-01-31**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:---------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
+| eastus             | ✅                        | ✅                       | ✅                       | ✅                            |
+| eastus2            | ✅                        | ✅                       | ✅                       | ✅                            |
+| francecentral      | -                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | -                       | ✅                       | ✅                       | ✅                            |
+| northcentralus     | ✅                        | ✅                       | ✅                       | ✅                            |
+| polandcentral      | -                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                        | ✅                       | ✅                       | ✅                            |
+| spaincentral       | -                       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | -                       | ✅                       | ✅                       | ✅                            |
+| westeurope         | -                       | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                        | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                        | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリックスの更新"
}
```

### Explanation
この変更は、Azure OpenAI に関するモデルマトリックスの情報を更新したことを示しています。具体的には、日付が `10/31/2024` から `02/19/2025` に変更され、モデルのバージョンと地域の情報が新しい形式に改訂されました。

新しいマトリックスでは、モデル `o3-mini` が追加され、異なる地域における各日付でのモデルの可用性が明確に示されています。また、一部の地域ではモデルの利用可否が不明なことを表すために `-` 記号が使われるようになりました。全体として、これにより、ユーザーは最新のモデルとその可用性についての情報をよりわかりやすく得ることができ、Azure OpenAI サービスの活用を促進することが期待されます。

## articles/ai-services/openai/monitor-openai-reference.md{#item-8d8887}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Monitoring data reference for Azure OpenAI
 description: This article contains important reference material you need when you monitor Azure OpenAI Service by using Azure Monitor.
-ms.date: 08/20/2024
+ms.date: 02/20/2025
 ms.custom: horz-monitor, subject-monitoring
 ms.topic: reference
 author: mrbullwinkle
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "監視データ参照の更新日付修正"
}
```

### Explanation
この変更は、Azure OpenAI の監視データ参照に関する文書の更新を示しています。具体的には、文書の更新日付が `08/20/2024` から `02/20/2025` に変更されました。これにより、文書の鮮度が保たれ、ユーザーは最新の情報を基に Azure OpenAI サービスを監視する際の重要な参照資料として利用できるようになります。この変更は、主に文献の管理とユーザーへの情報提供の明確さを向上させるために行われました。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: whats-new
-ms.date: 2/6/2025
+ms.date: 2/19/2025
 recommendations: false
 ---
 
@@ -21,6 +21,12 @@ This article provides a summary of the latest releases and major documentation u
 
 ## February 2025
 
+### o3-mini datazone standard deployments
+
+`o3-mini` is now available for global standard, and data zone standard deployments for registered limited access customers. Data standard deployment regions are currently United States regions only.
+
+For more information, see our [reasoning model guide](./how-to/reasoning.md). 
+
 ### gpt-4o mini audio released
 
 The `gpt-4o-mini-audio-preview` (2024-12-17) model is the latest audio completions model. For more information, see the [audio generation quickstart](./audio-completions-quickstart.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "2月の新機能の更新"
}
```

### Explanation
この変更は、Azure OpenAI の「新機能」文書における情報の更新を示しています。具体的には、文書の日付が `2/6/2025` から `2/19/2025` に変更され、2月2025年の新機能に関する内容が追加されました。

更新内容には、`o3-mini` のグローバル標準およびデータゾーン標準デプロイメントが、制限付きアクセスの顧客向けに利用可能になったことが含まれています。また、データ標準デプロイメント地域が現時点ではアメリカ地域に限定されていることが明記されています。さらに、`gpt-4o-mini-audio-preview` モデルが最新の音声完了モデルとして紹介されており、音声生成に関するクイックスタートガイドへのリンクも提供されています。この変更により、ユーザーは最新の機能とリリース情報にアクセスしやすくなります。


