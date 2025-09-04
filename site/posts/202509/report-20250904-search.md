---
date: '2025-09-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:06ab90f...MicrosoftDocs:9037dee
summary: このコード差分は、Azure AI Searchに関する一連のマイナーアップデートを示しており、特にAPIバージョンの更新や説明の改訂が行われています。新しいAPIバージョン「2025-08-01-preview」では、ベクトルフィールドの強化や新機能の追加が特徴です。従来のAPIバージョンからの大幅な変更があり、ユーザーは対応するコードの調整が必要です。また、ドキュメントの整合性向上や新しいナレッジソースの作成についてのガイドが追加されており、これにより開発者はより効率的にAzure
  AI Searchを利用できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:06ab90f...MicrosoftDocs:9037dee){target="_blank"}

<format>
# ハイライト
このコード差分は、Azure AI Searchのさまざまなドキュメントに対する一連のマイナーアップデートを示しています。具体的には、APIバージョンの更新と日付の改訂が多くのドキュメントに適用され、新しい機能の導入や既存機能に関する説明の改善が行われています。

## 新機能
- REST APIの新しいバージョン「2025-08-01-preview」が多くのドキュメントで導入されました。このバージョンでは、ベクトルフィールドの強化や厳密なポストフィルタリングモードの追加、知識エージェントによる回答合成の改善などが特徴です。
- 新しいドキュメントが追加され、Blobナレッジソースや検索インデックスナレッジソースの作成方法についてのガイドが提供されています。
- ベクトルクエリのフィルターモードやベクトルフィールド次元数の最大値の増加など、AI検索機能での精度と効率を高めるための新たなオプションが追加されました。

## ブレイキングチェンジ
- APIバージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新されたことで、いくつかの構文やフィールド構成に対する大幅な変更が導入されており、ユーザーは対応するためのコードの調整が必要です。

## その他の更新
- ドキュメントの整合性と可読性が向上するよう、説明の改善や用語の統一が行われました。
- インデクサー、ナレッジエージェント、およびストレージ関連の設定やアクセス制御の詳細なガイドラインが追加されたり、強化されたりしています。

# 洞察
このコード差分は、Azure AI Searchを利用する開発者やユーザーが、最新の機能を確実に活用できるようにするための改善を行っています。特に、APIバージョンの複数にわたる並行サポートがなくなり、新たなAPIバージョンへの完全な移行が必要になった点は重要です。これにより、開発者は最新のサービス機能を利用するために既存のコードおよび設定をアップデートすることが求められます。

また、新しいナレッジソースの作成ガイドの追加により、開発者はより多様なデータソースを効率的に活用することが可能になり、Azure AI Searchの機能を最大限に活用できる環境が整備されています。これらの変更は、ユーザーエクスペリエンスの向上とサービスの効率的な利用を強化するものと期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-genai-prompt.md](#item-384bf9) | minor update | 記事の更新: GenAIプロンプトスキルの情報の修正 | modified | 5 | 3 | 8 | 
| [enrichment-cache-how-to-configure.md](#item-b0ae0b) | minor update | キャッシュ設定に関する情報の更新 | modified | 10 | 10 | 20 | 
| [enrichment-cache-how-to-manage.md](#item-a972bd) | minor update | キャッシュ管理に関する情報の更新 | modified | 12 | 12 | 24 | 
| [hybrid-search-how-to-query.md](#item-345ce6) | minor update | ハイブリッド検索クエリに関する情報の更新 | modified | 13 | 11 | 24 | 
| [hybrid-search-ranking.md](#item-dad887) | minor update | ハイブリッド検索のランキングに関する情報の更新 | modified | 5 | 5 | 10 | 
| [agentic-retrieval-csharp.md](#item-f93ed3) | minor update | エージェントリトリーバルに関するC#クイックスタートの更新 | modified | 4 | 2 | 6 | 
| [agentic-retrieval-java.md](#item-4e2c55) | minor update | エージェントリトリーバルに関するJavaクイックスタートの更新 | modified | 5 | 1 | 6 | 
| [agentic-retrieval-javascript.md](#item-715283) | minor update | エージェントリトリーバルに関するJavaScriptクイックスタートの更新 | modified | 5 | 1 | 6 | 
| [agentic-retrieval-python.md](#item-efee6a) | minor update | エージェントリトリーバルに関するPythonクイックスタートの更新 | modified | 4 | 1 | 5 | 
| [agentic-retrieval-rest.md](#item-3df373) | breaking change | エージェントリトリーバルに関するRESTクイックスタートの大幅な更新 | modified | 215 | 158 | 373 | 
| [agentic-retrieval-setup.md](#item-e5e297) | minor update | エージェントリトリーバルのセットアップガイドの更新 | modified | 57 | 43 | 100 | 
| [agentic-retrieval-typescript.md](#item-e6370b) | minor update | エージェントリトリーバルのTypeScriptクイックスタートの更新 | modified | 5 | 1 | 6 | 
| [search-get-started-rag-rest.md](#item-aa7f2b) | minor update | RAG REST APIを用いた検索のクイックスタートの更新 | modified | 2 | 2 | 4 | 
| [semantic-ranker-rest.md](#item-d74861) | minor update | セマンティックランカーのREST APIクイックスタートの更新 | modified | 7 | 7 | 14 | 
| [index-similarity-and-scoring.md](#item-75603d) | minor update | インデックスの類似性とスコアリングドキュメントの更新 | modified | 3 | 3 | 6 | 
| [knowledge-store-concept-intro.md](#item-7475c2) | minor update | ナレッジストアの概念紹介ドキュメントの更新 | modified | 4 | 1 | 5 | 
| [knowledge-store-connect-power-bi.md](#item-7ad25a) | minor update | Power BIとのナレッジストア接続に関するドキュメントの更新 | modified | 4 | 1 | 5 | 
| [knowledge-store-create-portal.md](#item-9b92e5) | minor update | Azureポータルでのナレッジストア作成に関するクイックスタートの更新 | modified | 4 | 1 | 5 | 
| [knowledge-store-create-rest.md](#item-2643dd) | minor update | RESTを使用したナレッジストア作成に関するドキュメントの更新 | modified | 4 | 1 | 5 | 
| [knowledge-store-projection-example-long.md](#item-e18999) | minor update | ナレッジストアにおけるプロジェクションの例の更新 | modified | 4 | 1 | 5 | 
| [knowledge-store-projection-overview.md](#item-81aa4a) | minor update | ナレッジストアプロジェクションの概要に関するドキュメントの更新 | modified | 4 | 1 | 5 | 
| [knowledge-store-projection-shape.md](#item-2e47a8) | minor update | ナレッジストアプロジェクションシェイプに関するドキュメントの更新 | modified | 4 | 1 | 5 | 
| [knowledge-store-projections-examples.md](#item-9bfff5) | minor update | ナレッジストアのプロジェクション例に関するドキュメントの更新 | modified | 4 | 1 | 5 | 
| [search-agentic-retrieval-concept.md](#item-797a22) | minor update | エージェンティックリトリーバルに関するコンセプトドキュメントの更新 | modified | 16 | 10 | 26 | 
| [search-agentic-retrieval-how-to-create.md](#item-310fbe) | breaking change | ナレッジエージェントの作成に関するドキュメントの更新 | modified | 128 | 45 | 173 | 
| [search-agentic-retrieval-how-to-index.md](#item-a078ea) | minor update | エージェンティックリトリーバルのためのインデックス設計に関するドキュメント更新 | modified | 20 | 8 | 28 | 
| [search-agentic-retrieval-how-to-migrate.md](#item-4011b8) | new feature | エージェンティックリトリーバルコードの移行に関する新しいドキュメント | added | 192 | 0 | 192 | 
| [search-agentic-retrieval-how-to-pipeline.md](#item-1ad1c3) | minor update | エージェンティックリトリーバルパイプラインに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [search-agentic-retrieval-how-to-retrieve.md](#item-5f7fc0) | minor update | エージェンティックリトリーバルによるデータ取得に関するドキュメントの更新 | modified | 11 | 7 | 18 | 
| [search-agentic-retrieval-how-to-synthesize.md](#item-18668b) | new feature | Azure AI Searchにおける回答合成の構成に関する新しいドキュメント | added | 150 | 0 | 150 | 
| [search-api-migration.md](#item-07297b) | minor update | Azure AI SearchのAPI移行ガイドの更新 | modified | 16 | 3 | 19 | 
| [search-api-preview.md](#item-511f5d) | minor update | Azure AI Searchのプレビュー機能に関するドキュメントの更新 | modified | 13 | 9 | 22 | 
| [search-blob-indexer-role-based-access.md](#item-887e42) | minor update | Azure Blob IndexerのRBACに関するドキュメントの更新 | modified | 27 | 9 | 36 | 
| [search-document-level-access-overview.md](#item-4bb055) | minor update | ドキュメントレベルアクセス制御の概要に関する更新 | modified | 8 | 8 | 16 | 
| [search-get-started-agentic-retrieval.md](#item-4a40f4) | minor update | エージェント探索のクイックスタートガイドのタイトル変更 | modified | 4 | 4 | 8 | 
| [search-how-to-alias.md](#item-3a72bc) | minor update | Azure AI Searchのエイリアスに関するドキュメントの更新 | modified | 8 | 8 | 16 | 
| [search-how-to-create-search-index.md](#item-c4ff31) | minor update | Azure AI Searchインデックス作成に関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [search-how-to-index-logic-apps-indexers.md](#item-64a12e) | minor update | Azure Logic Appsインデクサーに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [search-how-to-index-markdown-blobs.md](#item-c94a20) | minor update | Markdown Blobのインデクシングに関するドキュメントの更新 | modified | 4 | 4 | 8 | 
| [search-how-to-managed-identities.md](#item-3536f2) | minor update | マネージドIDに関するドキュメントの更新 | modified | 3 | 3 | 6 | 
| [search-howto-index-mysql.md](#item-5d31c4) | minor update | MySQLインデクシングに関するドキュメントの更新 | modified | 6 | 6 | 12 | 
| [search-howto-index-sharepoint-online.md](#item-49ff6e) | minor update | SharePoint Onlineインデクシングに関するドキュメントの更新 | modified | 21 | 21 | 42 | 
| [search-howto-managed-identities-cosmos-db.md](#item-a74464) | minor update | Cosmos DBにおけるマネージドIDの使用に関するドキュメントの更新 | modified | 4 | 4 | 8 | 
| [search-howto-managed-identities-sql.md](#item-2af8aa) | minor update | SQLにおけるマネージドIDの使用に関するドキュメントの更新 | modified | 3 | 3 | 6 | 
| [search-howto-managed-identities-storage.md](#item-8209c4) | minor update | ストレージにおけるマネージドIDの使用に関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [search-howto-reindex.md](#item-46738a) | minor update | 再インデックス作業に関するドキュメントの更新 | modified | 3 | 3 | 6 | 
| [search-howto-run-reset-indexers.md](#item-fb10c8) | minor update | インデクサーのリセットに関するドキュメントの更新 | modified | 38 | 7 | 45 | 
| [search-index-access-control-lists-and-rbac-push-api.md](#item-45e71e) | minor update | インデックスアクセス制御リストとRBACに関するドキュメントの更新 | modified | 11 | 7 | 18 | 
| [search-indexer-access-control-lists-and-role-based-access.md](#item-67b42f) | minor update | インデクサーのアクセス制御リストとRBACに関するドキュメントの更新 | modified | 5 | 6 | 11 | 
| [search-knowledge-source-how-to-blob.md](#item-58d84a) | new feature | Blobナレッジソースの作成に関する新規ドキュメント | added | 242 | 0 | 242 | 
| [search-knowledge-source-how-to-index.md](#item-fb0876) | new feature | 検索インデックスナレッジソースの作成に関する新規ドキュメント | added | 138 | 0 | 138 | 
| [search-knowledge-source-overview.md](#item-1969d3) | new feature | ナレッジソース概要に関する新規ドキュメント | added | 117 | 0 | 117 | 
| [search-query-access-control-rbac-enforcement.md](#item-d24df7) | minor update | アクセス制御とRBAC施行に関する日付とAPIバージョンの更新 | modified | 3 | 3 | 6 | 
| [search-relevance-overview.md](#item-cb0e09) | minor update | 検索関連性概要の更新日付とAPIバージョンの変更 | modified | 2 | 2 | 4 | 
| [semantic-code-migration.md](#item-ad1ba7) | minor update | セマンティックコード移行の更新日付とAPIバージョンの追加 | modified | 2 | 1 | 3 | 
| [semantic-how-to-enable-scoring-profiles.md](#item-e8d524) | minor update | スコアリングプロファイルの有効化に関するドキュメントの日付とAPIバージョンの更新 | modified | 6 | 6 | 12 | 
| [speller-how-to-add.md](#item-9b4502) | minor update | スペラ―の追加に関するドキュメントの日付とAPIバージョンの更新 | modified | 6 | 6 | 12 | 
| [toc.yml](#item-c4768f) | minor update | TOCの項目名の変更と新しいリンクの追加 | modified | 16 | 6 | 22 | 
| [tutorial-adls-gen2-indexer-acls.md](#item-6881a0) | minor update | ACLインデキサーに関するチュートリアルの日付とAPIバージョンの更新 | modified | 4 | 4 | 8 | 
| [tutorial-document-extraction-image-verbalization.md](#item-398a90) | minor update | 文書抽出画像の可視化に関するチュートリアルの日付とAPIバージョンの更新 | modified | 13 | 13 | 26 | 
| [tutorial-document-extraction-multimodal-embeddings.md](#item-a3db59) | minor update | マルチモーダル埋め込みの文書抽出に関するチュートリアルの日付とAPIバージョンの更新 | modified | 13 | 13 | 26 | 
| [tutorial-document-layout-image-verbalization.md](#item-f5de57) | minor update | 文書レイアウト画像の可視化に関するチュートリアルの日付とAPIバージョンの更新 | modified | 13 | 13 | 26 | 
| [tutorial-document-layout-multimodal-embeddings.md](#item-f67371) | minor update | マルチモーダル埋め込みの文書レイアウトに関するチュートリアルの日付とAPIバージョンの更新 | modified | 13 | 13 | 26 | 
| [vector-search-filters.md](#item-f47c2b) | minor update | ベクトル検索フィルターに関するチュートリアルの更新 | modified | 71 | 88 | 159 | 
| [vector-search-how-to-create-index.md](#item-97c769) | minor update | ベクトルインデックスの作成方法に関するチュートリアルの更新 | modified | 3 | 3 | 6 | 
| [vector-search-multi-vector-fields.md](#item-9aa482) | minor update | マルチベクトルフィールドのサポートに関するドキュメントの更新 | modified | 4 | 4 | 8 | 
| [vector-store.md](#item-db9b8c) | minor update | ベクトルストレージに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [whats-new.md](#item-fa71b4) | minor update | 最新機能に関するアップデートの追加 | modified | 16 | 2 | 18 | 


# Modified Contents
## articles/search/cognitive-search-skill-genai-prompt.md{#item-384bf9}

<details>
<summary>Diff</summary>
````diff
@@ -8,14 +8,14 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2025
 ms.topic: reference
-ms.date: 07/28/2025
+ms.date: 08/27/2025
 ---
 
 # GenAI Prompt skill
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-The **GenAI (Generative AI) Prompt** skill executes a *chat completion* request against a Large Language Model (LLM) deployed in Azure AI Foundry or Azure OpenAI in Azure AI Foundry Models. Use this capability to create new information that can be indexed and stored as searchable content.
+The **GenAI (Generative AI) Prompt** skill executes a *chat completion* request against a large language model (LLM) deployed in Azure AI Foundry or Azure OpenAI in Azure AI Foundry Models. Use this capability to create new information that can be indexed and stored as searchable content.
 
 Here are some examples of how the GenAI prompt skill can help you create content:
 
@@ -24,7 +24,7 @@ Here are some examples of how the GenAI prompt skill can help you create content
 - Simplify complex content
 - Perform any other task that you can articulate in a prompt
 
-The GenAI Prompt skill is available in the [2025-05-01-preview REST API](/rest/api/searchservice/skillsets/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true) only. The skill supports text, image, and multimodal content such as a PDF that contains text and images. 
+The GenAI Prompt skill is available in the [latest preview REST API](/rest/api/searchservice/skillsets/create?view=rest-searchservice-2025-08-01-preview&preserve-view=true). This skill supports text, image, and multimodal content, such as a PDF that contains text and images.
 
 > [!TIP]
 > It's common to use this skill combined with a data chunking skill. The following tutorials demonstrate image verbalization with two different data chunking techniques:
@@ -37,6 +37,8 @@ The GenAI Prompt skill is available in the [2025-05-01-preview REST API](/rest/a
 
 You can use any [chat completion inference model](/azure/ai-foundry/model-inference/concepts/models) deployed in AI Foundry, such as GPT models, Deepseek R#, Llama-4-Mavericj, Cohere-command-r, and so forth.
 
+For image verbalization, the model you use to analyze the image determines what image formats are supported.
+
 Billing is based on the pricing of the model you use.
 
 > [!NOTE]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事の更新: GenAIプロンプトスキルの情報の修正"
}
```

### Explanation
この修正は、`cognitive-search-skill-genai-prompt.md`というドキュメントに対するマイナーアップデートです。主な変更点は、日付の更新や文中の用語の小さな改善を含んでいます。具体的には、`ms.date`が「2025年5月1日プレビュー」から「最新のプレビューレストAPI」に変更され、また「large language model」という表現における大文字と小文字の調整が行われました。

この変更により、文書の情報が最新の状態に保たれ、読者にとって分かりやすく保持されています。内容に関しても、GenAIプロンプトスキルの機能や使い方について明確な説明が提供されており、よりスムーズに利用できるようになっています。また、画像の分析に関する情報や、モデルの使用による請求についての注意書きも追加されており、読者にとっての利便性が向上しています。

## articles/search/enrichment-cache-how-to-configure.md{#item-b0ae0b}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/28/2025
+ms.date: 08/27/2025
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
@@ -55,10 +55,10 @@ You can use the Azure portal, preview APIs, or preview Azure SDK packages to ena
 
 On new indexers, add the `cache` property in the indexer definition payload when calling Create or Update Indexer. 
 
-We recommend the latest preview for [Create or Update Indexer (2025-05-01-preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
+We recommend the latest preview REST API for [Create or Update Indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true).
 
 ```https
-POST https://[service name].search.windows.net/indexers?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/indexers?api-version=2025-08-01-preview
     {
         "name": "<YOUR-INDEXER-NAME>",
         "targetIndexName": "<YOUR-INDEX-NAME>",
@@ -82,10 +82,10 @@ For existing indexers that already have a skillset, use the following steps to a
 
 ### Step 1: Get the indexer definition
 
-Start with a valid, work indexer that has these components: data source, skillset, index. Using an API client, send a [GET Indexer](/rest/api/searchservice/indexers/get?view=rest-searchservice-2025-05-01-preview&preserve-view=true) request to retrieve the indexer. When you use the preview API version to the GET the indexer, a `cache` property set to null is added to the definition automatically.
+Start with a valid, work indexer that has these components: data source, skillset, index. Using an API client, send a [GET Indexer](/rest/api/searchservice/indexers/get?view=rest-searchservice-2025-08-01-preview&preserve-view=true) request to retrieve the indexer. When you use the preview API version to the GET the indexer, a `cache` property set to null is added to the definition automatically.
 
 ```http
-GET https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]?api-version=2025-05-01-preview
+GET https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]?api-version=2025-08-01-preview
     Content-Type: application/json
     api-key: [YOUR-ADMIN-KEY]
 ```
@@ -98,7 +98,7 @@ In the index definition, modify `cache` to include the following required and op
 + (Optional) `enableReprocessing` boolean property (`true` by default), indicates that incremental enrichment is enabled. Set to `false` if you want to suspend incremental processing while other resource-intensive operations, such as indexing new documents, are underway and then switch back to `true` later.
 
 ```http
-POST https://[service name].search.windows.net/indexers?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/indexers?api-version=2025-08-01-preview
     {
         "name": "<YOUR-INDEXER-NAME>",
         "targetIndexName": "<YOUR-INDEX-NAME>",
@@ -119,17 +119,17 @@ POST https://[service name].search.windows.net/indexers?api-version=2025-05-01-p
 [Reset Indexer](/rest/api/searchservice/indexers/reset) is required when setting up incremental enrichment for existing indexers to ensure all documents are in a consistent state. You can use the Azure portal or an API client for this task.
 
 ```https
-POST https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]/reset?api-version=2025-05-01-preview
+POST https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]/reset?api-version=2025-08-01-preview
     Content-Type: application/json
     api-key: [YOUR-ADMIN-KEY]
 ```
 
 ### Step 4: Save the indexer
 
-[Update Indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) with a PUT request, where the body of the request includes `cache`.
+[Update Indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) with a PUT request, where the body of the request includes `cache`.
 
 ```http
-PUT https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]?api-version=2025-05-01-preview
+PUT https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]?api-version=2025-08-01-preview
     Content-Type: application/json
     api-key: [YOUR-ADMIN-KEY]
     {
@@ -159,7 +159,7 @@ To run indexer, you can use the Azure portal or the API. In the Azure portal, fr
 Alternatively, you can use REST to [run the indexer](/rest/api/searchservice/indexers/run):
 
 ```http
-POST https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]/run?api-version=2025-05-01-preview
+POST https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]/run?api-version=2025-08-01-preview
 Content-Type: application/json
 api-key: [YOUR-ADMIN-KEY]
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "キャッシュ設定に関する情報の更新"
}
```

### Explanation
この差分は、`enrichment-cache-how-to-configure.md`というドキュメントに対するマイナーアップデートを示しています。主な更新内容は、日付の変更とREST APIのバージョン番号の更新です。具体的には、`ms.date`が「2025年7月28日」から「2025年8月27日」に変更され、APIのエンドポイントにおけるバージョンも「2025-05-01-preview」から「2025-08-01-preview」に更新されています。

この変更により、ドキュメントは最新のAPIバージョンを反映する形となり、読者が最新の情報に基づいて操作を行えるようになります。また、キャッシュプロパティに関連する設定方法や手順についても整然とした説明が続き、特にGETリクエストやPOSTリクエストにおけるエンドポイントの正しい使用を促す内容が強調されています。

さらに、インクリメンタルエンリッチメントの設定に関する注意事項や推奨手順も含まれており、ユーザーにとって役立つ情報が充実しています。これにより、AzureポータルやAPIを使用した設定手順がより明確に理解できるようになっています。

## articles/search/enrichment-cache-how-to-manage.md{#item-a972bd}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/28/2025
+ms.date: 08/27/2025
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
@@ -43,10 +43,10 @@ The cache is created when you specify the "cache" property and run the indexer.
 
 The following example illustrates an indexer with caching enabled. See [Configure enrichment caching](enrichment-cache-how-to-configure.md) for full instructions. 
 
-To set the cache property, use a preview REST API [Create or Update Indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) or a preview Azure SDK package that provides the feature. You can also enable enrichment caching in the Import data wizard in the Azure portal.
+To set the cache property, use latest preview REST API for [Create or Update Indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) or a preview Azure SDK package that provides the feature. You can also enable enrichment caching in the Import data wizard in the Azure portal.
 
 ```json
-POST https://[YOUR-SEARCH-SERVICE-NAME].search.windows.net/indexers?api-version=2025-05-01-preview
+POST https://[YOUR-SEARCH-SERVICE-NAME].search.windows.net/indexers?api-version=2025-08-01-preview
     {
         "name": "myIndexerName",
         "targetIndexName": "myIndex",
@@ -96,7 +96,7 @@ If you know that a change to the skill is indeed superficial, you should overrid
 Setting this parameter ensures that only updates to the skillset definition are committed and the change isn't evaluated for effects on the existing cache. Use a preview API version, 2020-06-30-Preview or later. We recommend the latest preview API.
 
 ```http
-PUT https://[servicename].search.windows.net/skillsets/[skillset name]?api-version=2025-05-01-preview&disableCacheReprocessingChangeDetection
+PUT https://[servicename].search.windows.net/skillsets/[skillset name]?api-version=2025-08-01-preview&disableCacheReprocessingChangeDetection
   
 ```
 
@@ -107,7 +107,7 @@ PUT https://[servicename].search.windows.net/skillsets/[skillset name]?api-versi
 Most changes to a data source definition will invalidate the cache. However, for scenarios where you know that a change shouldn't invalidate the cache - such as changing a connection string or rotating the key on the storage account - append the `ignoreResetRequirement` parameter on the [data source update](/rest/api/searchservice/data-sources/create-or-update). Setting this parameter to true allows the commit to go through, without triggering a reset condition that would result in all objects being rebuilt and populated from scratch.
 
 ```http
-PUT https://[search service].search.windows.net/datasources/[data source name]?api-version=2025-05-01-preview&ignoreResetRequirement
+PUT https://[search service].search.windows.net/datasources/[data source name]?api-version=2025-08-01-preview&ignoreResetRequirement
  
 ```
 
@@ -117,13 +117,13 @@ PUT https://[search service].search.windows.net/datasources/[data source name]?a
 
 The purpose of the cache is to avoid unnecessary processing, but suppose you make a change to a skill that the indexer doesn't detect (for example, changing something in external code, such as a custom skill).
 
-In this case, you can use the [Reset Skills](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2025-05-01-preview&preserve-view=true) to force reprocessing of a particular skill, including any downstream skills that have a dependency on that skill's output. This API accepts a POST request with a list of skills that should be invalidated and marked for reprocessing. After Reset Skills, follow with a [Run Indexer](/rest/api/searchservice/indexers/run) request to invoke the pipeline processing.
+In this case, you can use the [Reset Skills](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2025-08-01-preview&preserve-view=true) to force reprocessing of a particular skill, including any downstream skills that have a dependency on that skill's output. This API accepts a POST request with a list of skills that should be invalidated and marked for reprocessing. After Reset Skills, follow with a [Run Indexer](/rest/api/searchservice/indexers/run) request to invoke the pipeline processing.
 
 ## Re-cache specific documents
 
 [Resetting an indexer](/rest/api/searchservice/indexers/reset) will result in all documents in the search corpus being reprocessed. 
 
-In scenarios where only a few documents need to be reprocessed, use [Reset Documents (preview)](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2025-05-01-preview&preserve-view=true) to force reprocessing of specific documents. When a document is reset, the indexer invalidates the cache for that document, which is then reprocessed by reading it from the data source. For more information, see [Run or reset indexers, skills, and documents](search-howto-run-reset-indexers.md).
+In scenarios where only a few documents need to be reprocessed, use [Reset Documents (preview)](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2025-08-01-preview&preserve-view=true) to force reprocessing of specific documents. When a document is reset, the indexer invalidates the cache for that document, which is then reprocessed by reading it from the data source. For more information, see [Run or reset indexers, skills, and documents](search-howto-run-reset-indexers.md).
 
 To reset specific documents, the request provides a list of document keys as read from the search index. If the key is mapped to a field in the external data source, the value that you provide should be the one used in the search index.
 
@@ -138,7 +138,7 @@ Depending on how you call the API, the request will either append, overwrite, or
 The following example illustrates a reset document request:
 
 ```http
-POST https://[search service name].search.windows.net/indexers/[indexer name]/resetdocs?api-version=2025-05-01-preview
+POST https://[search service name].search.windows.net/indexers/[indexer name]/resetdocs?api-version=2025-08-01-preview
     {
         "documentKeys" : [
             "key1",
@@ -189,10 +189,10 @@ Preview APIs provide extra properties on indexers. We recommend the latest previ
 
 Skillsets and data sources can use the generally available version. In addition to the reference documentation, see  [Configure caching for incremental enrichment](enrichment-cache-how-to-configure.md) for details about order of operations.
 
-+ [Create or Update Indexer (api-version=2025-05-01-preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) 
++ [Create or Update Indexer (api-version=2025-08-01-preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) 
 
-+ [Reset Skills (api-version=2025-05-01-preview)](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2025-05-01-preview&preserve-view=true)
++ [Reset Skills (api-version=2025-08-01-preview)](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2025-08-01-preview&preserve-view=true)
 
-+ [Create or Update Skillset (api-version=2025-05-01-preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) (New URI parameter on the request)
++ [Create or Update Skillset (api-version=2025-08-01-preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) (New URI parameter on the request)
 
-+ [Create or Update Data Source (api-version=2025-05-01-preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true), when called with a preview API version, provides a new parameter named "ignoreResetRequirement", which should be set to true when your update action shouldn't invalidate the cache. Use "ignoreResetRequirement" sparingly as it could lead to unintended inconsistency in your data that won't be detected easily.
++ [Create or Update Data Source (api-version=2025-08-01-preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true), when called with a preview API version, provides a new parameter named "ignoreResetRequirement", which should be set to true when your update action shouldn't invalidate the cache. Use "ignoreResetRequirement" sparingly as it could lead to unintended inconsistency in your data that won't be detected easily.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "キャッシュ管理に関する情報の更新"
}
```

### Explanation
この修正は、`enrichment-cache-how-to-manage.md`というドキュメントに対するマイナーアップデートを示しています。主な変更点は、日付の更新とREST APIのバージョン番号の調整です。具体的には、従来の「2025-05-01-preview」から「2025-08-01-preview」への移行が行われています。この更新により、読者は最新のAPIバージョンに基づいた情報を参照できるようになっています。

本文の変更内容では、キャッシュの設定に関する手順や、スキルが変化した際のキャッシュ管理方法について詳しく説明されています。例えば、キャッシュプロパティを設定する際のAPIエンドポイントの最新情報や、スキルセットやデータソースの更新時にキャッシュの無効化を防ぐための新たなパラメータ「ignoreResetRequirement」の使用方法についても言及されています。

また、特定のドキュメントの再処理を行う方法に関する具体例も新たに追加されており、これにより、ユーザーは必要な操作を的確に実施できるようになります。全体として、このアップデートは文書の精度を向上させ、最新の情報提供を通じて利用者の利便性を高めることを目的としています。

## articles/search/hybrid-search-how-to-query.md{#item-345ce6}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 07/21/2025
+ms.date: 08/28/2025
 ---
 
 # Create a hybrid query in Azure AI Search
@@ -163,12 +163,12 @@ A hybrid query can be tuned to control how much of each subquery contributes to
 
 If you use `maxTextRecallSize`, you might also want to set `CountAndFacetMode`. This parameter determines whether the `count` and `facets` should include all documents that matched the search query, or only those documents retrieved within the `maxTextRecallSize` window. The default value is "countAllResults".
 
-We recommend the latest preview REST API version [2025-05-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&preserve-view=true) for setting these options.
+We recommend the [latest preview REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-08-01-preview&preserve-view=true) for setting these options.
 
 > [!TIP]
 > Another approach for hybrid query tuning is [vector weighting](vector-search-how-to-query.md#vector-weighting), used to increase the importance of vector queries in the request.
 
-1. Use [Search - POST (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&preserve-view=true) or [Search - GET (preview)](/rest/api/searchservice/documents/search-get?view=rest-searchservice-2025-05-01-preview&preserve-view=true) to specify preview parameters.
+1. Use [Search - POST (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-08-01-preview&preserve-view=true) or [Search - GET (preview)](/rest/api/searchservice/documents/search-get?view=rest-searchservice-2025-08-01-preview&preserve-view=true) to specify preview parameters.
 
 1. Add a `hybridSearch` query parameter object to set the maximum number of documents recalled through the BM25-ranked results of a hybrid query. It has two properties:
 
@@ -259,7 +259,7 @@ api-key: {{admin-api-key}}
         }
     ],
     "search": "historic hotel walk to restaurants and shopping",
-    "vectorFilterMode": "postFilter",
+    "vectorFilterMode": "preFilter",
     "filter": "ParkingIncluded",
     "top": "10"
 }
@@ -269,28 +269,28 @@ api-key: {{admin-api-key}}
 
 + Filters are applied to the content of filterable fields. In this example, the ParkingIncluded field is a boolean and it's marked as `filterable` in the index schema.
 
-+ In hybrid queries, filters can be applied before query execution to reduce the query surface, or after query execution to trim results. `"preFilter"` is the default. To use `postFilter`, set the [filter processing mode](vector-search-filters.md) as shown in this example.
++ In hybrid queries, filters can be applied before query execution to reduce the query surface or after query execution to trim results. `"preFilter"` is the default. To use `postFilter` or `strictPostFilter` (preview), set the [filter processing mode](vector-search-filters.md) as shown in this example.
 
 + When you postfilter query results, the number of results might be less than top-n.
 
 ### Example: Hybrid search with filters targeting vector subqueries (preview)
 
-Using a [preview API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&preserve-view=true), you can override a global filter on the search request by applying a secondary filter that targets just the vector subqueries in a hybrid request.
+Using the [latest preview REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-08-01-preview&preserve-view=true), you can override a global filter on the search request by applying a secondary filter that targets just the vector subqueries in a hybrid request.
 
 This feature provides fine-grained control by ensuring that filters only influence the vector search results, leaving keyword-based search results unaffected. 
 
 The targeted filter fully overrides the global filter, including any filters used for [security trimming](search-security-trimming-for-azure-search.md) or geospatial search.  In cases where global filters are required, such as security trimming, you must explicitly include these filters in both the top-level filter and in each vector-level filter to ensure security and other constraints are consistently enforced.
 
 To apply targeted vector filters:
 
-+ Use the [latest preview Search Documents REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&preserve-view=true#request-body) or an Azure SDK beta package that provides the feature.
++ Use the [latest preview Search Documents REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-08-01-preview&preserve-view=true#request-body) or an Azure SDK beta package that provides the feature.
 
 + Modify a query request, adding a new `vectorQueries.filterOverride` parameter set to an [OData filter expression](search-query-odata-filter.md).
 
 Here's an example of hybrid query that adds a filter override. The global filter "Rating gt 3" is replaced at run time by the `filterOverride`.
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2025-05-01=preview
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2025-08-01-preview
 
 {
     "vectorQueries": [
@@ -390,7 +390,7 @@ api-key: {{admin-api-key}}
     "captions": "extractive",
     "answers": "extractive",
     "filter": "ParkingIsIncluded'",
-    "vectorFilterMode": "postFilter",
+    "vectorFilterMode": "preFilter",
     "top": "50"
 }
 ```
@@ -399,9 +399,11 @@ api-key: {{admin-api-key}}
 
 + The filter mode can affect the number of results available to the semantic reranker. As a best practice, it's smart to give the semantic ranker the maximum number of documents (50). If prefilters or postfilters are too selective, you might be underserving the semantic ranker by giving it fewer than 50 documents to work with.
 
-+ Prefiltering is applied before query execution. If prefilter reduces the search area to 100 documents, the vector query executes over the "DescriptionVector" field for those 100 documents, returning the k=50 best matches. Those 50 matching documents then pass to RRF for merged results, and then to semantic ranker.
++ `preFilter` is applied before query execution. If prefilter reduces the search area to 100 documents, the vector query executes over the `DescriptionVector` field for those 100 documents, returning the k=50 best matches. Those 50 matching documents then pass to RRF for merged results, and then to semantic ranker.
 
-+ Postfilter is applied after query execution. If k=50 returns 50 matches on the vector query side, followed by a post-filter applied to the 50 matches, your results are reduced by the number of documents that meet filter criteria. This leaves you with fewer than 50 documents to pass to semantic ranker. Keep this in mind if you're using semantic ranking. The semantic ranker works best if it has 50 documents as input.
++ `postFilter` is applied after query execution. If k=50 returns 50 matches on the vector query side, followed by a post-filter applied to the 50 matches, your results are reduced by the number of documents that meet filter criteria. This leaves you with fewer than 50 documents to pass to semantic ranker. Keep this in mind if you're using semantic ranking. The semantic ranker works best if it has 50 documents as input.
+
++ `strictPostFilter` (preview) is applied on the unfiltered top-`k` results after query execution. It always returns less than or equal to `k` documents. If the unfiltered k=50 returns 50 unfiltered results, and the filter matches 30 documents, only 30 documents are returned in the result set, even if the index has more than 30 documents that match the filter. Since this mode has the greatest reduction in recall, we don't recommend that you use it with semantic ranker.
 
 ## Configure a query response
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索クエリに関する情報の更新"
}
```

### Explanation
この修正は、`hybrid-search-how-to-query.md`というドキュメントに対するマイナーアップデートを示しています。主な変更ポイントには、日付の更新と、REST APIのバージョン番号の変更が含まれています。具体的には、推奨されるAPIバージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新されており、最新の機能やオプションを使用するための情報が提供されています。

文書中では、ハイブリッドクエリの設定に関する具体的な手順や、フィルタリングオプションの適用方法についての説明が強化されています。特に、`vectorFilterMode`のデフォルト設定の変更や、`preFilter`と`postFilter`の適切な使用方法について詳しく解説されており、クエリの効率を高めるための重要な設定に焦点が当てられています。

また、フィルタリングの力を利用して、検索結果に対する影響を制御する方法が示されており、ユーザーはクエリの結果を最適化し、必要に応じてフィルタを適用することで、求めるデータにより簡単にアクセスできるようになります。これにより、ハイブリッド検索機能の実用性が向上し、浸透性のある検索体験が提供されることが期待されます。

## articles/search/hybrid-search-ranking.md{#item-dad887}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 07/21/2025
+ms.date: 08/27/2025
 ---
 
 # Relevance scoring in hybrid search using Reciprocal Rank Fusion (RRF)
@@ -18,7 +18,7 @@ Reciprocal Rank Fusion (RRF) is an algorithm that evaluates the search scores fr
 RRF is based on the concept of *reciprocal rank*, which is the inverse of the rank of the first relevant document in a list of search results. The goal of the technique is to take into account the position of the items in the original rankings, and give higher importance to items that are ranked higher in multiple lists. This can help improve the overall quality and reliability of the final ranking, making it more useful for the task of fusing multiple ordered search results.
 
 > [!NOTE]
-> [Preview APIs](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&preserve-view=true) can deconstruct an RRF-ranked search score into its component subscores. This gives you transparency into all-up score composition. For more information, see [unpack search scores (preview)](#unpack-a-search-score-into-subscores-preview) in this article.
+> The [latest preview REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-08-01-preview&preserve-view=true) can deconstruct an RRF-ranked search score into its component subscores. This gives you transparency into all-up score composition. For more information, see [Unpack search scores (preview)](#unpack-a-search-score-into-subscores-preview) in this article.
 
 ## How RRF ranking works
 
@@ -61,20 +61,20 @@ Semantic ranking occurs after RRF merging of results. Its score (`@search.rerank
 
 ## Unpack a search score into subscores (preview)
 
-Using the [latest preview API version](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&preserve-view=true), you can deconstruct a search score to view its subscores.
+Using the [latest preview REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-08-01-preview&preserve-view=true), you can deconstruct a search score to view its subscores.
 
 For vector queries, this information can help you determine an appropriate value for [vector weighting](vector-search-how-to-query.md#vector-weighting) or [setting minimum thresholds](vector-search-how-to-query.md#set-thresholds-to-exclude-low-scoring-results-preview).
 
 To get subscores:
 
-+ Use the [latest preview Search Documents REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&preserve-view=true#request-body) or an Azure SDK beta package that provides the feature.
++ Use the [latest preview Search Documents REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-08-01-preview&preserve-view=true#request-body) or an Azure SDK beta package that provides the feature.
 
 + Modify a query request, adding a new `debug` parameter set to either `vector`, `semantic` if using semantic ranker, or `all`.
 
 Here's an example of hybrid query that returns subscores in debug mode:
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2025-05-01=preview
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2025-08-01-preview
 
 {
     "vectorQueries": [
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索のランキングに関する情報の更新"
}
```

### Explanation
この修正は、`hybrid-search-ranking.md`というドキュメントに対するマイナーアップデートを示しています。変更の主なポイントには、日付の更新と、REST APIのバージョン番号の変更が含まれています。具体的には、以前の「2025-05-01-preview」から「2025-08-01-preview」へと、推奨されるAPIのバージョンが最新のものに更新されています。

文書は、相互ランキング融合（RRF）を用いたハイブリッド検索における関連スコアリングについて詳述しています。RRFアルゴリズムによって、複数の検索結果からの評価スコアを効率的に融合し、全体のランク付け品質を向上させることを目的としています。また、更新された内容では、最新のAPIを使用することで、RRFランク付けされた検索スコアを構成要素に分解し、それぞれの評価スコアを確認する方法が具体的に説明されています。

さらに、新しいデバッグパラメータの追加により、ユーザーはセマンティックランカーを使用する際に、検索結果の詳細な情報にアクセスし、より適切な重み付けを設定する手助けとなる情報を得ることができます。この変更により、ユーザーはハイブリッド検索の機能を最大限に活用するための新しい手段を得ることになります。全体として、ドキュメントの精度と信頼性が向上し、利用者にとっての利便性が高まることが期待されています。

## articles/search/includes/quickstarts/agentic-retrieval-csharp.md{#item-f93ed3}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 6/24/2025
+ms.date: 08/28/2025
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -13,8 +13,10 @@ In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-c
 
 Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
+To get started with a Jupyter notebook instead, see the [Azure-Samples/azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) repository on GitHub.
+
 > [!TIP]
-> To get started with a Jupyter notebook instead, see the [Azure-Samples/azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-agentic-retrieval) repository on GitHub.
+> The C# version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST version of this quickstart.
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するC#クイックスタートの更新"
}
```

### Explanation
この修正は、`agentic-retrieval-csharp.md`というC#クイックスタートガイドに対するマイナーアップデートを示しています。主な変更内容には、更新された日付の反映と、さらなる情報を提供するためのテキストの追加が含まれます。具体的には、ドキュメントの日付が「2025年6月24日」から「2025年8月28日」に更新されています。

更新されたテキストでは、まずJupyterノートブックを使用して開始する方法に関するリンクが追加され、ユーザーはGitHubのリポジトリに直接アクセスできるようになっています。さらに、現行のC#クイックスタートが使用しているAPIバージョン「2025-05-01-preview」には、知識ソースや他のエージェントリトリーバル機能がサポートされていないことが明記されています。これにより、ユーザーは新機能を利用するために別のクイックスタートのバージョンを参照する必要があることを理解できます。

全体として、この修正は一般的な理解を深め、利用者にとっての利便性を高めるために必要な情報を提供しています。また、APIのバージョンに関する明確な指示により、ユーザーは最適な体験を得るための適切なリソースを選択できるようになります。

## articles/search/includes/quickstarts/agentic-retrieval-java.md{#item-4e2c55}

<details>
<summary>Diff</summary>
````diff
@@ -4,14 +4,18 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 7/21/2025
+ms.date: 08/28/2025
 ---
+
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
 
 In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-concept.md) to create a conversational search experience powered by large language models (LLMs) and your proprietary data. Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries in parallel, and extracts grounding data from documents indexed in Azure AI Search. The output is intended for integration with agentic and custom chat solutions.
 
 Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
+> [!TIP]
+> The Java version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST version of this quickstart.
+
 ## Prerequisites
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するJavaクイックスタートの更新"
}
```

### Explanation
この修正は、`agentic-retrieval-java.md`というJavaクイックスタートガイドに対するマイナーアップデートです。主な変更点は、ドキュメントの日付が「2025年7月21日」から「2025年8月28日」に更新されたことと、ユーザーにとって有益な追加情報が含まれたことです。

具体的には、クイックスタートの内容において、エージェントリトリーバルの機能を使用して複雑なユーザーのクエリをサブクエリに分解し、Azure AI Searchにインデックスされた文書から基礎データを抽出する過程が説明されています。また、サンプルJSONドキュメントとしてNASAの「Earth at Night」電子書籍からのデータが使用されていることが記載されています。

さらに、新たに追加された情報として、現在のJavaクイックスタートが利用しているAPIバージョン「2025-05-01-preview」には、知識ソースや新機能がサポートされていないことが記載され、これらの機能を使用するには別のRESTバージョンのクイックスタートを参照する必要があることが注意喚起されています。また、Azureアカウントの作成を促すリンクも加えられています。

これにより、ユーザーは必要なリソースを更に活用しやすくなり、エージェントリトリーバルを用いた検索体験をよりスムーズに実装するための指針が示されています。全体として、この修正はユーザーの理解を深め、クイックスタートの使いやすさを向上させるための重要な情報を提供しています。

## articles/search/includes/quickstarts/agentic-retrieval-javascript.md{#item-715283}

<details>
<summary>Diff</summary>
````diff
@@ -4,14 +4,18 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 7/21/2025
+ms.date: 08/28/2025
 ---
+
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
 
 In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-concept.md) to create a conversational search experience powered by large language models (LLMs) and your proprietary data. Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries in parallel, and extracts grounding data from documents indexed in Azure AI Search. The output is intended for integration with agentic and custom chat solutions.
 
 Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
+> [!TIP]
+> The JavaScript version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST version of this quickstart.
+
 ## Prerequisites
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するJavaScriptクイックスタートの更新"
}
```

### Explanation
この修正は、`agentic-retrieval-javascript.md`というJavaScriptクイックスタートガイドに対するマイナーアップデートです。主な変更点は、ドキュメントの日付が「2025年7月21日」から「2025年8月28日」に更新されたことと、ユーザー向けの重要な追加情報が含まれたことです。

具体的には、このクイックスタートでは、エージェントリトリーバル技術を使用して会話型検索体験を構築する方法が説明されています。この技術は、ユーザーの複雑なクエリをサブクエリに分解し、それらを並行して実行し、Azure AI Searchにインデックスされた文書から基礎データを抽出します。提供される情報は、エージェントリトリーバルやカスタムチャットソリューションと統合することを意図しています。

追加された情報として、JavaScript版のクイックスタートが使用しているAPIバージョン「2025-05-01-preview」には、知識ソースやエージェントリトリーバル機能がサポートされておらず、これらの新機能を利用するには別のRESTバージョンのクイックスタートを参照する必要があることが明記されています。また、Azureアカウントの作成を促すリンクも加えられており、ユーザーが速やかに準備を整える手助けとなっています。

全体として、この修正はユーザーの理解と利便性を向上させ、エージェントリトリーバルを通じた優れた検索体験を提供するためのガイドラインを示しています。

## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 6/24/2025
+ms.date: 08/28/2025
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -15,6 +15,9 @@ Although you can provide your own data, this quickstart uses [sample JSON docume
 
 This quickstart is based on the [Quickstart-Agentic-Retrieval](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Agentic-Retrieval) Jupyter notebook on GitHub.
 
+> [!TIP]
+> The Python version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST version of this quickstart.
+
 ## Prerequisites
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルに関するPythonクイックスタートの更新"
}
```

### Explanation
この修正は、`agentic-retrieval-python.md`というPythonクイックスタートガイドに対するマイナーアップデートです。主な変更点は、ドキュメントの日付が「2025年6月24日」から「2025年8月28日」に更新されたことと、ユーザー向けの重要な追加情報が含まれたことです。

このクイックスタートでは、エージェントリトリーバル技術を使用して会話型検索を構築する方法が説明されています。また、ユーザーが自分のデータを提供できることに加えて、NASAの「Earth at Night」電子書籍からのサンプルJSONドキュメントが使用されることが強調されています。

新たに追加された情報として、Python版のクイックスタートが使用しているAPIバージョン「2025-05-01-preview」には、知識ソースやエージェントリトリーバルの新機能がサポートされていないことが指摘されており、これらの機能を使用するには別のRESTバージョンのクイックスタートを参照する必要があることが案内されています。また、Azureアカウントの作成を促すリンクも掲載されています。

全体として、この修正によってユーザーはエージェントリトリーバル技術をより効果的に活用できるようになるとともに、必要なリソースを準備する手助けが提供されています。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

<details>
<summary>Diff</summary>
````diff
@@ -4,178 +4,182 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 6/15/2025
+ms.date: 08/26/2025
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
 
-In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-concept.md) to create a conversational search experience powered by large language models (LLMs) and your proprietary data. Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries in parallel, and extracts grounding data from documents indexed in Azure AI Search. The output is intended for integration with custom chat solutions.
+In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-concept.md) to create a conversational search experience powered by documents indexed in Azure AI Search and large language models (LLMs) from Azure AI Foundry Models.
+
+A *knowledge agent* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the agent outputs raw content from your sources, but this quickstart passes the output to an LLM for natural-language answer generation.
 
 Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
 > [!TIP]
-> The REST version of this quickstart introduces agentic retrieval in Azure AI Search, which *extracts* rather than *generates* answers. For an end-to-end workflow, including steps for adding conversational turns and passing your retrieved content to an LLM for answer generation, see the C# or Python version.
+> Want to get started right away? See the [azure-search-rest-samples](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-agentic-retrieval) repository on GitHub.
 
 ## Prerequisites
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
 + An [Azure AI Search service](../../search-create-service-portal.md) on the Basic tier or higher with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
 
-+ An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects). You get an Azure AI Foundry resource (that's needed for model deployments) when you create an Azure AI Foundry project.
-
-+ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
++ An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects) and Azure AI Foundry resource. When you create a project, the resource is automatically created.
 
 + The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
+
 [!INCLUDE [Setup](./agentic-retrieval-setup.md)]
 
 ## Connect from your local system
 
-You configured role-based access to interact with Azure AI Search and Azure OpenAI. From the command line, use the Azure CLI to sign in to the same subscription and tenant for both services. For more information, see [Quickstart: Connect without keys](../../search-get-started-rbac.md).
+You configured role-based access to interact with Azure AI Search and Azure AI Foundry. From the command line, use the Azure CLI to sign in to the same subscription and tenant for both resources. For more information, see [Quickstart: Connect without keys](../../search-get-started-rbac.md).
 
 To connect from your local system:
 
-1. Open a new terminal in Visual Studio Code and change to the directory where you want to save your files.
+1. Open a command-line tool, such as PowerShell.
 
-1. Run the following command and sign in with your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Azure AI Foundry project.
+1. Sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service and Azure AI Foundry project.
 
     ```azurecli
     az login
     ```
 
-1. To obtain your Microsoft Entra token, run the following command. You specify this value in the next section.
+1. Generate a Microsoft Entra ID token.
 
    ```azurecli
    az account get-access-token --scope https://search.azure.com/.default --query accessToken --output tsv
    ```
 
+1. Make a note of the token for use in the next section.
+
 ## Load connections
 
-Before you send any requests, define credentials, endpoints, and deployment details for connections to Azure AI Search and Azure OpenAI. These values are used in subsequent operations.
+Before you send any requests, define endpoints, credentials, and deployment details for connections to Azure AI Search and Azure AI Foundry. These values are used in the following sections.
 
 To load the connections:
 
-1. In Visual Studio Code create a `.rest` or `.http` file. For example, you can name the file `agentic-retrieval.rest`.
-1. Paste these placeholders into the new file:
+1. In Visual Studio Code, create a file named `agentic-retrieval.rest`.
+
+1. Paste the following variables and HTTP request into the file.
 
     ```HTTP
-    @baseUrl = PUT-YOUR-SEARCH-SERVICE-URL-HERE
+    @search-url = PUT-YOUR-SEARCH-SERVICE-URL-HERE
     @token = PUT-YOUR-MICROSOFT-ENTRA-TOKEN-HERE
-    @aoaiBaseUrl = PUT-YOUR-AI-FOUNDRY-URL-HERE
-    @aoaiGptModel = gpt-4.1-mini
-    @aoaiGptDeployment = gpt-4.1-mini
-    @aoaiEmbeddingModel = text-embedding-3-large
-    @aoaiEmbeddingDeployment = text-embedding-3-large
-    @index-name = earth_at_night
-    @agent-name = earth-search-agent
-    @api-version = 2025-05-01-Preview
-    ```
+    @aoai-url = PUT-YOUR-AOAI-FOUNDRY-URL-HERE
+    @aoai-embedding-model = text-embedding-3-large
+    @aoai-embedding-deployment = text-embedding-3-large
+    @aoai-gpt-model = gpt-4.1-mini
+    @aoai-gpt-deployment = gpt-4.1-mini
+    @index-name = earth-at-night
+    @knowledge-source-name = earth-knowledge-source
+    @knowledge-agent-name = earth-knowledge-agent
+    @api-version = 2025-08-01-Preview
 
-1. Set `@baseUrl` to your Azure AI Search endpoint, which looks like `https://<your-search-service-name>.search.windows.net.` Set `@aoaiBaseUrl` to your Azure AI Foundry endpoint, which looks like `https://<your-foundry-resource-name>.openai.azure.com.` You obtained both values in the [Get endpoints](#get-endpoints) section. 
-
-1. Replace `@token` with the Microsoft Entra token you obtained in [Connect from your local system](#connect-from-your-local-system).
-
-1. In the same file, enter and send the following HTTP request to verify that you can connect to Azure AI Search. The request lists existing indexes in your search service.
-
-    ```HTTP
     ### List existing indexes by name
-    GET {{baseUrl}}/indexes?api-version={{api-version}}  HTTP/1.1
+    GET {{search-url}}/indexes?api-version={{api-version}}  HTTP/1.1
         Content-Type: application/json
         Authorization: Bearer {{token}}
     ```
 
+1. Set `@search-url` and `aoai-url` to the values you obtained in [Get endpoints](#get-endpoints).
+
+1. Set `@token` to the value you obtained in [Connect from your local system](#connect-from-your-local-system).
+
+1. Under `### List existing indexes by name`, select **Send Request** to verify the connection to your search service.
+
     A response should appear in an adjacent pane. If you have existing indexes, they're listed. Otherwise, the list is empty. If the HTTP code is `200 OK`, you're ready to proceed.
 
 ## Create a search index
 
-In Azure AI Search, an index is a structured collection of data. Use [Create Index](/rest/api/searchservice/indexes/create) to define an index named `earth_at_night`, which you specified using the `@index-name` variable in the previous section.
+In Azure AI Search, an index is a structured collection of data. Use [Indexes - Create (REST API)](/rest/api/searchservice/indexes/create) to define an index named `earth-at-night`, which you previously specified using the `@index-name` variable.
+
+The index schema contains fields for document identification and page content, embeddings, and numbers. The schema also includes configurations for semantic ranking and vector search, which uses your `text-embedding-3-large` deployment to vectorize text and match documents based on semantic or conceptual similarity.
 
 ```HTTP
 ### Create an index
-PUT {{baseUrl}}/indexes/{{index-name}}?api-version={{api-version}}  HTTP/1.1
+PUT {{search-url}}/indexes/{{index-name}}?api-version={{api-version}}  HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{token}}
 
     {
-    "name": "{{index-name}}",
-    "fields": [
-        {
-        "name": "id",
-        "type": "Edm.String",
-        "key": true
-        },
-        {
-        "name": "page_chunk",
-        "type": "Edm.String",
-        "searchable": true
-        },
-        {
-        "name": "page_embedding_text_3_large",
-        "type": "Collection(Edm.Single)",
-        "stored": false,
-        "dimensions": 3072,
-        "vectorSearchProfile": "hnsw_text_3_large"
+        "name": "{{index-name}}",
+        "fields": [
+            {
+                "name": "id",
+                "type": "Edm.String",
+                "key": true
+            },
+            {
+                "name": "page_chunk",
+                "type": "Edm.String",
+                "searchable": true
+            },
+            {
+                "name": "page_embedding_text_3_large",
+                "type": "Collection(Edm.Single)",
+                "stored": false,
+                "dimensions": 3072,
+                "vectorSearchProfile": "hnsw_text_3_large"
+            },
+            {
+                "name": "page_number",
+                "type": "Edm.Int32",
+                "filterable": true
+            }
+        ],
+        "semantic": {
+            "defaultConfiguration": "semantic_config",
+            "configurations": [
+                {
+                    "name": "semantic_config",
+                    "prioritizedFields": {
+                    "prioritizedContentFields": [
+                        {
+                            "fieldName": "page_chunk"
+                        }
+                    ]
+                    }
+                }
+            ]
         },
-        {
-        "name": "page_number",
-        "type": "Edm.Int32",
-        "filterable": true
-        }
-    ],
-    "semantic": {
-        "defaultConfiguration": "semantic_config",
-        "configurations": [
-        {
-            "name": "semantic_config",
-            "prioritizedFields": {
-            "prioritizedContentFields": [
+        "vectorSearch": {
+            "profiles": [
+                {
+                    "name": "hnsw_text_3_large",
+                    "algorithm": "alg",
+                    "vectorizer": "azure_openai_text_3_large"
+                }
+            ],
+            "algorithms": [
+                {
+                    "name": "alg",
+                    "kind": "hnsw"
+                }
+            ],
+            "vectorizers": [
                 {
-                "fieldName": "page_chunk"
+                    "name": "azure_openai_text_3_large",
+                    "kind": "azureOpenAI",
+                    "azureOpenAIParameters": {
+                    "resourceUri": "{{aoai-url}}",
+                    "deploymentId": "{{aoai-embedding-deployment}}",
+                    "modelName": "{{aoai-embedding-model}}"
+                    }
                 }
             ]
-            }
         }
-        ]
-    },
-    "vectorSearch": {
-        "profiles": [
-        {
-            "name": "hnsw_text_3_large",
-            "algorithm": "alg",
-            "vectorizer": "azure_openai_text_3_large"
-        }
-        ],
-        "algorithms": [
-        {
-            "name": "alg",
-            "kind": "hnsw"
-        }
-        ],
-        "vectorizers": [
-        {
-            "name": "azure_openai_text_3_large",
-            "kind": "azureOpenAI",
-            "azureOpenAIParameters": {
-            "resourceUri": "{{aoaiBaseUrl}}",
-            "deploymentId": "{{aoaiEmbeddingDeployment}}",
-            "modelName": "{{aoaiEmbeddingModel}}"
-            }
-        }
-        ]
-    }
     }
 ```
 
-The index schema contains fields for document identification and page content, embeddings, and numbers. It also includes configurations for semantic ranking and vector queries, which use the `text-embedding-3-large` model you previously deployed.
-
 ## Upload documents to the index
 
-Currently, the `earth_at_night` index is empty. Use [Index Documents](/rest/api/searchservice/documents/index) to populate the index with JSON documents from NASA's Earth at Night e-book. As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
+Currently, the `earth-at-night` index is empty. Use [Documents - Index (REST API)](/rest/api/searchservice/documents/index) to populate the index with JSON documents from NASA's Earth at Night e-book. As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
 
 ```HTTP
-### Load documents
-POST {{baseUrl}}/indexes/{{index-name}}/docs/index?api-version={{api-version}}  HTTP/1.1
+### Upload documents
+POST {{search-url}}/indexes/{{index-name}}/docs/index?api-version={{api-version}}  HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{token}}
 
@@ -203,46 +207,72 @@ POST {{baseUrl}}/indexes/{{index-name}}/docs/index?api-version={{api-version}}
     }
 ```
 
+## Create a knowledge source
+
+A knowledge source is a reusable reference to your source data. Use [Knowledge Sources - Create (REST API)](/rest/api/searchservice/knowledge-sources/create?view=rest-searchservice-2025-08-01-preview&preserve-view=true) to define a knowledge source named `earth-knowledge-source` that targets the `earth-at-night` index.
+
+`searchIndexParameters.sourceDataSelect` specifies which index fields are accessible for retrieval and citations. Our example includes only human-readable fields to avoid lengthy, uninterpretable embeddings in responses.
+
+```HTTP
+### Create a knowledge source
+POST {{search-url}}/knowledgesources?api-version={{api-version}}  HTTP/1.1
+    Content-Type: application/json
+    Authorization: Bearer {{token}}
+
+    {
+        "name": "{{knowledge-source-name}}",
+        "description": "This knowledge source pulls from a search index that contains pages from the Earth at Night e-book.",
+        "kind": "searchIndex",
+        "searchIndexParameters": {
+            "searchIndexName": "{{index-name}}",
+            "sourceDataSelect": "id, page_chunk, page_number"
+        }
+    }
+```
+
 ## Create a knowledge agent
 
-To connect Azure AI Search to your `gpt-4.1-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. Use [Create Knowledge Agents](/rest/api/searchservice/knowledge-agents/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true) to define an agent named `earth-search-agent`, which you specified using the `@agent-name` variable in a previous section.
+To target your `earth-knowledge-source` and `gpt-4.1-mini` deployment at query time, you need a knowledge agent. Use [Knowledge Agents - Create (REST API)](/rest/api/searchservice/knowledge-agents/create?view=rest-searchservice-2025-08-01-preview&preserve-view=true) to define an agent named `earth-knowledge-agent`, which you previously specified using the `@knowledge-agent-name` variable.
 
-To ensure relevant and semantically meaningful responses, `defaultRerankerThreshold` is set to exclude responses with a reranker score of `2.5` or lower.
+`knowledgeSources.rerankerThreshold` ensures semantic relevance by excluding responses with a reranker score of `2.5` or lower. Meanwhile, `outputConfiguration.modality` is set to `answerSynthesis`, enabling natural-language answers that cite the retrieved documents.
 
 ```HTTP
-### Create an agent
-PUT {{baseUrl}}/agents/{{agent-name}}?api-version={{api-version}}  HTTP/1.1
+### Create a knowledge agent
+PUT {{search-url}}/agents/{{knowledge-agent-name}}?api-version={{api-version}}  HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{token}}
 
     {
-        "name": "{{agent-name}}",
-        "targetIndexes": [
+        "name": "{{knowledge-agent-name}}",
+        "knowledgeSources": [
             {
-                "indexName": "{{index-name}}",
-                "defaultRerankerThreshold": 2.5
+            "name": "{{knowledge-source-name}}",
+            "rerankerThreshold": 2.5
             }
         ],
         "models": [
             {
                 "kind": "azureOpenAI",
                 "azureOpenAIParameters": {
-                    "resourceUri": "{{aoaiBaseUrl}}",
-                    "deploymentId": "{{aoaiGptDeployment}}",
-                    "modelName": "{{aoaiGptModel}}"
+                    "resourceUri": "{{aoai-url}}",
+                    "deploymentId": "{{aoai-gpt-deployment}}",
+                    "modelName": "{{aoai-gpt-model}}"
                 }
             }
-        ]
+        ],
+        "outputConfiguration": {
+            "modality": "answerSynthesis"
+        }
     }
 ```
 
 ## Run the retrieval pipeline
 
-You're ready to initiate the agentic retrieval pipeline. Use [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-05-01-preview&preserve-view=true) to send a two-part user query to `earth-search-agent`, which deconstructs the query into subqueries, runs the subqueries against both text fields and vector embeddings in the `earth_at_night` index, and ranks and merges the results.
+You're ready to run agentic retrieval. Use [Knowledge Retrieval - Retrieve (REST API)](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true) to send a two-part user query to `earth-knowledge-agent`, which deconstructs the query into subqueries, runs the subqueries against text and vector fields in the `earth-at-night` index, and ranks and merges the results.
 
 ```HTTP
 ### Run agentic retrieval
-POST {{baseUrl}}/agents/{{agent-name}}/retrieve?api-version={{api-version}}  HTTP/1.1
+POST {{search-url}}/agents('{{knowledge-agent-name}}')/retrieve?api-version={{api-version}}  HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{token}}
 
@@ -258,110 +288,137 @@ POST {{baseUrl}}/agents/{{agent-name}}/retrieve?api-version={{api-version}}  HTT
                 ]
             }
         ],
-        "targetIndexParams": [
+        "knowledgeSourceParams": [
             {
-                "indexName": "{{index-name}}",
-                "rerankerThreshold": 2.5
+                "knowledgeSourceName": "{{knowledge-source-name}}",
+                "kind": "searchIndex"
             }
         ]
     }
 ```
 
 The output should be similar to the following JSON, where:
 
-+ `response` provides a text string of the most relevant documents (or chunks) in the search index based on the user query. You can pass this string to an LLM for use as grounding data in answer generation.
++ `response` provides a synthesized, LLM-generated answer to the query based on the retrieved documents. When answer synthesis isn't enabled, this section contains content extracted directly from the documents.
 
-+ `activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for query planning and execution.
++ `activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for semantic ranking, query planning, and answer synthesis.
 
 + `references` lists the documents that contributed to the response, each one identified by their `docKey`.
 
 ```JSON
 {
   "response": [
     {
-      "role": "assistant",
       "content": [
         {
           "type": "text",
-          "text": "[{\"ref_id\":1,\"content\":\"# Urban Structure\\n\\n## March 16, 2013\\n\\n### Phoenix Metropolitan Area at Night\\n\\nThis figure presents a nighttime satellite view of the Phoenix metropolitan area, highlighting urban structure and transport corridors. City lights illuminate the layout of several cities and major thoroughfares.\\n\\n**Labeled Urban Features:**\\n\\n- **Phoenix:** Central and brightest area in the right-center of the image.\\n- **Glendale:** Located to the west of Phoenix, this city is also brightly lit.\\n- **Peoria:** Further northwest, this area is labeled and its illuminated grid is seen.\\n- **Grand Avenue:** Clearly visible as a diagonal, brightly lit thoroughfare running from Phoenix through Glendale and Peoria.\\n- **Salt River Channel:** Identified in the southeast portion, running through illuminated sections.\\n- **Phoenix Mountains:** Dark, undeveloped region to the northeast of Phoenix.\\n- **Agricultural Fields:** Southwestern corner of the image, grid patterns are visible but with much less illumination, indicating agricultural land use.\\n\\n**Additional Notes:**\\n\\n- The overall pattern shows a grid-like urban development typical of western U.S. cities, with scattered bright nodes at major intersections or city centers.\\n- There is a clear transition from dense urban development to sparsely populated or agricultural land, particularly evident towards the bottom and left of the image.\\n- The illuminated areas follow the existing road and street grids, showcasing the extensive spread of the metropolitan area.\\n\\n**Figure Description:**  \\nA satellite nighttime image captured on March 16, 2013, showing Phoenix and surrounding areas (including Glendale and Peoria). Major landscape and infrastructural features, such as the Phoenix Mountains, Grand Avenue, the Salt River Channel, and agricultural fields, are labeled. The image reveals the extent of urbanization and the characteristic street grid illuminated by city lights.\\n\\n---\\n\\nPage 89\"},{\"ref_id\":0,\"content\":\"<!-- PageHeader=\\\"Urban Structure\\\" -->\\n\\n### Location of Phoenix, Arizona\\n\\nThe image depicts a globe highlighting the location of Phoenix, Arizona, in the southwestern United States, marked with a blue pinpoint on the map of North America. Phoenix is situated in the central part of Arizona, which is in the southwestern region of the United States.\\n\\n---\\n\\n### Grid of City Blocks-Phoenix, Arizona\\n\\nLike many large urban areas of the central and western United States, the Phoenix metropolitan area is laid out along a regular grid of city blocks and streets. While visible during the day, this grid is most evident at night, when the pattern of street lighting is clearly visible from the low-Earth-orbit vantage point of the ISS.\\n\\nThis astronaut photograph, taken on March 16, 2013, includes parts of several cities in the metropolitan area, including Phoenix (image right), Glendale (center), and Peoria (left). While the major street grid is oriented north-south, the northwest-southeast oriented Grand Avenue cuts across the three cities at image center. Grand Avenue is a major transportation corridor through the western metropolitan area; the lighting patterns of large industrial and commercial properties are visible along its length. Other brightly lit properties include large shopping centers, strip malls, and gas stations, which tend to be located at the intersections of north-south and east-west trending streets.\\n\\nThe urban grid encourages growth outwards along a city's borders by providing optimal access to new real estate. Fueled by the adoption of widespread personal automobile use during the twentieth century, the Phoenix metropolitan area today includes 25 other municipalities (many of them largely suburban and residential) linked by a network of surface streets and freeways.\\n\\nWhile much of the land area highlighted in this image is urbanized, there are several noticeably dark areas. The Phoenix Mountains are largely public parks and recreational land. To the west, agricultural fields provide a sharp contrast to the lit streets of residential developments. The Salt River channel appears as a dark ribbon within the urban grid.\\n\\n\\n<!-- PageFooter=\\\"Earth at Night\\\" -->\\n<!-- PageNumber=\\\"88\\\" -->\"}]",
-          "image": null
+          "text": "Suburban belts display larger December brightening than urban cores despite higher absolute light levels downtown because the urban grid encourages outward growth along city borders, fueled by widespread personal automobile use, leading to extensive suburban and residential municipalities linked by surface streets and freeways. This expansion results in increased lighting in suburban areas during December. The Phoenix nighttime street grid is sharply visible from space due to its regular grid layout of city blocks and streets, with major transportation corridors like Grand Avenue and brightly lit commercial properties at intersections, which create distinct lighting patterns. In contrast, large stretches of interstate highways between Midwestern cities remain comparatively dim because they lack the dense, grid-like urban development and associated lighting found in metropolitan areas like Phoenix [ref_id:0][ref_id:1]."
         }
       ]
     }
   ],
   "activity": [
     {
-      "type": "ModelQueryPlanning",
+      "type": "modelQueryPlanning",
       "id": 0,
-      "inputTokens": 1355,
-      "outputTokens": 423
+      "inputTokens": 2079,
+      "outputTokens": 121,
+      "elapsedMs": 2887
     },
     {
-      "type": "AzureSearchQuery",
+      "type": "searchIndex",
       "id": 1,
-      "targetIndex": "earth_at_night",
-      "query": {
-        "search": "suburban belts December brightening urban cores comparison",
+      "knowledgeSourceName": "earth-knowledge-source",
+      "queryTime": "2025-08-25T16:23:17.832Z",
+      "count": 0,
+      "elapsedMs": 1065,
+      "searchIndexArguments": {
+        "search": "Reasons for larger December brightening in suburban belts compared to urban cores despite higher downtown light levels",
         "filter": null
-      },
-      "queryTime": "2025-05-06T15:57:14.666Z",
-      "elapsedMs": 270
+      }
     },
     {
-      "type": "AzureSearchQuery",
+      "type": "searchIndex",
       "id": 2,
-      "targetIndex": "earth_at_night",
-      "query": {
-        "search": "Phoenix nighttime street grid visibility from space",
-        "filter": null
-      },
-      "queryTime": "2025-05-06T15:57:14.858Z",
+      "knowledgeSourceName": "earth-knowledge-source",
+      "queryTime": "2025-08-25T16:23:18.139Z",
       "count": 2,
-      "elapsedMs": 192
+      "elapsedMs": 298,
+      "searchIndexArguments": {
+        "search": "Factors making Phoenix nighttime street grid sharply visible from space",
+        "filter": null
+      }
     },
     {
-      "type": "AzureSearchQuery",
+      "type": "searchIndex",
       "id": 3,
-      "targetIndex": "earth_at_night",
-      "query": {
-        "search": "interstate visibility from space midwestern cities",
+      "knowledgeSourceName": "earth-knowledge-source",
+      "queryTime": "2025-08-25T16:23:18.332Z",
+      "count": 0,
+      "elapsedMs": 189,
+      "searchIndexArguments": {
+        "search": "Reasons why large stretches of interstate between Midwestern cities are comparatively dim at night from space",
         "filter": null
-      },
-      "queryTime": "2025-05-06T15:57:15.026Z",
-      "count": 1,
-      "elapsedMs": 167
+      }
+    },
+    {
+      "type": "semanticReranker",
+      "id": 4,
+      "inputTokens": 2349
+    },
+    {
+      "type": "modelAnswerSynthesis",
+      "id": 5,
+      "inputTokens": 3216,
+      "outputTokens": 155,
+      "elapsedMs": 2274
     }
   ],
   "references": [
     {
-      "type": "AzureSearchDoc",
+      "type": "searchIndex",
       "id": "0",
       "activitySource": 2,
-      "docKey": "earth_at_night_508_page_104_verbalized",
-      "sourceData": null
+      "sourceData": null,
+      "rerankerScore": 2.6642752,
+      "docKey": "earth_at_night_508_page_104_verbalized"
     },
     {
-      "type": "AzureSearchDoc",
+      "type": "searchIndex",
       "id": "1",
       "activitySource": 2,
-      "docKey": "earth_at_night_508_page_105_verbalized",
-      "sourceData": null
+      "sourceData": null,
+      "rerankerScore": 2.5905457,
+      "docKey": "earth_at_night_508_page_105_verbalized"
     }
   ]
 }
 ```
 
 ## Clean up resources
 
-When working in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money. You can delete resources individually, or you can delete the resource group to delete the entire set of resources.
+When you work in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money.
+
+Run the following code to delete the objects you created in this quickstart.
+
+<!-- You can delete resources individually or delete the entire resource group.
 
-In the Azure portal, you can find and manage resources by selecting **All resources** or **Resource groups** from the left pane. You can also run the following code to delete the objects you created in this quickstart.
+In the Azure portal, you can find and manage resources by selecting **All resources** or **Resource groups** from the left pane. -->
+
+### Delete the knowledge agent
 
+```HTTP
 ### Delete the knowledge agent
+DELETE {{search-url}}/agents/{{knowledge-agent-name}}?api-version={{api-version}}  HTTP/1.1
+    Content-Type: application/json
+    Authorization: Bearer {{token}}
+```
+
+### Delete the knowledge source
 
 ```HTTP
-### Delete the agent
-DELETE {{baseUrl}}/agents/{{agent-name}}?api-version={{api-version}}
+### Delete the knowledge source
+DELETE {{search-url}}/knowledgesources('{{knowledge-source-name}}')?api-version={{api-version}}  HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{token}}
 ```
@@ -370,7 +427,7 @@ DELETE {{baseUrl}}/agents/{{agent-name}}?api-version={{api-version}}
 
 ```HTTP
 ### Delete the index
-DELETE {{baseUrl}}/indexes/{{index-name}}?api-version={{api-version}}
+DELETE {{search-url}}//indexes/{{index-name}}?api-version={{api-version}}  HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{token}}
 ```
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エージェントリトリーバルに関するRESTクイックスタートの大幅な更新"
}
```

### Explanation
この修正は、`agentic-retrieval-rest.md`というRESTクイックスタートガイドに対する大幅な更新を含んでいます。主な変更点には、ドキュメントの日付の更新に加え、クイックスタートの全体的な内容と構成、手順に関する詳細な情報が盛り込まれています。このアップデートにより、エージェントリトリーバル技術に関する理解が深まるとともに、実装手順が明確に示されています。

まず、クイックスタートの目的が明確に説明され、ユーザーがAzure AI SearchとAzure AI Foundryからの大規模言語モデル（LLM）を利用して会話型検索体験を構築できる方法が記載されています。特に、新たに「knowledge agent」が追加され、これは複雑なクエリをサブクエリに分解し、結果とメタデータを返す役割を果たします。また、LLMを介して自然言語での回答生成も行われることが強調されています。

さらに、利用するAzureリソースや、必要なプロジェクトの設定、接続方法やデータの読み込み・アップロード手順についても詳細にわたり解説されています。また、索引や知識ソース、エージェントの作成手順も具体的に説明され、その構造やフィールドの形式についての具体的な例も含まれています。

このバージョンでは、システムが稼働するために必要なAPIバージョンが「2025-08-01-Preview」に更新されたことも重要な点です。また、リソースのクリーンアップ手順についても詳しく説明がされており、プロジェクト終了後に作成したリソースを適切に管理できるようになっています。

総じて、この修正はエージェントリトリーバルシステムの利用を促進し、実装の際の具体的な手順をユーザーが理解しやすい形で提供しています。

## articles/search/includes/quickstarts/agentic-retrieval-setup.md{#item-e5e297}

<details>
<summary>Diff</summary>
````diff
@@ -4,87 +4,101 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 06/23/2025
+ms.date: 08/26/2025
 ---
 
-## Configure role-based access
+## Configure access
 
-You can use search service API keys or Microsoft Entra ID with role assignments. Keys are easier to start with, but roles are more secure.
+Before you begin, make sure you have permissions to access content and operations. We recommend Microsoft Entra ID for authentication and role-based access for authorization. You must be an **Owner** or **User Access Administrator** to assign roles. If roles aren't feasible, use [key-based authentication](../../search-security-api-keys.md) instead.
 
-To configure the recommended role-based access:
+To configure access for this quickstart, select both of the following tabs.
 
-1. Sign in to the [Azure portal](https://portal.azure.com/).
+### [Azure AI Search](#tab/search-perms)
 
-1. [Enable role-based access](../../search-security-enable-roles.md) on your Azure AI Search service.
+Azure AI Search provides the agentic retrieval pipeline. Configure access for yourself and your search service to read and write data, interact with Azure AI Foundry, and run the pipeline.
 
-1. On your Azure AI Search service, [assign the following roles](../../search-security-rbac.md#how-to-assign-roles-in-the-azure-portal) to yourself.
+To configure access for Azure AI Search:
+
+1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
+
+1. [Enable role-based access](../../search-security-enable-roles.md).
+
+1. [Create a system-assigned managed identity](../../search-how-to-managed-identities.md#create-a-system-managed-identity).
+
+1. [Assign the following roles](../../search-security-rbac.md#how-to-assign-roles-in-the-azure-portal) to yourself.
 
     + **Search Service Contributor**
 
     + **Search Index Data Contributor**
 
     + **Search Index Data Reader**
 
-For agentic retrieval, Azure AI Search also needs access to your Azure OpenAI Foundry resource.
+### [Azure AI Foundry](#tab/foundry-perms)
 
-1. [Create a system-assigned managed identity](../../search-how-to-managed-identities.md#create-a-system-managed-identity) on your Azure AI Search service. Here's how to do it using the Azure CLI:
+Azure AI Foundry provides the Azure OpenAI models used for embeddings, query planning, and answer generation. Grant your search service permission to use these models.
 
-   ```azurecli
-   az search service update --name YOUR-SEARCH-SERVICE-NAME --resource-group YOUR-RESOURCE-GROUP-NAME --identity-type SystemAssigned
-   ```
+To configure access for Azure AI Foundry:
 
-    If you already have a managed identity, you can skip this step.
+1. Sign in to the [Azure portal](https://portal.azure.com/) and select your Azure AI Foundry resource.
 
-1. On your Azure AI Foundry resource, assign **Cognitive Services User** to the managed identity that you created for your search service.
+1. Assign **Cognitive Services User** to the managed identity of your search service.
 
-## Deploy models
+---
 
-To use agentic retrieval, you must deploy [one of the supported Azure OpenAI models](../../search-agentic-retrieval-how-to-create.md#supported-models) to your Azure AI Foundry resource:
+> [!IMPORTANT]
+> Agentic retrieval has two token-based billing models:
+>
+> + Billing from Azure AI Search for semantic ranking.
+> + Billing from Azure OpenAI for query planning and answer synthesis.
+>
+> Semantic ranking is free in the initial public preview. After the preview, standard token billing applies. For more information, see [Availability and pricing of agentic retrieval](../../search-agentic-retrieval-concept.md#availability-and-pricing).
 
-+ A chat model for query planning and answer generation. We use `gpt-4.1-mini` in this quickstart. Optionally, you can use a different model for query planning and another for answer generation, but this quickstart uses the same model for simplicity.
+## Get endpoints
 
-+ An embedding model for vector queries. We use `text-embedding-3-large` in this quickstart, but you can use any embedding model that supports the `text-embedding` task.
+Each Azure AI Search service and Azure AI Foundry resource has an *endpoint*, which is a unique URL that identifies and provides network access to the resource. In a later section, you specify these endpoints to connect to your resources programmatically.
 
-To deploy the Azure OpenAI models:
+To get the endpoints for this quickstart, select both of the following tabs.
 
-1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and select your Azure AI Foundry resource.
+### [Azure AI Search](#tab/search-endpoint)
 
-1. From the left pane, select **Model catalog**.
+1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
 
-1. Select **gpt-4.1-mini**, and then select **Use this model**.
+1. From the left pane, select **Overview**.
 
-1. Specify a deployment name. To simplify your code, we recommend **gpt-4.1-mini**.
+1. Make a note of the endpoint, which should look like `https://my-service.search.windows.net`.
 
-1. Leave the default settings.
+### [Azure AI Foundry](#tab/foundry-endpoint)
 
-1. Select **Deploy**.
+1. Sign in to the [Azure portal](https://portal.azure.com/) and select your Azure AI Foundry resource.
 
-1. Repeat the previous steps, but this time deploy the **text-embedding-3-large** embedding model.
+1. From the left pane, select **Resource Management** > **Keys and Endpoint**.
 
-## Get endpoints
+1. Select the **OpenAI** tab.
 
-In your code, you specify the following endpoints to establish connections with your Azure AI Search service and Azure AI Foundry resource. These steps assume that you [configured role-based access as described previously](#configure-role-based-access).
+1. Make a note of the endpoint, which should look like `https://my-resource.openai.azure.com`.
 
-To obtain your service endpoints:
+---
 
-1. Sign in to the [Azure portal](https://portal.azure.com/).
+## Deploy models
 
-1. On your Azure AI Search service:
+To use agentic retrieval, you must deploy two Azure OpenAI models to your Azure AI Foundry resource:
 
-    1. From the left pane, select **Overview**.
++ An embedding model for text-to-vector conversion. This quickstart uses `text-embedding-3-large`, but you can use any embedding model that supports the `text-embedding` task.
 
-    1. Copy the URL, which should be similar to `https://my-service.search.windows.net`.
++ A [supported chat completion model](../../search-agentic-retrieval-how-to-create.md#supported-models) for query planning and answer generation. This quickstart uses `gpt-4.1-mini`. Optionally, you can use one model for query planning and another model for answer generation, but this quickstart uses the same model for simplicity.
 
-1. On your Azure AI Foundry resource:
+To deploy the Azure OpenAI models:
 
-    1. From the left pane, select **Resource Management** > **Keys and Endpoint**.
+1. Sign in to the [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs) and select your Azure AI Foundry resource.
 
-    1. Select the **OpenAI** tab and copy the URL that looks similar to `https://my-resource.openai.azure.com`.
+1. From the left pane, select **Model catalog**.
 
-> [!IMPORTANT]
-> Agentic retrieval has two token-based billing models:
->
-> + Billing from Azure OpenAI for query planning.
-> + Billing from Azure AI Search for query execution (semantic ranking).
->
-> Semantic ranking is free in the initial public preview. After the preview, standard token billing applies. For more information, see [Availability and pricing of agentic retrieval](../../search-agentic-retrieval-concept.md#availability-and-pricing).
+1. Select **text-embedding-3-large**, and then select **Use this model**.
+
+1. Enter a deployment name. To simplify your code, we recommend **text-embedding-3-large**.
+
+1. Leave the default settings.
+
+1. Select **Deploy**.
+
+1. Repeat the previous steps, but this time, deploy **gpt-4.1-mini** from the model catalog.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルのセットアップガイドの更新"
}
```

### Explanation
この修正は、`agentic-retrieval-setup.md`というエージェントリトリーバルのセットアップガイドに対するマイナーアップデートです。変更内容には、構成手順の見直しと明確化、新しい情報の追加が含まれています。

まず、ドキュメントの日付が「2025年6月23日」から「2025年8月26日」に更新され、最新の情報が反映されるようになっています。また、認証とアクセス権の設定手順が改善され、特にMicrosoft Entra IDを推奨する形に変更されています。これは、より安全なロールベースのアクセス管理を強調するもので、具体的な手順として、Azureポータルにサインインし、ロールを設定する方法が詳述されています。

さらに、Azure AI SearchとAzure AI Foundryの両方に対するアクセス構成をするための具体的な手順が追加され、それぞれのリソースへの適切な役割を設定するように促されています。これにより、ユーザーはエージェントリトリーバル機能を活用するための準備が整います。

また、Azure OpenAIモデルの展開手順も整備され、必要なモデルの選択や設定についてのガイダンスが拡充されています。特に、エージェントリトリーバルが2つのトークンベースの請求モデルを持つことの重要性が強調され、利用者に対して注意事項として記載されています。

全体として、この修正はエージェントリトリーバルを利用するための手続きがわかりやすくなり、利用者がスムーズに環境設定を行えるよう工夫されています。

## articles/search/includes/quickstarts/agentic-retrieval-typescript.md{#item-e6370b}

<details>
<summary>Diff</summary>
````diff
@@ -4,14 +4,18 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 7/21/2025
+ms.date: 08/28/2025
 ---
+
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
 
 In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-concept.md) to create a conversational search experience powered by large language models (LLMs) and your proprietary data. Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries in parallel, and extracts grounding data from documents indexed in Azure AI Search. The output is intended for integration with agentic and custom chat solutions.
 
 Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
 
+> [!TIP]
+> The TypeScript version of this quickstart uses the 2025-05-01-preview REST API version, which doesn't support knowledge sources and other agentic retrieval features introduced in the 2025-08-01-preview. To use these features, see the REST version of this quickstart.
+
 ## Prerequisites
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルのTypeScriptクイックスタートの更新"
}
```

### Explanation
この修正は、`agentic-retrieval-typescript.md`というTypeScriptによるエージェントリトリーバルのクイックスタートガイドに対するマイナーアップデートです。主な変更点には、日付の更新と新しい情報の追加が含まれています。

まず、ドキュメントの日付が「2025年7月21日」から「2025年8月28日」に変更されており、内容が最新であることが反映されています。追加された情報として、TypeScript版のクイックスタートが「2025-05-01-preview」のREST APIバージョンを使用していることが強調されています。このバージョンでは、2025年の8月1日から導入された知識ソースや他のエージェントリトリーバル機能がサポートされていないため、それらの機能を使用したい場合は、REST版のクイックスタートを見るように案内があります。

さらに、クイックスタートが使用するサンプルデータとして、NASAの「Earth at Night」e-bookからのJSONドキュメントのリンクが提供されており、利用者がこのリソースを参照できるようになっています。これにより、ユーザーがエージェントリトリーバルの機能を具体的に実装する際の理解が深まることが期待されます。

総じて、この修正は、ユーザーにとってより有用な情報を提供し、エージェントリトリーバル機能の適切な利用方法を示すものとなっています。

## articles/search/includes/quickstarts/search-get-started-rag-rest.md{#item-aa7f2b}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: heidisteen
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 07/08/2025
+ms.date: 08/27/2025
 ---
 
 ## Prerequisites
@@ -104,7 +104,7 @@ We recommend [Visual Studio Code](https://code.visualstudio.com/download) with a
 
    ```http
    ### List existing indexes by name (verify the connection)
-    GET  {{searchUrl}}/indexes?api-version=2025-05-01-preview&$select=name  HTTP/1.1
+    GET  {{searchUrl}}/indexes?api-version=2025-08-01-preview&$select=name  HTTP/1.1
     Authorization: Bearer {{personalAccessToken}}
    ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAG REST APIを用いた検索のクイックスタートの更新"
}
```

### Explanation
この修正は、`search-get-started-rag-rest.md`というRAG（Retrieval-Augmented Generation）REST APIによる検索のクイックスタートガイドに対するマイナーアップデートです。変更内容として、日付の更新とAPIバージョンの変更が含まれています。

まず、ドキュメントの日付が「2025年7月8日」から「2025年8月27日」に更新され、最新の情報が反映されるようになっています。次に、クイックスタートの実行に必要なHTTPリクエストのサンプルが修正されており、APIのバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更されています。これにより、ユーザーは最新の機能を活用した状態でAPIを使用することができます。

全体として、この修正は、利用者にとって現在のAPIの使用方法を正確に反映したものであり、RAG REST APIを用いた検索の実装を容易にするための重要な更新となっています。

## articles/search/includes/quickstarts/semantic-ranker-rest.md{#item-d74861}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: heidisteen
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 07/03/2025
+ms.date: 08/27/2025
 ---
 
 [!INCLUDE [Semantic ranker introduction](semantic-ranker-intro.md)]
@@ -30,7 +30,7 @@ We recommend [Visual Studio Code](https://code.visualstudio.com/download) with a
 
    ```http
    ### List existing indexes by name (verify the connection)
-    GET  {{searchUrl}}/indexes?api-version=2025-05-01-preview&$select=name  HTTP/1.1
+    GET  {{searchUrl}}/indexes?api-version=2025-08-01-preview&$select=name  HTTP/1.1
     Authorization: Bearer {{personalAccessToken}}
    ```
 
@@ -64,7 +64,7 @@ To update an index using the REST API, you must provide the entire schema, plus
 1. Formulate a POST request specifying the index name, operation, and full JSON schema. All required elements of the schema must be present. This request includes the full schema for hotels-sample-index plus the semantic configuration.
 
     ```http
-    POST  {{searchUrl}}/indexes?api-version=2025-05-01-preview  HTTP/1.1
+    POST  {{searchUrl}}/indexes?api-version=2025-08-01-preview  HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{personalAccessToken}}
     
@@ -160,14 +160,14 @@ Required semantic parameters include `query_type` and `semantic_configuration_na
 1. Test the connection with a GET request that returns the hotels-sample-index.
 
     ```http
-    GET  {{searchUrl}}/indexes/hotels-sample-index?api-version=2025-05-01-preview  HTTP/1.1
+    GET  {{searchUrl}}/indexes/hotels-sample-index?api-version=2025-08-01-preview  HTTP/1.1
     Authorization: Bearer {{personalAccessToken}}
     ```
 
 1. Send a query that includes the semantic query type and configuration name.
 
    ```http
-    POST {{searchUrl}}/indexes/hotels-sample-index/docs/search?api-version=2025-05-01-preview  HTTP/1.1
+    POST {{searchUrl}}/indexes/hotels-sample-index/docs/search?api-version=2025-08-01-preview  HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{personalAccessToken}}
     
@@ -247,7 +247,7 @@ Optionally, you can add captions to extract portions of the text and apply hit h
 1. Add the `captions` parameter and send the request.
 
     ```http
-    POST {{searchUrl}}/indexes/hotels-sample-index/docs/search?api-version=2025-05-01-preview  HTTP/1.1
+    POST {{searchUrl}}/indexes/hotels-sample-index/docs/search?api-version=2025-08-01-preview  HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{personalAccessToken}}
     
@@ -290,7 +290,7 @@ To produce a semantic answer, the question and answer must be closely aligned, a
 1. Formulate the request using a search string that asks a question.
 
     ```http
-    POST {{searchUrl}}/indexes/hotels-sample-index/docs/search?api-version=2025-05-01-preview  HTTP/1.1
+    POST {{searchUrl}}/indexes/hotels-sample-index/docs/search?api-version=2025-08-01-preview  HTTP/1.1
     Content-Type: application/json
     Authorization: Bearer {{personalAccessToken}}
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーのREST APIクイックスタートの更新"
}
```

### Explanation
この修正は、`semantic-ranker-rest.md`というセマンティックランカーに関するREST APIのクイックスタートガイドに対するマイナーアップデートです。主な変更点は、日付の更新とAPIバージョンの変更です。

具体的には、ドキュメントの日付が「2025年7月3日」から「2025年8月27日」に変更され、最新の情報が反映されるようになっています。また、HTTPリクエストのサンプルコードにおいて、APIバージョンがすべて「2025-05-01-preview」から「2025-08-01-preview」に更新されています。この変更により、ユーザーは最新の機能および改善を利用した状態でAPIを使用することができるようになります。

加えて、複数のリクエストのサンプルコードが関連するすべての場所で更新されているため、ユーザーは今後の実装において維持するべき最新のベストプラクティスに基づいて作業を進めることが可能となっています。

全体として、この修正はセマンティックランカー機能の利用者に対して、最新のAPIに基づいた情報を提供し、より効果的なクイックスタート体験をサポートするものとなっています。

## articles/search/index-similarity-and-scoring.md{#item-75603d}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 08/13/2025
+ms.date: 08/27/2025
 ms.update-cycle: 365-days
 ---
 
@@ -137,7 +137,7 @@ In Azure AI Search, for keyword search and the text portion of a hybrid query, y
 > [!NOTE]
 > The `featuresMode` parameter isn't documented in the REST APIs, but you can use it on a preview REST API call to Search Documents for text (Keyword) search that's BM25-ranked.
 
-[Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&preserve-view=true) requests support a `featuresMode` parameter that provides more detail about a BM25 relevance score at the field level. Whereas the `@searchScore` is calculated for the document all-up (how relevant is this document in the context of this query), featuresMode reveals information about individual fields, as expressed in a `@search.features` structure. The structure contains all fields used in the query (either specific fields through **searchFields** in a query, or all fields attributed as **searchable** in an index).
+[Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-08-01-preview&preserve-view=true) requests support a `featuresMode` parameter that provides more detail about a BM25 relevance score at the field level. Whereas the `@searchScore` is calculated for the document all-up (how relevant is this document in the context of this query), featuresMode reveals information about individual fields, as expressed in a `@search.features` structure. The structure contains all fields used in the query (either specific fields through **searchFields** in a query, or all fields attributed as **searchable** in an index).
 
 Valid values for featuresMode:
 
@@ -155,7 +155,7 @@ This parameter is especially useful when you're trying to understand why certain
 For a query that targets a "description" field, a request might look like this:
 
 ```http
-POST {{baseUrl}}/indexes/hotels-sample-index/docs/search?api-version=2025-05-01-preview  HTTP/1.1
+POST {{baseUrl}}/indexes/hotels-sample-index/docs/search?api-version=2025-08-01-preview  HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer {{accessToken}}
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスの類似性とスコアリングドキュメントの更新"
}
```

### Explanation
この修正は、`index-similarity-and-scoring.md`というインデックスの類似性およびスコアリングに関するドキュメントに対するマイナーアップデートです。主にドキュメントの日付およびAPIバージョンに関する情報が更新されています。

最初に、ドキュメントの日付が「2025年8月13日」から「2025年8月27日」に変更されており、これにより最新の更新情報が反映されています。次に、APIリクエストのサンプルコードにおいて、使用するAPIバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更されている点が重要です。この変更により、最新のAPI機能や修正を利用することができます。

特に、`featuresMode`パラメータについての説明も同様に更新されており、このパラメータを使用してBM25関連スコアのフィールドレベルでの詳細な情報を取得できることが強調されています。この情報は、個々のフィールドに対する関連性を理解するのに役立ちます。

全体として、この修正はインデックスの類似性とスコアリングの理解を深め、最新のAPIの機能を正しく反映した内容となっており、ユーザーにとって価値のある情報を提供しています。

## articles/search/knowledge-store-concept-intro.md{#item-7475c2}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 05/27/2025
+ms.date: 08/21/2025
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
@@ -16,6 +16,9 @@ ms.custom:
 
 # Knowledge store in Azure AI Search
 
+> [!NOTE]
+> Knowledge stores exist in Azure Storage and contain the outputs of Azure AI Search skillsets. They're separate from knowledge sources and knowledge agents, which are used in [agentic retrieval](search-agentic-retrieval-concept.md) workflows.
+
 Knowledge store is secondary storage for [AI-enriched content created by a skillset](cognitive-search-concept-intro.md) in Azure AI Search. In Azure AI Search, an indexing job always sends output to a search index, but if you attach a skillset to an indexer, you can optionally also send AI-enriched output to a container or table in Azure Storage. A knowledge store can be used for independent analysis or downstream processing in non-search scenarios like knowledge mining. 
 
 The two outputs of indexing, a search index and knowledge store, are mutually exclusive products of the same pipeline. They're derived from the same inputs and contain the same data, but their content is structured, stored, and used in different applications.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジストアの概念紹介ドキュメントの更新"
}
```

### Explanation
この修正は、`knowledge-store-concept-intro.md`というナレッジストアに関する概念紹介ドキュメントに対するマイナーアップデートです。主な変更点は、日付の更新と新しい注意書きの追加です。

まず、ドキュメントの日付が「2025年5月27日」から「2025年8月21日」に変更され、最新の情報を反映するようになっています。この日付更新によりユーザーは、リソースが最新であることを確認しやすくなります。

次に、ナレッジストアがAzureストレージに存在し、Azure AI Searchのスキルセットの出力を含むことについての注意書きが新たに追加されています。この注意書きは、ナレッジソースやナレッジエージェントとは異なるものであり、エージェント型リトリーバルのワークフローにおける役割を明確にしています。この情報の追加により、ナレッジストアの理解が深まり、特にその使用方法や目的がよりしっかりと伝わるようになっています。

全体として、この修正はナレッジストアのコンセプトをより明確にし、ユーザーがこのリソースをどのように活用できるかを理解するのに役立つ情報を提供しています。

## articles/search/knowledge-store-connect-power-bi.md{#item-7ad25a}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: heidist
 manager: nitinme
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 05/27/2025
+ms.date: 08/21/2025
 ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
@@ -16,6 +16,9 @@ ms.custom:
 
 # Connect a knowledge store with Power BI
 
+> [!NOTE]
+> Knowledge stores exist in Azure Storage and contain the outputs of Azure AI Search skillsets. They're separate from knowledge sources and knowledge agents, which are used in [agentic retrieval](search-agentic-retrieval-concept.md) workflows.
+
 In this article, learn how to connect to and query a knowledge store using Power Query in the Power BI Desktop app. You can get started faster with templates, or build a custom dashboard from scratch.
 
 A knowledge store that's composed of tables in Azure Storage work best in Power BI. If the tables contain projections from the same skillset and projection group, you can easily "join" them to build table visualizations that include fields from related tables.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Power BIとのナレッジストア接続に関するドキュメントの更新"
}
```

### Explanation
この修正は、`knowledge-store-connect-power-bi.md`というPower BIとナレッジストアの接続に関するドキュメントに対するマイナーアップデートです。主な変更点は、日付の更新と新しい注意書きの追加です。

まず、ドキュメントの日付が「2025年5月27日」から「2025年8月21日」に変更され、最新の情報を反映しています。この変更により、ユーザーはリソースの更新状況を容易に把握できるようになります。

次に、新たに追加された注意書きでは、ナレッジストアがAzureストレージに存在し、Azure AI Searchのスキルセットの出力を含むことが明記されています。この注意書きは、ナレッジソースやナレッジエージェントとは異なるものであり、エージェント型リトリーバルワークフローでの使用方法が強調されています。この情報を通じて、ナレッジストアの役割と機能がより明確に理解されるようになります。

全体として、この修正はPower BIユーザーがナレッジストアをより効果的に利用するための情報を提供し、具体的な使用方法の理解を助けるものとなっています。

## articles/search/knowledge-store-create-portal.md{#item-9b92e5}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: haileytapia
 manager: nitinme
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 03/04/2025
+ms.date: 08/21/2025
 ms.update-cycle: 365-days
 ms.custom:
   - mode-ui
@@ -17,6 +17,9 @@ ms.custom:
 
 # Quickstart: Create a knowledge store in the Azure portal
 
+> [!NOTE]
+> Knowledge stores exist in Azure Storage and contain the outputs of Azure AI Search skillsets. They're separate from knowledge sources and knowledge agents, which are used in [agentic retrieval](search-agentic-retrieval-concept.md) workflows.
+
 In this quickstart, you create a [knowledge store](knowledge-store-concept-intro.md) that serves as a repository for output generated from an [AI enrichment pipeline](cognitive-search-concept-intro.md) in Azure AI Search. A knowledge store makes generated content available in Azure Storage for workloads other than search.
 
 First, you set up sample data in Azure Storage. Next, you run the **Import data** wizard to create an enrichment pipeline that also generates a knowledge store. The knowledge store contains original source content pulled from the data source (customer reviews of a hotel), plus AI-generated content that includes a sentiment label, key phrase extraction, and text translation of non-English customer comments.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureポータルでのナレッジストア作成に関するクイックスタートの更新"
}
```

### Explanation
この修正は、`knowledge-store-create-portal.md`というAzureポータルでのナレッジストア作成に関するクイックスタートドキュメントに対するマイナーアップデートです。主な変更点は、日付の更新と新しい注意書きの追加です。

まず、ドキュメントの日付が「2025年3月4日」から「2025年8月21日」に変更され、これにより内容が最新であることが示されています。この日付の更新は、ユーザーが常に最新の情報に基づいて作業できるようにするため重要です。

次に、新たに追加された注意書きにより、ナレッジストアがAzureストレージに存在し、Azure AI Searchのスキルセットから生成された出力を含むことが説明されています。この注意書きは、ナレッジソースやナレッジエージェントといった他の要素とは異なり、エージェント型リトリーバルワークフローにおけるナレッジストアの特別な役割を強調しています。この情報により、ユーザーはナレッジストアの機能をより理解しやすくなります。

全体として、この修正はAzureポータルを使ってナレッジストアを作成する際の手順とその背景に関する理解を深め、特にAIエンリッチメントパイプラインから生成されたコンテンツの用途についてのクリアな指針を提供します。

## articles/search/knowledge-store-create-rest.md{#item-2643dd}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/17/2025
+ms.date: 08/21/2025
 ms.custom:
   - ignite-2023
   - sfi-image-nochange
@@ -16,6 +16,9 @@ ms.custom:
 
 # Create a knowledge store using REST
 
+> [!NOTE]
+> Knowledge stores exist in Azure Storage and contain the outputs of Azure AI Search skillsets. They're separate from knowledge sources and knowledge agents, which are used in [agentic retrieval](search-agentic-retrieval-concept.md) workflows.
+
 In Azure AI Search, a [knowledge store](knowledge-store-concept-intro.md) is a repository of [AI-generated content](cognitive-search-concept-intro.md) that's used for non-search scenarios. You create the knowledge store using an indexer and skillset, and specify Azure Storage to store the output. After the knowledge store is populated, use tools like [Storage Explorer](/azure/vs-azure-tools-storage-manage-with-storage-explorer) or [Power BI](knowledge-store-connect-power-bi.md) to explore the content.
 
 In this article, you use the REST API to ingest, enrich, and explore a set of customer reviews of hotel stays in a knowledge store. The knowledge store contains original text content pulled from the source, plus AI-generated content that includes a sentiment score, key phrase extraction, language detection, and text translation of non-English customer comments.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTを使用したナレッジストア作成に関するドキュメントの更新"
}
```

### Explanation
この修正は、`knowledge-store-create-rest.md`というRESTを使用したナレッジストア作成に関するドキュメントに対するマイナーアップデートです。変更内容は、主に日付の更新と新しい注意書きの追加です。

最初に、ドキュメントの日付が「2025年6月17日」から「2025年8月21日」に変更され、最新の情報が反映されています。この日付の更新は、ユーザーが資料を参照する際に内容の新しさを確認できるため重要です。

次に、新しく追加された注意書きでは、ナレッジストアがAzureストレージに存在し、Azure AI Searchのスキルセットから生成された出力を含むことが説明されています。この注意書きは、ナレッジソースやナレッジエージェントとは異なり、エージェント型リトリーバルワークフローでのナレッジストアの特性を強調しています。この情報を提供することで、ユーザーはナレッジストアの機能をより明確に理解できるようになります。

全体として、この修正はREST APIを使用してナレッジストアを作成する手順に関する内容を最新化し、特にAIによって生成されたコンテンツについての理解を深める助けとなります。具体的には、ホテルの宿泊に関する顧客レビューを含む知識ストアの構築方法が詳述されています。

## articles/search/knowledge-store-projection-example-long.md{#item-e18999}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 07/28/2025
+ms.date: 08/21/2025
 ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
@@ -16,6 +16,9 @@ ms.custom:
 
 # Example of shapes and projections in a knowledge store
 
+> [!NOTE]
+> Knowledge stores exist in Azure Storage and contain the outputs of Azure AI Search skillsets. They're separate from knowledge sources and knowledge agents, which are used in [agentic retrieval](search-agentic-retrieval-concept.md) workflows.
+
 This article provides a detailed example that supplements [high-level concepts](knowledge-store-projection-overview.md) and [syntax-based articles](knowledge-store-projections-examples.md) by walking you through the shaping and projection steps required for fully expressing the output of a rich skillset in a [knowledge store](knowledge-store-concept-intro.md) in Azure Storage.
 
 If your application requirements call for multiple skills and projections, this example can give you a better idea of how shapes and projections interact.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジストアにおけるプロジェクションの例の更新"
}
```

### Explanation
この修正は、`knowledge-store-projection-example-long.md`というナレッジストアに関するプロジェクションの例を示すドキュメントに対するマイナーアップデートです。主な変更は、日付の更新と新しい注意書きの追加です。

まず、ドキュメントの日付が「2025年7月28日」から「2025年8月21日」に変更されており、これはドキュメントの情報を最新のものに保つために重要なステップです。この日付の更新により、ユーザーは参照する際に内容が新鮮であることを確認できます。

次に、新たに追加された注意書きでは、ナレッジストアがAzureストレージに存在し、Azure AI Searchのスキルセットから生成された出力を格納するものであることが説明されています。この注意書きは、ナレッジソースやナレッジエージェントとは異なることを強調し、エージェント型リトリーバルワークフローにおけるナレッジストアの役割を明確にしています。

この変更によって、ユーザーはナレッジストアの機能や、リッチスキルセットの出力を完全に表現するためのシェーピングおよびプロジェクションのステップについて深く理解できる内容となっています。全体として、このドキュメントはアプローチの理解を助けるための良いリソースとなります。

## articles/search/knowledge-store-projection-overview.md{#item-81aa4a}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 06/17/2025
+ms.date: 08/21/2025
 ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
@@ -16,6 +16,9 @@ ms.custom:
 
 # Knowledge store "projections" in Azure AI Search
 
+> [!NOTE]
+> Knowledge stores exist in Azure Storage and contain the outputs of Azure AI Search skillsets. They're separate from knowledge sources and knowledge agents, which are used in [agentic retrieval](search-agentic-retrieval-concept.md) workflows.
+
 Projections define the physical tables, objects, and files in a [**knowledge store**](knowledge-store-concept-intro.md) that accept content from an Azure AI Search enrichment pipeline. If you're creating a knowledge store, defining and shaping projections is most of the work.
 
 This article introduces projection concepts and workflow so that you have some background before you start coding.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジストアプロジェクションの概要に関するドキュメントの更新"
}
```

### Explanation
この修正は、`knowledge-store-projection-overview.md`というナレッジストアプロジェクションの概要を説明するドキュメントに対するマイナーアップデートです。変更の主な点は、日付の更新と新しい注意書きの追加です。

まず、ドキュメントの日付が「2025年6月17日」から「2025年8月21日」に更新されています。この変更は、情報を最新に保つために重要であり、ユーザーが参照する際の信頼性を高めます。

次に、新たに追加された注意書きでは、ナレッジストアがAzureストレージに存在し、Azure AI Searchのスキルセットから生成された出力を含むことが記されています。この説明は、ナレッジソースやナレッジエージェントとの違いを明確にし、エージェント型リトリーバルワークフローにおけるナレッジストアの役割を強調しています。

この変更により、読者はナレッジストアのプロジェクションがAzure AI Searchのエンリッチメントパイプラインからコンテンツを受け入れるための物理的なテーブルやオブジェクト、ファイルを定義する重要な要素であることを理解しやすくなります。また、このドキュメントはプロジェクションの概念やワークフローを紹介しており、コーディングを始める前の重要な背景知識を提供しています。全体として、これによりユーザーはナレッジストアの理解を深めることができる内容となっています。

## articles/search/knowledge-store-projection-shape.md{#item-2e47a8}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 06/17/2025
+ms.date: 08/21/2025
 ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
@@ -15,6 +15,9 @@ ms.custom:
 
 # Shaping data for projection into a knowledge store
 
+> [!NOTE]
+> Knowledge stores exist in Azure Storage and contain the outputs of Azure AI Search skillsets. They're separate from knowledge sources and knowledge agents, which are used in [agentic retrieval](search-agentic-retrieval-concept.md) workflows.
+
 In Azure AI Search, "shaping data" describes a step in the [knowledge store workflow](knowledge-store-concept-intro.md) that creates a data representation of the content that you want to project into tables, objects, and files in Azure Storage.
 
 As skills execute, the outputs are written to an enrichment tree in a hierarchy of nodes, and while you might want to view and consume the enrichment tree in its entirety, it's more likely that you'll want a finer grain, creating subsets of nodes for different scenarios, such as placing the nodes related to translated text or extracted entities in specific tables.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジストアプロジェクションシェイプに関するドキュメントの更新"
}
```

### Explanation
この修正は、`knowledge-store-projection-shape.md`というナレッジストアのプロジェクションシェイプに関するドキュメントに対するマイナーアップデートです。主に日付の更新と新しい注意書きの追加が行われました。

最初に、ドキュメントの日付が「2025年6月17日」から「2025年8月21日」に変更されています。この更新により、コンテンツが最新であることを示し、読者に対して信頼性を提供します。

次に追加された注意書きでは、ナレッジストアとはAzureストレージ内に存在し、Azure AI Searchのスキルセットからの出力を含むことが明示されています。また、ナレッジソースやナレッジエージェントとは別物であることも説明されています。この情報は、エージェント型リトリーバルワークフローにおけるナレッジストアの役割を理解するのに役立ちます。

修正された内容の中では、Azure AI Searchにおける「データのシェイピング」というプロセスが紹介されています。これは、Azureストレージ内のテーブルやオブジェクト、ファイルにプロジェクションするために必要なデータの表現を作成するステップです。スキルが実行されると、出力はエンリッチメントツリーに書き込まれ、異なるシナリオ用にノードのサブセットを生成することが可能であることが強調されています。

このように、修正されたドキュメントはナレッジストアの操作やデータの組織化に関する理解を深めるための重要な情報を提供し、アクセス可能な形で分かりやすくまとめられています。

## articles/search/knowledge-store-projections-examples.md{#item-9bfff5}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 06/17/2025
+ms.date: 08/21/2025
 ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
@@ -16,6 +16,9 @@ ms.custom:
 
 # Define projections in a knowledge store
 
+> [!NOTE]
+> Knowledge stores exist in Azure Storage and contain the outputs of Azure AI Search skillsets. They're separate from knowledge sources and knowledge agents, which are used in [agentic retrieval](search-agentic-retrieval-concept.md) workflows.
+
 [Projections](knowledge-store-projection-overview.md) are the component of a [knowledge store definition](knowledge-store-concept-intro.md) that determines how AI enriched content is stored in Azure Storage. Projections determine the type, quantity, and composition of the data structures containing your content.
 
 In this article, learn the syntax for each type of projection:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジストアのプロジェクション例に関するドキュメントの更新"
}
```

### Explanation
この修正は、`knowledge-store-projections-examples.md`というナレッジストアのプロジェクション例に関するドキュメントに対するマイナーアップデートです。主な変更点は、日付の更新と新しい注意書きの追加です。

最初に、ドキュメントの日付が「2025年6月17日」から「2025年8月21日」に変更されました。この日付の更新により、コンテンツが最新であることが示され、読者に対して信頼性を向上させます。

加えて、ドキュメントに新しい注意書きが追加され、ナレッジストアがAzureストレージに存在し、Azure AI Searchのスキルセットからの出力を含むことが強調されています。この情報は、ナレッジソースやナレッジエージェントとの違いを明確にし、エージェント型リトリーバルワークフローにおけるナレッジストアの機能をよりよく理解するのに役立ちます。

修正された内容の中では、プロジェクションがナレッジストア定義の一部であり、AIによって強化されたコンテンツがAzureストレージにどのように保存されるかを決定する要素であることが説明されています。また、プロジェクションはデータ構造の種類、量、構成を決定する役割を持っていることが明示されています。

このように、このドキュメントの変更により、ナレッジストアにおけるプロジェクションの定義とその役割について、より深い理解を得ることができる内容になっています。

## articles/search/search-agentic-retrieval-concept.md{#item-797a22}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about agentic retrieval concepts, architecture, and use cases
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 08/18/2025
+ms.date: 09/02/2025
 ms.service: azure-ai-search
 ms.topic: concept-article
 ms.custom:
@@ -21,13 +21,13 @@ In Azure AI Search, *agentic retrieval* is a new multi-query pipeline designed f
 
 + Uses a large language model (LLM) to break down a complex query into smaller, focused subqueries for better coverage over your indexed content. Subqueries can include chat history for extra context.
 
-+ Runs the multiple subqueries in parallel. Each subquery is semantically reranked to find the most relevant matches.
++ Runs subqueries in parallel. Each subquery is semantically reranked to promote the most relevant matches.
 
-+ Combines the best results into a unified response that your LLM can use to generate answers with your proprietary content.
++ Combines the best results into a unified response that an LLM can use to generate answers with your proprietary content.
 
 This high-performance pipeline helps you generate high quality grounding data for your chat application, with the ability to answer complex questions quickly.
 
-Programmatically, agentic retrieval is supported through a new [Knowledge Agents object](/rest/api/searchservice/knowledge-agents?view=rest-searchservice-2025-05-01-preview&preserve-view=true) in the 2025-05-01-preview data plane REST API and in Azure SDK preview packages that provide the feature. A knowledge agent's retrieval response is designed for downstream consumption by other agents and chat apps.
+Programmatically, agentic retrieval is supported through a new [Knowledge Agents object](/rest/api/searchservice/knowledge-agents?view=rest-searchservice-2025-08-01-preview&preserve-view=true) in the 2025-08-01-preview and 2025-05-01-preview data plane REST APIs and in Azure SDK preview packages that provide the feature. A knowledge agent's retrieval response is designed for downstream consumption by other agents and chat apps.
 
 ## Why use agentic retrieval
 
@@ -67,7 +67,7 @@ The agentic retrieval process follows three main phases:
 
 1. **Query planning**: A knowledge agent sends your query and conversation history to an LLM (gpt-4o or gpt-4.1 series), which analyzes the context and breaks down complex questions into focused subqueries. This step is automated and not customizable. The number of subqueries depends on what the LLM decides and whether the `maxDocsForReranker` parameter is higher than 50. A new subquery is defined for each 50-document batch sent to semantic ranker.
 
-2. **Query execution**: All subqueries run simultaneously against your search index, using keyword, vector, and hybrid search. Each subquery undergoes semantic reranking to find the most relevant matches. References are extracted and retained for citation purposes.
+2. **Query execution**: All subqueries run simultaneously against your knowledge sources, using keyword, vector, and hybrid search. Each subquery undergoes semantic reranking to find the most relevant matches. References are extracted and retained for citation purposes.
 
 3. **Result synthesis**: The system merges and ranks all results, then returns a unified response containing grounding data, source references, and execution metadata.
 
@@ -81,6 +81,7 @@ Your search index determines query execution and any optimizations that occur du
 | **Knowledge agent** | Azure AI Search | Orchestrates the pipeline, connecting to your LLM and managing query parameters |
 | **Search index** | Azure AI Search | Stores your searchable content (text and vectors) with semantic configuration |
 | **Semantic ranker** | Azure AI Search | Required component that reranks results for relevance (L2 reranking) |
+| **Knowledge source** | Azure AI Search | Wraps the search index with properties pertaining to knowledge agent usage |
 
 ### Integration requirements
 
@@ -106,11 +107,16 @@ Choose any of these options for your next step.
 
 + How-to guides for a focused look at development tasks:
 
+  + [Create a search index knowledge source](search-knowledge-source-how-to-index.md) or a [blob knowledge source](search-knowledge-source-how-to-blob.md)
   + [Create a knowledge agent](search-agentic-retrieval-how-to-create.md)
   + [Use a knowledge agent to retrieve data](search-agentic-retrieval-how-to-retrieve.md)
-  + [Build an agent-to-agent retrieval solution](search-agentic-retrieval-how-to-pipeline.md).
+  + [Build an agent-to-agent retrieval solution](search-agentic-retrieval-how-to-pipeline.md)
 
-+ REST API reference, [Knowledge Agents](/rest/api/searchservice/knowledge-agents?view=rest-searchservice-2025-05-01-preview&preserve-view=true) and [Knowledge Retrieval](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
++ REST API reference:
+
+  + [Knowledge Sources](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-08-01-preview&preserve-view=true)
+  + [Knowledge Agents](/rest/api/searchservice/knowledge-agents?view=rest-searchservice-2025-08-01-preview&preserve-view=true)
+  + [Knowledge Retrieval](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true)
 
 + [Azure OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo), updated to use agentic retrieval.
 
@@ -120,7 +126,7 @@ Agentic retrieval is available in [all regions that provide semantic ranker](sea
 
 Billing for agentic retrieval has two parts:
 
-+ Billing for query planning is pay-as-you-go in Azure OpenAI. It's token based for both input and output tokens. The model you assign to the knowledge agent is the one charged for token usage. For example, if you use gpt-4o, the token charge appears in the bill for gpt-4o.
++ Billing for query planning and [answer synthesis](search-agentic-retrieval-how-to-synthesize.md) (optional) is pay-as-you-go in Azure OpenAI. It's token based for both input and output tokens. The model you assign to the knowledge agent is the one charged for token usage. For example, if you use gpt-4o, the token charge appears in the bill for gpt-4o.
 
 + Billing for semantic ranking during query execution. Billing is suspended during the initial roll-out phase but then transitions to pay-as-you-go on the Azure AI Search side through the semantic ranker. Semantic ranker, which is a premium billable feature, is an integral part of agentic retrieval. You're charged on the Azure AI Search side for token inputs to the semantic ranking models.
 
@@ -138,9 +144,9 @@ Semantic ranking is performed for every subquery in the plan. Semantic ranking c
 
 ### Example: Estimate costs
 
-Agentic retrieval has two billing models: billing from Azure OpenAI (query planning) and billing from Azure AI Search for semantic ranking (query execution).
+Agentic retrieval has two billing models: billing from Azure OpenAI (query planning and, if enabled, answer synthesis) and billing from Azure AI Search for semantic ranking (query execution).
 
-The prices shown in this article are hypothetical. They're used to illustrate the estimation process. Your costs could be lower. For the actual price of transactions, see [Azure OpenAI pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing). For query execution, there's no charge for semantic ranking for agentic retrieval in the initial public preview.
+This example omits answer synthesis and uses hypothetical prices to illustrate the estimation process. Your costs could be lower. For the actual price of transactions, see [Azure OpenAI pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing). For query execution, there's no charge for semantic ranking for agentic retrieval in the initial public preview.
 
 #### Estimated billing costs for query planning
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルに関するコンセプトドキュメントの更新"
}
```

### Explanation
この修正は、`search-agentic-retrieval-concept.md`というエージェンティックリトリーバルに関するコンセプトのドキュメントに対するマイナーアップデートです。主な変更点は、日付の更新、新しい情報の追加、用語の修正、さらには整合性の向上です。

まず、ドキュメントの日付が「2025年8月18日」から「2025年9月2日」に変更されました。この日付の更新により、コンテンツが最新であることが示され、読者に対する信頼性が高まります。

次に、新しい情報が追加され、エージェンティックリトリーバルのプロセスに関する説明が強化されました。具体的には、大規模言語モデル（LLM）を使用して複雑なクエリを小さなサブクエリに分解し、インデックスされたコンテンツに対するより良いカバレッジを提供することが述べられています。また、サブクエリは並行して実行され、各サブクエリが意味的に再ランキングされて最も関連性の高いマッチを見つけることが確認されています。

使用する技術の整合性も向上しました。たとえば、知識エージェントのプログラミングサポートが、更新されたAPIのバージョンである「2025-08-01-preview」に対応するように変更されています。このAPIは、他のエージェントやチャットアプリケーションへの利用を意図した取得応答を提供します。

さらに、費用に関する記述も更新され、クエリ計画に対する請求がオプションの「回答合成」にも適用されることが追加されました。これにより、ユーザーはエージェンティックリトリーバルのコストについてより明確に理解できるようになります。

これらの修正により、エージェンティックリトリーバルに関する理解が深まり、技術的要素が明確に示されています。ドキュメントは、ユーザーがこの機能を活用するための有益なガイドとなります。

## articles/search/search-agentic-retrieval-how-to-create.md{#item-310fbe}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/30/2025
+ms.date: 08/29/2025
 ---
 
 # Create a knowledge agent in Azure AI Search
@@ -18,12 +18,15 @@ In Azure AI Search, a *knowledge agent* is a top-level resource representing a c
 
 A knowledge agent specifies:
 
-+ A model that provides reasoning capabilities
-+ A target search index used at query time
-+ Parameters on the index for setting default behaviors and response shaping
++ A knowledge source (one or more) that points to a searchable content
++ A chat completion model that provides reasoning capabilities for query planning and answer formulation
++ Properties for performance optimization (constrain query processing time)
 
 After you create a knowledge agent, you can update its properties at any time. If the knowledge agent is in use, updates take effect on the next job.
 
+> [!IMPORTANT]
+> 2025-08-01-preview introduces breaking changes for existing knowledge agents. This preview version requires one or more `knowledgeSource` definitions. We recommend [migrating existing code](search-agentic-retrieval-how-to-migrate.md) to the new APIs as soon as possible.
+
 ## Prerequisites
 
 + Familiarity with [agentic retrieval concepts and use cases](search-agentic-retrieval-concept.md).
@@ -32,17 +35,17 @@ After you create a knowledge agent, you can update its properties at any time. I
 
 + Azure AI Search, in any [region that provides semantic ranker](search-region-support.md), on the basic pricing tier or higher. Your search service must have a [managed identity](search-how-to-managed-identities.md) for role-based access to the model.
 
-+ Permissions on Azure AI Search. **Search Service Contributor** can create and manage a knowledge agent. **Search Index Data Reader** can run queries. Instructions are provided in this article.
++ Permissions on Azure AI Search. **Search Service Contributor** can create and manage a knowledge agent. **Search Index Data Reader** can run queries. Instructions are provided in this article. [Quickstart: Connect to a search service](/azure/search/search-get-started-rbac?pivots=rest) explains how to configure roles and get a personal access token for REST calls.
 
-+ A search index containing plain text or vectors. The index must [meet the requirements for agentic retrieval](search-agentic-retrieval-how-to-index.md), including a [semantic configuration](semantic-how-to-configure.md) with the `defaultConfiguration` specified.
++ A [knowledge source](search-knowledge-source-overview.md) that identifies searchable content used by the agent. It can be either a [search index knowledge source](search-knowledge-source-how-to-index.md) or a [blob knowledge source](search-knowledge-source-how-to-blob.md)
 
-+ API requirements. To create or use a knowledge agent, use the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API. Or, use a prerelease package of an Azure SDK that provides knowledge agent APIs: [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta3-2025-03-25), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
++ API requirements. To create or use a knowledge agent, use the [2025-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) data plane REST API. Or, use a preview package of an Azure SDK that provides knowledge agent APIs: [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta3-2025-03-25), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md). **There's no Azure portal support knowledge agents at this time**.
 
-To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending preview REST API calls to Azure AI Search. There's no portal support at this time.
+To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending preview REST API calls to Azure AI Search. T
 
 ## Deploy a model for agentic retrieval
 
-Make sure you have a supported model that Azure AI Search can access. The following instruction assumes Azure AI Foundry Model as the provider.
+Make sure you have a supported model that Azure AI Search can access. The following instructions assume Azure AI Foundry Model as the provider.
 
 1. Sign in to [Azure AI Foundry portal](https://ai.azure.com/?cid=learnDocs).
 
@@ -83,7 +86,7 @@ In Azure, you must have **Owner** or **User Access Administrator** permissions o
     @accessToken=<YOUR PERSONAL ID>
     
     # List Indexes
-    GET https://{{search-url}}/indexes?api-version=2025-05-01-preview
+    GET https://{{search-url}}/indexes?api-version=2025-08-01-preview
     Authorization: Bearer {{accessToken}}
     ```
 
@@ -103,7 +106,7 @@ You can use API keys if you don't have permission to create role assignments.
     @search-api-key=<YOUR SEARCH SERVICE ADMIN API KEY>
 
    # List Indexes
-   GET https://{{search-url}}/indexes?api-version=2025-05-01-preview
+   GET {{search-url}}/indexes?api-version=2025-08-01-preview
       Content-Type: application/json
       @api-key: {{search-api-key}}
    ```
@@ -112,11 +115,9 @@ You can use API keys if you don't have permission to create role assignments.
 
 The following request lists knowledge agents by name. Within the knowledge agents collection, all knowledge agents must be uniquely named. It's helpful to know about existing knowledge agents for reuse or for naming new agents.
 
-<!-- ### [**REST APIs**](#tab/rest-get) -->
-
 ```http
 # List knowledge agents
-GET https://{{search-url}}/agents?api-version=2025-05-01-preview
+GET {{search-url}}/agents?api-version=2025-08-01-preview
    Content-Type: application/json
    Authorization: Bearer {{accessToken}}
 ```
@@ -125,41 +126,52 @@ You can also return a single agent by name to review its JSON definition.
 
 ```http
 # Get knowledge agent
-GET https://{{search-url}}/agents/{{agent-name}}?api-version=2025-05-01-preview
+GET {{search-url}}/agents/{{agent-name}}?api-version=2025-08-01-preview
    Content-Type: application/json
    Authorization: Bearer {{accessToken}}
 ```
 
-<!-- --- -->
-
 ## Create a knowledge agent
 
-A knowledge agent represents a connection between a model that you've deployed in Azure OpenAI and a target index on Azure AI Search. Parameters on the model establish the connection. Parameters on the index establish defaults that inform query execution and the response.
+A knowledge agent drives the agentic retrieval pipeline. In application code, it's called by other agents or chat bots. 
 
-<!-- ### [**REST APIs**](#tab/rest-create) -->
+Its composition consists of connections between *knowledge sources* (searchable content) and chat completion models that you've deployed in Azure OpenAI. Properties on the model establish the connection. Properties on the knowledge source establish defaults that inform query execution and the response.
 
-To create an agent, use the 2025-05-01-preview data plane REST API or an Azure SDK prerelease package that provides equivalent functionality.
+To create an agent, use the 2025-08-01-preview data plane REST API or an Azure SDK preview package that provides equivalent functionality.
 
 ```http
 @search-url=<YOUR SEARCH SERVICE URL>
 @agent-name=<YOUR AGENT NAME>
 @index-name=<YOUR INDEX NAME>
 @model-provider-url=<YOUR AZURE OPENAI RESOURCE URI>
+@model-api-key=<YOUR AZURE OPENAI API KEY>
 @accessToken = <a long GUID>
 
 # Create knowledge agent
-PUT https://{{search-url}}/agents/{{agent-name}}?api-version=2025-05-01-preview
+PUT {{search-url}}/agents/{{agent-name}}?api-version=2025-08-01-preview
    Content-Type: application/json
    Authorization: Bearer {{accessToken}}
 
 {
     "name" : "{{agent-name}}",
-    "targetIndexes" : [
+    "description": "This knowledge agent handles questions directed at two unrelated sample indexes."
+    "retrievalInstructions": "Use the hotels knowledge source only for queries about hotels or where to stay, otherwise use the earth at night knowledge source.",
+    "knowledgeSources": [
         {
-            "indexName" : "{{index-name}}",
-            "defaultRerankerThreshold": 2.5,
-            "defaultIncludeReferenceSourceData": true,
-            "defaultMaxDocsForReranker": 200
+            "name": "earth-at-night-blob-ks",
+            "alwaysQuerySource": false,
+            "includeReferences": true,
+            "includeReferenceSourceData": true,
+            "maxSubQueries": 30,
+            "rerankerThreshold": null
+        },
+        {
+            "name": "hotels-index-ks",
+            "alwaysQuerySource": false,
+            "includeReferences": true,
+            "includeReferenceSourceData": true,
+            "maxSubQueries": 5,
+            "rerankerThreshold": null
         }
     ],
     "models" : [ 
@@ -173,37 +185,53 @@ PUT https://{{search-url}}/agents/{{agent-name}}?api-version=2025-05-01-preview
             }
         }
     ],
+    "outputConfiguration": {
+        "modality": "extractiveData",
+        "answerInstructions": "Provide a concise answer to the question.",
+        "attemptFastPath": false,
+        "includeActivity": true
+    },
     "requestLimits": {
         "maxOutputSize": 5000,
         "maxRuntimeInSeconds": 60
-    },
-    "encryptionKey": { }
+    }
 }
 ```
 
 **Key points**:
 
 + `name` must be unique within the knowledge agents collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects on Azure AI Search.
 
-+ `targetIndexes` is required for knowledge agent creation. It lists the search indexes that can use the knowledge agent. Currently in this preview release, the `targetIndexes` array can contain only one index. *It must have a default semantic configuration* (`defaultConfiguration`). For more information, see [Design an index for agentic retrieval](search-agentic-retrieval-how-to-index.md).
++ `description` is recommended for query planning. The LLM uses the description to inform query planning. 
 
-    ```json
-    "semantic": {
-        "defaultConfiguration": "my-default-semantic-config",
-        "configurations": [ ]
-    }
-    ```
++ `retrievalInstructions` is recommended for query planning when you have multiple knowledge sources. The instructions are passed as a prompt to the LLM to determine whether a knowledge source should be in scope for a query. This field influences both knowledge source selection and query formulation. For example, instructions could append information or prioritize a knowledge source. Instructions are passed directly to the LLM, which means it's possible to provide instructions that break query planning (for example, if instructions resulted in bypassing an essential knowledge source). If you set `retrievalInstructions`, make sure `alwaysQuerySource` is set to false.
 
-+ `defaultRerankerThreshold` is the minimum semantic reranker score that's acceptable for inclusion in a response. [Reranker scores](semantic-search-overview.md#how-results-are-scored) range from 1 to 4. Plan on revising this value based on testing and what works for your content.
++ `knowledgeSources` is required for knowledge agent creation. It specifies the search indexes or Azure blobs used by the knowledge agent. New in this preview release, the `knowledgeSources` is an array, and it replaces the previous `targetIndexes` array. 
 
-+ `defaultIncludeReferenceSourceData` is a boolean that determines whether the reference portion of the response includes source data. We recommend starting with this value set to true if you want to shape your own response using output from the search engine. Otherwise, if you want to use the output in the response `content` string, you can set it to false.
+    + `name` is a reference to either a [search index knowledge source](search-knowledge-source-how-to-index.md) or a [blob knowledge source](search-knowledge-source-how-to-blob.md).
+    
+    + `alwaysQuerySource` is a boolean that specifies whether a knowledge source must always be used (true), or only used if the query planning step determines it's useful. The default is false, which means source selection can skip this source if the model doesn’t think the query needs it. Source descriptions and retrieval instructions are used in this assessment. If you're using `attemptFastPath` on a specific knowledge source, `alwaysQuerySource` must be set to true.
+    
+    + `includeReferences` is a boolean that determines whether the reference portion of the response includes source data. We recommend starting with this value set to true if you want to shape your own response using output from the search engine. Otherwise, if you want to use the output in the response `content` string, you can set it to false.
+    
+    + `maxSubQueries` is the maximum number of queries the query planning step will generate. Each query can return up to 50 documents, which are reranked by semantic ranker. The `maxSubQueries` property must be between 2 and 40.
 
-+ `defaultMaxDocsForReranker` is the maximum number of documents that can be sent to the semantic ranker. Each subquery can pass a maximum of 50 documents to the semantic reranker, so setting this value above 50 generates more subqueries until the maximum is reached. For example, if you set this value to 200, then four subqueries are generated to support this number. This 
+    + `rerankerThreshold` is the minimum semantic reranker score that's acceptable for inclusion in a response. [Reranker scores](semantic-search-overview.md#how-results-are-scored) range from 1 to 4. Plan on revising this value based on testing and what works for your content.
 
 + `models` specifies one or more connections to an existing gpt-4o or gpt-4o-mini model. Currently in this preview release, models can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Azure AI Foundry portal or from a command line request. You can use role-based access control instead of API keys for the Azure AI Search connection to the model. For more information, see [How to deploy Azure OpenAI models with Azure AI Foundry](/azure/ai-foundry/how-to/deploy-models-openai).
 
++ `outputConfiguration` gives you control over query execution logic and output.
+
+  + `modality` determines the shape of the results. Valid values are `extractiveData` (default) or `answerSynthesis` (see [Use answer synthesis for citation-backed responses](search-agentic-retrieval-how-to-synthesize.md)).
+
+  + `answerInstructions` is used for shaping answers (see [Use answer synthesis for citation-backed responses](search-agentic-retrieval-how-to-synthesize.md)). The default is null.
+
+  + `attemptFastPath` is a boolean that can be used to enable a fast path to query execution. If `true`, the search engine skips query planning if the query is less than 512 characters and the semantic ranker score on the small query is above 1.9, indicating sufficient relevance. If the query is larger or the score is lower, query planning is invoked. You must have at least one knowledge source that has `alwaysQuerySource` enabled. If there are multiple knowledge sources, they must all have `alwaysQuerySource` enabled to be considered for fast path. The small query runs on all of them. The default is `false`.
+
+  + `includeActivity` indicates whether retrieval results should include the query plan. The default is `true`.
+
 <!--  Check minimum 10k  -->
-+ `requestLimits` gives you control over the output generated during retrieval so that you can better manage inputs to the LLM. 
++ `requestLimits` sets numeric limits over query processing.
 
   + `maxOutputSize` is the maximum number of tokens in the response `content` string, with 5,000 tokens as the minimum and recommended value, and no explicit maximum. The most relevant matches are preserved but the overall response is truncated at the last complete document to fit your token budget. 
 
@@ -213,15 +241,70 @@ PUT https://{{search-url}}/agents/{{agent-name}}?api-version=2025-05-01-preview
 
 <!-- --- -->
 
-## Confirm knowledge agent operations
+## Query the knowledge agent
+
+Call the **retrieve** action on the knowledge agent object to confirm the model connection and return a response. Use the [2025-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) data plane REST API or an Azure SDK preview package that provides equivalent functionality for this task.
+
+Replace "where does the ocean look green?" with a query string that's valid for your search index.
+
+```http
+# Send grounding request
+POST {{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-08-01-preview
+   Content-Type: application/json
+   Authorization: Bearer {{accessToken}}
 
-Call the **retrieve** action on the knowledge agent object to confirm the model connection and return a response. Use the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API or an Azure SDK prerelease package that provides equivalent functionality for this task.
+{
+  "messages" : [
+        { "role" : "assistant",
+                "content" : [
+                  { "type" : "text", "text" : "Use the earth at night index to answer the question. If you can't find relevant content, say you don't know." }
+                ]
+        },
+        {
+            "role" : "user",
+            "content" : [
+                {
+                    "text" : "where does the ocean look green?",
+                    "type" : "text"
+                }
+            ]
+        }
+    ],
+  "knowledgeSourceParams": [
+    {
+      "filterAddOn": null,
+      "knowledgeSourceName": "earth-at-night-blob-ks",
+      "kind": "searchIndex"
+    }
+  ]
+}
+```
+
+[messages](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview#knowledgeagentmessage&preserve-view=true) is required, but you can run this example using just "user" role that provides the query.
+
+[`knowledgeSourceParams`](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview#searchindexknowledgesourceparams&preserve-view=true) is optional. Specify a knowledge source if the agent is configured for multiple sources and you want to focus the retrieve action on just one of them.
 
-Replace "What are my vision benefits?" with a query string that's valid for your search index.
+A knowledge source specification on the retrieve action describes the target search index on the search service. So even if the knowledge source "kind" is Azure blob, the valid value here is `searchIndex`. In this first public preview release, `knowledgeSourceParams.kind` is always `searchIndex`.
+
+The response to the previous query might look like this:
 
 ```http
+  "response": [
+    {
+      "content": [
+        {
+          "type": "text",
+          "text": "The ocean appears green off the coast of Antarctica due to phytoplankton flourishing in the water, particularly in Granite Harbor near Antarctica’s Ross Sea, where they can grow in large quantities during spring, summer, and even autumn under the right conditions [ref_id:0]. Additionally, off the coast of Namibia, the ocean can also look green due to blooms of phytoplankton and yellow-green patches of sulfur precipitating from bacteria in oxygen-depleted waters [ref_id:1]. In the Strait of Georgia, Canada, the waters turned bright green due to a massive bloom of coccolithophores, a type of phytoplankton [ref_id:5]. Furthermore, a milky green and blue bloom was observed off the coast of Patagonia, Argentina, where nutrient-rich waters from different currents converge [ref_id:6]. Lastly, a large bloom of cyanobacteria was captured in the Baltic Sea, which can also give the water a green appearance [ref_id:9]."
+        }
+      ]
+    }
+  ],
+```
+
+
+<!-- ```http
 # Send grounding request
-POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-05-01-preview
+POST {{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-08-01-preview
    Content-Type: application/json
    Authorization: Bearer {{accessToken}}
 
@@ -250,7 +333,7 @@ POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-05-0
         } 
     ]
 }
-```
+``` -->
 
 For more information about the **retrieve** API and the shape of the response, see [Retrieve data using a knowledge agent in Azure AI Search](search-agentic-retrieval-how-to-retrieve.md).
 
@@ -260,7 +343,7 @@ If you no longer need the agent, or if you need to rebuild it on the search serv
 
 ```http
 # Delete agent
-DELETE https://{{search-url}}/agents/{{agent-name}}?api-version=2025-05-01-preview
+DELETE {{search-url}}/agents/{{agent-name}}?api-version=2025-08-01-preview
    Authorization: Bearer {{accessToken}}
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ナレッジエージェントの作成に関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-agentic-retrieval-how-to-create.md`というナレッジエージェントの作成方法に関するドキュメントに対する大幅な更新を含んでいます。この変更により、既存のナレッジエージェントとAPIの利用方法に重要なブレイキングチェンジが導入されました。

主な変更点には、ナレッジエージェントのプロパティとAPIの仕様変更が含まれています。具体的には、以下のような点があります：

1. **日付の更新**: ドキュメントの日付が「2025年5月30日」から「2025年8月29日」に変更され、最新の情報を反映しています。

2. **プロパティの変更**: ナレッジエージェントは、検索可能なコンテンツを指し示す「知識ソース」や、クエリ計画と回答の形成に必要な「チャット完了モデル」を指定するように更新されました。また、性能最適化のためのプロパティも追加されています。

3. **重要な注意喚起**: 「2025-08-01-preview」バージョンでは、既存のナレッジエージェントに対するブレイキングチェンジが導入されており、一つ以上の`knowledgeSource`の定義が必須とされています。これにより、ユーザーは速やかにコードの移行を行うことが推奨されています。

4. **新しい依存関係**: 新しいナレッジソースの仕様により、ナレッジエージェントは複数の知識ソースを持つことができ、これが生成するクエリの選択や形成に影響を与えるようになっています。

5. **APIバージョンの更新**: APIのバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更され、エージェントの作成や操作に新しいエンドポイントが導入されました。

これらの変更により、ドキュメントはナレッジエージェントの作成と管理に必要な最新の機能と手法を反映しています。また、提供される情報は、ユーザーがこの機能を利用するための明確なガイドとなります。

## articles/search/search-agentic-retrieval-how-to-index.md{#item-a078ea}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/05/2025
+ms.date: 08/29/2025
 ---
 
 # Design an index for agentic retrieval in Azure AI Search
@@ -16,18 +16,28 @@ ms.date: 05/05/2025
 
 In Azure AI Search, *agentic retrieval* is a new parallel query architecture that uses a chat completion model for query planning, generating subqueries that broaden the scope of what's searchable and relevant.
 
-Queries are created internally. Certain aspects of those generated queries are determined by your search index. This article explains which index elements affect agentic retrieval. None of the required elements are new or specific to agentic retrieval, which means you can use an existing index if it meets the criteria identified in this article, even if it was created using earlier API versions.
+Subqueries are created internally. Certain aspects of the subqueries are determined by your search index. This article explains which index elements have an effect on agentic retrieval. None of the required elements are new or specific to agentic retrieval, which means you can use an existing index if it meets the criteria identified in this article, even if it was created using earlier API versions.
 
-Summarized, the search index specified in the `targetIndexes` of an [agent definition](search-agentic-retrieval-how-to-create.md) must have these elements:
+A search index that's used in agentic retrieval is specified as *knowledge source* and is either:
+
++ An existing indexing containing searchable content. This index is made available to agentic retrieval through a [search index knowledge source](search-knowledge-source-how-to-index.md) definition.
+
++ A generated index created from a generated blob indexer pipeline. This index is generated and populated using information from a [blob knowledge source](search-knowledge-source-how-to-blob.md). It's based on a template that meets all of the criteria for knowledge agents and agentic retrieval. 
+
+## Criteria for agentic retrieval
+
+An index that's used in agentic retrieval must have these elements:
 
 + String fields attributed as `searchable` and `retrievable`
 + A semantic configuration, with a `defaultSemanticConfiguration`
-+ A vectorizer if you want to include vector queries in the pipeline
++ Vector fields and a vectorizer if you want to include vector queries in the pipeline
+
+It should also have fields that can be used for citations, such as  document or file name, page or chapter name, or at least a chunk ID.
 
 Optionally, the following index elements increase your opportunities for optimization:
 
 + `scoringProfile` with a `defaultScoringProfile`, for boosting relevance
-+ `synonymMaps` for terminology or jargon
++ `synonymMaps` for terminology or jargon 
 + `analyzers` for linguistics rules or patterns (like whitespace preservation, or special characters)
 
 ## Example index definition
@@ -139,9 +149,11 @@ Here's an example index that works for agentic retrieval. It meets the criteria
 
 **Key points**:
 
-In agentic retrieval, a large language model (LLM) is used twice. First, it's used to create a query plan. After the query plan is executed and search results are generated, those results are passed to the LLM again, this time as grounding data. LLMs consume and emit tokenized strings of human readable plain text content. For this reason, you must have `searchable` fields that provide plain text strings, and are `retrievable` in the response.
+In agentic retrieval, a large language model (LLM) is used twice. First, it's used to create a query plan. After the query plan is executed and search results are generated, those results are passed to the LLM again, this time as grounding data that's used to formulate an answer. 
+
+LLMs consume and emit tokenized strings of human readable plain text content. For this reason, you must have `searchable` fields that provide plain text strings, and are `retrievable` in the response. Vector fields and vector search are also important because they add similarity search to information retrieval. Vectors enhance and improve the quality of search, but aren't otherwise strictly required. Azure AI Search has built-in capabilities that [simplify and automate vectorization](vector-search-overview.md).
 
-This index includes a vector field that's used at query time. You don't need the vector in results because it isn't human or LLM readable, but it does need to be `searchable`. Since you don't need vectors in the response, both `retrievable` and `stored` are false. 
+The previous example index includes a vector field that's used at query time. You don't need the vector in results because it isn't human or LLM readable, but notice that its `searchable` for vector search. Since you don't need vectors in the response, both `retrievable` and `stored` are false. 
 
 The vectorizer defined in the vector search configuration is critical. It determines whether your vector field is used during query execution. The vectorizer encodes subqueries into vectors at query time for similarity search over the vectors. The vectorizer must be the same embedding model used to create the vectors in the index.
 
@@ -269,7 +281,7 @@ Here's an example of a vectorizer that works for agentic retrieval, as it appear
 
 [Scoring profiles](index-add-scoring-profiles.md) are criteria for relevance boosting. They're applied to non-vector fields (text and numbers) and are evaluated during query execution, although the precise behavior depends on the API version used to create the index.
 
-If you create the index using 2025-05-01-preview, the scoring profile executes last. If the index is created using an earlier API version, scoring profiles are evaluated before semantic reranking.
+If you create the index using 2025-05-01-preview or later, the scoring profile executes last. If the index is created using an earlier API version, scoring profiles are evaluated before semantic reranking.
 
 You can use any scoring profile that makes sense for your index. Here's an example of one that boosts the search score of a match if the match is found in a specific field. Fields are weighted by boosting multipliers. For example if a match was found in the "Category" field, the boosted score is multiplied by 5.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルのためのインデックス設計に関するドキュメント更新"
}
```

### Explanation
この修正は、`search-agentic-retrieval-how-to-index.md`というエージェンティックリトリーバルのためのインデックス設計に関するドキュメントに対するマイナーアップデートです。主に日付の更新といくつかの内容の修正が行われています。

まず、ドキュメントの日付が「2025年5月5日」から「2025年8月29日」に変更され、内容が最新であることを示しています。

次に、テキストのいくつかの部分が明確化されており、特にサブクエリ、知識ソース、インデックスの要件に関する説明が改善されています。具体的には、エージェンティックリトリーバルで使用されるインデックスが、「知識ソース」として指定されることが強調されています。また、インデックスが持つべき要素として、`searchable`および`retrievable`として設定された文字列フィールド、セマンティック構成、そしてベクトルフィールドとベクトライザーの重要性が強調されています。

さらに、インデックス設計の具体的な例が提供されており、これによりユーザーがエージェンティックリトリーバルの要件に合ったインデックスを設計しやすくなっています。

全体として、これらの変更はドキュメントの明確性を向上させ、ユーザーがエージェンティックリトリーバルのためのインデックス設計を理解しやすくするための貴重な情報を提供しています。

## articles/search/search-agentic-retrieval-how-to-migrate.md{#item-4011b8}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,192 @@
+---
+title: Migrate Agentic Retrieval Code
+titleSuffix: Azure AI Search
+description: Learn how to migrate your agentic retrieval code to the latest REST API version. Starting with the 2025-08-01-preview, you must update knowledge agents to use knowledgeSources instead of targetIndexes due to breaking changes.
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: how-to
+ms.date: 08/28/2025
+---
+
+# Migrate agentic retrieval code to the latest version
+
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+If you wrote [agentic retrieval](search-agentic-retrieval-concept.md) code using an early preview REST API, this article explains when and how to migrate to the latest version. It also describes breaking and nonbreaking changes for all REST API versions that support agentic retrieval.
+
+## When to migrate
+
+Migrate your agentic retrieval code when any of the following apply:
+
++ The REST API version you use is announced for retirement or enters a deprecation window.
+
++ A newer REST API version introduces breaking changes that affect features you use. For example, you must address breaking changes if your code targets the [2025-05-01-preview](#2025-05-01-preview), which uses `targetIndexes` in agent definitions.
+
++ You want features that are only available in a newer REST API version.
+
++ Your code fails when unrecognized properties are returned in a REST API response. As a best practice, your application should ignore properties it doesn't understand.
+
+## How to migrate
+
+If you created a knowledge agent using the [2025-05-01-preview](#2025-05-01-preview), your agent's definition includes an inline `targetIndexes` array and an optional `defaultMaxDocsForReranker` property.
+
+Starting with the [2025-08-01-preview](#2025-08-01-preview), reusable knowledge sources replace `targetIndexes`, and `defaultMaxDocsForReranker` is no longer supported. These breaking changes require you to:
+
+1. [Get the current `targetIndexes` configuration](#get-the-current-configuration).
+2. [Create an equivalent knowledge source](#create-a-knowledge-source).
+3. [Update the agent to use `knowledgeSources` instead of `targetIndexes`](#update-the-agent).
+4. [Send a query to test the retrieval](#test-the-retrieval).
+5. [Remove code that uses `targetIndexes` and update clients](#update-code-and-clients).
+
+### Get the current configuration
+
+To retrieve your agent's definition, use the 2025-05-01-preview of [Knowledge Agents - Get (REST API)](/rest/api/searchservice/knowledge-agents/get?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
+
+```http
+@search-url = <YourSearchServiceUrl>
+@agent-name = <YourAgentName>
+@api-key = <YourApiKey>
+
+### Get agent definition
+GET https://{{search-url}}/agents/{{agent-name}}?api-version=2025-05-01-preview  HTTP/1.1
+    api-key: {{api-key}}
+```
+
+The response should be similar to the following example. Copy the `indexName`, `defaultRerankerThreshold`, and `defaultIncludeReferenceSourceData` values for use in the upcoming steps. `defaultMaxDocsForReranker` is deprecated, so you can ignore its value.
+
+```json
+{
+  "@odata.etag": "0x1234568AE7E58A1",
+  "name": "my-knowledge-agent",
+  "description": "My description of the agent",
+  "targetIndexes": [
+    {
+      "indexName": "my-index", // Copy this value
+      "defaultRerankerThreshold": 2.5, // Copy this value
+      "defaultIncludeReferenceSourceData": true, // Copy this value
+      "defaultMaxDocsForReranker": 100
+    }
+  ],
+  ... // Redacted for brevity
+}
+```
+
+### Create a knowledge source
+
+To create a `searchIndex` knowledge source, use the 2025-08-01-preview of [Knowledge Sources - Create (REST API)](/rest/api/searchservice/knowledge-sources/create?view=rest-searchservice-2025-08-01-preview&preserve-view=true). Set `searchIndexName` to the value you previously copied.
+
+```http
+@source-name = <YourSourceName>
+
+### Create a knowledge source
+PUT https://{{search-url}}/knowledgeSources/{{source-name}}?api-version=2025-08-01-preview  HTTP/1.1
+    Content-Type: application/json
+    api-key: {{api-key}}
+    
+    {
+        "name": "{{source-name}}",
+        "description": "My description of the knowledge source",
+        "kind": "searchIndex",
+        "searchIndexParameters": {
+            "searchIndexName": "my-index" // Use the previous value
+        }
+    }
+```
+
+This example creates a knowledge source that represents one index, but you can target multiple indexes or an Azure blob. For more information, see [Create a knowledge source](search-knowledge-source-overview.md).
+
+### Update the agent
+
+To replace `targetIndexes` with `knowledgeSources` in your agent's definition, use the 2025-08-01-preview of [Knowledge Agents - Create or Update (REST API)](/rest/api/searchservice/knowledge-agents/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true). Set `rerankerThreshold` and `includeReferenceSourceData` to the values you previously copied.
+
+```http
+### Replace targetIndexes with knowledgeSources
+POST https://{{search-url}}/agents/{{agent-name}}?api-version=2025-08-01-preview  HTTP/1.1
+    Content-Type: application/json
+    api-key: {{api-key}}
+
+    { 
+        "name": "{{agent-name}}", 
+        "knowledgeSources": [  
+            {  
+                "name": "{{source-name}}",
+                "rerankerThreshold": 2.5, // Use the previous value
+                "includeReferenceSourceData": true // Use the previous value
+            }
+        ]
+    } 
+```
+
+This example updates the definition to reference one knowledge source, but you can target multiple knowledge sources. You can also use other properties to control the retrieval behavior, such as `alwaysQuerySource`. For more information, see [Create a knowledge agent](search-agentic-retrieval-how-to-create.md).
+
+### Test the retrieval
+
+To test your agent's output with a query, use the 2025-08-01-preview of [Knowledge Retrieval - Retrieve (REST API)](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true).
+
+```http
+### Send a query to the agent
+POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-08-01-preview  HTTP/1.1
+    Content-Type: application/json
+    api-key: {{api-key}}
+        
+    {
+      "messages": [
+            {
+                "role": "user",
+                "content" : [
+                    {
+                        "text": "<YourQueryText>",
+                        "type": "text"
+                    }
+                ]
+            }
+        ]
+    }
+```
+
+If the response has a `200 OK` HTTP code, your agent successfully retrieved content from the knowledge source.
+
+### Update code and clients
+
+To complete your migration, follow these cleanup steps:
+
++ Replace all `targetIndexes` references with `knowledgeSources` in configuration files, code, scripts, and tests.
++ Update client calls to use the 2025-08-01-preview.
++ Clear or regenerate cached agent definitions that were created using the old shape.
+
+## Version-specific changes
+
+This section covers breaking and nonbreaking changes for the following REST API versions:
+
++ [2025-08-01-preview](#2025-08-01-preview)
++ [2025-05-01-preview](#2025-05-01-preview)
+
+### 2025-08-01-preview
+
+#### [Breaking changes](#tab/breaking)
+
++ Introduces knowledge sources as the new way to define data sources, supporting both `searchIndex` (one or multiple indexes) and `azureBlob` kinds. For more information, see [Create a search index knowledge source](search-knowledge-source-how-to-index.md) and [Create a blob knowledge source](search-knowledge-source-how-to-blob.md).
+
++ Requires `knowledgeSources` instead of `targetIndexes` in agent definitions. For migration steps, see [How to migrate](#how-to-migrate).
+
++ Removes `defaultMaxDocsForReranker` support. This property previously existed in `targetIndexes`, but there's no replacement in `knowledgeSources`.
+
+#### [Nonbreaking changes](#tab/nonbreaking)
+
++ Adds `knowledgeSources`, `outputConfiguration`, and `retrievalInstructions` to agent definitions. For information about supported properties, see [Create a knowledge agent](search-agentic-retrieval-how-to-create.md).
+
++ Renames `defaultRerankerThreshold` to `rerankerThreshold` and `defaultIncludeReferenceSourceData` to `includeReferenceSourceData`. These properties previously existed in `targetIndexes`, but you now specify them within each knowledge source reference in `knowledgeSources`.
+
+---
+
+### 2025-05-01-preview
+
+This REST API version introduces agentic retrieval and knowledge agents. Each agent definition requires a `targetIndexes` array that specifies a single index and optional properties, such as `defaultRerankerThreshold` and `defaultIncludeReferenceSourceData`.
+
+## Related content
+
++ [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
++ [Create a knowledge agent](search-agentic-retrieval-how-to-create.md)
++ [Create a knowledge source](search-knowledge-source-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "エージェンティックリトリーバルコードの移行に関する新しいドキュメント"
}
```

### Explanation
この修正は、`search-agentic-retrieval-how-to-migrate.md`という新たなドキュメントの追加を示しています。このドキュメントは、以前のREST APIバージョンから最新のAPIバージョンへのエージェンティックリトリーバルコードの移行方法を解説しています。

新しいドキュメントは、以下の主要な内容を含んでいます：

1. **移行のタイミング**: どのような状況で移行が必要になるのかを説明しています。例えば、REST APIバージョンの廃止や、ビジネスルールに影響する破壊的変更が導入された場合などです。

2. **移行手順**: 使用しているエージェントの設定を取得し、適切な知識ソースを作成し、エージェントの定義を更新する具体的な手順が詳細に記載されています。これにより、ユーザーは新しい`knowledgeSources`構成を使用するようにエージェントを修正できます。

3. **コード例**: 各手順に対して具体的なコードスニペットを提供し、実際にどのように移行を行うかを示しています。特に、`targetIndexes`の代わりに`knowledgeSources`を使用する方法が強調されています。

4. **バージョン固有の変更**: 2025-08-01-previewおよび2025-05-01-previewの各APIバージョンにおける破壊的変更と非破壊的変更についても詳細に説明されています。これにより、ユーザーは新しい仕様に基づいてコードを更新する際の理解を深められます。

このドキュメントの追加により、エージェンティックリトリーバルを使用しているユーザーは、最新のAPIにスムーズに移行し、機能の利用を続けることが容易になります。

## articles/search/search-agentic-retrieval-how-to-pipeline.md{#item-1ad1c3}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to design and build a custom agentic retrieval solution w
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 06/08/2025
+ms.date: 08/29/2025
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.custom:
@@ -192,7 +192,7 @@ project_client.agents.enable_auto_function_calls(toolset)
 
 ## How to structure messages
 
-The messages sent to the agent tool include instructions for chat history and using the results obtained from [knowledge retrieval](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-05-01-preview&preserve-view=true) on Azure AI Search. The response is passed as a large single string with no serialization or structure.
+The messages sent to the agent tool include instructions for chat history and using the results obtained from [knowledge retrieval](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true) on Azure AI Search. The response is passed as a large single string with no serialization or structure.
 
 ```python
 def agentic_retrieval() -> str:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルパイプラインに関するドキュメントの更新"
}
```

### Explanation
この修正では、`search-agentic-retrieval-how-to-pipeline.md`というエージェンティックリトリーバルパイプラインに関するドキュメントのマイナーアップデートが行われました。主な変更点は、日付の更新と知識リトリーバルのAPIバージョンに関するリンクの修正です。

具体的には、以下の変更が行われました：

1. **日付の更新**: ドキュメントの日付が「2025年6月8日」から「2025年8月29日」に変更され、最新の情報に更新されたことを示しています。

2. **APIバージョンのリンク修正**: 知識リトリーバルのAPIに関するリンクが、2025-05-01-previewから2025-08-01-previewに更新されました。これにより、ユーザーは最新のAPIバージョンに基づいた情報にアクセスできるようになります。

これらの変更は、ドキュメントの正確性と関連性を保つために重要であり、ユーザーが最新の情報を基にエージェンティックリトリーバルソリューションを設計・構築する際に役立ちます。

## articles/search/search-agentic-retrieval-how-to-retrieve.md{#item-5f7fc0}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/08/2025
+ms.date: 08/29/2025
 ---
 
 # Retrieve data using a knowledge agent in Azure AI Search
@@ -16,7 +16,9 @@ ms.date: 06/08/2025
 
 In Azure AI Search, *agentic retrieval* is a new parallel query architecture that uses a large language model (LLM) for query planning. It generates subqueries that broaden the scope of what's searchable and relevant. It incorporates chat history for context. The LLM studies the query and subdivides it into more targeted queries, using different phrases and terminology for subquery composition.
 
-This article explains how to use the [**retrieve method**](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-05-01-preview&preserve-view=true) that invokes a knowledge agent and parallel query processing. This article also explains the three components of the retrieval response: 
+This article explains how to use the [**retrieve method**](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true) that invokes a knowledge agent and parallel query processing. It's updated for the new 2025-08-01-preview, which introduces breaking changes from the 2025-05-01-preview. For help with breaking changes, see [Migrate your agentic retrieval code](search-agentic-retrieval-how-to-migrate.md).
+
+This article also explains the three components of the retrieval response: 
 
 + *extracted response for the LLM*
 + *referenced results*
@@ -25,23 +27,25 @@ This article explains how to use the [**retrieve method**](/rest/api/searchservi
 The retrieve request can include instructions for query processing that override the defaults set on the knowledge agent.
 
 > [!NOTE]
-> There's no model-generated "answer" in the response. Instead, you should pass the response to an LLM that grounds its answer based on the content. For an end-to-end example that includes this step, see [Build an agent-to-agent retrieval solution ](search-agentic-retrieval-how-to-pipeline.md) or [Azure OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo).
+> By default, there's no model-generated "answer" in the response and you should pass the extracted response to an LLM so that it can ground its answer based on the search results. For an end-to-end example that includes this step, see [Build an agent-to-agent retrieval solution ](search-agentic-retrieval-how-to-pipeline.md) or [Azure OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo). Alternatively, you can use [answer synthesis](search-agentic-retrieval-how-to-synthesize.md) to bring answer formulation into the agentic pipeline. In this workflow, the knowledge agent output consists of LLM-formulated answers instead of the raw search results.
 
 ## Prerequisites
 
-+ A [knowledge agent](search-agentic-retrieval-how-to-create.md) that represents the chat completion model and a valid target index.
++ A *knowledge source* that wraps a searchable index. It's either a [search index knowledge source](search-knowledge-source-how-to-index.md) or a [blob knowledge source](search-knowledge-source-how-to-blob.md).
+
++ A [knowledge agent](search-agentic-retrieval-how-to-create.md) that represents the chat completion model and one or more knowledge sources.
 
 + Azure AI Search, in any [region that provides semantic ranker](search-region-support.md), on Basic pricing tier and higher. Your search service must have a [managed identity](search-how-to-managed-identities.md) for role-based access to a chat completion model.
 
 + Permissions on Azure AI Search. **Search Index Data Reader** can run queries on Azure AI Search, but the search service managed identity must have **Cognitive Services User** permissions on the Azure OpenAI resource. For more information about local testing and obtaining access tokens, see [Quickstart: Connect without keys](search-get-started-rbac.md).
 
-+ API requirements. To create or use a knowledge agent, use the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API. Or, use a prerelease package of an Azure SDK that provides knowledge agent APIs: [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta3-2025-03-25), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
++ API requirements. To create or use a knowledge agent, use the [2025-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) data plane REST API. Or, use a prerelease package of an Azure SDK that provides knowledge agent APIs: [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta3-2025-03-25), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
 
 To follow the steps in this guide, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending REST API calls to Azure AI Search. There's no portal support at this time.
 
 ## Call the retrieve action
 
-Call the **retrieve** action on the knowledge agent object to invoke retrieval and return a response. Use the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) data plane REST API or an Azure SDK prerelease package that provides equivalent functionality for this task.
+Call the **retrieve** action on the knowledge agent object to invoke retrieval and return a response. Use the [2025-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) data plane REST API or an Azure SDK prerelease package that provides equivalent functionality for this task.
 
 All `searchable` fields in the search index are in-scope for query execution. If the index includes vector fields, your index should have a valid [vectorizer definition](vector-search-how-to-configure-vectorizer.md) so that it can vectorize the query inputs. Otherwise, vector fields are ignored. The implied query type is `semantic`, and there's no search mode or selection of search fields.
 
@@ -52,7 +56,7 @@ The input for the retrieval route is chat conversation history in natural langua
 @accessToken=<YOUR PERSONAL ID>
 
 # Send grounding request
-POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-05-01-preview
+POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-08-01-preview
     Content-Type: application/json
     Authorization: Bearer {{accessToken}}
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルによるデータ取得に関するドキュメントの更新"
}
```

### Explanation
この修正では、`search-agentic-retrieval-how-to-retrieve.md`というエージェンティックリトリーバルを用いたデータ取得に関するドキュメントの内容が更新されました。主に以下の変更が行われています：

1. **日付の更新**: ドキュメントの日付が「2025年6月8日」から「2025年8月29日」に改定されました。この更新により、最新の情報が反映されています。

2. **APIバージョンリンクの修正**: `retrieve`メソッドに関するリンクが、旧バージョンの「2025-05-01-preview」から新バージョンの「2025-08-01-preview」に変更されました。これは、新しいAPIバージョンでの破壊的変更に関連しています。

3. **内容の追加**: 記事に新たな情報が追加され、取得応答の三つのコンポーネント（抽出応答、参照結果）に関する言及や、モデル生成された「回答」がデフォルトでは含まれないことを明確にしています。また、エンドツーエンドの例として「エージェント間リトリーバルソリューションの構築」や「Azure OpenAIデモ」に言及し、知識エージェントの出力をLLMに渡して応答を生成することも提案されています。

4. **条件の修正**: 取得の前提条件が明確化され、知識ソースが重要な要素として示されています。また、API要件が新しいバージョンにアップデートされています。

これらの変更は、ユーザーがエージェンティックリトリーバルを効果的に利用するための情報を可能な限り最新の状態に保ち、正確かつ関連性のあるガイダンスを提供することを目的としています。

## articles/search/search-agentic-retrieval-how-to-synthesize.md{#item-18668b}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,150 @@
+---
+title: Configure Answer Synthesis
+titleSuffix: Azure AI Search
+description: Learn how to configure a knowledge agent to use answer synthesis in Azure AI Search. At query time, the agent uses your deployed chat completion model to produce natural-language answers with citations to your knowledge sources.
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: how-to
+ms.date: 08/26/2025
+---
+
+# Use answer synthesis for citation-backed responses in Azure AI Search
+
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+By default, a [knowledge agent](search-agentic-retrieval-how-to-create.md) in Azure AI Search performs *data extraction*, which returns raw grounding chunks from your knowledge sources. Data extraction is useful for retrieving specific information, but it lacks the context and reasoning necessary for complex queries.
+
+You can configure the agent to perform *answer synthesis*, which uses your deployed chat completion model to respond to queries in natural language. Each answer includes citations to the retrieved sources and follows any instructions you provide, such as using bulleted lists.
+
+This article explains how to configure and test answer synthesis for an existing agent. Although you can use this configuration for new agents, agent creation is beyond the scope of this article.
+
+> [!IMPORTANT]
+> Answer synthesis incurs pay-as-you-go charges from Azure OpenAI, which is based on the number of input and output tokens. Charges appear under the chat completion model assigned to the agent. For more information, see [Availability and pricing of agentic retrieval](search-agentic-retrieval-concept.md#availability-and-pricing).
+
+## Prerequisites
+
++ A knowledge agent that uses the 2025-08-01-preview syntax, which requires `knowledgeSources` instead of `targetIndexes`.
+
++ [Visual Studio Code](https://code.visualstudio.com/) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) or a prerelease package of an Azure SDK that provides the knowledge agent REST APIs. Currently, there's no portal support.
+
+## Configure answer synthesis
+
+To configure your knowledge agent for answer synthesis, use the 2025-08-01-preview of [Knowledge Agent - Create or Update (REST API)](/rest/api/searchservice/knowledge-agents/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true).
+
+In the `outputConfiguration` section:
+
+1. Set `modality` to `answerSynthesis`.
+
+1. (Optional) Use `answerInstructions` to customize the answer output. Our example instructs the agent to `Use concise bulleted lists`.
+
+```http
+@search-url = <YourSearchServiceUrl>
+@agent-name = <YourAgentName>
+@api-key = <YourApiKey>
+
+### Configure answer synthesis
+PUT https://{{search-url}}/knowledgeAgents/{{agent-name}}?api-version=2025-08-01-preview  HTTP/1.1
+    Content-Type: application/json
+    api-key: {{api-key}}
+
+    {
+        "name": "{{agent-name}}",
+        "models": [
+            ... // Redacted for brevity
+        ],
+        "knowledgeSources": [
+            ... // Redacted for brevity
+        ],
+        "outputConfiguration": {
+            "modality": "answerSynthesis",
+            "answerInstructions": "Use concise bulleted lists"
+        }
+    }
+```
+
+> [!IMPORTANT]
+> This example assumes that you're using key-based authentication for local proof-of-concept testing. We recommend role-based access control for production workloads. For more information, see [Connect to Azure AI Search using roles](search-security-rbac.md).
+
+<!--
+1. (Optional) Set the `includeReferences` property to `true` or `false`.
+
+    ```http
+          "knowledgeSources" : [
+              {
+                  "name" : "<YourKnowledgeSource>", 
+                  "includeReferences" : true,
+                  "includeReferenceSourceData" : true
+              }
+          ]
+    ```
+
+1. (Optional) Set the `includeActivity` property to `true` to include an activity log in answers.
+
+    ```http
+        	"outputConfiguration": {
+        		"modality": "answerSynthesis",
+        		"answerInstructions": "Use concise bulleted lists",
+        		"includeActivity": true
+        	}
+    ```
+-->
+
+## Get a synthesized answer
+
+After your knowledge agent is configured for answer synthesis, use the 2025-08-01-preview of [Knowledge Retrieval - Retrieve (REST API)](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true) to test its output.
+
+```http
+### Send a query to the agent
+POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-08-01-preview  HTTP/1.1
+    Content-Type: application/json
+    api-key: {{api-key}}
+        
+    {
+      "messages": [
+            {
+                "role": "user",
+                "content" : [
+                    {
+                        "text": "<YourQueryText>",
+                        "type": "text"
+                    }
+                ]
+            }
+        ]
+    }
+```
+
+The response should include a natural-language answer based on your instructions, with citations to your knowledge sources formatted as `[ref_id:<number>]`. For example, if your instructions are `Use concise bulleted lists` and your query is `What is healthcare?`, the response might look like this:
+
+```json
+{
+  "response": [
+    {
+      "content": [
+        {
+          "type": "text",
+          "text": "- Healthcare encompasses various services provided to patients and the general population ... // Trimmed for brevity
+        }
+      ]
+    }
+  ],
+  ... // Redacted for brevity
+}
+```
+
+The full `text` output is as follows:
+
+```
+"- Healthcare encompasses various services provided to patients and the general population, including primary health services, hospital care, dental care, mental health services, and alternative health services [ref_id:1].\n- It involves the delivery of safe, effective, patient-centered care through different modalities, such as in-person encounters, shared medical appointments, and group education sessions [ref_id:0].\n- Behavioral health is a significant aspect of healthcare, focusing on the connection between behavior and overall health, including mental health and substance use [ref_id:2].\n- The healthcare system aims to ensure quality of care, access to providers, and accountability for positive outcomes while managing costs effectively [ref_id:2].\n- The global health system is evolving to address complex health needs, emphasizing the importance of cross-sectoral collaboration and addressing social determinants of health [ref_id:4]."
+```
+
+Depending on your agent's configuration, the response might include other information, such as activity logs and reference arrays. For more information, see [Create a knowledge agent](search-agentic-retrieval-how-to-create.md).
+
+## Related content
+
++ [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
++ [Create a knowledge agent](search-agentic-retrieval-how-to-create.md)
++ [Create a search index knowledge source](search-knowledge-source-how-to-index.md)
++ [Create a blob knowledge source](search-knowledge-source-how-to-blob.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Searchにおける回答合成の構成に関する新しいドキュメント"
}
```

### Explanation
この修正は、`search-agentic-retrieval-how-to-synthesize.md`という新しいドキュメントの追加を示しています。このドキュメントでは、Azure AI Searchにおける知識エージェントを使用した回答合成の構成方法について詳細に説明しています。新機能である回答合成は、自然言語での回答を生成し、引用を知識ソースに基づいて行います。

主な内容は以下の通りです：

1. **概要と目的**: このドキュメントは、Azure AI Searchにおいてデプロイされたチャット補完モデルを使用して、質問に対して自然言語の回答を生成するための知識エージェントの設定方法を解説しています。回答は提出された指示に従っており、リスト形式での出力が可能です。

2. **重要な注意点**: 回答合成はAzure OpenAI使用時に按分課金が発生することが明示されています。この情報はユーザーがコストを理解し、計画するのに役立ちます。

3. **前提条件**: 回答合成を構成するためには、特定のバージョンの知識エージェントと、Visual Studio CodeのREST Client拡張が推奨されています。

4. **構成手順**: 知識エージェントの回答合成を構成するための具体的な手順が提供されており、`outputConfiguration`セクションでの設定項目が説明されています。ここには、`modality`の設定や、出力をカスタマイズするためのオプションが含まれます。

5. **例とテスト**: 構成後には、知識エージェントを使用して合成された回答を取得するための具体的なAPIリクエストの例が示されており、ユーザーはその応答から得られる情報のフォーマットも確認できます。

このドキュメントは、ユーザーがAzure AI Searchを通じてよりインタラクティブで効率的な情報 Retrieval を行うための重要な資源となります。

## articles/search/search-api-migration.md{#item-07297b}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: conceptual
-ms.date: 07/31/2025
+ms.date: 08/27/2025
 ---
 
 # Upgrade to the latest REST API in Azure AI Search
@@ -23,7 +23,7 @@ Here are the most recent versions of the REST APIs:
 | Targeted operations | REST API | Status |
 |---------------------|----------|--------|
 | Data plane | [`2024-07-01`](/rest/api/searchservice/search-service-api-versions#2024-07-01) | Stable |
-| Data plane | [`2025-05-01-preview`](/rest/api/searchservice/search-service-api-versions#2025-05-01-preview&preserve-view=true) | Preview |
+| Data plane | [`2025-08-01-preview`](/rest/api/searchservice/search-service-api-versions#2025-08-01-preview&preserve-view=true) | Preview |
 | Control plane | [`2025-05-01`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2025-05-01&preserve-view=true) | Stable |
 | Control plane | [`2025-02-01-preview`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true) | Preview |
 
@@ -40,7 +40,7 @@ We recommend upgrading API versions in succession, working through each version
 
 Azure AI Search breaks backward compatibility as a last resort. Upgrade is necessary when:
 
-+ Your code references a retired or unsupported API version and is subject to one or more breaking changes. You must address breaking changes if your code targets [`2023-07-10-preview`](#code-upgrade-for-vector-indexes-and-queries) for vectors, [`2020-06-01-preview`](#breaking-changes-for-semantic-ranker) for semantic ranker, and [`2019-05-06`](#upgrade-to-2019-05-06) for obsolete skills and workarounds.
++ Your code references a retired or unsupported API version and is subject to one or more breaking changes. You must address breaking changes if your code targets [`2025-05-01-preview`](#breaking-changes-for-knowledge-agents) for knowledge agents, [`2023-07-10-preview`](#code-upgrade-for-vector-indexes-and-queries) for vectors, [`2020-06-01-preview`](#breaking-changes-for-semantic-ranker) for semantic ranker, and [`2019-05-06`](#upgrade-to-2019-05-06) for obsolete skills and workarounds.
 
 + Your code fails when unrecognized properties are returned in an API response. As a best practice, your application should ignore properties that it doesn't understand.
 
@@ -62,6 +62,10 @@ Azure AI Search breaks backward compatibility as a last resort. Upgrade is neces
 
 The following breaking changes apply to data operations.
 
+### Breaking changes for knowledge agents
+
+[Knowledge agents](search-agentic-retrieval-how-to-create.md) were introduced in `2025-05-01-preview`. Breaking changes apply to agents that use `targetIndexes` and `defaultMaxDocsForReranker`, which are deprecated starting in `2025-08-01-preview`. For help with breaking changes, see [Migrate your agentic retrieval code](search-agentic-retrieval-how-to-migrate.md).
+
 ### Breaking changes for client code that reads connection information
 
 Effective March 29, 2024 and applicable to all [supported REST APIs](/rest/api/searchservice/search-service-api-versions):
@@ -86,6 +90,15 @@ See [Migrate from preview version](semantic-code-migration.md) to transition you
 
 Upgrade guidance assumes upgrade from the most recent previous version. If your code is based on an old API version, we recommend upgrading through each successive version to get to the newest version.
 
+### Upgrade to 2025-08-01-preview
+
+[`2025-08-01-preview`](/rest/api/searchservice/search-service-api-versions#2025-08-01-preview) introduces the following breaking changes to knowledge agents created using `2025-05-01-preview`:
+
++ Replaces `targetIndexes` with `knowledgeSources`.
++ Removes `defaultMaxDocsForReranker` without replacement.
+
+Otherwise, there are no behavior changes on existing APIs. You can swap in the new API version and your code runs the same as before.
+
 ### Upgrade to 2025-05-01-preview
 
 [`2025-05-01-preview`](/rest/api/searchservice/search-service-api-versions#2025-05-01-preview) provides new features, but there are no behavior changes on existing APIs. You can swap in the new API version and your code runs the same as before.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI SearchのAPI移行ガイドの更新"
}
```

### Explanation
この修正は、`search-api-migration.md`というAPI移行ガイドの内容を更新したもので、主に以下の変更が含まれています：

1. **日付の更新**: ドキュメントの日付が「2025年7月31日」から「2025年8月27日」に改定され、最新情報が反映されています。

2. **APIバージョンのアップデート**: REST APIのバージョン表において、`2025-05-01-preview`の項目が`2025-08-01-preview`に更新されました。これにより最新のプレビューAPIが表示されます。

3. **破壊的変更の明確化**: 知識エージェントに関する新しい破壊的変更が追加され、`2025-08-01-preview`以降、`targetIndexes`が`knowledgeSources`に置き換えられ、`defaultMaxDocsForReranker`が削除されたことが記載されています。これにより、ユーザーは必ず新しいプロパティに更新する必要があります。

4. **条件の追加**: APIの応答に認識されないプロパティが含まれる場合の対処法について説明が追加され、アプリケーションは理解していないプロパティを無視するべきであるとされています。

これらの変更を通じて、APIの利用者に対して、最新の機能や、従来のAPIの利用から新しいAPIへの移行における変化について、より明確なガイダンスを提供することを目的としています。

## articles/search/search-api-preview.md{#item-511f5d}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: conceptual
-ms.date: 08/18/2025
+ms.date: 08/27/2025
 ---
 
 # Preview features in Azure AI Search
@@ -25,14 +25,18 @@ Preview features are removed from this list if they're retired or transition to
 
 |Feature&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Category | Description | Availability  |
 |---------|------------------|-------------|---------------|
-| [**Agentic retrieval**](search-agentic-retrieval-concept.md) | Query | Create a conversational search experience powered by large language models (LLMs) and your proprietary data. Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries in parallel, and extracts grounding data from documents indexed in Azure AI Search. The output is intended for agents and custom chat solutions. A new [knowledge agent](search-agentic-retrieval-how-to-create.md) object is introduced in this preview. Its [response payload](search-agentic-retrieval-how-to-retrieve.md) is designed for downstream agent and chat model consumption, with full transparency of the query plan and reference data. To get started, see [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md). | [Knowledge Agents (preview)](/rest/api/searchservice/knowledge-agents?view=rest-searchservice-2025-05-01-preview&preserve-view=true) and [Knowledge Retrieval (preview)](/rest/api/searchservice/knowledge-retrieval?view=rest-searchservice-2025-05-01-preview&preserve-view=true)|
-| [**Multivector support**](vector-search-multi-vector-fields.md) | Indexing | Index multiple child vectors within a single document field. You can now use vector types in nested fields of complex collections, effectively allowing multiple vectors to be associated with a single document.| [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true). |
-| [**Scoring profiles with semantic ranking**](semantic-how-to-enable-scoring-profiles.md) | Relevance | Semantic ranker adds a new field, `@search.rerankerBoostedScore`, to help you maintain consistent relevance and greater control over final ranking outcomes in your search pipeline. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true). |
+| [**"Fast path" for knowledge agents**](search-agentic-retrieval-how-to-create.md) | Agentic search | New `attemptFastPath` boolean for knowledge agents. Enables a shorter processing time if queries are concise and the initial response is sufficiently relevant. | [Knowledge Agents - Create Or Update (preview)](/rest/api/searchservice/knowledge-agents/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) |
+| [**Retrieval instructions**](search-agentic-retrieval-how-to-create.md) | Agentic search | New `retrievalInstructions` property for knowledge agents guides query planning in an agentic retrieval workflow. For example, you can specify criteria for including or excluding specific knowledge sources. | [Knowledge Agents - Create Or Update (preview)](/rest/api/searchservice/knowledge-agents/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) |
+| [**Improved indexer runtime tracking information**](search-howto-run-reset-indexers.md) | Indexers | New cumulative indexer processing information for the search service and for specific indexers. | [Get Service Statistics (preview)](/rest/api/searchservice/get-service-statistics/get-service-statistics?view=rest-searchservice-2025-08-01-preview&preserve-view=true) and [Get Status - Indexers (preview)](/rest/api/searchservice/get-service-statistics/get-status?view=rest-searchservice-2025-08-01-preview&preserve-view=true) |
+| [**Strict postfiltering for vector queries**](vector-search-filters.md) | Vectors | New `strictPostFilter` mode for the `vectorFilterMode` parameter. When specified, filters are applied after the global top-`k` vector results are identified, ensuring that returned documents are a subset of the unfiltered results. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-08-01-preview&preserve-view=true). |
+| [**Agentic retrieval**](search-agentic-retrieval-concept.md) | Query | Create a conversational search experience powered by large language models (LLMs) and your proprietary content. Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries simultaneously, and either extracts grounding data or synthesizes an answer based on documents indexed in Azure AI Search. To get started, see [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md).<p>The pipeline involves one or more [knowledge sources](search-knowledge-source-overview.md) and an associated [knowledge agent](search-agentic-retrieval-how-to-create.md), whose [response payload](search-agentic-retrieval-how-to-retrieve.md) provides full transparency into the query plan and reference data. Knowledge sources currently support [search indexes](search-knowledge-source-how-to-index.md) and [Azure blobs](search-knowledge-source-how-to-blob.md). | [Knowledge Sources (preview)](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-08-01-preview&preserve-view=true), [Knowledge Agents (preview)](/rest/api/searchservice/knowledge-agents?view=rest-searchservice-2025-08-01-preview&preserve-view=true), and [Knowledge Retrieval (preview)](/rest/api/searchservice/knowledge-retrieval?view=rest-searchservice-2025-08-01-preview&preserve-view=true). |
+| [**Multivector support**](vector-search-multi-vector-fields.md) | Indexing | Index multiple child vectors within a single document field. You can now use vector types in nested fields of complex collections, effectively allowing multiple vectors to be associated with a single document.| [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true). |
+| [**Scoring profiles with semantic ranking**](semantic-how-to-enable-scoring-profiles.md) | Relevance | Semantic ranker adds a new field, `@search.rerankerBoostedScore`, to help you maintain consistent relevance and greater control over final ranking outcomes in your search pipeline. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true). |
 | [**Logic Apps integration in the portal wizard**](search-how-to-index-logic-apps-indexers.md) | Indexing | Create an automated indexing pipeline that retrieves content using a logic app workflow. Use the [Import and vectorize data wizard](search-get-started-portal-import-vectors.md) in the Azure portal to build an indexing pipeline based on Logic Apps. | Image and vectorize data wizard in the Azure portal. |
-| [**Document-level access control**](search-document-level-access-overview.md) | Security | Flow document-level permissions from blobs in Azure Data Lake Storage (ADLS) Gen2 to searchable documents in an index. Queries can now filter results based on user identity for selected data sources. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true). |
-| [**GenAI Prompt skill**](cognitive-search-skill-genai-prompt.md) | Skills | A new skill that connects to a large language model (LLM) for information, using a prompt you provide. With this skill, you can populate a searchable field using content from an LLM. A primary use case for this skill is *image verbalization*, using an LLM to describe images and send the description to a searchable field in your index. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true). |
-| [**Document Layout skill**](cognitive-search-skill-document-intelligence-layout.md)| Skills | New parameters are available for this skill if you use the 2025-05-01-preview API version or later. The new parameters support image offset metadata that improves the image search experience. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true). |
-| [**Index "description" support**](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true#request-body) | REST | The 2025-05-01-preview API version adds a description to an index. A description is useful in agentic solutions, where the agent reads the description to decide whether to run a query or move on to another index. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true). |
+| [**Document-level access control**](search-document-level-access-overview.md) | Security | Flow document-level permissions from blobs in Azure Data Lake Storage (ADLS) Gen2 to searchable documents in an index. Queries can now filter results based on user identity for selected data sources. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true). |
+| [**GenAI Prompt skill**](cognitive-search-skill-genai-prompt.md) | Skills | A new skill that connects to a large language model (LLM) for information, using a prompt you provide. With this skill, you can populate a searchable field using content from an LLM. A primary use case for this skill is *image verbalization*, using an LLM to describe images and send the description to a searchable field in your index. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true). |
+| [**Document Layout skill**](cognitive-search-skill-document-intelligence-layout.md)| Skills | New parameters are available for this skill if you use the 2025-05-01-preview API version or later. The new parameters support image offset metadata that improves the image search experience. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true). |
+| [**Index "description" support**](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true#request-body) | REST | You can now write descriptions for indexes. A description is useful in agentic solutions, where the agent reads the description to decide whether to run a query or move on to another index. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true). |
 | [**flightingOptIn parameter in a semantic configuration**](semantic-how-to-configure.md#opt-in-for-prerelease-semantic-ranking-models) | Queries| You can opt in to use prerelease semantic ranking models if one is available in a search service region. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true). |
 | [**Rescore vector queries over binary embeddings using full precision vectors**](vector-search-how-to-quantization.md#recommended-rescoring-techniques) | Relevance (scoring) | For vector indexes that contain quantized binary embeddings, you can rescore query results using a full precision query vector. The query engine uses the dot product for rescoring, which improves the quality of search results. Set `enableRescoring` and `discardOriginals` to use this feature.| [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true). |
 | [**Facet hierarchies, aggregations, and facet filters**](search-faceted-navigation-examples.md) | Queries| New facet query parameters support nested facets. For numeric facetable fields, you can sum the values of each field. You can also specify filters on a facet to add inclusion or exclusion criteria. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-03-01-preview&preserve-view=true). |
@@ -92,7 +96,7 @@ If you write code against a preview API, you should prepare to upgrade that code
 
 Preview REST APIs are accessed through the api-version parameter on the URI. Older previews are still operational but become stale over time and aren't updated with new features or bug fixes.
 
-For data plane operation on content, [**`2024-05-01-preview`**](/rest/api/searchservice/search-service-api-versions#2024-05-01-Preview) is the most recent preview version. The following example shows the syntax for [Indexes GET (preview)](/rest/api/searchservice/indexes/get?view=rest-searchservice-2024-05-01-preview&preserve-view=true):
+For data plane operations on content, [**`2025-08-01-preview`**](/rest/api/searchservice/search-service-api-versions#2025-08-01-Preview) is the most recent preview version. The following example shows the syntax for [Indexes GET (preview)](/rest/api/searchservice/indexes/get?view=rest-searchservice-2025-08-01-preview&preserve-view=true):
 
 ```rest
 GET {endpoint}/indexes('{indexName}')?api-version=2024-05-01-Preview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのプレビュー機能に関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-api-preview.md`というドキュメントの内容を更新したもので、主に以下の変更が含まれています：

1. **日付の更新**: ドキュメントの日付が「2025年8月18日」から「2025年8月27日」に更新され、最新情報が反映されています。

2. **新機能の追加**: 新しいプレビュー機能がいくつか追加されており、以下のポイントが示されています：
   - 知識エージェントに対して新たに`attemptFastPath`ブール値が導入され、短時間での処理を可能にする機能。
   - 知識エージェントのクエリ計画を導くための新しい`retrievalInstructions`プロパティの追加。
   - インデクサーの累積処理情報の改善に関する機能の導入。
   - `strictPostFilter`モードが追加され、グローバルなトップ`k`ベクトル結果が識別された後にフィルターが適用されるようになりました。

3. **内容の再配置と削除**: 一部の過去の機能の説明が削除され、新しい機能の説明が追加されることで、ドキュメントの内容が更新されました。

4. **APIバージョンの更新**: プレビューAPIの最新バージョンが`2025-08-01-preview`に更新され、それに関連する情報が記載されています。

これらの変更を通じて、ユーザーはAzure AI Searchの最新のプレビュー機能を理解し、効果的に利用できるようになります。ノートには新機能や変更点が明確に示されており、開発者やユーザーにとっての重要なリソースとなっています。

## articles/search/search-blob-indexer-role-based-access.md{#item-887e42}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how to configure Azure AI Search indexers for ingesting Azure Role-Based Access (RBAC) metadata on Azure blobs.
 ms.service: azure-ai-search  
 ms.topic: how-to
-ms.date: 07/16/2025
+ms.date: 09/01/2025
 author: vaishalishah
 ms.author: vaishalishah
 ---  
@@ -13,25 +13,33 @@ ms.author: vaishalishah
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Azure Storage allows for role-based access on containers in blob storage, where roles like **Storage Blob Data Reader** or **Storage Blob Data Contributor** determine whether someone has access to content. Starting in 2025-05-01-preview, you can now include RBAC scope alongside document ingestion in Azure AI Search and use those permissions to control access to search results. If you have rights to the content, you can see those results in a search query. If you don't have rights (or more specifically, a role assignment on the blob container), you *can't* see those results even if you personally have a **Search Index Data Reader** assignment on the index.
+Azure Storage allows for role-based access on containers in blob storage, where roles like **Storage Blob Data Reader** or **Storage Blob Data Contributor** determine whether someone has access to content. Starting in 2025-05-01-preview, you can now include RBAC scope alongside document ingestion in Azure AI Search and use those permissions to control access to search results. If you have rights to the content, you can see that content in search results. If you don't have rights (or more specifically, a role assignment on the blob container), you *can't* see those results even if you personally have a **Search Index Data Reader** assignment *on the index*.
 
-RBAC scope is set at the container level and flows to all blobs (documents) through permission inheritance. RBAC scope is captured during indexing as permission metadata, You can use the push APIs to upload and index content and permission metadata manually see [Indexing Permissions using the push REST API](search-index-access-control-lists-and-rbac-push-api.md), or you can use an indexer to automate data ingestion. This article focuses on the indexer approach.
+RBAC scope is set at the container level and flows to all blobs (documents) through permission inheritance. RBAC scope is captured during indexing as permission metadata. You can use the push APIs to upload and index content and permission metadata manually (see [Indexing Permissions using the push REST API](search-index-access-control-lists-and-rbac-push-api.md)), or you can use an indexer to automate data ingestion. This article focuses on the indexer approach.
 
 At query time, the identity of the caller is included in the request header via the `x-ms-query-source-authorization` parameter. The identity must match the permission metadata on documents if the user is to see the search results.
 
 The indexer approach is built on this foundation:
 
-+ [Role-based access control (Azure RBAC)](/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac). There's no support for Attribute-based access control (Azure ABAC).
++ [Azure Storage blobs secured using role-based access control (Azure RBAC)](/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac). There's no support for Attribute-based access control (Azure ABAC).
 
-+ [An Azure AI Search indexer for blobs](search-howto-indexing-azure-blob-storage.md) that retrieves and ingests data and metadata, including permission filters. To get permission filter support, you must use the 2025-05-01-preview REST API or a preview package of an Azure SDK that supports the feature.
++ [An Azure AI Search indexer for blobs](search-howto-indexing-azure-blob-storage.md) that retrieves and ingests data and metadata, including permission filters. To get permission filter support, use the latest preview REST API or a preview package of an Azure SDK that supports the feature.
 
-+ [An index in Azure AI Search](search-how-to-create-search-index.md) containing the ingested documents and corresponding permissions. Permission metadata is stored as fields in the index. To set up queries that respect the permission filters, you must use the 2025-05-01-preview REST API or a preview package of an Azure SDK that supports the feature. 
++ [An index in Azure AI Search](search-how-to-create-search-index.md) containing the ingested documents and corresponding permissions. Permission metadata is stored as fields in the index. 
+
++ [A query that uses permission filters](search-query-access-control-rbac-enforcement.md). To set up queries that respect the permission filters, use the latest preview REST API or a preview package of an Azure SDK that supports the feature.
 
 ## Prerequisites
 
 + [Microsoft Entra ID authentication and authorization](/entra/identity/authentication/overview-authentication). Services and apps must be in the same tenant. Users can be in different tenants as long as all of the tenants are Microsoft Entra ID. Role assignments are used for each authenticated connection.
 
-+ Azure AI Search, any region, but you must have a billable tier (basic and higher) see [Service limits](search-limits-quotas-capacity.md) for managed identity support. The search service must be [configured for role-based access](search-security-enable-roles.md) and it must [have a managed identity (either system or user)](search-how-to-managed-identities.md).
++ Azure AI Search, any region, but you must have a billable tier (basic and higher) for managed identity support. The search service must be [configured for role-based access](search-security-enable-roles.md) and it must [have a managed identity (either system or user)](search-how-to-managed-identities.md).
+
++ Azure Storage, Standard performance (general-purpose v2), on hot, cool, and cold access tiers, with RBAC-secured containers or blobs.
+
++ You should understand how indexers work and how to create an index. This article explains the configuration settings for the data source and indexer, but doesn't provide steps for creating the index. For more information about indexes designed for permission filters, see [Create an index with permission filter fields](search-index-access-control-lists-and-rbac-push-api.md#create-an-index-with-permission-filter-fields).
+
+Permission filters aren't supported in the indexers and indexes created through the [Import wizards](search-import-data-portal.md). Use a programmatic approach to create or modify existing objects for document-level access.
 
 ## Configure Blob storage
 
@@ -75,7 +83,7 @@ In Azure AI Search, configure an indexer, data source, and index to pull permiss
   + For connection strings using a [user-assigned managed identity](search-howto-managed-identities-storage.md#user-assigned-managed-identity-preview), you must also specify the `identity` property.
 
 <!-- Question/Comment: check this example -->
-JSON example with system managed identity:
+JSON example with system managed identity and `indexerPermissionOptions`:
 
 ```json
 {
@@ -164,9 +172,19 @@ JSON schema example:
 }
 ```
 
+### Run the indexer
+
+Once your indexer, data source, and index are configured, run the indexer to set the process in motion. If there's a problem with configuration or permissions, those problems will surface in this step.
+
+By default, an indexer runs as soon as you post it to a search service, but if the indexer configuration includes `disabled` set to true, the indexer is posted in a disabled state so that you can run the indexer manually.
+
+We recommend [running the indexer from the Azure portal](search-howto-run-reset-indexers.md#how-to-reset-and-run-indexers) so that you can monitor status and messages.
+
+Assuming no errors, the index is now populated and you can move forward with [queries and testing](search-query-access-control-rbac-enforcement.md).
+
 ## Deletion tracking 
 
-To effectively manage blob deletion, ensure that you have enabled [deletion tracking](search-howto-index-changed-deleted-blobs.md) before your indexer runs for the first time. This feature allows the system to detect deleted blobs from your source and have them deleted from the index.  
+To effectively manage blob deletion, ensure that you have enabled [deletion tracking](search-howto-index-changed-deleted-blobs.md) before your indexer runs for the first time. This feature allows the system to detect deleted blobs from your source and delete the corresponding content from the index.  
 
 ## See also
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Blob IndexerのRBACに関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-blob-indexer-role-based-access.md`というドキュメントの内容を更新したもので、以下のような変更が行われています：

1. **日付の更新**: ドキュメントの日付が「2025年7月16日」から「2025年9月1日」に更新され、最新の情報が反映されました。

2. **RBACの説明の明確化**: RBAC（Role-Based Access Control）の説明が改訂され、コンテンツにアクセスできる条件がより明確に記述されています。特に、役割の割り当てが重要であることが強調されています。

3. **インデクサーの設定に関する追記**: インデクサーの動作や設定手順、特にRBACに関するメタデータの捕捉プロセスに関する情報が追加され、ユーザーが設定を行う際の理解が深まるように配慮されています。

4. **新しいセクションの追加**: インデクサーを実行する手順のセクションが新たに追加され、インデクサーが実行されたときに表示されるエラーメッセージについても触れられています。これにより、ユーザーはインデクサーの状態をモニタリングしやすくなっています。

5. **削除追跡に関する注意書きの強調**: Blobの削除管理に関して、削除追跡を有効にする重要性が再度強調されており、ユーザーが適切にインデクサーを運用するためのインサイトが提供されています。

これらの変更を通じて、ユーザーはAzure Blob IndexerのRBAC設定に関する理解を深め、効果的に機能を活用できるようになることが期待されています。ドキュメントは、役立つリソースとしての役割を強化しています。

## articles/search/search-document-level-access-overview.md{#item-4bb055}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Conceptual overview of document-level permissions in Azure AI Search.
 author: gmndrg
 ms.author: gimondra
-ms.date: 07/16/2025
+ms.date: 08/27/2025
 ms.service: azure-ai-search
 ms.topic: conceptual
 ms.custom:
@@ -20,7 +20,7 @@ Azure AI Search supports document-level access control, enabling organizations t
 | Approach | Description |
 |----------|-------------|
 | Security filters | String comparison. Your application passes in a user or group identity as a string, which populates a filter on a query, excluding any documents that don't match on the string. <br><br>Security filters are a technique for achieving document-level access control. This approach isn't bound to an API so you can use any version or package. |
-| ACLs / RBAC scopes (preview) | Microsoft Entra ID security principal behind the query token is compared to the permission metadata of documents returned in search results, excluding any documents that don't match on permissions. Access Control Lists (ACL) permissions apply to Azure Data Lake Storage (ADLS) Gen2 directories and files. Role-based access control (RBAC) scopes apply to ADLS Gen2 content and to Azure blobs. <br><br>Built-in support for identity-based access at the document level is in preview, available in REST APIs and prerelease Azure SDK packages that provide the feature. Be sure to check the [SDK package change log](#retrieve-permissions-metadata-during-data-ingestion-process) for evidence of feature support.|
+| ACLs / RBAC scopes (preview) | Microsoft Entra ID security principal behind the query token is compared to the permission metadata of documents returned in search results, excluding any documents that don't match on permissions. Access Control Lists (ACL) permissions apply to Azure Data Lake Storage (ADLS) Gen2 directories and files. Role-based access control (RBAC) scopes apply to ADLS Gen2 content and to Azure blobs. <br><br>Built-in support for identity-based access at the document level is in preview, available in REST APIs and preview Azure SDK packages that provide the feature. Be sure to check the [SDK package change log](#retrieve-permissions-metadata-during-data-ingestion-process) for evidence of feature support.|
 
 ## Pattern for security trimming using filters  
 
@@ -46,10 +46,10 @@ Azure Data Lake Storage (ADLS) Gen2 containers support ACLs on the container and
 For ACL-secured content, we recommend group access IDs over user access IDs for ease of management. The pattern includes the following components:
 
 - Start with documents or files that have ACL assignments.
-- [Enable permission filters](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true#searchindexpermissionfilteroption) in the index.
-- [Add a permission filter](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true#permissionfilter) to a string field in an index.
+- [Enable permission filters](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true#searchindexpermissionfilteroption) in the index.
+- [Add a permission filter](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true#permissionfilter) to a string field in an index.
 - Load the index with source documents having associated ACLs.
-- Query the index, [adding `x-ms-query-source-authorization`](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&preserve-view=true#request-headers) in the request header.
+- Query the index, [adding `x-ms-query-source-authorization`](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-08-01-preview&preserve-view=true#request-headers) in the request header.
 
 Your client app has read permissions to the index via **Search Index Data Reader**, but user or group permission metadata on indexed content determines access at query time. Queries that include a permission filter pass a user or group token as `x-ms-query-source-authorization` in the request header. When you use permission filters at query time, Azure AI Search checks for 2 things:
 
@@ -67,7 +67,7 @@ How you retrieve permissions varies depending on whether you're pushing a docume
 
 Start with a preview API that provides the feature:
 
-- [2025-05-01 preview REST API](/rest/api/searchservice/documents/?view=rest-searchservice-2025-05-01-preview&preserve-view=true)
+- [2025-08-01 preview REST API](/rest/api/searchservice/documents/?view=rest-searchservice-2025-08-01-preview&preserve-view=true)
 - [Azure SDK for Python prerelease package](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md#1160b12-2025-05-14)
 - [Azure SDK for .NET prerelease package](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md#1170-beta4-2025-05-14)
 - [Azure SDK for Java prerelease package](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md#1180-beta7-2025-05-16)
@@ -76,12 +76,12 @@ For the [push model approach](search-index-access-control-lists-and-rbac-push-ap
 
 1. Ensure your index schema is also created with a preview or prerelease SDK and that the schema has permission filters.
 1. Consider using the Microsoft Graph SDK to get group or user IDs.
-1. Use the [Index Documents](/rest/api/searchservice/documents/?view=rest-searchservice-2025-05-01-preview&preserve-view=true#indexdocumentsresult) or equivalent Azure SDK API to push documents and their associated permission metadata into the search index. 
+1. Use the [Index Documents](/rest/api/searchservice/documents/?view=rest-searchservice-2025-08-01-preview&preserve-view=true#indexdocumentsresult) or equivalent Azure SDK API to push documents and their associated permission metadata into the search index. 
 
 For the [pull model ADLS Gen2 indexer approach](search-indexer-access-control-lists-and-role-based-access.md):
 
 1. Verify that files in the directory are secured using the [ADLS Gen2 access control model](/azure/storage/blobs/data-lake-storage-access-control-model).
-1. Use the [Create Indexer](/rest/api/searchservice/indexers/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true) or equivalent Azure SDK API to create the indexer, index, and data source. 
+1. Use the [Create Indexer](/rest/api/searchservice/indexers/create?view=rest-searchservice-2025-08-01-preview&preserve-view=true) or equivalent Azure SDK API to create the indexer, index, and data source. 
 
 ### Enforce document-level permissions at query time
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレベルアクセス制御の概要に関する更新"
}
```

### Explanation
この修正は、`search-document-level-access-overview.md`というドキュメントに対して行われたもので、主に以下の変更が含まれています：

1. **日付の更新**: ドキュメントの日付が「2025年7月16日」から「2025年8月27日」に変更され、最新の情報が反映されています。

2. **RBACとACLに関する説明の調整**: 論理の整合性を保つために、ACL（Access Control Lists）およびRBAC（Role-Based Access Control）の説明が微調整され、文の構成が改善されています。これにより、利用者が理解しやすくなっています。

3. **パーミッションフィルターの有効化に関するリンクの更新**: パーミッションフィルターの有効化に関連するAPIのバージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新され、最新APIを使用することの重要性が強調されています。

4. **クエリ時のパーミッションフィルターに関する説明の明確化**: クエリ時にパーミッションフィルターを使用する際の要求ヘッダーに`x-ms-query-source-authorization`を追加することに関する記述が更新され、具体的な実装手順が示されています。

5. **ドキュメントのインデクシングに関する手順の見直し**: ドキュメントのインデクシング手順に関して、エラーの管理や設定の確認方法がより明確化されており、ユーザーが自身の設定を効果的に行えるようサポートされています。

これらの変更によって、Azure AI Searchにおけるドキュメントレベルのアクセス権の管理とそれに関連する機能について、利用者がより深く理解できるようになっています。また、これによりドキュメントがより信頼性の高いリファレンス資料となっています。

## articles/search/search-get-started-agentic-retrieval.md{#item-4a40f4}

<details>
<summary>Diff</summary>
````diff
@@ -1,17 +1,17 @@
 ---
-title: "Quickstart: Run agentic retrieval in Azure AI Search"
+title: "Quickstart: Agentic Retrieval"
 titleSuffix: Azure AI Search
 description: Learn how to use agentic retrieval to create a knowledge agent that processes multi-turn conversations.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 7/21/2025
+ms.date: 08/26/2025
 zone_pivot_groups: search-get-started-agentic-retrieval
-#User intent: I want to learn how to use agentic retrieval to create a knowledge agent that processes multi-turn conversations. It should retrieve relevant information from an Azure AI Search index and extract answers using an Azure OpenAI chat model.
+# Customer intent: I want to learn how to use agentic retrieval to create a knowledge agent that processes multi-turn conversations. The agent should retrieve relevant information from a knowledge source that points to an Azure AI Search index and use an Azure OpenAI chat completion model to synthesize answers.
 ---
 
-# Quickstart: Run agentic retrieval in Azure AI Search
+# Quickstart: Use agentic retrieval in Azure AI Search
 
 ::: zone pivot="programming-language-csharp"
 [!INCLUDE [C# quickstart](includes/quickstarts/agentic-retrieval-csharp.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント探索のクイックスタートガイドのタイトル変更"
}
```

### Explanation
この修正は、`search-get-started-agentic-retrieval.md`というドキュメントに対して行われたもので、以下のような変更が含まれています：

1. **タイトルの更新**: ドキュメントのタイトルが「Quickstart: Run agentic retrieval in Azure AI Search」から「Quickstart: Agentic Retrieval」に変更され、より簡潔で明確になりました。

2. **日付の更新**: ドキュメントの日付が「2025年7月21日」から「2025年8月26日」に変更され、最新の情報が反映されています。

3. **顧客の意図の修正**: 顧客の意図を示すセクションの文が更新され、エージェントが「Azure AI Searchインデックス」を指す知識源から関連情報を取得し、Azure OpenAIチャットモデルを使用して回答を合成するように記述されています。これにより、エージェントの機能がより具体的に説明されています。

4. **クイックスタートの見出しの変更**: セクションの見出しが「Quickstart: Run agentic retrieval in Azure AI Search」から「Quickstart: Use agentic retrieval in Azure AI Search」に変更され、内容の実施に対する指示がより直接的になっています。

これらの変更により、ドキュメントの内容がより直感的になり、Azure AI Searchを使用してエージェント探索を行う方法についての理解が深まることが期待されます。また、更新された表現は、ユーザーにとってより理解しやすく、関連性の高いものとなっています。

## articles/search/search-how-to-alias.md{#item-3a72bc}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/29/2025
+ms.date: 08/27/2025
 ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
@@ -23,7 +23,7 @@ An index alias in Azure AI Search is an alternate name for an index. You can use
 Before using an alias, your application sends requests directly to `hotel-samples-index`.
 
 ```http
-POST /indexes/hotel-samples-index/docs/search?api-version=2025-05-01-preview
+POST /indexes/hotel-samples-index/docs/search?api-version=2025-08-01-preview
 {
     "search": "pool spa +airport",
     "select": "HotelId, HotelName, Category, Description",
@@ -34,7 +34,7 @@ POST /indexes/hotel-samples-index/docs/search?api-version=2025-05-01-preview
 After using an alias, your application sends requests to `my-alias`, which maps to `hotel-samples-index`.
 
 ```http
-POST /indexes/my-alias/docs/search?api-version=2025-05-01-preview
+POST /indexes/my-alias/docs/search?api-version=2025-08-01-preview
 {
     "search": "pool spa +airport",
     "select": "HotelId, HotelName, Category, Description",
@@ -54,10 +54,10 @@ You can create an alias using the preview REST API, the preview SDKs, or through
 
 ### [**REST API**](#tab/rest)
 
-You can use the [Create or Update Alias (REST preview)](/rest/api/searchservice/aliases/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) to create an index alias.
+You can use the [Create or Update Alias (REST preview)](/rest/api/searchservice/aliases/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) to create an index alias.
 
 ```http
-POST /aliases?api-version=2025-05-01-preview
+POST /aliases?api-version=2025-08-01-preview
 {
     "name": "my-alias",
     "indexes": ["hotel-samples-index"]
@@ -100,7 +100,7 @@ Aliases can be used for all document operations including querying, indexing, su
 This query sends the request to `my-alias`, which is mapped to an actual index on your search service. 
 
 ```http
-POST /indexes/my-alias/docs/search?api-version=2025-05-01-preview
+POST /indexes/my-alias/docs/search?api-version=2025-08-01-preview
 {
     "search": "pool spa +airport",
     "searchMode": any,
@@ -112,10 +112,10 @@ POST /indexes/my-alias/docs/search?api-version=2025-05-01-preview
 
 ## Update an alias
 
-PUT is required for alias updates as described in [Create or Update Alias (REST preview)](/rest/api/searchservice/aliases/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
+PUT is required for alias updates as described in [Create or Update Alias (REST preview)](/rest/api/searchservice/aliases/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true).
 
 ```http
-PUT /aliases/my-alias?api-version=2025-05-01-preview
+PUT /aliases/my-alias?api-version=2025-08-01-preview
 {
     "name": "my-alias",
     "indexes": ["hotel-samples-index2"]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのエイリアスに関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-how-to-alias.md`というドキュメントに対して行われたもので、以下の変更が含まれています：

1. **日付の更新**: ドキュメントの日付が「2025年5月29日」から「2025年8月27日」に変更され、最新の情報が反映されています。

2. **APIバージョンの更新**: APIのバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更されています。これにより、最近の機能や改善に関する情報が確実に提供されるようになっています。

3. **HTTPリクエスト例の更新**: エイリアスを使用するためのHTTPリクエスト例が更新され、新しいAPIバージョンに基づいた様々なセクション（検索依頼、エイリアス作成など）が見直されています。この更新により、ユーザーは新しいバージョンを使用してリクエストを送信する際の正確な方法を理解できます。

4. **REST APIリファレンスの更新**: エイリアスを作成または更新するためのREST APIリファレンスのリンクも新しいバージョンについて更新され、ユーザーが適切なAPIを利用できるようになります。

これらの変更によって、Azure AI Searchにおけるエイリアスの使用方法がより明確になり、ユーザーが最新のAPI機能を利用しやすくなっています。さらに、文書全体が最新の情報を提供しているため、運用上のトラブルを避けることができるでしょう。

## articles/search/search-how-to-create-search-index.md{#item-c4ff31}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: how-to
-ms.date: 08/07/2025
+ms.date: 08/27/2025
 ---
 
 # Create an index in Azure AI Search
@@ -53,7 +53,7 @@ Use this checklist to assist the design decisions for your search index.
 
 1. Review [supported data types](/rest/api/searchservice/supported-data-types). The data type affects how the field is used. For example, numeric content is filterable but not full text searchable. The most common data type is `Edm.String` for searchable text, which is tokenized and queried using the full text search engine. The most common data type for a vector field is `Edm.Single` but you can use other types as well.
 
-1. Provide a description of the index (preview), 4,000 character maximum. This human-readable text is invaluable when a system must access several indexes and make a decision based on the description. Consider a Model Context Protocol (MCP) server that must pick the correct index at run time. The decision can be  based on the description rather than on index name alone. An index Description field is available in the [2025-05-01-preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true), the Azure portal, or a preview package of an Azure SDK that provides the feature. For more information, see [Add an index description](search-howto-reindex.md#add-an-index-description-preview).
+1. Provide a description of the index (preview), 4,000 character maximum. This human-readable text is invaluable when a system must access several indexes and make a decision based on the description. Consider a Model Context Protocol (MCP) server that must pick the correct index at run time. The decision can be based on the description rather than on index name alone. An index `description` field is available in the [latest preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true), the Azure portal, or a preview package of an Azure SDK that provides the feature. For more information, see [Add an index description](search-howto-reindex.md#add-an-index-description-preview).
 
 1. Identify a [document key](#document-keys). A document key is an index requirement. It's a single string field populated from a source data field that contains unique values. For example, if you're indexing from Blob Storage, the metadata storage path is often used as the document key because it uniquely identifies each blob in the container.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchインデックス作成に関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-how-to-create-search-index.md`というドキュメントに対して行われたもので、以下のような変更が含まれています：

1. **日付の更新**: ドキュメントの日付が「2025年8月7日」から「2025年8月27日」に変更され、最新の情報が反映されています。

2. **APIバージョンの修正**: インデックスの説明フィールドに関する文が更新され、REST APIのバージョンが「2025-05-01-preview」から「最新のプレビューバージョン」に変更されています。これにより、利用可能な最新のAPIに関する情報が強調され、利用者が最も新しいバージョンを参照できるようになっています。

3. **インデックス説明の記述の改善**: フィールドの説明がより明確になり、インデックスの「description」フィールドがREST APIだけでなく、AzureポータルやAzure SDKのプレビューパッケージでも利用可能であることが示されています。この明確な説明は、複数のインデックスにアクセスしなければならないシステムにおいて、インデックスの選択を容易にします。

これらの変更により、Azure AI Searchにおけるインデックス作成のプロセスがより明確になり、ユーザーが最新の情報と最適な実践を活用できるようになります。特にAPIに関する最新の指針が強調されているため、開発者は新しい機能を効果的に利用できるでしょう。

## articles/search/search-how-to-index-logic-apps-indexers.md{#item-64a12e}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Use an Azure Logic Apps workflow for indexer-based indexing in Azur
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 05/19/2025
+ms.date: 08/27/2025
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.custom:
@@ -103,7 +103,7 @@ Currently, the public preview has these limitations:
 + Vectorization supports text embedding only.
 + Deletion detection isn't supported. You must manually [delete orphaned documents](search-howto-reindex.md#delete-orphan-documents) from the index.
 + Duplicate documents in the search index are a known issue in this preview. Consider deleting objects and starting over if this becomes an issue.
-+ No support for private endpoints in the logic app workflow created by the portal wizard. The workflow is hosted using the [**Consumption** hosting option](/azure/logic-apps/single-tenant-overview-compare) and is subject to its constraints. To use the **Standard** hosting option, use a programmatic approach to creating the workflow. Use the [2025-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) or a prerelease Azure SDK package that provides the feature.
++ No support for private endpoints in the logic app workflow created by the portal wizard. The workflow is hosted using the [**Consumption** hosting option](/azure/logic-apps/single-tenant-overview-compare) and is subject to its constraints. To use the **Standard** hosting option, use a programmatic approach to creating the workflow. Use the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) or a prerelease Azure SDK package that provides the feature.
 
 ## Create a logic app workflow
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Logic Appsインデクサーに関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-how-to-index-logic-apps-indexers.md`というドキュメントに対して行われたもので、以下のような変更が含まれています：

1. **日付の更新**: ドキュメントの日付が「2025年5月19日」から「2025年8月27日」に変更されており、最新の情報が反映されています。

2. **APIのバージョンの修正**: Logic Appsワークフローに関する文が更新され、REST APIのバージョンが「2025-05-01-preview」から「最新のプレビューバージョン」に変更されました。これにより、最新のAPIに基づく機能を強調し、利用者が最新の情報を利用できるようにしています。

3. **ワークフローのホスティングオプションの明確化**: Logic Appsワークフローに関する情報が明確化され、ポータルウィザードによって作成されるワークフローが「Consumption」ホスティングオプションでホストされ、その制約に従うことが説明されています。さらに、標準ホスティングオプションを使用するためには、プログラムによるアプローチを取る必要があることが明記されています。

これらの変更によって、Azure Logic Appsを使用したインデクサーに関するドキュメントがより具体的かつ最新の情報を提供し、ユーザーが効果的にこの機能を活用できるようになっています。特に、APIの最新情報が強調されているため、開発者は新しい機能を適切に活かすことが可能です。

## articles/search/search-how-to-index-markdown-blobs.md{#item-c94a20}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 05/29/2025
+ms.date: 08/27/2025
 ms.update-cycle: 180-days
 ---
 
@@ -37,7 +37,7 @@ In Azure AI Search, indexers for Azure Blob Storage, Azure Files, and OneLake su
 Parsing mode parameters are specified in an indexer definition when you create or update an indexer.
 
 ```http
-POST https://[service name].search.windows.net/indexers?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/indexers?api-version=2025-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
@@ -154,7 +154,7 @@ An example index configuration might look something like this:
 If field names and data types align, the blob indexer can infer the mapping without an explicit field mapping present in the request, so an indexer configuration corresponding to the provided index configuration might look like this:
 
 ```http
-POST https://[service name].search.windows.net/indexers?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/indexers?api-version=2025-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
@@ -342,7 +342,7 @@ If you aren't utilizing field mappings, the shape of the index should reflect th
 ### Indexer definition for one-to-one parsing
 
 ```http
-POST https://[service name].search.windows.net/indexers?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/indexers?api-version=2025-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Markdown Blobのインデクシングに関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-how-to-index-markdown-blobs.md`というドキュメントに対して行われたもので、以下のような変更が含まれています：

1. **日付の更新**: ドキュメントの日付が「2025年5月29日」から「2025年8月27日」に変更されています。これにより、最新の情報が提供されていることが反映されています。

2. **APIバージョンの修正**: インデクサーを作成または更新する際のHTTP POSTリクエストのAPIバージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新されています。この変更は、利用者が最新のAPI機能を使用できるようにするためのものです。

3. **リクエストの例の統一性**: いくつかのHTTPリクエストの例において、APIバージョンが統一されることで、リファレンスの整合性が保たれています。これにより、ユーザーは一貫した情報を得やすくなります。特に、インデクサーの作成や設定に関する具体的な手順が明確化されました。

これらの変更により、Azure AI Searchを使用したMarkdown Blobのインデクシングに関するドキュメントがより正確かつ最新の情報を反映したものとなり、ユーザーが容易に理解し実践できるようになっています。特に、新しいAPIバージョンの情報が強調されているため、開発者はより効率的に機能を利用できるでしょう。

## articles/search/search-how-to-managed-identities.md{#item-3536f2}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/07/2025
+ms.date: 08/27/2025
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
@@ -44,7 +44,7 @@ You can use managed identities for these scenarios.
 
 <sup>1</sup> For connectivity between search and storage, network security imposes constraints on which type of managed identity you can use. Only a system managed identity can be used for a same-region connection to Azure Storage, and that connection must be via the *trusted service exception* or resource instance rule. See [Access to a network-protected storage account](search-indexer-securing-resources.md#access-to-a-network-protected-storage-account) for details.
 
-<sup>2</sup> User-assigned managed identities can be used in data source connection strings. However, only the newer preview REST APIs and preview packages support a user-assigned managed identity in a  connection string. Be sure to switch to a preview API if you set [SearchIndexerDataUserAssignedIdentity](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true#searchindexerdatauserassignedidentity) as the `identity` in a data source connection.
+<sup>2</sup> User-assigned managed identities can be used in data source connection strings. However, only the newer preview REST APIs and preview packages support a user-assigned managed identity in a  connection string. Be sure to switch to a preview API if you set [SearchIndexerDataUserAssignedIdentity](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true#searchindexerdatauserassignedidentity) as the `identity` in a data source connection.
 
 <sup>3</sup> Connections to Azure OpenAI,  Azure AI Foundry, and Azure Functions via skills/vectorizers include: [Custom skill](cognitive-search-custom-skill-interface.md), [Custom vectorizer](vector-search-vectorizer-custom-web-api.md), [Azure OpenAI embedding skill](cognitive-search-skill-azure-openai-embedding.md), [Azure OpenAI vectorizer](vector-search-how-to-configure-vectorizer.md), [AML skill](cognitive-search-aml-skill.md) and [Azure AI Foundry model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md).
 
@@ -244,7 +244,7 @@ A system managed identity is indicated when a connection string is the unique re
 
 [**Blob data source (user managed identity):**](search-howto-managed-identities-storage.md)
 
-User-assigned managed identities can also be used in indexer data source connection strings. However, only the newer preview REST APIs and preview packages support a user-assigned managed identity in a data source connection string. Be sure to switch to a preview version if you set [SearchIndexerDataUserAssignedIdentity](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true#searchindexerdatauserassignedidentity) as the identity in a data source connection.
+User-assigned managed identities can also be used in indexer data source connection strings. However, only the newer preview REST APIs and preview packages support a user-assigned managed identity in a data source connection string. Be sure to switch to a preview version if you set [SearchIndexerDataUserAssignedIdentity](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true#searchindexerdatauserassignedidentity) as the identity in a data source connection.
 
 A search service user identity is specified in the `identity `property.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージドIDに関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-how-to-managed-identities.md`というドキュメントに対して行われたもので、以下のような変更が含まれています：

1. **日付の更新**: ドキュメントの日付が「2025年8月7日」から「2025年8月27日」に変更され、最新の情報が反映されています。

2. **APIバージョンの修正**: ユーザー割り当てマネージドIDに関する文が更新され、REST APIのバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更されています。この変更により、ユーザーは新しいAPIを利用することが推奨されます。

3. **リファレンス情報の明確化**: ユーザー割り当てマネージドIDをデータソースの接続文字列に使用する場合について詳しく説明されており、最新のプレビュー版APIやパッケージを使用する必要性が強調されています。これにより、ユーザーは適切なAPIを選択しやすくなるとともに、実装時のエラーを避けることができます。

これらの変更によって、マネージドIDの使用方法に関するドキュメントがより明確かつ最新の情報を提供し、ユーザーが正確にマネージドIDを設定し利用できるようになっています。特に、新しいAPIバージョンの情報に注意することで、開発者は最新の機能を効果的に利用することができます。

## articles/search/search-howto-index-mysql.md{#item-5d31c4}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ manager: nitinme
 ms.devlang: rest-api
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/29/2025
+ms.date: 08/27/2025
 ms.update-cycle: 365-days
 ms.custom:
   - kr2b-contr-experiment
@@ -51,7 +51,7 @@ As noted, there’s no portal support for indexer creation, but a MySQL indexer
 
 The data source definition specifies the data to index, credentials, and policies for identifying changes in the data. The data source is defined as an independent resource so that it can be used by multiple indexers.
 
-[Create or Update Data Source](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true) specifies the definition. Be sure to use a preview REST API when creating the data source.
+[Create or Update Data Source](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2025-08-01-preview&preserve-view=true) specifies the definition. Be sure to use a preview REST API when creating the data source.
 
 ```http
 {   
@@ -89,7 +89,7 @@ The data source definition specifies the data to index, credentials, and policie
 
 ## Create an index
 
-[Create or Update Index](/rest/api/searchservice/indexes/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true) specifies the index schema:
+[Create or Update Index](/rest/api/searchservice/indexes/create?view=rest-searchservice-2025-08-01-preview&preserve-view=true) specifies the index schema:
 
 ```http
 {
@@ -129,7 +129,7 @@ The following table maps the MySQL database to Azure AI Search equivalents. For
 
 Once the index and data source have been created, you're ready to create the indexer. Indexer configuration specifies the inputs, parameters, and properties controlling run time behaviors.
 
-[Create or update an indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) by giving it a name and referencing the data source and target index:
+[Create or update an indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) by giving it a name and referencing the data source and target index:
 
 ```http
 {
@@ -158,10 +158,10 @@ Once the index and data source have been created, you're ready to create the ind
 
 ## Check indexer status
 
-Send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-05-01-preview&preserve-view=true) request to monitor indexer execution:
+Send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-08-01-preview&preserve-view=true) request to monitor indexer execution:
 
 ```http
-GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2025-05-01-preview
+GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2025-08-01-preview
   Content-Type: application/json  
   api-key: [admin key]
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MySQLインデクシングに関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-howto-index-mysql.md`というドキュメントに対して行われたもので、以下のような変更が含まれています：

1. **日付の更新**: ドキュメントの日付が「2025年5月29日」から「2025年8月27日」に変更されています。これにより、情報が最新であることが反映されています。

2. **APIバージョンの修正**: ドキュメント内の複数のリファレンスにおいて、MySQLインデクサーに関連するREST APIバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更されています。この修正により、ユーザーは最新のAPIを使用することが推奨されています。

3. **手順の一貫性**: データソースの作成やインデクサーの更新に関する手順で、APIバージョンの変更が一貫して適用されています。これにより、利用者は正確なバージョンに基づいて設定を行うことができ、エラーを未然に防ぐことが可能になります。

これらの更新により、MySQLインデクシングに関するドキュメントがより明確で、最新の情報を反映したものとなっています。特に新しいAPIバージョンについての情報が強調されることで、開発者は最新の機能を適切に利用できるようになります。

## articles/search/search-howto-index-sharepoint-online.md{#item-49ff6e}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/13/2025
+ms.date: 08/27/2025
 ms.custom:
   - ignite-2023
   - sfi-image-nochange
@@ -105,7 +105,7 @@ We recommend app-based permissions. See [limitations](#limitations-and-considera
 
 + Application permissions (recommended), where the indexer runs under the [identity of the SharePoint tenant](/sharepoint/dev/solution-guidance/security-apponly-azureacs) with access to all sites and files. The indexer requires a [client secret](/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow). The indexer will also require [tenant admin approval](/azure/active-directory/manage-apps/grant-admin-consent) before it can index any content.
 
-+ Delegated permissions, where the indexer runs under the identity of the user or app sending the request. Data access is limited to the sites and files to which the caller has access. To support delegated permissions, the indexer requires a [device code prompt](/azure/active-directory/develop/v2-oauth2-device-code) to sign in on behalf of the user. User-delegated permissions enforce token expiration every 75 minutes, per the most recent security libraries used to implement this authentication type. This isn't a behavior that can be adjusted. An expired token requires manual indexing using [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true). For this reason, you should use app-based permissions instead.
++ Delegated permissions, where the indexer runs under the identity of the user or app sending the request. Data access is limited to the sites and files to which the caller has access. To support delegated permissions, the indexer requires a [device code prompt](/azure/active-directory/develop/v2-oauth2-device-code) to sign in on behalf of the user. User-delegated permissions enforce token expiration every 75 minutes, per the most recent security libraries used to implement this authentication type. This isn't a behavior that can be adjusted. An expired token requires manual indexing using [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2025-08-01-preview&tabs=HTTP&preserve-view=true). For this reason, you should use app-based permissions instead.
 
 <a name='step-3-create-an-azure-ad-application'></a>
 
@@ -182,10 +182,10 @@ For SharePoint indexing, the data source must have the following required proper
 + **credentials** provide the SharePoint endpoint and the Microsoft Entra application (client) ID. An example SharePoint endpoint is `https://microsoft.sharepoint.com/teams/MySharePointSite`. You can get the endpoint by navigating to the home page of your SharePoint site and copying the URL from the browser.
 + **container** specifies which document library to index. Properties [control which documents are indexed](#controlling-which-documents-are-indexed).
 
-To create a data source, call [Create Data Source (preview)](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
+To create a data source, call [Create Data Source (preview)](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2025-08-01-preview&preserve-view=true).
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2025-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
@@ -218,10 +218,10 @@ You can get tenant ID from the overview page in the Microsoft Entra admin center
 
 The index specifies the fields in a document, attributes, and other constructs that shape the search experience.
 
-To create an index, call [Create Index (preview)](/rest/api/searchservice/indexes/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true):
+To create an index, call [Create Index (preview)](/rest/api/searchservice/indexes/create?view=rest-searchservice-2025-08-01-preview&preserve-view=true):
 
 ```http
-POST https://[service name].search.windows.net/indexes?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/indexes?api-version=2025-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
@@ -251,10 +251,10 @@ If you're using delegated permissions, during this step, you’re asked to sign
 
 There are a few steps to creating the indexer:
 
-1. Send a [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) request:
+1. Send a [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-08-01-preview&tabs=HTTP&preserve-view=true) request:
 
     ```http
-    POST https://[service name].search.windows.net/indexers?api-version=2025-05-01-preview
+    POST https://[service name].search.windows.net/indexers?api-version=2025-08-01-preview
     Content-Type: application/json
     api-key: [admin key]
     
@@ -287,17 +287,17 @@ There are a few steps to creating the indexer:
 
    If you're using application permissions, it's necessary to wait until the initial run is complete before starting to query your index. The following instructions provided in this step pertain specifically to delegated permissions, and aren't applicable to application permissions.
 
-1. When you create the indexer for the first time, the [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) request waits until you complete the next step. You must call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) to get the link and enter your new device code. 
+1. When you create the indexer for the first time, the [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-08-01-preview&tabs=HTTP&preserve-view=true) request waits until you complete the next step. You must call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-08-01-preview&tabs=HTTP&preserve-view=true) to get the link and enter your new device code. 
 
     ```http
-    GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2025-05-01-preview
+    GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2025-08-01-preview
     Content-Type: application/json
     api-key: [admin key]
     ```
 
-    If you don’t run the [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) within 10 minutes, the code expires and you’ll need to recreate the [data source](#create-data-source).
+    If you don’t run the [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-08-01-preview&tabs=HTTP&preserve-view=true) within 10 minutes, the code expires and you’ll need to recreate the [data source](#create-data-source).
 
-1. Copy the device login code from the [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) response. The device login can be found in the "errorMessage".
+1. Copy the device login code from the [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-08-01-preview&tabs=HTTP&preserve-view=true) response. The device login can be found in the "errorMessage".
 
     ```http
     {
@@ -320,18 +320,18 @@ There are a few steps to creating the indexer:
 
     :::image type="content" source="media/search-howto-index-sharepoint-online/aad-app-approve-api-permissions.png" alt-text="Screenshot showing how to approve API permissions.":::
 
-1. The [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) initial request completes if all the permissions provided above are correct and within the 10 minute timeframe.
+1. The [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-08-01-preview&tabs=HTTP&preserve-view=true) initial request completes if all the permissions provided above are correct and within the 10 minute timeframe.
 
 > [!NOTE]
 > If the Microsoft Entra application requires admin approval and was not approved before logging in, you may see the following screen. [Admin approval](/azure/active-directory/manage-apps/grant-admin-consent) is required to continue.
 :::image type="content" source="media/search-howto-index-sharepoint-online/no-admin-approval-error.png" alt-text="Screenshot showing admin approval required.":::
 
 ### Step 7: Check the indexer status
 
-After the indexer has been created, you can call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true):
+After the indexer has been created, you can call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-08-01-preview&tabs=HTTP&preserve-view=true):
 
 ```http
-GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2025-05-01-preview
+GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2025-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 ```
@@ -344,18 +344,18 @@ However, if you modify the data source object while the device code is expired,
 
 Here are the steps for updating a data source, assuming an expired device code:
 
-1. Call [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true) to manually start [indexer execution](search-howto-run-reset-indexers.md).
+1. Call [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2025-08-01-preview&tabs=HTTP&preserve-view=true) to manually start [indexer execution](search-howto-run-reset-indexers.md).
 
     ```http
-    POST https://[service name].search.windows.net/indexers/sharepoint-indexer/run?api-version=2025-05-01-preview  
+    POST https://[service name].search.windows.net/indexers/sharepoint-indexer/run?api-version=2025-08-01-preview  
     Content-Type: application/json
     api-key: [admin key]
     ```
 
-1. Check the [indexer status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-05-01-preview&tabs=HTTP&preserve-view=true). 
+1. Check the [indexer status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-08-01-preview&tabs=HTTP&preserve-view=true). 
 
     ```http
-    GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2025-05-01-preview
+    GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2025-08-01-preview
     Content-Type: application/json
     api-key: [admin key]
     ```
@@ -398,7 +398,7 @@ You can control which files are indexed by setting inclusion and exclusion crite
 Include specific file extensions by setting `"indexedFileNameExtensions"` to a comma-separated list of file extensions (with a leading dot). Exclude specific file extensions by setting `"excludedFileNameExtensions"` to the extensions that should be skipped. If the same extension is in both lists, it's excluded from indexing.
 
 ```http
-PUT /indexers/[indexer name]?api-version=2025-05-01-preview
+PUT /indexers/[indexer name]?api-version=2025-08-01-preview
 {
     "parameters" : { 
         "configuration" : { 
@@ -449,7 +449,7 @@ The "query" parameter of the data source is made up of keyword/value pairs. The
 By default, the SharePoint Online indexer stops as soon as it encounters a document with an unsupported content type (for example, an image). You can use the `excludedFileNameExtensions` parameter to skip certain content types. However, you might need to index documents without knowing all the possible content types in advance. To continue indexing when an unsupported content type is encountered, set the `failOnUnsupportedContentType` configuration parameter to false:
 
 ```http
-PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2025-05-01-preview
+PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2025-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint Onlineインデクシングに関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-howto-index-sharepoint-online.md`というドキュメントに対して行われたもので、以下のような内容が変更されています：

1. **日付の更新**: ドキュメントの日付が「2025年8月13日」から「2025年8月27日」に変更されています。この更新により、内容が最新のものとなっていることが明確になっています。

2. **APIバージョンの修正**: ドキュメント中の複数の場所で使用されているREST APIバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更されており、これにより最新のAPI仕様に基づいて情報が更新されています。

3. **アプリケーション権限に関する追加情報**: アプリケーション権限の推奨が強調され、インデクサーがSharePointテナントのアイデンティティの下で実行されることが記述されています。また、クライアントシークレットやテナント管理者の承認に関する情報が具体的に含まれています。

4. **手順の更新**: データソースとインデクサーの作成手順において、API呼び出しのリンクが最新のものに更新されており、ユーザーは正しいバージョンを参照して手続きを行うことができます。

これらの変更により、SharePoint Onlineへのインデクシングに関するドキュメントが明確で最新の情報を反映したものとなり、特にAPIのバージョンやインデクサーの設定に関して、ユーザーがV最新の仕様に基づいて作業を行えるようになります。

## articles/search/search-howto-managed-identities-cosmos-db.md{#item-a74464}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: arv100kri
 ms.author: arjagann
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/07/2025
+ms.date: 08/27/2025
 ms.update-cycle: 365-days
 ms.custom:
   - subject-rbac-steps
@@ -126,7 +126,7 @@ You need to add an "identity" property to the data source definition, where you
 Here's an example using user-assigned identity via the _modern_ approach.
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2025-08-01-preview
 {
     "name": "[my-cosmosdb-ds]",
     "type": "cosmosdb",
@@ -158,7 +158,7 @@ Follow the same steps as before to assign the appropriate roles on the control p
 Here's an example to connect to MongoDB collections using system-assigned identity via the REST API
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2025-08-01-preview
 {
     "name": "my-cosmosdb-ds",
     "type": "cosmosdb",
@@ -173,7 +173,7 @@ POST https://[service name].search.windows.net/datasources?api-version=2025-05-0
 Here's an example to connect to Gremlin graphs using user-assigned identity.
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2025-08-01-preview
 {
     "name": "[my-cosmosdb-ds]",
     "type": "cosmosdb",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cosmos DBにおけるマネージドIDの使用に関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-howto-managed-identities-cosmos-db.md`というドキュメントに対して行われたもので、以下の変更が反映されています：

1. **日付の更新**: ドキュメントの日付が「2025年8月7日」から「2025年8月27日」に変更され、内容が最新であることを示しています。

2. **APIバージョンの修正**: 複数の場所で使用されるREST APIバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更されました。これにより、ユーザーは最新のAPI仕様に基づいて正しい情報で作業できるようになります。

3. **サンプルの一貫性**: Cosmos DBへの接続に関するサンプルコードが更新され、最新のAPIバージョンに準拠していることが確認できます。特に、ユーザー割り当ておよびシステム割り当てのIDを使用したデータソースの定義に関する具体例が提供されています。

これらの変更により、マネージドIDをCosmos DBに使用するための手順がより明確になり、利用者が最新の情報に基づいて設定を行えるようになっています。また、APIのバージョン管理が行われることで、将来的な互換性が確保されています。

## articles/search/search-howto-managed-identities-sql.md{#item-2af8aa}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: gimondra
 manager: nitinme
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/29/2025
+ms.date: 08/27/2025
 ms.update-cycle: 365-days
 ms.custom:
   - subject-rbac-steps
@@ -124,10 +124,10 @@ Preview REST APIs support connections based on a user-assigned managed identity.
 
 * Second, add an "identity" property that contains the collection of user-assigned managed identities. Only one user-assigned managed identity should be provided when creating the data source. Set it to type "userAssignedIdentities".
 
-Here's an example of how to create an indexer data source object using the most recent preview API version for [Create or Update Data Source](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true):
+Here's an example of how to create an indexer data source object using the most recent preview API version for [Create or Update Data Source](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true):
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2025-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SQLにおけるマネージドIDの使用に関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-howto-managed-identities-sql.md`というドキュメントに対するもので、以下の変更が含まれています：

1. **日付の更新**: ドキュメントの日付が「2025年5月29日」から「2025年8月27日」に変更され、最新の情報に更新されています。

2. **APIバージョンの修正**: 使用されるREST APIバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更されており、これによってユーザーは最新のAPIの仕様に基づいて正しい情報で作業できるようになります。

3. **サンプルの適用**: データソースオブジェクトの作成に関する具体的な例が最新のAPIバージョンに合わせて更新されています。この更新によって、ユーザーはマネージドIDを使用したデータソースの設定方法をより明確に理解できるようになります。

この修正により、SQLデータベースとの接続に関するマネージドIDの使用が先進的かつ確実に管理されるようになり、ユーザーが最新の手順に従って設定を行いやすくなっています。

## articles/search/search-howto-managed-identities-storage.md{#item-8209c4}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: gimondra
 manager: vinodva
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 02/18/2025
+ms.date: 08/27/2025
 ms.update-cycle: 365-days
 ms.custom:
   - subject-rbac-steps
@@ -99,7 +99,7 @@ Provide a connection string that contains a `ResourceId`, with no account key or
 Provide an `identity` using the syntax shown in the following example. Set `userAssignedIdentity` to the user-assigned managed identity.
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2025-08-01-preview
 
 {
     "name" : "blob-datasource",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ストレージにおけるマネージドIDの使用に関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-howto-managed-identities-storage.md`というドキュメントに対して行われたもので、以下の変更が含まれています：

1. **日付の更新**: ドキュメントの日付が「2025年2月18日」から「2025年8月27日」に変更され、情報が最新の状態に維持されています。

2. **APIバージョンの修正**: 使用されるREST APIバージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新され、ユーザーが最新の機能と仕様に基づいて作業できるようになっています。

3. **サンプルの整合性**: データソースの作成に関する例が最新のAPIバージョンに対応して更新され、ユーザーはマネージドIDを利用する際の具体的な手順を理解しやすくなっています。

この修正により、ストレージサービスにおけるマネージドIDの使用についてのドキュメントの正確性が向上し、利用者が新しいAPIに基づいて適切に管理できるようになります。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 05/19/2025
+ms.date: 08/27/2025
 ms.update-cycle: 180-days
 ---
 
@@ -286,11 +286,11 @@ The Azure portal supports the latest preview API.
 
 1. Copy the JSON so that you can use it as the basis of a new request.
 
-1. [Formulate an index update using a PUT request](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true) and the preview API.
+1. [Formulate an index update using a PUT request](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) and the latest preview REST API.
 
 1. Provide the *full* JSON of the existing schema, plus the new `description` field. The field must be a top-level field, on the same level as `name` or `fields`. The value must be less than 4,000 characters and in Unicode.
 
-1. To confirm the change, issue another [GET using the 2025-05-01-preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
+1. To confirm the change, issue another [GET using the latest preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true).
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "再インデックス作業に関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-howto-reindex.md`というドキュメントに対するものであり、以下の主要な変更が行われています：

1. **日付の更新**: ドキュメントの日付が「2025年5月19日」から「2025年8月27日」に変更され、新しい情報を反映したものとなっています。

2. **APIバージョンの修正**: インデックス更新のためのPUTリクエストを作成する際に参照するAPIバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更されています。これにより、ユーザーは最新のAPI仕様に基づいて作業ができるようになります。

3. **確認手順の更新**: 変更を確認するためのGETリクエストの参照も、同様に最新のAPIバージョンに更新されています。

これらの修正により、再インデックス作業に関する手順がより最新で正確な情報に基づいて明確化され、ユーザーの利便性が高まっています。

## articles/search/search-howto-run-reset-indexers.md{#item-fb10c8}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/19/2025
+ms.date: 09/01/2025
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
@@ -26,7 +26,7 @@ This article explains how to run indexers on demand, with and without a reset. I
 
 ## How indexers connect to Azure resources
 
-Indexers are one of the few subsystems that make overt outbound calls to other Azure resources. You can use keys or roles to authenticate the connection.
+Indexers are one of the few subsystems that make overt outbound calls to other Azure resources. Depending on the external data source, you can use keys or roles to authenticate the connection.
 
 In terms of Azure roles, indexers don't have separate identities: a connection from the search engine to another Azure resource is made using the [system or user-assigned managed identity](search-how-to-managed-identities.md) of a search service, plus a role assignment on the target Azure resource. If the indexer connects to an Azure resource on a virtual network, you should create a [shared private link](search-indexer-howto-access-private.md) for that connection.
 
@@ -261,7 +261,7 @@ POST https://[service name].search.windows.net/indexers/[indexer name]/resetdocs
 
 ## How to resync indexers (preview)
 
-[Resync Indexers](/rest/api/searchservice/indexers/resync?view=rest-searchservice-2025-05-01-preview&preserve-view=true) is a new preview API that performs a partial reindex of all documents.
+[Resync Indexers](/rest/api/searchservice/indexers/resync?view=rest-searchservice-2025-08-01-preview&preserve-view=true) is a preview REST API that performs a partial reindex of all documents.
 An indexer is considered synchronized with its data source when specific fields of all documents in the target index are consistent with the data in the data source. Typically, an indexer achieves synchronization after a successful initial run. If a document is deleted from the data source, the indexer remains synchronized according to this definition. However, during the next indexer run, the corresponding document in the target index will be removed if delete tracking is enabled.
 
 If a document is modified in the data source, the indexer becomes unsynchronized. Generally, change tracking mechanisms will resynchronize the indexer during the next run. For example, in Azure Storage, modifying a blob updates its last modified time, allowing it to be re-indexed in the subsequent indexer run because the updated time surpasses the high-water mark set by the previous run.
@@ -272,13 +272,12 @@ While using either "reset" or "reset docs" can address this issue, "reset" can b
 
 Resync Indexers offers an efficient and convenient alternative. Users simply place the indexer in resync mode and specify the content to resynchronize by calling the resync indexers API. In the next run, the indexer will inspect only relevant portion of data in the source and avoid any unnecessary processing that is unrelated to the specified data.  It will also query the existing documents in the target index and only update the documents that show discrepancies between the data source and the target index. After the resync run, the indexer will be synchronized and revert to regular indexer run mode for subsequent runs.
 
-
 ### How to resync and run indexers
 
-1. Call [Indexers - Resync](/rest/api/searchservice/indexers/resync?view=rest-searchservice-2025-05-01-preview&preserve-view=true) with a preview API version to specify what content to re-synchronize.
+1. Call [Indexers - Resync](/rest/api/searchservice/indexers/resync?view=rest-searchservice-2025-08-01-preview&preserve-view=true) with a preview API version to specify what content to re-synchronize.
 
     ```http
-    POST https://[service name].search.windows.net/indexers/[indexer name]/resync?api-version=2025-05-01-preview
+    POST https://[service name].search.windows.net/indexers/[indexer name]/resync?api-version=2025-08-01-preview
     {
         "options" : [
             "permissions"
@@ -295,7 +294,7 @@ Resync Indexers offers an efficient and convenient alternative. Users simply pla
 
 To check reset status and to see which document keys are queued up for processing, following these steps.
 
-1. Call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2024-05-01-preview&preserve-view=true) with a preview API. 
+1. Call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-08-01-preview&preserve-view=true) with a preview API. 
 
    The preview API will return the **`currentState`** section, found at the end of the response.
 
@@ -325,6 +324,38 @@ To check reset status and to see which document keys are queued up for processin
 
 1. After the documents are reprocessed, run Get Indexer Status again. The indexer returns to the **`indexingAllDocs`** mode and will process any new or updated documents on the next run.
 
+## Check indexer runtime quota for S3 HD search services
+
+Applies to search services at the Standard 3 High Density (S3 HD) pricing tier.
+
+To help you monitor indexer running times relative to the 24-hour window, [Get Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics#servicestatistics?view=rest-searchservice-2025-08-01-preview&preserve-view=true) and [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2025-08-01-preview&preserve-view=true) now return more information in the response.
+
+### Track cumulative runtime quota
+
+Track a search service's cumulative indexer runtime usage and determine how much runtime quota is left within the current 24-hour window period.
+
+Send a GET request to the search service resource provider. For help with setting up a REST client and getting an access token, see [Connect to a search service](/azure/search/search-get-started-rbac?pivots=rest).
+
+```http
+GET {{search-endpoint}}/servicestats?api-version=2025-08-01-preview 
+  Content-Type: application/json
+  Authorization: Bearer {{accessToken}}
+```
+
+Responses include `indexersRuntime` properties, showing start and end times, seconds used, seconds remaining, and cumulative runtime within the last 24 hours.
+
+### Track indexer runtime quota
+
+Return the same information for a single indexer.
+
+```http
+GET {{search-endpoint}}/indexers/hotels-sample-indexer/search.status?api-version=2025-08-01-preview 
+  Content-Type: application/json
+  Authorization: Bearer {{accessToken}}
+```
+
+Responses include a `runtime` properties, showing start and end times, seconds used, and seconds remaining.
+
 ## Next steps
 
 Reset APIs are used to inform the scope of the next indexer run. For actual processing, you'll need to invoke an on-demand indexer run or allow a scheduled job to complete the work. After the run is finished, the indexer returns to normal processing, whether that is on a schedule or on-demand processing.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーのリセットに関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-howto-run-reset-indexers.md`というドキュメントに対して行われたもので、主要な変更点は以下の通りです：

1. **日付の更新**: ドキュメントの日付が「2025年3月19日」から「2025年9月1日」に変更され、新しい情報を反映しています。

2. **文言の改善**: インデクサーがAzureリソースに接続する方法についての記述が強化され、外部データソースに応じて認証に使用するキーやロールについての説明が追加されました。これにより、利用者が認証方法についてより明確に理解できるようになっています。

3. **APIバージョンの更新**: リセットと再同期に関連するAPIのバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更され、最新のAPIを使用することが強調されています。

4. **新しい機能の追加**: S3 HD検索サービスのインデクサーの実行時間クォータを確認するための手順が追加され、インデクサーの累積実行時間の使用状況を追跡する機能が説明されています。この新機能により、ユーザーはインデクサーの実行時間を効率的に管理できるようになっています。

これらの修正により、インデクサーのリセットや管理に関するドキュメントが最新かつ分かりやすい情報に基づいて更新され、利用者にとって利便性が向上しています。

## articles/search/search-index-access-control-lists-and-rbac-push-api.md{#item-45e71e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how to use the REST API for indexing documents with ACLs and RBAC metadata.  
 ms.service: azure-ai-search  
 ms.topic: how-to 
-ms.date: 07/16/2025 
+ms.date: 08/27/2025 
 author: admayber
 ms.author: admayber  
 ---  
@@ -13,7 +13,7 @@ ms.author: admayber
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Indexing documents, along with their associated [Access Control Lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control) and container [Role-Based Access Control (RBAC) roles](/azure/role-based-access-control/overview), into an Azure AI Search index via the [push REST APIs](/rest/api/searchservice/documents/?view=rest-searchservice-2025-05-01-preview&preserve-view=true) preserves document-level permission on indexed content at query time. 
+Indexing documents, along with their associated [Access Control Lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control) and container [Role-Based Access Control (RBAC) roles](/azure/role-based-access-control/overview), into an Azure AI Search index via the [push REST APIs](/rest/api/searchservice/documents/?view=rest-searchservice-2025-08-01-preview&preserve-view=true) preserves document-level permission on indexed content at query time.
 
 Key features include:
 
@@ -27,7 +27,7 @@ This article explains how to use the push REST API to index document-level permi
 
 - Content with ACL metadata from [Microsoft Entra ID](/entra/fundamentals/whatis) or another POSIX-style ACL system. 
 
-- Preview REST API version [2025-05-01-preview](/rest/api/searchservice/documents/?view=rest-searchservice-2025-05-01-preview&preserve-view=true) or a preview Azure SDK package providing equivalent features.
+- The [latest preview REST API](/rest/api/searchservice/documents/?view=rest-searchservice-2025-08-01-preview&preserve-view=true) or a preview Azure SDK package providing equivalent features.
 
 - An index schema with a `permissionFilterOption` enabled, plus `permissionFilter` field attributes that store the permissions associated with the document.
 
@@ -37,15 +37,19 @@ This article explains how to use the push REST API to index document-level permi
 
 - An index can hold at most five unique values among fields of type `rbacScope` on all documents. There's no limit on the number of documents that share the same value of `rbacScope`.
 
-- A preexisting field can't be converted into a `permissionFilter` field type for use with built-in ACLs or RBAC metadata filtering. To enable filtering on an existing index, new fields must be created with the correct permission filter type.
+- A preexisting field can be converted into a `permissionFilter` field type for use with built-in ACLs or RBAC metadata filtering. To enable filtering on an existing index, create new fields or modify an existing field to include a `permissionFilter`.
 
 - Only one field of each `permissionFilter` type (one each of `groupIds`, `usersIds`, and `rbacScope`) can exist in an index.
 
+- Each permissionFilter field should have `filterable` set to true.
+
 ## Create an index with permission filter fields
 
 Indexing document ACLs and RBAC metadata with the REST API requires setting up an index schema that enables permission filters and has fields with permission filter assignments.
 
-Permission filter field types can be added to an existing index on new fields. The value of `permissionFilterOption` can be set to either `enabled` or `disabled` while indexing documents. However, setting it to `disabled` turns off the permission filter functionality.
+First, add a `permissionFilterOption` option. Valid values are `enabled` or `disabled`, and you should set it to `enabled`. You can switch it to `disabled` if you want to turn off the permission filter functionality at the index level.
+
+Second, create string fields for your permission metadata and include `permissionFilter`. Recall that you can have one of each permission filter type.
 
 Here's a basic example schema that includes all `permissionFilter` types:
 
@@ -63,10 +67,10 @@ Here's a basic example schema that includes all `permissionFilter` types:
 
 ## REST API indexing example
 
-Once you have an index with the desired permission filter fields, you can populate those values using the indexing push API as with any other document fields. Here's an example using the specified index schema.
+Once you have an index with permission filter fields, you can populate those values using the indexing push API as with any other document fields. Here's an example using the specified index schema, where each document specifies the upload action, the key field (DocumentId), and permission fields. It should also have content, but that field is omitted in this example for brevity.
 
 ```https
-POST https://exampleservice.search.windows.net/indexes('indexdocumentsexample')/docs/search.index?api-version=2025-05-01-preview
+POST https://exampleservice.search.windows.net/indexes('indexdocumentsexample')/docs/search.index?api-version=2025-08-01-preview
 {
   "value": [
     {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスアクセス制御リストとRBACに関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-index-access-control-lists-and-rbac-push-api.md`というドキュメントに適用されたもので、以下の主要な変更点が含まれています：

1. **日付の更新**: ドキュメントの日付が「2025年7月16日」から「2025年8月27日」に変更され、新しい情報を反映しています。

2. **APIバージョンの改訂**: プッシュREST APIに関連するバージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新され、最新のAPI仕様に基づいていることが強調されています。

3. **内容の明確化**: ドキュメント内のいくつかの記述が改良され、特に「permissionFilter」と「RBAC」に関連するフィールドに関する説明が詳細になっています。特に、既存のフィールドを「permissionFilter」フィールドタイプに変換できる点に関する説明が明確化され、新しいフィールドを作成するか、既存のフィールドを修正することによってフィルター機能を有効にできることが示されています。

4. **新しい設定手順の追加**: インデクサーの設定時に「permissionFilterOption」を「enabled」として設定する手順が追加され、具体的なフィールドの設定方法にも言及されています。

5. **REST APIインデクシングの例の改善**: 例として示されるインデックススキーマの説明がより詳細になり、各ドキュメントがどのようにアップロードアクション、キーフィールド、パーミッションフィールドを指定するかを明示しています。

これにより、ユーザーはAzure AI Searchのインデクサ―の使用とアクセス制御の管理に関する最新の情報をより理解しやすくなり、実施できる手順が具体的に示されています。

## articles/search/search-indexer-access-control-lists-and-role-based-access.md{#item-67b42f}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how to configure Azure AI Search indexers for ingesting Access Control Lists (ACLs) and Azure Role-Based Access (RBAC) metadata on Azure Data Lake Storage (ADLS) Gen2 blobs.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/08/2025  
+ms.date: 08/27/2025  
 author: wlifuture
 ms.author: wli
 ---  
@@ -21,9 +21,9 @@ The indexer approach is built on this foundation:
 
 + [The ADLS Gen2 access control model](/azure/storage/blobs/data-lake-storage-access-control-model) that provides [Access control lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control-model#access-control-lists-acls) and [Role-based access control (Azure RBAC)](/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac). There's no support for Attribute-based access control (Azure ABAC).
 
-+ [An Azure AI Search indexer for ADLS Gen2](search-howto-index-azure-data-lake-storage.md) that retrieves and ingests data and metadata, including permission filters. To get permission filter support, you must use the 2025-05-01-preview REST API or a prerelease package of an Azure SDK that supports the feature.
++ [An Azure AI Search indexer for ADLS Gen2](search-howto-index-azure-data-lake-storage.md) that retrieves and ingests data and metadata, including permission filters. To get permission filter support, use the latest preview REST API or a prerelease package of an Azure SDK that supports the feature.
 
-+ [An index in Azure AI Search](search-how-to-create-search-index.md) containing the ingested documents and corresponding permissions. Permission metadata is stored as fields in the index. To set up queries that respect the permission filters, you must use the 2025-05-01-preview REST API or a prerelease package of an Azure SDK that supports the feature.
++ [An index in Azure AI Search](search-how-to-create-search-index.md) containing the ingested documents and corresponding permissions. Permission metadata is stored as fields in the index. To set up queries that respect the permission filters, use the latest preview REST API or a prerelease package of an Azure SDK that supports the feature.
 
 <!-- Addison has a concept article for doc-level permission concept. we should link to that instead. -->
 This functionality helps align [document-level permissions](search-security-trimming-for-azure-search.md) in the search index with the access controls defined in ADLS Gen2, allowing users to retrieve content in a way that reflects their existing permissions.
@@ -265,11 +265,10 @@ Choose one of the following mechanisms, depending on how many items changed:
 | **Dozens to thousands of blobs** | Call [/resetdocs (preview)](search-howto-run-reset-indexers.md#how-to-reset-docs-preview) and list the affected document keys. | Document content **and** ACL/RBAC metadata               |  
 | **Entire data source**          | Call [/resync (preview)](search-howto-run-reset-indexers.md#how-to-resync-indexers-preview) with the permissions option.              | **Only** ACL/RBAC metadata (content is left untouched)    |
 
-
 **Resetdocs (preview) API example:**
 
    ```http
-   POST https://{service}.search.windows.net/indexers/{indexer}/resetdocs?api-version=2025-05-01-preview 
+   POST https://{service}.search.windows.net/indexers/{indexer}/resetdocs?api-version=2025-08-01-preview 
    { 
      "documentKeys": [ 
        "1001", 
@@ -281,7 +280,7 @@ Choose one of the following mechanisms, depending on how many items changed:
 **Resync (preview) API example:**
 
    ```http
-   POST https://{service}.search.windows.net/indexers/{indexer}/resync?api-version=2025-05-01-preview 
+   POST https://{service}.search.windows.net/indexers/{indexer}/resync?api-version=2025-08-01-preview 
    { 
      "options": [ 
        "permissions" 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーのアクセス制御リストとRBACに関するドキュメントの更新"
}
```

### Explanation
この修正は、`search-indexer-access-control-lists-and-role-based-access.md`という文章に対して行われたもので、以下の重要な変更が含まれています：

1. **日付の更新**: ドキュメントの日付が「2025年5月8日」から「2025年8月27日」に変更され、新しい情報が反映されています。

2. **APIバージョンの更新**: インデクサーの機能に関する記述で、REST APIのバージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新されています。この変更により、最新のAPIを使用する重要性が強調されています。

3. **トラックバックの明確化**: 特にADLS Gen2のアクセス制御モデルに関する記述が改善され、役割に基づくアクセス制御（RBAC）の使用条件や、必要となる新しいプレビューAPIの情報が詳しく説明されています。

4. **クエリ設定の強調**: インデックス内のパーミッションメタデータの設定方法が強調され、これに関連するAPIの情報が明確化されています。ユーザーは、パーミッションフィルターを尊重するクエリを設定する際に、最新のプレビューREST APIを使用する必要があることが伝えられています。

5. **API例のバージョン変更**: 「resetdocs」および「resync」APIのエンドポイントの記述においても、最新のプレビューAPIバージョンに基づく変更が行われています。

これらの修正により、ユーザーはAzure AI Searchのインデクサーの設定およびアクセス制御の管理について、より最新かつ正確な情報を理解できるようになり、実際の使用に役立つ内容が提供されています。

## articles/search/search-knowledge-source-how-to-blob.md{#item-58d84a}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,242 @@
+---
+title: Create a blob knowledge source
+titleSuffix: Azure AI Search
+description: A blob knowledge source specifies a blob container that you want to read from. It also includes models and properties for creating an indexer, data source, skillset, and index used for agentic retrieval workloads.
+manager: nitinme
+author: HeidiSteen
+ms.author: heidist
+ms.service: azure-ai-search
+ms.topic: how-to
+ms.date: 08/29/2025
+---
+
+# Create a blob knowledge source
+
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+A *blob knowledge source* specifies all of the information necessary for indexing and querying multimodal Azure blob content in an Azure AI Search agentic pipeline. It's created independently, and then referenced by a [knowledge agent](search-agentic-retrieval-how-to-create.md) and used at query time when an agent or chat bot calls a [retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true) action.
+
+In contrast with a [search index knowledge source](search-knowledge-source-how-to-index.md) that specifies an existing and qualified index, a blob knowledge source specifies an external data source (a blob container) plus models and properties that are used to create an entire enrichment pipeline:
+
++ The generated data source specifies the blob container
++ The generated skillset chunks and vectorizes multimodal content
++ The generated index stores indexed content and meets the criteria for agentic retrieval
++ The generated indexer drives the indexing and enrichment pipeline
+
+The generated index provides the content that's used by a knowledge agent.
+
+Knowledge sources are new in the 2025-08-01-preview release.
+
+## Prerequisites
+
++ Azure Storage with a blob container containing [supported content types](search-howto-indexing-azure-blob-storage.md#supported-document-formats) for text content. For images, the supported content type depends on your chat completion model and whether it can analyze and describe the image file.
+
++ Azure AI Search, basic tier or higher, configured for semantic ranker.
+
++ An embedding model and a chat completion model used for verbalizing images. Depending on the models you specify, the generated skillset can include any of the following skills: [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md), [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md), [Azure AI Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md), [AML skill](cognitive-search-aml-skill.md). Each of these skills has a finite list of supported models. Check the skill documentation for supported models.
+
+To try the examples in this article, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending preview REST API calls to Azure AI Search. There's no portal support at this time.
+
+## Check for existing knowledge sources
+
+A knowledge source is a top-level, reusable object. All knowledge sources must be uniquely named within the knowledge sources collection. It's helpful to know about existing knowledge sources for either reuse or for naming new objects.
+
+The following request lists knowledge sources by name and type.
+
+```http
+# List knowledge sources by name and type
+GET {{search-url}}/knowledgeSources?api-version=2025-08-01-preview&$select=name,kind
+api-key: {{api-key}}
+Content-Type: application/json
+```
+
+You can also return a single knowledge source by name to review its JSON definition.
+
+```http
+### Get a knowledge source definition
+GET {{search-url}}/knowledgeSources/{{knowledge-source-name}}?api-version=2025-08-01-preview
+api-key: {{api-key}}
+Content-Type: application/json
+```
+
+A response for blob knowledge source might look like the following example. 
+
+```json
+{
+  "name": "earth-at-night-blob-ks",
+  "kind": "azureBlob",
+  "description": "This knowledge source pull from a blob storage container containing pages from the Earth at Night PDF.",
+  "encryptionKey": null,
+  "searchIndexParameters": null,
+  "azureBlobParameters": {
+    "connectionString": "<REDACTED>",
+    "folderPath": null,
+    "disableImageVerbalization": null,
+    "identity": null,
+    "embeddingModel": {
+      "name": "demo-blob-embedding-vectorizer",
+      "kind": "azureOpenAI",
+      "azureOpenAIParameters": {
+        "resourceUri": "<REDACTED>",
+        "deploymentId": "text-embedding-ada-002",
+        "apiKey": "<REDACTED>",
+        "modelName": "text-embedding-ada-002",
+        "authIdentity": null
+      },
+      "customWebApiParameters": null,
+      "aiServicesVisionParameters": null,
+      "amlParameters": null
+    },
+    "chatCompletionModel": {
+      "kind": "azureOpenAI",
+      "azureOpenAIParameters": {
+        "resourceUri": "<REDACTED>",
+        "deploymentId": "gpt-4o-mini",
+        "apiKey": "<REDACTED>",
+        "modelName": "gpt-4o-mini",
+        "authIdentity": null
+      }
+    },
+    "ingestionSchedule": null,
+    "createdResources": {
+      "datasource": "earth-at-night-blob-ks-datasource",
+      "indexer": "earth-at-night-blob-ks-indexer",
+      "skillset": "earth-at-night-blob-ks-skillset",
+      "index": "earth-at-night-blob-ks-index"
+    }
+  },
+  "webParameters": null
+}
+```
+
+> [!NOTE]
+> Sensitive information is redacted. The generated resources appear at the end of the response. The `webParameters` property isn't operational in this preview and it's reserved for future use.
+
+## Create a knowledge source
+
+To create a [knowledge source](search-knowledge-source-overview.md), use the 2025-08-01-preview data plane REST API or an Azure SDK preview package that provides equivalent functionality.
+
+A knowledge source can contain exactly one of the following: `searchIndexParameters` *or* `azureBlobParameters`. The `webParameters` property isn't supported in this release. If you specify `azureBlobParameters`, then `searchIndexParameters` must be null.
+
+For `azureBlobParameters`:
+
++ Provide a connection to Azure AI Search
++ Provide a full access connection string for Azure Storage and the container name
++ Provide a text embedding model. This model is used to vectorize text content during indexing and queries.
++ Provide a chat completion model used for describing image content.
++ Provide an encryption key to doubly encrypt sensitive information in this knowledge source and in the generated resources.
+
+Models are referenced in the skillset and as vectorizer for encoding text strings at query time.
+
+A blob knowledge source can include an `ingestionSchedule` that adds scheduling information to an indexer. You can also [add a schedule](search-howto-schedule-indexers.md) later if you want to automate data refresh
+
+1. Use the [Create or Update Knowledge Source](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) preview REST API.
+
+1. Set environment variables at the top of your file.
+
+    ```http
+    @search-url=<YOUR SEARCH SERVICE URL>
+    @api-key=<YOUR SEARCH ADMIN API KEY>
+    @connection-string=<YOUR FULL ACCESS CONNECTION STRING TO AZURE STORAGE>
+    @aoai-endpoint=<YOUR AZURE OPENAI ENDPOINT>
+    @aoai-key=<YOUR AZURE OPENAI API KEY>
+    ```
+
+1. Formulate the request and then **Send**.
+
+    ```http
+    PUT {{search-url}}/knowledgeSources/earth-at-night-blob-ks?api-version=2025-08-01-preview
+    api-key: {{api-key}}
+    Content-Type: application/json
+    
+    {
+      "name": "earth-at-night-blob-ks",
+      "kind": "azureBlob",
+      "description": "This knowledge source pull from a blob storage container containing pages from the Earth at Night PDF.",
+      "encryptionKey": null,
+      "azureBlobParameters": {
+        "connectionString": "{{connection-string}}",
+        "containerName": "nasa-ebook",
+        "folderPath": null,
+        "disableImageVerbalization": null,
+        "identity": null,
+        "embeddingModel": {
+          "kind": "azureOpenAI",
+          "azureOpenAIParameters": {
+            "resourceUri": "{{aoai-endpoint}}",
+            "deploymentId": "text-embedding-3-small",
+            "apiKey": "{{aoai-key}}",
+            "modelName": "text-embedding-3-small",
+            "authIdentity": null
+          },
+          "customWebApiParameters": null,
+          "aiServicesVisionParameters": null,
+          "amlParameters": null
+        },
+        "chatCompletionModel": {
+          "kind": "azureOpenAI",
+          "azureOpenAIParameters": {
+            "resourceUri": "{{aoai-endpoint}}",
+            "deploymentId": "gpt-4o-mini",
+            "apiKey": "{{aoai-key}}",
+            "modelName": "gpt-4o-mini",
+            "authIdentity": null
+          }
+        },
+        "ingestionSchedule": {
+          "interval": "P1D",
+          "startTime": "2025-01-07T19:30:00Z"
+        }
+      }
+    }
+    ```
+
+If you get errors, make sure the embedding model and chat completion models exist at the endpoint you provided.
+
+## Check output
+
+When you create a blob knowledge source, the search service also creates the following objects: an indexer, data source, skillset, and index. Exercise caution when editing these objects because you can break the pipeline if you introduce an error or incompatibility.
+
+The response on knowledge source creation lists the created resources. Objects are created according to a fixed template and naming is based on the knowledge source. You can't change the object names.
+
+We recommend using the Azure portal to validate output creation.
+
+1. Check the indexer for success or failure messages. Connection or quota errors appear here. If the indexer failed, try reset and rerun.
+
+1. Check the index for searchable content. Use Search Explorer to run your queries.
+
+1. Check the skillset to learn more about how your content is chunked and vectorized.
+
+1. Modify the data source if you want to change connection details, such as authentication and authorization. The example uses API keys for simplicity but you can use Microsoft Entra ID authentication and role-based access.
+
+## Assign to a knowledge agent
+
+If you're satisfied with the index, continue to the next step: specify the knowledge source in a [knowledge agent](search-agentic-retrieval-how-to-create.md).
+
+Within the knowledge agent, there are more properties to set on the knowledge source that are specific to query operations.
+
+After the knowledge agent is configured, use the retrieve action to query the knowledge source.
+
+## Delete a knowledge source
+
+If you no longer need the knowledge source, or if you need to rebuild it on the search service, use this request to delete the current object.
+
+```http
+# Delete agent
+DELETE {{search-url}}/knowledgeSources/{{ks-name}}?api-version=2025-08-01-preview
+api-key: {{api-key}}
+```
+
+> [!IMPORTANT]
+> Before you can delete a knowledge source, you must first update the knowledge agent to remove all references to the knowledge source.
+>
+> Deleting a blob knowledge source also deletes the objects it created. The indexer, data source, skillset, and index are automatically deleted when the blob knowledge source is deleted.
+>
+
+## Learn more
+
++ [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
+
++ [Agentic RAG: build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
+
++ [Azure OpenAI Demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Blobナレッジソースの作成に関する新規ドキュメント"
}
```

### Explanation
この修正は、`search-knowledge-source-how-to-blob.md`という新しいドキュメントの追加で、Azure AI Searchに関連する新しい機能を詳細に説明しています。このドキュメントは、Blobナレッジソースの作成に必要な情報を提供し、以下の点に焦点を当てています：

1. **Blobナレッジソースの紹介**: Blobナレッジソースは、Azure AI Searchエージェントパイプラインでのインデクシングとクエリ操作に必要な情報を指定します。これには、データソース、スキルセット、インデクサー、インデックスの作成に必要なモデルとプロパティが含まれます。

2. **前提条件の設定**: Azure Storageを使用して、対応するコンテンツタイプを持つBlobコンテナが存在することや、基本テキストのためのAzure AI Searchの構成が必要であることが記載されています。また、埋め込みモデルやチャット完了モデルが必要であることも明記されています。

3. **ナレッジソースの作成手順**: REST APIを使用してBlobナレッジソースを作成する具体的な手順が示されており、接続文字列やモデルの指定方法などが詳述されています。

4. **APIリクエストの例**: ナレッジソースの取得、リスト、作成、削除のための具体的なAPIリクエスト例が提供されており、利用者が実践的に理解しやすい内容になっています。

5. **エラー処理と出力確認**: Blobナレッジソース作成時に生成されるリソースに関する注意点や、インデクサーやインデックスの成功/失敗メッセージの確認方法が説明されており、トラブルシューティングのための情報が提供されています。

このドキュメントにより、ユーザーはAzure AI Searchを利用してBlobコンテナから効率的にコンテンツをインデックス化し、エージェントによる情報検索を効果的に行うための理解を深めることができます。

## articles/search/search-knowledge-source-how-to-index.md{#item-fb0876}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,138 @@
+---
+title: Create a search index knowledge source
+titleSuffix: Azure AI Search
+description: A search index knowledge source specifies an index used by a knowledge agent for agentic retrieval workloads.
+manager: nitinme
+author: HeidiSteen
+ms.author: heidist
+ms.service: azure-ai-search
+ms.topic: how-to
+ms.date: 08/29/2025
+---
+
+# Create a search index knowledge source
+
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+A *search index knowledge source* specifies a connection to a search index on Azure AI Search that provides searchable content in an agentic retrieval pipeline. It's created independently, and then referenced by a [knowledge agent](search-agentic-retrieval-how-to-create.md) and used at query time when an agent or chat bot calls a [retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true) action.
+
+Knowledge sources are new in the 2025-08-01-preview release.
+
+## Prerequisites
+
+You need a search index containing plain text or vector content, with a semantic configuration. [Review index criteria for agentic retrieval](search-agentic-retrieval-how-to-index.md#criteria-for-agentic-retrieval). The search index must be on the same search service as the knowledge agent.
+
+To try the examples in this article, we recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for sending preview REST API calls to Azure AI Search. There's no portal support at this time.
+
+## Check for existing knowledge sources
+
+A knowledge source is a top-level, reusable object. All knowledge sources must be uniquely named within the knowledge sources collection. It's helpful to know about existing knowledge sources for either reuse or for naming new objects.
+
+Example request: List all knowledge sources on a search service by name and type.
+
+```http
+# List knowledge sources by name and type
+GET {{search-url}}/knowledgeSources?api-version=2025-08-01-preview&$select=name,kind
+api-key: {{api-key}}
+Content-Type: application/json
+```
+
+Example request: Return a single knowledge source by name to review its JSON definition.
+
+```http
+### Get a knowledge source definition
+GET {{search-url}}/knowledgeSources/{{knowledge-source-name}}?api-version=2025-08-01-preview
+api-key: {{api-key}}
+Content-Type: application/json
+```
+
+An example response for a `searchIndex` knowledge source might look like the following JSON. Notice that the knowledge source specifies a single index name and which fields in the index to include in the query.
+
+```json
+{
+
+  "name": "earth-at-night-ks",
+  "kind": "searchIndex",
+  "description": "Earth at night e-book knowledge source",
+  "encryptionKey": null,
+  "searchIndexParameters": {
+    "searchIndexName": "earth_at_night",
+    "sourceDataSelect": "page_chunk,page_number"
+  },
+  "azureBlobParameters": null,
+  "webParameters": null
+}
+```
+
+> [!NOTE]
+> The `webParameters` property isn't operational in this preview and it's reserved for future use.
+
+## Create a knowledge source
+
+To create a [knowledge source](search-knowledge-source-overview.md), use the 2025-08-01-preview data plane REST API or an Azure SDK preview package that provides equivalent functionality.
+
+A knowledge source can contain exactly one of the following: `searchIndexParameters` *or* `azureBlobParameters`. The `webParameters` property isn't supported in this release. If you specify `searchIndexParameters`, then `azureBlobParameters` must be null.
+
+For `searchIndexParameters`:
+
++ Choose an index [designed for agentic retrieval](search-agentic-retrieval-how-to-index.md)
++ Specify any `retrievable` fields that can be used for citations, such as a file name or page number.
+
+1. Use the [Create or Update Knowledge Source](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true) preview REST API.
+
+1. Set environment variables at the top of your file.
+
+    ```http
+    @search-url=<YOUR SEARCH SERVICE URL>
+    @api-key=<YOUR ADMIN API KEY>
+    @ks-name=<YOUR KNOWLEDGE SOURCE NAME>
+    @index-name=<YOUR INDEX NAME>
+    ```
+
+1. Formulate the request and then **Send**.
+
+    ```http
+    POST {{search-url}}/knowledgeSources?api-version=2025-08-01-preview
+    api-key: {{api-key}}
+    Content-Type: application/json
+    
+    {
+        "name" : "{{ks-name}}",
+        "kind" : "searchIndex",
+        "description" : "Earth at night e-book knowledge source",
+        "searchIndexParameters" :{
+          "searchIndexName" : "{{index-name}}",
+          "sourceDataSelect" : "page_chunk,page_number"
+        }
+    }
+    ```
+
+**Key points**:
+
++ `name` must be unique within the knowledge sources collection and follow the [naming guidelines](/rest/api/searchservice/naming-rules) for objects on Azure AI Search.
+
++ `sourceDataSelect` is the list of fields returned if you specify `includeReferenceSourceData` in the knowledge agent definition. These fields are used for the citation view experience and should include fields like a document or file name, page or chapter number, and so forth.
+
+## Assign to a knowledge agent
+
+If you're satisfied with the index, continue to the next step: specifying the knowledge source in a [knowledge agent](search-agentic-retrieval-how-to-create.md).
+
+Within the knowledge agent, there are more properties to set on the knowledge source that are specific to query operations.
+
+## Delete a knowledge source
+
+If you no longer need the knowledge source, or if you need to rebuild it on the search service, use this request to delete the current object.
+
+```http
+# Delete agent
+DELETE {{search-url}}/knowledgeSources/{{ks-name}}?api-version=2025-08-01-preview
+api-key: {{api-key}}
+```
+
+## Learn more
+
++ [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
+
++ [Agentic RAG: build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
+
++ [Azure OpenAI Demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "検索インデックスナレッジソースの作成に関する新規ドキュメント"
}
```

### Explanation
この修正は、`search-knowledge-source-how-to-index.md`という新しいドキュメントの追加で、Azure AI Searchでの検索インデックスナレッジソースの作成方法についての情報を提供します。以下の主要なポイントが含まれています：

1. **検索インデックスナレッジソースの定義**: このドキュメントでは、検索インデックスナレッジソースが、エージェントによる検索可能なコンテンツを提供するために、Azure AI Search上の検索インデックスとの接続を指定するものであることが説明されています。

2. **前提条件のリスト**: 検索インデックスには、通常のテキストまたはベクトルコンテンツが含まれていること、またセマンティック設定が必要である旨が明記されています。ナレッジエージェントと同じ検索サービス内に存在しなければならないことも重要です。

3. **既存のナレッジソースの確認**: 既存のナレッジソースをリスト化し、そのJSON定義を取得する方法についてのAPIリクエストの例が提供されています。

4. **ナレッジソースの作成手順**: REST APIを通じてナレッジソースを作成するための具体的な手順が示されており、必要なフィールドを含むリクエスト構造が詳述されています。特に、一意の名前付けや引用のためのリトリーバブルなフィールドを指定する方法が強調されています。

5. **ナレッジエージェントへの割り当てと削除**: ナレッジソースをナレッジエージェントに指定する手順や、不要になった場合の削除手続きについても説明されています。

6. **追加情報へのリンク**: エージェントリトリーバルに関する一般的な情報や、関連するデモへのリンクも提供されており、ユーザーの理解を深めるためのリソースが充実しています。

この新規ドキュメントにより、Azure AI Searchのユーザーは、検索インデックスを利用した効率的なナレッジソースの作成と管理について、より深く理解することができます。

## articles/search/search-knowledge-source-overview.md{#item-1969d3}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,117 @@
+---
+title: Create a knowledge source
+titleSuffix: Azure AI Search
+description: Learn how to create a knowledge source for agentic retrieval workloads in Azure AI Search.
+manager: nitinme
+author: HeidiSteen
+ms.author: heidist
+ms.service: azure-ai-search
+ms.topic: how-to
+ms.date: 08/29/2025
+---
+
+# Create a knowledge source
+
+A knowledge source wraps a search index with extra properties for agentic retrieval. It's a required definition in a knowledge agent. We provide guidance on how to create specific knowledge sources, but generally, you can:
+
++ Create multiple knowledge sources as top-level resources on your search service.
+
++ Reference one or more knowledge sources in a knowledge agent. In an agentic retrieval pipeline, it's possible to query against multiple knowledge sources in single request. Subqueries are generated for each knowledge sources. Top results are returned in the retrieval response.
+
+Make sure you have at least one knowledge source before creating a knowledge agent. The full specification of a knowledge agent is in the [REST API reference](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true). 
+
+## Key points about a knowledge source
+
++ Creation path: first create knowledge source, then create knowledge agents. Deletion path: update or delete knowledge agents, delete knowledge sources last.
+
++ A knowledge source, its index, and the knowledge agent must all exist on the same search service.
+
++ Each knowledge source points to exactly one index, and that index must [meet the criteria for agentic retrieval](search-agentic-retrieval-how-to-index.md).
+
++ For each knowledge source, the knowledge agent provides extra properties for query execution. [KnowledgeSourceReference](/rest/api/searchservice/knowledge-agents/create-or-update#knowledgesourcereference?view=rest-searchservice-2025-08-01-preview&preserve-view=true) properties affect query planning. [KnowledgeAgentOutputConfiguration](/rest/api/searchservice/knowledge-agents/create-or-update#knowledgeagentoutputconfiguration?view=rest-searchservice-2025-08-01-preview&preserve-view=true) properties affect query output.
+
+## Supported knowledge sources
+
+Here are the knowledge sources you can create in this preview:
+
++ [Search index knowledge source (an existing index)](search-knowledge-source-how-to-index.md)
++ [Blob knowledge source](search-knowledge-source-how-to-blob.md)
+
+A platform-specific knowledge source like the blob knowledge source includes specifications for generating an entire indexing pipeline that provides all extraction, enrichment and transformations over blob content, and a viable index. You can modify the pipeline and rerun the indexer, but you can't rename the objects.
+
+> [!NOTE]
+> `WebKnowledgeSource` (also referred to as `WebParameters` in REST APIs) isn't currently available in the 2025-08-01-preview.
+
+## Control knowledge source usage
+
+Properties on the knowledge agent determine whether and how the knowledge source is used. The [KnowledgeSourceReference](/rest/api/searchservice/knowledge-agents/create-or-update#knowledgesourcereference?view=rest-searchservice-2025-08-01-preview&preserve-view=true) array specifies the knowledge sources available to the knowledge agent.
+
+### Use multiple knowledge sources simultaneously
+
+When you have multiple knowledge sources, set the following properties to bias query planning to a specific knowledge source.
+
++ Setting `alwaysQuerySource` forces query planning to always include the knowledge source.
++ Setting `retrievalInstructions` provides guidance that includes or excludes a knowledge source. 
+
+Retrieval instructions are sent as a prompt to the large language model (LLM) used for query planning. This prompt is helpful when you have multiple knowledge sources and want to provide guidance on when to use each one. For example, if you have separate indexes for product information, job postings, and technical support, the retrieval instructions might say "use the jobs index only if the question is about a job application."
+
+The `alwaysQuerySource` property overrides `retrievalInstructions`. You should set `alwaysQuerySource` to false when providing retrieval instructions.
+
+### Attempt fast path processing
+
+Fast path is opportunistic query processing that approaches the millisecond query performance of regular search. If you enable it, the search engine attempts fast path under the following conditions:
+
++ `attemptFastPath` is set to true in `knowledgeSourceReferences`.
+
++ The query input is a single message that's fewer than 512 characters.
+
++ The query targets are the knowledge sources specified in the agent that have `alwaysQuerySource` set to true.
+
+The small query, which executes in parallel on all compliant knowledge sources listed in the knowledge agent, returns a result if its scored 1.9 or higher. The highest scoring result is returned in the response. If no results satisfy this criteria, fast path is abandoned and query execution resumes with query planning and the usual agentic retrieval pipeline.
+
+Under fast path, the response omits query planning information (`type": "modelQueryPlanning"`) and "activitySource" is set to 0 for each reference citation.
+
+Under fast path, `retrievalInstructions` are ignored. In general, `alwaysQuerySource` overrides `retrievalInstructions`.
+
+To achieve the fastest possible response times, follow these best practices:
+
++ Set `modality` to `answerSynthesis` to get a response framed as an LLM-formulated answer. It takes a few extra seconds, but it improves the quality of the response and saves time overall if the answer is usable without further LLM processing.
+
++ Retain `includeActivity` set to true (default setting) for insights about query execution and elapsed time.
+
++ Retain `includeReferences` set to true (default setting) for details about each individually scored result.
+
++ Set `includeReferenceSourceData` to false if you don't need the verbatim content from the index. Omitting this information simplifies the response and makes it more readable.
+
+## Delete a knowledge source
+
+Before you can delete a knowledge source, you must delete or update any knowledge agent that references it. The associated index is a standalone object in Azure AI Search and doesn't need to be deleted or updated in tandem with the knowledge source, but no references to the knowledge source can exist if you want to delete it.
+
+If you try to delete a knowledge source that's in use, the action fails and a list of affected knowledge agents is returned.
+
+1. Get the knowledge agent definition to confirm knowledge source references.
+
+    ```http
+    ### Get the knowledge agent
+    GET {{search-endpoint}}/agents/hotels-index-ka?api-version=2025-08-01-preview
+    api-key: {{api-key}}
+    Content-Type: application/json
+    ```
+
+1. Either update the knowledge agent by removing the knowledge source, or delete the knowledge agent. This example shows deletion.
+
+    ```http
+    ### Delete knowledge agent
+    DELETE {{search-endpoint}}/agents/hotels-index-ka?api-version=2025-08-01-preview
+    api-key: {{api-key}}
+    Content-Type: application/json
+    ```
+
+1. Delete the knowledge source.
+
+    ```http
+    ### Delete a knowledge source definition
+    GET {{search-endpoint}}/knowledgeSources/hotels-index-ks?api-version=2025-08-01-preview
+    api-key: {{api-key}}
+    Content-Type: application/json
+    ```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ナレッジソース概要に関する新規ドキュメント"
}
```

### Explanation
この修正は、`search-knowledge-source-overview.md`という新しいドキュメントの追加に関するもので、Azure AI Searchにおけるナレッジソースの作成方法とその利用について詳細に説明しています。以下の主要なポイントが含まれています：

1. **ナレッジソースの定義**: ナレッジソースは、エージェントによる検索インデックスをラップするものであり、エージェントのリトリーバルに必要不可欠な要素です。ユーザーは、複数のナレッジソースを作成し、それらをエージェント内で参照することが可能です。

2. **ナレッジソースの反映に関するガイドライン**: ナレッジエージェントがリトリーバルプロセスを最適化するために、ナレッジソースの数に応じたクエリ計画の調整方法や、同時に複数のナレッジソースからのクエリが可能であることが強調されています。また、ナレッジソースの作成後、エージェント作成を行うべきことに言及されています。

3. **ナレッジソースの管理**: ナレッジソースの作成および削除のプロセス、特にエージェントが参照するナレッジソースの削除前に行うべき手順について説明されています。この管理には、エージェントの定義や参照の確認が含まれます。

4. **高速パス処理の活用**: 高速パス処理の条件や、最適な応答時間を実現するためのベストプラクティスが提供されており、特に迅速なクエリパフォーマンスを追求する開発者に向けた情報が含まれています。

5. **サポートされるナレッジソース**: このプレビューで作成可能なナレッジソースの種類が列挙され、具体的な構成要素についても説明されています。Blobナレッジソースのようなプラットフォーム特有のナレッジソースに関する詳細も含まれています。

この新しいドキュメントにより、Azure AI Searchの利用者はナレッジソースの構造とその管理方法についての理解を深め、より効果的にエージェントによる検索機能を実装することができます。

## articles/search/search-query-access-control-rbac-enforcement.md{#item-d24df7}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how query-time ACL and RBAC enforcement ensures secure document retrieval in Azure AI Search for indexes containing permission filters from Azure Data Lake Storage (ADLS) Gen2 data sources.  
 ms.service: azure-ai-search  
 ms.topic: conceptual  
-ms.date: 07/16/2025  
+ms.date: 08/27/2025  
 author: mattgotteiner  
 ms.author: magottei 
 ---  
@@ -25,7 +25,7 @@ This article explains how to set up queries that use permission metadata to filt
 
 - For ADLS Gen2 data sources, you must have configured Access Control Lists (ACLs) and/or Azure role-based access control (RBAC) roles at the container level. For blob data sources, your have role assignments on the container. You can use a [built-in indexer](search-indexer-access-control-lists-and-role-based-access.md) or [Push APIs](search-index-access-control-lists-and-rbac-push-api.md) to index permission metadata in your index.
 
-- Use the 2025-05-01-preview REST API or a preview package of an Azure SDK to query the index. This API version supports internal queries that filter out unauthorized results.
+- The latest preview REST API (2025-08-01-preview) or a preview package of an Azure SDK to query the index. This API version supports internal queries that filter out unauthorized results.
 
 ## How query-time enforcement works
 
@@ -64,7 +64,7 @@ The security filter efficiently matches the userIds, groupIds, and rbacScope fro
 Here's an example of a query request from [sample code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-ACL). The query token is passed in the request header. The query token is the personal access token of a user or a group identity behind the request.
 
 ```http
-POST  {{endpoint}}/indexes/stateparks/docs/search?api-version=2025-05-01-preview
+POST  {{endpoint}}/indexes/stateparks/docs/search?api-version=2025-08-01-preview
 Authorization: Bearer {{query-token}}
 x-ms-query-source-authorization: {{query-token}}
 Content-Type: application/json
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アクセス制御とRBAC施行に関する日付とAPIバージョンの更新"
}
```

### Explanation
この修正は、`search-query-access-control-rbac-enforcement.md`ドキュメントの軽微な変更に関するもので、以下の点が更新されています：

1. **日付の更新**: ドキュメントの日付が「2025-07-16」から「2025-08-27」に変更されました。この変更は、コンテンツの新しさを反映するものです。

2. **APIバージョンの更新**: 使用するREST APIのバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更されました。この最新版APIは、許可されていない結果をフィルタリングする内部クエリをサポートしています。この更新は、ユーザーに最新の機能を提供するためのものです。

3. **クエリリクエスト例の更新**: クエリリクエストの例で指定されているAPIバージョンが変更され、最新のAPIバージョンに合わせて更新されています。

この修正により、ユーザーは最新のAPIを使用してアクセス制御とRBACの施行に関する正確な情報を得ることができ、Azure AI Searchにおける安全な文書の取得方法についての理解を深めることができます。

## articles/search/search-relevance-overview.md{#item-cb0e09}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 07/23/2025
+ms.date: 08/27/2025
 ms.update-cycle: 180-days
 ---
 
@@ -84,7 +84,7 @@ The following diagram illustrates how the ranking algorithms work together.
 A query that generates the previous workflow might look like the following example. This hybrid semantic query is scored using RRF (based on L1 scores for text and vectors), and semantic ranking.
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2025-05-01-preview
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2025-08-01-preview
 
 {
   "search": "cloud formation over water",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索関連性概要の更新日付とAPIバージョンの変更"
}
```

### Explanation
この修正は、`search-relevance-overview.md`ドキュメントの小規模な変更に関するもので、以下の点が主に更新されています：

1. **日付の更新**: ドキュメントの日付が「2025-07-23」から「2025-08-27」に変更されました。この変更は、ドキュメントが最新の情報を反映していることを示しています。

2. **APIバージョンの更新**: 使用するREST APIのバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更されました。この新しいAPIバージョンでは、検索リクエストの処理に関する機能が更新または改善されている可能性があります。

3. **クエリリクエスト例の更新**: APIバージョンが変更されたことに伴い、クエリリクエストの例も最新のAPIに適合するように修正されました。

これにより、ユーザーはより新しいAPIを利用して検索関連性を扱うための最新の情報を得ることができ、Azure AI Searchのリクエスト処理についての理解を深めることができます。

## articles/search/semantic-code-migration.md{#item-ad1ba7}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 05/29/2025
+ms.date: 08/27/2025
 ms.update-cycle: 365-days
 ---
 
@@ -45,6 +45,7 @@ Check your code for the REST API version or SDK package version to confirm which
 | preview | [2024-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-11-01-preview&preserve-view=true) | Adds query rewrite. The `queryLanguage` property is now required if you use [query rewrite (preview)](semantic-how-to-query-rewrite.md).  |
 | preview | [2025-03-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-03-01-preview&preserve-view=true) | Adds opt-in to prerelease versions of semantic models. |
 | preview | [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) | No API updates in this preview, but semantic ranking now has [better integration with scoring profiles](semantic-how-to-enable-scoring-profiles.md). |
+| preview | [2025-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) | No change |
 
 ## Change logs for Azure SDKs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックコード移行の更新日付とAPIバージョンの追加"
}
```

### Explanation
この修正は、`semantic-code-migration.md`ドキュメントに関する軽微な変更で、以下の点が主に更新されています：

1. **日付の更新**: ドキュメントの日付が「2025-05-29」から「2025-08-27」に変更されました。この日付変更は、ドキュメントが最新情報を反映していることを示しています。

2. **新しいAPIバージョンの追加**: 新しいAPIバージョン「2025-08-01-preview」が追加されました。このバージョンではAPIの変更はありませんが、セマンティックランキングの統合が改善されていることを示しています。

3. **変更内容の整理**: APIバージョンごとの機能内容が整理され、最新のAPIバージョンに関する情報が追加されました。

この更新により、ユーザーは最新のAPIを用いたセマンティックコード移行についての正確な情報を得ることができ、Azure AI Searchの機能を効果的に活用する助けとなります。

## articles/search/semantic-how-to-enable-scoring-profiles.md{#item-e8d524}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: how-to
-ms.date: 07/22/2025
+ms.date: 08/27/2025
 ---
 
 # Use scoring profiles with semantic ranker in Azure AI Search
@@ -25,7 +25,7 @@ To ensure the scoring profile provides the determining score, the semantic ranke
 
 - [Azure AI Search](search-create-service-portal.md), Basic pricing tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
-- [REST API version `2025-05-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) or a preview Azure SDK package that provides the new APIs.
+- The [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) or a preview Azure SDK package that provides the new APIs.
 
 - A search index with a semantic configuration that specifies `"rankingOrder": "boostedReRankerScore"` and a scoring profile that specifies [functions](index-add-scoring-profiles.md#use-functions).
 
@@ -58,10 +58,10 @@ In this scenario, a scoring profile is used twice.
 
 ## Enable scoring profiles in semantic configuration
 
-To enable scoring profiles with semantic ranking, use preview API version `2025-05-01-preview` to update an index by setting the `rankingOrder` property of its semantic configuration. Use the PUT method to update the index with your revisions. No index rebuild is required.
+To enable scoring profiles with semantic ranking, use the latest preview REST API (2025-08-01-preview) to update an index by setting the `rankingOrder` property of its semantic configuration. Use the PUT method to update the index with your revisions. No index rebuild is required.
 
 ```json
-PUT https://{service-name}.search.windows.com/indexes/{index-name}?api-version=2025-05-01-Preview
+PUT https://{service-name}.search.windows.com/indexes/{index-name}?api-version=2025-08-01-preview
 {
   "semantic": {
     "configurations": [
@@ -79,7 +79,7 @@ PUT https://{service-name}.search.windows.com/indexes/{index-name}?api-version=2
 To opt out of sorting by semantic reranker boosted score, set the `rankingOrder` field to `reRankerScore` value in the semantic configuration.
 
 ```json
-PUT https://{service-name}.search.windows.com/indexes/{index-name}?api-version=2025-05-01-Preview
+PUT https://{service-name}.search.windows.com/indexes/{index-name}?api-version=2025-08-01-preview
 {
   "semantic": {
     "configurations": [
@@ -99,7 +99,7 @@ Even if you opt out of sorting by `@search.rerankerBoostedScore`, the `boostedRe
 Start with a [semantic query](semantic-how-to-query-request.md) that specifies a scoring profile. The query uses the new preview REST API, and it targets a search index that has `rankingOrder` set to `boostedReRankerScore`.
 
 ```json
-POST https://{service-name}.search.windows.com/indexes/{index-name}/docs/search?api-version=2025-05-01-Preview
+POST https://{service-name}.search.windows.com/indexes/{index-name}/docs/search?api-version=2025-08-01-preview
 {
   "search": "my query to be boosted",
   "scoringProfile": "myScoringProfile",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリングプロファイルの有効化に関するドキュメントの日付とAPIバージョンの更新"
}
```

### Explanation
この修正は、`semantic-how-to-enable-scoring-profiles.md`ドキュメントに対する軽微な変更を反映しており、以下の内容が主に更新されています：

1. **日付の更新**: ドキュメントの日付が「2025-07-22」から「2025-08-27」に変更され、最新の情報を示すようになりました。

2. **APIバージョンの変更**: 使用するREST APIのバージョンが「2025-05-01-preview」から「2025-08-01-preview」に変更されました。これにより、最新のAPIを利用することが求められる点が強調されています。

3. **スニペットの更新**: APIバージョンに関連する具体的なリクエスト例が新しいバージョンに合わせて修正されました。これにより、ユーザーは最新のAPIを使用したスコアリングプロファイルの有効化方法を理解しやすくなっています。

この更新により、ユーザーはAzure AI Searchの最新機能を活用し、スコアリングプロファイルの設定に関する正確な情報を得ることができるようになります。

## articles/search/speller-how-to-add.md{#item-9b4502}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 05/29/2025
+ms.date: 08/27/2025
 ms.update-cycle: 365-days
 ---
 
@@ -32,7 +32,7 @@ Use a search client that supports preview APIs on the query request. You can use
 
 | Client library | Versions |
 |----------|----------|
-| REST API | Versions 2020-06-30-Preview and later. We recommend the latest preview API. [2025-05-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&preserve-view=true)|
+| REST API | Versions 2020-06-30-Preview and later. We recommend the latest preview API: [2025-08-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-08-01-preview&preserve-view=true)|
 | Azure SDK for .NET | [version 11.7.0-beta.4](https://www.nuget.org/packages/Azure.Search.Documents/11.7.0-beta.4) | 
 | Azure SDK for Java |  [version 11.8.0-beta.7](https://central.sonatype.com/artifact/com.azure/azure-search-documents/11.8.0-beta.7) |
 | Azure SDK for JavaScript | [version 11.3.0-beta.8](https://www.npmjs.com/package/@azure/search-documents/v/11.3.0-beta.8) |
@@ -43,7 +43,7 @@ Use a search client that supports preview APIs on the query request. You can use
 The following example uses the built-in hotels-sample index to demonstrate spell correction on a simple text query. Without spell correction, the query returns zero results. With correction, the query returns one result for Johnson's family-oriented resort.
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-08-01-preview
 {
     "search": "famly acitvites",
     "speller": "lexicon",
@@ -64,7 +64,7 @@ Spelling correction occurs on individual query terms that undergo text analysis,
 This example uses fielded search over the Category field, with full Lucene syntax, and a misspelled query term. By including speller, the typo in "Suiite" is corrected and the query succeeds.
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-05-01-preview
+POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-08-01-preview
 {
     "search": "Category:(Resort and Spa) OR Category:Suiite",
     "queryType": "full",
@@ -80,7 +80,7 @@ POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/
 This query, with typos in every term except one, undergoes spelling corrections to return relevant results. To learn more, see [Configure semantic ranker](semantic-how-to-query-request.md).
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-05-01-preview    
+POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-08-01-preview    
 {
     "search": "hisotoric hotell wiht great restrant nad wiifi",
     "queryType": "semantic",
@@ -94,7 +94,7 @@ POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/
 
 ## Supported languages
 
-Valid values for `queryLanguage` can be found in the following table, copied from the list of [supported languages (REST API reference)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-05-01-preview&tabs=HTTP#querylanguage&preserve-view=true).
+Valid values for `queryLanguage` can be found in the following table, copied from the list of [supported languages (REST API reference)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-08-01-preview&tabs=HTTP#querylanguage&preserve-view=true).
 
 | Language | queryLanguage |
 |----------|---------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スペラ―の追加に関するドキュメントの日付とAPIバージョンの更新"
}
```

### Explanation
この修正は、`speller-how-to-add.md`ドキュメントに対する軽微な変更で、以下の主なポイントが更新されています：

1. **日付の更新**: ドキュメントの日付が「2025-05-29」から「2025-08-27」に変更され、最新の日付が反映されました。

2. **APIバージョンの変更**: 使用するREST APIのバージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新されました。この変更により、最新の機能と改善が利用できることが示されています。

3. **クエリ例の更新**: APIバージョンの変更に伴い、複数のHTTPリクエストにおけるAPIバージョンが最新の「2025-08-01-preview」に修正され、正しいリクエストが行えるようになっています。また、スペル補正に関連する具体的なクエリ例も適切に更新されています。

この更新により、ユーザーはAzure AI Searchのスペラ―機能を活用するための正確で最新な情報を得ることができるようになります。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ items:
       href: search-what-is-an-index.md
     - name: Vector index
       href: vector-store.md
-    - name: Knowledge store
+    - name: Knowledge store in Azure Storage
       href: knowledge-store-concept-intro.md
     - name: Indexers
       href: search-indexer-overview.md
@@ -394,14 +394,26 @@ items:
     items:
     - name: Agentic retrieval
       items:
-      - name: Design an index for agentic retrieval
+      - name: Create an index for agentic retrieval
         href: search-agentic-retrieval-how-to-index.md
+      - name: Create a knowledge source
+        items:
+        - name: Knowledge sources
+          href: search-knowledge-source-overview.md
+        - name: Azure blobs
+          href: search-knowledge-source-how-to-blob.md
+        - name: Search indexes
+          href: search-knowledge-source-how-to-index.md
       - name: Create a knowledge agent
         href: search-agentic-retrieval-how-to-create.md
-      - name: Retrieve data using a knowledge agent
+      - name: Configure answer synthesis for an agent
+        href: search-agentic-retrieval-how-to-synthesize.md
+      - name: Retrieve data using an agent
         href: search-agentic-retrieval-how-to-retrieve.md
       - name: Build a retrieval pipeline
         href: search-agentic-retrieval-how-to-pipeline.md
+      - name: Migrate agentic retrieval code
+        href: search-agentic-retrieval-how-to-migrate.md
     - name: Vector search
       items:
       - name: Query vectors
@@ -455,7 +467,7 @@ items:
           href: search-query-fuzzy.md
     - name: Hybrid search
       href: hybrid-search-how-to-query.md
-  - name: Ranking and relevance
+  - name: Ranking
     items:
     - name: BM25 ranking
       items:
@@ -589,8 +601,6 @@ items:
       href: search-performance-tips.md
   - name: Knowledge store
     items:
-    - name: Knowledge store overview
-      href: knowledge-store-concept-intro.md
     - name: Knowledge store projections overview
       href: knowledge-store-projection-overview.md
     - name: Create using REST
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCの項目名の変更と新しいリンクの追加"
}
```

### Explanation
この修正は、`toc.yml`ファイルに対する軽微な変更で、以下の主なポイントが反映されています：

1. **項目名の変更**: 
   - 「Knowledge store」の名称が「Knowledge store in Azure Storage」に変更され、具体的なコンテキストが追加されました。
   - 「Design an index for agentic retrieval」が「Create an index for agentic retrieval」に変更され、アクションを明確に示す措置が取られています。
   - 「Retrieve data using a knowledge agent」が「Configure answer synthesis for an agent」に変更され、エージェントの機能に関連する具体的なタスクが強調されています。
   
2. **新しい項目の追加**: 
   - 「Create a knowledge source」という新しいカテゴリーが追加され、その下に「Knowledge sources」、「Azure blobs」、「Search indexes」という具体的なリンクが追加されています。
   - 「Migrate agentic retrieval code」という新しいリンクが追加され、エージェントのコード移行に関する情報が提供されています。

3. **項目の削除**: 
   - 「Knowledge store overview」という項目が削除され、より洗練されたTOCの構造が提供されています。

これらの更新により、ユーザーはAzure AI Searchにおけるさまざまな機能やトピックに関する情報を簡単に見つけることができるようになり、ナビゲーションが向上しました。

## articles/search/tutorial-adls-gen2-indexer-acls.md{#item-6881a0}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to index Access Control Lists (ACLs) and Azure Role-Based
 ms.service: azure-ai-search  
 ms.update-cycle: 180-days
 ms.topic: tutorial  
-ms.date: 05/20/2025
+ms.date: 08/27/2025
 author: wlifuture
 ms.author: wli
 ---  
@@ -27,7 +27,7 @@ In this tutorial, you learn how to:
 > + Create and run an indexer to ingest permission information into an index from a data source
 > + Search the index you just created
 
-Use a REST client to complete this tutorial and the [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) REST API. There's no currently no support for ACL indexing in the Azure portal.
+Use a REST client to complete this tutorial and the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true). Currently, there's no support for ACL indexing in the Azure portal.
 
 ## Prerequisites
 
@@ -79,7 +79,7 @@ As a best practice, use [`Group` sets](search-indexer-access-control-lists-and-r
 
 [Create an index](search-how-to-create-search-index.md#create-an-index) that contains fields for content and [permission metadata](search-indexer-access-control-lists-and-role-based-access.md#create-permission-fields-in-the-index).
 
-Be sure to use [2025-05-01-preview data plane REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) or a prerelease Azure SDK that provides equivalent functionality. The permission filter properties are only available in the preview APIs.
+Be sure to use the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) or a prerelease Azure SDK that provides equivalent functionality. The permission filter properties are only available in the preview APIs.
 
 For demo purposes, the permission field has `retrievable` enabled so that you can check the values from the index. In a production environment, you should disable `retrievable` to avoid leaking sensitive information.
 
@@ -190,7 +190,7 @@ Now that documents are loaded, you can issue queries against them by using [Docu
 The URI is extended to include a query input, which is specified by using the `/docs/search` operator. The query token is passed in the request header. For more information, see [Query-Time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md).
 
 ```http
-POST  {{endpoint}}/indexes/stateparks/docs/search?api-version=2025-05-01-preview
+POST  {{endpoint}}/indexes/stateparks/docs/search?api-version=2025-08-01-preview
 Authorization: Bearer {{search-token}}
 x-ms-query-source-authorization: {{search-token}}
 Content-Type: application/json
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ACLインデキサーに関するチュートリアルの日付とAPIバージョンの更新"
}
```

### Explanation
この修正は、`tutorial-adls-gen2-indexer-acls.md`ファイルに対する軽微な変更で、主に以下のポイントが更新されています：

1. **日付の更新**: 
   - ドキュメントの日付が「2025-05-20」から「2025-08-27」に変更され、最新の日付が反映されています。

2. **APIバージョンの変更**: 
   - APIのバージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新され、最新の機能や改善を示しています。この変更は、チュートリアルに記載されたリソースリンクやコードサンプルにも適用されています。

3. **テキストの修正**: 
   - チュートリアル内の説明文がわずかに変更され、「Currently, there's no support for ACL indexing in the Azure portal.」という表現が追加され、明確さが向上しています。
   - RESTクライアントを使用する際に従うべき最新のガイダンスが提供されており、パーミッションフィルタープロパティがプレビューAPIでのみ利用可能であることを強調しています。

これらの修正によって、ユーザーがAccess Control Lists (ACLs)をインデックスし、最新のAPIを使用する際の明瞭性が向上し、最新の情報に基づいた操作が促進されます。

## articles/search/tutorial-document-extraction-image-verbalization.md{#item-398a90}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
 ms.topic: tutorial
-ms.date: 07/30/2025
+ms.date: 08/27/2025
 
 ---
 
@@ -137,7 +137,7 @@ To get the Azure AI Search endpoint and API key:
 
 ```http
 ### Create a data source
-POST {{searchUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/datasources?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -166,7 +166,7 @@ Send the request. The response should look like:
 HTTP/1.1 201 Created
 Transfer-Encoding: chunked
 Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
-Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-05-01-preview -Preview
+Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-08-01-preview -Preview
 Server: Microsoft-IIS/10.0
 Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
 Preference-Applied: odata.include-annotations="*"
@@ -204,7 +204,7 @@ For nested JSON, the index fields must be identical to the source fields. Curren
 
 ```http
 ### Create an index
-POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -356,7 +356,7 @@ The skillset also performs actions specific to images. It uses the GenAI Prompt
 
 ```http
 ### Create a skillset
-POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/skillsets?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -624,7 +624,7 @@ Key points:
 
 ```http
 ### Create and run an indexer
-POST {{searchUrl}}/indexers?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -656,7 +656,7 @@ You can start searching as soon as the first document is loaded.
 
 ```http
 ### Query the index
-POST {{searchUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
   
@@ -692,7 +692,7 @@ Connection: close
   },
   "value": [
   ],
-  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-05-01-preview "
+  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-08-01-preview "
 }
 ```
 
@@ -707,7 +707,7 @@ Here are some examples of other queries:
 
 ```http
 ### Query for only images
-POST {{searchUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
   
@@ -720,7 +720,7 @@ POST {{searchUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?
 
 ```http
 ### Query for text or images with content related to energy, returning the id, parent document, and text (extracted text for text chunks and verbalized image text for images), and the content path where the image is saved in the knowledge store (only populated for images)
-POST {{searchUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
   
@@ -737,19 +737,19 @@ Indexers can be reset to clear the high-water mark, which allows a full rerun. T
 
 ```http
 ### Reset the indexer
-POST {{searchUrl}}/indexers/doc-extraction-image-verbalization-indexer/reset?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers/doc-extraction-image-verbalization-indexer/reset?api-version=2025-08-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Run the indexer
-POST {{searchUrl}}/indexers/doc-extraction-image-verbalization-indexer/run?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers/doc-extraction-image-verbalization-indexer/run?api-version=2025-08-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Check indexer status 
-GET {{searchUrl}}/indexers/doc-extraction-image-verbalization-indexer/status?api-version=2025-05-01-preview   HTTP/1.1
+GET {{searchUrl}}/indexers/doc-extraction-image-verbalization-indexer/status?api-version=2025-08-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書抽出画像の可視化に関するチュートリアルの日付とAPIバージョンの更新"
}
```

### Explanation
この修正は、`tutorial-document-extraction-image-verbalization.md`ファイルに対する軽微な変更で、主に以下のポイントが更新されています：

1. **日付の更新**: 
   - ドキュメントの日付が「2025年7月30日」から「2025年8月27日」に変更され、最新の更新が反映されています。

2. **APIバージョンの変更**: 
   - 多くのエンドポイントのAPIバージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新されています。具体的には、データソース、インデックス、スキルセット、インデクサーの作成やクエリに関するリクエストの部分が変更されています。

3. **テキストの修正**: 
   - 「Location」や「@odata.nextLink」などのレスポンスに関する説明が更新され、新しいAPIバージョンに対応した記載が行われています。

これらの更新により、ユーザーがAzure AIの文書抽出および画像の可視化機能を利用する際に、構造と内容が最新のAPIに沿った形で改良されており、より正確で実用的な情報が提供されます。

## articles/search/tutorial-document-extraction-multimodal-embeddings.md{#item-a3db59}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
 ms.topic: tutorial
-ms.date: 07/30/2025
+ms.date: 08/27/2025
 
 ---
 
@@ -130,7 +130,7 @@ To get the Azure AI Search endpoint and API key:
 [Create Data Source (REST)](/rest/api/searchservice/data-sources/create) creates a data source connection that specifies what data to index.
 
 ```http
-POST {{searchUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/datasources?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -159,7 +159,7 @@ Send the request. The response should look like:
 HTTP/1.1 201 Created
 Transfer-Encoding: chunked
 Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
-Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-05-01-preview -Preview
+Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-08-01-preview -Preview
 Server: Microsoft-IIS/10.0
 Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
 Preference-Applied: odata.include-annotations="*"
@@ -197,7 +197,7 @@ For nested JSON, the index fields must be identical to the source fields. Curren
 
 ```http
 ### Create an index
-POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -346,7 +346,7 @@ Key points:
 
 ```http
 ### Create a skillset
-POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/skillsets?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -576,7 +576,7 @@ Key points:
 
 ```http
 ### Create and run an indexer
-POST {{searchUrl}}/indexers?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -609,7 +609,7 @@ You can start searching as soon as the first document is loaded.
 
 ```http
 ### Query the index
-POST {{searchUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
   
@@ -645,7 +645,7 @@ Connection: close
   },
   "value": [
   ],
-  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview "
+  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-08-01-preview "
 }
 ```
 100 documents are returned in the response.
@@ -657,7 +657,7 @@ For filters, you can also use Logical operators (and, or, not) and comparison op
 
 ```http
 ### Query for only images
-POST {{searchUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
   
@@ -670,7 +670,7 @@ POST {{searchUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search
 
 ```http
 ### Query for text or images with content related to energy, returning the id, parent document, and text (only populated for text chunks), and the content path where the image is saved in the knowledge store (only populated for images)
-POST {{searchUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
   
@@ -688,19 +688,19 @@ Indexers can be reset to clear the high-water mark, which allows a full rerun. T
 
 ```http
 ### Reset the indexer
-POST {{searchUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/reset?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/reset?api-version=2025-08-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Run the indexer
-POST {{searchUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/run?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/run?api-version=2025-08-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Check indexer status 
-GET {{searchUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/status?api-version=2025-05-01-preview   HTTP/1.1
+GET {{searchUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/status?api-version=2025-08-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダル埋め込みの文書抽出に関するチュートリアルの日付とAPIバージョンの更新"
}
```

### Explanation
この修正は、`tutorial-document-extraction-multimodal-embeddings.md`ファイルに対する軽微な変更で、主に以下のポイントが更新されています：

1. **日付の更新**: 
   - ドキュメントの日付が「2025年7月30日」から「2025年8月27日」に変更され、最新の更新が反映されています。

2. **APIバージョンの変更**: 
   - 多くのHTTPリクエストにおいて、APIのバージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新されています。これには、データソースの作成、インデックスの作成、スキルセットの作成、インデクサーの実行、クエリの実行などのリクエストが含まれます。

3. **テキストの修正**: 
   - 更新されたAPIバージョンがレスポンスの中で使用され、特に`Location`や`@odata.nextLink`などのパラメーター変更が強調されています。

これらの変更により、ユーザーがAzure AIを利用したマルチモーダル埋め込みの文書抽出に関する最新の情報を得ることができ、正確なAPIの使用方法が明記されています。

## articles/search/tutorial-document-layout-image-verbalization.md{#item-f5de57}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
 ms.topic: tutorial
-ms.date: 07/30/2025
+ms.date: 08/27/2025
 
 ---
 
@@ -155,7 +155,7 @@ To get the Azure AI Search endpoint and API key:
 
 ```http
 ### Create a data source using system-assigned managed identities
-POST {{searchUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/datasources?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -185,7 +185,7 @@ Send the request. The response should look like:
 HTTP/1.1 201 Created
 Transfer-Encoding: chunked
 Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
-Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-05-01-preview -Preview
+Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-08-01-preview -Preview
 Server: Microsoft-IIS/10.0
 Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
 Preference-Applied: odata.include-annotations="*"
@@ -223,7 +223,7 @@ For nested JSON, the index fields must be identical to the source fields. Curren
 
 ```http
 ### Create an index
-POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -376,7 +376,7 @@ The skillset also performs actions specific to images. It uses the GenAI Prompt
 
 ```http
 ### Create a skillset
-POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/skillsets?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -611,7 +611,7 @@ Key points:
 
 ```http
 ### Create and run an indexer
-POST {{searchUrl}}/indexers?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -643,7 +643,7 @@ You can start searching as soon as the first document is loaded.
 
 ```http
 ### Query the index
-POST {{searchUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
   
@@ -665,7 +665,7 @@ Send the request. This is an unspecified full-text search query that returns all
   },
   "value": [
   ],
-  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-05-01-preview "
+  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-08-01-preview "
 }
 ```
 100 documents are returned in the response.
@@ -677,7 +677,7 @@ For filters, you can also use Logical operators (and, or, not) and comparison op
 
 ```http
 ### Query for only images
-POST {{searchUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
   
@@ -690,7 +690,7 @@ POST {{searchUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/searc
 
 ```http
 ### Query for text or images with content related to energy, returning the id, parent document, and text (only populated for text chunks), and the content path where the image is saved in the knowledge store (only populated for images)
-POST {{searchUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
   
@@ -707,19 +707,19 @@ Indexers can be reset to clear execution history, which allows a full rerun. The
 
 ```http
 ### Reset the indexer
-POST {{searchUrl}}/indexers/doc-intelligence-image-verbalization-indexer/reset?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers/doc-intelligence-image-verbalization-indexer/reset?api-version=2025-08-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Run the indexer
-POST {{searchUrl}}/indexers/doc-intelligence-image-verbalization-indexer/run?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers/doc-intelligence-image-verbalization-indexer/run?api-version=2025-08-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Check indexer status 
-GET {{searchUrl}}/indexers/doc-intelligence-image-verbalization-indexer/status?api-version=2025-05-01-preview   HTTP/1.1
+GET {{searchUrl}}/indexers/doc-intelligence-image-verbalization-indexer/status?api-version=2025-08-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書レイアウト画像の可視化に関するチュートリアルの日付とAPIバージョンの更新"
}
```

### Explanation
この修正は、`tutorial-document-layout-image-verbalization.md`ファイルに対する軽微な変更で、主に以下のポイントが更新されています：

1. **日付の更新**: 
   - ドキュメントの日付が「2025年7月30日」から「2025年8月27日」に改訂され、最新の情報が反映されています。

2. **APIバージョンの変更**: 
   - 多くのAPIリクエストにおいて、バージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新されております。これには、データソース作成、インデックス作成、スキルセット作成、インデクサー起動、クエリ実行などが含まれています。

3. **テキストの修正**: 
   - レスポンスに含まれる`Location`や`@odata.nextLink`などのURLも最新のAPIバージョンに合わせて修正されています。

これらの更新により、Azure AIの文書レイアウト画像の可視化に関連する深い知識をユーザーに提供し、最新のAPIに基づいた適切な使用例が明示されていることが強調されています。

## articles/search/tutorial-document-layout-multimodal-embeddings.md{#item-f67371}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
 ms.topic: tutorial
-ms.date: 07/30/2025
+ms.date: 08/27/2025
 
 ---
 
@@ -130,7 +130,7 @@ To get the Azure AI Search endpoint and API key:
 
 ```http
 ### Create a data source using system-assigned managed identities
-POST {{searchUrl}}/datasources?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/datasources?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -159,7 +159,7 @@ Send the request. The response should look like:
 HTTP/1.1 201 Created
 Transfer-Encoding: chunked
 Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
-Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-05-01-preview -Preview
+Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-08-01-preview -Preview
 Server: Microsoft-IIS/10.0
 Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
 Preference-Applied: odata.include-annotations="*"
@@ -197,7 +197,7 @@ For nested JSON, the index fields must be identical to the source fields. Curren
 
 ```http
 ### Create an index
-POST {{searchUrl}}/indexes?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -346,7 +346,7 @@ Key points:
 
 ```http
 ### Create a skillset
-POST {{searchUrl}}/skillsets?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/skillsets?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -537,7 +537,7 @@ Key points:
 
 ```http
 ### Create and run an indexer
-POST {{searchUrl}}/indexers?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
 
@@ -569,7 +569,7 @@ You can start searching as soon as the first document is loaded.
 
 ```http
 ### Query the index
-POST {{searchUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
   
@@ -591,7 +591,7 @@ Send the request. This is an unspecified full-text search query that returns all
   },
   "value": [
   ],
-  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview "
+  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-08-01-preview "
 }
 ```
 100 documents are returned in the response.
@@ -603,7 +603,7 @@ For filters, you can also use Logical operators (and, or, not) and comparison op
 
 ```http
 ### Query for only images
-POST {{searchUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
   
@@ -616,7 +616,7 @@ POST {{searchUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/sear
 
 ```http
 ### Query for text or images with content related to energy, returning the id, parent document, and text (only populated for text chunks), and the content path where the image is saved in the knowledge store (only populated for images)
-POST {{searchUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-08-01-preview   HTTP/1.1
   Content-Type: application/json
   api-key: {{searchApiKey}}
   
@@ -633,19 +633,19 @@ Indexers can be reset to clear execution history, which allows a full rerun. The
 
 ```http
 ### Reset the indexer
-POST {{searchUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/reset?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/reset?api-version=2025-08-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Run the indexer
-POST {{searchUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/run?api-version=2025-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/run?api-version=2025-08-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 ```
 
 ```http
 ### Check indexer status 
-GET {{searchUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/status?api-version=2025-05-01-preview   HTTP/1.1
+GET {{searchUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/status?api-version=2025-08-01-preview   HTTP/1.1
   api-key: {{searchApiKey}}
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダル埋め込みの文書レイアウトに関するチュートリアルの日付とAPIバージョンの更新"
}
```

### Explanation
この修正は、`tutorial-document-layout-multimodal-embeddings.md`ファイルに対して実施されており、以下の主な変更が含まれています：

1. **日付の更新**:
   - ドキュメントの日付が「2025年7月30日」から「2025年8月27日」に変更され、最新の情報を反映しています。

2. **APIバージョンの変更**:
   - 異なるAPIリクエストにおいて使用されるAPIバージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新されました。この変更は、データソースの作成、インデックスの作成、スキルセットの作成、インデクサーの実行、クエリの実行の各リクエストに適用されています。

3. **テキスト内容の修正**:
   - レスポンスの中に含まれる`Location`や`@odata.nextLink`などのURLも新しいAPIバージョンに合わせて更新されています。

これにより、ユーザーはAzure AIを活用したマルチモーダル埋め込みの文書レイアウトに関する最新の情報を確認でき、最新のAPIを正確に使用するためのガイダンスが提供されています。

## articles/search/vector-search-filters.md{#item-f47c2b}

<details>
<summary>Diff</summary>
````diff
@@ -1,142 +1,119 @@
 ---
 title: Vector Query Filters
 titleSuffix: Azure AI Search
-description: Learn how to add filter expressions to vector queries in Azure AI Search. Configure prefiltering and postfiltering modes to optimize query performance and improve search results.
+description: Learn how to add filter expressions to vector queries in Azure AI Search. Configure prefilter, postfilter, and strict postfilter (preview) modes to optimize query performance and improve search results.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
   + ignite-2023
 ms.topic: how-to
-ms.date: 07/11/2025
+ms.date: 08/28/2025
 ---
 
 # Add a filter to a vector query in Azure AI Search
 
-In Azure AI Search, you can define a vector query request that includes a [filter expression](search-filters.md) to add inclusion or exclusion criteria to your queries. This article explains how to:
+> [!NOTE]
+> `strictPostFilter` is currently in public preview. This preview is provided without a service-level agreement and isn't recommended for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+>
+> `prefilter` and `postfilter` are generally available in the [latest stable REST API version](/rest/api/searchservice/search-service-api-versions).
 
-> [!div class="checklist"]
-> + [Define a `filter` expression](#define-a-filter)
-> + [Set the `vectorFilterMode` for pre-query or post-query filtering](#set-the-vectorfiltermode)
+In Azure AI Search, you can use a [filter expression](search-filters.md) to add inclusion or exclusion criteria to a vector query. You can also specify a filtering mode that applies the filter:
+
++ Before query execution, known as *prefiltering*.
++ After query execution, known as *postfiltering*.
++ After the global top-`k` results are identified, known as *strict postfiltering* (preview).
 
 This article uses REST for illustration. For code samples in other languages and end-to-end solutions that include vector queries, see the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) GitHub repository.
 
 You can also use [Search Explorer](search-get-started-portal-import-vectors.md#check-results) in the Azure portal to query vector content. If you use the JSON view, you can add filters and specify the filter mode.
 
-## How filtering works in a vector query
-
-Filters apply to `filterable` *nonvector* fields, either string or numeric, to include or exclude search documents based on filter criteria. Although a vector field isn't filterable itself, you can add filters to nonvector fields in the same index to include or exclude documents that also contain vector fields you're searching on.
+## How filtering works in vector queries
 
-Filters are applied before or after query execution based on the `vectorFilterMode` parameter.
+Filters apply to `filterable` *nonvector* fields, either string or numeric, to include or exclude search documents based on filter criteria. Although vector fields aren't filterable, you can use filters on nonvector fields in the same index to include or exclude documents that contain vector fields you're searching on.
 
-## Define a filter
+If your index lacks suitable text or numeric fields, check for document metadata that might be useful in filtering, such as `LastModified` or `CreatedBy` properties.
 
-Filters determine the scope of a vector query. They're set on and iterate over nonvector string and numeric fields marked as `filterable` in the index. The purpose of a filter determines *what* the vector query executes over: the entire searchable space (prefiltering) or the contents of a search result (postfiltering).
+The `vectorFilterMode` parameter controls when the filter is applied in the vector search process, with `k` setting the maximum number of nearest neighbors to return. Depending on the filter mode and how selective your filter is, fewer than `k` results might be returned.
 
-If you don't have source fields with text or numeric values, check for document metadata, such as `LastModified` or `CreatedBy` properties, that might be useful in a metadata filter.
+## Define a filter
 
-### [**2024-07-01**](#tab/filter-2024-07-01)
+Filters determine the scope of vector queries and are defined using [Documents - Search Post (REST API)](/rest/api/searchservice/documents/search-post). Unless you want to use a preview feature, use the latest stable version of the [Search Service REST APIs](/rest/api/searchservice/search-service-api-versions) to formulate the request.
 
-[**2024-07-01**](/rest/api/searchservice/search-service-api-versions#2024-07-01) is the stable version of this API. This version has:
+This REST API provides:
 
-+ `vectorFilterMode` for prefilter (default) or postfilter filtering modes.
 + `filter` for the criteria.
-
-In the following example, the vector is a representation of this query string: "what Azure services support full text search". The query targets the `contentVector` field. The actual vector has 1,536 embeddings, so it's trimmed for readability.
-
-The filter criteria are applied to a filterable text field (`category` in this example) before the search engine executes the vector query.
++ `vectorFilterMode` for pre-query or post-query filtering. For supported modes, see the [next section](#set-the-filter-mode).
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-07-01
+POST https://{search-endpoint}/indexes/{index-name}/docs/search?api-version={api-version}
 Content-Type: application/json
-api-key: {{admin-api-key}}
-{
-    "count": true,
-    "select": "title, content, category",
-    "filter": "category eq 'Databases'",
-    "vectorFilterMode": "preFilter",
-    "vectorQueries": [
-        {
-            "kind": "vector",
-            "vector": [
-                -0.009154141,
-                0.018708462,
-                . . . 
-                -0.02178128,
-                -0.00086512347
-            ],
-            "exhaustive": true,
-            "fields": "contentVector",
-            "k": 5
-        }
-    ]
-}
+api-key: {admin-api-key}
+    
+    {
+        "count": true,
+        "select": "title, content, category",
+        "filter": "category eq 'Databases'",
+        "vectorFilterMode": "preFilter",
+        "vectorQueries": [
+            {
+                "kind": "vector",
+                "vector": [
+                    -0.009154141,
+                    0.018708462,
+                    . . . // Trimmed for readability
+                    -0.02178128,
+                    -0.00086512347
+                ],
+                "exhaustive": true,
+                "fields": "contentVector",
+                "k": 5
+            }
+        ]
+    }
 ```
 
-### [**2024-05-01-preview**](#tab/filter-2024-05-01-preview)
+In this example, the vector embedding targets the `contentVector` field, and the filter criteria apply to `category`, a filterable text field. Because the `preFilter` mode is used, the filter is applied before the search engine runs the query, so only documents in the `Databases` category are considered during the vector search.
 
-[**2024-05-01-preview**](/rest/api/searchservice/search-service-api-versions#2024-05-01-preview) introduces filter options. This version adds:
+## Set the filter mode
 
-+ `vectorFilterMode` for prefilter (default) or postfilter filtering modes.
-+ `filter` for the criteria.
+The `vectorFilterMode` parameter determines when and how the filter is applied relative to vector query execution. There are three modes:
 
-In the following example, the vector is a representation of this query string: "what Azure services support full text search". The query targets the `contentVector` field. The actual vector has 1,536 embeddings, so it's trimmed for readability.
++ `preFilter` (default)
++ `postFilter`
++ `strictPostFilter` (preview)
 
-The filter criteria are applied to a filterable text field (`category` in this example) before the search engine executes the vector query.
+### [preFilter](#tab/prefilter-mode)
 
-```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-05-01-preview
-Content-Type: application/json
-api-key: {{admin-api-key}}
-{
-    "count": true,
-    "select": "title, content, category",
-    "filter": "category eq 'Databases'",
-    "vectorFilterMode": "preFilter",
-    "vectorQueries": [
-        {
-            "kind": "vector",
-            "vector": [
-                -0.009154141,
-                0.018708462,
-                . . . 
-                -0.02178128,
-                -0.00086512347
-            ],
-            "exhaustive": true,
-            "fields": "contentVector",
-            "k": 5
-        }
-    ]
-}
-```
-
----
+Prefiltering applies filters before query execution, which reduces the candidate set for the vector search algorithm. The top-`k` results are then selected from this filtered set.
 
-## Set the vectorFilterMode
+In a vector query, `preFilter` is the default mode because it favors recall and quality over latency.
 
-The `vectorFilterMode` query parameter determines whether the filter is applied before or after vector query execution.
+:::image type="content" source="media/vector-search-filters/pre-filter.svg" alt-text="Diagram of prefilters." border="true" lightbox="media/vector-search-filters/pre-filter.png":::
 
-### [Prefilter mode](#tab/prefilter-mode)
+### [postFilter](#tab/postfilter-mode)
 
-Prefiltering applies filters before query execution, reducing the search surface area over which the vector search algorithm looks for similar content.
+Postfiltering applies filters after query execution, which narrows the search results. This mode processes results within each shard and then merges the filtered results from all shards to produce the top-`k` results. As a result, you might receive documents that match the filter but aren't among the global top-`k` results.
 
-In a vector query, `preFilter` is the default.
+To use this option in a vector query, use `"vectorFilterMode": "postFilter"`.
 
-:::image type="content" source="media/vector-search-filters/pre-filter.svg" alt-text="Diagram of prefilters." border="true" lightbox="media/vector-search-filters/pre-filter.png":::
+:::image type="content" source="media/vector-search-filters/post-filter.svg" alt-text="Diagram of post-filters." border="true" lightbox="media/vector-search-filters/post-filter.png":::
 
-### [Postfilter mode](#tab/postfilter-mode)
+### [strictPostFilter (preview)](#tab/strictpostfilter-mode)
 
-Postfiltering applies filters after query execution, narrowing the search results.
+Strict postfiltering applies filters after identifying the global top-`k` results. This mode guarantees that the filtered results are always a subset of the unfiltered top `k`.
 
-In a vector query, use `postFilter` for this task.
+With strict postfiltering, highly selective filters or small `k` values can return zero results (even if matches exist) because only documents that match the filter within the global top `k` are returned. Don't use this mode if missing relevant results could have serious consequences, such as in healthcare or patent searches.
 
-:::image type="content" source="media/vector-search-filters/post-filter.svg" alt-text="Diagram of post-filters." border="true" lightbox="media/vector-search-filters/post-filter.png":::
+To use this option in a vector query, use `"vectorFilterMode": "strictPostFilter"` with the latest preview version of the [Search Service REST APIs](/rest/api/searchservice/search-service-api-versions).
 
 ---
 
-### Benchmark testing of vector filter modes
+### Benchmark testing of prefiltering and postfiltering
+
+> [!IMPORTANT]
+> This section applies to prefiltering and postfiltering, not strict postfiltering.
 
 To understand the conditions under which one filter mode performs better than the other, we ran a series of tests to evaluate query outcomes over small, medium, and large indexes.
 
@@ -231,3 +208,9 @@ The vertical axis represents the relative performance of prefiltering compared t
 + A value of `1.0` means prefiltering and post filtering are equivalent.
 
 The horizontal axis represents the filtering rate, or the percentage of candidate documents after applying the filter. For example, a rate of `1.00%` means the filter criteria selected one percent of the search corpus.
+
+## Related content
+
++ [Vector search in Azure AI Search](vector-search-overview.md)
++ [Create a vector index](vector-search-how-to-create-index.md)
++ [Create a vector query](vector-search-how-to-query.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索フィルターに関するチュートリアルの更新"
}
```

### Explanation
この修正は、`vector-search-filters.md`ファイルに対して行われたもので、以下の主な変更が含まれています：

1. **説明内容の拡充**:
   - ベクトルクエリにフィルター式を追加する方法に関する説明が追加され、`prefilter`、`postfilter`、およびプレビュー機能である`strict postfilter`モードが具体的に説明されています。

2. **日付の更新**:
   - ドキュメントの日付が「2025年7月11日」から「2025年8月28日」に更新され、最新の情報が反映されています。

3. **フィルターモードの具体化**:
   - フィルターモードに関する詳細が追加され、各モードの動作と利点が明確に説明されています。また、`strict postfilter`については、その使用に関する注意点も強調されています。

4. **使用例の更新**:
   - APIリクエストの構文が最新の形式に更新され、具体的なコードサンプルも追加されて、実装時の参考になるようにされています。

5. **ベンチマークテストの追加**:
   - フィルターモードの性能に関するベンチマークテスト結果が含まれ、どの条件下でフィルターモードのパフォーマンスが最適かを示す情報が提供されています。

これらの変更により、ユーザーはAzure AI検索におけるベクトル検索フィルターの使い方をより深く理解でき、より効果的な検索結果を得るための手法が解説されています。

## articles/search/vector-search-how-to-create-index.md{#item-97c769}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 07/07/2025
+ms.date: 08/28/2025
 ---
 
 # Create a vector index
@@ -326,7 +326,7 @@ Vector fields are characterized by [their data type](/rest/api/searchservice/sup
    + `stored` can be true or false. It determines whether an extra copy of vectors is stored for retrieval. For more information, see [Reduce vector size](vector-search-how-to-storage-options.md).
    + `filterable`, `facetable`, and `sortable` must be false.
 
-1. Add filterable nonvector fields to the collection, such as `title` with `filterable` set to true, if you want to invoke [prefiltering or postfiltering](vector-search-filters.md) on the [vector query](vector-search-how-to-query.md).
+1. Add filterable nonvector fields to the collection, such as `title` with `filterable` set to true, if you want to invoke [prefiltering, postfiltering, or strict postfiltering (preview)](vector-search-filters.md) on the [vector query](vector-search-how-to-query.md).
 
 1. Add other fields that define the substance and structure of the textual content you're indexing. At a minimum, you need a document key.
 
@@ -436,7 +436,7 @@ Vector fields are characterized by [their data type](/rest/api/searchservice/sup
    + `stored` is a new boolean property that applies to vector fields only. True stores a copy of vectors returned in search results. False discards that copy during indexing. You can search on vectors, but you can't return vectors in results.
    + `filterable`, `facetable`, and `sortable` must be false.
 
-1. Add filterable nonvector fields to the collection, such as "title" with `filterable` set to true, if you want to invoke [prefiltering or postfiltering](vector-search-filters.md) on the [vector query](vector-search-how-to-query.md).
+1. Add filterable nonvector fields to the collection, such as "title" with `filterable` set to true, if you want to invoke [prefiltering, postfiltering, or strict postfiltering (preview)](vector-search-filters.md) on the [vector query](vector-search-how-to-query.md).
 
 1. Add other fields that define the substance and structure of the textual content you're indexing. At a minimum, you need a document key.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルインデックスの作成方法に関するチュートリアルの更新"
}
```

### Explanation
この修正は、`vector-search-how-to-create-index.md`ファイルに対して行われたもので、主に以下の変更が含まれています：

1. **日付の更新**:
   - 文書の日付が「2025年7月7日」から「2025年8月28日」に更新され、情報が最新のものになっています。

2. **フィルタリングオプションの拡充**:
   - ベクトルクエリにおいて使用できるフィルタリングオプションの説明が拡充され、`prefiltering`、`postfiltering`に加え、プレビュー機能である`strict postfiltering`についても言及されるようになりました。これにより、ユーザーはより多様なフィルタリング戦略を理解し、適用できるようになります。

3. **具体的な手順の更新**:
   - フィルタリングの手順に関する具体的な内容が更新され、集めるべき非ベクトルフィールドに対する注記が強化されています。

これにより、ユーザーはAzure AI検索において、より効果的にベクトルインデックスを作成するための最新かつ詳細なガイダンスを得ることができるようになります。

## articles/search/vector-search-multi-vector-fields.md{#item-9aa482}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: gimondra
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: conceptual
-ms.date: 05/07/2025
+ms.date: 08/27/2025
 ---
 
 # Multi-vector field support in Azure AI Search
@@ -98,7 +98,7 @@ Here's a sample document that illustrates how you might use multi-vector fields
   "title": "Non-Existent Movie",
   "description": "A fictional movie for demonstration purposes.",
   "descriptionEmbedding": [1, 2, 3],
-  "releaseDate": "2025-05-01",
+  "releaseDate": "2025-08-01",
   "scenes": [
     {
       "embedding": [4, 5, 6],
@@ -161,10 +161,10 @@ When a collection of complex types is included in the `$select` parameter, only
 
 When a document includes multiple embedded vectors, such as text and image embeddings in different subfields, the system uses the highest vector score across all elements to rank the document.
 
-To debug how each vector contributed, use the `innerHits` debug mode (available in API version 2025-05-01-preview).
+To debug how each vector contributed, use the `innerHits` debug mode (available in the latest preview REST API).
 
 ```json
-POST /indexes/my-index/docs/search?api-version=2025-05-01-preview
+POST /indexes/my-index/docs/search?api-version=2025-08-01-preview
 {
   "vectorQueries": [
     {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチベクトルフィールドのサポートに関するドキュメントの更新"
}
```

### Explanation
この修正は、`vector-search-multi-vector-fields.md`ファイルに対して行われたもので、主に以下の変更が含まれています：

1. **日付の更新**:
   - ドキュメントの日付が「2025年5月7日」から「2025年8月27日」に更新され、情報が最新のものになっています。

2. **リリース日付の更新**:
   - サンプルドキュメント内のリリース日付が「2025年5月1日」から「2025年8月1日」に変更され、例としての内容が最新のものに適合するようになりました。

3. **APIバージョンの表記変更**:
   - `innerHits`デバッグモードに関する説明において、APIバージョンの表記が「2025-05-01-preview」から「最新のプレビューレストAPI」に変更され、常に最新のAPIを参照する形になりました。

4. **検索リクエストのAPIバージョン更新**:
   - 検索リクエストのサンプル内でもAPIバージョンが「2025-05-01-preview」から「2025-08-01-preview」に更新され、ユーザーが最新のAPIを使用できるようにしています。

これらの変更により、ユーザーはAzure AI検索におけるマルチベクトルフィールドの使用方法に関する最新かつ正確な情報を得ることができるようになります。

## articles/search/vector-store.md{#item-db9b8c}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 08/01/2025
+ms.date: 08/28/2025
 ms.update-cycle: 365-days
 ---
 
@@ -92,7 +92,7 @@ Vector indexes require more than just vector fields. For example, all indexes mu
 
 Other fields, such as the `content` field, provide the human-readable equivalent of the `content_vector` field. If you're using language models exclusively for response formulation, you can omit nonvector content fields, but solutions that push search results directly to client apps should have nonvector content.
 
-Metadata fields are useful for filters, especially if they include origin information about the source document. Although you can't filter directly on a vector field, you can set prefilter or postfilter modes to filter before or after vector query execution.
+Metadata fields are useful for filters, especially if they include origin information about the source document. Although you can't filter directly on a vector field, you can set prefilter, postfilter, or strict postfilter (preview) modes to filter before or after vector query execution.
 
 ### Schema generated by the Import and vectorize data wizard
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルストレージに関するドキュメントの更新"
}
```

### Explanation
この修正は、`vector-store.md`ファイルに対して行われたもので、主に以下の変更が含まれています：

1. **日付の更新**:
   - 文書の日付が「2025年8月1日」から「2025年8月28日」に更新され、最新の情報が反映されています。

2. **フィルターモードの拡充**:
   - メタデータフィールドに関する説明が更新され、`prefilter`、`postfilter`に加え、プレビュー機能である`strict postfilter`モードが追加されています。この変更により、ユーザーはベクトルクエリの実行前後にフィルタリングを行うための選択肢が増え、より柔軟にデータを扱うことができるようになります。

これにより、Azure AI検索におけるベクトルストレージに関する理解が深まり、ユーザーは最新の機能を効果的に活用できるようになります。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Announcements of new and enhanced features, including a service ren
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 08/18/2025
+ms.date: 09/01/2025
 ms.service: azure-ai-search
 ms.topic: overview
 ms.custom:
@@ -20,6 +20,20 @@ Learn about the latest updates to Azure AI Search functionality, docs, and sampl
 > [!NOTE]
 > Preview features are announced here, but we also maintain a [preview features list](search-api-preview.md) so you can find them in one place.
 
+## August 2025
+
+| Item | Type | Description |
+|-----------------------------|------|--------------|
+| [Search Service 2025-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) | REST | New preview REST API version providing programmatic access to the data plane operations described in this table. |
+| [Knowledge agents (preview)](search-agentic-retrieval-how-to-create.md) | Agentic search | Architectural changes to the knowledge agent definition, which now requires one or more `knowledgeSources` instead of `targetIndexes` and deprecates `defaultMaxDocsForReranker`. New `retrievalInstructions` and `outputConfiguration` properties provide greater control over query planning and execution. For help with breaking changes, see [Migrate your agentic retrieval code](search-agentic-retrieval-how-to-migrate.md). |
+| [Knowledge sources (preview)](search-knowledge-source-overview.md) | Agentic search | New REST APIs for creating and managing knowledge sources, which represent content that knowledge agents use to ground and answer queries. In this preview, you can create knowledge sources for [search indexes](search-knowledge-source-how-to-index.md) and [Azure blobs](search-knowledge-source-how-to-blob.md).  |
+| [Answer synthesis (preview)](search-agentic-retrieval-how-to-synthesize.md) | Agentic search | New `answerSynthesis` modality for knowledge agents. When specified, an LLM generates a natural-language answer as an embedded step in the retrieval pipeline. This differs from the default `extractiveData` modality, which returns raw search results for downstream processing. |
+| ["Fast path" for knowledge agents (preview)](search-knowledge-source-overview.md#attempt-fast-path-processing) | Agentic search | New `attemptFastPath` boolean for knowledge agents. Enables a shorter processing time if queries are concise and the initial response is sufficiently relevant. |
+| [Retrieval instructions (preview)](search-agentic-retrieval-how-to-create.md) | Agentic search | New `retrievalInstructions` property for knowledge agents guides query planning in an agentic retrieval workflow. For example, you can specify criteria for including or excluding specific knowledge sources.  |
+| [Improved indexer runtime tracking information (preview)](search-howto-run-reset-indexers.md#check-indexer-runtime-quota-for-s3-hd-search-services) | Indexers | Applies to Standard 3 High Density (S3 HD) services only. [Get Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics?view=rest-searchservice-2025-08-01-preview&preserve-view=true) response now provides cumulative indexer processing information for the entire service. [Get Status - Indexers](/rest/api/searchservice/get-service-statistics/get-status?view=rest-searchservice-2025-08-01-preview&preserve-view=true) provides the same information, but for a specific indexer. |
+| [Strict postfiltering for vector queries (preview)](vector-search-filters.md) | Vector search | New `strictPostFilter` mode for the `vectorFilterMode` parameter. When specified, filters are applied after the global top-`k` vector results are identified, ensuring that returned documents are a subset of the unfiltered results. |
+| [Increased maximum dimensions for vector fields](search-limits-quotas-capacity.md#index-limits) | Vector search | The maximum dimensions per vector field are now `4096`. This update applies to all stable and preview REST API versions that support vectors and doesn't introduce breaking changes. |
+
 ## July 2025
 
 | Item | Type | Description |
@@ -41,7 +55,7 @@ Learn about the latest updates to Azure AI Search functionality, docs, and sampl
 | [Document-level access control (preview)](search-document-level-access-overview.md) | Security | Flow document-level permissions from blobs in Azure Data Lake Storage (ADLS) Gen2 to searchable documents in an index. Queries can now filter results based on user identity for selected data sources. |
 | [Multimodal search (preview)](multimodal-search-overview.md) | Indexing, Query | Ingest, understand, and retrieve documents that contain text and images, enabling you to perform searches that combine various modalities, such as querying with text to find information embedded in relevant complex images. See [Quickstart: Search for multimodal content](search-get-started-portal-image-search.md) for portal wizard support and [Azure AI Search Multimodal RAG Demo](https://github.com/Azure-Samples/azure-ai-search-multimodal-sample) for a code-first approach. |
 | [GenAI prompt skill (preview)](cognitive-search-skill-genai-prompt.md) | Skills | A new skill that connects to a large language model (LLM) for information, using a prompt you provide. With this skill, you can populate a searchable field using content from an LLM. A primary use case for this skill is *image verbalization*, using an LLM to describe images and send the description to a searchable field in your index. |
-| [Document Layout skill (preview)](cognitive-search-skill-document-intelligence-layout.md)| Skills | New parameters are available for this skill if you use the 2025-05-01-preview API version. New parameters support image offset metadata that improves the image search experience. |
+| [Document Layout skill (preview)](cognitive-search-skill-document-intelligence-layout.md)| Skills | New parameters are available for this skill if you use the 2025-05-01-preview API version or later. New parameters support image offset metadata that improves the image search experience. |
 | Import and vectorize data wizard enhancements | Portal | This wizard provides two paths for creating and populating vector indexes: [Retrieval Augmented Generation (RAG)](search-get-started-portal-import-vectors.md) and [Multimodal RAG](search-get-started-portal-image-search.md). Logic apps integration is through the RAG path. |
 | [Index "description" support (preview)](search-howto-reindex.md#add-an-index-description-preview) | REST | The latest preview API adds a description to an index. Consider a Model Context Protocol (MCP) server that must pick the correct index at run time. The decision can be  based on the description rather than on the index name alone. The description must be human readable and under four thousand characters.|
 | [2025-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) | REST | New data plane preview REST API version providing programmatic access to the preview features announced in this release. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新機能に関するアップデートの追加"
}
```

### Explanation
この修正は、`whats-new.md`ファイルに対して行われたもので、以下の重要な変更が含まれています：

1. **日付の更新**:
   - ドキュメントの日付が「2025年8月18日」から「2025年9月1日」に更新され、最新の情報が反映されています。

2. **新機能の追加**:
   - 2025年8月のセクションが新しく追加され、新機能や改善点がリストとしてまとめられています。具体的には、以下のような新しいプレビュー機能が紹介されています：
     - 新しいREST APIバージョン（2025-08-01-preview）
     - 知識エージェントに関するアーキテクチャの変更
     - 新しいREST APIによる知識ソースの作成と管理
     - 回答合成モダリティの導入
     - ベクトルクエリに対する厳密なポストフィルタリングモードの追加
     - ベクトルフィールドの最大次元数の増加

3. **過去の機能の更新**:
   - 2025年7月のセクションにおいて、いくつかの新しいパラメーターが追加されたことも記載されています。その中には、ドキュメントレイアウトスキルの新しいパラメーターが含まれており、特定のAPIバージョンに基づく条件について詳しく説明されています。

これらの変更により、Azure AI Searchの最新機能に関する情報が一元化され、ユーザーはこれからの機能や改善点を容易に把握できるようになります。


