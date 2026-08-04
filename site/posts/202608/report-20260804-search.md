---
date: '2026-08-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:93ed0d0...MicrosoftDocs:f5c6198
summary: このアップデートは、Azure AI Search関連の文書に対する小規模な改訂を行ったもので、主に新しいガイダンスや設定手順、フィールド名の変更、そして制限やクォータに関するセクションの追加が含まれています。特に、インデックスプロジェクション定義でのフィールド名変更や、SharePoint
  URLフィールド名の改訂があり、これによりアクセス制御の整合性が担保されています。また、新機能としては認知検索のカスタムスキルにおけるIP制御やタイムアウトの設定が追加され、ユーザーの設定精度と効率が向上しています。全体として、この更新はAzureサービスの利便性とユーザー体験を向上させる目的で設計されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:93ed0d0...MicrosoftDocs:f5c6198){target="_blank"}

<format>
# ハイライト
この更新は、Azure AI Search関連の複数の文書に対する小幅な更新です。主な新機能として、新規のガイダンスや設定手順、フィールド名の変更、そして制限やクォータについてのセクション追加が含まれています。破壊的変更としては、いくつかのフィールド名の変更があります。

## 新機能
- ファイル知識ソース利用時のファイル名重複対応とファイルID生成。
- 認知検索のカスタムスキルインターフェースにおけるIP制御とタイムアウトキュー。
- SharePoint Onlineインデクシングでの詳細な設定手順。
- クォータ、キャパシティ、制限診断に関するセクションの追加。

## 破壊的変更
- インデックスプロジェクション定義でのフィールド名変更: `metadata_sharepoint_site_url`が`metadata_spo_site_url`に。
- RBAC文書でのSharePoint URLフィールド名の変更。

## その他の更新
- 目次ファイル更新により、モニタリングデータ参照の追加と削除が行われました。
- Azure AI Search文書の日付情報の更新。

# インサイト
今回のアップデートでは、主に複数の技術文書の明確化と最新情報の反映が行われ、エンタープライズユーザーにおいてAzure AI Searchを利用した設定の正確性と効率性を強化しています。新機能としては、認知検索カスタムスキルのIP制御やタイムアウトの具体的設定方法が追加され、より確実なインデックス運用やトラブルシュートが可能になっています。

特に、SharePoint OnlineやAzure AI Searchにおける設定手順の拡充は実用的価値が高く、ユーザーがそれぞれの環境に合った細かな設定ができるよう設計されています。クォータや制限に関する情報追加も、より正確なリソース管理をサポートするもので、開発者やインフラ担当者にとって助かる内容です。

