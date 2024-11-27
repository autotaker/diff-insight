---
date: '2024-11-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9760ca7...MicrosoftDocs:796b906
summary: |-
  このレポートでは、Azure AI Searchに関連する重要な修正や新機能についてまとめています。主要なポイントとして、RBACを用いたキーなし接続のクイックスタートガイドが新たに追加され、目次に「キーなし認証情報」が加わり、ユーザーのナビゲーションが向上しています。また、新しい画像が追加されてビジュアルサポートが強化されています。

  特に、既存の機能やAPIに影響を与えるようなブレイキングチェンジはありませんが、用語やインターフェースの整合性が向上しました。タイトルや見出しの更新、画像の最新化、SQLデータベースに関する用語の一貫性改善も行われ、高い理解度を促進しています。

  全体として、これらの変更はユーザーの体験を向上させ、よりセキュアで一貫したAzure AI Searchの使用を可能にすることを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9760ca7...MicrosoftDocs:796b906){target="_blank"}

# ハイライト

この記事では、Azure AI Searchに関連するドキュメントにおける重要な修正や機能追加について説明します。以下はその主要なハイライトです：

## 新機能
- 「search-get-started-rbac.md」では、新たにRBAC（ロールベースのアクセス制御）を用いたキーなし接続のクイックスタートガイドが追加されました。
- 目次に「キーなし認証情報」が追加され、ユーザーのナビゲーションが向上しました。
- 「select-subscription-name.png」という新しい画像が追加され、RBACガイドがビジュアル的に補強されました。

## ブレイキングチェンジ
- 特に、既存の機能やAPIに影響を与えるようなブレイクングチェンジはありませんが、用語やインターフェースの一貫性がより整えられています。

## その他の更新
- タイトルおよび見出しの更新がなされ、内容がより具体的になり理解しやすくなっています。
- いくつかの画像が更新され、最新情報が反映されました。
- SQLデータベースのインデクシングに関するドキュメントで用語の一貫性が改善されました。

# インサイト

今回の更新は、Azure AI Search関連のドキュメントをよりユーザーに優しいものにすることを目的としています。具体的には、以下のポイントが注目に値します。

まず、ドキュメントの見出しやタイトルが変更されたことは、内容の精度を向上させ、ユーザーが意図をより理解しやすくするための重要なステップです。特に、開発者がアプリケーションでどのようにAzure AI Searchを使用するかを明確にすることで、学習曲線が和らぎます。

次に、RBACを使用したキーなし接続のクイックスタートガイドの追加は、Azureのセキュリティ機能をフルに活用したいユーザーに対して大きなメリットを提供します。このガイドには143行もの詳細な情報が含まれていますが、新規ユーザーにとっても分かりやすい内容となっています。セキュリティの向上と、APIキー不要での操作は、プロジェクト管理におけるリスク軽減の一助となるでしょう。

画像の更新と新規追加は、特に初心者にとって直感的に手順を理解する助けとなります。視覚的な情報補完は、ユーザーの理解を深めるために非常に有効です。

さらに、目次への「キーなし認証情報」の追加により、ドキュメント内での情報検索が簡便となり、ユーザーエクスペリエンスの向上につながっています。

