---
date: '2026-03-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:42934f5...MicrosoftDocs:700cf50
summary: この報告書では、主にAzureのドキュメントに関する変更点がまとめられています。新機能として、ユーザーが操作手順を視覚的に理解できる新しいスクリーンショットとガイドが追加されたこと、また、セマンティックランキング用のリソース認証ガイドが新たに導入されたことが紹介されています。一方で、いくつかのクイックスタートガイドやイントロダクションガイドが削除され、重要な学習リソースが失われた点が問題視されています。また、インデックス名の統一や文書のメタデータ調整など、整合性の向上に向けた他の更新も行われています。全体として、ユーザー体験の向上が目的ですが、一部のコンテンツ削除による不便さのリスクも懸念されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:42934f5...MicrosoftDocs:700cf50){target="_blank"}

<format>
# Highlights

## New features
- 新しいスクリーンショットとガイドの追加により、ユーザーが操作手順を視覚的に理解できるようになりました。
- セマンティックランキング用のリソース認証ガイドが新たに追加されました。

## Breaking changes
- クイックスタートガイドやイントロダクションガイドのいくつかが削除され、重要な学習リソースが失われました。

## Other updates
- `hotels-sample-index` が `hotels-sample` に変更され、インデックス名が一貫化されました。
- 各言語やクイックスタートガイドのラベル・メタデータが調整され、文書の整合性と可読性が改善されました。

# Insights

この一連の変更においては、主にドキュメント全体の整合性を高めつつ、新しいスクリーンショットやガイドを取り入れることで、ユーザーがAzureの各機能をより効果的に学べるようにしている点が注目されます。特に、インデックス名の統一は些細な変更に思えるかもしれませんが、ユーザーが誤解を避けるためには重要です。スクリーンショットの更新や追加も、視覚的な情報によって操作を補助する役割を担っています。

一方で、一部のクイックスタートガイドが削除されたことで、新しい利用者が宝の情報にアクセスしづらくなる可能性があります。このような変更を行う場合は、代替資料のへの誘導や、削除の背景説明をしっかり行うことが求められます。

また、新たに追加されたセマンティックランキングの認証に関するガイドは、技術的な障壁を取り除き、ユーザーがよりスムーズに設定を開始できるための一助となっています。Azureを利用する開発者にとっては認証関連情報の一元化が利便性向上につながりますが、このような文書の充実は、サービス利用のサポート面でも大きな意味を持っています。

全体として、この更新シリーズはドキュメントの利用体験向上を目的としたものですが、削除されたコンテンツによりユーザーに不便を与えるリスクも存在するため、今後の管理ポリシーに注意を払う必要があります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-blob.md](#item-ac6c8a) | minor update | エージェント知識ソースの更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-onelake.md](#item-ec7a80) | minor update | OneLakeエージェント知識ソースの更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-search-index.md](#item-09d366) | minor update | 検索インデックスエージェント知識ソースの更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed.md](#item-fe72fc) | minor update | SharePointインデックスエージェント知識ソースの更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-sharepoint-remote.md](#item-79d019) | minor update | リモートSharePointエージェント知識ソースの更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-web.md](#item-6b21d0) | minor update | Webエージェント知識ソースの更新 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-how-to-create-knowledge-base.md](#item-7df0e2) | minor update | 知識ベース作成に関するドキュメントの更新 | modified | 1 | 1 | 2 | 
| [get-started-portal-agentic-retrieval.md](#item-2bf1dc) | minor update | エージェント情報検索の開始ガイドの更新 | modified | 1 | 1 | 2 | 
| [hybrid-search-how-to-query.md](#item-345ce6) | minor update | ハイブリッド検索クエリのサンプルインデックス名の更新 | modified | 2 | 2 | 4 | 
| [agentic-retrieval-how-to-create-knowledge-base-csharp.md](#item-4469a2) | minor update | エージェント情報検索に関するC#の知識ベース作成ガイドの修正 | modified | 2 | 2 | 4 | 
| [agentic-retrieval-how-to-create-knowledge-base-python.md](#item-4e498f) | minor update | エージェント情報検索に関するPythonの知識ベース作成ガイドの修正 | modified | 2 | 2 | 4 | 
| [agentic-retrieval-how-to-create-knowledge-base-rest.md](#item-37851c) | minor update | エージェント情報検索に関するREST APIの知識ベース作成ガイドの修正 | modified | 2 | 2 | 4 | 
| [agentic-retrieval-csharp.md](#item-f93ed3) | minor update | C#を使用したエージェント情報検索のクイックスタートガイドの修正 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-java.md](#item-4e2c55) | minor update | Javaを使用したエージェント情報検索のクイックスタートガイドの修正 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-javascript.md](#item-715283) | minor update | JavaScriptを使用したエージェント情報検索のクイックスタートガイドの修正 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-python.md](#item-efee6a) | minor update | Pythonを使用したエージェント情報検索のクイックスタートガイドの修正 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-rest.md](#item-3df373) | minor update | RESTを使用したエージェント情報検索のクイックスタートガイドの修正 | modified | 2 | 2 | 4 | 
| [agentic-retrieval-typescript.md](#item-e6370b) | minor update | TypeScriptを使用したエージェント情報検索のクイックスタートガイドの修正 | modified | 1 | 1 | 2 | 
| [full-text-rest.md](#item-5d3419) | minor update | フルテキスト検索のRESTクイックスタートガイドの修正 | modified | 1 | 1 | 2 | 
| [search-get-started-portal-new-wizard.md](#item-114e35) | breaking change | クイックスタートガイドの削除: ポータルの新ウィザードを使った検索の開始 | removed | 0 | 159 | 159 | 
| [search-get-started-vector-csharp.md](#item-9e800b) | minor update | C#向けベクトル検索クイックスタートガイドの名称変更 | renamed | 0 | 0 | 0 | 
| [search-get-started-vector-rest.md](#item-c7d261) | minor update | REST APIによるベクトル検索クイックスタートガイドの内容修正 | modified | 1 | 1 | 2 | 
| [search-get-started-vector-typescript.md](#item-9b3bc8) | minor update | TypeScriptによるベクトル検索クイックスタートガイドの内容修正 | modified | 15 | 9 | 24 | 
| [semantic-ranker-csharp.md](#item-09fa32) | breaking change | C#におけるセマンティックランカーのクイックスタートガイドの大幅改訂 | modified | 308 | 373 | 681 | 
| [semantic-ranker-index.md](#item-44a527) | new feature | セマンティック構成を含むインデックスのクイックスタートガイドの追加 | added | 69 | 0 | 69 | 
| [semantic-ranker-intro.md](#item-538e0f) | breaking change | セマンティックランカーのイントロダクションガイドの削除 | removed | 0 | 163 | 163 | 
| [semantic-ranker-java.md](#item-93a05a) | minor update | Java用セマンティックランカーのクイックスタートガイドの更新 | modified | 441 | 105 | 546 | 
| [semantic-ranker-javascript.md](#item-2e091c) | minor update | JavaScript用セマンティックランカーのクイックスタートガイドの更新 | modified | 343 | 337 | 680 | 
| [semantic-ranker-python.md](#item-a6dcfa) | minor update | Python用セマンティックランカーのクイックスタートガイドの更新 | modified | 335 | 274 | 609 | 
| [semantic-ranker-rest.md](#item-d74861) | minor update | REST API用セマンティックランカーのクイックスタートガイドの更新 | modified | 274 | 302 | 576 | 
| [semantic-ranker-typescript.md](#item-6d5573) | minor update | TypeScript用セマンティックランカーのクイックスタートガイドの更新 | modified | 361 | 397 | 758 | 
| [resource-authentication-semantic.md](#item-da8e67) | new feature | セマンティックランキング用のリソース認証ガイドを追加 | added | 23 | 0 | 23 | 
| [index-add-language-analyzers.md](#item-004ac0) | minor update | インデックスの言語アナライザー仕様の例を更新 | modified | 1 | 1 | 2 | 
| [index-add-suggesters.md](#item-28ed57) | minor update | サジェスターのインデックス仕様の例を更新 | modified | 1 | 1 | 2 | 
| [index-similarity-and-scoring.md](#item-75603d) | minor update | 検索リクエストのインデックス名を更新 | modified | 1 | 1 | 2 | 
| [add-suggestions.png](#item-8e78d8) | new feature | 提案追加のスクリーンショットを追加 | added | 0 | 0 | 0 | 
| [configure-results.png](#item-33a179) | breaking change | 結果の設定に関するスクリーンショットを削除 | removed | 0 | 0 | 0 | 
| [create-demo-app-action.png](#item-fc56b8) | breaking change | デモアプリの作成アクションに関するスクリーンショットを削除 | removed | 0 | 0 | 0 | 
| [customize-results.png](#item-fb3041) | new feature | 結果のカスタマイズに関するスクリーンショットを追加 | added | 0 | 0 | 0 | 
| [customize-sidebar.png](#item-445361) | new feature | サイドバーのカスタマイズに関するスクリーンショットを追加 | added | 0 | 0 | 0 | 
| [delete-filters.png](#item-c9f3bb) | breaking change | フィルター削除に関するスクリーンショットを削除 | removed | 0 | 0 | 0 | 
| [enable-cors-continue.png](#item-b62d62) | new feature | CORSを有効にする手順に関するスクリーンショットを追加 | added | 0 | 0 | 0 | 
| [connect-to-your-data.png](#item-4eb5d4) | minor update | データ接続に関するスクリーンショットの修正 | modified | 0 | 0 | 0 | 
| [index-schema-definition.png](#item-152d3e) | minor update | インデックススキーマ定義に関するスクリーンショットの修正 | modified | 0 | 0 | 0 | 
| [indexers-status.png](#item-f09549) | minor update | インデクサーのステータスに関するスクリーンショットの修正 | modified | 0 | 0 | 0 | 
| [indexes-list.png](#item-bb803f) | minor update | インデックスのリストに関するスクリーンショットの修正 | modified | 0 | 0 | 0 | 
| [review-and-create.png](#item-9dea50) | minor update | レビューと作成に関するスクリーンショットの修正 | modified | 0 | 0 | 0 | 
| [search-explorer-change-view.png](#item-65fbc6) | minor update | 検索エクスプローラーのビュー変更に関するスクリーンショットの修正 | modified | 0 | 0 | 0 | 
| [search-explorer-query-results.png](#item-6aa0cb) | minor update | 検索エクスプローラーのクエリ結果に関するスクリーンショットの修正 | modified | 0 | 0 | 0 | 
| [search-explorer-query-string.png](#item-ce0c3c) | minor update | 検索エクスプローラーのクエリ文字列に関するスクリーンショットの修正 | modified | 0 | 0 | 0 | 
| [default-semantic-configuration.png](#item-0aa386) | new feature | デフォルトのセマンティック構成に関する新しいスクリーンショットの追加 | added | 0 | 0 | 0 | 
| [no-semantic-configuration.png](#item-be001a) | breaking change | セマンティック構成なしのスクリーンショットの削除 | removed | 0 | 0 | 0 | 
| [search-explorer-simple-query.png](#item-df72be) | breaking change | シンプルクエリの検索エクスプローラーのスクリーンショットの削除 | removed | 0 | 0 | 0 | 
| [query-lucene-syntax.md](#item-736436) | minor update | 検索リクエストのインデックス名の修正 | modified | 1 | 1 | 2 | 
| [search-create-app-portal.md](#item-19ab44) | minor update | デモアプリウィザードの改善とスクリーンショットの更新 | modified | 11 | 7 | 18 | 
| [search-faceted-navigation-examples.md](#item-2b1158) | minor update | ファセットナビゲーションのサンプルでのインデックス名の修正 | modified | 19 | 19 | 38 | 
| [search-faceted-navigation.md](#item-f29d1e) | minor update | インデックス名の修正とファセットに関する情報の更新 | modified | 5 | 5 | 10 | 
| [search-get-started-agentic-retrieval.md](#item-4a40f4) | minor update | エージェントリトリーバルのクイックスタートドキュメントの改善 | modified | 13 | 13 | 26 | 
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | マルチモーダル検索のウィザード開始の説明の修正 | modified | 0 | 2 | 2 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | ベクトル検索のウィザード開始の説明の修正 | modified | 1 | 3 | 4 | 
| [search-get-started-portal.md](#item-6d0cb1) | minor update | Azureポータルにおけるフルテキスト検索のクイックスタートのアップデート | modified | 164 | 32 | 196 | 
| [search-get-started-rbac.md](#item-9d96c1) | minor update | RBACにおけるクイックスタートのゾーンピボットの修正 | modified | 3 | 3 | 6 | 
| [search-get-started-semantic.md](#item-2b3902) | minor update | セマンティック検索のクイックスタートの更新 | modified | 16 | 18 | 34 | 
| [search-get-started-text.md](#item-935941) | minor update | フルテキスト検索のクイックスタートの更新 | modified | 11 | 11 | 22 | 
| [search-get-started-vector.md](#item-4984d9) | minor update | ベクター検索のクイックスタートの更新 | modified | 10 | 10 | 20 | 
| [search-how-to-delete-documents.md](#item-556879) | minor update | ドキュメント削除方法のクイックスタートの更新 | modified | 10 | 10 | 20 | 
| [search-how-to-integrated-vectorization.md](#item-86fb1e) | minor update | 統合ベクトル化に関する記事の用語修正 | modified | 1 | 1 | 2 | 
| [search-how-to-load-search-index.md](#item-a72573) | minor update | 検索インデックスの読み込みに関する記事のインデックス名修正 | modified | 3 | 3 | 6 | 
| [search-how-to-manage-index.md](#item-6bf53b) | minor update | インデックス管理に関する記事のゾーンピボットグループ修正 | modified | 1 | 1 | 2 | 
| [search-howto-complex-data-types.md](#item-75a002) | minor update | Hotelsサンプルインデックスの名称修正 | modified | 1 | 1 | 2 | 
| [search-howto-concurrency.md](#item-863358) | minor update | Hotelsサンプルインデックスの名称修正と拼音形式の変更 | modified | 2 | 2 | 4 | 
| [search-howto-reindex.md](#item-46738a) | minor update | Hotelsサンプルインデックスの名称変更 | modified | 2 | 2 | 4 | 
| [search-import-data-portal.md](#item-b804d1) | minor update | ホテルサンプルインデックスに関する説明の修正 | modified | 1 | 1 | 2 | 
| [search-language-support.md](#item-a7979b) | minor update | ホテルサンプルインデックスの名称変更 | modified | 2 | 2 | 4 | 
| [search-monitor-queries.md](#item-279569) | minor update | ホテルサンプルインデックス名の修正 | modified | 1 | 1 | 2 | 
| [search-more-like-this.md](#item-56c565) | minor update | ホテルサンプルインデックス名の統一 | modified | 4 | 4 | 8 | 
| [search-pagination-page-layout.md](#item-115902) | minor update | ホテルサンプルインデックス名の変更 | modified | 4 | 4 | 8 | 
| [search-query-create.md](#item-532822) | minor update | インデックス名の変更と一致性の向上 | modified | 6 | 6 | 12 | 
| [search-query-fuzzy.md](#item-a130e3) | minor update | ファジー検索に関する説明の明確化 | modified | 4 | 4 | 8 | 
| [search-query-lucene-examples.md](#item-ce3624) | minor update | インデックス名の一貫性の向上と表現の調整 | modified | 3 | 4 | 7 | 
| [search-query-simple-examples.md](#item-834766) | minor update | サンプルインデックス名の統一と表現の改善 | modified | 14 | 14 | 28 | 
| [search-synonyms.md](#item-2d5d63) | minor update | インデックス名の調整 | modified | 1 | 1 | 2 | 
| [search-what-is-data-import.md](#item-d73ef5) | minor update | インデックス名の表現の統一 | modified | 1 | 1 | 2 | 
| [semantic-how-to-query-request.md](#item-85530d) | minor update | インデックス名の統一と修正 | modified | 4 | 4 | 8 | 
| [semantic-how-to-query-rewrite.md](#item-3e168f) | minor update | インデックス名の一貫性の向上 | modified | 5 | 5 | 10 | 
| [speller-how-to-add.md](#item-9b4502) | minor update | インデックス名の修正と一貫性の向上 | modified | 4 | 4 | 8 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-blob.md{#item-ac6c8a}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 11/19/2025
-zone_pivot_groups: agentic-retrieval-pivots
+zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create a blob knowledge source from Azure Blob Storage and ADLS Gen2
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースの更新"
}
```

### Explanation
この変更は、Azure Blob StorageおよびADLS Gen2からエージェント知識ソースを作成する方法に関するドキュメントの軽微な更新を示しています。具体的には、`zone_pivot_groups`の値が`agentic-retrieval-pivots`から`search-csharp-python-rest`に変更されています。この変更は、ナレッジソースの使い方に関する指針をより正確に反映するものとなっています。ファイル内では1行が追加され、1行が削除されているため、全体として2行の変更が行われています。

## articles/search/agentic-knowledge-source-how-to-onelake.md{#item-ec7a80}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2025
 ms.topic: how-to
 ms.date: 11/20/2025
-zone_pivot_groups: agentic-retrieval-pivots
+zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create an indexed OneLake knowledge source
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLakeエージェント知識ソースの更新"
}
```

### Explanation
この変更は、OneLakeからのエージェント知識ソースの作成方法について記述されたドキュメントの軽微な更新を反映しています。具体的には、`zone_pivot_groups`の値が`agentic-retrieval-pivots`から`search-csharp-python-rest`に変更されています。この変更により、ドキュメントが最新の情報や推奨事項を反映したものとなります。ファイル内では1行が追加され、1行が削除されているため、合計で2行の変更が行われています。

## articles/search/agentic-knowledge-source-how-to-search-index.md{#item-09d366}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 11/19/2025
-zone_pivot_groups: agentic-retrieval-pivots
+zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create a search index knowledge source
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスエージェント知識ソースの更新"
}
```

### Explanation
この変更は、検索インデックスを作成するためのエージェント知識ソースに関するドキュメントの軽微な更新を示しています。具体的には、`zone_pivot_groups`の値が`agentic-retrieval-pivots`から`search-csharp-python-rest`に変更されています。この修正によって、文書が最新の推奨用途に適合し、より正確な情報を提供するようになっています。ファイル内では1行が追加され、1行が削除されているため、合計で2行の変更が行われています。

## articles/search/agentic-knowledge-source-how-to-sharepoint-indexed.md{#item-fe72fc}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 11/20/2025
-zone_pivot_groups: agentic-retrieval-pivots
+zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create an indexed SharePoint knowledge source
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointインデックスエージェント知識ソースの更新"
}
```

### Explanation
この変更は、SharePointのインデックスを作成するためのエージェント知識ソースに関するドキュメントの軽微な更新を示しています。具体的には、`zone_pivot_groups`の値が`agentic-retrieval-pivots`から`search-csharp-python-rest`に変更されています。この変更により、最新の推奨設定に従った正確な情報をユーザーに提供できるようになります。ファイルでは1行が追加され、1行が削除されているため、合計で2行の変更が行われています。

## articles/search/agentic-knowledge-source-how-to-sharepoint-remote.md{#item-79d019}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 11/19/2025
-zone_pivot_groups: agentic-retrieval-pivots
+zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create a remote SharePoint knowledge source
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リモートSharePointエージェント知識ソースの更新"
}
```

### Explanation
この変更は、リモートSharePointエージェント知識ソースのドキュメントに対する軽微な更新を示しています。具体的には、`zone_pivot_groups`の値が`agentic-retrieval-pivots`から`search-csharp-python-rest`に変更されています。この修正により、情報が最新の推奨設定に沿ったものとなり、ユーザーに対してより適切なガイダンスを提供することが可能になります。ファイル内では1行が追加され、1行が削除されており、合計で2行の変更が実施されています。

## articles/search/agentic-knowledge-source-how-to-web.md{#item-6b21d0}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2025
 ms.topic: how-to
 ms.date: 11/19/2025
-zone_pivot_groups: agentic-retrieval-pivots
+zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create a Web Knowledge Source resource
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Webエージェント知識ソースの更新"
}
```

### Explanation
この変更は、Webエージェント知識ソースに関するドキュメントの軽微な更新を示しています。具体的には、`zone_pivot_groups`の値が`agentic-retrieval-pivots`から`search-csharp-python-rest`に変更されています。この変更により、ユーザーが最新の推奨される設定に基づいた正確な情報を得ることができるようになります。ファイル内では1行が追加され、1行が削除されており、合計で2行の変更が行われています。

## articles/search/agentic-retrieval-how-to-create-knowledge-base.md{#item-7df0e2}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 01/15/2026
-zone_pivot_groups: agentic-retrieval-pivots
+zone_pivot_groups: search-csharp-python-rest
 ---
 
 # Create a knowledge base in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ベース作成に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおける知識ベースの作成方法に関するドキュメントの軽微な更新を示しています。具体的には、`zone_pivot_groups`の値が`agentic-retrieval-pivots`から`search-csharp-python-rest`に変更されています。この修正により、ユーザーは最新の情報に基づいたガイダンスを受けることができ、より適切な設定を行うことが可能になります。ファイル内では1行が追加され、1行が削除されており、合計で2行の変更が行われています。

## articles/search/get-started-portal-agentic-retrieval.md{#item-2bf1dc}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ Afterwards, you test the knowledge base by submitting a complex query that requi
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](search-create-service-portal.md) in any [region that provides agentic retrieval](search-region-support.md).
++ An [Azure AI Search service](search-create-service-portal.md) in any [region that provides agentic retrieval](search-region-support.md). This quickstart requires the Basic tier or higher for managed identity support.
 
 + An [Azure Blob Storage account](/azure/storage/common/storage-account-create).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント情報検索の開始ガイドの更新"
}
```

### Explanation
この変更は、エージェント情報検索を開始するためのポータルに関するドキュメントに対する軽微な更新を示しています。具体的には、Azure AI Searchサービスに必要な条件に関する情報が追加されています。新たに「このクイックスタートには、マネージドIDサポートのためにBasic層以上が必要です。」という注意書きが挿入され、ユーザーが準備すべきサービスの要件を明確にしています。ファイル内では1行が追加され、1行が削除されており、合計で2行の変更が行われています。

## articles/search/hybrid-search-how-to-query.md{#item-345ce6}

<details>
<summary>Diff</summary>
````diff
@@ -214,7 +214,7 @@ from azure.search.documents.models import VectorizedQuery
 
 # Set up the client
 endpoint = os.environ["AZURE_SEARCH_ENDPOINT"]
-index_name = "hotels-sample-index"
+index_name = "hotels-sample"
 credential = DefaultAzureCredential()
 
 client = SearchClient(endpoint=endpoint, index_name=index_name, credential=credential)
@@ -256,7 +256,7 @@ using Azure.Search.Documents.Models;
 
 // Set up the client
 string endpoint = Environment.GetEnvironmentVariable("AZURE_SEARCH_ENDPOINT");
-string indexName = "hotels-sample-index";
+string indexName = "hotels-sample";
 
 SearchClient client = new SearchClient(
     new Uri(endpoint),
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索クエリのサンプルインデックス名の更新"
}
```

### Explanation
この変更は、ハイブリッド検索のクエリに関するドキュメントの軽微な更新で、サンプルコード内のインデックス名が変更されています。具体的には、PythonおよびC#のコードサンプル両方において、インデックス名が`"hotels-sample-index"`から`"hotels-sample"`に変更されました。この修正により、ドキュメントのサンプルコードが最新の状態になり、ユーザーが正確な情報を得られるようになります。ファイル内では合計で2行が追加され、2行が削除されており、変更は全部で4行に及びます。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-csharp.md{#item-4469a2}

<details>
<summary>Diff</summary>
````diff
@@ -45,7 +45,7 @@ After you create a knowledge base, you can update its properties at any time. If
 
 ### Supported models
 
-Use one of the following LLMs from Azure OpenAI in Foundry Models or an equivalent open-source model. For deployment instructions, see [Deploy Microsoft Foundry Models in the Foundry portal](/azure/ai-foundry/how-to/deploy-models-openai).
+Use one of the following LLMs from Azure OpenAI in Foundry Models. For deployment instructions, see [Deploy Microsoft Foundry Models in the Foundry portal](/azure/ai-foundry/how-to/deploy-models-openai).
 
 + `gpt-4o`
 + `gpt-4o-mini`
@@ -234,7 +234,7 @@ Pass the following properties to create a knowledge base.
 | `RetrievalInstructions` | A prompt for the LLM to determine whether a knowledge source should be in scope for a query. Include this prompt when you have multiple knowledge sources. This field influences both knowledge source selection and query formulation. For example, instructions could append information or prioritize a knowledge source. Instructions are passed directly to the LLM, which means it's possible to provide instructions that break query planning, such as instructions that result in bypassing an essential knowledge source. | String | Yes |
 | `AnswerInstructions` | Custom instructions to shape synthesized answers. The default is null. For more information, see [Use answer synthesis for citation-backed responses](../../agentic-retrieval-how-to-answer-synthesis.md). | String | Yes |
 | `OutputMode` | Valid values are `AnswerSynthesis` for an LLM-formulated answer or `ExtractedData` for full search results that you can pass to an LLM as a downstream step. | String | Yes |
-| `Models` | A connection to a [supported LLM](#supported-models) used for answer formulation or query planning. In this preview, `Models` can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Foundry portal or a command-line request. Provide the parameters by using the [KnowledgeBaseAzureOpenAIModel class](/dotnet/api/azure.search.documents.indexes.models.knowledgebaseazureopenaimodel?view=azure-dotnet-preview&preserve-view=true). You can use role-based access control instead of API keys for the Azure AI Search connection to the model. For more information, see [How to deploy Azure OpenAI models with Foundry](/azure/ai-foundry/how-to/deploy-models-openai). | Object | No |
+| `Models` | A connection to a [supported LLM](#supported-models) used for answer formulation or query planning. In this preview, `Models` can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Foundry portal or a command-line request. Provide the parameters by using the [KnowledgeBaseAzureOpenAIModel class](/dotnet/api/azure.search.documents.indexes.models.knowledgebaseazureopenaimodel?view=azure-dotnet-preview&preserve-view=true). You can use role-based access control instead of API keys for the Azure AI Search connection to the model. | Object | No |
 | `RetrievalReasoningEffort` | Determines the level of LLM-related query processing. Valid values are `minimal`, `low` (default), and `medium`. For more information, see [Set the retrieval reasoning effort](../../agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). | Object | No |
 
 ## Query a knowledge base
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント情報検索に関するC#の知識ベース作成ガイドの修正"
}
```

### Explanation
この変更は、C#におけるエージェント情報検索の知識ベースを作成するためのガイドに対する軽微な更新です。主に、使用する大規模言語モデル（LLM）に関する記述が改訂されました。具体的には、Azure OpenAIからのLLMをFoundry Modelsの中で使用する際に、`"gpt-4o"`と`"gpt-4o-mini"`の2つのモデルが明示的に追加されました。また、ドキュメント内の文の構造が一部明確化されています。これにより、ユーザーは推奨されるモデルとそのデプロイ方法に関する情報をより理解しやすくなります。変更は合計で4行に及び、2行の追加と2行の削除が含まれています。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-python.md{#item-4e498f}

<details>
<summary>Diff</summary>
````diff
@@ -45,7 +45,7 @@ After you create a knowledge base, you can update its properties at any time. If
 
 ### Supported models
 
-Use one of the following LLMs from Azure OpenAI in Foundry Models or an equivalent open-source model. For deployment instructions, see [Deploy Microsoft Foundry Models in the Foundry portal](/azure/ai-foundry/how-to/deploy-models-openai).
+Use one of the following LLMs from Azure OpenAI in Foundry Models. For deployment instructions, see [Deploy Microsoft Foundry Models in the Foundry portal](/azure/ai-foundry/how-to/deploy-models-openai).
 
 + `gpt-4o`
 + `gpt-4o-mini`
@@ -201,7 +201,7 @@ Pass the following properties to create a knowledge base.
 | `answer_instructions` | Custom instructions to shape synthesized answers. The default is null. For more information, see [Use answer synthesis for citation-backed responses](../../agentic-retrieval-how-to-answer-synthesis.md). | String | Yes |
 | `output_mode` | Valid values are `answer_synthesis` for an LLM-formulated answer or `extracted_data` for full search results that you can pass to an LLM as a downstream step. | String | Yes |
 | `knowledge_sources` | One or more [supported knowledge sources](../../agentic-knowledge-source-overview.md#supported-knowledge-sources). | Array | Yes |
-| `models` | A connection to a [supported LLM](#supported-models) used for answer formulation or query planning. In this preview, `models` can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Foundry portal or a command-line request. You can use role-based access control instead of API keys for the Azure AI Search connection to the model. For more information, see [How to deploy Azure OpenAI models with Foundry](/azure/ai-foundry/how-to/deploy-models-openai). | Object | No |
+| `models` | A connection to a [supported LLM](#supported-models) used for answer formulation or query planning. In this preview, `models` can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Foundry portal or a command-line request. You can use role-based access control instead of API keys for the Azure AI Search connection to the model. | Object | No |
 | `encryption_key` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge base and the generated objects. | Object | No |
 | `retrieval_reasoning_effort` | Determines the level of LLM-related query processing. Valid values are `minimal`, `low` (default), and `medium`. For more information, see [Set the retrieval reasoning effort](../../agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). | Object | No |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント情報検索に関するPythonの知識ベース作成ガイドの修正"
}
```

### Explanation
この変更は、Pythonを使用したエージェント情報検索の知識ベースを作成するためのガイドに対する軽微な更新です。主な改訂点は、使用する大規模言語モデル（LLM）に関連する記述の明確化です。具体的には、Azure OpenAIからのLLMをFoundry Models内で使用する際の説明が修正され、`"gpt-4o"`と`"gpt-4o-mini"`の二つのモデルが新たに追加されました。また、ドキュメント内の用語や構文が整理され、全体的に理解しやすくなっています。変更内容は合計4行で、2行が追加され、2行が削除されています。この更新により、ユーザーは最新のモデルや設定に関する情報をより簡単に得られるようになります。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-rest.md{#item-37851c}

<details>
<summary>Diff</summary>
````diff
@@ -45,7 +45,7 @@ After you create a knowledge base, you can update its properties at any time. If
 
 ### Supported models
 
-Use one of the following LLMs from Azure OpenAI in Foundry Models or an equivalent open-source model. For deployment instructions, see [Deploy Microsoft Foundry Models in the Foundry portal](/azure/ai-foundry/how-to/deploy-models-openai).
+Use one of the following LLMs from Azure OpenAI in Foundry Models. For deployment instructions, see [Deploy Microsoft Foundry Models in the Foundry portal](/azure/ai-foundry/how-to/deploy-models-openai).
 
 + `gpt-4o`
 + `gpt-4o-mini`
@@ -195,7 +195,7 @@ Pass the following properties to create a knowledge base.
 | `answerInstructions` | Custom instructions to shape synthesized answers. The default is null. For more information, see [Use answer synthesis for citation-backed responses](../../agentic-retrieval-how-to-answer-synthesis.md). | String | Yes |
 | `outputMode` | Valid values are `answerSynthesis` for an LLM-formulated answer or `extractedData` for full search results that you can pass to an LLM as a downstream step. | String | Yes |
 | `knowledgeSources` | One or more [supported knowledge sources](../../agentic-knowledge-source-overview.md#supported-knowledge-sources). | Array | Yes |
-| `models` | A connection to a [supported LLM](#supported-models) used for answer formulation or query planning. In this preview, `models` can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Foundry portal or a command-line request. You can use role-based access control instead of API keys for the Azure AI Search connection to the model. For more information, see [How to deploy Azure OpenAI models with Foundry](/azure/ai-foundry/how-to/deploy-models-openai). | Object | No |
+| `models` | A connection to a [supported LLM](#supported-models) used for answer formulation or query planning. In this preview, `models` can contain just one model, and the model provider must be Azure OpenAI. Obtain model information from the Foundry portal or a command-line request. You can use role-based access control instead of API keys for the Azure AI Search connection to the model. | Object | No |
 | `encryptionKey` | A [customer-managed key](../../search-security-manage-encryption-keys.md) to encrypt sensitive information in both the knowledge base and the generated objects. | Object | No |
 | `retrievalReasoningEffort.kind` | Determines the level of LLM-related query processing. Valid values are `minimal`, `low` (default), and `medium`. For more information, see [Set the retrieval reasoning effort](../../agentic-retrieval-how-to-set-retrieval-reasoning-effort.md). | Object | No |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント情報検索に関するREST APIの知識ベース作成ガイドの修正"
}
```

### Explanation
この変更は、REST APIを使用したエージェント情報検索の知識ベースを作成するためのガイドに対する軽微な更新です。変更の主な内容は、使用する大規模言語モデル（LLM）に関する説明の更新です。具体的には、Azure OpenAIから利用可能なLLMのリストが修正され、`"gpt-4o"`および`"gpt-4o-mini"`の二つのモデルが追加されました。また、文書内の構成が整理され、ユーザーに提供される情報の明確さが向上しています。変更は合計で4行に及び、2行が新たに追加され、2行が削除されています。この更新によって、ユーザーは推奨されるモデルやその利用方法について、より明確な情報を得られるようになります。

## articles/search/includes/quickstarts/agentic-retrieval-csharp.md{#item-f93ed3}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ Although you can use your own data, this quickstart uses [sample JSON documents]
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md).
++ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md). This quickstart requires the Basic tier or higher for managed identity support.
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#を使用したエージェント情報検索のクイックスタートガイドの修正"
}
```

### Explanation
この変更は、C#を用いたエージェント情報検索のクイックスタートガイドに対する軽微な更新です。変更点は主に、Azure AI Searchサービスに関する要件の明確化です。具体的には、Azure AI Searchサービスが必要な場合、マネージドアイデンティティサポートのためには基本プラン以上が求められることが追記されました。また、他の要件についての表現も微調整されています。変更は合計で2行に及び、1行が追加され、1行が削除されています。この更新により、ユーザーは必要なサービスのプランについてより具体的な情報を得られるようになります。

## articles/search/includes/quickstarts/agentic-retrieval-java.md{#item-4e2c55}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ Although you can use your own data, this quickstart uses [sample JSON documents]
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md).
++ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md). This quickstart requires the Basic tier or higher for managed identity support.
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaを使用したエージェント情報検索のクイックスタートガイドの修正"
}
```

### Explanation
この変更は、Javaを用いたエージェント情報検索のクイックスタートガイドに対する軽微な更新です。主な内容は、Azure AI Searchサービスに関連する要件の追加です。具体的には、利用するAzure AI Searchサービスが必要な場合、マネージドアイデンティティサポートのためには基本プラン以上が必要であることが明記されました。この修正により、ユーザーが必要なプランについての理解を深めることができ、設定作業を円滑に進められるようになります。変更は合計で2行に及び、1行が追加され、1行が削除されています。

## articles/search/includes/quickstarts/agentic-retrieval-javascript.md{#item-715283}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ Although you can use your own data, this quickstart uses [sample JSON documents]
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md).
++ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md). This quickstart requires the Basic tier or higher for managed identity support.
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptを使用したエージェント情報検索のクイックスタートガイドの修正"
}
```

### Explanation
この変更は、JavaScriptを用いたエージェント情報検索のクイックスタートガイドにおける軽微な修正です。この修正では、Azure AI Searchサービスの利用に関する要件が更新されました。具体的に言うと、Azure AI Searchサービスが必要な場合、マネージドアイデンティティサポートのために基本プラン以上が要求されることが付け加えられました。この修正によって、ユーザーは必要なサービスのプランについてのより明確な情報を得ることができ、設定をスムーズに行えるようになります。変更内容は2行にわたり、1行が新たに追加され、1行が削除されています。

## articles/search/includes/quickstarts/agentic-retrieval-python.md{#item-efee6a}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ Although you can use your own data, this quickstart uses [sample JSON documents]
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md).
++ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md). This quickstart requires the Basic tier or higher for managed identity support.
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonを使用したエージェント情報検索のクイックスタートガイドの修正"
}
```

### Explanation
この変更は、Pythonを用いたエージェント情報検索のクイックスタートガイドに対する軽微な更新を示しています。具体的には、Azure AI Searchサービスに関連する要件が追加されており、このクイックスタートがマネージドアイデンティティサポートのために基本プラン以上を必要とすることが明記されています。この情報は、ユーザーが使用するサービスのプランを正しく理解するために重要です。変更内容は合計で2行にわたり、1行が追加され、1行が削除されています。

## articles/search/includes/quickstarts/agentic-retrieval-rest.md{#item-3df373}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ Although you can use your own data, this quickstart uses [sample JSON documents]
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md).
++ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md). This quickstart requires the Basic tier or higher for managed identity support.
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
@@ -69,7 +69,7 @@ Although you can use your own data, this quickstart uses [sample JSON documents]
    az account get-access-token --scope https://search.azure.com/.default --query accessToken --output tsv
    ```
 
-1. Replace the placeholder value for `@token` with the access token from the previous step.
+1. Replace the placeholder value for `@token` with the token from the previous step.
 
 ## Run the code
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTを使用したエージェント情報検索のクイックスタートガイドの修正"
}
```

### Explanation
この変更は、RESTを使用したエージェント情報検索のクイックスタートガイドに対する軽微な修正を示しています。主な更新内容としては、Azure AI Searchサービスの利用に関する要件に、マネージドアイデンティティサポートのために基本プラン以上が必要であることが追記されました。また、手順項目の一部において、"access token" から "token" への表現変更が行われています。これにより、手順がより簡潔でわかりやすくなります。変更された箇所は合計で4行で、2行が追加され、2行が削除されています。ユーザーは、必要なサービスのプランと手順についてのより明確な情報を得ることができます。

## articles/search/includes/quickstarts/agentic-retrieval-typescript.md{#item-e6370b}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ Although you can use your own data, this quickstart uses [sample JSON documents]
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-+ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md).
++ An [Azure AI Search service](../../search-create-service-portal.md) in any [region that provides agentic retrieval](../../search-region-support.md). This quickstart requires the Basic tier or higher for managed identity support.
 
 + A [Microsoft Foundry project](/azure/ai-foundry/how-to/create-projects) and resource. When you create a project, the resource is automatically created.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptを使用したエージェント情報検索のクイックスタートガイドの修正"
}
```

### Explanation
この変更は、TypeScriptを用いたエージェント情報検索のクイックスタートガイドに対する軽微な更新を示しています。具体的には、Azure AI Searchサービスを使用する際の要件として、マネージドアイデンティティサポートのために基本プラン以上が必要であることが新たに追加されました。この情報により、ユーザーは適切なサービスプランを選択する際に重要な指針を得ることができます。変更は合計で2行にわたり、1行が追加され、1行が削除されています。これにより、ガイドの正確性と明確さが向上しています。

## articles/search/includes/quickstarts/full-text-rest.md{#item-5d3419}

<details>
<summary>Diff</summary>
````diff
@@ -63,7 +63,7 @@ Full-text search uses Apache Lucene for indexing and queries and the BM25 rankin
     az account get-access-token --scope https://search.azure.com/.default --query accessToken -o tsv
     ```
 
-1. Replace the placeholder value for `@token` with the access token from the previous step.
+1. Replace the placeholder value for `@token` with the token from the previous step.
 
 ## Run the code
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フルテキスト検索のRESTクイックスタートガイドの修正"
}
```

### Explanation
この変更は、フルテキスト検索のRESTクイックスタートガイドに対する軽微な調整を示しています。具体的な修正内容は、手順の一部において、`access token` という表現が `token` へと変更された点です。この変更により、指示がより簡潔になり、理解しやすくなっています。全体として、変更は2行にわたり、1行の追加と1行の削除が行われました。これにより、ユーザーは前のステップから得られるトークンの扱いについて、より明確な指示を受け取ることができます。

## articles/search/includes/quickstarts/search-get-started-portal-new-wizard.md{#item-114e35}

<details>
<summary>Diff</summary>
````diff
@@ -1,159 +0,0 @@
----
-manager: nitinme
-author: haileytap
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 01/15/2026
----
-
-> [!IMPORTANT]
-> The **Import data (new)** wizard now supports keyword search, which was previously only available in the **Import data** wizard. We recommend the new wizard for an improved search experience. For more information about how we're consolidating the wizards, see [Import data wizards in the Azure portal](../../search-import-data-portal.md).
-
-In this quickstart, you use the **Import data (new)** wizard and sample data about fictitious hotels to get started with [full-text search](../../search-lucene-query-architecture.md), also known as keyword search. The wizard requires no code to create an index, helping you write interesting queries within minutes.
-
-The wizard creates multiple objects on your search service, including a searchable index, an indexer, and a data source connection for automated data retrieval. At the end of this quickstart, you review each object.
-
-## Prerequisites
-
-+ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-
-+ An [Azure AI Search service](../../search-create-service-portal.md). You can use a free service for this quickstart.
-
-+ An [Azure Storage account](/azure/storage/common/storage-account-create). Use Azure Blob Storage or Azure Data Lake Storage Gen2 (storage account with a hierarchical namespace) on a standard performance (general-purpose v2) account. To avoid bandwidth charges, use the same region as Azure AI Search.
-
-+ Familiarity with the wizard. See [Import data wizards in the Azure portal](../../search-import-data-portal.md).
-
-### Check for network access
-
-For this quickstart, all of the preceding resources must have public access enabled so that the Azure portal nodes can access them. Otherwise, the wizard fails. After the wizard runs, you can enable firewalls and private endpoints on the integration components for security. For more information, see [Secure connections in the import wizards](../../search-import-data-portal.md#secure-connections).
-
-### Check for space
-
-Many customers start with a free search service, which is limited to three indexes, three indexers, and three data sources. This quickstart creates one of each, so before you begin, make sure you have room for extra objects.
-
-On the **Overview** page, select **Usage** to see how many indexes, indexers, and data sources you currently have.
-
-   :::image type="content" source="../../media/search-get-started-portal/overview-quota-usage.png" alt-text="Screenshot of the Overview page for an Azure AI Search service instance in the Azure portal, showing the number of indexes, indexers, and data sources." lightbox="../../media/search-get-started-portal/overview-quota-usage.png":::
-
-## Prepare sample data
-
-This quickstart uses a JSON document that contains metadata for 50 fictitious hotels, but you can also use your own files.
-
-To prepare the sample data for this quickstart:
-
-1. Download the `HotelsData_toAzureBlobs.json` file from the [azure-search-sample-data](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toAzureBlobs.json) repo.
-
-1. Sign in to the [Azure portal](https://portal.azure.com/) and select your Azure Storage account.
-
-1. From the left pane, select **Data storage** > **Containers**.
-
-1. Create a container named **hotels-sample**.
-
-1. Upload the `HotelsData_toAzureBlobs.json` file to the container.
-
-## Run the wizard
-
-The wizard walks you through several configuration steps. This section covers each step in sequence.
-
-### Start the wizard
-
-To start the wizard for this quickstart:
-
-1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
-
-1. On the **Overview** page, select **Import data (new)**.
-
-   :::image type="content" source="../../media/search-import-data-portal/import-data-new-button.png" alt-text="Screenshot that shows how to open the new import wizard in the Azure portal.":::
-
-1. Select your data source: **Azure Blob Storage** or **Azure Data Lake Storage Gen2**.
-
-   :::image type="content" source="../../media/search-get-started-portal-images/select-data-source.png" alt-text="Screenshot of the options for selecting a data source in the wizard." border="true" lightbox="../../media/search-get-started-portal-images/select-data-source.png":::
-
-1. Select **Keyword search**.
-
-   :::image type="content" source="../../media/search-get-started-portal/keyword-search-tile.png" alt-text="Screenshot of the keyword search tile in the Azure portal." border="true" lightbox="../../media/search-get-started-portal/keyword-search-tile.png":::
-
-### Connect to a data source
-
-Azure AI Search requires a connection to a data source for content ingestion and indexing. In this case, the data source is your Azure Storage account.
-
-To connect to the sample data:
-
-1. On the **Connect to your data** page, select your Azure subscription.
-
-1. Select your storage account, and then select the **hotels-sample** container.
-
-1. Select **JSON array** for the parsing mode.
-
-   :::image type="content" source="../../media/search-get-started-portal/connect-to-your-data.png" alt-text="Screenshot of the Connect to your data page in the Azure portal." lightbox="../../media/search-get-started-portal/connect-to-your-data.png":::
-
-1. Select **Next**.
-
-### Skip AI enrichment
-
-The wizard supports skillset creation and [AI enrichment](../../cognitive-search-concept-intro.md) during indexing, which are beyond the scope of this quickstart. Skip this step by selecting **Next**.
-
-> [!TIP]
-> For a similar walkthrough that focuses on AI enrichment, see [Quickstart: Create a skillset in the Azure portal](../../search-get-started-skillset.md).
-
-### Configure the index
-
-Based on the structure and content of the sample hotel data, the wizard infers a schema for your search index.
-
-To configure the index:
-
-1. For each of the following fields, select **Configure field**, and then set the respective attributes.
-
-   | Fields | Attributes |
-   |-------|------------|
-   | `HotelId` | Key, Retrievable, Filterable, Sortable, Searchable |
-   | `HotelName`, `Category` | Retrievable, Filterable, Sortable, Searchable |
-   | `Description`, `Description_fr` | Retrievable, Searchable |
-   | `Tags` | Retrievable, Filterable, Searchable |
-   | `ParkingIncluded`, `IsDeleted` | Retrievable, Filterable, Facetable |
-   | `LastRenovationDate`, `Rating`, `Location` | Retrievable, Filterable, Sortable |
-   | `Address.StreetAddress`, `Rooms.Description`, `Rooms.Description_fr` | Retrievable, Searchable |
-   | `Address.City`, `Address.StateProvince`, `Address.PostalCode`, `Address.Country` | Retrievable, Filterable, Facetable, Searchable, Sortable|
-   | `Rooms.Type`, `Rooms.BedOptions`, `Rooms.Tags` | Retrievable, Filterable, Facetable, Searchable |
-   | `Rooms.BaseRate`, `Rooms.SleepsCount`, `Rooms.SmokingAllowed` | Retrievable, Filterable, Facetable |
-
-   :::image type="content" source="../../media/search-get-started-portal/configure-index.gif" alt-text="GIF that shows how to configure attributes for fields in the index." lightbox="../../media/search-get-started-portal/configure-index.gif":::
-
-1. Select **Next**.
-
-At a minimum, the index requires a name and a collection of fields. The wizard scans for unique string fields and marks one as the document key, which uniquely identifies each document in the index.
-
-Each field has a name, [data type](/rest/api/searchservice/supported-data-types), and attributes that control how the field is used in the index. You can enable or disable the following attributes:
-
-| Attribute | Description | Applicable data types |
-|-----------|-------------|------------------------|
-| Retrievable | Fields returned in a query response. | Strings and integers |
-| Filterable | Fields that accept a filter expression. | Strings and integers |
-| Sortable | Fields that accept an orderby expression. | Strings and integers |
-| Facetable | Fields used in a faceted navigation structure. | Strings and integers |
-| Searchable | Fields used in full-text search. Strings are searchable, but numeric and Boolean fields are often marked as not searchable. | Strings |
-
-Attributes affect storage in different ways. For example, filterable fields consume extra storage, while retrievable fields don't. For more information about attributes and data types, see [Configure field definitions](/azure/search/search-how-to-create-search-index#configure-field-definitions).
-
-If you want autocomplete or suggested queries, specify **Suggesters**.
-
-### Skip advanced settings
-
-The wizard offers advanced settings for semantic ranking and index scheduling, which are beyond the scope of this quickstart. Skip this step by selecting **Next**.
-
-### Finish the wizard
-
-The last step is to review your configuration and create the index, indexer, and data source on your search service. The indexer automates the process of extracting content from your data source and loading it into the index, enabling keyword search.
-
-To finish the wizard:
-
-1. Change the object name prefix to **hotels-sample**.
-
-1. Review the object configurations.
-
-   :::image type="content" source="../../media/search-get-started-portal/review-and-create.png" alt-text="Screenshot of the object configuration page in the Azure portal." lightbox="../../media/search-get-started-portal/review-and-create.png":::
-
-   AI enrichment, semantic ranker, and indexer scheduling are either disabled or set to their default values because you skipped their wizard steps.
-
-1. Select **Create** to simultaneously create the objects and run the indexer.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "クイックスタートガイドの削除: ポータルの新ウィザードを使った検索の開始"
}
```

### Explanation
この変更は、ポータルの新ウィザードを使用した検索の開始に関するクイックスタートガイドが削除されたことを示しています。このファイルは159行の内容を含んでいましたが、すべての行が削除され、新たに追加されたコンテンツはありません。削除された内容には、ウィザードを利用したデータのインポート方法や、サンプルデータの準備、ウィザードの手順に関する詳細なガイダンスが含まれていました。この変更は、ユーザーがAzure AI Searchの機能を理解し、利用するための重要なリソースが失われたことを意味しています。

## articles/search/includes/quickstarts/search-get-started-vector-csharp.md{#item-9e800b}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#向けベクトル検索クイックスタートガイドの名称変更"
}
```

### Explanation
この変更は、C#向けのベクトル検索に関するクイックスタートガイドのファイル名が変更されたことを示しています。以前のファイル名は `search-get-started-vector-dotnet.md` であり、現在のファイル名は `search-get-started-vector-csharp.md` です。この変更は、ファイルのコンテンツには影響を与えず、ただ名称がより適切で明確になるように調整されたものです。これにより、ユーザーはC#（Cシャープ）に特化した情報をより容易に見つけることができるようになります。

## articles/search/includes/quickstarts/search-get-started-vector-rest.md{#item-c7d261}

<details>
<summary>Diff</summary>
````diff
@@ -68,7 +68,7 @@ In Azure AI Search, a vector index has an index schema that defines vector and n
     az account get-access-token --scope https://search.azure.com/.default --query accessToken -o tsv
     ```
 
-1. Replace the placeholder value for `@token` with the access token from the previous step.
+1. Replace the placeholder value for `@token` with the token from the previous step.
 
 ## Run the code
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIによるベクトル検索クイックスタートガイドの内容修正"
}
```

### Explanation
この変更は、REST APIを使用したベクトル検索に関するクイックスタートガイドの内容が修正されたことを示しています。具体的には、69行目の説明文が微妙に変更されており、トークンの取得方法に関する記述が「access token」から「token」に簡潔になりました。この変更は、情報の明確さを向上させ、ユーザーに対してよりシンプルな表現を提供することを目的としています。変更に伴う行数の追加は1行、削除は1行であり、全体的な内容には大きな影響は与えていません。

## articles/search/includes/quickstarts/search-get-started-vector-typescript.md{#item-9b3bc8}

<details>
<summary>Diff</summary>
````diff
@@ -74,6 +74,12 @@ In Azure AI Search, a vector index has an index schema that defines vector and n
 
    When the installation completes, you should see a `node_modules` folder in the project directory.
 
+1. Build the TypeScript files.
+
+   ```bash
+   npm run build
+   ```
+
 1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
    ```azurecli
@@ -85,32 +91,32 @@ In Azure AI Search, a vector index has an index schema that defines vector and n
 1. Create a vector index.
 
     ```bash
-    npm run build && node -r dotenv/config dist/createIndex.js
+    node -r dotenv/config dist/createIndex.js
     ```
 
 1. Load documents that contain precomputed embeddings.
 
     ```bash
-    npm run build && node -r dotenv/config dist/uploadDocuments.js
+    node -r dotenv/config dist/uploadDocuments.js
     ```
 
 1. Run a vector search query.
 
     ```bash
-    npm run build && node -r dotenv/config dist/searchSingle.js
+    node -r dotenv/config dist/searchSingle.js
     ```
 
 1. (Optional) Run additional query variations.
 
     ```bash
-    npm run build && node -r dotenv/config dist/searchSingleWithFilter.js
-    npm run build && node -r dotenv/config dist/searchSingleWithFilterGeo.js
-    npm run build && node -r dotenv/config dist/searchHybrid.js
-    npm run build && node -r dotenv/config dist/searchSemanticHybrid.js
+    node -r dotenv/config dist/searchSingleWithFilter.js
+    node -r dotenv/config dist/searchSingleWithFilterGeo.js
+    node -r dotenv/config dist/searchHybrid.js
+    node -r dotenv/config dist/searchSemanticHybrid.js
     ```
 
-> [!NOTE]
-> The `npm run build` command compiles the TypeScript files in `src/` to JavaScript in `dist/`.
+    > [!NOTE]
+    > These commands run `.js` files from the `dist` folder because you previously transpiled from TypeScript to JavaScript with `npm run build`.
 
 ### Output
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptによるベクトル検索クイックスタートガイドの内容修正"
}
```

### Explanation
この変更は、TypeScriptを使用したベクトル検索に関するクイックスタートガイドの内容が修正されたことを示しています。具体的には、新たにTypeScriptファイルをビルドする手順が追加され、既存の手順であるインデックスの作成や文書のアップロード、検索クエリの実行に関する記述が更新されています。

新しい手順では、TypeScriptファイルをビルドするためのコマンドが明確に説明され、ビルド後に実行するコマンドが示されています。また、以前の手順であった「npm run build」との明確な関連性が強調されています。それにより、ユーザーはビルド工程をより理解しやすくなります。全体として、15行が追加され、9行が削除され、24行が変更されたことが記録されていますが、これらの変更はドキュメントの可読性と明確さを向上させるものであるといえます。

## articles/search/includes/quickstarts/semantic-ranker-csharp.md{#item-09fa32}

<details>
<summary>Diff</summary>
````diff
@@ -4,442 +4,377 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
+  - dev-focus
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 03/04/2026
+ai-usage: ai-assisted
 ---
 
-[!INCLUDE [Semantic ranker introduction](semantic-ranker-intro.md)]
+In this quickstart, you use the [Azure AI Search client library for .NET](/dotnet/api/overview/azure/search) to add [semantic ranking](../../semantic-search-overview.md) to an existing search index and query the index.
 
-## Set up the client
+Semantic ranking is query-side functionality that uses machine reading comprehension to rescore search results, promoting the most semantically relevant matches to the top of the list. You can add a semantic configuration to an existing index with no rebuild requirement. Semantic ranking is most effective for informational or descriptive text.
 
-In this quickstart, you use an IDE and the [**Azure.Search.Documents**](/dotnet/api/overview/azure/search.documents-readme) client library to add semantic ranking to an existing search index.
+> [!TIP]
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-semantic-ranking) on GitHub.
 
-We recommend [Visual Studio](https://visualstudio.microsoft.com/vs/community/) for this quickstart.
+## Prerequisites
 
-> [!TIP]
-> You can download the [source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-semantic-ranking) to start with a finished project or follow these steps to create your own.
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-### Install libraries
++ An [Azure AI Search service](../../search-create-service-portal.md) with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
 
-1. Start Visual Studio and open the [quickstart-semantic-ranking.sln](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-semantic-ranking) or create a new project using a console application template.
++ An [index](../../search-how-to-create-search-index.md) with descriptive text fields attributed as `searchable` and `retrievable`.  This quickstart assumes the [hotels-sample index](../../search-get-started-portal.md).
 
-1. In **Tools** > **NuGet Package Manager**, select **Manage NuGet Packages for Solution...**.
++ [.NET 9](https://dotnet.microsoft.com/download) or later.
 
-1. Select **Browse**.
++ [Visual Studio Code](https://code.visualstudio.com/download).
 
-1. Search for the [Azure.Search.Documents package](https://www.nuget.org/packages/Azure.Search.Documents/) and select the latest stable version.
++ [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-1. Search for the [Azure.Identity package](https://www.nuget.org/packages/Azure.Identity) and select the latest stable version.
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-1. Select **Install** to add the assembly to your project and solution.
+## Configure access
 
-### Sign in to Azure
+[!INCLUDE [resource authentication](../resource-authentication-semantic.md)]
 
-If you signed in to the [Azure portal](https://portal.azure.com), you're signed into Azure. If you aren't sure, use the Azure CLI or Azure PowerShell to log in: `az login` or `az connect`. If you have multiple tenants and subscriptions, see [Quickstart: Connect without keys](../../search-get-started-rbac.md) for help on how to connect.
+## Get endpoint
 
-## Update the index
+[!INCLUDE [resource endpoint](../resource-endpoint.md)]
 
-In this section, you update a search index to include a semantic configuration. The code gets the index definition from the search service and adds a semantic configuration.
+## Start with an index
 
-1. Open the [BuildIndex project](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-semantic-ranking/BuildIndex) in Visual Studio. The program consists of the following code.
+[!INCLUDE [start with an index](semantic-ranker-index.md)]
 
-   This code uses a SearchIndexClient to update an index on your search service.
+## Set up the environment
 
-    ```csharp
-    class BuildIndex
-    {
-        static async Task Main(string[] args)
-        {
-            string searchServiceName = "PUT-YOUR-SEARCH-SERVICE-NAME-HERE";
-            string indexName = "hotels-sample-index";
-            string endpoint = $"https://{searchServiceName}.search.windows.net";
-            var credential = new Azure.Identity.DefaultAzureCredential();
-    
-            await ListIndexesAsync(endpoint, credential);
-            await UpdateIndexAsync(endpoint, credential, indexName);
-        }
-    
-        // Print a list of all indexes on the search service
-        // You should see hotels-sample-index in the list
-        static async Task ListIndexesAsync(string endpoint, Azure.Core.TokenCredential credential)
-        {
-            try
-            {
-                var indexClient = new Azure.Search.Documents.Indexes.SearchIndexClient(
-                    new Uri(endpoint),
-                    credential
-                );
-    
-                var indexes = indexClient.GetIndexesAsync();
-    
-                Console.WriteLine("Here's a list of all indexes on the search service. You should see hotels-sample-index:");
-                await foreach (var index in indexes)
-                {
-                    Console.WriteLine(index.Name);
-                }
-                Console.WriteLine(); // Add an empty line for readability
-            }
-            catch (Exception ex)
-            {
-                Console.WriteLine($"Error listing indexes: {ex.Message}");
-            }
-        }
-    
-        static async Task UpdateIndexAsync(string endpoint, Azure.Core.TokenCredential credential, string indexName)
-        {
-            try
-            {
-                var indexClient = new Azure.Search.Documents.Indexes.SearchIndexClient(
-                    new Uri(endpoint),
-                    credential
-                );
-    
-                // Get the existing definition of hotels-sample-index
-                var indexResponse = await indexClient.GetIndexAsync(indexName);
-                var index = indexResponse.Value;
-    
-                // Add a semantic configuration
-                const string semanticConfigName = "semantic-config";
-                AddSemanticConfiguration(index, semanticConfigName);
-    
-                // Update the index with the new information
-                var updatedIndex = await indexClient.CreateOrUpdateIndexAsync(index);
-                Console.WriteLine("Index updated successfully.");
-    
-                // Print the updated index definition as JSON
-                var refreshedIndexResponse = await indexClient.GetIndexAsync(indexName);
-                var refreshedIndex = refreshedIndexResponse.Value;
-                var jsonOptions = new JsonSerializerOptions { WriteIndented = true };
-                string indexJson = JsonSerializer.Serialize(refreshedIndex, jsonOptions);
-                Console.WriteLine($"Here is the revised index definition:\n{indexJson}");
-            }
-            catch (Exception ex)
-            {
-                Console.WriteLine($"Error updating index: {ex.Message}");
-            }
-        }
-    
-        // This is the semantic configuration definition
-        static void AddSemanticConfiguration(SearchIndex index, string semanticConfigName)
-        {
-            if (index.SemanticSearch == null)
-            {
-                index.SemanticSearch = new SemanticSearch();
-            }
-            var configs = index.SemanticSearch.Configurations;
-            if (configs == null)
-            {
-                throw new InvalidOperationException("SemanticSearch.Configurations is null and cannot be assigned. Your service must be Basic tier or higher.");
-            }
-            if (!configs.Any(c => c.Name == semanticConfigName))
-            {
-                var prioritizedFields = new SemanticPrioritizedFields
-                {
-                    TitleField = new SemanticField("HotelName"),
-                    ContentFields = { new SemanticField("Description") },
-                    KeywordsFields = { new SemanticField("Tags") }
-                };
-    
-                configs.Add(
-                    new SemanticConfiguration(
-                        semanticConfigName,
-                        prioritizedFields
-                    )
-                );
-                Console.WriteLine($"Added new semantic configuration '{semanticConfigName}' to the index definition.");
-            }
-            else
-            {
-                Console.WriteLine($"Semantic configuration '{semanticConfigName}' already exists in the index definition.");
-            }
-            index.SemanticSearch.DefaultConfigurationName = semanticConfigName;
-        }
-    }
+1. Use Git to clone the sample repository.
+
+    ```bash
+    git clone https://github.com/Azure-Samples/azure-search-dotnet-samples
     ```
 
-1. Replace the search service URL with a valid endpoint.
+1. Navigate to the quickstart folder and open it in Visual Studio Code.
 
-1. Run the program.
+    ```bash
+    cd azure-search-dotnet-samples/quickstart-semantic-ranking
+    code .
+    ```
 
-1. Output is logged to a console window from [Console.WriteLine](/dotnet/api/system.console.writeline). You should see messages for each step, including the JSON of the index schema with the new semantic configuration included.
+1. In `BuildIndex/Program.cs`, replace the placeholder value for `endpoint` with the URL you obtained in [Get endpoint](#get-endpoint).
 
-## Run semantic queries
+1. Repeat the previous step for `QueryIndex/Program.cs`.
 
-In this section, the program runs several semantic queries in sequence.
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
-1. Open the [QueryIndex project](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart-semantic-ranking/QueryIndex) in Visual Studio. The program consists of the following code.
+    ```azurecli
+    az login
+    ```
 
-   This code uses a SearchClient for sending queries to an index.
+## Run the code
 
-    ```csharp
-    class SemanticQuery
-    {
-        static async Task Main(string[] args)
-        {
-            string searchServiceName = "PUT-YOUR-SEARCH-SERVICE-NAME-HERE";
-            string indexName = "hotels-sample-index";
-            string endpoint = $"https://{searchServiceName}.search.windows.net";
-            var credential = new Azure.Identity.DefaultAzureCredential();
-    
-            var client = new SearchClient(new Uri(endpoint), indexName, credential);
-    
-            // Query 1: Simple query
-            string searchText = "walking distance to live music";
-            Console.WriteLine("\nQuery 1: Simple query using the search string 'walking distance to live music'.");
-            await RunQuery(client, searchText, new SearchOptions
-            {
-                Size = 5,
-                QueryType = SearchQueryType.Simple,
-                IncludeTotalCount = true,
-                Select = { "HotelId", "HotelName", "Description" }
-            });
-            Console.WriteLine("Press Enter to continue to the next query...");
-            Console.ReadLine();
-    
-            // Query 2: Semantic query (no captions, no answers)
-            Console.WriteLine("\nQuery 2: Semantic query (no captions, no answers) for 'walking distance to live music'.");
-            var semanticOptions = new SearchOptions
-            {
-                Size = 5,
-                QueryType = SearchQueryType.Semantic,
-                SemanticSearch = new SemanticSearchOptions
-                {
-                    SemanticConfigurationName = "semantic-config"
-                },
-                IncludeTotalCount = true,
-                Select = { "HotelId", "HotelName", "Description" }
-            };
-            await RunQuery(client, searchText, semanticOptions);
-            Console.WriteLine("Press Enter to continue to the next query...");
-            Console.ReadLine();
-    
-            // Query 3: Semantic query with captions
-            Console.WriteLine("\nQuery 3: Semantic query with captions.");
-            var captionsOptions = new SearchOptions
-            {
-                Size = 5,
-                QueryType = SearchQueryType.Semantic,
-                SemanticSearch = new SemanticSearchOptions
-                {
-                    SemanticConfigurationName = "semantic-config",
-                    QueryCaption = new QueryCaption(QueryCaptionType.Extractive)
-                    {
-                        HighlightEnabled = true
-                    }
-                },
-                IncludeTotalCount = true,
-                Select = { "HotelId", "HotelName", "Description" }
-            };
-            // Add the field(s) you want captions for to the QueryCaption.Fields collection
-            captionsOptions.HighlightFields.Add("Description");
-            await RunQuery(client, searchText, captionsOptions, showCaptions: true);
-            Console.WriteLine("Press Enter to continue to the next query...");
-            Console.ReadLine();
-    
-            // Query 4: Semantic query with answers
-            // This query uses different search text designed for an answers scenario
-            string searchText2 = "what's a good hotel for people who like to read";
-            searchText = searchText2; // Update searchText for the next query
-            Console.WriteLine("\nQuery 4: Semantic query with a verbatim answer from the Description field for 'what's a good hotel for people who like to read'.");
-            var answersOptions = new SearchOptions
-            {
-                Size = 5,
-                QueryType = SearchQueryType.Semantic,
-                SemanticSearch = new SemanticSearchOptions
-                {
-                    SemanticConfigurationName = "semantic-config",
-                    QueryAnswer = new QueryAnswer(QueryAnswerType.Extractive)
-                },
-                IncludeTotalCount = true,
-                Select = { "HotelId", "HotelName", "Description" }
-            };
-            await RunQuery(client, searchText2, answersOptions, showAnswers: true);
-    
-            static async Task RunQuery(
-            SearchClient client,
-            string searchText,
-            SearchOptions options,
-            bool showCaptions = false,
-            bool showAnswers = false)
-            {
-                try
-                {
-                    var response = await client.SearchAsync<SearchDocument>(searchText, options);
-    
-                    if (showAnswers && response.Value.SemanticSearch?.Answers != null)
-                    {
-                        Console.WriteLine("Extractive Answers:");
-                        foreach (var answer in response.Value.SemanticSearch.Answers)
-                        {
-                            Console.WriteLine($"  {answer.Highlights}");
-                        }
-                        Console.WriteLine(new string('-', 40));
-                    }
-    
-                    await foreach (var result in response.Value.GetResultsAsync())
-                    {
-                        var doc = result.Document;
-                        // Print captions first if available
-                        if (showCaptions && result.SemanticSearch?.Captions != null)
-                        {
-                            foreach (var caption in result.SemanticSearch.Captions)
-                            {
-                                Console.WriteLine($"Caption: {caption.Highlights}");
-                            }
-                        }
-                        Console.WriteLine($"HotelId: {doc.GetString("HotelId")}");
-                        Console.WriteLine($"HotelName: {doc.GetString("HotelName")}");
-                        Console.WriteLine($"Description: {doc.GetString("Description")}");
-                        Console.WriteLine($"@search.score: {result.Score}");
-    
-                        // Print @search.rerankerScore if available
-                        if (result.SemanticSearch != null && result.SemanticSearch.RerankerScore.HasValue)
-                        {
-                            Console.WriteLine($"@search.rerankerScore: {result.SemanticSearch.RerankerScore.Value}");
-                        }
-                        Console.WriteLine(new string('-', 40));
-                    }
-                }
-                catch (Exception ex)
-                {
-                    Console.WriteLine($"Error querying index: {ex.Message}");
-                }
-            }
-        }
-    }
+1. Run the first project to update the index with a semantic configuration.
+
+    ```bash
+    dotnet run --project BuildIndex
     ```
 
-1. Replace the search service URL with a valid endpoint.
+1. Run the second project to query the index. Press **Enter** between queries to see the progression from simple query to semantic query with captions and answers.
 
-1. Run the program.
+    ```bash
+    dotnet run --project QueryIndex
+    ```
 
-1. Output is logged to a console window from [Console.WriteLine](/dotnet/api/system.console.writeline). You should see search results for each query.
+### Output
+
+The first project updates the hotels-sample index with a semantic configuration. The output includes confirmation of the semantic configuration.
+
+```output
+Here's a list of all indexes on the search service. You should see hotels-sample:
+hotels-sample
+
+Added new semantic configuration 'semantic-config' to the index definition.
+Index updated successfully.
+Here is the revised index definition:
+{
+  "Name": "hotels-sample",
+  ... // Trimmed for brevity
+  "SemanticSearch": {
+    "DefaultConfigurationName": "semantic-config",
+    "Configurations": [
+      {
+        "Name": "hotels-sample-semantic-configuration",
+        ... // Trimmed for brevity
+      },
+      {
+        "Name": "semantic-config",
+        "PrioritizedFields": {
+          "TitleField": {
+            "FieldName": "HotelName"
+          },
+          "ContentFields": [
+            {
+              "FieldName": "Description"
+            }
+          ],
+          "KeywordsFields": [
+            {
+              "FieldName": "Tags"
+            }
+          ]
+        },
+        "RankingOrder": {}
+      }
+    ]
+  }
+}
+```
 
-### Output for semantic query (no captions or answers)
+The second project runs four queries. The output includes the search results with relevance scores, captions, and answers.
 
-This output is from the semantic query, with no captions or answers. The query string is 'walking distance to live music'.
+```output
+Query 1: Simple query using the search string 'walking distance to live music'.
+HotelId: 2
+HotelName: Old Century Hotel
+Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
+@search.score: 5.004435
+----------------------------------------
+HotelId: 24
+HotelName: Uptown Chic Hotel
+Description: Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance.
+@search.score: 4.555706
+----------------------------------------
+... // Trimmed for brevity
+Press Enter to continue to the next query...
 
-Here, the initial results from the term query are rescored using the semantic ranking models. For this particular dataset and query, the first several results are in similar positions. The effects of semantic ranking are more pronounced in the remainder of the results.
 
-```bash
+Query 2: Semantic query (no captions, no answers) for 'walking distance to live music'.
 HotelId: 24
 HotelName: Uptown Chic Hotel
 Description: Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance.
-@search.score: 5.074317
+@search.score: 4.555706
 @search.rerankerScore: 2.613231658935547
 ----------------------------------------
 HotelId: 2
 HotelName: Old Century Hotel
 Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
-@search.score: 5.5153193
+@search.score: 5.004435
 @search.rerankerScore: 2.271434783935547
 ----------------------------------------
-HotelId: 4
-HotelName: Sublime Palace Hotel
-Description: Sublime Cliff Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.
-@search.score: 4.8959594
-@search.rerankerScore: 1.9861756563186646
-----------------------------------------
-HotelId: 39
-HotelName: White Mountain Lodge & Suites
-Description: Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings.
-@search.score: 0.7334347
-@search.rerankerScore: 1.9615401029586792
-----------------------------------------
-HotelId: 15
-HotelName: By the Market Hotel
-Description: Book now and Save up to 30%. Central location. Walking distance from the Empire State Building & Times Square, in the Chelsea neighborhood. Brand new rooms. Impeccable service.
-@search.score: 1.5502293
-@search.rerankerScore: 1.9085469245910645
-----------------------------------------
+... // Trimmed for brevity
 Press Enter to continue to the next query...
-```
 
-### Output for a semantic query with captions
 
-Here are the results for the query that adds captions with hit highlighting.
-
-```
+Query 3: Semantic query with captions.
 Caption: Chic hotel near the city. High-rise hotel in downtown, within walking distance to<em> theaters, </em>art galleries, restaurants and shops. Visit<em> Seattle Art Museum </em>by day, and then head over to<em> Benaroya Hall </em>to catch the evening's concert performance.
 HotelId: 24
 HotelName: Uptown Chic Hotel
 Description: Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance.
-@search.score: 5.074317
+@search.score: 4.555706
 @search.rerankerScore: 2.613231658935547
 ----------------------------------------
-Caption:
-HotelId: 2
-HotelName: Old Century Hotel
-Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
-@search.score: 5.5153193
-@search.rerankerScore: 2.271434783935547
-----------------------------------------
-Caption: Sublime Cliff Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within<em> short walking distance </em>to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort,.
-HotelId: 4
-HotelName: Sublime Palace Hotel
-Description: Sublime Cliff Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.
-@search.score: 4.8959594
-@search.rerankerScore: 1.9861756563186646
-----------------------------------------
-Caption: Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend<em> evening entertainment </em>on the patio features special<em> guest musicians </em>or.
-HotelId: 39
-HotelName: White Mountain Lodge & Suites
-Description: Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings.
-@search.score: 0.7334347
-@search.rerankerScore: 1.9615401029586792
-----------------------------------------
-Caption: Book now and Save up to 30%. Central location. <em>Walking distance from the Empire State Building & Times Square, in the Chelsea neighborhood.</em> Brand new rooms. Impeccable service.
-HotelId: 15
-HotelName: By the Market Hotel
-Description: Book now and Save up to 30%. Central location. Walking distance from the Empire State Building & Times Square, in the Chelsea neighborhood. Brand new rooms. Impeccable service.
-@search.score: 1.5502293
-@search.rerankerScore: 1.9085469245910645
-----------------------------------------
+... // Trimmed for brevity
 Press Enter to continue to the next query...
+
+
+Query 4: Semantic query with a verbatim answer from the Description field for 'what's a good hotel for people who like to read'.
+Extractive Answers:
+  Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
+----------------------------------------
+... // Trimmed for brevity
 ```
 
-### Output for semantic answers
+## Understand the code
 
-The final query returns a semantic answer. Notice that we changed the query string for this example: 'what's a good hotel for people who like to read'.
+[!INCLUDE [understand code note](../understand-code-note.md)]
 
-Semantic ranker can produce an answer to a query string that has the characteristics of a question. The generated answer is extracted verbatim from your content so it won't include composed content like what you might expect from a chat completion model. If the semantic answer isn't useful for your scenario, you can omit `semantic_answers` from your code.
+Now that you've run the code, let's break down the key steps:
 
-To produce a semantic answer, the question and answer must be closely aligned, and the model must find content that clearly answers the question. If potential answers fail to meet a confidence threshold, the model doesn't return an answer. For demonstration purposes, the question in this example is designed to get a response so that you can see the syntax.
+1. [Configuration and authentication](#configuration-and-authentication)
+1. [Update the index with a semantic configuration](#update-the-index-with-a-semantic-configuration)
+1. [Query the index](#query-the-index)
 
-Recall that answers are *verbatim content* pulled from your index and might be missing phrases that a user would expect to see. To get *composed answers* as generated by a chat completion model, considering using a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
+### Configuration and authentication
 
-```bash
-Extractive Answers:
-  Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
-----------------------------------------
-HotelId: 1
-HotelName: Stay-Kay City Hotel
-Description: This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
-@search.score: 2.0361428
-@search.rerankerScore: 2.124817371368408
-----------------------------------------
-HotelId: 16
-HotelName: Double Sanctuary Resort
-Description: 5 star Luxury Hotel - Biggest Rooms in the city. #1 Hotel in the area listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso in room.
-@search.score: 3.759768
-@search.rerankerScore: 2.0705394744873047
-----------------------------------------
-HotelId: 38
-HotelName: Lakeside B & B
-Description: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the library by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
-@search.score: 0.7308748
-@search.rerankerScore: 2.041472911834717
-----------------------------------------
-HotelId: 2
-HotelName: Old Century Hotel
-Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
-@search.score: 3.391012
-@search.rerankerScore: 2.0231292247772217
-----------------------------------------
-HotelId: 15
-HotelName: By the Market Hotel
-Description: Book now and Save up to 30%. Central location. Walking distance from the Empire State Building & Times Square, in the Chelsea neighborhood. Brand new rooms. Impeccable service.
-@search.score: 1.3198771
-@search.rerankerScore: 2.021622657775879
-----------------------------------------
+Both projects share the same configuration pattern. The `Program.cs` files define the search endpoint and use `DefaultAzureCredential` for keyless authentication.
+
+```csharp
+var endpoint = new Uri("PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE");
+var credential = new DefaultAzureCredential();
+var indexClient = new SearchIndexClient(endpoint, credential);
+```
+
+Key takeaways:
+
++ `DefaultAzureCredential` provides keyless authentication using Microsoft Entra ID. It chains multiple credential types, including the Azure CLI credential from `az login`.
++ `SearchIndexClient` manages index-level operations, such as updating the index schema.
++ `SearchClient` handles document-level operations, such as querying the index.
+
+### Update the index with a semantic configuration
+
+The following code in `BuildIndex/Program.cs` adds a semantic configuration to the existing index. This operation doesn't delete any search documents, and your index remains operational after the configuration is added.
+
+```csharp
+static void AddSemanticConfiguration(
+    SearchIndex index,
+    string semanticConfigName)
+{
+    if (index.SemanticSearch == null)
+    {
+        index.SemanticSearch = new SemanticSearch();
+    }
+    var configs = index.SemanticSearch.Configurations;
+    if (!configs.Any(c => c.Name == semanticConfigName))
+    {
+        var prioritizedFields =
+            new SemanticPrioritizedFields
+        {
+            TitleField = new SemanticField("HotelName"),
+            ContentFields =
+            {
+                new SemanticField("Description")
+            },
+            KeywordsFields =
+            {
+                new SemanticField("Tags")
+            }
+        };
+
+        configs.Add(
+            new SemanticConfiguration(
+                semanticConfigName,
+                prioritizedFields
+            )
+        );
+    }
+    index.SemanticSearch.DefaultConfigurationName =
+        semanticConfigName;
+}
 ```
+
+Key takeaways:
+
++ A semantic configuration specifies the fields used for semantic ranking.
++ Semantic configurations can be added to existing indexes without rebuilding.
++ `TitleField` sets the field that represents the document title.
++ `ContentFields` sets the fields containing the main content.
++ `KeywordsFields` sets the fields containing keywords or tags.
+
+### Query the index
+
+The `QueryIndex` project runs four queries in sequence, progressing from a simple keyword search to semantic ranking with captions and answers.
+
+#### Simple query
+
+The first query is a simple keyword search that doesn't use semantic ranking. This query serves as a baseline for comparing results with and without semantic reranking.
+
+```csharp
+await RunQuery(client, searchText, new SearchOptions
+{
+    Size = 5,
+    QueryType = SearchQueryType.Simple,
+    IncludeTotalCount = true,
+    Select = { "HotelId", "HotelName", "Description" }
+});
+```
+
+Key takeaways:
+
++ `SearchQueryType.Simple` uses the default BM25 ranking algorithm.
++ Results are ranked by keyword relevance (`@search.score`) only.
+
+#### Semantic query (no captions, no answers)
+
+The next query adds semantic ranking with no captions or answers. The following code shows the minimum requirement for invoking semantic ranking.
+
+```csharp
+var semanticOptions = new SearchOptions
+{
+    Size = 5,
+    QueryType = SearchQueryType.Semantic,
+    SemanticSearch = new SemanticSearchOptions
+    {
+        SemanticConfigurationName = "semantic-config"
+    },
+    IncludeTotalCount = true,
+    Select =
+    {
+        "HotelId", "HotelName", "Description"
+    }
+};
+await RunQuery(client, searchText, semanticOptions);
+```
+
+Key takeaways:
+
++ `SearchQueryType.Semantic` enables semantic ranking on the query.
++ `SemanticConfigurationName` specifies which semantic configuration to use.
++ `@search.rerankerScore` indicates semantic relevance (higher is better).
++ The initial results from the term query are rescored using semantic ranking models. For this dataset and query, the effects of semantic ranking are more pronounced in the lower-ranked results.
+
+#### Semantic query with captions
+
+The following code adds captions to extract the most relevant passages from each result, with hit highlighting applied to the important terms and phrases.
+
+```csharp
+var captionsOptions = new SearchOptions
+{
+    Size = 5,
+    QueryType = SearchQueryType.Semantic,
+    SemanticSearch = new SemanticSearchOptions
+    {
+        SemanticConfigurationName = "semantic-config",
+        QueryCaption =
+            new QueryCaption(QueryCaptionType.Extractive)
+        {
+            HighlightEnabled = true
+        }
+    },
+    IncludeTotalCount = true,
+    Select =
+    {
+        "HotelId", "HotelName", "Description"
+    }
+};
+captionsOptions.HighlightFields.Add("Description");
+await RunQuery(
+    client, searchText, captionsOptions, showCaptions: true
+);
+```
+
+Key takeaways:
+
++ `QueryCaption` enables extractive captions from the content fields.
++ Captions surface the most relevant passages and add `<em>` tags around important terms.
+
+#### Semantic query with answers
+
+The final query adds semantic answers. This query uses a different search string (`searchText2`) because semantic answers work best when the query is phrased as a question. The answer is a verbatim passage extracted from your index, not a composed response from a chat completion model.
+
+The query and the indexed content must be closely aligned for an answer to be returned. If no candidate meets the confidence threshold, the response doesn't include an answer. This example uses a question that's known to produce a result so that you can see the syntax. If answers aren't useful for your scenario, omit `QueryAnswer` from your code. For composed answers, consider a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
+
+```csharp
+var answersOptions = new SearchOptions
+{
+    Size = 5,
+    QueryType = SearchQueryType.Semantic,
+    SemanticSearch = new SemanticSearchOptions
+    {
+        SemanticConfigurationName = "semantic-config",
+        QueryAnswer =
+            new QueryAnswer(QueryAnswerType.Extractive)
+    },
+    IncludeTotalCount = true,
+    Select =
+    {
+        "HotelId", "HotelName", "Description"
+    }
+};
+await RunQuery(
+    client, searchText2, answersOptions, showAnswers: true
+);
+```
+
+Key takeaways:
+
++ `QueryAnswer` enables extractive answers for question-like queries.
++ Answers are verbatim content extracted from your index, not generated text.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "C#におけるセマンティックランカーのクイックスタートガイドの大幅改訂"
}
```

### Explanation
この変更は、C#におけるセマンティックランカーのクイックスタートガイドの内容が大幅に改訂されたことを示しています。具体的には、内容の整理と構成の見直しが行われ、新しい情報が追加され、古い情報が削除されました。この変更では、全体的に308行が追加され、373行が削除され、合計681行が変更されました。

主な改訂点は、セマンティックランキングに関する機能の説明が明確になり、クイックスタートガイドの流れがスムーズになったことです。たとえば、クイックスタート手順の冒頭に、Azure AI Searchクライアントライブラリを使用する重要性が強調されており、ユーザーがすぐに始められるようにソースコードへのリンクも追加されています。

また、依存関係のインストールから環境の設定、インデックスの更新、セマンティッククエリの実行に至るまで、手順が整理され、より明確な指示が提供されています。中でも、セマンティック構成の追加や、クエリの実行に必要なコードの具体例が付加され、ユーザーが実際に操作する際の理解を助ける構成になっています。全体として、精緻な情報を提供しつつ、従来の内容からの大幅な変更を遂げたガイドとなっています。

## articles/search/includes/quickstarts/semantic-ranker-index.md{#item-44a527}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,69 @@
+---
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 03/04/2026
+---
+
+This quickstart modifies an existing index to include a semantic configuration. We recommend the hotels-sample index, which you can create in minutes using an Azure portal wizard.
+
+To use a different index, replace the index name, field names in the semantic configuration, and field names in query `select` statements throughout the sample code. Your index should contain descriptive text fields that are attributed as `searchable` and `retrievable`.
+
+To review and query the hotels-sample index before semantic ranking:
+
+1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
+
+1. From the left pane, select **Search management** > **Indexes**.
+
+1. Select **hotels-sample**.
+
+1. Select **Semantic configurations** to view any existing configurations. If you enabled semantic ranking during the wizard creation flow, there should be a default configuration.
+
+   :::image type="content" source="../../media/search-get-started-semantic/default-semantic-configuration.png" alt-text="Screenshot of the default semantic configuration in the Azure portal." lightbox="../../media/search-get-started-semantic/default-semantic-configuration.png":::
+
+1. Select **Search explorer**, and then select **View** > **JSON view**.
+
+1. Paste the following JSON into the query editor.
+
+    ```json
+    {
+      "search": "walking distance to live music",
+      "select": "HotelId, HotelName, Description",
+      "count": true
+    }
+    ```
+
+1. Select **Search** to run the query.
+
+   The response should be similar to the following example. This is a full-text query ranked by BM25, so results match on individual query terms and linguistic variants rather than the overall meaning of the query. For example, `walking` matches `walk`, and `live` and `music` match independently rather than as a phrase.
+
+    ```json
+    "@odata.count": 30,
+    "value": [
+      {
+        "@search.score": 5.004435,
+        "HotelId": "2",
+        "HotelName": "Old Century Hotel",
+        "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music."
+      },
+      {
+        "@search.score": 4.555706,
+        "HotelId": "24",
+        "HotelName": "Uptown Chic Hotel",
+        "Description": "Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance."
+      },
+      {
+        "@search.score": 3.5625167,
+        "HotelId": "4",
+        "HotelName": "Sublime Palace Hotel",
+        "Description": "Sublime Cliff Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience."
+      },
+      ... // Trimmed for brevity
+    ]
+   ```
+
+    > [!TIP]
+    > This query shows how the response looks before semantic ranking is applied. After you configure a semantic configuration, add `"queryType": "semantic"` and `"semanticConfiguration": "semantic-config"` to see how the same query is ranked differently by semantic ranking.
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "セマンティック構成を含むインデックスのクイックスタートガイドの追加"
}
```

### Explanation
この変更では、セマンティックランカーに関する新しいクイックスタートガイドが追加され、既存のインデックスにセマンティック構成を含める手順が説明されています。全体で69行が追加され、削除された行はありません。

新しいガイドでは、特に「hotels-sample」インデックスを利用することが推奨されており、ユーザーが簡単にAzureポータルを使用してこのインデックスを作成できるように手順が明示されています。また、別のインデックスを使用する場合の注意事項や、構成のカスタマイズ方法が紹介されています。

ガイドには、インデックスをレビューし、セマンティックランキングを適用する前のクエリの実行例も含まれています。具体的には、Azureポータルへのサインインから、検索管理、セマンティック構成の確認、検索クエリの実行、レスポンスの確認に至るまで、詳細な手順が提供されています。最後に、セマンティックランキングを適用した後のクエリの見え方についてのヒントが記載されており、ユーザーがより深く理解できるよう配慮されています。

この追加により、ユーザーは新しいインデックスをセマンティックランカーに合わせて迅速に設定し、テストする方法を学ぶことができます。

## articles/search/includes/quickstarts/semantic-ranker-intro.md{#item-538e0f}

<details>
<summary>Diff</summary>
````diff
@@ -1,163 +0,0 @@
----
-manager: nitinme
-author: haileytap
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.topic: include
-ms.date: 11/20/2025
----
-
-In this quickstart, you learn how to use [semantic ranking](../../semantic-search-overview.md) by adding a semantic configuration to a search index and adding semantic parameters to a query. You can use the hotels-sample-index or one of your own.
-
-In Azure AI Search, semantic ranking is query-side functionality that uses machine reading comprehension from Microsoft to rescore search results, promoting the most semantically relevant matches to the top of the list. Depending on the content and the query, semantic ranking can [significantly improve search relevance](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-outperforming-vector-search-with-hybrid/ba-p/3929167) with minimal developer effort.
-
-You can add a semantic configuration to an existing index with no rebuild requirement. Semantic ranking is most effective on text that's informational or descriptive.
-
-## Prerequisites
-
-+ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-
-+ An [Azure AI Search service](../../search-create-service-portal.md) with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
-
-+ A [new or existing index](../../search-how-to-create-search-index.md) with descriptive or verbose text fields that are attributed as retrievable. This quickstart assumes the [hotels-sample-index](../../search-get-started-portal.md).
-
-## Configure access
-
-You can connect to your Azure AI Search service using API keys or Microsoft Entra ID with role assignments. Keys are easier to start with, but roles are more secure. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
-
-To configure role-based access:
-
-1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
-
-1. From the left pane, select **Settings** > **Keys**.
-
-1. Under **API Access control**, select **Role-based access control** or **Both** if you need time to transition clients to role-based access.
-
-1. From the left pane, select **Access control (IAM)**.
-
-1. Select **Add** > **Add role assignment**.
-
-1. Assign the **Search Service Contributor** and **Search Index Data Contributor** roles to your user account.
-
-## Start with an index
-
-This quickstart assumes an existing index and modifies it to include a semantic configuration. We recommend the [hotels-sample-index](../../search-get-started-portal.md) that you can create in minutes using an Azure portal wizard.
-
-To start with an existing index:
-
-1. Sign in to the [Azure portal](https://portal.azure.com/) and find your search service.
-
-1. Under **Search management** > **Indexes**, select the hotels-sample-index.
-
-1. Select **Semantic configurations** to ensure the index doesn't have a semantic configuration.
-
-   :::image type="content" source="../../media/search-get-started-semantic/no-semantic-configuration.png" alt-text="Screenshot of an empty semantic configuration page in the Azure portal.":::
-
-1. Select **Search explorer**, and then select the **JSON view**.
-
-1. Paste the following JSON into the query editor.
-
-    ```json
-    {
-      "search": "walking distance to live music",
-      "select": "HotelId, HotelName, Description",
-      "count": true
-    }
-    ```
-
-   :::image type="content" source="../../media/search-get-started-semantic/search-explorer-simple-query.png" alt-text="Screenshot of a query in Search Explorer in the portal.":::
-
-1. Select **Search** to run the query.
-
-   This query is a keyword search. The response should be similar to the following example, as scored by the default BM25 L1 ranker for full-text search.
-
-   For readability, the example only selects the `HotelId`, `HotelName`, and `Description` fields. The results contain verbatim matches on the query terms (`walking`, `distance`, `live`, `music`) or linguistic variants (`walk`, `living`).
-
-    ```json
-    "@odata.count": 13,
-    "value": [
-      {
-        "@search.score": 5.5153193,
-        "HotelId": "2",
-        "HotelName": "Old Century Hotel",
-        "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music."
-      },
-      {
-        "@search.score": 5.074317,
-        "HotelId": "24",
-        "HotelName": "Uptown Chic Hotel",
-        "Description": "Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance."
-      },
-      {
-        "@search.score": 4.8959594,
-        "HotelId": "4",
-        "HotelName": "Sublime Palace Hotel",
-        "Description": "Sublime Cliff Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience."
-      },
-      {
-        "@search.score": 2.5966604,
-        "HotelId": "35",
-        "HotelName": "Bellevue Suites",
-        "Description": "Comfortable city living in the very center of downtown Bellevue. Newly reimagined, this hotel features apartment-style suites with sleeping, living and work spaces. Located across the street from the Light Rail to downtown. Free shuttle to the airport."
-      },
-      {
-        "@search.score": 2.566386,
-        "HotelId": "47",
-        "HotelName": "Country Comfort Inn",
-        "Description": "Situated conveniently at the north end of the village, the inn is just a short walk from the lake, offering reasonable rates and all the comforts home inlcuding living room suites and functional kitchens. Pets are welcome."
-      },
-      {
-        "@search.score": 2.2405157,
-        "HotelId": "9",
-        "HotelName": "Smile Up Hotel",
-        "Description": "Experience the fresh, modern downtown. Enjoy updated rooms, bold style & prime location. Don't miss our weekend live music series featuring who's new/next on the scene."
-      },
-      {
-        "@search.score": 2.1737604,
-        "HotelId": "8",
-        "HotelName": "Foot Happy Suites",
-        "Description": "Downtown in the heart of the business district. Close to everything. Leave your car behind and walk to the park, shopping, and restaurants. Or grab one of our bikes and take your explorations a little further."
-      },
-      {
-        "@search.score": 2.0364518,
-        "HotelId": "31",
-        "HotelName": "Country Residence Hotel",
-        "Description": "All of the suites feature full-sized kitchens stocked with cookware, separate living and sleeping areas and sofa beds. Some of the larger rooms have fireplaces and patios or balconies. Experience real country hospitality in the heart of bustling Nashville. The most vibrant music scene in the world is just outside your front door."
-      },
-      {
-        "@search.score": 1.7595702,
-        "HotelId": "49",
-        "HotelName": "Swirling Currents Hotel",
-        "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary W-Fi and flat-screen TVs. "
-      },
-      {
-        "@search.score": 1.5502293,
-        "HotelId": "15",
-        "HotelName": "By the Market Hotel",
-        "Description": "Book now and Save up to 30%. Central location. Walking distance from the Empire State Building & Times Square, in the Chelsea neighborhood. Brand new rooms. Impeccable service."
-      },
-      {
-        "@search.score": 1.3302404,
-        "HotelId": "42",
-        "HotelName": "Rock Bottom Resort & Campground",
-        "Description": "Rock Bottom is nestled on 20 unspoiled acres on a private cove of Rock Bottom Lake. We feature both lodging and campground accommodations to suit just about every taste. Even though we are out of the traffic of the city, getting there is only a short drive away."
-      },
-      {
-        "@search.score": 0.9050383,
-        "HotelId": "38",
-        "HotelName": "Lakeside B & B",
-        "Description": "Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the library by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply."
-      },
-      {
-        "@search.score": 0.7334347,
-        "HotelId": "39",
-        "HotelName": "White Mountain Lodge & Suites",
-        "Description": "Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings."
-      }
-    ]
-   ```
-
-This query shows how the response looks *before* semantic ranking is applied. Later, you can run the same query after semantic ranking is configured to see how the response changes.
-
-> [!TIP]
-> You can add a semantic configuration in the Azure portal. However, if you want to learn how to add a semantic configuration programmatically, continue with this quickstart.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "セマンティックランカーのイントロダクションガイドの削除"
}
```

### Explanation
この変更では、セマンティックランカーのイントロダクションに関するガイドが完全に削除されました。削除されたコンテンツは163行にわたり、これにより、ユーザーがセマンティックランキングの使用方法やその機能についての基本的な情報を学ぶためのリソースが失われました。

削除されたガイドでは、セマンティック構成の追加やクエリにセマンティックパラメーターを加える方法が説明されており、Azure AI Searchにおけるセマンティックランキングの重要性や利点を強調していました。また、クイックスタートの手順として、Azureポータルでの設定や、サンプルインデックスを使用したクエリ実行の具体的な指示が提供されていました。

今後、ユーザーはこの情報にアクセスできないため、セマンティックランカーを効果的に利用するための導入としての資源を探しづらくなるか、他の文書を参照する必要があります。この変更は、セマンティックランカーを初めて使用するユーザーにとっての障壁を高める可能性がある、重要な影響を持つものです。

## articles/search/includes/quickstarts/semantic-ranker-java.md{#item-93a05a}

<details>
<summary>Diff</summary>
````diff
@@ -1,163 +1,499 @@
 ---
 author: KarlErickson
-ms.author: karler
+ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom: devx-track-java
 ms.topic: include
-ms.date: 12/15/2025
+ms.date: 03/04/2026
 ai-usage: ai-assisted
 ---
 
-[!INCLUDE [Semantic ranker introduction](semantic-ranker-intro.md)]
+In this quickstart, you use the [Azure AI Search client library for Java](/java/api/overview/azure/search-documents-readme) to add [semantic ranking](../../semantic-search-overview.md) to an existing search index and query the index.
 
-## Set up the client
+Semantic ranking is query-side functionality that uses machine reading comprehension to rescore search results, promoting the most semantically relevant matches to the top of the list. You can add a semantic configuration to an existing index with no rebuild requirement. Semantic ranking is most effective for informational or descriptive text.
 
-In this quickstart, you use an IDE and the [**Azure AI Search Java SDK**](https://search.maven.org/artifact/com.azure/azure-search-documents) client library to add semantic ranking to an existing search index.
+> [!TIP]
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart-semantic-ranking) on GitHub.
 
-The quickstart assumes the following is available on your computer:
-- [Visual Studio Code](https://code.visualstudio.com/) with Java extensions or IntelliJ IDEA
-- [Java 21 (LTS)](/java/openjdk/install).
-- [Maven](https://maven.apache.org/download.cgi).
+## Prerequisites
 
-### Set up local development environment
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-1. Create a new Maven project directory.
++ An [Azure AI Search service](../../search-create-service-portal.md) with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
 
-   ```bash
-   mkdir semantic-ranking-quickstart && cd semantic-ranking-quickstart
-   code .
-   ```
++ An [index](../../search-how-to-create-search-index.md) with descriptive text fields attributed as `searchable` and `retrievable`.  This quickstart assumes the [hotels-sample index](../../search-get-started-portal.md).
 
-1. Create a `pom.xml` file with required dependencies.
++ [Java 21 (LTS)](/java/openjdk/install) and [Maven](https://maven.apache.org/download.cgi).
 
-   :::code language="xml" source="~/azure-search-java-samples/quickstart-semantic-ranking/pom.xml" :::
++ [Visual Studio Code](https://code.visualstudio.com/download).
 
-1. Compile the project to resolve the dependencies.
++ [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-    ```bash
-    mvn compile
-    ```
-
-1. Create the source directory structure.
-
-   ```bash
-   mkdir -p src/main/java/com/azure/search/quickstart
-   mkdir -p src/main/resources
-   ```
-
-1. Create an `application.properties` file in the `src/main/resources` directory and provide your search service endpoint. You can get the endpoint from the Azure portal on the search service **Overview** page.
-
-    ```properties
-    azure.search.endpoint=YOUR-SEARCH-SERVICE-ENDPOINT
-    azure.search.index.name=hotels-sample-index
-    semantic.configuration.name=semantic-config
-    ```
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-### Sign in to Azure
+## Configure access
 
-If you signed in to the [Azure portal](https://portal.azure.com), you're signed into Azure. If you aren't sure, use the Azure CLI to log in: `az login`. If you have multiple tenants and subscriptions, see [Quickstart: Connect without keys](../../search-get-started-rbac.md) for help on how to connect.
+[!INCLUDE [resource authentication](../resource-authentication-semantic.md)]
 
-## Create a common configuration class
+## Get endpoint
 
-Create a `SearchConfig.java` file in the `src/main/java/com/azure/search/quickstart` directory to read the properties file and hold the configuration values and authentication credential.
+[!INCLUDE [resource endpoint](../resource-endpoint.md)]
 
-:::code language="java" source="~/azure-search-java-samples/quickstart-semantic-ranking/src/main/java/com/azure/search/quickstart/SearchConfig.java" :::
+## Start with an index
 
-## Get the index schema
+[!INCLUDE [start with an index](semantic-ranker-index.md)]
 
-In this section, you get settings for the existing `hotels-sample-index` index on your search service.
+## Set up the environment
 
-1. Create a `GetIndexSettings.java` file in the `src/main/java/com/azure/search/quickstart` directory.
-
-   :::code language="java" source="~/azure-search-java-samples/quickstart-semantic-ranking/src/main/java/com/azure/search/quickstart/GetIndexSettings.java" :::
-
-1. Compile and run the code.
+1. Use Git to clone the sample repository.
 
     ```bash
-    mvn compile exec:java -Dexec.mainClass="com.azure.search.quickstart.GetIndexSettings"
+    git clone https://github.com/Azure-Samples/azure-search-java-samples
     ```
 
-1. Output is the name of the index, list of fields, and a statement indicating whether a semantic configuration exists. For the purposes of this quickstart, the message should say `No semantic configuration exists for this index`.
-
-## Update the index with a semantic configuration
-
-1. Create an `UpdateIndexSettings.java` file in the `src/main/java/com/azure/search/quickstart` directory to add a semantic configuration to the existing `hotels-sample-index` index on your search service.
-
-   :::code language="java" source="~/azure-search-java-samples/quickstart-semantic-ranking/src/main/java/com/azure/search/quickstart/UpdateIndexSettings.java" :::
-
-1. Compile and run the code.
+1. Navigate to the quickstart folder and open it in Visual Studio Code.
 
     ```bash
-    mvn compile exec:java -Dexec.mainClass="com.azure.search.quickstart.UpdateIndexSettings"
+    cd azure-search-java-samples/quickstart-semantic-ranking
+    code .
     ```
 
-1. Output is the semantic configuration you just added, `Semantic configuration updated successfully.`.
-
-## Run semantic queries
-
-After the `hotels-sample-index` index has a semantic configuration, you can run queries that include semantic parameters.
+1. In `src/main/resources/application.properties`, replace the placeholder value for `azure.search.endpoint` with the URL you obtained in [Get endpoint](#get-endpoint).
 
-1. Create a `SemanticQuery.java` file in the `src/main/java/com/azure/search/quickstart` directory to create a semantic query of the index.
-
-   :::code language="java" source="~/azure-search-java-samples/quickstart-semantic-ranking/src/main/java/com/azure/search/quickstart/SemanticQuery.java" :::
-
-1. Compile and run the code.
+1. Compile the project to resolve dependencies, including [azure-search-documents](https://search.maven.org/artifact/com.azure/azure-search-documents).
 
     ```bash
-    mvn compile exec:java -Dexec.mainClass="com.azure.search.quickstart.SemanticQuery"
+    mvn compile
     ```
 
-1. Output should consist of 13 documents, ordered by the reranker score.
-
-### Return captions
+    When the build completes, verify that no errors appear in the output.
 
-Optionally, you can add captions to extract portions of the text and apply hit highlighting to the important terms and phrases.
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
-1. Create a `SemanticQueryWithCaptions.java` file in the `src/main/java/com/azure/search/quickstart` directory.
+    ```azurecli
+    az login
+    ```
 
-   :::code language="java" source="~/azure-search-java-samples/quickstart-semantic-ranking/src/main/java/com/azure/search/quickstart/SemanticQueryWithCaptions.java" :::
+## Run the code
 
-1. Compile and run the code.
+1. Get the existing index settings.
 
     ```bash
-    mvn compile exec:java -Dexec.mainClass="com.azure.search.quickstart.SemanticQueryWithCaptions"
+    mvn compile exec:java "-Dexec.mainClass=com.azure.search.quickstart.GetIndexSettings"
     ```
 
-1. Output should include a new caption element alongside search field. Captions are the most relevant passages in a result. If your index includes larger chunks of text, a caption is helpful for extracting the most interesting sentences.
-
-    ```output
-    Search result #1:
-      Re-ranker Score: 2.613231658935547
-      HotelName: Uptown Chic Hotel
-      Description: Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance.
+1. Update the index with a semantic configuration.
 
-      Caption with highlights: Chic hotel near the city. High-rise hotel in downtown, within walking distance to<em> theaters, </em>art galleries, restaurants and shops. Visit<em> Seattle Art Museum </em>by day, and then head over to<em> Benaroya Hall </em>to catch the evening's concert performance.
+    ```bash
+    mvn compile exec:java "-Dexec.mainClass=com.azure.search.quickstart.UpdateIndexSettings"
     ```
 
-### Return semantic answers
-
-In this final query, return semantic answers.
+1. Run a semantic query.
 
-Semantic ranker can produce an answer to a query string that has the characteristics of a question. The generated answer is extracted verbatim from your content so it won't include composed content like what you might expect from a chat completion model.
-
-To produce a semantic answer, the question and answer must be closely aligned, and the model must find content that clearly answers the question. If potential answers fail to meet a confidence threshold, the model doesn't return an answer. For demonstration purposes, the question in this example is designed to get a response so that you can see the syntax.
-
-1. Create a `SemanticAnswer.java` file in the `src/main/java/com/azure/search/quickstart` directory.
-
-   :::code language="java" source="~/azure-search-java-samples/quickstart-semantic-ranking/src/main/java/com/azure/search/quickstart/SemanticAnswer.java" :::
+    ```bash
+    mvn compile exec:java "-Dexec.mainClass=com.azure.search.quickstart.SemanticQuery"
+    ```
 
-1. Compile and run the code.
+1. Run a semantic query with captions.
 
     ```bash
-    mvn compile exec:java -Dexec.mainClass="com.azure.search.quickstart.SemanticAnswer"
+    mvn compile exec:java "-Dexec.mainClass=com.azure.search.quickstart.SemanticQueryWithCaptions"
     ```
 
-1. Output should look similar to the following example, where the best answer to question is pulled from one of the results.
-
-    Recall that answers are *verbatim content* pulled from your index and might be missing phrases that a user would expect to see. To get *composed answers* as generated by a chat completion model, considering using a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
+1. Run a semantic query with answers.
 
-    ```output
-    Semantic answer result #1:
-    Semantic Answer: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
-    Semantic Answer Score: 0.9829999804496765
+    ```bash
+    mvn compile exec:java "-Dexec.mainClass=com.azure.search.quickstart.SemanticAnswer"
     ```
+
+### Output
+
+The output of `GetIndexSettings.java` is the name of the index, its fields, and its semantic configurations. Before you add a new configuration, the index has only the default one.
+
+```output
+Index name: hotels-sample
+Number of fields: 23
+Field: HotelId, Type: Edm.String, Searchable: true
+Field: HotelName, Type: Edm.String, Searchable: true
+Field: Description, Type: Edm.String, Searchable: true
+// Trimmed for brevity
+Semantic search configurations: 1
+Configuration name: hotels-sample-semantic-configuration
+```
+
+The output of `UpdateIndexSettings.java` lists all semantic configurations on the index, including the one the code added, followed by a success message.
+
+```output
+// Trimmed for brevity
+Configuration name: semantic-config
+Title field: HotelName
+Keywords fields: Tags
+Content fields: Description
+----------------------------------------
+Semantic configuration updated successfully.
+```
+
+The output of `SemanticQuery.java` returns all matching documents ordered by the semantic ranking re-ranker score.
+
+```output
+Search result #1:
+  Re-ranker Score: 2.61
+  HotelId: 24
+  HotelName: Uptown Chic Hotel
+  Description: Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance.
+
+Search result #2:
+  Re-ranker Score: 2.27
+  HotelId: 2
+  HotelName: Old Century Hotel
+  Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
+
+Search result #3:
+  Re-ranker Score: 1.99
+  HotelId: 4
+  HotelName: Sublime Palace Hotel
+  Description: Sublime Cliff Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.
+// Trimmed for brevity
+```
+
+The output of `SemanticQueryWithCaptions.java` adds a caption element with hit highlighting alongside search fields. Captions are the most relevant passages in a result. If your index includes larger text, captions help extract the most interesting sentences.
+
+```output
+Search result #1:
+  Re-ranker Score: 2.61
+  HotelName: Uptown Chic Hotel
+  Description: Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance.
+
+  Caption with highlights: Chic hotel near the city. High-rise hotel in downtown, within walking distance to<em> theaters, </em>art galleries, restaurants and shops. Visit<em> Seattle Art Museum </em>by day, and then head over to<em> Benaroya Hall </em>to catch the evening's concert performance.
+------------------------------------------------------------
+Search result #2:
+  Re-ranker Score: 2.27
+  HotelName: Old Century Hotel
+  Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
+
+  Caption text: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live.
+------------------------------------------------------------
+// Trimmed for brevity
+```
+
+The output of `SemanticAnswer.java` includes a semantic answer pulled from one of the results that best matches the question, followed by search results with captions.
+
+```output
+Semantic answer result #1:
+Semantic Answer: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
+Semantic Answer Score: 0.98
+
+Search Results:
+
+Search result #1:
+Re-ranker Score: 2.12
+Hotel: Stay-Kay City Hotel
+Description: This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
+Caption: This classic hotel is<em> fully-refurbished </em>and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
+
+Search result #2:
+Re-ranker Score: 2.07
+Hotel: Double Sanctuary Resort
+Description: 5 star Luxury Hotel - Biggest Rooms in the city. #1 Hotel in the area listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso in room.
+Caption: <em>5 star Luxury Hotel </em>-<em> Biggest </em>Rooms in the city. #1 Hotel in the area listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso in room.
+// Trimmed for brevity
+```
+
+## Understand the code
+
+[!INCLUDE [understand code note](../understand-code-note.md)]
+
+Now that you've run the code, let's break down the key steps:
+
+1. [Configuration and authentication](#configuration-and-authentication)
+1. [Update the index with a semantic configuration](#update-the-index-with-a-semantic-configuration)
+1. [Query the index](#query-the-index)
+
+### Configuration and authentication
+
+The `SearchConfig.java` class loads properties from `application.properties` and creates a `DefaultAzureCredential` for keyless authentication.
+
+```java
+import com.azure.identity.DefaultAzureCredential;
+import com.azure.identity.DefaultAzureCredentialBuilder;
+
+import java.io.IOException;
+import java.io.InputStream;
+import java.util.Properties;
+
+public class SearchConfig {
+    private static final Properties properties =
+        new Properties();
+
+    static {
+        try (InputStream input = SearchConfig.class
+            .getClassLoader()
+            .getResourceAsStream(
+                "application.properties")) {
+            properties.load(input);
+        } catch (IOException e) {
+            throw new RuntimeException(
+                "Failed to load application.properties",
+                e);
+        }
+    }
+
+    public static final String SEARCH_ENDPOINT =
+        properties.getProperty(
+            "azure.search.endpoint");
+    public static final String INDEX_NAME =
+        properties.getProperty(
+            "azure.search.index.name");
+    public static final String SEMANTIC_CONFIG_NAME =
+        properties.getProperty(
+            "semantic.configuration.name");
+
+    public static final DefaultAzureCredential
+        CREDENTIAL = new DefaultAzureCredentialBuilder()
+            .build();
+}
+```
+
+Key takeaways:
+
++ `DefaultAzureCredential` provides keyless authentication using Microsoft Entra ID. It chains multiple credential types, including the Azure CLI credential from `az login`.
++ Properties are loaded from the `application.properties` file in the classpath.
++ Static fields (`SEARCH_ENDPOINT`, `INDEX_NAME`, `SEMANTIC_CONFIG_NAME`, `CREDENTIAL`) are shared across all classes in the project.
+
+### Update the index with a semantic configuration
+
+The `UpdateIndexSettings.java` class adds a semantic configuration to the existing `hotels-sample` index. This operation doesn't delete any search documents, and your index remains operational after the configuration is added.
+
+```java
+import com.azure.search.documents.indexes
+    .SearchIndexClientBuilder;
+import com.azure.search.documents.indexes.models
+    .SearchIndex;
+import com.azure.search.documents.indexes.models
+    .SemanticConfiguration;
+import com.azure.search.documents.indexes.models
+    .SemanticField;
+import com.azure.search.documents.indexes.models
+    .SemanticPrioritizedFields;
+import com.azure.search.documents.indexes.models
+    .SemanticSearch;
+
+import java.util.ArrayList;
+import java.util.List;
+
+var indexClient = new SearchIndexClientBuilder()
+    .endpoint(SearchConfig.SEARCH_ENDPOINT)
+    .credential(SearchConfig.CREDENTIAL)
+    .buildClient();
+
+SearchIndex existingIndex =
+    indexClient.getIndex(SearchConfig.INDEX_NAME);
+
+var prioritizedFields =
+    new SemanticPrioritizedFields()
+        .setTitleField(
+            new SemanticField("HotelName"))
+        .setKeywordsFields(
+            List.of(new SemanticField("Tags")))
+        .setContentFields(
+            List.of(
+                new SemanticField("Description")));
+
+var newSemanticConfiguration =
+    new SemanticConfiguration(
+        SearchConfig.SEMANTIC_CONFIG_NAME,
+        prioritizedFields);
+
+SemanticSearch semanticSearch =
+    existingIndex.getSemanticSearch();
+if (semanticSearch == null) {
+    semanticSearch = new SemanticSearch();
+    existingIndex.setSemanticSearch(semanticSearch);
+}
+
+List<SemanticConfiguration> configurations =
+    semanticSearch.getConfigurations();
+if (configurations == null) {
+    configurations = new ArrayList<>();
+    semanticSearch.setConfigurations(configurations);
+}
+
+configurations.add(newSemanticConfiguration);
+
+indexClient.createOrUpdateIndex(existingIndex);
+```
+
+Key takeaways:
+
++ `SemanticPrioritizedFields` defines which fields the semantic ranker evaluates. `setTitleField` sets the document title, `setContentFields` sets the main content, and `setKeywordsFields` sets the keyword or tag fields.
++ `SemanticConfiguration` pairs a name with the prioritized fields, identifying which semantic configuration to use at query time.
++ `createOrUpdateIndex` pushes the updated schema to the search service without rebuilding the index or deleting documents.
+
+### Query the index
+
+The following three classes query the index in sequence, progressing from a basic semantic search to semantic ranking with captions and answers.
+
+#### Semantic query (no captions, no answers)
+
+The first query adds semantic ranking with no captions or answers. The `SemanticQuery.java` class shows the minimum requirement for invoking semantic ranking.
+
+```java
+import com.azure.search.documents
+    .SearchClientBuilder;
+import com.azure.search.documents.SearchDocument;
+import com.azure.search.documents.models.QueryType;
+import com.azure.search.documents.models.SearchOptions;
+import com.azure.search.documents.models.SearchResult;
+import com.azure.search.documents.models
+    .SemanticSearchOptions;
+import com.azure.search.documents.util
+    .SearchPagedIterable;
+
+var searchClient = new SearchClientBuilder()
+    .endpoint(SearchConfig.SEARCH_ENDPOINT)
+    .indexName(SearchConfig.INDEX_NAME)
+    .credential(SearchConfig.CREDENTIAL)
+    .buildClient();
+
+var searchOptions = new SearchOptions()
+    .setQueryType(QueryType.SEMANTIC)
+    .setSemanticSearchOptions(
+        new SemanticSearchOptions()
+            .setSemanticConfigurationName(
+                SearchConfig.SEMANTIC_CONFIG_NAME))
+    .setSelect("HotelId", "HotelName", "Description");
+
+SearchPagedIterable results = searchClient.search(
+    "walking distance to live music",
+    searchOptions, null);
+
+for (SearchResult result : results) {
+    var document = result.getDocument(
+        SearchDocument.class);
+    double rerankerScore = result
+        .getSemanticSearch().getRerankerScore();
+
+    System.out.printf("Re-ranker Score: %.2f%n",
+        rerankerScore);
+    System.out.printf("HotelName: %s%n",
+        document.get("HotelName"));
+    System.out.printf("Description: %s%n%n",
+        document.get("Description"));
+}
+```
+
+Key takeaways:
+
++ `QueryType.SEMANTIC` enables semantic ranking on the query.
++ `setSemanticConfigurationName` specifies which semantic configuration to use.
++ `SearchPagedIterable` provides an iterable over the reranked results. Each `SearchResult` contains a `getSemanticSearch()` accessor for the reranker score.
+
+#### Semantic query with captions
+
+The `SemanticQueryWithCaptions.java` class adds captions to extract the most relevant passages from each result, with hit highlighting applied to the important terms and phrases.
+
+```java
+import com.azure.search.documents.models
+    .QueryCaption;
+import com.azure.search.documents.models
+    .QueryCaptionResult;
+import com.azure.search.documents.models
+    .QueryCaptionType;
+
+var searchOptions = new SearchOptions()
+    .setQueryType(QueryType.SEMANTIC)
+    .setSemanticSearchOptions(
+        new SemanticSearchOptions()
+            .setSemanticConfigurationName(
+                SearchConfig.SEMANTIC_CONFIG_NAME)
+            .setQueryCaption(
+                new QueryCaption(
+                    QueryCaptionType.EXTRACTIVE)
+                    .setHighlightEnabled(true)))
+    .setSelect(
+        "HotelId", "HotelName", "Description");
+
+SearchPagedIterable results = searchClient.search(
+    "walking distance to live music",
+    searchOptions, null);
+
+for (SearchResult result : results) {
+    List<QueryCaptionResult> captions =
+        result.getSemanticSearch()
+            .getQueryCaptions();
+    if (captions != null && !captions.isEmpty()) {
+        QueryCaptionResult caption = captions.get(0);
+        if (caption.getHighlights() != null) {
+            System.out.printf(
+                "Caption: %s%n",
+                caption.getHighlights());
+        }
+    }
+}
+```
+
+Key takeaways:
+
++ `QueryCaption(QueryCaptionType.EXTRACTIVE)` enables extractive captions from the content fields.
++ `setHighlightEnabled(true)` adds `<em>` tags around important terms in captions.
++ Each `SearchResult` provides `getQueryCaptions()` on the semantic search accessor.
+
+#### Semantic query with answers
+
+The `SemanticAnswer.java` class adds semantic answers. This class uses a question as the search text because semantic answers work best when the query is phrased as a question. The answer is a verbatim passage extracted from your index, not a composed response from a chat completion model.
+
+The query and the indexed content must be closely aligned for an answer to be returned. If no candidate meets the confidence threshold, the response doesn't include an answer. This example uses a question that's known to produce a result so that you can see the syntax. If answers aren't useful for your scenario, omit `setQueryAnswer` from your code. For composed answers, consider a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
+
+```java
+import com.azure.search.documents.models
+    .QueryAnswer;
+import com.azure.search.documents.models
+    .QueryAnswerResult;
+import com.azure.search.documents.models
+    .QueryAnswerType;
+
+var searchOptions = new SearchOptions()
+    .setQueryType(QueryType.SEMANTIC)
+    .setSemanticSearchOptions(
+        new SemanticSearchOptions()
+            .setSemanticConfigurationName(
+                SearchConfig.SEMANTIC_CONFIG_NAME)
+            .setQueryCaption(
+                new QueryCaption(
+                    QueryCaptionType.EXTRACTIVE))
+            .setQueryAnswer(
+                new QueryAnswer(
+                    QueryAnswerType.EXTRACTIVE)))
+    .setSelect(
+        "HotelName", "Description", "Category");
+
+SearchPagedIterable results = searchClient.search(
+    "What's a good hotel for people who like to read",
+    searchOptions, null);
+
+List<QueryAnswerResult> semanticAnswers =
+    results.getSemanticResults().getQueryAnswers();
+
+for (QueryAnswerResult answer :
+    semanticAnswers != null ? semanticAnswers
+        : List.<QueryAnswerResult>of()) {
+    if (answer.getHighlights() != null) {
+        System.out.printf(
+            "Semantic Answer: %s%n",
+            answer.getHighlights());
+    } else {
+        System.out.printf(
+            "Semantic Answer: %s%n",
+            answer.getText());
+    }
+    System.out.printf(
+        "Semantic Answer Score: %.2f%n",
+        answer.getScore());
+}
+```
+
+Key takeaways:
+
++ `QueryAnswer(QueryAnswerType.EXTRACTIVE)` enables extractive answers for question-like queries.
++ Answers are verbatim content extracted from your index, not generated text.
++ `results.getSemanticResults().getQueryAnswers()` retrieves the answer objects separately from the search results.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java用セマンティックランカーのクイックスタートガイドの更新"
}
```

### Explanation
この変更では、Java向けのセマンティックランカーに関するクイックスタートガイドが大幅に更新され、全体で546行が変更されました。その結果、441行が追加され、105行が削除されました。主な目的は、セマンティックランキング機能の利用方法についての情報をより具体的で実用的にすることです。

変更の中で、ガイドはJava SDKを使用してセマンティックランキングを既存の検索インデックスに追加し、クエリを実行する手順が詳しく説明されています。また、Azure AI Searchサービスへの接続や、必要なツールのセットアップが強調されています。特に、コードサンプルや実行手順が明示されており、ユーザーがセマンティック検索を容易に実装できるようにしています。

新たに追加された情報として、ソースコードへの直接的なリンクやヒントが含まれることで、ユーザーはすぐに実装に取り掛かることができるようになりました。また、Azure CLIによる認証や、環境設定の詳細が提供され、より包括的な導入ガイドとなっています。

このアップデートにより、ユーザーはセマンティックランキングの効果的な利用法をより深く理解し、迅速に構成を行うことができるようになります。また、クエリの実行結果やキャプション、セマンティックアンサーについての情報も豊富に追加され、実践的なコンテキストが提供されています。

## articles/search/includes/quickstarts/semantic-ranker-javascript.md{#item-2e091c}

<details>
<summary>Diff</summary>
````diff
@@ -4,423 +4,429 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
+  - dev-focus
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 03/04/2026
+ai-usage: ai-assisted
 ---
 
-[!INCLUDE [Semantic ranker introduction](semantic-ranker-intro.md)]
+In this quickstart, you use the [Azure AI Search client library for JavaScript](/javascript/api/overview/azure/search-documents-readme) to add [semantic ranking](../../semantic-search-overview.md) to an existing search index and query the index.
 
-## Set up the client
+Semantic ranking is query-side functionality that uses machine reading comprehension to rescore search results, promoting the most semantically relevant matches to the top of the list. You can add a semantic configuration to an existing index with no rebuild requirement. Semantic ranking is most effective for informational or descriptive text.
 
-In this quickstart, you use an IDE and the [**@azure/search-documents**](https://www.npmjs.com/package/@azure/search-documents) client library to add semantic ranking to an existing search index.
+> [!TIP]
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-js) on GitHub.
 
-The quickstart assumes the following is available on your computer:
-- [Visual Studio Code](https://code.visualstudio.com/) for this quickstart.
-- [Node.js](https://nodejs.org/) (LTS) for running the sample.
+## Prerequisites
 
-> [!TIP]
-> You can download the [source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-js) to start with a finished project or follow these steps to create your own.
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
+
++ An [Azure AI Search service](../../search-create-service-portal.md) with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
+
++ An [index](../../search-how-to-create-search-index.md) with descriptive text fields attributed as `searchable` and `retrievable`.  This quickstart assumes the [hotels-sample index](../../search-get-started-portal.md).
+
++ [Node.js 20 LTS](https://nodejs.org/en/download/) or later.
+
++ [Visual Studio Code](https://code.visualstudio.com/download).
+
++ [Git](https://git-scm.com/downloads) to clone the sample repository.
+
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-### Set up local development environment
+## Configure access
 
-1. Start Visual Studio Code in a new directory.
+[!INCLUDE [resource authentication](../resource-authentication-semantic.md)]
 
-   ```bash
-   mkdir semantic-ranking-quickstart && cd semantic-ranking-quickstart
-   code .
-   ```
+## Get endpoint
 
-1. Create a new package for ESM modules in your project directory.
+[!INCLUDE [resource endpoint](../resource-endpoint.md)]
 
-   ```bash
-   npm init -y
-   npm pkg set type=module
-   ```
+## Start with an index
 
-1. Install packages, including [azure-search-documents](/javascript/api/%40azure/search-documents).
+[!INCLUDE [start with an index](semantic-ranker-index.md)]
+
+## Set up the environment
+
+1. Use Git to clone the sample repository.
 
     ```bash
-   npm install @azure/identity @azure/search-documents dotenv
+    git clone https://github.com/Azure-Samples/azure-search-javascript-samples
     ```
 
-1. Create `.env`, and provide your search service endpoint. You can get the endpoint from the Azure portal on the search service **Overview** page.
+1. Navigate to the quickstart folder and open it in Visual Studio Code.
 
-    ```ini
-    AZURE_SEARCH_ENDPOINT=YOUR-SEARCH-SERVICE-ENDPOINT
-    AZURE_SEARCH_INDEX_NAME=hotels-sample-index
-    SEMANTIC_CONFIGURATION_NAME=semantic-config
+    ```bash
+    cd azure-search-javascript-samples/quickstart-semantic-ranking-js
+    code .
     ```
 
-1. Create a `src` directory in your project directory.
+1. In `sample.env`, replace the placeholder value for `AZURE_SEARCH_ENDPOINT` with the URL you obtained in [Get endpoint](#get-endpoint).
 
-   ```bash
-   mkdir src
-   ```
+1. Rename `sample.env` to `.env`.
 
-### Sign in to Azure
+    ```bash
+    mv sample.env .env
+    ```
 
-If you signed in to the [Azure portal](https://portal.azure.com), you're signed into Azure. If you aren't sure, use the Azure CLI or Azure PowerShell to log in: `az login` or `az connect`. If you have multiple tenants and subscriptions, see [Quickstart: Connect without keys](../../search-get-started-rbac.md) for help on how to connect.
+1. Install the dependencies.
 
-## Create a common authentication file
+    ```bash
+    npm install
+    ```
 
-Create a file in `./src` called `config.ts` to read the `.env` file and hold the environment variables and authentication credential. Copy in the following code; don't change it. This file will be used by all the other files in this quickstart.
+    When the installation completes, you should see a `node_modules` folder in the project directory.
 
-```javascript
-import { DefaultAzureCredential } from "@azure/identity";
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
-// Configuration - use environment variables
-export const searchEndpoint = process.env.AZURE_SEARCH_ENDPOINT || "PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE";
-export const indexName = process.env.AZURE_SEARCH_INDEX_NAME || "hotels-sample-index";
-export const semanticConfigurationName = process.env.SEMANTIC_CONFIGURATION_NAME || "semantic-config";
+    ```azurecli
+    az login
+    ```
 
-// Create credential
-export const credential = new DefaultAzureCredential();
+## Run the code
 
-console.log(`Using Azure Search endpoint: ${searchEndpoint}`);
-console.log(`Using index name: ${indexName}\n\n`);
-```
+1. Get the existing index settings.
 
-## Get the index schema
-
-In this section, you get settings for the existing `hotels-sample-index` index on your search service.
-
-1. Create a file in `./src` called `getIndexSettings.js` and copy in the following code.
-
-    ```javascript
-    import {
-        SearchIndexClient
-    } from "@azure/search-documents";
-    import { searchEndpoint, indexName, credential } from "./config.js";
-    
-    const indexClient = new SearchIndexClient(searchEndpoint, credential);
-    
-    console.log('Getting semantic search index settings...');
-    
-    // Get the existing schema
-    const index = await indexClient.getIndex(indexName);
-    
-    console.log(`Index name: ${index.name}`);
-    console.log(`Number of fields: ${index.fields.length}`);
-    
-    for(const field of index.fields) {
-        console.log(`Field: ${field.name}, Type: ${field.type}, Searchable: ${field.searchable}`);
-    }
-    
-    if(index.semanticSearch && index.semanticSearch.configurations) {
-        console.log(`Semantic search configurations: ${index.semanticSearch.configurations.length}`);
-        for(const config of index.semanticSearch.configurations) {
-            console.log(`Configuration name: ${config.name}`);
-            console.log(`Title field: ${config.prioritizedFields.titleField?.name}`);
-        }
-    } else {
-        console.log("No semantic configuration exists for this index.");
-    }
+    ```bash
+    node -r dotenv/config src/getIndexSettings.js
     ```
 
-1. Run the code.
+1. Update the index with a semantic configuration.
 
     ```bash
-    node -r dotenv/config src/getIndexSettings.js
+    node -r dotenv/config src/updateIndexSettings.js
     ```
 
-1. Output is the name of the index, list of fields, and a statement indicating whether a semantic configuration exists. For the purposes of this quickstart, the message should say `No semantic configuration exists for this index`.
-
-## Update the index with a semantic configuration
-
-1. Create a file in `./src` called `updateIndexSettings.js` and copy in the following code to add a semantic configuration to the existing `hotels-sample-index` index on your search service. No search documents are deleted by this operation and your index is still operational after the configuration is added.
-
-    ```javascript
-    import {
-        SearchIndexClient
-    } from "@azure/search-documents";
-    import { searchEndpoint, indexName, credential, semanticConfigurationName } from "./config.js";
-    
-    try {
-    
-        const indexClient = new SearchIndexClient(searchEndpoint, credential);
-    
-        const existingIndex = await indexClient.getIndex(indexName);
-    
-        const fields = {
-            titleField: {
-                name: "HotelName"
-            },
-            keywordsFields: [{
-                name: "Tags"
-            }],
-            contentFields: [{
-                name: "Description"
-            }]
-        };
-    
-        const newSemanticConfiguration = {
-            name: semanticConfigurationName,
-            prioritizedFields: fields
-        };
-    
-        // Add the new semantic configuration to the existing index
-        if (existingIndex.semanticSearch && existingIndex.semanticSearch.configurations) {
-            existingIndex.semanticSearch.configurations.push(newSemanticConfiguration);
-        } else {
-            const configExists = existingIndex.semanticSearch?.configurations?.some(
-                config => config.name === semanticConfigurationName
-            );
-            if (!configExists) {
-                existingIndex.semanticSearch = {
-                    configurations: [newSemanticConfiguration]
-                };
-            }
-        }
-    
-        await indexClient.createOrUpdateIndex(existingIndex);
-    
-        const updatedIndex = await indexClient.getIndex(indexName);
-    
-        console.log(`Semantic configurations:`);
-        console.log("-".repeat(40));
-    
-        if (updatedIndex.semanticSearch && updatedIndex.semanticSearch.configurations) {
-            for (const config of updatedIndex.semanticSearch.configurations) {
-                console.log(`Configuration name: ${config.name}`);
-                console.log(`Title field: ${config.prioritizedFields.titleField?.name}`);
-                console.log(`Keywords fields: ${config.prioritizedFields.keywordsFields?.map(f => f.name).join(", ")}`);
-                console.log(`Content fields: ${config.prioritizedFields.contentFields?.map(f => f.name).join(", ")}`);
-                console.log("-".repeat(40));
-            }
-        } else {
-            console.log("No semantic configurations found.");
-        }
-    
-        console.log("Semantic configuration updated successfully.");
-    } catch (error) {
-        console.error("Error updating semantic configuration:", error);
-    }
+1. Run a semantic query.
+
+    ```bash
+    node -r dotenv/config src/semanticQuery.js
     ```
 
-1. Run the code.
+1. Run a semantic query with captions.
 
     ```bash
-    node -r dotenv/config src/updateIndexSettings.js
+    node -r dotenv/config src/semanticQueryReturnCaptions.js
     ```
 
-1. Output is the semantic configuration you just added, `Semantic configuration updated successfully.`.
+1. Run a semantic query with answers.
 
-## Run semantic queries
+    ```bash
+    node -r dotenv/config src/semanticAnswer.js
+    ```
 
-Once the `hotels-sample-index` index has a semantic configuration, you can run queries that include semantic parameters.
+### Output
+
+The `getIndexSettings.js` script returns the name of the index, its fields, and any existing semantic configurations.
+
+```output
+Getting semantic ranking index settings...
+Index name: hotels-sample
+Number of fields: 23
+Field: HotelId, Type: Edm.String, Searchable: true
+Field: HotelName, Type: Edm.String, Searchable: true
+Field: Description, Type: Edm.String, Searchable: true
+Field: Description_fr, Type: Edm.String, Searchable: true
+Field: Category, Type: Edm.String, Searchable: true
+Field: Tags, Type: Collection(Edm.String), Searchable: true
+// Trimmed for brevity
+Semantic ranking configurations: 1
+Configuration name: hotels-sample-semantic-configuration
+Title field: undefined
+```
 
-1. Create a file in `./src` called `semanticQuery.js` and copy in the following code to create a semantic query of the index. This is the minimum requirement for invoking semantic ranking.
+The `updateIndexSettings.js` script returns all semantic configurations on the index, including the one the code added, followed by a success message.
+
+```output
+Semantic configurations:
+----------------------------------------
+Configuration name: hotels-sample-semantic-configuration
+Title field: undefined
+Keywords fields:
+Content fields: AzureSearch_DocumentKey
+----------------------------------------
+Configuration name: semantic-config
+Title field: HotelName
+Keywords fields: Tags
+Content fields: Description
+----------------------------------------
+Semantic configuration updated successfully.
+```
 
-    ```javascript
-    import { SearchClient } from "@azure/search-documents";
-    import { credential, searchEndpoint, indexName, semanticConfigurationName } from "./config.js";
-    
-    const searchClient = new SearchClient(
-        searchEndpoint,
-        indexName,
-        credential
-    );
-    
-    const results = await searchClient.search("walking distance to live music", {
+The `semanticQuery.js` script returns all matching documents ordered by the semantic ranking re-ranker score.
+
+```output
+Search result #1:
+  Re-ranker Score: 2.613231658935547
+  HotelId: 24
+  HotelName: Uptown Chic Hotel
+  Description: Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance.
+
+Search result #2:
+  Re-ranker Score: 2.271434783935547
+  HotelId: 2
+  HotelName: Old Century Hotel
+  Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
+
+Search result #3:
+  Re-ranker Score: 1.9861756563186646
+  HotelId: 4
+  HotelName: Sublime Palace Hotel
+  Description: Sublime Cliff Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience.
+// Trimmed for brevity
+```
+
+The `semanticQueryReturnCaptions.js` script returns a caption element with hit highlighting alongside search fields. Captions are the most relevant passages in a result. If your index includes larger text, captions help extract the most interesting sentences.
+
+```output
+Search result #1:
+  Re-ranker Score: 2.613231658935547
+  HotelName: Uptown Chic Hotel
+  Description: Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance.
+
+  Caption with highlights: Chic hotel near the city. High-rise hotel in downtown, within walking distance to<em> theaters, </em>art galleries, restaurants and shops. Visit<em> Seattle Art Museum </em>by day, and then head over to<em> Benaroya Hall </em>to catch the evening's concert performance.
+------------------------------------------------------------
+Search result #2:
+  Re-ranker Score: 2.271434783935547
+  HotelName: Old Century Hotel
+  Description: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music.
+
+  Caption text: The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live.
+------------------------------------------------------------
+// Trimmed for brevity
+```
+
+The `semanticAnswer.js` script returns a semantic answer pulled from one of the results that best matches the question, followed by search results with captions.
+
+```output
+Answers:
+
+Semantic answer result #1:
+Semantic Answer: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
+Semantic Answer Score: 0.9829999804496765
+
+Search Results:
+
+Search result #1:
+2.124817371368408
+Stay-Kay City Hotel
+This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
+Caption: This classic hotel is<em> fully-refurbished </em>and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
+// Trimmed for brevity
+```
+
+## Understand the code
+
+[!INCLUDE [understand code note](../understand-code-note.md)]
+
+Now that you've run the code, let's break down the key steps:
+
+1. [Configuration and authentication](#configuration-and-authentication)
+1. [Update the index with a semantic configuration](#update-the-index-with-a-semantic-configuration)
+1. [Query the index](#query-the-index)
+
+### Configuration and authentication
+
+The `config.js` file loads environment variables and creates a `DefaultAzureCredential` for authentication.
+
+```javascript
+import { DefaultAzureCredential }
+    from "@azure/identity";
+
+export const searchEndpoint =
+    process.env.AZURE_SEARCH_ENDPOINT
+    || "PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE";
+export const indexName =
+    process.env.AZURE_SEARCH_INDEX_NAME
+    || "hotels-sample";
+export const semanticConfigurationName =
+    process.env.SEMANTIC_CONFIGURATION_NAME
+    || "semantic-config";
+
+export const credential = new DefaultAzureCredential();
+```
+
+Key takeaways:
+
++ `DefaultAzureCredential` provides keyless authentication using Microsoft Entra ID. It chains multiple credential types, including the Azure CLI credential from `az login`.
++ Environment variables are loaded from the `.env` file using `dotenv`.
+
+### Update the index with a semantic configuration
+
+The `updateIndexSettings.js` file adds a semantic configuration to the existing `hotels-sample` index. This operation doesn't delete any search documents, and your index remains operational after the configuration is added.
+
+```javascript
+import { SearchIndexClient }
+    from "@azure/search-documents";
+import {
+    searchEndpoint, indexName,
+    credential, semanticConfigurationName
+} from "./config.js";
+
+const indexClient = new SearchIndexClient(
+    searchEndpoint, credential
+);
+const existingIndex =
+    await indexClient.getIndex(indexName);
+
+const fields = {
+    titleField: { name: "HotelName" },
+    keywordsFields: [{ name: "Tags" }],
+    contentFields: [{ name: "Description" }]
+};
+
+const newSemanticConfiguration = {
+    name: semanticConfigurationName,
+    prioritizedFields: fields
+};
+
+if (existingIndex.semanticSearch
+    && existingIndex.semanticSearch.configurations) {
+    existingIndex.semanticSearch.configurations
+        .push(newSemanticConfiguration);
+} else {
+    existingIndex.semanticSearch = {
+        configurations: [newSemanticConfiguration]
+    };
+}
+
+await indexClient.createOrUpdateIndex(existingIndex);
+```
+
+Key takeaways:
+
++ A semantic configuration specifies the fields used for semantic ranking. `titleField` defines the document title, `contentFields` defines the main content, and `keywordsFields` defines the keyword or tag fields.
++ You create a configuration object and push it to the existing index's `semanticSearch.configurations` array.
++ `createOrUpdateIndex` pushes the updated schema to the search service without rebuilding the index or deleting documents.
+
+### Query the index
+
+The query scripts run three queries in sequence, progressing from a basic semantic search to semantic ranking with captions and answers.
+
+#### Semantic query (no captions, no answers)
+
+The following code shows the minimum requirement for invoking semantic ranking.
+
+```javascript
+import { SearchClient }
+    from "@azure/search-documents";
+import {
+    credential, searchEndpoint,
+    indexName, semanticConfigurationName
+} from "./config.js";
+
+const searchClient = new SearchClient(
+    searchEndpoint, indexName, credential
+);
+
+const results = await searchClient.search(
+    "walking distance to live music",
+    {
         queryType: "semantic",
         semanticSearchOptions: {
-            configurationName: semanticConfigurationName
+            configurationName:
+                semanticConfigurationName
         },
-        select: ["HotelId", "HotelName", "Description"]
-    });
-    
-    let rowNumber = 1;
-    for await (const result of results.results) {
-        // Log each result
-        const doc = result.document;
-        const score = result.score;
-        const rerankerScoreDisplay = result.rerankerScore;
-    
-        console.log(`Search result #${rowNumber++}:`);
-        console.log(`  Re-ranker Score: ${rerankerScoreDisplay}`);
-        console.log(`  HotelId: ${doc.HotelId}`);
-        console.log(`  HotelName: ${doc.HotelName}`);
-        console.log(`  Description: ${doc.Description || 'N/A'}\n`);
+        select: [
+            "HotelId", "HotelName", "Description"
+        ]
     }
-    ```
-
-1. Run the code.
-
-    ```bash
-    node -r dotenv/config src/semanticQuery.js
-    ```
+);
+```
 
-1. Output should consist of 13 documents, ordered by the `rerankerScoreDisplay`.
+Key takeaways:
 
-### Return captions
++ `queryType: "semantic"` enables semantic ranking on the query.
++ `semanticSearchOptions.configurationName` specifies which semantic configuration to use.
++ The `rerankerScore` in results indicates semantic relevance (higher is better).
 
-Optionally, you can add captions to extract portions of the text and apply hit highlighting to the important terms and phrases. This query adds captions.
+#### Semantic query with captions
 
-1. Create a file in `./src` called `semanticQueryReturnCaptions.js` and copy in the following code to add captions to the query.
+The following code adds captions to extract the most relevant passages from each result, with hit highlighting applied to the important terms and phrases.
 
-    ```javascript
-    import { SearchClient } from "@azure/search-documents";
-    import { credential, searchEndpoint, indexName, semanticConfigurationName } from "./config.js";
-    
-    const searchClient = new SearchClient(
-        searchEndpoint,
-        indexName,
-        credential
-    );
-    
-    console.log(`Using semantic configuration: ${semanticConfigurationName}`);
-    console.log("Search query: walking distance to live music");
-    
-    const results = await searchClient.search("walking distance to live music", {
+```javascript
+const results = await searchClient.search(
+    "walking distance to live music",
+    {
         queryType: "semantic",
         semanticSearchOptions: {
-            configurationName: semanticConfigurationName,
+            configurationName:
+                semanticConfigurationName,
             captions: {
                 captionType: "extractive",
                 highlight: true
             }
         },
-        select: ["HotelId", "HotelName", "Description"],
-    });
-    
-    console.log(`Found ${results.count} results with semantic search\n`);
-    let rowNumber = 1;
-    
-    for await (const result of results.results) {
-        // Log each result
-        const doc = result.document;
-        const rerankerScoreDisplay = result.rerankerScore;
-    
-        console.log(`Search result #${rowNumber++}:`);
-        console.log(`  Re-ranker Score: ${rerankerScoreDisplay}`);
-        console.log(`  HotelName: ${doc.HotelName}`);
-        console.log(`  Description: ${doc.Description || 'N/A'}\n`);
-    
-        // Caption handling with better debugging
-        const captions = result.captions;
-        
-        if (captions && captions.length > 0) {
-            const caption = captions[0];
-            
-            if (caption.highlights) {
-                console.log(`  Caption with highlights: ${caption.highlights}`);
-            } else if (caption.text) {
-                console.log(`  Caption text: ${caption.text}`);
-            } else {
-                console.log(`  Caption exists but has no text or highlights content`);
-            }
-        } else {
-            console.log("  No captions found for this result");
+        select: [
+            "HotelId", "HotelName", "Description"
+        ]
+    }
+);
+
+for await (const result of results.results) {
+    const captions = result.captions;
+    if (captions && captions.length > 0) {
+        const caption = captions[0];
+        if (caption.highlights) {
+            console.log(
+                `Caption: ${caption.highlights}`
+            );
         }
-        console.log("-".repeat(60));
     }
-    ```
-
-1. Run the code.
-
-    ```bash
-    node -r dotenv/config src/semanticQueryReturnCaptions.js
-    ```
-
-1. Output should include a new caption element alongside search field. Captions are the most relevant passages in a result. If your index includes larger chunks of text, a caption is helpful for extracting the most interesting sentences.
-
-    ```console
-    Search result #1:
-      Re-ranker Score: 2.613231658935547
-      HotelName: Uptown Chic Hotel
-      Description: Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance.
-    
-      Caption with highlights: Chic hotel near the city. High-rise hotel in downtown, within walking distance to<em> theaters, </em>art galleries, restaurants and shops. Visit<em> Seattle Art Museum </em>by day, and then head over to<em> Benaroya Hall </em>to catch the evening's concert performance.
-    ```
+}
+```
 
-### Return semantic answers
+Key takeaways:
 
-In this final query, return semantic answers.
++ `captions.captionType: "extractive"` enables extractive captions from the content fields.
++ Captions surface the most relevant passages and add `<em>` tags around important terms.
 
-Semantic ranker can produce an answer to a query string that has the characteristics of a question. The generated answer is extracted verbatim from your content so it won't include composed content like what you might expect from a chat completion model. If the semantic answer isn't useful for your scenario, you can omit `semantic_answers` from your code.
+#### Semantic query with answers
 
-To produce a semantic answer, the question and answer must be closely aligned, and the model must find content that clearly answers the question. If potential answers fail to meet a confidence threshold, the model doesn't return an answer. For demonstration purposes, the question in this example is designed to get a response so that you can see the syntax.
+The final query adds semantic answers. This query uses a question as the search text because semantic answers work best when the query is phrased as a question. The answer is a verbatim passage extracted from your index, not a composed response from a chat completion model.
 
-1. Create a file in `./src` called `semanticAnswer.js` and copy in the following code to get semantic answers. 
+The query and the indexed content must be closely aligned for an answer to be returned. If no candidate meets the confidence threshold, the response doesn't include an answer. This example uses a question that's known to produce a result so that you can see the syntax. If answers aren't useful for your scenario, omit `answers` from your code. For composed answers, consider a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
 
-    ```javascript
-    import { SearchClient } from "@azure/search-documents";
-    import { credential, searchEndpoint, indexName, semanticConfigurationName } from "./config.js";
-    
-    const searchClient = new SearchClient(
-        searchEndpoint,
-        indexName,
-        credential
-    );
-    
-    const results = await searchClient.search("What's a good hotel for people who like to read", {
+```javascript
+const results = await searchClient.search(
+    "What's a good hotel for people who "
+    + "like to read",
+    {
         queryType: "semantic",
         semanticSearchOptions: {
-            configurationName: semanticConfigurationName,
+            configurationName:
+                semanticConfigurationName,
             captions: {
                 captionType: "extractive"
             },
             answers: {
                 answerType: "extractive"
             }
         },
-        select: ["HotelName", "Description", "Category"]
-    });
-    
-    console.log(`Answers:\n\n`);
-    let rowNumber = 1; 
-    
-    // Extract semantic answers from the search results
-    const semanticAnswers = results.answers;
-    for (const answer of semanticAnswers || []) {
-        console.log(`Semantic answer result #${rowNumber++}:`);
-        if (answer.highlights) {
-            console.log(`Semantic Answer: ${answer.highlights}`);
-        } else {
-            console.log(`Semantic Answer: ${answer.text}`);
-        }
-        console.log(`Semantic Answer Score: ${answer.score}\n\n`);
+        select: [
+            "HotelName", "Description", "Category"
+        ]
     }
-    
-    console.log(`Search Results:\n\n`);
-    rowNumber = 1;
-    
-    // Iterate through the search results
-    for await (const result of results.results) {
-        // Log each result
-        const doc = result.document;
-        const rerankerScoreDisplay = result.rerankerScore;
-    
-        console.log(`Search result #${rowNumber++}:`);
-        console.log(`${rerankerScoreDisplay}`);
-        console.log(`${doc.HotelName}`);
-        console.log(`${doc.Description || 'N/A'}`);
-    
-        const captions = result.captions;
-    
-        if (captions && captions.length > 0) {
-            const caption = captions[0];
-            if (caption.highlights) {
-                console.log(`Caption: ${caption.highlights}\n`);
-            } else {
-                console.log(`Caption: ${caption.text}\n`);
-            }
-        }
+);
+
+const semanticAnswers = results.answers;
+for (const answer of semanticAnswers || []) {
+    if (answer.highlights) {
+        console.log(
+            `Semantic Answer: ${answer.highlights}`
+        );
+    } else {
+        console.log(
+            `Semantic Answer: ${answer.text}`
+        );
     }
-    ```
-
-1. Run the code.
-
-    ```bash
-    node -r dotenv/config src/semanticAnswer.js
-    ```
-
-1. Output should look similar to the following example, where the best answer to question is pulled from one of the results.
+    console.log(
+        `Semantic Answer Score: ${answer.score}`
+    );
+}
+```
 
-    Recall that answers are *verbatim content* pulled from your index and might be missing phrases that a user would expect to see. To get *composed answers* as generated by a chat completion model, considering using a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
+Key takeaways:
 
-    ```console
-    Semantic answer result #1:
-    Semantic Answer: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
-    Semantic Answer Score: 0.9829999804496765
-    ```
++ `answers.answerType: "extractive"` enables extractive answers for question-like queries.
++ Answers are verbatim content extracted from your index, not generated text.
++ `results.answers` retrieves the answer objects separately from the search results.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript用セマンティックランカーのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、JavaScript向けのセマンティックランカーに関するクイックスタートガイドの更新を含み、全体で680行が変更されました。その内訳は、343行の追加と337行の削除です。主な目的は、セマンティックランキング機能の追加および更新された情報を提供することにあります。

変更点としては、Azure AI SearchのJavaScriptクライアントライブラリを使用して、既存の検索インデックスにセマンティックランキングを追加し、インデックスをクエリする手順が詳細に説明されています。新たに追加された内容には、GitHubによるソースコードのダウンロードリンク、必要な前提条件（Azureアカウント、Azure AI Searchサービス、Node.jsなど）、およびプロジェクト設定の手順が含まれています。

また、セマンティッククエリの実行例が整理され、キャプションやセマンティックアンサーを使った詳細なクエリの実行手順も含まれています。これによって、ユーザーはインデックス設定の取得やセマンティック構成の追加、さまざまなクエリの実行方法を本ガイドを通じて学ぶことができます。

このアップデートにより、ユーザーにとっての利用体験が向上し、セマンティックランキングの有用性を最大限に活用できるような情報の提供が強化されています。また、実際のコードサンプルが追加されたことで、具体的な実装がより分かりやすくなっています。

## articles/search/includes/quickstarts/semantic-ranker-python.md{#item-a6dcfa}

<details>
<summary>Diff</summary>
````diff
@@ -4,327 +4,388 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
+  - dev-focus
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 03/04/2026
+ai-usage: ai-assisted
 ---
 
-[!INCLUDE [Semantic ranker introduction](semantic-ranker-intro.md)]
+In this quickstart, you use the [Azure AI Search client library for Python](/python/api/overview/azure/search-documents-readme) to add [semantic ranking](../../semantic-search-overview.md) to an existing search index and query the index.
 
-## Set up the client
+Semantic ranking is query-side functionality that uses machine reading comprehension to rescore search results, promoting the most semantically relevant matches to the top of the list. You can add a semantic configuration to an existing index with no rebuild requirement. Semantic ranking is most effective for informational or descriptive text.
 
-In this quickstart, use a Jupyter notebook and the [**azure-search-documents**](/python/api/overview/azure/search-documents-readme) library in the Azure SDK for Python to learn about semantic ranking.
+> [!TIP]
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Ranking) on GitHub.
 
-We recommend [Visual Studio Code](https://code.visualstudio.com/download) with Python 3.10 or later and the [Python extension](https://code.visualstudio.com/docs/languages/python) for this quickstart.
+## Prerequisites
 
-> [!TIP]
-> You can [download a finished notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Ranking) to start with a finished project or follow these steps to create your own.
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
+
++ An [Azure AI Search service](../../search-create-service-portal.md) with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
+
++ An [index](../../search-how-to-create-search-index.md) with descriptive text fields attributed as `searchable` and `retrievable`.  This quickstart assumes the [hotels-sample index](../../search-get-started-portal.md).
+
++ [Python 3.10](https://www.python.org/downloads/) or later.
 
-We recommend a virtual environment for this quickstart:
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
 
-1. Start Visual Studio Code.
++ [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-1. Open the **semantic-ranking-quickstart.ipynb** file or create a new notebook.
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-1. Open the Command Palette by using **Ctrl+Shift+P**.
+## Configure access
 
-1. Search for **Python: Create Environment**.
+[!INCLUDE [resource authentication](../resource-authentication-semantic.md)]
 
-1. Select **`Venv.`**
+## Get endpoint
 
-1. Select a Python interpreter. Choose 3.10 or later.
+[!INCLUDE [resource endpoint](../resource-endpoint.md)]
 
-It can take a minute to set up. If you run into problems, see [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments).
+## Start with an index
 
-### Install packages and set environment variables
+[!INCLUDE [start with an index](semantic-ranker-index.md)]
 
-1. Install packages, including [azure-search-documents](/python/api/azure-search-documents).
+## Set up the environment
 
-    ```python
-   ! pip install -r requirements.txt --quiet
+1. Use Git to clone the sample repository.
+
+    ```bash
+    git clone https://github.com/Azure-Samples/azure-search-python-samples
     ```
 
-1. Rename `sample.env` to `.env`, and provide your search service endpoint. You can get the endpoint from the Azure portal on the search service **Overview** page.
+1. Navigate to the quickstart folder and open it in Visual Studio Code.
 
-    ```python
-    AZURE_SEARCH_ENDPOINT=https://your-search-service.search.windows.net
-    AZURE_SEARCH_INDEX_NAME=hotels-sample-index
+    ```bash
+    cd azure-search-python-samples/Quickstart-Semantic-Ranking
+    code .
     ```
 
-### Sign in to Azure
+1. In `sample.env`, replace the placeholder value for `AZURE_SEARCH_ENDPOINT` with the URL you obtained in [Get endpoint](#get-endpoint).
 
-If you signed in to the [Azure portal](https://portal.azure.com), you're signed into Azure. If you aren't sure, use the Azure CLI or Azure PowerShell to log in: `az login` or `az connect`. If you have multiple tenants and subscriptions, see [Quickstart: Connect without keys](../../search-get-started-rbac.md) for help on how to connect.
+1. Rename `sample.env` to `.env`.
 
-## Update the index
+    ```bash
+    mv sample.env .env
+    ```
 
-In this section, you update a search index to include a semantic configuration. The code gets the index definition from the search service and adds a semantic configuration.
+1. Open `semantic-ranking-quickstart.ipynb`.
 
-1. Open the [semantic-ranking-quickstart.ipynb](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Semantic-Ranking/semantic-ranking-quickstart.ipynb) file in Visual Studio Code or create a new file.
+1. Press **Ctrl+Shift+P**, select **Notebook: Select Notebook Kernel**, and follow the prompts to create a virtual environment. Select **requirements.txt** for the dependencies.
 
-1. Provide the variables used in the solution.
+   When complete, you should see a `.venv` folder in the project directory.
 
-    ```python
-    # Provide variables
-    from dotenv import load_dotenv
-    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
-    import os
-    
-    load_dotenv(override=True) # Take environment variables from .env.
-    
-    # The following variables from your .env file are used in this notebook
-    search_endpoint = os.environ["AZURE_SEARCH_ENDPOINT"]
-    credential = DefaultAzureCredential()
-    token_provider = get_bearer_token_provider(credential, "https://search.azure.com/.default")
-    index_name = os.getenv("AZURE_SEARCH_INDEX", "hotels-sample-index")
-    ```
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
-1. Create a SearchIndexClient and get the existing hotels-sample-index.
-
-    ```python
-    from azure.search.documents.indexes import SearchIndexClient
-    from azure.identity import DefaultAzureCredential
-    import os
-    
-    # Initialize the client (similar to what you already have)
-    search_endpoint = os.environ["AZURE_SEARCH_ENDPOINT"]
-    credential = DefaultAzureCredential()
-    index_name = "hotels-sample-index"  # or use your existing index_name variable
-    
-    # Create the SearchIndexClient
-    index_client = SearchIndexClient(endpoint=search_endpoint, credential=credential)
-    
-    try:
-        # Get the existing index schema
-        index = index_client.get_index(index_name)
-        
-        print(f"Index name: {index.name}")
-        print(f"Number of fields: {len(index.fields)}")
-        
-        # Print field details
-        for field in index.fields:
-            print(f"Field: {field.name}, Type: {field.type}, Searchable: {field.searchable}")
-        
-        # Access semantic configuration if it exists
-        if index.semantic_search and index.semantic_search.configurations:
-            for config in index.semantic_search.configurations:
-                print(f"Semantic config: {config.name}")
-                if config.prioritized_fields.title_field:
-                    print(f"Title field: {config.prioritized_fields.title_field.field_name}")
-        else:
-            print("No semantic configuration exists for this index")
-    
-    except Exception as ex:
-        print(f"Error retrieving index: {ex}")
+    ```azurecli
+    az login
     ```
 
-1. Run the code.
+## Run the code
+
+1. Run the `Install packages and set variables` cells to install the required packages and load environment variables.
+
+1. Run the remaining cells sequentially to add a semantic configuration and query the index.
+
+### Output
+
+The output of the `Get the index definition` cell is the name of the index, its fields, and any existing semantic configurations.
+
+```output
+Index name: hotels-sample
+Number of fields: 23
+Field: HotelId, Type: Edm.String, Searchable: True
+Field: HotelName, Type: Edm.String, Searchable: True
+Field: Description, Type: Edm.String, Searchable: True
+Field: Description_fr, Type: Edm.String, Searchable: True
+Field: Category, Type: Edm.String, Searchable: True
+Field: Tags, Type: Collection(Edm.String), Searchable: True
+// Trimmed for brevity
+Semantic config: hotels-sample-semantic-configuration
+Title field: HotelName
+```
+
+The output of the `Add a semantic configuration to the index` cell lists all semantic configurations on the index, including the one the code added, followed by a success message.
+
+```output
+Semantic configurations:
+----------------------------------------
+  Configuration: hotels-sample-semantic-configuration
+    Title field: HotelName
+    Keywords fields: Category
+    Content fields: Description
+
+  Configuration: semantic-config
+    Title field: HotelName
+    Keywords fields: Tags
+    Content fields: Description
+
+✅ Semantic configuration successfully added!
+```
+
+The output of the `Run a term query` cell returns all matching documents ordered by BM25 score. This baseline query doesn't use semantic ranking.
+
+```output
+5.360838
+4
+Sublime Palace Hotel
+Description: Sublime Cliff Hotel is located in the heart of the
+historic center of Sublime in an extremely vibrant and lively area
+within short walking distance to the sites and landmarks of the city
+and is surrounded by the extraordinary beauty of churches, buildings,
+shops and monuments. Sublime Cliff is part of a lovingly restored
+19th century resort, updated for every modern convenience.
+4.691083
+2
+Old Century Hotel
+Description: The hotel is situated in a nineteenth century plaza,
+which has been expanded and renovated to the highest architectural
+standards to create a modern, functional and first-class hotel in
+which art and unique historical elements coexist with the most
+modern comforts. The hotel also regularly hosts events like wine
+tastings, beer dinners, and live music.
+// Trimmed for brevity
+```
+
+The output of the `Run a semantic query` cell returns all matching documents ordered by the semantic re-ranker score.
+
+```output
+2.613231658935547
+24
+Uptown Chic Hotel
+Description: Chic hotel near the city. High-rise hotel in downtown,
+within walking distance to theaters, art galleries, restaurants and
+shops. Visit Seattle Art Museum by day, and then head over to
+Benaroya Hall to catch the evening's concert performance.
+2.271434783935547
+2
+Old Century Hotel
+Description: The hotel is situated in a nineteenth century plaza,
+which has been expanded and renovated to the highest architectural
+standards to create a modern, functional and first-class hotel in
+which art and unique historical elements coexist with the most
+modern comforts. The hotel also regularly hosts events like wine
+tastings, beer dinners, and live music.
+// Trimmed for brevity
+```
+
+The output of the `Return captions` cell adds a caption element with hit highlighting alongside search fields. Captions are the most relevant passages in a result. If your index includes larger text, captions help extract the most interesting sentences.
+
+```output
+2.613231658935547
+24
+Uptown Chic Hotel
+Description: Chic hotel near the city. High-rise hotel in downtown,
+within walking distance to theaters, art galleries, restaurants and
+shops. Visit Seattle Art Museum by day, and then head over to
+Benaroya Hall to catch the evening's concert performance.
+Caption: Chic hotel near the city. High-rise hotel in downtown,
+within walking distance to<em> theaters, </em>art galleries,
+restaurants and shops. Visit<em> Seattle Art Museum </em>by day, and
+then head over to<em> Benaroya Hall </em>to catch the evening's
+concert performance.
+// Trimmed for brevity
+```
+
+The output of the `Return semantic answers` cell includes a semantic answer pulled from one of the results that best matches the question, followed by search results with captions.
+
+```output
+Semantic Answer: Nature is Home on the beach. Explore the shore by
+day, and then come home to our shared living space to relax around a
+stone fireplace, sip something warm, and explore the<em> library
+</em>by night. Save up to 30 percent. Valid Now through the end of
+the year. Restrictions and blackouts may apply.
+Semantic Answer Score: 0.9829999804496765
+```
+
+## Understand the code
+
+[!INCLUDE [understand code note](../understand-code-note.md)]
+
+Now that you've run the code, let's break down the key steps:
+
+1. [Configuration and authentication](#configuration-and-authentication)
+1. [Update the index with a semantic configuration](#update-the-index-with-a-semantic-configuration)
+1. [Query the index](#query-the-index)
+
+### Configuration and authentication
+
+The `Install packages and set variables` cell loads environment variables and creates a `DefaultAzureCredential` for authentication.
+
+```python
+from dotenv import load_dotenv
+from azure.identity import DefaultAzureCredential
+from azure.identity import get_bearer_token_provider
+import os
+
+load_dotenv(override=True)
+
+search_endpoint = os.environ["AZURE_SEARCH_ENDPOINT"]
+credential = DefaultAzureCredential()
+index_name = os.getenv(
+    "AZURE_SEARCH_INDEX", "hotels-sample"
+)
+```
+
+Key takeaways:
+
++ `DefaultAzureCredential` provides keyless authentication using Microsoft Entra ID. It chains multiple credential types, including the Azure CLI credential from `az login`.
++ Environment variables are loaded from the `.env` file using `python-dotenv`.
+
+### Update the index with a semantic configuration
+
+The `Add a semantic configuration to the index` cell adds a semantic configuration to the existing `hotels-sample` index. This operation doesn't delete any search documents, and your index remains operational after the configuration is added.
+
+```python
+from azure.search.documents.indexes.models import (
+    SemanticConfiguration,
+    SemanticField,
+    SemanticPrioritizedFields,
+    SemanticSearch
+)
+
+new_semantic_config = SemanticConfiguration(
+    name="semantic-config",
+    prioritized_fields=SemanticPrioritizedFields(
+        title_field=SemanticField(field_name="HotelName"),
+        keywords_fields=[
+            SemanticField(field_name="Tags")
+        ],
+        content_fields=[
+            SemanticField(field_name="Description")
+        ]
+    )
+)
 
-1. Output is the name of the index, list of fields, and a statement indicating whether a semantic configuration exists. For the purposes of this quickstart, the message should say "No semantic configuration exists for this index".
+if existing_index.semantic_search is None:
+    existing_index.semantic_search = SemanticSearch(
+        configurations=[new_semantic_config]
+    )
+else:
+    existing_index.semantic_search.configurations.append(
+        new_semantic_config
+    )
 
-1. Add a semantic configuration to an existing hotels-sample-index on your search service. No search documents are deleted by this operation and your index is still operational after the configuration is added.
+result = index_client.create_or_update_index(existing_index)
+```
 
-    ```python
-    # Add semantic configuration to hotels-sample-index and display updated index details
-    from azure.search.documents.indexes.models import (
-        SemanticConfiguration,
-        SemanticField,
-        SemanticPrioritizedFields,
-        SemanticSearch
-    )
-    
-    try:
-        # Get the existing index
-        existing_index = index_client.get_index(index_name)
-        
-        # Create a new semantic configuration
-        new_semantic_config = SemanticConfiguration(
-            name="semantic-config",
-            prioritized_fields=SemanticPrioritizedFields(
-                title_field=SemanticField(field_name="HotelName"),
-                keywords_fields=[SemanticField(field_name="Tags")],
-                content_fields=[SemanticField(field_name="Description")]
-            )
-        )
-        
-        # Add semantic configuration to the index
-        if existing_index.semantic_search is None:
-            existing_index.semantic_search = SemanticSearch(configurations=[new_semantic_config])
-        else:
-            # Check if configuration already exists
-            config_exists = any(config.name == "semantic-config" 
-                              for config in existing_index.semantic_search.configurations)
-            if not config_exists:
-                existing_index.semantic_search.configurations.append(new_semantic_config)
-        
-        # Update the index
-        result = index_client.create_or_update_index(existing_index)
-        
-        # Get the updated index and display detailed information
-        updated_index = index_client.get_index(index_name)
-        
-        print("Semantic configurations:")
-        print("-" * 40)
-        if updated_index.semantic_search and updated_index.semantic_search.configurations:
-            for config in updated_index.semantic_search.configurations:
-                print(f"  Configuration: {config.name}")
-                if config.prioritized_fields.title_field:
-                    print(f"    Title field: {config.prioritized_fields.title_field.field_name}")
-                if config.prioritized_fields.keywords_fields:
-                    keywords = [kf.field_name for kf in config.prioritized_fields.keywords_fields]
-                    print(f"    Keywords fields: {', '.join(keywords)}")
-                if config.prioritized_fields.content_fields:
-                    content = [cf.field_name for cf in config.prioritized_fields.content_fields]
-                    print(f"    Content fields: {', '.join(content)}")
-                print()
-        else:
-            print("  No semantic configurations found")
-        
-        print("✅ Semantic configuration successfully added!")
-        
-    except Exception as ex:
-        print(f"❌ Error adding semantic configuration: {ex}")
-    ```
+Key takeaways:
 
-1. Run the code.
++ A semantic configuration specifies the fields used for semantic ranking. `title_field` sets the document title, `content_fields` sets the main content, and `keywords_fields` sets the keyword or tag fields.
++ You create the configuration with `SemanticConfiguration` and its associated `SemanticPrioritizedFields` model, and then append it to the existing index.
++ `create_or_update_index` pushes the updated schema to the search service without rebuilding the index or deleting documents.
 
-1. Output is the semantic configuration you just added.
+### Query the index
 
-## Run semantic queries
+The query cells run four queries in sequence: a baseline keyword search followed by three semantic ranking variations with increasing functionality.
 
-Once the index has a semantic configuration, you can run queries that include semantic parameters.
+#### Term query (baseline)
 
-1. Create a SearchClient and a query request that includes the semantic query type and the semantic configuration. This is the minimum requirement for invoking semantic ranking.
+The `Run a term query` cell runs a keyword search using BM25 scoring. This baseline query doesn't use semantic ranking and serves as a comparison point.
 
-    ```python
-    # Set up the search client
-    search_client = SearchClient(endpoint=search_endpoint,
-                          index_name=index_name,
-                          credential=credential)
-    
-    # Runs a semantic query (runs a BM25-ranked query, rescoring and promoting the most semantically relevant matches to the top)
-    results =  search_client.search(query_type='semantic', semantic_configuration_name='semantic-config',
-        search_text="walking distance to live music", 
-        select='HotelId,HotelName,Description', query_caption='extractive')
-    
-    for result in results:
-        print(result["@search.reranker_score"])
-        print(result["HotelId"])
-        print(result["HotelName"])
-        print(f"Description: {result['Description']}")
-    ```
+```python
+from azure.search.documents import SearchClient
 
-1. Run the code.
-
-1. Output should consist of 13 documents, ordered by the `"@search.reranker_score"`.
-
-### Return captions
-
-Optionally, you can add captions to extract portions of the text and apply hit highlighting to the important terms and phrases. This query adds captions.
-
-1. Add `captions` to the query.
-
-    ```python
-    # Runs a semantic query that returns captions
-    results =  search_client.search(query_type='semantic', semantic_configuration_name='semantic-config',
-        search_text="walking distance to live music", 
-        select='HotelName,HotelId,Description', query_caption='extractive')
-    
-    for result in results:
-        print(result["@search.reranker_score"])
-        print(result["HotelId"])
-        print(result["HotelName"])
-        print(f"Description: {result['Description']}")
-    
-        captions = result["@search.captions"]
-        if captions:
-            caption = captions[0]
-            if caption.highlights:
-                print(f"Caption: {caption.highlights}\n")
-            else:
-                print(f"Caption: {caption.text}\n")
-    ```
+search_client = SearchClient(
+    endpoint=search_endpoint,
+    index_name=index_name,
+    credential=credential
+)
 
-1. Run the code.
+results = search_client.search(
+    query_type='simple',
+    search_text="walking distance to live music",
+    select='HotelId,HotelName,Description',
+    include_total_count=True
+)
+```
 
-1. Output should include a new caption element alongside search field. Captions are the most relevant passages in a  result. If your index includes larger chunks of text, a caption is helpful for extracting the most interesting sentences.
+Key takeaways:
 
-    ```bash
-    2.613231658935547
-    24
-    Uptown Chic Hotel
-    Description: Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance.
-    Caption: Chic hotel near the city. High-rise hotel in downtown, within walking distance to<em> theaters, </em>art galleries, restaurants and shops. Visit<em> Seattle Art Museum </em>by day, and then head over to<em> Benaroya Hall </em>to catch the evening's concert performance.
-    ```
++ `query_type='simple'` specifies a keyword search using BM25 scoring.
++ The `@search.score` in results indicates the BM25 relevance score.
 
-### Return semantic answers
-
-In this final query, return semantic answers.
-
-Semantic ranker can produce an answer to a query string that has the characteristics of a question. The generated answer is extracted verbatim from your content so it won't include composed content like what you might expect from a chat completion model. If the semantic answer isn't useful for your scenario, you can omit `semantic_answers` from your code.
-
-To produce a semantic answer, the question and answer must be closely aligned, and the model must find content that clearly answers the question. If potential answers fail to meet a confidence threshold, the model doesn't return an answer. For demonstration purposes, the question in this example is designed to get a response so that you can see the syntax.
-
-1. Add `answers` to the query.
-
-    ```python
-    # Run a semantic query that returns semantic answers  
-    results =  search_client.search(query_type='semantic', semantic_configuration_name='semantic-config',
-     search_text="what's a good hotel for people who like to read",
-     select='HotelName,Description,Category', query_caption='extractive', query_answer="extractive",)
-    
-    semantic_answers = results.get_answers()
-    for answer in semantic_answers:
-        if answer.highlights:
-            print(f"Semantic Answer: {answer.highlights}")
-        else:
-            print(f"Semantic Answer: {answer.text}")
-        print(f"Semantic Answer Score: {answer.score}\n")
-    
-    for result in results:
-        print(result["@search.reranker_score"])
-        print(result["HotelName"])
-        print(f"Description: {result['Description']}")
-    
-        captions = result["@search.captions"]
-        if captions:
-            caption = captions[0]
-            if caption.highlights:
-                print(f"Caption: {caption.highlights}\n")
-            else:
-                print(f"Caption: {caption.text}\n")
-    ```
+#### Semantic query (no captions, no answers)
 
-1. Run the code.
+The `Run a semantic query` cell shows the minimum requirement for invoking semantic ranking.
 
-1. Output should look similar to the following example, where the best answer to question is pulled from one of the results.
+```python
+from azure.search.documents import SearchClient
 
-    Recall that answers are *verbatim content* pulled from your index and might be missing phrases that a user would expect to see. To get *composed answers* as generated by a chat completion model, considering using a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
+search_client = SearchClient(
+    endpoint=search_endpoint,
+    index_name=index_name,
+    credential=credential
+)
 
-    ```bash
-    Semantic Answer: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
-    Semantic Answer Score: 0.9829999804496765
-    
-    2.124817371368408
-    1
-    Stay-Kay City Hotel
-    Description: This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
-    Caption: This classic hotel is<em> fully-refurbished </em>and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.
-    
-    2.0705394744873047
-    16
-    Double Sanctuary Resort
-    Description: 5 star Luxury Hotel - Biggest Rooms in the city. #1 Hotel in the area listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso in room.
-    Caption: <em>5 star Luxury Hotel </em>-<em> Biggest </em>Rooms in the city. #1 Hotel in the area listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso in room.
-    
-    2.041472911834717
-    38
-    Lakeside B & B
-    Description: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the library by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
-    Caption: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
-    
-    2.084540843963623
-    Double Sanctuary Resort
-    Description: 5 star Luxury Hotel - Biggest Rooms in the city. #1 Hotel in the area listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso in room.
-    Caption: <em>5 star Luxury Hotel </em>-<em> Biggest </em>Rooms in the<em> city. #1 </em>Hotel in the area listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso in room.
-    
-    ...
-    ```
+results = search_client.search(
+    query_type='semantic',
+    semantic_configuration_name='semantic-config',
+    search_text="walking distance to live music",
+    select='HotelId,HotelName,Description',
+    query_caption='extractive'
+)
+```
+
+Key takeaways:
+
++ `query_type='semantic'` enables semantic ranking on the query.
++ `semantic_configuration_name` specifies which semantic configuration to use.
++ The `@search.reranker_score` in results indicates semantic relevance (higher is better).
+
+#### Semantic query with captions
+
+The `Return captions` cell adds captions to extract the most relevant passages from each result, with hit highlighting applied to the important terms and phrases.
+
+```python
+results = search_client.search(
+    query_type='semantic',
+    semantic_configuration_name='semantic-config',
+    search_text="walking distance to live music",
+    select='HotelName,HotelId,Description',
+    query_caption='extractive'
+)
+
+for result in results:
+    captions = result["@search.captions"]
+    if captions:
+        caption = captions[0]
+        if caption.highlights:
+            print(f"Caption: {caption.highlights}\n")
+```
+
+Key takeaways:
+
++ `query_caption='extractive'` enables extractive captions from the content fields.
++ Captions surface the most relevant passages and add `<em>` tags around important terms.
+
+#### Semantic query with answers
+
+The `Return semantic answers` cell adds semantic answers. This query uses a question as the search text because semantic answers work best when the query is phrased as a question. The answer is a verbatim passage extracted from your index, not a composed response from a chat completion model.
+
+The query and the indexed content must be closely aligned for an answer to be returned. If no candidate meets the confidence threshold, the response doesn't include an answer. This example uses a question that's known to produce a result so that you can see the syntax. If answers aren't useful for your scenario, omit `query_answer` from your code. For composed answers, consider a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
+
+```python
+results = search_client.search(
+    query_type='semantic',
+    semantic_configuration_name='semantic-config',
+    search_text="what's a good hotel for people who "
+                "like to read",
+    select='HotelName,Description,Category',
+    query_caption='extractive',
+    query_answer="extractive",
+)
+
+semantic_answers = results.get_answers()
+for answer in semantic_answers:
+    if answer.highlights:
+        print(f"Semantic Answer: {answer.highlights}")
+    else:
+        print(f"Semantic Answer: {answer.text}")
+    print(f"Semantic Answer Score: {answer.score}\n")
+```
+
+Key takeaways:
+
++ `query_answer="extractive"` enables extractive answers for question-like queries.
++ Answers are verbatim content extracted from your index, not generated text.
++ `results.get_answers()` retrieves the answer objects separately from the search results.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python用セマンティックランカーのクイックスタートガイドの更新"
}
```

### Explanation
このコード変更は、Pythonにおけるセマンティックランカーのクイックスタートガイドが大幅に更新されたことを示しています。全体で609行が変更され、その内訳は335行の追加と274行の削除を含みます。この更新の主な目的は、ユーザーがPythonのAzure AI Searchクライアントライブラリを用いて、既存の検索インデックスにセマンティックランキングを追加し、インデックスをクエリするための具体的な手順を詳細に理解できるようにすることです。

新しく追加された内容には、セマンティックランキングの機能やその効果的な利用法が説明され、GitHubからのソースコードのダウンロードリンク、Azureアカウントや検索サービスの具体的な構成についての前提条件が含まれています。また、VS Codeの使用法や仮想環境の設定方法、Azure CLIを用いた認証の設定に関する手順も詳述されています。

更新後のガイドでは、セマンティッククエリの実行例が追加されており、実際にデータを取得するプロセスや結果の表示方法までが具体的に示されています。このことにより、ユーザーはクイックスタートガイドを通じて、簡単にプロジェクトを設定し、効果的にセマンティック検索を実行できるようになります。

いずれの手順も、ユーザーが手を動かしながら理解を深めるのに役立つように設計されており、より良い学習体験を提供することが狙いとされています。

## articles/search/includes/quickstarts/semantic-ranker-rest.md{#item-d74861}

<details>
<summary>Diff</summary>
````diff
@@ -4,365 +4,337 @@ author: heidisteen
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 03/04/2026
+ai-usage: ai-assisted
 ---
 
-[!INCLUDE [Semantic ranker introduction](semantic-ranker-intro.md)]
+In this quickstart, you use the [Azure AI Search REST APIs](/rest/api/searchservice) to add [semantic ranking](../../semantic-search-overview.md) to an existing search index and query the index.
 
-## Set up the client
+Semantic ranking is query-side functionality that uses machine reading comprehension to rescore search results, promoting the most semantically relevant matches to the top of the list. You can add a semantic configuration to an existing index with no rebuild requirement. Semantic ranking is most effective for informational or descriptive text.
 
-In this quickstart, you use a REST client and the [Azure AI Search REST APIs](/rest/api/searchservice) to configure and use a semantic ranker.
+> [!TIP]
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-semantic-ranking) on GitHub.
 
-We recommend [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for this quickstart.
+## Prerequisites
 
-> [!TIP]
-> You can download the [source code](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/Quickstart-semantic-ranking) to start with a finished project or follow these steps to create your own.
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-1. Start Visual Studio Code and open the [semantic-index-update.rest](https://github.com/Azure-Samples/azure-search-rest-samples/blob/main/Quickstart-semantic-ranking/semantic-index-update.rest) file or create a new file.
++ An [Azure AI Search service](../../search-create-service-portal.md) with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
 
-1. At the top, set environment variables for your search service, authorization, and index name.
++ An [index](../../search-how-to-create-search-index.md) with descriptive text fields attributed as `searchable` and `retrievable`.  This quickstart assumes the [hotels-sample index](../../search-get-started-portal.md).
 
-   + For @searchURL, sign in to the Azure portal and copy the URL from the search service **Overview** page.
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
-   + For @personalAccessToken, follow the instructions in [Connect without keys](../../search-get-started-rbac.md) to get your personal access token.
++ [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-1. To test the connection, send your first request.
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-   ```http
-   ### List existing indexes by name (verify the connection)
-    GET  {{searchUrl}}/indexes?api-version=2025-09-01&$select=name  HTTP/1.1
-    Authorization: Bearer {{personalAccessToken}}
-   ```
+## Configure access
 
-1. Select **Send Request**.
+[!INCLUDE [resource authentication](../resource-authentication-semantic.md)]
 
-   :::image type="content" source="../../media/search-get-started-semantic/visual-studio-code-send-request.png" alt-text="Screenshot of the REST client send request link.":::
+## Get endpoint
 
-1. Output for this GET request returns a list of existing indexes. You should get an HTTP 200 Success status code and a list of indexes, including hotels-sample-index used in this quickstart.
+[!INCLUDE [resource endpoint](../resource-endpoint.md)]
 
-## Update the index
+## Start with an index
 
-To update an index using the REST API, you must provide the entire schema, plus the modifications you want to make. This request provides hotels-sample-index schema, plus the semantic configuration. The modification consists of the following JSON.
+[!INCLUDE [start with an index](semantic-ranker-index.md)]
 
-```json
-"semantic": {
-   "configurations": [
-   {
-      "name": "semantic-config",
-      "rankingOrder": "BoostedRerankerScore",
-      "prioritizedFields": {
-         "titleField": { "fieldName": "HotelName" },
-         "prioritizedContentFields": [{ "fieldName": "Description" }],
-         "prioritizedKeywordsFields": [{ "fieldName": "Tags" }]
-      }
-   }
-   ]
-}
-```
+## Set up the environment
 
-1. Formulate a PUT request specifying the index name, operation, and full JSON schema. All required elements of the schema must be present. This request includes the full schema for hotels-sample-index plus the semantic configuration.
+1. Use Git to clone the sample repository.
 
-    ```http
-    PUT {{searchUrl}}/indexes/hotels-sample-index?api-version=2025-09-01  HTTP/1.1
-    Content-Type: application/json
-    Authorization: Bearer {{personalAccessToken}}
-    
-    {
-       "name": "hotels-sample-index",
-       "fields": [
-           { "name": "HotelId", "type": "Edm.String", "searchable": false, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true, "key": true },
-           { "name": "HotelName", "type": "Edm.String", "searchable": true, "filterable": false, "retrievable": true, "stored": true, "sortable": false, "facetable": false, "analyzer": "en.microsoft" },
-           { "name": "Description", "type": "Edm.String", "searchable": true, "filterable": false, "retrievable": true, "stored": true, "sortable": false, "facetable": false, "analyzer": "en.microsoft" },
-           { "name": "Description_fr", "type": "Edm.String", "searchable": true, "filterable": false, "retrievable": true, "stored": true, "sortable": false, "facetable": false, "analyzer": "fr.microsoft" },
-           { "name": "Category", "type": "Edm.String", "searchable": true, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true, "analyzer": "en.microsoft" },
-           { "name": "Tags", "type": "Collection(Edm.String)", "searchable": true, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true, "analyzer": "en.microsoft" },
-           { "name": "ParkingIncluded", "type": "Edm.Boolean", "searchable": false, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true },
-           { "name": "LastRenovationDate", "type": "Edm.DateTimeOffset", "searchable": false, "filterable": false, "retrievable": true, "stored": true, "sortable": true, "facetable": false },
-           { "name": "Rating", "type": "Edm.Double", "searchable": false, "filterable": true, "retrievable": true, "stored": true, "sortable": true, "facetable": true },
-           { "name": "Address", "type": "Edm.ComplexType", "fields": [
-              { "name": "StreetAddress", "type": "Edm.String", "searchable": true, "filterable": false, "retrievable": true, "stored": true, "sortable": false, "facetable": false, "analyzer": "en.microsoft" },
-              { "name": "City", "type": "Edm.String", "searchable": true, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true, "analyzer": "en.microsoft" },
-              { "name": "StateProvince", "type": "Edm.String", "searchable": true, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true, "analyzer": "en.microsoft" },
-              { "name": "PostalCode", "type": "Edm.String", "searchable": true, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true, "analyzer": "en.microsoft" },
-              { "name": "Country", "type": "Edm.String", "searchable": true, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true, "analyzer": "en.microsoft" }]},
-           { "name": "Location", "type": "Edm.GeographyPoint", "searchable": false, "filterable": true, "retrievable": true, "stored": true, "sortable": true, "facetable": false },
-           { "name": "Rooms", "type": "Collection(Edm.ComplexType)", "fields": [
-              { "name": "Description", "type": "Edm.String", "searchable": true, "filterable": false, "retrievable": true, "stored": true, "sortable": false, "facetable": false, "analyzer": "en.microsoft" },
-              { "name": "Description_fr", "type": "Edm.String", "searchable": true, "filterable": false, "retrievable": true, "stored": true, "sortable": false, "facetable": false, "analyzer": "fr.microsoft" },
-              { "name": "Type", "type": "Edm.String", "searchable": true, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true, "analyzer": "en.microsoft" },
-              { "name": "BaseRate", "type": "Edm.Double", "searchable": false, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true },
-              { "name": "BedOptions", "type": "Edm.String", "searchable": true, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true, "analyzer": "en.microsoft" },
-              { "name": "SleepsCount", "type": "Edm.Int64", "searchable": false, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true },
-              { "name": "SmokingAllowed", "type": "Edm.Boolean", "searchable": false, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true },
-              { "name": "Tags", "type": "Collection(Edm.String)", "searchable": true, "filterable": true, "retrievable": true, "stored": true, "sortable": false, "facetable": true, "analyzer": "en.microsoft" }]},
-           { "name": "id", "type": "Edm.String", "searchable": false, "filterable": false, "retrievable": false, "stored": true, "sortable": false, "facetable": false },
-           { "name": "rid", "type": "Edm.String", "searchable": false, "filterable": false, "retrievable": false, "stored": true, "sortable": false, "facetable": false }],
-      "scoringProfiles": [],
-      "suggesters": [],
-      "analyzers": [],
-      "normalizers": [],
-      "tokenizers": [],
-      "tokenFilters": [],
-      "charFilters": [],
-      "similarity": {
-        "@odata.type": "#Microsoft.Azure.Search.BM25Similarity"
-      },
-      "semantic": {
-        "configurations": [
-          {
-            "name": "semantic-config",
-            "rankingOrder": "BoostedRerankerScore",
-            "prioritizedFields": {
-              "titleField": {
-                "fieldName": "HotelName"
-              },
-              "prioritizedContentFields": [
-                {
-                  "fieldName": "Description"
-                }
-              ],
-              "prioritizedKeywordsFields": [
-                {
-                  "fieldName": "Tags"
-                }
-              ]
-            }
-          }
-        ]
-      }
-    }
+    ```bash
+    git clone https://github.com/Azure-Samples/azure-search-rest-samples
     ```
 
-1. Select **Send Request**.
+1. Navigate to the quickstart folder and open it in Visual Studio Code.
 
-1. Output for this POST request is an `HTTP 200 Success` status message.
+    ```bash
+    cd azure-search-rest-samples/Quickstart-semantic-ranking
+    code .
+    ```
 
-## Run semantic queries
+1. In `semantic-index-update.rest`, replace the placeholder value for `@searchUrl` with the URL you obtained in [Get endpoint](#get-endpoint).
 
-Required semantic parameters include `query_type` and `semantic_configuration_name`. Here's an example of a basic semantic query using the minimum parameters.
+1. Repeat the previous step for `semantic-query.rest`.
 
-1. Open the [semantic-query.rest](https://github.com/Azure-Samples/azure-search-rest-samples/blob/main/Quickstart-semantic-ranking/semantic-query.rest) file or create a new file.
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
-1. At the top of the file, set environment variables for your search service, authorization, and index name.
+    ```azurecli
+    az login
+    ```
 
-   + For @searchURL, sign in to the Azure portal and copy the URL from the search service **Overview** page.
+1. For keyless authentication with Microsoft Entra ID, generate an access token.
 
-   + For @personalAccessToken, follow the instructions in [Connect without keys](../../search-get-started-rbac.md) to get your personal access token.
+    ```azurecli
+    az account get-access-token --scope https://search.azure.com/.default --query accessToken --output tsv
+    ```
 
-1. Test the connection with a GET request that returns the hotels-sample-index.
+1. In both `.rest` files, replace the placeholder value for `@personalAccessToken` with the token from the previous step.
 
-    ```http
-    GET {{searchUrl}}/indexes/hotels-sample-index?api-version=2025-09-01  HTTP/1.1
-    Authorization: Bearer {{personalAccessToken}}
-    ```
+## Run the code
 
-1. Send a query that includes the semantic query type and configuration name.
+1. Open `semantic-index-update.rest`.
 
-   ```http
-    POST {{searchUrl}}/indexes/hotels-sample-index/docs/search?api-version=2025-09-01  HTTP/1.1
-    Content-Type: application/json
-    Authorization: Bearer {{personalAccessToken}}
-    
-    {
-      "search": "walking distance to live music",
-      "select": "HotelId, HotelName, Description",
-      "count": true,
-      "top": 7,
-      "queryType": "simple"
-    }
-   ```
+1. Select **Send Request** on the first GET request to verify your connection.
 
-1. Output consists of JSON search results. Thirteen hotels match the query. The top seven are included in this example.
+    A response should appear in an adjacent pane. If you have existing indexes, they're listed by name. If the HTTP code is `200 OK`, you're ready to proceed.
 
-   ```json
-   {
-      "@odata.count": 13,
-      "@search.answers": [],
-      "value": [
-        {
-          "@search.score": 5.074317,
-          "@search.rerankerScore": 2.613231658935547,
-          "HotelId": "24",
-          "HotelName": "Uptown Chic Hotel",
-          "Description": "Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance."
-        },
-        {
-          "@search.score": 5.5153193,
-          "@search.rerankerScore": 2.271434783935547,
-          "HotelId": "2",
-          "HotelName": "Old Century Hotel",
-          "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music."
-        },
-        {
-          "@search.score": 4.8959594,
-          "@search.rerankerScore": 1.9861756563186646,
-          "HotelId": "4",
-          "HotelName": "Sublime Palace Hotel",
-          "Description": "Sublime Cliff Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 19th century resort, updated for every modern convenience."
-        },
-        {
-          "@search.score": 0.7334347,
-          "@search.rerankerScore": 1.9615401029586792,
-          "HotelId": "39",
-          "HotelName": "White Mountain Lodge & Suites",
-          "Description": "Live amongst the trees in the heart of the forest. Hike along our extensive trail system. Visit the Natural Hot Springs, or enjoy our signature hot stone massage in the Cathedral of Firs. Relax in the meditation gardens, or join new friends around the communal firepit. Weekend evening entertainment on the patio features special guest musicians or poetry readings."
-        },
-        {
-          "@search.score": 1.5502293,
-          "@search.rerankerScore": 1.9085469245910645,
-          "HotelId": "15",
-          "HotelName": "By the Market Hotel",
-          "Description": "Book now and Save up to 30%. Central location. Walking distance from the Empire State Building & Times Square, in the Chelsea neighborhood. Brand new rooms. Impeccable service."
-        },
-        {
-          "@search.score": 1.7595702,
-          "@search.rerankerScore": 1.90234375,
-          "HotelId": "49",
-          "HotelName": "Swirling Currents Hotel",
-          "Description": "Spacious rooms, glamorous suites and residences, rooftop pool, walking access to shopping, dining, entertainment and the city center. Each room comes equipped with a microwave, a coffee maker and a minifridge. In-room entertainment includes complimentary W-Fi and flat-screen TVs. "
-        },
-        {
-          "@search.score": 2.0364518,
-          "@search.rerankerScore": 1.9012802839279175,
-          "HotelId": "31",
-          "HotelName": "Country Residence Hotel",
-          "Description": "All of the suites feature full-sized kitchens stocked with cookware, separate living and sleeping areas and sofa beds. Some of the larger rooms have fireplaces and patios or balconies. Experience real country hospitality in the heart of bustling Nashville. The most vibrant music scene in the world is just outside your front door."
-        }
-      ]
-    }
-    ```
+1. Send the `### Update the hotels-sample index to include a semantic configuration` request to add a semantic configuration to the index.
+
+    If you get a `400 Bad Request` error, your index schema differs from the sample. Send the `### Get the schema of the index` request, copy the response JSON, add the `semantic` section from the source code to the JSON, and replace the PUT request body with your merged schema.
 
-### Return captions
+1. Switch to `semantic-query.rest` and send the requests sequentially: a simple query for baseline comparison, and then semantic queries with ranking, captions, and answers.
 
-Optionally, you can add captions to extract portions of the text and apply hit highlighting to the important terms and phrases. This query adds captions that include hit highlighting.
+### Output
 
-1. Add the `captions` parameter and send the request.
+The `Send a search query to the hotels-sample index` request returns results ranked by BM25 relevance, which is indicated by the `@search.score` field.
 
-    ```http
-    POST {{searchUrl}}/indexes/hotels-sample-index/docs/search?api-version=2025-09-01  HTTP/1.1
-    Content-Type: application/json
-    Authorization: Bearer {{personalAccessToken}}
-    
+```json
+{
+  "@odata.count": 30,
+  "value": [
     {
-      "search": "walking distance to live music",
-      "select": "HotelId, HotelName, Description",
-      "count": true,
-      "queryType": "semantic",
-      "semanticConfiguration": "semantic-config",
-      "captions": "extractive|highlight-true"
-    }
-    ```
+      "@search.score": 5.004435,
+      "HotelId": "2",
+      "HotelName": "Old Century Hotel",
+      "Description": "The hotel is situated in a nineteenth century plaza..."
+    },
+    // Trimmed for brevity
+  ]
+}
+```
 
-1. Output consists of the same results, with the addition of `"@search.captions"`. Here's the JSON for a single document. Each match includes search scores, captions in plain text and highlight formatting, and the select fields.
+The `Send a search query to the hotels-sample index with semantic ranking` request adds `@search.rerankerScore`. Notice that the order changes from the simple query.
 
-   ```json
-   {
-      "@search.score": 5.074317,
+```json
+{
+  "@odata.count": 30,
+  "@search.answers": [],
+  "value": [
+    {
+      "@search.score": 4.555706,
+      "@search.rerankerScore": 2.613231658935547,
+      "HotelId": "24",
+      "HotelName": "Uptown Chic Hotel",
+      "Description": "Chic hotel near the city. High-rise hotel in downtown..."
+    },
+    // Trimmed for brevity
+  ]
+}
+```
+
+The `Return captions in the query` request adds `@search.captions` with extracted text and highlights.
+
+```json
+{
+  "value": [
+    {
+      "@search.score": 4.555706,
       "@search.rerankerScore": 2.613231658935547,
       "@search.captions": [
         {
-          "text": "Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance.",
-          "highlights": "Chic hotel near the city. High-rise hotel in downtown, within walking distance to<em> theaters, </em>art galleries, restaurants and shops. Visit<em> Seattle Art Museum </em>by day, and then head over to<em> Benaroya Hall </em>to catch the evening's concert performance."
+          "text": "Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops...",
+          "highlights": "Chic hotel near the city. High-rise hotel in downtown, within walking distance to<em> theaters, </em>art galleries, restaurants and shops..."
         }
       ],
       "HotelId": "24",
-      "HotelName": "Uptown Chic Hotel",
-      "Description": "Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance."
-   }
-   ```
+      "HotelName": "Uptown Chic Hotel"
+    },
+    // Trimmed for brevity
+  ]
+}
+```
 
-### Return semantic answers
+The `Return semantic answers in the query` request returns an extractive answer in `@search.answers` when the query is phrased as a question.
 
-In this final query, return semantic answers.
+```json
+{
+  "@odata.count": 46,
+  "@search.answers": [
+    {
+      "key": "38",
+      "text": "Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the library by night...",
+      "highlights": "Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night...",
+      "score": 0.9829999804496765
+    }
+  ],
+  "value": [
+    {
+      "@search.score": 2.060124,
+      "@search.rerankerScore": 2.124817371368408,
+      "@search.captions": [
+        {
+          "text": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city...",
+          "highlights": "This classic hotel is<em> fully-refurbished </em>and ideally located on the main commercial artery of the city..."
+        }
+      ],
+      "HotelId": "1",
+      "HotelName": "Stay-Kay City Hotel"
+    },
+    // Trimmed for brevity
+  ]
+}
+```
 
-Semantic ranker can produce an answer to a query string that has the characteristics of a question. The generated answer is extracted verbatim from your content so it won't include composed content like what you might expect from a chat completion model. If the semantic answer isn't useful for your scenario, you can omit `semantic_answers` from your code.
+## Understand the code
 
-To produce a semantic answer, the question and answer must be closely aligned, and the model must find content that clearly answers the question. If potential answers fail to meet a confidence threshold, the model doesn't return an answer. For demonstration purposes, the question in this example is designed to get a response so that you can see the syntax.
+[!INCLUDE [understand code note](../understand-code-note.md)]
 
-1. Formulate the request using a search string that asks a question.
+Now that you've run the code, let's break down the key steps:
 
-    ```http
-    POST {{searchUrl}}/indexes/hotels-sample-index/docs/search?api-version=2025-09-01  HTTP/1.1
-    Content-Type: application/json
-    Authorization: Bearer {{personalAccessToken}}
-    
-    {
-      "search": "what's a good hotel for people who like to read",
-      "select": "HotelId, HotelName, Description",
-      "count": true,
-      "queryType": "semantic",
-      "semanticConfiguration": "semantic-config"
-      "answers": "extractive"
-    }
-    ```
+1. [Configuration and authentication](#configuration-and-authentication)
+1. [Update the index with a semantic configuration](#update-the-index-with-a-semantic-configuration)
+1. [Query the index](#query-the-index)
+
+### Configuration and authentication
 
-1. Output consists of 41 results for the new query, with "@search.answers" for the question in the query about hotels for people who like to read.
+Both `.rest` files define variables at the top for reuse across all requests.
 
-   Recall that answers are *verbatim content* pulled from your index and might be missing phrases that a user would expect to see. To get *composed answers* as generated by a chat completion model, considering using a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
+```http
+@searchUrl = PUT-YOUR-SEARCH-SERVICE-URL-HERE
+@personalAccessToken = PUT-YOUR-PERSONAL-ACCESS-TOKEN-HERE
+@api-version = 2025-09-01
+```
 
-   In this example, the answer is considered as a strong fit for the question.
+Key takeaways:
 
-    ```json
-    {
-      "@odata.count": 41,
-      "@search.answers": [
-        {
-          "key": "38",
-          "text": "Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the library by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.",
-          "highlights": "Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.",
-          "score": 0.9829999804496765
-        }
-      ],
-      "value": [
-        {
-          "@search.score": 2.0361428,
-          "@search.rerankerScore": 2.124817371368408,
-          "HotelId": "1",
-          "HotelName": "Stay-Kay City Hotel",
-          "Description": "This classic hotel is fully-refurbished and ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Times Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities."
-        },
-        {
-          "@search.score": 3.759768,
-          "@search.rerankerScore": 2.0705394744873047,
-          "HotelId": "16",
-          "HotelName": "Double Sanctuary Resort",
-          "Description": "5 star Luxury Hotel - Biggest Rooms in the city. #1 Hotel in the area listed by Traveler magazine. Free WiFi, Flexible check in/out, Fitness Center & espresso in room."
-        },
-        {
-          "@search.score": 0.7308748,
-          "@search.rerankerScore": 2.041472911834717,
-          "HotelId": "38",
-          "HotelName": "Lakeside B & B",
-          "Description": "Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the library by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply."
-        },
-        {
-          "@search.score": 3.391012,
-          "@search.rerankerScore": 2.0231292247772217,
-          "HotelId": "2",
-          "HotelName": "Old Century Hotel",
-          "Description": "The hotel is situated in a nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts. The hotel also regularly hosts events like wine tastings, beer dinners, and live music."
-        },
-        {
-          "@search.score": 1.3198771,
-          "@search.rerankerScore": 2.021622657775879,
-          "HotelId": "15",
-          "HotelName": "By the Market Hotel",
-          "Description": "Book now and Save up to 30%. Central location. Walking distance from the Empire State Building & Times Square, in the Chelsea neighborhood. Brand new rooms. Impeccable service."
-        },
-        {
-          "@search.score": 1.3983066,
-          "@search.rerankerScore": 2.005582809448242,
-          "HotelId": "5",
-          "HotelName": "Red Tide Hotel",
-          "Description": "On entering this charming hotel in Scarlet Harbor, you'll notice an uncommon blend of antiques, original artwork, and contemporary comforts that give this hotel its signature look. Each suite is furnished to accentuate the views and unique characteristics of the building's classic architecture. No two suites are alike. However, all guests are welcome in the mezzanine plaza, the surrounding gardens, and the northside terrace for evening refreshments."
-        },
++ `@searchUrl` is the endpoint of your search service.
++ `@personalAccessToken` is a Microsoft Entra ID token obtained from the Azure CLI. This replaces API keys with keyless authentication.
++ `Authorization: Bearer {{personalAccessToken}}` is included in every request header for authentication.
+
+### Update the index with a semantic configuration
+
+The `### Update the hotels-sample index to include a semantic configuration` request in `semantic-index-update.rest` sends the full index schema along with a new `semantic` section. The REST API requires the complete schema for any update operation, so you can't send only the semantic configuration.
+
+The key addition is the `semantic` section:
+
+```json
+"semantic": {
+    "configurations": [
         {
-          "@search.score": 1.4815493,
-          "@search.rerankerScore": 1.9739465713500977,
-          "HotelId": "24",
-          "HotelName": "Uptown Chic Hotel",
-          "Description": "Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance."
+            "name": "semantic-config",
+            "rankingOrder":
+                "BoostedRerankerScore",
+            "prioritizedFields": {
+                "titleField": {
+                    "fieldName": "HotelName"
+                },
+                "prioritizedContentFields": [
+                    {
+                        "fieldName": "Description"
+                    }
+                ],
+                "prioritizedKeywordsFields": [
+                    {
+                        "fieldName": "Tags"
+                    }
+                ]
+            }
         }
-      ]
-    }
-    ```
+    ]
+}
+```
+
+Key takeaways:
+
++ `titleField` identifies which field contains the document title for semantic evaluation.
++ `prioritizedContentFields` identifies the main content fields. Semantic ranker evaluates these first when scoring relevance.
++ `prioritizedKeywordsFields` identifies keyword or tag fields for additional context.
++ `rankingOrder: BoostedRerankerScore` combines the BM25 score with the semantic reranker score.
++ The REST API requires the full schema for PUT operations. Only the `semantic` section is new; all other fields are unchanged.
+
+### Query the index
+
+The requests in `semantic-query.rest` progress from a simple keyword search to semantic ranking with captions and answers. All queries are POST requests to the [Documents - Search Post](/rest/api/searchservice/documents/search-post) (REST API).
+
+#### Simple query
+
+The `### Send a search query to the hotels-sample index` request is a simple keyword search that doesn't use semantic ranking. It serves as a baseline for comparing results with and without semantic reranking.
+
+```json
+{
+    "search":
+        "walking distance to live music",
+    "select":
+        "HotelId, HotelName, Description",
+    "count": true,
+    "queryType": "simple"
+}
+```
+
+Key takeaways:
+
++ `queryType: "simple"` uses the default BM25 ranking algorithm.
++ Results are ranked by keyword relevance (`@search.score`) only.
+
+#### Semantic query (no captions, no answers)
+
+The `### Send a search query to the hotels-sample index with semantic ranking` request adds semantic ranking. The following JSON shows the minimum requirement for invoking semantic ranking.
+
+```json
+{
+    "search":
+        "walking distance to live music",
+    "select":
+        "HotelId, HotelName, Description",
+    "count": true,
+    "queryType": "semantic",
+    "semanticConfiguration": "semantic-config"
+}
+```
+
+Key takeaways:
+
++ `queryType: "semantic"` enables semantic ranking on the query.
++ `semanticConfiguration` specifies which semantic configuration to use.
+
+#### Semantic query with captions
+
+The `### Return captions in the query` request adds captions to extract the most relevant passages from each result, with hit highlighting applied to the important terms and phrases.
+
+```json
+{
+    "search":
+        "walking distance to live music",
+    "select":
+        "HotelId, HotelName, Description",
+    "count": true,
+    "queryType": "semantic",
+    "semanticConfiguration": "semantic-config",
+    "captions": "extractive|highlight-true"
+}
+```
+
+Key takeaways:
+
++ `captions: "extractive|highlight-true"` enables extractive captions with `<em>` tags around important terms.
++ Captions appear in the `@search.captions` array for each result.
+
+#### Semantic query with answers
+
+The `### Return semantic answers in the query` request adds semantic answers. It uses a question as the search text because semantic answers work best when the query is phrased as a question. The answer is a verbatim passage extracted from your index, not a composed response from a chat completion model.
+
+The query and the indexed content must be closely aligned for an answer to be returned. If no candidate meets the confidence threshold, the response doesn't include an answer. This example uses a question that's known to produce a result so that you can see the syntax. If answers aren't useful for your scenario, omit the `answers` parameter from your request. For composed answers, consider a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
+
+```json
+{
+    "search":
+        "what's a good hotel for people who like to read",
+    "select":
+        "HotelId, HotelName, Description",
+    "count": true,
+    "queryType": "semantic",
+    "semanticConfiguration": "semantic-config",
+    "captions": "extractive|highlight-true",
+    "answers": "extractive"
+}
+```
+
+Key takeaways:
+
++ `answers: "extractive"` enables extractive answers for question-like queries.
++ Answers appear in the top-level `@search.answers` array, separate from individual results.
++ Answers are verbatim content extracted from your index, not generated text.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST API用セマンティックランカーのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、REST APIにおけるセマンティックランカーのクイックスタートガイドの更新を示しています。全体で576行が変更され、その内訳は274行の追加と302行の削除です。この更新の主な目的は、ユーザーがAzure AI Search REST APIを使用して、既存の検索インデックスにセマンティックランキングを追加し、インデックスをクエリする手順を明確かつ効果的に理解できるようにすることです。

変更点の中心には、RESTクライアントとAzure AI Search REST APIを使ったセマンティックランキングの設定方法、前提条件の説明、そして実際にインデックスを更新するための具体的な手順が詳細に記述されています。特に、Azureアカウント、検索サービス、インデックスの設定に関する新しい前提条件が加えられ、ユーザーがすぐにプロジェクトを開始できるようにサポートしています。

また、新たにソースコードのダウンロードリンクやGitHubへのリンクが追加されており、ユーザーは実際のプロジェクトファイルを使用して環境設定やクエリ実行の手順を実践的に学ぶことができます。更新されたガイドでは、具体的なクエリの例や、成功したリクエストから得られるレスポンスの構造に関しても詳細に説明されています。

これにより、ユーザーはセマンティックランカーの機能を十分に活用できる基盤を整えられ、REST APIを使用した効果的な検索機能の実装が可能になります。

## articles/search/includes/quickstarts/semantic-ranker-typescript.md{#item-6d5573}

<details>
<summary>Diff</summary>
````diff
@@ -4,496 +4,460 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
+  - dev-focus
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 03/04/2026
+ai-usage: ai-assisted
 ---
 
-[!INCLUDE [Semantic ranker introduction](semantic-ranker-intro.md)]
+In this quickstart, you use the [Azure AI Search client library for JavaScript](/javascript/api/overview/azure/search-documents-readme) (compatible with TypeScript) to add [semantic ranking](../../semantic-search-overview.md) to an existing search index and query the index.
 
-## Set up the client
+Semantic ranking is query-side functionality that uses machine reading comprehension to rescore search results, promoting the most semantically relevant matches to the top of the list. You can add a semantic configuration to an existing index with no rebuild requirement. Semantic ranking is most effective for informational or descriptive text.
 
-In this quickstart, you use an IDE and the [**@azure/search-documents**](https://www.npmjs.com/package/@azure/search-documents) client library to add semantic ranking to an existing search index.
+> [!TIP]
+> Want to get started right away? Download the [source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-ts) on GitHub.
 
-The quickstart assumes the following is available on your computer:
-- [Visual Studio Code](https://code.visualstudio.com/) for this quickstart.
-- [Node.js](https://nodejs.org/) (LTS) for running the sample.
-- [TypeScript](https://www.typescriptlang.org/) for writing the sample code.
+## Prerequisites
 
-> [!TIP]
-> You can download the [source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart-semantic-ranking-ts) to start with a finished project or follow these steps to create your own.
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
+
++ An [Azure AI Search service](../../search-create-service-portal.md) with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
+
++ An [index](../../search-how-to-create-search-index.md) with descriptive text fields attributed as `searchable` and `retrievable`.  This quickstart assumes the [hotels-sample index](../../search-get-started-portal.md).
+
++ [Node.js 20 LTS](https://nodejs.org/en/download/) or later to run the compiled code.
+
++ [TypeScript](https://www.typescriptlang.org/download/) to compile TypeScript to JavaScript.
+
++ [Visual Studio Code](https://code.visualstudio.com/download).
+
++ [Git](https://git-scm.com/downloads) to clone the sample repository.
 
-### Set up local development environment
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
 
-1. Start Visual Studio Code in a new directory.
+## Configure access
 
-   ```bash
-   mkdir semantic-ranking-quickstart && cd semantic-ranking-quickstart
-   code .
-   ```
+[!INCLUDE [resource authentication](../resource-authentication-semantic.md)]
 
-1. Create a new package for ESM modules in your project directory.
+## Get endpoint
 
-   ```bash
-   npm init -y
-   npm pkg set type=module
-   ```
+[!INCLUDE [resource endpoint](../resource-endpoint.md)]
 
-1. Install development packages, including [azure-search-documents](/javascript/api/%40azure/search-documents).
+## Start with an index
+
+[!INCLUDE [start with an index](semantic-ranker-index.md)]
+
+## Set up the environment
+
+1. Use Git to clone the sample repository.
 
     ```bash
-   npm install @azure/identity @azure/search-documents dotenv
+    git clone https://github.com/Azure-Samples/azure-search-javascript-samples
     ```
 
-1. Install development dependency packages.
+1. Navigate to the quickstart folder and open it in Visual Studio Code.
 
     ```bash
-   npm install dotenv @types/node --save-dev
+    cd azure-search-javascript-samples/quickstart-semantic-ranking-ts
+    code .
     ```
 
+1. In `sample.env`, replace the placeholder value for `AZURE_SEARCH_ENDPOINT` with the URL you obtained in [Get endpoint](#get-endpoint).
 
-1. Create a `tsconfig.json` file in your project directory to enable ESM modules and set the module resolution.
+1. Rename `sample.env` to `.env`.
 
-   ```json
-    {
-      "compilerOptions": {
-        "target": "es2022",
-        "module": "esnext",
-        "moduleResolution": "bundler",
-        "rootDir": "./src",
-        "outDir": "./dist/",
-        "esModuleInterop": true,
-        "forceConsistentCasingInFileNames": true,
-        "strict": true,
-        "skipLibCheck": true,
-        "declaration": true,
-        "sourceMap": true,
-        "resolveJsonModule": true,
-        "moduleDetection": "force",
-        "allowSyntheticDefaultImports": true,
-        "verbatimModuleSyntax": false
-      },
-      "include": [
-        "src/**/*.ts"
-      ],
-      "exclude": [
-        "node_modules/**/*",
-        "**/*.spec.ts"
-      ]
-    }
-   ```
+    ```bash
+    mv sample.env .env
+    ```
+
+1. Install the dependencies.
 
-1. Update `package.json` to include a script for building TypeScript files. Add the following line to the `scripts` section.
+    ```bash
+    npm install
+    ```
 
-   ```json
-   "build": "tsc"
-   ```
+    When the installation completes, you should see a `node_modules` folder in the project directory.
 
-1. Create `.env`, and provide your search service endpoint. You can get the endpoint from the Azure portal on the search service **Overview** page.
+1. Build the TypeScript files.
 
-    ```ini
-    AZURE_SEARCH_ENDPOINT=YOUR-SEARCH-SERVICE-ENDPOINT
-    AZURE_SEARCH_INDEX_NAME=hotels-sample-index
-    SEMANTIC_CONFIGURATION_NAME=semantic-config
+    ```bash
+    npm run build
     ```
 
-1. Create a `src` directory in your project directory.
+1. For keyless authentication with Microsoft Entra ID, sign in to your Azure account. If you have multiple subscriptions, select the one that contains your Azure AI Search service.
 
-   ```bash
-   mkdir src
-   ```
+    ```azurecli
+    az login
+    ```
 
-### Sign in to Azure
+## Run the code
 
-If you signed in to the [Azure portal](https://portal.azure.com), you're signed into Azure. If you aren't sure, use the Azure CLI or Azure PowerShell to log in: `az login` or `az connect`. If you have multiple tenants and subscriptions, see [Quickstart: Connect without keys](../../search-get-started-rbac.md) for help on how to connect.
+1. Get the existing index settings.
 
-## Create a common authentication file
+    ```bash
+    node -r dotenv/config dist/getIndexSettings.js
+    ```
 
-Create a file in `./src` called `config.ts` to read the `.env` file and hold the environment variables and authentication credential. Copy in the following code; don't change it. This file will be used by all the other files in this quickstart.
+1. Update the index with a semantic configuration.
 
-```typescript
-import { DefaultAzureCredential } from "@azure/identity";
+    ```bash
+    node -r dotenv/config dist/updateIndexSettings.js
+    ```
 
-// Configuration - use environment variables
-export const searchEndpoint = process.env.AZURE_SEARCH_ENDPOINT || "PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE";
-export const indexName = process.env.AZURE_SEARCH_INDEX_NAME || "hotels-sample-index";
-export const semanticConfigurationName = process.env.SEMANTIC_CONFIGURATION_NAME || "semantic-config";
+1. Run a semantic query.
 
-// Create credential
-export const credential = new DefaultAzureCredential();
+    ```bash
+    node -r dotenv/config dist/semanticQuery.js
+    ```
+
+1. Run a semantic query with captions.
+
+    ```bash
+    node -r dotenv/config dist/semanticQueryReturnCaptions.js
+    ```
 
-console.log(`Using Azure Search endpoint: ${searchEndpoint}`);
-console.log(`Using index name: ${indexName}\n\n`);
+1. Run a semantic query with answers.
+
+    ```bash
+    node -r dotenv/config dist/semanticAnswer.js
+    ```
+
+    > [!NOTE]
+    > These commands run `.js` files from the `dist` folder because you previously transpiled from TypeScript to JavaScript with `npm run build`.
+
+### Output
+
+The `getIndexSettings.js` script returns the index name, field count, field details with type and searchable status, and any existing semantic configurations.
+
+```output
+Index name: hotels-sample
+Number of fields: 23
+Field: HotelId, Type: Edm.String, Searchable: true
+Field: HotelName, Type: Edm.String, Searchable: true
+Field: Description, Type: Edm.String, Searchable: true
+// Trimmed for brevity
+Semantic ranking configurations: 1
+Configuration name: hotels-sample-semantic-configuration
+Title field: undefined
+```
+
+The `updateIndexSettings.js` script returns all semantic configurations, including the one you added.
+
+```output
+Semantic configurations:
+----------------------------------------
+Configuration name: hotels-sample-semantic-configuration
+Title field: undefined
+Keywords fields:
+Content fields: AzureSearch_DocumentKey
+----------------------------------------
+Configuration name: semantic-config
+Title field: HotelName
+Keywords fields: Tags
+Content fields: Description
+----------------------------------------
+Semantic configuration updated successfully.
+```
+
+The `semanticQuery.js` script returns results ordered by the reranker score.
+
+```output
+Search result #1:
+  Re-ranker Score: 2.613231658935547
+  HotelId: 24
+  HotelName: Uptown Chic Hotel
+  Description: Chic hotel near the city. High-rise hotel in downtown,
+  within walking distance to theaters, art galleries, restaurants and
+  shops. Visit Seattle Art Museum by day, and then head over to
+  Benaroya Hall to catch the evening's concert performance.
+
+Search result #2:
+  Re-ranker Score: 2.271434783935547
+  HotelId: 2
+  HotelName: Old Century Hotel
+  Description: The hotel is situated in a nineteenth century plaza...
+  // Trimmed for brevity
+```
+
+The `semanticQueryReturnCaptions.js` script returns extractive captions with hit highlighting. Captions are the most relevant passages in a result.
+
+```output
+Search result #1:
+  Re-ranker Score: 2.613231658935547
+  HotelName: Uptown Chic Hotel
+  Description: Chic hotel near the city. High-rise hotel in downtown,
+  within walking distance to theaters, art galleries, restaurants and
+  shops. Visit Seattle Art Museum by day, and then head over to
+  Benaroya Hall to catch the evening's concert performance.
+
+  Caption with highlights: Chic hotel near the city. High-rise hotel
+  in downtown, within walking distance to<em> theaters, </em>art
+  galleries, restaurants and shops. Visit<em> Seattle Art Museum
+  </em>by day, and then head over to<em> Benaroya Hall </em>to catch
+  the evening's concert performance.
+------------------------------------------------------------
+Search result #2:
+  Re-ranker Score: 2.271434783935547
+  HotelName: Old Century Hotel
+  // Trimmed for brevity
+```
+
+The `semanticAnswer.js` script returns a semantic answer (verbatim content) pulled from the result that best matches the question.
+
+```output
+Semantic answer result #1:
+Semantic Answer: Nature is Home on the beach. Explore the shore by
+day, and then come home to our shared living space to relax around
+a stone fireplace, sip something warm, and explore the<em> library
+</em>by night. Save up to 30 percent. Valid Now through the end of
+the year. Restrictions and blackouts may apply.
+Semantic Answer Score: 0.9829999804496765
+
+Search Results:
+
+Search result #1:
+2.124817371368408
+Stay-Kay City Hotel
+This classic hotel is fully-refurbished and ideally located on the
+main commercial artery of the city in the heart of New York...
+Caption: This classic hotel is<em> fully-refurbished </em>and
+ideally located on the main commercial artery of the city...
+// Trimmed for brevity
+```
+
+## Understand the code
+
+[!INCLUDE [understand code note](../understand-code-note.md)]
+
+Now that you've run the code, let's break down the key steps:
+
+1. [Configuration and authentication](#configuration-and-authentication)
+1. [Update the index with a semantic configuration](#update-the-index-with-a-semantic-configuration)
+1. [Query the index](#query-the-index)
+
+### Configuration and authentication
+
+The `config.ts` file loads environment variables, creates a `DefaultAzureCredential` for authentication, and defines a `HotelDocument` interface for type safety.
+
+```typescript
+import { DefaultAzureCredential }
+    from "@azure/identity";
+
+export const searchEndpoint =
+    process.env.AZURE_SEARCH_ENDPOINT
+    || "PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE";
+export const indexName =
+    process.env.AZURE_SEARCH_INDEX_NAME
+    || "hotels-sample";
+export const semanticConfigurationName =
+    process.env.SEMANTIC_CONFIGURATION_NAME
+    || "semantic-config";
+
+export const credential = new DefaultAzureCredential();
 
-// Hotel document interface
 export interface HotelDocument {
-    "@search.action"?: string;
     HotelId: string;
     HotelName: string;
     Description: string;
     Category: string;
     Tags: string[];
-    ParkingIncluded: string;
-    LastRenovationDate: string;
-    Rating: number;
-    Address: {
-        StreetAddress: string;
-        City: string;
-        StateProvince: string;
-        PostalCode: string;
-        Country: string;
-    };
 }
 ```
 
-## Get the index schema
-
-In this section, you get settings for the existing `hotels-sample-index` index on your search service.
-
-1. Create a file in `./src` called `getIndexSettings.ts` and copy in the following code.
-
-    ```typescript
-    import {
-        SearchIndexClient
-    } from "@azure/search-documents";
-    import { searchEndpoint, indexName, credential } from "./config.js";
-    
-    const indexClient = new SearchIndexClient(searchEndpoint, credential);
-    
-    console.log('Updating semantic search index...');
-    
-    // Get the existing schema
-    const index = await indexClient.getIndex(indexName);
-    
-    console.log(`Index name: ${index.name}`);
-    console.log(`Number of fields: ${index.fields.length}`);
-    
-    for(const field of index.fields) {
-    
-        // @ts-ignore
-        console.log(`Field: ${field.name}, Type: ${field.type}, Searchable: ${field.searchable}`);
-    }
-    
-    if(index.semanticSearch && index.semanticSearch.configurations) {
-        console.log(`Semantic search configurations: ${index.semanticSearch.configurations.length}`);
-        for(const config of index.semanticSearch.configurations) {
-            console.log(`Configuration name: ${config.name}`);
-            console.log(`Title field: ${config.prioritizedFields.titleField?.name}`);
-        }
-    } else {
-        console.log("No semantic configuration exists for this index.");
-    }
-    ```
+Key takeaways:
 
-1. Run the code.
++ `DefaultAzureCredential` provides keyless authentication using Microsoft Entra ID. It chains multiple credential types, including the Azure CLI credential from `az login`.
++ The `HotelDocument` interface provides compile-time type checking for search results, ensuring type-safe access to document fields.
++ Environment variables are loaded from the `.env` file using `dotenv`.
 
-    ```bash
-    npm run build && node -r dotenv/config dist/getIndexSettings.js
-    ```
+### Update the index with a semantic configuration
 
-1. Output is the name of the index, list of fields, and a statement indicating whether a semantic configuration exists. For the purposes of this quickstart, the message should say `No semantic configuration exists for this index`.
-
-## Update the index with a semantic configuration
-
-1. Create a file in `./src` called `updateIndexSettings.ts` and copy in the following code to add a semantic configuration to the existing `hotels-sample-index` index on your search service. No search documents are deleted by this operation and your index is still operational after the configuration is added.
-
-    ```typescript
-    import {
-        SearchIndexClient,
-        SemanticConfiguration,
-        SemanticPrioritizedFields,
-        SemanticField
-    } from "@azure/search-documents";
-    import { searchEndpoint, indexName, credential, semanticConfigurationName } from "./config.js";
-    
-    try {
-    
-        const indexClient = new SearchIndexClient(searchEndpoint, credential);
-    
-        const existingIndex = await indexClient.getIndex(indexName);
-    
-        const fields: SemanticPrioritizedFields = {
-            titleField: {
-                name: "HotelName"
-            },
-            keywordsFields: [{
-                name: "Tags"
-            }] as SemanticField[],
-            contentFields: [{
-                name: "Description"
-            }] as SemanticField[]
-        }
-    
-        const newSemanticConfiguration: SemanticConfiguration = {
-            name: semanticConfigurationName,
-            prioritizedFields: fields
-        };
-    
-        // Add the new semantic configuration to the existing index
-        if (existingIndex.semanticSearch && existingIndex.semanticSearch.configurations) {
-            existingIndex.semanticSearch.configurations.push(newSemanticConfiguration);
-        } else {
-            const configExists = existingIndex.semanticSearch?.configurations?.some(
-                config => config.name === semanticConfigurationName
-            );
-            if (!configExists) {
-                existingIndex.semanticSearch = {
-                    configurations: [newSemanticConfiguration]
-                };
-            }
-        }
-    
-        await indexClient.createOrUpdateIndex(existingIndex);
-    
-        const updatedIndex = await indexClient.getIndex(indexName);
-    
-        console.log(`Semantic configurations:`);
-        console.log("-".repeat(40));
-    
-        if (updatedIndex.semanticSearch && updatedIndex.semanticSearch.configurations) {
-            for (const config of updatedIndex.semanticSearch.configurations) {
-                console.log(`Configuration name: ${config.name}`);
-                console.log(`Title field: ${config.prioritizedFields.titleField?.name}`);
-                console.log(`Keywords fields: ${config.prioritizedFields.keywordsFields?.map(f => f.name).join(", ")}`);
-                console.log(`Content fields: ${config.prioritizedFields.contentFields?.map(f => f.name).join(", ")}`);
-                console.log("-".repeat(40));
-            }
-        } else {
-            console.log("No semantic configurations found.");
-        }
-    
-        console.log("Semantic configuration updated successfully.");
-    } catch (error) {
-        console.error("Error updating semantic configuration:", error);
-    }
-    ```
+The `updateIndexSettings.ts` file adds a semantic configuration to the existing `hotels-sample` index. This operation doesn't delete any search documents, and your index remains operational after the configuration is added. TypeScript type annotations ensure the configuration matches the expected schema.
 
-1. Run the code.
+```typescript
+import {
+    SearchIndexClient,
+    SemanticConfiguration,
+    SemanticPrioritizedFields,
+    SemanticField
+} from "@azure/search-documents";
+import {
+    searchEndpoint, indexName,
+    credential, semanticConfigurationName
+} from "./config.js";
+
+const indexClient = new SearchIndexClient(
+    searchEndpoint, credential
+);
+const existingIndex =
+    await indexClient.getIndex(indexName);
+
+const fields: SemanticPrioritizedFields = {
+    titleField: { name: "HotelName" },
+    keywordsFields: [
+        { name: "Tags" }
+    ] as SemanticField[],
+    contentFields: [
+        { name: "Description" }
+    ] as SemanticField[]
+};
+
+const newSemanticConfiguration:
+    SemanticConfiguration = {
+    name: semanticConfigurationName,
+    prioritizedFields: fields
+};
+
+if (existingIndex.semanticSearch
+    && existingIndex.semanticSearch.configurations) {
+    existingIndex.semanticSearch.configurations
+        .push(newSemanticConfiguration);
+} else {
+    existingIndex.semanticSearch = {
+        configurations: [newSemanticConfiguration]
+    };
+}
 
-    ```bash
-    npm run build && node -r dotenv/config dist/updateIndexSettings.js
-    ```
+await indexClient.createOrUpdateIndex(existingIndex);
+```
+
+Key takeaways:
+
++ TypeScript types like `SemanticPrioritizedFields`, `SemanticConfiguration`, and `SemanticField` provide compile-time validation for the configuration structure.
++ `titleField` sets the document title, `contentFields` sets the main content, and `keywordsFields` sets the keyword or tag fields.
++ `createOrUpdateIndex` pushes the updated schema to the search service without rebuilding the index or deleting documents.
 
-1. Output is the semantic configuration you just added, `Semantic configuration updated successfully.`.
+### Query the index
 
-## Run semantic queries
+The query scripts run three queries in sequence, progressing from a basic semantic search to semantic ranking with captions and answers.
 
-Once the `hotels-sample-index` index has a semantic configuration, you can run queries that include semantic parameters.
+#### Semantic query (no captions, no answers)
 
-1. Create a file in `./src` called `semanticQuery.ts` and copy in the following code to create a semantic query of the index. This is the minimum requirement for invoking semantic ranking.
+The `semanticQuery.ts` script shows the minimum requirement for invoking semantic ranking with type-safe results.
 
-    ```typescript
-    import { SearchClient } from "@azure/search-documents";
-    import { HotelDocument, credential, searchEndpoint, indexName, semanticConfigurationName } from "./config.js";
-    
-    const searchClient = new SearchClient<HotelDocument>(
-        searchEndpoint,
-        indexName,
-        credential
+```typescript
+import { SearchClient }
+    from "@azure/search-documents";
+import {
+    HotelDocument, credential,
+    searchEndpoint, indexName,
+    semanticConfigurationName
+} from "./config.js";
+
+const searchClient =
+    new SearchClient<HotelDocument>(
+        searchEndpoint, indexName, credential
     );
-    
-    const results = await searchClient.search("walking distance to live music", {
+
+const results = await searchClient.search(
+    "walking distance to live music",
+    {
         queryType: "semantic",
         semanticSearchOptions: {
-            configurationName: semanticConfigurationName
+            configurationName:
+                semanticConfigurationName
         },
-        select: ["HotelId", "HotelName", "Description"]
-    });
-    
-    let rowNumber = 1;
-    for await (const result of results.results) {
-    
-        // Log each result
-        const doc = result.document;
-        const score = result.score;
-        const rerankerScoreDisplay = result.rerankerScore;
-    
-        console.log(`Search result #${rowNumber++}:`);
-        console.log(`  Re-ranker Score: ${rerankerScoreDisplay}`);
-        console.log(`  HotelId: ${doc.HotelId}`);
-        console.log(`  HotelName: ${doc.HotelName}`);
-        console.log(`  Description: ${doc.Description || 'N/A'}\n`);
+        select: [
+            "HotelId", "HotelName", "Description"
+        ]
     }
-    ```
-
-1. Run the code.
-
-    ```bash
-    npm run build && node -r dotenv/config dist/semanticQuery.js
-    ```
+);
+```
 
-1. Output should consist of 13 documents, ordered by the `rerankerScoreDisplay`.
+Key takeaways:
 
-### Return captions
++ `SearchClient<HotelDocument>` provides type-safe access to document fields in results, with autocomplete for field names in `select` and `result.document`.
++ `queryType: "semantic"` enables semantic ranking on the query.
++ `semanticSearchOptions.configurationName` specifies which semantic configuration to use.
 
-Optionally, you can add captions to extract portions of the text and apply hit highlighting to the important terms and phrases. This query adds captions.
+#### Semantic query with captions
 
-1. Create a file in `./src` called `semanticQueryReturnCaptions.ts` and copy in the following code to add captions to the query. 
+The `semanticQueryReturnCaptions.ts` script adds captions to extract the most relevant passages from each result, with hit highlighting applied to the important terms and phrases.
 
-    ```typescript
-    import { SearchClient } from "@azure/search-documents";
-    import { HotelDocument, credential, searchEndpoint, indexName, semanticConfigurationName } from "./config.js";
-    
-    const searchClient = new SearchClient<HotelDocument>(
-        searchEndpoint,
-        indexName,
-        credential
-    );
-    
-    // Debug info
-    console.log(`Using semantic configuration: ${semanticConfigurationName}`);
-    console.log("Search query: walking distance to live music");
-    
-    const results = await searchClient.search("walking distance to live music", {
+```typescript
+const results = await searchClient.search(
+    "walking distance to live music",
+    {
         queryType: "semantic",
         semanticSearchOptions: {
-            configurationName: semanticConfigurationName,
+            configurationName:
+                semanticConfigurationName,
             captions: {
                 captionType: "extractive",
                 highlight: true
             }
         },
-        select: ["HotelId", "HotelName", "Description"],
-    });
-    
-    console.log(`Found ${results.count} results with semantic search\n`);
-    let rowNumber = 1;
-    
-    for await (const result of results.results) {
-        // Log each result
-        const doc = result.document;
-        const rerankerScoreDisplay = result.rerankerScore;
-    
-        console.log(`Search result #${rowNumber++}:`);
-        console.log(`  Re-ranker Score: ${rerankerScoreDisplay}`);
-        console.log(`  HotelName: ${doc.HotelName}`);
-        console.log(`  Description: ${doc.Description || 'N/A'}\n`);
-    
-        // Caption handling with better debugging
-        const captions = result.captions;
-        
-        if (captions && captions.length > 0) {
-            const caption = captions[0];
-            
-            if (caption.highlights) {
-                console.log(`  Caption with highlights: ${caption.highlights}`);
-            } else if (caption.text) {
-                console.log(`  Caption text: ${caption.text}`);
-            } else {
-                console.log(`  Caption exists but has no text or highlights content`);
-            }
-        } else {
-            console.log("  No captions found for this result");
+        select: [
+            "HotelId", "HotelName", "Description"
+        ]
+    }
+);
+
+for await (const result of results.results) {
+    const captions = result.captions;
+    if (captions && captions.length > 0) {
+        const caption = captions[0];
+        if (caption.highlights) {
+            console.log(
+                `Caption: ${caption.highlights}`
+            );
         }
-        console.log("-".repeat(60));
     }
-    ```
-
-1. Run the code.
-
-    ```bash
-    npm run build && node -r dotenv/config dist/semanticQueryReturnCaptions.js
-    ```
-
-1. Output should include a new caption element alongside search field. Captions are the most relevant passages in a result. If your index includes larger chunks of text, a caption is helpful for extracting the most interesting sentences.
-
-    ```console
-    Search result #1:
-      Re-ranker Score: 2.613231658935547
-      HotelName: Uptown Chic Hotel
-      Description: Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance.
-    
-      Caption with highlights: Chic hotel near the city. High-rise hotel in downtown, within walking distance to<em> theaters, </em>art galleries, restaurants and shops. Visit<em> Seattle Art Museum </em>by day, and then head over to<em> Benaroya Hall </em>to catch the evening's concert performance.
-    ```
+}
+```
 
-### Return semantic answers
+Key takeaways:
 
-In this final query, return semantic answers.
++ `captions.captionType: "extractive"` enables extractive captions from the content fields.
++ Captions surface the most relevant passages and add `<em>` tags around important terms.
 
-Semantic ranker can produce an answer to a query string that has the characteristics of a question. The generated answer is extracted verbatim from your content so it won't include composed content like what you might expect from a chat completion model. If the semantic answer isn't useful for your scenario, you can omit `semantic_answers` from your code.
+#### Semantic query with answers
 
-To produce a semantic answer, the question and answer must be closely aligned, and the model must find content that clearly answers the question. If potential answers fail to meet a confidence threshold, the model doesn't return an answer. For demonstration purposes, the question in this example is designed to get a response so that you can see the syntax.
+The `semanticAnswer.ts` script adds semantic answers. It uses a question as the search text because semantic answers work best when the query is phrased as a question. The answer is a verbatim passage extracted from your index, not a composed response from a chat completion model.
 
-1. Create a file in `./src` called `semanticAnswer.ts` and copy in the following code to get semantic answers. 
+The query and the indexed content must be closely aligned for an answer to be returned. If no candidate meets the confidence threshold, the response doesn't include an answer. This example uses a question that's known to produce a result so that you can see the syntax. If answers aren't useful for your scenario, omit `answers` from your code. For composed answers, consider a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
 
-    ```typescript
-    import { SearchClient } from "@azure/search-documents";
-    import { HotelDocument, credential, searchEndpoint, indexName, semanticConfigurationName } from "./config.js";
-    
-    const searchClient = new SearchClient<HotelDocument>(
-        searchEndpoint,
-        indexName,
-        credential
-    );
-    
-    const results = await searchClient.search("What's a good hotel for people who like to read", {
+```typescript
+const results = await searchClient.search(
+    "What's a good hotel for people who "
+    + "like to read",
+    {
         queryType: "semantic",
         semanticSearchOptions: {
-            configurationName: semanticConfigurationName,
+            configurationName:
+                semanticConfigurationName,
             captions: {
                 captionType: "extractive"
             },
             answers: {
                 answerType: "extractive"
             }
         },
-        select: ["HotelName", "Description", "Category"]
-    });
-    
-    console.log(`Answers:\n\n`);
-    let rowNumber = 1; 
-    
-    // Extract semantic answers from the search results
-    const semanticAnswers = results.answers;
-    for (const answer of semanticAnswers || []) {
-        console.log(`Semantic answer result #${rowNumber++}:`);
-        if (answer.highlights) {
-            console.log(`Semantic Answer: ${answer.highlights}`);
-        } else {
-            console.log(`Semantic Answer: ${answer.text}`);
-        }
-        console.log(`Semantic Answer Score: ${answer.score}\n\n`);
+        select: [
+            "HotelName", "Description", "Category"
+        ]
     }
-    
-    console.log(`Search Results:\n\n`);
-    rowNumber = 1;
-    
-    // Iterate through the search results
-    for await (const result of results.results) {
-    
-    
-        // Log each result
-        const doc = result.document;
-        const rerankerScoreDisplay = result.rerankerScore;
-        console.log(`Search result #${rowNumber++}:`);
-        console.log(`${rerankerScoreDisplay}`);
-        console.log(`${doc.HotelName}`);
-        console.log(`${doc.Description || 'N/A'}`);
-    
-        const captions = result.captions;
-    
-        if (captions && captions.length > 0) {
-            const caption = captions[0];
-            if (caption.highlights) {
-                console.log(`Caption: ${caption.highlights}\n`);
-            } else {
-                console.log(`Caption: ${caption.text}\n`);
-            }
-        }
+);
+
+const semanticAnswers = results.answers;
+for (const answer of semanticAnswers || []) {
+    if (answer.highlights) {
+        console.log(
+            `Semantic Answer: ${answer.highlights}`
+        );
+    } else {
+        console.log(
+            `Semantic Answer: ${answer.text}`
+        );
     }
-    ```
-
-1. Run the code.
-
-    ```bash
-    npm run build && node -r dotenv/config dist/semanticAnswer.js
-    ```
-
-1. Output should look similar to the following example, where the best answer to question is pulled from one of the results.
+    console.log(
+        `Semantic Answer Score: ${answer.score}`
+    );
+}
+```
 
-    Recall that answers are *verbatim content* pulled from your index and might be missing phrases that a user would expect to see. To get *composed answers* as generated by a chat completion model, considering using a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../agentic-retrieval-overview.md).
+Key takeaways:
 
-    ```console
-    Semantic answer result #1:
-    Semantic Answer: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
-    Semantic Answer Score: 0.9829999804496765
-    ```
++ `answers.answerType: "extractive"` enables extractive answers for question-like queries.
++ Answers are verbatim content extracted from your index, not generated text.
++ `results.answers` retrieves the answer objects separately from the search results.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScript用セマンティックランカーのクイックスタートガイドの更新"
}
```

### Explanation
この変更は、TypeScriptを使用したセマンティックランカーのクイックスタートガイドの更新を示しています。全体で758行が変更され、その内訳は361行の追加と397行の削除です。この更新の主な目的は、ユーザーがAzure AI Searchクライアントライブラリを用いてセマンティックランキングを既存の検索インデックスに追加し、インデックスをクエリするための手順をより明確かつ効果的に理解できるようにすることです。

変更点では、JavaScriptに対応したAzure AI Searchクライアントライブラリを利用する方法が詳述されており、クイックスタートを開始するための前提条件が追加されています。特に、Azureアカウント、Azure AI Searchサービス、また複数の依存関係に関する具体的な指示が加えられています。これにより、ユーザーは開発環境を迅速にセットアップでき、サンプルコードを効果的に実行することが可能になります。

また、新たにGitHubからのソースコードのダウンロード手順、Node.js、TypeScriptのインストール、そして環境変数の設定方法が詳しく説明されています。インデックスの更新やセマンティッククエリの実行に関連するスクリプトも具体的に示され、ユーザーがいかにしてセマンティック検索の機能を活用できるかを強調しています。

このように、更新されたガイドは、TypeScriptにおけるセマンティックランカーの利用を一層簡単にし、実用的な学習体験を提供することを目的としています。

## articles/search/includes/resource-authentication-semantic.md{#item-da8e67}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,23 @@
+---
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 03/02/2026
+# Use this file for the semantic ranking quickstart. For other scenarios, use resource-authentication.md.
+---
+
+Before you begin, make sure you have permissions to access content and operations in Azure AI Search. This quickstart uses Microsoft Entra ID for authentication and role-based access for authorization. You must be an **Owner** or **User Access Administrator** to assign roles. If roles aren't feasible, use [key-based authentication](../search-security-api-keys.md) instead.
+
+To configure the recommended role-based access:
+
+1. [Enable role-based access](../search-security-enable-roles.md) for your search service.
+
+1. [Assign the following roles](../search-security-rbac.md) to your user account.
+
+    + **Search Service Contributor**
+
+    + **Search Index Data Reader**
+
+> [!NOTE]
+> Unlike other quickstarts that create and load an index, this quickstart assumes an existing index that already contains data, so you don't need the **Search Index Data Contributor** role.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "セマンティックランキング用のリソース認証ガイドを追加"
}
```

### Explanation
この変更は、セマンティックランキングに関する新しいリソース認証ガイドファイルの追加を示しています。全体で23行のコードが追加され、削除はありません。このガイドは、Azure AI Searchにアクセスするための権限に関する重要な情報を提供します。

具体的には、このクイックスタートはMicrosoft Entra IDを使用して認証を行い、役割ベースのアクセス権を用いて認可します。ユーザーは、役割を割り当てるために「オーナー」または「ユーザーアクセス管理者」である必要があります。役割が適用できない場合は、代わりにAPIキーによる認証を使用するように指示されています。

推奨される役割ベースのアクセスを設定するための手順も含まれており、具体的には役割の有効化や、必要な役割（例：**Search Service Contributor**や**Search Index Data Reader**）のユーザーアカウントへの割り当てについて説明されています。また、他のクイックスタートと異なり、このガイドは既存のインデックスを前提としているため、**Search Index Data Contributor**の役割が不要であることを明確にしています。

この追加により、ユーザーはセマンティックランカーのクイックスタートに向けた準備をよりしやすくなり、Azure AI Searchを利用する際の認証とアクセス権の設定について一元的に理解できるようになります。

## articles/search/index-add-language-analyzers.md{#item-004ac0}

<details>
<summary>Diff</summary>
````diff
@@ -68,7 +68,7 @@ The following example illustrates a language analyzer specification in an index:
 
 ```json
 {
-  "name": "hotels-sample-index",
+  "name": "hotels-sample",
   "fields": [
     {
       "name": "Description",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスの言語アナライザー仕様の例を更新"
}
```

### Explanation
この変更は、インデックスにおける言語アナライザーの仕様の具体例を更新する内容です。変更内容は1行の追加と1行の削除であり、合計2行の変更が行われました。この修正は、より適切なサンプル名への変更を意図しています。

具体的には、言語アナライザーの仕様例の中で、インデックス名が「hotels-sample-index」から「hotels-sample」に変更されました。この変更は、インデックス名をより簡潔にすることで、サンプルが示す内容がわかりやすくなることを目的としています。

このマイナーアップデートにより、ユーザーは言語アナライザーの使用方法をより明確に理解できるようになり、適切なインデックス名の例が提供されることで、関連する設定の参考になります。

## articles/search/index-add-suggesters.md{#item-28ed57}

<details>
<summary>Diff</summary>
````diff
@@ -86,7 +86,7 @@ In the REST API, add suggesters by using [Create Index](/rest/api/searchservice/
 
   ```json
   {
-    "name": "hotels-sample-index",
+    "name": "hotels-sample",
     "fields": [
       . . .
           {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サジェスターのインデックス仕様の例を更新"
}
```

### Explanation
この変更は、サジェスターを追加する際のインデックス仕様例を更新する内容です。具体的には、1行の追加と1行の削除が行われ、合計で2行の変更が発生しました。

変更内容は、REST APIのサジェスター作成に関する例において、インデックス名が「hotels-sample-index」から「hotels-sample」に改名されたことです。この修正は、インデックス名をより簡潔で理解しやすいものにすることを目的としています。

このマイナーアップデートを通じて、ユーザーはサジェスターを実装するためのインデックス仕様の例をより明確に理解でき、適切な設定を行う際の参考として活用できるようになります。

## articles/search/index-similarity-and-scoring.md{#item-75603d}

<details>
<summary>Diff</summary>
````diff
@@ -155,7 +155,7 @@ This parameter is especially useful when you're trying to understand why certain
 For a query that targets a "description" field, a request might look like this:
 
 ```http
-POST {{baseUrl}}/indexes/hotels-sample-index/docs/search?api-version=2025-11-01-preview  HTTP/1.1
+POST {{baseUrl}}/indexes/hotels-sample/docs/search?api-version=2025-11-01-preview  HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer {{accessToken}}
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索リクエストのインデックス名を更新"
}
```

### Explanation
この変更は、検索リクエストの具体例におけるインデックス名を更新する内容です。1行の追加と1行の削除が行われ、合計で2行の変更が発生しました。

具体的には、HTTPリクエストの例において、インデックス名が「hotels-sample-index」から「hotels-sample」に変更されています。この修正は、より単純化されたインデックス名を用いることで、ユーザーがリクエストを理解しやすくすることを目的としています。

このマイナーアップデートにより、特定のフィールドをターゲットにした検索リクエストの構成が明確になり、実際の使用シナリオとしてより適切な実例が提供されるようになります。

## articles/search/media/search-create-app-portal/add-suggestions.png{#item-8e78d8}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "提案追加のスクリーンショットを追加"
}
```

### Explanation
この変更は、提案機能に関連する新しいスクリーンショットファイル（add-suggestions.png）が追加されたことを示しています。このファイルは、検索アプリケーションポータルにおける提案追加のプロセスを視覚的に説明するためのものであり、ユーザーがこの機能をより理解しやすくする助けとなります。

ファイルの変更履歴には、追加や削除は記録されていませんが、使用されるメディアコンテンツとして新たに追加されたことが重要です。このスクリーンショットにより、ユーザーは操作手順を視覚的に確認でき、実際のアプリケーションでの実装時に役立つリソースとなるでしょう。

## articles/search/media/search-create-app-portal/configure-results.png{#item-33a179}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "結果の設定に関するスクリーンショットを削除"
}
```

### Explanation
この変更は、結果の設定に関連するスクリーンショットファイル（configure-results.png）が削除されたことを示しています。このファイルは、検索アプリケーションポータルにおける結果の設定手順を視覚的に説明するためのものでしたが、現在はリポジトリから取り除かれました。

削除に伴うファイルの変更履歴には、新たな追加はありませんが、ユーザーがこの情報を参照することができなくなっているため、重要なコンテンツが失われたことになります。これにより、結果設定の手順を視覚的に理解する手段が減少し、ユーザーエクスペリエンスに影響を与える可能性があります。

## articles/search/media/search-create-app-portal/create-demo-app-action.png{#item-fc56b8}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "デモアプリの作成アクションに関するスクリーンショットを削除"
}
```

### Explanation
この変更は、デモアプリの作成アクションに関連するスクリーンショットファイル（create-demo-app-action.png）が削除されたことを示しています。このファイルは、検索アプリケーションポータル内でデモアプリを作成する手順を視覚的に示すために役立っていましたが、現在はリポジトリから取り除かれています。

このファイルの削除により、ユーザーはデモアプリの作成手順を視覚的に確認することができなくなり、関連する情報が不足することになります。これにより、特に初めて手順を実行するユーザーにとって、アプリケーションの作成プロセスがより難しくなる可能性があります。

## articles/search/media/search-create-app-portal/customize-results.png{#item-fb3041}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "結果のカスタマイズに関するスクリーンショットを追加"
}
```

### Explanation
この変更は、結果のカスタマイズに関連する新しいスクリーンショットファイル（customize-results.png）が追加されたことを示しています。このファイルは、検索アプリケーションポータルにおける結果のカスタマイズ手順を視覚的に示すためのもので、ユーザーがカスタマイズのプロセスをより理解しやすくすることを目的としています。

新しいスクリーンショットの追加により、ユーザーは結果設定の具体的な手順を視覚的に確認できるようになり、アプリケーションの利用が向上することが期待されます。これは、特に視覚的な情報を好むユーザーにとって、より良い体験を提供するものとなります。

## articles/search/media/search-create-app-portal/customize-sidebar.png{#item-445361}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "サイドバーのカスタマイズに関するスクリーンショットを追加"
}
```

### Explanation
この変更は、サイドバーのカスタマイズに関連する新しいスクリーンショットファイル（customize-sidebar.png）が追加されたことを示しています。このファイルは、検索アプリケーションポータルにおけるサイドバーのカスタマイズ手順を視覚的に示すためのもので、ユーザーがインターフェースの調整方法をよりよく理解できるように設計されています。

新たに追加されたスクリーンショットにより、ユーザーはサイドバーの設定プロセスを視覚的に確認でき、実際の操作をよりスムーズに行うことが可能になります。これにより、ユーザー体験が向上し、特に視覚的な支援を求めるユーザーにとって役立つリソースとなります。

## articles/search/media/search-create-app-portal/delete-filters.png{#item-c9f3bb}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "フィルター削除に関するスクリーンショットを削除"
}
```

### Explanation
この変更は、フィルターの削除に関連するスクリーンショットファイル（delete-filters.png）が削除されたことを示しています。このファイルは、検索アプリケーションポータルにおけるフィルター削除の手順を視覚的に説明するために使用されていましたが、今回の変更で削除されることになりました。

フィルター削除に関する情報がビジュアル的に提供されなくなったため、ユーザーはフィルター設定や削除の手順についての理解を深めるために別のリソースを探さなければならなくなります。これにより、特に視覚的なガイダンスを必要とするユーザーに対しては、利用の手間が増える可能性があります。

## articles/search/media/search-create-app-portal/enable-cors-continue.png{#item-b62d62}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "CORSを有効にする手順に関するスクリーンショットを追加"
}
```

### Explanation
この変更は、CORS（Cross-Origin Resource Sharing）を有効にする手順を示す新しいスクリーンショットファイル（enable-cors-continue.png）が追加されたことを示しています。このファイルは、検索アプリケーションポータルにおけるCORS設定を視覚的に説明するためのもので、ユーザーにとって操作の理解を助ける目的で提供されています。

新しく追加されたスクリーンショットは、ユーザーにCORSを正しく設定する方法を具体的に示し、実際の手順をより明確に理解できるようにしています。このビジュアルリソースにより、特に技術的な詳細が必要なユーザーにとって、CORSの設定が容易になり、全体的なユーザー体験の向上が期待されます。

## articles/search/media/search-get-started-portal/connect-to-your-data.png{#item-4eb5d4}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ接続に関するスクリーンショットの修正"
}
```

### Explanation
この変更は、データ接続に関連するスクリーンショットファイル（connect-to-your-data.png）が修正されたことを示しています。このファイルは、ユーザーがデータに接続する手順を視覚的に説明するために使用されています。

修正内容の詳細な情報は提供されていませんが、通常、この種の更新は画像の品質向上、説明の明確化、または最新のインターフェースに対応するための調整を目的としています。更新されたスクリーンショットにより、ユーザーはデータ接続の手順をより理解しやすくなり、効果的に操作を行うことができるようになるでしょう。これにより、ユーザー体験の向上が図られます。

## articles/search/media/search-get-started-portal/index-schema-definition.png{#item-152d3e}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックススキーマ定義に関するスクリーンショットの修正"
}
```

### Explanation
この変更は、インデックススキーマ定義に関連するスクリーンショットファイル（index-schema-definition.png）が修正されたことを示しています。この画像は、ユーザーがインデックススキーマを理解し、設定する手順を視覚的にサポートするために使用されています。

具体的な変更点についての詳細は提供されていませんが、一般的にこのような修正は、画像の情報を最新の仕様に合わせるためのアップデートや、視認性の向上を目的とした品質改善を含むことがあります。この修正により、ユーザーはインデックススキーマの設定に関する理解を深め、実行する際の成功率を高めることが期待されます。全体として、ユーザーの利便性と体験の向上に寄与する変更となっています。

## articles/search/media/search-get-started-portal/indexers-status.png{#item-f09549}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーのステータスに関するスクリーンショットの修正"
}
```

### Explanation
この変更は、インデクサーのステータスに関するスクリーンショットファイル（indexers-status.png）が修正されたことを示しています。この画像は、ユーザーがインデクサーの状態を視覚的に把握し、確認する際に役立つ情報を提供します。

具体的な変更内容は記載されていませんが、一般的には画像の更新は、最新のインターフェース、機能改善、または視認性の向上を目的としています。この修正により、ユーザーはインデクサーの状況をより正確に理解し、トラブルシューティングや設定の最適化を行えるようになるでしょう。全体的に見て、ユーザー体験を向上させることに寄与する重要な更新となっています。

## articles/search/media/search-get-started-portal/indexes-list.png{#item-bb803f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスのリストに関するスクリーンショットの修正"
}
```

### Explanation
この変更は、インデックスのリストに関連するスクリーンショットファイル（indexes-list.png）が修正されたことを示しています。この画像は、ユーザーがインデックスの管理や選択を行う際に必要な情報を視覚的に提供する役割を担っています。

具体的な変更内容については記載されていませんが、通常、このような画像の修正は、最新のユーザーインターフェースを反映させたり、機能の改善を示したりするために行われます。ユーザーは更新された画像を通じて、インデックスの状態や設定に関してより良い理解を得られるようになります。全体として、ユーザー体験の向上を目指した重要な更新と考えられます。

## articles/search/media/search-get-started-portal/review-and-create.png{#item-9dea50}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レビューと作成に関するスクリーンショットの修正"
}
```

### Explanation
この変更は、レビューと作成に関連するスクリーンショットファイル（review-and-create.png）が修正されたことを示しています。この画像は、ユーザーが設定や入力内容を確認し、最終的な作成手続きを行う際に役立つ視覚情報を提供します。

具体的な変更内容については詳細がありませんが、通常、このような画像の更新は、インターフェースの変更や機能向上を反映するものです。ユーザーは新しい画像を通じて、レビューおよび作成のプロセスをより円滑に進められることが期待されます。この修正は、全体的なユーザー体験の向上に貢献する重要なアップデートと考えられます。

## articles/search/media/search-get-started-portal/search-explorer-change-view.png{#item-65fbc6}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索エクスプローラーのビュー変更に関するスクリーンショットの修正"
}
```

### Explanation
この変更は、検索エクスプローラーのビュー変更に関連するスクリーンショットファイル（search-explorer-change-view.png）が修正されたことを示しています。この画像は、ユーザーが検索エクスプローラーの異なる表示モードを使用する際に必要な視覚的ガイダンスを提供します。

具体的な変更内容に関する情報はありませんが、こうした画像の更新は、ユーザーインターフェースの改善や機能の進化を反映すると予想されます。ユーザーは新たに更新された画像を参照することで、より効果的に検索エクスプローラーを活用できるようになります。この修正は、全体的な操作性の向上を助けるものと考えられます。

## articles/search/media/search-get-started-portal/search-explorer-query-results.png{#item-6aa0cb}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索エクスプローラーのクエリ結果に関するスクリーンショットの修正"
}
```

### Explanation
この変更は、検索エクスプローラーのクエリ結果に関連するスクリーンショットファイル（search-explorer-query-results.png）が修正されたことを示しています。この画像は、ユーザーが検索クエリの結果をどのように確認し、分析するかを視覚的に示すための重要なリソースです。

具体的に何が変更されたかの詳細は提供されていませんが、一般的にこの種の画像の修正は、ユーザーインターフェースの更新や機能強化を反映している可能性があります。新しいスクリーンショットを通じて、ユーザーは検索結果の解釈や利用がより容易になることが期待されます。この修正は、ユーザー体験の向上に寄与すると考えられます。

## articles/search/media/search-get-started-portal/search-explorer-query-string.png{#item-ce0c3c}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索エクスプローラーのクエリ文字列に関するスクリーンショットの修正"
}
```

### Explanation
この変更は、検索エクスプローラーのクエリ文字列に関連するスクリーンショットファイル（search-explorer-query-string.png）が修正されたことを示しています。この画像は、ユーザーがどのようにクエリを構成し、検索エクスプローラーに入力するかを示す重要な視覚ガイドです。

具体的な変更内容については詳細がありませんが、通常、この種の画像の更新は、新しい機能の追加やユーザーインターフェースの改善を反映している可能性があります。更新されたスクリーンショットは、ユーザーにとってクエリ入力の手順をより明確にし、検索エクスプローラーを効果的に活用できるようサポートすることを目的としています。この修正により、ユーザー体験が向上することが期待されます。

## articles/search/media/search-get-started-semantic/default-semantic-configuration.png{#item-0aa386}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "デフォルトのセマンティック構成に関する新しいスクリーンショットの追加"
}
```

### Explanation
この変更は、デフォルトのセマンティック構成を示す新しいスクリーンショットファイル（default-semantic-configuration.png）が追加されたことを示しています。この画像は、ユーザーがセマンティック検索の設定方法を理解する手助けとなるべく、視覚的なガイドラインを提供します。

新しいスクリーンショットは、特にセマンティック検索機能に関連する設定や構成のデフォルトオプションを示すことを目的としており、ユーザーは手順を視覚的に確認できるようになります。この追加により、製品ドキュメントがより充実し、利用者が新機能を容易に習得できることが期待されます。全体的に、この変更はユーザー体験の向上に寄与するものです。

## articles/search/media/search-get-started-semantic/no-semantic-configuration.png{#item-be001a}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "セマンティック構成なしのスクリーンショットの削除"
}
```

### Explanation
この変更は、「セマンティック構成なし」を示すスクリーンショットファイル（no-semantic-configuration.png）が削除されたことを示しています。この画像は、セマンティック検索の機能を利用しない場合の設定を示すものでした。

この削除により、利用者がセマンティック検索に関する情報を参照する際に、以前の設定方法や流れを確認する手段が失われることになります。ドキュメントから旧情報を削除することは、情報の整理や更新の一環として行われることがありますが、利用者には新しいバージョンの機能に注目し、既存の情報と混同しないようにするメリットもあります。しかし、一方で、セマンティック検索機能を利用しないユーザーにとっては、役立つ情報が消失したことになります。したがって、この変更は重要な影響を与える可能性があるため、十分な注意が必要です。

## articles/search/media/search-get-started-semantic/search-explorer-simple-query.png{#item-df72be}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "シンプルクエリの検索エクスプローラーのスクリーンショットの削除"
}
```

### Explanation
この変更は、シンプルクエリに関する検索エクスプローラーのスクリーンショットファイル（search-explorer-simple-query.png）が削除されたことを示しています。この画像は、ユーザーがシンプルな検索クエリを利用する際のインターフェースを視覚的に説明するために使用されていました。

この削除により、特にこの機能を利用しようとしているユーザーにとって、過去の利用方法や手順を参照するための貴重な情報が失われました。ドキュメントの整備の一環として古い情報を削除することは行われることがありますが、利用者が必要とする情報が消失することで、混乱や不便を引き起こす可能性があります。

したがって、この変更は利用者への影響が大きく、特に新機能の学習に必要な情報を求めるユーザーにとっては重要な注意点となるでしょう。このようなスクリーンショットは、特定の機能の理解を深めるための手助けをしているため、今後のドキュメントづくりにおいては、適切なビジュアルリソースの提供が求められます。

## articles/search/query-lucene-syntax.md{#item-736436}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ To use full Lucene syntax, set the queryType to `full` and pass in a query expre
 The following example is a search request constructed using the full syntax. This particular example shows in-field search and term boosting. It looks for hotels where the category field contains the term `budget`. Any documents containing the phrase `"recently renovated"` are ranked higher as a result of the term boost value (3).  
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST /indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
   "queryType": "full",
   "search": "category:budget AND \"recently renovated\"^3",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索リクエストのインデックス名の修正"
}
```

### Explanation
この変更は、Lucene構文を使用した検索リクエストの例において、インデックス名を修正したことを示しています。具体的には、`hotels-sample-index`というインデックス名が`hotels-sample`に変更されました。

このような修正は、ユーザーが実際のリクエストを利用する際に、一貫性や正確性を保つために重要です。特に、インデックス名の整合性は、ドキュメントを実際のシステムで使用する際に、誤解を避けるために欠かせません。

この修正は、1行の削除と1行の追加から成り、全体としては2つの変更を伴っています。変更により、ユーザーは新しいインデックス名を使用した正確なリクエストを参照できるようになります。このような小規模な更新でも、利用者が正しい情報に基づいて作業を行う上での重要な一歩となります。

## articles/search/search-create-app-portal.md{#item-19ab44}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 02/27/2026
+ms.date: 03/05/2026
 ms.update-cycle: 180-days
 ms.custom:
   - mode-ui
@@ -32,32 +32,36 @@ A demo app can help you visualize how an index functions in a client app, but it
 
 The **Create demo app** wizard is available for existing indexes. Choose an index that includes retrievable, filterable, and facetable fields.
 
+To start the wizard:
+
 1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
 
 1. From the left pane, select **Search management** > **Indexes**.
 
-1. Select **hotels-sample-index** from the list.
+1. Select **hotels-sample** from the list.
 
 1. At the top of the index page, select **Create demo app**.
 
 1. Select **Enable CORS and continue** to add CORS support to your index definition.
 
-:::image type="content" source="media/search-create-app-portal/create-demo-app-action.png" alt-text="Screenshot of the Create Demo App action.":::
+    :::image type="content" source="media/search-create-app-portal/enable-cors-continue.png" alt-text="Screenshot of the button for enabling CORS and continuing." lightbox="media/search-create-app-portal/enable-cors-continue.png":::
 
 ## Configure search results
 
 You can configure a basic layout for the rendered search results, including space for a thumbnail image, title, and description. Each element is backed by a field in your index that provides the necessary data.
 
 To configure the search results:
 
-1. Skip **Thumbnail** because the hotels-sample-index doesn't have image URLs. If your index contains a field populated with URLs that resolve to publicly available images, you should specify that field for the thumbnail.
+1. Skip **Thumbnail** because the hotels-sample index doesn't have image URLs. If your index contains a field populated with URLs that resolve to publicly available images, you should specify that field for the thumbnail.
 
 1. For **Title**, choose a field that conveys the uniqueness of each document. Our example uses **HotelName**.
 
 1. For **Description**, choose a field that might help someone decide whether to drill down to that particular document. Our example uses **Description**.
 
 1. Select **Next**.
 
+    :::image type="content" source="media/search-create-app-portal/customize-results.png" alt-text="Screenshot of the page for customizing individual results." lightbox="media/search-create-app-portal/customize-results.png":::
+
 ## Add a sidebar
 
 The search service supports filters and faceted navigation, which is often rendered as a sidebar. Facets are based on fields attributed as filterable and facetable in your index schema.
@@ -75,7 +79,7 @@ To customize the sidebar:
 
 1. Select **Next**.
 
-:::image type="content" source="media/search-create-app-portal/delete-filters.png" alt-text="Screenshot of the filters page and the delete option.":::
+    :::image type="content" source="media/search-create-app-portal/customize-sidebar.png" alt-text="Screenshot of the page for customizing the sidebar." lightbox="media/search-create-app-portal/customize-sidebar.png":::
 
 ## Add suggestions
 
@@ -87,7 +91,7 @@ To customize the suggestions:
 
 1. Use the **Show Field Name** checkbox to include or exclude labels for the suggestions.
 
-    :::image type="content" source="media/search-create-app-portal/suggestions.png" lightbox="media/search-create-app-portal/suggestions.png" alt-text="Screenshot of the suggestion configuration page.":::
+    :::image type="content" source="media/search-create-app-portal/add-suggestions.png" lightbox="media/search-create-app-portal/add-suggestions.png" alt-text="Screenshot of the page for adding suggestions.":::
 
 ## Create, download, and execute
 
@@ -107,7 +111,7 @@ To finish the wizard and use the demo app:
 
 1. Test suggestions by typing in part of a search term. If you don't see suggested results, check your browser settings or try a different browser. Notice that suggested results are different from autocompletion of a search term. The demo app supports suggested results only.
 
-   :::image type="content" source="media/search-create-app-portal/app-suggestions.png" alt-text="Screenshot of suggested results.":::
+   :::image type="content" source="media/search-create-app-portal/app-suggestions.png" alt-text="Screenshot of suggested results." lightbox="media/search-create-app-portal/app-suggestions.png":::
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デモアプリウィザードの改善とスクリーンショットの更新"
}
```

### Explanation
この変更は、デモアプリウィザードに関する文書（search-create-app-portal.md）が更新されたことを示しています。具体的には、いくつかの手順が追加され、いくつかのスクリーンショットが新しい内容に置き換えられました。

主な変更点は以下の通りです：
- ウィザードの開始手順に、Azureポータルにサインインして検索サービスを選択する手順が追加されました。
- インデックス名が`hotels-sample-index`から`hotels-sample`に変更され、情報の整合性が保たれるように更新されました。
- CORSの有効化ボタンのスクリーンショットが新しいものに置き換えられ、より正確な情報を提供しています。

さらに、検索結果のカスタマイズやサイドバーの追加に関する手順においても、関連するスクリーンショットが更新され、ユーザーが具体的な操作を理解しやすくなっています。

これらの変更は、全体で11行の追加と7行の削除を含み、18の変更が加えられています。これにより、ユーザーはデモアプリを作成する際のプロセスをより明確に理解できるようになります。特に、視覚的な要素の増加は、ユーザー支援に対する重要な改善です。

## articles/search/search-faceted-navigation-examples.md{#item-2b1158}

<details>
<summary>Diff</summary>
````diff
@@ -44,12 +44,12 @@ Interval facets on date time are computed based on the UTC time if `timeoffset`
 
 ## Basic facet example
 
-The following facet queries work against the [hotels sample index](search-get-started-portal.md). You can use **JSON view** in Search Explorer to paste in the JSON query. For help with getting started, see [Add faceted navigation to search results](search-faceted-navigation.md).
+The following facet queries work against the [hotels-sample index](search-get-started-portal.md). You can use **JSON view** in Search Explorer to paste in the JSON query. For help with getting started, see [Add faceted navigation to search results](search-faceted-navigation.md).
 
 This first query retrieves facets for Categories, Ratings, Tags, and rooms with baseRate values in specific ranges. Notice the last facet is on a subfield of the Rooms collection. Facets count the parent document (Hotels) and not intermediate subdocuments (Rooms), so the response determines the number of *hotels* that have any rooms in each pricing category.
 
-```rest
-POST /indexes/hotels-sample-index/docs/search?api-version={{api_version}}
+```http
+POST /indexes/hotels-sample/docs/search?api-version={{api_version}}
 {  
   "search": "ocean view",  
   "facets": [ "Category", "Rating", "Tags", "Rooms/BaseRate,values:80|150|220" ],
@@ -59,8 +59,8 @@ POST /indexes/hotels-sample-index/docs/search?api-version={{api_version}}
 
 This second example uses a filter to narrow down the previous faceted query result after the user selects Rating 3 and category "Motel".
 
-```rest
-POST /indexes/hotels-sample-index/docs/search?api-version={{api_version}}
+```http
+POST /indexes/hotels-sample/docs/search?api-version={{api_version}}
 {  
   "search": "water view",  
   "facets": [ "Tags", "Rooms/BaseRate,values:80|150|220" ],
@@ -71,8 +71,8 @@ POST /indexes/hotels-sample-index/docs/search?api-version={{api_version}}
 
 The third example sets an upper limit on unique terms returned in a query. The default is 10, but you can increase or decrease this value using the count parameter on the facet attribute. This example returns facets for city, limited to 5.
 
-```rest
-POST /indexes/hotels-sample-index/docs/search?api-version={{api_version}}
+```http
+POST /indexes/hotels-sample/docs/search?api-version={{api_version}}
 {  
   "search": "view",  
   "facets": [ "Address/City,count:5" ],
@@ -83,7 +83,7 @@ POST /indexes/hotels-sample-index/docs/search?api-version={{api_version}}
 This example shows three facets for "Category", "Tags", and "Rating", with a count override on "Tags" and a range override for "Rating", which is otherwise stored as a double in the index.
 
 ```http
-POST https://{{service_name}}.search.windows.net/indexes/hotels/docs/search?api-version={{api_version}}
+POST https://{{service_name}}.search.windows.net/indexes/hotels-sample/docs/search?api-version={{api_version}}
 {
     "search": "*",
     "facets": [ 
@@ -105,10 +105,10 @@ Each range is built using 0 as a starting point, a value from the list as an end
 
 You can formulate a query that returns a distinct value count for each facetable field. This example formulates an empty or unqualified query (`"search": "*"`) that matches on all documents, but by setting `top` to zero, you get just the counts, with no results.
 
-For brevity, this query includes just two fields marked as `facetable` in the hotels sample index.
+For brevity, this query includes just two fields marked as `facetable` in the hotels-sample index.
 
 ```http
-POST https://{{service_name}}.search.windows.net/indexes/hotels/docs/search?api-version={{api_version}}
+POST https://{{service_name}}.search.windows.net/indexes/hotels-sample/docs/search?api-version={{api_version}}
 {
     "search": "*",
     "count": true,
@@ -220,8 +220,8 @@ Notice that parentheses are processed before nesting and append operations: `A >
 
 There are several examples for facet hierarchies. The first example is a query that returns just a few documents, which is helpful for viewing a full response. Facets count the parent document (Hotels) and not intermediate subdocuments (Rooms), so the response determines the number of *hotels* that have any rooms in each facet bucket.
 
-```rest
-POST /indexes/hotels-sample-index/docs/search?api-version=2025-11-01-Preview
+```http
+POST /indexes/hotels-sample/docs/search?api-version=2025-11-01-Preview
 {
   "search": "ocean",  
   "facets": ["Address/StateProvince>Address/City", "Tags>Rooms/BaseRate,values:50"],
@@ -380,8 +380,8 @@ Results from this query are as follows. Both hotels have pools. For other tags,
 
 This second example extends the previous one, demonstrating multiple top-level facets with multiple children. Notice the semicolon (`;`) operator separates each child.
 
-```rest
-POST /indexes/hotels-sample-index/docs/search?api-version=2025-11-01-Preview
+```http
+POST /indexes/hotels-sample/docs/search?api-version=2025-11-01-Preview
 {  
   "search": "+ocean",  
   "facets": ["Address/StateProvince > Address/City", "Tags > (Rooms/BaseRate,values:50 ; Rooms/Type)"],
@@ -390,7 +390,7 @@ POST /indexes/hotels-sample-index/docs/search?api-version=2025-11-01-Preview
 }  
 ```
 
-A partial response, trimmed for brevity, shows Tags with child facets for the rooms base rate and type. In the hotels sample index, both hotels that match to `+ocean` have rooms in each type and a pool.
+A partial response, trimmed for brevity, shows Tags with child facets for the rooms base rate and type. In the hotels-sample index, both hotels that match to `+ocean` have rooms in each type and a pool.
 
 ```json
 {
@@ -507,7 +507,7 @@ The following example shows how to escape special characters in your regular exp
 Here's an example of a facet filter that matches on Budget and Extended-Stay hotels, with Rating as a child of each hotel category.
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2025-11-01-Preview
+POST /indexes/hotels-sample/docs/search?api-version=2025-11-01-Preview
 { 
     "search": "*", 
     "facets": ["(Category,includeTermFilter:/(Budget|Extended-Stay)/)>Rating,values:1|2|3|4|5"],
@@ -627,10 +627,10 @@ Faceting is performed in memory. Increasing `precisionThreshold` results in more
 
 You can sum any facetable field of a numeric data type (except vectors and geographic coordinates). 
 
-Here's an example using the hotels-sample-index. The Rooms/SleepsCount field is facetable and numeric, so we choose this field to demonstrate sum. If we sum that field, we get the sleep count for the entire hotel. Recall that facets count the parent document (Hotels) and not intermediate subdocuments (Rooms), so the response sums the SleepsCount of all rooms for the entire hotel. In this query, we add a filter to sum the SleepsCount for just one hotel.
+Here's an example using the hotels-sample index. The Rooms/SleepsCount field is facetable and numeric, so we choose this field to demonstrate sum. If we sum that field, we get the sleep count for the entire hotel. Recall that facets count the parent document (Hotels) and not intermediate subdocuments (Rooms), so the response sums the SleepsCount of all rooms for the entire hotel. In this query, we add a filter to sum the SleepsCount for just one hotel.
 
-```rest
-POST /indexes/hotels-sample-index/docs/search?api-version=2025-11-01-Preview
+```http
+POST /indexes/hotels-sample/docs/search?api-version=2025-11-01-Preview
 
 { 
       "search": "*",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファセットナビゲーションのサンプルでのインデックス名の修正"
}
```

### Explanation
この変更は、ファセットナビゲーションの例に関する文書（search-faceted-navigation-examples.md）が修正されたことを示しています。具体的には、サンプルインデックス名が`hotels-sample-index`から`hotels-sample`に一貫して修正されました。

主な変更点は以下の通りです：
- ドキュメント内のサンプルリクエストのインデックス名が、旧名から新名に変更されました。これにより、ユーザーが実際のコーディングの際に正しいインデックス名を使用できるようになります。
- 各サンプルリクエストが、最新のインデックス名を使用するように調整されています。また、HTTPリクエストの形式も統一されています。

これらの変更は、追加と削除がそれぞれ19行ずつあり、合計で38の変更点を含みます。これにより、ドキュメントの整合性が向上し、ユーザーがファセットナビゲーションを効果的に活用するための明確なガイドが提供されます。この更新は、ファセットナビゲーション機能の理解を深めるために重要です。

## articles/search/search-faceted-navigation.md{#item-f29d1e}

<details>
<summary>Diff</summary>
````diff
@@ -42,7 +42,7 @@ Facets are enabled on supported fields in an index, and then specified on a quer
 The following REST example is an empty query (`"search": "*"`) that is scoped to the entire index (see the [built-in hotels sample](search-get-started-portal.md)). The `facets` parameter specifies the "Category" field.
 
 ```http
-POST https://{{service_name}}.search.windows.net/indexes/hotels/docs/search?api-version={{api_version}}
+POST https://{{service_name}}.search.windows.net/indexes/hotels-sample/docs/search?api-version={{api_version}}
 {
     "search": "*",
     "queryType": "simple",
@@ -59,7 +59,7 @@ The response for the example starts with the faceted navigation structure. The s
 
 ```json
 {
-    "@odata.context": "https://demo-search-svc.search.windows.net/indexes('hotels')/$metadata#docs(*)",
+    "@odata.context": "https://demo-search-svc.search.windows.net/indexes('hotels-sample')/$metadata#docs(*)",
     "@odata.count": 50,
     "@search.facets": {
         "Category": [
@@ -154,11 +154,11 @@ When you define an index schema, facets are enabled when you set `"facetable": t
 
 Start with [Create or Update Index](search-how-to-create-search-index.md) request and specify the fields collection.
 
-  Here's a JSON example of the hotels sample index, showing "facetable" and "filterable" on low cardinality fields that contain single values or short phrases: "Category", "Tags", "Rating".
+  Here's a JSON example of the hotels-sample index, showing "facetable" and "filterable" on low cardinality fields that contain single values or short phrases: "Category", "Tags", "Rating".
 
   ```json
   {
-    "name": "hotels",  
+    "name": "hotels-sample",  
     "fields": [
       { "name": "hotelId", "type": "Edm.String", "key": true, "searchable": false, "sortable": false, "facetable": false },
       { "name": "Description", "type": "Edm.String", "filterable": false, "sortable": false, "facetable": false },
@@ -205,7 +205,7 @@ Use JSON view in Search Explorer to set facet parameters in the [Azure portal](h
 1. Provide a query in JSON. You can type it out, copy the JSON from a REST example, or use intellisense to help with syntax. Refer to the REST example in the next tab for reference on facet expressions.
 1. Select **Search** to return faceted results, articulated in JSON.
 
-Here's a screenshot of the [basic facet query example](search-faceted-navigation-examples.md#basic-facet-example) on the [hotels sample index](search-get-started-portal.md). You can paste in other examples in this article to return the results in Search Explorer.
+Here's a screenshot of the [basic facet query example](search-faceted-navigation-examples.md#basic-facet-example) on the [hotels-sample index](search-get-started-portal.md). You can paste in other examples in this article to return the results in Search Explorer.
 
 :::image type="content" source="media/search-faceted-navigation/portal-facet-query.png" alt-text="Screenshot of the Search Explorer page in the Azure portal." border="true" lightbox="media/search-faceted-navigation/portal-facet-query.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス名の修正とファセットに関する情報の更新"
}
```

### Explanation
この変更は、ファセットナビゲーションに関する文書（search-faceted-navigation.md）が修正されたことを示しています。主な修正は、サンプルインデックスの名前が`hotels`から`hotels-sample`に変更されたことです。

具体的な変更点は以下の通りです：
- REST APIのサンプルリクエストにおいて、インデックス名が`hotels`から`hotels-sample`に変更され、送信先のURLが最新のデモ用インデックスに合わせて更新されました。
- JSONレスポンスの`@odata.context`も同様に、インデックス名が更新されることで関連情報が正確に反映されています。
- インデックススキーマの定義に関連する説明でも、同じようにインデックス名が修正され、整合性が保たれました。
- 基本ファセットクエリの例に関するスクリーンショットも、最新のインデックス名に符合するように更新されています。

この変更は追加と削除がそれぞれ5行ずつあり、合計で10の変更が加えられています。これにより、ドキュメント全体の一貫性が向上し、ユーザーがファセットナビゲーションを利用する際に正確な情報にアクセスできるようになりました。

## articles/search/search-get-started-agentic-retrieval.md{#item-4a40f4}

<details>
<summary>Diff</summary>
````diff
@@ -9,34 +9,34 @@ ms.topic: quickstart
 ms.date: 02/23/2026
 ms.custom: dev-focus
 ai-usage: ai-assisted
-zone_pivot_groups: search-get-started-agentic-retrieval
+zone_pivot_groups: search-sdks-rest
 # Customer intent: I want to learn how to use agentic retrieval to create a knowledge base that processes multi-turn conversations. The knowledge base should retrieve relevant information from a knowledge source that points to an Azure AI Search index and use an Azure OpenAI LLM to synthesize answers.
 ---
 
 # Quickstart: Agentic retrieval
 
-::: zone pivot="programming-language-csharp"
-[!INCLUDE [C# quickstart](includes/quickstarts/agentic-retrieval-csharp.md)]
+::: zone pivot="csharp"
+[!INCLUDE [C#](includes/quickstarts/agentic-retrieval-csharp.md)]
 ::: zone-end
 
-::: zone pivot="programming-language-java"
-[!INCLUDE [Java quickstart](includes/quickstarts/agentic-retrieval-java.md)]
+::: zone pivot="java"
+[!INCLUDE [Java](includes/quickstarts/agentic-retrieval-java.md)]
 ::: zone-end
 
-::: zone pivot="programming-language-javascript"
-[!INCLUDE [JavaScript quickstart](includes/quickstarts/agentic-retrieval-javascript.md)]
+::: zone pivot="javascript"
+[!INCLUDE [JavaScript](includes/quickstarts/agentic-retrieval-javascript.md)]
 ::: zone-end
 
-::: zone pivot="programming-language-python"
-[!INCLUDE [Python quickstart](includes/quickstarts/agentic-retrieval-python.md)]
+::: zone pivot="python"
+[!INCLUDE [Python](includes/quickstarts/agentic-retrieval-python.md)]
 ::: zone-end
 
-::: zone pivot="programming-language-typescript"
-[!INCLUDE [TypeScript quickstart](includes/quickstarts/agentic-retrieval-typescript.md)]
+::: zone pivot="typescript"
+[!INCLUDE [TypeScript](includes/quickstarts/agentic-retrieval-typescript.md)]
 ::: zone-end
 
-::: zone pivot="programming-language-rest"
-[!INCLUDE [REST quickstart](includes/quickstarts/agentic-retrieval-rest.md)]
+::: zone pivot="rest"
+[!INCLUDE [REST](includes/quickstarts/agentic-retrieval-rest.md)]
 ::: zone-end
 
 ## Related content
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルのクイックスタートドキュメントの改善"
}
```

### Explanation
この変更は、「エージェントリトリーバルのクイックスタート」に関する文書（search-get-started-agentic-retrieval.md）が修正されたことを示しています。主に、プログラミング言語に関連するゾーンのピボット名が一貫した形式に統一されました。

具体的な変更点は以下の通りです：
- ゾーンのピボット名が、`programming-language-csharp`などから`csharp`のように簡略化され、より明確な表記に変更されました。
- 各プログラミング言語（C#, Java, JavaScript, Python, TypeScript, REST）に関するリンクの記述も更新され、統一感が出るように改善されました。
- これにより、文書全体の可読性が向上し、ユーザーが必要な情報を簡単に見つけやすくなっています。

この変更は、追加と削除がそれぞれ13行ずつあり、合計で26の変更が加えられています。これにより、エージェントリトリーバル機能の使い方を学ぼうとするユーザーにとって、よりスムーズでの理解を促進するコンテンツが提供されています。

## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -170,8 +170,6 @@ To deploy the models required for your chosen [embedding method](#supported-embe
 
 ## Start the wizard
 
-To start the wizard for multimodal search:
-
 1. Sign in to the [Azure portal](https://portal.azure.com/) and select your Azure AI Search service.
 
 1. On the **Overview** page, select **Import data (new)**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダル検索のウィザード開始の説明の修正"
}
```

### Explanation
この変更は、マルチモーダル検索に関連する文書（search-get-started-portal-image-search.md）が修正されたことを示しています。具体的には、ウィザードの開始手順に関する説明が簡略化されました。

以下が具体的な変更点です：
- ウィザードを開始するための手順から、「ウィザードを開始するには」といった導入文が削除されました。
- 残された手順として、Azureポータルにサインインし、選択するサービスに関する具体的な指示が維持されています。

この変更により、文書の流れがよりシンプルになり、読者が手順に入る際の障壁が低くなりました。変更は合計で2行の削除が行われており、全体としての明快さと簡潔さが向上しています。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ This quickstart uses text-based PDFs and simple images from the [azure-search-sa
 
 The wizard [supports several Azure data sources](search-import-data-portal.md#supported-data-sources-and-scenarios). However, this quickstart only covers the data sources that work with whole files, which are described in the following table.
 
-| Supported data source | Description |
+| Data source | Description |
 |--|--|
 | [Azure Blob Storage](/azure/storage/common/storage-account-create) | This data source works with blobs and tables. You must use a standard performance (general-purpose v2) account. Access tiers can be hot, cool, or cold. |
 | [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/create-data-lake-storage-account) | This is an Azure Storage account with a hierarchical namespace enabled. To confirm that you have Data Lake Storage, check the **Properties** tab on the **Overview** page. |
@@ -211,8 +211,6 @@ The wizard supports several embedding models from Azure OpenAI and the Microsoft
 
 ## Start the wizard
 
-To start the wizard for vector search:
-
 1. Sign in to the [Azure portal](https://portal.azure.com/) and select your Azure AI Search service.
 
 1. On the **Overview** page, select **Import data (new)**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のウィザード開始の説明の修正"
}
```

### Explanation
この変更は、ベクトル検索に関する文書（search-get-started-portal-import-vectors.md）が修正されたことを反映しています。主に、サポートされるデータソースの表の見出しが改善され、ウィザードの開始手順が簡略化されました。

具体的な変更点は以下の通りです：
- 表の見出しが「Supported data source」から「Data source」に変更され、より一般的な表現に統一されました。これにより、文書全体の一貫性が向上しました。
- ウィザードを開始するための説明部分から、余分な導入文が削除され、手順の流れがよりスムーズになりました。

これらの修正により、文書の明確性と可読性が向上し、読者が必要な情報を素早く把握できるように配慮されています。変更は合計で4行、うち3行の削除と1行の追加があり、全体的な簡潔さが改善されています。

## articles/search/search-get-started-portal.md{#item-6d0cb1}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 12/05/2025
+ms.date: 03/04/2026
 ms.custom:
   - mode-ui
   - ignite-2023
@@ -16,62 +16,196 @@ ms.custom:
 
 # Quickstart: Full-text search in the Azure portal
 
-[!INCLUDE [Import data (new) instructions](includes/quickstarts/search-get-started-portal-new-wizard.md)]
+> [!IMPORTANT]
+> The **Import data (new)** wizard now supports keyword search, which was previously only available in the **Import data** wizard. We recommend the new wizard for an improved search experience. For more information about how we're consolidating the wizards, see [Import data wizards in the Azure portal](search-import-data-portal.md).
 
-<!-- Removed this from metadata. Remove the the zone pivot entry on next PR
-zone_pivot_groups: azure-portal-wizards -->
+In this quickstart, you use the **Import data (new)** wizard and sample data about fictitious hotels to get started with [full-text search](search-lucene-query-architecture.md), also known as keyword search. The wizard requires no code to create an index, helping you write interesting queries within minutes.
 
-<!-- ::: zone pivot="import-data-new"
-[!INCLUDE [Import data (new) instructions](includes/quickstarts/search-get-started-portal-new-wizard.md)]
-::: zone-end
+The wizard creates multiple objects on your search service, including a searchable index, an indexer, and a data source connection for automated data retrieval. At the end of this quickstart, you review each object.
 
-::: zone pivot="import-data"
-[!INCLUDE [Import data instructions](includes/quickstarts/search-get-started-portal-old-wizard.md)]
-::: zone-end -->
+## Prerequisites
 
-## Monitor indexer progress
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-You can monitor the creation of the indexer and index in the Azure portal. The **Overview** page provides links to the objects created on your search service.
++ An [Azure AI Search service](search-create-service-portal.md). This quickstart requires the Basic tier or higher for managed identity support.
 
-To monitor the progress of the indexer:
++ An [Azure Storage account](/azure/storage/common/storage-account-create). Use Azure Blob Storage or Azure Data Lake Storage Gen2 (storage account with a hierarchical namespace) on a standard performance (general-purpose v2) account. To avoid bandwidth charges, use the same region as Azure AI Search.
 
-1. From the left pane, select **Indexers**.
++ Familiarity with the wizard. See [Import data wizards in the Azure portal](search-import-data-portal.md).
+
+### Check for network access
+
+For this quickstart, all of the preceding resources must have public access enabled so that the Azure portal nodes can access them. Otherwise, the wizard fails. After the wizard runs, you can enable firewalls and private endpoints on the integration components for security. For more information, see [Secure connections in the import wizards](search-import-data-portal.md#secure-connections).
+
+### Check for space
+
+Many customers start with a free search service, which is limited to three indexes, three indexers, and three data sources. This quickstart creates one of each, so before you begin, make sure you have room for extra objects.
+
+On the **Overview** page, select **Usage** to see how many indexes, indexers, and data sources you currently have.
+
+   :::image type="content" source="media/search-get-started-portal/overview-quota-usage.png" alt-text="Screenshot of the Overview page for an Azure AI Search service instance in the Azure portal, showing the number of indexes, indexers, and data sources." lightbox="media/search-get-started-portal/overview-quota-usage.png":::
+
+## Configure access
+
+Before you begin, make sure you have permissions to access content and operations. This quickstart uses Microsoft Entra ID for authentication and role-based access for authorization. You must be an **Owner** or **User Access Administrator** to assign roles. If roles aren't feasible, use [key-based authentication](search-security-api-keys.md) instead.
+
+To configure access for this quickstart:
+
+1. Sign in to the [Azure portal](https://portal.azure.com).
+
+1. On your Azure AI Search service:
+
+    1. [Enable role-based access](search-security-enable-roles.md).
+
+    1. [Create a system-assigned managed identity](search-how-to-managed-identities.md#create-a-system-managed-identity).
+
+    1. [Assign the following roles](search-security-rbac.md) to your user account: **Search Service Contributor**, **Search Index Data Contributor**, and **Search Index Data Reader**.
+
+1. On your Azure Storage account, assign **Storage Blob Data Reader** to the managed identity of your search service.
+
+## Prepare sample data
+
+This quickstart uses a sample JSON document that contains metadata for 50 fictitious hotels, but you can also use your own files.
+
+To prepare the sample data for this quickstart:
+
+1. Sign in to the [Azure portal](https://portal.azure.com/) and select your Azure Storage account.
+
+1. From the left pane, select **Data storage** > **Containers**.
+
+1. Create a container named **hotels-sample-data**.
+
+1. Upload the [sample JSON document](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toAzureBlobs.json) to the container.
+
+## Start the wizard
+
+1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
+
+1. On the **Overview** page, select **Import data (new)**.
+
+   :::image type="content" source="media/search-import-data-portal/import-data-new-button.png" alt-text="Screenshot that shows how to open the new import wizard in the Azure portal.":::
+
+1. Select your data source: **Azure Blob Storage** or **Azure Data Lake Storage Gen2**.
+
+   :::image type="content" source="media/search-get-started-portal-images/select-data-source.png" alt-text="Screenshot of the options for selecting a data source in the wizard." border="true" lightbox="media/search-get-started-portal-images/select-data-source.png":::
+
+1. Select **Keyword search**.
+
+   :::image type="content" source="media/search-get-started-portal/keyword-search-tile.png" alt-text="Screenshot of the keyword search tile in the Azure portal." border="true" lightbox="media/search-get-started-portal/keyword-search-tile.png":::
+
+## Run the wizard
+
+The wizard walks you through several configuration steps. This section covers each step in sequence.
+
+### Connect to a data source
+
+Azure AI Search requires a connection to a data source for content ingestion and indexing. In this case, the data source is your Azure Storage account.
+
+To connect to the sample data:
+
+1. On the **Connect to your data** page, select your Azure subscription.
+
+1. Select your storage account, and then select the **hotels-sample-data** container.
+
+1. Select **JSON array** for the parsing mode.
+
+1. Select the **Authenticate using managed identity** checkbox. Leave the identity type as **System-assigned**.
+
+   :::image type="content" source="media/search-get-started-portal/connect-to-your-data.png" alt-text="Screenshot of the Connect to your data page in the Azure portal." lightbox="media/search-get-started-portal/connect-to-your-data.png":::
+
+1. Select **Next**.
+
+### Skip AI enrichment
+
+The wizard supports skillset creation and [AI enrichment](cognitive-search-concept-intro.md) during indexing, which are beyond the scope of this quickstart. Skip this step by selecting **Next**.
+
+> [!TIP]
+> For a similar walkthrough that focuses on AI enrichment, see [Quickstart: Create a skillset in the Azure portal](search-get-started-skillset.md).
+
+### Configure the index
+
+The wizard infers a schema for your search index based on the sample data. At a minimum, the index requires a name and a collection of fields. The wizard scans for unique string fields and marks one as the document key, which uniquely identifies each document in the index.
+
+Each field has a name, [data type](/rest/api/searchservice/supported-data-types), and attributes that control how it's used. For example, **Filterable** fields support filter expressions in queries, while **Searchable** fields support keyword search. For more information, see [Configure field definitions](/azure/search/search-how-to-create-search-index#configure-field-definitions).
+
+To configure the index for the query examples in this quickstart:
+
+1. For each of the following fields, select **Configure field**, and then set the respective attributes.
+
+   | Fields | Attributes |
+   |-------|------------|
+   | `HotelId` | Key, Retrievable, Filterable, Sortable, Searchable |
+   | `HotelName`, `Category` | Retrievable, Filterable, Sortable, Searchable |
+   | `Description`, `Description_fr` | Retrievable, Searchable |
+   | `Tags` | Retrievable, Filterable, Searchable |
+   | `ParkingIncluded`, `IsDeleted` | Retrievable, Filterable, Facetable |
+   | `LastRenovationDate`, `Rating`, `Location` | Retrievable, Filterable, Sortable |
+   | `Address.StreetAddress`, `Rooms.Description`, `Rooms.Description_fr` | Retrievable, Searchable |
+   | `Address.City`, `Address.StateProvince`, `Address.PostalCode`, `Address.Country` | Retrievable, Filterable, Facetable, Searchable, Sortable|
+   | `Rooms.Type`, `Rooms.BedOptions`, `Rooms.Tags` | Retrievable, Filterable, Facetable, Searchable |
+   | `Rooms.BaseRate`, `Rooms.SleepsCount`, `Rooms.SmokingAllowed` | Retrievable, Filterable, Facetable |
+
+   :::image type="content" source="media/search-get-started-portal/configure-index.gif" alt-text="GIF that shows how to configure attributes for fields in the index." lightbox="media/search-get-started-portal/configure-index.gif":::
+
+1. Select **Next**.
+
+### Skip advanced settings
+
+The wizard offers advanced settings for semantic ranking and index scheduling, which are beyond the scope of this quickstart. Skip this step by selecting **Next**.
+
+## Finish the wizard
+
+The final step is to review your configuration and create the index, indexer, and data source on your search service. The indexer automates the process of extracting content from your data source and loading it into the index, enabling keyword search.
+
+To finish the wizard:
+
+1. Change the object name prefix to **hotels-sample**.
+
+1. Review the object configurations.
+
+   :::image type="content" source="media/search-get-started-portal/review-and-create.png" alt-text="Screenshot of the object configuration page in the Azure portal." lightbox="media/search-get-started-portal/review-and-create.png":::
+
+   AI enrichment, semantic ranker, and indexer scheduling are either disabled or set to their default values because you skipped their wizard steps.
+
+1. Select **Create** to simultaneously create the objects and run the indexer.
+
+## Check indexer status
+
+1. From the left pane, select **Search management** > **Indexers**.
 
 1. Find **hotels-sample-indexer** in the list.
 
    :::image type="content" source="media/search-get-started-portal/indexers-status.png" alt-text="Screenshot that shows the creation of the indexer in progress in the Azure portal." lightbox="media/search-get-started-portal/indexers-status.png":::
 
    It can take a few minutes for the results to update. You should see the newly created indexer with a status of **In progress** or **Success**. The list also shows the number of documents indexed.
 
-## Check search index results
+## Check index results
 
-1. From the left pane, select **Indexes**.
+1. From the left pane, select **Search management** > **Indexes**.
 
-1. Select **hotels-sample-index**. If the index has zero documents or storage, wait for the Azure portal to refresh.
+1. Select **hotels-sample**. If the index has zero documents or storage, wait for the Azure portal to refresh.
 
    :::image type="content" source="media/search-get-started-portal/indexes-list.png" alt-text="Screenshot of the Indexes list on the Azure AI Search service dashboard in the Azure portal." lightbox="media/search-get-started-portal/indexes-list.png":::
 
 1. Select the **Fields** tab to view the index schema.
 
-1. Check which fields are **Filterable** or **Sortable** so that you know what queries to write.
-
    :::image type="content" source="media/search-get-started-portal/index-schema-definition.png" alt-text="Screenshot that shows the schema definition for an index in the Azure AI Search service in the Azure portal." lightbox="media/search-get-started-portal/index-schema-definition.png":::
 
-## Add or change fields
+### Add or change index fields
 
-On the **Fields** tab, you can create a field by selecting **Add field** and specifying a name, [supported data type](/rest/api/searchservice/supported-data-types), and attributes.
+On the **Fields** tab, you can create a field by selecting **Add field** and specifying a name, supported data type, and attributes.
 
-Changing existing fields is more difficult. Existing fields have a physical representation in the search index, so they aren't modifiable, not even in code. To fundamentally change an existing field, you must create a new field to replace the original. You can add other constructs, such as scoring profiles and CORS options, to an index at any time.
+Changing existing fields is more difficult. Existing fields have a physical representation in the search index, so they aren't modifiable, not even in code. To fundamentally change an existing field, you must create a new field to replace the original. You can add other constructs, such as scoring profiles and a semantic configuration, to an index at any time.
 
 Review the index definition options to understand what you can and can't edit during index design. If an option appears dimmed, you can't modify or delete it.
 
-## Query with Search explorer
+## Query the index
 
 You now have a search index that can be queried using [**Search explorer**](search-explorer.md), which sends REST calls that conform to [Documents - Search Post (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-11-01-preview&preserve-view=true). This tool supports [simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search) and [full Lucene query syntax](/rest/api/searchservice/lucene-query-syntax-in-azure-search) for keyword search.
 
 To query your search index:
 
-1. On the **Search explorer** tab, enter text to search on.
+1. On the **Search explorer** tab, enter a query term or string, such as `new york hotel with pool or gym`.
 
    :::image type="content" source="media/search-get-started-portal/search-explorer-query-string.png" alt-text="Screenshot that shows how to enter and run a query in the  Search Explorer tool." lightbox="media/search-get-started-portal/search-explorer-query-string.png":::
 
@@ -83,14 +217,12 @@ To query your search index:
 
    :::image type="content" source="media/search-get-started-portal/search-explorer-change-view.png" alt-text="Screenshot of the JSON view selector." lightbox="media/search-get-started-portal/search-explorer-change-view.png":::
 
-## Example queries for hotels-sample index
+1. Run the following query examples to see how filtering and query syntax work.
 
-The following examples assume the JSON view and the latest preview REST API version.
-
-> [!TIP]
-> The JSON view supports intellisense for parameter name completion. Place your cursor inside the JSON view and enter a space character to see a list of all query parameters. You can also enter a letter, like `s`, to see only the query parameters that begin with that letter.
->
-> Intellisense doesn't exclude invalid parameters, so use your best judgment.
+   > [!TIP]
+   > The JSON view supports intellisense for parameter name completion. Place your cursor inside the JSON view and enter a space character to see a list of all query parameters. You can also enter a letter, like `s`, to see only the query parameters that begin with that letter.
+   >
+   > Intellisense doesn't exclude invalid parameters, so use your best judgment.
 
 ### Filter examples
 
@@ -145,7 +277,7 @@ The default syntax is [simple syntax](query-simple-syntax.md), but if you want f
 
 Misspelled query terms, like `seatle` instead of `Seattle`, don't return matches in a typical search. The `queryType=full` parameter invokes the full Lucene query parser, which supports the tilde (`~`) operand. When you use these parameters, the query performs a fuzzy search for the specified keyword and matches on terms that are similar but not an exact match.
 
-Take a minute to try these example queries on your index. For more information, see [Querying in Azure AI Search](search-query-overview.md).
+For more information about these examples, see [Querying in Azure AI Search](search-query-overview.md).
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureポータルにおけるフルテキスト検索のクイックスタートのアップデート"
}
```

### Explanation
この変更は、Azureポータルにおけるフルテキスト検索のクイックスタートガイド（search-get-started-portal.md）が大幅に修正されたことを示しています。主に、手順の改善、新情報の追加、および古い情報の削除に関する内容が含まれています。

具体的な変更点は以下の通りです：
- クイックスタートの説明において、「**Import data (new)**ウィザードがキーワード検索をサポートするようになりました」との重要な情報が追加されました。この変更により、読者は新しいウィザードの使用を推奨され、検索体験が向上したことが強調されています。
- 新しい手順や確認事項が追加され、Azureアカウントの作成、アクセスの構成、サンプルデータの準備、ウィザードの実行に関する具体的な指示が整理されました。これにより、読者は実際に手順を進めやすくなっています。
- 「モニターインデクサの進捗」や「検索インデックスの結果を確認」などのセクションが改善され、重要な作業の流れが一目で理解できるようになりました。

全体として、変更は164行の追加と32行の削除を含み、クイックスタートのステップがより明確で、ユーザーフレンドリーなものになっています。文書の内容が最新の情報に基づいて更新され、読者が簡単にフルテキスト検索を始められるようになりました。

## articles/search/search-get-started-rbac.md{#item-9d96c1}

<details>
<summary>Diff</summary>
````diff
@@ -7,20 +7,20 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
 ms.date: 11/20/2025
-zone_pivot_groups: search-get-started-rbac
+zone_pivot_groups: search-python-rest
 ---
 
 # Quickstart: Connect to a search service
 
 ::: zone pivot="python"
 
-[!INCLUDE [Python quickstart](includes/quickstarts/search-get-started-rbac-python.md)]
+[!INCLUDE [Python](includes/quickstarts/search-get-started-rbac-python.md)]
 
 ::: zone-end
 
 ::: zone pivot="rest"
 
-[!INCLUDE [REST quickstart](includes/quickstarts/search-get-started-rbac-rest.md)]
+[!INCLUDE [REST](includes/quickstarts/search-get-started-rbac-rest.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACにおけるクイックスタートのゾーンピボットの修正"
}
```

### Explanation
この変更は、RBAC（Role-Based Access Control）に関するクイックスタートガイド（search-get-started-rbac.md）の構成に関するもので、主にゾーンピボットのラベルが修正されました。

具体的な変更点は以下の通りです：
- ゾーンピボットのグループ名が「search-get-started-rbac」から「search-python-rest」に変更され、文書の内容に合わせてより適切な名称が与えられました。
- Python用のクイックスタートとREST用のクイックスタートの見出しにおいても、ラベルが「Python quickstart」および「REST quickstart」から「Python」および「REST」に変更され、文書の一貫性が高まりました。

これらの変更により、クイックスタートガイドがより明確になり、読者が必要な情報に簡単にアクセスできるようになっています。全体として、コード内の変更は3行の追加と3行の削除を含んでおり、クイックスタートドキュメントの整理と明瞭性向上が図られています。

## articles/search/search-get-started-semantic.md{#item-2b3902}

<details>
<summary>Diff</summary>
````diff
@@ -11,45 +11,45 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: quickstart
-ms.date: 11/20/2025
-zone_pivot_groups: search-get-started-semantic
+ms.date: 03/04/2026
+zone_pivot_groups: search-sdks-rest
 ---
 
 # Quickstart: Semantic ranking
 
 ::: zone pivot="csharp"
 
-[!INCLUDE [C# quickstart](includes/quickstarts/semantic-ranker-csharp.md)]
+[!INCLUDE [C#](includes/quickstarts/semantic-ranker-csharp.md)]
 
 ::: zone-end
 
-::: zone pivot="javascript"
+::: zone pivot="java"
 
-[!INCLUDE [JavaScript quickstart](includes/quickstarts/semantic-ranker-javascript.md)]
+[!INCLUDE [Java](includes/quickstarts/semantic-ranker-java.md)]
 
 ::: zone-end
 
-::: zone pivot="java"
+::: zone pivot="javascript"
 
-[!INCLUDE [Java quickstart](includes/quickstarts/semantic-ranker-java.md)]
+[!INCLUDE [JavaScript](includes/quickstarts/semantic-ranker-javascript.md)]
 
 ::: zone-end
 
 ::: zone pivot="python"
 
-[!INCLUDE [Python quickstart](includes/quickstarts/semantic-ranker-python.md)]
+[!INCLUDE [Python](includes/quickstarts/semantic-ranker-python.md)]
 
 ::: zone-end
 
-::: zone pivot="rest"
+::: zone pivot="typescript"
 
-[!INCLUDE [REST quickstart](includes/quickstarts/semantic-ranker-rest.md)]
+[!INCLUDE [TypeScript](includes/quickstarts/semantic-ranker-typescript.md)]
 
 ::: zone-end
 
-::: zone pivot="typescript"
+::: zone pivot="rest"
 
-[!INCLUDE [TypeScript quickstart](includes/quickstarts/semantic-ranker-typescript.md)]
+[!INCLUDE [REST](includes/quickstarts/semantic-ranker-rest.md)]
 
 ::: zone-end
 
@@ -59,9 +59,7 @@ zone_pivot_groups: search-get-started-semantic
 
 ## Related content
 
-In this quickstart, you learned how to invoke semantic ranking on an existing index. We recommend trying semantic ranking on your own indexes as a next step. The following articles can help you get started.
-
-+ [Semantic ranking overview](semantic-search-overview.md)
-+ [Configure semantic ranker ](semantic-how-to-configure.md)
-+ [Add query rewrite to semantic ranking](semantic-how-to-query-rewrite.md)
-+ [Use scoring profiles and semantic ranking together](semantic-how-to-enable-scoring-profiles.md)
++ [Semantic ranking in Azure AI Search](semantic-search-overview.md)
++ [Configure semantic ranker](semantic-how-to-configure.md)
++ [Add query rewrite to semantic ranker](semantic-how-to-query-rewrite.md)
++ [Use scoring profiles with semantic ranker](semantic-how-to-enable-scoring-profiles.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティック検索のクイックスタートの更新"
}
```

### Explanation
この変更は、Azureのセマンティック検索に関するクイックスタートガイド（search-get-started-semantic.md）のいくつかの部分が修正されたことを示しています。主な変更は、メタデータの更新、ゾーン名の変更、関連コンテンツのリンクの改善に関連しています。

具体的な変更点は以下の通りです：
- 日付が「2025年11月20日」から「2026年3月4日」に更新され、最新の情報に合わせられました。
- ゾーンピボットグループ名が「search-get-started-semantic」から「search-sdks-rest」に変更され、より適切なグループ化が行われました。
- プログラミング言語に対するゾーンの名称も変更されました。例えば、JavaScript用のクイックスタートはJavaに置き換えられ、逆もまた然りです。この変更により、一貫したゾーンのネーミングが保たれています。
- 関連コンテンツのリンクが若干改善され、文書がより流暢かつ論理的につながるようになりました。関連する項目に対するリンクも見直され、表現やリンク先が整理されました。

全体として、これらの変更は文書の整合性と可読性を向上させ、読者がセマンティックランキングを容易に実施できるようにするための貢献となっています。変更により、16行が追加され、18行が削除され、合計34行の変更が行われました。

## articles/search/search-get-started-text.md{#item-935941}

<details>
<summary>Diff</summary>
````diff
@@ -14,51 +14,51 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: quickstart
-zone_pivot_groups: search-quickstart-full-text
+zone_pivot_groups: search-sdks-rest-powershell
 ms.date: 02/02/2026
 ---
 
 # Quickstart: Full-text search
 
 ::: zone pivot="csharp"
 
-[!INCLUDE [C# quickstart](includes/quickstarts/full-text-csharp.md)]
+[!INCLUDE [C#](includes/quickstarts/full-text-csharp.md)]
 
 ::: zone-end
 
 ::: zone pivot="java"
 
-[!INCLUDE [Java quickstart](includes/quickstarts/full-text-java.md)]
+[!INCLUDE [Java](includes/quickstarts/full-text-java.md)]
 
 ::: zone-end
 
 ::: zone pivot="javascript"
 
-[!INCLUDE [JavaScript quickstart](includes/quickstarts/full-text-javascript.md)]
+[!INCLUDE [JavaScript](includes/quickstarts/full-text-javascript.md)]
 
 ::: zone-end
 
-::: zone pivot="powershell"
+::: zone pivot="python"
 
-[!INCLUDE [PowerShell quickstart](includes/quickstarts/full-text-powershell.md)]
+[!INCLUDE [Python](includes/quickstarts/full-text-python.md)]
 
 ::: zone-end
 
-::: zone pivot="python"
+::: zone pivot="typescript"
 
-[!INCLUDE [Python SDK quickstart](includes/quickstarts/full-text-python.md)]
+[!INCLUDE [TypeScript](includes/quickstarts/full-text-typescript.md)]
 
 ::: zone-end
 
 ::: zone pivot="rest"
 
-[!INCLUDE [REST quickstart](includes/quickstarts/full-text-rest.md)]
+[!INCLUDE [REST](includes/quickstarts/full-text-rest.md)]
 
 ::: zone-end
 
-::: zone pivot="typescript"
+::: zone pivot="powershell"
 
-[!INCLUDE [TypeScript quickstart](includes/quickstarts/full-text-typescript.md)]
+[!INCLUDE [PowerShell](includes/quickstarts/full-text-powershell.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フルテキスト検索のクイックスタートの更新"
}
```

### Explanation
この変更は、Azureのフルテキスト検索に関するクイックスタートガイド（search-get-started-text.md）の内容を更新したものです。主に、ゾーンピボットのラベルが改訂され、プログラミング言語に対応したクイックスタートの記述が整理されています。

具体的な変更点は次の通りです：
- ゾーンピボットグループ名が「search-quickstart-full-text」から「search-sdks-rest-powershell」に変更され、ドキュメントの分類がより適切になっています。
- 日付が新しく「2026年2月2日」に更新され、公開日が最新の情報を反映しています。
- 各プログラミング言語対応のクイックスタートに関するラベルが見直され、例えば「JavaScript quickstart」は「JavaScript」に変更され、より一貫性のある表現が使用されています。
- また、PowerShellに対応するゾーンが追加され、Python や TypeScript に関連するゾーンの順序も変更されています。

全体として、この変更はドキュメントの整合性を高めるとともに、ユーザーが必要な情報にアクセスしやすくするための改善がなされています。11行の追加と11行の削除が行われ、合計22行の変更があったことを示しています。

## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -11,44 +11,44 @@ ms.custom:
 ms.topic: quickstart
 ms.date: 01/14/2026
 ai-usage: ai-assisted
-zone_pivot_groups: search-get-started-vector-search
+zone_pivot_groups: search-sdks-rest
 ---
 
 # Quickstart: Vector search
 
-::: zone pivot="python"
+::: zone pivot="csharp"
 
-[!INCLUDE [Python quickstart](includes/quickstarts/search-get-started-vector-python.md)]
+[!INCLUDE [C#](includes/quickstarts/search-get-started-vector-csharp.md)]
 
 ::: zone-end
 
 ::: zone pivot="java"
 
-[!INCLUDE [Java quickstart](includes/quickstarts/search-get-started-vector-java.md)]
+[!INCLUDE [Java](includes/quickstarts/search-get-started-vector-java.md)]
 
 ::: zone-end
 
 ::: zone pivot="javascript"
 
-[!INCLUDE [JavaScript quickstart](includes/quickstarts/search-get-started-vector-javascript.md)]
+[!INCLUDE [JavaScript](includes/quickstarts/search-get-started-vector-javascript.md)]
 
 ::: zone-end
 
-::: zone pivot="typescript"
+::: zone pivot="python"
 
-[!INCLUDE [TypeScript quickstart](includes/quickstarts/search-get-started-vector-typescript.md)]
+[!INCLUDE [Python](includes/quickstarts/search-get-started-vector-python.md)]
 
 ::: zone-end
 
-::: zone pivot="dotnet"
+::: zone pivot="typescript"
 
-[!INCLUDE [.NET quickstart](includes/quickstarts/search-get-started-vector-dotnet.md)]
+[!INCLUDE [TypeScript](includes/quickstarts/search-get-started-vector-typescript.md)]
 
 ::: zone-end
 
 ::: zone pivot="rest"
 
-[!INCLUDE [REST quickstart](includes/quickstarts/search-get-started-vector-rest.md)]
+[!INCLUDE [REST](includes/quickstarts/search-get-started-vector-rest.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクター検索のクイックスタートの更新"
}
```

### Explanation
この変更は、Azureのベクター検索に関するクイックスタートガイド（search-get-started-vector.md）の内容を更新したもので、主にゾーンの修正とメタデータの更新が含まれています。

具体的な変更点は以下の通りです：
- ゾーンピボットグループ名が「search-get-started-vector-search」から「search-sdks-rest」に変更され、より適切なカテゴリに分類されています。
- 日付が「2026年1月14日」に設定され、最新状態が反映されています。
- ゾーンピボットの名称が変更され、Python用のクイックスタートがC#と入れ替わり、TypeScriptのゾーンがPythonに置き換えられました。また、.NET用のクイックスタートがTypeScriptに更新されました。
- 各プログラミング言語に対する文言が一貫性を持った形に整理され、表現が統一されています。

全体として、この変更は文書の整合性を向上させ、読者が必要な情報によりアクセスしやすくなることを目的としています。変更部分では10行の追加と10行の削除が行われ、合計で20行の変更がありました。

## articles/search/search-how-to-delete-documents.md{#item-556879}

<details>
<summary>Diff</summary>
````diff
@@ -73,7 +73,7 @@ Once you know which field is the document key, you can get the key value by runn
 In this example, the search string is used to find the document in the index, and the select statement determines what fields are in the results. The "HotelId" is the document key in this example. 
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
     "search": "this query has terms that pertain to the document I want to delete",
     "select": "HotelName, HotelId",
@@ -106,7 +106,7 @@ Now that you have the document key, run a [look up query](/rest/api/searchservic
 The first example returns the hotel having a document key value of `18`.
 
 ```http
-GET https://[service name].search.windows.net/indexes/hotels-sample-index/docs('18')&api-version=2025-09-01
+GET https://[service name].search.windows.net/indexes/hotels-sample/docs('18')&api-version=2025-09-01
 ```
 
 The second example returns a chunk document. The "chunk_id" is the document key.
@@ -160,7 +160,7 @@ Here's an example response:
 1. Make sure the body of the request includes the key of the document you want to delete.
 
     ```http
-    POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/index?api-version=2025-09-01
+    POST https://[service name].search.windows.net/indexes/hotels-sample/docs/index?api-version=2025-09-01
     Content-Type: application/json   
     api-key: [admin key]
     
@@ -216,7 +216,7 @@ from azure.search.documents import SearchClient
 
 # Set up the client
 service_name = "<your-search-service-name>"
-index_name = "hotels-sample-index"
+index_name = "hotels-sample"
 api_key = "<your-admin-api-key>"
 
 endpoint = f"https://{service_name}.search.windows.net"
@@ -241,7 +241,7 @@ using Azure.Search.Documents.Models;
 
 // Set up the client
 string serviceName = "<your-search-service-name>";
-string indexName = "hotels-sample-index";
+string indexName = "hotels-sample";
 string apiKey = "<your-admin-api-key>";
 
 Uri endpoint = new Uri($"https://{serviceName}.search.windows.net");
@@ -288,7 +288,7 @@ Code sample: [IndexContentManagementExample.java](https://github.com/Azure/azure
 1. Make sure the body of the request includes the keys of all of the documents you want to delete.
 
     ```http
-    POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/index?api-version=2025-09-01
+    POST https://[service name].search.windows.net/indexes/hotels-sample/docs/index?api-version=2025-09-01
     Content-Type: application/json   
     api-key: [admin key]
     
@@ -326,7 +326,7 @@ from azure.search.documents import SearchClient
 
 # Set up the client
 service_name = "<your-search-service-name>"
-index_name = "hotels-sample-index"
+index_name = "hotels-sample"
 api_key = "<your-admin-api-key>"
 
 endpoint = f"https://{service_name}.search.windows.net"
@@ -356,7 +356,7 @@ using Azure.Search.Documents.Models;
 
 // Set up the client
 string serviceName = "<your-search-service-name>";
-string indexName = "hotels-sample-index";
+string indexName = "hotels-sample";
 string apiKey = "<your-admin-api-key>";
 
 Uri endpoint = new Uri($"https://{serviceName}.search.windows.net");
@@ -410,7 +410,7 @@ After deleting documents, verify the deletion was successful.
 Use the [Get Document](/rest/api/searchservice/documents/get) API to confirm the document no longer exists:
 
 ```http
-GET https://[service-name].search.windows.net/indexes/hotels-sample-index/docs/18?api-version=2025-09-01
+GET https://[service-name].search.windows.net/indexes/hotels-sample/docs/18?api-version=2025-09-01
 api-key: [admin-key]
 ```
 
@@ -419,7 +419,7 @@ Expected response: HTTP 404 Not Found if the document was deleted successfully.
 You can also check index statistics:
 
 ```http
-GET https://[service-name].search.windows.net/indexes/hotels-sample-index/stats?api-version=2025-09-01
+GET https://[service-name].search.windows.net/indexes/hotels-sample/stats?api-version=2025-09-01
 api-key: [admin-key]
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント削除方法のクイックスタートの更新"
}
```

### Explanation
この変更は、Azureにおけるドキュメント削除の方法を説明するクイックスタートガイド（search-how-to-delete-documents.md）に対する更新であり、主に使用されるインデックス名の修正が含まれています。

具体的な変更点は次のとおりです：
- インデックス名が「hotels-sample-index」から「hotels-sample」に変更され、これに伴い、HTTPリクエストのURLも更新されています。この変更は、検索サービスのエンドポイントをより明確にするためのものです。
- ドキュメントを削除する際のHTTPリクエスト例やクライアントの設定に関連するコードサンプルが、インデックス名の変更に合わせて適切に修正されています。
- 全体を通じて、API呼び出しの各部分においてインデックス名の一貫性が保たれるようになっています。

この変更により、ユーザーは実際の操作においてより正確な情報を得ることができ、ドキュメント削除のプロセスが明確になります。10行の追加と10行の削除が行われ、合計で20行の変更が行われました。

## articles/search/search-how-to-integrated-vectorization.md{#item-86fb1e}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ This article describes the end-to-end workflow for [integrated vectorization](ve
 
 Integrated vectorization works with [all supported data sources](search-indexer-overview.md#supported-data-sources). However, this article focuses on the most commonly used data sources, which are described in the following table.
 
-| Supported data source | Description |
+| Data source | Description |
 |--|--|
 | [Azure Blob Storage](/azure/storage/common/storage-account-create) | This data source works with blobs and tables. You must use a standard performance (general-purpose v2) account. Access tiers can be hot, cool, or cold. |
 | [Azure Data Lake Storage (ADLS) Gen2](/azure/storage/blobs/create-data-lake-storage-account) | This is an Azure Storage account with a hierarchical namespace enabled. To confirm that you have Data Lake Storage, check the **Properties** tab on the **Overview** page.<br><br> :::image type="content" source="media/search-how-to-integrated-vectorization/data-lake-storage-account.png" alt-text="Screenshot of an Azure Data Lake Storage account in the Azure portal." border="true" lightbox="media/search-how-to-integrated-vectorization/data-lake-storage-account.png"::: |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "統合ベクトル化に関する記事の用語修正"
}
```

### Explanation
この変更は、統合ベクトル化に関する記事（search-how-to-integrated-vectorization.md）の表のヘッダーにおける用語を微修正したものです。

具体的な変更点は次の通りです：
- 表のヘッダーの項目名が「Supported data source」から「Data source」に修正されました。この変更により、表のコンテンツがより簡潔で明確になります。
- 表の構成自体には変更はなく、データソースに関する説明部分はそのまま維持されています。

この変更は、用語の統一性を高め、読者が情報をより容易に理解できるようにすることを目的としています。1行の追加と1行の削除があり、合計2行の変更が行われました。

## articles/search/search-how-to-load-search-index.md{#item-a72573}

<details>
<summary>Diff</summary>
````diff
@@ -66,7 +66,7 @@ REST APIs are useful for initial proof-of-concept testing, where you can test in
 1. Formulate a POST call specifying the index name, the "docs/index" endpoint, and a request body that includes the `@search.action` parameter.
 
     ```http
-    POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/index?api-version=2025-09-01
+    POST https://[service name].search.windows.net/indexes/hotels-sample/docs/index?api-version=2025-09-01
     Content-Type: application/json   
     api-key: [admin key] 
     {
@@ -187,7 +187,7 @@ using Azure.Search.Documents.Models;
 
 // Create the search client
 string serviceName = "<your-search-service-name>";
-string indexName = "hotels-sample-index";
+string indexName = "hotels-sample";
 string apiKey = "<your-admin-api-key>";
 
 Uri endpoint = new Uri($"https://{serviceName}.search.windows.net");
@@ -269,7 +269,7 @@ After loading documents, verify the data is indexed correctly.
 Use the [Get Document](/rest/api/searchservice/documents/get) API to retrieve a specific document by key:
 
 ```http
-GET https://[service-name].search.windows.net/indexes/hotels-sample-index/docs/1111?api-version=2025-09-01
+GET https://[service-name].search.windows.net/indexes/hotels-sample/docs/1111?api-version=2025-09-01
 api-key: [admin-key]
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスの読み込みに関する記事のインデックス名修正"
}
```

### Explanation
この変更は、検索インデックスの読み込みに関する記事（search-how-to-load-search-index.md）の中で、インデックス名を更新するために行われた修正です。

具体的な変更点は以下の通りです：
- インデックスに関するHTTP POSTリクエストとGETリクエストのURLが、「hotels-sample-index」というインデックス名から「hotels-sample」に変更されました。この変更は、ドキュメントの一貫性を保つことを目的としています。
- コードサンプルにおいて、C#のコードでもインデックス名が適切に更新されています。

この修正により、ユーザーが正しいインデックス名を使用して操作を実行できるようになり、全体の説明が一貫性を持つようになっています。3行の追加と3行の削除があり、合計6行の変更が行われました。

## articles/search/search-how-to-manage-index.md{#item-6bf53b}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.topic: how-to
 ms.date: 07/03/2025
 ms.update-cycle: 365-days
-zone_pivot_groups: search-how-to-manage-index
+zone_pivot_groups: search-portal-sdks-rest
 ---
 
 # Manage an index in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス管理に関する記事のゾーンピボットグループ修正"
}
```

### Explanation
この変更は、インデックス管理に関する記事（search-how-to-manage-index.md）のメタデータ内のゾーンピボットグループを変更するために行われた修正です。

具体的には、以下の点が修正されています：
- ゾーンピボットグループの値が「search-how-to-manage-index」から「search-portal-sdks-rest」に変更されました。この変更は、ドキュメントが更に適切なコンテキストに分類されることを目的としています。

この修正により、リファレンスや関連情報の検索がより効果的に行えるようになり、コンテンツの整合性が向上しています。1行の追加と1行の削除があり、合計2行の変更が行われました。

## articles/search/search-howto-complex-data-types.md{#item-75a002}

<details>
<summary>Diff</summary>
````diff
@@ -118,7 +118,7 @@ Use the [Search Index class](/dotnet/api/azure.search.documents.indexes.models.s
 
 The following snippets are from [search-dotnet-getting-started/DotNetHowTo](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowTo/DotNetHowTo). 
 
-In the Hotels sample index, `Address` is a complex field that isn't a collection (a hotel has one address). `Rooms` is a complex collection field (a hotel has many rooms). Both [Address](https://github.com/Azure-Samples/search-dotnet-getting-started/blob/master/DotNetHowTo/DotNetHowTo/Address.cs) and [Room](https://github.com/Azure-Samples/search-dotnet-getting-started/blob/master/DotNetHowTo/DotNetHowTo/Room.cs) are defined as classes.
+In the hotels-sample index, `Address` is a complex field that isn't a collection (a hotel has one address). `Rooms` is a complex collection field (a hotel has many rooms). Both [Address](https://github.com/Azure-Samples/search-dotnet-getting-started/blob/master/DotNetHowTo/DotNetHowTo/Address.cs) and [Room](https://github.com/Azure-Samples/search-dotnet-getting-started/blob/master/DotNetHowTo/DotNetHowTo/Room.cs) are defined as classes.
 
 ```csharp
 using Azure.Search.Documents.Indexes;
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Hotelsサンプルインデックスの名称修正"
}
```

### Explanation
この変更は、複雑なデータ型に関する記事（search-howto-complex-data-types.md）内で、サンプルインデックスの名称を修正するために行われたものです。

具体的な変更点は以下の通りです：
- 「Hotels sample index」という表現が「hotels-sample index」に変更されました。この変更は、インデックス名に対する一貫性を保つことを目的としています。

この修正により、ユーザーは正しいインデックス名を使用した説明を得ることができ、全体の理解が容易になります。1行の追加と1行の削除があり、合計2行の変更が行われました。

## articles/search/search-howto-concurrency.md{#item-863358}

<details>
<summary>Diff</summary>
````diff
@@ -152,7 +152,7 @@ A design pattern for implementing optimistic concurrency should include a loop t
 
 This code snippet illustrates the addition of a synonymMap to an index that already exists.
 
-The snippet gets the [hotels-sample-index](search-get-started-portal.md), checks the object version on an update operation, throws an exception if the condition fails, and then retries the operation (up to three times), starting with index retrieval from the server to get the latest version.
+The snippet gets the [hotels-sample index](search-get-started-portal.md), checks the object version on an update operation, throws an exception if the condition fails, and then retries the operation (up to three times), starting with index retrieval from the server to get the latest version.
 
 ```csharp
 private static void EnableSynonymsInHotelsIndexSafely(SearchIndexClient indexClient)
@@ -163,7 +163,7 @@ private static void EnableSynonymsInHotelsIndexSafely(SearchIndexClient indexCli
     {
         try
         {
-            SearchIndex index = indexClient.GetIndex("hotels-sample-index");
+            SearchIndex index = indexClient.GetIndex("hotels-sample");
             index = AddSynonymMapsToFields(index);
 
             // The onlyIfUnchangedcondition ensures that the index is updated only if the ETags match.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Hotelsサンプルインデックスの名称修正と拼音形式の変更"
}
```

### Explanation
この変更は、同時実行性に関する記事（search-howto-concurrency.md）内で、ホテルサンプルインデックスの名称を修正するために行われました。

具体的な変更点は以下の通りです：
- 「hotels-sample-index」という表現が「hotels-sample index」に変更されました。この変更は、インデックス名における一貫性を確保することを目的としています。
- また、インデックスを取得する際のコードスニペット内でも、インデックス名が「hotels-sample-index」から「hotels-sample」に変更されました。

これにより、ユーザーは正確で一貫性のあるインデックス名を使用していることが確認でき、理解が向上します。全体として、2行の追加と2行の削除が行われ、4行の変更が反映されています。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -226,7 +226,7 @@ from azure.search.documents import SearchClient
 
 # Set up the client
 service_name = "<your-search-service-name>"
-index_name = "hotels-sample-index"
+index_name = "hotels-sample"
 api_key = "<your-admin-api-key>"
 
 endpoint = f"https://{service_name}.search.windows.net"
@@ -257,7 +257,7 @@ using Azure.Search.Documents.Models;
 
 // Set up the client
 string serviceName = "<your-search-service-name>";
-string indexName = "hotels-sample-index";
+string indexName = "hotels-sample";
 string apiKey = "<your-admin-api-key>";
 
 Uri endpoint = new Uri($"https://{serviceName}.search.windows.net");
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Hotelsサンプルインデックスの名称変更"
}
```

### Explanation
この変更は、再インデックスに関する記事（search-howto-reindex.md）内で、ホテルサンプルインデックスの名称を変更するために行われました。

具体的な変更点は以下の通りです：
- Pythonコードスニペット内の`index_name`変数が「hotels-sample-index」から「hotels-sample」へ変更されました。
- 同様に、C#コードスニペット内の`indexName`変数も「hotels-sample-index」から「hotels-sample」へと修正されています。

この変更により、インデックス名がより一貫性のある形式に整えられ、ユーザーが正しく理解できるようになります。全体として、2行の追加と2行の削除があり、合計4行の変更が実施されています。

## articles/search/search-import-data-portal.md{#item-b804d1}

<details>
<summary>Diff</summary>
````diff
@@ -45,7 +45,7 @@ Despite their differences, the wizards follow similar workflows for content inge
 | Semantic ranking support | ❌ | ✅ |
 | Knowledge store support | ✅ | ❌ |
 
-Built-in sample data for the hotels sample index is no longer provided, but you can create an identical index by following the [Quickstart: Create an index for keyword search](search-get-started-portal.md).
+Built-in sample data for the hotels-sample index is no longer provided, but you can create an identical index by following [Quickstart: Full-text search in the Azure portal](search-get-started-portal.md).
 
 This article explains how the wizards work to help you with proof-of-concept testing. For step-by-step instructions, see [Try the wizards](#try-the-wizards).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ホテルサンプルインデックスに関する説明の修正"
}
```

### Explanation
この変更は、データインポートに関する記事（search-import-data-portal.md）において、ホテルサンプルインデックスに関する説明を修正するために行われました。

具体的な変更点は以下の通りです：
- 「Built-in sample data for the hotels sample index is no longer provided」という文が「Built-in sample data for the hotels-sample index is no longer provided」に修正されました。この変更により、インデックス名が統一され、明確性が向上します。
- また、情報を提供するためのリンクの文言も変更されました。「Quickstart: Create an index for keyword search」という表現が「Quickstart: Full-text search in the Azure portal」に変更されています。これにより、関連情報へのアクセスがより的確に表現されています。

全体として、1行の追加と1行の削除があり、合計2行の変更が実施されています。これにより、コンテンツの整合性が高まり、ユーザーが情報を正確に理解できるようになっています。

## articles/search/search-language-support.md{#item-a7979b}

<details>
<summary>Diff</summary>
````diff
@@ -72,7 +72,7 @@ The `analyzer` property on a field definition is used to set the [language analy
 
 ```JSON
 {
-  "name": "hotels-sample-index",
+  "name": "hotels-sample",
   "fields": [
     {
       "name": "Description",
@@ -114,7 +114,7 @@ By default, a search returns all fields that are marked as retrievable. As such,
 #### Example in REST
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
     "search": "animaux acceptés",
     "searchFields": "Tags, Description_fr",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ホテルサンプルインデックスの名称変更"
}
```

### Explanation
この変更は、言語サポートに関する記事（search-language-support.md）内で、ホテルサンプルインデックスに関する名称の変更が行われました。

具体的な変更点は以下の通りです：
- JSONコードスニペット内のインデックス名が「hotels-sample-index」から「hotels-sample」へ変更されました。この修正により、インデックス名称がよりシンプルで一貫性のあるものになります。
- HTTPリクエストの例でも、インデックス名が「hotels-sample-index」から「hotels-sample」へと修正されています。これにより、API使用時の参照が正確で、ユーザーが適切にリクエストを行えるようになります。

全体として、2行の追加と2行の削除があり、合計4行の変更が実施されています。この変更により、情報の一貫性が向上し、ユーザーが正しいインデックス名を使用して作業する際に混乱を防ぐことができます。

## articles/search/search-monitor-queries.md{#item-279569}

<details>
<summary>Diff</summary>
````diff
@@ -88,7 +88,7 @@ When you enable resource logging, the system captures query requests in the **Az
    | project OperationName, Query_s, IndexName_s, Documents_d
    | where OperationName == "Query.Search"
    | where Query_s != "?api-version=2025-09-01&search=*"
-   | where IndexName_s != "hotels-sample-index"
+   | where IndexName_s != "hotels-sample"
    ```
 
 1. Optionally, set a Column filter on *Query_s* to search over a specific syntax or string. For example, you could filter over *is equal to* `?api-version=2025-09-01&search=*&%24filter=HotelName`.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ホテルサンプルインデックス名の修正"
}
```

### Explanation
この変更は、クエリのモニタリングに関する記事（search-monitor-queries.md）において、ホテルサンプルインデックスの名称を修正するために行われました。

具体的な変更点は以下の通りです：
- クエリ実行におけるインデックス名のフィルタリング条件が修正されました。以前は「hotels-sample-index」として指定されていたものが、「hotels-sample」に変更されています。この修正により、インデックス名が一貫性を持ち、ユーザーが正しいインデックスに対してクエリを実行できるようになります。

全体として、1行の追加と1行の削除があり、合計2行の変更が実施されています。この変更は、情報の明確性を向上させ、ユーザーが適切なデータを取得するための助けとなります。

## articles/search/search-more-like-this.md{#item-56c565}

<details>
<summary>Diff</summary>
````diff
@@ -32,14 +32,14 @@ All following examples use the hotels sample from [Quickstart: Full-text search
 The following query finds documents whose description fields are most similar to the field of the source document as specified by the `moreLikeThis` parameter:
 
 ```http
-GET /indexes/hotels-sample-index/docs?moreLikeThis=29&searchFields=Description&api-version=2024-05-01-preview
+GET /indexes/hotels-sample/docs?moreLikeThis=29&searchFields=Description&api-version=2024-05-01-preview
 ```
 
 In this example, the request searches for hotels similar to the one with `HotelId` 29.
 Rather than using HTTP GET, you can also invoke `MoreLikeThis` using HTTP POST:
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2024-05-01-preview
+POST /indexes/hotels-sample/docs/search?api-version=2024-05-01-preview
     {
       "moreLikeThis": "29",
       "searchFields": "Description"
@@ -51,15 +51,15 @@ POST /indexes/hotels-sample-index/docs/search?api-version=2024-05-01-preview
 `MoreLikeThis` can be combined with other common query parameters like `$filter`. For instance, the query can be restricted to only hotels whose category is 'Budget' and where the rating is higher than 3.5:
 
 ```http
-GET /indexes/hotels-sample-index/docs?moreLikeThis=20&searchFields=Description&$filter=(Category eq 'Budget' and Rating gt 3.5)&api-version=2024-05-01-preview
+GET /indexes/hotels-sample/docs?moreLikeThis=20&searchFields=Description&$filter=(Category eq 'Budget' and Rating gt 3.5)&api-version=2024-05-01-preview
 ```
 
 ### Select fields and limit results
 
 The `$top` selector can be used to limit how many results should be returned in a `MoreLikeThis` query. Also, fields can be selected with `$select`. Here the top three hotels are selected along with their ID, Name, and Rating: 
 
 ```http
-GET /indexes/hotels-sample-index/docs?moreLikeThis=20&searchFields=Description&$filter=(Category eq 'Budget' and Rating gt 3.5)&$top=3&$select=HotelId,HotelName,Rating&api-version=2024-05-01-preview
+GET /indexes/hotels-sample/docs?moreLikeThis=20&searchFields=Description&$filter=(Category eq 'Budget' and Rating gt 3.5)&$top=3&$select=HotelId,HotelName,Rating&api-version=2024-05-01-preview
 ```
 
 ## Next steps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ホテルサンプルインデックス名の統一"
}
```

### Explanation
この変更は、類似検索に関する記事（search-more-like-this.md）で、ホテルサンプルインデックスの名称を統一するために行われました。

具体的な変更点は以下の通りです：
- HTTPリクエストの例で使用されているインデックス名がすべて「hotels-sample-index」から「hotels-sample」へと変更されました。これにより、インデックス名がより明確で一貫したものになり、ガイドラインに従った使用が促進されます。

具体的には、GETおよびPOSTリクエストの例において、インデックス名が修正されました。また、この変更は、類似検索におけるクエリの文脈でも一貫性を保つためのもので、ユーザーが正しいエンドポイントを参照できるようにしています。

全体として、4行の追加と4行の削除が行われており、合計で8行の変更がなされています。この修正は、ドキュメントの正確性と可読性を向上させ、開発者がAPIを利用する際の混乱を避ける手助けとなります。

## articles/search/search-pagination-page-layout.md{#item-115902}

<details>
<summary>Diff</summary>
````diff
@@ -47,7 +47,7 @@ You can choose which fields are in search results. While a search document might
 Pick fields that offer contrast and differentiation among documents, providing sufficient information to invite a clickthrough response on the part of the user. On an e-commerce site, it might be a product name, description, brand, color, size, price, and rating. For the [hotels-sample index](search-get-started-portal.md), it might be the "select" fields in the following example:
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01 
+POST /indexes/hotels-sample/docs/search?api-version=2025-09-01 
     {  
       "search": "sandy beaches",
       "select": "HotelId, HotelName, Description, Rating, Address/City",
@@ -85,7 +85,7 @@ Azure AI Search uses server-side paging to prevent queries from retrieving too m
 The default page size is 50, while the maximum page size is 1,000. If you specify a value greater than 1,000 and there are more than 1,000 results found in your index, only the first 1,000 results are returned. If the number of matches exceed the page size, the response includes information to retrieve the next page of results. For example:
 
 ```json
-"@odata.nextLink": "https://contoso-search-eastus.search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01"
+"@odata.nextLink": "https://contoso-search-eastus.search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-09-01"
 ```
 
 The top matches are determined by search score, assuming the query is full text search or semantic. Otherwise, the top matches are an arbitrary order for exact match queries (where uniform `@search.score=1.0` indicates arbitrary ranking).
@@ -95,7 +95,7 @@ Set `top` to override the default of 50. In newer preview APIs, if you're using
 To control the paging of all documents returned in a result set, use `top` and `skip` together. This query returns the first set of 15 matching documents plus a count of total matches.
 
 ```http
-POST https://contoso-search-eastus.search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST https://contoso-search-eastus.search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-09-01
 
 {
     "search": "room with a view",
@@ -108,7 +108,7 @@ POST https://contoso-search-eastus.search.windows.net/indexes/hotels-sample-inde
 This query returns the second set, skipping the first 15 to get the next 15 (16 through 30):
 
 ```http
-POST https://contoso-search-eastus.search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST https://contoso-search-eastus.search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-09-01
 
 {
     "search": "room with a view",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ホテルサンプルインデックス名の変更"
}
```

### Explanation
この変更は、検索のページネーションに関する記事（search-pagination-page-layout.md）で、ホテルサンプルインデックスの名称を更新するために行われました。

具体的な変更点は以下の通りです：
- HTTPリクエストの例で使用されているインデックス名が「hotels-sample-index」から「hotels-sample」に変更されました。この修正により、一貫したインデックス名が使用され、ユーザーが該当するAPIリクエストを正確に実行できるようになります。

具体的には、POSTリクエストの複数の例においてインデックス名が統一され、ページネーションに関する情報やクエリの実行方法についての説明が明確にされています。

全体として、4行の追加と4行の削除があり、合計で8行の変更がなされています。この修正は、ドキュメントの正確性を向上させ、開発者が検索機能を効果的に利用するための助けとなります。

## articles/search/search-query-create.md{#item-532822}

<details>
<summary>Diff</summary>
````diff
@@ -47,7 +47,7 @@ A full text query is specified in a `search` parameter and consists of terms, qu
 The following [Search POST REST API](/rest/api/searchservice/documents/search-post) call illustrates a query request using `search` and other parameters.
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
     "search": "NY +view",
     "queryType": "simple",
@@ -97,7 +97,7 @@ In the Azure portal, when you open an index, you can work with Search Explorer a
 
 1. An index opens to the [**Search explorer**](search-explorer.md) tab so that you can query right away. Switch to **JSON view** to specify query syntax. 
 
-   Here's a full text search query expression that works for the Hotels sample index:
+   Here's a full text search query expression that works for the hotels-sample index:
 
    ```json
       {
@@ -128,7 +128,7 @@ Use a REST client to set up a request. If you need help with getting started, se
 The following example calls the REST API for full text search:
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
     "search": "NY +view",
     "queryType": "simple",
@@ -162,7 +162,7 @@ from azure.search.documents import SearchClient
 
 # Set up the client
 service_name = "<your-search-service-name>"
-index_name = "hotels-sample-index"
+index_name = "hotels-sample"
 api_key = "<your-query-api-key>"
 
 endpoint = f"https://{service_name}.search.windows.net"
@@ -195,7 +195,7 @@ using Azure.Search.Documents.Models;
 
 // Set up the client
 string serviceName = "<your-search-service-name>";
-string indexName = "hotels-sample-index";
+string indexName = "hotels-sample";
 string apiKey = "<your-query-api-key>";
 
 Uri endpoint = new Uri($"https://{serviceName}.search.windows.net");
@@ -262,7 +262,7 @@ Search is fundamentally a user-driven exercise, where terms or phrases are colle
 
 If you're familiar with [query types and composition](search-query-overview.md), you might remember that the parameters on a query request depend on field attributes in an index. For example, only fields marked as *searchable* and *retrievable* can be used in queries and search results. When setting the `search`, `filter`, and `orderby` parameters in your request, you should check attributes to avoid unexpected results.
 
-In the following screenshot of the [hotels sample index](search-get-started-portal.md), only the last two fields **LastRenovationDate** and **Rating** are *sortable*, a requirement for use in an `"$orderby"` only clause.
+In the following screenshot of the [hotels-sample index](search-get-started-portal.md), only the last two fields **LastRenovationDate** and **Rating** are *sortable*, a requirement for use in an `"$orderby"` only clause.
 
 :::image type="content" source="media/search-query-overview/hotel-sample-index-definition.png" alt-text="Screenshot that shows the index definition for the hotel sample.":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス名の変更と一致性の向上"
}
```

### Explanation
この変更は、検索クエリの作成に関する記事（search-query-create.md）で、インデックス名を最新のものに統一するために行われました。

具体的な変更点は以下の通りです：
- インデックス名が「hotels-sample-index」から「hotels-sample」に変更され、一貫性が持たせられました。この修正により、ドキュメント全体でのインデックス名が統一され、利用者が理解しやすくなっています。

主な変更内容は以下のリクエスト中に見られます：
- HTTP POST リクエストおよび、いくつかのコード例が新しいインデックス名を反映するように修正されました。これにより、利用者が正しいエンドポイントを参照しやすくなっています。

また、文中の説明についても、インデックス名の一貫性に関する表現が改善されました。

全体として、6行の追加と6行の削除があり、合計で12行の変更がなされています。この修正は、ドキュメントの視認性と使用性を向上させ、開発者がAPIをより効果的に使えるようになります。

## articles/search/search-query-fuzzy.md{#item-a130e3}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ It's a query expansion exercise that produces a match on terms having a similar
 
 The graph consists of up to 50 expansions, or permutations, of each term, capturing both correct and incorrect variants in the process. The engine then returns the topmost relevant matches in the response. 
 
-For a term like "university", the graph might have `"unversty, universty, university, universe, inverse"`. Any documents that match on those in the graph are included in results. In contrast with other queries that analyze the text to handle different forms of the same word ("mice" and "mouse"), the comparisons in a fuzzy query are taken at face value without any linguistic analysis on the text. "Universe" and "inverse", which are semantically different, will match because the syntactic discrepancies are small.
+For a term like "university", the graph might have `"unversty, universty, university, universe, inverse"`. Any documents that match on those in the graph are included in results. In contrast with other queries that analyze the text to handle different forms of the same word ("mice" and "mouse"), the comparisons in a fuzzy query are taken at face value without any linguistic analysis on the text. "Universe" and "inverse", which are semantically different, match because the syntactic discrepancies are small.
 
 A match succeeds if the discrepancies are limited to two or fewer edits, where an edit is an inserted, deleted, substituted, or transposed character. The string correction algorithm that specifies the differential is the [Damerau-Levenshtein distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance) metric. It's described as the "minimum number of operations (insertions, deletions, substitutions, or transpositions of two adjacent characters) required to change one word into the other". 
 
@@ -51,7 +51,7 @@ String fields that are attributed as "searchable" are candidates for fuzzy searc
 
 Analyzers aren't used to create an expansion graph, but that doesn't mean analyzers should be ignored in fuzzy search scenarios. Analyzers are important for tokenization during indexing, where tokens in the inverted indexes are used for matching against the graph.
 
-As always, if test queries aren't producing the matches you expect, experiment with different indexing analyzers. For example, try a [language analyzer](index-add-language-analyzers.md) to see if you get better results. Some languages, particularly those with vowel mutations, can benefit from the inflection and irregular word forms generated by the Microsoft natural language processors. In some cases, using the right language analyzer can make a difference in whether a term is tokenized in a way that is compatible with the value provided by the user.
+As always, if test queries aren't producing the matches you expect, experiment with different indexing analyzers. For example, try a [language analyzer](index-add-language-analyzers.md) to see if you get better results. Some languages, particularly those with vowel mutations, can benefit from the inflection and irregular word forms generated by the Microsoft natural language processors. In some cases, using the right language analyzer can make a difference in whether a term is tokenized in a way that's compatible with the value provided by the user.
 
 ## How to invoke fuzzy search
 
@@ -60,7 +60,7 @@ Fuzzy queries are constructed using the full Lucene query syntax, invoking the [
 Here's an example of a query request that invokes fuzzy search. It includes four terms, two of which are misspelled:
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
     "search": "seatle~ waterfront~ view~ hotle~",
     "queryType": "full",
@@ -141,7 +141,7 @@ Notice that the same response is returned, but now instead of matching on "speci
 }
 ```
 
-The point of this expanded example is to illustrate the clarity that hit highlighting can bring to ambiguous results. In all cases, the same document is returned. Had you relied on document IDs to verify a match, you might have missed the shift from "special" to "SQL".
+The point of this expanded example is to illustrate the clarity that hit highlighting can bring to ambiguous results. In all cases, the same document is returned. Had you relied on document IDs to verify a match, you might miss the shift from "special" to "SQL".
 
 ## See also
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファジー検索に関する説明の明確化"
}
```

### Explanation
この変更は、ファジー検索に関する記事（search-query-fuzzy.md）で、文の表現を改善し、内容の明確性を向上させることを目的としています。

具体的な変更点は以下の通りです：
- いくつかの文において用語が調整され、より流暢で理解しやすい表現に変更されました。たとえば、「will match」が「match」に修正され、冗長な表現が削減されています。
- プログレスリクエストのURLも最新のインデックス名に更新され、「hotels-sample-index」から「hotels-sample」に変更されました。この変更により、ドキュメント全体で一貫したインデックス名が使用されています。

その他にも、ファジー検索がどのように機能するかについての説明をより直感的に伝えるための調整が行われています。具体的には、文字の誤りや編集に関する説明が少し変更され、より正確に意図が伝わるようになりました。

全体として、4行の追加と4行の削除があり、合計で8行の変更が行われています。これにより、利用者がファジー検索の機能とその使用方法をより理解しやすくなることが期待されます。

## articles/search/search-query-lucene-examples.md{#item-ce3624}

<details>
<summary>Diff</summary>
````diff
@@ -21,11 +21,10 @@ The Lucene parser supports complex query formats, such as field-scoped queries,
 
 > [!NOTE]
 > Many of the specialized query constructions enabled through the full Lucene query syntax are not [text-analyzed](search-lucene-query-architecture.md#stage-2-lexical-analysis), which can be surprising if you expect stemming or lemmatization. Lexical analysis is only performed on complete terms (a term query or phrase query). Query types with incomplete terms (prefix query, wildcard query, regex query, fuzzy query) are added directly to the query tree, bypassing the analysis stage. The only transformation performed on partial query terms is lowercasing. 
->
 
 ## Hotels sample index
 
-The following queries are based on the hotels-sample-index, which you can create by following the instructions in this [quickstart](search-get-started-portal.md).
+The following queries are based on the hotels-sample index, which you can create by following the instructions in [Quickstart: Full-text search in the Azure portal](search-get-started-portal.md).
 
 Example queries are articulated using the REST API and POST requests. You can paste and run them in a [REST client](search-get-started-text.md). Or, use the JSON view of [Search Explorer](search-explorer.md) in the Azure portal. In JSON view, you can paste in the query examples shown here in this article.
 
@@ -39,7 +38,7 @@ Request headers must have the following values:
 URI parameters must include your search service endpoint with the index name, docs collections, search command, and API version, similar to the following example:
 
 ```http
-https://{{service-name}}.search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+https://{{service-name}}.search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-09-01
 ```
 
 The request body should be formed as valid JSON:
@@ -59,7 +58,7 @@ The request body should be formed as valid JSON:
 
 + `select` set to a comma-delimited list of fields is used for search result composition, including only those fields that are useful in the context of search results.
 
-+ `count` returns the number of documents matching the search criteria. On an empty search string, the count is all documents in the index (50 in the hotels-sample-index).
++ `count` returns the number of documents matching the search criteria. On an empty search string, the count is all documents in the index (50 in the hotels-sample index).
 
 ## Example 1: Fielded search
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス名の一貫性の向上と表現の調整"
}
```

### Explanation
この変更は、Luceneクエリの例に関する記事（search-query-lucene-examples.md）で、一貫性を持たせるための調整が行われています。

具体的な変更点は以下の通りです：
- 「hotels-sample-index」というインデックス名が「hotels-sample」と変更され、他の箇所でも同様の表現に統一されています。この修正により、ドキュメント全体での用語の一貫性が向上しました。
- ドキュメント内のいくつかの文が、より自然な表現に修正されています。たとえば、クイックスタートのリファレンスが「Quickstart: Full-text search in the Azure portal」と明確化されました。

その他にも、リクエストURIの例や検索結果に関する説明がわかりやすくなるようにマイナーな修正が施されています。

全体として、3行の追加と4行の削除があり、合計で7行の変更が行われています。この変更により、利用者が検索クエリの構成をより理解しやすくなることが期待されます。

## articles/search/search-query-simple-examples.md{#item-834766}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ In Azure AI Search, the [simple query syntax](query-simple-syntax.md) invokes th
 
 ## Hotels sample index
 
-The following queries are based on the hotels-sample-index, which you can create by following the instructions in [Quickstart: Full-text search in the Azure portal](search-get-started-portal.md).
+The following queries are based on the hotels-sample index, which you can create by following the instructions in [Quickstart: Full-text search in the Azure portal](search-get-started-portal.md).
 
 Example queries are articulated using the REST API and POST requests. You can paste and run them in a [REST client](search-get-started-text.md). Or, use the JSON view of [Search explorer](search-explorer.md) in the Azure portal. In JSON view, you can paste in the query examples shown here in this article.
 
@@ -36,7 +36,7 @@ Request headers must have the following values:
 URI parameters must include your search service endpoint with the index name, docs collections, search command, and API version, similar to the following example:
 
 ```http
-https://{{service-name}}.search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+https://{{service-name}}.search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-09-01
 ```
 
 The request body should be formed as valid JSON:
@@ -56,7 +56,7 @@ The request body should be formed as valid JSON:
 
 + `select` set to a comma-delimited list of fields is used for search result composition, including just those fields that are useful in the context of search results.
 
-+ `count` returns the number of documents matching the search criteria. On an empty search string, the count is all documents in the index (50 in the hotels-sample-index).
++ `count` returns the number of documents matching the search criteria. On an empty search string, the count is all documents in the index (50 in the hotels-sample index).
 
 ## Example 1: Full text search
 
@@ -122,7 +122,7 @@ Uniform scores of *1.0* occur when there's no rank, either because the search wa
 After search results are returned, a logical next step is to provide a details page that includes more fields from the document. This example shows you how to return a single document using [Get Document](/rest/api/searchservice/documents/get) by passing in the document ID.
 
 ```http
-GET /indexes/hotels-sample-index/docs/41?api-version=2025-09-01
+GET /indexes/hotels-sample/docs/41?api-version=2025-09-01
 ```
 
 All documents have a unique identifier. If you're using the Azure portal, select the index from the **Indexes** tab and then look at the field definitions to determine which field is the key. In the REST API, the [GET Index](/rest/api/searchservice/indexes/get) call returns the index definition in the response body.
@@ -171,10 +171,10 @@ The response for the preceding query consists of the document whose key is *41*.
 
 [Filter syntax](search-query-odata-filter.md) is an OData expression that you can use by itself or with `search`. When used together in the same request, `filter` is applied first to the entire index, and then the `search` is performed on the results of the filter. Filters can therefore be a useful technique to improve query performance since they reduce the set of documents that the search query needs to process.
 
-Filters can be defined on any field marked as `filterable` in the index definition. For hotels-sample-index, filterable fields include *Category*, *Tags*, *ParkingIncluded*, *Rating*, and most *Address* fields.
+Filters can be defined on any field marked as `filterable` in the index definition. For the hotels-sample index, filterable fields include *Category*, *Tags*, *ParkingIncluded*, *Rating*, and most *Address* fields.
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST /indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
     "search": "art tours",
     "queryType": "simple",
@@ -204,7 +204,7 @@ The response for the preceding query is scoped to only those hotels categorized
 Filter expressions can include [search.ismatch and search.ismatchscoring functions](search-query-odata-full-text-search-functions.md), allowing you to build a search query within the filter. This filter expression uses a wildcard on *free* to select amenities including free wifi, free parking, and so forth.
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST /indexes/hotels-sample/docs/search?api-version=2025-09-01
   {
     "search": "",
     "filter": "search.ismatch('free*', 'Tags', 'full', 'any')",
@@ -255,10 +255,10 @@ The response for the preceding query matches on 27 hotels that offer free amenit
 
 Range filtering is supported through filters expressions for any data type. The following examples illustrate numeric and string ranges. Data types are important in range filters and work best when numeric data is in numeric fields, and string data in string fields. Numeric data in string fields isn't suitable for ranges because numeric strings aren't comparable.
 
-The following query is a numeric range. In hotels-sample-index, the only filterable numeric field is `Rating`.
+The following query is a numeric range. In the hotels-sample index, the only filterable numeric field is `Rating`.
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST /indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
     "search": "*",
     "filter": "Rating ge 2 and Rating lt 4",
@@ -297,7 +297,7 @@ The response for this query should look similar to the following example, trimme
 The next query is a range filter over a string field (Address/StateProvince):
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST /indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
     "search": "*",
     "filter": "Address/StateProvince ge 'A*' and Address/StateProvince lt 'D*'",
@@ -357,7 +357,7 @@ The response for this query should look similar to the following example, trimme
 
 ## Example 6: Geospatial search
 
-The hotels-sample-index includes a *Location* field with latitude and longitude coordinates. This example uses the [geo.distance function](search-query-odata-geo-spatial-functions.md#examples) that filters on documents within the circumference of a starting point, out to an arbitrary distance (in kilometers) that you provide. You can adjust the last value in the query (10) to reduce or enlarge the surface area of the query.
+The hotels-sample index includes a *Location* field with latitude and longitude coordinates. This example uses the [geo.distance function](search-query-odata-geo-spatial-functions.md#examples) that filters on documents within the circumference of a starting point, out to an arbitrary distance (in kilometers) that you provide. You can adjust the last value in the query (10) to reduce or enlarge the surface area of the query.
 
 ```http
 POST /indexes/v/docs/search?api-version=2025-09-01
@@ -419,7 +419,7 @@ The following example provides an illustration. The query looks for matches on *
 Notice that there's no space between the boolean operator (`-`) and the phrase *air conditioning*. The quotation marks are escaped (`\"`).
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST /indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
     "search": "restaurant -\"air conditioning\"",
     "searchMode": "any",
@@ -479,7 +479,7 @@ By default, a search service returns the top 50 matches. To control the number o
 The following example uses a filter and sort order on the `Rating` field (Rating is both filterable and sortable) because it's easier to see the effects of paging on sorted results. In a regular full search query, the top matches are ranked and paged by `@search.score`.
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST /indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
     "search": "*",
     "filter": "Rating gt 4",
@@ -495,7 +495,7 @@ The query finds 21 matching documents, but because you specified `top`, the resp
 To get the next five, skip the first batch:
 
 ```http
-POST /indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST /indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
     "search": "*",
     "filter": "Rating gt 4",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サンプルインデックス名の統一と表現の改善"
}
```

### Explanation
この変更は、シンプルな検索クエリに関する例の記事（search-query-simple-examples.md）で、インデックス名の一貫性を高め、いくつかの表現を改善することを目的としています。

具体的な変更点は以下の通りです：
- 「hotels-sample-index」というインデックス名が「hotels-sample」に変更され、他の部分でもその表現が一貫して使用されるようになりました。これにより、読者が混乱せずに理解しやすくなっています。
- クエリのリクエスト例や説明文がいくつか見直され、より明確で自然な表現が使われています。たとえば、リクエストURIや条件の説明が洗練されています。

全体として、14行の追加と14行の削除が行われ、合計で28行の変更が実施されています。この修正により、利用者が検索クエリの構成や使用方法についてよりスムーズに理解できることが見込まれます。

## articles/search/search-synonyms.md{#item-2d5d63}

<details>
<summary>Diff</summary>
````diff
@@ -157,7 +157,7 @@ Use the [Create or Update Index (REST API)](/rest/api/searchservice/indexes/crea
 ```http
 PUT /indexes?api-version=2025-09-01
 {
-    "name":"hotels-sample-index",
+    "name":"hotels-sample",
     "fields":[
         {
             "name":"description",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス名の調整"
}
```

### Explanation
この変更は、同義語に関する記事（search-synonyms.md）におけるインデックス名の修正です。具体的には、インデックス名が「hotels-sample-index」から「hotels-sample」に変更されています。

この修正により、インデックス名が他のドキュメントで使用されている用語と一致するようになり、利用者にとっての理解を容易にしています。全体として、1行の追加と1行の削除があり、合計で2行の変更が行われています。この変更は、一貫性を持たせるためのもので、ドキュメントの整合性を向上させています。

## articles/search/search-what-is-data-import.md{#item-d73ef5}

<details>
<summary>Diff</summary>
````diff
@@ -112,7 +112,7 @@ A quick way to perform a preliminary check on the document upload is to use [**S
 
 The explorer lets you query an index without having to write any code. The search experience is based on default settings, such as the [simple syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search) and default [searchMode query parameter](/rest/api/searchservice/documents/search-post). Results are returned in JSON so that you can inspect the entire document.
 
-Here's an example query that you can run in Search Explorer in JSON view. The "HotelId" is the document key of the hotels-sample-index. The filter provides the document ID of a specific document:
+Here's an example query that you can run in Search Explorer in JSON view. The "HotelId" is the document key of the hotels-sample index. The filter provides the document ID of a specific document:
 
 ```JSON
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス名の表現の統一"
}
```

### Explanation
この変更は、データインポートに関する記事（search-what-is-data-import.md）でのインデックス名の表現に関する修正です。具体的には、インデックス名「hotels-sample-index」が「hotels-sample index」に変更されました。

この修正は、インデックス名の表現を一貫性を持たせるために行われており、他の部分と合わせて表現が統一されています。結果的に、利用者がドキュメントを読みやすくなることが期待されます。全体として、1行の追加と1行の削除が行われ、合計で2行の変更となっています。このように小規模な修正でも、文書全体の整合性を保つことが重要です。

## articles/search/semantic-how-to-query-request.md{#item-85530d}

<details>
<summary>Diff</summary>
````diff
@@ -107,14 +107,14 @@ Use [Search Documents](/rest/api/searchservice/documents/search-post) to formula
 
 A response includes an `@search.rerankerScore` automatically. If you want captions or answers in the response, enable semantic ranking by setting `queryType` to `semantic` or setting `semanticQuery` and adding captions and answers to the request.
 
-The following examples in this section use the [hotels-sample-index](search-get-started-portal.md) to demonstrate semantic ranking with semantic answers and captions.
+The following examples in this section use the [hotels-sample index](search-get-started-portal.md) to demonstrate semantic ranking with semantic answers and captions.
 
 #### Use queryType=semantic
 
-If you want to set `queryType` to `semantic`, paste the following request into a web client as a template. Replace `search-service-name` with your search service name and replace `hotels-sample-index` if you have a different index name.
+If you want to set `queryType` to `semantic`, paste the following request into a web client as a template. Replace `search-service-name` with your search service name and replace `hotels-sample` if you have a different index name.
 
 ```http
-POST https://[search-service-name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST https://[search-service-name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
       "search": "interesting hotel with restaurant on site and cozy lobby or shared area",
       "count": true,
@@ -157,7 +157,7 @@ By using `semanticQuery`, you can explicitly apply [simple text syntax](query-si
 Adjust your request to the following JSON to use `semanticQuery`.
 
 ```http
-POST https://[search-service-name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-09-01
+POST https://[search-service-name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-09-01
 {
     "search": "Description:breakfast",
     "semanticQuery": "interesting hotel with restaurant on site and cozy lobby or shared area",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス名の統一と修正"
}
```

### Explanation
この変更は、セマンティック検索に関する記事（semantic-how-to-query-request.md）のインデックス名に関する修正です。具体的には、「hotels-sample-index」から「hotels-sample」に名称が統一されています。また、文中の説明とリクエスト例においてもインデックス名を一貫して修正しています。

この修正により、使用されるインデックス名の表現が一貫性を持ち、利用者にとって理解しやすくなります。合計で8つの変更が行われ、各所でインデックス名が適切に修正されていることが確認できます。このような小さな修正でも、ドキュメント全体の整合性と正確性を保つために重要です。

## articles/search/semantic-how-to-query-rewrite.md{#item-3e168f}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ Query rewriting is an optional feature. Without query rewriting, the search serv
 
 - [Azure AI Search](search-create-service-portal.md) in any [region that provides query rewrite](search-region-support.md), with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
-- An existing search index with a [semantic configuration](semantic-how-to-configure.md) and rich text content. The examples in this guide use the [hotels-sample-index](search-get-started-portal.md) sample data to demonstrate query rewriting.
+- An existing search index with a [semantic configuration](semantic-how-to-configure.md) and rich text content. The examples in this guide use the [hotels-sample index](search-get-started-portal.md) to demonstrate query rewriting.
 
 - To follow the instructions in this article, you need a web client that supports REST API requests. The examples in this article were tested with [Visual Studio Code](https://code.visualstudio.com/download) and the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension. 
 
@@ -51,7 +51,7 @@ In this REST API example, use [Search Documents (preview)](/rest/api/searchservi
 1. Paste the following request into a web client as a template. 
 
     ```http
-    POST https://[search-service-name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-11-01-preview
+    POST https://[search-service-name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-11-01-preview
     {
         "search": "newer hotel near the water with a great restaurant",
         "semanticConfiguration":"en-semantic-config",
@@ -64,7 +64,7 @@ In this REST API example, use [Search Documents (preview)](/rest/api/searchservi
     ```
 
     - Replace `search-service-name` with your search service name.
-    - Replace `hotels-sample-index` with your index name if it's different. 
+    - Replace `hotels-sample` with your index name if it's different. 
     - Set "search" to a full text search query. The search property is required for query rewriting, unless you specify [vector queries](#vector-queries-with-query-rewrite). If you specify vector queries, then the "search" text must match the `"text"` property of the `"vectorQueries"` object. Your search string can support either the [simple syntax](query-simple-syntax.md) or [full Lucene syntax](query-lucene-syntax.md).
     - Set "semanticConfiguration" to a [predefined semantic configuration](semantic-how-to-configure.md) embedded in your index.
     - Set "queryType" to "semantic". You either need to set "queryType" to "semantic" or include a nonempty "semanticQuery" property in the request. [Semantic ranking](semantic-search-overview.md) is required for query rewriting.
@@ -202,7 +202,7 @@ Here's an example of a query that includes a vector query with query rewrites. M
 - The "text" value is the same as the "search" value. These values must be identical for query rewriting to work.
 
 ```http
-POST https://[search-service-name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-11-01-preview
+POST https://[search-service-name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-11-01-preview
 {
     "search": "newer hotel near the water with a great restaurant",
     "vectorQueries": [
@@ -234,7 +234,7 @@ You might observe that the debug (test) response includes an empty array for the
 
 ```json
 {
-  "@odata.context": "https://demo-search-svc.search.windows.net/indexes('hotels-sample-index')/$metadata#docs(*)",
+  "@odata.context": "https://demo-search-svc.search.windows.net/indexes('hotels-sample')/$metadata#docs(*)",
   "@search.debug": {
     "semantic": null,
     "queryRewrites": {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス名の一貫性の向上"
}
```

### Explanation
この修正は、セマンティッククエリリライトに関する記事（semantic-how-to-query-rewrite.md）でのインデックス名の統一に焦点を当てています。変更により、「hotels-sample-index」から「hotels-sample」に名称が変更され、文書内での一貫性が向上しました。

具体的には、インデックス名が変更された部分は、クエリの例や解説においてすべて同様に修正されています。合計で10の変更が行われ、削除と追加が各5行ずつあり、全体の表記が統一されています。このような修正は、ユーザーが情報を迅速に理解できるようにするために重要であり、文書全体の整合性を高めています。

## articles/search/speller-how-to-add.md{#item-9b4502}

<details>
<summary>Diff</summary>
````diff
@@ -40,10 +40,10 @@ Use a search client that supports preview APIs on the query request. You can use
 
 ## Spell correction with simple search
 
-The following example uses the [hotels-sample-index](search-get-started-portal.md) to demonstrate spell correction on a simple text query. Without spell correction, the query returns zero results. With correction, the query returns one result for Johnson's family-oriented resort.
+The following example uses the [hotels-sample index](search-get-started-portal.md) to demonstrate spell correction on a simple text query. Without spell correction, the query returns zero results. With correction, the query returns one result for Johnson's family-oriented resort.
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-11-01-preview
+POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-11-01-preview
 {
     "search": "famly acitvites",
     "speller": "lexicon",
@@ -64,7 +64,7 @@ Spelling correction occurs on individual query terms that undergo text analysis,
 This example uses fielded search over the Category field, with full Lucene syntax, and a misspelled query term. By including speller, the typo in "Suiite" is corrected and the query succeeds.
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-11-01-preview
+POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-11-01-preview
 {
     "search": "Category:(Resort and Spa) OR Category:Suiite",
     "queryType": "full",
@@ -80,7 +80,7 @@ POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/
 This query, with typos in every term except one, undergoes spelling corrections to return relevant results. To learn more, see [Configure semantic ranker](semantic-how-to-query-request.md).
 
 ```http
-POST https://[service name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-11-01-preview    
+POST https://[service name].search.windows.net/indexes/hotels-sample/docs/search?api-version=2025-11-01-preview    
 {
     "search": "hisotoric hotell wiht great restrant nad wiifi",
     "queryType": "semantic",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス名の修正と一貫性の向上"
}
```

### Explanation
この変更は、スペル修正に関する記事（speller-how-to-add.md）でのインデックス名に焦点を当てています。具体的には、「hotels-sample-index」から「hotels-sample」にインデックス名が修正され、文書内での表記が一貫性を持つようになりました。

変更内容は、スペル修正機能を示す例に関するもので、各所で使用されていたインデックス名が正確に一つの形式に置き換えられています。合計で8つの変更があり、追加4行、削除4行の修正が行われています。これにより、ユーザーがドキュメントを読む際に、より明確で理解しやすくなっています。このような小規模な修正でも、全体的な文書の整合性を高める上で重要です。


