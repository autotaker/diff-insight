---
date: '2026-05-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ee819cc...MicrosoftDocs:c2a4792
summary: |-
  この報告書では、OneLakeとSharePoint Onlineに関するいくつかの重要な変更点が紹介されています。

  新機能としては、OneLakeが明確化された制限事項と推奨事項を追加し、SharePoint Onlineには新しいパラメータ「includeFolder」と「excludeFolder」が導入されました。これにより、特定のフォルダーのコンテンツを選択的に取り込むことが可能になります。

  破壊的変更については特に挙げられていませんが、既存機能に影響を与える可能性があるため、読者は留意すべきです。

  その他の更新として、記事の日付が更新されました。

  全体として、これらのアップデートはインデックス作成プロセスにおけるユーザーの操作性を向上させることを目的としていますが、実際に適用する際には組織のデータ構造やセキュリティポリシーへの影響を十分に考慮する必要があります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ee819cc...MicrosoftDocs:c2a4792){target="_blank"}

<format>
# Highlights

## New features
- **OneLake Articles:** 明確化された制限事項と推奨事項の追加
- **SharePoint Online Articles:** 新しいパラメータ「includeFolder」と「excludeFolder」の導入

## Breaking changes
- 特に挙げられていませんが、機能拡張に伴う既存機能の影響について読者が留意すべき点はあります。

## Other updates
- 記事の日付の更新

# Insights

この記事の更新は、ユーザーが直面するであろうインデックス作成プロセスに関する課題を解決するための詳細情報を提供しようとするものです。まず、OneLakeに関しては、インデックス作成の制限事項と推奨事項に上記の変更が加えられました。特にMicrosoft Purviewのセンシティビティラベルに関連する内容がより詳細に説明されています。これはセキュリティやデータ保護に関心のあるユーザーにとって重要であり、この新しい情報は、インデクサーを使用した際の失敗を防ぐ手助けをします。

一方で、SharePoint Onlineのインデックス作成においても新しいパラメータの導入により、より細かい制御が可能になりました。「includeFolder」と「excludeFolder」のパラメータが新たに追加され、これによりユーザーは特定のフォルダーのコンテンツのみを取り込む、または除外することができます。このような細かい制御オプションは、特定のデータセットに基づいたカスタマイズされたインデックス作成に大いに役立ちます。

