---
date: '2025-01-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:70337bc...MicrosoftDocs:de17d62
summary: このレポートでは、Azure Cosmos DBに関するドキュメントの主要な更新点をまとめています。新機能として、索引設定の際の削除検出機能の設定方法や、マネージドアイデンティティを使用した接続の詳細が追加されました。また、C#検索クエリ統合チュートリアルの設定ファイル名が変更され、ユーザーにとっての利便性が向上しています。全体として、これらの更新はユーザーの作業を簡素化し、効率性やセキュリティの向上を目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:70337bc...MicrosoftDocs:de17d62){target="_blank"}

# Highlights

- **新機能**: Azure Cosmos DBの索引に関するドキュメントの更新では、削除検出機能の設定法や新しいManaged Identity接続文字列が追加されました。
- **新機能**: Azure Cosmos DBでのマネージドアイデンティティを使用した接続ガイドには、新しい認証メカニズムや接続手順の詳細が追加されました。
- **その他更新**: C#検索クエリ統合チュートリアルで設定ファイルの参照名が変更され、ユーザーの設定が容易になりました。

## New features

### Azure Cosmos DBの索引設定
- Cosmos DBの索引設定ドキュメント内で、削除検出機能を有効にするためのフィールド設定が明確化。
- 新しいManaged Identity接続文字列の形式が追加され、アカウントキーを使用せずにアクセス可能であることが強調されました。

### マネージドアイデンティティを用いた接続
- 接続方法が「レガシーアプローチ」と「モダンアプローチ」とに細分化され、特にモダンアプローチが推奨されるよう詳細が記載。
  
## Breaking changes

なし

## Other updates

### C#検索クエリ統合チュートリアル
- `local.settings.json`ファイルが`sample.local.settings.json`に変更され、ユーザーがサンプル設定を容易に利用できるようになりました。

# Insights

Azure Cosmos DBやC#検索クエリの設定における変更は、ユーザーの作業を簡素化し、効率性やセキュリティの強化を目的としています。

### Azure Cosmos DBの索引構成
Azure Cosmos DBを利用する際、検索インデックスをセットアップするプロセスは重要です。今回のアップデートにより、ドキュメントは削除検出フィールドの指定を明確にし、誤解を防ぐ内容になっています。特に、ソフト削除フラグとして`true`値を使用することが強調されています。この変更は、データのライフサイクル管理を考慮したインデックス管理の一環です。

### マネージドアイデンティティでの接続
ドキュメントでは、Azure Cosmos DBにおけるデータアクセスをよりセキュアにすることを目的とし、マネージドアイデンティティを活用する接続ガイドを刷新しました。これにより、アカウントキーを使わない接続が推奨されています。特にAzure環境でよりモダンな認証アプローチへの移行が促進されます。これらの記載は、安全性向上とともに、運用の自動化を推進するためのステップと考えられます。

### C#チュートリアルの改善
C#のチュートリアル更新では、サンプル設定ファイルの導入でユーザーが容易に環境設定を行えるようになりました。こうしたドキュメントの微調整によって特に初心者が従うべき手順がわかりやすくなり、学習曲線を緩和する効果が期待されています。

