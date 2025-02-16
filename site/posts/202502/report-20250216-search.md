---
date: '2025-02-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b07793e...MicrosoftDocs:1cff62f
summary: Azure AI Searchのドキュメントに関する複数のマイナーアップデートが実施されました。これらの更新では、APIバージョンのアップグレード、診断ログの設定、APIキーの使用、ベクトルインデックスの作成方法、セキュリティに関する新しい情報が追加されました。特に、セキュリティアップデートにより、GETリクエストの応答から接続文字列やキーが返されないよう修正されています。また、用語の見直しや診断ログ設定の明確化も行われています。これらの変更により、開発者は新しいAPIを効果的に活用し、安全にシステムを運用できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b07793e...MicrosoftDocs:1cff62f){target="_blank"}

# ハイライト

Azure AI Searchのドキュメントに関する複数のマイナーアップデートが実施されました。これらの更新は、APIバージョンのアップグレード、診断ログの設定、APIキーの使用、ベクトルインデックスの作成方法、およびセキュリティに関する新しい情報に焦点を当てています。これにより、開発者が新しいバージョンのAPIを活用し、適切なセキュリティ対策を講じるためのガイドラインが強化されました。

## 新機能
- Azure AI Searchの新しいAPIバージョンに関する情報と具体的なアップグレード手順の追加。
- Azure AI Searchのベクトルインデックス作成についての詳細な説明とガイドラインの改善。
- セキュリティアップデートに関する最新情報の提供。

## 互換性の破れ
- セキュリティアップデートにより、GETリクエストの応答から接続文字列やキーが返されないよう修正されました。

## その他の更新
- APIドキュメント中の「管理面」という用語の「コントロールプレーン」への変更。
- 領域および機能に関連する診断ログ設定の明確化とリンクの追加。

# インサイト

これらの変更は、Azure AI Searchを利用する企業や開発者にとって重要なガイドラインを提供するためのものです。特に、APIバージョンのアップグレードやセキュリティへの対応は、システムの最新化や安全性の確保に非常に重要です。

APIのアップグレードに関しては、データ平面と管理平面（コントロールプレーン）における具体的な対応策が示されています。これにより、開発者は新しいバージョンに対応するコード変更を迅速に行うことができ、APIキーの使用を含む統一された用語を通じてAPIの利用を理解しやすくなりました。

また、ベクトルインデックスの作成手順の改善は、特にセマンティッククエリを活用するデータサイエンティストにとって貴重な情報となります。詳細なAPIコールの例が含まれていることで、実際の開発現場での適用が容易になります。

さらに、セキュリティアップデートが、未許可のアクセスを防ぐための具体的な情報を明示しており、クライアントコードへの影響を考慮した情報提供が行われています。これにより、ユーザーはシステムの安全性を高めるための具体的な策を講じることができ、新しいストレージクォータや機能を最大限に活用することが可能になります。

