---
date: '2025-05-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0ff32a6...MicrosoftDocs:cfed402
summary: |-
  このコードの差分は、Azure Cognitive Searchに関連する3つのドキュメントに対するマイナーな更新を含んでいます。アップデートには、ドキュメントインテリジェンスレイアウトに関する地域設定の強調や、ベクトル検索クエリの新しいプロパティの追加が含まれています。破壊的変更は特にありませんが、APIの使用に関する重要な制限が明確化されました。また、各ドキュメントの日付が更新され、内容が最新の状態に保たれています。

  これにより、ユーザーは最新の技術要件を理解し、適切に実装できるようサポートされています。特に、地域制限の明確化和ベクトル検索における詳細なガイドラインは、パフォーマンスと効率性を向上させるために重要であり、ユーザー体験を改善する助けとなります。全体として、これらのアップデートはAzure Cognitive Searchの利用におけるユーザー理解と満足度を高めるために重要と言えるでしょう。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0ff32a6...MicrosoftDocs:cfed402){target="_blank"}

# ハイライト
このコードの差分は、Azure Cognitive Searchに関連する3つのドキュメントに対するマイナーな更新を含んでいます。アップデートには以下のような新機能や重要な変更点が含まれています。

## 新機能
- ドキュメントインテリジェンスレイアウトに関して、Azure AI Searchサービスとのマルチサービスリソース間の地域設定が強調されました。
- ベクトル検索クエリの新しいプロパティとオプションの追加。

## 破壊的変更
- これに関連する破壊的変更は特にありませんが、APIの使用に関する重要な制限が明確化されました。

## その他の更新
- 各ドキュメントの日付が更新され、内容が最新の状態に保たれています。
- 検索制限およびクォータにおいて、ベクトルクエリのフィールド制限に関する情報が追加されました。

# インサイト
この差分により、Azure Cognitive Searchの使用においてユーザーが安心して最新の技術要件を理解し、適切に実装できるようサポートされています。特にドキュメントインテリジェンスレイアウトにおいて、地域制限の明確化により、ユーザーはマルチサービスリソースの配置を適切に計画することが可能となります。これは、異なる地域により発生する可能性のある接続問題を未然に防ぐための重要な情報です。

検索APIの制限に関する更新は、開発者がクエリを設計する際に考慮すべきポイントを具体的に示しており、特にベクトル検索におけるフィールド制限やクエリの構成に対する詳細なガイドラインは、パフォーマンスと効率性を向上させるために重要です。

また、ベクトル検索に関する更新では、新しいプロパティの導入により、より柔軟かつ効果的な検索実行が可能となります。特に`vectorQueries.k`プロパティなどの説明は、検索結果のチューニングを可能にし、より直感的なユーザー体験を提供します。このような詳細な情報は、エンドユーザーが実際に利用する際の選択肢を広げ、結果としてより適切な結果を得るための道を開くものです。

