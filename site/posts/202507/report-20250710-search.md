---
date: '2025-07-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2b324c3...MicrosoftDocs:d3417cf
summary: |-
  この一連の変更は、Azure AI Search関連のドキュメントにおける内容の更新と調整を目指しています。新機能として、.NET、REST、Python用の検索スタートガイドが追加され、RBACに関する新しい文書が作成されました。また、視覚的理解向上のために新しい画像も追加されています。一方で、`search-get-started-rbac.md`の内容が大幅に削減されるなどの破壊的変更も存在します。

  さらに、更新周期に関するメタデータの追加により、ドキュメントの見直し頻度が明示され、技術的用語の整合性も向上しました。これらの改訂は、ユーザーがドキュメントをより直感的に参照できるようにし、セキュリティに関する文書の強化により、より安全な利用をサポートします。全体として、開発者はAzure AIの機能を安全かつ効率的に活用するためのガイドラインを得ることができます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2b324c3...MicrosoftDocs:d3417cf){target="_blank"}

<format>
# ハイライト
この一連の変更は、主にAzure AI Search関連のドキュメントにおける内容の更新と調整を目的としたものであり、新機能の追加や既存情報の改善、マークダウン文法の修正が行われています。

## 新機能
- .NET、REST、Python用の新しい検索スタートガイドが追加され、Azure AI SearchおよびAzure OpenAIとの連携方法が詳述されています。
- RBAC（ロールベースのアクセス制御）関連の新しいドキュメントが追加され、Azure AI Searchとのセキュリティ強化を支援しています。
- 各種新しい画像が追加され、視覚的理解が向上しています。

## 破壊的変更
- `search-get-started-rbac.md`の大幅な改訂による内容の削減。

## その他の更新
- 更新周期に関するメタデータの追加により、各ドキュメントの更新頻度が明示されました。
- 用語の整合性と詳細な説明が改善され、特に技術的な用語の表記が統一されています。

# 洞察
今回の変更は、Azure AI Searchの利用者がより明確かつ直感的にドキュメントを参照し、活用できるようにすることを目的としています。新しいスタートガイドの追加は、ユーザーがAzure AI SearchやOpenAIと容易に互換性を持たせられるように設計されており、特に.NETとREST、Pythonを使用したアクセス制御の導入が強化されました。これは、セキュアな接続の確立が重要視されていることを反映しています。

更新周期の追加は、ドキュメントがどれほど頻繁に見直されるかを示し、ユーザーがいつ最新の内容をもたらされるか予測しやすくするための重要なステップです。技術的用語の一貫性を図るための修正は、特に非英語話者にとって情報理解の差を縮小し、アクセシビリティを高める効果が期待されます。

特に、RBACおよびセキュリティに関する文書の充実は、ユーザーの従来のAPIキーからの脱却を促進し、より安全なアイデンティティベースの制御へと移行を助けるもので、クラウドサービス利用におけるセキュリティベストプラクティスの推進に寄与しています。

