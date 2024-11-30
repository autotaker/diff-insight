---
date: '2024-11-30'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b20ad3b...MicrosoftDocs:51f1731
summary: この更新は、Azure AI Searchの役割ベースのアクセス制御（RBAC）のガイドに対するマイナーな修正を行っています。具体的には、日付の更新や文言の調整が行われており、特にユーザーが手順を誤解しないように説明が改善されています。新しい機能は追加されていませんが、ガイド内の日付が2024年11月28日から2024年11月29日に変更され、一部の文言も明確にされています。また、RESTクライアントでの接続方法の手順が整理され、わかりやすいサンプルURLやトークンの指示が追加されています。これにより、Azure
  AI Searchの利用がより効果的かつ安全に行えるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b20ad3b...MicrosoftDocs:51f1731){target="_blank"}

# ハイライト
この更新はAzure AI Searchの役割ベースのアクセス制御（RBAC）に関するガイドに対するマイナーな修正を行っており、特に日付の更新と文言の調整が含まれています。

## 新機能
- 特に新しい機能は追加されていませんが、既存の説明がより理解しやすくなるよう改善されています。

## 破壊的な変更
- 破壊的な変更は特にありません。

## その他の更新
- ガイド内の日付が2024年11月28日から2024年11月29日に更新されました。
- 一部の文言が明確かつ簡潔になるよう修正されました。
- RESTクライアントでの接続方法の手順が整理され、サンプルURLやトークンの挿入指示がわかりやすくなりました。

# インサイト
このコードの変更では、Azure AI Searchを活用する開発者向けドキュメントの改善を目的としています。役割ベースのアクセス制御（RBAC）は、Azureのセキュリティ機能の一部として重要な位置を占めており、明確に理解することが必要です。今回の更新では、日付変更や文言の微調整を通じて、ユーザーが求める正確で明快な情報提供を実現しています。