これらのアップデートは、インデックス作成の過程における柔軟性の向上と、ユーザーにとっての操作性の向上を狙っています。ただし、これらの新しい機能が組織全体のデータ構造やセキュリティポリシーにどのように影響を与えるか、実際の適用に当たっては十分な検討が必要です。特に組織のデータガバナンスポリシーと整合させる際に、影響度を評価するための時間を確保することをおすすめします。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-how-to-index-onelake-files.md](#item-95f3db) | minor update | OneLakeファイルのインデックス作成に関する記事の更新 | modified | 2 | 4 | 6 | 
| [search-how-to-index-sharepoint-online.md](#item-8c099c) | minor update | SharePoint Onlineインデックス作成に関する記事の更新 | modified | 3 | 11 | 14 | 


# Modified Contents
## articles/search/search-how-to-index-onelake-files.md{#item-95f3db}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Set up a OneLake indexer to automate indexing of content and metada
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 02/17/2026
+ms.date: 04/23/2026
 ms.custom:
   - build-2024
   - ignite-2024
@@ -58,9 +58,7 @@ This article uses the REST APIs to illustrate each step.
 
 + There's no support to ingest files from **My Workspace** workspace in OneLake since this is a personal repository per user.
 
-+ Microsoft Purview sensitivity labels [applied to Fabric items](/fabric/fundamentals/apply-sensitivity-labels) (such as lakehouses) will cause the indexer to fail if the search service doesn't have the required access. To prevent this behavior, you must either:
-    - Add the AI Search service’s Service Principal Name (SPN) to an existing organization group that grants access under the sensitivity label policy, or
-    - Request an exception from your organization’s IT team responsible for Purview sensitivity label policy configurations, and have them add the SPN directly to the policy.
++ Indexing files from [Fabric items with sensitivity labels](/fabric/fundamentals/apply-sensitivity-labels), for example, lakehouses, isn't supported. However, when sensitivity labels are applied directly to individual documents, ingestion of protected content and associated labels is supported. In these cases, Azure AI Search can extract and honor sensitivity labels and labeled documents' content through its [integration with Purview](search-indexer-sensitivity-labels.md). 
   
 + Workspace role-based permissions in Microsoft OneLake may affect indexer access to files. Ensure that the Azure AI Search service principal (managed identity) has sufficient permissions over the files you intend to access in the target [Microsoft Fabric workspace](/fabric/fundamentals/workspaces). 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLakeファイルのインデックス作成に関する記事の更新"
}
```

### Explanation
このコードの変更は、「OneLakeファイルのインデックス作成に関する記事」の内容を更新することを目的としています。主な改良点は、記事の日付の更新と、新しい情報の追加に関連しています。具体的には、インデックス作成に関する制限事項や推奨事項が明確化されました。特に、Microsoft Purviewのセンシティビティラベルが適用されたファブリックアイテムのインデクサーの失敗に関する説明がより詳細になり、個別文書に適用されたセンシティビティラベルを通じたコンテンツの取り込みがサポートされることが強調されています。また、Microsoft OneLakeのワークスペースにおける役割ベースの権限がインデクサーのファイルアクセスに影響を与える可能性があることも強調され、ユーザーが必要な権限を確保する必要性が指摘されています。これにより、ユーザーはインデクサーの使用に際してより効果的なガイダンスを得ることができます。

## articles/search/search-how-to-index-sharepoint-online.md{#item-8c099c}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Set up a SharePoint in Microsoft 365 indexer to automate indexing o
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 04/20/2026
+ms.date: 04/23/2026
 ms.custom:
   - ignite-2025
   - sfi-image-nochange
@@ -199,25 +199,15 @@ These are the instructions to configure the application so Microsoft Entra trust
 1. Create (or select) a [user-assigned managed identity and assign to your search service](search-how-to-managed-identities.md#create-a-user-assigned-managed-identity) or a [system-assigned managed identity](search-how-to-managed-identities.md#create-a-system-managed-identity), depending on your scenario requirements.
    
 1. Capture the **object (principal) ID**. This will be used as part of the credentials configuration when creating the data source.
-    <!-- GIA TO ADD THIS SCREENSHOT OF UAMI OBJECT PRINCIPAL --> 
-    <!-- GIA TO ADD THIS SCREENSHOT OF SAMI OBJECT PRINCIPAL -->
    
 1. Select **Certificates & Secrets** from the menu on the left.
-      <!-- GIA TO ADD THIS SCREENSHOT -->
 
 1. Under **Federated credentials** select **+ Add a credential**.
 
-      <!-- GIA TO ADD THIS SCREENSHOT -->
-
 1. Under **Federated credential scenario** select **Managed Identity**. 
 
-    <!-- GIA TO ADD THIS SCREENSHOT OF SAMI OBJECT PRINCIPAL -->
-
 1. Select managed identity: Choose the created managed identity created as part of step 1.
 
-    <!-- GIA TO ADD THIS SCREENSHOT OF UAMI SELECTION --> 
-    <!-- GIA TO ADD THIS SCREENSHOT OF SAMI SELECTION -->
-
 1. Add a name for your credential and select **Save**.
 
 <a name="create-data-source"></a>
@@ -528,6 +518,8 @@ The "query" parameter of the data source is made up of keyword/value pairs. The
 | includeLibrariesInSite | Index content from all libraries under the specified site in the connection string. The value should be the URI of the site or subsite. <br><br>Example 1: <br><br>```"container" : { "name" : "useQuery", "query" : "includeLibrariesInSite=https://mycompany.sharepoint.com/mysite" }``` <br><br>Example 2 (include a few subsites only): <br><br>```"container" : { "name" : "useQuery", "query" : "includeLibrariesInSite=https://mycompany.sharepoint.com/sites/TopSite/SubSite1;includeLibrariesInSite=https://mycompany.sharepoint.com/sites/TopSite/SubSite2" }``` |
 | includeLibrary | Index all content from this library. The value is the fully qualified path to the library, which can be copied from your browser: <br><br>Example 1 (fully qualified path): <br><br>```"container" : { "name" : "useQuery", "query" : "includeLibrary=https://mycompany.sharepoint.com/mysite/MyDocumentLibrary" }``` <br><br>Example 2 (URI copied from your browser): <br><br>```"container" : { "name" : "useQuery", "query" : "includeLibrary=https://mycompany.sharepoint.com/teams/mysite/MyDocumentLibrary/Forms/AllItems.aspx" }``` |
 | excludeLibrary | Don't index content from this library. The value is the fully qualified path to the library, which can be copied from your browser: <br><br> Example 1 (fully qualified path): <br><br>```"container" : { "name" : "useQuery", "query" : "includeLibrariesInSite=https://mysite.sharepoint.com/subsite1; excludeLibrary=https://mysite.sharepoint.com/subsite1/MyDocumentLibrary" }``` <br><br> Example 2 (URI copied from your browser): <br><br>```"container" : { "name" : "useQuery", "query" : "includeLibrariesInSite=https://mycompany.sharepoint.com/teams/mysite; excludeLibrary=https://mycompany.sharepoint.com/teams/mysite/MyDocumentLibrary/Forms/AllItems.aspx" }``` |
+| includeFolder | Index content from a specific folder and its subfolders. Value must be a full SharePoint folder URL. <br><br> Behavior: Applies recursively to all subfolders. Multiple folders can be specified by repeating the parameter with semicolons. Folder filters are scoped to a single document library. Root-only paths aren't supported. If a folder referenced is renamed, the query must be updated. <br><br> Example 1 (single folder): <br>```"container": { "name": "useQuery", "query": "includeFolder=contoso.sharepoint.com/sites/hr/Shared Documents/Policies" }```<br><br> Example 2 (multiple folders): <br> ```"container": { "name": "useQuery", "query": "includeFolder=contoso.sharepoint.com/sites/hr/Shared Documents/Specs;includeFolder=contoso.sharepoint.com/sites/hr/Shared Documents/Designs" }``` |
+| excludeFolder | Don’t index content from a specific folder and its subfolders. Value must be a full SharePoint folder URL. <br><br> Behavior: Applies recursively to all subfolders. If a file matches both include and exclude rules, exclude takes precedence and the file is skipped. Folder filters are scoped to a single document library. <br><br> Example 1 (exclude folder): <br>```"container": { "name": "useQuery", "query": "excludeFolder=contoso.sharepoint.com/sites/hr/Shared Documents/Policies/Archive" }```<br><br> Example 2 (combine include + exclude): <br>```"container": { "name": "useQuery", "query": "includeFolder=contoso.sharepoint.com/sites/hr/Shared Documents/Policies;excludeFolder=contoso.sharepoint.com/sites/hr/Shared Documents/Policies/Drafts" }```|
 | additionalColumns | Index columns from the document library. The value is a comma-separated list of column names you want to index. Use a double backslash to escape semicolons and commas in column names: <br><br> Example 1 (additionalColumns=MyCustomColumn,MyCustomColumn2):  <br><br>```"container" : { "name" : "useQuery", "query" : "includeLibrary=https://mycompany.sharepoint.com/mysite/MyDocumentLibrary;additionalColumns=MyCustomColumn,MyCustomColumn2" }``` <br><br> Example 2 (escape characters using double backslash): <br><br> ```"container" : { "name" : "useQuery", "query" : "includeLibrary=https://mycompany.sharepoint.com/teams/mysite/MyDocumentLibrary/Forms/AllItems.aspx;additionalColumns=MyCustomColumnWith\\,,MyCustomColumnWith\\;" }``` |
 
 ## Handling errors
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint Onlineインデックス作成に関する記事の更新"
}
```

### Explanation
このコードの変更は、「SharePoint Onlineのインデックス作成」に関する記事の内容を更新するもので、記事の日付を更新し、いくつかの重要な情報を追加したことが含まれます。主な変更点として、いくつかの削除や修正が行われ、新しい機能や手順が追加されました。

具体的には、「特定のフォルダーとそのサブフォルダーからのコンテンツをインデックスする」という新しいパラメータ「includeFolder」が追加され、複数のフォルダーをセミコロンで区切って指定できるようになりました。また、「特定のフォルダーとそのサブフォルダーからのコンテンツをインデックスしない」機能を提供する「excludeFolder」パラメータも導入されました。これにより、ユーザーはインデックスの適用範囲をより柔軟に制御できるようになりました。

これらの変更により、SharePoint Onlineでのインデックス作成の設定や管理が一層明確になり、利用者にとって使いやすくなっています。全体として、ユーザーがインデクサー設定を行う際のガイダンスが強化されています。


