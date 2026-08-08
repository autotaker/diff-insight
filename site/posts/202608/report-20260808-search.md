---
date: '2026-08-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5715d37...MicrosoftDocs:bc909e2
summary: このコード変更では、主に3種類の修正が行われ、Azure Container AppsにC#の検索アプリをデプロイするための新しいチュートリアルが追加されました。既存のチュートリアルのいくつかが削除され、目次や一部の内容が更新されました。新たに追加されたチュートリアルにより、C#開発者向けに詳細な手順が提供され、モダンなアプローチを促進する方向性が示されています。ただし、削除されたチュートリアルに依存していたユーザーには新たな情報が必要になるため、追加のガイドラインが求められる可能性があります。全体的に、Azureプラットフォームの利用を促進し、開発者にとって便利なツールを提供することを目的とした変更です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5715d37...MicrosoftDocs:bc909e2){target="_blank"}

<format>
# ハイライト
このコード変更では、複数のJSONおよびマークダウンファイルに対して主に3種類の変更が行われています。新機能の追加として、Azure Container AppsにC#の検索アプリをデプロイするための新しいチュートリアルが導入されました。また、既存のチュートリアルの削除や、目次および一部チュートリアル内容の小規模な更新も行われています。

## 新機能
- `tutorial-csharp-deploy-web-search.md`という新しいファイルが追加され、C#アプリケーションをAzure Container Appsにデプロイするための手順を詳細に説明しています。

## ブレイキングチェンジ
- `tutorial-csharp-create-load-index.md`と`tutorial-csharp-deploy-static-web-app.md`の削除により、これらのチュートリアルに依存していたユーザーは新たな情報を必要とします。

## 他の更新
- リダイレクトURLの更新と追加が`search.json`で行われ、正しいチュートリアルへ誘導するように調整されました。
- `toc.yml`で目次の内容が更新され、特にC#のウェブアプリ向けの項目が新たに追加されています。
- いくつかの既存チュートリアルが小規模な更新を受け、最新の技術や開発ツールを反映しました。

# インサイト
この一連の変更は、Azureプラットフォーム上でのC#ウェブアプリケーションの開発とデプロイに関するドキュメンテーションを最新のものにすることを目的としています。まず、Azure Static Web Apps向けだったいくつかのチュートリアルが削除され、新たにAzure Container Apps向けのデプロイ方法が強調されています。これは、Azureのコンテナサービスの利用を促進し、よりモダンなアプローチを採用しようとする方針の一貫と考えられます。

また、新しいチュートリアルの追加や、既存のものの更新により、ユーザーに対してより詳細で具体的な手順が提供されています。これにより、特にC#開発者がAzure AI Searchを使用した効果的なアプリケーション構成やデプロイが可能になります。

