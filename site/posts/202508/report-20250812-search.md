---
date: '2025-08-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:236be21...MicrosoftDocs:fd2e69f
summary: このコード差分の主要なハイライトは、Azure AI Searchに関連するファイルのリダイレクトURLとコンテンツの更新、新しいマルチリージョン機能の追加、重要な信頼性に関する記事の削除です。また、TOCファイルの整理によってユーザーが情報にアクセスしやすくなるよう改善されています。新機能として、マルチリージョン展開に関する新しいファイルが追加され、破壊的変更として信頼性に関する記事が削除されました。そのほかに、リダイレクトURLの修正や文書の日付変更などが行われています。全体として、これらの変更はAzure
  AI Searchサービスのドキュメントの品質向上とユーザー体験の改善を目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:236be21...MicrosoftDocs:fd2e69f){target="_blank"}

<format>
# ハイライト

このコード差分における主なハイライトは、Azure AI Searchに関するいくつかのファイルのリダイレクトURLとコンテンツの更新、新しいマルチリージョン機能の追加、信頼性に関する重要な記事の削除などです。また、TOCファイルの整理によって、ユーザーが情報によりアクセスしやすくなるよう改善されています。

## 新機能
- 新しいファイル `articles/search/search-multi-region.md` が追加され、Azure AI Searchでのマルチリージョン展開に関する詳細情報が提供されています。

## 破壊的変更
- `articles/search/search-reliability.md` が削除されました。これは信頼性についての重要な記事であり、これまで信頼性メカニズムについて説明がされていました。

## その他の更新
- リダイレクトURLの修正、TOCファイルの再編成、画像ファイル名の変更、リンクの正確性及び文書の日付変更が含まれています。

# 洞察

今回のアップデートは、Azure AI Searchサービスのドキュメントに関していくつかの重要な改善を行っています。まず、新しいマルチリージョンソリューションの追加によって、グローバル化したアプリケーションのための高可用性と耐障害性を実現するための詳細情報が提供されました。これは、ユーザーがAzure Searchを使用してより信頼性の高いサービスを構築するのを助けるための重要な追加です。

一方で、大きな破壊的変更として信頼性に関する記事が削除されており、ユーザーは今後新しいドキュメントや参照先を確認する必要があります。信頼性に関する情報は他のリードングな記事やセクションに組み入れられるか、新たに提供されるドキュメントで補完されることが予想されます。

また、TOCの再編により、ユーザーのナビゲーションが改善され、正確で最新の情報へのアクセスが強化されました。これには信頼性に関する新しいカテゴリの追加が含まれ、情報の整合性と利便性が向上しています。

これらの変更は、Azure AI Searchサービスの利便性と有効性を高めるためにデザインされており、特にエンタープライズレベルのユーザーがこれらの更新を歓迎することになりそうです。全体として、今回の差分はドキュメントの品質を向上させ、ユーザー体験をより良好にすることを目指しています。

