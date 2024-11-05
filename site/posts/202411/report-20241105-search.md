---
date: '2024-11-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8de853c...MicrosoftDocs:c2df9dc
summary: このコード差分では、Azure AI Searchに関するドキュメントに対する軽微な更新、新機能追加、及び修正が行われました。主な変更点には、RBACアクセス制御の画像追加、`pip`コマンドのスペルミス修正、Java用ライブラリのバージョン更新、名称の変更（「Azure
  Identity」から「Microsoft Entra ID」）、および同義語インデックス作成に関するAPIメソッドの修正が含まれています。これらの変更により、ドキュメントの信頼性と情報の正確性が向上し、ユーザーが最新の機能やセキュリティパッチを利用できるようになっています。全体として、利便性と信頼性の向上を目指したアップデートです。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8de853c...MicrosoftDocs:c2df9dc){target="_blank"}

# ハイライト
このコード差分では、Azure AI Searchに関するドキュメントに対する一連の軽微な更新、新機能追加、及び修正が行われています。主な変更点は以下の通りです：

- **新機能**: AzureポータルでのRBACアクセス制御に関する画像が追加されました。
- **バグ修正**: `pip`コマンドのスペルミスが修正されました。
- **依存関係更新**: Java用ライブラリのバージョンが最新のものに更新されました。
- **名称変更**: 「Azure Identity」から「Microsoft Entra ID」への名称変更が行われました。
- **APIメソッド修正**: 同義語インデックス作成のHTTPメソッドが`POST`から`PUT`に修正されました。

## 新機能
- RBACに関連するポータルアクセス制御の画像が追加され、視覚的なガイドが提供されるようになりました。

## バグ修正
- `pip install`コマンドのスペルミスを修正することで、正しい環境設定の妨げとなるエラーを防止しました。

## その他の更新
- ドキュメント内の依存関係バージョンや内容の明確化、最新名称の反映などの小規模な更新が複数行われています。

# インサイト
今回の変更では、Azure AI Searchに関連するドキュメントの信頼性と情報の正確性が向上しています。

Javaクイックスタートではライブラリのバージョンが更新され、最新の機能に対応するようになりました。これにより、開発者は最新のセキュリティパッチや機能を利用できます。

キーなし接続のドキュメントでは名称変更や認証プロセスの明示などが行われ、ユーザーが最新の認証メソッドを適用できるようになっています。また、RBACや認証に関する情報が強化され、具体的なツールや手順が示されることで、ユーザーはより具体的かつ安全にAzure AI Searchを利用可能です。

さらに、APIリクエストに関する修正は、誤った情報が印刷されていた場合の混乱を防ぎ、ユーザーがサービスを通して一貫した性能を享受できることを保証します。