全体として、この一連のドキュメント更新は、Azureサービスの利用者が安全で効率的にリソースを活用できるように意図されています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-howto-index-cosmosdb.md](#item-568fab) | minor update | Cosmos DBの索引に関するドキュメントの更新 | modified | 11 | 6 | 17 | 
| [search-howto-managed-identities-cosmos-db.md](#item-a74464) | minor update | Azure Cosmos DBでのマネージドアイデンティティを使用したインデクサ接続の設定ガイドの更新 | modified | 96 | 49 | 145 | 
| [tutorial-csharp-search-query-integration.md](#item-8ad6b5) | minor update | C# 検索クエリ統合チュートリアルの設定ファイルの変更 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-howto-index-cosmosdb.md{#item-568fab}

<details>
<summary>Diff</summary>
````diff
@@ -84,7 +84,7 @@ You can use either the **Import data** wizard or **Import and vectorize data** w
 
    [Change detection](#incremental-indexing-and-custom-queries) is supported by default through a `_ts` field (timestamp). If you upload content using the approach described in [Try with sample data](#try-with-sample-data), the collection is created with a `_ts` field.
 
-   [Deletion detection](#indexing-deleted-documents) requires that you have a pre-existing top-level field in the collection that can be used as a soft-delete flag. It should be a Boolean field (you could name it IsDeleted). Specify `true` as the soft-delete value. In the search index, add a corresponding search field called *IsDeleted* set to retrievable and filterable. 
+   [Deletion detection](#indexing-deleted-documents) requires that you have a preexisting top-level field in the collection that can be used as a soft-delete flag. It should be a Boolean field (you could name it IsDeleted). Specify `true` as the soft-deleted value. In the search index, add a corresponding search field called *IsDeleted* set to retrievable and filterable. 
 
 1. Continue with the remaining steps to complete the wizard:
 
@@ -149,10 +149,15 @@ Avoid port numbers in the endpoint URL. If you include the port number, the conn
 |`{ "connectionString" : "AccountEndpoint=https://<Cosmos DB account name>.documents.azure.com;AccountKey=<Cosmos DB auth key>;Database=<Cosmos DB database id>`" }` |
 | You can get the connection string from the Azure Cosmos DB account page in the Azure portal by selecting **Keys** in the left navigation pane. Make sure to select a full connection string and not just a key. |
 
-| Managed identity connection string |
-|------------------------------------|
-|`{ "connectionString" : "ResourceId=/subscriptions/<your subscription ID>/resourceGroups/<your resource group name>/providers/Microsoft.DocumentDB/databaseAccounts/<your cosmos db account name>/;(ApiKind=[api-kind];)/(IdentityAuthType=[identity-auth-type])" }`|
-|This connection string doesn't require an account key, but you must have a search service that can [connect using a managed identity](search-howto-managed-identities-data-sources.md). For connections targeting the [SQL API](/azure/cosmos-db/sql-query-getting-started), you can omit `ApiKind` from the connection string. For more information about `ApiKind`, `IdentityAuthType` see [Setting up an indexer connection to an Azure Cosmos DB database using a managed identity](search-howto-managed-identities-cosmos-db.md).|
+| (Modern approach) Managed identity connection string for NoSQL accounts |
+|------------------------------------------------------------------------------|
+|`{ "connectionString" : "ResourceId=/subscriptions/<your subscription ID>/resourceGroups/<your resource group name>/providers/Microsoft.DocumentDB/databaseAccounts/<your cosmos db account name>/;(ApiKind=[api-kind];)/(IdentityAuthType=AccessToken)" }`|
+|This connection string, supported only for Azure Cosmos DB for NoSQL accounts, ensures that the search service will never use account keys (even in the background) when attempting to access data from Cosmos DB. This is recommended, as it works even if the NoSQL account has account keys disabled. For more information, see [Setting up an indexer connection to an Azure Cosmos DB database using a managed identity](search-howto-managed-identities-cosmos-db.md)|
+
+| (Legacy approach) Managed identity connection string |
+|------------------------------------------------------|
+|`{ "connectionString" : "ResourceId=/subscriptions/<your subscription ID>/resourceGroups/<your resource group name>/providers/Microsoft.DocumentDB/databaseAccounts/<your cosmos db account name>/;(ApiKind=[api-kind];)/(IdentityAuthType=AccountKey)" }`|
+|This connection string doesn't require an account key to be specified directly, but the search service will utilize the managed identity to fetch the account keys in the background. Though this is supported for all Cosmos DB account types, it isn't recommended for the NoSQL account type. Such a connection string won't work if account keys are disabled for the Cosmos DB account. If the `IdentityAuthType` property is omitted, the search service will still default to fetching the account key in the background. For connections targeting the [SQL API](/azure/cosmos-db/sql-query-getting-started), you can omit `ApiKind` from the connection string. For more information about `ApiKind`, `IdentityAuthType` see [Setting up an indexer connection to an Azure Cosmos DB database using a managed identity](search-howto-managed-identities-cosmos-db.md)|
 
 <a name="flatten-structures"></a>
 
@@ -380,7 +385,7 @@ The following example shows a [data source definition](#define-the-data-source)
 ```
 
 > [!NOTE]
-> When you assign a `null` value to a field in your Azure Cosmos DB, the AI Search indexer is unable to distinguish between `null` and a missing field value. Therefore, if a field in the index is empty, it will not be substituted with a `null` value, even if that modification was specifically made in your database.
+> When you assign a `null` value to a field in your Azure Cosmos DB, the AI Search indexer is unable to distinguish between `null` and a missing field value. Therefore, if a field in the index is empty, it will not be substituted with a `null` value, even if that modification was made in your database.
 
 <a name="IncrementalProgress"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cosmos DBの索引に関するドキュメントの更新"
}
```

### Explanation
この変更では、Azure Cosmos DBに関する検索インデックスの構成や操作に関連するドキュメントが更新されました。具体的には、削除検出機能を有効にするためのフィールドの設定方法が明確にされ、新しいManaged Identity接続文字列の形式が追加されました。

修正内容には以下のポイントが含まれています：

1. **削除検出の説明の整合性**: 使用するフィールドに関する説明がわかりやすく調整されています。`true`値がソフト削除フラグとして指定されることが明確に示されています。
2. **接続文字列の更新**: 
   - 新しい接続文字列形式として「Modern approach」が導入され、Azure Cosmos DBのNoSQLアカウント用のベストプラクティスが記述されています。これにより、アカウントキーを使用せずに検索サービスがCosmos DBにアクセスできることが強調されました。
   - 従来の接続文字列形式も説明されていますが、NoSQLアカウントでは推奨されていない点が明示され、注意喚起が行われています。

全体として、これらの修正はAzure Cosmos DBを利用した検索インデックスの設定・管理におけるユーザーの理解を深めることを目的としています。

## articles/search/search-howto-managed-identities-cosmos-db.md{#item-a74464}

<details>
<summary>Diff</summary>
````diff
@@ -2,12 +2,12 @@
 title: Set up an indexer connection to Azure Cosmos DB using a managed identity
 titleSuffix: Azure AI Search
 description: Learn how to set up an indexer connection to an Azure Cosmos DB account using a managed identity.
-author: gmndrg
-ms.author: gimondra
+author: arv100kri
+ms.author: arjagann
 
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/10/2024
+ms.date: 01/06/2025
 ms.custom:
   - subject-rbac-steps
   - ignite-2023
@@ -17,21 +17,31 @@ ms.custom:
 
 This article explains how to set up an indexer connection to an Azure Cosmos DB database using a managed identity instead of providing credentials in the connection string.'
 
-You can use a system-assigned managed identity or a user-assigned managed identity. Managed identities are Microsoft Entra logins and require Azure role assignments to access data in Azure Cosmos DB. 
+You can use a system-assigned managed identity or a user-assigned managed identity. Managed identities are Microsoft Entra logins and require Azure role assignments to access data in Azure Cosmos DB. You can optionally [enforce role-based access as the only authentication method](/azure/cosmos-db/how-to-setup-rbac#disable-local-auth) for data connections by setting `disableLocalAuth` to `true` for your Azure Cosmos DB for NoSQL account.
 
 ## Prerequisites
 
 * [Create a managed identity](search-howto-managed-identities-data-sources.md) for your search service.
 
-* Azure Cosmos DB for NoSQL. You can optionally [enforce role-based access as the only authentication method](/azure/cosmos-db/how-to-setup-rbac#disable-local-auth) for data connections by setting `disableLocalAuth` to `true` for your Cosmos DB account.
+## Supported approaches for managed identity authentication
+
+Azure AI Search supports two mechanisms to connect to Azure Cosmos DB using managed identity. 
+
+* The _legacy_ approach requires configuring the managed identity to have reader permissions on the control plane of the target Azure Cosmos DB account. Azure AI Search utilizes that identity to fetch the account keys of Cosmos DB account in the background to access the data. This approach won't work if the Cosmos DB account has `"disableLocalAuth": true`.
+
+* The _modern_ approach requires configuring the managed identity appropriate roles on the control and data plane of the target Azure Cosmos DB account. Azure AI Search will then request an access token to access the data in the Cosmos DB account. This approach works even if the Cosmos DB account has `"disableLocalAuth": true`.
+
+Indexers that connect to Azure Cosmos DB for NoSQL support both the _legacy_ and the _modern_ approach - the _modern_ approach is highly recommended.
 
 ## Limitations
 
-Indexer support for Azure Cosmos DB for Gremlin and MongoDB Collections is currently in preview. At this time, a preview limitation requires Azure AI Search to connect using keys. You can still set up a managed identity and role assignment, but Azure AI Search will only use the role assignment to get keys for the connection. This limitation means that you can't configure a [role-based approach](/azure/cosmos-db/how-to-setup-rbac#disable-local-auth) if your indexers are connecting to Gremlin or MongoDB.
+* Indexers that connect to Azure Cosmos DB for Gremlin and MongoDB (currently in preview) only support the _legacy_ approach.
+
+## Connect to Azure Cosmos DB for NoSQL
 
-## Create a role assignment in Azure Cosmos DB
+This section outlines the steps to configure connecting to Azure Cosmos DB for NoSQL via the _modern_ approach.
 
-### [**Azure portal**](#tab/portal)
+### Configure control plane role assignments
 
 1. Sign in to Azure portal and find your Cosmos DB for NoSQL account.
 
@@ -49,108 +59,145 @@ Indexer support for Azure Cosmos DB for Gremlin and MongoDB Collections is curre
 
 1. Select the identity and save the role assignment.
 
-For more information, see [Configure role-based access control with Microsoft Entra ID for your Azure Cosmos DB account](/azure/cosmos-db/how-to-setup-rbac).
+For more information, see [Use control plane role-based access control with Azure Cosmos DB for NoSQL](/azure/cosmos-db/nosql/security/how-to-grant-control-plane-role-based-access).
+
+### Configure data plane role assignments
 
-### [**PowerShell**](#tab/powershell)
+The managed identity needs to assigned a role to read from the Cosmos DB account's data plane. 
+The Object (principal) ID for the search service's system/user assigned identity can be found from the search service's "Identity" tab.
+This step can only be performed via Azure CLI at the moment. 
 
 Set variables:
 
-```azurepowershell
+```azurecli
 $cosmosdb_acc_name = <cosmos db account name>
 $resource_group = <resource group name>
 $subsciption = <subscription ID>
-$system_assigned_principal = <principal ID for the search service's system assigned identity>
+$system_assigned_principal = <Object (principal) ID for the search service's system/user assigned identity>
 $readOnlyRoleDefinitionId = "00000000-0000-0000-0000-00000000000"
 $scope=$(az cosmosdb show --name $cosmosdbname --resource-group $resourcegroup --query id --output tsv)
 ```
 
 Define a role assignment for the system-assigned identity:
 
-```azurepowershell
+```azurecli
 az cosmosdb sql role assignment create --account-name $cosmosdbname --resource-group $resourcegroup --role-definition-id $readOnlyRoleDefinitionId --principal-id $sys_principal --scope $scope
 ```
 
----
+For more information, see [Use data plane role-based access control with Azure Cosmos DB for NoSQL](/azure/cosmos-db/nosql/security/how-to-grant-data-plane-role-based-access)
 
-## Specify a managed identity in a connection string
+### Configure the data source definition
 
-Once you have a role assignment, you can set up a connection to Azure Cosmos DB for NoSQL that operates under that role.
+Once you have configured **both** control plane and data plane role assignments on the Azure Cosmos DB for NoSQL account, you can set up a connection to it that operates under that role.
 
 Indexers use a data source object for connections to an external data source. This section explains how to specify a system-assigned managed identity or a user-assigned managed identity on a data source connection string. You can find more [connection string examples](search-howto-managed-identities-data-sources.md#connection-string-examples) in the managed identity article.
 
 > [!TIP]
-> You can create a data source connection to CosmosDB in the Azure portal, specifying either a system or user-assigned managed identity, and then view the JSON definition to see how the connection string is formulated.
+> You can create a data source connection to Cosmos DB in the Azure portal, specifying either a system or user-assigned managed identity, and then view the JSON definition to see how the connection string is formulated.
 
-### System-assigned managed identity
+The [REST API](/rest/api/searchservice/data-sources/create), Azure portal, and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) support using a system-assigned or user-assigned managed identity.
 
-The [REST API](/rest/api/searchservice/data-sources/create), Azure portal, and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) support using a system-assigned managed identity. 
+#### Connect through system-assigned identity
 
 When you're connecting with a system-assigned managed identity, the only change to the data source definition is the format of the "credentials" property. Provide a database name and a ResourceId that has no account key or password. The ResourceId must include the subscription ID of Azure Cosmos DB, the resource group, and the Azure Cosmos DB account name.
 
-* For SQL collections, the connection string doesn't require "ApiKind". 
-* For SQL collections, add "IdentityAuthType=AccessToken" if role-based access is enforced as the only authentication method. It isn't applicable for MongoDB and Gremlin collections.
-* For MongoDB collections, add "ApiKind=MongoDb" to the connection string and use a preview REST API.
-* For Gremlin graphs, add "ApiKind=Gremlin" to the connection string and use a preview REST API.
-
-Here's an example of how to create a data source to index data from a Cosmos DB account using the [Create Data Source](/rest/api/searchservice/data-sources/create) REST API and a managed identity connection string. The managed identity connection string format is the same for the REST API, .NET SDK, and the Azure portal.
+Here's an example using the [Create Data Source](/rest/api/searchservice/data-sources/create) REST API that exercises the _modern_ approach.
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
+POST https://[service name].search.windows.net/datasources?api-version=2024-11-01-preview
 {
     "name": "my-cosmosdb-ds",
     "type": "cosmosdb",
     "credentials": {
-        "connectionString": "ResourceId=/subscriptions/[subscription-id]/resourceGroups/[rg-name]/providers/Microsoft.DocumentDB/databaseAccounts/[cosmos-account-name];Database=[cosmos-database];ApiKind=SQL;IdentityAuthType=[AccessToken | AccountKey]"
+        "connectionString": "ResourceId=/subscriptions/[subscription-id]/resourceGroups/[rg-name]/providers/Microsoft.DocumentDB/databaseAccounts/[cosmos-account-name];Database=[cosmos-database];IdentityAuthType=AccessToken"
     },
-    "container": { "name": "[my-cosmos-collection]", "query": null },
-    "dataChangeDetectionPolicy": null
+    "container": { "name": "[my-cosmos-collection]" }
+}
+```
+
+>[!NOTE]
+> If the `IdentityAuthType` property isn't part of the connection string, then Azure AI Search defaults to the _legacy_ approach to ensure backward compatibility.
+
+#### Connect through user-assigned identity
+
+You need to add an "identity" property to the data source definition, where you specify the specific identity (out of several that can be assigned to the search service), that will be used to connect to the Azure Cosmos DB account.
+
+Here's an example using user-assigned identity via the _modern_ approach.
 
- 
+```http
+POST https://[service name].search.windows.net/datasources?api-version=2024-11-01-preview
+{
+    "name": "[my-cosmosdb-ds]",
+    "type": "cosmosdb",
+    "credentials": {
+        "connectionString": "ResourceId=/subscriptions/[subscription-id]/resourceGroups/[rg-name]/providers/Microsoft.DocumentDB/databaseAccounts/[cosmos-account-name];Database=[cosmos-database];IdentityAuthType=AccessToken"
+    },
+    "container": { "name": "[my-cosmos-collection]"},
+    "identity" : { 
+        "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
+        "userAssignedIdentity": "/subscriptions/[subscription-id]/resourcegroups/[rg-name]/providers/Microsoft.ManagedIdentity/userAssignedIdentities/[my-user-managed-identity-name]" 
+    }
 }
 ```
 
-### User-assigned managed identity
+## Connect to Azure Cosmos DB for Gremlin/MongoDB (preview)
+
+This section outlines the steps to configure connecting to Azure Cosmos DB for Gremlin/Mongo via the _legacy_ approach.
 
-When you're connecting with a user-assigned managed identity, there are two changes to the data source definition:
+### Configure control plane role assignments
 
-* First, the format of the "credentials" property is the database name and a ResourceId that has no account key or password. The ResourceId must include the subscription ID of Azure Cosmos DB, the resource group, and the Azure Cosmos DB account name.
+Follow the same steps as before to assign the appropriate roles on the control plane of the Azure Cosmos DB for Gremlin/MongoDB.
 
-  * For SQL collections, the connection string doesn't require "ApiKind". 
-  * For SQL collections, add "IdentityAuthType=AccessToken" if role-based access is enforced as the only authentication method. It isn't applicable for MongoDB and Gremlin collections.
-  * For MongoDB collections, add "ApiKind=MongoDb" to the connection string
-  * For Gremlin graphs, add "ApiKind=Gremlin" to the connection string.
+### Set the connection string
 
-* Second, you add an "identity" property that contains the collection of user-assigned managed identities. Only one user-assigned managed identity should be provided when creating the data source. Set it to type "userAssignedIdentities".
+* For MongoDB collections, add "ApiKind=MongoDb" to the connection string and use a preview REST API.
+* For Gremlin graphs, add "ApiKind=Gremlin" to the connection string and use a preview REST API.
+* For either kinds, only the __legacy__ approach is supported - that is, `IdentityAuthType=AccountKey` or omitting it entirely is the only valid connection string.
 
-Here's an example of how to create an indexer data source object using the REST API.
+Here's an example to connect to MongoDB collections using system-assigned identity via the REST API
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
+POST https://[service name].search.windows.net/datasources?api-version=2024-11-01-preview
+{
+    "name": "my-cosmosdb-ds",
+    "type": "cosmosdb",
+    "credentials": {
+        "connectionString": "ResourceId=/subscriptions/[subscription-id]/resourceGroups/[rg-name]/providers/Microsoft.DocumentDB/databaseAccounts/[cosmos-account-name];Database=[cosmos-database];ApiKind=MongoDb"
+    },
+    "container": { "name": "[my-cosmos-collection]", "query": null },
+    "dataChangeDetectionPolicy": null
+}
+```
+
+Here's an example to connect to Gremlin graphs using user-assigned identity.
 
+```http
+POST https://[service name].search.windows.net/datasources?api-version=2024-11-01-preview
 {
     "name": "[my-cosmosdb-ds]",
     "type": "cosmosdb",
     "credentials": {
-        "connectionString": "ResourceId=/subscriptions/[subscription-id]/resourceGroups/[rg-name]/providers/Microsoft.DocumentDB/databaseAccounts/[cosmos-account-name];Database=[cosmos-database];ApiKind=SQL;IdentityAuthType=[AccessToken | AccountKey]"
-    },
-    "container": { 
-        "name": "[my-cosmos-collection]", "query": null 
+        "connectionString": "ResourceId=/subscriptions/[subscription-id]/resourceGroups/[rg-name]/providers/Microsoft.DocumentDB/databaseAccounts/[cosmos-account-name];Database=[cosmos-database];ApiKind=Gremlin"
     },
+    "container": { "name": "[my-cosmos-collection]"},
     "identity" : { 
         "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
         "userAssignedIdentity": "/subscriptions/[subscription-id]/resourcegroups/[rg-name]/providers/Microsoft.ManagedIdentity/userAssignedIdentities/[my-user-managed-identity-name]" 
-    },
-    "dataChangeDetectionPolicy": null
+    }
 }
 ```
 
+## Run the indexer to verify permissions
+
 Connection information and permissions on the remote service are validated at run time during indexer execution. If the indexer is successful, the connection syntax and role assignments are valid. For more information, see [Run or reset indexers, skills, or documents](search-howto-run-reset-indexers.md).
 
-## Troubleshooting
+## Troubleshoot connections
+
+* For Azure Cosmos DB for NoSQL, check whether the account has its access restricted to select networks. You can rule out any firewall issues by trying the connection without restrictions in place. Refer to [Indexer access to content protected by Azure network security](search-indexer-securing-resources.md) for more information
 
-For Azure Cosmos DB for NoSQL, check whether the account has its access restricted to select networks. You can rule out any firewall issues by trying the connection without restrictions in place.
+* For Azure Cosmos DB for NoSQL, if the indexer fails due to authentication issues, ensure that the role assignments have been done **both** on the control plane and data plane of the Cosmos DB account.
 
-For Gremlin or MongoDB, if you recently rotated your Azure Cosmos DB account keys, you need to wait up to 15 minutes for the managed identity connection string to work.
+* For Gremlin or MongoDB, if you recently rotated your Azure Cosmos DB account keys, you need to wait up to 15 minutes for the managed identity connection string to work.
 
 ## See also
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Cosmos DBでのマネージドアイデンティティを使用したインデクサ接続の設定ガイドの更新"
}
```

### Explanation
この変更では、Azure Cosmos DBにマネージドアイデンティティを使用したインデクサ接続の設定方法に関するドキュメントが更新されました。主な改訂点は以下の通りです：

1. **著者情報の更新**: 著者及び日付が変更され、新しい情報が反映されています。
2. **認証メカニズムの追加**: マネージドアイデンティティを用いた接続方法が「レガシーアプローチ」と「モダンアプローチ」の二つに分かれて詳細に説明されました。特にモダンアプローチが推奨されており、Azure Cosmos DBのデータ平面に対する役割も設定する必要があることが強調されています。
3. **接続設定の手順更新**: Cosmos DBへの接続手順が改善され、役割の割当てやデータソース定義の具体的な設定方法が詳述されています。また、Azure CLIを通じて設定する手順が含まれており、利用者が容易に実施できるようになっています。
4. **制限事項の明確化**: GremlinおよびMongoDBコレクションに関しては、現在プレビュー段階であり、レガシーアプローチのみをサポートしていることが記載されています。
5. **トラブルシューティング情報の追加**: コネクションの検証や問題解決に関するヒントが追加され、ユーザーが問題に直面した際の助けとなる情報が提供されています。

これらの変更は、ユーザーがAzure Cosmos DBを利用したインデクサ接続を効率的に管理し、セキュアにデータにアクセスするためのガイドラインを強化しています。

## articles/search/tutorial-csharp-search-query-integration.md{#item-8ad6b5}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,7 @@ The function app authenticates through the SDK to the cloud-based Azure AI Searc
 
 ## Configure secrets in a local.settings.json file
 
-:::code language="json" source="~/azure-search-static-web-app/api/local.settings.json":::
+:::code language="json" source="~/azure-search-static-web-app/api/sample.local.settings.json":::
 
 ## Azure Function: Search the catalog
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# 検索クエリ統合チュートリアルの設定ファイルの変更"
}
```

### Explanation
この変更では、Azure AI Searchに関連するC#の検索クエリ統合チュートリアルにおいて、ローカル設定ファイルの参照先が変更されました。具体的には、以下のポイントが修正されています：

1. **設定ファイル名の更新**: コードスニペット内で参照されている`local.settings.json`ファイルが、`sample.local.settings.json`ファイルに変更されました。これにより、ユーザーがサンプル設定を利用することが促進されることを意図しています。

この変更は、ユーザーがより明確で直感的な設定を行う手助けをすることを目的としており、特に初心者にとっての設定が容易になるよう配慮されています。