全体として、これらの修正と機能追加は、Azure AI Searchを利用する開発者にとって、より一貫性があり、アクセスしやすく、そしてセキュアなソリューションを提供するものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [keyless-connections.md](#item-3f0d72) | minor update | キーのない接続に関する記事のタイトルと見出しの修正 | modified | 2 | 2 | 4 | 
| [select-subscription-name.png](#item-bb6978) | new feature | RBACに関する情報を強化する画像の追加 | added | 0 | 0 | 0 | 
| [search-security-enable-roles.png](#item-7cd66f) | minor update | RBACのセキュリティに関する画像の更新 | modified | 0 | 0 | 0 | 
| [search-get-started-rbac.md](#item-9d96c1) | new feature | RBACを用いたキーなし接続のクイックスタートガイドの追加 | added | 143 | 0 | 143 | 
| [search-how-to-index-sql-database.md](#item-86d873) | minor update | SQLデータベースのインデクシング方法に関するドキュメントの修正 | modified | 2 | 2 | 4 | 
| [toc.yml](#item-c4768f) | minor update | 目次にキーなし認証情報を追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/search/keyless-connections.md{#item-3f0d72}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Use keyless connections with Azure AI Search
+title: Use keyless connections in search apps
 description: Use keyless connections with an Azure Identity library for Microsoft Entra ID authentication and authorization with Azure AI Search.
 ms.topic: how-to
 ms.date: 10/30/2024
@@ -9,7 +9,7 @@ ms.custom: devx-track-dotnet, devx-track-extended-java, devx-track-js, devx-trac
 #customer intent: As a developer, I want to use keyless connections so that I don't leak secrets.
 ---
 
-# Use Azure AI Search without keys 
+# Connect your app to Azure AI Search using identities
 
 In your application code, you can set up a keyless connection to Azure AI Search that uses Microsoft Entra ID and roles for authentication and authorization. Application requests to most Azure services must be authenticated with keys or keyless connections. Developers must be diligent to never expose the keys in an unsecure location. Anyone who gains access to the key is able to authenticate to the service. Keyless authentication offers improved management and security benefits over the account key because there's no key (or connection string) to store.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "キーのない接続に関する記事のタイトルと見出しの修正"
}
```

### Explanation
この変更では、Azure AI Searchの「キーのない接続」に関するドキュメントのタイトルと見出しが修正されました。具体的には、タイトルが「Use keyless connections with Azure AI Search」から「Use keyless connections in search apps」に変更され、見出しも「Use Azure AI Search without keys」から「Connect your app to Azure AI Search using identities」に更新されました。これにより、ドキュメントの内容がより具体的で明確になり、開発者がアプリケーションでの接続を理解しやすくなっています。また、説明文は、Microsoft Entra IDを使用した認証と承認に関する情報を強化しています。全体として、この記事はより正確な情報とユーザー意図を反映するように改訂されました。

## articles/search/media/search-get-started-rbac/select-subscription-name.png{#item-bb6978}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "RBACに関する情報を強化する画像の追加"
}
```

### Explanation
この変更では、RBAC（ロールベースのアクセス制御）に関連する「select-subscription-name.png」という画像が新たに追加されました。この画像は、Azure AI Searchの「Get Started」ガイドにおいて、サブスクリプション名の選択方法を視覚的に示すために使用されることが期待されます。画像の追加によって、ユーザーは手順をより理解しやすくなり、操作を効果的に行えるようになります。新しいビジュアルコンテンツは、特に初心者にとって、情報をより消化しやすくするのに役立ちます。

## articles/search/media/search-security-rbac/search-security-enable-roles.png{#item-7cd66f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACのセキュリティに関する画像の更新"
}
```

### Explanation
この変更では、RBAC（ロールベースのアクセス制御）に関する「search-security-enable-roles.png」という画像が修正されました。この画像は、Azure AI Searchにおいて役割を有効にする方法についての情報を視覚的に提供しています。具体的には、画像の内容は変更されていないものの、画像が更新されることで、より最新の情報やデザインが反映されている可能性があります。このような更新は、ユーザーが最新のインターフェースや機能を理解するのに役立ち、実際の操作における混乱を軽減するために重要です。

## articles/search/search-get-started-rbac.md{#item-9d96c1}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,143 @@
+---
+title: Quickstart keyless connection
+titleSuffix: Azure AI Search
+description: In this quickstart, learn how to switch from API keys to Microsoft Entra identities and role-based access control (RBAC).
+author: HeidiSteen
+ms.author: heidist
+ms.service: azure-ai-search
+
+ms.topic: quickstart
+ms.date: 11/26/2024
+---
+
+# Quickstart: Connect without keys
+
+Configure Azure AI Search to use Microsoft Entra ID authentication and roles. Connect from your local system, running Jupyter notebooks, or using a REST client.
+
+If you stepped through other quickstarts that connect using API keys, this quickstart shows you how to switch to identity-based authentication so that you can avoid hard-coded API keys in your example code.
+
+## Prerequisites
+
+- An Azure subscription. [Create one for free](https://azure.microsoft.com/free/).
+
+- [Azure AI Search](search-create-service-portal.md), any region or tier, but you need Basic or higher to configure a system-assigned managed identity for Azure AI Search.
+
+- A command line tool, such as the [Azure CLI](/cli/azure/install-azure-cli).
+
+## Step 1: Set up your Azure subscription and tenant
+
+This step is necessary if you have more than one subscription or tenant.
+
+1. Get the Azure subscription and tenant for your search service:
+
+   1. Sign into the Azure portal and navigate to your search service.
+
+   1. Notice the subscription name and ID in **Overview** > **Essentials**.
+
+   1. Select the subscription name to view the parent management group (tenant ID).
+
+      :::image type="content" source="media/search-get-started-rbac/select-subscription-name.png" lightbox="media/search-get-started-rbac/select-subscription-name.png" alt-text="Screenshot of the portal page providing the subscription name":::
+
+1. Identify the active Azure subscription and tenant on your local device:
+
+   `az account show`
+
+1. Set your Azure subscription to the subscription and tenant:
+
+   `az account set --subscription <your-subscription-id>`
+
+   `az login --tenant <your-tenant-id>`
+
+1. Check your tenant ID:
+
+   `az account show --query tenantId --output tsv`
+
+## Step 2: Configure Azure AI Search for Microsoft Entra ID authentication
+
+1. Sign in to the Azure portal and navigate to your Azure AI Search service.
+
+1. Enable role-based access control (RBAC):
+
+   1. Go to **Settings** > **Keys**.
+
+   1. Choose **Role-based control** or **Both** if you need time to transition clients to role-based access control1.
+
+1. Assign roles in the Azure portal:
+
+   1. Navigate to your search service.
+
+   1. Select **Access Control (IAM)** in the left navigation pane.
+
+   1. Select **+ Add** > **Add role assignment**.
+
+   1. Choose a role (Search Service Contributor, Search Index Data Contributor, Search Index Data Reader) and assign it to your Microsoft Entra user or group identity. These three roles provide the full set of permissions for creating, loading, and querying objects on Azure AI Search. For more information, see [Connect using roles](search-security-rbac.md).
+
+## Step 3: Connect from your local system
+
+### Using Python and Jupyter notebooks
+
+1. Install the Azure Identity and Azure Search libraries:
+
+    ```python
+    pip install azure-identity azure-search-documents
+    ```
+
+1. Authenticate and connect to Azure AI Search:
+
+    ```python
+    from azure.identity import DefaultAzureCredential
+    from azure.search.documents import SearchClient
+    
+    service_endpoint = "https://<your-search-service-name>.search.windows.net"
+    index_name = "<your-index-name>"
+    
+    credential = DefaultAzureCredential()
+    client = SearchClient(endpoint=service_endpoint, index_name=index_name, credential=credential)
+    
+    results = client.search("search text")
+    for result in results:
+        print(result)
+    ```
+
+### Using a REST client
+
+Several quickstarts and tutorials use a REST client, such as Visual Studio Code with the REST extension. Here's how you connect to Azure AI Search from Visual Studio Code.
+
+1. Get a personal identity token:
+
+   `az account get-access-token --resource https://<your-search-service-name>.search.windows.net`
+
+1. Extract the token from the output:
+
+   `TOKEN=$(az account get-access-token --resource https://<your-search-service-name>.search.windows.net --query accessToken --output tsv)`
+
+1. Provide the token in a request header:
+
+   `az rest --method get --url "https://<your-search-service-name>.search.windows.net/indexes/<your-index-name>/docs?api-version=2021-04-30-Preview&search=*" --headers "Authorization=Bearer $TOKEN"`
+
+1. Specify the authorization bearer token in a REST call:
+
+   ```REST
+    POST https://{{baseUrl}}/indexes/{{index-name}}/docs/search?api-version=2024-07-01 HTTP/1.1
+      Content-type: application/json
+      Authorization: Bearer {{token}}
+    
+        {
+             "queryType": "simple",
+             "search": "motel",
+             "filter": "",
+             "select": "HotelName,Description,Category,Tags",
+             "count": true
+         }
+   ```
+
+## Additional configuration
+
+Configure a managed identity for outbound connections:
+
+- [Configure a system-assigned or user-assigned managed identity](search-howto-managed-identities-data-sources.md) for your search service.
+- [Use role assignments](keyless-connections.md) to authorize access to other Azure resources.
+
+Network access configuration:
+
+- [Set inbound rules](service-configure-firewall.md) to accept or reject requests to Azure AI Search based on IP address.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "RBACを用いたキーなし接続のクイックスタートガイドの追加"
}
```

### Explanation
この変更では、RBAC（ロールベースのアクセス制御）を使用したキーなし接続に関する新しいクイックスタートガイドが追加されました。このガイドは、Microsoft Entra IDを使用した認証方法への切り替えを学ぶためのもので、APIキーの使用を回避する方法を具体的に説明しています。143行の詳細な内容が含まれ、Azure AI Searchへの接続手順が包括的にカバーされています。

ガイドは、Azureサブスクリプションのセットアップ、Microsoft Entra ID認証の構成、PythonやRESTクライアントを使用した接続方法に関するステップバイステップの手順を提供しています。また、追加の構成やネットワークアクセスに関する情報も含まれており、ユーザーがAzureリソースへのアクセスを適切に管理できるよう促しています。この新しいリソースは、特に新しいユーザーや役割に基づくアクセス管理を取り入れたい開発者にとって非常に重要です。

## articles/search/search-how-to-index-sql-database.md{#item-86d873}

<details>
<summary>Diff</summary>
````diff
@@ -122,7 +122,7 @@ You can use either the **Import data** wizard or **Import and vectorize data** w
 
 1. Specify an authentication method, either a SQL Server login defined during server setup, or a managed identity.
 
-   If you [configure Azure AI Search to use a managed identity](search-howto-managed-identities-data-sources.md), and you create a role assignment on the database server that grants **SQL Server Contributor** or **SQL Server DB Contributor** permissions to the identity, your indexer can connect to Azure SQL using Microsoft Entra ID and roles.
+   If you [configure Azure AI Search to use a managed identity](search-howto-managed-identities-data-sources.md), and you create a role assignment on the database server that grants **SQL Server Contributor** or **SQL DB Contributor** permissions to the identity, your indexer can connect to Azure SQL using Microsoft Entra ID and roles.
 
 1. For the **Import and vectorize data** wizard, you can specify options for change and deletion tracking.
 
@@ -280,7 +280,7 @@ An indexer runs automatically when it's created. You can prevent this by setting
 
 ## Check indexer status
 
-To monitor the indexer status and execution history, check the indexer execution history in the Azure portal, or send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) REST APIrequest
+To monitor the indexer status and execution history, check the indexer execution history in the Azure portal, or send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) REST API request
 
 ### [**Portal**](#tab/portal-check-indexer)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SQLデータベースのインデクシング方法に関するドキュメントの修正"
}
```

### Explanation
この変更では、「search-how-to-index-sql-database.md」ドキュメントの一部が修正され、SQLデータベースインデクシングに関する情報が明確化されました。具体的には、ロール割り当ての名称が「SQL Server DB Contributor」から「SQL DB Contributor」に修正され、これによりドキュメント内の用語が一貫性を持つようになりました。

さらに、最終行ではREST APIリクエストの説明においてスペースが追加され、読みやすさが向上しています。この修正により、ユーザーがAzure SQLとの接続を設定する際の手順がより明確になり、インデクサーのステータスを監視する方法についての情報もより理解しやすくなっています。これらの変更は、特に新たにAzure AI Searchを利用しようとする開発者にとって、よりスムーズな理解を助けるものです。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -26,6 +26,8 @@ items:
     href: search-get-started-semantic.md
   - name: Chat with your data 
     href: /azure/ai-services/openai/use-your-data-quickstart?context=/azure/search/context/context
+  - name: Keyless authentication
+    href: search-get-started-rbac.md
   - name: Portal
     items:
     - name: Keyword search wizard
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次にキーなし認証情報を追加"
}
```

### Explanation
この変更では、目次ファイル「toc.yml」に新しい項目「キーなし認証」が追加されました。この新しい項目は、RBAC（ロールベースのアクセス制御）を使用してキーなしでAzure AI Searchに接続する手法を紹介するガイド「search-get-started-rbac.md」へのリンクを提供しています。

具体的には、既存の「Chat with your data」という項目の後にこの新しい項目が追加され、ユーザーがアクセスしやすくなっています。この更新により、ユーザーはキーなし認証の設定方法についての情報により簡単にアクセスできるようになり、Azure AI Searchを活用する際の選択肢が広がります。全体として、この修正はドキュメントの可用性を向上させ、ユーザー体験を向上させるものです。