全体としてこの更新は、Azure AI Searchを利用するユーザーにとって利便性と信頼性の向上を意図しており、情報の正確さやUIの改善を通じて価値ある開発体験を提供することを狙っています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [java.md](#item-bd5406) | minor update | Java クイックスタートの更新 | modified | 3 | 3 | 6 | 
| [keyless-connections.md](#item-3f0d72) | minor update | キーなし接続に関するドキュメントの更新 | modified | 15 | 18 | 33 | 
| [portal-access-control.png](#item-89ca91) | new feature | ポータルアクセス制御の画像追加 | added | 0 | 0 | 0 | 
| [search-get-started-rag.md](#item-05ff0e) | bug fix | パッケージインストールコマンドの修正 | modified | 2 | 2 | 4 | 
| [search-get-started-text.md](#item-935941) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [search-region-support.md](#item-25b0f1) | minor update | 地域サポート表の修正 | modified | 1 | 1 | 2 | 
| [search-security-api-keys.md](#item-d8c908) | minor update | APIキーに関するセクションの修正 | modified | 2 | 2 | 4 | 
| [search-security-enable-roles.md](#item-4985c4) | minor update | 役割ベースのアクセス制御に関するセクションの修正 | modified | 7 | 11 | 18 | 
| [search-security-get-encryption-keys.md](#item-7aed9d) | minor update | 暗号化キーに関する更新 | modified | 1 | 1 | 2 | 
| [search-security-rbac.md](#item-a5d129) | minor update | 役割ベースのアクセス制御に関するドキュメントの大幅修正 | modified | 87 | 54 | 141 | 
| [search-sku-tier.md](#item-7686b8) | minor update | SKU Tier情報の更新 | modified | 0 | 1 | 1 | 
| [search-synonyms.md](#item-2d5d63) | minor update | インデックス作成APIのHTTPメソッドの修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/includes/quickstarts/java.md{#item-bd5406}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 10/07/2024
+ms.date: 11/01/2024
 ---
 
 Build a Java console application using the [Azure.Search.Documents](/java/api/overview/azure/search) library to create, load, and query a search index. 
@@ -65,12 +65,12 @@ Use the following tools to create this quickstart.
         <dependency>
           <groupId>com.azure</groupId>
           <artifactId>azure-search-documents</artifactId>
-          <version>11.5.2</version>
+          <version>11.7.3</version>
         </dependency>
         <dependency>
           <groupId>com.azure</groupId>
           <artifactId>azure-core</artifactId>
-          <version>1.34.0</version>
+          <version>1.53.0</version>
         </dependency>
         <dependency>
           <groupId>junit</groupId>
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java クイックスタートの更新"
}
```

### Explanation
この変更は、Java 用の Azure.Search.Documents ライブラリに関するクイックスタートガイドの軽微な更新を示しています。主な変更点は、記事の日付と依存関係のバージョン番号が更新されたことです。具体的には、`ms.date` が 2024 年 10 月 7 日から 2024 年 11 月 1 日に変更され、`azure-search-documents` のバージョンが 11.5.2 から 11.7.3 に、また `azure-core` のバージョンが 1.34.0 から 1.53.0 にそれぞれ更新されています。この更新により、最新のライブラリバージョンを使用することでユーザーが最新の機能を活用できるようになっています。

## articles/search/keyless-connections.md{#item-3f0d72}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +1,10 @@
 ---
 title: Use keyless connections with Azure AI Search
-description: Use keyless connections with an Azure Identity library for authentication and authorization with Azure AI Search.
+description: Use keyless connections with an Azure Identity library for Microsoft Entra ID authentication and authorization with Azure AI Search.
 ms.topic: how-to
-ms.date: 06/05/2024
+ms.date: 10/30/2024
 author: HeidiSteen
 ms.author: heidist
-ms.reviewer: scaddie
 ms.custom: devx-track-dotnet, devx-track-extended-java, devx-track-js, devx-track-python, Keyless-dotnet, Keyless-java, Keyless-js, Keyless-python, build-2024-intelligent-apps
 #customer intent: As a developer, I want to use keyless connections so that I don't leak secrets.
 ---
@@ -34,7 +33,7 @@ Before continuing with this article, you need an Azure AI Search resource to wor
 
 ### Install Azure Identity client library
 
-Before working locally without keyless, update your AI Search enabled code with the Azure Identity client library.
+To use a keyless approach, update your AI Search enabled code with the Azure Identity client library.
 
 #### [.NET](#tab/csharp)
 
@@ -211,22 +210,21 @@ search_index_client = SearchIndexClient(
 
 ---
 
-
 ## Local development
 
-Local development without keyless includes these steps:
+Local development using roles includes these steps:
 
-- Assign your personal identity with RBAC roles on the specific resource.
-- Use a tool to authenticate with Azure.
+- Assign your personal identity to RBAC roles on the specific resource.
+- Use a tool like the Azure CLI or Azure PowerShell to authenticate with Azure.
 - Establish environment variables for your resource.
 
 ### Roles for local development
 
-As a local developer, your Azure identity needs full control of your service. This control is provided with RBAC roles. To manage your resource during development, these are the suggested roles:
+As a local developer, your Azure identity needs full control over data plane operations. These are the suggested roles:
 
-- Search Service Contributor
-- Search Index Data Contributor
-- Search Index Data Reader
+- Search Service Contributor, create and manage objects
+- Search Index Data Contributor, load an index
+- Search Index Data Reader, query an index
 
 Find your personal identity with one of the following tools. Use that identity as the `<identity-id>` value.
 
@@ -253,7 +251,7 @@ Find your personal identity with one of the following tools. Use that identity a
         --assignee "<identity-id>" \
         --scope "/subscriptions/<subscription-id>/resourceGroups/<resource-group-name>"
     ```
-    
+
 #### [Azure PowerShell](#tab/azure-powershell)
 
 1. Sign in with PowerShell.
@@ -277,13 +275,12 @@ Find your personal identity with one of the following tools. Use that identity a
 #### [Azure portal](#tab/portal)
 
 1. Use the steps found here: [find the user object ID](/partner-center/find-ids-and-domain-names#find-the-user-object-id) in the Azure portal.
-    
-2. Use the steps found at [open the Add role assignment page](search-security-rbac.md) in the Azure portal.
-    
+
+1. Use the steps found at [open the Add role assignment page](search-security-rbac.md) in the Azure portal.
+
 ---
-    
-Where applicable, replace `<identity-id>`, `<subscription-id>`, and `<resource-group-name>` with your actual values. 
 
+Where applicable, replace `<identity-id>`, `<subscription-id>`, and `<resource-group-name>` with your actual values. 
 
 ### Authentication for local development
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "キーなし接続に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Search におけるキーなし接続の使用に関するドキュメントを更新したものであり、主に内容の明確化と情報の最新化が含まれています。具体的には、`description` の部分が「Azure Identity ライブラリによる認証と承認」から「Microsoft Entra ID 認証と承認」に変更され、最新の名称が反映されています。また、更新日時が 2024 年 6 月 5 日から 2024 年 10 月 30 日に変更されました。

ローカル開発のセクションでは、「キーなし」との表現が「ロールを使った」ものに修正され、RBAC ロールの説明が強化されています。さらに、Azure での認証を行うためのツールについて具体的なツール（Azure CLI や Azure PowerShell）を挙げ、より具体的な手順が示されています。また、ローカル開発者が必要とする RBAC ロールの記述も明確化され、データプレーン操作に対する完全な制御が必要であることが強調されています。全体として、ユーザーが理解しやすい形で情報が整理されています。

## articles/search/media/search-security-rbac/portal-access-control.png{#item-89ca91}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ポータルアクセス制御の画像追加"
}
```

### Explanation
この変更は、Azure AI Search におけるセキュリティ RBAC（ロールベースのアクセス制御）に関連するポータルアクセス制御の画像を新たに追加したものです。画像ファイルは、ユーザーが Azure ポータルにおけるアクセス制御の設定方法を視覚的に理解するための補助資料として機能します。具体的な変更内容としては、画像ファイルが追加されており、ユーザーがポータルでの操作をより明確に把握できるようになることを目的としています。この画像は、ドキュメントの内容を補強し、ユーザー体験を向上させるために役立ちます。

## articles/search/search-get-started-rag.md{#item-05ff0e}

<details>
<summary>Diff</summary>
````diff
@@ -212,8 +212,8 @@ This section uses Visual Studio Code and Python to call the chat completion APIs
    ! pip install azure-search-documents==11.6.0b5 --quiet
    ! pip install azure-identity==1.16.1 --quiet
    ! pip install openai --quiet
-   ! pip intall aiohttp --quiet
-   ! pip intall ipykernel --quiet
+   ! pip install aiohttp --quiet
+   ! pip install ipykernel --quiet
    ```
 
 1. Set the following variables, substituting placeholders with the endpoints you collected in the previous step. 
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "パッケージインストールコマンドの修正"
}
```

### Explanation
この変更は、Azure AI Search に関する「検索を開始する」セクションでのパッケージインストールコマンドに関して誤字を修正したものです。具体的には、`pip intall` が `pip install` に修正されています。このミスは、パッケージが正しくインストールされない原因となるため、ユーザーがスムーズに環境をセットアップできるようにするための重要な修正です。この更新により、ユーザーは必要な依存関係を正しくインストールできるようになり、開発環境の構築が円滑に進むことが期待されます。

## articles/search/search-get-started-text.md{#item-935941}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: quickstart
-ms.date: 10/07/2024
+ms.date: 11/01/2024
 ---
 
 # Quickstart: Full text search using the Azure SDKs
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、「検索を開始する」セクションのメタデータの一部である日付を更新したものです。具体的には、`ms.date` フィールドの値が `10/07/2024` から `11/01/2024` に変更されています。この日付の更新は、コンテンツの最新性を反映させるためのもので、ユーザーに提供される情報がタイムリーであることを保証します。このような小さな更新は、ドキュメントの信頼性を維持するために重要です。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -94,7 +94,7 @@ You can create an Azure AI Search resource in any of the following Azure public
 | Australia Southeast​​​ |  | ✅ |  | |
 | East Asia​ | ✅ | ✅ | ✅ |  |
 | Southeast Asia​ ​ ​ | ✅ | ✅ | ✅ |  |
-| Central India | ✅ | ✅ | ✅ | S2, S3, S3HD, L1, L2 |
+| Central India | ✅ | ✅ | ✅ |  |
 | Jio India West​ ​ | ✅ | ✅ |  |
 | South India <sup>1</sup> |  | | ✅ |
 | Japan East  | ✅ | ✅ | ✅ |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域サポート表の修正"
}
```

### Explanation
この変更は、Azure AI Search リソースにおける地域サポートに関する表の内容を修正したものです。具体的には、`Central India` の列において、リソースの提供可能性が示されていますが、以前は `S2, S3, S3HD, L1, L2` と記載されていた部分が空白に修正されました。これは、特定のSKUの利用可能性が変更された場合や情報の整合性を保つために行われた可能性があります。この更新により、ユーザーはより正確な地域サポートの情報を得ることができ、リソースの作成時に役立つ情報となることが期待されます。

## articles/search/search-security-api-keys.md{#item-d8c908}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 06/28/2024
+ms.date: 10/30/2024
 ---
 
 # Connect to Azure AI Search using keys
@@ -245,7 +245,7 @@ It's not possible to use [customer-managed key encryption](search-security-manag
 
 + Always check code, samples, and training material before publishing to make sure you didn't leave valid API keys behind.
 
-+ For production workloads, switch to [Microsoft Entra ID and role-based access](search-security-rbac.md). Or, if you want to continue using API keys, be sure to always monitor [who has access to your API keys](#secure-api-keys) and [regenerate API keys](#regenerate-admin-keys) on a regular cadence.
++ For production workloads, switch to [Microsoft Entra ID and role-based access](keyless-connections.md). Or, if you want to continue using API keys, be sure to always monitor [who has access to your API keys](#secure-api-keys) and [regenerate API keys](#regenerate-admin-keys) on a regular cadence.
 
 ## See also
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIキーに関するセクションの修正"
}
```

### Explanation
この変更は、「Azure AI SearchのAPIキーに関する」セクションの内容を更新するもので、主に二つの点において修正が行われています。まず、`ms.date` フィールドの更新があり、日付が `06/28/2024` から `10/30/2024` に変更されています。次に、APIキーを使用する際の推奨事項に関する文言が修正されており、「Microsoft Entra IDとロールベースのアクセス」に関するリンク先が、`search-security-rbac.md` から新しいページ `keyless-connections.md` へと変更されています。この変更により、ユーザーはより適切な情報にアクセスできるようになり、セキュリティおよびアクセス管理に関するベストプラクティスに従うことが促されます。

## articles/search/search-security-enable-roles.md{#item-4985c4}

<details>
<summary>Diff</summary>
````diff
@@ -8,20 +8,18 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/18/2024
+ms.date: 10/30/2024
 
 ---
 
 # Enable or disable role-based access control in Azure AI Search
 
-Before you can assign roles for authorized access to Azure AI Search, enable role-based access control on your search service.
+Azure AI Search uses [key-based authentication](search-security-api-keys.md) by default, but it fully supports Microsoft Entra ID authentication and authorization for all control plane and data plane operations through Azure role-based access control (RBAC).
 
-Role-based access for data plane operations is optional, but recommended as the more secure option. The alternative is [key-based authentication](search-security-api-keys.md), which is the default. 
-
-Roles for service administration (control plane) are built in and can't be enabled or disabled. 
+Before you can assign roles for authorized data plane access to Azure AI Search, you must enable role-based access control on your search service. Roles for service administration (control plane) are built in and can't be enabled or disabled. 
 
 > [!NOTE]
-> *Data plane* refers to operations against the search service endpoint, such as indexing or queries, or any other operation specified in the [Search REST API](/rest/api/searchservice/) or equivalent Azure SDK client libraries.
+> *Data plane* refers to operations against the search service endpoint, such as indexing or queries, or any other operation specified in the [Search Service REST APIs](/rest/api/searchservice/) or equivalent Azure SDK client libraries. *Control plane* refers to Azure resource management, such as creating or configuring a search service.
 
 ## Prerequisites
 
@@ -223,13 +221,11 @@ To re-enable key authentication, set "disableLocalAuth" to false. The search ser
 
 ---
 
-## Limitations
-
-+ Role-based access control can increase the latency of some requests. Each unique combination of service resource (index, indexer, etc.) and service principal triggers an authorization check. These authorization checks can add up to 200 milliseconds of latency per request. 
+## Effects of role-based access control
 
-+ In rare cases where requests originate from a high number of different service principals, all targeting different service resources (indexes, indexers, etc.), it's possible for the authorization checks to result in throttling. Throttling would only happen if hundreds of unique combinations of search service resource and service principal were used within a second.
++ Role-based access control can increase the latency of some requests. Each unique combination of service resource (index, indexer, skillsets and so forth) and service principal triggers an authorization check. These authorization checks can add up to 200 milliseconds of latency per request. 
 
----
++ In rare cases where requests originate from a high number of different service principals, all targeting different service resources (indexes, indexers, and so forth), it's possible for the authorization checks to result in throttling. Throttling would only happen if hundreds of unique combinations of search service resource and service principal were used within a second.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "役割ベースのアクセス制御に関するセクションの修正"
}
```

### Explanation
この変更は、Azure AI Searchにおける役割ベースのアクセス制御に関する文書を更新しています。最初に、`ms.date` フィールドが `06/18/2024` から `10/30/2024` に変更され、文書の更新日が反映されています。次に、役割ベースのアクセス制御の説明が追加され、Azure AI Searchがデフォルトでキーを使用した認証を行うことが述べられていますが、Microsoft Entra IDによる認証と認可も完全にサポートしているという情報が強調されています。

また、データプレーン操作に対して役割ベースのアクセス制御がオプションとしてより安全な選択肢であることが明確に示されています。さらに、認可チェックによる遅延に関する注意点が追加され、特定の条件下ではリクエストのレイテンシーが増加する可能性についても詳しく説明されています。このように、ユーザーが役割ベースのアクセス制御を理解し、適切に管理できるように情報が整理されています。

## articles/search/search-security-get-encryption-keys.md{#item-7aed9d}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 02/16/2024
+ms.date: 10/30/2024
 ---
 
 # Find encrypted objects and information
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "暗号化キーに関する更新"
}
```

### Explanation
この変更は、「暗号化キーの取得」に関する文書の更新を含んでいます。具体的には、`ms.date` フィールドの値が `02/16/2024` から `10/30/2024` に変更されており、文書の更新日が反映されています。この変更により、利用者は情報が新しいものであることを確認でき、最新の内容を参照することが可能になります。文書に追加の内容や変更はありませんが、日付の更新により、リソースが最新の情報を提供していることが示されています。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -8,19 +8,20 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/03/2024
+ms.date: 10/30/2024
 ms.custom: subject-rbac-steps, devx-track-azurepowershell
 ---
 
 # Connect to Azure AI Search using roles
 
-Azure provides a global authentication and [role-based authorization system](/azure/role-based-access-control/role-assignments-portal) for all services running on the platform. In Azure AI Search, you can assign Azure roles for:
+Azure provides a global authentication and [role-based access control](/azure/role-based-access-control/role-assignments-portal) through Microsoft Entra ID for all services running on the platform. In this article, learn which roles provide access to search content and administration on Azure AI Search.
 
-> [!div class="checklist"]
-> + [Service administration](#assign-roles-for-service-administration)
-> + [Development or write-access to a search service](#assign-roles-for-development)
-> + [Read-only access for queries](#assign-roles-for-read-only-queries)
-> + [Scoped access to a single index](#grant-access-to-a-single-index)
+In Azure AI Search, you can assign Azure roles for:
+
++ [Service administration](#assign-roles-for-service-administration)
++ [Development or write-access to a search service](#assign-roles-for-development)
++ [Read-only access for queries](#assign-roles-for-read-only-queries)
++ [Scoped access to a single index](#grant-access-to-a-single-index)
 
 Per-user access over search results (sometimes referred to as *row-level security* or *document-level security*) isn't supported through role assignments. As a workaround, [create security filters](search-security-trimming-for-azure-search.md) that trim results by user identity, removing documents for which the requestor shouldn't have access. See this [Enterprise chat sample using RAG](/azure/developer/python/get-started-app-chat-template) for a demonstration.
 
@@ -32,11 +33,35 @@ Role-based access is optional, but recommended. The alternative is [key-based au
 
 + A search service in any region, on any tier, [enabled for role-based access](search-security-enable-roles.md).
 
-+ Owner, User Access Administrator, or a custom role with [Microsoft.Authorization/roleAssignments/write](/azure/templates/microsoft.authorization/roleassignments) permissions.
++ Owner, User Access Administrator, Role-based Access Control Administrator, or a custom role with [Microsoft.Authorization/roleAssignments/write](/azure/templates/microsoft.authorization/roleassignments) permissions.
+
+## How to assign roles in the portal
+
+The following steps work for all role assignments.
+
+1. Sign in to the [Azure portal](https://portal.azure.com).
+
+1. Navigate to your search service.
+
+1. [Enable role-based access](search-security-enable-roles.md).
+
+1. Select **Access Control (IAM)** in the left navigation pane.
+
+1. Select **+ Add** > **Add role assignment** to start the **Add role assignment** wizard.
 
-<a name = "built-in-roles-used-in-search"></a>
+   :::image type="content" source="media/search-security-rbac/portal-access-control.png" alt-text="Screenshot of the access control page in the Azure portal.":::
 
-## Built-in roles used in Azure AI Search
+1. Select a role. You can assign multiple security principals, whether users or managed identities to a role in one pass through the wizard, but you have to repeat these steps for each role you define.
+
+1. On the **Members** tab, select the Microsoft Entra user or group identity. If you're setting up permissions for another Azure service, select a system or user-managed identity.
+
+1. On the **Review + assign** tab, select **Review + assign** to assign the role.
+
+## Built-in roles used in search
+
+*Data plane* refers to operations against the search service endpoint, such as indexing or queries, or any other operation specified in the [Search Service REST APIs](/rest/api/searchservice/) or equivalent Azure SDK client libraries. 
+
+*Control plane* refers to Azure resource management, such as creating or configuring a search service.
 
 The following roles are built in. If these roles are insufficient, [create a custom role](#create-a-custom-role). 
 
@@ -54,18 +79,47 @@ Combine these roles to get sufficient permissions for your use case.
 > [!NOTE]
 > If you disable Azure role-based access, built-in roles for the control plane (Owner, Contributor, Reader) continue to be available. Disabling role-based access removes just the data-related permissions associated with those roles. If data plane roles are disabled, Search Service Contributor is equivalent to control-plane Contributor.
 
+## Summary
+
+| Permissions | Search Index Data Reader | Search Index Data Contributor | Search Service Contributor | Owner/Contributor | Reader |
+|-------------|--------------------------|-------------------------------|----------------------------|-------------------|--------|
+|View the resource in Azure portal |❌|❌|✅|✅|✅|
+|View resource properties/metrics/endpoint |❌|❌|✅|✅|✅|
+|List all objects on the resource |❌|❌|✅|✅|✅|
+|Access quotas and service statistics |❌|❌|✅|✅|❌|
+|Read/query an index |✅|❌|❌|❌|❌|
+|Upload data for indexing |❌|✅|❌|❌|❌|
+|Create or edit indexes/aliases |❌|❌|✅|✅|❌|
+|Create, edit and run indexers/data sources/skillsets |❌|❌|✅|✅|❌|
+|Create or edit synonym maps |❌|❌|✅|✅|❌|
+|Create or edit debug sessions |❌|❌|✅|✅|❌|
+|Create or manage deployments |❌|❌|✅|✅|❌|
+|Create or configure Azure AI Search resources |❌|❌|✅|✅|❌|
+|View/Copy/Regenerate keys under Keys |❌|❌|✅|✅|❌|
+|View roles/policies/definitions |❌|❌|✅|✅|❌|
+|Set authentication options |❌|❌|✅|✅|❌|
+|Configure private connections |❌|❌|✅|✅|❌|
+|Configure network security |❌|❌|✅|✅|❌|
+
+Owners and Contributors grant the same permissions, except that only Owners can assign roles.
+
+Owners and Contributors can create, read, update, and delete objects in the Azure portal *if API keys are enabled*. The portal uses keys on internal calls to data plane APIs. In you subsequently configure Azure AI Search to use "roles only", then Owner and Contributor won't be able to manage objects in the portal using just those role assignments. The solution is to assign more roles, such as Search Index Data Reader, Search Index Data Contributor, and Search Service Contributor.
+
 ## Assign roles
 
 In this section, assign roles for:
 
-+ [Service administration](#assign-roles-for-service-administration)
++ Service administration
++ Development or write-access to a search service
++ Read-only access for queries
+
+<!-- + [Service administration](#assign-roles-for-service-administration)
 
     | Role | ID|
     | --- | --- |
     |`Owner`|8e3af657-a8ff-443c-a75c-2fe8c4bcb635|
     |`Contributor`|b24988ac-6180-42a0-ab88-20f7382dd24c|
     |`Reader`|acdd72a7-3385-48ef-bd42-f606fba81ae7|
-    
 
 + [Development or write-access to a search service](#assign-roles-for-development)
 
@@ -79,33 +133,28 @@ In this section, assign roles for:
 
     | Role | ID|
     | --- | --- |
-    | `Search Index Data Reader` [with PowerShell](search-security-rbac.md?tabs=roles-portal-admin%2Croles-portal%2Croles-portal-query%2Ctest-portal%2Ccustom-role-portal#grant-access-to-a-single-index)|1407120a-92aa-4202-b7e9-c0e197c71c8f|
+    | `Search Index Data Reader` [with PowerShell](search-security-rbac.md?tabs=roles-portal-admin%2Croles-portal%2Croles-portal-query%2Ctest-portal%2Ccustom-role-portal#grant-access-to-a-single-index)|1407120a-92aa-4202-b7e9-c0e197c71c8f| -->
 
 ### Assign roles for service administration
 
-As a service administrator, you can create and configure a search service, and perform all control plane operations described in the [Management REST API](/rest/api/searchmanagement/) or equivalent client libraries. Depending on the role, you can also perform most data plane [Search REST API](/rest/api/searchservice/) tasks.
+As a service administrator, you can create and configure a search service, and perform all control plane operations described in the [Management REST API](/rest/api/searchmanagement/) or equivalent client libraries. If you're an Owner or Contributor, you can also perform most data plane [Search REST API](/rest/api/searchservice/) tasks in the Azure portal.
 
+| Role | ID|
+| --- | --- |
+|[`Owner`](/azure/role-based-access-control/built-in-roles#owner) |8e3af657-a8ff-443c-a75c-2fe8c4bcb635|
+|[`Contributor`](/azure/role-based-access-control/built-in-roles#contributor)|b24988ac-6180-42a0-ab88-20f7382dd24c|
+|[`Reader`](/azure/role-based-access-control/built-in-roles#reader)|acdd72a7-3385-48ef-bd42-f606fba81ae7|
 
 #### [**Azure portal**](#tab/roles-portal-admin)
 
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
-1. Navigate to your search service.
-
-1. Select **Access Control (IAM)** in the left navigation pane.
-
-1. Select **+ Add** > **Add role assignment**.
-
-1. Select an applicable role:
+1. Assign these roles:
 
    + Owner (full access to all data plane and control plane operations, except for query permissions)
    + Contributor (same as Owner, except for permissions to assign roles)
    + Reader (acceptable for monitoring and viewing metrics)
 
-1. On the **Members** tab, select the Microsoft Entra user or group identity.
-
-1. On the **Review + assign** tab, select **Review + assign** to assign the role.
-
 #### [**PowerShell**](#tab/roles-powershell-admin)
 
 When you [use PowerShell to assign roles](/azure/role-based-access-control/role-assignments-powershell), call [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment), providing the Azure user or group name, and the scope of the assignment.
@@ -124,6 +173,12 @@ New-AzRoleAssignment -SignInName <email> `
 
 Role assignments are global across the search service. To [scope permissions to a single index](#rbac-single-index), use PowerShell or the Azure CLI to create a custom role.
 
+| Task | Role | ID|
+| --- | --- | --- |
+| CRUD operations | [`Search Service Contributor`](/azure/role-based-access-control/built-in-roles#search-service-contributor)|7ca78c08-252a-4471-8644-bb5ff32d4ba0|
+| Load documents, run indexing jobs | [`Search Index Data Contributor`](/azure/role-based-access-control/built-in-roles#search-index-data-contributor)|8ebe5a00-799e-43f5-93ac-243d3dce84a7|
+| Query an index | [`Search Index Data Reader`](/azure/role-based-access-control/built-in-roles#search-index-data-reader)|1407120a-92aa-4202-b7e9-c0e197c71c8f|
+
 Another combination of roles that provides full access is Contributor or Owner, plus Search Index Data Reader.
 
 > [!IMPORTANT]
@@ -133,28 +188,12 @@ Another combination of roles that provides full access is Contributor or Owner,
 
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
-1. Navigate to your search service.
-
-1. Select **Access Control (IAM)** in the left navigation pane.
-
-1. Select **+ Add** > **Add role assignment**.
-
-   ![Access control (IAM) page with Add role assignment menu open.](~/reusable-content/ce-skilling/azure/media/role-based-access-control/add-role-assignment-menu-generic.png)
-
-1. Select a role:
+1. Assign these roles:
 
    + Search Service Contributor (create-read-update-delete operations on indexes, indexers, skillsets, and other top-level objects)
    + Search Index Data Contributor (load documents and run indexing jobs)
    + Search Index Data Reader (query an index)
 
-   Another combination of roles that provides full access is Contributor or Owner, plus Search Index Data Reader.
-
-1. On the **Members** tab, select the Microsoft Entra user or group identity.
-
-1. On the **Review + assign** tab, select **Review + assign** to assign the role.
-
-1. Repeat for the other roles. Most developers need all three.
-
 #### [**PowerShell**](#tab/roles-powershell)
 
 When you [use PowerShell to assign roles](/azure/role-based-access-control/role-assignments-powershell), call [New-AzRoleAssignment](/powershell/module/az.resources/new-azroleassignment), providing the Azure user or group name, and the scope of the assignment.
@@ -179,7 +218,11 @@ New-AzRoleAssignment -SignInName <email> `
 
 ### Assign roles for read-only queries
 
-Use the Search Index Data Reader role for apps and processes that only need read-access to an index. 
+Use the Search Index Data Reader role for apps and processes that only need read-access to an index.
+
+| Role | ID|
+| --- | --- |
+| [`Search Index Data Reader`](/azure/role-based-access-control/built-in-roles#search-index-data-reader) [with PowerShell](search-security-rbac.md#grant-access-to-a-single-index)|1407120a-92aa-4202-b7e9-c0e197c71c8f|
 
 This is a very specific role. It grants [GET or POST access](/rest/api/searchservice/documents) to the *documents collection of a search index* for search, autocomplete, and suggestions. It doesn't support GET or LIST operations on an index or other top-level objects, or GET service statistics.
 
@@ -189,17 +232,7 @@ This section provides basic steps for setting up the role assignment and is here
 
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
-1. Navigate to your search service.
-
-1. Select **Access Control (IAM)** in the left navigation pane.
-
-1. Select **+ Add** > **Add role assignment**.
-
-1. Select the **Search Index Data Reader** role.
-
-1. On the **Members** tab, select the Microsoft Entra user or group identity. If you're setting up permissions for another service, you might be using a system or user-managed identity. Choose that option if the role assignment is for a service identity.
-
-1. On the **Review + assign** tab, select **Review + assign** to assign the role.
+1. Assign the **Search Index Data Reader** role.
 
 #### [**PowerShell**](#tab/roles-powershell-query)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "役割ベースのアクセス制御に関するドキュメントの大幅修正"
}
```

### Explanation
この変更は、Azure AI Searchにおける役割ベースのアクセス制御に関する文書を大幅に修正したものです。主な更新内容には、`ms.date` フィールドの変更、役割の割り当てに関する情報の拡充、役割を割り当てる際の手順の詳細化、そして各役割に関連するパーミッションの表が追加されています。

具体的には、Azure Entra IDを通じた役割ベースのアクセス制御について説明が強化されました。また、役割の管理方法や権限設定に関する手順が明確に示され、特にAzureポータルでの操作手順が詳細に記述されています。これにより、ユーザーは役割の割り当てや管理を容易に行えるようになります。さらに、役割に関連する権限のサマリーが表形式で提供されており、どの役割がどの操作を実行できるかが一目でわかるようになっています。

この更新により、ユーザーはAzure AI Searchの役割ベースのアクセス制御を理解し、適切に管理するための有用な情報を得ることができます。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -59,7 +59,6 @@ Currently, several regions are at capacity for specific tiers and can't be used
 
 | Region | Disabled tier (SKU) due to over-capacity | Suggested alternative |
 |--------|------------------------------------------|-----------------------|
-| Central India | S2, S3, S3HD, L1, L2| South India |
 | East US 2| Basic, S1| Central US |
 | South Central US | All tiers | Central US |
 | US Gov Virginia | All tiers | US Gov Arizona |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SKU Tier情報の更新"
}
```

### Explanation
この変更は、AzureのSKU Tierに関するドキュメントの一部を更新したものです。具体的には、特定の地域でのSKUの使用制限に関する表から「Central India」地域に関する行が削除されました。この行は、S2、S3、S3HD、L1、L2の各SKUが容量制限により利用できないことを示していました。

この更新により、情報が整理され、利用者に提供される情報が最新の状況を反映するようになりました。削除された情報は他の地域に比べて重要度が低くなった可能性があり、ユーザーは他の提案された代替地域を考慮して選択することができます。

## articles/search/search-synonyms.md{#item-2d5d63}

<details>
<summary>Diff</summary>
````diff
@@ -155,7 +155,7 @@ If the synonym map exists on the search service, it's used on the next query, wi
 Use the [Create or Update Index (REST API)](/rest/api/searchservice/indexes/create-or-update) to modify a field definition.
 
 ```http
-POST /indexes?api-version=2024-07-01
+PUT /indexes?api-version=2024-07-01
 {
     "name":"hotels-sample-index",
     "fields":[
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス作成APIのHTTPメソッドの修正"
}
```

### Explanation
この変更は、Azureの検索サービスに関連する「検索同義語」ドキュメントの一部を更新したもので、インデックスを作成または更新するためのHTTPメソッドが修正されました。具体的には、以前のAPIリクエストではHTTPメソッドが`POST`として指定されていましたが、これが`PUT`に変更されました。

この修正により、インデックスの定義を更新するためのAPIリクエストの仕様が正確に反映され、ユーザーがAPIを適切に利用できるようになります。これにより、検索サービスのインデックス管理における一貫性と正確性が向上します。