これらの文書更新は、開発者が効率的かつ安全にシステムを運用し、最新のAzure AI Searchの特性を活用するための道しるべとなっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-api-migration.md](#item-07297b) | minor update | Azure AI Search REST APIのアップグレードに関する最新情報 | modified | 58 | 32 | 90 | 
| [search-monitor-enable-logging.md](#item-e3600e) | minor update | Azure AI Searchの診断ログ設定に関する修正 | modified | 1 | 1 | 2 | 
| [search-security-api-keys.md](#item-d8c908) | minor update | Azure AI SearchのAPIキーの使用に関する修正 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-create-index.md](#item-97c769) | minor update | Azure AI Searchにおけるベクトルインデックスの作成方法に関する更新 | modified | 70 | 34 | 104 | 
| [whats-new.md](#item-fa71b4) | minor update | 新しいセキュリティアップデートに関する情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-api-migration.md{#item-07297b}

<details>
<summary>Diff</summary>
````diff
@@ -12,16 +12,19 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: conceptual
-ms.date: 11/19/2024
+ms.date: 02/14/2025
 ---
 
 # Upgrade to the latest REST API in Azure AI Search
 
-Use this article to migrate data plane calls to newer versions of the [**Search REST APIs**](/rest/api/searchservice/).
+Use this article to migrate to newer versions of the [**Search Service REST APIs**](/rest/api/searchservice/) and the [**Search Management REST APIs**](/rest/api/searchmanagement/) for [data plane and control plane](/azure/azure-resource-manager/management/control-plane-and-data-plane) operations.
 
-+ [`2024-07-01`](/rest/api/searchservice/search-service-api-versions#2024-07-01) is the most recent stable version.
-
-+ [`2024-11-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-11-01-preview) is the most recent preview API version. 
+| Targeted operations | REST API | Status |
+|---------------------|----------|--------|
+| Data plane | [`2024-07-01`](/rest/api/searchservice/search-service-api-versions#2024-07-01) | Stable |
+| Data plane | [`2024-11-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-11-01-preview) | Preview |
+| Control plane | [`2023-11-01`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2023-11-0&preserve-view=true1) | Stable |
+| Control plane | [`2024-03-01-preview`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2024-03-01-preview&preserve-view=true) | Preview |
 
 Upgrade instructions focus on code changes that get you through breaking changes from previous versions so that existing code runs the same as before, but on the newer API version. Once your code is in working order, you can decide whether to adopt newer features. To learn more about new features, see [vector code samples](https://github.com/Azure/azure-search-vector-samples) and [What's New](whats-new.md).
 
@@ -36,25 +39,29 @@ We recommend upgrading API versions in succession, working through each version
 
 Azure AI Search breaks backward compatibility as a last resort. Upgrade is necessary when:
 
-+ Your code references a retired or unsupported API version and is subject to one or more breaking changes. You must address breaking changes if your code targets [`2023-07-10-preview`](#code-upgrade-for-vector-indexes-and-queries) for vectors, [`2020-06-01-preview`](#breaking-change-for-semantic-ranker) for semantic ranker, and [`2019-05-06`](#upgrade-to-2019-05-06) for obsolete skills and workarounds. 
++ Your code references a retired or unsupported API version and is subject to one or more breaking changes. You must address breaking changes if your code targets [`2023-07-10-preview`](#code-upgrade-for-vector-indexes-and-queries) for vectors, [`2020-06-01-preview`](#breaking-changes-for-semantic-ranker) for semantic ranker, and [`2019-05-06`](#upgrade-to-2019-05-06) for obsolete skills and workarounds. 
 
 + Your code fails when unrecognized properties are returned in an API response. As a best practice, your application should ignore properties that it doesn't understand.
 
 + Your code persists API requests and tries to resend them to the new API version. For example, this might happen if your application persists continuation tokens returned from the Search API (for more information, look for `@search.nextPageParameters` in the [Search API Reference](/rest/api/searchservice/documents/search-post)).
 
 ## How to upgrade
 
-1. Review the [release notes](/rest/api/searchservice/search-service-api-versions) for each API version.
+1. If you're upgrading a data plane version, review the [release notes](/rest/api/searchservice/search-service-api-versions) for the new API version.
 
 1. Update the `api-version` parameter, specified in the request header, to a newer version. 
 
    In your application code that makes direct calls to the REST APIs, search for all instances of the existing version and then replace it with the new version. For more information about structuring a REST call, see [Quickstart: using REST](search-get-started-rest.md#set-up-visual-studio-code).
 
    If you're using an Azure SDK, those packages target specific versions of the REST API. Package updates might coincide with a REST API update, but each SDK is on its own release schedule that ships independently of Azure AI Search REST API versions. Check the change log of your SDK package to determine whether a package release targets the latest REST API version.
 
-1. Review the breaking changes documented in this article and implement the workarounds. Start with the version used by your code and resolve any breaking change for each newer API version until you get to the newest stable or preview release.
+1. If you're upgrading a data plane version, review the breaking changes documented in this article and implement the workarounds. Start with the version used by your code and resolve any breaking change for each newer API version until you get to the newest stable or preview release.
+
+## Breaking changes
+
+The following breaking changes apply to data operations.
 
-## Breaking change for client code that reads connection information
+### Breaking changes for client code that reads connection information
 
 Effective March 29, 2024 and applicable to all [supported REST APIs](/rest/api/searchservice/search-service-api-versions): 
 
@@ -64,17 +71,19 @@ Effective March 29, 2024 and applicable to all [supported REST APIs](/rest/api/s
 
 + If you need to retrieve connection strings of another Azure resource such as Azure Storage or Azure Cosmos DB, use the APIs of that resource and published guidance to obtain the information. 
 
-## Breaking change for semantic ranker
+### Breaking changes for semantic ranker
 
-[Semantic ranker](semantic-search-overview.md) is generally available in `2023-11-01`. Here are the breaking changes for semantic ranker from earlier releases:
+[Semantic ranker](semantic-search-overview.md) is generally available in `2023-11-01`. There are the breaking changes from earlier releases:
 
 + In all versions after `2020-06-01-preview`: `semanticConfiguration` replaces `searchFields` as the mechanism for specifying which fields to use for L2 ranking.
 
 + For all API versions, updates on July 14, 2023 to the Microsoft-hosted semantic models made semantic ranker language-agnostic, effectively decommissioning the `queryLanguage` property. There's no "breaking change" in code, but the property is ignored.
 
 See [Migrate from preview version](semantic-code-migration.md) to transition your code to use `semanticConfiguration`.
 
-## Upgrade to 2024-11-01-preview
+## Data plane upgrades
+
+### Upgrade to 2024-11-01-preview
 
 [`2024-11-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-11-01-preview) query rewrite, Document Layout skill, keyless billing for skills processing, Markdown parsing mode, and rescoring options for compressed vectors.
 
@@ -87,21 +96,21 @@ However, the new version introduces syntax changes to `vectorSearch.compressions
 
 Backwards compatibility is preserved due to an internal API mapping, but we recommend changing the syntax if you adopt the new preview version. For a comparison of the syntax, see [Compress vectors using scalar or binary quantization](vector-search-how-to-quantization.md#add-compressions-to-a-search-index).
 
-## Upgrade to 2024-09-01-preview
+### Upgrade to 2024-09-01-preview
 
 [`2024-09-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-09-01-preview) adds Matryoshka Representation Learning (MRL) compression for text-embedding-3 models, targeted vector filtering for hybrid queries, vector subscore details for debugging, and token chunking for [Text Split skill](cognitive-search-skill-textsplit.md).
 
 If you're upgrading from `2024-05-01-preview`, you can use the new preview APIs with no change to existing code.
 
-## Upgrade to 2024-07-01
+### Upgrade to 2024-07-01
 
 [`2024-07-01`](/rest/api/searchservice/search-service-api-versions#2024-07-01) is a general release. The former preview features are now generally available: integrated chunking and vectorization (Text Split skill, AzureOpenAIEmbedding skill), query vectorizer based on AzureOpenAIEmbedding, vector compression (scalar quantization, binary quantization, stored property, narrow data types).
 
 There are no breaking changes if you upgrade from `2024-05-01-preview` to stable. To use the new stable release, change the API version and test your code.
 
 There are breaking changes if you upgrade directly from `2023-11-01`. Follow the steps outlined for each newer preview to migrate from `2023-11-01` to `2024-07-01`.
 
-## Upgrade to 2024-05-01-preview
+### Upgrade to 2024-05-01-preview
 
 [`2024-05-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-05-01-preview) adds OneLake index, support for binary vectors, and support for more embedding models. 
 
@@ -111,37 +120,37 @@ If you're upgrading from `2024-03-01-preview`, the AzureOpenAIEmbedding skill no
 
 1. Set `modelName` to "text-embedding-ada-002" and set `dimensions` to "1536".
 
-## Upgrade to 2024-03-01-preview
+### Upgrade to 2024-03-01-preview
 
 [`2024-03-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-03-01-preview) adds narrow data types, scalar quantization, and vector storage options. 
 
 If you're upgrading from `2023-10-01-preview`, there are no breaking changes. However, there's one behavior difference: for `2023-11-01` and newer previews, the `vectorFilterMode` default changed from postfilter to prefilter for [filter expressions](vector-search-filters.md).
 
 1. Search your codebase for `vectorFilterMode` references.
 
-1. If the property is explicitly set, no action is required. If you used the default, be aware that the new default behavior is to filter before query execution. If you want post-query filtering, explicitly set `vectorFilterMode` to postfilter to retain the old behavior.
+1. If the property is explicitly set, no action is required. If you relied on the default value, the new default behavior is to filter *before* query execution. If you want post-query filtering, explicitly set `vectorFilterMode` to postfilter to retain the old behavior.
 
-## Upgrade to 2023-11-01
+### Upgrade to 2023-11-01
 
-[`2023-11-01`](/rest/api/searchservice/search-service-api-versions#2023-11-01) is a general release. The former preview features are now generally available: semantic ranker, vector index and query support.
+[`2023-11-01`](/rest/api/searchservice/search-service-api-versions#2023-11-01) is a general release. The former preview features are now generally available: semantic ranker and vector support.
 
 There are no breaking changes from `2023-10-01-preview`, but there are multiple breaking changes from `2023-07-01-preview` to `2023-11-01`. For more information, see [Upgrade from 2023-07-01-preview](#upgrade-from-2023-07-01-preview).
 
 To use the new stable release, change the API version and test your code.
 
-## Upgrade to 2023-10-01-preview
+### Upgrade to 2023-10-01-preview
 
 [`2023-10-01-preview`](/rest/api/searchservice/search-service-api-versions#2023-10-01-preview) was the first preview version to add [built-in data chunking and vectorization during indexing](vector-search-integrated-vectorization.md) and [built-in query vectorization](vector-search-how-to-configure-vectorizer.md). It also supports vector indexing and queries from the previous version.
 
 If you're upgrading from the previous version, the next section has the steps. 
 
-## Upgrade from 2023-07-01-preview
+### Upgrade from 2023-07-01-preview
 
 Don't use this API version. It implements a vector query syntax that's incompatible with any newer API version.
 
 `2023-07-01-preview` is now deprecated, so you shouldn't base new code on this version, nor should you upgrade *to* this version under any circumstances. This section explains the migration path from `2023-07-01-preview` to any newer API version.
 
-### Portal upgrade for vector indexes
+#### Portal upgrade for vector indexes
 
 Azure portal supports a one-click upgrade path for `2023-07-01-preview` indexes. It detects vector fields and provides a **Migrate** button. 
 
@@ -153,7 +162,7 @@ There's no portal migration for upgrading vector query syntax. See [code upgrade
 
 Before selecting **Migrate**, select **Edit JSON** to review the updated schema first. You should find a schema that conforms to the changes described in the [code upgrade](#code-upgrade-for-vector-indexes-and-queries) section. Portal migration only handles indexes with one vector search algorithm configuration. It creates a default profile that maps to the `2023-07-01-preview` vector search algorithm. Indexes with multiple vector search configurations require manual migration.
 
-### Code upgrade for vector indexes and queries
+#### Code upgrade for vector indexes and queries
 
 [Vector search](vector-search-overview.md) support was introduced in [Create or Update Index (2023-07-01-preview)](/rest/api/searchservice/preview-api/create-or-update-index). 
 
@@ -317,25 +326,25 @@ Use the instructions in this section to migrate vector fields, configuration, an
 
 These steps complete the migration to `2023-11-01` stable API version or newer preview API versions.
 
-## Upgrade to 2020-06-30
+### Upgrade to 2020-06-30
 
 In this version, there's one breaking change and several behavioral differences. Generally available features include:
 
 + [Knowledge store](knowledge-store-concept-intro.md), persistent storage of enriched content created through skillsets, created for downstream analysis and processing through other applications. A knowledge store is created through Azure AI Search REST APIs but it resides in Azure Storage. 
 
-### Breaking change
+#### Breaking change
 
 Code written against earlier API versions breaks on `2020-06-30` and later if code contains the following functionality:
 
 + Any `Edm.Date` literals (a date composed of year-month-day, such as `2020-12-12`) in filter expressions must follow the `Edm.DateTimeOffset` format: `2020-12-12T00:00:00Z`. This change was necessary to handle erroneous or unexpected query results due to timezone differences.
 
-### Behavior changes
+#### Behavior changes
 
 + [BM25 ranking algorithm](index-ranking-similarity.md) replaces the previous ranking algorithm with newer technology. Services created after 2019 use this algorithm automatically. For older services, you must set parameters to use the new algorithm.  
 
 + Ordered results for null values have changed in this version, with null values appearing first if the sort is `asc` and last if the sort is `desc`. If you wrote code to handle how null values are sorted, be aware of this change.
 
-## Upgrade to 2019-05-06
+### Upgrade to 2019-05-06
 
 Features that became generally available in this API version include:
 
@@ -344,7 +353,7 @@ Features that became generally available in this API version include:
 + [JsonLines parsing modes](search-howto-index-json-blobs.md), part of Azure Blob indexing, creates one search document per JSON entity that is separated by a newline.
 + [AI enrichment](cognitive-search-concept-intro.md) provides indexing that uses the AI enrichment engines of Azure AI services.
 
-### Breaking changes
+#### Breaking changes
 
 Code written against an earlier API version breaks on `2019-05-06` and later if it contains the following functionality:
 
@@ -356,7 +365,7 @@ Code written against an earlier API version breaks on `2019-05-06` and later if
 
 1. Named Entity Recognition cognitive skill is retired. If you called the [Name Entity Recognition](cognitive-search-skill-named-entity-recognition.md) skill in your code, the call fails. Replacement functionality is [Entity Recognition Skill (V3)](cognitive-search-skill-entity-recognition-v3.md). Follow the recommendations in [Deprecated skills](cognitive-search-skill-deprecated.md) to migrate to a supported skill.
 
-### Upgrading complex types
+#### Upgrading complex types
 
 API version `2019-05-06` added formal support for complex types. If your code implemented previous recommendations for complex type equivalency in 2017-11-11-Preview or 2016-09-01-Preview, there are some new and changed limits starting in version `2019-05-06` of which you need to be aware:
 
@@ -366,7 +375,7 @@ API version `2019-05-06` added formal support for complex types. If your code im
 
 For more information, see [Service limits for Azure AI Search](search-limits-quotas-capacity.md).
 
-#### How to upgrade an old complex type structure
+##### How to upgrade an old complex type structure
 
 If your code is using complex types with one of the older preview API versions, you might be using an index definition format that looks like this:
 
@@ -414,9 +423,26 @@ You can update flat indexes to the new format with the following steps using API
 1. Perform a PUT request to update the index to the new format. Avoid changing any other details of the index, such as the searchability/filterability of fields, because changes that affect the physical expression of existing index isn't allowed by the Update Index API.
 
 > [!NOTE]
-> It is not possible to manage indexes created with the old "flat" format from the Azure portal. Please upgrade your indexes from the “flat” representation to the “tree” representation at your earliest convenience.
+> It isn't possible to manage indexes created with the old "flat" format from the Azure portal. Upgrade your indexes from the “flat” representation to the “tree” representation at your earliest convenience.
+
+## Control plane upgrades
+
+**Applies to:** `2014-07-31-Preview`, `2015-02-28`, and `2015-08-19`
+
+The `listQueryKeys` GET request on older Search Management API versions is now deprecated. We recommend migrating to the most recent stable control plane API version to use the `listQueryKeys` POST request.
+
+1. In existing code, change the `api-version` parameter to the most recent version (`2023-11-01`).
+
+1. Refactor the request from `GET` to `POST`:
+
+   ```http
+   POST https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}/listQueryKeys?api-version=2023-11-01
+   Authorization: Bearer {{token}}
+   ```
+
+1. If you're using an Azure SDK, it's recommended that you upgrade to the latest version.
 
-## Next steps
+### Next steps
 
 Review the Search REST API reference documentation. If you encounter problems, ask us for help on [Stack Overflow](https://stackoverflow.com/) or [contact support](https://azure.microsoft.com/support/community/?product=search).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search REST APIのアップグレードに関する最新情報"
}
```

### Explanation
この変更は、Azure AI Search REST APIのアップグレードに関するドキュメントの更新を含んでいます。主な内容としては、データ平面および管理平面のAPIバージョンに関する情報の追加と具体的なアップグレード手順の強調があります。新しいAPIバージョンが具体的に示され、これに伴う互換性の破れや注意点についての詳細が記載されています。

新しい日付やバージョンの情報が加えられ、ユーザーがアップグレードを行う際の指示が整理されているため、開発者が必要な変更を迅速に実施できるようになっています。また、コードの更新が必要な場合のガイダンスや、新しい機能への移行に関する手順も明確にされています。

変更により、確実にシステムが新しいREST APIバージョンと互換性を持つようになり、古いAPIバージョンからの移行がスムーズに行える情報が提供されています。コミュニティサポートや問題解決のためのリソースへのリンクも含まれており、ユーザーが直面する可能性のある問題に対処するための助けとなる情報が整っています。

## articles/search/search-monitor-enable-logging.md{#item-e3600e}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ ms.date: 01/28/2025
 
 # Configure diagnostic logging for Azure AI Search
 
-Resource-level diagnostic logs provide insight into operations that occur in your Azure AI Search resource. In contrast, activity logs provide an insight into the operations performed on each Azure resource in the subscription from the outside, known as the control plane or management plane. Activity logging is enabled automatically, and often
+Resource-level diagnostic logs provide insight into operations that occur in your Azure AI Search resource. In contrast, activity logs provide an insight into the operations performed on each Azure resource in the subscription from the outside, known as the [control plane](/azure/azure-resource-manager/management/control-plane-and-data-plane). Activity logging is enabled automatically, and often
 
 This article explains how to enable resource-level diagnostic logging and how to find information about system and user operations on an Azure AI Search resource.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchの診断ログ設定に関する修正"
}
```

### Explanation
この変更は、Azure AI Searchにおける診断ログ設定に関するドキュメントの内容を改善しています。具体的には、リソースレベルの診断ログとコントロールプレーン活動ログの違いに関する説明にリンクが追加されました。このリンクは、リソース管理に関連する詳細情報を提供するためのもので、ユーザーがコントロールプレーンの概念についてさらに学ぶための助けとなります。

この文書は、Azure AI Searchリソースでのシステムおよびユーザー操作に関する情報を見つける方法と、リソースレベルの診断ログを有効にする方法を説明しています。そのため、ユーザーはログや操作の監視を効果的に行えるようになります。全体として、この変更は情報の明確性を高め、機能的な理解を促進することを目的としています。

## articles/search/search-security-api-keys.md{#item-d8c908}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ Visually, there's no distinction between an admin key or query key. Both keys ar
 
 API keys are used for data plane (content) requests, such as creating or accessing an index or, any other request that's represented in the [Search REST APIs](/rest/api/searchservice/). 
 
-You can use either an API key or [Azure roles](search-security-rbac.md) for management plane (service) requests. When you use an API key:
+You can use either an API key or [Azure roles](search-security-rbac.md) for control plane (service) requests. When you use an API key:
 - Admin keys are used for creating, modifying, or deleting objects. Admin keys are also used to GET object definitions and system information.
 - Query keys are typically distributed to client applications that issue queries.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI SearchのAPIキーの使用に関する修正"
}
```

### Explanation
この変更は、Azure AI SearchにおけるAPIキーの使用に関するドキュメントの表現を修正しています。具体的には、管理面（サービス）リクエストに関する記述で、「管理面」という用語が「コントロールプレーン」に変更されました。これにより、用語の正確さが向上し、ユーザーがAPIキーを使用する際の理解が深まります。

APIキーは、データプレーンリクエスト（インデックスの作成やアクセスなど）とコントロールプレーンリクエスト（サービス関連の操作）を行うために使用されます。文書のこの部分では、管理用のAPIキーとクエリキーの役割についても説明されており、ユーザーがそれぞれのキーをどのように適切に使用するかのガイダンスが整理されています。全体として、この変更は情報の明確性を高め、ユーザーがAPIキーの機能を効果的に理解できるようにしています。

## articles/search/vector-search-how-to-create-index.md{#item-97c769}

<details>
<summary>Diff</summary>
````diff
@@ -9,80 +9,102 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 01/09/2025
+ms.date: 02/14/2025
 ---
 
 # Create a vector index
 
-In Azure AI Search, a *vector store* has an index schema that defines vector and nonvector fields, a vector configuration for algorithms that create and compress the embedding space, and settings on vector field definitions that are used in query requests. 
+In Azure AI Search, you can store vectors in a search index and send vector queries to match on semantic similarity. A vector store in Azure AI Search has an index schema that defines both vector and nonvector fields. It also has a vector configuration for algorithms used to create and compress the embedding space.
 
-The [Create or Update Index](/rest/api/searchservice/indexes/create-or-update) API creates the vector store. Follow these steps to index vector data:
+[Create or Update Index API](/rest/api/searchservice/indexes/create-or-update) creates the vector store. Follow these steps to index vectors in Azure AI Search:
 
 > [!div class="checklist"]
-> + Define a schema with vector algorithms and optional compression
+> + Start with a basic schema definition
+> + Add vector algorithms and optional compression
 > + Add vector field definitions
 > + Load prevectorized data [as a separate step](#load-vector-data-for-indexing), or use [integrated vectorization](vector-search-integrated-vectorization.md) for data chunking and encoding during indexing
 
-This article explains the workflow and uses REST for illustration. Once you understand the basic workflow, continue with the Azure SDK code samples in the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) repository for guidance on using these features in test and production code.
+This article explains the workflow using the REST API for illustration. Once you understand the basic workflow, continue with the Azure SDK code samples in the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) repository for guidance on using vectors in test and production code.
 
 > [!TIP]
-> Use the Azure portal to [create a vector index](search-get-started-portal-import-vectors.md) and try integrated data chunking and vectorization.
+> You can also use the Azure portal to [create a vector index](search-get-started-portal-import-vectors.md) and try out integrated data chunking and vectorization.
 
 ## Prerequisites
 
-+ Azure AI Search, in any region and on any tier. On services created before January 2019, there's a small subset that can't create a vector index. If this applies to you, create a new service to use vectors. For indexing workloads that include integrated vectorization (skillsets that call Azure AI), Azure AI Search must be in the same region as Azure OpenAI or Azure AI services.
++ Azure AI Search, in any region and on any tier. If you plan to use [integrated vectorization](vector-search-integrated-vectorization.md), Azure AI Search must be in the same region as the embedding models hosted on Azure OpenAI or in Azure AI Vision.
 
-+ You must have [pre-existing vector embeddings](vector-search-how-to-generate-embeddings.md) to upload to the index, or you can use [integrated vectorization](vector-search-integrated-vectorization.md), where embedding models are called from a skillset in an indexer pipeline.
++ Your source documents must have [vector embeddings](vector-search-how-to-generate-embeddings.md) to upload to the index. Or, you can use [integrated vectorization](vector-search-integrated-vectorization.md) for this step.
 
-+ You should know the dimensions limit of the model used to create the embeddings so that you can assign that limit to the vector field. Integrated vectorization supports a finite number of embedding models. For **text-embedding-ada-002**, dimensions are fixed at 1536. For **text-embedding-3-small** or **text-embedding-3-large**, the vector length ranges from 1 to 1536 and 3072, respectively. 
++ You should know the dimensions limit of the model used to create the embeddings so that you can assign that limit to the vector field. For **text-embedding-ada-002**, dimensions are fixed at 1536. For **text-embedding-3-small** or **text-embedding-3-large**, dimensions range from 1 to 1536 and 3072, respectively. 
 
 + You should also know what similarity metric to use. For embedding models on Azure OpenAI, similarity is [computed using `cosine`](/azure/ai-services/openai/concepts/understand-embeddings#cosine-similarity). 
 
 + You should be familiar with [creating an index](search-how-to-create-search-index.md). The schema must include a field for the document key, other fields you want to search or filter, and other configurations for behaviors needed during indexing and queries. 
 
+## Limitations
+
+For search services created before January 2019, there's a small subset that can't create a vector index. If this applies to you, create a new service to use vectors.
+
 ## Prepare documents for indexing
 
-Prior to indexing, assemble a document payload that includes fields of vector and nonvector data. The document structure must conform to the index schema. 
+Before indexing, assemble a document payload that includes fields of vector and nonvector data. The document structure must conform to the index schema. 
 
-Make sure your documents:
+Make sure your documents provide the following content:
 
-1. Provide a field or a metadata property that uniquely identifies each document. All search indexes require a document key. To satisfy document key requirements, a source document must have one field or property that can uniquely identify it in the index. This source field must be mapped to an index field of type `Edm.String` and `key=true` in the search index. 
+| Content | Description |
+|---------|-------------|
+| Unique identifier | A field or a metadata property that uniquely identifies each document. All search indexes require a document key. To satisfy document key requirements, a source document must have one field or property uniquely identifies it in the index. If you're indexing blobs, it might be the metadata_storage_path that uniquely identifies each blob. If you're indexing from a database, it might be primary key. This source field must be mapped to an index field of type `Edm.String` and `key=true` in the search index.|
+| Non-vector content | Provide other fields with human-readable content. Human readable content is useful for the query response, and for hybrid query scenarios that include full text search or semantic ranking in the same request. If you're using a chat completion model, most models like ChatGPT don't accept raw vectors as input. |
+| Vector content| A vectorized version of your non-vector content. A vector is an array of single-precision floating point numbers generated by an embedding model. Each vector field contains an array generated by an embedding model, one embedding per field, where the field is a top-level field (not part of a nested or complex type). For the simplest integration, we recommend the embedding models in [Azure OpenAI](https://aka.ms/oai/access), such as an **text-embedding-3** model for text documents or the [Image Retrieval REST API](/rest/api/computervision/image-retrieval/vectorize-image) for images. <br><br>If you can take a dependency on indexers and skillsets, consider using [integrated vectorization](vector-search-integrated-vectorization.md) that encodes images and textual content during indexing. Your field definitions are for vector fields, but incoming source data can be text or images, which are converted to vector arrays during indexing. |
 
-1. Provide vector data (an array of single-precision floating point numbers) in source fields.
+Your search index should include fields and content for all of the query scenarios you want to support. Suppose you want to search or filter over product names, versions, metadata, or addresses. In this case, vector similarity search isn't especially helpful. Keyword search, geo-search, or filters would be a better choice. A search index that includes a comprehensive collection of both vector and nonvector fields provides maximum flexibility for query construction and response composition.
 
-   Vector fields contain an array generated by embedding models, one embedding per field, where the field is a top-level field (not part of a nested or complex type). For the simplest integration, we recommend the embedding models in [Azure OpenAI](https://aka.ms/oai/access), such as a **text-embedding-3** model for text documents or the [Image Retrieval REST API](/rest/api/computervision/2023-02-01-preview/image-retrieval/vectorize-image) for images.
+A short example of a documents payload that includes vector and nonvector fields is in the [load vector data](#load-vector-data-for-indexing) section of this article.
 
-   If you can take a dependency on indexers and skillsets, consider using [integrated vectorization](vector-search-integrated-vectorization.md) that encodes images and textual content during indexing. Your field definitions are for vector fields, but incoming source data can be text or images, which are converted to vector arrays during indexing.
+## Start with a basic index
 
-1. Provide other fields with human-readable content for the query response, and for hybrid query scenarios that include full text search or semantic ranking in the same request. 
+Start with a minimum schema so that you have a definition to work with before adding a vector configuration and vector fields. A simple index might look the following example. You can learn more about an index schema in [Create a search index](search-how-to-create-search-index.md).
 
-Your search index should include fields and content for all of the query scenarios you want to support. Suppose you want to search or filter over product names, versions, metadata, or addresses. In this case, similarity search isn't especially helpful. Keyword search, geo-search, or filters would be a better choice. A search index that includes a comprehensive field collection of vector and nonvector data provides maximum flexibility for query construction and response composition.
+Notice that it has a required name, a required document key (`"key": true`), and fields for human readable content in plain text. It's common to have a human-readable version of whatever content you intend to vectorize. For example, if you have a chunk of text from a PDF file, your index schema should have the plain text equivalent of the vectorized text. 
 
-A short example of a documents payload that includes vector and nonvector fields is in the [load vector data](#load-vector-data-for-indexing) section of this article.
+```http
+POST https://[servicename].search.windows.net/indexes?api-version=[api-version] 
+{
+  "name": "example-index",
+  "fields": [
+    { "name": "documentId", "type": "Edm.String", "key": true, "retrievable": true, "searchable": true, "filterable": true },
+    { "name": "myHumanReadableNameField", "type": "Edm.String", "retrievable": true, "searchable": true, "filterable": false, "sortable": true, "facetable": false },
+    { "name": "myHumanReadableContentField", "type": "Edm.String", "retrievable": true, "searchable": true, "filterable": false, "sortable": false, "facetable": false, "analyzer": "en.microsoft" },
+  ],
+  "suggesters": [ ],
+  "scoringProfiles": [ ],
+  "analyzers":(optional)[ ... ]
+}
+```
 
 ## Add a vector search configuration
 
-A vector configuration specifies the parameters used during indexing to create "nearest neighbor" information among the vector nodes:
+Next, add a vector search configuration to your schema. Configuration occurs before field definitions because you specify one on each field as part of its definition. In the schema, vector configuration is typically added after the fields collection, perhaps after `"suggesters"`, `"scoringProfiles"`, or `"analyzers"`.
+
+A vector configuration specifies the parameters used during indexing to create "nearest neighbor" information among the vector nodes. Algorithms include:
 
 + Hierarchical Navigable Small World (HNSW)
-+ Exhaustive KNN
++ Exhaustive k-Nearest Neighbor (KNN)
 
-If you choose HNSW on a field, you can opt in for exhaustive KNN at query time. But the other direction doesn’t work: if you choose exhaustive, you can’t later request HNSW search because the extra data structures that enable approximate search don’t exist.
+If you choose HNSW on a field, you can opt in for exhaustive KNN at query time. But the other direction doesn’t work: if you choose exhaustive for indexing, you can’t later request HNSW search because the extra data structures that enable approximate search don’t exist.
 
 Optionally, a vector configuration also specifies quantization methods for reducing vector size:
 
 + Scalar
 + Binary (available in 2024-07-01 only and in newer Azure SDK packages)
 
-For instructions on how to migrate to the latest version, see [Upgrade REST API](search-api-migration.md).
-
 ### [**2024-07-01**](#tab/config-2024-07-01)
 
 [**2024-07-01**](/rest/api/searchservice/search-service-api-versions#2024-07-01) is generally available. It supports a vector configuration having:
 
 + `vectorSearch.algorithms` support HNSW and exhaustive KNN.
 + `vectorSearch.compressions` support scalar and binary quantization, oversampling, and reranking with original vectors.
-+ `vectorSearch.profiles` provide for multiple combinations of algorithm and compression configurations.
++ `vectorSearch.profiles` for specifying multiple combinations of algorithm and compression configurations.
 
 Be sure to have a strategy for [vectorizing your content](vector-search-how-to-generate-embeddings.md). We recommend [integrated vectorization](vector-search-integrated-vectorization.md) and [query-time vectorizers](vector-search-how-to-configure-vectorizer.md) for built-in encoding.
 
@@ -270,7 +292,19 @@ For more information about new preview features, see [What's new in Azure AI Sea
 
 The fields collection must include a field for the document key, vector fields, and any other fields that you need for hybrid search scenarios.
 
-Vector fields are characterized by [their data type](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields), a `dimensions` property based on the embedding model used to output the vectors, and a vector profile.
+Vector fields are characterized by [their data type](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields), a `dimensions` property based on the embedding model used to output the vectors, and a vector profile that you created in a previous step.
+
+```json
+{
+    "name": "contentVector",
+    "type": "Collection(Edm.Single)",
+    "searchable": true,
+    "retrievable": false,
+    "stored": false,
+    "dimensions": 1536,
+    "vectorSearchProfile": "vector-profile-1"
+}
+```
 
 ### [**2024-07-01**](#tab/rest-2024-07-01)
 
@@ -284,7 +318,7 @@ Vector fields are characterized by [their data type](/rest/api/searchservice/sup
    + `dimensions` is the number of dimensions generated by the embedding model. For text-embedding-ada-002, it's fixed at 1536. For the text-embedding-3 model series, there's a range of values. If you're using integrated vectorization and an embedding skill to generate vectors, make sure this property is set to the [same dimensions value](cognitive-search-skill-azure-openai-embedding.md#supported-dimensions-by-modelname) used by the embedding skill.
    + `vectorSearchProfile` is the name of a profile defined elsewhere in the index.
    + `searchable` must be true.
-   + `retrievable` can be true or false. True returns the raw vectors (1536 of them) as plain text and consumes storage space. Set to true if you're passing a vector result to a downstream app.
+   + `retrievable` can be true or false. True returns the raw vectors (1,536 of them) as plain text and consumes storage space. Set to true if you're passing a vector result to a downstream app.
    + `stored` can be true or false. It determines whether an extra copy of vectors is stored for retrieval. For more information, see [Reduce vector size](vector-search-how-to-storage-options.md).
    + `filterable`, `facetable`, `sortable` must be false. 
 
@@ -367,8 +401,10 @@ Vector fields are characterized by [their data type](/rest/api/searchservice/sup
 
 ### [**2024-05-01-preview**](#tab/rest-2024-05-01-Preview)
 
+[**2024-05-01-preview**](/rest/api/searchservice/search-service-api-versions#2024-05-01-preview) is the most recent preview version.
+
 + Supports all [vector data types](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields).
-+ Inclusive of `2024-03-01-preview`, with new support [indexing binary data for vector search](vector-search-how-to-index-binary-data.md).
++ Inclusive of `2024-03-01-preview`.
 
 1. Use the [Create or Update Index Preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true) to define the fields collection of an index.
 
@@ -378,7 +414,7 @@ Vector fields are characterized by [their data type](/rest/api/searchservice/sup
    + `dimensions` is the number of dimensions generated by the embedding model. For text-embedding-ada-002, it's 1536.
    + `vectorSearchProfile` is the name of a profile defined elsewhere in the index.
    + `searchable` must be true.
-   + `retrievable` can be true or false. True returns the raw vectors (1536 of them) as plain text and consumes storage space. Set to true if you're passing a vector result to a downstream app. False is required if `stored` is false.
+   + `retrievable` can be true or false. True returns the raw vectors (1,536 of them) as plain text and consumes storage space. Set to true if you're passing a vector result to a downstream app. False is required if `stored` is false.
    + `stored` is a new boolean property that applies to vector fields only. True stores a copy of vectors returned in search results. False discards that copy during indexing. You can search on vectors, but can't return vectors in results.
    + `filterable`, `facetable`, `sortable` must be false. 
 
@@ -547,7 +583,7 @@ If you're familiar with indexers and skillsets:
 
 ---
 
-## Check your index for vector content
+## Query your index for vector content
 
 For validation purposes, you can query the index using Search Explorer in the Azure portal or a REST API call. Because Azure AI Search can't convert a vector to human-readable text, try to return fields from the same document that provide evidence of the match. For example, if the vector query targets the "titleVector" field, you could select "title" for the search results.
 
@@ -565,7 +601,7 @@ Fields must be attributed as "retrievable" to be included in the results.
 
   + Use the default Query view for a quick confirmation that the index contains vectors. The query view is for full text search. Although you can't use it for vector queries, you can send an empty search (`search=*`) to check for content. The content of all fields, including vector fields, is returned as plain text.
 
-  + See [Create a vector query](vector-search-how-to-query.md) for more details.
+For more information, see [Create a vector query](vector-search-how-to-query.md).
 
 ### [**REST API**](#tab/rest-check-index)
 
@@ -595,18 +631,18 @@ api-key: {{admin-api-key}}
 
 ## Update a vector store
 
-To update a vector store, modify the schema and if necessary, reload documents to populate new fields. APIs for schema updates include [Create or Update Index (REST)](/rest/api/searchservice/indexes/create-or-update), [CreateOrUpdateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createorupdateindexasync) in the Azure SDK for .NET, [create_or_update_index](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient?view=azure-python#azure-search-documents-indexes-searchindexclient-create-or-update-index&preserve-view=true) in the Azure SDK for Python, and similar methods in other Azure SDKs.
+To update a vector store, modify the schema and reload documents to populate new fields. APIs for schema updates include [Create or Update Index (REST)](/rest/api/searchservice/indexes/create-or-update), [CreateOrUpdateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createorupdateindexasync) in the Azure SDK for .NET, [create_or_update_index](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient?view=azure-python#azure-search-documents-indexes-searchindexclient-create-or-update-index&preserve-view=true) in the Azure SDK for Python, and similar methods in other Azure SDKs.
 
 The standard guidance for updating an index is covered in [Update or rebuild an index](search-howto-reindex.md). 
 
 Key points include:
 
-+ Drop and rebuild is often required for updates to and deletion of existing fields.
++ Drop and full index rebuild is often required for updates to and deletion of existing fields.
 
-+ However, you can update an existing schema with the following modifications, with no rebuild required:
++ A few modifications can be made with no rebuild requirement:
 
   + Add new fields to a fields collection.
-  + Add new vector configurations, assigned to new fields but not existing fields that have already been vectorized.
+  + Add new vector configurations, assigned to new fields but not existing fields that are already vectorized.
   + Change "retrievable" (values are true or false) on an existing field. Vector fields must be searchable and retrievable, but if you want to disable access to a vector field in situations where drop and rebuild isn't feasible, you can set retrievable to false.
 
 ## Next steps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおけるベクトルインデックスの作成方法に関する更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるベクトルインデックスの作成方法に関するドキュメントの内容を大幅に改善しています。具体的には、ベクトルストアの定義や操作手順の明確化が行われており、特にベクトルと非ベクトルフィールドの取り扱いに関する説明が充実しています。

主な変更点として、次の要素が挙げられます：
- ベクトルインデックスの概要をより包括的に説明し、ユーザーがセマンティックな類似性を持つクエリを発行できるようにするための構成要素を明確化しました。
- 記事の流れに沿った手順が示され、具体的なAPIコールの例やドキュメントペイロードを提供することで、実際の操作が行いやすくなっています。
- 「統合ベクトル化」や「クエリ時間のベクトル化」についての推奨事項が明記されており、ユーザーがそれらを利用する際のガイドラインが強化されています。
- 記事全体にわたって用語の整合性が保たれ、特に「管理面」から「コントロールプレーン」への用語統一がなされています。

この変更により、Azure AI Searchを使用する開発者やデータサイエンティストは、ベクトルインデックスの作成やクエリの実行においてより多くの情報を得て、効果的に活用できるようになります。70行以上の追加と削除により、内容が豊富になり、全体として、文章がよりわかりやすく、実践的なガイダンスを提供するよう改善されています。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -104,7 +104,7 @@ ms.custom:
 
 | Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
 |-----------------------------|------|--------------|
-| [Security update addressing information disclosure](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29063) | API | GET responses [no longer return connection strings or keys](search-api-migration.md#breaking-change-for-client-code-that-reads-connection-information). Applies to GET Skillset, GET Index, and GET Indexer. This change helps protect your Azure assets integrated with AI Search from unauthorized access. |
+| [Security update addressing information disclosure](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29063) | API | GET responses [no longer return connection strings or keys](search-api-migration.md#breaking-changes-for-client-code-that-reads-connection-information). Applies to GET Skillset, GET Index, and GET Indexer. This change helps protect your Azure assets integrated with AI Search from unauthorized access. |
 | [More storage on Basic and Standard tiers](search-limits-quotas-capacity.md#service-limits) | Infrastructure |  Basic now supports up to three partitions and three replicas. Basic and Standard (S1, S2, S3) tiers have significantly more storage per partition, at the same per-partition billing rate. Extra capacity is subject to [regional availability](search-limits-quotas-capacity.md#service-limits) and applies to new search services created after April 3, 2024. Currently, there's no in-place upgrade, so you must create a new search service to get the extra storage. |
 | [More quota for vectors](search-limits-quotas-capacity.md#vector-index-size-limits) | Infrastructure | Vector quotas are also higher on new services created after April 3, 2024 in selected regions. |
 | [Vector quantization, narrow vector data types, and a new `stored` property (preview)](vector-search-how-to-configure-compression-storage.md) | Feature | Collectively, these three features add vector compression and smarter storage options. First, *scalar quantization* reduces vector index size in memory and on disk. Second, [narrow data types](/rest/api/searchservice/supported-data-types) reduce per-field storage by storing smaller values. Third, you can use `stored` to opt-out of storing the extra copy of a vector that's used only for search results. If you don't need vectors in a query response, you can set `stored` to false to save on space. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいセキュリティアップデートに関する情報の更新"
}
```

### Explanation
この変更は、「What's New」ページ内のセキュリティアップデートに関する情報を修正しています。特に、Azure AI SearchのAPIに関する重要な変更点が明記されています。具体的には、GETリクエストの応答から接続文字列やキーが返されなくなったことが強調されています。

元の記述では「breaking change for client code that reads connection information」という表現が「breaking changes for client code that reads connection information」に修正され、文言が若干洗練されました。これは、APIの変更がクライアントコードに与える影響についての理解を深めるものです。このセキュリティアップデートは、AI Searchと統合されたAzure資産を未許可のアクセスから保護することを目的としています。

さらに、基本および標準層のストレージの増加や、ベクトルに対する新しいクォータについての情報も含まれており、ユーザーが新しい機能や制限について把握しやすくなっています。全体として、この変更はユーザーに最新のアップデート情報を提供し、APIの変更がもたらす影響を強調する重要な役割を果たしています。


