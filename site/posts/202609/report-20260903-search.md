---
date: '2026-09-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e6461f7...MicrosoftDocs:1b8d987
summary: 今回の変更では、Azure AI Searchのドキュメントが更新され、自動言語アナライザーという新機能が追加されました。このアナライザーは、各ドキュメントの言語を自動的に検出し、対応する言語アナライザーを適用します。この機能により、多言語のコンテンツを扱う際の効率が向上します。また、情報の更新や新しいセクションの追加により、最新の詳細も反映されています。特に、国際的な企業や多言語対応が求められるアプリケーションにとって、有用なアップデートとなっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e6461f7...MicrosoftDocs:1b8d987){target="_blank"}

<format>
# Highlights
今回の変更では、Azure AI Searchに関する複数のドキュメントが更新されました。主な新機能として、Blob、インデックスされたOneLake、インデックスされたSharePointの知識ソースに対応する自動言語アナライザーが追加されました。このアナライザーにより、各ドキュメントの言語が自動的に検出され、対応する言語アナライザーが適用されます。これにより、多言語のコンテンツを効果的に扱うことが可能となります。また、各日付が更新され、新しいセクションが追加されることで最新の情報が反映されています。

## New features
- 自動言語アナライザーの追加: 言語を自動で検出し、対応する言語アナライザーを適用。

## Breaking changes
- 特に大きな破壊的変更は行われていないが、新機能の導入により一部設定に変更の可能性。

## Other updates
- ドキュメントの更新: 日付や新しいセクションの追加により、情報がアップデート。
- 概要や各知識ソースに関する詳細な手順が明確化。

# Insights
Azure AI Searchのドキュメント群が更新され、特に自動言語アナライザーという新機能が注目されます。このアップデートにより、多言語環境での検索効率が格段に向上します。具体的には、各ドキュメントの言語を自動的に検出することで、ユーザーは手動でアナライザーを選ぶ必要がなく、Microsoftの適切な言語アナライザーが自動的に適用されます。これは、特に国際的な企業や多言語に対応する必要のあるアプリケーションにおいて、大きな利点となります。

また、新セクションの追加により、Azure AI Searchの機能を活用するための具体的な設定方法が詳細に説明されています。特に、言語特有のコンテンツフィールドの生成に対するインデックススキーマの設計や、言語検出による課金に関する情報が追加された点も重要です。これらの情報は、ユーザーが新機能を最適に導入し、活用するための助けとなるでしょう。

