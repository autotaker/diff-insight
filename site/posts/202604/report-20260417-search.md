---
date: '2026-04-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4e14138...MicrosoftDocs:3c4ffb2
summary: |-
  以下は、主要な変更点の概要です。

  SharePointとエージェンティックリトリーバルに関するドキュメントが更新され、新しいパフォーマンス最適化戦略や設定方法の具体例が追加されました。また、各ドキュメントには「AI支援」タグが付けられ、更新日も修正されています。リージョンの検索に関する情報も明確化されました。特に破壊的な変更はありませんが、文書内容は精緻化され、ユーザーエクスペリエンスの向上が図られています。これにより、ユーザーはドキュメントをより効果的に利用できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4e14138...MicrosoftDocs:3c4ffb2){target="_blank"}

# Highlights
以下は主要な変更点の概要です:
- SharePointとエージェンティックリトリーバル関連のドキュメントの更新が実施されました。
- 新しいパフォーマンス最適化戦略や設定の具体例が追加されました。
- 新しいタグ「AI支援」が各ドキュメントに追加され、更新日が修正されました。
- リージョンの検索サポートに関わる情報も明確化されました。

## New features
- エージェンティックリトリーバルのドキュメントに「AI支援」タグの追加。
- 新しい戦略と設定方法の具体例が追加。
- トラブルシューティングセクションの追加。

## Breaking changes
- 特に破壊的な変更は含まれませんが、誤解を避けるためにドキュメントの内容が精緻化されました。

## Other updates
- ドキュメントの日付が修正されました。

# Insights
この差分分析は、SharePointとエージェンティックリトリーバルに関するドキュメントがどのように更新されたかを詳しく説明します。主要な変更点は、情報の明確化を目的としており、特にユーザーエクスペリエンスを向上させています。

まず、SharePoint関連のドキュメントでは、インデックス作成の手順がより理解しやすく調整されています。リンク先やリンクの表示が更新され、特にAzure AI Searchのための管理されたIDの関連情報が強調されました。このような更新は、設定を行う際のつまずきを減らし、ユーザーが手順をスムーズに実行するのを助けます。

次に、エージェンティックリトリーバル関連の資料では、パフォーマンス最適化と遅延の低減に関する新しい戦略が詳述されています。出力サイズや実行時間の上限がどのように設定されるかなど、実例を挙げて説明しているため、ユーザーは設定項目の具体的な役割と影響を理解しやすくなっています。また、トラブルシューティングセクションが追加され、検索時に発生し得る問題点とその対応策が提示されています。これによりトラブルの早期発見と解決が可能になり、ユーザーは知識ベースをより効率的に活用できます。

最後に、検索リージョンサポートの記事では、特定のリージョンでの新しい検索サービス作成とスケーリングの制限について、記載内容が改善されました。これにより、ユーザーは各地域での能力の制限をよりよく理解でき、最適な戦略を選択することができます。

