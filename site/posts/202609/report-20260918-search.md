---
date: '2026-09-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:cf104d1...MicrosoftDocs:e47f14e
summary: このコードの変更では、Azure AI Searchに関する文書が更新され、特にプレビュー段階の機能についての情報がわかりやすく示されています。新機能の状況が明確になり、ユーザーが注意すべきポイントを理解できるようになりました。具体的には、プレビューモードの追加や詳細な機能情報の提供が行われた一方で、レストAPIの一般提供に関するお知らせが削除され、公式情報源が減少したため、開発者やユーザーがガイダンスを得にくくなる可能性があります。全体的に、文書の構成や表記が統一され、重要なプレビュー情報が強調されています。この変更により、ユーザーがAzure
  AI Searchを効果的に活用し、最新の情報をもとに技術的な問題を理解しやすくなっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:cf104d1...MicrosoftDocs:e47f14e){target="_blank"}

<format>
# Highlights
このコードの変更では、Azure AI Searchのさまざまな文書が更新され、特にプレビュー段階にある機能に関する情報が明確に示されるようになっています。これにより、ユーザーは新しい機能のステータスを正確に把握し、利用に際する注意点を理解できるようになりました。

## New features
- プレビューモードの追加や更新により、Azure AI Searchの新機能の現状が明示されました。
- 異なる機能に対する詳細な情報が提供され、利用者の理解を助ける内容が追加されています。

## Breaking changes
- レストAPIの一般提供に関するお知らせが削除され、公式の情報源が減少しました。これにより、開発者やユーザーが新機能に関するガイダンスを得にくくなる可能性があります。

## Other updates
- プレビュー機能の整理と統一が図られ、文書全体の構成や表記の一貫性が向上しました。
- 必要なプレビュー情報がインクルードファイルを通じて提供されるようになり、重要な注意点が強調されました。

# Insights
このコードの変更から得られる知見は、多くの新しい機能がAzure AI Searchに追加され、そのほとんどがプレビュー段階にあるということです。プレビューとして提供される機能は、まだ開発中であるため、利用する際には注意が必要です。ユーザーは提供される情報とトラブルシューティングのガイダンスを活用し、最新の技術的アプローチや制約を理解することが求められます。

ドキュメントの更新は、情報の整合性と透明性を高め、ユーザーがAzure AI Searchを最大限に活用できるように設計されています。特に、プレビューフィーチャーに関連するような新しいインクルードファイルの追加は、重要な利用条件を視覚的に理解しやすくし、複雑な技術的背景を容易に把握するのに役立ちます。結果として、これらのドキュメントは、Azure AI Searchの技術を活用する開発者にとって、不可欠なリソースとなるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-azure-sql.md](#item-89aa4d) | minor update | Azure SQL 知識ソースのインデックス作成に関する変更 | modified | 2 | 8 | 10 | 
| [agentic-knowledge-source-how-to-blob.md](#item-ac6c8a) | minor update | Blob 知識ソースの作成に関する変更 | modified | 3 | 13 | 16 | 
| [agentic-knowledge-source-how-to-fabric-data-agent.md](#item-900ecc) | minor update | Fabric Data Agent 知識ソースの作成に関する変更 | modified | 4 | 8 | 12 | 
| [agentic-knowledge-source-how-to-fabric-ontology.md](#item-1f2bb6) | minor update | Fabric Ontology 知識ソースの作成に関する変更 | modified | 4 | 8 | 12 | 
| [agentic-knowledge-source-how-to-file.md](#item-88f720) | minor update | ファイル知識ソースの作成に関する変更 | modified | 2 | 8 | 10 | 
| [agentic-knowledge-source-how-to-mcp-server.md](#item-9a2e92) | minor update | MCPサーバー知識ソースの作成に関する変更 | modified | 5 | 10 | 15 | 
| [agentic-knowledge-source-how-to-onelake.md](#item-ec7a80) | minor update | インデックス付きOneLake知識ソースの作成に関する変更 | modified | 2 | 12 | 14 | 
| [agentic-knowledge-source-how-to-search-index.md](#item-09d366) | minor update | 検索インデックス知識ソースの作成に関する変更 | modified | 2 | 13 | 15 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed.md](#item-fe72fc) | minor update | インデックス付きSharePoint知識ソースの作成に関する変更 | modified | 2 | 12 | 14 | 
| [agentic-knowledge-source-how-to-sharepoint-remote.md](#item-79d019) | minor update | リモートSharePoint知識ソースの作成に関する変更 | modified | 2 | 10 | 12 | 
| [agentic-knowledge-source-how-to-web-manage.md](#item-af61ec) | minor update | Web知識ソースアクセス管理に関する変更 | modified | 1 | 0 | 1 | 
| [agentic-knowledge-source-how-to-web.md](#item-6b21d0) | minor update | Web知識ソースリソースの管理に関する変更 | modified | 3 | 11 | 14 | 
| [agentic-knowledge-source-how-to-work-iq.md](#item-94718e) | minor update | Work IQ知識ソースの作成に関する変更 | modified | 4 | 8 | 12 | 
| [agentic-knowledge-source-overview.md](#item-dcf29a) | minor update | 知識ソースの概要に関する変更 | modified | 2 | 8 | 10 | 
| [agentic-retrieval-how-to-answer-synthesis.md](#item-f44e99) | minor update | 回答合成に関する変更 | modified | 3 | 11 | 14 | 
| [agentic-retrieval-how-to-configure-freshness.md](#item-0b04e6) | minor update | フレッシュネス対応の取得設定に関する変更 | modified | 2 | 8 | 10 | 
| [agentic-retrieval-how-to-create-index.md](#item-3fbd2e) | minor update | エージェント取得用インデックス作成に関する変更 | modified | 1 | 2 | 3 | 
| [agentic-retrieval-how-to-create-knowledge-base.md](#item-7df0e2) | minor update | ナレッジベース作成に関する変更 | modified | 2 | 10 | 12 | 
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | エージェント取得ソリューション構築チュートリアルの更新 | modified | 12 | 17 | 29 | 
| [agentic-retrieval-how-to-enable-disable.md](#item-44591a) | minor update | エージェント取得の課金計画に関する情報追加 | modified | 1 | 0 | 1 | 
| [agentic-retrieval-how-to-image-serving.md](#item-48db70) | minor update | エージェント取得における画像サービングの有効化に関する情報追加 | modified | 2 | 10 | 12 | 
| [agentic-retrieval-how-to-migrate.md](#item-9653ea) | minor update | エージェント取得コードの移行に関する情報追加 | modified | 2 | 8 | 10 | 
| [agentic-retrieval-how-to-retrieve.md](#item-d739cf) | minor update | 知識ベースのクエリに関する情報の追加と更新 | modified | 11 | 19 | 30 | 
| [agentic-retrieval-how-to-set-retrieval-reasoning-effort.md](#item-141e97) | minor update | 取得推論努力の設定に関する情報の追加 | modified | 2 | 10 | 12 | 
| [agentic-retrieval-overview.md](#item-d1f354) | minor update | エージェント取得の概要に関する情報の更新 | modified | 26 | 16 | 42 | 
| [cognitive-search-aml-skill.md](#item-51366c) | minor update | AMLスキルに関するプレビュー情報の追加 | modified | 5 | 6 | 11 | 
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | AI支援機能の追加とプレビュー情報の強調 | modified | 3 | 2 | 5 | 
| [cognitive-search-concept-intro.md](#item-bf9ed7) | minor update | インクリメンタルエンリッチメントのプレビュー情報の追加 | modified | 4 | 4 | 8 | 
| [cognitive-search-defining-skillset.md](#item-e2d71d) | minor update | AI支援機能とプレビュー情報の追加 | modified | 2 | 1 | 3 | 
| [cognitive-search-predefined-skills.md](#item-81d522) | minor update | AI支援機能の追加とプレビュー情報の更新 | modified | 2 | 1 | 3 | 
| [cognitive-search-skill-content-understanding.md](#item-c7787e) | minor update | プレビュー機能の条件に関する更新 | modified | 2 | 3 | 5 | 
| [cognitive-search-skill-textsplit.md](#item-9bf753) | minor update | テキスト分割スキルのパラメータの更新と整理 | modified | 14 | 17 | 31 | 
| [cognitive-search-skill-vision-vectorize.md](#item-386571) | minor update | Azure Visionマルチモーダル埋め込みスキルのプレビュー記載の追加 | modified | 4 | 4 | 8 | 
| [cognitive-search-tutorial-debug-sessions.md](#item-7e10e9) | minor update | キャッシュ設定のプレビュー状態の明示化 | modified | 1 | 1 | 2 | 
| [cognitive-search-working-with-skillsets.md](#item-6091d1) | minor update | キャッシュ機能のプレビュー状態の表記追加 | modified | 1 | 1 | 2 | 
| [enrichment-cache-how-to-configure.md](#item-b0ae0b) | minor update | エンリッチメントキャッシュ機能のプレビュー状態の表記追加 | modified | 5 | 5 | 10 | 
| [enrichment-cache-how-to-manage.md](#item-a972bd) | minor update | エンリッチメントキャッシュ管理機能のプレビュー状態の表記追加 | modified | 5 | 5 | 10 | 
| [get-started-portal-agentic-retrieval.md](#item-2bf1dc) | minor update | エージェンティックリトリーバルに関するクイックスタートガイドの修正 | modified | 7 | 6 | 13 | 
| [hybrid-search-how-to-query.md](#item-345ce6) | minor update | ハイブリッド検索クエリに関するドキュメントの修正 | modified | 7 | 7 | 14 | 
| [hybrid-search-ranking.md](#item-dad887) | minor update | ハイブリッド検索ランキングに関するドキュメントの修正 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-ga-announcement.md](#item-4f2f62) | breaking change | エージェント検索の一般提供に関するお知らせの削除 | removed | 0 | 14 | 14 | 
| [agentic-retrieval-ga-feature.md](#item-2de8dc) | breaking change | エージェント検索の一般提供機能に関するお知らせの削除 | removed | 0 | 14 | 14 | 
| [agentic-retrieval-preview-feature.md](#item-e94474) | breaking change | エージェント検索のプレビューフィーチャーに関するお知らせの削除 | removed | 0 | 12 | 12 | 
| [preview-generic.md](#item-51bbcc) | breaking change | プレビューフィーチャーに関する一般的なインクルードファイルの削除 | removed | 0 | 13 | 13 | 
| [preview-terms.md](#item-b7699b) | new feature | プレビューフィーチャーの利用に関する新しいインクルードファイルの追加 | added | 13 | 0 | 13 | 
| [agentic-retrieval-csharp.md](#item-f93ed3) | minor update | エージェンティックリトリーバルのC#クイックスタートの内容修正 | modified | 3 | 5 | 8 | 
| [agentic-retrieval-java.md](#item-4e2c55) | minor update | エージェンティックリトリーバルのJavaクイックスタートの内容修正 | modified | 3 | 5 | 8 | 
| [agentic-retrieval-javascript.md](#item-715283) | minor update | エージェンティックリトリーバルのJavaScriptクイックスタートの内容修正 | modified | 5 | 5 | 10 | 
| [agentic-retrieval-python.md](#item-efee6a) | minor update | エージェンティックリトリーバルのPythonクイックスタートの内容修正 | modified | 5 | 5 | 10 | 
| [agentic-retrieval-rest.md](#item-3df373) | minor update | エージェンティックリトリーバルのRESTクイックスタートの内容修正 | modified | 5 | 5 | 10 | 
| [agentic-retrieval-setup.md](#item-e5e297) | minor update | エージェンティックリトリーバル設定のドキュメント修正 | modified | 2 | 1 | 3 | 
| [agentic-retrieval-typescript.md](#item-e6370b) | minor update | エージェンティックリトリーバルのTypeScriptクイックスタートの内容修正 | modified | 5 | 5 | 10 | 
| [index-similarity-and-scoring.md](#item-75603d) | minor update | インデックスの類似性とスコアリングに関するドキュメントの修正 | modified | 2 | 1 | 3 | 
| [knowledge-store-concept-intro.md](#item-7475c2) | minor update | Azure AI Searchにおけるナレッジストアの概念に関するドキュメントの修正 | modified | 2 | 1 | 3 | 
| [knowledge-store-projection-example-long.md](#item-e18999) | minor update | ナレッジストアにおけるプロジェクションの例に関するドキュメントの修正 | modified | 2 | 1 | 3 | 
| [multimodal-search-overview.md](#item-d82192) | minor update | マルチモーダル検索の概要に関するドキュメントの修正 | modified | 1 | 1 | 2 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | 検索強化生成 (RAG) に関する概要ドキュメントの修正 | modified | 3 | 2 | 5 | 
| [samples-rest.md](#item-198ebc) | minor update | REST APIサンプルドキュメントの修正 | modified | 1 | 1 | 2 | 
| [search-blob-indexer-role-based-access.md](#item-887e42) | minor update | RBACスコープメタデータの取り込みに関する文書の更新 | modified | 3 | 14 | 17 | 
| [search-blob-metadata-properties.md](#item-2137f3) | minor update | SharePointインデクシングに関するプレビュー情報の追加 | modified | 1 | 1 | 2 | 
| [search-capacity-planning.md](#item-0dd6c9) | minor update | Serverlessプランのプレビュー情報の書式変更 | modified | 1 | 1 | 2 | 
| [search-document-level-access-overview.md](#item-4bb055) | minor update | ドキュメントレベルアクセスに関するプレビュー情報の追加 | modified | 9 | 18 | 27 | 
| [search-faceted-navigation-examples.md](#item-2b1158) | minor update | ファセットナビゲーションのプレビュー情報の追加 | modified | 8 | 11 | 19 | 
| [search-faceted-navigation.md](#item-f29d1e) | minor update | スペルチェック機能のプレビュー情報の追加 | modified | 2 | 1 | 3 | 
| [search-features-list.md](#item-d34448) | minor update | ファーチャーリストの修正とプレビュー機能の追加 | modified | 7 | 7 | 14 | 
| [search-file-storage-integration.md](#item-d20e26) | minor update | プレビュー用インクルードの更新とインデクサーの説明修正 | modified | 2 | 2 | 4 | 
| [search-get-started-agentic-retrieval.md](#item-4a40f4) | minor update | エージェンティックリトリーバルのクイックスタート説明の改善 | modified | 4 | 2 | 6 | 
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | Azureポータルにおけるマルチモーダル検索のクイックスタートの更新 | modified | 3 | 3 | 6 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | Azureポータルにおけるベクター検索のクイックスタートの更新 | modified | 3 | 3 | 6 | 
| [search-get-started-semantic.md](#item-2b3902) | minor update | Azure AI Searchにおけるセマンティックランキングのクイックスタートの更新 | modified | 1 | 1 | 2 | 
| [search-how-to-create-indexers.md](#item-de71fb) | minor update | Azure AI Searchのインデクサー作成に関する記事の更新 | modified | 5 | 4 | 9 | 
| [search-how-to-define-index-projections.md](#item-a7e2c5) | minor update | 親子インデクシングのためのインデックス投影の定義に関する記事の更新 | modified | 2 | 1 | 3 | 
| [search-how-to-delete-documents.md](#item-556879) | minor update | 文書削除に関する記事の更新 | modified | 1 | 1 | 2 | 
| [search-how-to-index-azure-blob-csv.md](#item-185bfc) | minor update | Azure Blob CSVのインデックス作成に関する記事の更新 | modified | 2 | 2 | 4 | 
| [search-how-to-index-azure-blob-json.md](#item-8133fe) | minor update | Azure Blob JSONのインデックス作成に関する記事の更新 | modified | 2 | 1 | 3 | 
| [search-how-to-index-azure-blob-markdown.md](#item-c35bd7) | minor update | Azure Blob Markdownのインデックス作成に関する記事の更新 | modified | 1 | 1 | 2 | 
| [search-how-to-index-azure-blob-one-to-many.md](#item-30a1f9) | minor update | Azure Blob One to Manyのインデックス作成に関する記事の更新 | modified | 2 | 1 | 3 | 
| [search-how-to-index-azure-blob-plaintext.md](#item-1d543c) | minor update | Azure Blob Plaintextのインデックス作成に関する記事の更新 | modified | 2 | 1 | 3 | 
| [search-how-to-index-azure-blob-storage.md](#item-353b6b) | minor update | Azure Blob Storageのインデックス作成に関する記事の軽微な更新 | modified | 3 | 3 | 6 | 
| [search-how-to-index-azure-data-lake-storage.md](#item-faca23) | minor update | Azure Data Lake Storageのインデックス作成に関する記事の更新 | modified | 2 | 2 | 4 | 
| [search-how-to-index-azure-tables.md](#item-c8a1d1) | minor update | Azure Table Storageのインデックス作成に関する記事の軽微な更新 | modified | 1 | 1 | 2 | 
| [search-how-to-index-cosmosdb-gremlin.md](#item-e5e93d) | minor update | Azure Cosmos DB Gremlinのインデックス作成に関する記事の更新 | modified | 3 | 3 | 6 | 
| [search-how-to-index-cosmosdb-mongodb.md](#item-b5aa9f) | minor update | Azure Cosmos DB MongoDBのインデックス作成に関する記事の更新 | modified | 3 | 3 | 6 | 
| [search-how-to-index-cosmosdb-sql.md](#item-2e888b) | minor update | Azure Cosmos DB SQLのインデックス作成に関する記事の更新 | modified | 1 | 1 | 2 | 
| [search-how-to-index-logic-apps.md](#item-e25907) | minor update | Logic Appsのインデックス作成に関する記事の更新 | modified | 1 | 1 | 2 | 
| [search-how-to-index-mysql.md](#item-fffdee) | minor update | MySQLからのインデックス作成に関する記事の更新 | modified | 4 | 3 | 7 | 
| [search-how-to-index-onelake-files.md](#item-95f3db) | minor update | OneLakeファイルのインデックス作成に関する記事の更新 | modified | 3 | 3 | 6 | 
| [search-how-to-index-sharepoint-online.md](#item-8c099c) | minor update | SharePoint Onlineインデックス作成に関する記事の更新 | modified | 7 | 14 | 21 | 
| [search-how-to-index-sql-database.md](#item-86d873) | minor update | SQLデータベースのインデックス作成に関する記事の更新 | modified | 1 | 1 | 2 | 
| [search-how-to-index-sql-managed-instance.md](#item-009ccc) | minor update | SQLマネージドインスタンスのインデックス作成に関する記事の更新 | modified | 2 | 1 | 3 | 
| [search-how-to-integrated-vectorization.md](#item-86fb1e) | minor update | 統合ベクトル化に関する記事の文言修正 | modified | 1 | 1 | 2 | 
| [search-how-to-large-index.md](#item-d34e42) | minor update | 大規模インデックス作成に関する記事の文言修正 | modified | 1 | 1 | 2 | 
| [search-how-to-managed-identities.md](#item-3536f2) | minor update | 管理対象アイデンティティに関する記事の内容更新 | modified | 3 | 2 | 5 | 
| [search-how-to-multiple-indexers-one-index.md](#item-5ccefd) | minor update | 複数のインデクサーを使用する方法に関する記事の更新 | modified | 3 | 10 | 13 | 
| [search-how-to-page-list-results.md](#item-73059a) | minor update | ページリスト結果の表示方法に関する記事の内容更新 | modified | 1 | 8 | 9 | 
| [search-how-to-semantic-chunking-content-understanding.md](#item-5968e6) | minor update | コンテンツ理解によるチャンク化とベクトル化に関する記事の更新 | modified | 14 | 14 | 28 | 
| [search-how-to-semantic-chunking.md](#item-4a1d07) | minor update | セマンティックチャンク化に関する記事の索引作成者の更新 | modified | 1 | 1 | 2 | 
| [search-howto-managed-identities-cosmos-db.md](#item-a74464) | minor update | Azure Cosmos DB管理ID接続に関する記事の更新 | modified | 3 | 2 | 5 | 
| [search-howto-managed-identities-storage.md](#item-8209c4) | minor update | Azureストレージに管理IDで接続する方法に関する記事の更新 | modified | 2 | 1 | 3 | 
| [search-howto-run-reset-indexers.md](#item-fb10c8) | minor update | インデクサーのリセットと実行方法に関する記事の更新 | modified | 2 | 2 | 4 | 
| [search-import-data-portal.md](#item-b804d1) | minor update | データポータルのインポートに関する記事の更新 | modified | 5 | 5 | 10 | 
| [search-index-access-control-lists-and-rbac-push-api.md](#item-45e71e) | minor update | インデックスアクセス制御リストとRBACに関する記事の更新 | modified | 3 | 12 | 15 | 
| [search-indexer-access-control-lists-and-role-based-access.md](#item-67b42f) | minor update | インデクサーのアクセス制御リストとRBACに関する記事の更新 | modified | 2 | 11 | 13 | 
| [search-indexer-high-density-serverless-overview.md](#item-2bc606) | minor update | サーバーレスおよび標準3高密度インデクサーの概要に関する記事の更新 | modified | 7 | 6 | 13 | 
| [search-indexer-howto-access-trusted-service-exception.md](#item-e19826) | minor update | 信頼されたサービス例外へのアクセスに関する記事の更新 | modified | 2 | 1 | 3 | 
| [search-indexer-overview.md](#item-292796) | minor update | Azure AI Searchにおけるインデクサーの概要に関する記事の更新 | modified | 8 | 7 | 15 | 
| [search-indexer-securing-resources.md](#item-c075c4) | minor update | リソースのセキュリティ確保に関するインデクサーの記事の更新 | modified | 13 | 9 | 22 | 
| [search-indexer-sensitivity-labels.md](#item-2a7bfc) | minor update | 感度ラベルに関するインデクサーの記事の更新 | modified | 3 | 14 | 17 | 
| [search-indexer-sharepoint-access-control-lists.md](#item-532a24) | minor update | SharePoint アクセス制御リストに関するインデクサーの記事の更新 | modified | 4 | 13 | 17 | 
| [search-indexer-troubleshooting.md](#item-087365) | minor update | インデクサートラブルシューティングガイドの更新 | modified | 14 | 2 | 16 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索制限・クォータ・キャパシティに関するガイドの更新 | modified | 4 | 4 | 8 | 
| [search-more-like-this.md](#item-56c565) | minor update | moreLikeThis機能のプレビューメッセージの更新 | modified | 4 | 4 | 8 | 
| [search-pagination-page-layout.md](#item-115902) | minor update | ページネーションに関するAPIの更新 | modified | 1 | 1 | 2 | 
| [search-preview-terms.md](#item-4fe0af) | minor update | プレビューロゴと関連するセキュリティ項目の更新 | modified | 5 | 3 | 8 | 
| [search-query-access-control-rbac-enforcement.md](#item-d24df7) | minor update | クエリのアクセス制御に関する内容の更新 | modified | 4 | 15 | 19 | 
| [search-query-overview.md](#item-dcd5d6) | minor update | エージェンティック検索のプレビュー状態の説明を更新 | modified | 1 | 1 | 2 | 
| [search-query-sensitivity-labels.md](#item-3e1f8a) | minor update | 感度ラベルポリシーに関する説明の更新 | modified | 3 | 12 | 15 | 
| [search-region-support.md](#item-25b0f1) | minor update | マイクロソフト・パービュー感度ラベルの説明を更新 | modified | 1 | 3 | 4 | 
| [search-relevance-overview.md](#item-cb0e09) | minor update | エージェントリック検索の用語の修正 | modified | 2 | 2 | 4 | 
| [search-security-best-practices.md](#item-9dd4cd) | minor update | クエリ書き換えのプレビュー表記を追加 | modified | 1 | 1 | 2 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | プレビュー用の説明文を追加 | modified | 2 | 2 | 4 | 
| [search-security-managed-encryption-cross-tenant.md](#item-efc726) | minor update | プレビュー情報と説明の更新 | modified | 3 | 10 | 13 | 
| [search-security-rbac.md](#item-a5d129) | minor update | プレビュー機能への言及を更新 | modified | 2 | 2 | 4 | 
| [search-sku-manage-costs.md](#item-6e0122) | minor update | プレビュー機能の記述を更新 | modified | 4 | 3 | 7 | 
| [search-sku-tier.md](#item-7686b8) | minor update | プレビュー機能の表記を修正 | modified | 3 | 3 | 6 | 
| [search-try-for-free.md](#item-36e28d) | minor update | プレビュー表記の統一 | modified | 3 | 3 | 6 | 
| [search-what-is-azure-search.md](#item-93853a) | minor update | 日付の更新と表記の整合性 | modified | 4 | 15 | 19 | 
| [semantic-code-migration.md](#item-ad1ba7) | minor update | プレビュー表記の追加 | modified | 1 | 1 | 2 | 
| [semantic-how-to-configure.md](#item-7a92a6) | minor update | プレビュー表記の追加と内容の整理 | modified | 3 | 3 | 6 | 
| [semantic-how-to-query-request.md](#item-85530d) | minor update | AI使用の明記と注意書きの内容修正 | modified | 2 | 1 | 3 | 
| [semantic-how-to-query-rewrite.md](#item-3e168f) | minor update | プレビュー版表示の修正とAI使用の明示 | modified | 4 | 3 | 7 | 
| [semantic-search-overview.md](#item-b7497b) | minor update | クエリ再作成のプレビュー表示の修正 | modified | 1 | 1 | 2 | 
| [serverless-cost-optimization.md](#item-8dc21e) | minor update | サーバーレスプランのプレビュー表示の修正 | modified | 1 | 1 | 2 | 
| [speller-how-to-add.md](#item-9b4502) | minor update | スペルチェック機能のプレビューモード表示の修正 | modified | 4 | 4 | 8 | 
| [toc.yml](#item-c4768f) | minor update | プレビューモードに関する情報の追加 | modified | 12 | 12 | 24 | 
| [troubleshoot-sharepoint-query-permission-filtering.md](#item-85cf41) | minor update | SharePointの権限フィルタリングに関するトラブルシューティングの更新 | modified | 2 | 2 | 4 | 
| [tutorial-adls-gen2-indexer-acls.md](#item-6881a0) | minor update | ADLS Gen2インデクサーACLsに関するチュートリアルの更新 | modified | 3 | 12 | 15 | 
| [tutorial-multimodal.md](#item-718d2e) | minor update | マルチモーダルチュートリアルのAzure AI Visionスキルの更新 | modified | 1 | 1 | 2 | 
| [vector-search-filters.md](#item-f47c2b) | minor update | ベクトル検索フィルターに関するドキュメントの更新 | modified | 1 | 4 | 5 | 
| [vector-search-how-to-configure-vectorizer.md](#item-30ffd8) | minor update | ベクトル検索のベクトライザーに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [vector-search-how-to-query.md](#item-9bb93c) | minor update | ベクトル検索のクエリ設定に関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [vector-search-integrated-vectorization-ai-studio.md](#item-353fcc) | minor update | 統合ベクトル化に関するドキュメントのプレビュー表記の追加 | modified | 3 | 4 | 7 | 
| [vector-search-integrated-vectorization.md](#item-48219d) | minor update | ベクトル化に関するドキュメントのモデルカタログ情報更新 | modified | 1 | 1 | 2 | 
| [vector-search-multi-vector-fields.md](#item-9aa482) | minor update | Azure AI Searchにおけるマルチベクトルフィールドのプレビュー表記の追加 | modified | 4 | 3 | 7 | 
| [vector-search-vectorizer-ai-services-vision.md](#item-942a3e) | minor update | Azure Visionベクトライザーのプレビュー情報追加 | modified | 4 | 4 | 8 | 
| [vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md](#item-ebe7a3) | minor update | Microsoft Foundryモデルカタログベクトライザーのプレビュー情報追加 | modified | 4 | 4 | 8 | 
| [whats-new.md](#item-fa71b4) | minor update | Azure AI Search 更新情報の修正 | modified | 5 | 8 | 13 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-azure-sql.md{#item-89aa4d}

<details>
<summary>Diff</summary>
````diff
@@ -7,20 +7,14 @@ ms.topic: how-to
 ms.date: 08/14/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to create an indexed Azure SQL knowledge source with column mappings, authentication, and change detection so that rows from a SQL table or view can ground agentic retrieval responses.
 ---
 
 # Create an indexed Azure SQL knowledge source (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 An *indexed Azure SQL knowledge source* (preview) ingests rows from Azure SQL Database or Azure SQL Managed Instance into an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure SQL 知識ソースのインデックス作成に関する変更"
}
```

### Explanation
この変更では、Azure SQL 知識ソースのインデックス作成に関するドキュメントが修正されました。具体的には、顧客の意図を明確に示す文が新たに追加されました。この文は、アプリケーション開発者としてインデックスを持つ Azure SQL 知識ソースを作成したいという要求を伝え、列マッピング、認証、および変更検知機能に関する情報を強調しています。

また、元々存在していたいくつかの重要な注意事項が削除され、テキストが簡潔化されました。全体として、ドキュメントはより明確に目的を伝え、ユーザーが必要としている情報に迅速にアクセスできるようになっています。変更により、Azure SQL Database または Azure SQL Managed Instance からエージェントリトリーバルパイプラインにデータを取り込む方法が改善され、知識ベースとの統合が強調されています。

## articles/search/agentic-knowledge-source-how-to-blob.md{#item-ac6c8a}

<details>
<summary>Diff</summary>
````diff
@@ -7,24 +7,14 @@ ms.date: 09/02/2026
 ai-usage: ai-assisted
 ms.custom: doc-kit-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to create a blob knowledge source and configure its generated ingestion, enrichment, and access-control behavior so that content from Azure Blob Storage or ADLS Gen2 can ground agentic retrieval responses.
 ---
 
 # Create a blob knowledge source from Azure Blob Storage or ADLS Gen2
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [GA feature](./includes/previews/agentic-retrieval-ga-feature.md)]
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 A *blob knowledge source* ingests Azure Blob Storage or ADLS Gen2 content into an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
@@ -38,7 +28,7 @@ When you create a blob knowledge source, you specify an external data source, mo
 The generated indexer conforms to the *blob indexer*, whose prerequisites, supported document formats, and limitations also apply to blob knowledge sources. For more information, see the [blob indexer documentation](search-how-to-index-azure-blob-storage.md) and [indexer limits](search-limits-quotas-capacity.md#indexer-limits). If the generated skillset calls an external service, that skill's input and service limits also apply.
 
 > [!NOTE]
-> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](search-indexer-access-control-lists-and-role-based-access.md) or [Blob RBAC scopes](search-blob-indexer-role-based-access.md).
+> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata (preview)](search-indexer-access-control-lists-and-role-based-access.md) or [Blob RBAC scopes (preview)](search-blob-indexer-role-based-access.md).
 
 ### Usage support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blob 知識ソースの作成に関する変更"
}
```

### Explanation
この変更では、Azure Blob Storage または ADLS Gen2 からの blob 知識ソースの作成に関するドキュメントが更新されました。新たに追加された文は、アプリケーション開発者がblob 知識ソースを作成し、その生成されたインジェスト、エンリッチメント、およびアクセス制御の挙動を構成したいという顧客の意図を明確にしています。

これにより、ユーザーは Azure Blob Storage や ADLS Gen2 からのコンテンツがエージェントリトリーバルパイプラインに取り込まれるプロセスをより理解しやすくなります。また、以前の重要な注意事項の一部が削除され、テキスト全体が明瞭化されました。さらに、アクセス権の指定に関するノートが更新され、ADLS Gen2 の権限メタデータに関する情報がプレビューと明記されています。

全体として、この修正により、blob 知識ソースの設定や管理に関する指針が強化され、開発者が考慮すべき重要な情報が提供されています。

## articles/search/agentic-knowledge-source-how-to-fabric-data-agent.md{#item-900ecc}

<details>
<summary>Diff</summary>
````diff
@@ -6,20 +6,16 @@ ms.topic: how-to
 ms.date: 06/02/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to create a Fabric Data Agent knowledge source and authorize queries on behalf of end users so that agentic retrieval can return live, permission-aware answers, tables, and charts from Fabric data.
 ---
 
 # Create a Fabric Data Agent knowledge source (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> When you connect to Fabric IQ, you might incur costs, and data might be sent outside the Azure compliance boundary and processed according to the applicable service terms and data handling policies. It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
+When you connect to Fabric IQ, you might incur costs, and data might be sent outside the Azure compliance boundary and processed according to the applicable service terms and data handling policies.
 
 A *Fabric Data Agent knowledge source* (preview) connects your [Microsoft Fabric Data Agent](/fabric/data-science/concept-data-agent) to an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Fabric Data Agent 知識ソースの作成に関する変更"
}
```

### Explanation
この変更では、Fabric Data Agent 知識ソースの作成に関するドキュメントが更新され、アプリケーション開発者がエンドユーザーに代わってクエリを認可し、エージェントリトリーバルがライブでパーミッションを考慮した回答、テーブル、およびチャートを返すことができるようにすることに関する顧客の意図が新たに追加されました。

加えて、いくつかの重要な注意事項が削除され、接続に伴うコストやデータの取り扱いに関する情報が簡潔に表現されています。この更新により、Fabric Data Agent 知識ソースが Azure AI サーチのエージェントリトリーバルパイプラインにどのように接続されるか、そのプロセスがより明確に説明されます。全体として、この記事はユーザーが必要とする重要な情報を強調し、コンプライアンスの境界内でのデータ管理についての責任を再確認させる内容となっています。

## articles/search/agentic-knowledge-source-how-to-fabric-ontology.md{#item-1f2bb6}

<details>
<summary>Diff</summary>
````diff
@@ -6,20 +6,16 @@ ms.topic: how-to
 ms.date: 06/02/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to create a Fabric Ontology knowledge source and authorize queries on behalf of end users so that agentic retrieval can return permission-aware answers based on live Fabric data, business entities, and relationships.
 ---
 
 # Create a Fabric Ontology knowledge source (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> When you connect to Fabric IQ, you might incur costs, and data might be sent outside the Azure compliance boundary and processed according to the applicable service terms and data handling policies. It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
+When you connect to Fabric IQ, you might incur costs, and data might be sent outside the Azure compliance boundary and processed according to the applicable service terms and data handling policies.
 
 A *Fabric Ontology knowledge source* (preview) connects your [Microsoft Fabric ontology](/fabric/iq/ontology/overview) to an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Fabric Ontology 知識ソースの作成に関する変更"
}
```

### Explanation
この変更では、Fabric Ontology 知識ソースの作成に関するドキュメントが更新され、アプリケーション開発者がエンドユーザーに代わってクエリを認可し、エージェントリトリーバルがライブのFabricデータに基づくパーミッションを考慮した回答、ビジネスエンティティ、関係を返すことができるようにするという顧客の意図が追加されました。

重要な注意事項のいくつかが削除され、接続に伴うコストやデータ取り扱いに関する情報が簡潔に整理されています。この更新により、Fabric Ontology 知識ソースがどのようにAzure AI サーチのエージェントリトリーバルパイプラインに接続されるのかがより明確に示されており、ユーザーが効果的に知識ソースを管理できるようにするための重要な情報が提供されています。全体として、この記事は開発者が必要とする実用的なガイダンスを強調し、データ管理における責任について再確認させる内容となっています。

## articles/search/agentic-knowledge-source-how-to-file.md{#item-88f720}

<details>
<summary>Diff</summary>
````diff
@@ -7,20 +7,14 @@ ms.date: 08/21/2026
 ai-usage: ai-assisted
 ms.custom: doc-kit-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to create a file knowledge source and manage uploaded files so that I can ground knowledge base responses without provisioning Azure Storage.
 ---
 
 # Create a file knowledge source (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The preview APIs support connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 A *file knowledge source* (preview) uploads small-to-medium file sets directly to Azure AI Search for agentic retrieval. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイル知識ソースの作成に関する変更"
}
```

### Explanation
この変更では、ファイル知識ソースの作成に関するドキュメントが更新され、アプリケーション開発者がファイル知識ソースを作成し、アップロードしたファイルを管理することで、Azure Storageを用意することなく知識ベースの応答を支えることができるという顧客の意図が新たに追加されました。

重要事項のいくつかが削除され、より簡潔な形式で情報が提供されています。この更新により、ファイル知識ソースがどのようにAzure AI サーチに直接アップロードされ、エージェントリトリーバルが行われるのかが明確に示され、開発者が知識ソースを効果的に利用するための重要な情報が強調されています。また、利用者がより良い運用を行えるようにするためのガイダンスも含まれています。全体として、この記事はアプリケーション開発者にとって実用的かつ重要な指針を提供する内容となっています。

## articles/search/agentic-knowledge-source-how-to-mcp-server.md{#item-9a2e92}

<details>
<summary>Diff</summary>
````diff
@@ -7,29 +7,24 @@ ms.date: 08/17/2026
 ms.custom: doc-kit-assisted
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to create an MCP Server knowledge source and configure its authentication, tool selection, and result processing so that agentic retrieval can invoke selected external tools and use their live results.
 ---
 
 # Create an MCP Server knowledge source (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> MCP implementations are susceptible to risks, such as attacks, cascading failures, and loss of human oversight. You can mitigate these risks by vetting MCP servers for security and reliability, following [Microsoft's recommended practices](/azure/api-management/secure-mcp-servers) and [industry best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices), and implementing approval mechanisms and monitoring cascading behaviors.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 An *MCP Server knowledge source* (preview) connects any system that exposes a [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP)–compatible endpoint to an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
 MCP tools surface data and functionality from external systems as callable functions that agents invoke at query time. This makes MCP Server knowledge sources useful when the information you need lives in internal tools, third-party APIs, or custom backends that Azure AI Search doesn't natively support.
 
 Unlike indexed knowledge sources, MCP Server knowledge sources query live data directly at retrieval time. No ingestion pipeline is needed. You provide the MCP server URL and specify which tools Azure AI Search can call at query time.
 
+> [!WARNING]
+> MCP implementations are susceptible to risks, such as attacks, cascading failures, and loss of human oversight. You can mitigate these risks by vetting MCP servers for security and reliability, following [Microsoft's recommended practices](/azure/api-management/secure-mcp-servers) and [industry best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices), and implementing approval mechanisms and monitoring cascading behaviors.
+
 ### Usage support
 
 | [Azure portal](get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2026-08-01-preview&preserve-view=true) |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MCPサーバー知識ソースの作成に関する変更"
}
```

### Explanation
この変更では、MCPサーバー知識ソースの作成に関するドキュメントが更新され、アプリケーション開発者がMCPサーバー知識ソースを作成し、その認証、ツール選択、結果処理を構成することで、エージェントリトリーバルが選択した外部ツールを呼び出し、ライブの結果を利用できるようにするという顧客の意図が新たに追加されました。

重要事項の一部が改訂され、MCP実装に関連するリスクやそれを軽減するための手段についての情報が強調されています。この更新により、ユーザーはMCPサーバー知識ソースを使用して内部ツールやサードパーティのAPI、カスタムバックエンドからのデータを直接クエリする方法を理解できるようになります。また、MCPサーバーがライブデータを直接取得できる点が強調され、インジェストパイプラインが不要であることが明確に示されています。

全体として、この記事は開発者にとって有用な情報を提供し、エージェントリトリーバル機能をより効果的に活用するための指針を示す内容となっています。

## articles/search/agentic-knowledge-source-how-to-onelake.md{#item-ec7a80}

<details>
<summary>Diff</summary>
````diff
@@ -7,24 +7,14 @@ ms.topic: how-to
 ms.date: 09/02/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to create an indexed OneLake knowledge source and configure its generated ingestion, enrichment, and access-control behavior so that lakehouse files can ground agentic retrieval responses.
 ---
 
 # Create an indexed OneLake knowledge source
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [GA feature](./includes/previews/agentic-retrieval-ga-feature.md)]
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 An *indexed OneLake knowledge source* ingests Microsoft OneLake files into an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス付きOneLake知識ソースの作成に関する変更"
}
```

### Explanation
この変更では、インデックス付きOneLake知識ソースの作成に関するドキュメントが更新され、アプリケーション開発者がOneLakeファイルをインジェストし、生成されたインジェスト、強化、アクセス制御の動作を構成することで、Lakehouseファイルがエージェントリトリーバルの応答を支えることができるという顧客の意図が新たに追加されました。

ドキュメント内では、重要事項のいくつかが削除され、より簡潔で明確な情報が提供されています。この更新により、OneLake知識ソースがAzure AI サーチにどのように統合されるか、またそれがどのようにエージェントリトリーバル機能を活用するかがより明確になります。ラテラルな制限やアクセス権の管理についても言及されており、ユーザーが自分たちの用途に応じた適切な設定を行うための重要な情報が含まれています。

全体として、この記事は開発者にとって実用的かつ効果的な指針を提供し、Azure AIサーチを利用する上で必要な手続きを明確にしています。

## articles/search/agentic-knowledge-source-how-to-search-index.md{#item-09d366}

<details>
<summary>Diff</summary>
````diff
@@ -6,22 +6,14 @@ ms.topic: how-to
 ms.date: 08/14/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to create a search index knowledge source from an existing index and configure its retrieval fields, filters, and query guidance so that agentic retrieval can use relevant indexed content.
 ---
 
 # Create a search index knowledge source
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [GA feature](./includes/previews/agentic-retrieval-ga-feature.md)]
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 A *search index knowledge source* connects an existing Azure AI Search index, including its indexed text and vectors, to an agentic retrieval pipeline. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
@@ -294,9 +286,6 @@ Content-Type: application/json
 
 ### Persist a base filter on a knowledge source (preview)
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
-
 Starting with the `2026-05-01-preview` API version, a search index knowledge source can persist a default filter through the `baseFilter` property. Use `baseFilter` when the same filter expression should apply to every retrieve request that uses the knowledge source, so callers don't have to repeat the filter on every call.
 
 The following example stores a base filter on a search index knowledge source.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックス知識ソースの作成に関する変更"
}
```

### Explanation
この変更では、検索インデックス知識ソースを作成する方法に関するドキュメントが更新され、アプリケーション開発者が既存のインデックスから知識ソースを作成し、その取得フィールド、フィルター、およびクエリガイダンスを構成することで、エージェントリトリーバルが関連するインデックス化されたコンテンツを活用できるようにするという顧客の意図が新たに追加されました。

一部の重要な情報が削除され、内容が簡潔に整理されました。具体的には、プレビューの機能に関する注意事項が削除され、代わりに「プレビュー条件」が追加されました。これにより、ユーザーは知識ソースがどのようにアクティブなAzure AI サーチインデックスと接続され、エージェントリトリーバルパイプラインにどのように関連付けられるかを理解しやすくなっています。

全体として、この記事は検索インデックス知識ソースを効果的に利用するための実用的な手引きを提供し、ユーザーがエージェントリトリーバル機能を最大限に活用できるようにすることを目指しています。

## articles/search/agentic-knowledge-source-how-to-sharepoint-indexed.md{#item-fe72fc}

<details>
<summary>Diff</summary>
````diff
@@ -7,24 +7,14 @@ ms.date: 09/02/2026
 ai-usage: ai-assisted
 ms.custom: doc-kit-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to create an indexed SharePoint knowledge source and configure document-level access and protected Azure dependencies so that SharePoint content can ground agentic retrieval responses.
 ---
 
 # Create an indexed SharePoint knowledge source (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [Preview feature](./includes/previews/agentic-retrieval-preview-feature.md)]
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 An *indexed SharePoint knowledge source* (preview) ingests SharePoint content into an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス付きSharePoint知識ソースの作成に関する変更"
}
```

### Explanation
この変更では、インデックス付きSharePoint知識ソースを作成する方法に関するドキュメントが更新され、アプリケーション開発者がインデックス付きSharePoint知識ソースを作成し、文書レベルのアクセスおよび保護されたAzure依存関係を構成することで、SharePointコンテンツがエージェントリトリーバルの応答を支えることができるという顧客の意図が新たに追加されました。

一部の重要情報が削除され、より簡潔で明確な内容に整理されました。具体的には、プレビュー機能に関する情報が削除され、新たに「プレビュー条件」が追加され、ユーザーがこれらの機能を利用する際に考慮すべき点を明確にしています。

この更新により、インデックス付きSharePoint知識ソースがAzure AI サーチのエージェントリトリーバルパイプラインにどのように統合され、機能するかがより理解しやすくなります。全体として、この記事はSharePointコンテンツを効果的に利用するための実用的な手引きを提供し、エージェントリトリーバル機能を最大限に引き出す方法を示しています。

## articles/search/agentic-knowledge-source-how-to-sharepoint-remote.md{#item-79d019}

<details>
<summary>Diff</summary>
````diff
@@ -6,22 +6,14 @@ ms.topic: how-to
 ms.date: 09/03/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to create a remote SharePoint knowledge source, scope its live content, and handle query-time user authorization and SharePoint response data so that agentic retrieval can use content each user is permitted to access.
 ---
 
 # Create a remote SharePoint knowledge source (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [Preview feature](./includes/previews/agentic-retrieval-preview-feature.md)]
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 A *remote SharePoint knowledge source* (preview) uses the [Copilot Retrieval API (preview)](/microsoft-365-copilot/extensibility/api/ai-services/retrieval/overview) to query textual content directly from SharePoint in Microsoft 365. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リモートSharePoint知識ソースの作成に関する変更"
}
```

### Explanation
この変更では、リモートSharePoint知識ソースを作成する方法に関するドキュメントが更新され、アプリケーション開発者がリモートSharePoint知識ソースを作成し、そのライブコンテンツをスコープ設定し、クエリ時のユーザー認証およびSharePoint応答データを処理することで、エージェントリトリーバルが各ユーザーがアクセスを許可されたコンテンツを利用できるようにするという顧客の意図が新たに追加されました。

いくつかの不要な情報が削除され、より簡潔に整理されました。特に、プレビューボタンや重要な注意事項が短縮され、代わりに「プレビュー条件」が追加されました。これにより、ユーザーがその機能の利用時に考慮すべき点が明確に示されます。

更新された情報により、リモートSharePoint知識ソースがMicrosoft 365から直接テキストコンテンツを取得するためにCopilot Retrieval APIをどのように活用できるかがわかりやすくなり、またエージェントリトリーバル機能への統合方法についても明確な指針が提供されています。全体として、この記事はリモートSharePointコンテンツを効果的に活用するための実用的な手引きを提供します。

## articles/search/agentic-knowledge-source-how-to-web-manage.md{#item-af61ec}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.custom:
 ms.topic: how-to
 ms.date: 04/30/2026
 ai-usage: ai-assisted
+#customer intent: As an Azure administrator, I want to check, enable, or disable Web Knowledge Source access so that I can govern its use across all Azure AI Search services in a subscription.
 ---
 
 # Manage access to Web Knowledge Source in your Azure subscription
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Web知識ソースアクセス管理に関する変更"
}
```

### Explanation
この変更では、Web知識ソースに対するアクセス管理に関するドキュメントが更新され、Azure管理者がWeb知識ソースのアクセスを確認、有効化、または無効化することで、サブスクリプション内のすべてのAzure AI Searchサービスに対するその利用を管理できるという顧客の意図が新たに追加されました。

具体的には、一行の情報が追加されただけですが、これによりAzure管理者の視点からのニーズや目的が明確に示され、利用者がこの機能をどのように活用できるかに対する理解が深まります。全体として、この変更はWeb知識ソースのアクセス管理に関する重要なポイントを強調し、管理者が意思決定を行う際に役立つ情報を提供しています。

## articles/search/agentic-knowledge-source-how-to-web.md{#item-6b21d0}

<details>
<summary>Diff</summary>
````diff
@@ -8,22 +8,14 @@ ms.topic: how-to
 ms.date: 06/02/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to create and scope a Web Knowledge Source while accounting for its usage terms and limitations so that my knowledge base can supplement proprietary content with current information from permitted public web domains.
 ---
 
 # Create a Web Knowledge Source resource
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [GA feature](./includes/previews/agentic-retrieval-ga-feature.md)]
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 > [!IMPORTANT]
 > + Web Knowledge Source, which uses Grounding with Bing Search and/or Grounding with Bing Custom Search, is a [First Party Consumption Service](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/EAEAS) governed by the [Grounding with Bing terms of use](https://www.microsoft.com/en-us/bing/apis/grounding-legal-enterprise) and the [Microsoft Privacy Statement](https://www.microsoft.com/privacy/privacystatement).
@@ -96,7 +88,7 @@ Web Knowledge Source works best alongside other knowledge sources. Use it when y
 
 + For the 2026-04-01 API version, the knowledge base must include a model reference to provide the LLM for web content summarization. Retrieval is always extractive (cited summaries). Answer synthesis and configurable reasoning effort aren't available in this version.
 
-+ For the `2026-08-01-preview` API version, the knowledge base model reference also enables [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md), which produces a single LLM-formulated response instead of extracted citations.
++ For the `2026-08-01-preview` API version, the knowledge base model reference also enables [answer synthesis (preview)](agentic-retrieval-how-to-answer-synthesis.md), which produces a single LLM-formulated response instead of extracted citations.
 
 ## Check for existing knowledge sources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Web知識ソースリソースの管理に関する変更"
}
```

### Explanation
この変更では、Web知識ソースを作成する方法に関するドキュメントが更新され、アプリケーション開発者がWeb知識ソースを作成し、その使用条件と制限を考慮に入れることで、知識ベースが許可された公開ウェブドメインからの最新情報で独自のコンテンツを補完できるようにするという顧客の意図が新たに追加されました。

具体的には、重要事項が簡略化され、プレビューボタンに関する詳細が削除される一方で、Web知識ソースがBing検索およびカスタム検索を用いる「ファーストパーティ消費サービス」であることについての情報が追加されました。これにより、利用者がこのサービスの使用に関する法律やプライバシー条件について理解する手助けが強化されました。

また、APIバージョンに関する明確な記述が追加され、2026-04-01 APIバージョンにおいては知識ベースにモデル参照が必要であることや、データ取得が常に抽出的であることが強調されています。これにより、ユーザーは機能の違いを認識しやすくなり、適切な使用方法の理解が促進されます。全体として、これらの変更はWeb知識ソースにおける重要な運用上の考慮事項を強調し、開発者がその機能を効果的に利用できるようにするための情報を提供しています。

## articles/search/agentic-knowledge-source-how-to-work-iq.md{#item-94718e}

<details>
<summary>Diff</summary>
````diff
@@ -8,20 +8,16 @@ ms.custom:
   - dev-focus
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to set up delegated Microsoft Entra authentication, create a Work IQ knowledge source, and process its response data so that agentic retrieval can return permission-aware organizational intelligence.
 ---
 
 # Create a Work IQ knowledge source (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> When you connect to Work IQ, you might incur costs, and data might be sent outside the Azure compliance boundary and processed according to the applicable service terms and data handling policies. It's your responsibility to manage whether your data flows outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This responsibility includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
+When you connect to Work IQ, you might incur costs, and data might be sent outside the Azure compliance boundary and processed according to the applicable service terms and data handling policies.
 
 A *Work IQ knowledge source* (preview) connects [Work IQ](/microsoft-365/copilot/extensibility/work-iq) to an agentic retrieval pipeline in Azure AI Search. [Knowledge sources](agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when the knowledge base is [queried at runtime](agentic-retrieval-how-to-retrieve.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Work IQ知識ソースの作成に関する変更"
}
```

### Explanation
この変更では、Work IQ知識ソースの作成に関するドキュメントが更新され、アプリケーション開発者が委任されたMicrosoft Entra認証を設定し、Work IQ知識ソースを作成し、その応答データを処理できるようにするための顧客の意図が明示的に追加されました。これにより、ユーザーが権限に配慮した組織の知識を返すエージェント型の検索機能を利用するための情報が強調されています。

具体的には、重要事項に関する表現が簡略化され、Work IQへの接続に関するコストの発生や、データの処理がAzureのコンプライアンス境界の外で行われる可能性について明記されました。また、関連するサービス条件やデータ処理ポリシーに従ってデータが扱われることも言及されています。これにより、利用者はデータの取り扱いに関する責任をより明確に理解できるようになっています。

全体として、この変更はWork IQ知識ソースの使用方法とその影響に関する重要な情報を提供し、開発者がこの新機能を効果的に利用できるようにサポートしています。

## articles/search/agentic-knowledge-source-overview.md{#item-dcf29a}

<details>
<summary>Diff</summary>
````diff
@@ -5,20 +5,14 @@ ms.service: azure-ai-search
 ms.topic: concept-article
 ms.date: 09/01/2026
 ai-usage: ai-assisted
+#customer intent: As a solution architect, I want to compare supported indexed and remote knowledge sources and understand their ingestion, security, enrichment, and retrieval options so that I can select and design appropriate sources for an agentic retrieval solution.
 ---
 
 # What is a knowledge source?
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [GA announcement](./includes/previews/agentic-retrieval-ga-announcement.md)]
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 A *knowledge source* is a top-level resource on your Azure AI Search service that defines the content used in an agentic retrieval pipeline. Each knowledge source is either indexed or remote, which determines how the content is ingested, processed, and queried. Knowledge sources are required components of a knowledge base.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ソースの概要に関する変更"
}
```

### Explanation
この変更では、知識ソースに関する概要ドキュメントが更新され、ソリューションアーキテクトがサポートされているインデックスおよびリモートの知識ソースを比較し、それらの取り込み、セキュリティ、強化、および検索オプションを理解できるようにするという顧客の意図が追加されました。これにより、適切な知識ソースを選択し、エージェント型の検索ソリューションを設計するための情報が強調されています。

具体的には、重要事項の表現が簡略化され、GAアナウンスメントのインクルード部分が削除されました。また、知識ソースの定義やその役割についての説明が明確化され、各知識ソースがインデックス型またはリモート型であることが具体的に示されています。これにより、知識ソースがどのように取り込まれ、処理され、クエリされるのかがより分かりやすく説明されています。

全体として、この変更は知識ソースの役割とその機能に関する重要な情報を提供し、ユーザーがエージェント型の検索アプローチに適した決定を行う際の手助けとなることを目指しています。

## articles/search/agentic-retrieval-how-to-answer-synthesis.md{#item-f44e99}

<details>
<summary>Diff</summary>
````diff
@@ -6,22 +6,14 @@ ms.topic: how-to
 ms.date: 06/02/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to configure answer synthesis at the knowledge base or request level and process its output so that users receive instructed natural-language answers with citations instead of raw grounding chunks.
 ---
 
 # Use answer synthesis for citation-backed responses in Azure AI Search (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [Preview feature](./includes/previews/agentic-retrieval-preview-feature.md)]
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 By default, a knowledge base in Azure AI Search performs *data extraction*, which returns raw grounding chunks from your knowledge sources. Data extraction is useful for retrieving specific information but lacks the context and reasoning necessary for complex queries.
 
@@ -71,7 +63,7 @@ You can set this property in a knowledge base or a retrieve request. The knowled
 
 - The `minimal` retrieval reasoning effort disables LLM processing, so it's incompatible with answer synthesis in both knowledge base definitions and retrieve requests. For more information, see [Set the retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md).
 
-- Answer synthesis incurs pay-as-you-go charges from Azure OpenAI, which are based on the number of input and output tokens. Charges appear under the LLM assigned to the knowledge base. For more information, see [Availability and pricing](agentic-retrieval-overview.md#availability-and-pricing).
+- Answer synthesis incurs pay-as-you-go charges from Azure OpenAI, which are based on the number of input and output tokens. Charges appear under the LLM assigned to the knowledge base. For more information, see [Region availability, limits, and billing](agentic-retrieval-overview.md#region-availability-limits-and-billing).
 
 ## Enable answer synthesis in a knowledge base
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "回答合成に関する変更"
}
```

### Explanation
この変更では、Azure AI Searchにおける回答合成の使用方法に関するドキュメントが更新され、アプリケーション開発者が知識ベースまたはリクエストレベルで回答合成を設定し、その出力を処理することで、ユーザーが生の根拠のチャンクではなく、引用を含む自然言語で指示された回答を受け取ることができるという顧客の意図が追加されました。

具体的には、重要事項に関するセクションが簡略化され、プレビュー機能に関するインクルード部分が削除されました。また、知識ベースがデフォルトで行うデータ抽出の方法とその限界についての説明が強調されています。さらに、回答合成によるコストがAzure OpenAIに基づくものであることが示されていますが、料金の詳細に関しては「地域の可用性、制限、および請求」に変更されています。

全体として、この変更は回答合成の機能やその使用に関する重要な情報を提供し、開発者がユーザーに対してより効果的な回答を提供するための手助けを目指しています。

## articles/search/agentic-retrieval-how-to-configure-freshness.md{#item-0b04e6}

<details>
<summary>Diff</summary>
````diff
@@ -6,20 +6,14 @@ ms.topic: how-to
 ms.date: 06/02/2026
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to determine when freshness-aware retrieval is appropriate and configure and validate a freshness policy so that newer indexed content receives a ranking preference without excluding older relevant content.
 ---
 
 # Configure freshness-aware retrieval in Azure AI Search (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 *Freshness-aware retrieval* (preview) lets an indexed knowledge source prefer newer content during agentic retrieval. The knowledge source can include a freshness policy so Azure AI Search biases ranking toward recent documents without requiring callers to send custom ranking logic on each retrieve request.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フレッシュネス対応の取得設定に関する変更"
}
```

### Explanation
この変更では、Azure AI Searchにおけるフレッシュネス対応の取得を設定する方法に関するドキュメントが更新され、アプリケーション開発者がフレッシュネスを考慮した取得が適切なタイミングを判断し、フレッシュネスポリシーを設定・検証することで、新しいインデックスされたコンテンツがランキングで優先されつつ、古い関連コンテンツも除外されないようにすることを目的とした顧客の意図が追加されました。

具体的には、重要事項に関するセクションが簡略化され、プレビュー機能に関する詳細が削除されました。フレッシュネス対応の取得がどのように動作し、どう新しいコンテンツを優先するかについての説明が明確化されました。この機能は、インデックスされた知識ソースが新しいドキュメントを優先する際に、カスタムランキング論理を毎回送信する必要がないことを強調しています。

この変更は、フレッシュネスを考慮したデータ取得の機能とその利点を詳述することで、開発者がより効果的にアプリケーションを構築できるよう支援しています。

## articles/search/agentic-retrieval-how-to-create-index.md{#item-3fbd2e}

<details>
<summary>Diff</summary>
````diff
@@ -5,14 +5,13 @@ ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 06/02/2026
 ai-usage: ai-assisted
+#customer intent: As an application developer, I want to create or validate an index against agentic retrieval criteria and configure its relevance behavior so that I can use the index with an indexed knowledge source.
 ---
 
 # Create an index for agentic retrieval in Azure AI Search
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [GA announcement](./includes/previews/agentic-retrieval-ga-announcement.md)]
-
 This article explains the required index fields and configurations for agentic retrieval. None of these requirements are new. You can use an existing index that meets the criteria, even if it was created with an earlier API version.
 
 Each indexed knowledge source depends on an underlying index. Depending on how you set up your pipeline, the index can be one of the following:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント取得用インデックス作成に関する変更"
}
```

### Explanation
この変更では、Azure AI Searchにおけるエージェント取得用のインデックスを作成する方法に関するドキュメントが更新され、アプリケーション開発者がエージェント取得基準に対してインデックスを作成または検証し、その関連性の振る舞いを設定することができるようにする意図が追加されました。これにより、開発者はインデックスをインデックスされた知識ソースと共に使用できるようになります。

具体的には、インデックス作成に関するセクションからGA発表に関するインクルード部分が削除されましたが、それ以外の要件は変更されていません。記事内では、エージェント取得に必要なインデックスフィールドと設定について説明されており、これらの要件は新しいものではないことが強調されています。開発者は、これらの基準を満たす既存のインデックスを使用することも可能です。

全体として、この変更はエージェント取得用のインデックス作成に関連する重要な情報を提供し、開発者がその機能を有効に活用できるように支援しています。

## articles/search/agentic-retrieval-how-to-create-knowledge-base.md{#item-7df0e2}

<details>
<summary>Diff</summary>
````diff
@@ -9,22 +9,14 @@ ms.custom:
   - doc-kit-assisted
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to create and configure a knowledge base that references my knowledge sources and defines retrieval behavior so that my application can run agentic retrieval.
 ---
 
 # Create a knowledge base in Azure AI Search
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [GA feature](./includes/previews/agentic-retrieval-ga-feature.md)]
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 In Azure AI Search, a *knowledge base* is a top-level object that orchestrates [agentic retrieval](agentic-retrieval-overview.md). It defines which knowledge sources to query and the default behavior for retrieval operations. At query time, the [retrieve method](agentic-retrieval-how-to-retrieve.md) targets the knowledge base to run the configured retrieval pipeline.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジベース作成に関する変更"
}
```

### Explanation
この変更では、Azure AI Searchにおけるナレッジベースの作成方法に関するドキュメントが更新され、アプリケーション開発者が自分の知識ソースを参照し、取得動作を定義するナレッジベースを作成および構成する意図が追加されました。これは、開発者のアプリケーションがエージェント取得を実行できるようにすることを目的としています。

具体的には、重要事項に関するセクションが簡略化され、GA機能についてのインクルード文が削除されています。また、ナレッジベースの定義とその役割、及び取得操作のデフォルトの動作についての説明が残されています。このナレッジベースは、エージェント取得を調整するトップレベルのオブジェクトとして機能し、どの知識ソースをクエリするかを指定し、取得パイプラインを実行するためのメソッドを明示しています。

全体として、この変更はナレッジベースの重要性を強調し、開発者がその機能を活用してアプリケーションを最適化するための情報を提供しています。

## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -1,33 +1,25 @@
 ---
 title: 'Tutorial: Build an Agentic Retrieval Solution'
-description: Build an agentic retrieval solution that connects Azure AI Search to Foundry Agent Service via MCP. Follow this tutorial to create a knowledge base and agent.
+description: Build an agentic retrieval solution that connects Azure AI Search to Foundry Agent Service through MCP.
 ms.date: 08/06/2026
 ms.service: azure-ai-search
 ms.topic: tutorial
 ms.custom:
   - build-2025
 ai-usage: ai-assisted
+#customer intent: As an application developer, I want to build and test an end-to-end agentic retrieval solution so that a Foundry agent can use an Azure AI Search knowledge base through MCP to return grounded responses.
 ---
 
 # Tutorial: Build an end-to-end agentic retrieval solution using Azure AI Search
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [Preview API usage](./includes/previews/agentic-retrieval-preview-api-usage.md)]
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> MCP implementations are susceptible to risks, such as attacks, cascading failures, and loss of human oversight. You can mitigate these risks by vetting MCP servers for security and reliability, following [Microsoft's recommended practices](/azure/api-management/secure-mcp-servers) and [industry best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices), and implementing approval mechanisms and monitoring cascading behaviors.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 Learn how to create an intelligent, MCP-enabled solution that integrates Azure AI Search with Foundry Agent Service for [agentic retrieval](agentic-retrieval-overview.md). You can use this architecture for conversational applications that require complex reasoning over large knowledge domains, such as customer support or technical troubleshooting.
 
+This tutorial uses preview REST API surfaces in two places. The knowledge base uses `output_mode` and `retrieval_reasoning_effort` (preview) to explicitly specify extractive output and minimal reasoning, although equivalent behavior is generally available. The project connection uses `RemoteTool` (preview) and the project managed identity to authenticate to Azure AI Search.
+
 In this tutorial, you:
 
 > [!div class="checklist"]
@@ -324,9 +316,9 @@ The following code creates a knowledge base that orchestrates agentic retrieval
 
 For integration with Foundry Agent Service, the knowledge base is configured with the following parameters:
 
-+ `output_mode` is set to extractive data, which provides the agent with verbatim, unprocessed content for grounding and reasoning. The alternative mode, answer synthesis, returns pregenerated answers that limit the agent's ability to reason over source content.
++ `output_mode` (preview) is set to extractive data, which provides the agent with verbatim, unprocessed content for grounding and reasoning. The alternative mode, answer synthesis, returns pregenerated answers that limit the agent's ability to reason over source content.
 
-+ `retrieval_reasoning_effort` is set to minimal effort, which bypasses LLM-based query planning to reduce costs and latency. For other reasoning efforts, the knowledge base uses an LLM to reformulate user queries before retrieval.
++ `retrieval_reasoning_effort` (preview) is set to minimal effort, which bypasses LLM-based query planning to reduce costs and latency. For other reasoning efforts, the knowledge base uses an LLM to reformulate user queries before retrieval.
 
 For more information about this step, see [Create a knowledge base in Azure AI Search](agentic-retrieval-how-to-create-knowledge-base.md).
 
@@ -368,7 +360,7 @@ list(project_client.agents.list())
 
 ### Create a project connection
 
-The following code creates a project connection in Microsoft Foundry that points to the MCP endpoint of your knowledge base. This connection uses your project managed identity to authenticate to Azure AI Search.
+The following code creates a `RemoteTool` project connection (preview) in Microsoft Foundry that points to the MCP endpoint of your knowledge base. This connection uses your project managed identity to authenticate to Azure AI Search.
 
 ```python
 import requests
@@ -402,6 +394,9 @@ print(f"Connection '{project_connection_name}' created or updated successfully."
 
 ### Create an agent with the MCP tool
 
+> [!WARNING]
+> MCP implementations are susceptible to risks, such as attacks, cascading failures, and loss of human oversight. You can mitigate these risks by vetting MCP servers for security and reliability, following [Microsoft's recommended practices](/azure/api-management/secure-mcp-servers) and [industry best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices), and implementing approval mechanisms and monitoring cascading behaviors.
+
 The following code creates an agent configured with the MCP tool. When the agent receives a user query, it can call your knowledge base through the MCP tool to retrieve relevant content for response grounding.
 
 The agent definition includes instructions that specify its behavior and the project connection you previously created. Based on our experiments, these instructions are effective in maximizing the accuracy of knowledge base invocations and ensuring proper citation formatting.
@@ -611,7 +606,7 @@ By default, search results from knowledge bases are consolidated into a large, u
 
 ## Control the number of subqueries
 
-You can control the number of subqueries by [setting the retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) on the knowledge base. The reasoning effort determines the level of LLM processing for query planning, ranging from minimal (no LLM processing) to medium (deeper search and follow-up iterations).
+You can control the number of subqueries by [setting the retrieval reasoning effort (preview)](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) on the knowledge base. The reasoning effort determines the level of LLM processing for query planning, ranging from minimal (no LLM processing) to medium (deeper search and follow-up iterations).
 
 For non-minimal reasoning efforts, the LLM determines the number of subqueries based on the following factors:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント取得ソリューション構築チュートリアルの更新"
}
```

### Explanation
この変更では、Azure AI Searchを使用してエージェント取得ソリューションを構築するためのチュートリアルが更新され、アプリケーション開発者がエンドツーエンドのエージェント取得ソリューションを構築してテストできるようにする情報が追加されました。具体的には、FoundryエージェントがAzure AI Searchのナレッジベースを通じて実用的な応答を返すことができるようになります。

このチュートリアルでは、MCPを介してAzure AI SearchとFoundry Agent Serviceを接続する方法が説明されていますが、重要事項に関するセクションが簡略化され、プレビューAPIの使用についての情報が引き続き提供されています。また、取得に関する理由付けの設定やプロジェクト接続の詳細が追加され、特定のパラメータがプレビュー版であることを明記しています。

さらに、MCP実装に関するセキュリティリスクについての警告が追加され、適切なセキュリティ対策を講じる必要性が強調されています。これらの変更は、開発者がエージェント取得ソリューションを構築する際の指針をより明確にし、責任あるAIの実装やセキュリティ面での考慮を促す内容となっています。

## articles/search/agentic-retrieval-how-to-enable-disable.md{#item-44591a}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ ms.update-cycle: 180-days
 ms.topic: how-to
 ms.date: 06/16/2026
 ai-usage: ai-assisted
+#customer intent: As an Azure administrator, I want to understand agentic retrieval billing plans and control paid usage independently from semantic ranker billing so that I can manage service availability after the monthly free allowance is consumed.
 ---
 
 # Enable or disable agentic retrieval billing
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント取得の課金計画に関する情報追加"
}
```

### Explanation
この変更では、Azureの管理者がエージェント取得の課金計画を理解し、セマンティックランカーの課金とは独立して有料使用を管理できるようにする意図が文書に追加されました。この更新により、エージェント取得の課金オプションを適切に管理し、月々の無料枠が消費された後のサービスの可用性を確保するための情報が提供されます。

具体的には、ドキュメントの冒頭に新しいカスタマーインテントの説明が追加され、Azure管理者が必要とする情報にフォーカスがあてられています。この変更は、使用状況の管理とオプションの理解を助けるためのものであり、Azureのサービスをより効果的に活用するためのガイダンスを提供しています。

## articles/search/agentic-retrieval-how-to-image-serving.md{#item-48db70}

<details>
<summary>Diff</summary>
````diff
@@ -6,22 +6,14 @@ ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 08/18/2026
 ai-usage: ai-assisted
+#customer intent: As an application developer, I want to configure asset storage and access, enable image serving, and inspect its retrieval activity so that answer synthesis can use document-embedded images and my application can retrieve authorized image assets.
 ---
 
 # Surface document-embedded images in agentic retrieval (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 Use *image serving* (preview) to surface images embedded in your source documents (such as diagrams, charts, infographics, scanned forms, and product images) during agentic retrieval, so your large language model (LLM) can reason over visual context alongside text when it synthesizes an answer.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント取得における画像サービングの有効化に関する情報追加"
}
```

### Explanation
この変更では、「エージェント取得」において、ソース文書に埋め込まれた画像をサーブするための情報が更新されました。具体的には、アプリケーション開発者が資産ストレージとアクセスを構成し、画像サービングを有効にし、その取得活動を検査できるようにすることが強調されています。また、回答合成が文書に埋め込まれた画像を使用できるようにするためのガイダンスが提供されています。

ドキュメントの冒頭に新しいカスタマーインテントが追加され、開発者が画像を活用した回答合成を行えるよう支援する内容になっています。一方で、重要情報に関するセクションが削除され、過剰な注意事項が省略されましたが、これはドキュメントの明瞭性を高めるための措置と考えられます。この変更により、開発者がエージェント取得機能をより効果的に利用できるようになることを目的としています。

## articles/search/agentic-retrieval-how-to-migrate.md{#item-9653ea}

<details>
<summary>Diff</summary>
````diff
@@ -8,20 +8,14 @@ ms.custom:
   - dev-focus
   - doc-kit-assisted
 ai-usage: ai-assisted
+#customer intent: As an application developer, I want to understand version-specific changes and migrate agentic retrieval code and resources so that my existing solution behaves as before on a newer API version.
 ---
 
 # Migrate agentic retrieval code to the latest version
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 If your [agentic retrieval](agentic-retrieval-overview.md) code targets an earlier API version, this article explains when and how to migrate to a newer version. It also describes breaking and nonbreaking changes for all API versions that support agentic retrieval.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント取得コードの移行に関する情報追加"
}
```

### Explanation
この変更では、エージェント取得のコードを新しいAPIバージョンに移行する際のガイダンスが改訂されました。具体的には、アプリケーション開発者がバージョン固有の変更を理解し、既存のソリューションが新しいAPIバージョンでもこれまで通りに動作するようにするためのサポートが強調されています。

ドキュメントには新しくカスタマーインテントが追加されており、開発者が移行プロセスを理解しやすくすることを目的としています。また、重要情報に関する説明が削除され、文書が簡潔になりました。さらに、エージェント取得のAPIバージョン間の破壊的変更と非破壊的変更について説明する内容が強調されており、開発者が移行作業をスムーズに行えるように配慮されています。これにより、ユーザーの体験を向上させることを図っています。

## articles/search/agentic-retrieval-how-to-retrieve.md{#item-d739cf}

<details>
<summary>Diff</summary>
````diff
@@ -9,22 +9,14 @@ ms.custom:
   - doc-kit-assisted
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to query a knowledge base through the retrieve action or MCP endpoint, control retrieval behavior and query-time authorization, and process responses so that my application or agent can use grounded content.
 ---
 
 # Query a knowledge base using the retrieve action or MCP endpoint
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [GA feature](./includes/previews/agentic-retrieval-ga-feature.md)]
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 In an agentic retrieval pipeline, the [retrieve action](/rest/api/searchservice/knowledge-retrieval/retrieve) invokes parallel query processing from a knowledge base. You can call the retrieve action directly using the Search Service REST APIs or an Azure SDK. Each knowledge base also exposes a Model Context Protocol (MCP) endpoint for consumption by MCP-compatible agents.
 
@@ -527,7 +519,7 @@ To confirm which mode ran, check whether the knowledge source's references inclu
 
 For knowledge sources that target a search index, the implied query type is `semantic`, and there's no search mode. When reranking runs, query execution uses `semanticConfigurationName`. Other source settings, including `searchFields` and `sourceDataFields`, apply in both modes.
 
-Agentic retrieval doesn't accept `scoringProfile` or `scoringParameters` inputs. If you need recency bias for indexed knowledge sources, use [freshness-aware retrieval](agentic-retrieval-how-to-configure-freshness.md) instead of an index scoring profile.
+Agentic retrieval doesn't accept `scoringProfile` or `scoringParameters` inputs. If you need recency bias for indexed knowledge sources, use [freshness-aware retrieval (preview)](agentic-retrieval-how-to-configure-freshness.md) instead of an index scoring profile.
 
 If the index includes vector fields, you need a valid vectorizer definition so the agentic retrieval engine can vectorize query inputs. Otherwise, vector fields are ignored.
 
@@ -1271,7 +1263,7 @@ The retrieve action returns three main components:
 
 # [2026-08-01-preview](#tab/2026-08-01-preview)
 
-+ [Extracted response](#extracted-response) or [synthesized answer](agentic-retrieval-how-to-answer-synthesis.md) (depending on output mode)
++ [Extracted response](#extracted-response) or [synthesized answer (preview)](agentic-retrieval-how-to-answer-synthesis.md) (depending on output mode)
 + [Activity array](#activity-array)
 + [References array](#references-array)
 
@@ -1330,12 +1322,12 @@ The activity array includes the following components:
 | Section | Description |
 | --------- | ------------- |
 | Source-specific activity | For each knowledge source included in the query, this section reports on elapsed time and which arguments were used in the query, including semantic ranker. Knowledge source types include `searchIndex`, `azureBlob`, and other [supported knowledge sources](agentic-knowledge-source-overview.md#supported-knowledge-sources). |
-| `agenticReasoning` | This section reports on token consumption for agentic reasoning during retrieval, which depends on the specified [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). |
+| `agenticReasoning` | This section reports on token consumption for agentic reasoning during retrieval, which depends on the specified [retrieval reasoning effort (preview)](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). |
 | `modelQueryPlanning` | For knowledge bases that use an LLM for query planning, this section reports on the token count used for input and the token count for the subqueries. It includes a `model` field with a `modelName` field containing the public model name, not the deployment name, of the model that ran the activity. |
-| `modelAnswerSynthesis` | For knowledge bases that use [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md), this section reports on the token count for formulating the answer and the token count of the answer output. It includes a `model` field with a `modelName` field containing the public model name, not the deployment name, of the model that ran the activity. |
+| `modelAnswerSynthesis` | For knowledge bases that use [answer synthesis (preview)](agentic-retrieval-how-to-answer-synthesis.md), this section reports on the token count for formulating the answer and the token count of the answer output. It includes a `model` field with a `modelName` field containing the public model name, not the deployment name, of the model that ran the activity. |
 | `modelWebSummarization` | For knowledge bases that use web summarization, this section reports on token consumption for summarizing web results. It includes a `model` field with a `modelName` field containing the public model name, not the deployment name, of the model that ran the activity. |
 | `model` | For model-backed activity records, this section identifies the model used to perform the activity. This section appears only when you set `includeActivity` to `true`. |
-| `imageServing` | For knowledge sources that have [image serving](agentic-retrieval-how-to-image-serving.md) enabled, this section reports `imagesRetrieved`, `imagesSentToModel`, `totalImageSizeBytes`, and whether indexing-time `verbalizationUsed` was on. Inspect `verbalizationUsed` and `imagesSentToModel` independently. A response can report `verbalizationUsed` as `true` and still send images to the downstream model. To find the number of dropped images, subtract `imagesSentToModel` from `imagesRetrieved`. |
+| `imageServing` | For knowledge sources that have [image serving (preview)](agentic-retrieval-how-to-image-serving.md) enabled, this section reports `imagesRetrieved`, `imagesSentToModel`, `totalImageSizeBytes`, and whether indexing-time `verbalizationUsed` was on. Inspect `verbalizationUsed` and `imagesSentToModel` independently. A response can report `verbalizationUsed` as `true` and still send images to the downstream model. To find the number of dropped images, subtract `imagesSentToModel` from `imagesRetrieved`. |
 
 # [2026-04-01](#tab/2026-04-01)
 
@@ -2798,7 +2790,7 @@ For a model activity error, use the activity `type` to identify the failed proce
 
 If your application permits partial results, process the successful results and record each failed source or model stage. Correct configuration, authorization, and permission errors before you retry. For throttling, timeout, or transient availability failures, use bounded retries with backoff.
 
-If results are unsafe without a specific source and its source type supports [`alwaysQuerySource`](#require-a-knowledge-source-to-succeed), set both `alwaysQuerySource` and `failOnError`. The first option ensures the source is selected, and the second returns a hard error if querying it fails. [MCP server knowledge sources](agentic-knowledge-source-how-to-mcp-server.md) don't support `alwaysQuerySource`; for those sources, `failOnError` applies only when the source is selected. `failOnError` doesn't apply to model activity failures.
+If results are unsafe without a specific source and its source type supports [`alwaysQuerySource`](#require-a-knowledge-source-to-succeed), set both `alwaysQuerySource` and `failOnError`. The first option ensures the source is selected, and the second returns a hard error if querying it fails. [MCP server knowledge sources (preview)](agentic-knowledge-source-how-to-mcp-server.md) don't support `alwaysQuerySource`; for those sources, `failOnError` applies only when the source is selected. `failOnError` doesn't apply to model activity failures.
 
 ### `502 Bad Gateway`
 
@@ -2819,7 +2811,7 @@ To avoid this behavior, index large source documents as smaller chunks with stab
 
 ## Call the MCP endpoint
 
-> [!IMPORTANT]
+> [!WARNING]
 > MCP implementations are susceptible to risks, such as attacks, cascading failures, and loss of human oversight. You can mitigate these risks by vetting MCP servers for security and reliability, following [Microsoft's recommended practices](/azure/api-management/secure-mcp-servers) and [industry best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices), and implementing approval mechanisms and monitoring cascading behaviors.
 
 [MCP](https://modelcontextprotocol.io/) is an open protocol that standardizes how AI applications connect to external data sources and tools.
@@ -3062,7 +3054,7 @@ Key points:
 ## Related content
 
 + [Agentic retrieval in Azure AI Search](agentic-retrieval-overview.md)
-+ [Query-time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md)
-+ [Use a blob indexer or knowledge source to ingest RBAC scopes metadata](search-blob-indexer-role-based-access.md)
++ [Query-time ACL and RBAC enforcement (preview)](search-query-access-control-rbac-enforcement.md)
++ [Use a blob indexer or knowledge source to ingest RBAC scopes metadata (preview)](search-blob-indexer-role-based-access.md)
 + [Agentic RAG: Build a reasoning retrieval engine with Azure AI Search (YouTube video)](https://www.youtube.com/watch?v=PeTmOidqHM8)
 + [Azure OpenAI demo featuring agentic retrieval](https://github.com/Azure-Samples/azure-search-openai-demo)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ベースのクエリに関する情報の追加と更新"
}
```

### Explanation
この変更は、知識ベースからデータを取得するための「retrieve」アクションやMCPエンドポイントを用いたクエリに関する情報を更新しています。主なポイントとして、アプリケーション開発者がクエリの動作を制御し、取得時の認可や応答処理を行うことで、アプリケーションやエージェントが基盤となるコンテンツを利用できるようにするためのガイダンスが強調されています。

新たにカスタマーインテントが追加され、開発者がAPIの具体的な利用方法を理解しやすくするための一次情報が提供されています。ドキュメント内の特定の重要情報の記述が削除され、全体的に文書の構成が見直されました。また、いくつかのリンクが「プレビュー」バージョンに更新され、最新の機能や注意事項が反映されています。

この改訂により、エージェント取得のプロセスや取得結果の処理についての理解が深まり、開発者がより効率的に機能を利用できることが期待されます。

## articles/search/agentic-retrieval-how-to-set-retrieval-reasoning-effort.md{#item-141e97}

<details>
<summary>Diff</summary>
````diff
@@ -10,22 +10,14 @@ ms.custom:
   - doc-kit-assisted
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
+#customer intent: As an application developer, I want to choose and configure a retrieval reasoning effort so that I can balance retrieval depth, relevance, latency, and LLM cost while meeting model and regional requirements.
 ---
 
 # Set the retrieval reasoning effort (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [Preview feature](./includes/previews/agentic-retrieval-preview-feature.md)]
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 In agentic retrieval, you can specify the level of large language model (LLM) processing for query planning and answer formulation. Use the *retrieval reasoning effort* (preview) to set LLM processing levels that affect costs and latency. Extra LLM processing improves relevance, but it also takes longer and uses billable LLM resources.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "取得推論努力の設定に関する情報の追加"
}
```

### Explanation
この変更は、取得推論努力を設定する方法に関するドキュメントを更新し、アプリケーション開発者がクエリの計画や回答の生成において大規模言語モデル（LLM）の処理レベルを選択および構成できることを強調しています。特に、開発者が取得の深さ、関連性、レイテンシ、およびLLMコストのバランスを取るための設定が可能であることが示されています。

新たにカスタマーインテントが追加され、開発者にとっての具体的なニーズである「取得推論努力」の選択が明示されています。また、文書内の重要情報が削除され、全体的に内容が簡潔になりました。このことにより、開発者が実装にあたって必要な情報を迅速に取得できるようになり、効果的なチャレンジを行う手助けとなることが期待されます。さらに、プレビュー機能に関する情報も更新され、最新の機能や条件が反映されています。

## articles/search/agentic-retrieval-overview.md{#item-d1f354}

<details>
<summary>Diff</summary>
````diff
@@ -1,35 +1,27 @@
 ---
 title: Agentic Retrieval Overview
 description: Learn about agentic retrieval in Azure AI Search, a pipeline that uses LLMs to decompose complex queries into subqueries for better RAG and agent workflows.
-ms.date: 06/02/2026
+ms.date: 09/16/2026
 ms.service: azure-ai-search
 ms.topic: concept-article
 ms.custom:
   - references_regions
   - build-2025
 ai-usage: ai-assisted
+#customer intent: As a solution architect, I want to evaluate how agentic retrieval works, its requirements, and its tradeoffs so that I can decide whether it fits my RAG or agent solution.
 ---
 
 # Agentic retrieval in Azure AI Search
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [GA announcement](./includes/previews/agentic-retrieval-ga-announcement.md)]
-
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 In Azure AI Search, *agentic retrieval* is a multi-query pipeline designed for complex questions posed by users or agents in chat and copilot apps. It's intended for [retrieval-augmented generation](retrieval-augmented-generation-overview.md) (RAG) patterns and agent-to-agent workflows.
 
 Here's what agentic retrieval does:
 
-+ Can use a large language model (LLM) to break down a complex query into smaller, focused subqueries for better coverage over proprietary and external content. Subqueries can include chat history for extra context.
++ Can use LLM-based query planning (preview) to break down a complex query into smaller, focused subqueries for better coverage across proprietary and external content. Query planning can use chat history for additional context.
 
 + Runs subqueries in parallel. Each subquery is semantically reranked to promote the most relevant matches.
 
@@ -81,23 +73,41 @@ For all agentic retrieval scenarios, a knowledge base and at least one knowledge
 | Knowledge source | Azure AI Search | Defines the content used in the pipeline. Can be indexed (backed by a search index on your service) or remote (content retrieved at query time from an external platform). |
 | Search index | Azure AI Search | Stores searchable content (text and vectors) with a semantic configuration. Determines which query types run and which optimizations apply. Required for indexed knowledge sources only. |
 | Semantic ranker | Azure AI Search | Used internally by the agentic retrieval pipeline to rerank results for relevance (L2 reranking). |
-| LLM | Azure OpenAI | Plans queries and selects knowledge sources. Used at `low` and `medium` retrieval reasoning effort only. Bypassed at `minimal` effort. |
+| LLM | Azure OpenAI | Can power multiple stages of agentic retrieval: planning queries and selecting knowledge sources (preview), summarizing web results, and generating citation-backed answers through answer synthesis (preview). |
 
 ### Integration requirements
 
 Your application drives the pipeline by calling the knowledge base and handling the response. The pipeline returns grounding data that you can pass to an LLM for answer generation or use directly in your conversation interface. For implementation details, see [Tutorial: Build an end-to-end agentic retrieval solution](agentic-retrieval-how-to-create-pipeline.md).
 
-## Availability and pricing
+## Feature availability
+
+Agentic retrieval supports both generally available and preview capabilities. Choose the Search Service REST API version that matches your agentic retrieval experience:
+
++ Use the `2026-04-01` REST API for production workloads that use generally available knowledge source types with minimal, extractive retrieval.
+
++ Use the `2026-08-01-preview` REST API for preview knowledge source types and capabilities such as LLM-based query planning, answer synthesis, non-minimal retrieval reasoning effort, and multi-turn messages. See [Azure AI Search preview terms](/azure/search/search-preview-terms).
+
+The Azure portal and Microsoft Foundry portal provide preview-only access to all agentic retrieval capabilities. Objects created in either portal might use preview schemas and require migration when you move to the generally available REST API version. For a version-by-version breakdown and migration guidance, see [Migrate agentic retrieval code to the latest version](agentic-retrieval-how-to-migrate.md).
+
+## Region availability, limits, and billing
+
+Before you use agentic retrieval, review its regional availability, service limits, and billing model.
+
+### Region availability
+
+Agentic retrieval is available in [select regions](search-region-support.md).
+
+### Limits
 
-Agentic retrieval is available in [select regions](search-region-support.md). Knowledge sources and knowledge bases also have [maximum limits](search-limits-quotas-capacity.md#agentic-retrieval-limits) that vary by pricing tier and retrieval reasoning effort.
+Knowledge sources and knowledge bases have [maximum limits](search-limits-quotas-capacity.md#agentic-retrieval-limits) that vary by pricing tier and retrieval reasoning effort.
 
 ### Billing
 
 Agentic retrieval incurs charges from two services:
 
 + **Azure AI Search** bills for retrieval tokens consumed during subquery execution and semantic ranking. The free plan (default) provides a monthly token allowance. The standard plan enables pay-as-you-go pricing after the free allowance is consumed. For more information, see [Enable or disable agentic retrieval billing](agentic-retrieval-how-to-enable-disable.md).
 
-+ **Azure OpenAI** bills for input and output tokens used in LLM-based query planning and [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md). Pricing is always pay-as-you-go and based on the model you assign to the knowledge base. Charges appear on your Azure OpenAI bill. For rates, see [Azure OpenAI pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing).
++ **Azure OpenAI** bills for input and output tokens used in LLM-based query planning and [answer synthesis (preview)](agentic-retrieval-how-to-answer-synthesis.md). Pricing is always pay-as-you-go and based on the model you assign to the knowledge base. Charges appear on your Azure OpenAI bill. For rates, see [Azure OpenAI pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing).
 
 The following table compares billing between the classic single-query pipeline and the agentic retrieval multi-query pipeline. In the classic pipeline, the billable component is [semantic ranker](semantic-search-overview.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント取得の概要に関する情報の更新"
}
```

### Explanation
この変更では、Azure AI Searchにおけるエージェント取得の概要情報が更新され、エージェント取得の動作やその利点、要件、トレードオフに関する情報が強調されています。特に、ソリューションアーキテクトがエージェント取得が自分のRAGやエージェントソリューションに適しているかを評価できるようにするための具体的なニーズが取り入れられています。

新たに追加された情報として、エージェント取得が複雑なクエリを小さなサブクエリに分解し、より良いカバレッジを提供するために大規模言語モデル（LLM）によるクエリの計画を利用することが示されています。サブクエリは並行して実行され、関連性に基づいてリランクされることが詳述されています。

また、エージェント取得の機能の可用性、新機能のプレビュー、地域別の利用制限や請求モデルに関する情報が整理されて追加されています。このことで、ユーザーはどのREST APIバージョンが自分のニーズに合っているかを理解しやすくなります。全体として、エージェント取得に関する情報が包括的に見直され、最新の機能やその利用方法がわかりやすく説明されています。

## articles/search/cognitive-search-aml-skill.md{#item-51366c}

<details>
<summary>Diff</summary>
````diff
@@ -16,10 +16,9 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> Support for indexer connections to the model catalog is in preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). Preview REST APIs support this capability.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-Use the **AML** skill to extend AI enrichment with a deployed base embedding model from the [Microsoft Foundry model catalog](vector-search-integrated-vectorization-ai-studio.md) or a custom [Azure Machine Learning](../machine-learning/overview-what-is-azure-machine-learning.md) (AML) model. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed.
+Use the **AML** skill to extend AI enrichment with a deployed base embedding model from the [Microsoft Foundry model catalog (preview)](vector-search-integrated-vectorization-ai-studio.md) or a custom [Azure Machine Learning](../machine-learning/overview-what-is-azure-machine-learning.md) (AML) model. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed.
 
 You specify the AML skill in a skillset, which then integrates your deployed model into an AI enrichment pipeline. The AML skill is useful for performing processing or inference not supported by built-in skills. Examples include generating embeddings with your own model and applying custom machine learning logic to enriched content.
 
@@ -34,9 +33,9 @@ The indexer retries two times for the following HTTP status codes:
 - `503 Service Unavailable`
 - `429 Too Many Requests`
 
-## AML skill for models in Microsoft Foundry
+## AML skill for models in Microsoft Foundry (preview)
 
-Azure AI Search provides the [Microsoft Foundry model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md), which is also available in the [**Import data** wizard](search-import-data-portal.md#skills), for query-time connections to the model catalog. If you want to use this vectorizer for queries, the AML skill is the *indexing counterpart* for generating embeddings using a model from the model catalog.
+Azure AI Search provides the [Microsoft Foundry model catalog vectorizer (preview)](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md), which is also available in the [**Import data** wizard](search-import-data-portal.md#skills), for query-time connections to the model catalog. If you want to use this vectorizer for queries, the AML skill is the *indexing counterpart* for generating embeddings using a model from the model catalog.
 
 During indexing, the AML skill can connect to the model catalog to generate vectors for the index. At query time, queries can use a vectorizer to connect to the same model to vectorize text strings. You should use the AML skill and the Microsoft Foundry model catalog vectorizer together so that the same embedding model is used for indexing and queries. For more information, see [Use embedding models from the Foundry model catalog](vector-search-integrated-vectorization-ai-studio.md).
 
@@ -182,5 +181,5 @@ If the model provider is unavailable or returns an HTTP error, a friendly error
 ## Related content
 
 - [Create a skillset in Azure AI Search](cognitive-search-defining-skillset.md)
-- [Use embedding models from the Microsoft Foundry model catalog for integrated vectorization](vector-search-integrated-vectorization-ai-studio.md)
+- [Use embedding models from the Microsoft Foundry model catalog for integrated vectorization (preview)](vector-search-integrated-vectorization-ai-studio.md)
 - [Troubleshoot online endpoint deployment and scoring](../machine-learning/how-to-troubleshoot-online-endpoints.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AMLスキルに関するプレビュー情報の追加"
}
```

### Explanation
この変更は、Azure AI SearchにおけるAMLスキルに関するドキュメントを更新し、Microsoft Foundryモデルカタログに関するプレビュー情報が強調されています。特に、AMLスキルを使用することで、デプロイされた基本的な埋め込みモデルやカスタムAzure Machine Learning（AML）モデルを活用してAIの強化を拡張できることが説明されています。

重要な変更点として、Microsoft Foundryモデルカタログのベクタイザがプレビューとして提供されていることが強調され、これによりユーザーがクエリ時にモデルカタログに接続できることが示されています。また、モデルカタログとの接続が可能であることは、インデックス作成時に同じ埋め込みモデルを使用するために重要であると説明されており、これにより一貫したベクトル生成が可能になります。

さらに、関連するスキルセットの作成方法や、埋め込みモデルを使用した統合ベクトル化に関する情報も更新されています。全体として、AMLスキルに関する情報が明確になり、ユーザーが機能を利用するための理解を深めるのに役立つ内容になっています。

## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -9,6 +9,7 @@ ms.custom:
   - ignite-2023
   - ignite-2024
   - sfi-image-nochange
+ai-usage: ai-assisted
 ---
 
 # Attach a billable resource to a skillset in Azure AI Search
@@ -314,14 +315,14 @@ Billable built-in skills that make backend calls to external services include:
 + [Personally Identifiable Information (PII) Detection](cognitive-search-skill-pii-detection.md)
 + [Sentiment](cognitive-search-skill-sentiment-v3.md)
 + [Text Translation](cognitive-search-skill-text-translation.md)
-+ [Azure Vision multimodal embeddings](cognitive-search-skill-vision-vectorize.md)
++ [Azure Vision multimodal embeddings (preview)](cognitive-search-skill-vision-vectorize.md)
 
 A [query-time vectorizer](vector-search-how-to-configure-vectorizer.md) backed by the Azure Vision multimodal embedding model is also a billable enrichment.
 
 Image extraction is an Azure AI Search operation that occurs when documents are cracked prior to enrichment. Image extraction is billable on all pricing tiers, except for 20 free daily extractions on the free tier. Image extraction costs apply to image files inside blobs, embedded images in other files (PDF and other app files), and images extracted using [Document Extraction](cognitive-search-skill-document-extraction.md). For image extraction pricing, see the [Azure AI Search pricing page](https://azure.microsoft.com/pricing/details/search/).
 
 > [!TIP]
-> To lower the cost of skillset processing, enable [incremental enrichment](enrichment-cache-how-to-configure.md) to cache and reuse any enrichments that are unaffected by changes made to a skillset. Caching requires Azure Storage (see [pricing](https://azure.microsoft.com/pricing/details/storage/blobs/)), but the cumulative cost of skillset execution is lower if existing enrichments can be reused, especially for skillsets that use image extraction and analysis.
+> To lower the cost of skillset processing, enable [incremental enrichment (preview)](enrichment-cache-how-to-configure.md) to cache and reuse any enrichments that are unaffected by changes made to a skillset. Caching requires Azure Storage (see [pricing](https://azure.microsoft.com/pricing/details/storage/blobs/)), but the cumulative cost of skillset execution is lower if existing enrichments can be reused, especially for skillsets that use image extraction and analysis.
 
 ## Example: Estimate costs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI支援機能の追加とプレビュー情報の強調"
}
```

### Explanation
この変更は、Azure AI Searchにおけるスキルセットに請求可能なリソースを関連付けるためのドキュメントを更新し、AI支援の機能に関する新しい情報を追加しています。また、いくつかの機能がプレビューとして強調されています。

特に、スキルとして利用可能な「Azure Visionマルチモーダル埋め込み」がプレビュー表示されるようになりました。これにより、ユーザーはこの新機能を利用した場合の請求方式についても知識を深めることが可能です。

さらに、インクリメンタルエンリッチメントの有効化が提案されており、これがプレビュー機能としても言及されていることから、コスト削減のオプションが利用可能であることが強調されています。ユーザーは、スキルセットに対して行われた変更から影響を受けないエンリッチメントをキャッシュし再利用することで、総コストを下げることができます。

全体として、この更新により、Azure AI Searchの機能をより効果的に利用するための情報が提供されており、ユーザーにとって便利な最新情報が盛り込まれています。

## articles/search/cognitive-search-concept-intro.md{#item-bf9ed7}

<details>
<summary>Diff</summary>
````diff
@@ -44,7 +44,7 @@ The following diagram shows the progression of AI enrichment:
 
 - Enrichment starts when the indexer *[cracks documents](search-indexer-overview.md#document-cracking)* and extracts images and text. The type of processing that occurs next depends on your data and the skills you've added to a skillset. Images can be forwarded to [skills that perform image processing](cognitive-search-concept-image-scenarios.md). Text content is queued for text and natural language processing. Internally, skills create an *[enriched document](cognitive-search-working-with-skillsets.md#enrichment-tree)* that collects transformations as they occur.
 
-- Enriched content is generated during skillset execution and is temporary unless you save it. You can enable an [enrichment cache](enrichment-cache-how-to-configure.md) to persist skill outputs for reuse in future skillset executions.
+- Enriched content is generated during skillset execution and is temporary unless you save it. You can enable an [enrichment cache (preview)](enrichment-cache-how-to-configure.md) to persist skill outputs for reuse in future skillset executions.
 
 - To get content into a search index, the indexer must have mapping information for sending enriched content to target field. [Field mappings](search-indexer-field-mappings.md) (explicit or implicit) set the data path from source data to a search index. [Output field mappings](cognitive-search-output-field-mapping.md) set the data path from enriched documents to an index.
 
@@ -82,9 +82,9 @@ In Azure AI Search, an indexer saves the output it creates. A single indexer run
 
 | Data store | Required | Location | Description |
 | --- | --- | --- | --- |
-| [searchable index](search-what-is-an-index.md) | Required | Search service | Used for full-text search and other query forms. Specifying an index is an indexer requirement. Index content is populated from skill outputs, plus any source fields that are mapped directly to fields in the index. |
-| [knowledge store](knowledge-store-concept-intro.md) | Optional | Azure Storage | Used for downstream apps like knowledge mining, data science, and multimodal search. A knowledge store is defined within a skillset. Its definition determines whether your enriched documents are projected as tables or objects (files or blobs) in Azure Storage. For [multimodal search scenarios](multimodal-search-overview.md#how-does-multimodal-search-work), you can save extracted images to the knowledge store and reference them at query time, allowing the images to be returned directly to client apps. |
-| [enrichment cache](enrichment-cache-how-to-configure.md) | Optional | Azure Storage | Used for caching enrichments for reuse in subsequent skillset executions. The cache stores imported, unprocessed content (cracked documents). It also stores the enriched documents created during skillset execution. Caching is helpful if you're using image analysis or OCR, and you want to avoid the time and expense of reprocessing image files. |
+| [Searchable index](search-what-is-an-index.md) | Required | Search service | Used for full-text search and other query forms. Specifying an index is an indexer requirement. Index content is populated from skill outputs, plus any source fields that are mapped directly to fields in the index. |
+| [Knowledge store](knowledge-store-concept-intro.md) | Optional | Azure Storage | Used for downstream apps like knowledge mining, data science, and multimodal search. A knowledge store is defined within a skillset. Its definition determines whether your enriched documents are projected as tables or objects (files or blobs) in Azure Storage. For [multimodal search scenarios](multimodal-search-overview.md#how-does-multimodal-search-work), you can save extracted images to the knowledge store and reference them at query time, allowing the images to be returned directly to client apps. |
+| [Enrichment cache (preview)](enrichment-cache-how-to-configure.md) | Optional | Azure Storage | Used for caching enrichments for reuse in subsequent skillset executions. The cache stores imported, unprocessed content (cracked documents). It also stores the enriched documents created during skillset execution. Caching is helpful if you're using image analysis or OCR, and you want to avoid the time and expense of reprocessing image files. |
 
 Indexes and knowledge stores are fully independent of each other. While you must attach an index to satisfy indexer requirements, if your sole objective is a knowledge store, you can ignore the index after it's populated.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インクリメンタルエンリッチメントのプレビュー情報の追加"
}
```

### Explanation
この変更は、Azure AI Searchの概念に関するドキュメントを更新し、インクリメンタルエンリッチメントに関する新しいプレビュー情報を追加しています。具体的には、エンリッチメントキャッシュの機能がプレビューとして強調され、将来のスキルセット実行のためにスキルの出力を保持する方法が紹介されています。

文章の一部では、エンリッチメントがスキルセットの実行中に生成され、一時的なものであることが説明され、キャッシュを有効にすることで、このエンリッチメントを持続的に活用できることが述べられています。これにより、将来的にスキル出力を再利用する際の効率が向上します。

また、検索可能なインデックスやナレッジストア、エンリッチメントキャッシュに関するテーブルが更新され、それぞれの機能と配置場所についての詳細が整理されています。特に、エンリッチメントキャッシュがどのようにして再処理の時間とコストを削減できるかについても言及されています。

この変更によって、ユーザーはAzure AI Searchの利用方法について最新の情報を得ることができ、効率的なデータ処理のためのツールをより理解できるようになります。

## articles/search/cognitive-search-defining-skillset.md{#item-e2d71d}

<details>
<summary>Diff</summary>
````diff
@@ -8,6 +8,7 @@ ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
   - sfi-ropc-nochange
+ai-usage: ai-assisted
 ---
 
 # Create a skillset in Azure AI Search
@@ -30,7 +31,7 @@ Rules for skillset definition include:
 Attach a skillset to an indexer. To use the skillset, reference it in an [indexer](search-howto-create-indexers.md) and then run the indexer to import data, invoke skills processing, and send output to an [index](search-what-is-an-index.md). A skillset is a high-level resource, but it's operational only within indexer processing. As a high-level resource, you can reference it in multiple indexers.
 
 > [!TIP]
-> Enable [enrichment caching](enrichment-cache-how-to-configure.md) to reuse the content you already processed and lower the cost of development.
+> Enable [enrichment caching (preview)](enrichment-cache-how-to-configure.md) to reuse the content you already processed and lower the cost of development.
 
 ## Add a skillset definition
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI支援機能とプレビュー情報の追加"
}
```

### Explanation
この変更は、Azure AI Searchにおけるスキルセット定義に関するドキュメントを更新し、AI支援機能に関する情報を追加しています。また、エンリッチメントキャッシングの機能がプレビューとして明記されています。

具体的には、スキルセットのメタデータに「ai-usage: ai-assisted」という新しい項目が追加され、これはAI技術の活用に関連することを示しています。さらに、エンリッチメントキャッシングを有効にすることで、すでに処理済みのコンテンツを再利用できる点が強調され、開発コストを削減するための手法が紹介されています。

これにより、ユーザーはより効率的にスキルセットを管理し、使用するための新たな情報を得ることができます。また、プレビュー機能としてのエンリッチメントキャッシングの重要性が示され、ユーザーは将来的な機能向上の可能性に備えることができます。全体として、この変更はAzure AI Searchの利用方法を改善するための有益な情報を提供しています。

## articles/search/cognitive-search-predefined-skills.md{#item-81d522}

<details>
<summary>Diff</summary>
````diff
@@ -9,6 +9,7 @@ ms.custom:
 ms.topic: reference
 ms.date: 06/25/2026
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Skills for extra processing during indexing (Azure AI Search)
@@ -44,7 +45,7 @@ These skills are billed at the Standard rate.
 
 | Skill  | Description | Metered by |
 |-------|-------------|-------------|
-| [Azure Vision multimodal embeddings](cognitive-search-skill-vision-vectorize.md) | Multimodal image and text vectorization. | Foundry Tools ([pricing](https://azure.microsoft.com/pricing/details/cognitive-services/)) |
+| [Azure Vision multimodal embeddings (preview)](cognitive-search-skill-vision-vectorize.md) | Multimodal image and text vectorization. | Foundry Tools ([pricing](https://azure.microsoft.com/pricing/details/cognitive-services/)) |
 | [Custom Entity Lookup](cognitive-search-skill-custom-entity-lookup.md) | Looks for text from a custom, user-defined list of words and phrases.| Azure AI Search ([pricing](https://azure.microsoft.com/pricing/details/search/)) |
 | [Entity Linking](cognitive-search-skill-entity-linking-v3.md) | This skill uses a pretrained model to generate links for recognized entities to articles in Wikipedia. | Foundry Tools ([pricing](https://azure.microsoft.com/pricing/details/cognitive-services/)) |
 | [Entity Recognition](cognitive-search-skill-entity-recognition-v3.md) | This skill uses a pretrained model to establish entities for a fixed set of categories: `"Person"`, `"Location"`, `"Organization"`, `"Quantity"`, `"DateTime"`, `"URL"`, `"Email"`, `"PersonType"`, `"Event"`, `"Product"`, `"Skill"`, `"Address"`, `"Phone Number"` and `"IP Address"` fields. | Foundry Tools ([pricing](https://azure.microsoft.com/pricing/details/cognitive-services/)) |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI支援機能の追加とプレビュー情報の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける事前定義されたスキルに関するドキュメントを更新し、AI支援機能に関する情報を追加しています。具体的には、メタデータに「ai-usage: ai-assisted」という項目が新たに追加され、AIを利用したプロセスのサポートを示しています。

さらに、特に「Azure Vision multimodal embeddings」スキルの項目において、プレビューとしての情報が強調されるように改訂されています。これにより、ユーザーはこのスキルが現在プレビュー段階であることを認識し、利用を検討する際の判断材料とすることができます。

全体として、この変更はAzure AI Searchの機能をより明確にし、ユーザーが最新の情報に基づいてスキルを利用できるようにすることを目的としています。プレビューの明示は、利用者に対して新たな可能性を提供する一方で、その現段階における状況を理解させる役割も果たします。

## articles/search/cognitive-search-skill-content-understanding.md{#item-c7787e}

<details>
<summary>Diff</summary>
````diff
@@ -18,8 +18,7 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> Features, capabilities, or properties marked (preview) aren't covered by a service-level agreement, aren't recommended for production workloads, and might change or be constrained before they become generally available. If you choose to use preview functionality, whether it's standalone or part of a generally available feature, you're responsible for data handling, data access, responsible AI use, and other obligations described in the [Azure AI Search preview terms](search-preview-terms.md).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 The **Azure Content Understanding** skill uses [document analyzers](/azure/ai-services/content-understanding/document/overview) from [Azure Content Understanding in Foundry Tools](/azure/ai-services/content-understanding/overview) to analyze unstructured documents and other content types, generating organized, searchable outputs that can be integrated into automation workloads. This skill extracts both text and images, including location metadata that preserves each image's position within the document. Image proximity to related content is especially useful for [multimodal search](multimodal-search-overview.md), [agentic retrieval](agentic-retrieval-overview.md), and [retrieval-augmented generation](retrieval-augmented-generation-overview.md) (RAG).
 
@@ -37,7 +36,7 @@ You can use the Azure Content Understanding skill for both content extraction an
 
 + Azure Content Understanding can generate AI-based descriptions for images, charts, diagrams, and embedded figures. Embedded figure descriptions are incorporated directly into markdown content generated for retrieval. These descriptions are searchable and can improve RAG grounding and multimodal retrieval quality. 
 
-The Azure Content Understanding skill is generally available in the [`2026-04-01` REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true). Starting with the [`2026-05-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true), the skill optionally generates AI-based descriptions for document-embedded images, charts, and diagrams. To enable descriptions, you must deploy an Azure OpenAI chat completion model in the Foundry resource attached to the skillset. This API version also adds *semantic* chunking (preview), a layout-aware option that respects paragraph boundaries and measures chunk length in tokens. Both capabilities require opt-in. When the new parameters are omitted, the skill behaves the same as in the stable `2026-04-01` API version.
+The Azure Content Understanding skill is generally available in the [`2026-04-01` REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-04-01&preserve-view=true). Starting with the [`2026-05-01-preview`](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true), the skill optionally generates AI-based image descriptions for document-embedded images, charts, and diagrams (preview). To enable descriptions, you must deploy an Azure OpenAI chat completion model in the Foundry resource attached to the skillset. This API version also adds semantic chunking (preview), a layout-aware option that respects paragraph boundaries and measures chunk length in tokens. Both capabilities require opt-in. When the new parameters are omitted, the skill behaves the same as in the stable `2026-04-01` API version.
 
 ## Limitations
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビュー機能の条件に関する更新"
}
```

### Explanation
この変更は、Azureのコンテンツ理解スキルに関するドキュメントを改訂し、プレビュー機能に関連する重要な情報を整理・強調することを目的としています。具体的には、プレビュー機能の使用に関して新たなインクルードファイルとガイダンスを追加しました。

修正後の内容では、プレビュー機能がサービス契約の対象外であることや、プロダクション環境での使用が推奨されないことを明示する代わりに、プレビューに関する条件が別ファイルに整理されました。これにより、ユーザーはプレビュー機能を利用する際に遵守すべき条項を、より明確に確認できるようになっています。

加えて、Azureコンテンツ理解スキルが文書内に埋め込まれた画像やチャート、図のAIベースの説明を生成する機能が強調されており、これにより検索の質が向上することが期待されます。また、セマンティックチャンク処理（プレビュー機能）についても言及されており、視覚的に文書の構造を尊重するオプションとしての重要性が示されています。

全体として、この変更はユーザーに対して新しい機能とプレビューの条件を明確にし、従来のドキュメントの理解を深めるための重要な情報を提供します。

## articles/search/cognitive-search-skill-textsplit.md{#item-9bf753}

<details>
<summary>Diff</summary>
````diff
@@ -8,49 +8,46 @@ ms.custom:
 ms.topic: reference
 ms.date: 01/07/2026
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Text Split skill
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT] 
-> Some parameters are in preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [preview REST API](/rest/api/searchservice/index-preview) supports these parameters.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 The **Text Split** skill breaks text into chunks of text. You can specify whether you want to break the text into sentences or into pages of a particular length. Positional metadata like offset and ordinal position are also available as outputs. This skill is useful if there are maximum text length requirements in other skills downstream, such as embedding skills that pass data chunks to embedding models on Azure OpenAI and other model providers. For more information about this scenario, see [Chunk documents for vector search](vector-search-how-to-chunk-documents.md).
 
-Several parameters are version-specific. The skills parameter table notes the API version in which a parameter was introduced so that you know whether a [version upgrade](search-api-migration.md) is required. To use version-specific features such as *token chunking* in **2024-09-01-preview**, you can use the Azure portal, or target a REST API version, or check an Azure SDK change log to see if it supports the feature.
-
-The Azure portal supports most preview features and can be used to create or update a skillset. For updates to the Text Split skill, edit the skillset JSON definition to add new preview parameters. 
-
 > [!NOTE]
 > This skill isn't bound to Foundry Tools. It's non-billable and has no Foundry Tools key requirement.
 
-## @odata.type  
+## @odata.type
+  
 Microsoft.Skills.Text.SplitSkill 
 
-## Skill Parameters
+## Skill parameters
 
 Parameters are case sensitive. 
 
-| Parameter name     | Description |
-|--------------------|-------------|-------------|
-| `textSplitMode`    | Either `pages` or `sentences`. Pages have a configurable maximum length, but the skill attempts to avoid truncating a sentence so the actual length might be smaller. Sentences are a string that terminates at sentence-ending punctuation, such as a period, question mark, or exclamation point, assuming the language has sentence-ending punctuation. | 
+| Parameter name | Description |
+| --- | --- |
+| `textSplitMode` | Either `pages` or `sentences`. Pages have a configurable maximum length, but the skill attempts to avoid truncating a sentence so the actual length might be smaller. Sentences are a string that terminates at sentence-ending punctuation, such as a period, question mark, or exclamation point, assuming the language has sentence-ending punctuation. |
 | `maximumPageLength` | Only applies if `textSplitMode` is set to `pages`. For `unit` set to `characters`, this parameter refers to the maximum page length in characters as measured by `String.Length`. The minimum value is 300, the maximum is 50000, and the default value is 5000.  The algorithm does its best to break the text on sentence boundaries, so the size of each chunk might be slightly less than `maximumPageLength`. <br><br>For `unit` set to `azureOpenAITokens`, the maximum page length is the token length limit of the model. For text embedding models, a general recommendation for page length is 512 tokens. |
-| `defaultLanguageCode`	| (optional) One of the following language codes: `am, bs, cs, da, de, en, es, et, fr, he, hi, hr, hu, fi, id, is, it, ja, ko, lv, no, nl, pl, pt-PT, pt-BR, ru, sk, sl, sr, sv, tr, ur, zh-Hans`. Default is English (en). A few things to consider: <ul><li>Providing a language code is useful to avoid cutting a word in half for nonwhitespace languages such as Chinese, Japanese, and Korean.</li><li>If you don't know the language  in advance (for example, if you're using the [LanguageDetectionSkill](cognitive-search-skill-language-detection.md) to detect language), we recommend the `en` default. </li></ul>  |
+| `defaultLanguageCode` | (optional) One of the following language codes: `am, bs, cs, da, de, en, es, et, fr, he, hi, hr, hu, fi, id, is, it, ja, ko, lv, no, nl, pl, pt-PT, pt-BR, ru, sk, sl, sr, sv, tr, ur, zh-Hans`. Default is English (en). A few things to consider: <ul><li>Providing a language code is useful to avoid cutting a word in half for nonwhitespace languages such as Chinese, Japanese, and Korean.</li><li>If you don't know the language  in advance (for example, if you're using the [LanguageDetectionSkill](cognitive-search-skill-language-detection.md) to detect language), we recommend the `en` default. </li></ul> |
 | `pageOverlapLength` | Only applies if `textSplitMode` is set to `pages`. Each page starts with this number of characters or tokens from the end of the previous page. If this parameter is set to 0, there's no overlapping text on successive pages. This [example](#example-for-chunking-and-vectorization) includes the parameter. |
-| `maximumPagesToTake` | Only applies if `textSplitMode` is set to `pages`. Number of pages to return. The default is 0, which means to return all pages. You should set this value if only a subset of pages are needed. This [example](#example-for-chunking-and-vectorization) includes the parameter.|
-| `unit` | Only applies if `textSplitMode` is set to `pages`. Specifies whether to chunk by `characters` (default) or `azureOpenAITokens`. Setting the unit affects `maximumPageLength` and `pageOverlapLength`. |
-| `azureOpenAITokenizerParameters` An object providing extra parameters for the `azureOpenAITokens` unit. <br><br>`encoderModelName` is a designated tokenizer used for converting text into tokens, essential for natural language processing (NLP) tasks. Different models use different tokenizers. Valid values include cl100k_base (default) used by GPT-4. Other valid values are r50k_base, p50k_base, and p50k_edit. The skill implements the tiktoken library by way of [SharpToken](https://www.nuget.org/packages/SharpToken) and `Microsoft.ML.Tokenizers` but doesn't support every encoder. For example, there's currently no support for o200k_base encoding used by GPT-4o. <br><br>`allowedSpecialTokens` defines a collection of special tokens that are permitted within the tokenization process. Special tokens are  string that you want to treat uniquely, ensuring they aren't split during tokenization. For example ["[START"], "[END]"]. If the `tiktoken` library doesn't perform tokenization as expected, either due to language-specific limitations or other unexpected behaviors, it's recommended to use text splitting instead.|
+| `maximumPagesToTake` | Only applies if `textSplitMode` is set to `pages`. Number of pages to return. The default is 0, which means to return all pages. You should set this value if only a subset of pages are needed. This [example](#example-for-chunking-and-vectorization) includes the parameter. |
+| `unit` (preview) | Only applies if `textSplitMode` is set to `pages`. Specifies whether to chunk by `characters` (default) or `azureOpenAITokens`. Setting the unit affects `maximumPageLength` and `pageOverlapLength`. |
+| `azureOpenAITokenizerParameters` (preview) | An object providing extra parameters for the `azureOpenAITokens` unit. <br><br>`encoderModelName` is a designated tokenizer used for converting text into tokens, essential for natural language processing (NLP) tasks. Different models use different tokenizers. Valid values include cl100k_base (default) used by GPT-4. Other valid values are r50k_base, p50k_base, and p50k_edit. The skill implements the tiktoken library by way of [SharpToken](https://www.nuget.org/packages/SharpToken) and `Microsoft.ML.Tokenizers` but doesn't support every encoder. For example, there's currently no support for o200k_base encoding used by GPT-4o. <br><br>`allowedSpecialTokens` defines a collection of special tokens that are permitted within the tokenization process. Special tokens are  string that you want to treat uniquely, ensuring they aren't split during tokenization. For example, ["[START"], "[END]"]. If the `tiktoken` library doesn't perform tokenization as expected, either due to language-specific limitations or other unexpected behaviors, it's recommended to use text splitting instead. |
 
-## Skill Inputs
+## Skill inputs
 
 | Parameter name	   | Description      |
 |----------------------|------------------|
 | `text` | The text to split into substring. |
 | `languageCode` | (Optional) Language code for the document. If you don't know the language of the text inputs (for example, if you're using [LanguageDetectionSkill](cognitive-search-skill-language-detection.md) to detect the language), you can omit this parameter. If you set `languageCode` to a language isn't in the supported list for the `defaultLanguageCode`, a warning is emitted and the text isn't split.  |
 
-## Skill Outputs 
+## Skill outputs
 
 | Parameter name	 | Description |
 |--------------------|-------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト分割スキルのパラメータの更新と整理"
}
```

### Explanation
この変更は、Azureのテキスト分割スキルに関するドキュメントを更新し、パラメータに関する情報を整理しています。具体的には、プレビュー機能に関連する条件を明示するためのインクルードファイルの追加や、テキスト分割のための入力と出力パラメータの説明が強化されています。

更新された内容では、特にテキスト分割に関連するいくつかの新しいパラメータが詳しく説明されています。これには、ページの最大長や言語コード、ページのオーバーラップ長、トークン化に関するパラメータが含まれます。また、一部のパラメータはプレビューバージョンに限定されており、これらの仕様に関する注意喚起も行われています。

加えて、テキスト分割スキルがどのようにテキストをチャンクに分けるのか、その処理の目的と関連機能についての説明が明確化されており、特に後続のスキルでのテキスト最大長要件を考慮した利用方法が提示されています。

全体として、この変更はユーザーに対して新たな機能と詳細なパラメータ情報を提供し、テキスト分割スキルの利用をより効果的にサポートすることを目的としています。また、細かい変更によりドキュメントの可読性が向上し、利用者が必要な情報をより簡単に見つけられるようになっています。

## articles/search/cognitive-search-skill-vision-vectorize.md{#item-386571}

<details>
<summary>Diff</summary>
````diff
@@ -8,16 +8,16 @@ ms.custom:
   - references_regions
 ms.topic: reference
 ms.date: 01/16/2026
+ai-usage: ai-assisted
 ---
 
-# Azure Vision multimodal embeddings skill
+# Azure Vision multimodal embeddings skill (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> This skill is in preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The latest preview version of [Skillsets - Create Or Update](/rest/api/searchservice/skillsets/create-or-update) (REST API) supports this feature.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-The **Azure Vision multimodal embeddings** skill uses the [multimodal embeddings API](/azure/ai-services/computer-vision/concept-image-retrieval) from Azure Vision in Foundry Tools to generate embeddings for text or image input.
+The **Azure Vision multimodal embeddings** skill (preview) uses the [multimodal embeddings API](/azure/ai-services/computer-vision/concept-image-retrieval) from Azure Vision in Foundry Tools to generate embeddings for text or image input.
 
 For transactions that exceed 20 documents per indexer per day, this skill requires you to [attach a billable Microsoft Foundry resource](cognitive-search-attach-cognitive-services.md) to your skillset. Execution of built-in skills is charged at the existing [Foundry Tools Standard price](https://azure.microsoft.com/pricing/details/cognitive-services/). Image extraction is also [billable by Azure AI Search](https://azure.microsoft.com/pricing/details/search/).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Visionマルチモーダル埋め込みスキルのプレビュー記載の追加"
}
```

### Explanation
この変更は、Azure Visionによるマルチモーダル埋め込みスキルに関するドキュメントを更新し、プレビュー状態の明示化と重要な情報の整理を行っています。特に、スキルの名称に「(preview)」という記載が追加され、これは使用者にこの機能が現在プレビュー版であることを周知する意図があります。

さらに、プレビュー機能に関連したインクルードファイルの追加により、ユーザーがプレビュー利用時に従うべき条件をより明確に理解できるようになりました。これにより、利用者は最新のプレビューバージョンに関する情報を参照することが容易になり、スキルセットの作成・更新に必要なリソースと料金に関する情報も整理されています。

この修正は、特にドキュメントの可読性を向上させることを目的しており、Azure Visionマルチモーダル埋め込みスキルの利用者が必要な情報を迅速に取得できるよう配慮されています。全体として、変更は利用者に最新の機能状況と料金情報を確実に伝えるために役立ちます。

## articles/search/cognitive-search-tutorial-debug-sessions.md{#item-7e10e9}

<details>
<summary>Diff</summary>
````diff
@@ -271,4 +271,4 @@ This tutorial touched on various aspects of skillset definition and processing.
 
 + [Skillsets in Azure AI Search](cognitive-search-working-with-skillsets.md)
 
-+ [How to configure caching for incremental enrichment](enrichment-cache-how-to-configure.md)
++ [How to configure caching for incremental enrichment (preview)](enrichment-cache-how-to-configure.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "キャッシュ設定のプレビュー状態の明示化"
}
```

### Explanation
この変更は、Azure Cognitive Searchに関するデバッグセッションのチュートリアルドキュメントを更新し、キャッシュ設定に関する情報を明確に示すための修正です。具体的には、「キャッシュ設定の構成に関する方法」というリンクのタイトルに「(preview)」という表記が追加されました。

この追加により、ユーザーはそのリンク先がプレビュー版の情報であることを認識し、現在のサポート状況や使用上の注意点を理解する手助けになります。また、より効果的に新機能を試す際の注意喚起となります。

全体として、この変更はドキュメントの整合性を保ちつつ、利用者がプレビュー機能に関する正確な情報を得られるよう配慮しており、Azure Cognitive Searchの機能利用をサポートする目的があります。

## articles/search/cognitive-search-working-with-skillsets.md{#item-6091d1}

<details>
<summary>Diff</summary>
````diff
@@ -127,7 +127,7 @@ Notice how the output of the first skill ("pages") is used in sentiment analysis
 
 An enriched document is a temporary, tree-like data structure created during skillset execution that collects all of the changes introduced through skills. Collectively, enrichments are represented as a hierarchy of addressable nodes. Nodes also include any unenriched fields that are passed in verbatim from the external data source. The best approach for examining the structure and content of an enrichment tree is through a [debug session](cognitive-search-debug-session.md) in the Azure portal.
 
-An enriched document exists for the duration of skillset execution, but can be [cached](enrichment-cache-how-to-configure.md) or sent to a [knowledge store](knowledge-store-concept-intro.md). 
+An enriched document exists for the duration of skillset execution, but can be [cached (preview)](enrichment-cache-how-to-configure.md) or sent to a [knowledge store](knowledge-store-concept-intro.md). 
 
 Initially, an enriched document is simply the content extracted from a data source during [*document cracking*](search-indexer-overview.md#document-cracking), where text and images are extracted from the source and made available for language or image analysis. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "キャッシュ機能のプレビュー状態の表記追加"
}
```

### Explanation
この変更は、Azure Cognitive Searchにおけるスキルセットの操作に関するドキュメントを更新し、エンリッチメントドキュメントのキャッシュ機能に関連する情報をより明確にすることを目的としています。具体的には、エンリッチメントドキュメントがスキルセット実行中に存在し得ることに関する説明に、「キャッシュする」機能のリンクに「(preview)」という表記が追加されました。

これにより、ユーザーはそのキャッシュ機能が現在プレビュー版であることを認識し、使用に際しての注意点や最新の機能状況を把握しやすくなります。プレビュー機能には制限や特別な条件がある場合が多いため、この明示化は利用者にとって重要です。

全体として、この変更はドキュメントの正確性を向上させるとともに、ユーザーが利用可能な新機能について正しい情報を得られるように支援することを意図しています。

## articles/search/enrichment-cache-how-to-configure.md{#item-b0ae0b}

<details>
<summary>Diff</summary>
````diff
@@ -8,16 +8,16 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
   - sfi-ropc-nochange
+ai-usage: ai-assisted
 ---
 
-# Configure an enrichment cache
+# Configure an enrichment cache (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT] 
-> This feature is in preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). [Preview REST APIs](/rest/api/searchservice/index-preview) support this feature.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-This article explains how to add caching to a skillset pipeline so that you can modify downstream enrichment steps without a full rebuild every time. By default, a skillset is stateless, and changing any part of its composition requires a full rerun of the indexer. With an *enrichment cache*, the indexer determines which parts of the document tree must be refreshed based on skillset or indexer definition changes. The indexer preserves and reuses existing processed output where possible.
+This article explains how to add caching to a skillset pipeline so that you can modify downstream enrichment steps without a full rebuild every time. Enrichment caching (preview) requires a [preview REST API](/rest/api/searchservice/index-preview). By default, a skillset is stateless, and changing any part of its composition requires a full rerun of the indexer. With an *enrichment cache*, the indexer determines which parts of the document tree must be refreshed based on skillset or indexer definition changes. The indexer preserves and reuses existing processed output where possible.
 
 You place cached content in Azure Storage by using a connection string that you provide. The indexer creates these objects when it runs. Consider the enrichment cache an internal component managed by your search service that you must not modify.
 
@@ -38,7 +38,7 @@ You should be familiar with setting up indexers and skillsets. Start with [index
 ## Limitations
 
 > [!CAUTION]
-> If you're using the [SharePoint indexer (Preview)](search-how-to-index-sharepoint-online.md), avoid incremental enrichment. Under certain circumstances, the cache becomes invalid. To reload it, perform an [indexer reset and full rebuild](search-howto-run-reset-indexers.md).
+> If you're using the [SharePoint indexer (preview)](search-how-to-index-sharepoint-online.md), avoid incremental enrichment. Under certain circumstances, the cache becomes invalid. To reload it, perform an [indexer reset and full rebuild](search-howto-run-reset-indexers.md).
 
 Large data sources have an additional cache limitation.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンリッチメントキャッシュ機能のプレビュー状態の表記追加"
}
```

### Explanation
この変更は、Azureのエンリッチメントキャッシュの設定に関するドキュメントを更新し、機能がプレビュー状態であることをより明確にするための修正です。具体的には、記事タイトルに「(preview)」が追加され、重要な警告がプレビューに関連する情報を含むように修正されています。

この変更により、ユーザーはエンリッチメントキャッシュ機能が現在プレビュー段階であることを理解し、その利用にあたっての特別な注意が必要であることを認識できるようになります。また、プレビュー機能を利用するためには、特定のREST APIを使用する必要があることが強調されています。

さらに、内部コンポーネントとしてのキャッシュの扱いや、SharePointインデクサーを使用する際の注意点についても再確認されています。全体として、この更新はユーザーに対して正確で関連性の高い情報を提供し、より良い使用体験を促進することを目指しています。

## articles/search/enrichment-cache-how-to-manage.md{#item-a972bd}

<details>
<summary>Diff</summary>
````diff
@@ -8,16 +8,16 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
   - sfi-ropc-nochange
+ai-usage: ai-assisted
 ---
 
-# Manage an enrichment cache
+# Manage an enrichment cache (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT] 
-> This feature is in preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [preview REST API](/rest/api/searchservice/search-service-api-versions#preview-versions) supports this feature.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-An *enrichment cache* is an optional feature that stores enriched content created during [skillset execution](cognitive-search-working-with-skillsets.md). It preserves content between runs so that only changed skills and documents require reprocessing. It isn't a backup of skillset outputs, indexer state, or indexed documents. 
+An *enrichment cache* (preview) is an optional feature that stores enriched content created during [skillset execution](cognitive-search-working-with-skillsets.md). It preserves content between runs so that only changed skills and documents require reprocessing. It isn't a backup of skillset outputs, indexer state, or indexed documents.
 
 You create the enrichment cache in Azure Storage. The cache contains the output from [document cracking](search-indexer-overview.md#document-cracking), plus the outputs of each skill for every document. Although caching is billable (it uses Azure Storage), the overall cost of enrichment is reduced because the costs of storage are less than image extraction and AI processing.
 
@@ -32,7 +32,7 @@ If you configure an enrichment cache, this article explains how to manage skill
 ## Limitations
 
 > [!CAUTION]
-> If you're using the [SharePoint indexer (Preview)](search-how-to-index-sharepoint-online.md), avoid incremental enrichment. Under certain circumstances, the cache becomes invalid. To reload it, perform an [indexer reset and full rebuild](search-howto-run-reset-indexers.md).
+> If you're using the [SharePoint indexer (preview)](search-how-to-index-sharepoint-online.md), avoid incremental enrichment. Under certain circumstances, the cache becomes invalid. To reload it, perform an [indexer reset and full rebuild](search-howto-run-reset-indexers.md).
 
 Large data sources have an additional cache limitation.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンリッチメントキャッシュ管理機能のプレビュー状態の表記追加"
}
```

### Explanation
この変更は、Azureにおけるエンリッチメントキャッシュの管理に関するドキュメントの更新を目的としています。主な修正点は、記事タイトルに「(preview)」が追加され、この機能が現在プレビュー段階にあることが明示されたことです。また、重要な注意事項には、プレビュー機能の利用に関する情報が含まれています。

エンリッチメントキャッシュは、スキルセットの実行中に生成されたエンリッチコンテンツを保存するオプション機能であるとし、その内容が実行間で保持されることを説明しています。この機能によって、変更されたスキルやドキュメントのみが再処理されるため、処理効率が向上します。さらに、キャッシュの作成にはAzureストレージを利用し、コスト効率が良い点が紹介されています。

これらの変更は、ユーザーに対してエンリッチメントキャッシュの機能を使用する際の注意点を強調し、プレビュー機能に関する情報を正確に提供することを目指しています。全体的に、ユーザーがこの機能を適切に管理し、利用できるように支援しています。

## articles/search/get-started-portal-agentic-retrieval.md{#item-2bf1dc}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
 title: "Quickstart: Agentic Retrieval in the Azure Portal"
-description: Learn how to use agentic retrieval in the Azure portal for a conversational search experience powered by Azure AI Search and Azure OpenAI models.
+description: Learn how to use agentic retrieval in the Azure portal for a conversational experience powered by Azure AI Search and Azure OpenAI.
 author: mattwojo
 ms.author: mattwoj
 ms.service: azure-ai-search
@@ -9,21 +9,22 @@ ms.custom:
 ms.topic: quickstart
 ms.date: 07/20/2026
 ai-usage: ai-assisted
+#customer intent: As an application developer, I want to create and test a blob knowledge source and knowledge base in the Azure portal and understand the generated ingestion objects so that I can evaluate a conversational search experience without writing code.
 ---
 
 # Quickstart: Agentic retrieval in the Azure portal
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [GA announcement](./includes/previews/agentic-retrieval-ga-announcement.md)]
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 In this quickstart, use [agentic retrieval](agentic-retrieval-overview.md) in the Azure portal to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models.
 
 The portal guides you through the process of creating the following objects:
 
 + A *knowledge source* that references a container in Azure Blob Storage. When you create a blob knowledge source, Azure AI Search automatically generates an index and other pipeline objects to ingest and enrich your content for agentic retrieval.
 
-+ A *knowledge base* that uses agentic retrieval to infer the underlying information need, plan and execute subqueries, and formulate a natural-language answer using the optional answer synthesis output mode.
++ A *knowledge base* that uses LLM-based query planning (preview) to infer the underlying information need and execute subqueries and answer synthesis (preview) to formulate a natural-language answer.
 
 Afterwards, you test the knowledge base by submitting a complex query that requires information from multiple documents and reviewing the synthesized answer.
 
@@ -80,7 +81,7 @@ To configure access for this quickstart:
 > + Billing from Azure AI Search for agentic retrieval.
 > + Billing from Azure OpenAI for query planning and answer synthesis.
 >
-> For more information, see [Availability and pricing of agentic retrieval](agentic-retrieval-overview.md#availability-and-pricing).
+> For more information, see [Region availability, limits, and billing](agentic-retrieval-overview.md#region-availability-limits-and-billing).
 
 ## Prepare sample data
 
@@ -130,9 +131,9 @@ To create the knowledge source for this quickstart:
 
 ## Create a knowledge base
 
-A knowledge base uses your knowledge source and deployed LLM to orchestrate agentic retrieval. When a user submits a complex query, the LLM generates subqueries that are sent simultaneously to your knowledge source. Azure AI Search then semantically ranks the results for relevance and combines the best results into a single, unified response.
+A knowledge base uses your knowledge source and deployed LLM to orchestrate agentic retrieval. When a user submits a complex query, LLM-based query planning (preview) generates subqueries that are sent simultaneously to your knowledge source. Azure AI Search then semantically ranks the results for relevance and combines the best results into a single, unified response.
 
-The output mode determines how the knowledge base formulates answers. You can either use extractive data for verbatim content or [answer synthesis](agentic-retrieval-how-to-answer-synthesis.md) for natural-language answer generation. By default, the portal uses answer synthesis.
+The output mode determines how the knowledge base formulates answers. You can either use extractive data for verbatim content or [answer synthesis (preview)](agentic-retrieval-how-to-answer-synthesis.md) for natural-language answer generation. By default, the portal uses answer synthesis.
 
 To create the knowledge base for this quickstart:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルに関するクイックスタートガイドの修正"
}
```

### Explanation
この変更は、Azureポータルにおけるエージェンティックリトリーバルのクイックスタートガイドに関する内容を更新しています。主な修正点は、説明文の修正と、リトリーバル機能に関連するプレビュー機能の明示化です。特に、「会話体験」に関する表現がより具体的になり、ユーザーが何を期待できるのかが明確に示されています。

新たに追加された情報として、「顧客の意図」としてアプリケーション開発者の視点が強調され、コードを書かずに会話型検索体験を評価できる方法が紹介されています。また、エンジニアリングプロセスにおいて生成されるサブクエリや回答合成に関するプレビュー機能が強調され、それによって知識ベースがどのように機能するかが解説されています。

クイックスタートでのサンプルデータの準備や、エージェンティックリトリーバルの利用に関わる請求情報に関する更新も行われています。これにより、ユーザーはこの機能を効果的に活用し、利用に際する注意点を理解する手助けとなることを目指しています。全体として、文書の明確さと実用性を向上させるための修正が行われました。

## articles/search/hybrid-search-how-to-query.md{#item-345ce6}

<details>
<summary>Diff</summary>
````diff
@@ -14,6 +14,8 @@ ms.date: 08/06/2026
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
 [Hybrid search](hybrid-search-overview.md) combines text (keyword) and vector queries in a single search request. Both queries execute in parallel. The results are merged and reordered by new search scores, using [Reciprocal Rank Fusion (RRF)](hybrid-search-ranking.md) to return a unified result set. In many cases, [per benchmark tests](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/azure-ai-search-outperforming-vector-search-with-hybrid-retrieval-and-reranking/3929167), hybrid queries with semantic ranking return the most relevant results.
 
 In this article, learn how to:
@@ -48,7 +50,7 @@ By the end of this article, you can execute hybrid queries that combine keyword
 
 + Newer stable or preview packages of the Azure SDKs (see change logs for SDK feature support).
 
-+ [Stable REST APIs](/rest/api/searchservice/documents/search-post) or a recent preview API version if you're using preview features like [maxTextRecallSize and countAndFacetMode(preview)](#set-maxtextrecallsize-and-countandfacetmode).
++ [Stable REST APIs](/rest/api/searchservice/documents/search-post) or a recent preview API version if you're using preview features like [maxTextRecallSize and countAndFacetMode (preview)](#set-maxtextrecallsize-and-countandfacetmode-preview).
 
     For readability, we use REST examples to explain how the APIs work. You can use a REST client like Visual Studio Code with the REST extension to build hybrid queries. You can also use the Azure SDKs. For more information, see [Quickstart: Vector search](search-get-started-vector.md).
 
@@ -293,19 +295,17 @@ await foreach (SearchResult<SearchDocument> result in results.GetResultsAsync())
 
 ---
 
-## Set maxTextRecallSize and countAndFacetMode
-
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+## Set maxTextRecallSize and countAndFacetMode (preview)
 
-A hybrid query can be tuned to control how much of each subquery contributes to the combined results. Setting `maxTextRecallSize` specifies how many BM25-ranked results are passed to the hybrid ranking model.
+A hybrid query can be tuned to control how much of each subquery contributes to the combined results. Setting the `maxTextRecallSize` parameter (preview) specifies how many BM25-ranked results are passed to the hybrid ranking model.
 
 If your request includes facets, use nonvector fields that are marked as `facetable` in the index. Vector fields aren't facetable.
 
 Facet counts depend on the query type:
 
 + In a text-only query, facets count the documents that match the text query.
 + In a vector-only query, facets count the `k` documents returned by the vector query.
-+ In a hybrid query, facets account for both vector and text results. The vector side contributes the `k` nearest documents. The text side contributes BM25-ranked documents. The `countAndFacetMode` parameter determines whether count and facet calculations use all text matches or only the text matches that are retrieved for ranking.
++ In a hybrid query, facets account for both vector and text results. The vector side contributes the `k` nearest documents. The text side contributes BM25-ranked documents. The `countAndFacetMode` parameter (preview) determines whether count and facet calculations use all text matches or only the text matches that are retrieved for ranking.
 
 If you use `maxTextRecallSize`, you might also want to set `countAndFacetMode`. This parameter determines whether `count` and `facets` include all documents that matched the text query, or only documents retrieved within the `maxTextRecallSize` window. The default value is `countAllResults`.
 
@@ -586,7 +586,7 @@ A query might match to any number of documents, as many as all of them if the se
 Both `k` and `top` are optional. Unspecified, the default number of results in a response is 50. You can set `top` and `skip` to [page through more results](search-pagination-page-layout.md#paging-results) or change the default.
 
 > [!NOTE]
-> If you're using hybrid search in 2024-05-01-preview API, you can control the number of results from the keyword query using [maxTextRecallSize](#set-maxtextrecallsize-and-countandfacetmode). Combine this with a setting for `k` to control the representation from each search subsystem (keyword and vector).
+> If you're using hybrid search in 2024-05-01-preview API, you can control the number of results from the keyword query using [maxTextRecallSize](#set-maxtextrecallsize-and-countandfacetmode-preview). Combine this with a setting for `k` to control the representation from each search subsystem (keyword and vector).
 
 ### Semantic ranker results
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索クエリに関するドキュメントの修正"
}
```

### Explanation
この変更は、ハイブリッド検索のクエリに関するドキュメントを更新し、プレビュー機能に関する情報を追加することを目的としています。特に、ハイブリッド検索がテキスト（キーワード）とベクトルクエリを1つの検索リクエストで統合し、結果を新しいスコアに基づいて再評価する仕組みについて詳述されています。

本更新では、Azure SDKの新しい安定版またはプレビュー版のパッケージの利用を推奨する情報が追加され、ユーザーが最新機能を正確に活用できるようになっています。また、`maxTextRecallSize`や`countAndFacetMode`といったプレビュー機能に特に注目し、これらの設定がハイブリッドクエリの結果に与える影響を詳しく説明しています。

具体的には、ハイブリッド検索で使用される結果の制御やファセットの計算方法についてのセクションに修正が加えられており、これにはプレビュー機能に関連する内容が強調されています。全体として、ユーザーに対する新しい機能の明確な理解を促進し、ハイブリッド検索を効果的に利用できるようにすることを目的とした更新です。

## articles/search/hybrid-search-ranking.md{#item-dad887}

<details>
<summary>Diff</summary>
````diff
@@ -130,7 +130,7 @@ In this example, the `@search.score` (weighted) values go to the RRF ranking mod
 
 By default, if you aren't using pagination, the search engine returns the top 50 highest ranking matches for full-text search, and the most similar `k` matches for vector search. In a hybrid query, `top` determines the number of results in the response. Based on defaults, the top 50 highest ranked matches of the unified result set are returned.
 
-Often, the search engine finds more results than `top` and `k`. To return more results, use the paging parameters `top`, `skip`, and `next`. Paging is how you determine the number of results on each logical page and navigate through the full payload. You can [set `maxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) to larger values (the default is 1,000) to return more results from the text side of hybrid query.
+Often, the search engine finds more results than `top` and `k`. To return more results, use the paging parameters `top`, `skip`, and `next`. Paging is how you determine the number of results on each logical page and navigate through the full payload. You can [set `maxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview) to larger values (the default is 1,000) to return more results from the text side of hybrid query.
 
 By default, full-text search is subject to a maximum limit of 1,000 matches (see [API response limits](search-limits-quotas-capacity.md#api-response-limits)). Once 1,000 matches are found, the search engine no longer looks for more.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索ランキングに関するドキュメントの修正"
}
```

### Explanation
この変更は、ハイブリッド検索のランキングに関するドキュメントにおいて、テキスト検索の結果取得に関するリンクを更新しています。具体的には、`maxTextRecallSize`パラメータに関連するリンクを改訂され、プレビュー機能を明示する形で新しいセクションへと修正されています。

この修正により、ユーザーはハイブリッドクエリから取得するテキスト結果の最大値を調整する方法について、より正確な情報を得ることができます。また、ページングパラメータの使用方法についての説明はそのまま保持され、結果の数やナビゲーション方法を理解するのに役立ちます。

全体として、この更新はユーザーに対し、ハイブリッド検索の機能をさらに活用できるように情報を提供することを目的としています。

## articles/search/includes/previews/agentic-retrieval-ga-announcement.md{#item-4f2f62}

<details>
<summary>Diff</summary>
````diff
@@ -1,14 +0,0 @@
----
-title: Agentic Retrieval GA Announcement
-description: Note announcing that some agentic retrieval features are generally available in the 2026-04-01 REST API, with portal caveats and migration guidance.
-author: haileytap
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 05/19/2026
----
-
-> [!NOTE]
-> Some agentic retrieval features are generally available in the 2026-04-01 REST API via programmatic access. The Azure portal and Microsoft Foundry portal continue to provide preview-only access to all agentic retrieval features. For migration guidance, including a breakdown of what's generally available and what remains in preview, see [Migrate agentic retrieval code to the latest version](../../agentic-retrieval-how-to-migrate.md).
->
-> If you choose to use a preview REST API, you can access agentic retrieval capabilities that aren't yet generally available. Preview features are provided without a service-level agreement and aren't recommended for production workloads. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エージェント検索の一般提供に関するお知らせの削除"
}
```

### Explanation
この変更では、エージェント検索に関する一般提供（GA）のお知らせを含むドキュメントが完全に削除されました。このドキュメントには、2026年4月1日付けのREST APIで一般提供されるエージェント検索機能に関する情報や、ポータルでの制約、移行ガイドが含まれていました。

主な内容としては、プレビューの機能が引き続きAzureポータルやMicrosoft Foundryポータルでのみ使用可能であること、一般提供された機能とプレビューの機能の違いについての詳細な案内、そしてプレビューレベルの機能を使用する際の注意点が取り上げられていました。

この削除により、エージェント検索に関する公式な情報源が減少し、その影響を受けるのはこれらの機能の利用を検討している開発者やユーザーになると考えられます。一般提供に関する情報がなくなることで、これらの機能に関するガイダンスが不足し、ユーザーが適切な決定を下すための参考が減少します。

## articles/search/includes/previews/agentic-retrieval-ga-feature.md{#item-2de8dc}

<details>
<summary>Diff</summary>
````diff
@@ -1,14 +0,0 @@
----
-title: Agentic Retrieval GA Feature
-description: Note indicating a specific agentic retrieval feature is generally available in the 2026-04-01 REST API via programmatic access.
-author: haileytap
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 05/19/2026
----
-
-> [!NOTE]
-> This agentic retrieval feature is generally available in the 2026-04-01 REST API via programmatic access. The Azure portal and Microsoft Foundry portal continue to provide preview-only access to all agentic retrieval features. For migration guidance, see [Migrate agentic retrieval code to the latest version](../../agentic-retrieval-how-to-migrate.md).
->
-> If you choose to use a preview REST API, you can access capabilities that aren't yet generally available for this feature. Preview features are provided without a service-level agreement and aren't recommended for production workloads. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エージェント検索の一般提供機能に関するお知らせの削除"
}
```

### Explanation
この変更は、エージェント検索に関連する特定の一般提供（GA）機能を示すドキュメントが削除されたことを示しています。この文書には、2026年4月1日付けのREST APIでプログラムアクセスを通じて一般提供されるエージェント検索機能に関する情報が記載されており、移行ガイドも含まれていました。

具体的には、この機能は一般提供されている一方で、AzureポータルやMicrosoft Foundryポータルでは引き続きプレビュー版の機能しか利用できないこと、またプレビューレベルの機能にはサービスレベル契約が適用されないため、本番環境での使用は推奨されないという注意点が挙げられていました。

このドキュメントの削除により、ユーザーはエージェント検索の一般提供されている機能に対する公式な情報を失うことになります。結果として、これを利用する開発者やユーザーがその機能の利用方法や移行手順を理解するのが難しくなる可能性があります。

## articles/search/includes/previews/agentic-retrieval-preview-feature.md{#item-e94474}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +0,0 @@
----
-title: Agentic Retrieval Preview Feature
-description: Note indicating a specific agentic retrieval feature remains in preview despite the overall GA release in the 2026-04-01 REST API.
-author: haileytap
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 04/16/2026
----
-
-> [!NOTE]
-> Some agentic retrieval features are generally available in the 2026-04-01 REST API. However, this feature remains in preview and requires a preview REST API. Preview features are provided without a service-level agreement and aren't recommended for production workloads. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エージェント検索のプレビューフィーチャーに関するお知らせの削除"
}
```

### Explanation
この変更は、エージェント検索の特定のプレビューフィーチャーに関するドキュメントが削除されたことを示しています。この文書は、2026年4月1日付けのREST APIで一般提供（GA）される一部のエージェント検索機能に関して説明していましたが、その中で特定の機能がプレビューのままであることも記載されていました。

具体的には、一般提供されている機能の中で、この特定の機能はまだプレビュー版に留まっており、プレビューREST APIを必要とすること、またプレビューミッションはサービスレベル契約の対象外であり、本番環境での利用は推奨されないという重要な注意点が述べられていました。

このドキュメントの削除により、ユーザーはこのプレビューフィーチャーに関する公式の情報を失い、どの機能が依然としてプレビューであるかを把握するのが難しくなるでしょう。その結果、開発者やユーザーが製品環境における適切な使用方法を見つけることに影響が出る可能性があります。

## articles/search/includes/previews/preview-generic.md{#item-51bbcc}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +0,0 @@
----
-title: Include File
-description: Include file
-author: haileytap
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 03/19/2024
-ms.custom: include, ignite-2024
----
-
-> [!NOTE]
-> This feature is currently in preview. This preview is provided without a service-level agreement and isn't recommended for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プレビューフィーチャーに関する一般的なインクルードファイルの削除"
}
```

### Explanation
この変更は、プレビューフィーチャーに関する一般的なインクルードファイルが削除されたことを示しています。このファイルには、特定の機能が現在プレビュー版であることが記載されており、そのプレビューはサービスレベル契約が適用されないため、本番環境での使用は推奨されないという重要な警告が含まれていました。

具体的には、プレビュー中の機能にはサポートがない場合や制約のある能力が発生する可能性があることが説明されていました。また、Azureのプレビュー機能に関する補足利用規約へのリンクも提供されていました。

このインクルードファイルの削除により、ユーザーはプレビューフィーチャーの利用方法や注意点についての公式な情報を失うことになります。そのため、開発者やユーザーがこれらの機能を安全に利用することが難しくなる可能性があります。

## articles/search/includes/previews/preview-terms.md{#item-b7699b}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,13 @@
+---
+title: Include File
+description: Include file for the preview terms banner displayed across Azure AI Search documentation.
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 09/16/2026
+ai-usage: ai-assisted
+---
+
+> [!IMPORTANT]
+> Features, capabilities, or properties marked (preview) aren't covered by a service-level agreement, aren't recommended for production workloads, and might change or be constrained before they become generally available. The [Azure AI Search preview terms](/azure/search/search-preview-terms) apply to all preview functionality, whether it's standalone or part of a generally available feature.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "プレビューフィーチャーの利用に関する新しいインクルードファイルの追加"
}
```

### Explanation
この変更は、Azure AI Searchのドキュメントにおけるプレビューフィーチャーに関する新しいインクルードファイルが追加されたことを示しています。このファイルは、プレビュー用の用語バナーに関連する内容を含んでおり、特にプレビューフィーチャーの使用に関する重要な注意事項が記載されています。

具体的には、(プレビュー)とマークされた機能や能力、特性はサービスレベル契約の対象外であり、本番環境での利用は推奨されず、一般提供される前に変更されるか、制約を受ける可能性があるという警告が含まれています。また、このインクルードファイルには、全プレビュー機能に適用される[Azure AI Searchのプレビュー条項]へのリンクも提供されています。

この追加により、ユーザーはプレビューフィーチャーを利用する際のリスクや重要な情報を理解しやすくなり、文書全体の貴重なリソースとなるでしょう。それによって、より安全かつ効果的にプレビュー機能を活用できるようになることが期待されます。

## articles/search/includes/quickstarts/agentic-retrieval-csharp.md{#item-f93ed3}

<details>
<summary>Diff</summary>
````diff
@@ -6,11 +6,9 @@ ms.custom: dev-focus
 ai-usage: ai-assisted
 ---
 
-[!INCLUDE [Preview API usage](../previews/agentic-retrieval-preview-api-usage.md)]
+In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview.md) to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models. 
 
-In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview.md) to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models.
-
-A *knowledge base* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the knowledge base outputs raw content from your sources, but this quickstart uses the answer synthesis output mode for natural-language answer generation.
+The *knowledge base* uses LLM-based query planning (preview) to decompose complex queries into subqueries. It then runs the subqueries against one or more *knowledge sources* and returns results with metadata. By default, a knowledge base returns raw content from its sources, but this quickstart uses answer synthesis (preview) to generate natural-language answers.
 
 Although you can use your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book.
 
@@ -300,7 +298,7 @@ Console.WriteLine($"Knowledge source '{knowledgeSourceName}' created or updated
 
 To target `earth-knowledge-source` and your `gpt-5-mini` deployment at query time, you need a knowledge base. The following code defines a knowledge base named `earth-knowledge-base`.
 
-`OutputMode` is set to `AnswerSynthesis`, enabling natural-language answers that cite the retrieved documents and follow the provided `AnswerInstructions`.
+`OutputMode` (preview) is set to `AnswerSynthesis`, enabling natural-language answers that cite the retrieved documents and follow the provided `AnswerInstructions`. `RetrievalReasoningEffort` (preview) is set to `low` to control the amount of reasoning used for query planning.
 
 ```csharp
 // Create a knowledge base
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルのC#クイックスタートの内容修正"
}
```

### Explanation
この変更は、C#を用いたエージェンティックリトリーバルのクイックスタートに関する内容の修正を示しています。主に、文の明確化と情報の更新が行われました。

具体的には、エージェンティックリトリーバルの使用方法についての説明が改善され、LLMベースのクエリプランニングや回答合成機能のプレビュー特性に関する詳細が追加されました。具体的には、複雑なクエリをサブクエリに分解する過程や、ナチュラルランゲージの回答生成についての説明が強化されています。

また、`OutputMode`と`RetrievalReasoningEffort`に関連する設定の記載も更新され、これらの機能がプレビュー版であることが明確にされています。これにより、ユーザーは新しい機能の使用に関する理解を深め、より洗練された検索体験を実現するための具体的な情報を得ることができます。この修正は、文書の情報の正確性とユーザーの利便性を向上させるためのものであり、エージェンティックリトリーバルを活用する際の役立つリソースとなっています。

## articles/search/includes/quickstarts/agentic-retrieval-java.md{#item-4e2c55}

<details>
<summary>Diff</summary>
````diff
@@ -6,11 +6,9 @@ ms.custom: dev-focus
 ai-usage: ai-assisted
 ---
 
-[!INCLUDE [Preview API usage](../previews/agentic-retrieval-preview-api-usage.md)]
+In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview.md) to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models. 
 
-In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview.md) to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models.
-
-A *knowledge base* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the knowledge base outputs raw content from your sources, but this quickstart uses the answer synthesis output mode for natural-language answer generation.
+The *knowledge base* uses LLM-based query planning (preview) to decompose complex queries into subqueries. It then runs the subqueries against one or more *knowledge sources* and returns results with metadata. By default, a knowledge base returns raw content from its sources, but this quickstart uses answer synthesis (preview) to generate natural-language answers.
 
 Although you can use your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book.
 
@@ -348,7 +346,7 @@ indexClient.createOrUpdateKnowledgeSource(indexKnowledgeSource);
 
 To target `earth-knowledge-source` and your `gpt-5-mini` deployment at query time, you need a knowledge base. The following code defines a knowledge base named `earth-knowledge-base`.
 
-Set `OutputMode` to `ANSWER_SYNTHESIS` to enable natural-language answers that cite the retrieved documents and follow the provided `AnswerInstructions`.
+`OutputMode` (preview) is set to `ANSWER_SYNTHESIS` to enable natural-language answers that cite the retrieved documents and follow the provided `AnswerInstructions`. `RetrievalReasoningEffort` (preview) is set to `low` to control the amount of reasoning used for query planning.
 
 ```java
 AzureOpenAIVectorizerParameters openAiParameters =
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルのJavaクイックスタートの内容修正"
}
```

### Explanation
この変更は、Javaを用いたエージェンティックリトリーバルのクイックスタートに関する内容が修正されたことを示しています。主な変更点は、文の整理や情報の更新により、これまでの説明が改善されていることです。

具体的には、エージェンティックリトリーバルを使用しての対話型検索体験の構築に関する説明が明確にされ、LLM（大規模言語モデル）を用いたクエリプランニングや回答合成機能についての最新情報が追加されました。特に、複雑なクエリをサブクエリに分解し、それを知識ソースに対して実行する流れが強調されています。

さらに、`OutputMode`や`RetrievalReasoningEffort`における設定のプレビュー情報が明示されており、これにより、ユーザーは新機能で得られる自然言語の回答を利用しやすくなります。このような改善は、文書の正確さを向上させ、開発者がエージェンティックリトリーバル機能をより効果的に活用するための手助けとなるでしょう。

## articles/search/includes/quickstarts/agentic-retrieval-javascript.md{#item-715283}

<details>
<summary>Diff</summary>
````diff
@@ -6,11 +6,9 @@ ms.custom: dev-focus
 ai-usage: ai-assisted
 ---
 
-[!INCLUDE [Preview API usage](../previews/agentic-retrieval-preview-api-usage.md)]
+In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview.md) to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models. 
 
-In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview.md) to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models.
-
-A *knowledge base* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the knowledge base outputs raw content from your sources, but this quickstart uses the answer synthesis output mode for natural-language answer generation.
+The *knowledge base* uses LLM-based query planning (preview) to decompose complex queries into subqueries. It then runs the subqueries against one or more *knowledge sources* and returns results with metadata. By default, a knowledge base returns raw content from its sources, but this quickstart uses answer synthesis (preview) to generate natural-language answers.
 
 Although you can use your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book.
 
@@ -364,7 +362,7 @@ console.log(`✅ Knowledge source 'earth-knowledge-source' created successfully.
 
 To target `earth-knowledge-source` and your `gpt-5-mini` deployment at query time, you need a knowledge base. The following code defines a knowledge base named `earth-knowledge-base`.
 
-`outputMode` is set to `answerSynthesis`, enabling natural-language answers that cite the retrieved documents and follow the provided `answerInstructions`.
+`outputMode` (preview) is set to `answerSynthesis`, enabling natural-language answers that cite the retrieved documents and follow the provided `answerInstructions`.
 
 ```javascript
 await searchIndexClient.createKnowledgeBase({
@@ -403,6 +401,8 @@ You're ready to run agentic retrieval. The following code sends a two-part user
 1. Uses semantic ranker to rerank and filter the results.
 1. Synthesizes the top results into a natural-language answer.
 
+`retrievalReasoningEffort` (preview) is set to `low` to control the amount of reasoning used for query planning.
+
 ```javascript
 const knowledgeRetrievalClient = new KnowledgeRetrievalClient(
     process.env.AZURE_SEARCH_ENDPOINT,
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルのJavaScriptクイックスタートの内容修正"
}
```

### Explanation
この変更は、JavaScriptを用いたエージェンティックリトリーバルのクイックスタートに関するドキュメントにおける修正を示しています。主な目的は、情報の正確性と可読性を向上させることです。変更された内容には、エージェンティックリトリーバルの使用方法と関連する設定の詳細が含まれています。

具体的には、対話型検索体験を構築するためのエージェンティックリトリーバルの使用方法についての説明が明確化され、LLM（大規模言語モデル）を用いたクエリプランニングの詳細が新たに追加されました。特に、複雑なクエリをサブクエリに分解し、その結果を知識ソースから取得するプロセスに焦点が当てられています。

さらに、`outputMode`や`retrievalReasoningEffort`に関連する設定が更新され、それぞれの機能がプレビュー版であることが指摘されています。これにより、ユーザーはナチュラルランゲージの回答生成のための設定を理解しやすくなり、クエリプランニングの推論の程度を制御する方法についても説明が加わりました。

このような変更は、開発者がエージェンティックリトリーバル機能を効率的に利用できるよう、より明確で役立つ情報を提供することを目的としています。

## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -6,11 +6,9 @@ ms.custom: dev-focus
 ai-usage: ai-assisted
 ---
 
-[!INCLUDE [Preview API usage](../previews/agentic-retrieval-preview-api-usage.md)]
+In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview.md) to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models. 
 
-In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview.md) to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models.
-
-A *knowledge base* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the knowledge base outputs raw content from your sources, but this quickstart uses the answer synthesis output mode for natural-language answer generation.
+The *knowledge base* uses LLM-based query planning (preview) to decompose complex queries into subqueries. It then runs the subqueries against one or more *knowledge sources* and returns results with metadata. By default, a knowledge base returns raw content from its sources, but this quickstart uses answer synthesis (preview) to generate natural-language answers.
 
 Although you can use your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book.
 
@@ -278,7 +276,7 @@ print(f"Knowledge source '{knowledge_source_name}' created or updated successful
 
 To target `earth-knowledge-source` and your `gpt-5-mini` deployment at query time, you need a knowledge base. The following code defines a knowledge base named `earth-knowledge-base`.
 
-`output_mode` is set to `answerSynthesis`, enabling natural-language answers that cite the retrieved documents and follow the provided `answer_instructions`.
+`output_mode` (preview) is set to `answerSynthesis`, enabling natural-language answers that cite the retrieved documents and follow the provided `answer_instructions`.
 
 ```python
 # Create a knowledge base
@@ -338,6 +336,8 @@ You're ready to run agentic retrieval. The following code sends a two-part user
 1. Uses semantic ranker to rerank and filter the results.
 1. Synthesizes the top results into a natural-language answer.
 
+`retrieval_reasoning_effort` (preview) is set to `low` to control the amount of reasoning used for query planning.
+
 ```python
 # Run agentic retrieval
 agent_client = KnowledgeBaseRetrievalClient(endpoint=search_endpoint, knowledge_base_name=knowledge_base_name, credential=credential)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルのPythonクイックスタートの内容修正"
}
```

### Explanation
この変更は、Pythonを用いたエージェンティックリトリーバルのクイックスタートに関するドキュメントの修正を示しています。主な目的は、情報の精度を向上させ、利用者が理解しやすい内容にすることです。

具体的には、エージェンティックリトリーバルを用いて対話型の検索体験を構築する手法についての説明が強化され、LLM（大規模言語モデル）を活用したクエリプランニング機能の詳細が追加されました。これにより、複雑なクエリをサブクエリに分解し、それを知識ソースに対して実行する能力が強調されています。

さらに、`output_mode`や`retrieval_reasoning_effort`に関する設定内容が更新され、それぞれの機能がプレビュー版であることが強調されています。これにより、ユーザーはナチュラルランゲージの回答生成やクエリプランニングの推論の程度を制御する方法について理解しやすくなります。

このような更新は、開発者がエージェンティックリトリーバル機能を効果的に活用できるよう、より分かりやすい情報を提供することを意図しています。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

<details>
<summary>Diff</summary>
````diff
@@ -6,11 +6,9 @@ ms.custom: dev-focus
 ai-usage: ai-assisted
 ---
 
-[!INCLUDE [Preview API usage](../previews/agentic-retrieval-preview-api-usage.md)]
+In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview.md) to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models. 
 
-In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview.md) to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models.
-
-A *knowledge base* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the knowledge base outputs raw content from your sources, but this quickstart uses the answer synthesis output mode for natural-language answer generation.
+The *knowledge base* uses LLM-based query planning (preview) to decompose complex queries into subqueries. It then runs the subqueries against one or more *knowledge sources* and returns results with metadata. By default, a knowledge base returns raw content from its sources, but this quickstart uses answer synthesis (preview) to generate natural-language answers.
 
 Although you can use your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book.
 
@@ -332,7 +330,7 @@ Authorization: Bearer {{token}}
 
 To target your `earth-knowledge-source` and `gpt-5-mini` deployment at query time, you need a knowledge base. The following code defines a base named `earth-knowledge-base`.
 
-`outputMode` is set to `answerSynthesis`, enabling natural-language answers that cite the retrieved documents and follow the provided `answerInstructions`.
+`outputMode` (preview) is set to `answerSynthesis`, enabling natural-language answers that cite the retrieved documents and follow the provided `answerInstructions`.
 
 ```HTTP
 ### Create a knowledge base
@@ -374,6 +372,8 @@ You're ready to run agentic retrieval. The following code sends a two-part user
 1. Uses semantic ranker to rerank and filter the results. This example excludes responses with a reranker score of `2.5` or lower.
 1. Synthesizes the top results into a natural-language answer.
 
+`retrievalReasoningEffort` (preview) is set to `low` to control the amount of reasoning used for query planning.
+
 ```HTTP
 ### Run agentic retrieval
 POST {{search-url}}/knowledgebases/{{knowledge-base-name}}/retrieve?api-version={{api-version}}  HTTP/1.1
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルのRESTクイックスタートの内容修正"
}
```

### Explanation
この変更は、RESTを利用したエージェンティックリトリーバルに関するクイックスタートドキュメントの修正を示しており、情報提供の精度を向上させることが目的です。具体的には、エージェンティックリトリーバルを使用して、Azure AI Searchでインデックスされた文書とAzure OpenAIの大規模言語モデル（LLM）を活用した対話型検索体験を構築する方法についての説明が更新されました。

改修された内容では、知識ベースがLLMを基にしたクエリプランニングを用いて複雑なクエリをサブクエリに分解し、それを知識ソースに対して実行するプロセスが強調されています。また、デフォルトでは知識ベースが元のコンテンツを返す一方で、このクイックスタートではナチュラルランゲージの回答を生成するための「answer synthesis」出力モードが利用されています。

その他の変更点として、`outputMode`に関する説明が更新され、プレビュー版であることが強調され、さらに `retrievalReasoningEffort`が追加されて、クエリプランニングの推論の程度を制御する方法についても説明がなされています。

このように、ドキュメントの修正は、開発者がエージェンティックリトリーバルを使用してより効果的に作業できるよう支援することを目的としています。

## articles/search/includes/quickstarts/agentic-retrieval-setup.md{#item-e5e297}

<details>
<summary>Diff</summary>
````diff
@@ -2,6 +2,7 @@
 ms.service: azure-ai-search
 ms.topic: include
 ms.date: 02/23/2026
+ai-usage: ai-assisted
 ---
 
 ## Configure access
@@ -28,7 +29,7 @@ To configure access for this quickstart:
 > + Billing from Azure AI Search for agentic retrieval.
 > + Billing from Azure OpenAI for query planning and answer synthesis.
 >
-> For more information, see [Availability and pricing of agentic retrieval](../../agentic-retrieval-overview.md#availability-and-pricing).
+> For more information, see [Region availability, limits, and billing](../../agentic-retrieval-overview.md#region-availability-limits-and-billing).
 
 ## Get endpoints
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバル設定のドキュメント修正"
}
```

### Explanation
この変更は、エージェンティックリトリーバル設定に関するクイックスタートドキュメントの修正を示しています。主な目的は、情報の正確さを向上させ、読者により良い理解を提供することです。

具体的には、AIの使用に関するドキュメントに新たに「ai-usage: ai-assisted」というメタデータが追加され、エージェンティックリトリーバルの活用方法が強調されました。また、アクセシビリティを設定する手順のセクションでは、料金に関する情報の表現が変更されました。以前の「Availability and pricing of agentic retrieval」という表現から、より具体的な「Region availability, limits, and billing」に修正されています。この変更により、利用者は特定の地域での利用可能性や制限、請求に関する情報をより明確に把握できるようになります。

これらの更新は、最終的にエージェンティックリトリーバルを設定する際のユーザーエクスペリエンスを向上させることを目的としています。

## articles/search/includes/quickstarts/agentic-retrieval-typescript.md{#item-e6370b}

<details>
<summary>Diff</summary>
````diff
@@ -6,11 +6,9 @@ ms.custom: dev-focus
 ai-usage: ai-assisted
 ---
 
-[!INCLUDE [Preview API usage](../previews/agentic-retrieval-preview-api-usage.md)]
+In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview.md) to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models. 
 
-In this quickstart, you use [agentic retrieval](../../agentic-retrieval-overview.md) to create a conversational search experience powered by documents indexed in Azure AI Search and a large language model (LLM) from Azure OpenAI in Foundry Models.
-
-A *knowledge base* orchestrates agentic retrieval by decomposing complex queries into subqueries, running the subqueries against one or more *knowledge sources*, and returning results with metadata. By default, the knowledge base outputs raw content from your sources, but this quickstart uses the answer synthesis output mode for natural-language answer generation.
+The *knowledge base* uses LLM-based query planning (preview) to decompose complex queries into subqueries. It then runs the subqueries against one or more *knowledge sources* and returns results with metadata. By default, a knowledge base returns raw content from its sources, but this quickstart uses answer synthesis (preview) to generate natural-language answers.
 
 Although you can use your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book.
 
@@ -375,7 +373,7 @@ console.log(`✅ Knowledge source 'earth-knowledge-source' created successfully.
 
 To target `earth-knowledge-source` and your `gpt-5-mini` deployment at query time, you need a knowledge base. The following code defines a knowledge base named `earth-knowledge-base`.
 
-`outputMode` is set to `answerSynthesis`, enabling natural-language answers that cite the retrieved documents and follow the provided `answerInstructions`.
+`outputMode` (preview) is set to `answerSynthesis`, enabling natural-language answers that cite the retrieved documents and follow the provided `answerInstructions`.
 
 ```typescript
 await searchIndexClient.createKnowledgeBase({
@@ -414,6 +412,8 @@ You're ready to run agentic retrieval. The following code sends a two-part user
 1. Uses semantic ranker to rerank and filter the results.
 1. Synthesizes the top results into a natural-language answer.
 
+`retrievalReasoningEffort` (preview) is set to `low` to control the amount of reasoning used for query planning.
+
 ```typescript
 const knowledgeRetrievalClient = new KnowledgeRetrievalClient(
     process.env.AZURE_SEARCH_ENDPOINT!,
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルのTypeScriptクイックスタートの内容修正"
}
```

### Explanation
この変更は、エージェンティックリトリーバルに関するTypeScriptクイックスタートドキュメントの修正を示しています。この修正の主な目的は、文書の内容を最新の情報に更新し、開発者に対する理解を深めることです。

具体的には、エージェンティックリトリーバルを使用して、Azure AI Searchにインデックスされた文書およびAzure OpenAIの大規模言語モデル（LLM）を利用した対話型検索体験を構築する手段に関しての説明が強調されました。また、知識ベースがLLMを使用してクエリプランニングを行い、複雑なクエリをサブクエリに分解する過程についても詳細が更新されています。

さらに、`outputMode`と`retrievalReasoningEffort`の設定についても修正され、これらがプレビュー段階であることが明記されています。特に、`retrievalReasoningEffort`はクエリプランニングにおける推論の程度を制御するための設定です。

全体として、これらの変更は開発者がエージェンティックリトリーバルを効果的に利用できるよう、関連情報をより分かりやすく提供することを目指しています。

## articles/search/index-similarity-and-scoring.md{#item-75603d}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.custom:
 ms.topic: concept-article
 ms.date: 08/27/2025
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Relevance in keyword search (BM25 scoring)
@@ -219,7 +220,7 @@ You can consume these data points in [custom scoring solutions](https://github.c
 
 By default, if you aren't using pagination, the search engine returns the top 50 highest ranking matches for full text search. You can use the `top` parameter to return a smaller or larger number of items (up to 1,000 in a single response). You can use `skip` and `next` to page results. Paging determines the number of results on each logical page and supports content navigation. For more information, see [Shape search results](search-pagination-page-layout.md).
 
-If your full text query is part of a [hybrid query](hybrid-search-how-to-query.md), you can [set `maxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) to increase or decrease the number of results from the text side of the query.
+If your full text query is part of a [hybrid query](hybrid-search-how-to-query.md), you can [set `maxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview) to increase or decrease the number of results from the text side of the query.
 
 Full text search is subject to a maximum limit of 1,000 matches (see [API response limits](search-limits-quotas-capacity.md#api-response-limits)). Once 1,000 matches are found, the search engine no longer looks for more.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスの類似性とスコアリングに関するドキュメントの修正"
}
```

### Explanation
この変更は、インデックスの類似性とスコアリングに関するドキュメントの修正を示しています。主な目的は、利用者に対して最新の情報を提供し、機能の理解を深めてもらうことです。

修正内容では、「ai-usage: ai-assisted」が新たに追加され、AIの使用を強調しています。また、フルテキストクエリがハイブリッドクエリの一部である場合の、`maxTextRecallSize`パラメータについての説明も更新されました。具体的には、このパラメータのリンクが、プレビュー段階を示すものに変更されています。これにより、ユーザーはクエリのテキスト部分からの結果数を増減させる方法をより明確に理解できるようになります。

文書全体にわたり、デフォルトの検索結果の取り扱いやページネーションに関する情報も更新されており、関連する制限やクォータについての詳細が提供されています。これにより、開発者やユーザーは、体系的に情報を確認しやすくなり、検索機能を効果的に活用できるようなリソースを得られることを目指しています。

## articles/search/knowledge-store-concept-intro.md{#item-7475c2}

<details>
<summary>Diff</summary>
````diff
@@ -8,6 +8,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
   - sfi-ropc-nochange
+ai-usage: ai-assisted
 ---
 
 # Knowledge store in Azure AI Search
@@ -128,7 +129,7 @@ For data sources that support change tracking, an indexer will process new and c
 
 ### Changes to a skillset
 
-If you're making changes to a skillset, you should [enable caching of enriched documents](enrichment-cache-how-to-configure.md) to reuse existing enrichments where possible.
+If you're making changes to a skillset, you should [enable caching of enriched documents (preview)](enrichment-cache-how-to-configure.md) to reuse existing enrichments where possible.
 
 Without incremental caching, the indexer will always process documents in order of the high water mark, without going backwards. For blobs, the indexer would process blobs sorted by `lastModified`, regardless of any changes to indexer settings or the skillset. If you change a skillset, previously processed documents aren't updated to reflect the new skillset. Documents processed after the skillset change will use the new skillset, resulting in index documents being a mix of old and new skillsets.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおけるナレッジストアの概念に関するドキュメントの修正"
}
```

### Explanation
この変更は、Azure AI Searchに関連するナレッジストアの概念を説明したドキュメントの修正を示しています。主な目的は、利用者に対して最新の情報を提供し、機能の理解を促進することです。

具体的には、「ai-usage: ai-assisted」が新たに追加され、AIの使用に関する情報が強調されています。また、スキルセットに変更を加える場合における、文書のキャッシュを有効にする重要性が記述された部分の文言が更新されています。変更後の記述では、キャッシュの有効化がプレビュー段階であることを明示しています。

これらの修正は、開発者がスキルセットの変更に対してより適切に対処できるようにするためのものであり、既存の強化を再利用するための方法を明確にしています。このように、ドキュメント全体の情報が最新かつ正確なものとなることを目指しており、結果としてナレッジストアの機能をより効果的に活用できるようにユーザーをサポートしています。

## articles/search/knowledge-store-projection-example-long.md{#item-e18999}

<details>
<summary>Diff</summary>
````diff
@@ -8,6 +8,7 @@ ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
   - sfi-ropc-nochange
+ai-usage: ai-assisted
 ---
 
 # Example of shapes and projections in a knowledge store
@@ -661,4 +662,4 @@ When building projections of different types, file and object projections are ge
 The example in this article demonstrates common patterns on how to create projections. Now that you have a good understanding of the concepts, you're better equipped to build projections for your specific scenario.
 
 > [!div class="nextstepaction"]
-> [Configure caching for incremental enrichment](enrichment-cache-how-to-configure.md)
+> [Configure caching for incremental enrichment (preview)](enrichment-cache-how-to-configure.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナレッジストアにおけるプロジェクションの例に関するドキュメントの修正"
}
```

### Explanation
この変更は、ナレッジストアにおけるプロジェクションの例を示すドキュメントの修正を示しています。主な目的は、利用者に最新の情報を提供し、機能の理解を深めることです。

修正された内容では、「ai-usage: ai-assisted」が新たに追加され、AI関連の使用について強調されています。また、キャッシングの設定に関するリンクの文言が更新され、現在は「プレビュー」段階であることが示されています。これにより、ユーザーはこの機能がまだ最終的な形ではないことを認識し、利用する際に留意すべき点を理解できるようになります。

記事全体では、さまざまなタイプのプロジェクションの構築方法に関する一般的なパターンが示されており、読者が特定のシナリオに応じたプロジェクションを構築するための知識を得ることができるようになっています。これらの更新により、ドキュメントの情報がより正確で役立つものとなり、ナレッジストアの機能を効果的に活用するためのサポートを提供しています。

## articles/search/multimodal-search-overview.md{#item-d82192}

<details>
<summary>Diff</summary>
````diff
@@ -48,7 +48,7 @@ The wizard follows these steps to create a multimodal pipeline:
 
 1. **Generate image descriptions:** The [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md) verbalizes images, producing concise natural-language descriptions for text search and embedding using a large language model (LLM).
 
-1. **Generate embeddings:** The embedding skill creates vector representations of text and images, enabling similarity and hybrid retrieval. You can call [Azure OpenAI](cognitive-search-skill-azure-openai-embedding.md), [Microsoft Foundry](cognitive-search-aml-skill.md), or [Azure Vision](cognitive-search-skill-vision-vectorize.md) embedding models natively.
+1. **Generate embeddings:** The embedding skill creates vector representations of text and images, enabling similarity and hybrid retrieval. You can call [Azure OpenAI](cognitive-search-skill-azure-openai-embedding.md), [Microsoft Foundry](cognitive-search-aml-skill.md), or [Azure Vision (preview)](cognitive-search-skill-vision-vectorize.md) embedding models natively.
 
    Alternatively, you can skip image verbalization and pass the extracted text and images directly to a multimodal embedding model through the [AML skill](cognitive-search-aml-skill.md) or [Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md). For more information, see [Options for multimodal content embedding](#options-for-multimodal-content-embedding).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダル検索の概要に関するドキュメントの修正"
}
```

### Explanation
この変更は、マルチモーダル検索の概要を説明するドキュメントの修正を示しています。主な目的は、利用者に最新の情報を提供し、マルチモーダルパイプラインの構築方法をより明確にすることです。

具体的には、埋め込みモデルに関する部分で、Azure Visionを使用した際のリンクが「プレビュー」段階であることを示すために更新されました。この変更により、ユーザーはAzure Visionの機能がまだ最終的ではなく、今後の変更が考えられることを理解できるようになります。

また、埋め込みスキルがテキストと画像のベクトル表現を作成するプロセスの重要性が引き続き強調されています。この情報は、ユーザーがマルチモーダル検索システムを適切に活用し、さまざまなリトリーバル手法を理解するために役立ちます。全体として、ドキュメントは最新かつ正確な情報を提供し、ユーザーが効率的にマルチモーダル検索を活用できるようにサポートしています。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -9,6 +9,7 @@ ms.custom:
   - ignite-2024
   - build-2025
 ai-usage: ai-assisted
+#customer intent: As a solution architect, I want to compare agentic retrieval and classic RAG for common RAG challenges so that I can choose an Azure AI Search approach that fits my application requirements.
 ---
 
 # Retrieval-augmented generation (RAG) in Azure AI Search
@@ -31,7 +32,7 @@ Retrieval-augmented generation (RAG) is a pattern that extends LLM capabilities
 
 Azure AI Search provides two approaches designed specifically for these RAG challenges:
 
-- **[Agentic retrieval](#modern-rag-with-agentic-retrieval)**: A complete RAG pipeline with LLM-assisted query planning, multi-source access, and structured responses optimized for agent consumption.
+- **[Agentic retrieval](#modern-rag-with-agentic-retrieval)**: A complete RAG pipeline with LLM-based query planning (preview), multi-source access, and structured responses optimized for agent consumption.
 
 - **[Classic RAG pattern](#classic-rag-pattern-for-azure-ai-search)**: The proven approach using hybrid search and semantic ranking, ideal for simpler requirements or when generally available (GA) features are required.
 
@@ -54,7 +55,7 @@ The following sections explain how each approach solves specific RAG challenges.
 - Semantic ranking re-scores results based on meaning, not just keywords.
 - Vector similarity search matches concepts, not exact terms.
 
-[Learn more about query planning](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md).
+[Learn more about query planning (preview)](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md).
 
 ### Solving multisource data challenges
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索強化生成 (RAG) に関する概要ドキュメントの修正"
}
```

### Explanation
この変更は、検索強化生成（RAG）に関する概要を示すドキュメントの修正を示しています。主な目的は、利用者にとっての情報の明確さと関連性を向上させることです。

具体的には、顧客の意図を明示する追加情報が新たに組み込まれました。この情報では、ソリューションアーキテクトがエージェント的リトリーバルと従来のRAGを比較する目的が示されており、Azure AI Searchの選択肢を評価する際に役立つ内容となっています。

さらに、エージェント的リトリーバルの部分では、クエリ計画が「LLMベース」に変更され、現在はプレビュー段階であることを明示しています。これによりユーザーは、利用可能な技術の状態をより正確に把握できるようになります。また、クエリ計画に関する情報も「プレビュー」段階であることが明記されており、ユーザーに最新の情報を提供しています。

全体として、この変更はドキュメントが最新の情報を反映し、ユーザーがAzure AI Searchのさまざまなアプローチを理解しやすくすることに寄与しています。

## articles/search/samples-rest.md{#item-198ebc}

<details>
<summary>Diff</summary>
````diff
@@ -29,7 +29,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. T
 | [quickstart-keyword-search](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-keyword-search) | [Quickstart: Full-text search](search-get-started-text.md) | Create, load, and query a search index using sample data. |
 | [quickstart-semantic-ranking](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-semantic-ranking) | [Quickstart: Semantic ranking](search-get-started-semantic.md) | Add semantic ranking to an index schema and run semantic queries. |
 | [quickstart-vectors](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-vectors) | [Quickstart: Vector search](search-get-started-vector.md) | Index and query vector content. |
-| [acl](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/acl) | [Query-time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md) | Implement query-time access control using role-based access control (RBAC) and access control lists (ACLs). |
+| [acl](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/acl) | [Query-time ACL and RBAC enforcement (preview)](search-query-access-control-rbac-enforcement.md) | Implement query-time access control using role-based access control (RBAC) and access control lists (ACLs). |
 | [custom-analyzers](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/custom-analyzers) | [Tutorial: Create a custom analyzer for phone numbers](tutorial-create-custom-analyzer.md) | Use an analyzer to preserve patterns and special characters in searchable content. |
 | [debug-sessions](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/debug-sessions) | [Tutorial: Fix a skillset using Debug Sessions](cognitive-search-tutorial-debug-sessions.md) | Create search objects that you later debug in the Azure portal. |
 | [index-json-blobs](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/index-json-blobs) | [Tutorial: Index JSON blobs from Azure Storage](search-semi-structured-data.md) | Create an indexer, data source, and index for nested JSON within a JSON array. Demonstrates the jsonArray parsing model and documentRoot parameters. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIサンプルドキュメントの修正"
}
```

### Explanation
この変更は、Azure AI SearchのREST APIサンプルに関するドキュメントの修正を示しています。主な目標は、ユーザーが利用する際の情報を最新の状態に保つことです。

具体的には、アクセス制御リスト（ACL）とロールベースのアクセス制御（RBAC）を利用したクエリ時のアクセス制御に関連するリンクの説明が更新されました。変更前は「クエリ時のACLとRBACの実装」と記載されていましたが、変更後は「プレビュー版」と明記されています。この情報により、ユーザーはこの機能が現在プレビュー段階にあることを理解し、適切な利用を考慮できるようになります。

全体として、この修正はドキュメントが最新の技術的状況を反映し、Azure AI Searchの機能を使用する際の透明性と理解を高めることに寄与しています。

## articles/search/search-blob-indexer-role-based-access.md{#item-887e42}

<details>
<summary>Diff</summary>
````diff
@@ -10,24 +10,13 @@ ms.custom:
 ai-usage: ai-assisted
 ---
 
-# Use a blob indexer or knowledge source to ingest RBAC scopes metadata
+# Use a blob indexer or knowledge source to ingest RBAC scopes metadata (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
-
-Azure Storage allows for role-based access on containers in blob storage, where roles like **Storage Blob Data Reader** or **Storage Blob Data Contributor** determine whether someone has access to content. Preview APIs in Azure AI Search now support ingestion of user permissions alongside document ingestion so that you can use those permissions to control access to search results. If a user lacks permissions on a specific directory or file in Azure Storage, that user doesn't have access to the corresponding documents in Azure AI Search results, even if you personally have a **Search Index Data Reader** assignment *on the index*.
+Azure Storage allows for role-based access on containers in blob storage, where roles like **Storage Blob Data Reader** or **Storage Blob Data Contributor** determine whether someone has access to content. Azure AI Search supports ingestion of user permissions (preview) alongside document ingestion so that you can use those permissions to control access to search results. If a user lacks permissions on a specific directory or file in Azure Storage, that user doesn't have access to the corresponding documents in Azure AI Search results, even if you personally have a **Search Index Data Reader** assignment *on the index*.
 
 + 2025-05-01-preview and later, RBAC scopes metadata can be ingested using the [Blob indexer](search-how-to-index-azure-data-lake-storage.md).
 + 2025-11-01-preview and later provides equivalent support for [Blob knowledge sources](agentic-knowledge-source-how-to-blob.md) in Azure Storage.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACスコープメタデータの取り込みに関する文書の更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるRBAC（ロールベースアクセス制御）スコープメタデータの取り込みに関するドキュメントの更新を示しています。主な焦点は、ユーザーが使用する際の明確な情報提供と機能の最新状況の反映です。

変更の主な点として、RBACスコープメタデータの取り込みに関して「プレビュー版」であることが明記され、情報に強調が追加されました。また、2025-05-01-previewおよび2025-11-01-preview以降におけるBlobインデクサーとBlob知識ソースのサポートについての情報が追加されました。これにより、ユーザーは具体的なプレビューのバージョンに関連した機能の利用可能性を把握しやすくなっています。

文書内の一部情報が簡略化され、その内容も全体的にすっきりと整理されました。例えば、元々長かった注記がよりコンパクトになり、重要な情報がより明確に伝わるようになっています。

全体として、この修正はドキュメントが最新の技術的な内容を反映し、ユーザーがAzure AI SearchのRBAC機能を理解しやすくなることに寄与しています。

## articles/search/search-blob-metadata-properties.md{#item-2137f3}

<details>
<summary>Diff</summary>
````diff
@@ -60,4 +60,4 @@ The following table summarizes processing for each document format, and describe
 * [Indexers in Azure AI Search](search-indexer-overview.md)
 * [AI enrichment in Azure AI Search](cognitive-search-concept-intro.md)
 * [Search over Azure Blob Storage content](search-blob-storage-integration.md)
-* [Index data from SharePoint](search-how-to-index-sharepoint-online.md)
+* [Index data from SharePoint (preview)](search-how-to-index-sharepoint-online.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointインデクシングに関するプレビュー情報の追加"
}
```

### Explanation
この変更は、Azure AI SearchにおけるBlobメタデータプロパティに関するドキュメントの更新を示しています。特に、SharePointからデータをインデクシングする際の情報に「プレビュー版」という注記が追加された点が重要です。

修正内容は、SharePointに関連するインデクシングの項目が、もともと単に「Index data from SharePoint」と記載されていた部分から、「Index data from SharePoint (preview)」に変更されました。この変更により、ユーザーはこの機能が現在プレビュー段階にあり、利用に際しての注意が必要であることを認識しやすくなります。

全体として、この修正はユーザーに対して正確かつ最新の機能情報を提供し、Azure AI Searchを利用する際の透明性を高めることに寄与しています。

## articles/search/search-capacity-planning.md{#item-0dd6c9}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ Azure AI Search offers two pricing models that handle capacity differently:
     - Choose a service tier to provision the capacity needed based on expected peak demand.
     - Once you configure capacity upfront, you pay an hourly rate measured by Search Units (SUs), regardless of usage.
 
-- **Serverless (Preview)**: The service automatically manages capacity based on usage and service limits. You don't need to pre-provision capacity. Instead, optimize your workload efficiency to manage cost.
+- **Serverless (preview)**: The service automatically manages capacity based on usage and service limits. You don't need to pre-provision capacity. Instead, optimize your workload efficiency to manage cost.
     - Capacity automatically scales with demand (can scale to zero when idle).
     - You're billed based on actual usage as measured by Compute Units (CUs) and storage.
     - Rather than infrastructure, planning focuses on these cost drivers: Query patterns, Index size and growth, and Data ingestion patterns. See [Optimize cost for the Serverless model](#optimize-cost-for-the-serverless-model).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Serverlessプランのプレビュー情報の書式変更"
}
```

### Explanation
この変更は、Azure AI Searchのキャパシティプランニングに関するドキュメント内で、「Serverless」プランの説明部分の表記が修正されたことを示しています。具体的には、「Serverless (Preview)」から「Serverless (preview)」に表記が統一されました。

修正された箇所は、サーバーレスモデルに関する説明の中で、プレビューであることを示す「Preview」の頭文字が小文字に変更された点です。この表記の変更は、ドキュメント内での一貫性を保持するためのものと考えられます。

このわずかな修正ではありますが、全体的に見てドキュメントの整合性を保ち、ユーザーに対する情報の明瞭さを向上させることに寄与しています。

## articles/search/search-document-level-access-overview.md{#item-4bb055}

<details>
<summary>Diff</summary>
````diff
@@ -15,16 +15,7 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag occurs before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data flows outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This responsibility includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 Azure AI Search supports document-level access control, enabling organizations to enforce fine-grained permissions at the document level, from data ingestion through query execution. This capability is essential for building secure AI agentic systems grounding data, retrieval-augmented generation (RAG) applications, and enterprise search solutions that require authorization checks at the document level.
 
@@ -152,7 +143,7 @@ If the knowledge source points to a chunked index, such as one populated through
 
 For more information, see [Use Azure AI Search indexers to ingest Microsoft Purview sensitivity labels](search-indexer-sensitivity-labels.md).
 
-## Enforce document-level permissions at query time
+## Enforce document-level permissions at query time (preview)
 
 Token-based query enforcement is a cross-cutting capability that applies to the POSIX-like ACL and RBAC scopes, Microsoft Purview sensitivity labels, and SharePoint in Microsoft 365 ACLs patterns. By using [native token-based querying](search-query-access-control-rbac-enforcement.md), Azure AI Search validates the caller's [Microsoft Entra token](/entra/identity-platform/access-tokens) on each request and trims result sets to only the documents the caller is authorized to read according to the document ACLs, as long as the document ACL metadata is synchronized to the index.
 
@@ -180,17 +171,17 @@ Native document-level access control in Azure AI Search delivers concrete advant
 
 Explore document-level access control in Azure AI Search with more articles and samples.
 
-- [Tutorial: Index ADLS Gen2 permissions metadata using an indexer](tutorial-adls-gen2-indexer-acls.md)
+- [Tutorial: Index ADLS Gen2 permissions metadata using an indexer (preview)](tutorial-adls-gen2-indexer-acls.md)
 - [azure-search-rest-samples/acl](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/acl)
 - [azure-search-python-samples/Quickstart-Document-Permissions-Push-API](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Document-Permissions-Push-API)
 - [azure-search-python-samples/Quickstart-Document-Permissions-Pull-API](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Document-Permissions-Pull-API)
 - [Demo app: Ingesting and honoring sensitivity labels](https://aka.ms/Ignite25/aisearch-purview-sensitivity-labels-repo)
 
 ## Related content
 
-- [How to index document-level permissions using push API](search-index-access-control-lists-and-rbac-push-api.md)
-- [How to index document-level permissions using the ADLS Gen2 indexer](search-indexer-access-control-lists-and-role-based-access.md)
-- [How to index document-level permissions using the SharePoint in Microsoft 365 indexer](search-indexer-sharepoint-access-control-lists.md)
-- [How to index sensitivity labels using indexers](search-indexer-sensitivity-labels.md)
-- [How to query a sensitivity labels-enabled index](search-query-sensitivity-labels.md)
-- [How to query using Microsoft Entra token-based permissions](search-query-access-control-rbac-enforcement.md)
+- [How to index document-level permissions using push API (preview)](search-index-access-control-lists-and-rbac-push-api.md)
+- [How to index document-level permissions using the ADLS Gen2 indexer (preview)](search-indexer-access-control-lists-and-role-based-access.md)
+- [How to index document-level permissions using the SharePoint in Microsoft 365 indexer (preview)](search-indexer-sharepoint-access-control-lists.md)
+- [How to index sensitivity labels using indexers (preview)](search-indexer-sensitivity-labels.md)
+- [How to query a sensitivity labels-enabled index (preview)](search-query-sensitivity-labels.md)
+- [How to query using Microsoft Entra token-based permissions (preview)](search-query-access-control-rbac-enforcement.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレベルアクセスに関するプレビュー情報の追加"
}
```

### Explanation
この変更は、Azure AI Searchのドキュメントレベルアクセスに関する記事において、全体の構成や内容の一部に変更があったことを示しています。主に「プレビュー」に関連する情報が強調されており、いくつかのセクションに「(preview)」という表記が追加されています。

具体的には、マークダウン文書の重要性についてのセクションが削除され、新しいプレビューに関する条件や使用についての警告が「[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]」として統合されました。また、クエリ時のドキュメントレベル権限の強制に関する見出しにも「(preview)」の文言が追加されています。

さらに、いくつかのチュートリアルやサンプルへのリンクも更新され、「プレビュー」状態を反映した形となっています。こうした変更は、ユーザーに対して新しい機能がプレビュー段階であることを明確に示し、利用に際する注意点を強調するもので、情報の透明性を高めることに寄与しています。

## articles/search/search-faceted-navigation-examples.md{#item-2b1158}

<details>
<summary>Diff</summary>
````diff
@@ -5,15 +5,18 @@ ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 11/10/2025
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Faceted navigation examples
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
 This section extends [faceted navigation configuration](search-faceted-navigation.md) with examples that demonstrate basic usage and other scenarios.
 
-Facetable fields are defined in an index, but facet parameters and expressions are defined in query requests. If you have an index with facetable fields, you can try new preview features like [facet hierarchies](#facet-hierarchy-example), [facet aggregations](#facet-aggregation-example), and [facet filters](#facet-filtering-example) on existing indexes.
+Facetable fields are defined in an index, but facet parameters and expressions are defined in query requests. If you have an index with facetable fields, you can try [facet hierarchies (preview)](#facet-hierarchy-example-preview), [facet aggregations (preview)](#facet-aggregation-example-preview), and [facet filters (preview)](#facet-filtering-example-preview) on existing indexes.
 
 ## Facet parameters and syntax
 
@@ -195,9 +198,7 @@ Results from this query are as follows:
 }
 ```
 
-## Facet hierarchy example
-
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+## Facet hierarchy example (preview)
 
 Using the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) or the Azure portal, you can configure a facet hierarchy using the `>` and `;` operators.
 
@@ -475,9 +476,7 @@ Address/StateProvince
     Category
 ```
 
-## Facet filtering example
-
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+## Facet filtering example (preview)
 
 Using the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) or the Azure portal, you can configure facet filters.
 
@@ -488,7 +487,7 @@ Facet filtering enables you to constrain the facet values returned to those matc
 
 If a facet string satisfies both conditions, the `excludeTermFilter` takes precedence because the set of bucket strings is first evaluated with `includeTermFilter` and then excluded with `excludeTermFilter`.
 
-Only those facet values that match the regular expression are returned. You can combine these parameters with other facet options (for example, `count`, `sort`, and [hierarchical faceting](#facet-hierarchy-example)) on string fields.
+Only those facet values that match the regular expression are returned. You can combine these parameters with other facet options (for example, `count`, `sort`, and [hierarchical faceting](#facet-hierarchy-example-preview)) on string fields.
 
 Because the regular expression is nested within a JSON string value, you must escape both the double quote (`"`) and the backslash (`\`) characters. The regular expression itself is delimited by the forward slash (`/`). For more information about escape patterns, see [Regular expression search](query-lucene-syntax.md#bkmk_regex).
 
@@ -598,9 +597,7 @@ The following example is an abbreviated response (hotel documents are omitted fo
 }
 ```
 
-## Facet aggregation example
-
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+## Facet aggregation example (preview)
 
 Using the [latest preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) or the Azure portal, you can aggregate facets.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファセットナビゲーションのプレビュー情報の追加"
}
```

### Explanation
この変更は、Azure AI Searchにおけるファセットナビゲーションの使用例に関するドキュメントの更新を示しています。主な改訂は、プレビュー機能に関する明示的な言及を追加したことで、使用できる新しい機能をよりわかりやすく説明しています。

具体的には、「ファセット階層」や「ファセット集約」および「ファセットフィルタリング」といった機能の説明に「(preview)」という注記が加えられ、これらの機能がプレビュー段階にあることが明確に示されています。また、「[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]」が新たに加えられ、プレビュー機能に関連する使用条件が強調されています。

さらに、ファセットフィルタリングのセクション内でも、ファセット階層のリンク先に「(preview)」が追加されるなど、全体的に文書内での言及が一貫性を持って強化されています。これにより、ユーザーが新機能を試す際の注意点を明確にし、より効果的に利用できるように工夫されています。

## articles/search/search-faceted-navigation.md{#item-f29d1e}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 11/05/2025
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Add faceted navigation to search results
@@ -249,7 +250,7 @@ Remember that you can't use `Edm.GeographyPoint` or `Collection(Edm.GeographyPoi
 
 ### Check for bad data
 
-As you prepare data for indexing, check fields for null values, misspellings or case discrepancies, and single and plural versions of the same word. By default, filters and facets don't undergo lexical analysis or [spell check](speller-how-to-add.md), which means that all values of a "facetable" field are potential facets, even if the words differ by one character. 
+As you prepare data for indexing, check fields for null values, misspellings or case discrepancies, and single and plural versions of the same word. By default, filters and facets don't undergo lexical analysis or [spell check (preview)](speller-how-to-add.md), which means that all values of a "facetable" field are potential facets, even if the words differ by one character. 
 
 [Normalizers](search-normalizers.md) can mitigate data discrepancies, correcting for casing and character differences. Otherwise, to inspect your data, you can check fields at their source, or run queries that return values from the index.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スペルチェック機能のプレビュー情報の追加"
}
```

### Explanation
この変更は、Azure AI Searchにおけるファセットナビゲーションに関するドキュメントに対する更新を示しています。主な修正点は、スペルチェック機能に関する言及が「(preview)」という注記を伴って追加されたことです。

具体的には、データのインデックス準備においてフィールドを確認する際、「スペルチェック」がプレビュー機能であることを示すために、そのリンクに「(preview)」が付け加えられました。これにより、ユーザーに対してこの機能がまだ完全にはリリースされていないことが明示され、使用する際の注意が促されています。

新たに「ai-usage: ai-assisted」というメタデータも追加されており、AIの使用に関連した情報が強調されています。このような改訂は、ユーザーに対する情報の透明性を高め、Azure AI Searchの機能を効果的に活用するための助けとなります。

## articles/search/search-features-list.md{#item-d34448}

<details>
<summary>Diff</summary>
````diff
@@ -22,11 +22,11 @@ The following table summarizes features by category. There's feature parity in a
 | Category&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Features |
 |-------------------|----------|
 | Knowledge bases | [**Knowledge bases**](agentic-retrieval-how-to-create-knowledge-base.md) orchestrate the agentic retrieval pipeline, connecting to your LLM and managing query parameters. A knowledge base references one or more knowledge sources and defines the retrieval behavior. |
-| Knowledge sources | [**Knowledge sources**](agentic-knowledge-source-overview.md) specify the content used for agentic retrieval. Create knowledge sources from [search indexes](agentic-knowledge-source-how-to-search-index.md), [Azure Blob Storage](agentic-knowledge-source-how-to-blob.md), [OneLake](agentic-knowledge-source-how-to-onelake.md), [SharePoint (indexed)](agentic-knowledge-source-how-to-sharepoint-indexed.md), [SharePoint (remote)](agentic-knowledge-source-how-to-sharepoint-remote.md), or [web (Bing)](agentic-knowledge-source-how-to-web.md). |
-| Query planning | Query planning uses an LLM to analyze conversation context and break down complex questions into focused subqueries. This includes chat history processing, query decomposition, synonym expansion, and spelling correction. |
+| Knowledge sources | [**Knowledge sources**](agentic-knowledge-source-overview.md) define the content available to a knowledge base. An indexed knowledge source is backed by a search index, while a remote knowledge source retrieves content from an external platform at query time. |
+| Query planning (preview) | Query planning uses an LLM to analyze conversation context and break down complex questions into focused subqueries. This includes chat history processing, query decomposition, synonym expansion, and spelling correction. |
 | Parallel query execution | Subqueries run simultaneously across all knowledge sources. Each subquery supports keyword, vector, and hybrid search with automatic semantic reranking. |
-| Retrieval reasoning effort | [**Retrieval reasoning effort (preview)**](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) controls the level of LLM processing in the pipeline. Set to minimal for speed (no LLM), low for balanced processing, or medium for maximum relevance optimization. |
-| Response synthesis | Results are combined into a unified response with three parts: merged content for grounding data, source references for citations, and execution details showing the query plan. |
+| Retrieval reasoning effort (preview) | [**Retrieval reasoning effort**](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) controls the level of LLM processing in the pipeline so that you can balance retrieval depth and relevance against latency and LLM cost. |
+| Response output | The pipeline returns either extractive grounding content or, with answer synthesis (preview) enabled, an LLM-generated answer with citations. You can optionally include source references and execution details. |
 
 ## Indexing and data extraction
 
@@ -50,7 +50,7 @@ The following table summarizes features by category. There's feature parity in a
 | AI processing during indexing | [**AI enrichment**](cognitive-search-concept-intro.md) refers to embedded image and natural language processing in an indexer pipeline that extracts text and information from content that can't otherwise be indexed for full text search. AI processing is achieved by adding and combining skills in a skillset, which is then attached to an indexer. AI can be either [built-in skills](cognitive-search-predefined-skills.md) from Microsoft, such as text translation or Optical Character Recognition (OCR), or [custom skills](cognitive-search-create-custom-skill-example.md) that you provide. </p>[**Integrated data chunking and vectorization**](vector-search-integrated-vectorization.md) splits up larger passages into smaller chunks that can be vectorized, with vectors routed to dedicated fields in an index for vector and hybrid search.|
 | AI processing during query execution | [**Vectorizers**](vector-search-how-to-configure-vectorizer.md) are used to encode user query strings into vectors for vector search. You can use the same embedding models for queries that you used for indexing. </p>|
 | Storing enriched content for analysis and consumption in non-search scenarios | [**Knowledge store**](knowledge-store-concept-intro.md) is persistent storage of AI enriched or AI generated content, intended for non-search scenarios like knowledge mining and data science workloads. A knowledge store is defined in a skillset, but created in Azure Storage as objects or tabular rowsets.|
-| Cached enrichments | [**Enrichment caching (preview)**](enrichment-cache-how-to-configure.md) refers to cached enrichments that can be reused during skillset execution. Caching is valuable in skillsets that include OCR and image analysis, which are expensive to process. |
+| Cached enrichments (preview) | [**Enrichment caching**](enrichment-cache-how-to-configure.md) refers to cached enrichments that can be reused during skillset execution. Caching is valuable in skillsets that include OCR and image analysis, which are expensive to process. |
 
 ## Vector and hybrid retrieval
 
@@ -61,7 +61,7 @@ The following table summarizes features by category. There's feature parity in a
 | Vector search algorithms | Use [Hierarchical Navigable Small World (HNSW)](vector-search-ranking.md#about-hnsw) or [exhaustive K-Nearest Neighbors (KNN)](vector-search-ranking.md#about-exhaustive-knn) to find similar vectors in a search index. |
 | Vector filters | [Apply filters before or after query execution](vector-search-filters.md) for greater precision during information retrieval. |
 | Hybrid information retrieval | Search for concepts and keywords in a single [hybrid query request](hybrid-search-how-to-query.md). </p>[**Hybrid search**](hybrid-search-overview.md) consolidates vector and text search, with optional semantic ranking and relevance tuning for best results.|
-| Integrated data chunking and vectorization | Native data chunking through [Text Split skill](cognitive-search-skill-textsplit.md). Native vectorization through [vectorizers](vector-search-how-to-configure-vectorizer.md) and embedding skills such as [Azure OpenAI Embedding](cognitive-search-skill-azure-openai-embedding.md), [Azure Vision multimodal](cognitive-search-skill-vision-vectorize.md), and [AML](cognitive-search-aml-skill.md) that you can use to connect to endpoints in the Microsoft Foundry model catalog. </p>[**Integrated vectorization**](vector-search-integrated-vectorization.md) provides an end-to-end indexing pipeline from source files to queries.|
+| Integrated data chunking and vectorization | Native data chunking through [Text Split skill](cognitive-search-skill-textsplit.md). Native vectorization through [vectorizers](vector-search-how-to-configure-vectorizer.md) and embedding skills such as [Azure OpenAI Embedding](cognitive-search-skill-azure-openai-embedding.md), [Azure Vision multimodal (preview)](cognitive-search-skill-vision-vectorize.md), and [AML](cognitive-search-aml-skill.md) that you can use to connect to endpoints in the Microsoft Foundry model catalog. </p>[**Integrated vectorization**](vector-search-integrated-vectorization.md) provides an end-to-end indexing pipeline from source files to queries.|
 | Integrated vector compression and quantization | Use [built-in scalar and binary quantization](vector-search-how-to-quantization.md) to reduce vector index size in memory and on disk. You can also forego storage of vectors you don't need, or assign narrow data types to vector fields for reduced storage requirements. |
 
 ## Classic full text and other query forms
@@ -80,7 +80,7 @@ The following table summarizes features by category. There's feature parity in a
 |-------------------|----------|
 | Network security | [**IP rules for inbound firewall support**](service-configure-firewall.md) allows you to set up IP ranges over which the search service accepts requests. </br></br>[**Create a private endpoint**](service-create-private-endpoint.md) using Azure Private Link to force all requests through a virtual network. </br></br>[**Network security perimeter**](search-security-network-security-perimeter.md) support allows you to join Azure AI Search to a network security perimeter that includes other Azure resources so that you can manage network access holistically. |
 | Data encryption | [**Microsoft-managed encryption-at-rest**](search-security-built-in.md#data-encryption) is built into the internal storage layer and is irrevocable. </br></br>[**Customer-managed encryption keys (CMK)**](search-security-manage-encryption-keys.md) that you create and manage in Azure Key Vault can be used for supplemental encryption of indexes and synonym maps. For services created after August 1 2020, CMK encryption extends to data on temporary disks, for full double encryption of indexed content.|
-| Inbound access | [**Role-based access control**](search-security-rbac.md) assigns roles to users and groups in Microsoft Entra ID for controlled access to search content and operations. You can also use [**key-based authentication**](search-security-api-keys.md) if you don't want to use role assignments. </br></br>[**Document-level access control (preview)**](search-document-level-access-overview.md) filters out search results that a user isn't authorized to see. For several data sources, if the data source provides an access control model, you can configure an index to inherit the user permission metadata. |
+| Inbound access | [**Role-based access control**](search-security-rbac.md) assigns roles to users and groups in Microsoft Entra ID for controlled access to search content and operations. You can also use [**key-based authentication**](search-security-api-keys.md) if you don't want to use role assignments. </br></br>[**Document-level access control**](search-document-level-access-overview.md) filters out search results that a user isn't authorized to see. For several data sources, if the data source provides an access control model, you can configure an index to inherit the user permission metadata. |
 | Outbound security (indexers) | [**Data connections through private endpoints**](search-indexer-howto-access-private.md) allows an indexer to connect to Azure resources that are protected through Azure Private Link. </br></br>[**Data connections through managed identities**](search-how-to-managed-identities.md) authenticates connections to Azure resources using a Microsoft Entra security principal, which eliminates storage and passing of hardcoded API keys.</br></br>[**Data access using a trusted identity**](search-how-to-managed-identities.md) means that connection strings to external data sources can omit user names and passwords. When an indexer connects to the data source, the resource allows the connection if the search service was previously registered as a trusted service (applies to Azure Storage only). |
 
 ## Portal features
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファーチャーリストの修正とプレビュー機能の追加"
}
```

### Explanation
この変更は、Azure AI Searchの機能リストに関するドキュメントの更新を示しています。主な内容は、一部の機能の説明が明確化され、さらにいくつかの機能に「(preview)」というタグが追加されたことです。

具体的には、「Knowledge sources」のセクションが改訂され、知識ベースに利用可能なコンテンツの定義が明確になりました。また、「Query planning」と「Retrieval reasoning effort」もプレビュー機能として位置付けられ、これらが現在試験的な段階であることが強調されています。

さらに、「Response output」など新しい項目が追加され、パイプラインが返すことができるコンテンツについての情報が詳細に説明されています。このような改訂により、ユーザーは新機能の使用方法やその進行状況についてより理解を深めることができ、より効果的にAzure AI Searchの機能を活用することが可能になります。

## articles/search/search-file-storage-integration.md{#item-d20e26}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.custom: [ignite-2023, ignite-2024, sfi-ropc-nochange, doc-kit-assisted]
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 > [!IMPORTANT]
 > These features and functionality support connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
@@ -23,7 +23,7 @@ ms.custom: [ignite-2023, ignite-2024, sfi-ropc-nochange, doc-kit-assisted]
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-In this article, learn how to configure an [**indexer**](search-indexer-overview.md) that imports content from Azure Files and makes it searchable in Azure AI Search. Inputs to the indexer are your files in a single share. Output is a search index with searchable content and metadata stored in individual fields.
+The *Azure Files indexer* (preview) imports content from a file share into an Azure AI Search index. Inputs to the indexer are your files in a single share. Output is a search index with searchable content and metadata stored in individual fields.
 
 To configure and run the indexer, you can use:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビュー用インクルードの更新とインデクサーの説明修正"
}
```

### Explanation
この変更は、Azure AI Searchにおけるファイルストレージ統合に関連するドキュメントの更新を示しています。主な修正は、プレビュー情報のインクルードが「`preview-terms`」に更新されたことと、Azure Filesインデクサーの説明が明確になったことです。

具体的には、ファイル共有からコンテンツをインポートするインデクサーの機能が強調され、'Azure Files indexer (preview)'という表現が追加され、現在機能が試験的であることが示されています。これにより、ユーザーはこの機能がまだ完全に安定したものではないことを理解し、使用時の注意が促されます。

また、インデクサーの入力と出力に関する説明が整理され、インポートされるファイルや、その結果として生成される検索インデックスに関する情報が明確に示されています。この更新は、Azure AI Searchを利用する際に、ユーザーがより適切に機能を理解し活用するための情報を提供します。

## articles/search/search-get-started-agentic-retrieval.md{#item-4a40f4}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
 title: "Quickstart: Agentic Retrieval"
-description: Learn how to use agentic retrieval to create a knowledge base that processes multi-turn conversations.
+description: Learn how to use preview agentic retrieval features to create a knowledge base that processes multi-turn conversations and synthesizes answers.
 author: mattwojo
 ms.author: mattwoj
 ms.service: azure-ai-search
@@ -9,13 +9,15 @@ ms.date: 07/20/2026
 ms.custom: dev-focus
 ai-usage: ai-assisted
 zone_pivot_groups: search-sdks-rest
-# Customer intent: I want to learn how to use agentic retrieval to create a knowledge base that processes multi-turn conversations. The knowledge base should retrieve relevant information from a knowledge source that points to an Azure AI Search index and use an Azure OpenAI LLM to synthesize answers.
+#customer intent: As an application developer, I want to use an Azure SDK or REST API to create a search index knowledge source and knowledge base and run a retrieval query so that my application can produce grounded, citation-backed answers.
 ---
 
 # Quickstart: Agentic retrieval
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
 ::: zone pivot="csharp"
 [!INCLUDE [C#](includes/quickstarts/agentic-retrieval-csharp.md)]
 ::: zone-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバルのクイックスタート説明の改善"
}
```

### Explanation
この変更は、エージェンティックリトリーバルに関するクイックスタートガイドの説明を更新したものです。具体的には、プレビュー機能について言及し、知識ベースの作成や回答の合成に関する情報が追加されています。

変更点の一つは、ドキュメントの紹介文が改訂され、「プレビューのエージェンティックリトリーバル機能を使用して、マルチターンの会話を処理し、回答を合成する知識ベースを作成する方法を学びます」との具体的な内容が追加されました。これにより、ユーザーはこの機能の試験的な性質を理解し、今後の利用についての期待を持つことが可能です。

また、顧客の意図についての記述が改訂され、アプリケーション開発者としての視点から、Azure SDKまたはREST APIを使用して検索インデックスの知識ソースを作成し、検索クエリを実行する目的が明確に示されています。この変更は、ユーザーがより適切に機能を活用し、具体的な実装方法を学ぶ手助けとなる情報を提供します。

## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -1,4 +1,4 @@
-﻿---
+---
 title: "Quickstart: Multimodal Search in the Azure portal"
 description: Learn how to index and search for multimodal content in the Azure portal. Run a wizard to extract and embed both text and images, and then use Search Explorer to query your multimodal index.
 author: mattwojo
@@ -62,9 +62,9 @@ The portal supports the following models for each method. Deployment instruction
 | [Microsoft Foundry project](/azure/foundry/how-to/create-projects?pivots=web-portal&preserve-view=true) | LLMs:<ul><li>phi-4</li><li>gpt-4o</li><li>gpt-4o-mini</li><li>gpt-5</li><li>gpt-5-mini</li><li>gpt-5-nano</li></ul>Embedding models:<ul><li>text-embedding-ada-002</li><li>text-embedding-3-small</li><li>text-embedding-3-large</li></ul> | |
 | [Azure OpenAI resource](/azure/foundry-classic/openai/how-to/create-resource?pivots=web-portal) <sup>3, 4</sup> | LLMs:<ul><li>gpt-4o</li><li>gpt-4o-mini</li><li>gpt-5</li><li>gpt-5-mini</li><li>gpt-5-nano</li></ul>Embedding models:<ul><li>text-embedding-ada-002</li><li>text-embedding-3-small</li><li>text-embedding-3-large</li></ul> | |
 
-<sup>1</sup> For billing purposes, you must [attach your multi-service account](cognitive-search-attach-cognitive-services.md) to your Azure AI Search skillset. The wizard requires your search service and multi-service account to be in the [same supported region for the Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md#supported-regions).
+<sup>1</sup> For billing purposes, you must [attach your multi-service account](cognitive-search-attach-cognitive-services.md) to your Azure AI Search skillset. The wizard requires your search service and multi-service account to be in the [same supported region for the Azure Vision multimodal embeddings skill (preview)](cognitive-search-skill-vision-vectorize.md#supported-regions).
 
-<sup>2</sup> The wizard only supports serverless API deployments for this model. You can use [use the Azure CLI](vector-search-integrated-vectorization-ai-studio.md#deploy-an-embedding-model-as-a-serverless-deployment) to provision the serverless deployment.
+<sup>2</sup> The wizard only supports serverless API deployments for this model. You can use [use the Azure CLI](vector-search-integrated-vectorization-ai-studio.md#deploy-an-embedding-model-as-a-serverless-deployment) to provision the serverless deployment (preview).
 
 <sup>3</sup> The endpoint of your Azure OpenAI resource must have a [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains), such as `https://my-unique-name.openai.azure.com`. If you created your resource in the Azure portal, this subdomain was automatically generated during resource setup.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureポータルにおけるマルチモーダル検索のクイックスタートの更新"
}
```

### Explanation
この変更は、「Azureポータルにおけるマルチモーダル検索」のクイックスタートガイドの内容を更新したものです。主に、プレビュー機能に関する項目が明確化されました。

具体的には、知識をエンベッドするためのウィザードにおいて「Azure Visionのマルチモーダルエンベディングスキル（プレビュー）」が明示されました。これにより、ユーザーはこの機能がまだ開発中であることを理解でき、使用時の注意点を認識することができます。

また、ウィザードに関する説明でも、サーバーレスAPIデプロイメントがプレビューに関連付けられ、一時的な機能の性質が強調されています。これにより、開発者は機能の利用方法や適用範囲についての理解を深めることができるでしょう。全体として、この更新はユーザーに最新の情報を提供し、マルチモーダルコンテンツのインデックスと検索を行う際のガイダンスを強化するものとなっています。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -1,4 +1,4 @@
-﻿---
+---
 title: "Quickstart: Vector Search in the Azure portal"
 description: Learn how to use a wizard to automate data chunking and vectorization in a search index.
 author: mattwojo
@@ -56,9 +56,9 @@ The portal supports the following embedding models for integrated vectorization.
 | [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) | For text:<ul><li>text-embedding-ada-002</li><li>text-embedding-3-small</li><li>text-embedding-3-large</li></ul> |
 | [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource) <sup>3, 4</sup> | For text:<ul><li>text-embedding-ada-002</li><li>text-embedding-3-small</li><li>text-embedding-3-large</li></ul> |
 
-<sup>1</sup> For billing purposes, you must [attach your multi-service account](cognitive-search-attach-cognitive-services.md) to your Azure AI Search skillset. The wizard requires your search service and multi-service account to be in the [same supported region for the Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md#supported-regions).
+<sup>1</sup> For billing purposes, you must [attach your multi-service account](cognitive-search-attach-cognitive-services.md) to your Azure AI Search skillset. The wizard requires your search service and multi-service account to be in the [same supported region for the Azure Vision multimodal embeddings skill (preview)](cognitive-search-skill-vision-vectorize.md#supported-regions).
 
-<sup>2</sup> The wizard only supports serverless API deployments for this model. You can use [use the Azure CLI](vector-search-integrated-vectorization-ai-studio.md#deploy-an-embedding-model-as-a-serverless-deployment) to provision the serverless deployment.
+<sup>2</sup> The wizard only supports serverless API deployments for this model. You can use [use the Azure CLI](vector-search-integrated-vectorization-ai-studio.md#deploy-an-embedding-model-as-a-serverless-deployment) to provision the serverless deployment (preview).
 
 <sup>3</sup> The endpoint of your Azure OpenAI resource must have a [custom subdomain](/azure/ai-services/cognitive-services-custom-subdomains), such as `https://my-unique-name.openai.azure.com`. If you created your resource in the Azure portal, this subdomain was automatically generated during resource setup.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureポータルにおけるベクター検索のクイックスタートの更新"
}
```

### Explanation
この変更は、「Azureポータルにおけるベクター検索」のクイックスタートガイドを更新する内容です。主に、ウィザードの機能に関する情報が強化され、プレビュー機能についての言及が追加されました。

具体的には、ウィザードが「Azure Visionのマルチモーダルエンベディングスキル（プレビュー）」に関連することが明示されています。これにより、ユーザーはこの機能が開発中であり、今後の使用に際して注意が必要であることを理解できるようになります。

さらに、ウィザードに関する説明では、サーバーレスAPIデプロイメントがプレビューとして示されており、ユーザーがこれを利用する際の環境や設定についての理解が深まります。全体として、この更新は、使用者がデータのチャンク化とベクター化を自動化する方法をより効果的に学ぶための情報を提供することを意図しています。

## articles/search/search-get-started-semantic.md{#item-2b3902}

<details>
<summary>Diff</summary>
````diff
@@ -64,5 +64,5 @@ In this quickstart, you add semantic ranking to an existing Azure AI Search inde
 
 + [Semantic ranking in Azure AI Search](semantic-search-overview.md)
 + [Configure semantic ranker](semantic-how-to-configure.md)
-+ [Add query rewrite to semantic ranker](semantic-how-to-query-rewrite.md)
++ [Add query rewrite to semantic ranker (preview)](semantic-how-to-query-rewrite.md)
 + [Use scoring profiles with semantic ranker](semantic-how-to-enable-scoring-profiles.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおけるセマンティックランキングのクイックスタートの更新"
}
```

### Explanation
この変更は、「Azure AI Searchにおけるセマンティックランキング」のクイックスタートガイドの内容を更新したものです。具体的には、クイックスタートに関するリンクの一部が修正されています。

主な変更点として、「セマンティックランキングのクイックスタート」ガイドのリンクに「(プレビュー)」という文言が追加され、ユーザーに現在の機能がまだ開発中であることを明示しています。これにより、利用者はこの機能を使用する際の注意点を理解しやすくなります。

全体として、この更新はユーザーに対して最新の状況を反映し、セマンティックランキングに関連する機能の利用についての明確なガイダンスを提供することを目的としています。

## articles/search/search-how-to-create-indexers.md{#item-de71fb}

<details>
<summary>Diff</summary>
````diff
@@ -8,6 +8,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
   - sfi-ropc-nochange
+ai-usage: ai-assisted
 ---
 
 # Create an indexer in Azure AI Search
@@ -104,7 +105,7 @@ Skills-based indexing uses [AI enrichment](cognitive-search-concept-intro.md) to
 }
 ```
 
-AI enrichment is its own subject area and is out of scope for this article. For more information, start with [AI enrichment](cognitive-search-concept-intro.md), [Skillsets in Azure AI Search](cognitive-search-working-with-skillsets.md), [Create a skillset](cognitive-search-defining-skillset.md), [Map enriched output fields](cognitive-search-output-field-mapping.md), and [Enable caching for AI enrichment](enrichment-cache-how-to-configure.md).
+AI enrichment is its own subject area and is out of scope for this article. For more information, start with [AI enrichment](cognitive-search-concept-intro.md), [Skillsets in Azure AI Search](cognitive-search-working-with-skillsets.md), [Create a skillset](cognitive-search-defining-skillset.md), [Map enriched output fields](cognitive-search-output-field-mapping.md), and [Enable caching for AI enrichment (preview)](enrichment-cache-how-to-configure.md).
 
 ## Prepare external data
 
@@ -245,10 +246,10 @@ Change detection logic is built into the data platforms. How an indexer supports
 + Cloud database services provide optional change detection features. For these data sources, change detection isn't automatic. You need to specify in the data source definition which policy is used:
 
   + [Azure SQL (change detection)](search-how-to-index-sql-database.md#indexing-new-changed-and-deleted-rows)
-  + [Azure Database for MySQL (change detection)](search-how-to-index-mysql.md#indexing-new-and-changed-rows)
+  + [Azure Database for MySQL (change detection) (preview)](search-how-to-index-mysql.md#indexing-new-and-changed-rows)
   + [Azure Cosmos DB for NoSQL (change detection)](search-how-to-index-cosmosdb-sql.md#indexing-new-and-changed-documents)
-  + [Azure Cosmos DB for MongoDB (change detection)](search-how-to-index-cosmosdb-mongodb.md#indexing-new-and-changed-documents)
-  + [Azure Cosmos DB for Apache Gremlin (change detection)](search-how-to-index-cosmosdb-gremlin.md#indexing-new-and-changed-documents)
+  + [Azure Cosmos DB for MongoDB (change detection) (preview)](search-how-to-index-cosmosdb-mongodb.md#indexing-new-and-changed-documents)
+  + [Azure Cosmos DB for Apache Gremlin (change detection) (preview)](search-how-to-index-cosmosdb-gremlin.md#indexing-new-and-changed-documents)
 
 Indexers keep track of the last document they processed from the data source through an internal *high water mark*. The marker is never exposed in the API, but internally the indexer tracks where it stopped. When indexing resumes, either through a scheduled run or an on-demand invocation, the indexer references the high water mark so that it can pick up where it left off.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのインデクサー作成に関する記事の更新"
}
```

### Explanation
この変更は、「Azure AI Searchのインデクサー作成」に関するガイドラインを一部更新したものです。主な更新内容は、AI拡張機能に関連する情報がプレビューに関する記述を含むようになった点です。

具体的には、AI拡張機能のキャッシングに関するリンクと、Azure Database for MySQLおよびAzure Cosmos DBの変更検出に関するリンクに「(プレビュー)」という表記が追加されました。これにより、利用者はこれらの機能がまだ最終的な状態にないことを理解でき、注意を促されます。

また、新たに「ai-usage: ai-assisted」というメタデータが追加され、記事の内容がAIを活用した支援に関連していることが示されています。全体として、この更新は、ユーザーにとって関連する機能の最新情報を提供し、正確な実装を促進することを目的としています。

## articles/search/search-how-to-define-index-projections.md{#item-a7e2c5}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.custom:
 ms.topic: how-to
 ms.date: 07/28/2026
 ms.update-cycle: 180-days
+ai-usage: ai-assisted
 ---
 
 # Define an index projection for parent-child indexing
@@ -162,7 +163,7 @@ Index projections are generally available. We recommend the most recent stable A
 
 Here's an example payload for an index projections definition that you might use to project individual pages output by the [Text Split skill](cognitive-search-skill-textsplit.md) as their own documents in the search index.
 
-If the parent document carries permission metadata for document-level access, such as `metadata_user_ids`, `metadata_group_ids`, or `metadata_spo_site_url`, include those fields in `mappings`. Every chunk must inherit them for query-time permission filters to apply. For more information, see [Choose where to populate ACL fields](search-indexer-sharepoint-access-control-lists.md#choose-where-to-populate-acl-fields).
+If the parent document carries permission metadata for document-level access, such as `metadata_user_ids`, `metadata_group_ids`, or `metadata_spo_site_url`, include those fields in `mappings`. Every chunk must inherit them for query-time permission filters to apply. For more information, see [Choose where to populate ACL fields (preview)](search-indexer-sharepoint-access-control-lists.md#choose-where-to-populate-acl-fields).
 
 ```json
 "indexProjections": {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "親子インデクシングのためのインデックス投影の定義に関する記事の更新"
}
```

### Explanation
この変更は、「親子インデクシングのためのインデックス投影の定義」に関するガイドを更新したもので、主にメタデータとリンクの修正が含まれています。

具体的には、新たに「ai-usage: ai-assisted」というメタデータが追加され、記事の内容がAIを活用する方法に関連していることが強調されています。また、親ドキュメントが文書レベルでのアクセスのための権限メタデータを保持している場合に関する説明が、リンクの文言を「(プレビュー)」とする形で更新されています。この変更は、読者に対してその機能が現在も開発中であることを知らせ、注意を促すものです。

全体として、この更新はユーザーに最新の情報を提供し、正確な実装を支援することを目的としています。

## articles/search/search-how-to-delete-documents.md{#item-556879}

<details>
<summary>Diff</summary>
````diff
@@ -55,7 +55,7 @@ The following links provide more information about change and deletion detection
 + [Azure SQL](search-how-to-index-sql-database.md#indexing-new-changed-and-deleted-rows)
 + [Azure Cosmos DB](search-how-to-index-cosmosdb-sql.md#indexing-deleted-documents)
 + [Azure Database for MySQL (preview)](search-how-to-index-mysql.md#indexing-deleted-rows)
-+ [SharePoint indexer](search-how-to-index-sharepoint-online.md)
++ [SharePoint indexer (preview)](search-how-to-index-sharepoint-online.md)
 + [OneLake indexer](search-how-to-index-onelake-files.md#supported-tasks)
 
 ## Identify specific documents for deletion
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書削除に関する記事の更新"
}
```

### Explanation
この変更は、「文書削除」に関するガイドを更新し、主にリンクの表記を修正したものです。具体的には、SharePointインデクサーに関連するリンクの文言が「(プレビュー)」という表記に変更されました。

これにより、使用者はSharePointインデクサーの機能が現在も開発中であることを理解できるようになりました。その他のリンクに関しては、更新は行われていないため、処理や削除の検出に関する情報は引き続き提供されています。

全体として、この更新はユーザーに最新の状況を示し、機能が最終的な状態でないことを周知させることを目的としています。

## articles/search/search-how-to-index-azure-blob-csv.md{#item-185bfc}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-**Applies to**: [Blob storage indexers](search-how-to-index-azure-blob-storage.md), [Files indexers](search-file-storage-integration.md)
+**Applies to**: [Blob storage indexers](search-how-to-index-azure-blob-storage.md), [Files indexers (preview)](search-file-storage-integration.md)
 
 In Azure AI Search, indexers for Azure Blob Storage and Azure Files support a `delimitedText` parsing mode for CSV files that treats each line in the CSV as a separate search document. For example, given the following comma-delimited text, the `delimitedText` parsing mode would result in two documents in the search index: 
 
@@ -100,4 +100,4 @@ api-key: [admin key]
 ## Related content
 
 + [Index data from Azure Blob Storage](search-how-to-index-azure-blob-storage.md)
-+ [Index data from Azure Files](search-file-storage-integration.md)
++ [Index data from Azure Files (preview)](search-file-storage-integration.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Blob CSVのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、「Azure Blob CSVのインデックス作成」に関するガイドを更新し、主に関連リンクの表記を修正したものです。具体的には、「Files indexers」や「Index data from Azure Files」というリンクの表記が「(プレビュー)」という形に変更されました。

この更新により、ユーザーはこれらの機能が現在も開発段階であることを理解し、利用時に注意が必要であることが伝えられます。また、Blobストレージに関するリンクはそのまま維持されており、変更がないことが示されています。

このような修正は、最新の情報を提供し、ユーザーが機能の状況を正確に把握できるようになることを目的としています。全体として、ガイドの信頼性と透明性を向上させる内容となっています。

## articles/search/search-how-to-index-azure-blob-json.md{#item-8133fe}

<details>
<summary>Diff</summary>
````diff
@@ -7,13 +7,14 @@ ms.custom:
 ms.topic: how-to
 ms.date: 09/18/2025
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Index JSON blobs and files in Azure AI Search
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-**Applies to**: [Blob indexers](search-how-to-index-azure-blob-storage.md), [File indexers](search-file-storage-integration.md)
+**Applies to**: [Blob indexers](search-how-to-index-azure-blob-storage.md), [File indexers (preview)](search-file-storage-integration.md)
 
 For blob indexing in Azure AI Search, this article shows you how to set properties for blobs or files consisting of JSON documents. JSON files in Azure Blob Storage or Azure Files commonly assume any of these forms:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Blob JSONのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、「Azure Blob JSONのインデックス作成」に関するガイドに対して行われた軽微な更新です。主な内容としては、ファイルインデクサーに関するリンクの表記が「(プレビュー)」に修正され、新たに「ai-usage: ai-assisted」というメタ情報が追加されました。

これにより、ユーザーはファイルインデクサー機能が開発中であることを把握でき、利用時の注意喚起がなされることになります。また、AI支援出機能を利用することが強調されています。

この更新は、記事の可用性と透明性を向上させ、ユーザーに対して最新の情報を提供することを目的としています。全体として、Azure AI SearchにおけるJSONファイルのインデックス作成に関する信頼性が高まる内容です。

## articles/search/search-how-to-index-azure-blob-markdown.md{#item-c35bd7}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ In Azure AI Search, indexers for Azure Blob Storage, Azure Files, and Microsoft
 
   For OneLake, make sure you meet all of the requirements of the [OneLake indexer](search-how-to-index-onelake-files.md#prerequisites).
 
-  Azure Storage for [blob indexers](search-how-to-index-azure-blob-storage.md#prerequisites) and [file indexers](search-file-storage-integration.md#prerequisites) is a standard performance (general-purpose v2) instance that supports hot and cool access tiers.
+  Azure Storage for [blob indexers](search-how-to-index-azure-blob-storage.md#prerequisites) and [file indexers (preview)](search-file-storage-integration.md#prerequisites) is a standard performance (general-purpose v2) instance that supports hot and cool access tiers.
 
 ## Markdown parsing mode parameters
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Blob Markdownのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、「Azure Blob Markdownのインデックス作成」に関するガイドの一部を更新したものです。具体的には、ファイルインデクサーに関するリンクの表記を修正し、「(プレビュー)」という注釈を追加しました。この修正により、ユーザーはファイルインデクサーが現在開発中であることを理解し、利用時に注意を払う必要があることが明示されます。

また、ブロブインデクサーに関するリンクは変更されておらず、引き続き参照可能です。これにより、情報の信頼性が維持されつつ、新たに追加された注意喚起がユーザーに対して明確に伝えられることになります。

全体として、この更新はAzure AI Searchに関する情報の透明性とユーザーへの指導を強化するためのものです。

## articles/search/search-how-to-index-azure-blob-one-to-many.md{#item-30a1f9}

<details>
<summary>Diff</summary>
````diff
@@ -8,13 +8,14 @@ ms.custom:
 ms.topic: concept-article
 ms.date: 01/14/2026
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Indexing blobs and files to produce multiple search documents
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-**Applies to**: [Blob indexers](search-how-to-index-azure-blob-storage.md), [File indexers](search-file-storage-integration.md)
+**Applies to**: [Blob indexers](search-how-to-index-azure-blob-storage.md), [File indexers (preview)](search-file-storage-integration.md)
 
 By default, an indexer treats the contents of a blob or file as a single search document. If you want a more granular representation in a search index, you can set **parsingMode** values to create multiple search documents from one blob or file. The **parsingMode** values that result in many search documents include `delimitedText` (for [CSV](search-how-to-index-azure-blob-csv.md)), `jsonArray` or `jsonLines` (for [JSON](search-how-to-index-azure-blob-json.md)), or `markdown` with sub-mode `oneToMany` for [markdown](search-how-to-index-azure-blob-markdown.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Blob One to Manyのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、「Azure Blob One to Manyのインデックス作成」に関するガイドの記事における軽微な更新を示しています。主な変更点は、ファイルインデクサーに関するリンクに「(プレビュー)」という注釈を追加し、記事に新たに「ai-usage: ai-assisted」というメタ情報を加えたことです。

これにより、ユーザーはファイルインデクサー機能が開発中であることを知ることができ、注意を払う必要があることが強調されます。また、AIの支援を受ける機能に関する情報も提供され、利用時の選択肢が増えます。

全体として、この更新はAzure AI Searchにおけるインデックス作成プロセスについて、より詳細かつ最新の情報をユーザーに提供することを目的としています。これにより、ドキュメントの信頼性が向上し、ユーザー体験が向上することが期待されます。

## articles/search/search-how-to-index-azure-blob-plaintext.md{#item-1d543c}

<details>
<summary>Diff</summary>
````diff
@@ -7,13 +7,14 @@ ms.custom:
 ms.topic: how-to
 ms.date: 03/25/2026
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Index plain text blobs and files in Azure AI Search
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-**Applies to**: [Blob indexers](search-how-to-index-azure-blob-storage.md), [File indexers](search-file-storage-integration.md)
+**Applies to**: [Blob indexers](search-how-to-index-azure-blob-storage.md), [File indexers (preview)](search-file-storage-integration.md)
 
 When using an indexer to extract searchable blob text or file content for full text search, you can assign a parsing mode to get better indexing outcomes. By default, the indexer parses a blob's `content` property as a single chunk of text. However, if all blobs and files contain plain text in the same encoding, you can significantly improve indexing performance by using the `text` parsing mode.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Blob Plaintextのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、「Azure Blob Plaintextのインデックス作成」に関するガイドの記事に対する軽微な更新を示しています。主な変更点は、ファイルインデクサーに「(プレビュー)」という注釈を追加し、さらに「ai-usage: ai-assisted」というメタ情報を新たに追加したことです。

これにより、ユーザーはファイルインデクサーの機能がまだ開発中であることを認識し、注意が必要であることが伝えられます。また、AIに支援される機能の情報が明記されることで、より良いインデックス作成のための選択肢が提供されます。

記事の内容自体は、平文テキストのインデックス作成に関する手法とパフォーマンスの向上について説明しており、ユーザーが特定のパースモードを使用することでインデックス作成の結果を改善できることを強調しています。この更新は、Azure AI Searchにおける情報の透明性と最新性を高めることを目的としています。

## articles/search/search-how-to-index-azure-blob-storage.md{#item-353b6b}

<details>
<summary>Diff</summary>
````diff
@@ -26,15 +26,15 @@ ms.custom:
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-In this article, you learn how to configure an [indexer](search-indexer-overview.md) that imports content from Azure Blob Storage and makes it searchable in Azure AI Search. The indexer receives blobs in a single container as input. The output is a search index that stores searchable content and metadata in individual fields.
+The *blob indexer* imports content from Azure Blob Storage and makes it searchable in Azure AI Search. The indexer receives blobs in a single container as input. The output is a search index that stores searchable content and metadata in individual fields.
 
 This article uses the [Search Service REST APIs](/rest/api/searchservice) to demonstrate how to configure and run the indexer. However, you can also use:
 
 + An Azure SDK package (any version)
 + [**Import data** wizard](search-get-started-portal-import-vectors.md) in the Azure portal
 
 > [!NOTE]
-> Azure AI Search can ingest role-based access control (RBAC) scope during indexing and transfer those permissions to indexed content in a search index. For more information, see [Use a blob indexer or knowledge source to ingest RBAC scopes metadata](search-blob-indexer-role-based-access.md).
+> Azure AI Search can ingest role-based access control (RBAC) scope during indexing and transfer those permissions to indexed content in a search index. For more information, see [Use a blob indexer or knowledge source to ingest RBAC scopes metadata (preview)](search-blob-indexer-role-based-access.md).
 
 ## Prerequisites
 
@@ -64,7 +64,7 @@ You can use this indexer for the following tasks:
 
 + **Parsing modes:** The indexer supports [JSON parsing modes](search-how-to-index-azure-blob-json.md) if you want to parse JSON arrays or lines into individual search documents. It also supports [Markdown parsing mode](search-how-to-index-azure-blob-markdown.md).
 
-+ **Compatibility with other features:** The indexer works seamlessly with other indexer features, such as [debug sessions](cognitive-search-debug-session.md), [indexer cache for incremental enrichments](enrichment-cache-how-to-configure.md), and [knowledge store](knowledge-store-concept-intro.md).
++ **Compatibility with other features:** The indexer works seamlessly with other indexer features, such as [debug sessions](cognitive-search-debug-session.md), [indexer cache for incremental enrichments (preview)](enrichment-cache-how-to-configure.md), and [knowledge store](knowledge-store-concept-intro.md).
 
 <a name="SupportedFormats"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Blob Storageのインデックス作成に関する記事の軽微な更新"
}
```

### Explanation
この変更は、「Azure Blob Storageのインデックス作成」に関するガイドの記事に対する軽微な更新を示しています。具体的には、インデクサーの機能や利点に関する表現の明確化と、情報の最新化が行われました。

主な変更点には、以下のようなものがあります：
- **表現の明確化**: インデクサーの名称を「*blob indexer*」として明示し、ユーザーに役割をより理解しやすくしました。
- **追加情報の提供**: インデクサーの実行方法がAzure SDKパッケージやインポートウィザードを使用することもできるという情報が強調され、新しい選択肢がユーザーに示されています。
- **プレビューの注記の追加**: RBACスコープのメタデータがプレビュー機能としてインデクサーに統合されることが明記され、潜在的な新しい機能についての注意喚起がされています。

全体として、この更新はAzure AI Searchでのインデックス作成の方法をより的確に示すものであり、ユーザーが最新の情報をもとにより良い決定を下せるようにサポートしています。また、AIに責任を持たせるためのガイダンスも追加され、倫理的な使用を促進します。

## articles/search/search-how-to-index-azure-data-lake-storage.md{#item-faca23}

<details>
<summary>Diff</summary>
````diff
@@ -21,14 +21,14 @@ ms.custom: [ignite-2023, sfi-ropc-nochange, doc-kit-assisted]
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-In this article, learn how to configure an [**indexer**](search-indexer-overview.md) that imports content from Azure Data Lake Storage (ADLS) Gen2 and makes it searchable in Azure AI Search. Inputs to the indexer are your blobs, in a single container. Output is a search index with searchable content and metadata stored in individual fields.
+The *Azure Data Lake Storage Gen2 indexer* imports content from Azure Data Lake Storage Gen2 (ADLS Gen2) into an Azure AI Search index. Inputs to the indexer are your blobs, in a single container. Output is a search index with searchable content and metadata stored in individual fields.
 
 This article supplements [**Create an indexer**](search-howto-create-indexers.md) with information that's specific to indexing from ADLS Gen2. It uses the REST APIs to demonstrate a three-part workflow common to all indexers: create a data source, create an index, create an indexer. Data extraction occurs when you submit the Create Indexer request.
 
 For a code sample in C#, see [Index Data Lake Gen2 using Microsoft Entra ID](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/data-lake-gen2-acl-indexing/README.md) on GitHub.
 
 > [!NOTE]
-> ADLS Gen2 supports an [access control model](/azure/storage/blobs/data-lake-storage-access-control) with Azure role-based access control (Azure RBAC) and POSIX-like access control lists (ACLs) at the blob level. Azure AI Search can now recognize document-level permissions in ADLS Gen2 blobs during indexing and transfers those permissions to indexed content in the search index. For more information about ACL ingestion and RBAC scope during indexing, see [Indexing access control lists and Azure role-based access control scope using indexers](search-indexer-access-control-lists-and-role-based-access.md).
+> ADLS Gen2 supports an [access control model](/azure/storage/blobs/data-lake-storage-access-control) with Azure role-based access control (Azure RBAC) and POSIX-like access control lists (ACLs) at the blob level. Azure AI Search can now recognize document-level permissions in ADLS Gen2 blobs during indexing and transfers those permissions to indexed content in the search index. For more information about ACL ingestion and RBAC scope during indexing, see [Indexing access control lists and Azure role-based access control scope using indexers (preview)](search-indexer-access-control-lists-and-role-based-access.md).
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Data Lake Storageのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、Azure Data Lake Storage (ADLS) Gen2からコンテンツをインデックスする方法に関するガイドの記事に対する軽微な更新を示しています。主な変更点は、インデクサーに関する情報の明確化と詳細の追加です。

具体的には、以下の事項が変更されました：
- **名称の明確化**: 「ADLS Gen2インデクサー」という名称を用いて、何に対してのインデクサーであるかを明確に示しました。
- **機能の説明の改善**: ADLS Gen2からAzure AI Searchインデックスへのコンテンツのインポート方法についての説明が強調され、ユーザーが流れを理解しやすくなっています。
- **プレビュー機能の追加情報**: ADLS Gen2のインデクサーがドキュメントレベルの権限を認識することができ、インデックスされたコンテンツにその権限を転送することが明記され、「プレビュー」機能としての位置付けがより明瞭になりました。

これらの更新により、Azure AI Searchを活用する際のADLS Gen2の使用方法がより明確になり、ユーザーが必要な情報を効率的に得る手助けをしています。また、アプリケーションの開発における責任あるAIの実装に関するガイダンスも引き続き提供されています。

## articles/search/search-how-to-index-azure-tables.md{#item-c8a1d1}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,7 @@ ms.custom:
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-In this article, learn how to configure an [**indexer**](search-indexer-overview.md) that imports content from Azure Table Storage and makes it searchable in Azure AI Search. Inputs to the indexer are your entities, in a single table. Output is a search index with searchable content and metadata stored in individual fields.
+The *Azure Table indexer* imports content from Azure Table Storage into an Azure AI Search index. Inputs to the indexer are your entities, in a single table. Output is a search index with searchable content and metadata stored in individual fields.
 
 This article supplements [**Create an indexer**](search-howto-create-indexers.md) with information that's specific to indexing from Azure Table Storage. It uses the Azure portal and REST APIs to demonstrate a three-part workflow common to all indexers: create a data source, create an index, create an indexer. Data extraction occurs when you submit the Create Indexer request.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Table Storageのインデックス作成に関する記事の軽微な更新"
}
```

### Explanation
この変更は、Azure Table Storageからのコンテンツをインデックスする方法に関する記事に対する軽微な更新を示しています。主にインデクサーの名称の明確化が行われ、文章の一部が修正されました。

具体的な変更点は以下の通りです：
- **名称の明確化**: インデクサーを「*Azure Table indexer*」として明記し、ユーザーにその役割をより明確に伝えています。
- **インデクサーの機能説明の改善**: Azure Table StorageからAzure AI Searchインデックスへコンテンツをインポートするというプロセスがよりはっきりと説明され、ユーザーが内容を理解しやすくなっています。

全体として、この記事はAzure Table Storageを使用してインデックス作成を行う際のプロセスをスムーズに理解できるように更新されており、関連する他のリソースへのリンクも提供されています。これにより、ユーザーは必要な情報に簡単にアクセスできるようにサポートされています。

## articles/search/search-how-to-index-cosmosdb-gremlin.md{#item-e5e93d}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.custom:
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 > [!IMPORTANT]
 > These features and functionality support connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
@@ -25,15 +25,15 @@ ms.custom:
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-In this article, learn how to configure an [**indexer**](search-indexer-overview.md) that imports content from [Azure Cosmos DB for Apache Gremlin](/azure/cosmos-db/gremlin/introduction) and makes it searchable in Azure AI Search.
+The *Azure Cosmos DB for Apache Gremlin indexer* (preview) imports content from [Azure Cosmos DB for Apache Gremlin](/azure/cosmos-db/gremlin/introduction) and makes it searchable in Azure AI Search.
 
 This article supplements [**Create an indexer**](search-howto-create-indexers.md) with information that's specific to Cosmos DB. It uses the REST APIs to demonstrate a three-part workflow common to all indexers: create a data source, create an index, create an indexer. Data extraction occurs when you submit the Create Indexer request.
 
 Because terminology can be confusing, it's worth noting that [Azure Cosmos DB indexing](/azure/cosmos-db/index-overview) and [Azure AI Search indexing](search-what-is-an-index.md) are different operations. Indexing in Azure AI Search creates and loads a search index on your search service.
 
 ## Prerequisites
 
-+ [Register for the preview](https://aka.ms/azure-cognitive-search/indexer-preview) to provide scenario feedback. You can access the feature automatically after form submission.
++ Complete the [indexer preview registration form](https://aka.ms/azure-cognitive-search/indexer-preview). Registration is automatically approved.
 
 + An [Azure Cosmos DB account, database, container, and items](/azure/cosmos-db/sql/create-cosmosdb-resources-portal). Use the same region for both Azure AI Search and Azure Cosmos DB for lower latency and to avoid bandwidth charges.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Cosmos DB Gremlinのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、Azure Cosmos DB Gremlinからのコンテンツをインデックスする方法について説明した記事に対する軽微な更新を示しています。変更内容は、文書内の情報の更新と整理が含まれます。

具体的な変更点には以下が含まれます：
- **インデクサーの名称の明確化**: 「Azure Cosmos DB for Apache Gremlin indexer」として、インデクサーの名称が明記され、役割がより分かりやすくなっています。
- **プレビュー関連の情報の更新**: 「Feature preview」のインクルードが「preview-terms」に変更され、より具体的な情報が提供されています。
- **登録手続きの情報の改善**: プレビュー登録に関する表現がより明確になり、登録プロセスが自動承認であることが強調されています。
- **付加情報の追加**: Azure Cosmos DBアカウント、データベース、コンテナー、アイテムに関する情報が追加され、低遅延を得るための地域設定の重要性が説明されています。

このアップデートにより、ユーザーがAzure Cosmos DB Gremlinを使用してインデックス作成を行う際の手順や考慮すべき点がより一層明確になっており、関連知識の向上に寄与しています。記事全体が整然としていて、ユーザーが必要な情報を得やすくなっています。

## articles/search/search-how-to-index-cosmosdb-mongodb.md{#item-b5aa9f}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.custom:
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 > [!IMPORTANT]
 > These features and functionality support connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
@@ -25,15 +25,15 @@ ms.custom:
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-In this article, learn how to configure an [**indexer**](search-indexer-overview.md) that imports content from [Azure Cosmos DB for MongoDB](/azure/cosmos-db/mongodb/introduction) and makes it searchable in Azure AI Search.
+The *Azure Cosmos DB for MongoDB indexer* (preview) imports content from [Azure Cosmos DB for MongoDB](/azure/cosmos-db/mongodb/introduction) and makes it searchable in Azure AI Search.
 
 This article supplements [**Create an indexer**](search-howto-create-indexers.md) with information that's specific to Cosmos DB. It uses the REST APIs to demonstrate a three-part workflow common to all indexers: create a data source, create an index, create an indexer. Data extraction occurs when you submit the Create Indexer request.
 
 Because terminology can be confusing, it's worth noting that [Azure Cosmos DB indexing](/azure/cosmos-db/index-overview) and [Azure AI Search indexing](search-what-is-an-index.md) are different operations. Indexing in Azure AI Search creates and loads a search index on your search service.
 
 ## Prerequisites
 
-+ [Register for the preview](https://aka.ms/azure-cognitive-search/indexer-preview) to provide scenario feedback. You can access the feature automatically after form submission.
++ Complete the [indexer preview registration form](https://aka.ms/azure-cognitive-search/indexer-preview). Registration is automatically approved.
   
 + An [Azure Cosmos DB account, database, collection, and documents](/azure/cosmos-db/sql/create-cosmosdb-resources-portal). Use the same region for both Azure AI Search and Azure Cosmos DB for lower latency and to avoid bandwidth charges.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Cosmos DB MongoDBのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、Azure Cosmos DB MongoDBからのコンテンツをインデックスする方法について説明した記事に対する軽微な更新を示しています。主な焦点は、文書の情報を整理し、明確にすることにあります。

具体的な変更点は以下の通りです：
- **インデクサーの名称の明確化**: インデクサーを「Azure Cosmos DB for MongoDB indexer」として明記し、ユーザーにその機能がより具体的に伝わるよう修正されています。
- **プレビュー関連の情報の更新**: 「Feature preview」のインクルードが「preview-terms」に変更され、プレビュー機能に関する情報が明確になっています。
- **登録手続きの情報の改善**: プレビュー登録の表現が変更され、登録プロセスが自動承認であることが強調されています。
- **付加情報の追加**: Azure Cosmos DBアカウント、データベース、コレクション、ドキュメントに関する情報が更新され、低遅延を実現するための地域設定の重要性が説明されています。

これらの変更により、読者はAzure Cosmos DB MongoDBを利用してインデックス作成を行う方法をより簡単に理解し、関連情報を得ることができるようになっています。記事全体が整然としており、必要な情報にアクセスしやすくなっています。

## articles/search/search-how-to-index-cosmosdb-sql.md{#item-2e888b}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ ms.custom:
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-In this article, learn how to configure an [**indexer**](search-indexer-overview.md) that imports content from [Azure Cosmos DB for NoSQL](/azure/cosmos-db/nosql/) and makes it searchable in Azure AI Search.
+The *Azure Cosmos DB for NoSQL indexer* imports content from [Azure Cosmos DB for NoSQL](/azure/cosmos-db/nosql/) and makes it searchable in Azure AI Search.
 
 This article supplements [**Create an indexer**](search-howto-create-indexers.md) with information that's specific to Cosmos DB. It uses the Azure portal and REST APIs to demonstrate a three-part workflow common to all indexers: create a data source, create an index, create an indexer. Data extraction occurs when you submit the Create Indexer request.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Cosmos DB SQLのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、Azure Cosmos DB SQLからのコンテンツをインデックスする方法に関する記事における軽微な更新を示しています。主に、文中の情報が整理され、ユーザーにとっての明確さが向上しています。

具体的な変更点は以下の通りです：
- **インデクサーの名称の明確化**: 記事内の「indexer」の説明が改訂され、「Azure Cosmos DB for NoSQL indexer」として具体的な名称が強調されています。これにより、使用するインデクサーがどのサービスに関連しているかが明確になります。
- **文の構造の変更**: 記事の初めにインデクサーがどのように機能するかについての情報がより簡潔に表現され、読みやすさが増しています。

これらの変更により、読者はAzure Cosmos DB SQLを利用したインデックス作成の手順をより簡単に理解できるようになり、関連情報にアクセスしやすくなっています。記事全体の流れが改善されており、ユーザーの理解を助ける内容となっています。

## articles/search/search-how-to-index-logic-apps.md{#item-e25907}

<details>
<summary>Diff</summary>
````diff
@@ -185,7 +185,7 @@ You can make the following modifications to a search index without breaking inde
 
 - [Add scoring profiles](index-add-scoring-profiles.md)
 - [Add semantic ranking](semantic-how-to-configure.md)
-- [Add spell check](speller-how-to-add.md)
+- [Add spell check (preview)](speller-how-to-add.md)
 - [Add synonym maps](search-synonyms.md)
 - [Add suggesters](index-add-suggesters.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Logic Appsのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、Logic Appsに関するインデックス作成方法の記事に対する軽微な更新を示しています。主に、スペルチェック機能に関する情報が更新され、読者にとっての明確さが向上しています。

具体的な変更点は以下の通りです：
- **スペルチェック機能の状態の明示化**: 「Add spell check」の記述が「Add spell check (preview)」に変更され、ユーザーにこの機能が現在プレビュー版であることが明示されています。この変更により、利用者がその機能を使用するにあたっての注意が促されます。

この更新により、読者はLogic Appsのインデックス作成の際に利用可能な機能について、より正確な情報を得ることができるようになります。全体として、記事の内容が改善され、情報の理解を助けることになっています。

## articles/search/search-how-to-index-mysql.md{#item-fffdee}

<details>
<summary>Diff</summary>
````diff
@@ -11,13 +11,14 @@ ms.custom:
   - kr2b-contr-experiment
   - ignite-2023
   - sfi-ropc-nochange
+ai-usage: ai-assisted
 ---
 
 # Index data from Azure Database for MySQL Flexible Server (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 > [!IMPORTANT]
 > These features and functionality support connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
@@ -26,15 +27,15 @@ ms.custom:
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-In this article, learn how to configure an [**indexer**](search-indexer-overview.md) that imports content from Azure Database for MySQL and makes it searchable in Azure AI Search. Inputs to the indexer are rows from a single table or view. Output is a search index with searchable content in individual fields.
+The *Azure Database for MySQL indexer* (preview) imports content from Azure Database for MySQL Flexible Server into an Azure AI Search index. Inputs to the indexer are rows from a single table or view. Output is a search index with searchable content in individual fields.
 
 This article supplements [**Create an indexer**](search-howto-create-indexers.md) with information that's specific to indexing from Azure Database for MySQL Flexible Server. It uses the REST APIs to demonstrate a three-part workflow common to all indexers: create a data source, create an index, create an indexer. Data extraction occurs when you submit the Create Indexer request.
 
 When configured to include a high water mark and soft deletion, the indexer takes all changes, uploads, and deletes for your MySQL database. It reflects these changes in your search index. Data extraction occurs when you submit the Create Indexer request.
 
 ## Prerequisites
 
-- [Register for the preview](https://aka.ms/azure-cognitive-search/indexer-preview) to provide scenario feedback. You can access the feature automatically after form submission.
+- Complete the [indexer preview registration form](https://aka.ms/azure-cognitive-search/indexer-preview). Registration is automatically approved.
 
 - [Azure Database for MySQL Flexible Server](/azure/mysql/flexible-server/overview) and sample data. Data must reside in a table or view. A primary key is required. If you're using a view, it must have a [high water mark column](#DataChangeDetectionPolicy). 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MySQLからのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、Azure Database for MySQLからのインデックス作成に関する記事に対する軽微な更新を示しています。主な変更点は、プレビュー機能の明示化と文の構造の整理にあります。

具体的な変更点は以下の通りです：
- **AI利用の記述追加**: 「ai-usage: ai-assisted」という内容が追加され、AI支援機能に関する情報が強調されています。この変更により、機能の利用方法がより明確になります。
- **プレビューの記述の調整**: 「[!INCLUDE [Feature preview]」が「[!INCLUDE [preview-terms]」に置き換えられ、プレビュー機能に関する具体的な東京情報が提供されています。
- **文の構造改善**: 「Azure Database for MySQL indexer」の説明が再構成され、明確に「プレビュー」版であることが強調されています。また、「登録」を促す表現が具体的になり、ユーザーがプレビュー機能を利用するための登録手続きがスムーズに理解できるようになっています。

これらの変更により、記事はユーザーにとってより利用しやすく、理解しやすい内容になっています。Azure Database for MySQLからのデータを検索インデックスにインポートする方法についてのガイダンスが、より明確に示されています。

## articles/search/search-how-to-index-onelake-files.md{#item-95f3db}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ ms.custom:
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-In this article, you learn how to configure a OneLake files indexer for extracting searchable data and metadata from a [lakehouse](/fabric/onelake/create-lakehouse-onelake) on top of [Microsoft OneLake](/fabric/onelake/onelake-overview).
+The *OneLake files indexer* imports content and metadata from a [lakehouse](/fabric/onelake/create-lakehouse-onelake) in [Microsoft OneLake](/fabric/onelake/onelake-overview) and makes the content searchable in Azure AI Search.
 
 To configure and run the indexer, you can use:
 
@@ -71,7 +71,7 @@ This article uses the REST APIs to illustrate each step.
 
 + There's no support to ingest files from **My Workspace** workspace in OneLake since this is a personal repository per user.
 
-+ Indexing files from [Fabric items with sensitivity labels](/fabric/fundamentals/apply-sensitivity-labels), for example, lakehouses, isn't supported. However, when sensitivity labels are applied directly to individual documents, ingestion of protected content and associated labels is supported. In these cases, Azure AI Search can extract and honor sensitivity labels and labeled documents' content through its [integration with Purview](search-indexer-sensitivity-labels.md). 
++ Indexing files from [Fabric items with sensitivity labels](/fabric/fundamentals/apply-sensitivity-labels), for example, lakehouses, isn't supported. However, when sensitivity labels are applied directly to individual documents, ingestion of protected content and associated labels is supported. In these cases, Azure AI Search can extract and honor sensitivity labels and labeled documents' content through its [integration with Purview (preview)](search-indexer-sensitivity-labels.md). 
   
 + Workspace role-based permissions in Microsoft OneLake might affect indexer access to files. Ensure that the Azure AI Search service principal (managed identity) has sufficient permissions over the files you intend to access in the target [Microsoft Fabric workspace](/fabric/fundamentals/workspaces). 
 
@@ -83,7 +83,7 @@ You can use this indexer for the following tasks:
 + **Deletion detection:** The indexer can [detect deletions via custom metadata](#detect-deletions-via-custom-metadata) for most files and shortcuts. This requires adding metadata to files to signify that they have been "soft deleted", enabling their removal from the search index. Currently, it's not possible to detect deletions in Google Cloud Storage or Amazon S3 shortcut files because custom metadata isn't supported for those data sources.
 + **Applied AI enrichment through skillsets:** [Skillsets](cognitive-search-concept-intro.md) are fully supported by the OneLake files indexer. This includes key features like [integrated vectorization](vector-search-integrated-vectorization.md) that adds data chunking and embedding steps.
 + **Parsing modes:** The indexer supports [JSON parsing modes](search-how-to-index-azure-blob-json.md) if you want to parse JSON arrays or lines into individual search documents. It also supports [Markdown parsing mode](search-how-to-index-azure-blob-markdown.md).
-+ **Compatibility with other features:** The OneLake indexer is designed to work seamlessly with other indexer features, such as [debug sessions](cognitive-search-debug-session.md), [indexer cache for incremental enrichments](enrichment-cache-how-to-configure.md), and [knowledge store](knowledge-store-concept-intro.md).
++ **Compatibility with other features:** The OneLake indexer is designed to work seamlessly with other indexer features, such as [debug sessions](cognitive-search-debug-session.md), [indexer cache for incremental enrichments (preview)](enrichment-cache-how-to-configure.md), and [knowledge store](knowledge-store-concept-intro.md).
 
 <a name="SupportedFormats"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLakeファイルのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、OneLakeファイルのインデックス作成方法に関する記事の軽微な更新を示しています。主な変更点は、説明の明確化や機能に関する詳細の追加です。

具体的な変更点は以下の通りです：
- **インデックス作成者の説明の強化**: 「OneLake files indexer」がコンテンツとメタデータをインポートし、Azure AI Searchで検索可能にする機能がより具体的に記述されています。
- **プレビュー機能の明示化**: 「インデックス作成者のキャッシュとインクリメンタル強化（プレビュー）」についての記述が追加され、ユーザーに最新機能の状況を理解させています。
- **ファイルアクセス権限に関する注意点の追加**: Microsoft OneLakeのワークスペースにおける役割ベースのアクセス許可に関連する情報が追加され、インデックス作成者がファイルにアクセスする際の権限確保についての注意喚起が行われています。

これらの変更により、読者はOneLakeからのデータインデクシングに関するプロセスや注意事項をより深く理解することができ、Azure AI Searchを利用する上での利便性が向上します。全体として、記事はユーザーにとって利用価値の高い情報を提供するよう改良されています。

## articles/search/search-how-to-index-sharepoint-online.md{#item-8c099c}

<details>
<summary>Diff</summary>
````diff
@@ -17,25 +17,16 @@ ms.custom:
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-When setting up permissions, consider the following information:
-> The SharePoint in Microsoft 365 indexer is in preview. It's offered "as-is" under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) and supported on a best-effort basis only. Preview features aren't recommended for production workloads and aren't guaranteed to become generally available.
->
-> Before you proceed, review the [known limitations](#limitations-and-considerations).
->
-> [Fill out this form](https://aka.ms/azure-cognitive-search/indexer-preview) to register for the preview. All requests are approved automatically. After you fill out the form, use a [preview REST API](/rest/api/searchservice/search-service-api-versions#preview-versions) to index your content. 
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> These features and functionality support connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag occurs before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data flows outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This responsibility includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-This article explains how to configure a [search indexer](search-indexer-overview.md) to index documents stored in SharePoint document libraries for full-text search in Azure AI Search. The configuration steps are first, followed by behaviors and scenarios.
+The *SharePoint in Microsoft 365 indexer* (preview) imports documents from SharePoint document libraries and makes them searchable in Azure AI Search. The configuration steps are first, followed by behaviors and scenarios.
 
 In Azure AI Search, an indexer extracts searchable data and metadata from a data source. The SharePoint in Microsoft 365 indexer provides the following functionality:
 
@@ -52,6 +43,8 @@ In Azure AI Search, an indexer extracts searchable data and metadata from a data
   
 ## Prerequisites
 
++ Complete the [indexer preview registration form](https://aka.ms/azure-cognitive-search/indexer-preview). Registration is automatically approved.
+
 + [Azure AI Search](search-create-service-portal.md), Basic pricing tier or higher.
 
 + [SharePoint in Microsoft 365](/sharepoint/introduction) cloud service (OneDrive isn't a supported data source).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint Onlineインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、SharePoint Onlineのインデックス作成に関する記事に対する軽微な更新を示しています。内容の一部が明確に整理され、重要な情報が強調されています。

具体的な変更点は以下の通りです：
- **インデックス作成者の説明の明確化**: 「SharePoint in Microsoft 365 indexer」がドキュメントをインポートし、Azure AI Searchで検索可能にする役割についての具体的な説明が追加されました。
- **プレビュー登録に関する手続きの強化**: プレビュー登録用のフォームの記述がより明確になり、ユーザーが登録を行う際の指示が簡潔に整理されています。
- **重要な注意事項の修正**: 機能が他のMicrosoftサービスやサードパーティサービスと連携できることの重要性が強調され、データの処理や保存に関する責任についてのフレーズが再構成されています。
- **責任の明示化**: ユーザーが自組織のコンプライアンスや地理的な境界を管理する責任が再確認され、適切な許可の設定や境界の明確化が求められています。

これにより、読者はSharePoint Onlineからのデータインデクシングに関する手順や注意点をより容易に理解できるようになり、実装時のリスクや考慮事項について通知を受けることができます。全体として、記事はユーザーに対してより具体的で有用な情報を提供する形へと改善されています。

## articles/search/search-how-to-index-sql-database.md{#item-86d873}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ ms.custom:
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-In this article, learn how to configure an [**indexer**](search-indexer-overview.md) that imports content from Azure SQL Database or an Azure SQL managed instance and makes it searchable in Azure AI Search. 
+The *Azure SQL indexer* imports content from Azure SQL Database or Azure SQL Managed Instance into an Azure AI Search index.
 
 This article supplements [**Create an indexer**](search-howto-create-indexers.md) with information that's specific to Azure SQL. It uses the Azure portal and REST APIs to demonstrate a three-part workflow common to all indexers: create a data source, create an index, create an indexer. Data extraction occurs when you submit the Create Indexer request.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SQLデータベースのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、SQLデータベースインデックス作成に関する記事の軽微な更新を示しています。記事の内容がより明確に記述され、特定の用語が改訂されました。

具体的な変更点は以下の通りです：
- **インデックス作成者の名称の変更**: 「Azure SQL Database」や「Azure SQL Managed Instance」を使用してデータをインポートするインデックス作成者について、名称が「*Azure SQL indexer*」に統一され、機能がよりわかりやすくなりました。
- **説明の簡素化**: 記事全体の説明が簡潔になり、インデックス作成者の役割と機能を端的に表現しています。この変更により、読者はインデックス作成者の目的をより直感的に理解できるようになりました。

これにより、読者はAzure SQLからのデータインデクシングに関する手法を把握しやすくなり、インデックス作成に必要な情報が明確に伝わるようになりました。全体的に、記事はより一貫性があり、ユーザーフレンドリーな内容へと改善されています。

## articles/search/search-how-to-index-sql-managed-instance.md{#item-009ccc}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.custom:
 ms.topic: how-to
 ms.date: 07/11/2025
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Indexer connections to Azure SQL Managed Instance through a public endpoint
@@ -20,7 +21,7 @@ ms.update-cycle: 365-days
 >
 > You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
 
-Indexers in Azure AI Search connect to external data sources over a public endpoint. If you're setting up an [Azure SQL indexer](search-how-to-index-sql-database.md) for a connection to a SQL managed instance, follow the steps in this article to ensure the public endpoint is set up correctly. 
+An *Azure SQL indexer* connects Azure AI Search to external data sources over a public endpoint. If you're setting up a connection to Azure SQL Managed Instance, follow the steps in this article to ensure the public endpoint is set up correctly.
 
 Alternatively, for private connections, [create a shared private link](search-indexer-how-to-access-private-sql.md) instead.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SQLマネージドインスタンスのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、SQLマネージドインスタンスのインデックス作成に関する記事に対する軽微な更新を示しています。文言の明確化と用語の整理が行われ、より理解しやすくなっています。

具体的な変更点は以下の通りです：
- **新しい属性の追加**: `ai-usage: ai-assisted`というプロパティが追加され、AIの利用に関する情報が明示されました。
- **インデックス作成者の説明の改善**: 「インデックス作成者」という用語がより明確に定義され、Azure AI Searchと外部データソースとの接続という説明が修正されました。これにより、読者はインデックス作成者の役割をより正確に理解できるようになりました。
- **文の簡略化**: 文構造が簡じされ、内容がわかりやすく表現されています。「接続を設定する際の手順」という部分が明確になり、ユーザーが求める情報に迅速にアクセスできるように配慮されています。

この変更により、読者はAzure SQLマネージドインスタンスへのインデックス作成に関する手順や要件をより効果的に理解できるようになりました。全体として、記事はより洗練され、使いやすい内容へと改善されています。

## articles/search/search-how-to-integrated-vectorization.md{#item-86fb1e}

<details>
<summary>Diff</summary>
````diff
@@ -238,7 +238,7 @@ Azure AI Search supports text-embedding-ada-002, text-embedding-3-small, and tex
 
 ### [Azure Vision](#tab/prepare-model-vision)
 
-Azure AI Search supports Azure Vision image retrieval through multimodal embeddings (version 4.0). Internally, Azure AI Search calls the [multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) to connect to Azure Vision.
+Azure AI Search supports Azure Vision image retrieval through multimodal embeddings (version 4.0). Internally, Azure AI Search calls the [multimodal embeddings skill (preview)](cognitive-search-skill-vision-vectorize.md) to connect to Azure Vision.
 
 1. Go to your Microsoft Foundry resource in the [Azure portal](https://portal.azure.com).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "統合ベクトル化に関する記事の文言修正"
}
```

### Explanation
この変更は、統合ベクトル化に関する記事に対する軽微な文言修正を示しています。特に、Azure Visionに関連する機能の説明が更新されています。

具体的な変更点は以下の通りです：
- **プレビュー版の明示化**: Azure AI Searchが内部的に呼び出す「multimodal embeddings skill」に関する記述が修正され、バージョンが「プレビュー」として明示されています。これにより、ユーザーはこの機能がまだ正式リリースではなく、開発中であることを認識できます。
- **文の一貫性の向上**: 表現が整理され、技術的な情報がより明確に伝わるように配慮されています。

この変更により、読者はAzure Visionの画像検索機能の利用状況やそのステータスをより理解しやすくなり、利用に関する期待や注意点を正確に把握できるようになりました。全体として、記事はより透明性のある情報を提供する内容へと改善されています。

## articles/search/search-how-to-large-index.md{#item-d34e42}

<details>
<summary>Diff</summary>
````diff
@@ -75,7 +75,7 @@ Partitioning data into smaller individual data sources enables parallel processi
 
 As with the push API, indexers allow you to configure the number of items per batch. For indexers based on the [Create Indexer REST API](/rest/api/searchservice/indexers/create), set the `batchSize` argument to customize this setting to better match the characteristics of your data.
 
-Default batch sizes are data-source specific. Azure SQL Database and Azure Cosmos DB have a default batch size of 1,000. In contrast, Azure Blob and SharePoint (Preview) indexing set the batch size at 10 documents in recognition of the larger average document size.
+Default batch sizes are data-source specific. Azure SQL Database and Azure Cosmos DB have a default batch size of 1,000. In contrast, Azure Blob and SharePoint (preview) indexing set the batch size at 10 documents in recognition of the larger average document size.
 
 ### Schedule indexers for long-running processes
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "大規模インデックス作成に関する記事の文言修正"
}
```

### Explanation
この変更は、大規模インデックス作成に関する記事における軽微な文言修正を示しています。特に、SharePointに関連するインデックス作成の情報が更新されています。

具体的な変更点は以下の通りです：
- **プレビュー版の明示化**: SharePointに関する記述が修正され、「SharePoint (Preview)」という表記が「SharePoint (preview)」に変更されています。これにより、読者はこの機能がプレビュー版であることを理解しやすくなります。
- **文の整合性の向上**: 用語の統一が図られ、情報の一貫性が改善されています。

この更新により、読者はAzure BlobおよびSharePointのインデックス作成に関するバッチサイズの設定やその特性をより正確に理解できるようになり、リソース管理やインデックス作成プロセスの最適化に役立ちます。全体として、記事は技術的な透明性が向上した内容へと改善されています。

## articles/search/search-how-to-managed-identities.md{#item-3536f2}

<details>
<summary>Diff</summary>
````diff
@@ -9,6 +9,7 @@ ms.custom:
   - ignite-2023
   - build-2024
   - sfi-ropc-nochange
+ai-usage: ai-assisted
 ---
 
 # Configure a search service to connect using a managed identity
@@ -37,7 +38,7 @@ You can use managed identities for the following scenarios.
 | Connect to embedding and chat completion models in Azure OpenAI, Microsoft Foundry, and Azure Functions via skills/vectorizers <sup>2</sup> | Yes | Yes |
 | [Connect to Azure Key Vault for customer-managed keys](search-security-manage-encryption-keys.md) | Yes | Yes |
 | [Connect to Debug sessions (hosted in Azure Storage)](cognitive-search-debug-session.md)	<sup>1</sup> | Yes | No |
-| [Connect to an enrichment cache (hosted in Azure Storage)](enrichment-cache-how-to-configure.md) <sup>1,</sup> <sup>3</sup> | Yes | Yes <sup>4</sup>|
+| [Connect to an enrichment cache, hosted in Azure Storage (preview)](enrichment-cache-how-to-configure.md) <sup>1,</sup> <sup>3</sup> | Yes | Yes <sup>4</sup>|
 | [Connect to a Knowledge Store (hosted in Azure Storage)](knowledge-store-create-rest.md) <sup>1</sup>| Yes | Yes |
 
 <sup>1</sup> For connectivity between search and storage, network security imposes constraints on which type of managed identity you can use. Only a system managed identity can be used for a same-region connection to Azure Storage, and that connection must be via the *trusted service exception* or resource instance rule. See [Access to a network-protected storage account](search-indexer-securing-resources.md#access-to-a-network-protected-storage-account) for details.
@@ -279,7 +280,7 @@ A user-assigned managed identity is supported through the `identity` property on
 }
 ```
 
-[**Enrichment cache:**](enrichment-cache-how-to-configure.md)
+[**Enrichment cache (preview):**](enrichment-cache-how-to-configure.md)
 
 An indexer creates, uses, and remembers the container used for the cached enrichments. It's not necessary to include the container in the cache connection string. You can find the object ID on the **Identity** page of your search service in the Azure portal.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "管理対象アイデンティティに関する記事の内容更新"
}
```

### Explanation
この変更は、管理対象アイデンティティに関する記事の更新を示しており、特に新しい情報と用語の明確化が行われています。

具体的な変更点は以下の通りです：
- **新しいカスタムタグの追加**: 記事のメタデータに「ai-usage: ai-assisted」というタグが追加され、AI技術の使用に関する情報が強調されています。
- **プレビュー版の明示化**: エンリッチメントキャッシュに関する項目の表記が「エンリッチメントキャッシュ (プレビュー)」に変更され、本機能がプレビュー版であることが明確に示されています。これにより、読者はこの機能の開発段階を理解しやすくなります。
- **表の用語修正**: エンリッチメントキャッシュのリンク付き表記が更新され、より一貫した用語が使用されています。

これらの変更により、読者は管理対象アイデンティティを使用するシナリオや関連機能について最新の情報を取得でき、文書の透明性と信頼性が向上しています。全体として、記事はより現代の要件に適応した内容へと改善されています。

## articles/search/search-how-to-multiple-indexers-one-index.md{#item-5ccefd}

<details>
<summary>Diff</summary>
````diff
@@ -13,6 +13,8 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
 In this tutorial, you configure independent blob indexers for DOCX, JSON, and CSV content that write to one Azure AI Search index. A nullable union schema lets each pipeline populate the fields it owns while your application queries all formats together. You can extend this pattern to other compatible indexer types when the indexers have compatible field mappings and target the same index. This tutorial demonstrates and verifies only folder-scoped blob indexers.
 
 In this tutorial, you:
@@ -24,16 +26,7 @@ In this tutorial, you:
 > + Run the indexers and verify the combined keyword, vector, and hybrid results
 > + Review content ownership, troubleshooting, and cleanup practices
 
-> [!IMPORTANT]
-> Semantic chunking in the Azure Content Understanding skill is part of the 2026-08-01-preview REST API. The multi-indexer pattern, index projections, and the Content Understanding skill without semantic chunking are generally available. However, for consistency, this tutorial uses the 2026-08-01-preview across all requests.
->
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data flows outside of your organization's compliance and geographic boundaries and any related implications. Ensure that appropriate permissions, boundaries, and approvals are in place.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This responsibility includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+Semantic chunking (preview) in the Azure Content Understanding skill requires the `2026-08-01-preview` REST API. The multi-indexer pattern, index projections, and the Content Understanding skill without semantic chunking are generally available. However, for consistency, this tutorial uses `2026-08-01-preview` across all requests.
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "複数のインデクサーを使用する方法に関する記事の更新"
}
```

### Explanation
この変更は、複数のインデクサーを使用して一つのインデックスにデータを記録する方法に関する記事の内容を更新したものです。具体的には、プレビュー機能に関する情報の追加と、重要な注意事項の簡略化が行われています。

具体的な変更点は以下の通りです：
- **プレビュー用のインクルード追加**: 記事の冒頭に「[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]」が追加され、プレビュー機能に関する詳細が明確にされました。これにより、使用する機能がプレビューであることが強調されています。
- **注意事項の簡略化**: Semantic chunkingに関する注意事項が簡素化され、「2026-08-01-preview」REST APIが必要であることが明記されている一方で、他の詳細が削除され、内容がすっきりとしました。これにより、重要な情報がより簡単に伝わるようになっています。

この更新により、読者は複数のインデクサーを使ったデータの構成方法を理解しやすくなり、特にプレビュー機能の利用条件や注意事項に関する情報が整理されています。全体として、この記事は技術的な透明性とユーザビリティが向上した内容へと改善されています。

## articles/search/search-how-to-page-list-results.md{#item-73059a}

<details>
<summary>Diff</summary>
````diff
@@ -15,14 +15,7 @@ zone_pivot_groups: search-csharp-python-rest
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 Starting with the `2026-08-01-preview` REST API, use cursor pagination (preview) to enumerate supported service resources one page at a time. The service returns an opaque continuation URL when more results are available.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ページリスト結果の表示方法に関する記事の内容更新"
}
```

### Explanation
この変更は、ページリスト結果の表示方法に関する記事に対する更新で、主にプレビュー機能についての情報の整理と追加が行われています。

具体的な変更点は以下の通りです：
- **重要な注意事項の削除**: これまで記載されていた詳細な注意事項が削除され、内容が簡素化されました。しかし、その代わりにプレビュー条項のインクルードが追加され、「[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]」が挿入され、プレビュー機能に関する情報が適切に整備されています。
- **新しい情報の追加**: `2026-08-01-preview` REST APIを使用して、カーソルページネーションについての説明が新たに追加されており、これによりサポートされるサービスリソースを1ページずつ列挙する方法が具体的に説明されています。この内容は、クライアントがサービスからの続行URLを利用して、より多くの結果が利用可能な場合に対応する方法を明確にしています。

これらの変更により、読者は新しいカーソルページネーション機能の利用方法を理解しやすくなり、プレビューとしての条件を確認できるようになっています。全体として、記事はよりシンプルで明確な内容へと改善され、技術的情報の透明性が高まっています。

## articles/search/search-how-to-semantic-chunking-content-understanding.md{#item-5968e6}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
-title: Chunk and Vectorize Content with Azure Content Understanding Skill
-description: Use the Azure Content Understanding skill to semantically chunk documents, generate AI-based image descriptions, and vectorize the results in an Azure AI Search index.
+title: Chunk and Vectorize with Content Understanding
+description: Use preview semantic chunking and AI-based image descriptions with the Azure Content Understanding skill to build an Azure AI Search index.
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 06/02/2026
@@ -14,10 +14,10 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
 > [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
+> These features and functionality support connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
 >
 > It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
 >
@@ -27,8 +27,8 @@ In this article, you learn how to use the [Azure Content Understanding skill](co
 
 > [!div class="checklist"]
 > + Extract text and images from a document
-> + Produce semantically coherent chunks that respect paragraph and section boundaries
-> + Generate AI descriptions of charts, diagrams, and other inline images
+> + Produce semantically coherent chunks that respect paragraph and section boundaries (preview)
+> + Generate AI descriptions of charts, diagrams, and other inline images (preview) 
 > + Embed each chunk for vector search and project it into an Azure AI Search index
 
 The Azure Content Understanding skill returns one or more chunks per document. Each chunk contains Markdown-formatted content, location metadata (page numbers and bounding polygons), and optional references to extracted images. When you set `chunkingProperties.method` to `semantic`, chunks follow paragraph and heading boundaries instead of fixed-character spans. When you set `modelName` and `modelDeployment`, the skill calls an Azure OpenAI chat-completion deployment to generate descriptions of embedded images. The skill then merges those descriptions into the chunk content.
@@ -55,7 +55,7 @@ The article builds a one-to-many indexing pipeline. Each source document produce
 
 1. The indexer reads each file from Azure Blob Storage and passes the binary content to the skillset through `/document/file_data`.
 
-1. The **Azure Content Understanding skill** chunks the document into `text_sections`. When `modelName` and `modelDeployment` are set, it also produces AI-generated descriptions of embedded images and inlines them into each chunk's Markdown.
+1. The **Azure Content Understanding skill** uses semantic chunking (preview) to produce `text_sections`. When `modelName` and `modelDeployment` are set, it also produces AI-generated descriptions (preview) of embedded images and inlines them into each chunk's Markdown.
 
 1. The **Azure OpenAI Embedding skill** runs once per chunk and produces a vector for the chunk content.
 
@@ -201,13 +201,13 @@ The following index definition matches the skillset that you create in the next
 }
 ```
 
-## Define a skillset for semantic chunking and vectorization
+## Define a skillset for semantic chunking (preview) and vectorization
 
 With the target index in place, define the skillset that produces the chunks, vectors, and projection mappings that feed it.
 
 The skillset has two skills:
 
-+ The [Azure Content Understanding skill](cognitive-search-skill-content-understanding.md) chunks each document. Setting `chunkingProperties.method` to `semantic` makes the skill respect paragraph and heading boundaries. Setting `modelName` and `modelDeployment` enables AI-generated image descriptions, which the skill inlines into the chunk content before vectorization. For the list of supported chat completion models and other parameter details, see [Skill parameters](cognitive-search-skill-content-understanding.md#skill-parameters).
++ The [Azure Content Understanding skill](cognitive-search-skill-content-understanding.md) chunks each document. Setting `chunkingProperties.method` to `semantic` makes the skill respect paragraph and heading boundaries. Setting `modelName` and `modelDeployment` enables AI-generated image descriptions (preview), which the skill inlines into the chunk content before vectorization. For the list of supported chat completion models and other parameter details, see [Skill parameters](cognitive-search-skill-content-understanding.md#skill-parameters).
 
 + The [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md) generates a vector for each chunk's content.
 
@@ -358,7 +358,7 @@ POST {endpoint}/indexers?api-version=2026-08-01-preview
 }
 ```
 
-When the indexer runs, the Content Understanding skill chunks each document, optionally generates image descriptions, and writes one search document per chunk to the index.
+When the indexer runs, the Content Understanding skill uses semantic chunking (preview), optionally generates AI-based image descriptions (preview), and writes one search document per chunk to the index.
 
 ### Check indexer status
 
@@ -421,7 +421,7 @@ A successful response looks similar to the following (trimmed for brevity):
 
 The response includes:
 
-+ `chunk`: The Markdown content of each chunk. When you configure `modelName` and `modelDeployment`, AI-generated image descriptions appear inline within the Markdown.
++ `chunk`: The Markdown content of each chunk. When you configure `modelName` and `modelDeployment`, AI-generated image descriptions (preview) appear inline within the Markdown.
 + `page_number_from` and `page_number_to`: The page range that produced the chunk.
 + `image_path`: The path to the image extracted with the chunk or, when a chunk spans multiple images, a semicolon-separated list of paths. The exact shape depends on whether a knowledge store file projection is configured. Without a file projection, the path is the short form shown in the example (`figures/3`). With a file projection, the path is the relative path of the image in the knowledge store. To make these images available to client apps, see [(Optional) Project images for retrieval](#optional-project-images-for-retrieval).
 
@@ -468,7 +468,7 @@ If the indexer fails or returns unexpected results, check the following common c
 The skill returns a `400 Skill validation failed` error when parameter combinations conflict. Common causes:
 
 + `modelName` is set without `modelDeployment`, or vice versa. Both must be set together.
-+ `method` is `semantic` and `overlapLength` is greater than `0`. Set `overlapLength` to `0` or omit it.
++ `method` is `semantic` (preview) and `overlapLength` is greater than `0`. Set `overlapLength` to `0` or omit it.
 + `method` and `unit` aren't a supported pair. Use `fixedSize` with `characters` or `semantic` with `tokens`.
 
 ### Authorization fails against the Foundry resource
@@ -486,7 +486,7 @@ If indexed documents have no chunks, verify that:
 + The Foundry resource is in a supported region.
 + Password-protected PDFs are unlocked before indexing.
 
-### Image descriptions are missing
+### Image descriptions (preview) are missing
 
 If chunks don't include inline image descriptions, verify that:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツ理解によるチャンク化とベクトル化に関する記事の更新"
}
```

### Explanation
この変更は、Azure Content Understanding skillを使用してコンテンツをチャンク化およびベクトル化する方法に関する記事を更新したもので、主にタイトル、説明、プレビュー機能の強調が行われています。

具体的な変更点は以下の通りです：
- **タイトルと説明の変更**: 記事のタイトルが「Chunk and Vectorize Content with Azure Content Understanding Skill」から「Chunk and Vectorize with Content Understanding」に変更され、よりシンプルで具体的な内容になりました。また、説明文も更新され、プレビュー機能が追加されたことが強調されています。
- **プレビュー用のインクルード追加**: プレビュー機能に関する注意事項を示す「[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]」が追加され、読者がこれらの機能を使用する際の条件が明確化されました。
- **重要な機能についての表現の変更**: いくつかの段落で、AIが生成する画像の説明やセマンティックチャンク化（プレビュー）についての言及が更新され、プレビュー機能であることが明示されています。

これらの更新により、記事はより読みやすく、最新の機能に関する正確な情報を提供することができるようになっています。また、読者は新たなプレビュー機能についての理解を深め、実際の使用例に適切に適用できるようになります。全体として、情報の透明性と一貫性が向上しています。

## articles/search/search-how-to-semantic-chunking.md{#item-4a1d07}

<details>
<summary>Diff</summary>
````diff
@@ -58,7 +58,7 @@ You must use a [supported data source](search-indexer-overview.md#supported-data
 
 - Supported file formats include PDF, JPEG, JPG, PNG, BMP, TIFF, DOCX, XLSX, PPTX, and HTML.
 
-- Supported indexers are any indexer that can handle the supported file formats. These indexers include [Blob indexers](search-how-to-index-azure-blob-storage.md), [Microsoft OneLake indexers](search-how-to-index-onelake-files.md), and [File indexers](search-file-storage-integration.md).
+- Supported indexers are any indexer that can handle the supported file formats. These indexers include [Blob indexers](search-how-to-index-azure-blob-storage.md), [Microsoft OneLake indexers](search-how-to-index-onelake-files.md), and [File indexers (preview)](search-file-storage-integration.md).
 
 - Supported regions for the portal experience of this feature include East US, West Europe, and North Central US. If you're setting up your skillset programmatically, you can use any Azure Document Intelligence region that also provides the AI enrichment feature of Azure AI Search. For more information, see [Supported regions for the Document Layout skill](cognitive-search-skill-document-intelligence-layout.md#supported-regions).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックチャンク化に関する記事の索引作成者の更新"
}
```

### Explanation
この変更は、セマンティックチャンク化に関する記事における索引作成者の種類についての情報を更新したものです。

具体的な変更内容は以下の通りです：
- **索引作成者の説明の変更**: "File indexers" の説明において、以前はこの機能に関する特定の言及がなかったのですが、変更後は「File indexers (preview)」と表記され、プレビュー版であることが明示されました。これにより、読者はこの索引作成者が現在プレビュー版であることを理解できるようになりました。
  
全体として、この変更により、情報が最新の状態に保たれ、利用者が現在利用可能な機能について正確に理解できるようになっています。特に、どの索引作成者が利用可能であるかを明確に示すことで、ユーザーの混乱を防ぎ、適切な選択肢を提供することが意図されています。

## articles/search/search-howto-managed-identities-cosmos-db.md{#item-a74464}

<details>
<summary>Diff</summary>
````diff
@@ -10,6 +10,7 @@ ms.custom:
   - subject-rbac-steps
   - ignite-2023
   - sfi-ropc-nochange
+ai-usage: ai-assisted
 ---
 
 # Connect to Azure Cosmos DB using a managed identity (Azure AI Search)
@@ -203,5 +204,5 @@ Connection information and permissions on the remote service are validated at ru
 ## See also
 
 * [Indexing via an Azure Cosmos DB for NoSQL](search-how-to-index-cosmosdb-sql.md)
-* [Indexing via an Azure Cosmos DB for MongoDB](search-how-to-index-cosmosdb-mongodb.md)
-* [Indexing via an Azure Cosmos DB for Apache Gremlin](search-how-to-index-cosmosdb-gremlin.md)
+* [Indexing via an Azure Cosmos DB for MongoDB (preview)](search-how-to-index-cosmosdb-mongodb.md)
+* [Indexing via an Azure Cosmos DB for Apache Gremlin (preview)](search-how-to-index-cosmosdb-gremlin.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Cosmos DB管理ID接続に関する記事の更新"
}
```

### Explanation
この変更は、Azure Cosmos DBに管理IDを使用して接続する方法に関する記事において、いくつかの小さな更新を行ったものです。

具体的な変更内容は以下の通りです：
- **新しいメタデータの追加**: 記事のメタデータに「ai-usage: ai-assisted」が追加され、AIアシスタンス機能が使用されていることが明示されました。これにより、ユーザーは記事がAIによる支援を受けていることを理解できます。
- **リンクの更新**: Azure Cosmos DBのMongoDBおよびApache Gremlin用のインデクシングに関するリンクが更新され、プレビュー版であることが強調されています。具体的には、「Indexing via an Azure Cosmos DB for MongoDB」が「Indexing via an Azure Cosmos DB for MongoDB (preview)」に変更され、同様にGremlinについてもプレビュー版が明記されました。

これらの変更により、記事はより最新の状態となり、ユーザーはどの機能が試験中であるかを明確に認識できるようになりました。また、AIアシスタンスの使用が強調されていることで、技術的なガイダンスの信頼性が向上しています。全体として、記事は読者に対して一貫した情報を提供することを目指しています。

## articles/search/search-howto-managed-identities-storage.md{#item-8209c4}

<details>
<summary>Diff</summary>
````diff
@@ -10,6 +10,7 @@ ms.custom:
   - subject-rbac-steps
   - ignite-2023
   - sfi-ropc-nochange
+ai-usage: ai-assisted
 ---
 
 # Connect to Azure Storage using a managed identity (Azure AI Search)
@@ -44,7 +45,7 @@ You can use a system-assigned managed identity or a user-assigned managed identi
    | Table indexing using an indexer | Add **Storage Table Data Reader** |
    | File indexing using an indexer | Add **Reader and Data Access** |
    | Write to a [knowledge store](knowledge-store-concept-intro.md) | Add **Storage Blob Data Contributor** for object and file projections, and **Reader and Data Access** for table projections. |
-   | Write to an [enrichment cache](enrichment-cache-how-to-configure.md) | Add **Storage Blob Data Contributor** and **Storage Table Data Contributor** |
+   | Write to an [enrichment cache (preview)](enrichment-cache-how-to-configure.md) | Add **Storage Blob Data Contributor** and **Storage Table Data Contributor** |
    | Save [debug session state](cognitive-search-debug-session.md) | Add **Storage Blob Data Contributor**  |
 
 1. Select **Next**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureストレージに管理IDで接続する方法に関する記事の更新"
}
```

### Explanation
この変更は、Azureストレージに管理IDを使用して接続する方法を説明する記事に関して行われた小さな更新を含んでいます。

具体的な変更内容は以下の通りです：
- **新しいメタデータの追加**: 記事のメタデータに「ai-usage: ai-assisted」を追加しました。これにより、この文書がAI支援のコンテキストで作成されたことが強調されています。読者は、指示がAIによって強化されていることを理解することができます。
- **表の内容の更新**: 「enrichment cache」の説明に変更があり、これまでの表現「Write to an [enrichment cache]」が「Write to an [enrichment cache (preview)]」に更新されました。これにより、読者はこの機能が現在プレビュー版であることを認識できるようになります。

全体として、この変更は文書を最新の情報で更新し、読者に対して明確なガイダンスを提供することを目的としています。プレビュー版の機能に対する明示的な言及は、ユーザーに対して機能の利用状況を明らかにし、適切な期待を持たせる助けとなります。

## articles/search/search-howto-run-reset-indexers.md{#item-fb10c8}

<details>
<summary>Diff</summary>
````diff
@@ -105,7 +105,7 @@ After reset, follow with a Run command to reprocess new and existing documents.
 
 ## How to reset and run indexers
 
-Reset clears the high-water mark. All documents in the search index are flagged for full overwrite, without inline updates or merging into existing content. For indexers with a skillset and [enrichment caching](enrichment-cache-how-to-configure.md), resetting the index also implicitly resets the skillset. 
+Reset clears the high-water mark. All documents in the search index are flagged for full overwrite, without inline updates or merging into existing content. For indexers with a skillset and [enrichment caching (preview)](enrichment-cache-how-to-configure.md), resetting the index also implicitly resets the skillset. 
 
 The actual work occurs when you follow a reset with a Run command:
 
@@ -336,7 +336,7 @@ To check the reset status and see which document keys are queued for processing,
 
 ## Check indexer runtime quota for S3 HD and Serverless search services
 
-This section applies to Standard 3 High Density (S3 HD) and Serverless search services. For aggregate quota behavior and planning guidance, see [Indexer execution on Serverless and S3 HD](search-indexer-high-density-serverless-overview.md).
+This section applies to Standard 3 High Density (S3 HD) and Serverless search services. For aggregate quota behavior and planning guidance, see [Indexer execution on Serverless and S3 HD (preview)](search-indexer-high-density-serverless-overview.md).
 
 Each indexer run has a two-hour maximum. Separately, all indexers share 24 hours of cumulative runtime per service in each 24-hour UTC window.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーのリセットと実行方法に関する記事の更新"
}
```

### Explanation
この変更は、インデクサーをリセットして実行する方法に関する記事において、いくつかの小さな修正を行ったものです。

具体的な変更内容は以下の通りです：
- **リンクの更新**: 「enrichment caching」に関する言及が更新され、旧い文言「enrichment caching」が「enrichment caching (preview)」に変更されました。これにより、読者はこの機能が現在プレビュー版であることを認識できるようになり、技術的な文書の正確性が向上します。
- **リンクの更新**: 「Indexer execution on Serverless and S3 HD」という文言も同様に、「Indexer execution on Serverless and S3 HD (preview)」に修正され、プレビュー版の情報が明確に示されています。

これらの更新により、文書の内容が現行の機能状況をより正確に反映するようになっています。読者に対してプレビュー機能の認識を促すことで、適切な期待を持ってもらうことが目的です。全体として、この小さな変更によって、記事は最新の情報を提供し続けることができるようになっています。

## articles/search/search-import-data-portal.md{#item-b804d1}

<details>
<summary>Diff</summary>
````diff
@@ -48,9 +48,9 @@ The wizard connects to the following data sources through [built-in indexers](se
 | [Azure Table Storage](search-how-to-index-azure-tables.md) | ✅ | Built-in indexer |
 | [Azure SQL Database and Managed Instance](search-how-to-index-sql-database.md) | ✅ | Built-in indexer |
 | [Cosmos DB for NoSQL](search-how-to-index-cosmosdb-sql.md) | ✅ | Built-in indexer |
-| [Cosmos DB for MongoDB](search-how-to-index-cosmosdb-mongodb.md) | ✅ | Built-in indexer |
-| [Cosmos DB for Apache Gremlin](search-how-to-index-cosmosdb-gremlin.md) | ✅ | Built-in indexer |
-| [MySQL](search-how-to-index-mysql.md) | ❌ | Not applicable |
+| [Cosmos DB for MongoDB (preview)](search-how-to-index-cosmosdb-mongodb.md) | ✅ | Built-in indexer |
+| [Cosmos DB for Apache Gremlin (preview)](search-how-to-index-cosmosdb-gremlin.md) | ✅ | Built-in indexer |
+| [MySQL (preview)](search-how-to-index-mysql.md) | ❌ | Not applicable |
 | [OneDrive](search-how-to-index-logic-apps.md#supported-connectors) | ✅ | Logic Apps connector |
 | [OneDrive for Business](search-how-to-index-logic-apps.md#supported-connectors) | ✅ | Logic Apps connector |
 | [OneLake](search-how-to-index-onelake-files.md) | ✅ | Built-in indexer |
@@ -59,7 +59,7 @@ The wizard connects to the following data sources through [built-in indexers](se
 | [SQL Server on virtual machines](search-how-to-index-sql-server.md) | ✅ | Built-in indexer |
 
 > [!TIP]
-> Instead of using a Logic Apps connector for Azure File Storage or SharePoint, you can use the Search Service REST APIs to programmatically index data from these sources. For more information, see [Index data from Azure Files](search-file-storage-integration.md) and [Index data from SharePoint document libraries](search-how-to-index-sharepoint-online.md).
+> Instead of using a Logic Apps connector for Azure File Storage or SharePoint, you can use the Search Service REST APIs to programmatically index data from these sources. For more information, see [Index data from Azure Files (preview)](search-file-storage-integration.md) and [Index data from SharePoint document libraries (preview)](search-how-to-index-sharepoint-online.md).
 
 ### Skills
 
@@ -68,7 +68,7 @@ The following skills might appear in a wizard-generated skillset. After the skil
 | Skill | Supported | Description |
 |--|--|--|
 | [AML](cognitive-search-aml-skill.md) | ✅ | Available for RAG and multimodal RAG only. |
-| [Azure Vision multimodal embedding](cognitive-search-skill-vision-vectorize.md) | ✅ | Available for RAG and multimodal RAG only. |
+| [Azure Vision multimodal embedding (preview)](cognitive-search-skill-vision-vectorize.md) | ✅ | Available for RAG and multimodal RAG only. |
 | [Azure OpenAI embedding](cognitive-search-skill-azure-openai-embedding.md) | ✅ | Available for RAG and multimodal RAG only. |
 | [Document Layout](cognitive-search-skill-document-intelligence-layout.md) | ✅ | Available for RAG and multimodal RAG only. |
 | [Entity Recognition](cognitive-search-skill-entity-recognition-v3.md) | ✅ | Available for keyword search only. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データポータルのインポートに関する記事の更新"
}
```

### Explanation
この変更は、データポータルにデータをインポートする方法に関する記事に対する小規模な更新を反映しています。

具体的な変更内容は以下の通りです：
- **プレビュー情報の追加**: いくつかのデータソースとスキルに関する表現が修正され、特に「Cosmos DB for MongoDB」、「Cosmos DB for Apache Gremlin」、「MySQL」などの項目が「(preview)」という言葉を追加され、これらの機能がプレビュー版であることが明示されています。
- **リンクの改善**: リンクのテキストが更新され、プレビュー機能に関する注意喚起が強調されました。これにより、読者は最新の機能状況に基づく正しい判断ができるようになります。
- **ヒントの更新**: Azure File StorageやSharePoint用のLogic Appsコネクタに関するTIPも更新され、プレビュー版の参照を追加しました。この変更は、ユーザーがより効果的に情報を活用できるようにすることを目的としています。

これらの修正は、文書を最新の情報で更新し、読者に対して正確な情報を提供し続けるためのものです。全体として、記事はユーザーがデータポータルを使用する際の理解を深める助けとなります。

## articles/search/search-index-access-control-lists-and-rbac-push-api.md{#item-45e71e}

<details>
<summary>Diff</summary>
````diff
@@ -12,18 +12,9 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
-
-Indexing documents, along with their associated [access control lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control) and container [role-based access control (RBAC) roles](/azure/role-based-access-control/overview), into an Azure AI Search index via the [push REST APIs](/rest/api/searchservice/documents/?view=rest-searchservice-2026-08-01-preview&preserve-view=true) preserves document-level permission on indexed content at query time.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
+Document-level permission ingestion through the push REST APIs (preview) lets you index documents along with their associated [access control lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control) and container [role-based access control (RBAC) roles](/azure/role-based-access-control/overview). When you push content into an Azure AI Search index via the [push REST APIs](/rest/api/searchservice/documents/?view=rest-searchservice-2026-08-01-preview&preserve-view=true), the service preserves those permissions on indexed content and enforces them at query time.
 
 Key features include:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスアクセス制御リストとRBACに関する記事の更新"
}
```

### Explanation
この変更は、インデックスアクセス制御リスト（ACL）およびロールベースアクセス制御（RBAC）に関する記事の内容を更新しています。主な改善点は、プレビュー版APIに関する情報の整理と明確化です。

具体的な変更内容は以下の通りです：
- **情報の簡素化**: 以前の内容では、プレビューAPIに関する詳細な注意事項が長文で記載されていましたが、これが整理され、より明確な指示へと修正されました。プレビューAPIに関連するリスクや責任について、簡潔に言及されています。
- **新しい表現の追加**: 文書レベルの権限を保つために、プッシュREST APIを使用して文書とそのACLおよびRBACロールをインデックスする方法について、具体的な表現が追加され、より分かりやすくなりました。
- **重要な情報の明示化**: 新しい段落が追加され、プッシュREST APIを通じた文書のインデックス作成がどのように機能するか、特にクエリの際に権限がどのように守られるかが詳述されています。このため、読者はインデックス作成時の権限管理の仕組みを理解しやすくなります。

全体として、この変更は文書の可読性と情報の正確性を向上させることを目的としており、ユーザーがより良い理解を深めながら利用できるようになっています。

## articles/search/search-indexer-access-control-lists-and-role-based-access.md{#item-67b42f}

<details>
<summary>Diff</summary>
````diff
@@ -12,20 +12,11 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 Azure Data Lake Storage (ADLS) Gen2 supports per-user access to directories and files through [access control lists](/azure/storage/blobs/data-lake-storage-access-control-model#access-control-lists-acls) (ACLs) and [role-based access control](/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac) (Azure RBAC). [Attribute-based access control](/azure/storage/blobs/data-lake-storage-access-control-model#attribute-based-access-control-azure-abac) (Azure ABAC) isn't supported.
 
-Preview APIs in Azure AI Search can ingest this permission metadata alongside document content. Users who lack access to a directory or file in storage don't see the corresponding documents in search results. This is one of several strategies for [document-level access control](search-document-level-access-overview.md) in Azure AI Search.
+Azure AI Search can ingest this permission metadata (preview) alongside document content by using a preview REST API. Users who lack access to a directory or file in storage don't see the corresponding documents in search results. This is one of several strategies for [document-level access control](search-document-level-access-overview.md) in Azure AI Search.
 
 This article explains how to configure an ADLS Gen2 indexer or ADLS Gen2 blob knowledge source to automatically *pull* permission metadata into a search index. It supplements [Index data from ADLS Gen2](search-how-to-index-azure-data-lake-storage.md) and [Create a blob knowledge source for ADLS Gen2](agentic-knowledge-source-how-to-blob.md) with information specific to permission ingestion. To manually *push* permission metadata, see [Index document ACLs using the push API](search-index-access-control-lists-and-rbac-push-api.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーのアクセス制御リストとRBACに関する記事の更新"
}
```

### Explanation
この変更は、インデクサーのアクセス制御リストおよびロールベースアクセス（RBAC）に関連する記事に対する小規模な更新を反映しています。

主な変更点は次のとおりです：
- **プレビューAPIに関する情報の短縮**: 以前の長文から短縮され、プレビューAPIに関連する注意事項が簡潔に整理されました。これにより、ユーザーは重要な情報を迅速に把握できるようになっています。
- **文書データの取り込み方法の明示化**: 「Azure AI SearchがプレビューREST APIを使用して権限メタデータを文書コンテンツとともに取り込むことができる」という文が新たに強調され、利用者がどのようにデータを検索できるかが明確に示されています。
- **情報の流れの整理**: インデクサーの設定方法や、ADLS Gen2に関連する権限メタデータの取り込みの手順についての説明が、関連する他の文書へのリンクとともに整理されており、ドキュメントの理解が容易になっています。

全体として、この変更は読者がインデクサーの設定および権限管理に関する情報をより効率的に取得できるようにすることを目的としています。

## articles/search/search-indexer-high-density-serverless-overview.md{#item-2bc606}

<details>
<summary>Diff</summary>
````diff
@@ -9,17 +9,18 @@ ai-usage: ai-assisted
 ms.custom: doc-kit-assisted
 ---
 
-# Indexer execution on Serverless and Standard 3 High Density (S3 HD)
+# Indexer execution on Serverless and Standard 3 High Density (S3 HD) (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
 This article describes the indexer execution model that Azure AI Search uses for Serverless and Standard 3 High Density (S3 HD) search services. Both options have a service-level daily runtime quota that governs how much total indexer time you can use per 24-hour UTC window.
 
-> [!IMPORTANT]
-> The capabilities described in this article are in preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> + Indexer support on S3 HD requires the [`2025-11-01-preview` REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) or later.
-> + Serverless indexer support requires the [`2026-05-01-preview` REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or later.
+The capabilities described in this article are in preview:
+
++ Indexer support on S3 HD requires the [`2025-11-01-preview` REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) or later.
++ Serverless indexer support requires the [`2026-05-01-preview` REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-05-01-preview&preserve-view=true) or later.
 
 ## Where it applies
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスおよび標準3高密度インデクサーの概要に関する記事の更新"
}
```

### Explanation
この変更は、サーバーレスおよび標準3高密度（S3 HD）インデクサーに関する記事に対する小規模な更新を反映しています。

主な変更点は次のとおりです：
- **タイトルの更新**: 記事のタイトルに「(preview)」が追加され、現在この機能がプレビュー状態であることが明示されました。この変更により、利用者は提供される機能がまだ安定版ではないことを理解しやすくなります。
- **プレビュー関連の情報の強調**: 記事冒頭にプレビューサービスに関する情報を示すための新しいセクションが追加されました。これにより、この記事で説明される機能が現在プレビュー中であることが強調されています。
- **重要事項の整理**: プレビューAPIに関する注意事項が簡潔に整理され、各APIが必要であることが再度強調されています。これにより、必要なAPIバージョンについての情報が明確化され、開発者の理解を助けています。

全体として、この変更は読者に対して、インデクサー機能がプレビューであることをより明確にし、必要なAPIバージョンについての情報を強化することを目的としています。

## articles/search/search-indexer-howto-access-trusted-service-exception.md{#item-e19826}

<details>
<summary>Diff</summary>
````diff
@@ -9,6 +9,7 @@ ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
   - sfi-image-nochange
+ai-usage: ai-assisted
 ---
 
 # Make indexer connections to Azure Storage as a trusted service
@@ -71,7 +72,7 @@ A system-assigned managed identity is a Microsoft Entra service principal. The a
 
 1. Add **Storage Blob Data Contributor** if write access is required.
 
-   Features that require write access include [enrichment caching](enrichment-cache-how-to-configure.md), [debug sessions](cognitive-search-debug-session.md), and [knowledge store](knowledge-store-concept-intro.md).
+   Features that require write access include [enrichment caching (preview)](enrichment-cache-how-to-configure.md), [debug sessions](cognitive-search-debug-session.md), and [knowledge store](knowledge-store-concept-intro.md).
 
 ## Set up and test the connection
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "信頼されたサービス例外へのアクセスに関する記事の更新"
}
```

### Explanation
この変更は、Azure Storageに対するインデクサーの接続方法に関する記事に対する小規模な更新を反映しています。

主な変更点は次のとおりです：
- **新しいメタデータの追加**: 記事に「ai-usage: ai-assisted」というメタデータが追加されました。この変更により、記事がAIによる支援を受けていることが示され、関連するリソースや情報の信頼性が増しています。
- **特徴のプレビュー情報の明確化**: 書き込みアクセスが必要な機能のリストの中で、「enrichment caching」がプレビューであることを明記するために「(preview)」というラベルが追加されました。これにより、利用者はこの機能が現在プレビュー状態であることを理解しやすくなります。

全体として、この変更は記事の情報をより正確で明確にし、読者が機能の現状を正しく認識できるようにすることを目的としています。

## articles/search/search-indexer-overview.md{#item-292796}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.custom:
 ms.topic: concept-article
 ms.date: 06/23/2025
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Indexers in Azure AI Search
@@ -24,7 +25,7 @@ You can run indexers on demand or on a recurring data refresh schedule that runs
 A search service runs one indexer job per search unit. If you need concurrent processing, make sure you have [sufficient replicas](/azure/search/search-capacity-planning#add-or-reduce-replicas-and-partitions). Indexers don't run in the background, so you might detect more query throttling than usual if the service is under pressure.
 
 > [!NOTE]
-> Indexer execution on Standard 3 High Density (S3 HD) search services and Serverless search services follows a different model that includes a service-level daily runtime quota. For more information, see [Indexer execution on Serverless and S3 HD](search-indexer-high-density-serverless-overview.md).
+> Indexer execution on Standard 3 High Density (S3 HD) search services and Serverless search services follows a different model that includes a service-level daily runtime quota. For more information, see [Indexer execution on Serverless and S3 HD (preview)](search-indexer-high-density-serverless-overview.md).
 
 ## Indexer scenarios and use cases
 
@@ -59,11 +60,11 @@ Indexers crawl data stores on Azure and outside of Azure.
 + [Azure SQL Managed Instance](search-how-to-index-sql-managed-instance.md)
 + [Microsoft OneLake](search-how-to-index-onelake-files.md)
 + [SQL Server on Azure Virtual Machines](search-how-to-index-sql-server.md)
-+ [Azure Files](search-file-storage-integration.md) (in preview)
-+ [Azure MySQL](search-how-to-index-mysql.md) (in preview)
-+ [SharePoint in Microsoft 365](search-how-to-index-sharepoint-online.md) (in preview)
-+ [Azure Cosmos DB for MongoDB](search-how-to-index-cosmosdb-mongodb.md) (in preview)
-+ [Azure Cosmos DB for Apache Gremlin](search-how-to-index-cosmosdb-gremlin.md) (in preview)
++ [Azure Files (preview)](search-file-storage-integration.md)
++ [Azure MySQL (preview)](search-how-to-index-mysql.md)
++ [SharePoint in Microsoft 365 (preview)](search-how-to-index-sharepoint-online.md)
++ [Azure Cosmos DB for MongoDB (preview)](search-how-to-index-cosmosdb-mongodb.md)
++ [Azure Cosmos DB for Apache Gremlin (preview)](search-how-to-index-cosmosdb-gremlin.md)
 
 Azure Cosmos DB for Cassandra is not supported.
 
@@ -89,7 +90,7 @@ You can also enable image extraction during document cracking for an [extra fee]
 
 Depending on the data source, the indexer will try different operations to extract potentially indexable content:
 
-+ When the document is a file with embedded images, such as a PDF, the indexer extracts text, images, and metadata. Indexers can open files from [Azure Blob Storage](search-how-to-index-azure-blob-storage.md#supported-document-formats), [Azure Data Lake Storage Gen2](search-how-to-index-azure-data-lake-storage.md#supported-document-formats), and [SharePoint](search-how-to-index-sharepoint-online.md#supported-document-formats).
++ When the document is a file with embedded images, such as a PDF, the indexer extracts text, images, and metadata. Indexers can open files from [Azure Blob Storage](search-how-to-index-azure-blob-storage.md#supported-document-formats), [Azure Data Lake Storage Gen2](search-how-to-index-azure-data-lake-storage.md#supported-document-formats), and [SharePoint (preview)](search-how-to-index-sharepoint-online.md#supported-document-formats).
 
 + When the document is a record in [Azure SQL](search-how-to-index-sql-database.md), the indexer will extract non-binary content from each field in each record.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおけるインデクサーの概要に関する記事の更新"
}
```

### Explanation
この変更は、Azure AI Searchのインデクサーに関する概要記事に対する小規模な更新を反映しています。

主な変更点は次のとおりです：
- **新しいメタデータの追加**: 記事に「ai-usage: ai-assisted」というメタデータが追加され、AI支援を受けていることが示され、記事の関連性が向上します。
- **プレビュー情報の明確化**: 記事内の注記において、サーバーレスおよび標準3高密度（S3 HD）検索サービスのインデクサー実行がプレビューであることを明示するために「(preview)」が追加されました。この追加によって、読者に対して現行の機能がまだ確定版ではないことが強調されています。
- **いくつかのサービスのプレビュー状態の明確化**: インデクサーが対応しているデータストアのリストにおいて、複数のサービスについて「(preview)」というラベルが追加されました。これにより、これらの機能がプレビュー中であることを明確にし、利用者が期待する機能の状況を理解しやすくなります。

全体として、この変更は利用者がインデクサーの機能に関する情報をより正確に理解できるようにし、提供されるサービスの現状を透明にすることを目的としています。

## articles/search/search-indexer-securing-resources.md{#item-c075c4}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,9 @@ ms.reviewer: arjagann
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
+  - doc-kit-assisted
 ms.topic: concept-article
-ms.date: 08/31/2026
+ms.date: 09/17/2026
 ms.update-cycle: 365-days
 ai-usage: ai-assisted
 ---
@@ -31,17 +32,19 @@ A list of all possible Azure resource types that an indexer might access in a ty
 
 | Resource | Purpose within indexer run |
 | --- | --- |
-| Azure Storage (blobs, ADLS Gen 2, files, tables) | Data source |
+| Azure Storage (blobs, ADLS Gen2, files, tables) | Data source |
 | Azure Storage (blobs, tables) | Skillsets (caching enrichments, debug sessions, knowledge store projections) |
 | Azure Cosmos DB (various APIs) | Data source |
 | Azure SQL Database | Data source |
 | Microsoft OneLake | Data source |
 | SQL Server on Azure virtual machines | Data source |
 | SQL Managed Instance | Data source |
 | Azure Functions | Attached to a skillset and used to host for custom web API skills |
+| Azure OpenAI | Embedding and model skill execution |
+| Microsoft Foundry | Model skill execution and keyless billing for built-in skills |
 
 > [!NOTE]
-> An indexer also connects to Foundry Tools for built-in skills. However, that connection is made over the internal network and isn't subject to any network provisions under your control.
+> Azure AI Search internally hosts processing for most built-in skills that are billed through Foundry Tools. For keyless billing, the skillset makes a separate outbound connection to the attached Foundry resource. If public network access is disabled on the Foundry resource, configure a shared private link for the billing connection. For configuration details, see [Supported resource types](search-indexer-howto-access-private.md#supported-resource-types).
 
 Indexers connect to resources using the following approaches:
 
@@ -58,15 +61,16 @@ Your Azure resources could be protected using any number of the network isolatio
 
 | Resource | IP restriction | Private endpoint |
 | --- | --- | ---- |
-| Azure Storage for text-based indexing (blobs, ADLS Gen 2, files, tables) | Supported only if the storage account and search service are in different regions. | Supported |
+| Azure Storage for text-based indexing (blobs, ADLS Gen2, files, tables) | Supported only if the storage account and search service are in different regions. | Supported |
 | Azure Storage for AI enrichment (caching, debug sessions, knowledge store) | Supported only if the storage account and search service are in different regions. | Supported |
 | Azure Cosmos DB for NoSQL | Supported | Supported |
 | Azure Cosmos DB for MongoDB | Supported | Unsupported |
 | Azure Cosmos DB for Apache Gremlin | Supported | Unsupported |
 | Azure SQL Database | Supported | Supported |
 | SQL Server on Azure virtual machines | Supported | N/A |
 | SQL Managed Instance | Supported | N/A |
-| Azure Functions | Supported | Supported, only for certain tiers of Azure functions |
+| Azure Functions | Supported | Supported only for certain tiers of Azure Functions. |
+| Azure OpenAI or Microsoft Foundry | Supported | Supported with limitations. See [Supported resource types](search-indexer-howto-access-private.md#supported-resource-types). |
 
 ## Network access and indexer execution environments
 
@@ -76,8 +80,8 @@ For any given indexer run, Azure AI Search determines the best environment in wh
 
 | Execution environment | Description |
 |-----------------------|-------------|
-| Private <sup>1</sup> | Internal to a search service. Indexers running in the private environment share computing resources with other indexing and query workloads on the same search service. If you set up a private connection between an indexer and your data, such as a shared private link, this is the only execution environment you can use and it's used automatically. |
-|  multitenant | Managed and secured by Microsoft at no extra cost. It isn't subject to any network provisions under your control. This environment is used to offload computationally intensive processing, leaving service-specific resources available for routine operations. Examples of resource-intensive indexer jobs include skillsets, processing large documents, or processing a high volume of documents. |
+| Private <sup>1</sup> | Internal to a search service. Indexers running in the private environment share computing resources with other indexing and query workloads on the same search service. Only the private execution environment can use a shared private link. To use this connection, explicitly set `executionEnvironment` to `private` on the indexer. Automatic selection isn't guaranteed. For more information, see [Considerations for using a private endpoint](#considerations-for-using-a-private-endpoint). |
+| Multitenant | Managed and secured by Microsoft at no extra cost. It isn't subject to any network provisions under your control. This environment is used to offload computationally intensive processing, leaving service-specific resources available for routine operations. Examples of resource-intensive indexer jobs include skillsets, processing large documents, or processing a high volume of documents. |
 
 
 <sup>1</sup> To prevent heavy load on the private execution environment, indexers with more than two Azure OpenAI Embedding or Azure Vision multimodal embeddings skills are restricted from running in this environment.
@@ -135,7 +139,7 @@ This section narrows in on the private connection option.
 
 - Requires that you turn off the multitenant execution environment for the indexer.
 
-  You do this by setting the `executionEnvironment` of the indexer to `"Private"`. This step ensures that all indexer execution is confined to the private environment provisioned within the search service. This setting is scoped to an indexer and not the search service. If you want all indexers to connect over private endpoints, each one must have the following configuration:
+  You do this by setting the `executionEnvironment` of the indexer to `"private"`. This step ensures that all indexer execution is confined to the private environment provisioned within the search service. This setting is scoped to an indexer and not the search service. If you want all indexers to connect over private endpoints, each one must have the following configuration:
   
   ```json
       {
@@ -145,7 +149,7 @@ This section narrows in on the private connection option.
             ... other parameters
             "configuration" : {
               ... other configuration properties
-              "executionEnvironment": "Private"
+              "executionEnvironment": "private"
             }
           }
       }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースのセキュリティ確保に関するインデクサーの記事の更新"
}
```

### Explanation
この変更は、Azureのリソースを保護するためのインデクサーに関する記事における小規模な更新を反映しています。

主な変更点は次のとおりです：
- **新しいメタデータの追加**: 記事に「doc-kit-assisted」という新しいメタデータが追加され、文書作成の支援を示しています。また、更新日が「2026年9月17日」に変更されました。
- **リソースの詳細情報の追加**: インデクサーがアクセスする可能性のあるリソースのリストに「Azure OpenAI」と「Microsoft Foundry」が追加され、それぞれの役割が明確化されました。これにより、インデクサーが使用するリソースの範囲が広がり、機能の理解が深まります。
- **内部処理に関する明記の変更**: 内部ネットワークを通じてFoundry Toolsに接続する方法についての説明が拡充され、請求に関する詳細が強調されました。特に、プライベートリンクの構成に関する情報が追加され、ネットワークアクセスの制御についての理解を助けます。
- **実行環境セクションの明確化**: プライベートおよびマルチテナントの実行環境についての説明が詳細化され、特にプライベートエンドポイントとの接続方法における要件が明記されました。

この変更は、Azureのインデクサーを利用する際のリソースのセキュリティと接続方法をより明確にし、利用者がそれぞれの機能をより深く理解できるようにすることを目的としています。

## articles/search/search-indexer-sensitivity-labels.md{#item-2a7bfc}

<details>
<summary>Diff</summary>
````diff
@@ -12,26 +12,15 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag occurs before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data flows outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This responsibility includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
-
-Azure AI Search supports automatic extraction of [Microsoft Purview sensitivity labels](/purview/sensitivity-labels) at document level during indexing, with label-based access control enforced at query time. Available in preview, this feature enables organizations to align search experiences with existing [information protection policies](/purview/create-sensitivity-labels) defined in Microsoft Purview.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-With sensitivity label indexing, Azure AI Search extracts and stores metadata that describes each document's sensitivity level. It also enforces label-based access control, ensuring that only authorized users can view or retrieve labeled content in search results.
+Azure AI Search supports [Microsoft Purview sensitivity label](/purview/sensitivity-labels) extraction and query-time enforcement (preview). During indexing, it automatically extracts and stores sensitivity label metadata for each document. At query time, it enforces label-based access control according to existing [information protection policies](/purview/create-sensitivity-labels) in Microsoft Purview, ensuring that only authorized users can retrieve labeled content in search results.
 
 This functionality is available for the following data sources:
 
 + [Azure Blob Storage](search-how-to-index-azure-blob-storage.md)
 + [Azure Data Lake Storage Gen2](search-how-to-index-azure-data-lake-storage.md)
-+ [SharePoint in Microsoft 365 (Preview)](search-how-to-index-sharepoint-online.md)
++ [SharePoint in Microsoft 365 (preview)](search-how-to-index-sharepoint-online.md)
 + [Microsoft OneLake](search-how-to-index-onelake-files.md)
 
 :::image type="content" source="media/search-indexer-sensitivity-labels/sensitivity-label-rag-architecture.png" alt-text="Architecture diagram showing a governed RAG solution where documents labeled with Microsoft Purview sensitivity labels are indexed into Azure AI Search, and a RAG orchestrator filters query results by label so junior users see only General content while executive users see General, Confidential, and Highly Confidential content." lightbox="media/search-indexer-sensitivity-labels/sensitivity-label-rag-architecture.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "感度ラベルに関するインデクサーの記事の更新"
}
```

### Explanation
この変更は、Azure AI Searchの感度ラベルに関するインデクサーの記事における小規模な更新を反映しています。

主な変更点は次のとおりです：
- **注意事項の簡略化**: 記事内にあった重要な注意事項が一部削除され、情報が簡潔化されました。具体的には、プレビューAPIに関連する詳細なライセンスや運用の注意点が簡略化され、[!INCLUDE]構文を使った他のテンプレートも含まれるようになりました。
- **機能説明の改良**: 感度ラベルの自動抽出機能とクエリ時のアクセス制御の強化に関する説明が更新され、より明確に機能が記載されています。特に、Microsoft Purviewの感度ラベルを使用した冗長な表現や情報が削除され、機能の要点がより強調されています。
- **データソースリストの更新**: データソースのリストにおいて、「SharePoint in Microsoft 365」のプレビュー表記の形式が統一されました。この修正は、ユーザビリティ向上を目的としています。

全体として、この変更は、感度ラベルに関する機能の理解を促進し、読者に対して重要情報を明確に伝えることを目的としています。

## articles/search/search-indexer-sharepoint-access-control-lists.md{#item-532a24}

<details>
<summary>Diff</summary>
````diff
@@ -13,18 +13,9 @@ ms.custom: doc-kit-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-This article explains how to ingest an access control list (ACL) alongside other content from SharePoint in Microsoft 365 using an Azure AI Search indexer. Permissions from SharePoint are preserved as permission metadata for each indexed document. When users query an index containing content from SharePoint, their search results consist of only those documents for which they have permission to access.
+SharePoint permission metadata ingestion (preview) uses an Azure AI Search indexer to preserve permission metadata, such as access control lists (ACLs), alongside other content from SharePoint in Microsoft 365. The indexer stores the permissions as metadata on each indexed document. At query time, users receive only documents they have permission to access.
 
 :::image type="content" source="media/search-indexer-sharepoint-access-control-lists/security-trimmed-rag-sharepoint.png" alt-text="Architecture diagram showing a security-trimmed RAG solution where a SharePoint indexer ingests documents and ACL permission metadata from a SharePoint site, stores them in an Azure AI Search index, and a RAG orchestrator filters query results so each user retrieves only documents they're authorized to access." lightbox="media/search-indexer-sharepoint-access-control-lists/security-trimmed-rag-sharepoint.png":::
 
@@ -300,7 +291,7 @@ If you enabled ACL ingestion on an existing indexer that already indexed items,
 To confirm ACL values populated correctly:
 
 1. Temporarily set `retrievable` to `true` on `UserIds` and `GroupIds` in your index definition. Changing `retrievable` doesn't require an index rebuild.
-1. Run an [elevated-read query](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results) that selects `UserIds` and `GroupIds`, and confirm the collections aren't empty. For chunked scenarios, confirm every chunk carries both fields.
+1. Run an [elevated-read query](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results-preview) that selects `UserIds` and `GroupIds`, and confirm the collections aren't empty. For chunked scenarios, confirm every chunk carries both fields.
 1. Return `retrievable` to `false` after verification.
 
 ## Configure SharePoint groups support
@@ -374,7 +365,7 @@ For the request shape, see the [general query example](search-query-access-contr
 
 ### 5. Verify
 
-To confirm SharePoint group IDs landed in the index, run an [elevated-read query](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results) that selects `GroupIds` and look for `spg:`-prefixed values in the response.
+To confirm SharePoint group IDs landed in the index, run an [elevated-read query](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results-preview) that selects `GroupIds` and look for `spg:`-prefixed values in the response.
 
 ## Synchronize permissions between indexed and source content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint アクセス制御リストに関するインデクサーの記事の更新"
}
```

### Explanation
この変更は、SharePointのアクセス制御リストに関連するAzure AI Searchインデクサーの記事における小規模な更新を反映しています。

主な変更点は次のとおりです：
- **重要事項の簡略化**: 記事内にあった重要な注意事項が大幅に削除され、情報が整理されました。ただし、[!INCLUDE]構文を通じてプレビュー関連の用語が追加され、整合性が向上しています。
- **機能説明の改良**: SharePointからのACL（アクセス制御リスト）を取り込む過程がより明確になり、パーミッションメタデータがどのように保管されるかが簡潔に説明されています。特に、ユーザーがクエリを実行した際に、アクセス権限に基づく結果のみが表示される点が強調されています。
- **クエリに関するハイパーリンクの更新**: アクセス制御の確認方法に関するハイパーリンクが、以前のものから新しいプレビューバージョンのものに変更されました。これにより、最新情報へのリンクが提供されています。

全体的に、この更新は、SharePointアクセス制御リストに関する情報の整理と、機能の利用方法をより理解しやすくすることを目的としています。

## articles/search/search-indexer-troubleshooting.md{#item-087365}

<details>
<summary>Diff</summary>
````diff
@@ -3,9 +3,11 @@ title: Indexer Troubleshooting
 description: Provides indexer problem and resolution guidance for cases when no error messages are returned from the service search.
 ms.reviewer: gimondra
 ms.service: azure-ai-search
+ms.custom: doc-kit-assisted
 ms.topic: troubleshooting-general
-ms.date: 07/07/2026
+ms.date: 09/17/2026
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Indexer troubleshooting guidance for Azure AI Search
@@ -48,6 +50,16 @@ This error occurs if you [configured a shared private link](search-indexer-howto
 
 If the Foundry resource isn't in the same region as Azure AI Search, [use a keyless connection](cognitive-search-attach-cognitive-services.md) to attach the resource.
 
+### Error using a shared private link
+
+If you get error code 403 with the following message, the indexer might be connecting through the public endpoint instead of an approved shared private link:
+
+```output
+Unexpected error validating provided resource. {"error":{"code":"403","message":"Public access is disabled. Please configure private endpoint."}}
+```
+
+This error can occur when the indexer isn't configured to use the private execution environment. Confirm that the shared private link is approved, set the indexer's `executionEnvironment` to `private`, and verify that the connection uses the correct resource endpoint and [group ID](search-indexer-howto-access-private.md#supported-resource-types).
+
 ### Firewall rules
 
 Azure Storage, Azure Cosmos DB, and Azure SQL provide a configurable firewall. There's no specific error message when the firewall blocks the request. Typically, firewall errors are generic. Some common errors include:
@@ -255,7 +267,7 @@ An indexer might show a different document count than either the data source, th
 Indexers use a conservative buffering strategy to ensure that every new and changed document in the data source is picked up during indexing. In certain situations, these buffers can overlap, causing an indexer to index a document two or more times. As a result, the processed documents count is more than the actual number of documents in the data source. This behavior doesn't affect the data stored in the index, such as duplicating documents, only that it can take longer to reach eventual consistency. This condition is especially prevalent if any of the following criteria are true:
 
 - On-demand indexer requests are issued in quick succession.
-- The data source's topology includes multiple replicas and partitions (one such example is discussed [here](/azure/cosmos-db/consistency-levels)).
+- The data source's topology includes multiple replicas and partitions, such as the topology described in [Consistency levels in Azure Cosmos DB](/azure/cosmos-db/consistency-levels).
 - The data source is an Azure SQL database and the column chosen as "high water mark" is of type `datetime2`.
 
 Indexers aren't intended to be invoked multiple times in quick succession. If you need updates quickly, the supported approach is to push updates to the index while simultaneously updating the data source. For on-demand processing, pace your requests in five-minute intervals or more, and run the indexer on a schedule.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサートラブルシューティングガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchのインデクサーに関するトラブルシューティングガイドの記事における小規模な更新を反映しています。

主な変更点は次のとおりです：
- **メタデータの追加**: `ms.custom`と`ai-usage`という新しいメタデータフィールドが追加され、文書の目的や使用方法をより明確にしています。
- **日付の更新**: 記事の日付が「07/07/2026」から「09/17/2026」に変更され、最新の情報に基づくことを示しています。
- **新しいエラーメッセージのセクション追加**: 404エラーの原因となる「共有プライベートリンク」を使用している場合の具体的なエラーメッセージのセクションが追加され、どのようにトラブルシューティングを行うべきかが説明されています。この内容には、エラーコードや具体的な解決策が含まれています。
- **用語の整理**: 「データソースのトポロジー」に関する説明が明確になり、具体的な引用先リンクが更新されました。これにより、読者が関連情報を見つけやすくなっています。

全体として、この更新は、読者がインデクサーのトラブルシューティングにおいて直面する可能性のある特定の問題に対する理解を深め、解決策を提供することを目的としています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,7 @@ Maximum limits on storage, workloads, and quantities of indexes and other object
 Azure AI Search supports two pricing models, each with associated service tiers. The tier you select impacts the service limits outlined in this guidance.
 
 - **Dedicated**: Fixed pricing measured by Search Units (SUs). Service tier options include: Basic, Standard (S1-S3, including S3 HD), Storage Optimized (L1-L2), and a Free tier with limited search service capabilities.
-- **Serverless (Preview)**: Consumption-based pricing measured by Compute Units per hour (CU/hr) and per-GB/month for indexed storage. The current preview tier is: Serverless Developer. Limits are defined by per-index caps, per-service object counts, and Serverless throttling behavior. 
+- **Serverless (preview)**: Consumption-based pricing measured by Compute Units per hour (CU/hr) and per-GB/month for indexed storage. The current preview tier is: Serverless Developer. Limits are defined by per-index caps, per-service object counts, and Serverless throttling behavior.
 
 [!INCLUDE [Serverless preview](./includes/previews/preview-serverless.md)]
 
@@ -134,7 +134,7 @@ This table shows the progression of storage quota increases in GB over time. Sta
 
 <sup>4</sup> An upper limit exists for elements because having a large number of them significantly increases the storage required for your index. An element of a complex collection is defined as a member of that collection. For example, assume a [Hotel document with a Rooms complex collection](search-howto-complex-data-types.md#complex-collection-limits). Each room in the Rooms collection is considered an element. During indexing, the indexing engine can safely process a maximum of 3,000 elements across the document as a whole. [This limit](search-api-migration.md#upgrade-to-2019-05-06) was introduced in `api-version=2019-05-06` and applies to complex collections only, and not to string collections or to complex fields.
 
-<sup>5</sup> For most tiers, the maximum index size is the total available storage on your search service. For S2, S3, and S3 HD services with multiple partitions, and therefore more storage, the maximum size of a single index is provided in the table. Applies to search services created after April 3, 2024. Indexes for services set up with the Serverless model (Preview) have a set maximum size provided in the table.
+<sup>5</sup> For most tiers, the maximum index size is the total available storage on your search service. For S2, S3, and S3 HD services with multiple partitions, and therefore more storage, the maximum size of a single index is provided in the table. Applies to search services created after April 3, 2024. Indexes for services set up with the Serverless model (preview) have a set maximum size provided in the table.
 
 You might find some variation in maximum limits if your service happens to be provisioned on a more powerful cluster. The limits here represent the common denominator. Indexes built to the above specifications are portable across equivalent service tiers in any region.
 
@@ -242,7 +242,7 @@ Maximum running times exist to provide balance and stability to the service as a
 
 <sup>5</sup> Regarding the 2 or 24 hour maximum duration for indexers: a 2-hour maximum is the most common and it's what you should plan for. It refers to indexers that run in the [public environment](search-howto-run-reset-indexers.md#indexer-execution-environment), which offloads computationally intensive processing and leaves more resources for queries. The 24-hour limit applies if you configure the indexer to run in a private environment using only the infrastructure that's allocated to your search service. Some older indexers are incapable of running in the public environment, and those indexers always have a 24-hour processing range. If you have unscheduled indexers that run continuously for 24 hours, you can assume those indexers couldn't be migrated to the newer infrastructure. As a general rule, for indexing jobs that can't finish within two hours, put the indexer on a [5-minute schedule](search-howto-schedule-indexers.md) so that the indexer can quickly pick up where it left off. On the Free tier, the 3-10 minute maximum running time is for indexers with skillsets.
 
-<sup>6</sup> On S3 HD and Serverless services, all indexers share 24 hours of cumulative runtime per service in each 24-hour UTC window. For quota behavior, monitoring, and planning guidance, see [Indexer execution on Serverless and S3 HD](search-indexer-high-density-serverless-overview.md).
+<sup>6</sup> On S3 HD and Serverless services, all indexers share 24 hours of cumulative runtime per service in each 24-hour UTC window. For quota behavior, monitoring, and planning guidance, see [Indexer execution on Serverless and S3 HD (preview)](search-indexer-high-density-serverless-overview.md).
 
 ### Source-file limits for blob-like indexers
 
@@ -314,7 +314,7 @@ The maximum number of [index aliases](search-how-to-alias.md) varies by tier and
 
 ## Agentic retrieval limits
 
-A [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) specifies one or more [knowledge sources](agentic-knowledge-source-overview.md) and a [retrieval reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) that controls the level of large language model (LLM) processing for [agentic retrieval](agentic-retrieval-overview.md). Limits vary by pricing tier, API version, and reasoning effort level.
+A [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) specifies one or more [knowledge sources](agentic-knowledge-source-overview.md) and a [retrieval reasoning effort (preview)](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md) that controls the level of large language model (LLM) processing for [agentic retrieval](agentic-retrieval-overview.md). Limits vary by pricing tier, API version, and reasoning effort level.
 
 | Resource | Free | Basic | S1 | S2 | S3 | S3 HD | L1 | L2 | Serverless Developer |
 |--|--|--|--|--|--|--|--|--|--|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索制限・クォータ・キャパシティに関するガイドの更新"
}
```

### Explanation
この変更は、Azure AI Searchの検索制限、クォータ、およびキャパシティに関する記事における小規模な更新を反映しています。

主な変更点は次のとおりです：
- **用語の統一**: "Serverless (Preview)"から"Serverless (preview)"に表記が統一され、整合性が保たれています。
- **エラーメッセージ内の注釈更新**: サーバーレスモデルの制限や、インデックスの最大サイズに関する注釈が更新され、プレビュー版の内容がより明確に示されています。
- **プレビュードキュメントのハイパーリンク**: サーバーレスおよびS3 HDサービスに関連するインデクサーの挙動のガイドに対するリンクが更新され、プレビュー対象の情報が強調されています。
- **文言の整然化**: 文章内での説明がより理解しやすくなるように、いくつかの表現が改善されています。

この更新は、Azure AI Searchのユーザーにとって、サービス制限及びクォータの理解を助け、最新の情報に基づく利用を促進することを目的としています。

## articles/search/search-more-like-this.md{#item-56c565}

<details>
<summary>Diff</summary>
````diff
@@ -7,16 +7,16 @@ ms.custom:
 ms.topic: concept-article
 ms.date: 02/19/2026
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
-# moreLikeThis in Azure AI Search
+# moreLikeThis in Azure AI Search (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT] 
-> This feature is in preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [preview REST API](/rest/api/searchservice/index-preview) supports this feature.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-`moreLikeThis=[key]` is a query parameter in the [Search Documents API](/rest/api/searchservice/documents/search-post) that finds documents similar to the document specified by the document key. When a search request is made with `moreLikeThis`, a query is generated with search terms extracted from the given document that describe that document best. The generated query is then used to make the search request. The `moreLikeThis` parameter can't be used with the search parameter, `search=[string]`.
+The `moreLikeThis` query parameter (preview), specified as `moreLikeThis=[key]` in the [Search Documents API](/rest/api/searchservice/documents/search-post), finds documents similar to a source document identified by its key. When a search request includes `moreLikeThis`, Azure AI Search generates a query from the terms that best describe the source document. You can't combine `moreLikeThis` with `search=[string]`.
 
 By default, the contents of all top-level searchable fields are considered. If you want to specify particular fields instead, you can use the `searchFields` parameter. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "moreLikeThis機能のプレビューメッセージの更新"
}
```

### Explanation
この変更は、Azure AI Searchの「moreLikeThis」機能に関する記事における小規模な更新を反映しています。

主な変更点は以下の通りです：
- **プレビューの強調**: タイトルに「(preview)」が追加され、この機能がプレビュー版であることが明示されています。
- **重要な情報の整備**: プレビュー機能に関する注意事項が、直接的なテキストからインクルードファイルを通じての参照に変更され、情報の一貫性が向上しました。
- **クエリパラメータの説明の更新**: `moreLikeThis` パラメータの説明が若干改訂され、文書キーによって識別されたソース文書に類似した文書を検索する方法がより明確になっています。また、クエリ生成の仕組みがわかりやすく説明されています。
- **用語の明確化**: 検索のデフォルト動作に関する記述が一部改善され、どのフィールドが対象となるのかを明確にしました。

全体として、この更新はユーザーに対して「moreLikeThis」機能の使用方法やプレビューの性質を明確にし、機能の理解を深めることを目的としています。

## articles/search/search-pagination-page-layout.md{#item-115902}

<details>
<summary>Diff</summary>
````diff
@@ -89,7 +89,7 @@ The default page size is 50, while the maximum page size is 1,000. If you specif
 
 The top matches are determined by search score, assuming the query is full-text search or semantic. Otherwise, the top matches are an arbitrary order for exact match queries (where uniform `@search.score=1.0` indicates arbitrary ranking).
 
-Set `top` to override the default of 50. In newer preview APIs, if you're using a hybrid query, you can [specify maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) to return up to 10,000 documents.
+Set `top` to override the default of 50. In newer preview APIs, if you're using a hybrid query, you can [specify maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview) to return up to 10,000 documents.
 
 To control the paging of all documents returned in a result set, use `top` and `skip` together. This query returns the first set of 15 matching documents plus a count of total matches.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ページネーションに関するAPIの更新"
}
```

### Explanation
この変更は、Azure AI Searchのページネーションに関する記事における小規模な更新を反映しています。

主な変更点は次のとおりです：
- **ハイパーリンクの更新**: `maxTextRecallSize` パラメータを指定するためのハイパーリンクが改善されており、プレビュー版の情報への直接的なリンクが提供されています。これにより、ユーザーは最新の情報を容易に参照できるようになっています。
  
この更新は、Azure AI Searchのページネーション機能の利用に関する理解を深め、特に新しいプレビューAPIでの機能強化についての情報をより分かりやすくしています。ユーザーが正確で最新の情報にアクセスできるようサポートすることが目的です。

## articles/search/search-preview-terms.md{#item-4fe0af}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Azure AI Search Preview Terms
 description: Review the supplemental preview terms that apply to features, capabilities, and properties marked (preview) in the Azure AI Search documentation.
 ms.service: azure-ai-search
 ms.topic: legal
-ms.date: 07/29/2026
+ms.date: 08/24/2026
 ai-usage: ai-assisted
 ---
 
@@ -13,8 +13,6 @@ ai-usage: ai-assisted
 
 Azure AI Search releases some features, capabilities, and properties in preview. In the documentation, this functionality is marked (preview). Preview functionality, whether standalone or part of a generally available feature, isn't covered by a service-level agreement, isn't recommended for production workloads, and might change or be constrained before it becomes generally available.
 
-The terms in this article are based on the most recent data plane preview, the `2026-08-01-preview` [Search Service REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true). Depending on the preview version and functionality, some terms might not apply. Nevertheless, you're still responsible for complying with all applicable terms.
-
 ## Licensing and preview terms
 
 Preview features and functionality are licensed to you as part of your Azure subscription and are subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
@@ -33,6 +31,10 @@ Preview features can't modify access permissions that were set outside of Azure
 
 You can use some preview features to enable CORS, which allows browser-based applications to request data directly from the service. Depending on your CORS configuration, external webpages might access or invoke the service and its data by using the user's browser context, which can create security risks. Enabling CORS is at your own risk.
 
+## Model Context Protocol (MCP) security
+
+MCP implementations are susceptible to risks, such as attacks, cascading failures, and loss of human oversight. You can mitigate these risks by vetting MCP servers for security and reliability, following [Microsoft's recommended practices](/azure/api-management/secure-mcp-servers) and [industry best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices), and implementing approval mechanisms and monitoring cascading behaviors.
+
 ## Responsible AI and application testing
 
 You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビューロゴと関連するセキュリティ項目の更新"
}
```

### Explanation
この変更は、Azure AI Searchのプレビューロゴに関する記事の内容を更新するものです。

主な変更点は以下の通りです：
- **日付の更新**: ドキュメントの日付が変更され、新しい日付「08/24/2026」が反映されています。
- **説明文の整備**: プレビュー機能に関する説明が整理され、利用者が留意すべき点が明確になりました。
- **新セクションの追加**: 「Model Context Protocol (MCP) security」という新しいセクションが追加され、MCPの実装におけるリスクやその緩和策について説明されています。これにより、ユーザーがセキュリティリスクを理解し、適切な対策を講じる助けとなる情報が提供されています。

この更新により、ユーザーはAzure AI Searchのプレビュー機能に関する法的およびセキュリティ関連の重要な情報を最新の状態で把握できるようになります。

## articles/search/search-query-access-control-rbac-enforcement.md{#item-d24df7}

<details>
<summary>Diff</summary>
````diff
@@ -13,18 +13,9 @@ ms.custom: doc-kit-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
-
-Query-time access control ensures that users only retrieve search results they're authorized to access, based on their identity, group memberships, roles, or attributes. This functionality is essential for secure enterprise search and compliance-driven workflows.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
+Query-time access control (preview) ensures that users only retrieve search results they're authorized to access, based on their identity, group memberships, roles, or attributes. This functionality is essential for secure enterprise search and compliance-driven workflows.
 
 Authorized access depends on permission metadata that's ingested during indexing. For indexer data sources that have built-in access models, such as Azure Data Lake Storage (ADLS) Gen2 and SharePoint in Microsoft 365, an indexer can pull in the permission metadata for each document automatically. For other data sources, you must assemble the document payload yourself, and the payload must include both content and the associated permission metadata. You then use the [push APIs](search-index-access-control-lists-and-rbac-push-api.md) to load the index.
 
@@ -151,9 +142,7 @@ Content-Type: application/json
 > [!NOTE]
 > If the query token is omitted, only public documents accessible to everyone are returned in the query request.
 
-## Elevated permissions for investigating incorrect results
-
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+## Elevated permissions for investigating incorrect results (preview)
 
 Debugging queries that include permission metadata can be problematic because search results are specific to each user. As a developer or administrator, you might need elevated permissions to return results regardless of the permission metadata so that you can investigate problems with queries returning unauthorized content.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリのアクセス制御に関する内容の更新"
}
```

### Explanation
この変更は、Azure AI Searchのクエリアクセス制御に関連するドキュメントにおける小規模な更新を示しています。

主な変更点は次の通りです：
- **情報の整理**: プレビューフィーチャーに関する情報が新しい形式で整理され、関連するバナーが含まれるようになりました。このバナーを通じて、ユーザーはプレビュー用の条件に関する重要な情報にアクセスできるようになっています。
- **説明文の簡素化**: 大規模な削除が行われ、情報が簡潔にまとめられています。特に、プレビューAPIの使用に関する責任やセキュリティについての重要な注意点が強調されています。
- **クエリ時のアクセス制御の明確化**: クエリ時のアクセス制御機能が明確に説明され、ユーザーが自分の身元や属性に基づいて適切な検索結果を取得できることが強調されています。

これにより、ユーザーがAzure AI Searchのアクセス制御機能をよりよく理解し、適切に利用するための情報が提供されています。

## articles/search/search-query-overview.md{#item-dcd5d6}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,7 @@ Azure AI Search supports query constructs for a broad range of scenarios, from f
 | [Full-text search](search-lucene-query-architecture.md) | Inverted indexes of tokenized terms. | Full-text queries iterate over inverted indexes that are structured for fast scans, where a match can be found in potentially any field, within any number of search documents. Text is analyzed and tokenized for full-text search.|
 | [Vector search](vector-search-overview.md) | Vector indexes of generated embeddings. | Vector queries iterate over vector fields in a search index. |
 | [Hybrid search](hybrid-search-overview.md) | All of the above in a single search index. | Combines text search and vector search in a single query request. Text search works on plain-text content in searchable fields. Filters apply to filterable fields. Vector search works on vector fields. |
-| [Agentic retrieval (preview)](agentic-retrieval-overview.md) | All of the above in a single search index. | This is an alternative retrieval path on Azure AI Search that leverages large language models for query planning. The response is designed for agent consumption, where the agent rather than search app client code coordinates the response delivered to the user. |
+| [Agentic retrieval](agentic-retrieval-overview.md) | All of the above in a single search index. | This is an alternative retrieval path on Azure AI Search that optionally uses large language models for query planning (preview). The response is designed for agent consumption, where the agent rather than search app client code coordinates the response delivered to the user. |
 | Others | Plain text and human-readable content.| Raw content, extracted verbatim from source documents, supporting filters and pattern matching queries like geo-spatial search, fuzzy search, and fielded search. |
 
 The remainder of this article brings focus to the last category: classic queries that work on plain text and human-readable content, extracted intact from original source, used for filters and other specialized query forms. If you're creating a traditional search application that isn't using AI, this section explains the query methods that you can implement in your client code.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティック検索のプレビュー状態の説明を更新"
}
```

### Explanation
この変更は、Azure AI Searchのクエリオーバービューに関するドキュメントの小規模な修正を示しています。

主な変更点は次の通りです：
- **エージェンティック検索の表記変更**: 「Agentic retrieval (preview)」から「Agentic retrieval」に変更され、説明文に「(preview)」という注釈が追加されています。これにより、ユーザーはこの機能がプレビュー版であることを理解しつつ、エージェンティック検索が大規模言語モデルを利用したクエリ計画をオプションとして提供することを明確に認識できます。
- **簡潔な表現**: 全体として、エージェンティック検索の説明が明瞭になり、機能の概要と意図される利用方法がよりわかりやすくなっています。

これにより、読者はAzure AI Searchにおけるエージェンティック検索の利用可能性とその特長をより効果的に理解できるようになります。

## articles/search/search-query-sensitivity-labels.md{#item-3e1f8a}

<details>
<summary>Diff</summary>
````diff
@@ -12,18 +12,9 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag occurs before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data flows outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This responsibility includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
-
-At query time, Azure AI Search can enforce sensitivity label policies defined in [Microsoft Purview](/purview/create-sensitivity-labels). These policies include the evaluation of [`EXTRACT` usage rights](/purview/rights-management-usage-rights) associated with each document, ensuring users can only retrieve documents they're permitted to access.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
+At query time, Azure AI Search can enforce sensitivity label policies (preview) defined in [Microsoft Purview](/purview/create-sensitivity-labels). These policies include the evaluation of [`EXTRACT` usage rights](/purview/rights-management-usage-rights) associated with each document, ensuring users can only retrieve documents they're permitted to access.
 
 This capability extends [document-level access control](search-document-level-access-overview.md) to align with your organization's [information protection and compliance requirements](/purview/create-sensitivity-labels) managed in Microsoft Purview.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "感度ラベルポリシーに関する説明の更新"
}
```

### Explanation
この変更は、Azure AI Searchのクエリ感度ラベルに関するドキュメントの内容に対する小規模な修正を示しています。

主な変更点は次の通りです：
- **プレビュー用の注釈の追加**: 「感度ラベルポリシー (preview)」という表現が追加され、これによりユーザーはこの機能が現在プレビュー版であることを明確に理解できるようになります。これは、機能のニュアンスを明確にし、ユーザーの期待を調整します。
- **説明文の整理**: 重要な警告メッセージが削除され、代わりにプレビューテクノロジーに関する文書が統合されました。この変更は、情報を簡略化し、より関連性のある内容へ焦点を絞る手助けになります。
- **内容の明確化**: 感度ラベルポリシーがMicrosoft Purviewで定義され、この評価がどのようにユーザーの文書アクセスに影響を与えるかがより明確に説明されています。

これにより、ドキュメントが簡潔で理解しやすくなり、読者が感度ラベルポリシーの目的と適用についてよりよく理解できるようになります。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -16,8 +16,6 @@ ms.custom:
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
-
 This article identifies the cloud regions in which Azure AI Search is available. It also lists which premium features are available in each region.
 
 ## Features subject to regional availability
@@ -63,7 +61,7 @@ You can create an Azure AI Search service in any of the following Azure public r
 
 <sup>2</sup> This region is in high demand, which prevents the creation of new search services. Please choose a different region.
 
-<sup>3</sup> This region doesn't have indexer support for [Microsoft Purview sensitivity labels](search-indexer-sensitivity-labels.md).
+<sup>3</sup> This region doesn't have indexer support for [Microsoft Purview sensitivity labels (preview)](search-indexer-sensitivity-labels.md).
 
 ### Europe
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マイクロソフト・パービュー感度ラベルの説明を更新"
}
```

### Explanation
この変更は、Azure AI Searchの地域サポートに関するドキュメントの小規模な修正を示しています。

主な変更点は次の通りです：
- **プレビューに関する注釈の追加**: Microsoft Purview感度ラベルの説明が更新され、サポートされている地域の説明に「(preview)」が追加されました。これにより、ユーザーはこの機能がまだプレビュー版であることを認識でき、利用の際の注意点を理解できます。
- **重複の削除**: 残されていた前文の再表示部分が削除され、文書がより簡潔になりました。これにより、情報が整理され、ユーザーにとっての可読性が向上します。

この変更によって、読者は地域ごとのAzure AI Searchの利用状況を掴みやすくなり、特に新しい機能がどのように位置付けられているかを理解しやすくなります。

## articles/search/search-relevance-overview.md{#item-cb0e09}

<details>
<summary>Diff</summary>
````diff
@@ -23,11 +23,11 @@ The true measure of relevance is *how well* a retrieved set of results meets you
 In Azure AI Search, two main strategies have emerged as the best approaches for producing highly relevant results.
 
 + Hybrid search with semantic ranker
-+ Agentic retrieval with LLM-assisted query planning (preview) and answer synthesis (preview)
++ Agentic retrieval with LLM-based query planning (preview) and answer synthesis (preview)
 
 [Hybrid search (classic)](hybrid-search-overview.md) delivers relevance by combining the precision of keyword queries and the semantic similarity of vector queries in a search request targeting a single index. Keyword search operates over a verbatim query. Vector search runs an identical query using a vectorized version of the same string. The queries execute in parallel, looking for precise and semantically similar matches. Results are merged, ranked, and then rescored using a semantic ranker that promotes the most relevant matches. Using keyword and vector search *together* offsets the weaknesses of each approach as a standalone solution. Semantic ranker is an extra component that contributes to a better outcome.
 
-[Agentic retrieval](agentic-retrieval-overview.md) delivers relevance through LLM-assisted query planning (preview), answer synthesis (preview), and a knowledge base that defines an entire search domain. The LLM can analyze and transform queries for more effective retrieval. It can decompose complex questions into targeted subqueries, refine vague requests, or generalize narrow ones for broader scope. In a typical agentic retrieval workload, the LLM answers the question using its reasoning power, context from chat history, and retrieval instructions to identify the very best content and use it to best advantage. This combination of LLM-assisted query planning, multi-source knowledge base search, and LLM reasoning is how agentic retrieval returns highly relevant results.
+[Agentic retrieval](agentic-retrieval-overview.md) delivers relevance through LLM-based query planning (preview), answer synthesis (preview), and a knowledge base that defines an entire search domain. The LLM can analyze and transform queries for more effective retrieval. It can decompose complex questions into targeted subqueries, refine vague requests, or generalize narrow ones for broader scope. In a typical agentic retrieval workload, the LLM answers the question using its reasoning power, context from chat history, and retrieval instructions to identify the very best content and use it to best advantage. This combination of LLM-based query planning, multi-source knowledge base search, and LLM reasoning is how agentic retrieval returns highly relevant results.
 
 Relevance also depends on having grounding data of sufficient quantity and quality. In agentic retrieval, you can list multiple knowledge sources to expand the scope of what's searchable and provide logic for selecting specific ones.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリック検索の用語の修正"
}
```

### Explanation
この変更は、Azure AI Searchの関連性に関するドキュメントに対する小規模な修正を示しています。

主な変更点は次の通りです：
- **用語の修正**: 「LLM-assisted query planning」という表現が「LLM-based query planning」に変更されました。これにより、用語の一貫性が向上し、ユーザーが理解しやすくなります。
- **文章の更新**: 変更に伴い、関連する文章も修正され、文書全体の流れが整えられています。

これにより、エージェントリック検索に関する情報がより精緻になり、読者は技術や関連性の向上に向けた最新のアプローチを把握しやすくなります。特に、LLMを使用した検索のプロセスが明確にされ、全体的な理解を促進する効果があります。

## articles/search/search-security-best-practices.md{#item-9dd4cd}

<details>
<summary>Diff</summary>
````diff
@@ -232,7 +232,7 @@ We only recommend confidential computing for organizations whose compliance or r
 | Compute type | Description | Limitations | Cost | Availability |
 | ------------ | ----------- | ----------- | ---- | ------------ |
 | Default | Standard VMs with built-in encryption for data at rest and in transit. No hardware-based isolation for data in use. | No limitations. | No change to the base cost of free or billable tiers. | Available in all regions. |
-| Confidential | Confidential VMs (DCasv5 or DCesv5) in hardware-based trusted execution environment. Isolates computations and memory from the host operating system and other VMs. | Disables or restricts [agentic retrieval](agentic-retrieval-overview.md), [semantic ranker](semantic-search-overview.md), [query rewrite](semantic-how-to-query-rewrite.md), [skillset execution](cognitive-search-concept-intro.md), and indexers that run in the [multitenant environment](search-howto-run-reset-indexers.md#indexer-execution-environment) <sup>1</sup>. | Adds 10% surcharge to the base cost of billable tiers. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/search/). | Available in some regions. For more information, see the [list of supported regions](search-region-support.md). |
+| Confidential | Confidential VMs (DCasv5 or DCesv5) in hardware-based trusted execution environment. Isolates computations and memory from the host operating system and other VMs. | Disables or restricts [agentic retrieval](agentic-retrieval-overview.md), [semantic ranker](semantic-search-overview.md), [query rewrite (preview)](semantic-how-to-query-rewrite.md), [skillset execution](cognitive-search-concept-intro.md), and indexers that run in the [multitenant environment](search-howto-run-reset-indexers.md#indexer-execution-environment) <sup>1</sup>. | Adds 10% surcharge to the base cost of billable tiers. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/search/). | Available in some regions. For more information, see the [list of supported regions](search-region-support.md). |
 
 <sup>1</sup> When you enable this compute type, indexers can only run in the private execution environment, meaning they run from the search clusters hosted on confidential computing.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリ書き換えのプレビュー表記を追加"
}
```

### Explanation
この変更は、Azure AI Searchのセキュリティベストプラクティスに関するドキュメントにおいて、機密コンピューティングに関連する情報に小規模な修正を行ったものです。

主な変更点は次の通りです：
- **クエリ書き換えのプレビュー表記の追加**: 機密コンピューティングで使用されるVMに関する説明の中で、「query rewrite」の表記が「query rewrite (preview)」に変更されました。これにより、読者はこの機能が現時点ではプレビュー状態であることをより明確に認識できます。
- **一貫性の向上**: その他の説明文と整合性を持たせるために用語が調整されました。これにより、文書がより整然とした形で提示され、技術的な理解がしやすくなります。

この変更は、機密コンピューティングを利用する場合の制約を明確にし、Azure AI Searchの機能を利用する際の注意点を強調しています。結果として、ユーザーはシステムの動作や制限をより正確に理解できるようになります。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -15,6 +15,8 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
 Enabling customer‑managed keys (CMK) adds additional security on top of the default encryption at rest when using [Microsoft-managed keys](/azure/security/fundamentals/encryption-atrest#azure-encryption-at-rest-components). When you enable CMK, you control the encryption keys used to protect your data, including the ability to:
 
 - Rotate keys on a customer‑defined schedule
@@ -70,8 +72,6 @@ Adding a customer-managed key to an object must happen when the object is newly
 
 ## Enable service-level CMK on new objects by default (preview)
 
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
-
 Starting in the 2026-03-01-preview release, you can configure a customer-managed key at the service level on the Azure AI Search service itself. This feature lets you configure the key once and apply it to all newly created objects by default. That protection keeps sensitive data in your search service secure with a key you control, without requiring you to specify key information each time you create an object. In data plane API version `2026-05-01-preview` and later, the `isServiceLevelKey` property on `encryptionKey` helps you determine whether an object inherits the service-level key or uses an explicit object-level key.
 
 Enabling CMK at the service level means:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビュー用の説明文を追加"
}
```

### Explanation
この変更は、Azure AI Searchの暗号化キーの管理に関するドキュメントにおいて、機能に関連するプレビュー情報の明示化を目的とした小規模な修正です。

主な変更点は次の通りです：
- **プレビュー用のバナーの追加**: 新たに `[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]` のバナーが追加されました。これにより、ドキュメント内で述べられている機能がプレビュー版であることを明確にし、読み手にその注意を促します。
- **不要な記述の削除**: もともと記載されていた「Feature preview」に関する行が削除され、より簡潔な表現に整えられました。これにより、情報の冗長性が解消され、内容が明瞭になります。

この変更により、読者はAzure AI Searchの機能がプレビュー段階であることを認識しやすくなり、実装する際のリスクや制限についてより適切に判断できるようになります。また、機能の適用方法に関する具体的な情報が、最新の状態で提供されることになります。

## articles/search/search-security-managed-encryption-cross-tenant.md{#item-efc726}

<details>
<summary>Diff</summary>
````diff
@@ -13,6 +13,8 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
 This article describes a cross-tenant scenario where a service provider hosts Azure AI Search in their own tenant and enables [customer-managed key (CMK) encryption](search-security-manage-encryption-keys.md) using a multitenant Microsoft Entra application.
 
 In this configuration, the customer uses Azure Key Vault in their own tenant to manage their encryption key. The service provider has no access to this key.
@@ -37,7 +39,7 @@ In this configuration, the customer uses Azure Key Vault in their own tenant to
 
 You can configure a multitenant Microsoft Entra application to use customer-managed keys in a cross-tenant scenario by using one of the following approaches:
 
-1. **Federated identity support (recommended)**: Configure Microsoft Entra federated identity credentials (FIC) with a user-assigned managed identity (UAMI). This approach uses managed identity tokens and exchanges them for access tokens, eliminating the need for long-lived secrets and aligning with workload identity federation principles. This approach requires the preview `federatedIdentityClientId` property, introduced in API version `2026-05-01-preview`.
+1. **Federated identity support (preview, recommended)**: Configure Microsoft Entra federated identity credentials (FIC) with a user-assigned managed identity (UAMI). This approach uses managed identity tokens and exchanges them for access tokens, eliminating the need for long-lived secrets and aligning with workload identity federation principles. This approach requires the preview `federatedIdentityClientId` property, introduced in API version `2026-05-01-preview`.
 
 1. **Client secrets**: Configure a client secret using the `accessCredentials` property. This approach is less secure and requires additional management to rotate and protect the secret.
 
@@ -58,15 +60,6 @@ Use the Azure CLI to send requests. The service provider's tenant that contains
 
 ## Use federated identity support (preview)
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
-
 To use federated identity to support a cross-tenant CMK scenario:
 
 1. The service provider configures the AI Search service in their tenant (Tenant A). For guidance on how to do this, see [Create a Search Service (in the Azure portal)](/azure/search/search-create-service-portal) or use the [az search service create](/cli/azure/search/service#az-search-service-create) command in Azure CLI.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビュー情報と説明の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける顧客管理キー（CMK）を用いたクロステナントシナリオに関するドキュメントの内容を更新し、より明確にすることを目的とした小規模な修正です。

主な変更点は次の通りです：
- **プレビュー用バナーの追加**: `[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]`が追加され、現在の機能がプレビュー版であることを明示しています。これにより、ユーザーに対してこの機能の使用に関する認識を高めます。
- **テキストの更新**: 「Federated identity support (recommended)」の表記が「Federated identity support (preview, recommended)」に変更され、これはこの機能がプレビュー中であることを強調します。
- **重要情報の削除**: 一部の詳細な注意事項が削除されました。これにより、重要でない情報が削除され、コンテンツがより簡潔になります。特に、標準的な利用条件やリスクに関する注意事項が整理され、文書の流れをスムーズにする効果があります。

これらの変更により、ユーザーはクロステナントのCMKシナリオを実装する際に必要な情報を、より効率的に取得できるようになります。また、どの機能が現在プレビュー中であるかを理解しやすくなります。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -89,7 +89,7 @@ Use the following table to quickly find which role provides the permissions you
 | Upload data for indexing <sup>2</sup> | ❌ | ❌ | ❌ | ✅ | ❌ |
 | Query an index | ❌ | ❌ | ❌ | ✅ | ✅ |
 | Retrieve from a knowledge base | ❌ | ❌ | ❌ | ✅ | ✅ |
-| Bypass permission filters with [elevated read](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results) | ❌ | ❌ | ❌ | ✅ | ❌ |
+| Bypass permission filters with [elevated read (preview)](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results-preview) | ❌ | ❌ | ❌ | ✅ | ❌ |
 
 <sup>1</sup> Includes indexes, indexers, data sources, skillsets, aliases, synonym maps, debug sessions, knowledge bases, and knowledge sources. Indexers also support run and reset operations.
 
@@ -966,7 +966,7 @@ When you develop applications that use role-based access control for authenticat
 
 + If the authorization token comes from a [managed identity](/entra/identity/managed-identities-azure-resources/overview) and you recently assigned the appropriate permissions, it [might take several hours](/entra/identity/managed-identities-azure-resources/managed-identity-best-practice-recommendations#limitation-of-using-managed-identities-for-authorization) for the permissions assignments to take effect.
 
-+ If queries with document-level permissions don't return expected results, use Search Index Data Contributor or [create a custom role](#create-a-custom-role) with [elevated permissions](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results) to investigate.
++ If queries with document-level permissions don't return expected results, use Search Index Data Contributor or [create a custom role](#create-a-custom-role) with [elevated permissions (preview)](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results-preview) to investigate.
 
 ## Next step
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビュー機能への言及を更新"
}
```

### Explanation
この変更は、AzureのRBAC（役割ベースアクセス制御）に関する文書において、プレビュー機能に関連する表現を更新することを目的とした小規模な修正です。

主な変更点は以下の通りです：
- **プレビュー機能の明示化**: 「elevated read」という機能の記述に、プレビューであることを示すために「(preview)」が追加されました。この変更により、読者はこの特定の機能がプレビュー段階にあることを認識しやすくなります。
- **他の項目の更新**: 確定的な変更ではないが、他の文言も微調整されており、文全体の整合性が向上しています。

この変更によって、ドキュメントが最新の機能に即した内容となり、ユーザーがRBACを用いる際にどの権限を利用できるのかをより正確に理解できるようになります。プレビュー状態の機能に対する意識を高めることで、利用に関するリスクや特性についての適切な判断がしやすくなります。

## articles/search/search-sku-manage-costs.md{#item-6e0122}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: how-to
 ms.date: 06/02/2026
+ai-usage: ai-assisted
 ---
 
 # Plan and manage costs of an Azure AI Search service
@@ -17,7 +18,7 @@ Azure AI Search is available in two pricing models:
 
 - **Dedicated**: Provisioned capacity with fixed pricing. You select a service tier and you're billed per hour based on Search Units (SUs). Best for steady, predictable, high-utilization workloads.
 
-- **Serverless (Preview)**: Consumption-based pricing measured by Compute Units per hour (CU/hr) and per-GB/month for indexed storage. Best for infrequent, bursty, or highly variable workloads.
+- **Serverless (preview)**: Consumption-based pricing measured by Compute Units per hour (CU/hr) and per-GB/month for indexed storage. Best for infrequent, bursty, or highly variable workloads.
 
 This article explains how billing works under each model and provides guidance for cost estimation, minimization, and monitoring.
 
@@ -39,7 +40,7 @@ For more details on the service tiers available, see [Choose a pricing model and
 
 As you increase or decrease the number of replicas or partitions, your total search units change, and costs scale accordingly. For more information and examples, see [Billing rates](search-sku-tier.md#billing-rates).
 
-### Serverless pricing model (Preview)
+### Serverless pricing model (preview)
 
 [!INCLUDE [Serverless preview](./includes/previews/preview-serverless.md)]
 
@@ -82,7 +83,7 @@ Depending on your configuration and usage, the following charges might apply:
 
 + Data traffic might incur networking costs. See the [bandwidth pricing](https://azure.microsoft.com/pricing/details/bandwidth/).
 
-+ Several premium features, such as [knowledge stores](knowledge-store-concept-intro.md), [debug sessions](cognitive-search-debug-session.md)<sup>1</sup> , and [enrichment caches](enrichment-cache-how-to-configure.md), depend on Azure Storage and incur storage costs. Charges for these features appear on your Azure Storage bill.
++ Several premium features, such as [knowledge stores](knowledge-store-concept-intro.md), [debug sessions](cognitive-search-debug-session.md)<sup>1</sup> , and [enrichment caches (preview)](enrichment-cache-how-to-configure.md), depend on Azure Storage and incur storage costs. Charges for these features appear on your Azure Storage bill.
 
 + [Customer-managed keys](search-security-manage-encryption-keys.md), which provide double encryption of sensitive content, require a billable [Azure Key Vault](https://azure.microsoft.com/pricing/details/key-vault/).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビュー機能の記述を更新"
}
```

### Explanation
この変更は、Azure AI Searchサービスのコスト管理に関する文書において、プレビュー機能に関する言及を最新の状態に保つことを目的とした小規模な修正です。

主な変更点は以下の通りです：
- **プレビュー機能の明示化**: 「Serverless (Preview)」という表記が「Serverless (preview)」に修正され、プレビュー状態であることを強調しました。この修正により、ユーザーがこの機能の利用状況を把握しやすくなります。
- **その他のプレビュー内容の追加**: 「enrichment caches」機能についても「(preview)」という表記を追加し、これがプレビュー機能であることを明示しました。

このような変更により、ユーザーはAzure AI Searchサービスを利用する際に、どの機能がプレビューであるかを正確に理解し、使用する際のリスクや特性について適切に判断できるようになります。また、コストに関する情報が明確に整理されているため、ユーザーがより効率的にコスト計画を立てる手助けにもなります。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
 title: Choose a pricing model and service tier
-description: Learn about the Dedicated and Serverless (Preview) pricing models and service tiers (or SKUs) for Azure AI Search. Serverless tiers are consumption-based and Dedicated tiers are capacity-based with fixed pricing.
+description: Learn about the Dedicated and Serverless (preview) pricing models and service tiers (or SKUs) for Azure AI Search. Serverless tiers are consumption-based and Dedicated tiers are capacity-based with fixed pricing.
 author: mattwojo
 ms.author: mattwoj
 ms.service: azure-ai-search
@@ -18,7 +18,7 @@ When you [create a search service](search-create-service-portal.md), you must ch
 | Pricing model | Best for | How you're billed |
 | --- | --- | --- |
 | Dedicated | Steady, predictable, high-utilization workloads | Fixed capacity via Search Units (SUs); hourly rate based on selection of a [service tier](#tier-descriptions) |
-| Serverless (Preview) | Infrequent, bursty, or highly variable workloads | Consumption-based: measured by [Compute Units](./serverless-cost-optimization.md) (CUs) and indexed storage (GB/month) |
+| Serverless (preview) | Infrequent, bursty, or highly variable workloads | Consumption-based: measured by [Compute Units](./serverless-cost-optimization.md) (CUs) and indexed storage (GB/month) |
 
 > [!NOTE] 
 > Dedicated model Search Units (SUs) and Serverless model Compute Units (CUs) are not the same and cannot be used interchangeably. Don't use SU-based pricing calculators or estimates for Serverless workloads.
@@ -125,7 +125,7 @@ Most features are available across all tiers. In some cases, feature availabilit
 
 | Feature | Tier considerations |
 |---------|---------------------|
-| [indexers](search-indexer-overview.md) | Indexers are available on S3 HD with [daily execution quota across indexers and other considerations](search-indexer-high-density-serverless-overview.md). Indexers have [more limitations](search-limits-quotas-capacity.md#indexer-limits) on the free tier. |
+| [indexers](search-indexer-overview.md) | Indexers are available on S3 HD with [daily execution quota across indexers and other considerations (preview)](search-indexer-high-density-serverless-overview.md). Indexers have [more limitations](search-limits-quotas-capacity.md#indexer-limits) on the free tier. |
 | [indexer `executionEnvironment` configuration parameter](search-how-to-create-indexers.md?tabs=indexer-rest#create-an-indexer) | The ability to pin all indexer processing to just the search clusters allocated to your search service requires S2 and higher. |
 | [AI enrichment](cognitive-search-concept-intro.md) | Runs on the Free tier but not recommended for large workloads. |
 | [Managed or trusted identities for outbound (indexer) access](search-how-to-managed-identities.md) | Not available on the Free tier.|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビュー機能の表記を修正"
}
```

### Explanation
この変更は、Azure AI Searchサービスに関する価格モデルとサービスレベル（SKU）の説明文書において、プレビュー機能に関連する表現を最新の状態にするための小規模な修正です。

主な変更点は以下の通りです：
- **プレビュー表記の更新**: 「Serverless (Preview)」という表現が「Serverless (preview)」に修正され、プレビュー機能としての認識を明確にしました。この変更により、ユーザーがプレビュー機能の状態をより理解しやすくなります。
- **説明の整合性向上**: 表の内容や説明文中でのプレビュー機能に関する言及も同様に更新され、全体としての一貫性が強化されています。

この変更により、ユーザーはAzure AI Searchの価格モデルやサービスレベルを理解する際に、プレビュー機能に関する情報を明確に把握でき、より良い意思決定が可能となります。結果として、設定や使用に関する情報が整理され、利用者にとって参考になる内容が充実しています。

## articles/search/search-try-for-free.md{#item-36e28d}

<details>
<summary>Diff</summary>
````diff
@@ -43,13 +43,13 @@ Before you create resources for a key-based connection, confirm regional support
 
 ## Choose a pricing model and tier
 
-Azure AI Search offers two pricing models: Dedicated and Serverless (Preview).
+Azure AI Search offers two pricing models: Dedicated and Serverless (preview).
 
 - **Dedicated pricing model** - **Free tier** doesn't consume credits and provides 50 MB of storage. You can have one free search service per Azure subscription. This tier is always free and doesn't expire, even after your 30-day trial ends. However, it doesn't support semantic ranking or managed identities for Microsoft Entra ID authentication and authorization, which are commonly used in quickstarts.
 
 - **Dedicated pricing model** - **Basic tier** (recommended) consumes about one-third of your USD200 credits over 30 days, and provides 15 GB of storage in most regions. This tier supports all features, including semantic ranking and managed identities, and runs on dedicated infrastructure for consistent performance.
 
-- **Serverless pricing model** - **Serverless Developer tier** (Preview) uses consumption-based pricing. To evaluate usage costs in this tier, visit the [Azure portal](https://portal.azure.com) where you can view charges accrued once the billing period begins in the **Scale + Cost** tab.
+- **Serverless pricing model** - **Serverless Developer tier** (preview) uses consumption-based pricing. To evaluate usage costs in this tier, visit the [Azure portal](https://portal.azure.com) where you can view charges accrued once the billing period begins in the **Scale + Cost** tab.
 
 [!INCLUDE [Serverless preview](./includes/previews/preview-serverless.md)]
 
@@ -87,7 +87,7 @@ You can access Azure AI Search through two portals, each optimized for different
 
 ## Track your credit usage
 
-During the trial period, stay under the USD200 credit allocation. Dedicated services are billed for provisioned capacity while they exist, even when idle. If you create a Dedicated Basic search service, expect Azure AI Search to consume about one-third of your available credits during the trial period. Serverless Developer (Preview) billing behavior is covered in the preview notice above, and you should still monitor estimated usage.
+During the trial period, stay under the USD200 credit allocation. Dedicated services are billed for provisioned capacity while they exist, even when idle. If you create a Dedicated Basic search service, expect Azure AI Search to consume about one-third of your available credits during the trial period. Serverless Developer (preview) billing behavior is covered in the preview notice above, and you should still monitor estimated usage.
 
 In the Azure portal, a notification in the upper-right corner shows how many credits have been used and how many remain. You can also monitor billing by searching for **Subscriptions** in the topmost search bar. The **Overview** page shows spending rates, forecasts, and cost management. For more information, see [Check usage of free services included with your Azure free account](/azure/cost-management-billing/manage/check-free-service-usage).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビュー表記の統一"
}
```

### Explanation
この変更は、Azure AI Searchの「無料で試す」セクションにおいて、プレビュー機能に関する表記を最新の状態に保つための小規模な修正です。具体的には、「Serverless (Preview)」の表記が「Serverless (preview)」に統一されました。

主な変更点は以下の通りです：
- **プレビュー表記の統一**: すべての関連箇所において「Preview」を「preview」に修正し、文書内の一貫性を保ちました。これにより、ユーザーはプレビュー機能であることをより明確に理解できるようになります。
- **情報の明確化**: プライシングモデルについての説明や、各ティアのサービスの違いについても補足されており、ユーザーがどのモデルを選択すべきかを理解する手助けが強化されています。

この修正により、Azure AI Searchの特性に関する情報が整理され、利用者はプレビュー機能の利用に関する注意点を効果的に把握できるようになります。結果として、Azure AI Searchを利用する際の意思決定がより円滑になることが期待されます。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how Azure AI Search helps you build rich search experiences a
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: overview
-ms.date: 08/05/2026
+ms.date: 09/17/2026
 ai-usage: ai-assisted
 ---
 
@@ -14,14 +14,6 @@ ai-usage: ai-assisted
 
 Azure AI Search is a fully managed, cloud-hosted service that connects your data to AI. The service unifies access to enterprise and web content so agents and large language models (LLMs) can use context, chat history, and multi-source signals to produce reliable, grounded answers.
 
-Azure AI Search is available in two pricing models:
-
-- **Dedicated**: Provisioned capacity with fixed pricing. You select a service tier and you're billed per hour based on Search Units (SUs). Best for steady, predictable, high-utilization workloads.
-
-- **Serverless (Preview)**: Consumption-based pricing measured by Compute Units per hour (CU/hr) and per-GB/month for indexed storage. Best for infrequent, bursty, or highly variable workloads.
-
-[!INCLUDE [Serverless preview](./includes/previews/preview-serverless.md)]
-
 Common use cases include *classic search* and retrieval-augmented generation (RAG) using *agentic retrieval*, where the service orchestrates query planning, retrieval, and response construction. These capabilities support scenarios ranging from traditional search experiences to AI-powered agents and chat applications suitable for both enterprise and consumer scenarios.
 
 When you create a search service, the following capabilities are included:
@@ -54,9 +46,6 @@ When you create a search service, the following capabilities are included:
 
 + Scale and operate in production with Azure reliability, monitoring and diagnostics (logs, metrics, and alerts), and REST API or SDK tooling for automation.
 
-> [!NOTE]
-> In the Serverless pricing model, scaling is handled automatically by the service. Unlike Dedicated models where you configure replicas and partitions, Serverless uses consumption-based scaling and service-level limits to manage capacity. For more information, see [Optimize costs with the Serverless pricing model](./serverless-cost-optimization.md).
-
 For more information about specific functionality, see [Features of Azure AI Search](search-features-list.md).
 
 ## What is classic search?
@@ -108,7 +97,7 @@ Classic search and agentic retrieval are complementary modes of information retr
 | Region restrictions | No | Yes |
 | Status | Generally available | Generally available, with some capabilities in preview |
 | Dedicated pricing model support | Yes | Yes |
-| Serverless pricing model support | Yes | Yes |
+| Serverless pricing model support (preview) | Yes | Yes |
 
 ## How to get started
 
@@ -120,9 +109,9 @@ The portal is useful for service administration and content management, with too
 
 Before you get started, use this checklist to make key decisions:
 
-+ **Choose a pricing model**: Select between the **Dedicated** or **Serverless** pricing model. See [Choose a pricing model and service tier](./search-sku-tier.md) for help with choosing the model that best fits your needs.
++ **Choose a pricing model**: Select between the **Dedicated** or **Serverless** (preview) pricing model. See [Choose a pricing model and service tier](./search-sku-tier.md) for help with choosing the model that best fits your needs.
 
-+ **Choose how you want to retrieve data:** You can query directly from a search index for predictable, low-latency results, or use agentic retrieval to query across multiple indexes through a knowledge base. If you’re building a traditional app without an agent or chatbot, direct index queries can meet most needs with lower cost and complexity. If you want to work across multiple knowledge sources or support more advanced scenarios, consider agentic retrieval with minimal [reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md).
++ **Choose how you want to retrieve data:** You can query directly from a search index for predictable, low-latency results, or use agentic retrieval to query across multiple indexes through a knowledge base. If you’re building a traditional app without an agent or chatbot, direct index queries can meet most needs with lower cost and complexity. If you want to work across multiple knowledge sources or support more advanced scenarios, consider agentic retrieval with minimal [reasoning effort (preview)](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md).
 
 + **Choose a region:** If you're using agentic retrieval, choose a [supported region](search-region-support.md). For classic search, choose a region that offers the features and capacity you need.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新と表記の整合性"
}
```

### Explanation
この変更は、Azure AI Searchに関する文書において、日付の更新や表記の整合性を図るための小規模な修正です。

主な変更点は以下の通りです：
- **日付の更新**: 最終更新日が「08/05/2026」から「09/17/2026」に変更され、最新の情報を反映しました。
- **プレビュー表記の統一**: 「Serverless (Preview)」の表記を「Serverless (preview)」に修正し、一貫性を持たせたことにより、文書中の表現が統一されています。
- **コンテンツの整理**: 不要な説明が削除され、情報の流れや明確さが向上しています。特に、サーバーレスモデルのプレビュー表記が各所に更新され、ユーザーがプレビュー機能のステータスを明確に理解できるようになっています。

これにより、Azure AI Searchの機能やプライシングモデルに関する情報が整然と提示され、ユーザーが選択肢を比較しやすくなっています。また、全体としての内容がスリムになり、読みやすさが向上しています。

## articles/search/semantic-code-migration.md{#item-ad1ba7}

<details>
<summary>Diff</summary>
````diff
@@ -62,7 +62,7 @@ To determine which semantic features are available in a specific Azure SDK packa
 
 ## 2024-11-01-preview
 
-+ Adds [query rewrite](semantic-how-to-query-rewrite.md) to Search Documents.
++ Adds [query rewrite (preview)](semantic-how-to-query-rewrite.md) to Search Documents.
 + Requires `queryLanguage` for query rewrite workloads. For a list of valid values, see the [REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-11-01-preview#querylanguage&preserve-view=true).
 
 ## 2024-09-01-preview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビュー表記の追加"
}
```

### Explanation
この変更は、Azure AI Searchのセマンティックコードマイグレーションに関する文書の小規模な修正であり、機能の明確化を目的としています。

主な変更点は以下の通りです：
- **プレビュー表記の追加**: 「query rewrite」を「query rewrite (preview)」に修正し、この機能が現時点でプレビュー版であることを明示しました。これにより、ユーザーは、この機能の利用に関する注意点やステータスを理解しやすくなります。

この修正により、文書の明確性が向上し、ユーザーが機能の現状について正確な情報を得られるようになります。結果的に、Azure AI Searchを利用する際のユーザー体験が向上することが期待されます。

## articles/search/semantic-how-to-configure.md{#item-7a92a6}

<details>
<summary>Diff</summary>
````diff
@@ -14,6 +14,8 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
 Semantic ranking iterates over an initial result set, applying an L2 ranking methodology that promotes the most semantically relevant results to the top of the stack. You can also get semantic captions, with highlights over the most relevant terms and phrases, and [semantic answers](semantic-answers.md).
 
 This article explains how to configure a search index for semantic reranking.
@@ -167,9 +169,7 @@ SearchIndex searchIndex = new(indexName)
 
 ---
 
-## Opt in for prerelease semantic ranking models
-
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+## Opt in for prerelease semantic ranking models (preview)
 
 Using [preview REST APIs](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) and preview Azure SDKs that provide the property, you can optionally configure an index to use prerelease semantic ranking models if one is deployed in your region. There's no mechanism for knowing if a prerelease is available, or if it was used on specific query. For this reason, we recommend that you use this property in test environments, and only if you're interested in trying out the very latest semantic ranking models.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビュー表記の追加と内容の整理"
}
```

### Explanation
この変更は、Azure AI Searchのセマンティック構成に関する文書の小規模な修正であり、情報の明確化とプレビューの情報提供を目的としています。

主な変更点は以下の通りです：
- **プレビューの情報追加**: 新しい情報として「[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]」を追加し、プレビューと関連する用語を明示しました。これにより、ユーザーは非公開の機能やベータ版の特性についての理解が深まります。
- **タイトルの変更**: 「Opt in for prerelease semantic ranking models」というセクションタイトルを「Opt in for prerelease semantic ranking models (preview)」に変更し、この機能がプレビュー版であることを強調しました。この変更により、ユーザーはこの機能の隠れたリスクや使用方法を把握しやすくなります。

さらなる内容の整理により、セマンティックランキングに関する基本的な情報が強化され、この技術を効果的に使用するための手助けがなされており、結果として記事全体の明瞭さが向上しています。

## articles/search/semantic-how-to-query-request.md{#item-85530d}

<details>
<summary>Diff</summary>
````diff
@@ -8,6 +8,7 @@ ms.custom:
   - ignite-2024
 ms.topic: how-to
 ms.date: 04/24/2026
+ai-usage: ai-assisted
 ---
 
 # Add semantic ranking to queries in Azure AI Search
@@ -27,7 +28,7 @@ This article explains how to invoke the semantic ranker on queries. It assumes y
 + Familiarity with [semantic ranking](semantic-search-overview.md).
 
 > [!NOTE]
-> Captions and answers are extracted verbatim from text in the search document. The semantic subsystem uses machine reading comprehension to recognize content having the characteristics of a caption or answer, but doesn't compose new sentences or phrases except in the case of [query rewrite](semantic-how-to-query-rewrite.md). For this reason, content that includes explanations or definitions work best for semantic ranking. If you want chat-style interaction with generated responses, see [Agentic retrieval](agentic-retrieval-overview.md) or [Retrieval Augmented Generation (RAG)](retrieval-augmented-generation-overview.md).
+> Captions and answers are extracted verbatim from text in the search document. The semantic subsystem uses machine reading comprehension to recognize content having the characteristics of a caption or answer, but doesn't compose new sentences or phrases except in the case of [query rewrite (preview)](semantic-how-to-query-rewrite.md). For this reason, content that includes explanations or definitions work best for semantic ranking. If you want chat-style interaction with generated responses, see [Agentic retrieval](agentic-retrieval-overview.md) or [Retrieval Augmented Generation (RAG)](retrieval-augmented-generation-overview.md).
 
 ## Choose a client
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI使用の明記と注意書きの内容修正"
}
```

### Explanation
この変更は、Azure AI Searchのクエリリクエストに関する文書の小規模な修正であり、AIの使用に関する明示及び注意書きの内容の明確化を目的としています。

主な変更点は以下の通りです：
- **AI使用の明記**: 新しく「ai-usage: ai-assisted」という行が追加され、AIを活用した検索の特徴が強調されました。これにより、文書がAIの使用に関連する情報を明確に示すようになっています。
- **注意書きの修正**: 注意書きの中で「query rewrite」の表記が「query rewrite (preview)」に変更され、プレビュー版であることが示されることで、ユーザーがこの機能の状態についてより正確に理解できるようになりました。

これらの変更により、文書全体の理解が向上し、特にユーザーに対してAIを利用した機能やその使用感に関する情報が明確に伝わるように改善されています。

## articles/search/semantic-how-to-query-rewrite.md{#item-3e168f}

<details>
<summary>Diff</summary>
````diff
@@ -8,15 +8,16 @@ ms.custom:
   - references_regions
 ms.topic: how-to
 ms.date: 04/24/2026
+ai-usage: ai-assisted
 ---
 
-# Rewrite queries with semantic ranker in Azure AI Search (Preview)
+# Rewrite queries with semantic ranker in Azure AI Search (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-Query rewriting is the process of transforming a user's query into a more effective one, adding more terms and refining search results. The search service sends the search query (or a variation of it) to a generative model that generates alternative queries. 
+Query rewriting (preview) is the process of transforming a user's query into a more effective one, adding more terms and refining search results. The search service sends the search query (or a variation of it) to a generative model that generates alternative queries. 
 
 Query rewriting improves results from [semantic ranking](search-get-started-semantic.md) by correcting typos or spelling errors in user queries, and expanding queries with synonyms.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビュー版表示の修正とAI使用の明示"
}
```

### Explanation
この変更は、Azure AI Searchのクエリ再作成に関する文書の小規模な修正であり、プレビュー版の内容を明確にし、AI使用に関する情報を追加することを目的としています。

主な変更点は以下の通りです：
- **プレビュー表示の修正**: タイトルから「(Preview)」が「(preview)」に変更され、表記が統一されました。これにより視覚的な一貫性が保たれ、ユーザーにとっての理解が容易になります。
- **AI使用の明記**: 「ai-usage: ai-assisted」という行が追加され、AIを活用した機能であることが強調されました。これにより、文書は最新の技術的な実装をより分かりやすく表現しています。
- **注意書きの変更**: 「[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]」の行が「[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]」に変更され、プレビュー版に関連する情報が強調され、利用者が最新の機能を理解しやすくなっています。

これらの変更により、文書の明確さと信頼性が向上し、特にユーザーがAIを用いたクエリの再作成機能をより効果的に利用できるようになることを目指しています。

## articles/search/semantic-search-overview.md{#item-b7497b}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ Semantic ranker has the following capabilities:
 | L2 ranking | Uses the context or semantic meaning of a query to compute a new relevance score over preranked results. |
 | [Semantic captions and highlights](semantic-how-to-query-request.md) | Extracts verbatim sentences and phrases from fields that best summarize the content, with highlights over key passages for easy scanning. Captions that summarize a result are useful when individual content fields are too dense for the search results page. Highlighted text elevates the most relevant terms and phrases so that users can quickly determine why a match was considered relevant. |
 | [Semantic answers](semantic-answers.md) | An optional and extra substructure returned from a semantic query. It provides a direct answer to a query that looks like a question. It requires that a document has text with the characteristics of an answer. |
-| [Query rewrite](semantic-how-to-query-rewrite.md) | Using text queries or the text portion of a vector query, semantic ranker creates up to 10 variants of the query, perhaps correcting typos or spelling errors, or rephrasing a query using generated synonyms. The rewritten query runs on the search engine. The results are scored using BM25 or RRF scoring, and then rescored by semantic ranker.  |
+| [Query rewrite (preview)](semantic-how-to-query-rewrite.md) | Using text queries or the text portion of a vector query, semantic ranker creates up to 10 variants of the query, perhaps correcting typos or spelling errors, or rephrasing a query using generated synonyms. The rewritten query runs on the search engine. The results are scored using BM25 or RRF scoring, and then rescored by semantic ranker.  |
 
 ## How semantic ranker works
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリ再作成のプレビュー表示の修正"
}
```

### Explanation
この変更は、Azure AI Searchにおけるセマンティック検索の概要に関する文書の小規模な修正であり、クエリの再作成機能に関する説明を更新することを目的としています。

主な変更点は以下の通りです：
- **プレビュー表示の修正**: 「Query rewrite」の項目のタイトルに「(preview)」が追加され、ユーザーに対してこの機能が現在プレビュー版であることを明示しています。これにより、利用者は機能が完全ではない可能性を理解しやすくなります。

この変更により、クエリ再作成機能の使用に関するユーザーの期待が適切に設定され、文書の内容がより正確で一貫したものとなります。

## articles/search/serverless-cost-optimization.md{#item-8dc21e}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ Azure AI Search supports two pricing models, each designed for different workloa
 
 - **Dedicated**: Fixed pricing measured by Search Units (SUs). You select a service tier, and you're billed hourly based on provisioned units.
 
-- **Serverless (Preview)**: Consumption-based pricing measured by Compute Units per hour (CU/hr) and per-GB/month for indexed storage.
+- **Serverless (preview)**: Consumption-based pricing measured by Compute Units per hour (CU/hr) and per-GB/month for indexed storage.
 
 [!INCLUDE [Serverless preview](./includes/previews/preview-serverless.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスプランのプレビュー表示の修正"
}
```

### Explanation
この変更は、Azure AI Searchのサーバーレスコスト最適化に関する文書の内容を更新し、特にサーバーレスプランに関連する表示を調整することを目的としています。

主な変更点は以下の通りです：
- **プレビュー表示の修正**: 「Serverless (Preview)」という表記が「Serverless (preview)」に修正され、文書全体での表記の一貫性が向上しています。この変更により、サーバーレスオプションが現在プレビュー版であることを分かりやすく示し、利用者に対する明確な情報提供が行われています。

この更新によって、ユーザーがサーバーレスプランに関する最新の情報を把握しやすくなり、文書が全体としてより明確で一貫したものになっています。

## articles/search/speller-how-to-add.md{#item-9b4502}

<details>
<summary>Diff</summary>
````diff
@@ -7,16 +7,16 @@ ms.custom:
 ms.topic: how-to
 ms.date: 08/27/2025
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
-# Add spell check to queries in Azure AI Search
+# Add spell check to queries in Azure AI Search (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> Spell correction is in preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). It's available through the Azure portal, preview REST APIs, and beta versions of Azure SDK libraries.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-You can improve recall by spell-correcting words in a query before they reach the search engine. The `speller` parameter is supported for all text (non-vector) query types.
+You can improve recall by spell-correcting words in a query before they reach the search engine. The `speller` parameter (preview) is supported for all text (non-vector) query types and is available through the Azure portal, preview REST APIs, and beta versions of Azure SDK libraries.
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スペルチェック機能のプレビューモード表示の修正"
}
```

### Explanation
この変更は、Azure AI Searchにおけるスペルチェック機能の追加方法に関する文書を更新し、特にプレビューモードとその利用に関する情報を明確にすることを目的としています。

主な変更点は以下の通りです：
- **プレビュー表示の強調**: タイトルに「(preview)」が追加され、スペルチェック機能が現時点でプレビュー版であることが明示されました。
- **利用条件の文言更新**: スペルチェック機能に関連する重要な注意事項がインクルード文に置き換えられ、プレビューモードに関する利用規約が明記されています。これにより、ユーザーが機能の利用条件を把握しやすくなります。
- **`speller`パラメータについての説明の改善**: `speller`パラメータがプレビュー版であることが強調され、どのように機能するかについての情報も更新されています。

この更新により、ユーザーは新しいスペルチェック機能がどのように提供されているかについて正確かつ詳細な情報を得られるようになります。また、文書全体の整合性も改善されています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -170,7 +170,7 @@ items:
         href: vector-search-how-to-generate-embeddings.md
       - name: Use integrated vectorization
         href: search-how-to-integrated-vectorization.md
-      - name: Use embedding models from Microsoft Foundry
+      - name: Use embedding models from Microsoft Foundry (preview)
         href: vector-search-integrated-vectorization-ai-studio.md
       - name: Use Azure API Management with Azure OpenAI skills and vectorizers
         href: search-how-to-configure-azure-openai-api-management.md
@@ -198,7 +198,7 @@ items:
       items:
       - name: What is an indexer?
         href: search-indexer-overview.md
-      - name: Indexer execution on Serverless and S3 HD
+      - name: Indexer execution on Serverless and S3 HD (preview)
         href: search-indexer-high-density-serverless-overview.md
       - name: Create and manage
         items:
@@ -330,9 +330,9 @@ items:
         href: cognitive-search-tutorial-debug-sessions.md
     - name: Enrichment caches
       items:
-      - name: Configure an enrichment cache
+      - name: Configure an enrichment cache (preview)
         href: enrichment-cache-how-to-configure.md
-      - name: Manage an enrichment cache
+      - name: Manage an enrichment cache (preview)
         href: enrichment-cache-how-to-manage.md
     - name: Knowledge stores
       items:
@@ -380,7 +380,7 @@ items:
         href: search-query-create.md
       - name: Add autocomplete and suggestions
         href: search-add-autocomplete-suggestions.md
-      - name: Add spell check
+      - name: Add spell check (preview)
         href: speller-how-to-add.md
       - name: Sample queries (simple syntax)
         href: search-query-simple-examples.md
@@ -422,7 +422,7 @@ items:
         href: vector-search-filters.md
       - name: Add a vectorizer
         href: vector-search-how-to-configure-vectorizer.md
-      - name: Use a multi-vector field
+      - name: Use a multi-vector field (preview)
         href: vector-search-multi-vector-fields.md
     - name: Hybrid search
       items:
@@ -466,7 +466,7 @@ items:
         href: semantic-how-to-configure.md
       - name: Add semantic ranking to queries
         href: semantic-how-to-query-request.md
-      - name: Rewrite queries with semantic ranker
+      - name: Rewrite queries with semantic ranker (preview)
         href: semantic-how-to-query-rewrite.md
       - name: Enable scoring profiles in semantic ranker
         href: semantic-how-to-enable-scoring-profiles.md
@@ -608,7 +608,7 @@ items:
         href: tutorial-adls-gen2-indexer-acls.md
       - name: Query with permission filters
         href: search-query-access-control-rbac-enforcement.md
-      - name: Troubleshoot SharePoint permission filtering
+      - name: Troubleshoot SharePoint permission filtering (preview)
         href: troubleshoot-sharepoint-query-permission-filtering.md
     - name: Microsoft Purview sensitivity labels (preview)
       items:
@@ -758,7 +758,7 @@ items:
       href: query-simple-syntax.md
     - name: Full Lucene query syntax
       href: query-lucene-syntax.md
-    - name: moreLikeThis
+    - name: moreLikeThis (preview)
       href: search-more-like-this.md
     - name: OData language
       items:
@@ -796,7 +796,7 @@ items:
       items:
       - name: Microsoft Foundry resource
         items:
-        - name: Azure Vision multimodal embeddings
+        - name: Azure Vision multimodal embeddings (preview)
           href: cognitive-search-skill-vision-vectorize.md
         - name: Document Layout
           href: cognitive-search-skill-document-intelligence-layout.md
@@ -857,11 +857,11 @@ items:
         href: cognitive-search-skill-sentiment.md
   - name: Vectorizers
     items:
-    - name: Microsoft Foundry model catalog
+    - name: Microsoft Foundry model catalog (preview)
       href: vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md
     - name: Azure OpenAI
       href: vector-search-vectorizer-azure-open-ai.md
-    - name: Azure Vision
+    - name: Azure Vision (preview)
       href: vector-search-vectorizer-ai-services-vision.md
     - name: Custom Web API
       href: vector-search-vectorizer-custom-web-api.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビューモードに関する情報の追加"
}
```

### Explanation
この変更は、Azure AI Searchの目次（toc.yml）ファイルを更新し、さまざまな機能に関する情報を精査して、特にプレビューモードで提供されている機能を明示することを目的としています。

主な変更点は以下の通りです：
- **プレビューモードの明示化**: いくつかの項目の名称に「(preview)」が追加され、これによってユーザーはこれらの機能が現在プレビュー版であることを認識しやすくなります。具体的には、Microsoft Foundryの埋め込みモデル、スペルチェック機能、インデクサーの実行、エンリッチメントキャッシュの設定および管理などに関して変更が加えられています。
- **全体的な整合性の向上**: これらの変更によって、プレビュー機能に関する情報の明確さが向上し、ユーザーがどの機能が現在使用可能なものか、またはその信頼性について判断しやすくなります。

この更新により、ドキュメンテーションの明確性と一貫性が高まり、ユーザーは最新の機能について正確な情報を得ることができるようになります。

## articles/search/troubleshoot-sharepoint-query-permission-filtering.md{#item-85cf41}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ai-usage: ai-assisted
 ms.custom: doc-kit-assisted
 ---
 
-# Troubleshoot SharePoint permission filtering in Azure AI Search
+# Troubleshoot SharePoint permission filtering in Azure AI Search (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
@@ -70,7 +70,7 @@ If the user token is omitted, permission-protected content isn't returned. The `
 
 ### 5. Check Microsoft Entra permissions
 
-1. Confirm the indexed `UserIds` or `GroupIds` contain the expected Microsoft Entra object ID. Use an [elevated-read query](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results) only for this diagnostic comparison.
+1. Confirm the indexed `UserIds` or `GroupIds` contain the expected Microsoft Entra object ID. Use an [elevated-read query](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results-preview) only for this diagnostic comparison.
 1. Confirm the test user has a direct assignment or reaches the assigned Microsoft Entra group through transitive Microsoft Entra group membership.
 1. If the Microsoft Entra group is nested within a SharePoint group, change the assignment. This mixed relationship isn't expanded and can cause missing results. Add the user directly to the SharePoint group, or grant permission through a supported Microsoft Entra group assignment.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointの権限フィルタリングに関するトラブルシューティングの更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるSharePointの権限フィルタリングに関するトラブルシューティングの文書を更新し、特にプレビュー機能に関する情報を追加することを目的としています。

主な変更点は以下の通りです：
- **プレビューモードの強調**: ドキュメントのタイトルに「(preview)」が追加され、SharePointの権限フィルタリング機能が現在プレビュー版であることが明記されました。これによりユーザーは、この機能の安定性や完全性について認識するための重要な情報を得られます。
- **リンクの更新**: エレベーテッドリードクエリに関するリンクが更新され、プレビューモードに関連付けられた新しい情報に誘導されています。この変更により、ユーザーは最新の診断比較手法にアクセスできるようになります。

この更新は、ドキュメントの正確性を向上させ、ユーザーが権限フィルタリングの問題をトラブルシューティングする際に必要な情報を効果的に提供することを目的としています。また、プレビュー版の機能に関する注意喚起により、ユーザーが期待する結果を得るための理解の助けとなるでしょう。

## articles/search/tutorial-adls-gen2-indexer-acls.md{#item-6881a0}

<details>
<summary>Diff</summary>
````diff
@@ -13,18 +13,9 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
->
-> The 2026-08-01-preview can't modify access permissions that were set outside of the 2026-08-01-preview. If you use the 2026-08-01-preview with access- or permission-restricted content, a timing lag will occur before the 2026-08-01-preview recognizes changes to those access or permission restrictions.
->
-> It's your responsibility to manage whether your data will flow outside of your organization's compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.
->
-> You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. For more information, see the [Azure AI Search Transparency Note](/azure/foundry/responsible-ai/search/transparency-note).
-
-This tutorial demonstrates how to index Azure Data Lake Storage (ADLS) Gen2 [access control lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control-model#access-control-lists-acls) and [role-based access control (RBAC)](/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac) scope into a search index using an indexer.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
+This tutorial demonstrates Azure Data Lake Storage (ADLS) Gen2 permission metadata ingestion (preview), in which an Azure AI Search indexer adds [access control lists (ACLs)](/azure/storage/blobs/data-lake-storage-access-control-model#access-control-lists-acls) and [role-based access control (RBAC)](/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac) scope to a search index.
 
 It also shows you how to structure a query that respects user access permissions. A successful query outcome confirms the permission transfer that occurred during index.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ADLS Gen2インデクサーACLsに関するチュートリアルの更新"
}
```

### Explanation
この変更は、Azure Data Lake Storage (ADLS) Gen2のインデクサーにおけるアクセス制御リスト（ACL）に関するチュートリアル文書を更新し、特にプレビュー機能に関する情報を追加していることを目的としています。

主な変更点は以下の通りです：
- **プレビューモードの明示化**: 新たに「(preview)」が追加され、ADLS Gen2の権限メタデータのインジェクション機能がプレビュー状態であることが強調されています。これにより、ユーザーは利用可能な機能の状態を理解しやすくなります。
- **重要情報の削除**: 以前の重要な注意事項が多数削除され、その代わりにプレビューに関連する一般的な用語が含まれたインクルード文が追加されました。これは、ドキュメントの簡潔さを高めるための措置と考えられます。
- **チュートリアルの目的の明確化**: チュートリアルの内容が、ADLS Gen2のアクセス制御リストのインデクサーによる追加から、権限メタデータのインジェクションにフォーカスを移しました。また、ユーザーアクセス権限を尊重するクエリの構造化方法も示されるようになっています。

この更新は、ドキュメンテーションの整合性と明確さを向上させ、プレビュー機能を利用する上での新たな指針を提供することを目的としています。結果的に、ユーザーはADLS Gen2の機能をより効果的に利用できるようになります。

## articles/search/tutorial-multimodal.md{#item-718d2e}

<details>
<summary>Diff</summary>
````diff
@@ -114,7 +114,7 @@ Most of these skills depend on a [deployed model](/azure/ai-foundry/foundry-mode
 | -- | -- | -- | -- | -- |
 | [Document Extraction skill](cognitive-search-skill-document-extraction.md), [Text Split skill](cognitive-search-skill-textsplit.md) | Extract and chunk based on fixed size. <br>Text extraction is free. <br>[Image extraction is billable](https://azure.microsoft.com/pricing/details/search/). | None (built-in) | Azure AI Search | See [Configure access](#configure-access) |
 | [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) | Extract and chunk based on document layout. | [Document Intelligence 4.0](/azure/ai-services/document-intelligence/model-overview?view=doc-intel-4.0.0&preserve-view=true) | [Microsoft Foundry](/azure/ai-services/multi-service-resource?pivots=azportal) | Cognitive Services User |
-| [Azure AI Vision skill](cognitive-search-skill-vision-vectorize.md) | Vectorize text and image content. | [Azure AI Vision multimodal 4.0](/azure/ai-services/computer-vision/concept-image-retrieval) | [Microsoft Foundry](/azure/ai-services/multi-service-resource?pivots=azportal) | Cognitive Services User |
+| [Azure AI Vision skill (preview)](cognitive-search-skill-vision-vectorize.md) | Vectorize text and image content. | [Azure AI Vision multimodal 4.0](/azure/ai-services/computer-vision/concept-image-retrieval) | [Microsoft Foundry](/azure/ai-services/multi-service-resource?pivots=azportal) | Cognitive Services User |
 | [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md)  | Call an LLM to generate text descriptions of image content. | [GPT-5 or GPT-4](/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure) | [Microsoft Foundry](/azure/ai-services/multi-service-resource?pivots=azportal) | Cognitive Services User |
 | [Azure OpenAI embedding skill](cognitive-search-skill-azure-openai-embedding.md) | Vectorize text and generated textual image descriptions. | [Text-embedding-3 or text-embedding-ada-002](/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure#embeddings) | [Microsoft Foundry](/azure/ai-services/multi-service-resource?pivots=azportal) | Cognitive Services User |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダルチュートリアルのAzure AI Visionスキルの更新"
}
```

### Explanation
この変更は、Azure AIのマルチモーダルチュートリアルにおける「Azure AI Vision」スキルの表記を更新し、特にプレビュー機能の状態を明示することを目的としています。

主な変更点は以下の通りです：
- **スキルの状態の明示化**: 「Azure AI Vision」スキルの名前が「Azure AI Vision (preview)」に変更され、現在のプレビュー状態が強調されるようになっています。これにより、ユーザーはこの機能が正式なリリース前のものであることを理解できるようになります。
- **表の整合性**: この変更は、情報表の整合性を保つために行われており、他のスキル名や詳細と一貫性を持たせることで、文書全体の明確さを向上させています。

この更新は、ドキュメンテーションの正確性と最新性を向上させ、ユーザーがAzure AI Visionスキルを適切に利用するための重要な情報を提供することを目的としています。結果的に、ユーザーはより良い判断を下し、プレビュー機能を効果的に利用できるようになります。

## articles/search/vector-search-filters.md{#item-f47c2b}

<details>
<summary>Diff</summary>
````diff
@@ -14,10 +14,7 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!NOTE]
-> `strictPostFilter` is currently in preview. This preview is provided without a service-level agreement and isn't recommended for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> `prefilter` and `postfilter` are generally available in the [latest stable REST API version](/rest/api/searchservice/search-service-api-versions).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
 In Azure AI Search, you can use a [filter expression](search-filters.md) to add inclusion or exclusion criteria to a [vector query](vector-search-how-to-query.md). You can also specify a filtering mode that applies the filter:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索フィルターに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるベクトル検索フィルターに関するドキュメントを更新し、特にフィルタリング機能の状態に関する情報を整理することを目的としています。

主な変更点は以下の通りです：
- **注意書きの簡略化と追加**: `strictPostFilter`についての詳細な情報が削除され、その代わりにプレビュー用語を含むインクルード文が追加されました。これにより、ドキュメントがより簡潔になり、関連する注意事項が一般的なプレビュー用語に統一されます。
- **機能の明確化**: `prefilter` と `postfilter` の一般提供に関する情報が保持されている一方で、サービスレベル契約についての具体的な注意書きが省略されています。これにより、ユーザーがフィルタ機能をより迅速に理解できるようにしています。

この更新は、ユーザーがAzure AI Searchの機能をより効果的に理解し、活用できるようにすることを目的としており、ドキュメントの整合性と明確さを向上させています。結果的に、ユーザーはドキュメントを参照する際の混乱を減らし、最新の情報にアクセスできるようになります。

## articles/search/vector-search-how-to-configure-vectorizer.md{#item-30ffd8}

<details>
<summary>Diff</summary>
````diff
@@ -46,8 +46,8 @@ The following table lists the vectorizers and their supported models and associa
 | Vectorizer | Supported models | Associated skill |
 |-----------------|------------|------------------|
 | [Azure OpenAI](vector-search-vectorizer-azure-open-ai.md) | text-embedding-ada-002<br>text-embedding-3-large<br>text-embedding-3-small | [Azure OpenAI Embedding](cognitive-search-skill-azure-openai-embedding.md) |
-| [Microsoft Foundry model catalog](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) | Cohere-embed-v3-english<br>Cohere-embed-v3-multilingual<br>Cohere-embed-v4 <sup>1</sup> | [AML](cognitive-search-aml-skill.md) |
-| [Azure Vision](vector-search-vectorizer-ai-services-vision.md) | [Multimodal embeddings 4.0 API](/azure/ai-services/computer-vision/concept-image-retrieval) | [Azure Vision multimodal embeddings](cognitive-search-skill-vision-vectorize.md) |
+| [Microsoft Foundry model catalog (preview)](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) | Cohere-embed-v3-english<br>Cohere-embed-v3-multilingual<br>Cohere-embed-v4 <sup>1</sup> | [AML](cognitive-search-aml-skill.md) |
+| [Azure Vision (preview)](vector-search-vectorizer-ai-services-vision.md) | [Multimodal embeddings 4.0 API](/azure/ai-services/computer-vision/concept-image-retrieval) | [Azure Vision multimodal embeddings (preview)](cognitive-search-skill-vision-vectorize.md) |
 | [Custom Web API](vector-search-vectorizer-custom-web-api.md) | Any embedding model (hosted externally) | [Custom Web API](cognitive-search-custom-skill-web-api.md) |
 
 <sup>1</sup> You can only specify `embed-v-4-0` programmatically through the [AML skill](cognitive-search-aml-skill.md) or [Microsoft Foundry model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md), not through the Azure portal. However, you can use the portal to manage the skillset or vectorizer afterward.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のベクトライザーに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azureのベクトル検索のベクトライザー設定に関するドキュメントを更新し、特にプレビュー版のモデルの状態を明確にすることを目的としています。

主な変更点は以下の通りです：
- **名称の明確化**: 「Microsoft Foundryモデルカタログ」と「Azure Vision」の項目がそれぞれ「プレビュー」として明記され、ユーザーがこれらの機能が現行のプレビュー状態であることを理解できるようになっています。
- **テーブルの修正**: 一部のモデルの表現が更新され、これにより、各ベクトライザーに関連するサポートされているモデルや関連スキルがより分かりやすく整理されています。

この更新は、Azure AI Searchユーザーに対して、最新の機能とその使用状況に関する明確な情報を提供し、ドキュメントの整合性とユーザーエクスペリエンスを向上させることを目的としています。結果として、ユーザーはこれらの機能をより適切に利用できるようになります。

## articles/search/vector-search-how-to-query.md{#item-9bb93c}

<details>
<summary>Diff</summary>
````diff
@@ -140,7 +140,7 @@ api-key: {{admin-api-key}}
 This preview supports:
 
 + [`threshold`](#set-thresholds-to-exclude-low-scoring-results-preview) for excluding low-scoring results.
-+ [`hybridSearch.MaxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) for more control over the inputs to a [hybrid query](hybrid-search-how-to-query.md).
++ [`hybridSearch.MaxTextRecallSize`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview) for more control over the inputs to a [hybrid query](hybrid-search-how-to-query.md).
 
 In the following example, the vector is a representation of this string: `"what Azure services support full text search"`. The query targets the `contentVector` field and returns `k` results. The actual vector has 1,536 embeddings, which are trimmed in this example for readability.
 
@@ -496,7 +496,7 @@ POST https://[service-name].search.windows.net/indexes/[index-name]/docs/search?
     } 
 ```
 
-Vector weighting applies to vectors only. The text query in this example, `"hello world"`, has an implicit neutral weight of 1.0. However, in a hybrid query, you can increase or decrease the importance of text fields by setting [maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode).
+Vector weighting applies to vectors only. The text query in this example, `"hello world"`, has an implicit neutral weight of 1.0. However, in a hybrid query, you can increase or decrease the importance of text fields by setting [maxTextRecallSize](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode-preview).
 
 ## Set thresholds to exclude low-scoring results (preview)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のクエリ設定に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azureのベクトル検索におけるクエリ設定に関するドキュメントを更新し、特にプレビュー機能に関連する情報を整備することを目的としています。

主な変更点は以下の通りです：
- **プレビュー機能の明示化**: 新たに追加された`threshold`に関する説明が加わり、低スコアの結果を除外するための設定を明確にしています。また、`hybridSearch.MaxTextRecallSize`においても、プレビュー状態であることを示すために「-preview」が追加されています。これにより、ユーザーが機能の現状をより正確に理解できるようになります。
- **整合性の向上**: 文中のリンクも整理され、プレビュー版での使用方法に対する明確なハンドリングが行われています。これにより、ユーザーは最新の情報を基に自分のニーズに応じたクエリの設定を行いやすくなります。

この更新は、ドキュメントの正確性を向上させ、利用者がAzure AI Searchのクエリ機能をより効果的に活用できるようにすることを目的としています。結果として、ユーザーは新機能に簡単にアクセスでき、適切な設定を行うための理解を深めることができます。

## articles/search/vector-search-integrated-vectorization-ai-studio.md{#item-353fcc}

<details>
<summary>Diff</summary>
````diff
@@ -10,14 +10,13 @@ ms.custom:
 ai-usage: ai-assisted
 ---
 
-# Use embedding models from the Microsoft Foundry model catalog for integrated vectorization
+# Use embedding models from the Microsoft Foundry model catalog for integrated vectorization (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> This feature is in preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The latest preview version of [Skillsets - Create Or Update (REST API)](/rest/api/searchservice/skillsets/create-or-update) supports this feature.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-In this article, you learn how to access embedding models from the [Microsoft Foundry model catalog](/azure/ai-foundry/how-to/model-catalog-overview) for vector conversions during indexing and query execution in Azure AI Search.
+In this article, you learn how to use Microsoft Foundry model catalog models for integrated vectorization (preview) during indexing and query execution in Azure AI Search.
 
 The workflow requires that you deploy a model from the catalog, which includes embedding models from Microsoft and other companies. Deploying a model is billable according to the billing structure of each provider.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "統合ベクトル化に関するドキュメントのプレビュー表記の追加"
}
```

### Explanation
この変更は、Azureの統合ベクトル化に関するドキュメントを更新し、特にプレビュー機能についての情報を強調することを目的としています。

主な変更点は以下の通りです：
- **プレビューの明示**: 「統合ベクトル化」の機能が「プレビュー」であることをタイトルに追加し、利用者がこの機能の現状を把握できるようにしています。
- **重要情報の更新**: 重要事項として、プレビュー条件に関する注釈を追加し、ユーザーが現在の利用規約を理解できるように努めています。特に、プレビュー版の利用条件を示すために新しいインクルードファイルが使用されています。
- **内容の整理**: ドキュメント内のテキストが微調整されており、Microsoft Foundryモデルカタログからのモデルの使用に関する情報がより明確に説明されています。

この更新は、ユーザーがAzure AI Searchの最新機能を理解しやすくし、プレビュー機能に関する注意点を強調することにより、より良い利用体験を提供することを目指しています。結果として、ユーザーは新しい機能に対する意識が高まり、適切な利用方法を把握できるようになります。

## articles/search/vector-search-integrated-vectorization.md{#item-48219d}

<details>
<summary>Diff</summary>
````diff
@@ -62,7 +62,7 @@ For text-to-vector conversion during queries, you take a dependency on these com
     | [AzureOpenAIEmbedding skill](cognitive-search-skill-azure-openai-embedding.md) | [Azure OpenAI vectorizer](vector-search-vectorizer-azure-open-ai.md) |
     | [Custom skill](cognitive-search-custom-skill-web-api.md) | [Custom Web API vectorizer](vector-search-vectorizer-custom-web-api.md) |
     | [Azure Vision multimodal embeddings skill (preview)](cognitive-search-skill-vision-vectorize.md)  | [Azure Vision vectorizer](vector-search-vectorizer-ai-services-vision.md) |
-    | [AML skill pointing to the model catalog in Foundry portal](cognitive-search-aml-skill.md) | [Microsoft Foundry model catalog vectorizer](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) |
+    | [AML skill pointing to the model catalog in Foundry portal](cognitive-search-aml-skill.md) | [Microsoft Foundry model catalog vectorizer (preview)](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) |
 
 ## Component diagram
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル化に関するドキュメントのモデルカタログ情報更新"
}
```

### Explanation
この変更は、Azureのベクトル化に関するドキュメントを更新し、特にMicrosoft Foundryモデルカタログに関する情報を明確にすることを目的としています。

主な変更点は以下の通りです：
- **プレビューの注釈追加**: Microsoft Foundryモデルカタログに関連するベクトル化機能が「プレビュー」として明示され、ユーザーがこの機能の現状を把握できるようになりました。これにより、利用者はこの機能がまだ開発段階にあり、安定性において注意が必要であることを理解できます。
- **内容の整合性向上**: この変更により、ベクトル化に関する情報がアップデートされ、利用者がAzureの各種機能を適切に組み合わせて使用できるよう、文書内の内容の整合性が向上しています。

この更新は、利用者がAzure AI Searchの機能を最大限に活かすための重要な情報を提供し、ベクトル化に関する使い方や注意点をより明確にすることを目指しています。結果として、ユーザーは新しい機能を理解し、適切に活用するための手助けを得られるでしょう。

## articles/search/vector-search-multi-vector-fields.md{#item-9aa482}

<details>
<summary>Diff</summary>
````diff
@@ -6,15 +6,16 @@ ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: concept-article
 ms.date: 03/25/2026
+ai-usage: ai-assisted
 ---
 
-# Multi-vector field support in Azure AI Search
+# Multi-vector field support in Azure AI Search (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-The multi-vector field support feature in Azure AI Search enables you to index multiple child vectors within a single document field. This feature is valuable for use cases like multimodal data or long-form documents, where representing the content with a single vector would lead to loss of important detail.
+The multi-vector field support feature (preview) in Azure AI Search enables you to index multiple child vectors within a single document field. This feature is valuable for use cases like multimodal data or long-form documents, where representing the content with a single vector would lead to loss of important detail.
 
 ## Limitations
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおけるマルチベクトルフィールドのプレビュー表記の追加"
}
```

### Explanation
この変更は、Azure AI Searchにおけるマルチベクトルフィールドのサポートに関するドキュメントを更新し、特にこの機能がプレビュー段階にあることを強調することを目的としています。

主な変更点は以下の通りです：
- **プレビューの明示**: タイトルに「プレビュー」の注記が追加され、機能がまだ開発段階にあることが明確になりました。この明示により、ユーザーはこの機能の利用に際して慎重さが求められることを理解できます。
- **重要情報の更新**: プレビューバージョンに関する新しいインクルードファイルが追加され、利用規約に関するガイダンスが提供されています。これにより、ユーザーは現在の利用条件を把握しやすくなります。
- **内容の修正**: 説明文の中に「プレビュー」という表現が追加され、機能に関する詳細が明確にされています。これは、マルチベクトルフィールドの特徴や利点を強調するために重要です。

この更新により、利用者はAzure AI Searchの新しい機能に対する理解を深め、適切な利用のための情報を得ることができます。また、この情報提供によって、ユーザーは新機能の試用を考慮する際に、リスクについても認識できるようになります。

## articles/search/vector-search-vectorizer-ai-services-vision.md{#item-942a3e}

<details>
<summary>Diff</summary>
````diff
@@ -8,16 +8,16 @@ ms.custom:
 ms.topic: concept-article
 ms.date: 10/23/2025
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
-# Azure Vision vectorizer
+# Azure Vision vectorizer (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> This vectorizer is in preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The latest preview version of [Indexes - Create Or Update](/rest/api/searchservice/indexes/create-or-update) (REST API) supports this feature.
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-The **Azure Vision** vectorizer connects to Azure Vision in Foundry Tools via a [Microsoft Foundry resource](/azure/ai-services/multi-service-resource). At query time, the vectorizer uses the [multimodal embeddings API](/azure/ai-services/computer-vision/concept-image-retrieval) to generate embeddings.
+The **Azure Vision** vectorizer (preview) connects to Azure Vision in Foundry Tools via a [Microsoft Foundry resource](/azure/ai-services/multi-service-resource). At query time, the vectorizer uses the [multimodal embeddings API](/azure/ai-services/computer-vision/concept-image-retrieval) to generate embeddings.
 
 To determine where this model is accessible, see the [region availability for multimodal embeddings](/azure/ai-services/computer-vision/overview-image-analysis?tabs=4-0#region-availability). Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Visionベクトライザーのプレビュー情報追加"
}
```

### Explanation
この変更は、Azure Visionベクトライザーに関するドキュメントを更新し、特にこの機能がプレビュー段階にあることを示すことを目的としています。

主な変更点は以下の通りです：
- **プレビューの明示**: 文書のタイトルに「プレビュー」の表記が追加され、機能の現状が分かりやすくなっています。これにより、ユーザーはこのベクトライザーがまだ開発段階にあり、使用に際しての注意が必要であることを理解できます。
- **重要情報のインクルード**: 新しいインクルードファイルが追加され、プレビュー版の利用規約が示されています。これにより、ユーザーは最新の利用条件を把握しやすくなります。
- **内容の修正**: ベクトライザーの説明が更新され、プレビューであることが明示されています。また、Azure Visionの接続方法や、クエリ時に使用されるAPIについての情報が整理されて提供されています。

この更新により、ユーザーはAzure Visionベクトライザーの機能をより理解しやすくなり、新しい機能を試す際のリスクや利用条件を把握できるようになります。結果として、ユーザーはより informed decision を持ってこの機能を利用することができるでしょう。

## articles/search/vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md{#item-ebe7a3}

<details>
<summary>Diff</summary>
````diff
@@ -8,16 +8,16 @@ ms.custom:
 ms.topic: concept-article
 ms.date: 10/23/2025
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
-# Microsoft Foundry model catalog vectorizer
+# Microsoft Foundry model catalog vectorizer (preview)
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
-> [!IMPORTANT]
-> This vectorizer is in preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). To use this feature, we recommend the latest preview version of [Indexes - Create Or Update (REST API)](/rest/api/searchservice/indexes/create-or-update).
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
 
-The **Microsoft Foundry model catalog** vectorizer connects to an embedding model deployed from the [Foundry model catalog](/azure/ai-foundry/how-to/model-catalog-overview) or an [Azure Machine Learning](../machine-learning/overview-what-is-azure-machine-learning.md) (AML) endpoint. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed.
+The **Microsoft Foundry model catalog** vectorizer (preview) connects to an embedding model deployed from the [Foundry model catalog](/azure/ai-foundry/how-to/model-catalog-overview) or an [Azure Machine Learning](../machine-learning/overview-what-is-azure-machine-learning.md) (AML) endpoint. Your data is processed in the [Geo](https://azure.microsoft.com/explore/global-infrastructure/data-residency/) where your model is deployed.
 
 If you're using integrated vectorization to create the vector arrays, the skillset should include an [AML skill](cognitive-search-aml-skill.md) that points to the same model specified in the vectorizer.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Foundryモデルカタログベクトライザーのプレビュー情報追加"
}
```

### Explanation
この変更は、Microsoft Foundryモデルカタログに関連するベクトライザーに関するドキュメントを更新し、特にこの機能がプレビュー段階にあることを示すことを目的としています。

主な変更点は以下の通りです：
- **プレビューの明示**: ベクトライザーのタイトルに「プレビュー」の表記が追加され、この機能がまだ開発段階にあることを明確にしています。これにより、利用者はこの機能の使用に際しての注意を促されます。
- **重要情報の更新**: 新たにインクルードされた文書が、プレビュー版の利用規約に関する情報を提供しています。これにより、ユーザーは最新の規約を理解するのに役立ちます。
- **内容の修正**: 文書内の説明文が更新され、ベクトライザーがプレビューであることが強調されています。また、Microsoft FoundryモデルカタログとAzure Machine Learningとの接続についての情報が整理されています。

この更新により、ユーザーはMicrosoft Foundryモデルカタログに関するベクトライザーの機能をより良く理解し、新しい機能を利用する際のリスクや利用条件を把握できるようになります。結果として、ユーザーは informed decision を持ってこの機能を利用できるでしょう。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -17,15 +17,12 @@ ai-usage: ai-assisted
 
 [!INCLUDE [search-fiq-banner](./includes/search-fiq-banner.md)]
 
+[!INCLUDE [preview-terms](./includes/previews/preview-terms.md)]
+
 Learn about the latest updates to Azure AI Search functionality, documentation, and samples.
 
 ## August 2026
 
-> [!IMPORTANT]
-> These features and functionality are part of the 2026-08-01-preview REST API. The 2026-08-01-preview is licensed to you as part of your Azure subscription and is subject to the terms applicable to "Previews" in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), the [Microsoft Products and Services Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA) ("DPA"), and the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
->
-> The 2026-08-01-preview supports connections to other Microsoft services and third-party services. Use of these services is subject to their respective terms and might result in data processing or storage outside of the Azure compliance boundary, as well as data flowing into the Azure compliance boundary.
-
 | Item | Description |
 |--|--|
 | [Search Service 2026-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-08-01-preview&preserve-view=true) | New preview REST API version providing programmatic access to the data plane operations described in this table. |
@@ -119,11 +116,11 @@ Learn about the latest updates to Azure AI Search functionality, documentation,
 | November | [Foundry IQ (preview)](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) | New integration that allows agents in Foundry Agent Service to invoke knowledge bases in Azure AI Search. Foundry IQ offloads complex retrieval operations to the knowledge base, enabling the agent to provide accurate, citation-backed responses based on enterprise data and web sources. |
 | November | Skills | [Azure Content Understanding skill (preview)](cognitive-search-skill-content-understanding.md) wraps Azure Content Understanding in Foundry Tools to extract structured Markdown from text, images, PDFs, Microsoft PowerPoint, Microsoft Word, and more. This skill provides advanced document parsing with better table extraction (including cross-page tables), image descriptions, and semantic chunking. For indexed knowledge sources, this skill is available through the `contentExtractionMode` property within `ingestionParameters`. |
 | November | Security | [SharePoint indexer ACL support (preview)](search-indexer-sharepoint-access-control-lists.md) extends ACL support to flow basic SharePoint permissions to indexed documents, enabling document-level access control. |
-| November | Security | [Elevated read permissions for ACLs (preview)](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results). New capability to assign elevated read permissions to administrators for investigating problems with ACL configurations used in document access control. |
+| November | Security | [Elevated read permissions for ACLs (preview)](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results-preview). New capability to assign elevated read permissions to administrators for investigating problems with ACL configurations used in document access control. |
 | November | Security | [Document-level sensitivity label indexing (preview)](search-indexer-sensitivity-labels.md). New integration with Microsoft Purview to sync document sensitivity labels to the index, honoring their labels and protection at query time for data governance. |
 | November | SharePoint | [SharePoint indexing updates (preview)](search-how-to-index-sharepoint-online.md). New SharePoint indexer capabilities, including improved authentication options, incremental updates, and basic handling of document permissions. |
 | November | Queries | [Scoring function aggregation (preview)](index-add-scoring-profiles.md#example-function-aggregation). New capability to combine and aggregate multiple scoring functions, enabling more sophisticated relevance customization and weighted signal combination. |
-| November | Queries | [Facet aggregations (preview)](search-faceted-navigation-examples.md#facet-aggregation-example). New facet aggregation operations, including minimum, maximum, average, and cardinality, provide enhanced analytics in faceted search experiences. |
+| November | Queries | [Facet aggregations (preview)](search-faceted-navigation-examples.md#facet-aggregation-example-preview). New facet aggregation operations, including minimum, maximum, average, and cardinality, provide enhanced analytics in faceted search experiences. |
 | November | Endpoints | `azure-api.net` endpoint support (preview). The [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md) and [Azure OpenAI vectorizer](vector-search-vectorizer-azure-open-ai.md) now accept `azure-api.net` endpoints for Azure API Management (not custom endpoints). |
 | November | Endpoints | `services.ai.azure.com` endpoint support. The [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md), [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md), [Azure OpenAI vectorizer](vector-search-vectorizer-azure-open-ai.md), and [AI enrichment](cognitive-search-concept-intro.md) now accept `services.ai.azure.com` endpoints for Microsoft Foundry resources. When you [upgrade from Azure OpenAI to Foundry](/azure/ai-foundry/how-to/upgrade-azure-openai), a new project is automatically created and becomes available for RAG and multimodal RAG in the [**Import data (new)** wizard](search-import-data-portal.md). |
 | September | REST API | [Search Service 2025-09-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-09-01&preserve-view=true). New stable REST API version supports general availability for Microsoft OneLake indexer, Document Layout skill, and other APIs. |
@@ -169,7 +166,7 @@ Learn about the latest updates to Azure AI Search functionality, documentation,
 | March | Pricing | [Pricing tier change (preview)](search-capacity-planning.md#change-your-pricing-tier). Change the [pricing tier](search-sku-tier.md) of your search service. This provides flexibility to scale storage, increase request throughput, and decrease latency based on your needs. Initially, this preview only supported upgrades between Basic and Standard (S1, S2, and S3) tiers, but starting in July 2025, it supports upgrades *and* downgrades between these tiers. Available in [Update Service (2025-02-01-preview)](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true#searchupdateservicewithsku) and the Azure portal. |
 | March | Queries | [Facet hierarchies, aggregations, and facet filters (preview)](search-faceted-navigation-examples.md). New facet query parameters support nested facets. For numeric facetable fields, you can sum the values of each field. You can also specify filters on a facet to add inclusion or exclusion criteria. Available in [Search Documents (2025-03-01-preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-03-01-preview&preserve-view=true) and the Azure portal.|
 | March | Vector search | [Rescore vector queries over binary quantization using full precision vectors (preview)](vector-search-how-to-quantization.md#supported-rescoring-techniques). For vector indexes that contain binary quantization, you can rescore query results using a full precision vector query. The query engine uses the dot product of the binary embeddings and the vector query for rescoring, which improves the quality of search results.  Set `enableRescoring` and `discardOriginals` to use this feature, and call the latest preview API version on the request.|
-| March | Queries | [Semantic ranker prerelease models (preview)](semantic-how-to-configure.md#opt-in-for-prerelease-semantic-ranking-models). Opt in to use prerelease semantic ranker models if one happens to be available in your region. Available in [Create or Update Index (2025-03-01-preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true#semanticconfiguration).|
+| March | Queries | [Semantic ranker prerelease models (preview)](semantic-how-to-configure.md#opt-in-for-prerelease-semantic-ranking-models-preview). Opt in to use prerelease semantic ranker models if one happens to be available in your region. Available in [Create or Update Index (2025-03-01-preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true#semanticconfiguration).|
 | March | REST API | [Search Service REST 2025-03-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-03-01-preview&preserve-view=true). Preview release of REST APIs for data plane operations. Adds support for multi-vector embeddings, hierarchical facets, facet aggregation, and facet filters. |
 | March | REST API | [Search Management 2025-02-01-preview](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true). Preview release of REST APIs for control plane operations. Adds support for in-place upgrade to higher capacity partitions, in-place upgrade to higher tiers, and Azure Confidential Compute. |
 | February | Security | [Customer-managed keys support for Managed HSM](search-security-manage-encryption-keys.md). Use either Azure Key Vault or Azure Key Vault Managed HSM (Hardware Security Module) to store customer-managed keys for extra encryption of sensitive content. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search 更新情報の修正"
}
```

### Explanation
この変更は、Azure AI Search に関する最新情報のドキュメントに対する修正を行い、特にプレビュー機能や新しい機能に関する情報を整備することを目的としています。

主な変更点は以下の通りです：
- **プレビューの強調**: 更新情報にプレビューに関する注記が加わり、特定の日付のREST API版がプレビューであることを明示しています。これにより、ユーザーは新しい機能が完全に安定したものではなく、注意が必要であることを認識できます。
- **重要情報の整理**: プレビュー版の利用に関する重要なライセンス条項が削除され、一部の詳細が新しいインクルードファイルへのリンクで置き換えられました。これにより、重要な情報が分かりやすく整理されています。
- **新機能の明記**: 更新情報には、複数の新機能や改善点に関する詳細が追加されており、特にセキュリティ、エンドポイント、およびクエリに関連した新機能が一覧化されています。また、すでにプレビューとして発表されている機能についても明示的に「プレビュー」と註記されています。

この更新によって、ユーザーはAzure AI Searchの新しい機能や更新内容をより簡単に把握できるようになり、いかにそれを利用すべきかについての理解が深まることが期待されます。


