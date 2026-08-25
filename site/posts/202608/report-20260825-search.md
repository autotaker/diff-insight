---
date: '2026-08-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8ce8c73...MicrosoftDocs:ad20cc4
summary: このコード差分では、ドキュメントに対していくつかのマイナーな更新が行われ、SharePoint のアクセス制御リスト、Azure 検索のセキュリティトリミング、Azure
  AI Search のインデックス定義に関する説明が見直されました。これにより、情報がより明確になり、ユーザーが理解しやすくなっています。新しいメタデータが追加され、セキュリティのベストプラクティスも提供されました。互換性に影響する変更はありませんが、より明確な説明により再調整が必要な場合があります。この更新は特に、技術を深く理解し、安全な構成を実現するためのサポートを提供します。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8ce8c73...MicrosoftDocs:ad20cc4){target="_blank"}

# ハイライト
このコード差分では、ドキュメントに対するいくつかのマイナーな更新が実施されました。主に、SharePoint のアクセス制御リストに関する説明、Azure 検索のセキュリティトリミングに関する情報、および Azure AI Search におけるインデックス定義が見直されました。これらの更新により、より明確な説明と新たなメタデータの追加が行われ、ユーザーが情報を理解しやすくなっています。

## 新機能
- メタデータ「ai-usage: ai-assisted」の追加により、AI を活用した情報の使用が促進されました。
- 敏感なフィールドに関する新セクションの追加でベストプラクティスが提供されました。

## 互換性を壊す変更
特に互換性に影響する変更はありませんが、説明が明確になったことで、従来の理解からの再調整が必要な場合があるかもしれません。

## その他の更新
- ドキュメントの日付を2026年8月21日に変更。
- `retrievable` 属性の説明が向上し、挙動が明確化されました。
- フィールド属性設定の注意点を強調。

# インサイト
この更新は、主にドキュメントをよりユーザーに親しみやすくすることを目指したものであり、新機能そのものの追加ではなく、既存の情報の見直しと強化に焦点が当てられています。特に、AI 技術の利用が進む中で、「ai-usage: ai-assisted」のメタデータ追加は、機械学習やAIによる処理を活用するための準備を示唆しています。加えて、フィールドの `retrievable` 属性の動作が明確にされたことで、システムのセキュリティ設定やアクセス制御に対し、より細やかな管理が可能になっています。