全体として、これらのアップデートはAzure Cognitive Searchの利用におけるユーザー理解と満足度を高めるために重要なものであると言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-document-intelligence-layout.md](#item-62c06f) | minor update | ドキュメントインテリジェンスレイアウトの更新 | modified | 2 | 2 | 4 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索制限およびクォータの更新 | modified | 2 | 1 | 3 | 
| [vector-search-how-to-query.md](#item-9bb93c) | minor update | ベクトル検索クエリ方法の更新 | modified | 8 | 3 | 11 | 


# Modified Contents
## articles/search/cognitive-search-skill-document-intelligence-layout.md{#item-62c06f}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: reference
-ms.date: 04/07/2025
+ms.date: 04/30/2025
 ---
 
 # Document Layout skill
@@ -26,7 +26,7 @@ The **Document Layout** skill calls the [Document Intelligence Public preview ve
 
 Supported regions varies by modality:
 
-+ In code, your skillset can call Document Intelligence through an Azure AI multi-service resource in any region that provides both AI enrichment and Document Intelligence. See [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table) to find regions that provide both *AI enrichment* in Azure AI Search and *Document Intelligence* under Azure AI services.
++ When you're using AI services keys [to attach your multi-service resource to your skillset](cognitive-search-attach-cognitive-services.md#bill-through-a-resource-key) via the REST API, both your Azure AI Search service and AI multi-service resource must be in the same region. This is only possible in the Azure regions of **East US**, **West Europe**, **North Central US**, **West US 2**. But if you're using a managed identity for [billing through a keyless connection](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection), your Azure AI Search service must be in one of the following regions: **East US**, **West Europe**, **North Central US**, **West US 2**. On the other hand, you can use AI Document Intelligence through an Azure AI multi-service resource in any region where this service is available. See [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).
 
 + In the [Import and vectorize data](search-import-data-portal.md) wizard in the Azure portal, you can enable document layout detection in the data source connection step. Document layout detection in the portal is available in the following Azure regions: **East US**, **West Europe**, **North Central US**. Create an Azure AI multi-service resource in one of these three regions to get the portal experience.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスレイアウトの更新"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-document-intelligence-layout.md`というファイルに対するマイナーな更新を含んでいます。主に、ドキュメントレイアウトスキルに関する情報が明確化され、最新の情報に更新されています。具体的には、ドキュメントインテリジェンスの使用に関連する地域制限や、Azureポータルにおけるデータソース接続時の設定の説明が追加されました。

更新された部分では、AIサービスキーを使用してマルチサービスリソースをスキルセットに接続する場合、Azure AI SearchサービスとAIマルチサービスリソースが同じ地域に配置されている必要があることが強調されています。さらに、ドキュメントレイアウト検出が利用可能な地域に関する詳細なガイダンスも提供されています。

ドキュメントの日付が2025年4月7日から2025年4月30日に更新されている点も注目すべき変更点です。全体として、これらの更新はユーザーがスキルを適切に利用するための有益な情報を提供するものです。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 04/14/2025
+ms.date: 04/30/2025
 ms.custom:
   - references_regions
   - build-2024
@@ -241,6 +241,7 @@ Indexing APIs:
 
 Query APIs:
 
++ Maximum 10 fields in a vector query
 + Maximum 32 fields in $orderby clause.
 + Maximum 100,000 characters in a search clause.
 + Maximum number of clauses in search is 3,000.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索制限およびクォータの更新"
}
```

### Explanation
この変更は、`articles/search/search-limits-quotas-capacity.md`ファイルに対するマイナーな更新を表しています。主な変更点は、検索の制限およびクォータに関する情報の更新です。特に、APIに関する制約が明確化されています。

具体的には、ベクトルクエリにおいて最大10フィールドの制限が新たに追加され、他の制限（$orderby句内の最大32フィールド、検索句内の最大100,000文字、および検索における最大3,000の句）についても触れられています。加えて、公開日が2025年4月14日から2025年4月30日に変更されており、全体としてこのドキュメントはユーザーに対して最新の技術要件を提供することを目的としています。この更新により、ユーザーは検索APIの使用に関する重要な制約を理解しやすくなっています。

## articles/search/vector-search-how-to-query.md{#item-9bb93c}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: how-to
-ms.date: 03/11/2025
+ms.date: 04/30/2025
 ---
 
 # Create a vector query in Azure AI Search
@@ -98,8 +98,11 @@ This section shows you the basic structure of a vector query. You can use the Az
 + `vectorQueries` is the construct for vector search.
 + `vectorQueries.kind` set to `vector` for a vector array, or set to `text` if the input is a string and [you have a vectorizer](#query-with-integrated-vectorization).
 + `vectorQueries.vector` is query (a vector representation of text or an image).
++ `vectorQueries.exhaustive` (optional) invokes exhaustive KNN at query time, even if the field is indexed for HNSW.
++ `vectorQueries.fields` (optional) targets specific fields for query execution (up to 10 per query).
 + `vectorQueries.weight` (optional) specifies the relative weight of each vector query included in search operations (see [Vector weighting](#vector-weighting)).
-+ `exhaustive` (optional) invokes exhaustive KNN at query time, even if the field is indexed for HNSW.
++ `vectorQueries.k` is the number of matches to return.
+
 
 In the following example, the vector is a representation of this string: "what Azure services support full text search". The query targets the `contentVector` field. The query returns `k` results. The actual vector has 1536 embeddings, so it's trimmed in this example for readability.
 
@@ -257,7 +260,9 @@ If you do want vector fields in the result, here's an example of the response st
 
 ## Multiple vector fields
 
-You can set the "vectorQueries.fields" property to multiple vector fields. The vector query executes against each vector field that you provide in the `fields` list. When querying multiple vector fields, make sure each one contains embeddings from the same embedding model, and that the query is also generated from the same embedding model.
+You can set the "vectorQueries.fields" property to multiple vector fields. The vector query executes against each vector field that you provide in the `fields` list. You can specify up to 10 fields.
+
+When querying multiple vector fields, make sure each one contains embeddings from the same embedding model, and that the query is also generated from the same embedding model.
 
 ```http
 POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索クエリ方法の更新"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-query.md`ファイルに対するマイナーな更新を示しています。主な目的は、Azure AI Searchにおけるベクトル検索クエリの作成に関する情報を最新に保つことです。

更新された内容には、`vectorQueries`の新しいプロパティやオプションが追加されています。具体的には、`vectorQueries.exhaustive`と`vectorQueries.fields`のオプションが新たに説明されており、それぞれ、クエリ時に完全なKNNを呼び出す機能や、最大10個の特定フィールドに対してクエリを実行するための設定を提供しています。また、`vectorQueries.k`プロパティが追加され、返すマッチの数を指定することができるようになっています。

さらに、日付の更新が行われ、2025年3月11日から2025年4月30日に変更されています。全体として、これらの改訂により、ユーザーはベクトル検索に関するより詳しい情報を得ることができ、実装の際に役立つガイダンスが提供されています。この改訂は、ドキュメントの内容を向上させ、ユーザー体験を改善することを目指しています。


