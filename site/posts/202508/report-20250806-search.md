---
date: '2025-08-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:88b6cf1...MicrosoftDocs:10d2435
summary: 今回の変更では、Azure AI Searchに関連するドキュメントからいくつかのメタデータフィールドが削除され、ドキュメントの整理とコンテンツの明確化が図られています。具体的には、著者情報やメソッド名の更新が行われ、情報の正確性が向上しました。メタデータの削除によって、既存のプロセスやスクリプトに影響が出る可能性がありますが、目立った破壊的変更はありません。全体として、このメンテナンスは読者が必要な情報を効率的に取得できるようにし、技術的内容の正確さを保つための重要な取り組みとなっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:88b6cf1...MicrosoftDocs:10d2435){target="_blank"}

<format>
# Highlights
今回の変更では、Azure AI Searchに関連する多数のドキュメントにおいて、`author`、`ms.author`、`manager`、`ms.service`といったメタデータフィールドが一斉に削除されていることが共通しています。これは、ドキュメントの整理とコンテンツの明確化を目的としており、メタ情報が主題の理解に影響を及ぼさないようにする小規模な改訂です。

## New features
特定のドキュメントではメソッド名の更新や著者情報の変更（例: `eric-urban` から `HeidiSteen` への変更）が行われ、情報の正確性が改善されています。

## Breaking changes
目立った破壊的変更はありませんが、メタデータの削除により、ドキュメントのメタ情報を参照する既存のプロセスやスクリプトが影響を受ける可能性があります。

## Other updates
多くのドキュメントでは、メタデータの削除を通じてシンプルさと集中力を高める意図が伺えます。それらの多くは、ベクター検索、セキュリティ、データインデクシング、生成AIなどの技術的な主題を扱っています。

# Insights
今回のメタデータ削除は、Azure AI Search関連ドキュメントのクリーンアップおよび利便性改善の一環として捉えることができます。特に、メタデータフィールドの削除により、ドキュメントはよりシンプルで、読者が内容に直接フォーカスしやすい構成になりました。これにより、ユーザーは技術的な詳細により明確にアクセスできるようになります。

さらに、これらの変更は、メタデータがドキュメントの主な目的や技術的内容とは直接関係がないと判断された場合に行われたものと推測されます。著者情報の更新については、文書の権威性と信頼性を保証するために有効です。結果として、読者は一貫した内容を期待しつつ、最新の情報に基づいて作業することが可能になります。

