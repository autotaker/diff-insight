---
date: '2026-06-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5af4e75...MicrosoftDocs:9057c21
summary: このコードの変更は、Azure AI Searchに関連する知識ソースの作成と使用に関する文書のマイナーアップデートおよび大幅な更新を中心に行われています。新たに知識ソースの生成オブジェクトレビューに関するガイドが追加され、各種知識ソースの統合方法について説明が強化されました。特にファイル知識ソースのドキュメントには大幅な変更が加えられ、アップロードと処理に関する制限やフォーマットが具体的に定義されています。全体として、Azure
  AI Searchユーザーへのサポートが強化され、情報の理解と実用性が向上することが期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5af4e75...MicrosoftDocs:9057c21){target="_blank"}

<format>
# ハイライト
このコードの変更は、Azure AI Searchに関連する複数の知識ソースの作成と使用に関する文書のマイナーアップデートおよび、大幅な更新を中心に行われています。また、生成オブジェクトのレビューに関する新しいガイドが追加されています。特にファイル知識ソースのドキュメントには、機能が大幅に更新されています。

## 新機能
- 知識ソースの生成オブジェクトレビューに関する新しいガイドの導入。
- 各種知識ソース（Azure SQL, Blob, Fabric Data Agent, Fabric Ontology など）がどのようにAzure AI Searchに統合されるかの説明が強化されました。

## 破壊的変更
- ファイル知識ソースのドキュメントに大幅な変更が加えられました。これは、ファイルのアップロードと処理に関する制限やフォーマットについて具体的に定義されています。

## その他の更新
- 各種知識ソースのドキュメントがより明確になり、特定の設定や使用手順が詳述されました。
- 知識ベースへの追加手順が整理され、簡素化されました。

# 洞察
コードの変更は、Azure AI Searchの様々な知識ソースとその統合方法に関する文書の改善に主眼を置いています。これにより、ユーザーがこれらのソースをより効果的に設定・使用できるようにすることを目的としています。

特に、ファイル知識ソースでは、アップロードの手順や制限事項が明確にされており、以前の制約から解放された新しい仕様が示されています。また、生成オブジェクトに関する新しいガイドの導入は、知識ソース作成後に自動生成されるオブジェクトをユーザーが確認するための手助けとなります。