</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [.openpublishing.redirection.search.json](#item-8b66f9) | minor update | リダイレクトURLの変更と新しいエントリーの追加 | modified | 7 | 2 | 9 | 
| [toc.yml](#item-eeb848) | minor update | TOCファイルへの新しい項目の追加 | modified | 3 | 1 | 4 | 
| [keyless-connections.md](#item-3f0d72) | minor update | オーディエンスURLの更新 | modified | 1 | 1 | 2 | 
| [azure-function-search-traffic-mgr.png](#item-e807c0) | minor update | 画像ファイルの名前変更 | renamed | 0 | 0 | 0 | 
| [geo-redundancy.png](#item-ca8a4b) | minor update | 画像ファイルの名前変更 | renamed | 0 | 0 | 0 | 
| [geo-search-traffic-mgr.png](#item-ebb4d4) | minor update | 画像ファイルの名前変更 | renamed | 0 | 0 | 0 | 
| [scale-indexers.png](#item-f7d0a8) | minor update | 画像ファイルの名前変更 | renamed | 0 | 0 | 0 | 
| [search-create-service-portal.md](#item-f90159) | minor update | サービス ポータルに関する記事の更新 | modified | 2 | 2 | 4 | 
| [search-how-to-upgrade.md](#item-990225) | minor update | サービスのアップグレード手順に関する記事の修正 | modified | 2 | 2 | 4 | 
| [search-indexer-overview.md](#item-292796) | minor update | インデクサーの概要に関する記事の更新 | modified | 2 | 2 | 4 | 
| [search-multi-region.md](#item-14f9af) | new feature | Azure AI Searchにおけるマルチリージョンソリューションの解説記事の追加 | added | 122 | 0 | 122 | 
| [search-region-support.md](#item-25b0f1) | minor update | 地域サポートに関する記事の更新 | modified | 2 | 2 | 4 | 
| [search-reliability.md](#item-3e9b1a) | breaking change | Azure AI Searchの信頼性に関する記事の削除 | removed | 0 | 205 | 205 | 
| [search-sku-tier.md](#item-7686b8) | minor update | Azure AI SearchのSKU Tierに関する更新 | modified | 3 | 3 | 6 | 
| [toc.yml](#item-c4768f) | minor update | Azure AI Searchにおける目次の更新 | modified | 6 | 2 | 8 | 


# Modified Contents
## articles/search/.openpublishing.redirection.search.json{#item-8b66f9}

<details>
<summary>Diff</summary>
````diff
@@ -217,8 +217,8 @@
         },
         {
             "source_path_from_root": "/articles/search/search-performance-optimization.md",
-            "redirect_url": "/azure/search/search-reliability",
-            "redirect_document_id": true
+            "redirect_url": "/azure/reliability/reliability-ai-search",
+            "redirect_document_id": false
         },
         {
             "source_path_from_root": "/articles/search/cognitive-search-quickstart-ocr.md",
@@ -455,6 +455,11 @@
             "source_path_from_root": "/articles/search/search-get-started-powershell.md",
             "redirect_url": "/azure/search/search-get-started-text",
             "redirect_document_id": false
+        },
+        {
+            "source_path_from_root": "/articles/search/search-reliability.md",
+            "redirect_url": "/azure/reliability/reliability-ai-search",
+            "redirect_document_id": false
         }
     ]
   }
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リダイレクトURLの変更と新しいエントリーの追加"
}
```

### Explanation
この変更は、`articles/search/.openpublishing.redirection.search.json` ファイルに対するマイナーな更新です。主な変更点は、既存のリダイレクトURLの修正と新しいリダイレクトエントリーの追加です。

具体的には、"search-performance-optimization.md" に関連するリダイレクトURLが、以前の "/azure/search/search-reliability" から新しい "/azure/reliability/reliability-ai-search" に変更されています。また、`redirect_document_id` フラグが `true` から `false` に変更されています。

さらに、新たに "search-reliability.md" に関連するリダイレクトエントリーが追加されており、こちらも同様に "/azure/reliability/reliability-ai-search" という新しいリダイレクトURLを持っています。この修正により、ドキュメントへのリンクの整合性が向上し、ユーザーは最新の情報に簡単にアクセスできるようになります。

## articles/search/breadcrumb/toc.yml{#item-eeb848}

<details>
<summary>Diff</summary>
````diff
@@ -1,15 +1,17 @@
+items:
 - name: Azure
   tocHref: /azure/
   topicHref: /azure/index
   items:
+  - name: Search
+    tocHref: /azure/reliability
   - name: AI services
     tocHref: /azure/ai-services/
     topicHref: /azure/ai-services/index
     items:
     - name: Azure AI Search
       tocHref: /azure/search/
       topicHref: /azure/search/index
-
 - name: Azure
   tocHref: /legal/
   topicHref: /azure/index
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCファイルへの新しい項目の追加"
}
```

### Explanation
この変更は、`articles/search/breadcrumb/toc.yml` ファイルに対するマイナーな更新です。主に、TOC（Table of Contents）ファイルに新しい階層的な項目が追加されています。

具体的には、新たに "Search" という項目が追加され、そのリンクは "/azure/reliability" へ向けられています。この変更により、既存の "Azure" セクション内に "Search" セクションが追加され、ユーザーが検索関連のリソースへ簡単にアクセスできるようになります。

さらに、TOCファイルの構造が改善され、ナビゲーションがより整理されることで、全体的な使い勝手が向上しています。これにより、ユーザーが情報を見つけやすくなることを目的としています。

## articles/search/keyless-connections.md{#item-3f0d72}

<details>
<summary>Diff</summary>
````diff
@@ -185,7 +185,7 @@ from azure.search.documents import SearchClient
 from azure.identity import DefaultAzureCredential, AzureAuthorityHosts
 
 # Azure Public Cloud
-audience = "https://search.windows.net"
+audience = "[https://search.windows.net](https://search.azure.com)"
 authority = AzureAuthorityHosts.AZURE_PUBLIC_CLOUD
 
 service_endpoint = os.environ["AZURE_SEARCH_ENDPOINT"]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オーディエンスURLの更新"
}
```

### Explanation
この変更は、`articles/search/keyless-connections.md` ファイルに対するマイナーな更新です。主な変更点は、オーディエンス（`audience`）のURLが更新されたことです。

具体的には、元のオーディエンスURLである "https://search.windows.net" が、新しい形式のマークダウンリンク "[https://search.windows.net](https://search.azure.com)" に変更されています。この変更により、読みやすさが向上し、URLが適切なリンクとして表示されるようになります。

この更新は、ユーザーがAzure の検索エンドポイントへの接続を行う際の情報をより分かりやすくすることを目的としています。また、URLの更新により、正しいサービスにアクセスできることを確保しています。

## articles/search/media/search-multi-region/azure-function-search-traffic-mgr.png{#item-e807c0}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの名前変更"
}
```

### Explanation
この変更は、`articles/search/media/search-multi-region/azure-function-search-traffic-mgr.png` という画像ファイルの名称変更に関するものです。元のファイル名は `articles/search/media/search-reliability/azure-function-search-traffic-mgr.png` です。

このファイル名の変更は、画像がどのコンテンツをより正確に表しているかに基づいて行われたと考えられます。具体的には、コンテキストが「マルチリージョン検索」に合わせて更新されたことを示唆しています。このような名称変更は、資源の整理や関連性の向上を目的とし、読者が関連するコンテンツを見つけやすくするために重要です。

この変更に伴い、実際のファイルの内容は変更されていないため、視覚的な情報には影響がありません。

## articles/search/media/search-multi-region/geo-redundancy.png{#item-ca8a4b}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの名前変更"
}
```

### Explanation
この変更は、`articles/search/media/search-multi-region/geo-redundancy.png` という画像ファイルの名称変更に関するものです。元のファイル名は `articles/search/media/search-reliability/geo-redundancy.png` でした。

ファイル名の変更は、画像が表す内容やコンテキストに沿ったものであることを反映しています。具体的には、検索の「マルチリージョン」に関連する情報を明示するために、より適切な名称に更新されたと考えられます。このようなファイル名の見直しは、資源を整理し、読者が関連内容を容易に見つけられるようにするために重要です。

なお、ファイルの内容自体には変更がなく、視覚的情報もそのまま保持されています。これにより、コンテンツの一貫性が維持されます。

## articles/search/media/search-multi-region/geo-search-traffic-mgr.png{#item-ebb4d4}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの名前変更"
}
```

### Explanation
この変更は、`articles/search/media/search-multi-region/geo-search-traffic-mgr.png` という画像ファイルの名称変更を示しています。元のファイル名は `articles/search/media/search-reliability/geo-search-traffic-mgr.png` でした。

ファイル名の変更は、画像の内容や関連するコンテキストを反映するために行われたもので、特に「マルチリージョン検索」という新しいテーマに合わせたものと考えられます。このような名称変更は、情報の整理やユーザーが資料を効率的に探しやすくするために重要です。

ファイルの内容自体には変更がなく、視覚的情報もそのまま維持されています。この変更により、コンテンツの一貫性が保たれ、関連情報がより明確にユーザーに伝わるようになります。

## articles/search/media/search-multi-region/scale-indexers.png{#item-f7d0a8}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの名前変更"
}
```

### Explanation
この変更は、`articles/search/media/search-multi-region/scale-indexers.png` という画像ファイルの名称変更を示しています。元のファイル名は `articles/search/media/search-reliability/scale-indexers.png` でした。

ファイル名の変更は、画像が持つ意味や関連するコンテキストを更新するために行われます。具体的には、「マルチリージョン検索」に関連する情報を一般的に強調するためのもので、この新しい名前は内容の理解を助けることを目的としています。このような変更によって、リソースが整理され、ユーザーが必要な情報を素早く見つけられるようになります。

なお、ファイルの内容自体には変更はなく、視覚的な要素も保持されています。そのため、修正後もコンテンツの一貫性が維持されています。

## articles/search/search-create-service-portal.md{#item-f90159}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: how-to
-ms.date: 08/01/2025
+ms.date: 08/08/2025
 ms.custom:
   - references_regions
   - build-2024
@@ -115,7 +115,7 @@ In most cases, choose a region near you, unless any of the following apply:
 
 1. Do you have a specific tier in mind? Check [region availability by tier](search-sku-tier.md#region-availability-by-tier).
 
-1. Do you have business continuity and disaster recovery (BCDR) requirements? Create two or more search services in [regional pairs](/azure/reliability/cross-region-replication-azure#azure-paired-regions) within [availability zones](search-reliability.md#availability-zones). For example, if you're operating in North America, you might choose East US and West US, or North Central US and South Central US, for each search service.
+1. Do you have business continuity and disaster recovery (BCDR) requirements? Create two or more search services in [regional pairs](/azure/reliability/cross-region-replication-azure#azure-paired-regions), each with two or more replicas for [availability zones](/azure/reliability/reliability-ai-search#availability-zone-support). For example, if you're operating in North America, you might choose East US and West US, or North Central US and South Central US, for each search service.
 
 1. Do you need [AI enrichment](cognitive-search-concept-intro.md), [integrated data chunking and vectorization](vector-search-integrated-vectorization.md), or [multimodal search](multimodal-search-overview.md)? For [billing purposes](cognitive-search-attach-cognitive-services.md), Azure AI Search and Azure AI services multi-service must coexist in the same region.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス ポータルに関する記事の更新"
}
```

### Explanation
この変更は、`articles/search/search-create-service-portal.md` というMarkdownファイルに対する修正を示しています。具体的には、2行が追加され、2行が削除され、合計で4つの変更が加えられています。

主な変更点は以下の通りです：

1. **日付の更新**: ドキュメントの更新日が `08/01/2025` から `08/08/2025` に変更されました。これにより、文書の最新性が強調されています。
   
2. **BCDR要件の記述改善**: ビジネス継続性と災害復旧（BCDR）要件に関する説明が明確にされ、サーチサービスの地域ペアにおいて「二つ以上のレプリカ」を持つように求める記述に修正されました。これにより、可用性ゾーンに対するサポートを明示しています。

これらの変更は、情報の正確性と明瞭さを向上させ、ユーザーがサービスを利用する際の理解を助けることを目的としています。全体として、この記事は最新の業界標準とベストプラクティスに沿った内容となっています。

## articles/search/search-how-to-upgrade.md{#item-990225}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: how-to
 ms.custom: references_regions
-ms.date: 08/01/2025
+ms.date: 08/08/2025
 ---
 
 # Upgrade your Azure AI Search service in the Azure portal
@@ -76,7 +76,7 @@ The date you created your service partially determines its [upgrade eligibility]
 
 You can't undo a service upgrade. Before you proceed, make sure that you want to permanently increase the [storage limit](#higher-storage-limits) and [vector index size](#higher-vector-limits) of your search service. We recommend that you test this operation in a nonproduction environment.
 
-The availability of your search service during an upgrade depends on how many replicas you've provisioned. With two or more replicas, your service remains available while one replica is updated. For more information, see [Reliability in Azure AI Search](search-reliability.md).
+The availability of your search service during an upgrade depends on how many replicas you've provisioned. With two or more replicas, your service remains available while one replica is updated. For more information, see [Reliability in Azure AI Search](/azure/reliability/reliability-ai-search).
 
 To upgrade your service:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービスのアップグレード手順に関する記事の修正"
}
```

### Explanation
この変更は、`articles/search/search-how-to-upgrade.md` というMarkdownファイルに対する修正を示しています。このファイルでは、Azure AI Searchサービスのアップグレード手順に関する情報が提供されています。合計で4つの変更があり、2行が追加され、2行が削除されています。

主な変更点は以下の通りです：

1. **日付の更新**: ドキュメントの最終更新日が `08/01/2025` から `08/08/2025` に変更されました。この変更により、文書が最新の情報を反映していることが保証されます。
   
2. **リンクの正確性**: サービスのアップグレード中の可用性に関する説明の中で、関連リンクがより正確に修正されました。「[Reliability in Azure AI Search](search-reliability.md)」から、「[Reliability in Azure AI Search](/azure/reliability/reliability-ai-search)」に変更され、利用者が正確な情報にアクセスしやすくなっています。

これらの修正は、文書の正確性と使いやすさを向上させ、ユーザーがAzure AI Searchサービスのアップグレードを行う際に必要な情報を明確に理解できるようにすることを目的としています。全体として、この記事は最新のアップグレード手順と関連情報を提供しています。

## articles/search/search-indexer-overview.md{#item-292796}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 04/18/2025
+ms.date: 06/23/2025
 ---
 
 # Indexers in Azure AI Search
@@ -32,7 +32,7 @@ You can use an indexer as the sole means for data ingestion, or in combination w
 |----------|---------|
 | Single data source | This pattern is the simplest: one data source is the sole content provider for a search index. Most supported data sources provide some form of change detection so that subsequent indexer runs pick up the difference when content is added or updated in the source. |
 | Multiple data sources | An indexer specification can have only one data source, but the search index itself can accept content from multiple sources, where each indexer job brings new content from a different data provider. Each source can contribute its share of full documents, or populate selected fields in each document. For a closer look at this scenario, see [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md). |
-| Multiple indexers | Multiple data sources are typically paired with multiple indexers if you need to vary run time parameters, the schedule, or field mappings. </br></br>[Cross-region scale out of Azure AI Search](search-reliability.md#data-sync) is a variation of this scenario. You might have copies of the same search index in different regions. To synchronize search index content, you could have multiple indexers pulling from the same data source, where each indexer targets a different search index in each region.</br></br>[Parallel indexing](search-howto-large-index.md#parallel-indexing) of very large data sets also requires a multi-indexer strategy, where each indexer targets a subset of the data. |
+| Multiple indexers | Multiple data sources are typically paired with multiple indexers if you need to vary run time parameters, the schedule, or field mappings. </br></br>[Cross-region scale out of Azure AI Search](search-multi-region.md#data-synchronization) is a variation of this scenario. You might have copies of the same search index in different regions. To synchronize search index content, you could have multiple indexers pulling from the same data source, where each indexer targets a different search index in each region.</br></br>[Parallel indexing](search-howto-large-index.md#parallel-indexing) of very large data sets also requires a multi-indexer strategy, where each indexer targets a subset of the data. |
 | Content transformation | Indexers drive [skillset execution and AI enrichment](cognitive-search-concept-intro.md). Content transforms are defined in a [skillset](cognitive-search-working-with-skillsets.md) that you attach to the indexer. You can use skills to [incorporate data chunking and vectorization](vector-search-integrated-vectorization.md).|
 
  You should plan on creating one indexer for every target index and data source combination. You can have multiple indexers writing into the same index, and you can reuse the same data source for multiple indexers. However, an indexer can only consume one data source at a time, and can only write to a single index. As the following graphic illustrates, one data source provides input to one indexer, which then populates a single index:  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーの概要に関する記事の更新"
}
```

### Explanation
この変更は、`articles/search/search-indexer-overview.md` というMarkdownファイルに対する修正を示しています。このファイルでは、Azure AI Searchにおけるインデクサーの機能と利用方法についての情報が提供されています。合計で4つの変更があり、2行が追加され、2行が削除されています。

主な変更点は以下の通りです：

1. **日付の更新**: ドキュメントの最終更新日が `04/18/2025` から `06/23/2025` に変更されました。この更新により、ユーザーはこの情報が最新であることを確認できます。

2. **リンクの修正**: インデクサー関連の情報にアクセスするためのリンクが修正されました。「[Cross-region scale out of Azure AI Search](search-reliability.md#data-sync)」というリンクは、「[Cross-region scale out of Azure AI Search](search-multi-region.md#data-synchronization)」に変更され、最新の情報源を指し示すようになっています。この変更により、ユーザーは正確で関連性の高い情報を得ることができます。

これらの修正は、文書の正確性を向上させ、利用者がAzure AI Searchのインデクサーに関する理解を深めるための助けとなります。全体として、この記事はAzure AI Searchのインデクサーの使用に関する重要な情報を提供し、ユーザーが効率的にサービスを利用できるようサポートしています。

## articles/search/search-multi-region.md{#item-14f9af}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,122 @@
+---
+title: Multi-Region Solutions in Azure AI Search
+titleSuffix: Azure AI Search
+description: Learn about multi-region deployments in Azure AI Search, including data synchronization and request failover.
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: conceptual
+ms.date: 08/08/2025
+---
+
+# Multi-region deployments in Azure AI Search
+
+Although Azure AI Search is a single-region service, you can achieve higher availability and resiliency by deploying multiple search services with identical configurations and content across multiple regions.
+
+This article describes the components of a multi-region solution, which relies on your custom script or code to handle failover if a service becomes unavailable.
+
+For more information about the reliability features of Azure AI Search, including intra-regional resiliency via availability zones, see [Reliability in Azure AI Search](/azure/reliability/reliability-ai-search).
+
+## Why use multiple regions?
+
+If you need two or more search services, creating them in different regions can meet the following operational requirements:
+
++ **Resiliency to region outages**. If there's an outage, Azure AI Search doesn't provide instant failover to another region.
+
++ **Fast performance for a globally distributed application**. If indexing and query requests come from around the world, users who are closest to the host data center experience faster performance. Creating more services in regions with close proximity to these users can equalize performance for everyone.
+
+## Multi-region architecture
+
+In a multi-region setup, two or more search services are located in different regions and have synchronized indexes. Users are automatically routed to the service with the lowest latency.
+
+Azure AI Search doesn't provide an automated method of index replication across regions. However, you can synchronize data using [push or pull model indexing](search-what-is-data-import.md), both of which are described in the following section. You can also add Azure Traffic Manager or another load balancer for [request redirection](#request-failover-and-redirection).
+
+The following diagram illustrates a geo-distributed set of search services:
+
+:::image type="content" source="media/search-multi-region/geo-redundancy.png" alt-text="Diagram that shows a cross-tab view of services by region." border="true" lightbox="media/search-multi-region/geo-redundancy.png":::
+
+> [!TIP]
+> For a complete implementation, see the [Bicep sample](https://github.com/Azure-Samples/azure-search-multiple-regions) on GitHub. The sample deploys a fully configured, multi-region search solution that can be modified to your regions and indexing strategies.
+
+## Data synchronization
+
+To synchronize two or more distinct search services, you can either:
+
++ Push content into an index using [Documents - Index (REST API)](/rest/api/searchservice/documents/) or an equivalent API in the Azure SDKs.
++ Pull content into an index using an [indexer](search-indexer-overview.md).
+
+### [Push APIs](#tab/push-apis)
+
+If you use the REST APIs to [push content into your index](search-what-is-data-import.md#pushing-data-to-an-index), you can synchronize multiple search services by sending updates to each service whenever changes occur. Ensure that your code handles cases in which an update fails for one service but succeeds for other services.
+
+### [Pull APIs (Indexers)](#tab/pull-apis)
+
+If you have an indexer on one search service, you can create a second indexer on a second service to reference the same data source. Each service in each region has its own indexer and target index. Although the indexes are independent and store their own copies of the data, they remain synchronized because the indexers pull from the same source.
+
+The following diagram illustrates this architecture:
+
+:::image type="content" source="media/search-multi-region/scale-indexers.png" alt-text="Diagram of a single data source with distributed indexer and service combinations." border="true" lightbox="media/search-multi-region/scale-indexers.png":::
+
+---
+
+## Data residency
+
+When you create multiple search services in different regions, your content is stored in the region you chose for each service.
+
+Azure AI Search doesn't store data outside of your specified region without your authorization. Authorization is implicit when you use features that write to Azure Storage, for which you provide a storage account in your preferred region. These features include:
+
++ [Enrichment cache](cognitive-search-incremental-indexing-conceptual.md)
++ [Debug sessions](cognitive-search-debug-session.md)
++ [Knowledge store](knowledge-store-concept-intro.md)
+
+If your search service and storage account are in the same region, network traffic uses private IP addresses over the Microsoft backbone network, so you can't configure IP firewalls or private endpoints for network security. As an alternative, use the [trusted service exception](search-indexer-howto-access-trusted-service-exception.md).
+
+## Request failover and redirection
+
+For redundancy at the request level, Azure provides several [load-balancing options](/azure/architecture/guide/technology-choices/load-balancing-overview):
+
+### [Azure Application Gateway](#tab/application-gateway)
+
+Use [Azure Application Gateway](/azure/application-gateway/overview) to load balance between servers in a region at the application layer.
+
+By default, service endpoints are accessed through a public internet connection. Use Application Gateway if you set up a private endpoint for client connections that originate from within a virtual network.
+
+### [Azure Front Door](#tab/front-door)
+
+Use [Azure Front Door](/azure/frontdoor/front-door-overview) to optimize global routing of web traffic and provide global failover.
+
+### [Azure Load Balancer](#tab/load-balancer)
+
+Use [Azure Load Balancer](/azure/load-balancer/load-balancer-overview) to load balance between search services in a backend pool.
+
+To use [health probes](/azure/load-balancer/load-balancer-custom-probe-overview) on a search service, you must use an HTTPS probe with `/ping` as the path.
+
+### [Azure Traffic Manager](#tab/traffic-manager)
+
+Use [Azure Traffic Manager](/azure/traffic-manager/traffic-manager-overview) to route requests to multiple geo-located websites backed by multiple search services.
+
+Traffic Manager doesn't provide an endpoint for a direct connection to Azure AI Search. Instead, requests are assumed to flow from Traffic Manager to a search-enabled web client to a search service on the backend. In this scenario, the service and client are in the same region. If one service goes down, the client fails, and Traffic Manager redirects to the remaining client.
+
+The following diagram illustrates search apps connecting through Traffic Manager:
+
+:::image type="content" source="media/search-multi-region/azure-function-search-traffic-mgr.png" alt-text="Diagram of search apps connecting through Azure Traffic Manager." border="true" lightbox="media/search-multi-region/azure-function-search-traffic-mgr.png":::
+
+> [!TIP]
+> Azure AI Search provides a [multi-region Bicep sample](https://github.com/Azure-Samples/azure-search-multiple-regions) that uses Traffic Manager for request redirection when the primary endpoint fails. This solution is useful for routing to a search-enabled client that only calls a search service in the same region.
+
+---
+
+As you evaluate these load-balancing options, consider the following points:
+
++ Azure AI Search is a backend service that accepts indexing and query requests from a client.
+
++ By default, service endpoints are accessed through a public internet connection. We recommend [Azure Application Gateway](/azure/application-gateway/overview) for private endpoints that originate from within a virtual network.
+
++ Azure AI Search accepts requests addressed to the `<your-search-service-name>.search.windows.net` endpoint. If you reach the same endpoint using a different DNS name in the host header, such as a CNAME, the request is rejected.
+
++ Requests from the client to a search service must be authenticated. To access search operations, the caller must have [role-based permissions](search-security-rbac.md) or provide an [API key](search-security-api-keys.md) with the request.
+
+## Related content
+
++ [Reliability in Azure AI Search](/azure/reliability/reliability-ai-search)
++ [Design reliable Azure applications](/azure/architecture/framework/resiliency/app-design)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Searchにおけるマルチリージョンソリューションの解説記事の追加"
}
```

### Explanation
この変更は、新しいMarkdownファイルである `articles/search/search-multi-region.md` の追加を示しています。このファイルは、Azure AI Searchにおけるマルチリージョン展開に関する詳細な情報を提供しています。合計で122行が追加されており、主にサービスの概要や仕組み、データ同期方法、リクエストのフェイルオーバーについて説明しています。

主な内容は以下の通りです：

1. **マルチリージョン展開の利点**: Azure AI Searchは単一リージョンサービスですが、複数のリージョンに同一の構成とコンテンツを持つ検索サービスを展開することで、高い可用性と耐障害性を実現できることが説明されています。

2. **アーキテクチャの概要**: マルチリージョン設定では、2つ以上の検索サービスが異なるリージョンに置かれ、インデックスが同期されていることが述べられています。ユーザーは、最低レイテンシのサービスに自動的にルーティングされます。

3. **データ同期の方法**: データを複数の検索サービス間で同期するための主要な手段として、「プッシュモデル」または「プルモデル」によるインデクシングが挙げられています。具体的には、REST APIを使用したデータのプッシュや、インデクサーを利用したデータのプルが説明されています。

4. **リクエストのフェイルオーバーとリダイレクション**: リクエストレベルの冗長性を提供するために、Azureの様々なロードバランシングオプション（例：Azure Application Gateway、Azure Front Door、Azure Traffic Managerなど）が提示されています。これにより、サービスがダウンした場合でもリクエストが別のサービスにリダイレクトされることができる点が強調されています。

この新しい文書は、Azure AI Searchを使用する際のマルチリージョンの展開方法や考慮事項に関する重要な資料を提供し、ユーザーがグローバルに分散したアプリケーションのニーズに応えられるように設計されています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Shows supported regions and feature availability across regions for
 author: haileytap
 ms.author: haileytapia
 manager: nitinme
-ms.date: 07/31/2025
+ms.date: 08/08/2025
 ms.service: azure-ai-search
 ms.update-cycle: 90-days
 ms.topic: conceptual
@@ -25,7 +25,7 @@ When you create an Azure AI Search service, your region selection might depend o
 | Feature | Description | Availability |
 |---------|-------------|--------------|
 | [AI enrichment](cognitive-search-concept-intro.md) | Refers to [built-in skills](cognitive-search-predefined-skills.md) that make internal calls to Azure AI for enrichment and transformation during indexing. Integration requires that Azure AI Search coexists with an [Azure AI services multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills) in the same physical region. You can bypass region requirements by using [identity-based connections](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection), currently in public preview. | Regional support is noted in this article. |
-| [Availability zones](search-reliability.md#availability-zone-support) | Divides a region's data centers into distinct physical location groups, providing high availability within the same geo. | Regional support is noted in this article. |
+| [Availability zones](/azure/reliability/reliability-ai-search#availability-zone-support) | Divides a region's data centers into distinct physical location groups, providing high availability within the same geo. | Regional support is noted in this article. |
 | [Agentic retrieval](search-agentic-retrieval-concept.md) | Takes a dependency on semantic ranker, which is another premium feature. | Regional support is noted in this article. |
 | [Semantic ranker](semantic-search-overview.md) | Takes a dependency on Microsoft-hosted models in specific regions. | Regional support is noted in this article. |
 | [Query rewrite](semantic-how-to-query-rewrite.md) | Takes a dependency on Microsoft-hosted models in specific regions. | Regional support is noted in this article. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域サポートに関する記事の更新"
}
```

### Explanation
この変更は、`articles/search/search-region-support.md` というMarkdownファイルの修正を示しています。このファイルでは、Azure AI Searchサービスにおける地域の選択と機能の可用性に関する情報が提供されています。合計で4つの変更があり、そのうち2行が追加され、2行が削除されています。

主な変更点は以下の通りです：

1. **日付の更新**: ドキュメントの最終更新日が `07/31/2025` から `08/08/2025` に変更され、提供される情報が最新のものであることを示しています。

2. **リンクの修正**: 「Availability zones」に関連するリンクが修正され、`search-reliability.md#availability-zone-support` から `/azure/reliability/reliability-ai-search#availability-zone-support` へと変更されました。この修正により、ユーザーが最新の情報窓口にアクセスできるようになっています。

3. **テーブルの内容**: 機能の説明における文言がわずかに調整されていますが、内容の意味合いは変わりません。

これらの修正は、Azure AI Searchにおける地域のサポートや機能に関する理解を向上させ、ユーザーがサービスをより効果的に利用できるようサポートすることを目的としています。全体として、この文書はAzure AI Searchサービスの地域選択に関する重要な情報を提供しており、ユーザーが地域が提供する機能を最大限に活用するための指針となります。

## articles/search/search-reliability.md{#item-3e9b1a}

<details>
<summary>Diff</summary>
````diff
@@ -1,205 +0,0 @@
----
-title: Reliability in Azure AI Search
-titleSuffix: Azure AI Search
-description: Learn how to improve the reliability and availability of Azure AI Search services.
-author: haileytap
-ms.author: haileytapia
-ms.service: azure-ai-search
-ms.topic: conceptual
-ms.date: 04/14/2025
-ms.custom:
-  - subject-reliability
-  - references_regions
-  - ignite-2023
----
-
-# Reliability in Azure AI Search
-
-Across Azure, [reliability](/azure/reliability/overview) means resiliency and availability if there's a service outage or degradation. In Azure AI Search, reliability can be achieved within a single service or through multiple search services in separate regions.
-
-+ Deploy a single search service and scale up for high availability. You can add multiple replicas to handle higher indexing and query workloads. If your search service [supports availability zones](#availability-zone-support), replicas are automatically provisioned in different physical data centers for extra resiliency.
-
-+ Deploy multiple search services across different geographic regions. All search workloads are fully contained within a single service that runs in a single geographic region, but in a multi-service scenario, you have options for synchronizing content so that it's the same across all services. You can also set up a load balancing solution to redistribute requests or fail over if there's a service outage.
-
-For business continuity and recovery from disasters at a regional level, plan on a cross-regional topology, consisting of multiple search services having identical configuration and content. Your custom script or code provides the *failover* mechanism to an alternate search service if one suddenly becomes unavailable.
-
-<a name="scale-for-availability"></a>
-
-## High availability
-
-In Azure AI Search, replicas are copies of your index. A search service is commissioned with at least one replica, and can have up to 12 replicas. [Adding replicas](search-capacity-planning.md#add-or-remove-partitions-and-replicas) allows Azure AI Search to do machine reboots and maintenance against one replica, while query execution continues on other replicas.
-
-For each individual search service, Microsoft guarantees at least 99.9% availability for configurations that meet these criteria:
-
-+ Two replicas for high availability of *read-only* workloads (queries)
-
-+ Three or more replicas for high availability of *read-write* workloads (queries and indexing) 
-
-The system has internal mechanisms for monitoring replica health and partition integrity. If you provision a specific combination of replicas and partitions, the system ensures that level of capacity for your service.
-
-No Service Level Agreement (SLA) is provided for the *Free* tier. For more information, see the [SLA for Azure AI Search](https://azure.microsoft.com/support/legal/sla/search/v1_0/).
-
-<a name="availability-zones"></a>
-
-## Availability zone support
-
-[Availability zones](/azure/reliability/availability-zones-overview) are an Azure platform capability that divides a region's data centers into distinct physical location groups to provide high availability, within the same region. In Azure AI Search, individual replicas are the units for zone assignment. A search service runs within one region; its replicas run in different physical data centers (or zones) within that region.
-
-Availability zones are used when you add two or more replicas to your search service. Each replica is placed in a different availability zone within the region. If you have more replicas than available zones in the search service region, the replicas are distributed across zones as evenly as possible. There's no specific action on your part, except to [create a search service](search-create-service-portal.md) in a region that provides availability zones, and then to configure the service to [use multiple replicas](search-capacity-planning.md#add-or-remove-partitions-and-replicas).
-
-### Prerequisites
-
-+ Service tier must be *Standard* or higher
-+ Service region must be in a region that has available zones (listed in the following section)
-+ Configuration must include multiple replicas: two for read-only query workloads, three for read-write workloads that include indexing
-
-### Supported regions
-
-Support for availability zones depends on infrastructure and storage. Currently, the following zone has insufficient storage and doesn't provide an availability zone for Azure AI Search:
-
-+ Japan West
-
-Otherwise, availability zones for Azure AI Search are supported in the following regions:
-
-| Region | Roll out date |
-|--------|-----------|
-| Australia East | January 30, 2021 or later |
-| Brazil South |  May 2, 2021 or later |
-| Canada Central | January 30, 2021 or later |
-| Central India | January 20, 2022 or later |
-| Central US | December 4, 2020 or later |
-| China North 3 | September 7, 2022 or later |
-| East Asia | January 13, 2022 or later |
-| East US | January 27, 2021 or later |
-| East US 2 | January 30, 2021 or later |
-| France Central| October 23, 2020 or later |
-| Germany West Central |  May 3, 2021, or later |
-| Israel Central | April 1, 2024, or later |
-| Italy North | April 1, 2024, or later |
-| Japan East | January 30, 2021 or later |
-| Korea Central | January 20, 2022 or later |
-| North Europe | January 28, 2021 or later |
-| Norway East | January 20, 2022 or later |
-| Qatar Central | August 25, 2022 or later |
-| South Africa North | September 7, 2022 or later |
-| South Central US | April 30, 2021 or later |
-| South East Asia | January 31, 2021 or later |
-| Sweden Central | January 21, 2022 or later |
-| Switzerland North | September 7, 2022 or later |
-| UAE North | September 9, 2022 or later |
-| UK South | January 30, 2021 or later |
-| US Gov Virginia | April 30, 2021 or later |
-| West Europe | January 29, 2021 or later |
-| West US 2 | January 30, 2021 or later |
-| West US 3 | June 02, 2021 or later |
-
-> [!NOTE]
-> Availability zones don't change the terms of the [SLA](https://azure.microsoft.com/support/legal/sla/search/v1_0/). You still need three or more replicas for query high availability.
-
-## Multiple services in separate geographic regions
-
-Service redundancy is necessary if your operational requirements include:
-
-+ [Business continuity and disaster recovery (BCDR) requirements](/azure/reliability/disaster-recovery-overview). Azure AI Search doesn't provide instant failover if there's an outage.
-
-+ Fast performance for a globally distributed application. If query and indexing requests come from all over the world, users who are closest to the host data center experience faster performance. Creating more services in regions with close proximity to these users can equalize performance for all users.
-
-If you need two or more search services, creating them in different regions can meet application requirements for continuity and recovery, and faster response times for a global user base.
-
-Azure AI Search doesn't provide an automated method of replicating search indexes across geographic regions, but there are some techniques that can make this process simple to implement and manage. These techniques are outlined in the next few sections.
-
-The goal of a geo-distributed set of search services is to have two or more indexes available in two or more regions, where a user is routed to the Azure AI Search service that provides the lowest latency:
-
-   ![Diagram showing cross-tab view of services by region.][1]
-
-You can implement this architecture by creating multiple services and designing a strategy for data synchronization. Optionally, you can include a resource like Azure Traffic Manager for routing requests. 
-
-> [!TIP]
-> For help with deploying multiple search services across multiple regions, see this [Bicep sample on GitHub](https://github.com/Azure-Samples/azure-search-multiple-regions) that deploys a fully configured, multi-regional search solution. The sample gives you two options for index synchronization, and request redirection using Traffic Manager.
-
-<a name="data-sync"></a>
-
-### Synchronize data across multiple services
-
-There are two options for keeping two or more distinct search services in sync:
-
-+ Pull content updates into a search index by using an [indexer](search-indexer-overview.md).
-+ Push content into an index using the [Add or Update Documents (REST)](/rest/api/searchservice/documents) API or an Azure SDK equivalent API.
-
-To configure either option, we recommend using the [sample Bicep script in the azure-search-multiple-region](https://github.com/Azure-Samples/azure-search-multiple-regions) repository, modified to your regions and indexing strategies.
-
-#### Option 1: Use indexers for updating content on multiple services
-
-If you're already using indexer on one service, you can configure a second indexer on a second service to use the same data source object, pulling data from the same location. Each service in each region has its own indexer and a target index (your search index isn't shared, which means each index has its own copy of the data), but each indexer references the same data source.
-
-Here's a high-level visual of what that architecture would look like.
-
-![Diagram showing a single data source with distributed indexer and service combinations.][2]
-
-#### Option 2: Use REST APIs for pushing content updates on multiple services
-
-If you're using the Azure AI Search REST API to [push content to your search index](tutorial-optimize-indexing-push-api.md), you can keep your various search services in sync by pushing changes to all search services whenever an update is required. In your code, make sure to handle cases where an update to one search service fails but succeeds for other search services.
-
-### Fail over or redirect query requests
-
-If you need redundancy at the request level, Azure provides several [load balancing options](/azure/architecture/guide/technology-choices/load-balancing-overview):
-
-+ [Azure Traffic Manager](/azure/traffic-manager/traffic-manager-overview), used to route requests to multiple geo-located websites that are then backed by multiple search services. 
-+ [Application Gateway](/azure/application-gateway/overview), used to load balance between servers in a region at the application layer.
-+ [Azure Front Door](/azure/frontdoor/front-door-overview), used to optimize global routing of web traffic and provide global failover.
-+ [Azure Load Balancer](/azure/load-balancer/load-balancer-overview), used to load balance between services in a backend pool.
-
-Some points to keep in mind when evaluating load balancing options:
-
-+ Search is a backend service that accepts query and indexing requests from a client. 
-
-+ Requests from the client to a search service must be authenticated. For access to search operations, the caller must have role-based permissions or provide an API key on the request.
-
-+ Service endpoints are reached through a public internet connection by default. If you set up a private endpoint for client connections that originate from within a virtual network, use [Application Gateway](/azure/application-gateway/overview).
-
-+ Azure AI Search accepts requests addressed to the `<your-search-service-name>.search.windows.net` endpoint. If you reach the same endpoint using a different DNS name in the host header, such as a CNAME, the request is rejected.
-
-Azure AI Search provides a [multi-region deployment sample](https://github.com/Azure-Samples/azure-search-multiple-regions) that uses Azure Traffic Manager for request redirection if the primary endpoint fails. This solution is useful when you route to a search-enabled client that only calls a search service in the same region.
-
-Azure Traffic Manager is primarily used for routing network traffic across different endpoints based on specific routing methods (such as priority, performance, or geographic location). It acts at the DNS level to direct incoming requests to the appropriate endpoint. If an endpoint that Traffic Manager is servicing begins refusing requests, traffic is routed to another endpoint.
-
-Traffic Manager doesn't provide an endpoint for a direct connection to Azure AI Search, which means you can't put a search service directly behind Traffic Manager. Instead, the assumption is that requests flow to Traffic Manager, then to a search-enabled web client, and finally to a search service on the backend. The client and service are located in the same region. If one search service goes down, the search client starts failing, and Traffic Manager redirects to the remaining client.
-
-> [!NOTE]
-> If you are using Azure Load Balancer [health probes](/azure/load-balancer/load-balancer-custom-probe-overview) on a search service, you must use an HTTPS probe with `/ping` as the path.
-
-![Diagram of search apps connecting through Azure Traffic Manager.][4]
-
-## Data residency in a multi-region deployment
-
-When you deploy multiple search services in various geographic regions, your content is stored in the region you chose for each search service.
-
-Azure AI Search doesn't store data outside of your specified region without your authorization. Authorization is implicit when you use features that write to an Azure Storage resource: [enrichment cache](enrichment-cache-how-to-configure.md), [debug session](cognitive-search-debug-session.md), [knowledge store](knowledge-store-concept-intro.md). In all cases, the storage account is one that you provide, in the region of your choice. 
-
-> [!NOTE]
-> If both the storage account and the search service are in the same region, network traffic between search and storage uses a private IP address and occurs over the Microsoft backbone network. Because private IP addresses are used, you can't configure IP firewalls or a private endpoint for network security. Instead, use the [trusted service exception](search-indexer-howto-access-trusted-service-exception.md) as an alternative when both services are in the same region. 
-
-## About service outages and catastrophic events
-
-As stated in the [SLA](https://azure.microsoft.com/support/legal/sla/search/v1_0/), Microsoft guarantees a high level of availability for index query requests when an Azure AI Search service instance is configured with two or more replicas, and index update requests when an Azure AI Search service instance is configured with three or more replicas. However, there's no built-in mechanism for disaster recovery. If continuous service is required in the event of a catastrophic failure outside of Microsoft’s control, we recommend provisioning a second service in a different region and implementing a geo-replication strategy to ensure indexes are fully redundant across all services.
-
-Customers who use [indexers](search-indexer-overview.md) to populate and refresh indexes can handle disaster recovery through geo-specific indexers that retrieve data from the same data source. Two services in different regions, each running an indexer, could index the same data source to achieve geo-redundancy. If you're indexing from data sources that are also geo-redundant, remember that Azure AI Search indexers can only perform incremental indexing (merging updates from new, modified, or deleted documents) from primary replicas. In a failover event, be sure to redirect the indexer to the new primary replica. 
-
-If you don't use indexers, you would use your application code to push objects and data to different search services in parallel. For more information, see [Synchronize data across multiple services](#data-sync).
-
-## Back up and restore alternatives
-
-A business continuity strategy for the data layer usually includes a restore-from-backup step. Because Azure AI Search isn't a primary data storage solution, Microsoft doesn't provide a formal mechanism for self-service backup and restore. However, you can use the **index-backup-restore** sample code in this [Azure AI Search .NET sample repo](https://github.com/Azure-Samples/azure-search-dotnet-utilities)  or in this [Python sample repository](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/index-backup-restore/azure-search-backup-and-restore.ipynb) to back up your index definition and snapshot to a series of JSON files, and then use these files to restore the index, if needed. This tool can also move indexes between service tiers.
-
-Otherwise, your application code used for creating and populating an index is the de facto restore option if you delete an index by mistake. To rebuild an index, you would delete it (assuming it exists), recreate the index in the service, and reload by retrieving data from your primary data store.
-
-## Related content
-
-+ Review [Service limits](search-limits-quotas-capacity.md) to learn more about the pricing tiers and service limits.
-+ Review [Plan for capacity](search-capacity-planning.md) to learn more about partition and replica combinations.
-+ Review [Case Study: Use Cognitive Search to Support Complex AI Scenarios](https://techcommunity.microsoft.com/t5/azure-ai/case-study-effectively-using-cognitive-search-to-support-complex/ba-p/2804078) for more configuration guidance.
-
-<!--Image references-->
-[1]: ./media/search-reliability/geo-redundancy.png
-[2]: ./media/search-reliability/scale-indexers.png
-[4]: ./media/search-reliability/azure-function-search-traffic-mgr.png
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azure AI Searchの信頼性に関する記事の削除"
}
```

### Explanation
この変更は、`articles/search/search-reliability.md` というMarkdownファイルが完全に削除されたことを示しています。このファイルは、Azure AI Searchにおける信頼性と可用性の向上に関する詳細なガイドラインを提供していましたが、205行が削除されました。

主な内容は以下の通りです：

1. **信頼性の概念**: Azureにおける信頼性の考え方の説明や、単一の検索サービスまたは複数のリージョンにまたがる検索サービスを通じて信頼性を達成する方法が記載されていました。

2. **高可用性の実現**: 検索サービスにおけるレプリカの使用や、可用性ゾーンのサポートについての具体的なガイドライン、そしてそれに対する条件が説明されていました。

3. **災害時のビジネス継続性**: 地域レベルでのビジネス継続と災害復旧のためのクロスリージョナルトポロジーの計画が強調されていました。

4. **複数サービスによる冗長性**: 地理的に分散したサービスに対する冗長性や、データの同期手法についても言及されていました。

この更新は、Azure AI Searchのドキュメントにおける重大な変更を示しており、ユーザーに信頼性に関する情報を別のリソースで確認する必要があることを示唆しています。完全な情報が提供されていた記事を削除することで、今後は新しい文書やガイドラインに基づいた情報の提供が行われる可能性が高いです。これにより、ユーザーは最新のリソースを参照しつつ、Azure AI Searchの利用に関する信頼性の概念を理解することが期待されています。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 08/01/2025
+ms.date: 08/08/2025
 ---
 
 # Choose a service tier for Azure AI Search
@@ -69,7 +69,7 @@ Most features are available on all tiers, including the Free tier. In a few case
 | [Customer-managed encryption keys](search-security-manage-encryption-keys.md) | Not available on the Free tier. |
 | [IP firewall access](service-configure-firewall.md) | Not available on the Free tier. |
 | [Private endpoint (integration with Azure Private Link)](service-create-private-endpoint.md) | For inbound connections to a search service, not available on the Free tier. <br>For outbound connections by indexers to other Azure resources, not available on Free or S3 HD. <br>For indexers that use skillsets, not available on Free, Basic, S1, or S3 HD.|
-| [Availability Zones](search-reliability.md) | Not available on the Free or Basic tier. |
+| [Availability zones](/azure/reliability/reliability-ai-search#availability-zone-support) | Not available on the Free tier. |
 | [Semantic ranker](semantic-search-overview.md) | Not available on the Free tier. |
 
 Resource-intensive features might not work well unless you give it sufficient capacity. For example, [AI enrichment](cognitive-search-concept-intro.md) has long-running skills that time out on a Free service unless the dataset is small.
@@ -80,7 +80,7 @@ Tiers determine the  maximum storage of the service itself, plus the maximum num
 
 ## Partition size and speed
 
-Tier pricing includes details about per-partition storage that ranges from 15 GB for Basic, up to 2 TB for Storage Optimized (L2) tiers. Other hardware characteristics, such as speed of operations, latency, and transfer rates, aren't published, but tiers that are designed for specific solution architectures are built on hardware that has the features to support those scenarios. For more information about partitions, see [Estimate and manage capacity](search-capacity-planning.md) and [Reliability in Azure AI Search](search-reliability.md).
+Tier pricing includes details about per-partition storage that ranges from 15 GB for Basic, up to 2 TB for Storage Optimized (L2) tiers. Other hardware characteristics, such as speed of operations, latency, and transfer rates, aren't published, but tiers that are designed for specific solution architectures are built on hardware that has the features to support those scenarios. For more information about partitions, see [Estimate and manage capacity](search-capacity-planning.md) and [Reliability in Azure AI Search](/azure/reliability/reliability-ai-search).
 
 > [!NOTE]
 > Higher-capacity partitions became available in select regions in April 2024. A second wave of higher-capacity partitions was released in May 2024. If you have an older search service, you might be able to [upgrade your service](search-how-to-upgrade.md) to benefit from more capacity at the same billing rate.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI SearchのSKU Tierに関する更新"
}
```

### Explanation
この変更は、`articles/search/search-sku-tier.md` というMarkdownファイルへの修正を示しています。主な内容は、Azure AI Searchのサービスティア（SKU Tier）に関する情報の更新です。合計で6つの変更があり、3行が追加され、3行が削除されています。

主な変更点は以下の通りです：

1. **最終更新日の日付変更**: ドキュメントの最終更新日が `08/01/2025` から `08/08/2025` に修正され、提供される情報が最新のものであることを示しています。

2. **リンクの修正**: 「Availability Zones」に関連するリンクが変更されました。具体的には、プレビューリンクに対して適切なパスが指定され、`search-reliability.md` から `/azure/reliability/reliability-ai-search#availability-zone-support` に変更されました。この修正により、ユーザーが最新の情報にアクセスしやすくなっています。

3. **コンテンツの調整**: 一部の記述が微調整され、全体の文書が明確で理解しやすくなるよう更新されています。特に、他の機能との関連性や各ティアの特徴についての言及が整理されました。

これらの修正は、Azure AI SearchのSKUティアに関する理解を助け、ユーザーが適切なサービスを選択するための情報を提供することを目的としています。ユーザーはこの更新によって、サービスの利用可能な機能や関連するリソースに簡単にアクセスできるようになります。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -52,6 +52,12 @@ items:
       href: search-query-overview.md
   - name: Relevance
     href: search-relevance-overview.md
+  - name: Reliability
+    items:
+      - name: Reliability in Azure AI Search
+        href: /azure/reliability/reliability-ai-search?toc=/azure/search/toc.json&bc=/azure/search/breadcrumb/toc.json
+      - name: Multi-region deployment
+        href: search-multi-region.md
   - name: Security
     href: search-security-overview.md
 - name: Quickstarts
@@ -188,8 +194,6 @@ items:
       href: search-capacity-planning.md
     - name: Plan and manage costs
       href: search-sku-manage-costs.md
-    - name: Reliability and recovery
-      href: search-reliability.md
     - name: Multi-tenancy
       href: search-modeling-multitenant-saas-applications.md
     - name: Manage
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおける目次の更新"
}
```

### Explanation
この変更は、`articles/search/toc.yml`というファイルに対する修正を示しています。合計で8つの変更があり、6行が追加され、2行が削除されています。主な更新内容は、Azure AI Searchの目次に新たな項目を追加し、一部の項目を削除したことです。

主な変更点は以下の通りです：

1. **新しいカテゴリ「Reliability」の追加**: 
   - 「Reliability」という新しいセクションが目次に追加され、このセクション内に「Reliability in Azure AI Search」と「Multi-region deployment」という2つの項目が新設されました。これにより、ユーザーは信頼性に関する情報に簡単にアクセスできるようになります。

2. **「Reliability and recovery」の削除**:
   - 目次から「Reliability and recovery」という項目が削除されました。この変更は、内容の整理を目的としており、情報の重複を避けるために行われた可能性があります。

3. **リンクの更新**:
   - 新規追加された項目には、適切なリンク先が設定されており、ユーザーがそれぞれのトピックにアクセスしやすくなっています。

これらの変更により、Azure AI Searchのドキュメントがより明確になり、特に信頼性に関連する情報が強調されていることで、ユーザーにとっての利便性が向上しています。目次の整理は、情報を効率的に探しやすくし、関連するリソースへのアクセスを促進するための重要な更新です。


