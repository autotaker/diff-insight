---
date: '2024-12-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fffd4c5...MicrosoftDocs:3b6e85f
summary: このコード差分では、Azure AI Searchに関連する複数のドキュメントが更新されました。主な変更点は、デモサイト情報の更新、RBACのクイックスタートガイドの修正、REST
  APIクイックスタートガイドの改善、インデクサートラブルシューティングガイドのリンク更新です。新しい機能は追加されていませんが、情報の鮮度と正確性を高めるための小規模な調整が行われました。全体として、これらの改善により、ユーザーがAzure
  AI Searchを効果的に活用できるように文書が整備されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fffd4c5...MicrosoftDocs:3b6e85f){target="_blank"}

# ハイライト

このコード差分では、Azure AI Searchに関連した複数のドキュメントファイルの更新が行われました。主な変更点は以下の通りです。

- デモサイト情報の更新
- ロールベースアクセス制御（RBAC）のクイックスタートガイドの修正
- REST APIクイックスタートガイドの改善
- インデクサートラブルシューティングガイドのリンク更新

## 新しい機能

- 特に新しい機能の追加はありませんが、既存の文書が更新されています。

## 破壊的変更

- 破壊的変更は特に含まれていません。

## その他の更新

- ドキュメント内の日付やリンクの更新、新しい注意事項の追加など、情報の鮮度と正確性を高めるための小規模な調整が行われています。

# インサイト

この差分では、Azure AI Search関連のドキュメントに対する複数のマイナーな更新が行われています。重要な更新点として、最新のデモ情報やクイックスタートガイドの内容がより分かりやすく、実用的になるよう改善されています。

例えば、デモサイトの情報更新により、ユーザーは簡単に最新のデモにアクセスでき、Azure AI Searchの最新機能を体験することが可能になります。また、RBACクイックスタートガイドの修正により、Azure CLIだけでなくPowerShellやBashを用いた手順が明確化され、実際の開発環境とよりマッチした内容となっています。

REST APIに関するガイドでは、トークン使用時の注意点が追加され、認証エラーが発生した際の具体的な解決方法が示されています。これにより、API利用時のトラブルシューティングが容易になり、開発者はより快適にAzureサービスを使用することができます。

