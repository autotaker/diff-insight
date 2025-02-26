---
date: '2025-02-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:50dc684...MicrosoftDocs:bc33227
summary: 今回のコード変更では、Azure AI Searchに関連するドキュメントの軽微な更新と重要な変更が行われました。特に、多数の画像ファイルが削除され、これがブレイキングチェンジとしてユーザーに影響を与える可能性があります。新たな機能は追加されていませんが、既存機能の理解度は向上しました。削除されたドキュメントは情報参照に影響を与え、代替情報の提供が急務です。日付の更新やコマンドの修正も行われ、ユーザビリティが向上しました。全体として、情報提供の明確化を目指す変更ですが、削除されたコンテンツの補完が必要です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:50dc684...MicrosoftDocs:bc33227){target="_blank"}

<format>
# ハイライト

今回のコード変更では、Azure AI Searchに関連するドキュメントの軽微な更新と重要な変更が行われました。特に画像ファイルの削除が多く含まれており、これがブレイキングチェンジとして、ユーザーの利用に直接的な影響を与える可能性があります。

## 新機能
今回の仕様変更により、新たな機能が追加されたわけではありませんが、ドキュメントの明確化や説明の整備によって、既存機能の理解度が向上しました。

## ブレイキングチェンジ
- 多数の画像ファイルがリポジトリから削除され、関連するドキュメントの一部が参照元を失っています。この変更はドキュメントの完全性に影響し、利用者には適切な代替手段や更新が求められる可能性があります。
- 「performance-benchmarks.md」や「search-traffic-analytics.md」など一部の根幹的なドキュメントも削除され、これにより情報参照に影響が生じています。

## その他の更新
- ドキュメントの更新に伴い、日付の調整が行われ、最新の情報が提供されるようになっています。
- クイックスタートおよびプロジェクトの設定に関するコマンドが修正され、ユーザーがフォルダーを作成した後の手順が明確化されました。

# インサイト

今回のドキュメント変更の主な狙いは、Azure AI Searchのユーザーに最新の情報を提供し、より明確で正確なガイドラインを提供することにあります。しかし、リポジトリ内からの画像ファイルの大量削除は衝撃的であり、多くのユーザーに影響を及ぼす可能性があります。このようなブレイキングチェンジは、とりわけユーザーのドキュメント参照習慣に影響を与え、代替情報やビジュアルの導入を急務としています。

また、日付の更新は最新版での情報提供を確実にするための標準的な処置ですが、これは日常的な運用やプロジェクト設定においても重要な意味を持ちます。特に、日付の変更があることで、ユーザーは情報が常に更新されているという信頼を置くことができ、その結果、Azure AI Searchが提供する技術的なサポートの品質が高く維持されることになります。

クイックスタートガイドのコマンド修正は、ユーザビリティの向上を目的としたものであり、新しい開発者がセットアップ作業を開始する際の障壁や混乱を防ぐ設計になっています。