この一連のアップデートは、Azure AI Searchの利便性と機能性をさらに高めるものであり、ユーザーがより効率的にデータを管理し、検索する手助けとなります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-blob.md](#item-ac6c8a) | minor update | エージェント知識ソース用のBlobの作成に関する改善 | modified | 5 | 1 | 6 | 
| [agentic-knowledge-source-how-to-onelake.md](#item-ec7a80) | minor update | インデックス付きOneLake知識ソースの作成に関する更新 | modified | 5 | 1 | 6 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed.md](#item-fe72fc) | minor update | インデックス付きSharePoint知識ソースの作成に関する更新 | modified | 5 | 1 | 6 | 
| [agentic-knowledge-source-overview.md](#item-dcf29a) | minor update | 知識ソースに関する概要の更新 | modified | 6 | 2 | 8 | 
| [knowledge-source-language-analyzers.md](#item-698858) | new feature | 自動言語アナライザーの機能追加 | added | 37 | 0 | 37 | 
| [whats-new.md](#item-fa71b4) | minor update | 自動言語アナライザーの機能の紹介追加 | modified | 1 | 0 | 1 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-blob.md{#item-ac6c8a}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Create a Blob Knowledge Source for Agentic Retrieval
 description: Learn how to create a blob knowledge source in Azure AI Search that ingests content from Azure Blob Storage or ADLS Gen2 for agentic retrieval.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/18/2026
+ms.date: 09/02/2026
 ai-usage: ai-assisted
 ms.custom: doc-kit-assisted
 zone_pivot_groups: search-csharp-python-rest
@@ -517,6 +517,10 @@ To configure and verify private network access:
 
 [!INCLUDE [Configure private network ingestion](includes/how-tos/knowledge-source-private-network.md)]
 
+### Use automatic per-language analyzers (preview)
+
+[!INCLUDE [Configure automatic per-language analyzers](includes/how-tos/knowledge-source-language-analyzers.md)]
+
 ## Check ingestion status
 
 [!INCLUDE [Check ingestion status](includes/how-tos/knowledge-source-status.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソース用のBlobの作成に関する改善"
}
```

### Explanation
この変更は、Azure AI SearchにおけるBlob知識ソースを作成する方法に関するドキュメントを更新したものです。具体的には、日付が2026年の8月18日から2026年の9月2日に変更され、内容があらたに「言語別自動アナライザー（プレビュー）」に関するセクションが追加されました。この新しいセクションには、言語別アナライザーを設定する方法についての情報も含まれています。全体として、文書は5つの行が追加され、1行が削除されており、全体の変更は6行となっています。

## articles/search/agentic-knowledge-source-how-to-onelake.md{#item-ec7a80}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to create an indexed OneLake knowledge source that define
 ms.service: azure-ai-search
 ms.custom: [ignite-2025, doc-kit-assisted]
 ms.topic: how-to
-ms.date: 08/14/2026
+ms.date: 09/02/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
@@ -479,6 +479,10 @@ Content-Type: application/json
 > [!NOTE]
 > To enforce document-level permissions with `ingestionPermissionOptions`, use the 2026-08-01-preview API version. The 2026-04-01 API version doesn't support this feature.
 
+### Use automatic per-language analyzers (preview)
+
+[!INCLUDE [Configure automatic per-language analyzers](includes/how-tos/knowledge-source-language-analyzers.md)]
+
 ## Check ingestion status
 
 [!INCLUDE [Check ingestion status](includes/how-tos/knowledge-source-status.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス付きOneLake知識ソースの作成に関する更新"
}
```

### Explanation
この変更は、Azure AI Searchのインデックス付きOneLake知識ソースを作成する際の手順に関するドキュメントを更新しています。主な更新点は、日付が2026年の8月14日から2026年の9月2日に変更されたことと、新たに「言語別自動アナライザー（プレビュー）」に関するセクションが追加されたことです。このセクションには、言語別アナライザーを設定する方法に関する情報が含まれています。全体として、文書には5つの行が追加され、1行が削除され、合計で6行の変更が行われています。

## articles/search/agentic-knowledge-source-how-to-sharepoint-indexed.md{#item-fe72fc}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Create a SharePoint (Indexed) Knowledge Source
 description: Learn how to create an indexed SharePoint knowledge source, which ingests content from SharePoint sites into a searchable index on Azure AI Search.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/14/2026
+ms.date: 09/02/2026
 ai-usage: ai-assisted
 ms.custom: doc-kit-assisted
 zone_pivot_groups: search-csharp-python-rest
@@ -310,6 +310,10 @@ To configure and verify private access to supported Azure dependencies:
 
 [!INCLUDE [Configure private network ingestion](includes/how-tos/knowledge-source-private-network.md)]
 
+### Use automatic per-language analyzers
+
+[!INCLUDE [Configure automatic per-language analyzers](includes/how-tos/knowledge-source-language-analyzers.md)]
+
 ## Check ingestion status
 
 [!INCLUDE [Check ingestion status](includes/how-tos/knowledge-source-status.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス付きSharePoint知識ソースの作成に関する更新"
}
```

### Explanation
この変更は、インデックス付きSharePoint知識ソースを作成するための手順に関するドキュメントを更新しています。主な変更点は、日付が2026年の8月14日から2026年の9月2日に修正され、また「言語別自動アナライザー」のセクションが新たに追加されました。このセクションでは、Azure AI SearchにおいてSharePointサイトからコンテンツを検索可能なインデックスに取り込む際のアナライザー設定について述べられています。全体として、文書には5つの行が追加され、1行が削除されており、合計で6行の変更が行われています。

## articles/search/agentic-knowledge-source-overview.md{#item-dcf29a}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: What is a Knowledge Source?
 description: Learn about the knowledge source object used for agentic retrieval workloads in Azure AI Search.
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 08/14/2026
+ms.date: 09/01/2026
 ai-usage: ai-assisted
 ---
 
@@ -95,10 +95,14 @@ Don't configure `assetStore` and `ingestionPermissionOptions` on the same knowle
 
 ### Restrict ingestion to a private network (preview)
 
-Starting with the `2026-08-01-preview` API version, [blob](agentic-knowledge-source-how-to-blob.md#restrict-ingestion-to-a-private-network-preview), [indexed SharePoint](agentic-knowledge-source-how-to-sharepoint-indexed.md#protect-azure-dependencies-during-ingestion), and [indexed Azure SQL](agentic-knowledge-source-how-to-azure-sql.md#restrict-ingestion-to-a-private-network) knowledge sources support private indexer execution. For blob and Azure SQL, approved shared private links can protect the source connection and Azure dependencies. SharePoint Online isn't a shared private link target, so private mode applies only to its protected Azure dependencies.
+[Blob](agentic-knowledge-source-how-to-blob.md#restrict-ingestion-to-a-private-network-preview), [indexed SharePoint](agentic-knowledge-source-how-to-sharepoint-indexed.md#protect-azure-dependencies-during-ingestion), and [indexed Azure SQL](agentic-knowledge-source-how-to-azure-sql.md#restrict-ingestion-to-a-private-network) knowledge sources support private indexer execution. For blob and Azure SQL, approved shared private links can protect the source connection and Azure dependencies. SharePoint Online isn't a shared private link target, so private mode applies only to its protected Azure dependencies.
 
 Currently, private synchronization isn't supported for [indexed OneLake knowledge sources](agentic-knowledge-source-how-to-onelake.md#limitations).
 
+### Use automatic per-language analyzers (preview)
+
+[Blob](agentic-knowledge-source-how-to-blob.md#use-automatic-per-language-analyzers-preview), [indexed OneLake](agentic-knowledge-source-how-to-onelake.md#use-automatic-per-language-analyzers-preview), and [indexed SharePoint](agentic-knowledge-source-how-to-sharepoint-indexed.md#use-automatic-per-language-analyzers) knowledge sources support automatic per-language analyzers for multilingual content. When enabled, Azure AI Search detects each source document's language and automatically applies a matching Microsoft language analyzer. You don't specify an analyzer in the knowledge source definition or in a query.
+
 ## Using knowledge sources
 
 After you create a knowledge source, reference it in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md). The knowledge base determines which knowledge sources to query. The following sections describe options for controlling which sources are included and how the engine selects among them.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ソースに関する概要の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける知識ソースの概要を説明する文書に対する更新を示しています。主な変更内容は、日付が2026年の8月14日から2026年の9月1日に修正されたこと、そして「言語別自動アナライザー」の新しいセクションが追加された点です。この新セクションでは、複数言語のコンテンツに対応するための自動的なアナライザーの使用が説明され、Azure AI Searchが各ドキュメントの言語を自動的に検出し、それに合ったアナライザーを適用することが述べられています。文書内では、知識ソースに関する情報が明確化され、私的ネットワークへの取り込み制限についても言及されています。全体として、6行が追加され、2行が削除されており、合計で8行の変更が行われています。

## articles/search/includes/how-tos/knowledge-source-language-analyzers.md{#item-698858}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,37 @@
+---
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 09/02/2026
+ai-usage: ai-assisted
+---
+
+Starting with the `2026-08-01-preview` API version, automatic per-language analyzers are available for blob, indexed OneLake, and indexed SharePoint knowledge sources. When enabled, Azure AI Search detects each source document's language and automatically applies a matching Microsoft language analyzer. You don't specify an analyzer in the knowledge source definition or in a query.
+
+To enable automatic per-language analyzers, set `contentExtractionMode` to `minimal` and configure `ingestionParameters.aiServices` in the knowledge source definition.
+
+For keyless authentication, omit `aiServices.apiKey` and assign the **Cognitive Services User** role on your Microsoft Foundry resource to the managed identity of your search service. For key-based authentication, set `aiServices.apiKey` to a valid key for your Foundry resource.
+
+The following languages are supported:
+
++ English
++ Japanese
++ French
++ Spanish
++ German
++ Dutch
++ Italian
++ Brazilian Portuguese
++ European Portuguese
++ Simplified Chinese
++ Traditional Chinese
++ Korean
+
+For multilingual content, Azure AI Search selects an analyzer based on the predominant detected language. It uses the standard analyzer when the language is unsupported or uncertain.
+
+When you enable automatic per-language analyzers, Azure AI Search adds language-specific content fields for every supported language to the generated index schema, whether or not your data contains documents in those languages. During ingestion, documents are routed to the appropriate language-specific field based on their detected language.
+
+Unused language fields don't contain indexed content and have minimal storage impact, but they remain part of the index schema and count toward the index field limit. Consider the additional fields when you plan your index design, field count, and storage requirements. For more information, see [Index limits](../../search-limits-quotas-capacity.md#index-limits) and [Estimate and manage capacity of a search service](../../search-capacity-planning.md).
+
+Language detection is billable after the free AI enrichment allocation. For more information, see [Free enrichments](../../cognitive-search-attach-cognitive-services.md#free-enrichments).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "自動言語アナライザーの機能追加"
}
```

### Explanation
この変更は、Azure AI Searchにおける自動言語アナライザーの機能に関する新しい文書を追加しています。この文書では、2026年の8月1日以降のAPIバージョンから利用可能な自動言語アナライザーについて詳細に説明しています。自動言語アナライザーが有効になると、Azure AI Searchは各ソースドキュメントの言語を検出し、対応するMicrosoftの言語アナライザーを自動的に適用します。

自動言語アナライザーを有効にするための設定方法、言語のサポート一覧、そしてマルチ言語コンテンツに対する動作についても記載されています。また、言語特有のコンテンツフィールドが生成される際のインデックススキーマの設計に関する考慮点や、言語検出が請求対象となる説明もあります。この文書は37行の新しい内容が追加され、ドキュメントの整合性と利便性を向上させています。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -30,6 +30,7 @@ Learn about the latest updates to Azure AI Search functionality, documentation,
 |--|--|
 | [Search Service 2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) | New preview REST API version providing programmatic access to the data plane operations described in this table. |
 | [Private network support for indexed knowledge sources (preview)](agentic-knowledge-source-overview.md#restrict-ingestion-to-a-private-network-preview) | Blob, indexed SharePoint, and indexed Azure SQL knowledge sources now support private network ingestion through the generated indexer. |
+| [Automatic per-language analyzers for indexed knowledge sources (preview)](agentic-knowledge-source-overview.md#use-automatic-per-language-analyzers-preview) | Blob, indexed OneLake, and indexed SharePoint knowledge sources can now use automatic per-language analyzers to detect each source document's language and apply a matching Microsoft language analyzer. |
 | [File knowledge source updates (preview)](agentic-knowledge-source-how-to-file.md) | File knowledge sources add the following capabilities:<p><ul><li>Support for Serverless search services.</li><li>Higher limits of 200 files (up from 100) and 100 MB per file on Serverless and Dedicated tiers above Free and Basic.</li><li>A multipart upload operation that accepts custom metadata.</li><li>An update operation that replaces file content.</li><li>A list operation that supports filtering by path or file name.</li><li>CORS configuration for the upload, list, update, and delete operations.</li></ul> |
 | [Work IQ knowledge source custom Microsoft Entra app (preview)](agentic-knowledge-source-how-to-work-iq.md) | Work IQ knowledge sources now use a customer-owned Microsoft Entra app and federated credential for on-behalf-of (OBO) access. This authentication model replaces preview feature registration and separate access requests. |
 | [Knowledge base expanded model support (preview)](agentic-retrieval-how-to-create-knowledge-base.md#supported-models) | Knowledge bases now support `gpt-5.5` and the `gpt-5.6` model family (`gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna`) for query planning and answer generation. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "自動言語アナライザーの機能の紹介追加"
}
```

### Explanation
この変更は、「Azure AI Search」の最新機能や更新に関する文書の更新を示しています。新たに追加された内容は、「インデックスされた知識ソースの自動言語アナライザー（プレビュー）」に関する情報です。この機能では、Blob、インデックスされたOneLake、およびインデックスされたSharePointの知識ソースが利用可能になり、各ソースドキュメントの言語を検出し、それに対応するMicrosoftの言語アナライザーを自動的に適用することが可能となります。

変更はテーブルの1行の追加にとどまり、Azure AI Searchの機能の幅を広げる重要な情報が提供されています。このアップデートにより、ユーザーは新機能をより理解し、活用しやすくなります。