さらに、インデクサートラブルシューティングガイドにおいて、Azure Cosmos DB関連のリンクが更新され、ユーザーは最新の手順に従って問題を解決できるようになりました。これらの変更は全体として、ユーザーがAzure AI Searchを最大限に活用するための文書整備を目的としています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [resource-demo-sites.md](#item-af1bd0) | minor update | デモサイト情報の更新 | modified | 2 | 2 | 4 | 
| [search-get-started-rbac.md](#item-9d96c1) | minor update | RBACのクイックスタートガイドの更新 | modified | 10 | 18 | 28 | 
| [search-get-started-rest.md](#item-0df9d5) | minor update | REST APIクイックスタートガイドの更新 | modified | 5 | 3 | 8 | 
| [search-indexer-troubleshooting.md](#item-087365) | minor update | インデクサートラブルシューティングガイドのリンク更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/resource-demo-sites.md{#item-af1bd0}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 10/07/2024
+ms.date: 12/02/2024
 ---
 
 # Demos - Azure AI Search
@@ -20,5 +20,5 @@ The Azure AI Search currently builds and hosts the following demos.
 
 | Demo name | Description | Source code |
 |-----------|------------ |-------------|
-| [Chat with your data](https://entgptsearch.azurewebsites.net/) | An Azure web app that uses ChatGPT in Azure OpenAI with fictitious health plan data in a search index. | [https://github.com/Azure-Samples/azure-search-openai-demo/](https://github.com/Azure-Samples/azure-search-openai-demo/)  |
+| [Chat with your data](https://aka.ms/officialazsdemo) | An Azure web app that uses ChatGPT in Azure OpenAI with fictitious health plan data in a search index. | [https://github.com/Azure-Samples/azure-search-openai-demo/](https://github.com/Azure-Samples/azure-search-openai-demo/)  |
 | [Semantic ranking for retail](https://brave-meadow-0f59c9b1e.1.azurestaticapps.net/) | Web app for a fictitious online retailer, "Terra" | Not available |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デモサイト情報の更新"
}
```

### Explanation
この変更は、Azure AI Search関連のデモサイト情報を更新するもので、具体的にはデモのリンクと日付が修正されています。具体的には、「ms.date」の値が2024年10月7日から2024年12月2日に変更され、デモリンク「Chat with your data」が新しいURL（https://aka.ms/officialazsdemo）に更新されました。これにより、ユーザーが最新のデモに簡単にアクセスできるようになります。

## articles/search/search-get-started-rbac.md{#item-9d96c1}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.date: 11/29/2024
 
 # Quickstart: Connect without keys
 
-Configure Azure AI Search to use Microsoft Entra ID authentication and role-based access control (RBAC). Connect from your local system with your personal identity, using Jupyter notebooks or a REST client to interact with your search service.
+Configure Azure AI Search to use Microsoft Entra ID authentication and role-based access control (RBAC) so that you can connect from your local system with your personal identity, using Jupyter notebooks or a REST client to interact with your search service.
 
 If you stepped through other quickstarts that connect using API keys, this quickstart shows you how to switch to identity-based authentication so that you can avoid hard-coded keys in your example code.
 
@@ -22,7 +22,7 @@ If you stepped through other quickstarts that connect using API keys, this quick
 
 - [Azure AI Search](search-create-service-portal.md), any region or tier, but you need Basic or higher to configure a managed identity for Azure AI Search.
 
-- A command line tool, such as the [Azure CLI](/cli/azure/install-azure-cli).
+- A command line tool, such as PowerShell or Bash, and the [Azure CLI](/cli/azure/install-azure-cli).
 
 ## Step 1: Get your Azure subscription and tenant IDs
 
@@ -38,13 +38,13 @@ You need this step if you have more than one subscription or tenant.
 
       :::image type="content" source="media/search-get-started-rbac/select-subscription-name.png" lightbox="media/search-get-started-rbac/select-subscription-name.png" alt-text="Screenshot of the portal page providing the subscription name":::
 
-1. You now know which subscription and tenant Azure AI Search is under. Switching to your local device and a command prompt, identify the active Azure subscription and tenant on your device:
+1. You now know which subscription and tenant Azure AI Search is under. Switch to your local device and a command prompt, and identify the active Azure subscription and tenant on your device:
 
    ```azurecli
    az account show
    ```
 
-1. If the active subscription and tenant differ from the information obtained in the previous step, change the subscription ID. Next, sign in to Azure using the tenant ID also found in the previous step:
+1. If the active subscription and tenant differ from the information obtained in the previous step, change the subscription ID. Next, sign in to Azure using the tenant ID that you found in the previous step:
 
    ```azurecli
     az account set --subscription <your-subscription-id>
@@ -110,12 +110,12 @@ az login
     from azure.search.documents import SearchClient
     
     service_endpoint = "https://<your-search-service-name>.search.windows.net"
-    index_name = "<your-index-name>"
+    index_name = "hotels-sample-index"
     
     credential = DefaultAzureCredential()
     client = SearchClient(endpoint=service_endpoint, index_name=index_name, credential=credential)
     
-    results = client.search("search text")
+    results = client.search("beach access")
     for result in results:
         print(result)
     ```
@@ -127,24 +127,16 @@ az login
 1. Get a personal identity token:
 
    ```azurecli
-   az account get-access-token --scope https://search.azure.com/.default
+   az account get-access-token --scope https://search.azure.com/.default --query accessToken --output tsv
    ```
 
-1. Set variables used for the connection, pasting the full search service endpoint and the token you got in the previous step.
+1. Set variables used for the connection, pasting the full search service endpoint and the token you got in the previous step. Make sure neither value is quote-enclosed.
 
-    ```http
+    ```REST
     @baseUrl = PUT-YOUR-SEARCH-SERVICE-URL-HERE
     @token = PUT-YOUR-PERSONAL-IDENTITY-TOKEN-HERE
     ```
 
-<!-- 1. Extract the token from the output:
-
-   `TOKEN=$(az account get-access-token --resource https://<your-search-service-name>.search.windows.net --query accessToken --output tsv)`
-
-1. Provide the token in a request header:
-
-   `az rest --method get --url "https://<your-search-service-name>.search.windows.net/indexes/<your-index-name>/docs?api-version=2021-04-30-Preview&search=*" --headers "Authorization=Bearer $TOKEN"` -->
-
 1. Specify the authorization bearer token in a REST call:
 
    ```REST
@@ -154,7 +146,7 @@ az login
     
         {
              "queryType": "simple",
-             "search": "motel",
+             "search": "beach access",
              "filter": "",
              "select": "HotelName,Description,Category,Tags",
              "count": true
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchのロールベースアクセス制御（RBAC）を使用した接続に関するクイックスタートガイドを更新するものです。主な変更点には、接続手順の一部の文言の修正や、説明の明確化が含まれています。具体的には、Azure CLIに加えてPowerShellやBashが指定された点や、検索サービスのインデックス名が「<your-index-name>」から「hotels-sample-index」に変更され、検索テキストも「search text」から「beach access」に更新されました。また、アクセストークン取得のコマンドにおいて、`--query accessToken --output tsv`オプションが追加され、トークン取得の手順が明確になっています。これにより、ユーザーはより効果的にAzure AI Searchの機能を活用できるようになります。

## articles/search/search-get-started-rest.md{#item-0df9d5}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: quickstart
 ms.devlang: rest-api
-ms.date: 10/31/2024
+ms.date: 11/29/2024
 ms.custom:
   - mode-api
   - ignite-2023
@@ -116,7 +116,7 @@ If you're not familiar with the REST client for Visual Studio Code, this section
 
 1. Open or create a new file named with either a `.rest` or `.http` file extension.
 
-1. Paste in the following example if you're using API keys. Replace the `@baseUrl` and `@apiKey` placeholders with the values you copied earlier.
+1. Paste in the following example if you're using API keys. Replace the `@baseUrl` and `@apiKey` placeholders with the values you copied earlier, without quotes.
 
    ```http
    @baseUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
@@ -128,7 +128,7 @@ If you're not familiar with the REST client for Visual Studio Code, this section
       api-key: {{apiKey}}
     ```
 
-1. Or, paste in this example if your using roles. Replace the `@baseUrl` and `@token` placeholders with the values you copied earlier.
+1. Or, paste in this example if your using roles. Replace the `@baseUrl` and `@token` placeholders with the values you copied earlier, without quotes.
 
    ```http
    @baseUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
@@ -144,6 +144,8 @@ If you're not familiar with the REST client for Visual Studio Code, this section
 
    :::image type="content" source="media/search-get-started-rest/rest-client-request-setup.png" lightbox="media/search-get-started-rest/rest-client-request-setup.png" alt-text="Screenshot that shows a REST client configured for a search service request.":::
 
+    If you get `WWW-Authenticate: Bearer realm="Azure Cognitive Search" error="invalid_token" error_description="Authentication token failed validation."`, remove the quotes around the token, save the file, and retry your request.
+
     Key points:
   
     - Parameters are specified by using an `@` prefix.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Azure AI SearchのREST APIに関するクイックスタートガイドを更新したもので、主に利用者への注意点や操作手順の明確化が含まれています。変更内容には、「ms.date」の更新があり、2024年10月31日から2024年11月29日に変更されています。また、RESTクライアントでのAPIキーやトークンの使用に際して、プレースホルダーを値で置き換える際に「引用符なしで」という注意喚起が追加されました。

更に、「WWW-Authenticate」エラーに関する新しい情報が追加されており、トークンの周りの引用符を削除して再試行するよう促しています。これにより、ユーザーは認証関連のエラーを回避するための具体的なアドバイスを得ることができ、よりスムーズにAPIを利用できるようになります。

## articles/search/search-indexer-troubleshooting.md{#item-087365}

<details>
<summary>Diff</summary>
````diff
@@ -38,7 +38,7 @@ There are two options for allowing indexers to access these resources in such an
 * Configure an inbound rule for the IP address of your search service and the IP address range of `AzureCognitiveSearch` [service tag](/azure/virtual-network/service-tags-overview#available-service-tags). Details for configuring IP address range restrictions for each data source type can be found from the following links:
 
   * [Azure Storage](/azure/storage/common/storage-network-security#grant-access-from-an-internet-ip-range)
-  * [Azure Cosmos DB](/azure/storage/common/storage-network-security#grant-access-from-an-internet-ip-range)
+  * [Azure Cosmos DB](/azure/cosmos-db/how-to-configure-firewall)
   * [Azure SQL](/azure/azure-sql/database/firewall-configure#create-and-manage-ip-firewall-rules)
 
 * As a last resort or as a temporary measure, disable the firewall by allowing access from **All Networks**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサートラブルシューティングガイドのリンク更新"
}
```

### Explanation
この変更は、Azure AI Searchのインデクサートラブルシューティングガイドにおけるリンクの更新を含んでいます。具体的には、Azure Cosmos DBに関連するリンクが、以前の「Azure Storage」のセクション内から新しいURL「/azure/cosmos-db/how-to-configure-firewall」に変更されました。これにより、ユーザーはAzure Cosmos DBのファイアウォール設定に関する最新の情報にアクセスできるようになります。このような更新は、ユーザーが正確かつ最新の情報を基に問題解決を行う手助けとなります。