特に、ユーザーが手順を誤解することなく実施できるような説明が行われるようになりました。RESTクライアント使用時の接続設定において間違いが起きやすい点を解消するため、手順を整理し、具体的な例や指示がさらに明確に示されています。これにより、ドキュメント全体の品質が向上し、ユーザーはAzure AI Searchをより効果的かつ安全に使用できるようになるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-rbac.md](#item-9d96c1) | minor update | 検索の開始：RBACに関するガイドの更新 | modified | 20 | 11 | 31 | 


# Modified Contents
## articles/search/search-get-started-rbac.md{#item-9d96c1}

<details>
<summary>Diff</summary>
````diff
@@ -7,26 +7,26 @@ ms.author: heidist
 ms.service: azure-ai-search
 
 ms.topic: quickstart
-ms.date: 11/28/2024
+ms.date: 11/29/2024
 ---
 
 # Quickstart: Connect without keys
 
-Configure Azure AI Search to use Microsoft Entra ID authentication and role-based access control (RBAC). Connect from your local system using your personal identity, using Jupyter notebooks or a REST client to interact with your search service.
+Configure Azure AI Search to use Microsoft Entra ID authentication and role-based access control (RBAC). Connect from your local system with your personal identity, using Jupyter notebooks or a REST client to interact with your search service.
 
 If you stepped through other quickstarts that connect using API keys, this quickstart shows you how to switch to identity-based authentication so that you can avoid hard-coded keys in your example code.
 
 ## Prerequisites
 
 - An Azure subscription. [Create one for free](https://azure.microsoft.com/free/).
 
-- [Azure AI Search](search-create-service-portal.md), any region or tier, but you need Basic or higher to configure a system-assigned managed identity for Azure AI Search.
+- [Azure AI Search](search-create-service-portal.md), any region or tier, but you need Basic or higher to configure a managed identity for Azure AI Search.
 
 - A command line tool, such as the [Azure CLI](/cli/azure/install-azure-cli).
 
 ## Step 1: Get your Azure subscription and tenant IDs
 
-This step is necessary if you have more than one subscription or tenant.
+You need this step if you have more than one subscription or tenant.
 
 1. Get the Azure subscription and tenant for your search service:
 
@@ -38,13 +38,13 @@ This step is necessary if you have more than one subscription or tenant.
 
       :::image type="content" source="media/search-get-started-rbac/select-subscription-name.png" lightbox="media/search-get-started-rbac/select-subscription-name.png" alt-text="Screenshot of the portal page providing the subscription name":::
 
-1. Switching to your local device and a command prompt, identify the active Azure subscription and tenant:
+1. You now know which subscription and tenant Azure AI Search is under. Switching to your local device and a command prompt, identify the active Azure subscription and tenant on your device:
 
    ```azurecli
    az account show
    ```
 
-1. If the active subscription is different from the information obtained in the previous step, change the subscription ID. Next, sign in to Azure using the tenant ID also found in the previous step:
+1. If the active subscription and tenant differ from the information obtained in the previous step, change the subscription ID. Next, sign in to Azure using the tenant ID also found in the previous step:
 
    ```azurecli
     az account set --subscription <your-subscription-id>
@@ -122,24 +122,33 @@ az login
 
 ### Using a REST client
 
-Several quickstarts and tutorials use a REST client, such as Visual Studio Code with the REST extension. Here's how you connect to Azure AI Search from Visual Studio Code.
+[Several quickstarts](search-get-started-vector.md) and tutorials use a REST client, such as Visual Studio Code with the REST extension. Here's how you connect to Azure AI Search from Visual Studio Code.
 
 1. Get a personal identity token:
 
-   `az account get-access-token --scope https://search.azure.com/.default`
+   ```azurecli
+   az account get-access-token --scope https://search.azure.com/.default
+   ```
+
+1. Set variables used for the connection, pasting the full search service endpoint and the token you got in the previous step.
+
+    ```http
+    @baseUrl = PUT-YOUR-SEARCH-SERVICE-URL-HERE
+    @token = PUT-YOUR-PERSONAL-IDENTITY-TOKEN-HERE
+    ```
 
-1. Extract the token from the output:
+<!-- 1. Extract the token from the output:
 
    `TOKEN=$(az account get-access-token --resource https://<your-search-service-name>.search.windows.net --query accessToken --output tsv)`
 
 1. Provide the token in a request header:
 
-   `az rest --method get --url "https://<your-search-service-name>.search.windows.net/indexes/<your-index-name>/docs?api-version=2021-04-30-Preview&search=*" --headers "Authorization=Bearer $TOKEN"`
+   `az rest --method get --url "https://<your-search-service-name>.search.windows.net/indexes/<your-index-name>/docs?api-version=2021-04-30-Preview&search=*" --headers "Authorization=Bearer $TOKEN"` -->
 
 1. Specify the authorization bearer token in a REST call:
 
    ```REST
-    POST https://{{baseUrl}}/indexes/{{index-name}}/docs/search?api-version=2024-07-01 HTTP/1.1
+    POST https://{{baseUrl}}/indexes/hotels-sample-index/docs/search?api-version=2024-07-01 HTTP/1.1
       Content-type: application/json
       Authorization: Bearer {{token}}
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索の開始：RBACに関するガイドの更新"
}
```

### Explanation
このコードの変更では、Azure AI Searchの役割ベースのアクセス制御（RBAC）に関する「検索の開始」ガイドのいくつかの文言が修正されました。具体的には、日付が2024年11月28日から2024年11月29日に更新されたほか、一部の文がより明確に、または簡潔に表現されています。例えば、「このステップは必要です」という表現が「このステップは必要です」と変更され、読みやすさが向上しました。また、RESTクライアントでの接続方法に関する手順も整理され、サンプルURLやトークンを挿入する際に必要な指示がより分かりやすくなっています。

全体的に、修正の目的は文書の明確性を向上させ、ユーザーがAzure AI Searchを使用する際のガイダンスをより効果的にすることです。


