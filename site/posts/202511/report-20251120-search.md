---
date: '2025-11-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:877b82c...MicrosoftDocs:05b2bb7
summary: このドキュメント更新は、Azure AI Searchに関する技術文書のマイナーな変更をまとめています。主な改良点として、REST APIリンクの修正、新しいAPI機能の紹介、権限管理の明確化が挙げられ、ユーザー体験と文書の正確性が向上しています。最新のAPI情報が追加され、セキュリティ機能についての詳細が記載されました。破壊的変更はありませんが、APIエンドポイントのURL修正により古い形式使用時にエラーの可能性があるため注意が必要です。この更新は、技術改善とユーザビリティ向上の努力を反映しており、特にリンク修正や地域サポート情報のアップデートがユーザーの計画に役立つ重要な要素となっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:877b82c...MicrosoftDocs:05b2bb7){target="_blank"}

<format>
# ハイライト
このドキュメント更新は、Azure AI Searchに関するさまざまな技術文書におけるマイナーな変更をまとめています。主に、REST APIリンクの修正、利用可能な新たなAPI機能の紹介、権限管理の明確化が行われ、ユーザー体験の向上とドキュメントの正確性の向上を図っています。

## 新機能
- 複数のページにおいて、最新のAPIバージョンやクライアントライブラリバージョン情報が追加されました。
- Azure AI Searchの文書において、新しいセキュリティ機能と権限設定に関する誤解を避けるための詳細情報が記載されました。

## 破壊的変更
- 明示的な破壊的変更は含まれていませんが、APIのエンドポイントURLの修正により、ユーザーが古い形式を使用するとエラーの可能性があります。

## その他の更新
- 一貫性を保つために複数のAPIリンクのパスが修正されました。
- 検索サービスのキャパシティ変更に際する操作性改善とその制約に関する情報の強化を行いました。
- 地域サポートとセマンティックランカーの利用可能性に関する情報がアップデートされています。

# インサイト
この一連の更新は、継続的な技術改善およびユーザビリティ向上への努力を反映しています。特に、APIおよびSDKの使用において頻繁に発生する問題に対処するためのリンク修正が目を引きます。`/knowledgebases/`から`/knowledge-bases/`への修正は、ユーザーが正確な情報を迅速に取得し、実装作業を円滑に行うため、不可欠な改善です。

さらに、Microsoft Purviewの感度ラベル機能に関連する情報更新は、データセキュリティとコンプライアンスの強化を目指しており、Azure AI Searchの使用が企業のセキュリティ基準に合致しやすくします。

また、リージョンサポートのセクション更新は、ユーザーがサービス利用を計画する際に、誤った仮定や混乱を防ぐために重要です。地域ごとの具体的な制約も考慮に入れた情報提供により、ユーザーはAzure AI Searchをより適切に利用し、効率的な計画を立てることができるでしょう。

これら全体を通して、Azure AI Searchの技術文書は、より現実の開発環境に即した、実用的で価値あるリソースとなることを目指しています。