このようなドキュメントのメンテナンスは、読者が必要な情報を効率的に取得できるようにするだけでなく、ドキュメント自体の価値を高め、全体的なユーザー体験を向上させるために重要といえます。情報の提供は、技術的内容の正確さが特に求められる領域であるため、こうした継続的改良は不可欠です。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-aml-skill.md](#item-51366c) | minor update | 著者情報の削除 | modified | 0 | 1 | 1 | 
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | 著者情報の更新 | modified | 2 | 2 | 4 | 
| [cognitive-search-common-errors-warnings.md](#item-a5c854) | minor update | マネージャー情報の削除 | modified | 0 | 1 | 1 | 
| [cognitive-search-concept-intro.md](#item-bf9ed7) | minor update | マネージャー情報の削除 | modified | 0 | 1 | 1 | 
| [cognitive-search-custom-skill-scale.md](#item-efc3d8) | minor update | 著者情報の削除 | modified | 0 | 1 | 1 | 
| [cognitive-search-debug-session.md](#item-edf092) | minor update | マネージャーおよび著者情報の削除 | modified | 0 | 1 | 1 | 
| [cognitive-search-how-to-debug-skillset.md](#item-31db42) | minor update | マネージャーおよび著者情報の削除 | modified | 0 | 1 | 1 | 
| [cognitive-search-skill-annotation-language.md](#item-aaedc7) | minor update | 著者およびサービス情報の削除 | modified | 0 | 1 | 1 | 
| [cognitive-search-skill-document-extraction.md](#item-072b72) | minor update | 著者およびサービス情報の削除 | modified | 0 | 2 | 2 | 
| [cognitive-search-skill-document-intelligence-layout.md](#item-62c06f) | minor update | 著者およびサービス情報の削除 | modified | 0 | 2 | 2 | 
| [cognitive-search-skill-image-analysis.md](#item-07daa8) | minor update | 著者およびサービス情報の削除 | modified | 0 | 2 | 2 | 
| [cognitive-search-skill-ocr.md](#item-259256) | minor update | 著者およびサービス情報の削除 | modified | 0 | 2 | 2 | 
| [cognitive-search-skill-pii-detection.md](#item-c7cc73) | minor update | マネージャー情報の削除 | modified | 0 | 1 | 1 | 
| [cognitive-search-skill-sentiment-v3.md](#item-bb46e0) | minor update | 著者情報の削除 | modified | 0 | 1 | 1 | 
| [cognitive-search-skill-text-translation.md](#item-b42884) | minor update | マネージャー情報の削除 | modified | 0 | 1 | 1 | 
| [cognitive-search-tutorial-debug-sessions.md](#item-7e10e9) | minor update | 著者およびマネージャー情報の削除 | modified | 0 | 1 | 1 | 
| [hybrid-search-how-to-query.md](#item-345ce6) | minor update | 著者情報およびサービス情報の削除 | modified | 0 | 1 | 1 | 
| [hybrid-search-overview.md](#item-6987b4) | minor update | 著者情報およびサービス情報の削除 | modified | 0 | 1 | 1 | 
| [hybrid-search-ranking.md](#item-dad887) | minor update | 著者情報およびサービス情報の削除 | modified | 0 | 1 | 1 | 
| [preview-generic.md](#item-51bbcc) | minor update | 著者情報の更新 | modified | 2 | 2 | 4 | 
| [resource-authentication.md](#item-381ff1) | minor update | 著者情報の更新 | modified | 2 | 2 | 4 | 
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | 管理者情報の削除 | modified | 0 | 1 | 1 | 
| [index-add-suggesters.md](#item-28ed57) | minor update | 管理者情報の削除 | modified | 0 | 1 | 1 | 
| [index-similarity-and-scoring.md](#item-75603d) | minor update | 著者情報の削除 | modified | 0 | 1 | 1 | 
| [knowledge-store-projection-example-long.md](#item-e18999) | minor update | 管理者および著者情報の削除 | modified | 0 | 1 | 1 | 
| [knowledge-store-projection-overview.md](#item-81aa4a) | minor update | 管理者および著者情報の削除 | modified | 0 | 1 | 1 | 
| [knowledge-store-projections-examples.md](#item-9bfff5) | minor update | 管理者および著者情報の削除 | modified | 0 | 1 | 1 | 
| [query-lucene-syntax.md](#item-736436) | minor update | 管理者および著者情報の削除 | modified | 0 | 1 | 1 | 
| [query-odata-filter-orderby-syntax.md](#item-6ab74f) | minor update | 著者およびサービス情報の削除 | modified | 0 | 1 | 1 | 
| [query-simple-syntax.md](#item-ab3c96) | minor update | 管理者および著者情報の削除 | modified | 0 | 1 | 1 | 
| [reference-stopwords.md](#item-63e4b3) | minor update | 著者および管理者情報の削除と文章の修正 | modified | 1 | 3 | 4 | 
| [resource-tools.md](#item-0c6ac1) | minor update | 著者情報の削除 | modified | 0 | 1 | 1 | 
| [resource-training.md](#item-07788d) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-add-autocomplete-suggestions.md](#item-0a43e0) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-agentic-retrieval-how-to-create.md](#item-310fbe) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-agentic-retrieval-how-to-index.md](#item-a078ea) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-agentic-retrieval-how-to-pipeline.md](#item-1ad1c3) | minor update | メソッド名の更新 | modified | 1 | 1 | 2 | 
| [search-agentic-retrieval-how-to-retrieve.md](#item-5f7fc0) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-api-migration.md](#item-07297b) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-api-preview.md](#item-511f5d) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-api-versions.md](#item-69ca3e) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-blob-storage-integration.md](#item-bbdaa6) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-capacity-planning.md](#item-0dd6c9) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-create-service-portal.md](#item-f90159) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-data-sources-gallery.md](#item-18727f) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-dotnet-mgmt-sdk-migration.md](#item-bcb84f) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-dotnet-sdk-migration-version-11.md](#item-5ca9e8) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-faceted-navigation-examples.md](#item-2b1158) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-faceted-navigation.md](#item-f29d1e) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-features-list.md](#item-d34448) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-filters.md](#item-3f2a7a) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-how-to-create-indexers.md](#item-de71fb) | minor update | 著者および管理者情報の削除とメタデータの一部修正 | modified | 0 | 2 | 2 | 
| [search-how-to-dotnet-sdk.md](#item-5333eb) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-how-to-index-csv-blobs.md](#item-2c3f3e) | minor update | 著者および管理者情報の削除とメタデータの修正 | modified | 0 | 2 | 2 | 
| [search-how-to-index-markdown-blobs.md](#item-c94a20) | minor update | 著者情報およびメタデータの削除 | modified | 0 | 2 | 2 | 
| [search-how-to-index-sql-database.md](#item-86d873) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-how-to-index-sql-managed-instance.md](#item-009ccc) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-how-to-index-sql-server.md](#item-d7fb35) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-how-to-large-index.md](#item-d34e42) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-how-to-load-search-index.md](#item-a72573) | minor update | メタデータの削除 | modified | 0 | 2 | 2 | 
| [search-howto-complex-data-types.md](#item-75a002) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-howto-concurrency.md](#item-863358) | minor update | 著者および管理者情報の削除 | modified | 0 | 1 | 1 | 
| [search-howto-index-changed-deleted-blobs.md](#item-32a688) | minor update | メタデータ情報の削除 | modified | 0 | 1 | 1 | 
| [search-howto-index-cosmosdb-gremlin.md](#item-698c99) | minor update | メタデータ情報の削除 | modified | 0 | 2 | 2 | 
| [search-howto-index-cosmosdb.md](#item-568fab) | minor update | メタデータ情報の削除 | modified | 0 | 1 | 1 | 
| [search-howto-index-encrypted-blobs.md](#item-a7097a) | minor update | メタデータ情報の削除 | modified | 0 | 1 | 1 | 
| [search-howto-index-json-blobs.md](#item-b8230c) | minor update | メタデータの削除と整理 | modified | 0 | 2 | 2 | 
| [search-howto-index-mysql.md](#item-5d31c4) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-howto-index-one-to-many-blobs.md](#item-04ada2) | minor update | メタデータの簡素化 | modified | 0 | 2 | 2 | 
| [search-howto-index-plaintext-blobs.md](#item-63efcb) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-howto-index-sharepoint-online.md](#item-49ff6e) | minor update | メタデータの簡素化 | modified | 0 | 1 | 1 | 
| [search-howto-indexing-azure-blob-storage.md](#item-dc4668) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-howto-indexing-azure-tables.md](#item-7655b0) | minor update | メタデータの簡素化 | modified | 0 | 2 | 2 | 
| [search-howto-managed-identities-azure-functions.md](#item-2f13c4) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-howto-managed-identities-cosmos-db.md](#item-a74464) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-howto-managed-identities-data-sources.md](#item-edf98d) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-howto-managed-identities-storage.md](#item-8209c4) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-howto-monitor-indexers.md](#item-0e3133) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-howto-move-across-regions.md](#item-bcecf6) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-howto-reindex.md](#item-46738a) | minor update | メタデータの削除 | modified | 0 | 2 | 2 | 
| [search-index-azure-sql-managed-instance-with-managed-identity.md](#item-a4ec86) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-indexer-field-mappings.md](#item-0e4628) | minor update | メタデータの削除 | modified | 0 | 2 | 2 | 
| [search-indexer-how-to-access-private-sql.md](#item-1bd4cc) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-indexer-howto-access-ip-restricted.md](#item-aec22f) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-indexer-howto-access-trusted-service-exception.md](#item-e19826) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-indexer-overview.md](#item-292796) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-indexer-securing-resources.md](#item-c075c4) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-indexer-troubleshooting.md](#item-087365) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-indexer-tutorial.md](#item-a3e3ff) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-language-support.md](#item-a7979b) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-manage-azure-cli.md](#item-7fdd08) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-manage-powershell.md](#item-3c3485) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-markdown-data-tutorial.md](#item-32ea2a) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-monitor-enable-logging.md](#item-e3600e) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-monitor-logs-powerbi.md](#item-5b3491) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-monitor-queries.md](#item-279569) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-more-like-this.md](#item-56c565) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-pagination-page-layout.md](#item-115902) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-create.md](#item-532822) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-fuzzy.md](#item-a130e3) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-lucene-examples.md](#item-ce3624) | minor update | メタデータの削除 | modified | 0 | 2 | 2 | 
| [search-query-odata-collection-operators.md](#item-9fba57) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-odata-comparison-operators.md](#item-c92abf) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-odata-filter.md](#item-69d5d6) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-odata-full-text-search-functions.md](#item-5748d4) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-odata-geo-spatial-functions.md](#item-859407) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-odata-logical-operators.md](#item-61c263) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-odata-orderby.md](#item-dff8d3) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-odata-search-in-function.md](#item-d768e7) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-odata-search-score-function.md](#item-f51766) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-odata-select.md](#item-8d6e1d) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-odata-syntax-reference.md](#item-14b8d9) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-overview.md](#item-dcd5d6) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-partial-matching.md](#item-bd97dc) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-simple-examples.md](#item-834766) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-troubleshoot-collection-filters.md](#item-abeca4) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-query-understand-collection-filters.md](#item-32c01a) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-relevance-overview.md](#item-cb0e09) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-security-get-encryption-keys.md](#item-7aed9d) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-security-overview.md](#item-6b3f1e) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-security-trimming-for-azure-search.md](#item-d8ae51) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-semi-structured-data.md](#item-d3388d) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-sku-tier.md](#item-7686b8) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-synapseml-cognitive-services.md](#item-dcc36f) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-synonyms.md](#item-2d5d63) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-try-for-free.md](#item-36e28d) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-what-is-an-index.md](#item-5a3344) | minor update | メタデータの削除 | modified | 0 | 2 | 2 | 
| [search-what-is-azure-search.md](#item-93853a) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [search-what-is-data-import.md](#item-d73ef5) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [semantic-answers.md](#item-c3fee9) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [semantic-how-to-enable-disable.md](#item-71ac1e) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [semantic-how-to-query-request.md](#item-85530d) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [semantic-how-to-query-rewrite.md](#item-3e168f) | minor update | 著者情報の更新 | modified | 2 | 2 | 4 | 
| [semantic-search-overview.md](#item-b7497b) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [service-configure-firewall.md](#item-75be3f) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [speller-how-to-add.md](#item-9b4502) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [troubleshoot-shared-private-link-resources.md](#item-0e1867) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [tutorial-csharp-create-mvc-app.md](#item-608a5d) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [tutorial-document-extraction-image-verbalization.md](#item-398a90) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [tutorial-document-extraction-multimodal-embeddings.md](#item-a3db59) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [tutorial-document-layout-image-verbalization.md](#item-f5de57) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [tutorial-document-layout-multimodal-embeddings.md](#item-f67371) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [tutorial-rag-build-solution-index-schema.md](#item-9a17ca) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [tutorial-rag-build-solution-maximize-relevance.md](#item-2fdb09) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [tutorial-rag-build-solution-minimize-storage.md](#item-088ad8) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [tutorial-rag-build-solution-pipeline.md](#item-25ce01) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [tutorial-rag-build-solution-query.md](#item-93965f) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [tutorial-rag-build-solution.md](#item-c7eca4) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-how-to-assign-narrow-data-types.md](#item-6b81cd) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-how-to-chunk-documents.md](#item-b79133) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-how-to-configure-compression-storage.md](#item-c653c3) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-how-to-configure-vectorizer.md](#item-30ffd8) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-how-to-create-index.md](#item-97c769) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-how-to-generate-embeddings.md](#item-e98f7b) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-how-to-index-binary-data.md](#item-b233b9) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-how-to-quantization.md](#item-744f48) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-how-to-query.md](#item-9bb93c) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-how-to-storage-options.md](#item-ee1680) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-how-to-truncate-dimensions.md](#item-8350a3) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-index-size.md](#item-bb2846) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-integrated-vectorization.md](#item-48219d) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-overview.md](#item-56e5fa) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-search-ranking.md](#item-0764d8) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 
| [vector-store.md](#item-db9b8c) | minor update | メタデータの削除 | modified | 0 | 1 | 1 | 


# Modified Contents
## articles/search/cognitive-search-aml-skill.md{#item-51366c}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Custom AML skill in skillsets
 titleSuffix: Azure AI Search
 description: Extend capabilities of Azure AI Search skillsets with Azure Machine Learning models.
-
 author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-aml-skill.md` ドキュメント内での著者情報の削除を反映しています。具体的には、ドキュメントの2行目にあった著者情報である `author: gmndrg` が削除され、代わりに `ms.author: gimondra` と `ms.service: azure-ai-search` が残されています。この小規模な更新はドキュメントの整理と一貫性を向上させることを目的としています。

## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -2,8 +2,8 @@
 title: Attach Azure AI services to a skillset
 titleSuffix: Azure AI Search
 description: Learn how to attach an Azure AI services resource to an AI enrichment pipeline in Azure AI Search.
-author: eric-urban 
-ms.author: eur 
+author: HeidiSteen 
+ms.author: heidist 
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 06/11/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報の更新"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-attach-cognitive-services.md` ドキュメント内での著者情報の更新を行っています。具体的には、元の著者 `author: eric-urban` と `ms.author: eur` が、`author: HeidiSteen` と `ms.author: heidist` に変更されています。この変更により、ドキュメントの著者情報が更新され、より関連性のある情報が提供されるようになります。また、全体としての文書の明確性と正確性を向上させるための小規模な改訂です。

## articles/search/cognitive-search-common-errors-warnings.md{#item-a5c854}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Indexer errors and warnings
 titleSuffix: Azure AI Search
 description: This article provides information and solutions to common errors and warnings you might encounter during AI enrichment in Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージャー情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-common-errors-warnings.md` ドキュメント内でのマネージャー情報の削除を反映しています。具体的には、元の情報 `manager: nitinme` が削除された一方で、著者情報 `author: HeidiSteen` と `ms.author: heidist` はそのままとなっています。このマイナーな更新により、ドキュメントが簡潔になり、関連情報が整理されています。

## articles/search/cognitive-search-concept-intro.md{#item-bf9ed7}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: AI enrichment concepts
 titleSuffix: Azure AI Search
 description: Content extraction, natural language processing (NLP), and image processing can create searchable content in Azure AI Search indexes.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージャー情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-concept-intro.md` ドキュメントにおいて、マネージャー情報の削除を行っています。具体的には、行頭にあった `manager: nitinme` の行が削除され、著者情報 `author: HeidiSteen` と `ms.author: heidist` はそのままとなっています。この更新により、ドキュメントがよりシンプルになり、重要な情報に焦点が当てられるようになります。内容の明確性を向上させるための小さな修正です。

## articles/search/cognitive-search-custom-skill-scale.md{#item-efc3d8}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'Scale and manage custom skill'
 titleSuffix: Azure AI Search
 description: Learn the tools and techniques for efficiently scaling out a custom skill for maximum throughput. Custom skills invoke custom AI models or logic that you can add to an AI-enriched indexing pipeline in Azure AI Search.
-
 author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-custom-skill-scale.md` ドキュメントにおいて、著者情報の削除を行っています。具体的には、元の情報 `author: gmndrg` と `ms.author: gimondra` 、および `ms.service: azure-ai-search` の行が削除されました。この更新により、ドキュメントがより簡潔になり、著者に関する情報が省かれたことで、内容の主旨に焦点が当たるようになっています。これは、情報の整理と明確性を向上させるための小さな修正です。

## articles/search/cognitive-search-debug-session.md{#item-edf092}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Debug Sessions concepts
 titleSuffix: Azure AI Search
 description: Debug Sessions, accessed through the Azure portal, provides an IDE-like environment where you can identify and fix errors, validate changes, and push changes to skillsets in an Azure AI Search enrichment pipeline.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージャーおよび著者情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-debug-session.md` ドキュメントにおいて、マネージャーおよび著者の情報を削除するものです。具体的には、行頭にあった `manager: nitinme` と `author: HeidiSteen` 、および `ms.author: heidist` の行が削除されました。この修正により、ドキュメントがよりフォーカスされた内容になり、著者やマネージャー情報による情報の分散を避けることができます。これは、利用者にとって内容がより明確で理解しやすくなることを目的とした小さな更新です。

## articles/search/cognitive-search-how-to-debug-skillset.md{#item-31db42}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Debug a skillset
 titleSuffix: Azure AI Search
 description: Learn how to troubleshoot Azure AI Search skillset errors and issues by using a debug session in Azure portal.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージャーおよび著者情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-how-to-debug-skillset.md` ドキュメントにおいて、マネージャーおよび著者の情報を削除するものです。具体的には、行にあった `manager: nitinme` と `author: HeidiSteen` 、および `ms.author: heidist` の行が削除されました。これにより、ドキュメントはよりシンプルになり、内容の理解を妨げることなく、利用者が重要な情報に注目できるようになります。この変更は、情報の整理と明確さの向上を目的とした小さな更新です。

## articles/search/cognitive-search-skill-annotation-language.md{#item-aaedc7}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Skill context and input annotation reference language
 titleSuffix: Azure AI Search
 description: Annotation syntax reference for annotation in the context, inputs, and outputs of a skillset in an AI enrichment pipeline in Azure AI Search.
-
 author: BertrandLeRoy
 ms.author: beleroy
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者およびサービス情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-annotation-language.md` ドキュメントにおいて、著者およびサービスの情報を削除するものです。具体的には、`author: BertrandLeRoy` 、`ms.author: beleroy` 、および `ms.service: azure-ai-search` の行が削除されました。この修正により、文書がより洗練された内容になり、利用者が核心に集中しやすくなります。情報の簡潔さを高めることで、ドキュメントの利便性が向上し、読者が重要な情報にアクセスしやすくなることを目的とした小さな更新です。

## articles/search/cognitive-search-skill-document-extraction.md{#item-072b72}

<details>
<summary>Diff</summary>
````diff
@@ -2,10 +2,8 @@
 title: Document Extraction cognitive skill
 titleSuffix: Azure AI Search
 description: Extracts content from a file within the enrichment pipeline.
-
 author: gmndrg
 ms.author: gimondra
-
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者およびサービス情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-document-extraction.md` ドキュメントにおいて、著者およびサービスに関する情報を削除するものです。具体的には、`author: gmndrg` 、`ms.author: gimondra` 、および `ms.service: azure-ai-search` の行が削除されました。この修正により、ドキュメントがよりスッキリとし、利用者が重要な情報に集中できるようになります。また、`ms.custom` フィールドに含まれている `ignite-2023` はそのまま残っているため、特定のカスタム設定についての情報は依然として保持されています。この変更は、情報の整理とドキュメントの明確さを向上させることを目的とした小規模な更新です。

## articles/search/cognitive-search-skill-document-intelligence-layout.md{#item-62c06f}

<details>
<summary>Diff</summary>
````diff
@@ -2,10 +2,8 @@
 title: Document Layout skill
 titleSuffix: Azure AI Search
 description: Analyze a document to extract regions of interest and their inter-relationships to produce a syntactical representation (markdown format) in an enrichment pipeline in Azure AI Search.
-
 author: rawan
 ms.author: rawan
-
 ms.service: azure-ai-search
 ms.custom:
   - references_regions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者およびサービス情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-document-intelligence-layout.md` ドキュメントにおいて、著者やサービスに関する情報を削除するもので、具体的には `author: rawan` および `ms.author: rawan`、そして `ms.service: azure-ai-search` の行が削除されました。これにより、ドキュメントがよりコンパクトで読みやすくなり、利用者が内容に集中しやすくなります。また、`ms.custom` フィールドに残された `references_regions` については、特定のカスタム設定に関する情報が引き続き保持されています。この修正は、情報の整理とドキュメントの明確化を目的とした小規模な更新です。

## articles/search/cognitive-search-skill-image-analysis.md{#item-07daa8}

<details>
<summary>Diff</summary>
````diff
@@ -2,10 +2,8 @@
 title: Image Analysis cognitive skill
 titleSuffix: Azure AI Search
 description: Extract semantic text through image analysis using the Image Analysis cognitive skill in an AI enrichment pipeline in Azure AI Search.
-
 author: gmndrg
 ms.author: gimondra
-
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者およびサービス情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-image-analysis.md` ドキュメントにおいて、著者及びサービスに関連する情報を削除するもので、具体的には `author: gmndrg`、`ms.author: gimondra`、および `ms.service: azure-ai-search` の行が削除されました。この更新により、ドキュメントがより整理され、余計な情報が削除されることで、利用者が重要な内容に集中しやすくなります。また、`ms.custom` フィールドに残された `ignite-2023` は、特定のカスタム設定についての情報が依然として保持されています。この修正は、ドキュメントの明確さを向上させる小規模な更新です。

## articles/search/cognitive-search-skill-ocr.md{#item-259256}

<details>
<summary>Diff</summary>
````diff
@@ -2,10 +2,8 @@
 title: OCR skill
 titleSuffix: Azure AI Search
 description: Extract text from image files using optical character recognition (OCR) in an enrichment pipeline in Azure AI Search.
-
 author: gmndrg
 ms.author: gimondra
-
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者およびサービス情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-ocr.md` ドキュメントで行われ、著者及びサービスに関連する情報が削除されました。具体的には、`author: gmndrg`、`ms.author: gimondra`、および `ms.service: azure-ai-search` の行が取り除かれています。この修正により、ドキュメントがよりシンプルになり、余分な情報が排除されることで、利用者はコアな内容により集中しやすくなります。なお、`ms.custom` フィールドに記載されている `ignite-2023` は、そのまま保持されており、カスタム設定に関する情報は続投されています。この修正は、ドキュメントの整然さを高めるための小規模な更新です。

## articles/search/cognitive-search-skill-pii-detection.md{#item-c7cc73}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: PII Detection cognitive skill
 titleSuffix: Azure AI Search
 description: Extract and mask personal information from text in an enrichment pipeline in Azure AI Search.
-
 manager: nitinme
 author: gmndrg
 ms.author: gimondra
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージャー情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-pii-detection.md` ドキュメントにおいて、マネージャーに関する情報が削除されています。具体的には、行 `manager: nitinme` が取り除かれ、著者や共同著者に関連する情報も保持されました。この修正により、ドキュメントはより簡潔で分かりやすくなり、読者が主要な内容に集中しやすくなります。著者情報が変更されない限り、ドキュメントの他の部分はそのまま維持されており、機能には特に影響を与えません。この更新は、ドキュメントの可読性を向上させるための小規模な改善です。

## articles/search/cognitive-search-skill-sentiment-v3.md{#item-bb46e0}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Sentiment cognitive skill (v3)
 titleSuffix: Azure AI Search
 description: Provides sentiment labels for text in an AI enrichment pipeline in Azure AI Search.
-
 author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-sentiment-v3.md` ドキュメントにおいて、著者に関する情報が削除されたことを示しています。具体的には、行 `author: gmndrg` および `ms.author: gimondra` が取り除かれました。この修正により、ドキュメントの内容がよりすっきりとし、余分な情報が排除され、読者は重要な情報に集中しやすくなります。サービス情報である `ms.service: azure-ai-search` はそのまま残されており、機能に影響を与えることなく、ドキュメントの可読性を向上させるための小規模な更新です。

## articles/search/cognitive-search-skill-text-translation.md{#item-b42884}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Text Translation cognitive skill
 titleSuffix: Azure AI Search
 description: Evaluates text and, for each record, returns text translated to the specified target language in an  AI enrichment pipeline in Azure AI Search.
-
 manager: nitinme
 author: gmndrg
 ms.author: gimondra
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージャー情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-text-translation.md` ドキュメントにおいて、マネージャーに関する情報が削除されていることを示しています。具体的には、行 `manager: nitinme` が削除され、著者情報はそのまま残されています。この修正により、ドキュメントの内容がシンプルになり、読者が本質的な情報に集中しやすくなります。著者情報が変更されていないため、ドキュメントの主要な内容には影響を与えず、全体的な可読性を向上させるためのマイナーな更新です。

## articles/search/cognitive-search-tutorial-debug-sessions.md{#item-7e10e9}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'Tutorial: Debug Skillsets'
 titleSuffix: Azure AI Search
 description: Practice creating and completing a debug session on an Azure AI Search skillset. This tutorial provides a buggy sample skillset that you resolve in a debug session.
-
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者およびマネージャー情報の削除"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-tutorial-debug-sessions.md` ドキュメントにおいて、著者とマネージャーに関する情報が削除されたことを示しています。具体的には、行 `author: HeidiSteen` と `manager: nitinme` が削除されました。この修正により、ドキュメントの内容が簡素化され、余分な情報が省かれることで、読者は重要なコンテンツに集中しやすくなります。サービス情報 `ms.author: heidist` も削除されているため、全体的にシンプルで焦点を絞った調整となっています。

## articles/search/hybrid-search-how-to-query.md{#item-345ce6}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Hybrid query
 titleSuffix: Azure AI Search
 description: Learn how to build queries for hybrid search.
-
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報およびサービス情報の削除"
}
```

### Explanation
この変更は、`articles/search/hybrid-search-how-to-query.md` ドキュメントにおいて、著者およびサービスに関する情報が削除されたことを示しています。具体的には、行 `author: HeidiSteen` と `ms.service: azure-ai-search` が削除されました。この修正により、ドキュメントはよりシンプルになり、情報の焦点がコンテンツにシフトします。著者情報やサービス情報の削除は、文書全体の一貫性に寄与し、読者が重要な情報に集中できるようにするためのマイナーな更新です。

## articles/search/hybrid-search-overview.md{#item-6987b4}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Hybrid search
 titleSuffix: Azure AI Search
 description: Describes concepts and architecture of hybrid query processing and document retrieval. Hybrid queries combine vector search and full text search.
-
 author: robertklee
 ms.author: robertlee
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報およびサービス情報の削除"
}
```

### Explanation
この変更は、`articles/search/hybrid-search-overview.md` ドキュメントにおいて、著者およびサービスに関する情報が削除されたことを示しています。具体的には、行 `author: robertklee` と `ms.service: azure-ai-search` が削除されました。この修正は、ドキュメントをより簡素化し、読者が主要な内容に集中できるようにすることを目的としています。著者情報やサービス情報の削除により、文書の一貫性が保たれ、全体的な焦点が内容に移ることが期待されます。

## articles/search/hybrid-search-ranking.md{#item-dad887}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Hybrid search scoring (RRF)
 titleSuffix: Azure AI Search
 description: Describes the Reciprocal Rank Fusion (RRF) algorithm used to unify search scores from parallel queries in Azure AI Search.
-
 author: yahnoosh
 ms.author: jlembicz
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報およびサービス情報の削除"
}
```

### Explanation
この変更は、`articles/search/hybrid-search-ranking.md` ドキュメントにおいて、著者およびサービスに関する情報が削除されたことを示しています。具体的には、行 `author: yahnoosh` と `ms.service: azure-ai-search` が削除されました。この修正により、ドキュメントはより簡素になり、読者が内容に集中しやすくなります。著者情報やサービス情報が削除されることで、文書の全体的な一貫性が向上し、重要な情報に対する焦点が強化されることが期待されます。

## articles/search/includes/previews/preview-generic.md{#item-51bbcc}

<details>
<summary>Diff</summary>
````diff
@@ -1,8 +1,8 @@
 ---
 title: Include file
 description: Include file
-author: eric-urban
-ms.author: eur
+author: HeidiSteen
+ms.author: heidist
 ms.service: azure-ai-speech
 ms.topic: include
 ms.date: 03/19/2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報の更新"
}
```

### Explanation
この変更は、`articles/search/includes/previews/preview-generic.md` ドキュメントにおける著者情報の更新を示しています。具体的には、著者名が `eric-urban` から `HeidiSteen` に、また `ms.author` の値も `eur` から `heidist` に変更されました。さらに、その他のメタデータ（`ms.service`, `ms.topic`, `ms.date`）は変更されていません。この修正には2つの追加と2つの削除が含まれており、ドキュメントの著者に関する情報が最新のものになり、より正確な表記が可能になります。著者情報の明確化は、ドキュメントの信頼性を向上させ、読者にとっての有用性を高めることが期待されます。

## articles/search/includes/resource-authentication.md{#item-381ff1}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
-author: eric-urban 
-ms.author: eur 
+author: HeidiSteen 
+ms.author: heidist 
 ms.service: azure-ai-search
 ms.topic: include
 ms.date: 2/12/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報の更新"
}
```

### Explanation
この変更は、`articles/search/includes/resource-authentication.md` ドキュメントにおける著者情報の更新を示しています。具体的には、著者名が `eric-urban` から `HeidiSteen` に、そして `ms.author` が `eur` から `heidist` に変更されました。これに加え、他のメタデータ（`ms.service`, `ms.topic`, `ms.date`）は変更されておらず、文書のサービスに関する情報はそのまま維持されています。この修正により、ドキュメントの著者に関する情報が最新のものになり、読者にとっての透明性と信頼性が向上します。また、正確な著者情報は、情報提供者の可視性を高め、ドキュメントの利用者がサポートを必要とする場合に役立つ可能性があります。

## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Add scoring profiles
 titleSuffix: Azure AI Search
 description: Boost search relevance scores for Azure AI Search results by adding scoring profiles to a search index.
-
 manager: nitinme
 author: shmed
 ms.author: ramero
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/index-add-scoring-profiles.md` ドキュメントにおける管理者情報の削除を示しています。具体的には、`manager` フィールドから `nitinme` が削除されました。この修正は、ドキュメントの内容に影響を与えるものではないものの、管理者情報の明確さを保つことに寄与します。変更後の文書は、検索スコアの関連性を向上させるためのスコアリングプロファイルを検索インデックスに追加するというメインのテーマを強調し、管理者情報を省略することで視覚的な簡潔さを提供しています。このようなマイナーな更新は、文書の一貫性と整合性を向上させる役割を果たし、読者にとってより洗練された情報を提供します。

## articles/search/index-add-suggesters.md{#item-28ed57}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Configure a suggester for autocomplete and suggestions
 titleSuffix: Azure AI Search
 description: Enable typeahead query actions in Azure AI Search by creating suggesters and formulating requests that invoke autocomplete or autosuggested query terms.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/index-add-suggesters.md` ドキュメントにおいて、管理者情報の削除を示しています。具体的には、`manager` フィールドから `nitinme` が削除されました。このマイナーな更新により、文書はより簡潔になり、読者が主要な内容に集中しやすくなっています。文書全体のテーマは、Azure AI Searchのオートコンプリートとサジェスト機能を設定する方法に焦点を当てており、管理者情報の削除は、そのテーマに対して不要なノイズを減らす効果があります。この変更は、情報の明確さと一貫性を保つために重要です。

## articles/search/index-similarity-and-scoring.md{#item-75603d}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: BM25 relevance scoring
 titleSuffix: Azure AI Search
 description: Explains the concepts of BM25 relevance and scoring in Azure AI Search, and what a developer can do to customize the scoring result.
-
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報の削除"
}
```

### Explanation
この変更は、`articles/search/index-similarity-and-scoring.md` ドキュメントにおいて、著者情報の削除を示しています。具体的には、`author` フィールドから `HeidiSteen` が削除されました。このマイナーな更新により、そのドキュメントはより簡素化されており、主題に対する集中を高めています。文書の内容は、Azure AI SearchにおけるBM25関連性スコアリングの概念を解説しており、開発者がスコアリング結果をカスタマイズする方法について説明しています。著者情報の削除は、この主題には必要ない情報を省くことに寄与し、視覚的なノイズを減少させる役割を果たします。このような更新は、文書の整合性と一貫性を保つための重要なステップです。

## articles/search/knowledge-store-projection-example-long.md{#item-e18999}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Projection examples
 titleSuffix: Azure AI Search
 description: Explore a detailed example that projects the output of a rich skillset into complex shapes that inform the structure and composition of content in a knowledge store.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "管理者および著者情報の削除"
}
```

### Explanation
この変更は、`articles/search/knowledge-store-projection-example-long.md` ドキュメントにおいて、管理者と著者の情報が削除されたことを示しています。具体的には、`manager` フィールドから `nitinme`、および `author` フィールドから `HeidiSteen` が削除されました。このマイナーな更新は、文書を簡潔にし、主要な内容に焦点を合わせることに貢献しています。ドキュメント自体は、リッチスキルセットの出力をプロジェクションして、ナレッジストアの構造と構成を明らかにする詳細な例を探求する内容となっています。管理者および著者情報の不要な削除は、文書全体の整合性を高め、読者が情報の核心に集中できるようにするための重要な措置です。

## articles/search/knowledge-store-projection-overview.md{#item-81aa4a}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Projection concepts
 titleSuffix: Azure AI Search
 description: Introduces projection concepts and best practices. If you're creating a knowledge store in Azure AI Search, projections determine the type, quantity, and composition of objects in Azure Storage.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "管理者および著者情報の削除"
}
```

### Explanation
この変更は、`articles/search/knowledge-store-projection-overview.md` ドキュメントにおいて、管理者および著者の情報が削除されたことを示しています。具体的には、`manager` フィールドから `nitinme` 及び `author` フィールドから `HeidiSteen` が削除されました。このマイナーな更新は、文書をよりシンプルにし、内容への集中を促進することを目的としています。文書は、Azure AI Search におけるナレッジストアを作成する際のプロジェクションの概念とベストプラクティスを紹介しており、プロジェクションがAzure Storageのオブジェクトの種類、量、構成を決定する重要な要素であることを説明しています。管理者および著者情報を削除することにより、文書の焦点がより明確になり、読者が本質的な情報に集中しやすくなっています。

## articles/search/knowledge-store-projections-examples.md{#item-9bfff5}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Define projections
 titleSuffix: Azure AI Search
 description: Learn how to define table, object, and file projections in a knowledge store by reviewing syntax and examples.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "管理者および著者情報の削除"
}
```

### Explanation
この変更は、`articles/search/knowledge-store-projections-examples.md` ドキュメントにおいて、管理者および著者の情報が削除されたことを示しています。具体的には、`manager` フィールドから `nitinme` 及び `author` フィールドから `HeidiSteen` が削除されました。このマイナーな更新は、文書を簡潔に保ち、内容に対する読者の集中を促進する目的があります。ドキュメントは、知識ストアにおけるテーブル、オブジェクト、ファイルのプロジェクションを定義する方法について、構文や例を通じて学ぶ内容となっています。管理者および著者情報の削除により、文書の核心的な情報が強調され、利用者が重要なコンテンツに集中しやすくなっています。

## articles/search/query-lucene-syntax.md{#item-736436}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Lucene query syntax
 titleSuffix: Azure AI Search
 description: Reference for the full Lucene query syntax, as used in Azure AI Search for wildcard, fuzzy search, RegEx, and other advanced query constructs.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "管理者および著者情報の削除"
}
```

### Explanation
この変更は、`articles/search/query-lucene-syntax.md` ドキュメントにおいて、管理者および著者の情報が削除されたことを示しています。具体的には、`manager` フィールドから `nitinme` 及び `author` フィールドから `bevloh` が削除されました。このマイナーな更新は、文書の簡潔さを向上させることを意図しており、読者が重要な内容に集中しやすくするためのものです。このドキュメントは、Azure AI Search で使用されるワイルドカード、ファジー検索、正規表現（RegEx）などの高度なクエリ構文を含む、完全な Lucene クエリ構文の参照を提供しています。管理者や著者の情報を削除することで、文書の本質的な情報がより際立ち、利用者が必要な情報を容易に見つけることができるようになります。

## articles/search/query-odata-filter-orderby-syntax.md{#item-6ab74f}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: OData language overview
 titleSuffix: Azure AI Search
 description: OData language overview for filters, select, and order-by for Azure AI Search keyword search.
-
 author: bevloh
 ms.author: beloh
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者およびサービス情報の削除"
}
```

### Explanation
この変更は、`articles/search/query-odata-filter-orderby-syntax.md` ドキュメントにおいて、著者およびサービス情報が削除されたことを示しています。具体的には、`author` フィールドから `bevloh` と `ms.author` フィールドから `beloh`、さらに `ms.service` フィールドも削除されました。このマイナーな更新は、文書をより簡潔にし、読者が重要な内容に集中しやすくすることを目的としています。このドキュメントは、Azure AI Search におけるフィルター、選択、並べ替えのための OData 言語の概要を提供しており、文書から著者情報を排除することにより、内容の重要性が際立つようになります。結果として、読者は必要な情報をよりスムーズに取得できるようになります。

## articles/search/query-simple-syntax.md{#item-ab3c96}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Simple query syntax
 titleSuffix: Azure AI Search
 description: Reference for the simple query syntax used for full text search queries in Azure AI Search.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "管理者および著者情報の削除"
}
```

### Explanation
この変更は、`articles/search/query-simple-syntax.md` ドキュメントにおいて、管理者および著者の情報が削除されたことを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `bevloh`、および `ms.author` フィールドから `beloh` が削除されました。このマイナーな更新は、ドキュメントの簡潔さを高め、読者が重要な情報により集中できるようにするためのものです。このドキュメントは、Azure AI Search においてフルテキスト検索クエリに使用されるシンプルなクエリ構文の参照を提供しており、著者や管理者の情報を削除することで、内容がより際立つようになっています。その結果、読者は必要な情報をより簡単に把握できるようになります。

## articles/search/reference-stopwords.md{#item-63e4b3}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,9 @@
 title: Stopwords
 titleSuffix: Azure AI Search
 description: Reference documentation containing the stopwords list of the Microsoft language analyzers.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
-
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
@@ -16,7 +14,7 @@ ms.date: 05/16/2022
 
 # Stopwords reference (Microsoft analyzers)
 
-When text is indexed into Azure AI Search, it's processed by analyzers so it can be efficiently stored in a search index. During this [lexical analysis](tutorial-create-custom-analyzer.md#how-analyzers-work) process, [language analyzers](index-add-language-analyzers.md) will remove stopwords specific to that language. Stopwords are non-essential words such as "the" or "an" that can be removed without compromising the lexical integrity of your content. 
+When text is indexed into Azure AI Search, analyzers process the text so it can be efficiently stored in a search index. During this [lexical analysis](tutorial-create-custom-analyzer.md#how-analyzers-work) process, [language analyzers](index-add-language-analyzers.md) removes stopwords specific to that language. Stopwords are non-essential words such as "the" or "an" that can be removed without compromising the lexical integrity of your content. 
 
 Stopword removal applies to all supported [Lucene and Microsoft analyzers](index-add-language-analyzers.md#supported-language-analyzers) used in Azure AI Search.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除と文章の修正"
}
```

### Explanation
この変更は、`articles/search/reference-stopwords.md` ドキュメントにおいて、著者や管理者の情報が削除された上で、テキストの表現がわずかに修正されたことを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `haileytap`、および `ms.author` フィールドから `haileytapia` が削除され、`ms.service` と `ms.custom` 情報も削除されました。また、文章の一部が「analyzers will remove」から「analyzers removes」に変更され、文法的な一貫性が向上しています。

このマイナーな更新は、ドキュメントを簡潔に保ち、読者に重要な情報が伝わりやすくすることを目的としています。このドキュメントは、Microsoft の言語解析器によるストップワードリストを含む参照資料であり、ストップワードがどのように処理されるかを説明しています。情報の削除によって、読者は必要な情報に焦点を当てやすくなり、全体的な内容の理解が促進されます。

## articles/search/resource-tools.md{#item-0c6ac1}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Productivity Tools
 titleSuffix: Azure AI Search
 description: Use existing code samples or build your own tools for working with a search index in Azure AI Search.
-
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報の削除"
}
```

### Explanation
この変更は、`articles/search/resource-tools.md` ドキュメントにおいて、著者情報が削除されたことを示しています。具体的には、`author` フィールドから `haileytap` および `ms.author` フィールドから `haileytapia`、さらに `ms.service` フィールドも削除されました。このマイナーな更新は、ドキュメントの簡潔さを促進し、読者がコンテンツに集中しやすくすることを目的としています。

このドキュメントは、Azure AI Search における検索インデックスで作業するための既存のコードサンプルを使用する方法や、自分自身のツールを構築する方法を説明しており、著者情報を削除することで、内容の重要性がより際立つようになっています。読者は、必要な情報に迅速にアクセスできるようになるため、全体的な使いやすさが向上すると考えられます。

## articles/search/resource-training.md{#item-07788d}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Training modules
 titleSuffix: Azure AI Search
 description: Get hands-on training on Azure AI Search from Microsoft and other third-party training providers.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/resource-training.md` ドキュメントの著者および管理者情報が削除されたことを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `haileytap`、および `ms.author` フィールドから `haileytapia` が削除されました。このマイナーな更新により、文書の簡潔さが向上し、読者が内容に集中しやすくなることを目指しています。

ドキュメント自体は、Microsoft および他の第三者のトレーニングプロバイダーからの Azure AI Search に関するハンズオントレーニングを取得する方法を説明しています。著者や管理者の詳細を削除することにより、提供されるトレーニングリソースの重要性に焦点を当て、より明確かつ直接的な内容にすることを目的としています。これにより、ユーザーは必要な情報を迅速に見つけやすくなります。

## articles/search/search-add-autocomplete-suggestions.md{#item-0a43e0}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Autocomplete or typeahead
 titleSuffix: Azure AI Search
 description: Enable search-as-you-type query actions in Azure AI Search by creating suggesters and queries that autocomplete a search string with finished terms or phrases. You can also return suggested matches.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-add-autocomplete-suggestions.md` ドキュメントにおいて、著者および管理者情報が削除されたことを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `HeidiSteen`、および `ms.author` フィールドから `heidist` が削除されました。このマイナーな更新は、ドキュメントの簡潔さを促進し、読者が主要な内容に注目することを容易にすることを目指しています。

ドキュメントは、Azure AI Search において「タイプアヘッド」クエリアクションを有効にする方法を説明しており、検索文字列を自動補完するためのサジェスターやクエリの作成について記載されています。著者や管理者の情報を削除することにより、説明されている機能やその利用方法に対する焦点がより明確になり、ユーザーが必要な情報を迅速に取得できるようになります。これにより、全体的なユーザーエクスペリエンスが改善されることが期待されます。

## articles/search/search-agentic-retrieval-how-to-create.md{#item-310fbe}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Create a knowledge agent
 titleSuffix: Azure AI Search
 description: Learn how to create a knowledge agent for agentic retrieval workloads in Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-agentic-retrieval-how-to-create.md` ドキュメントにおいて、著者および管理者情報が削除されたことを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `HeidiSteen`、さらに `ms.author` フィールドから `heidist` が削除されました。このマイナーな更新により、ドキュメントがよりシンプルになり、読者がコンテンツの本質に集中しやすくなることを目指しています。

このドキュメントは、Azure AI Search におけるエージェント型リトリーバルワークロードのためのナレッジエージェントの作成方法について説明しています。著者や管理者に関する情報を取り除くことで、提示されている内容の重要性が一層際立ち、ユーザーは必要な情報を迅速に探し出しやすくなります。全体として、ユーザーエクスペリエンスの向上が期待される更新です。

## articles/search/search-agentic-retrieval-how-to-index.md{#item-a078ea}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Design an index for agentic retrieval
 titleSuffix: Azure AI Search
 description: Create an index that has fields and configurations that work for agentic retrieval workloads in Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-agentic-retrieval-how-to-index.md` ドキュメントにおいて、著者および管理者情報を削除したことを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `HeidiSteen`、さらに `ms.author` フィールドから `heidist` が除かれています。このマイナー更新により、ドキュメントはより簡潔になり、読者が主要な情報に集中しやすくなります。

このドキュメントは、Azure AI Search においてエージェント型リトリーバルワークロードに適したフィールドと設定を持つインデックスを作成する方法を説明しています。著者や管理者に関する情報を削除することにより、コンテンツの重要性が強調され、ユーザーが必要な情報を迅速に見つける手助けとなることが期待されます。全体的なユーザーエクスペリエンスの向上が目的とされているこの変更は、情報のアクセス性をより高めることを目指しています。

## articles/search/search-agentic-retrieval-how-to-pipeline.md{#item-1ad1c3}

<details>
<summary>Diff</summary>
````diff
@@ -203,7 +203,7 @@ def agentic_retrieval() -> str:
         Be sure to use the same format in your agent's response
     """
     # Take the last 5 messages in the conversation
-    messages = project_client.agents.list_messages(thread.id, limit=5, order=ListSortOrder.DESCENDING)
+    messages = project_client.agents.messages.list(thread.id, limit=5, order=ListSortOrder.DESCENDING)
     # Reverse the order so the most recent message is last
     messages.data.reverse()
     retrieval_result = retrieval_result = agent_client.retrieve(
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メソッド名の更新"
}
```

### Explanation
この変更は、`articles/search/search-agentic-retrieval-how-to-pipeline.md` ドキュメントにおけるメソッド名の更新を示しています。具体的には、`project_client.agents.list_messages` の部分が `project_client.agents.messages.list` に変更されました。この変更は、メソッドの呼び出し方を改善するものであり、適切なAPI呼び出しの形式に合わせてコードを整理することを目的としています。

この変更により、エージェント型リトリーバル機能を実装する際に利用するメソッドの使い方が明確になります。また、元の呼び出しが非推奨または誤っている場合に、それを修正することで将来的な互換性を保つことが期待されます。全体として、コードの可読性と保守性が向上し、開発者が適切な方法を使用してエージェントのメッセージをリストすることが可能になります。

## articles/search/search-agentic-retrieval-how-to-retrieve.md{#item-5f7fc0}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Use a knowledge agent to retrieve data
 titleSuffix: Azure AI Search
 description: Set up a retrieval route for agentic retrieval workloads in Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-agentic-retrieval-how-to-retrieve.md` ドキュメントにおいて、著者および管理者に関する情報を削除することを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `HeidiSteen`、さらには `ms.author` フィールドから `heidist` の項目が除かれています。このマイナー更新は、ドキュメントの簡潔さを向上させることを目的としており、主要な内容に対する焦点をより明確にします。

このドキュメントは、Azure AI Searchにおけるエージェント型リトリーバルワークロードのためのデータ取得ルートの設定方法を説明しています。著者や管理者に関する情報を削除することで、ユーザーが必要な情報を迅速に見つけやすくなり、全体的なユーザーエクスペリエンスが向上することが期待されます。この変更により、コンテンツの重要性が強調され、ユーザーにとっての情報のアクセス性が向上します。

## articles/search/search-api-migration.md{#item-07297b}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Upgrade REST API versions
 titleSuffix: Azure AI Search
 description: Review differences in API versions and learn about the REST API lifecycle and the steps for migrating code to the newer versions.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-api-migration.md` ドキュメントに対して行われた著者および管理者の情報を削除することを示しています。具体的には、`manager` フィールドにあった `nitinme`、`author` フィールドの `bevloh`、および `ms.author` の `beloh` が削除されました。このマイナー更新は、ドキュメントの内容に焦点を当て、冗長な情報を省くことを目的としています。

このドキュメントは、Azure AI SearchのREST APIバージョンのアップグレードに関するもので、APIバージョン間の違いのレビューやREST APIライフサイクル、コードを新しいバージョンに移行するためのステップを学ぶことができます。著者と管理者情報の削除により、ユーザーは内容に直接集中でき、情報へのアクセスが簡潔かつ効率的になることが期待されます。全体として、この変更はドキュメントのクオリティを向上させ、読者にとっての使いやすさを改善します。

## articles/search/search-api-preview.md{#item-511f5d}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Preview feature list
 titleSuffix: Azure AI Search
 description: Preview features are released so that customers can provide feedback on their design and utility. This article is a comprehensive list of all features currently in preview.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-api-preview.md` ドキュメントにおいて、著者および管理者に関する情報を削除することを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `HeidiSteen`、および `ms.author` フィールドから `heidist` の項目が削除されています。このマイナーアップデートの目的は、ユーザーにとって関連性の高い情報に焦点を当て、ドキュメントをより簡潔にすることです。

このドキュメントは、Azure AI Searchのプレビュー機能リストについて説明しており、顧客がデザインや有用性についてフィードバックを提供できるようにリリースされたプレビュー機能の包括的なリストを提供しています。著者や管理者に関する情報を削除することで、ユーザーが最も重要な情報に迅速にアクセスできるようになり、全体的な読解体験が向上することが期待されます。この変更は、ドキュメントの焦点を明確にし、コンテンツの価値を高めることに寄与します。

## articles/search/search-api-versions.md{#item-69ca3e}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: API versions
 titleSuffix: Azure AI Search
 description: Version policy for Azure AI Search REST APIs and the client library in the .NET SDK.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-api-versions.md` ドキュメントにおいて、著者および管理者に関する情報を削除することを示しています。具体的には、`manager` フィールドにあった `nitinme`、`author` フィールドの `HeidiSteen`、および `ms.author` の `heidist` が削除されました。このマイナー更新は、ドキュメントの内容に焦点を当て、冗長な情報を省くことを目的としています。

このドキュメントは、Azure AI SearchにおけるREST APIと.NET SDKのクライアントライブラリのバージョンポリシーについて説明しています。著者や管理者情報の削除により、ユーザーは内容に直接集中でき、情報へのアクセスが簡潔かつ効率的になることが期待されます。この変更は、ドキュメントの焦点を明確にし、読者にとっての使いやすさを改善します。全体として、この変更はドキュメントのクオリティを向上させ、コンテンツの価値を高めることに寄与します。

## articles/search/search-blob-storage-integration.md{#item-bbdaa6}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Search over Azure Blob Storage content
 titleSuffix: Azure AI Search
 description: Learn how to extract text from Azure blobs and making the content full-text searchable in an Azure AI Search index.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-blob-storage-integration.md` ドキュメントにおいて、著者および管理者に関する情報を削除することを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `HeidiSteen`、および `ms.author` フィールドから `heidist` が削除されました。このマイナーアップデートは、ドキュメントを簡潔に保ち、内容に直接集中できるようにすることを目的としています。

このドキュメントは、Azure Blob Storageのコンテンツからテキストを抽出し、その内容をAzure AI Searchインデックスでフルテキスト検索可能にする方法について説明しています。著者および管理者に関する情報が削除されたことにより、読み手は重要な情報により早くアクセスできるようになり、全体的なユーザー体験が向上することが期待されます。この変更は、ドキュメントの明瞭性を高め、内容の価値をさらに引き出すことに寄与します。

## articles/search/search-capacity-planning.md{#item-0dd6c9}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Estimate capacity for query and index workloads
 titleSuffix: Azure AI Search
 description: Learn how capacity is structured and used in Azure AI Search, and how to estimate the resources needed for indexing and query workloads.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-capacity-planning.md` ドキュメントにおいて、著者および管理者に関する情報を削除することを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `haileytap`、および `ms.author` フィールドから `haileytapia` が削除されました。このマイナーアップデートは、ドキュメントを簡素化し、利用者がコンテンツに直接集中できるようにすることを目的としています。

このドキュメントは、Azure AI Searchにおけるクエリとインデックスのワークロードに必要なキャパシティの構造および使用方法、ならびにインデックス作成とクエリワークロードに必要なリソースの推定方法について解説しています。著者および管理者情報の削除により、読者は核心的な情報に素早くアクセスできるようになり、ドキュメントの全体的な使いやすさが向上することが期待されます。この変更は内容の明確さを高め、ドキュメントの情報価値を向上させることに寄与します。

## articles/search/search-create-service-portal.md{#item-f90159}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'Create a Search Service in the Azure Portal'
 titleSuffix: Azure AI Search
 description: Learn how to set up an Azure AI Search resource in the Azure portal. Choose resource groups, regions, and a pricing tier.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-create-service-portal.md` ドキュメントにおいて、著者および管理者に関する情報を削除することを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `haileytap`、および `ms.author` フィールドから `haileytapia` が削除されました。このマイナーアップデートは、ドキュメントをより簡潔にし、ユーザーがコンテンツに直接集中できるようにすることを目的としています。

このドキュメントは、AzureポータルでAzure AI Searchリソースを設定する方法について説明しています。リソースグループ、リージョン、および料金プランを選択する手順が含まれています。著者および管理者情報が削除されたことにより、読者はより重要な情報に迅速にアクセスできるようになり、ドキュメントの全体的なユーザー体験が向上することが期待されます。これにより、内容の明快さを高め、ドキュメントの情報価値を向上させることに寄与します。

## articles/search/search-data-sources-gallery.md{#item-18727f}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,6 @@ titleSuffix: Azure AI Search
 description: Lists data source connectors for importing into an Azure AI Search index.
 author: HeidiSteen
 ms.author: heidist
-
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-data-sources-gallery.md` ドキュメントにおいて、特定のメタデータ情報を削除することを示しています。具体的には、`ms.service` フィールドから `azure-ai-search`、`ms.update-cycle` フィールドから `180-days`、および `ms.custom` フィールドが削除されました。このマイナーアップデートは、ドキュメントの内容を簡素化し、関連情報を更新または再構成する目的があります。

このドキュメントは、Azure AI Searchインデックスにインポートするためのデータソースコネクタの一覧を提供しています。メタデータの削除により、利用者は本来の内容やコネクタに簡単にアクセスできるようになり、情報の重要性を明確に理解できることが期待されます。全体として、この変更はドキュメントの使いやすさを向上させ、読者が必要な情報により迅速に到達できるようにします。

## articles/search/search-dotnet-mgmt-sdk-migration.md{#item-bcb84f}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Upgrade management SDKs
 titleSuffix: Azure AI Search
 description: Learn about the management libraries and packages used for control plane operations in Azure AI Search.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-dotnet-mgmt-sdk-migration.md` ドキュメントにおいて、著者および管理者に関する情報を削除することを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `bevloh`、および `ms.author` フィールドから `beloh` が削除されました。このマイナーアップデートは、ドキュメントの内容をよりシンプルにし、ユーザーが主要な情報にフォーカスできるようにすることを目指しています。

このドキュメントは、Azure AI Searchにおける制御プレーン操作のために使用される管理ライブラリとパッケージについて説明しています。著者および管理者の情報の削除により、読者はコンテンツに集中しやすくなり、重要な情報に迅速にアクセスできるようになります。全体として、この変更はドキュメントの可読性を向上させ、ユーザー体験を向上させることに寄与します。

## articles/search/search-dotnet-sdk-migration-version-11.md{#item-5ca9e8}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Upgrade to .NET SDK version 11
 titleSuffix: Azure AI Search
 description: Migrate your search application code from older SDK versions to the Azure AI Search .NET SDK version 11.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-dotnet-sdk-migration-version-11.md` ドキュメントにおいて、管理者および著者に関する情報を削除したことを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `HeidiSteen`、および `ms.author` フィールドから `heidist` が削除されました。このマイナーアップデートは、ドキュメントの内容をより簡素化し、ユーザーが重要な情報に集中しやすくすることを目的としています。

このドキュメントは、古いSDKバージョンからAzure AI Search .NET SDKバージョン11への検索アプリケーションコードの移行について説明しています。著者および管理者の情報が削除されたことで、読者はコンテンツの主要な部分に集中しやすくなり、必要な情報に迅速にアクセスできるようになります。全体として、この変更はドキュメントの可読性を向上させ、ユーザー体験を改善することに寄与します。

## articles/search/search-faceted-navigation-examples.md{#item-2b1158}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,6 @@
 title: Faceted navigation examples
 titleSuffix: Azure AI Search
 description: Examples that demonstrate query syntax for facet hierarchies, distinct counts, facet aggregations, and facet filters.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-faceted-navigation-examples.md` ドキュメントにおいて、著者および管理者に関する情報を削除したことを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `HeidiSteen`、および `ms.author` フィールドから `heidist` が削除されました。このマイナーアップデートは、ドキュメントをよりシンプルにし、ユーザーが主要な情報に集中しやすくすることを目的としています。

このドキュメントは、ファセット階層、異なるカウント、ファセット集計、およびファセットフィルターに関するクエリ構文を示す例を紹介しています。著者および管理者の情報が削除されたことにより、読者はドキュメントの内容に気を取られず、必要な情報に迅速にアクセスできるようになります。全体として、この変更はドキュメントの可読性を向上させ、ユーザー体験を改善することに寄与します。

## articles/search/search-faceted-navigation.md{#item-f29d1e}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Add facets to a query
 titleSuffix: Azure AI Search
 description: Add faceted navigation for self-directed navigation in applications that integrate with Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-faceted-navigation.md` ドキュメントにおいて、著者および管理者に関する情報を削除したことを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `HeidiSteen`、および `ms.author` フィールドから `heidist` が削除されました。このマイナーアップデートは、ドキュメントの内容をより簡素化し、読者が重要な情報に集中できるようにしたことを目的としています。

このドキュメントは、Azure AI Searchと統合されたアプリケーションにおける自己指向のナビゲーションのためにファセットナビゲーションを追加する方法について説明しています。著者および管理者情報の削除により、ユーザーはコンテンツの核心に迅速にアクセスできるようになり、全体的な可読性が向上します。この変更は、ユーザー体験を向上させることに寄与しています。

## articles/search/search-features-list.md{#item-d34448}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Feature descriptions
 titleSuffix: Azure AI Search
 description: Explore the feature categories of Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-features-list.md` ドキュメントにおいて、著者および管理者に関する情報が削除されたことを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `HeidiSteen`、および `ms.author` フィールドから `heidist` が除去されました。このマイナーアップデートは、ドキュメントをさらに明確にし、読者が主要な情報により集中できるようにするために行われました。

このドキュメントは、Azure AI Searchの機能カテゴリを探ることを目的としており、ユーザーは全体的な機能の理解を深めることができます。著者および管理者の情報の削除は、内容の簡素化を促進し、読者にとっての理解のしやすさを高めています。この変更により、情報のアクセシビリティと可読性が向上し、ユーザー体験を向上させる効果が期待されます。

## articles/search/search-filters.md{#item-3f2a7a}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Text query filters
 titleSuffix: Azure AI Search
 description: Apply filter criteria to include or exclude content before text query execution in Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-filters.md` ドキュメントにおける著者および管理者情報の削除を示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `HeidiSteen`、および `ms.author` フィールドから `heidist` が削除されました。このマイナーアップデートは、ドキュメントの内容をより簡素化し、ユーザーが重要な情報に集中しやすくするために行われました。

このドキュメントは、Azure AI Searchにおけるテキストクエリの実行前に、コンテンツを含むまたは除外するためのフィルター基準の適用方法について説明しています。著者および管理者情報の削除により、ユーザーはドキュメントの核心部分に迅速にアクセスでき、全体的な可読性が向上します。この変更は、情報の明確さとユーザー体験の向上に寄与しています。

## articles/search/search-how-to-create-indexers.md{#item-de71fb}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,9 @@
 title: Create an indexer
 titleSuffix: Azure AI Search
 description: Configure an indexer to automate data import and indexing from Azure data sources into a search index in Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
-
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 06/17/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除とメタデータの一部修正"
}
```

### Explanation
この変更は、`articles/search/search-how-to-create-indexers.md` ドキュメントにおいて、著者および管理者情報の削除とメタデータの一部修正が行われたことを示しています。具体的には、`manager` フィールドから `nitinme`、`author` フィールドから `HeidiSteen`、および `ms.author` フィールドから `heidist` が削除され、`ms.service`、`ms.topic`、`ms.date` フィールドも削除されました。このマイナーアップデートは、ドキュメントの内容を効率化し、ユーザーが重要な情報に集中しやすくするために実施されました。

このドキュメントは、Azure AI Search におけるデータのインポートとインデクシングを自動化するためのインデクサの設定方法について説明しています。著者および管理者情報の削除、およびメタデータの整理により、ドキュメントの可読性と明確さが向上し、ユーザーが必要な情報を迅速に把握できるようになります。この変更は、ユーザー体験の向上に寄与しています。

## articles/search/search-how-to-dotnet-sdk.md{#item-5333eb}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Use Azure.Search.Documents in .NET
 titleSuffix: Azure AI Search
 description: Learn how to create and manage search objects in a .NET application using C# and the Azure.Search.Documents client library.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-how-to-dotnet-sdk.md` ドキュメントにおける著者および管理者情報の削除を示しています。具体的には、`manager` フィールドの `nitinme`、`author` フィールドの `HeidiSteen`、および `ms.author` フィールドの `heidist` が削除されました。このマイナーアップデートは、ドキュメントの内容を簡素化し、ユーザーが重要な情報に集中しやすくするために行われました。

ドキュメントは、C# および Azure.Search.Documents クライアントライブラリを使用して、.NET アプリケーション内で検索オブジェクトを作成および管理する方法についてのガイドを提供しています。著者および管理者の情報が削除されることで、ユーザーはドキュメントの主題により迅速にアクセスでき、全体的な可読性が向上します。この変更は、情報の整理とユーザーエクスペリエンスの向上に寄与しています。

## articles/search/search-how-to-index-csv-blobs.md{#item-2c3f3e}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,9 @@
 title: Search over CSV blobs using delimitedText parsing
 titleSuffix: Azure AI Search
 description: Extract CSV blobs from Azure Blob Storage or Azure Files, and import as search documents into Azure AI Search using the delimitedText parsing mode.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
-
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 03/11/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除とメタデータの修正"
}
```

### Explanation
この変更は、`articles/search/search-how-to-index-csv-blobs.md` ドキュメントにおける著者および管理者情報の削除と、メタデータの修正を示しています。具体的には、`manager` フィールドの `nitinme`、`author` フィールドの `HeidiSteen`、および `ms.author` フィールドの `heidist` が削除され、また `ms.service` フィールドも削除されました。このマイナーアップデートは、ドキュメントを簡素化し、ユーザーが重要な情報に焦点を当てやすくするために行われました。

このドキュメントは、Azure Blob Storage や Azure Files から CSV バイナリを抽出し、区切りテキスト解析モードを使用して Azure AI Search に検索ドキュメントとしてインポートする方法を説明しています。著者および管理者の情報が削除されることで、ユーザーはドキュメントの内容に対するアクセスが迅速かつ効率的に行えるようになります。この変更は、全体的な可読性の向上と、ユーザー体験の向上に寄与しています。

## articles/search/search-how-to-index-markdown-blobs.md{#item-c94a20}

<details>
<summary>Diff</summary>
````diff
@@ -2,10 +2,8 @@
 title: Search over Markdown blobs
 titleSuffix: Azure AI Search
 description: Extract searchable text from Markdown blobs using the blob indexer in Azure AI Search. Indexers provide indexing automation for supported data sources like Azure Blob Storage.
-
 author: mdonovan
 ms.author: mdonovan
-
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報およびメタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-how-to-index-markdown-blobs.md` ドキュメントにおいて、著者情報および関連メタデータの削除を示しています。具体的には、`author` フィールドの `mdonovan`、`ms.author` フィールドの `mdonovan`、および `ms.service` フィールドが削除されました。また、`ms.custom` フィールドも存在していましたが、内容は削除されました。このマイナーアップデートは、ドキュメントの簡素化と焦点の明確化を目指しています。

このドキュメントでは、Azure AI Search の blob インデクサーを使用して、Markdown バイナリから検索可能なテキストを抽出する方法について説明しています。著者情報やメタデータが削除されることで、ユーザーはドキュメントの主要な内容に集中しやすくなり、全体的な可読性が向上します。この変更は、情報の明瞭性を高め、ユーザー体験を向上させることに寄与しています。

## articles/search/search-how-to-index-sql-database.md{#item-86d873}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Azure SQL indexer
 titleSuffix: Azure AI Search
 description: Set up a search indexer to index tables in Azure SQL Database for vector and full text search in Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-how-to-index-sql-database.md` ドキュメントにおいて、著者および管理者情報の削除を示しています。具体的には、`manager` フィールドの `nitinme`、`author` フィールドの `HeidiSteen`、および `ms.author` フィールドの `heidist` が削除されました。このマイナーアップデートは、ドキュメントをよりシンプルにし、ユーザーが重要な情報にアクセスしやすくすることを目的としています。

このドキュメントは、Azure SQL Database のテーブルをインデックスするための検索インデクサーの設定方法を説明しており、ベクトル検索および全文検索を Azure AI Search で実行可能にします。著者および管理者に関する情報を削除することで、ユーザーはドキュメントの主題に迅速に集中できるようになり、全体的な可読性が向上します。この変更は、情報の明瞭性を高め、ユーザーの利便性に寄与しています。

## articles/search/search-how-to-index-sql-managed-instance.md{#item-009ccc}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Indexer connection to SQL Managed Instances
 titleSuffix: Azure AI Search
 description: Enable public endpoint to allow connections to SQL Managed Instances from an indexer on Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-how-to-index-sql-managed-instance.md` ドキュメントにおける著者および管理者情報の削除を示しています。具体的には、`manager` フィールドの `nitinme`、`author` フィールドの `HeidiSteen`、および `ms.author` フィールドの `heidist` が取り除かれました。このマイナーアップデートは、ドキュメントのシンプルさを向上させるために実施されました。

このドキュメントは、Azure AI Search 上のインデクサーが SQL Managed Instances に接続できるようにするための公開エンドポイントの有効化について説明しています。著者および管理者に関する情報が削除されることで、ユーザーはドキュメントの主要な目的にすぐに焦点を合わせられるようになり、全体の可読性が向上します。この変更は、情報の明瞭性を高め、ユーザーの利便性を向上させることに寄与しています。

## articles/search/search-how-to-index-sql-server.md{#item-d7fb35}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,6 @@ description: Enable encrypted connections and configure the firewall to allow co
 author: gmndrg
 ms.author: gimondra
 manager: nitinme
-
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-how-to-index-sql-server.md` ドキュメントにおいて、特定のメタデータ情報の削除を示しています。具体的には、`ms.service` フィールドと `ms.custom` フィールドの情報が削除されました。このマイナーアップデートにより、ドキュメントがよりクリーンで、特定のメタデータに依存しない形になります。

このドキュメントは、SQL Server への接続を暗号化し、Azure AI Search でのインデクサーによる接続を許可するファイアウォールの設定を説明しています。メタデータの削除によって、ドキュメントの内容がより直接的になり、ユーザーが重要な手順に集中できるようになります。この変更は、情報の焦点を絞り、全体的な可読性を向上させることに寄与しています。

## articles/search/search-how-to-large-index.md{#item-d34e42}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Index large data sets for full text search
 titleSuffix: Azure AI Search
 description: Learn about strategies for large data indexing or computationally intensive indexing through batch mode, resourcing, and scheduled, parallel, and distributed indexing.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-how-to-large-index.md` ドキュメントにおいて、著者および管理者の情報が削除されたことを示しています。具体的には、`manager` フィールドの `nitinme`、`author` フィールドの `HeidiSteen`、および `ms.author` フィールドの `heidist` が取り除かれました。このマイナーな更新により、ドキュメントがよりクリーンに保たれ、読者がコンテンツに集中しやすくなります。

このドキュメントは、大規模なデータセットのインデックス作成に関する戦略や、計算集約型のインデクシングを通じたバッチモード、リソースの確保、スケジュールされた並列インデックス作成に関する情報を提供しています。著者および管理者情報の削除は、ユーザーがドキュメントの内容に迅速にアクセスできるようにし、全体的な可読性を向上させる効果があります。

## articles/search/search-how-to-load-search-index.md{#item-a72573}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,9 @@
 title: Load an index
 titleSuffix: Azure AI Search
 description: Import and refresh data in a search index using the Azure portal, REST APIs, or an Azure SDK.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
-
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: how-to
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-how-to-load-search-index.md` ドキュメントにおいて、メタデータの一部が削除されたことを示しています。具体的には、`manager` フィールドの `nitinme`、`author` フィールドの `HeidiSteen`、`ms.author` フィールドの `heidist`、および `ms.service`、`ms.update-cycle`、`ms.topic` フィールドが取り除かれました。このマイナーアップデートにより、ドキュメントがよりシンプルになり、読者が主要な内容に集中しやすくなります。

このドキュメントは、Azure ポータルや REST API、Azure SDK を使用して、検索インデックスにデータをインポートおよび更新する方法について説明しています。メタデータの削除によって、具体的な操作に焦点を当てることができ、全体的な可読性と理解のしやすさが向上しています。

## articles/search/search-howto-complex-data-types.md{#item-75a002}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Model complex data types
 titleSuffix: Azure AI Search
 description: Nested or hierarchical data structures can be modeled in an Azure AI Search index using ComplexType and Collections data types.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-complex-data-types.md` ドキュメントにおける著者および管理者の情報が削除されたことを示しています。具体的には、`manager` フィールドの `nitinme`、`author` フィールドの `bevloh`、および `ms.author` フィールドの `beloh` が取り除かれました。このマイナーな更新により、ドキュメントがよりシンプルで、読者がコンテンツの主要な部分に集中しやすくなります。

このドキュメントは、ネストされたデータ構造や階層的データ構造を Azure AI Search インデックスでモデル化する方法について説明しています。具体的には、`ComplexType` や `Collections` データ型の使用に関する情報が提供されています。著者および管理者情報の削除は、ドキュメント全体の可読性を向上させ、利用者が必要な情報に簡単にアクセスできるようにする効果があります。

## articles/search/search-howto-concurrency.md{#item-863358}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Manage concurrent writes
 titleSuffix: Azure AI Search
 description: Use optimistic concurrency to avoid mid-air collisions on updates or deletes to Azure AI Search indexes, indexers, data sources.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者および管理者情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-concurrency.md` ドキュメントにおいて、著者および管理者の情報が削除されたことを示しています。具体的には、`manager` フィールドの `nitinme`、`author` フィールドの `HeidiSteen`、および `ms.author` フィールドの `heidist` が取り除かれました。このマイナーアップデートにより、ドキュメントがよりコンパクトになり、読者が主要な内容に集中しやすくなります。

このドキュメントは、Azure AI Search インデックスやインデクサー、データソースの更新や削除中にミッドエア衝突を避けるための楽観的同時実行制御について説明しています。著者および管理者情報の削除によって、全体の可読性が向上し、利用者が必要な情報に対してよりスムーズにアクセスできるようになります。

## articles/search/search-howto-index-changed-deleted-blobs.md{#item-32a688}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,6 @@ description: Indexers that index from Azure Storage can pick up new and changed
 author: gmndrg
 ms.author: gimondra
 manager: nitinme
-
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 02/24/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータ情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-index-changed-deleted-blobs.md` ドキュメントにおいて、メタデータ情報が削除されたことを示しています。具体的には、`author` フィールドの `gmndrg`、`ms.author` フィールドの `gimondra`、`manager` フィールドの `nitinme`、および `ms.service`、`ms.topic`、`ms.date` の情報が取り除かれました。このマイナーな更新により、ドキュメントがすっきりし、重要な内容に対するフォーカスが向上します。

このドキュメントは、Azure Storage からインデックスを作成するインデクサーが新しいおよび変更されたデータをどのように取り込むかについて説明しています。メタデータ情報の削除は、ドキュメントの簡素化を促進し、利用者が内容をよりスムーズに理解できるようにする効果があります。

## articles/search/search-howto-index-cosmosdb-gremlin.md{#item-698c99}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,9 @@
 title: Azure Cosmos DB Gremlin indexer
 titleSuffix: Azure AI Search
 description: Set up an Azure Cosmos DB indexer to automate indexing of Apache Gremlin content for full text search in Azure AI Search. This article explains how index data using the Azure Cosmos DB for Apache Gremlin protocol.
-
 author: mgottein
 ms.author: magottei
 manager: nitinme
-
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 05/29/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータ情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-index-cosmosdb-gremlin.md` ドキュメントにおいて、メタデータ情報が削除されたことを示しています。具体的には、`author` フィールドの `mgottein`、`ms.author` フィールドの `magottei`、`manager` フィールドの `nitinme`、および `ms.service`、`ms.topic`、`ms.date` の情報が取り除かれました。このマイナーな更新により、ドキュメントの構成が簡素化され、内容に対するフォーカスが強化されました。

このドキュメントは、Azure AI Search におけるフルテキスト検索のために、Apache Gremlin コンテンツのインデクシングを自動化するAzure Cosmos DB インデクサーの設定方法について説明しています。メタデータ情報の削除は、ドキュメントを読みやすくすることで、利用者が必要な情報により迅速にアクセスできるようにしています。

## articles/search/search-howto-index-cosmosdb.md{#item-568fab}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Azure Cosmos DB NoSQL indexer
 titleSuffix: Azure AI Search
 description: Set up a search indexer to index data stored in Azure Cosmos DB for vector and full text search in Azure AI Search. This article explains how index data using the NoSQL API protocol.
-
 manager: nitinme
 author: mgottein
 ms.author: magottei
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータ情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-index-cosmosdb.md` ドキュメントにおいて、メタデータ情報が削除されたことを示しています。具体的には、`manager` フィールドの `nitinme`、`author` フィールドの `mgottein`、および `ms.author` フィールドの `magottei` が取り除かれました。このマイナーな更新により、ドキュメントの構造が簡潔になり、ユーザーが必要な情報をよりスムーズに得られるように促進されています。

このドキュメントは、Azure Cosmos DB に保存されているデータを Azure AI Search でのベクトルおよびフルテキスト検索のためにインデクシングする方法について説明しています。メタデータ情報の削除は、内容に注目させるための調整であり、ユーザビリティの向上を目指しています。

## articles/search/search-howto-index-encrypted-blobs.md{#item-a7097a}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'Tutorial: Index Encrypted Blobs'
 titleSuffix: Azure AI Search
 description: Learn how to index and extract text from encrypted documents in Azure Blob Storage with Azure AI Search.
-
 manager: nitinme
 author: gmndrg
 ms.author: gimondra
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータ情報の削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-index-encrypted-blobs.md` ドキュメントにおいて、メタデータ情報が削除されたことを示しています。具体的には、`manager` フィールドの `nitinme`、`author` フィールドの `gmndrg`、および `ms.author` フィールドの `gimondra` が取り除かれました。このマイナーな更新により、ドキュメントの構成がシンプルになり、読者が重要な情報に集中しやすくなっています。

このドキュメントは、Azure Blob Storage における暗号化された文書からテキストをインデクシングおよび抽出する方法について説明しています。メタデータ情報の削除は、内容に対するフォーカスを高め、ユーザーにとっての利便性を向上させるための一環です。

## articles/search/search-howto-index-json-blobs.md{#item-b8230c}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,9 @@
 title: Search over JSON blobs
 titleSuffix: Azure AI Search
 description: Extract searchable text from JSON blobs using the blob indexer in Azure AI Search. Indexers provide indexing automation for supported data sources like Azure Blob Storage.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
-
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除と整理"
}
```

### Explanation
この変更は、`articles/search/search-howto-index-json-blobs.md` ドキュメントにおいて、メタデータが整理され、いくつかのフィールドが削除されたことを示しています。具体的には、`manager` フィールドの `nitinme`、`author` フィールドの `HeidiSteen`、および `ms.author` フィールドの `heidist` などが取り除かれました。また、`ms.service` フィールドの情報が削除される一方、`ms.custom` フィールドも削除されています。この結果、全体的にドキュメントの構造が簡素化されています。

このドキュメントは、Azure AI Search の blob インデクサーを利用して、JSON ブロブから検索可能なテキストを抽出する方法について説明しています。メタデータの削除と整理により、ユーザーがコンテンツにより集中しやすくなることを目的としています。変更によって、情報がクリアになり、ドキュメント全体の読みやすさが向上しています。

## articles/search/search-howto-index-mysql.md{#item-5d31c4}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,6 @@ description: Learn how to set up a search indexer to index data stored in Azure
 author: gmndrg
 ms.author: gimondra
 manager: nitinme
-
 ms.devlang: rest-api
 ms.service: azure-ai-search
 ms.topic: how-to
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-index-mysql.md` ドキュメントにおいて、いくつかのメタデータフィールドが削除されたことを示しています。具体的には、`ms.devlang` フィールドの情報と `ms.service` フィールド、`ms.topic` フィールドが取り除かれました。この変更により、ドキュメントが簡素化され、必要な情報に対する注目が高まることが期待されます。

このドキュメントは、Azure に保存されたデータをインデックス化するための検索インデクサーの設定方法について説明しています。メタデータの削除は、ドキュメントの可読性を向上させ、ユーザーが内容を理解しやすくするための措置です。全体として、情報が整理され、ユーザーにとっての利便性が向上しています。

## articles/search/search-howto-index-one-to-many-blobs.md{#item-04ada2}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,9 @@
 title: Index blobs containing multiple documents
 titleSuffix: Azure AI Search
 description: Crawl Azure blobs for text content using the Azure blob indexer, where each blob might yield one or more search index documents.
-
 manager: nitinme
 author: arv100kri
 ms.author: arjagann
-
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの簡素化"
}
```

### Explanation
この変更は、`articles/search/search-howto-index-one-to-many-blobs.md` ドキュメントにおいて、メタデータの一部が削除され、全体の構造が簡素化されたことを示しています。具体的には、`manager` フィールドの `nitinme`、`author` フィールドの `arv100kri`、および `ms.author` フィールドの `arjagann` が取り除かれました。また、`ms.service` フィールドも削除され、`ms.custom` の情報も整理されています。

このドキュメントは、Azure Blob Indexer を使用して Azure に保存された複数のドキュメントを含むブロブからテキストコンテンツをクロールする方法について説明しています。メタデータの削除と整理により、内容の明確さが向上し、ユーザーが情報に集中しやすくなります。全体として、情報の整理は、ドキュメントの可読性を向上させる目的があります。

## articles/search/search-howto-index-plaintext-blobs.md{#item-63efcb}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Search over plain text blobs
 titleSuffix: Azure AI Search
 description: Configure a search indexer to extract plain text from Azure blobs for full text search in Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-index-plaintext-blobs.md` ドキュメントにおいて、メタデータの一部が削除されたことを示しています。具体的には、`manager` フィールドの `nitinme`、`author` フィールドの `HeidiSteen`、および `ms.author` フィールドの `heidist` が取り除かれました。この変更により、ドキュメントの構造が簡素化され、特に不要なメタデータが削除されることで、ユーザーが重要な内容に集中しやすくなります。

このドキュメントは、Azure Blob からプレーンテキストを抽出し、Azure AI Search での全文検索用に検索インデクサーを構成する方法について説明しています。メタデータの整理は、情報の明確性を高め、全体の可読性を向上させるための重要な一歩といえます。

## articles/search/search-howto-index-sharepoint-online.md{#item-49ff6e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,6 @@ titleSuffix: Azure AI Search
 description: Set up a SharePoint Online indexer to automate indexing of document library content in Azure AI Search.
 author: gmndrg
 ms.author: gimondra
-
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 06/17/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの簡素化"
}
```

### Explanation
この変更は、`articles/search/search-howto-index-sharepoint-online.md` ドキュメントにおいて、メタデータの一部が削除されたことを示しています。具体的には、`ms.service` フィールドが削除され、その他のメタデータはそのまま残っています。この変更により、ドキュメントの内容がよりシンプルになり、特にユーザーが重要な情報に集中できるよう配慮されています。

このドキュメントは、Azure AI Search において SharePoint Online のインデクサーを設定し、ドキュメントライブラリのコンテンツを自動的にインデックスする方法について説明しています。メタデータの削除は、情報の可読性を向上させ、全体としてのユーザー体験を改善することを目的としています。

## articles/search/search-howto-indexing-azure-blob-storage.md{#item-dc4668}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,6 @@ description: Set up an Azure blob indexer to automate indexing of blob content f
 author: gmndrg
 ms.author: gimondra
 manager: vinodva
-
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 05/08/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-indexing-azure-blob-storage.md` ドキュメントにおいて、メタデータの一部が削除されたことを示しています。具体的には、`ms.service` フィールドが削除され、他のメタデータはそのまま残っています。これにより、ドキュメントの構造が若干簡素化され、ユーザーが重要な情報にアクセスしやすくなることが期待されます。

このドキュメントは、Azure Blob コンテンツのインデクシングを自動化するための Azure インデクサーの設定について説明しています。メタデータの整理は、情報の明確さを高め、読者にとっての利便性を向上させるための重要な施策です。

## articles/search/search-howto-indexing-azure-tables.md{#item-7655b0}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,9 @@
 title: Azure table indexer
 titleSuffix: Azure AI Search
 description: Set up a search indexer to index data stored in Azure Table Storage for vector and full text search in Azure AI Search.
-
 manager: nitinme
 author: mgottein
 ms.author: magottei
-
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 05/08/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの簡素化"
}
```

### Explanation
この変更は、`articles/search/search-howto-indexing-azure-tables.md` ドキュメントにおいて、メタデータの一部が削除されたことを示しています。具体的には、`manager` フィールドと `ms.service` フィールドが削除され、残るメタデータはそのまま維持されています。この削除により、ドキュメントがより簡潔になり、ユーザーが重要な情報に集中できるようになっています。

このドキュメントは、Azure Table Storage に保存されているデータをインデックスするための検索インデクサーの設定について説明しており、ベクトル検索および全文検索の機能を活用するための手順を提供しています。メタデータの整理は、ドキュメントの可読性を向上させ、ユーザーにとっての利便性を高めるために重要な役割を果たしています。

## articles/search/search-howto-managed-identities-azure-functions.md{#item-2f13c4}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,6 @@ titleSuffix: Azure AI Search
 description: Learn how to set up an indexer connection to an Azure Function using built-in authentication also known as "Easy Auth".
 author: arv100kri
 ms.author: arjagann
-
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 01/20/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-managed-identities-azure-functions.md` ドキュメントにおいて、メタデータの一部が削除されたことを示しています。具体的には、`ms.service` フィールドが削除され、他のメタデータはそのまま残っています。この削除により、ドキュメントがよりシンプルになり、利用者が主要な情報に焦点を合わせやすくなっています。

このドキュメントは、Azure Functions へのインデクサー接続を設定するための手順を説明しており、組み込み認証（「Easy Auth」として知られる）を利用する方法を学ぶことができます。メタデータの簡素化は、文書の可読性を向上させ、ユーザーにとっての利便性を高めるための重要な改善になります。

## articles/search/search-howto-managed-identities-cosmos-db.md{#item-a74464}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,6 @@ titleSuffix: Azure AI Search
 description: Learn how to set up an indexer connection to an Azure Cosmos DB account using a managed identity.
 author: arv100kri
 ms.author: arjagann
-
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 01/06/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-managed-identities-cosmos-db.md` ドキュメントにおいて、メタデータの一部が削除されたことを示しています。具体的には、`ms.service` フィールドが削除され、他のメタデータ要素は変更されていません。この修正により、ドキュメントがよりシンプルになり、ユーザーが必要な情報をより早く見つけやすくなることが期待されます。

このドキュメントは、管理されたアイデンティティを使用して Azure Cosmos DB アカウントへのインデクサー接続を設定する方法について説明しています。メタデータの削除は、ドキュメントの可読性を改善し、ユーザーエクスペリエンスの向上に寄与します。

## articles/search/search-howto-managed-identities-data-sources.md{#item-edf98d}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Configure a managed identity
 titleSuffix: Azure AI Search
 description: Create a managed identity for your search service and use Microsoft Entra authentication and role-based-access controls for connections to other cloud services.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-managed-identities-data-sources.md` ドキュメントにおいて、メタデータの一部が削除されたことを示しています。具体的には、`manager` フィールドが削除され、その他のメタデータはそのまま残っています。この変更により、ドキュメントがより簡潔になり、読者が必要な情報に集中できるようになります。

このドキュメントでは、検索サービスの管理されたアイデンティティを作成し、Microsoft Entra 認証およびロールベースのアクセス制御を用いて他のクラウドサービスへの接続を行う方法について説明しています。メタデータの簡素化は、全体的な可読性の向上に寄与し、ユーザーエクスペリエンスを改善します。

## articles/search/search-howto-managed-identities-storage.md{#item-8209c4}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,6 @@ description: Learn how to set up an indexer connection to an Azure Storage accou
 author: gmndrg
 ms.author: gimondra
 manager: vinodva
-
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 02/18/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-managed-identities-storage.md` ドキュメントにおいて、メタデータの一部が削除されたことを示しています。具体的には、`ms.service` フィールドが削除され、残りのメタデータはそのまま残されています。この修正によって、ドキュメントがよりシンプルになり、情報が整理された形で提示されることになります。

このドキュメントは、Azure ストレージアカウントへのインデクサー接続を設定する方法についての学習を目的としています。メタデータの削除は、ドキュメントの可読性を向上させ、ユーザーにとっての理解を促進する効果が期待されます。

## articles/search/search-howto-monitor-indexers.md{#item-0e3133}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Monitor indexer status and results
 titleSuffix: Azure AI Search
 description: Monitor the status, progress, and results of Azure AI Search indexers in the Azure portal, using the REST API, or the Azure SDKs.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-monitor-indexers.md` ドキュメントにおいて、1つのメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールドが削除され、他のメタデータに関しては変更がありません。この修正により、ドキュメントはよりシンプルに保たれ、情報が一貫して提供されることになります。

このドキュメントは、Azure AI Search のインデクサーのステータス、進捗、および結果を Azure ポータル、REST API、または Azure SDK を使用して監視する方法について説明しています。メタデータの削除は、文書の明確性を高め、ユーザーが必要な情報に迅速にアクセスできるようにする効果があります。

## articles/search/search-howto-move-across-regions.md{#item-bcecf6}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Move a search service across regions
 titleSuffix: Azure AI Search
 description: Learn how to move your Azure AI Search resources from one region to another in the Azure cloud.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-move-across-regions.md` ドキュメントにおいて、1つのメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールドが削除され、他のメタデータはそのままとなっています。この修正により、ドキュメントがより整理され、情報が簡潔に提示されるようになります。

このドキュメントは、Azureクラウド内でAzure AI Searchのリソースをあるリージョンから別のリージョンに移動する方法について説明しています。メタデータの削除により、ドキュメントの明瞭さが向上し、ユーザーが必要な情報を迅速に見つけやすくなる効果が期待されます。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,9 @@
 title: Update or rebuild an index
 titleSuffix: Azure AI Search
 description: Update or rebuild an index to update the schema or clean out obsolete documents. You can fully rebuild or do partial indexing.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
-
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-howto-reindex.md` ドキュメントにおいて、2つのメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールドと `ms.service` フィールドが削除され、その他のメタデータはそのまま残されています。この修正により、ドキュメントはよりクリーンでシンプルになります。

このドキュメントは、インデックスの更新または再構築を行い、スキーマを更新したり、古いドキュメントを取り除く方法について説明しています。また、インデックスの完全な再構築や部分的なインデキシングも可能であることが述べられています。メタデータの整理は、情報の明瞭さを高め、ユーザーが必要な内容をより簡単に見つけられるようにする効果があります。

## articles/search/search-index-azure-sql-managed-instance-with-managed-identity.md{#item-a4ec86}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,6 @@ titleSuffix: Azure AI Search
 description: Learn how to set up an Azure AI Search indexer connection to an Azure SQL Managed Instance using a managed identity
 author: gmndrg
 ms.author: gimondra
-
 ms.service: azure-ai-search
 ms.topic: conceptual
 ms.date: 06/04/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-index-azure-sql-managed-instance-with-managed-identity.md` ドキュメントにおいて、1つのメタデータフィールドが削除されたことを示しています。具体的には、`ms.service` フィールドが削除され、他のメタデータはそのままとなっています。この修正により、ドキュメントがより簡潔になり、冗長な情報が削除されます。

このドキュメントは、Azure SQL Managed Instance に対して、マネージドアイデンティティを使用して Azure AI Search インデクサーの接続を設定する方法について説明しています。メタデータの削除は、ユーザーにとっての情報の明瞭性を高め、必要な内容を見つけやすくする効果があります。

## articles/search/search-indexer-field-mappings.md{#item-0e4628}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,9 @@
 title: Map fields in indexers
 titleSuffix: Azure AI Search
 description: Configure field mappings in an indexer to account for differences in field names and data representations.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
-
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-indexer-field-mappings.md` ドキュメントにおいて、2つのメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールドと `ms.service` フィールドが削除され、他のメタデータはそのまま残されています。この修正により、ドキュメントがよりシンプルで焦点が明確になります。

このドキュメントは、インデクサーでのフィールドマッピングの設定方法について説明しており、フィールド名やデータ表現の違いに対応するための情報を提供しています。メタデータの整理は、読む人の理解を助け、必要な情報に迅速にアクセスできるようにすることに寄与します。

## articles/search/search-indexer-how-to-access-private-sql.md{#item-1bd4cc}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Connect to SQL Managed Instance
 titleSuffix: Azure AI Search
 description: Configure an indexer connection to access content in an Azure SQL Managed instance that's protected through a private endpoint.
-
 author: mattgotteiner
 ms.author: magottei
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-indexer-how-to-access-private-sql.md` ドキュメントにおいて、1つのメタデータフィールドが削除されたことを示しています。具体的には、`author` フィールド、`ms.author` フィールド、及び `ms.service` フィールドが削除され、残りの情報がさらに焦点を絞ったものになっています。この修正によって、ドキュメントがよりスリムで明確になります。

このドキュメントは、プライベートエンドポイントによって保護された Azure SQL Managed Instance にアクセスするためのインデクサー接続の設定方法に関する情報を提供しています。メタデータの整理は、読み手の理解を促進し、必要な情報を効率的に集められるようにすることに役立ちます。

## articles/search/search-indexer-howto-access-ip-restricted.md{#item-aec22f}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Connect through firewalls
 titleSuffix: Azure AI Search
 description: Configure IP firewall rules to allow data access by an Azure AI Search indexer.
-
 manager: nitinme
 author: arv100kri
 ms.author: arjagann
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-indexer-howto-access-ip-restricted.md` ドキュメントにおいて、1つのメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、及び `ms.author` フィールドが削除され、残る内容がより明確に整理されています。この修正は、ドキュメントの簡潔さを向上させます。

このドキュメントは、Azure AI Search のインデクサーによってデータへアクセスするために、IP ファイアウォールルールを設定する方法について説明しています。メタデータの削除は、読み手が文書の内容に集中しやすくするための重要なステップです。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Connect through a shared private link
 titleSuffix: Azure AI Search
 description: Configure indexer connections to access content from other Azure resources that are protected through a shared private link.
-
 manager: nitinme
 author: mrcarter8
 ms.author: mcarter
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-indexer-howto-access-private.md` ドキュメントにおいて、1つのメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、及び `ms.author` フィールドが削除され、ドキュメントの内容がよりシンプルで明確になっています。この修正により、情報が整理され、読みやすさが向上します。

このドキュメントは、共有プライベートリンクを介して保護された他の Azure リソースからコンテンツにアクセスするためのインデクサー接続の設定方法に関する情報を提供しています。メタデータの削除は、内容に焦点を当てるための重要な要素となります。

## articles/search/search-indexer-howto-access-trusted-service-exception.md{#item-e19826}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Connect as trusted service
 titleSuffix: Azure AI Search
 description: Enable secure data access to Azure Storage from an indexer in Azure AI Search 
-
 manager: nitinme
 author: arv100kri
 ms.author: arjagann
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-indexer-howto-access-trusted-service-exception.md` ドキュメントにおいて、1つのメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除され、ドキュメントの情報がより整然とした構造になっています。この修正は、ドキュメントのクリアなプレゼンテーションを促進します。

このドキュメントでは、Azure AI Search のインデクサーから Azure Storage への安全なデータアクセスを有効にする方法が説明されています。メタデータの削除は、読み手が重要な情報に集中できるよう改善された重要なポイントです。

## articles/search/search-indexer-overview.md{#item-292796}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Indexer overview
 titleSuffix: Azure AI Search
 description: Crawl Azure SQL Database, SQL Managed Instance, Azure Cosmos DB, or Azure storage to extract searchable data and populate an Azure AI Search index.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-indexer-overview.md` ドキュメントにおいて、1つのメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、及び `ms.author` フィールドが削除され、内容がさらに整理され、読みやすくなっています。この修正は、全体的な情報の提示がより明確になることを目的としています。

このドキュメントは、Azure SQL Database、SQL Managed Instance、Azure Cosmos DB、または Azure Storage から検索可能なデータを抽出し、Azure AI Search インデックスにポピュレートするプロセスについての概観を提供しています。メタデータの削除により、重要な情報に焦点を当てやすくなる利点があります。

## articles/search/search-indexer-securing-resources.md{#item-c075c4}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Indexer access to protected resources
 titleSuffix: Azure AI Search
 description: Learn import concepts and requirements related to network-level security options for outbound requests made by indexers in Azure AI Search.
-
 manager: nitinme
 author: arv100kri
 ms.author: arjagann
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-indexer-securing-resources.md` ドキュメントにおいて、1つのメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、及び `ms.author` フィールドが削除され、ドキュメントの内容がよりシンプルで整理された形になっています。この修正により、情報の提示方法が向上し、ユーザーにとってより親しみやすくなります。

このドキュメントは、Azure AI Search におけるインデクサーが行うアウトバウンドリクエストのネットワークレベルのセキュリティオプションに関連する重要な概念や要件を学ぶことができる内容になっています。メタデータの削除は、読者が核心の情報に集中しやすくするための措置です。

## articles/search/search-indexer-troubleshooting.md{#item-087365}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Indexer troubleshooting
 titleSuffix: Azure AI Search
 description: Provides indexer problem and resolution guidance for cases when no error messages are returned from the service search.
-
 author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-indexer-troubleshooting.md` ドキュメントにおける1つのメタデータフィールドの削除を反映しています。具体的には、`author` フィールド、`ms.author` フィールド、および `ms.service` フィールドが削除され、ドキュメントの構造がよりシンプルに整理されています。この修正により、内容が明確になり、読者が必要な情報に焦点を合わせやすくなります。

このドキュメントの目的は、サービス検索からエラーメッセージが表示されない場合のインデクサーの問題とその解決策に関するガイダンスを提供することです。メタデータの削除は、ドキュメント全体の可読性とユーザー体験の向上を目指しています。

## articles/search/search-indexer-tutorial.md{#item-a3e3ff}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'C# Tutorial: Index Azure SQL Data'
 titleSuffix: Azure AI Search
 description: In this C# tutorial, you connect to Azure SQL Database, extract searchable data, and load it into an Azure AI Search index.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-indexer-tutorial.md` ドキュメントにおける複数のメタデータフィールドの削除を示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されました。これにより、ドキュメントがより簡潔に整理され、ユーザーが内容に集中しやすくなっています。

このドキュメントは、C# を使用して Azure SQL データベースに接続し、検索可能なデータを抽出して Azure AI Search インデックスにロードする手順を説明するチュートリアルです。メタデータの削除は、情報の明確さを高め、ドキュメント全体の可読性を向上させる目的があります。

## articles/search/search-language-support.md{#item-a7979b}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Multi-language indexing for non-English search queries
 titleSuffix: Azure AI Search
 description: Create an index that supports multi-language content and then create queries scoped to that content.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-language-support.md` ドキュメントにおいて、いくつかのメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されています。これにより、ドキュメントがより簡潔になり、読者が情報に集中しやすくなります。

このドキュメントは、非英語の検索クエリをサポートするマルチランゲージインデックスを作成し、コンテンツにスコープを設定したクエリを作成する方法について説明しています。メタデータの削除によって、情報の清潔さと明瞭さが向上し、ユーザー体験の向上が期待されます。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Service Limits for Tiers and SKUs
 titleSuffix: Azure AI Search
 description: Service limits used for capacity planning and maximum limits on requests and responses for Azure AI Search.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-limits-quotas-capacity.md` ドキュメントにおけるメタデータフィールドの削除を含んでいます。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されました。この変更により、ドキュメントがよりシンプルになり、内容への集中が促進されます。

このドキュメントは、Azure AI Search におけるサービスの制限、ティアや SKU による最大リクエストおよびレスポンスの制限に関する情報を提供します。メタデータの削除は、情報の明確さを高め、全体的な可読性を向上させることを目的としています。

## articles/search/search-manage-azure-cli.md{#item-7fdd08}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Azure CLI scripts using the az search module
 titleSuffix: Azure AI Search
 description: Create and configure an Azure AI Search service with the Azure CLI. You can scale a service up or down, manage admin and query api-keys, and query for system information.
-
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-manage-azure-cli.md` ドキュメントにおいて、いくつかのメタデータフィールドが削除されたことを示します。具体的には、`author` フィールドと `ms.author` フィールド、さらには `ms.service` フィールドが削除されています。これにより、ドキュメントがさらにシンプルで読みやすくなります。

このドキュメントは、Azure CLI を使用して Azure AI Search サービスを作成および構成する方法について説明しています。ユーザーはサービスのスケーリング、管理者やクエリAPIキーの管理、システム情報のクエリなどを行うことができます。メタデータの削除によって、情報の明確さが増し、ユーザーが求める具体的な情報にアクセスしやすくなります。

## articles/search/search-manage-powershell.md{#item-3c3485}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: PowerShell scripts using Azure Search PowerShell module
 titleSuffix: Azure AI Search
 description: Create and configure an Azure AI Search service with PowerShell. You can scale a service up or down, manage admin and query api-keys, and query for system information.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-manage-powershell.md` ドキュメントにおいて特定のメタデータフィールドの削除を含んでいます。具体的には、`manager` フィールド、`author` フィールド、及び `ms.author` フィールドが削除されました。この編集により、ドキュメントが一層簡潔になり、内容への集中が高まります。

このドキュメントでは、PowerShell を使用して Azure AI Search サービスを作成および構成する方法について説明しています。ユーザーは、サービスをスケーリングしたり、管理者やクエリAPIキーを管理したり、システム情報をクエリしたりすることが可能です。メタデータの削除は、この情報へのアクセスをより明確にし、読者にとっての使いやすさを向上させることを目的としています。

## articles/search/search-markdown-data-tutorial.md{#item-32ea2a}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'Tutorial: Index Markdown Blobs'
 titleSuffix: Azure AI Search
 description: Learn how to index and search Markdown in Azure blobs using Azure AI Search REST APIs.
-
 author: mdonovan
 ms.author: mdonovan
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-markdown-data-tutorial.md` 文書において特定のメタデータフィールドが削除されたことを示しています。具体的には、`author` フィールド、`ms.author` フィールド、および `ms.service` フィールドが削除されました。この更新により、文書の見通しが良くなり、内容に対してのユーザーの集中が高まります。

この文書では、Azure AI Search REST APIを使用して、Azure Blob内のMarkdownをインデックス化し、検索する方法について学ぶことができます。メタデータの削除は、情報の明確さを保ちながら、ドキュメントの簡潔さを向上させることを目的としています。これにより、ユーザーは特定の手続きをより容易に理解できるようになります。

## articles/search/search-monitor-enable-logging.md{#item-e3600e}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Configure logging
 titleSuffix: Azure AI Search
 description: Set up diagnostic logging to collect information about indexing and query processing in Azure AI Search resource logs.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-monitor-enable-logging.md` ドキュメントから特定のメタデータフィールドの削除を含んでいます。具体的には、`manager` フィールド、`author` フィールド、及び `ms.author` フィールドが削除されました。この更新によって、文書の構造がよりシンプルになり、内容に対しての集中力が高まります。

このドキュメントでは、Azure AI Search リソースログにおけるインデックス作成およびクエリ処理に関する情報を収集するための診断ログの設定方法について解説しています。メタデータの削除は、ユーザーが必要な情報に迅速にアクセスできるようにするため、ドキュメントの効率を向上させることを目的としています。

## articles/search/search-monitor-logs-powerbi.md{#item-5b3491}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,6 @@ description: Visualize Azure AI Search logs and metrics with Power BI.
 author: gmndrg
 ms.author: gimondra
 manager: nitinme
-
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-monitor-logs-powerbi.md` 文書において特定のメタデータフィールドが削除されたことを示しています。具体的には、`ms.service` フィールドと `ms.custom` フィールドが削除されました。この更新により、文書がより簡潔になり、重要な情報に対してユーザーが集中しやすくなります。

このドキュメントは、Azure AI SearchのログとメトリクスをPower BIで視覚化する方法について説明しています。メタデータの削除は、情報の明瞭さを向上させながら、ユーザーが関連する内容を迅速に理解できるようにすることを目的としています。

## articles/search/search-monitor-queries.md{#item-279569}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Monitor queries
 titleSuffix: Azure AI Search
 description: Monitor query metrics for performance and throughput. Collect and analyze query string inputs in resource logs.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-monitor-queries.md` ドキュメントから特定のメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されました。この更新により、文書が簡潔になり、内容への集中を高めることが目的です。

このドキュメントでは、クエリのパフォーマンスとスループットをモニタリングする方法について説明しており、リソースログでクエリ文字列の入力を収集および分析することができます。メタデータの削除は、ユーザーが必要な情報に迅速にアクセスできるような構造を提供することを目指しています。

## articles/search/search-more-like-this.md{#item-56c565}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: moreLikeThis (preview) query feature
 titleSuffix: Azure AI Search
 description: Describes the moreLikeThis (preview) feature, which is available in preview versions of the Azure AI Search REST API.
-
 author: bevloh
 ms.author: beloh
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-more-like-this.md` ドキュメントからいくつかのメタデータフィールドが削除されたことを示しています。具体的には、`author` フィールド、`ms.author` フィールド、および `ms.service` フィールドが削除されました。この更新により、文書がよりシンプルになり、重要な情報に対するユーザーの集中を促進することを目的としています。

このドキュメントは、Azure AI Search REST APIのプレビュー版で利用可能な moreLikeThis 機能について説明しています。メタデータの整理は、ユーザーが必要な情報を速やかに見つけやすくするための工夫であり、情報の明瞭さを向上させるためのものです。

## articles/search/search-pagination-page-layout.md{#item-115902}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Shape search results
 titleSuffix: Azure AI Search
 description: Modify search result composition, get a document count, sort results, and add content navigation to search results in Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-pagination-page-layout.md` ドキュメントから特定のメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されました。この更新は、文書の構造を簡素化し、主要なコンテンツに焦点を当てやすくすることを目的としています。

このドキュメントでは、Azure AI Searchにおける検索結果の構成を変更し、ドキュメントのカウントを取得し、結果をソートし、検索結果へのコンテンツナビゲーションを追加する方法について説明しています。メタデータの削除は、ユーザーが必要な情報を迅速に見つけやすくし、文書の可読性を向上させることを目指しています。

## articles/search/search-query-create.md{#item-532822}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Create a full text query 
 titleSuffix: Azure AI Search
 description: Learn how to construct a query request for full text search in Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-create.md` ドキュメントから特定のメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されました。この更新は、文書をよりシンプルにし、ユーザーが必要な情報に集中しやすくすることを目的としています。

このドキュメントでは、Azure AI Searchにおけるフルテキスト検索のためのクエリリクエストの構築方法について説明しています。メタデータの削除は、情報の洪水を避け、内容の明快さを向上させる助けとなります。ユーザーが必要な情報を迅速に取得できるようにするための配慮といえます。

## articles/search/search-query-fuzzy.md{#item-a130e3}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Fuzzy search
 titleSuffix: Azure AI Search
 description: Implement a fuzzy search query for a "did you mean" search experience. Fuzzy search autocorrects a misspelled term or typo on the query.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-fuzzy.md` ドキュメントから特定のメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されています。この更新は、ドキュメントを簡素化し、ユーザーがコンテンツにより集中できるようにすることを目的としています。

このドキュメントでは、Azure AI Searchで「Did you mean」検索体験を実現するためのファジー検索クエリの実装方法について説明しています。ファジー検索は、クエリ内の誤字やタイプミスを自動的に修正する機能を提供します。メタデータの削除により、情報の一貫性が保たれ、読みやすさが向上しています。

## articles/search/search-query-lucene-examples.md{#item-ce3624}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,9 @@
 title: Examples of full Lucene query syntax
 titleSuffix: Azure AI Search
 description: Explore query examples that demonstrate the Lucene query syntax for fuzzy search, proximity search, term boosting, regular expression search, and wildcard searches in an Azure AI Search index.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
-
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-lucene-examples.md` ドキュメントから特定のメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、`ms.service` フィールド、及び `ms.custom` フィールドが削除されています。この更新は、ドキュメントをよりシンプルにし、ユーザーが重要な内容に集中できるようにすることを目的としています。

このドキュメントでは、Azure AI Searchにおけるファジー検索、近接検索、用語のブースティング、正規表現検索、およびワイルドカード検索に関するLuceneクエリ構文の例が紹介されています。メタデータの削除により、情報の明快さが向上し、ユーザーが必要な情報を容易に把握できるようになっています。

## articles/search/search-query-odata-collection-operators.md{#item-9fba57}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: OData collection operator reference
 titleSuffix: Azure AI Search
 description: When creating filter expressions in Azure AI Search queries, use "any" and "all" operators in lambda expressions when the filter is on a collection or complex collection field.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-odata-collection-operators.md` ドキュメントから特定のメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されています。この更新は、ドキュメントを簡素化し、ユーザーが内容に集中できるようにすることを目的としています。

このドキュメントでは、Azure AI Searchのクエリでフィルター式を作成する際に、コレクションまたは複雑なコレクションフィールドに対して「any」および「all」オペレーターをラバダ式で使用する方法について説明しています。メタデータの削除により、情報の一貫性が保たれ、ドキュメントがより明確になります。

## articles/search/search-query-odata-comparison-operators.md{#item-c92abf}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: OData comparison operator reference
 titleSuffix: Azure AI Search
 description: Syntax and reference documentation for using OData comparison operators (eq, ne, gt, lt, ge, and le) in Azure AI Search queries.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-odata-comparison-operators.md` ドキュメントから特定のメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されています。この更新は、ドキュメントをより明確にし、ユーザーが重要な内容に集中できるようにすることを目的としています。

このドキュメントでは、Azure AI Searchのクエリにおいて用いるOData比較演算子（eq、ne、gt、lt、ge、および le）の構文および参照情報が提供されています。メタデータの削除により、情報の透明性が向上し、ユーザーが必要な情報に対してアクセスしやすくなっています。

## articles/search/search-query-odata-filter.md{#item-69d5d6}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: OData filter reference
 titleSuffix: Azure AI Search
 description: OData language reference and full syntax used for creating filter expressions in Azure AI Search queries.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-odata-filter.md` ドキュメントから特定のメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されています。この更新は、ドキュメントを簡潔にし、ユーザーが内容に集中できるようにすることを目的としています。

このドキュメントでは、Azure AI Searchのクエリ内でフィルター式を作成する際に使用されるOData言語の参照および完全な構文が説明されています。メタデータの削除は、情報の明確性を高め、ユーザーが必要な情報に対してアクセスしやすくする効果があります。

## articles/search/search-query-odata-full-text-search-functions.md{#item-5748d4}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: OData full-text search function reference
 titleSuffix: Azure AI Search
 description: OData full-text search functions, search.ismatch and search.ismatchscoring, in Azure AI Search queries.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-odata-full-text-search-functions.md` ドキュメントから特定のメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されています。この更新は、ドキュメントの情報を整理し、ユーザーがコンテンツに集中できるようにすることを目的としています。

このドキュメントでは、Azure AI Searchのクエリにおいて使用されるODataのフルテキスト検索関数、特に `search.ismatch` および `search.ismatchscoring` に関する情報が提供されています。メタデータの削除により、情報の明確性が向上し、ユーザーは必要な技術的詳細により簡単にアクセスできるようになります。

## articles/search/search-query-odata-geo-spatial-functions.md{#item-859407}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: OData geo-spatial function reference
 titleSuffix: Azure AI Search
 description: Syntax and reference documentation for using OData geo-spatial functions, geo.distance and geo.intersects, in Azure AI Search queries.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-odata-geo-spatial-functions.md` ドキュメントから特定のメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されました。この変更は、ドキュメントのコンテンツを整理し、ユーザーが主要な情報により集中できるようにするためのものです。

このドキュメントは、Azure AI SearchのクエリにおけるODataの地理空間関数に関する構文と参照情報を提供します。特に、`geo.distance` および `geo.intersects` 関数について説明しています。メタデータの削除は、情報の明確性を向上させ、ユーザーが必要とする技術的な詳細にアクセスしやすくする効果があります。

## articles/search/search-query-odata-logical-operators.md{#item-61c263}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: OData logical operator reference
 titleSuffix: Azure AI Search
 description: Syntax and reference documentation for using OData logical operators, and, or, and not, in Azure AI Search queries.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-odata-logical-operators.md` ドキュメントから特定のメタデータフィールドが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されています。この更新の目的は、ドキュメントをより明確にし、ユーザーが主要な内容に集中できるようにすることです。

ドキュメントは、Azure AI SearchのクエリにおけるODataの論理演算子に関する構文および参照情報を提供しています。特に、`and`、`or`、`not` という演算子の使用方法について説明されています。メタデータの削除により、文書の目的と内容が洗練され、ユーザーが必要な情報にアクセスしやすくなる効果があります。

## articles/search/search-query-odata-orderby.md{#item-dff8d3}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: OData order-by reference
 titleSuffix: Azure AI Search
 description: Syntax and language reference documentation for using order-by in Azure AI Search queries.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-odata-orderby.md` ドキュメントから特定のメタデータが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されました。この変更は、ドキュメントの整理と明確化を目的としています。

このドキュメントは、Azure AI Searchにおけるクエリでの`order-by`の使用に関する構文および言語の参照情報を提供しています。`order-by`は、検索結果の並び替えを行うための重要な要素であり、ユーザーが情報を受け取る際の体験を向上させるために、この情報が役立ちます。メタデータが削除されることで、読みやすさと焦点が強化され、ユーザーがコンテンツに集中しやすくなる効果があります。

## articles/search/search-query-odata-search-in-function.md{#item-d768e7}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: OData search.in function reference
 titleSuffix: Azure AI Search
 description: Syntax and reference documentation for using the search.in function in Azure AI Search queries.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-odata-search-in-function.md` ドキュメントから特定のメタデータが削除されたことを反映しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されました。この更新は、文書の整理および可読性向上を目的としています。

該当ドキュメントは、Azure AI Searchにおける`search.in`関数の使用に関する構文と参照情報を提供しています。この関数は、特定の値のリストに対して検索を行うために使用され、ユーザーがより効率的にデータを取得できるように支援します。メタデータの削除により、中心となる情報が強調され、ユーザーが重要な内容に集中しやすくなる効果があります。

## articles/search/search-query-odata-search-score-function.md{#item-f51766}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: OData search.score function reference
 titleSuffix: Azure AI Search
 description: Syntax and reference documentation for using the search.score function in Azure AI Search queries.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-odata-search-score-function.md` ドキュメントから特定のメタデータが削除されたことを示しています。具体的には、`manager` フィールド、`author` フィールド、および `ms.author` フィールドが削除されました。この変更は、文書の内容をより明確にし、可読性を向上させることを目的としています。

このドキュメントは、Azure AI Searchにおける`search.score`関数の使用に関する構文および参照情報を提供しており、検索結果のスコアリングを制御するための重要な機能です。メタデータの削除によって、ユーザーは本来の情報に集中しやすくなり、内容がより際立つようになります。

## articles/search/search-query-odata-select.md{#item-8d6e1d}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: OData select reference
 titleSuffix: Azure AI Search
 description: Syntax and language reference for explicit selection of fields to return in the search results of Azure AI Search queries.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-odata-select.md` ドキュメントから特定のメタデータが削除されたことを示しています。削除されたのは、`manager`、`author`、および `ms.author` フィールドです。この修正は、文書をよりシンプルにし、情報のクリアさと可読性を高めることを意図しています。

このドキュメントは、Azure AI Searchにおける`OData`の`select`機能に関する構文および言語の参照を提供しています。`select`機能は、検索結果に返されるフィールドを明示的に選択するために使用され、ユーザーが必要な情報に迅速にアクセスできるようにします。メタデータの削除により、フォーカスが主な内容にシフトし、ユーザーは重要な情報をより簡単に見つけることができるようになります。

## articles/search/search-query-odata-syntax-reference.md{#item-14b8d9}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: OData expression syntax reference
 titleSuffix: Azure AI Search
 description: Formal grammar and syntax specification for OData expressions in Azure AI Search queries.
-
 manager: nitinme
 author: bevloh
 ms.author: beloh
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-odata-syntax-reference.md` ドキュメントから特定のメタデータが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されています。この修正は、文書の簡潔さを向上させ、読者が重要な情報に集中できるようにすることを目的としています。

このドキュメントは、Azure AI SearchにおけるOData式の文法および構文の仕様を提供しており、Azure AI Searchクエリで使用されるOData表現の正式な文法が説明されています。メタデータの削除により、文書がよりスムーズに読まれるようになり、技術的な内容に焦点を当てることができます。

## articles/search/search-query-overview.md{#item-dcd5d6}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Query types
 titleSuffix: Azure AI Search
 description: Learn about the types of queries supported in Azure AI Search, including vector and hybrid queries, free text, filter, autocomplete and suggestions, geospatial search, system queries, and document lookup.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-overview.md` ドキュメントから特定のメタデータが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` のフィールドが削除されています。この修正は、文書をよりシンプルにし、読者が中心となるコンテンツに集中できるようにするためのものです。

この文書では、Azure AI Searchでサポートされているさまざまなクエリタイプについて説明しており、ベクトルおよびハイブリッドクエリ、自由テキスト、フィルタ、オートコンプリートと提案、地理空間検索、システムクエリ、ドキュメントルックアップに関する情報が含まれています。メタデータの削除により、文書の可読性と理解しやすさが向上し、読者は検索クエリの機能に関する主な情報を容易に取得できるようになります。

## articles/search/search-query-partial-matching.md{#item-bd97dc}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Partial terms, patterns, and special characters
 titleSuffix: Azure AI Search
 description: Use wildcard, regex, and prefix queries to match on whole or partial terms in an Azure AI Search query request. Hard-to-match patterns that include special characters can be resolved using full query syntax and custom analyzers.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-partial-matching.md` ドキュメントから特定のメタデータが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されました。この修正により、文書がよりクリーンになり、読者が内容に集中しやすくなります。

このドキュメントでは、Azure AI Searchにおける部分一致のための用語、パターン、および特殊文字に関する情報が記載されています。ワイルドカードや正規表現、接頭辞クエリを使用して、完全または部分的な用語にマッチさせる方法や、特殊文字を含む難解なパターンを解決するための完全なクエリ構文とカスタムアナライザーの使用について説明しています。メタデータの削除により、文書のフォーカスが一層強まり、読者は重要な技術的な情報にアクセスしやすくなります。

## articles/search/search-query-simple-examples.md{#item-834766}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Examples of simple syntax
 titleSuffix: Azure AI Search
 description: Explore query examples that demonstrate the simple syntax for full text search, filter search, and geo search against an Azure AI Search index.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-simple-examples.md` ドキュメントから特定のメタデータが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されました。この修正により、文書の精度と可読性が向上し、読者が主な内容に集中できるようになります。

このドキュメントでは、Azure AI Searchのインデックスに対する全文検索、フィルター検索、地理検索のための簡単な構文を示すクエリの例が探求されています。メタデータの削除は、全体的な文書の焦点を高め、ユーザーに必要なテクニカルなコンテンツを明確に提供することを目的としています。これにより、Azure AI Searchの機能を理解する助けとなる情報がさらに強調されます。

## articles/search/search-query-troubleshoot-collection-filters.md{#item-abeca4}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Troubleshooting OData collection filters
 titleSuffix: Azure AI Search
 description: Learn approaches for resolving OData collection filter errors in Azure AI Search queries.
-
 author: bevloh
 ms.author: beloh
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-troubleshoot-collection-filters.md` ドキュメントから特定のメタデータが削除されたことを示しています。具体的には、`author`、`ms.author`、および `ms.service` フィールドが削除されました。この修正により、文書の構成が簡潔になり、読者がコンテンツにより集中しやすくなります。

このドキュメントでは、Azure AI SearchクエリにおけるODataコレクションフィルターエラーの解決方法について説明しています。メタデータの削除は、ドキュメントの理解を妨げる情報を減少させ、技術的な詳細に対する焦点を強化することを目的としています。結果として、読者はODataフィルターに関連する問題解決のアプローチによりアクセスしやすくなるでしょう。

## articles/search/search-query-understand-collection-filters.md{#item-32c01a}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: OData collection filters
 titleSuffix: Azure AI Search
 description: Learn the mechanics of how OData collection filters work in Azure AI Search queries, including limitations and behaviors unique to collections.
-
 author: bevloh
 ms.author: beloh
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-query-understand-collection-filters.md` ドキュメントから特定のメタデータが削除されたことを示しています。具体的には、`author`、`ms.author`、および `ms.service` フィールドが削除されました。この修正により、文書の情報が整理され、読者が内容に集中しやすくなります。

このドキュメントでは、Azure AI SearchクエリにおけるODataコレクションフィルターの仕組みや、コレクション特有の制限や挙動について学ぶことができます。メタデータの削除は、この技術的内容に対する焦点を高め、読者が重要な情報へよりスムーズにアクセスできるようにすることを目的としています。これにより、ODataコレクションフィルターの理解がさらに深まるでしょう。

## articles/search/search-relevance-overview.md{#item-cb0e09}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Relevance
 titleSuffix: Azure AI Search
 description: Describes how the scoring and ranking algorithms work in Azure AI Search and how to use them together.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-relevance-overview.md` ドキュメントから特定のメタデータが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されました。この修正により、文書がよりシンプルになり、読者が内容に集中しやすくなります。

このドキュメントは、Azure AI Searchにおけるスコアリングおよびランキングアルゴリズムの動作を説明し、それらをどのように組み合わせて使用するかについて具体的な情報を提供します。メタデータの削除は、こうした技術的内容に焦点を当てることを目的としており、読者が重要な情報にアクセスしやすくなるよう配慮されています。結果的に、Azure AI Searchのリレバンス（関連性）の理解が深まることが期待されます。

## articles/search/search-security-get-encryption-keys.md{#item-7aed9d}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Find encryption key information
 titleSuffix: Azure AI Search
 description: Retrieve the encryption key name and version used in an index or synonym map so that you can manage the key in Azure Key Vault.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-security-get-encryption-keys.md` ドキュメントから特定のメタデータが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されました。この修正により、文書が整理され、読者がその内容により集中できるようになります。

このドキュメントでは、インデックスや同義語マップで使用される暗号化キーの名前とバージョンを取得し、それらをAzure Key Vaultで管理する方法が説明されています。メタデータの削除は、文書の焦点を明確にし、テクニカルコンテンツをより分かりやすくすることを目的としています。これにより、ユーザーはAzure AI Searchでの暗号化キーの利用と管理についての理解を深めることが期待されます。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Encrypt data using customer-managed keys
 titleSuffix: Azure AI Search
 description: Supplement server-side encryption in Azure AI Search using customer managed keys (CMK) or bring your own keys (BYOK) that you create and manage in Azure Key Vault.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-security-manage-encryption-keys.md` ドキュメントから特定のメタデータが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されました。この修正によって、文書はよりシンプルになり、読者が内容に集中できるようになります。

このドキュメントでは、Azure AI Searchにおけるデータの暗号化に関して、カスタマー管理キー（CMK）や持ち込みキー（BYOK）を使用し、Azure Key Vaultで作成・管理する方法が説明されています。メタデータの削除は、文書の焦点をテクニカルコンテンツに明確にすることを目的としており、ユーザーが暗号化のプロセスを理解しやすくなることが期待されます。全体として、この変更によってAzure AI Searchでのデータ管理に関する情報がより利用しやすくなります。

## articles/search/search-security-overview.md{#item-6b3f1e}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Security overview
 titleSuffix: Azure AI Search
 description: Learn about the security features in Azure AI Search to protect endpoints, content, and operations.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-security-overview.md` ドキュメントから特定のメタデータが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されました。この修正により、ドキュメントはよりクリーンになり、ユーザーがコンテンツに集中しやすくなります。

このドキュメントでは、Azure AI Searchにおけるセキュリティ機能について説明されており、エンドポイント、コンテンツ、操作を保護するための手段についての洞察を提供しています。メタデータの削除は、内容を圧縮し、ユーザーが重要なセキュリティ機能に注目できるようにすることを目的としています。この変更を通じて、Azure AI Searchのセキュリティに関する理解が一層深まることが期待されます。

## articles/search/search-security-trimming-for-azure-search.md{#item-d8ae51}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Security filter pattern
 titleSuffix: Azure AI Search
 description: Learn how to implement security privileges at the document level for Azure AI Search search results, using security filters and user identities.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-security-trimming-for-azure-search.md` ドキュメントから特定のメタデータフィールドの削除を示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されました。この修正によって、文書はより明確になり、ユーザーが情報を把握しやすくなることを目的としています。

ドキュメントは、Azure AI Searchにおけるセキュリティ権限を文書レベルで実装する方法について説明しており、セキュリティフィルターやユーザーのアイデンティティを活用した検索結果の制御についての洞察を提供します。メタデータの削除は、主要な内容に焦点を当てさせ、ユーザーが重要な情報により集中できるようにするためのステップです。これにより、Azure AI Searchの安全なデータ管理に関する理解がさらに深まることが期待されます。

## articles/search/search-semi-structured-data.md{#item-d3388d}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'Tutorial: Index Semi-Structured Data in JSON Blobs'
 titleSuffix: Azure AI Search
 description: Learn how to index and search semi-structured Azure JSON blobs using Azure AI Search REST APIs.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-semi-structured-data.md` ドキュメントからいくつかのメタデータフィールドの削除を示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されました。この修正により、文書がよりシンプルになり、読者が主要な内容に集中しやすくなります。

このドキュメントは、Azure AI SearchのREST APIを使用して、半構造化データであるJSONブロブをインデックスし、検索する方法についてのチュートリアルを提供しています。メタデータの削除によって、ユーザーが重要なトピックに焦点を当てられるようにし、理解を深めることが促進されることが期待されます。検索とインデクシングのプロセスに関する明瞭な情報を提供することを目的としています。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Choose a service tier
 titleSuffix: Azure AI Search
 description: 'Learn about the service tiers (or SKUs) for Azure AI Search. A search service can be provisioned at these tiers: Free, Basic, Standard, and Storage Optimized. Standard is available in various resource configurations and capacity levels.'
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-sku-tier.md` ドキュメントからいくつかのメタデータフィールドが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されました。この修正により、ドキュメントはよりクリーンで、内容に集中しやすくなります。

このドキュメントは、Azure AI Searchのサービスティア（SKU）について説明しており、利用可能なティアとして無料、ベーシック、スタンダード、およびストレージ最適化が含まれています。特に、スタンダードはさまざまなリソース構成やキャパシティレベルで提供されています。このメタデータの削除は、ユーザーにとっての主要な情報の視認性を向上させることを目的としており、サービスに関する理解をより深める助けとなることが期待されます。

## articles/search/search-synapseml-cognitive-services.md{#item-dcc36f}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'Tutorial: Index at Scale (Spark)'
 titleSuffix: Azure AI Search
 description: Search big data from Apache Spark that's been transformed by SynapseML. Load invoices into data frames, apply machine learning, and then send output to a generated search index.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-synapseml-cognitive-services.md` ドキュメントから複数のメタデータフィールドが削除されたことを示しています。具体的には、`manager`、`author`、及び `ms.author` フィールドが削除されました。この修正によって、ドキュメントがよりシンプルになり、読者が主要な内容により集中できるようになります。

このドキュメントは、Apache Sparkによって変換されたビッグデータを検索する方法についてのチュートリアルを提供しています。請求書をデータフレームに読み込み、機械学習を適用し、生成された検索インデックスに出力を送信するプロセスが説明されています。このメタデータの削除は、読者がチュートリアルの実用的な側面に焦点を当てやすくすることを目指しており、使いやすさと理解を向上させることが期待されます。

## articles/search/search-synonyms.md{#item-2d5d63}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Add synonyms to expand queries for equivalent terms
 titleSuffix: Azure AI Search
 description: Create a synonym map to expand the scope of a search query over an Azure AI Search index. The query can search on equivalent terms provided in the synonym map, even if the query doesn't explicitly include the term.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-synonyms.md` ドキュメントからいくつかのメタデータフィールドが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されています。この修正により、ドキュメントはより簡潔になり、重要な内容に焦点を合わせやすくなります。

このドキュメントは、Azure AI Searchインデックスの検索クエリの範囲を拡張するための同義語マップの作成方法について説明しています。具体的には、同義語マップに提供された同等の用語を使用して、クエリが明示的にその用語を含まなくても検索できるようになります。このメタデータの削除は、ドキュメントの視認性を高め、ユーザーが内容を容易に理解できるようにすることを目的としており、読者の利便性向上に寄与することが期待されます。

## articles/search/search-try-for-free.md{#item-36e28d}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'Try Azure AI Search for free'
 titleSuffix: Azure AI Search
 description: Learn how to create a trial subscription and use credits for trying advanced features.
-
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-try-for-free.md` ドキュメントからいくつかのメタデータフィールドが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されています。この修正によって、ドキュメントはより簡潔になり、読者が主要な情報に集中しやすくなります。

このドキュメントは、Azure AI Searchを無料で試すための手順を説明しており、トライアルサブスクリプションの作成方法と、クレジットを使用して高度な機能を試す方法を学ぶことができます。メタデータの削除は、内容を読みやすくし、重要な部分に焦点を合わせやすくすることを意図しており、ユーザー体験を向上させることが期待されています。

## articles/search/search-what-is-an-index.md{#item-5a3344}

<details>
<summary>Diff</summary>
````diff
@@ -2,11 +2,9 @@
 title: Search index overview
 titleSuffix: Azure AI Search
 description: Explains what is a search index in Azure AI Search and describes content, construction, physical expression, and the index schema.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
-
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-what-is-an-index.md` ドキュメントから複数のメタデータフィールドが削除されたことを示しています。具体的には、`manager`、`author`、`ms.author`、および `ms.service` エントリが削除されています。この修正により、ドキュメントはよりシンプルになり、読者が重要な情報に集中できるようになります。

ドキュメント自体は、Azure AI Searchにおける検索インデックスの概要を説明しており、その内容、構成、物理的表現、インデックススキーマについて詳しく説明しています。このメタデータの削除は、文書の視認性の向上を目的としており、ユーザーが内容を容易に把握できるようにすることを意図しています。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Introduction to Azure AI Search
 titleSuffix: Azure AI Search
 description: Azure AI Search is an AI-powered information retrieval platform, helps developers build rich search experiences and generative AI apps that combine large language models with enterprise data.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-what-is-azure-search.md` ドキュメントからいくつかのメタデータフィールドが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されました。この修正により、ドキュメントはより明確になり、読者が重要な情報に対して集中しやすくなります。

ドキュメント自体は、Azure AI Searchの導入を説明しており、AIを活用した情報検索プラットフォームとして、開発者が豊かな検索体験や、エンタープライズデータと統合した生成AIアプリを構築するのに役立つことを説明しています。メタデータの削除は、内容をより読みやすくし、主要なポイントを強調するためのものであり、全体的なユーザー体験の向上を目指しています。

## articles/search/search-what-is-data-import.md{#item-d73ef5}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Data import and data ingestion
 titleSuffix: Azure AI Search
 description: Populate and upload data to an index in Azure AI Search from external data sources.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/search-what-is-data-import.md` ドキュメントからいくつかのメタデータフィールドが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されています。この修正により、ドキュメントは簡潔さが増し、読者が重要な情報に集中できるようになります。

ドキュメント自体は、Azure AI Searchにおけるデータのインポートとデータ摂取に関する説明を行っており、外部データソースからインデックスにデータを格納しアップロードする方法について詳しく説明しています。メタデータの削除は、情報をより効果的に伝達するための改善の一環であり、読者が文書の主題に焦点を合わせやすくすることを目的としています。

## articles/search/semantic-answers.md{#item-c3fee9}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Return a semantic answer
 titleSuffix: Azure AI Search
 description: Describes the composition of a semantic answer and how to obtain answers from a result set.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/semantic-answers.md` ドキュメントからいくつかのメタデータフィールドが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されており、これにより文書がより簡潔になります。

この文書は、セマンティックアンサーの構成と、結果セットから回答を取得する方法について説明しています。削除されたメタデータは、文書の主旨に対してあまり必要でない情報とされ、ドキュメントの内容に焦点を当てやすくするための変更です。全体として、この修正は読者が主要な情報に集中できるようにするための改善と考えられます。

## articles/search/semantic-how-to-enable-disable.md{#item-71ac1e}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Enable or disable semantic ranker
 titleSuffix: Azure AI Search
 description: Learn how to turn semantic ranker on or off in Azure AI Search, and how to prevent others from enabling it.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/semantic-how-to-enable-disable.md` ドキュメントからいくつかのメタデータフィールドが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されました。この修正により、文書の構造が簡潔になり、読者が重要な内容に集中しやすくなります。

この文書は、Azure AI Searchにおけるセマンティックランカーのオン/オフの切り替え方法や、他のユーザーがそれを有効にできないようにする方法について説明しています。削除されたメタデータは、文書内容に対する重要性が低いと考えられ、情報の明確性を高めるための改善として解釈されます。全体的に、この変更は文書の読みやすさと利便性を向上させることを目的としています。

## articles/search/semantic-how-to-query-request.md{#item-85530d}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Add semantic ranking
 titleSuffix: Azure AI Search
 description: Set a semantic query type to attach the deep learning models of semantic ranker.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/semantic-how-to-query-request.md` ドキュメントからいくつかのメタデータフィールドが削除されたことを示しています。具体的には、`manager`、`author`、および `ms.author` フィールドが削除されました。この修正により、文書の構成がよりシンプルになり、読者が主要な情報に集中できるようになります。

この文書は、セマンティックランクを追加する方法について説明しており、セマンティックランカーの深層学習モデルを接続するためのセマンティッククエリタイプの設定方法に焦点を当てています。削除されたメタデータは、文書の内容にあまり影響を与えないとみなされ、文書のクリアさを向上させることを目的とした変更です。全体として、この修正は読者が重要な情報にアクセスしやすくするための改善と考えられます。

## articles/search/semantic-how-to-query-rewrite.md{#item-3e168f}

<details>
<summary>Diff</summary>
````diff
@@ -3,8 +3,8 @@ title: Rewrite queries with semantic ranker in Azure AI Search
 titleSuffix: Azure AI Search
 description: Learn how to rewrite queries with semantic ranker in Azure AI Search
 manager: nitinme
-author: eric-urban
-ms.author: eur
+author: HeidiSteen
+ms.author: heidist
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.custom:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者情報の更新"
}
```

### Explanation
この変更は、`articles/search/semantic-how-to-query-rewrite.md` ドキュメント内で著者に関するメタデータが更新されたことを示しています。具体的には、`author` と `ms.author` フィールドが別の著者に差し替えられました。元の著者である "eric-urban" が "HeidiSteen" に、`ms.author` フィールドも "eur" から "heidist" に変更されています。

この文書は、Azure AI Searchにおけるセマンティックランカーを使用したクエリの書き換え方法について学ぶことを目的としています。著者情報の更新は、文書の権威性や信頼性を高めるために重要です。この変更により、最新の著者情報が反映され、読者は現在の文書の責任者に関する正確な情報を得ることができます。全体的に、この修正は文書の透明性と正確性を確保するための重要な改善です。

## articles/search/semantic-search-overview.md{#item-b7497b}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Semantic ranking
 titleSuffix: Azure AI Search
 description: Learn how Azure AI Search uses deep learning semantic ranking models from Bing to make search results more intuitive.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/semantic-search-overview.md` ドキュメントからメタデータの一部が削除されたことを示しています。具体的には、`manager` フィールドが削除され、それに伴い документの構成がシンプルになりました。

この文書は、Azure AI SearchがBingの深層学習セマンティックランキングモデルを使用して検索結果をどのように直感的にするかについて説明しています。メタデータの削除は、文書の主要なメッセージに集中できるようにし、読者にとって内容がより明確になることを目的としています。この修正は、文書の整頓と情報の明確さを向上させるための小さな改善です。

## articles/search/service-configure-firewall.md{#item-75be3f}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Configure network access
 titleSuffix: Azure AI Search
 description: Configure IP control policies to restrict network access to your Azure AI Search service to specific IP addresses.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/service-configure-firewall.md` ドキュメントから管理者に関するメタデータが削除されたことを示しています。具体的には、`manager` フィールドが削除され、文書の構成が簡略化されました。

この文書では、特定のIPアドレスに対してAzure AI Searchサービスへのネットワークアクセスを制限するためのIP制御ポリシーの設定方法について説明しています。メタデータの削除は、文書の主要な内容に焦点を当てるためのもので、読者にとってより明確で集中した情報を提供することを目的としています。このような修正は、文書の整頓を促進し、内容の理解を助けるために有益です。

## articles/search/speller-how-to-add.md{#item-9b4502}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Add spell check to queries
 titleSuffix: Azure AI Search
 description: Attach spelling correction to the query pipeline, to fix typos on query terms before executing the query.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/speller-how-to-add.md` ドキュメントから`manager`フィールドが削除されたことを示しています。これにより、文書の情報が簡潔になり、主要なコンテンツに焦点を当てることが促進されました。

この文書は、クエリパイプラインにスペルチェックを追加し、クエリ用語の誤字を修正する方法について説明しています。メタデータの削除は、読者にとって内容がより明確に理解できるようにするための措置であり、文書全体の整頓を助ける任意の小さな改善です。

## articles/search/troubleshoot-shared-private-link-resources.md{#item-0e1867}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Troubleshoot shared private link resources
 titleSuffix: Azure AI Search
 description: Troubleshooting guide for common problems when managing shared private link resources in Azure AI Search.
-
 manager: nitinme
 author: arv100kri
 ms.author: arjagann
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/troubleshoot-shared-private-link-resources.md` ドキュメントから`manager`フィールドが削除されたことを示しています。この小さな変更により、ドキュメントがより明確になり、主要な情報に焦点を当てることが可能になりました。

この文書は、Azure AI Searchにおける共有プライベートリンクリソースの管理時に発生する一般的な問題に対するトラブルシューティングガイドです。メタデータの削除は、内容を明確にし、読者が必要な情報に迅速にアクセスできるようにするための一環として行われたと考えられます。このような改善は、文書自体の整理とユーザビリティ向上に寄与します。

## articles/search/tutorial-csharp-create-mvc-app.md{#item-608a5d}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Add search to ASP.NET Core MVC
 titleSuffix: Azure AI Search
 description: In this Azure AI Search tutorial, learn how to add search to an ASP.NET Core (Model-View-Controller) application.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-csharp-create-mvc-app.md` ドキュメントから`manager`フィールドが削除されたことを示しています。この変更により、文書がよりシンプルになり、重要な情報に対する焦点が強化されました。

このチュートリアルは、Azure AI Searchを使用してASP.NET Core (モデル-ビュー-コントローラー) アプリケーションに検索機能を追加する方法について説明しています。メタデータの削除は、内容をより明確にし、読者が関連情報をすばやく把握できるようにすることを目的としています。このような小さな改善は、全体的な文書の読みやすさを向上させるものです。

## articles/search/tutorial-document-extraction-image-verbalization.md{#item-398a90}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'Tutorial: Verbalize images using generative AI'
 titleSuffix: Azure AI Search
 description: Learn how to extract, index, and search multimodal content using the Document Extraction skill for chunking and GenAI Prompt skill for image verbalizations.
-
 manager: arjagann
 author: mdonovan
 ms.author: mdonovan
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-document-extraction-image-verbalization.md` ドキュメントから`manager`フィールドが削除されたことを示しています。この修正により、文書がより洗練され、必要な情報に焦点が当てられるようになりました。

このチュートリアルは、ドキュメント抽出スキルを利用してマルチモーダルコンテンツを抽出、インデックス化、検索する方法を学ぶことを目的としています。また、生成AIプロンプトスキルを使用した画像の言語化についても説明しています。メタデータの削除は、文書の明確性を向上させ、読者が必要な情報に迅速にアクセスできるようにするために実施されました。このような改善は、ユーザーエクスペリエンスの向上に寄与します。

## articles/search/tutorial-document-extraction-multimodal-embeddings.md{#item-a3db59}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'Tutorial: Vectorize images and text'
 titleSuffix: Azure AI Search
 description: Learn how to extract, index, and search multimodal content using the Document Extraction skill for chunking and Azure AI Vision for embeddings.
-
 manager: arjagann
 author: mdonovan
 ms.author: mdonovan
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-document-extraction-multimodal-embeddings.md` ドキュメントから`manager`フィールドが削除されたことを示しています。この修正により、文書の内容がより明瞭になり、重要な情報に集中できるようになりました。

このチュートリアルでは、ドキュメント抽出スキルを使用してマルチモーダルコンテンツを抽出、インデックス化、検索する方法について学ぶことができます。特に、画像とテキストをベクトル化する過程に焦点を当てており、Azure AI Visionを利用した埋め込み技術にも言及しています。メタデータの削除は、文書のクリーンさを向上させ、読者が必要な情報を容易に見つけられるようにするために行われました。このような小さな更新は、全体のユーザー体験を向上させる効果があります。

## articles/search/tutorial-document-layout-image-verbalization.md{#item-f5de57}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'Tutorial: Verbalize images from a structured document layout'
 titleSuffix: Azure AI Search
 description: Learn how to extract, index, and search multimodal content using the Document Layout skill for chunking and GenAI Prompt skill for image verbalizations.
-
 manager: arjagann
 author: rawan    
 ms.author: rawan
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-document-layout-image-verbalization.md` ドキュメントから`manager`フィールドが削除されたことを示しています。この変更により、文書がよりシンプルになり、読者が重要な情報に集中しやすくなります。

このチュートリアルは、構造化されたドキュメントレイアウトから画像を言語化する方法を学ぶことを目的としています。具体的には、ドキュメントレイアウトスキルを利用してマルチモーダルコンテンツを抽出、インデックス化、検索する方法に焦点を当てており、生成AIプロンプトスキルを使用した画像の言語化も解説されています。メタデータの削除は、文書の明瞭性と精度を向上させ、ユーザーエクスペリエンスを改善するために行われました。このような小規模な改訂は、資料全体の使いやすさに寄与します。

## articles/search/tutorial-document-layout-multimodal-embeddings.md{#item-f67371}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'Tutorial: Vectorize from a structured document layout'
 titleSuffix: Azure AI Search
 description: Learn how to extract, index, and search multimodal content using the Document Layout skill for chunking and Azure AI Vision for embeddings.
-
 manager: arjagann
 author: rawan
 ms.author: rawan
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-document-layout-multimodal-embeddings.md` ドキュメントから`manager`フィールドが削除されたことを示しています。この修正により、文書が簡潔になり、読者が重要な情報に集中しやすくなります。

このチュートリアルでは、構造化されたドキュメントレイアウトからのベクトル化について学ぶことができ、ドキュメントレイアウトスキルを使ってマルチモーダルコンテンツを抽出、インデックス化、検索する方法を詳述しています。また、Azure AI Visionを使用した埋め込み技術にも触れられています。メタデータの削除は文書の可読性を向上させ、ユーザーの体験をより良くするために行われました。このような小規模な更新は、全体のクオリティ向上に寄与します。

## articles/search/tutorial-rag-build-solution-index-schema.md{#item-9a17ca}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'RAG tutorial: Design an index'
 titleSuffix: Azure AI Search
 description: Design an index for RAG patterns in Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-rag-build-solution-index-schema.md` ドキュメントから`manager`フィールドが削除されたことを示しています。この修正により、文書がシンプルになり、読者が重要な情報に集中しやすくなります。

このチュートリアルは、Azure AI Search における RAG（Retriever-Augmented Generation）パターンのためのインデックスデザインに焦点を当てています。特に、インデックス設計の方法に関するガイダンスを提供し、ユーザーが効果的な検索ソリューションを構築できるようにすることを目的としています。メタデータの削除は、文書の可読性を向上させ、ユーザーエクスペリエンスを高めるためのものであり、読み手にとってより明確な内容を提供します。

## articles/search/tutorial-rag-build-solution-maximize-relevance.md{#item-2fdb09}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'RAG tutorial: Tune relevance'
 titleSuffix: Azure AI Search
 description: Learn how to use the relevance tuning capabilities to return high quality results for generative search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-rag-build-solution-maximize-relevance.md` ドキュメントから`manager`フィールドが削除されたことを示しています。この修正により、文書がより簡潔になり、読者が重要な内容に集中しやすくなります。

このチュートリアルでは、生成検索のために高品質な結果を得るためのリレバンストuning機能の使用方法について学ぶことができます。特に、Azure AI Searchにおけるリレバンストレーニングの重要性と、それをどのように活用するかに焦点を当てています。メタデータの削除は、文書の可読性を向上させ、ユーザーエクスペリエンスを向上させるための一助となっています。これにより、読者はクリアで役立つ情報にアクセスできるようになります。

## articles/search/tutorial-rag-build-solution-minimize-storage.md{#item-088ad8}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'RAG tutorial: Minimize storage and costs'
 titleSuffix: Azure AI Search
 description: Compress vectors using narrow data types and scalar quantization. Remove extra copies of stored vectors to further save on space.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-rag-build-solution-minimize-storage.md` ドキュメントから`manager`フィールドが削除されたことを示しています。この修正により、ドキュメントがより明確で簡潔になり、読者が本文に集中しやすくなります。

このチュートリアルでは、ストレージとコストを最小化する方法について説明しています。特に、狭いデータ型を使用したベクトルの圧縮や、スカラー量子化の技術を利用して、保存されるベクトルの余分なコピーを削除する方法に焦点を当てています。メタデータの削除は、内容の可読性を高め、ユーザーの理解を促進するために役立つものであり、文書の全体的な品質向上に寄与しています。

## articles/search/tutorial-rag-build-solution-pipeline.md{#item-25ce01}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'RAG tutorial: Build an indexing pipeline'
 titleSuffix: Azure AI Search
 description: Create an indexer-driven pipeline that loads, chunks, embeds, and ingests content for RAG solutions on Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-rag-build-solution-pipeline.md` ドキュメントから`manager`フィールドが削除されたことを示しています。この修正により、ドキュメントがより簡素化され、読者が主要な内容に集中できるようになります。

このチュートリアルでは、Azure AI SearchでのRAGソリューション用に、コンテンツをロード、チャンク分割、埋め込み、および取り込みを行うインデクサ駆動のパイプラインの構築方法について説明しています。メタデータの削除は、内容のフォーカスを高め、ユーザーにとって有益な情報を提供する上で役立っています。これにより、文書はよりクリーンで、ナビゲーションしやすくなっています。

## articles/search/tutorial-rag-build-solution-query.md{#item-93965f}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: 'RAG tutorial: Search using an LLM'
 titleSuffix: Azure AI Search
 description: Learn how to build queries and engineer prompts for LLM-enabled search on Azure AI Search. Queries used in generative search provide the inputs to an LLM chat engine.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-rag-build-solution-query.md` ドキュメントから`manager`フィールドが削除されたことを示しています。これにより、文書がよりすっきりとした印象となり、読者がコンテンツに集中しやすくなります。

このチュートリアルでは、Azure AI SearchにおけるLLM（大規模言語モデル）対応の検索機能のために、クエリを構築しプロンプトをエンジニアリングする方法を学ぶことができます。生成的な検索に使用されるクエリは、LLMチャットエンジンへの入力を提供します。メタデータの削除は、文書の可読性を向上させ、内容に対する理解を深める役割を果たしています。

## articles/search/tutorial-rag-build-solution.md{#item-c7eca4}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Build a RAG solution
 titleSuffix: Azure AI Search
 description: Learn how to build a generative search (RAG) app using LLMs and your proprietary grounding data in Azure AI Search.
-
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-rag-build-solution.md` ドキュメントから`manager`フィールドが削除されたことを反映しています。この修正により、ドキュメントが簡素化され、読者がより重要な内容に集中できるようになっています。

このチュートリアルでは、Azure AI Searchを使用して、LLM（大規模言語モデル）と独自の基盤データを活用した生成的検索（RAG）アプリの構築方法について学ぶことができます。メタデータの削除は、文書の明瞭さを向上させるとともに、ユーザーの体験を向上させることに寄与しています。

## articles/search/vector-search-how-to-assign-narrow-data-types.md{#item-6b81cd}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Assign narrow data types
 titleSuffix: Azure AI Search
 description: In vector search, assign narrow data types to vector fields to reduce the storage requirements of vector indexes.
-
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-assign-narrow-data-types.md` ドキュメントから一部のメタデータ、具体的には`author`、`ms.author`、`ms.service`フィールドが削除されたことを示しています。この修正により、文書の内容が一層シンプルになり、読者が情報に集中しやすくなります。

このドキュメントでは、ベクター検索においてベクターフィールドに狭いデータ型を割り当てる方法について説明しています。これにより、ベクターインデックスのストレージ要件を削減することができます。メタデータの削除は、文書の可読性を向上させ、ユーザーが求める情報に迅速にアクセスできるようにするための改善です。

## articles/search/vector-search-how-to-chunk-documents.md{#item-b79133}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Chunk documents in vector search
 titleSuffix: Azure AI Search
 description: Learn strategies for chunking PDFs, HTML files, and other large documents for vectors and search indexing and query workloads.
-
 author: arv100kri
 ms.author: arjagann
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-chunk-documents.md` ドキュメントから`author`、`ms.author`、および`ms.service`のメタデータフィールドが削除されたことを示しています。この修正により、文書がより簡潔になり、読者はより核となる内容にフォーカスしやすくなります。

このドキュメントは、PDFやHTMLファイルなどの大きな文書をベクターと検索インデックス、クエリワークロードのためにチャンク化する戦略について学ぶことができます。メタデータの削除は、ユーザーが目的の内容に迅速にアクセスできるようにするため、文書の読みやすさを向上させる効果があります。

## articles/search/vector-search-how-to-configure-compression-storage.md{#item-c653c3}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Choose vector optimization
 titleSuffix: Azure AI Search
 description: Learn about the vector compression options in Azure AI Search, and how to reduce storage through narrow data types, built-in scalar or quantization, truncated dimensions, and elimination of redundant storage.
-
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-configure-compression-storage.md` ドキュメントから`author`、`ms.author`、および`ms.service`のメタデータフィールドが削除されたことを示しています。この修正により、ドキュメントがシンプルになり、読者が重要な情報に集中しやすくなります。

このドキュメントでは、Azure AI Searchにおけるベクター圧縮オプションについて学ぶことができ、狭いデータ型や組み込みスカラー、量子化、次元の切り捨て、冗長ストレージの排除を通じてストレージを削減する方法が解説されています。メタデータの除去は、ユーザーが必要な情報に素早くアクセスできるようにし、ドキュメント全体の可読性を向上させることを目的としています。

## articles/search/vector-search-how-to-configure-vectorizer.md{#item-30ffd8}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Configure a vectorizer
 titleSuffix: Azure AI Search
 description: Steps for adding a vectorizer to a search index in Azure AI Search. A vectorizer calls an embedding model that generates embeddings from text.
-
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-configure-vectorizer.md` ドキュメントから`author`、`ms.author`、および`ms.service`のメタデータフィールドが削除されたことを示しています。この修正により、ドキュメントがより簡潔になり、読者にとって重要な内容にアクセスしやすくなります。

このドキュメントは、Azure AI Searchにおいて検索インデックスにベクタイザを追加するための手順を説明しています。ベクタイザは、テキストから埋め込みを生成する埋め込みモデルを呼び出します。メタデータの削除は、ドキュメントの可読性を改善し、ユーザーが必要な情報を迅速に見つけられるようにすることを目的としています。

## articles/search/vector-search-how-to-create-index.md{#item-97c769}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Create a vector index
 titleSuffix: Azure AI Search
 description: Create or update a search index to include vector fields.
-
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-create-index.md` ドキュメントから`author`、`ms.author`、および`ms.service`のメタデータフィールドが削除されたことを示しています。この修正は、ドキュメントのシンプルさを向上させ、ユニークな情報にアクセスしやすくすることを目的としています。

文書は、Azure AI Searchを使用してベクターフィールドを含む検索インデックスを作成または更新する手順を説明しています。メタデータを削除することで、よりフォーカスされたコンテンツが提供され、読者が必要な情報に迅速にアクセスできるようになります。

## articles/search/vector-search-how-to-generate-embeddings.md{#item-e98f7b}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Generate embeddings
 titleSuffix: Azure AI Search
 description: Learn how to generate embeddings for downstream indexing into an Azure AI Search index.
-
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-generate-embeddings.md` ドキュメントから`author`、`ms.author`、および`ms.service`のメタデータフィールドが削除されたことを示しています。この修正により、ドキュメントがより明確で簡潔に保たれ、読者が必要な情報に集中できるようになります。

この文書は、Azure AI Searchインデックスへのダウンサンプルインデキシングのために埋め込みを生成する方法を学ぶことに焦点を当てています。メタデータの削除は、情報の提供方法を改善し、ユーザーにとっての利便性を向上させることを目的としています。

## articles/search/vector-search-how-to-index-binary-data.md{#item-b233b9}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Index binary vectors for vector search
 titleSuffix: Azure AI Search
 description: Explains how to configure fields for binary vectors and the vector search configuration for querying the fields.
-
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-index-binary-data.md` ドキュメントから`author`、`ms.author`、および`ms.service`というメタデータフィールドが削除されたことを示しています。この修正により、文書がさらに洗練され、内容に焦点を合わせることが可能になっています。

この文書は、バイナリベクトルをインデックス化する方法及び、フィールドを照会するためのベクトル検索の設定について説明しています。メタデータの削除によって、読者は情報に直接アクセスしやすくなり、内容の理解を深めることができるようになります。

## articles/search/vector-search-how-to-quantization.md{#item-744f48}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Compress vectors using quantization
 titleSuffix: Azure AI Search
 description: Configure built-in scalar or quantization for compressing vectors on disk and in memory.
-
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-quantization.md` ドキュメントから`author`、`ms.author`、および`ms.service`というメタデータフィールドが削除されたことを示しています。この修正により、コンテンツの明確性が向上し、読者が重要な情報に集中できるようになります。

この文書は、ベクトルをディスク上およびメモリ内で圧縮するためのスカラーまたは量子化の設定方法について説明しています。メタデータの削除は、情報の提供をシンプルにし、ユーザーが文書の内容により迅速にアクセスできることを目指しています。

## articles/search/vector-search-how-to-query.md{#item-9bb93c}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Create a Vector Query
 titleSuffix: Azure AI Search
 description: Learn how to build queries for vector search.
-
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-query.md` ドキュメントから`author`、`ms.author`、および`ms.service`というメタデータフィールドが削除されたことを示しています。この修正により、文書の内容がより明瞭になり、読者が必要な情報に集中しやすくなります。

この文書は、ベクトル検索のためのクエリの作成方法について説明しています。メタデータの削除によって、重要な情報に直接アクセスすることが可能となり、ユーザーの体験が向上することが期待されます。

## articles/search/vector-search-how-to-storage-options.md{#item-ee1680}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Eliminate optional vector instances
 titleSuffix: Azure AI Search
 description: In vector search, configure storage to exclude optional copies of vector fields, reducing the storage requirements of vector data.
-
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-storage-options.md` ドキュメントから`author`、`ms.author`、および`ms.service`というメタデータフィールドが削除されたことを示しています。この修正は、文書のコンテンツがよりクリアになり、利用者がフォーカスを維持しやすくなることを目的としています。

この文書は、ベクトル検索においてストレージを構成してオプションのベクトルフィールドのコピーを排除し、ベクトルデータのストレージ要件を削減する方法について説明しています。メタデータの削除により、コンテンツの重要な情報により簡単にアクセスできるようになることが期待され、ユーザーエクスペリエンスの向上も見込まれます。

## articles/search/vector-search-how-to-truncate-dimensions.md{#item-8350a3}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Truncate dimensions
 titleSuffix: Azure AI Search
 description: Truncate dimensions on text-embedding-3 models using Matryoshka Representation Learning (MRL) compression.
-
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-truncate-dimensions.md` ドキュメントから`author`、`ms.author`、および`ms.service`というメタデータフィールドが削除されたことを示しています。この修正により、文書の内容がより集中しやすくなり、利用者が重要な情報を簡単に把握できるようになります。

この文書は、Matryoshka Representation Learning (MRL) 圧縮を使用してテキスト埋め込みモデルの次元を切り捨てる方法について説明しています。メタデータの削除は、ユーザーが技術的な詳細に注目しやすくするためのものであり、読みやすさの向上が期待されます。

## articles/search/vector-search-index-size.md{#item-bb2846}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Vector index limits
 titleSuffix: Azure AI Search
 description: Explanation of the factors affecting the size of a vector index.
-
 author: robertklee
 ms.author: robertlee
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-index-size.md` ドキュメントから`author`、`ms.author`、および`ms.service`というメタデータフィールドが削除されたことを示しています。この編集により、文書の流れがスムーズになり、読者が内容に集中しやすくなることが期待されます。

この文書は、ベクトルインデックスのサイズに影響を与える要因について説明しており、読者がその概念を理解しやすくするための情報を提供しています。メタデータの削除は、必要な情報に焦点を当てるためのものであり、全体的な可読性向上につながります。

## articles/search/vector-search-integrated-vectorization.md{#item-48219d}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Integrated vectorization
 titleSuffix: Azure AI Search
 description: Add a vector embedding step in an Azure AI Search skillset to vectorize content during indexing or queries.
-
 author: heidisteen
 ms.author: heidist
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-integrated-vectorization.md` ドキュメントから`author`、`ms.author`、および`ms.service`というメタデータフィールドが削除されたことを示しています。この修正により、読者は文書の内容により集中しやすくなります。

この文書は、Azure AI Searchのスキルセットにおいて、インデックス作成またはクエリの際にコンテンツをベクトル化するためのベクトル埋め込みステップを追加する方法について説明しています。メタデータの削除は、文書のクリーンさを保ち、必要な技術的情報へと焦点を当てるためのもので、全体的な可読性の向上につながります。

## articles/search/vector-search-overview.md{#item-56e5fa}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Vector search
 titleSuffix: Azure AI Search
 description: Describes concepts, scenarios, and availability of vector capabilities in Azure AI Search.
-
 author: robertklee
 ms.author: robertlee
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-overview.md` ドキュメントから`author`、`ms.author`、および`ms.service`というメタデータフィールドが削除されたことを示しています。この修正により、内容に対する集中が高まり、読者にとっての可読性が向上します。

この文書は、Azure AI Searchにおけるベクトル検索の概念、シナリオ、および機能の可用性について詳細に説明しています。メタデータの削除は、主に文書を明確にし、核心的な情報に焦点を当てる目的があるため、全体の流れをよりスムーズに保つことが期待されます。

## articles/search/vector-search-ranking.md{#item-0764d8}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Vector relevance and ranking
 titleSuffix: Azure AI Search
 description: Explains the concepts behind vector relevance, scoring, including how matches are found in vector space and ranked in search results.
-
 author: yahnoosh
 ms.author: jlembicz
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-search-ranking.md` ドキュメントから`author`、`ms.author`、および`ms.service`というメタデータフィールドが削除されたことを示しています。この修正は、文書をより明確にし、読者が内容に集中できる環境を提供することを目的としています。

この文書は、ベクトル関連性やスコアリングの背後にある概念を説明し、ベクトル空間での一致の見つけ方と検索結果でのランク付け方法について詳細に述べています。メタデータの削除により、技術的な焦点がより強調され、必要な情報が一層明確に提示されることが期待されます。

## articles/search/vector-store.md{#item-db9b8c}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@
 title: Vector store database
 titleSuffix: Azure AI Search
 description: Describes concepts behind vector storage in Azure AI Search.
-
 author: robertklee
 ms.author: robertlee
 ms.service: azure-ai-search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "メタデータの削除"
}
```

### Explanation
この変更は、`articles/search/vector-store.md` ドキュメントから`author`、`ms.author`、および`ms.service`というメタデータフィールドが削除されたことを示しています。この修正は、文書をより簡潔にし、読者が主要な内容に集中できるようにすることを目的としています。

この文書は、Azure AI Searchにおけるベクトルストレージの概念を説明しています。メタデータの削除は、内容の流れを改善し、技術的な情報や説明に焦点を当てることで、読者が理解しやすくなります。これにより、関連情報の直接的な理解が促進されることが期待されます。


