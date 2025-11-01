---
date: '2025-11-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:84a7ec4...MicrosoftDocs:fc84978
summary: この変更は、ドキュメントにおける「SharePoint Online」から「Microsoft 365のSharePoint」への名称変更を中心に行われました。これにより、Azure
  AI Searchのインデクサーに関する説明が明確になり、一貫性が向上します。また、ガイドラインの明確化とプレビュー機能の利用に関する注意点の強調も含まれています。特に新機能や破壊的変更はありませんが、名称変更によってユーザーの認識が改善され、より良いユーザー体験が期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:84a7ec4...MicrosoftDocs:fc84978){target="_blank"}

<format>
# ハイライト
この変更は、ドキュメントにおける「SharePoint Online」から「Microsoft 365のSharePoint」への名称変更を中心とした内容の更新を含んでいます。このアップデートは、Azure AI Searchのインデクサーに関する説明をより明確にし、一貫性を持たせるためのものです。また、ガイドラインの明確化とプレビュー機能の利用に関する注意点の強調も行われています。

## 新機能
特記すべき新機能の追加はありません。

## 破壊的変更
破壊的変更は特にありません。主に名称変更および内容の更新が中心です。

## その他の更新
- 「SharePoint Onlineインデクサー」から「Microsoft 365のSharePointインデクサー」への名称変更。
- ガイドラインの明確化とプレビュー機能利用に関する注意点の強調。

# インサイト
この更新は、Microsoftの製品名称ポリシーに準拠するための重要な調整です。「SharePoint Online」という用語が「Microsoft 365のSharePoint」に変更されることにより、Azure AI Searchを利用する際のドキュメントの一貫性と明確さが向上します。名称の変更により、ユーザーは現在のMicrosoftの製品命名規則に基づいたサービスを利用していると認識しやすくなります。

さらに、プレビュー機能の利用に関する注意点が強調されており、これはユーザーが新しい機能を試す際に注意すべきポイントを明示的に理解できるようにするための意図があります。このようなガイドラインの明確化は、誤解を避け、ユーザーが正しくサービスを利用するための助けとなるでしょう。