この更新全体を通じて、Azure AI Searchユーザーに対するサポートが強化され、情報の理解と実用性が向上しています。これにより、ユーザーは異なる知識ソースを活用し、エージェント取得パイプラインに効率的に組み込むことが可能となります。これらの改善により、Azure AI Searchの利用体験が一層スムーズで効果的になることが期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-azure-sql.md](#item-89aa4d) | minor update | Azure SQL 知識ソースのアップデート | modified | 64 | 56 | 120 | 
| [agentic-knowledge-source-how-to-blob.md](#item-ac6c8a) | minor update | Blob 知識ソースの作成方法の更新 | modified | 20 | 23 | 43 | 
| [agentic-knowledge-source-how-to-fabric-data-agent.md](#item-900ecc) | minor update | Fabric Data Agent 知識ソースの説明更新 | modified | 7 | 5 | 12 | 
| [agentic-knowledge-source-how-to-fabric-ontology.md](#item-1f2bb6) | minor update | Fabric Ontology 知識ソースの説明更新 | modified | 8 | 6 | 14 | 
| [agentic-knowledge-source-how-to-file.md](#item-88f720) | breaking change | ファイル知識ソースのドキュメント大幅更新 | modified | 39 | 289 | 328 | 
| [agentic-knowledge-source-how-to-mcp-server.md](#item-9a2e92) | minor update | MCPサーバー知識ソースの文書修正 | modified | 8 | 6 | 14 | 
| [agentic-knowledge-source-how-to-onelake.md](#item-ec7a80) | minor update | OneLake知識ソースに関する文書更新 | modified | 18 | 24 | 42 | 
| [agentic-knowledge-source-how-to-search-index.md](#item-09d366) | minor update | 検索インデックス知識ソースの文書更新 | modified | 10 | 7 | 17 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed.md](#item-fe72fc) | minor update | SharePointインデックス知識ソースの文書更新 | modified | 18 | 24 | 42 | 
| [agentic-knowledge-source-how-to-sharepoint-remote.md](#item-79d019) | minor update | リモートSharePoint知識ソースの文書更新 | modified | 14 | 13 | 27 | 
| [agentic-knowledge-source-how-to-web.md](#item-6b21d0) | minor update | Web知識ソースの文書更新 | modified | 8 | 6 | 14 | 
| [agentic-knowledge-source-how-to-work-iq.md](#item-94718e) | minor update | Work IQ知識ソースの文書更新 | modified | 9 | 7 | 16 | 
| [get-started-portal-agentic-retrieval.md](#item-2bf1dc) | minor update | エージェント検索の開始ガイドの文書更新 | modified | 4 | 4 | 8 | 
| [knowledge-source-delete.md](#item-4a16f9) | minor update | 知識ソース削除ガイドの更新 | modified | 13 | 6 | 19 | 
| [knowledge-source-review-objects.md](#item-0babd3) | new feature | 知識ソースの生成オブジェクトレビューガイドの追加 | added | 19 | 0 | 19 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-azure-sql.md{#item-89aa4d}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ zone_pivot_groups: search-csharp-python-rest
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-Use an *indexed Azure SQL knowledge source* (preview) to ingest rows from Azure SQL Database or Azure SQL Managed Instance into an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+An *indexed Azure SQL knowledge source* (preview) ingests rows from Azure SQL Database or Azure SQL Managed Instance into an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
 Unlike file-based knowledge sources, such as Azure Blob Storage and OneLake, each SQL row is treated as one logical document. The index schema is customer driven through explicit column mappings rather than a fixed document schema.
 
@@ -41,7 +41,7 @@ The generated indexer conforms to the *Azure SQL indexer*, whose prerequisites,
 
 ## Prerequisites
 
-+ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md).
++ An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md).
 
 + Completion of the [Azure SQL indexer prerequisites](search-how-to-index-sql-database.md#prerequisites), including:
 
@@ -83,6 +83,28 @@ The generated indexer conforms to the *Azure SQL indexer*, whose prerequisites,
 + Real-time synchronization isn't supported. The generated indexer is schedule based.
 + Real-time SQL retrieval isn't supported. The knowledge source is indexed, not remote.
 
+## Prepare the generated indexer
+
+An indexed Azure SQL knowledge source automatically creates an indexer to drive ingestion. Review the following details before you create the knowledge source.
+
+### Change detection
+
+The generated indexer uses standard [Azure SQL indexer change detection](search-how-to-index-sql-database.md#indexing-new-changed-and-deleted-rows):
+
++ **Tables:** The service applies [SQL integrated change tracking](search-how-to-index-sql-database.md#sql-integrated-change-tracking-policy) automatically. Enable [SQL change tracking](/sql/relational-databases/track-changes/about-change-tracking-sql-server) on the source table before you create the knowledge source.
+
++ **Views:** The service applies [high-water-mark change detection](search-how-to-index-sql-database.md#high-water-mark-change-detection-policy). Specify the column to use in `highWaterMarkColumn`. A `rowversion` column is strongly recommended. To detect deletions in a view, include a soft-delete marker column in the view as described in [Soft delete column deletion detection policy](search-how-to-index-sql-database.md#soft-delete-column-deletion-detection-policy).
+
+### Authentication
+
+The generated indexer supports two authentication options:
+
++ **SQL authentication:** Provide a username and password in the connection string.
+
++ **Managed identity authentication:** Use a system-assigned or user-assigned managed identity that has Azure RBAC and database-level roles on the SQL resource.
+
+For connection string formats, role requirements, and setup steps, see the [Azure SQL indexer prerequisites](search-how-to-index-sql-database.md#prerequisites) and [Connect through a managed identity](search-how-to-managed-identities.md).
+
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources](includes/how-tos/knowledge-source-check.md)]
@@ -126,9 +148,6 @@ The following JSON is an example response for an indexed Azure SQL knowledge sou
 }
 ```
 
-> [!NOTE]
-> The generated resources appear at the end of the response under `createdResources`.
-
 ## Create a knowledge source
 
 Run the following code to create an indexed Azure SQL knowledge source.
@@ -306,62 +325,62 @@ Content-Type: application/json
 
 The following properties apply to indexed Azure SQL knowledge sources.
 
-| Property | Description | Required |
-|--|--|--|
-| `name` | The name of the knowledge source. The name must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | Yes |
-| `kind` | The kind of knowledge source, which is `indexedSql` in this case. | Yes |
-| `description` | A description of the knowledge source. | No |
-| `encryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | No |
-| `indexedSqlParameters` | Parameters specific to indexed Azure SQL knowledge sources, which are described in the following section. | Yes |
+| Property | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the knowledge source. The name must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects in Azure AI Search. | String | Yes | Yes |
+| `kind` | The kind of knowledge source, which is `indexedSql` in this case. | String | No | Yes |
+| `description` | A description of the knowledge source. | String | Yes | No |
+| `encryptionKey` | A [customer-managed key](search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge source and the generated objects. | Object | Yes | No |
+| `indexedSqlParameters` | Parameters specific to indexed Azure SQL knowledge sources, which are described in the following section. | Object | | Yes |
 
 ### `indexedSqlParameters` properties
 
 The following properties are specific to the `indexedSqlParameters` object of an indexed Azure SQL knowledge source.
 
-| Property | Description | Required |
-|--|--|--|
-| `connectionString` | A SQL authentication or managed-identity connection string for Azure SQL Database or Azure SQL Managed Instance. For supported credential formats, see the [Azure SQL indexer prerequisites](search-how-to-index-sql-database.md#prerequisites). | Yes |
-| `tableOrView` | The fully qualified name of the SQL table or view to ingest, specified in the `schema.objectName` format. A knowledge source ingests from exactly one table or one view. | Yes |
-| `highWaterMarkColumn` | Required when `tableOrView` refers to a view. The name of the column used for high-water-mark change detection. We strongly recommend a `rowversion` column. For more information, see [High water mark change detection policy](search-how-to-index-sql-database.md#high-water-mark-change-detection-policy). | Conditional |
-| `contentColumns` | An array of [column mappings](#column-mapping) that defines which SQL columns are treated as searchable text content in the generated index. Each mapping must use `Edm.String` as the `searchFieldType`. | No |
-| `embeddingColumns` | An array of [embedding mappings](#embedding-mapping) that defines which SQL columns are used to generate vector fields. | No |
-| `ingestionParameters` | A subset of the standard knowledge source [ingestion parameters](#ingestionparameters-properties). | No |
+| Property | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `connectionString` | A SQL authentication or managed-identity connection string for Azure SQL Database or Azure SQL Managed Instance. For supported credential formats, see the [Azure SQL indexer prerequisites](search-how-to-index-sql-database.md#prerequisites). | String | No | Yes |
+| `tableOrView` | The fully qualified name of the SQL table or view to ingest, specified in the `schema.objectName` format. A knowledge source ingests from exactly one table or one view. | String | No | Yes |
+| `highWaterMarkColumn` | Required when `tableOrView` refers to a view. The name of the column used for high-water-mark change detection. We strongly recommend a `rowversion` column. For more information, see [High water mark change detection policy](search-how-to-index-sql-database.md#high-water-mark-change-detection-policy). | String | No | Conditional |
+| `contentColumns` | An array of [column mappings](#column-mapping) that defines which SQL columns are treated as searchable text content in the generated index. Each mapping must use `Edm.String` as the `searchFieldType`. | Array | No | No |
+| `embeddingColumns` | An array of [embedding mappings](#embedding-mapping) that defines which SQL columns are used to generate vector fields. | Array | No | No |
+| `ingestionParameters` | A subset of the standard knowledge source [ingestion parameters](#ingestionparameters-properties). | Object | | No |
 
 ### Column mapping
 
 `contentColumns` uses the following column mapping shape.
 
-| Property | Description |
-|--|--|
-| `name` | The name of the field as it appears in the generated Azure AI Search index. |
-| `sourceField` | The SQL column whose value populates the target field. |
-| `searchFieldType` | The Azure AI Search field type for the generated field. For `contentColumns`, this must be `Edm.String`. |
+| Property | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the field as it appears in the generated Azure AI Search index. | String | No | Yes |
+| `sourceField` | The SQL column whose value populates the target field. | String | No | Yes |
+| `searchFieldType` | The Azure AI Search field type for the generated field. For `contentColumns`, this must be `Edm.String`. | String | No | Yes |
 
 ### Embedding mapping
 
 `embeddingColumns` uses the following embedding mapping shape.
 
-| Property | Description |
-|--|--|
-| `name` | The name of the target vector field that the service creates in the generated index. For example, it could be `descriptionVector`. |
-| `sourceField` | The SQL column whose text content is sent to the embedding model. |
+| Property | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `name` | The name of the target vector field that the service creates in the generated index. For example, it could be `descriptionVector`. | String | No | Yes |
+| `sourceField` | The SQL column whose text content is sent to the embedding model. | String | No | Yes |
 
 ### `ingestionParameters` properties
 
 For indexed Azure SQL knowledge sources, the existing `ingestionParameters` schema is unchanged, but only the following properties apply.
 
-| Property | Description |
-|--|--|
-| `contentExtractionMode` | Must be `"minimal"`. Other modes aren't supported because Azure SQL ingestion is row based and doesn't extract content from binary documents. |
-| `embeddingModel` | An Azure OpenAI embedding model used to vectorize the columns listed in `embeddingColumns`. Required only when `embeddingColumns` is specified. |
-| `identity` | An optional user-assigned managed identity used to authenticate to Azure SQL and Azure OpenAI. |
-| `ingestionSchedule` | An optional schedule that controls how often the generated indexer runs. |
+| Property | Description | Type | Editable | Required |
+|--|--|--|--|--|
+| `contentExtractionMode` | Must be `"minimal"`. Other modes aren't supported because Azure SQL ingestion is row based and doesn't extract content from binary documents. | String | No | No |
+| `embeddingModel` | An Azure OpenAI embedding model used to vectorize the columns listed in `embeddingColumns`. Required only when `embeddingColumns` is specified. | Object | Only `apiKey` and `deploymentId` are editable | Conditional |
+| `identity` | An optional user-assigned managed identity used to authenticate to Azure SQL and Azure OpenAI. | Object | Yes | No |
+| `ingestionSchedule` | An optional schedule that controls how often the generated indexer runs. | Object | Yes | No |
 
 Image extraction and image verbalization aren't supported for indexed Azure SQL knowledge sources, so `chatCompletionModel`, `assetStore`, `aiServices`, and image-related settings have no effect.
 
 ### Defaulting and validation rules
 
-The following defaults apply when you create an indexed Azure SQL knowledge source:
+The following defaults apply when you create an indexed Azure SQL knowledge source.
 
 + If you omit `contentColumns`, the service automatically maps SQL columns that can be safely represented as text to `Edm.String` fields in the generated index, using a 1:1 mapping where `name` equals `sourceField`.
 
@@ -371,40 +390,29 @@ The following defaults apply when you create an indexed Azure SQL knowledge sour
 
 + The primary key of the source table or view is auto-discovered. Explicit overrides aren't supported, and the source must have a single-valued primary key.
 
-## Configure the generated indexer
-
-An indexed Azure SQL knowledge source automatically creates an indexer to drive ingestion. The following sections cover change detection and authentication options for the generated indexer.
-
-### Change detection
-
-The generated indexer uses standard [Azure SQL indexer change detection](search-how-to-index-sql-database.md#indexing-new-changed-and-deleted-rows):
+## Check ingestion status
 
-+ **Tables:** The service applies [SQL integrated change tracking](search-how-to-index-sql-database.md#sql-integrated-change-tracking-policy) automatically. Enable [SQL change tracking](/sql/relational-databases/track-changes/about-change-tracking-sql-server) on the source table before you create the knowledge source.
+[!INCLUDE [Check ingestion status](includes/how-tos/knowledge-source-status.md)]
 
-+ **Views:** The service applies [high-water-mark change detection](search-how-to-index-sql-database.md#high-water-mark-change-detection-policy). Specify the column to use in `highWaterMarkColumn`. A `rowversion` column is strongly recommended. To detect deletions in a view, include a soft-delete marker column in the view as described in [Soft delete column deletion detection policy](search-how-to-index-sql-database.md#soft-delete-column-deletion-detection-policy).
+## Review the generated objects
 
-### Authentication
-
-The generated indexer supports two authentication options:
-
-+ **SQL authentication:** Provide a username and password in the connection string.
-
-+ **Managed identity authentication:** Use a system-assigned or user-assigned managed identity that has Azure RBAC and database-level roles on the SQL resource.
-
-For connection string formats, role requirements, and setup steps, see the [Azure SQL indexer prerequisites](search-how-to-index-sql-database.md#prerequisites) and [Connect through a managed identity](search-how-to-managed-identities.md).
+[!INCLUDE [Review the generated objects](includes/how-tos/knowledge-source-review-objects.md)]
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+If you're satisfied with the knowledge source, [add it to a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+
+## Query a knowledge base
 
-After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
 ## Delete a knowledge source
 
 [!INCLUDE [Delete a knowledge source](includes/how-tos/knowledge-source-delete.md)]
 
 ## Related content
 
++ [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
 + [What is a knowledge source?](agentic-knowledge-source-overview.md)
 + [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md)
 + [Query a knowledge base](agentic-retrieval-how-to-retrieve.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure SQL 知識ソースのアップデート"
}
```

### Explanation
本変更は、Azure SQLの知識ソースに関する文書の更新です。具体的には、インデックスされたAzure SQLの知識ソースの機能と要件に関する詳細が追加され、構成手順が明確になりました。また、いくつかの記述の表現が改善され、情報の一貫性が向上しています。

主な変更点は以下の通りです：
- Azure SQLの知識ソースがどのようにエージェントの取得パイプラインに統合されるかの説明が強化されました。
- 変更検出と認証オプションに関する情報が明確化されました。
- 知識ソースを生成する際の期待されるパラメータやプロパティに関する具体的なガイダンスが追加されています。

このドキュメントは、ユーザーがAzure SQLデータベースまたはAzure SQL Managed Instanceからデータをインデックスするための明確な指示を提供します。全体として、変更は機能の理解を深め、ユーザーの利便性を向上させることを目的としています。

## articles/search/agentic-knowledge-source-how-to-blob.md{#item-ac6c8a}

<details>
<summary>Diff</summary>
````diff
@@ -1,14 +1,14 @@
 ---
 title: Create a Blob Knowledge Source for Agentic Retrieval
-description: A blob knowledge source specifies a blob container that you want to read from. It also includes models and properties for creating an indexer, data source, skillset, and index used for agentic retrieval workloads.
+description: Learn how to create a blob knowledge source in Azure AI Search that ingests content from Azure Blob Storage or ADLS Gen2 for agentic retrieval.
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 06/02/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
 
-# Create a blob knowledge source from Azure Blob Storage and ADLS Gen2
+# Create a blob knowledge source from Azure Blob Storage or ADLS Gen2
 
 [!INCLUDE [GA feature](./includes/previews/agentic-retrieval-ga-feature.md)]
 
@@ -23,7 +23,7 @@ zone_pivot_groups: search-csharp-python-rest
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-Use a *blob knowledge source* to index and query Azure blob content in an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+A *blob knowledge source* ingests Azure Blob Storage or ADLS Gen2 content into an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
 When you create a blob knowledge source, you specify an external data source, models, and properties to automatically generate the following Azure AI Search objects:
 
@@ -43,7 +43,7 @@ When you create a blob knowledge source, you specify an external data source, mo
 
 ## Prerequisites
 
-+ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md).
++ An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md).
 
 + An [Azure Blob Storage](/azure/storage/common/storage-account-create) or [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/create-data-lake-storage-account) account.
 
@@ -492,7 +492,7 @@ Content-Type: application/json
 
 ### Source-specific properties
 
-For both the 2026-05-01-preview and 2026-04-01 API versions, you can pass the following properties to create a blob knowledge source.
+The following properties apply to blob knowledge sources.
 
 ::: zone pivot="csharp"
 
@@ -556,29 +556,25 @@ For both the 2026-05-01-preview and 2026-04-01 API versions, you can pass the fo
 
 [!INCLUDE [Check ingestion status](includes/how-tos/knowledge-source-status.md)]
 
-## Review the created objects
+## Review the generated objects
 
-When you create a blob knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
+[!INCLUDE [Review the generated objects](includes/how-tos/knowledge-source-review-objects.md)]
 
-After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
+## Assign to a knowledge base
 
-We recommend using the Azure portal to validate output creation. The workflow is:
+If you're satisfied with the knowledge source, [add it to a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
-1. Check the indexer for success or failure messages. Connection or quota errors appear here.
-1. Check the index for searchable content. Use Search Explorer to run queries.
-1. Check the skillset to learn how your content is chunked and optionally vectorized.
-1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
+## Query a knowledge base
 
-## Assign to a knowledge base
+After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query the knowledge source. This knowledge source supports optional configurations for document-level permissions enforcement and document-embedded image surfacing.
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+### Enforce document-level permissions
 
-After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time (preview)](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview).
 
-> [!TIP]
-> + To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview).
->
-> + To surface document-embedded images (such as diagrams or scans) in answer synthesis responses, configure `assetStore` on this knowledge source and enable image serving on the knowledge base. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
+### Surface document-embedded images
+
+To surface document-embedded images (such as diagrams or scans) in answer synthesis responses, configure `assetStore` on this knowledge source, and then enable image serving on the knowledge base. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
 
 ## Delete a knowledge source
 
@@ -587,6 +583,7 @@ After the knowledge base is configured, use the [retrieve action](agentic-retrie
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
-+ [Azure AI Search blob knowledge source Python sample](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/knowledge/blob-knowledge-source.ipynb)
-+ [Agentic RAG: Build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
-+ [Azure OpenAI demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
++ [What is a knowledge source?](agentic-knowledge-source-overview.md)
++ [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md)
++ [Query a knowledge base](agentic-retrieval-how-to-retrieve.md)
++ [Blob knowledge source Python sample](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/knowledge/blob-knowledge-source.ipynb)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blob 知識ソースの作成方法の更新"
}
```

### Explanation
この変更は、Blob知識ソースを作成するための手順に関する文書を更新したものです。具体的には、Azure AI SearchにおけるAzure Blob StorageまたはADLS Gen2から内容を取り入れるためのBlob知識ソースの作成方法を詳しく説明しています。

主な変更点は以下の通りです：
- 文書の説明が明確化され、Blob知識ソースがAzure AI Searchのエージェント取得パイプラインにどのように取り込まれるかが具体的に示されました。
- 依存関係のあるサービスについての記述が明確にされ、BlobストレージやADLS Gen2に関する指針が追加されました。
- 作成されたオブジェクトのレビュー方法や、ドキュメントレベルの権限の実施方法が明記され、実用的な情報が強化されました。

全体として、これによりユーザーがBlob知識ソースを利用する際の理解が向上し、エージェント取得機能の活用が促進されることを目的としています。 

## articles/search/agentic-knowledge-source-how-to-fabric-data-agent.md{#item-900ecc}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,9 @@ zone_pivot_groups: search-csharp-python-rest
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-A *Fabric Data Agent knowledge source* (preview) connects your [Microsoft Fabric Data Agent](/fabric/data-science/concept-data-agent) to an agentic retrieval pipeline in Azure AI Search. The data agent acts as a virtual analyst, generating and running queries against your live Microsoft Fabric data to return natural-language answers, tables, and charts as grounding data.
+A *Fabric Data Agent knowledge source* (preview) connects your [Microsoft Fabric Data Agent](/fabric/data-science/concept-data-agent) to an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
+
+The data agent acts as a virtual analyst, generating and running queries against your Microsoft Fabric data to return natural-language answers, tables, and charts. This makes Fabric Data Agent knowledge sources useful for high-churn data and analytical queries.
 
 Unlike indexed knowledge sources, Fabric Data Agent knowledge sources query live data directly at retrieval time. No ingestion pipeline is needed. Queries require an end-user access token, which the retrieval engine uses to query the Fabric Data Agent on behalf of the end user.
 
@@ -74,7 +76,7 @@ Fabric IQ inherits Microsoft Fabric's compliance certifications for the workspac
 
 ## Check for existing knowledge sources
 
-[!INCLUDE [](./includes/how-tos/knowledge-source-check.md)]
+[!INCLUDE [Check for existing knowledge sources](includes/how-tos/knowledge-source-check.md)]
 
 The following JSON is an example response for a Fabric Data Agent knowledge source.
 
@@ -190,14 +192,14 @@ The following properties apply to Fabric Data Agent knowledge sources.
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+If you're satisfied with the knowledge source, [add it to a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
 > [!IMPORTANT]
 > Fabric Data Agent knowledge sources don't support the `minimal` [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). Use `low` or `medium` instead.
 
 ## Query a knowledge base
 
-After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query Fabric Data Agent content. This knowledge source has unique query-time permissions enforcement and response characteristics.
+After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query Fabric Data Agent content. This knowledge source has unique query-time permissions enforcement and response characteristics.
 
 ### Enforce permissions at query time
 
@@ -267,7 +269,7 @@ The following example shows a retrieve response containing a Fabric Data Agent k
 
 ## Delete a knowledge source
 
-[!INCLUDE [](./includes/how-tos/knowledge-source-delete.md)]
+[!INCLUDE [Delete a knowledge source](includes/how-tos/knowledge-source-delete.md)]
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Fabric Data Agent 知識ソースの説明更新"
}
```

### Explanation
この変更は、Fabric Data Agentに関連する知識ソースの文書を更新したもので、Azure AI Searchとの接続方法や利用ケースについての説明が明確化されています。

主な変更点は以下の通りです：
- Fabric Data Agent知識ソースがAzure AI Searchのエージェント取得パイプラインに接続される方法に関する記述が強化され、知識ソースが独立して作成され、知識ベースに参照されることが説明されています。
- Fabric Data Agentが仮想アナリストとして機能し、Microsoft Fabricデータに対して生成・実行されるクエリが、自然言語の回答や表、チャートを返すことが強調されています。
- 利用者のアクセス権トークンを用いて、Fabric Data Agentに直接クエリを行う必要があることが説明されています。これにより、リアルタイムデータにアクセスする利点が示されています。

更新によって、ユーザーがFabric Data Agentを効果的に活用するための情報が提供され、エージェント取得機能の理解が促進されます。また、クエリの執行時に必要な設定や注意事項についても強調されています。

## articles/search/agentic-knowledge-source-how-to-fabric-ontology.md{#item-1f2bb6}

<details>
<summary>Diff</summary>
````diff
@@ -19,9 +19,11 @@ zone_pivot_groups: search-csharp-python-rest
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-A *Fabric Ontology knowledge source* (preview) connects your [Microsoft Fabric ontology](/fabric/iq/ontology/overview) to an agentic retrieval pipeline in Azure AI Search, providing ontology-defined entities, relationships, and content as grounding data. Because ontologies capture how your business defines its data, agents can answer in business terms rather than reasoning over raw tables and columns.
+A *Fabric Ontology knowledge source* (preview) connects your [Microsoft Fabric ontology](/fabric/iq/ontology/overview) to an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
-Unlike indexed knowledge sources, Fabric Ontology knowledge sources query live data directly. No ingestion pipeline is needed. Queries require an end-user access token, which the retrieval engine uses to authenticate with Microsoft Fabric on the caller's behalf.
+Ontologies capture how your business defines its data, entities, and relationships, allowing agents to answer in business terms rather than reasoning over raw tables and columns.
+
+Unlike indexed knowledge sources, Fabric Ontology knowledge sources query live data directly at retrieval time. No ingestion pipeline is needed. Queries require an end-user access token, which the retrieval engine uses to authenticate with Microsoft Fabric on the caller's behalf.
 
 ### Usage support
 
@@ -74,7 +76,7 @@ Fabric IQ inherits Microsoft Fabric's compliance certifications for the workspac
 
 ## Check for existing knowledge sources
 
-[!INCLUDE [](./includes/how-tos/knowledge-source-check.md)]
+[!INCLUDE [Check for existing knowledge sources](includes/how-tos/knowledge-source-check.md)]
 
 The following JSON is an example response for a Fabric Ontology knowledge source.
 
@@ -190,14 +192,14 @@ The following properties apply to Fabric Ontology knowledge sources.
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+If you're satisfied with the knowledge source, [add it to a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
 > [!NOTE]
 > Fabric Ontology knowledge sources don't support the `minimal` [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). Use `low` or `medium` instead.
 
 ## Query a knowledge base
 
-After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query Fabric Ontology content. This knowledge source has unique query-time permissions enforcement and response characteristics.
+After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query Fabric Ontology content. This knowledge source has unique query-time permissions enforcement and response characteristics.
 
 ### Enforce permissions at query time
 
@@ -261,7 +263,7 @@ The following example shows a retrieve response containing a Fabric Ontology kno
 
 ## Delete a knowledge source
 
-[!INCLUDE [](./includes/how-tos/knowledge-source-delete.md)]
+[!INCLUDE [Delete a knowledge source](includes/how-tos/knowledge-source-delete.md)]
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Fabric Ontology 知識ソースの説明更新"
}
```

### Explanation
この変更は、Fabric Ontologyに関連する知識ソースの文書を更新し、Azure AI Searchとの接続やその機能に関する説明を明確にしています。

主な変更点は以下の通りです：
- Fabric Ontology知識ソースがAzure AI Searchのエージェント取得パイプラインに接続されることに関する記述が強化され、知識ソースが独立して作成され、知識ベースに参照されることについての詳細が追加されました。
- オントロジーがビジネスデータの定義、エンティティ、関係性をどのように捉えるかが説明され、エージェントが生のテーブルやカラムを推論するのではなく、ビジネス用語で回答できる利点が強調されています。
- 知識ソースがライブデータを直接クエリできることおよび、エンドユーザーのアクセス権トークンが必要である旨の説明も更新されています。

これにより、ユーザーがFabric Ontologyを効果的に利用するための理解が深まり、エージェント取得機能の効果的な活用が促進されます。

## articles/search/agentic-knowledge-source-how-to-file.md{#item-88f720}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Create File Knowledge Source for Agentic Retrieval
+title: Create a File Knowledge Source for Agentic Retrieval
 description: Learn how to create a file knowledge source in Azure AI Search, upload files directly, and use the processed content in a knowledge base.
 ms.service: azure-ai-search
 ms.topic: how-to
@@ -19,9 +19,11 @@ zone_pivot_groups: search-csharp-python-rest
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-Use a *file knowledge source* (preview) to upload small and medium file sets directly to Azure AI Search for agentic retrieval. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+A *file knowledge source* (preview) uploads small and medium file sets directly to Azure AI Search for agentic retrieval. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
-A file knowledge source is useful when you want a managed upload experience instead of provisioning Azure Storage, configuring access, and creating an indexer pipeline over an external container. Azure AI Search processes uploaded files so their extracted content can be retrieved from a knowledge base. Use [blob knowledge sources](agentic-knowledge-source-how-to-blob.md) instead when your content already lives in Azure Blob Storage or ADLS Gen2, when you need large-scale ingestion, or when you depend on storage-account capabilities.
+File knowledge sources are useful when you want a managed upload experience instead of provisioning Azure Storage, configuring access, and creating an indexer pipeline over an external container. Azure AI Search processes uploaded files so their extracted content can be retrieved from a knowledge base.
+
+If your content already lives in Azure Blob Storage or ADLS Gen2, or if you need large-scale ingestion or storage account capabilities, use a [blob knowledge source](agentic-knowledge-source-how-to-blob.md) instead.
 
 ### Usage support
 
@@ -57,6 +59,27 @@ A file knowledge source is useful when you want a managed upload experience inst
 
 ::: zone-end
 
+## Supported formats and limits
+
+The following file types are supported.
+
+| Category | Extensions |
+|--|--|
+| Text | `.txt`, `.md`, `.html`, `.json`, `.csv` |
+| Code | `.c`, `.cs`, `.cpp`, `.java`, `.py`, `.js`, `.ts`, `.php`, `.rb`, `.sh` |
+| Documents | `.pdf`, `.docx`, `.pptx`, `.doc` |
+
+The following limits apply to file knowledge sources.
+
+| Limit | Value |
+|--|--|
+| Maximum file size per upload | 50 MB |
+| Maximum files per file knowledge source | 100 |
+
+> [!NOTE]
+> Uploaded content is stored in the generated search index. For total storage limits by pricing tier, see [Service limits](search-limits-quotas-capacity.md#service-limits).
+
+
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources](includes/how-tos/knowledge-source-check.md)]
@@ -208,13 +231,13 @@ Prefer: return=representation
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledgesources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
 
 ::: zone-end
 
 ### Source-specific properties
 
-You can pass the following properties to create a file knowledge source.
+The following properties apply to file knowledge sources.
 
 ::: zone pivot="csharp"
 
@@ -252,7 +275,7 @@ You can pass the following properties to create a file knowledge source.
 
 ### Ingestion parameters properties
 
-You can pass the following ingestion parameter properties to control how uploaded files are processed.
+The following ingestion parameter properties control how uploaded files are processed.
 
 ::: zone pivot="csharp"
 
@@ -283,9 +306,9 @@ You can pass the following ingestion parameter properties to control how uploade
 
 ## Upload files
 
-After the source exists, upload files directly to it. Each upload is a synchronous call: Azure AI Search extracts content from the uploaded file, chunks the content, creates embeddings when needed, and prepares the extracted content for retrieval before the call returns. You don't have to configure or run a separate ingestion pipeline.
+After the knowledge source exists, upload files directly to it. Each upload is a synchronous call: Azure AI Search extracts content from the uploaded file, chunks the content, creates embeddings when needed, and prepares the extracted content for retrieval before the call returns. You don't have to configure or run a separate ingestion pipeline.
 
-The request body contains the file content. The listed `fileName` is taken from the `Content-Disposition: attachment; filename="..."` header on the upload request; if the header isn't set, the service assigns an auto-generated `fileName`. SDKs can set the header through the upload method parameters shown in the following examples.
+The request body contains the file content. The listed `fileName` is taken from the `Content-Disposition: attachment; filename="..."` header on the upload request. If the header isn't set, the service assigns an auto-generated `fileName`. SDKs can set the header through the upload method parameters shown in the following examples.
 
 ::: zone pivot="csharp"
 
@@ -345,7 +368,9 @@ Content-Disposition: attachment; filename="installation-guide.pdf"
 ::: zone-end
 
 > [!NOTE]
-> Uploading a file doesn't replace an existing file even if you reuse the same `fileName`. Each upload creates a new file with its own `fileId`, and the list of uploaded files can contain multiple entries that share a `fileName`. To replace content, delete the prior file by `fileId` before or after the new upload.
+> Uploading a file doesn't replace an existing file, even if you reuse the same `fileName`. Each upload creates a new file with its own `fileId`, so the list of uploaded files can contain multiple entries that share a `fileName`.
+>
+> To replace content, delete the prior file by `fileId` before or after the new upload.
 
 ## List uploaded files
 
@@ -449,296 +474,21 @@ api-key: {{api-key}}
 
 ::: zone-end
 
-## Create a knowledge base
-
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
-
-::: zone pivot="csharp"
-
-```csharp
-using Azure;
-using Azure.Search.Documents.Indexes;
-using Azure.Search.Documents.Indexes.Models;
-using Azure.Search.Documents.KnowledgeBases.Models;
-
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
-
-var knowledgeBase = new KnowledgeBase(
-    name: "my-file-kb",
-    knowledgeSources: new[] { new KnowledgeSourceReference("my-file-ks") }
-)
-{
-    Description = "A knowledge base for uploaded product manuals.",
-    OutputMode = KnowledgeRetrievalOutputMode.ExtractiveData,
-    RetrievalReasoningEffort = new KnowledgeRetrievalMinimalReasoningEffort()
-};
-
-await indexClient.CreateOrUpdateKnowledgeBaseAsync(knowledgeBase);
-Console.WriteLine($"Knowledge base '{knowledgeBase.Name}' created or updated successfully.");
-```
-
-**Reference:** [KnowledgeBase](/dotnet/api/azure.search.documents.indexes.models.knowledgebase?view=azure-dotnet-preview&preserve-view=true)
-
-::: zone-end
-
-::: zone pivot="python"
-
-```python
-from azure.core.credentials import AzureKeyCredential
-from azure.search.documents.indexes import SearchIndexClient
-from azure.search.documents.indexes.models import (
-    KnowledgeBase,
-    KnowledgeRetrievalOutputMode,
-    KnowledgeSourceReference,
-)
-from azure.search.documents.knowledgebases.models import KnowledgeRetrievalMinimalReasoningEffort
-
-index_client = SearchIndexClient(endpoint="search_url", credential=AzureKeyCredential("api_key"))
-
-knowledge_base = KnowledgeBase(
-    name="my-file-kb",
-    description="A knowledge base for uploaded product manuals.",
-    knowledge_sources=[KnowledgeSourceReference(name="my-file-ks")],
-    output_mode=KnowledgeRetrievalOutputMode.EXTRACTIVE_DATA,
-    retrieval_reasoning_effort=KnowledgeRetrievalMinimalReasoningEffort(),
-)
-
-index_client.create_or_update_knowledge_base(knowledge_base=knowledge_base)
-print(f"Knowledge base '{knowledge_base.name}' created or updated successfully.")
-```
-
-**Reference:** [KnowledgeBase](/python/api/azure-search-documents/azure.search.documents.indexes.models.knowledgebase)
-
-::: zone-end
-
-::: zone pivot="rest"
+## Assign to a knowledge base
 
-```http
-PUT {{search-url}}/knowledgebases/my-file-kb?api-version=2026-05-01-preview
-api-key: {{api-key}}
-Content-Type: application/json
-Prefer: return=representation
-
-{
-  "name": "my-file-kb",
-  "description": "A knowledge base for uploaded product manuals.",
-  "outputMode": "extractiveData",
-  "retrievalReasoningEffort": {
-    "kind": "minimal"
-  },
-  "knowledgeSources": [
-    {
-      "name": "my-file-ks"
-    }
-  ]
-}
-```
-
-::: zone-end
+If you're satisfied with the knowledge source, [add it to a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
 ## Query a knowledge base
 
-After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
-
-The simplest retrieve call sends an intent and lets the knowledge base apply its configured defaults for each attached knowledge source.
-
-::: zone pivot="csharp"
-
-```csharp
-using Azure;
-using Azure.Search.Documents.KnowledgeBases;
-using Azure.Search.Documents.KnowledgeBases.Models;
-
-var kbClient = new KnowledgeBaseRetrievalClient(
-    new Uri(searchEndpoint),
-    "my-file-kb",
-    new AzureKeyCredential(apiKey));
-
-var request = new KnowledgeBaseRetrievalRequest
-{
-    IncludeActivity = true
-};
-request.Intents.Add(new KnowledgeRetrievalSemanticIntent(
-    "What does the installation guide say about network prerequisites?"));
-
-var result = await kbClient.RetrieveAsync(request);
-```
-
-**Reference:** [KnowledgeBaseRetrievalClient](/dotnet/api/azure.search.documents.knowledgebases.knowledgebaseretrievalclient?view=azure-dotnet-preview&preserve-view=true)
-
-::: zone-end
-
-::: zone pivot="python"
-
-```python
-from azure.core.credentials import AzureKeyCredential
-from azure.search.documents.knowledgebases import KnowledgeBaseRetrievalClient
-from azure.search.documents.knowledgebases.models import (
-    KnowledgeBaseRetrievalRequest,
-    KnowledgeRetrievalSemanticIntent,
-)
-
-kb_client = KnowledgeBaseRetrievalClient(
-    endpoint="search_url",
-    knowledge_base_name="my-file-kb",
-    credential=AzureKeyCredential("api_key"),
-)
-
-request = KnowledgeBaseRetrievalRequest(
-    intents=[
-        KnowledgeRetrievalSemanticIntent(
-            search="What does the installation guide say about network prerequisites?"
-        )
-    ],
-    include_activity=True,
-)
-
-result = kb_client.retrieve(request)
-```
-
-**Reference:** [KnowledgeBaseRetrievalClient](/python/api/azure-search-documents/azure.search.documents.knowledgebases.knowledgebaseretrievalclient)
-
-::: zone-end
-
-::: zone pivot="rest"
-
-```http
-POST {{search-url}}/knowledgebases/my-file-kb/retrieve?api-version=2026-05-01-preview
-api-key: {{api-key}}
-Content-Type: application/json
-Accept: application/json
-
-{
-  "includeActivity": true,
-  "intents": [
-    {
-      "type": "semantic",
-      "search": "What does the installation guide say about network prerequisites?"
-    }
-  ],
-  "knowledgeSourceParams": [
-    {
-      "kind": "file",
-      "knowledgeSourceName": "my-file-ks",
-      "includeReferences": true,
-      "includeReferenceSourceData": true
-    }
-  ]
-}
-```
-
-::: zone-end
-
-## Supported formats and limits
-
-The following file types are supported in this preview.
-
-| Category | Extensions |
-|--|--|
-| Text | `.txt`, `.md`, `.html`, `.json`, `.csv` |
-| Code | `.c`, `.cs`, `.cpp`, `.java`, `.py`, `.js`, `.ts`, `.php`, `.rb`, `.sh` |
-| Documents | `.pdf`, `.docx`, `.pptx`, `.doc` |
-
-The file knowledge source preview has the following limits.
-
-| Limit | Value |
-|--|--|
-| Maximum file size per upload | 50 MB |
-| Maximum files per file knowledge source | 100 |
-
-> [!NOTE]
-> Uploaded content is stored in the generated search index. For total storage limits by SKU, see [Service limits](search-limits-quotas-capacity.md#service-limits).
-
-File knowledge sources are designed for direct upload scenarios, not large-scale scheduled crawling. If you need recurring ingestion from durable external storage, use a [blob knowledge source](agentic-knowledge-source-how-to-blob.md) instead.
+After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
 ## Delete a knowledge source
 
-Before you can delete a knowledge source, you must delete any knowledge base that references it or update the knowledge base definition to remove the reference. If you try to delete a knowledge source that's in use, the action fails and returns a list of affected knowledge bases.
-
-::: zone pivot="csharp"
-
-```csharp
-using Azure;
-using Azure.Search.Documents.Indexes;
-
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
-
-// List knowledge bases on the service.
-await foreach (var kb in indexClient.GetKnowledgeBasesAsync())
-{
-    Console.WriteLine(kb.Name);
-}
-
-// Delete the knowledge base that references the file knowledge source.
-await indexClient.DeleteKnowledgeBaseAsync("my-file-kb");
-
-// Delete the file knowledge source.
-await indexClient.DeleteKnowledgeSourceAsync("my-file-ks");
-```
-
-::: zone-end
-
-::: zone pivot="python"
-
-```python
-from azure.core.credentials import AzureKeyCredential
-from azure.search.documents.indexes import SearchIndexClient
-
-index_client = SearchIndexClient(endpoint="search_url", credential=AzureKeyCredential("api_key"))
-
-# List knowledge bases on the service.
-for kb in index_client.list_knowledge_bases():
-    print(kb.name)
-
-# Delete the knowledge base that references the file knowledge source.
-index_client.delete_knowledge_base("my-file-kb")
-
-# Delete the file knowledge source.
-index_client.delete_knowledge_source("my-file-ks")
-```
-
-::: zone-end
-
-::: zone pivot="rest"
-
-To delete a knowledge source:
-
-1. Get a list of all knowledge bases on your search service.
-
-    ```http
-    ### Get knowledge bases
-    GET {{search-url}}/knowledgebases?api-version=2026-05-01-preview&$select=name
-    api-key: {{api-key}}
-    ```
-
-1. Get an individual knowledge base definition to check for knowledge source references.
-
-    ```http
-    ### Get a knowledge base definition
-    GET {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version=2026-05-01-preview
-    api-key: {{api-key}}
-    ```
-
-1. Either delete the knowledge base or update the knowledge base by removing the knowledge source if you have multiple sources. This example shows deletion.
-
-    ```http
-    ### Delete a knowledge base
-    DELETE {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version=2026-05-01-preview
-    api-key: {{api-key}}
-    ```
-
-1. Delete the knowledge source.
-
-    ```http
-    ### Delete a knowledge source
-    DELETE {{search-url}}/knowledgesources/{{knowledge-source-name}}?api-version=2026-05-01-preview
-    api-key: {{api-key}}
-    ```
-
-::: zone-end
+[!INCLUDE [Delete a knowledge source](includes/how-tos/knowledge-source-delete.md)]
 
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
 + [What is a knowledge source?](agentic-knowledge-source-overview.md)
 + [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md)
++ [Query a knowledge base](agentic-retrieval-how-to-retrieve.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ファイル知識ソースのドキュメント大幅更新"
}
```

### Explanation
この変更は、ファイル知識ソースに関連する文書を大幅に更新し、Azure AI Search内でのファイルのアップロードと処理に関する情報を整理・強化しています。主なポイントは以下の通りです：

- **タイトルの修正**: タイトルが「Create File Knowledge Source for Agentic Retrieval」から「Create a File Knowledge Source for Agentic Retrieval」へ変更され、文法的に正確になっています。
- **ファイル知識ソースの説明**: ファイル知識ソースは、Azure AI Searchに直接小規模および中規模のファイルセットをアップロードし、エージェントの取得に使用されることが明示されています。また、知識ソースが独立して作成され、知識ベースに参照されることの説明が強化されました。
- **サポートされるフォーマットと制限**: 新たにサポートされるファイルフォーマットと制限（最大ファイルサイズは50MB、ファイル知識ソースごとに100ファイルまで）についての詳細が追加されました。
- **削除に関する情報の整理**: 知識ソースを削除する前に、その参照がある知識ベースを削除する必要があることについての説明が整理されました。
- **使用サポートや注意点の追加**: アップロードされたコンテンツが生成された検索インデックスに保存されることや、従来のストレージを使用する場合の推奨事項が明示されています。

この変更により、ユーザーはファイル知識ソースの作成と使用方法をより明確に理解でき、効率的にその機能を利用することができるようになります。増えた情報と整理された説明により、ファイル知識ソースの管理と実装が容易になることを目的としています。

## articles/search/agentic-knowledge-source-how-to-mcp-server.md{#item-9a2e92}

<details>
<summary>Diff</summary>
````diff
@@ -21,9 +21,11 @@ zone_pivot_groups: search-csharp-python-rest
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-An *MCP Server knowledge source* (preview) connects your agentic retrieval pipeline to any external system that exposes a [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP)–compatible endpoint. Use this knowledge source to reach internal tools, third-party APIs, or custom backends that Azure AI Search doesn't natively support.
+An *MCP Server knowledge source* (preview) connects any system that exposes a [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP)–compatible endpoint to an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
-Unlike indexed knowledge sources, MCP Server knowledge sources query live data directly at retrieval time. No ingestion pipeline is needed. You provide the MCP server URL and specify which tools to allow, and Azure AI Search calls those tools on each query.
+MCP tools surface data and functionality from external systems as callable functions that agents invoke at query time. This makes MCP Server knowledge sources useful when the information you need lives in internal tools, third-party APIs, or custom backends that Azure AI Search doesn't natively support.
+
+Unlike indexed knowledge sources, MCP Server knowledge sources query live data directly at retrieval time. No ingestion pipeline is needed. You provide the MCP server URL and specify which tools Azure AI Search can call at query time.
 
 ### Usage support
 
@@ -67,7 +69,7 @@ Unlike indexed knowledge sources, MCP Server knowledge sources query live data d
 
 ## Check for existing knowledge sources
 
-[!INCLUDE [](./includes/how-tos/knowledge-source-check.md)]
+[!INCLUDE [Check for existing knowledge sources](includes/how-tos/knowledge-source-check.md)]
 
 The following JSON is an example response for an MCP Server knowledge source.
 
@@ -462,11 +464,11 @@ The `none` mode requires no configuration. The entire tool output is treated as
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+If you're satisfied with the knowledge source, [add it to a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
 ## Query a knowledge base
 
-After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query MCP server content. MCP Server knowledge sources have source-specific retrieval behavior and response fields.
+After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query MCP server content. MCP Server knowledge sources have source-specific retrieval behavior and response fields.
 
 ### How retrieval works for MCP Server knowledge sources
 
@@ -527,7 +529,7 @@ The following example shows a retrieve response containing an MCP Server knowled
 
 ## Delete a knowledge source
 
-[!INCLUDE [](./includes/how-tos/knowledge-source-delete.md)]
+[!INCLUDE [Delete a knowledge source](includes/how-tos/knowledge-source-delete.md)]
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MCPサーバー知識ソースの文書修正"
}
```

### Explanation
この変更は、MCPサーバー知識ソースに関する文書の内容を更新し、Azure AI Searchのエージェント取得パイプラインとの接続方法に関する情報を整理しています。

主な改訂点は以下の通りです：
- **文の強化**: MCPサーバー知識ソースがどのようにMCP互換のエンドポイントを使ってAzure AI Searchのエージェント取得パイプラインに接続されるかをより明確に説明しています。これにより、内部ツールやサードパーティのAPI、カスタムバックエンドといった、Azure AI Searchがネイティブでサポートしていないシステムにアクセスできることが強調されています。
- **ツールの説明の更新**: MCPツールが外部システムからデータや機能を呼び出す方法についての説明が追加され、エージェントがクエリ時にこれらのツールを利用できる利点を説明しています。
- **クエリ方法の修正**: 知識ソースが満足できるものであれば、知識ベースに「追加する」（was "specify the knowledge source in"）という表現に変更されました。また、MCPサーバーのコンテンツをクエリするためのアクションについての記述も明確化されています。

これにより、ユーザーはMCPサーバー知識ソースの利用方法を理解しやすくなり、Azure AI Searchの機能を効果的に活用できるようになります。文書の整合性と理解の促進が図られています。

## articles/search/agentic-knowledge-source-how-to-onelake.md{#item-ec7a80}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ zone_pivot_groups: search-csharp-python-rest
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-Use an *indexed OneLake knowledge source* to index and query Microsoft OneLake files in an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+An *indexed OneLake knowledge source* ingests Microsoft OneLake files into an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
 When you create an indexed OneLake knowledge source, you specify an external data source, models, and properties to automatically generate the following Azure AI Search objects:
 
@@ -44,7 +44,7 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 
 ## Prerequisites
 
-+ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md).
++ An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md).
 
 + Completion of the [OneLake indexer prerequisites](search-how-to-index-onelake-files.md#prerequisites).
 
@@ -139,9 +139,6 @@ The following JSON is an example response for an indexed OneLake knowledge sourc
 }
 ```
 
-> [!NOTE]
-> Sensitive information is redacted. The generated resources appear at the end of the response.
-
 ## Create a knowledge source
 
 Run the following code to create an indexed OneLake knowledge source.
@@ -477,7 +474,7 @@ Content-Type: application/json
 
 ### Source-specific properties
 
-For both the 2026-05-01-preview and 2026-04-01 API versions, you can pass the following properties to create an indexed OneLake knowledge source.
+The following properties apply to indexed OneLake knowledge sources.
 
 ::: zone pivot="csharp"
 
@@ -538,31 +535,27 @@ For both the 2026-05-01-preview and 2026-04-01 API versions, you can pass the fo
 
 [!INCLUDE [Check ingestion status](includes/how-tos/knowledge-source-status.md)]
 
-## Review the created objects
+## Review the generated objects
 
-When you create an indexed OneLake knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
+[!INCLUDE [Review the generated objects](includes/how-tos/knowledge-source-review-objects.md)]
+
+## Assign to a knowledge base
 
-After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
+If you're satisfied with the knowledge source, [add it to a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
-We recommend using the Azure portal to validate output creation. The workflow is:
+For any knowledge base that specifies an indexed OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
 
-1. Check the indexer for success or failure messages. Connection or quota errors appear here.
-1. Check the index for searchable content. Use Search Explorer to run queries.
-1. Check the skillset to learn how your content is chunked and optionally vectorized.
-1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
+## Query a knowledge base
 
-## Assign to a knowledge base
+After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query the knowledge source. This knowledge source supports optional configurations for document-level permissions enforcement and document-embedded image surfacing.
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+### Enforce document-level permissions
 
-For any knowledge base that specifies an indexed OneLake knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
+To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time (preview)](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview).
 
-After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+### Surface document-embedded images
 
-> [!TIP]
-> + To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview).
->
-> + To surface document-embedded images (such as diagrams or scans) in answer synthesis responses, configure `assetStore` on this knowledge source and enable image serving on the knowledge base. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
+To surface document-embedded images (such as diagrams or scans) in answer synthesis responses, configure `assetStore` on this knowledge source, and then enable image serving on the knowledge base. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
 
 ## Delete a knowledge source
 
@@ -571,5 +564,6 @@ After the knowledge base is configured, use the [retrieve action](agentic-retrie
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
-+ [Agentic RAG: Build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
-+ [Azure OpenAI demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
++ [What is a knowledge source?](agentic-knowledge-source-overview.md)
++ [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md)
++ [Query a knowledge base](agentic-retrieval-how-to-retrieve.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLake知識ソースに関する文書更新"
}
```

### Explanation
この変更では、OneLake知識ソースに関連する文書が更新され、Microsoft OneLakeファイルをエージェント取得パイプラインにインポートする方法が整理されています。以下の主なポイントが含まれています。

- **定義の強化**: 「*indexed OneLake knowledge source*」の定義が明確になり、Microsoft OneLakeファイルがAzure AI Searchのエージェント取得パイプラインにインポートされることが強調されています。
- **事前条件の明確化**: Azure AI Searchサービスが必須であることが明記され、OneLakeインデクサーの事前条件を完了する必要があることが追加されました。
- **生成されたオブジェクトについて**: 作成されるオブジェクト（インデクサー、インデックス、スキルセット、データソース）についての説明が更新され、これらを編集すべきではない理由が強調されています。
- **知識ベースへの追加**: 知識ソースが満足できるものであれば、次のステップとして知識ベースに追加するようにという表現が変更され、追加の手順が簡素化されています。
- **ドキュメントレベルの権限の強制**: ドキュメントレベルの権限を強制する方法についての具体的な手順が示され、知識ソースに関連する新しい構成オプションが導入されました。
- **ドキュメントに埋め込まれた画像のサーフィス**: 画像をレスポンスに表示する方法が追加され、特定の構成手順が明示されました。

これにより、ユーザーはOneLake知識ソースの設定と使用方法についてより明確に理解でき、Azure AI Searchを利用してファイルを効果的に処理できるようになります。変更が全体的にすっきり整理されており、理解しやすくなっています。

## articles/search/agentic-knowledge-source-how-to-search-index.md{#item-09d366}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ zone_pivot_groups: search-csharp-python-rest
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-A *search index knowledge source* specifies a connection to an Azure AI Search index that provides searchable content in an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+A *search index knowledge source* connects an existing Azure AI Search index, including its indexed text and vectors, to an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
 ### Usage support
 
@@ -31,7 +31,7 @@ A *search index knowledge source* specifies a connection to an Azure AI Search i
 
 ## Prerequisites
 
-+ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md).
++ An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md).
 
 + A search index containing plain text or vector content with a semantic configuration. [Review the index criteria for agentic retrieval](agentic-retrieval-how-to-create-index.md#criteria-for-agentic-retrieval). The index must be on the same search service as the knowledge base.
 
@@ -281,7 +281,7 @@ Content-Type: application/json
 
 ### Source-specific properties
 
-You can pass the following properties to create a search index knowledge source. Most properties are supported in both the 2026-05-01-preview and 2026-04-01 API versions; preview-only properties are marked in the description.
+The following properties apply to search index knowledge sources.
 
 ::: zone pivot="csharp"
 
@@ -458,9 +458,11 @@ Because the filters are combined with `AND`, `filterAddOn` can only narrow the p
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+If you're satisfied with the knowledge source, [add it to a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
-After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+## Query a knowledge base
+
+After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
 
 ## Delete a knowledge source
 
@@ -469,5 +471,6 @@ After the knowledge base is configured, use the [retrieve action](agentic-retrie
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
-+ [Agentic RAG: Build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
-+ [Azure OpenAI demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
++ [What is a knowledge source?](agentic-knowledge-source-overview.md)
++ [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md)
++ [Query a knowledge base](agentic-retrieval-how-to-retrieve.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックス知識ソースの文書更新"
}
```

### Explanation
この変更では、検索インデックス知識ソースに関する文書が更新され、Azure AI Searchのエージェント取得パイプラインとの接続方法がより明確に説明されています。

以下のポイントが主な変更内容です：
- **接続の明確化**: 「*search index knowledge source*」が、既存のAzure AI Searchインデックスと接続することを強調しており、インデックスされたテキストやベクトルをエージェント取得パイプラインに利用できることが追加されました。
- **事前条件の記述の変更**: Azure AI Searchサービスの記述が更新され、インデックスが知識ベースと同じ検索サービス上に存在する必要があることが強調されています。また、適切なセマンティック構成を持つインデックスが必要であることが示されています。
- **プロパティの明確化**: 検索インデックス知識ソースに適用されるプロパティの説明が更新され、これらが利用可能であることが記載されています。
- **知識ベースへの追加手順の簡素化**: 知識ソースが満足できる場合は、それを直接知識ベースに「追加する」という表現に改められ、手続きが明確になりました。
- **クエリの手順の更新**: 知識ベースの設定後に、どのようにクエリを行うかについての手順が「retrieve action」または「MCP endpoint」を呼び出す形で明確に記載されています。

これにより、ユーザーは検索インデックス知識ソースの設定や利用方法をより効果的に理解できるようになります。文書全体の理解が容易になり、Azure AI Searchを用いた情報検索がスムーズに行えるように設計されています。

## articles/search/agentic-knowledge-source-how-to-sharepoint-indexed.md{#item-fe72fc}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,7 @@ zone_pivot_groups: search-csharp-python-rest
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-Use an *indexed SharePoint knowledge source* (preview) to index and query SharePoint content in an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+An *indexed SharePoint knowledge source* (preview) ingests SharePoint content into an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
 When you create an indexed SharePoint knowledge source, you specify a SharePoint connection string, models, and properties to automatically generate the following Azure AI Search objects:
 
@@ -40,7 +40,7 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
 
 ## Prerequisites
 
-+ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md).
++ An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md).
 
 + Completion of the [SharePoint indexer prerequisites](search-how-to-index-sharepoint-online.md#prerequisites).
 
@@ -121,9 +121,6 @@ The following JSON is an example response for an indexed SharePoint knowledge so
 }
 ```
 
-> [!NOTE]
-> Sensitive information is redacted. The generated resources appear at the end of the response.
-
 ## Create a knowledge source
 
 Run the following code to create an indexed SharePoint knowledge source.
@@ -282,7 +279,7 @@ Content-Type: application/json
 
 ### Source-specific properties
 
-You can pass the following properties to create an indexed SharePoint knowledge source.
+The following properties apply to indexed SharePoint knowledge sources.
 
 ::: zone pivot="csharp"
 
@@ -335,31 +332,27 @@ You can pass the following properties to create an indexed SharePoint knowledge
 
 [!INCLUDE [Check ingestion status](includes/how-tos/knowledge-source-status.md)]
 
-## Review the created objects
+## Review the generated objects
 
-When you create an indexed SharePoint knowledge source, your search service also creates an indexer, index, skillset, and data source. We don't recommend that you edit these objects, as introducing an error or incompatibility can break the pipeline.
+[!INCLUDE [Review the generated objects](includes/how-tos/knowledge-source-review-objects.md)]
 
-After you create a knowledge source, the response lists the created objects. These objects are created according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names.
+## Assign to a knowledge base
 
-We recommend using the Azure portal to validate output creation. The workflow is:
+If you're satisfied with the knowledge source, [add it to a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
-1. Check the indexer for success or failure messages. Connection or quota errors appear here.
-1. Check the index for searchable content. Use Search Explorer to run queries.
-1. Check the skillset to learn how your content is chunked and optionally vectorized.
-1. Check the data source for connection details. Our example uses API keys for simplicity, but you can use Microsoft Entra ID for authentication and role-based access control for authorization.
+For any knowledge base that specifies an indexed SharePoint knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
 
-## Assign to a knowledge base
+## Query a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query the knowledge source. This knowledge source supports optional configurations for document-level permissions enforcement and document-embedded image surfacing.
 
-For any knowledge base that specifies an indexed SharePoint knowledge source, be sure to set `includeReferenceSourceData` to `true`. This step is necessary for pulling the source document URL into the citation.
+### Enforce document-level permissions
 
-After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time (preview)](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview).
 
-> [!TIP]
-> + To enforce document-level permissions, set `ingestionPermissionOptions` when you create this knowledge source, and then include the user's access token in the retrieve request. For more information, see [Enforce permissions at query time](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview).
->
-> + To surface document-embedded images (such as diagrams or scans) in answer synthesis responses, configure `assetStore` on this knowledge source and enable image serving on the knowledge base. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
+### Surface document-embedded images
+
+To surface document-embedded images (such as diagrams or scans) in answer synthesis responses, configure `assetStore` on this knowledge source, and then enable image serving on the knowledge base. For more information, see [Surface document-embedded images in agentic retrieval (preview)](agentic-retrieval-how-to-image-serving.md).
 
 ## Delete a knowledge source
 
@@ -368,5 +361,6 @@ After the knowledge base is configured, use the [retrieve action](agentic-retrie
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
-+ [Agentic RAG: Build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
-+ [Azure OpenAI demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
++ [What is a knowledge source?](agentic-knowledge-source-overview.md)
++ [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md)
++ [Query a knowledge base](agentic-retrieval-how-to-retrieve.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointインデックス知識ソースの文書更新"
}
```

### Explanation
この変更では、SharePointインデックス知識ソースに関する文書が更新され、Azure AI Searchにおけるエージェント取得パイプラインでの利用方法が強化されています。

以下のポイントが主な変更内容です：
- **接続の強調**: 更新された説明では、*indexed SharePoint knowledge source*がSharePointコンテンツをAzure AI Searchのエージェント取得パイプラインに取り込むことが強調され、具体的な用途が明確になっています。
- **事前条件の修正**: Azure AI Searchのサービスに関する記述が変更され、SharePointインデクサーの事前条件を完了する必要があることが追加されました。
- **プロパティの記述の明確化**: SharePointインデックス知識ソースに関連するプロパティの指定方法が明文化され、具体的な使用方法がより分かりやすくなっています。
- **生成されたオブジェクトに関する変更**: 知識ベースへの追加手順が「指定する」から「追加する」に変更され、より簡潔な表現に改善されています。
- **クエリ処理の手順の更新**: 知識ベースが設定された後のクエリ手順が更新され、取得アクションやMCPエンドポイントを呼び出す方法が明確にされています。
- **ドキュメントレベルの権限強制の追加**: ドキュメントレベルの権限を強制する方法が新たに追加され、具体的な手順が提供されています。また、ドキュメントに埋め込まれた画像の表現方法についての説明も強化されています。

これにより、ユーザーはSharePointインデックス知識ソースの設定および利用方法をより効果的に理解でき、全体的な文書のわかりやすさが向上しています。Azure AI Searchを使用した情報検索がよりスムーズに行えるように設計されています。

## articles/search/agentic-knowledge-source-how-to-sharepoint-remote.md{#item-79d019}

<details>
<summary>Diff</summary>
````diff
@@ -21,11 +21,11 @@ zone_pivot_groups: search-csharp-python-rest
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-A *remote SharePoint knowledge source* (preview) uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) (preview) to query textual content directly from SharePoint in Microsoft 365. No search index or connection string is needed. Only textual content is queried, and usage is billed through Microsoft 365 and a Copilot license.
+A *remote SharePoint knowledge source* (preview) uses the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) (preview) to query textual content directly from SharePoint in Microsoft 365. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
 To limit sites or constrain search, set a [filter expression](#filter-expression-examples) to scope by URLs, date ranges, file types, and other metadata. The caller's identity must be recognized by both the Azure tenant and the Microsoft 365 tenant because the retrieval engine queries SharePoint on behalf of the user.
 
-Like any other knowledge source, you specify a remote SharePoint knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) and use the results as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+Unlike indexed knowledge sources, remote SharePoint knowledge sources query live data directly at retrieval time. No search index or connection string is needed, and usage is billed through Microsoft 365 and a Copilot license.
 
 ### Usage support
 
@@ -35,7 +35,7 @@ Like any other knowledge source, you specify a remote SharePoint knowledge sourc
 
 ## Prerequisites
 
-+ Azure AI Search in any [region that provides agentic retrieval](search-region-support.md). 
++ An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md). 
 
 + SharePoint in a Microsoft 365 tenant that's under the same Microsoft Entra ID tenant as Azure.
 
@@ -61,25 +61,25 @@ Like any other knowledge source, you specify a remote SharePoint knowledge sourc
 
 ::: zone-end
 
-## Limitations
+## Limitations and considerations
 
-The following limitations in the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) apply to remote SharePoint knowledge sources.
+The following limitations and considerations in the [Copilot Retrieval API](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) apply to remote SharePoint knowledge sources.
 
 + There's no support for Copilot connectors or OneDrive content. Content is retrieved from SharePoint sites only.
 
 + Limit of 200 requests per user per hour.
 
 + Query character limit of 1,500 characters.
 
-+ Hybrid queries are only supported for the following file extensions: .doc, .docx, .pptx, .pdf, .aspx, and .one.
++ Hybrid queries are only supported for the following file extensions: `.doc`, `.docx`, `.pptx`, `.pdf`, `.aspx`, and `.one`.
 
 + Multimodal retrieval (nontextual content, including tables, images, and charts) isn't supported.
 
 + Maximum of 25 results from a query.
 
-+ Results are returned by Copilot Retrieval API as unordered.
++ Results are returned by the Copilot Retrieval API as unordered.
 
-+ Invalid Keyword Query Language (KQL) filter expressions are ignored and the query continues to execute without the filter.
++ Invalid Keyword Query Language (KQL) filter expressions are ignored, and the query continues to execute without the filter.
 
 ## Check for existing knowledge sources
 
@@ -193,7 +193,7 @@ Content-Type: application/json
 
 ### Source-specific properties
 
-You can pass the following properties to create a remote SharePoint knowledge source.
+The following properties apply to remote SharePoint knowledge sources.
 
 ::: zone pivot="csharp"
 
@@ -255,11 +255,11 @@ Learn more about [KQL filters](/microsoft-365-copilot/extensibility/api/ai-servi
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+If you're satisfied with the knowledge source, [add it to a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
 ## Query a knowledge base
 
-After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query SharePoint content. Remote SharePoint has source-specific behaviors for query-time filtering, query formulation, response fields, and permissions enforcement.
+After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query SharePoint content. Remote SharePoint has source-specific behaviors for query-time filtering, query formulation, response fields, and permissions enforcement.
 
 ### Apply a KQL filter at query time
 
@@ -427,5 +427,6 @@ For instructions on passing the token, see [Enforce permissions at query time](a
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
-+ [Agentic RAG: Build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
-+ [Azure OpenAI demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
++ [What is a knowledge source?](agentic-knowledge-source-overview.md)
++ [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md)
++ [Query a knowledge base](agentic-retrieval-how-to-retrieve.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リモートSharePoint知識ソースの文書更新"
}
```

### Explanation
この変更では、リモートSharePoint知識ソースに関する文書が更新され、Azure AI Searchにおけるクエリ方法が強化されています。

主な変更ポイントは以下の通りです：
- **内容の明確化**: リモートSharePoint知識ソースがMicrosoft 365内のSharePointから直接テキストコンテンツを取得するためのものであることが強調されています。また、インデックスや接続文字列が不要である点も明確にされています。
- **事前条件の修正**: Azure AI Searchサービスの記述が改善され、さらにSharePointが同じMicrosoft Entra IDテナントに存在する必要があることが明記されました。
- **制限事項の変更**: 制限箇所のタイトルが「制限」から「制限と考慮事項」に変更され、APIに関連する重要な情報が更新されています。具体的には、コンテンツがSharePointサイトからのみ取得可能であることや、リクエスト制限、クエリ文字数制限などが明示されています。
- **プロパティの説明の修正**: リモートSharePoint知識ソースに適用されるプロパティに関する記述が一貫して明確化されています。
- **知識ベースへの追加手順の簡素化**: 知識ソースが満足できる場合の追加手順が「指定する」から「追加する」という表現に変更され、理解しやすくなっています。
- **クエリ時の詳細**: 知識ベースが構成された後のクエリ手順が更新され、取得アクションやMCPエンドポイントを呼び出す方法が明確に記載されています。

これらの変更により、ユーザーはリモートSharePoint知識ソースの設定および使用に関してより効果的に理解できるように改善されています。Azure AI Searchを通じての情報取得がスムーズに行えるように設計されています。

## articles/search/agentic-knowledge-source-how-to-web.md{#item-6b21d0}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ ms.custom:
   - ignite-2025
 ms.topic: how-to
 ms.date: 06/02/2026
+ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
 
@@ -31,11 +32,11 @@ zone_pivot_groups: search-csharp-python-rest
 >
 > + Learn more about how Azure admins can [manage access to use of Web Knowledge Source](agentic-knowledge-source-how-to-web-manage.md).
 
-*Web Knowledge Source* enables retrieval of real-time web data from Microsoft Bing in an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](agentic-retrieval-how-to-retrieve.md) at query time.
+*Web Knowledge Source* enables retrieval of real-time web data from Microsoft Bing in an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
 Bing Custom Search is always the search provider for Web Knowledge Source. Although you can't specify alternative search providers or engines, you can include or exclude specific *domains*, such as https://learn.microsoft.com. When no domains are specified, Web Knowledge Source has unrestricted access to the entire public internet.
 
-Web Knowledge Source works best alongside other knowledge sources. Use Web Knowledge Source when your proprietary content doesn't provide complete, up-to-date answers or when you want to supplement results with information from a commercial search engine.
+Web Knowledge Source works best alongside other knowledge sources. Use it when your proprietary content doesn't provide complete, up-to-date answers or when you want to supplement results with information from a commercial search engine.
 
 ### Usage support
 
@@ -305,7 +306,7 @@ api-key: {{api-key}}
 
 ### Source-specific properties
 
-For the 2026-05-01-preview and 2026-04-01 API versions, you can pass the following properties to create a web knowledge source.
+The following properties apply to web knowledge sources.
 
 ::: zone pivot="csharp"
 
@@ -352,9 +353,7 @@ For the 2026-05-01-preview and 2026-04-01 API versions, you can pass the followi
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
-
-After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query the knowledge source.
+If you're satisfied with the knowledge source, [add it to a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
 ## Query a knowledge base
 
@@ -398,3 +397,6 @@ When you query a knowledge base that includes Web Knowledge Source, the retrieve
 
 + [Manage access to Web Knowledge Source in your Azure subscription](agentic-knowledge-source-how-to-web-manage.md)
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
++ [What is a knowledge source?](agentic-knowledge-source-overview.md)
++ [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md)
++ [Query a knowledge base](agentic-retrieval-how-to-retrieve.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Web知識ソースの文書更新"
}
```

### Explanation
この変更では、Web知識ソースに関する文書が更新され、Azure AI Searchにおける情報取得の方法が強化されています。

主な変更点は以下の通りです：
- **AI活用の追加**: 文書に「ai-usage: ai-assisted」というフィールドが追加され、AIの使用に関する情報が明確に示されています。
- **クエリ方法の明確化**: Web知識ソースが取得するデータが、Microsoft Bingからのリアルタイムウェブデータであることを強調し、クエリ時のデータ取得方法についての表現が更新されています。
- **継続的な補足の説明**: Web知識ソースが他の知識ソースと併用することで最も効果があることが強調され、使用の推奨理由が明確になっています。
- **プロパティの説明の簡素化**: Web知識ソースに適用されるプロパティに関する記述が明文化され、理解しやすくなっています。
- **知識ベースへの追加手順の修正**: 知識ソースに満足できた場合の追加手順が、「指定する」から「追加する」という表現に修正され、より明確に言及されています。
- **関連リソースの拡充**: 文書の最後に、Web知識ソースの管理やその他の関連リソースへのリンクが追加され、ユーザーが必要な情報にアクセスしやすくなっています。

これにより、ユーザーはWeb知識ソースの利用に関する情報をより効率的に理解でき、Azure AI Searchを活用した情報取得がスムーズに行えるように改善されています。

## articles/search/agentic-knowledge-source-how-to-work-iq.md{#item-94718e}

<details>
<summary>Diff</summary>
````diff
@@ -19,12 +19,14 @@ zone_pivot_groups: search-csharp-python-rest
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-A *Work IQ knowledge source* (preview) connects [Work IQ](/microsoft-365/copilot/extensibility/work-iq) to an agentic retrieval pipeline in Azure AI Search, providing intelligence from your organization's Microsoft 365 content as grounding data.
+A *Work IQ knowledge source* (preview) connects [Work IQ](/microsoft-365/copilot/extensibility/work-iq) to an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
-Unlike indexed knowledge sources, a Work IQ knowledge source queries Work IQ directly at retrieval time. No ingestion pipeline is needed. Queries require an end-user access token, which the retrieval engine uses to call Work IQ on the caller's behalf.
+Work IQ surfaces organizational intelligence from your Microsoft 365 content, including documents, emails, meetings, and activity across Microsoft 365 apps.
+
+Unlike indexed knowledge sources, Work IQ knowledge sources query live data directly at retrieval time. No ingestion pipeline is needed. Queries require an end-user access token, which the retrieval engine uses to call Work IQ on the caller's behalf.
 
 > [!WARNING]
-> In this preview, a Work IQ knowledge source may use Work IQ capabilities that perform actions, not just retrieve information. Use it with care, limit access to trusted applications and users, and review your scenario's permissions and governance controls before enabling it.
+> In this preview, a Work IQ knowledge source might use Work IQ capabilities that perform actions, not just retrieve information. Use it with care, limit access to trusted applications and users, and review your scenario's permissions and governance controls before enabling it.
 
 ### Usage support
 
@@ -113,7 +115,7 @@ Work IQ inherits Microsoft 365's compliance certifications. For details, see [Da
 
 ## Check for existing knowledge sources
 
-[!INCLUDE [](./includes/how-tos/knowledge-source-check.md)]
+[!INCLUDE [Check for existing knowledge sources](includes/how-tos/knowledge-source-check.md)]
 
 The following JSON is an example response for a Work IQ knowledge source.
 
@@ -211,11 +213,11 @@ The following properties apply to Work IQ knowledge sources.
 
 ## Assign to a knowledge base
 
-If you're satisfied with the knowledge source, continue to the next step: specify the knowledge source in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+If you're satisfied with the knowledge source, [add it to a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
 ## Query a knowledge base
 
-After the knowledge base is configured, use the [retrieve action](agentic-retrieval-how-to-retrieve.md) to query Work IQ content. This knowledge source has unique query-time permissions enforcement and response characteristics.
+After the knowledge base is configured, [call the retrieve action or MCP endpoint](agentic-retrieval-how-to-retrieve.md) to query Work IQ content. This knowledge source has unique query-time permissions enforcement and response characteristics.
 
 > [!IMPORTANT]
 > Work IQ can take 40–60 seconds or more to respond. To avoid timeout errors, set `maxRuntimeInSeconds` on the retrieve request to `120` or higher.
@@ -289,7 +291,7 @@ The following example shows a retrieve response containing a Work IQ knowledge s
 
 ## Delete a knowledge source
 
-[!INCLUDE [](./includes/how-tos/knowledge-source-delete.md)]
+[!INCLUDE [Delete a knowledge source](includes/how-tos/knowledge-source-delete.md)]
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Work IQ知識ソースの文書更新"
}
```

### Explanation
この変更では、Work IQ知識ソースに関する文書が更新され、Azure AI Searchにおける情報取得の方法が改善されています。

具体的な変更点は以下の通りです：
- **定義の明確化**: Work IQ知識ソースがAzure AI Searchのエージェントリトリーバルパイプラインに接続し、Microsoft 365の組織内コンテンツからのインテリジェンスを提供する仕組みが強調されています。また、知識ソースの独立した作成や使用方法についても具体的に言及されています。
- **データ取得の詳細な説明**: Work IQがMicrosoft 365コンテンツからの組織インテリジェンスを引き出すことを説明する新しい文章が追加され、ユーザーにとっての利点がより明確になっています。
- **警告の表現の変更**: 一部表現が「might」に変更され、より柔軟な読み手への配慮が示されています。具体的には、Work IQの機能に関する警告が強調され、信頼できるアプリケーションやユーザーに対するアクセス制限の重要性が上記されています。
- **手順の修正**: 知識ソースを知識ベースに追加する際の手順が「指定する」から「追加する」に変更され、よりシンプルで明確な表現になっています。
- **クエリ方法の更新**: クエリ時の知識ソースへのアクセス方法が「呼び出しアクションまたはMCPエンドポイントを呼び出す」という形に整理され、特異なクエリ時間の権限付与や応答特性についても言及されています。
- **関連リソースのリンク更新**: いくつかのインクルード参照や関連コンテンツのリンクが明確に更新され、文書全体の整合性が向上しています。

これらの変更により、Work IQ知識ソースの利用に関する情報がユーザーにとってより理解しやすくなり、Azure AI Searchを活用した情報の取得プロセスが円滑に進むように設計されています。

## articles/search/get-started-portal-agentic-retrieval.md{#item-2bf1dc}

<details>
<summary>Diff</summary>
````diff
@@ -235,21 +235,21 @@ To query the knowledge base:
 
    The activity log offers insight into the steps taken during retrieval, including query planning and execution, semantic ranking, and answer synthesis. For more information, see [Review the activity array](agentic-retrieval-how-to-retrieve.md#activity-array).
 
-## Review the created objects
+## Review the generated objects
 
 Azure AI Search automatically generates a data source, skillset, index, and indexer for each blob knowledge source. These objects form an end-to-end pipeline for data ingestion, enrichment, chunking, and vectorization. You can review these objects to learn how your data is processed for agentic retrieval.
 
 To review the auto-generated objects:
 
 1. From the left pane, select **Search management**.
 
+1. Check the indexer for success or failure messages. Connection or quota errors appear here.
+
 1. Check the data source to verify the connection to your blob storage container.
 
 1. Check the skillset to see how your content is chunked and vectorized using your embedding model.
 
-1. Check the index to see how your content is indexed and exposed for retrieval, including which fields are searchable and filterable and which fields store vectors for similarity search.
-
-1. Check the indexer for success or failure messages. Connection or quota errors appear here.
+1. Check the index to see how your content is indexed and exposed for retrieval, including which fields are searchable and filterable and which fields store vectors for similarity search. Use Search Explorer to run queries against the generated index.
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索の開始ガイドの文書更新"
}
```

### Explanation
この変更では、エージェント検索に関連する開始ガイドの文書が更新され、特に生成されたオブジェクトのレビューに関する説明が改善されています。

主な変更点は以下の通りです：
- **見出しの表現変更**: 「Review the created objects」という見出しが「Review the generated objects」に変更され、より適切な内容を反映しています。
- **オブジェクトのチェック手順の順序変更**: オート生成されたデータソース、スキルセット、インデックス、インデクサーに関する手順が整理され、より明確なチェック方法が提示されています。
- **インデクサーの位置変更**: インデクサーの確認手順が、他の手順の順序の中ではなく、最後に移動されており、より良い流れが確保されています。
- **新しい確認項目の追加**: データソースの接続確認の手順が追加され、Blobストレージコンテナへの接続が正しいかどうかを確認することが新たに推奨されています。
- **クエリ実行の強調**: インデックスに関連する説明が更新され、生成されたインデックスに対してSearch Explorerを使用してクエリを実行することが明示的に言及されています。

これにより、ユーザーはエージェント検索プロセスのオブジェクトの生成とレビューに関する情報をより理解しやすくなり、全体的なデータ処理の流れを把握しやすくなっています。

## articles/search/includes/how-tos/knowledge-source-delete.md{#item-4a16f9}

<details>
<summary>Diff</summary>
````diff
@@ -33,12 +33,19 @@ To delete a knowledge source:
 
    An example response might look like the following:
 
-   ```md
-    Knowledge Bases:
-      - earth-knowledge-base
-      - hotels-sample-knowledge-base
-      - my-demo-knowledge-base
-    ```
+   ```json
+    {
+        "@odata.context": "https://my-search-service.search.windows.net/$metadata#knowledgebases(name)",
+        "value": [
+        {
+            "name": "my-kb"
+        },
+        {
+            "name": "my-kb-2"
+        }
+        ]
+    }
+   ```
 
 1. Get an individual knowledge base definition to check for knowledge source references.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ソース削除ガイドの更新"
}
```

### Explanation
この変更では、知識ソースを削除するための手順を説明する文書が更新され、特に応答の形式に関する詳細が改善されています。

主な変更点は以下の通りです：
- **応答形式の変更**: 以前の例応答がMarkdown形式からJSON形式に変更され、より標準的なデータ形式としてのJSONが使用されています。これにより、開発者が実際のAPI応答と一致する形式で例を確認できるようになります。
- **具体的な内容の追加**: 新しいJSON形式の応答には、知識ベースの情報が含まれ、具体的な知識ベース名（例: "my-kb", "my-kb-2"）が示されています。これにより、ユーザーは削除対象の知識ソースを識別しやすくなります。
- **コーディングブロックの明確化**: コーディングブロックの表現が改善され、コードが明確に区別され、理解しやすくなっています。

これらの変更によって、ユーザーは知識ソースの削除手順をより具体的に理解し、実際のAPIとの整合性を持った形で操作を進めることができるようになります。

## articles/search/includes/how-tos/knowledge-source-review-objects.md{#item-0babd3}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,19 @@
+---
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 05/29/2026
+---
+
+When you create this knowledge source, Azure AI Search automatically generates a data source, skillset, indexer, and index. The creation response lists each object under `createdResources`.
+
+These objects are generated according to a fixed template, and their names are based on the name of the knowledge source. You can't change the object names. Avoid editing these objects directly, as changes can introduce errors or incompatibilities that break the indexer pipeline.
+
+You can use the Azure portal to validate object creation. The workflow is:
+
+1. Check the indexer for success or failure messages. Connection or quota errors appear here.
+
+1. Check the data source to verify the connection to your data store. The connection uses either a connection string or a managed identity, depending on how you configured the knowledge source.
+
+1. Check the skillset to see how your content is chunked and optionally vectorized.
+
+1. Check the index to see how your content is indexed and exposed for retrieval, including which fields are searchable and filterable and which fields store vectors for similarity search. Use Search Explorer to run queries against the generated index.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "知識ソースの生成オブジェクトレビューガイドの追加"
}
```

### Explanation
この変更では、Azure AI Searchにおける知識ソースを作成した際に自動生成されるオブジェクトのレビューに関する新しいガイドが追加されました。この文書は、生成されたデータソース、スキルセット、インデクサー、インデックスに関する詳細情報を提供します。

主な内容は以下の通りです：
- **生成オブジェクトの概要**: ユーザーが知識ソースを作成すると、関連するデータソースやインデクサーなどのオブジェクトが自動的に生成され、それらがどのように利用されるかが説明されています。
- **オブジェクト名の固定性に関する注意**: 生成されたオブジェクトの名前は知識ソースに基づいているため変更できず、直接編集しないよう警告がされています。これにより、インデクサーのパイプラインが壊れるリスクを回避することができます。
- **Azureポータルでの検証手順**: オブジェクトの作成を確認するための具体的な手順（インデクサー、データソース、スキルセット、インデックスのチェック）が順序立てて示されています。
- **クエリ実行の提案**: 最後に、ユーザーが生成されたインデックスに対してクエリを実行するためにSearch Explorerを使用することが推奨されています。

このガイドの追加により、ユーザーは知識ソースの生成プロセスとその結果をより良く理解し、効果的に対応するための情報を手に入れることができます。