以上のアップデートは、全体としてドキュメントの質を向上させ、ユーザーが情報を効果的に利用できるようにするための重要なステップです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-sharepoint-indexed.md](#item-fe72fc) | minor update | SharePoint インデクサーの手順の更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | エージェンティックリトリーバルパイプライン作成チュートリアルの更新 | modified | 4 | 1 | 5 | 
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | minor update | エージェンティックリトリーバル取得方法の更新 | modified | 11 | 2 | 13 | 
| [search-how-to-index-sharepoint-online.md](#item-8c099c) | minor update | SharePoint Onlineインデクサーの設定方法の更新 | modified | 43 | 46 | 89 | 
| [search-region-support.md](#item-25b0f1) | minor update | 検索リージョンサポートに関する情報の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-sharepoint-indexed.md{#item-fe72fc}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
 
 + Completion of the following SharePoint indexer configuration steps:
 
-  + [Step 1: Enable a managed identity for Azure AI Search](search-how-to-index-sharepoint-online.md#step-1-optional-enable-system-assigned-managed-identity) (required only for secretless authentication; skip if using a client secret)
+  + [Step 1: Enable a managed identity for Azure AI Search](search-how-to-index-sharepoint-online.md#optional-step-1-enable-a-system-assigned-managed-identity) (required only for secretless authentication; skip if using a client secret)
   + [Step 2: Choose either delegated or application permissions](search-how-to-index-sharepoint-online.md#step-2-decide-which-permissions-the-indexer-requires)
   + [Step 3: Create a Microsoft Entra application registration](search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration) (for application permissions, you also configure a [client secret](search-how-to-index-sharepoint-online.md#using-client-secret) or [secretless authentication](search-how-to-index-sharepoint-online.md#using-secretless-authentication-to-obtain-application-tokens))
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint インデクサーの手順の更新"
}
```

### Explanation
この変更は、SharePoint 知識ソースのインデックス作成に関するドキュメントの手順に対する小さな更新です。具体的には、「ステップ 1: Azure AI Search のための管理された ID を有効にする」というリンクのテキストが微調整され、リンク先が「optional-step-1-enable-a-system-assigned-managed-identity」という変更後の形式に適応されています。この更新は、読者がより明確に手順を理解できるようにするためのものであり、ドキュメント全体の有用性を向上させることを目的としています。

## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,12 @@
 ---
 title: 'Tutorial: Build an Agentic Retrieval Solution'
 description: Build an agentic retrieval solution that connects Azure AI Search to Foundry Agent Service via MCP. Follow this tutorial to create a knowledge base and agent.
-ms.date: 04/01/2026
+ms.date: 04/15/2026
 ms.service: azure-ai-search
 ms.topic: tutorial
 ms.custom:
   - build-2025
+ai-usage: ai-assisted
 ---
 
 # Tutorial: Build an end-to-end agentic retrieval solution using Azure AI Search
@@ -595,6 +596,8 @@ To optimize performance and reduce latency, consider the following strategies:
 
 + Set `maxOutputSize` on the [retrieve action](agentic-retrieval-how-to-retrieve.md) to govern the size of the response or `maxRuntimeInSeconds` for time-bound processing.
 
++ Chunk large documents into smaller pieces before indexing. Documents that exceed the output budget can be [silently omitted from grounded results](agentic-retrieval-how-to-retrieve.md#troubleshoot-empty-responses).
+
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルパイプライン作成チュートリアルの更新"
}
```

### Explanation
この変更は、「エージェンティックリトリーバルソリューションの構築」に関するチュートリアルの内容を更新したものです。具体的には、最終更新日が「2026年4月1日」から「2026年4月15日」に変更され、ドキュメントに新たに「AI支援」というタグが追加されました。また、パフォーマンスの最適化とレイテンシの低減に関するセクションに新しい戦略が追加され、特に「retrieve action」に関する `maxOutputSize` および `maxRuntimeInSeconds` の設定方法が明記されました。さらに、大きなドキュメントをインデックス作成前に小さな部分に分割することが推奨され、関連するコンテンツへのリンクも追加されました。これにより、ユーザーがエージェンティックリトリーバルの効果的な活用をより理解できるようになっています。

## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Query Knowledge Base via APIs or MCP
 description: Learn how to Query a knowledge base using the retrieve action or MCP endpoint in Azure AI Search using REST APIs, Azure SDKs, or any MCP-compatible client.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/17/2026
+ms.date: 04/15/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
@@ -437,7 +437,10 @@ Key points:
 
 + In this preview, `content.type` has one valid value: `text`.
 
-+ The `maxOutputSize` property on the [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) determines the length of the string.
++ The `maxOutputSize` property on the knowledge base determines the length of the string.
+
+    > [!IMPORTANT]
+    > A document that exceeds the `maxOutputSize` output budget can be silently omitted from the response without a warning. For more information, see [Troubleshoot empty responses](#troubleshoot-empty-responses).
 
 ### Activity array
 
@@ -817,6 +820,12 @@ Content-Type: application/json
 
 :::zone-end
 
+## Troubleshoot empty responses
+
+A document can be found during the search step but still be omitted from the final response if its grounded content exceeds the `maxOutputSize` output budget. When this happens, the activity array shows that matches were found, but the references array and grounded response content are empty for that document. No truncation warning or explicit error is returned.
+
+To avoid this behavior, index large source documents as smaller chunks with stable identifiers and source metadata. This applies especially to long manuals, policies, or knowledge base articles.
+
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバル取得方法の更新"
}
```

### Explanation
この変更は、「エージェンティックリトリーバルを使用して知識ベースをクエリする方法」に関するドキュメントを更新したものです。最初に、最終更新日が「2026年3月17日」から「2026年4月15日」に変更され、新たに「AI支援」というタグが追加されました。ドキュメントの中では、`maxOutputSize` プロパティに関する重要な注意事項が加わり、出力予算を超えるドキュメントが応答から静かに省略される可能性があることが明記されました。ユーザーがトラブルシューティングのための新しいセクションも追加され、検索ステップで見つかった文書が最終的な応答から省略される可能性について説明しています。特に、大きなソースドキュメントを安定した識別子とメタデータを持つ小さなチャンクとしてインデックス作成することが推奨されています。この改訂により、ユーザーが知識ベースを効果的に活用できるような情報が提供されています。

## articles/search/search-how-to-index-sharepoint-online.md{#item-8c099c}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Set up a SharePoint in Microsoft 365 indexer to automate indexing o
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/24/2026
+ms.date: 04/16/2026
 ms.custom:
   - ignite-2025
   - sfi-image-nochange
@@ -14,13 +14,13 @@ ms.custom:
 # Index data from SharePoint document libraries
 
 > [!IMPORTANT]
-> SharePoint in Microsoft 365 indexer support is in public preview. It's offered "as-is", under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) and supported on best effort only. Preview features aren't recommended for production workloads and aren't guaranteed to become generally available.
+> The SharePoint in Microsoft 365 indexer is in public preview. It's offered "as-is" under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) and supported on a best-effort basis only. Preview features aren't recommended for production workloads and aren't guaranteed to become generally available.
 >
-> See [known limitations](#limitations-and-considerations) section before you start.
+> Before you proceed, review the [known limitations](#limitations-and-considerations).
 >
 > [Fill out this form](https://aka.ms/azure-cognitive-search/indexer-preview) to register for the preview. All requests are approved automatically. After you fill out the form, use a [preview REST API](search-api-preview.md) to index your content. 
 
-This article explains how to configure a [search indexer](search-indexer-overview.md) to index documents stored in SharePoint document libraries for full text search in Azure AI Search. Configuration steps are first, followed by behaviors and scenarios.
+This article explains how to configure a [search indexer](search-indexer-overview.md) to index documents stored in SharePoint document libraries for full-text search in Azure AI Search. The configuration steps are first, followed by behaviors and scenarios.
 
 In Azure AI Search, an indexer extracts searchable data and metadata from a data source. The SharePoint in Microsoft 365 indexer provides the following functionality:
 
@@ -51,7 +51,7 @@ The SharePoint in Microsoft 365 indexer can extract text from the following docu
 
 Here are the limitations of this feature:
 
-+ The indexer can index content from supported document formats in a document library. There's no indexer support for [SharePoint Lists](https://support.microsoft.com/office/introduction-to-lists-0a1c3ace-def0-44af-b225-cfa8d92c52d7), .ASPX site content, or OneNote notebook files. Furthermore, indexing sub-sites recursively from a specific site isn't supported.
++ The indexer can index content from supported document formats in a document library. There's no indexer support for [SharePoint lists](https://support.microsoft.com/office/introduction-to-lists-0a1c3ace-def0-44af-b225-cfa8d92c52d7), .ASPX site content, or OneNote notebook files. Furthermore, indexing sub-sites recursively from a specific site isn't supported.
 
 + Incremental indexing limitations:
 
@@ -61,42 +61,39 @@ Here are the limitations of this feature:
 
 + Security limitations:
 
-  + No support for [Private endpoint](search-indexer-howto-access-private.md). Secure network configuration must be enabled [via a firewall](service-configure-firewall.md).
+  + No support for [private endpoints](search-indexer-howto-access-private.md). Secure network configuration must be enabled [via a firewall](service-configure-firewall.md).
 
   + No support for tenants with [Microsoft Entra ID Conditional Access](/entra/identity/conditional-access/overview) enabled.
     
-  +  User-encrypted files and password-protected ZIP files aren't supported. However, encrypted content is allowed if it's protected by [Purview sensitivity labels](/purview/sensitivity-labels) and if the [configuration to preserve and honor those labels (preview)](search-indexer-sensitivity-labels.md) is enabled.
-
-  + Limited support for document-level access permissions. A basic level of ACL sync is currently in public preview. Review the [SharePoint ACL configuration documentation](search-indexer-sharepoint-access-control-lists.md) for details and setup.
+  +  No support for user-encrypted files and password-protected ZIP files. However, encrypted content is allowed if it's protected by [Microsoft Purview sensitivity labels](/purview/sensitivity-labels) and if the [configuration to preserve and honor those labels (preview)](search-indexer-sensitivity-labels.md) is enabled.
 
+  + Limited support for document-level access permissions. A basic level of ACL sync is currently in public preview. For details and setup, see the [SharePoint ACL configuration documentation](search-indexer-sharepoint-access-control-lists.md).
 
 Here are some considerations when using this feature:
 
-+ To build a custom Copilot or Retrieval-Augmented Generation (RAG) app that interacts with SharePoint data using Azure AI Search, Microsoft recommends using the [SharePoint (Remote) Knowledge Source](agentic-knowledge-source-how-to-sharepoint-remote.md). This knowledge source uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) to query textual content directly from SharePoint in Microsoft 365, returning results to the agentic retrieval engine for merging, ranking, and response formulation. There's no search index used by this knowledge source, and only textual content is queried. Azure AI Search doesn't replicate data. It enforces the SharePoint permission model by returning only the results that each user is authorized to see.
-
-+ If you need to create a custom Copilot / RAG (Retrieval Augmented Generation) application or AI agent to chat with SharePoint data in production environments, consider first building it directly via [Microsoft Copilot Studio](/microsoft-copilot-studio/knowledge-add-sharepoint).
++ To build a custom Copilot or retrieval-augmented generation (RAG) app that interacts with SharePoint data using Azure AI Search, Microsoft recommends using the [remote SharePoint knowledge source](agentic-knowledge-source-how-to-sharepoint-remote.md). This knowledge source uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) to query textual content directly from SharePoint in Microsoft 365, returning results to the agentic retrieval engine for merging, ranking, and response formulation. There's no search index used by this knowledge source, and only textual content is queried. Azure AI Search doesn't replicate data. It enforces the SharePoint permission model by returning only the results that each user is authorized to see.
 
-+ If you still need a custom copilot / RAG application or agent indexing data from SharePoint in Azure AI Search in a production environment, despite the recommendation to use Copilot Studio, consider:
++ If you need to create a custom Copilot/RAG application or AI agent to chat with SharePoint data in production environments, consider first building it directly via [Microsoft Copilot Studio](/microsoft-copilot-studio/knowledge-add-sharepoint). If Copilot Studio doesn't meet your needs, consider:
 
-  + Creating a custom connector with [SharePoint Webhooks](/sharepoint/dev/apis/webhooks/overview-sharepoint-webhooks), calling [Microsoft Graph API](/graph/use-the-api) to export the data to an Azure Blob container, and then use the [Azure blob indexer](search-how-to-index-azure-blob-storage.md) for incremental indexing.
+  + Creating a custom connector with [SharePoint webhooks](/sharepoint/dev/apis/webhooks/overview-sharepoint-webhooks), calling the [Microsoft Graph API](/graph/use-the-api) to export data to an Azure Blob container, and then using the [Azure blob indexer](search-how-to-index-azure-blob-storage.md) for incremental indexing.
 
-  + Creating your own [Azure Logic Apps workflow](/azure/logic-apps/logic-apps-overview) using [Azure Logic Apps SharePoint connector](/connectors/sharepointonline/) and [Azure AI Search connector](/connectors/azureaisearch/) when reaching General Availability. You can use the workflow generated by the [Azure portal wizard](search-how-to-index-logic-apps.md) as a starting point and then customize it in the [Azure Logic Apps designer](/azure/logic-apps/quickstart-create-example-consumption-workflow#add-the-trigger) to include the transformation steps you need. The Azure Logic App workflow created when using the [Azure AI Search wizard](search-how-to-index-logic-apps.md) to index SharePoint in Microsoft 365 data is a [consumption workflow](/azure/logic-apps/logic-apps-overview#key-terms). When setting up production workloads, switch to a [standard logic app workflow](/azure/logic-apps/logic-apps-overview#key-terms) to use its extra enterprise features.
+  + Creating your own [Azure Logic Apps workflow](/azure/logic-apps/logic-apps-overview) using the [Azure Logic Apps SharePoint connector](/connectors/sharepointonline/) and [Azure AI Search connector](/connectors/azureaisearch/) when reaching general availability. You can use the workflow generated by the [Azure portal wizard](search-how-to-index-logic-apps.md) as a starting point and then customize it in the [Azure Logic Apps designer](/azure/logic-apps/quickstart-create-example-consumption-workflow#add-the-trigger) to include the transformation steps you need. The Azure Logic App workflow created when using the [Azure AI Search wizard](search-how-to-index-logic-apps.md) to index SharePoint in Microsoft 365 data is a [consumption workflow](/azure/logic-apps/logic-apps-overview#key-terms). When setting up production workloads, switch to a [standard logic app workflow](/azure/logic-apps/logic-apps-overview#key-terms) to use its extra enterprise features.
   
-Regardless of the approach you choose, whether building a custom connector with SharePoint hooks or creating an Azure Logic Apps workflow, be sure to implement robust security measures. These measures include configuring shared private links, setting up firewalls, preserving user permissions from the source and honor those permissions at query time, among others. You should also regularly audit and monitor your pipeline.
+Regardless of the approach you choose, whether building a custom connector with SharePoint webhooks or creating an Azure Logic Apps workflow, be sure to implement robust security measures. These measures include configuring shared private links, setting up firewalls, and preserving user permissions from the source and honoring those permissions at query time. You should also regularly audit and monitor your pipeline.
 
 ## Configure the SharePoint in Microsoft 365 indexer
 
 To set up the SharePoint in Microsoft 365 indexer, use a preview REST API. This section provides the steps. 
 
-### Step 1 (Optional): Enable system assigned managed identity
+### (Optional) Step 1: Enable a system-assigned managed identity
 
 Enable a [system-assigned managed identity](search-how-to-managed-identities.md#create-a-system-managed-identity) to automatically detect the tenant in which the search service is provisioned. 
 
-Perform this step if the SharePoint site is in the same tenant as the search service. Skip this step if the SharePoint site is in a different tenant. The identity is used for tenant detection. You can also skip this step if you want to put the tenant ID in the [connection string](#connection-string-format). If you would like to use the system-managed identity or configure a user-assigned managed identity for secretless indexing, configure the [application permissions with secretless authentication](#using-secretless-authentication-to-obtain-application-tokens)
+Perform this step if the SharePoint site is in the same tenant as the search service. Skip this step if the SharePoint site is in a different tenant. The identity is used for tenant detection. You can also skip this step if you want to put the tenant ID in the [connection string](#connection-string-format). If you want to use the system-assigned managed identity or configure a user-assigned managed identity for secretless indexing, configure the [application permissions with secretless authentication](#using-secretless-authentication-to-obtain-application-tokens).
 
 :::image type="content" source="media/search-howto-index-sharepoint-online/enable-managed-identity.png" alt-text="Screenshot showing how to enable system assigned managed identity.":::
 
-After selecting **Save**, you receive an Object ID assigned to your search service.
+After selecting **Save**, you receive an object ID assigned to your search service.
 
 <!-- Replace this with a new image without GUID
 :::image type="content" source="media/search-howto-index-sharepoint-online/system-assigned-managed-identity.png" alt-text="Screenshot the object identifier."::: -->
@@ -105,11 +102,11 @@ After selecting **Save**, you receive an Object ID assigned to your search servi
 
 The SharePoint in Microsoft 365 indexer supports both [delegated and application](/graph/auth/auth-concepts#delegated-and-application-permissions) permissions. Choose which permissions you want to use based on your scenario.
 
-We recommend app-based permissions. See [limitations](#limitations-and-considerations) for known issues related to delegated permissions.
+We recommend app-based permissions. For known issues related to delegated permissions, see [Limitations and considerations](#limitations-and-considerations).
 
 + Application permissions (recommended), where the indexer runs under the [identity of the SharePoint tenant](/sharepoint/dev/solution-guidance/security-apponly-azureacs) with access to all sites and files. The indexer requires a [client secret](/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow). The indexer also requires [tenant admin approval](/azure/active-directory/manage-apps/grant-admin-consent) before it can index content. This permission type is the only one that supports basic [ACL preservation (preview)](search-indexer-sharepoint-access-control-lists.md) configuration. Delegated permissions can't be used for ACL sync.
 
-+ Delegated permissions, where the indexer runs under the identity of the user or app sending the request. Data access is limited to the sites and files to which the caller has access. To support delegated permissions, the indexer requires a [device code prompt](/azure/active-directory/develop/v2-oauth2-device-code) to sign in on behalf of the user. User-delegated permissions enforce token expiration every 75 minutes, per the most recent security libraries used to implement this authentication type. This isn't a behavior that can be adjusted. An expired token requires manual indexing using [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2025-11-01-preview&tabs=HTTP&preserve-view=true). For this reason, you should use app-based permissions instead. This configuration is only recommended for small testing operations, due to token expiration period and since this permission type doesn't support any level of [ACL preservation](search-indexer-sharepoint-access-control-lists.md) configuration.
++ Delegated permissions, where the indexer runs under the identity of the user or app sending the request. Data access is limited to the sites and files to which the caller has access. To support delegated permissions, the indexer requires a [device code prompt](/azure/active-directory/develop/v2-oauth2-device-code) to sign in on behalf of the user. User-delegated permissions enforce token expiration every 75 minutes, per the most recent security libraries used to implement this authentication type. This behavior can't be adjusted. An expired token requires manual indexing using [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2025-11-01-preview&tabs=HTTP&preserve-view=true). For this reason, you should use app-based permissions instead. This configuration is only recommended for small testing operations, due to token expiration period and since this permission type doesn't support any level of [ACL preservation](search-indexer-sharepoint-access-control-lists.md) configuration.
 
 <a name='step-3-create-an-azure-ad-application'></a>
 
@@ -119,10 +116,10 @@ The SharePoint in Microsoft 365 indexer uses a Microsoft Entra application for a
 
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
-1. Search for or navigate to **Microsoft Entra ID**, then select **Add** > **App registrations**. 
+1. Search for or navigate to **Microsoft Entra ID**, then select **Add** > **App registration**. 
 
 1. Select **+ New registration**:
-    1. Provide a name for your app.
+    1. Enter a name for your app.
     1. Select **Single tenant**.
     1. Skip the URI designation step. No redirect URI required.
     1. Select **Register**.
@@ -165,7 +162,7 @@ The SharePoint in Microsoft 365 indexer uses a Microsoft Entra application for a
 
 1. Select the **Authentication** tab.
 
-1. Set **Allow public client flows** to **Yes** then select **Save**.
+1. Set **Allow public client flows** to **Yes**, then select **Save**.
 
 1. Select **+ Add a platform**, then **Mobile and desktop applications**, then check `https://login.microsoftonline.com/common/oauth2/nativeclient`, then **Configure**.
 
@@ -221,7 +218,7 @@ These are the instructions to configure the application so Microsoft Entra trust
     <!-- GIA TO ADD THIS SCREENSHOT OF UAMI SELECTION --> 
     <!-- GIA TO ADD THIS SCREENSHOT OF SAMI SELECTION -->
 
-1. Add a name for your credential and click on **Save**.
+1. Add a name for your credential and select **Save**.
 
 <a name="create-data-source"></a>
 
@@ -290,15 +287,14 @@ The format of the connection string changes based on whether the indexer is usin
 
     `SharePointOnlineEndpoint=[SharePoint site url];ApplicationId=[Azure AD App ID];FederatedCredentialObjectId=[selected managed identity object (principal) ID];TenantId=[SharePoint site tenant id]`
 
-You can get `tenantId` from the overview page in the Microsoft Entra admin center in your Microsoft 365 subscription.
-You can get the managed identity `object (principal) ID` from the section [Configuring the registered application with a managed identity](#configuring-the-registered-application-with-a-managed-identity)
+You can get `tenantId` from the **Overview** page in the Microsoft Entra admin center in your Microsoft 365 subscription.
+
+You can get the managed identity `object (principal) ID` from the [Configuring the registered application with a managed identity](#configuring-the-registered-application-with-a-managed-identity) section.
 
 > [!NOTE]
 > If the SharePoint site is in the same tenant as the search service and system-assigned managed identity is enabled, `TenantId` doesn't have to be included in the connection string. If the SharePoint site is in a different tenant from the search service, `TenantId` must be included.
->
-
-If your indexer uses [SharePoint ACL configuration (preview)](search-indexer-sharepoint-access-control-lists.md) or [preserves and honors Microsoft Purview sensitivity labels (preview)](search-indexer-sensitivity-labels.md), review the related articles for data source setup before creating the indexer. Each feature has specific configuration steps.
 
+If your indexer uses [SharePoint ACL configuration (preview)](search-indexer-sharepoint-access-control-lists.md) or [preserves and honors Microsoft Purview sensitivity labels (preview)](search-indexer-sensitivity-labels.md), review the related articles for data source configuration before you create the indexer. Each feature has specific configuration steps.
 
 ### Step 5: Create an index
 
@@ -329,15 +325,15 @@ api-key: [admin key]
 > [!IMPORTANT]
 > Only [`metadata_spo_site_library_item_id`](#metadata) may be used as the key field in an index populated by the SharePoint in Microsoft 365 indexer. If a key field doesn't exist in the data source, `metadata_spo_site_library_item_id` is automatically mapped to the key field.
 
-If your indexer will use either [SharePoint ACL configuration (preview)](search-indexer-sharepoint-access-control-lists.md) or will [preserve and honor Microsoft Purview sensitivity labels (preview)](search-indexer-sensitivity-labels.md), review each article for index and skillset configuration before proceeding with indexer creation since those functionalities have specific configurations.
+If your indexer uses [SharePoint ACL configuration (preview)](search-indexer-sharepoint-access-control-lists.md) or [preserves and honors Microsoft Purview sensitivity labels (preview)](search-indexer-sensitivity-labels.md), review the related articles for index and skillset configuration before you create the indexer. Each feature has specific configuration steps.
 
 ### Step 6: Create an indexer
 
-An indexer connects a data source with a target search index and provides a schedule to automate the data refresh. Once the index and data source are created, you can create the indexer.
+An indexer connects a data source with a target search index and provides a schedule to automate the data refresh. After the data source and index are created, you can create the indexer.
 
 If you're using delegated permissions, during this step, you're asked to sign in with organization credentials that have access to the SharePoint site. If possible, we recommend creating a new organizational user account and giving that new user the exact permissions that you want the indexer to have. 
 
-There are a few steps to creating the indexer:
+To create the indexer:
 
 1. Send a [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-11-01-preview&tabs=HTTP&preserve-view=true) request:
 
@@ -374,7 +370,7 @@ There are a few steps to creating the indexer:
     }
     ```
 
-    If you're using application permissions, it's necessary to wait until the initial run is complete before starting to query your index. The following instructions provided in this step pertain specifically to delegated permissions, and aren't applicable to application permissions.
+    If you're using application permissions, you must wait until the initial run is complete before you start to query your index. The instructions provided in this step apply only to delegated permissions, not application permissions.
 
 1. When you create the indexer for the first time, the [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-11-01-preview&tabs=HTTP&preserve-view=true) request waits until you complete the next step. You must call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-11-01-preview&tabs=HTTP&preserve-view=true) to get the link and enter your new device code. 
 
@@ -397,7 +393,7 @@ There are a few steps to creating the indexer:
     }
     ```
 
-1. Provide the code that was included in the error message.
+1. Enter the code that was included in the error message.
 
     :::image type="content" source="media/search-howto-index-sharepoint-online/enter-device-code.png" alt-text="Screenshot showing how to enter a device code.":::
 
@@ -409,11 +405,12 @@ There are a few steps to creating the indexer:
 
     :::image type="content" source="media/search-howto-index-sharepoint-online/aad-app-approve-api-permissions.png" alt-text="Screenshot showing how to approve API permissions.":::
 
-1. The [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-11-01-preview&tabs=HTTP&preserve-view=true) initial request completes if all the permissions provided above are correct and within the 10 minute timeframe.
+1. The [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-11-01-preview&tabs=HTTP&preserve-view=true) initial request completes if all the permissions provided above are correct and within the 10-minute timeframe.
 
 > [!NOTE]
-> If the Microsoft Entra application requires admin approval and was not approved before logging in, you may see the following screen. [Admin approval](/azure/active-directory/manage-apps/grant-admin-consent) is required to continue.
-:::image type="content" source="media/search-howto-index-sharepoint-online/no-admin-approval-error.png" alt-text="Screenshot showing admin approval required.":::
+> If the Microsoft Entra application requires admin approval and wasn't approved before logging in, you might see the following screen. [Admin approval](/azure/active-directory/manage-apps/grant-admin-consent) is required to continue.
+>
+> :::image type="content" source="media/search-howto-index-sharepoint-online/no-admin-approval-error.png" alt-text="Screenshot showing admin approval required.":::
 
 ### Step 7: Check the indexer status
 
@@ -475,7 +472,7 @@ If you're indexing document metadata (`"dataToExtract": "contentAndMetadata"`),
 | metadata_spo_item_weburi | Edm.String | The URI of the item. |
 | metadata_spo_item_path | Edm.String | The combination of the parent path and item name. | 
 
-The SharePoint in Microsoft 365 indexer also supports metadata specific to each document type. More information can be found in [Content metadata properties used in Azure AI Search](search-blob-metadata-properties.md).
+The SharePoint in Microsoft 365 indexer also supports metadata specific to each document type. For more information, see [Content metadata properties used in Azure AI Search](search-blob-metadata-properties.md).
 
 > [!NOTE]
 > To index custom metadata, "additionalColumns" must be specified in the [query parameter of the data source](#query).
@@ -513,14 +510,14 @@ The "name" property is required and must be one of three values:
 | Value | Description |
 |-|-|
 | defaultSiteLibrary | Index all content from the site's default document library. |
-| allSiteLibraries | Index all content from all document libraries in a site. Document libraries from a subsite are out of scope/ If you need content from subsites, choose "useQuery" and specify "includeLibrariesInSite". |
+| allSiteLibraries | Index all content from all document libraries in a site. Document libraries from a subsite are out of scope. If you need content from subsites, choose "useQuery" and specify "includeLibrariesInSite". |
 | useQuery | Only index the content defined in the "query". |
 
 <a name="query"></a>
 
 ### Query
 
-The "query" parameter of the data source is made up of keyword/value pairs. The below are the keywords that can be used. The values are either site URLs or document library URLs.
+The "query" parameter of the data source is made up of keyword/value pairs. The following keywords can be used. The values are either site URLs or document library URLs.
 
 > [!NOTE]
 > To get the value for a particular keyword, we recommend navigating to the document library that you're trying to include/exclude and copying the URI from the browser. This is the easiest way to get the value to use with a keyword in the query.
@@ -535,7 +532,7 @@ The "query" parameter of the data source is made up of keyword/value pairs. The
 
 ## Handling errors
 
-By default, the SharePoint in Microsoft 365 indexer stops as soon as it encounters a document with an unsupported content type (for example, an image). You can use the `excludedFileNameExtensions` parameter to skip certain content types. However, you might need to index documents without knowing all the possible content types in advance. To continue indexing when an unsupported content type is encountered, set the `failOnUnsupportedContentType` configuration parameter to false:
+By default, the SharePoint in Microsoft 365 indexer stops as soon as it encounters a document with an unsupported content type, such as an image. You can use the `excludedFileNameExtensions` parameter to skip certain content types. However, you might need to index documents without knowing all the possible content types in advance. To continue indexing when an unsupported content type is encountered, set the `failOnUnsupportedContentType` configuration parameter to false:
 
 ```http
 PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2025-11-01-preview
@@ -548,13 +545,13 @@ api-key: [admin key]
 }
 ```
 
-For some documents, Azure AI Search is unable to determine the content type, or unable to process a document of otherwise supported content type. To ignore this failure mode, set the `failOnUnprocessableDocument` configuration parameter to false:
+For some documents, Azure AI Search is unable to determine the content type or unable to process a document of an otherwise supported content type. To ignore this failure mode, set the `failOnUnprocessableDocument` configuration parameter to false:
 
 ```http
 "parameters" : { "configuration" : { "failOnUnprocessableDocument" : false } }
 ```
 
-Azure AI Search limits the size of documents that are indexed. These limits are documented in [Service Limits in Azure AI Search](./search-limits-quotas-capacity.md). Oversized documents are treated as errors by default. However, you can still index storage metadata of oversized documents if you set `indexStorageMetadataOnlyForOversizedDocuments` configuration parameter to true:
+Azure AI Search limits the size of documents that are indexed. These limits are documented in [Service Limits in Azure AI Search](./search-limits-quotas-capacity.md). Oversized documents are treated as errors by default. However, you can still index storage metadata of oversized documents if you set the `indexStorageMetadataOnlyForOversizedDocuments` configuration parameter to true:
 
 ```http
 "parameters" : { "configuration" : { "indexStorageMetadataOnlyForOversizedDocuments" : true } }
@@ -575,9 +572,9 @@ If a file on the SharePoint site has encryption enabled, you might see the follo
 Code: resourceModified Message: The resource has changed since the caller last read it; usually an eTag mismatch Inner error: Code: irmEncryptFailedToFindProtector
 ```
 
-The error message will also include the SharePoint site ID, drive ID, and drive item ID in the following pattern: `<sharepoint site id> :: <drive id> :: <drive item id>`. This information can be used to identify which item is failing on the SharePoint end. The user can then remove the encryption from the item to resolve the issue.
+The error message also includes the SharePoint site ID, drive ID, and drive item ID in the following pattern: `<sharepoint site id> :: <drive id> :: <drive item id>`. Use this information to identify which item is failing on the SharePoint end. The user can then remove the encryption from the item to resolve the issue.
 
-## See also
+## Related content
 
 + [YouTube video: SharePoint in Microsoft 365 indexer](https://www.youtube.com/watch?v=QmG65Vgl0JI)
 + [Indexers in Azure AI Search](search-indexer-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint Onlineインデクサーの設定方法の更新"
}
```

### Explanation
この変更は、「SharePoint Onlineのデータをインデックスする方法」に関する記事の改訂です。最終更新日が「2026年3月24日」から「2026年4月16日」に変更され、インデクサーの説明がより明確になりました。不具合を示す警告や注意事項が再構成され、新たに重要なポイントが追加されています。また、設定手順の表現が一貫性を持たせるために修正されました。

具体的には、SharePoint in Microsoft 365インデクサーに関する情報が更新され、ユーザーが知っておくべき制限事項や考慮事項についての警告文が追加されています。さらに、記事の構成が整えられ、特に "クエリ" パラメータやインデックス作成手順に関する説明が改善されています。これにより、ユーザーがよりスムーズにSharePointからデータをインデックスできるようになります。この改訂は、特にユーザーがドキュメントやコンテンツを効果的に管理・検索するために役立つ情報を提供しています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -47,15 +47,15 @@ You can create an Azure AI Search service in any of the following Azure public r
 | East US 2 <sup>1, 2</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Mexico Central |  | ✅ |  |  |  |  |
 | North Central US​ <sup>1</sup> ​| ✅ |  | ✅ |  | ✅ | ✅ |
-| South Central US​ <sup>1, 2</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| South Central US​ <sup>1 </sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | West US​​ <sup>1, 2</sup> | ✅ |  | ✅ |  | ✅ | ✅ |
 | West US 2​ <sup>3</sup> ​| ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | West US 3​ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | West Central US​ ​<sup>1</sup>| ✅ |  | ✅ |  | ✅ |  |
 
 <sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
-<sup>2</sup> This region is experiencing capacity constraints that prevent the creation of new search services. Please choose a different region.
+<sup>2</sup> This region is experiencing capacity constraints that prevent the creation of new search services and scaling operations. Please choose a different region.
 
 <sup>3</sup> This region doesn't have indexer support for [Microsoft Purview sensitivity labels](search-indexer-sensitivity-labels.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索リージョンサポートに関する情報の更新"
}
```

### Explanation
この変更は、「検索リージョンサポート」に関する文書の一部を修正したものです。具体的には、特定のリージョンに関連する注意書きが改善され、容量制約がある地域における新しい検索サービスの作成やスケーリング操作の制限についての情報が明確になりました。以前は「新しい検索サービスの作成を妨げる」と記載されていましたが、変更後は「新しい検索サービスの作成とスケーリング操作を妨げる」と具体的になっています。この改訂により、ユーザーは各リージョンの能力の制限についての理解が深まり、最適な選択をする手助けとなります。


