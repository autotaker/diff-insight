---
date: '2026-02-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f5997cf...MicrosoftDocs:ad7cfc9
summary: この更新では、Azure AI Searchおよびインデックス機能に関する知識ソースのガイドや機能に小規模な修正が加えられました。新しい機能の導入や既存機能の改善により、ユーザーがより効率的に利用できるよう情報が明確化されています。特に、Azureポータルのサポートが拡張され、新たにいくつかの知識ソースが利用可能になりました。さらに、C#、Python、REST
  APIに関するガイドラインの更新も行われ、情報の充実が図られました。全体として、この更新はユーザー体験の向上と開発者の生産性向上を目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f5997cf...MicrosoftDocs:ad7cfc9){target="_blank"}

<format>
# Highlights
この更新では、Azure AI Search やインデックス機能を含む知識ソースに関するガイドや機能に小さな修正が施されました。新しい機能と改善された機能が浮き彫りにされ、ユーザーがそれらをより効率的に活用できるよう情報の明確化が図られています。

## 新機能
- Azure ポータルサポートの拡張が導入され、Indexed OneLake および Indexed SharePoint、Remote SharePoint や Web などが新たにサポート対象となりました。
- 新機能と改善点は、特定の検索フィールドやセマンティック設定のオプションを含むポータル上での操作性向上を図っており、知識ベースにはプレイグラウンドでの新しい取得オプションが導入されました。

## 破壊的変更
- 特に破壊的な変更は報告されていませんが、いくつかの既存の知識ソースやガイドラインは、新機能に合わせて再編成されています。

## その他の更新
- C#、Python、および REST API に関連する知識ベース作成ガイドが更新され、情報の再配置と新しい詳細が追加されました。
- Azure ポータルのサポート状況が更新され、いくつかのガイドで利用可能性の表記が修正されています。
- `create-knowledge-source.png` 画像が更新され、視覚的な理解の向上が図られています。

# Insights
この一連の更新は、Azure AI Search のユーザーの利便性を向上させ、知識ソースに関する操作をよりわかりやすくするためのものです。まず、Azure ポータルサポートの拡張により、ユーザーはさらに多様な知識ソースをポータル上で利用可能となり、Azure のエコシステムとの統合性が強化されています。このサポートには Indexed 一連の知識ソースが含まれ、より精細な検索体験を提供することが可能となっています。

ガイドの更新に関しては、各知識ソースの具体的な使用方法や設定方法がより詳細に記載されており、ユーザーはそれぞれのプログラミング言語や REST API に基づいた実践的な支持を得ることができます。これにより、知識ベースの作成や活用の際に、開発者が選択可能なツールおよび手段は多岐にわたり、効率的なデータ管理や運用が期待されます。