今回の変更におけるフィールド名更新は、エンタープライズレベルのアクセス制御における整合性を確保し、ドキュメント内でのリファレンスの正確さを保証しています。これにより、ユーザーはAzure AI Searchを用いた認証やアクセス制御をより安全に行うことができます。全体的に、文書更新がAzureサービスの利用効率を高め、ユーザー体験を向上させるための設計的意図が感じられます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-file.md](#item-88f720) | minor update | エージェント知識ソースのファイルに関する文書の更新 | modified | 6 | 5 | 11 | 
| [agentic-knowledge-source-overview.md](#item-dcf29a) | minor update | エージェント知識ソース概要の更新 | modified | 1 | 1 | 2 | 
| [cognitive-search-custom-skill-interface.md](#item-4cb17d) | minor update | 認知検索カスタムスキルインターフェースの文書更新 | modified | 2 | 0 | 2 | 
| [cognitive-search-custom-skill-web-api.md](#item-5d1065) | minor update | 認知検索カスタムスキルWeb APIの文書更新 | modified | 5 | 1 | 6 | 
| [search-blob-indexer-role-based-access.md](#item-887e42) | minor update | Blobインデクサーの役割ベースアクセスに関する文書更新 | modified | 1 | 3 | 4 | 
| [search-how-to-define-index-projections.md](#item-a7e2c5) | minor update | インデックスプロジェクション定義に関する文書更新 | modified | 2 | 2 | 4 | 
| [search-how-to-index-sharepoint-online.md](#item-8c099c) | minor update | SharePoint Onlineインデクシングに関する文書の拡張 | modified | 58 | 7 | 65 | 
| [search-indexer-access-control-lists-and-role-based-access.md](#item-67b42f) | minor update | アクセス制御リストと役割ベースアクセスに関する文書の更新 | modified | 1 | 4 | 5 | 
| [search-indexer-howto-access-ip-restricted.md](#item-aec22f) | minor update | IP制限されたデータアクセスのためのインデクサ設定の更新 | modified | 3 | 2 | 5 | 
| [search-indexer-sensitivity-labels.md](#item-2a7bfc) | minor update | 感度ラベルに関する文書の更新 | modified | 0 | 2 | 2 | 
| [search-indexer-sharepoint-access-control-lists.md](#item-532a24) | minor update | SharePointアクセス制御リストに関する文書の更新 | modified | 85 | 50 | 135 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | Azure AI Searchの制限とクォータの診断に関する情報追加 | modified | 18 | 0 | 18 | 
| [search-query-access-control-rbac-enforcement.md](#item-d24df7) | minor update | SharePointサイトURLに関するフィールド名の更新 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c4768f) | minor update | 目次にモニタリングデータ参照の追加と削除 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-file.md{#item-88f720}

<details>
<summary>Diff</summary>
````diff
@@ -21,11 +21,11 @@ zone_pivot_groups: search-csharp-python-rest
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-A *file knowledge source* (preview) uploads small and medium file sets directly to Azure AI Search for agentic retrieval. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
+A *file knowledge source* (preview) uploads small-to-medium file sets directly to Azure AI Search for agentic retrieval. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
 File knowledge sources are useful when you want a managed upload experience instead of provisioning Azure Storage, configuring access, and creating an indexer pipeline over an external container. Azure AI Search processes uploaded files so their extracted content can be retrieved from a knowledge base.
 
-If your content already lives in Azure Blob Storage or ADLS Gen2, or if you need large-scale ingestion or storage account capabilities, use a [blob knowledge source](agentic-knowledge-source-how-to-blob.md) instead.
+A file knowledge source supports up to 100 files. Use a [blob knowledge source](agentic-knowledge-source-how-to-blob.md) instead when your files are already in Azure Blob Storage or Azure Data Lake Storage Gen2, when your file set exceeds or is likely to exceed 100 files, or when you need scheduled ingestion. Also use a blob knowledge source when you want to manage source blobs with [Azure Blob Storage lifecycle management policies](/azure/storage/blobs/lifecycle-management-overview) or when you need [document-level permissions (preview)](agentic-knowledge-source-how-to-blob.md#enforce-document-level-permissions-preview) based on permissions in Azure Storage.
 
 ### Usage support
 
@@ -81,7 +81,8 @@ The following limits apply to file knowledge sources.
 | Maximum files per file knowledge source | 100 |
 
 > [!NOTE]
-> Uploaded content is stored in the generated search index. For total storage limits by pricing tier, see [Service limits](search-limits-quotas-capacity.md#service-limits).
+> + Uploading the same file name doesn't replace an existing file. For more information, see [Upload files](#upload-files).
+> + The generated search index stores the uploaded content. For total storage limits by pricing tier, see [Service limits](search-limits-quotas-capacity.md#service-limits).
 
 
 ## Check for existing knowledge sources
@@ -309,9 +310,9 @@ Content-Disposition: attachment; filename="installation-guide.pdf"
 ::: zone-end
 
 > [!NOTE]
-> Uploading a file doesn't replace an existing file, even if you reuse the same `fileName`. Each upload creates a new file with its own `fileId`, so the list of uploaded files can contain multiple entries that share a `fileName`.
+> Uploading a file doesn't replace an existing file, even if you reuse the same `fileName`. Each successful upload creates a new file with its own `fileId`, so the list of uploaded files can contain multiple entries that share a `fileName`.
 >
-> To replace content, delete the prior file by `fileId` before or after the new upload.
+> To replace content, delete the prior file by `fileId` before you upload the replacement.
 
 ## List uploaded files
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースのファイルに関する文書の更新"
}
```

### Explanation
このコードの変更は、エージェント知識ソースに関連するファイルの取り扱いに関する解説文書の一部を更新するものです。主な変更点は、ファイルのアップロードや使用制限についての説明が明確化されたことです。また、一部の文言が修正され、ファイル名が重複する場合の取り扱いや、ファイルの置き換えに関する注意が追加されています。

これにより、利用者がファイル知識ソースを使用する際の理解が深まり、既存のファイルと新しいファイルの扱いについての誤解を避ける手助けとなる内容が含まれています。さらに、追加された情報として、ファイルの名称が重複した場合でも新しいファイルIDが生成される点や、古いファイルを削除する必要があることが強調されています。全体として、このアップデートは文書の明確さと正確性を向上させることを目的としています。

## articles/search/agentic-knowledge-source-overview.md{#item-dcf29a}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: What is a Knowledge Source?
 description: Learn about the knowledge source object used for agentic retrieval workloads in Azure AI Search.
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 06/02/2026
+ms.date: 07/30/2026
 ai-usage: ai-assisted
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソース概要の更新"
}
```

### Explanation
この変更は、エージェント知識ソースに関する概要文書の日付情報を更新するものです。具体的には、「ms.date」フィールドが2026年6月2日から2026年7月30日に変更されました。この更新は、文書の公開日が正確に反映されるようにするために行われており、利用者が最新の情報にアクセスできることを保証します。内容そのものに大きな変更はありませんが、日付のアップデートは、文書の信頼性や最新性を維持するために重要です。

## articles/search/cognitive-search-custom-skill-interface.md{#item-4cb17d}

<details>
<summary>Diff</summary>
````diff
@@ -51,6 +51,8 @@ Ensure that `uri` points to the endpoint of the application identified by `authR
 
 By default, the connection to the endpoint times out if a response isn't returned within a 30-second window (`PT30S`). The indexing pipeline is synchronous, and indexing produces a timeout error if a response isn't received in that time frame. You can increase the interval to a maximum value of 230 seconds by setting the `timeout` parameter (`PT230S`).
 
+If an endpoint protected by IP access restrictions doesn't respond, temporarily set `timeout` to a short value, such as `PT10S`, to surface the timeout error faster. For an Azure function app, manage inbound IP rules under **Settings** > **Networking** > **Access restrictions**. For the IP addresses to allow, see [Configure IP firewall rules to allow indexer connections](search-indexer-howto-access-ip-restricted.md).
+
 ## Format web API inputs
 
 The web API must accept an array of records to process. Within each record, provide a property bag as input to your web API.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "認知検索カスタムスキルインターフェースの文書更新"
}
```

### Explanation
この変更は、認知検索におけるカスタムスキルインターフェースに関する文書の内容を更新したものです。主な追加内容として、エンドポイントがIPアクセス制限で保護されている場合のタイムアウト設定に関する具体的な指示が含まれています。具体的には、応答がない場合はタイムアウトを10秒（`PT10S`）に短縮することで、タイムアウトエラーを迅速に表示できることが言及されています。

また、Azure FunctionアプリでのインバウンドIPルールの管理方法や、インデクサー接続を許可するためのIPファイアウォールルールの構成に関するリファレンスリンクも追加されています。さらに、ウェブAPIがレコードの配列を受け入れる必要があることに関する説明も加わり、文書がより明確かつ実用的になっています。これらの改善により、開発者が認知検索を効果的に利用するためのガイダンスが強化されています。

## articles/search/cognitive-search-custom-skill-web-api.md{#item-5d1065}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.custom:
   - ignite-2023
 ai-usage: ai-assisted
 ms.topic: reference
-ms.date: 07/28/2026
+ms.date: 07/30/2026
 ms.update-cycle: 365-days
 ---
 
@@ -280,6 +280,10 @@ For cases when the Web API is unavailable or returns an HTTP error, the indexer
 
 When using managed identity authentication with a Custom Web API skill, Azure AI Search obtains a Microsoft Entra access token for the application identified by `authResourceId` and includes that token in requests sent to the endpoint specified by `uri`. The endpoint referenced by `uri` is typically your Azure Function, Azure App Service, Azure API Management endpoint, or another Microsoft Entra-protected application. You're responsible for configuring and maintaining the relationship between the endpoint and the application identified by `authResourceId`.
 
+Regardless of the authentication method, custom skill inputs can contain values from customer-provided documents or values derived from those documents. Treat all custom skill inputs as untrusted. Azure AI Search forwards the inputs configured in the skillset to your endpoint without interpreting, validating, or constraining their content for your custom implementation.
+
+Validate and constrain document-derived values in your custom skill before using them in outbound requests or other security-sensitive operations. Use input validation, destination allowlists, URL and hostname validation, protocol restrictions, and least-privilege network access that permits only the destinations and ports the skill requires. For more information, see [Architecture strategies for networking and connectivity](/azure/well-architected/security/networking#classify-the-traffic-flows).
+
 ### Recommended security practices
 
 To help maintain a secure deployment, follow these practices:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "認知検索カスタムスキルWeb APIの文書更新"
}
```

### Explanation
この変更は、認知検索のカスタムスキルWeb APIに関する文書を更新したもので、いくつかの重要なポイントが追加されています。まず、文書の日付が2026年7月28日から2026年7月30日に変更され、最新の情報が反映されるようにしています。

主な内容として、カスタムスキルの入力が信頼できないものとみなされるべきであるという警告が含まれており、ドキュメント由来の値や顧客提供のドキュメントから派生した値をカスタムスキル入力に使用する際の注意点が強調されています。Azure AI Searchは、スキルセットで構成された入力をエンドポイントに送信する際、それらの内容を解釈したり検証したりしないため、入力の検証や制約を自らのカスタムスキルで行う必要があります。

さらに、アウトバウンドリクエストやその他のセキュリティに敏感な操作に使用する前に、これらの値を検証し、制約を設けるべきであると説明しており、ネットワーク接続やセキュリティに関する推奨プラクティスへのリファレンスも提供されています。このような更新により、利用者がより安全にカスタムスキルを実装できるようにガイダンスが強化されています。

## articles/search/search-blob-indexer-role-based-access.md{#item-887e42}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to configure Azure AI Search knowledge sources and indexe
 ms.reviewer: vaishalishah
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/12/2026
+ms.date: 07/28/2026
 ms.custom:
   - dev-focus
 ai-usage: ai-assisted
@@ -64,8 +64,6 @@ This article focuses on the indexing automation approaches, built on this founda
 
   + [Custom Web API skill](cognitive-search-custom-skill-web-api.md)
 
-  + [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md)
-
   + [Knowledge store](knowledge-store-concept-intro.md)
 
   + [Indexer enrichment cache](enrichment-cache-how-to-configure.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blobインデクサーの役割ベースアクセスに関する文書更新"
}
```

### Explanation
この変更は、Blobインデクサーに関する役割ベースアクセスの文書を更新したもので、主に以下の点が修正されています。まず、文書の日付が2026年5月12日から2026年7月28日に変更され、新しい情報が正確に反映されるようになっています。

さらに、文中の関連リンクのリストから「GenAI Prompt skill」という項目が削除され、残りのスキルやリソースのリストが整理されています。具体的には、カスタムWeb APIスキルやナレッジストア、インデクサーエンリッチメントキャッシュに関するリンクが引き続き残されており、関連情報へのアクセスが維持されています。

このような更新により、文書がより明確で時宜を得たものとなり、ユーザーがBlobインデクサーの役割ベースアクセスを効果的に活用できるようにサポートが強化されています。

## articles/search/search-how-to-define-index-projections.md{#item-a7e2c5}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 06/02/2026
+ms.date: 07/28/2026
 ms.update-cycle: 180-days
 ---
 
@@ -162,7 +162,7 @@ Index projections are generally available. We recommend the most recent stable A
 
 Here's an example payload for an index projections definition that you might use to project individual pages output by the [Text Split skill](cognitive-search-skill-textsplit.md) as their own documents in the search index.
 
-When the parent document carries permission metadata used for document-level access, such as `metadata_user_ids`, `metadata_group_ids`, or `metadata_sharepoint_site_url`, include those fields in `mappings` so that every chunk inherits them. For more information, see [Choose where to populate ACL fields](search-indexer-sharepoint-access-control-lists.md#choose-where-to-populate-acl-fields).
+If the parent document carries permission metadata for document-level access, such as `metadata_user_ids`, `metadata_group_ids`, or `metadata_spo_site_url`, include those fields in `mappings`. Every chunk must inherit them for query-time permission filters to apply. For more information, see [Choose where to populate ACL fields](search-indexer-sharepoint-access-control-lists.md#choose-where-to-populate-acl-fields).
 
 ```json
 "indexProjections": {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスプロジェクション定義に関する文書更新"
}
```

### Explanation
この変更は、インデックスプロジェクションの定義に関する文書の更新を行ったもので、いくつかの重要な修正が含まれています。最初に、文書の日付が2026年6月2日から2026年7月28日に変更され、最新情報が反映されています。

具体的には、親ドキュメントに関連する許可メタデータに関する説明がより明確になっています。元の文では「parent document carries permission metadata used for document-level access」と記載されていますが、変更後は「If the parent document carries permission metadata for document-level access」となり、文が読みやすく、条件付きでの説明が強調されています。また、「metadata_sharepoint_site_url」が「metadata_spo_site_url」と修正されています。

これにより、クエリ時のアクセス許可フィルターが適用されるためには、すべてのチャンクがこれらのフィールドを継承する必要があることが強調されています。この更新は、インデックスプロジェクションの利用に関する理解を深めるために重要であり、ユーザーにとって役立つ内容となっています。

## articles/search/search-how-to-index-sharepoint-online.md{#item-8c099c}

<details>
<summary>Diff</summary>
````diff
@@ -311,7 +311,13 @@ api-key: [admin key]
 }
 ```
 
-For user-assigned managed identities, supply the `identity` block in the data source and omit `FederatedCredentialApplicationId` from the connection string. For system-assigned managed identities, set `FederatedCredentialApplicationId` in the connection string (see the connection-string formats below).
+Federated credential configurations require `FederatedCredentialApplicationId` in the connection string. The value differs by identity type:
+
+- **System-assigned managed identity**: Set `FederatedCredentialApplicationId` to the service's system-assigned managed identity application (client) ID. Omit the `identity` block.
+- **User-assigned managed identity**: Supply the `identity` block with the user-assigned managed identity resource path. Set `FederatedCredentialApplicationId` to the user-assigned managed identity's own application (client) ID.
+
+> [!NOTE]
+> `ApplicationId` and `FederatedCredentialApplicationId` are different values. `ApplicationId` is your registered Entra ingestion app that holds the SharePoint permissions. `FederatedCredentialApplicationId` is the application (client) ID of the managed identity itself, which is the entity whose token proves the managed identity's identity.
 
 ```http
 POST https://[service name].search.windows.net/datasources?api-version=2026-05-01-preview
@@ -344,7 +350,7 @@ The format of the connection string changes based on whether the indexer is usin
 
 + Application API permissions with secretless (federated identity credential) connection string format:
 
-    `SharePointOnlineEndpoint=[SharePoint site url];ApplicationId=[Azure AD App ID];FederatedCredentialApplicationId=[Entra application (client) ID that the FIC federates to];TenantId=[SharePoint site tenant id]`
+    `SharePointOnlineEndpoint=[SharePoint site url];ApplicationId=[Azure AD App ID];FederatedCredentialApplicationId=[managed identity's application (client) ID];TenantId=[SharePoint site tenant id]`
 
 The following table describes each connection string field.
 
@@ -354,7 +360,7 @@ The following table describes each connection string field.
 | `ApplicationId` | Yes | Microsoft Entra application (client) ID of the ingestion app. Must be a valid GUID. |
 | `TenantId` | Optional | Microsoft Entra tenant GUID. Required when the SharePoint site is in a different tenant from the search service. |
 | `ApplicationSecret` | Conditional | Client secret of the ingestion app. Use for secret-based authentication. |
-| `FederatedCredentialApplicationId` | Conditional (FIC mode) | Microsoft Entra application (client) ID that the federated identity credential federates to. Must be a valid GUID. |
+| `FederatedCredentialApplicationId` | Conditional (federated identity credential) | Microsoft Entra application (client) ID used to validate the managed identity. Must be a valid GUID. For a system-assigned managed identity, use the identity's application (client) ID. For a user-assigned managed identity, use the identity's own application (client) ID. For a cross-tenant user-assigned managed identity with `federatedIdentityClientId` set in the `identity` block, use the multi-tenant app's client ID. |
 
 > [!IMPORTANT]
 > `FederatedCredentialApplicationId` and `ApplicationSecret` are mutually exclusive. Connection strings that combine them are rejected on data source create or update.
@@ -369,23 +375,67 @@ You can get the managed identity `object (principal) ID` from the [Configuring t
 When setting up permissions, consider the following information:
 > If the SharePoint site is in the same tenant as the search service and system-assigned managed identity is enabled, `TenantId` doesn't have to be included in the connection string. If the SharePoint site is in a different tenant from the search service, `TenantId` must be included.
 
-The following example shows a data source created with `FederatedCredentialApplicationId`:
+The following examples show data sources created with `FederatedCredentialApplicationId`:
+
+**System-assigned managed identity with federated credential:**
 
 ```http
-PUT https://[service name].search.windows.net/datasources/sharepoint-ds?api-version=2026-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2026-05-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
 {
   "name": "sharepoint-ds",
   "type": "sharepoint",
   "credentials": {
-    "connectionString": "SharePointOnlineEndpoint=https://[your-tenant-name].sharepoint.com;ApplicationId=[Azure AD App ID];TenantId=[SharePoint site tenant id];FederatedCredentialApplicationId=[Entra application (client) ID that the FIC federates to]"
+    "connectionString": "SharePointOnlineEndpoint=https://[your-tenant-name].sharepoint.com;ApplicationId=[Azure AD App ID];TenantId=[SharePoint site tenant id];FederatedCredentialApplicationId=[system-assigned managed identity's application (client) ID]"
   },
   "container": { "name": "defaultSiteLibrary" }
 }
 ```
 
+**User-assigned managed identity with federated credential (single-tenant):**
+
+```json
+{
+  "name": "sharepoint-uami-fed",
+  "type": "sharepoint",
+  "credentials": {
+    "connectionString": "SharePointOnlineEndpoint=https://[your-tenant-name].sharepoint.com;ApplicationId=[Azure AD App ID];TenantId=[SharePoint site tenant id];FederatedCredentialApplicationId=[user-assigned managed identity application (client) ID]"
+  },
+  "container": { "name": "defaultSiteLibrary" },
+  "identity": {
+    "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
+    "userAssignedIdentity": "/subscriptions/[subscription-id]/resourceGroups/[resource-group]/providers/Microsoft.ManagedIdentity/userAssignedIdentities/[uami-name]"
+  }
+}
+```
+
+> [!NOTE]
+> For a user-assigned managed identity, `FederatedCredentialApplicationId` must equal the user-assigned managed identity's application (client) ID, not the ingestion app's ID (`ApplicationId`). If you omit the `identity` block, the indexer falls back to the system-assigned managed identity.
+
+**Cross-tenant user-assigned managed identity with federated credential (advanced):**
+
+Before using this configuration, ensure your user-assigned managed identity is configured with a federated identity credential that trusts the multi-tenant Entra app. For setup steps, see [Configuring the registered application with a managed identity](#configuring-the-registered-application-with-a-managed-identity).
+
+```json
+{
+  "name": "sharepoint-uami-crosstenantfed",
+  "type": "sharepoint",
+  "credentials": {
+    "connectionString": "SharePointOnlineEndpoint=https://[your-tenant-name].sharepoint.com;ApplicationId=[Azure AD App ID];TenantId=[SharePoint site tenant id];FederatedCredentialApplicationId=[multi-tenant app client ID]"
+  },
+  "container": { "name": "defaultSiteLibrary" },
+  "identity": {
+    "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
+    "userAssignedIdentity": "/subscriptions/[subscription-id]/resourceGroups/[resource-group]/providers/Microsoft.ManagedIdentity/userAssignedIdentities/[uami-name]",
+    "federatedIdentityClientId": "[multi-tenant app client ID]"
+  }
+}
+```
+
+Use the cross-tenant user-assigned managed identity configuration when the user-assigned managed identity itself federates to a multi-tenant Entra app. In this case, set `federatedIdentityClientId` in the `identity` block to the multi-tenant app's client ID, and set `FederatedCredentialApplicationId` in the connection string to the **same** multi-tenant app's client ID. Setting `FederatedCredentialApplicationId` to the user-assigned managed identity's own client ID in this scenario fails validation.
+
 If your indexer uses [SharePoint ACL configuration (preview)](search-indexer-sharepoint-access-control-lists.md) or [preserves and honors Microsoft Purview sensitivity labels (preview)](search-indexer-sensitivity-labels.md), review the related articles before you create the indexer. Each feature has specific data source, index, and skillset configuration steps.
 
 ### Step 5: Create an index
@@ -571,7 +621,8 @@ If you index document metadata (`"dataToExtract": "contentAndMetadata"`), you ca
 | metadata_spo_item_content_type | Edm.String | The content type of the item. | 
 | metadata_spo_item_extension | Edm.String | The extension of the item. |
 | metadata_spo_item_weburi | Edm.String | The URI of the item. |
-| metadata_spo_item_path | Edm.String | The combination of the parent path and item name. | 
+| metadata_spo_item_path | Edm.String | The combination of the parent path and item name. |
+| metadata_spo_site_url | Edm.String | The URL of the SharePoint site. Required when you enable SharePoint site group resolution. See [Configure SharePoint groups support](search-indexer-sharepoint-access-control-lists.md#configure-sharepoint-groups-support). |
 
 The SharePoint in Microsoft 365 indexer also supports metadata specific to each document type. For more information, see [Content metadata properties used in Azure AI Search](search-blob-metadata-properties.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint Onlineインデクシングに関する文書の拡張"
}
```

### Explanation
この変更は、SharePoint Onlineをインデクシングするための方法を説明する文書に対して行われた拡張を含んでいます。具体的には、58件の追加と7件の削除が行われ、合計で66の変更が加えられています。

主な変更点として、設定手順が詳しく説明され、管理IDの種類に応じた接続文字列の構成についての情報が増えています。特に、「FederatedCredentialApplicationId」に関する新しいガイダンスが含まれ、システム割り当て管理IDとユーザー割り当て管理IDそれぞれの設定方法が明確に示されています。また、ユーザー管理IDを用いる場合の注意点も強調されています。

接続文字列の構造も更新されており、具体的な例が追加されて、使いやすさが向上しています。さらに、クロステナントのユーザー割り当て管理IDを使用する際の詳細な設定例も掲載されており、特定のシナリオにおける設定方法が理解しやすくなっています。

このような文書の更新は、ユーザーがSharePoint Onlineのインデクシングを正確に実行できるようにサポートするものであり、機能の利用に関する情報の充実を図っています。

## articles/search/search-indexer-access-control-lists-and-role-based-access.md{#item-67b42f}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to configure Azure AI Search indexers for ingesting Acces
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 04/24/2026
+ms.date: 07/28/2026
 ai-usage: ai-assisted
 ---
 
@@ -53,8 +53,6 @@ This article explains how to configure an ADLS Gen2 indexer or ADLS Gen2 blob kn
 
   + [Custom Web API skill](cognitive-search-custom-skill-web-api.md)
 
-  + [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md)
-
   + [Knowledge store](knowledge-store-concept-intro.md)
 
   + [Indexer enrichment cache](enrichment-cache-how-to-configure.md)
@@ -154,7 +152,6 @@ Key points about the configuration that make it work for this scenario:
 
 + `isADLSGen2` is set to true, meeting the data source requirement for this scenario.
 + `ingestionPermissionOptions` specifies user and group IDs.
-+ `disableImageVerbalization` is set to true because the GenAI Prompt skill that backs this experience isn't currently supported in ADLS Gen2 permission inheritance.
 
 ```http
 # Create / Update Azure Blob Knowledge Source
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アクセス制御リストと役割ベースアクセスに関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchインデクサにおけるアクセス制御リストと役割ベースアクセスについての文書に対するマイナーな更新です。具体的には、4件の削除と1件の追加が行われ、合計で5件の変更が加えられています。

主な変更点は、文書の日付が2026年4月24日から2026年7月28日に更新されたことです。これにより、読者は最新の情報が反映されていることを確認できます。

また、リストから「GenAI Prompt skill」に関する項目が削除されました。この変更は、ADLS Gen2の権限継承における現在のサポート状況を反映したものと考えられます。加えて、設定に関する説明も若干調整され、一部の内容が削除されていますが、全体の文脈における重要な情報は保たれています。

この更新により、ユーザーは現在のAzure AI Searchインデクサに関する正確な設定方法を理解しやすくなり、特に権限やアクセスに関連する新たな状況への適応が進められています。

## articles/search/search-indexer-howto-access-ip-restricted.md{#item-aec22f}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Configure IP firewall rules to allow data access by an Azure AI Sea
 ms.reviewer: arjagann
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/13/2026
+ms.date: 07/28/2026
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
@@ -19,7 +19,7 @@ ai-usage: ai-assisted
 
 Azure AI Search makes external, outbound calls during indexer processing for content and skills, and for agentic retrieval requests that include calls to large language models (LLMs). If the target Azure resource uses IP firewall rules to filter incoming calls, you must create an inbound rule in your firewall that admits requests from Azure AI Search.
 
-This article explains how to find the IP address of your search service and configure an inbound IP rule on an Azure Storage account. While specific to Azure Storage, this approach also works for other Azure resources that use IP firewall rules for data access, such as Azure Cosmos DB and Azure SQL.
+This article explains how to find the IP address of your search service and configure an inbound IP rule on an Azure Storage account. While specific to Azure Storage, this approach also works for other Azure resources that use IP firewall rules for data access, such as Azure Cosmos DB, Azure SQL, and function apps hosting custom skills.
 
 ## Prerequisites
 
@@ -154,3 +154,4 @@ If you don't need key-based authentication, we recommend that you disable API ke
 - [Configure Azure Storage firewalls](/azure/storage/common/storage-network-security)
 - [Configure an IP firewall for Azure Cosmos DB](/azure/cosmos-db/how-to-configure-firewall)
 - [Configure IP firewall for Azure SQL Server](/azure/azure-sql/database/firewall-configure)
+- [Manage Azure Functions inbound access restrictions](/azure/azure-functions/functions-networking-options#inbound-access-restrictions)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "IP制限されたデータアクセスのためのインデクサ設定の更新"
}
```

### Explanation
この変更は、IP制限されたデータアクセスのためのAzure AI Searchインデクサの設定に関する文書に対して行われたマイナーな更新です。具体的には、3件の追加と2件の削除が行われ、合計で5件の変更が加えられています。

主な変更点は、文書の日付が2026年3月13日から2026年7月28日に更新されたことです。これにより、最新の情報が反映されていることを示しています。

また、説明文には「Azure SQL」や「Azure Cosmos DB」に加えて、「カスタムスキルをホスティングする関数アプリ」のサポートが追加され、IPファイアウォールルールを用いるAzureリソースの範囲が広がっています。この変更は、ユーザーがさまざまなAzureサービスと連携する際の設定方法をより包括的に理解できるように助けます。

さらに、文末には「Azure Functionsのインバウンドアクセス制限を管理する」ためのリンクが追加され、関連情報へのアクセシビリティが向上しています。このように、本更新はユーザーの利便性を高めることを目的としています。

## articles/search/search-indexer-sensitivity-labels.md{#item-2a7bfc}

<details>
<summary>Diff</summary>
````diff
@@ -65,8 +65,6 @@ This functionality is available for the following data sources:
 
   + [Custom Web API skill](cognitive-search-custom-skill-web-api.md)
 
-  + [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md)
-
   + [Knowledge store](knowledge-store-concept-intro.md)
 
   + [Indexer enrichment cache](enrichment-cache-how-to-configure.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "感度ラベルに関する文書の更新"
}
```

### Explanation
この変更は、感度ラベルに関するAzure AI Searchインデクサの設定に関する文書に対するマイナーな更新です。具体的には、2件の削除が行われ、合計で2件の変更が加えられています。

主な変更点は、データソースのリストから「GenAI Prompt skill」が削除されたことです。この削除は、ドキュメントの情報を最新の状況に合わせるためのものであり、特定の機能が現在サポートされていないか、使用されなくなったことを示唆しています。

他のデータソースの情報は変更されていないため、読者は引き続き既存のサポートデータソースについての情報を確認できます。この更新は、インデクサの利用者が最新の機能セットについて理解するのに役立ちます。

## articles/search/search-indexer-sharepoint-access-control-lists.md{#item-532a24}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to configure Azure AI Search indexers for ingesting Acces
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/02/2026
+ms.date: 07/30/2026
 ai-usage: ai-assisted
 ---
 
@@ -42,6 +42,56 @@ This article explains how to ingest an access control list (ACL) alongside other
 
 + REST API version 2026-05-01-preview or an equivalent preview SDK package.
 
+## Limitations
+
++ Incremental ACL updates require the 2026-05-01-preview REST API or later. In earlier preview API versions, the system captures ACLs only on the first ingestion of each item. Later permission changes require explicit reindexing. For migration steps, see [Synchronize permissions between indexed and source content](#synchronize-permissions-between-indexed-and-source-content).
+
++ Parent-scope permission changes aren't picked up automatically on subsequent indexer runs. For the refresh options, see [Synchronize permissions between indexed and source content](#synchronize-permissions-between-indexed-and-source-content).
+
++ The Azure portal doesn't support this feature.
+
++ The following features aren't supported in this preview:
+
+  + [SharePoint Information Management policies](/sharepoint/intro-to-info-mgmt-policies) applicable to user access. The system doesn't evaluate, ingest, or honor these policies at query time.
+
+  + [Shareable links](/sharepoint/shareable-links-anyone-specific-people-organization) scoped to "Anyone" or "People in your organization." Only links scoped to "Specific people" are supported.
+
+  + [SharePoint groups](/sharepoint/modern-experience-sharing-permissions) (such as Owners, Members, and Visitors groups) are supported starting in the 2026-05-01-preview REST API. See [Configure SharePoint groups support](#configure-sharepoint-groups-support). In earlier preview API versions, only SharePoint groups that resolve to Microsoft Entra groups are supported.
+
++ The following indexer features don't support permission inheritance in indexed documents originating from SharePoint. If you use any of these features in a skillset or indexer, document-level permissions aren't included in the indexed content.
+
+  + [Custom Web API skill](cognitive-search-custom-skill-web-api.md)
+
+  + [Knowledge store](knowledge-store-concept-intro.md)
+
+  + [Indexer enrichment cache](enrichment-cache-how-to-configure.md)
+
+  + [Debug sessions](cognitive-search-debug-session.md)
+
+
+## Support for the SharePoint permission model
+
+This preview supports basic ACLs for documents, list items, and modern ASPX site pages.
+
+| SharePoint Feature | Description | Supported | Notes |
+|--------------------|-------------|-----------|-------|
+| Site, library, list, and page inheritance | Site → library/list → folder → file/item/page. | ✔️ | Evaluated at ingestion; effective ACLs computed per item. |
+| Folder, file, list item, and page unique ACLs | Item-level access. | ✔️ | Included when present at first ingestion and on subsequent runs that detect ACL changes for items with unique permissions. |
+| SharePoint list items | Permissions on list items (`allSiteLists` and `allSiteContent` containers). | ✔️ | Preview, starting in the 2026-05-01-preview REST API. |
+| ASPX site pages | Permissions on modern site pages (`allSitePages` and `allSiteContent` containers). | ✔️ | Preview, starting in the 2026-05-01-preview REST API. |
+| Microsoft Entra (Microsoft 365 and security) groups | Group-based access. | ✔️ | Group IDs included when resolvable to a Microsoft Entra identifier (ID). |
+| SharePoint site groups | Owners/Members/Visitors and custom site groups. | ✔️ | Preview, starting in the 2026-05-01-preview REST API. Requires the [SharePoint groups configuration](#configure-sharepoint-groups-support). Group IDs are emitted with the `spg:` prefix. |
+| Shareable "Anyone links" or "People in your organization links" | Org-wide or public access. | ❌ | Not supported in preview. |
+| External/guest users | Access for guests. | ❌ | Not supported. |
+| Information Management policies | Policies to define specific permissions requirements. | ❌ | Not supported in preview. |
+| Purview sensitivity labels  | Document-level security for privacy, categorization, permissions, and encryption  | ❌ | Supported via a separate feature: [preserving and honoring sensitivity labels](search-indexer-sensitivity-labels.md). |
+
+## How hierarchical permissions are evaluated
+
+SharePoint permissions inherit the hierarchy of Site → Library → Folder → File, unless inheritance is broken.
+
+During ingestion, the indexer gathers user and group identifiers (ID) at each level and computes the effective ACL for each file.
+
 ## Permissions by ACL scenario
 
 The Microsoft Entra application permissions and credential type required for ACL ingestion depend on which item types and group types you index. In the app registration, all permissions are added under **API permissions** > **Add a permission**, and the federated credential is added under **Certificates & secrets** > **Federated credentials**. For step-by-step instructions and screenshots, see [Step 3: Create a Microsoft Entra application registration](search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration) and [Configuring the registered application with a managed identity](search-how-to-index-sharepoint-online.md#configuring-the-registered-application-with-a-managed-identity).
@@ -78,57 +128,37 @@ Complete these steps on your registered Microsoft Entra application:
    - For any scenario that includes SharePoint permissions, add a federated credential under **Certificates & secrets** > **Federated credentials**. See [Configuring the registered application with a managed identity](search-how-to-index-sharepoint-online.md#configuring-the-registered-application-with-a-managed-identity).
 1. Grant the application access to the target SharePoint sites (especially important when you use `Sites.Selected` for scoped access) so it can read the content and permissions you want to index.
 
-## Limitations
-
-+ Incremental ACL updates require the 2026-05-01-preview REST API or later. In earlier preview API versions, ACLs are captured only on the first ingestion of each item, and later permission changes require explicit reindexing. For migration steps, see [Synchronize permissions between indexed and source content](#synchronize-permissions-between-indexed-and-source-content).
-  
-+ Parent-scope permission changes aren't picked up automatically on subsequent indexer runs. For the refresh options, see [Synchronize permissions between indexed and source content](#synchronize-permissions-between-indexed-and-source-content).
-
-+ The Azure portal doesn't support this feature.
-
-+ The following aren't supported in this preview:
-
-  + [SharePoint Information Management policies](/sharepoint/intro-to-info-mgmt-policies) applicable to user access. These policies aren't evaluated, ingested, or honored at query time.
-
-  + [Shareable links](/sharepoint/shareable-links-anyone-specific-people-organization) scoped to "Anyone" or "People in your organization." Only links scoped to "Specific people" are supported.
-
-  + [SharePoint groups](/sharepoint/modern-experience-sharing-permissions) (such as Owners, Members, and Visitors groups) are supported starting in the 2026-05-01-preview REST API. See [Configure SharePoint groups support](#configure-sharepoint-groups-support). In earlier preview API versions, only SharePoint groups that resolve to Microsoft Entra groups are supported.
- 
-+ The following indexer features don't support permission inheritance in indexed documents originating from SharePoint. If you use any of these features in a skillset or indexer, document-level permissions aren't included in the indexed content.
-
-  + [Custom Web API skill](cognitive-search-custom-skill-web-api.md)
-
-  + [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md)
-
-  + [Knowledge store](knowledge-store-concept-intro.md)
+## Find the correct Microsoft Entra identifiers
 
-  + [Indexer enrichment cache](enrichment-cache-how-to-configure.md)
+Each identifier appears in a different location in the Azure portal and maps to a specific configuration field. Use this section as a reference when configuring SharePoint ACL ingestion with a federated credential. These identifiers are referenced in [Configure SharePoint groups support](#configure-sharepoint-groups-support) and in the data source connection string.
 
-  + [Debug sessions](cognitive-search-debug-session.md)
+| Identifier | Portal location | Used where | Notes |
+|---|---|---|---|
+| Application (client) ID | **App registrations** > `<your-app>` > **Overview** | `ApplicationId` in the data source connection string; `applicationId` in `sharePointConnectorAppRegistration` | This is the correct ID for most configuration fields. Also called "client ID." |
+| Application object ID | **App registrations** > `<your-app>` > **Overview** (below Application (client) ID) | Not used in Azure AI Search configuration | Don't confuse this with the Application (client) ID. It appears in the same blade, directly below the client ID. |
+| Service principal object ID | **Microsoft Entra ID** > **Enterprise applications** > `<your-app>` > **Manage** > **Properties** | Not used in Azure AI Search configuration | This is the service principal representation of the app. It's a different GUID from the app registration object ID. |
+| Managed identity principal ID | Managed identity resource > **Properties** or the search service **Identity** blade | Not used directly in Azure AI Search data source or index configuration | Used internally when you set up the federated identity credential on the app registration. The credential you create trusts this identity. |
+| Federated credential object ID | **App registrations** > `<your-app>` > **Manage** > **Certificates & secrets** > **Federated credentials** > `<credential-name>` | `federatedCredentialId` in `sharePointConnectorAppRegistration` | The GUID of the federated identity credential entry itself, not the managed identity's GUID. |
+| Federated credential application ID | System-assigned: **Microsoft Entra ID** > **Enterprise applications** > `<search-service>` > **Properties**; User-assigned: `<managed-identity-resource>` > **Properties** | `FederatedCredentialApplicationId` in the data source connection string | See [Federated credential application ID](#federated-credential-application-id) for the system-assigned identity lookup. |
 
+### Federated credential application ID
 
-## Support for the SharePoint permission model
-
-This preview supports basic ACLs for documents, list items, and modern ASPX site pages.
+For `FederatedCredentialApplicationId` in the data source connection string, use the managed identity's own application (client) ID, not the ingestion app's ID.
 
-| SharePoint Feature | Description | Supported | Notes |
-|--------------------|-------------|-----------|-------|
-| Site, library, list, and page inheritance | Site → library/list → folder → file/item/page. | ✔️ | Evaluated at ingestion; effective ACLs computed per item. |
-| Folder, file, list item, and page unique ACLs | Item-level access. | ✔️ | Included when present at first ingestion and on subsequent runs that detect ACL changes for items with unique permissions. |
-| SharePoint list items | Permissions on list items (`allSiteLists` and `allSiteContent` containers). | ✔️ | Preview, starting in the 2026-05-01-preview REST API. |
-| ASPX site pages | Permissions on modern site pages (`allSitePages` and `allSiteContent` containers). | ✔️ | Preview, starting in the 2026-05-01-preview REST API. |
-| Microsoft Entra (Microsoft 365 and security) groups | Group-based access. | ✔️ | Group IDs included when resolvable to a Microsoft Entra identifier (ID). |
-| SharePoint site groups | Owners/Members/Visitors and custom site groups. | ✔️ | Preview, starting in the 2026-05-01-preview REST API. Requires the [SharePoint groups configuration](#configure-sharepoint-groups-support). Group IDs are emitted with the `spg:` prefix. |
-| Shareable "Anyone links" or "People in your organization links" | Org-wide or public access. | ❌ | Not supported in preview. |
-| External/guest users | Access for guests. | ❌ | Not supported. | 
-| Information Management policies | Policies to define specific permissions requirements. | ❌ | Not supported in preview. | 
-| Purview sensitivity labels  | Document-level security for privacy, categorization, permissions, and encryption  | ❌ | Supported via a separate feature: [preserving and honoring sensitivity labels](search-indexer-sensitivity-labels.md). | 
+**System-assigned managed identity:**
 
-## How hierarchical permissions are evaluated
+1. Go to your Azure AI Search service.
+1. Select **Security + networking** > **Identity**.
+1. On the **System assigned** tab, note the **Object (principal) ID**.
+1. Go to **Microsoft Entra ID** > **Manage** > **Enterprise applications**.
+1. Search for your search service name or paste the **Object (principal) ID** into the search box.
+1. Select the result and open **Properties**. Copy the **Application ID** shown here, which is the value for `FederatedCredentialApplicationId`.
 
-SharePoint permissions inherit the hierarchy of Site → Library → Folder → File, unless inheritance is broken.
+**User-assigned managed identity:**
 
-During ingestion, the indexer gathers user and group identifiers (ID) at each level and computes the effective ACL for each file.
+1. Go to the user-assigned managed identity resource.
+1. Select **Settings** > **Properties**.
+1. Copy the **Client ID**, which is the value for `FederatedCredentialApplicationId`.
 
 ## Configure your search service for ACL ingestion and query-time enforcement
 
@@ -140,8 +170,8 @@ Where you map the ACL metadata fields depends on whether the indexer writes one
 
 | Scenario | Populate ACL fields via | Why |
 |---|---|---|
-| No skillset or skillset without chunking; one search document per source item | **Indexer field mappings** only (`metadata_user_ids` → `UserIds`, `metadata_group_ids` → `GroupIds`, and for SharePoint groups `metadata_sharepoint_site_url` → `SharePointSiteUrl`). | The indexer writes a single document to the target index, and field mappings carry source metadata to index fields. |
-| Skillset with chunking (for example, Text Split skill for integrated vectorization), single index with parent fields repeated on each chunk (`projectionMode: skipIndexingParentDocuments`) | **Index projections** in the skillset (`mappings` from `/document/metadata_user_ids`, `/document/metadata_group_ids`, and for SharePoint groups `/document/metadata_sharepoint_site_url`). | The parent document isn't indexed; only chunks are. ACL values must be projected onto every chunk so query-time filters apply on the chunk returned in results. Indexer field mappings for these fields are bypassed in this mode. |
+| No skillset or skillset without chunking; one search document per source item | **Indexer field mappings** only (`metadata_user_ids` → `UserIds`, `metadata_group_ids` → `GroupIds`, and for SharePoint groups `metadata_spo_site_url` → `SharePointSiteUrl`). | The indexer writes a single document to the target index, and field mappings carry source metadata to index fields. |
+| Skillset with chunking (for example, Text Split skill for integrated vectorization), single index with parent fields repeated on each chunk (`projectionMode: skipIndexingParentDocuments`) | **Index projections** in the skillset (`mappings` from `/document/metadata_user_ids`, `/document/metadata_group_ids`, and for SharePoint groups `/document/metadata_spo_site_url`). | The parent document isn't indexed; only chunks are. ACL values must be projected onto every chunk so query-time filters apply on the chunk returned in results. Indexer field mappings for these fields are bypassed in this mode. |
 | Skillset with chunking, two-index pattern (parent index + child chunk index) | **Both**: indexer field mappings populate ACL fields on the parent index, index projections populate ACL fields on the child chunk index. | Both indexes are queryable, and each needs the metadata it filters on. |
 
 In all chunked scenarios, every chunk must carry the ACL fields. Permission filters apply per document, so a chunk missing ACL fields can't be returned to the right caller.
@@ -212,7 +242,7 @@ PUT https://{service}.search.windows.net/skillsets/{skillset}?api-version=2026-0
           { "name": "parentId",          "source": "/document/id" },              // parent doc id
           { "name": "UserIds",  "source": "/document/metadata_user_ids" },
           { "name": "GroupIds",  "source": "/document/metadata_group_ids" },
-          { "name": "SharePointSiteUrl", "source": "/document/metadata_sharepoint_site_url" } // include when the index has sharePointConnectorAppRegistration (SharePoint groups support)
+          { "name": "SharePointSiteUrl", "source": "/document/metadata_spo_site_url" } // include when the index has sharePointConnectorAppRegistration (SharePoint groups support)
         ]
       }
     ],
@@ -271,7 +301,7 @@ The following components work together to enable SharePoint site group resolutio
 | Component | Where | Purpose |
 |---|---|---|
 | `sharePointConnectorAppRegistration` (with `applicationId`, `tenantId`, `federatedCredentialId`) | Index definition | Provides the authentication configuration required for the search service to call the SharePoint REST API as the calling user and resolve site group membership at query time. |
-| `SharePointSiteUrl` field (with `sharepointSiteUrl: true`) | Index schema + indexer field mapping from `metadata_sharepoint_site_url` | Identifies which SharePoint site a document belongs to, so SP group resolution is scoped correctly. |
+| `SharePointSiteUrl` field (with `sharepointSiteUrl: true`) | Index schema + indexer field mapping from `metadata_spo_site_url` | Identifies which SharePoint site a document belongs to, so SP group resolution is scoped correctly. |
 | `spg:`-prefixed values in `GroupIds` | Document permission metadata | Distinguish SharePoint site group IDs from Microsoft Entra group object IDs. |
 
 
@@ -281,6 +311,9 @@ The following components work together to enable SharePoint site group resolutio
 + Microsoft Entra app registration with a federated identity credential. See [Configuring the registered application with a managed identity](search-how-to-index-sharepoint-online.md#configuring-the-registered-application-with-a-managed-identity).
 + REST API `2026-05-01-preview` or later.
 
+> [!NOTE]
+> `FederatedCredentialApplicationId` in the data source connection string differs from `applicationId` in `sharePointConnectorAppRegistration`, which is the ingestion app's client ID. To find the correct values, see [Find the correct Microsoft Entra identifiers](#find-the-correct-microsoft-entra-identifiers).
+
 ### 2. Configure the index
 
 Add the `sharePointConnectorAppRegistration` configuration and the `SharePointSiteUrl` field alongside the `UserIds` and `GroupIds` permission-filter fields, so the full index shape is in one place. Keep `permissionFilterOption: "enabled"`.
@@ -314,7 +347,7 @@ Map the SharePoint metadata fields to the index fields in a single combined mapp
   "fieldMappings": [
     { "sourceFieldName": "metadata_user_ids",             "targetFieldName": "UserIds" },
     { "sourceFieldName": "metadata_group_ids",            "targetFieldName": "GroupIds" },
-    { "sourceFieldName": "metadata_sharepoint_site_url",  "targetFieldName": "SharePointSiteUrl" }
+    { "sourceFieldName": "metadata_spo_site_url",  "targetFieldName": "SharePointSiteUrl" }
   ]
 }
 ```
@@ -379,10 +412,12 @@ After indexing your data and ACLs, you can [query the index](search-query-access
 | Symptom | Cause and resolution |
 |---|---|
 | `UserIds` or `GroupIds` are empty in indexed documents | If your skillset uses `projectionMode: skipIndexingParentDocuments`, indexer field mappings for ACL fields are bypassed. Set ACL fields via [`indexProjections.mappings`](#3-configure-index-projections-in-your-skillset-if-applicable) on every chunk instead. |
-| SharePoint site group IDs are missing, or `GroupIds` values don't have the `spg:` prefix | Confirm the index has the [`sharePointConnectorAppRegistration`](#2-configure-the-index) configuration, the `SharePointSiteUrl` field exists with `sharepointSiteUrl: true`, and the `metadata_sharepoint_site_url` mapping is present in either indexer field mappings or index projections. |
+| SharePoint site group IDs are missing, or `GroupIds` values don't have the `spg:` prefix | Confirm the index has the [`sharePointConnectorAppRegistration`](#2-configure-the-index) configuration, the `SharePointSiteUrl` field exists with `sharepointSiteUrl: true`, and the `metadata_spo_site_url` mapping is present in either indexer field mappings or index projections. |
+| `SharePointSiteUrl` is empty or null after indexing even though ACLs are otherwise populating correctly | The indexer emits this metadata under `metadata_spo_site_url`, not `metadata_sharepoint_site_url`. Verify that your indexer field mapping uses `"sourceFieldName": "metadata_spo_site_url"`. If your skillset uses index projections for chunked documents, verify that the projection mapping source is `/document/metadata_spo_site_url`. |
 | The indexer returns 401 or 403 | Grant admin consent on both Microsoft Graph and SharePoint API permissions for your scenario. Use a federated credential (not a client secret) when the scenario requires it. See [Permissions by ACL scenario](#permissions-by-acl-scenario). |
 | Permissions are stale after changing a site, library, list, or folder ACL | Call [`/resync` with `options: ["permissions"]`](#resync-acls-across-the-full-data-source). See [Synchronize permissions between indexed and source content](#synchronize-permissions-between-indexed-and-source-content) for context. |
 | `federatedCredentialId` is rejected when configuring `sharePointConnectorAppRegistration` | Use the ID (GUID) of the federated identity credential on the app registration, not the app object ID or the managed identity principal ID. |
+| The indexer returns `401 Unauthorized` and `FederatedCredentialApplicationId` is set | Verify you used the managed identity's Application ID (found in **Enterprise applications**), not the app registration's Application (client) ID or any Object ID. For a user-assigned managed identity, use the **Client ID** from the managed identity resource's **Properties** page. See [Find the correct Microsoft Entra identifiers](#find-the-correct-microsoft-entra-identifiers). |
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointアクセス制御リストに関する文書の更新"
}
```

### Explanation
この変更は、SharePointアクセス制御リストに関するAzure AI Searchインデクサの設定に関する文書に対するマイナーな更新です。具体的には、85件の新規追加と50件の削除があり、合計で135件の変更が加えられています。

主な変更点は、文書の日付が2026年6月2日から2026年7月30日に更新されたこと、そして新たに「制限」に関するセクションが追加されたことです。このセクションでは、ACL（アクセス制御リスト）に関する機能の制限や、特定のSharePoint機能が現在サポートされていないことが明確にされています。

また、新しい「SharePoint Permission Modelのサポート」が追加され、基本的なACLがドキュメントやリストアイテム、モダンASPXサイトページに対してどのようにサポートされるかが詳細に説明されています。この部分では、SharePointの階層構造や権限の評価方法についても言及されており、利用者にとって重要な情報となっています。

さらに、インデクサの使用に関する重要なガイドラインやサポートが追加されており、ユーザーが最新のAPIバージョンに適合させた設定を行うことができるようになっています。これにより、ユーザーは最新の機能や制限事項を理解し、効果的にアクセス制御を管理できるようになります。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.service: azure-ai-search
 ms.topic: limits-and-quotas
 ms.date: 06/02/2026
 ms.update-cycle: 180-days
+ai-usage: ai-assisted
 ms.custom:
   - references_regions
 #customer intent: As a developer making decisions about the infrastructure we use, planning to optimize for usage need, capacity, and cost, I want to understand the limits, quotas, and capacities associated with Azure AI Search services, detailing how these factors depend on the chosen pricing tier.
@@ -27,6 +28,23 @@ Azure AI Search supports two pricing models, each with associated service tiers.
 
 To learn more, see [Choose a pricing model and service tier](search-sku-tier.md).
 
+## Diagnose quota, capacity, or limit failures
+
+Quota and capacity failures come from separate controls. Use the error from the completed operation to find which one applies.
+
+If a create, scale, or upgrade operation is still running, wait for the provisioning state to become `Succeeded` or `Failed`. An operation in progress isn't evidence of a quota or capacity problem. If a scale operation fails, see [Errors during scaling](search-capacity-planning.md#errors-during-scaling).
+
+| Failure | Likely cause | First action |
+| --- | --- | --- |
+| Service creation blocked in a subscription and region | Subscription quota | In the **Quotas** service, check the limit for your tier and region, then [request more services](search-create-service-portal.md#add-more-services-to-your-subscription). |
+| Create, scale, or upgrade fails even though quota is available | Regional capacity constraint | Check the footnotes in [region support](search-region-support.md) for constrained tiers, then [choose another region](search-region-capacity.md#capacity-constraint-options). |
+| Replica, partition, tier, or object request rejected | Service or index limit | Compare your configuration and object counts with [service limits](#service-limits) and [index limits](#index-limits). |
+| The search service returns throttling responses under load | Throttling | Reduce the request rate or add search units. See [Throttling limits](#throttling-limits). |
+| Indexing fails near a storage or vector limit | Storage or vector quota | Compare `storageSize` with [partition storage](#partition-storage-gb) for disk and `vectorIndexSize` with [vector index size limits](#vector-index-size-limits) for memory. |
+| Indexer, skill, or vectorizer reports a 429 from another service | Azure OpenAI or other service quota | Follow the quota guidance for the service that issued the error, such as [Azure OpenAI](/azure/ai-services/openai/quotas-limits). |
+
+Available subscription quota doesn't guarantee regional capacity, and requesting more quota doesn't resolve a capacity constraint. If the failure persists, open an Azure support request that includes the subscription, region, tier, requested configuration, full error text, UTC time, and any correlation or operation ID.
+
 ## Subscription limits
 <!-- [!INCLUDE [azure-search-limits-per-subscription](~/reusable-content/ce-skilling/azure/includes/azure-search-limits-per-subscription.md)] -->
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchの制限とクォータの診断に関する情報追加"
}
```

### Explanation
この変更は、Azure AI Searchの制限およびクォータに関する文書に対するマイナーな更新です。具体的には、18件の新規追加が行われ、合計で18件の変更が加えられています。

主な変更点は、「クォータ、キャパシティ、または制限の失敗を診断する」セクションが新たに追加されたことです。このセクションでは、クォータやキャパシティの問題が発生した場合の診断方法や、エラーメッセージを使用して問題を特定する手順が詳しく説明されています。

具体的には、サービスの作成、スケーリング、アップグレードの失敗原因として考えられる事象と、それに対する初期のアクションが明示されており、ユーザーが問題を迅速に解決できる手助けをします。例として、「サービスの作成がブロックされた場合」「スケール操作が失敗した場合」などについて、必要な手順やリソースを示しています。

この更新により、開発者やインフラ担当者は、Azure AI Searchの利用における制限やクォータにより発生する可能性のある問題について、より深く理解することができます。

## articles/search/search-query-access-control-rbac-enforcement.md{#item-d24df7}

<details>
<summary>Diff</summary>
````diff
@@ -103,7 +103,7 @@ The security filter efficiently matches the userIds, groupIds, and rbacScope fro
 Starting in the 2026-05-01-preview REST API, Azure AI Search can honor SharePoint site group memberships, such as Owners, Members, Visitors, and custom site groups, at query time. To enable this scenario, the index must include:
 
 - A `sharePointConnectorAppRegistration` property that references the federated identity credential of the Microsoft Entra application used to call SharePoint on behalf of the user.
-- A field marked with the `sharepointSiteUrl: true` attribute that stores the SharePoint site URL for each indexed item (typically named `SharePointSiteUrl` and populated from the `metadata_sharepoint_site_url` source field).
+- A field marked with the `sharepointSiteUrl: true` attribute that stores the SharePoint site URL for each indexed item (typically named `SharePointSiteUrl` and populated from the `metadata_spo_site_url` source field).
 
 At query time, Azure AI Search uses the registered application and the site URL on each candidate document to resolve the SharePoint group memberships of the calling user on that site. The resolved groups are matched against the `spg:`-prefixed values stored in the `groupIds` permission filter field. The `spg:` prefix distinguishes SharePoint site groups from Microsoft Entra group object IDs, which are stored without a prefix.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointサイトURLに関するフィールド名の更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるRBAC（ロールベースアクセス制御）の実施に関する文書に対するマイナーな更新です。具体的には、1件の追加と1件の削除があり、合計で2件の変更があります。

主な変更点は、SharePointサイトのURLを格納するフィールドに関連するソースフィールド名が更新されたことです。具体的には、フィールドは、従来の`metadata_sharepoint_site_url`から新しい`metadata_spo_site_url`に変更されています。この変更により、Azure AI SearchがSharePointのグループメンバーシップを適切に解決し、クエリ時に正しい情報を提供できるようになります。

この変更は、Azure AI SearchがユーザーのSharePointサイトにおけるグループメンバーシップに基づいてアクセス制御を行う際には重要であり、ユーザーに対してより正確で動的な認可が可能になることを意味しています。これにより、特定のSharePointのサイトグループに対する整合性が確保されます。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -666,6 +666,8 @@ items:
       href: search-monitor-queries.md
     - name: Monitor indexer-based indexing
       href: search-monitor-indexers.md
+    - name: Monitoring data reference
+      href: monitor-azure-cognitive-search-data-reference.md
     - name: Troubleshoot storage metrics
       href: troubleshoot-storage-metrics.md
   - name: Visualize resource logs
@@ -740,8 +742,6 @@ items:
     - name: Azure Policy built-ins
       displayName: samples, policies, definitions
       href: ./policy-reference.md
-    - name: Monitoring data reference
-      href: monitor-azure-cognitive-search-data-reference.md
   - name: Data
     items:
     - name: Data types
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次にモニタリングデータ参照の追加と削除"
}
```

### Explanation
この変更は、Azure AI Searchに関する目次ファイル（toc.yml）のマイナーな更新です。合計で4件の変更が行われており、2件の追加と2件の削除が含まれています。

具体的には、目次に「モニタリングデータ参照」という項目が新たに追加され、関連するリンクである`monitor-azure-cognitive-search-data-reference.md`が提供されています。これにより、ユーザーはAzure Cognitive Searchのデータモニタリングに関する情報に簡単にアクセスできるようになります。

逆に、以前は存在していた「Monitoring data reference」の項目が、別のセクションから削除されています。これにより文書の構成が整理され、必要な情報へのアクセスが向上することが意図されています。

この更新は、利用者がリソースの監視手法やデータ参照に関する最新情報を得やすくすることを目指しています。