</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-overview.md](#item-dcf29a) | minor update | エージェント知識ソースの概要に関する文書の更新 | modified | 9 | 11 | 20 | 
| [agentic-retrieval-how-to-answer-synthesis.md](#item-f44e99) | minor update | エージェントリトリーバルの回答合成に関する文書の更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-how-to-migrate.md](#item-9653ea) | minor update | エージェントリトリーバルの移行に関する文書の更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-how-to-set-retrieval-reasoning-effort.md](#item-141e97) | minor update | エージェントリトリーバルの推論努力設定に関する文書の更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-blob-python.md](#item-029d03) | minor update | エージェント情報源に関するPython文書の更新 | modified | 6 | 1 | 7 | 
| [agentic-knowledge-source-how-to-blob-rest.md](#item-b5ce57) | minor update | エージェント情報源に関するREST文書の更新 | modified | 5 | 0 | 5 | 
| [agentic-knowledge-source-how-to-onelake-python.md](#item-c7d61d) | minor update | OneLakeに関するPython文書の更新 | modified | 2 | 0 | 2 | 
| [agentic-knowledge-source-how-to-onelake-rest.md](#item-876f49) | minor update | OneLakeに関するREST文書の更新 | modified | 2 | 0 | 2 | 
| [agentic-knowledge-source-how-to-search-index-python.md](#item-58056f) | minor update | Pythonでの検索インデックスに関する文書の更新 | modified | 2 | 0 | 2 | 
| [agentic-knowledge-source-how-to-search-index-rest.md](#item-e95367) | minor update | RESTによる検索インデックスに関する文書の更新 | modified | 2 | 0 | 2 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-python.md](#item-923abb) | minor update | SharePointのインデックスに関する文書の更新 | modified | 2 | 0 | 2 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-rest.md](#item-e26ea0) | minor update | SharePointインデックス化に関するREST APIの文書更新 | modified | 2 | 0 | 2 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-python.md](#item-822712) | minor update | SharePointリモートアクセスに関するPython文書の更新 | modified | 2 | 2 | 4 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-rest.md](#item-5514b1) | minor update | SharePointリモートREST APIに関する文書の更新 | modified | 2 | 0 | 2 | 
| [agentic-knowledge-source-how-to-web-python.md](#item-72b59c) | minor update | Web知識ソースに関するPython文書の更新 | modified | 2 | 0 | 2 | 
| [agentic-knowledge-source-how-to-web-rest.md](#item-649608) | minor update | Web知識ソースに関するREST API文書の更新 | modified | 2 | 0 | 2 | 
| [agentic-retrieval-how-to-create-knowledge-base-python.md](#item-4e498f) | minor update | Pythonによる知識ベース作成に関する文書の更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-how-to-create-knowledge-base-rest.md](#item-37851c) | minor update | REST API文書の知識ベースのリンク修正 | modified | 1 | 1 | 2 | 
| [knowledge-source-delete-python.md](#item-bf68d8) | minor update | Pythonによるナレッジソース削除文書のリンク修正 | modified | 1 | 1 | 2 | 
| [knowledge-source-delete-rest.md](#item-225321) | minor update | RESTによるナレッジソース削除文書のリンク修正 | modified | 1 | 1 | 2 | 
| [search-blob-indexer-role-based-access.md](#item-887e42) | minor update | BlobインデクサーにおけるRBACスコープのメタデータの取り込み改善 | modified | 64 | 11 | 75 | 
| [search-capacity-planning.md](#item-0dd6c9) | minor update | 検索サービスのキャパシティ計画に関する運用の詳細変更 | modified | 7 | 3 | 10 | 
| [search-document-level-access-overview.md](#item-4bb055) | minor update | ドキュメントレベルアクセス制御に関する情報の更新 | modified | 5 | 7 | 12 | 
| [search-indexer-access-control-lists-and-role-based-access.md](#item-67b42f) | minor update | インデクサーとアクセス制御リストに関する情報の更新 | modified | 72 | 15 | 87 | 
| [search-query-sensitivity-labels.md](#item-3e1f8a) | minor update | クエリ時の感度ラベルの強制に関する情報の更新 | modified | 3 | 1 | 4 | 
| [search-region-support.md](#item-25b0f1) | minor update | Azure AI Searchのリージョンサポートに関する情報の更新 | modified | 17 | 15 | 32 | 


# Modified Contents
## articles/search/agentic-knowledge-source-overview.md{#item-dcf29a}

<details>
<summary>Diff</summary>
````diff
@@ -32,17 +32,16 @@ Make sure you have at least one knowledge source before creating a knowledge bas
 
 + A knowledge source, its index, and the knowledge base must all exist on the same search service. External content is either accessed over the public internet (Bing) or in a Microsoft tenant (remote SharePoint).
 
-<!-- Update the REST API links for all knowledge sources -->
 ## Supported knowledge sources
 
 Here are the knowledge sources you can create in this preview:
 
-+ [`"searchIndex"` API](/rest/api/searchservice/knowledge-sources/create-or-update#searchindexknowledgesource?view=rest-searchservice-2025-11-01-preview&preserve-view=true) wraps an existing index.
-+ [`"azureBlob"` API](/rest/api/searchservice/knowledge-sources/create-or-update#azureblobknowledgesource?view=rest-searchservice-2025-11-01-preview&preserve-view=true) generates an indexer pipeline that pulls from a blob container.
-+ [`"indexedOneLake"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) generates an indexer pipeline that pulls from a lakehouse.
-+ [`"indexedSharePoint"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) generates an indexer pipeline that pulls from a SharePoint site.
-+ [`"remoteSharePoint"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) retrieves content directly from SharePoint.
-+ [`"webParameters"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) retrieves real-time grounding data from Microsoft Bing.
++ [`"searchIndex"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#searchindexknowledgesource) wraps an existing index.
++ [`"azureBlob"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#azureblobknowledgesource) generates an indexer pipeline that pulls from a blob container.
++ [`"indexedOneLake"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#indexedonelakeknowledgesource) generates an indexer pipeline that pulls from a lakehouse.
++ [`"indexedSharePoint"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#indexedsharepointknowledgesource) generates an indexer pipeline that pulls from a SharePoint site.
++ [`"remoteSharePoint"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#remotesharepointknowledgesource) retrieves content directly from SharePoint.
++ [`"webParameters"` API](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#webknowledgesource) retrieves real-time grounding data from Microsoft Bing.
 
 ## Creating knowledge sources
 
@@ -59,16 +58,15 @@ You can use the REST API or an Azure SDK preview package to create a knowledge s
 
 After the knowledge source is created, you can reference it in a knowledge base.
 
-<!-- Fix bookmark links to REST API section once docs are staged -->
 ## Using knowledge sources
 
 Properties on the [*knowledge base*](agentic-retrieval-how-to-create-knowledge-base.md) determine which knowledge sources are used.
 
-+ ["knowledgeSources" REST](/rest/api/searchservice/knowledgebases/create-or-update#knowledgesourcereference?view=rest-searchservice-2025-11-01-preview&preserve-view=true) array specifies the knowledge sources available to the knowledge base.
++ ["knowledgeSources" REST](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#knowledgesourcereference) array specifies the knowledge sources available to the knowledge base.
 
-+ ["retrievalReasoningEffort" REST](/rest/api/searchservice/knowledgebases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) properties determine the amount of effort put into a retrieval. For more information, see [Set the retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md).
++ ["retrievalReasoningEffort" REST](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#knowledgeretrievalreasoningeffortkind) properties determine the amount of effort put into a retrieval. For more information, see [Set the retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md).
 
-+ ["outputMode" REST](/rest/api/searchservice/knowledgebases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) affects query output and what goes in the response.
++ ["outputMode" REST](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true#knowledgeretrievaloutputmode) affects query output and what goes in the response.
 
 The knowledge base uses the [retrieve action](agentic-retrieval-how-to-retrieve.md) to send queries to the index specified in the knowledge source. In the retrieve action, some knowledge base and source defaults can be overridden at retrieval time.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースの概要に関する文書の更新"
}
```

### Explanation
この変更では、`articles/search/agentic-knowledge-source-overview.md`という文書に対して、いくつかのマイナーな更新が行われました。主に、リンクの修正と情報の明確化が含まれており、内容の全体的な理解を向上させることを目的としています。

具体的には、新たに知識ソースに関するAPIリンクが追加され、既存のリンクが更新されました。これにより、それぞれのエンドポイントに直接アクセスする際の利便性が向上しています。また、REST APIのセクションへの参照がより正確で明確になるように修正されています。

この更新によって、ユーザーが知識ベースを作成する際に必要な情報が、よりスムーズに得られるようになりました。特に、外部コンテンツを参照する方法や利用可能な知識ソースのタイプについての記述が強化されています。全体として、ドキュメントはより使いやすく、分かりやすくなっています。

## articles/search/agentic-retrieval-how-to-answer-synthesis.md{#item-f44e99}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ This section explains how to enable answer synthesis on an existing knowledge ba
 
 To enable answer synthesis on a knowledge base:
 
-1. Use the 2025-11-01-preview of [Knowledge Base - Create or Update (REST API)](/rest/api/searchservice/knowledgebases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to formulate the request.
+1. Use the 2025-11-01-preview of [Knowledge Base - Create or Update (REST API)](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to formulate the request.
 
 1. In the body of the request, set `outputMode` to `answerSynthesis`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルの回答合成に関する文書の更新"
}
```

### Explanation
この変更では、`articles/search/agentic-retrieval-how-to-answer-synthesis.md`という文書に対して、マイナーな更新が行われました。具体的には、REST APIのリンクに関する表記の修正が行われ、正確性が向上しています。

具体的には、以下の点が修正されました：
- ステップ1の指示に含まれるREST APIのリンクのパスが、`knowledgebases`から`knowledge-bases`に変更されました。この微調整により、ユーザーが正確なエンドポイントにアクセスしやすくなりました。

全体として、この修正は文書の明確さを向上させており、エンドユーザーが知識ベースに対する回答合成を有効にする際の手順をより理解しやすくしています。

## articles/search/agentic-retrieval-how-to-migrate.md{#item-9653ea}

<details>
<summary>Diff</summary>
````diff
@@ -353,7 +353,7 @@ The response includes the full definition of the new object. For more informatio
     }
     ```
 
-1. Formulate a [Create Knowledge Base](/rest/api/searchservice/knowledgebases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) request as the basis for your migration.
+1. Formulate a [Create Knowledge Base](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) request as the basis for your migration.
 
     Start with the 08-01-preview JSON.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルの移行に関する文書の更新"
}
```

### Explanation
この変更では、`articles/search/agentic-retrieval-how-to-migrate.md`という文書に対して、マイナーな更新が行われました。主な修正内容は、REST APIのリンクに関する文言の変更です。

具体的には、以下のポイントが修正されています：
- ステップ1の指示に含まれるREST APIのリンクにて、`knowledgebases`という表記から`knowledge-bases`に修正されました。この変更により、ユーザーが正確なエンドポイントにアクセスしやすくなり、混乱を避けることができます。

この更新によって、マイグレーションに関する手順が明確になり、利用者が新しい知識ベースを作成するための正しい情報を得ることができるようになっています。全体として、文書の精度と使いやすさが向上しています。

## articles/search/agentic-retrieval-how-to-set-retrieval-reasoning-effort.md{#item-141e97}

<details>
<summary>Diff</summary>
````diff
@@ -38,7 +38,7 @@ Levels of reasoning effort include:
 
 To establish the default behavior, set the property in the knowledge base.
 
-1. Use [Create or Update Knowledge Base](/rest/api/searchservice/knowledgebases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to set the `retrievalReasoningEffort`.
+1. Use [Create or Update Knowledge Base](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to set the `retrievalReasoningEffort`.
 
 1. Add the `retrievalReasoningEffort` property. The following JSON shows the syntax. For more information about knowledge bases, see [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルの推論努力設定に関する文書の更新"
}
```

### Explanation
この変更では、`articles/search/agentic-retrieval-how-to-set-retrieval-reasoning-effort.md`という文書に対して、マイナーな更新が行われました。主に、REST APIのリンクに関連する表記の修正です。

具体的には、以下の点が修正されました：
- ステップ1の指示に含まれているREST APIのリンクが、`knowledgebases`から`knowledge-bases`に変更されました。この修正により、ユーザーが正確なエンドポイントにアクセスできるようになり、手順の明確性が向上しました。

この修正によって、知識ベースの推論努力を設定する方法がより理解しやすくなり、利用者が必要な情報を正確に把握できるようになります。全体的に見て、文書の信頼性と有用性が向上しています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-python.md{#item-029d03}

<details>
<summary>Diff</summary>
````diff
@@ -18,16 +18,21 @@ Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-s
 + An index that stores enriched content and meets the criteria for agentic retrieval.
 + An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
 
+> [!NOTE]
+> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](/azure/search/search-indexer-access-control-lists-and-role-based-access) or [Blob RBAC scopes](/azure/search/search-blob-indexer-role-based-access).
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
 
-+ An [Azure Blob Storage](/azure/storage/common/storage-account-create) or [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/create-data-lake-storage-account) account.
++ An [Azure Blob Storage](/azure/storage/common/storage-account-create) or [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/create-data-lake-storage-account) account. 
 
 + A blob container with [supported content types](../../search-how-to-index-azure-blob-storage.md#supported-document-formats) for text content. For optional image verbalization, the supported content type depends on whether your chat completion model can analyze and describe the image file.
 
 + The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
 
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
+
 > [!NOTE]
 > Although you can use the Azure portal to create blob knowledge sources, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](../../agentic-retrieval-how-to-migrate.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント情報源に関するPython文書の更新"
}
```

### Explanation
このコードの変更は、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-python.md`という文書に対するマイナーな更新を示しています。主な変更点は、Azure AI Searchに関連する事前条件と注意点の追加です。

具体的には、以下の内容が更新されました：
- エージェントリトリーバルに関する情報を補完するため、許可メタデータやリソースへのアクセス制御の重要性に関する説明が追加されました。
- サポートされるコンテンツタイプや、最新の`azure-search-documents`クライアントライブラリのバージョンに関する具体的な情報が追加され、ユーザーが必要な前提条件を理解しやすくなっています。
- Azureポータルを使用してエージェント情報源を作成する際の注意点も補足され、2025年08月版の用語に関する情報が明示されています。

この更新により、ユーザーがAzure AI Search環境を適切にセットアップし、関連するアクションを実行するための手順がよりわかりやすくなりました。全体として、文書は利用者にとって役立つ情報が増強され、精度が向上しています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-rest.md{#item-b5ce57}

<details>
<summary>Diff</summary>
````diff
@@ -18,6 +18,9 @@ Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-s
 + An index that stores enriched content and meets the criteria for agentic retrieval.
 + An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
 
+> [!NOTE]
+> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](/azure/search/search-indexer-access-control-lists-and-role-based-access) or [Blob RBAC scopes](/azure/search/search-blob-indexer-role-based-access).
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
@@ -28,6 +31,8 @@ Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-s
 
 + The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
 
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
+
 > [!NOTE]
 > Although you can use the Azure portal to create blob knowledge sources, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](../../agentic-retrieval-how-to-migrate.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント情報源に関するREST文書の更新"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-rest.md`という文書に対するマイナーな更新を示しています。主に、Azure AI Searchのエージェント情報源に関する手順と注意点を明確にするための情報が追加されました。

具体的には、以下の内容が更新されました：
- エージェントリトリーバルに関連する情報として、許可メタデータについての説明が追加され、Azure Storageでのユーザーアクセスの重要性が強調されました。これにより、ユーザーはインデックス化されたコンテンツに対して必要な権限を理解する助けになります。
- 文書の事前条件部分に、Azure AI Searchの特定のバージョンや、オブジェクトを作成および使用するための権限に関する情報が追加されました。これにより、ユーザーが必要なセットアップや前提条件をより明確に把握できるようになります。
- 最後に、AzureポータルでのBlob情報源の作成に関する注意事項が追加され、相違点やサポートされていない機能に関する情報が提供されています。

この更新によって、文書は具体的で有用な情報が増え、ユーザーの理解を助ける内容となっています。全体的に、Azure AI Searchにおけるエージェント情報源に関連した運用のガイドラインが強化されました。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-python.md{#item-c7d61d}

<details>
<summary>Diff</summary>
````diff
@@ -30,6 +30,8 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 
 + The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
 
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
+
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources using Python](knowledge-source-check-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLakeに関するPython文書の更新"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-python.md`という文書に関するマイナーな更新を示しています。主に、Azure AI SearchのOneLakeインデクサーに関連する情報が追加されました。

具体的には、以下の内容が更新されました：
- 最新のプレビュー版である[`azure-search-documents`クライアントライブラリ](https://pypi.org/project/azure-search-documents/11.7.0b2/)に関する情報が追加され、ユーザーが適切なバージョンのライブラリを使用できるようになりました。
- Azure AI Searchでオブジェクトを作成し使用するための権限に関する情報も追加されました。これには、役割ベースのアクセス制御を推奨し、役割の割り当てが難しい場合にはAPIキーを使用できることが明記されています。

この更新によって、文書は特定の技術的要件についてさらに明確なガイダンスを提供し、ユーザーがOneLakeインデクサーを効果的に利用できるよう支援しています。全体的に、Azure AI Searchの利用に向けた知識源の取り扱いに関する理解が深まります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-rest.md{#item-876f49}

<details>
<summary>Diff</summary>
````diff
@@ -30,6 +30,8 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 
 + The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
 
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
+
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources using REST](knowledge-source-check-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLakeに関するREST文書の更新"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-rest.md`という文書に対するマイナーな更新を示しています。主に、Azure AI SearchのOneLakeインデクサーに関する情報が追加されました。

具体的な変更内容は以下の通りです：
- Azure Search Service REST APIの[2025-11-01-preview](https://rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true)バージョンに関する情報が追加され、最新のAPI仕様を参照できるようになりました。
- Azure AI Searchでオブジェクトを作成および使用するための権限に関する内容が追加されました。役割ベースのアクセス制御を推奨し、役割の割り当てが難しい場合にはAPIキーを利用することが可能であることが明記されています。

この更新により、文書は特定のAPIバージョンに関する重要な情報や権限に関するガイダンスを提供し、OneLakeインデクサーの利用における理解を深めるのに役立ちます。全体的に、Azure AI Searchの操作に関するユーザーのサポートが強化されています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-python.md{#item-58056f}

<details>
<summary>Diff</summary>
````diff
@@ -19,6 +19,8 @@ A *search index knowledge source* specifies a connection to an Azure AI Search i
 
 + The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
 
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
+
 > [!NOTE]
 > Although you can use the Azure portal to create search index knowledge sources, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](../../agentic-retrieval-how-to-migrate.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonでの検索インデックスに関する文書の更新"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-python.md`という文書に対するマイナーな更新を含んでいます。主に、Azure AI Searchの検索インデックスに関連する情報を最新のものに更新しています。

具体的には、以下の内容が追加されました：
- 最新のプレビュー版である[`azure-search-documents`クライアントライブラリ](https://pypi.org/project/azure-search-documents/11.7.0b2/)に関する情報が追加され、Pythonユーザーが必要なライブラリのバージョンを知ることができるようになりました。
- Azure AI Searchでオブジェクトを作成および使用するための権限に関する情報が追加されました。役割ベースのアクセス制御を推奨し、役割の割り当てが困難な場合にはAPIキーを使用できることが明記されています。また、文書にはAzureポータルの制限についても言及されており、ポータルは2025-08-01-previewを使用することがあり、これは以前の「知識エージェント」という用語を使用しており、2025-11-01-previewのすべての機能をサポートしていないことが記載されています。

この更新により、Azure AI Searchの機能や使用方法についての理解を深め、ユーザーが必要なリソースやアクセス権限を適切に管理するための手助けとなります。全体として、文書は最新の情報を反映し、より効果的にAzure AI Searchを利用できるようにしています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-rest.md{#item-e95367}

<details>
<summary>Diff</summary>
````diff
@@ -19,6 +19,8 @@ A *search index knowledge source* specifies a connection to an Azure AI Search i
 
 + The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
 
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
+
 > [!NOTE]
 > Although you can use the Azure portal to create search index knowledge sources, the portal uses the 2025-08-01-preview, which uses the previous "knowledge agent" terminology and doesn't support all 2025-11-01-preview features. For help with breaking changes, see [Migrate your agentic retrieval code](../../agentic-retrieval-how-to-migrate.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTによる検索インデックスに関する文書の更新"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-rest.md`という文書に対するマイナーな更新を示しています。主な焦点は、Azure AI Searchの検索インデクサーに関する情報が更新され、最新のAPI技術を含めることです。

具体的な変更内容は以下の通りです：
- Azure Search Service REST APIの[2025-11-01-preview](https://rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true)バージョンについての情報が追加され、ユーザーがどのバージョンを用いるべきかを理解できるようになりました。
- Azure AI Searchでオブジェクトの作成と使用のための権限に関する情報が追加され、役割ベースのアクセス制御が推奨されています。役割の割り当てが難しい場合にはAPIキーを使用できることが記載されています。また、Azureポータルを使用して検索インデックス知識ソースを作成する場合の注意点も強調されています。このポータルは古い「知識エージェント」という用語を使用しており、最新の機能をサポートしていないことが明記されています。

この更新により、文書は最新の技術情報を反映し、Azure AI Searchの利用についてユーザーに必要な指導とアドバイスを提供します。全体として、ユーザーがシステムを効果的に使用し、進化するAPIバージョンに適応できるようサポートしています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-python.md{#item-923abb}

<details>
<summary>Diff</summary>
````diff
@@ -32,6 +32,8 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
 
 + The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
 
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
+
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources using Python](knowledge-source-check-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointのインデックスに関する文書の更新"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-python.md`という文書のマイナーな更新を示しています。主に、Azure AI Searchを利用してインデックス化されたSharePointの知識ソースに関する情報が更新されています。

具体的には、以下の内容が追加されました：
- 最新のプレビュー版である[`azure-search-documents`クライアントライブラリ](https://pypi.org/project/azure-search-documents/11.7.0b2/)に関する情報が含まれ、Pythonを使用するユーザーが最新のライブラリのバージョンを知っているべきことが示されています。
- Azure AI Searchでオブジェクトを作成し使用するための権限に関する説明も追加され、役割ベースのアクセス制御が推奨されている一方で、役割の割り当てが実現できない場合にはAPIキーの使用が可能であることが示されています。また、Azure Searchサービスへの接続方法に関するリンクも提供されています。

これにより、ユーザーは最新の情報を元に、効果的にSharePointのインデックス化を行うための参考とすることができます。全体として、文書はAzure AI Searchを利用しやすくし、利用者が必要なリソースと権限について理解を深めるための支援を行っています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-rest.md{#item-e26ea0}

<details>
<summary>Diff</summary>
````diff
@@ -32,6 +32,8 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
 
 + The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
 
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
+
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources using REST](knowledge-source-check-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointインデックス化に関するREST APIの文書更新"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-rest.md`という文書に対するマイナーな更新を示しています。主に、SharePointをインデックス化するためのREST APIに関連する最新情報が追加されています。

具体的な変更内容は以下の通りです：
- Search Service REST APIの[2025-11-01-preview](https://rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true)バージョンに関する情報が加えられ、将来的な更新や使用方法についての知識が提供されています。
- Azure AI Searchでオブジェクトを作成し使用するための権限に関する詳細も追加されており、役割ベースのアクセス制御が推奨されていることが強調されています。役割の割り当てが異常な場合にはAPIキーを使用できる選択肢が示されています。また、Azure Searchサービスへの接続に関する情報を得られるリンクも提供されています。

これにより、ユーザーは最新のREST API仕様と必要な権限を理解し、SharePointのインデックス化作業をより円滑に進められるようになります。全体として、文書は利用者がAzure AI Searchを効果的に活用するための重要な情報を強化しており、使いやすさを向上させています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-python.md{#item-822712}

<details>
<summary>Diff</summary>
````diff
@@ -31,9 +31,9 @@ Like any other knowledge source, you specify a remote SharePoint knowledge sourc
 
 + The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
 
-For local development, the agentic retrieval engine uses your access token to call SharePoint on your behalf. For more information about using a personal access token on requests, see [Connect to Azure AI Search](../../search-get-started-rbac.md).
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible.
 
-<!-- invalid filter expression will return a 400 soon, so we should be able to remove this limitation -->
+For local development, the agentic retrieval engine uses your access token to call SharePoint on your behalf. For more information about using a personal access token on requests, see [Connect to Azure AI Search](../../search-get-started-rbac.md).
 
 ## Limitations
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointリモートアクセスに関するPython文書の更新"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-python.md`という文書のマイナーな更新を反映しています。主に、SharePointリモートアクセスを行うためのPythonクライアントライブラリやアクセス権限に関する情報が追加および変更されています。

具体的な変更内容は以下の通りです：
- 最新のプレビュー版の[`azure-search-documents`クライアントライブラリ](https://pypi.org/project/azure-search-documents/11.7.0b2/)に関する情報が追加され、ユーザーがこのライブラリの最新バージョンを利用できるようにしています。
- Azure AI Searchでオブジェクトを作成し使用するための権限についての説明が更新され、役割ベースのアクセス制御が推奨される一方で、役割の割り当てが不可能な場合にはAPIキーを使用できることが強調されています。
- 元々記載されていた一部の文が入れ替えられ、エンジンのローカル開発時にアクセス・トークンを使用する際の情報が明確にされています。

この更新によって、ユーザーはAzure AI SearchとSharePointの連携に関する最新のベストプラクティスを理解し、適切にAPIやトークンを用いるためのガイダンスが提供されることになっています。全体として、文書はユーザーがより効果的に技術を利用できるようサポートしています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-rest.md{#item-5514b1}

<details>
<summary>Diff</summary>
````diff
@@ -31,6 +31,8 @@ Like any other knowledge source, you specify a remote SharePoint knowledge sourc
 
 + The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
 
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible.
+
 For local development, the agentic retrieval engine uses your access token to call SharePoint on your behalf. For more information about using a personal access token on requests, see [Connect to Azure AI Search](../../search-get-started-rbac.md).
 
 <!-- invalid filter expression will return a 400 soon, so we should be able to remove this limitation -->
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointリモートREST APIに関する文書の更新"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-rest.md`という文書に対するマイナーな更新を表しています。主に、SharePointリモートアクセスに関するREST APIの最新情報とアクセス権限に関する内容が追加されています。

具体的な変更内容は以下の通りです：
- Search Service REST APIの[2025-11-01-preview](https://rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true)バージョンに関する記述が追加されており、利用者は最新のAPI仕様を理解することができます。
- Azure AI Searchでオブジェクトを作成し使用するための権限についての説明が強化されており、役割ベースのアクセス制御が推奨される一方で、役割の割り当てが困難な場合にはAPIキーを使用できることが強調されています。
- ローカル開発時にエンジンがアクセス・トークンを使用してSharePointを呼び出す方法に関する情報が保持され、パーソナルアクセス・トークンを使用するためのガイダンスが示されています。

今回の更新により、ユーザーはAzure AI Searchの使用において、最新のAPIと適切なアクセス権の設定についてより理解を深めることができるようになります。これにより、文書は技術的に適切なアプローチを促進し、ユーザーが具体的なシナリオでの利用をスムーズに行えるようサポートしています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-python.md{#item-72b59c}

<details>
<summary>Diff</summary>
````diff
@@ -38,6 +38,8 @@ When you use Web Knowledge Source, keep the following in mind:
 
 + The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
 
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
+
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources using Python](knowledge-source-check-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Web知識ソースに関するPython文書の更新"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-python.md`という文書のマイナーな更新を反映しています。主に、Web知識ソースの使用に関する最新情報とアクセス権限についての説明が追加されています。

具体的な変更内容は以下の通りです：
- 最新のプレビュー版の[`azure-search-documents`クライアントライブラリ](https://pypi.org/project/azure-search-documents/11.7.0b2/)に関する情報が追加され、ユーザーはライブラリの最新バージョンを利用することが奨励されています。
- Azure AI Searchでオブジェクトを作成し使用するための権限についての説明が強化されています。役割に基づくアクセス制御が推奨されつつ、役割の割り当てが困難な場合にはAPIキーの使用が可能であることが明示されています。さらに、検索サービスに接続するための詳細な情報もリンクされています。
- 既存の知識ソースを確認するセクションが追加されており、Pythonを使用した知識ソースの確認方法のヘルプが提供されています。

この更新により、ユーザーはWeb知識ソースを使用する際の最新のベストプラクティスと技術的なガイダンスを得ることができます。文書は、ユーザーがAzure AI Searchを利用する際に必要な情報を効果的に提供し、技術的なアプローチをサポートしています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-rest.md{#item-649608}

<details>
<summary>Diff</summary>
````diff
@@ -38,6 +38,8 @@ When you use Web Knowledge Source, keep the following in mind:
 
 + The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
 
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
+
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources using REST](knowledge-source-check-rest.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Web知識ソースに関するREST API文書の更新"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-rest.md`という文書のマイナーな更新を示しています。主な内容は、Web知識ソースの利用に関する最新情報とアクセス権の取り扱いについての記述を強化することです。

具体的な変更内容は以下の通りです：
- Search Service REST APIの[2025-11-01-preview](https://rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true)バージョンに関する情報が追加され、利用者が最新のAPI情報にアクセスできるようになっています。
- Azure AI Search上でオブジェクトを作成および使用するための権限について詳細が強化され、役割に基づくアクセスが推奨されていますが、役割の割り当てが不可能な場合にはAPIキーの使用が許可されることが記されています。また、検索サービスへの接続に関する詳細情報へのリンクも提供されています。
- 既存の知識ソースをRESTを使って確認する方法に関するセクションが追加されており、ユーザーはRESTアプローチを用いた知識ソースの確認方法についての詳細を得ることができます。

この更新により、ユーザーはWeb知識ソースの利用において必要な最新のベストプラクティスと技術的ガイダンスを入手できるようになります。文書は、Azure AI Searchの効果的な利用を促進し、ユーザーが具体的なシナリオでの実装をスムーズに行えるようサポートしています。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-python.md{#item-4e498f}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ After you create a knowledge base, you can update its properties at any time. If
 
 + One or more [knowledge sources](../../agentic-knowledge-source-overview.md#supported-knowledge-sources) on your search service.
 
-+ Permissions on your search service. **Search Service Contributor** can create and manage a knowledge base. **Search Index Data Reader** can run queries.
++ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md). **Search Service Contributor** can create and manage a knowledge base. **Search Index Data Reader** can run queries. Alternatively, you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
 
 + The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonによる知識ベース作成に関する文書の更新"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-python.md`という文書のマイナーな更新を示しています。主な目的は、Azure AI Searchにおけるオブジェクトの作成および使用に必要な権限についての情報を明確化することです。

具体的な変更内容は以下の通りです：
- 知識ベースを作成するための条件として、検索サービス上の1つ以上の[知識ソース](../../agentic-knowledge-source-overview.md#supported-knowledge-sources)の存在が必要であることが新たに記載されました。
- 検索サービス上の権限に関する説明が更新され、「Azure AI Search上でオブジェクトを作成および使用するための権限」という文言が追加されました。役割に基づくアクセスの利用が推奨されており、**Search Service Contributor**が知識ベースの作成と管理を行えること、**Search Index Data Reader**がクエリを実行できることが明示されています。また、役割の割り当てが不可能な場合には[APIキー](../../search-security-api-keys.md)の使用が代替案として提案されています。詳細な情報として、検索サービスへの接続に関するリンクも提供されています。

これらの修正により、ユーザーはPythonを使用して知識ベースを作成する際に必要な権限や条件をより容易に理解できるようになります。この文書更新は、Azure AI Searchの利用を支援し、関連するベストプラクティスを提示しています。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-rest.md{#item-37851c}

<details>
<summary>Diff</summary>
````diff
@@ -138,7 +138,7 @@ A knowledge base drives the agentic retrieval pipeline. In application code, it'
 
 A knowledge base connects knowledge sources (searchable content) to an LLM deployment from Azure OpenAI. Properties on the LLM establish the connection, while properties on the knowledge source establish defaults that inform query execution and the response.
 
-Use [Knowledge Bases - Create or Update (REST API)](/rest/api/searchservice/knowledgebases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to formulate the request.
+Use [Knowledge Bases - Create or Update (REST API)](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to formulate the request.
 
 ```http
 # Create a knowledge base
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST API文書の知識ベースのリンク修正"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-rest.md`という文書のマイナーな更新を示しています。主な目的は、知識ベースを作成または更新するためのREST APIのリンクに関する修正です。

具体的な変更内容は以下の通りです：
- 知識ベースの作成または更新に使用するREST APIのURLに誤りがあり、`/knowledgebases/`という部分が`/knowledge-bases/`に修正されました。これは、URLコンポーネントの一貫性を保ち、正確なエンドポイントに対してリクエストを行うために重要です。

この修正により、ユーザーは正しいREST APIエンドポイントを使用して知識ベースのリクエストを行うことができるようになり、エラーを避けることができます。文書全体の信頼性と精度が向上するため、実装時の問題発生を減少させる助けとなります。

## articles/search/includes/how-tos/knowledge-source-delete-python.md{#item-bf68d8}

<details>
<summary>Diff</summary>
````diff
@@ -81,7 +81,7 @@ To delete a knowledge source:
     }
    ```
 
-1. Either delete the knowledge base or [update the knowledge base](/rest/api/searchservice/knowledgebases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to remove the knowledge source if you have multiple sources. This example shows deletion.
+1. Either delete the knowledge base or [update the knowledge base](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) to remove the knowledge source if you have multiple sources. This example shows deletion.
 
     ```python
     # Delete a knowledge base
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonによるナレッジソース削除文書のリンク修正"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/knowledge-source-delete-python.md`という文書のマイナーな更新を示しています。主な目的は、ナレッジソースを削除するための手順に関するREST APIのリンク修正です。

具体的な変更内容は以下の通りです：
- ナレッジソースを削除する際に、ナレッジベースを削除するか、または複数のソースがある場合にはナレッジベースを更新してナレッジソースを削除するためのAPIのURLが修正されました。修正前は`/knowledgebases/`となっていた部分が、正しい形式である`/knowledge-bases/`に変更されました。

この修正により、ユーザーは正確なREST APIエンドポイントを介してナレッジソースを操作することができるようになり、手続きがスムーズに進むことが期待されます。文書の信頼性が向上し、ユーザーにとっての理解が促進されます。

## articles/search/includes/how-tos/knowledge-source-delete-rest.md{#item-225321}

<details>
<summary>Diff</summary>
````diff
@@ -67,7 +67,7 @@ To delete a knowledge source:
     }
    ```
 
-1. Either delete the knowledge base or [update the knowledge base](/rest/api/searchservice/knowledgebases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) by removing the knowledge source if you have multiple sources. This example shows deletion.
+1. Either delete the knowledge base or [update the knowledge base](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) by removing the knowledge source if you have multiple sources. This example shows deletion.
 
     ```http
     ### Delete a knowledge base
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTによるナレッジソース削除文書のリンク修正"
}
```

### Explanation
この変更は、`articles/search/includes/how-tos/knowledge-source-delete-rest.md`という文書のマイナーな更新を示しています。主な目的は、ナレッジソースを削除するための手順に関するREST APIのリンク修正です。

具体的な変更内容は以下の通りです：
- ナレッジソースを削除する際に、ナレッジベースを削除するか、または複数のソースがある場合にはナレッジベースを更新してナレッジソースを削除するためのAPIのURLが修正されました。修正前は`/knowledgebases/`となっていた部分が、正しい形式である`/knowledge-bases/`に変更されました。

この修正により、ユーザーは正確なREST APIエンドポイントを通じてナレッジソースを操作することができ、手続きがより円滑に進むことが期待されます。また、文書の信頼性が向上し、ユーザーの理解を助けることになります。

## articles/search/search-blob-indexer-role-based-access.md{#item-887e42}

<details>
<summary>Diff</summary>
````diff
@@ -1,29 +1,32 @@
 ---  
-title: Use a Blob indexer to ingest RBAC scopes metadata
+title: Use a Blob indexer or knowledge source to ingest RBAC scopes metadata
 titleSuffix: Azure AI Search  
-description: Learn how to configure Azure AI Search indexers for ingesting Azure Role-Based Access (RBAC) metadata on Azure blobs.
+description: Learn how to configure Azure AI Search knowledge sources and indexers for ingesting Azure Role-Based Access (RBAC) metadata on Azure blobs.
 ms.service: azure-ai-search  
 ms.topic: how-to
-ms.date: 09/18/2025
+ms.date: 11/18/2025
 author: vaishalishah
 ms.author: vaishalishah
 ---  
 
-# Use a Blob indexer to ingest RBAC scopes metadata
+# Use a Blob indexer or knowledge source to ingest RBAC scopes metadata
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Azure Storage allows for role-based access on containers in blob storage, where roles like **Storage Blob Data Reader** or **Storage Blob Data Contributor** determine whether someone has access to content. Starting in 2025-05-01-preview, you can now include RBAC scope alongside document ingestion in Azure AI Search and use those permissions to control access to search results. If you have rights to the content, you can see that content in search results. If you don't have rights (or more specifically, a role assignment on the blob container), you *can't* see those results even if you personally have a **Search Index Data Reader** assignment *on the index*.
+Azure Storage allows for role-based access on containers in blob storage, where roles like **Storage Blob Data Reader** or **Storage Blob Data Contributor** determine whether someone has access to content. Preview APIs in Azure AI Search now support ingestion of user permissions alongside document ingestion so that you can use those permissions to control access to search results. If a user lacks permissions on a specific directory or file in Azure Storage, that user doesn't have access to the corresponding documents in Azure AI Search results, even if you personally have a **Search Index Data Reader** assignment *on the index*.
 
-RBAC scope is set at the container level and flows to all blobs (documents) through permission inheritance. RBAC scope is captured during indexing as permission metadata. You can use the push APIs to upload and index content and permission metadata manually (see [Indexing Permissions using the push REST API](search-index-access-control-lists-and-rbac-push-api.md)), or you can use an indexer to automate data ingestion. This article focuses on the indexer approach.
++ 2025-05-01-preview and later, RBAC scopes metadata can be ingested using the [Blob indexer](search-how-to-index-azure-data-lake-storage.md).
++ 2025-11-01-preview provides equivalent support for [Blob knowledge sources](agentic-knowledge-source-how-to-blob.md) in Azure Storage.
+
+RBAC scope is set at the container level and flows to all blobs (documents) through permission inheritance. RBAC scope is captured during indexing as permission metadata. You can use the push APIs to upload and index content and permission metadata manually (see [Indexing Permissions using the push REST API](search-index-access-control-lists-and-rbac-push-api.md)), or you can use an indexer or knowledge source to automate data ingestion. This article focuses on indexing automation.
 
 At query time, the identity of the caller is included in the request header via the `x-ms-query-source-authorization` parameter. The identity must match the permission metadata on documents if the user is to see the search results.
 
-The indexer approach is built on this foundation:
+This article focuses on the indexing automation approaches, built on this foundation:
 
 + [Azure Storage blobs secured using role-based access control (Azure RBAC)](/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac). There's no support for Attribute-based access control (Azure ABAC).
 
-+ [An Azure AI Search indexer for blobs](search-how-to-index-azure-blob-storage.md) that retrieves and ingests data and metadata, including permission filters. To get permission filter support, use the latest preview REST API or a preview package of an Azure SDK that supports the feature.
++ [Azure Blob indexer](#configure-indexer-based-indexing) or a [Blob knowledge source](#configure-a-knowledge-source) that retrieves and ingests data and metadata, including permission filters. To get permission filter support, use the latest preview REST API or a preview package of an Azure SDK that supports the feature.
 
 + [An index in Azure AI Search](search-how-to-create-search-index.md) containing the ingested documents and corresponding permissions. Permission metadata is stored as fields in the index. 
 
@@ -37,7 +40,7 @@ The indexer approach is built on this foundation:
 
 + Azure Storage, Standard performance (general-purpose v2), on hot, cool, and cold access tiers, with RBAC-secured containers or blobs.
 
-+ You should understand how indexers work and how to create an index. This article explains the configuration settings for the data source and indexer, but doesn't provide steps for creating the index. For more information about indexes designed for permission filters, see [Create an index with permission filter fields](search-index-access-control-lists-and-rbac-push-api.md#create-an-index-with-permission-filter-fields).
++ You should understand how indexers and knowledge sources work and how to create an index. This article explains the configuration settings for the data source and indexer, but doesn't provide steps for creating the index. For more information about indexes designed for permission filters, see [Create an index with permission filter fields](search-index-access-control-lists-and-rbac-push-api.md#create-an-index-with-permission-filter-fields).
 
 + This functionality is currently not supported in the Azure portal, this includes Permission filters created through the [Import wizards](search-import-data-portal.md). Use a programmatic approach to create or modify existing objects for document-level access. 
 
@@ -66,9 +69,59 @@ Recall that the search service must have:
 
 For indexer execution, the client issuing the API call must have **Search Service Contributor** permission to create objects, **Search Index Data Contributor** permission to perform data import, and **Search Index Data Reader** to query an index see [Connect to Azure AI Search using roles](search-security-rbac.md).
 
-## Configure indexing
+## Configure a knowledge source
+
+If you're using a knowledge source, definitions in the knowledge source are used to generate a full indexing pipeline (indexer, data source, and index). RBAC scope is detected and automatically included in the generated index. There's no need to modify any of the generated objects if you want permission inheritance in your indexed content.
+
+Key points about the configuration that make it work for this scenario:
+
++ `isADLSGen2` is set to false, which means the data source is Azure Blob storage.
++ `ingestionPermissionOptions` specifies `rbacScope`.
+
+```http
+# Create / Update Azure Blob Knowledge Source
+###
+PUT {{url}}/knowledgesources/azure-blob-ks?api-version=2025-11-01-preview
+api-key: {{key}}
+Content-Type: application/json
+ 
+{
+    "name": "azure-blob-ks",
+    "kind": "azureBlob",
+    "description": "A sample azure blob knowledge source",
+    "azureBlobParameters": {
+        "connectionString": "{{blob-connection-string}}",
+        "containerName": "blobcontainer",
+        "folderPath": null,
+        "isADLSGen2": false,
+        "ingestionParameters": {
+            "identity": null,
+            "embeddingModel": {
+                "kind": "azureOpenAI",
+                "azureOpenAIParameters": {
+                    "deploymentId": "text-embedding-3-large",
+                    "modelName": "text-embedding-3-large",
+                    "resourceUri": "{{aoai-endpoint}}",
+                    "apiKey": "{{aoai-key}}"
+                }
+            },
+            "chatCompletionModel": null,
+            "disableImageVerbalization": true,
+            "ingestionSchedule": null,
+            "ingestionPermissionOptions": ["rbacScope"],
+            "contentExtractionMode": "minimal",
+            "aiServices": {
+                "uri": "{{ai-endpoint}}",
+                "apiKey": "{{ai-key}}"
+            }
+        }
+    }
+}
+```
+
+## Configure indexer-based indexing
 
-In Azure AI Search, configure an indexer, data source, and index to pull permission metadata from blobs.
+If you're using an indexer, configure it, the data source, and the index to pull permission metadata from blobs.
 
 ### Create the data source
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "BlobインデクサーにおけるRBACスコープのメタデータの取り込み改善"
}
```

### Explanation
この変更は、`articles/search/search-blob-indexer-role-based-access.md`という文書の大規模な更新を示しています。主な目的は、RBACスコープのメタデータを取り込む際のBlobインデクサーとナレッジソースの利用を明確にすることです。

具体的な変更内容は以下の通りです：
- 文書のタイトルと説明において、Blobインデクサーだけでなく、知識ソースを使用してRBACスコープメタデータを取り込むことができることを明記しました。
- RBACスコープのメタデータ取り込みに関する説明が強化され、Azure AI Searchがユーザーの権限を考慮に入れて検索結果にアクセスを制御できることを明示しました。
- 知識ソースに関連する設定やその効果に関する詳細な説明が追加され、インデクサーにおけるRBACスコープの継承を簡素化する内容が含まれています。

これにより、ユーザーはBlobインデクサーやナレッジソースを用いたRBACスコープメタデータの取り込みについて、より包括的に理解できるようになります。また、関連するAPIやSDKの使用に関する具体的な設定も提供され、実行可能性が高まります。これにより、ユーザーはAzure AI Searchを通じて権限管理をより効果的に行うことが期待されます。

## articles/search/search-capacity-planning.md{#item-0dd6c9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: conceptual
-ms.date: 09/26/2025
+ms.date: 11/19/2025
 ms.update-cycle: 180-days
 ---
 
@@ -103,7 +103,9 @@ To increase or decrease the capacity of your service, you have two options:
 
    :::image type="content" source="media/search-capacity-planning/portal-notifications.png" alt-text="Screenshot of the notification of the scaling operation in the Azure portal." border="true" lightbox="media/search-capacity-planning/portal-notifications.png":::
 
-   This operation can take several hours to complete. You can’t cancel the process after it starts, and there’s no real-time monitoring of replica and partition adjustments. However, the following message displays while changes are underway.
+   This operation can take several hours to complete. It occurs in the background, so your search service remains fully operational and available for read and write operations.
+
+   You can't cancel the operation or monitor its progress. However, the following message displays while changes are underway:
 
    :::image type="content" source="media/search-capacity-planning/updating-message.png" alt-text="Screenshot of the Updating message in the Azure portal." border="true" lightbox="media/search-capacity-planning/updating-message.png":::
 
@@ -138,7 +140,9 @@ To change your pricing tier:
 
    :::image type="content" source="media/search-capacity-planning/save-button.png" alt-text="Screenshot of the Save button in the Azure portal." border="true" lightbox="media/search-capacity-planning/save-button.png":::
 
-   This operation can take several hours to complete. You can't cancel the process after it starts, and there's no real-time monitoring of tier changes. However, the following message displays while changes are underway.
+   This operation can take several hours to complete. It occurs in the background, so your search service remains fully operational and available for read and write operations.
+
+   You can't cancel the operation or monitor its progress. However, the following message displays while changes are underway:
 
    :::image type="content" source="media/search-capacity-planning/updating-message.png" alt-text="Screenshot of the Updating message in the Azure portal." border="true" lightbox="media/search-capacity-planning/updating-message.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスのキャパシティ計画に関する運用の詳細変更"
}
```

### Explanation
この変更は、`articles/search/search-capacity-planning.md`という文書のマイナーな更新を示しています。主な目的は、検索サービスのキャパシティを調整する際の手順とその運用面に関する情報を明確にしたことです。

具体的な変更内容は以下の通りです：
- キャパシティの増減を行う際に、操作がバックグラウンドで実行されるため、検索サービスは完全に操作可能であり、読み書きが可能であることが強調されました。この変更により、ユーザーはサービスの可用性についての理解が深まると考えられます。
- 操作が開始された後はキャンセルできず、進行状況を監視することもできないという情報が明確に示されました。これにより、ユーザーはキャパシティ変更の際の制約を理解しやすくなります。
- 文中の具体的なメッセージ内容については変更がありませんが、変更に伴う通知画像はそのまま保持されています。

これにより、ユーザーが検索サービスのキャパシティ計画をより良く理解し、実際の運用にご活用いただくことが期待されます。

## articles/search/search-document-level-access-overview.md{#item-4bb055}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Conceptual overview of document-level permissions in Azure AI Search.
 author: gmndrg
 ms.author: gimondra
-ms.date: 11/10/2025
+ms.date: 11/18/2025
 ms.service: azure-ai-search
 ms.topic: conceptual
 ms.custom:
@@ -14,7 +14,6 @@ ms.custom:
 # Document-level access control in Azure AI Search  
   
 Azure AI Search supports document-level access control, enabling organizations to enforce fine-grained permissions at the document level, from data ingestion through query execution. This capability is essential for building secure AI agentic systems grounding data, Retrieval-Augmented Generation (RAG) applications, and enterprise search solutions that require authorization checks at the document level.  
-
   
 ## Approaches for document-level access control
 
@@ -44,7 +43,7 @@ This approach is useful for systems with custom access models or non-Microsoft s
 
 Native support is based on Microsoft Entra users and groups affiliated with documents that you want to index and query. 
 
-Azure Data Lake Storage (ADLS) Gen2 containers support ACLs on the container and on files. For ADLS Gen2, RBAC scope preservation at document level is natively supported when you use the [ADLS Gen2 indexer](search-how-to-index-azure-data-lake-storage.md) and the preview API version 2025-11-01-preview to ingest content. For Azure blobs using the [Azure blob indexer](search-blob-indexer-role-based-access.md), RBAC scope preservation is at the container level.
+Azure Data Lake Storage (ADLS) Gen2 containers support ACLs on the container and on files. For ADLS Gen2, RBAC scope preservation at document level is natively supported when you use an [ADLS Gen2 indexer](search-how-to-index-azure-data-lake-storage.md) or a [Blob knowledge source (supports ADLS Gen2)](agentic-knowledge-source-how-to-blob.md) and a preview API to ingest content. For Azure blobs using the [Azure blob indexer](search-blob-indexer-role-based-access.md) or knowledge source, RBAC scope preservation is at the container level.
 
 For ACL-secured content, we recommend group access over individual user access for ease of management. The pattern includes the following components:
 
@@ -81,11 +80,10 @@ For the [push model approach](search-index-access-control-lists-and-rbac-push-ap
 1. Consider using the Microsoft Graph SDK to get group or user identities.
 1. Use the [Index Documents](/rest/api/searchservice/documents/?view=rest-searchservice-2025-11-01-preview&preserve-view=true#indexdocumentsresult) or equivalent Azure SDK API to push documents and their associated permission metadata into the search index. 
 
-For the [pull model ADLS Gen2 indexer approach](search-indexer-access-control-lists-and-role-based-access.md):
+For the [pull model ADLS Gen2 indexer approach](search-indexer-access-control-lists-and-role-based-access.md) or [Blob (ADLS Gen2) knowledge source](agentic-knowledge-source-how-to-blob.md):
 
 1. Verify that files in the directory are secured using the [ADLS Gen2 access control model](/azure/storage/blobs/data-lake-storage-access-control-model).
-1. Use the [Create Indexer](/rest/api/searchservice/indexers/create?view=rest-searchservice-2025-11-01-preview&preserve-view=true) or equivalent Azure SDK API to create the indexer, index, and data source.
-
+1. Use the [Create Indexer REST API](/rest/api/searchservice/indexers/create?view=rest-searchservice-2025-11-01-preview&preserve-view=true) or [Create Knowledge Source REST API](/rest/api/searchservice/knowledge-sources/create?view=rest-searchservice-2025-11-01-preview&preserve-view=true) or equivalent Azure SDK API to create the indexer, index, and data source.
 
 ## Pattern for SharePoint in Microsoft 365 basic ACL permissions ingestion (preview)
 
@@ -107,7 +105,7 @@ During preview, only the following principal types are supported in SharePoint A
 - Microsoft 365 groups  
 - Mail-enabled security groups  
 
-SharePoint groups are not supported in the preview release. 
+SharePoint groups aren't supported in the preview release. 
 
 For configuration details and full limitations, see [How to index SharePoint in Microsoft 365 document-level permissions (preview)](https://aka.ms/azs-sharepoint-indexer-acls).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレベルアクセス制御に関する情報の更新"
}
```

### Explanation
この変更は、`articles/search/search-document-level-access-overview.md`という文書の小規模な更新を示しています。主な目的は、Azure AI Searchにおけるドキュメントレベルアクセス制御に関する情報の明確化と強化です。

具体的な変更内容は以下の通りです：
- 更新日が2025年11月10日から2025年11月18日に変更されました。
- ドキュメントレベルアクセス制御において、Azure Data Lake Storage (ADLS) Gen2のインデクサーまたはBlobナレッジソースを使用することで、RBACスコープの保存が文書レベルでネイティブにサポートされることが強調されました。これにより、ユーザーはデータ取得の際の権限管理の詳細を理解しやすくなります。
- アクセス制御リスト（ACL）に関する推奨事項として、個別ユーザーよりもグループアクセスを推奨する文言が明確化され、管理の容易性が示されています。
- プルモデルのADLS Gen2インデクサーアプローチやBlobナレッジソースの使用に関して、APIの呼び出し方法がより具体的に更新されました。具体的には、インデクサーやナレッジソースを作成するためのREST APIのリンクが追加され、ドキュメントと権限メタデータを検索インデックスにプッシュする方法が具体化されています。

これにより、ユーザーはAzure AI Searchにおけるドキュメントレベルのアクセス制御について、より深く理解し、具体的な操作手順や推奨事項を把握できるようになります。

## articles/search/search-indexer-access-control-lists-and-role-based-access.md{#item-67b42f}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how to configure Azure AI Search indexers for ingesting Access Control Lists (ACLs) and Azure Role-Based Access (RBAC) metadata on Azure Data Lake Storage (ADLS) Gen2 blobs.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 11/08/2025  
+ms.date: 11/18/2025  
 author: gmndrg
 ms.author: gimondra
 ---  
@@ -13,21 +13,24 @@ ms.author: gimondra
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-The permission model in Azure Data Lake Storage (ADLS) Gen2 can be used for per-user access to specific directories or files. Starting in 2025-05-01-preview, you can now include user permissions alongside document ingestion in Azure AI Search and use those permissions to control access to search results. If a user lacks permissions on a specific directory or file in ADLS Gen2, that user doesn't have access to the corresponding documents in Azure AI Search results.
+The permission model in Azure Data Lake Storage (ADLS) Gen2 allows for per-user access to specific directories or files. Preview APIs in Azure AI Search now support ingestion of user permissions alongside document ingestion so that you can use those permissions to control access to search results. If a user lacks permissions on a specific directory or file in ADLS Gen2, that user doesn't have access to the corresponding documents in Azure AI Search results.
 
-You can use the push APIs to upload and index content and permission metadata manually, or you can use an indexer to automate data ingestion. This article focuses on the indexer approach.
++ 2025-05-01-preview and later, ADLS Gen2 permissions can be ingested using the [ADLS Gen2 indexer](search-how-to-index-azure-data-lake-storage.md).
++ 2025-11-01-preview provides equivalent support for [ADLS Gen2 blob knowledge sources](agentic-knowledge-source-how-to-blob.md) in Azure Storage.
 
-The indexer approach is built on this foundation:
+You can use the push APIs to upload and index content and permission metadata manually, or you can use an indexer or knowledge source to automate data ingestion. 
+
+This article focuses on the indexing automation approaches, built on this foundation:
 
 + [The ADLS Gen2 access control model](/azure/storage/blobs/data-lake-storage-access-control-model) that provides [Access control lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control-model#access-control-lists-acls) and [Role-based access control (Azure RBAC)](/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac). There's no support for Attribute-based access control (Azure ABAC).
 
-+ [An Azure AI Search indexer for ADLS Gen2](search-how-to-index-azure-data-lake-storage.md) that retrieves and ingests data and metadata, including permission filters. To get permission filter support, use the latest preview REST API or a prerelease package of an Azure SDK that supports the feature.
++ [An ADLS Gen2 indexer](#configure-adls-gen2) or [ADLS Gen2 blob knowledge source](#configure-a-knowledge-source) that retrieves and ingests data and metadata, including permission filters. To get permission filter support, use the latest preview REST API or a preview package of an Azure SDK that supports the feature.
 
-+ [An index in Azure AI Search](search-how-to-create-search-index.md) containing the ingested documents and corresponding permissions. Permission metadata is stored as fields in the index. To set up queries that respect the permission filters, use the latest preview REST API or a prerelease package of an Azure SDK that supports the feature.
++ [An index in Azure AI Search](search-how-to-create-search-index.md) containing the ingested documents and corresponding permissions. Permission metadata is stored as fields in the index. To set up [queries that respect the permission filters](search-query-access-control-rbac-enforcement.md), use the latest preview REST API or a preview package of an Azure SDK that supports the feature.
 
 This functionality helps align [document-level permissions](search-security-trimming-for-azure-search.md) in the search index with the access controls defined in ADLS Gen2, allowing users to retrieve content in a way that reflects their existing permissions.
 
-This article supplements [**Index data from ADLS  Gen2**](search-how-to-index-azure-data-lake-storage.md) with information that's specific to ingesting permissions alongside document content into an Azure AI Search index. 
+This article supplements [**Index data from ADLS  Gen2**](search-how-to-index-azure-data-lake-storage.md) and [**ADLS Gen2 blob knowledge sources**](agentic-knowledge-source-how-to-blob.md) with information that's specific to ingesting permissions alongside document content into an Azure AI Search index. 
 
 ## Prerequisites
 
@@ -66,15 +69,15 @@ This section compares document-level access control features between ADLS Gen2 a
 
 ## About ACL hierarchical permissions
 
-Indexers can retrieve ACL assignments from the specified container and all directories leading to each file by following the ADLS Gen2 [hierarchical access evaluation flow](/azure/storage/blobs/data-lake-storage-access-control#common-scenarios-related-to-acl-permissions). The final effective access lists for each file are computed and the different access categories are indexed into the corresponding index fields.
+Indexers and knowledge sources can retrieve ACL assignments from the specified container and all directories leading to each file by following the ADLS Gen2 [hierarchical access evaluation flow](/azure/storage/blobs/data-lake-storage-access-control#common-scenarios-related-to-acl-permissions). The final effective access lists for each file are computed and the different access categories are indexed into the corresponding index fields.
 
 For example, in [ADLS Gen2 common scenarios related to permissions](/azure/storage/blobs/data-lake-storage-access-control#common-scenarios-related-to-acl-permissions) as the file path /Oregon/Portland/Data.txt.
 
 | Operation |	/ |	Oregon/ |	Portland/ |	Data.txt |
 | - | - | - | - | - |
 | Read Data.txt	| --X	| --X	| --X	| R-- |
 
-The indexer collects ACLs from each container and directory. It then determines effective access at lower levels and continues until it resolves permissions for every file.
+The indexer or knowledge source collects ACLs from each container and directory. It then determines effective access at lower levels and continues until it resolves permissions for every file.
 
 ```txt
 / assigned access vs Oregon/ assigned access
@@ -85,11 +88,11 @@ The indexer collects ACLs from each container and directory. It then determines
 
 ## Configure ADLS Gen2
 
-An indexer can retrieve ACLs on a storage account if the following criteria are met. For more information about ACL assignments, see [ADLS Gen2 ACL assignments](/azure/storage/blobs/data-lake-storage-access-control#how-to-set-acls).
+An indexer or knowledge source can retrieve ACLs on a storage account if the following criteria are met. For more information about ACL assignments, see [ADLS Gen2 ACL assignments](/azure/storage/blobs/data-lake-storage-access-control#how-to-set-acls).
 
 ### Authorization
 
-For indexer execution, your search service identity must have **Storage Blob Data Reader** permission. 
+For indexing, your search service identity must have **Storage Blob Data Reader** permission. 
 
 If you're testing locally, you should also have a **Storage Blob Data Reader** role assignment. For more information, see [Connect to Azure Storage using a managed identity](search-howto-managed-identities-storage.md).
 
@@ -119,7 +122,7 @@ Here's a diagram of the ACL assignment structure for the [fictitious directory h
 
 ### Updating ACL assignments over time
 
-Over time, as any new ACL assignments are added or modified, repeat the above steps to ensure proper propagation and permissions alignment. Updated permissions in ADLS Gen2 are updated in the search index when you re-ingest the content using the indexer.
+Over time, as any new ACL assignments are added or modified, repeat the above steps to ensure proper propagation and permissions alignment. Updated permissions in ADLS Gen2 are updated in the search index when you re-ingest the content using the indexer or knowledge source.
 
 ## Configure Azure AI Search
 
@@ -130,13 +133,67 @@ Recall that the search service must have:
 
 ### Authorization
 
-For indexer execution, the client issuing the API call must have **Search Service Contributor** permission to create objects, **Search Index Data Contributor** permission to perform data import, and **Search Index Data Reader** to query an index. 
+For indexing, the client issuing the API call must have **Search Service Contributor** permission to create objects, **Search Index Data Contributor** permission to perform data import, and **Search Index Data Reader** to query an index. 
 
 If you're testing locally, you should have the same role assignments. For more information, see [Connect to Azure AI Search using roles](search-security-rbac.md).
 
-## Configure indexing
+## Configure a knowledge source
+
+If you're using a knowledge source, definitions in the knowledge source are used to generate a full indexing pipeline (indexer, data source, and index). ACL assignments are detected and automatically included in the generated index. There's no need to modify any of the generated objects if you want permission inheritance in your indexed content.
+
+Key points about the configuration that make it work for this scenario:
+
++ `isADLSGen2` is set to true, meeting the data source requirement for this scenario.
++ `ingestionPermissionOptions` specifies user and group IDs.
++ `disableImageVerbalization` is set to true because the GenAI Prompt skill that backs this experience isn't currently supported in ADLS Gen2 permission inheritance.
+
+```http
+# Create / Update Azure Blob Knowledge Source
+###
+PUT {{url}}/knowledgesources/azure-blob-ks?api-version=2025-11-01-preview
+api-key: {{key}}
+Content-Type: application/json
+ 
+{
+    "name": "azure-blob-ks",
+    "kind": "azureBlob",
+    "description": "A sample azure blob knowledge source",
+    "azureBlobParameters": {
+        "connectionString": "{{blob-connection-string}}",
+        "containerName": "blobcontainer",
+        "folderPath": null,
+        "isADLSGen2": true,
+        "ingestionParameters": {
+            "identity": null,
+            "embeddingModel": {
+                "kind": "azureOpenAI",
+                "azureOpenAIParameters": {
+                    "deploymentId": "text-embedding-3-large",
+                    "modelName": "text-embedding-3-large",
+                    "resourceUri": "{{aoai-endpoint}}",
+                    "apiKey": "{{aoai-key}}"
+                }
+            },
+            "chatCompletionModel": null,
+            "disableImageVerbalization": true,
+            "ingestionSchedule": null,
+             "ingestionPermissionOptions": [
+                "userIds","groupIds"
+                           ],
+            "contentExtractionMode": "minimal",
+            "aiServices": {
+                "uri": "{{ai-endpoint}}",
+                "apiKey": "{{ai-key}}"
+            }
+        }
+    }
+}
+###
+```
+
+## Configure indexer-based indexing
 
-In Azure AI Search, configure an indexer, data source, and index to pull permission metadata from ADLS Gen2 blobs.
+If you're using an indexer, configure it, the data source, and the index to pull permission metadata from ADLS Gen2 blobs.
 
 ### Create the data source
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーとアクセス制御リストに関する情報の更新"
}
```

### Explanation
この変更は、`articles/search/search-indexer-access-control-lists-and-role-based-access.md`という文書の更新を示しており、Azure AI Searchにおけるインデクサーとアクセス制御リスト（ACL）に関する情報を強化しています。

具体的な変更内容は以下の通りです：
- 更新日が2025年11月8日から2025年11月18日に変更されました。
- Azure Data Lake Storage (ADLS) Gen2のアクセス許可モデルについての説明が明確化され、ユーザーの各ディレクトリやファイルへのアクセスを制御する方法が再確認されました。また、ADLS Gen2のインデクサーまたはBlobナレッジソースを通じて、ユーザーのパーミッションを文書の取り込みと同時に処理できる機能が追加されています。
- 同時に、ACLの取得に関する手法が、インデクサーだけでなくナレッジソースでもサポートされることが強調されています。
- 記事内では、インデクサーの設定やデータソースの作成についても詳細が追加されており、具体的なHTTPリクエストの例が示されています。これにより、ユーザーはリアルな設定手順を追いやすくなります。
- ACLのハイエラルキーに基づくパーミッション評価フローに関する内容が、インデクサーだけでなくナレッジソースにも適用されることが強調され、知識ソースの設定に関する情報が詳細に追加されています。

これにより、Azure AI Searchに関わるユーザーは、インデクサーおよび ACL 管理の実装に際しての手順や注意点をより明確に把握できるようになります。

## articles/search/search-query-sensitivity-labels.md{#item-3e1f8a}

<details>
<summary>Diff</summary>
````diff
@@ -4,13 +4,15 @@ titleSuffix: Azure AI Search
 description: Learn how query-time enforcement of Microsoft Purview sensitivity labels ensures secure document retrieval in Azure AI Search for indexes containing label metadata.  
 ms.service: azure-ai-search  
 ms.topic: conceptual  
-ms.date: 11/10/2025  
+ms.date: 11/18/2025  
 author: gmndrg  
 ms.author: gimondra  
 ---
 
 # Query-Time Microsoft Purview Sensitivity Label Enforcement in Azure AI Search  
 
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
 At query time, Azure AI Search enforces sensitivity label policies defined in [Microsoft Purview](/purview/create-sensitivity-labels). These policies include evaluation of [extract usage rights](/purview/rights-management-usage-rights) tied to each document. As a result, users can only retrieve documents they are allowed to view.
 
 This capability extends [document-level access control](search-document-level-access-overview.md) to align with your organization's [information protection and compliance requirements](/purview/create-sensitivity-labels) managed in Microsoft Purview.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリ時の感度ラベルの強制に関する情報の更新"
}
```

### Explanation
この変更は、`articles/search/search-query-sensitivity-labels.md`という文書の小規模な更新を示しています。主な目的は、Azure AI SearchにおけるMicrosoft Purviewの感度ラベルのクエリ時の強制機能に関する情報を明確化することです。

具体的な変更内容は以下の通りです：
- 更新日が2025年11月10日から2025年11月18日に変更されました。
- Microsoft Purviewの感度ラベルポリシーをクエリ時に強制する機能についての説明が追加され、これらのポリシーが各文書に関連付けられた使用権の評価を含むことが明記されました。その結果、ユーザーは自分が閲覧を許可されている文書のみを取得できるようになります。
- この機能はドキュメントレベルのアクセス制御を拡張し、組織の情報保護およびコンプライアンス要件に従った管理を行うことができる点が強調されています。
- 変更内容冒頭に「[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]」の記述が追加され、新機能のプレビュー情報が含まれることが示されています。

これにより、ユーザーはAzure AI Searchにおける情報の取得と管理に関する最新の機能とその重要性について、より明確に理解できるようになります。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about the regions that offer Azure AI Search and the features
 author: haileytap
 ms.author: haileytapia
 manager: nitinme
-ms.date: 11/10/2025
+ms.date: 11/19/2025
 ms.service: azure-ai-search
 ms.topic: conceptual
 ms.custom:
@@ -35,7 +35,7 @@ When you create an Azure AI Search service, your region selection might depend o
 
 ## Azure Public regions
 
-You can create an Azure AI Search service in any of the following Azure public regions. Almost all of these regions support [higher-capacity tiers](search-limits-quotas-capacity.md#service-limits). Exceptions are noted where they apply.
+You can create an Azure AI Search service in any of the following Azure public regions. Almost all of these regions support [higher-capacity tiers](search-limits-quotas-capacity.md#service-limits). Exceptions are noted where applicable.
 
 ### Americas
 
@@ -45,19 +45,21 @@ You can create an Azure AI Search service in any of the following Azure public r
 | Canada Central​​ <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Canada East​​ ​<sup>1</sup> |  |  | ✅ |  | ✅ |  |
 | ​Central US​​ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
-| East US​ <sup>1</sup> | ✅ | ✅ | ✅ |  | ✅ |  |
+| East US​ <sup>1, 2</sup> | ✅ | ✅ | ✅ |  | ✅ |  |
 | East US 2 <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 | Mexico Central |  | ✅ |  |  |  |  |
 | North Central US​ <sup>1</sup> ​| ✅ |  | ✅ |  | ✅ | ✅ |
 | South Central US​ <sup>1</sup> | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | West US​​ <sup>1</sup> | ✅ |  | ✅ |  | ✅ | ✅ |
-| West US 2​ <sup>2</sup> ​| ✅ | ✅ | ✅ |  | ✅ | ✅ |
+| West US 2​ <sup>3</sup> ​| ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | West US 3​ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 | West Central US​ ​<sup>1</sup>| ✅ |  | ✅ |  | ✅ |  |
 
-<sup>1</sup> Supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
+<sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
-<sup>2</sup> There's no indexer support in West US 2 for [Microsoft Purview sensitivity labels](search-indexer-sensitivity-labels.md).
+<sup>2</sup> This region is experiencing capacity constraints that prevent the creation of new search services and might present failures for scale operations. Please choose a different region.
+
+<sup>3</sup> This region doesn't have indexer support for [Microsoft Purview sensitivity labels](search-indexer-sensitivity-labels.md).
 
 ### Europe
 
@@ -77,31 +79,31 @@ You can create an Azure AI Search service in any of the following Azure public r
 | UK West​ ​|  |  | ✅ |  | ✅ |  |
 | West Europe​​ <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
 
-<sup>1</sup> Supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
+<sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
 <sup>2</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
 
 ### Middle East
 
 | Region | AI enrichment | Availability zones | Agentic retrieval | Confidential computing | Semantic ranker | Query rewrite |
 |--|--|--|--|--|--|--|
-| Israel Central​ <sup>2</sup> |  | ✅ |  |  |  |  |
-| Qatar Central​ <sup>2</sup> |  | ✅ | ✅ |  | ✅ |  |
-| UAE North​​ <sup>1, 3</sup> | ✅ | ✅ | ✅ | ✅ | ✅ |  |
+| Israel Central​ <sup>1</sup> |  | ✅ |  |  |  |  |
+| Qatar Central​ <sup>1</sup> |  | ✅ | ✅ |  | ✅ |  |
+| UAE North​​ <sup>2, 3</sup> | ✅ | ✅ | ✅ | ✅ | ✅ |  |
 
-<sup>1</sup> Supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
+<sup>1</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
 
-<sup>2</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
+<sup>2</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
-<sup>3</sup> This region is experiencing constraints on capacity that prevents the creation of new search services. Please choose a different region.
+<sup>3</sup> This region is experiencing capacity constraints that prevent the creation of new search services. Please choose a different region.
 
 ### Africa
 
 | Region | AI enrichment | Availability zones | Agentic retrieval | Confidential computing | Semantic ranker | Query rewrite |
 |--|--|--|--|--|--|--|
 | South Africa North​ <sup>1</sup> | ✅ | ✅ | ✅ | ✅ | ✅ |  |
 
-<sup>1</sup> Supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
+<sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
 ### Asia Pacific
 
@@ -123,7 +125,7 @@ You can create an Azure AI Search service in any of the following Azure public r
 | South India |  | ✅ |  |  |  |  |
 | Southeast Asia​​ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
 
-<sup>1</sup> Supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
+<sup>1</sup> This region supports [agentic retrieval](agentic-retrieval-overview.md) and [semantic ranker](semantic-search-overview.md) on the free tier.
 
 ## Azure Government regions
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのリージョンサポートに関する情報の更新"
}
```

### Explanation
この変更は、`articles/search/search-region-support.md`という文書の更新を示し、Azure AI Searchがサポートするリージョンに関する情報を含んでいます。主な目的は、ユーザーが利用可能なリージョンとそれに関連する機能の理解を深めることです。

具体的な変更内容は以下の通りです：
- 更新日が2025年11月10日から2025年11月19日に変更されました。
- 文中で地域について言及する際の表現が明確化され、”exceptions are noted where they apply”が”exceptions are noted where applicable”に変更されました。
- 各地域のテーブルが更新され、隣接する地域に対するサポート情報が調整されています。特に、East US、West US 2およびUAE Northについて、新たに記載された制約や機能サポートの詳細が環境の可用性と制約に基づいて修正されています。
- ”アジェンティック検索”や”セマンティックランカー”のサポートに関する記載が、それぞれの地域で実際にサポートされていることを強調するために改訂されました。
- いくつかの地域に対して、容量制約により新しい検索サービスの作成に影響が出る可能性があること、またそのかわりに他の地域を選択するようにとの警告が追加されています。

これらの更新により、ユーザーはAzure AI Searchの利用可能なリージョンとその機能、制限に関する最新の情報を得られるようになります。