この一連のドキュメント変更は、利用者が技術を深く理解し、安全で効果的な構成を行うための足掛かりを提供します。特に機密情報の管理に関して新たに追加されたガイダンスは、セキュリティ意識の高まる現代において重要な役割を果たすでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-indexer-sharepoint-access-control-lists.md](#item-532a24) | minor update | SharePoint アクセス制御リストの説明の更新 | modified | 11 | 13 | 24 | 
| [search-security-trimming-for-azure-search.md](#item-d8ae51) | minor update | Azure 検索のセキュリティトリミングに関する記事の更新 | modified | 7 | 3 | 10 | 
| [search-what-is-an-index.md](#item-5a3344) | minor update | Azure AI Search におけるインデックスの説明の更新 | modified | 12 | 2 | 14 | 


# Modified Contents
## articles/search/search-indexer-sharepoint-access-control-lists.md{#item-532a24}

<details>
<summary>Diff</summary>
````diff
@@ -147,16 +147,16 @@ Each identifier appears in a different location in the Azure portal and maps to
 
 | Identifier | Portal location | Used where | Notes |
 |---|---|---|---|
-| Application (client) ID | **App registrations** > `<your-app>` > **Overview** | `ApplicationId` in the data source connection string; `applicationId` in `sharePointConnectorAppRegistration` | This is the correct ID for most configuration fields. Also called "client ID." |
+| Ingestion app application (client) ID | **App registrations** > `<your-app>` > **Overview** | `ApplicationId` in the data source connection string; `applicationId` in `sharePointConnectorAppRegistration` | This ID is correct for most configuration fields. Also called "client ID." |
 | Application object ID | **App registrations** > `<your-app>` > **Overview** (below Application (client) ID) | Not used in Azure AI Search configuration | Don't confuse this with the Application (client) ID. It appears in the same blade, directly below the client ID. |
 | Service principal object ID | **Microsoft Entra ID** > **Enterprise applications** > `<your-app>` > **Manage** > **Properties** | Not used in Azure AI Search configuration | This is the service principal representation of the app. It's a different GUID from the app registration object ID. |
 | Managed identity principal ID | Managed identity resource > **Properties** or the search service **Identity** blade | Not used directly in Azure AI Search data source or index configuration | Used internally when you set up the federated identity credential on the app registration. The credential you create trusts this identity. |
-| Federated credential object ID | **App registrations** > `<your-app>` > **Manage** > **Certificates & secrets** > **Federated credentials** > `<credential-name>` | `federatedCredentialId` in `sharePointConnectorAppRegistration` | The GUID of the federated identity credential entry itself, not the managed identity's GUID. |
-| Federated credential application ID | System-assigned: **Microsoft Entra ID** > **Enterprise applications** > `<search-service>` > **Properties**; User-assigned: `<managed-identity-resource>` > **Properties** | `FederatedCredentialApplicationId` in the data source connection string | See [Federated credential application ID](#federated-credential-application-id) for the system-assigned identity lookup. |
+| Federated credential object ID | **App registrations** > `<your-app>` > **Manage** > **Certificates & secrets** > **Federated credentials** > `<credential-name>` | Not used in Azure AI Search configuration | Don't use the GUID of the federated identity credential entry for `federatedCredentialId`. |
+| Federated credential application ID | System-assigned: **Microsoft Entra ID** > **Enterprise applications** > `<search-service>` > **Properties**; User-assigned: `<managed-identity-resource>` > **Properties** | `FederatedCredentialApplicationId` in the data source connection string; `federatedCredentialId` in `sharePointConnectorAppRegistration` | See [Federated credential application ID](#federated-credential-application-id) for the managed identity lookup. |
 
 ### Federated credential application ID
 
-For `FederatedCredentialApplicationId` in the data source connection string, use the managed identity's own application (client) ID, not the ingestion app's ID.
+For `FederatedCredentialApplicationId` in the data source connection string and `federatedCredentialId` in the index definition, use the managed identity's own application (client) ID, not the ingestion app's ID.
 
 **System-assigned managed identity:**
 
@@ -165,13 +165,13 @@ For `FederatedCredentialApplicationId` in the data source connection string, use
 1. On the **System assigned** tab, note the **Object (principal) ID**.
 1. Go to **Microsoft Entra ID** > **Manage** > **Enterprise applications**.
 1. Search for your search service name or paste the **Object (principal) ID** into the search box.
-1. Select the result and open **Properties**. Copy the **Application ID** shown here, which is the value for `FederatedCredentialApplicationId`.
+1. Select the result and open **Properties**. Copy the **Application ID** shown here, which is the value for `FederatedCredentialApplicationId` in the data source and `federatedCredentialId` in the index.
 
 **User-assigned managed identity:**
 
 1. Go to the user-assigned managed identity resource.
 1. Select **Settings** > **Properties**.
-1. Copy the **Client ID**, which is the value for `FederatedCredentialApplicationId`.
+1. Copy the **Client ID**, which is the value for `FederatedCredentialApplicationId` in the data source and `federatedCredentialId` in the index.
 
 ## Configure your search service for ACL ingestion and query-time enforcement
 
@@ -325,7 +325,7 @@ The following components work together to enable SharePoint site group resolutio
 + REST API `2026-05-01-preview` or later.
 
 > [!NOTE]
-> `FederatedCredentialApplicationId` in the data source connection string differs from `applicationId` in `sharePointConnectorAppRegistration`, which is the ingestion app's client ID. To find the correct values, see [Find the correct Microsoft Entra identifiers](#find-the-correct-microsoft-entra-identifiers).
+> `FederatedCredentialApplicationId` in the data source connection string and `federatedCredentialId` in `sharePointConnectorAppRegistration` use the managed identity's application ID. The `applicationId` property in `sharePointConnectorAppRegistration` uses the ingestion app's client ID. To find the correct values, see [Find the correct Microsoft Entra identifiers](#find-the-correct-microsoft-entra-identifiers).
 
 ### 2. Configure the index
 
@@ -336,8 +336,8 @@ PUT https://{service}.search.windows.net/indexes/{index}?api-version=2026-05-01-
 {
   "name": "my-sharepoint-acl-index",
   "sharePointConnectorAppRegistration": {
-     "applicationId": "<entra-application-id>",
-     "federatedCredentialId": "<federated-identity-credential-object-id>",
+      "applicationId": "<ingestion-app-client-id>",
+      "federatedCredentialId": "<managed-identity-application-id>",
      "tenantId": "<sharepoint-tenant-id>"
   },
   "fields": [
@@ -349,8 +349,6 @@ PUT https://{service}.search.windows.net/indexes/{index}?api-version=2026-05-01-
 }
 ```
 
-The `federatedCredentialId` value is the object ID of the federated identity credential previously configured on the [Microsoft Entra application registration](search-how-to-index-sharepoint-online.md#configuring-the-registered-application-with-a-managed-identity) used by the indexer.
-
 ### 3. Configure the indexer field mappings
 
 Map the SharePoint metadata fields to the index fields in a single combined mapping block. The first two mappings are the same ones used for standard ACL ingestion; the third mapping activates SharePoint groups resolution.
@@ -429,8 +427,8 @@ After indexing your data and ACLs, you can [query the index](search-query-access
 | `SharePointSiteUrl` is empty or null after indexing even though ACLs are otherwise populating correctly | The indexer emits this metadata under `metadata_spo_site_url`, not `metadata_sharepoint_site_url`. Verify that your indexer field mapping uses `"sourceFieldName": "metadata_spo_site_url"`. If your skillset uses index projections for chunked documents, verify that the projection mapping source is `/document/metadata_spo_site_url`. |
 | The indexer returns 401 or 403 | Grant admin consent on both Microsoft Graph and SharePoint API permissions for your scenario. Use a federated credential (not a client secret) when the scenario requires it. See [Permissions by ACL scenario](#permissions-by-acl-scenario). |
 | Permissions are stale after changing a site, library, list, or folder ACL | Call [`/resync` with `options: ["permissions"]`](#resync-acls-across-the-full-data-source). See [Synchronize permissions between indexed and source content](#synchronize-permissions-between-indexed-and-source-content) for context. |
-| `federatedCredentialId` is rejected when configuring `sharePointConnectorAppRegistration` | Use the ID (GUID) of the federated identity credential on the app registration, not the app object ID or the managed identity principal ID. |
-| The indexer returns `401 Unauthorized` and `FederatedCredentialApplicationId` is set | Verify you used the managed identity's Application ID (found in **Enterprise applications**), not the app registration's Application (client) ID or any Object ID. For a user-assigned managed identity, use the **Client ID** from the managed identity resource's **Properties** page. See [Find the correct Microsoft Entra identifiers](#find-the-correct-microsoft-entra-identifiers). |
+| `federatedCredentialId` is rejected when configuring `sharePointConnectorAppRegistration` | Use the managed identity's application ID, not the federated identity credential's object ID or the managed identity's principal ID. See [Federated credential application ID](#federated-credential-application-id). |
+| The indexer returns `401 Unauthorized` and `FederatedCredentialApplicationId` is set | Verify you used the managed identity's Application ID (found in **Enterprise applications**), not the ingestion app's Application (client) ID (`ApplicationId`) or any Object ID. For a user-assigned managed identity, use the **Client ID** from the managed identity resource's **Properties** page. See [Find the correct Microsoft Entra identifiers](#find-the-correct-microsoft-entra-identifiers). |
 
 For missing, unexpected, or failed query-time results after ACL metadata is indexed, see [Troubleshoot SharePoint permission filtering](troubleshoot-sharepoint-query-permission-filtering.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint アクセス制御リストの説明の更新"
}
```

### Explanation
この変更は、SharePoint アクセス制御リスト (ACL) に関するドキュメントの一部を更新したものです。具体的には、構成項目に関する識別子の説明が修正され、いくつかの表現が改善されました。主な変更点として、アプリケーションおよびフェデレーテッド資格情報の ID を特定する際の注意点が明確化され、従来の用語や表現がより一貫して使用されるようになりました。また、挿入アプリのクライアント ID と管理アイデンティティのクライアント ID の違いを強調し、リファレンスを更新しました。これにより、ユーザーが必要な情報をより容易に理解し、正確に構成を行えることを目的としています。

## articles/search/search-security-trimming-for-azure-search.md{#item-d8ae51}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,8 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 01/23/2026
+ms.date: 08/21/2026
+ai-usage: ai-assisted
 ---
 
 # Security filters for trimming results in Azure AI Search
@@ -66,13 +67,13 @@ In the search index, within the fields collection, you need one field that conta
 
 1. Set the field's `filterable` attribute set to `true`.
 
-1. Set the field's `retrievable` attribute to `false` so that it isn't returned as part of the search request.
+1. Set the field's `retrievable` attribute to `false` so that it isn't returned as part of the search response.
 
 1. Indexes require a document key. The "file_id" field satisfies that requirement. 
 
 1. Indexes should also contain searchable and retrievable content. The "file_name" and "file_description" fields represent that in this example.
 
-   The following index schema satisfies the field requirements. Documents that you index on Azure AI Search should have values for all of these fields, including the "group_ids". For the document with `file_name` "secured_file_b", only users that belong to group IDs "group_id1" or "group_id2" have read access to the file.
+    The following index schema satisfies the field requirements. Documents that you index on Azure AI Search should have values for all of these fields, including the `group_ids`. A query returns the document with `file_name` `secured_file_b` when its security filter includes `group_id1` or `group_id2`.
 
    ```https
    POST https://[search service].search.windows.net/indexes/securedfiles/docs/index?api-version=2026-04-01
@@ -87,6 +88,9 @@ In the search index, within the fields collection, you need one field that conta
     }
    ```
 
+> [!NOTE]
+> Setting `retrievable` to `false` prevents `group_ids` from being returned as part of a document in search results. It isn't a content-obfuscation or field-level security mechanism. In this pattern, document-level authorization is enforced by applying the security filter to every query. Don't rely on `retrievable` alone to protect sensitive information from all query features or response formats.
+
 ## Push data into your index using the REST API
 
 Populate your search index with documents that provide values for each field in the fields collection, including values for the security field. Azure AI Search doesn't provide APIs or features for populating the security field specifically. However, several of the examples listed at the end of this article explain techniques for populating this field.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure 検索のセキュリティトリミングに関する記事の更新"
}
```

### Explanation
この変更は、Azure AI Search におけるセキュリティトリミングに関する記事のいくつかの要素を更新したものです。具体的には、ドキュメントの日付が2026年1月23日から2026年8月21日に変更され、新たに「ai-usage: ai-assisted」のメタデータが追加されました。さらに、検索応答におけるフィールドの属性に関する説明が修正され、`retrievable` 属性が `false` に設定された場合の挙動が明確化されました。これにより、セキュリティフィルターを適用したクエリがどのように動作するかがより理解しやすくなり、ユーザーは適切なセキュリティ設定を行うための情報を得ることができます。また、注意書きが追加され、`retrievable` 属性の使用についての制限が強調されました。

## articles/search/search-what-is-an-index.md{#item-5a3344}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,9 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 01/27/2026
+ms.date: 08/21/2026
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Search indexes in Azure AI Search
@@ -105,13 +106,22 @@ Field attributes determine how a field is used, such as whether it's used in ful
 |sortable |By default the system sorts by a search score, but you can configure an explicit sort based on fields in the documents. Fields of type `Collection(Edm.String)` can't be sortable. |  
 |facetable |Typically used in a presentation of search results that includes a hit count by category (for example, hotels in a specific city). This option can't be used with fields of type `Edm.GeographyPoint`. Fields of type `Edm.String` that are filterable, sortable, or facetable can be at most 32 kilobytes in length. For details, see [Create Index (REST API)](/rest/api/searchservice/indexes/create).|  
 |key |Unique identifier for documents within the index. Exactly one field must be chosen as the key field and it must be of type `Edm.String`.|  
-|retrievable |Determines whether the field can be returned in a search result. This is useful when you want to use a field (such as *profit margin*) as a filter, sorting, or scoring mechanism, but don't want the field to be visible to the end user. This attribute must be `true` for `key` fields.|  
+|retrievable |Indicates whether the field can be returned as part of a document in search results. Setting this attribute to `false` excludes the field from returned document fields, and the field can't be requested through `$select`. This setting doesn't prevent internal use by search features that depend on indexed content or schema configuration. Depending on the feature configuration, field content or derived information can still contribute to outputs such as highlighting, facets, ranking, filtering, sorting, or other query processing. This attribute must be `true` for `key` fields.|
 
 Although you can add new fields at any time, existing field definitions are locked in for the lifetime of the index. For this reason, developers typically use the Azure portal for creating simple indexes, testing ideas, or using the Azure portal pages to look up a setting. Frequent iteration over an index design is more efficient if you follow a code-based approach so that you can rebuild the index easily.
 
 > [!NOTE]
 > The APIs you use to build an index have varying default behaviors. For the [REST APIs](/rest/api/searchservice/indexes/create), most attributes are enabled by default (for example, searchable and retrievable are true for string fields) and you often only need to set them if you want to turn them off. For the .NET SDK, the opposite is true. On any property you don't explicitly set, the default is to disable the corresponding search behavior unless you specifically enable it.
 
+## Best practices for sensitive fields
+
+If a field contains sensitive or confidential information:
+
++ Enable only the field attributes required by your application, such as `searchable`, `filterable`, or `facetable`.
++ Configure field attributes explicitly instead of relying on API or SDK defaults.
++ Don't assume that excluding a field from document results prevents disclosure through all query features or response formats.
++ Review application and feature requirements before storing sensitive information in the search index.
+
 <a name="index-size"></a>
 
 ## Physical structure and size
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search におけるインデックスの説明の更新"
}
```

### Explanation
この変更は、Azure AI Search におけるインデックスの定義とその特徴に関する記事を更新したものです。特に、日付が2026年1月27日から2026年8月21日に変更され、「ai-usage: ai-assisted」というメタデータが追加されました。主な内容の修正として、フィールド属性 `retrievable` の説明がより詳しくなり、この属性が `false` に設定された場合の効果や注意点が明確化されました。これにより、フィールドが検索結果でどのように使用されるか、またはその内容が内部的にどのように利用されるかについての理解が深まります。

さらに、新たに「敏感なフィールドに関するベストプラクティス」というセクションが追加され、機密情報を含むフィールドに対する推奨事項が示されました。このセクションでは、フィールド属性の設定や情報の取り扱いに関する重要なガイダンスが提供され、ユーザーが安全に情報を管理するための情報が強化されています。