合計36行にわたる変更は、ドキュメント内容の整合性を増すためのものであり、ユーザー体験を向上させることが期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-how-to-index-sharepoint-online.md](#item-8c099c) | minor update | SharePointインデクサーの名称変更と内容の更新 | modified | 18 | 18 | 36 | 


# Modified Contents
## articles/search/search-how-to-index-sharepoint-online.md{#item-8c099c}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,12 @@
 ---
-title: SharePoint Online indexer (preview)
+title: SharePoint in Microsoft 365 indexer (preview)
 titleSuffix: Azure AI Search
-description: Set up a SharePoint Online indexer to automate indexing of document library content in Azure AI Search.
+description: Set up a SharePoint in Microsoft 365 indexer to automate indexing of document library content in Azure AI Search.
 author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 09/12/2025
+ms.date: 10/30/2025
 ms.custom:
   - ignite-2023
   - sfi-image-nochange
@@ -16,15 +16,15 @@ ms.custom:
 # Index data from SharePoint document libraries
 
 > [!IMPORTANT]
-> SharePoint Online indexer support is in public preview. It's offered "as-is", under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) and supported on best effort only. Preview features aren't recommended for production workloads and aren't guaranteed to become generally available.
+> SharePoint in Microsoft 365 indexer support is in public preview. It's offered "as-is", under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) and supported on best effort only. Preview features aren't recommended for production workloads and aren't guaranteed to become generally available.
 >
 > See [known limitations](#limitations-and-considerations) section before you start.
 >
 > [Fill out this form](https://aka.ms/azure-cognitive-search/indexer-preview) to register for the preview. All requests are approved automatically. After you fill out the form, use a [preview REST API](search-api-preview.md) to index your content. 
 
 This article explains how to configure a [search indexer](search-indexer-overview.md) to index documents stored in SharePoint document libraries for full text search in Azure AI Search. Configuration steps are first, followed by behaviors and scenarios.
 
-In Azure AI Search, an indexer extracts searchable data and metadata from a data source. The SharePoint Online indexer provides the following functionality:
+In Azure AI Search, an indexer extracts searchable data and metadata from a data source. The SharePoint in Microsoft 365 indexer provides the following functionality:
 
 + Indexes files and metadata from one or more document libraries.
 + Indexes incrementally, picking up just the new and changed files and metadata. 
@@ -43,7 +43,7 @@ In Azure AI Search, an indexer extracts searchable data and metadata from a data
 
 ## Supported document formats
 
-The SharePoint Online indexer can extract text from the following document formats:
+The SharePoint in Microsoft 365 indexer can extract text from the following document formats:
 
 [!INCLUDE [search-document-data-sources](./includes/search-blob-data-sources.md)]
 
@@ -73,17 +73,17 @@ Here are some considerations when using this feature:
 
 + If you need to create a custom Copilot or RAG (Retrieval Augmented Generation) application to chat with SharePoint data, Microsoft recommends using [Microsoft Copilot Studio](https://www.microsoft.com/microsoft-copilot/microsoft-copilot-studio) instead of this preview feature. 
 
-+ If you still need a custom SharePoint Online content indexing solution using Azure AI Search in a production environment, despite the recommendation to use Microsoft Copilot Studio, consider:
++ If you still need a custom SharePoint in Microsoft 365 content indexing solution using Azure AI Search in a production environment, despite the recommendation to use Microsoft Copilot Studio, consider:
 
   + Creating a custom connector with [SharePoint Webhooks](/sharepoint/dev/apis/webhooks/overview-sharepoint-webhooks), calling [Microsoft Graph API](/graph/use-the-api) to export the data to an Azure Blob container, and then use the [Azure blob indexer](search-how-to-index-azure-blob-storage.md) for incremental indexing.
 
-  + Creating your own [Azure Logic Apps workflow](/azure/logic-apps/logic-apps-overview) using [Azure Logic Apps SharePoint connector](/connectors/sharepointonline/) and [Azure AI Search connector](/connectors/azureaisearch/) when reaching General Availability. You can use the workflow generated by the [Azure portal wizard](search-how-to-index-logic-apps.md) as a starting point and then customize it in the [Azure Logic Apps designer](/azure/logic-apps/quickstart-create-example-consumption-workflow#add-the-trigger) to include the transformation steps you need. The Azure Logic App workflow created when using the [Azure AI Search wizard](search-how-to-index-logic-apps.md) to index SharePoint Online data is a [consumption workflow](/azure/logic-apps/logic-apps-overview#key-terms). If you're setting up production workloads, make sure to switch to a [standard logic app workflow](/azure/logic-apps/logic-apps-overview#key-terms) and take advantage of its additional enterprise features.
+  + Creating your own [Azure Logic Apps workflow](/azure/logic-apps/logic-apps-overview) using [Azure Logic Apps SharePoint connector](/connectors/sharepointonline/) and [Azure AI Search connector](/connectors/azureaisearch/) when reaching General Availability. You can use the workflow generated by the [Azure portal wizard](search-how-to-index-logic-apps.md) as a starting point and then customize it in the [Azure Logic Apps designer](/azure/logic-apps/quickstart-create-example-consumption-workflow#add-the-trigger) to include the transformation steps you need. The Azure Logic App workflow created when using the [Azure AI Search wizard](search-how-to-index-logic-apps.md) to index SharePoint in Microsoft 365 data is a [consumption workflow](/azure/logic-apps/logic-apps-overview#key-terms). If you're setting up production workloads, make sure to switch to a [standard logic app workflow](/azure/logic-apps/logic-apps-overview#key-terms) and take advantage of its additional enterprise features.
   
   Regardless of the approach you choose, whether building a custom connector with SharePoint hooks or creating an Azure Logic Apps workflow, be sure to implement robust security measures. These measures include configuring shared private links, setting up firewalls, preserving user permissions from the source and honor those permissions at query time, among others. You should also regularly audit and monitor your pipeline.
 
-## Configure the SharePoint Online indexer
+## Configure the SharePoint in Microsoft 365 indexer
 
-To set up the SharePoint Online indexer, use a preview REST API. This section provides the steps. 
+To set up the SharePoint in Microsoft 365 indexer, use a preview REST API. This section provides the steps. 
 
 ### Step 1 (Optional): Enable system assigned managed identity
 
@@ -99,7 +99,7 @@ After selecting **Save**, you get an Object ID that has been assigned to your se
 
 ### Step 2: Decide which permissions the indexer requires
 
-The SharePoint Online indexer supports both [delegated and application](/graph/auth/auth-concepts#delegated-and-application-permissions) permissions. Choose which permissions you want to use based on your scenario.
+The SharePoint in Microsoft 365 indexer supports both [delegated and application](/graph/auth/auth-concepts#delegated-and-application-permissions) permissions. Choose which permissions you want to use based on your scenario.
 
 We recommend app-based permissions. See [limitations](#limitations-and-considerations) for known issues related to delegated permissions.
 
@@ -111,7 +111,7 @@ We recommend app-based permissions. See [limitations](#limitations-and-considera
 
 ### Step 3: Create a Microsoft Entra application registration
 
-The SharePoint Online indexer uses a Microsoft Entra application for authentication. Create the application registration in the same tenant as Azure AI Search.
+The SharePoint in Microsoft 365 indexer uses a Microsoft Entra application for authentication. Create the application registration in the same tenant as Azure AI Search.
 
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
@@ -244,7 +244,7 @@ api-key: [admin key]
 ```
 
 > [!IMPORTANT]
-> Only [`metadata_spo_site_library_item_id`](#metadata) may be used as the key field in an index populated by the SharePoint Online indexer. If a key field doesn't exist in the data source, `metadata_spo_site_library_item_id` is automatically mapped to the key field.
+> Only [`metadata_spo_site_library_item_id`](#metadata) may be used as the key field in an index populated by the SharePoint in Microsoft 365 indexer. If a key field doesn't exist in the data source, `metadata_spo_site_library_item_id` is automatically mapped to the key field.
 
 ### Step 6: Create an indexer
 
@@ -316,7 +316,7 @@ There are a few steps to creating the indexer:
 
     :::image type="content" source="media/search-howto-index-sharepoint-online/enter-device-code.png" alt-text="Screenshot showing how to enter a device code.":::
 
-1. The SharePoint Online indexer will access the SharePoint content as the signed-in user. The user that logs in during this step will be that signed-in user. So, if you sign in with a user account that doesn’t have access to a document in the Document Library that you want to index, the indexer won’t have access to that document.
+1. The SharePoint in Microsoft 365 indexer will access the SharePoint content as the signed-in user. The user that logs in during this step will be that signed-in user. So, if you sign in with a user account that doesn’t have access to a document in the Document Library that you want to index, the indexer won’t have access to that document.
 
     If possible, we recommend creating a new user account and giving that new user the exact permissions that you want the indexer to have.
 
@@ -390,7 +390,7 @@ If you're indexing document metadata (`"dataToExtract": "contentAndMetadata"`),
 | metadata_spo_item_weburi | Edm.String | The URI of the item. |
 | metadata_spo_item_path | Edm.String | The combination of the parent path and item name. | 
 
-The SharePoint Online indexer also supports metadata specific to each document type. More information can be found in [Content metadata properties used in Azure AI Search](search-blob-metadata-properties.md).
+The SharePoint in Microsoft 365 indexer also supports metadata specific to each document type. More information can be found in [Content metadata properties used in Azure AI Search](search-blob-metadata-properties.md).
 
 > [!NOTE]
 > To index custom metadata, "additionalColumns" must be specified in the [query parameter of the data source](#query).
@@ -417,7 +417,7 @@ PUT /indexers/[indexer name]?api-version=2025-08-01-preview
 
 ## Controlling which documents are indexed
 
-A single SharePoint Online indexer can index content from one or more document libraries. Use the "container" parameter on the data source definition to indicate which sites and document libraries to index from.
+A single SharePoint in Microsoft 365 indexer can index content from one or more document libraries. Use the "container" parameter on the data source definition to indicate which sites and document libraries to index from.
 
 The [data source "container" section](#create-data-source) has two properties for this task: "name" and "query".
 
@@ -450,7 +450,7 @@ The "query" parameter of the data source is made up of keyword/value pairs. The
 
 ## Handling errors
 
-By default, the SharePoint Online indexer stops as soon as it encounters a document with an unsupported content type (for example, an image). You can use the `excludedFileNameExtensions` parameter to skip certain content types. However, you might need to index documents without knowing all the possible content types in advance. To continue indexing when an unsupported content type is encountered, set the `failOnUnsupportedContentType` configuration parameter to false:
+By default, the SharePoint in Microsoft 365 indexer stops as soon as it encounters a document with an unsupported content type (for example, an image). You can use the `excludedFileNameExtensions` parameter to skip certain content types. However, you might need to index documents without knowing all the possible content types in advance. To continue indexing when an unsupported content type is encountered, set the `failOnUnsupportedContentType` configuration parameter to false:
 
 ```http
 PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2025-08-01-preview
@@ -494,7 +494,7 @@ The error message will also include the SharePoint site ID, drive ID, and drive
 
 ## See also
 
-+ [YouTube video: SharePoint Online indexer](https://www.youtube.com/watch?v=QmG65Vgl0JI)
++ [YouTube video: SharePoint in Microsoft 365 indexer](https://www.youtube.com/watch?v=QmG65Vgl0JI)
 + [Indexers in Azure AI Search](search-indexer-overview.md)
 + [Content metadata properties used in Azure AI Search](search-blob-metadata-properties.md)
 + [Index SharePoint Online content and other sources in Azure AI Search using Azure Logic App connectors](search-how-to-index-logic-apps.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointインデクサーの名称変更と内容の更新"
}
```

### Explanation
この変更では、ドキュメントのタイトルや説明などに関連する用語の一部が更新され、特に「SharePoint Online」から「Microsoft 365のSharePoint」への名称変更が行われました。この修正は、Azure AI Searchにおけるインデクサーの機能に対する説明をより明確にし、一貫性を持たせるためのものです。具体的には、段落内の「SharePoint Onlineインデクサー」という表現が全て「Microsoft 365のSharePointインデクサー」に変更されています。

また、日付の更新や利用ガイドラインの明確化も行われており、特にプレビュー機能の利用に関する注意点が強調されています。これにより、ユーザーがAzure AI Searchを使用してSharePointからのデータインデックス作成を行う際の理解を促進し、全体的な文書の関連性を高めることを目的としています。

この修正は18行の追加と18行の削除を伴い、文書の内容に新たに適用された変更が36行にわたって行われました。


