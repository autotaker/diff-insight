---
date: '2026-09-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b3cb2f2...MicrosoftDocs:8e2ab63
summary: この報告書はAPIバージョンの更新に関する様々なドキュメントの変更を扱っています。主要な変更点として、新しいAPIバージョン「2026-08-01-preview」がプロジェクト全体に実装され、多くのドキュメントが更新されたことが挙げられます。この更新により、プライベートネットワークのサポートや新しい知識ソース機能など、Azureの各種サービスの利便性が向上しました。また、過去のAPIバージョンとの互換性に注意が必要な点や、最新の手順や通知が反映されたことで、文書の整合性が強化されています。ユーザーにとっては、これにより最新の機能を活用できる重要な情報源となり、安全で効率的なアプリケーション開発が促進されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b3cb2f2...MicrosoftDocs:8e2ab63){target="_blank"}

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新に関する様々なドキュメントの変更"
}
```

# Highlights

## New features
- 新しいAPIバージョン`2026-08-01-preview`がプロジェクト全体に実装され、多くのドキュメントで利用可能な新機能が増強されました。
- 特にプライベートネットワークのサポートや新しい知識ソースの機能が追加され、Azureの様々なサービスをより効果的に利用できるようになりました。

## Breaking changes
- 特にAPIバージョンの更新は過去のバージョンとの互換性に関わる場合があるため、適切な調整が必要です。

## Other updates
- 各セクションにおける詳細な手順、例、通知が最新のAPIバージョンに応じて更新され、ドキュメントの整合性が強化されました。

# Insights

このコード変更における最も重要なポイントの一つは、広範なAPIバージョンの更新です。これにより、ユーザーは最新の機能と改善点を活用することが可能になり、さまざまなドキュメントで最新の仕様が反映されています。

具体的な更新としては、Azure AI Searchにおけるエージェント知識ソースや、Blobストレージ、SQLなど多岐にわたるサービスに関するドキュメントが最新化され、新機能を効果的に使用するための情報が豊富に提供されています。特にプライベートネットワークの設定や、クロステナントの暗号化など、セキュリティを重視した機能が多く強調されています。

加えて、APIへのアクセスを制御するための新しいプレビュー機能や、ベストプラクティスの変更点が明記され、技術文書がより実用的かつ具体的な内容となっています。

これらの変更はユーザーにとって、最新のAzure環境に対応するための必須ガイドラインを提供するものであり、サービスの互換性を維持しつつ、新たな技術的要求にも対応するための重要な役割を担っています。最新の情報に基づいて、効率的で安全なアプリケーションの開発が可能になることでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-azure-sql.md](#item-89aa4d) | minor update | エージェント知識ソースの Azure SQL に関する更新 | modified | 60 | 33 | 93 | 
| [agentic-knowledge-source-how-to-blob.md](#item-ac6c8a) | minor update | エージェント知識ソースの Azure Blob に関する更新 | modified | 78 | 55 | 133 | 
| [agentic-knowledge-source-how-to-fabric-data-agent.md](#item-900ecc) | minor update | ファブリックデータエージェント知識ソースの更新 | modified | 25 | 19 | 44 | 
| [agentic-knowledge-source-how-to-fabric-ontology.md](#item-1f2bb6) | minor update | ファブリック・オントロジー知識ソースの更新 | modified | 24 | 18 | 42 | 
| [agentic-knowledge-source-how-to-file.md](#item-88f720) | minor update | ファイル知識ソースに関する更新 | modified | 572 | 66 | 638 | 
| [agentic-knowledge-source-how-to-mcp-server.md](#item-9a2e92) | minor update | MCPサーバー知識ソースの更新 | modified | 62 | 38 | 100 | 
| [agentic-knowledge-source-how-to-onelake.md](#item-ec7a80) | minor update | OneLake知識ソースの更新 | modified | 63 | 55 | 118 | 
| [agentic-knowledge-source-how-to-search-index.md](#item-09d366) | minor update | 検索インデックス知識ソースの更新 | modified | 225 | 41 | 266 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed.md](#item-fe72fc) | minor update | SharePoint（インデックス付き）知識ソースの更新 | modified | 52 | 25 | 77 | 
| [agentic-knowledge-source-how-to-sharepoint-remote.md](#item-79d019) | minor update | リモートSharePoint知識ソースの更新 | modified | 24 | 18 | 42 | 
| [agentic-knowledge-source-how-to-web-manage.md](#item-af61ec) | minor update | Web知識ソース管理の更新 | modified | 15 | 15 | 30 | 
| [agentic-knowledge-source-how-to-web.md](#item-6b21d0) | minor update | Web知識ソースのAPIバージョン更新 | modified | 38 | 32 | 70 | 
| [agentic-knowledge-source-how-to-work-iq.md](#item-94718e) | breaking change | Work IQ知識ソースのAPIおよび認証方法の変更 | modified | 346 | 85 | 431 | 
| [agentic-knowledge-source-overview.md](#item-dcf29a) | minor update | 知識ソース概要のAPIバージョン更新 | modified | 13 | 9 | 22 | 
| [agentic-retrieval-how-to-answer-synthesis.md](#item-f44e99) | minor update | 回答合成機能のAPIバージョン更新 | modified | 37 | 25 | 62 | 
| [agentic-retrieval-how-to-configure-freshness.md](#item-0b04e6) | minor update | フレッシュネス設定に関するAPIバージョン更新 | modified | 20 | 8 | 28 | 
| [agentic-retrieval-how-to-create-index.md](#item-3fbd2e) | minor update | インデックス作成に関する内容の改善 | modified | 28 | 32 | 60 | 
| [agentic-retrieval-how-to-create-knowledge-base.md](#item-7df0e2) | minor update | 知識ベースの作成に関するドキュメントの改善 | modified | 245 | 110 | 355 | 
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | パイプライン作成に関するドキュメントの更新 | modified | 7 | 7 | 14 | 
| [agentic-retrieval-how-to-enable-disable.md](#item-44591a) | minor update | エージェント検索機能の有効化および無効化に関するドキュメントの更新 | modified | 13 | 13 | 26 | 
| [agentic-retrieval-how-to-image-serving.md](#item-48db70) | minor update | 画像サービングに関するドキュメントの更新 | modified | 21 | 15 | 36 | 
| [agentic-retrieval-how-to-migrate.md](#item-9653ea) | breaking change | エージェント検索移行に関するドキュメントの大幅な更新 | modified | 336 | 164 | 500 | 
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | new feature | エージェント検索の取得方法に関するドキュメントの大幅な更新 | modified | 1240 | 172 | 1412 | 
| [agentic-retrieval-how-to-set-retrieval-reasoning-effort.md](#item-141e97) | minor update | エージェント検索の推論努力設定に関するドキュメントの更新 | modified | 229 | 31 | 260 | 
| [agentic-retrieval-overview.md](#item-d1f354) | minor update | エージェント検索に関する概要ドキュメントの更新 | modified | 10 | 10 | 20 | 
| [cognitive-search-skill-vision-vectorize.md](#item-386571) | minor update | ビジョンスキルの入力パラメータに関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [enrichment-cache-how-to-configure.md](#item-b0ae0b) | minor update | エンリッチメントキャッシュ設定に関するドキュメントの更新 | modified | 4 | 4 | 8 | 
| [enrichment-cache-how-to-manage.md](#item-a972bd) | minor update | エンリッチメントキャッシュ管理に関するドキュメントの更新 | modified | 10 | 10 | 20 | 
| [get-started-portal-agentic-retrieval.md](#item-2bf1dc) | minor update | エージェンティックリトリーバルに関するAPIバージョンの更新 | modified | 1 | 1 | 2 | 
| [hybrid-search-how-to-query.md](#item-345ce6) | minor update | ハイブリッド検索のクエリ設定に関するAPIバージョンの更新 | modified | 7 | 7 | 14 | 
| [billing-split-version-compatibility.md](#item-c08436) | minor update | 請求とセマンティックランカーの課金に関する表の整形修正 | modified | 1 | 1 | 2 | 
| [knowledge-source-private-network.md](#item-41c52f) | new feature | プライベートネットワーク向けの新しい知識ソース設定手順 | added | 18 | 0 | 18 | 
| [agentic-retrieval-preview-api-usage.md](#item-2442de) | minor update | エージェンティックリトリーバルプレビューAPIに関する日付の更新 | modified | 2 | 2 | 4 | 
| [agentic-retrieval-java.md](#item-4e2c55) | minor update | エージェンティックリトリーバルJavaクイックスタートからの不要な情報の削除 | modified | 0 | 4 | 4 | 
| [agentic-retrieval-javascript.md](#item-715283) | minor update | エージェンティックリトリーバルJavaScriptクイックスタートからの不要な情報の削除 | modified | 0 | 4 | 4 | 
| [agentic-retrieval-python.md](#item-efee6a) | minor update | エージェンティックリトリーバルPythonクイックスタートからの不要な情報の削除 | modified | 0 | 4 | 4 | 
| [agentic-retrieval-rest.md](#item-3df373) | minor update | エージェンティックリトリーバルRESTクイックスタートのAPIバージョンの更新 | modified | 3 | 3 | 6 | 
| [agentic-retrieval-typescript.md](#item-e6370b) | minor update | エージェンティックリトリーバルTypeScriptクイックスタートからの不要な情報の削除 | modified | 0 | 4 | 4 | 
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | スコアリングプロファイルに関するAPIバージョンの更新 | modified | 4 | 4 | 8 | 
| [index-similarity-and-scoring.md](#item-75603d) | minor update | BM25スコアリングに関するAPIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-api-migration.md](#item-07297b) | minor update | 最新のREST APIへのアップグレードに関する情報の更新 | modified | 14 | 2 | 16 | 
| [search-blob-indexer-role-based-access.md](#item-887e42) | minor update | Azure Blob Indexerに関するAPIバージョンの更新 | modified | 5 | 5 | 10 | 
| [search-document-level-access-overview.md](#item-4bb055) | minor update | ドキュメントレベルのアクセス制御に関するAPIバージョンの更新 | modified | 11 | 11 | 22 | 
| [search-explorer.md](#item-738774) | minor update | Search ExplorerでのAPIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-faceted-navigation-examples.md](#item-2b1158) | minor update | ファセットナビゲーション例のAPIバージョン更新 | modified | 11 | 11 | 22 | 
| [search-file-storage-integration.md](#item-d20e26) | minor update | ファイルストレージ統合のAPIバージョン更新 | modified | 2 | 2 | 4 | 
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | ウィザードでのインデックスAPIバージョン更新 | modified | 1 | 1 | 2 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | インデックスAPIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-get-started-portal.md](#item-6d0cb1) | minor update | 検索インデックスのREST APIバージョン更新 | modified | 1 | 1 | 2 | 
| [search-how-to-create-indexers.md](#item-de71fb) | minor update | インデクサのリセットAPIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-how-to-index-cosmosdb-gremlin.md](#item-e5e93d) | minor update | APIバージョンの更新によるCosmos DB Gremlinインデクシング手順の改訂 | modified | 7 | 7 | 14 | 
| [search-how-to-index-cosmosdb-mongodb.md](#item-b5aa9f) | minor update | APIバージョンの更新によるCosmos DB MongoDBインデクシング手順の改訂 | modified | 9 | 9 | 18 | 
| [search-how-to-index-mysql.md](#item-fffdee) | minor update | APIバージョンの更新によるMySQLインデクシング手順の改訂 | modified | 5 | 5 | 10 | 
| [search-how-to-index-sharepoint-online.md](#item-8c099c) | minor update | APIバージョンの更新によるSharePoint Onlineインデクシング手順の改訂 | modified | 27 | 27 | 54 | 
| [search-how-to-multiple-indexers-one-index.md](#item-5ccefd) | minor update | APIバージョンの更新による複数インデクサーと単一インデックスの手順改訂 | modified | 71 | 71 | 142 | 
| [search-how-to-page-list-results.md](#item-73059a) | minor update | Azure AI Searchリスト結果のページング手法のアップデート | modified | 117 | 102 | 219 | 
| [search-how-to-semantic-chunking-content-understanding.md](#item-5968e6) | minor update | セマンティックチャンクとコンテンツ理解におけるAPIバージョンの更新 | modified | 8 | 8 | 16 | 
| [search-howto-managed-identities-cosmos-db.md](#item-a74464) | minor update | Cosmos DBとの接続方法に関するAPIバージョンの更新 | modified | 2 | 2 | 4 | 
| [search-howto-run-reset-indexers.md](#item-fb10c8) | minor update | インデクサーのリセットと実行に関するAPIバージョンの更新 | modified | 15 | 15 | 30 | 
| [search-index-access-control-lists-and-rbac-push-api.md](#item-45e71e) | minor update | RBACおよびACLを使用したインデクシングAPIのバージョン更新 | modified | 6 | 6 | 12 | 
| [search-indexer-access-control-lists-and-role-based-access.md](#item-67b42f) | minor update | RBACおよびACLに関するインデクサーAPIのバージョン更新 | modified | 6 | 6 | 12 | 
| [search-indexer-high-density-serverless-overview.md](#item-2bc606) | minor update | 高密度サーバーレスインデクサーに関するAPIバージョン更新 | modified | 3 | 3 | 6 | 
| [search-indexer-sensitivity-labels.md](#item-2a7bfc) | minor update | 感度ラベル機能のAPIバージョン更新 | modified | 11 | 11 | 22 | 
| [search-indexer-sharepoint-access-control-lists.md](#item-532a24) | minor update | SharePointアクセス制御リストに関するAPIバージョン更新 | modified | 12 | 12 | 24 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索の制限、クォータ、容量に関する文書の更新 | modified | 3 | 3 | 6 | 
| [search-more-like-this.md](#item-56c565) | minor update | More Like Thisクエリに関するAPIバージョンの更新 | modified | 4 | 4 | 8 | 
| [search-preview-terms.md](#item-4fe0af) | minor update | 検索プレビュー用語のAPIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-query-access-control-rbac-enforcement.md](#item-d24df7) | minor update | RBAC強制適用に関するプレビューAPIバージョンの更新 | modified | 9 | 9 | 18 | 
| [search-query-sensitivity-labels.md](#item-3e1f8a) | minor update | センシティビティラベルに関するクエリのAPIバージョンの更新 | modified | 6 | 6 | 12 | 
| [search-relevance-overview.md](#item-cb0e09) | minor update | 検索関連のAPIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | 暗号化キー管理に関するAPIバージョンの更新 | modified | 6 | 6 | 12 | 
| [search-security-managed-encryption-cross-tenant.md](#item-efc726) | minor update | クロステナントの暗号化に関するAPIバージョンの更新 | modified | 3 | 3 | 6 | 
| [search-sku-tier.md](#item-7686b8) | minor update | サーバーレス開発者ティアに関する情報の更新 | modified | 1 | 2 | 3 | 
| [semantic-answers.md](#item-c3fee9) | minor update | セマンティッククエリにおけるAPIバージョンの更新 | modified | 1 | 1 | 2 | 
| [semantic-code-migration.md](#item-ad1ba7) | minor update | セマンティックコード移行に関するAPIバージョンの追加 | modified | 1 | 0 | 1 | 
| [semantic-how-to-configure.md](#item-7a92a6) | minor update | セマンティック構成に関するAPIバージョンの更新と情報の整理 | modified | 6 | 22 | 28 | 
| [semantic-how-to-enable-disable.md](#item-71ac1e) | minor update | セマンティックランカーの有効化/無効化に関する情報の整備 | modified | 9 | 9 | 18 | 
| [semantic-how-to-query-rewrite.md](#item-3e168f) | minor update | クエリ再書き換えに関するAPIバージョンの更新 | modified | 3 | 3 | 6 | 
| [speller-how-to-add.md](#item-9b4502) | minor update | スペル補正機能に関するAPIバージョンの変更 | modified | 6 | 6 | 12 | 
| [toc.yml](#item-c4768f) | minor update | 目次の項目更新 | modified | 2 | 2 | 4 | 
| [troubleshoot-sharepoint-query-permission-filtering.md](#item-85cf41) | minor update | REST APIバージョンの更新 | modified | 2 | 2 | 4 | 
| [tutorial-adls-gen2-indexer-acls.md](#item-6881a0) | minor update | REST APIバージョンのアップデート | modified | 6 | 6 | 12 | 
| [tutorial-multimodal.md](#item-718d2e) | minor update | REST APIバージョンの更新 | modified | 10 | 10 | 20 | 
| [vector-search-how-to-chunk-documents.md](#item-b79133) | minor update | トークンチャンク処理に関するAPIバージョンの更新 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-query.md](#item-9bb93c) | minor update | ベクトルクエリに関するAPIバージョンの更新 | modified | 6 | 6 | 12 | 
| [vector-search-multi-vector-fields.md](#item-9aa482) | minor update | マルチベクトルフィールドに関するAPIバージョンの更新 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-fa71b4) | minor update | 最新のAzure AI Search機能に関する情報の更新 | modified | 25 | 9 | 34 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-azure-sql.md{#item-89aa4d}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to create an indexed Azure SQL knowledge source in Azure
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/02/2026
+ms.date: 08/14/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
@@ -14,17 +14,17 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
 An *indexed Azure SQL knowledge source* (preview) ingests rows from Azure SQL Database or Azure SQL Managed Instance into an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
-Unlike file-based knowledge sources, such as Azure Blob Storage and OneLake, each SQL row is treated as one logical document. The index schema is customer driven through explicit column mappings rather than a fixed document schema.
+Unlike file-based knowledge sources, such as Azure Blob Storage and OneLake, each SQL row is treated as one logical document. You drive the index schema through explicit column mappings rather than using a fixed document schema.
 
 When you create an indexed Azure SQL knowledge source, you specify a SQL data source, optional column mappings, and optional models to automatically generate the following Azure AI Search objects:
 
@@ -37,8 +37,8 @@ The generated indexer conforms to the *Azure SQL indexer*, whose prerequisites,
 
 ### Usage support
 
-| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources) |
-|--|--|--|--|--|--|--|
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-08-01-preview&preserve-view=true) |
+| -- | -- | -- | -- | -- | -- | -- |
 | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
@@ -47,31 +47,47 @@ The generated indexer conforms to the *Azure SQL indexer*, whose prerequisites,
 
 + Completion of the [Azure SQL indexer prerequisites](search-how-to-index-sql-database.md#prerequisites), including:
 
-    + An [Azure SQL Database](/azure/azure-sql/database/sql-database-paas-overview) or [Azure SQL Managed Instance](/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview) with a table or view to ingest.
-        
-    + A single-valued primary key on the source table or view.
-        
-    + For views, a column suitable for high-water-mark change detection. We strongly recommend a `rowversion` column.
+  + An [Azure SQL Database](/azure/azure-sql/database/sql-database-paas-overview) or [Azure SQL Managed Instance](/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview) with a table or view to ingest.
 
-+ Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
+  + A single-valued primary key on the source table or view.
+
+  + For views, a column suitable for high-water-mark change detection. We strongly recommend a `rowversion` column.
+
++ Permission to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 + If you specify `embeddingColumns`, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource that hosts the embedding model.
 
++ If you set `networkAccessMode` to `private`, complete the following requirements:
+
+  + Use an [S2, S3, L1, or L2 search service](search-sku-tier.md#tier-descriptions).
+
+  + Create and approve a shared private link to the SQL server with the `sqlServer` group ID. For SQL Managed Instance, use the `managedInstance` group ID.
+
+  + Use either SQL authentication or managed identity authentication. For managed identity, grant the identity the required Azure and database roles, and use a connection string with `Database=<database-name>` and the resource ID of the [SQL server](search-howto-managed-identities-sql.md) or [SQL Managed Instance](search-how-to-index-sql-managed-instance-with-managed-identity.md). Set `ingestionParameters.identity` only for a user-assigned identity. If you omit it, the indexer uses the search service's system-assigned identity.
+
+  + Create and approve a shared private link for each protected model endpoint. Use the `openai_account` group ID for Azure OpenAI endpoints and `foundry_account` for Foundry resource endpoints.
+
 ::: zone pivot="csharp"
 
 + The latest [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
+
 ::: zone-end
 
 ::: zone pivot="python"
 
 + The latest [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) preview package: `pip install --pre azure-search-documents`
 
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
+
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
++ The [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) version of the Search Service REST API.
+
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
@@ -82,7 +98,7 @@ The generated indexer conforms to the *Azure SQL indexer*, whose prerequisites,
 + The primary key is auto-discovered and can't be overridden.
 + `contentExtractionMode` supports only `"minimal"`.
 + Image extraction and image verbalization aren't supported.
-+ Real-time synchronization isn't supported. The generated indexer is schedule based.
++ Real-time synchronization isn't supported. The generated indexer is schedule-based.
 + Real-time SQL retrieval isn't supported. The knowledge source is indexed, not remote.
 
 ## Prepare the generated indexer
@@ -105,7 +121,7 @@ The generated indexer supports two authentication options:
 
 + **Managed identity authentication:** Use a system-assigned or user-assigned managed identity that has Azure RBAC and database-level roles on the SQL resource.
 
-For connection string formats, role requirements, and set up steps, see the [Azure SQL indexer prerequisites](search-how-to-index-sql-database.md#prerequisites) and [Connect through a managed identity](search-how-to-managed-identities.md).
+For connection string formats, role requirements, and setup steps, see the [Azure SQL indexer prerequisites](search-how-to-index-sql-database.md#prerequisites) and [Connect through a managed identity](search-how-to-managed-identities.md).
 
 ## Check for existing knowledge sources
 
@@ -120,7 +136,7 @@ The following JSON is an example response for an indexed Azure SQL knowledge sou
   "description": "Sample indexed Azure SQL knowledge source.",
   "encryptionKey": null,
   "indexedSqlParameters": {
-    "connectionString": "<SQL database connection string>",
+    "connectionString": "<sql-connection-string>",
     "tableOrView": "dbo.tbl_hotels",
     "contentColumns": [
       { "name": "hotelName", "sourceField": "HotelName", "searchFieldType": "Edm.String" },
@@ -134,7 +150,7 @@ The following JSON is an example response for an indexed Azure SQL knowledge sou
       "embeddingModel": {
         "kind": "azureOpenAI",
         "azureOpenAIParameters": {
-          "resourceUri": "<Foundry resource endpoint URI>",
+          "resourceUri": "<aoai-endpoint>",
           "deploymentId": "text-embedding-3-large",
           "modelName": "text-embedding-3-large"
         }
@@ -157,23 +173,23 @@ Run the following code to create an indexed Azure SQL knowledge source.
 ::: zone pivot="csharp"
 
 ```csharp
-using Azure;
+using Azure.Identity;
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 using Azure.Search.Documents.KnowledgeBases.Models;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var embeddingParams = new AzureOpenAIVectorizerParameters
 {
     ResourceUri = new Uri(aoaiEndpoint),
     DeploymentName = aoaiEmbeddingDeployment,
-    ModelName = aoaiEmbeddingModel,
-    ApiKey = aoaiKey
+    ModelName = aoaiEmbeddingModel
 };
 
 var ingestionParams = new KnowledgeSourceIngestionParameters
 {
+    NetworkAccessMode = KnowledgeSourceNetworkAccessMode.Public,
     ContentExtractionMode = "minimal",
     EmbeddingModel = new KnowledgeSourceAzureOpenAIVectorizer
     {
@@ -215,7 +231,7 @@ Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated
 ::: zone pivot="python"
 
 ```python
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import (
     AzureOpenAIVectorizerParameters,
@@ -227,18 +243,19 @@ from azure.search.documents.indexes.models import (
 from azure.search.documents.knowledgebases.models import (
     KnowledgeSourceAzureOpenAIVectorizer,
     KnowledgeSourceIngestionParameters,
+    KnowledgeSourceNetworkAccessMode,
 )
 
-index_client = SearchIndexClient(endpoint="search_url", credential=AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint="<search-endpoint>", credential=DefaultAzureCredential())
 
 embedding_params = AzureOpenAIVectorizerParameters(
-    resource_url="aoai_endpoint",
-    deployment_name="aoai_embedding_deployment",
-    model_name="aoai_embedding_model",
-    api_key="aoai_key",
+    resource_url="<aoai-endpoint>",
+    deployment_name="<aoai-embedding-deployment>",
+    model_name="<aoai-embedding-model>",
 )
 
 ingestion_params = KnowledgeSourceIngestionParameters(
+    network_access_mode=KnowledgeSourceNetworkAccessMode.PUBLIC,
     content_extraction_mode="minimal",
     embedding_model=KnowledgeSourceAzureOpenAIVectorizer(
         azure_open_ai_parameters=embedding_params
@@ -285,8 +302,8 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 
 ```http
 ### Create an indexed Azure SQL knowledge source
-PUT {{search-url}}/knowledgesources/indexedsqlks?api-version=2026-05-01-preview
-api-key: {{api-key}}
+PUT {{search-endpoint}}/knowledgesources/indexedsqlks?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 
 {
@@ -304,22 +321,22 @@ Content-Type: application/json
       { "name": "descriptionVector", "sourceField": "Description" }
     ],
     "ingestionParameters": {
+      "networkAccessMode": "public",
       "contentExtractionMode": "minimal",
       "embeddingModel": {
         "kind": "azureOpenAI",
         "azureOpenAIParameters": {
           "resourceUri": "{{aoai-endpoint}}",
           "deploymentId": "{{aoai-embedding-deployment}}",
-          "modelName": "{{aoai-embedding-model}}",
-          "apiKey": "{{aoai-key}}"
+          "modelName": "{{aoai-embedding-model}}"
         }
       }
     }
   }
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
@@ -333,7 +350,7 @@ Use `contentColumns` to map SQL text columns into searchable fields in the gener
 
 Use `embeddingColumns` to map SQL text columns into generated vector fields. Specify an embedding model in `ingestionParameters` when you use embedding columns.
 
-For indexed Azure SQL knowledge sources, `contentExtractionMode` must be `"minimal"` because SQL ingestion is row based and doesn't extract content from binary documents. Image extraction and image verbalization aren't supported, so `chatCompletionModel`, `assetStore`, `aiServices`, and image-related settings have no effect.
+For indexed Azure SQL knowledge sources, `contentExtractionMode` must be `"minimal"` because SQL ingestion is row-based and doesn't extract content from binary documents. Image extraction and image verbalization aren't supported, so `chatCompletionModel`, `assetStore`, `aiServices`, and image-related settings have no effect.
 
 ### Defaulting and validation rules
 
@@ -347,6 +364,16 @@ The following defaults apply when you create an indexed Azure SQL knowledge sour
 
 + The primary key of the source table or view is auto-discovered. Explicit overrides aren't supported, and the source must have a single-valued primary key.
 
+### Restrict ingestion to a private network
+
+Starting with the `2026-08-01-preview` API version, `networkAccessMode` controls the network environment in which the generated indexer for an indexed Azure SQL knowledge source runs. This setting affects ingestion only and doesn't change knowledge base retrieve requests or responses.
+
+`networkAccessMode` defaults to `public`, which preserves existing public network behavior. When `networkAccessMode` is `private`, the generated indexer runs in the [private execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment). It uses approved [shared private links](search-indexer-howto-access-private.md) to access the Azure SQL Database or SQL Managed Instance source connection and supported Azure dependencies, such as Azure OpenAI models and Microsoft Foundry resources.
+
+To configure and verify private network access:
+
+[!INCLUDE [Configure private network ingestion](includes/how-tos/knowledge-source-private-network.md)]
+
 ## Check ingestion status
 
 [!INCLUDE [Check ingestion status](includes/how-tos/knowledge-source-status.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースの Azure SQL に関する更新"
}
```

### Explanation
この変更は、Azure SQL 知識ソースに関するドキュメントの更新を反映しています。主な変更点として、新しい API バージョンのリリース日が `2026-05-01-preview` から `2026-08-01-preview` に変更されていることが挙げられます。また、ドキュメント内の記述がより明確に更新され、参加者によるデータマッピングやネットワークアクセスモードの設定など、インデクサー生成時の要件が強調されています。

具体的には、以下のような詳細な修正があります：

1. 日付の変更：ドキュメントの関連日付が新しい API リリース日付に合わせて変更されました。
2. 説明の見直し：プレビュー機能やその他のサービスとの接続についての説明が更新され、ユーザーが対応すべきセキュリティの注意点が強調されています。
3. 認証の方法に関する詳細が追加され、新しい認証メソッドが紹介されています。これにより、ユーザーは最新の Azure 環境での操作に関して、より正確な情報を得られます。

全体として、これらの変更はエンドユーザーにとっての利用可能性を高め、最新の Azure 環境との互換性を確保することを目的としています。

## articles/search/agentic-knowledge-source-how-to-blob.md{#item-ac6c8a}

<details>
<summary>Diff</summary>
````diff
@@ -16,11 +16,11 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [GA feature](./includes/previews/agentic-retrieval-ga-feature.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -43,7 +43,7 @@ The generated indexer conforms to the *blob indexer*, whose prerequisites, suppo
 ### Usage support
 
 | [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources) |
-|--|--|--|--|--|--|--|
+| -- | -- | -- | -- | -- | -- | -- |
 | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
@@ -54,39 +54,55 @@ The generated indexer conforms to the *blob indexer*, whose prerequisites, suppo
 
 + A blob container with [supported content types](search-how-to-index-azure-blob-storage.md#supported-document-formats) for text content. For optional image verbalization, the supported content type depends on whether your chat completion model can analyze and describe the image file.
 
-+ If `contentExtractionMode` is `standard`, use a Microsoft Foundry resource in a [region supported by Content Understanding in Foundry Tools](/azure/ai-services/content-understanding/language-region-support) and the `https://<resource-name>.services.ai.azure.com` endpoint. Deploy an embedding model, and deploy a multimodal chat model if you enable image verbalization.
++ If `contentExtractionMode` is `standard`, use a Microsoft Foundry resource in a [region supported by Content Understanding in Foundry Tools](/azure/ai-services/content-understanding/language-region-support) with a `https://<resource-name>.services.ai.azure.com` endpoint. The resource must have an embedding model deployment and, if you enable image verbalization, a multimodal chat model deployment.
 
-+ Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Permission to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 + A [managed identity](search-how-to-managed-identities.md) for the search service with **Storage Blob Data Reader** at the source storage-account scope and **Cognitive Services User** on the Microsoft Foundry resource. If you configure an asset store in a different storage account, also assign **Storage Blob Data Contributor** at that storage-account scope. If the source and asset containers share an account, **Storage Blob Data Contributor** provides both source read access and asset-store read/write access.
 
++ If you set `networkAccessMode` to `private`, complete the following requirements:
+
+  + Use an [S2, S3, L1, or L2 search service](search-sku-tier.md#tier-descriptions).
+
+  + Enable a system-assigned or user-assigned managed identity on the search service, grant it the **Storage Blob Data Reader** role on the storage account, and use a `ResourceId=/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Storage/storageAccounts/<storage-account>` connection string. For a user-assigned identity, also set `ingestionParameters.identity`.
+
+  + Create and approve a shared private link to the storage account with the `blob` group ID. For ADLS Gen2, create and approve both `blob` and `dfs` shared private links.
+
+  + Create and approve a shared private link for each protected model endpoint. Use the `openai_account` group ID for Azure OpenAI endpoints and `foundry_account` for Foundry resource endpoints.
+
 ::: zone pivot="csharp"
 
 + Required [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) package:
 
-  + For 2026-05-01-preview features, the latest preview package: `dotnet add package Azure.Search.Documents --prerelease`
+  + For `2026-08-01-preview` features, the latest preview package: `dotnet add package Azure.Search.Documents --prerelease`
+
+  + For `2026-04-01` features, the latest stable package: `dotnet add package Azure.Search.Documents`
 
-  + For 2026-04-01 features, the latest stable package: `dotnet add package Azure.Search.Documents`
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
 
 ::: zone-end
 
 ::: zone pivot="python"
 
 + Required [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) package:
 
-  + For 2026-05-01-preview features, the latest preview package: `pip install --pre azure-search-documents`
+  + For `2026-08-01-preview` features, the latest preview package: `pip install --pre azure-search-documents`
+
+  + For `2026-04-01` features, the latest stable package: `pip install azure-search-documents`
 
-  + For 2026-04-01 features, the latest stable package: `pip install azure-search-documents`
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
 
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ Required REST API version:
++ Required Search Service REST API version:
 
-  + For preview features: [Search Service 2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+  + For preview features: [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
-  + For generally available features: [Search Service 2026-04-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true)
+  + For generally available features: [2026-04-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true)
+
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
@@ -117,26 +133,23 @@ The following JSON is an example response for a blob knowledge source.
         "azureOpenAIParameters": {
           "resourceUri": "<REDACTED>",
           "deploymentId": "text-embedding-3-large",
-          "apiKey": "<REDACTED>",
           "modelName": "text-embedding-3-large",
           "authIdentity": null
         }
       },
       "chatCompletionModel": {
         "kind": "azureOpenAI",
         "azureOpenAIParameters": {
-          "resourceUri": "<your-foundry-resource-endpoint>",
+          "resourceUri": "<aoai-endpoint>",
           "deploymentId": "gpt-5-mini",
-          "apiKey": "<REDACTED>",
           "modelName": "gpt-5-mini",
           "authIdentity": null
         }
       },
       "ingestionSchedule": null,
       "assetStore": null,
       "aiServices": {
-        "uri": "<your-foundry-resource-endpoint>",
-        "apiKey": "<REDACTED>"
+        "uri": "<aoai-endpoint>",
       }
     },
     "createdResources": {
@@ -158,16 +171,17 @@ Run the following code to create a blob knowledge source.
 
 ::: zone pivot="csharp"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```csharp
 // Create a blob knowledge source
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 using Azure.Search.Documents.KnowledgeBases.Models;
-using Azure;
+using Azure.Search.Documents.Models;
+using Azure.Identity;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var chatCompletionParams = new AzureOpenAIVectorizerParameters
 {
@@ -185,6 +199,7 @@ var embeddingParams = new AzureOpenAIVectorizerParameters
 
 var ingestionParams = new KnowledgeSourceIngestionParameters
 {
+    NetworkAccessMode = KnowledgeSourceNetworkAccessMode.Public,
     DisableImageVerbalization = false,
     ChatCompletionModel = new KnowledgeBaseAzureOpenAIModel(azureOpenAIParameters: chatCompletionParams),
     EmbeddingModel = new KnowledgeSourceAzureOpenAIVectorizer
@@ -228,9 +243,9 @@ Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 using Azure.Search.Documents.KnowledgeBases.Models;
-using Azure;
+using Azure.Identity;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var chatCompletionParams = new AzureOpenAIVectorizerParameters
 {
@@ -285,16 +300,16 @@ Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated
 
 ::: zone pivot="python"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```python
 # Create a blob knowledge source
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
-from azure.search.documents.indexes.models import AzureBlobKnowledgeSource, AzureBlobKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceContentExtractionMode
-from azure.search.documents.knowledgebases.models import KnowledgeSourceAzureOpenAIVectorizer, KnowledgeSourceIngestionParameters
+from azure.search.documents.indexes.models import AzureBlobKnowledgeSource, AzureBlobKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceAzureOpenAIVectorizer, KnowledgeSourceContentExtractionMode, KnowledgeSourceIngestionParameters
+from azure.search.documents.knowledgebases.models import KnowledgeSourceNetworkAccessMode
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
 knowledge_source = AzureBlobKnowledgeSource(
     name = "my-blob-ks",
@@ -306,22 +321,21 @@ knowledge_source = AzureBlobKnowledgeSource(
         folder_path = None,
         is_adls_gen2 = False,
         ingestion_parameters = KnowledgeSourceIngestionParameters(
+            network_access_mode = KnowledgeSourceNetworkAccessMode.PUBLIC,
             identity = None,
             disable_image_verbalization = False,
             chat_completion_model = KnowledgeBaseAzureOpenAIModel(
                 azure_open_ai_parameters = AzureOpenAIVectorizerParameters(
-                    resource_url = "aoai_endpoint",
-                    deployment_name = "aoai_gpt_deployment",
-                    model_name = "aoai_gpt_model",
-                    api_key = "aoai_api_key"
+                    resource_url = "<aoai-endpoint>",
+                    deployment_name = "<aoai-gpt-deployment>",
+                    model_name = "<aoai-gpt-model>",
                 )
             ),
             embedding_model = KnowledgeSourceAzureOpenAIVectorizer(
                 azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
-                    resource_url = "aoai_endpoint",
-                    deployment_name = "aoai_embedding_deployment",
-                    model_name = "aoai_embedding_model",
-                    api_key = "aoai_api_key"
+                    resource_url = "<aoai-endpoint>",
+                    deployment_name = "<aoai-embedding-deployment>",
+                    model_name = "<aoai-embedding-model>",
                 )
             ),
             content_extraction_mode = KnowledgeSourceContentExtractionMode.MINIMAL,
@@ -341,12 +355,12 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 
 ```python
 # Create a blob knowledge source
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import AzureBlobKnowledgeSource, AzureBlobKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceContentExtractionMode
 from azure.search.documents.knowledgebases.models import KnowledgeSourceIngestionParameters, KnowledgeSourceAzureOpenAIVectorizer
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
 knowledge_source = AzureBlobKnowledgeSource(
     name = "my-blob-ks",
@@ -362,18 +376,16 @@ knowledge_source = AzureBlobKnowledgeSource(
             disable_image_verbalization = False,
             chat_completion_model = KnowledgeBaseAzureOpenAIModel(
                 azure_open_ai_parameters = AzureOpenAIVectorizerParameters(
-                    resource_url = "aoai_endpoint",
-                    deployment_name = "aoai_gpt_deployment",
-                    model_name = "aoai_gpt_model",
-                    api_key = "aoai_api_key"
+                    resource_url = "<aoai-endpoint>",
+                    deployment_name = "<aoai-gpt-deployment>",
+                    model_name = "<aoai-gpt-model>",
                 )
             ),
             embedding_model = KnowledgeSourceAzureOpenAIVectorizer(
                 azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
-                    resource_url = "aoai_endpoint",
-                    deployment_name = "aoai_embedding_deployment",
-                    model_name = "aoai_embedding_model",
-                    api_key = "aoai_api_key"
+                    resource_url = "<aoai-endpoint>",
+                    deployment_name = "<aoai-embedding-deployment>",
+                    model_name = "<aoai-embedding-model>",
                 )
             ),
             content_extraction_mode = KnowledgeSourceContentExtractionMode.MINIMAL,
@@ -394,12 +406,12 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 
 ::: zone pivot="rest"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```http
 ### Create a blob knowledge source
-PUT {{search-url}}/knowledgesources/my-blob-ks?api-version=2026-05-01-preview
-Authorization: Bearer {{token}}
+PUT {{search-endpoint}}/knowledgesources/my-blob-ks?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 
 {
@@ -409,10 +421,11 @@ Content-Type: application/json
   "encryptionKey": null,
   "azureBlobParameters": {
   "connectionString": "ResourceId=<storage-resource-id>",
-    "containerName": "<YOUR BLOB CONTAINER NAME>",
+    "containerName": "<blob-container-name>",
     "folderPath": null,
     "isADLSGen2": false,
     "ingestionParameters": {
+        "networkAccessMode": "public",
         "identity": null,
         "disableImageVerbalization": null,
         "chatCompletionModel": {
@@ -439,14 +452,14 @@ Content-Type: application/json
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 # [2026-04-01](#tab/2026-04-01)
 
 ```http
 ### Create a blob knowledge source
-PUT {{search-url}}/knowledgesources/my-blob-ks?api-version=2026-04-01
-Authorization: Bearer {{token}}
+PUT {{search-endpoint}}/knowledgesources/my-blob-ks?api-version=2026-04-01
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 
 {
@@ -456,7 +469,7 @@ Content-Type: application/json
   "encryptionKey": null,
   "azureBlobParameters": {
   "connectionString": "ResourceId=<storage-resource-id>",
-    "containerName": "<YOUR BLOB CONTAINER NAME>",
+    "containerName": "<blob-container-name>",
     "folderPath": null,
     "isADLSGen2": false,
     "ingestionParameters": {
@@ -492,7 +505,17 @@ Content-Type: application/json
 ::: zone-end
 
 > [!NOTE]
-> Document-level permissions enforcement using `ingestionPermissionOptions` requires the 2026-05-01-preview API version. 2026-04-01 doesn't support this feature.
+> To enforce document-level permissions with `ingestionPermissionOptions`, use the 2026-08-01-preview API version. The 2026-04-01 API version doesn't support this feature.
+
+### Restrict ingestion to a private network (preview)
+
+Starting with the `2026-08-01-preview` API version, `networkAccessMode` controls the network environment in which the generated indexer for a blob knowledge source runs. This setting affects ingestion only and doesn't change knowledge base retrieve requests or responses.
+
+`networkAccessMode` defaults to `public`, which preserves existing public network behavior. When `networkAccessMode` is `private`, the generated indexer runs in the [private execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment). It uses approved [shared private links](search-indexer-howto-access-private.md) to access the Azure Blob Storage or ADLS Gen2 source connection and supported Azure dependencies, such as Azure OpenAI models and Microsoft Foundry resources.
+
+To configure and verify private network access:
+
+[!INCLUDE [Configure private network ingestion](includes/how-tos/knowledge-source-private-network.md)]
 
 ## Check ingestion status
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースの Azure Blob に関する更新"
}
```

### Explanation
この変更は、Azure Blob を使用したエージェント知識ソースに関するドキュメントの更新を反映しています。最も重要な変更として、新しい API バージョン `2026-05-01-preview` が `2026-08-01-preview` に更新され、大幅に改善された機能が盛り込まれています。また、ドキュメントの内容は、Azure Blob ストレージの使用方法および関連する認証の仕組みについての詳細を強調しています。

主な変更点は以下の通りです：

1. **API バージョンの更新**：ドキュメント内のすべての参照が、プレビュー API バージョンを新しい日付に合わせて更新されています。
2. **パーミッションの扱い**：新しい API バージョンにおいて、アクセス権の変更に関連する注意点が強調されています。特に、外部で設定されたパーミッションに対して制限があることが再確認されました。
3. **ネットワークアクセスの設定**：新たに `networkAccessMode` 設定が導入され、プライベートネットワーク環境下でのインデクシングの動作について詳細が追加されました。
4. **コードの例の更新**：C# および Python のサンプルコードが新しい API バージョンに合わせて修正され、利用者がより簡単にアップデートを実施できるようになっています。

これらの変更は、Azure Blob ストレージを介してエージェント知識ソースを利用する開発者にとって、最新の機能とベストプラクティスを反映したものであり、利用方法がより明確になっています。

## articles/search/agentic-knowledge-source-how-to-fabric-data-agent.md{#item-900ecc}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
 title: Create a Fabric Data Agent Knowledge Source
-description: Learn how to create a Fabric Data Agent knowledge source, which connects a Microsoft Fabric Data Agent to an agentic retrieval pipeline in Azure AI Search for live, data-driven answers as grounding data.
+description: Learn how to create a Fabric Data Agent knowledge source in Azure AI Search for live, data-driven answers from Microsoft Fabric.
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 06/02/2026
@@ -13,9 +13,9 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > When you connect to Fabric IQ, you might incur costs, and data might be sent outside the Azure compliance boundary and processed according to the applicable service terms and data handling policies. It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -29,9 +29,9 @@ Unlike indexed knowledge sources, Fabric Data Agent knowledge sources query live
 
 ### Usage support
 
-| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-08-01-preview&preserve-view=true) |
+| -- | -- | -- | -- | -- | -- | -- |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
@@ -41,23 +41,29 @@ Unlike indexed knowledge sources, Fabric Data Agent knowledge sources query live
 
 + Your search service and workspace must be in the same Microsoft Entra ID tenant.
 
-+ Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Permission to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 ::: zone pivot="csharp"
 
 + The latest [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
+
 ::: zone-end
 
 ::: zone pivot="python"
 
 + The latest [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) preview package: `pip install --pre azure-search-documents`
 
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
+
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
++ The [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) version of the Search Service REST API.
+
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
@@ -102,12 +108,12 @@ Run the following code to create a Fabric Data Agent knowledge source.
 ::: zone pivot="csharp"
 
 ```csharp
-using Azure;
+using Azure.Identity;
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 
-Uri searchEndpoint = new Uri("<search-service-url>");
-AzureKeyCredential credential = new AzureKeyCredential("<api-key>");
+Uri searchEndpoint = new Uri("<search-endpoint>");
+DefaultAzureCredential credential = new DefaultAzureCredential();
 var indexClient = new SearchIndexClient(searchEndpoint, credential);
 
 var fabricDataAgent = new FabricDataAgentKnowledgeSource(
@@ -127,16 +133,16 @@ await indexClient.CreateOrUpdateKnowledgeSourceAsync(fabricDataAgent);
 ::: zone pivot="python"
 
 ```python
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import (
     FabricDataAgentKnowledgeSource,
     FabricDataAgentKnowledgeSourceParameters,
 )
 
 index_client = SearchIndexClient(
-    endpoint="<search-service-url>",
-    credential=AzureKeyCredential("<api-key>")
+    endpoint="<search-endpoint>",
+    credential=DefaultAzureCredential()
 )
 
 knowledge_source = FabricDataAgentKnowledgeSource(
@@ -159,8 +165,8 @@ index_client.create_or_update_knowledge_source(knowledge_source)
 
 ```http
 ### Create a Fabric Data Agent knowledge source
-PUT {{search-url}}/knowledgesources/my-fabric-data-agent-ks?api-version=2026-05-01-preview
-api-key: {{api-key}}
+PUT {{search-endpoint}}/knowledgesources/my-fabric-data-agent-ks?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 
 {
@@ -174,7 +180,7 @@ Content-Type: application/json
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
@@ -226,7 +232,7 @@ The following example shows a retrieve response containing a Fabric Data Agent k
       }
     },
     {
-      // ... Additional activity records omitted for brevity 
+      // ... Additional activity records omitted for brevity
     }
   ],
   "references": [
@@ -249,7 +255,7 @@ The following example shows a retrieve response containing a Fabric Data Agent k
       }
     },
     {
-      // ... Additional references omitted for brevity 
+      // ... Additional references omitted for brevity
     }
   ]
 }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファブリックデータエージェント知識ソースの更新"
}
```

### Explanation
この変更は、ファブリックデータエージェント知識ソースに関するドキュメントの改善を示しています。主な変更ポイントには、API バージョンが `2026-05-01-preview` から `2026-08-01-preview` に更新されたことが含まれます。また、ドキュメントの記述がより明確になり、検索サービスとの接続方法に関する詳細が追加されています。

具体的には以下のような変更があります：

1. **説明文の修正**：ファブリックデータエージェントについての説明がシンプルかつ明確に更新され、Microsoft Fabric からライブでデータ駆動の回答を得られることが強調されています。
2. **API バージョンの更新**：プレビュー API バージョンの参照が新しい日付に変更され、使用できる機能が最新のものに合わせられています。
3. **接続情報の明確化**：Azure を利用する際の接続に関する注意点が明示され、適切な権限や認証方法についての情報が整理されました。
4. **コード例の更新**：C# および Python のサンプルコードが新しい API バージョンに対応する形で修正され、特に認証の方法が `AzureKeyCredential` から `DefaultAzureCredential` に変更されたことが目を引きます。

この改訂により、ユーザーはファブリックデータエージェントを利用した知識ソースの作成に関するより正確で最新の情報を得ることができ、実装に際しての理解が深まります。

## articles/search/agentic-knowledge-source-how-to-fabric-ontology.md{#item-1f2bb6}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
 title: Create a Fabric Ontology Knowledge Source
-description: Learn how to create a Fabric Ontology knowledge source, which connects a Microsoft Fabric ontology to an agentic retrieval pipeline in Azure AI Search for ontology-backed answers.
+description: Learn how to create a Fabric Ontology knowledge source in Azure AI Search for ontology-backed answers from Microsoft Fabric.
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 06/02/2026
@@ -13,9 +13,9 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > When you connect to Fabric IQ, you might incur costs, and data might be sent outside the Azure compliance boundary and processed according to the applicable service terms and data handling policies. It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -29,9 +29,9 @@ Unlike indexed knowledge sources, Fabric Ontology knowledge sources query live d
 
 ### Usage support
 
-| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-08-01-preview&preserve-view=true) |
+| -- | -- | -- | -- | -- | -- | -- |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
@@ -41,23 +41,29 @@ Unlike indexed knowledge sources, Fabric Ontology knowledge sources query live d
 
 + Your search service and workspace must be in the same Microsoft Entra ID tenant.
 
-+ Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Permission to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 ::: zone pivot="csharp"
 
 + The latest [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
+
 ::: zone-end
 
 ::: zone pivot="python"
 
 + The latest [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) preview package: `pip install --pre azure-search-documents`
 
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
+
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
++ The [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) version of the Search Service REST API.
+
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
@@ -102,12 +108,12 @@ Run the following code to create a Fabric Ontology knowledge source.
 ::: zone pivot="csharp"
 
 ```csharp
-using Azure;
+using Azure.Identity;
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 
-Uri searchEndpoint = new Uri("<search-service-url>");
-AzureKeyCredential credential = new AzureKeyCredential("<api-key>");
+Uri searchEndpoint = new Uri("<search-endpoint>");
+DefaultAzureCredential credential = new DefaultAzureCredential();
 var indexClient = new SearchIndexClient(searchEndpoint, credential);
 
 var fabricOntology = new FabricOntologyKnowledgeSource(
@@ -127,16 +133,16 @@ await indexClient.CreateOrUpdateKnowledgeSourceAsync(fabricOntology);
 ::: zone pivot="python"
 
 ```python
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import (
     FabricOntologyKnowledgeSource,
     FabricOntologyKnowledgeSourceParameters,
 )
 
 index_client = SearchIndexClient(
-    endpoint="<search-service-url>",
-    credential=AzureKeyCredential("<api-key>")
+    endpoint="<search-endpoint>",
+    credential=DefaultAzureCredential()
 )
 
 knowledge_source = FabricOntologyKnowledgeSource(
@@ -159,8 +165,8 @@ index_client.create_or_update_knowledge_source(knowledge_source)
 
 ```http
 ### Create a Fabric Ontology knowledge source
-PUT {{search-url}}/knowledgesources/my-fabric-ontology-ks?api-version=2026-05-01-preview
-api-key: {{api-key}}
+PUT {{search-endpoint}}/knowledgesources/my-fabric-ontology-ks?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 
 {
@@ -174,7 +180,7 @@ Content-Type: application/json
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
@@ -226,7 +232,7 @@ The following example shows a retrieve response containing a Fabric Ontology kno
       }
     },
     {
-      // ... Additional activity records omitted for brevity 
+      // ... Additional activity records omitted for brevity
     }
   ],
   "references": [
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファブリック・オントロジー知識ソースの更新"
}
```

### Explanation
この変更は、ファブリック・オントロジー知識ソースに関するドキュメントの更新を示しています。主な更新内容は、API バージョンが `2026-05-01-preview` から `2026-08-01-preview` に切り替えられ、ドキュメントの説明が明確化された点にあります。この更新により、Azure AI Search 内でのオントロジーに基づく回答の提供に関する情報が整理されています。

具体的な変更点は以下のとおりです：

1. **説明文の改善**：ファブリック・オントロジー知識ソースの説明が更新され、Microsoft Fabric からオントロジーに基づく回答を取得できることが強調されています。
2. **API バージョンの更新**：使用するREST APIのバージョンが新しいものに変更され、最新の機能を利用できることが裾野を広げています。
3. **接続サポートの明示化**：Microsoftサービスおよびサードパーティサービスへの接続についての情報が整備され、データの処理やストレージに関する注意事項が強調されています。
4. **認証方法の変更**：C#およびPythonのサンプルコードで、`AzureKeyCredential` から `DefaultAzureCredential` への変更が行われ、より柔軟で安全な認証が推奨されています。

これらの改訂により、ユーザーはファブリック・オントロジー知識ソースをAzure AI Searchでどのように効果的に使用するかについての整理された情報を得ることができます。

## articles/search/agentic-knowledge-source-how-to-file.md{#item-88f720}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Create a File Knowledge Source for Agentic Retrieval
 description: Learn how to create a file knowledge source in Azure AI Search, upload files directly, and use the processed content in a knowledge base.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/08/2026
+ms.date: 08/21/2026
 ai-usage: ai-assisted
 ms.custom: doc-kit-assisted
 zone_pivot_groups: search-csharp-python-rest
@@ -14,9 +14,9 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The preview APIs support connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -26,67 +26,105 @@ A *file knowledge source* (preview) uploads small-to-medium file sets directly t
 
 File knowledge sources are useful when you want a managed upload experience instead of provisioning Azure Storage, configuring access, and creating an indexer pipeline over an external container. Azure AI Search processes uploaded files so their extracted content can be retrieved from a knowledge base.
 
-A file knowledge source supports up to 100 files. Use a [blob knowledge source](agentic-knowledge-source-how-to-blob.md) instead when your files are already in Azure Blob Storage or Azure Data Lake Storage Gen2, when your file set exceeds or is likely to exceed 100 files, or when you need scheduled ingestion. Also use a blob knowledge source when you want to manage source blobs with [Azure Blob Storage lifecycle management policies](/azure/storage/blobs/lifecycle-management-overview) or when you need [document-level permissions (preview)](agentic-knowledge-source-how-to-blob.md#enforce-document-level-permissions-preview) based on permissions in Azure Storage.
+Use a [blob knowledge source](agentic-knowledge-source-how-to-blob.md) instead when your files are already in Azure Blob Storage or Azure Data Lake Storage Gen2, when your file set exceeds or is likely to exceed the [file knowledge source limits](#file-support-and-limits), or when you need scheduled ingestion. Also use a blob knowledge source when you want to manage source blobs with [Azure Blob Storage lifecycle management policies](/azure/storage/blobs/lifecycle-management-overview) or when you need [document-level permissions (preview)](agentic-knowledge-source-how-to-blob.md#enforce-document-level-permissions-preview) based on permissions in Azure Storage.
 
 ### Usage support
 
-| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-08-01-preview&preserve-view=true) |
+| -- | -- | -- | -- | -- | -- | -- |
 | ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
-+ A dedicated Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md). File knowledge sources aren't supported on serverless search services. For more information about dedicated tiers, see [Choose a service tier](search-sku-tier.md). If you need paid usage beyond the monthly free allowance, set the `knowledgeRetrieval` service property to `standard` by using the [Search Management REST API](/rest/api/searchmanagement/services/create-or-update).
++ An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md). File knowledge sources support both the Dedicated and Serverless pricing models. For model and tier details, see [Choose a pricing model and service tier](search-sku-tier.md).
 
-+ Files in a [supported format](#supported-formats-and-limits).
++ Review [Azure AI Search costs](search-sku-manage-costs.md). Model calls, vectorization, and other AI processing can incur separate charges.
 
-+ Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ On Serverless, successful file ingestion operations consume billable compute. Failed uploads don't incur Serverless compute charges.
+
++ If you need paid agentic retrieval beyond the monthly free allowance, [enable the standard agentic retrieval plan](agentic-retrieval-how-to-enable-disable.md). The `knowledgeRetrieval=standard` setting is separate from Serverless compute and storage charges and doesn't select a pricing model.
+
++ Files in a [supported format](#file-support-and-limits).
+
++ Permission to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 + If the knowledge source specifies an Azure OpenAI model for embeddings, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource.
 
-  + If the Foundry resource has public network access disabled, create an `openai_account` [shared private link](search-indexer-howto-access-private.md#supported-resource-types) from the search service to the Foundry resource, and keep the resource's **Allow Azure services on the trusted services list** setting enabled.
+  + If the Foundry resource has public network access disabled, create a `foundry_account` [shared private link](search-indexer-howto-access-private.md#supported-resource-types) from the search service to the Foundry resource and keep the resource's **Allow Azure services on the trusted services list** setting enabled.
+
++ If the knowledge source specifies the `standard` content extraction mode, review the requirements for the [Azure Content Understanding skill](cognitive-search-skill-content-understanding.md).
+
+  + Usage is charged at [Azure Content Understanding in Foundry Tools pricing](https://azure.microsoft.com/pricing/details/content-understanding/) to the Foundry resource configured through `aiServices`.
+
+  + The 20-document daily free allowance available to some built-in skills doesn't apply.
+
+  + For the example in this article, you need the Foundry resource endpoint and key, plus Azure OpenAI embedding and chat completion model information.
 
 ::: zone pivot="csharp"
 
 + The latest [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
+
 ::: zone-end
 
 ::: zone pivot="python"
 
 + The latest [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) preview package: `pip install --pre azure-search-documents`
 
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
+
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
++ The [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) version of the Search Service REST API.
+
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
-## Supported formats and limits
+## File support and limits
+
+Before you create a file knowledge source, review the requirements and limits that affect file upload, extraction, and management.
+
+### Supported content types
+
+File knowledge sources accept files based on detected content type. A caller-provided content type doesn't override detection.
 
-The following file types are supported.
+Supported content types include:
 
-| Category | Extensions |
-|--|--|
-| Text | `.txt`, `.md`, `.html`, `.json`, `.csv` |
-| Code | `.c`, `.cs`, `.cpp`, `.java`, `.py`, `.js`, `.ts`, `.php`, `.rb`, `.sh` |
-| Documents | `.pdf`, `.docx`, `.pptx`, `.doc` |
++ PDF
++ Word (`.doc`, `.docx`)
++ PowerPoint (`.ppt`, `.pptx`)
++ Excel (`.xls`, `.xlsx`)
++ JSON
++ Shell scripts
++ Content detected as `text/*`, such as `.txt`, `.md`, `.html`, and `.csv`
 
-The following limits apply to file knowledge sources.
+### Supported extraction modes
 
-| Limit | Value |
-|--|--|
-| Maximum file size per upload | 50 MB |
-| Maximum files per file knowledge source | 100 |
++ For the listed content types, both `2026-05-01-preview` and `2026-08-01-preview` support `minimal`. `standard` is available only in `2026-08-01-preview`.
 
-If you configure the file knowledge source to chunk or vectorize uploaded content, model and downstream processing limits also apply.
++ Content detected as `image/*` isn't supported in `2026-05-01-preview`. In `2026-08-01-preview`, use `standard` extraction. `minimal` extraction returns HTTP status `415` in both versions.
+
+### Limits and file operations
+
+Limits and supported file operations differ by API version.
+
+| Capability | `2026-05-01-preview` | `2026-08-01-preview` |
+| -- | -- | -- |
+| Maximum files per knowledge source | 100 | 200 |
+| Maximum file size | 50 MB on all supported pricing tiers | 50 MB on Free and Basic; 100 MB on other supported Dedicated tiers and Serverless |
+| Processing duration | Upload can run for up to 180 seconds | Upload and update can run for up to 180 seconds |
+| Upload content and metadata | Raw file content | Raw file content or multipart content with metadata |
+| List uploaded files | List files | Filter by path or file name, and return richer file details |
+| Replace existing file content | Delete and re-upload | Use update operation |
+| Browser access to file operations | CORS isn't available | Configure CORS |
 
 > [!NOTE]
-> + Uploading the same file name doesn't replace an existing file. For more information, see [Upload files](#upload-files).
 > + The generated search index stores the uploaded content. For total storage limits by pricing tier, see [Service limits](search-limits-quotas-capacity.md#service-limits).
-
+> + If you configure the file knowledge source to chunk or vectorize uploaded content, model and downstream processing limits also apply.
 
 ## Check for existing knowledge sources
 
@@ -120,14 +158,16 @@ The following JSON is an example response for a file knowledge source.
 
 Create a file knowledge source that specifies the embedding model used to vectorize uploaded content.
 
+Each file knowledge source creates an index, but not an indexer or schedule. You must include the `fileParameters.ingestionParameters` object. The service rejects requests that specify `networkAccessMode`.
+
 ::: zone pivot="csharp"
 
 ```csharp
-using Azure;
+using Azure.Identity;
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var embeddingParams = new AzureOpenAIVectorizerParameters
 {
@@ -169,7 +209,7 @@ Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated
 ::: zone pivot="python"
 
 ```python
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import (
     AzureOpenAIVectorizerParameters,
@@ -181,12 +221,12 @@ from azure.search.documents.knowledgebases.models import (
     KnowledgeSourceIngestionParameters,
 )
 
-index_client = SearchIndexClient(endpoint="search_url", credential=AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint="<search-endpoint>", credential=DefaultAzureCredential())
 
 embedding_params = AzureOpenAIVectorizerParameters(
-    resource_url="aoai_endpoint",
-    deployment_name="aoai_embedding_deployment",
-    model_name="aoai_embedding_model",
+    resource_url="<aoai-endpoint>",
+    deployment_name="<aoai-embedding-deployment>",
+    model_name="<aoai-embedding-model>",
 )
 
 ingestion_params = KnowledgeSourceIngestionParameters(
@@ -213,8 +253,8 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 ::: zone pivot="rest"
 
 ```http
-PUT {{search-url}}/knowledgesources/my-file-ks?api-version=2026-05-01-preview
-api-key: {{api-key}}
+PUT {{search-endpoint}}/knowledgesources/my-file-ks?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 Prefer: return=representation
 
@@ -239,24 +279,187 @@ Prefer: return=representation
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
+### Configure standard extraction
+
+Starting with the `2026-08-01-preview` API version, `standard` extraction uses Content Understanding to extract, semantically chunk, and enrich uploaded files. Azure AI Search manages this processing as part of the knowledge source, and [Content Understanding charges](https://azure.microsoft.com/pricing/details/content-understanding/) apply separately.
+
+::: zone pivot="csharp"
+
+```csharp
+using Azure.Identity;
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+using Azure.Search.Documents.KnowledgeBases.Models;
+
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
+
+var embeddingParameters = new AzureOpenAIVectorizerParameters
+{
+  ResourceUri = new Uri(aoaiEndpoint),
+  DeploymentName = aoaiEmbeddingDeployment,
+  ModelName = aoaiEmbeddingModel
+};
+
+var ingestionParameters = new KnowledgeSourceIngestionParameters
+{
+  ContentExtractionMode = KnowledgeSourceContentExtractionMode.Standard,
+  AiServices = new AIServices(new Uri(foundryEndpoint)) { ApiKey = foundryKey },
+  EmbeddingModel = new KnowledgeSourceAzureOpenAIVectorizer
+  {
+    AzureOpenAIParameters = embeddingParameters
+  },
+  ChatCompletionModel = new KnowledgeBaseAzureOpenAIModel(
+    new AzureOpenAIVectorizerParameters
+    {
+      ResourceUri = new Uri(aoaiEndpoint),
+      DeploymentName = aoaiChatDeployment,
+      ModelName = aoaiChatModel
+    })
+};
+
+var knowledgeSource = new FileKnowledgeSource(
+  "my-file-ks",
+  new FileKnowledgeSourceParameters { IngestionParameters = ingestionParameters });
+
+await indexClient.CreateOrUpdateKnowledgeSourceAsync(knowledgeSource);
+Console.WriteLine($"Configured standard extraction for '{knowledgeSource.Name}'.");
+```
+
+**Reference:** [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient?view=azure-dotnet-preview&preserve-view=true)
+
+::: zone-end
+
+::: zone pivot="python"
+
+```python
+from azure.identity import DefaultAzureCredential
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import (
+  AzureOpenAIVectorizerParameters,
+  FileKnowledgeSource,
+  FileKnowledgeSourceParameters,
+  KnowledgeBaseAzureOpenAIModel,
+)
+from azure.search.documents.knowledgebases.models import (
+  AIServices,
+  KnowledgeSourceAzureOpenAIVectorizer,
+  KnowledgeSourceIngestionParameters,
+)
+
+index_client = SearchIndexClient(endpoint="<search-endpoint>", credential=DefaultAzureCredential())
+
+embedding_parameters = AzureOpenAIVectorizerParameters(
+  resource_url="<aoai-endpoint>",
+  deployment_name="<aoai-embedding-deployment>",
+  model_name="<aoai-embedding-model>",
+)
+ingestion_parameters = KnowledgeSourceIngestionParameters(
+  content_extraction_mode="standard",
+  ai_services=AIServices(
+    uri="<foundry-resource-endpoint>",
+    api_key="<foundry-resource-key>",
+  ),
+  embedding_model=KnowledgeSourceAzureOpenAIVectorizer(
+    azure_open_ai_parameters=embedding_parameters
+  ),
+  chat_completion_model=KnowledgeBaseAzureOpenAIModel(
+    azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
+      resource_url="<aoai-endpoint>",
+      deployment_name="<aoai-gpt-deployment>",
+      model_name="<aoai-gpt-model>",
+    )
+  ),
+)
+knowledge_source = FileKnowledgeSource(
+  name="my-file-ks",
+  file_parameters=FileKnowledgeSourceParameters(
+    ingestion_parameters=ingestion_parameters
+  ),
+)
+
+index_client.create_or_update_knowledge_source(knowledge_source)
+print(f"Configured standard extraction for '{knowledge_source.name}'.")
+```
+
+**Reference:** [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient?view=azure-python-preview&preserve-view=true)
+
+::: zone-end
+
+::: zone pivot="rest"
+
+```http
+PUT {{search-endpoint}}/knowledgesources/my-file-ks?api-version=2026-08-01-preview
+Content-Type: application/json
+Authorization: Bearer {{search-access-token}}
+Prefer: return=representation
+
+{
+  "name": "my-file-ks",
+  "kind": "file",
+  "description": "This knowledge source uses standard extraction.",
+  "fileParameters": {
+    "ingestionParameters": {
+      "embeddingModel": {
+        "kind": "azureOpenAI",
+        "azureOpenAIParameters": {
+          "resourceUri": "{{aoai-endpoint}}",
+          "deploymentId": "{{aoai-embedding-deployment}}",
+          "modelName": "{{aoai-embedding-model}}"
+        }
+      },
+      "chatCompletionModel": {
+        "kind": "azureOpenAI",
+        "azureOpenAIParameters": {
+          "resourceUri": "{{aoai-endpoint}}",
+          "deploymentId": "{{aoai-gpt-deployment}}",
+          "modelName": "{{aoai-gpt-model}}"
+        }
+      },
+      "contentExtractionMode": "standard",
+      "aiServices": {
+        "uri": "{{foundry-resource-endpoint}}",
+        "apiKey": "{{foundry-resource-key}}"
+      }
+    }
+  }
+}
+```
+
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
+
+::: zone-end
+
+### CORS for file operations
+
+To allow browser-based file operations, set `corsOptions` on the file knowledge source with the trusted origins and maximum preflight cache duration for your application.
+
+> [!IMPORTANT]
+> In the `2026-08-01-preview` API version, `corsOptions` applies to file upload, list, update, and delete endpoints independently of the extraction mode. If you omit `corsOptions`, the file knowledge source has no browser cross-origin policy. CORS doesn't authorize requests. Enabling origins can expose service operations and data in a browser context and introduce security risks. Specify only trusted origins, and don't use a wildcard origin in production. For browser requests, use Microsoft Entra token authentication with the minimum required role. Never expose access tokens or service keys in browser code.
+
 ## Upload files
 
-After the knowledge source exists, upload files directly to it. Each upload is a synchronous call: Azure AI Search extracts content from the uploaded file, chunks the content, creates embeddings when needed, and prepares the extracted content for retrieval before the call returns. You don't have to configure or run a separate ingestion pipeline.
+After you create the knowledge source, upload files directly to it. Each upload is a synchronous call: Azure AI Search extracts content, chunks it, creates embeddings when needed, indexes the chunks, and persists file metadata before the call returns. You don't have to configure or run a separate ingestion pipeline.
+
+For help with errors related to uploading and managing files, see [Troubleshoot file operations](#troubleshoot-file-operations).
+
+### Upload a raw file
 
-The listed `fileName` is taken from the `Content-Disposition: attachment; filename="..."` header on the upload request. REST calls and the .NET SDK set this header directly, while the Python SDK accepts a `filename` parameter and builds the header automatically. If the header isn't set, the service assigns an auto-generated `fileName`.
+For a raw upload, the listed `fileName` comes from the `Content-Disposition: attachment; filename="..."` header. REST calls and the .NET SDK set this header directly, while the Python SDK accepts a `filename` parameter and builds the header automatically. If you don't provide a file name, the service assigns an autogenerated `fileName`.
+
+File names can include a relative path, such as `manuals/installation-guide.pdf`. The service normalizes backslashes to forward slashes. It rejects absolute paths, empty path segments, `.` or `..` segments, colon-containing segments, and invalid file-name characters with HTTP status `400`.
 
 ::: zone pivot="csharp"
 
 ```csharp
-using Azure;
+using Azure.Identity;
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 string fileName = "installation-guide.pdf";
 byte[] fileBytes = await File.ReadAllBytesAsync(fileName);
@@ -279,10 +482,10 @@ Console.WriteLine($"Uploaded file ID: {uploadedFile.FileId}");
 ```python
 from pathlib import Path
 
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 
-index_client = SearchIndexClient(endpoint="search_url", credential=AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint="<search-endpoint>", credential=DefaultAzureCredential())
 
 file_path = Path("installation-guide.pdf")
 uploaded_file = index_client.upload_knowledge_source_file(
@@ -300,22 +503,124 @@ print(f"Uploaded file ID: {uploaded_file.file_id}")
 ::: zone pivot="rest"
 
 ```http
-POST {{search-url}}/knowledgesources/my-file-ks/files?api-version=2026-05-01-preview
-api-key: {{api-key}}
+POST {{search-endpoint}}/knowledgesources/my-file-ks/files?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/octet-stream
 Content-Disposition: attachment; filename="installation-guide.pdf"
 
 <binary file content>
 ```
 
-**Reference:** [Knowledge Sources - Upload File](/rest/api/searchservice/knowledge-sources/upload-file?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Upload File](/rest/api/searchservice/knowledge-sources/upload-file?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
+
+::: zone-end
+
+### Upload a file with optional metadata
+
+Starting with the `2026-08-01-preview` API version, use a multipart request to upload one binary file with optional custom metadata. The request includes exactly one `content` part and an optional JSON `metadata` part.
+
+If both names are specified, `metadata.fileName` takes precedence over the filename on the `content` part. If neither is specified, the service assigns an autogenerated file name.
+
+::: zone pivot="csharp"
+
+```csharp
+using Azure.Identity;
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
+var metadata = new FileUploadMetadata
+{
+  FileName = "installation-guide.pdf",
+  Metadata =
+  {
+    ["department"] = "support",
+    ["product"] = "contoso-100"
+  }
+};
+
+#pragma warning disable SCME0004
+var request = new UploadKnowledgeSourceFileMultipartRequest(
+  metadata,
+  "installation-guide.pdf");
+KnowledgeSourceFile uploadedFile = (await indexClient
+  .UploadKnowledgeSourceFileMultipartAsync("my-file-ks", request)).Value;
+#pragma warning restore SCME0004
+
+Console.WriteLine($"Uploaded file ID: {uploadedFile.FileId}");
+```
+
+**Reference:** [SearchIndexClient.UploadKnowledgeSourceFileMultipartAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient?view=azure-dotnet-preview&preserve-view=true)
+
+::: zone-end
+
+::: zone pivot="python"
+
+```python
+from pathlib import Path
+
+from azure.identity import DefaultAzureCredential
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import (
+  FileUploadMetadata,
+  UploadKnowledgeSourceFileMultipartRequest,
+)
+
+index_client = SearchIndexClient(endpoint="<search-endpoint>", credential=DefaultAzureCredential())
+file_path = Path("installation-guide.pdf")
+request = UploadKnowledgeSourceFileMultipartRequest(
+  metadata=FileUploadMetadata(
+    file_name=file_path.name,
+    metadata={"department": "support", "product": "contoso-100"},
+  ),
+  content=(file_path.name, file_path.read_bytes(), "application/pdf"),
+)
+
+uploaded_file = index_client.upload_knowledge_source_file_multipart(
+  name="my-file-ks",
+  body=request,
+)
+print(f"Uploaded file ID: {uploaded_file.file_id}")
+```
+
+**Reference:** [SearchIndexClient.upload_knowledge_source_file_multipart](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient?view=azure-python-preview&preserve-view=true)
+
+::: zone-end
+
+::: zone pivot="rest"
+
+```http
+POST {{search-endpoint}}/knowledgesources('my-file-ks')/files?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
+Content-Type: multipart/form-data; boundary=file-boundary
+
+--file-boundary
+Content-Disposition: form-data; name="metadata"
+Content-Type: application/json
+
+{
+  "fileName": "installation-guide.pdf",
+  "metadata": {
+    "department": "support",
+    "product": "contoso-100"
+  }
+}
+--file-boundary
+Content-Disposition: form-data; name="content"; filename="installation-guide.pdf"
+Content-Type: application/octet-stream
+
+< ./installation-guide.pdf
+--file-boundary--
+```
+
+**Reference:** [Knowledge Sources - Upload File](/rest/api/searchservice/knowledge-sources/upload-file?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
 > [!NOTE]
 > Uploading a file doesn't replace an existing file, even if you reuse the same `fileName`. Each successful upload creates a new file with its own `fileId`, so the list of uploaded files can contain multiple entries that share a `fileName`.
 >
-> To replace content, delete the prior file by `fileId` before you upload the replacement.
+> With `2026-05-01-preview`, replace content by deleting the prior file and uploading the replacement. With `2026-08-01-preview`, use the update operation.
 
 ## List uploaded files
 
@@ -324,11 +629,11 @@ List files on the knowledge source to inspect the uploaded file set.
 ::: zone pivot="csharp"
 
 ```csharp
-using Azure;
+using Azure.Identity;
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 await foreach (KnowledgeSourceFile file in indexClient.GetKnowledgeSourceFilesAsync("my-file-ks"))
 {
@@ -343,10 +648,10 @@ await foreach (KnowledgeSourceFile file in indexClient.GetKnowledgeSourceFilesAs
 ::: zone pivot="python"
 
 ```python
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 
-index_client = SearchIndexClient(endpoint="search_url", credential=AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint="<search-endpoint>", credential=DefaultAzureCredential())
 
 for file in index_client.list_knowledge_source_files("my-file-ks"):
     print(f"{file.file_name} ({file.file_size_bytes} bytes) error={file.error_message}")
@@ -359,23 +664,23 @@ for file in index_client.list_knowledge_source_files("my-file-ks"):
 ::: zone pivot="rest"
 
 ```http
-GET {{search-url}}/knowledgesources/my-file-ks/files?api-version=2026-05-01-preview
-api-key: {{api-key}}
+GET {{search-endpoint}}/knowledgesources/my-file-ks/files?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 ```
 
-**Reference:** [Knowledge Sources - List Files](/rest/api/searchservice/knowledge-sources/list-files?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - List Files](/rest/api/searchservice/knowledge-sources/list-files?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
-A response includes metadata for each uploaded file. The `errorMessage` value is `null` when the upload is processed without an error.
+The response includes metadata for each uploaded file. Successfully listed files have an `errorMessage` value of `null`.
 
 ```json
 {
   "value": [
     {
       "fileId": "file-abc123",
-      "fileName": "installation-guide.txt",
-      "fileSizeBytes": 89,
+      "fileName": "installation-guide.pdf",
+      "fileSizeBytes": 1048576,
       "createdAt": "2026-05-07T18:10:00Z",
       "lastUpdatedAt": "2026-05-07T18:14:00.803Z",
       "errorMessage": null
@@ -384,9 +689,199 @@ A response includes metadata for each uploaded file. The `errorMessage` value is
 }
 ```
 
-Because uploads are synchronous, a file is ready for retrieval as soon as its upload call succeeds. If processing fails, the upload response and any subsequent list entry include a non-`null` `errorMessage`. Common causes include unsupported file types, extraction failures, model access issues, and quota limits.
+If a new upload fails, the request returns an error and doesn't create a file metadata record. The failed upload doesn't appear in later list results and isn't billed.
+
+If a model access failure occurs and the Foundry resource that hosts the embedding model uses private networking, confirm that the `foundry_account` shared private link is approved and the trusted-services bypass is enabled. A disabled bypass returns `403 Public access is disabled`. For setup details, see [Prerequisites](#prerequisites).
+
+### List and filter files
+
+Starting with the `2026-08-01-preview` API version, use `prefix` to filter files by relative path or `search` to filter by file-name prefix. Set `pageSize` to control the number of results.
+
+::: zone pivot="csharp"
+
+```csharp
+using Azure.Identity;
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
+
+await foreach (KnowledgeSourceFile file in indexClient.GetKnowledgeSourceFilesAsync(
+  "my-file-ks",
+  prefix: "manuals/",
+  pageSize: 100))
+{
+  Console.WriteLine($"{file.FileName} ({file.FileId})");
+}
+```
+
+**Reference:** [SearchIndexClient.GetKnowledgeSourceFilesAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.getknowledgesourcefilesasync?view=azure-dotnet-preview&preserve-view=true)
+
+::: zone-end
+
+::: zone pivot="python"
+
+```python
+from azure.identity import DefaultAzureCredential
+from azure.search.documents.indexes import SearchIndexClient
+
+index_client = SearchIndexClient(endpoint="<search-endpoint>", credential=DefaultAzureCredential())
+
+files = index_client.list_knowledge_source_files(
+  "my-file-ks",
+  prefix="manuals/",
+  page_size=100,
+)
+for file in files:
+  print(f"{file.file_name} ({file.file_id})")
+```
+
+**Reference:** [SearchIndexClient.list_knowledge_source_files](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient?view=azure-python-preview&preserve-view=true#azure-search-documents-indexes-searchindexclient-list-knowledge-source-files)
+
+::: zone-end
+
+::: zone pivot="rest"
+
+```http
+GET {{search-endpoint}}/knowledgesources('my-file-ks')/files?api-version=2026-08-01-preview&prefix=manuals/&pageSize=100
+Authorization: Bearer {{search-access-token}}
+```
+
+**Reference:** [Knowledge Sources - List Files](/rest/api/searchservice/knowledge-sources/list-files?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
+
+::: zone-end
+
+The response includes service-selected parsing and extraction modes, as well as user metadata for file management. User metadata isn't searchable or filterable.
+
+```json
+{
+  "value": [
+    {
+      "fileId": "file-abc123",
+      "fileName": "manuals/installation-guide.md",
+      "prefix": "manuals/",
+      "metadata": {
+        "department": "support",
+        "product": "contoso-100"
+      },
+      "parsingMode": "markdown",
+      "extractionMode": "minimal",
+      "fileSizeBytes": 1048576,
+      "createdAt": "2026-08-03T18:10:00Z",
+      "lastUpdatedAt": "2026-08-03T18:14:00Z",
+      "errorMessage": null
+    }
+  ],
+  "@odata.nextLink": "<service-generated continuation URL>"
+}
+```
+
+To retrieve all results, follow `@odata.nextLink` until it's absent. Send the complete URL exactly as returned, without changing the query parameters.
+
+## Update an uploaded file
+
+Starting with the `2026-08-01-preview` API version, update a file by its `fileId`. The multipart request requires the binary `content` part. The metadata JSON part is optional, so a content-only update is supported. A metadata-only update isn't supported.
+
+::: zone pivot="csharp"
+
+```csharp
+using Azure.Identity;
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
+var metadata = new FileUploadMetadata
+{
+  FileName = "installation-guide.pdf",
+  Metadata =
+  {
+    ["department"] = "support",
+    ["product"] = "contoso-200"
+  }
+};
+
+#pragma warning disable SCME0004
+var request = new UpdateKnowledgeSourceFileRequest(
+  metadata,
+  "installation-guide.pdf");
+KnowledgeSourceFile updatedFile = (await indexClient.UpdateKnowledgeSourceFileAsync(
+  fileId,
+  "my-file-ks",
+  request)).Value;
+#pragma warning restore SCME0004
+
+Console.WriteLine($"Updated file ID: {updatedFile.FileId}");
+```
+
+**Reference:** [SearchIndexClient.UpdateKnowledgeSourceFileAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient?view=azure-dotnet-preview&preserve-view=true)
+
+::: zone-end
+
+::: zone pivot="python"
+
+```python
+from pathlib import Path
+
+from azure.identity import DefaultAzureCredential
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import (
+  FileUploadMetadata,
+  UpdateKnowledgeSourceFileRequest,
+)
+
+index_client = SearchIndexClient(endpoint="<search-endpoint>", credential=DefaultAzureCredential())
+file_path = Path("installation-guide.pdf")
+request = UpdateKnowledgeSourceFileRequest(
+  metadata=FileUploadMetadata(
+    file_name=file_path.name,
+    metadata={"department": "support", "product": "contoso-200"},
+  ),
+  content=(file_path.name, file_path.read_bytes(), "application/pdf"),
+)
+
+updated_file = index_client.update_knowledge_source_file(
+  name="my-file-ks",
+  file_id=file_id,
+  body=request,
+)
+print(f"Updated file ID: {updated_file.file_id}")
+```
+
+**Reference:** [SearchIndexClient.update_knowledge_source_file](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient?view=azure-python-preview&preserve-view=true)
+
+::: zone-end
+
+::: zone pivot="rest"
+
+```http
+PUT {{search-endpoint}}/knowledgesources('my-file-ks')/files('{{file-id}}')?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
+Content-Type: multipart/form-data; boundary=file-boundary
+
+--file-boundary
+Content-Disposition: form-data; name="metadata"
+Content-Type: application/json
+
+{
+  "fileName": "installation-guide.pdf",
+  "metadata": {
+    "department": "support",
+    "product": "contoso-200"
+  }
+}
+--file-boundary
+Content-Disposition: form-data; name="content"; filename="installation-guide.pdf"
+Content-Type: application/octet-stream
+
+< ./installation-guide.pdf
+--file-boundary--
+```
+
+**Reference:** [Knowledge Sources - Update File](/rest/api/searchservice/knowledge-sources/update-file?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
+
+::: zone-end
 
-If a model access failure occurs and the Foundry resource that hosts the embedding model uses private networking, confirm that the `openai_account` shared private link is approved and the trusted-services bypass is enabled. A disabled bypass returns `403 Public access is disabled`. For setup details, see [Prerequisites](#prerequisites).
+If an update fails, the previous metadata record remains. Don't assume that an update changes indexed content transactionally.
 
 ## Delete uploaded files
 
@@ -395,10 +890,10 @@ Delete files from the knowledge source when you no longer want them available fo
 ::: zone pivot="csharp"
 
 ```csharp
-using Azure;
+using Azure.Identity;
 using Azure.Search.Documents.Indexes;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 await indexClient.DeleteKnowledgeSourceFileAsync("my-file-ks", "file-abc123");
 ```
@@ -410,10 +905,10 @@ await indexClient.DeleteKnowledgeSourceFileAsync("my-file-ks", "file-abc123");
 ::: zone pivot="python"
 
 ```python
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 
-index_client = SearchIndexClient(endpoint="search_url", credential=AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint="<search-endpoint>", credential=DefaultAzureCredential())
 
 index_client.delete_knowledge_source_file("my-file-ks", "file-abc123")
 ```
@@ -425,11 +920,11 @@ index_client.delete_knowledge_source_file("my-file-ks", "file-abc123")
 ::: zone pivot="rest"
 
 ```http
-DELETE {{search-url}}/knowledgesources/my-file-ks/files/file-abc123?api-version=2026-05-01-preview
-api-key: {{api-key}}
+DELETE {{search-endpoint}}/knowledgesources/my-file-ks/files/file-abc123?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 ```
 
-**Reference:** [Knowledge Sources - Delete File](/rest/api/searchservice/knowledge-sources/delete-file?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Delete File](/rest/api/searchservice/knowledge-sources/delete-file?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
@@ -445,9 +940,20 @@ After the knowledge base is configured, [call the retrieve action or MCP endpoin
 
 [!INCLUDE [Delete a knowledge source](includes/how-tos/knowledge-source-delete.md)]
 
+## Troubleshoot file operations
+
+The following status codes are specific to file knowledge source operations.
+
+| Status code | Cause and action |
+| -- | -- |
+| `400` | The file is empty, contains no extractable text, has an unsafe relative path, or has an invalid continuation request. Verify the file has supported, readable content and a valid file name. For list operations, follow `@odata.nextLink` exactly as returned. Don't combine `$skiptoken` with `search` or `pageSize`. |
+| `409` | The file knowledge source reached the file limit for the API version. Delete files before uploading more. |
+| `415` | The service detected an unsupported MIME type, or it detected an image while the knowledge source uses minimal extraction. Use a supported format. For images, use standard extraction. Changing only the caller-provided content type doesn't override detection. |
+| `429` | The processing queue is full. Use bounded parallelism and retry with exponential backoff. The service doesn't guarantee a `Retry-After` header. |
+| `504` | Processing exceeded 180 seconds during file upload or update. Reduce the file size or complexity and try again. |
+
 ## Related content
 
-+ [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
 + [What is a knowledge source?](agentic-knowledge-source-overview.md)
 + [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md)
 + [Query a knowledge base](agentic-retrieval-how-to-retrieve.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイル知識ソースに関する更新"
}
```

### Explanation
この変更は、Azure AI Searchでのファイル知識ソースの作成方法に関するドキュメントを更新するものです。主に、API バージョンが `2026-05-01-preview` から `2026-08-01-preview` に更新され、新機能が追加され、説明が明確化されました。さらに、ファイルのアップロードや管理に関する手順が詳細に記述されています。

具体的な変更点は以下のとおりです：

1. **API バージョンの更新**：REST API のバージョンが新しいものに変更され、それに伴い利用可能な機能が拡張されています。特に `standard` 抽出モードなどの新機能が追加されました。
   
2. **ドキュメントの明確化**：ファイルのアップロードや管理に関連する情報が整理されており、特にファイルのサポート形式、制限、認証のやり方についての説明が強化されています。

3. **サンプルコードの更新**：C# および Python のコード例が新しい API バージョンに合うように更新され、`AzureKeyCredential` から `DefaultAzureCredential` に変更されています。これにより、よりセキュアな方法での認証が推奨されています。

4. **アップロードのプロセス改善**：ファイルのアップロードについてより詳細な手順が追加され、エラーハンドリングのガイダンスも示されています。特に、失敗したアップロードがどのように扱われるか、エラーメッセージがどのように解釈されるべきかについても言及されています。

これらの更新により、ユーザーはファイル知識ソースを利用してAzure AI Searchでのデータのアップロードと処理を行う際に、より明確で具体的な指針を得ることができます。

## articles/search/agentic-knowledge-source-how-to-mcp-server.md{#item-9a2e92}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,8 @@ title: Create an MCP Server Knowledge Source
 description: Learn how to create an MCP Server knowledge source for agentic retrieval in Azure AI Search, which connects to any external Model Context Protocol server.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/02/2026
+ms.date: 08/17/2026
+ms.custom: doc-kit-assisted
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
@@ -13,9 +14,9 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -31,8 +32,8 @@ Unlike indexed knowledge sources, MCP Server knowledge sources query live data d
 
 ### Usage support
 
-| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-08-01-preview&preserve-view=true) |
+| -- | -- | -- | -- | -- | -- | -- |
 | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
@@ -41,23 +42,29 @@ Unlike indexed knowledge sources, MCP Server knowledge sources query live data d
 
 + An MCP server with one or more tools. The server must be reachable from Azure AI Search over HTTPS. For testing, you can use the public Microsoft Learn MCP server at `https://learn.microsoft.com/api/mcp`.
 
-+ Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Permission to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 ::: zone pivot="csharp"
 
 + The latest [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
+
 ::: zone-end
 
 ::: zone pivot="python"
 
 + The latest [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) preview package: `pip install --pre azure-search-documents`
 
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
+
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
++ The [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) version of the Search Service REST API.
+
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
@@ -80,15 +87,16 @@ The following JSON is an example response for an MCP Server knowledge source.
   "name": "my-mcp-server-ks",
   "kind": "mcpServer",
   "description": "An MCP Server knowledge source.",
+  "resultsProcessing": "rerank",
   "encryptionKey": null,
   "mcpServerParameters": {
     "serverURL": "https://learn.microsoft.com/api/mcp",
     "authentication": null,
     "tools": [
       {
         "name": "microsoft_docs_search",
-        "inclusionMode": null,
-        "maxOutputTokens": null,
+        "resultsProcessing": "none",
+        "maxOutputTokens": 1000,
         "outputParsing": {
           "kind": "auto",
           "jsonParameters": null,
@@ -107,16 +115,16 @@ Run the following code to create an MCP Server knowledge source.
 ::: zone pivot="csharp"
 
 ```csharp
-using Azure;
+using Azure.Identity;
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 
-Uri searchEndpoint = new Uri("<search-service-url>");
-AzureKeyCredential credential = new AzureKeyCredential("<api-key>");
+Uri searchEndpoint = new Uri("<search-endpoint>");
+DefaultAzureCredential credential = new DefaultAzureCredential();
 var indexClient = new SearchIndexClient(searchEndpoint, credential);
 
 var mcpServer = new McpServerKnowledgeSource(
-    "<knowledge-source-name>",
+    "my-mcp-server-ks",
     new McpServerKnowledgeSourceParameters(
         "https://learn.microsoft.com/api/mcp",
         new[]
@@ -125,12 +133,13 @@ var mcpServer = new McpServerKnowledgeSource(
             {
                 Name = "microsoft_docs_search",
                 OutputParsing = new McpServerAutoOutputParsing(),
-                InclusionMode = McpServerToolInclusionMode.Reranked,
+                ResultsProcessing = KnowledgeSourceResultsProcessing.None,
                 MaxOutputTokens = 1000
             }
         }))
 {
-    Description = "An MCP Server knowledge source."
+    Description = "An MCP Server knowledge source.",
+    ResultsProcessing = KnowledgeSourceResultsProcessing.Rerank
 };
 
 await indexClient.CreateOrUpdateKnowledgeSourceAsync(mcpServer);
@@ -143,56 +152,67 @@ await indexClient.CreateOrUpdateKnowledgeSourceAsync(mcpServer);
 ::: zone pivot="python"
 
 ```python
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import (
+    McpServerAutoOutputParsing,
     McpServerKnowledgeSource,
-    McpServerParameters,
+    McpServerKnowledgeSourceParameters,
     McpServerTool,
-    McpServerToolOutputParsing,
 )
 
 index_client = SearchIndexClient(
-    endpoint="<search-service-url>",
-    credential=AzureKeyCredential("<api-key>")
+    endpoint="<search-endpoint>",
+    credential=DefaultAzureCredential(),
 )
 
 knowledge_source = McpServerKnowledgeSource(
-    name="<knowledge-source-name>",
+    name="my-mcp-server-ks",
     description="An MCP Server knowledge source.",
-    mcp_server_parameters=McpServerParameters(
+    results_processing="rerank",
+    mcp_server_parameters=McpServerKnowledgeSourceParameters(
         server_url="https://learn.microsoft.com/api/mcp",
         tools=[
             McpServerTool(
                 name="microsoft_docs_search",
-                output_parsing=McpServerToolOutputParsing(kind="auto"),
-                inclusion_mode="reranked",
-                max_output_tokens=1000
+                output_parsing=McpServerAutoOutputParsing(),
+                results_processing="none",
+                max_output_tokens=1000,
             )
-        ]
-    )
+        ],
+    ),
 )
 
 index_client.create_or_update_knowledge_source(knowledge_source)
+
+saved_source = index_client.get_knowledge_source(
+    knowledge_source.name
+)
+assert saved_source.results_processing == "rerank"
+assert (
+    saved_source.mcp_server_parameters.tools[0].results_processing
+    == "none"
+)
 ```
 
-**Reference:** [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient?view=azure-python-preview&preserve-view=true)
+**Reference:** [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient?view=azure-python-preview&preserve-view=true), [McpServerKnowledgeSource](/python/api/azure-search-documents/azure.search.documents.indexes.models.mcpserverknowledgesource?view=azure-python-preview&preserve-view=true), [McpServerTool](/python/api/azure-search-documents/azure.search.documents.indexes.models.mcpservertool?view=azure-python-preview&preserve-view=true)
 
 ::: zone-end
 
 ::: zone pivot="rest"
 
 ```http
 ### Create an MCP Server knowledge source
-PUT {{search-url}}/knowledgesources/my-mcp-server-ks?api-version=2026-05-01-preview
-api-key: {{api-key}}
+PUT {{search-endpoint}}/knowledgesources/my-mcp-server-ks?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 Prefer: return=representation
 
 {
   "name": "my-mcp-server-ks",
   "kind": "mcpServer",
   "description": "An MCP Server knowledge source.",
+  "resultsProcessing": "rerank",
   "encryptionKey": null,
   "mcpServerParameters": {
     "serverURL": "https://learn.microsoft.com/api/mcp",
@@ -202,15 +222,15 @@ Prefer: return=representation
         "outputParsing": {
           "kind": "auto"
         },
-        "inclusionMode": "reranked",
+        "resultsProcessing": "none",
         "maxOutputTokens": 1000
       }
     ]
   }
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
@@ -226,7 +246,7 @@ Use `foundryConnection` only when an agent from Foundry Agent Service invokes a
 "authentication": {
   "kind": "foundryConnection",
   "foundryConnectionParameters": {
-    "connectionId": "<your-foundry-connection-id>"
+    "connectionId": "<foundry-connection-id>"
   }
 }
 ```
@@ -240,7 +260,7 @@ Use `storedHeaders` to send static HTTP headers with every MCP request. We recom
   "kind": "storedHeaders",
   "storedHeadersParameters": {
     "headers": {
-      "x-custom-auth": "<your-header-value>"
+      "x-custom-auth": "<header-value>"
     }
   }
 }
@@ -258,7 +278,7 @@ If an MCP server requires per-request credentials, pass them on the retrieve req
 Use the knowledge source name as the prefix:
 
 | Control header | Description |
-|--|--|
+| -- | -- |
 | `<knowledge-source-name>-header-name<N>` | The name of the HTTP header to send to the MCP server. |
 | `<knowledge-source-name>-header-value<N>` | The value of the HTTP header to send to the MCP server. |
 
@@ -269,7 +289,7 @@ Use the knowledge source name as the prefix:
 Create the retrieval client with a policy that adds the control headers to the retrieve request.
 
 ```csharp
-using Azure;
+using Azure.Identity;
 using Azure.Core;
 using Azure.Core.Pipeline;
 using Azure.Search.Documents;
@@ -357,7 +377,7 @@ result = retrieval_client.retrieve(
 ::: zone pivot="rest"
 
 ```http
-POST {{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2026-05-01-preview
+POST {{search-endpoint}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2026-08-01-preview
 Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 my-mcp-server-ks-header-name: Authorization
@@ -392,7 +412,11 @@ Each header pair must include exactly one name control header and one matching v
 
 ### Configure tools
 
-Each entry in the `tools` array specifies an allowed MCP tool and optional output parsing behavior.
+Each entry in the `tools` array specifies an allowed MCP tool, optional output parsing behavior, and how the tool's results are processed.
+
+Use `resultsProcessing` to control whether the retrieval engine reranks a tool's results. Valid values are `rerank` and `none`. For mappings from earlier contracts, see [Migrate agentic retrieval code to the latest version](agentic-retrieval-how-to-migrate.md).
+
+For each MCP tool, the service resolves `resultsProcessing` in this order: the tool value, the request value in `knowledgeSourceParams`, the stored knowledge source value, and then `rerank`. A tool value applies only to that tool.
 
 ### Output parsing modes
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MCPサーバー知識ソースの更新"
}
```

### Explanation
この変更は、Azure AI SearchのMCP（Model Context Protocol）サーバー知識ソースに関するドキュメントのアップデートを反映しています。主な目的は、APIのバージョンを新しいものに更新し、さまざまな機能や設定が強化されたことにあります。

具体的な変更点は以下のとおりです：

1. **API バージョンの変更**：REST APIのバージョンが `2026-05-01-preview` から `2026-08-01-preview` に更新され、これにより新たな機能や改善が可能になっています。

2. **機能の追加**：MCPサーバー知識ソースにおいて、ツールの結果の処理方法を制御する `resultsProcessing` オプションが追加されました。これにより、結果の再ランキングやその他の処理が柔軟に設定できるようになりました。

3. **ドキュメントの明確化**：認証やツール設定に関する情報が整理され、ユーザーがMCPサーバー知識ソースを構成する際のガイダンスが強化されています。また、従来の契約からのマイグレーションに関する参考も追加されました。

4. **サンプルコードの更新**：C# および Python のサンプルコードが新しいAPIに合うように更新され、特に認証方法が `AzureKeyCredential` から `DefaultAzureCredential` に変更されており、より安全でモダンな認証が推奨されています。

これらの改訂を通じて、ユーザーはMCPサーバー知識ソースの使用や設定に関して、より明確で実用的な情報を得ることができるようになります。特に新しい機能や設定の追加により、システムの柔軟性と拡張性が向上しています。

## articles/search/agentic-knowledge-source-how-to-onelake.md{#item-ec7a80}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to create an indexed OneLake knowledge source that define
 ms.service: azure-ai-search
 ms.custom: [ignite-2025, doc-kit-assisted]
 ms.topic: how-to
-ms.date: 08/08/2026
+ms.date: 08/14/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
@@ -16,11 +16,11 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [GA feature](./includes/previews/agentic-retrieval-ga-feature.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -40,7 +40,7 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 ### Usage support
 
 | [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources) |
-|--|--|--|--|--|--|--|
+| -- | -- | -- | -- | -- | -- | -- |
 | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
@@ -53,40 +53,50 @@ The generated indexer conforms to the *OneLake indexer*, whose prerequisites, su
 
 + If `contentExtractionMode` is `standard`, use a Microsoft Foundry resource in a [region supported by Content Understanding in Foundry Tools](/azure/ai-services/content-understanding/language-region-support) and the `https://<resource-name>.services.ai.azure.com` endpoint. Deploy an embedding model, and deploy a multimodal chat model if you enable image verbalization.
 
-+ Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Permission to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 + If the knowledge source specifies an Azure OpenAI model for embeddings or image verbalization, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource.
 
 ::: zone pivot="csharp"
 
 + Required [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) package:
 
-  + For 2026-05-01-preview features, the latest preview package: `dotnet add package Azure.Search.Documents --prerelease`
+  + For `2026-08-01-preview` features, the latest preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
-  + For 2026-04-01 features, the latest stable package: `dotnet add package Azure.Search.Documents`
+  + For `2026-04-01` features, the latest stable package: `dotnet add package Azure.Search.Documents`
+
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
 
 ::: zone-end
 
 ::: zone pivot="python"
 
 + Required [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) package:
 
-  + For 2026-05-01-preview features, the latest preview package: `pip install --pre azure-search-documents`
+  + For `2026-08-01-preview` features, the latest preview package: `pip install --pre azure-search-documents`
+
+  + For `2026-04-01` features, the latest stable package: `pip install azure-search-documents`
 
-  + For 2026-04-01 features, the latest stable package: `pip install azure-search-documents`
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
 
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ Required REST API version:
++ Required Search Service REST API version:
+
+  + For preview features: [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
-  + For preview features: [Search Service 2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+  + For generally available features: [2026-04-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true)
 
-  + For generally available features: [Search Service 2026-04-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true)
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
+## Limitations
+
+Private synchronization isn't supported for indexed OneLake knowledge sources. Keep `networkAccessMode` set to `public`.
+
 ## Check for existing knowledge sources
 
 [!INCLUDE [Check for existing knowledge sources](includes/how-tos/knowledge-source-check.md)]
@@ -113,23 +123,20 @@ The following JSON is an example response for an indexed OneLake knowledge sourc
         "azureOpenAIParameters": {
           "resourceUri": "<REDACTED>",
           "deploymentId": "text-embedding-3-large",
-          "apiKey": "<REDACTED>",
           "modelName": "text-embedding-3-large"
         }
       },
       "chatCompletionModel": {
         "kind": "azureOpenAI",
         "azureOpenAIParameters": {
-          "resourceUri": "<your-foundry-resource-endpoint>",
+          "resourceUri": "<aoai-endpoint>",
           "deploymentId": "gpt-5-mini",
-          "apiKey": "<REDACTED>",
           "modelName": "gpt-5-mini"
         }
       },
       "ingestionSchedule": null,
       "aiServices": {
-        "uri": "<your-foundry-resource-endpoint>",
-        "apiKey": "<REDACTED>"
+        "uri": "<aoai-endpoint>",
       }
     },
     "createdResources": {
@@ -148,16 +155,17 @@ Run the following code to create an indexed OneLake knowledge source.
 
 ::: zone pivot="csharp"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```csharp
 // Create an indexed OneLake knowledge source
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
+using Azure.Search.Documents.KnowledgeBases.Models;
 using Azure.Search.Documents.Models;
-using Azure;
+using Azure.Identity;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var chatCompletionParams = new AzureOpenAIVectorizerParameters
 {
@@ -175,6 +183,7 @@ var embeddingParams = new AzureOpenAIVectorizerParameters
 
 var ingestionParams = new KnowledgeSourceIngestionParameters
 {
+    NetworkAccessMode = KnowledgeSourceNetworkAccessMode.Public,
     DisableImageVerbalization = false,
     ChatCompletionModel = new KnowledgeBaseAzureOpenAIModel(azureOpenAIParameters: chatCompletionParams),
     EmbeddingModel = new KnowledgeSourceAzureOpenAIVectorizer
@@ -215,9 +224,9 @@ Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 using Azure.Search.Documents.KnowledgeBases.Models;
-using Azure;
+using Azure.Identity;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var chatCompletionParams = new AzureOpenAIVectorizerParameters
 {
@@ -269,15 +278,16 @@ Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated
 
 ::: zone pivot="python"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```python
 # Create an indexed OneLake knowledge source
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import IndexedOneLakeKnowledgeSource, IndexedOneLakeKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceAzureOpenAIVectorizer, KnowledgeSourceContentExtractionMode, KnowledgeSourceIngestionParameters
+from azure.search.documents.knowledgebases.models import KnowledgeSourceNetworkAccessMode
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
 knowledge_source = IndexedOneLakeKnowledgeSource(
     name = "my-onelake-ks",
@@ -288,22 +298,21 @@ knowledge_source = IndexedOneLakeKnowledgeSource(
         lakehouse_id = "lakehouse_id",
         target_path = None,
         ingestion_parameters = KnowledgeSourceIngestionParameters(
+            network_access_mode = KnowledgeSourceNetworkAccessMode.PUBLIC,
             identity = None,
             disable_image_verbalization = False,
             chat_completion_model = KnowledgeBaseAzureOpenAIModel(
                 azure_open_ai_parameters = AzureOpenAIVectorizerParameters(
-                    resource_url = "aoai_endpoint",
-                    deployment_name = "aoai_gpt_deployment",
-                    model_name = "aoai_gpt_model",
-                    api_key = "aoai_api_key"
+                    resource_url = "<aoai-endpoint>",
+                    deployment_name = "<aoai-gpt-deployment>",
+                    model_name = "<aoai-gpt-model>",
                 )
             ),
             embedding_model = KnowledgeSourceAzureOpenAIVectorizer(
                 azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
-                    resource_url = "aoai_endpoint",
-                    deployment_name = "aoai_embedding_deployment",
-                    model_name = "aoai_embedding_model",
-                    api_key = "aoai_api_key"
+                    resource_url = "<aoai-endpoint>",
+                    deployment_name = "<aoai-embedding-deployment>",
+                    model_name = "<aoai-embedding-model>",
                 )
             ),
             content_extraction_mode = KnowledgeSourceContentExtractionMode.MINIMAL,
@@ -323,12 +332,12 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 
 ```python
 # Create an indexed OneLake knowledge source
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import IndexedOneLakeKnowledgeSource, IndexedOneLakeKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceContentExtractionMode
 from azure.search.documents.knowledgebases.models import KnowledgeSourceIngestionParameters, KnowledgeSourceAzureOpenAIVectorizer
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
 knowledge_source = IndexedOneLakeKnowledgeSource(
     name = "my-onelake-ks",
@@ -343,18 +352,16 @@ knowledge_source = IndexedOneLakeKnowledgeSource(
             disable_image_verbalization = False,
             chat_completion_model = KnowledgeBaseAzureOpenAIModel(
                 azure_open_ai_parameters = AzureOpenAIVectorizerParameters(
-                    resource_url = "aoai_endpoint",
-                    deployment_name = "aoai_gpt_deployment",
-                    model_name = "aoai_gpt_model",
-                    api_key = "aoai_api_key"
+                    resource_url = "<aoai-endpoint>",
+                    deployment_name = "<aoai-gpt-deployment>",
+                    model_name = "<aoai-gpt-model>",
                 )
             ),
             embedding_model = KnowledgeSourceAzureOpenAIVectorizer(
                 azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
-                    resource_url = "aoai_endpoint",
-                    deployment_name = "aoai_embedding_deployment",
-                    model_name = "aoai_embedding_model",
-                    api_key = "aoai_api_key"
+                    resource_url = "<aoai-endpoint>",
+                    deployment_name = "<aoai-embedding-deployment>",
+                    model_name = "<aoai-embedding-model>",
                 )
             ),
             content_extraction_mode = KnowledgeSourceContentExtractionMode.MINIMAL,
@@ -375,23 +382,24 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 
 ::: zone pivot="rest"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```http
 ### Create an indexed OneLake knowledge source
-PUT {{search-url}}/knowledgesources/my-onelake-ks?api-version=2026-05-01-preview
-Authorization: Bearer {{token}}
+PUT {{search-endpoint}}/knowledgesources/my-onelake-ks?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 
 {
     "name": "my-onelake-ks",
     "kind": "indexedOneLake",
     "description": "This knowledge source pulls content from a lakehouse.",
     "indexedOneLakeParameters": {
-      "fabricWorkspaceId": "<YOUR FABRIC WORKSPACE GUID>",
-      "lakehouseId": "<YOUR LAKEHOUSE GUID>",
+      "fabricWorkspaceId": "<fabric-workspace-id>",
+      "lakehouseId": "<lakehouse-id>",
       "targetPath": null,
       "ingestionParameters": {
+        "networkAccessMode": "public",
         "identity": null,
         "disableImageVerbalization": null,
         "chatCompletionModel": {
@@ -418,23 +426,23 @@ Content-Type: application/json
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 # [2026-04-01](#tab/2026-04-01)
 
 ```http
 ### Create an indexed OneLake knowledge source
-PUT {{search-url}}/knowledgesources/my-onelake-ks?api-version=2026-04-01
-Authorization: Bearer {{token}}
+PUT {{search-endpoint}}/knowledgesources/my-onelake-ks?api-version=2026-04-01
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 
 {
     "name": "my-onelake-ks",
     "kind": "indexedOneLake",
     "description": "This knowledge source pulls content from a lakehouse.",
     "indexedOneLakeParameters": {
-      "fabricWorkspaceId": "<YOUR FABRIC WORKSPACE GUID>",
-      "lakehouseId": "<YOUR LAKEHOUSE GUID>",
+      "fabricWorkspaceId": "<fabric-workspace-id>",
+      "lakehouseId": "<lakehouse-id>",
       "targetPath": null,
       "ingestionParameters": {
         "identity": null,
@@ -469,7 +477,7 @@ Content-Type: application/json
 ::: zone-end
 
 > [!NOTE]
-> Document-level permissions enforcement using `ingestionPermissionOptions` requires the 2026-05-01-preview API version. 2026-04-01 doesn't support this feature.
+> To enforce document-level permissions with `ingestionPermissionOptions`, use the 2026-08-01-preview API version. The 2026-04-01 API version doesn't support this feature.
 
 ## Check ingestion status
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLake知識ソースの更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるOneLake知識ソースの作成方法に関するドキュメントを更新するものです。主に、APIのバージョンが `2026-05-01-preview` から `2026-08-01-preview` に更新され、新機能や明確化が含まれています。

具体的な変更点は以下のとおりです：

1. **API バージョンの更新**：REST APIのバージョンが新しいものに更新され、それに伴って新機能が利用可能になっています。特に、新しいAPIバージョンでは、サービス間の接続やデータ処理方法が改善されています。

2. **ドキュメントの明確化**：重要な情報や注意事項が整理され、OneLake知識ソースに関連する技術的な要件や制限事項が明記されています。特に、推奨される認証方法や必要な権限に関する説明が強化されています。

3. **サンプルコードの更新**：C# および Python のコード例が新しいAPI仕様に合わせて修正され、特に認証方法が `AzureKeyCredential` から `DefaultAzureCredential` に変更されており、よりセキュアな実装が推奨されています。これにより、開発者はより安全にAzureのサービスに接続できるようになります。

4. **新機能の追加**：`networkAccessMode` の設定に関する情報が追加され、`public` モードが強調されています。また、ドキュメントレベルの権限を強制する機能に関する情報も更新されています。

これらの変更により、ユーザーはOneLake知識ソースを利用する際の手順や設定に関して、より分かりやすい情報を得ることができ、システムを効果的に活用できるようになります。

## articles/search/agentic-knowledge-source-how-to-search-index.md{#item-09d366}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Create a Search Index Knowledge Source
 description: Learn how to create a search index knowledge source, which specifies an index used by a knowledge base for agentic retrieval workloads.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 07/07/2026
+ms.date: 08/14/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
@@ -15,9 +15,9 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [GA feature](./includes/previews/agentic-retrieval-ga-feature.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -28,7 +28,7 @@ A *search index knowledge source* connects an existing Azure AI Search index, in
 ### Usage support
 
 | [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources) |
-|--|--|--|--|--|--|--|
+| -- | -- | -- | -- | -- | -- | -- |
 | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
@@ -37,35 +37,41 @@ A *search index knowledge source* connects an existing Azure AI Search index, in
 
 + A search index containing plain text or vector content with a semantic configuration. [Review the index criteria for agentic retrieval](agentic-retrieval-how-to-create-index.md#criteria-for-agentic-retrieval). The index must be on the same search service as the knowledge base.
 
-+ Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Permission to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 ::: zone pivot="csharp"
 
 + Required [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) package:
 
-  + For 2026-05-01-preview features, the latest preview package: `dotnet add package Azure.Search.Documents --prerelease`
+  + For `2026-08-01-preview` features, the latest preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
-  + For 2026-04-01 features, the latest stable package: `dotnet add package Azure.Search.Documents`
+  + For `2026-04-01` features, the latest stable package: `dotnet add package Azure.Search.Documents`
+
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
 
 ::: zone-end
 
 ::: zone pivot="python"
 
 + Required [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) package:
 
-  + For 2026-05-01-preview features, the latest preview package: `pip install --pre azure-search-documents`
+  + For `2026-08-01-preview` features, the latest preview package: `pip install --pre azure-search-documents`
+
+  + For `2026-04-01` features, the latest stable package: `pip install azure-search-documents`
 
-  + For 2026-04-01 features, the latest stable package: `pip install azure-search-documents`
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
 
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ Required REST API version:
++ Required Search Service REST API version:
+
+  + For preview features: [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
-  + For preview features: [Search Service 2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+  + For generally available features: [2026-04-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true)
 
-  + For generally available features: [Search Service 2026-04-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true)
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
@@ -98,17 +104,20 @@ The following JSON is an example response for a search index knowledge source. N
 
 Run the following code to create a search index knowledge source.
 
+> [!NOTE]
+> Starting with the `2026-05-01-preview` API version, `semanticConfigurationName` is optional on search index knowledge sources. Earlier API versions still require `semanticConfigurationName`. If your knowledge source needs to support both older and newer API versions, keep specifying `semanticConfigurationName`.
+
 ::: zone pivot="csharp"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```csharp
 // Create a search index knowledge source
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
-using Azure;
+using Azure.Identity;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var indexKnowledgeSource = new SearchIndexKnowledgeSource(
     name: knowledgeSourceName,
@@ -131,9 +140,9 @@ Console.WriteLine($"Knowledge source '{knowledgeSourceName}' created or updated
 // Create a search index knowledge source
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
-using Azure;
+using Azure.Identity;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var indexKnowledgeSource = new SearchIndexKnowledgeSource(
     name: knowledgeSourceName,
@@ -157,23 +166,22 @@ Console.WriteLine($"Knowledge source '{knowledgeSourceName}' created or updated
 
 ::: zone pivot="python"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```python
 # Create a search index knowledge source
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import SearchIndexKnowledgeSource, SearchIndexKnowledgeSourceParameters, SearchIndexFieldReference
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
 knowledge_source = SearchIndexKnowledgeSource(
     name = "my-search-index-ks",
     description= "This knowledge source pulls from an existing index designed for agentic retrieval.",
     encryption_key = None,
     search_index_parameters = SearchIndexKnowledgeSourceParameters(
         search_index_name = "search_index_name",
-        semantic_configuration_name = "semantic_configuration_name",
         source_data_fields = [
             SearchIndexFieldReference(name="description"),
             SearchIndexFieldReference(name="category"),
@@ -194,11 +202,11 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 
 ```python
 # Create a search index knowledge source
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import SearchIndexKnowledgeSource, SearchIndexKnowledgeSourceParameters, SearchIndexFieldReference
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
 knowledge_source = SearchIndexKnowledgeSource(
     name = "my-search-index-ks",
@@ -229,12 +237,12 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 
 ::: zone pivot="rest"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```http
 ### Create a search index knowledge source
-PUT {{search-url}}/knowledgesources/my-search-index-ks?api-version=2026-05-01-preview
-api-key: {{api-key}}
+PUT {{search-endpoint}}/knowledgesources/my-search-index-ks?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 
 {
@@ -243,8 +251,7 @@ Content-Type: application/json
     "description": "This knowledge source pulls from an existing index designed for agentic retrieval.",
     "encryptionKey": null,
     "searchIndexParameters": {
-        "searchIndexName": "<YOUR INDEX NAME>",
-        "semanticConfigurationName": "my-semantic-config",
+        "searchIndexName": "<index-name>",
         "sourceDataFields": [
           { "name": "description" },
           { "name": "category" }
@@ -253,14 +260,14 @@ Content-Type: application/json
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 # [2026-04-01](#tab/2026-04-01)
 
 ```http
 ### Create a search index knowledge source
-PUT {{search-url}}/knowledgesources/my-search-index-ks?api-version=2026-04-01
-api-key: {{api-key}}
+PUT {{search-endpoint}}/knowledgesources/my-search-index-ks?api-version=2026-04-01
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 
 {
@@ -269,7 +276,7 @@ Content-Type: application/json
     "description": "This knowledge source pulls from an existing index designed for agentic retrieval.",
     "encryptionKey": null,
     "searchIndexParameters": {
-        "searchIndexName": "<YOUR INDEX NAME>",
+        "searchIndexName": "<index-name>",
         "semanticConfigurationName": "my-semantic-config",
         "sourceDataFields": [
           { "name": "description" },
@@ -288,14 +295,11 @@ Content-Type: application/json
 ### Persist a base filter on a knowledge source (preview)
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
-
-In the `2026-05-01-preview` API, a search index knowledge source can persist a default filter through the `baseFilter` property. Use `baseFilter` when the same filter expression should apply to every retrieve request that uses the knowledge source, so callers don't have to repeat the filter on every call.
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 
-> [!NOTE]
-> Starting with `2026-05-01-preview`, `semanticConfigurationName` is optional on search index knowledge sources. The examples in this section omit it. Earlier API versions still require `semanticConfigurationName`. If your knowledge source needs to support both the older and newer API versions, keep specifying it.
+Starting with the `2026-05-01-preview` API version, a search index knowledge source can persist a default filter through the `baseFilter` property. Use `baseFilter` when the same filter expression should apply to every retrieve request that uses the knowledge source, so callers don't have to repeat the filter on every call.
 
-The following example stores a base filter on a search index knowledge source:
+The following example stores a base filter on a search index knowledge source.
 
 ::: zone pivot="csharp"
 
@@ -336,9 +340,9 @@ index_client.create_or_update_knowledge_source(knowledge_source)
 ::: zone pivot="rest"
 
 ```http
-PUT {{search-url}}/knowledgesources/public-docs-ks?api-version=2026-05-01-preview
+PUT {{search-endpoint}}/knowledgesources/public-docs-ks?api-version=2026-08-01-preview
 Content-Type: application/json
-api-key: {{search-api-key}}
+Authorization: Bearer {{search-access-token}}
 
 {
   "name": "public-docs-ks",
@@ -350,7 +354,7 @@ api-key: {{search-api-key}}
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
@@ -409,6 +413,186 @@ baseFilter AND filterAddOn
 
 Because the filters are combined with `AND`, `filterAddOn` can only narrow the persisted base filter. It can't replace or broaden it.
 
+### Configure query hints (preview)
+
+Starting with the `2026-08-01-preview` API version, query hints guide the query-planning model to generate filters and ranking boosts from a user's request. Store default hints in `searchIndexParameters.queryHints`, which can hold both filters and boosts.
+
+The following example stores one filter hint and one `fieldValue` boost on a knowledge source for `product-docs-index`, which has a filterable `productFamily` field and a searchable `language` field.
+
+::: zone pivot="csharp"
+
+```csharp
+using System;
+using Azure.Identity;
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+
+var endpoint = new Uri("<search-endpoint>");
+var indexClient = new SearchIndexClient(
+    endpoint,
+    new DefaultAzureCredential());
+
+var queryHints = new SearchIndexKnowledgeSourceQueryHints();
+queryHints.Filters.Add(
+    new SearchIndexKnowledgeSourceFilterHint(
+        "productFamily",
+        ["Model-X100", "Model-X200"])
+    {
+        FilterInstructions =
+            "Filter only when the user names a model."
+    });
+
+var languageBoost =
+    new SearchIndexKnowledgeSourceFieldValueBoost(
+        "language",
+        2.0);
+languageBoost.FieldValues.Add("en-US");
+languageBoost.FieldValues.Add("ja-JP");
+languageBoost.BoostInstructions =
+    "Prefer the language requested by the user.";
+queryHints.Boosts.Add(languageBoost);
+
+var knowledgeSource = new SearchIndexKnowledgeSource(
+    "product-docs-ks",
+    new SearchIndexKnowledgeSourceParameters(
+        "product-docs-index")
+    {
+        QueryHints = queryHints
+    });
+
+await indexClient.CreateOrUpdateKnowledgeSourceAsync(
+    knowledgeSource);
+```
+
+**Reference:** [SearchIndexKnowledgeSourceParameters](/dotnet/api/azure.search.documents.indexes.models.searchindexknowledgesourceparameters?view=azure-dotnet-preview&preserve-view=true)
+
+::: zone-end
+
+::: zone pivot="python"
+
+```python
+from azure.identity import DefaultAzureCredential
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import (
+    SearchIndexKnowledgeSource,
+    SearchIndexKnowledgeSourceFieldValueBoost,
+    SearchIndexKnowledgeSourceFilterHint,
+    SearchIndexKnowledgeSourceParameters,
+    SearchIndexKnowledgeSourceQueryHints,
+)
+
+endpoint = "<search-endpoint>"
+index_client = SearchIndexClient(
+    endpoint=endpoint,
+    credential=DefaultAzureCredential(),
+)
+
+query_hints = SearchIndexKnowledgeSourceQueryHints(
+    filters=[
+        SearchIndexKnowledgeSourceFilterHint(
+            field="productFamily",
+            field_values=["Model-X100", "Model-X200"],
+            filter_instructions=(
+                "Filter only when the user names a model."
+            ),
+        )
+    ],
+    boosts=[
+        SearchIndexKnowledgeSourceFieldValueBoost(
+            field="language",
+            field_values=["en-US", "ja-JP"],
+            boost=2.0,
+            boost_instructions=(
+                "Prefer the language requested by the user."
+            ),
+        )
+    ],
+)
+
+knowledge_source = SearchIndexKnowledgeSource(
+    name="product-docs-ks",
+    search_index_parameters=SearchIndexKnowledgeSourceParameters(
+        search_index_name="product-docs-index",
+        query_hints=query_hints,
+    ),
+)
+
+index_client.create_or_update_knowledge_source(knowledge_source)
+```
+
+**Reference:** [SearchIndexKnowledgeSourceParameters](/python/api/azure-search-documents/azure.search.documents.indexes.models.searchindexknowledgesourceparameters)
+
+::: zone-end
+
+::: zone pivot="rest"
+
+```http
+PUT {{search-endpoint}}/knowledgesources('product-docs-ks')?api-version=2026-08-01-preview
+Content-Type: application/json
+Authorization: Bearer {{search-access-token}}
+
+{
+  "name": "product-docs-ks",
+  "kind": "searchIndex",
+  "searchIndexParameters": {
+    "searchIndexName": "product-docs-index",
+    "queryHints": {
+      "filters": [{
+        "field": "productFamily",
+        "fieldValues": ["Model-X100", "Model-X200"],
+        "filterInstructions": "Filter only when the user names a model."
+      }],
+      "boosts": [{
+        "kind": "fieldValue",
+        "field": "language",
+        "fieldValues": ["en-US", "ja-JP"],
+        "boost": 2.0,
+        "boostInstructions": "Prefer the language requested by the user."
+      }]
+    }
+  }
+}
+```
+
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
+
+::: zone-end
+
+Configure each hint according to the following requirements:
+
+| Hint | Field requirements | `fieldValues` behavior | Collection limits |
+| --- | --- | --- | --- |
+| Filter | `field` must identify a filterable index field. | Required. List the exhaustive set of allowed values. If the request doesn't map to a listed value, the planner is instructed not to filter on that field. | Up to five hints with unique fields. Each value can contain up to 128 characters, and all values in one hint can contain up to 2,048 characters combined. |
+| `fieldValue` boost | `field` must identify a searchable field that uses a language, standard, or default analyzer. | Optional examples. If you omit them, use `boostInstructions` to explain which value to select from the request. | Up to five hints with unique fields. Each hint can contain up to 20 values, with 128 characters per value and 1,024 characters combined. |
+| `multiWordExpression` boost | Omit `field`. The index must contain at least one searchable field that uses a language, standard, or default analyzer. | Optional examples of domain-specific phrases. | One hint. It can contain up to 20 values, with 128 characters per value and 1,024 characters combined. |
+
+For either boost kind, `boost` is required and must be a finite number greater than `1.0`. Higher values give matching documents more influence in ranking without excluding other documents. Limit each optional `filterInstructions` or `boostInstructions` value to 1,024 characters.
+
+Use a `multiWordExpression` boost for domain-specific phrases whose meaning isn't captured by the individual words. Provide example phrases in `fieldValues`, or omit them and let `boostInstructions` and the user's request guide phrase selection:
+
+```json
+{
+  "boosts": [{
+    "kind": "multiWordExpression",
+    "fieldValues": ["deferred tax", "wash sale"],
+    "boost": 3.0,
+    "boostInstructions": "Boost domain terms used as complete phrases."
+  }]
+}
+```
+
+When you design query hints, keep the following behaviors in mind:
+
++ Hints are best effort, so the model might not generate a filter or boost for every request. For required constraints, such as authorization boundaries, use [document-level access control](search-document-level-access-overview.md) or a [deterministic filter](#persist-a-base-filter-on-a-knowledge-source-preview) instead.
+
++ Hints need model-driven query planning, so they aren't applied when the retrieval reasoning effort is `minimal`. At other effort levels, a GPT-4o or GPT-4.1 family model returns HTTP 400 when the stored `queryHints` object contains a filter. The service checks stored filters before applying `queryHintOverrides`, so an empty or boosts-only override doesn't bypass this validation. Stored `fieldValue` and `multiWordExpression` boosts alone don't trigger the validation.
+
++ Generated filters combine with `baseFilter` and `filterAddOn` by using `AND`. A generated boost rewrites the query in full Lucene syntax while preserving the original terms.
+
++ Query hints use indexed values as grounding. They don't configure analyzers or enable language detection. The `language` values in these examples are ordinary index metadata.
+
+To replace stored hints for a single retrieve request and verify the generated filter or boost, see [Override stored query hints at query time (preview)](agentic-retrieval-how-to-retrieve.md#override-stored-query-hints-at-query-time-preview).
+
 ## Assign to a knowledge base
 
 If you're satisfied with the knowledge source, [add it to a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックス知識ソースの更新"
}
```

### Explanation
この変更は、検索インデックス知識ソースの作成方法に関するドキュメントの大幅な更新を反映しています。主に、APIのバージョンが `2026-05-01-preview` から `2026-08-01-preview` に変更され、新機能や重要な情報が追加されています。

具体的な変更点は以下の通りです：

1. **API バージョンの更新**：新しいAPIバージョンに合わせて、知識ソースの機能や接続が強化され、より多くのMicrosoftサービスやサードパーティのサービスとの互換性が確保されています。

2. **ドキュメント内容の大幅な追加**：知識ソースの構成に関する情報が拡充され、特にクエリヒントの設定やストレージのフィルター、ブーストに関する詳細な指示が含まれています。これにより、ユーザーはより具体的で適切な設定が可能になります。

3. **認証方法の変更**：サンプルコードでの認証方法が `AzureKeyCredential` から `DefaultAzureCredential` に変更されており、ユーザーはより安全で推奨される実装に沿った形でAPIにアクセスできます。

4. **クエリヒント機能の追加**：新バージョンでは、クエリプランニングモデルによって使用者のリクエストからフィルターやランキングブーストを生成することができるようになりました。これに対応するサンプルコードも具体的に指定されており、ユーザーが実際にどのように実装を行えばよいかが明確になっています。

5. **API使用の注意点**：新機能の利用に際して、「semanticConfigurationName」がオプションであることや、旧APIとの互換性を保つ方法についての説明が強調されています。

これにより、ユーザーは検索インデックス知識ソースをより適切に利用でき、従来よりも充実した機能を活用できるようになります。

## articles/search/agentic-knowledge-source-how-to-sharepoint-indexed.md{#item-fe72fc}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Create a SharePoint (Indexed) Knowledge Source
 description: Learn how to create an indexed SharePoint knowledge source, which ingests content from SharePoint sites into a searchable index on Azure AI Search.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/08/2026
+ms.date: 08/14/2026
 ai-usage: ai-assisted
 ms.custom: doc-kit-assisted
 zone_pivot_groups: search-csharp-python-rest
@@ -16,11 +16,11 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [Preview feature](./includes/previews/agentic-retrieval-preview-feature.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -39,8 +39,8 @@ The generated indexer conforms to the *SharePoint in Microsoft 365 indexer*, who
 
 ### Usage support
 
-| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-08-01-preview&preserve-view=true) |
+| -- | -- | -- | -- | -- | -- | -- |
 | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
@@ -59,25 +59,39 @@ The generated indexer conforms to the *SharePoint in Microsoft 365 indexer*, who
 
 + If `contentExtractionMode` is `standard`, use a Microsoft Foundry resource in a [region supported by Content Understanding in Foundry Tools](/azure/ai-services/content-understanding/language-region-support) and the `https://<resource-name>.services.ai.azure.com` endpoint. Deploy an embedding model, and deploy a multimodal chat model if you enable image verbalization.
 
-+ Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Permission to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 + If the knowledge source specifies an Azure OpenAI model for embeddings or image verbalization, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource.
 
++ If you set `networkAccessMode` to `private`, complete the following requirements:
+
+  + Use an [S2, S3, L1, or L2 search service](search-sku-tier.md#tier-descriptions).
+
+  + Keep the SharePoint connection string, Microsoft Entra application, and SharePoint permissions described in the previous prerequisites. SharePoint Online isn't a supported shared private link target, so private mode doesn't make this source connection private.
+
+  + For each protected model endpoint, enable a managed identity on the search service, grant it the **Cognitive Services User** role on the resource, and create and approve a shared private link. Use the `openai_account` group ID for Azure OpenAI endpoints and `foundry_account` for Foundry resource endpoints.
+
 ::: zone pivot="csharp"
 
 + The latest [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
+
 ::: zone-end
 
 ::: zone pivot="python"
 
 + The latest [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) preview package: `pip install --pre azure-search-documents`
 
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
+
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
++ The [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) version of the Search Service REST API.
+
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
@@ -107,7 +121,6 @@ The following JSON is an example response for an indexed SharePoint knowledge so
         "azureOpenAIParameters": {
           "resourceUri": "<redacted>",
           "deploymentId": "text-embedding-3-large",
-          "apiKey": "<redacted>",
           "modelName": "text-embedding-3-large",
           "authIdentity": null
         }
@@ -139,9 +152,9 @@ Run the following code to create an indexed SharePoint knowledge source.
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 using Azure.Search.Documents.KnowledgeBases.Models;
-using Azure;
+using Azure.Identity;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var chatCompletionParams = new AzureOpenAIVectorizerParameters
 {
@@ -159,6 +172,7 @@ var embeddingParams = new AzureOpenAIVectorizerParameters
 
 var ingestionParams = new KnowledgeSourceIngestionParameters
 {
+    NetworkAccessMode = KnowledgeSourceNetworkAccessMode.Public,
     DisableImageVerbalization = false,
     ChatCompletionModel = new KnowledgeBaseAzureOpenAIModel(azureOpenAIParameters: chatCompletionParams),
     EmbeddingModel = new KnowledgeSourceAzureOpenAIVectorizer
@@ -193,12 +207,12 @@ Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated
 
 ```python
 # Create an indexed SharePoint knowledge source
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import IndexedSharePointKnowledgeSource, IndexedSharePointKnowledgeSourceParameters, KnowledgeBaseAzureOpenAIModel, AzureOpenAIVectorizerParameters, KnowledgeSourceContentExtractionMode
-from azure.search.documents.knowledgebases.models import KnowledgeSourceIngestionParameters, KnowledgeSourceAzureOpenAIVectorizer
+from azure.search.documents.knowledgebases.models import KnowledgeSourceIngestionParameters, KnowledgeSourceNetworkAccessMode, KnowledgeSourceAzureOpenAIVectorizer
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
 knowledge_source = IndexedSharePointKnowledgeSource(
     name = "my-indexed-sharepoint-ks",
@@ -209,22 +223,21 @@ knowledge_source = IndexedSharePointKnowledgeSource(
         container_name = "defaultSiteLibrary",
         query = None,
         ingestion_parameters = KnowledgeSourceIngestionParameters(
+            network_access_mode = KnowledgeSourceNetworkAccessMode.PUBLIC,
             identity = None,
             disable_image_verbalization = False,
             chat_completion_model = KnowledgeBaseAzureOpenAIModel(
                 azure_open_ai_parameters = AzureOpenAIVectorizerParameters(
-                    resource_url = "aoai_endpoint",
-                    deployment_name = "aoai_gpt_deployment",
-                    model_name = "aoai_gpt_model",
-                    api_key = "aoai_api_key"
+                    resource_url = "<aoai-endpoint>",
+                    deployment_name = "<aoai-gpt-deployment>",
+                    model_name = "<aoai-gpt-model>",
                 )
             ),
             embedding_model = KnowledgeSourceAzureOpenAIVectorizer(
                 azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
-                    resource_url = "aoai_endpoint",
-                    deployment_name = "aoai_embedding_deployment",
-                    model_name = "aoai_embedding_model",
-                    api_key = "aoai_api_key"
+                    resource_url = "<aoai-endpoint>",
+                    deployment_name = "<aoai-embedding-deployment>",
+                    model_name = "<aoai-embedding-model>",
                 )
             ),
             content_extraction_mode = KnowledgeSourceContentExtractionMode.MINIMAL,
@@ -246,8 +259,8 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 
 ```http
 ### Create an indexed SharePoint knowledge source
-PUT {{search-url}}/knowledgesources/my-indexed-sharepoint-ks?api-version=2026-05-01-preview
-Authorization: Bearer {{token}}
+PUT {{search-endpoint}}/knowledgesources/my-indexed-sharepoint-ks?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 
 {
@@ -260,6 +273,7 @@ Content-Type: application/json
         "containerName": "defaultSiteLibrary",
         "query": null,
         "ingestionParameters": {
+            "networkAccessMode": "public",
             "identity": null,
             "embeddingModel": {
                 "kind": "azureOpenAI",
@@ -279,10 +293,23 @@ Content-Type: application/json
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
+### Protect Azure dependencies during ingestion
+
+Starting with the `2026-08-01-preview` API version, `networkAccessMode` controls the network environment in which the generated indexer for an indexed SharePoint knowledge source runs. This setting affects ingestion only and doesn't change knowledge base retrieve requests or responses.
+
+`networkAccessMode` defaults to `public`, which preserves existing public network behavior. When `networkAccessMode` is `private`, the generated indexer runs in the [private execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment). It uses approved [shared private links](search-indexer-howto-access-private.md) to access supported Azure dependencies, such as Azure OpenAI models and Microsoft Foundry resources.
+
+> [!IMPORTANT]
+> For indexed SharePoint knowledge sources, private mode applies only to supported Azure dependencies. SharePoint Online isn't a supported shared private link target, so the SharePoint source connection remains public.
+
+To configure and verify private access to supported Azure dependencies:
+
+[!INCLUDE [Configure private network ingestion](includes/how-tos/knowledge-source-private-network.md)]
+
 ## Check ingestion status
 
 [!INCLUDE [Check ingestion status](includes/how-tos/knowledge-source-status.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint（インデックス付き）知識ソースの更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるSharePointインデックス付き知識ソースの作成手順に関するドキュメントを更新するものです。主に、APIのバージョンが `2026-05-01-preview` から `2026-08-01-preview` に変更され、新しい機能や設定条件が追加されています。

具体的な変更点は以下のとおりです：

1. **API バージョンの更新**：新しいAPIバージョンに移行したことで、提供される機能やサポートが向上し、特にMicrosoftの各種サービスとの接続性が強化されています。

2. **ネットワークアクセスモードの設定**：`networkAccessMode` の新しい設定が導入され、デフォルトは `public` ですが、必要に応じて `private` に設定することもできるようになりました。ただし、SharePoint Onlineはプライベートリンクの対象外なので、接続は引き続きパブリックとなります。

3. **追加の認証オプション**：サンプルコードでは、使用する認証方法が `AzureKeyCredential` から `DefaultAzureCredential` に変更され、安全な認証の推奨が強調されています。

4. **新機能の追加と詳細な説明**：文書には、インデクサーがプライベート実行環境で実行される条件や、その効果についての詳細な説明が含まれています。また、公式ドキュメントリンクが新しいバージョンに合わせて更新されています。

5. **サンプルコードの更新**：C#やPythonのコード例が新しいバージョンに適合するように更新され、ユーザーが独自の環境で容易に導入できるようになっています。

これらの更新により、開発者はより効果的にSharePoint知識ソースを設定し、利用できるようになります。

## articles/search/agentic-knowledge-source-how-to-sharepoint-remote.md{#item-79d019}

<details>
<summary>Diff</summary>
````diff
@@ -15,9 +15,9 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [Preview feature](./includes/previews/agentic-retrieval-preview-feature.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -31,35 +31,41 @@ Unlike indexed knowledge sources, remote SharePoint knowledge sources query live
 
 ### Usage support
 
-| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-08-01-preview&preserve-view=true) |
+| -- | -- | -- | -- | -- | -- | -- |
 | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
-+ An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md). 
++ An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md).
 
 + SharePoint in a Microsoft 365 tenant that's under the same Microsoft Entra ID tenant as Azure.
 
 + A Microsoft 365 Copilot license for query-time access to SharePoint content.
 
-+ Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Permission to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 ::: zone pivot="csharp"
 
 + The latest [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
+
 ::: zone-end
 
 ::: zone pivot="python"
 
 + The latest [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) preview package: `pip install --pre azure-search-documents`
 
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
+
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
++ The [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) version of the Search Service REST API.
+
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
@@ -117,9 +123,9 @@ Run the following code to create a remote SharePoint knowledge source.
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 using Azure.Search.Documents.KnowledgeBases.Models;
-using Azure;
+using Azure.Identity;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var knowledgeSource = new RemoteSharePointKnowledgeSource(name: "my-remote-sharepoint-ks")
 {
@@ -143,11 +149,11 @@ Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated
 
 ```python
 # Create a remote SharePoint knowledge source
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import RemoteSharePointKnowledgeSource, RemoteSharePointKnowledgeSourceParameters
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
 knowledge_source = RemoteSharePointKnowledgeSource(
     name = "my-remote-sharepoint-ks",
@@ -172,8 +178,8 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 
 ```http
 ### Create a remote SharePoint knowledge source
-PUT {{search-url}}/knowledgesources/my-remote-sharepoint-ks?api-version=2026-05-01-preview
-api-key: {{api-key}}
+PUT {{search-endpoint}}/knowledgesources/my-remote-sharepoint-ks?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 
 {
@@ -189,7 +195,7 @@ Content-Type: application/json
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
@@ -200,7 +206,7 @@ Not all SharePoint properties are supported in the `filterExpression`. For a lis
 Learn more about [KQL filters](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/copilotroot-retrieval?pivots=graph-v1#example-7-use-filter-expressions) in the syntax reference.
 
 | Example | Filter expression |
-|---------|-------------------|
+| --------- | ------------------- |
 | Filter to a single site by ID | `"filterExpression": "SiteID:\"00aa00aa-bb11-cc22-dd33-44ee44ee44ee\""` |
 | Filter to multiple sites by ID | `"filterExpression": "SiteID:\"00aa00aa-bb11-cc22-dd33-44ee44ee44ee\" OR SiteID:\"11bb11bb-cc22-dd33-ee44-55ff55ff55ff\""` |
 | Filter to files under a specific path | `"filterExpression": "Path:\"https://my-demo.sharepoint.com/sites/mysite/Shared Documents/en/mydocs\""` |
@@ -294,8 +300,8 @@ You can pass a `filterExpressionAddOn` in the `knowledgeSourceParams` on the ret
 
 ```http
 ### Retrieve knowledge base content
-POST {{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2026-05-01-preview
-Authorization: Bearer {{accessToken}}
+POST {{search-endpoint}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 x-ms-query-source-authorization: {{user-access-token}}
 
@@ -318,7 +324,7 @@ x-ms-query-source-authorization: {{user-access-token}}
 }
 ```
 
-**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リモートSharePoint知識ソースの更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるリモートSharePoint知識ソースの作成方法に関するドキュメントの更新を反映しています。主な改訂点は、APIのバージョンが `2026-05-01-preview` から `2026-08-01-preview` に変更されたことに伴うもので、機能や使用条件に関する情報が最新の内容にアップデートされています。

具体的な変更点は以下の通りです：

1. **API バージョンの更新**：新しいAPIバージョンが適用され、それに伴い、機能の向上やパフォーマンスの改善が期待されます。

2. **認証方式の変更**：サンプルコードでは、使用する認証方法が `AzureKeyCredential` から `DefaultAzureCredential` に変更されており、安全性や使いやすさが向上しています。

3. **サポート情報の更新**：さまざまなSDKやサービスのリンクが新しいバージョンに合わせて更新されており、ユーザーは最新のリソースにアクセスしやすくなっています。

4. **知識ソースの作成の詳細**：リモートSharePoint知識ソースの作成手順やAPI呼び出しのサンプルが具体的に更新され、より明確な指示が提供されています。

5. **フィルターおよびクエリの更新**：いくつかのクエリ表現やフィルター表現に関する説明が追加されており、ユーザーが特定の条件でデータを効果的に取得できるようになっています。

6. **ドキュメントの整えられた構成**：説明やコード例がより一貫性のある形式で整理されており、新しい情報を含む形で、ユーザーが必要な情報を迅速に見つけられるようになっています。

これにより、リモートSharePoint知識ソースの設定が行いやすくなり、開発者は最新機能を活用してエンジニアリングプロセスを効率化できます。

## articles/search/agentic-knowledge-source-how-to-web-manage.md{#item-af61ec}

<details>
<summary>Diff</summary>
````diff
@@ -32,17 +32,17 @@ As an Azure admin, you can use the Azure CLI to enable or disable the use of [We
 
 To check the current status of Web Knowledge Source access, run the following command.
 
-### [PowerShell](#tab/powershell)
+# [Azure CLI](#tab/azure-cli)
 
 ```azurecli
 az feature show --name WebKnowledgeSourceDisabled --namespace Microsoft.Search --subscription "<subscription-id>"
 ```
 
-### [REST API](#tab/rest-api)
+# [REST API](#tab/rest-api)
 
 ```http
-GET https://management.azure.com/subscriptions/{{subscriptionId}}/providers/Microsoft.Features/providers/Microsoft.Search/features/WebKnowledgeSourceDisabled?api-version=2021-07-01
-Authorization: Bearer {{accessToken}} // Obtain using `az account get-access-token --scope https://management.azure.com/.default --query accessToken --output tsv`
+GET https://management.azure.com/subscriptions/{{subscription-id}}/providers/Microsoft.Features/providers/Microsoft.Search/features/WebKnowledgeSourceDisabled?api-version=2021-07-01
+Authorization: Bearer {{management-access-token}} // Obtain using `az account get-access-token --scope https://management.azure.com/.default --query accessToken --output tsv`
 ```
 
 ---
@@ -56,17 +56,17 @@ The output shows the `state` property, which indicates the current registration
 
 Access to Web Knowledge Source is enabled by default. If access has been disabled, you can run the following command to enable it.
 
-### [PowerShell](#tab/powershell)
+# [Azure CLI](#tab/azure-cli)
 
-```powershell
+```azurecli
 az feature unregister --name WebKnowledgeSourceDisabled --namespace Microsoft.Search --subscription "<subscription-id>"
 ```
 
-### [REST API](#tab/rest-api)
+# [REST API](#tab/rest-api)
 
 ```http
-POST https://management.azure.com/subscriptions/{{subscriptionId}}/providers/Microsoft.Features/providers/Microsoft.Search/features/WebKnowledgeSourceDisabled/unregister?api-version=2021-07-01
-Authorization: Bearer {{accessToken}} // Obtain using `az account get-access-token --scope https://management.azure.com/.default --query accessToken --output tsv`
+POST https://management.azure.com/subscriptions/{{subscription-id}}/providers/Microsoft.Features/providers/Microsoft.Search/features/WebKnowledgeSourceDisabled/unregister?api-version=2021-07-01
+Authorization: Bearer {{management-access-token}} // Obtain using `az account get-access-token --scope https://management.azure.com/.default --query accessToken --output tsv`
 ```
 
 ---
@@ -75,22 +75,22 @@ Authorization: Bearer {{accessToken}} // Obtain using `az account get-access-tok
 
 Run the following command to disable access to Web Knowledge Source.
 
-### [PowerShell](#tab/powershell)
+# [Azure CLI](#tab/azure-cli)
 
-```powershell
+```azurecli
 az feature register --name WebKnowledgeSourceDisabled --namespace Microsoft.Search --subscription "<subscription-id>"
 ```
 
-### [REST API](#tab/rest-api)
+# [REST API](#tab/rest-api)
 
 ```http
-POST https://management.azure.com/subscriptions/{{subscriptionId}}/providers/Microsoft.Features/providers/Microsoft.Search/features/WebKnowledgeSourceDisabled/register?api-version=2021-07-01
-Authorization: Bearer {{accessToken}} // Obtain using `az account get-access-token --scope https://management.azure.com/.default --query accessToken --output tsv`
+POST https://management.azure.com/subscriptions/{{subscription-id}}/providers/Microsoft.Features/providers/Microsoft.Search/features/WebKnowledgeSourceDisabled/register?api-version=2021-07-01
+Authorization: Bearer {{management-access-token}} // Obtain using `az account get-access-token --scope https://management.azure.com/.default --query accessToken --output tsv`
 ```
 
 ---
 
 ## Related content
 
 + [Create a Web Knowledge Source resource](agentic-knowledge-source-how-to-web.md)
-+ [Agentic retrieval in Azure AI Search](search-agentic-retrieval-concept.md)
++ [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Web知識ソース管理の更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるWeb知識ソースの管理方法に関するドキュメントを更新するもので、主にコマンドやAPIエンドポイントの表記に関する改善が行われました。

主な変更点は以下の通りです：

1. **コマンドの表記変更**：PowerShellのコマンドからAzure CLIのコマンドに変更され、コマンドの使用法が最新の推奨に基づいて整備されています。これにより、ユーザーがCLIツールを利用して機能を管理する際の一貫性が向上しています。

2. **引数の形式統一**：`<subscription-id>`が `"<subscription-id>"` から `"<subscription-id>"` に変更され、指示が一貫性を持った形式に統一されました。また、`{{accessToken}}`の部分も `{{management-access-token}}` に変更され、より具体的な命名が反映されています。

3. **関連コンテンツのリンク更新**：関連情報へのリンクが修正され、ドキュメントの整合性やナビゲーションが向上しました。特に、情報のリンク先が現在有用とされているリソースに合わせて更新されています。

4. **全体の構成整備**：文書全体のフォーマットが整えられ、ユーザーが必要な情報にすぐアクセスできるように工夫されています。指示や注記が明確に区分され、読みやすくなっています。

これらの更新により、Web知識ソースの管理がより簡単に行えるようになり、Azureの利用者は最新の機能を効果的に活用できるようになります。

## articles/search/agentic-knowledge-source-how-to-web.md{#item-6b21d0}

<details>
<summary>Diff</summary>
````diff
@@ -17,9 +17,9 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [GA feature](./includes/previews/agentic-retrieval-ga-feature.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -43,7 +43,7 @@ Web Knowledge Source works best alongside other knowledge sources. Use it when y
 ### Usage support
 
 | [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources) |
-|--|--|--|--|--|--|--|
+| -- | -- | -- | -- | -- | -- | -- |
 | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
@@ -52,35 +52,41 @@ Web Knowledge Source works best alongside other knowledge sources. Use it when y
 
 + An Azure AI Search service in any [public region that provides agentic retrieval](search-region-support.md). Web Knowledge Source isn't supported in private or sovereign clouds.
 
-+ Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Permission to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 ::: zone pivot="csharp"
 
 + Required [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) package:
 
-  + For 2026-05-01-preview features, the latest preview package: `dotnet add package Azure.Search.Documents --prerelease`
+  + For `2026-08-01-preview` features, the latest preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
-  + For 2026-04-01 features, the latest stable package: `dotnet add package Azure.Search.Documents`
+  + For `2026-04-01` features, the latest stable package: `dotnet add package Azure.Search.Documents`
+
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
 
 ::: zone-end
 
 ::: zone pivot="python"
 
 + Required [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) package:
 
-  + For 2026-05-01-preview features, the latest preview package: `pip install --pre azure-search-documents`
+  + For `2026-08-01-preview` features, the latest preview package: `pip install --pre azure-search-documents`
+
+  + For `2026-04-01` features, the latest stable package: `pip install azure-search-documents`
 
-  + For 2026-04-01 features, the latest stable package: `pip install azure-search-documents`
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
 
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ Required REST API version:
++ Required Search Service REST API version:
+
+  + For preview features: [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
-  + For preview features: [Search Service 2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+  + For generally available features: [2026-04-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true)
 
-  + For generally available features: [Search Service 2026-04-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true)
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
@@ -90,7 +96,7 @@ Web Knowledge Source works best alongside other knowledge sources. Use it when y
 
 + For the 2026-04-01 API version, the knowledge base must include a model reference to provide the LLM for web content summarization. Retrieval is always extractive (cited summaries). Answer synthesis and configurable reasoning effort aren't available in this version.
 
-+ For the 2026-05-01-preview API version, the knowledge base model reference also enables [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md), which produces a single LLM-formulated response instead of extracted citations.
++ For the `2026-08-01-preview` API version, the knowledge base model reference also enables [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md), which produces a single LLM-formulated response instead of extracted citations.
 
 ## Check for existing knowledge sources
 
@@ -116,15 +122,15 @@ Run the following code to create a web knowledge source.
 
 ::: zone pivot="csharp"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```csharp
 // Create Web Knowledge Source
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
-using Azure;
+using Azure.Identity;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var knowledgeSource = new WebKnowledgeSource(name: "my-web-ks")
 {
@@ -133,11 +139,11 @@ var knowledgeSource = new WebKnowledgeSource(name: "my-web-ks")
     {
         Domains = new WebKnowledgeSourceDomains
         {
-            AllowedDomains = 
+            AllowedDomains =
             {
                 new WebKnowledgeSourceDomain(address: "learn.microsoft.com") { IncludeSubpages = true }
             },
-            BlockedDomains = 
+            BlockedDomains =
             {
                 new WebKnowledgeSourceDomain(address: "bing.com") { IncludeSubpages = false }
             }
@@ -157,9 +163,9 @@ Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated
 // Create Web Knowledge Source
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
-using Azure;
+using Azure.Identity;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var knowledgeSource = new WebKnowledgeSource(name: "my-web-ks")
 {
@@ -168,11 +174,11 @@ var knowledgeSource = new WebKnowledgeSource(name: "my-web-ks")
     {
         Domains = new WebKnowledgeSourceDomains
         {
-            AllowedDomains = 
+            AllowedDomains =
             {
                 new WebKnowledgeSourceDomain(address: "learn.microsoft.com") { IncludeSubpages = true }
             },
-            BlockedDomains = 
+            BlockedDomains =
             {
                 new WebKnowledgeSourceDomain(address: "bing.com") { IncludeSubpages = false }
             }
@@ -192,15 +198,15 @@ Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated
 
 ::: zone pivot="python"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```python
 # Create Web Knowledge Source
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import WebKnowledgeSource, WebKnowledgeSourceParameters, WebKnowledgeSourceDomains, WebKnowledgeSourceDomain
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
 knowledge_source = WebKnowledgeSource(
     name = "my-web-ks",
@@ -224,11 +230,11 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 
 ```python
 # Create Web Knowledge Source
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import WebKnowledgeSource, WebKnowledgeSourceParameters, WebKnowledgeSourceDomains, WebKnowledgeSourceDomain
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
 knowledge_source = WebKnowledgeSource(
     name = "my-web-ks",
@@ -254,13 +260,13 @@ print(f"Knowledge source '{knowledge_source.name}' created or updated successful
 
 ::: zone pivot="rest"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```http
 ### Create Web Knowledge Source
-PUT {{search-url}}/knowledgesources/my-web-ks?api-version=2026-05-01-preview
+PUT {{search-endpoint}}/knowledgesources/my-web-ks?api-version=2026-08-01-preview
 Content-Type: application/json
-api-key: {{api-key}}
+Authorization: Bearer {{search-access-token}}
 
 {
   "name": "my-web-ks",
@@ -276,15 +282,15 @@ api-key: {{api-key}}
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 # [2026-04-01](#tab/2026-04-01)
 
 ```http
 ### Create Web Knowledge Source
-PUT {{search-url}}/knowledgesources/my-web-ks?api-version=2026-04-01
+PUT {{search-endpoint}}/knowledgesources/my-web-ks?api-version=2026-04-01
 Content-Type: application/json
-api-key: {{api-key}}
+Authorization: Bearer {{search-access-token}}
 
 {
   "name": "my-web-ks",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Web知識ソースのAPIバージョン更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるWeb知識ソースについてのドキュメントを更新するもので、主にAPIのバージョンが2026-05-01-previewから2026-08-01-previewに更新されたことを反映しています。この変更により、提供される機能や使用条件が最新のものに合わせて整備されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：ドキュメント内のすべての参照が新しいAPIバージョンに変更され、これによりユーザーは最新の機能セットとそれに伴う条件を利用できるようになります。

2. **認証方法の変更**：サンプルコード内で、`AzureKeyCredential` から `DefaultAzureCredential` への変更が行われており、より安全で柔軟な認証方法が推奨されています。これにより、ユーザーは異なる認証シナリオに簡単に対応できるようになります。

3. **フィーチャー関連情報の強調**：新しいAPIバージョンに伴う機能が強調されており、Web知識ソースが他の知識ソースとどのように連携するかについての情報が整理されています。

4. **使用法のサンプル追加**：Web知識ソースの作成や管理に関連する具体的なコード例が更新され、最新の機能を活用するための指定方法が明確になっています。

5. **関連コンテンツの更新**：API呼び出しに関するリファレンスリンクが新しいバージョンに合わせて更新され、ユーザーが適切なドキュメントにアクセスしやすくなっています。

これらの改善により、ユーザーはAzure AI SearchでのWeb知識ソースの利用をより効果的に行えるようになり、最新のツールや機能を利用する際のリソースが整備されています。

## articles/search/agentic-knowledge-source-how-to-work-iq.md{#item-94718e}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,9 @@ title: Create a Work IQ Knowledge Source
 description: Learn how to create a Work IQ knowledge source to ground an agentic retrieval pipeline in Azure AI Search with organizational intelligence from Work IQ.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/02/2026
+ms.date: 08/17/2026
+ms.custom:
+  - dev-focus
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
@@ -13,107 +15,185 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> When you connect to Work IQ, you might incur costs, and data might be sent outside the Azure compliance boundary and processed according to the applicable service terms and data handling policies. It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
+> When you connect to Work IQ, you might incur costs, and data might be sent outside the Azure compliance boundary and processed according to the applicable service terms and data handling policies. It's your responsibility to manage whether your data flows outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This responsibility includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
 A *Work IQ knowledge source* (preview) connects [Work IQ](/microsoft-365/copilot/extensibility/work-iq) to an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
 Work IQ surfaces organizational intelligence from your Microsoft 365 content, including documents, emails, meetings, and activity across Microsoft 365 apps.
 
-Unlike indexed knowledge sources, Work IQ knowledge sources query live data directly at retrieval time. No ingestion pipeline is needed. Queries require an end-user access token, which the retrieval engine uses to call Work IQ on the caller's behalf.
+Unlike indexed knowledge sources, Work IQ knowledge sources query live data directly at retrieval time. No ingestion pipeline is needed. Queries require a user access token issued for your Microsoft Entra app registration. Azure AI Search exchanges that token for a delegated Work IQ token and calls Work IQ on the user's behalf.
 
 > [!WARNING]
 > In this preview, a Work IQ knowledge source might use Work IQ capabilities that perform actions, not just retrieve information. Use it with care, limit access to trusted applications and users, and review your scenario's permissions and governance controls before enabling it.
 
 ### Usage support
 
-| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-05-01-preview&preserve-view=true) |
-|--|--|--|--|--|--|--|
-| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-08-01-preview&preserve-view=true) |
+| --- | --- | --- | --- | --- | --- | --- |
+| ❌ | ❌ | ✔️ | ✔️ | ❌ | ❌ | ✔️ |
 
 ## Prerequisites
 
 + An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md).
 
-+ Each end user who queries through this knowledge source must have a Microsoft 365 Copilot license.
++ A [usage-based billing plan for Work IQ](/microsoft-365/copilot/extensibility/work-iq/enable-work-iq#prerequisites) set up in Copilot Studio with an Azure subscription and resource group. Assign each user who queries Work IQ to the billing plan.
 
-+ The Azure AI Search service, the Work IQ environment, and end users must be in the same Microsoft Entra tenant. Cross-tenant retrieval isn't supported.
++ Your [Microsoft Entra tenant enabled for Work IQ](/microsoft-365/copilot/extensibility/work-iq/enable-work-iq#enable-work-iq-api-in-your-organization). After billing is configured, a Microsoft Entra Global Administrator completes this one-time setup.
 
-+ Approved access to Work IQ retrieval through Azure AI Search. For more information, see [Request access to Work IQ retrieval](#request-access-to-work-iq-retrieval).
++ A client application that signs in users and sends retrieve requests.
 
-+ Permissions to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Recommended Microsoft Entra roles for each app setup action:
+
+  + [Application Developer](/entra/identity/role-based-access-control/permissions-reference#application-developer) to create an app registration.
+
+  + App registration owner or a supported administrator role to [create its federated identity credential](/entra/workload-id/workload-identity-federation-create-trust#important-considerations-and-restrictions).
+
+  + [Cloud Application Administrator or Application Administrator](/entra/identity/enterprise-apps/grant-admin-consent#prerequisites) to grant tenant-wide admin consent for the `WorkIQAgent.Ask` delegated permission.
+
++ Permission to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 ::: zone pivot="csharp"
 
 + The latest [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
+
 ::: zone-end
 
 ::: zone pivot="python"
 
 + The latest [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) preview package: `pip install --pre azure-search-documents`
 
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
+
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
++ The [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) version of the Search Service REST API.
+
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
-## Request access to Work IQ retrieval
+## Data governance and compliance
 
-Work IQ retrieval through Azure AI Search is off by default and requires a Microsoft-approved request before use.
+Before you enable Work IQ retrieval, review [Data, Privacy, and Security for Microsoft 365 Copilot](/microsoft-365/copilot/microsoft-365-copilot-privacy).
 
-To request access:
+### Data use and privacy
 
-1. Register the `EnableFoundryIQWithWorkIQ` feature flag on your Azure subscription.
+Prompts, responses, and data accessed through Microsoft Graph aren't used to
+train foundation language models.
 
-   ```azurecli
-   az feature register --namespace Microsoft.Search --name EnableFoundryIQWithWorkIQ --subscription "<your-subscription-guid>"
-   ```
+### Access control
 
-1. Re-register the `Microsoft.Search` resource provider.
+Work IQ applies Microsoft 365 permissions on every request. Retrieval returns
+only organizational data that the signed-in user has permission to access.
 
-   ```azurecli
-   az provider register -n Microsoft.Search --subscription "<your-subscription-guid>"
-   ```
+### Data residency and compliance
 
-1. Have a Microsoft Entra administrator for your tenant submit the [Work IQ access request form](https://aka.ms/foundry-iq-work-iq-admin-consent-form).
-    
-1. Wait for Microsoft to enable access after reviewing and approving the request.
+Review the Microsoft 365 documentation for the data residency, privacy,
+security, and compliance commitments that apply to your organization and
+scenario.
 
-    > [!TIP]
-    > Registering a preview feature requires the **Owner** or **Contributor** built-in role on the subscription, which is a separate role from the Microsoft Entra administrator who submits the form. The two responsibilities can be held by different people in your organization. For more information about the registration mechanism, see [Set up preview features in Azure subscription](/azure/azure-resource-manager/management/preview-features).
+## Set up Microsoft Entra authentication
 
-## Data governance and compliance
+Starting with the `2026-08-01-preview` API version, each Work IQ knowledge source uses a customer-owned Microsoft Entra app registration for authentication. [At query time](#enforce-permissions-at-query-time), authentication works as follows:
+
+1. The client app signs in the user and sends a user assertion to Azure AI Search.
+1. The search service managed identity authenticates as the customer-owned app through a federated credential.
+1. Azure AI Search exchanges the user assertion for a delegated Work IQ token and calls Work IQ on behalf of the signed-in user.
+
+No client secret is stored on the Work IQ knowledge source. Configure the app and its permissions once, and then create a federated credential for each search service identity that uses the app.
+
+### Configure the Work IQ app registration
+
+To configure the customer-owned app that Azure AI Search uses to call Work IQ:
+
+1. [Register an application](/entra/identity-platform/quickstart-register-app) in the Microsoft Entra tenant where you want to manage Work IQ consent. For **Supported account types**, select **Accounts in this organizational directory only**.
+
+1. On the app registration's **Overview** page, copy the **Application (client) ID** and **Directory (tenant) ID**. You need the application ID to configure Work IQ authentication and the tenant ID to sign in to the tenant that contains the app registration.
+
+1. On the app registration's **Expose an API** page, [add the required delegated scope](/entra/identity-platform/quickstart-configure-app-expose-web-apis#add-a-scope) named exactly `access_as_user`. Use this lowercase name; don't substitute another scope name. The full scope is `api://<application-client-id>/access_as_user`.
+
+1. On the app registration's **API permissions** page, select **Add a permission** > **APIs my organization uses**.
+
+1. Search for **Work IQ** (application ID `fdcc1f02-fc51-4226-8753-f668596af7f7`), select **Delegated permissions** > **WorkIQAgent.Ask**, and then select **Add permissions**.
+
+1. Have an administrator with a consent role listed in the prerequisites select **Grant admin consent for [your tenant]** on the same page. This consent allows the app to exchange a user assertion for a delegated Work IQ token.
+
+### Configure the search service identity
+
+To configure the identity that Azure AI Search uses to authenticate as your Work IQ app:
+
+1. [Enable a system-assigned managed identity](search-how-to-managed-identities.md) on your search service. If you can't use a system-assigned identity, configure exactly one user-assigned identity. A search service with multiple user-assigned identities and no system-assigned identity isn't supported.
 
-Work IQ operates entirely within the Microsoft 365 trust boundary. The following commitments apply when you route agent requests through Work IQ.
+1. On the search service's **Identity** page, copy the **Object (principal) ID**. The federated credential uses this value as its `subject`.
 
-### Data residency
+1. Go to **Microsoft Entra ID** > **Overview** and copy the **Tenant ID**. The federated credential uses this value in its `issuer` URL.
 
-Work IQ retrieves data from your organization's Microsoft 365 tenant. Data doesn't leave your tenant or cross regional boundaries during retrieval. The data's location follows your Microsoft 365 tenant data residency configuration, not your Azure AI Search service region. For details, see [Data, Privacy, and Security for Microsoft 365 Copilot](/microsoft-365/copilot/microsoft-365-copilot-privacy).
+### Create a federated credential
 
-### Privacy and data handling
+To create a federated credential for the search service identity:
 
-All Work IQ requests are governed by [Data, Privacy, and Security for Microsoft 365 Copilot](/microsoft-365/copilot/microsoft-365-copilot-privacy). Key commitments:
+1. Create a file named `credential.json`. Replace `<search-service-name>`, `<search-service-tenant-id>`, and `<search-service-principal-id>` with values for your search service.
 
-- Work IQ doesn't use customer content to train or improve underlying AI models.
+    ```json
+    {
+      "name": "<search-service-name>-identity",
+      "issuer": "https://login.microsoftonline.com/<search-service-tenant-id>/v2.0",
+      "subject": "<search-service-principal-id>",
+      "audiences": ["api://AzureADTokenExchange"]
+    }
+    ```
+
+    The credential name must be unique on the app registration. The `subject` value must match the managed identity principal ID exactly. A mismatch surfaces when you query, not when you create the knowledge source.
+
+1. Sign in to the [Azure CLI](/cli/azure/install-azure-cli) with the tenant that contains the app registration.
+
+    ```azurecli
+    az login --tenant <app-tenant-id> --allow-no-subscriptions
+    ```
+
+1. Create the federated credential.
+
+    ```azurecli
+    az ad app federated-credential create --id <application-client-id> --parameters credential.json --query id --output tsv
+    ```
+
+1. Copy the command output. Use this value for `federatedCredentialId` when you create the Work IQ knowledge source.
+
+Each federated credential trusts one managed identity principal ID. If another search service identity uses the app registration, repeat this procedure with a unique credential name and that identity's tenant and principal IDs. Use the corresponding credential ID on each Work IQ knowledge source.
+
+### Configure the client app
+
+To configure the app that signs in users and sends retrieve requests:
 
-### Access control and permissions
+1. On the client app's **API permissions** page, select **Add a permission** > **APIs my organization uses**.
 
-Work IQ enforces Microsoft 365 permissions automatically on every request. Agents can only access data that the signed-in user is already authorized to see. No elevation of privilege is possible.
+1. Paste the **Application (client) ID** that you copied earlier into the search box, and then select the Work IQ app registration.
 
-- Role-based access control, sensitivity labels, and information barriers defined in Microsoft 365 are respected.
+1. Select **Delegated permissions** > **access_as_user**, and then select **Add permissions**.
 
-### Compliance certifications
+1. Complete any consent required by your tenant's user-consent policy. If admin consent is required, have an administrator select **Grant admin consent for [your tenant]**.
 
-Work IQ inherits Microsoft 365's compliance certifications. For details, see [Data, Privacy, and Security for Microsoft 365 Copilot](/microsoft-365/copilot/microsoft-365-copilot-privacy).
+The client app can now request a user assertion for the Work IQ app registration. The `access_as_user` permission doesn't grant the client app direct access to Work IQ.
+
+### Authentication values
+
+When you create a Work IQ knowledge source, use the following `entraAppAuthentication` values from your Microsoft Entra app setup. Each value you provide must be a GUID.
+
+| Property | Required | Value |
+| --- | --- | --- |
+| `applicationId` | Yes | Application (client) ID of your Work IQ app registration. |
+| `federatedCredentialId` | Yes | Object ID of the federated credential you created on the app. It's not the credential name and isn't the search service principal ID. |
+| `tenantId` | No | Directory (tenant) ID of the app registration. Omit this property when the app registration and search service are in the same tenant. If they're in different tenants, this property is required. |
 
 ## Check for existing knowledge sources
 
@@ -126,6 +206,13 @@ The following JSON is an example response for a Work IQ knowledge source.
   "name": "my-workiq-ks",
   "kind": "workIQ",
   "description": "A sample Work IQ knowledge source.",
+  "workIQParameters": {
+    "entraAppAuthentication": {
+      "applicationId": "11111111-1111-1111-1111-111111111111",
+      "federatedCredentialId": "22222222-2222-2222-2222-222222222222",
+      "tenantId": null
+    }
+  },
   "encryptionKey": null
 }
 ```
@@ -137,68 +224,97 @@ Run the following code to create a Work IQ knowledge source.
 ::: zone pivot="csharp"
 
 ```csharp
-using Azure;
+using Azure.Identity;
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
+using Azure.Search.Documents.Models;
 
-Uri searchEndpoint = new Uri("<search-service-url>");
-AzureKeyCredential credential = new AzureKeyCredential("<api-key>");
+Uri searchEndpoint =
+    new("https://<search-service-name>.search.windows.net");
+var credential = new DefaultAzureCredential();
 var indexClient = new SearchIndexClient(searchEndpoint, credential);
 
-var knowledgeSource = new WorkIQKnowledgeSource(name: "my-workiq-ks")
+var entraAuthentication = new EntraAppAuthentication(
+    Guid.Parse("<application-client-id>"),
+    Guid.Parse("<federated-credential-id>"));
+var knowledgeSource = new WorkIQKnowledgeSource(
+    "my-workiq-ks",
+    new WorkIQKnowledgeSourceParameters(entraAuthentication))
 {
     Description = "A sample Work IQ knowledge source."
 };
 
-await indexClient.CreateOrUpdateKnowledgeSourceAsync(knowledgeSource);
-Console.WriteLine($"Knowledge source '{knowledgeSource.Name}' created or updated successfully.");
+KnowledgeSource createdSource =
+    await indexClient.CreateOrUpdateKnowledgeSourceAsync(knowledgeSource);
+Console.WriteLine($"Created knowledge source '{createdSource.Name}'.");
 ```
 
-**Reference:** [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient?view=azure-dotnet-preview&preserve-view=true)
+**Reference:** [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient?view=azure-dotnet-preview&preserve-view=true), [WorkIQKnowledgeSource](/dotnet/api/azure.search.documents.indexes.models.workiqknowledgesource?view=azure-dotnet-preview&preserve-view=true)
 
 ::: zone-end
 
 ::: zone pivot="python"
 
 ```python
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
-from azure.search.documents.indexes.models import WorkIQKnowledgeSource
-
-index_client = SearchIndexClient(
-    endpoint="<search-service-url>",
-    credential=AzureKeyCredential("<api-key>")
+from azure.search.documents.indexes.models import (
+    EntraAppAuthentication,
+    WorkIQKnowledgeSource,
+    WorkIQKnowledgeSourceParameters,
 )
 
+endpoint = "https://<search-service-name>.search.windows.net"
+credential = DefaultAzureCredential()
+
 knowledge_source = WorkIQKnowledgeSource(
     name="my-workiq-ks",
-    description="A sample Work IQ knowledge source."
+    description="A sample Work IQ knowledge source.",
+    work_iq_parameters=WorkIQKnowledgeSourceParameters(
+        entra_app_authentication=EntraAppAuthentication(
+            application_id="<application-client-id>",
+            federated_credential_id="<federated-credential-id>",
+        )
+    ),
 )
 
-index_client.create_or_update_knowledge_source(knowledge_source=knowledge_source)
-print(f"Knowledge source '{knowledge_source.name}' created or updated successfully.")
+with SearchIndexClient(endpoint, credential) as index_client:
+    created_source = index_client.create_or_update_knowledge_source(
+        knowledge_source
+    )
+print(f"Created knowledge source '{created_source.name}'.")
 ```
 
-**Reference:** [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient?view=azure-python-preview&preserve-view=true)
+**Reference:** [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient), [WorkIQKnowledgeSource](/python/api/azure-search-documents/azure.search.documents.indexes.models.workiqknowledgesource)
 
 ::: zone-end
 
 ::: zone pivot="rest"
 
 ```http
+@search-endpoint = <search-endpoint> // Example: https://my-service.search.windows.net
+@search-access-token = <search-access-token> // Run: az account get-access-token --scope https://search.azure.com/.default --query accessToken -o tsv
+
 ### Create a Work IQ knowledge source
-PUT {{search-url}}/knowledgesources/my-workiq-ks?api-version=2026-05-01-preview
-api-key: {{api-key}}
+PUT {{search-endpoint}}/knowledgesources/my-workiq-ks?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
+Prefer: return=representation
 
 {
   "name": "my-workiq-ks",
   "kind": "workIQ",
-  "description": "A sample Work IQ knowledge source."
+  "description": "A sample Work IQ knowledge source.",
+  "workIQParameters": {
+    "entraAppAuthentication": {
+      "applicationId": "<application-client-id>",
+      "federatedCredentialId": "<federated-credential-id>"
+    }
+  }
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
@@ -215,18 +331,166 @@ After the knowledge base is configured, [call the retrieve action or MCP endpoin
 
 ### Enforce permissions at query time
 
-Work IQ knowledge sources use an on-behalf-of (OBO) token flow. You pass the end-user access token in the `x-ms-query-source-authorization` header on the retrieve request. The token must be scoped to the Azure AI Search audience (`https://search.azure.com/.default`). The retrieval engine exchanges this token for a Work IQ–scoped token and uses it to query Work IQ on behalf of the end user.
+Starting with the `2026-08-01-preview` API version, Work IQ knowledge sources use an on-behalf-of (OBO) token flow through your customer-owned Microsoft Entra app registration. In addition to authenticating the retrieve request to Azure AI Search, your client must provide an app-audience user assertion for the signed-in user.
 
-Standard Azure AI Search authentication is also required on the retrieve request. The `x-ms-query-source-authorization` token is passed separately and doesn't replace service authentication.
+Your client app must sign in the user and acquire the user assertion. How you acquire the assertion depends on the app's platform and language. Use Microsoft Authentication Library (MSAL) and the [authorization code flow with Proof Key for Code Exchange](/entra/identity-platform/v2-oauth2-auth-code-flow) (PKCE) to request the exact scope `api://<application-client-id>/access_as_user`.
 
-For instructions on passing the token, see [Enforce permissions at query time (preview)](agentic-retrieval-how-to-retrieve.md#enforce-permissions-at-query-time-preview).
+Before you send the user assertion, confirm that:
 
-### Work IQ–specific response fields
++ `aud` identifies your Work IQ app registration.
++ `scp` contains `access_as_user`.
++ `oid` and `tid` identify the signed-in user and app tenant.
+
+Send both credentials in the same retrieve request, as shown in the following example. Use an Azure AI Search token or API key for service authentication. Pass the raw user assertion in the `x-ms-query-work-iq-source-authorization` header, not `x-ms-query-source-authorization`.
+
+::: zone pivot="csharp"
+
+```csharp
+using Azure.Identity;
+using Azure.Search.Documents;
+using Azure.Search.Documents.KnowledgeBases;
+using Azure.Search.Documents.KnowledgeBases.Models;
+
+Uri searchEndpoint =
+    new("https://<search-service-name>.search.windows.net");
+string userAssertion = "<user-assertion>";
+var credential = new DefaultAzureCredential();
+var options = new SearchClientOptions();
+options.Retry.NetworkTimeout = TimeSpan.FromSeconds(130);
+var retrievalClient = new KnowledgeBaseRetrievalClient(
+    searchEndpoint,
+    "my-kb",
+    credential,
+    options);
+
+var request = new KnowledgeBaseRetrievalRequest
+{
+    IncludeActivity = true,
+    MaxRuntimeInSeconds = 120
+};
+request.Intents.Add(
+    new KnowledgeRetrievalSemanticIntent("Find my project status."));
+request.KnowledgeSourceParams.Add(
+    new WorkIQKnowledgeSourceParams("my-workiq-ks")
+    {
+        IncludeReferences = true,
+        IncludeReferenceSourceData = true
+    });
+
+var response = await retrievalClient.RetrieveAsync(
+    request,
+    querySourceAuthorization: null,
+    queryWorkIQSourceAuthorization: userAssertion);
+Console.WriteLine(response.Value);
+```
+
+**Reference:** [KnowledgeBaseRetrievalClient](/dotnet/api/azure.search.documents.knowledgebases.knowledgebaseretrievalclient?view=azure-dotnet-preview&preserve-view=true), [KnowledgeBaseRetrievalRequest](/dotnet/api/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest?view=azure-dotnet-preview&preserve-view=true)
+
+::: zone-end
+
+::: zone pivot="python"
+
+```python
+from azure.identity import DefaultAzureCredential
+from azure.search.documents.knowledgebases import (
+    KnowledgeBaseRetrievalClient,
+)
+from azure.search.documents.knowledgebases.models import (
+    KnowledgeBaseRetrievalRequest,
+    KnowledgeRetrievalSemanticIntent,
+    WorkIQKnowledgeSourceParams,
+)
+
+endpoint = "https://<search-service-name>.search.windows.net"
+user_assertion = "<user-assertion>"
+credential = DefaultAzureCredential()
+
+request = KnowledgeBaseRetrievalRequest(
+    intents=[
+        KnowledgeRetrievalSemanticIntent(
+            search="Find my project status."
+        )
+    ],
+    knowledge_source_params=[
+        WorkIQKnowledgeSourceParams(
+            knowledge_source_name="my-workiq-ks",
+            include_references=True,
+            include_reference_source_data=True,
+        )
+    ],
+    include_activity=True,
+    max_runtime_in_seconds=120,
+)
+
+with KnowledgeBaseRetrievalClient(
+    endpoint,
+    credential,
+    knowledge_base_name="my-kb",
+) as retrieval_client:
+    response = retrieval_client.retrieve(
+        request,
+        query_work_iq_source_authorization=user_assertion,
+        timeout=130,
+    )
+
+print(response)
+```
+
+**Reference:** [KnowledgeBaseRetrievalClient](/python/api/azure-search-documents/azure.search.documents.knowledgebases.knowledgebaseretrievalclient), [KnowledgeBaseRetrievalRequest](/python/api/azure-search-documents/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest)
+
+::: zone-end
+
+::: zone pivot="rest"
+
+```http
+@search-endpoint = <search-endpoint>
+@search-access-token = <search-access-token>
+@user-assertion = <user-assertion>
+
+### Query a knowledge base with a Work IQ knowledge source
+POST {{search-endpoint}}/knowledgebases/my-kb/retrieve?api-version=2026-08-01-preview
+Authorization: Bearer {{search-access-token}}
+x-ms-query-work-iq-source-authorization: {{user-assertion}}
+Content-Type: application/json
+
+{
+  "messages": [{
+    "role": "user",
+    "content": [{
+      "type": "text",
+      "text": "Find my project status."
+    }]
+  }],
+  "knowledgeSourceParams": [{
+    "knowledgeSourceName": "my-workiq-ks",
+    "kind": "workIQ",
+    "includeReferences": true,
+    "includeReferenceSourceData": true
+  }],
+  "includeActivity": true,
+  "maxRuntimeInSeconds": 120
+}
+```
+
+**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
+
+::: zone-end
+
+A successful request returns `200 OK`. Confirm that `activity` contains an entry whose `type` is `workIQ` and whose `knowledgeSourceName` matches your Work IQ knowledge source. Also confirm that `references` contains a `workIQ` entry.
+
+The following table lists common configuration failures.
+
+| Status | Cause |
+| --- | --- |
+| 400 | The Work IQ authorization header is missing or malformed, required user claims are absent, or the search service doesn't have a supported managed identity configuration. |
+| 206 or 502 | The Work IQ source failed because token exchange, consent, the delegated permission, the federated credential, downstream authorization, or the Work IQ request failed or timed out. Inspect the source activity error. A `206` response means another source succeeded. A `502` response means every selected source failed or a required source failed. |
+
+### Work IQ-specific response fields
 
 Work IQ knowledge sources return results in the `references` array and query diagnostics in the `activity` array. Each reference entry contains:
 
-- `sourceData.extracts[].text`: Grounded text passages from Work IQ.
-- `attributions[].seeMoreWebUrl`: A link to the source document in Microsoft 365.
++ `sourceData.parts[].text`: Grounded text passages from Work IQ.
++ `sourceData.parts[].data`: Work IQ citation data. Citation parts have the media type `application/vnd.ms-workiq-reference`.
 
 The following example shows a retrieve response containing a Work IQ knowledge source reference and its corresponding activity record. For broader guidance on interpreting retrieve responses, see [Review the response](agentic-retrieval-how-to-retrieve.md#review-the-response).
 
@@ -235,23 +499,18 @@ The following example shows a retrieve response containing a Work IQ knowledge s
 
 ```json
 {
-  "response": [
-      // ... Response omitted for brevity
-  ],
+  "response": [],
   "activity": [
     {
       "type": "workIQ",
       "id": 0,
       "knowledgeSourceName": "my-workiq-ks",
-      "queryTime": "2026-05-01T19:25:23.683Z",
+      "queryTime": "2026-08-01T19:25:23.683Z",
       "count": 1,
       "elapsedMs": 1137,
       "workIQArguments": {
         "search": "my query"
       }
-    },
-    {
-       // ... Additional activity records omitted for brevity       
     }
   ],
   "references": [
@@ -260,21 +519,23 @@ The following example shows a retrieve response containing a Work IQ knowledge s
       "id": "83dd7d40",
       "activitySource": 0,
       "rerankerScore": 3.5,
-      "attributions": [
-        {
-          "seeMoreWebUrl": "https://..."
-        }
-      ],
       "sourceData": {
-        "extracts": [
+        "parts": [
           {
             "text": "Have your VPN username and password ready."
+          },
+          {
+            "data": {
+              "1-abc123": {
+                "targetLink": "https://contoso.sharepoint.com/doc.docx",
+                "isCitedInResponse": true,
+                "isSourceFiltered": false
+              }
+            },
+            "mediaType": "application/vnd.ms-workiq-reference"
           }
         ]
       }
-    },
-    {
-      // ... Additional references omitted for brevity
     }
   ]
 }
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Work IQ知識ソースのAPIおよび認証方法の変更"
}
```

### Explanation
この変更は、Azure AI SearchにおけるWork IQ知識ソースに関するドキュメントの大規模な更新を伴っており、主にAPIバージョンの更新と認証方法の変更が行われています。これにより、ユーザーは新しい機能と改善されたセキュリティを活用できるようになります。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：APIのバージョンが2026-05-01-previewから2026-08-01-previewに変更され、これにより新機能やパフォーマンスの改善が導入されています。

2. **認証プロセスの改善**：新しいAPIでは、Work IQ知識ソースを利用する際に、顧客所有のMicrosoft Entraアプリ登録を使用して認証を行う必要があります。これには、クライアントアプリがユーザーをサインインさせ、ユーザーアサーションを取得してAzure AI Searchに送信し、トークン交換を行う新しい手順が追加されています。

3. **データガバナンスとコンプライアンスの強調**：新しい情報が追加され、Work IQのリトリーバルを有効にする前に注意すべきデータのプライバシーやセキュリティに関するポイントが強調されています。

4. **サンプルコードの大規模な修正**：あなたのアプリケーションが新しいAPI機能をどのように活用できるかについての具体的な例が改訂され、構文の変更や新しい認証手順が反映されています。これにはC#, PythonおよびREST APIのサンプルが含まれています。

5. **新しいパラメータの追加**：Work IQ知識ソースの作成時に必要な`entraAppAuthentication`パラメータが導入され、これによりアプリケーションIDとフェデレーテッドクレデンシャルIDの管理が簡素化されます。

6. **エラーハンドリングとレスポンスフィールドの更新**：リトリーバルのレスポンスに含まれるフィールドが変更され、動作の正確性を確保するための新しいエラーハンドリングとデータ構造が導入されています。

この変更は多くの新しい機能と改善をもたらし、ユーザーにとってはより強力で安全な方法でWork IQ知識ソースを活用できるようになっています。ただし、これに伴う構成変更が必要なので、十分な注意と準備が求められます。

## articles/search/agentic-knowledge-source-overview.md{#item-dcf29a}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: What is a Knowledge Source?
 description: Learn about the knowledge source object used for agentic retrieval workloads in Azure AI Search.
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 07/30/2026
+ms.date: 08/14/2026
 ai-usage: ai-assisted
 ---
 
@@ -14,11 +14,9 @@ ai-usage: ai-assisted
 [!INCLUDE [GA announcement](./includes/previews/agentic-retrieval-ga-announcement.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
@@ -31,7 +29,7 @@ You can reference multiple knowledge sources in a single knowledge base. The age
 Azure AI Search supports the following knowledge sources for agentic retrieval workloads.
 
 | Kind | Description | Indexed or remote |
-|------|-------------|-------------------|
+| ------ | ------------- | ------------------- |
 | [Search index](agentic-knowledge-source-how-to-search-index.md) | Wraps an existing index. | Indexed |
 | [Azure blob](agentic-knowledge-source-how-to-blob.md) | Generates an indexer pipeline from a blob container. | Indexed |
 | [Azure SQL (preview)](agentic-knowledge-source-how-to-azure-sql.md) | Generates an indexer pipeline from an Azure SQL table or view. | Indexed |
@@ -55,7 +53,9 @@ An indexed knowledge source points to a search index that [meets the criteria fo
 
 + **Auto-generated indexer pipeline:** For all other indexed knowledge sources, Azure AI Search automatically creates a complete indexer pipeline from your external data source. This includes a [data source](search-data-sources-gallery.md), [skillset](cognitive-search-working-with-skillsets.md), [indexer](search-indexer-overview.md), and [index](search-what-is-an-index.md) that's populated and chunked.
 
-Queries run locally on your search service using keyword (full text), vector, or hybrid queries.
+Queries run locally on your search service using full-text (keyword), vector, or hybrid queries.
+
+Because an indexed knowledge source has a backing search index, references in the response can include service-generated [citation URLs (preview)](agentic-retrieval-how-to-retrieve.md#look-up-documents-with-citation-urls-preview) that resolve to their documents in the index. Remote knowledge sources have no backing index, so they don't return citation URLs.
 
 ### Remote knowledge sources
 
@@ -79,8 +79,6 @@ Knowledge sources are independent objects that you create and manage separately
 
 ## Creating knowledge sources
 
-To create a knowledge source, you need [**Search Service Contributor** permissions](search-security-rbac.md) on your search service. If the knowledge source generates an indexer pipeline, you also need **Search Index Data Contributor** permissions to load an index. You can use an [admin API key](search-security-api-keys.md) as an alternative to role assignments.
-
 Creation support in the Azure portal, Microsoft Foundry portal, REST API, and Azure SDKs varies by knowledge source kind. For per-kind instructions, see the links in [Supported knowledge sources](#supported-knowledge-sources).
 
 ### Ingest sensitivity labels (preview)
@@ -95,6 +93,12 @@ For blob, indexed OneLake, and indexed SharePoint knowledge sources, you can con
 
 Don't configure `assetStore` and `ingestionPermissionOptions` on the same knowledge source. Image serving isn't supported when `ingestionPermissionOptions` is configured.
 
+### Restrict ingestion to a private network (preview)
+
+Starting with the `2026-08-01-preview` API version, [blob](agentic-knowledge-source-how-to-blob.md#restrict-ingestion-to-a-private-network-preview), [indexed SharePoint](agentic-knowledge-source-how-to-sharepoint-indexed.md#protect-azure-dependencies-during-ingestion), and [indexed Azure SQL](agentic-knowledge-source-how-to-azure-sql.md#restrict-ingestion-to-a-private-network) knowledge sources support private indexer execution. For blob and Azure SQL, approved shared private links can protect the source connection and Azure dependencies. SharePoint Online isn't a shared private link target, so private mode applies only to its protected Azure dependencies.
+
+Currently, private synchronization isn't supported for [indexed OneLake knowledge sources](agentic-knowledge-source-how-to-onelake.md#limitations).
+
 ## Using knowledge sources
 
 After you create a knowledge source, reference it in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md). The knowledge base determines which knowledge sources to query. The following sections describe options for controlling which sources are included and how the engine selects among them.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ソース概要のAPIバージョン更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける知識ソースの概要に関するドキュメントに対する小規模な更新を含んでおり、主にAPIバージョンの変更と新しい機能の紹介に焦点を当てています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：ドキュメント内のAPIバージョンが2026-05-01-previewから2026-08-01-previewに変更され、これにより、新しい機能や仕様を反映した情報が提供されています。

2. **注意喚起の修正**：重要な情報ブロック内で、Microsoftサービスやサードパーティサービスに接続する際のデータ処理やストレージに関する責任について、より明確な表現が使用されています。

3. **クエリの説明の明確化**：クエリの種類についての説明が改善され、「フルテキスト（キーワード）、ベクトル、またはハイブリッドクエリを使用してローカルで実行される」という説明が明確になりました。

4. **引⽤URLの説明の追加**：インデックスされた知識ソースのレスポンスにおいて、サービス生成の引⽤URLが文書を解決する点に関する新しい情報が追加されています。

5. **プライベートネットワーク制限の新機能追加**：新しいセクションが追加され、特定の知識ソースがプライベートネットワークでの実行をサポートすることが記載され、ユーザーに対する新しいオプションが提供されています。

6. **全体的な内容の精査と整理**：ドキュメントの内容が精査され、理解しやすく整理が施されています。新たに追加された情報セクションによって、ユーザーが最新の機能や制限についても容易に理解できるようになっています。

これらの更新により、ドキュメントは最新のAzure AI Search APIの機能や使用法に則った情報をユーザーに提供し、利用効率の向上に寄与します。

## articles/search/agentic-retrieval-how-to-answer-synthesis.md{#item-f44e99}

<details>
<summary>Diff</summary>
````diff
@@ -15,9 +15,9 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [Preview feature](./includes/previews/agentic-retrieval-preview-feature.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -29,29 +29,41 @@ You can instead enable *answer synthesis* (preview), which uses the LLM specifie
 
 You can set this property in a knowledge base or a retrieve request. The knowledge base setting establishes the default for all queries, while the retrieve request setting overrides the default on a query-by-query basis.
 
+### Usage support
+
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-08-01-preview&preserve-view=true) |
+| -- | -- | -- | -- | -- | -- | -- |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + An Azure AI Search service with a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) that specifies an LLM.
 
-+ Permissions to update knowledge bases. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Permission to update knowledge bases. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 + For outbound calls to the LLM, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource.
 
 :::zone pivot="csharp"
 
 + The latest [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
+
 :::zone-end
 
 :::zone pivot="python"
 
 + The latest [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) preview package: `pip install --pre azure-search-documents`
 
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
+
 :::zone-end
 
 :::zone pivot="rest"
 
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
++ The [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) version of the Search Service REST API.
+
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 :::zone-end
 
@@ -67,19 +79,19 @@ This section demonstrates how to enable answer synthesis in an existing knowledg
 
 :::zone pivot="csharp"
 
-Set `OutputMode` to `"answerSynthesis"` on the `KnowledgeBase` definition. Optionally, set `AnswerInstructions` to customize the answer output. Our example instructs the knowledge base to `Use concise bulleted lists`.
+Set `OutputMode` to `"answerSynthesis"` on the `KnowledgeBase` definition. Optionally, set `AnswerInstructions` to customize the answer output. The following example instructs the knowledge base to `Use concise bulleted lists`.
 
 ```csharp
 var aoaiParams = new AzureOpenAIVectorizerParameters
 {
-    ResourceUri = new Uri(aoaiEndpoint),
-    DeploymentName = aoaiGptDeployment,
-    ModelName = aoaiGptModel,
+    ResourceUri = new Uri("<aoai-endpoint>"),
+    DeploymentName = "<aoai-gpt-deployment>",
+    ModelName = "<aoai-gpt-model>",
 };
 
 var knowledgeBase = new KnowledgeBase(
-    name: knowledgeBaseName,
-    knowledgeSources: new[] { new KnowledgeSourceReference(knowledgeSourceName) })
+    name: "<knowledge-base-name>",
+    knowledgeSources: new[] { new KnowledgeSourceReference("<knowledge-source-name>") })
 {
     Models = { new KnowledgeBaseAzureOpenAIModel(aoaiParams) },
     OutputMode = "answerSynthesis",
@@ -95,7 +107,7 @@ await indexClient.CreateOrUpdateKnowledgeBaseAsync(knowledgeBase);
 
 :::zone pivot="python"
 
-Set `output_mode` to `"answerSynthesis"` on the `KnowledgeBase` definition. Optionally, set `answer_instructions` to customize the answer output. Our example instructs the knowledge base to `Use concise bulleted lists`.
+Set `output_mode` to `"answerSynthesis"` on the `KnowledgeBase` definition. Optionally, set `answer_instructions` to customize the answer output. The following example instructs the knowledge base to `Use concise bulleted lists`.
 
 ```python
 from azure.search.documents.indexes import SearchIndexClient
@@ -107,15 +119,15 @@ from azure.search.documents.indexes.models import (
 )
 
 aoai_params = AzureOpenAIVectorizerParameters(
-    resource_url=aoai_endpoint,
-    deployment_name=aoai_gpt_deployment,
-    model_name=aoai_gpt_model,
+    resource_url="<aoai-endpoint>",
+    deployment_name="<aoai-gpt-deployment>",
+    model_name="<aoai-gpt-model>",
 )
 
 knowledge_base = KnowledgeBase(
-    name=knowledge_base_name,
+    name="<knowledge-base-name>",
     models=[KnowledgeBaseAzureOpenAIModel(azure_open_ai_parameters=aoai_params)],
-    knowledge_sources=[KnowledgeSourceReference(name=knowledge_source_name)],
+    knowledge_sources=[KnowledgeSourceReference(name="<knowledge-source-name>")],
     output_mode="answerSynthesis",
     answer_instructions="Use concise bulleted lists",
 )
@@ -130,13 +142,13 @@ index_client.create_or_update_knowledge_base(knowledge_base)
 
 :::zone pivot="rest"
 
-Set `outputMode` to `"answerSynthesis"` on the knowledge base definition. Optionally, set `answerInstructions` to customize the answer output. Our example instructs the knowledge base to `Use concise bulleted lists`.
+Set `outputMode` to `"answerSynthesis"` on the knowledge base definition. Optionally, set `answerInstructions` to customize the answer output. The following example instructs the knowledge base to `Use concise bulleted lists`.
 
 ```http
 ### Enable answer synthesis in a knowledge base
-PUT {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version=2026-05-01-preview
+PUT {{search-endpoint}}/knowledgebases/{{knowledge-base-name}}?api-version=2026-08-01-preview
 Content-Type: application/json
-api-key: {{api-key}}
+Authorization: Bearer {{search-access-token}}
 
 {
     "name": "{{knowledge-base-name}}",
@@ -147,7 +159,7 @@ api-key: {{api-key}}
 }
 ```
 
-**Reference:** [Knowledge Base - Create or Update](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Base - Create or Update](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 :::zone-end
 
@@ -222,9 +234,9 @@ Set `outputMode` to `"answerSynthesis"` on a retrieve request.
 
 ```http
 ### Enable answer synthesis in a retrieve request
-POST {{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2026-05-01-preview
+POST {{search-endpoint}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2026-08-01-preview
 Content-Type: application/json
-api-key: {{api-key}}
+Authorization: Bearer {{search-access-token}}
 
 {
     "messages": [
@@ -242,15 +254,15 @@ api-key: {{api-key}}
 }
 ```
 
-**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 :::zone-end
 
 ## Get a synthesized answer
 
 When answer synthesis is enabled, the knowledge base returns a natural-language answer based on the instructions you optionally specified in the knowledge base. Citations to your knowledge sources are formatted as `[ref_id:<number>]`.
 
-For example, if your instructions are `Use concise bulleted lists` and your query is `What is healthcare?`, the response might look like this:
+For example, if your instructions are `Use concise bulleted lists` and your query is `What is healthcare?`, the response should be similar to the following example.
 
 ```json
 {
@@ -280,4 +292,4 @@ Depending on your knowledge base's configuration, the response might include oth
 - [Create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md)
 - [Query a knowledge base](agentic-retrieval-how-to-retrieve.md)
 - [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md) (uses answer synthesis)
-- [Python sample: Azure AI Search blob knowledge source](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/knowledge/blob-knowledge-source.ipynb) (uses answer synthesis)
\ No newline at end of file
+- [Python sample: Azure AI Search blob knowledge source](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/knowledge/blob-knowledge-source.ipynb) (uses answer synthesis)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "回答合成機能のAPIバージョン更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける回答合成機能に関するドキュメントの更新を示しており、主にAPIバージョンの更新と使用方法の改善が含まれています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：ドキュメント内のAPIバージョンが2026-05-01-previewから2026-08-01-previewに変更され、これにより新しい機能や改善を利用するための最新情報が提供されています。

2. **重要なセクションのリビジョン**：重要な注意喚起のセクションでは、Azureサブスクリプションに関連する条件や、他のMicrosoftサービスやサードパーティサービスとの接続に関する内容が更新されています。

3. **使用サポートの表の追加**：Azureポータルや各種SDKに対するサポートの状態が一目でわかる表が追加され、ユーザーが必要な情報を迅速に得られるようになっています。

4. **知識ベースおよび更新権限に関する変更**：ユーザーが必要な権限を得るための要件がわかりやすく記述され、キーなし認証の設定が簡素化されています。

5. **具体的なコード例の修正**：C#やPython、REST APIのセクションで、具体的なコード例が改善され、可読性が向上しました。また、パラメータ名がプレースホルダーで示されるようになり、ユーザーによるカスタマイズが容易になっています。

6. **サンプルレスポンスの改善**：回答合成が有効化された場合のレスポンスサンプルがより具体的に示され、ユーザーが期待される出力形式についての理解が深められています。

これらの更新は、回答合成機能を利用する際の使い勝手を向上させることを目的としており、ユーザーにとってより効果的な情報取得の手助けとなります。

## articles/search/agentic-retrieval-how-to-configure-freshness.md{#item-0b04e6}

<details>
<summary>Diff</summary>
````diff
@@ -13,9 +13,9 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -25,29 +25,41 @@ zone_pivot_groups: search-csharp-python-rest
 
 Freshness is a ranking bias, not a hard filter. Older documents can still appear when they're strongly relevant to the query.
 
+### Usage support
+
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-08-01-preview&preserve-view=true) |
+| -- | -- | -- | -- | -- | -- | -- |
+| ❌ | ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + An [indexed knowledge source](agentic-knowledge-source-overview.md#supported-knowledge-sources) that creates and maintains an Azure AI Search index, such as a blob knowledge source.
 
 + A [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) that references the knowledge source.
 
-+ Permissions to update knowledge bases. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Permission to update knowledge bases. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 ::: zone pivot="csharp"
 
 + The latest [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
+
 ::: zone-end
 
 ::: zone pivot="python"
 
 + The latest [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) preview package: `pip install --pre azure-search-documents`
 
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
+
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
++ The [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) version of the Search Service REST API.
+
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
@@ -61,7 +73,7 @@ Don't use freshness as a replacement for filtering. If a query must only return
 
 Add a freshness policy to the indexed knowledge source definition. The preview contract uses the policy to apply a recency-aware ranking signal while preserving the rest of the retrieval pipeline.
 
-The following example shows a blob knowledge source with a freshness policy:
+The following example shows a blob knowledge source with a freshness policy.
 
 ::: zone pivot="csharp"
 
@@ -115,9 +127,9 @@ index_client.create_or_update_knowledge_source(knowledge_source)
 ::: zone pivot="rest"
 
 ```http
-PUT {{search-url}}/knowledgesources/news-articles-ks?api-version=2026-05-01-preview
+PUT {{search-endpoint}}/knowledgesources/news-articles-ks?api-version=2026-08-01-preview
 Content-Type: application/json
-api-key: {{search-api-key}}
+Authorization: Bearer {{search-access-token}}
 
 {
   "name": "news-articles-ks",
@@ -135,7 +147,7 @@ api-key: {{search-api-key}}
 }
 ```
 
-**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フレッシュネス設定に関するAPIバージョン更新"
}
```

### Explanation
この変更は、Azure AI Searchのフレッシュネス設定に関するドキュメントの更新を含んでおり、主にAPIバージョンの更新と内容の追加に焦点を当てています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：ドキュメント内のAPIバージョンが2026-05-01-previewから2026-08-01-previewに変更され、新機能や最適化された使用法を提供することが明示されています。

2. **重要な通知の更新**：重要なセクションにおいて、Azureサブスクリプションに関連する条件や外部サービスとの接続に関する注意が強調されています。

3. **使用サポートの表の追加**：AzureポータルやSDKに対するサポート状況が表形式で示され、ユーザーが必要な情報を簡単に確認できるようになりました。

4. **前提条件の明確化**：インデックス付き知識ソースや知識ベースに関する要件が再確認され、必要な権限についての明確な情報が提供されるようになりました。特に、キーなし認証の設定について新たに管理者APIキーの使用が推奨されています。

5. **コード例の修正と改善**：C#、Python、REST APIセクションで具体的なコード例が改善され、可読性と実用性が向上しました。特に、プレースホルダーを使ってユーザーがどの値を適用すべきかがよりわかりやすく表現されています。

6. **フレッシュネスポリシーの適用に関する情報の強調**：新たに、フレッシュネスポリシーを設定する重要性が強調されており、どのように検索結果に影響を及ぼすかについての具体的な事例が示されています。

これらの更新により、フレッシュネス機能およびAPIの最新情報が効果的にユーザーに提供され、Azure AI Searchの使用をより円滑にすることを目的としています。

## articles/search/agentic-retrieval-how-to-create-index.md{#item-3fbd2e}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ Each indexed knowledge source depends on an underlying index. Depending on how y
 The following table organizes the index elements that affect agentic retrieval by requirement level.
 
 | Index element | Requirement | Notes |
-|---|---|---|
+| --- | --- | --- |
 | [`searchable` and `retrievable` string fields](search-what-is-an-index.md#field-attributes) | Required | Used for query execution and result retrieval. |
 | [Semantic configuration](#add-a-semantic-configuration) | Required | Use `defaultSemanticConfiguration` or override the semantic configuration in the knowledge source. |
 | Citation fields | Recommended | User-defined fields that attribute responses to source content, such as document name, page number, or chunk ID. |
@@ -37,12 +37,12 @@ The following table organizes the index elements that affect agentic retrieval b
 
 ## Example index definition
 
-Here's an example index that works for agentic retrieval. It meets the criteria for required elements and includes vector fields as a best practice.
+The following example shows an index that works for agentic retrieval. It meets the criteria for required elements and includes vector fields as a best practice.
 
 ```json
 {
   "name": "earth_at_night",
-  "description": "Contains images an descriptions of our planet in darkness as captured from space by Earth-observing satellites and astronauts on the International Space Station over the past 25 years.",
+  "description": "Contains images and descriptions of our planet in darkness as captured from space by Earth-observing satellites and astronauts on the International Space Station over the past 25 years.",
   "fields": [
     {
       "name": "id", "type": "Edm.String",
@@ -123,7 +123,6 @@ Here's an example index that works for agentic retrieval. It meets the criteria
         "azureOpenAIParameters": {
           "resourceUri": "https://YOUR-AOAI-RESOURCE.openai.azure.com",
           "deploymentId": "text-embedding-3-large",
-          "apiKey": "<redacted>",
           "modelName": "text-embedding-3-large"
         }
       }
@@ -157,7 +156,7 @@ By default, all `searchable` fields are included in query execution, and all `re
 
 ## Add a description
 
-An index `description` field is a user-defined string that you can use to provide guidance to LLMs and Model Context Protocol (MCP) servers when deciding to use a specific index for a query. This human-readable text is invaluable when a system must access several indexes and make a decision based on the description. 
+An index `description` field is a user-defined string that you can use to provide guidance to LLMs and Model Context Protocol (MCP) servers when deciding to use a specific index for a query. This human-readable text is invaluable when a system must access several indexes and make a decision based on the description.
 
 An index description is a schema update, and you can add it without having to rebuild the entire index.
 
@@ -176,7 +175,7 @@ There are two ways to specify a semantic configuration by name. If the index has
 
 Within the configuration, `prioritizedContentFields` is required. Title and keywords are optional. For chunked content, you might not have either. However, if you add [entity recognition](cognitive-search-skill-entity-recognition-v3.md) or [key phrase extraction](cognitive-search-skill-keyphrases.md), you might have some keywords associated with each chunk that can be useful in search scenarios, perhaps in a scoring profile.
 
-Here's an example of a semantic configuration that works for agentic retrieval:
+The following example shows a semantic configuration that works for agentic retrieval.
 
 ```json
 "semantic":{
@@ -186,27 +185,25 @@ Here's an example of a semantic configuration that works for agentic retrieval:
          "name":"semantic_config",
          "flightingOptIn":false,
          "prioritizedFields":{
-            "prioritizedFields":{
-               "titleField":{
-                  "fieldName":""
+            "titleField":{
+               "fieldName":""
+            },
+            "prioritizedContentFields":[
+               {
+                  "fieldName":"page_chunk"
+               }
+            ],
+            "prioritizedKeywordsFields":[
+               {
+                  "fieldName":"Category"
                },
-               "prioritizedContentFields":[
-                  {
-                     "fieldName":"page_chunk"
-                  }
-               ],
-               "prioritizedKeywordsFields":[
-                  {
-                     "fieldName":"Category"
-                  },
-                  {
-                     "fieldName":"Tags"
-                  },
-                  {
-                     "fieldName":"Location"
-                  }
-               ]
-            }
+               {
+                  "fieldName":"Tags"
+               },
+               {
+                  "fieldName":"Location"
+               }
+            ]
          }
       }
    ]
@@ -239,7 +236,7 @@ Vector profiles are configurations of vectorizers, algorithms, and compression t
 
 Querying vectors and calling a vectorizer adds latency to the overall request, but if you want similarity search, it might be worth the trade-off.
 
-Here's an example of a vectorizer that works for agentic retrieval, as it appears in a vectorSearch configuration. There's nothing in the vectorizer definition that needs to be changed to work with agentic retrieval.
+The following example shows a vectorizer that works for agentic retrieval as it appears in a vectorSearch configuration. There's nothing in the vectorizer definition that needs to be changed to work with agentic retrieval.
 
 ```json
 "vectorSearch": {
@@ -269,7 +266,6 @@ Here's an example of a vectorizer that works for agentic retrieval, as it appear
       "azureOpenAIParameters": {
         "resourceUri": "https://YOUR-AOAI-RESOURCE.openai.azure.com",
         "deploymentId": "text-embedding-3-large",
-        "apiKey": "<redacted>",
         "modelName": "text-embedding-3-large"
       }
     }
@@ -280,13 +276,13 @@ Here's an example of a vectorizer that works for agentic retrieval, as it appear
 
 ## Add a scoring profile
 
-[Scoring profiles](index-add-scoring-profiles.md) are criteria for relevance boosting. They're applied to non-vector fields (text and numbers) and are evaluated during query execution, although the precise behavior depends on the API version used to create the index. 
+[Scoring profiles](index-add-scoring-profiles.md) are criteria for relevance boosting. They're applied to non-vector fields (text and numbers) and are evaluated during query execution, although the precise behavior depends on the API version used to create the index.
 
 A scoring profile is more likely to add value to your solution if your index is based on structured data. Structured data is indexed into multiple discrete fields, which means your scoring profile can have criteria that target the content or characteristics of a specific field.
 
 If you create the index using 2025-05-01-preview or later, the scoring profile executes last. If the index is created using an earlier API version, scoring profiles are evaluated before semantic reranking. The actual order of semantically ranked results is determined by the [rankingOrder property](/rest/api/searchservice/indexes/create-or-update#rankingorder) in the index, which is either set to `boostedRerankerScore` (a scoring profile was applied) or `rerankerScore` (no scoring profile).
 
-You can use any scoring profile that makes sense for your index. Here's an example of one that boosts the search score of a match if the match is found in a specific field. Fields are weighted by boosting multipliers. For example, if a match is found in the "Category" field, the boosted score is multiplied by 5.
+You can use any scoring profile that makes sense for your index. The following example shows a scoring profile that boosts the search score of a match if the match is found in a specific field. Fields are weighted by boosting multipliers. For example, if a match is found in the "Category" field, the boosted score is multiplied by 5.
 
 ```json
 "scoringProfiles": [
@@ -295,7 +291,7 @@ You can use any scoring profile that makes sense for your index. Here's an examp
       "text": {
         "weights": {
           "Location": 2,
-          "Category": 5 
+          "Category": 5
         }
       }
     }
@@ -322,7 +318,7 @@ Analyzers are defined within a search index and assigned to fields. The [fields
 
 [Synonym maps](search-synonyms.md) expand queries by adding synonyms for named terms. For example, you might have scientific or medical terms for common terms.
 
-Synonym maps are defined as a top-level resource on a search index and assigned to fields. The [fields collection example](#example-index-definition) doesn't include a synonym map, but if you had variant spellings of country names in a synonym map, here's what an example might look like if it was assigned to a hypothetical "locations" field.
+Synonym maps are defined as a top-level resource on a search index and assigned to fields. The [fields collection example](#example-index-definition) doesn't include a synonym map, but the following example shows how a synonym map with variant spellings of country names might be assigned to a hypothetical "locations" field.
 
 ```json
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス作成に関する内容の改善"
}
```

### Explanation
この変更は、Azure AI Searchのインデックス作成に関するドキュメントの改訂を示しており、主に内容の追加、説明の明確化、エラーの修正がなされています。

主な変更点は以下の通りです：

1. **説明の明確化**：インデックスの要素や構成についての説明がより具体的にされており、特にインデックス要素の必要性が強調されています。たとえば、`searchable`および`retrievable`な文字列フィールドがクエリ実行と結果取得に必要である旨が明記されています。

2. **インデックス定義の改善**：インデックスの具体例が提供され、それがエージェント検索にどのように適応できるかが示されています。特に、ベクトルフィールドが最良の実践として含まれていることが説明されています。

3. **セマンティック構成の例の改善**：セマンティック構成に関する部分が簡潔に整理され、使用例と共に具体的な構成の説明が追加されています。これにより、セマンティック機能の利用法がより理解しやすくなっています。

4. **スコアリングプロファイルの詳細の追加**：スコアリングプロファイルの概念が強化され、特定のフィールドでマッチしたときにスコアをブーストする方法が具体的な例を通じて示されています。

5. **同義語マップの使用例の明確化**：同義語マップが検索インデックスにどのように適用されるかについての具体例が追加され、異なる国名の表記揺れを扱う方法についても言及されています。

6. **文法の修正**：全体を通じて文法の改善がされており、流れるような文章が多く出てきたことで、読みやすさが向上しています。

これらの変更により、インデックス作成のトピックに関する理解が深まり、ユーザーがAzure AI Searchを効果的に活用する助けとなることを目的としています。

## articles/search/agentic-retrieval-how-to-create-knowledge-base.md{#item-7df0e2}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,10 @@ title: Create a Knowledge Base
 description: Learn how to create a knowledge base for agentic retrieval workloads in Azure AI Search.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/06/2026
+ms.date: 08/12/2026
+ms.custom:
+  - dev-focus
+  - doc-kit-assisted
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
@@ -15,18 +18,16 @@ zone_pivot_groups: search-csharp-python-rest
 [!INCLUDE [GA feature](./includes/previews/agentic-retrieval-ga-feature.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
 In Azure AI Search, a *knowledge base* is a top-level object that orchestrates [agentic retrieval](agentic-retrieval-overview.md). It defines which knowledge sources to query and the default behavior for retrieval operations. At query time, the [retrieve method](agentic-retrieval-how-to-retrieve.md) targets the knowledge base to run the configured retrieval pipeline.
 
-You can create a knowledge base in a [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) workload in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
-
 A knowledge base specifies:
 
 + One or more knowledge sources that point to searchable content.
@@ -38,74 +39,82 @@ A knowledge base specifies:
 ### Usage support
 
 | [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases) |
-|--|--|--|--|--|--|--|
+| -- | -- | -- | -- | -- | -- | -- |
 | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](search-region-support.md). If you're using a [managed identity](search-how-to-managed-identities.md) for role-based access to deployed models, your search service must be on the Basic tier or higher.
 
-+ One or more [knowledge sources](agentic-knowledge-source-overview.md#supported-knowledge-sources). Use the 2026-05-01-preview API version to access preview knowledge sources or to use an LLM with non-web knowledge sources. Use the 2026-04-01 API version for generally available knowledge sources and minimal, extractive retrieval.
++ One or more [knowledge sources](agentic-knowledge-source-overview.md#supported-knowledge-sources). Use the `2026-08-01-preview` API version to access preview knowledge sources or to use an LLM with non-web knowledge sources. Use the `2026-04-01` API version for generally available knowledge sources and minimal, extractive retrieval.
 
-+ (Conditional) Azure OpenAI with a [supported LLM](#supported-models) deployment. An LLM is required if your knowledge base includes a web knowledge source. For other knowledge sources, an LLM is optional in the 2026-05-01-preview API version and unsupported in the 2026-04-01 API version.
++ (Conditional) Azure OpenAI with a [supported LLM](#supported-models) deployment. An LLM is required if your knowledge base includes a web knowledge source. For other knowledge sources, an LLM is optional in the `2026-08-01-preview` API version and unsupported in the `2026-04-01` API version.
 
-+ Permissions to create knowledge bases. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Permission to create knowledge bases. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 + If the knowledge base specifies an LLM, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource.
 
 ::: zone pivot="csharp"
 
 + Required [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) package:
 
-  + For 2026-05-01-preview features, the latest preview package: `dotnet add package Azure.Search.Documents --prerelease`
+  + For `2026-08-01-preview` features, the latest preview package: `dotnet add package Azure.Search.Documents --prerelease`
+
+  + For `2026-04-01` features, the latest stable package: `dotnet add package Azure.Search.Documents`
 
-  + For 2026-04-01 features, the latest stable package: `dotnet add package Azure.Search.Documents`
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
 
 ::: zone-end
 
 ::: zone pivot="python"
 
 + Required [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) package:
 
-  + For 2026-05-01-preview features, the latest preview package: `pip install --pre azure-search-documents`
+  + For `2026-08-01-preview` features, the latest preview package: `pip install --pre azure-search-documents`
+
+  + For `2026-04-01` features, the latest stable package: `pip install azure-search-documents`
 
-  + For 2026-04-01 features, the latest stable package: `pip install azure-search-documents`
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
 
 ::: zone-end
 
 ::: zone pivot="rest"
 
-+ Required REST API version:
++ Required Search Service REST API version:
 
-  + For preview features: [Search Service 2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+  + For preview features: [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
-  + For generally available features: [Search Service 2026-04-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true)
+  + For generally available features: [2026-04-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true)
+
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
 ::: zone-end
 
 ### Supported models
 
 Use one of the following LLMs from Azure OpenAI in Foundry Models. Azure OpenAI determines regional availability for the deployment you select. For deployment instructions, see [Deploy Microsoft Foundry Models in the Foundry portal](/azure/ai-foundry/how-to/deploy-models-openai).
 
-For the latest model lifecycle guidance, including deprecations, review [Model retirement and deprecation](/azure/ai-foundry/openai/concepts/model-retirements).
-
-GPT-4 family models are deprecated. For retirement dates and current status in Microsoft Foundry, see [Model retirement schedule - Microsoft Foundry](/azure/foundry/openai/concepts/model-retirement-schedule).
+The GPT-4 family is deprecated. For model lifecycle guidance, retirement dates, and current status, see [Model retirement and deprecation](/azure/ai-foundry/openai/concepts/model-retirements) and [Model retirement schedule - Microsoft Foundry](/azure/foundry/openai/concepts/model-retirement-schedule).
 
 | Model | Supported API versions |
-|--|--|
-| `gpt-4o` (deprecated) | 2025-11-01-preview, 2026-05-01-preview |
-| `gpt-4o-mini` (deprecated) | 2025-11-01-preview, 2026-05-01-preview |
-| `gpt-4.1` (deprecated) | 2025-11-01-preview, 2026-05-01-preview |
-| `gpt-4.1-mini` (deprecated) | 2025-11-01-preview, 2026-05-01-preview |
-| `gpt-4.1-nano` (deprecated) | 2025-11-01-preview, 2026-05-01-preview |
-| `gpt-5` | 2025-11-01-preview, 2026-05-01-preview |
-| `gpt-5-mini` | 2025-11-01-preview, 2026-05-01-preview |
-| `gpt-5-nano` | 2025-11-01-preview, 2026-05-01-preview |
-| `gpt-5.1` | 2026-05-01-preview |
-| `gpt-5.2` | 2026-05-01-preview |
-| `gpt-5.4` | 2026-05-01-preview |
-| `gpt-5.4-mini` | 2026-05-01-preview |
-| `gpt-5.4-nano` | 2026-05-01-preview |
+| -- | -- |
+| `gpt-4o` (deprecated) | 2025-11-01-preview, 2026-05-01-preview, 2026-08-01-preview |
+| `gpt-4o-mini` (deprecated) | 2025-11-01-preview, 2026-05-01-preview, 2026-08-01-preview |
+| `gpt-4.1` (deprecated) | 2025-11-01-preview, 2026-05-01-preview, 2026-08-01-preview |
+| `gpt-4.1-mini` (deprecated) | 2025-11-01-preview, 2026-05-01-preview, 2026-08-01-preview |
+| `gpt-4.1-nano` (deprecated) | 2025-11-01-preview, 2026-05-01-preview, 2026-08-01-preview |
+| `gpt-5` | 2025-11-01-preview, 2026-05-01-preview, 2026-08-01-preview |
+| `gpt-5-mini` | 2025-11-01-preview, 2026-05-01-preview, 2026-08-01-preview |
+| `gpt-5-nano` | 2025-11-01-preview, 2026-05-01-preview, 2026-08-01-preview |
+| `gpt-5.1` | 2026-05-01-preview, 2026-08-01-preview |
+| `gpt-5.2` | 2026-05-01-preview, 2026-08-01-preview |
+| `gpt-5.4` | 2026-05-01-preview, 2026-08-01-preview |
+| `gpt-5.4-mini` | 2026-05-01-preview, 2026-08-01-preview |
+| `gpt-5.4-nano` | 2026-05-01-preview, 2026-08-01-preview |
+| `gpt-5.5` | 2026-08-01-preview |
+| `gpt-5.6-sol` | 2026-08-01-preview |
+| `gpt-5.6-terra` | 2026-08-01-preview |
+| `gpt-5.6-luna` | 2026-08-01-preview |
 
 ## Configure access
 
@@ -121,13 +130,13 @@ Azure AI Search needs access to the LLM from Azure OpenAI in Foundry Models. We
 
 1. On your model provider, assign **Cognitive Services User** to the managed identity of your search service. If you're testing locally, assign the same role to your user account.
 
-1. For local testing, follow the steps in [Quickstart: Connect without keys](search-get-started-rbac.md) to sign in to a specific subscription and tenant. Use `DefaultAzureCredential` instead of `AzureKeyCredential` in each request, which should look similar to the following example:
+1. For local testing, follow the steps in [Quickstart: Connect without keys](search-get-started-rbac.md) to sign in to a specific subscription and tenant. Use `DefaultAzureCredential` instead of `AzureKeyCredential` in each request, which should be similar to the following example.
 
     ```csharp
     // Authenticate using roles
     using Azure.Search.Documents.Indexes;
     using Azure.Identity;
-    
+
     var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
     ```
 
@@ -141,12 +150,12 @@ Azure AI Search needs access to the LLM from Azure OpenAI in Foundry Models. We
 
 1. On your model provider, assign **Cognitive Services User** to the managed identity of your search service. If you're testing locally, assign the same role to your user account.
 
-1. For local testing, follow the steps in [Quickstart: Connect without keys](search-get-started-rbac.md) to sign in to a specific subscription and tenant. Use `DefaultAzureCredential` instead of `AzureKeyCredential` in each request, which should look similar to the following example:
+1. For local testing, follow the steps in [Quickstart: Connect without keys](search-get-started-rbac.md) to sign in to a specific subscription and tenant. Use `DefaultAzureCredential` instead of `AzureKeyCredential` in each request, which should be similar to the following example.
 
     ```python
     # Authenticate using roles
     from azure.identity import DefaultAzureCredential
-    index_client = SearchIndexClient(endpoint = "search_url", credential = DefaultAzureCredential())
+    index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
     ```
 
 ::: zone-end
@@ -159,13 +168,13 @@ Azure AI Search needs access to the LLM from Azure OpenAI in Foundry Models. We
 
 1. On your model provider, assign **Cognitive Services User** to the managed identity of your search service. If you're testing locally, assign the same role to your user account.
 
-1. For local testing, follow the steps in [Quickstart: Connect without keys](search-get-started-rbac.md) to get a personal access token for a specific subscription and tenant. Specify your access token in each request, which should look similar to the following example:
+1. For local testing, follow the steps in [Quickstart: Connect without keys](search-get-started-rbac.md) to get a personal access token for a specific subscription and tenant. Specify your access token in each request, which should be similar to the following example.
 
     ```http
     # List indexes using roles
-    GET https://{{search-url}}/indexes?api-version=2026-04-01
+    GET {{search-endpoint}}/indexes?api-version=2026-04-01
     Content-Type: application/json
-    Authorization: Bearer {{access-token}}
+    Authorization: Bearer {{search-access-token}}
     ```
 
 ::: zone-end
@@ -176,13 +185,13 @@ Azure AI Search needs access to the LLM from Azure OpenAI in Foundry Models. We
 
 1. [Copy an Azure AI Search admin API key](search-security-api-keys.md#find-existing-keys) from the Azure portal.
 
-1. Use `AzureKeyCredential` to specify the API key in each request, which should look similar to the following example:
+1. Use `AzureKeyCredential` to specify the API key in each request, which should be similar to the following example.
 
     ```csharp
     // Authenticate using keys
     using Azure.Search.Documents.Indexes;
     using Azure;
-    
+
     var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
     ```
 
@@ -192,12 +201,12 @@ Azure AI Search needs access to the LLM from Azure OpenAI in Foundry Models. We
 
 1. [Copy an Azure AI Search admin API key](search-security-api-keys.md#find-existing-keys) from the Azure portal.
 
-1. Use `AzureKeyCredential` to specify the API key in each request, which should look similar to the following example:
+1. Use `AzureKeyCredential` to specify the API key in each request, which should be similar to the following example.
 
     ```python
     # Authenticate using keys
     from azure.core.credentials import AzureKeyCredential
-    index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+    index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = AzureKeyCredential("api_key"))
     ```
 
 ::: zone-end
@@ -206,11 +215,11 @@ Azure AI Search needs access to the LLM from Azure OpenAI in Foundry Models. We
 
 1. [Copy an Azure AI Search admin API key](search-security-api-keys.md#find-existing-keys) from the Azure portal.
 
-1. Specify the API key in each request, which should look similar to the following example:
+1. Specify the API key in each request, which should be similar to the following example.
 
    ```http
    # List indexes using keys
-   GET {{search-url}}/indexes?api-version=2026-04-01
+   GET {{search-endpoint}}/indexes?api-version=2026-04-01
    Content-Type: application/json
    api-key: {{search-api-key}}
    ```
@@ -220,7 +229,7 @@ Azure AI Search needs access to the LLM from Azure OpenAI in Foundry Models. We
 ---
 
 > [!IMPORTANT]
-> Code snippets in this article use API keys. If you use role-based authentication, update each request accordingly. In a request that specifies both approaches, the API key takes precedence.
+> The code snippets in this article use keyless authentication. To use an API key instead, update each request accordingly. In a request that specifies both approaches, the API key takes precedence.
 
 ## Check for existing knowledge bases
 
@@ -233,12 +242,12 @@ Run the following code to list existing knowledge bases by name. The list includ
 ```csharp
 // List knowledge bases by name
 using Azure.Search.Documents.Indexes;
-  
+
 var indexClient = new SearchIndexClient(new Uri(searchEndpoint), credential);
 var knowledgeBases = indexClient.GetKnowledgeBasesAsync();
-  
+
 Console.WriteLine("Knowledge Bases:");
-  
+
 await foreach (var kb in knowledgeBases)
 {
     Console.WriteLine($"  - {kb.Name}");
@@ -253,10 +262,10 @@ await foreach (var kb in knowledgeBases)
 
 ```python
 # List knowledge bases by name
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
 for kb in index_client.list_knowledge_bases():
     print(f"  - {kb.name}")
@@ -270,9 +279,9 @@ for kb in index_client.list_knowledge_bases():
 
 ```http
 # List knowledge bases
-GET {{search-url}}/knowledgebases?api-version={{api-version}}&$select=name
+GET {{search-endpoint}}/knowledgebases?api-version={{api-version}}&$select=name
 Content-Type: application/json
-api-key: {{search-api-key}}
+Authorization: Bearer {{search-access-token}}
 ```
 
 **Reference:** [Knowledge Bases - List](/rest/api/searchservice/knowledge-bases/list)
@@ -309,13 +318,13 @@ Console.WriteLine(json);
 
 ```python
 # Get a knowledge base definition
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 import json
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
-kb = index_client.get_knowledge_base("knowledge_base_name")
+kb = index_client.get_knowledge_base("<knowledge-base-name>")
 print(json.dumps(kb.as_dict(), indent = 2))
 ```
 
@@ -327,9 +336,9 @@ print(json.dumps(kb.as_dict(), indent = 2))
 
 ```http
 # Get knowledge base
-GET {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version={{api-version}}
+GET {{search-endpoint}}/knowledgebases/{{knowledge-base-name}}?api-version={{api-version}}
 Content-Type: application/json
-api-key: {{search-api-key}}
+Authorization: Bearer {{search-access-token}}
 ```
 
 **Reference:** [Knowledge Bases - Get](/rest/api/searchservice/knowledge-bases/get)
@@ -359,53 +368,52 @@ The following JSON is an example response for a knowledge base.
 ```
 
 > [!NOTE]
-> The response schema reflects the API version you used to create the knowledge base. A knowledge base created with the generally available 2026-04-01 API version returns a narrower definition than the 2026-05-01-preview. For more information about which properties each version supports, see [Create a knowledge base](#create-a-knowledge-base).
+> The response schema reflects the API version you used to create the knowledge base. A knowledge base created with the generally available `2026-04-01` API version returns a narrower definition than the `2026-08-01-preview`. For more information about which properties each version supports, see [Create a knowledge base](#create-a-knowledge-base).
 
 ## Create a knowledge base
 
 > [!IMPORTANT]
-> The 2026-04-01 API version only accepts generally available knowledge source types and supports minimal, extractive retrieval. Preview-only capabilities, such as query planning, answer synthesis, and configurable reasoning effort, aren't supported. For full functionality, use the 2026-05-01-preview.
+> The `2026-04-01` API version only accepts generally available knowledge source types and supports minimal, extractive retrieval. It doesn't support preview-only capabilities, such as query planning, answer synthesis, and configurable reasoning effort. For full functionality, use the `2026-08-01-preview`.
 
 A knowledge base connects one or more knowledge sources (searchable content) to an optional LLM from Azure OpenAI in Foundry Models. The properties you set establish defaults for query execution and the retrieval response.
 
 After you create a knowledge base, you can update its properties at any time. If the knowledge base is in use, updates take effect on the next retrieval.
 
 ::: zone pivot="csharp"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```csharp
 // Create a knowledge base
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 using Azure.Search.Documents.KnowledgeBases.Models;
-using Azure;
+using Azure.Identity;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var aoaiParams = new AzureOpenAIVectorizerParameters
 {
     ResourceUri = new Uri(aoaiEndpoint),
     DeploymentName = aoaiGptDeployment,
     ModelName = aoaiGptModel,
-    ApiKey = aoaiApiKey
 };
 
 var knowledgeBase = new KnowledgeBase(
     name: "my-kb",
-    knowledgeSources: new KnowledgeSourceReference[] 
-    { 
+    knowledgeSources: new KnowledgeSourceReference[]
+    {
         new KnowledgeSourceReference("hotels-ks"),
         new KnowledgeSourceReference("earth-at-night-ks")
     }
 )
 {
     Description = "This knowledge base handles questions directed at two unrelated sample indexes.",
     RetrievalInstructions = "Use the hotels knowledge source for queries about where to stay, otherwise use the earth at night knowledge source.",
-    AnswerInstructions = "Provide a two-sentence, concise, and informative answer based on the retrieved documents.",
+    AnswerInstructions = "Answer in two concise sentences.",
     OutputMode = KnowledgeRetrievalOutputMode.AnswerSynthesis,
     Models = { new KnowledgeBaseAzureOpenAIModel(azureOpenAIParameters: aoaiParams) },
-    RetrievalReasoningEffort = new KnowledgeRetrievalLowReasoningEffort()
+    RetrievalReasoningEffort = new KnowledgeRetrievalAutoReasoningEffort()
 };
 
 await indexClient.CreateOrUpdateKnowledgeBaseAsync(knowledgeBase);
@@ -420,14 +428,14 @@ Console.WriteLine($"Knowledge base '{knowledgeBase.Name}' created or updated suc
 // Create a knowledge base
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
-using Azure;
+using Azure.Identity;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var knowledgeBase = new KnowledgeBase(
     name: "my-kb",
-    knowledgeSources: new KnowledgeSourceReference[] 
-    { 
+    knowledgeSources: new KnowledgeSourceReference[]
+    {
         new KnowledgeSourceReference("hotels-ks"),
         new KnowledgeSourceReference("earth-at-night-ks")
     }
@@ -448,42 +456,44 @@ Console.WriteLine($"Knowledge base '{knowledgeBase.Name}' created or updated suc
 
 ::: zone pivot="python"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```python
 # Create a knowledge base
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import (
     AzureOpenAIVectorizerParameters,
     KnowledgeBase,
     KnowledgeBaseAzureOpenAIModel,
     KnowledgeSourceReference,
 )
-from azure.search.documents.knowledgebases.models import KnowledgeRetrievalLowReasoningEffort
+from azure.search.documents.knowledgebases.models import (
+    KnowledgeRetrievalAutoReasoningEffort,
+    KnowledgeRetrievalOutputMode,
+)
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
 aoai_params = AzureOpenAIVectorizerParameters(
-    resource_url = "aoai_endpoint",
-    api_key="aoai_api_key",
-    deployment_name = "aoai_gpt_deployment",
-    model_name = "aoai_gpt_model",
+    resource_url = "<aoai-endpoint>",
+    deployment_name = "<aoai-gpt-deployment>",
+    model_name = "<aoai-gpt-model>",
 )
 
 knowledge_base = KnowledgeBase(
     name = "my-kb",
     description = "This knowledge base handles questions directed at two unrelated sample indexes.",
     retrieval_instructions = "Use the hotels knowledge source for queries about where to stay, otherwise use the earth at night knowledge source.",
-    answer_instructions = "Provide a two-sentence, concise, and informative answer based on the retrieved documents.",
-    output_mode = "answerSynthesis",
+    answer_instructions = "Answer in two concise sentences.",
+    output_mode = KnowledgeRetrievalOutputMode.ANSWER_SYNTHESIS,
     knowledge_sources = [
         KnowledgeSourceReference(name = "hotels-ks"),
         KnowledgeSourceReference(name = "earth-at-night-ks"),
     ],
     models = [KnowledgeBaseAzureOpenAIModel(azure_open_ai_parameters = aoai_params)],
     encryption_key = None,
-    retrieval_reasoning_effort = KnowledgeRetrievalLowReasoningEffort(),
+    retrieval_reasoning_effort = KnowledgeRetrievalAutoReasoningEffort(),
 )
 
 index_client.create_or_update_knowledge_base(knowledge_base)
@@ -496,11 +506,11 @@ print(f"Knowledge base '{knowledge_base.name}' created or updated successfully."
 
 ```python
 # Create a knowledge base
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import KnowledgeBase, KnowledgeSourceReference
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
 
 knowledge_base = KnowledgeBase(
     name = "my-kb",
@@ -524,19 +534,19 @@ print(f"Knowledge base '{knowledge_base.name}' created or updated successfully."
 
 ::: zone pivot="rest"
 
-# [2026-05-01-preview](#tab/2026-05-01-preview)
+# [2026-08-01-preview](#tab/2026-08-01-preview)
 
 ```http
 # Create a knowledge base
-PUT {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version=2026-05-01-preview
+PUT {{search-endpoint}}/knowledgebases/my-kb?api-version=2026-08-01-preview
 Content-Type: application/json
-api-key: {{search-api-key}}
+Authorization: Bearer {{search-access-token}}
 
 {
     "name" : "my-kb",
     "description": "This knowledge base handles questions directed at two unrelated sample indexes.",
     "retrievalInstructions": "Use the hotels knowledge source for queries about where to stay, otherwise use the earth at night knowledge source.",
-    "answerInstructions": null,
+    "answerInstructions": "Answer in two concise sentences.",
     "outputMode": "answerSynthesis",
     "knowledgeSources": [
         {
@@ -546,33 +556,32 @@ api-key: {{search-api-key}}
             "name": "earth-at-night-ks"
         }
     ],
-    "models" : [ 
+    "models" : [
         {
             "kind": "azureOpenAI",
             "azureOpenAIParameters": {
-                "resourceUri": "{{model-provider-url}}",
-                "apiKey": "{{model-api-key}}",
+                "resourceUri": "{{aoai-endpoint}}",
                 "deploymentId": "gpt-5.4-mini",
                 "modelName": "gpt-5.4-mini"
             }
         }
     ],
     "encryptionKey": null,
     "retrievalReasoningEffort": {
-        "kind": "low"
+        "kind": "auto"
     }
 }
 ```
 
-**Reference:** [Knowledge Bases - Create or Update](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Bases - Create or Update](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 # [2026-04-01](#tab/2026-04-01)
 
 ```http
 # Create a knowledge base
-PUT {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version=2026-04-01
+PUT {{search-endpoint}}/knowledgebases/my-kb?api-version=2026-04-01
 Content-Type: application/json
-api-key: {{search-api-key}}
+Authorization: Bearer {{search-access-token}}
 
 {
     "name" : "my-kb",
@@ -595,12 +604,138 @@ api-key: {{search-api-key}}
 
 ::: zone-end
 
+### Configure default retrieve limits (preview)
+
+Starting with the `2026-08-01-preview` API version, you can use the optional `retrieveDefaults` object to store request-wide defaults on a knowledge base. Each stored property applies only when a retrieve request omits the corresponding request field:
+
+| Stored property | Retrieve request field |
+| --- | --- |
+| `maxRuntimeInSeconds` | `maxRuntimeInSeconds` |
+| `maxOutputDocuments` | `maxOutputDocuments` |
+| `maxOutputSizeInTokens` | `maxOutputSize` |
+
+The output token budget uses different property names when stored and overridden. Set `maxOutputSizeInTokens` in `retrieveDefaults`, and use `maxOutputSize` in a retrieve request.
+
+The effective value for each property is determined independently in this order:
+
+1. The corresponding value on the retrieve request.
+1. The value in the knowledge base `retrieveDefaults` object.
+1. The service default when the property is absent at both levels.
+
+The following example uses an existing search index knowledge source named `your-knowledge-source`. It stores a 45-second runtime budget, a maximum of eight output documents, and a 12,000-token output budget.
+
+::: zone pivot="csharp"
+
+```csharp
+using System;
+using Azure.Identity;
+using Azure.Search.Documents;
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+using Azure.Search.Documents.Models;
+
+string searchEndpoint = "<search-endpoint>";
+
+var options = new SearchClientOptions(
+    SearchClientOptions.ServiceVersion.V2026_08_01_Preview);
+var indexClient = new SearchIndexClient(
+    new Uri(searchEndpoint),
+    new DefaultAzureCredential(),
+    options);
+
+var knowledgeBase = new KnowledgeBase(
+    "your-knowledge-base",
+    new[] { new KnowledgeSourceReference("your-knowledge-source") })
+{
+    Description = "A knowledge base for product support content.",
+    RetrieveDefaults = new KnowledgeBaseRetrieveDefaults
+    {
+        MaxRuntimeInSeconds = 45,
+        MaxOutputDocuments = 8,
+        MaxOutputSizeInTokens = 12000
+    }
+};
+
+await indexClient.CreateOrUpdateKnowledgeBaseAsync(knowledgeBase);
+```
+
+**Reference:** [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient?view=azure-dotnet-preview&preserve-view=true), [SearchClientOptions.ServiceVersion](/dotnet/api/azure.search.documents.searchclientoptions.serviceversion?view=azure-dotnet-preview&preserve-view=true), [KnowledgeBase](/dotnet/api/azure.search.documents.indexes.models.knowledgebase?view=azure-dotnet-preview&preserve-view=true)
+
+::: zone-end
+
+::: zone pivot="python"
+
+```python
+from azure.identity import DefaultAzureCredential
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.indexes.models import (
+    KnowledgeBase,
+    KnowledgeBaseRetrieveDefaults,
+    KnowledgeSourceReference,
+)
+
+search_endpoint = "<search-endpoint>"
+index_client = SearchIndexClient(
+    endpoint=search_endpoint,
+    credential=DefaultAzureCredential(),
+    api_version="2026-08-01-preview",
+)
+
+knowledge_base = KnowledgeBase(
+    name="your-knowledge-base",
+    description="A knowledge base for product support content.",
+    knowledge_sources=[
+        KnowledgeSourceReference(name="your-knowledge-source"),
+    ],
+    retrieve_defaults=KnowledgeBaseRetrieveDefaults(
+        max_runtime_in_seconds=45,
+        max_output_documents=8,
+        max_output_size_in_tokens=12000,
+    ),
+)
+
+index_client.create_or_update_knowledge_base(knowledge_base)
+```
+
+**Reference:** [SearchIndexClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient), [KnowledgeBase](/python/api/azure-search-documents/azure.search.documents.indexes.models.knowledgebase)
+
+::: zone-end
+
+::: zone pivot="rest"
+
+```http
+PUT {{search-endpoint}}/knowledgebases/your-knowledge-base?api-version=2026-08-01-preview
+Content-Type: application/json
+Authorization: Bearer {{search-access-token}}
+
+{
+  "name": "your-knowledge-base",
+  "description": "A knowledge base for product support content.",
+  "knowledgeSources": [
+    {
+      "name": "your-knowledge-source"
+    }
+  ],
+  "retrieveDefaults": {
+    "maxRuntimeInSeconds": 45,
+    "maxOutputDocuments": 8,
+    "maxOutputSizeInTokens": 12000
+  }
+}
+```
+
+**Reference:** [Knowledge Bases - Create or Update](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
+
+::: zone-end
+
+To override these stored values with 20 seconds, one document, and 5,000 tokens for one request, see [Verify knowledge base retrieve defaults](agentic-retrieval-how-to-retrieve.md#verify-knowledge-base-retrieve-defaults).
+
 ### Configure CORS for browser-based retrieve calls (preview)
 
 > [!IMPORTANT]
-> You can use the 2026-05-01-preview to enable cross-origin resource sharing (CORS), which allows browser-based applications to request data directly from the service. Depending on your CORS configuration, external web pages might be able to access or invoke the service and its data using the user's browser context, as well as create other security threats. Enabling CORS is at your own risk.
+> Cross-origin resource sharing (CORS) allows browser-based applications to request data directly from the service. Depending on your CORS configuration, external web pages might access or invoke the service and its data by using the user's browser context. This access can create security threats. Enabling CORS is at your own risk.
 
-In the 2026-05-01-preview API version, a knowledge base can define `corsOptions` for browser-based applications that call the retrieve action directly from JavaScript. The CORS policy identifies which browser origins can send retrieve requests to the knowledge base.
+Starting with the `2026-05-01-preview` API version, a knowledge base can define `corsOptions` for browser-based applications that call the retrieve action directly from JavaScript. The CORS policy identifies which browser origins can send retrieve requests to the knowledge base.
 
 When you omit `corsOptions`, the knowledge base has no CORS policy, and browsers block cross-origin retrieve requests.
 
@@ -609,11 +744,11 @@ The following example creates a knowledge base that allows retrieve requests fro
 ::: zone pivot="csharp"
 
 ```csharp
-using Azure;
+using Azure.Identity;
 using Azure.Search.Documents.Indexes;
 using Azure.Search.Documents.Indexes.Models;
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new DefaultAzureCredential());
 
 var knowledgeBase = new KnowledgeBase(
     name: "browser-chat-kb",
@@ -637,15 +772,15 @@ await indexClient.CreateOrUpdateKnowledgeBaseAsync(knowledgeBase);
 ::: zone pivot="python"
 
 ```python
-from azure.core.credentials import AzureKeyCredential
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 from azure.search.documents.indexes.models import (
     CorsOptions,
     KnowledgeBase,
     KnowledgeSourceReference,
 )
 
-index_client = SearchIndexClient(endpoint="search_url", credential=AzureKeyCredential("api_key"))
+index_client = SearchIndexClient(endpoint="<search-endpoint>", credential=DefaultAzureCredential())
 
 knowledge_base = KnowledgeBase(
     name="browser-chat-kb",
@@ -667,9 +802,9 @@ index_client.create_or_update_knowledge_base(knowledge_base)
 ::: zone pivot="rest"
 
 ```http
-PUT {{search-url}}/knowledgebases/browser-chat-kb?api-version=2026-05-01-preview
+PUT {{search-endpoint}}/knowledgebases/browser-chat-kb?api-version=2026-08-01-preview
 Content-Type: application/json
-api-key: {{search-api-key}}
+Authorization: Bearer {{search-access-token}}
 
 {
   "name": "browser-chat-kb",
@@ -717,11 +852,11 @@ System.Console.WriteLine($"Knowledge base '{knowledgeBaseName}' deleted successf
 
 ```python
 # Delete a knowledge base
-from azure.core.credentials import AzureKeyCredential 
+from azure.identity import DefaultAzureCredential
 from azure.search.documents.indexes import SearchIndexClient
 
-index_client = SearchIndexClient(endpoint = "search_url", credential = AzureKeyCredential("api_key"))
-index_client.delete_knowledge_base("knowledge_base_name")
+index_client = SearchIndexClient(endpoint = "<search-endpoint>", credential = DefaultAzureCredential())
+index_client.delete_knowledge_base("<knowledge-base-name>")
 print(f"Knowledge base deleted successfully.")
 ```
 
@@ -733,8 +868,8 @@ print(f"Knowledge base deleted successfully.")
 
 ```http
 # Delete a knowledge base
-DELETE {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version={{api-version}}
-api-key: {{search-api-key}}
+DELETE {{search-endpoint}}/knowledgebases/{{knowledge-base-name}}?api-version={{api-version}}
+Authorization: Bearer {{search-access-token}}
 ```
 
 **Reference:** [Knowledge Bases - Delete](/rest/api/searchservice/knowledge-bases/delete?view=rest-searchservice-2026-04-01&preserve-view=true)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ベースの作成に関するドキュメントの改善"
}
```

### Explanation
この変更は、Azure AI Searchの知識ベース作成に関するドキュメントの大幅な更新を示しており、主にAPIバージョンの更新、内容の追加、および詳細の明確化に焦点を当てています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：ドキュメント内で使用されているAPIバージョンが、2026-05-01-previewから2026-08-01-previewに更新され、新機能に関する情報が強調されています。これにより、新しい機能や改善点が反映されています。

2. **重要な情報の追加**：Azure AI Searchの知識ベースがどのように機能するかの説明を詳述した部分が含まれ、特にユーザーに対する影響や注意点が明確に記載されています。

3. **新機能の詳細**：新しい `retrieveDefaults` 機能が追加されており、ユーザーがリクエスト全体のデフォルト値を設定できるようになっています。この機能は、特定のリクエストフィールドを省略した場合に自動的に適用される値を指定することができます。

4. **コードスニペットの改善**：C#およびPythonのコードスニペットが更新され、最新の認証方法である `DefaultAzureCredential` が使用されています。これにより、ユーザーがより安全にリソースにアクセスできるようになっています。

5. **CORS設定に関する更新**：CORS（クロスオリジンリソースシェアリング）に関する設定方法が説明されており、ブラウザベースのアプリケーションが知識ベースからデータを直接取得できるようになるための新しいオプションについても説明されています。

6. **不必要な情報の削除・整理**：古いAPIバージョンに関する複雑な情報や冗長な部分が削除され、ドキュメントの明瞭さと使いやすさが向上しています。

これらの更新により、Azure AI Searchを利用する開発者が知識ベースを作成する際の理解と実装がより容易になり、ユーザー体験が向上することを目的としています。

## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -16,9 +16,9 @@ ai-usage: ai-assisted
 [!INCLUDE [Preview API usage](./includes/previews/agentic-retrieval-preview-api-usage.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -58,7 +58,7 @@ In this tutorial, you:
 
     GPT-4 family models are deprecated. For retirement dates and current status in Microsoft Foundry, see [Model retirement schedule - Microsoft Foundry](/azure/foundry/openai/concepts/model-retirement-schedule).
 
-+ Permissions to access and manage Azure AI Search and Microsoft Foundry resources. For more information, see [Configure access](#configure-access).
++ Permission to access and manage Azure AI Search and Microsoft Foundry resources. For more information, see [Configure access](#configure-access).
 
 + [Python 3.8](https://www.python.org/downloads/) or later.
 
@@ -92,15 +92,15 @@ To configure access for this solution:
 1. On your search service, [enable role-based access](search-security-enable-roles.md) and [assign the following roles](search-security-rbac.md).
 
     | Role | Assignee | Purpose |
-    |------|----------|---------|
+    | ------ | ---------- | --------- |
     | Search Service Contributor | Your user account | Create objects |
     | Search Index Data Contributor | Your user account | Load data |
     | Search Index Data Reader | Your user account and project managed identity | Read indexed content |
 
 1. On your project's parent resource, assign the following roles.
 
     | Role | Assignee | Purpose |
-    |------|----------|---------|
+    | ------ | ---------- | --------- |
     | Foundry User | Your user account | Access model deployments and create agents |
     | Foundry Project Manager | Your user account | Create project connection and use MCP tool in agents |
     | Cognitive Services User | Search service managed identity | Access knowledge base |
@@ -351,7 +351,7 @@ index_client = SearchIndexClient(endpoint=endpoint, credential=credential)
 index_client.create_or_update_knowledge_base(knowledge_base=knowledge_base)
 print(f"Knowledge base '{base_name}' created or updated successfully")
 
-mcp_endpoint = f"{endpoint.rstrip('/')}/knowledgebases/{base_name}/mcp?api-version=2026-05-01-preview"
+mcp_endpoint = f"{endpoint.rstrip('/')}/knowledgebases/{base_name}/mcp?api-version=2026-08-01-preview"
 ```
 
 ### Set up a project client
@@ -530,7 +530,7 @@ response = openai_client.responses.create(
 print(f"Response: {response.output_text}")
 ```
 
-The response should be similar to the following:
+The response should be similar to the following example.
 
 ```
 Response: Here are evidence-based explanations to your questions:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "パイプライン作成に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchのパイプライン作成に関するドキュメントの見直しを示しており、主にAPIバージョンの更新と表現の改良に焦点が当てられています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：ドキュメント内で使用されるREST APIのバージョンが、2026-05-01-previewから2026-08-01-previewに更新されています。この変更は、最新の機能や改良を取り入れるための重要なステップです。

2. **重要な情報の更新**：APIの更新に伴い、接続可能な他のMicrosoftサービスやサードパーティサービスについての情報が最新のものに変更されました。

3. **権限の表現の改善**：ドキュメント内で権限に関する文言が修正され、読みやすさが向上しました。特に「+ Permissions to access」と「++ Permission to access」とすることで、内容がより一貫した表現になりました。

4. **例示文の明確化**：サンプル応答に関する文が明確化され、読者が期待される出力に関してより理解しやすくなっています。

これらの変更により、Azure AI Searchのパイプライン作成に関するドキュメントがより正確で実用的な情報を提供するように改善されており、ユーザーが効果的に利用できるようになっています。

## articles/search/agentic-retrieval-how-to-enable-disable.md{#item-44591a}

<details>
<summary>Diff</summary>
````diff
@@ -14,23 +14,23 @@ ai-usage: ai-assisted
 
 Agentic retrieval is a premium feature billed by usage. By default, all search services are enrolled in the free plan, which provides a monthly allowance at no charge. To enable continued access after the free quota is consumed, you can switch to the standard plan.
 
-Starting with Search Service REST API version 2026-04-01, billing consent for semantic ranker and agentic retrieval is separate. Use `knowledgeRetrieval` to control paid agentic retrieval usage independently of `semanticSearch`.
+Starting with Search Service REST API version `2026-04-01`, billing consent for semantic ranker and agentic retrieval is separate. Use `knowledgeRetrieval` to control paid agentic retrieval usage independently of `semanticSearch`.
 
 ## Prerequisites
 
 - An Azure AI Search service in any [region that provides agentic retrieval](search-region-support.md).
 
-- **Owner** or **Contributor** permissions on the search service.
+- **Owner** or **Contributor** access to the search service.
 
 - Search Management REST API version [2026-03-01-preview](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) or later to set the `knowledgeRetrieval` property.
 
 ## Billing split
 
 [!INCLUDE [billing-split-version-compatibility](includes/billing-split-version-compatibility.md)]
 
-For Search Service REST API version 2026-04-01 and later, `knowledgeRetrieval` controls agentic retrieval billing independently of `semanticSearch`. To control semantic ranker billing, see [Enable or disable semantic ranker billing](semantic-how-to-enable-disable.md).
+For Search Service REST API version `2026-04-01` and later, `knowledgeRetrieval` controls agentic retrieval billing independently of `semanticSearch`. To control semantic ranker billing, see [Enable or disable semantic ranker billing](semantic-how-to-enable-disable.md).
 
-For Search Service REST API version 2025-11-01-preview and earlier, `semanticSearch` controls consent for both semantic ranker and paid agentic retrieval usage. The `knowledgeRetrieval` property is ignored.
+For Search Service REST API version `2025-11-01-preview` and earlier, `semanticSearch` controls consent for both semantic ranker and paid agentic retrieval usage. The `knowledgeRetrieval` property is ignored.
 
 ## Billing plans
 
@@ -45,7 +45,7 @@ Agentic retrieval has two billing plans. For pricing by currency, see [Azure AI
 
 Follow these steps to switch agentic retrieval to the standard billing plan.
 
-### [Azure portal](#tab/portal)
+# [Azure portal](#tab/portal)
 
 1. Go to your search service in the [Azure portal](https://portal.azure.com).
 
@@ -57,14 +57,14 @@ Follow these steps to switch agentic retrieval to the standard billing plan.
 
     :::image type="content" source="media/agentic-retrieval-how-to-enable-disable/agentic-enable.png" alt-text="Screenshot of the Premium features page in the Azure portal, showing the Knowledge retrieval Standard plan selected." lightbox="media/agentic-retrieval-how-to-enable-disable/agentic-enable.png" border="true":::
 
-### [REST](#tab/rest)
+# [REST](#tab/rest)
 
 Use [Services - Create Or Update](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true#knowledgeretrieval) (Search Management REST API) to set `knowledgeRetrieval` to `standard`:
 
 ```http
-PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2026-03-01-preview
+PATCH https://management.azure.com/subscriptions/{{subscription-id}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2026-03-01-preview
 Content-Type: application/json
-Authorization: Bearer {{token}}
+Authorization: Bearer {{management-access-token}}
 
 {
   "properties": {
@@ -76,15 +76,15 @@ Authorization: Bearer {{token}}
 Management REST API calls are authenticated through Microsoft Entra ID. For instructions, see [Manage your Azure AI Search service with REST APIs](search-manage-rest.md).
 
 > [!IMPORTANT]
-> If you previously relied on `semanticSearch` to enable paid agentic retrieval usage, you must explicitly set `knowledgeRetrieval` to `standard` before you migrate agentic retrieval workloads to Search Service REST API version 2026-04-01 or later. Existing `semanticSearch=standard` consent doesn't carry over to `knowledgeRetrieval`.
+> If you previously relied on `semanticSearch` to enable paid agentic retrieval usage, you must explicitly set `knowledgeRetrieval` to `standard` before you migrate agentic retrieval workloads to Search Service REST API version `2026-04-01` or later. Existing `semanticSearch=standard` consent doesn't carry over to `knowledgeRetrieval`.
 
 ---
 
 ## Disable agentic retrieval billing
 
 Follow these steps to switch agentic retrieval back to the free billing plan.
 
-### [Azure portal](#tab/portal)
+# [Azure portal](#tab/portal)
 
 1. Go to your search service in the [Azure portal](https://portal.azure.com).
 
@@ -94,14 +94,14 @@ Follow these steps to switch agentic retrieval back to the free billing plan.
 
     :::image type="content" source="media/agentic-retrieval-how-to-enable-disable/agentic-disable.png" alt-text="Screenshot of the Premium features page in the Azure portal, showing the Knowledge retrieval Free plan selected." lightbox="media/agentic-retrieval-how-to-enable-disable/agentic-disable.png" border="true":::
 
-### [REST](#tab/rest)
+# [REST](#tab/rest)
 
 Use [Services - Create or Update](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true#knowledgeretrieval) (Search Management REST API) to set `knowledgeRetrieval` to `free`:
 
 ```http
-PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2026-03-01-preview
+PATCH https://management.azure.com/subscriptions/{{subscription-id}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2026-03-01-preview
 Content-Type: application/json
-Authorization: Bearer {{token}}
+Authorization: Bearer {{management-access-token}}
 
 {
   "properties": {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索機能の有効化および無効化に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエージェント検索機能の有効化および無効化に関するドキュメントの見直しを示しており、主に用語や表現の修正、新しいAPIバージョンの周知に然る重要な内容が含まれています。

主な変更点は以下の通りです：

1. **APIバージョンの明記**：REST APIのバージョンが明示的にバッククオートで囲まれるようになり、より明確な表現がされたことで、読者が関連する情報を認識しやすくなっています。

2. **権限に関する表現の改善**：従来の「**Owner** or **Contributor** permissions」から「**Owner** or **Contributor** access to the search service」への変更により、表現が一貫してわかりやすくなっています。

3. **トークン名の明確化**：HTTP PATCHリクエストで使用されるトークン名が「{{token}}」から「{{management-access-token}}」に変更され、より具体的であるため、読者が何を指しているのかが理解しやすくなりました。

4. **重要な箇所の強調**：エージェント検索機能を有効にするためには、以前の使用方法に依存していた場合に明示的に`knowledgeRetrieval`を`standard`に設定する必要があることが強調されています。

5. **文書の整理**：セクション見出しやリストの書式が整えられ、読みやすさが向上しています。

全体を通して、これらの変更により、エージェント検索機能の利用における重要なガイダンスが改善されており、ユーザーが検索サービスをスムーズに管理できるようになることを目的としています。

## articles/search/agentic-retrieval-how-to-image-serving.md{#item-48db70}

<details>
<summary>Diff</summary>
````diff
@@ -13,11 +13,11 @@ ai-usage: ai-assisted
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -33,6 +33,12 @@ When you enable image serving, Azure AI Search:
 
 This article shows you how to enable image serving on a knowledge base, override it per request, inspect image serving statistics, and plan for the storage account lifecycle requirements.
 
+### Usage support
+
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-08-01-preview&preserve-view=true) |
+| -- | -- | -- | -- | -- | -- | -- |
+| ❌ | ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + An Azure AI Search service with a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) that specifies an LLM. The knowledge base must use [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md).
@@ -51,15 +57,15 @@ This article shows you how to enable image serving on a knowledge base, override
 
 + A Microsoft Foundry resource in a [region supported by Azure Content Understanding in Foundry Tools](/azure/ai-services/content-understanding/language-region-support), with Azure OpenAI embedding and multimodal chat model deployments. Use the resource endpoint in the `https://<resource-name>.services.ai.azure.com` format.
 
-+ Permissions to create or update the knowledge base and managed knowledge source. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to the user or automation identity that performs these management operations (recommended). Alternatively, use an [API key](search-security-api-keys.md).
++ Permission to create or update the knowledge base and managed knowledge source. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Contributor** roles assigned to the user or automation identity that performs these management operations (recommended). Alternatively, use an [admin API key](search-security-api-keys.md).
 
-+ Permissions to call the retrieve action. Assign the **Search Index Data Reader** role to the identity that sends retrieve requests (recommended) or use an API key.
++ Permission to call the retrieve action. Assign the **Search Index Data Reader** role to the identity that sends retrieve requests (recommended) or use a [query API key](search-security-api-keys.md).
 
 + For outbound calls to the LLM during answer synthesis, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource that hosts the LLM.
 
 + For asset store access, configure the search service managed identity as described in [Configure asset store and application access](#configure-asset-store-and-application-access).
 
-+ The [2026-05-01-preview](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) REST API or an equivalent Azure SDK preview package: [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md)
++ The [2026-08-01-preview](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) REST API or an equivalent Azure SDK preview package: [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md)
 
 ## Limitations and considerations
 
@@ -134,9 +140,9 @@ For source-specific instructions, see:
 A minimal blob knowledge source with image serving enabled looks like this:
 
 ```http
-PUT https://{service-name}.search.windows.net/knowledgesources/my-blob-ks?api-version=2026-05-01-preview
+PUT https://{service-name}.search.windows.net/knowledgesources/my-blob-ks?api-version=2026-08-01-preview
 Content-Type: application/json
-Authorization: Bearer {{token}}
+Authorization: Bearer {{search-access-token}}
 
 {
   "name": "my-blob-ks",
@@ -210,9 +216,9 @@ The knowledge base definition also specifies the LLM used for **answer synthesis
 If your knowledge base references multiple knowledge sources, set `enableImageServing` only on supported file-based indexed kinds that have `assetStore` configured. Unsupported kinds (such as search index, remote SharePoint, or web) still contribute text grounding but don't supply document-embedded images to downstream answer synthesis.
 
 ```http
-PUT https://{service-name}.search.windows.net/knowledgebases/my-kb?api-version=2026-05-01-preview
+PUT https://{service-name}.search.windows.net/knowledgebases/my-kb?api-version=2026-08-01-preview
 Content-Type: application/json
-Authorization: Bearer {{token}}
+Authorization: Bearer {{search-access-token}}
 
 {
   "name": "my-kb",
@@ -245,9 +251,9 @@ Send a `GET` request to the knowledge base endpoint and verify that the knowledg
 Call the [retrieve action](agentic-retrieval-how-to-retrieve.md) against the knowledge base. To override the knowledge base default on a per-request basis, set `enableImageServing` in the matching entry under `knowledgeSourceParams`.
 
 ```http
-POST https://{service-name}.search.windows.net/knowledgebases/my-kb/retrieve?api-version=2026-05-01-preview
+POST https://{service-name}.search.windows.net/knowledgebases/my-kb/retrieve?api-version=2026-08-01-preview
 Content-Type: application/json
-Authorization: Bearer {{token}}
+Authorization: Bearer {{search-access-token}}
 
 {
   "retrievalReasoningEffort": { "kind": "medium" },
@@ -276,7 +282,7 @@ Authorization: Bearer {{token}}
 
 ### What happens at retrieval time
 
-For image references associated with matching content, the search service downloads the corresponding images from the asset store, base64-encodes them, and passes them as multimodal content to the downstream answer-synthesis model. Inspect aggregate image-serving statistics in `activity.imageServing`. For the exact response shape, see the reference documentation for [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (REST API).
+For image references associated with matching content, the search service downloads the corresponding images from the asset store, base64-encodes them, and passes them as multimodal content to the downstream answer-synthesis model. Inspect aggregate image-serving statistics in `activity.imageServing`. For the exact response shape, see the reference documentation for [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-08-01-preview&preserve-view=true) (REST API).
 
 ### Verify retrieve behavior
 
@@ -297,7 +303,7 @@ When both the knowledge base definition and the retrieve request specify `enable
 The following table summarizes the nine combinations.
 
 | Knowledge base definition (`enableImageServing`) | Retrieve request (`enableImageServing`) | Image serving enabled? |
-|---|---|---|
+| --- | --- | --- |
 | `true` | `true` | Yes |
 | `true` | `false` | No |
 | `true` | Not set | Yes |
@@ -375,7 +381,7 @@ Delete the knowledge base before you delete its knowledge source. Deleting these
 Use the `imageServing` activity block from [Inspect image serving statistics](#inspect-image-serving-statistics) as your first diagnostic. The following table lists checks for common symptoms without assuming a single cause.
 
 | Symptom | Checks |
-|---|---|
+| --- | --- |
 | `imagesRetrieved` is `0` for image-rich documents | Check indexer status and warnings, populated `image_path` values in matching indexed chunks, and image blobs in the asset container. Confirm that the source documents contain extractable images and that the search service identity has **Storage Blob Data Contributor** at the storage-account scope. |
 | Retrieve response has no `imageServing` block | Confirm that the request sets `includeActivity` to `true`. Check the effective `enableImageServing` value after applying request, knowledge base, and default precedence. Confirm that `outputMode` is `answerSynthesis`, and inspect source activity errors and warnings. |
 | `verbalizationUsed` differs from what you expect | Check `disableImageVerbalization`, `chatCompletionModel`, and the most recent indexer status. Inspect `verbalizationUsed` independently from `imagesSentToModel`. A response can report verbalization and images sent together. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像サービングに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける画像サービングの機能に関するドキュメントの修正を示しており、主にAPIバージョンの更新およびドキュメント内容の明確化が行われました。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：ドキュメント内で言及されているREST APIのバージョンが、2026-05-01-previewから2026-08-01-previewに更新されました。これにより、新しい機能や改善点が反映されています。

2. **重要な情報の強調**：特定の機能や操作に関する注意書きが強化され、ユーザーが理解すべき重要な要素がわかりやすくなっています。例えば、接続性やアクセス権限における制限に関する情報が明確に記載されています。

3. **使用サポートチャートの追加**：異なるプラットフォーム（Azureポータル、Microsoft Foundry、各種SDK、およびREST API）に対するサポート情報を示すテーブルが追加され、各プラットフォームでの機能の対応状況が視覚的に理解しやすくなっています。

4. **権限に関する表現の修正**：ドキュメント中で使用されている権限に関する文章が、より明確で一貫性のあるものに修正されています。特に、APIキーに関連する表現が具体的になっています。

5. **HTTPリクエストの例の更新**：API呼び出しに関するサンプルコードで、トークンの命名が変更され、より具体的な名称が使われることで、読者がどのトークンを使用すべきかが明確になりました。

これらの変更により、ユーザーが画像サービング機能をより理解しやすくなり、適切に利用できるように改善されています。全体として、ドキュメントの整合性と可読性が向上しています。

## articles/search/agentic-retrieval-how-to-migrate.md{#item-9653ea}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +1,12 @@
 ---
 title: Migrate Agentic Retrieval Code
-description: Learn how to migrate your agentic retrieval code to the latest REST API version. This article focuses on breaking changes and backwards compatibility.
+description: Learn how to migrate your agentic retrieval code to the latest API version. This article focuses on breaking changes and backward compatibility.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/02/2026
+ms.date: 08/20/2026
+ms.custom:
+  - dev-focus
+  - doc-kit-assisted
 ai-usage: ai-assisted
 ---
 
@@ -12,42 +15,193 @@ ai-usage: ai-assisted
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-If you wrote [agentic retrieval](agentic-retrieval-overview.md) code using an earlier REST API version, this article explains when and how to migrate to a newer version. It also describes breaking and nonbreaking changes for all API versions that support agentic retrieval.
+If your [agentic retrieval](agentic-retrieval-overview.md) code targets an earlier API version, this article explains when and how to migrate to a newer version. It also describes breaking and nonbreaking changes for all API versions that support agentic retrieval.
 
 Migration instructions are intended to help you run an existing solution on a newer API version. The instructions in this article help you address breaking changes at the API level so that your app runs as before. For help with adding new functionality, start with [What's new in Azure AI Search](whats-new.md).
 
 > [!TIP]
-> Using Azure SDKs instead of REST? Read this article to learn about breaking changes, and then install the latest package to begin your updates. Before you start, check the SDK changelogs to confirm API updates: [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md), [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md), [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md).
+> Using an Azure SDK instead of REST? Before you upgrade the package and apply the relevant migration changes, check the [changelog for your SDK language](search-api-versions.md) to confirm support for your target API version.
 
 ## When to migrate
 
-Every version that supports agentic retrieval has introduced breaking changes. You can continue to run older code unchanged by retaining the API version value, but to benefit from bug fixes, improvements, and newer functionality, you must update your code.
+Most versions that support agentic retrieval introduced breaking changes. You can continue to run older code unchanged by retaining the API version value, but to benefit from bug fixes, improvements, and newer functionality, you must update your code.
 
-If your code targets a preview version, we recommend migrating to the latest stable version only if your use case is fully supported by 2026-04-01. If you rely on answer synthesis, non-minimal reasoning effort, or multi-turn messages, review [breaking and nonbreaking changes](#version-specific-changes) before you decide to migrate. Those capabilities remain in preview.
+If your code targets a preview version, we recommend migrating to the latest stable version only if your use case is fully supported by `2026-04-01`. If you rely on answer synthesis, non-minimal reasoning effort, or multi-turn messages, review [breaking and nonbreaking changes](#version-specific-changes) before you decide to migrate. Those capabilities remain in preview.
 
-## How to migrate
-
-+ The supported migration path is incremental. If your code targets 2025-05-01-preview, first migrate to 2025-08-01-preview, and then to 2025-11-01-preview, and so on.
+## Before you migrate
 
 + To understand the scope of changes, review [breaking and nonbreaking changes](#version-specific-changes) for each version.
 
-+ "Migration" means creating new, uniquely named objects that implement the behaviors of the previous version. You can't overwrite an existing object if properties are added or deleted on the API. One advantage of creating new objects is the ability to preserve existing objects while new ones are developed and tested.
++ The supported migration path is incremental. If your code targets `2025-05-01-preview`, first migrate to `2025-08-01-preview`, then continue through each subsequent version until you reach your target version.
+
++ For a side-by-side migration, create uniquely named objects that implement the behaviors of the previous version. This approach preserves existing objects while you develop and test replacements. If an object supports update in place, the version-specific steps call out that option.
 
 + For each object that you migrate, start by getting the current definition from the search service so that you can review existing properties before specifying the new one.
 
 + Delete older versions only after your migration is fully tested and deployed.
 
-### [**2026-04-01**](#tab/2026-04-01)
+## How to migrate
+
+This section covers migration steps for the following API versions:
+
++ [2026-08-01-preview](#2026-08-01-preview)
++ [2026-05-01-preview](#2026-05-01-preview)
++ [2026-04-01](#2026-04-01)
++ [2025-11-01-preview](#2025-11-01-preview)
++ [2025-08-01-preview](#2025-08-01-preview)
+
+### 2026-08-01-preview
+
+If you're migrating from [2026-05-01-preview](#2026-05-01-preview-1), you can move directly to `2026-08-01-preview`. This migration requires updates to Work IQ knowledge sources, list paging, response processing, MCP server tools, and affected generated-client calls.
+
+1. [Migrate Work IQ knowledge sources](#migrate-work-iq-knowledge-sources)
+1. [Update list paging](#update-list-paging)
+1. [Update retrieve response processing](#update-retrieve-response-processing)
+1. [Update code and clients](#update-code-and-clients-for-2026-08-01-preview)
+
+#### Migrate Work IQ knowledge sources
+
+To migrate a Work IQ knowledge source to the new authentication configuration:
+
+1. Export its current definition.
+
+1. Update the existing knowledge source by using [Knowledge Sources - Create Or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true), or create a replacement with a unique name for a side-by-side migration.
+
+1. Use the `2026-08-01-preview` API version and configure `workIQParameters.entraAppAuthentication`. The `applicationId` and `federatedCredentialId` properties are required. The `tenantId` property is optional and defaults to the search service's tenant.
+
+1. If you created a replacement, update each knowledge base that references the previous knowledge source to use the replacement name.
+
+1. Update retrieve requests to pass the user assertion in the `x-ms-query-work-iq-source-authorization` header.
+
+For setup and examples, see [Create a Work IQ knowledge source (preview)](agentic-knowledge-source-how-to-work-iq.md).
+
+#### Update list paging
+
+To replace offset-based paging with cursor-based paging:
+
+1. Remove `$top`, `$skip`, and `$count` from knowledge source list requests. Set `pageSize` from 1 through 3,000 to control the page size. If you omit it, the service chooses the page size.
+
+1. To filter by name, set `search` and `searchType`. The only supported `searchType` value is `prefix`, which is also the default. The following request returns up to 100 knowledge sources whose names start with `contoso`.
+
+   ```http
+   GET {{search-endpoint}}/knowledgesources?api-version=2026-08-01-preview&pageSize=100&search=contoso&searchType=prefix
+   Authorization: Bearer {{search-access-token}}
+   ```
+
+   **Reference:** [Knowledge Sources - List](/rest/api/searchservice/knowledge-sources/list?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
+
+1. If the response contains `@odata.nextLink`, send that URL exactly as returned. Don't parse or modify its continuation state.
+
+#### Update retrieve response processing
+
+To process the new Work IQ reference and model-backed activity shapes:
+
+1. Remove dependencies on `attributions`, `WorkIQAttribution`, and `seeMoreWebUrl`. Read sensitivity-label metadata from `searchSensitivityLabelInfo` on the Work IQ reference.
+
+1. In query-planning, answer-synthesis, and web-summarization activity records, read `modelName` and `deploymentId` from the nested `model` object. The nested object and both properties are optional.
+
+The following fragments show the response-shape changes.
+
+```json
+{
+  "references": [
+    {
+      "type": "workIQ",
+      "id": "<reference-id>",
+      "activitySource": 1,
+      "sourceData": {},
+      "attributions": [
+        {
+          "seeMoreWebUrl": "<attribution-url>"
+        }
+      ]
+    }
+  ],
+  "activity": [
+    {
+      "type": "modelAnswerSynthesis",
+      "id": 2,
+      "modelName": "<model-name>"
+    }
+  ]
+}
+```
+
+In `2026-08-01-preview`, the same fragments use the following shape:
+
+```json
+{
+  "references": [
+    {
+      "type": "workIQ",
+      "id": "<reference-id>",
+      "activitySource": 1,
+      "sourceData": {},
+      "searchSensitivityLabelInfo": {
+        "displayName": "<label-name>",
+        "sensitivityLabelId": "<label-id>"
+      }
+    }
+  ],
+  "activity": [
+    {
+      "type": "modelAnswerSynthesis",
+      "id": 2,
+      "model": {
+        "modelName": "<model-name>",
+        "deploymentId": "<deployment-id>"
+      }
+    }
+  ]
+}
+```
+
+#### Update code and clients for 2026-08-01-preview
+
+To complete your migration:
+
+1. On each MCP server `tools` item, replace `inclusionMode` with `resultsProcessing`. Map `reranked` to `rerank` and `always` to `none`. The `rerank` value is the default. The `none` value bypasses reranking and preserves the tool's underlying result order. For setup, see [Configure tools for an MCP server knowledge source](agentic-knowledge-source-how-to-mcp-server.md#configure-tools).
+
+1. If you use an Azure SDK, install a package that supports `2026-08-01-preview`, and review positional list calls for parameter-order changes. REST callers aren't affected because HTTP parameters are keyed by name. In C#, prefer named arguments, such as `GetKnowledgeSourcesAsync(search: ..., pageSize: ...)`. In Python, pass list options as keyword arguments.
+
+1. Test Work IQ authentication and references, cursor paging, activity-record deserialization, MCP server result ordering, and generated-client calls before you update production.
+
+1. If you created replacement Work IQ knowledge sources, delete the earlier sources only after the migration passes all tests, your updated application is deployed, and no knowledge base references the earlier names.
+
+### 2026-05-01-preview
+
+If you're migrating from [2026-04-01](#2026-04-01-1) or [2025-11-01-preview](#2025-11-01-preview-1), you can move directly to `2026-05-01-preview`. Requests, responses, and persisted objects from those versions remain compatible. The differences are additive features and language SDK renames.
+
+1. Update the API version to `2026-05-01-preview` on REST requests. SDK clients use the package's default API version, so you don't need to pass an explicit `serviceVersion` argument. Instead, upgrade to the `2026-05-01-preview` SDK package.
+
+1. If you use the Python or JavaScript SDK, update the retrieve client to `KnowledgeBaseRetrievalClient` and call `retrieve(...)` instead of the legacy `retrieveKnowledge(...)`. For the full SDK shape mapping, see [Update code and clients for 2026-05-01-preview](#update-code-and-clients-for-2026-05-01-preview).
+
+1. (Optional) Adopt the new `2026-05-01-preview` features, such as [freshness-aware retrieval](agentic-retrieval-how-to-configure-freshness.md), per-source and final-result document caps, persisted retrieve defaults, knowledge base CORS, and Purview sensitivity-label metadata in retrieve responses. None of these features are required to keep an existing solution working.
+
+#### Update code and clients for 2026-05-01-preview
+
+The `2026-05-01-preview` SDKs introduce code-shape changes across the supported languages:
+
+| Language | Migration updates |
+| --- | --- |
+| Python | Create the retrieve client as `KnowledgeBaseRetrievalClient(endpoint=..., credential=..., knowledge_base_name=...)`. Construct reasoning effort instances such as `KnowledgeRetrievalLowReasoningEffort()` and pass the string `output_mode="answerSynthesis"` on the knowledge base or retrieve request. Pass `AzureOpenAIVectorizerParameters(resource_url=...)` (renamed from `resource_uri`), using the resource root endpoint rather than an `/openai/v1` endpoint. |
+| .NET | Create the retrieve client as `new KnowledgeBaseRetrievalClient(endpoint, knowledgeBaseName, credential)` and pass an `AzureKeyCredential` or token credential. To attach a key-based Azure OpenAI model to a knowledge base, set the model API key on `AzureOpenAIVectorizerParameters.ApiKey`. |
+| Java | Use `KnowledgeBaseRetrievalClientBuilder` to create the retrieve client and read results as `KnowledgeBaseRetrievalResult`. `KnowledgeBaseRetrievalOptions` now exposes `setMessages(...)` alongside `setIntents(...)`, plus `setRetrievalReasoningEffort`, `setOutputMode`, `setMaxOutputSize`, and `setMaxOutputDocuments`, so message-based retrieve and answer synthesis work without a semantic-intent workaround. `KnowledgeBase` adds `setOutputMode`, `setRetrievalReasoningEffort`, `setRetrievalInstructions`, `setAnswerInstructions`, and `setCorsOptions`. `SearchIndexKnowledgeSourceParams` adds `setAlwaysQuerySource`, `setFailOnError`, `setMaxOutputDocuments`, and `setEnableImageServing`. |
+| JavaScript and TypeScript | Use `KnowledgeRetrievalClient.retrieve({ intents: [{ type: "semantic", search: query }] })`. The previous `retrieveKnowledge(...)` method is removed in favor of `retrieve(...)`. |
 
-If you're migrating from [2025-11-01-preview](#2025-11-01-preview-1), you can migrate directly to 2026-04-01. Your index and content remain unchanged. You only need to update the knowledge base schema and the retrieve request shape.
+After you update the client shapes, run the full flow that creates the index, uploads documents, creates a knowledge source, creates a knowledge base, issues a retrieve request, and cleans up resources to confirm the migration end to end.
+
+### 2026-04-01
+
+If you're migrating from [2025-11-01-preview](#2025-11-01-preview-1), you can migrate directly to `2026-04-01`. Your index and content remain unchanged. You only need to update the knowledge base schema and the retrieve request shape.
 
 1. [Migrate knowledge sources](#migrate-knowledge-sources)
 1. [Migrate the knowledge base](#migrate-the-knowledge-base)
@@ -57,29 +211,29 @@ If you're migrating from [2025-11-01-preview](#2025-11-01-preview-1), you can mi
 
 #### Migrate knowledge sources
 
-In 2026-04-01, the `searchIndex`, `azureBlob`, `indexedOneLake`, and `web` knowledge source types are generally available. Other knowledge source types remain in preview.
+In `2026-04-01`, the `searchIndex`, `azureBlob`, `indexedOneLake`, and `web` knowledge source types are generally available. Other knowledge source types remain in preview.
 
 1. Use [Knowledge Sources - Get](/rest/api/searchservice/knowledge-sources/get?view=rest-searchservice-2025-11-01-preview&preserve-view=true) (REST API) to get the current definition.
 
    ```http
    GET {{search-endpoint}}/knowledge-sources/{{knowledge-source-name}}?api-version=2025-11-01-preview
-   api-key: {{api-key}}
+   Authorization: Bearer {{search-access-token}}
    Content-Type: application/json
    ```
 
 1. In the response, identify what to carry forward and what to remove:
 
    - For `searchIndex` and `web`, carry forward all property values.
 
-   - For `azureBlob` and `indexedOneLake`, carry forward all property values, but omit `ingestionPermissionOptions` from `ingestionParameters`. This property isn't supported in 2026-04-01.
+   - For `azureBlob` and `indexedOneLake`, carry forward all property values, but omit `ingestionPermissionOptions` from `ingestionParameters`. This property isn't supported in `2026-04-01`.
 
-1. Use [Knowledge Sources - Create Or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-04-01&preserve-view=true) (REST API) to create a new knowledge source with a unique name, the 2026-04-01 API version, and the property values from the previous step.
+1. Use [Knowledge Sources - Create Or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-04-01&preserve-view=true) (REST API) to create a new knowledge source with a unique name, the `2026-04-01` API version, and the property values from the previous step.
 
    The following example shows a `searchIndex` knowledge source. Use a similar pattern for `azureBlob`, `indexedOneLake`, and `web` knowledge sources.
 
    ```http
    PUT {{search-endpoint}}/knowledge-sources/{{new-knowledge-source-name}}?api-version=2026-04-01
-   api-key: {{api-key}}
+   Authorization: Bearer {{search-access-token}}
    Content-Type: application/json
 
    {
@@ -99,29 +253,29 @@ In 2026-04-01, the `searchIndex`, `azureBlob`, `indexedOneLake`, and `web` knowl
 
 #### Migrate the knowledge base
 
-The 2026-04-01 knowledge base has a simpler schema than the 2025-11-01-preview version: it keeps `knowledgeSources` and drops answer generation settings. Review the current definition before you create a new object.
+The `2026-04-01` knowledge base has a simpler schema than the `2025-11-01-preview` version: it keeps `knowledgeSources` and drops answer generation settings. Review the current definition before you create a new object.
 
 1. Use [Knowledge Bases - Get](/rest/api/searchservice/knowledge-bases/get?view=rest-searchservice-2025-11-01-preview&preserve-view=true) (REST API) to get the current definition.
 
    ```http
    GET {{search-endpoint}}/knowledgebases/{{knowledge-base-name}}?api-version=2025-11-01-preview
-   api-key: {{api-key}}
+   Authorization: Bearer {{search-access-token}}
    Content-Type: application/json
    ```
 
 1. In the response, identify what to carry forward and what to remove:
 
    - Note the `knowledgeSources` references. Carry these forward into the new knowledge base.
 
-   - If present, remove `outputMode`, `answerInstructions`, and `retrievalInstructions`. These properties aren't supported in 2026-04-01.
+   - If present, remove `outputMode`, `answerInstructions`, and `retrievalInstructions`. These properties aren't supported in `2026-04-01`.
 
    - If your knowledge base uses a `web` knowledge source, keep `models`. Web retrieval requires model-backed summarization. For all other knowledge source types, remove `models`.
 
-1. Use [Knowledge Bases - Create Or Update](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2026-04-01&preserve-view=true) (REST API) to create a new knowledge base with a unique name, the 2026-04-01 API version, and only the supported properties.
+1. Use [Knowledge Bases - Create Or Update](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2026-04-01&preserve-view=true) (REST API) to create a new knowledge base with a unique name, the `2026-04-01` API version, and only the supported properties.
 
    ```http
    PUT {{search-endpoint}}/knowledgebases/{{new-knowledge-base-name}}?api-version=2026-04-01
-   api-key: {{api-key}}
+   Authorization: Bearer {{search-access-token}}
    Content-Type: application/json
 
    {
@@ -135,28 +289,28 @@ The 2026-04-01 knowledge base has a simpler schema than the 2025-11-01-preview v
 
 #### Update the retrieve request
 
-The 2026-04-01 retrieve request has a different shape than the preview version:
+The `2026-04-01` retrieve request has a different shape than the preview version:
 
 + Use `intents` instead of `messages`.
 
 + Use `maxOutputSizeInTokens` instead of `maxOutputSize`.
 
-+ If present, remove `retrievalReasoningEffort` and `alwaysQuerySource`. These parameters aren't supported in 2026-04-01.
++ If present, remove `retrievalReasoningEffort` and `alwaysQuerySource`. These parameters aren't supported in `2026-04-01`.
 
-+ For follow-up questions, send a new retrieve request with a new semantic intent. 2026-04-01 doesn't maintain a running messages transcript.
++ For follow-up questions, send a new retrieve request with a new semantic intent. `2026-04-01` doesn't maintain a running messages transcript.
 
-To test your knowledge base output with a query, use the 2026-04-01 version of [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-04-01&preserve-view=true) (REST API).
+To test your knowledge base output with a query, use the `2026-04-01` version of [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-04-01&preserve-view=true) (REST API).
 
 ```http
 POST {{search-endpoint}}/knowledgebases/{{new-knowledge-base-name}}/retrieve?api-version=2026-04-01
-api-key: {{api-key}}
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 
 {
   "intents": [
     {
       "type": "semantic",
-      "search": "{{your-query-text}}"
+      "search": "{{query-text}}"
     }
   ],
   "knowledgeSourceParams": [
@@ -177,14 +331,14 @@ If the response has a `200 OK` HTTP code, your knowledge base successfully retri
 
 #### Update billing consent
 
-Starting with 2026-04-01, agentic retrieval billing consent is controlled by a dedicated `knowledgeRetrieval` property that's separate from `semanticSearch`, which now applies only to semantic ranker billing. `knowledgeRetrieval` is a management plane property, so you set it through the Search Management REST API, not the Search Service REST API.
+Starting with the `2026-04-01` API version, agentic retrieval billing consent is controlled by a dedicated `knowledgeRetrieval` property that's separate from `semanticSearch`, which now applies only to semantic ranker billing. `knowledgeRetrieval` is a management plane property, so you set it through the Search Management REST API, not the Search Service REST API.
 
 Use the latest preview version of [Services - Create Or Update](/rest/api/searchmanagement/services/create-or-update?view=rest-management-2026-03-01-preview&preserve-view=true) (REST API) to set `knowledgeRetrieval` on your search service.
 
 ```http
-PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2026-03-01-preview
+PATCH https://management.azure.com/subscriptions/{{subscription-id}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2026-03-01-preview
 Content-Type: application/json
-Authorization: Bearer {{token}}
+Authorization: Bearer {{management-access-token}}
 
 {
   "properties": {
@@ -199,7 +353,7 @@ For valid values and billing details, see [Enable or disable agentic retrieval b
 
 To complete your migration:
 
-1. Update client calls to use the 2026-04-01 API version.
+1. Update client calls to use the `2026-04-01` API version.
 
 1. Update any hardcoded knowledge base or knowledge source names in your code to reference the new objects created during migration.
 
@@ -209,49 +363,26 @@ To complete your migration:
 
 1. Delete preview objects only after the new objects are fully validated and deployed.
 
-### [**2026-05-01-preview**](#tab/2026-05-01-preview)
-
-If you're migrating from [2026-04-01](#2026-04-01-1) or [2025-11-01-preview](#2025-11-01-preview-1), you can move directly to 2026-05-01-preview. Requests, responses, and persisted objects from those versions remain compatible. The differences are additive features and language SDK renames.
-
-1. Update the API version to `2026-05-01-preview` on REST requests. SDK clients use the package's default API version, so you don't need to pass an explicit `serviceVersion` argument. Instead, upgrade to the 2026-05-01-preview SDK package.
-
-1. If you use the Python or JavaScript SDK, update the retrieve client to `KnowledgeBaseRetrievalClient` and call `retrieve(...)` instead of the legacy `retrieveKnowledge(...)`. See [Update code and clients for 2026-05-01-preview](#update-code-and-clients-for-2026-05-01-preview) for the full SDK shape mapping.
-
-1. Optionally adopt the new 2026-05-01-preview features, such as [freshness-aware retrieval](agentic-retrieval-how-to-configure-freshness.md), per-source and final-result document caps, persisted retrieve defaults, knowledge base CORS, and Purview sensitivity-label metadata in retrieve responses. None of these features are required to keep an existing solution working.
-
-#### Update code and clients for 2026-05-01-preview
-
-The 2026-05-01-preview language SDKs introduce code-shape changes across the supported languages.
-
-| Language | Migration updates |
-| --- | --- |
-| Python | Create the retrieve client as `KnowledgeBaseRetrievalClient(endpoint=..., credential=..., knowledge_base_name=...)`. Construct reasoning effort instances such as `KnowledgeRetrievalLowReasoningEffort()` and pass the string `output_mode="answerSynthesis"` on the knowledge base or retrieve request. Pass `AzureOpenAIVectorizerParameters(resource_url=...)` (renamed from `resource_uri`), using the resource root endpoint rather than an `/openai/v1` endpoint. |
-| .NET | Create the retrieve client as `new KnowledgeBaseRetrievalClient(endpoint, knowledgeBaseName, credential)` and pass an `AzureKeyCredential` or token credential. To attach a key-based Azure OpenAI model to a knowledge base, set the model API key on `AzureOpenAIVectorizerParameters.ApiKey`. |
-| Java | Use `KnowledgeBaseRetrievalClientBuilder` to create the retrieve client and read results as `KnowledgeBaseRetrievalResult`. `KnowledgeBaseRetrievalOptions` now exposes `setMessages(...)` alongside `setIntents(...)`, plus `setRetrievalReasoningEffort`, `setOutputMode`, `setMaxOutputSize`, and `setMaxOutputDocuments`, so message-based retrieve and answer synthesis work without a semantic-intent workaround. `KnowledgeBase` adds `setOutputMode`, `setRetrievalReasoningEffort`, `setRetrievalInstructions`, `setAnswerInstructions`, and `setCorsOptions`. `SearchIndexKnowledgeSourceParams` adds `setAlwaysQuerySource`, `setFailOnError`, `setMaxOutputDocuments`, and `setEnableImageServing`. |
-| JavaScript and TypeScript | Use `KnowledgeRetrievalClient.retrieve({ intents: [{ type: "semantic", search: query }] })`. The previous `retrieveKnowledge(...)` method is removed in favor of `retrieve(...)`. |
-
-After you update the client shapes, run the full flow that creates the index, uploads documents, creates a knowledge source, creates a knowledge base, issues a retrieve request, and cleans up resources to confirm the migration end to end.
-
-### [**2025-11-01-preview**](#tab/2025-11-01-preview)
+### 2025-11-01-preview
 
 If you're migrating from [2025-08-01-preview](#2025-08-01-preview-1), "knowledge agent" is renamed to "knowledge base," and multiple properties are relocated to different objects and levels within an object definition.
 
 1. [Update searchIndex knowledge sources](#update-a-searchindex-knowledge-source)
 1. [Update azureBlob knowledge sources](#update-an-azureblob-knowledge-source)
 1. [Replace knowledge agent with knowledge base](#replace-knowledge-agent-with-knowledge-base)
-1. [Update the retrieval request and send a query to test your updates](#update-and-test-the-retrieval-for-2025-11-01-preview-updates)
+1. [Update the retrieve request and send a query to test your updates](#update-and-test-the-retrieval-for-2025-11-01-preview-updates)
 1. [Update client code](#update-code-and-clients-for-2025-11-01-preview)
 
 #### Update a searchIndex knowledge source
 
-This procedure creates a new 2025-11-01-preview `searchIndex` knowledge source at the same functional level as the previous 2025-08-01 version. The underlying index itself requires no updates.
+This procedure creates a new `2025-11-01-preview` `searchIndex` knowledge source at the same functional level as the previous `2025-08-01` version. The underlying index itself requires no updates.
 
 1. List all knowledge sources by name to find your knowledge source.
 
    ```http
    ### List all knowledge sources by name
    GET {{search-endpoint}}/knowledge-sources?api-version=2025-08-01-preview&$select=name
-   api-key: {{api-key}}
+   Authorization: Bearer {{search-access-token}}
    Content-Type: application/json
    ```
 
@@ -260,11 +391,11 @@ This procedure creates a new 2025-11-01-preview `searchIndex` knowledge source a
    ```http
    ### Get a specific knowledge source
    GET {{search-endpoint}}/knowledge-sources/search-index-ks?api-version=2025-08-01-preview
-   api-key: {{api-key}}
+   Authorization: Bearer {{search-access-token}}
    Content-Type: application/json
    ```
 
-   The response should look similar to the following example.
+   The response should be similar to the following example.
 
    ```json
    {
@@ -285,8 +416,8 @@ This procedure creates a new 2025-11-01-preview `searchIndex` knowledge source a
     Start with the 08-01-preview JSON.
 
     ```http
-    POST {{url}}/knowledge-sources/search-index-ks?api-version=2025-08-01-preview
-    api-key: {{key}}
+    POST {{search-endpoint}}/knowledge-sources/search-index-ks?api-version=2025-08-01-preview
+    Authorization: Bearer {{search-access-token}}
     Content-Type: application/json
 
     {
@@ -301,7 +432,7 @@ This procedure creates a new 2025-11-01-preview `searchIndex` knowledge source a
     }
     ```
 
-   Make the following updates for a 2025-11-01-preview migration:
+   Make the following updates for a `2025-11-01-preview` migration:
 
    + Give the knowledge source a new name.
 
@@ -312,8 +443,8 @@ This procedure creates a new 2025-11-01-preview `searchIndex` knowledge source a
 1. Review your updates and then send the request to create the object.
 
     ```http
-    PUT {{url}}/knowledge-sources/search-index-ks-11-01?api-version=2025-11-01-preview
-    api-key: {{key}}
+    PUT {{search-endpoint}}/knowledge-sources/search-index-ks-11-01?api-version=2025-11-01-preview
+    Authorization: Bearer {{search-access-token}}
     Content-Type: application/json
 
     {
@@ -330,20 +461,20 @@ This procedure creates a new 2025-11-01-preview `searchIndex` knowledge source a
     }
     ```
 
-You now have a migrated `searchIndex` knowledge source that's backward compatible with the previous version, using the correct property specifications for the 2025-11-01-preview. 
+You now have a migrated `searchIndex` knowledge source that's backward compatible with the previous version, using the correct property specifications for the `2025-11-01-preview`.
 
 The response includes the full definition of the new object. For more information about new properties available to this knowledge source type, which you can now do through updates, see [How to create a search index knowledge source](agentic-knowledge-source-how-to-search-index.md).
 
 #### Update an azureBlob knowledge source
 
-This procedure creates a new 2025-11-01-preview `azureBlob` knowledge source at the same functional level as the previous 2025-08-01 version. It creates a new set of generated objects: data source, skillset, indexer, index.
+This procedure creates a new `2025-11-01-preview` `azureBlob` knowledge source at the same functional level as the previous `2025-08-01` version. It creates a new set of generated objects: data source, skillset, indexer, index.
 
 1. List all knowledge sources by name to find your knowledge source.
 
    ```http
    ### List all knowledge sources by name
    GET {{search-endpoint}}/knowledge-sources?api-version=2025-08-01-preview&$select=name
-   api-key: {{api-key}}
+   Authorization: Bearer {{search-access-token}}
    Content-Type: application/json
    ```
 
@@ -352,11 +483,11 @@ This procedure creates a new 2025-11-01-preview `azureBlob` knowledge source at
    ```http
    ### Get a specific knowledge source
    GET {{search-endpoint}}/knowledge-sources/azure-blob-ks?api-version=2025-08-01-preview
-   api-key: {{api-key}}
+   Authorization: Bearer {{search-access-token}}
    Content-Type: application/json
    ```
 
-   The response might look similar to the following example if your workflow includes a model. Notice that a response includes the names of the generated objects. These objects are fully independent of the knowledge source and remain operational even if you update or delete their knowledge source.
+   If your workflow includes a model, the response should be similar to the following example. Notice that a response includes the names of the generated objects. These objects are fully independent of the knowledge source and remain operational even if you update or delete their knowledge source.
 
    ```json
     {
@@ -411,8 +542,8 @@ This procedure creates a new 2025-11-01-preview `azureBlob` knowledge source at
     Start with the 08-01-preview JSON.
 
     ```http
-    POST {{url}}/knowledge-sources/azure-blob-ks?api-version=2025-08-01-preview
-    api-key: {{key}}
+    POST {{search-endpoint}}/knowledge-sources/azure-blob-ks?api-version=2025-08-01-preview
+    Authorization: Bearer {{search-access-token}}
     Content-Type: application/json
 
     {
@@ -446,7 +577,7 @@ This procedure creates a new 2025-11-01-preview `azureBlob` knowledge source at
     }
     ```
 
-   Make the following updates for a 2025-11-01-preview migration:
+   Make the following updates for a `2025-11-01-preview` migration:
 
    + Give the knowledge source a new name.
 
@@ -457,8 +588,8 @@ This procedure creates a new 2025-11-01-preview `azureBlob` knowledge source at
 1. Review your updates and then send the request to create the object. New generated objects are created for the indexer pipeline.
 
     ```http
-    PUT {{url}}/knowledge-sources/azure-blob-ks-11-01?api-version=2025-11-01-preview
-    api-key: {{key}}
+    PUT {{search-endpoint}}/knowledge-sources/azure-blob-ks-11-01?api-version=2025-11-01-preview
+    Authorization: Bearer {{search-access-token}}
     Content-Type: application/json
 
     {
@@ -489,24 +620,24 @@ This procedure creates a new 2025-11-01-preview `azureBlob` knowledge source at
     }
     ```
 
-You now have a migrated `azureBlob` knowledge source that's backward compatible with the previous version, using the correct property specifications for the 2025-11-01-preview. 
+You now have a migrated `azureBlob` knowledge source that's backward compatible with the previous version, using the correct property specifications for the `2025-11-01-preview`.
 
 The response includes the full definition of the new object. For more information about new properties available to this knowledge source type, which you can now do through updates, see [Create a blob knowledge source](agentic-knowledge-source-how-to-blob.md).
 
 #### Replace knowledge agent with knowledge base
 
-1. Knowledge bases require a knowledge source. Make sure you have a knowledge source that targets 2025-11-01-preview before you start.
+1. Knowledge bases require a knowledge source. Ensure you have a knowledge source that targets `2025-11-01-preview` before you start.
 
 1. [Get the current definition](/rest/api/searchservice/knowledge-agents/get?view=rest-searchservice-2025-08-01-preview&preserve-view=true) to review existing properties.
 
    ```http
    ### Get a knowledge agent by name
    GET {{search-endpoint}}/agents/earth-at-night?api-version=2025-08-01-preview
-   api-key: {{api-key}}
+   Authorization: Bearer {{search-access-token}}
    Content-Type: application/json
    ```
 
-   The response might look similar to the following example.
+   The response should be similar to the following example.
 
     ```json
     {
@@ -551,8 +682,8 @@ The response includes the full definition of the new object. For more informatio
     Start with the 08-01-preview JSON.
 
     ```http
-    PUT {{url}}/knowledgebases/earth-at-night?api-version=2025-08-01-preview  HTTP/1.1
-    api-key: {{key}}
+    PUT {{search-endpoint}}/knowledgebases/earth-at-night?api-version=2025-08-01-preview  HTTP/1.1
+    Authorization: Bearer {{search-access-token}}
     Content-Type: application/json
 
     {
@@ -587,19 +718,19 @@ The response includes the full definition of the new object. For more informatio
     }
     ```
 
-   Make the following updates for a 2025-11-01-preview migration:
+   Make the following updates for a `2025-11-01-preview` migration:
 
-   + Replace the endpoint: `/knowledgebases/{{your-object-name}}`. Give the knowledge base a unique name.
+   + Replace the endpoint: `/knowledgebases/{{knowledge-base-name}}`. Give the knowledge base a unique name.
 
    + Change the API version to `2025-11-01-preview`.
 
-   + Delete `requestLimits`. The `maxRuntimeInSeconds` and `maxOutputSize` properties are now specified on the retrieval request object directly.
+   + Delete `requestLimits`. The `maxRuntimeInSeconds` and `maxOutputSize` properties are now specified on the retrieve request directly.
 
    + Update `knowledgeSources`:
 
-     + Delete `maxSubQueries` and replace with a retrievalReasoningEffort` (see [Set the retrieval reasoning effort (preview)](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md)).
+     + Delete `maxSubQueries` and replace it with `retrievalReasoningEffort` (see [Set the retrieval reasoning effort (preview)](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md)).
 
-     + Move `alwaysQuerySource`, `includeReferenceSourceData`, `includeReferences`, and `rerankerThreshold` to the `knowledgeSourcesParams` section of a [retrieve action](agentic-retrieval-how-to-retrieve.md).
+    + Move `alwaysQuerySource`, `includeReferenceSourceData`, `includeReferences`, and `rerankerThreshold` to the `knowledgeSourceParams` section of a [retrieve action](agentic-retrieval-how-to-retrieve.md).
 
    + No changes for `models`.
 
@@ -611,13 +742,13 @@ The response includes the full definition of the new object. For more informatio
 
      + If modality is set to `answerSynthesis`, make sure you set the retrieval reasoning effort to low (default) or medium.
 
-   + Add `ingestionParameters` as a requirement for creating a 2025-11-01-preview azureBlob knowledge source.
+   + Add `ingestionParameters` as a requirement for creating a `2025-11-01-preview` azureBlob knowledge source.
 
 1. Review your updates and then send the request to create the object. New generated objects are created for the indexer pipeline.
 
    ```http
-    PUT {{url}}/knowledgebases/earth-at-night-11-01?api-version={{api-version}}
-    api-key: {{key}}
+    PUT {{search-endpoint}}/knowledgebases/earth-at-night-11-01?api-version={{api-version}}
+    Authorization: Bearer {{search-access-token}}
     Content-Type: application/json
 
     {
@@ -643,35 +774,34 @@ The response includes the full definition of the new object. For more informatio
       ],
       "retrievalReasoningEffort": null,
       "outputMode": "answerSynthesis",
-      "answerInstructions": "Provide a concise and accurate answer based on the retrieved information.",
-
+      "answerInstructions": "Provide a concise and accurate answer based on the retrieved information."
     }
    ```
 
-You now have a knowledge base instead of a knowledge agent, and the object is backwards compatible with the previous version. 
+You now have a knowledge base instead of a knowledge agent, and the object is backward compatible with the previous version.
 
 The response includes the full definition of the new object. For more information about new properties available to a knowledge base, which you can now do through updates, see [How to create a knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
 
 #### Update and test the retrieval for 2025-11-01-preview updates
 
-The retrieval request is modified for the 2025-11-01-preview to support more shapes, including a simpler request that minimizes LLM processing. For more information about retrieval in this preview, see [Retrieve data using a knowledge base](agentic-retrieval-how-to-retrieve.md). This section explains how to update your code.
+The retrieve request is modified for the `2025-11-01-preview` to support more shapes, including a simpler request that minimizes LLM processing. For more information about retrieval in this preview, see [Retrieve data using a knowledge base](agentic-retrieval-how-to-retrieve.md). This section explains how to update your code.
 
 1. Change the `/agents/retrieve` endpoint to `/knowledgebases/retrieve`.
 
 1. Change the API version to `2025-11-01-preview`.
 
-1. No changes to `messages` are required if you're using a `low` or `medium` retrievalReasoningEffort. Replace messages with `intent` if you use `minimal `reasoning (see [Set the retrieval reasoning effort (preview)](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md)).
+1. No changes to `messages` are required if you're using `low` or `medium` retrieval reasoning effort. Replace `messages` with `intents` if you use `minimal` reasoning (see [Set the retrieval reasoning effort (preview)](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md)).
 
 1. Modify `knowledgeSourceParams` to include any properties that were removed from the agent: `rerankerThreshold`, `alwaysQuerySource`, `includeReferenceSourceData`, `includeReferences`.
 
 1. Add `retrievalReasoningEffort` set to `minimum` if you were using `attemptFastPath`. If you were using `maxSubQueries`, it no longer exists. Use the `retrievalReasoningEffort` setting to specify subquery processing (see [Set the retrieval reasoning effort (preview)](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md)).
 
-To test your knowledge base's output with a query, use the 2025-11-01-preview of [Knowledge Retrieval - Retrieve (REST API)](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true).
+To test your knowledge base's output with a query, use the `2025-11-01-preview` of [Knowledge Retrieval - Retrieve (REST API)](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-11-01-preview&preserve-view=true).
 
 ```http
 ### Send a query to the knowledge base
-POST {{url}}/knowledgebases/earth-at-night-11-01/retrieve?api-version=2025-11-01-preview
-api-key: {{key}}
+POST {{search-endpoint}}/knowledgebases/earth-at-night-11-01/retrieve?api-version=2025-11-01-preview
+Authorization: Bearer {{search-access-token}}
 Content-Type: application/json
 
 {
@@ -701,15 +831,15 @@ To complete your migration, follow these cleanup steps:
 
 1. Replace all agent references with `knowledgeBases` in configuration files, code, scripts, and tests.
 
-1. Update client calls to use the 2025-11-01-preview.
+1. Update client calls to use the `2025-11-01-preview`.
 
 1. Clear or regenerate cached definitions that were created using the old shapes.
 
-### [**2025-08-01-preview**](#tab/2025-08-01-preview)
+### 2025-08-01-preview
 
 If you created a knowledge agent using the [2025-05-01-preview](#2025-05-01-preview), your agent's definition includes an inline `targetIndexes` array and an optional `defaultMaxDocsForReranker` property.
 
-Starting with the [2025-08-01-preview](#2025-08-01-preview-1), reusable knowledge sources replace `targetIndexes`, and `defaultMaxDocsForReranker` is no longer supported. These breaking changes require you to:
+Starting with the [2025-08-01-preview](#2025-08-01-preview-1) API version, reusable knowledge sources replace `targetIndexes`, and `defaultMaxDocsForReranker` is no longer supported. These breaking changes require you to:
 
 1. [Get the current `targetIndexes` configuration](#get-the-current-configuration)
 1. [Create an equivalent knowledge source](#create-a-knowledge-source)
@@ -719,16 +849,16 @@ Starting with the [2025-08-01-preview](#2025-08-01-preview-1), reusable knowledg
 
 #### Get the current configuration
 
-To retrieve your agent's definition, use the 2025-05-01-preview of [Knowledge Agents - Get (REST API)](/rest/api/searchservice/knowledge-agents/get?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
+To retrieve your agent's definition, use the `2025-05-01-preview` of [Knowledge Agents - Get (REST API)](/rest/api/searchservice/knowledge-agents/get?view=rest-searchservice-2025-05-01-preview&preserve-view=true).
 
 ```http
-@search-url = <YourSearchServiceUrl>
-@agent-name = <YourAgentName>
-@api-key = <YourApiKey>
+@search-endpoint = <search-endpoint>
+@agent-name = <agent-name>
+@search-access-token = <search-access-token>
 
 ### Get agent definition
-GET https://{{search-url}}/agents/{{agent-name}}?api-version=2025-05-01-preview  HTTP/1.1
-    api-key: {{api-key}}
+GET {{search-endpoint}}/agents/{{agent-name}}?api-version=2025-05-01-preview  HTTP/1.1
+    Authorization: Bearer {{search-access-token}}
 ```
 
 The response should be similar to the following example. Copy the `indexName`, `defaultRerankerThreshold`, and `defaultIncludeReferenceSourceData` values for use in the upcoming steps. `defaultMaxDocsForReranker` is deprecated, so you can ignore its value.
@@ -740,81 +870,80 @@ The response should be similar to the following example. Copy the `indexName`, `
   "description": "My description of the agent",
   "targetIndexes": [
     {
-      "indexName": "my-index", // Copy this value
-      "defaultRerankerThreshold": 2.5, // Copy this value
-      "defaultIncludeReferenceSourceData": true, // Copy this value
+      "indexName": "my-index",
+      "defaultRerankerThreshold": 2.5,
+      "defaultIncludeReferenceSourceData": true,
       "defaultMaxDocsForReranker": 100
     }
-  ],
-  ... // Redacted for brevity
+  ]
 }
 ```
 
 #### Create a knowledge source
 
-To create a `searchIndex` knowledge source, use the 2025-08-01-preview of [Knowledge Sources - Create (REST API)](/rest/api/searchservice/knowledge-sources/create?view=rest-searchservice-2025-08-01-preview&preserve-view=true). Set `searchIndexName` to the value you previously copied.
+To create a `searchIndex` knowledge source, use the `2025-08-01-preview` of [Knowledge Sources - Create (REST API)](/rest/api/searchservice/knowledge-sources/create?view=rest-searchservice-2025-08-01-preview&preserve-view=true). Set `searchIndexName` to the value you previously copied.
 
 ```http
-@source-name = <YourSourceName>
+@source-name = <source-name>
 
 ### Create a knowledge source
-PUT https://{{search-url}}/knowledgeSources/{{source-name}}?api-version=2025-08-01-preview  HTTP/1.1
+PUT {{search-endpoint}}/knowledgeSources/{{source-name}}?api-version=2025-08-01-preview  HTTP/1.1
     Content-Type: application/json
-    api-key: {{api-key}}
+    Authorization: Bearer {{search-access-token}}
 
     {
         "name": "{{source-name}}",
         "description": "My description of the knowledge source",
         "kind": "searchIndex",
         "searchIndexParameters": {
-            "searchIndexName": "my-index" // Use the previous value
+            "searchIndexName": "my-index"
         }
     }
 ```
 
-This example creates a knowledge source that represents one index, but you can target multiple indexes or an Azure blob. For more information, see [Create a knowledge source](agentic-knowledge-source-overview.md).
+The previous example creates a knowledge source that represents one index, but you can target multiple indexes or an Azure blob. For more information, see [Create a knowledge source](agentic-knowledge-source-overview.md).
 
 #### Update the agent
 
-To replace `targetIndexes` with `knowledgeSources` in your agent's definition, use the 2025-08-01-preview of [Knowledge Agents - Create or Update (REST API)](/rest/api/searchservice/knowledge-agents/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true). Set `rerankerThreshold` and `includeReferenceSourceData` to the values you previously copied.
+To replace `targetIndexes` with `knowledgeSources` in your agent's definition, use the `2025-08-01-preview` of [Knowledge Agents - Create or Update (REST API)](/rest/api/searchservice/knowledge-agents/create-or-update?view=rest-searchservice-2025-08-01-preview&preserve-view=true). Set `rerankerThreshold` and `includeReferenceSourceData` to the values you previously copied.
 
 ```http
 ### Replace targetIndexes with knowledgeSources
-POST https://{{search-url}}/agents/{{agent-name}}?api-version=2025-08-01-preview  HTTP/1.1
+POST {{search-endpoint}}/agents/{{agent-name}}?api-version=2025-08-01-preview  HTTP/1.1
     Content-Type: application/json
-    api-key: {{api-key}}
+    Authorization: Bearer {{search-access-token}}
 
-    { 
-        "name": "{{agent-name}}", 
+    {
+        "name": "{{agent-name}}",
         "knowledgeSources": [
             {
                 "name": "{{source-name}}",
-                "rerankerThreshold": 2.5, // Use the previous value
-                "includeReferenceSourceData": true // Use the previous value
+                "rerankerThreshold": 2.5,
+                "includeReferenceSourceData": true
             }
-        ]
-    } 
+        ]
+    }
 ```
 
-This example updates the definition to reference one knowledge source, but you can target multiple knowledge sources. You can also use other properties to control the retrieval behavior, such as `alwaysQuerySource`. For more information, see [Create a knowledge agent](agentic-retrieval-how-to-create-knowledge-base.md).
+The previous example updates the definition to reference one knowledge source, but you can target multiple knowledge sources. You can also use other properties to control the retrieval behavior, such as `alwaysQuerySource`. For more information, see [Create a knowledge agent](agentic-retrieval-how-to-create-knowledge-base.md).
 
 #### Test the retrieval for 2025-08-01-preview updates
 
-To test your agent's output with a query, use the 2025-08-01-preview of [Knowledge Retrieval - Retrieve (REST API)](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true).
+To test your agent's output with a query, use the `2025-08-01-preview` of [Knowledge Retrieval - Retrieve (REST API)](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview&preserve-view=true).
 
 ```http
 ### Send a query to the agent
-POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-08-01-preview  HTTP/1.1
+POST {{search-endpoint}}/agents/{{agent-name}}/retrieve?api-version=2025-08-01-preview  HTTP/1.1
     Content-Type: application/json
-    api-key: {{api-key}}
+    Authorization: Bearer {{search-access-token}}
 
     {
       "messages": [
             {
                 "role": "user",
                 "content" : [
                     {
-                        "text": "<YourQueryText>",
+                        "text": "<query-text>",
                         "type": "text"
                     }
                 ]
@@ -830,36 +959,79 @@ If the response has a `200 OK` HTTP code, your agent successfully retrieved cont
 To complete your migration, follow these cleanup steps:
 
 + Replace all `targetIndexes` references with `knowledgeSources` in configuration files, code, scripts, and tests.
-+ Update client calls to use the 2025-08-01-preview.
++ Update client calls to use the `2025-08-01-preview`.
 + Clear or regenerate cached agent definitions that were created using the old shape.
 
----
-
 ## Version-specific changes
 
-This section covers breaking and nonbreaking changes for the following REST API versions:
+This section covers breaking and nonbreaking changes for the following API versions:
 
++ [2026-08-01-preview](#2026-08-01-preview-1)
 + [2026-05-01-preview](#2026-05-01-preview-1)
 + [2026-04-01](#2026-04-01-1)
 + [2025-11-01-preview](#2025-11-01-preview-1)
 + [2025-08-01-preview](#2025-08-01-preview-1)
 + [2025-05-01-preview](#2025-05-01-preview)
 
-### 2026-05-01-preview
+### 2026-08-01-preview
 
-2026-05-01-preview adds knowledge base, knowledge source, and retrieve features on top of [2025-11-01-preview](#2025-11-01-preview-1) without removing previously persisted properties. Existing knowledge bases and knowledge sources that you created in earlier preview versions continue to work. This version mostly exposes new functionality and reverts a few preview-only limits.
+The `2026-08-01-preview` version builds on [2026-05-01-preview](#2026-05-01-preview-1) and includes breaking changes for applications that use Work IQ knowledge sources, offset-based list paging, model-backed activity records, MCP server result processing, or positional generated-client calls.
 
-To review the [REST API reference documentation](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) for this version, select the 2026-05-01-preview API version filter at the top of the page.
+To review the [REST API reference documentation](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) for this version, select the `2026-08-01-preview` API version filter at the top of the page.
 
 #### [**Breaking changes**](#tab/breaking)
 
-There are no breaking changes between 2025-11-01-preview and 2026-05-01-preview. Existing requests that target 2025-11-01-preview continue to work when you change the API version to 2026-05-01-preview.
++ `workIQParameters` is required on a Work IQ knowledge source and must contain `entraAppAuthentication`. Update the source in place, or create a replacement for a side-by-side migration. Pass the user assertion in the `x-ms-query-work-iq-source-authorization` header on retrieve requests.
+
++ Work IQ references remove `attributions`, the `WorkIQAttribution` shape, and `seeMoreWebUrl`. The reshaped reference exposes `searchSensitivityLabelInfo`. Remove dependencies on the deleted fields, and update reference processing for the new sensitivity-label shape.
+
++ The preview-only `$top`, `$skip`, and `$count` parameters are removed. Collection list operations use `search`, `pageSize`, and `searchType`. Responses use `@odata.nextLink` for continuation paging. Update list requests, and follow each `@odata.nextLink` exactly as returned.
+
++ Query-planning, answer-synthesis, and web-summarization activity records remove the scalar `modelName`. The replacement `model` object contains `modelName` and `deploymentId`. Deserialize the nested `model` object for model-backed activity records.
+
++ `McpServerTool.inclusionMode` is removed. On each MCP server `tools` item, map `reranked` to `resultsProcessing: "rerank"` and `always` to `resultsProcessing: "none"`. If omitted, `resultsProcessing` defaults to `rerank`; `none` bypasses reranking and preserves the underlying result order.
 
-The language SDKs that ship 2026-05-01-preview support introduce code-shape changes that are breaking at the SDK layer. See [Update code and clients for 2026-05-01-preview](#update-code-and-clients-for-2026-05-01-preview) for the full SDK shape mapping.
++ The new list parameters change generated method parameter order but don't affect REST parameter binding. Review positional calls after you install an SDK package that supports `2026-08-01-preview`. Prefer named arguments or options where available.
 
 #### [**Nonbreaking changes**](#tab/nonbreaking)
 
-These nonbreaking additions are available in 2026-05-01-preview:
++ [Private network ingestion](agentic-knowledge-source-overview.md#restrict-ingestion-to-a-private-network-preview) support for blob, indexed SharePoint, indexed OneLake, and indexed Azure SQL knowledge sources.
+
++ [File knowledge source](agentic-knowledge-source-how-to-file.md) metadata, file updates, filtered file lists, and `corsOptions` configuration.
+
++ [Knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) support for `gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna` model names.
+
++ Knowledge base `retrieveDefaults` for persisted retrieve request limits.
+
++ Server-sent events (SSE) response support through the `Accept: text/event-stream` request header in the [retrieve action](agentic-retrieval-how-to-retrieve.md).
+
++ [Automatic retrieval reasoning](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) with the `auto` value for `retrievalReasoningEffort`.
+
++ Stored `queryHints` on search-index-backed knowledge source definitions and request-level `queryHintOverrides` on each applicable `knowledgeSourceParams` item.
+
++ Request-time knowledge source exclusion with `neverQuerySource`.
+
++ Per-source reranking control with `resultsProcessing`.
+
++ Service-generated `citationUrl` values on indexed knowledge source references.
+
++ Activity timing fields (`startedAt`, `completedAt`, and `elapsedMs`) in the [activity array](agentic-retrieval-how-to-retrieve.md#activity-array).
+
+---
+
+### 2026-05-01-preview
+
+`2026-05-01-preview` adds knowledge base, knowledge source, and retrieve features on top of [2025-11-01-preview](#2025-11-01-preview-1) without removing previously persisted properties. Existing knowledge bases and knowledge sources that you created in earlier preview versions continue to work. This version mostly exposes new functionality and reverts a few preview-only limits.
+
+To review the [REST API reference documentation](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) for this version, select the `2026-05-01-preview` API version filter at the top of the page.
+
+#### [**Breaking changes**](#tab/breaking)
+
+There are no breaking changes between `2025-11-01-preview` and `2026-05-01-preview`. Existing requests that target `2025-11-01-preview` continue to work when you change the API version to `2026-05-01-preview`.
+
+The language SDKs that ship `2026-05-01-preview` support introduce code-shape changes that are breaking at the SDK layer. See [Update code and clients for 2026-05-01-preview](#update-code-and-clients-for-2026-05-01-preview) for the full SDK shape mapping.
+
+#### [**Nonbreaking changes**](#tab/nonbreaking)
 
 + Freshness-aware retrieval on indexed knowledge sources through a `freshnessPolicy` on `ingestionParameters`.
 
@@ -891,26 +1063,26 @@ These nonbreaking additions are available in 2026-05-01-preview:
 
 ### 2026-04-01
 
-2026-04-01 is the first stable API version for agentic retrieval. It establishes a minimal, extractive retrieval contract and removes preview-era message-based query planning and answer synthesis capabilities.
+`2026-04-01` is the first stable API version for agentic retrieval. It establishes a minimal, extractive retrieval contract and removes preview-era message-based query planning and answer synthesis capabilities.
 
-To review the [REST API reference documentation](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true) for this version, select the 2026-04-01 API version filter at the top of the page.
+To review the [REST API reference documentation](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true) for this version, select the `2026-04-01` API version filter at the top of the page.
 
 #### [**Breaking changes**](#tab/breaking)
 
 The following changes affect both the knowledge base schema and the retrieve request:
 
-  + `retrievalReasoningEffort` is removed. Knowledge bases previously configured with `low` or `medium` reasoning effort aren't compatible with 2026-04-01 and must be recreated.
-    
+  + `retrievalReasoningEffort` is removed. Knowledge bases previously configured with `low` or `medium` reasoning effort aren't compatible with `2026-04-01` and must be recreated.
+
   + `outputMode` is removed. Retrieval returns extractive grounded content by default. Answer synthesis isn't supported.
 
 The following changes affect the retrieve request only:
 
   + `intents` replaces `messages`.
-    
+
   + `alwaysQuerySource` is removed from `knowledgeSourceParams`.
-    
+
   + `maxOutputSize` is renamed to `maxOutputSizeInTokens`.
-    
+
   + Conversational state isn't maintained across requests. The `messages`-based multi-turn pattern isn't supported.
 
 The following change affects `azureBlob` and `indexedOneLake` knowledge sources:
@@ -922,9 +1094,9 @@ The following change affects `azureBlob` and `indexedOneLake` knowledge sources:
 
 #### [**Nonbreaking changes**](#tab/nonbreaking)
 
-+ `searchIndex`, `azureBlob`, `indexedOneLake`, and `web` knowledge source types are generally available in 2026-04-01. Existing indexed content remains valid; migration requires recreating knowledge source objects, not rebuilding indexes.
++ `searchIndex`, `azureBlob`, `indexedOneLake`, and `web` knowledge source types are generally available in `2026-04-01`. Existing indexed content remains valid; migration requires recreating knowledge source objects, not rebuilding indexes.
 
-+ Indexed and remote SharePoint knowledge sources remain in preview and aren't available in 2026-04-01.
++ Indexed and remote SharePoint knowledge sources remain in preview and aren't available in `2026-04-01`.
 
 + The knowledge source `status` operation now includes the knowledge source type directly and provides richer indexing error details.
 
@@ -936,32 +1108,32 @@ The following change affects `azureBlob` and `indexedOneLake` knowledge sources:
 
 + Retrieve responses still include `activity` and `references`, even though the request contract is narrower.
 
-+ A new management plane property, `knowledgeRetrieval`, controls agentic retrieval billing independently of `semanticSearch` on 2026-04-01 and later. The default value is `free`. To enable paid usage, set `knowledgeRetrieval` to `standard`. For more information, see [Enable or disable agentic retrieval billing](agentic-retrieval-how-to-enable-disable.md).
++ A new management plane property, `knowledgeRetrieval`, controls agentic retrieval billing independently of `semanticSearch` on `2026-04-01` and later. The default value is `free`. To enable paid usage, set `knowledgeRetrieval` to `standard`. For more information, see [Enable or disable agentic retrieval billing](agentic-retrieval-how-to-enable-disable.md).
 
 ---
 
 ### 2025-11-01-preview
 
-To review the [REST API reference documentation](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) for this version, select the 2025-11-01-preview API version filter at the top of the page.
+To review the [REST API reference documentation](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) for this version, select the `2025-11-01-preview` API version filter at the top of the page.
 
 #### [**Breaking changes**](#tab/breaking)
 
 + Knowledge agent is renamed to knowledge base.
 
   | Previous route | New route |
-  |-----|-----|
+  | ----- | ----- |
   | `/agents` | `/knowledgebases` |
   | `/agents/agent-name` | `/knowledgebases/knowledge-base-name` |
   | `/agents/agent-name/retrieve` | `/knowledgebases/knowledge-base-name/retrieve` |
 
 + Knowledge agent (base) `outputConfiguration` is renamed to `outputMode` and changed from an object to a string enumerator. Several properties are impacted:
 
-  + `includeActivity` is moved from `outputConfiguration` onto the retrieval request object directly.
+  + `includeActivity` is moved from `outputConfiguration` onto the retrieve request directly.
   + `attemptFastPath` in `outputConfiguration` is removed entirely. The new `minimal` reasoning effort is the replacement.
 
-+ Knowledge agent (base) `requestLimits` is removed. Its child properties of `maxRuntimeInSeconds` and `maxOutputSize` are moved onto the retrieval request object directly.
++ Knowledge agent (base) `requestLimits` is removed. Its child properties of `maxRuntimeInSeconds` and `maxOutputSize` are moved onto the retrieve request directly.
 
-+ Knowledge agent (base) `knowledgeSources` parameters now only list the names of knowledge source used by a knowledge base. Other child properties that used to be under `knowledgeSources` are moved to the `knowledgeSourceParams` properties of the retrieval request object: 
++ Knowledge agent (base) `knowledgeSources` parameters now only list the names of knowledge source used by a knowledge base. Other child properties that used to be under `knowledgeSources` are moved to the `knowledgeSourceParams` properties of the retrieve request:
 
   + `rerankerThreshold`
   + `alwaysQuerySource`
@@ -970,7 +1142,7 @@ To review the [REST API reference documentation](/rest/api/searchservice/operati
 
   The `maxSubQueries` property is gone. Its replacement is the new retrieval reasoning effort property.
 
-+ Knowledge agent (base) retrieval request object: The `semanticReranker` activity record is replaced with the `agenticReasoning` activity record type.
++ Knowledge agent (base) retrieve request: The `semanticReranker` activity record is replaced with the `agenticReasoning` activity record type.
 
 + Knowledge sources for both `azureBlob` and `searchIndex`: top-level properties for `identity`, `embeddingModel`, `chatCompletionModel`, `disableImageVerbalization`, and `ingestionSchedule` are now part of an `ingestionParameters` object on the knowledge source. All knowledge sources that pull from a search index have an `ingestionParameters` object.
 
@@ -984,7 +1156,7 @@ To review the [REST API reference documentation](/rest/api/searchservice/operati
 
 + All knowledge sources that pull from a search index have a `status` operation, which returns the synchronization status of the knowledge source with its data source.
 
-+ The `searchIndex` knowledge source adds `semanticConfigurationName` that overrides the default semantic configuration used by the retrieval request.
++ The `searchIndex` knowledge source adds `semanticConfigurationName` that overrides the default semantic configuration used by the retrieve request.
 
 + The `searchIndex` knowledge source adds `sourceDataFields` and `searchDataFields` to specify which fields are used at query time and also returned in a response.
 
@@ -998,7 +1170,7 @@ To review the [REST API reference documentation](/rest/api/searchservice/operati
 
 ### 2025-08-01-preview
 
-To review the [REST API reference documentation](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) for this version, select the 2025-08-01-preview API version filter at the top of the page.
+To review the [REST API reference documentation](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true) for this version, select the `2025-08-01-preview` API version filter at the top of the page.
 
 #### [**Breaking changes**](#tab/breaking)
 
@@ -1018,9 +1190,9 @@ To review the [REST API reference documentation](/rest/api/searchservice/operati
 
 ### 2025-05-01-preview
 
-This REST API version introduces agentic retrieval and knowledge agents. Each agent definition requires a `targetIndexes` array that specifies a single index and optional properties, such as `defaultRerankerThreshold` and `defaultIncludeReferenceSourceData`.
+This API version introduces agentic retrieval and knowledge agents. Each agent definition requires a `targetIndexes` array that specifies a single index and optional properties, such as `defaultRerankerThreshold` and `defaultIncludeReferenceSourceData`.
 
-To review the [REST API reference documentation](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) for this version, select the 2025-05-01-preview API version filter at the top of the page.
+To review the [REST API reference documentation](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-05-01-preview&preserve-view=true) for this version, select the `2025-05-01-preview` API version filter at the top of the page.
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エージェント検索移行に関するドキュメントの大幅な更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエージェント検索コードの移行方法に関するドキュメントを大幅に更新したもので、特に新しいAPIバージョンへの移行に伴う破壊的変更や互換性の考慮が詳述されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：旧APIバージョンのリファレンスが、2026-05-01-previewから2026-08-01-previewに変更されました。これに伴い、新機能や改善点が含まれるようになっています。

2. **新しい移行指針**：新しいAPIへの移行手順が詳細に記載されており、特に新しい知識ソースや知識ベースの作成手順、古いオブジェクトの削除についての指示が明確にされています。

3. **重要な注意事項の強調**：移行を行う際の注意事項が強調されており、ユーザーは新しいパラメータやメソッド名の変更に注意を払う必要があります。特に、APIの設計が変更されたいくつかのパラメータが削除または改名されています。

4. **一貫性のある用語の使用**：用語の統一がなされ、「knowledge agent」という表現が「knowledge base」に変更され、全体の文書が一貫性を保つように修正されています。

5. **SDKの変更についての情報**：Microsoftが提供する各種SDKとの互換性についても具体的に記載され、SDKを使用しているユーザーに向けた詳細なガイダンスを提供しています。

6. **ドキュメントの構成改善**：過去のAPIバージョンからの移行時に必要な更新項目や手順が明確に整理されており、ユーザーが参照しやすい形になっています。

このように、ドキュメント全体が見直され、ユーザーが新しいAPIに円滑に移行できるように支援しています。移行時に考慮すべき要点が非常に詳細に解説されているため、既存のソリューションを新しいバージョンに適応させる際のサポートが強化されています。

## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "エージェント検索の取得方法に関するドキュメントの大幅な更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchのエージェント検索に関する「取得方法」に関するドキュメントの大幅な更新を示しており、主に新しい機能の追加と、かつてのバージョンからの改善を反映しています。

主な変更点は以下の通りです：

1. **大規模なコンテンツの追加**：この変更では1240行の内容が新たに追加されており、エージェント検索の取得方法に関する詳細が豊富に説明されています。これにより、ユーザーは取得機能をより理解しやすくなります。

2. **改善された手順**：ドキュメント内における操作手順が明確にされており、ユーザーがエージェント検索を利用するための取得プロセスをスムーズに実行できるようにしています。

3. **新しい例とリソース**：具体的な例やコードスニペットが豊富に追加され、ユーザーは実際の実装において必要な情報を容易に参照できるようになっています。この変更は特に開発者にとって有益です。

4. **関連リソースのリンク**：他のドキュメントやリソースへのリンクが強化され、ユーザーが必要な情報に迅速にアクセスできるようになっています。

5. **削除された内容の整理**：172行の内容が削除されており、これによりドキュメントが一層整理され、必要ない情報が取り除かれて使いやすくなっています。

このように、全体のドキュメントが充実し、情報が整理された結果、ユーザーはエージェント検索の取得に関する理解を深め、技術的な適用をより簡単に行えるようになりました。この更新は、特に新機能の利用を計画している開発者にとって、非常に価値のある情報となります。

## articles/search/agentic-retrieval-how-to-set-retrieval-reasoning-effort.md{#item-141e97}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,15 @@
 ---
 title: Set the Retrieval Reasoning Effort
 description: Learn how to set the level of LLM processing for agentic retrieval in Azure AI Search.
-ms.date: 06/08/2026
+ms.date: 08/17/2026
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.custom:
   - references_regions
+  - dev-focus
+  - doc-kit-assisted
 ai-usage: ai-assisted
+zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Set the retrieval reasoning effort (preview)
@@ -16,40 +19,66 @@ ai-usage: ai-assisted
 [!INCLUDE [Preview feature](./includes/previews/agentic-retrieval-preview-feature.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
 In agentic retrieval, you can specify the level of large language model (LLM) processing for query planning and answer formulation. Use the *retrieval reasoning effort* (preview) to set LLM processing levels that affect costs and latency. Extra LLM processing improves relevance, but it also takes longer and uses billable LLM resources.
 
-You can set this property in a knowledge base or a retrieve request. The knowledge base setting establishes the default for all queries, while the retrieve request setting overrides the default on a query-by-query basis.
+You can set this property in a knowledge base or a retrieve request. The knowledge base setting establishes the default for all queries, while the retrieve request setting overrides the default on a query-by-query basis. If neither setting is present, the service uses `low`.
+
+### Usage support
+
+| [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-08-01-preview&preserve-view=true) |
+| -- | -- | -- | -- | -- | -- | -- |
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
-- An Azure AI Search service with a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md).
+- An existing [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) with at least one knowledge source and a model configuration.
+
+- Permission to update and query knowledge bases. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** and **Search Index Data Reader** roles assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
+
+::: zone pivot="csharp"
+
+- The latest [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) preview package: `dotnet add package Azure.Search.Documents --prerelease`
+
+- For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
+
+::: zone-end
+
+::: zone pivot="python"
+
+- The latest [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) preview package: `pip install --pre azure-search-documents`
+
+- For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
+
+::: zone-end
+
+::: zone pivot="rest"
 
-- Permissions to update knowledge bases. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
+- The [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) version of the Search Service REST API.
 
-- If the knowledge base specifies an LLM, the search service must have a [managed identity](search-how-to-managed-identities.md) with **Cognitive Services User** permissions on the Microsoft Foundry resource.
+- For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
-- The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) REST API or an equivalent Azure SDK preview package: [.NET](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md)
+::: zone-end
 
 ## Choose a reasoning effort
 
-Choose a reasoning effort based on the tradeoff you want between
-latency, cost, and retrieval depth.
+Choose a reasoning effort based on the tradeoff you want between latency, cost, and retrieval depth.
 
 ### Reasoning effort levels
 
 | Level | Description | Recommendation | Limits |
 | --- | --- | --- | --- |
-| `minimal` | Disables LLM-based query planning to deliver the lowest cost and latency for agentic retrieval. It issues direct text and vector searches across the knowledge sources listed in the knowledge base, and returns the best-matching passages. Because all knowledge sources in the knowledge base are always searched and no query expansion is performed, behavior is predictable and easy to control. It also means the `alwaysQueryKnowledgeSource` property on a retrieve request is ignored. | Use `minimal` for migrations from the [Search API](/rest/api/searchservice/documents/search-post) or when you want to manage query planning yourself. | <ul><li>`outputMode` must be set to `extractiveData`.</li><li>[Answer synthesis](agentic-retrieval-how-to-answer-synthesis.md) and [web knowledge](agentic-knowledge-source-how-to-web.md) aren't supported.</li><li>Maximum of [10 knowledge sources per knowledge base](search-limits-quotas-capacity.md#agentic-retrieval-limits).</li></ul> |
-| `low` | The default mode of agentic retrieval, running a single pass of LLM-based query planning and knowledge source selection. The agentic retrieval engine generates subqueries and fans them out to the selected knowledge sources, then merges the results. You can enable answer synthesis to produce a grounded natural-language response with inline citations. | Use `low` when you want a balance between minimal latency and deeper processing. | <ul><li>5,000 answer tokens.</li><li>In the 2026-05-01-preview, maximum of [10 knowledge sources per knowledge base on most paid tiers](search-limits-quotas-capacity.md#agentic-retrieval-limits).</li><li>In earlier preview API versions, maximum of three subqueries from three knowledge sources per knowledge base.</li><li>Maximum of 50 documents for semantic ranking, and 10 documents if the semantic ranker uses L3 classification.</li></ul> |
-| `medium` | Adds deeper search and an enhanced retrieval stack to agentic retrieval to maximize completeness. After the first search is performed, a [high-precision semantic classifier](search-relevance-overview.md) evaluates the retrieved documents to determine whether further processing and L3 ranking is required. If the initial results from the first pass are insufficiently relevant to the query, a follow-up iteration is performed using a revised query plan. This revised query plan takes the previous results into account and iterates by fine-tuning queries, broadening terms, or adding other knowledge sources such as the web. It also increases resource limits compared to low and minimal effort. This reasoning level optimizes for relevance rather than exhaustive recall. | Use `medium` to maximize the utility of LLM-assisted knowledge retrieval. | <ul><li>10,000 answer tokens.</li><li>In the 2026-05-01-preview, maximum of [10 knowledge sources per knowledge base on most paid tiers](search-limits-quotas-capacity.md#agentic-retrieval-limits).</li><li>In earlier preview API versions, maximum of five subqueries from five knowledge sources per knowledge base.</li><li>Maximum of 50 documents for semantic ranking, and 20 documents if the semantic ranker uses L3 classification.</li><li>Available in [select regions](#region-support-for-medium-retrieval).</li></ul> |
+| `minimal` | Disables LLM-based query planning to deliver the lowest cost and latency for agentic retrieval. It issues direct text and vector searches across the knowledge sources listed in the knowledge base, and returns the best-matching passages. Because all knowledge sources in the knowledge base are always searched and no query expansion is performed, behavior is predictable and easy to control. It also means the `alwaysQueryKnowledgeSource` property on a retrieve request is ignored. | Use `minimal` for migrations from the [Search API](/rest/api/searchservice/documents/search-post) or when you want to manage query planning yourself. | <ul><li>`outputMode` must be set to `extractiveData`.</li><li>[Answer synthesis (preview)](agentic-retrieval-how-to-answer-synthesis.md) and [web knowledge](agentic-knowledge-source-how-to-web.md) aren't supported.</li><li>Maximum of [10 knowledge sources per knowledge base](search-limits-quotas-capacity.md#agentic-retrieval-limits).</li></ul> |
+| `low` | The default mode of agentic retrieval, running a single pass of LLM-based query planning and knowledge source selection. The agentic retrieval engine generates subqueries and fans them out to the selected knowledge sources, then merges the results. You can enable answer synthesis (preview) to produce a grounded natural-language response with inline citations. | Use `low` when you want a balance between minimal latency and deeper processing. | <ul><li>5,000 answer tokens.</li><li>Maximum of 50 documents for semantic ranking, and 10 documents if the semantic ranker uses L3 classification.</li></ul> |
+| `medium` | Adds deeper search and an enhanced retrieval stack to agentic retrieval to maximize completeness. After the first search, a high-precision semantic classifier evaluates the retrieved documents. If the initial results aren't sufficiently relevant, the service performs one follow-up iteration using a revised query plan. | Use `medium` to maximize the utility of LLM-assisted knowledge retrieval. | <ul><li>10,000 answer tokens.</li><li>Maximum of 50 documents for semantic ranking, and 20 documents if the semantic ranker uses L3 classification.</li><li>Available in [select regions](#region-support-for-medium-retrieval).</li></ul> |
+| `auto` | Starts with a lightweight retrieval pass. If the first pass provides enough grounding, the service returns the result. Otherwise, it continues with LLM-based query planning, up to medium effort. | Use `auto` when you want the service to balance retrieval depth and latency for each request. | <ul><li>Requires the 2026-08-01-preview REST API.</li><li>Requires a model on the knowledge base.</li><li>Available in all [regions that support agentic retrieval](search-region-support.md).</li><li>Earlier API versions return `400 Bad Request`.</li></ul> |
 
 ### Iterative search for medium retrieval
 
@@ -65,7 +94,7 @@ The semantic classifier:
 
 There's only one retry. Each iteration adds latency and cost, so the system constrains retry to one pass. A second iteration adds input tokens to the query pipeline, which adds to the overall billable input token count.
 
-Iteration can reuse or choose different sources. The second pass selects the most promising knowledge resource to provide the missing information.
+Iteration can reuse existing knowledge sources or choose different sources. The second pass selects the most promising knowledge source to provide the missing information.
 
 ### Region support for medium retrieval
 
@@ -89,49 +118,218 @@ You can set a medium retrieval reasoning effort if your search service is in one
 
 ## Set the reasoning effort in a knowledge base
 
-This section demonstrates how to set the retrieval reasoning effort in an existing knowledge base. Although you can use this configuration for new knowledge bases, knowledge base creation is beyond the scope of this article.
+Set `retrievalReasoningEffort` in a knowledge base definition to establish the default for its queries. The `auto` reasoning effort requires a model configuration. The following example preserves the existing `knowledgeSources` and `models` configuration, sets the reasoning effort to `auto`, and updates the knowledge base.
+
+::: zone pivot="csharp"
+
+```csharp
+using Azure.Identity;
+using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+using Azure.Search.Documents.KnowledgeBases.Models;
+
+var endpoint = new Uri("<search-endpoint>");
+var credential = new DefaultAzureCredential();
+var knowledgeBaseName = "<knowledge-base-name>";
+
+var indexClient = new SearchIndexClient(endpoint, credential);
+var knowledgeBase = (
+    await indexClient.GetKnowledgeBaseAsync(knowledgeBaseName)).Value;
+knowledgeBase.RetrievalReasoningEffort =
+    new KnowledgeRetrievalAutoReasoningEffort();
+await indexClient.CreateOrUpdateKnowledgeBaseAsync(knowledgeBase);
+```
+
+**Reference:** [KnowledgeBase](/dotnet/api/azure.search.documents.indexes.models.knowledgebase?view=azure-dotnet-preview&preserve-view=true)
+
+To use another level, replace `KnowledgeRetrievalAutoReasoningEffort` with `KnowledgeRetrievalMinimalReasoningEffort`, `KnowledgeRetrievalLowReasoningEffort`, or `KnowledgeRetrievalMediumReasoningEffort`.
+
+::: zone-end
+
+::: zone pivot="python"
+
+```python
+from azure.identity import DefaultAzureCredential
+from azure.search.documents.indexes import SearchIndexClient
+from azure.search.documents.knowledgebases.models import (
+    KnowledgeRetrievalAutoReasoningEffort,
+)
+
+endpoint = "<search-endpoint>"
+credential = DefaultAzureCredential()
+knowledge_base_name = "<knowledge-base-name>"
 
-To establish the default behavior, set `retrievalReasoningEffort` in the knowledge base definition.
+index_client = SearchIndexClient(endpoint, credential)
+knowledge_base = index_client.get_knowledge_base(knowledge_base_name)
+knowledge_base.retrieval_reasoning_effort = (
+    KnowledgeRetrievalAutoReasoningEffort()
+)
+index_client.create_or_update_knowledge_base(knowledge_base)
+```
+
+**Reference:** [KnowledgeBase](/python/api/azure-search-documents/azure.search.documents.indexes.models.knowledgebase)
+
+To use another level, replace `KnowledgeRetrievalAutoReasoningEffort` with `KnowledgeRetrievalMinimalReasoningEffort`, `KnowledgeRetrievalLowReasoningEffort`, or `KnowledgeRetrievalMediumReasoningEffort`.
+
+::: zone-end
+
+::: zone pivot="rest"
 
 ```http
-### Set retrieval reasoning effort in a knowledge base
-PUT {{search-url}}/knowledgebases/{{knowledge-base-name}}?api-version=2026-05-01-preview
+@api-version = 2026-08-01-preview
+@knowledge-base-url = {{search-endpoint}}/knowledgebases/{{knowledge-base-name}}
+
+PUT {{knowledge-base-url}}?api-version={{api-version}}
 Content-Type: application/json
-api-key: {{api-key}}
+Authorization: Bearer {{search-access-token}}
 
 {
   "name": "{{knowledge-base-name}}",
-  "knowledgeSources": [ ... // OMITTED FOR BREVITY ],
+  "knowledgeSources": [
+    {
+      "name": "{{knowledge-source-name}}"
+    }
+  ],
+  "models": [
+    {
+      "kind": "azureOpenAI",
+      "azureOpenAIParameters": {
+        "resourceUri": "{{aoai-endpoint}}",
+        "authIdentity": null,
+        "deploymentId": "{{model-deployment-name}}",
+        "modelName": "{{model-name}}"
+      }
+    }
+  ],
   "retrievalReasoningEffort": {
-    "kind": "low"
+    "kind": "auto"
   }
 }
 ```
 
-**Reference:** [Knowledge Bases - Create or Update](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Bases - Create or Update](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
+
+To use another level, set `retrievalReasoningEffort.kind` to `minimal`, `low`, or `medium`.
+
+::: zone-end
 
 ## Set the reasoning effort in a retrieve request
 
-To override the default on a query-by-query basis, set `retrievalReasoningEffort` in the retrieve request body.
+Set `retrievalReasoningEffort` in a retrieve request to override the knowledge base default for that request. The following example sends a message, uses `low` to override the `auto` default from the previous section, and enables answer synthesis (preview).
+
+::: zone pivot="csharp"
+
+```csharp
+using Azure.Identity;
+using Azure.Search.Documents.KnowledgeBases;
+using Azure.Search.Documents.KnowledgeBases.Models;
+
+var endpoint = new Uri("<search-endpoint>");
+var credential = new DefaultAzureCredential();
+var knowledgeBaseName = "<knowledge-base-name>";
+
+var kbClient = new KnowledgeBaseRetrievalClient(
+    endpoint, knowledgeBaseName, credential);
+var request = new KnowledgeBaseRetrievalRequest
+{
+    RetrievalReasoningEffort =
+        new KnowledgeRetrievalLowReasoningEffort(),
+    OutputMode = KnowledgeRetrievalOutputMode.AnswerSynthesis
+};
+
+request.Messages.Add(
+    new KnowledgeBaseMessage(
+        content: new[] {
+            new KnowledgeBaseMessageTextContent("What is the return policy?")
+        }
+    ) { Role = "user" }
+);
+
+var result = await kbClient.RetrieveAsync(request);
+```
+
+**Reference:** [KnowledgeBaseRetrievalRequest](/dotnet/api/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest?view=azure-dotnet-preview&preserve-view=true)
+
+::: zone-end
+
+::: zone pivot="python"
+
+```python
+from azure.identity import DefaultAzureCredential
+from azure.search.documents.knowledgebases import KnowledgeBaseRetrievalClient
+from azure.search.documents.knowledgebases.models import (
+    KnowledgeBaseMessage,
+    KnowledgeBaseMessageTextContent,
+    KnowledgeBaseRetrievalRequest,
+    KnowledgeRetrievalOutputMode,
+    KnowledgeRetrievalLowReasoningEffort,
+)
+
+endpoint = "<search-endpoint>"
+credential = DefaultAzureCredential()
+knowledge_base_name = "<knowledge-base-name>"
+
+kb_client = KnowledgeBaseRetrievalClient(
+    endpoint,
+    credential,
+    knowledge_base_name=knowledge_base_name,
+)
+request = KnowledgeBaseRetrievalRequest(
+    messages=[
+        KnowledgeBaseMessage(
+            role="user",
+            content=[
+                KnowledgeBaseMessageTextContent(
+                    text="What is the return policy?"
+                )
+            ],
+        )
+    ],
+    retrieval_reasoning_effort=KnowledgeRetrievalLowReasoningEffort(),
+    output_mode=KnowledgeRetrievalOutputMode.ANSWER_SYNTHESIS,
+)
+
+result = kb_client.retrieve(request)
+```
+
+**Reference:** [KnowledgeBaseRetrievalRequest](/python/api/azure-search-documents/azure.search.documents.knowledgebases.models.knowledgebaseretrievalrequest)
+
+::: zone-end
+
+::: zone pivot="rest"
 
 ```http
-### Override retrieval reasoning effort in a retrieve request
-POST {{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version=2026-05-01-preview
+@api-version = 2026-08-01-preview
+@retrieve-url = {{search-endpoint}}/knowledgebases/{{knowledge-base-name}}/retrieve
+
+POST {{retrieve-url}}?api-version={{api-version}}
 Content-Type: application/json
-api-key: {{api-key}}
+Authorization: Bearer {{search-access-token}}
 
 {
-  "messages": [ ... // OMITTED FOR BREVITY ],
+  "messages": [
+    {
+      "role": "user",
+      "content": [
+        {
+          "type": "text",
+          "text": "What is the return policy?"
+        }
+      ]
+    }
+  ],
   "retrievalReasoningEffort": {
     "kind": "low"
   },
-  "outputMode": "answerSynthesis",
-  "maxRuntimeInSeconds": 30,
-  "maxOutputSize": 6000
+  "outputMode": "answerSynthesis"
 }
 ```
 
-**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
+
+::: zone-end
+
+The retrieve request returns a grounded answer based on the knowledge sources configured in the knowledge base.
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索の推論努力設定に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエージェント検索の「推論努力の設定」に関するドキュメントの更新を示しており、特定の情報の追加と共に、既存の内容の改訂が行われています。

主な変更点は以下の通りです：

1. **日付の更新**：ドキュメントの更新日が`2026年8月17日`に改訂されており、最新の情報が反映されています。

2. **APIバージョンの更新**：重要な注意が、`2026-05-01-preview`から`2026-08-01-preview`に変更され、これにより新しいAPIバージョンの利用を促しています。

3. **新しい機能の追加**：`auto`という新しい推論努力のレベルが追加され、サービスが各リクエストの深さと遅延のバランスをとれるようになったことが説明されています。

4. **より詳しい設定ガイド**：リクエストごとに推論努力を上書きする方法や、既存の知識ベースの設定例が具体的に示されています。また、各SDKおよびREST APIとの互換性に関する情報も提供されています。

5. **ユーザーガイドの強化**：構成の要件や権限付与に関する改善点が加えられ、ユーザーが知識ベースをより効率的に管理・操作できるようにしています。

6. **コード例の拡充**：C#、Python、REST APIそれぞれに対し、具体的なコードスニペットが提供されており、ユーザーはそれを参考にして実装を行うことができます。

7. **関連コンテンツのリンク**：推論努力の各レベルに関連する他のドキュメントへのリンクが追加され、情報の参照が容易になっています。

このように、ドキュメント全体が更新され、ユーザーにとってわかりやすく、実用的な情報が提供される形になっています。特に新機能の導入によって、エージェント検索の効果的な利用が促進されています。

## articles/search/agentic-retrieval-overview.md{#item-d1f354}

<details>
<summary>Diff</summary>
````diff
@@ -17,17 +17,17 @@ ai-usage: ai-assisted
 [!INCLUDE [GA announcement](./includes/previews/agentic-retrieval-ga-announcement.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-In Azure AI Search, *agentic retrieval* is a multi-query pipeline designed for complex questions posed by users or agents in chat and copilot apps. It's intended for [retrieval-augmented generation](retrieval-augmented-generation-overview.md) (RAG) patterns and agent-to-agent workflows. 
+In Azure AI Search, *agentic retrieval* is a multi-query pipeline designed for complex questions posed by users or agents in chat and copilot apps. It's intended for [retrieval-augmented generation](retrieval-augmented-generation-overview.md) (RAG) patterns and agent-to-agent workflows.
 
-Here's what it does:
+Here's what agentic retrieval does:
 
 + Can use a large language model (LLM) to break down a complex query into smaller, focused subqueries for better coverage over proprietary and external content. Subqueries can include chat history for extra context.
 
@@ -41,7 +41,7 @@ This high-performance pipeline helps you generate high-quality grounding data or
 
 ## Why use agentic retrieval?
 
-There are two use cases for agentic retrieval. First, it powers [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) in the Microsoft Foundry portal by providing the knowledge layer for agent solutions. Second, it's the basis for custom agentic solutions you build using the Azure AI Search APIs.
+Agentic retrieval supports both managed and custom experiences for agents and apps. In the Microsoft Foundry portal, it powers [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) as a managed knowledge layer for agents. You can also build custom agentic retrieval solutions by using the Azure portal, Search Service REST API, or a supported Azure SDK.
 
 Use agentic retrieval when you want to provide agents and apps with the most relevant content for answering harder questions, drawing on chat context, your proprietary content, and external sources.
 
@@ -76,7 +76,7 @@ The agentic retrieval process works as follows:
 For all agentic retrieval scenarios, a knowledge base and at least one knowledge source are required. Other components are optional and depend on your configuration.
 
 | Component | Service | Role |
-|-----------|---------|------|
+| ----------- | --------- | ------ |
 | Knowledge base | Azure AI Search | Orchestrates the pipeline, managing knowledge sources and query parameters. |
 | Knowledge source | Azure AI Search | Defines the content used in the pipeline. Can be indexed (backed by a search index on your service) or remote (content retrieved at query time from an external platform). |
 | Search index | Azure AI Search | Stores searchable content (text and vectors) with a semantic configuration. Determines which query types run and which optimizations apply. Required for indexed knowledge sources only. |
@@ -102,7 +102,7 @@ Agentic retrieval incurs charges from two services:
 The following table compares billing between the classic single-query pipeline and the agentic retrieval multi-query pipeline. In the classic pipeline, the billable component is [semantic ranker](semantic-search-overview.md).
 
 | Aspect | Classic pipeline | Agentic retrieval |
-|--|--|--|
+| -- | -- | -- |
 | Unit | Query based | Token based |
 | Cost per unit | Uniform cost per query | Variable cost per token (depends on reasoning effort) |
 | Cost estimation | Estimate query count | Estimate token usage |
@@ -148,9 +148,9 @@ Putting it all together, you'd pay about $3.30 for agentic retrieval in Azure AI
 
 + Review the activity log in the response to find out what queries were issued to which sources and the parameters used. You can reissue those queries against your indexes and use a public tokenizer to estimate tokens and compare to API-reported usage. Precise reconstruction of a query or response isn't guaranteed however. Factors include the type of knowledge source, such as public web data or a remote SharePoint knowledge source that's predicated on a user identity, which can affect query reproduction.
 
-+ Reduce the number of knowledge sources (indexes); consolidating content can lower fan-out and token volume. 
++ Reduce the number of knowledge sources (indexes); consolidating content can lower fan-out and token volume.
 
-+ Lower the reasoning effort to reduce LLM usage during query planning and query expansion (iterative search). 
++ Lower the reasoning effort to reduce LLM usage during query planning and query expansion (iterative search).
 
 + Organize content so the most relevant information can be found with fewer sources and documents (for example, curated summaries or tables).
 
@@ -198,4 +198,4 @@ The following articles cover core pipeline setup. For all how-to guides, see the
 ## Next step
 
 > [!div class="nextstepaction"]
-> [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md)
\ No newline at end of file
+> [Quickstart: Agentic retrieval](search-get-started-agentic-retrieval.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索に関する概要ドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるエージェント検索の概要に関するドキュメントの小規模な更新を示しており、主に日付やAPIバージョンの更新、およびテキストの微調整が行われています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：重要な警告文が`2026-05-01-preview`から`2026-08-01-preview`に変更され、この新しいAPIバージョンの機能に関する情報が反映されています。

2. **テキストの明確化**：エージェント検索がどのように機能するかについての説明文が修正され、特に「エージェント検索が行うこと」と入力の内容を分かりやすくするための文体が改善されています。

3. **ユースケースの説明の強化**：エージェント検索がMicrosoft Foundryポータルにおいての役割に加え、AzureポータルやREST APIを通じたカスタムソリューションとしての可能性が強調されています。

4. **内容の整理と要約**：いくつかの箇所で記述が簡潔に整理され、より明瞭にエージェント検索のプロセス、構成要素、およびコストに関する説明が行われています。

5. **ユーザーガイドの強調**：効率的なコンテンツ整理や、LLM使用量を削減するための推奨事項に関する詳細が追加され、ユーザーがエージェント検索を最適化するための具体的な手段が提示されています。

このように、ドキュメント内の具体的な変更により、ユーザーはエージェント検索の使用に関する最新情報やベストプラクティスを把握しやすくなっています。全体として、この変更はAzure AI Searchの利用者にとって価値ある情報更新と言えるでしょう。

## articles/search/cognitive-search-skill-vision-vectorize.md{#item-386571}

<details>
<summary>Diff</summary>
````diff
@@ -56,7 +56,7 @@ Parameters are case sensitive.
 
 ## Skill inputs
 
-Skill definition inputs include name, source, and inputs. The following table provides valid values for name of the input. You can also specify recursive inputs. For more information, see the [REST API reference](/rest/api/searchservice/skillsets/create?view=rest-searchservice-2026-05-01-preview#inputfieldmappingentry&preserve-view=true) and [Create a skillset](cognitive-search-defining-skillset.md).
+Skill definition inputs include name, source, and inputs. The following table provides valid values for name of the input. You can also specify recursive inputs. For more information, see the [REST API reference](/rest/api/searchservice/skillsets/create?view=rest-searchservice-2026-08-01-preview#inputfieldmappingentry&preserve-view=true) and [Create a skillset](cognitive-search-defining-skillset.md).
 
 | Input	 | Description |
 |--------|-------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ビジョンスキルの入力パラメータに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure Cognitive Searchのビジョンスキルに関するドキュメントの小規模な更新を示しており、主にREST APIのバージョンに関する情報が修正されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：ドキュメント内のREST APIリファレンスのリンクが、`2026-05-01-preview`から`2026-08-01-preview`に更新されました。これにより、最新のAPI機能や仕様が反映されています。

2. **記述の整合性**：他の部分との整合性を持たせ、最新のバージョン情報を反映させるために小規模なテキスト修正が行われています。

このように、APIバージョンの更新は、ユーザーが最新の機能にアクセスできるようにし、正しい情報をもとにスキルを定義できるようにするために重要です。全体的に、この変更はドキュメントの正確性と最新性を向上させるためのものです。

## articles/search/enrichment-cache-how-to-configure.md{#item-b0ae0b}

<details>
<summary>Diff</summary>
````diff
@@ -79,12 +79,12 @@ In the indexer definition, set `cache` with:
 
 ### [**REST**](#tab/rest)
 
-If you're editing an existing indexer, use [GET Indexer](/rest/api/searchservice/indexers/get?view=rest-searchservice-2026-05-01-preview&preserve-view=true) to get the current configuration.
+If you're editing an existing indexer, use [GET Indexer](/rest/api/searchservice/indexers/get?view=rest-searchservice-2026-08-01-preview&preserve-view=true) to get the current configuration.
 
-1. Use the latest preview API for [Create or Update Indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true).
+1. Use the latest preview API for [Create or Update Indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true).
 
     ```http
-    PUT https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]?api-version=2026-05-01-preview
+    PUT https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]?api-version=2026-08-01-preview
         Content-Type: application/json
         api-key: [YOUR-ADMIN-KEY]
         {
@@ -107,7 +107,7 @@ If you're editing an existing indexer, use [GET Indexer](/rest/api/searchservice
 1. [Run the indexer](/rest/api/searchservice/indexers/run). This one-time full rebuild seeds the cache. After it's loaded, incremental reuse applies on subsequent runs.
 
     ```http
-    POST https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]/run?api-version=2026-05-01-preview
+    POST https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]/run?api-version=2026-08-01-preview
         Content-Type: application/json
         api-key: [YOUR-ADMIN-KEY]
     ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンリッチメントキャッシュ設定に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azureのエンリッチメントキャッシュの設定に関するドキュメントの小規模な更新を示しており、主にREST APIのバージョンに関する情報が修正されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：`2026-05-01-preview`から`2026-08-01-preview`へ、いくつかのAPIリファレンスリンクが更新されました。これにより、ユーザーが最新のAPI機能やその使用方法にアクセスできるようになっています。

2. **コマンド例の修正**：具体的なHTTPリクエストの例においても、APIバージョンが変更されたことが反映されており、それに伴い全体的な文脈が一貫性を持って更新されています。

この変更は、ユーザーが最新の設定方法に従ってエンリッチメントキャッシュを正しく構成できるようにするもので、正確性と最新性を維持するために重要です。全体的に、この更新はドキュメントの信頼性を高めるためのものです。

## articles/search/enrichment-cache-how-to-manage.md{#item-a972bd}

<details>
<summary>Diff</summary>
````diff
@@ -50,7 +50,7 @@ The cache is created when you specify the `cache` property and run the indexer.
 The following example illustrates an indexer with caching enabled. See [Configure enrichment caching](enrichment-cache-how-to-configure.md) for full instructions. 
 
 ```json
-POST https://[YOUR-SEARCH-SERVICE-NAME].search.windows.net/indexers?api-version=2026-05-01-preview
+POST https://[YOUR-SEARCH-SERVICE-NAME].search.windows.net/indexers?api-version=2026-08-01-preview
     {
         "name": "myIndexerName",
         "targetIndexName": "myIndex",
@@ -96,7 +96,7 @@ If you know that a change to the skill is superficial, override skill evaluation
 When you set this parameter, only updates to the skillset definition are committed. The change isn't evaluated for effects on the existing cache. Use a preview API version, 2020-06-30-Preview or later. Use the latest preview API.
 
 ```http
-PUT https://[servicename].search.windows.net/skillsets/[skillset name]?api-version=2026-05-01-preview&disableCacheReprocessingChangeDetection
+PUT https://[servicename].search.windows.net/skillsets/[skillset name]?api-version=2026-08-01-preview&disableCacheReprocessingChangeDetection
   
 ```
 
@@ -105,21 +105,21 @@ PUT https://[servicename].search.windows.net/skillsets/[skillset name]?api-versi
 Most changes to a data source definition invalidate the cache. However, for scenarios where you know that a change shouldn't invalidate the cache - such as changing a connection string or rotating the key on the storage account - append the `ignoreResetRequirement` parameter on the [data source update](/rest/api/searchservice/data-sources/create-or-update). Set this parameter to true to allow the commit to go through, without triggering a reset condition that would result in all objects being rebuilt and populated from scratch.
 
 ```http
-PUT https://[search service].search.windows.net/datasources/[data source name]?api-version=2026-05-01-preview&ignoreResetRequirement
+PUT https://[search service].search.windows.net/datasources/[data source name]?api-version=2026-08-01-preview&ignoreResetRequirement
  
 ```
 
 ### Force skillset evaluation
 
 The purpose of the cache is to avoid unnecessary processing. But suppose you make a change to a skill that the indexer doesn't detect (for example, changing something in external code, such as a custom skill).
 
-In this case, use the [Reset Skills](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2026-05-01-preview&preserve-view=true) API to force reprocessing of a particular skill, including any downstream skills that have a dependency on that skill's output. This API accepts a POST request with a list of skills that should be invalidated and marked for reprocessing. After Reset Skills, follow with a [Run Indexer](/rest/api/searchservice/indexers/run) request to invoke the pipeline processing.
+In this case, use the [Reset Skills](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2026-08-01-preview&preserve-view=true) API to force reprocessing of a particular skill, including any downstream skills that have a dependency on that skill's output. This API accepts a POST request with a list of skills that should be invalidated and marked for reprocessing. After Reset Skills, follow with a [Run Indexer](/rest/api/searchservice/indexers/run) request to invoke the pipeline processing.
 
 ## Re-cache specific documents
 
 If you [reset an indexer](/rest/api/searchservice/indexers/reset), all documents in the search corpus are reprocessed. 
 
-In scenarios where only a few documents need reprocessing, use [Reset Documents (preview)](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2026-05-01-preview&preserve-view=true) to force reprocessing of specific documents. When you reset a document, the indexer invalidates the cache for that document. The indexer then reprocesses the document by reading it from the data source. For more information, see [Run or reset indexers, skills, and documents](search-howto-run-reset-indexers.md).
+In scenarios where only a few documents need reprocessing, use [Reset Documents (preview)](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2026-08-01-preview&preserve-view=true) to force reprocessing of specific documents. When you reset a document, the indexer invalidates the cache for that document. The indexer then reprocesses the document by reading it from the data source. For more information, see [Run or reset indexers, skills, and documents](search-howto-run-reset-indexers.md).
 
 To reset specific documents, include a list of document keys as read from the search index in the request. If the key maps to a field in the external data source, use the value from the search index.
 
@@ -134,7 +134,7 @@ Depending on how you call the API, the request either appends, overwrites, or qu
 The following example illustrates a reset document request:
 
 ```http
-POST https://[search service name].search.windows.net/indexers/[indexer name]/resetdocs?api-version=2026-05-01-preview
+POST https://[search service name].search.windows.net/indexers/[indexer name]/resetdocs?api-version=2026-08-01-preview
     {
         "documentKeys" : [
             "key1",
@@ -185,10 +185,10 @@ Preview APIs provide extra properties on indexers. Use the latest preview API.
 
 Use the generally available version for skillsets and data sources. In addition to the reference documentation, see [Configure caching for incremental enrichment](enrichment-cache-how-to-configure.md) for details about order of operations.
 
-+ [Create or Update Indexer (api-version=2026-05-01-preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) 
++ [Create or Update Indexer (api-version=2026-08-01-preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
-+ [Reset Skills (api-version=2026-05-01-preview)](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
++ [Reset Skills (api-version=2026-08-01-preview)](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
-+ [Create or Update Skillset (api-version=2026-05-01-preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (New URI parameter on the request)
++ [Create or Update Skillset (api-version=2026-08-01-preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) (New URI parameter on the request)
 
-+ [Create or Update Data Source (api-version=2026-05-01-preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) When you call this API with a preview API version, it provides a new parameter named `ignoreResetRequirement`. Set this parameter to `true` when your update action shouldn't invalidate the cache. Use `ignoreResetRequirement` sparingly as it could lead to unintended inconsistency in your data that isn't easily detected.
++ [Create or Update Data Source (api-version=2026-08-01-preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) When you call this API with a preview API version, it provides a new parameter named `ignoreResetRequirement`. Set this parameter to `true` when your update action shouldn't invalidate the cache. Use `ignoreResetRequirement` sparingly as it could lead to unintended inconsistency in your data that isn't easily detected.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンリッチメントキャッシュ管理に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azureのエンリッチメントキャッシュ管理に関するドキュメントの小規模な更新を示しており、主にREST APIのバージョンの情報が修正されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：ドキュメント内の複数のAPIリファレンスリンクが、`2026-05-01-preview`から`2026-08-01-preview`に変更されました。これにより、最新のREST API機能や仕様の使用が促進され、ユーザーが新しい機能にアクセスできるようになります。

2. **具体的なリクエスト例の修正**：HTTPリクエストの例も、対応する新しいAPIバージョンに合わせて更新されており、正確な構文が維持されています。

3. **処理の効率化**：ドキュメントでは、特定の条件下でキャッシュを無効化せずにデータソースやスキルセットを更新するための新しいパラメータ `ignoreResetRequirement` について言及されています。このパラメータの使い方にも注意が促されています。

これらの更新は、ユーザーがエンリッチメントキャッシュを正しく管理し、最新の仕様に従って作業を行えるようにするためのもので、全体的にドキュメントの信頼性を高めるための重要な変更です。

## articles/search/get-started-portal-agentic-retrieval.md{#item-2bf1dc}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ The portal guides you through the process of creating the following objects:
 Afterwards, you test the knowledge base by submitting a complex query that requires information from multiple documents and reviewing the synthesized answer.
 
 > [!IMPORTANT]
-> Some agentic retrieval features are generally available in the 2026-04-01 REST API through programmatic access. The Azure portal continues to use 2026-05-01-preview for the full feature set. If you previously created agentic retrieval objects in the portal, those objects might be subject to breaking changes. For migration guidance, see [Migrate agentic retrieval code to the latest version](agentic-retrieval-how-to-migrate.md).
+> Some agentic retrieval features are generally available in the 2026-04-01 REST API through programmatic access. The Azure portal continues to use 2026-08-01-preview for the full feature set. If you previously created agentic retrieval objects in the portal, those objects might be subject to breaking changes. For migration guidance, see [Migrate agentic retrieval code to the latest version](agentic-retrieval-how-to-migrate.md).
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルに関するAPIバージョンの更新"
}
```

### Explanation
この変更は、Azureポータルにおけるエージェンティックリトリーバル機能に関連するAPIバージョンの更新を示す小規模な更新です。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：エージェンティックリトリーバル機能が利用可能なREST APIのバージョンが、`2026-05-01-preview`から`2026-08-01-preview`に更新されました。これにより、ユーザーは最新の機能セットに基づいて操作を行うことができます。

2. **重要な通知**：ドキュメント内の重要な注意喚起には、エージェンティックリトリーバルオブジェクトをポータルで以前に作成したユーザーに対する、破壊的変更の可能性についての記述が含まれており、最新のバージョンへの移行ガイダンスも提供されています。

全体として、この変更はユーザーが最新のAPIを利用し、エージェンティックリトリーバル機能に関する最適な体験を得るための重要なアップデートです。

## articles/search/hybrid-search-how-to-query.md{#item-345ce6}

<details>
<summary>Diff</summary>
````diff
@@ -311,12 +311,12 @@ If you use `maxTextRecallSize`, you might also want to set `countAndFacetMode`.
 
 With the default `countAllResults` mode, counts and facets can include text-side documents that aren't retrieved for RRF ranking because they fall outside the `maxTextRecallSize` window. Increasing `maxTextRecallSize` increases the number of BM25-ranked documents available for ranking, but doesn't increase the vector contribution beyond `k`. Use `countRetrievableResults` if you want count and facet calculations scoped to the documents retrieved for hybrid ranking.
 
-We recommend the [latest preview REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) for setting these options.
+We recommend the [latest preview REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true) for setting these options.
 
 > [!TIP]
 > Another approach for hybrid query tuning is [vector weighting](vector-search-how-to-query.md#vector-weighting), used to increase the importance of vector queries in the request.
 
-1. Use [Search - POST (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or [Search - GET (preview)](/rest/api/searchservice/documents/search-get?view=rest-searchservice-2026-05-01-preview&preserve-view=true) to specify preview parameters.
+1. Use [Search - POST (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true) or [Search - GET (preview)](/rest/api/searchservice/documents/search-get?view=rest-searchservice-2026-08-01-preview&preserve-view=true) to specify preview parameters.
 
 1. Add a `hybridSearch` query parameter object to set the maximum number of documents recalled through the BM25-ranked results of a hybrid query. It has two properties:
 
@@ -335,7 +335,7 @@ The following REST examples show two use-cases for setting `maxTextRecallSize`.
 The first example reduces `maxTextRecallSize` to 100, limiting the text side of the hybrid query to just 100 documents. It also sets `countAndFacetMode` to include only retrievable documents in count and facet calculations.
 
 ```http
-POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?api-version=2026-05-01-preview 
+POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?api-version=2026-08-01-preview
 
     { 
       "vectorQueries": [ 
@@ -357,7 +357,7 @@ POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?
 The second example raises `maxTextRecallSize` to 5,000. It also uses top, skip, and next to pull results from large result sets. In this case, the request pulls in BM25-ranked results starting at position 1,500 through 2,000 as the text query contribution to the RRF composite result set.
 
 ```http
-POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?api-version=2026-05-01-preview 
+POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?api-version=2026-08-01-preview
 
     { 
       "vectorQueries": [ 
@@ -427,22 +427,22 @@ api-key: {{admin-api-key}}
 
 ### Example: Hybrid search with filters targeting vector subqueries (preview)
 
-Using the [latest preview REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true), you can override a global filter on the search request by applying a secondary filter that targets just the vector subqueries in a hybrid request.
+Using the [latest preview REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true), you can override a global filter on the search request by applying a secondary filter that targets just the vector subqueries in a hybrid request.
 
 This feature provides fine-grained control by ensuring that filters only influence the vector search results, leaving keyword-based search results unaffected. 
 
 The targeted filter fully overrides the global filter, including any filters used for [security trimming](search-security-trimming-for-azure-search.md) or geospatial search.  In cases where global filters are required, such as security trimming, you must explicitly include these filters in both the top-level filter and in each vector-level filter to ensure security and other constraints are consistently enforced.
 
 To apply targeted vector filters:
 
-+ Use the [latest preview Search Documents REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true#request-body) or an Azure SDK beta package that provides the feature.
++ Use the [latest preview Search Documents REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true#request-body) or an Azure SDK beta package that provides the feature.
 
 + Modify a query request, adding a new `vectorQueries.filterOverride` parameter set to an [OData filter expression](search-query-odata-filter.md).
 
 Here's an example of hybrid query that adds a filter override. The global filter "Rating gt 3" is replaced at run time by the `filterOverride`.
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2026-05-01-preview
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2026-08-01-preview
 
 {
     "vectorQueries": [
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索のクエリ設定に関するAPIバージョンの更新"
}
```

### Explanation
この変更は、Azureのハイブリッド検索に関するドキュメントの小規模な更新を示しており、主に使用されるREST APIのバージョンの情報が修正されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：各所で参照されているREST APIのバージョンが、`2026-05-01-preview`から`2026-08-01-preview`に変更されました。この更新により、ユーザーは最新版の機能とオプションにアクセスできます。

2. **クエリパラメータに関する設定**：ハイブリッド検索のためのクエリ設定の推奨事項や具体的なリクエスト例が含まれており、最新のAPIバージョンを使用することが強調されています。

3. **ハイブリッド検索のチューニング**：ドキュメントでは、ベクトルクエリの重要性を高める手法や、フィルターの適用方法について説明されており、ユーザーがハイブリッド検索をより効果的に利用できるように指導しています。

全体として、この変更はハイブリッド検索での最新のAPI機能を利用するために必要な情報を提供し、ユーザーが効果的にクエリを設定し、実行できるよう支援する内容となっています。

## articles/search/includes/billing-split-version-compatibility.md{#item-c08436}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,6 @@ ms.date: 04/24/2026
 You set billing consent using the Search Management REST API. The following table shows which property takes effect based on the Search Service REST API version your application uses.
 
 | Search Service REST API version | Semantic ranker billing | Agentic retrieval billing |
-|---|---|---|
+| --- | --- | --- |
 | [2026-04-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true) and later | Controlled by `semanticSearch` | Controlled by `knowledgeRetrieval` |
 | [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) and earlier | Controlled by `semanticSearch` | Controlled by `semanticSearch` |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "請求とセマンティックランカーの課金に関する表の整形修正"
}
```

### Explanation
この変更は、Azure検索サービスにおける請求とバージョンの互換性に関するドキュメントの小規模な更新を示します。

主な変更点は以下の通りです：

1. **表のフォーマット修正**：課金のルールに関する表の形式がわずかに修正され、線の形状が変更されています。これにより、情報の視認性が向上し、読みやすさが改善されています。

2. **情報の要約**：表の中では、異なるSearch Service REST APIバージョンに基づくセマンティックランカーとエージェンティックリトリーバルの課金の管理方法が明記されています。具体的には、`2026-04-01`以降のバージョンでは、セマンティック検索によって課金が制御される一方で、`2025-11-01-preview`以前のバージョンでは、両方の機能がセマンティック検索に依存することが示されています。

この変更は、ユーザーが異なるAPIバージョンにおける課金の管理方法を明確に理解できるようにするためのものです。

## articles/search/includes/how-tos/knowledge-source-private-network.md{#item-41c52f}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,18 @@
+---
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 08/14/2026
+ai-usage: ai-assisted
+---
+
+1. Complete the [private network prerequisites](#prerequisites).
+
+1. Set `networkAccessMode` to `private` in the knowledge source creation request. You can only set this property during creation. To change it later, delete and recreate the knowledge source.
+
+   Creation can fail if the service tier or runtime doesn't support private execution or if a required shared private link doesn't exist.
+
+1. Confirm that the generated indexer's `executionEnvironment` is `private`.
+
+1. Confirm that each required shared private link is approved and targets the correct dependency. Successful creation alone doesn't confirm link approval or targeting.
+
+1. Poll the knowledge source status until `lastSynchronizationState.endTime` has a value. Confirm that `itemsUpdatesFailed` is `0`, and then verify the connector-specific source content. Synchronization fails if a dependency isn't reachable.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "プライベートネットワーク向けの新しい知識ソース設定手順"
}
```

### Explanation
この変更は、AzureのAI検索サービスにおいてプライベートネットワーク向けの知識ソースの設定手順に関する新しいガイドラインを追加したものです。

主な内容は以下の通りです：

1. **新しいコンテンツの追加**：この記事では、プライベートネットワークの知識ソースを設定するための具体的な手順が記述されています。合計で18行が追加され、ユーザーが知識ソースの作成プロセスを理解するために必要な情報が提供されています。

2. **手順の詳細**：
   - プライベートネットワークの前提条件を確認するステップ。
   - 知識ソースの作成リクエストにおいて、`networkAccessMode` プロパティを `private` に設定する必要があることが説明されています。このプロパティは作成時にのみ設定可能で、後から変更する場合はソースを削除して再作成する必要があることが強調されています。
   - 作成されたインデクサーの `executionEnvironment` が `private` であるか確認すること。
   - 必要な共有プライベートリンクが承認され、正しい依存先をターゲットにしていることを確認する必要があること。
   - 知識ソースのステータスをポーリングし、`lastSynchronizationState.endTime` に値があることを確認し、`itemsUpdatesFailed` が0であることを確認する手順が含まれています。

この新しいガイドラインは、ユーザーがプライベートネットワークにおける知識ソースを正しく設定し、運用するための重要な手助けとなるものです。

## articles/search/includes/previews/agentic-retrieval-preview-api-usage.md{#item-2442de}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
 title: Agentic Retrieval Preview API Usage
-description: Note for articles that use the 2026-05-01-preview REST API to demonstrate the full agentic retrieval feature set, including features that remain in preview.
+description: Note for articles that use the 2026-08-01-preview REST API to demonstrate the full agentic retrieval feature set, including features that remain in preview.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
@@ -9,4 +9,4 @@ ms.date: 04/16/2026
 ---
 
 > [!NOTE]
-> Some agentic retrieval features are generally available in the 2026-04-01 REST API. However, this article uses the 2026-05-01-preview to demonstrate the full feature set, including features that remain in preview. Preview features are provided without a service-level agreement and aren't recommended for production workloads. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> Some agentic retrieval features are generally available in the 2026-04-01 REST API. However, this article uses the 2026-08-01-preview to demonstrate the full feature set, including features that remain in preview. Preview features are provided without a service-level agreement and aren't recommended for production workloads. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルプレビューAPIに関する日付の更新"
}
```

### Explanation
この変更は、エージェンティックリトリーバルプレビューAPIに関するドキュメントの小規模な更新を示しています。具体的には、使用されているREST APIのバージョンの更新が行われました。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：元々は2026-05-01-preview REST APIが使用されていましたが、これが2026-08-01-preview REST APIに変更されました。この更新により、最新の機能や修正が反映されることが期待されます。

2. **記述内容の一貫性**：ノートの部分についても同様に、使用するAPIのバージョンが更新されています。具体的には、2026-04-01 REST APIにおける一般的なエージェンティックリトリーバル機能が言及され、プレビュー機能が引き続き提供されることが強調されている点はそのまま保たれています。

この変更により、ユーザーは最新のAPIバージョンを参照することができ、エージェンティックリトリーバル機能の完全なセットを正確に理解できるようになります。

## articles/search/includes/quickstarts/agentic-retrieval-java.md{#item-4e2c55}

<details>
<summary>Diff</summary>
````diff
@@ -37,10 +37,6 @@ Although you can use your own data, this quickstart uses [sample JSON documents]
 
 [!INCLUDE [agentic retrieval setup](agentic-retrieval-setup.md)]
 
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
-
 ## Set up the environment
 
 1. Use Git to clone the sample repository.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルJavaクイックスタートからの不要な情報の削除"
}
```

### Explanation
この変更は、エージェンティックリトリーバルに関するJavaクイックスタートのドキュメントから不要な情報を削除したことを示しています。具体的には、アクセス権限やAPIバージョンに関する記述が削除されました。

主な変更点は以下の通りです：

1. **アクセス権限の説明を削除**：オブジェクトをAzure AI Search上で作成し使用するための権限に関する情報が削除されました。以前のバージョンでは、役割ベースのアクセスやAPIキーの使用に関連する情報が提供されていましたが、これが不要と判断されたため、削除されました。

2. **APIバージョンの記述を削除**：使用される検索サービスのREST APIバージョン（2026-05-01-preview）に関する記述も削除されました。この変更により、ドキュメントはよりすっきりとしたものになり、ユーザーにとっての重要な設定手順に焦点を合わせやすくなります。

この修正により、クイックスタートがより簡潔になり、ユーザーが必要な手順に集中しやすくなっています。また、関連情報の整理により、ドキュメント全体の可読性が向上しています。

## articles/search/includes/quickstarts/agentic-retrieval-javascript.md{#item-715283}

<details>
<summary>Diff</summary>
````diff
@@ -37,10 +37,6 @@ Although you can use your own data, this quickstart uses [sample JSON documents]
 
 [!INCLUDE [agentic retrieval setup](agentic-retrieval-setup.md)]
 
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
-
 ## Set up the environment
 
 1. Use Git to clone the sample repository.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルJavaScriptクイックスタートからの不要な情報の削除"
}
```

### Explanation
この変更は、エージェンティックリトリーバルに関するJavaScriptクイックスタートのドキュメントから不要な情報を削除したことを示しています。主に、アクセス権限や使用されるAPIバージョンに関する記述が削除されました。

主な変更点は以下の通りです：

1. **アクセス権限の説明の削除**：Azure AI Search上でオブジェクトを作成し使用するための権限に関する情報が削除されました。具体的には、役割ベースのアクセスやAPIキーの使用に関連する以前の言及がなくなり、この部分が簡潔になりました。

2. **APIバージョンの記述の削除**：使用される検索サービスのREST APIバージョン（2026-05-01-preview）に関する説明も、ドキュメントから削除されました。これにより、ユーザーはクイックスタートの主要な内容に集中できるようになり、冗長な情報が排除されています。

この修正により、クイックスタートはさらにシンプルで明確になり、ユーザーが必要な手順に注力しやすくなっています。また、ドキュメント全体の可読性が向上し、利用者にとって使いやすいものとなりました。

## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -39,10 +39,6 @@ Although you can use your own data, this quickstart uses [sample JSON documents]
 
 [!INCLUDE [agentic retrieval setup](agentic-retrieval-setup.md)]
 
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
-
 ## Set up the environment
 
 1. Use Git to clone the sample repository.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルPythonクイックスタートからの不要な情報の削除"
}
```

### Explanation
この変更は、エージェンティックリトリーバルに関するPythonクイックスタートのドキュメントから、不要な情報を削除したことを示しています。具体的には、アクセス権限やAPIバージョンに関する説明が削除されました。

主な変更点は以下の通りです：

1. **アクセス権限に関する記述の削除**：Azure AI Search上でオブジェクトを作成し使用するための権限に関する情報が削除されました。これには、役割ベースのアクセスやAPIキーの使用に関連する項目が含まれており、その説明が省かれました。

2. **APIバージョンに関する説明の削除**：使用される検索サービスのREST APIバージョン（2026-05-01-preview）に関する記述も削除され、ユーザーに対する混乱が軽減されました。

これにより、クイックスタートはよりすっきりとし、ユーザーが重点を置くべき手順に集中しやすくなっています。また、ドキュメント全体の可読性の向上にも寄与し、より使いやすいものとなっています。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

<details>
<summary>Diff</summary>
````diff
@@ -326,7 +326,7 @@ Authorization: Bearer {{token}}
 }
 ```
 
-**Reference:** [Knowledge Sources - Create](/rest/api/searchservice/knowledge-sources/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Sources - Create](/rest/api/searchservice/knowledge-sources/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ### Create a knowledge base
 
@@ -362,7 +362,7 @@ Authorization: Bearer {{token}}
 }
 ```
 
-**Reference:** [Knowledge Bases - Create](/rest/api/searchservice/knowledge-bases/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Bases - Create](/rest/api/searchservice/knowledge-bases/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 ### Run the retrieval pipeline
 
@@ -407,7 +407,7 @@ Authorization: Bearer {{token}}
 }
 ```
 
-**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Knowledge Retrieval - Retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 The output contains the following components:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルRESTクイックスタートのAPIバージョンの更新"
}
```

### Explanation
この変更は、エージェンティックリトリーバルに関するRESTクイックスタートのドキュメントにおいて、APIのバージョンを更新したことを示しています。具体的には、複数の場所で使用されているAPIエンドポイントのバージョンが、旧版の「2026-05-01-preview」から新しい「2026-08-01-preview」に変更されました。

主な変更点は以下の通りです：

1. **参照の更新**：以下の三つのセクションにおいて、APIの参照リンクが古いバージョンから新しいバージョンに更新されました。
   - 知識ソースの作成（Knowledge Sources - Create）
   - 知識ベースの作成（Knowledge Bases - Create）
   - 知識取得の実行（Knowledge Retrieval - Retrieve）

この更新により、ユーザーは最新のAPI仕様に基づいた正確な情報を得ることができ、より適切な利用が可能となります。また、ドキュメントの整合性が保たれ、今後の開発や利用における混乱を避けることに寄与しています。

## articles/search/includes/quickstarts/agentic-retrieval-typescript.md{#item-e6370b}

<details>
<summary>Diff</summary>
````diff
@@ -39,10 +39,6 @@ Although you can use your own data, this quickstart uses [sample JSON documents]
 
 [!INCLUDE [agentic retrieval setup](agentic-retrieval-setup.md)]
 
-+ Permission to create and use objects on Azure AI Search. We recommend [role-based access](../../search-security-rbac.md), but you can use [API keys](../../search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](../../search-get-started-rbac.md).
-
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
-
 ## Set up the environment
 
 1. Use Git to clone the sample repository.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルTypeScriptクイックスタートからの不要な情報の削除"
}
```

### Explanation
この変更は、エージェンティックリトリーバルに関するTypeScriptクイックスタートのドキュメントから、不要な情報を削除したことを示しています。具体的には、アクセス権限およびAPIバージョンに関する記述が削除されました。

主な変更点は以下の通りです：

1. **アクセス権限に関する記述の削除**：Azure AI Search上でオブジェクトを作成し使用するための権限に関する情報が削除されました。この情報には、役割ベースのアクセスやAPIキーに関する推奨事項が含まれていました。

2. **APIバージョンに関する説明の削除**：使用される検索サービスのREST APIバージョン（2026-05-01-preview）に関する記述も削除され、ユーザーに対する混乱が軽減されました。

これにより、クイックスタートはよりシンプルになり、ユーザーが手順に集中しやすくなりました。また、文書全体の可読性も向上し、利用の際の便宜が図られています。

## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -453,15 +453,15 @@ The `boostGenre` profile uses weighted text fields, boosting matches found in al
 ## Example: function aggregation
 
 > [!NOTE]
-> This capability is currently in preview, available through the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) and in Azure SDK preview packages that provide the feature.
+> This capability is currently in preview, available through the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) and in Azure SDK preview packages that provide the feature.
 
 Within a single scoring profile, you can specify multiple scoring functions, and then set `"functionAggregation": "product"`. Documents that score highly across all functions are prioritized, while those that score weak in one or more fields are suppressed.
 
 In this example, create a scoring profile that includes two boosting functions that boost by `rating` and `baseRate`, and then set `functionAggregation` to `product`.
 
 ```http
 ### Create a new index
-PUT {{url}}/indexes/hotels-scoring?api-version=2026-05-01-preview
+PUT {{url}}/indexes/hotels-scoring?api-version=2026-08-01-preview
 Content-Type: application/json
 api-key: {{key}}
 
@@ -524,7 +524,7 @@ This next request loads the index with searchable content that tests the profile
 
 ```http
 ### Upload documents to the index
-POST {{url}}/indexes/hotels-scoring/docs/index?api-version=2026-05-01-preview
+POST {{url}}/indexes/hotels-scoring/docs/index?api-version=2026-08-01-preview
 Content-Type: application/json
 api-key: {{key}}
 
@@ -613,7 +613,7 @@ Run a query that uses the criteria in the scoring profile to boost results based
 
 ```http
 ### Search with boost
-POST {{url}}/indexes/hotels-scoring/docs/search?api-version=2026-05-01-preview
+POST {{url}}/indexes/hotels-scoring/docs/search?api-version=2026-08-01-preview
 Content-Type: application/json
 api-key: {{key}}
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリングプロファイルに関するAPIバージョンの更新"
}
```

### Explanation
この変更は、スコアリングプロファイルに関するドキュメントの中で、使用されるAPIバージョンを最新のものに更新することで、より正確で最新の情報を提供しています。具体的には、いくつかのAPIエンドポイントのバージョンが「2026-05-01-preview」から「2026-08-01-preview」に変更されました。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：スコアリングプロファイルの例や関連するHTTPリクエストにおいて、すべて「2026-05-01-preview」から「2026-08-01-preview」に変更されました。これにより、ユーザーは最新のAPI仕様に基づいた機能を利用できるようになります。

2. **例の明確化**：スコアリングプロファイルの作成やドキュメントのアップロード、検索に関する各リクエストの具体的な例が、最新のバージョンに正確に適合する形に整えられています。これにより、ユーザーがこれらの手順を実行する際の信頼性が向上します。

この更新により、文書全体の整合性が保たれ、ユーザーは最新の機能やサービスを最大限に活用できるようになります。

## articles/search/index-similarity-and-scoring.md{#item-75603d}

<details>
<summary>Diff</summary>
````diff
@@ -136,7 +136,7 @@ In Azure AI Search, for keyword search and the text portion of a hybrid query, y
 > [!NOTE]
 > The `featuresMode` parameter isn't documented in the REST APIs, but you can use it on a preview REST API call to Search Documents for text (Keyword) search that's BM25-ranked.
 
-[Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) requests support a `featuresMode` parameter that provides more detail about a BM25 relevance score at the field level. Whereas the `@searchScore` is calculated for the document all-up (how relevant is this document in the context of this query), featuresMode reveals information about individual fields, as expressed in a `@search.features` structure. The structure contains all fields used in the query (either specific fields through **searchFields** in a query, or all fields attributed as **searchable** in an index).
+[Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true) requests support a `featuresMode` parameter that provides more detail about a BM25 relevance score at the field level. Whereas the `@searchScore` is calculated for the document all-up (how relevant is this document in the context of this query), featuresMode reveals information about individual fields, as expressed in a `@search.features` structure. The structure contains all fields used in the query (either specific fields through **searchFields** in a query, or all fields attributed as **searchable** in an index).
 
 Valid values for featuresMode:
 
@@ -154,7 +154,7 @@ This parameter is especially useful when you're trying to understand why certain
 For a query that targets a "description" field, a request might look like this:
 
 ```http
-POST {{baseUrl}}/indexes/hotels-sample/docs/search?api-version=2026-05-01-preview  HTTP/1.1
+POST {{baseUrl}}/indexes/hotels-sample/docs/search?api-version=2026-08-01-preview  HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer {{accessToken}}
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "BM25スコアリングに関するAPIバージョンの更新"
}
```

### Explanation
この変更は、BM25スコアリングの詳細を提供する`featuresMode`パラメータに関するドキュメント内のAPIバージョンを更新することで、正確な情報を提供することを目的としています。具体的には、`featuresMode`に関連するリクエストのAPIバージョンが「2026-05-01-preview」から「2026-08-01-preview」に変更されました。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：検索ドキュメントに関するリクエストの例で、使用されるAPIバージョンが最新のものに更新されました。これにより、ユーザーは最新の機能や改善点にアクセスできるようになります。

2. **`featuresMode`の説明**：`featuresMode`パラメータはBM25の関連スコアをフィールドレベルで詳細に示すものであることが説明されており、`@searchScore`との相違点が明確に説明されています。これにより、ユーザーが各フィールドの関連性を理解しやすくなります。

この変更により、ドキュメントの整合性が保たれ、ユーザーはAPIの最新の利用法を正しく理解し、自身のアプリケーションでの適用を円滑に行えるようになります。

## articles/search/search-api-migration.md{#item-07297b}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: upgrade-and-migration-article
-ms.date: 06/11/2026
+ms.date: 08/31/2026
 ---
 
 # Upgrade to the latest REST API in Azure AI Search
@@ -22,7 +22,7 @@ Here are the most recent versions of the REST APIs:
 | Targeted operations | REST API | Status |
 |---------------------|----------|--------|
 | Data plane | [`2026-04-01`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true) | Stable |
-| Data plane | [`2026-05-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) | Preview |
+| Data plane | [`2026-08-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) | Preview |
 | Control plane | [`2025-05-01`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2025-05-01&preserve-view=true) | Stable |
 | Control plane | [`2026-03-01-preview`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) | Preview |
 
@@ -103,6 +103,18 @@ See [Migrate from preview version](semantic-code-migration.md) to transition you
 
 Upgrade guidance assumes upgrade from the most recent previous version. If your code is based on an old API version, we recommend upgrading through each successive version to get to the newest version.
 
+### Upgrade to 2026-08-01-preview
+
+[`2026-08-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) adds new agentic retrieval controls, knowledge source enhancements, and cursor pagination for list operations.
+
+Before you upgrade, check whether any of the following `2026-08-01-preview` breaking changes apply to your code:
+
++ Agentic retrieval breaking changes include nested `model` objects in activity logs, `resultsProcessing` replacing `inclusionMode` for server tools in MCP knowledge source, and customer-owned Microsoft Entra app authentication for Work IQ knowledge sources. For step-by-step migration guidance, see [Migrate your agentic retrieval code](agentic-retrieval-how-to-migrate.md#2026-08-01-preview).
+
++ List operations for data sources, indexers, indexes, skillsets, and knowledge sources replace `$top`, `$skip`, and `$count` with cursor pagination using `pageSize`, `search`, and `@odata.nextLink`. For more information about the new paging mechanism, see [Page through Azure AI Search list results (preview)](search-how-to-page-list-results.md).
+
+For all other existing APIs, there are no behavior changes. You can swap in the new API version, and your code runs the same as before.
+
 ### Upgrade to 2026-05-01-preview
 
 [`2026-05-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) adds new knowledge source types, new parameters on the retrieve action, new SharePoint indexer content types and ACL options, and other capabilities.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新のREST APIへのアップグレードに関する情報の更新"
}
```

### Explanation
この変更は、Azure AI Searchの最新REST APIへのアップグレードに関するドキュメントの情報を更新し、新しいAPIバージョンや機能の追加を反映させています。具体的には、APIバージョンの更新や新機能の説明が追加されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：リストされたAPIバージョンの一つが「2026-05-01-preview」から「2026-08-01-preview」に更新され、最新のプレビューAPIに関する詳細情報が提供されています。

2. **新機能の追加**：新しいAPIバージョン「2026-08-01-preview」に追加された機能として、エージェント型の取得制御、知識ソースの拡張、およびリスト操作のためのカーソルページネーションが示されています。これにより、ユーザーは新機能の利用を検討できるようになります。

3. **移行ガイダンスの強化**：新しいAPIにアップグレードする際の注意点として、エージェント型取得に関連するブレイキング変更や、リスト操作におけるページネーションの新しいメカニズムが説明されています。これにより、ユーザーがスムーズにアップグレードできるようサポートします。

これらの変更により、ユーザーは最新のAPI機能を適切に理解し、自身のコードを最新バージョンに適合させやすくなるため、全体的な開発体験が向上します。

## articles/search/search-blob-indexer-role-based-access.md{#item-887e42}

<details>
<summary>Diff</summary>
````diff
@@ -17,11 +17,11 @@ ai-usage: ai-assisted
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -108,7 +108,7 @@ Key points about the configuration that make it work for this scenario:
 ```http
 # Create / Update Azure Blob Knowledge Source
 ###
-PUT {{url}}/knowledgesources/azure-blob-ks?api-version=2026-05-01-preview
+PUT {{url}}/knowledgesources/azure-blob-ks?api-version=2026-08-01-preview
 api-key: {{key}}
 Content-Type: application/json
  
@@ -146,7 +146,7 @@ Content-Type: application/json
 }
 ```
 
-**Reference:** [Create or Update Knowledge Source](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (REST API)
+**Reference:** [Create or Update Knowledge Source](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) (REST API)
 
 ## Configure indexer-based indexing
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Blob Indexerに関するAPIバージョンの更新"
}
```

### Explanation
この変更は、Azure Blob Indexerに関連するドキュメントのAPIバージョンを更新し、新機能や重要な情報を最新の内容に反映させるために行われました。主な更新点として、APIバージョン「2026-05-01-preview」から「2026-08-01-preview」への変更が含まれています。

具体的な変更点は以下の通りです：

1. **APIバージョンの更新**：ドキュメント内のすべての場所で、使用されるAPIバージョンが「2026-05-01-preview」から「2026-08-01-preview」に変更されています。これにより、ユーザーは最新のAPI機能にアクセスできるようになります。

2. **機能とライセンスについての情報の更新**：新しいAPIバージョンに関する特徴や機能が適切に更新されており、ユーザーが利用する際のライセンス条件に関する記述も最新のものに修正されています。

3. **アクセス権限に関する注意点**：新しいAPIバージョン「2026-08-01-preview」にも、外部で設定されたアクセス権限を変更できないことや、アクセス制限されたコンテンツにおけるタイミングラグの発生についての注意が記載されています。この情報は、ユーザーに安全かつ適切にAPIを使用するためのガイダンスを提供します。

これらの変更により、ドキュメントは最新の情報を提供し、ユーザーがAzure Blob Indexerを利用する際に必要な理解を深める助けとなります。

## articles/search/search-document-level-access-overview.md{#item-4bb055}

<details>
<summary>Diff</summary>
````diff
@@ -16,11 +16,11 @@ ai-usage: ai-assisted
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag occurs before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag occurs before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data flows outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -76,10 +76,10 @@ Azure Data Lake Storage (ADLS) Gen2 containers support ACLs on the container and
 For ACL-secured content, use group access over individual user access for ease of management. The pattern includes the following components:
 
 - Start with documents or files that have ACL assignments.
-- [Enable permission filters](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true#searchindexpermissionfilteroption) in the index.
-- [Add a permission filter](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true#permissionfilter) to a string field in an index.
+- [Enable permission filters](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true#searchindexpermissionfilteroption) in the index.
+- [Add a permission filter](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true#permissionfilter) to a string field in an index.
 - Load the index with source documents having associated ACLs.
-- Query the index, adding [`x-ms-query-source-authorization`](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true#request-headers) in the request header.
+- Query the index, adding [`x-ms-query-source-authorization`](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true#request-headers) in the request header.
 
 Your client app receives read permissions to the index through **Search Index Data Reader** or **Search Index Data Contributor** role. Access at query time is determined by user or group permission metadata in the indexed content. Queries that include a permission filter pass a user or group token as `x-ms-query-source-authorization` in the request header. When you use permission filters at query time, Azure AI Search checks for two things:
 
@@ -97,7 +97,7 @@ How you retrieve ACL permissions varies depending on whether you're pushing a do
 
 Start with a preview API that provides the feature:
 
-- [2026-05-01-preview REST API](/rest/api/searchservice/documents/?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+- [2026-08-01-preview REST API](/rest/api/searchservice/documents/?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 - [Azure SDK for Python prerelease package](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md). Check the changelog for the latest preview version that supports ACL and RBAC scope ingestion.
 - [Azure SDK for .NET prerelease package](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md). Check the changelog for the latest preview version that supports ACL and RBAC scope ingestion.
 - [Azure SDK for Java prerelease package](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md). Check the changelog for the latest preview version that supports ACL and RBAC scope ingestion.
@@ -106,18 +106,18 @@ For the [push model approach](search-index-access-control-lists-and-rbac-push-ap
 
 1. Confirm that your index schema is created with a preview or prerelease SDK and that the schema has permission filters.
 1. Consider using the Microsoft Graph SDK to get group or user identities.
-1. Use the [Index Documents](/rest/api/searchservice/documents/?view=rest-searchservice-2026-05-01-preview&preserve-view=true#indexdocumentsresult) or equivalent Azure SDK API to push documents and their associated permission metadata into the search index. 
+1. Use the [Index Documents](/rest/api/searchservice/documents/?view=rest-searchservice-2026-08-01-preview&preserve-view=true#indexdocumentsresult) or equivalent Azure SDK API to push documents and their associated permission metadata into the search index.
 
 For the [pull model ADLS Gen2 indexer approach](search-indexer-access-control-lists-and-role-based-access.md) or [Blob (ADLS Gen2) knowledge source](agentic-knowledge-source-how-to-blob.md):
 
 1. Verify that files in the directory are secured using the [ADLS Gen2 access control model](/azure/storage/blobs/data-lake-storage-access-control-model).
-1. Use [Indexers - Create](/rest/api/searchservice/indexers/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (REST API), [Knowledge Sources - Create](/rest/api/searchservice/knowledge-sources/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (REST API), or an equivalent Azure SDK API to create the indexer, index, and data source.
+1. Use [Indexers - Create](/rest/api/searchservice/indexers/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true) (REST API), [Knowledge Sources - Create](/rest/api/searchservice/knowledge-sources/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true) (REST API), or an equivalent Azure SDK API to create the indexer, index, and data source.
 
 If your skillset chunks documents, such as with the Text Split skill for integrated vectorization, the permission metadata fields move from indexer field mappings to index projections. See [Choose where to populate ACL fields](search-indexer-sharepoint-access-control-lists.md#choose-where-to-populate-acl-fields).
 
 ## Pattern for SharePoint in Microsoft 365 basic ACL permissions ingestion (preview)
 
-For indexed SharePoint content, Azure AI Search can store source permissions as metadata and use them to filter query results. You can access this capability in preview through the SharePoint in Microsoft 365 indexer and the `2026-05-01-preview` REST API or an equivalent preview SDK package.
+For indexed SharePoint content, Azure AI Search can store source permissions as metadata and use them to filter query results. You can access this capability in preview through the SharePoint in Microsoft 365 indexer and the latest REST API or an equivalent preview SDK package.
 
 For permission requirements, supported group relationships, permission synchronization, and limitations, see [Use a SharePoint indexer to ingest permission metadata](search-indexer-sharepoint-access-control-lists.md).
 
@@ -131,7 +131,7 @@ At query time, Azure AI Search checks each document's sensitivity label, the use
 
 This pattern includes the following components:
 
-- Configure your [index](/rest/api/searchservice/indexes/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true), [data source](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true), and [indexer](/rest/api/searchservice/indexers/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (for scheduling purposes) by using the 2026-05-01-preview REST API or a corresponding SDK that supports Purview label ingestion.
+- Configure your [index](/rest/api/searchservice/indexes/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true), [data source](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true), and [indexer](/rest/api/searchservice/indexers/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true) (for scheduling purposes) by using the latest preview REST API or a preview SDK that supports Purview label ingestion.
 - Enable a [system-assigned managed identity](search-how-to-managed-identities.md) on your search service. User-assigned managed identities aren't supported for Purview label extraction - the service's own identity must hold the elevated Purview permissions. Then have your tenant global administrator or privileged role administrator [grant the required access](search-indexer-sensitivity-labels.md#3-grant-access-to-extract-sensitivity-labels) to allow the search service to authenticate with Microsoft Purview and extract label metadata.
 - Apply sensitivity labels to documents before indexing so the system can recognize and preserve them during ingestion.
 - At query time, attach a valid Microsoft Entra token via the header `x-ms-query-source-authorization` to each query request. Azure AI Search evaluates the token and the associated label metadata to enforce label-based access control.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレベルのアクセス制御に関するAPIバージョンの更新"
}
```

### Explanation
この変更は、Azureのドキュメントレベルアクセス制御に関連する記事の内容を更新し、新しいAPIバージョンに適応させることを目的としています。具体的には、APIバージョンを「2026-05-01-preview」から「2026-08-01-preview」に変更し、関連する機能やライセンスについての記述も最新のものに修正されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：ドキュメント中のすべての参照箇所でAPIバージョンが更新され、これによりユーザーは最新の機能と改善点を利用できます。

2. **重要な機能に関する注意喚起の更新**：新しいAPIバージョンに関する特記事項が反映されており、アクセス権限に関連する注意事項が記載されています。特に、外部で設定されたアクセス許可を変更できないことや、アクセス制限コンテンツ使用時のタイミングラグについての説明が含まれています。

3. **インデックスの許可フィルターおよび検索機能の改善**：許可フィルターの有効化やクエリの実行時におけるヘッダーの追加についての手順が更新され、ユーザーがこれらの機能を正確に実行できるようにされています。

4. **SDKおよびREST APIの参照更新**：最新のSDKやREST APIへの参照が更新され、ユーザーは新しい機能や利用方法を理解しやすくなっています。

これらの変更によって、ユーザーはより効果的にAzureのドキュメントレベルアクセス制御機能を活用でき、最新のガイドラインに従った操作が可能になります。

## articles/search/search-explorer.md{#item-738774}

<details>
<summary>Diff</summary>
````diff
@@ -70,7 +70,7 @@ The following are examples of JSON queries you can run using Search explorer. To
 
 ### Run an unspecified query
 
-In Search explorer, POST requests are formulated internally using [Documents - Search Post](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (REST API), with responses returned as verbose JSON documents.
+In Search explorer, POST requests are formulated internally using [Documents - Search Post](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true) (REST API), with responses returned as verbose JSON documents.
 
 For a first look at content, execute an empty search by selecting **Search** with no terms provided. An empty search is useful as a first query because it returns entire documents so that you can review document composition. On an empty search, there's no search score, and documents are returned in arbitrary order (`"@search.score": 1` for all documents). By default, 50 documents are returned per search request.
 
@@ -198,7 +198,7 @@ In this quickstart, you used **Search explorer** to query an index using the RES
 
 ## Next step
 
-To learn more about query structures and syntax, use a REST client to create query expressions that use more parts of the REST API. [Documents - Search Post](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (REST API) is especially helpful for learning and exploration.
+To learn more about query structures and syntax, use a REST client to create query expressions that use more parts of the REST API. [Documents - Search Post](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true) (REST API) is especially helpful for learning and exploration.
 
 > [!div class="nextstepaction"]
 > [Quickstart: Full-text search](search-get-started-text.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Search ExplorerでのAPIバージョンの更新"
}
```

### Explanation
この変更は、AzureのSearch Explorerに関する記事を更新し、使用されるREST APIのバージョンを最新のものに置き換えることを目的としています。具体的には、旧バージョン「2026-05-01-preview」から新しいバージョン「2026-08-01-preview」への変更を行っています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：記事内のすべてのAPI参照が新しいバージョン「2026-08-01-preview」に更新されており、これによりユーザーは最新の機能や改善点にアクセスできるようになります。

2. **検索クエリの実行方法の説明**：Search Explorer内でのPOSTリクエストの構成方法についての説明も更新され、最新のAPIバージョンに沿った情報が提供されています。これにより、ユーザーは新しい機能や入力方法を正しく利用できるようになります。

この変更により、Search Explorerを使用する際のドキュメントが最新の情報を反映し、ユーザーが新機能をスムーズに活用できるようになります。

## articles/search/search-faceted-navigation-examples.md{#item-2b1158}

<details>
<summary>Diff</summary>
````diff
@@ -1,4 +1,4 @@
-﻿---
+---
 title: Faceted Navigation Examples
 description: Examples that demonstrate query syntax for facet hierarchies, distinct counts, facet aggregations, and facet filters.
 ms.service: azure-ai-search
@@ -199,7 +199,7 @@ Results from this query are as follows:
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Using the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or the Azure portal, you can configure a facet hierarchy using the `>` and `;` operators.
+Using the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) or the Azure portal, you can configure a facet hierarchy using the `>` and `;` operators.
 
 | Operator | Description |
 |-|-|
@@ -218,7 +218,7 @@ Notice that parentheses are processed before nesting and append operations: `A >
 There are several examples for facet hierarchies. The first example is a query that returns just a few documents, which is helpful for viewing a full response. Facets count the parent document (Hotels) and not intermediate subdocuments (Rooms), so the response determines the number of *hotels* that have any rooms in each facet bucket.
 
 ```http
-POST /indexes/hotels-sample/docs/search?api-version=2026-05-01-preview
+POST /indexes/hotels-sample/docs/search?api-version=2026-08-01-preview
 {
   "search": "ocean",  
   "facets": ["Address/StateProvince>Address/City", "Tags>Rooms/BaseRate,values:50"],
@@ -378,7 +378,7 @@ Results from this query are as follows. Both hotels have pools. For other tags,
 This second example extends the previous one, demonstrating multiple top-level facets with multiple children. Notice the semicolon (`;`) operator separates each child.
 
 ```http
-POST /indexes/hotels-sample/docs/search?api-version=2026-05-01-preview
+POST /indexes/hotels-sample/docs/search?api-version=2026-08-01-preview
 {  
   "search": "+ocean",  
   "facets": ["Address/StateProvince > Address/City", "Tags > (Rooms/BaseRate,values:50 ; Rooms/Type)"],
@@ -479,7 +479,7 @@ Address/StateProvince
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Using the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or the Azure portal, you can configure facet filters.
+Using the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) or the Azure portal, you can configure facet filters.
 
 Facet filtering enables you to constrain the facet values returned to those matching a specified regular expression. Two new parameters accept a regular expression that is applied to the facet field:
 
@@ -504,7 +504,7 @@ The following example shows how to escape special characters in your regular exp
 Here's an example of a facet filter that matches on Budget and Extended-Stay hotels, with Rating as a child of each hotel category.
 
 ```http
-POST /indexes/hotels-sample/docs/search?api-version=2026-05-01-preview
+POST /indexes/hotels-sample/docs/search?api-version=2026-08-01-preview
 { 
     "search": "*", 
     "facets": ["(Category,includeTermFilter:/(Budget|Extended-Stay)/)>Rating,values:1|2|3|4|5"],
@@ -602,7 +602,7 @@ The following example is an abbreviated response (hotel documents are omitted fo
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Using the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or the Azure portal, you can aggregate facets.
+Using the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) or the Azure portal, you can aggregate facets.
 
 Facet aggregations allow you to compute metrics from facet values. The aggregation capability works alongside the existing faceting options.
 
@@ -627,7 +627,7 @@ You can sum any facetable field of a numeric data type (except vectors and geogr
 Here's an example using the hotels-sample index. The Rooms/SleepsCount field is facetable and numeric, so we choose this field to demonstrate sum. If we sum that field, we get the sleep count for the entire hotel. Recall that facets count the parent document (Hotels) and not intermediate subdocuments (Rooms), so the response sums the SleepsCount of all rooms for the entire hotel. In this query, we add a filter to sum the SleepsCount for just one hotel.
 
 ```http
-POST /indexes/hotels-sample/docs/search?api-version=2026-05-01-preview
+POST /indexes/hotels-sample/docs/search?api-version=2026-08-01-preview
 
 { 
       "search": "*",
@@ -735,7 +735,7 @@ A response for the query might look like the following example. Windy Ocean Mode
 Here's an example using a hypothetical 'facets' index that shows the syntax for each aggregation. Notice that cardinality has an extra `precisionThreshold` option (default is 3,000) set to 40,000 in this example.
 
 ```http
-POST https://search-service.search.windows.net/indexes/facets/docs/search?api-version=2026-05-01-preview 
+POST https://search-service.search.windows.net/indexes/facets/docs/search?api-version=2026-08-01-preview
 Authorization: Bearer {{token}}
 Content-Type: application/json
 
@@ -798,7 +798,7 @@ You can add a default value to use if a document contains a null for that field:
 Here's a request that illustrates the default specification for each field type.
 
 ```http
-POST https://search-service.search.windows.net/indexes/facets/docs/search?api-version=2026-05-01-preview 
+POST https://search-service.search.windows.net/indexes/facets/docs/search?api-version=2026-08-01-preview
 Authorization: Bearer {{token}} 
 Content-Type: application/json 
 
@@ -820,7 +820,7 @@ For string fields, a default value is delimited using the single quote character
 If the underlying data supports the use case, you can specify multiple metrics on the same field.
 
 ```http
-POST https://search-service.search.windows.net/indexes/facets/docs/search?api-version=2026-05-01-preview 
+POST https://search-service.search.windows.net/indexes/facets/docs/search?api-version=2026-08-01-preview
 Authorization: Bearer {{token}} 
 Content-Type: application/json 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファセットナビゲーション例のAPIバージョン更新"
}
```

### Explanation
この変更は、Azureのファセットナビゲーションに関する記事に対して行われたもので、関連するREST APIのバージョンを最新のものにアップデートすることが主な目的です。具体的には、旧バージョンの「2026-05-01-preview」から新バージョンの「2026-08-01-preview」への変更が行われています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：記事内のすべてのAPI参照において、バージョンが新しい「2026-08-01-preview」に更新されています。これにより、ユーザーは最新の機能や改善を活用することができます。

2. **ファセット階層およびフィルタの構成方法**：記事中のコード例や説明が新しいAPIバージョンに基づいて修正されており、特にファセットフィルタやファセット集計の使用方法に関する最新の情報が提供されています。

3. **HTTPリクエストの例の更新**：クエリの実行に関するHTTP POSTリクエストの例が、更新されたAPIバージョンを反映する形で修正されており、ユーザーが正確にリクエストを構成できるようになっています。

この変更により、ファセットナビゲーションの例に関する記事が最新の情報を反映しており、ユーザーが新しい機能を効果的に利用できるようになります。

## articles/search/search-file-storage-integration.md{#item-d20e26}

<details>
<summary>Diff</summary>
````diff
@@ -75,10 +75,10 @@ The data source definition specifies the data to index, credentials, and policie
 
 You can use 2020-06-30-preview or later for "type": `"azurefile"`. We recommend the latest preview API.
 
-1. [Create a data source](/rest/api/searchservice/indexers/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true) to set its definition, using a preview API for "type": `"azurefile"`.
+1. [Create a data source](/rest/api/searchservice/indexers/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true) to set its definition, using a preview API for "type": `"azurefile"`.
 
     ```http
-    POST /datasources?api-version=2026-05-01-preview
+    POST /datasources?api-version=2026-08-01-preview
     {
         "name" : "my-file-datasource",
         "type" : "azurefile",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイルストレージ統合のAPIバージョン更新"
}
```

### Explanation
この変更は、Azureのファイルストレージ統合に関する記事を更新し、使用されるREST APIのバージョンを最新のものに置き換えることを目的としています。具体的には、旧バージョン「2026-05-01-preview」から新しいバージョン「2026-08-01-preview」への変更が行われています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：データソースを作成するためのAPI参照が新しいバージョンに更新されており、これによりユーザーは最新の機能や改善にアクセスできるようになります。

2. **HTTPリクエストの例の修正**：データソース作成に関するHTTP POSTリクエストの例も更新され、変更後のAPIバージョンを反映する形になっています。これにより、ユーザーが正確にリクエストを構成できるようになります。

この変更により、ファイルストレージ統合に関連する記事が最新の情報を反映しており、ユーザーが新機能を効果的に利用できるようになります。

## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -402,7 +402,7 @@ When the wizard completes the configuration, it creates the following objects:
 | Object | Description |
 |--|--|
 | Data source | Represents a connection to Azure Blob Storage. |
-| Index | Contains text fields, vector fields, vectorizers, vector profiles, and vector algorithms. You can't modify the default index during the wizard workflow. Indexes conform to the [latest preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) so that you can use preview features. |
+| Index | Contains text fields, vector fields, vectorizers, vector profiles, and vector algorithms. You can't modify the default index during the wizard workflow. Indexes conform to the [latest preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) so that you can use preview features. |
 | Skillset | Contains the following skills:<br><ul><li>The [Document Extraction skill](cognitive-search-skill-document-extraction.md) or [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) extracts text and images from source documents. The [Text Split skill](cognitive-search-skill-textsplit.md) accompanies the Document Extraction skill for data chunking, while the Document Layout skill has built-in chunking.</li><li>The [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md) verbalizes images in natural language. If you're using direct multimodal embeddings, this skill is absent.</li><li>The [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md), [AML skill](cognitive-search-aml-skill.md), or [Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) is called once for text vectorization and once for image vectorization.</li><li>The [Shaper skill](cognitive-search-skill-shaper.md) enriches the output with metadata and creates new images with contextual information.</li></ul> |
 | Indexer | Drives the indexing pipeline, with field mappings and output field mappings (if applicable). |
 | Knowledge store | Stores extracted images as blobs in Azure Storage for downstream processing or multimodal scenarios. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ウィザードでのインデックスAPIバージョン更新"
}
```

### Explanation
この変更は、Azureポータルでの画像検索の開始に関する記事の内容を更新し、インデックスに使用されるREST APIのバージョンを最新のものに置き換えるために行われました。具体的には、旧バージョン「2026-05-01-preview」から新しいバージョン「2026-08-01-preview」への変更が行われています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：ウィザードのワークフロー中に修正できないデフォルトのインデックスに関連するAPIの参照が新しいバージョンに更新されており、これによりユーザーは最新の機能セットを利用できるようになります。

2. **インデックスに関する説明の更新**：インデックスがどのように構成され、最新のプレビュー機能に準拠しているかという情報も最新のAPIバージョンを反映する形で修正されています。

この変更により、ポータルでの画像検索を開始するためのインストラクションが最新の情報を反映し、ユーザーが新機能や改善を活用できるようになります。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -460,7 +460,7 @@ When the wizard completes the configuration, it creates the following objects:
 | Object | Description |
 |--|--|
 | Data source | Represents a connection to your chosen data source. |
-| Index | Contains vector fields, vectorizers, vector profiles, and vector algorithms. You can't modify the default index during the wizard workflow. Indexes conform to the [latest preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) so that you can use preview features. |
+| Index | Contains vector fields, vectorizers, vector profiles, and vector algorithms. You can't modify the default index during the wizard workflow. Indexes conform to the [latest preview REST API](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) so that you can use preview features. |
 | Skillset | Contains the following skills and configuration:<br><ul><li>The [Text Split skill](cognitive-search-skill-textsplit.md) for chunking.</li><li>The [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md), [AML skill](cognitive-search-aml-skill.md), or [Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) for vectorization.</li><li>The [index projections](search-how-to-define-index-projections.md) configuration, which maps data from one document in the data source to its corresponding chunks in a "child" index.</li></ul> |
 | Indexer | Drives the indexing pipeline, with field mappings and output field mappings (if applicable). |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスAPIバージョンの更新"
}
```

### Explanation
この変更は、ポータルでのベクトルインポートに関する記事の内容を更新し、インデックスに使用されるREST APIのバージョンを最新のものに置き換えるために行われました。具体的に、旧バージョン「2026-05-01-preview」から新しいバージョン「2026-08-01-preview」への変更がなされています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：ウィザードのワークフロー中に修正できないデフォルトのインデックスに関連するAPIの参照が新しいバージョンに更新されており、これによりユーザーは最新のプレビュー機能にアクセスできるようになります。

2. **インデックスに関する説明の更新**：インデックスがどのように構成され、その機能が最新のプレビューREST APIに準拠しているかについての情報も改訂されました。

この変更によって、ポータルでのベクトルインポートに関する情報が最新状態になり、ユーザーが新機能を効果的に利用できるようになります。

## articles/search/search-get-started-portal.md{#item-6d0cb1}

<details>
<summary>Diff</summary>
````diff
@@ -199,7 +199,7 @@ Review the index definition options to understand what you can and can't edit du
 
 ## Query the index
 
-You now have a search index that can be queried using [**Search explorer**](search-explorer.md), which sends REST calls that conform to [Documents - Search Post (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true). This tool supports [simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search) and [full Lucene query syntax](/rest/api/searchservice/lucene-query-syntax-in-azure-search) for keyword search.
+You now have a search index that can be queried using [**Search explorer**](search-explorer.md), which sends REST calls that conform to [Documents - Search Post (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true). This tool supports [simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search) and [full Lucene query syntax](/rest/api/searchservice/lucene-query-syntax-in-azure-search) for keyword search.
 
 To query your search index:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスのREST APIバージョン更新"
}
```

### Explanation
この変更は、検索ポータルに関する記事において、検索インデックスがREST APIを介してクエリできる内容を更新したものです。具体的には、従来のAPIバージョン「2026-05-01-preview」から、新しいAPIバージョン「2026-08-01-preview」への変更が反映されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：検索インデックスをクエリするために使用されるREST APIの参照が新しいバージョンに置き換えられています。これにより、ユーザーは最新の仕様や機能を利用できるようになります。

2. **クエリ機能の強化**：この変更は、検索エクスプローラーを使用して検索インデックスに対するクエリを実行する際のガイドラインを最新のAPIに基づいて更新しているため、ユーザーがより正確に、また効率的にクエリを行えるようになります。

この変更により、ユーザーは最新の機能とAPIを活用して、より強力な検索体験を提供できるようになります。

## articles/search/search-how-to-create-indexers.md{#item-de71fb}

<details>
<summary>Diff</summary>
````diff
@@ -252,7 +252,7 @@ Change detection logic is built into the data platforms. How an indexer supports
 
 Indexers keep track of the last document they processed from the data source through an internal *high water mark*. The marker is never exposed in the API, but internally the indexer tracks where it stopped. When indexing resumes, either through a scheduled run or an on-demand invocation, the indexer references the high water mark so that it can pick up where it left off.
 
-If you need to clear the high water mark to reindex in full, you can use [Reset Indexer](/rest/api/searchservice/indexers/reset). For more selective reindexing, use [Reset Skills](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or [Reset Documents](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2026-05-01-preview&preserve-view=true). Through the reset APIs, you can clear internal state, and also flush the cache if you enabled [incremental enrichment](enrichment-cache-how-to-configure.md). For more background and comparison of each reset option, see [Run or reset indexers, skills, and documents](search-howto-run-reset-indexers.md).
+If you need to clear the high water mark to reindex in full, you can use [Reset Indexer](/rest/api/searchservice/indexers/reset). For more selective reindexing, use [Reset Skills](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2026-08-01-preview&preserve-view=true) or [Reset Documents](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2026-08-01-preview&preserve-view=true). Through the reset APIs, you can clear internal state, and also flush the cache if you enabled [incremental enrichment](enrichment-cache-how-to-configure.md). For more background and comparison of each reset option, see [Run or reset indexers, skills, and documents](search-howto-run-reset-indexers.md).
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサのリセットAPIバージョンの更新"
}
```

### Explanation
この変更は、インデクサの作成に関する記事を更新し、リセットAPIのバージョンを最新にすることを目的としています。具体的には、リセットスキルやリセットドキュメントのAPI参照が、従来のバージョン「2026-05-01-preview」から新しいバージョン「2026-08-01-preview」に変更されました。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：リセットスキルおよびリセットドキュメントのAPIへのリンクが新しい仕様に基づいて更新されており、ユーザーは最新の機能を利用できるようになっています。

2. **インデクサの機能に関する説明の明確化**：内部状態のクリアやキャッシュフラッシュの手法についても言及され、選択的な再インデクシングがどのように行われるかを明確にしています。

この変更により、ユーザーはインデクサのリセット機能を最新の仕様に基づいて使用することができ、より効果的にデータの再インデクシングを行うことが可能になります。

## articles/search/search-how-to-index-cosmosdb-gremlin.md{#item-e5e93d}

<details>
<summary>Diff</summary>
````diff
@@ -49,10 +49,10 @@ The data source definition specifies the data to index, credentials, and policie
 
 For this call, specify a preview REST API version to create a data source that connects via Azure Cosmos DB for Apache Gremlin. You can use `2021-04-01-preview` or later. We recommend the [latest preview REST API](/rest/api/searchservice/search-service-api-versions#preview-versions).
 
-1. [Create or update a data source](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) to set its definition: 
+1. [Create or update a data source](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) to set its definition:
 
    ```http
-    POST https://[service name].search.windows.net/datasources?api-version=2026-05-01-preview
+    POST https://[service name].search.windows.net/datasources?api-version=2026-08-01-preview
     Content-Type: application/json
     api-key: [Search service admin key]
     {
@@ -111,7 +111,7 @@ In a [search index](search-what-is-an-index.md), add fields to accept the source
 1. [Create or update an index](/rest/api/searchservice/indexes/create-or-update) to define search fields that store data:
 
    ```http
-    POST https://[service name].search.windows.net/indexes?api-version=2026-05-01-preview
+    POST https://[service name].search.windows.net/indexes?api-version=2026-08-01-preview
     Content-Type: application/json
     api-key: [Search service admin key]
     {
@@ -170,10 +170,10 @@ In a [search index](search-what-is-an-index.md), add fields to accept the source
 
 Once the index and data source have been created, you're ready to create the indexer. Indexer configuration specifies the inputs, parameters, and properties controlling run time behaviors.
 
-1. [Create or update an indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) by giving it a name and referencing the data source and target index:
+1. [Create or update an indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) by giving it a name and referencing the data source and target index:
 
     ```http
-    POST https://[service name].search.windows.net/indexers?api-version=2026-05-01-preview
+    POST https://[service name].search.windows.net/indexers?api-version=2026-08-01-preview
     Content-Type: application/json
     api-key: [search service admin key]
     {
@@ -205,7 +205,7 @@ An indexer runs automatically when it's created. You can prevent this by setting
 To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) request:
 
 ```http
-GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2026-05-01-preview
+GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2026-08-01-preview
   Content-Type: application/json  
   api-key: [admin key]
 ```
@@ -282,7 +282,7 @@ When graph data is deleted, you might want to delete its corresponding document
 The following example creates a data source with a soft-deletion policy:
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2026-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2026-08-01-preview
 Content-Type: application/json
 api-key: [Search service admin key]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新によるCosmos DB Gremlinインデクシング手順の改訂"
}
```

### Explanation
この変更は、Azure Cosmos DB Gremlinを使用したデータインデクシングに関する記事において、APIバージョンの更新を反映したものです。具体的には、複数のAPIの参照が古いバージョン「2026-05-01-preview」から新しいバージョン「2026-08-01-preview」に更新されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：データソースやインデクサーを作成・更新する際のAPIエンドポイントが新しいバージョンに変更されており、最新の機能や改善点を利用することができます。

2. **手順の整合性向上**：すべての関連するAPI呼び出しにおいて一貫したバージョン管理が行われているため、ユーザーが手順を追いやすくなり、適切なAPIリクエストを行うことが強調されています。

3. **詳細な構文例の提供**：GETおよびPOSTリクエストの構文例も更新されており、ユーザーは新しいAPIバージョンに基づいた正確なリクエストを簡単に設定できるようになっています。

この変更により、ユーザーは最新のAPIに基づいて効率的にCosmos DB Gremlinのインデクシングを行うことができ、よりスムーズな操作体験を実現することが期待されます。

## articles/search/search-how-to-index-cosmosdb-mongodb.md{#item-b5aa9f}

<details>
<summary>Diff</summary>
````diff
@@ -61,10 +61,10 @@ The data source definition specifies the data to index, credentials, and policie
 
 For this call, specify a preview REST API version to create a data source that connects via the MongoDB API. You can use `2020-06-30-preview` or later. We recommend the [latest preview REST API](/rest/api/searchservice/search-service-api-versions#preview-versions).
 
-1. [Create or update a data source](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) to set its definition: 
+1. [Create or update a data source](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) to set its definition:
 
     ```http
-    POST https://[service name].search.windows.net/datasources?api-version=2026-05-01-preview
+    POST https://[service name].search.windows.net/datasources?api-version=2026-08-01-preview
     Content-Type: application/json
     api-key: [Search service admin key]
     {
@@ -119,10 +119,10 @@ Avoid port numbers in the endpoint URL. If you include the port number, the conn
 
 In a [search index](search-what-is-an-index.md), add fields to accept the source JSON documents or the output of your custom query projection. Ensure that the search index schema is compatible with source data. For content in Azure Cosmos DB, your search index schema should correspond to the [Azure Cosmos DB items](/azure/cosmos-db/resource-model#azure-cosmos-db-items) in your data source.
 
-1. [Create or update an index](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) to define search fields that store data:
+1. [Create or update an index](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) to define search fields that store data:
 
     ```http
-    POST https://[service name].search.windows.net/indexes?api-version=2026-05-01-preview
+    POST https://[service name].search.windows.net/indexes?api-version=2026-08-01-preview
     Content-Type: application/json
     api-key: [Search service admin key]
     
@@ -173,10 +173,10 @@ In a [search index](search-what-is-an-index.md), add fields to accept the source
 
 Once the index and data source have been created, you're ready to create the indexer. Indexer configuration specifies the inputs, parameters, and properties controlling run time behaviors.
 
-1. [Create or update an indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) by giving it a name and referencing the data source and target index:
+1. [Create or update an indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) by giving it a name and referencing the data source and target index:
 
     ```http
-    POST https://[service name].search.windows.net/indexers?api-version=2026-05-01-preview
+    POST https://[service name].search.windows.net/indexers?api-version=2026-08-01-preview
     Content-Type: application/json
     api-key: [search service admin key]
     {
@@ -205,10 +205,10 @@ An indexer runs automatically when it's created. You can prevent this by setting
 
 ## Check indexer status
 
-To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&preserve-view=true) request:
+To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&preserve-view=true) request:
 
 ```http
-GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2026-05-01-preview
+GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2026-08-01-preview
   Content-Type: application/json  
   api-key: [admin key]
 ```
@@ -287,7 +287,7 @@ If you're using a custom query, make sure that the property referenced by `softD
 The following example creates a data source with a soft-deletion policy:
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2026-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2026-08-01-preview
 Content-Type: application/json
 api-key: [Search service admin key]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新によるCosmos DB MongoDBインデクシング手順の改訂"
}
```

### Explanation
この変更は、Azure Cosmos DB MongoDBを用いたインデクシングに関する記事において、APIバージョンの更新を反映したものです。具体的には、関連するAPIのバージョンが古い「2026-05-01-preview」から新しい「2026-08-01-preview」へと更新されており、ユーザーが最新の機能を使用できるようになっています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：データソース、インデクス、インデクサーを作成・更新する際のエンドポイントが新しい仕様に基づいて変更されており、これにより最新の機能を利用することが推奨されています。

2. **手順の整合性向上**：すべての関連リクエストで一貫したAPIバージョンを用いることにより、ユーザーは手順に従いやすくなっています。その結果、インデクシングプロセスをより簡単に理解できるようになっています。

3. **具体的なリクエスト例の提供**：GETおよびPOSTリクエストの具体的な構文例が更新されており、ユーザーが新しいAPIバージョンに基づいて正確にリクエストを行う手助けとなります。

この変更により、ユーザーは最新のAPIに基づいて効率的にCosmos DB MongoDBのインデクシングを実施でき、よりスムーズな運用が可能になります。

## articles/search/search-how-to-index-mysql.md{#item-fffdee}

<details>
<summary>Diff</summary>
````diff
@@ -56,7 +56,7 @@ As noted, there’s no portal support for indexer creation, but a MySQL indexer
 
 The data source definition specifies the data to index, credentials, and policies for identifying changes in the data. The data source is defined as an independent resource so that it can be used by multiple indexers.
 
-[Create or Update Data Source](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true) specifies the definition. Be sure to use a preview REST API when creating the data source.
+[Create or Update Data Source](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true) specifies the definition. Be sure to use a preview REST API when creating the data source.
 
 ```http
 {   
@@ -94,7 +94,7 @@ The data source definition specifies the data to index, credentials, and policie
 
 ## Create an index
 
-[Create or Update Index](/rest/api/searchservice/indexes/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true) specifies the index schema:
+[Create or Update Index](/rest/api/searchservice/indexes/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true) specifies the index schema:
 
 ```http
 {
@@ -134,7 +134,7 @@ The following table maps the MySQL database to Azure AI Search equivalents. For
 
 Once the index and data source have been created, you're ready to create the indexer. Indexer configuration specifies the inputs, parameters, and properties controlling run time behaviors.
 
-[Create or update an indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) by giving it a name and referencing the data source and target index:
+[Create or update an indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) by giving it a name and referencing the data source and target index:
 
 ```http
 {
@@ -163,10 +163,10 @@ Once the index and data source have been created, you're ready to create the ind
 
 ## Check indexer status
 
-Send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&preserve-view=true) request to monitor indexer execution:
+Send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&preserve-view=true) request to monitor indexer execution:
 
 ```http
-GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2026-05-01-preview
+GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2026-08-01-preview
   Content-Type: application/json  
   api-key: [admin key]
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新によるMySQLインデクシング手順の改訂"
}
```

### Explanation
この変更は、Azure AI SearchにおけるMySQLデータベースのインデクシング手順を扱った記事において、APIバージョンの更新を反映したものです。具体的には、データソースやインデクサーに関するAPIの参照が古いバージョン「2026-05-01-preview」から新しいバージョン「2026-08-01-preview」へと更新されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：各APIのエンドポイントが新しいバージョンに更新されており、最新の機能や改善点を利用することが可能です。これにより、ユーザーは利便性が向上します。

2. **手順の整合性向上**：すべての関連するAPI呼び出しで最新のバージョンを使用することにより、インデクシングプロセスの手順が一貫性を持つようになっています。このことは、ユーザーが手順を理解しやすくするのに寄与します。

3. **具体的なリクエスト例の更新**：HTTPリクエストの具体例が新しいAPIバージョンに基づいて更新されており、ユーザーが正確にリクエストを行うための参考になります。

この変更により、ユーザーは最新のAPIに基づいてMySQLデータベースのインデクシングをスムーズに実行できるようになり、より効率的に作業を進めることができることが期待されます。

## articles/search/search-how-to-index-sharepoint-online.md{#item-8c099c}

<details>
<summary>Diff</summary>
````diff
@@ -25,11 +25,11 @@ When setting up permissions, consider the following information:
 > [Fill out this form](https://aka.ms/azure-cognitive-search/indexer-preview) to register for the preview. All requests are approved automatically. After you fill out the form, use a [preview REST API](/rest/api/searchservice/search-service-api-versions#preview-versions) to index your content. 
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag occurs before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag occurs before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data flows outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -137,7 +137,7 @@ After selecting **Save**, you receive an object ID assigned to your search servi
 
 ### Step 2: Decide which permissions the indexer requires
 
-For the decision matrix that covers ACL and non-ACL scenarios, see [Choose your permissions setup](#choose-your-permissions-setup). If you choose delegated permissions, user-delegated tokens expire every 75 minutes and require manual indexing using [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2026-05-01-preview&tabs=HTTP&preserve-view=true) when they expire. Delegated permissions are recommended only for small testing operations.
+For the decision matrix that covers ACL and non-ACL scenarios, see [Choose your permissions setup](#choose-your-permissions-setup). If you choose delegated permissions, user-delegated tokens expire every 75 minutes and require manual indexing using [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2026-08-01-preview&tabs=HTTP&preserve-view=true) when they expire. Delegated permissions are recommended only for small testing operations.
 
 <a name='step-3-create-an-azure-ad-application'></a>
 
@@ -293,12 +293,12 @@ For SharePoint indexing, the data source must have the following required proper
 + **credentials** provide the SharePoint endpoint and the authentication method allowed for the application to request the Microsoft Entra tokens. An example SharePoint endpoint is `https://[your-tenant-name].sharepoint.com/teams/MySharePointSite`. You can get the endpoint by navigating to the home page of your SharePoint site and copying the URL from the browser. Review the [connection string format](#connection-string-format) for the supported syntax.
 + **container** specifies which document library to index. Properties [control which documents are indexed](#controlling-which-documents-are-indexed).
 
-To create a data source, call [Create Data Source (preview)](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true).
+To create a data source, call [Create Data Source (preview)](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true).
 
 Here's a data source definition sample for credentials with application secret or system-assigned managed identity.
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2026-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2026-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
@@ -319,7 +319,7 @@ Federated credential configurations require `FederatedCredentialApplicationId` i
 > `ApplicationId` and `FederatedCredentialApplicationId` are different values. `ApplicationId` is your registered Entra ingestion app that holds the SharePoint permissions. `FederatedCredentialApplicationId` is the application (client) ID of the managed identity itself, which is the entity whose token proves the managed identity's identity.
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2026-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2026-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
@@ -379,7 +379,7 @@ The following examples show data sources created with `FederatedCredentialApplic
 **System-assigned managed identity with federated credential:**
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2026-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2026-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
@@ -441,10 +441,10 @@ If your indexer uses [SharePoint ACL configuration (preview)](search-indexer-sha
 
 The index specifies the fields in a document, attributes, and other constructs that shape the search experience.
 
-To create an index, call [Create Index (preview)](/rest/api/searchservice/indexes/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true):
+To create an index, call [Create Index (preview)](/rest/api/searchservice/indexes/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true):
 
 ```http
-POST https://[service name].search.windows.net/indexes?api-version=2026-05-01-preview
+POST https://[service name].search.windows.net/indexes?api-version=2026-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
@@ -477,10 +477,10 @@ An indexer connects a data source with a target search index and provides a sche
 
 To create the indexer:
 
-1. Send a [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-05-01-preview&tabs=HTTP&preserve-view=true) request:
+1. Send a [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-08-01-preview&tabs=HTTP&preserve-view=true) request:
 
     ```http
-    POST https://[service name].search.windows.net/indexers?api-version=2026-05-01-preview
+    POST https://[service name].search.windows.net/indexers?api-version=2026-08-01-preview
     Content-Type: application/json
     api-key: [admin key]
     
@@ -516,17 +516,17 @@ To create the indexer:
 
     When you use application permissions, you can query the index while the initial indexer run is in progress, but only items that are already indexed return results. Wait until the run completes for full coverage. The remaining instructions in this step apply only to delegated permissions.
 
-1. When you create the indexer for the first time, the [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-05-01-preview&tabs=HTTP&preserve-view=true) request waits until you complete the next step. You must call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&tabs=HTTP&preserve-view=true) to get the link and enter your new device code. 
+1. When you create the indexer for the first time, the [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-08-01-preview&tabs=HTTP&preserve-view=true) request waits until you complete the next step. You must call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&tabs=HTTP&preserve-view=true) to get the link and enter your new device code.
 
     ```http
-    GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2026-05-01-preview
+    GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2026-08-01-preview
     Content-Type: application/json
     api-key: [admin key]
     ```
 
-    If you don't call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&tabs=HTTP&preserve-view=true) within 10 minutes, the code expires and you must recreate the [data source](#create-data-source).
+    If you don't call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&tabs=HTTP&preserve-view=true) within 10 minutes, the code expires and you must recreate the [data source](#create-data-source).
 
-1. Copy the device sign-in code from the [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&tabs=HTTP&preserve-view=true) response. The device sign-in code can be found in the "errorMessage".
+1. Copy the device sign-in code from the [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&tabs=HTTP&preserve-view=true) response. The device sign-in code can be found in the "errorMessage".
 
     ```http
     {
@@ -549,7 +549,7 @@ To create the indexer:
 
     :::image type="content" source="media/search-howto-index-sharepoint-online/aad-app-approve-api-permissions.png" alt-text="Screenshot showing how to approve API permissions.":::
 
-1. The [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-05-01-preview&tabs=HTTP&preserve-view=true) initial request completes if all the permissions provided earlier are correct and within the 10-minute timeframe.
+1. The [Create Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-08-01-preview&tabs=HTTP&preserve-view=true) initial request completes if all the permissions provided earlier are correct and within the 10-minute timeframe.
 
 When setting up permissions, consider the following information:
 > If the Microsoft Entra application requires admin approval and wasn't approved before signing in, you might see the following screen. [Admin approval](/azure/active-directory/manage-apps/grant-admin-consent) is required to continue.
@@ -558,16 +558,16 @@ When setting up permissions, consider the following information:
 
 ### Step 7: Check the indexer status
 
-After creating the indexer, call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&tabs=HTTP&preserve-view=true):
+After creating the indexer, call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&tabs=HTTP&preserve-view=true):
 
 ```http
-GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2026-05-01-preview
+GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2026-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 ```
 
 ```http
-GET https://[service-name].search.windows.net/indexes/[index-name]/docs?search=*&$count=true&api-version=2026-05-01-preview
+GET https://[service-name].search.windows.net/indexes/[index-name]/docs?search=*&$count=true&api-version=2026-08-01-preview
 api-key: [admin-api-key]
 ```
 
@@ -579,18 +579,18 @@ If you change the data source while the device code is expired, sign in again to
 
 To update a data source, follow these steps assuming an expired device code:
 
-1. Call [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2026-05-01-preview&tabs=HTTP&preserve-view=true) to manually start [indexer execution](search-howto-run-reset-indexers.md).
+1. Call [Run Indexer (preview)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2026-08-01-preview&tabs=HTTP&preserve-view=true) to manually start [indexer execution](search-howto-run-reset-indexers.md).
 
     ```http
-    POST https://[service name].search.windows.net/indexers/sharepoint-indexer/run?api-version=2026-05-01-preview  
+    POST https://[service name].search.windows.net/indexers/sharepoint-indexer/run?api-version=2026-08-01-preview
     Content-Type: application/json
     api-key: [admin key]
     ```
 
-1. Check the [indexer status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&tabs=HTTP&preserve-view=true). 
+1. Check the [indexer status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&tabs=HTTP&preserve-view=true).
 
     ```http
-    GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2026-05-01-preview
+    GET https://[service name].search.windows.net/indexers/sharepoint-indexer/status?api-version=2026-08-01-preview
     Content-Type: application/json
     api-key: [admin key]
     ```
@@ -685,7 +685,7 @@ Set inclusion and exclusion criteria in the "parameters" section of the indexer
 To include specific file extensions, set `"indexedFileNameExtensions"` to a comma-separated list of file extensions with a leading dot. To exclude specific file extensions, set `"excludedFileNameExtensions"` to the extensions that you want to skip. If the same extension appears in both lists, the indexer excludes it from indexing.
 
 ```http
-PUT /indexers/[indexer name]?api-version=2026-05-01-preview
+PUT /indexers/[indexer name]?api-version=2026-08-01-preview
 {
     "parameters" : { 
         "configuration" : { 
@@ -711,7 +711,7 @@ The `name` property is required and must be one of the following values:
 | Value | Description |
 |-|-|
 | defaultSiteLibrary | Index all content from the site's default document library. |
-| allSiteLibraries | Index all content from all document libraries in a site. Document libraries from a subsite are out of scope unless you set `includeSubsites=true` in the query (preview, 2026-05-01-preview). You can also choose `useQuery` and specify `includeLibrariesInSite` to scope to specific sites or subsites. |
+| allSiteLibraries | Index all content from all document libraries in a site. Document libraries from a subsite are out of scope unless you set `includeSubsites=true` in the query (preview). You can also choose `useQuery` and specify `includeLibrariesInSite` to scope to specific sites or subsites. |
 | allSiteLists | Index all [SharePoint list](#index-sharepoint-lists) items from a site. Preview, starting in the 2026-05-01-preview REST API. |
 | allSitePages | Index all [modern ASPX site pages](#index-aspx-site-pages) from a site. Preview, starting in the 2026-05-01-preview REST API. |
 | allSiteContent | Index libraries, lists, and pages from a site in a single indexer. Preview, starting in the 2026-05-01-preview REST API. |
@@ -746,7 +746,7 @@ For an `Invalid AAD tenant` message, a missing Microsoft Entra tenant ID, or a t
 By default, the SharePoint in Microsoft 365 indexer stops as soon as it encounters a document with an unsupported content type, such as an image. Use the `excludedFileNameExtensions` parameter to skip certain content types. However, you might need to index documents without knowing all the possible content types in advance. To continue indexing when the indexer encounters an unsupported content type, set the `failOnUnsupportedContentType` configuration parameter to false:
 
 ```http
-PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2026-05-01-preview
+PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2026-08-01-preview
 Content-Type: application/json
 api-key: [admin key]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新によるSharePoint Onlineインデクシング手順の改訂"
}
```

### Explanation
この変更は、Azure Cognitive SearchにおけるSharePoint Onlineのインデクシング手順に関する記事において、APIバージョンの更新を反映したものです。具体的には、使用するREST APIのバージョンが、古い「2026-05-01-preview」から新しい「2026-08-01-preview」へと変更されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：記事内のすべての参照が新しいAPIバージョンに更新され、これによって最新の機能や改善点を利用することが可能となります。これにより、ユーザーはより良い体験が得られます。

2. **手順の整合性が向上**：API呼び出しの一貫性が保たれることで、ユーザーが手順を理解しやすくなり、エラーを減少させることが期待されます。

3. **具体的なリクエスト例の更新**：HTTPリクエストの例が新しいAPIバージョンに合わせて変更され、ユーザーが正しいリクエストを簡単に自己実行できるようになっています。

この改訂により、ユーザーはSharePoint Onlineのインデクシング手順をよりスムーズに実行でき、最新の機能を最大限に活用することが可能となります。また、展開中の問題や意図しない動作を回避する手助けをします。

## articles/search/search-how-to-multiple-indexers-one-index.md{#item-5ccefd}

<details>
<summary>Diff</summary>
````diff
@@ -25,11 +25,11 @@ In this tutorial, you:
 > + Review content ownership, troubleshooting, and cleanup practices
 
 > [!IMPORTANT]
-> Semantic chunking in the Azure Content Understanding skill is part of the 2026-05-01-preview REST API. The multi-indexer pattern, index projections, and the Content Understanding skill without semantic chunking are generally available. However, for consistency, this tutorial uses the 2026-05-01-preview across all requests.
+> Semantic chunking in the Azure Content Understanding skill is part of the 2026-08-01-preview REST API. The multi-indexer pattern, index projections, and the Content Understanding skill without semantic chunking are generally available. However, for consistency, this tutorial uses the 2026-08-01-preview across all requests.
 >
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data flows outside of your organization's compliance and geographic boundaries and any related implications. Ensure that appropriate permissions, boundaries, and approvals are in place.
 >
@@ -172,7 +172,7 @@ To create the union-schema index:
 1. Send the create request:
 
    ```http
-   POST <search-endpoint>/indexes?api-version=2026-05-01-preview
+   POST <search-endpoint>/indexes?api-version=2026-08-01-preview
    Content-Type: application/json
    Authorization: Bearer <search-access-token>
 
@@ -299,18 +299,18 @@ To create the union-schema index:
    }
    ```
 
-   **Reference:** [Create Index (REST API)](/rest/api/searchservice/indexes/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Create Index (REST API)](/rest/api/searchservice/indexes/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    The response returns HTTP `201 Created` with the full index definition.
 
 1. Verify that the index was created:
 
    ```http
-   GET <search-endpoint>/indexes/multi-source-index?api-version=2026-05-01-preview
+   GET <search-endpoint>/indexes/multi-source-index?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
-   **Reference:** [Get Index (REST API)](/rest/api/searchservice/indexes/get?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Get Index (REST API)](/rest/api/searchservice/indexes/get?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    The response contains `"name": "multi-source-index"` and 12 fields. Confirm the `fields` array length equals 12 and the `vectorSearch` section includes the `content-azure-openai-vectorizer`.
 
@@ -325,7 +325,7 @@ To create the three folder-scoped data sources:
 1. Create the DOCX data source:
 
    ```http
-   POST <search-endpoint>/datasources?api-version=2026-05-01-preview
+   POST <search-endpoint>/datasources?api-version=2026-08-01-preview
    Content-Type: application/json
    Authorization: Bearer <search-access-token>
 
@@ -342,14 +342,14 @@ To create the three folder-scoped data sources:
    }
    ```
 
-   **Reference:** [Create Data Source (REST API)](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Create Data Source (REST API)](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    The response returns HTTP `201 Created`.
 
 1. Create the JSON data source:
 
    ```http
-   POST <search-endpoint>/datasources?api-version=2026-05-01-preview
+   POST <search-endpoint>/datasources?api-version=2026-08-01-preview
    Content-Type: application/json
    Authorization: Bearer <search-access-token>
 
@@ -366,14 +366,14 @@ To create the three folder-scoped data sources:
    }
    ```
 
-   **Reference:** [Create Data Source (REST API)](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Create Data Source (REST API)](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    The response returns HTTP `201 Created`.
 
 1. Create the CSV data source:
 
    ```http
-   POST <search-endpoint>/datasources?api-version=2026-05-01-preview
+   POST <search-endpoint>/datasources?api-version=2026-08-01-preview
    Content-Type: application/json
    Authorization: Bearer <search-access-token>
 
@@ -390,18 +390,18 @@ To create the three folder-scoped data sources:
    }
    ```
 
-   **Reference:** [Create Data Source (REST API)](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Create Data Source (REST API)](/rest/api/searchservice/data-sources/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    The response returns HTTP `201 Created`.
 
 Verify that all three data sources exist:
 
 ```http
-GET <search-endpoint>/datasources?api-version=2026-05-01-preview
+GET <search-endpoint>/datasources?api-version=2026-08-01-preview
 Authorization: Bearer <search-access-token>
 ```
 
-**Reference:** [List Data Sources (REST API)](/rest/api/searchservice/data-sources/list?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [List Data Sources (REST API)](/rest/api/searchservice/data-sources/list?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 The response `value` array contains `docx-blob-datasource`, `json-blob-datasource`, and `csv-blob-datasource`. If any are missing, review the corresponding creation step for errors.
 
@@ -414,7 +414,7 @@ To configure the DOCX pipeline:
 1. Create the skillset:
 
    ```http
-   POST <search-endpoint>/skillsets?api-version=2026-05-01-preview
+   POST <search-endpoint>/skillsets?api-version=2026-08-01-preview
    Content-Type: application/json
    Authorization: Bearer <search-access-token>
 
@@ -549,18 +549,18 @@ To configure the DOCX pipeline:
 1. Verify the skillset was created:
 
    ```http
-   GET <search-endpoint>/skillsets/docx-semantic-skillset?api-version=2026-05-01-preview
+   GET <search-endpoint>/skillsets/docx-semantic-skillset?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
-   **Reference:** [Get Skillset (REST API)](/rest/api/searchservice/skillsets/get?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Get Skillset (REST API)](/rest/api/searchservice/skillsets/get?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    The response contains `"name": "docx-semantic-skillset"` and three skills in the `skills` array.
 
 1. Create the DOCX indexer:
 
    ```http
-   POST <search-endpoint>/indexers?api-version=2026-05-01-preview
+   POST <search-endpoint>/indexers?api-version=2026-08-01-preview
    Content-Type: application/json
    Authorization: Bearer <search-access-token>
 
@@ -583,7 +583,7 @@ To configure the DOCX pipeline:
    }
    ```
 
-   **Reference:** [Create Indexer (REST API)](/rest/api/searchservice/indexers/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Create Indexer (REST API)](/rest/api/searchservice/indexers/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    The response returns HTTP `201 Created`. The indexer starts its first run automatically.
 
@@ -592,11 +592,11 @@ To configure the DOCX pipeline:
 1. Check the status of the indexer:
 
    ```http
-   GET <search-endpoint>/indexers/docx-indexer/status?api-version=2026-05-01-preview
+   GET <search-endpoint>/indexers/docx-indexer/status?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
-   **Reference:** [Get Indexer Status (REST API)](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Get Indexer Status (REST API)](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    Wait for `lastResult.status` to show `success` and confirm that `lastResult.itemsFailed` is `0`. If the status shows `inProgress`, wait 30 seconds and check again. You verify the projected DOCX output by querying the index later in this tutorial.
 
@@ -609,7 +609,7 @@ To configure the JSON pipeline:
 1. Create the JSON indexer:
 
    ```http
-   POST <search-endpoint>/indexers?api-version=2026-05-01-preview
+   POST <search-endpoint>/indexers?api-version=2026-08-01-preview
    Content-Type: application/json
    Authorization: Bearer <search-access-token>
 
@@ -661,18 +661,18 @@ To configure the JSON pipeline:
    }
    ```
 
-   **Reference:** [Create Indexer (REST API)](/rest/api/searchservice/indexers/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true), [Index JSON blobs and files](search-how-to-index-azure-blob-json.md), and [Define field mappings](search-indexer-field-mappings.md)
+   **Reference:** [Create Indexer (REST API)](/rest/api/searchservice/indexers/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true), [Index JSON blobs and files](search-how-to-index-azure-blob-json.md), and [Define field mappings](search-indexer-field-mappings.md)
 
    The response returns HTTP `201 Created`. The indexer starts its first run automatically.
 
 1. Verify that the indexer processed both records:
 
    ```http
-   GET <search-endpoint>/indexers/json-indexer/status?api-version=2026-05-01-preview
+   GET <search-endpoint>/indexers/json-indexer/status?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
-   **Reference:** [Get Indexer Status (REST API)](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Get Indexer Status (REST API)](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    Wait for `lastResult.status` to show `success` and confirm that `lastResult.itemsFailed` is `0`. If the status shows `inProgress`, wait 15 seconds and check again. You verify both JSON records by querying the index later in this tutorial.
 
@@ -685,7 +685,7 @@ To configure the CSV pipeline:
 1. Create the CSV skillset:
 
    ```http
-   POST <search-endpoint>/skillsets?api-version=2026-05-01-preview
+   POST <search-endpoint>/skillsets?api-version=2026-08-01-preview
    Content-Type: application/json
    Authorization: Bearer <search-access-token>
 
@@ -718,25 +718,25 @@ To configure the CSV pipeline:
    }
    ```
 
-   **Reference:** [Create Skillset (REST API)](/rest/api/searchservice/skillsets/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Create Skillset (REST API)](/rest/api/searchservice/skillsets/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    The response returns HTTP `201 Created`.
 
 1. Verify the skillset was created:
 
    ```http
-   GET <search-endpoint>/skillsets/csv-embedding-skillset?api-version=2026-05-01-preview
+   GET <search-endpoint>/skillsets/csv-embedding-skillset?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
-   **Reference:** [Get Skillset (REST API)](/rest/api/searchservice/skillsets/get?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Get Skillset (REST API)](/rest/api/searchservice/skillsets/get?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    The response contains `"name": "csv-embedding-skillset"` and one skill in the `skills` array.
 
 1. Create the CSV indexer:
 
    ```http
-   POST <search-endpoint>/indexers?api-version=2026-05-01-preview
+   POST <search-endpoint>/indexers?api-version=2026-08-01-preview
    Content-Type: application/json
    Authorization: Bearer <search-access-token>
 
@@ -796,18 +796,18 @@ To configure the CSV pipeline:
    }
    ```
 
-   **Reference:** [Create Indexer (REST API)](/rest/api/searchservice/indexers/create?view=rest-searchservice-2026-05-01-preview&preserve-view=true), [Index CSV blobs and files](search-how-to-index-azure-blob-csv.md), and [Output field mappings](cognitive-search-output-field-mapping.md)
+   **Reference:** [Create Indexer (REST API)](/rest/api/searchservice/indexers/create?view=rest-searchservice-2026-08-01-preview&preserve-view=true), [Index CSV blobs and files](search-how-to-index-azure-blob-csv.md), and [Output field mappings](cognitive-search-output-field-mapping.md)
 
    The response returns HTTP `201 Created`. The indexer starts its first run automatically.
 
 1. Verify that the indexer processed both rows:
 
    ```http
-   GET <search-endpoint>/indexers/csv-indexer/status?api-version=2026-05-01-preview
+   GET <search-endpoint>/indexers/csv-indexer/status?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
-   **Reference:** [Get Indexer Status (REST API)](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Get Indexer Status (REST API)](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    Wait for `lastResult.status` to show `success` and confirm that `lastResult.itemsFailed` is `0`. If the status shows `inProgress`, wait 15 seconds and check again. You verify both CSV rows by querying the index later in this tutorial.
 
@@ -818,27 +818,27 @@ Each indexer starts its first run automatically when you create it. To start ano
 1. Run the three indexers:
 
    ```http
-   POST <search-endpoint>/indexers/docx-indexer/run?api-version=2026-05-01-preview
+   POST <search-endpoint>/indexers/docx-indexer/run?api-version=2026-08-01-preview
    Content-Type: application/json
    Content-Length: 0
    Authorization: Bearer <search-access-token>
    ```
 
    ```http
-   POST <search-endpoint>/indexers/json-indexer/run?api-version=2026-05-01-preview
+   POST <search-endpoint>/indexers/json-indexer/run?api-version=2026-08-01-preview
    Content-Type: application/json
    Content-Length: 0
    Authorization: Bearer <search-access-token>
    ```
 
    ```http
-   POST <search-endpoint>/indexers/csv-indexer/run?api-version=2026-05-01-preview
+   POST <search-endpoint>/indexers/csv-indexer/run?api-version=2026-08-01-preview
    Content-Type: application/json
    Content-Length: 0
    Authorization: Bearer <search-access-token>
    ```
 
-   **Reference:** [Run Indexer (REST API)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Run Indexer (REST API)](/rest/api/searchservice/indexers/run?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
     Each run request returns HTTP `202 Accepted` with an empty body. Some REST clients require the `Content-Length: 0` header for a request without a body.
 
@@ -848,21 +848,21 @@ Each indexer starts its first run automatically when you create it. To start ano
 1. Check the status of each indexer:
 
    ```http
-   GET <search-endpoint>/indexers/docx-indexer/status?api-version=2026-05-01-preview
+   GET <search-endpoint>/indexers/docx-indexer/status?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
    ```http
-   GET <search-endpoint>/indexers/json-indexer/status?api-version=2026-05-01-preview
+   GET <search-endpoint>/indexers/json-indexer/status?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
    ```http
-   GET <search-endpoint>/indexers/csv-indexer/status?api-version=2026-05-01-preview
+   GET <search-endpoint>/indexers/csv-indexer/status?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
-   **Reference:** [Get Indexer Status (REST API)](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Get Indexer Status (REST API)](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    For each indexer, confirm that `lastResult.status` is `success` and `lastResult.itemsFailed` is `0`. The service reports processing details in `lastResult`; verify the indexed document counts in the next section because projected chunks and parsed records don't necessarily correspond one-to-one with source blobs.
 
@@ -875,7 +875,7 @@ Use the following requests to verify the combined result.
 Return all documents written by the three indexers:
 
 ```http
-POST <search-endpoint>/indexes/multi-source-index/docs/search?api-version=2026-05-01-preview
+POST <search-endpoint>/indexes/multi-source-index/docs/search?api-version=2026-08-01-preview
 Content-Type: application/json
 Authorization: Bearer <search-access-token>
 
@@ -886,7 +886,7 @@ Authorization: Bearer <search-access-token>
 }
 ```
 
-**Reference:** [Search Documents (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Search Documents (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 The result contains two JSON products, two CSV tickets, and one or more DOCX chunks. If the sample DOCX produces one chunk, `@odata.count` is `5`. Confirm all three `sourceType` values appear: `docx`, `json`, and `csv`.
 
@@ -895,7 +895,7 @@ The result contains two JSON products, two CSV tickets, and one or more DOCX chu
 Return the two JSON products:
 
 ```http
-POST <search-endpoint>/indexes/multi-source-index/docs/search?api-version=2026-05-01-preview
+POST <search-endpoint>/indexes/multi-source-index/docs/search?api-version=2026-08-01-preview
 Content-Type: application/json
 Authorization: Bearer <search-access-token>
 
@@ -907,7 +907,7 @@ Authorization: Bearer <search-access-token>
 }
 ```
 
-**Reference:** [Search Documents (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Search Documents (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 Confirm `@odata.count` is `2`. Both results have `category` and `price` values. The `status` and `priority` fields aren't in the select list because they belong to the CSV schema.
 
@@ -916,7 +916,7 @@ Confirm `@odata.count` is `2`. Both results have `category` and `price` values.
 Full-text search considers all documents with matching searchable text, including JSON records with null vectors.
 
 ```http
-POST <search-endpoint>/indexes/multi-source-index/docs/search?api-version=2026-05-01-preview
+POST <search-endpoint>/indexes/multi-source-index/docs/search?api-version=2026-08-01-preview
 Content-Type: application/json
 Authorization: Bearer <search-access-token>
 
@@ -928,7 +928,7 @@ Authorization: Bearer <search-access-token>
 }
 ```
 
-**Reference:** [Search Documents (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Search Documents (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 Results include documents from any source type that contains "search" or "product" in their `content` or `title` fields. With the sample data, expect matches from the DOCX chunk (contains "search") and the CSV ticket (contains "product").
 
@@ -937,7 +937,7 @@ Results include documents from any source type that contains "search" or "produc
 Send text to the index vectorizer instead of pasting 1,536 vector values. The results contain vector-bearing DOCX and CSV documents, not JSON documents whose `contentVector` is null.
 
 ```http
-POST <search-endpoint>/indexes/multi-source-index/docs/search?api-version=2026-05-01-preview
+POST <search-endpoint>/indexes/multi-source-index/docs/search?api-version=2026-08-01-preview
 Content-Type: application/json
 Authorization: Bearer <search-access-token>
 
@@ -954,7 +954,7 @@ Authorization: Bearer <search-access-token>
 }
 ```
 
-**Reference:** [Search Documents (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Search Documents (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 Confirm that no results have `"sourceType": "json"`. JSON documents are excluded because their `contentVector` is null.
 
@@ -963,7 +963,7 @@ Confirm that no results have `"sourceType": "json"`. JSON documents are excluded
 Limit vector results to CSV tickets:
 
 ```http
-POST <search-endpoint>/indexes/multi-source-index/docs/search?api-version=2026-05-01-preview
+POST <search-endpoint>/indexes/multi-source-index/docs/search?api-version=2026-08-01-preview
 Content-Type: application/json
 Authorization: Bearer <search-access-token>
 
@@ -982,7 +982,7 @@ Authorization: Bearer <search-access-token>
 }
 ```
 
-**Reference:** [Search Documents (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Search Documents (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 Confirm that all results have `"sourceType": "csv"` and include the `status` and `priority` fields.
 
@@ -991,7 +991,7 @@ Confirm that all results have `"sourceType": "csv"` and include the `status` and
 Combine keyword and vector retrieval in one request:
 
 ```http
-POST <search-endpoint>/indexes/multi-source-index/docs/search?api-version=2026-05-01-preview
+POST <search-endpoint>/indexes/multi-source-index/docs/search?api-version=2026-08-01-preview
 Content-Type: application/json
 Authorization: Bearer <search-access-token>
 
@@ -1010,7 +1010,7 @@ Authorization: Bearer <search-access-token>
 }
 ```
 
-**Reference:** [Search Documents (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+**Reference:** [Search Documents (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
 Hybrid queries combine keyword matches (which can include JSON documents) with vector matches (which exclude null-vector documents). The merged result set can contain documents from all three source types when both keyword and vector terms match across pipelines.
 
@@ -1044,9 +1044,9 @@ The following table lists common issues and resolutions when running the three p
 | JSON documents appear in vector query results | The JSON indexer populated `contentVector` unexpectedly. | Confirm `json-indexer` has no `outputFieldMappings` that target `contentVector`. JSON records should leave `contentVector` null. |
 | CSV indexer fails with parsing errors | The CSV file has unescaped commas, mismatched quotes, or encoding issues. | Open the CSV file and verify that fields with commas are enclosed in double quotes. Save the file with UTF-8 encoding. |
 | Content Understanding skill fails with `403 Forbidden` | The search service's managed identity lacks access, or the resource doesn't support Content Understanding in the selected region. | Confirm the managed identity has the **Cognitive Services User** role on the Foundry resource, and confirm the resource is in a [supported region](/azure/ai-services/content-understanding/language-region-support). |
-| `"The index 'multi-source-index' was not found"` error during queries | The index wasn't created, or you sent the query to the wrong search service. | Verify `<search-endpoint>` points to the correct service. Run `GET <search-endpoint>/indexes?api-version=2026-05-01-preview` to list indexes. |
+| `"The index 'multi-source-index' was not found"` error during queries | The index wasn't created, or you sent the query to the wrong search service. | Verify `<search-endpoint>` points to the correct service. Run `GET <search-endpoint>/indexes?api-version=2026-08-01-preview` to list indexes. |
 | Run indexer request returns HTTP `411 Length Required` | The POST request has no body, and the REST client didn't send a `Content-Length` header. | Add `Content-Length: 0` to the request headers. Some REST clients require this header explicitly for POST requests with empty bodies. |
-| Re-run shows `itemsProcessed` equal to `0` | The source blobs haven't changed since the last run. | This is expected behavior. Indexers use change detection and skip unchanged blobs. To force reprocessing, reset the indexer first by sending `POST <search-endpoint>/indexers/<indexer-name>/reset?api-version=2026-05-01-preview` with `Content-Length: 0` and the bearer token header. |
+| Re-run shows `itemsProcessed` equal to `0` | The source blobs haven't changed since the last run. | This is expected behavior. Indexers use change detection and skip unchanged blobs. To force reprocessing, reset the indexer first by sending `POST <search-endpoint>/indexers/<indexer-name>/reset?api-version=2026-08-01-preview` with `Content-Length: 0` and the bearer token header. |
 
 ## Clean up resources
 
@@ -1055,80 +1055,80 @@ When you no longer need the Azure AI Search objects you created in this tutorial
 1. Delete the indexers:
 
    ```http
-   DELETE <search-endpoint>/indexers/docx-indexer?api-version=2026-05-01-preview
+   DELETE <search-endpoint>/indexers/docx-indexer?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
    ```http
-   DELETE <search-endpoint>/indexers/json-indexer?api-version=2026-05-01-preview
+   DELETE <search-endpoint>/indexers/json-indexer?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
    ```http
-   DELETE <search-endpoint>/indexers/csv-indexer?api-version=2026-05-01-preview
+   DELETE <search-endpoint>/indexers/csv-indexer?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
-   **Reference:** [Delete Indexer (REST API)](/rest/api/searchservice/indexers/delete?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Delete Indexer (REST API)](/rest/api/searchservice/indexers/delete?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    Each delete operation returns HTTP `204 No Content` on success. If you receive `404 Not Found`, the indexer was already deleted.
 
 1. Delete the skillsets:
 
    ```http
-   DELETE <search-endpoint>/skillsets/docx-semantic-skillset?api-version=2026-05-01-preview
+   DELETE <search-endpoint>/skillsets/docx-semantic-skillset?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
    ```http
-   DELETE <search-endpoint>/skillsets/csv-embedding-skillset?api-version=2026-05-01-preview
+   DELETE <search-endpoint>/skillsets/csv-embedding-skillset?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
-   **Reference:** [Delete Skillset (REST API)](/rest/api/searchservice/skillsets/delete?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Delete Skillset (REST API)](/rest/api/searchservice/skillsets/delete?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    Each delete operation returns HTTP `204 No Content` on success.
 
 1. Delete the data sources:
 
    ```http
-   DELETE <search-endpoint>/datasources/docx-blob-datasource?api-version=2026-05-01-preview
+   DELETE <search-endpoint>/datasources/docx-blob-datasource?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
    ```http
-   DELETE <search-endpoint>/datasources/json-blob-datasource?api-version=2026-05-01-preview
+   DELETE <search-endpoint>/datasources/json-blob-datasource?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
    ```http
-   DELETE <search-endpoint>/datasources/csv-blob-datasource?api-version=2026-05-01-preview
+   DELETE <search-endpoint>/datasources/csv-blob-datasource?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
-   **Reference:** [Delete Data Source (REST API)](/rest/api/searchservice/data-sources/delete?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Delete Data Source (REST API)](/rest/api/searchservice/data-sources/delete?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    Each delete operation returns HTTP `204 No Content` on success.
 
 1. Delete the index:
 
    ```http
-   DELETE <search-endpoint>/indexes/multi-source-index?api-version=2026-05-01-preview
+   DELETE <search-endpoint>/indexes/multi-source-index?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
-   **Reference:** [Delete Index (REST API)](/rest/api/searchservice/indexes/delete?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [Delete Index (REST API)](/rest/api/searchservice/indexes/delete?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    Returns HTTP `204 No Content` on success.
 
 1. Verify the indexers are removed:
 
    ```http
-   GET <search-endpoint>/indexers?api-version=2026-05-01-preview
+   GET <search-endpoint>/indexers?api-version=2026-08-01-preview
    Authorization: Bearer <search-access-token>
    ```
 
-   **Reference:** [List Indexers (REST API)](/rest/api/searchservice/indexers/list?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
+   **Reference:** [List Indexers (REST API)](/rest/api/searchservice/indexers/list?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
    Confirm that `docx-indexer`, `json-indexer`, and `csv-indexer` no longer appear in the response.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新による複数インデクサーと単一インデックスの手順改訂"
}
```

### Explanation
この変更は、複数のインデクサーを単一インデックスで扱う手順についてのドキュメントにおける、APIバージョンの更新を反映したものです。具体的には、REST APIのバージョンが「2026-05-01-preview」から「2026-08-01-preview」へと更新されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：書かれているすべてのAPI呼び出しが新しいバージョンに変更されており、これにより最新の機能や改善点をユーザーが利用できるようになります。

2. **全体的な整合性の向上**：各手順におけるAPIバージョンの一貫性が保たれ、ユーザーが手順を理解しやすくなると共に、エラーの発生を減少させることが期待されます。

3. **情報の更新**：セマンティックチャンクやインデクサーのディスカッションに関する情報も、新しいバージョンに基づいて更新され、持続可能な使用法やトラブルシューティングのガイドラインが強調されています。このような情報の更新は、ユーザーが最新の規範に従うために役立ちます。

この改訂されたドキュメントにより、ユーザーは複数のインデクサーを使用する手順をより簡単に実行できるようになり、新しいAPI機能を最大限に活用することができるようになります。これにより全体的なユーザーエクスペリエンスが向上することが期待されます。

## articles/search/search-how-to-page-list-results.md{#item-73059a}

<details>
<summary>Diff</summary>
````diff
@@ -1,202 +1,217 @@
 ---
-title: Page List API Results
-description: Learn how to page through Azure AI Search list APIs in preview, including supported operations and continuation patterns.
+title: Page Through Azure AI Search List Results
+description: Learn how to page through Azure AI Search list operations using cursor pagination and service-provided continuation URLs.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 06/02/2026
+ms.date: 08/17/2026
+ms.custom:
+  - doc-kit-assisted
+  - dev-focus
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 ---
 
-# Use paging with Azure AI Search list APIs
+# Page through Azure AI Search list results (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-Paging support in the `2026-05-01-preview` API makes Azure AI Search list operations easier to use at scale. Instead of assuming a list call returns the full collection, callers can request one page at a time, process the results, and continue until the collection is exhausted.
+Starting with the `2026-08-01-preview` REST API, use cursor pagination (preview) to enumerate supported service resources one page at a time. The service returns an opaque continuation URL when more results are available.
 
-Use paging for management tools, admin workflows, and inventory jobs that enumerate large collections of indexes, indexers, data sources, skillsets, knowledge bases, or knowledge sources.
+This article explains the cursor contract and demonstrates how to page through existing indexes.
 
 ## Prerequisites
 
-+ An [Azure AI Search service](search-create-service-portal.md) with objects to enumerate.
++ An [Azure AI Search service](search-create-service-portal.md) that contains resources for one of the supported list operations.
 
-+ Permissions to call list operations. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [API key](search-security-api-keys.md).
++ Permission to list service resources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
 ::: zone pivot="csharp"
 
 + The latest [`Azure.Search.Documents`](https://www.nuget.org/packages/Azure.Search.Documents) preview package: `dotnet add package Azure.Search.Documents --prerelease`
 
++ For keyless authentication, the [`Azure.Identity`](https://www.nuget.org/packages/Azure.Identity) package: `dotnet add package Azure.Identity`
+
+  > [!NOTE]
+  > The client library must support the `2026-08-01-preview` version of the Search Service REST API. Earlier versions don't expose the cursor parameters shown in this article.
+
 ::: zone-end
 
 ::: zone pivot="python"
 
 + The latest [`azure-search-documents`](https://pypi.org/project/azure-search-documents/#history) preview package: `pip install --pre azure-search-documents`
 
-::: zone-end
-
-::: zone pivot="rest"
++ For keyless authentication, the [`azure-identity`](https://pypi.org/project/azure-identity/) package: `pip install azure-identity`
 
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
+  > [!NOTE]
+  > The client library must support the `2026-08-01-preview` version of the Search Service REST API. Earlier versions don't expose the cursor parameters shown in this article.
 
 ::: zone-end
 
-## Choose paging parameters
+::: zone pivot="rest"
 
-Supported preview list operations accept paging parameters that control the page size, offset, and count behavior.
++ The [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) version of the Search Service REST API.
 
-| Parameter | Type | Default | Maximum | Description |
-| --- | --- | --- | --- | --- |
-| `$top` | Integer | `50` | `1000` | Number of items to retrieve in the page. |
-| `$skip` | Integer | `0` | No fixed maximum other than the number of objects in the list. | Number of items to skip before returning results. |
-| `$count` | Boolean | `false` | Not applicable | Returns the total item count when set to `true`. |
++ For keyless authentication, include a [Microsoft Entra ID token](search-get-started-rbac.md?pivots=rest#get-token) in the `Authorization` header of each HTTP request.
 
-If `$top` is omitted, the service returns up to 50 items by default. If a request asks for more than 1,000 items, the service returns at most 1,000 items in the page and includes continuation information when more items remain. Filtering and ordering parameters, such as `$filter` and `$orderby`, aren't part of this preview paging contract.
+::: zone-end
+
+## Choose a list operation
 
-For knowledge base and knowledge source list operations, the service orders resources by name before applying `$skip` and `$top`, so paging is stable across requests when the collection doesn't change.
+The `2026-08-01-preview` cursor contract applies to the following list operations:
 
-## Send the first paged request
+| Operation | Resource path |
+| --- | --- |
+| List Aliases | `/aliases` |
+| [List Data Sources](/rest/api/searchservice/data-sources/list?view=rest-searchservice-2026-08-01-preview&preserve-view=true) | `/datasources` |
+| [List Indexers](/rest/api/searchservice/indexers/list?view=rest-searchservice-2026-08-01-preview&preserve-view=true) | `/indexers` |
+| [List Indexes](/rest/api/searchservice/indexes/list?view=rest-searchservice-2026-08-01-preview&preserve-view=true) | `/indexes` |
+| List Index Statistics | `/indexstats` |
+| List Knowledge Bases | `/knowledgebases` |
+| List Knowledge Sources | `/knowledgesources` |
+| List Knowledge Source Files | `/knowledgesources('{knowledge-source-name}')/files` |
+| [List Skillsets](/rest/api/searchservice/skillsets/list?view=rest-searchservice-2026-08-01-preview&preserve-view=true) | `/skillsets` |
+| List Synonym Maps | `/synonymmaps` |
 
-The following example requests five indexes and asks the service to include the total count.
+## Request and follow pages
 
 ::: zone pivot="csharp"
 
+The following example lists indexes whose names start with `hotels` and requests up to 50 indexes per page. Iterating the `AsyncPageable<SearchIndex>` result automatically requests each subsequent page.
+
 ```csharp
+using System;
 using Azure;
+using Azure.Identity;
+using Azure.Search.Documents;
 using Azure.Search.Documents.Indexes;
+using Azure.Search.Documents.Indexes.Models;
+using Azure.Search.Documents.Models;
+
+string endpoint = Environment.GetEnvironmentVariable(
+    "AZURE_SEARCH_ENDPOINT")!;
+
+var options = new SearchClientOptions(
+    SearchClientOptions.ServiceVersion.V2026_08_01_Preview);
+var client = new SearchIndexClient(
+    new Uri(endpoint),
+    new AzureCliCredential(),
+    options);
 
-var indexClient = new SearchIndexClient(new Uri(searchEndpoint), new AzureKeyCredential(apiKey));
+AsyncPageable<SearchIndex> indexes = client.GetIndexesAsync(
+    search: "hotels",
+    pageSize: 50,
+    searchType: ListingSearchType.Prefix);
 
-var page = indexClient.GetIndexesAsync(top: 5, skip: 0).AsPages().GetAsyncEnumerator();
-await page.MoveNextAsync();
-foreach (var index in page.Current.Values)
+await foreach (SearchIndex index in indexes)
 {
     Console.WriteLine(index.Name);
 }
 ```
 
-**Reference:** [SearchIndexClient.GetIndexesAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient?view=azure-dotnet-preview&preserve-view=true)
+**Reference:** [SearchIndexClient.GetIndexesAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.getindexesasync?view=azure-dotnet-preview&preserve-view=true)
 
 ::: zone-end
 
 ::: zone pivot="python"
 
+The following example lists indexes whose names start with `hotels` and requests up to 50 indexes per page. Iterating the `ItemPaged` result automatically requests each subsequent page.
+
 ```python
-from azure.core.credentials import AzureKeyCredential
-from azure.search.documents.indexes import SearchIndexClient
+import os
 
-index_client = SearchIndexClient(endpoint="search_url", credential=AzureKeyCredential("api_key"))
+from azure.identity import AzureCliCredential
+from azure.search.documents.indexes import SearchIndexClient
 
-for index in index_client.list_indexes(top=5, skip=0):
-    print(index.name)
+endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
+
+with SearchIndexClient(
+    endpoint,
+    AzureCliCredential(),
+    api_version="2026-08-01-preview",
+) as client:
+    indexes = client.list_indexes(
+        select=["name"],
+        search="hotels",
+        page_size=50,
+        search_type="prefix",
+    )
+    for index in indexes:
+        print(index.name)
 ```
 
-**Reference:** [SearchIndexClient.list_indexes](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient)
+**Reference:** [SearchIndexClient.list_indexes](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexclient?view=azure-python-preview&preserve-view=true#azure-search-documents-indexes-searchindexclient-list-indexes)
 
 ::: zone-end
 
 ::: zone pivot="rest"
 
+Send an initial request to list indexes whose names start with `hotels`. The request returns up to 50 index names:
+
 ```http
-GET {{search-url}}/indexes?$top=5&$skip=0&$count=true&api-version=2026-05-01-preview
-Content-Type: application/json
-api-key: {{search-api-key}}
+GET https://<search-service-name>.search.windows.net/indexes?api-version=2026-08-01-preview&search=hotels&searchType=prefix&pageSize=50&$select=name
+Authorization: Bearer <access-token>
+Accept: application/json
 ```
 
-**Reference:** [List Indexes](/rest/api/searchservice/indexes/list?view=rest-searchservice-2026-05-01-preview&preserve-view=true)
-
-::: zone-end
+**Reference:** [List Indexes](/rest/api/searchservice/indexes/list?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
-The response includes the first page of values. When you specify `$top`, request subsequent pages by increasing `$skip`.
+When more than 50 matching indexes exist, the response includes `@odata.nextLink`, which contains the complete continuation URL and an opaque token. The following response is abbreviated:
 
 ```json
 {
-  "@odata.count": 43,
   "value": [
-    { "name": "index-1" },
-    { "name": "index-2" },
-    { "name": "index-3" },
-    { "name": "index-4" },
-    { "name": "index-5" }
-  ]
+    {
+      "name": "<index-name>"
+    }
+  ],
+  "@odata.nextLink": "https://<search-service-name>.search.windows.net/indexes?api-version=2026-08-01-preview&searchType=prefix&%24select=name&%24skiptoken=<opaque-token>"
 }
 ```
 
-## Continue through all pages
+To request the next page, send a GET request to the complete `@odata.nextLink` value exactly as returned. Keep the same authentication header:
 
-When you control `$top`, continue by increasing `$skip` until the response contains fewer items than requested. If the service applies the default page size because `$top` is omitted, or caps a request above the maximum page size, the response can include `@odata.nextLink` when more results remain. Treat `@odata.nextLink` as opaque when it's present.
+```http
+GET <complete-@odata.nextLink-value>
+Authorization: Bearer <access-token>
+Accept: application/json
+```
 
-::: zone pivot="csharp"
+**Reference:** [List Indexes](/rest/api/searchservice/indexes/list?view=rest-searchservice-2026-08-01-preview&preserve-view=true)
 
-The .NET SDK pages through results transparently. Iterating an `AsyncPageable<T>` fetches each page on demand, so a simple `await foreach` covers the entire collection. Set `top` to control the page size that the SDK requests from the service.
+The terminal response contains the final index names and omits `@odata.nextLink`, indicating that no more pages are available. Result order isn't part of the cursor contract:
 
-```csharp
-await foreach (var index in indexClient.GetIndexesAsync(top: 50))
+```json
 {
-    Console.WriteLine(index.Name);
+  "value": [
+    {
+      "name": "<next-index-name>"
+    }
+  ]
 }
 ```
 
 ::: zone-end
 
-::: zone pivot="python"
-
-The Python SDK pages through results transparently. Iterating the iterator returned by `list_indexes` fetches each page on demand, so a simple `for` loop covers the entire collection. Set `top` to control the page size that the SDK requests from the service.
-
-```python
-for index in index_client.list_indexes(top=50):
-    print(index.name)
-```
-
-::: zone-end
-
-::: zone pivot="rest"
-
-The following pseudocode shows the basic paging loop for REST callers:
-
-```text
-top = 50
-skip = 0
-
-while true:
-    response = GET "/indexes?$top={top}&$skip={skip}&$count=true&api-version=2026-05-01-preview"
-    process response.value
-
-    if response.value.length < top:
-        break
-
-    skip = skip + top
-```
-
-::: zone-end
-
-## Supported list operations
+## Handle cursor behavior
 
-The following list operations support paging in the preview:
++ **Detect the final page:** Continue paging only while the response contains `@odata.nextLink`. The terminal page omits this property, and responses don't include `@odata.count`.
 
-+ List Indexes
-+ List Index Statistics Summary
-+ List Synonym Maps
-+ List Indexers
-+ List Data Sources
-+ List Skillsets
-+ List Knowledge Bases
-+ List Knowledge Sources
++ **Preserve continuation state:** Use the complete `@odata.nextLink` exactly as returned. Don't construct, modify, decode, or reuse its `$skiptoken`. The token supports forward paging only.
 
-Aliases aren't included in the preview paging scope.
++ **Change request parameters:** Start a new initial request to change the resource path, API version, search prefix, selected properties, or page size. Combining `$skiptoken` with `search` or `pageSize` returns HTTP 400.
 
-Knowledge base and knowledge source list operations support `$top`, `$skip`, and `$count` in the `2026-05-01-preview` API.
++ **Account for collection changes:** Forward paging is stable only while the collection remains unchanged. Adding, updating, or deleting resources during enumeration can produce duplicate or omitted results.
 
 ## Related content
 
 + [Manage Azure AI Search using REST APIs](search-manage-rest.md)
-+ [Knowledge Sources - Create or Update](/rest/api/searchservice/knowledge-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (REST API)
-+ [Knowledge Bases - Create or Update](/rest/api/searchservice/knowledge-bases/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (REST API)
++ [Manage an index in Azure AI Search](search-how-to-manage-index.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchリスト結果のページング手法のアップデート"
}
```

### Explanation
この変更は、Azure AI SearchのリストAPIにおけるページング手法に関するドキュメントのアップデートを含んでいます。具体的には、従来のAPIバージョン「2026-05-01-preview」から新たに「2026-08-01-preview」に移行したことに伴い、ページングの方法が更新されました。

主な変更点は以下の通りです：

1. **APIのバージョン更新**：ドキュメント内で使用されるREST APIのバージョンが更新され、特に新しい機能や動作が追加されています。これにより、ユーザーは新しいページングメカニズムである「カーソルページネーション」を利用できるようになりました。

2. **ページングの新機能**：新しいAPIでは、リソースの一覧を1ページずつ列挙するためにカーソルページネーションが導入されています。この手法では、追加の結果がある場合にサービスが不透明な継続URLを返します。

3. **手順と例の更新**：ページングに関する具体的な使用例や手順が新しいバージョンに合わせて見直され、シンプルになっています。特にC#やPythonでのインデクサーの使用例が強化され、開発者にとってより実用的なリファレンスが提供されています。

4. **警告と注意書きの追加**：ユーザーが自らのアプリケーションで安全で責任あるAIの実装を行うために注意点が強調されており、テストや適切な決定の重要性が示されています。

この改訂により、ユーザーはAzure AI Searchのリスト結果をより効果的に管理・取得できるようになり、アプリケーションの構築にあたっての有用性が向上しています。さらに、最新のAPI仕様に基づく正確な情報が提供されることで、開発者が最新の機能にアクセスする際のモチベーションが高まることが期待されます。

## articles/search/search-how-to-semantic-chunking-content-understanding.md{#item-5968e6}

<details>
<summary>Diff</summary>
````diff
@@ -15,9 +15,9 @@ ai-usage: ai-assisted
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -73,7 +73,7 @@ Upload your files to the supported data source. You can use the Azure portal, RE
 The following minimal request creates the data source used throughout this walkthrough.
 
 ```http
-POST {endpoint}/datasources?api-version=2026-05-01-preview
+POST {endpoint}/datasources?api-version=2026-08-01-preview
 
 {
   "name": "my_blob_datasource",
@@ -216,7 +216,7 @@ The skillset uses `indexProjections` to map each chunk to a separate search docu
 Before you send the request, replace `<subdomain>` with your Azure OpenAI subdomain, `<Azure OpenAI api key>` with the embedding-resource key, and `<Foundry resource key>` with the key for the Foundry resource attached to the skillset.
 
 ```http
-POST {endpoint}/skillsets?api-version=2026-05-01-preview
+POST {endpoint}/skillsets?api-version=2026-08-01-preview
 
 {
   "name": "my_content_understanding_skillset",
@@ -338,7 +338,7 @@ Create and run an indexer that reads from your data source, calls the skillset,
 You don't need `outputFieldMappings` in this scenario. The `indexProjections` block in the skillset already maps each chunk to the target index fields.
 
 ```http
-POST {endpoint}/indexers?api-version=2026-05-01-preview
+POST {endpoint}/indexers?api-version=2026-08-01-preview
 
 {
   "name": "my_content_understanding_indexer",
@@ -365,7 +365,7 @@ When the indexer runs, the Content Understanding skill chunks each document, opt
 Before you query, confirm the indexer run finished:
 
 ```http
-GET {endpoint}/indexers/my_content_understanding_indexer/status?api-version=2026-05-01-preview
+GET {endpoint}/indexers/my_content_understanding_indexer/status?api-version=2026-08-01-preview
 ```
 
 Verify that `lastResult.status` is `success`. If it's `transientFailure` with `itemsProcessed` higher than `0`, the run is a partial success, and you can still query the populated chunks. For more information, see [Monitor indexer status](search-monitor-indexers.md).
@@ -377,7 +377,7 @@ Query the index to verify that the chunks contain the expected content and that
 The following request runs a hybrid query (keyword search on `chunk` and a vector query against `text_vector`) to confirm that both the chunked text and the embeddings are populated.
 
 ```http
-POST /indexes/my_content_understanding_index/docs/search?api-version=2026-05-01-preview
+POST /indexes/my_content_understanding_index/docs/search?api-version=2026-08-01-preview
 {
   "search": "copay for in-network providers",
   "count": true,
@@ -431,7 +431,7 @@ The `image_path` values stored in the index are pointers into the skill's enrich
 
 This step is optional. Add it only if your client app needs to display or download the extracted images.
 
-Add the following property to the skillset payload from the previous section. The skillset request uses `api-version=2026-05-01-preview`.
+Add the following property to the skillset payload from the previous section. The skillset request uses `api-version=2026-08-01-preview`.
 
 ```json
 "knowledgeStore": {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックチャンクとコンテンツ理解におけるAPIバージョンの更新"
}
```

### Explanation
この変更は、Azure AI Searchのセマンティックチャンクおよびコンテンツ理解に関するドキュメントのAPIバージョンを更新することに焦点を当てています。具体的には、従来のAPIバージョン「2026-05-01-preview」が、新しいバージョン「2026-08-01-preview」へと移行されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：各API呼び出しのバージョンが新しい「2026-08-01-preview」に更新されており、これにより最新の機能や改善点をユーザーが利用できるようになります。

2. **コードスニペットの更新**：データソース、スキルセット、インデクサーの作成と確認に関するHTTPリクエストのコードスニペットが、最新のAPIバージョンに合わせて修正されています。これにより、ユーザーは新しいAPIに基づいた正確な情報を得ることができます。

3. **説明文の更新**：重要な注意事項に関しても内容が更新されており、新しいAPIバージョンへの移行に伴う変更事項や、サービスの利用に関する最新の利用規約が反映されています。

4. **クライアントアプリケーションの安全性強化**：新しいバージョンでは、適切な権限やセキュリティに関するガイドラインが強調されており、データのやり取りにおけるどのような管理責任が生じるかについても明記されています。

この改訂により、ユーザーはAzure AI Searchを利用する際の最新情報を把握しやすくなり、新しい機能を効果的に活用できるようになります。これにより、全体的なドキュメントの正確さと有用性が向上し、開発者がより良いアプリケーションを構築するための基準が強化されます。

## articles/search/search-howto-managed-identities-cosmos-db.md{#item-a74464}

<details>
<summary>Diff</summary>
````diff
@@ -158,7 +158,7 @@ Follow the same steps as before to assign the appropriate roles on the control p
 Here's an example to connect to MongoDB collections using system-assigned identity via the REST API
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2026-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2026-08-01-preview
 {
     "name": "my-cosmosdb-ds",
     "type": "cosmosdb",
@@ -173,7 +173,7 @@ POST https://[service name].search.windows.net/datasources?api-version=2026-05-0
 Here's an example to connect to Gremlin graphs using user-assigned identity.
 
 ```http
-POST https://[service name].search.windows.net/datasources?api-version=2026-05-01-preview
+POST https://[service name].search.windows.net/datasources?api-version=2026-08-01-preview
 {
     "name": "[my-cosmosdb-ds]",
     "type": "cosmosdb",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cosmos DBとの接続方法に関するAPIバージョンの更新"
}
```

### Explanation
この変更は、Azure Cosmos DBと接続する際のマネージドIDを使用した方法に関するドキュメントのAPIバージョンの更新に関するものです。具体的には、前年の「2026-05-01-preview」バージョンから、新しい「2026-08-01-preview」バージョンへと更新されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：HTTPリクエストにおけるAPIバージョンが、新しい「2026-08-01-preview」に更新されており、これによりユーザーは新たな機能や改善された機能を利用できるようになります。

2. **コード例の修正**：Cosmos DBに接続するための具体的なHTTPリクエストのコード例が、最新のAPIバージョンに基づいて修正され、正確性が向上しています。マネージドIDを使った接続方法についてのサンプルリクエストが反映されています。

3. **情報の整合性維持**：この変更により、ユーザーは最新のAPIでの接続手法について正確な情報を得られるため、実装の際に誤解を招く可能性が低くなります。

このドキュメントの改訂により、開発者はAzure Cosmos DBとAzure Searchとの接続を効果的に行うことができ、最新の機能を活用しやすくなります。コード例が最新の仕様に従って更新されているため、ユーザーにとっての利便性が向上していることが期待されます。

## articles/search/search-howto-run-reset-indexers.md{#item-fb10c8}

<details>
<summary>Diff</summary>
````diff
@@ -1,4 +1,4 @@
-﻿---
+---
 title: Run or Reset Indexers
 description: Run indexers in full, or reset an indexer, skills, or individual documents to refresh all or part of a search index or knowledge store.
 ms.service: azure-ai-search
@@ -189,10 +189,10 @@ The Reset Skills request selectively processes one or more skills during the nex
 
 For indexers that have caching enabled, you can explicitly request processing for skill updates that the indexer can't detect. For example, if you make external changes, such as revisions to a custom skill, use this API to rerun the skill. The process refreshes outputs, such as a knowledge store or search index, by using reusable data from the cache and new content per the updated skill.
 
-Use the [latest preview API](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2026-05-01-preview&preserve-view=true).
+Use the [latest preview API](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2026-08-01-preview&preserve-view=true).
 
 ```http
-POST /skillsets/[skillset name]/resetskills?api-version=2026-05-01-preview
+POST /skillsets/[skillset name]/resetskills?api-version=2026-08-01-preview
 {
     "skillNames" : [
         "#1",
@@ -212,7 +212,7 @@ Remember to follow up with [Run Indexer](/rest/api/searchservice/indexers/run) t
 
 ## How to reset docs (preview)
 
-The [Indexers - Reset Docs (preview)](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2026-05-01-preview&preserve-view=true) API accepts a list of document keys so you can refresh specific documents. If you specify the reset parameters, they solely determine what gets processed, regardless of other changes in the underlying data. For example, if 20 blobs were added or updated since the last indexer run, but you only reset one document, the indexer processes only that document.
+The [Indexers - Reset Docs (preview)](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2026-08-01-preview&preserve-view=true) API accepts a list of document keys so you can refresh specific documents. If you specify the reset parameters, they solely determine what gets processed, regardless of other changes in the underlying data. For example, if 20 blobs were added or updated since the last indexer run, but you only reset one document, the indexer processes only that document.
 
 On a per-document basis, the indexer refreshes all fields in the search document with values and metadata from the data source. You can't pick and choose which fields to refresh. 
 
@@ -222,12 +222,12 @@ If you enrich the document through a skillset and it has cached data, the indexe
 
 When you're testing this API for the first time, the following APIs can help you validate and test the behaviors. Use the latest preview API.
 
-1. Call [Indexers - Get Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&preserve-view=true) with a preview API version to check reset status and execution status. You can find information about the reset request at the end of the status response.
+1. Call [Indexers - Get Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&preserve-view=true) with a preview API version to check reset status and execution status. You can find information about the reset request at the end of the status response.
 
-1. Call [Indexers - Reset Docs](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2026-05-01-preview&preserve-view=true) with a preview API version to specify which documents to process.
+1. Call [Indexers - Reset Docs](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2026-08-01-preview&preserve-view=true) with a preview API version to specify which documents to process.
 
     ```http
-    POST https://[service name].search.windows.net/indexers/[indexer name]/resetdocs?api-version=2026-05-01-preview
+    POST https://[service name].search.windows.net/indexers/[indexer name]/resetdocs?api-version=2026-08-01-preview
     {
         "documentKeys" : [
             "1001",
@@ -257,7 +257,7 @@ When you're testing this API for the first time, the following APIs can help you
 If you call the Reset Documents API multiple times with different keys, the new keys are added to the list of document keys reset. If you call the API with the **`overwrite`** parameter set to true, the current list is replaced with the new one:
 
 ```http
-POST https://[service name].search.windows.net/indexers/[indexer name]/resetdocs?api-version=2026-05-01-preview
+POST https://[service name].search.windows.net/indexers/[indexer name]/resetdocs?api-version=2026-08-01-preview
 {
     "documentKeys" : [
         "200",
@@ -271,7 +271,7 @@ POST https://[service name].search.windows.net/indexers/[indexer name]/resetdocs
 
 ## How to resync indexers (preview)
 
-[Resync Indexers](/rest/api/searchservice/indexers/resync?view=rest-searchservice-2026-05-01-preview&preserve-view=true) is a preview REST API that performs a partial reindex of all documents.
+[Resync Indexers](/rest/api/searchservice/indexers/resync?view=rest-searchservice-2026-08-01-preview&preserve-view=true) is a preview REST API that performs a partial reindex of all documents.
 An indexer is considered synchronized with its data source when specific fields of all documents in the target index are consistent with the data in the data source. Typically, an indexer achieves synchronization after a successful initial run. If you delete a document from the data source, the indexer remains synchronized according to this definition. However, during the next indexer run, the corresponding document in the target index is removed if delete tracking is enabled.
 
 If you modify a document in the data source, the indexer becomes unsynchronized. Generally, change tracking mechanisms resynchronize the indexer during the next run. For example, in Azure Storage, modifying a blob updates its last modified time, so the indexer can reindex it in the subsequent indexer run because the updated time surpasses the high-water mark set by the previous run.
@@ -284,10 +284,10 @@ Resync Indexers offers an efficient and convenient alternative. You simply place
 
 ### How to resync and run indexers
 
-1. Call [Indexers - Resync](/rest/api/searchservice/indexers/resync?view=rest-searchservice-2026-05-01-preview&preserve-view=true) with a preview API version to specify what content to re-synchronize.
+1. Call [Indexers - Resync](/rest/api/searchservice/indexers/resync?view=rest-searchservice-2026-08-01-preview&preserve-view=true) with a preview API version to specify what content to re-synchronize.
 
     ```http
-    POST https://[service name].search.windows.net/indexers/[indexer name]/resync?api-version=2026-05-01-preview
+    POST https://[service name].search.windows.net/indexers/[indexer name]/resync?api-version=2026-08-01-preview
     {
         "options" : [
             "permissions"
@@ -304,7 +304,7 @@ Resync Indexers offers an efficient and convenient alternative. You simply place
 
 To check the reset status and see which document keys are queued for processing, follow these steps:
 
-1. Call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&preserve-view=true) by using a preview API. 
+1. Call [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&preserve-view=true) by using a preview API.
 
    The preview API returns the **`currentState`** section, found at the end of the response.
 
@@ -340,7 +340,7 @@ This section applies to Standard 3 High Density (S3 HD) and Serverless search se
 
 Each indexer run has a two-hour maximum. Separately, all indexers share 24 hours of cumulative runtime per service in each 24-hour UTC window.
 
-To help you monitor indexer running times relative to the 24-hour window, [Get Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics?view=rest-searchservice-2026-05-01-preview&preserve-view=true#servicestatistics) and [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-05-01-preview&preserve-view=true) now return more information in the response.
+To help you monitor indexer running times relative to the 24-hour window, [Get Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics?view=rest-searchservice-2026-08-01-preview&preserve-view=true#servicestatistics) and [Get Indexer Status](/rest/api/searchservice/indexers/get-status?view=rest-searchservice-2026-08-01-preview&preserve-view=true) now return more information in the response.
 
 ### Track cumulative runtime quota
 
@@ -349,7 +349,7 @@ Track a search service's cumulative indexer runtime usage and determine how much
 Send a GET request to the search service endpoint. For help with setting up a REST client and getting an access token, see [Connect to a search service](/azure/search/search-get-started-rbac?pivots=rest).
 
 ```http
-GET {{search-endpoint}}/servicestats?api-version=2026-05-01-preview 
+GET {{search-endpoint}}/servicestats?api-version=2026-08-01-preview
   Content-Type: application/json
   Authorization: Bearer {{accessToken}}
 ```
@@ -361,7 +361,7 @@ Responses include `indexersRuntime` properties that show the window start and en
 Return the same information for a single indexer.
 
 ```http
-GET {{search-endpoint}}/indexers/hotels-sample-indexer/search.status?api-version=2026-05-01-preview 
+GET {{search-endpoint}}/indexers/hotels-sample-indexer/search.status?api-version=2026-08-01-preview
   Content-Type: application/json
   Authorization: Bearer {{accessToken}}
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーのリセットと実行に関するAPIバージョンの更新"
}
```

### Explanation
この変更は、Azure検索サービスにおけるインデクサーのリセットおよび実行方法に関するドキュメント内のAPIバージョンを更新することを目的としています。具体的には、旧バージョンの「2026-05-01-preview」から新しいバージョン「2026-08-01-preview」へと移行されています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：ドキュメント内のすべてのAPIリクエストが、新しいAPIバージョンに合わせて修正されています。これにより、ユーザーは最新の機能と最適化されたプロセスを利用できるようになります。

2. **コードスニペットの修正**：各リクエストのコード例が、新しいAPIバージョンに基づいて更新されています。これには、スキルのリセット、ドキュメントのリセット、およびインデクサーの再同期に関する具体的なPOSTリクエストが含まれています。

3. **情報の最新化**：各APIの説明も、最新のバージョンに合わせて更新されており、APIの利用方法や期待される動作に関する明確で正確な情報が提供されています。

4. **処理フローの明確化**：インデクサーのリセットや再同期のための手順が整理されており、開発者がこれらのAPIを使用する際の理解が深まるように配慮されています。

このドキュメントの更新により、開発者はAzure検索サービスのインデクサーを効果的に管理し、最新のAPIを活用したアプリケーションの開発が行いやすくなります。正確で最新の情報が提供されることで、ユーザーは実装の際の誤解を避け、よりスムーズな操作が可能になることが期待されます。

## articles/search/search-index-access-control-lists-and-rbac-push-api.md{#item-45e71e}

<details>
<summary>Diff</summary>
````diff
@@ -13,17 +13,17 @@ ai-usage: ai-assisted
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-Indexing documents, along with their associated [access control lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control) and container [role-based access control (RBAC) roles](/azure/role-based-access-control/overview), into an Azure AI Search index via the [push REST APIs](/rest/api/searchservice/documents/?view=rest-searchservice-2026-05-01-preview&preserve-view=true) preserves document-level permission on indexed content at query time.
+Indexing documents, along with their associated [access control lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control) and container [role-based access control (RBAC) roles](/azure/role-based-access-control/overview), into an Azure AI Search index via the [push REST APIs](/rest/api/searchservice/documents/?view=rest-searchservice-2026-08-01-preview&preserve-view=true) preserves document-level permission on indexed content at query time.
 
 Key features include:
 
@@ -37,7 +37,7 @@ This article explains how to use the push REST API to index document-level permi
 
 - Content with ACL metadata from [Microsoft Entra ID](/entra/fundamentals/whatis) or another POSIX-style ACL system. For `userIds` and `groupIds` ACL fields, use Microsoft Entra object IDs (GUIDs), not UPNs or email addresses. Stable object IDs ensure reliable identity matching at query time, even if directory attributes change.
 
-- The [latest preview REST API](/rest/api/searchservice/documents/?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or a preview Azure SDK package providing equivalent features.
+- The [latest preview REST API](/rest/api/searchservice/documents/?view=rest-searchservice-2026-08-01-preview&preserve-view=true) or a preview Azure SDK package providing equivalent features.
 
 - An index schema with `permissionFilterOption` enabled, plus `permissionFilter` field attributes that store document permissions.
 
@@ -86,7 +86,7 @@ For enterprise repositories, such as SharePoint Online, resolve document-level o
 Once you have an index with permission-filter fields, you can populate those values using the push indexing API, just like any other document fields. Here's an example using the specified index schema, where each document specifies the indexing action, key field (`DocumentId`), and permission fields. Documents should also include content, but that field is omitted in this example for brevity.
 
 ```https
-POST https://exampleservice.search.windows.net/indexes('indexdocumentsexample')/docs/search.index?api-version=2026-05-01-preview
+POST https://exampleservice.search.windows.net/indexes('indexdocumentsexample')/docs/search.index?api-version=2026-08-01-preview
 {
   "value": [
     {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACおよびACLを使用したインデクシングAPIのバージョン更新"
}
```

### Explanation
この変更は、Azure検索サービスにおけるインデクシング時のアクセス制御リスト（ACL）および役割ベースアクセス制御（RBAC）の機能に関するドキュメントにおいて、使用されるREST APIのバージョンを2026-05-01-previewから2026-08-01-previewに更新するものです。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：すべての関連するAPI呼び出しが新しい2026-08-01-previewバージョンに適合しています。これにより、ユーザーは最新の機能や改善点を利用可能になります。

2. **重要なお知らせの更新**：重要な警告文が更新されており、サービスの利用に関する条件が新しいAPIバージョンに対応しています。これにより、ユーザーは使用するAPIがもたらす影響やリスクを把握することができます。

3. **コード例の修正**：ドキュメント内のHTTPリクエストの例が新しいAPIバージョンに基づいて修正されており、正しいバージョンを指定してリクエストを実行できるようになっています。

4. **詳細な使用方法の明示**：APIを通じて文書をインデクシングする際のACLおよびRBACに関する内容が強調されています。これにより、ユーザーは文書レベルの権限を保持しながらインデクシングを行う手法についてさらに理解を深めることができます。

この更新により、開発者はAzure検索サービスを通じてのインデクシング機能をより効果的に利用でき、最新の条件に基づいてアプリケーションを構築することが容易になります。情報が正確であり、最新のAPIに準拠しているため、ユーザーは信頼性の高い実装を行うことが期待されます。

## articles/search/search-indexer-access-control-lists-and-role-based-access.md{#item-67b42f}

<details>
<summary>Diff</summary>
````diff
@@ -13,11 +13,11 @@ ai-usage: ai-assisted
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -156,7 +156,7 @@ Key points about the configuration that make it work for this scenario:
 ```http
 # Create / Update Azure Blob Knowledge Source
 ###
-PUT {{url}}/knowledgesources/azure-blob-ks?api-version=2026-05-01-preview
+PUT {{url}}/knowledgesources/azure-blob-ks?api-version=2026-08-01-preview
 api-key: {{key}}
 Content-Type: application/json
  
@@ -332,7 +332,7 @@ Choose one of the following mechanisms, depending on how many items changed:
 **Resetdocs (preview) API example:**
 
    ```http
-   POST https://{service}.search.windows.net/indexers/{indexer}/resetdocs?api-version=2026-05-01-preview 
+   POST https://{service}.search.windows.net/indexers/{indexer}/resetdocs?api-version=2026-08-01-preview
    { 
      "documentKeys": [ 
        "1001", 
@@ -344,7 +344,7 @@ Choose one of the following mechanisms, depending on how many items changed:
 **Resync (preview) API example:**
 
    ```http
-   POST https://{service}.search.windows.net/indexers/{indexer}/resync?api-version=2026-05-01-preview 
+   POST https://{service}.search.windows.net/indexers/{indexer}/resync?api-version=2026-08-01-preview
    { 
      "options": [ 
        "permissions" 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACおよびACLに関するインデクサーAPIのバージョン更新"
}
```

### Explanation
この変更は、Azure検索サービスのインデクサーにおけるアクセス制御リスト（ACL）および役割ベースのアクセス制御（RBAC）に関連するドキュメントを更新するもので、APIのバージョンを2026-05-01-previewから2026-08-01-previewに更新しています。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：すべての関連するAPI呼び出しが新しい2026-08-01-previewバージョンに適合しており、これにより開発者はより新しい機能や改善点を利用できるようになります。

2. **重要なお知らせの修正**：ドキュメント内の重要な通知が、APIの新しいバージョンに基づいて更新されています。この通知には、利用条件や、他のMicrosoftサービスとの接続に関する情報が含まれています。

3. **HTTPリクエスト例の修正**：API呼び出しのコード例が、更新されたAPIバージョンに基づいて修正されています。具体的には、Azure Blob Knowledge Sourceの作成や更新、ドキュメントのリセット、再同期に関するAPIリクエストが新しいバージョンに修正されています。

4. **アクセス権限に関する注意点**：新しいバージョンでも、外部で設定されたアクセス権を変更することができない点や、権限制限のあるコンテンツでの遅延情報が強調されています。

この更新により、開発者はAzure検索サービス内の機能をより効果的に利用でき、最新のAPIを活用したアプリケーションの開発が行いやすくなります。また、正確な情報が提供されることで、ユーザーは実装時の誤解を避けることができ、よりスムーズに開発を進めることが期待されます。

## articles/search/search-indexer-high-density-serverless-overview.md{#item-2bc606}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ The execution model in this article applies to:
 + [Serverless search services](serverless-cost-optimization.md) that run indexers by using the `2026-05-01-preview` REST API or later.
 + S3 HD search services that run indexers by using the `2025-11-01-preview` REST API or later.
 
-Supported indexer definitions, data sources, skillsets, and indexer-backed knowledge sources work without modification on both options. File knowledge sources aren't supported on Serverless.
+Supported indexer definitions, data sources, skillsets, and indexer-backed knowledge sources work without modification on both options.
 
 ## Execution model
 
@@ -91,7 +91,7 @@ This section explains how to track runtime usage and remaining budget using the
 Use [Get Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics) (REST API) to retrieve cumulative indexer runtime across all indexers in the service for the current 24-hour window:
 
 ```http
-GET {endpoint}/servicestats?api-version=2026-05-01-preview
+GET {endpoint}/servicestats?api-version=2026-08-01-preview
 ```
 
 The response includes an `indexersRuntime` section. The following JSON shows a service whose 24-hour daily quota isn't used:
@@ -116,7 +116,7 @@ The response includes an `indexersRuntime` section. The following JSON shows a s
 Use [Get Indexer Status](/rest/api/searchservice/indexers/get-status) (REST API) to retrieve cumulative runtime for an individual indexer:
 
 ```http
-GET {endpoint}/indexers('{indexerName}')/search.status?api-version=2026-05-01-preview
+GET {endpoint}/indexers('{indexerName}')/search.status?api-version=2026-08-01-preview
 ```
 
 The response includes a `runtime` section. The following JSON shows an indexer on a service whose 24-hour daily quota isn't used:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "高密度サーバーレスインデクサーに関するAPIバージョン更新"
}
```

### Explanation
この変更は、Azureの高密度サーバーレスインデクサーに関するドキュメントを更新し、使用するREST APIのバージョンを2026-05-01-previewから2026-08-01-previewに更新するものです。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：インデクサーの実行モデルに関する記述が修正され、新しいAPIバージョンがリファレンスされています。これにより、最新の機能や改善点を反映した情報が提供されています。

2. **サポート対象の明示**：サポートされるインデクサー定義、データソース、スキルセット、インデクサーに基づくナレッジソースは、どちらのオプションでも変更なく機能すると確認されています。

3. **HTTPリクエスト例の修正**：ドキュメント内のHTTPリクエスト例が新しいAPIバージョンに基づいて更新されています。具体的には、サービス統計の取得およびインデクサーの状態の取得に際して、新しいAPIバージョンが指定されています。

この更新により、開発者は高密度サーバーレスインデクサーの利用に関する最新情報を得られ、APIを使用した開発がより円滑に行えるようになります。また、正確な情報の提供により、ユーザーが実装する際の混乱を軽減し、最新の環境での作業をサポートします。

## articles/search/search-indexer-sensitivity-labels.md{#item-2a7bfc}

<details>
<summary>Diff</summary>
````diff
@@ -13,11 +13,11 @@ ai-usage: ai-assisted
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag occurs before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag occurs before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data flows outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -46,7 +46,7 @@ This functionality is available for the following data sources:
 
 + Use source documents with file types that are both [supported by Purview sensitivity labels](/purview/sensitivity-labels-sharepoint-onedrive-files#supported-file-types) and [supported by Azure AI Search indexers](search-how-to-index-azure-blob-storage.md#supported-document-formats).
 
-+ Use REST API version 2026-05-01-preview or an equivalent preview SDK package.
++ Use REST API version 2026-08-01-preview or an equivalent preview SDK package.
 
 > [!IMPORTANT]
 > The search service must use its **system-assigned managed identity** to authenticate with Microsoft Purview. This feature doesn't support user-assigned managed identities.
@@ -90,7 +90,7 @@ When you configure indexing [on a schedule](search-howto-schedule-indexers.md),
 
 At query time, Azure AI Search evaluates sensitivity labels and enforces [document-level access control](search-document-level-access-overview.md) based on the user's Microsoft Entra ID token and Microsoft Purview label policies. Only users authorized to access content with [READ usage right](/purview/rights-management-usage-rights) under a given label can retrieve corresponding documents in search results.
 
-Authorized administrators can also issue [elevated read](search-query-sensitivity-labels.md#elevated-read-for-administrative-investigations-preview) requests, which return labeled documents that the calling user wouldn't normally see and emit a Microsoft Purview audit log entry for every document returned. Elevated read requires the **Search Index Data Contributor** role on the search service and the 2026-05-01-preview API version.
+Authorized administrators can also issue [elevated read](search-query-sensitivity-labels.md#elevated-read-for-administrative-investigations-preview) requests, which return labeled documents that the calling user wouldn't normally see and emit a Microsoft Purview audit log entry for every document returned. Elevated read requires the **Search Index Data Contributor** role on the search service and API version 2026-05-01-preview or later.
 
 ### End-to-end example
 
@@ -178,7 +178,7 @@ The appID roles in the provided PowerShell script are associated to the followin
 
 ## 4. Configure the index to enable Purview sensitivity label 
 
-When sensitivity label support is required, set the `purviewEnabled` property to `true` in your [index definition](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true).
+When sensitivity label support is required, set the `purviewEnabled` property to `true` in your [index definition](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true).
 
 > [!IMPORTANT]
 > The `purviewEnabled` property must be set to `true` when the index is created. This setting is permanent and can't be modified later.
@@ -188,7 +188,7 @@ When sensitivity label support is required, set the `purviewEnabled` property to
 API key access is limited to index schema retrieval (list and get).
 
 ```
-PUT https://{service}.search.windows.net/indexes('{indexName}')?api-version=2026-05-01-preview
+PUT https://{service}.search.windows.net/indexes('{indexName}')?api-version=2026-08-01-preview
 {
   "purviewEnabled": true,
   "fields": [
@@ -205,7 +205,7 @@ PUT https://{service}.search.windows.net/indexes('{indexName}')?api-version=2026
 
 ## 5. Configure the data source
 
-To enable sensitivity label ingestion, configure the [data source](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) with the indexerPermissionOptions property set to ["sensitivityLabel"]. 
+To enable sensitivity label ingestion, configure the [data source](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) with the indexerPermissionOptions property set to ["sensitivityLabel"].
 
 ```
 {
@@ -225,14 +225,14 @@ The `indexerPermissionOptions` property instructs the indexer to extract sensiti
 
 ## 6. Configure index projections in your skillset (if applicable)
 
-If your indexer has a [skillset](cognitive-search-working-with-skillsets.md) and you're implementing data chunking through the [Text Split skill](cognitive-search-skill-textsplit.md), such as with integrated vectorization, project the sensitivity label onto each chunk via [index projections in the skillset](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true).
+If your indexer has a [skillset](cognitive-search-working-with-skillsets.md) and you're implementing data chunking through the [Text Split skill](cognitive-search-skill-textsplit.md), such as with integrated vectorization, project the sensitivity label onto each chunk via [index projections in the skillset](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true).
 
 For the broader rule on when permission and ACL fields belong in indexer field mappings versus index projections, see [Choose where to populate ACL fields](search-indexer-sharepoint-access-control-lists.md#choose-where-to-populate-acl-fields).
 
 This step is required for both query-time enforcement and for [agentic retrieval](agentic-retrieval-overview.md) responses to include per-document `sensitivityLabelInfo` for each chunk. Without the projection mapping, child chunk rows won't be filtered correctly.
 
 ```
-PUT https://{service}.search.windows.net/skillsets/{skillset}?api-version=2026-05-01-preview
+PUT https://{service}.search.windows.net/skillsets/{skillset}?api-version=2026-08-01-preview
 {
   "name": "my-skillset",
   "skills": [
@@ -269,7 +269,7 @@ PUT https://{service}.search.windows.net/skillsets/{skillset}?api-version=2026-0
 
 ## 7. Configure the indexer
 
-- Define field mappings in your [indexer definition](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) to route extracted label metadata to the index fields.
+- Define field mappings in your [indexer definition](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) to route extracted label metadata to the index fields.
 If your data source emits label metadata under a different field name (for example, `metadata_sensitivity_label`), map it explicitly.
 
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "感度ラベル機能のAPIバージョン更新"
}
```

### Explanation
この変更は、Azureの検索インデクサーにおける感度ラベル機能に関するドキュメントを更新し、使用するREST APIのバージョンを2026-05-01-previewから2026-08-01-previewに更新するものです。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：重要な機能や通知が、最新のAPIバージョンに合わせて修正されています。これによりユーザーは最新の機能にアクセスでき、正確な情報が提供されます。

2. **機能に関する注意事項の修正**：各APIリクエストのURLに新しいバージョンが反映されており、感度ラベルの処理がAPIのバージョンに応じて正しく動作することが保証されています。

3. **REST APIリクエスト例の修正**：ドキュメント内で示されるサンプルリクエストが新しいバージョンに基づいて更新されています。これには、インデックスの作成や更新、スキルセットの設定に関連するリクエストが含まれています。

4. **管理者による特権読取の説明の修正**：特権読取リクエストの要件が最新のAPIバージョンに基づいて更新されています。これにより、権限のある管理者が正しく機能を利用できるようになっています。

この更新により、開発者は感度ラベルに関連する機能を最新のAPIを使用して適切に実装でき、ユーザーはエラーを避けてスムーズに作業を進めることができるようになります。また、最新の業界基準に従った情報を得ることで、ユーザーはサポート体制の恩恵を受けることが期待されます。

## articles/search/search-indexer-sharepoint-access-control-lists.md{#item-532a24}

<details>
<summary>Diff</summary>
````diff
@@ -14,11 +14,11 @@ ms.custom: doc-kit-assisted
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -41,7 +41,7 @@ This article explains how to ingest an access control list (ACL) alongside other
 
 + Configure Microsoft Entra application permissions and a credential appropriate for your scenario. See [Permissions by ACL scenario](#permissions-by-acl-scenario). ACL ingestion requires application permissions. Delegated permissions aren't supported. For the application vs delegated decision, see [Choose your permissions setup](search-how-to-index-sharepoint-online.md#choose-your-permissions-setup).
 
-+ REST API version 2026-05-01-preview or an equivalent preview SDK package.
++ REST API version 2026-08-01-preview or an equivalent preview SDK package.
 
 ## Limitations
 
@@ -227,10 +227,10 @@ Set `retrievable` attribute to `true` only during development to verify values.
 
 When chunking is enabled, the parent document isn't written to the index when `projectionMode` is `skipIndexingParentDocuments`. Carry the ACL metadata onto each chunk through `indexProjections.selectors[].mappings`.
 
-If your indexer uses a [skillset](cognitive-search-working-with-skillsets.md) with data chunking, such as the [Text Split skill](cognitive-search-skill-textsplit.md) when enabling [integrated vectorization](vector-search-integrated-vectorization.md), make sure to map ACL properties to each chunk using [index projections](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true). The `//` lines in the following example are illustrative annotations and aren't valid JSON. Remove them before submitting the request.
+If your indexer uses a [skillset](cognitive-search-working-with-skillsets.md) with data chunking, such as the [Text Split skill](cognitive-search-skill-textsplit.md) when enabling [integrated vectorization](vector-search-integrated-vectorization.md), make sure to map ACL properties to each chunk using [index projections](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true). The `//` lines in the following example are illustrative annotations and aren't valid JSON. Remove them before submitting the request.
 
 ```http
-PUT https://{service}.search.windows.net/skillsets/{skillset}?api-version=2026-05-01-preview
+PUT https://{service}.search.windows.net/skillsets/{skillset}?api-version=2026-08-01-preview
 {
   "name": "my-skillset",
   "skills": [
@@ -289,7 +289,7 @@ Besides your required [indexer configuration](search-how-to-index-sharepoint-onl
 ACL metadata is ingested when the indexer runs. After you create or update the indexer (see [Step 6: Create an indexer](search-how-to-index-sharepoint-online.md#step-6-create-an-indexer)), trigger a run so the indexer ingests ACLs alongside content.
 
 ```http
-POST https://[service name].search.windows.net/indexers/[indexer-name]/run?api-version=2026-05-01-preview
+POST https://[service name].search.windows.net/indexers/[indexer-name]/run?api-version=2026-08-01-preview
 api-key: [admin key]
 ```
 
@@ -332,7 +332,7 @@ The following components work together to enable SharePoint site group resolutio
 Add the `sharePointConnectorAppRegistration` configuration and the `SharePointSiteUrl` field alongside the `UserIds` and `GroupIds` permission-filter fields, so the full index shape is in one place. Keep `permissionFilterOption: "enabled"`.
 
 ```http
-PUT https://{service}.search.windows.net/indexes/{index}?api-version=2026-05-01-preview
+PUT https://{service}.search.windows.net/indexes/{index}?api-version=2026-08-01-preview
 {
   "name": "my-sharepoint-acl-index",
   "sharePointConnectorAppRegistration": {
@@ -391,21 +391,21 @@ Some scenarios still require an explicit refresh:
 
 ### Reset specific documents
 
-You can [reset specific documents](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2026-05-01-preview&preserve-view=true) to fully ingest again content and ACLs.
+You can [reset specific documents](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2026-08-01-preview&preserve-view=true) to fully ingest again content and ACLs.
 
 ```http
-POST https://{service}.search.windows.net/indexers/{indexer}/resetdocs?api-version=2026-05-01-preview
+POST https://{service}.search.windows.net/indexers/{indexer}/resetdocs?api-version=2026-08-01-preview
 {
   "documentKeys": ["doc123", "doc456"]
 }
 ```
 
 ### Resync ACLs across the full data source
 
-You can [resync the full data set ACL content](/rest/api/searchservice/indexers/resync?view=rest-searchservice-2026-05-01-preview&preserve-view=true) after initial ingestion. To fully succeed, this operation requires an [indexer run](search-howto-run-reset-indexers.md) after completion. 
+You can [resync the full data set ACL content](/rest/api/searchservice/indexers/resync?view=rest-searchservice-2026-08-01-preview&preserve-view=true) after initial ingestion. To fully succeed, this operation requires an [indexer run](search-howto-run-reset-indexers.md) after completion.
 
 ```http
-POST https://{service}.search.windows.net/indexers/{indexer}/resync?api-version=2026-05-01-preview
+POST https://{service}.search.windows.net/indexers/{indexer}/resync?api-version=2026-08-01-preview
 {
   "options": ["permissions"]
 }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointアクセス制御リストに関するAPIバージョン更新"
}
```

### Explanation
この変更は、Azureの検索インデクサーに関する文書を更新し、SharePointアクセス制御リスト（ACL）の機能に関連するREST APIのバージョンを2026-05-01-previewから2026-08-01-previewに更新するものです。

主な変更点は以下の通りです：

1. **APIバージョンの更新**：重要な機能や情報が、最新のREST APIバージョンに合わせて修正されています。これにより、ユーザーは最新のAPIを使用して正確かつ最新の機能にアクセスできるようになります。

2. **重要な注意事項の更新**：ドキュメント内の各セクションにおいて、APIバージョンが新しいものに変更され、それに伴う利用条件や制限に関する説明も更新されています。

3. **HTTPリクエスト例の修正**：インデックスやインデクサーの作成・更新、特定の文書のリセットなどの操作をサポートするために、示されるHTTPリクエストのサンプルが新しいAPIバージョンに基づいて更新されています。

4. **ACLの関連情報の明示化**：ACLの取り扱いに関する操作が新しいバージョンを反映しており、ユーザーは機能を使用する際に最新の情報と手順に従えるようになっています。

この更新により、開発者はSharePointアクセス制御リストをインデクサーで効果的に管理できるようになり、ユーザーはエラーを回避し、スムーズに作業を進めることができると期待されます。また、最新のAPIに基づいた正確な情報を提供することにより、ユーザーは安全かつ効果的に感度情報の管理が可能になります。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -263,7 +263,7 @@ The maximum source-file size and extracted-character limits in the following tab
 
 <sup>3</sup> When using `delimitedText` parsing mode for CSV files, the “maximum extracted content size” limit doesn't apply.
 
-<sup>4</sup> Blob-like indexers include the Azure Blob Storage indexer (blob indexer), ADLS Gen2 indexer, SharePoint in Microsoft 365 indexer, OneLake indexer, and Azure Files indexer. The direct-upload file knowledge source doesn't use an indexer and has [separate limits](agentic-knowledge-source-how-to-file.md#supported-formats-and-limits).
+<sup>4</sup> Blob-like indexers include the Azure Blob Storage indexer (blob indexer), ADLS Gen2 indexer, SharePoint in Microsoft 365 indexer, OneLake indexer, and Azure Files indexer. The direct-upload file knowledge source doesn't use an indexer and has [separate limits](agentic-knowledge-source-how-to-file.md#file-support-and-limits).
 
 ## Shared private link resource limits
 
@@ -326,11 +326,11 @@ A [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) specifies
 
 ### Knowledge sources per knowledge base
 
-Per-knowledge-base limits on knowledge sources depend on the API version used to create or update the knowledge base. In the `2026-05-01-preview`, all retrieval reasoning efforts support the same knowledge source limits. Earlier preview API versions have lower limits for `low` and `medium` reasoning efforts.
+Per-knowledge-base limits on knowledge sources depend on the API version used to create or update the knowledge base. In `2026-05-01-preview` and later, all retrieval reasoning efforts support the same knowledge source limits. Earlier preview API versions have lower limits for `low` and `medium` reasoning efforts.
 
 | API version | Retrieval reasoning effort | Free | Basic | S1 | S2 | S3 | S3 HD | L1 | L2 |
 |--|--|--|--|--|--|--|--|--|--|
-| `2026-05-01-preview` | `minimal`, `low`, `medium` | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 0 | 10 | 10 |
+| `2026-05-01-preview` and later | `minimal`, `low`, `medium` | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 0 | 10 | 10 |
 | `2026-05-01-preview`, `2025-08-01-preview` | `minimal` <sup>2</sup> | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 0 | 10 | 10 |
 | `2026-05-01-preview`, `2025-08-01-preview` | `low` | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 |
 | `2026-05-01-preview`, `2025-08-01-preview` | `medium` | 3 | 5 | 5 | 5 | 5 | 0 | 5 | 5 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索の制限、クォータ、容量に関する文書の更新"
}
```

### Explanation
この変更は、Azureの検索機能に関連する文書を更新し、特に制限、クォータ、容量に関する情報の明確化を目的としています。主な変更点は以下の通りです：

1. **引用情報の更新**：文書内の引用情報が変更され、特定の制限に関する説明が最新の内容に基づいて修正されています。例えば、Blobライクインデクサーの説明がより明確になりました。

2. **APIバージョンの明記の修正**：APIバージョンに関連する記述が更新されており、2026-05-01-preview以降のAPIバージョンにおいて、知識ベースごとの知識ソースの制限が統一されていることが明記されています。この変更により、過去のAPIバージョンとの比較が容易になります。

3. **テーブルの更新**：知識ベースの制限に関するテーブルが最新のもので修正され、APIバージョンに応じた制限が明確に示されています。これにより、ユーザーは異なるプランやAPIバージョンに対する制限を簡単に参照することができます。

この更新は、Azureの検索機能を利用する開発者やユーザーが、特定の制約条件を把握しやすくするためのものであり、明確な情報提供を通じて作業を効率化し、簡潔な利用の促進を図ることが期待されます。

## articles/search/search-more-like-this.md{#item-56c565}

<details>
<summary>Diff</summary>
````diff
@@ -31,14 +31,14 @@ All following examples use the hotels sample from [Quickstart: Full-text search
 The following query finds documents whose description fields are most similar to the field of the source document as specified by the `moreLikeThis` parameter:
 
 ```http
-GET /indexes/hotels-sample/docs?moreLikeThis=29&searchFields=Description&api-version=2026-05-01-preview
+GET /indexes/hotels-sample/docs?moreLikeThis=29&searchFields=Description&api-version=2026-08-01-preview
 ```
 
 In this example, the request searches for hotels similar to the one with `HotelId` 29.
 Rather than using HTTP GET, you can also invoke `MoreLikeThis` using HTTP POST:
 
 ```http
-POST /indexes/hotels-sample/docs/search?api-version=2026-05-01-preview
+POST /indexes/hotels-sample/docs/search?api-version=2026-08-01-preview
     {
       "moreLikeThis": "29",
       "searchFields": "Description"
@@ -50,15 +50,15 @@ POST /indexes/hotels-sample/docs/search?api-version=2026-05-01-preview
 `MoreLikeThis` can be combined with other common query parameters like `$filter`. For instance, the query can be restricted to only hotels whose category is 'Budget' and where the rating is higher than 3.5:
 
 ```http
-GET /indexes/hotels-sample/docs?moreLikeThis=20&searchFields=Description&$filter=(Category eq 'Budget' and Rating gt 3.5)&api-version=2026-05-01-preview
+GET /indexes/hotels-sample/docs?moreLikeThis=20&searchFields=Description&$filter=(Category eq 'Budget' and Rating gt 3.5)&api-version=2026-08-01-preview
 ```
 
 ### Select fields and limit results
 
 The `$top` selector can be used to limit how many results should be returned in a `MoreLikeThis` query. Also, fields can be selected with `$select`. Here the top three hotels are selected along with their ID, Name, and Rating: 
 
 ```http
-GET /indexes/hotels-sample/docs?moreLikeThis=20&searchFields=Description&$filter=(Category eq 'Budget' and Rating gt 3.5)&$top=3&$select=HotelId,HotelName,Rating&api-version=2026-05-01-preview
+GET /indexes/hotels-sample/docs?moreLikeThis=20&searchFields=Description&$filter=(Category eq 'Budget' and Rating gt 3.5)&$top=3&$select=HotelId,HotelName,Rating&api-version=2026-08-01-preview
 ```
 
 ## Next steps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "More Like Thisクエリに関するAPIバージョンの更新"
}
```

### Explanation
この変更は、Azureの検索機能における「More Like This」クエリに関する文書を更新し、特にAPIバージョンを2026-05-01-previewから2026-08-01-previewに変更しています。主な変更内容は以下の通りです：

1. **APIバージョンの更新**：すべての例において、APIバージョンが新しいもので修正されています。これにより、ユーザーは最新のAPIを利用して「More Like This」機能を適切に使用できるようになります。

2. **HTTPメソッドの利用例の修正**：GETリクエストとPOSTリクエストの両方において、APIバージョンの変更が反映され、新しいバージョンに基づいた具体的なリクエスト形式が示されています。

3. **フィルタリングの例の更新**：特定の条件に基づいた検索クエリの例も新しいバージョンに合わせて修正され、ユーザーが条件を具体的に設定する方法が明確に提示されています。

4. **結果の制限とフィールド選択の例の更新**：結果の数を制限し、特定のフィールドを選択するためのクエリが、新しいAPIバージョンを考慮した形式で更新されています。

これらの変更により、開発者は最新のAPIを基にして、検索クエリを効果的に構築し、適切なデータを取得することが期待されます。また、APIバージョンの更新によって、ユーザーは新機能や改善点を利用できるようになります。

## articles/search/search-preview-terms.md{#item-4fe0af}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ ai-usage: ai-assisted
 
 Azure AI Search releases some features, capabilities, and properties in preview. In the documentation, this functionality is marked (preview). Preview functionality, whether standalone or part of a generally available feature, isn't covered by a service-level agreement, isn't recommended for production workloads, and might change or be constrained before it becomes generally available.
 
-The terms in this article are based on the most recent data plane preview, the `2026-05-01-preview` [Search Service REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true). Depending on the preview version and functionality, some terms might not apply. Nevertheless, you're still responsible for complying with all applicable terms.
+The terms in this article are based on the most recent data plane preview, the `2026-08-01-preview` [Search Service REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true). Depending on the preview version and functionality, some terms might not apply. Nevertheless, you're still responsible for complying with all applicable terms.
 
 ## Licensing and preview terms
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索プレビュー用語のAPIバージョンの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるプレビュー機能に関する用語を更新し、最新のAPIバージョンを反映させることを目的としています。主な変更点は以下の通りです：

1. **APIバージョンの更新**：文書内で言及されているAPIバージョンが`2026-05-01-preview`から`2026-08-01-preview`に変更されました。これにより、最新のプレビュー機能に関連する正確な情報を提供することができます。

2. **プレビュー機能に関する明確化**：このセクションでは、プレビュー機能の使用に関する重要な注意点（例えば、サービスレベルアグリーメントの適用外や、運用環境での利用が推奨されないことなど）が強調されています。

この更新によって、開発者やユーザーは最新のAPIバージョンに基づいた正確な条件に従ってプレビュー機能を利用できるようになります。また、プレビューがどのように変化する可能性があるのかについての理解も深まります。

## articles/search/search-query-access-control-rbac-enforcement.md{#item-d24df7}

<details>
<summary>Diff</summary>
````diff
@@ -14,11 +14,11 @@ ms.custom: doc-kit-assisted
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -43,7 +43,7 @@ This article explains how to set up queries that use permission metadata to filt
   - For Azure Blob data sources, you must have role assignments on the container. You can use a [built-in indexer](search-indexer-access-control-lists-and-role-based-access.md), a [knowledge source](agentic-knowledge-source-how-to-blob.md), or [Push APIs](search-index-access-control-lists-and-rbac-push-api.md) to index permission metadata in your index.
   - For SharePoint data sources, you must configure access control lists (ACLs). You can use a [built-in SharePoint indexer](search-how-to-index-sharepoint-online.md) and configure it with [ACL ingestion capabilities](search-indexer-sharepoint-access-control-lists.md). You can also use an [indexed SharePoint knowledge source](agentic-knowledge-source-how-to-sharepoint-indexed.md) and configure it to [enforce document-level permissions](agentic-knowledge-source-how-to-sharepoint-indexed.md#enforce-document-level-permissions). Group-based permissions, including Microsoft 365 Groups, are supported when ingested as Entra object IDs. Group expansion occurs at query time through Microsoft Graph.
 
-- Use the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or a preview package of an Azure SDK to query the index or knowledge source. This API version supports internal queries that filter out unauthorized results.
+- Use the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) or a preview package of an Azure SDK to query the index or knowledge source. This API version supports internal queries that filter out unauthorized results.
 
 ## Limitations
 
@@ -119,7 +119,7 @@ If SharePoint permission filtering returns missing or unexpected results, see [T
 The request is identical to the standard ACL-enforced query. The search service uses the index's `sharePointConnectorAppRegistration` to resolve SharePoint group membership on the caller's behalf. Include `GroupIds` in the `select` clause to see `spg:`-prefixed values in the response.
 
 ```http
-POST {{endpoint}}/indexes/{index}/docs/search?api-version=2026-05-01-preview
+POST {{endpoint}}/indexes/{index}/docs/search?api-version=2026-08-01-preview
 Authorization: Bearer {{query-token}}
 x-ms-query-source-authorization: {{query-token}}
 Content-Type: application/json
@@ -136,7 +136,7 @@ Content-Type: application/json
 Here's an example of a query request from [sample code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/acl). The query token is a Microsoft Entra access token for the querying user.
 
 ```http
-POST  {{endpoint}}/indexes/stateparks/docs/search?api-version=2026-05-01-preview
+POST  {{endpoint}}/indexes/stateparks/docs/search?api-version=2026-08-01-preview
 Authorization: Bearer {{query-token}}
 x-ms-query-source-authorization: {{query-token}}
 Content-Type: application/json
@@ -176,7 +176,7 @@ Queries are a data plane operation, so the custom role can only consist of atomi
 After you set up permissions, you can run the query. The following example is a query request against a search index.
 
 ```http
-POST {endpoint}/indexes('{indexName}')/search.post.search?api-version=2026-05-01-preview
+POST {endpoint}/indexes('{indexName}')/search.post.search?api-version=2026-08-01-preview
 Authorization: Bearer {AUTH_TOKEN}
 x-ms-query-source-authorization: {TOKEN}
 x-ms-enable-elevated-read: true
@@ -189,7 +189,7 @@ x-ms-enable-elevated-read: true
 ```
 
 > [!IMPORTANT]
-> The `x-ms-enable-elevated-read` header only works on Search POST actions. You can't perform an elevated read query on a [knowledge base retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-05-01-preview&preserve-view=true) action.
+> The `x-ms-enable-elevated-read` header only works on Search POST actions. You can't perform an elevated read query on a [knowledge base retrieve](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2026-08-01-preview&preserve-view=true) action.
 
 ### Important ACL functionality behavior change in specific preview API versions
 
@@ -199,7 +199,7 @@ Starting in November 2025, this behavior changed:
 
 - ACL permission filters now apply even when using only service API keys or Entra authentication across all versions that support ACL.
 - If the user token is omitted, ACL-protected content isn't returned.
-- To view all documents for troubleshooting, you must explicitly include the elevated-read header when using REST API version `2026-05-01-preview`.
+- To view all documents for troubleshooting, you must explicitly include the elevated-read header when using REST API version `2026-05-01-preview` or later.
 
 This update helps keep content protected when applications don't enforce best practices for token validation.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBAC強制適用に関するプレビューAPIバージョンの更新"
}
```

### Explanation
この変更は、Azureの検索機能におけるロールベースアクセス制御（RBAC）に関連するクエリの文書を更新し、最新のAPIバージョンを反映させることを目指しています。主な変更点は以下の通りです：

1. **APIバージョンの更新**：文書内で言及されているAPIバージョンが`2026-05-01-preview`から`2026-08-01-preview`に変更されました。これにより、ユーザーは最新のプレビュー機能に関する正確な情報を得ることができます。

2. **重要な機能の明確化**：プレビュー機能やアクセス許可に関する重要な警告が更新されており、新しいAPIバージョンに基づく使用条件が適切に反映されています。これには、サービスを利用する際のコンプライアンスや地理的境界に関する注意点が含まれています。

3. **クエリ例の修正**：APIバージョンの変更に伴い、サンプルクエリリクエストのAPIエンドポイントが最新のバージョンに基づいて修正されています。具体的には、POSTリクエストのAPIバージョンが全て新しいバージョンに更新されています。

4. **ACL機能に関する重要な変更点**：特定のAPIバージョンにおけるアクセスポリシーの動作に関する変更が強調されています。これにより、コンテンツの保護が強化され、適切なベストプラクティスが強調されています。

これらの更新により、開発者やユーザーはより安全に最新の機能を使用し、RBACに基づくアクセス制御を適切に管理できるようになります。また、コンプライアンス維持のために必要な情報が提供されています。

## articles/search/search-query-sensitivity-labels.md{#item-3e1f8a}

<details>
<summary>Diff</summary>
````diff
@@ -13,11 +13,11 @@ ai-usage: ai-assisted
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag occurs before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag occurs before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data flows outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -42,7 +42,7 @@ This article explains how query-time sensitivity label enforcement works and how
 
 - Both the Azure AI Search service and the user issuing the query must be in the same Microsoft Entra tenant.
 
-- REST API version 2025-11-01-preview or an equivalent preview SDK package to query the index. The [elevated read](#elevated-read-for-administrative-investigations-preview) capability and Purview audit logging require [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or later.
+- REST API version 2025-11-01-preview or later, or an equivalent preview SDK package, to query the index. The [elevated read](#elevated-read-for-administrative-investigations-preview) capability and Purview audit logging require [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or later.
 
 - Authenticate queries using [Azure role-based access control](search-security-rbac.md) (RBAC), not API keys. When Purview sensitivity labels are enabled, API key access is restricted to index schema retrieval.
 
@@ -134,7 +134,7 @@ Here's an example of a query request that uses Microsoft Purview sensitivity lab
 Pass the application token as a bearer token in the `Authorization` header. Pass the user token as the raw token value in the `x-ms-query-source-authorization` header, without the `Bearer` prefix.
 
 ```http
-POST  {{endpoint}}/indexes/sensitivity-docs/docs/search?api-version=2025-11-01-preview
+POST  {{endpoint}}/indexes/sensitivity-docs/docs/search?api-version=2026-08-01-preview
 Authorization: Bearer {{app-query-token}}
 x-ms-query-source-authorization: {{user-query-token}}
 Content-Type: application/json
@@ -171,7 +171,7 @@ When the `x-ms-enable-elevated-read` header is set to `true`, the `x-ms-query-so
 ### Elevated read example
 
 ```http
-POST  {{endpoint}}/indexes/sensitivity-docs/docs/search?api-version=2026-05-01-preview
+POST  {{endpoint}}/indexes/sensitivity-docs/docs/search?api-version=2026-08-01-preview
 Authorization: Bearer {{contributor-token}}
 x-ms-enable-elevated-read: true
 Content-Type: application/json
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "センシティビティラベルに関するクエリのAPIバージョンの更新"
}
```

### Explanation
この変更は、Azureにおけるクエリのセンシティビティラベルの適用に関するドキュメントを更新し、最新のAPIバージョンを反映させるものです。主な変更点は以下の通りです：

1. **APIバージョンの更新**：文書内で言及されているAPIバージョンが、`2026-05-01-preview`から`2026-08-01-preview`に変更されました。これにより、最新の機能や使用条件が反映されています。

2. **重要な機能の強調**：プレビュー機能の使用に関する注意点が最新のバージョンに基づいて更新されており、他のMicrosoftサービスやサードパーティサービスとの接続に関する情報が含まれています。また、Azureのコンプライアンス境界に関する注意点も強調されています。

3. **クエリ例の調整**：具体的なAPI呼び出し例が新しいバージョンに合わせて修正されており、ユーザーはこの最新のAPIバージョンを使用してクエリを実行することができます。

4. **認証方法の明確化**：クエリを認証する際にAzureのロールベースアクセス制御（RBAC）を使用することが推奨されており、APIキーの使用が制限される点が示されています。

これらの更新により、ユーザーは最新のAPIを利用してより安全にセンシティビティラベルの管理を行い、コンプライアンスを維持しながらデータを扱うことができるようになります。

## articles/search/search-relevance-overview.md{#item-cb0e09}

<details>
<summary>Diff</summary>
````diff
@@ -105,7 +105,7 @@ The following diagram illustrates how the ranking algorithms work together.
 The following hybrid semantic query demonstrates the ranking workflow in the preceding diagram. The query is scored using RRF (based on L1 scores for text and vectors), followed by semantic ranking.
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2026-05-01-preview
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2026-08-01-preview
 
 {
   "search": "cloud formation over water",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索関連のAPIバージョンの更新"
}
```

### Explanation
この変更は、Azureの検索関連文書におけるAPIバージョンを更新したものです。主な変更点は以下の通りです：

1. **APIバージョンの更新**：指定されたAPIのバージョンが`2026-05-01-preview`から`2026-08-01-preview`に変更されました。この更新により、ユーザーは最新のプレビュー機能を利用するための正しい情報にアクセスできます。

2. **クエリ例の修正**：具体的なHTTPリクエストサンプルのAPIバージョンが更新された結果、ユーザーは新しいバージョンを使って検索クエリを実行することができるようになります。これにより、より良いパフォーマンスや機能の利用が可能になります。

この更新は、Azureを利用する開発者やユーザーが、そのプラットフォームの最新機能を効果的に活用する手助けとなります。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -72,7 +72,7 @@ Adding a customer-managed key to an object must happen when the object is newly
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Starting in the 2026-03-01-preview release, you can configure a customer-managed key at the service level on the Azure AI Search service itself. This feature lets you configure the key once and apply it to all newly created objects by default. That protection keeps sensitive data in your search service secure with a key you control, without requiring you to specify key information each time you create an object. In the data plane 2026-05-01-preview API, the `isServiceLevelKey` property on `encryptionKey` helps you determine whether an object inherits the service-level key or uses an explicit object-level key.
+Starting in the 2026-03-01-preview release, you can configure a customer-managed key at the service level on the Azure AI Search service itself. This feature lets you configure the key once and apply it to all newly created objects by default. That protection keeps sensitive data in your search service secure with a key you control, without requiring you to specify key information each time you create an object. In data plane API version `2026-05-01-preview` and later, the `isServiceLevelKey` property on `encryptionKey` helps you determine whether an object inherits the service-level key or uses an explicit object-level key.
 
 Enabling CMK at the service level means:
 
@@ -539,12 +539,12 @@ Currently, the Azure portal doesn't support service-level encryption. Use the RE
 
 ### [**REST APIs**](#tab/rest)
 
-In data plane API version `2026-05-01-preview`, use an object `GET` call to inspect `encryptionKey.isServiceLevelKey`.
+In data plane API version `2026-05-01-preview` and later, use an object `GET` call to inspect `encryptionKey.isServiceLevelKey`.
 
 The code snippet below is an example. You will need to update it with the values specific to your use-case.
 
 ```http
-GET https://{{search-service}}.search.windows.net/indexes/{{index-name}}?api-version=2026-05-01-preview
+GET https://{{search-service}}.search.windows.net/indexes/{{index-name}}?api-version=2026-08-01-preview
 api-key: {{admin-api-key}}
 ```
 
@@ -574,7 +574,7 @@ When `isServiceLevelKey` is `true`, the object inherits the service-level key an
 To decouple lifecycle for a specific object, set an explicit **object-level key** and set `isServiceLevelKey` to `false` in a `PUT` request that updates the object.
 
 ```http
-PUT https://{{search-service}}.search.windows.net/indexes/{{index-name}}?api-version=2026-05-01-preview
+PUT https://{{search-service}}.search.windows.net/indexes/{{index-name}}?api-version=2026-08-01-preview
 api-key: {{admin-api-key}}
 Content-Type: application/json
 ```
@@ -604,14 +604,14 @@ With this override, object-level key lifecycle is decoupled from the service-lev
 
 When you enable service-level CMK, create requests can omit `encryptionKey` and the object inherits the service-level key by default. To switch an existing object from an explicit object-level key to service-level CMK inheritance, set `isServiceLevelKey` to `true` in an update request.
 
-In data plane API version `2026-05-01-preview`, request validation applies to the `encryptionKey` object. If you provide `encryptionKey`, `keyVaultUri` and `keyVaultKeyName` are required string fields, regardless of whether `isServiceLevelKey` is present or what value it has. This validation checks field presence, not key existence. Placeholder string values satisfy this schema validation, and missing required fields result in HTTP 400.
+In data plane API version `2026-05-01-preview` and later, request validation applies to the `encryptionKey` object. If you provide `encryptionKey`, `keyVaultUri` and `keyVaultKeyName` are required string fields, regardless of whether `isServiceLevelKey` is present or what value it has. This validation checks field presence, not key existence. Placeholder string values satisfy this schema validation, and missing required fields result in HTTP 400.
 
 When `isServiceLevelKey` is `true`, the service applies the configured service-level key to the object. If you provide `keyVaultUri`, `keyVaultKeyName`, or `keyVaultKeyVersion` in the same request, the service ignores those values for key selection in that operation.
 
 For clarity and maintainability, provide the current service-level key values in the request and verify the effective key with a GET operation on the object.
 
 ```http
-PUT https://{{search-service}}.search.windows.net/indexes/{{index-name}}?api-version=2026-05-01-preview
+PUT https://{{search-service}}.search.windows.net/indexes/{{index-name}}?api-version=2026-08-01-preview
 api-key: {{admin-api-key}}
 Content-Type: application/json
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "暗号化キー管理に関するAPIバージョンの更新"
}
```

### Explanation
この変更は、Azureの暗号化キー管理に関する文書におけるAPIバージョンを更新したものです。以下のポイントが主な変更点です：

1. **APIバージョンの更新**：文書内で使用されているAPIバージョンが`2026-05-01-preview`から`2026-08-01-preview`に変更されました。これにより、最新の機能や更新された情報に基づいてユーザーが操作できるようになります。

2. **サービスレベルの暗号化キーの管理**：顧客管理キー（CMK）をサービスレベルで設定する機能についての説明が更新され、最新のAPIバージョンでの適用方法が明確に示されています。これにより、ユーザーは新しいオブジェクトを作成する際に、設定したキーを自動的に使用することができます。

3. **リクエストの検証の明確化**：新しいAPIバージョンにおいては、`encryptionKey`オブジェクトに対してリクエストの検証が適用されることが強調されており、必要なフィールドが満たされていない場合にはエラーが発生することが明記されています。

これらの更新は、セキュリティを重視するユーザーがAzureの暗号化機能をより効果的に利用するための情報を提供するものであり、暗号化キーの管理に関する信頼性と明確性を高めることを目的としています。

## articles/search/search-security-managed-encryption-cross-tenant.md{#item-efc726}

<details>
<summary>Diff</summary>
````diff
@@ -59,9 +59,9 @@ Use the Azure CLI to send requests. The service provider's tenant that contains
 ## Use federated identity support (preview)
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -128,7 +128,7 @@ After you configure the multitenant Microsoft Entra application and connect it t
    }
    ```
 
-1. Verify the index by sending a `GET` request: `GET https://<search-service>.search.windows.net/indexes/cross-tenant-cmk-test?api-version=2026-05-01-preview`
+1. Verify the index by sending a `GET` request: `GET https://<search-service>.search.windows.net/indexes/cross-tenant-cmk-test?api-version=2026-08-01-preview`
 
 If the request succeeds, the cross-tenant CMK configuration is working correctly.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クロステナントの暗号化に関するAPIバージョンの更新"
}
```

### Explanation
この変更は、Azureのクロステナント管理暗号化に関する文書においてAPIバージョンが更新された内容です。以下に主要な変更点を示します：

1. **APIバージョンの更新**：文書は、使用されるREST APIのバージョンを`2026-05-01-preview`から`2026-08-01-preview`に変更しました。この更新により、最新の機能や修正が反映され、ユーザーが新しい機能を利用できるようになります。

2. **フェデレーテッドアイデンティティサポート**：更新されたバージョンにおいても、他のMicrosoftサービスやサードパーティサービスへの接続がサポートされていることが記載されています。この接続に関しては、各サービスの利用規約に従う必要があります。

3. **データの流れと責任**：データが組織のコンプライアンスおよび地理的境界を越えるかどうかを管理する責任が利用者にあることが強調されています。また、適切な許可や境界、承認が必要であることに関する注意事項も含まれています。

この更新は、ユーザーがAzureのクロステナント暗号化機能をより適切に理解し、最新の情報に基づいてサービスを利用できるようにすることを目的としています。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,6 @@ The Serverless Developer tier is in Public Preview and doesn't currently support
 - Index aliases: Not supported
 - Debug sessions: Not supported
 - Private networking for indexers: Not supported
-- File Knowledge Source (Preview): Not supported
 - Shared Private Link resources: No planned support for the Serverless model
 - Service-level agreement (SLA): Not available during Public Preview
 
@@ -97,7 +96,7 @@ There is also a free, limited search service tier:
 
 - **Free** creates a [limited search service](search-limits-quotas-capacity.md#subscription-limits) for small projects, such as tutorials and development. Resources are shared across tenants, and scaling isn't supported. Some premium features are unavailable, and the service might be deleted after periods of inactivity. You can only have one free search service per Azure subscription.
 
-You see billing rates in the [Azure portal](https://portal.azure.com/auth/login/) when you create a new Azure AI Search service in the **Select Pricing Tier** page. 
+You see billing rates in the [Azure portal](https://portal.azure.com/auth/login/) when you create a new Azure AI Search service in the **Select Pricing Tier** page.
 
 :::image type="content" source="media/search-sku-tier/tiers.png" lightbox="media/search-sku-tier/tiers.png" alt-text="Screenshot of the Azure portal Select a pricing tier chart listing the service tiers and their associated SKU." border="true":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレス開発者ティアに関する情報の更新"
}
```

### Explanation
この変更は、Azureの検索SKUティアに関する文書において、特にサーバーレス開発者ティアに関連する情報の更新を行ったものです。以下のポイントが主な変更点です：

1. **サーバーレスティアのサポート機能の削除**：サーバーレス開発者ティアにおいて、「ファイル知識ソース（プレビュー）」がサポートされていない旨の記載が削除されました。このことでユーザーに対して明確にサポートされていない機能としての情報提供がなされ、わかりやすくなっています。

2. **文書の整頓**：全体の文構成が見直され、一部の文が削除されたことにより、記載内容が簡潔になり、重要な情報が際立つようになっています。

3. **料金情報の参照**：Azureポータルでの料金欄の情報についての記載は引き続きされています。新しいAzure AI検索サービスを作成する際に、料金ティアの選択ページで料金を見ることができることが確認されています。

この更新は、ユーザーがAzureの検索SKUティアに関する情報をより効果的に理解できるようにすることを目的としています。

## articles/search/semantic-answers.md{#item-c3fee9}

<details>
<summary>Diff</summary>
````diff
@@ -59,7 +59,7 @@ To return a semantic answer, the query must have the semantic `"queryType"`, `"q
 
 + `"queryType"` must be set to "semantic".
 
-+ `"queryLanguage"` must be one of the values from the [supported languages list (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true#querylanguage).
++ `"queryLanguage"` must be one of the values from the [supported languages list (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true#querylanguage).
 
 + A `"semanticConfiguration"` determines which string fields provide tokens to the extraction model. The same fields that produce captions also produce answers. See [Create a semantic configuration](semantic-how-to-configure.md) for details.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティッククエリにおけるAPIバージョンの更新"
}
```

### Explanation
この変更は、Azureのセマンティックアンサーに関する文書において、使用されるAPIバージョンに関する情報の更新を行ったものです。主な変更点は以下の通りです：

1. **APIバージョンの更新**：`"queryLanguage"`に関する記述が、従来の`2026-05-01-preview`から新しい`2026-08-01-preview`に更新されました。これにより、最新のAPIに基づいた正確な情報を提供することが目的とされています。

2. **セマンティック構成の説明**：新たに追加された行により、`"semanticConfiguration"`がどのフィールドからトークンを抽出するかを決定することが明記されました。キャプションを生成するのと同じフィールドが回答も生成することが強調され、ユーザーにとっての理解を深める内容となっています。

この更新は、ユーザーがセマンティッククエリの使用方法をより明確に理解できるように情報を最新の状態に保ち、利用しやすさを向上させることを意図しています。

## articles/search/semantic-code-migration.md{#item-ad1ba7}

<details>
<summary>Diff</summary>
````diff
@@ -49,6 +49,7 @@ Check your code for the REST API version or SDK package version to confirm which
 | Preview | [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) | Available on free tiers. |
 | Stable | [2026-04-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true) | Separates billing consent for semantic ranker and agentic retrieval. `semanticSearch` now only controls semantic ranker billing. Before upgrading, if you have `semanticSearch=standard`, you must also set `knowledgeRetrieval=standard`. For more information, see [Enable or disable semantic ranker billing](semantic-how-to-enable-disable.md). |
 | Preview | [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) | No change. |
+| Preview | [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) | No change. |
 
 ## Change logs for Azure SDKs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックコード移行に関するAPIバージョンの追加"
}
```

### Explanation
この変更は、Azureのセマンティックコード移行に関する文書に、新たなAPIバージョンを追加したものです。主な変更点は以下の通りです：

1. **新しいプレビューAPIバージョンの追加**：`2026-08-01-preview`という新しいプレビューAPIバージョンが追加されました。この行には「変更はなし」と記載されており、具体的な変更内容はないことが示されていますが、最新のAPI情報を文書に反映させることで、開発者が新しいバージョンを確認しやすくなっています。

2. **コードチェックの重要性の強調**：追加された行は、APIのバージョンを最新のものに保つ重要性を示しており、開発者が利用する際に現在のREST APIバージョンやSDKパッケージのバージョンを確認する必要があることを再確認させる内容となっています。

この更新により、ユーザーは最新のAPIバージョン情報を参考にし、適切な移行を行いやすくすることができます。

## articles/search/semantic-how-to-configure.md{#item-7a92a6}

<details>
<summary>Diff</summary>
````diff
@@ -29,7 +29,7 @@ This article explains how to configure a search index for semantic reranking.
 
 + Permission to create and use objects on Azure AI Search. We recommend [role-based access](search-security-rbac.md), but you can use [API keys](search-security-api-keys.md) if a role assignment isn't feasible. For more information, see [Connect to a search service](search-get-started-rbac.md).
 
-+ The [2026-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) version of the Search Service REST APIs.
++ The [2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) version of the Search Service REST API.
 
 ## Choose a client
 
@@ -46,29 +46,13 @@ You can specify a semantic configuration on new or existing indexes, using any o
 
 Some workloads create a semantic configuration automatically. If you're using [agentic retrieval](agentic-retrieval-overview.md) and a [knowledge source that indexes content](agentic-knowledge-source-overview.md#supported-knowledge-sources) on Azure AI Search, your generated index already has a semantic configuration that works for your content.
 
+> [!TIP]
+> Starting with the `2026-05-01-preview` API version, supported agentic retrieval knowledge base flows don't require an explicit semantic configuration. This exception doesn't apply to classic semantic ranking queries or older API versions. For more information, see [Create a search index knowledge source](agentic-knowledge-source-how-to-search-index.md).
+
 For other workloads, you can set up a semantic configuration yourself. A *semantic configuration* is a section in your index that establishes the field inputs used for semantic ranking. You can add or update a semantic configuration at any time, no rebuild necessary. If you create multiple configurations, you can specify a default. At query time, specify a semantic configuration on a [query request](semantic-how-to-query-request.md), or leave it blank to use the default.
 
 You can create up to 100 semantic configurations in a single index.
 
-### When semantic configuration is optional
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
-
-In the `2026-05-01-preview` API, supported agentic retrieval flows can use Azure AI Search ranking behavior without requiring an explicit semantic configuration on the underlying index. This preview behavior helps teams start with knowledge base retrieval without blocking on semantic configuration authoring.
-
-This change doesn't remove classic semantic ranking configuration. Continue to define a semantic configuration for classic semantic search queries, older API versions, and workloads that need explicit control over title, content, and keyword fields.
-
-For search index knowledge sources, `semanticConfigurationName` remains a supported property. Set it when you want the knowledge source to use a specific semantic configuration. In supported `2026-05-01-preview` agentic retrieval flows, you can omit it when you want the service to use the preview behavior that doesn't require an explicit semantic configuration on the underlying index.
-
-Semantic configuration is optional only for supported agentic retrieval knowledge base retrieve flows that use the `2026-05-01-preview` API. Classic semantic search queries and older API versions still require a semantic configuration when you use semantic ranking. If you create an index without a semantic configuration for the preview flow, don't assume that the same index can be used unchanged with GA or older preview semantic ranking APIs.
-
 A semantic configuration has a name and the following properties:
 
 | Property | Characteristics |
@@ -187,12 +171,12 @@ SearchIndex searchIndex = new(indexName)
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Using [preview REST APIs](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) and preview Azure SDKs that provide the property, you can optionally configure an index to use prerelease semantic ranking models if one is deployed in your region. There's no mechanism for knowing if a prerelease is available, or if it was used on specific query. For this reason, we recommend that you use this property in test environments, and only if you're interested in trying out the very latest semantic ranking models.
+Using [preview REST APIs](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) and preview Azure SDKs that provide the property, you can optionally configure an index to use prerelease semantic ranking models if one is deployed in your region. There's no mechanism for knowing if a prerelease is available, or if it was used on specific query. For this reason, we recommend that you use this property in test environments, and only if you're interested in trying out the very latest semantic ranking models.
 
 The configuration property is `"flightingOptIn": true`, and it's set in the semantic configuration section of an index. The property is null or false by default. You can set it true on a create or update request at any time, and it affects semantic queries moving forward, assuming the query stipulates a semantic configuration that includes the property.
 
 ```rest
-PUT https://myservice.search.windows.net/indexes('hotels')?allowIndexDowntime=False&api-version=2026-05-01-preview
+PUT https://myservice.search.windows.net/indexes('hotels')?allowIndexDowntime=False&api-version=2026-08-01-preview
 
 {
   "name": "hotels",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティック構成に関するAPIバージョンの更新と情報の整理"
}
```

### Explanation
この変更は、Azureのセマンティック構成を設定する方法に関する文書において、主に以下の点を改訂したものです：

1. **APIバージョンの更新**：文中で言及されているREST APIのバージョンが、従来の`2026-05-01-preview`から`2026-08-01-preview`に変更されました。これにより、最新のAPI情報を反映させることができ、実際の使用に即した正確な利用方法を提示しています。

2. **情報の整理と新しいヒントの追加**：セマンティック構成が不要な特定の状況について、ユーザーへのヒントが追加されました。特に、`2026-05-01-preview`以降のAPIバージョンでは、特定のエージェントリトリーバルの知識ベースフローで明示的なセマンティック構成を必要としないことが強調されています。この点を明確にすることで、開発者がより適切に設計作業を行う助けとなります。

3. **記述の簡略化**：不要な行が削除され、全体として文書がより読みやすくなりました。この整理によって、重要なポイントに焦点を当て、ユーザーが自分のニーズに応じて迅速に情報を探しやすくしています。

これらの変更により、ユーザーにとっての理解が深まり、Azureのセマンティック構成を効果的に利用する際の参考となることを目的としています。

## articles/search/semantic-how-to-enable-disable.md{#item-71ac1e}

<details>
<summary>Diff</summary>
````diff
@@ -16,23 +16,23 @@ ai-usage: ai-assisted
 
 Semantic ranker is a premium feature billed by usage. By default, all search services are enrolled in the free plan, which provides a monthly request allowance at no charge. To enable continued access after the free quota is consumed, you can switch to the standard plan.
 
-Starting with Search Service REST API version 2026-04-01, billing consent for semantic ranker and agentic retrieval is separate. Use `semanticSearch` to control billing for semantic ranker and `knowledgeRetrieval` to control billing for agentic retrieval.
+Starting with Search Service REST API version `2026-04-01`, billing consent for semantic ranker and agentic retrieval is separate. Use `semanticSearch` to control billing for semantic ranker and `knowledgeRetrieval` to control billing for agentic retrieval.
 
 ## Prerequisites
 
 - An Azure AI Search service in any [region that provides semantic ranker](search-region-support.md).
 
-- **Owner** or **Contributor** permissions on the search service.
+- **Owner** or **Contributor** access to the search service.
 
 - Search Management REST API version [2026-03-01-preview](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true) or later to set the `semanticSearch` property.
 
 ## Billing split
 
 [!INCLUDE [billing-split-version-compatibility](includes/billing-split-version-compatibility.md)]
 
-For Search Service REST API version 2026-04-01 and later, `semanticSearch` affects only semantic ranker billing. To control agentic retrieval billing, see [Enable or disable agentic retrieval billing](agentic-retrieval-how-to-enable-disable.md).
+For Search Service REST API version `2026-04-01` and later, `semanticSearch` affects only semantic ranker billing. To control agentic retrieval billing, see [Enable or disable agentic retrieval billing](agentic-retrieval-how-to-enable-disable.md).
 
-For Search Service REST API version 2025-11-01-preview and earlier, `semanticSearch` controls consent for both semantic ranker and paid agentic retrieval usage.
+For Search Service REST API version `2025-11-01-preview` and earlier, `semanticSearch` controls consent for both semantic ranker and paid agentic retrieval usage.
 
 ## Billing plans
 
@@ -64,9 +64,9 @@ Follow these steps to switch semantic ranker to the standard billing plan. The b
 Use [Services - Create Or Update](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true#searchsemanticsearch) (Search Management REST API) to set `semanticSearch` to `standard`:
 
 ```http
-PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2026-03-01-preview
+PATCH https://management.azure.com/subscriptions/{{subscription-id}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2026-03-01-preview
 Content-Type: application/json
-Authorization: Bearer {{token}}
+Authorization: Bearer {{management-access-token}}
 
 {
   "properties": {
@@ -101,9 +101,9 @@ Follow these steps to switch semantic ranker back to the free billing plan.
 Use [Services - Create or Update](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2026-03-01-preview&preserve-view=true#searchsemanticsearch) (Search Management REST API) to set `semanticSearch` to `free`:
 
 ```http
-PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2026-03-01-preview
+PATCH https://management.azure.com/subscriptions/{{subscription-id}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2026-03-01-preview
 Content-Type: application/json
-Authorization: Bearer {{token}}
+Authorization: Bearer {{management-access-token}}
 
 {
   "properties": {
@@ -115,7 +115,7 @@ Authorization: Bearer {{token}}
 Management REST API calls are authenticated through Microsoft Entra ID. For instructions on how to authenticate, see [Manage your Azure AI Search service with REST APIs](search-manage-rest.md).
 
 > [!NOTE]
-> The `disabled` value is no longer valid in Search Management REST API version 2026-03-01-preview and later. Existing services with `semanticSearch` set to `disabled` are automatically treated as `free`.
+> The `disabled` value is no longer valid in Search Management REST API version `2026-03-01-preview` and later. Existing services with `semanticSearch` set to `disabled` are automatically treated as `free`.
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーの有効化/無効化に関する情報の整備"
}
```

### Explanation
この変更は、Azureのセマンティックランカーに関するドキュメントを修正し、以下の重要なポイントが含まれています：

1. **一貫したフォーマットの適用**：APIのバージョン番号にバッククォート (`) を使用することにより、コードとテキストでの一貫性を持たせています。これにより、ユーザーがAPIバージョンを視覚的に認識しやすくなっています。

2. **アクセス権の表現の整理**：「**Owner** または **Contributor**」「**Owner** または **Contributor** アクセス」という言い回しが変更され、情報が明確化されました。これにより、必要な権限についての理解が深まり、ユーザーが設定を行う際の指針となります。

3. **APIエンドポイントの詳細の更新**：APIエンドポイントの説明文中の変数名として「{{subscription-id}}」と「{{management-access-token}}」が使用され、以前の形式から更新されています。これにより、適切なパラメーターを使用したAPI呼び出しが促進され、より明確なドキュメンテーションとなっています。

4. **無効な値に関する説明の明確化**：「`disabled`」値がもはや有効でないことが強調されています。これによって、ユーザーは過去の設定やAPIの動作について混乱を避けることができ、新しい運用方法を理解しやすくなっています。

この更新により、Azure AI Searchにおけるセマンティックランカーの機能についての理解が向上し、より効果的な利用を促すことが期待されています。

## articles/search/semantic-how-to-query-rewrite.md{#item-3e168f}

<details>
<summary>Diff</summary>
````diff
@@ -44,12 +44,12 @@ Query rewriting is an optional feature. Without query rewriting, the search serv
 
 ## Make a search request with query rewrites
 
-In this REST API example, use [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) to formulate the request.
+In this REST API example, use [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true) to formulate the request.
 
 1. Paste the following request into a web client as a template. 
 
     ```http
-    POST https://[search-service-name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2026-05-01-preview
+    POST https://[search-service-name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2026-08-01-preview
     {
         "search": "newer hotel near the water with a great restaurant",
         "semanticConfiguration":"en-semantic-config",
@@ -200,7 +200,7 @@ Here's an example of a query that includes a vector query with query rewrites. M
 - The "text" value is the same as the "search" value. These values must be identical for query rewriting to work.
 
 ```http
-POST https://[search-service-name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2026-05-01-preview
+POST https://[search-service-name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2026-08-01-preview
 {
     "search": "newer hotel near the water with a great restaurant",
     "vectorQueries": [
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリ再書き換えに関するAPIバージョンの更新"
}
```

### Explanation
この変更は、Azureのクエリ再書き換えに関するドキュメントの一部を更新したもので、主に以下のポイントが含まれています：

1. **APIバージョンの更新**：REST APIのバージョンが`2026-05-01-preview`から`2026-08-01-preview`に変更され、最新のAPIに対応しています。この更新は、APIの進化を反映しており、より新しい機能や修正に基づく情報を提供しています。

2. **一貫したテンプレートの使用**：クエリのPOSTリクエストの例において、同様にAPIバージョンが更新されています。これにより、ユーザーは最新のAPIを使用したリクエスト形式を理解しやすくなっています。

3. **説明の明確化**：クエリ再書き換え機能がオプショナルであることが再確認されており、ユーザーに対してこの機能の使用を促す文脈が整っています。

この更新によって、ユーザーが最新版のAPIを正しく使用し、効果的にクエリ再書き換え機能を活用できるよう支援することを目的としています。これにより、検索の品質や効率が向上する期待が高まります。

## articles/search/speller-how-to-add.md{#item-9b4502}

<details>
<summary>Diff</summary>
````diff
@@ -24,13 +24,13 @@ You can improve recall by spell-correcting words in a query before they reach th
 
 + An existing search index with content in a [supported language](#supported-languages).
 
-+ A [query request](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) that has `speller=lexicon` and `queryLanguage` set to a [supported language](#supported-languages). Spell check works on strings passed in the `search` parameter. It's not supported for filters, fuzzy search, wildcard search, regular expressions, or vector queries.
++ A [query request](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true) that has `speller=lexicon` and `queryLanguage` set to a [supported language](#supported-languages). Spell check works on strings passed in the `search` parameter. It's not supported for filters, fuzzy search, wildcard search, regular expressions, or vector queries.
 
 Use a search client that supports preview APIs on the query request. You can use a [REST client](search-get-started-text.md) or beta releases of the Azure SDKs.
 
 | Client library | Versions |
 |----------|----------|
-| REST API | Versions 2020-06-30-Preview and later. We recommend the latest preview API: [2026-05-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true)|
+| REST API | Versions 2020-06-30-Preview and later. We recommend the latest preview API: [2026-08-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true)|
 | Azure SDK for .NET | [version 11.7.0-beta.4](https://www.nuget.org/packages/Azure.Search.Documents/11.7.0-beta.4) | 
 | Azure SDK for Java |  [version 11.8.0-beta.7](https://central.sonatype.com/artifact/com.azure/azure-search-documents/11.8.0-beta.7) |
 | Azure SDK for JavaScript | [version 11.3.0-beta.8](https://www.npmjs.com/package/@azure/search-documents/v/11.3.0-beta.8) |
@@ -41,7 +41,7 @@ Use a search client that supports preview APIs on the query request. You can use
 The following example uses the [hotels-sample index](search-get-started-portal.md) to demonstrate spell correction on a simple text query. Without spell correction, the query returns zero results. With correction, the query returns one result for Johnson's family-oriented resort.
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2026-05-01-preview
+POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2026-08-01-preview
 {
     "search": "famly acitvites",
     "speller": "lexicon",
@@ -62,7 +62,7 @@ Spelling correction occurs on individual query terms that undergo text analysis,
 This example uses fielded search over the Category field, with full Lucene syntax, and a misspelled query term. By including speller, the typo in "Suiite" is corrected and the query succeeds.
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2026-05-01-preview
+POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2026-08-01-preview
 {
     "search": "Category:(Resort and Spa) OR Category:Suiite",
     "queryType": "full",
@@ -78,7 +78,7 @@ POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search
 This query, with typos in every term except one, undergoes spelling corrections to return relevant results. To learn more, see [Configure semantic ranker](semantic-how-to-query-request.md).
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2026-05-01-preview    
+POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2026-08-01-preview
 {
     "search": "hisotoric hotell wiht great restrant nad wiifi",
     "queryType": "semantic",
@@ -92,7 +92,7 @@ POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search
 
 ## Supported languages
 
-Valid values for `queryLanguage` can be found in the following table, copied from the list of [supported languages (REST API reference)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&tabs=HTTP#querylanguage&preserve-view=true).
+Valid values for `queryLanguage` can be found in the following table, copied from the list of [supported languages (REST API reference)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&tabs=HTTP#querylanguage&preserve-view=true).
 
 | Language | queryLanguage |
 |----------|---------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スペル補正機能に関するAPIバージョンの変更"
}
```

### Explanation
この変更は、Azureのスペル補正に関する文書を更新し、主に次のポイントが反映されています：

1. **APIバージョンの最新化**：各種REST APIリクエストのバージョンが`2026-05-01-preview`から`2026-08-01-preview`に変更されています。これにより、ユーザーは最新のAPI機能へのアクセスや改良されたパフォーマンスを利用できるようにしています。

2. **クエリリクエストの具体化**：スペル補正が機能するためのクエリリクエストに関する部分が明確に記載されており、特に`speller=lexicon`と`queryLanguage`が設定された場合の条件が強調されています。

3. **テンプレート例の更新**：スペル補正機能を利用するための具体的なHTTP POSTリクエストの例が、最新のAPIバージョンを反映した形で更新されています。これにより、開発者が実装する際に最新の情報を基に試行錯誤できるよう支援されています。

4. **サポートされている言語のリンク修正**：言語設定の情報を取得するためのリンクも最新のAPIバージョンに合わせて更新されており、正確な情報へスムーズにアクセスできるようになっています。

この更新を通じて、ユーザーはより効果的にスペル補正機能を活用し、精度の高い検索結果を得ることが可能になります。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -95,12 +95,12 @@ items:
       href: search-modeling-multitenant-saas-applications.md
   - name: Advanced management
     items:
+    - name: Page through list results (preview)
+      href: search-how-to-page-list-results.md
     - name: Manage a service
       items:
       - name: REST
         href: search-manage-rest.md
-      - name: Page list API results (preview)
-        href: search-how-to-page-list-results.md
       - name: PowerShell
         href: search-manage-powershell.md
       - name: Azure CLI
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の項目更新"
}
```

### Explanation
この変更は、Azureのドキュメント内の目次（toc.yml）を修正したもので、主に以下のポイントが含まれています：

1. **項目の追加**：目次に新しい項目「Page through list results (preview)」が追加され、この項目は「search-how-to-page-list-results.md」というドキュメントを参照しています。これにより、ユーザーはリスト結果のページングに関するガイドにアクセスできるようになります。

2. **項目の削除**：以前存在していた同様のテーマの項目「Page list API results (preview)」が削除されました。この変更は、重複を避け、目次を整理するために行われたと思われます。

3. **構造の整理**：新旧両方の項目が適切に整理され、目次の読みにくさが改善されています。特に関連するドキュメントが一つのカテゴリー内に集約され、ユーザーが必要な情報をより容易に見つけられるよう工夫されています。

この変更により、ドキュメントの可読性が向上し、ユーザーが特定のトピックに関連する情報を簡単に見つけることができるようになります。

## articles/search/troubleshoot-sharepoint-query-permission-filtering.md{#item-85cf41}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,7 @@ Use this article if query-time permission filtering for indexed SharePoint conte
 
 + An index populated by the [SharePoint in Microsoft 365 indexer](search-how-to-index-sharepoint-online.md) with [ACL ingestion configured](search-indexer-sharepoint-access-control-lists.md).
 + Query-time permission filtering configured as described in [Query-time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md).
-+ REST API version `2026-05-01-preview` or an equivalent preview SDK package when you use SharePoint site groups.
++ REST API version `2026-08-01-preview` or an equivalent preview SDK package when you use SharePoint site groups.
 + Access to the index definition, generated or explicit indexer status, and the SharePoint permissions for a test user.
 + **Search Index Data Contributor** or equivalent elevated-read permission if you need to compare filtered and unfiltered results.
 
@@ -88,7 +88,7 @@ If the indexed fields are empty or stale, fix ingestion or [synchronize the Shar
 
 ### 7. Check the query request
 
-1. Use REST API version `2026-05-01-preview` or an equivalent preview SDK package for SharePoint site-group permission filters.
+1. Use REST API version `2026-08-01-preview` or an equivalent preview SDK package for SharePoint site-group permission filters.
 1. Confirm `Authorization` authenticates a principal that can query the index.
 1. Confirm `x-ms-query-source-authorization` contains the delegated test-user token.
 1. Retry the same query without unrelated filters or ranking changes so you can isolate permission behavior.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIバージョンの更新"
}
```

### Explanation
この変更は、SharePoint のクエリ権限フィルタリングに関するトラブルシューティング記事を更新したもので、主に以下のポイントが含まれています：

1. **APIバージョンの更新**：REST APIのバージョンが`2026-05-01-preview`から`2026-08-01-preview`に更新されました。これにより、ユーザーは最新の機能や改善点を利用できるようになります。

2. **前提条件の明確化**：新しいAPIバージョンに基づいた使用条件や前提条件が具体的に示されています。特に、SharePointに関連するインデックスやアクセス制御リスト（ACL）の管理が強調されています。

3. **手順の更新**：クエリリクエストの手順が変更され、APIバージョンの更新に伴う具体的な指針が提供されています。これにより、ユーザーは新しいバージョンに適した方法で権限フィルタリングを実施することができます。

この変更により、ユーザーは最新のAPIを使用した際に遭遇する可能性のある問題を簡単に解決できるようになり、より効率的なトラブルシューティングが可能になります。

## articles/search/tutorial-adls-gen2-indexer-acls.md{#item-6881a0}

<details>
<summary>Diff</summary>
````diff
@@ -14,11 +14,11 @@ ai-usage: ai-assisted
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
+> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -39,7 +39,7 @@ In this tutorial, you learn how to:
 > + Create and run an indexer to ingest permission information into an index from a data source
 > + Search the index you just created
 
-Use a REST client to complete this tutorial and the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true). Currently, there's no support for ACL indexing in the Azure portal.
+Use a REST client to complete this tutorial and the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true). Currently, there's no support for ACL indexing in the Azure portal.
 
 ## Prerequisites
 
@@ -91,7 +91,7 @@ As a best practice, use [`Group` sets](search-indexer-access-control-lists-and-r
 
 [Create an index](search-how-to-create-search-index.md#create-an-index) that contains fields for content and [permission metadata](search-indexer-access-control-lists-and-role-based-access.md#create-permission-fields-in-the-index).
 
-Be sure to use the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or a preview Azure SDK package that provides equivalent functionality. The permission filter properties are only available in the preview APIs.
+Be sure to use the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) or a preview Azure SDK package that provides equivalent functionality. The permission filter properties are only available in the preview APIs.
 
 For demo purposes, the permission field has `retrievable` enabled so that you can check the values from the index. In a production environment, you should disable `retrievable` to avoid leaking sensitive information.
 
@@ -201,7 +201,7 @@ Now that documents are loaded, you can issue queries against them by using [Docu
 The URI is extended to include a query input, which is specified by using the `/docs/search` operator. The query token is passed in the request header. For more information, see [Query-time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md).
 
 ```http
-POST  {{endpoint}}/indexes/stateparks/docs/search?api-version=2026-05-01-preview
+POST  {{endpoint}}/indexes/stateparks/docs/search?api-version=2026-08-01-preview
 Authorization: Bearer {{search-token}}
 x-ms-query-source-authorization: {{search-token}}
 Content-Type: application/json
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIバージョンのアップデート"
}
```

### Explanation
この変更は、Azure Data Lake Storage Gen2インデクサーのACLに関するチュートリアル記事を更新したもので、以下の重要なポイントが含まれています：

1. **APIバージョンのアップデート**：REST APIの使用バージョンが`2026-05-01-preview`から`2026-08-01-preview`に変更されました。この更新により、ユーザーは新しい機能や修正を利用できるようになります。

2. **重要な注意事項の修正**：新しいAPIバージョンに関する注意事項が包括的に変更され、改訂されたAPIの利用条件や制限について詳細に説明されています。特に、外部で設定されたアクセス権限の変更を認識するまでの時間遅延についても言及されています。

3. **チュートリアルの手順の調整**：チュートリアル中で使用するRESTクライアントやAPIエンドポイントが新しいバージョンに沿って更新され、新しいAPIを適切に参照する方法が提供されました。

この変更によって、ユーザーは最新のREST APIを利用する際の指針が明確になり、環境での適切な利用と問題解決が容易になります。整体として、APIのバージョン更新に伴う重要な情報が反映されており、最新状況に基づいた使用が推奨されています。

## articles/search/tutorial-multimodal.md{#item-718d2e}

<details>
<summary>Diff</summary>
````diff
@@ -191,7 +191,7 @@ The [azure-search-rest-samples](https://github.com/Azure-Samples/azure-search-re
 [Create Data Source (REST)](/rest/api/searchservice/data-sources/create) creates a data source connection that specifies what data to index.
 
 ```http
-POST {{searchUrl}}/datasources?api-version=2026-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/datasources?api-version=2026-08-01-preview   HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer {{token}}
 
@@ -220,7 +220,7 @@ Send the request. The response should look like:
 HTTP/1.1 201 Created
 Transfer-Encoding: chunked
 Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
-Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('demo-multimodal-ds')?api-version=2026-05-01-preview -Preview
+Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('demo-multimodal-ds')?api-version=2026-08-01-preview -Preview
 Server: Microsoft-IIS/10.0
 Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
 Preference-Applied: odata.include-annotations="*"
@@ -1677,7 +1677,7 @@ This pattern uses:
 
 ```http
 ### Create and run an indexer
-POST {{searchUrl}}/indexers?api-version=2026-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers?api-version=2026-08-01-preview   HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer {{token}}
 
@@ -1714,7 +1714,7 @@ You can start searching as soon as the first document is loaded. This is an unsp
 
 ```http
 ### Query the index
-POST {{searchUrl}}/indexes/demo-multimodal-index/docs/search?api-version=2026-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/demo-multimodal-index/docs/search?api-version=2026-08-01-preview   HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer {{token}}
   
@@ -1750,7 +1750,7 @@ Connection: close
   },
   "value": [
   ],
-  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/demo-multimodal-index/docs/search?api-version=2026-05-01-preview "
+  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/demo-multimodal-index/docs/search?api-version=2026-08-01-preview "
 }
 ```
 
@@ -1763,7 +1763,7 @@ Use a filter to exclude all non-image content. The `$filter` parameter only work
 For filters, you can also use logical operators (and, or, not) and comparison operators (eq, ne, gt, lt, ge, le). String comparisons are case-sensitive. For more information and examples, see [Examples of simple search queries](search-query-simple-examples.md).
 
 ```http
-POST {{searchUrl}}/indexes/demo-multimodal-index/docs/search?api-version=2026-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/demo-multimodal-index/docs/search?api-version=2026-08-01-preview   HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer {{token}}
   
@@ -1789,7 +1789,7 @@ Query for text or images with content related to energy, returning the content I
 This query is full-text search only, but you can [query the vector field](vector-search-how-to-query.md) for similarity search.
 
 ```http
-POST {{searchUrl}}/indexes/demo-multimodal-index/docs/search?api-version=2026-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexes/demo-multimodal-index/docs/search?api-version=2026-08-01-preview   HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer {{token}}
   
@@ -1806,21 +1806,21 @@ Indexers can be reset to clear the high-water mark, which allows a full rebuild.
 
 ```http
 ### Reset the indexer
-POST {{searchUrl}}/indexers/demo-multimodal-indexer/reset?api-version=2026-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers/demo-multimodal-indexer/reset?api-version=2026-08-01-preview   HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer {{token}}
 ```
 
 ```http
 ### Run the indexer
-POST {{searchUrl}}/indexers/demo-multimodal-indexer/run?api-version=2026-05-01-preview   HTTP/1.1
+POST {{searchUrl}}/indexers/demo-multimodal-indexer/run?api-version=2026-08-01-preview   HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer {{token}}
 ```
 
 ```http
 ### Check indexer status 
-GET {{searchUrl}}/indexers/demo-multimodal-indexer/status?api-version=2026-05-01-preview   HTTP/1.1
+GET {{searchUrl}}/indexers/demo-multimodal-indexer/status?api-version=2026-08-01-preview   HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer {{token}}
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIバージョンの更新"
}
```

### Explanation
この変更は、マルチモーダル検索チュートリアルに関する記事の更新で、主に以下のポイントが含まれています：

1. **APIバージョンの変更**：このチュートリアルで使用されるREST APIのバージョンが`2026-05-01-preview`から`2026-08-01-preview`に更新されました。これにより、最新の機能が利用可能となり、バグ修正や改善が含まれる可能性があります。

2. **リクエストのパターンの見直し**：関連するHTTPリクエスト例のAPIバージョンが一致するようにすべて更新され、ユーザーが新しいバージョンを使用する際の手順が明確になりました。

3. **レスポンスの要領の調整**：API応答を示すサンプルコードにおいても新しいバージョンのURLが適用され、ユーザーは最新のリソースへのリンクを通じて適切に操作を行えるようになります。

この変更は、ユーザーが新しいAPIバージョンを活用し、マルチモーダル検索を効率的かつ効果的に利用できるようにするための重要なアップデートです。全体として、内容が最新の技術に基づいて更新されており、よりスムーズな実行が期待されます。

## articles/search/vector-search-how-to-chunk-documents.md{#item-b79133}

<details>
<summary>Diff</summary>
````diff
@@ -91,7 +91,7 @@ The `pages` parameter adds extra parameters:
 
 <sup>1</sup> Characters don't align to the definition of a [token](/azure/ai-services/openai/concepts/prompt-engineering#space-efficiency). The number of tokens measured by the LLM might be different than the character size measured by the Text Split skill with the character fixed-size.
 
-<sup>2</sup> Token chunking is available in the latest preview version of [Skillsets - Create or Update](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (REST API) and includes extra parameters for specifying a tokenizer and any tokens that shouldn't be split up during chunking.
+<sup>2</sup> Token chunking is available in the latest preview version of [Skillsets - Create or Update](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2026-08-01-preview&preserve-view=true) (REST API) and includes extra parameters for specifying a tokenizer and any tokens that shouldn't be split up during chunking.
 
 The following table shows how the choice of parameters affects the total chunk count from the Earth at Night e-book:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トークンチャンク処理に関するAPIバージョンの更新"
}
```

### Explanation
この変更は、文書をチャンクに分割するためのベクトル検索に関するチュートリアル記事の更新であり、主な内容は次のとおりです：

1. **APIバージョンの更新**：トークンチャンク処理に関する説明において、REST APIの使用バージョンが`2026-05-01-preview`から`2026-08-01-preview`に更新されました。これにより、新しいバージョンにおける機能や改善点が反映されています。

2. **整合性の確保**：APIの最新バージョンに応じた修正が行われており、トークン化やチャンク処理のパラメーターに関する情報が最新のものに保たれています。これにより、ユーザーが正確に新しいAPIを利用できるようになります。

この変更によって、ユーザーは最新の技術と仕様に基づいたトークンチャンク処理の実装方法を理解しやすくなり、より効果的なデータ処理が可能になります。全体として、内容が最新のAPIバージョンに適合していることを確認するための重要なアップデートです。

## articles/search/vector-search-how-to-query.md{#item-9bb93c}

<details>
<summary>Diff</summary>
````diff
@@ -1,4 +1,4 @@
-﻿---
+---
 title: Create a Vector Query
 description: Learn how to create vector queries that target an index in Azure AI Search.
 ms.service: azure-ai-search
@@ -133,9 +133,9 @@ api-key: {{admin-api-key}}
 }
 ```
 
-### [**2026-05-01-preview**](#tab/query-2026-05-01-preview)
+### [**2026-08-01-preview**](#tab/query-2026-08-01-preview)
 
-[**2026-05-01-preview**](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) is the latest preview API version of [Search - POST](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&tabs=HTTP&preserve-view=true). It supports the same vector query syntax as **2026-04-01**, but it has extra parameters for hybrid search and minimum thresholds for excluding weaker results.
+[**2026-08-01-preview**](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) is the latest preview API version of [Search - POST](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&tabs=HTTP&preserve-view=true). It supports the same vector query syntax as **2026-04-01**, but it has extra parameters for hybrid search and minimum thresholds for excluding weaker results.
 
 This preview supports:
 
@@ -145,7 +145,7 @@ This preview supports:
 In the following example, the vector is a representation of this string: `"what Azure services support full text search"`. The query targets the `contentVector` field and returns `k` results. The actual vector has 1,536 embeddings, which are trimmed in this example for readability.
 
 ```http
-POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2026-05-01-preview
+POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2026-08-01-preview
 Content-Type: application/json
 api-key: {{admin-api-key}}
 {
@@ -502,12 +502,12 @@ Vector weighting applies to vectors only. The text query in this example, `"hell
 
 Because nearest neighbor search always returns the requested `k` neighbors, it's possible to get multiple low-scoring matches as part of meeting the `k` number requirement on search results. To exclude low-scoring search results, you can add a `threshold` query parameter that filters out results based on a minimum score. Filtering occurs before [fusing results](hybrid-search-ranking.md) from different recall sets.
 
-This parameter is in preview. We recommend the latest preview version of [Documents - Search Post](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-05-01-preview&preserve-view=true) (REST API).
+This parameter is in preview. We recommend the latest preview version of [Documents - Search Post](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2026-08-01-preview&preserve-view=true) (REST API).
 
 In this example, all matches that score below 0.8 are excluded from vector search results, even if the number of results falls below `k`.
 
 ```http
-POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?api-version=2026-05-01-preview 
+POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?api-version=2026-08-01-preview
     Content-Type: application/json 
     api-key: [admin key] 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルクエリに関するAPIバージョンの更新"
}
```

### Explanation
この変更は、ベクトル検索に関するクエリの作成に関する記事の更新であり、次のようなポイントが含まれています：

1. **APIバージョンの更新**：クエリに関連するAPIバージョンが`2026-05-01-preview`から`2026-08-01-preview`に更新されました。これにより、新しいバージョンでは追加の機能や改善が利用可能となることが期待されています。

2. **レスポンスと要求の整合性**：HTTPリクエストサンプルのAPIバージョンも新しいものに更新され、記事全体で最新のAPIを使用する際の一貫性が保たれています。

3. **ドキュメントの引用の更新**：推奨される最新のAPIバージョンに基づいて、関連するリンクが調整されており、ユーザーが常に最新の情報を参照できるようになっています。

これらの更新によって、ユーザーは最新のベクトル検索機能を効果的に活用しやすくなり、特に新機能やパラメータを通じて、より良い検索結果を得ることが可能になります。全体として、この変更は、技術が進化する中でのユーザー体験の向上を目的とした重要なアップデートです。

## articles/search/vector-search-multi-vector-fields.md{#item-9aa482}

<details>
<summary>Diff</summary>
````diff
@@ -164,7 +164,7 @@ When a document includes multiple embedded vectors, such as text and image embed
 To debug how each vector contributed, use the `innerHits` debug mode (available in the latest preview REST API).
 
 ```json
-POST /indexes/my-index/docs/search?api-version=2026-05-01-preview
+POST /indexes/my-index/docs/search?api-version=2026-08-01-preview
 {
   "vectorQueries": [
     {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチベクトルフィールドに関するAPIバージョンの更新"
}
```

### Explanation
この変更は、マルチベクトルフィールドを含む文書の検索に関する記事のアップデートであり、以下のポイントが含まれています：

1. **APIバージョンの更新**：マルチベクトルフィールドを検索する際に使用するAPIのバージョンが、`2026-05-01-preview`から`2026-08-01-preview`に更新されました。これにより、新バージョンのAPIに含まれる新機能や改善が反映されます。

2. **デバッグモードの利用**：`innerHits`デバッグモードの利用が推奨され、各ベクトルがどのように影響を与えたかを分析する際に役立つ情報を提供します。最新のREST APIを使用することで、ユーザーはそれぞれのベクトルの寄与を詳しく理解することが可能になります。

この変更により、ユーザーは新しいAPIの利用において最新の情報に基づいて検索を行うことができ、特に複数のベクトルを持つ文書に対する照会性能が向上します。全体的に、この更新は、マルチベクトル検索機能の効果的な利用を促進するための重要なステップです。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +1,15 @@
 ---
 title: What's New
 description: Stay up to date with the latest Azure AI Search features, updates, and announcements. Discover new capabilities for search, vector, and AI-powered retrieval.
-ms.date: 08/05/2026
+ms.date: 08/25/2026
 ms.service: azure-ai-search
 ms.topic: whats-new
 ms.custom:
   - references_regions
   - ignite-2024
   - build-2025
+  - dev-focus
+  - doc-kit-assisted
 ai-usage: ai-assisted
 ---
 
@@ -17,16 +19,30 @@ ai-usage: ai-assisted
 
 Learn about the latest updates to Azure AI Search functionality, documentation, and samples.
 
-## June 2026
+## August 2026
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-05-01-preview REST API. The 2026-05-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-05-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
 >
-> The 2026-05-01-preview can't modify access permissions that were set outside of the 2026-05-01-preview. If you use the 2026-05-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-05-01-preview recognizes changes to those access or permission restrictions.
->
-> You can use the 2026-05-01-preview to enable cross-origin resource sharing (CORS), which allows browser-based applications to request data directly from the service. Depending on your CORS configuration, external web pages might be able to access or invoke the service and its data using the user's browser context, as well as create other security threats. Enabling CORS is at your own risk.
+> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+
+| Item | Description |
+|--|--|
+| [Search Service 2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) | New preview REST API version providing programmatic access to the data plane operations described in this table. |
+| [Private network support for indexed knowledge sources (preview)](agentic-knowledge-source-overview.md#restrict-ingestion-to-a-private-network-preview) | Blob, indexed SharePoint, and indexed Azure SQL knowledge sources now support private network ingestion through the generated indexer. |
+| [File knowledge source updates (preview)](agentic-knowledge-source-how-to-file.md) | File knowledge sources add the following capabilities:<p><ul><li>Support for Serverless search services.</li><li>Higher limits of 200 files (up from 100) and 100 MB per file on Serverless and Dedicated tiers above Free and Basic.</li><li>A multipart upload operation that accepts custom metadata.</li><li>An update operation that replaces file content.</li><li>A list operation that supports filtering by path or file name.</li><li>CORS configuration for the upload, list, update, and delete operations.</li></ul> |
+| [Work IQ knowledge source custom Microsoft Entra app (preview)](agentic-knowledge-source-how-to-work-iq.md) | Work IQ knowledge sources now use a customer-owned Microsoft Entra app and federated credential for on-behalf-of (OBO) access. This authentication model replaces preview feature registration and separate access requests. |
+| [Knowledge base expanded model support (preview)](agentic-retrieval-how-to-create-knowledge-base.md#supported-models) | Knowledge bases now support `gpt-5.5` and the `gpt-5.6` model family (`gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna`) for query planning and answer generation. |
+| [Automatic retrieval reasoning effort (preview)](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) | Set `retrievalReasoningEffort.kind` to `auto` to start with a lightweight retrieval pass and escalate to LLM-based query planning, up to `medium` effort, only when the first pass doesn't provide enough grounding. Store `auto` as the knowledge base default. Retrieve requests can override the stored default. `auto` requires a model configured on the knowledge base. |
+| [Request-time knowledge source exclusion (preview)](agentic-retrieval-how-to-retrieve.md#exclude-a-knowledge-source-from-a-request) | Set `neverQuerySource` to `true` to exclude an attached knowledge source from one retrieve request without changing knowledge base membership or knowledge source settings. |
+| [Query hints (preview)](agentic-knowledge-source-how-to-search-index.md#configure-query-hints-preview) | Guide the query planning model to generate filters and ranking boosts from a user's request. Store default hints on a search index knowledge source. Retrieve requests can override the stored hints. |
+| [Knowledge base retrieve defaults (preview)](agentic-retrieval-how-to-create-knowledge-base.md#configure-default-retrieve-limits-preview) | Store default runtime, output-document, and output-token budgets on a knowledge base. Retrieve requests can override each stored default independently. |
+| [Per-source reranking controls (preview)](agentic-retrieval-how-to-retrieve.md#disable-reranking-for-a-knowledge-source-preview) | Set `resultsProcessing` to `none` for a knowledge source to bypass reranking and preserve its underlying result order. Retrieve requests can override the stored default. |
+| [Stream retrieve results (preview)](agentic-retrieval-how-to-retrieve.md#stream-retrieve-results-preview) | Receive retrieve results as server-sent events instead of a single JSON response. Events report query planning, source activity, and the synthesized answer or extracted response as each becomes available, and a heartbeat comment keeps idle connections open. Whole-message answers are supported, but token-by-token answer deltas aren't. |
+| [Citation URLs for indexed knowledge sources (preview)](agentic-retrieval-how-to-retrieve.md#look-up-documents-with-citation-urls-preview) | Retrieve responses from indexed knowledge sources can include a service-generated `citationUrl` for an authenticated lookup of the backing document, preserving the selected fields and their order. Follow the URL with the same query-time authorization token used for permission-filtered retrieval. |
+| [Cursor pagination for list operations (preview)](search-how-to-page-list-results.md) | The 2026-08-01-preview adds cursor pagination for List Data Sources, List Indexers, List Indexes, and List Skillsets. Set `pageSize` and, when narrowing results by name, use `search` with `searchType=prefix`. Follow the complete, opaque `@odata.nextLink` to retrieve each subsequent page. |
+
+## June 2026
 
 | Item | Description |
 |--|--|
@@ -41,7 +57,7 @@ Learn about the latest updates to Azure AI Search functionality, documentation,
 | [Retrieve defaults for search index knowledge sources (preview)](agentic-knowledge-source-how-to-search-index.md) | Search index knowledge sources now support persisted retrieve defaults, including a `baseFilter` applied to all retrievals and a runtime `filterAddOn` that composes with the base filter using AND logic. A precedence model governs service defaults, knowledge source defaults, and per-request overrides. |
 | [Image serving for indexed knowledge sources (preview)](agentic-knowledge-source-overview.md) | Retrieved documents from indexed knowledge sources can include image content alongside text in agentic retrieval responses. |
 | [Freshness-aware retrieval for indexed knowledge sources (preview)](agentic-retrieval-how-to-configure-freshness.md) | Configure a freshness policy on indexed knowledge sources to bias retrieval toward recently updated documents. Adjust freshness weighting to balance recency with relevance in agentic workflows. |
-| [Knowledge base GPT-5 and CORS support (preview)](agentic-retrieval-how-to-create-knowledge-base.md) | Knowledge bases now support GPT-5 family models, including `gpt-5.4-mini`, for query planning and response generation. Configure CORS via the new `corsOptions` property to enable direct browser-to-service retrieve calls. |
+| [Knowledge base GPT-5 and CORS support (preview)](agentic-retrieval-how-to-create-knowledge-base.md) | Knowledge bases now support GPT-5 family models, including `gpt-5.4-mini`, for query planning and answer generation. Configure CORS via the new `corsOptions` property to enable direct browser-to-service retrieve calls. |
 | [Optional semantic configuration for agentic retrieval (preview)](semantic-how-to-configure.md) | Starting in the 2026-05-01-preview, a semantic configuration is optional in agentic retrieval flows. Classic semantic search still requires an explicit semantic configuration. |
 | [Retrieve action updates (preview)](agentic-retrieval-how-to-retrieve.md) | New parameters for the retrieve action:<p><ul><li>`knowledgeSourceParams.maxOutputDocuments` and `maxOutputDocuments` cap intermediate and final grounding documents returned.</li><li>`failOnError` marks each knowledge source as required or optional.</li><li>`modelName` appears in activity logs when `includeActivity` is `true`.</li></ul> |
 | [Knowledge base and knowledge source service statistics (preview)](vector-search-index-size.md) | [Get Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics?view=rest-searchservice-2026-05-01-preview&preserve-view=true) now returns `knowledgeBasesCount` and `knowledgeSourcesCount` as additive preview counters. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新のAzure AI Search機能に関する情報の更新"
}
```

### Explanation
この変更は、Azure AI Searchに関する「What's New」記事の更新であり、以下のポイントが含まれています：

1. **日付の更新**：記事の日付が2026年5月1日から2026年8月25日に変更され、地に足のついた最新の機能や更新を反映しています。

2. **APIバージョンの更新**：記事内で言及されているREST APIのバージョンが`2026-05-01-preview`から`2026-08-01-preview`に変更され、これにより新しいAPI機能を使用できる旨が記載されています。

3. **新機能の追加**：新バージョンに関連する新機能や改善点がリストアップされ、例えばプライベートネットワークのサポート、CORS設定の拡張、様々な新しい知識ソースの機能が提供されています。これにより、ユーザーは最新の技術や改善を踏まえた情報を得ることができ、活用の幅が広がります。

4. **重要情報のハイライト**：記事内で、新機能や機能改善に関する重要な情報が強調表示され、ユーザーが注意を払うべきポイントが明確にされています。

全体的に、この更新により、読者はAzure AI Searchの最新の動向を把握しやすくなり、これらの新機能を活用することで、より効率的な検索ソリューションを構築できるようになります。