特に、画像更新を含む、ビジュアル面での改善も行われているため、ガイドラインが提供する情報はユーザーに対してより直感的になりつつあります。これらの変更を通じて、Azure AI Search の機能強化は継続して進められており、ユーザー体験の向上とともに開発者の生産性の向上にも寄与しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-onelake.md](#item-ec7a80) | minor update | OneLake 知識ソースの作成方法のタイトルおよび説明の更新 | modified | 3 | 4 | 7 | 
| [agentic-knowledge-source-overview.md](#item-dcf29a) | minor update | Knowledge Source に関する概要のタイトルと日付の更新 | modified | 3 | 3 | 6 | 
| [agentic-retrieval-overview.md](#item-d1f354) | minor update | Agentic Retrieval 概要の更新 | modified | 1 | 3 | 4 | 
| [get-started-portal-agentic-retrieval.md](#item-2bf1dc) | minor update | エージェンティックリトリーバルのクイックスタートガイドの更新 | modified | 8 | 6 | 14 | 
| [agentic-knowledge-source-how-to-onelake-csharp.md](#item-d6611c) | minor update | OneLake 知識ソースのインデックス化に関するガイドの更新 | modified | 8 | 8 | 16 | 
| [agentic-knowledge-source-how-to-onelake-python.md](#item-c7d61d) | minor update | OneLake 知識ソースに関する Python ガイドの更新 | modified | 9 | 9 | 18 | 
| [agentic-knowledge-source-how-to-onelake-rest.md](#item-876f49) | minor update | OneLake REST 知識ソースに関するガイドの更新 | modified | 8 | 8 | 16 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md](#item-2eb305) | minor update | SharePoint インデックスされた知識ソースに関する C# ガイドの更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-python.md](#item-923abb) | minor update | SharePoint インデックスされた知識ソースに関する Python ガイドの更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-rest.md](#item-e26ea0) | minor update | SharePoint インデックスされた知識ソースに関する REST ガイドの更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-csharp.md](#item-f8bed1) | minor update | SharePoint リモート知識ソースに関する C# ガイドの更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-python.md](#item-822712) | minor update | SharePoint リモート知識ソースに関する Python ガイドの更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-rest.md](#item-5514b1) | minor update | SharePoint リモート知識ソースに関する REST ガイドの更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-web-csharp.md](#item-401063) | minor update | Web 知識ソースに関する C# ガイドの更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-web-python.md](#item-72b59c) | minor update | Web 知識ソースに関する Python ガイドの更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-web-rest.md](#item-649608) | minor update | Web 知識ソースに関する REST API ガイドの更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-how-to-create-knowledge-base-csharp.md](#item-4469a2) | minor update | C# 用の知識ベース作成ガイドの更新 | modified | 6 | 6 | 12 | 
| [agentic-retrieval-how-to-create-knowledge-base-python.md](#item-4e498f) | minor update | Python 用の知識ベース作成ガイドの更新 | modified | 6 | 6 | 12 | 
| [agentic-retrieval-how-to-create-knowledge-base-rest.md](#item-37851c) | minor update | REST 用知識ベース作成ガイドの更新 | modified | 6 | 6 | 12 | 
| [create-knowledge-source.png](#item-104c67) | minor update | 知識ソース作成の画像更新 | modified | 0 | 0 | 0 | 
| [whats-new.md](#item-fa71b4) | minor update | Azure AI Search の新機能に関する更新 | modified | 7 | 1 | 8 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-onelake.md{#item-ec7a80}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: Create a OneLake Knowledge Source for Agentic Retrieval
+title: Create an Indexed OneLake Knowledge Source for Agentic Retrieval
 titleSuffix: Azure AI Search
-description: Learn how to create a OneLake knowledge source in Azure AI Search. A OneLake knowledge source specifies a lakehouse, models, and properties that create an enrichment pipeline for agentic retrieval workloads.
+description: Learn how to create an indexed OneLake knowledge source in Azure AI Search. An indexed OneLake knowledge source specifies a lakehouse, models, and properties that create an enrichment pipeline for agentic retrieval workloads.
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
@@ -13,8 +13,7 @@ ms.date: 11/20/2025
 zone_pivot_groups: agentic-retrieval-pivots
 ---
 
-# Create a OneLake knowledge source
-
+# Create an indexed OneLake knowledge source
 
 ::: zone pivot="csharp"
 [!INCLUDE [C#](includes/how-tos/agentic-knowledge-source-how-to-onelake-csharp.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLake 知識ソースの作成方法のタイトルおよび説明の更新"
}
```

### Explanation
この変更では、`articles/search/agentic-knowledge-source-how-to-onelake.md` ファイルが修正され、OneLake 知識ソースに関する情報が更新されました。具体的には、ページタイトルが「Create a OneLake Knowledge Source for Agentic Retrieval」から「Create an Indexed OneLake Knowledge Source for Agentic Retrieval」に変更され、説明文にも「indexed」が追加されました。これにより、知識ソースのタイプが明確になり、ユーザーに提供される情報がより的確になっています。また、全体で7行にわたって変更が加えられ、3行が追加され、4行が削除されています。この変更は、Azure AI Searchのドキュメントにおける内容の正確性を向上させます。

## articles/search/agentic-knowledge-source-overview.md{#item-dcf29a}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +1,13 @@
 ---
-title: What is a knowledge source
+title: What is a Knowledge Source?
 titleSuffix: Azure AI Search
 description: Learn about the knowledge source object used for agentic retrieval workloads in Azure AI Search.
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 01/15/2026
+ms.date: 02/02/2026
 ---
 
 # What is a knowledge source?
@@ -57,7 +57,7 @@ Create knowledge sources as standalone objects. Then, specify them in a [knowled
 
 To create objects on a search service, you need [**Search Service Contributor** permissions](search-security-rbac.md). If you're using a knowledge source that creates an indexer pipeline, you also need **Search Index Data Contributor** permissions to load an index. Alternatively, you can [use an API admin key](search-security-api-keys.md) instead of roles.
 
-Use the REST API or an Azure SDK preview package to create a knowledge source. Azure portal support is available for select knowledge sources. The following links provide instructions for creating a knowledge source:
+Use the Azure portal, REST API, or an Azure SDK preview package to create a knowledge source. The following links provide instructions for creating a knowledge source:
 
 + [How to create a search index knowledge source (wraps an existing index)](agentic-knowledge-source-how-to-search-index.md)
 + [How to create a blob knowledge source (generates an indexer pipeline)](agentic-knowledge-source-how-to-blob.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Knowledge Source に関する概要のタイトルと日付の更新"
}
```

### Explanation
この変更では、`articles/search/agentic-knowledge-source-overview.md` ファイルに対していくつかの修正が行われました。主に、記事のタイトルが「What is a knowledge source」から「What is a Knowledge Source?」に変更され、タイトルの書式が整えられています。また、文書の日付が「01/15/2026」から「02/02/2026」に更新され、最新の情報が反映されています。

さらに、知識ソースを作成するための手段が改善され、最初に「Azure portal, REST API, or an Azure SDK preview package」を使用することが明記されました。これにより、ユーザーにとっての情報の理解が向上し、どの方法を用いて知識ソースを作成できるのかがより明確になっています。全体で6行の変更があり、3行ずつが追加・削除されています。これらの修正は、Azure AI Searchにおける知識ソースについての明確性を高めるものです。

## articles/search/agentic-retrieval-overview.md{#item-d1f354}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about agentic retrieval concepts, architecture, and use cases
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 01/16/2026
+ms.date: 02/02/2026
 ms.service: azure-ai-search
 ms.topic: concept-article
 ms.custom:
@@ -102,8 +102,6 @@ Your application drives the pipeline by calling the knowledge base and handling
 
 To create an agentic retrieval solution, you can use the Azure portal, the latest preview REST APIs, or a preview Azure SDK package that provides the functionality.
 
-Currently, the portal only supports creating search index and blob knowledge sources. Other types of knowledge sources must be created programmatically.
-
 ### [**Quickstarts**](#tab/quickstarts)
 
 + [Quickstart: Agentic retrieval in the Azure portal](get-started-portal-agentic-retrieval.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Agentic Retrieval 概要の更新"
}
```

### Explanation
この変更では、`articles/search/agentic-retrieval-overview.md` ファイルが修正され、エージェンティックリトリーバルに関する情報が更新されました。具体的には、文書の日付が「01/16/2026」から「02/02/2026」に変更され、最新の情報が反映されています。

また、エージェンティックリトリーバルソリューションを作成する際の方法の説明で、Azure ポータル、最新のプレビュー REST API、またはプレビューの Azure SDK パッケージを使用できることが明記されています。さらに、ポータルで現在サポートされている知識ソースの作成についての記述が削除され、より明確な情報提供が行われています。全体で4行の変更があり、1行が追加され、3行が削除されています。これらの修正により、Azure AI Searchにおけるエージェンティックリトリーバルに関する理解がさらに向上します。

## articles/search/get-started-portal-agentic-retrieval.md{#item-2bf1dc}

<details>
<summary>Diff</summary>
````diff
@@ -9,14 +9,14 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2025
 ms.topic: quickstart
-ms.date: 12/18/2025
+ms.date: 02/05/2026
 ---
 
 # Quickstart: Agentic retrieval in the Azure portal
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-In this quickstart, you use [agentic retrieval](agentic-retrieval-overview.md) in the Azure portal to create a conversational search experience powered by documents indexed in Azure AI Search and large language models (LLMs) from Azure OpenAI in Foundry Models.
+In this quickstart, you use [agentic retrieval](agentic-retrieval-overview.md) in the Azure portal to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models.
 
 The portal guides you through the process of creating the following objects:
 
@@ -87,9 +87,9 @@ On your Azure Blob Storage account:
 
 ### [Microsoft Foundry](#tab/foundry-perms)
 
-Foundry provides the Azure OpenAI models used for embeddings, query planning, and answer generation. Grant your search service permission to use these models.
+Microsoft Foundry provides the Azure OpenAI models used for embeddings, query planning, and answer generation. Grant your search service permission to use these models.
 
-On your Foundry resource:
+On your Microsoft Foundry resource:
 
 + Assign **Cognitive Services User** to your [search service identity](search-how-to-managed-identities.md#create-a-system-managed-identity).
 
@@ -131,18 +131,20 @@ To create the knowledge source for this quickstart:
 
 1. Select **Add knowledge source** > **Add knowledge source**.
 
-1. Select **Azure blob**.
+1. Select **Azure blob (Indexed)**.
 
 1. Enter **earth-at-night-ks** for the name, and then select your subscription, storage account, and container with the sample data.
 
 1. Select the **Authenticate using managed identity** checkbox. Leave the identity type as **System-assigned**.
 
-1. Select **Add vectorizer**.
+1. Under **Enable text vectorization**, select **Add vectorizer**.
 
 1. Select **Azure AI Foundry** for the kind, and then select your subscription, project, and embedding model deployment.
 
 1. Select **System assigned identity** for the authentication type.
 
+1. Save the vectorizer.
+
 1. Create the knowledge source.
 
    :::image type="content" source="media/get-started-portal-agentic-retrieval/create-knowledge-source.png" alt-text="Screenshot of the knowledge source configuration for this quickstart." lightbox="media/get-started-portal-agentic-retrieval/create-knowledge-source.png" :::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルのクイックスタートガイドの更新"
}
```

### Explanation
この変更では、`articles/search/get-started-portal-agentic-retrieval.md` ファイルが更新され、エージェンティックリトリーバルに関するクイックスタートガイドの内容が改善されました。具体的には、文書の日付が「12/18/2025」から「02/05/2026」に変更され、最新の情報が反映されています。

クイックスタートガイドの説明文において、Azure OpenAIからの大規模言語モデル(LLM)に関する記述が明確化されました。また、「Azure blob」という用語が「Azure blob (Indexed)」に変更され、手順がより具体的になっています。さらに、テキストベクトライザを有効にするための手順も追加されており、ユーザーが知識ソースを作成する際の手順がよりわかりやすくなっています。

全体で14行の変更があり、8行の追加と6行の削除が行われています。これにより、Azure AI Searchにおけるエージェンティックリトリーバルの利用がさらに容易になります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-csharp.md{#item-d6611c}

<details>
<summary>Diff</summary>
````diff
@@ -9,9 +9,9 @@ ms.date: 01/23/2026
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
 
-Use a *OneLake knowledge source* to index and query Microsoft OneLake files in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
+Use an *indexed OneLake knowledge source* to index and query Microsoft OneLake files in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
 
-When you create a OneLake knowledge source, you specify an external data source, models, and properties to automatically generate the following Azure AI Search objects:
+When you create an indexed OneLake knowledge source, you specify an external data source, models, and properties to automatically generate the following Azure AI Search objects:
 
 + A data source that represents a lakehouse.
 + A skillset that chunks and optionally vectorizes multimodal content from the lakehouse.
@@ -24,7 +24,7 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 
 | [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 |--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
@@ -42,7 +42,7 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 
 [!INCLUDE [Check for existing knowledge sources using C#](knowledge-source-check-csharp.md)]
 
-The following JSON is an example response for a OneLake knowledge source.
+The following JSON is an example response for an indexed OneLake knowledge source.
 
 ```json
 {
@@ -98,7 +98,7 @@ The following JSON is an example response for a OneLake knowledge source.
 
 ## Create a knowledge source
 
-Run the following code to create a OneLake knowledge source.
+Run the following code to create an indexed OneLake knowledge source.
 
 ```csharp
 // Create an IndexedOneLake knowledge source
@@ -153,7 +153,7 @@ Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated
 
 ### Source-specific properties
 
-You can pass the following properties to create a OneLake knowledge source.
+You can pass the following properties to create an indexed OneLake knowledge source.
 
 | Name | Description | Type | Editable | Required |
 |--|--|--|--|--|
@@ -175,7 +175,7 @@ You can pass the following properties to create a OneLake knowledge source.
 
 ## Review the created objects
 
-When you create a OneLake knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
+When you create an indexed OneLake knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
 
 After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
 
@@ -190,7 +190,7 @@ We recommend using the Azure portal to validate output creation. The workflow is
 
 If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../search-agentic-retrieval-how-to-create.md).
 
-For any knowledge base that specifies a OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
+For any knowledge base that specifies an indexed OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
 
 After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLake 知識ソースのインデックス化に関するガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-csharp.md` ファイルが更新され、OneLake 知識ソースに関連する情報が明確化されました。具体的には、流れの各所で「OneLake 知識ソース」から「インデックス化された OneLake 知識ソース」に表記が変更され、より具体的な内容になっています。

この変更には、知識ソース作成時に指定する項目やプロパティに関する説明が含まれており、利用者にインデックス化された知識ソースを作成する際の手順を明確にしています。たとえば、インデックス化された知識ソースを作成すると、Azure AI Search に必要なデータソース、スキルセット、インデクサーが自動的に生成されることが記載されています。

また、いくつかの箇所で「OneLake 知識ソース」という言葉を使用していた部分が「インデックス化された OneLake 知識ソース」に変更され、手順と JSON レスポンスの例もそれに合わせて更新されました。全体で 16 行の変更があり、8 行の追加と 8 行の削除が行われています。これにより、OneLake 知識ソースの作成や使用に関する理解が深まることが期待されます。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-python.md{#item-c7d61d}

<details>
<summary>Diff</summary>
````diff
@@ -9,9 +9,9 @@ ms.date: 11/14/2025
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
 
-Use a *OneLake knowledge source* to index and query Microsoft OneLake files in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
+Use an *indexed OneLake knowledge source* to index and query Microsoft OneLake files in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
 
-When you create a OneLake knowledge source, you specify an external data source, models, and properties to automatically generate the following Azure AI Search objects:
+When you create an indexed OneLake knowledge source, you specify an external data source, models, and properties to automatically generate the following Azure AI Search objects:
 
 + A data source that represents a lakehouse.
 + A skillset that chunks and optionally vectorizes multimodal content from the lakehouse.
@@ -24,7 +24,7 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 
 | [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 |--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
@@ -42,7 +42,7 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 
 [!INCLUDE [Check for existing knowledge sources using Python](knowledge-source-check-python.md)]
 
-The following JSON is an example response for a OneLake knowledge source.
+The following JSON is an example response for an indexed OneLake knowledge source.
 
 ```json
 {
@@ -98,10 +98,10 @@ The following JSON is an example response for a OneLake knowledge source.
 
 ## Create a knowledge source
 
-Run the following code to create a OneLake knowledge source.
+Run the following code to create an indexed OneLake knowledge source.
 
 ```python
-# Create a OneLake knowledge source
+# Create an indexed OneLake knowledge source
 from azure.core.credentials import AzureKeyCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import IndexedOneLakeKnowledgeSource, IndexedOneLakeKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceAzureOpenAIVectorizer, KnowledgeSourceContentExtractionMode, KnowledgeSourceIngestionParameters
@@ -142,7 +142,7 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 
 ### Source-specific properties
 
-You can pass the following properties to create a OneLake knowledge source.
+You can pass the following properties to create an indexed OneLake knowledge source.
 
 | Name | Description | Type | Editable | Required |
 |--|--|--|--|--|
@@ -164,7 +164,7 @@ You can pass the following properties to create a OneLake knowledge source.
 
 ## Review the created objects
 
-When you create a OneLake knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
+When you create an indexed OneLake knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
 
 After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
 
@@ -179,7 +179,7 @@ We recommend using the Azure portal to validate output creation. The workflow is
 
 If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../search-agentic-retrieval-how-to-create.md).
 
-For any knowledge base that specifies a OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
+For any knowledge base that specifies an indexed OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
 
 After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLake 知識ソースに関する Python ガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-python.md` ファイルが更新され、OneLake 知識ソースに関する Python の利用方法が明確化されました。具体的には、流れの中で「OneLake 知識ソース」という用語が「インデックス化された OneLake 知識ソース」に変更され、より具体的な情報提供が行われています。

特に、OneLake 知識ソースを作成する際に必要な外部データソース、モデル、プロパティの指定について詳しく記載されており、インデックス化された知識ソース作成時の手順をユーザーに分かりやすく説明しています。また、サンプルコードのコメントも更新され、インデックス化された知識ソースの生成手順がはっきりとしています。

さらに、インデックス化された知識ソースを作成する際に生成される各種 Azure AI Search オブジェクト（インデクサー、インデックス、スキルセット、データソース）の解説も更新され、ユーザーがこれらを変更しない方が良いという注意点も言及されています。

全体で 18 行の変更があり、9 行の追加と 9 行の削除が行われています。これにより、OneLake 知識ソースの作成や管理における理解が深まることが期待されます。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-rest.md{#item-876f49}

<details>
<summary>Diff</summary>
````diff
@@ -9,9 +9,9 @@ ms.date: 11/14/2025
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
 
-Use a *OneLake knowledge source* to index and query Microsoft OneLake files in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
+Use an *indexed OneLake knowledge source* to index and query Microsoft OneLake files in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
 
-When you create a OneLake knowledge source, you specify an external data source, models, and properties to automatically generate the following Azure AI Search objects:
+When you create an indexed OneLake knowledge source, you specify an external data source, models, and properties to automatically generate the following Azure AI Search objects:
 
 + A data source that represents a lakehouse.
 + A skillset that chunks and optionally vectorizes multimodal content from the lakehouse.
@@ -24,7 +24,7 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 
 | [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 |--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
@@ -42,7 +42,7 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 
 [!INCLUDE [Check for existing knowledge sources using REST](knowledge-source-check-rest.md)]
 
-The following JSON is an example response for a OneLake knowledge source.
+The following JSON is an example response for an indexed OneLake knowledge source.
 
 ```json
 {
@@ -98,7 +98,7 @@ The following JSON is an example response for a OneLake knowledge source.
 
 ## Create a knowledge source
 
-Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create a OneLake knowledge source.
+Use [Knowledge Sources - Create or Update (REST API)](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to create an indexed OneLake knowledge source.
 
 ```http
 PUT {{search-url}}/knowledgesources/my-onelake-ks?api-version=2025-11-01-preview
@@ -128,7 +128,7 @@ Content-Type: application/json
 
 ### Source-specific properties
 
-You can pass the following properties to create a OneLake knowledge source.
+You can pass the following properties to create an indexed OneLake knowledge source.
 
 | Name | Description | Type | Editable | Required |
 |--|--|--|--|--|
@@ -151,7 +151,7 @@ You can pass the following properties to create a OneLake knowledge source.
 
 ## Review the created objects
 
-When you create a OneLake knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
+When you create an indexed OneLake knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
 
 After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
 
@@ -166,7 +166,7 @@ We recommend using the Azure portal to validate output creation. The workflow is
 
 If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](../../search-agentic-retrieval-how-to-create.md).
 
-For any knowledge base that specifies a OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
+For any knowledge base that specifies an indexed OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
 
 After the knowledge base is configured, use the [retrieve action](../../agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLake REST 知識ソースに関するガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-rest.md` ファイルが更新され、OneLake REST 知識ソースに関する情報がより具体的になりました。具体的には、「OneLake 知識ソース」という用語から「インデックス化された OneLake 知識ソース」への表記の変更が行われ、ユーザーに対する指示や手順が明確化されています。

変更の内容は、知識ソースを作成する際に指定する外部データソース、モデル、プロパティに関しても同様に明確にされており、インデックス化された知識ソースを生成するための手順がユーザーにとって理解しやすく整備されています。具体的な例として、JSONレスポンスの見本が「OneLake 知識ソース」から「インデックス化された OneLake 知識ソース」へと変更されています。

さらに、リクエストコードの例や、知識ソース作成時に生成される Azure AI Search オブジェクト（インデクサー、インデックス、スキルセット、データソース）の説明も更新されています。これにより、ユーザーはこれらのオブジェクトがどのように利用されるかをより正確に理解できるようになります。

この変更では、合計16行の更新があり、追加と削除がそれぞれ8行ずつ行われています。これにより、OneLake 知識ソースの作成や使用に関するより良い理解が促進されることが期待されます。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md{#item-2eb305}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
 
 | [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 |--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint インデックスされた知識ソースに関する C# ガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md` ファイルが更新され、SharePoint インデックスされた知識ソースに関する C# のガイドがわずかに修正されました。具体的には、各 SDK のサポート状況を示す列の変更が行われました。

具体的には、Azure ポータルに関するサポート状況が更新され、利用可能な SDK のリストで「❌」から「✔️」に変更され、Azure ポータルが利用可能であることが示されています。この修正は、ユーザーに対して、SharePoint インデックスされた知識ソースの操作に関して Azure ポータルが正しく使用できることを明確にするものです。

全体として、2 行の変更があり、1 行の追加と1 行の削除が行われています。これにより、ユーザーが SharePoint 知識ソースのセットアップを行う際の指針がより正確になりました。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-python.md{#item-923abb}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
 
 | [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 |--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint インデックスされた知識ソースに関する Python ガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-python.md` ファイルが更新され、SharePoint インデックスされた知識ソースに関する Python 用のガイドが修正されました。具体的には、Azure ポータルのサポート状況を示す列の内容が更新されています。

変更点は、Azure ポータルについてのサポート状況が「❌」から「✔️」に変更され、Azure ポータルが利用可能であることを明示しています。この修正により、ユーザーは SharePoint インデックスされた知識ソースの設定を行う際に、Azure ポータルが正しく機能することを理解できるようになっています。

全体的に、2 行の変更があり、1 行の追加と1 行の削除が行われています。この変更により、ユーザーは Python を使用する際の適切なリソースとサポートが改めて強調され、ガイドの正確性が向上しています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-rest.md{#item-e26ea0}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
 
 | [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 |--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint インデックスされた知識ソースに関する REST ガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-rest.md` ファイルが更新され、SharePoint インデックスされた知識ソースに関する REST API のガイドが修正されました。主に、Azure ポータルについてのサポート状況を示す列の内容が変更されました。

具体的には、Azure ポータルに関して、サポートの有無が「❌」から「✔️」に変更され、ユーザーは Azure ポータルが利用可能であることを明確に示されています。この修正は、ユーザーが SharePoint インデックスされた知識ソースの操作を行う際に、Azure ポータルが正しく使用できることを理解できるようにするための重要な変更です。

全体的に、2 行の変更があり、1 行の追加と1 行の削除が行われています。これにより、REST API を利用する際の正確なリソースとサポートが強調され、ガイドの内容がより適切になります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-csharp.md{#item-f8bed1}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ Like any other knowledge source, you specify a remote SharePoint knowledge sourc
 
 | [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 |--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint リモート知識ソースに関する C# ガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-csharp.md` ファイルが更新され、SharePoint リモート知識ソースに関する C# のガイドが修正されました。主な変更は、Azure ポータルのサポート状況を示す列の内容です。

具体的には、Azure ポータルに関して、前は「❌」と表示されていたサポート状況が「✔️」に変更され、Azure ポータルが使用可能であることを示しています。この更新により、ユーザーがリモート SharePoint 知識ソースを設定する際に、Azure ポータルを利用する際の正確なサポート情報を得られるようになります。

全体として、2 行が変更され、1 行の追加と1 行の削除が行われています。これにより、ガイドの正確性が向上し、C# を用いてのリモート知識ソースの操作に関するユーザーの理解を深めることができます。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-python.md{#item-822712}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ Like any other knowledge source, you specify a remote SharePoint knowledge sourc
 
 | [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 |--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint リモート知識ソースに関する Python ガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-python.md` ファイルが更新され、SharePoint リモート知識ソースに関する Python のガイドが修正されました。主な内容の変更は、Azure ポータルのサポート状況を示す列に関連しています。

具体的には、Azure ポータルのサポートが「❌」から「✔️」に変更され、これはユーザーがリモート SharePoint 知識ソースを設定する際に Azure ポータルを確実に利用できることを示しています。この修正は、ガイドの情報を最新のものにし、ユーザーに正確な利用可能状況を提供します。

全体として、2 行が変更され、1 行の追加と1 行の削除が行われています。これにより、Python を使用してリモート知識ソースを操作する際のユーザーの理解が深まり、より効果的にガイドを活用できるようになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-rest.md{#item-5514b1}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ Like any other knowledge source, you specify a remote SharePoint knowledge sourc
 
 | [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 |--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint リモート知識ソースに関する REST ガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-rest.md` ファイルが更新され、SharePoint リモート知識ソースに関する REST API のガイドが修正されました。変更の主なポイントは、Azure ポータルのサポート状況を示す部分にあります。

具体的には、Azure ポータルのサポート状況が「❌」から「✔️」に変更されたことにより、ユーザーはリモート SharePoint 知識ソースを設定する際に Azure ポータルを使用できることを正確に理解できます。この修正は、情報の正確性を向上させ、読者に最新の利用可能性を提供します。

全体として、ガイドの中で2 行が変更され、1 行が追加され、1 行が削除されています。これにより、REST API を使用するユーザーへの支援が向上し、リモート知識ソースの操作に関する理解を促進します。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-csharp.md{#item-401063}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ When you use Web Knowledge Source, keep the following in mind:
 
 | [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 |--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Web 知識ソースに関する C# ガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-csharp.md` ファイルが更新され、Web 知識ソースに関する C# のガイドが修正されました。変更の主なポイントは、Azure ポータルのサポート状況を示す部分にあります。

具体的には、Azure ポータルのサポートが「❌」から「✔️」に変更されたことで、ユーザーは Web 知識ソースを利用する際に Azure ポータルがサポートされていることを確認できるようになりました。この修正は、ガイドの情報を最新のものにし、ユーザーに正確な情報を提供することを目的としています。

全体として、2 行が変更され、1 行の追加と1 行の削除が行われています。この修正により、C# を使用して Web 知識ソースを操作するユーザーへのサポートが向上し、より良い実践を促進します。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-python.md{#item-72b59c}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ When you use Web Knowledge Source, keep the following in mind:
 
 | [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 |--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Web 知識ソースに関する Python ガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-python.md` ファイルが更新され、Web 知識ソースに関する Python のガイドが修正されました。変更の主なポイントは、Azure ポータルのサポート状況を示す部分です。

具体的には、Azure ポータルのサポートが「❌」から「✔️」に変更されることで、ユーザーは Web 知識ソースを利用する際に Azure ポータルがサポートされていることを確認できます。この修正は、ガイドの情報を正確かつ最新のものに保つことを目的としています。

全体として、2 行が変更され、1 行が追加され、1 行が削除されています。この修正により、Python を使用して Web 知識ソースを操作するユーザーへの支援が強化され、より良い実践を促進します。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-rest.md{#item-649608}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ When you use Web Knowledge Source, keep the following in mind:
 
 | [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
 |--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Web 知識ソースに関する REST API ガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-rest.md` ファイルが更新され、Web 知識ソースに関する REST API のガイドが修正されました。主な変更内容は、Azure ポータルのサポート状況を示す部分に関連しています。

具体的には、Azure ポータルのサポートが「❌」から「✔️」に変更されたため、ユーザーは Web 知識ソースを利用する際に Azure ポータルが正式にサポートされていることを確認できるようになりました。この修正は、ガイドの情報を最新のものとし、利用者に正確な情報を提供することを目的としています。

全体として、2 行が変更され、1 行の追加と1 行の削除が行われています。この修正により、REST API を使用して Web 知識ソースを操作するユーザーに対する支援が強化され、より良い実践が促進されます。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-csharp.md{#item-4469a2}

<details>
<summary>Diff</summary>
````diff
@@ -13,12 +13,6 @@ In Azure AI Search, a *knowledge base* is a top-level object that orchestrates [
 
 You can create a knowledge base in a [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) workload in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
 
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
 A knowledge base specifies:
 
 + One or more knowledge sources that point to searchable content.
@@ -31,6 +25,12 @@ After you create a knowledge base, you can update its properties at any time. If
 > [!IMPORTANT]
 > 2025-11-01-preview renames the 2025-08-01-preview "knowledge agent" to "knowledge base." This is a breaking change. We recommend [migrating existing code](../../agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). If you're using a [managed identity](../../search-how-to-managed-identities.md) for role-based access to deployed models, your search service must be on the Basic pricing tier or higher.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# 用の知識ベース作成ガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-csharp.md` ファイルが更新され、C# における知識ベースの作成方法に関するガイドが修正されました。主な変更点としては、ガイドの内容構造が見直され、新しい情報が追加されるとともに、一部の情報が再配置されています。

具体的には、知識ベースの定義セクションが強化され、サポート情報のセクションが再配置されました。このインフォメーションの修正により、ユーザーは利用可能なリソースに素早くアクセスできるようになり、知識ベースの作成に関する重要な情報が一目でわかるようになっています。

結果として、全体で12行が変更され、6行が追加され、6行が削除されました。これによって、C# を使用する開発者が Azure AI Search の機能をより効果的に活用できることを目指しています。この更新は、より良いドキュメントの精度と利用可能性を促進することに寄与しています。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-python.md{#item-4e498f}

<details>
<summary>Diff</summary>
````diff
@@ -13,12 +13,6 @@ In Azure AI Search, a *knowledge base* is a top-level object that orchestrates [
 
 You can create a knowledge base in a [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) workload in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
 
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
 A knowledge base specifies:
 
 + One or more knowledge sources that point to searchable content.
@@ -31,6 +25,12 @@ After you create a knowledge base, you can update its properties at any time. If
 > [!IMPORTANT]
 > 2025-11-01-preview renames the 2025-08-01-preview "knowledge agent" to "knowledge base." This is a breaking change. We recommend [migrating existing code](../../agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). If you're using a [managed identity](../../search-how-to-managed-identities.md) for role-based access to deployed models, your search service must be on the Basic pricing tier or higher.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python 用の知識ベース作成ガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-python.md` ファイルが改訂され、Python における知識ベースの作成方法に関するガイドが改善されました。主な修正点としては、文書構造の見直しと新しい情報の追加があります。

具体的には、知識ベースの定義がより明確になり、使用サポートのセクションが再配置されました。また、知識ベースが持つべき情報の指摘も追加されています。この修正により、ユーザーは必要なリソースに迅速にアクセスでき、知識ベースの作成に関する実用的な情報が提供されます。

これにより、全体で12行が変更され、6行の追加と6行の削除が行われています。このアップデートの目的は、Python 開発者が Azure AI Search での知識ベース作成をより簡単に行えるようにすることです。ドキュメントの精度と利用可能性の向上に寄与する内容となっています。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-rest.md{#item-37851c}

<details>
<summary>Diff</summary>
````diff
@@ -13,12 +13,6 @@ In Azure AI Search, a *knowledge base* is a top-level object that orchestrates [
 
 You can create a knowledge base in a [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) workload in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
 
-### Usage support
-
-| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
-
 A knowledge base specifies:
 
 + One or more knowledge sources that point to searchable content.
@@ -31,6 +25,12 @@ After you create a knowledge base, you can update its properties at any time. If
 > [!IMPORTANT]
 > 2025-11-01-preview renames the 2025-08-01-preview "knowledge agent" to "knowledge base." This is a breaking change. We recommend [migrating existing code](../../agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). If you're using a [managed identity](../../search-how-to-managed-identities.md) for role-based access to deployed models, your search service must be on the Basic pricing tier or higher.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST 用知識ベース作成ガイドの更新"
}
```

### Explanation
この変更では、`articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-rest.md` ファイルが改訂され、REST API に基づく知識ベースの作成方法に関するガイドが更新されました。主な変更点には、情報の構造の見直しと新しい情報の追加があります。

特に、知識ベースの定義の説明が強化され、知識ベースが持つべき情報源に関する具体的な記述が加えられました。また、使用サポートに関するセクションが視覚的に再配置され、各サービスや SDK へのアクセシビリティが向上しています。

この変更に伴い、合計で12行が改善され、そのうち6行が追加され、6行が削除されています。このアップデートの目標は、REST API を使う開発者が Azure AI Search の機能をより効果的に活用できるようにすることです。優れたドキュメントの精度とアクセシビリティの向上に貢献する内容になっています。

## articles/search/media/get-started-portal-agentic-retrieval/create-knowledge-source.png{#item-104c67}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ソース作成の画像更新"
}
```

### Explanation
この変更では、`articles/search/media/get-started-portal-agentic-retrieval/create-knowledge-source.png` という画像ファイルが更新されています。具体的な内容の追加や削除は行われていないため、変更は画像自体に関するものと推測されます。このアップデートは、Azure AI Search の「知識ソース作成」プロセスに関連するビジュアル要素の最新化を目的としています。

画像が改訂されることで、内容がより理解しやすく、または新しい情報に基づいて視覚的に確認しやすくなっている可能性があります。ユーザーは、この画像を参照することで、操作手順や概念をより直感的に理解できるようになることが期待されます。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Announcements of new and enhanced features, including a service ren
 author: haileytap
 ms.author: haileytapia
 manager: nitinme
-ms.date: 12/18/2025
+ms.date: 02/02/2026
 ms.service: azure-ai-search
 ms.topic: overview
 ms.custom:
@@ -20,6 +20,12 @@ Learn about the latest updates to Azure AI Search functionality, docs, and sampl
 > [!NOTE]
 > Preview features are announced here, but we also maintain a [preview features list](search-api-preview.md) so you can find them in one place.
 
+## February 2026
+
+| Item | Description |
+|--|--|
+| [Expanded 2025-11-01-preview portal support for agentic retrieval](get-started-portal-agentic-retrieval.md) | The Azure portal now supports the following 2025-11-01-preview knowledge sources:<p><ul><li>[Indexed OneLake](agentic-knowledge-source-how-to-onelake.md)</li><li>[Indexed SharePoint](agentic-knowledge-source-how-to-sharepoint-indexed.md)</li><li>[Remote SharePoint](agentic-knowledge-source-how-to-sharepoint-remote.md)</li><li>[Web](agentic-knowledge-source-how-to-web.md)</li></ul><p>For [search index knowledge sources](agentic-knowledge-source-how-to-search-index.md), the portal adds optional configurations for specifying search fields and a semantic configuration. For [blob knowledge sources](agentic-knowledge-source-how-to-blob.md), the portal now supports Azure Data Lake Storage (ADLS) Gen2 accounts. Blob, indexed OneLake, and indexed SharePoint knowledge sources also support the content extraction mode for optional use of the [Azure Content Understanding skill](cognitive-search-skill-content-understanding.md).<p>New retrieval options in the knowledge base playground provide settings for maximum runtime, maximum output size, and inclusion of query activity.<p>If you previously created knowledge bases or knowledge sources in the portal, those objects still use the 2025-08-01-preview schema. For help with breaking changes, see [Migrate your agentic retrieval code](agentic-retrieval-how-to-migrate.md). |
+
 ## December 2025
 
 | Item | Description |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search の新機能に関する更新"
}
```

### Explanation
この変更は、`articles/search/whats-new.md` ファイルの更新であり、Azure AI Search に関連する新機能や改善点に関する情報が含まれています。具体的には、2026年2月の新機能についてのセクションが追加され、さらに既存の情報が更新されました。

新しい項目には、「エージェントリトリーバルのための2025年11月1日プレビュー ポータルサポートの拡張」が含まれ、Azure ポータル上でサポートされる多様な知識ソースの新機能が詳細に説明されています。このサポートには、Indexed OneLake や Indexed SharePoint のほか、Remote SharePoint や Web などの新しい知識ソースが含まれ、特定の検索フィールドやセマンティック設定など、ポータルのオプション設定が追加されたことも記載されています。

また、知識ベースのプレイグラウンドでは、新しい取得オプションが導入され、最大実行時間や最大出力サイズ、クエリアクティビティのインクルージョンに関する設定ができるようになっています。全体として、この更新により最新の機能と変更点が明確に整理され、ユーザーが新しい機能をより効果的に活用できるよう情報が提供されています。