これにより、開発者はAzure AIのもつ全機能をより、安全かつパフォーマンス良く活用するためのガイドラインを手に入れることができる状況となっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [full-text-rest.md](#item-5d3419) | minor update | マークダウンのリクエストファイル設定の修正 | modified | 1 | 1 | 2 | 
| [search-get-started-rag-dotnet.md](#item-c07a99) | new feature | 新しい .NET 用の検索スタートガイドの追加 | added | 362 | 0 | 362 | 
| [search-get-started-rag-python.md](#item-3927ba) | minor update | Python 用検索スタートガイドのテキスト修正 | modified | 1 | 2 | 3 | 
| [search-get-started-rag-rest.md](#item-aa7f2b) | new feature | REST API 用の検索スタートガイドの追加 | added | 266 | 0 | 266 | 
| [search-get-started-rag-typescript.md](#item-11994e) | minor update | TypeScript 用検索スタートガイドの前提条件追加 | modified | 2 | 0 | 2 | 
| [search-get-started-rbac-python.md](#item-de7760) | new feature | Python 用の RBAC 連携による検索スタートガイドの追加 | added | 95 | 0 | 95 | 
| [search-get-started-rbac-rest.md](#item-fd8ef4) | new feature | REST 用の RBAC 連携による検索スタートガイドの追加 | added | 95 | 0 | 95 | 
| [search-get-started-rbac-setup.md](#item-ad1076) | new feature | RBAC 構成手順の追加 | added | 46 | 0 | 46 | 
| [search-get-started-vector-rest.md](#item-c7d261) | minor update | ベクトル検索の説明の修正 | modified | 2 | 2 | 4 | 
| [semantic-ranker-rest.md](#item-d74861) | minor update | 著者情報の更新 | modified | 1 | 1 | 2 | 
| [keyless-connections.md](#item-3f0d72) | minor update | 更新周期の追加 | modified | 1 | 0 | 1 | 
| [access-control-options.png](#item-bc7170) | new feature | アクセス制御オプション画像の追加 | added | 0 | 0 | 0 | 
| [add-role-assignment.png](#item-fb7936) | new feature | ロール割り当て追加画像の追加 | added | 0 | 0 | 0 | 
| [subscription-and-endpoint.png](#item-b5f993) | new feature | サブスクリプションとエンドポイントの画像の追加 | added | 0 | 0 | 0 | 
| [multimodal-search-overview.md](#item-d82192) | minor update | マルチモーダル検索の更新周期の追加 | modified | 1 | 0 | 1 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | 取得強化生成の更新周期の追加 | modified | 1 | 0 | 1 | 
| [samples-dotnet.md](#item-12f3fa) | minor update | サンプルの更新周期の追加 | modified | 1 | 0 | 1 | 
| [samples-java.md](#item-5992fd) | minor update | サンプルの更新周期の変更 | modified | 1 | 0 | 1 | 
| [samples-javascript.md](#item-82e67e) | minor update | サンプルの更新周期の追加 | modified | 1 | 0 | 1 | 
| [samples-python.md](#item-d2bf09) | minor update | サンプルの更新周期の追加 | modified | 1 | 0 | 1 | 
| [samples-rest.md](#item-198ebc) | minor update | RESTサンプルの更新周期の追加 | modified | 1 | 0 | 1 | 
| [search-agentic-retrieval-concept.md](#item-797a22) | minor update | エージェント検索の概念に関する更新周期の追加 | modified | 1 | 0 | 1 | 
| [search-agentic-retrieval-how-to-create.md](#item-310fbe) | minor update | エージェント検索の作成方法に関する更新周期の追加 | modified | 1 | 0 | 1 | 
| [search-agentic-retrieval-how-to-index.md](#item-a078ea) | minor update | エージェント検索のインデックス作成方法に関する更新周期の追加 | modified | 1 | 0 | 1 | 
| [search-agentic-retrieval-how-to-pipeline.md](#item-1ad1c3) | minor update | エージェント検索のパイプライン作成方法に関する更新周期の追加 | modified | 1 | 0 | 1 | 
| [search-agentic-retrieval-how-to-retrieve.md](#item-5f7fc0) | minor update | エージェント検索の取得方法に関する更新周期の追加 | modified | 1 | 0 | 1 | 
| [search-blob-indexer-role-based-access.md](#item-887e42) | new feature | RBACスコープメタデータを取り込むためのBlobインデクサの追加 | added | 162 | 0 | 162 | 
| [search-create-service-portal.md](#item-f90159) | minor update | サービスポータル作成ガイドの更新周期を追加 | modified | 1 | 0 | 1 | 
| [search-data-sources-gallery.md](#item-18727f) | minor update | データソースギャラリーの更新周期を追加 | modified | 1 | 0 | 1 | 
| [search-document-level-access-overview.md](#item-4bb055) | minor update | ドキュメントレベルのアクセス概要の更新周期を追加 | modified | 1 | 0 | 1 | 
| [search-faq-frequently-asked-questions.yml](#item-eab2ba) | minor update | FAQの更新周期を追加 | modified | 1 | 0 | 1 | 
| [search-features-list.md](#item-d34448) | minor update | 機能リストに更新周期を追加 | modified | 2 | 1 | 3 | 
| [search-get-started-agentic-retrieval.md](#item-4a40f4) | minor update | エージェント取得のクイックスタートに更新周期を追加 | modified | 1 | 0 | 1 | 
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | ポータル画像検索のクイックスタートに更新周期を追加 | modified | 1 | 0 | 1 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | ポータルベクトルインポートのクイックスタートに更新周期を追加 | modified | 1 | 0 | 1 | 
| [search-get-started-portal.md](#item-6d0cb1) | minor update | ポータルのクイックスタートに更新周期を追加 | modified | 1 | 0 | 1 | 
| [search-get-started-rag.md](#item-05ff0e) | minor update | RAGのクイックスタートに新しいゾーンと更新情報を追加 | modified | 17 | 5 | 22 | 
| [search-get-started-rbac.md](#item-9d96c1) | breaking change | RBAC接続のクイックスタートを大幅に改訂 | modified | 15 | 154 | 169 | 
| [search-get-started-semantic.md](#item-2b3902) | minor update | セマンティック検索のドキュメントに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [search-get-started-skillset.md](#item-079744) | minor update | スキルセットのドキュメントに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [search-get-started-text.md](#item-935941) | minor update | テキスト検索のドキュメントに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [search-get-started-vector.md](#item-4984d9) | minor update | ベクトル検索のドキュメントに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [search-how-to-create-search-index.md](#item-c4ff31) | minor update | 検索インデックス作成に関するドキュメントに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [search-how-to-load-search-index.md](#item-a72573) | minor update | 検索インデックス読み込みに関するドキュメントに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [search-howto-indexing-azure-blob-storage.md](#item-dc4668) | minor update | Azure Blob Storage のインデックス作成に関するドキュメントに RBAC スコープのサポートを追加 | modified | 3 | 0 | 3 | 
| [search-indexer-access-control-lists-and-role-based-access.md](#item-67b42f) | minor update | ACL と RBAC メタデータのインジェストに関するドキュメントに更新周期情報を追加 | modified | 2 | 1 | 3 | 
| [search-region-support.md](#item-25b0f1) | minor update | Azure AI Search のドキュメントに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [search-security-overview.md](#item-6b3f1e) | minor update | Azure AI Search のセキュリティ概要ドキュメントに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [search-security-rbac.md](#item-a5d129) | minor update | Azure AI Search のRBACセキュリティドキュメントに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [search-security-trimming-for-azure-search.md](#item-d8ae51) | minor update | Azure Search のセキュリティトリミングドキュメントに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [search-sku-manage-costs.md](#item-6e0122) | minor update | Azure Search のSKU管理費用ドキュメントに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [search-try-for-free.md](#item-36e28d) | minor update | Azure Search 無料試行ドキュメントに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [search-what-is-azure-search.md](#item-93853a) | minor update | Azure Searchとはのドキュメントに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [semantic-how-to-configure.md](#item-7a92a6) | minor update | セマンティック検索の設定方法に更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [semantic-how-to-enable-disable.md](#item-71ac1e) | minor update | セマンティック検索の有効化と無効化に更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [semantic-how-to-enable-scoring-profiles.md](#item-e8d524) | minor update | セマンティックスコアリングプロファイルの有効化に更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [semantic-how-to-query-request.md](#item-85530d) | minor update | セマンティッククエリリクエストに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [semantic-how-to-query-rewrite.md](#item-3e168f) | minor update | セマンティッククエリーリライトに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [semantic-search-overview.md](#item-b7497b) | minor update | セマンティック検索の概要に更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [toc.yml](#item-c4768f) | minor update | 目次に新しいセクションと項目を追加 | modified | 5 | 3 | 8 | 
| [tutorial-adls-gen2-indexer-acls.md](#item-6881a0) | minor update | ADLS Gen2 インデクサ ACLs チュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-create-custom-analyzer.md](#item-ad5520) | minor update | カスタムアナライザー作成チュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-csharp-create-load-index.md](#item-0a6ffd) | minor update | C# インデックス作成と読み込みチュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-csharp-create-mvc-app.md](#item-608a5d) | minor update | C# MVC アプリ作成チュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-csharp-deploy-static-web-app.md](#item-a2300f) | minor update | C# 静的 Web アプリのデプロイチュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-csharp-overview.md](#item-57fa0d) | minor update | C# 概要チュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-csharp-search-query-integration.md](#item-8ad6b5) | minor update | C# 検索クエリ統合チュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-document-extraction-image-verbalization.md](#item-398a90) | minor update | ドキュメント抽出と画像の言語化チュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-document-extraction-multimodal-embeddings.md](#item-a3db59) | minor update | マルチモーダル埋め込みのドキュメント抽出チュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-document-layout-image-verbalization.md](#item-f5de57) | minor update | ドキュメントレイアウトと画像の言語化チュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-document-layout-multimodal-embeddings.md](#item-f67371) | minor update | マルチモーダル埋め込みのドキュメントレイアウトチュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-multiple-data-sources.md](#item-71558f) | minor update | 複数データソースのチュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-optimize-indexing-push-api.md](#item-ef0e96) | minor update | インデクシングプッシュAPIの最適化チュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-rag-build-solution-index-schema.md](#item-9a17ca) | minor update | RAGソリューション構築のインデックススキーマチュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-rag-build-solution-maximize-relevance.md](#item-2fdb09) | minor update | RAGソリューションの関連性最大化チュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-rag-build-solution-minimize-storage.md](#item-088ad8) | minor update | RAGソリューションのストレージ最適化チュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-rag-build-solution-models.md](#item-6796c9) | minor update | RAGソリューションのモデルに関するチュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-rag-build-solution-pipeline.md](#item-25ce01) | minor update | RAGソリューションのパイプラインに関するチュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-rag-build-solution-query.md](#item-93965f) | minor update | RAGソリューションのクエリに関するチュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [tutorial-rag-build-solution.md](#item-c7eca4) | minor update | RAGソリューションに関するチュートリアルに更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [vector-search-filters.md](#item-f47c2b) | minor update | ベクトル検索フィルターに関する記事に更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [vector-search-how-to-assign-narrow-data-types.md](#item-6b81cd) | minor update | ベクトル検索のデータ型割り当てに関する記事に更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [vector-search-how-to-chunk-documents.md](#item-b79133) | minor update | ドキュメントのチャンク化に関する記事に更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [vector-search-how-to-configure-compression-storage.md](#item-c653c3) | minor update | 圧縮ストレージの設定に関する記事に更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [vector-search-how-to-configure-vectorizer.md](#item-30ffd8) | minor update | ベクトライザー設定に関する記事に更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [vector-search-how-to-create-index.md](#item-97c769) | minor update | インデックス作成に関する記事の内容を更新 | modified | 10 | 7 | 17 | 
| [vector-search-how-to-generate-embeddings.md](#item-e98f7b) | minor update | 埋め込み生成に関する記事に更新周期情報を追加 | modified | 1 | 0 | 1 | 
| [vector-search-how-to-index-binary-data.md](#item-b233b9) | minor update | バイナリデータインデックスに関する記事の内容を更新 | modified | 2 | 1 | 3 | 
| [vector-search-how-to-quantization.md](#item-744f48) | minor update | 量子化に関する記事に更新情報と用語の整合性を追加 | modified | 4 | 3 | 7 | 
| [vector-search-how-to-query.md](#item-9bb93c) | minor update | ベクター検索クエリ構築に関する記事に更新周期を追加 | modified | 1 | 0 | 1 | 
| [vector-search-how-to-storage-options.md](#item-ee1680) | minor update | ベクター検索ストレージオプションに関する記事に更新周期と用語の整合性を追加 | modified | 3 | 2 | 5 | 
| [vector-search-how-to-truncate-dimensions.md](#item-8350a3) | minor update | テキスト埋め込みモデルの次元を切り捨てる方法に関する記事に更新周期を追加 | modified | 1 | 0 | 1 | 
| [vector-search-index-size.md](#item-bb2846) | minor update | ベクターインデックスサイズに関する記事に更新周期と用語の整合性を追加 | modified | 3 | 2 | 5 | 
| [vector-search-integrated-vectorization.md](#item-48219d) | minor update | 統合ベクトル化に関する記事に更新周期を追加 | modified | 1 | 0 | 1 | 
| [vector-search-multi-vector-fields.md](#item-9aa482) | minor update | 複数ベクトルフィールドに関する記事に更新周期を追加 | modified | 1 | 0 | 1 | 
| [vector-search-overview.md](#item-56e5fa) | breaking change | ベクトル検索に関する記事の大幅な修正 | modified | 2 | 69 | 71 | 
| [vector-search-ranking.md](#item-0764d8) | minor update | ベクトル検索のランキングに関する記事の更新 | modified | 31 | 21 | 52 | 


# Modified Contents
## articles/search/includes/quickstarts/full-text-rest.md{#item-5d3419}

<details>
<summary>Diff</summary>
````diff
@@ -89,7 +89,7 @@ To set up your request file:
     @token = PUT-YOUR-PERSONAL-IDENTITY-TOKEN-HERE
 
     ### List existing indexes by name
-        GET {{baseUrl}}/indexes?api-version=2024-07-01
+    GET {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
         Authorization: Bearer {{token}}
     ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マークダウンのリクエストファイル設定の修正"
}
```

### Explanation
この変更では、`full-text-rest.md` ファイル内の特定のリクエストファイル設定に関するマークダウンが修正されました。具体的には、HTTPメソッドの記述部分が修正され、GETリクエストに対してHTTPバージョン1.1が明示的に追加されています。この変更は、APIリクエストを適切に行うための明確さを高めることを目的としています。具体的な変更点は、GETリクエストの行が以下のように更新されたことです：

```diff
-        GET {{baseUrl}}/indexes?api-version=2024-07-01
+    GET {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
```

この変更により、利用者がAPI呼び出しを行う際の形式が統一され、理解しやすくなっています。

## articles/search/includes/quickstarts/search-get-started-rag-dotnet.md{#item-c07a99}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,362 @@
+---
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 06/05/2025
+---
+## Prerequisites
+
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+
+- An [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource).
+  - [Choose a region](/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) that supports the chat completion model you want to use (gpt-4o, gpt-4o-mini, or an equivalent model).
+  - [Deploy the chat completion model](/azure/ai-foundry/how-to/deploy-models-openai) in Azure AI Foundry or [use another approach](/azure/ai-services/openai/how-to/working-with-models).
+- An [Azure AI Search resource](../../search-create-service-portal.md).
+  - We recommend using the Basic tier or higher.
+  - [Enable semantic ranking](../../semantic-how-to-enable-disable.md).
+- [Visual Studio Code](https://code.visualstudio.com/download) or [Visual Studio](https://visualstudio.com).
+- [.NET 9.0](https://dotnet.microsoft.com/download) installed.
+
+## Configure access
+
+Requests to the search endpoint must be authenticated and authorized. You can use API keys or roles for this task. Keys are easier to start with, but roles are more secure. This quickstart assumes roles.
+
+You're setting up two clients, so you need permissions on both resources.
+
+Azure AI Search is receiving the query request from your local system. Assign yourself the **Search Index Data Reader** role assignment if the hotels sample index already exists. If it doesn't exist, assign yourself **Search Service Contributor** and **Search Index Data Contributor** roles so that you can create and query the index.
+
+Azure OpenAI is receiving the query and the search results from your local system. Assign yourself the **Cognitive Services OpenAI User** role on Azure OpenAI.
+
+1. Sign in to the [Azure portal](https://portal.azure.com).
+
+1. Configure Azure AI Search for role-based access:
+
+    1. In the Azure portal, find your Azure AI Search service.
+
+    1. On the left menu, select **Settings** > **Keys**, and then select either **Role-based access control** or **Both**.
+
+1. Assign roles:
+
+    1. On the left menu, select **Access control (IAM)**.
+
+    1. On Azure AI Search, select these roles to create, load, and query a search index, and then assign them to your Microsoft Entra ID user identity:
+
+       - **Search Index Data Contributor**
+       - **Search Service Contributor**
+
+    1. On Azure OpenAI, select **Access control (IAM)** to assign this role to yourself on Azure OpenAI:
+
+       - **Cognitive Services OpenAI User**
+
+It can take several minutes for permissions to take effect.
+
+## Create an index
+
+A search index provides grounding data for the chat model. We recommend the hotels-sample-index, which can be created in minutes and runs on any search service tier. This index is created using built-in sample data.
+
+1. In the Azure portal, [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
+
+1. On the **Overview** home page, select [**Import data**](../../search-get-started-portal.md) to start the wizard.
+
+1. On the **Connect to your data** page, select **Samples** from the dropdown list.
+
+1. Choose the **hotels-sample**.
+
+1. Select **Next** through the remaining pages, accepting the default values.
+
+1. Once the index is created, select **Search management** > **Indexes** from the left menu to open the index.
+
+1. Select **Edit JSON**. 
+
+1. Scroll to the end of the index, where you can find placeholders for constructs that can be added to an index.
+
+   ```json
+   "analyzers": [],
+   "tokenizers": [],
+   "tokenFilters": [],
+   "charFilters": [],
+   "normalizers": [],
+   ```
+
+1. On a new line after "normalizers", paste in the following semantic configuration. This example specifies a `"defaultConfiguration"`, which is important to the running of this quickstart.
+
+    ```json
+    "semantic":{
+       "defaultConfiguration":"semantic-config",
+       "configurations":[
+          {
+             "name":"semantic-config",
+             "prioritizedFields":{
+                "titleField":{
+                   "fieldName":"HotelName"
+                },
+                "prioritizedContentFields":[
+                   {
+                      "fieldName":"Description"
+                   }
+                ],
+                "prioritizedKeywordsFields":[
+                   {
+                      "fieldName":"Category"
+                   },
+                   {
+                      "fieldName":"Tags"
+                   }
+                ]
+             }
+          }
+       ]
+    },
+    ```
+
+1. **Save** your changes.
+
+1. Run the following query in [Search Explorer](../../search-explorer.md) to test your index: `complimentary breakfast`.
+
+   Output should look similar to the following example. Results that are returned directly from the search engine consist of fields and their verbatim values, along with metadata like a search score and a semantic ranking score and caption if you use semantic ranker. We used a [select statement](../../search-query-odata-select.md) to return just the HotelName, Description, and Tags fields.
+
+   ```
+   {
+   "@odata.count": 18,
+   "@search.answers": [],
+   "value": [
+      {
+         "@search.score": 2.2896252,
+         "@search.rerankerScore": 2.506816864013672,
+         "@search.captions": [
+         {
+            "text": "Head Wind Resort. Suite. coffee in lobby\r\nfree wifi\r\nview. The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a **complimentary continental breakfast** in the lobby, and free Wi-Fi throughout the hotel..",
+            "highlights": ""
+         }
+         ],
+         "HotelName": "Head Wind Resort",
+         "Description": "The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a complimentary continental breakfast in the lobby, and free Wi-Fi throughout the hotel.",
+         "Tags": [
+         "coffee in lobby",
+         "free wifi",
+         "view"
+         ]
+      },
+      {
+         "@search.score": 2.2158256,
+         "@search.rerankerScore": 2.288334846496582,
+         "@search.captions": [
+         {
+            "text": "Swan Bird Lake Inn. Budget. continental breakfast\r\nfree wifi\r\n24-hour front desk service. We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins..",
+            "highlights": ""
+         }
+         ],
+         "HotelName": "Swan Bird Lake Inn",
+         "Description": "We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins.",
+         "Tags": [
+         "continental breakfast",
+         "free wifi",
+         "24-hour front desk service"
+         ]
+      },
+      {
+         "@search.score": 0.92481667,
+         "@search.rerankerScore": 2.221315860748291,
+         "@search.captions": [
+         {
+            "text": "White Mountain Lodge & Suites. Resort and Spa. continental breakfast\r\npool\r\nrestaurant. Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings..",
+            "highlights": ""
+         }
+         ],
+         "HotelName": "White Mountain Lodge & Suites",
+         "Description": "Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings.",
+         "Tags": [
+         "continental breakfast",
+         "pool",
+         "restaurant"
+         ]
+      },
+      . . .
+   ]}
+   ```
+
+## Get service endpoints
+
+In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints so that you can provide them as variables in your code.
+
+1. Sign in to the [Azure portal](https://portal.azure.com).
+
+1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
+
+1. On the **Overview** home page, copy the URL. An example endpoint might look like `https://example.search.windows.net`. 
+
+1. [Find your Azure OpenAI service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.CognitiveServices%2Faccounts).
+
+1. On the **Overview** home page, select the link to view the endpoints. Copy the URL. An example endpoint might look like `https://example.openai.azure.com/`.
+
+## Sign in to Azure
+
+You're using Microsoft Entra ID and role assignments for the connection. Make sure you're logged in to the same tenant and subscription as Azure AI Search and Azure OpenAI. You can use the Azure CLI on the command line to show current properties, change properties, and to sign in. For more information, see [Connect without keys](../../search-get-started-rbac.md). 
+
+Run each of the following commands in sequence.
+
+```azure-cli
+az account show
+
+az account set --subscription <PUT YOUR SUBSCRIPTION ID HERE>
+
+az login --tenant <PUT YOUR TENANT ID HERE>
+```
+
+You should now be logged in to Azure from your local device.
+
+## Set up the .NET app
+
+To follow along with the steps ahead, you can either clone the completed sample app from GitHub, or create the app yourself.
+
+### Clone the sample app
+
+To access the completed sample app for this article: 
+
+1. Clone the [azure-search-dotnet-samples](https://github.com/Azure-Samples/azure-search-dotnet-samples) repo from GitHub.
+
+    ```bash
+    git clone https://github.com/Azure-Samples/azure-search-dotnet-samples
+    ```
+
+1. Navigate into the `quickstart-rag` folder.
+1. Open the `quickstart-rag` folder in Visual Studio Code or open the solution file using Visual Studio.
+
+### Create the sample app
+
+Complete the following steps to create a .NET console app to connect to an AI model.
+
+1. In an empty directory on your computer, use the `dotnet new` command to create a new console app:
+
+    ```dotnetcli
+    dotnet new console -o AISearchRag
+    ```
+
+1. Change directory into the app folder:
+
+    ```dotnetcli
+    cd AISearchRag
+    ```
+
+1. Install the required packages:
+
+    ```bash
+    dotnet add package Azure.AI.OpenAI
+    dotnet add package Azure.Identity
+    dotnet add package Azure.Search.Documents
+    ```
+
+1. Open the app in Visual Studio Code (or your editor of choice).
+
+    ```bash
+    code .
+    ```
+
+## Set up the query and chat thread
+
+The following example demonstrates how to set up a minimal RAG scenario using Azure AI Search to provide an OpenAI model with contextual resources to improve the generated responses.
+
+1. In the `minimal-query` project of the sample repo, open the `Program.cs` file to view the first example. If you created the project yourself, add the following code to connect to and query the Azure AI Search and Azure OpenAI services.
+
+    > [!NOTE]
+    > Make sure to replace the placeholders for the Azure OpenAI endpoint and model name, as well as the Azure AI Search endpoint and index name.
+    
+    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-rag/minimal-query/Program.cs" :::
+    
+    The preceding code accomplishes the following:
+    
+    - Searches an Azure Search index for hotels matching a user query about complimentary breakfast, retrieving hotel name, description, and tags.
+    - Formats the search results into a structured list to serve as contextual sources for the generative AI model.
+    - Constructs a prompt instructing the Azure OpenAI model to answer using only the provided sources.
+    - Sends the prompt to the AI model and streams the generated response.
+    - Outputs the AI’s response to the console, displaying both the role and content as it streams.
+
+1. Run the project to initiate a basic RAG scenario. The output from Azure OpenAI consists of recommendations for several hotels, such as the following example:
+    
+    ```output
+    Sure! Here are a few hotels that offer complimentary breakfast:
+    
+    - **Head Wind Resort**
+    - Complimentary continental breakfast in the lobby
+    - Free Wi-Fi throughout the hotel
+    
+    - **Double Sanctuary Resort**
+    - Continental breakfast included
+    
+    - **White Mountain Lodge & Suites**
+    - Continental breakfast available
+    
+    - **Swan Bird Lake Inn**
+    - Continental-style breakfast each morning with a variety of food and drinks 
+       such as caramel cinnamon rolls, coffee, orange juice, milk, cereal, 
+       instant oatmeal, bagels, and muffins
+    ```
+
+To experiment further, change the query and rerun the last step to better understand how the model works with the grounding data. You can also modify the prompt to change the tone or structure of the output.
+
+### Troubleshooting
+
+You might receive any of the following errors while testing:
+
+- **Forbidden**: Check Azure AI Search configuration to make sure role-based access is enabled.
+- **Authorization failed**: Wait a few minutes and try again. It can take several minutes for role assignments to become operational.
+- **Resource not found**: Check the resource URIs and make sure the API version on the chat model is valid.
+
+## Send a complex RAG query
+
+Azure AI Search supports [complex types](../../search-howto-complex-data-types.md) for nested JSON structures. In the hotels-sample-index, `Address` is an example of a complex type, consisting of `Address.StreetAddress`, `Address.City`, `Address.StateProvince`, `Address.PostalCode`, and `Address.Country`. The index also has complex collection of `Rooms` for each hotel. If your index has complex types, your query can provide those fields if you first convert the search results output to JSON, and then pass the JSON to the chat model.
+
+1. In the `complex-query` project of the sample repo, open the `Program.cs` file. If you created the project yourself, replace your code with the following:
+
+    :::code language="csharp" source="~/azure-search-dotnet-samples/quickstart-rag/complex-query/Program.cs" :::
+
+2. Run the project to initiate a basic RAG scenario. The output from Azure OpenAI consists of recommendations for several hotels, such as the following example:
+
+    ```output
+    1. **Double Sanctuary Resort**
+       - **Description**: 5-star luxury hotel with the biggest rooms in the city. Recognized as the #1 hotel in the area by Traveler magazine. Features include free WiFi, flexible check-in/out, a fitness center, and in-room espresso.
+       - **Address**: 2211 Elliott Ave, Seattle, WA, 98121, USA
+       - **Tags**: view, pool, restaurant, bar, continental breakfast
+       - **Room Rate for 4 People**: 
+         - Suite, 2 Queen Beds: $254.99 per night
+    
+    2. **Starlight Suites**
+       - **Description**: Spacious all-suite hotel with complimentary airport shuttle and WiFi. Facilities include an indoor/outdoor pool, fitness center, and Florida Green certification. Complimentary coffee and HDTV are also available.
+       - **Address**: 19575 Biscayne Blvd, Aventura, FL, 33180, USA
+       - **Tags**: pool, coffee in lobby, free wifi
+       - **Room Rate for 4 People**:
+         - Suite, 2 Queen Beds (Cityside): $231.99 per night
+         - Deluxe Room, 2 Queen Beds (Waterfront View): $148.99 per night
+    
+    3. **Good Business Hotel**
+       - **Description**: Located one mile from the airport with free WiFi, an outdoor pool, and a complimentary airport shuttle. Close proximity to Lake Lanier and downtown. The business center includes printers, a copy machine, fax, and a work area.
+       - **Address**: 4400 Ashford Dunwoody Rd NE, Atlanta, GA, 30346, USA
+       - **Tags**: pool, continental breakfast, free parking
+       - **Room Rate for 4 People**:
+         - Budget Room, 2 Queen Beds (Amenities): $60.99 per night
+         - Deluxe Room, 2 Queen Beds (Amenities): $139.99 per night
+    ```
+
+## Troubleshooting
+
+If you see output messages while debugging related to `ManagedIdentityCredential` and token acquisition failures, it could be that you have multiple tenants, and your Azure sign-in is using a tenant that doesn't have your search service. To get your tenant ID, search the Azure portal for "tenant properties" or run `az login tenant list`.
+
+Once you have your tenant ID, run `az login --tenant <YOUR-TENANT-ID>` at a command prompt, and then rerun the script.
+
+You can also log errors in your code by creating an instance of `ILogger`:
+
+```csharp
+using var loggerFactory = LoggerFactory.Create(builder =>
+{
+   builder.AddConsole();
+});
+ILogger logger = loggerFactory.CreateLogger<Program>();
+```
+
+## Clean up
+
+When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
+
+You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい .NET 用の検索スタートガイドの追加"
}
```

### Explanation
この変更では、`search-get-started-rag-dotnet.md` という新しいファイルが追加され、Azure AI Search と Azure OpenAI を使用して .NET アプリケーションの初期設定を行うための手順が詳細に説明されています。このドキュメントには、事前準備、アクセスの構成、インデックスの作成、API コールの設定、およびサンプルアプリケーションの構築方法が含まれています。

新しいガイドは、ユーザーが Azure サービスを利用して、検索クエリとチャットスレッドを統合する基本的な RAG（Retrieval-Augmented Generation）シナリオを構築するためのステップバイステップの手順を提供します。具体的には、Azure ポータルにサインインし、必要なリソースを設定し、サンプルアプリを作成してそれを Azure AI Search と Azure OpenAI に接続する方法が詳述されています。

この新機能の追加により、.NET 開発者は Azure の AI 機能を活用して効果的な情報検索システムを簡単に実装できるようになります。

## articles/search/includes/quickstarts/search-get-started-rag-python.md{#item-3927ba}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,6 @@ ms.date: 06/05/2025
   - [Enable semantic ranking](../../semantic-how-to-enable-disable.md).
 - [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and the [Jupyter package](https://pypi.org/project/jupyter/). For more information, see [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python).
 
-
 ## Download file
 
 [Download a Jupyter notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-RAG) from GitHub to send the requests in this quickstart. For more information, see [Downloading files from GitHub](https://docs.github.com/get-started/start-your-journey/downloading-files-from-github).
@@ -58,7 +57,7 @@ Azure OpenAI is receiving the query and the search results from your local syste
 
 It can take several minutes for permissions to take effect.
 
-## Create an index
+## Update the hotels-sample-index
 
 A search index provides grounding data for the chat model. We recommend the hotels-sample-index, which can be created in minutes and runs on any search service tier. This index is created using built-in sample data.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python 用検索スタートガイドのテキスト修正"
}
```

### Explanation
この変更では、`search-get-started-rag-python.md` ファイルでいくつかの小さな修正が行われています。主な変更点は、README 内のテキストのいくつかが更新されたことです。その中でも、マークダウンの見出しが「Create an index」から「Update the hotels-sample-index」へと変更されている点が特に重要です。

また、Visual Studio Code に関連する説明の一部が削除され、さらに Jupyter ノートブックをダウンロードするためのセクションも更新されました。このような微修正は、ユーザーが適切なリソースを見つけやすくし、プロジェクトにおける手順をより明確にするために行われています。

これらの変更は、特に Python 開発者が Azure サービスを利用した検索機能を効果的に実装するための手助けを目的としています。

## articles/search/includes/quickstarts/search-get-started-rag-rest.md{#item-aa7f2b}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,266 @@
+---
+manager: nitinme
+author: heidisteen
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 07/08/2025
+---
+
+## Prerequisites
+
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+
+- An [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource).
+  - [Choose a region](/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) that supports the chat completion model you want to use (gpt-4o, gpt-4o-mini, or an equivalent model).
+  - [Deploy the chat completion model](/azure/ai-foundry/how-to/deploy-models-openai) in Azure AI Foundry or [use another approach](/azure/ai-services/openai/how-to/working-with-models).
+- An [Azure AI Search resource](../../search-create-service-portal.md).
+  - We recommend using the Basic tier or higher.
+  - [Enable semantic ranking](../../semantic-how-to-enable-disable.md).
+
+- A [new or existing index](../../search-how-to-create-search-index.md) with descriptive or verbose text fields, attributed as retrievable in your index. This quickstart assumes the [hotels-sample-index](../../search-get-started-portal.md).
+
+- The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
+
+- [Visual Studio Code](https://code.visualstudio.com/download) with the [REST client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) .
+
+## Download file
+
+[Download a .rest file](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-RAG) from GitHub to send the requests in this quickstart. For more information, see [Downloading files from GitHub](https://docs.github.com/get-started/start-your-journey/downloading-files-from-github).
+
+You can also start a new file on your local system and create requests manually by using the instructions in this article.
+
+## Configure access
+
+Requests to the search endpoint must be authenticated and authorized. You can use [API keys](../../search-security-api-keys.md) or roles for this task. Keys are easier to start with, but roles are more secure. This quickstart assumes roles.
+
+You're setting up two clients, so you need permissions on both resources.
+
+Azure AI Search is receiving the query request from your local system. Assign yourself the **Search Index Data Reader** role assignment if the hotels sample index already exists. If it doesn't exist, assign yourself **Search Service Contributor** and **Search Index Data Contributor** roles so that you can create and query the index.
+
+Azure OpenAI is receiving the query and the search results from your local system. Assign yourself the **Cognitive Services OpenAI User** role on Azure OpenAI.
+
+1. Sign in to the [Azure portal](https://portal.azure.com).
+
+1. Configure Azure AI Search for role-based access:
+
+    1. In the Azure portal, find your Azure AI Search service.
+
+    1. On the left menu, select **Settings** > **Keys**, and then select either **Role-based access control** or **Both**.
+
+1. Assign roles:
+
+    1. On the left menu, select **Access control (IAM)**.
+
+    1. On Azure AI Search, select these roles to create, load, and query a search index, and then assign them to your Microsoft Entra ID user identity:
+
+       - **Search Index Data Contributor**
+       - **Search Service Contributor**
+
+    1. On Azure OpenAI, select **Access control (IAM)** to assign this role to yourself on Azure OpenAI:
+
+       - **Cognitive Services OpenAI User**
+
+It can take several minutes for permissions to take effect.
+
+## Get service endpoints and tokens
+
+In the remaining sections, you set up API calls to Azure OpenAI and Azure AI Search. Get the service endpoints and tokens so that you can provide them as variables in your code.
+
+1. Sign in to the [Azure portal](https://portal.azure.com).
+
+1. [Find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
+
+1. On the **Overview** home page, copy the URL. An example endpoint might look like `https://example.search.windows.net`. 
+
+1. [Find your Azure OpenAI service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.CognitiveServices%2Faccounts).
+
+1. On the **Overview** home page, select the link to view the endpoints. Copy the URL. An example endpoint might look like `https://example.openai.azure.com/`.
+
+1. Get personal access tokens from the Azure CLI on a command prompt. Here are the commands for each resource:
+
+   - `az account get-access-token --resource https://search.azure.com --query "accessToken" -o tsv`
+   - `az account get-access-token --resource https://cognitiveservices.azure.com --query "accessToken" -o tsv`
+
+## Set up the client
+
+In this quickstart, you use a REST client and the [Azure AI Search REST APIs](/rest/api/searchservice) to implement the RAG pattern.
+
+We recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for this quickstart.
+
+> [!TIP]
+> You can [download the source code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-rag) to start with a finished project or follow these steps to create your own. 
+
+1. Start Visual Studio Code and open the [quickstart-rag.rest](https://github.com/Azure-Samples/azure-search-rest-samples/blob/main/Quickstart-rag/quickstart-rag.rest) file or create a new file.
+
+1. At the top, set environment variables for your search service, authorization, and index name.
+
+   - For @searchUrl, paste in the search endpoint.
+   - For @aoaiUrl, paste in the Azure OpenAI endpoint.
+   - For @searchAccessToken, paste in the access token scoped to `https://search.azure.com`.
+   - For @aoaiAccessToken, paste in the access token scoped to `https://cognitiveservices.azure.com`.
+
+1. To test the connection, send your first request.
+
+   ```http
+   ### List existing indexes by name (verify the connection)
+    GET  {{searchUrl}}/indexes?api-version=2025-05-01-preview&$select=name  HTTP/1.1
+    Authorization: Bearer {{personalAccessToken}}
+   ```
+
+1. Select **Sent request**.
+
+   :::image type="content" source="../../media/search-get-started-semantic/visual-studio-code-send-request.png" alt-text="Screenshot of the REST client send request link.":::
+
+1. Output for this GET request should be a list of indexes. You should see the **hotels-sample-index** among them.
+
+## Set up the query and chat thread
+
+This section uses Visual Studio Code and REST to call the chat completion APIs on Azure OpenAI.
+
+1. Set up a query request on the phrase *"Can you recommend a few hotels with complimentary breakfast?"*. This query uses semantic ranking to return relevant matches, even if the verbatim text isn't an exact match. Results are held in the **searchRequest** variable for reuse on the next request.
+
+   ```http
+   # @name searchRequest
+    POST {{searchUrl}}/indexes/{{index-name}}/docs/search?api-version={{api-version}} HTTP/1.1
+    Content-Type: application/json
+    Authorization: Bearer {{searchAccessToken}}
+    
+    {
+      "search": "Can you recommend a few hotels with complimentary breakfast?",
+      "queryType": "semantic",
+      "semanticConfiguration": "semantic-config",
+      "select": "Description,HotelName,Tags",
+      "top": 5
+    }
+    
+    ### 3 - Use search results in Azure OpenAI call to a chat completion model
+    POST {{aoaiUrl}}/openai/deployments/{{aoaiGptDeployment}}/chat/completions?api-version=2024-08-01-preview HTTP/1.1
+    Content-Type: application/json
+    Authorization: Bearer {{aoaiAccessToken}}
+    
+    {
+      "messages": [
+        {
+          "role": "system", 
+          "content": "You recommend hotels based on activities and amenities. Answer the query using only the search result. Answer in a friendly and concise manner. Answer ONLY with the facts provided. If there isn't enough information below, say you don't know."
+        },
+        {
+          "role": "user",
+          "content": "Based on the hotel search results, can you recommend hotels with breakfast? Here are all the hotels I found:\n\nHotel 1: {{searchRequest.response.body.value[0].HotelName}}\nDescription: {{searchRequest.response.body.value[0].Description}}\n\nHotel 2: {{searchRequest.response.body.value[1].HotelName}}\nDescription: {{searchRequest.response.body.value[1].Description}}\n\nHotel 3: {{searchRequest.response.body.value[2].HotelName}}\nDescription: {{searchRequest.response.body.value[2].Description}}\n\nHotel 4: {{searchRequest.response.body.value[3].HotelName}}\nDescription: {{searchRequest.response.body.value[3].Description}}\n\nHotel 5: {{searchRequest.response.body.value[4].HotelName}}\nDescription: {{searchRequest.response.body.value[4].Description}}\n\nPlease recommend which hotels offer breakfast based on their descriptions."
+        }
+      ],
+      "max_tokens": 1000,
+      "temperature": 0.7
+    }`
+    ```
+
+1. **Send** the request.
+
+1. Output should look similar to the following example:
+
+   ```json
+      "value": [
+        {
+          "@search.score": 3.9269178,
+          "@search.rerankerScore": 2.380699872970581,
+          "HotelName": "Head Wind Resort",
+          "Description": "The best of old town hospitality combined with views of the river and cool breezes off the prairie. Our penthouse suites offer views for miles and the rooftop plaza is open to all guests from sunset to 10 p.m. Enjoy a complimentary continental breakfast in the lobby, and free Wi-Fi throughout the hotel.",
+          "Tags": [
+            "coffee in lobby",
+            "free wifi",
+            "view"
+          ]
+        },
+        {
+          "@search.score": 1.5450059,
+          "@search.rerankerScore": 2.1258809566497803,
+          "HotelName": "Thunderbird Motel",
+          "Description": "Book Now & Save. Clean, Comfortable rooms at the lowest price. Enjoy complimentary coffee and tea in common areas.",
+          "Tags": [
+            "coffee in lobby",
+            "free parking",
+            "free wifi"
+          ]
+        },
+        {
+          "@search.score": 2.2158256,
+          "@search.rerankerScore": 2.121671438217163,
+          "HotelName": "Swan Bird Lake Inn",
+          "Description": "We serve a continental-style breakfast each morning, featuring a variety of food and drinks. Our locally made, oh-so-soft, caramel cinnamon rolls are a favorite with our guests. Other breakfast items include coffee, orange juice, milk, cereal, instant oatmeal, bagels, and muffins.",
+          "Tags": [
+            "continental breakfast",
+            "free wifi",
+            "24-hour front desk service"
+          ]
+        },
+        {
+          "@search.score": 0.6395861,
+          "@search.rerankerScore": 2.116753339767456,
+          "HotelName": "Waterfront Scottish Inn",
+          "Description": "Newly Redesigned Rooms & airport shuttle. Minutes from the airport, enjoy lakeside amenities, a resort-style pool & stylish new guestrooms with Internet TVs.",
+          "Tags": [
+            "24-hour front desk service",
+            "continental breakfast",
+            "free wifi"
+          ]
+        },
+        {
+          "@search.score": 4.885111,
+          "@search.rerankerScore": 2.0008862018585205,
+          "HotelName": "Double Sanctuary Resort",
+          "Description": "5 star Luxury Hotel - Biggest Rooms in the city. #1 Hotel in the area listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso in room.",
+          "Tags": [
+            "view",
+            "pool",
+            "restaurant",
+            "bar",
+            "continental breakfast"
+          ]
+        }
+      ]
+    ```
+
+1. Set up a conversation turn with a chat completion model. This request includes a prompt that provides instructions for the response. The `max_tokens` value is large enough to accommodate the search results from the previous query.
+
+   ```http
+    POST {{aoaiUrl}}/openai/deployments/{{aoaiGptDeployment}}/chat/completions?api-version=2024-08-01-preview HTTP/1.1
+    Content-Type: application/json
+    Authorization: Bearer {{aoaiAccessToken}}
+    
+    {
+    "messages": [
+    {
+      "role": "system", 
+      "content": "You  are a friendly assistant that recommends hotels based on activities and amenities. Answer the query using only the search result. Answer in a friendly and concise manner. Answer ONLY with the facts provided. If there isn't enough information below, say you don't know."
+        },
+    {
+      "role": "user",
+      "content": "Based on the hotel search results, can you recommend hotels with breakfast? Here are all the hotels I found:\n\nHotel 1: {{searchRequest.response.body.value[0].HotelName}}\nDescription: {{searchRequest.response.body.value[0].Description}}\n\nHotel 2: {{searchRequest.response.body.value[1].HotelName}}\nDescription: {{searchRequest.response.body.value[1].Description}}\n\nHotel 3: {{searchRequest.response.body.value[2].HotelName}}\nDescription: {{searchRequest.response.body.value[2].Description}}\n\nHotel 4: {{searchRequest.response.body.value[3].HotelName}}\nDescription: {{searchRequest.response.body.value[3].Description}}\n\nHotel 5: {{searchRequest.response.body.value[4].HotelName}}\nDescription: {{searchRequest.response.body.value[4].Description}}\n\nPlease recommend which hotels offer breakfast based on their descriptions."
+    }
+    ],
+    "max_tokens": 1000,
+    "temperature": 0.7
+    }
+    ```
+
+1. **Send** the request.
+
+1. Output should be an HTTP 200 Success status message. Included in the output is content that answers the question:
+
+   ```json
+    "message": {
+      "annotations": [],
+      "content": "I recommend the following hotels that offer breakfast:\n\n1. **Head Wind Resort** - Offers a complimentary continental breakfast in the lobby.\n2. **Swan Bird Lake Inn** - Serves a continental-style breakfast each morning, including a variety of food and drinks. \n\nEnjoy your stay!",
+      "refusal": null,
+      "role": "assistant"
+    }
+    ```
+
+Notice that the output is missing several hotels that mention breakfast in the Tags field. The Tags field is an array, and including this field breaks the JSON structure in the results. Because there are no string conversion capabilities in the REST client, extra code for manually converting the JSON to a string is required if arrays are to be included. We omit this step for this quickstart.
+
+## Clean up
+
+When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
+
+You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "REST API 用の検索スタートガイドの追加"
}
```

### Explanation
この変更により、`search-get-started-rag-rest.md` という新しいファイルが追加され、Azure AI Search と Azure OpenAI を使用して REST API を介した RAG（Retrieval-Augmented Generation）パターンの基本的な実装方法が説明されています。このドキュメントには、必要な前提条件、アクセスの設定、サービスエンドポイントの取得、クライアントのセットアップ、クエリの実行方法、レスポンスの処理方法が詳細に記載されています。

ガイドは、Azure 環境における各種 API 呼び出しの手順を示すサンプルリクエストを含み、特に Visual Studio Code を使用する際の設定や操作方法に重点が置かれています。また、クエリを投げる際の構成や、Azure OpenAI に対して適切なレスポンスを引き出すための手法も紹介されており、ユーザーが効率的かつ効果的に Azure サービスを活用できるように設計されています。

この新しいドキュメントの追加により、REST API を使用して Azure の AI 機能を利用したアプリケーションを構築するための指針が提供され、開発者はより簡単にこの技術を活用できるようになります。

## articles/search/includes/quickstarts/search-get-started-rag-typescript.md{#item-11994e}

<details>
<summary>Diff</summary>
````diff
@@ -10,6 +10,8 @@ ms.date: 06/05/2025
 
 - An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
+- An [Azure AI Search service](../../search-create-service-portal.md), any tier and region.
+
 - An [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource).
   - [Choose a region](/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) that supports the chat completion model you want to use (gpt-4o, gpt-4o-mini, or an equivalent model).
   - [Deploy the chat completion model](/azure/ai-foundry/how-to/deploy-models-openai) in Azure AI Foundry or [use another approach](/azure/ai-services/openai/how-to/working-with-models).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScript 用検索スタートガイドの前提条件追加"
}
```

### Explanation
この変更は、`search-get-started-rag-typescript.md` ファイルにおける前提条件セクションの更新です。具体的には、Azure AI Search サービスを利用する必要があることが明記され、「任意のティアとリージョン」との説明が追加されました。これにより、ユーザーは Azure AI Search のサブスクリプションを作成する際に、特にサービスの制限を気にせずに利用できることを理解できます。

この更新は、TypeScript を使用して Azure サービスを活用しようとしている開発者にとって、設定を行う上での重要な指針となります。前提条件の明確化により、タスクを進める際のハードルが低くなり、ユーザーが必要なリソースを容易に取得できるようになります。

## articles/search/includes/quickstarts/search-get-started-rbac-python.md{#item-de7760}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,95 @@
+---
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 07/09/2025
+---
+
+In this quickstart, you use role-based access control (RBAC) and Microsoft Entra ID to establish a keyless connection to your Azure AI Search service. You then use Python in Visual Studio Code to interact with your service.
+
+Keyless connections provide enhanced security through granular permissions and identity-based authentication. We don't recommend hard-coded API keys, but if you prefer them, see [Connect to Azure AI Search using keys](../../search-security-api-keys.md).
+
+<!-- This quickstart is a prerequisite for other quickstarts that use Microsoft Entra ID with role assignments. -->
+
+## Prerequisites
+
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+
++ An [Azure AI Search service](../../search-create-service-portal.md) in any region or tier.
+
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
+
++ [Visual Studio Code](https://code.visualstudio.com/) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter package](https://jupyter.org/install).
+
+[!INCLUDE [Setup](./search-get-started-rbac-setup.md)]
+
+## Sign in to Azure
+
+Before you connect to your Azure AI Search service, use the Azure CLI to sign in to the subscription that contains your service. This step establishes your Microsoft Entra identity, which `DefaultAzureCredential` uses to authenticate requests in the next section.
+
+To sign in:
+
+1. On your local system, open a command-line tool.
+
+1. Sign in to Azure. If you have multiple subscriptions, select the one whose ID you obtained in [Get service information](#get-service-information).
+
+   ```azurecli
+   az login
+   ```
+
+## Connect to Azure AI Search
+
+> [!NOTE]
+> This section illustrates the basic Python pattern for keyless connections. For comprehensive guidance, see a specific quickstart or tutorial, such as [Quickstart: Run agentic retrieval in Azure AI Search](../../search-get-started-agentic-retrieval.md).
+
+You can use Python notebooks in Visual Studio Code to send requests to your Azure AI Search service. For request authentication, use the `DefaultAzureCredential` class from the Azure Identity library.
+
+To connect using Python:
+
+1. On your local system, open Visual Studio Code.
+
+1. Create a `.ipynb` file.
+
+1. Create a code cell to install the `azure-identity` and `azure-search-documents` libraries.
+
+   ```python
+   pip install azure-identity azure-search-documents
+   ```
+
+1. Create another code cell to authenticate and connect to your search service.
+
+   ```python
+   from azure.identity import DefaultAzureCredential
+   from azure.search.documents.indexes import SearchIndexClient
+    
+   service_endpoint = "PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE"
+   credential = DefaultAzureCredential()
+   client = SearchIndexClient(endpoint=service_endpoint, credential=credential)
+    
+   # List existing indexes
+   indexes = client.list_indexes()
+    
+   for index in indexes:
+      index_dict = index.as_dict()
+      print(json.dumps(index_dict, indent=2))
+   ```
+
+1. Set `service_endpoint` to the value you obtained in [Get service information](#get-service-information).
+
+1. Select **Run All** to run both code cells.
+
+   The output should list the existing indexes (if any) on your search service, indicating a successful connection.
+
+### Troubleshoot 401 errors
+
+If you encounter a 401 error, follow these troubleshooting steps:
+
++ Revisit [Configure role-based access](#configure-role-based-access). Your search service must have **Role-based access control** or **Both** enabled. Policies at the subscription or resource group level might also override your role assignments.
+
++ Revisit [Sign in to Azure](#sign-in-to-azure). You must sign in to the subscription that contains your search service.
+
++ Make sure your endpoint variable has surrounding quotes.
+
++ If all else fails, restart your device to remove cached tokens and then repeat the steps in this quickstart, starting with [Sign in to Azure](#sign-in-to-azure).
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Python 用の RBAC 連携による検索スタートガイドの追加"
}
```

### Explanation
この変更は、`search-get-started-rbac-python.md` という新しいファイルの追加を示しています。このクイックスタートでは、ロールベースのアクセス制御（RBAC）を利用し、Microsoft Entra ID を通じて Azure AI Search サービスへのキーレス接続を確立する方法が説明されています。ユーザーは Python を使用して Visual Studio Code 内でサービスと対話することができます。

新たに追加されたセクションでは、キーレス接続の利点として、詳細な権限設定とアイデンティティに基づく認証が挙げられており、従来のハードコードされた API キーの使用は推奨されていません。また、このドキュメントでは、Azure CLI を使用したサインイン手順、Python コードを使用した接続方法や、エラートラブルシューティングの手順が含まれています。

このクイックスタートは、他のクイックスタートが Microsoft Entra ID とロール割り当てを使用する前提条件として位置付けられており、Azure AI Search と Python の連携を学ぶ上での重要なリソースとなります。Python ノートブックを使用した実際のコード例も含まれており、ユーザーがスムーズに設定を行い、機能を利用できるように設計されています。

## articles/search/includes/quickstarts/search-get-started-rbac-rest.md{#item-fd8ef4}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,95 @@
+---
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 07/09/2025
+---
+
+In this quickstart, you use role-based access control (RBAC) and Microsoft Entra ID to establish a keyless connection to your Azure AI Search service. You then use REST in Visual Studio Code to interact with your service.
+
+Keyless connections provide enhanced security through granular permissions and identity-based authentication. We don't recommend hard-coded API keys, but if you prefer them, see [Connect to Azure AI Search using keys](../../search-security-api-keys.md).
+
+<!-- This quickstart is a prerequisite for other quickstarts that use Microsoft Entra ID with role assignments. -->
+
+## Prerequisites
+
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+
++ An [Azure AI Search service](../../search-create-service-portal.md) in any region or tier.
+
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
+
++ [Visual Studio Code](https://code.visualstudio.com/) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
+
+[!INCLUDE [Setup](./search-get-started-rbac-setup.md)]
+
+## Get token
+
+Before you connect to your Azure AI Search service, use the Azure CLI to sign in to the subscription that contains your service and generate a Microsoft Entra ID token. You use this token to authenticate requests in the next section.
+
+To get your token:
+
+1. On your local system, open a command-line tool.
+
+1. Sign in to Azure. If you have multiple subscriptions, select the one whose ID you obtained in [Get service information](#get-service-information).
+
+   ```azurecli
+   az login
+   ```
+
+1. Generate an access token.
+
+   ```azurecli
+   az account get-access-token --scope https://search.azure.com/.default --query accessToken --output tsv
+   ```
+
+1. Make a note of the token output.
+
+## Connect to Azure AI Search
+
+> [!NOTE]
+> This section illustrates the basic REST pattern for keyless connections. For comprehensive guidance, see a specific quickstart or tutorial, such as [Quickstart: Run agentic retrieval in Azure AI Search](../../search-get-started-agentic-retrieval.md).
+
+You can use the REST Client extension in Visual Studio Code to send requests to your Azure AI Search service. For request authentication, include an `Authorization` header with the Microsoft Entra ID token you previously generated.
+
+To connect using REST:
+
+1. On your local system, open Visual Studio Code.
+
+1. Create a `.rest` or `.http` file.
+
+1. Paste the following placeholders and request into the file.
+
+   ```http
+   @baseUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
+   @token = PUT-YOUR-PERSONAL-IDENTITY-TOKEN-HERE
+
+   ### List existing indexes
+   GET {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
+      Content-Type: application/json
+      Authorization: Bearer {{token}}
+   ```
+
+1. Replace `@baseUrl` with the value you obtained in [Get service information](#get-service-information).
+
+1. Replace `@token` with the value you obtained in [Get token](#get-token).
+
+1. Under `### List existing indexes`, select **Send Request**.
+
+   You should receive an `HTTP/1.1 200 OK` response, indicating a successful connection to your search service.
+
+### Troubleshoot 401 errors
+
+If you encounter a 401 error, follow these troubleshooting steps:
+
++ Revisit [Configure role-based access](#configure-role-based-access). Your search service must have **Role-based access control** or **Both** enabled. Policies at the subscription or resource group level might also override your role assignments.
+
++ Revisit [Get token](#get-token). You must sign in to the subscription that contains your search service.
+
++ Make sure your endpoint and token variables don't have surrounding quotes or extra spaces.
+
++ Make sure your token doesn't have the `@` symbol in the request header. For example, if the variable is `@token`, the reference in the request should be `{{token}}`.
+
++ If all else fails, restart your device to remove cached tokens and then repeat the steps in this quickstart, starting with [Get token](#get-token).
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "REST 用の RBAC 連携による検索スタートガイドの追加"
}
```

### Explanation
この変更は、`search-get-started-rbac-rest.md` という新しいファイルの追加を示しています。このクイックスタートガイドでは、ロールベースのアクセス制御（RBAC）と Microsoft Entra ID を用いて、Azure AI Search サービスへのキーレス接続を確立し、REST を使用してサービスと対話する方法が詳細に説明されています。

キーレス接続は、詳細な権限設定とアイデンティティに基づく認証を通じてセキュリティを強化します。従来のハードコードされた API キーは推奨されていませんが、必要であればキーを使った接続方法についてのリンクも提供されています。

更新されたガイドには、前提条件として Azure アカウント、Azure AI Search サービス、Azure CLI、Visual Studio Code の REST Client 拡張機能が含まれています。また、Azure CLI を使用してトークンを取得する手順や、Visual Studio Code で REST を介して接続するための具体的な手順が記載されています。

ユーザーは、生成したトークンを用いてリクエストを認証し、既存のインデックスをリストするためのサンプルリクエストを送信することができます。401 エラーのトラブルシューティング手順も提供されており、接続に成功するためのサポートがなされています。このガイドは、Microsoft Entra ID を使用する他のクイックスタートの前提条件となっており、Azure AI Search と REST の連携を学ぶための重要なリソースとなります。

## articles/search/includes/quickstarts/search-get-started-rbac-setup.md{#item-ad1076}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,46 @@
+---
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 07/08/2025
+---
+
+## Configure role-based access
+
+In this section, you enable RBAC on your Azure AI Search service and assign the necessary roles for creating, loading, and querying search objects. For more information about these steps, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
+
+To configure access:
+
+1. Sign in to the [Azure portal](https://portal.azure.com) and select your search service.
+
+1. From the left pane, select **Settings > Keys**.
+
+1. Select **Role-based access control** or **Both** if you need time to transition clients to RBAC.
+
+   :::image type="content" source="../../media/search-get-started-rbac/access-control-options.png" lightbox="../../media/search-get-started-rbac/access-control-options.png" alt-text="Screenshot of the access control options in the Azure portal.":::
+
+1. From the left pane, select **Access control (IAM)**.
+
+1. Select **Add** > **Add role assignment**.
+
+   :::image type="content" source="../../media/search-get-started-rbac/add-role-assignment.png" lightbox="../../media/search-get-started-rbac/add-role-assignment.png" alt-text="Screenshot of the dropdown menu for adding a role assignment in the Azure portal.":::
+
+1. Assign the **Search Service Contributor** role to your user account or managed identity.
+
+1. Repeat the role assignment for **Search Index Data Contributor**.
+
+## Get service information
+
+In this section, you retrieve the subscription ID and endpoint of your Azure AI Search service. If you only have one subscription, skip the subscription ID and only retrieve the endpoint. You use these values in the remaining sections of this quickstart.
+
+To get your service information:
+
+1. Sign in to the [Azure portal](https://portal.azure.com) and select your search service.
+
+1. From the left pane, select **Overview**.
+
+1. Make a note of the subscription ID and endpoint.
+
+   :::image type="content" source="../../media/search-get-started-rbac/subscription-and-endpoint.png" lightbox="../../media/search-get-started-rbac/subscription-and-endpoint.png" alt-text="Screenshot of the subscription ID and endpoint in the Azure portal.":::
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "RBAC 構成手順の追加"
}
```

### Explanation
この変更は、`search-get-started-rbac-setup.md` という新しいファイルの追加を示しています。このセクションでは、Azure AI Search サービスにおいてロールベースのアクセス制御（RBAC）を有効化し、検索オブジェクトを作成、ロード、照会するために必要な役割を割り当てる手順が説明されています。

ユーザーは Azure ポータルにサインインし、RBAC 設定のためのステップに従って、必要な役割を自身のユーザーアカウントまたはマネージドアイデンティティに割り当てることが出来ます。RBAC を適用するために、**アクセス制御 (IAM)** から新しいロールの割り当てを追加する操作が詳細に記載されており、役割の選択肢およびそれに関連するスクリーンショットが提供されています。

さらに、このガイドでは Azure AI Search サービスのサブスクリプション ID とエンドポイントを取得する方法についても記載されています。これらの情報は、他のクイックスタートセクションで使用されるため、重要な手順となります。具体的な手順を示すために、画像も含まれており、ユーザーが設定をより容易に行えるように工夫されています。この新しいセクションは、RBAC を利用したアクセス管理を行う上での基本的なリソースとなるでしょう。

## articles/search/includes/quickstarts/search-get-started-vector-rest.md{#item-c7d261}

<details>
<summary>Diff</summary>
````diff
@@ -388,7 +388,7 @@ Key takeaways about the [Create Index](/rest/api/searchservice/indexes/create) R
 
 - Vector fields must be one of the [EDM data types used for vectors](/rest/api/searchservice/supported-data-types#edm-data-types-for-vector-fields), such as `type: Collection(Edm.Single)`. Vector fields also have `dimensions` and `vectorSearchProfile` properties.
 
-- The `vectorSearch` section is an array of approximate nearest neighbor algorithm configurations and profiles. Supported algorithms include hierarchical navigable small world and exhaustive k-nearest neighbor. For more information, see [Relevance scoring in vector search](../../vector-search-ranking.md).
+- The `vectorSearch` section is an array of Approximate Nearest Neighbor (ANN) algorithm configurations and profiles. Supported algorithms include Hierarchical Navigable Small World and exhaustive K-Nearest Neighbor. For more information, see [Relevance scoring in vector search](../../vector-search-ranking.md).
 
 - The (optional) `semantic` configuration enables reranking of search results. You can rerank results in queries of type `semantic` for string fields that are specified in the configuration. To learn more, see [Semantic ranking overview](../../semantic-search-overview.md).
 
@@ -669,7 +669,7 @@ The vector query string is semantically similar to the search string, but it inc
 
 ### Single vector search
 
-1. Formulate the request. The query is a 1536 float representation of *quintessential lodging near running trails, eateries, retail*. The query is searching `DescriptionVector` and returning k-5 results. It's using the "exhaustive" override parameter to perform a full scan of the index instead of approximate nearest neighbor. An exhaustive search is useful for small indexes.
+1. Formulate the request. The query is a 1536 float representation of *quintessential lodging near running trails, eateries, retail*. The query is searching `DescriptionVector` and returning k-5 results. It's using the "exhaustive" override parameter to perform a full scan of the index instead of ANN. An exhaustive search is useful for small indexes.
 
     ```http
     ### Run a single vector query
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索の説明の修正"
}
```

### Explanation
この変更は、`search-get-started-vector-rest.md` ファイルにおけるベクトル検索に関連する説明の修正を示しています。具体的には、近似最近傍検索（ANN）アルゴリズムに関する記述が明確化されました。

修正内容には、まず「approximate nearest neighbor algorithm configurations and profiles」という表現が、「Approximate Nearest Neighbor (ANN) algorithm configurations and profiles」と変更されており、略語が初めて出る際にその意味を明示しています。また、"exhaustive k-nearest neighbor"という用語が"exhaustive K-Nearest Neighbor"に変更され、大文字記法が統一されています。これにより、用語の一貫性が向上しています。

これらの変更は、文書内での検索アルゴリズムの理解を促進し、読者にとっての明瞭さを向上させる目的で行われました。ファイルの他の部分に影響を与えることなく、具体的な用語の表現を改善することで、狙った情報を利用者がスムーズに取得できるよう工夫されています。

## articles/search/includes/quickstarts/semantic-ranker-rest.md{#item-d74861}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
 manager: nitinme
-author: haileytapia
+author: heidisteen
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
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
この変更は、`semantic-ranker-rest.md` ファイルにおける著者情報の更新を示しています。具体的には、著者の名前が「haileytapia」から「heidisteen」に変更されました。この変更は、文書の管理や著作権に関連する情報を最新のものに保つために行われたものです。

他のメタデータやコンテンツには影響を与えず、ただ著者名のみが修正されているため、文書の内容や構造には大きな変更はありませんが、正確な著者情報の反映は重要です。この更新により、ドキュメントが正確な情報を提供し続けることが期待されます。

## articles/search/keyless-connections.md{#item-3f0d72}

<details>
<summary>Diff</summary>
````diff
@@ -4,6 +4,7 @@ description: Use keyless connections with an Azure Identity library for Microsof
 ms.topic: how-to
 ms.date: 06/17/2025
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 author: HeidiSteen
 ms.author: heidist
 ms.custom: devx-track-dotnet, devx-track-extended-java, devx-track-js, devx-track-python, Keyless-dotnet, Keyless-java, Keyless-js, Keyless-python, build-2024-intelligent-apps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "更新周期の追加"
}
```

### Explanation
この変更は、`keyless-connections.md` ファイルにおいて、更新周期に関するメタデータの追加を示しています。具体的には、`ms.update-cycle: 180-days` という行が追加され、ドキュメントの内容がどのくらいの頻度で更新されるかを明示しています。

この修正は、利用者に対して情報の信頼性やメンテナンス状況を伝えるためのものであり、特に長期にわたってその内容が有効であることを示す役割を果たします。他の内容には影響を与えず、単独での追加であるため、文書全体の骨組みや構造には変化はありませんが、利用者にとっては重要な更新情報が提供されることになります。

## articles/search/media/search-get-started-rbac/access-control-options.png{#item-bc7170}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "アクセス制御オプション画像の追加"
}
```

### Explanation
この変更は、`access-control-options.png` という画像ファイルが `search-get-started-rbac` フォルダーに新たに追加されたことを示しています。この画像は、Azure 検索サービスにおけるロールベースのアクセス制御 (RBAC) に関連するオプションを視覚的に説明するためのものであると考えられます。

画像の追加により、ドキュメント内の情報が視覚的に強化され、利用者が概念を理解しやすくなることが期待されます。テキストだけでは伝えにくい情報を補完するための重要な要素であり、ユーザー体験を向上させるために役立ちます。この変更は、ドキュメントの内容に対して新しい情報を提供する役割を果たしています。

## articles/search/media/search-get-started-rbac/add-role-assignment.png{#item-fb7936}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ロール割り当て追加画像の追加"
}
```

### Explanation
この変更は、`add-role-assignment.png` という新しい画像ファイルが `search-get-started-rbac` フォルダーに追加されたことを反映しています。この画像は、Azure のロールベースのアクセス制御 (RBAC) におけるロール割り当ての追加手順を視覚的に示すために使用されると予想されます。

視覚資料の追加により、手順やプロセスを直感的に理解できるようになり、特に技術的な概念を学ぶ際に利用者にとっての利便性が向上します。また、テキスト情報だけでは伝えきれない内容を補完する重要なリソースとして機能します。この変更によって、全体のドキュメントがより包括的になり、読者が.value of information にアクセスしやすくなることが期待されます。

## articles/search/media/search-get-started-rbac/subscription-and-endpoint.png{#item-b5f993}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "サブスクリプションとエンドポイントの画像の追加"
}
```

### Explanation
この変更は、`subscription-and-endpoint.png` という新たな画像ファイルが `search-get-started-rbac` フォルダーに追加されたことを示しています。この画像は、Azure サービスのサブスクリプションやエンドポイントの設定に関する情報を視覚的に提供することを目的としていると考えられます。

新しい画像の追加によって、プロセスや概念をより明確に理解できるようになるため、特にドキュメントの対象とする読者にとって役立つ情報源となります。視覚的要素は、複雑な内容を簡潔に説明するのに役立ち、ユーザーの理解を促進します。また、この変更は、全体のドキュメントの質を向上させ、利用者にとっての利便性を高めることが期待されます。

## articles/search/multimodal-search-overview.md{#item-d82192}

<details>
<summary>Diff</summary>
````diff
@@ -3,6 +3,7 @@ title: Multimodal Search Concepts and Guidance
 titleSuffix: Azure AI Search
 description: Learn what multimodal search is, how Azure AI Search supports it for text and image content, and where to find detailed concepts, tutorials, and samples.
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: conceptual
 ms.date: 05/29/2025
 author: gmndrg
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダル検索の更新周期の追加"
}
```

### Explanation
この変更は、`multimodal-search-overview.md` ファイルに対する軽微な更新を示しており、具体的には「ms.update-cycle: 90-days」という新しいメタデータが追加されています。この項目は、Azure AI Searchに関連するマルチモーダル検索の内容が90日ごとに更新されることを示しています。

この修正により、ユーザーはコンテンツの更新頻度を理解し、最新情報が提供されるタイミングについて知ることができるようになります。特に、技術的なドキュメントやガイドラインにおいて、更新のサイクルは利用者にとって重要な情報であり、彼らが常に最新の知識を持っているかどうかを判断する助けとなります。このような情報の追加は、ドキュメントの透明性や信頼性を高める効果があります。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.author: heidist
 manager: nitinme
 ms.date: 04/15/2025
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: conceptual
 ms.custom:
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "取得強化生成の更新周期の追加"
}
```

### Explanation
この変更は、`retrieval-augmented-generation-overview.md` ファイルに対して行われたもので、具体的には「ms.update-cycle: 90-days」という新しいメタデータが追加されています。この情報は、Azure AI Searchに関連する取得強化生成のコンテンツが90日ごとに更新されることを示しています。

この更新により、読者はコンテンツの維持管理の透明性が増し、どの程度の頻度で新しい情報が提供されるかを把握できるようになります。特に、技術的な内容やドキュメントにおいては、更新のタイミングを理解することが重要であり、ユーザーが最新の知識や機能を利用できるようになることに寄与します。こうした詳細の追加は、文書の信頼性や有用性を高める効果があります。

## articles/search/samples-dotnet.md{#item-12f3fa}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.custom:
   - devx-track-dotnet
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サンプルの更新周期の追加"
}
```

### Explanation
この変更は、`samples-dotnet.md` ファイルに対して行われたもので、「ms.update-cycle: 90-days」という新しいメタデータが追加されています。この変更により、Azure AI Searchに関連するサンプルコードのコンテンツが90日ごとに更新されることが明示されます。

この更新は、利用者に対してサンプルコードのコンテンツがどのように管理されているかについての重要な情報を提供します。特に開発者にとって、ドキュメントの信頼性や最新性を担保することは非常に重要であり、こうした更新サイクルの情報は、利用者が常に最新の情報にアクセスできることを保証します。このように、更新周期の明記は、サンプルコードの有用性を高めるために役立ちます。

## articles/search/samples-java.md{#item-5992fd}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - devx-track-dotnet
   - devx-track-extended-java
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サンプルの更新周期の変更"
}
```

### Explanation
この変更は、`samples-java.md` ファイルに対して行われたもので、メタデータの一部として「ms.update-cycle: 180-days」という情報が追加されています。この内容は、Azure AI Searchに関連するJavaサンプルコードのコンテンツが180日ごとに更新されることを示しています。

この更新は、ユーザーにとってサンプルコードの情報がどのように維持管理されているかを理解する上で重要です。特に開発者にとって、プログラムサンプルの最新性は非常に重要であり、更新周期が記載されることで、ユーザーは自身のプロジェクトに対する信頼性を増すことができます。180日の更新周期の明示は、プログラムサンプルがどれだけ頻繁に見直されるかを示し、ドキュメントの有用性を向上させるために寄与しています。

## articles/search/samples-javascript.md{#item-82e67e}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.custom:
   - devx-track-dotnet
   - devx-track-js
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サンプルの更新周期の追加"
}
```

### Explanation
この変更は、`samples-javascript.md` ファイルに新たに「ms.update-cycle: 90-days」というメタデータが追加されたことを示しています。この情報により、Azure AI Searchに関連するJavaScriptのサンプルコードが90日ごとに更新されることが明確にされました。

この更新は、ドキュメントを利用する開発者にとって非常に重要です。サンプルコードがどのように維持され、どれだけの頻度で更新されるかを知ることができるため、ユーザーは常に最新の情報にアクセスできることを期待できます。90日間隔の更新周期の導入は、プロジェクトの信頼性を向上させるために必要な情報であり、利用者がより効果的にサンプルコードを活用できるようにします。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.custom:
   - devx-track-dotnet
   - devx-track-python
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サンプルの更新周期の追加"
}
```

### Explanation
この変更は、`samples-python.md` ファイルに「ms.update-cycle: 90-days」という情報が追加されたことを示しています。この更新により、Azure AI Searchに関連するPythonのサンプルコードが90日ごとに更新されることが明確になりました。

この追加は、ユーザーにとって非常に重要です。サンプルコードの更新頻度が示されることで、開発者は常に最新の情報を元に作業を行うことができます。また、この90日間隔の更新周期は、ドキュメントの信頼性を向上させ、利用者がより効率的にサンプルコードを活用するために役立ちます。このように、定期的な更新が明示されることで、ユーザーは自らのプロジェクトにおいて最新の技術や実装方法を反映しやすくなります。

## articles/search/samples-rest.md{#item-198ebc}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTサンプルの更新周期の追加"
}
```

### Explanation
この変更は、`samples-rest.md` ファイルに「ms.update-cycle: 90-days」という新しいメタデータが追加されたことを示しています。これにより、Azure AI Searchに関連するRESTのサンプルコードが90日ごとに更新されることが明確になりました。

この情報は、開発者やユーザーにとって重要です。定期的な更新周期があることで、サンプルコードの新しい情報や改善点が適時反映されることが期待され、ユーザーは常に最新のベストプラクティスに基づいて作業することができます。この90日間隔での更新は、ドキュメントの品質向上に寄与し、利用者が自らのプロジェクトにおいて最新の技術や手法を取り入れやすくするための基盤を提供します。

## articles/search/search-agentic-retrieval-concept.md{#item-797a22}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.author: heidist
 manager: nitinme
 ms.date: 06/08/2025
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: concept-article
 ms.custom:
   - references_regions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索の概念に関する更新周期の追加"
}
```

### Explanation
この変更は、`search-agentic-retrieval-concept.md` ファイルに「ms.update-cycle: 90-days」という新しいメタデータが追加されたことを示しています。この追加により、Azure AI Search に関連するエージェント検索の概念に関する情報が90日ごとに更新されることが規定されました。

この更新周期を明示することは、ユーザーや開発者において重要です。定期的な更新の存在は、関連情報の新しさや正確性を保つために欠かせない要素であり、最新の実装や概念が文書に反映されることを保証します。これにより、ユーザーは自分のプロジェクトに最新の知識や技術を取り入れやすくなり、エージェント検索の利用がより効果的になります。90日ごとの更新が明記されることで、ドキュメントの信頼性向上にも寄与します。

## articles/search/search-agentic-retrieval-how-to-create.md{#item-310fbe}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: how-to
 ms.date: 05/30/2025
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索の作成方法に関する更新周期の追加"
}
```

### Explanation
この変更は、`search-agentic-retrieval-how-to-create.md` ファイルに「ms.update-cycle: 90-days」という新しいメタデータが追加されたことを示しています。この変更により、Azure AI Search に関連する「エージェント検索の作成方法」についての文書が90日ごとに更新されることが明確になりました。

定期的な更新の確立は、ユーザーが最新の情報とベストプラクティスにアクセスできることを保証します。この文書が90日ごとに更新されることで、利用者は常に最も新しい手法や実装に基づいて作業を行うことができ、エージェント検索の機能をより効果的に活用できるようになります。更新サイクルを明示することで、ドキュメントの信頼性が高まり、利用者が適宜新たな知識を取り入れる手助けとなります。

## articles/search/search-agentic-retrieval-how-to-index.md{#item-a078ea}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: how-to
 ms.date: 05/05/2025
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索のインデックス作成方法に関する更新周期の追加"
}
```

### Explanation
この変更は、`search-agentic-retrieval-how-to-index.md` ファイルに「ms.update-cycle: 90-days」という新しいメタデータが追加されたことを示しています。この追加により、Azure AI Search に関連する「エージェント検索のインデックス作成方法」についての情報が90日ごとに更新されることが明確になります。

定期的な更新の導入は、利用者が最新の情報にアクセスできることを保証し、適切なインデックス作成手法に基づいてエージェント検索を効果的に活用するために重要です。このような更新サイクルがあることで、ユーザーは新しい機能やベストプラクティスが文書に反映されることを期待でき、常に最適な方法で作業を進めることが可能になります。また、情報の信頼性が向上し、エージェント検索の操作に対する理解が深まることにも寄与します。

## articles/search/search-agentic-retrieval-how-to-pipeline.md{#item-1ad1c3}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.author: heidist
 manager: nitinme
 ms.date: 06/08/2025
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: how-to
 ms.custom:
   - build-2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索のパイプライン作成方法に関する更新周期の追加"
}
```

### Explanation
この変更は、`search-agentic-retrieval-how-to-pipeline.md` ファイルに「ms.update-cycle: 90-days」という新しいメタデータが追加されたことを示しています。この新しい項目により、Azure AI Search に関連する「エージェント検索のパイプライン作成方法」についての情報が90日ごとに更新されることが明確になります。

定期的な更新サイクルを持つことは、ユーザーがアルゴリズムや機能の変更、新しいベストプラクティスに対する理解を深めるために重要です。この変更により、ユーザーはドキュメントが最新の情報を反映していることを期待でき、エージェント検索パイプラインの利用において最適な選択が可能になります。さらに、更新の内容やタイミングが明確であることで、利用者は必要に応じて情報を再確認し、より効果的に検索機能を利用することができます。

## articles/search/search-agentic-retrieval-how-to-retrieve.md{#item-5f7fc0}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: how-to
 ms.date: 06/08/2025
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント検索の取得方法に関する更新周期の追加"
}
```

### Explanation
この変更は、`search-agentic-retrieval-how-to-retrieve.md` ファイルに「ms.update-cycle: 90-days」という追加が行われたことを示しています。この新しいメタデータは、Azure AI Search に関連する「エージェント検索の取得方法」に関する情報が90日ごとに更新されることを明示します。

このアップデートにより、ユーザーは提供された情報が新しい技術やベストプラクティスを反映していることについての期待感を持つことができます。定期的な更新循環は、ドキュメントが常に最新の状態に保たれ、検索機能を最大限に活用するための手助けとなります。また、ユーザーがエージェント検索を効果的に理解し活用するために必要な情報が提供されることに貢献します。これにより、ユーザーは文書の更新状況を把握し、必要に応じて情報を再確認することができるようになります。

## articles/search/search-blob-indexer-role-based-access.md{#item-887e42}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,162 @@
+---  
+title: Use a Blob indexer to ingest RBAC scopes metadata
+titleSuffix: Azure AI Search  
+description: Learn how to configure Azure AI Search indexers for ingesting Azure Role-Based Access (RBAC) metadata on Azure Blobs.
+ms.service: azure-ai-search  
+ms.topic: how-to
+ms.date: 07/07/2025  
+author: vaishalishah
+ms.author: vaishalishah
+---  
+
+# Use a Blob indexer to ingest RBAC scopes metadata
+
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+Starting in 2025-05-01-preview, you can now include RBAC scope alongside document ingestion in Azure AI Search and use those permissions to control access to search results.
+
+You can use the push APIs to upload and index content and permission metadata manually see [Indexing Permissions using the push REST API](search-index-access-control-lists-and-rbac-push-api.md), or you can use an indexer to automate data ingestion. This article focuses on the indexer approach.
+
+The indexer approach is built on this foundation:
+
++ [Role-based access control (Azure RBAC)](/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac). There's no support for Attribute-based access control (Azure ABAC).
+
++ [An Azure AI Search indexer for Blob](search-howto-indexing-azure-blob-storage.md) that retrieves and ingests data and metadata, including permission filters. To get permission filter support, you must use the 2025-05-01-preview REST API or a prerelease package of an Azure SDK that supports the feature.
+
++ [An index in Azure AI Search](search-how-to-create-search-index.md) containing the ingested documents and corresponding permissions. Permission metadata is stored as fields in the index. To set up queries that respect the permission filters, you must use the 2025-05-01-preview REST API or a prerelease package of an Azure SDK that supports the feature.
+
+## Prerequisites
+
++ [Microsoft Entra ID authentication and authorization](/entra/identity/authentication/overview-authentication). Services and apps must be in the same tenant. Role assignments are used for each authenticated connection.
+
++ Azure AI Search, any region, but you must have a billable tier (basic and higher) see [Service limits](search-limits-quotas-capacity.md) for managed identity support. The search service must be [configured for role-based access](search-security-enable-roles.md) and it must [have a managed identity (either system or user)](search-howto-managed-identities-data-sources.md).
+
+## Limitations
+
++ The following indexer features don't support permission preservation capabilities but are otherwise operational for Azure Blob content-only indexing:
+  + One-to-many [parsing modes](/rest/api/searchservice/indexers/create?view=rest-searchservice-2025-05-01-preview&preserve-view=true#blobindexerparsingmode), such as: `delimitedText`, `jsonArray`, `jsonLines`, and `markdown` with sub-mode `oneToMany`
+
+
+### Authorization
+
+For indexer execution, your search service identity must have **Storage Blob Data Reader** permission see [Connect to Azure Storage using a managed identity](search-howto-managed-identities-storage.md).
+
+## Configure Azure AI Search for indexing permission filters
+
+Recall that the search service must have:
+
++ [Role-based access enabled](search-security-enable-roles.md)
++ [Managed identity configured](search-howto-managed-identities-data-sources.md)
+
+### Authorization
+
+For indexer execution, the client issuing the API call must have **Search Service Contributor** permission to create objects, **Search Index Data Contributor** permission to perform data import, and **Search Index Data Reader** to query an index see [Connect to Azure AI Search using roles](search-security-rbac.md).
+
+## Indexing permission metadata
+
+In Azure AI Search, configure an indexer, data source, and index to pull permission metadata from blobs.
+
+### Configure the data source
+
++ Data Source type must be `azureblob`.
+
++ Data source must have `indexerPermissionOptions` with `rbacScope`.
+
+  + For `rbacScope`, configure the [connection string](search-howto-index-azure-data-lake-storage.md#supported-credentials-and-connection-strings) with managed identity format.
+  
+  + For connection strings using a [user-assigned managed identity](search-howto-managed-identities-storage.md#user-assigned-managed-identity), you must also specify the `identity` property.
+
+<!-- Question/Comment: check this example -->
+JSON example with system managed identity:
+
+```json
+{
+    "name" : "my-blob-datasource",
+    "type": "azureblob",
+    "indexerPermissionOptions": ["rbacScope"],
+    "credentials": {
+    "connectionString": "ResourceId=/subscriptions/<your subscription ID>/resourceGroups/<your resource group name>/providers/Microsoft.Storage/storageAccounts/<your storage account name>/;"
+    },
+    "container": {
+        "name": "<your container name>",
+        "query": "<optional-query>"
+    }
+}
+```
+
+JSON schema example with a user-managed identity in the connection string:
+
+```json
+{
+    "name" : "my-blob-datasource",
+    "type": "azureblob",
+    "indexerPermissionOptions": ["rbacScope"],
+    "credentials": {
+    "connectionString": "ResourceId=/subscriptions/<your subscription ID>/resourceGroups/<your resource group name>/providers/Microsoft.Storage/storageAccounts/<your storage account name>/;"
+    },
+    "container": {
+        "name": "<your container name>",
+        "query": "<optional-query>"
+    },
+    "identity": {
+        "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
+        "userAssignedIdentity": "/subscriptions/{subscription-ID}/resourceGroups/{resource-group-name}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{user-assigned-managed-identity-name}"
+    }
+}
+```
+
+### Create permission fields in the index
+
+In Azure AI Search, make sure your index contains field definitions for the permission metadata. Permission metadata can be indexed when `indexerPermissionOptions` is specified in the data source definition.
+
+Recommended schema attributes RBAC Scope:
+
++ RBAC scope field with `rbacScope` permissionFilter value.
++ Property `permissionFilterOption` to enable filtering at querying time.
++ Use string fields for permission metadata
++ Set `filterable` to true on all fields.
+
+Notice that `retrievable` is false. You can set it true during development to verify permissions are present, but remember to set to back to false before deploying to a production environment.
+
+JSON schema example:
+
+```json
+{
+  ...
+  "fields": [
+    ...
+    { 
+        "name": "RbacScope", 
+        "type": "Edm.String", 
+        "permissionFilter": "rbacScope", 
+        "filterable": true, 
+        "retrievable": false 
+    }
+  ],
+  "permissionFilterOption": "enabled"
+}
+```
+
+### Configure the indexer
+
+Field mappings within an indexer set the data path to fields in an index. Target and destination fields that vary by name or data type require an explicit field mapping. The following metadata fields in Azure Blob might need field mappings if you vary the field name:
+
++ **metadata_rbac_scope** (`Edm.String`) - the container RBAC scope.
+
+Specify `fieldMappings` in the indexer to route the permission metadata to target fields during indexing.
+
+JSON schema example:
+
+```json
+{
+  ...
+  "fieldMappings": [
+    { "sourceFieldName": "metadata_rbac_scope", "targetFieldName": "RbacScope" }
+  ]
+}
+```
+
+## Deletion tracking 
+
+To effectively manage blob deletion, ensure that you have enabled [deletion tracking](search-howto-index-changed-deleted-blobs.md) before your indexer runs for the first time. This feature allows the system to detect deleted blobs from your source and have them deleted from the index.  
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "RBACスコープメタデータを取り込むためのBlobインデクサの追加"
}
```

### Explanation
この変更は、`search-blob-indexer-role-based-access.md` という新しいファイルが追加されたことを示しています。このファイルでは、Azure AI SearchにおいてRBAC（役割ベースのアクセス制御）スコープメタデータを取り込むためのBlobインデクサの設定方法について詳しく説明しています。

新機能では、2025年5月1日以降にRBACスコープを文書の取り込みとともに含めることができ、その権限を使用して検索結果へのアクセスを制御することが可能になります。ユーザーは手動でコンテンツと権限メタデータをアップロードするか、インデクサを利用してデータの取り込みを自動化することができます。

この文書は、RBACモデル、インデクサの設定、権限メタデータのインデクション、データソースの構成、インデックスのフィールド設定、削除のトラッキングなど、多くの重要なトピックをカバーしています。また、インデクサの実行には、必要な権限（Storage Blob Data Readerなど）や設定が求められることが明記されています。

ユーザーはこのドキュメントを参照することにより、Azure AI SearchのRBACを効果的に活用し、アクセス制御を強化するための具体的な手順とベストプラクティスを習得することができます。

## articles/search/search-create-service-portal.md{#item-f90159}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - references_regions
   - build-2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービスポータル作成ガイドの更新周期を追加"
}
```

### Explanation
この変更は、`search-create-service-portal.md` ファイルに「ms.update-cycle: 180-days」という新しいメタデータを追加しています。これにより、Azure AI Searchに関するサービスポータルの作成ガイドが180日ごとに更新されることが明示されたことを意味します。

このアップデートは、ドキュメントの信頼性を向上させ、ユーザーが提供される情報が最新のものであるとの期待感を持つことを可能にします。定期的な更新サイクルにより、ユーザーは新ハードウェア、ソフトウェア、またはベストプラクティスに関する変更を継続的に受け取ることができ、活用の幅が広がります。これにより、サービスポータルの利用者にとって、常に関連性があり、有用な情報を提供することが強調されています。

## articles/search/search-data-sources-gallery.md{#item-18727f}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ author: HeidiSteen
 ms.author: heidist
 
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データソースギャラリーの更新周期を追加"
}
```

### Explanation
この変更は、`search-data-sources-gallery.md` ファイルに「ms.update-cycle: 180-days」という新しいメタデータの行を追加しています。これにより、Azure AI Searchのデータソースギャラリーに関する情報が180日ごとに更新されることが示されています。

この更新の追加は、利用者が提供される情報をより信頼できるものとし、定期的な更新を通じて最新の機能やデータソースの、特にサポートされているソフトウェアやサービスについての詳細を受け取ることができるよう設計されています。このようにして、ユーザーは常に最新の情報を持つことができ、適切な意思決定に役立つことを目指しています。更新周期が設定されることで、ドキュメントの活用価値が高まると同時に、情報の鮮度を保つことが強調されています。

## articles/search/search-document-level-access-overview.md{#item-4bb055}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ author: gmndrg
 ms.author: gimondra
 ms.date: 07/03/2025
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: conceptual
 ms.custom:
   - build-2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレベルのアクセス概要の更新周期を追加"
}
```

### Explanation
この変更は、`search-document-level-access-overview.md` ファイルに「ms.update-cycle: 90-days」という新しいメタデータの行を追加しています。これにより、Azure AI Searchにおけるドキュメントレベルのアクセスに関する情報が90日ごとに更新されることが示されています。

このアップデートは、ユーザーが受け取る情報の信頼性と関連性を向上させることを目的としています。定期的な更新により、最新の機能やガイドライン、ベストプラクティスが反映されるため、利用者は常に最新のデータにアクセスでき、より適切な意思決定を行うことができるようになります。更新周期の設定は、ドキュメントの活用価値を高め、情報の鮮度を保つ重要な要素として機能しています。

## articles/search/search-faq-frequently-asked-questions.yml{#item-eab2ba}

<details>
<summary>Diff</summary>
````diff
@@ -8,6 +8,7 @@ metadata:
   author: haileytap
   ms.author: haileytapia
   ms.service: azure-ai-search
+  ms.update-cycle: 90-days
   ms.topic: faq
   ms.date: 03/21/2025
 title: Azure AI Search Frequently Asked Questions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQの更新周期を追加"
}
```

### Explanation
この変更は、`search-faq-frequently-asked-questions.yml` ファイルに「ms.update-cycle: 90-days」という新しいメタデータの行を追加しています。この追加により、Azure AI Searchに関するFAQ（よくある質問）の情報が90日ごとに見直され、更新されることが示されています。

この更新の目的は、ユーザーが常に最も関連性の高い情報を受け取ることを保証し、FAQセクションが最新の状態に保たれるようにすることです。定期的なレビューと更新によって、新しい質問や回答が追加され、現在のトレンドや問題に対する対応が可能となります。このようにして、FAQの信頼性が向上し、利用者が必要とする情報を迅速に見つける手助けをすることが期待されています。

## articles/search/search-features-list.md{#item-d34448}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.custom:
   - ignite-2024
 ms.topic: conceptual
@@ -36,7 +37,7 @@ The following table summarizes features by category. There's feature parity in a
 |-------------------|----------|
 | Vector indexing | Within a search index, add [vector fields](vector-search-how-to-create-index.md) to support  [**vector search**](vector-search-overview.md) scenarios. Vector fields can coexist with nonvector fields in the same search document. |
 | Vector queries | [Formulate single and multiple vector queries](vector-search-how-to-query.md). |
-| Vector search algorithms | Use [Hierarchical Navigable Small World (HNSW)](vector-search-ranking.md#when-to-use-hnsw) or [exhaustive K-Nearest Neighbors (KNN)](vector-search-ranking.md#when-to-use-exhaustive-knn) to find similar vectors in a search index. |
+| Vector search algorithms | Use [Hierarchical Navigable Small World (HNSW)](vector-search-ranking.md#about-hnsw) or [exhaustive K-Nearest Neighbors (KNN)](vector-search-ranking.md#about-exhaustive-knn) to find similar vectors in a search index. |
 | Vector filters | [Apply filters before or after query execution](vector-search-filters.md) for greater precision during information retrieval. |
 | Hybrid information retrieval | Search for concepts and keywords in a single [hybrid query request](hybrid-search-how-to-query.md). </p>[**Hybrid search**](hybrid-search-overview.md) consolidates vector and text search, with optional semantic ranking and relevance tuning for best results.|
 | Integrated data chunking and vectorization | Native data chunking through [Text Split skill](cognitive-search-skill-textsplit.md). Native vectorization through [vectorizers](vector-search-how-to-configure-vectorizer.md) and embedding skills such as [AzureOpenAIEmbeddingModel](cognitive-search-skill-azure-openai-embedding.md), [Azure AI Vision multimodal](cognitive-search-skill-vision-vectorize.md), and the [AML skill](cognitive-search-aml-skill.md) that you can use to connect to endpoints in the Azure AI Foundry model catalog. </p>[**Integrated vectorization**](vector-search-integrated-vectorization.md) provides an end-to-end indexing pipeline from source files to queries.|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "機能リストに更新周期を追加"
}
```

### Explanation
この変更は、`search-features-list.md` ファイルに「ms.update-cycle: 90-days」という新しいメタデータの行を追加し、90日ごとに内容が見直され、更新されることを示しています。また、機能リストの表内での用語がわずかに修正されています。「Vector search algorithms」セクションでは、HNSWやKNNに関する説明が「about」が追加されて明確になっています。

このアップデートにより、ユーザーはAzure AI Searchの機能についての情報が定期的に更新されることが保証され、より信頼性の高い情報が提供されるようになります。さらに、用語の明確化は情報の理解を助け、使いやすさを向上させることを目的としています。全体として、この変更はドキュメントの質とユーザビリティを向上させる重要なステップとなります。

## articles/search/search-get-started-agentic-retrieval.md{#item-4a40f4}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ description: Learn how to create a knowledge agent that processes multi-turn con
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: quickstart
 ms.date: 6/24/2025
 zone_pivot_groups: search-get-started-agentic-retrieval
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント取得のクイックスタートに更新周期を追加"
}
```

### Explanation
この変更は、`search-get-started-agentic-retrieval.md` ファイルに「ms.update-cycle: 90-days」という新しいメタデータの行を追加しています。この行は、ドキュメントの内容が90日ごとに見直され、更新されることを示しています。

この更新は、知識エージェントの作成に関するクイックスタートガイドにおいて、情報が常に最新で関連性の高いものであることを保証するためのものです。定期的な更新により、ユーザーは新たな機能やベストプラクティスについての情報を得ることができ、より効果的にAzure AI Searchを利用できるようになります。全体として、この修正は、ユーザーエクスペリエンスの向上に寄与する重要なステップです。

## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ description: Learn how to index and search for multimodal content in the Azure p
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: quickstart
 ms.date: 06/11/2025
 ms.custom:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータル画像検索のクイックスタートに更新周期を追加"
}
```

### Explanation
この変更は、`search-get-started-portal-image-search.md` ファイルに「ms.update-cycle: 90-days」という新しいメタデータの行を追加しています。この行は、ドキュメントが90日ごとに見直され、更新されることを示しています。

この更新は、Azureポータルにおけるマルチモーダルコンテンツのインデックス作成と検索方法に関するクイックスタートガイドの精度と関連性を高めるためのものです。定期的な更新により、ユーザーは最新の機能やベストプラクティスを反映した情報を得られるため、より効率的にAzure AI Searchを利用することができます。全体として、この修正はドキュメントの品質を向上させる重要なステップです。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ description: Learn how to use a wizard to automate data chunking and vectorizati
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.custom:
   - build-2024
   - ignite-2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータルベクトルインポートのクイックスタートに更新周期を追加"
}
```

### Explanation
この変更は、`search-get-started-portal-import-vectors.md` ファイルに「ms.update-cycle: 90-days」という新しいメタデータの行を追加しています。この追加は、ドキュメントが90日ごとに見直され、更新されることを示しています。

この更新は、Azureポータルにおけるデータのチャンク化とベクトル化を自動化するウィザードの使用方法に関するクイックスタートガイドの情報を最新の状態に保つためのものです。定期的な更新によってユーザーは新しい機能や改善点に迅速にアクセスでき、Azure AI Searchの効果的な利用が促進します。この修正は、ドキュメントの信頼性と有用性を高める重要なステップと言えます。

## articles/search/search-get-started-portal.md{#item-6d0cb1}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: quickstart
 ms.date: 03/04/2025
 ms.custom:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータルのクイックスタートに更新周期を追加"
}
```

### Explanation
この変更は、`search-get-started-portal.md` ファイルに「ms.update-cycle: 90-days」という新しいメタデータの行を追加しています。この行は、ドキュメントが90日ごとに見直され、更新されることを示しています。

この更新は、Azureポータルに関するクイックスタートガイドの正確性を保つためのもので、ユーザーが最新の情報や機能に素早くアクセスできるようにすることを目的としています。定期的に更新されることで、ユーザーは新しいベストプラクティスを反映した内容を得られ、Azure AI Searchをより効果的に利用することが可能になります。この修正は、ドキュメントの信頼性と有用性を向上させるために重要です。

## articles/search/search-get-started-rag.md{#item-05ff0e}

<details>
<summary>Diff</summary>
````diff
@@ -5,33 +5,45 @@ description: Learn how to use grounding data from Azure AI Search with a chat mo
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.custom:
   - ignite-2024
 ms.topic: quickstart
-ms.date: 03/04/2025
+ms.date: 07/09/2025
 zone_pivot_groups: programming-languages-ai-search-rag-qs
 ---
 
 # Quickstart: Generative search (RAG) using grounding data from Azure AI Search
 
 In this quickstart, you send queries to a chat completion model for a conversational search experience over your indexed content on Azure AI Search. After setting up Azure OpenAI and Azure AI Search resources in the Azure portal, you run code to call the APIs.
 
+::: zone pivot="csharp"
+
+[!INCLUDE [.NET quickstart](includes/quickstarts/search-get-started-rag-dotnet.md)]
+
+::: zone-end
+
+::: zone pivot="javascript"
+
+[!INCLUDE [JavaScript quickstart](includes/quickstarts/search-get-started-rag-javascript.md)]
+
+::: zone-end
 
 ::: zone pivot="python"
 
 [!INCLUDE [Python quickstart](includes/quickstarts/search-get-started-rag-python.md)]
 
 ::: zone-end
 
-::: zone pivot="typescript"
+::: zone pivot="rest"
 
-[!INCLUDE [TypeScript quickstart](includes/quickstarts/search-get-started-rag-typescript.md)]
+[!INCLUDE [Rest quickstart](includes/quickstarts/search-get-started-rag-rest.md)]
 
 ::: zone-end
 
-::: zone pivot="javascript"
+::: zone pivot="typescript"
 
-[!INCLUDE [JavaScript quickstart](includes/quickstarts/search-get-started-rag-javascript.md)]
+[!INCLUDE [TypeScript quickstart](includes/quickstarts/search-get-started-rag-typescript.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGのクイックスタートに新しいゾーンと更新情報を追加"
}
```

### Explanation
この変更は、`search-get-started-rag.md` ファイルに対する重要な改訂で、合計で17行が追加され、5行が削除され、22の変更が行われました。主な変更点は、以下の通りです：

1. **更新周期の追加**: 新しく「ms.update-cycle: 90-days」というメタデータが追加され、ドキュメントが90日ごとに見直されることを示しています。

2. **日付の更新**: ドキュメントの日付が「03/04/2025」から「07/09/2025」へと変更され、内容の有効性が保持されています。

3. **ゾーンの調整**: いくつかのプラットフォームに対するクイックスタートのゾーンが追加または変更され、`REST`と`TypeScript`のクイックスタートが含まれるようになりました。また、セクションの順序が変更されています。

4. **新しいクイックスタートの追加**: 各プログラミング言語に対応するクイックスタートが明確に区分され、ユーザーがより直感的に情報を得ることができるようになっています。

この変更は、Azure AI Searchに基づく生成検索（RAG）の利用を促進し、開発者がより簡単に関連情報にアクセスできるようにすることを目的としています。全体として、内容の整合性とユーザビリティが向上しています。

## articles/search/search-get-started-rbac.md{#item-9d96c1}

<details>
<summary>Diff</summary>
````diff
@@ -1,171 +1,32 @@
 ---
 title: 'Quickstart: Keyless Connection'
 titleSuffix: Azure AI Search
-description: Learn how to switch from API keys to Microsoft Entra identities and role-based access control (RBAC).
+description: Learn how to use role-based access control (RBAC) to connect to an Azure AI Search service.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: quickstart
-ms.date: 07/02/2025
+ms.date: 07/08/2025
+zone_pivot_groups: search-get-started-rbac
 ---
 
-# Quickstart: Connect without keys
+# Quickstart: Connect to a search service
 
-In this quickstart, you configure Azure AI Search to use Microsoft Entra ID authentication and role-based access control (RBAC) to connect from your local system without API keys. You then use Jupyter notebooks or a REST client to interact with your search service.
+::: zone pivot="python"
 
-If you completed other quickstarts that connect using API keys, this quickstart shows you how to switch to identity-based authentication so that you can avoid hard-coded keys in your example code.
+[!INCLUDE [Python quickstart](includes/quickstarts/search-get-started-rbac-python.md)]
 
-## Prerequisites
+::: zone-end
 
-- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+::: zone pivot="rest"
 
-- An [Azure AI Search service](search-create-service-portal.md) in any region or tier. However, to configure a managed identity for Azure AI Search, you need the Basic tier or higher.
+[!INCLUDE [REST quickstart](includes/quickstarts/search-get-started-rbac-rest.md)]
 
-- A command line tool, such as PowerShell or Bash, and the [Azure CLI](/cli/azure/install-azure-cli).
+::: zone-end
 
-## Step 1: Get your Azure subscription and tenant IDs
+## Related content
 
-You need this step if you have more than one subscription or tenant.
-
-1. Get the Azure subscription and tenant for your search service:
-
-   1. Sign into the [Azure portal](https://portal.azure.com) and navigate to your search service.
-
-   1. Notice the subscription name and ID in **Overview** > **Essentials**.
-
-   1. Now select the subscription name to show the parent management group (tenant ID) on the next page.
-
-      :::image type="content" source="media/search-get-started-rbac/select-subscription-name.png" lightbox="media/search-get-started-rbac/select-subscription-name.png" alt-text="Screenshot of the Azure portal page providing the subscription name":::
-
-1. You now know which subscription and tenant Azure AI Search is under. Switch to your local device and a command prompt, and identify the active Azure subscription and tenant on your device:
-
-   ```azurecli
-   az account show
-   ```
-
-1. If the active subscription and tenant differ from the information obtained in the previous step, change the subscription ID. Next, sign in to Azure using the tenant ID that you found in the previous step:
-
-   ```azurecli
-    az account set --subscription <your-subscription-id>
-
-    az login --tenant <your-tenant-id>
-   ```
-
-## Step 2: Configure Azure AI Search for RBAC
-
-1. Sign in to the [Azure portal](https://portal.azure.com) and navigate to your Azure AI Search service.
-
-1. Enable role-based access control (RBAC):
-
-   1. Go to **Settings** > **Keys**.
-
-   1. Choose **Role-based control** or **Both** if you need time to transition clients to role-based access control.
-
-      If you choose **Role-based control**, make sure that you assign yourself *all* roles named in the next instruction or you won't be able to complete tasks in the Azure portal or through a  local client.
-
-1. Assign roles in the Azure portal:
-
-   1. Navigate to your search service.
-
-   1. Select **Access Control (IAM)** in the left pane.
-
-   1. Select **+ Add** > **Add role assignment**.
-
-   1. Choose a role (**Search Service Contributor**, **Search Index Data Contributor**, **Search Index Data Reader**) and assign it to your Microsoft Entra user or group identity.
-
-      Repeat for each role.
-
-      You need **Search Service Contributor** plus **Search Index Data Contributor** to create, load, and query objects on Azure AI Search. For more information, see [Connect using roles](search-security-rbac.md).
-
-> [!TIP]
-> Later, if you get authentication failure errors, recheck the settings in this section. There could be policies at the subscription or resource group level that override any API settings you specify.
-
-## Step 3: Connect from your local system
-
-If you haven't yet signed in to Azure:
-
-```azurecli
-az login
-```
-
-### Using Python and Jupyter notebooks
-
-1. Install the Azure Identity and Azure Search libraries:
-
-    ```python
-    pip install azure-identity azure-search-documents
-    ```
-
-1. Authenticate and connect to Azure AI Search:
-
-    ```python
-    from azure.identity import DefaultAzureCredential
-    from azure.search.documents import SearchClient
-    
-    service_endpoint = "https://<your-search-service-name>.search.windows.net"
-    index_name = "hotels-sample-index"
-    
-    credential = DefaultAzureCredential()
-    client = SearchClient(endpoint=service_endpoint, index_name=index_name, credential=credential)
-    
-    results = client.search("beach access")
-    for result in results:
-        print(result)
-    ```
-
-### Using a REST client
-
-Several quickstarts and tutorials use a REST client, such as Visual Studio Code with the REST extension. Here's how you connect to Azure AI Search from Visual Studio Code.
-
-You should have a `.rest` or `.http` file, similar to the one described in [Quickstart: Vector search](search-get-started-vector.md).
-
-1. Generate an access token.
-
-   ```azurecli
-   az account get-access-token --scope https://search.azure.com/.default --query accessToken --output tsv
-   ```
-
-1. At the top of your file, set variables used for the connection, pasting the full search service endpoint and the access token you got in the previous step. Your variables should look similar to the following example. Notice the values aren't quote-enclosed.
-
-    ```REST
-    @baseUrl = https://contoso.search.search.windows.net
-    @token = <a long GUID>
-    ```
-
-1. Specify the authorization bearer token in a REST call:
-
-   ```REST
-    POST https://{{baseUrl}}/indexes/hotels-sample-index/docs/search?api-version=2024-07-01 HTTP/1.1
-      Content-type: application/json
-      Authorization: Bearer {{token}}
-    
-        {
-             "queryType": "simple",
-             "search": "beach access",
-             "filter": "",
-             "select": "HotelName,Description,Category,Tags",
-             "count": true
-         }
-   ```
-
-### Troubleshoot 401 errors
-
-- Check the active subscription and tenant (`az account show`) and make sure it's valid for your search service.
-
-- Check the search service **Settings** > **Keys** options in the Azure portal and confirm the service is configured for **Both"** or **Role-based access control**.
-
-- For the REST client only: Check the token and endpoint specified in your file and make sure there's no surrounding quotes or extra spaces. A 401 invalid token message occurs if the token in the request header includes the `@` symbol. For example, if the variable is `@token`, the reference in the request is simply `{{token}}`.
-
-If all else fails, restart your device to remove any cached tokens, and then repeat the steps in this section, starting with `az login`.
-
-## Additional configuration
-
-Configure a managed identity for outbound connections:
-
-- [Configure a system-assigned or user-assigned managed identity](search-howto-managed-identities-data-sources.md) for your search service.
-
-- [Use role assignments](keyless-connections.md) to authorize access to other Azure resources.
-
-Network access configuration:
-
-- [Set inbound rules](service-configure-firewall.md) to accept or reject requests to Azure AI Search based on IP address.
++ [Configure a managed identity in Azure AI Search](search-howto-managed-identities-data-sources.md)
++ [Connect your app to Azure AI Search using identities](keyless-connections.md)
++ [Configure network access and firewall rules for Azure AI Search](service-configure-firewall.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "RBAC接続のクイックスタートを大幅に改訂"
}
```

### Explanation
この変更は、`search-get-started-rbac.md` ファイルの大規模な改訂を示しています。15行が新たに追加され、154行が削除された結果、169の変更が行われました。主な変更内容は以下の通りです：

1. **タイトルと説明の変更**: ドキュメントのタイトルが「Quickstart: Keyless Connection」から「Quickstart: Connect to a search service」に変更され、説明も「APIキーからMicrosoft Entra IDとロールベースのアクセス制御（RBAC）に切り替える方法」から「RBACを使用してAzure AI Searchサービスに接続する方法」に更新されました。

2. **コンテンツの削減**: 元々の詳細な手順（Azureサブスクリプションやテナントの取得、RBACの構成、接続方法など）が大幅に削減され、ガイドラインがシンプルに整理されています。特に具体的な手順が短縮され、ユーザーが必要な手続きに迅速にアクセスできるようになっています。

3. **新しいゾーンの導入**: PythonおよびRESTのクイックスタートが追加され、ユーザーがそれぞれのプログラミング言語においてRBACを使用した接続方法を簡単に実装できるようになっています。

4. **メタデータの更新**: 新たに「ms.update-cycle: 90-days」が追加され、文書が90日ごとに見直される旨が明記されています。また、日付が01/07/2025から01/08/2025に更新されています。

この改訂は、Azure AI SearchにおけるRBACの導入を促進し、ユーザーがより効率的にサービスへアクセスできるようにすることを目的としています。しかしながら、大幅な内容削減はユーザーにとって重要な手順の見落としを招く可能性があるため、利用者は最新の情報に十分注意する必要があります。

## articles/search/search-get-started-semantic.md{#item-2b3902}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.custom:
   - devx-track-dotnet
   - devx-track-python
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティック検索のドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-get-started-semantic.md` ファイルに対する小規模な更新を示しています。1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 新しく「ms.update-cycle: 90-days」というメタデータが追加され、ドキュメントが90日ごとに見直されることを示しています。これにより、利用者は情報が定期的に更新されることを理解できるようになります。

この変更は、セマンティック検索に関するドキュメントの信頼性を向上させ、ユーザーに最新の情報を提供するための重要なステップです。全体として、内容の透明性が強化され、ユーザーに対する信頼感を高めることが期待されています。

## articles/search/search-get-started-skillset.md{#item-079744}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: quickstart
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スキルセットのドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-get-started-skillset.md` ファイルに対する小規模な更新を示しています。1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 新しく「ms.update-cycle: 180-days」というメタデータが追加され、ドキュメントが180日ごとに見直されることが示されています。これにより、利用者は情報が定期的に更新されることを理解できるようになります。

この変更は、スキルセットに関するドキュメントの透明性を高め、利用者が信頼性のある情報を得られるようにするための重要なステップです。全体として、更新周期の明示は、ユーザーに対する安心感を提供することが期待されます。

## articles/search/search-get-started-text.md{#item-935941}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.custom:
   - devx-track-dotnet
   - devx-track-extended-java
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト検索のドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-get-started-text.md` ファイルに対する小規模な更新を示しています。1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 新しく「ms.update-cycle: 90-days」というメタデータが追加され、ドキュメントが90日ごとに見直されることを示しています。これにより、利用者は情報が定期的に更新されることを理解できるようになります。

この変更は、テキスト検索に関するドキュメントの透明性を高め、ユーザーに信頼性のある情報を提供するための重要なステップです。全体として、更新周期の明示は、利用者に対する安心感を提供し、最新の情報を得られることに寄与すると期待されます。

## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ description: Learn how to call the Search REST and Azure SDK APIs for vector wor
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.custom:
   - ignite-2023
 ms.topic: quickstart
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-get-started-vector.md` ファイルに対する小規模な更新を示しています。1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 新しく「ms.update-cycle: 90-days」というメタデータが追加され、ドキュメントが90日ごとに見直されることを示しています。この追加により、利用者は情報が定期的に更新され、最新の内容が保たれることを認識できるようになります。

この変更は、ベクトル検索に関するドキュメントの透明性を高め、ユーザーに最新の情報を提供するための一歩です。全体として、更新周期の明示は、ユーザーへの信頼性を強化し、安心して情報を利用できるようにする役割を果たしています。

## articles/search/search-how-to-create-search-index.md{#item-c4ff31}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: how-to
 ms.date: 05/19/2025
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックス作成に関するドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-how-to-create-search-index.md` ファイルに対する小規模な更新を示しています。1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 新しく「ms.update-cycle: 180-days」というメタデータが追加され、ドキュメントが180日ごとに見直されることを示しています。この変更により、利用者はこのドキュメントが定期的に更新され、信頼性が保たれていることを理解できるようになります。

この更新は、検索インデックスの作成に関するガイドラインの透明性を高め、ユーザーに最新かつ関連性のある情報を提供するための重要な進展です。全体として、更新周期の明示は、ユーザーが信頼してこの情報を利用できるようになるための重要な要素となります。

## articles/search/search-how-to-load-search-index.md{#item-a72573}

<details>
<summary>Diff</summary>
````diff
@@ -8,6 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: how-to
 ms.date: 05/08/2025
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックス読み込みに関するドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-how-to-load-search-index.md` ファイルに対する小規模な更新を示しています。1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 新たに「ms.update-cycle: 180-days」というメタデータが追加され、このドキュメントが180日ごとに見直される旨が示されています。この変更により、利用者は情報が定期的に更新されていることを把握し、信頼性を感じられるようになります。

この更新は、検索インデックスの読み込みに関するドキュメントの透明性を高め、ユーザーに最新の情報を提供するための重要な進展です。全体として、更新周期の明示は、ユーザーがこの情報を活用する際の信頼性を向上させる重要な要素となります。

## articles/search/search-howto-indexing-azure-blob-storage.md{#item-dc4668}

<details>
<summary>Diff</summary>
````diff
@@ -27,6 +27,9 @@ To configure and run the indexer, you can use:
 
 This article uses the REST APIs to illustrate each step.
 
+> [!NOTE]
+> Azure AI Search can now ingest RBAC scope during indexing and transfers those permissions to indexed content in the search index. For more information about RBAC scope during indexing, see [Indexing Azure Role-Based Access Control scope using Indexers](search-blob-indexer-role-based-access.md).
+
 ## Prerequisites
 
 + [Azure Blob Storage](/azure/storage/blobs/storage-blobs-overview), Standard performance (general-purpose v2).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Blob Storage のインデックス作成に関するドキュメントに RBAC スコープのサポートを追加"
}
```

### Explanation
この変更は、`search-howto-indexing-azure-blob-storage.md` ファイルに対する小規模な更新を示しています。3行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **RBAC スコープのサポートについての注意書き**: 新しく「Azure AI Searchは、インデックス作成時にRBACのスコープを取り込み、検索インデックス内のインデックス化されたコンテンツにその権限を転送できます」という情報が追加されました。この更新により、RBACスコープのインデックス作成時の対応が明示され、ユーザーが権限を適切に設定できるようになります。

2. **関連リンクの追加**: RBAC スコープに関する追加情報を得るためのリンク「[Indexing Azure Role-Based Access Control scope using Indexers](search-blob-indexer-role-based-access.md)」も追加されており、ユーザーが詳しい情報に簡単にアクセスできるようになっています。

この変更によって、Azure Blob Storage のインデックス作成に関するドキュメントがより充実し、ユーザーが利用可能な機能に関する理解が深まることが期待されます。

## articles/search/search-indexer-access-control-lists-and-role-based-access.md{#item-67b42f}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,8 @@
 title: Use ADLS Gen2 indexer to ingest permission metadata
 titleSuffix: Azure AI Search  
 description: Learn how to configure Azure AI Search indexers for ingesting Access Control Lists (ACLs) and Azure Role-Based Access (RBAC) metadata on Azure Data Lake Storage (ADLS) Gen2 blobs.
-ms.service: azure-ai-search  
+ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: how-to
 ms.date: 05/08/2025  
 author: wlifuture
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ACL と RBAC メタデータのインジェストに関するドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-indexer-access-control-lists-and-role-based-access.md` ファイルに対する小規模な更新を示しています。2行が新たに追加され、1行が削除されました。主な変更点は以下の通りです：

1. **更新周期の追加**: ファイルに「ms.update-cycle: 90-days」が新たに追加され、ドキュメントが90日ごとに見直されることが示されています。この変更により、ユーザーはこの情報が定期的に更新されることを理解でき、より信頼性を感じることができます。

2. **メタデータの整理**: 既存の「ms.service: azure-ai-search」行のフォーマットが若干調整され、整合性が保たれています。

この更新は、Azure Data Lake Storage (ADLS) Gen2 のインデックス作成に関連するアクセス制御リスト (ACL) および Azureのロールベースのアクセス (RBAC) メタデータに関するドキュメントの透明性と信頼性を高めることを目的としています。全体として、ユーザーが権限管理に関する機能を理解する助けとなる重要な変更です。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.author: haileytapia
 manager: nitinme
 ms.date: 06/12/2025
 ms.service: azure-ai-search
+ms.update-cycle: 90-days
 ms.topic: conceptual
 ms.custom:
   - references_regions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search のドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-region-support.md` ファイルに対する小規模な更新を示しています。1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 90-days」が新たに追加され、ドキュメントが90日ごとに見直されることが明示されています。この情報により、ユーザーはこのドキュメントが定期的に更新されることを理解でき、より信頼感を持つことができます。

この変更は、Azure AI Search のサポート地域に関する情報を提供するドキュメントの透明性を高めることを目的としており、ユーザーに最新の情報が提供されることを保証しています。

## articles/search/search-security-overview.md{#item-6b3f1e}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search のセキュリティ概要ドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-security-overview.md` ファイルに対する小規模な更新を示しています。1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」が新たに追加され、このドキュメントが180日ごとに見直されることが明記されています。この情報によって、ユーザーはドキュメントが定期的に更新されることを把握し、信頼性を感じることができます。

この変更は、Azure AI Search のセキュリティに関する情報を提供するドキュメントの透明性を高め、ユーザーが最新のセキュリティ対策に関する情報を受け取れるようにしています。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ ms.author: heidist
 manager: nitinme
 ms.date: 03/31/2025
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: how-to
 ms.custom:
   - subject-rbac-steps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search のRBACセキュリティドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-security-rbac.md` ファイルに対する小規模な更新を示しています。1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」が新たに追加され、このドキュメントが180日ごとに見直されることが明確に示されています。この情報により、ユーザーはドキュメントが定期的に更新され、最新の情報が反映されることを確認することができます。

この変更は、Azure AI Search におけるロールベースのアクセス制御（RBAC）に関する情報を提供するドキュメントの透明性を高め、ユーザーが最新のやり方や手順にアクセスできるようにすることを目的としています。

## articles/search/search-security-trimming-for-azure-search.md{#item-d8ae51}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: how-to
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Search のセキュリティトリミングドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-security-trimming-for-azure-search.md` ファイルに対する小規模な更新を示しており、1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」が新たに追加され、このドキュメントが180日ごとに見直されることが明記されています。この追加によって、ユーザーはこのドキュメントが定期的に更新され、最新の情報が維持されることを理解できるようになります。

この変更は、Azure Search のセキュリティトリミングに関する情報を提供するドキュメントの透明性を高め、ユーザーが最新の手順や情報にアクセスできることを目指しています。

## articles/search/search-sku-manage-costs.md{#item-6e0122}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: how-to
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Search のSKU管理費用ドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-sku-manage-costs.md` ファイルに対する小規模な更新を示しており、1行が新たに追加されており、削除はありませんでした。主要な変更点は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」が新たに追加され、このドキュメントが定期的に（180日ごと）見直されることが示されています。これにより、ユーザーはドキュメントが最新の情報を反映するための定期的な更新が行われることを理解できます。

この変更は、Azure Search に関する費用管理方法に関する情報を提供するドキュメントの透明性を高め、ユーザーが常に最新の手順や情報にアクセスできるようにすることを目的としています。

## articles/search/search-try-for-free.md{#item-36e28d}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: conceptual
 ms.date: 06/11/2025
 ms.custom: references_regions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Search 無料試行ドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-try-for-free.md` ファイルに対する小規模な更新を示しており、1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」が新たに追加され、このドキュメントが定期的に（180日ごと）見直されることが記載されています。この追加により、ユーザーはドキュメントが最新の情報を常に反映するための更新が行われることを理解できるようになります。

この変更は、Azure Search の無料試行に関する情報を提供するドキュメントの透明性を向上させ、ユーザーが常に最新の手順や情報にアクセスできることを目指しています。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: overview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Searchとはのドキュメントに更新周期情報を追加"
}
```

### Explanation
この変更は、`search-what-is-azure-search.md` ファイルに対する小規模な更新を示しており、新たに1行が追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という行が新たに追加され、このドキュメントが180日ごとに見直されることが明記されています。これにより、ユーザーはこのドキュメントが定期的に更新され、常に最新の情報が提供されることを理解できます。

この変更は、Azure Search に関する基本的な情報を提供するドキュメントの透明性を高め、ユーザーが常に最新の知識や手続きを得られることを目的としています。

## articles/search/semantic-how-to-configure.md{#item-7a92a6}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: how-to
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティック検索の設定方法に更新周期情報を追加"
}
```

### Explanation
この変更は、`semantic-how-to-configure.md` ファイルに対する小規模な更新を示しており、1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」が新たに追加され、このドキュメントが180日ごとに見直されることが記載されています。この追加により、ユーザーは文書が定期的に更新され、最新の情報が提供されることを理解できるようになります。

この変更は、セマンティック検索の設定に関するドキュメントの透明性を向上させ、ユーザーが常に必要な最新情報を手に入れることを目的としています。

## articles/search/semantic-how-to-enable-disable.md{#item-71ac1e}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: how-to
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティック検索の有効化と無効化に更新周期情報を追加"
}
```

### Explanation
この変更は、`semantic-how-to-enable-disable.md` ファイルに対する小規模な更新を示しており、1行が新たに追加され、削除はありませんでした。主な変更点は次の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という行が新たに追加され、このドキュメントが180日ごとに見直されることが明記されています。これにより、ユーザーはドキュメントが定期的に更新され、最新の情報が反映されることを認識できるようになります。

この変更は、セマンティック検索の有効化と無効化に関するドキュメントの透明性を向上させ、ユーザーが常に最新の知識と手続きを得られることを目的としています。

## articles/search/semantic-how-to-enable-scoring-profiles.md{#item-e8d524}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ description: Learn how to combine scoring profiles with semantic ranking in Azur
 author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: how-to
 ms.date: 06/10/2025
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックスコアリングプロファイルの有効化に更新周期情報を追加"
}
```

### Explanation
この変更は、`semantic-how-to-enable-scoring-profiles.md` ファイルに対する小規模な更新を示しており、1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」が新たに追加され、このドキュメントが180日ごとに見直されることが記載されています。これにより、ユーザーは文書が定期的に更新され、最新の情報が保持されることを理解できるようになります。

この変更は、セマンティックスコアリングプロファイルの有効化に関するドキュメントの透明性を向上させ、ユーザーが常に最新の情報を持つことを助けることを目的としています。

## articles/search/semantic-how-to-query-request.md{#item-85530d}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
   - ignite-2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティッククエリリクエストに更新周期情報を追加"
}
```

### Explanation
この変更は、`semantic-how-to-query-request.md` ファイルに対する小規模な更新を示しており、1行が新たに追加され、削除はありませんでした。主な変更点は次の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という行が新たに追加され、このドキュメントが180日ごとに見直されることが示されています。これにより、ユーザーはドキュメントが定期的に更新され、新しい情報が反映される可能性があることを知ることができます。

この変更は、セマンティッククエリリクエストに関するドキュメントの信頼性を向上させ、ユーザーが常に最新の内容を得ることを促進することを目的としています。

## articles/search/semantic-how-to-query-rewrite.md{#item-3e168f}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: eric-urban
 ms.author: eur
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
   - references_regions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティッククエリーリライトに更新周期情報を追加"
}
```

### Explanation
この変更は、`semantic-how-to-query-rewrite.md` ファイルに対する小規模な更新を示しており、1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」が新たに追加され、このドキュメントが180日ごとに見直されることを示しています。これにより、ユーザーはこの文書が定期的に更新され、新しい情報が反映される可能性があることを知ることができます。

この変更は、セマンティッククエリーリライトに関するドキュメントの信頼性を向上させ、ユーザーが常に最新の情報にアクセスできるようにすることを目的としています。

## articles/search/semantic-search-overview.md{#item-b7497b}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティック検索の概要に更新周期情報を追加"
}
```

### Explanation
この変更は、`semantic-search-overview.md` ファイルに対する小規模な更新を示しており、1行が新たに追加され、削除はありませんでした。主な変更点は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という行が新たに追加され、このドキュメントが180日ごとに見直されることが示されています。この情報は、ユーザーがドキュメントが定期的に更新される期待を持つ手助けとなります。

この変更により、セマンティック検索に関するドキュメントの信頼性が高まり、ユーザーが最新の情報を得やすくなることを目的としています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -72,6 +72,8 @@ items:
       href: search-indexer-securing-resources.md
 - name: Quickstarts
   items:
+  - name: Connect to a search service
+    href: search-get-started-rbac.md
   - name: Agentic search
     href: search-get-started-agentic-retrieval.md
   - name: Vector search
@@ -84,8 +86,6 @@ items:
     href: search-get-started-semantic.md
   - name: Chat with your data
     href: /azure/ai-services/openai/use-your-data-quickstart?context=/azure/search/context/context
-  - name: Connect without keys
-    href: search-get-started-rbac.md
   - name: Azure portal
     items:
     - name: Create a search index
@@ -529,12 +529,14 @@ items:
         href: search-document-level-access-overview.md
       - name: Use security filters
         href: search-security-trimming-for-azure-search.md
-      - name: Use ACLs
+      - name: Use ACLs or RBAC scopes
         items:
         - name: Push document-level permissions to an index
           href: search-index-access-control-lists-and-rbac-push-api.md
         - name: Pull ADLS Gen2 permissions into an index
           href: search-indexer-access-control-lists-and-role-based-access.md
+        - name: Pull Blob RBAC scopes into an index
+          href: search-blob-indexer-role-based-access.md
         - name: Query with permission filters
           href: search-query-access-control-rbac-enforcement.md
     - name: Data encryption
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次に新しいセクションと項目を追加"
}
```

### Explanation
この変更は、`toc.yml` ファイルに対する小規模な更新を示し、5行が新たに追加され、3行が削除され、合計で8行の変更が行われました。主な変更点は次の通りです：

1. **新しい項目の追加**: 
   - 「Connect to a search service」に関連する新しい項目「Connect to a search service」が追加され、`search-get-started-rbac.md`にリンクされています。
   - 「Use ACLs」に関連するセクションに「Pull Blob RBAC scopes into an index」に関する新しい項目が追加され、`search-blob-indexer-role-based-access.md`にリンクされています。

2. **不要な項目の削除**: 
   - 「Connect without keys」という項目が削除され、関連するリンクも削除されています。これにより、ドキュメントの整合性が向上しています。

これらの変更により、目次が更新され、ユーザーは新しい情報および機能へのアクセスがより容易になります。また、リンクの整理により、全体的な使用体験も向上しています。

## articles/search/tutorial-adls-gen2-indexer-acls.md{#item-6881a0}

<details>
<summary>Diff</summary>
````diff
@@ -3,6 +3,7 @@ title: 'Tutorial: Index ADLS Gen2 permission metadata'
 titleSuffix: Azure AI Search  
 description: Learn how to index Access Control Lists (ACLs) and Azure Role-Based Access Control (RBAC) scope from ADLS Gen2 and query with permission-filtered results in Azure AI Search.
 ms.service: azure-ai-search  
+ms.update-cycle: 180-days
 ms.topic: tutorial  
 ms.date: 05/20/2025
 author: wlifuture
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ADLS Gen2 インデクサ ACLs チュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-adls-gen2-indexer-acls.md` ファイルに対する小規模な更新を示しており、1行が新たに追加され、削除はありませんでした。主な内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という行が新たに追加され、このチュートリアルが180日ごとに見直されることが示されています。この情報は、ユーザーがドキュメントが定期的に更新されるという期待を持つ助けとなります。

この変更により、ADLS Gen2に関するインデクサのACLsに関するチュートリアルの信頼性が向上し、ユーザーが最新の情報をもとに操作を行うことができるようになります。

## articles/search/tutorial-create-custom-analyzer.md{#item-ad5520}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ description: Learn how to build a custom analyzer to improve the quality of sear
 author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: tutorial
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムアナライザー作成チュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-create-custom-analyzer.md` ファイルに対する小規模な更新を示しており、1行が新たに追加され、削除はありませんでした。主な内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という行が新たに追加され、このチュートリアルが180日ごとに見直されることが明記されています。この情報は、ユーザーがチュートリアルの内容が定期的に更新されることに対する期待感を持つ手助けとなります。

この変更により、カスタムアナライザーに関するチュートリアルの信頼性と利用価値が向上し、ユーザーが最新の機能やベストプラクティスに基づいて学習できるようになります。

## articles/search/tutorial-csharp-create-load-index.md{#item-0a6ffd}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: diberry
 ms.author: diberry
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: tutorial
 ms.date: 01/17/2025
 ms.custom:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# インデックス作成と読み込みチュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-csharp-create-load-index.md` ファイルに対する小規模な更新を示しており、1行が新たに追加され、削除はありませんでした。主な内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という行が新たに追加され、このチュートリアルが180日ごとに見直されることが明記されています。この情報は、ユーザーがチュートリアルの内容が定期的に更新されるという信頼性を持つ助けとなります。

この変更により、C#を用いたインデックスの作成と読み込みに関するチュートリアルの有用性が向上し、ユーザーが最新の情報を得ることができるようになります。

## articles/search/tutorial-csharp-create-mvc-app.md{#item-608a5d}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.devlang: csharp
 ms.custom:
   - ignite-2023
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# MVC アプリ作成チュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-csharp-create-mvc-app.md` ファイルに対する小規模な更新を示しており、1行が新たに追加され、削除はありませんでした。主な内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という行が新たに追加され、このチュートリアルが180日ごとに見直されることが明記されています。この情報は、ユーザーがチュートリアルの信頼性を感じ、情報が定期的に更新されることを理解するのに役立ちます。

この変更により、C#を使用したMVCアプリケーションの作成に関するチュートリアルの質と有用性が向上し、ユーザーが最新の情報を得やすくなります。

## articles/search/tutorial-csharp-deploy-static-web-app.md{#item-a2300f}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: diberry
 ms.author: diberry
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: tutorial
 ms.date: 01/17/2025
 ms.custom:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# 静的 Web アプリのデプロイチュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-csharp-deploy-static-web-app.md` ファイルに対する小規模な更新であり、1行が追加され、削除はありませんでした。主な内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という行が新たに追加され、ユーザーに対してこのチュートリアルが180日ごとに見直されることが明記されています。この情報は、チュートリアルが信頼できるものであり、定期的に最新の情報にアップデートされることを示します。

この変更により、C#を使用した静的Webアプリケーションのデプロイに関するチュートリアルの有用性が高まり、ユーザーが常に最新の手順を確認することができるようになります。

## articles/search/tutorial-csharp-overview.md{#item-57fa0d}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: diberry
 ms.author: diberry
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: tutorial
 ms.date: 01/17/2025
 ms.custom:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# 概要チュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-csharp-overview.md` ファイルに対する小規模な更新であり、1行が追加され、削除はありませんでした。具体的には、以下の点が挙げられます：

1. **更新周期の追加**: 新たに「ms.update-cycle: 180-days」という行が追加され、このチュートリアルが180日ごとに見直されることが明記されています。このことで、ユーザーはチュートリアルの信頼性や最新性を理解しやすくなります。

この変更により、C#に関する概要チュートリアルがさらに質の高い情報を提供するものであることが確認でき、ユーザーは定期的な更新に基づいて学習を進めることができるようになります。

## articles/search/tutorial-csharp-search-query-integration.md{#item-8ad6b5}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: diberry
 ms.author: diberry
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: tutorial
 ms.date: 01/21/2025
 ms.custom:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# 検索クエリ統合チュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-csharp-search-query-integration.md` ファイルにおける小規模な更新であり、新たに1行が追加され、削除はありませんでした。主なポイントは以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という行が新たに導入され、このチュートリアルが180日ごとに見直されることが示されました。これにより、ユーザーはこのチュートリアルが定期的に更新され、最新の情報を反映していることを認識できます。

この追加情報により、C#を用いた検索クエリ統合に関するチュートリアルの信頼性が向上し、ユーザーは定期的に見直される内容を確認しながら学習を進めることができるようになります。

## articles/search/tutorial-document-extraction-image-verbalization.md{#item-398a90}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: arjagann
 author: mdonovan
 ms.author: mdonovan
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
 ms.topic: tutorial
 ms.date: 05/29/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント抽出と画像の言語化チュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-document-extraction-image-verbalization.md` ファイルに対する小規模な更新で、追加された行は1行であり、削除はありませんでした。具体的には以下の要点があります：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という項目が追加され、このチュートリアルが180日ごとに見直されることが示されています。この追加により、ユーザーはチュートリアルの最新性を把握しやすくなります。

この変更によって、ドキュメントからの情報抽出や画像の言語化に関連するチュートリアルがより信頼性の高いものとなり、ユーザーが最新の情報を活用しながら学習を行うことができるようになります。

## articles/search/tutorial-document-extraction-multimodal-embeddings.md{#item-a3db59}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: arjagann
 author: mdonovan
 ms.author: mdonovan
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
 ms.topic: tutorial
 ms.date: 06/11/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダル埋め込みのドキュメント抽出チュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-document-extraction-multimodal-embeddings.md` ファイルに対する小規模な更新であり、1行が追加され、削除はありませんでした。具体的な内容は以下のとおりです：

1. **更新周期の追加**: 新たに「ms.update-cycle: 180-days」という行が追加され、このチュートリアルが180日ごとに見直されることを示しています。この情報により、ユーザーはこのチュートリアルが継続的に更新され、最新の情報を保持していることを理解できます。

この変更により、マルチモーダル埋め込みに関するドキュメント抽出のチュートリアルの信頼性が向上し、ユーザーは進捗を確認しながら安心して学習を続けることができるようになります。

## articles/search/tutorial-document-layout-image-verbalization.md{#item-f5de57}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: arjagann
 author: rawan    
 ms.author: rawan
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
 ms.topic: tutorial
 ms.date: 05/29/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレイアウトと画像の言語化チュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-document-layout-image-verbalization.md` ファイルに対する小規模な更新であり、1行が追加され、削除はありませんでした。主な内容は次の通りです：

1. **更新周期の追加**: 新たに「ms.update-cycle: 180-days」という行が追加され、このチュートリアルが180日ごとに見直されることを示しています。これにより、ユーザーはこのチュートリアルが定期的に更新されることを理解しやすくなります。

この変更により、ドキュメントレイアウトと画像の言語化に関するチュートリアルがより信頼性の高いものとなり、ユーザーが常に最新の情報を活用しながら学習を進めることができるようになります。

## articles/search/tutorial-document-layout-multimodal-embeddings.md{#item-f67371}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: arjagann
 author: rawan
 ms.author: rawan
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
 ms.topic: tutorial
 ms.date: 06/11/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダル埋め込みのドキュメントレイアウトチュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-document-layout-multimodal-embeddings.md` ファイルに対する小規模な更新であり、1行が追加され、削除はありませんでした。具体的には以下の内容が変更されています：

1. **更新周期の追加**: 新たに「ms.update-cycle: 180-days」という行が追加され、チュートリアルが180日ごとに見直されることを示しています。この情報は、ユーザーに対してチュートリアルが定期的に更新されることを知らせ、信頼性を高めます。

この小さな変更により、マルチモーダル埋め込みに関するドキュメントレイアウトのチュートリアルがより充実し、ユーザーは常に新しい情報を得ることができる環境が整えられます。

## articles/search/tutorial-multiple-data-sources.md{#item-71558f}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: tutorial
 ms.date: 03/28/2025
 ms.custom:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "複数データソースのチュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-multiple-data-sources.md` ファイルに対する小規模な更新で、1行が追加され、削除はありませんでした。具体的には以下の内容が変更されています：

1. **更新周期の追加**: 新たに「ms.update-cycle: 180-days」という行が追加され、チュートリアルが180日ごとに見直されることを示しています。この追加により、ユーザーは情報が定期的に更新されることを理解しやすくなり、信頼性が向上します。

この変更は、複数のデータソースに関するチュートリアルをより充実させ、ユーザーが常に最新の情報を得られるように助けることを目的としています。

## articles/search/tutorial-optimize-indexing-push-api.md{#item-ef0e96}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ description: Learn how to efficiently index data using Azure AI Search's push AP
 author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: tutorial
 ms.date: 03/28/2025
 ms.custom:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクシングプッシュAPIの最適化チュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-optimize-indexing-push-api.md` ファイルに対する小規模な更新であり、1行が追加され、削除はありませんでした。具体的には以下の内容が追加されています：

1. **更新周期の追加**: 新たに「ms.update-cycle: 180-days」という行が追加され、インデクシングプッシュAPIに関するチュートリアルが180日ごとに見直されることを示しています。この更新により、ユーザーはこのドキュメントが定期的に更新されることで信頼性が高まることを理解できるようになります。

この小さな変更は、Azure AI Search におけるデータの効率的なインデクシングのチュートリアルをより信頼性のあるものとし、ユーザーに常に最新の情報を提供することを目指しています。

## articles/search/tutorial-rag-build-solution-index-schema.md{#item-9a17ca}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: tutorial
 ms.date: 05/29/2025
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューション構築のインデックススキーマチュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-rag-build-solution-index-schema.md` ファイルに対する小規模な更新で、1行が追加され、削除はありませんでした。以下の内容が新たに追加されています：

1. **更新周期の追加**: 新しく「ms.update-cycle: 180-days」と記述され、RAGソリューションのインデックススキーマに関するチュートリアルが180日ごとに見直されることを示しています。この追加は、ユーザーがこのドキュメントの更新頻度を理解しやすくし、情報の信頼性を高める役割を果たします。

この変更により、ユーザーは最新の内容を反映したチュートリアルを利用できることが保証され、Azure AI Searchにおけるインデクシングのベストプラクティスについての理解がさらに深まることを目指しています。

## articles/search/tutorial-rag-build-solution-maximize-relevance.md{#item-2fdb09}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: tutorial
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションの関連性最大化チュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-rag-build-solution-maximize-relevance.md` ファイルに対する小規模な更新であり、1行が追加されているものの、削除はありません。追加された内容は以下の通りです：

1. **更新周期の追加**: 新たに「ms.update-cycle: 180-days」という行が追加され、RAGソリューションにおける関連性最大化のチュートリアルが180日ごとに見直されることを示しています。この情報は、ユーザーに対してこのドキュメントの更新頻度を明確にし、信頼性を向上させる助けとなります。

この更新により、Azure AI Search の関連性を最大化するための最新の情報を提供する意義が強調され、ユーザーの理解を深めることが期待されます。

## articles/search/tutorial-rag-build-solution-minimize-storage.md{#item-088ad8}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: tutorial
 ms.date: 02/05/2025
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションのストレージ最適化チュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-rag-build-solution-minimize-storage.md` ファイルに対する小規模な更新であり、1行が追加され、削除はありませんでした。以下の内容が新たに追加されています：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、RAGソリューションのストレージを最小化するためのチュートリアルが180日ごとに見直されることを示しています。この追加は、ユーザーにこのドキュメントの更新頻度を知らせ、情報の新鮮さを維持することの重要性を強調します。

この変更により、Azure AI Searchにおけるストレージ最適化のベストプラクティスに関する情報が、最新の状態で提供されることが確保され、ユーザーの理解を深めることが目的とされています。

## articles/search/tutorial-rag-build-solution-models.md{#item-6796c9}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: tutorial
 ms.custom: references_regions
 ms.date: 06/11/2025
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションのモデルに関するチュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-rag-build-solution-models.md` ファイルに対する小規模な更新で、1行が追加され、削除はありません。追加された内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、RAGソリューションのモデルに関するチュートリアルが180日ごとに見直されることを示しています。この情報は、ユーザーに対してドキュメントの更新頻度を明示し、内容の新鮮さを確保することが重要であることを伝えています。

この変更により、Azure AI Searchのモデルに関する情報が最新の状態で保たれ、ユーザーが信頼できる情報を得ることができるようになることが期待されます。

## articles/search/tutorial-rag-build-solution-pipeline.md{#item-25ce01}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: tutorial
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションのパイプラインに関するチュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-rag-build-solution-pipeline.md` ファイルに対する小規模な更新であり、1行が追加され、削除はありません。新たに追加された内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、RAGソリューションのパイプラインに関するチュートリアルが180日ごとに見直されることが示されました。この情報は、ユーザーに対してドキュメントの更新頻度を通知し、提供される情報の正確性と新鮮さを維持することを目的としています。

この変更により、Azure AI Searchにおけるパイプラインの使用に関する情報が最新の状態で提供され、ユーザーが信頼できる情報を手に入れることができるようになることが期待されています。

## articles/search/tutorial-rag-build-solution-query.md{#item-93965f}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: tutorial
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションのクエリに関するチュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-rag-build-solution-query.md` ファイルに対する小規模な更新で、1行が追加され、削除はありません。追加された内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、RAGソリューションのクエリに関するチュートリアルが180日ごとに見直されることを示しています。この新たな情報は、ドキュメントの更新頻度をユーザーに通知し、内容の信頼性と有用性を高めることを目的としています。

この変更によって、Azure AI Searchにおけるクエリの使用に関する情報が最新の状態で保たれ、ユーザーが適切な情報を得られるようになることが期待されています。

## articles/search/tutorial-rag-build-solution.md{#item-c7eca4}

<details>
<summary>Diff</summary>
````diff
@@ -7,6 +7,7 @@ manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: overview
 ms.date: 05/29/2025
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションに関するチュートリアルに更新周期情報を追加"
}
```

### Explanation
この変更は、`tutorial-rag-build-solution.md` ファイルに対する小規模な更新で、1行が追加され、削除はありません。追加された内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、RAGソリューションに関するチュートリアルが180日ごとに見直されることを示しています。この変更は、ユーザーに対してドキュメントの更新頻度を明示し、情報の正確性と信頼性を向上させることを目的としています。

この変更により、Azure AI Searchに関連するRAGソリューションのチュートリアルが最新の情報を反映し、ユーザーが適切な知識獲得ができるようになることが期待されています。

## articles/search/vector-search-filters.md{#item-f47c2b}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ description: Explains prefilters and post-filters in vector queries, and how fil
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: how-to
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索フィルターに関する記事に更新周期情報を追加"
}
```

### Explanation
この変更は、`vector-search-filters.md` ファイルに対する小規模な更新で、1行が追加され、削除はありません。追加された内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、ベクトルクエリにおけるプリフィルターとポストフィルターに関する記事が180日ごとに見直されることを示しています。この情報は、ユーザーがドキュメントの更新頻度を把握できるようにすることで、内容の信頼性を高めることを目的としています。

この変更によって、Azure AI Searchにおけるベクトル検索フィルターの関連情報が常に最新の状態に保たれ、ユーザーが正確な情報を得られるようになることが期待されています。

## articles/search/vector-search-how-to-assign-narrow-data-types.md{#item-6b81cd}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ description: In vector search, assign narrow data types to vector fields to redu
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: how-to
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のデータ型割り当てに関する記事に更新周期情報を追加"
}
```

### Explanation
この変更は、`vector-search-how-to-assign-narrow-data-types.md` ファイルに対する小規模な更新で、1行が追加され、削除はありません。追加された内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、ベクトル検索における狭いデータ型の割り当てに関する記事が180日ごとに見直されることを示しています。この情報は、読者に対してドキュメントの更新頻度を明確にすることで、内容の正確性と信頼性を向上させることを目的としています。

この変更により、Azure AI Searchに関連するベクトル検索のデータ型に関する知識が常に最新の情報で提供されることを期待されています。ユーザーは、適切な指導と情報を得ることができるでしょう。

## articles/search/vector-search-how-to-chunk-documents.md{#item-b79133}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ description: Learn strategies for chunking PDFs, HTML files, and other large doc
 author: arv100kri
 ms.author: arjagann
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントのチャンク化に関する記事に更新周期情報を追加"
}
```

### Explanation
この変更は、`vector-search-how-to-chunk-documents.md` ファイルに対する小規模な更新で、1行が追加され、削除はありません。追加された内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、PDFやHTMLファイルなどの大きなドキュメントをチャンク化するための戦略に関する記事が180日ごとに見直されることを示しています。この情報は、記事の内容が定期的に更新されることを読者に通知し、情報の信頼性を向上させる目的があります。

この変更によって、Azure AI Searchにおけるドキュメントチャンク化に関する最新の知識が提供され、ユーザーが効果的な方法を学ぶ機会が広がることが期待されています。

## articles/search/vector-search-how-to-configure-compression-storage.md{#item-c653c3}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ description: Learn about the vector compression options in Azure AI Search, and
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: how-to
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "圧縮ストレージの設定に関する記事に更新周期情報を追加"
}
```

### Explanation
この変更は、`vector-search-how-to-configure-compression-storage.md` ファイルに対する小規模な更新で、1行が追加され、削除はありません。追加された内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、Azure AI Searchにおけるベクトル圧縮のオプションに関する記事が180日ごとに見直されることを示しています。この情報は、ユーザーが記事の内容が定期的に更新されることを認識できるようにし、最新の情報を提供することを目的としています。

この変更によって、ユーザーは圧縮ストレージの設定に関する最新の情報を得ることで、より効果的にAzure AI Searchを活用できるようになることが期待されています。

## articles/search/vector-search-how-to-configure-vectorizer.md{#item-30ffd8}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ description: Steps for adding a vectorizer to a search index in Azure AI Search.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - build-2024
 ms.topic: how-to
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトライザー設定に関する記事に更新周期情報を追加"
}
```

### Explanation
この変更は、`vector-search-how-to-configure-vectorizer.md` ファイルに対する小規模な更新で、1行が追加されており、削除はありません。追加された内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、Azure AI Searchにおける検索インデックスにベクトライザーを追加する手順に関する記事が180日ごとに見直されることを示しています。この情報は、記事の内容が定期的に更新されることを読者に伝え、情報の信頼性を高めることを目的としています。

この変更により、ユーザーはベクトライザーの設定に関する最新の情報を得られるため、Azure AI Searchの活用方法をさらに効果的に学ぶことができると期待されます。

## articles/search/vector-search-how-to-create-index.md{#item-97c769}

<details>
<summary>Diff</summary>
````diff
@@ -6,17 +6,20 @@ description: Create or update a search index to include vector fields.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 06/20/2025
+ms.date: 07/07/2025
 ---
 
 # Create a vector index
 
-In Azure AI Search, you can store vectors in a search index and send vector queries for matching based on semantic similarity. A vector index is defined by an index schema that has vector fields, nonvector fields, and a vector configuration section.
+In Azure AI Search, you can use [Create or Update Index (REST API)](/rest/api/searchservice/indexes/create-or-update) to store vectors in a search index. A vector index is defined by an index schema that has vector fields, nonvector fields, and a vector configuration section.
 
-The [Create or Update Index](/rest/api/searchservice/indexes/create-or-update) REST API creates the vector index. To index vectors in Azure AI Search, follow these steps:
+When you create a vector index, you implicitly create an *embedding space* that serves as the corpus for vector queries. The embedding space consists of all vector fields populated with embeddings from the same embedding model. At query time, the system compares the vector query to the indexed vectors, returning results based on semantic similarity.
+
+To index vectors in Azure AI Search, follow these steps:
 
 > [!div class="checklist"]
 > + Start with a basic schema definition.
@@ -99,8 +102,8 @@ A vector configuration includes:
 
 [**2024-07-01**](/rest/api/searchservice/search-service-api-versions#2024-07-01) is generally available. It supports a vector configuration that has:
 
-+ Hierarchical navigable small world (HNSW) algorithm.
-+ Exhaustive k-nearest neighbor (KNN) algorithm.
++ Hierarchical Navigable Small World (HNSW) algorithm.
++ Exhaustive K-Nearest Neighbor (KNN) algorithm.
 + Scalar compression.
 + Binary compression, which is available in 2024-07-01 only and in newer Azure SDK packages.
 + Oversampling.
@@ -185,7 +188,7 @@ Be sure to have a strategy for [vectorizing your content](vector-search-how-to-g
 
    + `vectorSearch.compressions.scalarQuantizationParameters.quantizedDataType` must be set to `int8`. This is the only primitive data type supported at this time. This property is optional. Default is `int8`.
 
-   + `vectorSearch.algorithms` is either `hnsw` or `exhaustiveKnn`. These are the approximate nearest neighbors (ANN) algorithms used to organize vector content during indexing.
+   + `vectorSearch.algorithms` is either `hnsw` or `exhaustiveKnn`. These are the Approximate Nearest Neighbors (ANN) algorithms used to organize vector content during indexing.
 
    + `vectorSearch.algorithms.m` is the bi-directional link count. Default is 4. The range is 4 to 10. Lower values should return less noise in the results.
 
@@ -269,7 +272,7 @@ Preview and stable API versions support the same `vectorSearch` configurations.
 
    + `vectorSearch.compressions.scalarQuantizationParameters.quantizedDataType` must be set to `int8`. This is the only primitive data type supported at this time. This property is optional. Default is `int8`.
 
-   + `vectorSearch.algorithms.kind` is either `hnsw` or `exhaustiveKnn`. These are the approximate nearest neighbors (ANN) algorithms used to organize vector content during indexing.
+   + `vectorSearch.algorithms.kind` is either `hnsw` or `exhaustiveKnn`. These are the Approximate Nearest Neighbors (ANN) algorithms used to organize vector content during indexing.
 
    + `vectorSearch.algorithms.m` is the bi-directional link count. Default is 4. The range is 4 to 10. Lower values should return less noise in the results.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス作成に関する記事の内容を更新"
}
```

### Explanation
この変更は、`vector-search-how-to-create-index.md` ファイルに対する小規模な更新で、10行が追加され、7行が削除され、合計で17行の変更が行われました。主な内容の変更点は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、記事が180日ごとに更新されることが明記されました。

2. **日付の更新**: 「ms.date」の値が「06/20/2025」から「07/07/2025」へ変更され、記事の最新の更新日が反映されました。

3. **API説明の改良**: Azure AI Searchのインデックス作成に関する段落が改善され、具体的に「Create or Update Index (REST API)」を用いてベクトルを検索インデックスに保存することが明記されました。また、埋め込み空間の概念が追加され、ベクトルクエリにおける重要性が強調されています。

4. **用語の整合性**: 「HNSW」や「KNN」などのアルゴリズム名が大文字表記に統一され、技術用語の正確性が向上しました。

5. **内容の明確化**: インデックス作成手順やベクトル設定に関する説明がさらに具体的になり、例や対象のパラメータが整理されました。

この変更により、ユーザーはインデックス作成のプロセスに関するより明確で詳細なガイダンスを受けることができ、Azure AI Searchの機能をより効果的に利用できることが期待されます。

## articles/search/vector-search-how-to-generate-embeddings.md{#item-e98f7b}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ description: Learn how to generate embeddings for downstream indexing into an Az
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: how-to
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "埋め込み生成に関する記事に更新周期情報を追加"
}
```

### Explanation
この変更は、`vector-search-how-to-generate-embeddings.md` ファイルに対する小規模な更新で、1行が追加され、削除はありません。追加された内容は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、埋め込み生成に関する記事が180日ごとに見直されることを示しています。この情報は、読者に対して記事の内容が定期的に更新され、最新の情報が反映されることを保証します。

この変更により、ユーザーは埋め込み生成に関する最新の情報を得ることができ、Azure AI Searchの機能を効果的に活用できることが期待されます。

## articles/search/vector-search-how-to-index-binary-data.md{#item-b233b9}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ description: Explains how to configure fields for binary vectors and the vector
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - build-2024
   - ignite-2024
@@ -48,7 +49,7 @@ Vector search algorithms are used to create the query navigation structures duri
 
 1. In the index schema, add a `vectorSearch` section that specifies profiles and algorithms.
 
-1. Add one or more [vector search algorithms](vector-search-ranking.md) that have a similarity metric of `hamming`. It's common to use Hierarchical Navigable Small Worlds (HNSW), but you can also use Hamming distance with exhaustive K-nearest neighbors.
+1. Add one or more [vector search algorithms](vector-search-ranking.md) that have a similarity metric of `hamming`. It's common to use Hierarchical Navigable Small Worlds (HNSW), but you can also use Hamming distance with exhaustive K-Nearest Neighbors (KNN).
 
 1. Add one or more vector profiles that specify the algorithm.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バイナリデータインデックスに関する記事の内容を更新"
}
```

### Explanation
この変更は、`vector-search-how-to-index-binary-data.md` ファイルの小規模な更新で、2行が追加され、1行が削除され、合計3行の変更が行われました。主な変更点は次の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、記事が180日ごとに見直されることを示す情報が明記されました。これにより、読者は記事が定期的に更新され、最新の情報が提供されることを理解できます。

2. **用語の整合性**: 箇条書きの中の「KNN」という略称が「K-Nearest Neighbors」と完全な形で表記されるように修正され、用語の正確性が向上しました。

3. **文言の追加**: バイナリデータのインデックス作成に関する手順の一部が明確にされ、情報が整理されてより理解しやすくなりました。

この変更は、ユーザーがバイナリデータをインデックスするための方法についての理解を深め、Azure AI Searchの機能を効果的に利用するための助けとなることが期待されます。

## articles/search/vector-search-how-to-quantization.md{#item-744f48}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ description: Configure built-in scalar or quantization for compressing vectors o
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: how-to
@@ -33,7 +34,7 @@ To use built-in quantization, follow these steps:
 
 ## Prerequisites
 
-- [Vector fields in a search index](vector-search-how-to-create-index.md), with a `vectorSearch` configuration specifying either the Hierarchical Navigable Small Worlds (HNSW) or exhaustive K-nearest neighbor (eKNN) algorithm, and a new vector profile.
+- [Vector fields in a search index](vector-search-how-to-create-index.md), with a `vectorSearch` configuration specifying either the Hierarchical Navigable Small Worlds (HNSW) or exhaustive K-Nearest Neighbor (KNN) algorithm, and a new vector profile.
 
 ## Supported quantization techniques
 
@@ -60,7 +61,7 @@ API versions determine which rescoring behavior is operational for your code. Th
 | [2024-11-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true) | Scalar and binary quantization on HNSW graphs | `rescoringOptions.enableRescoring` and `rescoreStorageMethod.preserveOriginals` |
 | [2025-03-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true) | Binary quantization on HNSW graphs | Previous parameter combinations are still supported but binary quantization can now be rescored if original embeddings are deleted: `rescoringOptions.enableRescoring` and `rescoringOptions.rescoreStorageMethod=discardOriginals` |
 
-Only HNSW graphs allow rescoring. Exhaustive K Nearest Neighbors (eKNN) doesn't support rescoring.
+Only HNSW graphs allow rescoring. Exhaustive KNN doesn't support rescoring.
 
 <!-- - In version 2024-11-01-preview, set `rescoringOptions.enableRescoring` and `rescoreStorageMethod.preserveOriginals`
 - In version 2025-03-01-preview, set `rescoringOptions.enableRescoring` and `rescoringOptions.rescoreStorageMethod=preserveOriginals` for scalar or binary quantization, or `rescoringOptions.enableRescoring` and `rescoringOptions.rescoreStorageMethod=discardOriginals` for binary quantization only -->
@@ -300,7 +301,7 @@ POST https://[servicename].search.windows.net/indexes?api-version=2025-03-01-pre
 
 ## Add the vector search algorithm
 
-You can use HNSW algorithm or exhaustive KNN in the 2024-11-01-preview REST API or later. For the stable version, use HNSW only. If you want rescoring, you must choose HNSW.
+You can use the HNSW or eKNN algorithm in the 2024-11-01-preview REST API or later. For the stable version, use HNSW only. If you want rescoring, you must choose HNSW.
 
    ```json
    "vectorSearch": {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "量子化に関する記事に更新情報と用語の整合性を追加"
}
```

### Explanation
この変更は、`vector-search-how-to-quantization.md` ファイルに対する小規模な更新で、4行が追加され、3行が削除され、合計7行の変更が行われました。主な変更点は次の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、記事の内容が180日ごとに見直されることを示しています。これにより、読者は最新の情報が提供されることを期待できるようになります。

2. **用語の整合性**: 箇条書きの中で、「K-Nearest Neighbor」という用語の略称が一貫して「KNN」と表記されるように修正され、読みやすさが向上しました。

3. **文言の明確化**: HNSWアルゴリズムやeKNNに関する説明が若干変更され、文書がより明確で理解しやすくなりました。

4. **テクニカルな詳細の更新**: APIバージョンに関連する情報や、量子化に関する支持技術もいくつか整理され、誤解を招かないような表現に訂正されました。

この変更は、ユーザーが量子化技術を理解し、Azure AI Searchの機能を効果的に活用するために役立つことが期待されます。

## articles/search/vector-search-how-to-query.md{#item-9bb93c}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ description: Learn how to build queries for vector search.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - build-2024
 ms.topic: how-to
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクター検索クエリ構築に関する記事に更新周期を追加"
}
```

### Explanation
この変更は、`vector-search-how-to-query.md` ファイルに対する小規模な更新で、1行が追加され、削除はありません。具体的な変更点は次の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、この記事が180日ごとに見直されることが示されています。これにより、読者はこの情報が定期的に更新されていることを理解でき、最新の技術やベストプラクティスが提供されることを期待できます。

この修正は、Azure AI Searchのベクター検索クエリの構築に関する記事の信頼性を高めるものであり、ユーザーが常に最新の情報を参照できるようにするための重要な一歩です。

## articles/search/vector-search-how-to-storage-options.md{#item-ee1680}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ description: In vector search, configure storage to exclude optional copies of v
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: how-to
@@ -20,7 +21,7 @@ Removing storage is irreversible and requires reindexing if you want it back.
 
 ## Prerequisites
 
-- [Vector fields in a search index](vector-search-how-to-create-index.md), with a `vectorSearch` configuration specifying either the Hierarchical Navigable Small Worlds (HNSW) or exhaustive K-nearest neighbor (KNN) algorithm, and a new vector profile.
+- [Vector fields in a search index](vector-search-how-to-create-index.md), with a `vectorSearch` configuration specifying either the Hierarchical Navigable Small Worlds (HNSW) or exhaustive K-Nearest Neighbor (KNN) algorithm, and a new vector profile.
 
 ## How vector fields are stored
 
@@ -30,7 +31,7 @@ For every vector field, there are up to three copies of the vectors, each servin
 |----------|-------|------------------|
 | Source vectors received during document indexing (JSON data) | Used for incremental data refresh with `merge` or `mergeOrUpload` indexing action. Also used to return "retrievable" vectors in the query response. | `stored` property on vector fields |
 | Original full-precision vectors (binary data) | Used for internal index operations and for exhaustive KNN search in older API versions. For compressed vectors, it's also used for `preserveOriginals` rescoring on an oversampled candidate set of results from ANN search. This applies to vector fields that undergo [scalar or binary quantization](vector-search-how-to-quantization.md). | `rescoringOptions.rescoreStorageMethod` property in `vectorSearch.compressions`. |
-| Vectors in the [HNSW graph for Approximate Nearest Neighbors (ANN) search](vector-search-overview.md) (HNSW graph) or vectors for exhaustive K Nearest Neighbors (eKNN index) | Used for query execution. Consists of either full-precision vectors (when no compression is applied) or quantized vectors. | Essential. There are no parameters for removing this instance. |
+| Vectors in the [HNSW graph for Approximate Nearest Neighbors (ANN) search](vector-search-overview.md) (HNSW graph) or vectors for exhaustive K-Nearest Neighbors (eKNN index) | Used for query execution. Consists of either full-precision vectors (when no compression is applied) or quantized vectors. | Essential. There are no parameters for removing this instance. |
 
 You can set properties that permanently discard the first two instances (JSON data and binary data) from vector storage, but not the last instance.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクター検索ストレージオプションに関する記事に更新周期と用語の整合性を追加"
}
```

### Explanation
この変更は、`vector-search-how-to-storage-options.md` ファイルに対する小規模な更新で、3行が追加され、2行が削除され、合計5行の変更が行われました。主な変更点は次の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、この記事が180日ごとに見直されることが示されています。これにより、情報が定期的に更新され、読者が最新のベストプラクティスを参照できるようになります。

2. **用語の整合性**: K-NNアルゴリズムに関する記述が「K-Nearest Neighbor」と一貫して表記されるように修正され、読みやすさが向上しました。

3. **内容の明確化**: ベクターが保持される方法やストレージオプションに関する説明が明確に整頓され、特にHNSWグラフやK-Nearest Neighborsに関する文言が改善されました。

この更新は、Azure AI Searchのベクター検索におけるストレージオプションをより効果的に理解し、利用するための重要な情報を提供することを目的としています。

## articles/search/vector-search-how-to-truncate-dimensions.md{#item-8350a3}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ description: Truncate dimensions on text-embedding-3 models using Matryoshka Rep
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: how-to
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト埋め込みモデルの次元を切り捨てる方法に関する記事に更新周期を追加"
}
```

### Explanation
この変更は、`vector-search-how-to-truncate-dimensions.md` ファイルに対する小規模な更新で、1行が追加され、削除はありません。具体的な変更点は次の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、この記事が180日ごとに見直されることが示されています。この情報により、読者はこのガイドが定期的に更新されていることを認識し、常に最新の技術情報を参照できることが保証されます。

この修正により、Azure AI Searchにおけるテキスト埋め込みモデルの次元を切り捨てる方法に関する記事の情報の信頼性が向上し、ユーザーが最新の手法を利用できるようになります。

## articles/search/vector-search-index-size.md{#item-bb2846}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ description: Explanation of the factors affecting the size of a vector index.
 author: robertklee
 ms.author: robertlee
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - build-2024
   - ignite-2024
@@ -24,7 +25,7 @@ For each vector field, Azure AI Search constructs an internal vector index using
 > [Vector optimization techniques](vector-search-how-to-configure-compression-storage.md) are now generally available. Use capabilities like narrow data types, scalar and binary quantization, and elimination of redundant storage to reduce your vector quota and storage quota consumption.
 
 > [!NOTE]
-> Not all algorithms consume vector index size quota. Vector quotas are established based on memory requirements of approximate nearest neighbor search. Vector fields created with the Hierarchical Navigable Small World (HNSW) algorithm need to reside in memory during query execution because of the random-access nature of graph-based traversals. Vector fields using exhaustive KNN algorithm are loaded into memory dynamically in pages during query execution, and as a result do not consume vector quota.
+> Not all algorithms consume vector index size quota. Vector quotas are established based on memory requirements of Approximate Nearest Neighbor (ANN) search. Vector fields created with the Hierarchical Navigable Small World (HNSW) algorithm need to reside in memory during query execution because of the random-access nature of graph-based traversals. Vector fields using the exhaustive K-Nearest Neighbors (KNN) algorithm are loaded into memory dynamically in pages during query execution, and as a result do not consume vector quota.
 
 ## Key points about quota and vector index size
 
@@ -178,7 +179,7 @@ The storage size of one vector is determined by its dimensionality. Multiply the
 
 ### Memory overhead from the selected algorithm  
   
-Every approximate nearest neighbor (ANN) algorithm generates extra data structures in memory to enable efficient searching. These structures consume extra space within memory.  
+Every ANN algorithm generates extra data structures in memory to enable efficient searching. These structures consume extra space within memory.  
   
 **For the HNSW algorithm, the memory overhead ranges between 1% and 20% for uncompressed float32 (Edm.Single) vectors.**  
   
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクターインデックスサイズに関する記事に更新周期と用語の整合性を追加"
}
```

### Explanation
この変更は、`vector-search-index-size.md` ファイルに対する小規模な更新で、3行が追加され、2行が削除され、合計5行の変更が行われました。主な変更点は次の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、この記事が180日ごとに見直されることが示されています。これにより、読者は情報が定期的に更新されていることを認識し、最新の技術を把握できるようになります。

2. **用語の整合性**: 「近似最近傍検索」という表現が「Approximate Nearest Neighbor (ANN) search」という正式な用語に変更され、読者が用語の意味をより明確に理解できるように改善されました。

3. **内容の明確化**: 近似最近傍アルゴリズムに関する説明が整理され、特にHNSWアルゴリズムのメモリオーバーヘッドに関する具体的な記述が強調されています。

この更新により、Azure AI Searchにおけるベクターインデックスサイズに関する情報がより信頼性を持ち、ユーザーが最新の情報とベストプラクティスを理解しやすくなることを目指しています。

## articles/search/vector-search-integrated-vectorization.md{#item-48219d}

<details>
<summary>Diff</summary>
````diff
@@ -6,6 +6,7 @@ description: Add a vector embedding step in an Azure AI Search skillset to vecto
 author: heidisteen
 ms.author: heidist
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "統合ベクトル化に関する記事に更新周期を追加"
}
```

### Explanation
この変更は、`vector-search-integrated-vectorization.md` ファイルに対する小規模な更新で、1行が追加され、削除はありません。具体的な変更点は次の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、この記事が180日ごとに見直されることが示されています。この追加により、読者はガイドラインが定期的に更新されていることを知ることができ、常に最新の情報にアクセスできることが確保されます。

この修正は、Azure AI Searchにおける統合ベクトル化の手法に関する記事の情報の信頼性を高め、利用者が最新の技術や方法を容易に理解できるようにしています。

## articles/search/vector-search-multi-vector-fields.md{#item-9aa482}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ description: Learn how Azure AI Search enables multi-vector field support for be
 author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
+ms.update-cycle: 180-days
 ms.topic: conceptual
 ms.date: 05/07/2025
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "複数ベクトルフィールドに関する記事に更新周期を追加"
}
```

### Explanation
この変更は、`vector-search-multi-vector-fields.md` ファイルに対する小規模な更新で、1行が追加され、削除はありません。主な変更点は以下の通りです：

1. **更新周期の追加**: 「ms.update-cycle: 180-days」という新しい行が追加され、このドキュメントが180日ごとに見直されることを示しています。このことで、読者は資料の信頼性が保たれ、最新の情報にアクセスできることが強調されます。

この小さな修正は、Azure AI Searchにおける複数ベクトルフィールドのサポートに関する情報をより信頼性のあるものにし、ユーザーが常に最新の技術情報を得られるようにすることを目的としています。

## articles/search/vector-search-overview.md{#item-56e5fa}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 06/20/2025
+ms.date: 07/03/2025
 ---
 
 # Vector search in Azure AI Search
@@ -20,7 +20,7 @@ Vector search is an information retrieval approach that supports indexing and qu
 + Multilingual content, such as "dog" in English and "hund" in German.
 + Multiple content types, such as "dog" in plain text and an image of a dog.
 
-This article covers vector support in Azure AI Search, including its integration with other Azure services. It also introduces concepts and terminology related to vector search development.
+This article provides an overview of vector search in Azure AI Search, including supported scenarios, availability, and integration with other Azure services.
 
 > [!TIP]
 > Want to get started right away? Follow these steps:
@@ -92,73 +92,6 @@ Azure AI Search is deeply integrated across the Azure AI platform. The following
 
 It's also commonly used in open-source frameworks like [LangChain](https://js.langchain.com/docs/integrations/vectorstores/azure_aisearch).
 
-## Vector search concepts
-
-If you're new to vectors, this section explains some core concepts.
-
-### About vector search
-
-Vector search is a method of information retrieval where documents and queries are represented as vectors instead of plain text. In vector search, machine learning models generate the vector representations of source inputs, which can be text, images, or other content.
-
-Having a mathematic representation of content provides a common language for comparing disparate content. If everything is a vector, a query can find a match in vector space, even if the associated original content is in different media or language than the query.
-
-### Why use vector search?
-
-When searchable content is represented as vectors, a query can find close matches in similar content. The embedding model used for vector generation knows which words and concepts are similar and places the resulting vectors close together in the embedding space.
-
-For example, vectorized source documents about "clouds" and "fog" are more likely to show up in a query about "mist" because they're semantically similar, even if they aren't a lexical match.
-
-### Embeddings and vectorization
-
-Machine learning models create *embeddings*, a specific type of vector representation of content or queries. These models capture the semantic meaning of text or representations of other content, such as images.
-
-Natural-language machine learning models are trained on large amounts of data to identify patterns and relationships between words. During training, the models learn to represent any input as a vector of real numbers in an intermediary step called the *encoder*. After training, the models can be modified so that the intermediary vector representation becomes their output. The resulting embeddings are high-dimensional vectors, where words with similar meanings are closer together in the vector space. For more information about embeddings, see [Understand embeddings in Azure OpenAI in Azure AI Foundry Models](/azure/ai-services/openai/concepts/understand-embeddings).
-
-The effectiveness of vector search in retrieving relevant information depends on how effectively the embedding model distills the meaning of documents and queries into the resulting vector. The best models are well-trained on the types of data they represent. You can evaluate existing models, such as Azure OpenAI text-embedding-ada-002; bring your own model that's trained directly on the problem space; or fine-tune a general-purpose model. Azure AI Search doesn't impose constraints on which model you choose, so pick the best one for your data.
-
-To create effective embeddings for vector search, it's important to consider input size limitations. We recommend following the [guidelines for chunking data](vector-search-how-to-chunk-documents.md) before generating embeddings. This best practice ensures that the embeddings accurately capture the relevant information and enable more efficient vector search.
-
-### What is an embedding space?
-
-An *embedding space* is the corpus for vector queries. Within a [search index](search-what-is-an-index.md), the embedding space is all of the vector fields populated with embeddings from the same embedding model. Machine learning models create the embedding space by mapping individual words, phrases, documents (for natural-language processing), images, or other data into representations comprised of vectors of real numbers that act as coordinates in a high-dimensional space.
-
-In the embedding space, similar items are located close together, while dissimilar items are located farther apart. For example, documents about different species of dogs would be clustered close together. Documents about cats would be close together but farther from the dogs cluster, while still being in the neighborhood for animals. Dissimilar concepts, such as cloud computing, would be much farther away.
-
-In practice, embedding spaces are abstract and don't have well-defined, human-interpretable meanings, but the core idea stays the same.
-
-<a name="eknn"></a>
-
-### Nearest neighbors search
-
-In vector search, the search engine scans vectors within the embedding space to identify vectors that are closest to the query vector. This technique is called [*nearest neighbor search*](https://en.wikipedia.org/wiki/Nearest_neighbor_search).
-
-Nearest neighbors quantify the similarity between items. A high degree of vector similarity indicates that the original data is also similar. To expedite nearest neighbor search and reduce the search space, the search engine uses data structures and data partitioning. Each vector search algorithm solves the nearest neighbor problems differently, optimizing for minimum latency, maximum throughput, recall, and memory. To compute similarity, similarity metrics provide the mechanism for computing distance.
-
-Azure AI Search supports the following algorithms:
-
-+ **Hierarchical navigable small world (HNSW)**. HNSW is a leading ANN algorithm optimized for high-recall, low-latency applications with unknown or volatile data distribution. It organizes high-dimensional data points into a hierarchical graph structure that enables fast, scalable similarity search and allows a tunable trade-off between search accuracy and computational cost. Because the algorithm requires all data points to reside in memory for fast random access, HNSW consumes [vector index size](vector-search-index-size.md) quota.
-
-+ **Exhaustive k-nearest neighbors (KNN)**. KNN calculates the distances between the query vector and all data points. It's computationally intensive and works best for smaller datasets. Because the algorithm doesn't require fast random access of data points, KNN doesn't consume vector index size quota. However, it provides the global set of nearest neighbors.
-
-To learn how to specify the algorithm, vector profile, and profile assignment for HNSW or KNN, see [Create a vector field](vector-search-how-to-create-index.md).
-
-Algorithm parameters that are used to initialize the index during index creation are immutable and can't be changed after the index is built. However, parameters that affect the query-time characteristics (`efSearch`) can be modified.
-
-Fields that specify the HNSW algorithm also support exhaustive KNN search using the [query request](vector-search-how-to-query.md) parameter `"exhaustive": true`. However, the opposite isn't true. If a field is indexed for `exhaustiveKnn`, you can't use HNSW in the query because the extra data structures that enable efficient search don't exist.
-
-### Approximate nearest neighbors
-
-Approximate nearest neighbor (ANN) is a class of algorithms for finding matches in vector space. This class of algorithms uses different data structures or data partitioning methods to significantly reduce the search space and accelerate query processing.
-
-ANN algorithms sacrifice some accuracy but offer scalable and faster retrieval of approximate nearest neighbors, which makes them ideal for balancing accuracy and efficiency in modern information retrieval applications. You can adjust the parameters of your algorithm to fine-tune the recall, latency, memory, and disk footprint requirements of your search application.
-
-Azure AI Search uses HNSW for its ANN algorithm.
-
-<!-- > [!NOTE]
-> Finding the true set of [nearest neighbors](https://en.wikipedia.org/wiki/Nearest_neighbor_search) requires comparing the input vector exhaustively against all vectors in the dataset. While each vector similarity calculation is relatively fast, performing these exhaustive comparisons across large datasets is computationally expensive and slow due to the sheer number of comparisons. For example, if a dataset contains 10 million 1,000-dimensional vectors, computing the distance between the query vector and all vectors in the dataset would require scanning 37 GB of data (assuming single-precision floating point vectors) and a high number of similarity calculations.
-> 
-> To address this challenge, approximate nearest neighbor (ANN) search methods are used to trade off recall for speed. These methods can efficiently find a small set of candidate vectors that are similar to the query vector and have high likelihood to be in the globally most similar neighbors. Each algorithm has a different approach to reducing the total number of vectors comparisons, but they all share the ability to balance accuracy and efficiency by tweaking the algorithm configuration parameters. -->
-
 ## Related content
 
 + [Quickstart: Vector search using REST](search-get-started-vector.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ベクトル検索に関する記事の大幅な修正"
}
```

### Explanation
この変更は、`vector-search-overview.md` ファイルに対する大幅な修正を伴い、合計で2行が追加され、69行が削除されました。主な変更点は以下の通りです：

1. **記事の概要の更新**: 記事の説明が更新され、「Azure AI Searchにおけるベクトル検索の概要、サポートされているシナリオ、可用性、および他のAzureサービスとの統合」という内容に変更されました。これにより、読者がこの記事で何を学べるのかが明確になっています。

2. **日付の変更**: 記事の日付が「06/20/2025」から「07/03/2025」に更新されています。

3. **セクションの削除**: 大規模な修正に伴い、ベクトル検索の概念に関する複数のセクションが削除されました。これにより、記事はスリム化され、重要な情報に集中できる内容となっています。具体的には、ベクトル検索の基本、なぜベクトル検索を使用するのか、埋め込みおよびベクトル化、近似最近傍検索などに関する詳細な説明が省かれています。

このような変更により、記事はよりシンプルで直接的な内容になり、読者がベクトル検索についての重要な情報を効率的に得られることを目指していますが、一部の詳細情報は削除されたため、より深入りした理解が必要な読者には物足りなく感じられるかもしれません。

## articles/search/vector-search-ranking.md{#item-0764d8}

<details>
<summary>Diff</summary>
````diff
@@ -9,36 +9,46 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 05/29/2025
+ms.date: 07/03/2025
 ---
 
 # Relevance in vector search
 
-During vector query execution, the search engine looks for similar vectors to find the best candidates to return in search results. Depending on how you indexed the vector content, the search for relevant matches is either exhaustive, or constrained to nearest neighbors for faster processing. Once candidates are found, similarity metrics are used to score each result based on the strength of the match. 
+During vector query execution, the search engine looks for similar vectors to find the best candidates to return in search results. Depending on how you indexed the vector content, the search for relevant matches is either exhaustive, or constrained to nearest neighbors for faster processing. Once candidates are found, similarity metrics are used to score each result based on the strength of the match.
 
 This article explains the algorithms used to find relevant matches and the similarity metrics used for scoring. It also offers tips for improving relevance if search results don't meet expectations.
 
 ## Algorithms used in vector search
 
-Vector search algorithms include exhaustive k-nearest neighbors (KNN) and Hierarchical Navigable Small World (HNSW). 
+Vector search algorithms include:
 
-+ Exhaustive KNN performs a brute-force scan of the entire vector space.
++ [Exhaustive K-Nearest Neighbors (KNN)](#about-exhaustive-knn), which performs a brute-force scan of the entire vector space.
 
-+ HNSW performs an [approximate nearest neighbor (ANN)](vector-search-overview.md#approximate-nearest-neighbors) search. 
++ [Hierarchical Navigable Small World (HNSW)](#about-hnsw), which performs an [Approximate Nearest Neighbor (ANN)](#about-ann) search.
 
-Only vector fields marked as `searchable` in the index, or as `searchFields` in the query, are used for searching and scoring. 
+Only vector fields marked as `searchable` in the index or `searchFields` in the query are used for searching and scoring.
 
-### When to use exhaustive KNN
+### About exhaustive KNN
 
-Exhaustive KNN calculates the distances between all pairs of data points and finds the exact `k` nearest neighbors for a query point. It's intended for scenarios where high recall is of utmost importance, and users are willing to accept the trade-offs in query latency. Because it's computationally intensive, use exhaustive KNN for small to medium datasets, or when precision requirements outweigh query performance considerations. 
+Exhaustive KNN calculates the distances between all pairs of data points and finds the exact `k` nearest neighbors for a query point. Because the algorithm doesn't require fast random access of data points, KNN doesn't consume [vector index size](vector-search-index-size.md) quota. However, it provides the global set of nearest neighbors.
 
-A secondary use case is to build a dataset to evaluate approximate nearest neighbor algorithm recall. Exhaustive KNN can be used to build the ground truth set of nearest neighbors.
+Exhaustive KNN is computationally intensive, so use it for small to medium datasets or when the need for precision outweighs the need for query performance. Another use case is building a dataset to evaluate the recall of an [ANN algorithm](#about-ann), as exhaustive KNN can be used to build the ground truth set of nearest neighbors.
 
-### When to use HNSW
+### About HNSW
 
-During indexing, HNSW creates extra data structures for faster search, organizing data points into a hierarchical graph structure. HNSW has several configuration parameters that can be tuned to achieve the throughput, latency, and recall objectives for your search application. For example, at query time, you can specify options for exhaustive search, even if the vector field is indexed for HNSW.
+HNSW is an ANN algorithm optimized for high-recall, low-latency applications with unknown or volatile data distribution. During indexing, HNSW creates extra data structures that organize data points into a hierarchical graph. During query execution, HNSW navigates through this graph to find the most relevant matches, enabling efficient nearest neighbor searches.
 
-During query execution, HNSW enables fast neighbor queries by navigating through the graph. This approach strikes a balance between search accuracy and computational efficiency. HNSW is recommended for most scenarios due to its efficiency when searching over larger data sets. 
+HNSW requires all data points to reside in memory for fast random access, which consumes [vector index size](vector-search-index-size.md) quota. This design balances search accuracy with computational efficiency and makes HNSW suitable for most scenarios, especially when searching over larger datasets.
+
+HNSW offers several tunable configuration parameters to optimize throughput, latency, and recall for your search application. For example, fields that specify HNSW also support exhaustive KNN using the [query request](vector-search-how-to-query.md) parameter `"exhaustive": true`. However, fields indexed for `exhaustiveKnn` don't support HNSW queries because the extra data structures that enable efficient search don't exist.
+
+### About ANN
+
+ANN is a class of algorithms for finding matches in vector space. This class of algorithms uses different data structures or data partitioning methods to significantly reduce the search space and accelerate query processing.
+
+ANN algorithms sacrifice some accuracy but offer scalable and faster retrieval of approximate nearest neighbors, which makes them ideal for balancing accuracy and efficiency in modern information retrieval applications. You can adjust the parameters of your algorithm to fine-tune the recall, latency, memory, and disk footprint requirements of your search application.
+
+Azure AI Search uses HNSW for its ANN algorithm.
 
 ## How nearest neighbor search works
 
@@ -56,15 +66,15 @@ During indexing, the search service constructs the HNSW graph. The goal of index
 
 1. Entry point: This is the top-level of the hierarchical graph and serves as the starting point for indexing.
 
-1. Adding to the graph: Different hierarchical levels represent different granularities of the graph, with higher levels being more global, and lower levels being more granular. Each node in the graph represents a vector point. 
+1. Adding to the graph: Different hierarchical levels represent different granularities of the graph, with higher levels being more global, and lower levels being more granular. Each node in the graph represents a vector point.
 
-   - Each node is connected to up to `m` neighbors that are nearby. This is the `m` parameter.
+   + Each node is connected to up to `m` neighbors that are nearby. This is the `m` parameter.
 
-   - The number of data points considered as candidate connections is governed by the `efConstruction` parameter. This dynamic list forms the set of closest points in the existing graph for the algorithm to consider. Higher `efConstruction` values result in more nodes being considered, which often leads to denser local neighborhoods for each vector.
+   + The number of data points considered as candidate connections is governed by the `efConstruction` parameter. This dynamic list forms the set of closest points in the existing graph for the algorithm to consider. Higher `efConstruction` values result in more nodes being considered, which often leads to denser local neighborhoods for each vector.
 
-   - These connections use the configured similarity `metric` to determine distance. Some connections are "long-distance" connections that connect across different hierarchical levels, creating shortcuts in the graph that enhance search efficiency.
+   + These connections use the configured similarity `metric` to determine distance. Some connections are "long-distance" connections that connect across different hierarchical levels, creating shortcuts in the graph that enhance search efficiency.
 
-1. Graph pruning and optimization: This can happen after indexing all vectors, and it improves navigability and efficiency of the HNSW graph. 
+1. Graph pruning and optimization: This can happen after indexing all vectors, and it improves navigability and efficiency of the HNSW graph.
 
 ### Navigating the HNSW graph at query time
 
@@ -99,14 +109,14 @@ Scores are calculated and assigned to each match, with the highest matches retur
 
 | Search method | Parameter | Scoring metric | Range |
 |---------------|-----------|-------------------|-------|
-| vector search | `@search.score` | Cosine | 0.333 - 1.00 | 
+| vector search | `@search.score` | Cosine | 0.333 - 1.00 |
 
 For`cosine` metric, it's important to note that the calculated `@search.score` isn't the cosine value between the query vector and the document vectors. Instead, Azure AI Search applies transformations such that the score function is monotonically decreasing, meaning score values will always decrease in value as the similarity becomes worse. This transformation ensures that search scores are usable for ranking purposes.
 
-There are some nuances with similarity scores: 
+There are some nuances with similarity scores:
 
-- Cosine similarity is defined as the cosine of the angle between two vectors.
-- Cosine distance is defined as `1 - cosine_similarity`.
++ Cosine similarity is defined as the cosine of the angle between two vectors.
++ Cosine distance is defined as `1 - cosine_similarity`.
 
 To create a monotonically decreasing function, the `@search.score` is defined as `1 / (1 + cosine_distance)`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のランキングに関する記事の更新"
}
```

### Explanation
この変更は、`vector-search-ranking.md` ファイルに対する修正で、31行が追加され、21行が削除され、合計52行にわたる変更が行われました。主な変更点は以下の通りです：

1. **記事の日付の更新**: 記事の日付が「05/29/2025」から「07/03/2025」に変更されました。

2. **アルゴリズムの説明の改善**: アルゴリズムのセクションが、用語の明確化と構造的な整理を含むように更新されました。特に、各アルゴリズム（Exhaustive KNN および HNSW）の役割や特性について、より詳細に説明されています。また、「About KNN」や「About HNSW」などの見出しが追加され、情報の整理が施されています。

3. **新しいトピックの追加**: ANN（Approximate Nearest Neighbor）に関する新しいセクションが追加され、これによりユーザーはベクトル空間でのマッチング手法についての理解を深めることができます。

4. **内容の明確化と流れの改善**: 文中の情報が再構成され、文の流れや読みやすさが向上されています。特に、各アルゴリズムについての説明が具体的にされており、読者が理解しやすくなっています。

これらの変更は全体的に、ベクトル検索のランキングに関する情報を提供し、ユーザーが検索結果の関連性を向上させる手助けをすることを目的としています。また、読者が検索アルゴリズムの理解を深めるための情報源としての実用性が高められています。