全体として、これらの変更は、Azure AI Searchの利用をより理解しやすく、そして効率的に行うためのものであると考えられます。しかしながら、削除されたコンテンツや画像に代わる情報が提供されない限り、ユーザーエクスペリエンスが低下する可能性もあり、今後の改善と補完が必要です。</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-concept-intro.md](#item-bf9ed7) | minor update | AI探索の概念イントロダクションの日付更新 | modified | 2 | 2 | 4 | 
| [full-text-csharp.md](#item-2e943a) | minor update | C#フルテキストクイックスタートのコマンド修正 | modified | 1 | 1 | 2 | 
| [full-text-javascript.md](#item-568e3a) | minor update | JavaScriptフルテキストクイックスタートのコマンド修正 | modified | 1 | 1 | 2 | 
| [full-text-typescript.md](#item-6630e8) | minor update | TypeScriptフルテキストクイックスタートのコマンド修正 | modified | 1 | 1 | 2 | 
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | スコアリングプロフィールに関するドキュメントの更新 | modified | 11 | 3 | 14 | 
| [index-ranking-similarity.md](#item-ba07fa) | minor update | BM25関連スコアリング設定のドキュメント更新 | modified | 1 | 1 | 2 | 
| [index.yml](#item-c67121) | minor update | インデックスファイルの日付更新 | modified | 1 | 1 | 2 | 
| [cdon-logo-160px2.png](#item-4ebc68) | breaking change | CDONのロゴ画像ファイル削除 | removed | 0 | 0 | 0 | 
| [example-test.png](#item-f04817) | breaking change | 例示用テスト画像ファイル削除 | removed | 0 | 0 | 0 | 
| [s1-docsearch-qps.png](#item-c9ef9f) | breaking change | S1ドキュメント検索QPS画像ファイル削除 | removed | 0 | 0 | 0 | 
| [s1-ecom-qps.png](#item-3a5eb4) | breaking change | S1EコマースQPS画像ファイル削除 | removed | 0 | 0 | 0 | 
| [s2-docsearch-qps.png](#item-6b8082) | breaking change | S2ドキュメント検索QPS画像ファイル削除 | removed | 0 | 0 | 0 | 
| [s2-ecom-qps.png](#item-4b0a0c) | breaking change | S2EコマースQPS画像ファイル削除 | removed | 0 | 0 | 0 | 
| [s3-docsearch-qps.png](#item-63e3ae) | breaking change | S3ドキュメント検索QPS画像ファイル削除 | removed | 0 | 0 | 0 | 
| [s3-ecom-qps.png](#item-362ef7) | breaking change | S3eコマースQPS画像ファイル削除 | removed | 0 | 0 | 0 | 
| [azuresearch-trafficanalytics.png](#item-9b0332) | breaking change | Azure Searchトラフィック分析画像ファイル削除 | removed | 0 | 0 | 0 | 
| [monitor-azure-cognitive-search.md](#item-5be826) | minor update | Azure Cognitive Searchの監視に関するドキュメント修正 | modified | 0 | 2 | 2 | 
| [performance-benchmarks.md](#item-32f399) | breaking change | パフォーマンスベンチマークに関するドキュメントの削除 | removed | 0 | 224 | 224 | 
| [search-dotnet-mgmt-sdk-migration.md](#item-bcb84f) | minor update | .NET Management SDK移行に関する文書の日付更新 | modified | 1 | 1 | 2 | 
| [search-features-list.md](#item-d34448) | minor update | Azure AI Search機能リストの日付更新 | modified | 1 | 1 | 2 | 
| [search-howto-incremental-index.md](#item-d98619) | minor update | 増分インデックスの方法に関する文書の内容更新 | modified | 6 | 2 | 8 | 
| [search-howto-index-changed-deleted-blobs.md](#item-32a688) | minor update | 変更および削除検出に関する文書の内容更新 | modified | 3 | 3 | 6 | 
| [search-howto-index-encrypted-blobs.md](#item-a7097a) | minor update | 暗号化されたBlobのインデックス作成に関する文書の更新 | modified | 1 | 1 | 2 | 
| [search-howto-index-plaintext-blobs.md](#item-63efcb) | minor update | プレーンテキストBlobのインデックス作成に関する文書の更新 | modified | 1 | 1 | 2 | 
| [search-howto-index-sharepoint-online.md](#item-49ff6e) | minor update | SharePoint Onlineからのインデックス作成に関する文書の更新 | modified | 1 | 1 | 2 | 
| [search-indexer-field-mappings.md](#item-0e4628) | minor update | インデクサーフィールドマッピングに関する文書の更新 | modified | 1 | 1 | 2 | 
| [search-lucene-query-architecture.md](#item-b0d568) | minor update | Luceneクエリアーキテクチャに関する文書の更新 | modified | 1 | 1 | 2 | 
| [search-performance-analysis.md](#item-5032b3) | minor update | パフォーマンス分析に関する文書の一部削除 | modified | 0 | 2 | 2 | 
| [search-region-support.md](#item-25b0f1) | minor update | 地域サポートに関する情報の更新 | modified | 2 | 2 | 4 | 
| [search-sku-manage-costs.md](#item-6e0122) | minor update | コスト管理に関するガイドの情報更新 | modified | 3 | 3 | 6 | 
| [search-sku-tier.md](#item-7686b8) | minor update | SKUティアに関する地域情報の更新 | modified | 2 | 2 | 4 | 
| [search-traffic-analytics.md](#item-c76f2f) | breaking change | 検索トラフィック分析に関するドキュメントの削除 | removed | 0 | 222 | 222 | 
| [toc.yml](#item-c4768f) | minor update | 目次の形式と構成の改善 | modified | 64 | 68 | 132 | 
| [vector-search-filters.md](#item-f47c2b) | minor update | ベクトルクエリにおけるフィルターの説明の明確化 | modified | 2 | 2 | 4 | 
| [vector-search-integrated-vectorization.md](#item-48219d) | minor update | 統合ベクトル化の説明の調整 | modified | 12 | 17 | 29 | 
| [vector-search-overview.md](#item-56e5fa) | minor update | ベクトルサーチの概要の更新 | modified | 8 | 8 | 16 | 


# Modified Contents
## articles/search/cognitive-search-concept-intro.md{#item-bf9ed7}

<details>
<summary>Diff</summary>
````diff
@@ -10,14 +10,14 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 09/04/2024
+ms.date: 02/24/2025
 ---
 
 # AI enrichment in Azure AI Search
 
 In Azure AI Search, *AI enrichment* refers to integration with [Azure AI services](/azure/ai-services/what-are-ai-services) to process content that isn't searchable in its raw form. Through enrichment, analysis and inference are used to create searchable content and structure where none previously existed. 
 
-Because Azure AI Search is used for text and vector queries, the purpose of AI enrichment is to improve the utility of your content in search-related scenarios. Raw content must be text or images (you can't enrich vectors), but the output of an enrichment pipeline can be vectorized and indexed in a vector index using skills like [Text Split skill](cognitive-search-skill-textsplit.md) for chunking and [AzureOpenAIEmbedding skill](cognitive-search-skill-azure-openai-embedding.md) for encoding. For more information about using skills in vector scenarios, see [Integrated data chunking and embedding](vector-search-integrated-vectorization.md).
+Because Azure AI Search is used for text and vector queries, the purpose of AI enrichment is to improve the utility of your content in search-related scenarios. Raw content must be text or images (you can't enrich vectors), but the output of an enrichment pipeline can be vectorized and indexed in a search index using skills like [Text Split skill](cognitive-search-skill-textsplit.md) for chunking and [AzureOpenAIEmbedding skill](cognitive-search-skill-azure-openai-embedding.md) for vector encoding. For more information about using skills in vector scenarios, see [Integrated data chunking and embedding](vector-search-integrated-vectorization.md).
 
 AI enrichment is based on [*skills*](cognitive-search-working-with-skillsets.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI探索の概念イントロダクションの日付更新"
}
```

### Explanation
この変更は、Azure AI Searchに関するドキュメントファイル「cognitive-search-concept-intro.md」に対して行われたマイナーな更新です。具体的には、文書内の日付を「2024年9月4日」から「2025年2月24日」に変更しました。この変更は他の文章には影響を与えず、主に最新の情報を反映させる目的で行われました。また、AIエンリッチメントの目的やそれに関連するスキルについての説明はクリアなままであり、文書の読みやすさに寄与しています。全体として、内容にあまり大きな変更はなく、主に日付の更新が焦点となっています。

## articles/search/includes/quickstarts/full-text-csharp.md{#item-2e943a}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create a new folder `full-text-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
-    mkdir full-text-quickstart && code full-text-quickstart
+    mkdir full-text-quickstart && cd full-text-quickstart
     ```
 
 1. Create a new console application with the following command:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#フルテキストクイックスタートのコマンド修正"
}
```

### Explanation
この変更は、「full-text-csharp.md」というフルテキスト検索に関するC#のクイックスタートガイド内でのマイナーな修正です。特に、プロジェクトを作成するためのコマンドが更新されました。具体的には、フォルダーを作成するためのコマンドが「mkdir full-text-quickstart && code full-text-quickstart」から「mkdir full-text-quickstart && cd full-text-quickstart」に修正されました。この更新は、指示の明確さを改善し、ユーザーが新規フォルダーに移動してから作業を続けることを促すものです。全体として、ドキュメントの正確性と実行可能性が向上しました。

## articles/search/includes/quickstarts/full-text-javascript.md{#item-568e3a}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create a new folder `full-text-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
-    mkdir full-text-quickstart && code full-text-quickstart
+    mkdir full-text-quickstart && cd full-text-quickstart
     ```
 
 1. Create the `package.json` with the following command:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptフルテキストクイックスタートのコマンド修正"
}
```

### Explanation
この変更は、「full-text-javascript.md」というJavaScriptのフルテキスト検索に関するクイックスタートガイドの内容に対するマイナーな修正です。更新では、ユーザーが新しいフォルダーを作成する際のコマンドが修正されました。具体的には、「mkdir full-text-quickstart && code full-text-quickstart」というコマンドから「mkdir full-text-quickstart && cd full-text-quickstart」に改訂されました。この変更により、フォルダーを作成した後にユーザーがそのフォルダーに移動することが明示され、手順の正確さと明確さが向上します。全体として、この修正はドキュメントの使いやすさを向上させるためのものです。

## articles/search/includes/quickstarts/full-text-typescript.md{#item-6630e8}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create a new folder `full-text-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
-    mkdir full-text-quickstart && code full-text-quickstart
+    mkdir full-text-quickstart && cd full-text-quickstart
     ```
 
 1. Create the `package.json` with the following command:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptフルテキストクイックスタートのコマンド修正"
}
```

### Explanation
この変更は、「full-text-typescript.md」というTypeScriptのフルテキスト検索に関するクイックスタートガイドの修正です。具体的には、ユーザーが新しいフォルダーを作成するためのコマンドが更新されました。元のコマンド「mkdir full-text-quickstart && code full-text-quickstart」は、「mkdir full-text-quickstart && cd full-text-quickstart」という新しいコマンドに修正されました。この変更により、ユーザーが作成したフォルダーに迅速に移動できるようになり、手順の明確さと実行可能性が向上します。このように、ドキュメント全体の使いやすさが向上することが意図されています。

## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -10,14 +10,22 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 10/01/2024
+ms.date: 02/25/2025
 ---
 
 # Add scoring profiles to boost search scores
 
-Scoring profiles allow you to boost the ranking of matching documents based on criteria. In this article, learn how to specify and assign a scoring profile that boosts a search score based on parameters that you provide. 
+Scoring profiles are used to boost the ranking of matching documents based on criteria. In this article, learn how to specify and assign a scoring profile that boosts a search score based on parameters that you provide. 
 
-You can use scoring profiles for [keyword search](search-lucene-query-architecture.md), [vector search](vector-search-overview.md), and [hybrid search](hybrid-search-overview.md). However, scoring profiles only apply to nonvector fields, so make sure your index has text or numeric fields that can be used in a scoring profile. Scoring profile support for vector and hybrid search is available in 2024-05-01-preview and 2024-07-01 REST APIs and in Azure SDK packages that targeting those releases.
+You can use scoring profiles for [keyword search](search-lucene-query-architecture.md), [vector search](vector-search-overview.md), and [hybrid search](hybrid-search-overview.md). However, scoring profiles only apply to nonvector fields, so make sure your index has text or numeric fields that can be used in a scoring profile. 
+
+## Prerequisites
+
++ A new or existing search index with text or numeric fields.
+
+You can specify a scoring profile in the index designer in the Azure portal or through APIs like [Create or Update Index REST](/rest/api/searchservice/indexes/create-or-update) or equivalent APIs in any Azure SDK.
+
+Scoring profile support for vector and hybrid search is available in 2024-05-01-preview and 2024-07-01 REST APIs and in Azure SDK packages that targeting those releases.
 
 ## Key points about scoring profiles
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリングプロフィールに関するドキュメントの更新"
}
```

### Explanation
この変更は、「index-add-scoring-profiles.md」という、スコアリングプロフィールを追加して検索スコアを向上させる方法に関するドキュメントに対する修正です。主な改訂点として、日付の更新が行われ、「ms.date」が「10/01/2024」から「02/25/2025」に変更されました。また、スコアリングプロフィールを説明する文の微塵な修正がなされ、文章の流れを改善しました。

さらに、新しい「## Prerequisites」セクションが追加され、スコアリングプロフィールを使用するための前提条件として「テキストまたは数値フィールドを持つ新しいまたは既存の検索インデックス」が明記されました。この更新により、AzureポータルやAPIを介してスコアリングプロフィールを指定する方法も示され、サポートされるREST APIのバージョンについての情報が繰り返し強調されています。全体として、このマイナーな更新は、ドキュメントの明確性と情報の正確性を向上させることを目的としています。

## articles/search/index-ranking-similarity.md{#item-ba07fa}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 07/22/2024
+ms.date: 02/24/2025
 ---
 
 # Configure BM25 relevance scoring
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "BM25関連スコアリング設定のドキュメント更新"
}
```

### Explanation
この変更は、「index-ranking-similarity.md」というBM25関連スコアリングを設定する方法に関するドキュメントの修正です。主な変更点は、ドキュメントの日付が「07/22/2024」から「02/24/2025」へと更新されたことです。この日付の変更は、いくつかの情報が新しいリリースやバージョンに基づくものであることを反映しています。また、他の変更はなく、内容の追加や削除は行われていないため、主に日付情報の調整によるユーザーへの最新情報の提供が目的とされています。全体として、このマイナーな更新は、内容の鮮度を保つための重要なステップとなっています。

## articles/search/index.yml{#item-c67121}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ metadata:
   ms.topic: landing-page
   author: HeidiSteen
   ms.author: heidist
-  ms.date: 09/04/2024
+  ms.date: 02/024/2025
 # linkListType: architecture | concept | deploy | download | get-started | how-to-guide | learn | overview | quickstart | reference | tutorial | video | whats-new
 
 landingContent:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスファイルの日付更新"
}
```

### Explanation
この変更は、「index.yml」というYAML形式の構成ファイルに対して行われた修正です。主な変更は、メタデータの一部である「ms.date」が「09/04/2024」から「02/024/2025」に更新されたことです。この日付更新により、ドキュメントの最新情報を反映させることを目的としています。変更の内容としては、追加や削除はなく、主に日付情報の調整といったマイナーな更新となっています。この更新は、全体的なドキュメントポリシーにおいて重要であり、ユーザーに対して常に最新の情報を提供するために欠かせないものです。

## articles/search/media/performance-benchmarks/cdon-logo-160px2.png{#item-4ebc68}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "CDONのロゴ画像ファイル削除"
}
```

### Explanation
この変更は、「cdon-logo-160px2.png」という画像ファイルがリポジトリから削除されたことを示しています。このファイルは、パフォーマンスベンチマークに関する情報を提供するドキュメントで使用されていた可能性がありますが、現在は取り除かれたため、関連するコンテンツからの削除に影響を与える可能性があります。この削除は重大な変更（ブレイキングチェンジ）と見なされることがあり、特にこの画像に依存しているユーザーや文書がある場合、適切な代替手段を考慮する必要があるかもしれません。今後の更新においては、この変更点を考慮して、他の関連コンテンツの整合性を保つことが重要です。

## articles/search/media/performance-benchmarks/example-test.png{#item-f04817}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "例示用テスト画像ファイル削除"
}
```

### Explanation
この変更は、「example-test.png」という画像ファイルがリポジトリから削除されたことを示しています。この画像は、パフォーマンスベンチマークに関するドキュメントの例として使用されていた可能性がありますが、現在は取り除かれました。この削除は、関連するドキュメントやコンテンツに依存しているユーザーに影響を与える可能性があり、特にこの画像を参照していた部分では情報の欠落が生じるでしょう。この変更は重要な変更（ブレイキングチェンジ）と見なされるため、今後の更新や利用においてはこの点を考慮し、必要に応じて代替の画像や情報を提供することが望まれます。

## articles/search/media/performance-benchmarks/s1-docsearch-qps.png{#item-c9ef9f}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "S1ドキュメント検索QPS画像ファイル削除"
}
```

### Explanation
この変更は、「s1-docsearch-qps.png」という画像ファイルがリポジトリから削除されたことを示しています。このファイルは、パフォーマンスベンチマークに関する資料や情報を視覚的に示すために使用されていたと考えられますが、現時点で取り除かれています。この削除により、関連ドキュメントにおいてこの画像を参照していた場合、情報が不足することになります。したがって、この変更は重大な変更（ブレイキングチェンジ）と見なされる可能性があります。利用者は、今後のドキュメントやリソースの更新において、この変更を考慮し、代替情報やビジュアルを提供することが求められるでしょう。

## articles/search/media/performance-benchmarks/s1-ecom-qps.png{#item-3a5eb4}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "S1EコマースQPS画像ファイル削除"
}
```

### Explanation
この変更は、「s1-ecom-qps.png」という画像ファイルがリポジトリから削除されたことを示しています。この画像は、パフォーマンスベンチマークに関する情報を視覚的に提示するためのものであったと考えられますが、現在は削除されています。この変更により、関連するドキュメントや資料において、以前の情報が欠落する可能性があります。このため、変更は重大な変更（ブレイキングチェンジ）と見なされ、ユーザーが該当する情報やリソースを再評価する必要があります。今後、代替となる視覚資料の提供やドキュメントの更新が必要となるでしょう。

## articles/search/media/performance-benchmarks/s2-docsearch-qps.png{#item-6b8082}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "S2ドキュメント検索QPS画像ファイル削除"
}
```

### Explanation
この変更は、「s2-docsearch-qps.png」という画像ファイルがリポジトリから削除されたことを示します。この画像は、さまざまなパフォーマンスベンチマークのデータを視覚的に示すために利用されていた可能性がありますが、現在は削除されています。この削除により、関連するドキュメントや情報において、この画像を参照していた場合には情報が不足することとなり、従来の内容が欠落することが懸念されます。したがって、この変更は重大な変更（ブレイキングチェンジ）と見なされ、利用者は今後のドキュメントや情報の更新を考慮する必要があります。代替情報やビジュアルが求められる可能性があるため、適切な対応が必要です。

## articles/search/media/performance-benchmarks/s2-ecom-qps.png{#item-4b0a0c}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "S2EコマースQPS画像ファイル削除"
}
```

### Explanation
この変更は、「s2-ecom-qps.png」という画像ファイルがリポジトリから削除されたことを示しています。この画像は、eコマースにおけるパフォーマンスベンチマークに関するデータを視覚的に表示するために使用されていた可能性があります。しかし、現在はそのファイルが削除されているため、関連ドキュメントや情報において、この画像を前提とした内容が不足することが懸念されます。このため、この変更は重大な変更（ブレイキングチェンジ）と見なされ、ユーザーは今後の情報の参照や更新に注意が必要です。代替のビジュアルや新しいデータの提供が求められる可能性もあります。

## articles/search/media/performance-benchmarks/s3-docsearch-qps.png{#item-63e3ae}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "S3ドキュメント検索QPS画像ファイル削除"
}
```

### Explanation
この変更では、「s3-docsearch-qps.png」という画像ファイルがリポジトリから削除されたことを示しています。この画像は、ドキュメント検索のパフォーマンスベンチマークに関するデータを視覚的に示すために利用されていた可能性がありますが、現在は削除されています。この削除により、関連するドキュメントや情報が不足する可能性があり、特にこの画像を参照していた内容が失われることになります。そのため、この変更はブレイキングチェンジと見なされ、利用者は情報の更新や代替資料の取得を考慮する必要があります。また、今後の関連ドキュメントにどのように影響を及ぼすかについても注意が必要です。

## articles/search/media/performance-benchmarks/s3-ecom-qps.png{#item-362ef7}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "S3eコマースQPS画像ファイル削除"
}
```

### Explanation
この変更は、「s3-ecom-qps.png」という画像ファイルがリポジトリから削除されたことを示しています。この画像は、eコマースに関連するパフォーマンスベンチマークのデータを視覚的に提供するために使用されていた可能性がありますが、現在は削除されています。この削除により、関連する文書や情報が不足するリスクがあり、特にこの画像を参照していた内容が失われることになります。そのため、この変更はブレイキングチェンジ（重大な変更）と見なされ、ユーザーは今後の情報や資料に対して慎重になる必要があります。また、代替手段や新しいコンテンツが求められる可能性もあります。

## articles/search/media/search-traffic-analytics/azuresearch-trafficanalytics.png{#item-9b0332}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azure Searchトラフィック分析画像ファイル削除"
}
```

### Explanation
この変更は、「azuresearch-trafficanalytics.png」という画像ファイルがリポジトリから削除されたことを示しています。この画像は、Azure Searchにおけるトラフィック分析に関連したデータを視覚的に示す役割を果たしていたと考えられますが、現在は削除されています。この削除により、該当する情報やドキュメントが不完全になる可能性があり、特にこの画像を参照していたユーザーに影響を及ぼします。そのため、この変更はブレイキングチェンジとして扱われます。ユーザーは、今後のリソースや情報の見直しが必要であり、代替となる資料の提供が求められるかもしれません。また、この削除が他の関連コンテンツにどのように影響を与えるかについて注意深く考慮する必要があります。

## articles/search/monitor-azure-cognitive-search.md{#item-5be826}

<details>
<summary>Diff</summary>
````diff
@@ -109,8 +109,6 @@ The following table lists common and recommended alert rules for Azure AI Search
 - [Monitor Azure resources with Azure Monitor](/azure/azure-monitor/essentials/monitor-azure-resource)
 - [Monitor queries](search-monitor-queries.md)
 - [Monitor indexer-based indexing](search-howto-monitor-indexers.md)
-- [Monitor client-side interactions](search-traffic-analytics.md)
 - [Visualize resource logs](search-monitor-logs-powerbi.md)
 - [Analyze performance in Azure AI Search](search-performance-analysis.md)
-- [Performance benchmarks](performance-benchmarks.md)
 - [Tips for better performance](search-performance-tips.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Cognitive Searchの監視に関するドキュメント修正"
}
```

### Explanation
この変更は、「monitor-azure-cognitive-search.md」ファイルに対して行われた修正を示しています。具体的には、ドキュメント内の2つの項目が削除されました。削除された項目は、「Monitor client-side interactions」（クライアントサイドのインタラクションの監視）と「Performance benchmarks」（パフォーマンスベンチマーク）です。これにより、Azure Cognitive Searchに関連する監視の推奨方法が更新され、焦点がより直接的なリソースの監視や分析方法に移ることが反映されています。この変更は、最新の監視手法やベストプラクティスに基づくものであり、ユーザーに対してより明確で関連性の高い情報を提供することを目的としています。全体として、これは軽微な更新と見なされますが、ユーザーが参照する情報の正確性を高める重要な変更です。

## articles/search/performance-benchmarks.md{#item-32f399}

<details>
<summary>Diff</summary>
````diff
@@ -1,224 +0,0 @@
----
-title: Performance benchmarks
-titleSuffix: Azure AI Search
-description: Learn about the performance of Azure AI Search through various performance benchmarks
-author: gmndrg
-ms.author: gimondra
-ms.service: azure-ai-search
-ms.custom:
-  - ignite-2023
-ms.topic: conceptual
-ms.date: 04/22/2024
----
-
-# Azure AI Search performance benchmarks
-
-> [!IMPORTANT]
-> These benchmarks apply to search services created *before April 3, 2024* on deployments that run on older infrastructure. The benchmarks also apply to nonvector workloads only. Updates are pending for services and workloads on the new limits. 
-
-Performance benchmarks are useful for estimating potential performance under similar configurations. Actual performance depends on a [variety of factors](search-performance-tips.md), including the size of your search service and the types of queries you're sending. 
-
-To help you estimate the size of search service needed for your workload, we ran several benchmarks to document the performance for different search services and configurations. 
-
-To cover a range of different use cases, we ran benchmarks for two main scenarios:
-
-* **E-commerce search** - This benchmark emulates a real e-commerce scenario and is based on the Nordic e-commerce company [CDON](https://cdon.com).
-* **Document search** - This scenario is comprised of keyword search over full text documents from [Semantic Scholar](https://www.aclweb.org/anthology/2020.acl-main.447/). This emulates a typical document search solution.
-
-While these scenarios reflect different use cases, every scenario is different so we always recommend performance testing your individual workload. We've published a [performance testing solution using JMeter](https://github.com/Azure-Samples/azure-search-performance-testing) so you can run similar tests against your own service.
-
-## Testing methodology
-
-To benchmark Azure AI Search's performance, we ran tests for two different scenarios at different tiers and replica/partition combinations.
-
-To create these benchmarks, the following methodology was used:
-
-1. The test begins at `X` queries per second (QPS) for 180 seconds. This was usually 5 or 10 QPS.
-2. QPS then increased by `X` and ran for another 180 seconds
-3. Every 180 seconds, the test increased by `X` QPS until average latency increased above 1000 ms or less than 99% of queries succeeded.
-
-The following graph gives a visual example of what the test's query load looks like:
-
-![Example test](./media/performance-benchmarks/example-test.png)
-
-Each scenario used at least 10,000 unique queries to avoid tests being overly skewed by caching.
-
-> [!IMPORTANT]
-> These tests only include query workloads. If you expect to have a high volume of indexing operations, be sure to factor that into your estimation and performance testing. Sample code for simulating indexing can be found in this [tutorial](tutorial-optimize-indexing-push-api.md).
-
-### Definitions
-
-- **Maximum QPS** -  the maximum QPS numbers are based on the highest QPS achieved in a test where 99% of queries completed successfully without throttling and average latency stayed under 1000 ms.
-
-- **Percentage of max QPS** - A percentage of the maximum QPS achieved for a particular test. For example, if a given test reached a maximum of 100 QPS, 20% of max QPS would be 20 QPS.
-
-- **Latency** - The server's latency for a query; these numbers don't include [round trip delay (RTT)](https://en.wikipedia.org/wiki/Round-trip_delay). Values are in milliseconds (ms).
-
-## Testing disclaimer
-
-The code we used to run these benchmarks is available on the [azure-search-performance-testing](https://github.com/Azure-Samples/azure-search-performance-testing/tree/main/other_tools) repository. It's worth noting that we observed slightly lower QPS levels with the [JMeter performance testing solution](https://github.com/Azure-Samples/azure-search-performance-testing) than in the benchmarks. The differences can be attributed to differences in the style of the tests. This speaks to the importance of making your performance tests as similar to your production workload as possible.
-
-> [!IMPORTANT]
-> These benchmarks in no way guarantee a certain level of performance from your service but can give you an idea of the performance you can expect based on your scenario.
-
-If you have any questions or concerns, reach out to us at azuresearch_contact@microsoft.com.
-
-## Benchmark 1: E-commerce search
-
-:::row:::
-   :::column span="1":::
-      ![CDON Logo](./media/performance-benchmarks/cdon-logo-160px2.png)
-   :::column-end:::
-   :::column span="3":::
-      This benchmark was created in partnership with the e-commerce company, [CDON](https://cdon.com), the Nordic region's largest online marketplace with operations in Sweden, Finland, Norway, and Denmark. Through its 1,500 merchants, CDON offers a wide range assortment that includes over 8 million products. In 2020, CDON had over 120 million visitors and 2 million active customers. You can learn more about CDON's use of Azure AI Search in [this article](https://pulse.microsoft.com/transform/na/fa1-how-cdon-has-been-using-technology-to-become-the-leading-marketplace-in-the-nordics/).
-   :::column-end:::
-:::row-end:::
-
-To run these tests, we used a snapshot of CDON's production search index and thousands of unique queries from their [website](https://cdon.com).
-
-### Scenario Details
-
-- **Document Count**: 6,000,000 
-- **Index Size**: 20 GB
-- **Index Schema**: a wide index with 250 fields total, 25 searchable fields, and 200 facetable/filterable fields
-- **Query Types**: full text search queries including facets, filters, ordering, and scoring profiles
-
-### S1 Performance
-
-#### Queries per second
-
-The following chart shows the highest query load a service could handle for an extended period of time in terms of queries per second (QPS).
-
-![Highest maintainable QPS ecommerce s1](./media/performance-benchmarks/s1-ecom-qps.png)
-
-#### Query latency
-
-Query latency varies based on the load of the service and services under higher stress have a higher average query latency. The following table shows the 25th, 50th, 75th, 90th, 95th, and 99th percentiles of query latency for three different usage levels.
-
-| Percentage of max QPS  | Average latency | 25% | 75% | 90% | 95% | 99%|
-|---|---|---|---| --- | --- | --- | 
-| 20%  | 104 ms  | 35 ms  | 115 ms   | 177 ms | 257 ms | 738 ms |
-| 50%  | 140 ms  | 47 ms  | 144 ms   | 241 ms | 400 ms | 1175 ms |
-| 80%  | 239 ms  | 77 ms  | 248 ms   | 466 ms | 763 ms | 1752 ms | 
-
-### S2 Performance
-
-#### Queries per second
-
-The following chart shows the highest query load a service could handle for an extended period of time in terms of queries per second (QPS).
-
-![Highest maintainable QPS ecommerce s2](./media/performance-benchmarks/s2-ecom-qps.png)
-
-#### Query latency
-
-Query latency varies based on the load of the service and services under higher stress have a higher average query latency. The following table shows the 25th, 50th, 75th, 90th, 95th, and 99th percentiles of query latency for three different usage levels.
-
-| Percentage of max QPS  | Average latency | 25% | 75% | 90% | 95% | 99%|
-|---|---|---|---| --- | --- | --- | 
-| 20%  | 56 ms | 21 ms | 68 ms  | 106 ms  | 132 ms | 210 ms | 
-| 50%  | 71 ms  | 26 ms  | 83 ms   | 132 ms | 177 ms | 329 ms |
-| 80%  | 140 ms  | 47 ms  | 153 ms   | 293 ms | 452 ms | 924 ms | 
-
-### S3 Performance
-
-#### Queries per second
-
-The following chart shows the highest query load a service could handle for an extended period of time in terms of queries per second (QPS).
-
-![Highest maintainable QPS ecommerce s3](./media/performance-benchmarks/s3-ecom-qps.png)
-
-In this case, we see that adding a second partition significantly increases the maximum QPS but adding a third partition provides diminishing marginal returns. The smaller improvement is likely because all of the data is already being pulled into the S3's active memory with just two partitions.
-
-#### Query latency
-
-Query latency varies based on the load of the service and services under higher stress have a higher average query latency. The following table shows the 25th, 50th, 75th, 90th, 95th, and 99th percentiles of query latency for three different usage levels.
-
-| Percentage of max QPS  | Average latency | 25% | 75% | 90% | 95% | 99%|
-|---|---|---|---| --- | --- | --- |
-| 20%  | 50 ms  | 20 ms  | 64 ms   | 83 ms | 98 ms | 160 ms |
-| 50%  | 62 ms  | 24 ms  | 80 ms   | 107 ms | 130 ms | 253 ms |
-| 80%  | 115 ms  | 38 ms  | 121 ms   | 218 ms | 352 ms | 828 ms |
-
-## Benchmark 2: Document search
-
-### Scenario Details
-
-- **Document Count**: 7.5 million
-- **Index Size**: 22 GB
-- **Index Schema**: 23 fields; 8 searchable, 10 filterable/facetable
-- **Query Types**: keyword searches with facets and hit highlighting
-
-### S1 Performance
-
-#### Queries per second
-
-The following chart shows the highest query load a service could handle for an extended period of time in terms of queries per second (QPS).
-
-![Highest maintainable QPS doc search s1](./media/performance-benchmarks/s1-docsearch-qps.png)
-
-#### Query latency
-
-Query latency varies based on the load of the service and services under higher stress have a higher average query latency. The following table shows the 25th, 50th, 75th, 90th, 95th, and 99th percentiles of query latency for three different usage levels.
-
-| Percentage of max QPS  | Average latency | 25% | 75% | 90% | 95% | 99%|
-|---|---|---|---| --- | --- | --- |
-| 20%  | 67 ms  | 44 ms  | 77 ms   | 103 ms | 126 ms | 216 ms |
-| 50%  | 93 ms  | 59 ms  | 110 ms   | 150 ms | 184 ms | 304 ms |
-| 80%  | 150 ms  | 96 ms  | 184 ms   | 248 ms | 297 ms | 424 ms |
-
-### S2 Performance
-
-#### Queries per second
-
-The following chart shows the highest query load a service could handle for an extended period of time in terms of queries per second (QPS).
-
-![Highest maintainable QPS doc search s2](./media/performance-benchmarks/s2-docsearch-qps.png)
-
-#### Query latency
-
-Query latency varies based on the load of the service and services under higher stress have a higher average query latency. The following table shows the 25th, 50th, 75th, 90th, 95th, and 99th percentiles of query latency for three different usage levels.
-
-| Percentage of max QPS  | Average latency | 25% | 75% | 90% | 95% | 99%|
-|---|---|---|---| --- | --- | --- |
-| 20%  | 45 ms  | 31 ms  | 55 ms   | 73 ms | 84 ms | 109 ms |
-| 50%  | 63 ms  | 39 ms  | 81 ms   | 106 ms | 123 ms | 163 ms |
-| 80%  | 115 ms  | 73 ms  | 145 ms   | 191 ms | 224 ms | 291 ms |
-
-### S3 Performance
-
-#### Queries per second
-
-The following chart shows the highest query load a service could handle for an extended period of time in terms of queries per second (QPS).
-
-![Highest maintainable QPS doc search s3](./media/performance-benchmarks/s3-docsearch-qps.png)
-
-#### Query latency
-
-Query latency varies based on the load of the service and services under higher stress have a higher average query latency. The following table shows the 25th, 50th, 75th, 90th, 95th, and 99th percentiles of query latency for three different usage levels.
-
-| Percentage of max QPS  | Average latency | 25% | 75% | 90% | 95% | 99%|
-|---|---|---|---| --- | --- | --- |
-| 20%  | 43 ms  | 29 ms  | 53 ms   | 74 ms | 86 ms | 111 ms |
-| 50%  | 65 ms  | 37 ms  | 85 ms   | 111 ms | 128 ms | 164 ms |
-| 80%  | 126 ms  | 83 ms  | 162 ms   | 205 ms | 233 ms | 281 ms |
-
-## Takeaways
-
-Through these benchmarks, you can get an idea of the performance Azure AI Search offers. You can also see difference between services at different tiers.
-
-Some key take ways from these benchmarks are:
-
-* An S2 can typically handle at least four times the query volume as an S1
-* An S2 typically has lower latency than an S1 at comparable query volumes
-* As you add replicas, the QPS a service can handle typically scales linearly (for example, if one replica can handle 10 QPS then five replicas can usually handle 50 QPS)
-* The higher the load on the service, the higher the average latency
-
-You can also see that performance can vary drastically between scenarios. If you're not getting the performance you expect, check out the [tips for better performance](search-performance-tips.md).
-
-## Next steps
-
-Now that you've seen the performance benchmarks, you can learn more about how to analyze Azure AI Search's performance and key factors that influence performance.
-
-+ [Analyze performance](search-performance-analysis.md)
-+ [Tips for better performance](search-performance-tips.md)
-+ [Case Study: Use Cognitive Search to Support Complex AI Scenarios](https://techcommunity.microsoft.com/t5/azure-ai/case-study-effectively-using-cognitive-search-to-support-complex/ba-p/2804078)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "パフォーマンスベンチマークに関するドキュメントの削除"
}
```

### Explanation
この変更は、「performance-benchmarks.md」というファイルが完全に削除されたことを示しています。このドキュメントは、Azure AI Searchのパフォーマンスに関する様々なベンチマークを説明しており、システムの性能を評価するための重要なリソースでした。削除された内容には、Eコマース検索やドキュメント検索に関する具体的な実行データ、テスト方法論、およびパフォーマンスに関連する用語の定義が含まれていました。

この変更は、ユーザーに対して大きな影響を及ぼす可能性が高く、特にAzure AI Searchのパフォーマンスを評価・分析しようとする開発者や技術者にとって重要な情報が失われることになります。そのため、この変更はブレイキングチェンジとして分類され、代替の情報源またはドキュメントの復旧が求められるかもしれません。今後、ユーザーはパフォーマンスのベンチマークや分析のための別のソースを探す必要があるでしょう。

## articles/search/search-dotnet-mgmt-sdk-migration.md{#item-bcb84f}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.custom:
   - devx-track-dotnet
   - ignite-2023
 ms.topic: conceptual
-ms.date: 07/22/2024
+ms.date: 02/24/2025
 ---
 
 # Upgrade versions of the Azure Search .NET Management SDK
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": ".NET Management SDK移行に関する文書の日付更新"
}
```

### Explanation
この変更は、「search-dotnet-mgmt-sdk-migration.md」ファイルに対して行われた軽微な更新を示しています。具体的には、ドキュメント内の日付が「2024年7月22日」から「2025年2月24日」に変更されました。この日付の更新は、ドキュメントの適用可能性や最新性を反映するためのものであり、ユーザーに最新の情報を提供することを目的としています。内容自体には追加や削除はありませんが、日付の変更により、このドキュメントがより現実の状況にマッチするものとなります。これにより、利用者は最新の情報を参照しやすくなり、理解が深まることが期待されます。

## articles/search/search-features-list.md{#item-d34448}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: conceptual
-ms.date: 09/04/2024
+ms.date: 02/24/2025
 ---
 
 # Features of Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search機能リストの日付更新"
}
```

### Explanation
この変更は、「search-features-list.md」ファイルに対して行われた軽微な更新を示しています。具体的には、ドキュメント内の日付が「2024年9月4日」から「2025年2月24日」に変更されました。この日付の更新は、情報の新鮮さや関連性を保つために重要であり、ユーザーが最新のコンテンツや情報を参照しやすくすることを意図しています。

内容自体には大きな変更はなく、日付の更新のみが行われていますが、これはユーザーにとって有用な、更新された情報を提供することにつながります。このような軽微な更新は、ドキュメンテーションの整合性を保つために重要です。ユーザーは最新の日付の情報を元に、Azure AI Searchの機能について理解を深めることができるでしょう。

## articles/search/search-howto-incremental-index.md{#item-d98619}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 12/10/2024
+ms.date: 02/24/2025
 ---
 
 # Enable caching for incremental enrichment in Azure AI Search
@@ -29,7 +29,11 @@ Cached content is placed in Azure Storage using account information that you pro
 You should be familiar with setting up indexers. Start with [indexer overview](search-indexer-overview.md) and then continue on to [skillsets](cognitive-search-working-with-skillsets.md) to learn about enrichment pipelines. For more background on key concepts, see [incremental enrichment](cognitive-search-incremental-indexing-conceptual.md).
 
 > [!CAUTION]
-> If you're using the [SharePoint Online indexer (Preview)](search-howto-index-sharepoint-online.md), you should avoid incremental enrichment. Under certain circumstances, the cache becomes invalid, requiring an [indexer reset and run](search-howto-run-reset-indexers.md), should you choose to reload it.
+> Avoid enrichment caching for data originating from the [SharePoint Online indexer (Preview)](search-howto-index-sharepoint-online.md). Under certain circumstances, the cache becomes invalid, requiring a [full indexer reset and run](search-howto-run-reset-indexers.md), should you choose to reload it.
+
+## Permissions
+
+Azure AI Search needs write-access to Azure Storage. If you're using a managed identity for your search service, make sure it's assigned to the **Storage Blob Data Contributor** and **Storage Table Data Reader** roles. For more information, see [Connect to Azure Storage using a managed identity (Azure AI Search)](search-howto-managed-identities-storage.md).
 
 ## Enable on new indexers
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "増分インデックスの方法に関する文書の内容更新"
}
```

### Explanation
この変更は、「search-howto-incremental-index.md」ファイルに対して行われた軽微な更新を示しています。主な変更点として、ドキュメントの日付が「2024年12月10日」から「2025年2月24日」に更新されたほか、幾つかの内容が修正・追加されました。

具体的には、SharePoint Onlineインデクサーに関連する注意書きが改訂され、「エンリッチメントキャッシングを避けるべきこと」と明確に記述されています。さらに、新しいセクションとして「Permissions」が追加され、Azure AI SearchがAzure Storageに書き込み可能であること、マネージドアイデンティティを使用する場合の必要な役割についても説明されています。

これにより、ユーザーは増分インデックスを使用する際に必要な権限や注意点をより理解しやすくなります。この更新は、情報の正確性と利用可能性を向上させることを目的としており、ドキュメンテーション全体の品質を保つために重要です。

## articles/search/search-howto-index-changed-deleted-blobs.md{#item-32a688}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 08/05/2024
+ms.date: 02/24/2025
 ---
 
 # Change and delete detection using indexers for Azure Storage in Azure AI Search
@@ -24,7 +24,7 @@ There are two ways to implement a soft delete strategy:
 + [Native blob soft delete (preview)](#native-blob-soft-delete), applies to Blob Storage only
 + [Soft delete using custom metadata](#soft-delete-using-custom-metadata)
 
-The deletion detection strategy should be applied from the very first indexer run. If you didn't establish the deletion policy prior to the initial run, any documents that were deleted before the policy was implemented will remain in your index, even if you add the policy to the indexer later and reset it. If this has occurred, it is suggested that you create a new index using a new indexer, ensuring the deletion policy is in place from the beginning.
+The deletion detection strategy must be applied from the very first indexer run. If you didn't establish the deletion policy prior to the initial run, any documents that were deleted before the policy was implemented will remain in your index, even if you add the policy to the indexer later and reset it. If this has occurred, it's suggested that you create a new index using a new indexer, ensuring the deletion policy is in place from the beginning.
 
 ## Prerequisites
 
@@ -33,7 +33,7 @@ The deletion detection strategy should be applied from the very first indexer ru
 + Use consistent document keys and file structure. Changing document keys or directory names and paths (applies to ADLS Gen2) breaks the internal tracking information used by indexers to know which content was indexed, and when it was last indexed.
 
 > [!NOTE]
-> ADLS Gen2 allows directories to be renamed. When a directory is renamed, the timestamps for the blobs in that directory do not get updated. As a result, the indexer will not re-index those blobs. If you need the blobs in a directory to be reindexed after a directory rename because they now have new URLs, you will need to update the `LastModified` timestamp for all the blobs in the directory so that the indexer knows to re-index them during a future run. The virtual directories in Azure Blob Storage cannot be changed, so they do not have this issue.
+> ADLS Gen2 allows directories to be renamed. When a directory is renamed, the timestamps for the blobs in that directory don't get updated. As a result, the indexer won't reindex those blobs. If you need the blobs in a directory to be reindexed after a directory rename because they now have new URLs, you need to update the `LastModified` timestamp for all the blobs in the directory so that the indexer knows to reindex them during a future run. The virtual directories in Azure Blob Storage can't be changed, so they don't have this issue.
 
 ## Native blob soft delete
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "変更および削除検出に関する文書の内容更新"
}
```

### Explanation
この変更は、「search-howto-index-changed-deleted-blobs.md」ファイルに対する軽微な更新を表しています。主な変更点は、ドキュメントの日付が「2024年8月5日」から「2025年2月24日」に更新されたことと、一部の文がより明確に修正されたことです。

具体的には、削除検出戦略に関する文の表現が微調整され、文の一貫性が向上しています。特に、「削除検出戦略は初回のインデクサー実行から適用される必要がある」という記述が「should」から「must」に変更されています。これにより、ユーザーに対してこのポリシーの重要性が強調され、適切な手順を確実に踏むことが促されています。

また、ADLS Gen2に関する注意点も改善され、より分かりやすい表現になっています。これらの変更は、ドキュメントの情報を最新のものに保ち、ユーザーがより明確に理解できるようにするためのものです。全体として、これらの更新は、文書の信頼性と利用価値を高めることを目的としています。

## articles/search/search-howto-index-encrypted-blobs.md{#item-a7097a}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - ignite-2023
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 09/04/2024
+ms.date: 02/24/2025
 ---
 
 # Tutorial: Index and enrich encrypted blobs for full-text search in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "暗号化されたBlobのインデックス作成に関する文書の更新"
}
```

### Explanation
この変更は、「search-howto-index-encrypted-blobs.md」ファイルに対する軽微な更新を示しています。主な変更点は、ドキュメントの日付が「2024年9月4日」から「2025年2月24日」に更新されたことのみです。

この日付の更新は、情報が最新であることを保証し、ユーザーが参照する際に正確な文書参照を提供するために重要です。暗号化されたBlobのインデックス作成と豊かな検索体験に関するチュートリアル自体の内容は変わっていませんが、日付の更新により、ドキュメントの信頼性と関連性が向上しています。全体として、この小さな変更でもドキュメントが最新であることを伝える重要な役割を果たしています。

## articles/search/search-howto-index-plaintext-blobs.md{#item-63efcb}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 07/25/2024
+ms.date: 02/24/2025
 ---
 
 # Index plain text blobs and files in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレーンテキストBlobのインデックス作成に関する文書の更新"
}
```

### Explanation
この変更は、「search-howto-index-plaintext-blobs.md」ファイルに対する軽微な更新を示しています。主要な変更点は、ドキュメントの日付が「2024年7月25日」から「2025年2月24日」に変更されたことです。

この日付の更新により、文書が最新の情報を反映していることが確認できます。プレーンテキストのBlobやファイルのインデックス作成に関する具体的な手順やガイドライン自体は変更されていませんが、日付の更新は文書の信頼性を高め、利用者が最新の情報にアクセスできるようにするために重要です。この小さな変更は、ユーザーにとって有用なリソースであることを維持するために役立っています。

## articles/search/search-howto-index-sharepoint-online.md{#item-49ff6e}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 08/20/2024
+ms.date: 02/24/2025
 ---
 
 # Index data from SharePoint document libraries
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint Onlineからのインデックス作成に関する文書の更新"
}
```

### Explanation
この変更は、「search-howto-index-sharepoint-online.md」ファイルに対する軽微な更新を示しています。主な変更点は、ドキュメントの日付が「2024年8月20日」から「2025年2月24日」に更新されたことです。

この日付の変更により、この文書が提供する情報が最新であり、ユーザーに対して信頼性のあるリソースとなることが強調されています。SharePointドキュメントライブラリからデータをインデックス化する手順やガイドライン自体には変更がないため、実際の内容はそのまま維持されていますが、日付の更新によって文書の関連性が向上しています。この小さな修正は、ユーザーが最新の手順に基づいて作業できるようにするために重要です。

## articles/search/search-indexer-field-mappings.md{#item-0e4628}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 08/09/2024
+ms.date: 02/24/2025
 ---
 
 # Field mappings and transformations using Azure AI Search indexers
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーフィールドマッピングに関する文書の更新"
}
```

### Explanation
この変更は、「search-indexer-field-mappings.md」ファイルに対する軽微な更新を示しています。主な変更点は、ドキュメントの日付が「2024年8月9日」から「2025年2月24日」に更新されたことです。

この日付の修正により、文書が最新であることが確認され、ユーザーがアクセスする情報の正確性と関連性が保たれます。Azure AI Searchにおけるフィールドマッピングと変換に関する具体的な手順やガイドライン自体は変更されておらず、内容はそのまま維持されています。この小さな更新は、ユーザーが最新の情報に基づいて作業を行えるようサポートする目的があります。

## articles/search/search-lucene-query-architecture.md{#item-b0d568}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 08/19/2024
+ms.date: 02/24/2025
 ---
 
 # Full text search in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Luceneクエリアーキテクチャに関する文書の更新"
}
```

### Explanation
この変更は、「search-lucene-query-architecture.md」ファイルに対する軽微な更新を示しています。主な変更点は、ドキュメントの日付が「2024年8月19日」から「2025年2月24日」に更新されたことです。

この日付の変更は、文書の情報が最新であることを示し、ユーザーが信頼性の高いリソースにアクセスできるようになります。Azure AI Searchにおけるフルテキスト検索に関する具体的なコンセプトや説明には変更がなく、文書の内容はそのまま保持されています。この小さな更新は、ユーザーが最新の情報を基にして作業を行えることをサポートすることを目的としています。

## articles/search/search-performance-analysis.md{#item-5032b3}

<details>
<summary>Diff</summary>
````diff
@@ -17,8 +17,6 @@ This article describes the tools, behaviors, and approaches for analyzing query
 
 In any large implementation, it's critical to do a performance benchmarking test of your Azure AI Search service before you roll it into production. You should test both the search query load that you expect, but also the expected data ingestion workloads (if possible, run both workloads simultaneously). Having benchmark numbers helps to validate the proper [search tier](search-sku-tier.md), [service configuration](search-capacity-planning.md), and expected [query latency](search-performance-analysis.md#average-query-latency).
 
-<!-- To develop benchmarks, we recommend the [azure-search-performance-testing (GitHub)](https://github.com/Azure-Samples/azure-search-performance-testing) tool. -->
-
 To isolate the effects of a distributed service architecture, try testing on service configurations of one replica and one partition.
 
 > [!NOTE]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "パフォーマンス分析に関する文書の一部削除"
}
```

### Explanation
この変更は、「search-performance-analysis.md」ファイルに対する軽微な更新を示しています。主な変更点は、文書からの2つの行の削除です。

削除された内容は、Azure AI Searchサービスのベンチマークを開発するために推奨される「azure-search-performance-testing」ツールに関する情報でした。これは、パフォーマンスベンチマークのテストに関連する情報であり、具体的なリンクも含まれていました。

この変更により、ドキュメントはより簡潔になり、必要な情報に直接アクセスできるようになります。ただし、ベンチマークの開発に役立つツールへの言及が除外されたため、ユーザーは他のリソースを参照する必要があるかもしれません。全体として、この更新は文書のフォーカスを維持しつつ、冗長な情報を排除することを目的としています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -58,9 +58,9 @@ AI service integration refers to internal connections to an Azure AI multi-servi
 
 | Region | AI service integration | Semantic ranker | Availability zones | Capacity constrained |
 |--|--|--|--|--|
-| North Europe​​ | ✅ | ✅ | ✅ | All tiers|
+| North Europe​​ | ✅ | ✅ | ✅ | S2, S3, L1, L2|
 | West Europe​​ | ✅ | ✅ | ✅ |  |
-| France Central​​ | ✅ | ✅ | ✅ | All Tiers|
+| France Central​​ | ✅ | ✅ | ✅ | S2, S3, L1, L2|
 | Germany West Central​ ​| ✅ |  | ✅ | |
 | Italy North​​ |  |  | ✅ | |
 | Norway East​​ | ✅ |  | ✅ |  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域サポートに関する情報の更新"
}
```

### Explanation
この変更は、「search-region-support.md」ファイルに対する軽微な更新を示しています。主な変更点は、特定の地域におけるAzure AIサービスの統合に関する可用性ゾーンとキャパシティ制約の情報が更新されたことです。

具体的には、以下のような変更が行われました：
- 「ノースヨーロッパ」および「フランス中央」地域の「キャパシティ制約」列が「全ティア」から「S2、S3、L1、L2」に更新されました。

この更新により、ユーザーはノースヨーロッパおよびフランス中央地域におけるサービスの利用可能なキャパシティオプションについて、最新かつ正確な情報を得ることができます。他の地域に関しては変更がないため、全体としての内容は維持されています。更新は、地域サポートの理解を助け、正しいサービス選択を行うための重要な情報を提供することを目的としています。

## articles/search/search-sku-manage-costs.md{#item-6e0122}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 12/10/2024
+ms.date: 02/25/2025
 ---
 
 # Plan and manage costs of an Azure AI Search service
@@ -42,15 +42,15 @@ Billing is based on capacity (SUs) and the costs of running premium features, su
 
 | Meter | Unit |
 |-------|------|
-| Image extraction (AI enrichment) <sup>1, 2</sup> | Per 1000 images. See the [pricing page](https://azure.microsoft.com/pricing/details/search/#pricing). |
+| Image extraction (AI enrichment) <sup>1, 2</sup> | Per 1000 images or files. See the [pricing page](https://azure.microsoft.com/pricing/details/search/#pricing). |
 | Custom Entity Lookup skill (AI enrichment) <sup>1</sup> | Per 1000 text records. See the [pricing page](https://azure.microsoft.com/pricing/details/search/#pricing) |
 | [Built-in skills](cognitive-search-predefined-skills.md)  (AI enrichment) <sup>1</sup> | Number of transactions, billed at the same rate as if you had performed the task by calling Azure AI services directly. You can process 20 documents per indexer per day for free. Larger or more frequent workloads require a multi-resource Azure AI services key. |
 | [Semantic ranker](semantic-search-overview.md) <sup>1</sup> | Number of queries of "queryType=semantic", billed at a progressive rate. See the [pricing page](https://azure.microsoft.com/pricing/details/search/#pricing). |
 | [Shared private link](search-indexer-howto-access-private.md) <sup>1</sup> | [Billed for bandwidth](https://azure.microsoft.com/pricing/details/private-link/) as long as the shared private link exists and is used. |
 
 <sup>1</sup> Applies only if you use or enable the feature.
 
-<sup>2</sup> In an [indexer configuration](/rest/api/searchservice/indexers/create#indexer-parameters), `imageAction` is the parameter that triggers image extraction. If `imageAction` is set to "none" (the default), you won't be charged for image extraction. Costs are incurred when `imageAction` parameter is set *and* you include OCR, Image Analysis, or Document Extraction in a skillset.
+<sup>2</sup> Extracts images from a file within the indexer pipeline. Text extraction is free. Image extraction is billed during the initial document cracking step and when invoking the Document Extraction skill. In an [indexer configuration](/rest/api/searchservice/indexers/create#indexer-parameters), `imageAction` is the parameter that triggers image extraction. If `imageAction` is set to "none" (the default), there's no charge. If set to "generateNormalizedImages" or "generateNormalizedImagePerPage" and the document contains images, you're charged for each image extraction. If the document contains no images, you're still billed for the action because the indexer has to crack the file to look for images.
 
 You aren't billed on the number of full text or vector queries, query responses, or documents ingested, although [service limits](search-limits-quotas-capacity.md) do apply at each tier.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コスト管理に関するガイドの情報更新"
}
```

### Explanation
この変更は、「search-sku-manage-costs.md」ファイルに対する軽微な更新を示しています。主な変更点は、ドキュメント内のいくつかの情報が修正され、具体的には日付の更新と料金に関する説明が明確化されたことです。

具体的には、以下の変更が行われました：
- 更新された日付が「2024年12月10日」から「2025年2月25日」に変更されました。
- 「画像抽出（AIエンリッチメント）」に関する料金体系が改訂され、1000の画像やファイルに基づいて請求される旨が明示されました。
- 画像抽出に関連する課金の詳細が詳しく説明され、特にドキュメントが画像を含む場合や含まない場合の料金発生条件が明確化されています。

これにより、ユーザーはAzure AI Searchサービスのコストをより正確に把握し、利用計画を立てやすくなります。全体の内容は一貫性を保ちながら、読者が料金に関する具体的な情報を理解できるように調整されています。この更新は、サービスを利用する上での透明性を高めることを目的としています。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -59,8 +59,8 @@ Currently, several regions are capacity-constrained for specific tiers and can't
 
 | Region | Disabled tier (SKU) due to over-capacity | Suggested alternative |
 |--------|------------------------------------------|-----------------------|
-| France Central | All tiers| Sweden Central, West Europe|
-| North Europe | All tiers | Sweden Central, West Europe|
+| France Central | S2, S3, L1, L2| Sweden Central, West Europe|
+| North Europe | S2, S3, L1, L2 | Sweden Central, West Europe|
 
 ## Feature availability by tier
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SKUティアに関する地域情報の更新"
}
```

### Explanation
この変更は、「search-sku-tier.md」ファイルに対する軽微な更新を示しており、特定の地域におけるSKUティアの制約に関する情報が修正されました。

具体的な変更内容は次の通りです：
- 「フランス中央」と「ノースヨーロッパ」の地域における「無効なティア（SKU）」の項目が、以前は「全ティア」として記載されていましたが、これが「S2、S3、L1、L2」に変更されました。これは、これらの地域で利用できない具体的なティアを明示するための更新です。
- それに応じて、代替として提案されている地域（スウェーデン中央および西ヨーロッパ）の情報はそのまま維持されています。

この更新により、ユーザーは各地域でのSKUティアの選択肢と制約について、より具体的で正確な情報を得られ、サービスの利用計画や移行において適切な意思決定が可能になります。全体として、情報の透明性と有用性が向上したことを目的としています。

## articles/search/search-traffic-analytics.md{#item-c76f2f}

<details>
<summary>Diff</summary>
````diff
@@ -1,222 +0,0 @@
----
-title: Telemetry for search traffic analytics
-titleSuffix: Azure AI Search
-description: Enable search traffic analytics for Azure AI Search, collect telemetry and user-initiated events using Application Insights.
-author: HeidiSteen
-manager: nitinme
-ms.author: heidist
-
-ms.service: azure-ai-search
-ms.topic: how-to
-ms.date: 10/29/2024
----
-
-# Collect telemetry data for search traffic analytics
-
-Search traffic analytics is a pattern for collecting telemetry about user interactions with your Azure AI Search application, such as user-initiated clickstream events and keyboard inputs. Using this information, you can determine the effectiveness of your search solution, including clickthrough rate and which query inputs yield zero results.
-
-Instrumentation has the following parts:
-
-+ Add a telemetry client
-+ Modify a search request to include a correlation Id that maps search results to user actions
-+ Create and send a custom event to Application Insights and use the visualization and reporting tools to view event data
-
-This pattern takes a dependency on [Application Insights](/azure/azure-monitor/app/app-insights-overview) (a feature of [Azure Monitor](/azure/azure-monitor/)) to collect user data. It requires that you add instrumentation to your application code, as described in this article. Finally, you need a reporting mechanism to analyze the data. You can use any visualization tool that connects to Application Insights.
-
-> [!NOTE]
-> The pattern described in this article is for advanced scenarios and clickstream data generated by code you add to your client. In contrast, service logs are easy to set up, provide a range of metrics including search terms, and can be done in the Azure portal with no code required. We recommend that you enable logging for all scenarios. For more information, see [Collect and analyze log data](monitor-azure-cognitive-search.md).
-
-## Prerequisites
-
-+ [Azure AI Search](search-create-service-portal.md), any region, basic tier and above.
-
-+ [Application Insights](/azure/azure-monitor/app/create-workspace-resource).
-
-+ A rich client application providing an interactive search experience that includes clickstream events or other user actions that you want to correlate to search result selections.
-
-## Identify relevant search data
-
-To collect useful metrics for search traffic analytics, it's necessary to log some signals from the users of your search application. These signals signify content that users are interested in and that they consider relevant. For search traffic analytics, these include:
-
-+ User-generated search events: Only search queries initiated by a user are interesting. Other search requests, such as those used to populate facets or retrieve internal information, aren't important. Be sure to only instrument user-initiated events to avoid skew or bias in your results.
-
-+ User-generated clickstream events: On a search results page, a clickstream event generally means that a document is a relevant result for a specific search query.
-
-In your application code, you should correlate these events with the search results returned from a given query. By linking search and clickstream events with a correlation ID, you can gain a deeper understanding of how well your application's search functionality is performing.
-
-## Add search traffic analytics
-
-For Azure AI Search, the Azure [portal](https://portal.azure.com) provides a Search Traffic Analytics page that has C# and JavaScript code snippets for adding a telemetry client, request headers, and properties necessary for custom log events. 
-
-> [!IMPORTANT]
-> The Search traffic analytics portal page is currently outdated and references an obsolete client libary. The workaround is to use code snippets from the [azure-search-traffic-analytics](https://github.com/Azure-Samples/azure-search-traffic-analytics) GitHub repository. This article includes code snippets from the GitHub repository.
-
-:::image type="content" source="media/search-traffic-analytics/azuresearch-trafficanalytics.png" alt-text="Screenshot of the Azure portal command and page for setting up Application Insights.":::
-
-## Step 1: Set up Application Insights
-
-Create an object that sends events to Application Insights. You can add instrumentation to your server-side application code or client-side code running in a browser, expressed here as C# and JavaScript variants. For other languages, see [supported platforms and frameworks](/azure/azure-monitor/app/app-insights-overview#supported-languages).
-
-Server-side telemetry captures metrics at the application layer, for example in applications running as a web service on Azure, or as an on-premises app on a corporate network. Server-side telemetry captures search and clickstream events, the position of a document in results, and query information, but your data collection will be scoped to whatever information is available at that layer.
-
-On the client, you might have other code that manipulates query inputs, adds navigation, or includes context (for example, queries initiated from a home page versus a product page). If this describes your solution, you might opt for client-side instrumentation so that your telemetry reflects the extra detail. How this extra detail is collected goes beyond the scope of this pattern, but you can review [Application Insights for web pages](/azure/azure-monitor/app/javascript#explore-browserclient-side-data) for help with that decision.
-
-In this step, provide a [connection string to Application Insights](/azure/azure-monitor/app/migrate-from-instrumentation-keys-to-connection-strings).
-
-### [**Visual Studio**](#tab/visual-studio-telemetry-client)
-
-A shortcut that works for some Visual Studio project types is reflected in the following steps.
-
-1. Open your solution in Visual Studio.
-
-1. On the **Project** menu, select **Connected services** > **Add** > **Azure Application Insights**.
-
-1. In Connect to dependency, select **Azure Application Insights**, and then select **Next**.
-
-1. Select your Azure subscription, your Application Insights resource, and then select **Finish**.
-
-At this point, your application is set up for application monitoring, which means all page loads in your client app are tracked with default metrics.
-
-If this shortcut didn't work for you, see [Enable Application Insights server-side telemetry](/azure/azure-monitor/app/asp-net-core#enable-application-insights-server-side-telemetry-visual-studio) or refer to code snippets in the adjacent tabs.
-
-### [**.NET**](#tab/dotnet-telemetry-client)
-
-```csharp
-var telemetryConfiguration = new TelemetryConfiguration
-{
-    ConnectionString = "<PUT YOUR CONNECTION STRING HERE>"
-};
-var telemetryClient = new TelemetryClient(telemetryConfiguration);
-```
-
-### [**JavaScript**](#tab/javascript-telemetry-client)
-
-```javascript
-const appInsights = new ApplicationInsights({ config: {
-  connectionString: '<PUT YOUR CONNECTION STRING HERE>'
-  /* ...Other Configuration Options... */
-} });
-appInsights.loadAppInsights();
-```
-
----
-
-## Step 2: Add instrumentation
-
-Add instrumentation code to your client application.
-
-### Correlate clickstream events with search results
-
-To correlate search requests with clicks, it's necessary to have a correlation ID that relates these two distinct events. Azure AI Search provides you with a search ID when you request it with an HTTP header.
-
-Having the search ID allows correlation of the metrics emitted by Azure AI Search for the request itself, with the custom metrics you're logging in Application Insights.
-
-### [**.NET**](#tab/dotnet-correlation)
-
-```csharp
-var client = new SearchClient(new Uri("https://contoso.search.windows.net"), "hotels-sample-index", new DefaultAzureCredential());
-
-// Generate a new correlation id for logs
-string searchId = Guid.NewGuid().ToString();
-string searchText = "*";
-SearchResults<SearchDocument> searchResults;
-
-// Set correlation id for search request
-using (HttpPipeline.CreateClientRequestIdScope(clientRequestId: searchId))
-{
-    searchResults = client.Search<SearchDocument>(searchText, options: new SearchOptions { IncludeTotalCount = true } );
-}
-```
-
-### [**JavaScript**](#tab/javascript-correlation)
-
-```javascript
-const searchId = uuidv4();
-const searchText = "*";
-const searchResults = await searchClient.search(searchText, { includeTotalCount: true, customHeaders: { "x-ms-client-request-id": searchId }});
-const properties = {
-    searchId: searchId,
-    serviceName: "<PUT YOUR SEARCH SERVICE NAME HERE, example contoso-search>",
-    indexName: "<PUT YOUR INDEX NAME HERE>",
-    searchText: searchText,
-    resultsCount: searchResults.count
-};
-appInsights.trackEvent({ name: "search" }, properties);
-```
-
----
-
-### Log custom events
-
-Every time that a search request is issued by a user, you should log that as a search event with the following schema on an [Application Insights custom event](/azure/azure-monitor/app/api-custom-events-metrics). Remember to log only user-generated search queries.
-
-+ **SearchId**: (guid) unique identifier of the search query (built into the search response)
-+ **SearchServiceName**: (string) search service name
-+ **IndexName**: (string) search service index to be queried
-+ **SearchText**: (string) search terms entered by the user
-+ **ResultCount**: (int) number of documents that were returned (built into the search response)
-
-> [!NOTE]
-> Request the count of user generated queries by adding `$count=true` to your search query. For more information, see [Search Documents (REST)](/rest/api/searchservice/documents/search-post#searchrequest).
->
-
-### [**.NET**](#tab/dotnet-properties)
-
-```csharp
-// Create properties for telemetry
-var properties = new Dictionary<string, string>
-{
-    ["searchId"] = searchId,
-    ["serviceName"] = "<PUT YOUR SEARCH SERVICE NAME HERE, example: contoso-search>",
-    ["indexName"] = "<PUT YOUR INDEX NAME HERE>",
-    ["searchText"] = searchText,
-    ["resultsCount"] = searchResults.TotalCount?.ToString()
-};
-```
-
-### [**JavaScript**](#tab/javascript-properties)
-
-```javascript
-const properties = {
-    searchId: searchId,
-    serviceName: "<PUT YOUR SEARCH SERVICE NAME HERE, example contoso-search>",
-    indexName: "<PUT YOUR INDEX NAME HERE>",
-    searchText: searchText,
-    resultsCount: searchResults.count
-};
-```
-
----
-
-### Send the custom event to Application Insights
-
-Add the custom even to the *custom events* table in Application Insights. For more information, see [Application Insights API for custom events and metrics](/azure/azure-monitor/app/api-custom-events-metrics).
-
-### [**.NET**](#tab/dotnet-custom-events)
-
-```csharp
-telemetryClient.TrackEvent("search", properties);
-telemetryClient.Flush();
-```
-
-### [**JavaScript**](#tab/javascript-custom-events)
-
-```javascript
-appInsights.trackEvent({ name: "search" }, properties);
-```
-
----
-
-## Step 3: Review logs
-
-Use any of the approaches supported by Application Insights for viewing custom events.
-
-+ [Create or edit an Azure Workbook](/azure/azure-monitor/visualize/workbooks-create-workbook)
-+ [Create and share dashboards of Log Analytics data](/azure/azure-monitor/visualize/tutorial-logs-dashboards)
-+ [Integrate Log Analytics with Power BI](/azure/azure-monitor/logs/log-powerbi)
-
-## Next steps
-
-You can find more information on [Application Insights](/azure/azure-monitor/app/app-insights-overview) and visit the [pricing page](https://azure.microsoft.com/pricing/details/application-insights/) to learn more about their different service tiers.
-
-Learn more about creating reports. See [Getting started with Power BI Desktop](/power-bi/fundamentals/desktop-getting-started) for details.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "検索トラフィック分析に関するドキュメントの削除"
}
```

### Explanation
この変更は、「search-traffic-analytics.md」ファイルが完全に削除されたことを示しています。この削除により、Azure AI Searchにおける検索トラフィック分析の実施方法や、そのために必要な手順、依存関係、使用するライブラリなどに関する情報が失われました。

具体的な内容としては、以下のセクションが含まれていましたが、全て削除されています：
- 検索トラフィック分析の概要、目的、およびその重要性
- Application Insightsを使用したユーザーインタラクションの計測方法
- テレメトリクライアントの追加やイベントの追跡に必要なコードスニペット
- 検索リクエストとユーザーのクリックストリームイベントを相関させる方法
- 検索トラフィック分析を実施するための事前条件や必要なツール

この削除は、ドキュメントの整合性や内容の見直しに基づいて行われた可能性があり、特にこの情報を必要とするユーザーには影響を与えるものとなります。今後、同様の情報を得るためには別のリソースや更新されたドキュメントを参照する必要があるでしょう。このような大規模な削除は、関連する機能やサービスの変更を反映しているかもしれません。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,6 @@ items:
 - name: Azure AI Search Documentation
   href: index.yml
 - name: Overview
-  expanded: true
   items:
   - name: What's Azure AI Search?
     href: search-what-is-azure-search.md
@@ -14,6 +13,7 @@ items:
     href: search-try-for-free.md
   - name: FAQ
     href: search-faq-frequently-asked-questions.yml
+  expanded: true
 - name: Quickstarts
   items:
   - name: Vector search
@@ -24,7 +24,7 @@ items:
     href: search-get-started-text.md
   - name: Semantic ranking
     href: search-get-started-semantic.md
-  - name: Chat with your data 
+  - name: Chat with your data
     href: /azure/ai-services/openai/use-your-data-quickstart?context=/azure/search/context/context
   - name: Connect without keys
     href: search-get-started-rbac.md
@@ -51,7 +51,7 @@ items:
   - name: Deployment
     items:
     - name: ARM template
-      displayName: Resource Manager 
+      displayName: Resource Manager
       href: search-get-started-arm.md
     - name: Bicep
       displayName: ARM, Resource Manager, Template
@@ -65,17 +65,17 @@ items:
     - name: Add search to ASP.NET Core (MVC)
       href: tutorial-csharp-create-mvc-app.md
     - name: Add search to static web apps
-      items: 
-        - name: Overview
-          href: tutorial-csharp-overview.md
-        - name: Create a search index
-          href: tutorial-csharp-create-load-index.md
-        - name: Deploy static web app
-          href: tutorial-csharp-deploy-static-web-app.md
-        - name: Explore the code
-          href: tutorial-csharp-search-query-integration.md          
-    - name: Query from Power Apps   
-      href: search-howto-powerapps.md     
+      items:
+      - name: Overview
+        href: tutorial-csharp-overview.md
+      - name: Create a search index
+        href: tutorial-csharp-create-load-index.md
+      - name: Deploy static web app
+        href: tutorial-csharp-deploy-static-web-app.md
+      - name: Explore the code
+        href: tutorial-csharp-search-query-integration.md
+    - name: Query from Power Apps
+      href: search-howto-powerapps.md
   - name: Indexing tutorials
     items:
     - name: Index any data
@@ -88,7 +88,7 @@ items:
       href: search-semi-structured-data.md
     - name: Index Markdown in Azure blobs
       href: search-markdown-data-tutorial.md
-    - name: Index multiple Azure data sources 
+    - name: Index multiple Azure data sources
       href: tutorial-multiple-data-sources.md
     - name: Index encrypted blobs
       href: search-howto-index-encrypted-blobs.md
@@ -140,7 +140,7 @@ items:
       href: search-what-is-an-index.md
     - name: Vector store
       href: vector-store.md
-    - name: Knowledge store 
+    - name: Knowledge store
       href: knowledge-store-concept-intro.md
     - name: Data import strategies
       href: search-what-is-data-import.md
@@ -267,44 +267,44 @@ items:
         href: cognitive-search-common-errors-warnings.md
     - name: Data sources (indexers)
       items:
-        - name: Data sources gallery
-          href: search-data-sources-gallery.md
-        - name: Azure Storage
-          items:
-          - name: Search over blobs
-            href: search-blob-storage-integration.md
-          - name: ADLS Gen2
-            href: search-howto-index-azure-data-lake-storage.md
-          - name: Blobs
-            href: search-howto-indexing-azure-blob-storage.md
-          - name: Files
-            href: search-file-storage-integration.md
-          - name: Tables
-            href: search-howto-indexing-azure-tables.md
-          - name: Index changed and deleted content
-            href: search-howto-index-changed-deleted-blobs.md
-        - name: Azure Cosmos DB
-          items:
-          - name: Azure Cosmos DB for NoSQL
-            href: search-howto-index-cosmosdb.md
-          - name: Azure Cosmos DB for MongoDB
-            href: search-howto-index-cosmosdb-mongodb.md
-          - name: Azure Cosmos DB for Apache Gremlin
-            href: search-howto-index-cosmosdb-gremlin.md
-        - name: Azure DB for MySQL
-          href: search-howto-index-mysql.md
-        - name: Azure SQL
-          items:
-          - name: Azure SQL Databases
-            href: search-how-to-index-sql-database.md
-          - name: Azure SQL Managed Instances
-            href: search-how-to-index-sql-managed-instance.md
-          - name: Azure SQL Server VMs
-            href: search-how-to-index-sql-server.md
-        - name: OneLake files
-          href: search-how-to-index-onelake-files.md
-        - name: SharePoint Online
-          href: search-howto-index-sharepoint-online.md
+      - name: Data sources gallery
+        href: search-data-sources-gallery.md
+      - name: Azure Storage
+        items:
+        - name: Search over blobs
+          href: search-blob-storage-integration.md
+        - name: ADLS Gen2
+          href: search-howto-index-azure-data-lake-storage.md
+        - name: Blobs
+          href: search-howto-indexing-azure-blob-storage.md
+        - name: Files
+          href: search-file-storage-integration.md
+        - name: Tables
+          href: search-howto-indexing-azure-tables.md
+        - name: Index changed and deleted content
+          href: search-howto-index-changed-deleted-blobs.md
+      - name: Azure Cosmos DB
+        items:
+        - name: Azure Cosmos DB for NoSQL
+          href: search-howto-index-cosmosdb.md
+        - name: Azure Cosmos DB for MongoDB
+          href: search-howto-index-cosmosdb-mongodb.md
+        - name: Azure Cosmos DB for Apache Gremlin
+          href: search-howto-index-cosmosdb-gremlin.md
+      - name: Azure DB for MySQL
+        href: search-howto-index-mysql.md
+      - name: Azure SQL
+        items:
+        - name: Azure SQL Databases
+          href: search-how-to-index-sql-database.md
+        - name: Azure SQL Managed Instances
+          href: search-how-to-index-sql-managed-instance.md
+        - name: Azure SQL Server VMs
+          href: search-how-to-index-sql-server.md
+      - name: OneLake files
+        href: search-how-to-index-onelake-files.md
+      - name: SharePoint Online
+        href: search-howto-index-sharepoint-online.md
     - name: Skillsets
       items:
       - name: Create a skillset
@@ -342,7 +342,7 @@ items:
     - name: Chunk documents
       href: vector-search-how-to-chunk-documents.md
     - name: Chunk and vectorize by document layout
-      href: search-how-to-semantic-chunking.md   
+      href: search-how-to-semantic-chunking.md
     - name: Generate embeddings
       href: vector-search-how-to-generate-embeddings.md
     - name: Use embedding models from Azure AI Foundry
@@ -412,7 +412,7 @@ items:
         href: search-query-troubleshoot-collection-filters.md
       - name: Normalize text for filters
         href: search-normalizers.md
-    - name: Search results 
+    - name: Search results
       items:
       - name: Page, sort, and shape results
         href: search-pagination-page-layout.md
@@ -435,7 +435,7 @@ items:
     - name: Configure BM25 ranking
       href: index-ranking-similarity.md
     - name: Enable or disable semantic ranker
-      href: semantic-how-to-enable-disable.md      
+      href: semantic-how-to-enable-disable.md
     - name: Configure semantic ranker
       href: semantic-how-to-configure.md
     - name: Add semantic ranking to queries
@@ -522,14 +522,10 @@ items:
       href: search-monitor-queries.md
     - name: Monitor indexer-based indexing
       href: search-howto-monitor-indexers.md
-    - name: Monitor client-side interactions
-      href: search-traffic-analytics.md
     - name: Visualize resource logs
       href: search-monitor-logs-powerbi.md
     - name: Performance analysis
       href: search-performance-analysis.md
-    - name: Performance benchmarks
-      href: performance-benchmarks.md
     - name: Tips for better performance
       href: search-performance-tips.md
   - name: Knowledge store
@@ -543,7 +539,7 @@ items:
     - name: Shape data
       href: knowledge-store-projection-shape.md
     - name: Define projections
-      href: knowledge-store-projections-examples.md 
+      href: knowledge-store-projections-examples.md
     - name: Projection example
       href: knowledge-store-projection-example-long.md
     - name: Connect with Power BI
@@ -633,7 +629,7 @@ items:
     - name: Azure CLI
       href: /cli/azure/search
     - name: Azure PowerShell
-      href: /powershell/module/az.search 
+      href: /powershell/module/az.search
     - name: Azure Resource Manager template
       href: /azure/templates/microsoft.search/searchservices
     - name: Azure Policy built-ins
@@ -650,27 +646,27 @@ items:
     - name: Azure AI resource skills
       items:
       - name: Document Layout skill
-        href: cognitive-search-skill-document-intelligence-layout.md  
+        href: cognitive-search-skill-document-intelligence-layout.md
       - name: Entity Linking (v3)
         href: cognitive-search-skill-entity-linking-v3.md
       - name: Entity Recognition (v3)
         href: cognitive-search-skill-entity-recognition-v3.md
       - name: Image Analysis
         href: cognitive-search-skill-image-analysis.md
-      - name: Key Phrase Extraction 
+      - name: Key Phrase Extraction
         href: cognitive-search-skill-keyphrases.md
       - name: Language Detection
         href: cognitive-search-skill-language-detection.md
       - name: OCR
         href: cognitive-search-skill-ocr.md
       - name: PII Detection
-        href: cognitive-search-skill-pii-detection.md  
+        href: cognitive-search-skill-pii-detection.md
       - name: Sentiment (v3)
         href: cognitive-search-skill-sentiment-v3.md
       - name: Text Translation
         href: cognitive-search-skill-text-translation.md
       - name: AI Vision multimodal embeddings
-        href: cognitive-search-skill-vision-vectorize.md      
+        href: cognitive-search-skill-vision-vectorize.md
     - name: Azure AI Search utility skills (nonbillable)
       items:
       - name: Conditional
@@ -686,7 +682,7 @@ items:
     - name: Azure OpenAI skills
       items:
       - name: Azure OpenAI Embedding
-        href: cognitive-search-skill-azure-openai-embedding.md 
+        href: cognitive-search-skill-azure-openai-embedding.md
     - name: Custom skills
       items:
       - name: Azure Machine Learning (AML)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の形式と構成の改善"
}
```

### Explanation
この変更は、「toc.yml」ファイルの目次に関する修正であり、全体としての構造とフォーマットの改善を目的としています。ファイルの内容には項目の追加や整形の変更が含まれており、読みやすさと整理の向上が図られています。

具体的な変更点は以下の通りです：
- 一部の項目の「expanded」プロパティが見直され、整合性が保たれました。
- 各項目の前後で不必要な空白が削除され、コードがクリーンになりました。
- 一部のセクション内で、リスト項目のネーミングやリンクがより明確に整理され、情報が一貫して配置されています。
- 「データソース」や「スキルセット」などのセクション内で、サブ項目が明確に構造化され、各リソースへのリンクが再配置されました。
- 不要な項目が削除され、情報の濃度が向上しました。

この更新により、ユーザーは目次を通じてリソースをより簡単にナビゲートできるようになり、関連情報へのアクセスが迅速に行えるようになります。目次の整理は、全体的なユーザーエクスペリエンスを向上させることで、ドキュメンテーションの有用性を高めることに寄与しています。

## articles/search/vector-search-filters.md{#item-f47c2b}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 08/19/2024
+ms.date: 02/24/2025
 ---
 
 # Add a filter in a vector query in Azure AI Search
@@ -26,7 +26,7 @@ You can also use [Search Explorer](search-get-started-portal-import-vectors.md#c
 
 ## How filtering works in a vector query
 
-Filters apply to `filterable` nonvector fields, either a string field or numeric, to include or exclude search documents based on filter criteria. Although a vector field isn't filterable itself, filters can be applied to other fields in the same index, including or excluding the documents that also contain vector fields.
+Filters apply to `filterable` *nonvector* fields, either a string field or numeric, to include or exclude search documents based on filter criteria. Although a vector field isn't filterable itself, filters can be applied to other nonvector fields in the same index, including or excluding the documents that also happen to contain vector fields you're searching on.
 
 Filters are applied before or after query execution based on the `vectorFilterMode` parameter.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルクエリにおけるフィルターの説明の明確化"
}
```

### Explanation
この変更は、「vector-search-filters.md」ファイル内のいくつかの文言を修正し、フィルターの動作に関する説明を明確化したものです。追加および削除された行は少ないものの、フィルターがどのように機能するかをより具体的に説明することで、ユーザーの理解を助けることを目的としています。

具体的な変更点は以下の通りです：
- 文中の「nonvector」に強調（イタリック）を加えることで、フィルターが適用されるフィールドの特性を際立たせています。
- 説明では、フィルターが適用可能な「非ベクトルフィールド」を明確に示しており、元のフィールドの説明から一部の文言が修正され、より明確に表現されています。
- フィルターの適用が、クエリ実行の前または後に行われるという重要な文脈が維持されており、これは「vectorFilterMode」パラメータによって制御されます。

この変更により、ユーザーはベクトルクエリに関するフィルタリングのメカニズムについて、より具体的かつ正確な情報を得ることができ、実施する際の信頼性が高まるでしょう。文言の小さな修正ですが、技術文書としての精度と明快さが向上しています。

## articles/search/vector-search-integrated-vectorization.md{#item-48219d}

<details>
<summary>Diff</summary>
````diff
@@ -1,38 +1,37 @@
 ---
 title: Integrated vectorization
 titleSuffix: Azure AI Search
-description: Add a data chunking and embedding step in an Azure AI Search skillset to vectorize content during indexing.
+description: Add a vector embedding step in an Azure AI Search skillset to vectorize content during indexing or queries.
 
 author: heidisteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 09/04/2024
+ms.date: 02/24/2025
 ---
 
-# Integrated data chunking and embedding in Azure AI Search
+# Integrated vector embedding in Azure AI Search
 
 Integrated vectorization is an extension of the indexing and query pipelines in Azure AI Search. It adds the following capabilities:
 
-+ Data chunking during indexing
-+ Text-to-vector conversion during indexing
-+ Text-to-vector conversion during queries
++ Vector encoding during indexing
++ Vector encoding during queries
 
-Data chunking isn't a hard requirement, but unless your raw documents are small, chunking is necessary for meeting the token input requirements of embedding models.
+[Data chunking](vector-search-how-to-chunk-documents.md) isn't a hard requirement, but unless your raw documents are small, chunking is necessary for meeting the token input requirements of embedding models.
 
-Vector conversions are one-way: text-to-vector. There's no vector-to-text conversion for queries or results (for example, you can't convert a vector result to a human-readable string).
+Vector conversions are one-way: nonvector-to-vector. For example, there's no vector-to-text conversion for queries or results, such as converting a vector result to a human-readable string, which is why indexes contain both vector and nonvector fields.
 
-Integrated data chunking and vectorization speeds up the development and minimizes maintenance tasks during data ingestion and query time because there are fewer external components to configure and manage. This capability is now generally available.
+Integrated vectorization speeds up the development and minimizes maintenance tasks during data ingestion and query time because there are fewer operations that you have to implement manually. This capability is now generally available.
 
 ## Using integrated vectorization during indexing
 
-For data chunking and text-to-vector conversions, you're taking a dependency on the following components:
+For integrated data chunking and vector conversions, you're taking a dependency on the following components:
 
-+ [An indexer](search-indexer-overview.md), which retrieves raw data from a [supported data source](search-indexer-overview.md#supported-data-sources) and serves as the pipeline engine.
++ [An indexer](search-indexer-overview.md), which retrieves raw data from a [supported data source](search-indexer-overview.md#supported-data-sources) and drives the pipeline engine.
 
-+ [A vector index](search-what-is-an-index.md) to receive the chunked and vectorized content.
++ [A search index](search-what-is-an-index.md) to receive the chunked and vectorized content.
 
 + [A skillset](cognitive-search-working-with-skillsets.md) configured for:
 
@@ -94,10 +93,6 @@ Data chunking (Text Split skill) is free and available on all Azure AI services
 
 + Combine vector and text fields for hybrid search, with or without semantic ranking. Integrated vectorization simplifies all of the [scenarios supported by vector search](vector-search-overview.md#what-scenarios-can-vector-search-support).
 
-## When to use integrated vectorization
-
-We recommend using the built-in vectorization support of Azure AI Foundry. If this approach doesn't meet your needs, you can create indexers and skillsets that invoke integrated vectorization using the programmatic interfaces of Azure AI Search.
-
 ## How to use integrated vectorization
 
 For query-only vectorization:
@@ -146,7 +141,7 @@ Here are some of the key benefits of the integrated vectorization:
 
 + Automate indexing end-to-end. When data changes in the source (such as in Azure Storage, Azure SQL, or Cosmos DB), the indexer can move those updates through the entire pipeline, from retrieval, to document cracking, through optional AI-enrichment, data chunking, vectorization, and indexing.
 
-+ Batching and retry logic is built in (non-configurable). Azure AI Search has internal retry policies for throttling errors that surface due to the Azure OpenAI endpoint maxing out on token quotas for the embedding model. We recommend putting the indexer on a schedule (for example, every 5 minutes) so the indexer can process any calls that were throttled by the Azure OpenAI endpoint despite of the retry policies.
++ Batching and retry logic is built in (non-configurable). Azure AI Search has internal retry policies for throttling errors that surface due to the Azure OpenAI endpoint maxing out on token quotas for the embedding model. We recommend putting the indexer on a schedule (for example, every 5 minutes) so the indexer can process any calls that are throttled by the Azure OpenAI endpoint despite of the retry policies.
 
 + Projecting chunked content to secondary indexes. Secondary indexes are created as you would any search index (a schema with fields and other constructs), but they're populated in tandem with a primary index by an indexer. Content from each source document flows to fields in primary and secondary indexes during the same indexing run. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "統合ベクトル化の説明の調整"
}
```

### Explanation
この変更は、「vector-search-integrated-vectorization.md」ファイルの内容を修正し、統合ベクトル化に関する情報を最新の内容に更新することを目的としています。主な変更点は、説明の明確化や用語の標準化であり、一部の文言がより具体的になるように調整されています。

具体的な変更点は以下の通りです：
- 概要説明が「データチャンク化と埋め込みステップ」に関するフィールドから「ベクトル埋め込みステップ」に簡潔に変更され、インデックス作成時やクエリ時の内容ベクトル化が明示されました。
- 「データチャンク化」を「ベクトルエンコーディング」に言い換え、用語が統一され、理解しやすくなっています。
- フィルターの説明の一部が修正され、ナーやクエリでの非ベクトル・ベクトルの対比が明示されました。
- 一部の文が再構成され、可読性が向上しました。特に、インデックスやスキルセットの運用に関する部分が明確になっています。
- 統合ベクトル化が開発を迅速化し、保守作業を最小限に抑えるという点も強調されていますが、具体的な操作が減少することに言及しています。

全体として、これらの変更により、統合ベクトル化の機能と利点がよりわかりやすくなり、ユーザーはこの機能を利用する際の理解が深まります。説明の精度向上は、実践における適用を一層容易にすることに寄与しています。

## articles/search/vector-search-overview.md{#item-56e5fa}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 08/05/2024
+ms.date: 02/24/2025
 ---
 
 # Vectors in Azure AI Search
@@ -20,7 +20,7 @@ Vector search is an approach in information retrieval that supports indexing and
 + multilingual content ("dog" in English and "hund" in German)
 + multiple content types ("dog" in plain text and a photograph of a dog in an image file)
 
-This article provides [a high-level introduction to vectors](#vector-search-concepts) in Azure AI Search. It also explains integration with other Azure services and covers [terminology and concepts](#vector-search-concepts) related to vector search development.
+This article provides [a high-level introduction to vector support](#vector-search-concepts) in Azure AI Search. It also explains integration with other Azure services and covers [terminology and concepts](#vector-search-concepts) related to vector search development.
 
 We recommend this article for background, but if you'd rather get started, follow these steps:
 
@@ -39,9 +39,9 @@ Scenarios for vector search include:
 
 + **Search across different content types (multimodal)**. Encode images and text using multimodal embeddings (for example, with [OpenAI CLIP](https://github.com/openai/CLIP) or [GPT-4 Turbo with Vision](/azure/ai-services/openai/whats-new#gpt-4-turbo-with-vision-now-available) in Azure OpenAI) and query an embedding space composed of vectors from both content types.
 
-+ [**Hybrid search**](hybrid-search-overview.md). In Azure AI Search, hybrid search refers to vector and keyword query execution in the same request. Vector support is implemented at the field level, with an index containing both vector fields and searchable text fields. The queries execute in parallel and the results are merged into a single response. Optionally, add [semantic ranking](semantic-search-overview.md) for more accuracy with L2 reranking using the same language models that power Bing.
++ [**Hybrid search**](hybrid-search-overview.md). In Azure AI Search, we define hybrid search as dual vector and keyword query execution in the same request. Vector support is implemented at the field level. If an index contains both vector and non-vector fields, you can write a query that targets both. The queries execute in parallel and the results are merged into a single response and ranked accordingly.
 
-+ **Multilingual search**. Providing a search experience in the users own language is possible through embedding models and chat models trained in multiple languages. If you need more control over translation, you can supplement with the [multi-language capabilities](search-language-support.md) that Azure AI Search supports for nonvector content, in hybrid search scenarios.
++ **Multilingual search**. Azure AI Search is designed for extensibility. If you have embedding models and chat models trained in multiple languages, you can call them through custom or built-in skills on the indexing side, or vectorizers on the query side. If you need more control over text translation, you can supplement with the [multi-language capabilities](search-language-support.md) that Azure AI Search supports for nonvector content, in hybrid search scenarios.
 
 + **Filtered vector search**. A query request can include a vector query and a [filter expression](search-filters.md). Filters apply to text and numeric fields, and are useful for metadata filters, and including or excluding search results based on filter criteria. Although a vector field isn't filterable itself, you can set up a filterable text or numeric field. The search engine can process the filter before or after the vector query executes.
 
@@ -57,11 +57,11 @@ The following diagram shows the indexing and query workflows for vector search.
 
 On the indexing side, Azure AI Search takes vector embeddings and uses a [nearest neighbors algorithm](vector-search-ranking.md) to place similar vectors close together in an index. Internally, it creates vector indexes for each vector field.
 
-How you get embeddings from your source content into Azure AI Search depends on whether you want to perform the work within an Azure AI Search indexing pipeline, or externally.  Azure AI Search offers [integrated data chunking and vectorization](vector-search-integrated-vectorization.md) in an indexer pipeline. You still provide the resources (endpoints and connection information to Azure OpenAI), but Azure AI Search makes all of the calls and handles the transitions. This approach requires an indexer, a supported data source, and a skillset that drives chunking and embedding. Otherwise, you can handle all vectorization separately, and then push prevectorized content to [vector fields](vector-search-how-to-create-index.md) in a vector store.
+How you get embeddings from your source content into Azure AI Search depends on whether you want to perform the work within an Azure AI Search indexing pipeline, or externally.  Azure AI Search offers [integrated data chunking and vectorization](vector-search-integrated-vectorization.md) in an indexer pipeline. You still provide the resources (endpoints and connection information to Azure OpenAI), but Azure AI Search makes all of the calls and handles the transitions. This approach requires an indexer, a supported data source, and a skillset that drives chunking and embedding. If you don't want to use indexers, you can handle all vectorization externally, and then push prevectorized content into [vector fields](vector-search-how-to-create-index.md) in the search index.
 
 On the query side, in your client application, you collect the query input from a user, usually through a prompt workflow. You can then add an encoding step that converts the input into a vector, and then send the vector query to your index on Azure AI Search for a similarity search. As with indexing, you can deploy the [integrated vectorization](vector-search-integrated-vectorization.md) to convert the question into a vector. For either approach, Azure AI Search returns documents with the requested `k` nearest neighbors (kNN) in the results.
 
-Azure AI Search supports [hybrid scenarios](hybrid-search-overview.md) that run vector and keyword search in parallel, returning a unified result set that often provides better results than just vector or keyword search alone. For hybrid, vector and nonvector content is ingested into the same index, for queries that run side by side.
+Azure AI Search supports [hybrid scenarios](hybrid-search-overview.md) that run vector and keyword search in parallel, returning a unified result set that often provides better results than just vector or keyword search alone. For hybrid, vector and non-vector content is ingested into the same index, for queries that run side by side.
 
 ## Availability and pricing
 
@@ -88,7 +88,7 @@ Azure AI Search is deeply integrated across the Azure AI platform. The following
 | Azure AI Foundry | In the chat with your data playground, **Add your own data** uses Azure AI Search for grounding data and conversational search. This is the easiest and fastest approach for chatting with your data. |
 | Azure OpenAI | Azure OpenAI provides embedding models and chat models. Demos and samples target the [text-embedding-ada-002](/azure/ai-services/openai/concepts/models#embeddings-models). We recommend Azure OpenAI for generating embeddings for text. |
 | Azure AI Services | [Image Retrieval Vectorize Image API(Preview)](/azure/ai-services/computer-vision/how-to/image-retrieval#call-the-vectorize-image-api) supports vectorization of image content. We recommend this API for generating embeddings for images. |
-| Azure data platforms: Azure Blob Storage, Azure Cosmos DB | You can use [indexers](search-indexer-overview.md) to automate data ingestion, and then use [integrated vectorization](vector-search-integrated-vectorization.md) to generate embeddings. Azure AI Search can automatically index vector data from two data sources: [Azure blob indexers](search-howto-indexing-azure-blob-storage.md) and [Azure Cosmos DB for NoSQL indexers](search-howto-index-cosmosdb.md). For more information, see [Add vector fields to a search index.](vector-search-how-to-create-index.md). |
+| Azure data platforms: Azure Blob Storage, Azure Cosmos DB, Azure SQL, OneLake | You can use [indexers](search-indexer-overview.md) to automate data ingestion, and then use [integrated vectorization](vector-search-integrated-vectorization.md) to generate embeddings. Azure AI Search can automatically index vector data from [Azure blob indexers](search-howto-indexing-azure-blob-storage.md), [Azure Cosmos DB for NoSQL indexers](search-howto-index-cosmosdb.md), [Azure Data Lake Storage Gen2](search-howto-index-azure-data-lake-storage.md), [Azure Table Storage](search-howto-indexing-azure-tables.md), [Fabric OneLake](search-how-to-index-onelake-files.md). For more information, see [Add vector fields to a search index.](vector-search-how-to-create-index.md). |
 
 It's also commonly used in open-source frameworks like [LangChain](https://js.langchain.com/docs/integrations/vectorstores/azure_aisearch).
 
@@ -98,7 +98,7 @@ If you're new to vectors, this section explains some core concepts.
 
 ### About vector search
 
-Vector search is a method of information retrieval where documents and queries are represented as vectors instead of plain text. In vector search, machine learning models generate the vector representations of source inputs, which can be text, images, or other content. Having a mathematic representation of content provides a common basis for search scenarios. If everything is a vector, a query can find a match in vector space, even if the associated original content is in different media or language than the query.
+Vector search is a method of information retrieval where documents and queries are represented as vectors instead of plain text. In vector search, machine learning models generate the vector representations of source inputs, which can be text, images, or other content. Having a mathematic representation of content provides a common language for comparing disparate content. If everything is a vector, a query can find a match in vector space, even if the associated original content is in different media or language than the query.
 
 ### Why use vector search
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルサーチの概要の更新"
}
```

### Explanation
この変更は、「vector-search-overview.md」ファイルの内容を更新し、Azure AI Searchにおけるベクトルサーチの概要を改善することを目的としています。文言の一部の修正と情報の整理により、より明確で簡潔な説明にしています。

主要な変更点は以下の通りです：
- ファイルの日付が「2024年8月5日」から「2025年2月24日」に更新され、最新のリリース情報を反映しています。
- 「ベクトルのサポート」という表現に変更し、コンテンツがより包括的に理解できるように改善されました。
- 複数のコンテンツ型を扱う場合や、ハイブリッド検索の定義に関して表現が洗練されました。特に、フィールドレベルでのベクトルサポートについての説明が強調されています。
- ユーザーの言語に応じた検索や、カスタムスキルを利用した多言語サポートの機能に関する表現が具体化され、理解しやすくなっています。
- 検索結果に対するフィルターの仕組みが詳しく説明され、ベクトル検索と他のフィールドに対する実用的な統合方法へと焦点が当てられています。
- 埋め込みを取得する際のプロセスについても明確化され、インデクサーを使用した場合と外部からの処理が選べることが説明されています。

これらの変更により、読者はAzure AI Searchにおけるベクトルサーチの機能や利点について、より的確に理解することができるようになりました。結果として、ユーザーはこの技術を効果的に活用するための情報を得ることができます。全体の文書の可読性と実用性が向上しています。