一方で、いくつかのチュートリアルの削除は開発者にとって痛手となる可能性があります。これらのチュートリアルに依存していた開発者に対しては、新たなガイドラインやリソースを提供する必要があります。全体として、Azureプラットフォームの利用を促進し、開発者にとってより便利で実用的なツールを提供しようとする試みとして評価できます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [.openpublishing.redirection.search.json](#item-8b66f9) | minor update | リダイレクトURLの更新と追加: search.jsonファイル | modified | 16 | 6 | 22 | 
| [toc.yml](#item-c4768f) | minor update | 目次の更新: toc.ymlファイル | modified | 4 | 6 | 10 | 
| [tutorial-csharp-create-load-index.md](#item-0a6ffd) | breaking change | チュートリアルの削除: C#でのインデックス作成 | removed | 0 | 95 | 95 | 
| [tutorial-csharp-deploy-static-web-app.md](#item-a2300f) | breaking change | チュートリアルの削除: C#静的ウェブアプリのデプロイ | removed | 0 | 164 | 164 | 
| [tutorial-csharp-deploy-web-search.md](#item-305a56) | new feature | C#検索アプリをAzure Container Appsにデプロイするチュートリアルの追加 | added | 130 | 0 | 130 | 
| [tutorial-csharp-overview.md](#item-57fa0d) | minor update | C#ウェブアプリに検索機能を追加するチュートリアルの更新 | modified | 39 | 35 | 74 | 
| [tutorial-csharp-search-query-integration.md](#item-8ad6b5) | minor update | C#アプリにおけるAzure AI Searchクエリ統合に関するチュートリアルの更新 | modified | 85 | 30 | 115 | 


# Modified Contents
## articles/search/.openpublishing.redirection.search.json{#item-8b66f9}

<details>
<summary>Diff</summary>
````diff
@@ -65,19 +65,24 @@
             "redirect_url": "/azure/search/tutorial-csharp-overview",
             "redirect_document_id": false
         },
+        {
+            "source_path_from_root": "/articles/search/tutorial-csharp-deploy-static-web-app.md",
+            "redirect_url": "/azure/search/tutorial-csharp-deploy-web-search",
+            "redirect_document_id": false
+        },
         {
             "source_path_from_root": "/articles/search/tutorial-javascript-create-load-index.md",
-            "redirect_url": "/azure/search/tutorial-csharp-create-load-index",
+            "redirect_url": "/azure/search/tutorial-csharp-overview",
             "redirect_document_id": false
         },
         {
             "source_path_from_root": "/articles/search/tutorial-javascript-deploy-static-web-app.md",
-            "redirect_url": "/azure/search/tutorial-csharp-deploy-static-web-app",
+            "redirect_url": "/azure/search/tutorial-csharp-overview",
             "redirect_document_id": false
         },
         {
             "source_path_from_root": "/articles/search/tutorial-javascript-search-query-integration.md",
-            "redirect_url": "/azure/search/tutorial-csharp-search-query-integration",
+            "redirect_url": "/azure/search/tutorial-csharp-overview",
             "redirect_document_id": false
         },
         {
@@ -87,17 +92,17 @@
         },
         {
             "source_path_from_root": "/articles/search/tutorial-python-create-load-index.md",
-            "redirect_url": "/azure/search/tutorial-csharp-create-load-index",
+            "redirect_url": "/azure/search/tutorial-csharp-overview",
             "redirect_document_id": false
         },
         {
             "source_path_from_root": "/articles/search/tutorial-python-deploy-static-web-app.md",
-            "redirect_url": "/azure/search/tutorial-csharp-deploy-static-web-app",
+            "redirect_url": "/azure/search/tutorial-csharp-overview",
             "redirect_document_id": false
         },
         {
             "source_path_from_root": "/articles/search/tutorial-python-search-query-integration.md",
-            "redirect_url": "/azure/search/tutorial-csharp-search-query-integration",
+            "redirect_url": "/azure/search/tutorial-csharp-overview",
             "redirect_document_id": false
         },
         {
@@ -659,6 +664,11 @@
             "source_path_from_root": "/articles/search/search-security-overview.md",
             "redirect_url": "/azure/search/search-security-built-in",
             "redirect_document_id": true
+        },
+        {
+            "source_path_from_root": "/articles/search/tutorial-csharp-create-load-index.md",
+            "redirect_url": "/azure/search/tutorial-csharp-overview",
+            "redirect_document_id": false
         }
     ]
   }
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リダイレクトURLの更新と追加: search.jsonファイル"
}
```

### Explanation
このコードの変更では、`articles/search/.openpublishing.redirection.search.json`ファイル内のリダイレクトURLに関する修正が行われています。主な変更点としては、いくつかの既存のリダイレクトURLが他のリダイレクトURLに更新され、さらに新しいリダイレクトエントリが追加されています。

具体的には、いくつかのチュートリアル関連のソースパスから、リダイレクト先が`/azure/search/tutorial-csharp-overview`に変更されていますとはべ、それに加えて新しいエントリも追加されています。この変更により、ユーザーが正しいチュートリアルに導かれるように、リダイレクトリンクの整合性が向上しました。

追加されたリダイレクトURLは、特定のチュートリアルから新しいアプローチに誘導することを意図しており、特にC#のチュートリアルに関連するリンクが強調されています。このようにすることで、ユーザーがよりスムーズに必要な情報にアクセスできるようになります。全体として、これらの修正はマイナーな更新に分類され、文書の利便性を向上させることが目的とされています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -643,15 +643,13 @@ items:
     items:
     - name: Create a demo app
       href: search-create-app-portal.md
-    - name: Add search to a static web app
+    - name: Add search to a C# web app
       items:
       - name: Overview
         href: tutorial-csharp-overview.md
-      - name: Create a search index
-        href: tutorial-csharp-create-load-index.md
-      - name: Deploy static web app
-        href: tutorial-csharp-deploy-static-web-app.md
-      - name: Explore the code
+      - name: 1 - Deploy to Azure Container Apps
+        href: tutorial-csharp-deploy-web-search.md
+      - name: 2 - Explore the code
         href: tutorial-csharp-search-query-integration.md
 
 - name: Monitoring
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新: toc.ymlファイル"
}
```

### Explanation
このコードの変更は、`articles/search/toc.yml`ファイルの目次に関する修正を反映しています。主な変更点には、リスト内の項目の名称変更、追加、および削除があります。

具体的には、「Add search to a static web app」という項目が「Add search to a C# web app」に名称変更され、内容がC#に特化したものに更新されています。これにより、C#のウェブアプリケーションへの検索機能追加に焦点を合わせた内容が反映されています。

さらに、いくつかの項目が削除され、代わりに「1 - Deploy to Azure Container Apps」という新たな項目が追加されています。この新しい項目はC#ウェブ検索のデプロイに関する内容を含んでおり、ユーザーに対して具体的な手順が提供されています。また、従来の「Explore the code」の項目も更新され、今後の項目との関連性が明確になっています。

これらの変更は全体としてマイナーな更新に分類され、目次の内容をよりユーザーに合わせた形に改善することを目的としています。これにより、ドキュメントを参照する際の利便性が向上し、ユーザーは目的の情報をより効率的に見つけることができます。

## articles/search/tutorial-csharp-create-load-index.md{#item-0a6ffd}

<details>
<summary>Diff</summary>
````diff
@@ -1,95 +0,0 @@
----
-title: Load an Index (.NET Tutorial)
-description: Create index and import CSV data into Search index with .NET.
-ms.reviewer: diberry
-ms.service: azure-ai-search
-ms.update-cycle: 180-days
-ms.topic: tutorial
-ms.date: 07/21/2026
-ai-usage: ai-assisted
-ms.custom:
-  - devx-track-csharp
-  - devx-track-azurecli
-  - devx-track-dotnet
-  - devx-track-azurepowershell
-  - ignite-2023
-ms.devlang: csharp
----
-
-# Step 2 - Create and load the search index
-
-[!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
-
-Continue to build your search-enabled website by following these steps:
-
-- Create a new index
-- Load data
-
-The program uses [Azure.Search.Documents](https://www.nuget.org/packages/Azure.Search.Documents/) in the Azure SDK for .NET:
-
-- [NuGet package Azure.Search.Documents](https://www.nuget.org/packages/Azure.Search.Documents/)
-- [Reference Documentation](/dotnet/api/overview/azure/search)
-
-Before you start, make sure you have room on your search service for a new index. The free tier limit is three indexes. The Basic tier limit is 15.
-
-## Prepare the bulk import script for Search
-
-1. In Visual Studio Code, open the `Program.cs` file in the subdirectory, `azure-search-static-web-app/bulk-insert`, replace the following variables with your own values to authenticate with the Azure Search SDK.
-
-   - YOUR-SEARCH-SERVICE-NAME (not the full URL)
-   - YOUR-SEARCH-ADMIN-API-KEY (see [Find API keys](search-security-api-keys.md#find-existing-keys))
-
-    :::code language="csharp" source="~/azure-search-static-web-app/bulk-insert/Program.cs" :::
-
-1. Open an integrated terminal in Visual Studio Code for the project directory's subdirectory, `azure-search-static-web-app/bulk-insert`.
-
-1. Run the following command to install the dependencies. 
-
-    ```bash
-    dotnet restore
-    ```
-
-## Run the bulk import script for Search
-
-1. Still in the same subdirectory (`azure-search-static-web-app/bulk-insert`), run the program:
-
-    ```bash
-    dotnet run
-    ```
-
-1. As the code runs, the console displays progress. You should see the following output.
-
-   ```bash
-    Creating (or updating) search index
-    Status: 201, Value: Azure.Search.Documents.Indexes.Models.SearchIndex
-    Download data file
-    Reading and parsing raw CSV data
-    Uploading bulk book data
-    Finished bulk inserting book data
-    ```
-
-## Review the new search index
-
-Once the upload completes, the search index is ready to use. Review your new index in Azure portal.
-
-1. Go to your search service in the [Azure portal](https://portal.azure.com).
-
-1. On the left, select **Search Management > Indexes**, and then select the good-books index.
-
-    :::image type="content" source="media/tutorial-csharp-create-load-index/azure-portal-indexes-page.png" lightbox="media/tutorial-csharp-create-load-index/azure-portal-indexes-page.png" alt-text="Expandable screenshot of Azure portal showing the index." border="true":::
-
-1. By default, the index opens in the **Search Explorer** tab. Select **Search** to return documents from the index.
-
-    :::image type="content" source="media/tutorial-csharp-create-load-index/azure-portal-search-explorer.png" lightbox="media/tutorial-csharp-create-load-index/azure-portal-search-explorer.png" alt-text="Expandable screenshot of Azure portal showing search results" border="true":::
-
-## Rollback bulk import file changes
-
-Use the following git command in the Visual Studio Code integrated terminal at the `bulk-insert` directory to roll back the changes to the `Program.cs` file. They aren't needed to continue the tutorial and you shouldn't save or push your API keys or search service name to your repo. 
-
-```git
-git checkout .
-```
-
-## Next steps
-
-[Deploy your Static Web App](tutorial-csharp-deploy-static-web-app.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "チュートリアルの削除: C#でのインデックス作成"
}
```

### Explanation
このコード変更は、`articles/search/tutorial-csharp-create-load-index.md`ファイルが完全に削除されたことを示しています。このファイルには、C#を使用してAzure Searchサービスにインデックスを作成し、CSVデータをインポートするためのチュートリアルが提供されていました。

削除された内容には、インデックスの作成、データの読み込み、Visual Studio Codeでの準備手順、バルクインポートスクリプトの実行、インデックスのレビュー、およびロールバック手順が含まれていました。このチュートリアルは、特に開発者がAzure Searchを有効にしたウェブアプリケーションに必要なステップを理解するための重要なガイドラインとなっていました。

この削除は大きな変更であり、チュートリアルに依存していたユーザーは新たな情報を探さなければならなくなります。それに加えて、他のチュートリアルやドキュメントとの整合性を保つための代替手段や新しいリソースの提供が期待されます。このように、モジュールの削除はユーザーにとって影響が大きいと考えられます。

## articles/search/tutorial-csharp-deploy-static-web-app.md{#item-a2300f}

<details>
<summary>Diff</summary>
````diff
@@ -1,164 +0,0 @@
----
-title: Deploy Search App (.NET Tutorial)
-description: Deploy search-enabled website with .NET APIs to Azure Static web app.
-ms.reviewer: diberry
-ms.service: azure-ai-search
-ms.update-cycle: 180-days
-ms.topic: tutorial
-ms.date: 04/27/2026
-ms.custom:
-  - devx-track-csharp
-  - devx-track-dotnet
-  - ignite-2023
-ms.devlang: csharp
-ai-usage: ai-assisted
----
-
-# Step 3 - Deploy the search-enabled .NET website
-
-[!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
-
-Deploy the search-enabled website as an Azure Static Web Apps site. This deployment includes both the React app for the web pages, and the Function app for search operations.  
-
-The static web app pulls the information and files for deployment from GitHub using your fork of the azure-search-static-web-app repository.  
-
-## Create a Static Web App in Visual Studio Code
-
-1. In Visual Studio Code, make sure you're at the repository root, and not the bulk-insert folder (for example, `azure-search-static-web-app`).
-
-1. Select **Azure** from the Activity Bar, then open **Resources** from the side bar. 
-
-1. Right-click **Static Web Apps** and then select **Create Static Web App (Advanced)**. If you don't see this option, verify that you have the Azure Functions extension for Visual Studio Code.
-
-    :::image type="content" source="media/tutorial-csharp-static-web-app/visual-studio-code-create-static-web-app-resource-advanced.png" alt-text="Screenshot of Visual Studio Code, with the Azure Static Web Apps explorer showing the option to create an advanced static web app.":::
-
-1. If you see a pop-up window asking you to commit your changes, don't do this. The secrets from the bulk import step shouldn't be committed to the repository. 
-
-    To roll back the changes, in Visual Studio Code select the Source Control icon in the Activity bar, then select each changed file in the Changes list and select the **Discard changes** icon.
-
-1. Follow the prompts to create the static web app:
-
-    |Prompt|Enter|
-    |--|--|
-    |Select a resource group for new resources. | Create a new resource group for the static app.|
-    |Enter the name for the new Static Web App. | Give your static app a name, such as `my-demo-static-web-app`. |
-    |Select a SKU | Select the free SKU for this tutorial.|
-    |Select a location for new resources. | Choose a region near you. |
-    |Choose build preset to configure default project structure. |Select **Custom**. |
-    |Select the location of your client application code | `client`<br><br>This is the path, from the root of the repository, to your static web app. |
-    |Enter the path of your build output... | `build`<br><br>This is the path, from your static web app, to your generated files.|
-
-    If you get an error about an incorrect region, make sure the resource group and static web app resource are in one of the supported regions listed in the error response. 
-
-1. When the static web app is created, a GitHub workflow YML file is also created locally and on GitHub in your fork. This workflow executes in your fork, building and deploying the static web app and functions.
-
-   Check the status of static web app deployment using any of these approaches:
-
-   * Select **Open Actions in GitHub** from the Notifications. This opens a browser window pointed to your forked repo.
-   * Select the **Actions** tab in your forked repository. You should see a list of all workflows on your fork.
-   * Select the **Azure: Activity Log** in Visual Code. You should see a message similar to the following screenshot.
-
-     :::image type="content" source="media/tutorial-csharp-static-web-app/visual-studio-code-azure-activity-log.png" alt-text="Screenshot of the Activity Log in Visual Studio Code." border="true":::
-
-## Get the Azure AI Search query key in Visual Studio Code
-
-While you might be tempted to reuse your search admin key for query purposes that isn't following the principle of least privilege. The Azure Function should use the query key to conform to least privilege.
-
-1. In Visual Studio Code, open a new terminal window.
-
-1. Get the query API key with this Azure CLI command:
-
-    ```azurecli
-    az search query-key list --resource-group YOUR-SEARCH-SERVICE-RESOURCE-GROUP --service-name YOUR-SEARCH-SERVICE-NAME
-    ```
-
-1. Keep this query key to use in the next section. The query key authorizes read access to a search index. 
-
-## Add environment variables in Azure portal
-
-The Azure Function app won't return search data until the search secrets are in settings. 
-
-1. Select **Azure** from the Activity Bar. 
-
-1. Right-click on your Static Web Apps resource then select **Open in Portal**.
-
-    :::image type="content" source="media/tutorial-csharp-static-web-app/open-static-web-app-in-azure-portal.png" alt-text="Screenshot of Visual Studio Code showing Azure Static Web Apps explorer with the Open in Portal option shown.":::
-
-1. Select **Environment variables** then select **+ Add application setting**.
-
-    :::image type="content" source="media/tutorial-csharp-static-web-app/add-new-application-setting-to-static-web-app-in-portal.png" alt-text="Screenshot of the static web app's environment variables page in the Azure portal.":::
-
-1. Add each of the following settings:
-
-    |Setting|Your Search resource value|
-    |--|--|
-    |SearchApiKey|Your search query key|
-    |SearchServiceName|Your search resource name|
-    |SearchIndexName|`good-books`|
-    |SearchFacets|`authors*,language_code`|
-
-    Azure AI Search requires different syntax for filtering collections than it does for strings. Add a `*` after a field name to denote that the field is of type `Collection(Edm.String)`. This allows the Azure Function to add filters correctly to queries.
-
-1. Check your settings to make sure they look like the following screenshot.
-
-    :::image type="content" source="media/tutorial-csharp-static-web-app/save-new-application-setting-to-static-web-app-in-portal.png" alt-text="Screenshot of browser showing Azure portal with the button to save the settings for your app.":::
-
-1. Return to Visual Studio Code. 
-
-1. Refresh your static web app to see the application settings and functions.
-
-    :::image type="content" source="media/tutorial-csharp-static-web-app/visual-studio-code-extension-fresh-resource-2.png" alt-text="Screenshot of Visual Studio Code showing the Azure Static Web Apps explorer with the new application settings." border="true":::
-
-If you don't see the application settings, revisit the steps for updating and relaunching the GitHub workflow.
-
-## Use search in your static web app
-
-1. In Visual Studio Code, open the [Activity bar](https://code.visualstudio.com/docs/getstarted/userinterface), and select the Azure icon.
-
-1. In the Side bar, **right-click on your Azure subscription** under the `Static Web Apps` area and find the static web app you created for this tutorial.
-
-1. Right-click the static web app name and select **Browse site**.
-
-    :::image type="content" source="media/tutorial-csharp-static-web-app/visual-studio-code-browse-static-web-app.png" alt-text="Screenshot of Visual Studio Code showing the Azure Static Web Apps explorer showing the **Browse site** option.":::
-
-1. Select **Open** in the pop-up dialog.
-
-1. In the website search bar, enter a search query such as `code`, so the suggest feature suggests book titles. Select a suggestion or continue entering your own query. Press enter when you've completed your search query. 
-
-1. Review the results then select one of the books to see more details. 
-
-## Troubleshooting
-
-If the web app didn't deploy or work, use the following list to determine and fix the issue:
-
-* **Did the deployment succeed?** 
-
-    In order to determine if your deployment succeeded, you need to go to _your_ fork of the sample repo and review the success or failure of the GitHub action. There should be only one action and it should have static web app settings for the  `app_location`, `api_location`, and `output_location`. If the action didn't deploy successfully, dive into the action logs and look for the last failure. 
-
-* **Does the client (front-end) application work?**
-
-    You should be able to get to your web app and it should successfully display. If the deployment succeeded but the website doesn't display, this might be an issue with how the static web app is configured for rebuilding the app, once it is on Azure. 
-
-* **Does the API (serverless back-end) application work?**
-
-    You should be able to interact with the client app, searching for books and filtering. If the form doesn't return any values, open the browser's developer tools, and determine if the HTTP calls to the API were successful. If the calls weren't successful, the most likely reason if the static web app configurations for the API endpoint name and search query key are incorrect.
-
-    If the path to the Azure function code (`api_location`) isn't correct in the YML file, the application loads but won't call any of the functions that provide integration with Azure AI Search. Revisit the deployment section to make sure paths are correct.
-
-## Clean up resources
-
-To clean up the resources created in this tutorial, delete the resource group or individual resources.
-
-1. In Visual Studio Code, open the [Activity bar](https://code.visualstudio.com/docs/getstarted/userinterface), and select the Azure icon. 
-
-1. In the Side bar, **right-click on your Azure subscription** under the `Static Web Apps` area and find the app you created for this tutorial.
-
-1. Right-click the app name then select **Delete**.
-
-1. If you no longer want the GitHub fork of the sample, remember to delete that on GitHub. Go to your fork's **Settings** then delete the repository.
-
-1. To delete Azure AI Search, go to your search service in the [Azure portal](https://portal.azure.com) and select **Delete** at the top of the page.
-
-## Next steps
-
-* [Understand Search integration for the search-enabled website](tutorial-csharp-search-query-integration.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "チュートリアルの削除: C#静的ウェブアプリのデプロイ"
}
```

### Explanation
このコードの変更は、`articles/search/tutorial-csharp-deploy-static-web-app.md`ファイルが完全に削除されたことを示しています。このファイルは、C#を使用して検索機能を持つウェブサイトをAzure Static Web Appsにデプロイするための手順を提供していました。

削除された内容には、次のような重要な手順が含まれていました：Azure Static Web Appの作成、環境変数の設定、クエリキーの取得、そしてデプロイされたアプリケーションの動作確認に関する詳細なガイドラインが記載されていました。これにより、ユーザーは自作のウェブアプリケーションをデプロイし、Azure Searchと統合する能力をもっていました。

このファイルの削除は大きな影響をもたらし、特にC#を用いたウェブアプリケーション開発者にとっては、必要なリソースやガイドを失うことになります。このため、代替情報がどのように提供されるのか、また新たなチュートリアルやドキュメントがどのように補完されるのかが注目されます。この変更は、既存のユーザーにとっては不便を引き起こす可能性が高いと考えられます。

## articles/search/tutorial-csharp-deploy-web-search.md{#item-305a56}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,130 @@
+---
+title: Deploy a C# Search App to Azure Container Apps
+description: Learn how to deploy a C# app with Azure AI Search to Azure Container Apps by using azd with managed identity or optional key-based authentication.
+ms.reviewer: diberry
+ms.service: azure-ai-search
+ms.update-cycle: 180-days
+ms.topic: tutorial
+ms.date: 08/07/2026
+ms.custom:
+  - devx-track-csharp
+  - devx-track-dotnet
+  - ignite-2023
+ms.devlang: csharp
+ai-usage: ai-assisted
+---
+
+# Deploy a C# Azure AI Search app to Azure Container Apps
+
+[!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
+
+Deploy the search-enabled website to Azure Container Apps by using the Azure Developer CLI (`azd`). This deployment includes the React client, the .NET API, Azure AI Search, managed identity, and supporting Azure resources.
+
+The deployment uses managed identity as the default authentication method for Azure AI Search. You can opt in to key-based authentication by setting `USE_KEYLESS_AUTH` to `false` before deployment.
+
+## Sign in to Azure
+
+1. In Visual Studio Code, open a terminal at the repository root, such as `azure-search-static-web-app`.
+
+1. Sign in to Azure by using `azd`.
+
+    ```bash
+    azd auth login
+    ```
+
+1. If prompted by your browser, complete the sign-in flow by using the Azure account that you're using for this tutorial.
+
+## Create an azd environment
+
+- Create an `azd` environment. Replace `YOUR-ENVIRONMENT-NAME` with a short name that identifies this tutorial deployment.
+
+    ```bash
+    azd env new YOUR-ENVIRONMENT-NAME
+    ```
+
+## (Optional) Configure key-based authentication
+
+The default authentication method is managed identity, so most environments can skip this section. Complete this section only if your environment requires API keys.
+
+Set `USE_KEYLESS_AUTH` to `false`.
+
+  ```bash
+  azd env set USE_KEYLESS_AUTH false
+  ```
+
+If you don't set `USE_KEYLESS_AUTH`, the deployment uses managed identity. The Bicep infrastructure grants the container app identity access to the Azure AI Search data plane.
+
+## Deploy with azd up
+
+1. From the repository root, run `azd up`.
+
+    ```bash
+    azd up
+    ```
+
+1. When prompted, select the Azure subscription and location for the resources.
+
+1. Wait for `azd` to provision the infrastructure, build the containers, push the images, and deploy the services to Azure Container Apps.
+
+1. Review the output after deployment. The output includes the client and server fully qualified domain names (FQDNs) for the Azure Container Apps deployment.
+
+    ```output
+    AZURE_CLIENT_URL: <client-container-app-fqdn>
+    AZURE_SERVER_URL: <server-container-app-fqdn>
+    SEARCH_SERVICE_NAME: <search-service-name>
+    ```
+
+    Use the `AZURE_CLIENT_URL` value to open the website. The client app calls the server app through the endpoint configured during deployment.
+
+    The deployment also created the Azure AI Search service and loaded the `good-books` index automatically through the `postprovision` hook in the sample repository.
+
+## Use search in your Container Apps website
+
+1. Open the client FQDN from the `azd up` output in a browser.
+
+1. In the website search bar, enter a search query, such as `code`. The autocomplete feature suggests matching book titles.
+
+1. Select a suggestion or continue entering your own query. Select **Enter** when you finish your search query.
+
+1. Review the results, and then select a book to see more details.
+
+## Troubleshooting
+
+If the web app doesn't deploy or work, use the following list to determine and fix the issue:
+
+- **Did `azd up` complete?**
+
+  Review the `azd up` output for the first failed provisioning, build, or deploy step. If deployment stops during provisioning, check your subscription permissions and the selected region. If deployment stops during the container build or deploy steps, rerun `azd up` after you fix the reported issue.
+
+- **Can you open the client endpoint?**
+
+  Open the `AZURE_CLIENT_URL` value from the `azd up` output. If the page doesn't load, go to the Azure portal, open the client container app and review its revision status and logs.
+
+- **Can the client call the server endpoint?**
+
+  Open your browser developer tools and review the network calls from the client app. If calls to the API fail, confirm that the server container app is running and that the client app received the server FQDN during deployment.
+
+- **Can the server query Azure AI Search?**
+
+  If searches return errors, review the server container app logs. For managed identity, confirm that the identity has Azure AI Search data-plane access. For key-based authentication, confirm that you set `USE_KEYLESS_AUTH` to `false` before deployment and that the generated container environment contains the search service configuration.
+
+## Clean up resources
+
+Use `azd down --purge` to delete the Azure resources that this tutorial created. The `--purge` flag permanently removes resources that support soft-delete, instead of leaving them in a recoverable state for their retention period. Purging avoids naming conflicts if you redeploy this tutorial later.
+
+1. From the repository root, run the clean-up command.
+
+    ```bash
+    azd down --purge
+    ```
+
+1. Review the resources that `azd` lists.
+
+1. Confirm the deletion when prompted.
+
+If you created an Azure AI Search service outside the `azd` deployment, go to your search service in the [Azure portal](https://portal.azure.com) and select **Delete** at the top of the page.
+
+## Next step
+
+> [!div class="nextstepaction"]
+> [Explore the search integration code](tutorial-csharp-search-query-integration.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "C#検索アプリをAzure Container Appsにデプロイするチュートリアルの追加"
}
```

### Explanation
このコード変更は、`articles/search/tutorial-csharp-deploy-web-search.md`という新しいファイルが追加されたことを示しています。このファイルは、C#アプリケーションをAzure AI Searchと共にAzure Container Appsにデプロイするための手順を詳細に説明しています。

新しいチュートリアルには、次の重要な項目が含まれています：
- Azure Developer CLI（`azd`）を使用して、検索機能を持つウェブサイトをAzure Container Appsにデプロイする方法。
- デプロイメントに必要な要素として、Reactクライアント、.NET API、Azure AI Search、管理されたID、その他のAzureリソースが含まれること。
- デフォルトの認証方法として管理されたIDを使用し、必要に応じてキーに基づいた認証をオプトインする方法。
- Azureへのサインイン手順や、環境を設定する指示も含まれており、ユーザーが実際にデプロイするための具合的な手順が提供されています。

この新しいチュートリアルは、特にC#開発者に対してAzure Cloud環境でのアプリケーションデプロイのための価値あるリソースを提供するものであり、学習や実務での利便性を高めると考えられます。この変更は、Azureを使った開発のエコシステムを強化し、ユーザーにより多くの選択肢と機能を提供するものです。

## articles/search/tutorial-csharp-overview.md{#item-57fa0d}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,11 @@
 ---
-title: Add Search to Web Sites (.NET Tutorial)
-description: Technical overview and setup for adding search to a website and deploying to Azure Static Web App with .NET.
+title: "Tutorial: Add Search to a C# Web App"
+description: Learn how to add Azure AI Search to a C# web app, deploy it to Azure Container Apps, and use managed identity for search access.
 ms.reviewer: diberry
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: tutorial
-ms.date: 04/27/2026
+ms.date: 08/07/2026
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
@@ -14,78 +14,82 @@ ms.devlang: csharp
 ai-usage: ai-assisted
 ---
 
-# Step 1 - Overview of adding search to a static web app with .NET
+# Tutorial: Add Azure AI Search to a C# web app on Azure Container Apps
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-This tutorial builds a website that searches through a catalog of books and then deploys the website to an Azure Static Web App. 
+This tutorial builds a website that searches through a catalog of books and deploys the website to Azure Container Apps. The deployment uses the Azure Developer CLI (`azd`) and managed identity as the default authentication method for Azure AI Search.
+
+In this tutorial, you:
+
+> [!div class="checklist"]
+> - Deploy Azure AI Search and auto-seed an index with the Azure Developer CLI.
+> - Integrate search queries, suggestions, facets, pagination, and document lookup in the C# app.
+> - Deploy the app to Azure Container Apps with managed identity as the default authentication method.
 
 ## What does the sample do?
 
-This sample website provides access to a catalog of 10,000 books. You can search the catalog by entering text in the search bar. While you enter text, the website uses the search index's suggestion feature to autocomplete the text. When the query finishes, the website displays the list of books with a portion of the details. You can select a book to see all the details, stored in the search index, of the book. 
+This sample website provides access to a catalog of 10,000 books. You can search the catalog by entering text in the search bar. While you enter text, the website uses the search index's suggestion feature to autocomplete the text.
+
+When the query finishes, the website displays the list of books with a portion of their details. You can select a book to see its complete details, which are stored in the search index.
 
 :::image type="content" source="media/tutorial-csharp-overview/cognitive-search-enabled-book-website-2.png" alt-text="Screenshot of the sample app in a browser window.":::
 
 The search experience includes:
 
-- [Search](search-query-create.md) – provides search functionality for the application.
-- [Suggest](search-add-autocomplete-suggestions.md) – provides suggestions as the user is typing in the search bar.
-- [Facets and filters](search-faceted-navigation.md) - provides a faceted navigation structure that filters by author or language.
-- [Paginated results](search-pagination-page-layout.md) - provides paging controls for scrolling through results.
-- [Document Lookup](search-query-overview.md#document-look-up) – looks up a document by ID to retrieve all of its contents for the details page.
+- [Search](search-query-create.md) - Provides search functionality for the application.
+- [Suggest](search-add-autocomplete-suggestions.md) - Provides suggestions as the user types in the search bar.
+- [Facets and filters](search-faceted-navigation.md) - Provides a faceted navigation structure that filters by author or language.
+- [Paginated results](search-pagination-page-layout.md) - Provides paging controls for scrolling through results.
+- [Document lookup](search-query-overview.md#document-look-up) - Looks up a document by ID to retrieve all of its contents for the details page.
 
 ## How is the sample organized?
 
 The [sample code](https://github.com/Azure-Samples/azure-search-static-web-app) includes the following components:
 
-|App|Purpose|GitHub<br>Repository<br>Location|
+| App | Purpose | GitHub repository location |
 |--|--|--|
-|client|React app (presentation layer) to display books, with search. It calls the Azure Function app. |[/azure-search-static-web-app/client](https://github.com/Azure-Samples/azure-search-static-web-app/tree/main/client)|
-|api|Azure .NET Function app (business layer) - calls the Azure AI Search API using .NET SDK |[/azure-search-static-web-app/api](https://github.com/Azure-Samples/azure-search-static-web-app/tree/main/api)|
-|bulk insert|.NET project to create the index and add documents to it.|[/azure-search-static-web-app/bulk-insert](https://github.com/Azure-Samples/azure-search-static-web-app/tree/main/bulk-insert)|
+| `client` | React app (presentation layer) to display books with search. It calls the API. | [/azure-search-static-web-app/client](https://github.com/Azure-Samples/azure-search-static-web-app/tree/main/client) |
+| `api` | C# Azure Functions API (business layer), hosted in a container on Azure Container Apps, that calls the Azure AI Search API with the .NET SDK. | [/azure-search-static-web-app/api](https://github.com/Azure-Samples/azure-search-static-web-app/tree/main/api) |
+| `bulk-insert` | .NET project that creates the index and loads documents. The `azd` deployment runs this automatically through the `postprovision` hook. | [/azure-search-static-web-app/bulk-insert](https://github.com/Azure-Samples/azure-search-static-web-app/tree/main/bulk-insert) |
+| `infra` | Bicep infrastructure used by `azd` to deploy Azure AI Search, Azure Container Apps, and supporting resources. | [Azure-Samples/azure-search-static-web-app](https://github.com/Azure-Samples/azure-search-static-web-app) |
 
 ## Set up your development environment
 
-Create services and install the following software for your local development environment. 
+Install the following software for your local development environment. The `azd up` command provisions all Azure resources, including Azure AI Search, so you don't need to create them beforehand.
 
-- [Azure AI Search](search-create-service-portal.md), any region or tier
-- [.NET 9](https://dotnet.microsoft.com/download/dotnet) or latest version
+- [.NET 9](https://dotnet.microsoft.com/download/dotnet) or later
 - [Git](https://git-scm.com/downloads)
 - [Visual Studio Code](https://code.visualstudio.com/)
 - [C# Dev Tools extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)
-- [Azure Static Web App extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurestaticwebapps) 
-
-This tutorial doesn't run the Azure Function API locally. If you want to run it locally, install [azure-functions-core-tools](/azure/azure-functions/functions-run-local?tabs=linux%2ccsharp%2cbash#install-the-azure-functions-core-tools).
-
-## Fork and clone the search sample with git
-
-To deploy the Static Web App, you need to fork the sample repository. The web apps use your GitHub fork location to decide the build actions and deployment content. Code execution in the Static Web App happens remotely, with Azure Static Web Apps reading the code from your forked sample.
+- [Azure Developer CLI](/azure/developer/azure-developer-cli/install-azd) (`azd`)
+- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or another Docker-compatible container runtime
 
-1. On GitHub, fork the [azure-search-static-web-app repository](https://github.com/Azure-Samples/azure-search-static-web-app). 
+This tutorial doesn't run the Azure Functions API locally. If you want to run it locally, install [Azure Functions Core Tools](/azure/azure-functions/functions-run-local?tabs=linux%2ccsharp%2cbash#install-the-azure-functions-core-tools).
 
-    Complete the [fork process](https://docs.github.com/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) in your web browser with your GitHub account. This tutorial uses your fork as part of the deployment to an Azure Static Web App. 
+## Clone the search sample with Git
 
-1. At a Bash terminal, download your forked sample application to your local computer. 
+You can deploy the sample from a local clone. The `azd up` command reads the application and infrastructure files from your local repository, builds the containers, provisions Azure resources, and deploys the client and API to Azure Container Apps.
 
-    Replace `YOUR-GITHUB-ALIAS` with your GitHub alias. 
+1. In a Bash terminal, clone the sample application to your local computer.
 
     ```bash
-    git clone https://github.com/YOUR-GITHUB-ALIAS/azure-search-static-web-app.git
+    git clone https://github.com/Azure-Samples/azure-search-static-web-app.git
     ```
 
-1. At the same Bash terminal, go into your forked repository for this website search example:
+1. In the same Bash terminal, go to the repository directory for this search example.
 
     ```bash
     cd azure-search-static-web-app
     ```
 
-1. Use the Visual Studio Code command, `code .` to open your forked repository. You accomplish the remaining tasks from Visual Studio Code, unless specified.
+1. Use the Visual Studio Code command, `code .`, to open the repository. Unless otherwise specified, you complete the remaining tasks in Visual Studio Code.
 
     ```bash
     code .
     ```
 
-## Next steps
+## Next step
 
-- [Create an index and load it with documents](tutorial-csharp-create-load-index.md)
-- [Deploy your Static Web App](tutorial-csharp-deploy-static-web-app.md)
+> [!div class="nextstepaction"]
+> [Deploy the app to Azure Container Apps](tutorial-csharp-deploy-web-search.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#ウェブアプリに検索機能を追加するチュートリアルの更新"
}
```

### Explanation
このコードの変更は、`articles/search/tutorial-csharp-overview.md`ファイルの内容が更新されたことを示しています。主な変更点は、チュートリアルの内容がAzure Static Web AppsからAzure Container Appsへのデプロイに焦点を移し、最新の手法やツールを反映するために情報が修正または追加されたことです。

具体的には、次のようなポイントが挙げられます：
- チュートリアルのタイトルと説明が更新され、具体的にC#ウェブアプリとAzure Container Appsへのデプロイ方法が言及されています。
- Azure Developer CLI（`azd`）を使用したデプロイメントの手順が詳細に追加され、管理されたIDをデフォルトの認証方法として使用することが強調されています。
- 検索機能の統合、オートコンプリートの提案、ファセットとフィルタリング、結果のページネーションなどの新しい機能についても詳しく説明されています。

さらに、サンプルコードや必要な開発環境の設定に関する情報が整理され、ユーザーがチュートリアルを通じてよりスムーズに実装できるように改善されています。この更新は、最新の開発トレンドを反映させ、ユーザーがAzureプラットフォーム上で効果的に開発できるようサポートするものです。

## articles/search/tutorial-csharp-search-query-integration.md{#item-8ad6b5}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,11 @@
 ---
-title: Explore Code (.NET Tutorial)
-description: Understand the .NET SDK Search integration queries used in the Search-enabled website with this cheat sheet.
+title: Explore Azure AI Search query integration in a C# app
+description: Learn how C# query integration works in an Azure AI Search app, including managed identity, search requests, suggestions, and document lookup.
 ms.reviewer: diberry
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: tutorial
-ms.date: 04/27/2026
+ms.date: 08/07/2026
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
@@ -14,67 +14,122 @@ ms.devlang: csharp
 ai-usage: ai-assisted
 ---
 
-# Step 4 - Explore the .NET search code
+# Explore Azure AI Search query integration in a C# app
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-In the previous lessons, you added search to a static web app. This lesson highlights the essential steps that establish integration. If you're looking for a cheat sheet on how to integrate search into your web app, this article explains what you need to know.
+In the previous step, you deployed the search-enabled website to Azure Container Apps. This article highlights the essential steps that establish search integration. Think of it as a cheat sheet for integrating search into your web app.
 
 ## Azure SDK Azure.Search.Documents
 
-The Function app uses the Azure SDK for Azure AI Search:
+The API uses the Azure SDK for Azure AI Search:
 
-* NuGet: [Azure.Search.Documents](https://www.nuget.org/packages/Azure.Search.Documents/)
-* Reference Documentation: [Client Library](/dotnet/api/overview/azure/search)
+- NuGet: [Azure.Search.Documents](https://www.nuget.org/packages/Azure.Search.Documents/)
+- Reference documentation: [Client Library](/dotnet/api/overview/azure/search)
 
-The function app authenticates through the SDK to the cloud-based Azure AI Search API using your resource name, resource key, and index name. The secrets are stored in the static web app settings and pulled in to the function as environment variables. 
+The API authenticates through the SDK to the cloud-based Azure AI Search API by using the search service name and index name. In Azure Container Apps, the container environment provides the configuration values. Managed identity is the default credential path.
 
-## Configure secrets in a local.settings.json file
+## Managed identity authentication
 
-:::code language="json" source="~/azure-search-static-web-app/api/sample.local.settings.json":::
+Each Azure function in the API creates its `SearchClient` through a shared `SearchClientFactory` class, so every function authenticates the same way. By default, the factory builds a `DefaultAzureCredential` and uses it to request tokens for Azure AI Search. In Azure Container Apps, `DefaultAzureCredential` resolves to the managed identity assigned to the container app.
 
-## Azure Function: Search the catalog
+The following method from `SearchClientFactory.cs` creates that credential. When the container app has a user-assigned managed identity, the client ID from the `AZURE_CLIENT_ID` environment variable is passed to `DefaultAzureCredentialOptions` so token acquisition isn't ambiguous.
 
-The [Search API](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/api/Search.cs) takes a search term and searches across the documents in the search index, returning a list of matches. Through the Suggest API, partial strings are sent to the search engine as the user types, suggesting search terms such as book titles and authors across the documents in the search index, and returning a small list of matches. 
+```csharp
+private static DefaultAzureCredential CreateManagedIdentityCredential()
+{
+    var options = new DefaultAzureCredentialOptions();
 
-The Azure function pulls in the search configuration information, and fulfills the query. 
+    if (!string.IsNullOrWhiteSpace(ManagedIdentityClientId))
+    {
+        options.ManagedIdentityClientId = ManagedIdentityClientId;
+    }
+
+    return new DefaultAzureCredential(options);
+}
+```
+
+The Bicep infrastructure assigns the managed identity access to the Azure AI Search data plane during `azd up`. This role assignment lets the API query the `good-books` index without storing a query key in the container environment.
+
+### Local vs. deployed credential resolution
+
+Locally, if `AZURE_CLIENT_ID` is unset, `DefaultAzureCredential` falls back through its standard credential chain and resolves to your signed-in developer credential, such as the Azure CLI or Visual Studio Code account you used to sign in. When deployed to Azure Container Apps, the Bicep infrastructure sets `AZURE_CLIENT_ID` to the user-assigned managed identity's client ID, so `DefaultAzureCredential` targets that identity specifically instead of resolving ambiguously among multiple identities that a host can expose.
+
+To use API keys instead, set `USE_KEYLESS_AUTH` to `false` before deployment:
+
+```bash
+azd env set USE_KEYLESS_AUTH false
+azd up
+```
+
+Use key authentication only when your environment requires it.
+
+## Local development settings
+
+For local development, the sample `sample.local.settings.json` file shows the values the API expects. Use local settings for development only. In Azure Container Apps, deployment configuration provides the equivalent container environment values.
+
+| Setting | Purpose | Required when |
+|--|--|--|
+| `SearchServiceName` | Name of the Azure AI Search service. Combines with `.search.windows.net` to build the service endpoint URI. | Always |
+| `SearchIndexName` | Name of the search index to query. Defaults to `good-books` if unset. | Optional |
+| `SEARCH_USE_KEY_AUTH` | Default is false, uses managed identity. Set to `true` to use an API key instead of managed identity. | Optional key authentication |
+| `SearchApiKey` | Admin key for Azure AI Search. | Required when `SEARCH_USE_KEY_AUTH` is `true` |
+
+:::code language="json" source="~/azure-search-static-web-app/api/sample.local.settings.json" :::
+
+## Function: Search the catalog
+
+The [Search API](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/api/Search.cs) takes a search term and searches across the documents in the search index, returning a list of matches. Through the Suggest API, partial strings are sent to the search engine as the user types. The API suggests search terms, such as book titles and authors, based on documents in the search index and returns a small list of matches.
+
+The Azure function pulls in the search configuration information from the container environment, creates the Azure AI Search client, and fulfills the query.
 
 The search suggester, `sg`, is defined in the [schema file](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/bulk-insert/BookSearchIndex.cs) used during bulk upload.
 
 :::code language="csharp" source="~/azure-search-static-web-app/api/Search.cs" :::
 
-## Client: Search from the catalog
+To verify the function independently, call `/api/search` with a search term in the request body and confirm the response includes matching book documents, a total count, and facet values.
+
+## Client: Search the catalog
 
-Call the Azure Function in the React client at `\client\src\pages\Search\Search.jsx` with the following code to search for books. 
+The React client's Search page calls the `search` Azure function whenever the user enters a query, changes a facet filter, or moves to a new page of results. The client sends the search text, the current page's `skip` and `top` values, and any selected author or language filters in the POST body to `/api/search`. The function returns a list of matching book documents, a total count, and facet values, which the page uses to render the result list, pager, and facet filters. The following code in `\client\src\pages\Search\Search.jsx` builds that request and stores the response in component state:
 
-:::code language="csharp" source="~/azure-search-static-web-app/client/src/pages/Search/Search.jsx" :::
+:::code language="jsx" source="~/azure-search-static-web-app/client/src/pages/Search/Search.jsx" :::
+
+To verify this integration, enter a search term in the website's search bar and confirm that the result list, result count, and facets all update.
 
 ## Client: Suggestions from the catalog
 
-The Suggest function API is called in the React app at `\client\src\components\SearchBar\SearchBar.jsx` as part of the [Material UI's Autocomplete component](https://mui.com/material-ui/react-autocomplete/). This component uses the input text to search for authors and books that match the input text then displays those possible matches at selectable items in the drop-down list. 
+The Suggest function API is called in the React app at `\client\src\components\SearchBar\SearchBar.jsx` as part of the [Material UI Autocomplete component](https://mui.com/material-ui/react-autocomplete/). This component uses the input text to search for authors and books that match. It then displays those possible matches as selectable items in the dropdown list.
+
+:::code language="jsx" source="~/azure-search-static-web-app/client/src/components/SearchBar/SearchBar.jsx" :::
+
+To verify this integration, enter text in the website's search bar and confirm that matching book titles and authors appear in the autocomplete dropdown.
+
+## Function: Get specific document
 
-:::code language="csharp" source="~/azure-search-static-web-app/client/src/components/SearchBar/SearchBar.jsx" :::
+The [Document Lookup API](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/api/Lookup.cs) retrieves the full document for a single book after a user selects it from the search results. The function reads a book `id` from the request's query string, uses `SearchClientFactory` to create an authenticated `SearchClient`, and calls `GetDocumentAsync` to look up that key in the `good-books` index. It returns the resulting document wrapped in a `LookupOutput` object.
 
-## Azure Function: Get specific document 
+:::code language="csharp" source="~/azure-search-static-web-app/api/Lookup.cs" :::
 
-The [Document Lookup API](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/api/Lookup.cs) takes an ID and returns the document object from the Search Index. 
+To verify the Lookup function independently, call `/api/lookup` with a valid book `id` and confirm the response returns that book's full document.
 
-:::code language="csharp" source="~/azure-search-static-web-app/api/Lookup.cs"  :::
+## Client: Get specific document
 
-## Client: Get specific document 
+When a user selects a book from the search results, the Details page needs the complete document for that book, including fields not shown in the summary list. The Details page reads the book `id` from the route parameters and calls the Document Lookup API through `/api/lookup` when the component mounts. It stores the returned document in component state and renders it in the **Result** and **Raw Data** tabs. The following code in `\client\src\pages\Details\Details.jsx` performs this lookup during component initialization:
 
-This function API is called in the React app at `\client\src\pages\Details\Details.jsx` as part of component initialization:
+:::code language="jsx" source="~/azure-search-static-web-app/client/src/pages/Details/Details.jsx" :::
 
-:::code language="csharp" source="~/azure-search-static-web-app/client/src/pages/Details/Details.jsx"  :::
+To verify this integration, select a book from the search results and confirm that its details, including cover image, authors, and rating, appear on the Details page.
 
-## C# models to support function app
+## C# models that support the API
 
-The following models are used to support the functions in this app.
+The Azure Functions API and the bulk import project share a set of C# model classes. These classes define the request bodies the client sends, such as search text, paging values, and filters. They also define the response shapes the client expects, such as search results, facet values, and a single looked-up document. Keeping these models in one file ensures the search, suggest, and document lookup endpoints stay consistent with the React client's expectations. The following models, defined in `Models.cs`, support the functions in this app:
 
 :::code language="csharp" source="~/azure-search-static-web-app/api/Models.cs" :::
 
-## Next steps
+## Next step
 
-To continue learning more about Azure AI Search development, try this next tutorial about indexing:
+To continue learning about Azure AI Search development, try this next tutorial about indexing:
 
-* [Index Azure SQL data](search-indexer-tutorial.md)
+> [!div class="nextstepaction"]
+> [Tutorial: Index Azure SQL data using the .NET SDK](search-indexer-tutorial.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#アプリにおけるAzure AI Searchクエリ統合に関するチュートリアルの更新"
}
```

### Explanation
このコードの変更は、`articles/search/tutorial-csharp-search-query-integration.md`ファイルの内容を更新したもので、Azure AI SearchをC#アプリに統合する方法に関する情報が改善されています。主な変更点は、チュートリアルのタイトルと説明が明確化され、具体的な手順やコード例が強化されたことです。

具体的には、次のような内容が変更されました：
- 説明文が更新され、C#アプリにおける検索クエリの統合、管理されたIDの使用、検索リクエスト、提案、ドキュメントの取得に関する具体的な情報が明記されています。
- Azure SDKの認証方法に関して、管理されたIDをデフォルトの認証手段として明確に説明し、APIが環境変数から設定を自動的に取得する流れが具体的に記載されています。
- ローカル開発およびデプロイ時に使用する設定ファイルや環境変数についての指示が追加され、ユーザーがより簡単にローカル環境での準備を行えるようになっています。

さらに、提案機能や詳細ページのドキュメント取得についての具体的な実装方法が示されており、Reactクライアントとの統合についても言及されています。この更新により、C#開発者がAzure AI Searchを効果的に利用できるよう、詳細なガイダンスが提供されていると考えられます。


