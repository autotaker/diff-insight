---
date: '2025-04-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:24b31df...MicrosoftDocs:a9279bd
summary: |-
  このコードディフは、Azure AI Searchに関連する日本語のドキュメントを改訂し、新機能や改良を多数追加しました。特に目立つ点は、画像ファイルの追加、セマンティックランカー及びベクトル検索の大幅な更新です。これにより、利用者は最新機能を理解しやすくなっています。

  新しい機能として、ベクトル量子化やストレージオプションに関するガイドラインが追加され、更新された検索クエリやREST APIの具体的な使用法も説明されています。また、重要な更新として、`articles/search/whats-new.md`ファイルに大きな変更があり、古い機能と新機能が整理されているため、ユーザーは最新情報をもとにシステムを管理する必要があります。

  画像ファイルの追加により視覚的な支援が強化され、複雑な概念の理解が向上します。セマンティック検索やベクトル検索に関する情報も最新化され、ユーザーはこれらの機能を効果的に活用できるようになります。

  全体として、これらの変更はAzure AI Searchの進化を示しており、特に高度な検索体験を提供するための改善に焦点が当てられています。新しいリソースにより、データ管理の効率が向上し、ユーザーが直面するストレージ関連の問題に対するソリューションも提案されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:24b31df...MicrosoftDocs:a9279bd){target="_blank"}

<format>
# Highlights
このコードディフは、日本語ロケールでAzure AI Searchに関連する一連のドキュメントを詳細に改訂したもので、新機能の追加や既存機能の改善が多数含まれています。特に重要なのは、新しい画像ファイルの追加と、セマンティックランカーおよびベクトル検索に関する大幅な更新です。また、多くの文章が明確化され、利用者が最新の機能を理解しやすくするための細かな改善が施されています。

## New features
- なによりも注目されるのは、Azure AI Searchのベクトル量子化およびストレージオプションに関する新しいガイドラインの提供です。これに伴って、関連する操作や概念の理解を助けるための具体的な手順と説明が追加されました。
- また、検索クエリやセマンティックランカーに関するセクションが更新され、新しいREST APIに対する具体的な使用法が明示されています。

## Breaking changes
- 特に大きな更新が施された`articles/search/whats-new.md`ファイルでは、以前の機能に変更が加えられており、ユーザーは最新の情報を確認してシステムを適切に管理する必要があります。この文書の更新は、複数の機能が削除され、新たに整理された形で機能が追加または強化されていることを示しています。

## Other updates
- 画像ファイルの大量追加により、特にキャパシティプランニングにおいて視覚的な支援が強化されています。これによりユーザーは複雑な概念をより直感的に理解できるようになりました。
- セマンティック検索およびベクトル検索の構成やクエリ方法の情報が最新化・強化されており、これによりユーザーは機能を最大限に活用することが可能になります。

# Insights
この一連の変更は、Azure AI Searchが進化し続けていることを示すもので、特にセマンティックランカーやベクトル検索といった高度な機能の改善に焦点を当てています。これらの機能強化は、ユーザーがよりリッチでパフォーマンスの高い検索エクスペリエンスを提供できるよう支援するものです。具体的な操作手順や構成例が豊富に提供されているため、特にエンジニアや開発者はこれを活用することで、検索サービスの能力を拡張し、ユーザーエクスペリエンスを向上させることができます。

その上、お客様が抱える複雑なデータセットをより効率的に扱うためのベクトル量子化技術が新たにドキュメントされ、ストレージ効率の面でも大きな改善が見込まれます。このリソースの追加により、Azure AI Searchがデータ管理の最前線に位置していることが強調されており、ユーザーが直面する可能性のあるストレージ関連の問題に対するソリューションを提案しています。

全体的に、新しい情報や視覚資料の追加、最新APIの利用促進といった対応により、ユーザーはAzure AI Searchをより効果的に活用して、最適な検索エクスペリエンスを構築することができます。このディフが提供する豊富な情報は、ユーザーが日常的に直面する課題を解決する価値あるガイドとして機能します。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [.openpublishing.redirection.search.json](#item-8b66f9) | minor update | JSONファイルのフォーマットの修正 | modified | 1 | 1 | 2 | 
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | 手順の説明を更新 | modified | 1 | 1 | 2 | 
| [cognitive-search-skill-document-intelligence-layout.md](#item-62c06f) | minor update | 文書レイアウトスキルに関する内容の更新 | modified | 8 | 7 | 15 | 
| [cognitive-search-tutorial-blob-dotnet.md](#item-ba889d) | minor update | C#チュートリアルのタイトルと内容の調整 | modified | 13 | 13 | 26 | 
| [cognitive-search-tutorial-blob.md](#item-ff148f) | minor update | RESTチュートリアルの内容調整 | modified | 10 | 10 | 20 | 
| [cognitive-search-tutorial-debug-sessions.md](#item-7e10e9) | minor update | デバッグセッションチュートリアルの内容更新 | modified | 27 | 27 | 54 | 
| [preview-generic.md](#item-51bbcc) | minor update | プレビュー機能情報の修正 | modified | 4 | 4 | 8 | 
| [add-two-each.png](#item-56b26e) | new feature | 新しい画像の追加: add-two-each.png | added | 0 | 0 | 0 | 
| [change-pricing-tier.png](#item-f71721) | new feature | 新しい画像の追加: change-pricing-tier.png | added | 0 | 0 | 0 | 
| [initial-values.png](#item-465304) | new feature | 新しい画像の追加: initial-values.png | added | 0 | 0 | 0 | 
| [portal-notifications.png](#item-4bd098) | new feature | 新しい画像の追加: portal-notifications.png | added | 0 | 0 | 0 | 
| [pricing-tier-list.png](#item-ff6b12) | new feature | 新しい画像の追加: pricing-tier-list.png | added | 0 | 0 | 0 | 
| [provisioning-status.png](#item-ede201) | new feature | 新しい画像の追加: provisioning-status.png | added | 0 | 0 | 0 | 
| [updating-message.png](#item-fc9f1b) | new feature | 新しい画像の追加: updating-message.png | added | 0 | 0 | 0 | 
| [portal-add-facetable-field.png](#item-d0b7a4) | new feature | 新しい画像の追加: portal-add-facetable-field.png | added | 0 | 0 | 0 | 
| [portal-facet-query.png](#item-57be1f) | new feature | 新しい画像の追加: portal-facet-query.png | added | 0 | 0 | 0 | 
| [search-data-source.png](#item-e559ff) | new feature | 新しい画像の追加: search-data-source.png | added | 0 | 0 | 0 | 
| [service-creation-upgrade-metadata.png](#item-d1251d) | new feature | 新しい画像の追加: service-creation-upgrade-metadata.png | added | 0 | 0 | 0 | 
| [upgrade-button.png](#item-894e31) | new feature | 新しい画像の追加: upgrade-button.png | added | 0 | 0 | 0 | 
| [upgrade-confirmation.png](#item-880793) | new feature | 新しい画像の追加: upgrade-confirmation.png | added | 0 | 0 | 0 | 
| [upgrade-panel.png](#item-0c9673) | new feature | 新しい画像の追加: upgrade-panel.png | added | 0 | 0 | 0 | 
| [assign-key-vault.png](#item-e19e19) | new feature | 新しい画像の追加: assign-key-vault.png | added | 0 | 0 | 0 | 
| [resource-training.md](#item-07788d) | minor update | リソーストレーニング文書の更新 | modified | 2 | 3 | 5 | 
| [search-api-migration.md](#item-07297b) | minor update | 検索API移行文書の更新 | modified | 2 | 2 | 4 | 
| [search-api-preview.md](#item-511f5d) | minor update | 検索APIプレビュー文書の更新 | modified | 9 | 4 | 13 | 
| [search-capacity-planning.md](#item-0dd6c9) | minor update | 検索キャパシティ計画文書の更新 | modified | 80 | 32 | 112 | 
| [search-create-service-portal.md](#item-f90159) | minor update | Azure AI 検索サービス作成ガイドの更新 | modified | 6 | 6 | 12 | 
| [search-faceted-navigation-examples.md](#item-2b1158) | new feature | ファセットナビゲーションの例に関する新規文書の追加 | added | 721 | 0 | 721 | 
| [search-faceted-navigation.md](#item-f29d1e) | minor update | ファセットナビゲーションの文書内容の更新 | modified | 112 | 167 | 279 | 
| [search-faq-frequently-asked-questions.yml](#item-eab2ba) | minor update | Azure AI Search FAQの内容更新 | modified | 24 | 7 | 31 | 
| [search-how-to-index-sql-database.md](#item-86d873) | minor update | SQLデータベースのインデックス作成方法に関する文書の更新 | modified | 50 | 39 | 89 | 
| [search-how-to-large-index.md](#item-d34e42) | minor update | 大規模インデックス作成に関する文書の更新 | modified | 4 | 4 | 8 | 
| [search-how-to-load-search-index.md](#item-a72573) | minor update | 検索インデックスのデータロードに関する文書の更新 | modified | 2 | 2 | 4 | 
| [search-how-to-semantic-chunking.md](#item-4a1d07) | minor update | セマンティックチャンクに関する文書の更新 | modified | 7 | 5 | 12 | 
| [search-how-to-upgrade.md](#item-990225) | new feature | Azure AI Searchサービスのアップグレード方法についての新規文書 | added | 115 | 0 | 115 | 
| [search-howto-index-encrypted-blobs.md](#item-a7097a) | minor update | 暗号化されたBLOBをインデックスするチュートリアルの更新 | modified | 43 | 41 | 84 | 
| [search-howto-managed-identities-data-sources.md](#item-edf98d) | minor update | 管理対象 ID とデータソースに関するドキュメントの更新 | modified | 6 | 6 | 12 | 
| [search-howto-reindex.md](#item-46738a) | minor update | インデックス再構築に関するドキュメントの更新 | modified | 3 | 3 | 6 | 
| [search-howto-run-reset-indexers.md](#item-fb10c8) | minor update | インデクサの実行とリセットに関するドキュメントの更新 | modified | 26 | 20 | 46 | 
| [search-indexer-how-to-access-private-sql.md](#item-1bd4cc) | minor update | Azure SQL管理インスタンスのプレビューAPIバージョンの更新 | modified | 1 | 1 | 2 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | プライベートSQLアクセスに関するドキュメントの更新 | modified | 5 | 5 | 10 | 
| [search-indexer-tutorial.md](#item-a3e3ff) | minor update | C#チュートリアル：Azure SQLデータのインデクシング | modified | 54 | 58 | 112 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索サービスの制限および容量に関するドキュメントの更新 | modified | 10 | 9 | 19 | 
| [search-manage-azure-cli.md](#item-7fdd08) | minor update | Azure CLIを使用したAzure AI Searchサービスの管理 | modified | 6 | 8 | 14 | 
| [search-manage-powershell.md](#item-3c3485) | minor update | PowerShellを使用したAzure AI Searchサービスの管理 | modified | 7 | 9 | 16 | 
| [search-manage-rest.md](#item-405ec7) | minor update | REST APIを使用したAzure AI Searchサービスの管理 | modified | 63 | 39 | 102 | 
| [search-markdown-data-tutorial.md](#item-32ea2a) | minor update | Markdownブロブのインデックス作成に関するチュートリアル | modified | 34 | 30 | 64 | 
| [search-performance-tips.md](#item-218e77) | minor update | Azure AI Searchのパフォーマンス向上に関するヒント | modified | 9 | 9 | 18 | 
| [search-region-support.md](#item-25b0f1) | minor update | Azure AI Searchのリージョンサポート | modified | 62 | 59 | 121 | 
| [search-reliability.md](#item-3e9b1a) | minor update | Azure AI Searchの信頼性について | modified | 6 | 6 | 12 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | 顧客管理キーを使用したデータの暗号化 | modified | 6 | 6 | 12 | 
| [search-security-network-security-perimeter.md](#item-49c0d7) | minor update | Azure AI Searchのネットワークセキュリティ境界 | modified | 3 | 3 | 6 | 
| [search-security-overview.md](#item-6b3f1e) | minor update | カスタマー管理キー（CMK）に関する情報の更新 | modified | 1 | 1 | 2 | 
| [search-semi-structured-data.md](#item-d3388d) | minor update | 半構造化データのインデックス作成に関するチュートリアルの更新 | modified | 25 | 25 | 50 | 
| [search-sku-manage-costs.md](#item-6e0122) | minor update | Azure AI Search サービスのコスト管理に関するガイドラインの更新 | modified | 4 | 4 | 8 | 
| [search-sku-tier.md](#item-7686b8) | minor update | Azure AI Search サービスティアに関するガイドラインの更新 | modified | 26 | 17 | 43 | 
| [search-synapseml-cognitive-services.md](#item-dcc36f) | minor update | SynapseML と Azure AI Search を使用した大規模データのインデックス作成チュートリアルの更新 | modified | 39 | 39 | 78 | 
| [semantic-how-to-configure.md](#item-7a92a6) | minor update | セマンティックランカーの構成方法に関するガイドの更新 | modified | 57 | 1 | 58 | 
| [semantic-how-to-enable-disable.md](#item-71ac1e) | minor update | セマンティックランカーの有効化と無効化に関するガイドの更新 | modified | 3 | 3 | 6 | 
| [semantic-how-to-query-request.md](#item-85530d) | minor update | セマンティッククエリリクエストに関するガイドの更新 | modified | 2 | 2 | 4 | 
| [semantic-how-to-query-rewrite.md](#item-3e168f) | minor update | セマンティッククエリ再構成に関するガイドの更新 | modified | 27 | 30 | 57 | 
| [semantic-search-overview.md](#item-b7497b) | minor update | セマンティック検索の概要の更新 | modified | 2 | 2 | 4 | 
| [toc.yml](#item-c4768f) | minor update | TOC（目次）ファイルの更新 | modified | 10 | 6 | 16 | 
| [tutorial-create-custom-analyzer.md](#item-ad5520) | minor update | カスタムアナライザー作成チュートリアルの更新 | modified | 62 | 62 | 124 | 
| [tutorial-multiple-data-sources.md](#item-71558f) | minor update | 複数データソースチュートリアルの更新 | modified | 8 | 8 | 16 | 
| [tutorial-optimize-indexing-push-api.md](#item-ef0e96) | minor update | プッシュAPIによるインデクシング最適化チュートリアルの更新 | modified | 54 | 56 | 110 | 
| [tutorial-rag-build-solution-pipeline.md](#item-25ce01) | minor update | RAG用インデクシングパイプラインのチュートリアル更新 | modified | 6 | 6 | 12 | 
| [vector-search-how-to-chunk-documents.md](#item-b79133) | minor update | Azure AI Searchにおける文書のチャンク処理に関する更新 | modified | 4 | 2 | 6 | 
| [vector-search-how-to-quantization.md](#item-744f48) | major update | Azure AI Searchにおけるベクトル量子化の詳細なガイド | modified | 186 | 46 | 232 | 
| [vector-search-how-to-storage-options.md](#item-ee1680) | major update | Azure AI Searchにおけるベクトルストレージオプションのアップデート | modified | 58 | 27 | 85 | 
| [vector-search-index-size.md](#item-bb2846) | minor update | ベクトルインデックスサイズと制限に関する情報の更新 | modified | 5 | 23 | 28 | 
| [vector-search-overview.md](#item-56e5fa) | minor update | ベクトル検索のサービスアップグレードに関する説明の追加 | modified | 1 | 1 | 2 | 
| [vector-store.md](#item-db9b8c) | minor update | ベクトルストレージに関する情報の更新 | modified | 4 | 4 | 8 | 
| [whats-new.md](#item-fa71b4) | breaking change | Azure AI Searchの新機能および変更点の大幅更新 | modified | 67 | 125 | 192 | 


# Modified Contents
## articles/search/.openpublishing.redirection.search.json{#item-8b66f9}

<details>
<summary>Diff</summary>
````diff
@@ -382,4 +382,4 @@
             "redirect_document_id": false
         }
     ]
-}
\ No newline at end of file
+  }
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JSONファイルのフォーマットの修正"
}
```

### Explanation
この変更は、`articles/search/.openpublishing.redirection.search.json`ファイルにおけるJSON構造の軽微な修正を示しています。具体的には、1行の削除と1行の追加があり、全体として2つの変更が行われました。変更内容は、ファイルの末尾に必要な括弧を追加することで、JSONの有効性を保つためのものです。ファイルの形式が適正に整えられることで、データのパースエラーを防ぐ効果が期待されます。この修正は大きな機能追加やバグ修正というわけではなく、JSONの整合性を確保するためのマイナーな更新です。

## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -50,7 +50,7 @@ Using the Azure portal or newer preview REST APIs and beta SDK packages, you can
 
 1. On your Azure AI services multi-service resource, [assign the identity](/azure/role-based-access-control/role-assignments-portal) to the **Cognitive Services User** role.
 
-1. Using the Azure portal, or the [Skillset 2024-11-01-preview REST API](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true), or an Azure SDK beta package that provides the syntax, configure a skillset to use an identity:
+1. Using the Azure portal, or the [Skillset 2024-11-01-preview REST API](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true) or later, or an Azure SDK beta package that provides the syntax, configure a skillset to use an identity:
 
    + The managed identity used on the connection belongs to the search service. It can be system managed or user assigned.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "手順の説明を更新"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-attach-cognitive-services.md`ファイルの手順説明に関する軽微な修正を示しています。具体的には、ステップの内容が1箇所更新されています。元の手順では「Azureポータル、または[Skillset 2024-11-01-preview REST API]」と記載されていましたが、今回は「または以降」と追加され、より明確に最新のAPIバージョンを示すようになりました。この更新は文書の正確性と明確さを向上させるものであり、プログラム利用者が適切なバージョンを参照できるようにするための重要な改善です。全体として、この変更は大きな機能追加やバグ修正ではなく、表現の微調整によるマイナーな更新と見なされます。

## articles/search/cognitive-search-skill-document-intelligence-layout.md{#item-62c06f}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: reference
-ms.date: 02/13/2025
+ms.date: 04/07/2025
 ---
 
 # Document Layout skill
@@ -22,12 +22,13 @@ The **Document Layout** skill analyzes a document to extract regions of interest
 
 This article is the reference documentation for the Document Layout skill. For usage information, see [Structure-aware chunking and vectorization](search-how-to-semantic-chunking.md).
 
-The **Document Layout** skill calls the [Document Intelligence Public preview version 2024-07-31-preview](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true). It's currently only available in the following Azure regions:
+The **Document Layout** skill calls the [Document Intelligence Public preview version 2024-07-31-preview](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true). 
 
-+ East US
-+ West US2
-+ West Europe
-+ North Central US
+Supported regions varies by modality:
+
++ In code, your skillset can call Document Intelligence through an Azure AI multi-service resource in any region that provides both AI enrichment and Document Intelligence. See [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table) to find regions that provide both *AI enrichment* in Azure AI Search and *Document Intelligence* under Azure AI services.
+
++ In the [Import and vectorize data](search-import-data-portal.md) wizard in the Azure portal, you can enable document layout detection in the data source connection step. Document layout detection in the portal is available in the following Azure regions: **East US**, **West Europe**, **North Central US**. Create an Azure AI multi-service resource in one of these three regions to get the portal experience.
 
 Supported file formats include:
 
@@ -59,7 +60,7 @@ Microsoft.Skills.Util.DocumentIntelligenceLayoutSkill
 
 ## Supported languages
 
-Refer to [Azure AI Document Intelligence layout model supported languages](/azure/ai-services/document-intelligence/language-support/ocr?view=doc-intel-3.1.0&tabs=read-print%2Clayout-print%2Cgeneral#layout) for printed text.
+Refer to [Azure AI Document Intelligence layout model supported languages](/azure/ai-services/document-intelligence/language-support/ocr?view=doc-intel-3.1.0&tabs=read-print%2Clayout-print%2Cgeneral#layout&preserve-view=true) for printed text.
 
 ## Limitations
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書レイアウトスキルに関する内容の更新"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-document-intelligence-layout.md`ファイルに対する修正を示しています。主な更新内容は以下の通りです。

1. **日付の変更**: ドキュメントの日付が変更され、2025年2月13日から2025年4月7日へと更新されました。
2. **サポートされる地域の説明**:
   - 元の文から具体的な地域名（East US、West US2、West Europe、North Central US）が削除され、「サポートされる地域はモダリティによって異なる」との文章に改訂されました。この内容により、地域の選択がより柔軟であることが強調されています。
   - Azureポータルでのデータインポート時の文書レイアウト検出の利用可能地域についての情報が追加されました。これにより、具体的にどの地域で機能を利用できるかが明示されています。

3. **リンクの更新**: レイアウトモデルに関連する最新のURLが追加され、情報アクセスが向上しています。

これらの変更は、利用者に対して文書の正確性や有用性を高めるためのマイナーな更新として位置付けられます。全体として、文書の内容が最新の情報に合わせて調整され、特に利用者が各機能をどの地域で利用可能かをより明確に理解できるよう配慮されています。

## articles/search/cognitive-search-tutorial-blob-dotnet.md{#item-ba889d}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Tutorial: Skillsets using C#'
+title: 'Tutorial: Skillsets Using C#'
 titleSuffix: Azure AI Search
 description: Use C# and the Azure SDK for .NET to create skillsets. This skillset applies AI transformations and analyses to create searchable content from images and unstructured text.
 
@@ -9,7 +9,7 @@ manager: nitinme
 
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 01/17/2025
+ms.date: 03/31/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
@@ -18,19 +18,17 @@ ms.custom:
 
 # C# Tutorial: Use skillsets to generate searchable content in Azure AI Search
 
-In this tutorial, learn how to use the [Azure SDK for .NET](https://www.nuget.org/packages/Azure.Search.Documents/) to create an [AI enrichment pipeline](cognitive-search-concept-intro.md) for content extraction and transformations during indexing.
+Learn how to use the [Azure SDK for .NET](https://www.nuget.org/packages/Azure.Search.Documents/) to create an [AI enrichment pipeline](cognitive-search-concept-intro.md) for content extraction and transformations during indexing.
 
-Skillsets add AI processing to raw content, making that content more uniform and searchable. Once you know how skillsets work, you can support a broad range of transformations: from image analysis, to natural language processing, to customized processing that you provide externally.
+Skillsets add AI processing to raw content, making it more uniform and searchable. Once you know how skillsets work, you can support a broad range of transformations, from image analysis to natural language processing to customized processing that you provide externally.
 
-This tutorial helps you learn how to:
+In this tutorial, you:
 
 > [!div class="checklist"]
 > + Define objects in an enrichment pipeline.
 > + Build a skillset. Invoke OCR, language detection, entity recognition, and key phrase extraction.
 > + Execute the pipeline. Create and load a search index.
-> + Check the results using full text search.
-
-If you don't have an Azure subscription, open a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
+> + Check the results using full-text search.
 
 ## Overview
 
@@ -42,16 +40,18 @@ Once content is extracted, the [skillset](cognitive-search-working-with-skillset
 
 ## Prerequisites
 
-+ [Visual Studio](https://visualstudio.microsoft.com/downloads/)
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+
++ [Azure Storage](/azure/storage/common/storage-account-create).
 
-+ [Azure.Search.Documents 11.x NuGet package](https://www.nuget.org/packages/Azure.Search.Documents) 
++ [Azure AI Search](search-create-app-portal.md).
 
-+ [Azure Storage](/azure/storage/common/storage-account-create)
++ [Azure.Search.Documents 11.x NuGet package](https://www.nuget.org/packages/Azure.Search.Documents).
 
-+ [Azure AI Search](search-create-app-portal.md)
++ [Visual Studio](https://visualstudio.microsoft.com/downloads/).
 
 > [!NOTE]
-> You can use a free search service for this tutorial. The free tier limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before starting, make sure you have room on your service to accept the new resources.
+> You can use a free search service for this tutorial. The Free tier limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before you start, make sure you have room on your service to accept the new resources.
 
 ### Download files
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#チュートリアルのタイトルと内容の調整"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-tutorial-blob-dotnet.md`ファイルに対する修正を示しています。主な更新点は次の通りです。

1. **タイトルの変更**: タイトルが「Tutorial: Skillsets using C#」から「Tutorial: Skillsets Using C#」に変更され、大文字が適用されています。この微調整により、タイトルのフォーマットが統一されています。

2. **日付の更新**: 文書の日付が2025年1月17日から2025年3月31日に更新され、最新の情報を反映するようになりました。

3. **内容の修正**:
   - テキストの一部において、文の構造や言い回しが改善され、読みやすさが向上しています。例えば、「このチュートリアルでは...」から「あなたはこのチュートリアルで...」というように、能動的な表現に変更されています。
   - プリレクイジット（前提条件）のセクションにおいて、リスト項目の順序が整理され、明確でコンシステントな形式に改善されました。

4. **ノートのテキストの整形**: “Free tier”に関するノートの表現が微調整され、明確で読みやすくなっています。

この変更は、全体的に文書の可読性と整合性を向上させる影響があり、特にチュートリアルの利用者が情報をより簡単に理解できるようになっています。これにより、ユーザーエクスペリエンスが向上することが期待されます。

## articles/search/cognitive-search-tutorial-blob.md{#item-ff148f}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Tutorial: Skillsets using REST'
+title: 'Tutorial: Skillsets Using REST'
 titleSuffix: Azure AI Search
 description: Use the Search REST APIs to create skillsets. This skillset applies AI transformations and analyses to create searchable content from images and unstructured text.
 
@@ -9,25 +9,23 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: tutorial
-ms.date: 01/17/2025
+ms.date: 03/31/2025
 ---
 
 # REST Tutorial: Use skillsets to generate searchable content in Azure AI Search
 
-In this tutorial, learn how to call REST APIs that create an [AI enrichment pipeline](cognitive-search-concept-intro.md) for content extraction and transformations during indexing.
+Learn how to call REST APIs that create an [AI enrichment pipeline](cognitive-search-concept-intro.md) for content extraction and transformations during indexing.
 
-Skillsets add AI processing to raw content, making that content more uniform and searchable. Once you know how skillsets work, you can support a broad range of transformations: from image analysis, to natural language processing, to customized processing that you provide externally.
+Skillsets add AI processing to raw content, making it more uniform and searchable. Once you know how skillsets work, you can support a broad range of transformations, from image analysis to natural language processing to customized processing that you provide externally.
 
-This tutorial helps you learn how to:
+In this tutorial, you:
 
 > [!div class="checklist"]
 > + Define objects in an enrichment pipeline.
 > + Build a skillset. Invoke OCR, language detection, entity recognition, and key phrase extraction.
 > + Execute the pipeline. Create and load a search index.
 > + Check the results using full text search.
 
-If you don't have an Azure subscription, open a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
-
 ## Overview
 
 This tutorial uses a REST client and the [Azure AI Search REST APIs](/rest/api/searchservice/) to create a data source, index, indexer, and skillset.
@@ -38,20 +36,22 @@ Once content is extracted, the [skillset](cognitive-search-working-with-skillset
 
 ## Prerequisites
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
 + [Azure Storage](/azure/storage/common/storage-account-create)
 
 + [Azure AI Search](search-create-app-portal.md)
 
++ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
+
 > [!NOTE]
-> You can use a free search service for this tutorial. The free tier limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before starting, make sure you have room on your service to accept the new resources.
+> You can use a free search service for this tutorial. The Free tier limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before you start, make sure you have room on your service to accept the new resources.
 
 ### Download files
 
 Download a zip file of the sample data repository and extract the contents. [Learn how](https://docs.github.com/get-started/start-your-journey/downloading-files-from-github).
 
-+ [Sample data files (mixed media)](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/ai-enrichment-mixed-media). 
++ [Sample data files (mixed media)](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/ai-enrichment-mixed-media).
 
 + [Sample REST file](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/skillset-tutorial)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTチュートリアルの内容調整"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-tutorial-blob.md`ファイルに対する修正を示しています。主な更新点は以下の通りです。

1. **タイトルの変更**: タイトルが「Tutorial: Skillsets using REST」から「Tutorial: Skillsets Using REST」に変更され、大文字が適用され、見た目が整っています。

2. **日付の更新**: 文書の日付が2025年1月17日から2025年3月31日に更新され、最新の情報が反映されています。

3. **内容の修正**:
   - 一部の文の表現が能動的に変更され、よりわかりやすくなっています。たとえば、「このチュートリアルでは...」から「あなたはこのチュートリアルで...」といった表現に変更されています。
   - プリレクイジット（前提条件）に新たに「Azure アカウントと有効なサブスクリプション」が追加され、利用開始前の準備が明確化されています。また、Visual Studio CodeとRESTクライアントについての記述も適切な順序に整理されています。

4. **ノートのテキストの調整**: “Free tier”に関するノートの表現が微調整され、クリアで読みやすくなりました。

5. **サンプルデータファイルの追加**: ダウンロード可能なサンプルデータファイルに関する情報が追加され、いくつかの新しいリンクが提供されています。

全体として、この更新は文書の構成と可読性を向上させており、特に学習者が必要な情報をより容易に見つけられるようになっています。ユーザーエクスペリエンスを向上させることが期待され、より良い学習体験を提供します。

## articles/search/cognitive-search-tutorial-debug-sessions.md{#item-7e10e9}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Tutorial: Debug skillsets'
+title: 'Tutorial: Debug Skillsets'
 titleSuffix: Azure AI Search
 description: Practice creating and completing a debug session on an Azure AI Search skillset. This tutorial provides a buggy sample skillset that you resolve in a debug session.
 
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: tutorial
-ms.date: 12/03/2024
+ms.date: 03/31/2025
 ---
 
 # Tutorial: Fix a skillset using Debug Sessions
@@ -19,15 +19,15 @@ In Azure AI Search, a skillset coordinates the actions of skills that analyze, t
 
 **Debug Sessions** is an Azure portal tool that provides a holistic visualization of a skillset that executes on Azure AI Search. Using this tool, you can drill down to specific steps to easily see where an action might be falling down.
 
-In this article, use **Debug Sessions** to find and fix missing inputs and outputs. The tutorial is all-inclusive. It provides sample data, a REST file that creates objects, and instructions for debugging problems in the skillset.
-
-If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
+In this tutorial, you use **Debug Sessions** to find and fix missing inputs and outputs. The tutorial is all-inclusive. It provides sample data, a REST file that creates objects, and instructions for debugging problems in the skillset.
 
 ## Prerequisites
 
-+ Azure AI Search. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) under your current subscription. You can use a free service for this tutorial. The free tier doesn't provide managed identity support for an Azure AI Search service. You must use keys for connections to Azure Storage.
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+
++ Azure AI Search. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription. You can use a free service for this tutorial. The Free tier doesn't provide managed identity support for an Azure AI Search service. You must use keys for connections to Azure Storage.
 
-+ Azure Storage account with [Blob storage](/azure/storage/blobs/), used for hosting sample data, and for persisting cached data created during a debug session. If you're using a free search service, the storage account must have shared access keys enabled and it must allow public network access.
++ Azure Storage account with [Blob storage](/azure/storage/blobs/), used for hosting sample data and for persisting cached data created during a debug session. If you're using a free search service, the storage account must have shared access keys enabled and it must allow public network access.
 
 + [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
@@ -44,29 +44,29 @@ This section creates the sample data set in Azure Blob Storage so that the index
 
 1. [Download sample data (clinical-trials-pdf-19)](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/_ARCHIVE/clinical-trials/clinical-trials-pdf-19), consisting of 19 files.
 
-1. [Create an Azure Storage account](/azure/storage/common/storage-account-create?tabs=azure-portal) or [find an existing account](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Storage%2storageAccounts/). 
+1. [Create an Azure Storage account](/azure/storage/common/storage-account-create?tabs=azure-portal) or [find an existing account](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Storage%2storageAccounts/).
 
    + Choose the same region as Azure AI Search to avoid bandwidth charges.
 
    + Choose the StorageV2 (general purpose V2) account type.
 
-1. Navigate to the Azure Storage services pages in the Azure portal and create a Blob container. Best practice is to specify the access level "private". Name your container `clinicaltrialdataset`.
+1. Go to the Azure Storage services pages in the Azure portal and create a Blob container. Best practice is to specify the access level "private". Name your container `clinicaltrialdataset`.
 
 1. In container, select **Upload** to upload the sample files you downloaded and unzipped in the first step.
 
-1. While in the Azure portal, copy the connection string for Azure Storage. You can get the connection string from **Settings** > **Access Keys** in the Azure portal.
+1. In the Azure portal, select **Settings** > **Access Keys** and copy the connection string for Azure Storage.
 
 ## Copy a key and URL
 
 This tutorial uses API keys for authentication and authorization. You need the search service endpoint and an API key, which you can get from the Azure portal.
 
-1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
+1. Sign in to the [Azure portal](https://portal.azure.com), go to the **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
 
 1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
 
    :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
 
-A valid API key establishes trust, on a per request basis, between the application sending the request and the search service handling it.
+A valid API key establishes trust, on a per-request basis, between the application sending the request and the search service handling it.
 
 ## Create data source, skillset, index, and indexer
 
@@ -82,9 +82,9 @@ In this section, create a "buggy" workflow that you can fix in this tutorial.
 
 ## Check results in the Azure portal
 
-The sample code intentionally creates a buggy index as a consequence of problems that occurred during skillset execution. The problem is that the index is missing data. 
+The sample code intentionally creates a buggy index as a consequence of problems that occurred during skillset execution. The problem is that the index is missing data.
 
-1. In Azure portal, on the search service **Overview** page, select the **Indexes** tab. 
+1. In Azure portal, on the search service **Overview** page, select the **Indexes** tab.
 
 1. Select *clinical-trials*.
 
@@ -98,15 +98,15 @@ The sample code intentionally creates a buggy index as a consequence of problems
 
 1. Run the query. You should see empty values for `organizations` and `locations`.
 
-    These fields should have been populated through the skillset's [Entity Recognition skill](cognitive-search-skill-entity-recognition-v3.md), used to detect organizations and locations anywhere within the blob's content. In the next exercise, you'll debug the skillset to determine what went wrong.
+    These fields should have been populated through the skillset's [Entity Recognition skill](cognitive-search-skill-entity-recognition-v3.md), used to detect organizations and locations anywhere within the blob's content. In the next exercise, you debug the skillset to determine what went wrong.
 
 Another way to investigate errors and warnings is through the Azure portal.
 
-1. Open the **Indexers** tab and select *clinical-trials-idxr*.
+1. On the **Indexers** tab, select *clinical-trials-idxr*.
 
    Notice that while the indexer job succeeded overall, there were warnings.
 
-1. Select **Success** to view the warnings (if there were mostly errors, the detail link would be **Failed**). You'll see a long list of every warning emitted by the indexer.
+1. Select **Success** to view the warnings. If there are mostly errors, the detail link is **Failed**. You should see a long list of every warning emitted by the indexer.
 
    :::image type="content" source="media/cognitive-search-debug/portal-indexer-errors-warnings.png" alt-text="Screenshot of view warnings." :::
 
@@ -116,27 +116,27 @@ Another way to investigate errors and warnings is through the Azure portal.
 
 1. Select **+ Add Debug Session**.
 
-1. Give the session a name. 
+1. Give the session a name.
 
 1. In Indexer template, provide the indexer name. The indexer has references to the data source, the skillset, and index.
 
 1. Select the storage account.
 
-1. **Save** the session. 
+1. **Save** the session.
 
    :::image type="content" source="media/cognitive-search-debug/debug-tutorial-create-session.png" lightbox="media/cognitive-search-debug/debug-tutorial-create-session.png" alt-text="Screenshot of Debug session definition page." :::
   
 1. A debug session opens to the settings page. You can make modifications to the initial configuration and override any defaults. A debug session only works with a single document. The default is to accept the first document in the collection as the basis of your debug sessions. You can [choose a specific document to debug](cognitive-search-how-to-debug-skillset.md#create-a-debug-session) by providing its URI in Azure Storage.
 
-1. When the debug session has finished initializing, you should see a skills workflow with mappings and a search index. The enriched document data structure appears in a details pane on the side. We excluded it from the following screenshot so that you could see more of the workflow.
+1. When the debug session finishes initializing, you should see a skills workflow with mappings and a search index. The enriched document data structure appears in a details pane on the side. We excluded it from the following screenshot so that you could see more of the workflow.
 
    :::image type="content" source="media/cognitive-search-debug/debug-execution-complete1.png" lightbox="media/cognitive-search-debug/debug-execution-complete1.png" alt-text="Screenshot of Debug Session visual editor." :::
 
 ## Find issues with the skillset
 
 Any issues reported by the indexer are indicated as **Errors** and **Warnings**.
 
-Notice that the number of errors and warning is a much smaller list than the one displayed earlier because this list is only detailing the errors for a single document. Like the list displayed by the indexer, you can select on a warning message and see the details of this warning.
+Notice that the number of errors and warnings is a smaller list than the one displayed earlier because this list is only detailing the errors for a single document. Like the list displayed by the indexer, you can select on a warning message and see the details of this warning.
 
 Select **Warnings** to review the notifications. You should see four:
 
@@ -163,7 +163,7 @@ Because all four notifications are about this skill, your next step is to debug
 
    :::image type="content" source="media/cognitive-search-debug/debug-tutorial-skill-detail.png" alt-text="Screenshot of the skill details pane.":::
 
-1. Hover over each input (or select an input) to show the values in the **Expression evaluator**. Notice that the displayed result for this input doesn’t look like a text input. It looks like a series of new line characters `\n \n\n\n\n` instead of text. The lack of text means that no entities can be identified, so either this document fails to meet the prerequisites of the skill, or there's another input that should be used instead.
+1. Hover over each input (or select an input) to show the values in the **Expression evaluator**. Notice that the displayed result for this input doesn’t look like a text input. It looks like a series of new line characters `\n \n\n\n\n` instead of text. The lack of text means that no entities can be identified. Either this document doesn't meet the prerequisites of the skill, or there's another input that should be used instead.
 
    :::image type="content" source="media/cognitive-search-debug/debug-tutorial-skill-input-null.png" alt-text="Screenshot of skill input showing null values.":::
 
@@ -177,7 +177,7 @@ Because all four notifications are about this skill, your next step is to debug
 
    :::image type="content" source="media/cognitive-search-debug/debug-tutorial-edit-skill.png" alt-text="Screenshot of Expression Evaluator for fixed merged_content input." :::
 
-1. Select **Run** in the session's window menu. This kicks off another execution of the skillset using the document. 
+1. Select **Run** in the session's window menu. This kicks off another execution of the skillset using the document.
 
 1. Once the debug session execution completes, notice that the warnings count has reduced by one. Warnings show that the error for text input is gone, but the other warnings remain. The next step is to address the warning about the missing or empty value `/document/languageCode`.
 
@@ -221,11 +221,11 @@ The messages say to check the 'outputFieldMappings' property of your indexer, so
 
 1. Select **Run**.
 
-All of the errors have been resolved.
+All of the errors are resolved.
 
 ## Commit changes to the skillset
 
-When the debug session was initiated, the search service created a copy of the skillset. This was done to protect the original skillset on your search service. Now that you have finished debugging your skillset, the fixes can be committed (overwrite the original skillset). 
+When the debug session was initiated, the search service created a copy of the skillset. This was done to protect the original skillset on your search service. Now that you debugged your skillset, the fixes can be committed (overwrite the original skillset).
 
 Alternatively, if you aren't ready to commit changes, you can save the debug session and reopen it later.
 
@@ -243,7 +243,7 @@ Alternatively, if you aren't ready to commit changes, you can save the debug ses
 
 1. Select **Refresh** to show the status of the reset and run commands.
 
-When the indexer has finished running, there should be a green checkmark and the word Success next to the time stamp for the latest run in the **Execution history** tab. To ensure that the changes have been applied:
+When the indexer finishes running, there should be a green checkmark and the word Success next to the time stamp for the latest run in the **Execution history** tab. To ensure that the changes are applied:
 
 1. In the left pane, open **Indexes**.
 
@@ -263,7 +263,7 @@ The free service is limited to three indexes, indexers, and data sources. You ca
 
 ## Next steps
 
-This tutorial touched on various aspects of skillset definition and processing. To learn more about concepts and workflows, refer to the following articles:
+This tutorial touched on various aspects of skillset definition and processing. To learn more about concepts and workflows, see the following articles:
 
 + [How to map skillset output fields to fields in a search index](cognitive-search-output-field-mapping.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デバッグセッションチュートリアルの内容更新"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-tutorial-debug-sessions.md`ファイルに対して行われた修正を示しています。主な更新点は以下の通りです。

1. **タイトルの変更**: タイトルが「Tutorial: Debug skillsets」から「Tutorial: Debug Skillsets」に変更され、大文字が適用されてより一貫性のある表現になりました。

2. **日付の更新**: 文書の日付が2024年12月3日から2025年3月31日に更新され、最新の情報を反映しています。

3. **内容の修正**:
   - デバッグセッションを使用して、入力と出力の欠落を見つけて修正する方法を強調する文が更新され、より明確な説明が追加されました。
   - プリレクイジット（前提条件）において、言葉の順序が整理され、新しい項目として「Visual Studio Code」が追加され、RESTクライアントを用いる準備が強調されています。

4. **手順の整備**: 手順の構造が全体的に見直され、各ステップが明確に整理されました。番号付きリストは一貫性を持たせるために修正され、情報の流れが改善されています。

5. **言語の明確化**: 特に「成功」や「エラー」についての表現が微調整され、より自然な日本語として流暢さが向上しました。また、該当部分の説明が簡潔かつ明瞭になり、読み手が理解しやすくなっています。

この変更は、全体的にドキュメントの整合性と可読性を向上させ、学習者が情報を理解しやすくするための改善に寄与しています。これにより、ユーザーがデバッグセッションを通じて問題解決のスキルを効果的に学ぶことができることが期待されます。

## articles/search/includes/previews/preview-generic.md{#item-51bbcc}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +1,13 @@
 ---
-title: include file
-description: include file
+title: Include file
+description: Include file
 author: eric-urban
 ms.author: eur
 ms.service: azure-ai-speech
 ms.topic: include
-ms.date: 9/20/2024
+ms.date: 03/19/2024
 ms.custom: include, ignite-2024
 ---
 
 > [!NOTE]
-> This feature is currently in public preview. This preview is provided without a service-level agreement, and is not recommended for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
+> This feature is currently in public preview. This preview is provided without a service-level agreement and isn't recommended for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレビュー機能情報の修正"
}
```

### Explanation
この変更は、`articles/search/includes/previews/preview-generic.md`ファイルにおける修正を反映しています。主な更新点は以下の通りです。

1. **タイトルの変更**: タイトルが「include file」から「Include file」に変更され、大文字が適用され、一貫性が持たれるようになりました。

2. **説明の修正**: 説明部分も同様に「include file」から「Include file」に変更され、タイトルと合わせて整形されています。

3. **日付の更新**: 文書の日付が2024年9月20日から2024年3月19日に更新され、新たな情報が反映されています。

4. **内容の明確化**: 項目に関連する注意書きの文章が少しだけ調整され、「isn't recommended for production workloads」という表現に変更され、文がより自然な流れになっています。これにより、読者に対する情報伝達がより効果的になることが期待されます。

この全体的な変更は、文書の整合性を高め、精度を向上させることに寄与しており、特にプレビュー機能を利用するユーザーに対して明確な情報を提供する助けとなります。

## articles/search/media/search-capacity-planning/add-two-each.png{#item-56b26e}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: add-two-each.png"
}
```

### Explanation
この変更は、`articles/search/media/search-capacity-planning/add-two-each.png`という画像ファイルが新たに追加されたことを示しています。この画像は、検索のキャパシティプランニングに関連する内容を視覚的に提供するためのものです。

画像の追加により、ドキュメントの理解が向上し、読者に対してより具体的な情報を提供できるようになります。特に、視覚的な要素は、複雑な概念の理解を助けるため、学習効果を高めるために重要な役割を果たします。これにより、関連するトピックに対する説明がより明確になり、その影響力が増すことが期待されます。

## articles/search/media/search-capacity-planning/change-pricing-tier.png{#item-f71721}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: change-pricing-tier.png"
}
```

### Explanation
この変更は、`articles/search/media/search-capacity-planning/change-pricing-tier.png`という新しい画像ファイルが追加されたことを示しています。この画像は、キャパシティプランニングにおける価格設定の変更に関連する情報を視覚的に提供する目的で作成されています。

新しい画像の追加により、ドキュメントはより分かりやすくなり、概念の理解が深まることが期待されます。特に、価格設定やその変更に関する複雑な情報を、視覚的な手段によって補完することで、読者にとっての理解を助け、重要なポイントを強調する役割を果たすことになります。これにより、学習体験や実践において、より効果的な情報伝達が可能となります。

## articles/search/media/search-capacity-planning/initial-values.png{#item-465304}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: initial-values.png"
}
```

### Explanation
この変更は、`articles/search/media/search-capacity-planning/initial-values.png`という新しい画像ファイルの追加を示しています。この画像は、キャパシティプランニングにおける初期値に関連する情報を視覚的に示すために使用されます。

新たに追加されたこの画像は、ドキュメントの内容をより具体的に理解する手助けをし、読者が初期値設定の概念を把握しやすくする向上に寄与します。視覚的な要素は特に説明を明確にするために重要で、情報の提供方法を多様化させることで、読者に対して効果的な学習体験を提供します。この変更により、検索のキャパシティプランニングに関する具体的な実例や理解が得やすくなることが期待されます。

## articles/search/media/search-capacity-planning/portal-notifications.png{#item-4bd098}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: portal-notifications.png"
}
```

### Explanation
この変更は、`articles/search/media/search-capacity-planning/portal-notifications.png`という新しい画像ファイルが追加されたことを示します。この画像は、キャパシティプランニングプロセスにおけるポータル通知の重要性や内容を視覚的に示すために設計されています。

新たに追加された画像は、文書における重要な情報を補足する役割を果たし、ポータルでの通知に関する理解を深める手助けをします。視覚的な要素を取り入れることで、読者は通知がどのように表示され、どのように情報を処理するかを容易に把握できるようになります。この変更により、キャパシティプランニングに関連する操作やアクションをより効果的に理解し、実践するための支援が提供されることが期待されます。

## articles/search/media/search-capacity-planning/pricing-tier-list.png{#item-ff6b12}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: pricing-tier-list.png"
}
```

### Explanation
この変更は、`articles/search/media/search-capacity-planning/pricing-tier-list.png`という新しい画像ファイルが追加されたことを示しています。この画像は、キャパシティプランニングにおける料金プランのリストを視覚的に表現するために作成されました。

新たに追加されたこの画像は、異なる料金プランやサービスレベルを示すことで、ユーザーが選択可能なオプションを理解しやすくします。視覚的な情報は、料金設定の違いや特長を一目で比較できるようにし、適切なプランを選択するための手助けとなります。この変更により、ユーザーは検索サービスの価格帯をより明確に理解し、より良いプラン選択に役立てることが期待されます。

## articles/search/media/search-capacity-planning/provisioning-status.png{#item-ede201}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: provisioning-status.png"
}
```

### Explanation
この変更は、`articles/search/media/search-capacity-planning/provisioning-status.png`という新しい画像ファイルが追加されたことを示しています。この画像は、キャパシティプランニングにおけるプロビジョニングの状態を視覚的に表現するために設計されています。

追加された画像は、プロビジョニングプロセスの進捗状況や状態を示すことで、ユーザーがシステムの準備状況を簡単に理解できるようにします。視覚的な情報を活用することで、ユーザーはどの段階にいるのか、何が完了していて何が残っているのかを一目で把握することができます。この変更により、キャパシティプランニングの効率が向上し、ユーザーはより迅速に必要なアクションを判断できるようになることが期待されます。

## articles/search/media/search-capacity-planning/updating-message.png{#item-fc9f1b}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: updating-message.png"
}
```

### Explanation
この変更は、`articles/search/media/search-capacity-planning/updating-message.png`という新しい画像ファイルが追加されたことを示しています。この画像は、キャパシティプランニングの過程において更新メッセージを視覚的に表現するために設計されています。

追加されたこの画像は、システムが更新を行っている際のメッセージを示すことで、ユーザーに対して現在の状況や進行中の操作についての理解を助けます。視覚的な要素を取り入れることにより、ユーザーは更新が行われていることを即座に把握でき、必要な場合にはその間の行動を調整することが可能になります。この変更により、ユーザー体験が向上し、キャパシティプランニングプロセスにおける情報の透明性が確保されることが期待されます。

## articles/search/media/search-faceted-navigation/portal-add-facetable-field.png{#item-d0b7a4}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: portal-add-facetable-field.png"
}
```

### Explanation
この変更は、`articles/search/media/search-faceted-navigation/portal-add-facetable-field.png`という新しい画像ファイルが追加されたことを示しています。この画像は、ファセットナビゲーションを用いたポータルでのファセットテーブルフィールドの追加に関する説明を視覚的に支援します。

追加された画像は、ユーザーがファセットテーブルフィールドをポータルに追加する方法を示すことで、操作手順を直感的に理解できるように設計されています。このビジュアルガイドにより、ユーザーは手順を容易に追うことができ、効率的に必要な設定を行うことができるようになります。この変更は、特に初めてこの機能を使用するユーザーにとって役立つものであり、全体的なユーザー体験の向上に寄与することが期待されます。

## articles/search/media/search-faceted-navigation/portal-facet-query.png{#item-57be1f}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: portal-facet-query.png"
}
```

### Explanation
この変更は、`articles/search/media/search-faceted-navigation/portal-facet-query.png`という新しい画像ファイルが追加されたことを示しています。この画像は、ファセットナビゲーションのポータルにおいてファセットクエリの構成方法を視覚的に説明するために設計されています。

追加された画像は、ユーザーがファセットクエリを利用して、データの絞り込みや検索結果の精度を高める方法を直感的に理解できるようにサポートします。このビジュアルは、特に初心者ユーザーにとってそのプロセスを容易にし、理解を深めるために役立ちます。この変更により、ユーザーはファセットナビゲーションの機能をより効果的に活用できるようになり、全体の操作体験が向上することが期待されます。

## articles/search/media/search-how-to-index-sql-database/search-data-source.png{#item-e559ff}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: search-data-source.png"
}
```

### Explanation
この変更は、`articles/search/media/search-how-to-index-sql-database/search-data-source.png`という新しい画像ファイルが追加されたことを示しています。この画像は、SQLデータベースのインデックス作成に関する手順を視覚的に説明するために使用されます。

追加された画像は、ユーザーが検索データソースを設定する方法や、SQLデータベースをどのようにインデックスできるかを簡単に理解できるように設計されています。このビジュアルは、特に新しいユーザーや手順に不慣れなユーザーにとって、操作を行う上での参照として役立ちます。したがって、ユーザー体験が向上し、SQLデータベースのインデックス作成プロセスがよりスムーズになることが期待されます。

## articles/search/media/search-how-to-upgrade/service-creation-upgrade-metadata.png{#item-d1251d}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: service-creation-upgrade-metadata.png"
}
```

### Explanation
この変更は、`articles/search/media/search-how-to-upgrade/service-creation-upgrade-metadata.png`という新しい画像ファイルが追加されたことを示しています。この画像は、サービス作成のアップグレードに関連するメタデータの管理方法を視覚的に説明するために設計されています。

追加された画像は、ユーザーがアップグレードプロセスをよりスムーズに理解し、具体的な手順を踏むための参照として役立ちます。特に、サービスのアップグレードに不安を感じているユーザーに対して、視覚的なガイドラインを提供することで、理解を助けることが期待されます。この変更により、ユーザーはサービス作成のアップグレードに関する情報をより効果的に活用できるようになります。

## articles/search/media/search-how-to-upgrade/upgrade-button.png{#item-894e31}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: upgrade-button.png"
}
```

### Explanation
この変更は、`articles/search/media/search-how-to-upgrade/upgrade-button.png`という新しい画像ファイルが追加されたことを示しています。この画像は、アップグレードボタンの使用方法を視覚的に説明するために作成されました。

追加された画像は、ユーザーがアップグレードプロセスを実行する際に、どのボタンをクリックすればよいかを明確に示すためのものです。この視覚的な補助により、特にアップグレードに慣れていないユーザーが操作を理解しやすくなることが期待されています。ユーザーは、アップグレードボタンの存在とその使用方法を確認することで、手順をスムーズに進めることができるでしょう。この変更により、ユーザー体験の向上が図られています。

## articles/search/media/search-how-to-upgrade/upgrade-confirmation.png{#item-880793}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: upgrade-confirmation.png"
}
```

### Explanation
この変更は、`articles/search/media/search-how-to-upgrade/upgrade-confirmation.png`という新しい画像ファイルが追加されたことを示しています。この画像は、アップグレードが成功したことを確認するための視覚的なフィードバックを提供するためにデザインされています。

追加された画像は、ユーザーに対してアップグレード確認メッセージの様子を示しており、アップグレード処理が正常に完了したことを知る手助けをします。この環境を整えることで、ユーザーは自信を持って次のステップに進むことができ、手続きをより安心して進めることが可能になります。この変更は、特に手続きの透明性を高めるため、ユーザー体験の向上を図っています。

## articles/search/media/search-how-to-upgrade/upgrade-panel.png{#item-0c9673}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: upgrade-panel.png"
}
```

### Explanation
この変更は、`articles/search/media/search-how-to-upgrade/upgrade-panel.png`という新しい画像ファイルが追加されたことを示しています。この画像は、ユーザーがアップグレードパネルのインターフェースを視覚的に理解するのをサポートするために作成されました。

追加された画像は、アップグレード手順の一環として、どのようにアップグレードパネルを使用するかを示すためのものであり、ユーザーがその機能や操作方法を正確に把握できるようにしています。この視覚的情報は、特にアップグレードの手続きに不安を感じるユーザーにとって助けになります。結果的に、この変更は全体のユーザー体験を向上させ、よりスムーズな作業を実現することを目的としています。

## articles/search/media/search-security-manage-encryption-keys/assign-key-vault.png{#item-e19e19}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加: assign-key-vault.png"
}
```

### Explanation
この変更は、`articles/search/media/search-security-manage-encryption-keys/assign-key-vault.png`という新しい画像ファイルが追加されたことを示しています。この画像は、暗号化キーの管理に関するコンテキストで、ユーザーがKey Vaultを割り当てる際の手順やインターフェースを視覚的に説明することを目的としています。

新たに追加されたこの画像は、ユーザーに対してKey Vaultの使用方法を示すためのものであり、関連する設定や選択がどのようになるかを一步的に理解させる助けになります。これにより、ユーザーは暗号化キーの管理プロセスをより簡単に把握でき、特にセキュリティやコンプライアンスの観点から重要なフィーチャーを効果的に利用できるようになります。この変更は、ドキュメントの全体的な明瞭さを向上させ、ユーザー体験の質を高めることに寄与しています。

## articles/search/resource-training.md{#item-07788d}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 10/28/2024
+ms.date: 04/07/2025
 ---
 
 # Training - Azure AI Search
@@ -27,10 +27,9 @@ Learning paths are a collection of training modules that are organized around sp
 
 | Module | Learning path |
 |--------|---------------|
-[Fundamentals of Knowledge Mining and Azure AI Search](/training/modules/intro-to-azure-search/) | [Microsoft Azure AI Fundamentals:](/training/paths/document-intelligence-knowledge-mining/) |
+[Fundamentals of Knowledge Mining and Azure AI Search](/training/modules/intro-to-azure-search/) | [Microsoft Azure AI Fundamentals](/training/paths/document-intelligence-knowledge-mining/) |
 | [Create an Azure AI Search solution](/training/modules/create-azure-cognitive-search-solution/) | [Implement knowledge mining](/training/paths/implement-knowledge-mining-azure-cognitive-search/) |
 | [Create a custom skill for Azure AI Search](/training/modules/create-azure-ai-custom-skill/) | [Implement knowledge mining](/training/paths/implement-knowledge-mining-azure-cognitive-search/) |
-| [Build an Azure Machine Learning custom skill for Azure AI Search](/training/modules/build-azure-machine-learn-custom-skill-for-azure-cognitive-search/) | |
 | [Enrich your data with Azure AI Language](/training/modules/enrich-search-index-using-language-studio/) | |
 | [Create a knowledge store with Azure AI Search](/training/modules/create-knowledge-store-azure-cognitive-search/) | [Implement knowledge mining](/training/paths/implement-knowledge-mining-azure-cognitive-search/) |
 | [Implement advanced search features in Azure AI Search](/training/modules/implement-advanced-search-features-azure-cognitive-search/)| [Implement knowledge mining](/training/paths/implement-knowledge-mining-azure-cognitive-search/) |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソーストレーニング文書の更新"
}
```

### Explanation
この変更は、`articles/search/resource-training.md`ファイルに対する更新で、いくつかの修正と日付の変更を含んでいます。具体的には、以前の更新日が「2024年10月28日」から「2025年4月7日」に変更され、訓練モジュールの表にも若干の調整が加えられました。

変更された内容には、トレーニングモジュールに関連するリンクの表記方法に若干の修正が含まれており、特に学習パスのタイトルが整理されました。これにより、ユーザーが提供されるリソースの理解を深めやすくなっています。文書の構造や表の内容が改善されることで、情報がより明確に伝わるようになり、トレーニングリソースを利用するユーザーの体験を向上させることを目的としています。

## articles/search/search-api-migration.md{#item-07297b}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: conceptual
-ms.date: 02/14/2025
+ms.date: 03/10/2025
 ---
 
 # Upgrade to the latest REST API in Azure AI Search
@@ -24,7 +24,7 @@ Use this article to migrate to newer versions of the [**Search Service REST APIs
 | Data plane | [`2024-07-01`](/rest/api/searchservice/search-service-api-versions#2024-07-01) | Stable |
 | Data plane | [`2024-11-01-preview`](/rest/api/searchservice/search-service-api-versions#2024-11-01-preview) | Preview |
 | Control plane | [`2023-11-01`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2023-11-0&preserve-view=true1) | Stable |
-| Control plane | [`2024-03-01-preview`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2024-03-01-preview&preserve-view=true) | Preview |
+| Control plane | [`2025-02-01-preview`](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true) | Preview |
 
 Upgrade instructions focus on code changes that get you through breaking changes from previous versions so that existing code runs the same as before, but on the newer API version. Once your code is in working order, you can decide whether to adopt newer features. To learn more about new features, see [vector code samples](https://github.com/Azure/azure-search-vector-samples) and [What's New](whats-new.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索API移行文書の更新"
}
```

### Explanation
この変更は、`articles/search/search-api-migration.md`ファイルの更新を示しており、文書の日付やAPIバージョンに関する情報が修正されています。具体的には、文書の日付が「2025年2月14日」から「2025年3月10日」に変更され、コントロールプレーンのプレビューAPIバージョンが「2024-03-01-preview」から「2025-02-01-preview」に更新されました。

これらの変更は、最新のREST APIバージョンに移行する際の情報を最新のものに保つために行われました。文書のアップグレード手順では、古いバージョンとの互換性を保ちながら、新しいAPIバージョンに適応するためのコードの変更に焦点を当てています。このようにして、ユーザーは最新の機能を利用できるようになるとともに、既存のコードが引き続き正しく動作する確保されています。全体として、ユーザーがAPIをスムーズに移行できるように、明確な情報が提供されています。

## articles/search/search-api-preview.md{#item-511f5d}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: conceptual
-ms.date: 11/05/2024
+ms.date: 03/31/2025
 ---
 
 # Preview features in Azure AI Search
@@ -26,6 +26,9 @@ Preview features are removed from this list if they're retired or transition to
 
 |Feature&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Category | Description | Availability  |
 |---------|------------------|-------------|---------------|
+| [**flightingOptIn parameter in a semantic configuration**](semantic-how-to-configure.md#opt-in-for-prerelease-semantic-ranking-models) | Queries| You can opt in to use prerelease semantic ranking models if one is available in a search service region. | [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true). |
+| [**Rescore vector queries over binary embeddings using full precision vectors**](vector-search-how-to-quantization.md#recommended-rescoring-techniques) | Relevance (scoring) | For vector indexes that contain quantized binary embeddings, you can rescore query results using a full precision query vector. The query engine uses the dot product for rescoring, which improves the quality of search results. Set `enableRescoring` and `discardOriginals` to use this feature.| [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true). |
+| [**Facet hierarchies, aggregations, and facet filters**](search-faceted-navigation-examples.md) | Queries| New facet query parameters support nested facets. For numeric facetable fields, you can sum the values of each field. You can also specify filters on a facet to add inclusion or exclusion criteria. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-03-01-preview&preserve-view=true). |
 | [**Query rewrite in the semantic reranker**](semantic-how-to-query-rewrite.md) | Relevance (scoring) | You can set options on a semantic query to rewrite the query input into a revised or expanded query that generates more relevant results from the L2 ranker. | [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-11-01-preview&preserve-view=true).|
 | [**Document Layout skill**](cognitive-search-skill-document-intelligence-layout.md) | Applied AI (skills) | A new skill used to analyze a document for structure and provide [structure-aware chunking](search-how-to-semantic-chunking.md). | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true). |
 | [**Keyless billing for Azure AI skills processing**](cognitive-search-attach-cognitive-services.md). | Applied AI (skills) | You can now use a managed identity and roles for a keyless connection to Azure AI services for built-in skills processing. This capability removes restrictions for having both search and AI services in the same region.  | [Create or Update Skillset  (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true).|
@@ -57,7 +60,9 @@ Preview features are removed from this list if they're retired or transition to
 
 |Feature&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Category | Description | Availability  |
 |---------|------------------|-------------|---------------|
-| [**Network security perimeter**](search-security-network-security-perimeter.md) | Service | Join a search service to a [network security perimeter](/azure/private-link/network-security-perimeter-concepts) to control network access to your search service. | The Azure portal and the [Network Security Perimeter APIs 2024-06-01-preview](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true). |
+| [**Service upgrade**](search-how-to-upgrade.md) | Feature | Upgrade your search service to higher storage limits in your region. With a one-time upgrade, you no longer need to recreate your service. | The Azure portal and [Upgrade Service (2025-02-01-preview)](/rest/api/searchmanagement/services/upgrade?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true). |
+| [**Pricing tier change**](search-capacity-planning.md#change-your-pricing-tier) | Feature | Change the [pricing tier](search-sku-tier.md) of your search service. This provides flexibility to scale storage, increase request throughput, and decrease latency based on your needs. In this preview, you can only change between Basic and Standard (S1, S2, and S3) tiers. | The Azure portal and [Update Service (2025-02-01-preview)](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true#searchupdateservicewithsku). |
+| [**Network security perimeter**](search-security-network-security-perimeter.md) | Service | Join a search service to a [network security perimeter](/azure/private-link/network-security-perimeter-concepts) to control network access to your search service. | The Azure portal and the [Network Security Perimeter APIs 2024-06-01-preview](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true) or the latest preview version. |
 | [**Search service under a user-assigned managed identity**](search-howto-managed-identities-data-sources.md) | Service | Configures a search service to use a previously created user-assigned managed identity. | [Services - Update](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true#identity), 2021-04-01-preview, or the latest preview version. We recommend using the latest preview version. |
 
 ## Preview features in Azure SDKs
@@ -91,10 +96,10 @@ For data plane operation on content, [**`2024-05-01-preview`**](/rest/api/search
 GET {endpoint}/indexes('{indexName}')?api-version=2024-05-01-Preview
 ```
 
-For management operations on the search service, [**`2024-06-01-preview`**](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true) is the most recent preview version. The following example shows the syntax for Update Service 2024-06-01-preview version.
+For management operations on the search service, [**`2025-05-01-preview`**](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2025-05-01-preview&preserve-view=true) is the most recent preview version. The following example shows the syntax for Update Service 2025-05-01-preview version.
 
 ```rest
-PATCH https://management.azure.com/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Search/searchServices/mysearchservice?api-version=2024-06-01-preview
+PATCH https://management.azure.com/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Search/searchServices/mysearchservice?api-version=2025-05-01-preview
 
 {
   "tags": {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索APIプレビュー文書の更新"
}
```

### Explanation
この変更は、`articles/search/search-api-preview.md`ファイルの更新を示しており、主に日付の変更やプレビュー機能に関する情報が追加されています。文書の日付が「2024年11月5日」から「2025年3月31日」に変更され、いくつかの新しい機能や更新の詳細が追加されました。

新しく追加された機能には、セマンティック構成における`flightingOptIn`パラメータ、バイナリエンベディングを使用したクエリの再スコアリング、階層的フェイシングや集計、フィルター機能の追加が含まれています。また、検索サービスをより高いストレージ制限にアップグレードする機能や、プライシングテーブルの変更といった新機能も紹介されています。

これにより、ユーザーは最新の機能やAPI使用のバージョンについての情報を把握でき、検索APIの移行や実装の際に役立つリソースが提供されます。この更新は、ユーザーが新しい機能を利用する際の参考として有用であり、技術文書の精度と有用性を向上させています。

## articles/search/search-capacity-planning.md{#item-0dd6c9}

<details>
<summary>Diff</summary>
````diff
@@ -11,14 +11,14 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: conceptual
-ms.date: 03/11/2025
+ms.date: 03/31/2025
 ---
 
 # Estimate and manage capacity of a search service
 
 In Azure AI Search, capacity is based on *replicas* and *partitions* that can be scaled to your workload. Replicas are copies of the search engine. Partitions are units of storage. Each new search service starts with one each, but you can add or remove replicas and partitions independently to accommodate fluctuating workloads. Adding capacity increases the [cost of running a search service](search-sku-manage-costs.md#billable-events).
 
-The physical characteristics of replicas and partitions, such as processing speed and disk IO, vary by [service tier](search-sku-tier.md). On a standard search service, the replicas and partitions are faster and larger than those of a basic service.
+The physical characteristics of replicas and partitions, such as processing speed and disk IO, vary by [pricing tier](search-sku-tier.md). On a standard search service, the replicas and partitions are faster and larger than those of a basic service.
 
 Changing capacity isn't instantaneous. It can take up to an hour to commission or decommission partitions, especially on services with large amounts of data.
 
@@ -30,73 +30,121 @@ When scaling a search service, you can choose from the following tools and appro
 + [Management REST API](/rest/api/searchmanagement/services/create-or-update)
 
 > [!NOTE]
-> Higher capacity partitions are available at the same billing rate on newer services created after April and May 2024. For more information, see [Service limits](search-limits-quotas-capacity.md#service-limits) for partition size upgrades.
+> If your service was created before April or May 2024, a one-time upgrade to higher storage limits might be available at no extra cost. For more information, see [Upgrade your search service](search-how-to-upgrade.md).
 
 ## Concepts: search units, replicas, partitions
 
 Capacity is expressed in *search units* that can be allocated in combinations of *partitions* and *replicas*.  
 
 | Concept  | Definition|
 |----------|-----------|
-|*Search unit* | A single increment of total available capacity (36 units). A minimum of one unit is required to run the service. The first replica and partition pair is the first search unit. However, each extra instance of a replica *or* a partition consumes an extra search unit. For example, you start with one replica and partition (one search unit), add a second replica, you are now consuming two search units. A search unit is also the billing unit for an Azure AI Search service. |
+|*Search unit* | A single increment of total available capacity (36 units). A minimum of one unit is required to run the service. The first replica and partition pair is the first search unit. However, each extra instance of a replica *or* a partition consumes an extra search unit. For example, you start with one replica and partition (one search unit), add a second replica, you're now consuming two search units. A search unit is also the billing unit for an Azure AI Search service. |
 |*Replica* | Instances of the search service, used primarily to load balance query operations. Each replica hosts one copy of an index. If you allocate three replicas, you have three copies of an index available for servicing query requests.|
 |*Partition* | Physical storage and I/O for read/write operations (for example, when rebuilding or refreshing an index). Each partition has a slice of the total index. If you allocate three partitions, your index is divided into thirds. |
 
-Review the [partitions and replicas table](#partition-and-replica-combinations) for possible combinations that stay under the 36 unit limit. 
+Review the [partitions and replicas table](#partition-and-replica-combinations) for possible combinations that stay under the 36 unit limit.
 
 ## When to add capacity
 
-Initially, a service is allocated a minimal level of resources consisting of one partition and one replica. The [tier you choose](search-sku-tier.md) determines partition size and speed, and each tier is optimized around a set of characteristics that fit various scenarios. If you choose a higher-end tier, you might [need fewer partitions](search-performance-tips.md#service-capacity) than if you go with S1. One of the questions you'll need to answer through self-directed testing is whether a larger and more expensive partition yields better performance than two cheaper partitions on a service provisioned at a lower tier.
+Initially, a service is allocated a minimal level of resources consisting of one partition and one replica. The [tier you choose](search-sku-tier.md) determines partition size and speed, and each tier is optimized around a set of characteristics that fit various scenarios. If you choose a higher-end tier, you might [need fewer partitions](search-performance-tips.md#service-capacity) than if you go with S1. One of the questions you need to answer through self-directed testing is whether a larger and more expensive partition yields better performance than two cheaper partitions on a service provisioned at a lower tier.
 
-A single service must have sufficient resources to handle all workloads (indexing and queries). Neither workload runs in the background. You can schedule indexing for times when query requests are naturally less frequent, but the service won't otherwise prioritize one task over another. Additionally, a certain amount of redundancy smooths out query performance when services or nodes are updated internally.
+A single service must have sufficient resources to handle all workloads (indexing and queries). Neither workload runs in the background. You can schedule indexing for times when query requests are naturally less frequent, but the service doesn't otherwise prioritize one task over another. Additionally, a certain amount of redundancy smooths out query performance when services or nodes are updated internally.
 
-Some guidelines for determining whether to add capacity include:
+Guidelines for determining whether to add capacity include:
 
-+ Meeting the high availability criteria for service level agreement
-+ The frequency of HTTP 503 errors is increasing
-+ Large query volumes are expected
++ Meeting the high availability criteria for service-level agreement.
++ The frequency of HTTP 503 errors is increasing.
++ Large query volumes are expected.
++ A [one-time upgrade](#how-to-upgrade-capacity) to newer infrastructure and larger partitions isn’t sufficient.
++ The current number of partitions isn’t adequate for indexing workloads.
 
-As a general rule, search applications tend to need more replicas than partitions, particularly when the service operations are biased toward query workloads. Each replica is a copy of your index, allowing the service to load balance requests against multiple copies. All load balancing and replication of an index is managed by Azure AI Search and you can alter the number of replicas allocated for your service at any time. You can allocate up to 12 replicas in a Standard search service and 3 replicas in a Basic search service. Replica allocation can be made either from the [Azure portal](search-create-service-portal.md) or one of the programmatic options.
+As a general rule, search applications tend to need more replicas than partitions, particularly when the service operations are biased toward query workloads. Each replica is a copy of your index, allowing the service to load balance requests against multiple copies. Azure AI Search manages all load balancing and replication of an index, and you can alter the number of replicas allocated for your service at any time. You can allocate up to 12 replicas in a Standard search service and 3 replicas in a Basic search service. Replica allocation can be made either from the [Azure portal](search-create-service-portal.md) or one of the programmatic options.
 
 Extra partitions are helpful for intensive indexing workloads. Extra partitions spread read/write operations across a larger number of compute resources.
 
-Finally, larger indexes take longer to query. As such, you might find that every incremental increase in partitions requires a smaller but proportional increase in replicas. The complexity of your queries and query volume will factor into how quickly query execution is turned around.
+Finally, larger indexes take longer to query. As such, you might find that every incremental increase in partitions requires a smaller but proportional increase in replicas. The complexity of your queries and query volume factors into how quickly query execution is turned around.
 
 > [!NOTE]
-> Adding more replicas or partitions increases the cost of running the service, and can introduce slight variations in how results are ordered. Be sure to check the [pricing calculator](https://azure.microsoft.com/pricing/calculator/) to understand the billing implications of adding more nodes. The [chart below](#chart) can help you cross-reference the number of search units required for a specific configuration. For more information on how additional replicas impact query processing, see [Ordering results](search-pagination-page-layout.md#ordering-results).
+> Adding more replicas or partitions increases the cost of running the service, and can introduce slight variations in how results are ordered. Be sure to check the [pricing calculator](https://azure.microsoft.com/pricing/calculator/) to understand the billing implications of adding more nodes. The [chart below](#chart) can help you cross-reference the number of search units required for a specific configuration. For more information on how extra replicas affect query processing, see [Ordering results](search-pagination-page-layout.md#ordering-results).
 
 <a name="adjust-capacity"></a>
 
+## How to upgrade capacity
+
+Some Azure AI Search capabilities are only available to new services. One such capability is higher storage capacity, which applies to [services created after April 2024](search-limits-quotas-capacity.md#service-limits). However, if you created your service before April 2024, you can get higher capacity without recreating your service by performing a one-time upgrade. For more information, see [Upgrade your search service](search-how-to-upgrade.md).
+
 ## How to change capacity
 
-To increase or decrease the capacity of your search service, add or remove partitions and replicas.
+To increase or decrease the capacity of your service, you have two options:
+
++ [Add or remove partitions and replicas](#add-or-remove-partitions-and-replicas)
++ [Change your pricing tier](#change-your-pricing-tier)
 
-1. Sign in to the [Azure portal](https://portal.azure.com/) and select the search service.
+### Add or remove partitions and replicas
 
-1. Under **Settings**, open the **Scale** page to modify replicas and partitions. 
+1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
+
+1. From the left pane, select **Settings** > **Scale**.
 
    The following screenshot shows a Standard service provisioned with one replica and partition. The formula at the bottom indicates how many search units are being used (1). If the unit price was $100 (not a real price), the monthly cost of running this service would be $100 on average.
 
-   :::image type="content" source="media/search-capacity-planning/1-initial-values.png" alt-text="Scale page showing current values" border="true":::
+   :::image type="content" source="media/search-capacity-planning/initial-values.png" alt-text="Screenshot of the Scale page showing the current replica and partition values." border="true":::
 
 1. Use the slider to increase or decrease the number of partitions. Select **Save**.
 
    This example adds a second replica and partition. Notice the search unit count; it's now four because the billing formula is replicas multiplied by partitions (2 x 2). Doubling capacity more than doubles the cost of running the service. If the search unit cost was $100, the new monthly bill would now be $400.
 
-   For the current per unit costs of each tier, visit the [Pricing page](https://azure.microsoft.com/pricing/details/search/).
+   For the current per unit costs of each tier, visit the [pricing page](https://azure.microsoft.com/pricing/details/search/).
+
+   :::image type="content" source="media/search-capacity-planning/add-two-each.png" alt-text="Screenshot of the Scale page with added replicas and partitions." border="true":::
 
-   :::image type="content" source="media/search-capacity-planning/2-add-2-each.png" alt-text="Add replicas and partitions" border="true":::
+1. Check your notifications to confirm that the operation started.
 
-1. After saving, you can check notifications to confirm the action succeeded.
+   :::image type="content" source="media/search-capacity-planning/portal-notifications.png" alt-text="Screenshot of the notification of the scaling operation in the Azure portal." border="true":::
 
-   :::image type="content" source="media/search-capacity-planning/3-save-confirm.png" alt-text="Save changes" border="true":::
+   This operation can take several hours to complete. You can’t cancel the process after it starts, and there’s no real-time monitoring of replica and partition adjustments. However, the following message displays while changes are underway.
 
-   Changes in capacity can take anywhere from 15 minutes up to several hours to complete. You can't cancel once the process has started and there's no real-time monitoring for replica and partition adjustments. However, the following message remains visible while changes are underway.
+   :::image type="content" source="media/search-capacity-planning/updating-message.png" alt-text="Screenshot of the Updating message in the Azure portal." border="true":::
 
-   :::image type="content" source="media/search-capacity-planning/4-updating.png" alt-text="Status message in the Azure portal" border="true":::
+### Change your pricing tier
 
 > [!NOTE]
-> After a service is provisioned, it cannot be upgraded to a higher tier. You must create a search service at the new tier and reload your indexes. See [Create an Azure AI Search service in the Azure portal](search-create-service-portal.md) for help with service provisioning.
+> The 2025-02-01-preview supports changes between Basic and Standard (S1, S2, and S3) tiers. Currently, you can only switch from a lower tier to a higher tier, such as going from Basic to S1. Your region also can't have [capacity constraints on the higher tier](search-region-support.md).
+
+Your [pricing tier](search-sku-tier.md) determines the maximum storage of your search service. If you need more <!-- or less capacity -->capacity, you can switch to a different pricing tier that accommodates your storage needs.
+
+In addition to capacity, changing your pricing tier affects the workload and maximum limits of your service. Before you proceed, compare the [service limits](search-limits-quotas-capacity.md) of your current tier and your desired tier. These include limits on:
+
++ Partition storage
++ Indexes
++ Vectors
++ Indexers
++ Shared private link resources
++ Synonyms
++ Index aliases
++ Semantic ranker throttling
+
+Generally, switching to a higher tier increases your [storage limit](search-limits-quotas-capacity.md#service-limits) and [vector limit](search-limits-quotas-capacity.md#vector-index-size-limits), increases request throughput, and decreases latency<!-- , while switching to a lower tier decreases your storage limit and vector limit, decreases request throughput, and increases latency -->.
+
+To change your pricing tier:
+
+1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
+
+1. From the left pane, select **Settings** > **Scale**.
+
+1. Under your current tier, select **Change Pricing Tier**.
+
+   :::image type="content" source="media/search-capacity-planning/change-pricing-tier.png" alt-text="Screenshot of the Change Pricing Tier button in the Azure portal." border="true":::
+
+1. On the **Select Pricing Tier** page, choose a higher tier from the list. Currently, you can only move up between Basic, S1, S2, and S3. Other pricing tiers are unavailable and appear dimmed.
+
+1. To switch to the higher tier, select **Select**.
+
+   :::image type="content" source="media/search-capacity-planning/pricing-tier-list.png" alt-text="Screenshot of the Select Pricing Tier page and the list of higher tiers in the Azure portal." border="true":::
+
+   This operation can take several hours to complete. You can’t cancel the process after it starts, and there’s no real-time monitoring of tier changes. However, on the **Overview** page, a **Provisioning** status indicates the operation is underway for your service.
+
+   :::image type="content" source="media/search-capacity-planning/provisioning-status.png" alt-text="Screenshot of the service Overview page with a Provisioning status." border="true":::
 
 ## How scale requests are handled
 
@@ -143,25 +191,25 @@ The following chart applies to Standard tier and higher. It shows all possible c
 
 Basic search services have lower search unit counts.
 
-+ On search services created before April 3, 2024, a basic search service can have exactly one partition and up to three replicas, for a maximum limit of three SUs. The only adjustable resource is replicas. 
++ On search services created before April 3, 2024, Basic services can have exactly one partition and up to three replicas for a maximum limit of three SUs. The only adjustable resource is replicas. However, you might be able to increase your partition count by [upgrading your service](search-how-to-upgrade.md).
 
-+ On search services created after April 3, 2024 in [supported regions](search-limits-quotas-capacity.md#service-limits), basic services can have up to three partitions and three replicas. The maximum SU limit is nine to support a full complement of partitions and replicas.
++ On search services created after April 3, 2024 in [supported regions](search-limits-quotas-capacity.md#service-limits), Basic services can have up to three partitions and three replicas. The maximum SU limit is nine to support a full complement of partitions and replicas.
 
 For search services on any billable tier, regardless of creation date, you need a minimum of two replicas for high availability on queries.
 
 For billing rates per tier and currency, see the [Azure AI Search pricing page](https://azure.microsoft.com/pricing/details/search/).
 
 ## Estimate capacity using a billable tier
 
-Storage needs are determined by the size of the indexes you expect to build. There are no solid heuristics or generalities that help with estimates. The only way to determine the size of an index is [build one](search-what-is-an-index.md). Its size is based on tokenization and embeddings, and whether you enable suggesters, filtering, and sorting, or can take advantage of [vector compression](vector-search-how-to-quantization.md).
+The size of the indexes you expect to build determines storage needs. There are no solid heuristics or generalities that help with estimates. The only way to determine the size of an index is [build one](search-what-is-an-index.md). Its size is based on tokenization and embeddings, and whether you enable suggesters, filtering, and sorting, or can take advantage of [vector compression](vector-search-how-to-quantization.md).
 
 We recommend estimating on a billable tier, Basic or above. The Free tier runs on physical resources shared by multiple customers and is subject to factors beyond your control. Only the dedicated resources of a billable search service can accommodate larger sampling and processing times for more realistic estimates of index quantity, size, and query volumes during development. 
 
 1. [Review service limits at each tier](search-limits-quotas-capacity.md#service-limits) to determine whether lower tiers can support the number of indexes you need. Consider whether you need multiple copies of an index for active development, testing, and production. 
 
    A search service is subject to object limits (maximum number of indexes, indexers, skillsets, etc.) and storage limits. Whichever limit is reached first is the effective limit. 
 
-1. [Create a service at a billable tier](search-create-service-portal.md). Tiers are optimized for certain workloads. For example, Storage Optimized tier has a limit of 10 indexes because it's designed to support a low number of very large indexes.
+1. [Create a service at a billable tier](search-create-service-portal.md). Tiers are optimized for certain workloads. For example, the Storage Optimized tier has a limit of 10 indexes because it's designed to support a low number of large indexes.
 
     + Start low, at Basic or S1, if you're not sure about the projected load.
 
@@ -187,11 +235,11 @@ Storage requirements can be inflated if you include data that will never be sear
 
 ## Service-level agreement considerations
 
-The Free tier and preview features aren't covered by [service-level agreements (SLAs)](https://azure.microsoft.com/support/legal/sla/search/v1_0/). For all billable tiers, SLAs take effect when you provision sufficient redundancy for your service. 
+The Free tier and preview features aren't covered by [service-level agreements (SLAs)](https://azure.microsoft.com/support/legal/sla/search/v1_0/). For all billable tiers, SLAs take effect when you provision sufficient redundancy for your service.
 
-+ Two or more replicas satisfy query (read) SLAs. 
++ Two or more replicas satisfy query (read) SLAs.
 
-+ Three or more replicas satisfy query and indexing (read-write) SLAs. 
++ Three or more replicas satisfy query and indexing (read-write) SLAs.
 
 The number of partitions doesn't affect SLAs.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索キャパシティ計画文書の更新"
}
```

### Explanation
この変更は、`articles/search/search-capacity-planning.md`ファイルの更新を示しており、主に日付の変更とキャパシティに関する内容の追加や修正が行われています。文書の日付が「2025年3月11日」から「2025年3月31日」に変更され、サービスの価格レベルに関する情報が改善されました。

更新内容には、サービスのキャパシティを表現する概念として「検索ユニット」、「レプリカ」、「パーティション」に関する説明の強化が含まれます。また、キャパシティの拡張や価格テーブルの変更手順が詳細に述べられ、特に「高いストレージ制限への一回限りのアップグレード」についての情報が新たに追加されています。

さらに、サービスのスケーリングに関するセクションでは、追加または削除したレプリカやパーティションを通じてキャパシティを調整する方法が明確に説明され、価格帯変更の手順も詳細に解説されています。これにより、ユーザーは実際の使用シナリオに基づいて最適なキャパシティ計画を立てやすくなるとともに、サービスの運用コストを把握しやすくなっています。全体として、この更新はAzure AI Searchサービスの効率的な運用を支援するための重要な情報を提供しています。

## articles/search/search-create-service-portal.md{#item-f90159}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - build-2024
 ms.topic: how-to
-ms.date: 02/20/2025
+ms.date: 03/21/2025
 ---
 
 # Create an Azure AI Search service in the Azure portal
@@ -33,13 +33,13 @@ You can also use:
 
 ## Before you start
 
-Some properties are fixed for the lifetime of the search service. Before creating your service, decide on the following properties:
+Some properties are fixed for the lifetime of the search service. Before you create your service, decide on the following properties:
 
 | Property | Description |
 |--|--|
 | [Name](#name-your-service) | Becomes part of the URL endpoint. The name must be unique and follow naming rules. |
 | [Region](search-region-support.md) | Determines data residency and availability of certain features. For example, semantic ranker and Azure AI integration have region requirements. Choose a region that supports the features you need. |
-| [Tier](search-sku-tier.md) | Determines infrastructure, service limits, and billing. Some features aren't available on lower or specialized tiers. |
+| [Tier](search-sku-tier.md) | Determines infrastructure, service limits, and billing. Some features aren't available on lower or specialized tiers. In the 2025-02-01-preview, you can also [switch from a lower tier to a higher tier](search-capacity-planning.md#change-your-pricing-tier). |
 
 ## Subscribe to Azure
 
@@ -131,7 +131,7 @@ Currently, the following regions offer cross-regional availability for Azure AI
 + Americas: West US, East US
 + Europe: Switzerland North, Sweden Central
 
-This list isn't definitive, and depending on your tier, you might have more choices. Region status can also change quickly, so confirm your region choice before creating your search service.
+This list isn't definitive, and depending on your tier, you might have more choices. Region status can also change quickly, so confirm your region choice before you create your search service.
 
 ## Choose a tier
 
@@ -149,8 +149,8 @@ The Basic and Standard tiers are the most common for production workloads, but m
 :::image type="content" source="media/search-create-service-portal/select-pricing-tier.png" lightbox="media/search-create-service-portal/select-pricing-tier.png" alt-text="Screenshot of the Select Pricing Tier page in the Azure portal." border="true":::
 
 > [!NOTE]
-> + You can't change the tier after creating your search service, so choose carefully.
-> + Search services created after April 3, 2024 have larger partitions and higher vector quotas at every billable tier.
+> + After you create your service, you can move up between Basic and Standard (S1, S2, and S3) tiers. Switching to a lower tier isn't currently supported. For more information, see [Change your pricing tier](search-capacity-planning.md#change-your-pricing-tier).
+> + Services created after April 3, 2024 have larger partitions and higher vector quotas at every billable tier.
 
 ## Create your service
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI 検索サービス作成ガイドの更新"
}
```

### Explanation
この変更は、`articles/search/search-create-service-portal.md`ファイルに対する更新を示しており、特に日付の修正及びいくつかの文言の修正が行われています。文書の日付が「2025年2月20日」から「2025年3月21日」に変更され、検索サービスを作成する際に考慮すべきプロパティに関する説明が明確化されました。

具体的には、サービスのティアに関する情報が拡張され、2025-02-01-previewバージョンでのティアの変更についての情報が追加されました。新しい表現により、ユーザーは検索サービスの作成時に選択肢を明確に理解できるようになっています。また、地域の選択に関するセクションも更新され、サービス作成前に地域を確認する重要性が強調されています。

この調整により、ユーザーはAzureポータル内でのサービス作成手順をより理解しやすくなり、適切な設定に基づいて効率よくサービスを立ち上げることが可能になります。全体的に、これらの更新は文書の精度と有用性を向上させるものであり、利用者が必要な情報をスムーズに取得できるようにしています。

## articles/search/search-faceted-navigation-examples.md{#item-2b1158}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,721 @@
+---
+
+title: Faceted navigation examples
+titleSuffix: Azure AI Search
+description: Examples that demonstrate query syntax for facet hierarchies, distinct counts, facet aggregations, and facet filters.
+
+manager: nitinme
+author: HeidiSteen
+ms.author: heidist
+ms.service: azure-ai-search
+ms.topic: how-to
+ms.date: 04/04/2025
+---
+
+# Faceted navigation examples
+
+This section extends [faceted navigation configuration](search-faceted-navigation.md) with examples that demonstrate basic usage and other scenarios.
+
+Facetable fields are defined in an index, but facet parameters and expressions are defined in query requests. If you have an index with facetable fields, you can try new preview features like [facet hierarchies](#facet-hierarchy-example), [facet aggregations](#facet-aggregation-example), and [facet filters](#facet-filtering-example) on existing indexes.
+
+## Facet parameters and syntax
+
+Depending on the API, a facet query is usually an array of facet expressions that are applied to search results. Each facet expression contains a facetable field name, optionally followed by a comma-separated list of name-value pairs.
+
++ *facet query* is a query request that includes a facet property.
++ *facetable field* is a field definition in the search index attributed with the `facetable` property.
++ *count* is the number of matches for each facet found in the search results.
+
+The following table describes facet parameters used in the examples.
+
+| Facet parameter | Description | Usage | Example |
+|-----------------|-------------|-------|---------|
+| `count` | Maximum number of facet terms per structure.| Integer. Default is 10. There's no upper limit, but higher values degrade performance, especially if the faceted field contains a large number of unique terms. This is due to the way facet queries are distributed across shards. You can set `count` to zero or to a value that's greater than or equal to the number of unique values in the facetable field to get an accurate count across all shards. The tradeoff is increased latency. | `Tags,count:5` limits the faceted navigation response to 5 facet buckets that containing the most facet counts, but they can be in any order. |
+| `sort` | Determines order of facet buckets. | Valid values are `count`, `-count`, `value`, `-value`. Use `count` to list facets from greatest to smallest. Use `-count` to sort in ascending order (smallest to greatest). Use `value` to sort alphanumerically by facet value in ascending order. Use `-value` to sort descending by value. | `"facet=Category,count:3,sort:count"` gets the top three facet buckets in search results, listed in descending order by the number of matches in each Category. If the top three categories are Budget, Extended-Stay, and Luxury, and Budget has 5 hits, Extended-Stay has 6, and Luxury has 4, then the facet buckets are ordered as Extended-Stay, Budget, Luxury. Another example is`"facet=Rating,sort:-value"`. It produces facets for all possible ratings, in descending order by value. If ratings are from 1 to 5, the facets are ordered 5, 4, 3, 2, 1, irrespective of how many documents match each rating. |
+| `values` | Provides values for facet labels. | Set to pipe-delimited numeric or `Edm.DateTimeOffset` values specifying a dynamic set of facet entry values. The values must be listed in sequential, ascending order to get the expected results. | `"facet=baseRate,values:10 | 20"` produces three facet buckets: one for base rate 0 up to but not including 10, one for 10 up to but not including 20, and one for 20 and higher. A string `"facet=lastRenovationDate,values:2024-02-01T00:00:00Z"` produces two facet buckets: one for hotels renovated before February 2024, and one for hotels renovated February 1, 2024 or later. |
+| `interval` | Provides an interval sequence for facets that can be grouped into intervals. | An integer interval greater than zero for numbers, or minute, hour, day, week, month, quarter, year for date time values. | `"facet=baseRate,interval:100"` produces facet buckets based on base rate ranges of size 100. If base rates are all between $60 and $600, there are facet buckets for 0-100, 100-200, 200-300, 300-400, 400-500, and 500-600. The string `"facet=lastRenovationDate,interval:year"` produces one facet bucket for each year a hotel was renovated. |
+| `timeoffset` | Specifies the UTC time offset to account for in setting time boundaries. | Set to (`[+-]hh:mm, [+-]hhmm, or [+-]hh`). If used, the `timeoffset` parameter must be combined with the interval option, and only when applied to a field of type `Edm.DateTimeOffset`. | `"facet=lastRenovationDate,interval:day,timeoffset:-01:00"` uses the day boundary that starts at 01:00:00 UTC (midnight in the target time zone). |
+
+`count` and `sort` can be combined in the same facet specification, but they can't be combined with `interval` or `values`.
+
+`interval` and `values` can't be combined together.
+
+Interval facets on date time are computed based on the UTC time if `timeoffset` isn't specified. For example, for `"facet=lastRenovationDate,interval:day"`, the day boundary starts at 00:00:00 UTC.
+
+## Basic facet example
+
+The following facet queries work against the [hotels sample index](search-get-started-portal.md). You can use **JSON view** in Search Explorer to paste in the JSON query. For help with getting started, see [Add faceted navigation to search results](search-faceted-navigation.md).
+
+This first query retrieves facets for Categories, Ratings, Tags, and rooms with baseRate values in specific ranges. Notice the last facet is on a subfield of the Rooms collection. Facets count the parent document (Hotels) and not intermediate subdocuments (Rooms), so the response determines the number of *hotels* that have any rooms in each pricing category.
+
+```rest
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-03-01-Preview
+{  
+  "search": "ocean view",  
+  "facets": [ "Category", "Rating", "Tags", "Rooms/BaseRate,values:80|150|220" ],
+  "count": true 
+}  
+```
+
+This second example uses a filter to narrow down the previous faceted query result after the user selects Rating 3 and category "Motel".
+
+```rest
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-03-01-Preview
+{  
+  "search": "water view",  
+  "facets": [ "Tags", "Rooms/BaseRate,values:80|150|220" ],
+  "filter": "Rating eq 3 and Category eq 'Motel'",
+  "count": true  
+} 
+```
+
+The third example sets an upper limit on unique terms returned in a query. The default is 10, but you can increase or decrease this value using the count parameter on the facet attribute. This example returns facets for city, limited to 5.
+
+```rest
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-03-01-Preview
+{  
+  "search": "view",  
+  "facets": [ "Address/City,count:5" ],
+  "count": true
+} 
+```
+
+This example shows three facets for "Category", "Tags", and "Rating", with a count override on "Tags" and a range override for "Rating", which is otherwise stored as a double in the index.
+
+```http
+POST https://{{service_name}}.search.windows.net/indexes/hotels/docs/search?api-version={{api_version}}
+{
+    "search": "*",
+    "facets": [ 
+        "Category", 
+        "Tags,count:5", 
+        "Rating,values:1|2|3|4|5"
+    ],
+    "count": true
+}
+```
+
+For each faceted navigation tree, there's a default limit of the top 10 facet instances found by the query. This default makes sense for navigation structures because it keeps the values list to a manageable size. You can override the default by assigning a value to "count". For example, `"Tags,count:5"` reduces the number of tags under the Tags section to the top five.
+
+For Numeric and DateTime values only, you can explicitly set values on the facet field (for example, `facet=Rating,values:1|2|3|4|5`) to separate results into contiguous ranges (either ranges based on numeric values or time periods). Alternatively, you can add "interval", as in `facet=Rating,interval:1`. 
+
+Each range is built using 0 as a starting point, a value from the list as an endpoint, and then trimmed of the previous range to create discrete intervals.
+
+## Distinct values example
+
+You can formulate a query that returns a distinct value count for each facetable field. This example formulates an empty or unqualified query (`"search": "*"`) that matches on all documents, but by setting `top` to zero, you get just the counts, with no results.
+
+For brevity, this query includes just two fields marked as `facetable` in the hotels sample index.
+
+```http
+POST https://{{service_name}}.search.windows.net/indexes/hotels/docs/search?api-version={{api_version}}
+{
+    "search": "*",
+    "count": true,
+    "top": 0,
+    "facets": [ 
+        "Category", "Address/StateProvince""
+    ]
+}
+```
+
+Results from this query are as follows:
+
+```json
+{
+  "@odata.count": 50,
+  "@search.facets": {
+    "Address/StateProvince": [
+      {
+        "count": 9,
+        "value": "WA"
+      },
+      {
+        "count": 6,
+        "value": "CA "
+      },
+      {
+        "count": 4,
+        "value": "FL"
+      },
+      {
+        "count": 3,
+        "value": "NY"
+      },
+      {
+        "count": 3,
+        "value": "OR"
+      },
+      {
+        "count": 3,
+        "value": "TX"
+      },
+      {
+        "count": 2,
+        "value": "GA"
+      },
+      {
+        "count": 2,
+        "value": "MA"
+      },
+      {
+        "count": 2,
+        "value": "TN"
+      },
+      {
+        "count": 1,
+        "value": "AZ"
+      }
+    ],
+    "Category": [
+      {
+        "count": 13,
+        "value": "Budget"
+      },
+      {
+        "count": 12,
+        "value": "Suite"
+      },
+      {
+        "count": 7,
+        "value": "Boutique"
+      },
+      {
+        "count": 7,
+        "value": "Resort and Spa"
+      },
+      {
+        "count": 6,
+        "value": "Extended-Stay"
+      },
+      {
+        "count": 5,
+        "value": "Luxury"
+      }
+    ]
+  },
+  "value": []
+}
+```
+
+## Facet hierarchy example
+
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+Starting in [2025-03-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-03-01-preview&preserve-view=true) and available in the Azure portal, you can configure a facet hierarchy using the `>` and `;` operators.
+
+The nesting (hierarchical) operator `>` denotes a parent–child relationship, and the semicolon operator `;` denotes multiple fields at the same nesting level, which are all children of the same parent. The parent must contain only one field. Both the parent and child fields must be `facetable`. 
+
+The order of operations in a facet expression that includes facet hierarchies are:
+
+* options operator (comma `,`) that separates facet parameters for the facet field, such as the comma in `Rooms/BaseRate,values`
+* parentheses, such as the ones enclosing `(Rooms/BaseRate,values:50 ; Rooms/Type)`.
+* nesting operator (angled bracket `>`)
+* append operator (semicolon `;`), demonstrated in a second example `"Tags>(Rooms/BaseRate,values:50 ; Rooms/Type)"` in this section, where two child facets are peers under the Tags parent.
+
+There are several examples for facet hierarchies. The first example is a query that returns just a few documents, which is helpful for viewing a full response. Facets count the parent document (Hotels) and not intermediate subdocuments (Rooms), so the response determines the number of *hotels* that have any rooms in each facet bucket.
+
+```rest
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-03-01-Preview
+{
+  "search": "ocean",  
+  "facets": ["Address/StateProvince>Address/City", "Tags>Rooms/BaseRate,values:50"],
+  "select": "HotelName, Description, Tags, Address/StateProvince, Address/City",
+  "count": true 
+}
+```
+
+Results from this query are as follows. Both hotels have pools. For other tags, only one hotel provides the amenity.
+
+```json
+{
+  "@odata.count": 2,
+  "@search.facets": {
+    "Tags": [
+      {
+        "value": "pool",
+        "count": 2,
+        "@search.facets": {
+          "Rooms/BaseRate": [
+            {
+              "to": 50,
+              "count": 0
+            },
+            {
+              "from": 50,
+              "count": 2
+            }
+          ]
+        }
+      },
+      {
+        "value": "air conditioning",
+        "count": 1,
+        "@search.facets": {
+          "Rooms/BaseRate": [
+            {
+              "to": 50,
+              "count": 0
+            },
+            {
+              "from": 50,
+              "count": 1
+            }
+          ]
+        }
+      },
+      {
+        "value": "bar",
+        "count": 1,
+        "@search.facets": {
+          "Rooms/BaseRate": [
+            {
+              "to": 50,
+              "count": 0
+            },
+            {
+              "from": 50,
+              "count": 1
+            }
+          ]
+        }
+      },
+      {
+        "value": "restaurant",
+        "count": 1,
+        "@search.facets": {
+          "Rooms/BaseRate": [
+            {
+              "to": 50,
+              "count": 0
+            },
+            {
+              "from": 50,
+              "count": 1
+            }
+          ]
+        }
+      },
+      {
+        "value": "view",
+        "count": 1,
+        "@search.facets": {
+          "Rooms/BaseRate": [
+            {
+              "to": 50,
+              "count": 0
+            },
+            {
+              "from": 50,
+              "count": 1
+            }
+          ]
+        }
+      }
+    ],
+    "Address/StateProvince": [
+      {
+        "value": "FL",
+        "count": 1,
+        "@search.facets": {
+          "Address/City": [
+            {
+              "value": "Tampa",
+              "count": 1
+            }
+          ]
+        }
+      },
+      {
+        "value": "HI",
+        "count": 1,
+        "@search.facets": {
+          "Address/City": [
+            {
+              "value": "Honolulu",
+              "count": 1
+            }
+          ]
+        }
+      }
+    ]
+  },
+  "value": [
+    {
+      "@search.score": 1.6076145,
+      "HotelName": "Ocean Water Resort & Spa",
+      "Description": "New Luxury Hotel for the vacation of a lifetime. Bay views from every room, location near the pier, rooftop pool, waterfront dining & more.",
+      "Tags": [
+        "view",
+        "pool",
+        "restaurant"
+      ],
+      "Address": {
+        "City": "Tampa",
+        "StateProvince": "FL"
+      }
+    },
+    {
+      "@search.score": 1.0594962,
+      "HotelName": "Windy Ocean Motel",
+      "Description": "Oceanfront hotel overlooking the beach features rooms with a private balcony and 2 indoor and outdoor pools. Inspired by the natural beauty of the island, each room includes an original painting of local scenes by the owner. Rooms include a mini fridge, Keurig coffee maker, and flatscreen TV. Various shops and art entertainment are on the boardwalk, just steps away.",
+      "Tags": [
+        "pool",
+        "air conditioning",
+        "bar"
+      ],
+      "Address": {
+        "City": "Honolulu",
+        "StateProvince": "HI"
+      }
+    }
+  ]
+}
+```
+
+This second example extends the previous one, demonstrating multiple top-level facets with multiple children. Notice the semicolon (`;`) operator separates each child.
+
+```rest
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-03-01-Preview
+{  
+  "search": "+ocean",  
+  "facets": ["Address/StateProvince > Address/City", "Tags > (Rooms/BaseRate,values:50 ; Rooms/Type)"],
+  "select": "HotelName, Description, Tags, Address/StateProvince, Address/City",
+  "count": true 
+}  
+```
+
+A partial response, trimmed for brevity, shows Tags with child facets for the rooms base rate and type. In the hotels sample index, both hotels that match to `+ocean` have rooms in each type and a pool.
+
+```json
+{
+  "@odata.count": 2,
+  "@search.facets": {
+    "Tags": [
+      {
+        "value": "pool",
+        "count": 2,
+        "@search.facets": {
+          "Rooms/BaseRate": [
+            {
+              "to": 50,
+              "count": 0
+            },
+            {
+              "from": 50,
+              "count": 2
+            }
+          ],
+          "Rooms/Type": [
+            {
+              "value": "Budget Room",
+              "count": 2
+            },
+            {
+              "value": "Deluxe Room",
+              "count": 2
+            },
+            {
+              "value": "Standard Room",
+              "count": 2
+            },
+            {
+              "value": "Suite",
+              "count": 2
+            }
+          ]
+        }}]},
+  ...
+}
+```
+
+This last example shows precedence rules for parentheses that affects nesting levels. Suppose you want to return a facet hierarchy in this order.
+
+```
+Address/StateProvince
+  Address/City
+    Category
+    Rating
+```
+
+To return this hierarchy, create a query where Category and Rating are siblings under Address/City.
+
+```json
+  { 
+    "search": "beach",  
+    "facets": [
+        "Address/StateProvince > (Address/City > (Category ; Rating))"
+        ],
+    "select": "HotelName, Description, Tags, Address/StateProvince, Address/City",
+    "count": true 
+  }
+```
+
+If you remove the innermost parentheses, Category and Rating are no longer siblings because the precedence rules mean that the `>` operator is evaluated before `;`.
+
+```json
+  { 
+    "search": "beach",  
+    "facets": [
+        "Address/StateProvince > (Address/City > Category ; Rating)"
+        ],
+    "select": "HotelName, Description, Tags, Address/StateProvince, Address/City",
+    "count": true 
+  }
+```
+
+The top-level parent is still Address/StateProvince, but now Address/City and Rating are on same level.
+
+```
+Address/StateProvince
+  Rating
+  Address/City
+    Category
+```
+
+## Facet filtering example
+
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+Starting in [2025-03-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-03-01-preview&preserve-view=true) and available in the Azure portal, you can configure facet filters.
+
+Facet filtering enables you to constrain the facet values returned to those matching a specified regular expression. Two new parameters accept a regular expression that is applied to the facet field:
+
+* `includeTermFilter` filters the facet values to those that match the regular expression
+* `excludeTermFilter` filters the facet values to those that don't match the regular expression 
+
+If a facet string satisfies both conditions, the `excludeTermFilter` takes precedence because the set of bucket strings is first evaluated with `includeTermFilter` and then excluded with `excludeTermFilter`.
+
+Only those facet values that match the regular expression are returned. You can combine these parameters with other facet options (for example, `count`, `sort`, and [hierarchical faceting](#facet-hierarchy-example)) on string fields.
+
+Because the regular expression is nested within a JSON string value, you must escape both the double quote (`"`) and the backslash (`\`) characters. The regular expression itself is delimited by the forward slash (`/`). For more information about escape patterns, see [Regular expression search](query-lucene-syntax.md#bkmk_regex).
+
+The following example shows how to escape special characters in your regular expression such as backslash, double quotes, or regular expression syntax characters. 
+
+```json
+{
+    "search": "*", 
+    "facets": ["name,includeTermFilter:/EscapeBackslash\\\OrDoubleQuote\\"OrRegexCharacter\\(/"] 
+}
+```
+
+Here's an example of a facet filter that matches on Budget and Extended-Stay hotels, with Rating as a child of each hotel category.
+
+```http
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-03-01-Preview
+{ 
+    "search": "*", 
+    "facets": ["(Category,includeTermFilter:/(Budget|Extended-Stay)/)>Rating,values:1|2|3|4|5"],
+    "select": "HotelName, Category, Rating",
+    "count": true 
+} 
+```
+
+The following example is an abbreviated response (hotel documents are omitted for brevity).
+
+```json
+{
+  "@odata.count": 50,
+  "@search.facets": {
+    "Category": [
+      {
+        "value": "Budget",
+        "count": 13,
+        "@search.facets": {
+          "Rating": [
+            {
+              "to": 1,
+              "count": 0
+            },
+            {
+              "from": 1,
+              "to": 2,
+              "count": 0
+            },
+            {
+              "from": 2,
+              "to": 3,
+              "count": 4
+            },
+            {
+              "from": 3,
+              "to": 4,
+              "count": 5
+            },
+            {
+              "from": 4,
+              "to": 5,
+              "count": 4
+            },
+            {
+              "from": 5,
+              "count": 0
+            }
+          ]
+        }
+      },
+      {
+        "value": "Extended-Stay",
+        "count": 6,
+        "@search.facets": {
+          "Rating": [
+            {
+              "to": 1,
+              "count": 0
+            },
+            {
+              "from": 1,
+              "to": 2,
+              "count": 0
+            },
+            {
+              "from": 2,
+              "to": 3,
+              "count": 4
+            },
+            {
+              "from": 3,
+              "to": 4,
+              "count": 1
+            },
+            {
+              "from": 4,
+              "to": 5,
+              "count": 1
+            },
+            {
+              "from": 5,
+              "count": 0
+            }
+          ]
+        }
+      }
+    ]
+  }, 
+  "value": [  ALL 50 HOTELS APPEAR HERE ]
+}
+```
+
+## Facet aggregation example
+
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+Starting in [2025-03-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-03-01-preview&preserve-view=true) and available in the Azure portal, you can aggregate facets.
+
+Facet aggregations allow you to compute metrics from facet values. The aggregation capability works alongside the existing faceting options. The only supported metric is `sum`. Adding `metric: sum` to a numeric facet aggregates all the values of each bucket. 
+
+You can add a default value to use if a document contains a null for that field: `"facets": [ "Rooms/SleepsCount, metric: sum, default:2"]`. If a room has a null value for the Rooms/SleepsCount field, the default substitutes for the missing value.
+
+You can sum any facetable field of a numeric data type (except vectors and geographic coordinates). 
+
+Here's an example using the hotels-sample-index. The Rooms/SleepsCount field is facetable and numeric, so we choose this field to demonstrate sum. If we sum that field, we get the sleep count for the entire hotel. Recall that facets count the parent document (Hotels) and not intermediate subdocuments (Rooms), so the response sums the SleepsCount of all rooms for the entire hotel. In this query, we add a filter to sum the SleepsCount for just one hotel.
+
+```rest
+POST /indexes/hotels-sample-index/docs/search?api-version=2025-03-01-Preview
+
+{ 
+      "search": "*",
+      "filter": "HotelId eq '41'",
+      "facets": [ "Rooms/SleepsCount, metric: sum"],
+      "select": "HotelId, HotelName, Rooms/Type, Rooms/SleepsCount",
+      "count": true
+}
+```
+
+A response for the query might look like the following example. Windy Ocean Model can accommodate a total of 40 guests.
+
+```json
+{
+  "@odata.count": 1,
+  "@search.facets": {
+    "Rooms/SleepsCount": [
+      {
+        "sum": 40.0
+      }
+    ]
+  },
+  "value": [
+    {
+      "@search.score": 1.0,
+      "HotelId": "41",
+      "HotelName": "Windy Ocean Motel",
+      "Rooms": [
+        {
+          "Type": "Suite",
+          "SleepsCount": 4
+        },
+        {
+          "Type": "Deluxe Room",
+          "SleepsCount": 2
+        },
+        {
+          "Type": "Budget Room",
+          "SleepsCount": 2
+        },
+        {
+          "Type": "Budget Room",
+          "SleepsCount": 2
+        },
+        {
+          "Type": "Suite",
+          "SleepsCount": 2
+        },
+        {
+          "Type": "Standard Room",
+          "SleepsCount": 2
+        },
+        {
+          "Type": "Deluxe Room",
+          "SleepsCount": 2
+        },
+        {
+          "Type": "Suite",
+          "SleepsCount": 2
+        },
+        {
+          "Type": "Suite",
+          "SleepsCount": 4
+        },
+        {
+          "Type": "Standard Room",
+          "SleepsCount": 4
+        },
+        {
+          "Type": "Standard Room",
+          "SleepsCount": 2
+        },
+        {
+          "Type": "Deluxe Room",
+          "SleepsCount": 2
+        },
+        {
+          "Type": "Suite",
+          "SleepsCount": 2
+        },
+        {
+          "Type": "Standard Room",
+          "SleepsCount": 2
+        },
+        {
+          "Type": "Deluxe Room",
+          "SleepsCount": 2
+        },
+        {
+          "Type": "Deluxe Room",
+          "SleepsCount": 2
+        },
+        {
+          "Type": "Standard Room",
+          "SleepsCount": 2
+        }
+      ]
+    }
+  ]
+}
+```
+
+## Next steps
+
+Revisit [facet navigation configuration](search-faceted-navigation.md) for tools and APIs, and review [best practices](search-faceted-navigation.md#best-practices-for-working-with-facets) for working with facets in code.
+
+We recommend the [C#: Add search to web apps](tutorial-csharp-overview.md) for an example of faceted navigation that includes code for the presentation layer. The sample also includes filters, suggestions, and autocomplete. It uses JavaScript and React for the presentation layer.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファセットナビゲーションの例に関する新規文書の追加"
}
```

### Explanation
この変更は、`articles/search/search-faceted-navigation-examples.md`という新しい文書の追加を示しており、ファセットナビゲーションの構成や使用方法に関する実例が詳述されています。この文書は、Azure AI Searchによるファセットナビゲーションの拡張について、具体的なクエリ構文や使い方を示す内容となっています。

文書には、ファセットパラメータや構文に関する説明が含まれ、APIに基づいたファセットクエリがどのように構成されるかが具体的に解説されています。さらに、ファセットフィルタやファセット集約に関する新機能、そしてファセット階層の使用方法についても包括的に触れています。

たとえば、ファセットクエリの基本例や、特定の条件に基づいたフィルタリングの方法、ファセットを用いた集約機能の実装方法が示されており、開発者がこの機能を効果的に活用するためのガイドラインも提供されています。また、具体的なAPIリクエストの例が豊富に含まれており、ユーザーが即座に実装に移行できるようになっています。

この文書の追加により、ファセットナビゲーション機能の効果的な利用が促進され、より直感的な検索体験を提供することが期待されます。全体として、この新規文書は、Azure AI Searchを利用する開発者や技術者にとって貴重なリソースとなるでしょう。

## articles/search/search-faceted-navigation.md{#item-f29d1e}

<details>
<summary>Diff</summary>
````diff
@@ -1,37 +1,45 @@
 ---
-title: Add a faceted navigation category hierarchy
+title: Add facets to a query
 titleSuffix: Azure AI Search
-description: Add faceted navigation for self-directed filtering in applications that integrate with Azure AI Search.
+description: Add faceted navigation for self-directed navigation in applications that integrate with Azure AI Search.
 
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
-ms.topic: concept-article
-ms.date: 02/26/2025
+ms.topic: how-to
+ms.date: 04/04/2025
 ---
 
-# Add faceted navigation to a search app
+# Add faceted navigation to search results
 
-Faceted navigation is used for self-directed drill-down filtering on query results in a search app, where your application offers form controls for scoping search to groups of documents (for example, categories or brands), and Azure AI Search provides the data structures and filters to back the experience.
+Faceted navigation is used for self-directed filtering on query results in a search app, where your application offers form controls for scoping search to groups of documents (for example, categories or brands), and Azure AI Search provides the data structures and filters to back the experience.
 
-In this article, learn how to return a faceted navigation structure in Azure AI Search.
+In this article, learn the steps for returning a faceted navigation structure in Azure AI Search. Once you're familiar with basic concepts and clients, continue to [Facet examples](search-faceted-navigation-examples.md) for syntax about various use cases, including basic faceting and distinct counts. 
+
+More facet capabilities are available through preview APIs:
+
++ hierarchical facet structures
++ facet filtering
++ facet aggregations
+
+[Facet navigation examples](search-faceted-navigation-examples.md) provide the syntax and usage for the preview features.
 
 ## Faceted navigation in a search page
 
-Facets are dynamic and returned on a query. A search response brings with it all of the facet categories used to navigate the documents in the result. The query executes first, and then facets are pulled from the current results and assembled into a faceted navigation structure.
+Facets are dynamic because they're based on each specific query result set. A search response brings with it all of the facet buckets used to navigate the documents in the result. The query executes first, and then facets are pulled from the current results and assembled into a faceted navigation structure.
 
-In Azure AI Search, facets are one layer deep and can't be hierarchical. If you aren't familiar with faceted navigation structures, the following example shows one on the left. Counts indicate the number of matches for each facet. The same document can be represented in multiple facets.
+In Azure AI Search, facets are one layer deep and can't be hierarchical unless you use the preview API. If you aren't familiar with faceted navigation structures, the following example shows one on the left. Counts indicate the number of matches for each facet. The same document can be represented in multiple facets.
 
 :::image source="media/search-faceted-navigation/azure-search-facet-nav.png" alt-text="Screenshot of faceted search results.":::
 
 Facets can help you find what you're looking for, while ensuring that you don't get zero results. As a developer, facets let you expose the most useful search criteria for navigating your search index.
 
 ## Faceted navigation in code
 
-Facets are enabled on supported fields in an index, and then specified on a query. At query time, a faceted navigation structure is returned at the top of the response.
+Facets are enabled on supported fields in an index, and then specified on a query. The faceted navigation structure is returned at the beginning of the response, followed by the results.
 
-The following REST example is an unqualified query (`"search": "*"`) that is scoped to the entire index (see the [built-in hotels sample](search-get-started-portal.md)). It returns a faceted navigation structure for the "Category" field.
+The following REST example is an empty query (`"search": "*"`) that is scoped to the entire index (see the [built-in hotels sample](search-get-started-portal.md)). The `facets` parameter specifies the "Category" field.
 
 ```http
 POST https://{{service_name}}.search.windows.net/indexes/hotels/docs/search?api-version={{api_version}}
@@ -47,7 +55,7 @@ POST https://{{service_name}}.search.windows.net/indexes/hotels/docs/search?api-
 }
 ```
 
-The response for the example includes the faceted navigation structure at the top. The structure consists of "Category" values and a count of the hotels for each one. It's followed by the rest of the search results, trimmed here to just one document for brevity. This example works well for several reasons. The number of facets for this field fall under the limit (default is 10) so all of them appear, and every hotel in the index of 50 hotels is represented in exactly one of these categories.
+The response for the example starts with the faceted navigation structure. The structure consists of "Category" values and a count of the hotels for each one. It's followed by the rest of the search results, trimmed here to just one document for brevity. This example works well for several reasons. The number of facets for this field fall under the limit (default is 10) so all of them appear, and every hotel in the index of 50 hotels is represented in exactly one of these categories.
 
 ```json
 {
@@ -94,214 +102,142 @@ The response for the example includes the faceted navigation structure at the to
                 "concierge"
             ],
             "ParkingIncluded": false,
-        }
+        },
+        . . . 
     ]
 }
 ```
 
 ## Enable facets on fields
 
-During [index creation or update](search-how-to-create-search-index.md), facets are enabled when you set `"facetable": true` on new fields that you add to an index. Although it's not strictly required, it's a best practice to also set the "filterable" attribute so that you can build the necessary filters that back the faceted navigation experience in your search application.
+You can add facets to new fields that contain plain text or numeric content. Supported data types include strings, dates, boolean fields, and numeric fields (but not vectors).
 
-Here's a JSON example of the hotels sample index, showing "facetable" and "filterable" on low cardinality fields that contain single values or short phrases: "Category", "Tags", "Rating".
+You can use the Azure portal, REST APIs, Azure SDKs or any method that supports the creation or update of index schemas in Azure AI Search. As a first step, identify which fields to use for faceting.
 
-```json
-{
-  "name": "hotels",  
-  "fields": [
-    { "name": "hotelId", "type": "Edm.String", "key": true, "searchable": false, "sortable": false, "facetable": false },
-    { "name": "Description", "type": "Edm.String", "filterable": false, "sortable": false, "facetable": false },
-    { "name": "HotelName", "type": "Edm.String", "facetable": false },
-    { "name": "Category", "type": "Edm.String", "filterable": true, "facetable": true },
-    { "name": "Tags", "type": "Collection(Edm.String)", "filterable": true, "facetable": true },
-    { "name": "Rating", "type": "Edm.Int32", "filterable": true, "facetable": true },
-    { "name": "Location", "type": "Edm.GeographyPoint" }
-  ]
-}
-```
+### Choose which fields to attribute
 
-### Prerequisites
+Facets can be calculated over single-value fields and collections. Fields that work best in faceted navigation have these characteristics:
 
-Add faceting to new fields that contain plain text or numeric content. Supported data types include strings, dates, boolean fields, and numeric fields (but not vectors).
+* Human readable (nonvector) content.
+* Low cardinality (a few distinct values that repeat throughout documents in your search corpus).
+* Short descriptive values (one or two words) that render nicely in a navigation tree.
+
+The values within a field, and not the field name itself, produce the facets in a faceted navigation structure. If the facet is a string field named *Color*, facets are blue, green, and any other value for that field. Review field values to ensure there are no typos, nulls, or casing differences. Consider [assigning a normalizer](search-normalizers.md) to a filterable and facetable field to smooth out minor variations in the text. For example, "Canada", "CANADA", and "canada" would all be normalized to one bucket.
+
+### Avoid unsupported fields
 
 You can't set facets on existing fields, on vector fields, or fields of type `Edm.GeographyPoint` or `Collection(Edm.GeographyPoint)`.
 
-On complex fields, "facetable" must be null.
+On complex field collections, "facetable" must be null. 
 
 ### Start with new field definitions
 
-Because attribution determines how a field is indexed, many attributes can only be set when fields are created. This restriction applies to facets and filters. If your index already exists and you add a new field definition, existing documents in the index get a null value for the new field. This null value is replaced the next time you [refresh the index](search-howto-reindex.md).
+Attributes that affect how a field is indexed can only be set when fields are created. This restriction applies to facets and filters. 
 
-### Choosing which fields to attribute
+If your index already exists, you can add a new field definition that provides facets. Existing documents in the index get a null value for the new field. This null value is replaced the next time you [refresh the index](search-howto-reindex.md).
 
-Facets can be calculated over single-value fields and collections. Fields that work best in faceted navigation have these characteristics:
+#### [**Azure portal**](#tab/portal-facet)
 
-* Human readable (nonvector) content.
+1. In the search services page of the [Azure portal](https://portal.azure.com), go to the **Fields** tab of the index and select **Add field**.
 
-* Low cardinality (a few distinct values that repeat throughout documents in your search corpus).
+1. Provide a name, data type, and attributes. We recommend adding filterable because it's common to set filters based on a facet bucket in the response. We recommend sortable because filters produce unordered results, and you might want to sort them in your application.
 
-* Short descriptive values (one or two words) that render nicely in a navigation tree.
+   You can also set searchable if you also want to support full text search on the field, and retrievable if you want to include the field in the search response.
 
-The values within a field, and not the field name itself, produce the facets in a faceted navigation structure. If the facet is a string field named *Color*, facets are blue, green, and any other value for that field.
+   :::image type="content" source="media/search-faceted-navigation/portal-add-facetable-field.png" alt-text="Screenshot of the Add fields page in the Azure portal." border="true" lightbox="media/search-faceted-navigation/portal-add-facetable-field.png":::
 
-### Defaults in REST and Azure SDKs
+1. Save the field definition.
 
-If you're using one of the Azure SDKs, your code must explicitly set the "facetable" attribute on a field.
+#### [**REST**](#tab/rest-facet)
 
-The REST API has defaults for field attributes based on the [data type](/rest/api/searchservice/supported-data-types). The following data types are "filterable" and "facetable" by default:
+When you define an index schema, facets are enabled when you set `"facetable": true` on new fields that you add to an index. Although it's not strictly required, it's a best practice to also set the "filterable" attribute so that you can build the necessary filters that back the faceted navigation experience in your search application.
+
+Start with [Create or Update Index](search-how-to-create-search-index.md) request and specify the fields collection.
+
+  Here's a JSON example of the hotels sample index, showing "facetable" and "filterable" on low cardinality fields that contain single values or short phrases: "Category", "Tags", "Rating".
+
+  ```json
+  {
+    "name": "hotels",  
+    "fields": [
+      { "name": "hotelId", "type": "Edm.String", "key": true, "searchable": false, "sortable": false, "facetable": false },
+      { "name": "Description", "type": "Edm.String", "filterable": false, "sortable": false, "facetable": false },
+      { "name": "HotelName", "type": "Edm.String", "facetable": false },
+      { "name": "Category", "type": "Edm.String", "filterable": true, "facetable": true },
+      { "name": "Tags", "type": "Collection(Edm.String)", "filterable": true, "facetable": true },
+      { "name": "Rating", "type": "Edm.Int32", "filterable": true, "facetable": true },
+      { "name": "Location", "type": "Edm.GeographyPoint" }
+    ]
+  }
+  ```
+
+#### Defaults in REST
+
+Both the Azure portal and the REST API have defaults for field attributes based on the [data type](/rest/api/searchservice/supported-data-types). The following data types are "filterable" and "facetable" by default:
 
 * `Edm.String` and `Collection(Edm.String)`
 * `Edm.DateTimeOffset` and `Collection(Edm.DateTimeOffset)`
 * `Edm.Boolean` and`Collection(Edm.Boolean)`
 * `Edm.Int32`, `Edm.Int64`, `Edm.Double`, and their collection equivalents
 
-## Return facets in a query
+#### [**Azure SDKs**](#tab/sdk-facet)
 
-Recall that facets are calculated from results in a query response. You only get facets for documents found by the current query. 
+If you're using one of the Azure SDKs, your code must explicitly set facetable on a field.
 
-1. Facets are configured at query-time. Use the [Search POST](/rest/api/searchservice/documents/search-post) or [Search GET](/rest/api/searchservice/documents/search-get) request, or an equivalent Azure SDK API, to specify facets. 
+Assign the facet property to fields using APIs that create or update an index.
 
-1. Set facet query parameters in the request. In Search POST, `facets` are an array of facet expressions to apply to the search query. Each facet expression contains a field name, optionally followed by a comma-separated list of name-value pairs. Valid facet parameters are `count`, `sort`, `values`, `interval`, and `timeoffset`.
+* [Azure SDK for .NET: SearchIndex.Fields Property](/dotnet/api/azure.search.documents.indexes.models.searchindex.fields)
+* [Azure SDK for Python: SearchField Class](/python/api/azure-search-documents/azure.search.documents.indexes.models.searchfield)
+* [Azure SDK for Java: SearchField Class](/java/api/com.azure.search.documents.indexes.models.searchfield)
+* [Azure SDK for JavaScript: Simple Field interface](/javascript/api/@azure/search-documents/simplefield)
 
-    | Facet parameter | Description and usage |
-    |-----------------|-----------------------|
-    | `count` | Maximum number of facet terms; default is 10. An example is `Tags,count:5`. There's no upper limit on the number of terms, but higher values degrade performance, especially if the faceted field contains a large number of unique terms. This is due to the way faceting queries are distributed across shards. You can set count to zero or to a value that's greater than or equal to the number of unique values in the "facetable" field to get an accurate count across all shards. The tradeoff is increased latency.
-    | `sort` | Set to "count", "-count", "value", "-value". Use `count` to sort descending by count. Use `-count` to sort ascending by count. Use `value` to sort ascending by value. Use `-value` to sort descending by value (for example, `"facet=category,count:3,sort:count"` gets the top three categories in facet results in descending order by the number of documents with each city name). If the top three categories are Budget, Motel, and Luxury, and Budget has five hits, Motel has 6, and Luxury has 4, then the buckets are in the order Motel, Budget, Luxury. For `-value`, `"facet=rating,sort:-value"` produces buckets for all possible ratings, in descending order by value (for example, if the ratings are from 1 to 5, the buckets are ordered 5, 4, 3, 2, 1, irrespective of how many documents match each rating). |
-    | `values` | Set to pipe-delimited numeric or `Edm.DateTimeOffset` values specifying a dynamic set of facet entry values. For example, `"facet=baseRate,values:10 | 20"` produces three buckets: one for base rate 0 up to but not including 10, one for 10 up to but not including 20, and one for 20 and higher. A string `"facet=lastRenovationDate,values:2010-02-01T00:00:00Z"` produces two buckets: one for hotels renovated before February 2010, and one for hotels renovated February 1, 2010 or later. The values must be listed in sequential, ascending order to get the expected results. |
-    | `interval` | An integer interval greater than zero for numbers, or minute, hour, day, week, month, quarter, year for date time values. For example, `"facet=baseRate,interval:100"` produces buckets based on base rate ranges of size 100. If base rates are all between $60 and $600, there are buckets for 0-100, 100-200, 200-300, 300-400, 400-500, and 500-600. The string `"facet=lastRenovationDate,interval:year"` produces one bucket for each year when hotels were renovated. |
-    | `timeoffset` | Can be set to (`[+-]hh:mm, [+-]hhmm, or [+-]hh`). If used, the timeoffset parameter must be combined with the interval option, and only when applied to a field of type `Edm.DateTimeOffset`. The value specifies the UTC time offset to account for in setting time boundaries. For example: `"facet=lastRenovationDate,interval:day,timeoffset:-01:00"` uses the day boundary that starts at 01:00:00 UTC (midnight in the target time zone). |
+---
 
-`count` and `sort` can be combined in the same facet specification, but they can't be combined with interval or values, and interval and values can't be combined together.
+## Return facets in a query
 
-Interval facets on date time are computed based on the UTC time if `timeoffset` isn't specified. For example, for `"facet=lastRenovationDate,interval:day"`, the day boundary starts at 00:00:00 UTC.
+Recall that facets are dynamically calculated from results in a query response. You only get facets for documents found by the current query.
 
-### Basic facet example
+#### [**Azure portal**](#tab/portal-facet-response)
 
-The following example works against the [hotels sample index](search-get-started-portal.md). You can use **JSON view** in Search Explorer to paste in the JSON query. This example shows three facets for "Category", "Tags", and "Rating", with a count override on "Tags" and a range override for "Rating", which is otherwise stored as a double in the index.
+Use JSON view in Search Explorer to set facet parameters in the [Azure portal](https://portal.azure.com).
 
-```http
-POST https://{{service_name}}.search.windows.net/indexes/hotels/docs/search?api-version={{api_version}}
-{
-    "search": "*",
-    "facets": [ 
-        "Category", 
-        "Tags,count:5", 
-        "Rating,values:1|2|3|4|5"
-    ],
-    "count": true
-}
-```
+1. Select an index and open Search Explorer in JSON View.
+1. Provide a query in JSON. You can type it out, copy the JSON from a REST example, or use intellisense to help with syntax. Refer to the REST example in the next tab for reference on facet expressions.
+1. Select **Search** to return faceted results, articulated in JSON.
 
-For each faceted navigation tree, there's a default limit of the top 10 facet instances found by the query. This default makes sense for navigation structures because it keeps the values list to a manageable size. You can override the default by assigning a value to "count". For example, `"Tags,count:5"` reduces the number of tags under the Tags section to the top five.
+Here's a screenshot of the [basic facet query example](search-faceted-navigation-examples.md#basic-facet-example) on the [hotels sample index](search-get-started-portal.md). You can paste in other examples in this article to return the results in Search Explorer.
 
-For Numeric and DateTime values only, you can explicitly set values on the facet field (for example, `facet=Rating,values:1|2|3|4|5`) to separate results into contiguous ranges (either ranges based on numeric values or time periods). Alternatively, you can add "interval", as in `facet=Rating,interval:1`. 
+:::image type="content" source="media/search-faceted-navigation/portal-facet-query.png" alt-text="Screenshot of the Search Explorer page in the Azure portal." border="true" lightbox="media/search-faceted-navigation/portal-facet-query.png":::
 
-Each range is built using 0 as a starting point, a value from the list as an endpoint, and then trimmed of the previous range to create discrete intervals.
+#### [**REST**](#tab/rest-facet-response)
 
-### Distinct values example
+1. Facets are configured at query-time. Use the [Search POST](/rest/api/searchservice/documents/search-post) or [Search GET](/rest/api/searchservice/documents/search-get) request, or an equivalent Azure SDK API, to specify facets. 
 
-You can formulate a query that returns a distinct value count for each "facetable" field. This example formulates an empty or unqualified query (`"search": "*"`) that matches on all documents, but by setting `top` to zero, you get just the counts, with no results.
+1. Set facet query parameters in the request. In Search POST, `facets` are an array of facet expressions to apply to the search query. Each facet expression contains a field name, optionally followed by a comma-separated list of name-value pairs. Valid facet parameters are `count`, `sort`, `values`, `interval`, and `timeoffset`.
 
-For brevity, this query includes just two fields marked as "facetable" in the hotels sample index.
+    | Facet parameter | Description and usage |
+    |-----------------|-----------------------|
+    | `count` | Maximum number of facet terms per structure; default is 10. An example is `Tags,count:5`. There's no upper limit on the number of terms, but higher values degrade performance, especially if the faceted field contains a large number of unique terms. This is due to the way faceting queries are distributed across shards. You can set count to zero or to a value that's greater than or equal to the number of unique values in the "facetable" field to get an accurate count across all shards. The tradeoff is increased latency.
+    | `sort` | Set to `count`, `-count`, `value`, `-value`. Use `count` to sort descending by count. Use `-count` to sort ascending by count. Use `value` to sort ascending by value. Use `-value` to sort descending by value (for example, `"facet=category,count:3,sort:count"` gets the top three categories in facet results in descending order by the number of documents with each Category name). If the top three categories are Budget, Motel, and Luxury, and Budget has five hits, Motel has 6, and Luxury has 4, then the buckets are in the order Motel, Budget, Luxury. For `-value`, `"facet=rating,sort:-value"` produces buckets for all possible ratings, in descending order by value (for example, if the ratings are from 1 to 5, the buckets are ordered 5, 4, 3, 2, 1, irrespective of how many documents match each rating). |
+    | `values` | Set to pipe-delimited numeric or `Edm.DateTimeOffset` values specifying a dynamic set of facet entry values. For example, `"facet=baseRate,values:10 | 20"` produces three buckets: one for base rate 0 up to but not including 10, one for 10 up to but not including 20, and one for 20 and higher. A string `"facet=lastRenovationDate,values:2010-02-01T00:00:00Z"` produces two buckets: one for hotels renovated before February 2010, and one for hotels renovated February 1, 2010 or later. The values must be listed in sequential, ascending order to get the expected results. |
+    | `interval` | An integer interval greater than zero for numbers, or minute, hour, day, week, month, quarter, year for date time values. For example, `"facet=baseRate,interval:100"` produces buckets based on base rate ranges of size 100. If base rates are all between $60 and $600, there are buckets for 0-100, 100-200, 200-300, 300-400, 400-500, and 500-600. The string `"facet=lastRenovationDate,interval:year"` produces one bucket for each year when hotels were renovated. |
+    | `timeoffset` | Can be set to (`[+-]hh:mm, [+-]hhmm, or [+-]hh`). If used, the `timeoffset` parameter must be combined with the interval option, and only when applied to a field of type `Edm.DateTimeOffset`. The value specifies the UTC time offset to account for in setting time boundaries. For example: `"facet=lastRenovationDate,interval:day,timeoffset:-01:00"` uses the day boundary that starts at 01:00:00 UTC (midnight in the target time zone). |
 
-```http
-POST https://{{service_name}}.search.windows.net/indexes/hotels/docs/search?api-version={{api_version}}
-{
-    "search": "*",
-    "count": true,
-    "top": 0,
-    "facets": [ 
-        "Category", "Address/StateProvince""
-    ]
-}
-```
+`count` and `sort` can be combined in the same facet specification, but they can't be combined with `interval` or `values`, and `interval` and `values` can't be combined together.
 
-Results from this query are as follows:
+Interval facets on date time are computed based on the UTC time if `timeoffset` isn't specified. For example, for `"facet=lastRenovationDate,interval:day"`, the day boundary starts at 00:00:00 UTC.
 
-```json
-{
-  "@odata.count": 50,
-  "@search.facets": {
-    "Address/StateProvince": [
-      {
-        "count": 9,
-        "value": "WA"
-      },
-      {
-        "count": 6,
-        "value": "CA "
-      },
-      {
-        "count": 4,
-        "value": "FL"
-      },
-      {
-        "count": 3,
-        "value": "NY"
-      },
-      {
-        "count": 3,
-        "value": "OR"
-      },
-      {
-        "count": 3,
-        "value": "TX"
-      },
-      {
-        "count": 2,
-        "value": "GA"
-      },
-      {
-        "count": 2,
-        "value": "MA"
-      },
-      {
-        "count": 2,
-        "value": "TN"
-      },
-      {
-        "count": 1,
-        "value": "AZ"
-      }
-    ],
-    "Category": [
-      {
-        "count": 13,
-        "value": "Budget"
-      },
-      {
-        "count": 12,
-        "value": "Suite"
-      },
-      {
-        "count": 7,
-        "value": "Boutique"
-      },
-      {
-        "count": 7,
-        "value": "Resort and Spa"
-      },
-      {
-        "count": 6,
-        "value": "Extended-Stay"
-      },
-      {
-        "count": 5,
-        "value": "Luxury"
-      }
-    ]
-  },
-  "value": []
-}
-```
+---
 
 ## Best practices for working with facets
 
 This section is a collection of tips and workarounds that are helpful for application development.
 
-### Initialize a faceted navigation structure
+We recommend the [C#: Add search to web apps](tutorial-csharp-overview.md) for an example of faceted navigation that includes code for the presentation layer. The sample also includes filters, suggestions, and autocomplete. It uses JavaScript and React for the presentation layer.
+
+### Initialize a faceted navigation structure with an unqualified or empty search string
 
-It's useful to initialize a search page with an open query (`"search": "*"`) to completely fill in the faceted navigation structure. As soon as you pass query terms in the request, the faceted navigation structure is scoped to just the matches in the results, rather than the entire index.
+It's useful to initialize a search page with an open query (`"search": "*"`) to completely fill in the faceted navigation structure. As soon as you pass query terms in the request, the faceted navigation structure is scoped to just the matches in the results, rather than the entire index. This practice is helpful for verifying facet and filter behaviors during testing. If you include match criteria in the query, the response excludes documents that don't match, which has the potential downstream effect of excluding facets.
 
 ### Clear facets
 
@@ -315,7 +251,15 @@ Remember that you can't use `Edm.GeographyPoint` or `Collection(Edm.GeographyPoi
 
 ### Check for bad data
 
-As you prepare data for indexing, check fields for null values, misspellings or case discrepancies, and single and plural versions of the same word. By default, filters and facets don't undergo lexical analysis or [spell check](speller-how-to-add.md), which means that all values of a "facetable" field are potential facets, even if the words differ by one character. Optionally, you can [assign a normalizer](search-normalizers.md) to a "filterable" and "facetable" field to smooth out variations in casing and characters.
+As you prepare data for indexing, check fields for null values, misspellings or case discrepancies, and single and plural versions of the same word. By default, filters and facets don't undergo lexical analysis or [spell check](speller-how-to-add.md), which means that all values of a "facetable" field are potential facets, even if the words differ by one character. 
+
+[Normalizers](search-normalizers.md) can mitigate data discrepancies, correcting for casing and character differences. Otherwise, to inspect your data, you can check fields at their source, or run queries that return values from the index.
+
+An index isn't the best place to fix nulls or invalid values. You should fix data problems in your source, assuming it's a database or persistent storage, or in a data cleansing step that you perform prior to indexing. 
+
+### Ordering facet buckets
+
+Although you can sort within a bucket, there's no parameters for controlling the order of facet buckets in the navigation structure as a whole. If you want facet buckets in a specific order, you must provide it in application code.
 
 ### Discrepancies in facet counts
 
@@ -346,4 +290,5 @@ Content type
 
 ## Next steps
 
-We recommend the [C#: Add search to web apps](tutorial-csharp-overview.md) for an example of faceted navigation that includes code for the presentation layer. The sample also includes filters, suggestions, and autocomplete. It uses JavaScript and React for the presentation layer.
+> [!div class="nextstepaction"]
+> [Facet navigation examples](search-faceted-navigation-examples.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファセットナビゲーションの文書内容の更新"
}
```

### Explanation
この変更は、`articles/search/search-faceted-navigation.md`ファイルの修正を示しており、ファセットナビゲーションに関する内容が更新されています。主な変更点には、タイトルや説明文の改訂、文の表現の明確化、内容の組織の整理が含まれています。

具体的には、ファセットナビゲーションが自己主導的なフィルタリングの手段であることを強調し、基本概念についての説明を更新しました。また、ファセット機能に新たに加わったプレビューAPIの機能についても述べており、階層的ファセット構造、ファセットフィルタリング、ファセット集約についての詳細が含まれています。これにより、ユーザーはより新しい機能を理解しやすくなっています。

文書内の例も修正され、特にレスポンスのサンプルやファセット構造に関する説明に関して、より明確で具体的な情報が提供されています。さらに、データの準備や欠陥の議論、新しいフィールド定義の重要性についても指摘されています。これにより、開発者は効果的にファセットナビゲーションを実装し、使用するための良い指針を得られるようになっています。

このように、ファセットナビゲーションに関する文書は、最新の情報を反映し、実用的な例を通じてより効果的なガイダンスを提供するよう改良されました。全体として、これらの変更は、Azure AI Searchを利用する開発者にとって大いに役立つものとなるでしょう。

## articles/search/search-faq-frequently-asked-questions.yml{#item-eab2ba}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ metadata:
   ms.author: haileytapia
   ms.service: azure-ai-search
   ms.topic: faq
-  ms.date: 01/16/2025
+  ms.date: 03/21/2025
 title: Azure AI Search Frequently Asked Questions
 summary:  Find answers to commonly asked questions about Azure AI Search.
 
@@ -36,7 +36,7 @@ sections:
         answer: |
           For vectors, the embedding models you use determines the linguistic experience. 
           
-          For nonvector strings and numbers, the default analyzer used for tokenization is standard Lucene and it's language agnostic. Otherwise, language support is expressed through [language analyzers](index-add-language-analyzers.md#supported-language-analyzers) that apply linguistic rules to inbound (indexing) and outbound (queries) content. Some features, such as [speller](speller-how-to-add.md#supported-languages) and [query rewrite](semantic-how-to-query-rewrite.md), are limited to a subset of languages.
+          For nonvector strings and numbers, the default analyzer used for tokenization is standard Lucene, which is language agnostic. Otherwise, language support is expressed through [language analyzers](index-add-language-analyzers.md#supported-language-analyzers) that apply linguistic rules to inbound (indexing) and outbound (queries) content. Some features, such as [speller](speller-how-to-add.md#supported-languages) and [query rewrite](semantic-how-to-query-rewrite.md), are limited to a subset of languages.
 
       - question: |
           How do I integrate search into my solution?
@@ -56,15 +56,27 @@ sections:
           You can't pause a search service. In Azure AI Search, computing resources are allocated when the service is created. It's not possible to release and reclaim those resources on-demand.
 
       - question: |
-          Can I upgrade, downgrade, rename or move the service?
+          Can I upgrade or downgrade the service?
         answer: |
-          Service tier, name, and region are fixed for the lifetime of the service.
+          Services created before April 2024 in select regions can be [upgraded to higher capacity clusters](search-how-to-upgrade.md). Downgrading your service isn't supported. 
+          
+          To get more capacity, you can also [switch to a higher pricing tier](search-capacity-planning.md#change-your-pricing-tier). Your region can't have [capacity constraints on the higher tier](search-region-support.md), and you can only move up between Basic and Standard (S1, S2, and S3) tiers, such as going from Basic to S1. Currently, you can't switch to a lower tier.
+          
+      - question: |
+          Can I rename or move the service?
+        answer: |
+          Service name and region are fixed for the lifetime of the service.
           
       - question: |
           If I migrate my search service to another subscription or resource group, should I expect any downtime?
         answer: |
           As long as you follow the [checklist before moving resources](/azure/azure-resource-manager/management/move-resource-group-and-subscription) and make sure each step is completed, there shouldn't be any downtime.
 
+      - question: |
+          Why do I see different storage limits for same-tier search services?
+        answer: |
+          Storage limits can vary by service creation date. In most supported regions, [newer services have higher storage limits than older services](search-limits-quotas-capacity.md#partition-storage-gb), even if they're on the same tier. However, you might be able to [upgrade your old service](search-how-to-upgrade.md) to access the new limits.
+
   - name: Indexing 
     questions:
       - question: |
@@ -130,7 +142,12 @@ sections:
       - question: |
           Why do I see different vector index size limits between my new search services and existing search services?
         answer: |
-          Azure AI Search rolled out improved vector index size limits worldwide for new search services, but [some regions experience capacity constraints](search-region-support.md), and some regions don't have the required infrastructure. New search services created in supported regions should see increased vector index size limits. Unfortunately, we can't migrate existing services to the new limits. Also, only vector indexes that use the Hierarchical Navigable Small World (HNSW) algorithm report on vector index size in the Azure portal. If your index uses exhaustive KNN, vector index size is reported as zero, even though the index contains vectors. 
+          Azure AI Search rolled out improved vector index size limits worldwide for new search services, but [some regions experience capacity constraints](search-region-support.md), and some regions don't have the required infrastructure. New search services created after May 2024 in supported regions should see increased vector index size limits. Alternatively, if you have an existing service in a supported region, you can [upgrade your service](search-how-to-upgrade.md) to access the new limits.
+          
+      - question: |
+          Why does my vector index show zero storage?
+        answer: |    
+          Only vector indexes that use the Hierarchical Navigable Small World (HNSW) algorithm report on vector index size in the Azure portal. If your index uses exhaustive KNN, vector index size is reported as zero, even though the index contains vectors. 
 
       - question: |
           How do I enable vector search on a search index?
@@ -141,7 +158,7 @@ sections:
           
           * Add a "vectorSearch" section to the index schema specifying the configuration used by vector search fields, including the parameters of the Approximate Nearest Neighbor algorithm used, like HNSW.
           
-          * Use the latest stable version[**2024-07-01**](/rest/api/searchservice), or an Azure SDK to create or update the index, load documents, and issue queries. For more information, see [Create a vector index](vector-search-how-to-create-index.md).
+          * Use the latest stable version, [**2024-07-01**](/rest/api/searchservice), or an Azure SDK to create or update the index, load documents, and issue queries. For more information, see [Create a vector index](vector-search-how-to-create-index.md).
 
   - name: Queries
     questions:
@@ -189,7 +206,7 @@ sections:
       - question: |
           Does Azure AI Search process customer data in other regions?
         answer: |
-          Processing (vectorization or applied AI transformations) is performed in the Geo that hosts the Azure AI services used by skills, or the Azure apps or functions hosting custom skills, or the Azure OpenAI or Azure AI Foundry region that hosts your deployed models. These resources are specified by you, so you can choose whether to provision them in the same Geo as your search service or not
+          Processing (vectorization or applied AI transformations) is performed in the Geo that hosts the Azure AI services used by skills, or the Azure apps or functions hosting custom skills, or the Azure OpenAI or Azure AI Foundry region that hosts your deployed models. These resources are specified by you, so you can choose whether to deploy them in the same Geo as your search service or not.
           
           If you send data to external (non-Azure) models or services, the processing location is determined by the external service. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search FAQの内容更新"
}
```

### Explanation
この変更は、`articles/search/search-faq-frequently-asked-questions.yml`ファイルの修正を示しており、Azure AI Searchに関するよくある質問（FAQ）の情報が更新されています。主な変更点には、日付の更新、質問と回答の内容の改訂が含まれます。

具体的には、FAQにいくつか新しい質問と回答が追加されており、特にサービスのアップグレード、ダウングレード、リネーム、移動の対応に関する情報が明確化されています。たとえば、選択された地域でサービスをアップグレードする方法や、同じ地域内でサービス名や地域を変更できないことについての注意が追加されました。また、サービスごとのストレージ制限の違いについても、新しい回答が追加されています。

他にも、ベクター検索に関する質問が改善されており、ベクターインデックスのサイズ制限や、インデックスのストレージに関する新しい情報も含まれています。これにより、ユーザーは新たな機能についての理解を深めることができ、より効果的にAzure AI Searchを活用するための具体的な指導を受けることができます。

このように、FAQは最新の情報を反映し、利用者が抱える疑問に対してより有用な回答を提供するよう更新されており、Azure AI Searchの使用に役立つ重要なリソースとなっています。全体的に、これらの変更はユーザーエクスペリエンスの向上に寄与するでしょう。

## articles/search/search-how-to-index-sql-database.md{#item-86d873}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 11/20/2024
+ms.date: 03/18/2025
 ---
 
 # Index data from Azure SQL Database
@@ -30,13 +30,17 @@ This article also provides:
 
 ## Prerequisites
 
-+ An [Azure SQL database](/azure/azure-sql/database/sql-database-paas-overview) with data in a single table or view, or a [SQL Managed Instance with a public endpoint](search-how-to-index-sql-managed-instance.md).
++ An [Azure SQL database](/azure/azure-sql/database/sql-database-paas-overview) or a [SQL Managed Instance with a public endpoint](search-how-to-index-sql-managed-instance.md).
 
-  Use a table if your data is large or if you need [incremental indexing](#CaptureChangedRows) using SQL's native change detection capabilities.
++ A single table or view.
 
-  Use a view if you need to consolidate data from multiple tables. Large views aren't ideal for SQL indexer. A workaround is to create a new table just for ingestion into your Azure AI Search index. You can use SQL integrated change tracking to track new and changed rows, which is easier to implement than High Water Mark.
+  Use a table if your data is large or if you need incremental indexing using SQL's native change detection capabilities ([SQL integrated change tracking](#indexing-new-changed-and-deleted-rows)) to reflect new, changed, and deleted rows in the search index.
 
-+ Read permissions. Azure AI Search supports SQL Server authentication, where the user name and password are provided on the connection string. Alternatively, you can [set up a managed identity and use Azure roles](search-howto-managed-identities-sql.md).
+  Use a view if you need to consolidate data from multiple tables. Large views aren't ideal for SQL indexer. A workaround is to create a new table just for ingestion into your Azure AI Search index. If you choose to go with a view, you can use [High Water Mark](#indexing-new-changed-and-deleted-rows) for change detection, but must use a workaround for deletion detection.
+
++ Primary key must be single-valued. On a table, it must also be non-clustered for full SQL integrated change tracking.
+
++ Read permissions. Azure AI Search supports SQL Server authentication, where the user name and password are provided on the connection string. Alternatively, you can [set up a managed identity and use Azure roles](search-howto-managed-identities-sql.md) with membership in **SQL Server Contributor** or **SQL DB Contributor** roles.
 
 To work through the examples in this article, you need the Azure portal or a [REST client](search-get-started-rest.md). If you're using Azure portal, make sure that access to all public networks is enabled in the Azure SQL firewall and that the client has access via an inbound rule. For a REST client that runs locally, configure the SQL Server firewall to allow inbound access from your device IP address. Other approaches for creating an Azure SQL indexer include Azure SDKs.
 
@@ -52,12 +56,12 @@ Use these instructions to create and load a table in Azure SQL Database for test
 
 1. On your Azure SQL database, select **Query editor (preview)** and then select **New Query**.
 
-1. Paste in and then run the T-SQL script that creates the hotels table.
+1. Paste in and then run the T-SQL script that creates the hotels table. A non-clustered primary key is a requirement for SQL integrated change tracking.
 
    ```tsql
    CREATE TABLE tbl_hotels
     (
-        Id TINYINT PRIMARY KEY,
+        Id TINYINT PRIMARY KEY NONCLUSTERED,
         Modified DateTime NULL DEFAULT '0000-00-00 00:00:00',
         IsDeleted TINYINT,
         HotelName VARCHAR(40),
@@ -93,9 +97,9 @@ Use these instructions to create and load a table in Azure SQL Database for test
    SELECT Description FROM tbl_hotels;
     ```
 
-You should see results similar to the following screenshot.
+   You should see results similar to the following screenshot.
 
-:::image type="content" source="media/search-how-to-index-sql-database/tsql-query-results.png" alt-text="Screenshot of query results showing the description field.":::
+   :::image type="content" source="media/search-how-to-index-sql-database/tsql-query-results.png" alt-text="Screenshot of query results showing the description field.":::
 
 The Description field provides the most verbose content. You should target this field for full text search and optional vectorization.
 
@@ -104,39 +108,42 @@ Now that you have a database table, you can use the Azure portal, REST client, o
 > [!TIP]
 > Another resource that provides sample content and code can be found on [Azure-Samples/SQL-AI-samples](https://github.com/Azure-Samples/SQL-AI-samples/tree/main/AzureSQLACSSamples/src).
 
-## Use the Azure portal
-
-You can use either the **Import data** wizard or **Import and vectorize data** wizard to automate indexing from an SQL database table or view. The data source configuration is similar for both wizards.
-
-1. [Start the wizard](search-import-data-portal.md#starting-the-wizards).
-
-1. On **Connect to your data**, select or verify that the data source type is either *Azure SQL Database* or *SQL database*.
+## Set up the indexer pipeline
 
-   The data source name refers to the data source connection object in Azure AI Search. If you use the vector wizard, your data source name is autogenerated using a custom prefix specified at the end of the wizard workflow.
+In this step, specify the data source, index, and indexer.
 
-1. Specify the server name, database name, and table or view name.
+### [**Azure portal**](#tab/portal-sql)
 
-   the Azure portal validates the connection. If the database is paused due to inactivity, navigate to the database server page and make sure database status is *online*. You can run a query on any table to activate the database.
+1. Make sure your SQL database is active and not paused due to inactivity. In the Azure portal, navigate to the database server page and verify the database status is *online*. You can run a query on any table to activate the database.
 
    :::image type="content" source="media/search-how-to-index-sql-database/database-online.png" alt-text="Screenshot of the database status page in the Azure portal.":::
 
-1. Specify an authentication method, either a SQL Server login defined during server setup, or a managed identity.
+1. Make sure you have a table or view that meets the requirements for indexers and change detection.
 
-   If you [configure Azure AI Search to use a managed identity](search-howto-managed-identities-data-sources.md), and you create a role assignment on the database server that grants **SQL Server Contributor** or **SQL DB Contributor** permissions to the identity, your indexer can connect to Azure SQL using Microsoft Entra ID and roles.
+   First, you can only pull from a single table or view. We recommend tables because they support SQL integrated change tracking policy, which detects new, updated, and deleted rows. A high water mark policy doesn't support row deletion and is harder to implement.
 
-1. For the **Import and vectorize data** wizard, you can specify options for change and deletion tracking.
+   Second, the primary key must be a single value (compound keys aren't supported) and non-clustered.
 
-   + Deletion tracking is based on [soft delete using custom metadata](#soft-delete-column-deletion-detection-policy).
+1. Switch to your search service and create a data source. Under **Search management** > **Data sources**, select **Add data source**:
 
-   + Change tracking is based on [SQL Server integrated change tracking](#sql-integrated-change-tracking-policy) or [high water mark change tracking](#high-water-mark-change-detection-policy).
+   1. For data source type, choose *Azure SQL Database*.
+   1. Provide a name for the data source object on Azure AI Search.
+   1. Use the dropdowns to select the subscription, account type, server, database, table or view, schema, and table name.
+   1. For change tracking we recommend **SQL Integrated Change Tracking Policy**.
+   1. For authentication, we recommend connecting with a [managed identity](search-howto-managed-identities-data-sources.md). Your search service must have **SQL Server Contributor** or **SQL DB Contributor** role membership on the database.
+   1. Select **Create** to create the data source.
 
-1. Continue with the remaining steps to complete the wizard:
+   :::image type="content" source="media/search-how-to-index-sql-database/search-data-source.png" alt-text="Screenshot of the data source creation page in the Azure portal.":::
 
-   + [Quickstart: Import data wizard](search-get-started-portal.md)
+1. Start the **Import data** wizard to create the index and indexer.
 
-   + [Quickstart: Import and vectorize data wizard](search-get-started-portal-import-vectors.md)
+   1. On the Overview page, select **Import data**.
+   1. Select the data source you just created, and select **Next**.
+   1. Skip the **Add cognitive skills (Optional)** page.
+   1. On **Customize target index**, name the index, set the key to your primary key in the table, and then group select *Retrievable* and *Searchable* for all fields, and optionally add *Filterable* and *Sortable* for short strings or numeric values.
+   1. On **Create an indexer**, name the indexer and select **Submit**.
 
-## Use the REST APIs
+### [**REST**](#tab/test-sql)
 
 This section demonstrates the REST API calls that create a data source, index, and indexer.
 
@@ -178,6 +185,7 @@ The data source definition specifies the data to index, credentials, and policie
    + Alternatively, you can specify a managed identity connection string that doesn't include database secrets with the following format: `Initial Catalog|Database=<your database name>;ResourceId=/subscriptions/<your subscription ID>/resourceGroups/<your resource group name>/providers/Microsoft.Sql/servers/<your SQL Server name>/;Connection Timeout=connection timeout length;`.
 
     For more information, see [Connect to Azure SQL Database indexer using a managed identity](search-howto-managed-identities-sql.md).
+
 > [!NOTE]
 > For the container name property, the value is restricted to only allow letters, numbers, underscores (_), dots (.), single dashes (-), and square brackets ([])
 
@@ -280,6 +288,8 @@ Once the index and data source have been created, you're ready to create the ind
 
 An indexer runs automatically when it's created. You can prevent this by setting "disabled" to true. To control indexer execution, [run an indexer on demand](search-howto-run-reset-indexers.md) or [put it on a schedule](search-howto-schedule-indexers.md).
 
+---
+
 ## Check indexer status
 
 To monitor the indexer status and execution history, check the indexer execution history in the Azure portal, or send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) REST API request
@@ -350,22 +360,23 @@ For Azure SQL indexers, there are two change detection policies:
 
 + "SqlIntegratedChangeTrackingPolicy" (applies to tables only)
 
-+ "HighWaterMarkChangeDetectionPolicy" (works for tables and views)
++ "HighWaterMarkChangeDetectionPolicy" (works for views)
 
 ### SQL Integrated Change Tracking Policy
 
 We recommend using "SqlIntegratedChangeTrackingPolicy" for its efficiency and its ability to identify deleted rows.
 
 Database requirements:
 
-+ SQL Server 2012 SP3 and later, if you're using SQL Server on Azure VMs
-+ Azure SQL Database or SQL Managed Instance
-+ Tables only (no views)
-+ On the database, [enable change tracking](/sql/relational-databases/track-changes/enable-and-disable-change-tracking-sql-server) for the table
-+ No composite primary key (a primary key containing more than one column) on the table
-+ No clustered indexes on the table. As a workaround, any clustered index would have to be dropped and re-created as nonclustered index, however, performance might be affected in the source compared to having a clustered index
++ Azure SQL Database or SQL Managed Instance. SQL Server 2016 or later if you're using an Azure VM.
++ Database must have [change tracking enabled](/sql/relational-databases/track-changes/enable-and-disable-change-tracking-sql-server)
++ Tables only (no views).
++ Tables can't be clustered. To meet this requirement, drop the clustered index and recreate it as non-clustered index. This workaround often degrades performance. Duplicating content in a second table that's dedicated to indexer processing can be a helpful mitigation. 
++ Tables can't be empty. If you use TRUNCATE TABLE to clear rows, a reset and rerun of the indexer won't remove the corresponding search documents. To remove orphaned search documents, you must [index them with a delete action](search-howto-reindex.md#delete-orphan-documents).
++ Primary key can't be a compound key (containing more than one column).
++ Primary key must be non-clustered if you want deletion detection.
 
-Change detection policies are added to data source definitions. To use this policy, create or update your data source like this:
+Change detection policies are added to data source definitions. To use this policy, edit the data source definition in the Azure portal, or use REST to update your data source like this:
 
 ```http
 POST https://myservice.search.windows.net/datasources?api-version=2024-07-01
@@ -382,10 +393,10 @@ api-key: admin-key
     }
 ```
 
-When using SQL integrated change tracking policy, don't specify a separate data deletion detection policy. The SQL integrated change tracking policy has built-in support for identifying deleted rows. However, for the deleted rows to be detected automatically, the document key in your search index must be the same as the primary key in the SQL table. 
+When using SQL integrated change tracking policy, don't specify a separate data deletion detection policy. The SQL integrated change tracking policy has built-in support for identifying deleted rows. However, for the deleted rows to be detected automatically, the document key in your search index must be the same as the primary key in the SQL table, and the primary key must be non-clustered.
 
-> [!NOTE]  
-> When using [TRUNCATE TABLE](/sql/t-sql/statements/truncate-table-transact-sql) to remove a large number of rows from a SQL table, the indexer needs to be [reset](/rest/api/searchservice/indexers/reset) to reset the change tracking state to pick up row deletions.
+<!-- > [!NOTE]  
+> When using [TRUNCATE TABLE](/sql/t-sql/statements/truncate-table-transact-sql) to remove a large number of rows from a SQL table, the indexer needs to be [reset](/rest/api/searchservice/indexers/reset) to reset the change tracking state to pick up row deletions. -->
 
 <a name="HighWaterMarkPolicy"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SQLデータベースのインデックス作成方法に関する文書の更新"
}
```

### Explanation
この変更は、`articles/search/search-how-to-index-sql-database.md`ファイルの修正を示しており、Azure SQLデータベースからのデータインデックス作成に関する方法が更新されています。主な変更点には、日付の更新、要件の明確化、新しい情報の追加が含まれます。

具体的には、プリケトリズのセクションで、Azure SQLデータベースまたはSQL管理インスタンスの利用に関して、再定義や要件が明確になっています。特に、プライマリキーが単一値である必要があることや、非クラスタ化されていることが強調されています。これにより、SQLインデックス作成における統合変更追跡の使用が推奨されています。

また、インデックス作成やデータソースの設定手順が更新され、必要な手順が明確に整理されています。特に、インデックス作成時にデータソースをどのように設定するか、さらにはデータの選択と追跡のための注意事項が詳述されています。

さらに、変更検出ポリシーに関する情報も更新され、SQL統合変更追跡の利用がより詳細に説明されています。これにより、ユーザーはデータベースの変更に基づいて効果的に情報をインデックスする方法を学びやすくなっています。

全体として、これらの変更は、Azure SQL Databaseからデータをインデックス作成する際のユーザーガイドをより使いやすくし、必要な手順や要件を明確に示すことに寄与しています。これにより、開発者はインデックス作成プロセスをより効率的に実行できるようになるでしょう。

## articles/search/search-how-to-large-index.md{#item-d34e42}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 02/25/2025
+ms.date: 03/21/2025
 ---
 
 # Index large data sets in Azure AI Search
@@ -21,7 +21,7 @@ These strategies assume familiarity with the [two basic approaches for importing
 
 This article complements [Tips for better performance](search-performance-tips.md), which offers best practices on index and query design. A well-designed index that includes only the fields and attributes you need is an important prerequisite for large-scale indexing.
 
-We recommend using a newer search service, created after April 3, 2024, for [higher storage per partition](search-limits-quotas-capacity.md#service-limits).
+We recommend using a search service created after April 3, 2024 for [higher storage per partition](search-limits-quotas-capacity.md#service-limits). Older services can also be [upgraded to benefit from higher partition storage](search-how-to-upgrade.md).
 
 > [!NOTE]
 > The strategies described in this article assume a single large data source. If your solution requires indexing from multiple data sources, see [Index multiple data sources in Azure AI Search](/samples/azure-samples/azure-search-dotnet-scale/multiple-data-sources/) for a recommended approach.
@@ -46,7 +46,7 @@ Because the optimal batch size depends on your index and your data, the best app
 
 ### Manage threads and a retry strategy
 
-Indexers have built-in thread management, but when you're using the push APIs, your application code needs to manage threads. Make sure there are sufficient threads to make full use of the available capacity, especially if you've recently increased partitions or upgraded to a higher tier search service. 
+Indexers have built-in thread management, but when you're using the push APIs, your application code needs to manage threads. Make sure there are sufficient threads to make full use of the available capacity, especially if you recently [upgraded your service](search-how-to-upgrade.md), [switched to a higher tier](search-capacity-planning.md#change-your-pricing-tier), or [increased partitions](search-capacity-planning.md#add-or-remove-partitions-and-replicas).
 
 1. [Increase the number of concurrent threads](tutorial-optimize-indexing-push-api.md#use-multiple-threadsworkers) in your client code.
 
@@ -97,7 +97,7 @@ When there are no longer any new or updated documents in the data source, indexe
 For more information about setting schedules, see [Create Indexer REST API](/rest/api/searchservice/indexers/create) or see [Schedule indexers for Azure AI Search](search-howto-schedule-indexers.md).
 
 > [!NOTE]
-> Some indexers that run on an older runtime architecture have a 24-hour rather than 2-hour maximum processing window. The two-hour limit is for newer content processors that run in an [internally managed multitenant environment](search-howto-run-reset-indexers.md#indexer-execution-environment). Whenever possible, Azure AI Search tries to offload indexer and skillset processing to the multi-tenant environment. If the indexer can't be migrated, it runs in the private environment and it can run for as long as 24 hours. If you're scheduling an indexer that exhibits these characteristics, assume a 24-hour processing window.
+> Some indexers that run on an older runtime architecture have a 24-hour rather than 2-hour maximum processing window. The two-hour limit is for newer content processors that run in an [internally managed multitenant environment](search-howto-run-reset-indexers.md#indexer-execution-environment). Whenever possible, Azure AI Search tries to offload indexer and skillset processing to the multitenant environment. If the indexer can't be migrated, it runs in the private environment and it can run for as long as 24 hours. If you're scheduling an indexer that exhibits these characteristics, assume a 24-hour processing window.
 
 <a name="parallel-indexing"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "大規模インデックス作成に関する文書の更新"
}
```

### Explanation
この変更は、`articles/search/search-how-to-large-index.md`ファイルの修正を示しており、Azure AI Searchにおける大規模データセットのインデックス作成方法に関する情報が更新されています。主な変更点としては、日付の更新、具体的なサービスの利用推奨の明確化、スレッド管理に関する注意が含まれています。

具体的には、推奨される検索サービスの作成日が明言され、2024年4月3日以降に作成されたサービスが高いストレージキャパシティを持つことが強調されています。また、従来のサービスもアップグレードすることで、同様の利点を得ることができることが追加されています。

さらに、インデクサについてのスレッド管理の記述が強化され、特にアプリケーションコードがスレッドを管理する必要があることが強調されています。最近サービスのアップグレードやパーティション数の増加を行った場合、十分なスレッド数を確保する重要性が示されています。

このように、文書全体にわたる修正は、ユーザーがAzure AI Searchを利用する際の大規模データセットのインデックス作成に関する理解を深め、より効果的にリソースを活用する方法を提供することを目指しています。全体として、これらの変更は文書の可読性と有用性を向上させるものとなっています。

## articles/search/search-how-to-load-search-index.md{#item-a72573}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.author: heidist
 
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 10/31/2024
+ms.date: 03/21/2025
 ---
 
 # Load data into a search index in Azure AI Search
@@ -28,7 +28,7 @@ You can prepare these documents yourself, but if content resides in a [supported
 
 Once data is indexed, the physical data structures of the index are locked in. For guidance on what can and can't be changed, see [Update and rebuild an index](search-howto-reindex.md).
 
-Indexing isn't a background process. A search service will balance indexing and query workloads, but if [query latency is too high](search-performance-analysis.md#impact-of-indexing-on-queries), you can either [add capacity](search-capacity-planning.md#adjust-capacity) or identify periods of low query activity for loading an index.
+Indexing isn't a background process. A search service will balance indexing and query workloads, but if [query latency is too high](search-performance-analysis.md#impact-of-indexing-on-queries), you can either [add capacity](search-capacity-planning.md#add-or-remove-partitions-and-replicas) or identify periods of low query activity for loading an index.
 
 For more information, see [Data import strategies](search-what-is-data-import.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスのデータロードに関する文書の更新"
}
```

### Explanation
この変更は、`articles/search/search-how-to-load-search-index.md`ファイルの修正を示しており、Azure AI Searchにおける検索インデックスへのデータのロード方法に関する情報が更新されています。主な変更点としては、日付の更新、インデクシングのプロセスに関する説明の明確化が含まれています。

具体的には、文書の日付が2024年10月31日から2025年3月21日に変更されました。この日付更新により、情報が最新のものであることが示されています。

また、インデクシングがバックグラウンドプロセスではなく、検索サービスがインデクシングとクエリワークロードをバランスよく管理することについての説明が強化されています。特に、クエリのレイテンシが高い場合の対策として、キャパシティを追加するか、インデックスロードのためにクエリ活動が低い時間帯を特定することが提案されています。この部分の文言がより具体的に更新され、ユーザーにとっての理解が深まる内容となっています。

全体として、これらの変更は、Azure AI Searchを用いた検索インデックスへのデータロードに関するユーザーガイドを更新し、実践的なアドバイスを提供することを目的としています。この修正により、ユーザーはインデクシングのプロセスとその影響についてより良い知識を得ることができるようになります。

## articles/search/search-how-to-semantic-chunking.md{#item-4a1d07}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: rawan
 ms.author: rawan
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 11/22/2024
+ms.date: 04/07/2025
 ms.custom:
   - references_regions
   - ignite-2024
@@ -36,13 +36,15 @@ For illustration purposes, this article uses the [sample health plan PDFs](https
 
 + [An indexer-based indexing pipeline](search-indexer-overview.md) with an index that accepts the output. The index must have fields for receiving headings and content.
 
++ [An index projection](search-how-to-define-index-projections.md) for one-to-many indexing.
+
 + [A supported data source](search-indexer-overview.md#supported-data-sources) having text content that you want to chunk.
 
-+ [A skillset with Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) that splits documents based on paragraph boundaries.
++ A skillset with these two skills:
 
-+ [An Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md) that generates vector embeddings.
+  + [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) that splits documents based on paragraph boundaries. This skill has region requirements. An Azure AI multi-service resource must be in the same region as Azure AI Search with AI Enrichment.
 
-+ [An index projection](search-how-to-define-index-projections.md) for one-to-many indexing.
+  + [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md) that generates vector embeddings. This skill also has region requirements. The model must be in the same region as Azure AI Search.
 
 ## Prepare data files
 
@@ -52,7 +54,7 @@ The raw inputs must be in a [supported data source](search-indexer-overview.md#s
 
 + Supported indexers can be any indexer that can handle the supported file formats. These indexers include [Blob indexers](search-howto-indexing-azure-blob-storage.md), [OneLake indexers](search-how-to-index-onelake-files.md), [File indexers](search-file-storage-integration.md).
 
-+ Supported regions for this feature include: East US, West US2, West Europe, North Central US. Be sure to [check this list](search-region-support.md#azure-public-regions) for updates on regional availability.
++ Supported regions for the portal experience of this feature include: East US, West Europe, North Central US. If your setting up your skillset programmatically, you can use any Document Intelligence region that also provides the AI enrichment feature of Azure AI Search. For more information, see [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).
 
 You can use the Azure portal, REST APIs, or an Azure SDK package to [create a data source](search-howto-indexing-azure-blob-storage.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックチャンクに関する文書の更新"
}
```

### Explanation
この変更は、`articles/search/search-how-to-semantic-chunking.md`ファイルの修正を示しており、Azure AI Searchにおけるセマンティックチャンクに関する情報が更新されています。主な変更点には、日付の更新、新しいスキルやデータソースの追加、および地域の要件の明確化が含まれています。

具体的には、文書の日付が2024年11月22日から2025年4月7日に変更され、最新の情報が反映されています。また、インデクサーベースのインデックスパイプラインや、データチャンクに必要なデータソースに関する新しい情報が追加されています。

変更内容には、スキルセットに関する説明が強化され、文書を段落の境界に基づいて分割する「Document Layout skill」と、ベクトル埋め込みを生成する「Azure OpenAI Embedding skill」が明確にリストされています。これに伴い、地域要件についても詳細が加わり、スキルセットがAzure AI SearchのAI強化機能を提供する地域に設定されている必要がある旨が説明されています。

さらに、サポートされるインデクサーや地域に関する情報も更新され、多様なインデクシングオプションが説明されています。このような修正を通じて、ユーザーはAzure AI Searchを活用したセマンティックチャンク手法に関する理解を深め、より効果的なデータハンドリングが可能になることを期待できます。全体として、文書が明確さと実用性を増したことを反映しています。

## articles/search/search-how-to-upgrade.md{#item-990225}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,115 @@
+---
+title: Service Upgrade in the Azure Portal
+titleSuffix: Azure AI Search
+description: Learn how to upgrade your existing Azure AI Search service to high-capacity storage and processors in your region.
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: how-to
+ms.custom: references_regions
+ms.date: 04/04/2025
+---
+
+# Upgrade your Azure AI Search service in the Azure portal
+
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+An upgrade brings older search services to the capabilities of new services created in the same region. Specifically, it upgrades the computing power of the underlying service. This one-time operation doesn't introduce breaking changes to your application, and you shouldn't need to change any code.
+
+For [eligible services](#upgrade-eligibility), an upgrade increases the [partition storage](#higher-storage-limits) and [vector index size](#higher-vector-limits) on the same tier at no extra cost.
+
+> [!TIP]
+> Looking to [change your pricing tier](search-capacity-planning.md#change-your-pricing-tier)? You can now move up between Basic and Standard (S1, S2, and S3) tiers.
+
+This article describes how to upgrade your service in the [Azure portal](https://portal.azure.com/). Alternatively, you can use the [Search Management REST APIs](/rest/api/searchmanagement/) to upgrade your service programmatically. For more information, see [Manage your search service using REST](search-manage-rest.md#upgrade-a-service).
+
+## About service upgrades
+
+In April 2024, Azure AI Search increased the [storage capacity](search-limits-quotas-capacity.md#service-limits) of newly created search services. Services created before April 2024 saw no capacity changes, so if you wanted larger and faster partitions, you had to create a new service. However, some older services can now be upgraded to benefit from the higher capacity partitions.
+
+In this preview, an upgrade only increases the [storage limit](#higher-storage-limits) and [vector index size](#higher-vector-limits) of [eligible services](#upgrade-eligibility).
+
+### Upgrade eligibility
+
+To qualify for an upgrade, your service:
+
+> [!div class="checklist"]
+> + Must have been created before April 2024. Services created after April 2024 should already have higher capacity. To see when you created your service, [check your service creation date](#check-your-service-creation-or-upgrade-date).
+> + Must be in a region where higher capacity is enabled.
+> + Must be in one of the following regions:
+>   + East US
+>   + North Central US
+>   + West Central US
+>   + UK South
+
+<!-- Check the footnotes in the [list of supported regions](search-region-support.md). -->
+
+### Higher storage limits
+
+For [eligible services](#upgrade-eligibility), the following table compares the storage limit (per partition) before and after an upgrade.
+
+| | Basic <sup>1</sup> | S1 | S2 | S3/HD | L1 | L2 |
+|-|-|-|-|-|-|-|
+| **Limit before upgrade** | 2 GB | 25 GB | 100 GB | 200 GB | 1 TB | 2 TB |
+| **Limit after upgrade** | 15 GB | 160 GB | 512 GB | 1 TB | 2 TB | 4 TB |
+
+<sup>1</sup> Basic services created before April 3, 2024 were originally limited to one partition, which increases to three partitions after an upgrade. [Partition counts for all other pricing tiers](search-limits-quotas-capacity.md#service-limits) stay the same.
+
+### Higher vector limits
+
+For [eligible services](#upgrade-eligibility), the following table compares the vector index size (per partition) before and after an upgrade.
+
+| | Basic | S1 | S2 | S3/HD | L1 | L2 |
+|-|-|-|-|-|-|-|
+| **Limit before upgrade** | 0.5 GB <sup>1</sup> or 1 GB <sup>2</sup> | 1 GB <sup>1</sup> or 3 GB <sup>2</sup> | 6 GB <sup>1</sup> or 12 GB <sup>2</sup> | 12 GB <sup>1</sup> or 36 GB <sup>2</sup> | 12 GB | 36 GB |
+| **Limit after upgrade** | 5 GB | 35 GB | 150 GB | 300 GB | 150 GB | 300 GB |
+
+<sup>1</sup> Applies to services created before July 1, 2023.
+
+<sup>2</sup> Applies to services created between July 1, 2023 and April 3, 2024 in all regions except Germany West Central, Qatar Central, and West India, to which the <sup>1</sup> limits apply.
+
+## Check your service creation or upgrade date
+
+On the **Overview** page, you can view various metadata about your search service, including the **Create date (UTC)** and **Upgrade date (UTC)**.
+
+:::image type="content" source="media/search-how-to-upgrade/service-creation-upgrade-metadata.png" alt-text="Screenshot of the service creation and service upgrade dates in the Azure portal." border="true":::
+
+The date you created your service partially determines its [upgrade eligibility](#upgrade-eligibility). If your service has never been upgraded, the **Upgrade date (UTC)** doesn't appear.
+
+## Upgrade your service
+
+You can’t undo a service upgrade. Before you proceed, make sure that you want to permanently increase the [storage limit](#higher-storage-limits) and [vector index size](#higher-vector-limits) of your search service. We recommend that you test this operation in a nonproduction environment.
+
+To upgrade your service:
+
+1. Sign in to the [Azure portal](https://portal.azure.com/) and select your search service.
+
+1. On the **Overview** page, select **Upgrade** from the command bar.
+
+   :::image type="content" source="media/search-how-to-upgrade/upgrade-button.png" alt-text="Screenshot of the Upgrade button on the command bar in the Azure portal." border="true":::
+
+   If this button appears dimmed, an upgrade isn’t available for your service. Your service either has the [latest upgrade](#check-your-service-creation-or-upgrade-date) or is in an [unsupported region](#upgrade-eligibility).
+
+1. Review the upgrade details for your service, and then select **Upgrade**.
+
+   :::image type="content" source="media/search-how-to-upgrade/upgrade-panel.png" alt-text="Screenshot of your service upgrade details in the Azure portal." border="true":::
+
+   A confirmation appears reminding you that the upgrade can't be undone.
+
+1. To permanently upgrade your service, select **Upgrade**.
+
+   :::image type="content" source="media/search-how-to-upgrade/upgrade-confirmation.png" alt-text="Screenshot of the upgrade confirmation in the Azure portal." border="true":::
+
+1. Check your notifications to confirm that the operation started.
+
+   The upgrade is an asynchronous operation, so you can continue using your service. Depending on the size of your service, the upgrade can take several hours to complete.
+
+   If the upgrade fails, your service returns to its original state.
+
+## Next step
+
+After you upgrade your search service, you might want to reconsider your scale configuration:
+
+> [!div class="nextstepaction"]
+> [Estimate and manage capacity of an Azure AI Search service](search-capacity-planning.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Searchサービスのアップグレード方法についての新規文書"
}
```

### Explanation
この変更は、`articles/search/search-how-to-upgrade.md`ファイルの新規作成を示しており、Azure AI Searchサービスをアップグレードする方法に関する詳細なガイドラインが提供されています。この文書は、高容量ストレージとプロセッサにサービスを改善するためのステップを説明しています。

新しい文書には、まずサービスのアップグレードの意義と、それによって得られるメリットが明確に説明されています。具体的には、既存の検索サービスを新しいサービスの機能にアップグレードすることで、コンピューティングパワーの向上が図られ、アプリケーションに対する破壊的変更を伴わないことが強調されています。

また、アップグレードの eligibility（適格性）についての詳細なガイドラインも含まれており、どの地域や条件でサービスのアップグレードが可能かを示しています。さらに、アップグレードを行った場合のストレージ制限やベクトルインデックスサイズの比較表が提供されており、ユーザーがアップグレードの影響を理解しやすくなっています。

加えて、Azureポータルを使用してサービスをアップグレードする具体的な手順やスクリーンショットも含まれており、実際の操作を視覚的にサポートしています。文書の最後には、アップグレード後にスケール設定を再考することを推奨するセクションも含まれており、ユーザーが適切にサービスを管理できるよう配慮されています。

この新しい文書は、ユーザーがAzure AI Searchサービスを効果的にアップグレードし、その機能を最大限に活用するための貴重なリソースとして機能します。

## articles/search/search-howto-index-encrypted-blobs.md{#item-a7097a}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Tutorial: Index encrypted blobs'
+title: 'Tutorial: Index Encrypted Blobs'
 titleSuffix: Azure AI Search
 description: Learn how to index and extract text from encrypted documents in Azure Blob Storage with Azure AI Search.
 
@@ -11,110 +11,112 @@ ms.custom:
   - ignite-2023
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 02/24/2025
+ms.date: 03/28/2025
 ---
 
 # Tutorial: Index and enrich encrypted blobs for full-text search in Azure AI Search
 
-This tutorial shows you how to use [Azure AI Search](search-what-is-azure-search.md) to index documents that have been previously encrypted with a customer-managed key in [Azure Blob Storage](/azure/storage/blobs/storage-blobs-introduction). 
+Learn how to use [Azure AI Search](search-what-is-azure-search.md) to index documents that were encrypted with a customer-managed key in [Azure Blob Storage](/azure/storage/blobs/storage-blobs-introduction).
 
-Normally, an indexer can't extract content from blobs that have been encrypted using the [client-side encryption](/azure/storage/blobs/client-side-encryption) of the Azure Blob Storage client library because the indexer doesn't have access to the customer-managed encryption key in [Azure Key Vault](/azure/key-vault/general/overview). However, by leveraging the [DecryptBlobFile custom skill](https://github.com/Azure-Samples/azure-search-power-skills/blob/main/Utils/DecryptBlobFile), followed by the [Document Extraction skill](cognitive-search-skill-document-extraction.md), you can provide controlled access to the key to decrypt the files and then extract content from them. This unlocks the ability to index and enrich these documents without compromising the encryption status of your stored documents.
+Normally, an indexer can't extract content from blobs that were encrypted using [client-side encryption](/azure/storage/blobs/client-side-encryption) in the Azure Blob Storage client library. This is because the indexer doesn't have access to the customer-managed encryption key in [Azure Key Vault](/azure/key-vault/general/overview). However, using the [DecryptBlobFile custom skill](https://github.com/Azure-Samples/azure-search-power-skills/blob/main/Utils/DecryptBlobFile) and the [Document Extraction skill](cognitive-search-skill-document-extraction.md), you can provide controlled access to the key to decrypt the files and then extract content from them. This unlocks the ability to index and enrich these documents without compromising the encryption status of your stored documents.
 
-Starting with previously encrypted whole documents (unstructured text) such as PDF, HTML, DOCX, and PPTX in Azure Blob Storage, this tutorial uses a REST client and the Search REST APIs to perform the following tasks:
+Starting with previously encrypted whole documents (unstructured text) such as PDF, HTML, DOCX, and PPTX in Azure Blob Storage, this tutorial uses a REST client and the Search REST APIs to:
 
 > [!div class="checklist"]
-> + Define a pipeline that decrypts the documents and extracts text from them.
-> + Define an index to store the output.
-> + Execute the pipeline to create and load the index.
-> + Explore results using full text search and a rich query syntax.
-
-If you don't have an Azure subscription, open a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
+> + Define a pipeline that decrypts the documents and extracts text from them
+> + Define an index to store the output
+> + Execute the pipeline to create and load the index
+> + Explore results using full-text search and a rich query syntax
 
 ## Prerequisites
 
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+
 + [Azure AI Search](search-create-service-portal.md) on any tier or region.
 
 + [Azure Storage](https://azure.microsoft.com/services/storage/), Standard performance (general-purpose v2).
 
-+ Blobs encrypted with a customer-managed key. See [Tutorial: Encrypt and decrypt blobs using Azure Key Vault](/azure/storage/blobs/storage-encrypt-decrypt-blobs-key-vault) if you need to create sample data.
++ Blobs encrypted with a customer-managed key. To create sample data, see [Tutorial: Encrypt and decrypt blobs using Azure Key Vault](/azure/storage/blobs/storage-encrypt-decrypt-blobs-key-vault).
 
 + [Azure Key Vault](https://azure.microsoft.com/services/key-vault/) in the same subscription as Azure AI Search. The key vault must have **soft-delete** and **purge protection** enabled.
 
-Custom skill deployment creates an Azure Function app and an Azure Storage account. Since these resources are created for you, they aren't listed as a prerequisite. When you're finished with this tutorial, remember to clean up the resources so that you aren't billed for services you're not using.
+Custom skill deployment creates an Azure Function app and an Azure Storage account. These resources are created for you, so they aren't listed as a prerequisite. When you finish this tutorial, remember to clean up the resources so that you aren't billed for services you're not using.
 
 > [!NOTE]
-> Skillsets often require [attaching an Azure AI services multi-service resource](cognitive-search-attach-cognitive-services.md). As written, this skillset has no dependency on Azure AI services and thus no key is required. If you later add enrichments that invoke built-in skills, remember to update your skillset accordingly.
+> Skillsets often require [attaching an Azure AI services multi-service resource](cognitive-search-attach-cognitive-services.md). As written, this skillset has no dependency on Azure AI services, so no key is required. If you later add enrichments that invoke built-in skills, remember to update your skillset accordingly.
 
 ## Deploy the custom skill
 
-This example uses the sample [DecryptBlobFile](https://github.com/Azure-Samples/azure-search-power-skills/blob/main/Utils/DecryptBlobFile) project from the [Azure Search Power Skills](https://github.com/Azure-Samples/azure-search-power-skills) GitHub repository. In this section, you deploy the skill to an Azure Function so that it can be used in a skillset. A built-in deployment script creates an Azure Function resource with a **psdbf-function-app-** prefix and loads the skill. You are prompted to provide a subscription and resource group. Be sure to choose the same subscription that your Azure Key Vault instance lives in.
+This tutorial uses the sample [DecryptBlobFile](https://github.com/Azure-Samples/azure-search-power-skills/blob/main/Utils/DecryptBlobFile) project from the [Azure Search Power Skills](https://github.com/Azure-Samples/azure-search-power-skills) GitHub repository. In this section, you deploy the skill to an Azure Function so that it can be used in a skillset. A built-in deployment script creates an Azure Function resource with a **psdbf-function-app-** prefix and loads the skill. You're prompted to provide a subscription and resource group. Be sure to choose the subscription that contains your Azure Key Vault instance.
 
-Operationally, the DecryptBlobFile skill takes the URL and SAS token for each blob as inputs, and it outputs the downloaded, decrypted file using the file reference contract that Azure AI Search expects. Recall that DecryptBlobFile needs the encryption key to perform the decryption. As part of setup, you also create an access policy that grants DecryptBlobFile function access to the encryption key in Azure Key Vault.
+Operationally, the DecryptBlobFile skill takes the URL and SAS token for each blob as inputs. It outputs the downloaded, decrypted file using the file reference contract that Azure AI Search expects. Recall that DecryptBlobFile needs the encryption key to perform the decryption. As part of setup, you also create an access policy that grants DecryptBlobFile function access to the encryption key in Azure Key Vault.
 
-1. Click the **Deploy to Azure** button found on the [DecryptBlobFile landing page](https://github.com/Azure-Samples/azure-search-power-skills/blob/main/Utils/DecryptBlobFile#deployment), which will open the provided Resource Manager template within the Azure portal.
+1. On the [DecryptBlobFile landing page](https://github.com/Azure-Samples/azure-search-power-skills/blob/main/Utils/DecryptBlobFile#deployment), select **Deploy to Azure** to open the Resource Manager template in the Azure portal.
 
-1. Choose the same subscription where your Azure Key Vault instance exists (this tutorial won't work if you select a different subscription).
+1. Choose the subscription where your Azure Key Vault instance exists. This tutorial doesn't work if you choose a different subscription.
 
 1. Select an existing resource group or create a new one. A dedicated resource group makes cleanup easier later.
 
-1. Select **Review + create**, make sure you agree to the terms, and then select **Create** to deploy the Azure Function.
+1. Select **Review + create**, agree to the terms, and then select **Create** to deploy the Azure Function.
 
     :::image type="content" source="media/indexing-encrypted-blob-files/arm-template.png" alt-text="Screenshot of the ARM template page in Azure portal." border="true":::
 
 1. Wait for the deployment to finish.
 
-You should have an Azure Function app that contains the decryption logic and an Azure Storage resource that will store application data. In the next several steps, you'll give the app permissions to access the key vault and collect information that you'll need for the REST calls.
+You should have an Azure Function app that contains the decryption logic and an Azure Storage resource that will store application data. In the next steps, you give the app permissions to access the key vault and collect information that you'll need for the REST calls.
 
 ## Grant permissions in Azure Key Vault
 
-1. Navigate to your Azure Key Vault service in the Azure portal. [Create an access policy](/azure/key-vault/general/assign-access-policy-portal) in the Azure Key Vault that grants key access to the custom skill.
+1. Go to your Azure Key Vault service in the Azure portal. [Create an access policy](/azure/key-vault/general/assign-access-policy-portal) in the Azure Key Vault that grants key access to the custom skill.
 
-1. On the left pane, select **Access policies**, and then select **+ Create** to start the **Create an access policy** wizard.
+1. From the left pane, select **Access policies**, and then select **+ Create** to start the **Create an access policy** wizard.
 
     :::image type="content" source="media/indexing-encrypted-blob-files/keyvault-access-policies.png" alt-text="Screenshot of the Access Policy command in the left pane." border="true":::
 
-1. On the **Permissions** page under **Configure from template**, select **Azure Data Lake Storage or Azure Storage**.
+1. On the **Permissions** page, under **Configure from template**, select **Azure Data Lake Storage or Azure Storage**.
 
 1. Select **Next**.
 
-1. On the **Principal** page, select the Azure Function instance that you deployed. You can search for it using the resource prefix that was used to create it in step 2, which has a default prefix value of **psdbf-function-app**.
+1. On the **Principal** page, select the Azure Function instance you deployed. You can search for it using its resource prefix, which has a default value of **psdbf-function-app**.
 
 1. Select **Next**.
 
 1. On **Review + create**, select **Create**.
 
 ## Collect app information
 
-1. Navigate to the **psdbf-function-app** function in the Azure portal, and make a note of the following properties you'll need for the REST calls:
+1. Go to the **psdbf-function-app** function in the Azure portal. Make a note of the following properties you'll need for the REST calls.
 
 1. Get the function URL, which can be found under **Essentials** on the main page for the function.
 
     :::image type="content" source="media/indexing-encrypted-blob-files/function-uri.png" alt-text="Screenshot of the overview page and Essentials section of the Azure Function app." border="true":::
 
-1. Get the host key code, which can be found by navigating to **App keys**, clicking to show the **default** key, and copying the value.
+1. Get the host key code, which can be found by going to **App keys** and showing the **default** key, and copying the value.
 
     :::image type="content" source="media/indexing-encrypted-blob-files/function-host-key.png" alt-text="Screenshot of the App Keys page of the Azure Function app." border="true":::
 
-## Get an admin api-key and URL for Azure AI Search
+## Get an admin key and URL for Azure AI Search
+
+1. Sign in to the [Azure portal](https://portal.azure.com).
 
-1. Sign in to the [Azure portal](https://portal.azure.com), and in your search service **Overview** page, get the name of your search service. You can confirm your service name by reviewing the endpoint URL. If your endpoint URL were `https://mydemo.search.windows.net`, your service name would be `mydemo`.
+1. On your search service **Overview** page, get the name of your search service. You can confirm your service name by reviewing the endpoint URL. For example, if your endpoint URL is `https://mydemo.search.windows.net`, your service name is `mydemo`.
 
-2. In **Settings** > **Keys**, get an admin key for full rights on the service. There are two interchangeable admin keys, provided for business continuity in case you need to roll one over. You can use either the primary or secondary key on requests for adding, modifying, and deleting objects.
+1. In **Settings** > **Keys**, get an admin key for full rights on the service. There are two interchangeable admin keys, provided for business continuity in case you need to roll one over. You can use either the primary or secondary key on requests for adding, modifying, and deleting objects.
 
-All requests require an api-key in the header of every request sent to your service. A valid key establishes trust, on a per request basis, between the application sending the request and the service that handles it.
+An API key is required in the header of every request sent to your service. A valid key establishes trust, on a per-request basis, between the application sending the request and the service that handles it.
 
 ## Set up a REST client
 
-Create variables for endpoints and keys:
+Create the following variables for endpoints and keys.
 
 | Variable    | Where to get it |
 |-------------|-----------------|
 | `admin-key` | On the **Keys** page of the Azure AI Search service.  |
 | `search-service-name` | The name of the Azure AI Search service. The URL is `https://{{search-service-name}}.search.windows.net`. |
 | `storage-connection-string` | In the storage account, on the **Access Keys** tab, select **key1** > **Connection string**. |
 | `storage-container-name` | The name of the blob container that has the encrypted files to be indexed. |
-| `function-uri` |  In the Azure Function under **Essentials** on the main page. |
-| `function-code` | In the Azure Function, by navigating to **App keys**, clicking to show the **default** key, and copying the value. |
+| `function-uri` |  In the Azure Function, under **Essentials** on the main page. |
+| `function-code` | In the Azure Function, by going to **App keys**, showing the **default** key, and copying the value. |
 | `api-version` | Leave as **2020-06-30**. |
 | `datasource-name` | Leave as **encrypted-blobs-ds**. |
 | `index-name` | Leave as **encrypted-blobs-idx**. |
@@ -123,25 +125,25 @@ Create variables for endpoints and keys:
 
 ## Review and run each request
 
-Use HTTP requests to create the objects of an enrichment pipeline:
+Use the following HTTP requests to create the objects of an enrichment pipeline.
 
 + **PUT request to create the index**: This search index holds the data that Azure AI Search uses and returns.
 
-+ **POST request to create the data source**: This data source specifies the connection to your storage account containing the encrypted blob files. 
++ **POST request to create the data source**: This data source specifies the connection to your storage account containing the encrypted blob files.
 
-+ **PUT request to create the skillset**: The skillset specifies the custom skill definition for the Azure Function that will decrypt the blob file data, and a [DocumentExtractionSkill](cognitive-search-skill-document-extraction.md) to extract the text from each document after it has been decrypted.
++ **PUT request to create the skillset**: The skillset specifies the custom skill definition for the Azure Function that will decrypt the blob file data. It also specifies a [DocumentExtractionSkill](cognitive-search-skill-document-extraction.md) to extract the text from each document after it's decrypted.
 
 + **PUT request to create the indexer**: Running the indexer retrieves the blobs, applies the skillset, and indexes and stores the results. You must run this request last. The custom skill in the skillset invokes the decryption logic.
 
 ## Monitor indexing
 
-Indexing and enrichment commence as soon as you submit the Create Indexer request. Depending on how many documents are in your storage account, indexing can take a while. To find out whether the indexer is still running, send a **Get Indexer Status** request and review the response to learn whether the indexer is running, or to view error and warning information.  
+Indexing and enrichment commence as soon as you submit the Create Indexer request. Depending on how many documents are in your storage account, indexing can take a while. To find out whether the indexer is still running, send a **Get Indexer Status** request and review the response to learn whether the indexer is running or view error and warning information.  
 
-If you're using the Free tier, the following message is expected: `"Could not extract content or metadata from your document. Truncated extracted text to '32768' characters"`. This message appears because blob indexing on the Free tier has a [32K limit on character extraction](search-limits-quotas-capacity.md#indexer-limits). You won't see this message for this data set on higher tiers. 
+If you're using the Free tier, expect the following message: `"Could not extract content or metadata from your document. Truncated extracted text to '32768' characters"`. This message appears because blob indexing on the Free tier has a [32,000 limit on character extraction](search-limits-quotas-capacity.md#indexer-limits). You don't see this message for this data set on higher tiers.
 
 ## Search your content
 
-After indexer execution is finished, you can run some queries to verify that the data has been successfully decrypted and indexed. Navigate to your Azure AI Search service in the Azure portal, and use the [Search Explorer](search-explorer.md) to run queries over the indexed data.
+After indexer execution is finished, you can run queries to verify that the data is successfully decrypted and indexed. Go to your Azure AI Search service in the Azure portal and use the [Search Explorer](search-explorer.md) to run queries over the indexed data.
 
 ## Clean up resources
 
@@ -151,6 +153,6 @@ You can find and manage resources in the Azure portal, using the All resources o
 
 ## Next steps
 
-Now that you have successfully indexed encrypted files, you can [iterate on this pipeline by adding more skills](cognitive-search-defining-skillset.md). This will allow you to enrich and gain additional insights to your data.
+Now that you've indexed encrypted files, you can [iterate on this pipeline by adding more skills](cognitive-search-defining-skillset.md) to enrich and gain more insights into your data.
 
-If you're working with doubly encrypted data, you might want to investigate the index encryption features available in Azure AI Search. Although the indexer needs decrypted data for indexing purposes, once the index exists, it can be encrypted in a search index using a customer-managed key. This will ensure that your data is always encrypted when at rest. For more information, see [Configure customer-managed keys for data encryption in Azure AI Search](search-security-manage-encryption-keys.md).
+If you're working with doubly encrypted data, you might want to investigate the index encryption features available in Azure AI Search. Although the indexer needs decrypted data for indexing purposes, once the index exists, it can be encrypted in a search index using a customer-managed key. This ensures that your data is always encrypted when at rest. For more information, see [Configure customer-managed keys for data encryption in Azure AI Search](search-security-manage-encryption-keys.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "暗号化されたBLOBをインデックスするチュートリアルの更新"
}
```

### Explanation
この変更は、`articles/search/search-howto-index-encrypted-blobs.md`ファイルの修正を示しており、Azure AI Searchを使用して暗号化されたBLOBをインデックスする方法に関するチュートリアルの内容が更新されています。主な変更点には、文言の明確化、日付の更新、そして一部の内容が整理されたことが含まれています。

具体的には、チュートリアルのタイトルが「Index encrypted blobs」から「Index Encrypted Blobs」に変更され、標題がより一貫性を持つように調整されています。また、文中の説明がリフレーズされ、読みやすさと明瞭さが向上しました。例として、「通常、インデクサーは…」の部分が条件に基づいて適切に構造化され、アクセスポリシーの設定などの具体的な手順が明確に記述されています。

さらに、必須条件や手順のセクションでのテキストが整理され、項目ごとの説明が整然としました。特に、Azure Key Vaultにおけるアクセス権の設定に関する指示が明確化されたことにより、ユーザーが手順を順を追って理解するのが容易になっています。

このような更新によって、ユーザーはAzure AI Searchを使用して暗号化されたデータを安全にインデックスし、情報を効率的に取得するための手順をより良く理解できるようになります。全体として、文書は内容の整合性と信頼性を高める方向で改善されており、ユーザーの学習体験を向上させるための重要な一歩となっています。

## articles/search/search-howto-managed-identities-data-sources.md{#item-edf98d}

<details>
<summary>Diff</summary>
````diff
@@ -17,9 +17,9 @@ ms.date: 11/22/2024
 # Configure a search service to connect using a managed identity in Azure AI Search
 
 > [!IMPORTANT]
-> User-assigned managed identity assignment is in public preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [Management preview REST API](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2024-03-01-preview&preserve-view=true#identity) provides user-assigned managed identity assignment for Azure AI Search. Support for a *system-assigned* managed identity is generally available.
+> User-assigned managed identity assignment is in public preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [Management preview REST API](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true#identity) provides user-assigned managed identity assignment for Azure AI Search. Support for a *system-assigned* managed identity is generally available.
 
-You can use Microsoft Entra ID and role assignments for outbound connections from Azure AI Search to resources providing data, applied AI, or vectorization during indexing or queries. 
+You can use Microsoft Entra ID and role assignments for outbound connections from Azure AI Search to resources providing data, applied AI, or vectorization during indexing or queries.
 
 To use roles on an outbound connection, first configure your search service to use either a [system-assigned or user-assigned managed identity](/azure/active-directory/managed-identities-azure-resources/overview) as the security principal for your search service in a Microsoft Entra tenant. Once you have a managed identity, you can assign roles for authorized access. Managed identities and role assignments eliminate the need for passing secrets and credentials in a connection string or code.
 
@@ -131,7 +131,7 @@ For more information, see [Create or Update Service (Management REST API)](/rest
 ## Create a user-assigned managed identity
 
 > [!IMPORTANT]
-> Part of this scenario is in public preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [Management preview REST API](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2024-03-01-preview&preserve-view=true#identity) provides user-assigned managed identity configuration for Azure AI Search.
+> Part of this scenario is in public preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [Management preview REST API](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true#identity) provides user-assigned managed identity configuration for Azure AI Search.
 
 A user-assigned managed identity is a resource on Azure. You can create multiple user-assigned managed identities if you want more granularity in role assignments. For example, you might want separate identities for different applications and scenarios.
 
@@ -170,12 +170,12 @@ Associating a user-assigned managed identity is supported in the Azure portal, i
 
 ### [**REST API**](#tab/rest-user)
 
-You can use a preview Management REST API instead of the Azure portal to assign a user-assigned managed identity. Use API versions `2021-04-01-preview` or later. This example uses `2024-06-01-preview`.
+You can use a preview Management REST API instead of the Azure portal to assign a user-assigned managed identity. Use API versions `2021-04-01-preview` or later. This example uses `2025-05-01-preview`.
 
-1. Formulate a request to [UPDATE](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true#identity) a search service.
+1. Formulate a request to [UPDATE](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2025-05-01-preview&preserve-view=true#identity) a search service.
 
     ```http
-    PUT https://management.azure.com/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Search/searchServices/mysearchservice?api-version=2024-06-01-preview
+    PUT https://management.azure.com/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Search/searchServices/mysearchservice?api-version=2025-05-01-preview
     {
       "location": "[region]",
       "sku": {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "管理対象 ID とデータソースに関するドキュメントの更新"
}
```

### Explanation
この変更は、`articles/search/search-howto-managed-identities-data-sources.md`ファイルの修正を示しており、Azure AI Searchにおける管理対象IDの使用に関する情報が更新されています。具体的には、いくつかの重要なAPIバージョンの更新が行われています。

主な変更点として、ユーザー割り当て管理対象IDの設定に関する言及が更新され、新しいAPIバージョン `2025-02-01-preview` と `2025-05-01-preview` が指定されています。これにより、ユーザーは最新のAPIを使用して管理対象IDを効果的に設定できるようになります。また、重要な注意事項も含まれており、管理対象IDが公開プレビュー中であることが確認され、潜在的な制限や使用条件に注意を促しています。

さらに、Microsoft Entra IDとロールの割り当てを使って、Azure AI SearchからデータやAIリソースへのアウトバウンド接続を管理する方法に関する説明は、そのまま維持されています。これにより、ユーザーはアウトバウンド接続の設定を容易に理解し、実行できるようになります。

全体として、これらの変更はドキュメントの一貫性と最新性を保つものであり、管理対象IDの使用やAPI更新に関心のあるユーザーにとって有益です。新しい情報によって、ユーザーはより安全で効果的な方法でAzure AI Searchのリソースを管理できるようになります。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 12/09/2024
+ms.date: 03/21/2025
 ---
 
 # Update or rebuild an index in Azure AI Search
@@ -134,7 +134,7 @@ The following table explains the various per-document status codes that can be r
 
 If your client code frequently encounters a 207 response, one possible reason is that the system is under load. You can confirm this by checking the statusCode property for 503. If the statusCode is 503, we recommend throttling indexing requests. Otherwise, if indexing traffic doesn't subside, the system could start rejecting all requests with 503 errors.
 
-Status code 429 indicates that you have exceeded your quota on the number of documents per index. You must either create a new index or upgrade for higher capacity limits.
+Status code 429 indicates that you've exceeded your quota on the number of documents per index. You must either [upgrade for higher capacity limits](search-how-to-upgrade.md) or create a new index.
 
 > [!NOTE]
 > When you upload `DateTimeOffset` values with time zone information to your index, Azure AI Search normalizes these values to UTC. For example, 2024-01-13T14:03:00-08:00 is stored as 2024-01-13T22:03:00Z. If you need to store time zone information, add an extra column to your index for this data point.
@@ -228,7 +228,7 @@ Some modifications require an index drop and rebuild, replacing a current index
 | Assign an analyzer to a field | [Analyzers](search-analyzers.md) are defined in an index, assigned to fields, and then invoked during indexing to inform how tokens are created. You can add a new analyzer definition to an index at any time, but you can only *assign* an analyzer when the field is created. This is true for both the **analyzer** and **indexAnalyzer** properties. The **searchAnalyzer** property is an exception (you can assign this property to an existing field). |
 | Update or delete an analyzer definition in an index | You can't delete or change an existing analyzer configuration (analyzer, tokenizer, token filter, or char filter) in the index unless you rebuild the entire index. |
 | Add a field to a suggester | If a field already exists and you want to add it to a [Suggesters](index-add-suggesters.md) construct, rebuild the index. |
-| Switch tiers | In-place upgrades aren't supported. If you require more capacity, create a new service and rebuild your indexes from scratch. To help automate this process, you can use a code sample that backs up your index to a series of JSON files. You can then recreate the index in a search service you specify.|
+| Upgrade your service or tier | If you need more capacity, check if you can [upgrade your service](search-how-to-upgrade.md) or [switch to a higher service tier](search-capacity-planning.md#change-your-pricing-tier). If not, you must create a new service and rebuild your indexes from scratch. To help automate this process, you can use a code sample that backs up your index to a series of JSON files. You can then recreate the index in a search service you specify. |
 
 The order of operations is:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス再構築に関するドキュメントの更新"
}
```

### Explanation
この変更は、`articles/search/search-howto-reindex.md`ファイルの修正を示しており、Azure AI Searchにおけるインデックスの更新または再構築に関連するドキュメントの内容が更新されています。主に、日付の更新といくつかの記述の明確化が含まれています。

具体的には、ドキュメントの日付が「12/09/2024」から「03/21/2025」に変更されており、より最新の情報を反映させています。また、ステータスコード429に関する説明の文が改善され、利用者は「新しいインデックスを作成するか、より高いキャパシティリミットにアップグレードする必要がある」という情報が明確に強調されています。これにより、ユーザーは制限に直面した際の対処方法を理解しやすくなっています。

さらに、「ティアの切り替え」に関する言及が更新され、サービスタイプのアップグレードに関する情報が具体的に説明されています。サービスのアップグレード手順や、新しいサービスを作成してインデックスを再構築するプロセスに関連する情報がクリアになっています。

これらの変更により、ユーザーはAzure AI Searchのインデックス管理に関する最新情報をよりスムーズに理解でき、機能を効果的に活用するための道筋が提供されています。全体として、ドキュメントは一貫しており、実際の使用に役立つ具体的な指示が含まれています。

## articles/search/search-howto-run-reset-indexers.md{#item-fb10c8}

<details>
<summary>Diff</summary>
````diff
@@ -9,26 +9,28 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 12/19/2024
+ms.date: 03/19/2025
 ---
 
 # Run or reset indexers, skills, or documents
 
 In Azure AI Search, there are several ways to run an indexer:
 
-+ [Run immediately upon indexer creation](search-howto-create-indexers.md), assuming it's not created in "disabled" mode.
++ [Run immediately upon indexer creation](search-howto-create-indexers.md). This is the default unless you create the indexer in a "disabled" state.
 + [Run on a schedule](search-howto-schedule-indexers.md) to invoke execution at regular intervals.
 + Run on demand, with or without a "reset".
 
 This article explains how to run indexers on demand, with and without a reset. It also describes indexer execution, duration, and concurrency.
 
 ## How indexers connect to Azure resources
 
-Indexers are one of the few subsystems that make overt outbound calls to other Azure resources. In terms of Azure roles, indexers don't have separate identities: a connection from the search engine to another Azure resource is made using the [system or user-assigned managed identity](search-howto-managed-identities-data-sources.md) of a search service. If the indexer connects to an Azure resource on a virtual network, you should create a [shared private link](search-indexer-howto-access-private.md) for that connection. For more information about secure connections, see the [Security in Azure AI Search](search-security-overview.md).
+Indexers are one of the few subsystems that make overt outbound calls to other Azure resources. You can use keys or roles to authenticate the connection.
+
+In terms of Azure roles, indexers don't have separate identities: a connection from the search engine to another Azure resource is made using the [system or user-assigned managed identity](search-howto-managed-identities-data-sources.md) of a search service, plus a role assignment on the target Azure resource. If the indexer connects to an Azure resource on a virtual network, you should create a [shared private link](search-indexer-howto-access-private.md) for that connection.
 
 ## Indexer execution
 
-A search service runs one indexer job per [search unit](search-capacity-planning.md#concepts-search-units-replicas-partitions). Every search service starts with one search unit, but each new partition or replica increases the search units of your service. You can check the search unit count in the Azure portal's Essential section of the **Overview** page. If you need concurrent processing, make sure your search units include sufficient replicas. Indexers don't run in the background, so you might detect more query throttling than usual if the service is under pressure.
+A search service runs one indexer job per [search unit](search-capacity-planning.md#concepts-search-units-replicas-partitions). Every search service starts with one search unit, but each new partition or replica increases the search units of your service. You can check the search unit count in the Azure portal's Essential section of the **Overview** page. If you need concurrent processing, make sure your search units include sufficient replicas. Indexers don't run in the background, so you might experience more query throttling than usual if the service is under pressure.
 
 The following screenshot shows the number of search units, which determines how many indexers can run at once.
 
@@ -42,45 +44,46 @@ You can run multiple indexers at one time assuming sufficient capacity, but each
 
 An indexer job runs in a managed execution environment. Currently, there are two environments:
 
-+ A private execution environment runs on search clusters that are specific to your search service. If your search service is Standard2 or higher, you can [set the `executionEnvironment` parameter](search-how-to-create-indexers.md?tabs=indexer-rest#create-an-indexer) in the indexer definition to always run an indexer in the private execution environment. 
++ A private execution environment runs on search clusters that are specific to your search service.
 
 + A multitenant environment has content processors that are managed and secured by Microsoft at no extra cost. This environment is used to offload computationally intensive processing, leaving service-specific resources available for routine operations. Whenever possible, most skillsets execute in the multitenant environment. This is the default.
 
-  *Computationally intensive processing* refers to skillsets running on content processors and indexer jobs that process a high volume of documents, or documents of a large size. Non-skillset processing on the multitenant content processors is determined by hueristics and system information and isn't under customer control. S2 services and higher support pinning an indexer and skillset processing exclusively to your search clusters through the `executionEnvironment` parameter.
+  *Computationally intensive processing* refers to skillsets running on content processors and indexer jobs that process a high volume of documents, or documents of a large size. Non-skillset processing on the multitenant content processors is determined by heuristics and system information and isn't under customer control. 
+
+You can prevent usage of the multitenant environment on Standard2 or higher services by pinning an indexer and skillset processing exclusively to your search clusters. [Set the `executionEnvironment` parameter](search-how-to-create-indexers.md?tabs=indexer-rest#create-an-indexer) in the indexer definition to always run an indexer in the private execution environment.
 
-  > [!NOTE]
-  > [IP firewalls](search-indexer-securing-resources.md#network-access-and-indexer-execution-environments) block the multitenant environment, so if you have a firewall, create a rule that allows multitenant processing.
+[IP firewalls](search-indexer-securing-resources.md#setting-up-ip-ranges-for-indexer-execution) block the multitenant environment, so if you have a firewall, [create a rule](search-indexer-howto-access-ip-restricted.md#configure-ip-firewall-rules-to-allow-indexer-connections-from-azure-ai-search) that allows multitenant processor connections.
 
 Indexer limits vary for each environment:
 
 | Workload | Maximum duration | Maximum jobs | Execution environment |
 |----------|------------------|---------------------|-----------------------------|
-| Private execution | 24 hours | One indexer job per [search unit](search-capacity-planning.md#concepts-search-units-replicas-partitions) <sup>1</sup>.  | Indexing doesn't run in the background. Instead, the search service will balance all indexing jobs against ongoing queries and object management actions (such as creating or updating indexes). When running indexers, you should expect to see [some query latency](search-performance-analysis.md#impact-of-indexing-on-queries) if indexing volumes are large. |
+| Private execution | 24 hours | One indexer job per [search unit](search-capacity-planning.md#concepts-search-units-replicas-partitions) <sup>1</sup>.  | Indexing doesn't run in the background. Instead, the search service balances all indexing jobs against ongoing queries and object management actions (such as creating or updating indexes). When running indexers, you should expect to see [some query latency](search-performance-analysis.md#impact-of-indexing-on-queries) if indexing volumes are large. |
 | Multitenant| 2 hours <sup>2</sup> | Indeterminate <sup>3</sup> | Because the content processing cluster is multitenant, content processors are added to meet demand. If you experience a delay in on-demand or scheduled execution, it's probably because the system is either adding processors or waiting for one to become available.|
 
 <sup>1</sup> Search units can be [flexible combinations](search-capacity-planning.md#partition-and-replica-combinations) of partitions and replicas, but indexer jobs aren't tied to one or the other. In other words, if you have 12 units, you can have 12 indexer jobs running concurrently in private execution, no matter how the search units are deployed.
 
-<sup>2</sup> If more than two hours are needed to process all of the data, [enable change detection](search-howto-create-indexers.md#change-detection-and-internal-state) and [schedule the indexer](search-howto-schedule-indexers.md) to run at 5 minute intervals to resume indexing quickly if it stops due to a timeout. See [Indexing a large data set](search-howto-large-index.md) for more strategies.
+<sup>2</sup> If more than two hours are needed to process all of the data, [enable change detection](search-howto-create-indexers.md#change-detection-and-internal-state) and [schedule the indexer](search-howto-schedule-indexers.md) to run at 5-minute intervals to resume indexing quickly if it stops due to a time out. See [Indexing a large data set](search-howto-large-index.md) for more strategies.
 
 <sup>3</sup> "Indeterminate" means that the limit isn't quantified by the number of jobs. Some workloads, such as skillset processing, can run in parallel, which could result in many jobs even though only one indexer is involved. Although the environment doesn't impose constraints, [indexer limits](search-limits-quotas-capacity.md#indexer-limits) for your search service still apply.
 
 ## Run without reset
 
-A [Run Indexer](/rest/api/searchservice/indexers/run) operation will detect and process only what it necessary to synchronize the search index with changes in the underlying data source. Incremental indexing starts by locating an internal high-water mark to find the last updated search document, which becomes the starting point for indexer execution over new and updated documents in the data source.
+A [Run Indexer](/rest/api/searchservice/indexers/run) operation detects and processes only what it necessary to synchronize the search index with changes in the underlying data source. Incremental indexing starts by locating an internal high-water mark to find the last updated search document, which becomes the starting point for indexer execution over new and updated documents in the data source.
 
-[Change detection](search-howto-create-indexers.md#change-detection-and-internal-state) is essential for determining what's new or updated in the data source. Indexers use the change detection capabilities of the underlying data source to determine what's new or updated in the data source. 
+[Change detection](search-howto-create-indexers.md#change-detection-and-internal-state) is essential for determining what's new or updated in the data source. Indexers use the change detection capabilities of the underlying data source to determine what's new or updated in the data source.
 
 + Azure Storage has built-in change detection through its LastModified property.
 
 + Other data sources, such as Azure SQL or Azure Cosmos DB, have to be configured for change detection before the indexer can read new and updated rows. 
 
-If the underlying content is unchanged, a run operation has no effect. In this case, indexer execution history will indicate `0\0` documents processed.
+If the underlying content is unchanged, a run operation has no effect. In this case, indexer execution history indicates `0\0` documents processed.
 
-You'll need to reset the indexer, as explained in the next section, to reprocess in full.
+You need to reset the indexer, as explained in the next section, to reprocess in full.
 
 ## Resetting indexers
 
-After the initial run, an indexer keeps track of which search documents have been indexed through an internal *high-water mark*. The marker is never exposed, but internally the indexer knows where it last stopped.
+After the initial run, an indexer keeps track of which search documents are indexed through an internal *high-water mark*. The marker is never exposed, but internally the indexer knows where it last stopped.
 
 If you need to rebuild all or part of an index, you can clear the indexer's high-water mark through a reset. Reset APIs are available at decreasing levels in the object hierarchy:
 
@@ -90,23 +93,26 @@ If you need to rebuild all or part of an index, you can clear the indexer's high
 
 After reset, follow with a Run command to reprocess new and existing documents. Orphaned search documents having no counterpart in the data source can't be removed through reset/run. If you need to delete documents, see [Documents - Index](/rest/api/searchservice/documents) instead.
 
+> [!NOTE]
+> Tables can't be empty. If you use TRUNCATE TABLE to clear rows, a reset and rerun of the indexer won't remove the corresponding search documents. To remove orphaned search documents, you must [index them with a delete action](search-howto-reindex.md#delete-orphan-documents).
+
 <a name="reset-indexers"></a>
 
 ## How to reset and run indexers
 
-Reset clears the high-water mark. All documents in the search index will be flagged for full overwrite, without inline updates or merging into existing content. For indexers with a skillset and [enrichment caching](cognitive-search-incremental-indexing-conceptual.md), resetting the index will also implicitly reset the skillset. 
+Reset clears the high-water mark. All documents in the search index are flagged for full overwrite, without inline updates or merging into existing content. For indexers with a skillset and [enrichment caching](cognitive-search-incremental-indexing-conceptual.md), resetting the index also implicitly resets the skillset. 
 
 The actual work occurs when you follow a reset with a Run command:
 
 + All new documents found the underlying source are added to the search index. 
-+ All documents that exist in both the data source and search index will be overwritten in the search index. 
-+ Any enriched content created from skillsets will be rebuilt. The enrichment cache, if one is enabled, is refreshed.
++ All documents that exist in both the data source and search index are overwritten in the search index. 
++ Any enriched content created from skillsets are rebuilt. The enrichment cache, if one is enabled, is refreshed.
 
-As previously noted, reset is a passive operation: you must follow up a Run request to rebuild the index. 
+As previously noted, reset is a passive operation: you must follow with a Run request to rebuild the index. 
 
 Reset/run operations apply to a search index or a knowledge store, to specific documents or projections, and to cached enrichments if a reset explicitly or implicitly includes skills.
 
-Reset also applies to create and update operations. It will not trigger deletion or clean up of orphaned documents in the search index. For more information about deleting documents, see [Documents - Index](/rest/api/searchservice/documents/).
+Reset also applies to create and update operations. It won't trigger deletion or clean up of orphaned documents in the search index. For more information about deleting documents, see [Documents - Index](/rest/api/searchservice/documents/).
 
 Once you reset an indexer, you can't undo the action.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサの実行とリセットに関するドキュメントの更新"
}
```

### Explanation
この変更は、`articles/search/search-howto-run-reset-indexers.md`ファイルの修正を示しており、Azure AI Searchにおけるインデクサの実行やリセットに関する説明が更新されています。主に日付の更新、記述の明確化、及び新しい情報が追加されています。

具体的には、ドキュメントの日付が「12/19/2024」から「03/19/2025」に変更されており、より最新の情報を反映しています。また、インデクサの接続方法や認証に関する説明が改訂され、システムまたはユーザー割り当ての管理対象IDに加えて役割の割り当ても必要であることを明示的に記載しています。

ナビゲーションや機能に関する詳細も強化されており、例えば、プライベート実行環境やマルチテナント環境の違いに関する説明が更新されました。これにより、ユーザーはAzure AI Searchのインデクサがどのように機能するかをより良く理解できるようになります。

さらに、リセット操作やその後の実行操作についての記述も強化され、インデクサの動作に関する注意事項や利用方法が明確にされています。特に、リセット後には必ず実行操作を行う必要があることが強調されています。

これらの変更を通じて、ユーザーはインデクサの使用時に直面する可能性のある問題や、効果的な使用方法についての情報を得ることができ、サポートを強化する内容となっています。全体として、このドキュメントはAzure AI Searchを利用する上で非常に有益な情報を提供しており、ユーザーがインデクサの動作をより良く管理できるようになります。

## articles/search/search-indexer-how-to-access-private-sql.md{#item-1bd4cc}

<details>
<summary>Diff</summary>
````diff
@@ -87,7 +87,7 @@ For more information about connection properties, see [Create an Azure SQL Manag
    Because shared private link support for SQL managed instances is still in preview, you need a preview version of the management REST API. Use `2021-04-01-preview` or a later preview API version for this step. We recommend using the latest preview API version.
 
    ```azurecli
-   az rest --method put --uri https://management.azure.com/subscriptions/{{search-service-subscription-ID}}/resourceGroups/{{search service-resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}/sharedPrivateLinkResources/{{shared-private-link-name}}?api-version=2024-06-01-preview --body @create-pe.json
+   az rest --method put --uri https://management.azure.com/subscriptions/{{search-service-subscription-ID}}/resourceGroups/{{search service-resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}/sharedPrivateLinkResources/{{shared-private-link-name}}?api-version=2025-05-01-preview --body @create-pe.json
    ```
 
    Provide the subscription ID, resource group name, and service name of your Azure AI Search resource.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure SQL管理インスタンスのプレビューAPIバージョンの更新"
}
```

### Explanation
この変更は、`articles/search/search-indexer-how-to-access-private-sql.md`ファイルの修正を示しており、Azure AI SearchがプライベートSQL管理インスタンスにアクセスする際のドキュメントが更新されています。具体的には、使用する管理REST APIのバージョンが変更されています。

元々、使用すべきAPIバージョンが「2024-06-01-preview」と指定されていましたが、最新のプレビューAPIバージョンとして「2025-05-01-preview」に更新されました。この変更により、ユーザーは新しい機能や改善点を持つ最新のAPIを利用することが推奨されることになります。

更新されたコマンドは、Azure CLIを使用して構成情報を設定する際の手順に関連しており、この変更によって、ユーザーは最新の仕様に従い、適切なAPIバージョンを使用することができます。全体として、この修正は、ユーザーが現在の技術仕様や導入方法に関して正確かつ最新の情報を得るために重要です。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -63,7 +63,7 @@ While both scenarios have a dependency on Azure Private Link, they're independen
 
 When evaluating shared private links for your scenario, remember these constraints.
 
-+ Several of the resource types used in a shared private link are in preview. If you're connecting to a preview resource (Azure Database for MySQL or Azure SQL Managed Instance), use a preview version of the Management REST API to create the shared private link. These versions include `2020-08-01-preview`, `2021-04-01-preview`, `2024-03-01-preview`, and `2024-06-01-preview`. We recommend the latest preview API.
++ Several of the resource types used in a shared private link are in preview. If you're connecting to a preview resource (Azure Database for MySQL or Azure SQL Managed Instance), use a preview version of the Management REST API to create the shared private link. These versions include `2020-08-01-preview`, `2021-04-01-preview`, `2024-03-01-preview`, `2024-06-01-preview`, and `2025-02-01-preview`. We recommend the latest preview API.
 
 + Indexer execution must use the [private execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment) that's specific to your search service. Private endpoint connections aren't supported from the multitenant content processing environment. The configuration setting for this requirement is covered in this article.
 
@@ -78,8 +78,8 @@ When evaluating shared private links for your scenario, remember these constrain
   | Workload | Tier requirements | Region requirements | Service creation requirements |
   |----------|-------------------|---------------------|---------------------|
   | Indexers without skillsets | Basic and higher | None | None |
-  | Skillsets with embedding skills ([integrated vectorization](vector-search-integrated-vectorization.md)) | Basic and higher | [High capacity regions](search-limits-quotas-capacity.md#partition-storage-gb) | [After April 3, 2024](vector-search-index-size.md#how-to-check-service-creation-date) |
-  | Skillsets using other [built-in](cognitive-search-predefined-skills.md) or custom skills | Standard 2 (S2) and higher | None | [After April 3, 2024](vector-search-index-size.md#how-to-check-service-creation-date) |
+  | Skillsets with embedding skills ([integrated vectorization](vector-search-integrated-vectorization.md)) | Basic and higher | [High capacity regions](search-limits-quotas-capacity.md#partition-storage-gb) | [After April 3, 2024](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date) |
+  | Skillsets using other [built-in](cognitive-search-predefined-skills.md) or custom skills | Standard 2 (S2) and higher | None | [After April 3, 2024](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date) |
 
 + Permissions on both Azure AI Search and the Azure resource:
 
@@ -88,9 +88,9 @@ When evaluating shared private links for your scenario, remember these constrain
   | Azure AI Search | `Microsoft.Search/searchServices/sharedPrivateLinkResources/write`<br> `Microsoft.Search/searchServices/sharedPrivateLinkResources/read`<br> `Microsoft.Search/searchServices/sharedPrivateLinkResources/operationStatuses/read` |
   | Other Azure resource | Permission to approve private endpoint connections. For example, on Azure Storage, you need `Microsoft.Storage/storageAccounts/privateEndpointConnectionsApproval/action`. |
 
-<!-- + For [integrated vectorization](vector-search-integrated-vectorization.md) only, outbound connections through shared private link are supported on all billable tiers, on services [created after April 3, 2024](vector-search-index-size.md#how-to-check-service-creation-date), in regions providing [higher capacity](search-limits-quotas-capacity.md#partition-storage-gb).  -->
+<!-- + For [integrated vectorization](vector-search-integrated-vectorization.md) only, outbound connections through shared private link are supported on all billable tiers, on services [created after April 3, 2024](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date), in regions providing [higher capacity](search-limits-quotas-capacity.md#partition-storage-gb).  -->
 
-<!-- + For [AI enrichment](cognitive-search-concept-intro.md) and skillset processing, shared private link  that doesn't include an embedding skill and in services [created before April 3, 2024](vector-search-index-size.md#how-to-check-service-creation-date), Azure AI Search must be Standard 2 (S2) or higher. -->
+<!-- + For [AI enrichment](cognitive-search-concept-intro.md) and skillset processing, shared private link  that doesn't include an embedding skill and in services [created before April 3, 2024](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date), Azure AI Search must be Standard 2 (S2) or higher. -->
 
 <!-- + For all other use cases, that don't involve skillsets, Azure AI Search can be Basic or higher. -->
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートSQLアクセスに関するドキュメントの更新"
}
```

### Explanation
この変更は、`articles/search/search-indexer-howto-access-private.md`ファイルの修正を示しており、プライベートSQLリソースへのアクセスに関する情報が更新されています。主に、プレビュー版のManagement REST APIのバージョンが最新のものに更新されることと、インデクサの実行環境に関する説明が強化されています。

具体的には、以前は使用すべきAPIバージョンが「2024-06-01-preview」までだったのが、新たに「2025-02-01-preview」が追加され、最新のAPIを推奨する内容になっています。この変更により、ユーザーは新しい機能や改善点を利用する準備ができるようになります。

また、インデクサの実行にはプライベート実行環境を使用する必要があることが強調され、マルチテナントのコンテンツ処理環境からの接続がサポートされないことが明確化されました。この情報は、プライベートリンクを評価する際に重要な要素であり、ユーザーの理解を深める助けとなります。

さらに、インデクサとスキルセットに関する要件や許可についての情報も更新され、特定の条件下におけるリソースの要求や制約が明示されています。これにより、ユーザーはAzure AI Searchにおけるプライベートリンクの使用方法とその制約をよりよく理解できるようになります。全体として、これらの修正はユーザーにとって、現在のAzureの技術スタックを最大限に活用するために非常に有益な情報を提供しています。

## articles/search/search-indexer-tutorial.md{#item-a3e3ff}

<details>
<summary>Diff</summary>
````diff
@@ -1,14 +1,14 @@
 ---
-title: C# tutorial indexing Azure SQL data
+title: 'C# Tutorial: Index Azure SQL Data'
 titleSuffix: Azure AI Search
-description: In this C# tutorial, connect to Azure SQL Database, extract searchable data, and load it into an Azure AI Search index.
+description: In this C# tutorial, you connect to Azure SQL Database, extract searchable data, and load it into an Azure AI Search index.
 
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 03/11/2025
+ms.date: 03/28/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
@@ -17,104 +17,101 @@ ms.custom:
 
 # Tutorial: Index Azure SQL data using the .NET SDK
 
-Configure an [indexer](search-indexer-overview.md) to extract searchable data from Azure SQL Database, sending it to a search index in Azure AI Search. 
+Learn how to configure an [indexer](search-indexer-overview.md) to extract searchable data from Azure SQL Database and send it to a search index in Azure AI Search.
 
-This tutorial uses C# and the [Azure SDK for .NET](/dotnet/api/overview/azure/search) to perform the following tasks:
+In this tutorial, you use C# and the [Azure SDK for .NET](/dotnet/api/overview/azure/search) to:
 
 > [!div class="checklist"]
 > * Create a data source that connects to Azure SQL Database
 > * Create an indexer
 > * Run an indexer to load data into an index
 > * Query an index as a verification step
 
-If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
-
 ## Prerequisites
 
-* [Azure SQL Database](https://azure.microsoft.com/services/sql-database/) using SQL Server authentication
-* [Visual Studio](https://visualstudio.microsoft.com/downloads/)
-* [Azure AI Search](search-what-is-azure-search.md). [Create](search-create-service-portal.md) or [find an existing search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) 
+* An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+* [Azure SQL Database](https://azure.microsoft.com/services/sql-database/) using SQL Server authentication.
+* [Azure AI Search](search-what-is-azure-search.md). [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription.
+* [Visual Studio](https://visualstudio.microsoft.com/downloads/).
 
 > [!NOTE]
-> You can use a free search service for this tutorial. The free tier limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before starting, make sure you have room on your service to accept the new resources.
+> You can use a free search service for this tutorial. The Free tier limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before you start, make sure you have room on your service to accept the new resources.
 
 ## Download files
 
 Source code for this tutorial is in the [DotNetHowToIndexer](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToIndexers) folder in the [Azure-Samples/search-dotnet-getting-started](https://github.com/Azure-Samples/search-dotnet-getting-started) GitHub repository.
 
-## 1 - Create services
+## Create services
 
-This tutorial uses Azure AI Search for indexing and queries, and Azure SQL Database as an external data source. If possible, create both services in the same region and resource group for proximity and manageability. In practice, Azure SQL Database can be in any region.
+This tutorial uses Azure AI Search for indexing and queries and Azure SQL Database as an external data source. If possible, create both services in the same region and resource group for proximity and manageability. In practice, Azure SQL Database can be in any region.
 
 ### Start with Azure SQL Database
 
-This tutorial provides *hotels.sql* file in the sample download to populate the database. Azure AI Search consumes flattened rowsets, such as one generated from a view or query. The SQL file in the sample solution creates and populates a single table.
-
-If you have an existing Azure SQL Database resource, you can add the hotels table to it, starting at the **Open query** step.
+This tutorial provides the *hotels.sql* file in the sample download to populate the database. Azure AI Search consumes flattened rowsets, such as one generated from a view or query. The SQL file in the sample solution creates and populates a single table.
 
-1. Create an Azure SQL database, using the instructions in [Quickstart: Create a single database](/azure/azure-sql/database/single-database-create-quickstart).
+If you have an existing Azure SQL Database resource, you can add the hotels table to it starting at the **Open query** step.
 
-   Server configuration for the database is important.
+1. [Create an Azure SQL database](/azure/azure-sql/database/single-database-create-quickstart). Server configuration for the database is important:
 
    * Choose the SQL Server authentication option that prompts you to specify a username and password. You need this for the ADO.NET connection string used by the indexer.
 
-   * Choose a public connection. It makes this tutorial easier to complete. Public isn't recommended for production and we recommend [deleting this resource](#clean-up-resources) at the end of the tutorial.
+   * Choose a public connection, which makes this tutorial easier to complete. Public isn't recommended for production, and we recommend [deleting this resource](#clean-up-resources) at the end of the tutorial.
 
    :::image type="content" source="media/search-indexer-tutorial/sql-server-config.png" alt-text="Screenshot of server configuration.":::
 
 1. In the Azure portal, go to the new resource.
 
-1. Add a firewall rule to allow access from your client, using the instructions in [Quickstart: Create a server-level firewall rule in Azure portal](/azure/azure-sql/database/firewall-create-server-level-portal-quickstart). You can run `ipconfig` from a command prompt to get your IP address. 
+1. [Add a firewall rule that allows access from your client](/azure/azure-sql/database/firewall-create-server-level-portal-quickstart). You can run `ipconfig` from a command prompt to get your IP address.
 
-1. Use the Query editor to load the sample data. On the navigation pane, select **Query editor (preview)** and enter the user name and password of server admin. 
+1. Use the Query editor to load the sample data. On the navigation pane, select **Query editor (preview)** and enter the username and password of the server admin.
 
-   If you get an access denied error, copy the client IP address from the error message, open the network security page for the server, and add an inbound rule that allows access from your client. 
+   If you get an access denied error, copy the client IP address from the error message, open the network security page for the server, and add an inbound rule that allows access from your client.
 
-1. In Query editor, select **Open query** and navigate to the location of *hotels.sql* file on your local computer. 
+1. In Query editor, select **Open query** and navigate to the location of *hotels.sql* file on your local computer.
 
 1. Select the file and select **Open**. The script should look similar to the following screenshot:
 
    :::image type="content" source="media/search-indexer-tutorial/sql-script.png" alt-text="Screenshot of SQL script in a Query Editor window." border="true":::
 
-1. Select **Run** to execute the query. In the Results pane, you should see a query succeeded message, for three rows.
+1. Select **Run** to execute the query. In the **Results** pane, you should see a query succeeded message for three rows.
 
 1. To return a rowset from this table, you can execute the following query as a verification step:
 
     ```sql
     SELECT * FROM Hotels
     ```
 
-1. Copy the ADO.NET connection string for the database. Under **Settings** > **Connection Strings**, copy the ADO.NET connection string, similar to the example below.
+1. Copy the ADO.NET connection string for the database. Under **Settings** > **Connection Strings**, copy the ADO.NET connection string, which should be similar to the following example:
 
     ```sql
     Server=tcp:<YOUR-DATABASE-NAME>.database.windows.net,1433;Initial Catalog=hotels-db;Persist Security Info=False;User ID=<YOUR-USER-NAME>;Password=<YOUR-PASSWORD>;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;
     ```
 
-You'll need this connection string in the next exercise, setting up your environment.
+You'll need this connection string to set up your environment in the next step.
 
 ### Azure AI Search
 
-The next component is Azure AI Search, which you can [create in the Azure portal](search-create-service-portal.md). You can use the Free tier to complete this walkthrough. 
+The next component is Azure AI Search, which you can [create in the Azure portal](search-create-service-portal.md). You can use the Free tier to complete this tutorial.
 
-### Get an admin api-key and URL for Azure AI Search
+### Get an admin key and URL for Azure AI Search
 
 API calls require the service URL and an access key. A search service is created with both, so if you added Azure AI Search to your subscription, follow these steps to get the necessary information:
 
-1. Sign in to the [Azure portal](https://portal.azure.com), and in your search service **Overview** page, get the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
+1. Sign in to the [Azure portal](https://portal.azure.com). On your service **Overview** page, copy the endpoint URL. An example endpoint might look like `https://mydemo.search.windows.net`.
 
-1. In **Settings** > **Keys**, get an admin key for full rights on the service. There are two interchangeable admin keys, provided for business continuity in case you need to roll one over. You can use either the primary or secondary key on requests for adding, modifying, and deleting objects.
+1. On **Settings** > **Keys**, get an admin key for full rights on the service. There are two interchangeable admin keys, provided for business continuity in case you need to roll one over. You can use either the primary or secondary key on requests for adding, modifying, and deleting objects.
 
    :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of Azure portal pages showing the HTTP endpoint and access key location for a search service." border="false":::
 
-## 2 - Set up your environment
+## Set up your environment
 
-1. Start Visual Studio and open **DotNetHowToIndexers.sln**.
+1. Start Visual Studio and open *DotNetHowToIndexers.sln*.
 
-1. In Solution Explorer, open **appsettings.json** to provide connection information.
+1. In Solution Explorer, open *appsettings.json* to provide connection information.
 
-1. For `SearchServiceEndPoint`, if the full URL on the service overview page is "https://my-demo-service.search.windows.net", then the value to provide is the entire URL.
+1. For `SearchServiceEndPoint`, if the full URL on your service **Overview** page is `https://my-demo-service.search.windows.net`, provide the entire URL.
 
-1. For `AzureSqlConnectionString`, the string format is similar to this: `"Server=tcp:<your-database-name>.database.windows.net,1433;Initial Catalog=hotels-db;Persist Security Info=False;User ID=<your-user-name>;Password=<your-password>;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"`
+1. For `AzureSqlConnectionString`, the string format is similar to `"Server=tcp:<your-database-name>.database.windows.net,1433;Initial Catalog=hotels-db;Persist Security Info=False;User ID=<your-user-name>;Password=<your-password>;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"`.
 
     ```json
     {
@@ -124,19 +121,18 @@ API calls require the service URL and an access key. A search service is created
     }
     ```
 
-1. Replace the user password in the SQL connection string to a valid password. While the database and user names will copy over, the password must be entered manually.
-
-## 3 - Create the pipeline
+1. Replace the user password in the SQL connection string with a valid password. While the database and usernames will copy over, you must enter the password manually.
 
-Indexers require a data source object and an index. Relevant code is in two files:
+## Create the pipeline
 
-* **hotel.cs**, containing a schema that defines the index
+Indexers require a data source object and an index. The relevant code is in two files:
 
-* **Program.cs**, containing functions for creating and managing structures in your service
+* *hotel.cs* contains a schema that defines the index
+* *Program.cs* contains functions for creating and managing structures in your service
 
 ### In hotel.cs
 
-The index schema defines the fields collection, including attributes specifying allowed operations, such as whether a field is full-text searchable, filterable, or sortable as shown in the following field definition for HotelName. A [SearchableField](/dotnet/api/azure.search.documents.indexes.models.searchablefield) is full-text searchable by definition. Other attributes are assigned explicitly.
+The index schema defines the fields collection, including attributes specifying allowed operations, such as whether a field is full-text searchable, filterable, or sortable, as shown in the following field definition for `HotelName`. A [SearchableField](/dotnet/api/azure.search.documents.indexes.models.searchablefield) is, by definition, full-text searchable. Other attributes are explicitly assigned.
 
 ```csharp
 . . . 
@@ -146,11 +142,11 @@ public string HotelName { get; set; }
 . . .
 ```
 
-A schema can also include other elements, including scoring profiles for boosting a search score, custom analyzers, and other constructs. However, for our purposes, the schema is sparsely defined, consisting only of fields found in the sample datasets.
+A schema can also include other elements, such as scoring profiles for boosting a search score and custom analyzers. However, for this tutorial, the schema is sparsely defined, consisting only of fields found in the sample datasets.
 
 ### In Program.cs
 
-The main program includes logic for creating [an indexer client](/dotnet/api/azure.search.documents.indexes.models.searchindexer), an index, a data source, and an indexer. The code checks for and deletes existing resources of the same name, under the assumption that you might run this program multiple times.
+The main program includes logic for creating [an indexer client](/dotnet/api/azure.search.documents.indexes.models.searchindexer), an index, a data source, and an indexer. The code checks for and deletes existing resources of the same name, assuming that you might run this program multiple times.
 
 The data source object is configured with settings that are specific to Azure SQL Database resources, including [partial or incremental indexing](search-how-to-index-sql-database.md#CaptureChangedRows) for using the built-in [change detection features](/sql/relational-databases/track-changes/about-change-tracking-sql-server) of Azure SQL. The source demo hotels database in Azure SQL has a "soft delete" column named **IsDeleted**. When this column is set to true in the database, the indexer removes the corresponding document from the Azure AI Search index.
 
@@ -167,7 +163,7 @@ var dataSource =
 indexerClient.CreateOrUpdateDataSourceConnection(dataSource);
 ```
 
-An indexer object is platform-agnostic, where  configuration, scheduling, and invocation are the same regardless of the source. This example indexer includes a schedule, a reset option that clears indexer history, and calls a method to create and run the indexer immediately. To create or update an indexer, use [CreateOrUpdateIndexerAsync](/dotnet/api/azure.search.documents.indexes.searchindexerclient.createorupdateindexerasync).
+An indexer object is platform agnostic, where configuration, scheduling, and invocation are the same regardless of the source. This example indexer includes a schedule and a reset option that clears the indexer history. It also calls a method to create and run the indexer immediately. To create or update an indexer, use [CreateOrUpdateIndexerAsync](/dotnet/api/azure.search.documents.indexes.searchindexerclient.createorupdateindexerasync).
 
 ```csharp
 Console.WriteLine("Creating Azure SQL indexer...");
@@ -203,7 +199,7 @@ var indexer = new SearchIndexer("hotels-sql-idxr", dataSource.Name, searchIndex.
 await indexerClient.CreateOrUpdateIndexerAsync(indexer);
 ```
 
-Indexer runs are usually scheduled, but during development you might want to run the indexer immediately using [RunIndexerAsync](/dotnet/api/azure.search.documents.indexes.searchindexerclient.runindexerasync).
+Indexer runs are usually scheduled, but during development, you might want to run the indexer immediately using [RunIndexerAsync](/dotnet/api/azure.search.documents.indexes.searchindexerclient.runindexerasync).
 
 ```csharp
 Console.WriteLine("Running Azure SQL indexer...");
@@ -218,35 +214,35 @@ catch (RequestFailedException ex) when (ex.Status == 429)
 }
 ```
 
-## 4 - Build the solution
+## Build the solution
 
-Press F5 to build and run the solution. The program executes in debug mode. A console window reports the status of each operation.
+Select **F5** to build and run the solution. The program executes in debug mode. A console window reports the status of each operation.
 
    :::image type="content" source="media/search-indexer-tutorial/console-output.png" alt-text="Screenshot showing the console output for the program." border="true":::
 
 Your code runs locally in Visual Studio, connecting to your search service on Azure, which in turn connects to Azure SQL Database and retrieves the dataset. With this many operations, there are several potential points of failure. If you get an error, check the following conditions first:
 
-* Search service connection information that you provide is the full URL. If you entered just the service name, operations stop at index creation, with a failure to connect error.
+* Search service connection information that you provide is the full URL. If you only entered the service name, operations stop at index creation, with a failure to connect error.
 
-* Database connection information in **appsettings.json**. It should be the ADO.NET connection string obtained from the Azure portal, modified to include a username and password that are valid for your database. The user account must have permission to retrieve data. Your local client IP address must be allowed inbound access through the firewall.
+* Database connection information in *appsettings.json*. It should be the ADO.NET connection string obtained from the Azure portal, modified to include a username and password that are valid for your database. The user account must have permission to retrieve data. Your local client IP address must be allowed inbound access through the firewall.
 
 * Resource limits. Recall that the Free tier has limits of three indexes, indexers, and data sources. A service at the maximum limit can't create new objects.
 
-## 5 - Search
+## Search
 
-Use Azure portal to verify object creation, and then use **Search explorer** to query the index.
+Use the Azure portal to verify object creation, and then use **Search explorer** to query the index.
 
-1. Sign in to the [Azure portal](https://portal.azure.com), and in your search service left pane, open each page in turn to verify the object is created. **Indexes**, **Indexers**, and **Data Sources** will have "hotels-sql-idx", "hotels-sql-indexer", and "hotels-sql-ds", respectively.
+1. Sign in to the [Azure portal](https://portal.azure.com) and go to your search service. From the left pane, open each page to verify the objects are created. **Indexes**, **Indexers**, and **Data Sources** should have **hotels-sql-idx**, **hotels-sql-indexer**, and **hotels-sql-ds**, respectively.
 
-1. On the Indexes tab, select the hotels-sql-idx index. On the hotels page, **Search explorer** is the first tab.
+1. On the **Indexes** tab, select the **hotels-sql-idx** index. On the hotels page, **Search explorer** is the first tab.
 
 1. Select **Search** to issue an empty query.
 
    The three entries in your index are returned as JSON documents. Search explorer returns documents in JSON so that you can view the entire structure.
 
    :::image type="content" source="media/search-indexer-tutorial/portal-search.png" alt-text="Screenshot of a Search Explorer query for the target index." border="true":::
 
-1. Next, [switch to **JSON View**](search-explorer.md#start-search-explorer) so that you can enter query parameters:
+1. [Switch to **JSON view**](search-explorer.md#start-search-explorer) so that you can enter query parameters.
 
    ```json
    {
@@ -255,9 +251,9 @@ Use Azure portal to verify object creation, and then use **Search explorer** to
    }
    ```
 
-   This query invokes full text search on the term `river`, and the result includes a count of the matching documents. Returning the count of matching documents is helpful in testing scenarios when you have a large index with thousands or millions of documents. In this case, only one document matches the query.
+   This query invokes full text search on the term `river`. The result includes a count of the matching documents. Returning the count of matching documents is helpful in testing scenarios where you have a large index with thousands or millions of documents. In this case, only one document matches the query.
 
-1. Lastly, enter parameters that limit search results to fields of interest: 
+1. Enter parameters that limit search results to fields of interest.
 
    ```json
    {
@@ -285,7 +281,7 @@ You can find and manage resources in the Azure portal, using the All resources o
 
 ## Next steps
 
-Now that you're familiar with the basics of SQL Database indexing, let's take a closer look at indexer configuration.
+Now that you're familiar with the basics of SQL Database indexing, take a closer look at indexer configuration:
 
 > [!div class="nextstepaction"]
 > [Configure a SQL Database indexer](search-how-to-index-sql-database.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#チュートリアル：Azure SQLデータのインデクシング"
}
```

### Explanation
この変更は、`articles/search/search-indexer-tutorial.md`ファイルの修正を示しており、C#を使用してAzure SQLデータをインデクシングするためのチュートリアルが更新されています。主な変更点は、タイトルや説明の言葉遣いの改善、構造の整理、新しい情報の追加などによる内容の明確化です。

具体的には、チュートリアルのタイトルがよりわかりやすく変更され、内容も読みやすくなるようにいくつかの文章がリフレーズされています。また、前提条件やサービスを作成する手順が明確にリスト化され、段階を追って理解しやすくなっています。

特に、Azure SQL Databaseのファイアウォールルールを設定する方法や、データベースへの接続文字列の設定についての指示が整理され、重要なポイントが強調されました。さらに、プログラムの主要な操作やエラーハンドリングに関する情報も更新され、ユーザーが直面する可能性のある問題に対する解決策が示されています。

この更新により、ユーザーはAzure AI SearchとAzure SQL Databaseの連携をより効果的に理解し、実装できるようになります。また、特定の手順や注意点が明確化されているため、初心者にも優しい内容となっています。全体として、この修正はチュートリアルの質と可読性を向上させ、ユーザーの学習体験を豊かにするものです。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 03/11/2025
+ms.date: 04/09/2025
 ms.custom:
   - references_regions
   - build-2024
@@ -47,6 +47,7 @@ Maximum limits on storage, workloads, and quantities of indexes and other object
 | Maximum depth of complex fields |10 |10 |10 |10 |10 |10 |10 |10 |
 | Maximum [suggesters](/rest/api/searchservice/suggesters) per index |1 |1 |1 |1 |1 |1 |1 |1 |
 | Maximum [scoring profiles](/rest/api/searchservice/add-scoring-profiles-to-a-search-index) per index |100 |100 |100 |100 |100 |100 |100 |100 |
+| Maximum [semantic configurations](semantic-how-to-configure.md) per index |100 |100 |100 |100 |100 |100 |100 |100 |
 | Maximum functions per profile |8 |8 |8 |8 |8 |8 |8 |8 |
 | Maximum index size&nbsp;<sup>4</sup> | N/A | N/A | N/A | 1.88&nbsp;TB | 2.34&nbsp;TB | 100 GB| N/A | N/A |
 
@@ -56,7 +57,7 @@ Maximum limits on storage, workloads, and quantities of indexes and other object
 
 <sup>3</sup> An upper limit exists for elements because having a large number of them significantly increases the storage required for your index. An element of a complex collection is defined as a member of that collection. For example, assume a [Hotel document with a Rooms complex collection](search-howto-complex-data-types.md#complex-collection-limits), each room in the Rooms collection is considered an element. During indexing, the indexing engine can safely process a maximum of 3,000 elements across the document as a whole. [This limit](search-api-migration.md#upgrade-to-2019-05-06) was introduced in `api-version=2019-05-06` and applies to complex collections only, and not to string collections or to complex fields.
 
-<sup>4</sup> On most tiers, maximum index size is all available storage on your search service. For S2, S3, and S3 HD, the maximum size of any index is the number provided in the table. Applies to search services created after April 3, 2024.
+<sup>4</sup> For most tiers, the maximum index size is the total available storage on your search service. For S2, S3, and S3 HD services with multiple partitions, and therefore more storage, the maximum size of a single index is provided in the table. Applies to search services created after April 3, 2024.
 
 You might find some variation in maximum limits if your service happens to be provisioned on a more powerful cluster. The limits here represent the common denominator. Indexes built to the above specifications are portable across equivalent service tiers in any region.
 
@@ -81,12 +82,12 @@ When you index documents with vector fields, Azure AI Search constructs internal
 
 Vector limits vary by:
 
-+ [service creation date](vector-search-index-size.md#how-to-check-service-creation-date)
-+ [region](search-region-support.md)
++ [Service creation date](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date)
++ [Region](search-region-support.md)
 
-Higher vector limits from April 2024 onwards exist on *new search services* in regions providing the extra capacity, which is most of them.
+Higher vector limits from April 2024 onwards exist on *new search services* in regions providing the extra capacity, which is most of them. If you have an older service in a supported region, check if you can [upgrade your service](search-how-to-upgrade.md) to the higher vector limits.
 
-This table shows the progression of vector quota increases in GB over time. The quota is per partition, so if you scale a new Standard (S1) service to 6 partitions, total vector quota is 35 multiplied by 6.
+This table shows the progression of vector quota increases in GB over time. The quota is per partition, so if you scale a new Standard (S1) service to 6 partitions, the total vector quota is 35 multiplied by 6.
 
 | Service creation date |Basic | S1| S2 | S3/HD | L1 | L2 |
 |-----------------------|------|---|----|----|----|----|
@@ -150,9 +151,9 @@ Indexers can access other Azure resources [over private endpoints](search-indexe
 | Maximum private endpoints | N/A | 10 or 30 | 100 | 400 | 400 | N/A | 20 | 20 |
 | Maximum distinct resource types <sup>3</sup> | N/A | 4 | 7 | 15 | 15 | N/A | 4 | 4 |
 
-<sup>1</sup> AI enrichment and image analysis are computationally intensive and consume disproportionate amounts of available processing power. For this reason, private connections are disabled on lower tiers to ensure the performance and stability of the search service itself. On basic services, private connections to an Azure AI services multi-service resource are unsupported to preserve service stability. For the S1 tier, make sure the service was created with [higher limits](search-limits-quotas-capacity.md#partition-storage-gb) after April 3, 2024. 
+<sup>1</sup> AI enrichment and image analysis are computationally intensive and consume disproportionate amounts of available processing power. For this reason, private connections are disabled on lower tiers to ensure the performance and stability of the search service itself. On Basic services, private connections to an Azure AI services multi-service resource are unsupported to preserve service stability. For the S1 tier, make sure the service was created with [higher limits](search-limits-quotas-capacity.md#partition-storage-gb) after April 3, 2024.
 
-<sup>2</sup> Private connections to an embedding model are supported on basic and S1 high-capacity search services created after April 3, 2024, with the [higher limits](search-limits-quotas-capacity.md#partition-storage-gb) for storage and computational processing. 
+<sup>2</sup> Private connections to an embedding model are supported on Basic and S1 high-capacity search services created after April 3, 2024, with the [higher limits](search-limits-quotas-capacity.md#partition-storage-gb) for storage and computational processing.
 
 <sup>3</sup> The number of distinct resource types are computed as the number of unique `groupId` values used across all shared private link resources for a given search service, irrespective of the status of the resource.
 
@@ -167,7 +168,7 @@ Maximum number of synonym maps varies by tier. Each rule can have up to 20 expan
 
 ## Index alias limits
 
-Maximum number of [index aliases](search-how-to-alias.md) varies by tier and [service creation date](vector-search-index-size.md#how-to-check-service-creation-date). In all tiers, if the service was created after October 2022 the maximum number of aliases is double the maximum number of indexes allowed. If the service was created before October 2022, the limit is the number of indexes allowed.
+Maximum number of [index aliases](search-how-to-alias.md) varies by tier and [service creation date](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date). In all tiers, if the service was created after October 2022 the maximum number of aliases is double the maximum number of indexes allowed. If the service was created before October 2022, the limit is the number of indexes allowed.
 
 | Service Creation Date | Free | Basic | S1 | S2 | S3 | S3-HD |L1 | L2 |
 |----------|------|-------|----|----|----|-------|----|----|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索サービスの制限および容量に関するドキュメントの更新"
}
```

### Explanation
この変更は、`articles/search/search-limits-quotas-capacity.md`ファイルの修正を示しており、Azure AI Searchの制限および容量に関する最新情報が反映されています。主な変更点は、制限に関するデータの追加や調整であり、特にセマンティック設定や複雑なフィールドの上限に関する新しい情報が追加されています。

具体的には、各インデックスに対するセマンティック設定の最大数（100）が新たに追加され、それに伴い全体の制限に関する情報が更新されました。また、インデックスサイズに関する説明が明確化されており、特定のサービスプランにおけるストレージの最大サイズについて詳細が追加されています。

さらに、ベクター制限やプライベート接続に関する条件についても更新され、これによりサービスの最大限度がどのように地域や作成日によって影響されるかが示されています。具体的には、古いサービスのユーザーが新しい制限にアップグレード可能かどうかの情報も提供されており、ユーザーは自分の環境のニーズに応じた適切な決定を下すことができます。

これらの修正により、ユーザーは最新の制限やベストプラクティスに基づいて、Azure AI Searchを効果的に活用することができるようになり、インデクシングや検索操作のパフォーマンスを向上させることが期待されます。全体的に、これらのアップデートは実用的で重要な情報を提供し、ユーザーの理解を深める役割を果たします。

## articles/search/search-manage-azure-cli.md{#item-7fdd08}

<details>
<summary>Diff</summary>
````diff
@@ -11,15 +11,10 @@ ms.custom:
   - devx-track-azurecli
   - ignite-2023
 ms.topic: how-to
-ms.date: 12/10/2024
+ms.date: 03/21/2025
 ---
 
-# Manage your Azure AI Search service with the Azure CLI
-> [!div class="op_single_selector"]
-> * [Portal](search-manage.md)
-> * [PowerShell](search-manage-powershell.md)
-> * [Azure CLI](search-manage-azure-cli.md)
-> * [REST API](search-manage-rest.md)
+# Manage your Azure AI Search service using the Azure CLI
 
 You can run Azure CLI commands and scripts on Windows, macOS, Linux, or in Azure Cloud Shell to create and configure Azure AI Search.
 
@@ -37,7 +32,10 @@ Use the [**az search module**](/cli/azure/search) to perform the following tasks
 
 Occasionally, questions are asked about tasks *not* on the above list.
 
-You can't change a server name, region, or tier programmatically or in the Azure portal. Dedicated resources are allocated when a service is created. As such, changing the underlying hardware (location or node type) requires a new service. 
+You can't change a service name, region, or tier programmatically or in the Azure portal. Dedicated resources are allocated when a service is created. As such, changing the underlying hardware (location or node type) requires a new service.
+
+> [!NOTE]
+> The 2025-02-01-preview supports changing your pricing tier using the [Management REST APIs](search-manage-rest.md#upgrade-a-service) and the [Azure portal](search-capacity-planning.md#change-your-pricing-tier). Currently, you can only move up between Basic and Standard (S1, S2, and S3) tiers, such as going from Basic to S1.
 
 You can't use tools or APIs to transfer content, such as an index, from one service to another. Within a service, programmatic creation of content is through [Search Service REST API](/rest/api/searchservice/) or an SDK such as [Azure SDK for .NET](/dotnet/api/overview/azure/search.documents-readme). While there are no dedicated commands for content migration, you can write script that calls REST API or a client library to create and load indexes on a new service.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure CLIを使用したAzure AI Searchサービスの管理"
}
```

### Explanation
この変更は、`articles/search/search-manage-azure-cli.md`ファイルの修正を示しており、Azure CLIを使用してAzure AI Searchサービスを管理する方法に関する情報が更新されています。主な変更点は、タイトルの文言が改善され、内容が明確化されたことです。

具体的には、ドキュメントのタイトルが「Azure AI SearchサービスをAzure CLIを使用して管理する」という形に変更され、より具体的で明確な表現になっています。また、日付が2024年12月10日から2025年3月21日へと更新され、新しい情報が反映されていることを示しています。

本文中では、サービス名、地域、またはティアをプログラム的に変更できないことに関する説明が明確にされ、専用リソースの割り当てについての情報が統一された形で提供されています。さらに、2025年2月1日以降のプレビュー版では、管理REST APIやAzureポータルを使用して料金プランを変更できることが注記され、利用可能なティアの変更に関する詳細が追加されました。

このように、ノートとして追加された情報により、価格プランの変更方法についての透明性が向上し、ユーザーはより効果的にサービスを管理できるようになります。また、コンテンツの移行に関する制限と、それを克服するためのアプローチについても言及されており、ユーザーに対する有用なガイダンスが提供されています。

全体として、この更新により、Azure CLIを用いたAzure AI Searchサービスの管理に関する情報がより明確で利用しやすくなり、ユーザーの理解と運用が向上することが期待されます。

## articles/search/search-manage-powershell.md{#item-3c3485}

<details>
<summary>Diff</summary>
````diff
@@ -9,20 +9,15 @@ ms.author: haileytapia
 ms.service: azure-ai-search
 ms.devlang: powershell
 ms.topic: how-to
-ms.date: 12/10/2024
+ms.date: 03/21/2025
 ms.custom:
   - devx-track-azurepowershell
   - ignite-2023
 ---
 
-# Manage your Azure AI Search service with PowerShell
-> [!div class="op_single_selector"]
-> * [Portal](search-manage.md)
-> * [PowerShell](search-manage-powershell.md)
-> * [Azure CLI](search-manage-azure-cli.md)
-> * [REST API](search-manage-rest.md)
+# Manage your Azure AI Search service using PowerShell
 
-You can run PowerShell cmdlets and scripts on Windows, Linux, or in Azure Cloud Shell to create and configure Azure AI Search. 
+You can run PowerShell cmdlets and scripts on Windows, Linux, or in Azure Cloud Shell to create and configure Azure AI Search.
 
 Use the [**Az.Search** module](/powershell/module/az.search/) to perform the following tasks:
 
@@ -38,7 +33,10 @@ Use the [**Az.Search** module](/powershell/module/az.search/) to perform the fol
 
 Occasionally, questions are asked about tasks *not* on the above list.
 
-You can't change a server name, region, or tier programmatically or in the Azure portal. Dedicated resources are allocated when a service is created. As such, changing the underlying hardware (location or node type) requires a new service. 
+You can't change a service name, region, or tier programmatically or in the Azure portal. Dedicated resources are allocated when a service is created. As such, changing the underlying hardware (location or node type) requires a new service.
+
+> [!NOTE]
+> The 2025-02-01-preview supports changing your pricing tier using the [Management REST APIs](search-manage-rest.md#upgrade-a-service) and the [Azure portal](search-capacity-planning.md#change-your-pricing-tier). Currently, you can only move up between Basic and Standard (S1, S2, and S3) tiers, such as going from Basic to S1.
 
 You can't use tools or APIs to transfer content, such as an index, from one service to another. Within a service, programmatic creation of content is through [Search Service REST API](/rest/api/searchservice/) or an SDK such as [Azure SDK for .NET](/dotnet/api/overview/azure/search.documents-readme). While there are no dedicated commands for content migration, you can write script that calls REST API or a client library to create and load indexes on a new service.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PowerShellを使用したAzure AI Searchサービスの管理"
}
```

### Explanation
この変更は、`articles/search/search-manage-powershell.md`ファイルの修正を示しており、PowerShellを使用してAzure AI Searchサービスを管理する方法に関する情報が更新されています。主な変更ポイントは、タイトルの表現が改善され、情報の一部が最新の内容に更新されたことです。

具体的には、ドキュメントのタイトルが「PowerShellを使用したAzure AI Searchサービスの管理」に変更され、よりわかりやすくなっています。また、日付が2024年12月10日から2025年3月21日へと更新され、最新情報の反映がなされています。

本文の内容では、サーバー名、地域、またはティアをプログラム的に変更できないことに関する説明が強調され、必要な専用リソースの割り当てについての情報が統一された形で示されています。さらに、新たにノートとして追加された部分により、2025年2月1日以降のプレビュー版では管理REST APIやAzureポータルを使用して料金プランを変更できる旨の情報も提供され、ユーザーはアップグレードの選択肢について知ることができるようになります。

また、コンテンツの移行についての制限に関する記述も引き続き含まれ、ユーザーが必要に応じて、REST APIやクライアントライブラリを使用してインデックスを作成・読み込むためのスクリプトを書くことができる旨が説明されています。

全体として、この更新によりPowerShellを用いたAzure AI Searchサービスの管理に関する情報がより明確で利用しやすくなり、ユーザーの理解を深め、運用の効率性を向上させることが期待されます。

## articles/search/search-manage-rest.md{#item-405ec7}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Manage with REST
+title: Manage using REST
 titleSuffix: Azure AI Search
 description: Create and configure an Azure AI Search service with the Management REST API. The Management REST API is comprehensive in scope, with access to generally available and preview features.
 author: haileytap
@@ -8,23 +8,19 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 12/10/2024
+ms.date: 03/26/2025
 ---
 
-# Manage your Azure AI Search service with REST APIs
+# Manage your Azure AI Search service using REST APIs
 
-> [!div class="op_single_selector"]
-> * [Portal](search-manage.md)
-> * [PowerShell](search-manage-powershell.md)
-> * [Azure CLI](search-manage-azure-cli.md)
-> * [REST API](search-manage-rest.md)
-
-In this article, learn how to create and configure an Azure AI Search service using the [Management REST APIs](/rest/api/searchmanagement/). Only the Management REST APIs are guaranteed to provide early access to [preview features](/rest/api/searchmanagement/management-api-versions). 
+Learn how to create and configure an Azure AI Search service using the [Management REST APIs](/rest/api/searchmanagement/). Only the Management REST APIs are guaranteed to provide early access to [preview features](/rest/api/searchmanagement/management-api-versions).
 
 The Management REST API is available in stable and preview versions. Be sure to set a preview API version if you're accessing preview features.
 
 > [!div class="checklist"]
 > * [Create or update a service](#create-or-update-a-service)
+> * [Upgrade a service](#upgrade-a-service)
+> * [Change pricing tiers](#change-pricing-tiers)
 > * [Enable Azure role-based access control for data plane](#enable-rbac)
 > * [Enforce a customer-managed key policy](#enforce-cmk)
 > * [Disable semantic ranker](#disable-semantic-ranker)
@@ -33,49 +29,45 @@ The Management REST API is available in stable and preview versions. Be sure to
 > * [Regenerate an admin key](#regenerate-admin-api-keys)
 > * [List private endpoint connections](#list-private-endpoint-connections)
 > * [List search operations](#list-search-operations)
-> * [Delete a search services](#delete-a-search-service)
+> * [Delete a search service](#delete-a-search-service)
 
 All of the Management REST APIs have examples. If a task isn't covered in this article, see the [API reference](/rest/api/searchmanagement/) instead.
 
 ## Prerequisites
 
-* An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-search/).
+* An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
 * [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
-* [Azure CLI](/cli/azure/install-azure-cli) used to get an access token. You must be an owner or administrator in your Azure subscription.
-
-## Get an access token
+* [Azure CLI](/cli/azure/install-azure-cli) to get an access token, as described in the following steps. You must be an owner or administrator in your Azure subscription.
 
-Management REST API calls are authenticated through Microsoft Entra ID. You need to provide an access token on the request, along with permissions to create and configure a resource.
+   Management REST API calls are authenticated through Microsoft Entra ID. You must provide an access token on the request and permissions to create and configure a resource. In addition to the Azure CLI, you can use [Azure PowerShell to create an access token](/azure/azure-resource-manager/management/manage-resources-rest).
 
-You can use the [Azure CLI or Azure PowerShell to create an access token](/azure/azure-resource-manager/management/manage-resources-rest).
+   1. Open a command shell for Azure CLI.
 
-1. Open a command shell for Azure CLI.
+   1. Sign in to your Azure subscription. If you have multiple tenants or subscriptions, make sure you select the correct one.
 
-1. Sign in to your Azure subscription.
+       ```azurecli
+       az login
+       ```
 
-   ```azurecli
-   az login
-   ```
+   1. Get the tenant ID and subscription ID.
 
-1. Get the tenant ID and subscription ID. If you have multiple tenants or subscriptions, make sure you use the correct one.
+      ```azurecli
+      az account show
+      ```
 
-   ```azurecli
-   az account show
-   ````
+   1. Get an access token.
 
-1. Get an access token.
+      ```azurecli
+      az account get-access-token --query accessToken --output tsv
+      ```
 
-   ```azurecli
-   az account get-access-token --query accessToken --output tsv
-   ```
-
-You should have a tenant ID, subscription ID, and bearer token. You'll paste these values into the `.rest` or `.http` file that you create in the next step.
+      You should have a tenant ID, subscription ID, and bearer token. You'll paste these values into the `.rest` or `.http` file that you create in the next step.
 
 ## Set up Visual Studio Code
 
-If you're not familiar with the REST client for Visual Studio Code, this section includes setup so that you can complete the tasks in this quickstart.
+If you're not familiar with the REST client for Visual Studio Code, this section includes setup so that you can complete the tasks in this article.
 
 1. Start Visual Studio Code and select the **Extensions** tile.
 
@@ -129,7 +121,7 @@ If you're not familiar with the REST client for Visual Studio Code, this section
 
 ## Create or update a service
 
-Creates or updates a search service under the current subscription. This example uses variables for the search service name and region, which haven't been defined yet. Either provide the names directly, or add new variables to the collection.
+Creates or updates a search service under the current subscription. This example uses variables for the search service name and region, which haven't been defined yet. Either provide the names directly or add new variables to the collection.
 
 ```http
 ### Create a search service (provide an existing resource group)
@@ -152,6 +144,38 @@ PUT https://management.azure.com/subscriptions/{{subscriptionId}}/resourceGroups
       }
 ```
 
+## Upgrade a service
+
+Some Azure AI Search capabilities are only available to new services. To avoid service recreation and bring these capabilities to an existing service, you can [upgrade your service](search-how-to-upgrade.md).
+
+```http
+### Upgrade a search service
+@resource-group = my-rg
+@search-service-name = my-search
+POST https://management.azure.com/subscriptions/{{subscriptionId}}/resourceGroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}/upgrade?api-version=2025-02-01-preview  HTTP/1.1
+     Content-type: application/json
+     Authorization: Bearer {{token}}
+```
+
+## Change pricing tiers
+
+If you need more <!-- or less-->capacity, you can [switch to a higher pricing tier](search-capacity-planning.md#change-your-pricing-tier). Currently, you can only move up between Basic and Standard (S1, S2, and S3) tiers. Use the `sku` property to specify the higher <!-- your new -->tier.
+
+```http
+### Change pricing tiers
+@resource-group = my-rg
+@search-service-name = my-search
+PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourceGroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2025-02-01-preview HTTP/1.1
+     Content-type: application/json
+     Authorization: Bearer {{token}}
+
+    {
+        "sku": {
+            "name": "standard2"
+        }
+    }
+```
+
 ## Create an S3HD service
 
 To create an [S3HD](search-sku-tier.md#tier-descriptions) service, use a combination of `sku` and `hostingMode` properties. Set `sku` to `standard3` and "hostingMode" to `HighDensity`.
@@ -182,7 +206,7 @@ PUT https://management.azure.com/subscriptions/{{subscriptionId}}/resourceGroups
 
 **Applies to:** Search Index Data Contributor, Search Index Data Reader, Search Service Contributor
 
-In this step, configure your search service to recognize an **authorization** header on data requests that provide an OAuth2 access token.
+Configure your search service to recognize an **authorization** header on data requests that provide an OAuth2 access token.
 
 To use role-based access control for data plane operations, set `authOptions` to `aadOrApiKey` and then send the request.
 
@@ -232,7 +256,7 @@ PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegrou
 [Semantic ranker is enabled](semantic-how-to-enable-disable.md) by default at the free plan that allows up to 1,000 requests per month at no charge. You can lock down the feature at the service level to prevent usage.
 
 ```http
-### disable semantic ranker
+### Disable semantic ranker
 PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2023-11-01 HTTP/1.1
      Content-type: application/json
      Authorization: Bearer {{token}}
@@ -251,7 +275,7 @@ PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegrou
 Azure AI Search [writes to external data sources](search-indexer-securing-resources.md) when updating a knowledge store, saving debug session state, or caching enrichments. The following example disables these workloads at the service level.
 
 ```http
-### disable-external-access
+### Disable external access
 PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2023-11-01 HTTP/1.1
      Content-type: application/json
      Authorization: Bearer {{token}}
@@ -266,7 +290,7 @@ PATCH https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegrou
 ## Delete a search service
 
 ```http
-### delete a search service
+### Delete a search service
 DELETE https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegroups/{{resource-group}}/providers/Microsoft.Search/searchServices/{{search-service-name}}?api-version=2023-11-01 HTTP/1.1
      Content-type: application/json
      Authorization: Bearer {{token}}
@@ -321,7 +345,7 @@ GET https://management.azure.com/subscriptions/{{subscriptionId}}/resourcegroups
 
 ## Next steps
 
-After a search service is configured, next steps include [create an index](search-how-to-create-search-index.md) or [query an index](search-query-overview.md) using the Azure portal, REST APIs, or an Azure SDK.
+After a search service is configured, your next steps include [creating an index](search-how-to-create-search-index.md) or [querying an index](search-query-overview.md) using the Azure portal, REST APIs, or an Azure SDK.
 
 * [Create an Azure AI Search index in the Azure portal](search-get-started-portal.md)
 * [Set up an indexer to load data from other services](search-indexer-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIを使用したAzure AI Searchサービスの管理"
}
```

### Explanation
この変更は、`articles/search/search-manage-rest.md`ファイルに対する修正を示しており、REST APIを使用してAzure AI Searchサービスを管理するための内容が大幅に更新されています。主な変更点として、ファイルのタイトル、日付、内容が変更され、情報が最新化され、実用性が向上しています。

具体的な更新内容としては、タイトルが「RESTを使用した管理」へと変更され、より明確になっています。また、日付が2024年12月10日から2025年3月26日へと更新され、最新の情報が反映されています。

本文の改訂により、Azure AI Searchサービスを管理する際に利用するさまざまなAPIの新たな機能が強調されました。具体的には、新しく「サービスのアップグレード」や「料金プランの変更」に関するセクションが追加され、現在利用可能な選択肢や手順が詳述されています。これにより、ユーザーが必要な機能を素早く見つけられるようになり、操作の簡便さが向上しました。

さらに、具体的なAPIリクエストの例なども充実しており、ユーザーが具体的な操作を実施する際の参考になります。また、「Visual Studio Codeでの設定」に関する情報が再構成され、より理解しやすくなっています。

全体として、これらの更新によってREST APIを使用したAzure AI Searchサービスの管理に関する情報がより包括的かつ実用的になり、ユーザーが直面する可能性のあるシナリオに対して正確かつ迅速に対処できるようになることが期待されます。

## articles/search/search-markdown-data-tutorial.md{#item-32ea2a}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Tutorial: Index Markdown blobs'
+title: 'Tutorial: Index Markdown Blobs'
 titleSuffix: Azure AI Search
 description: Learn how to index and search Markdown in Azure blobs using Azure AI Search REST APIs.
 
@@ -9,40 +9,40 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: tutorial
-ms.date: 11/19/2024
+ms.date: 03/28/2025
 
 ---
 
 # Tutorial: Index nested Markdown blobs from Azure Storage using REST
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Azure AI Search can index Markdown documents and arrays in Azure Blob Storage using an [indexer](search-indexer-overview.md) that knows how to read Markdown data. 
+Azure AI Search can index Markdown documents and arrays in Azure Blob Storage using an [indexer](search-indexer-overview.md) that knows how to read Markdown data.
 
-This tutorial shows you to index Markdown files indexed using the `oneToMany` Markdown parsing mode. It uses a REST client and the [Search REST APIs](/rest/api/searchservice/) to perform the following tasks:
+This tutorial shows you how to index Markdown files indexed using the `oneToMany` Markdown parsing mode. It uses a REST client and the [Search REST APIs](/rest/api/searchservice/) to:
 
 > [!div class="checklist"]
 > + Set up sample data and configure an `azureblob` data source
 > + Create an Azure AI Search index to contain searchable content
 > + Create and run an indexer to read the container and extract searchable content
 > + Search the index you just created
 
-If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
-
 ## Prerequisites
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
-+ [Azure Storage](/azure/storage/common/storage-account-create)
++ [Azure Storage](/azure/storage/common/storage-account-create).
 
-+ [Azure AI Search](search-what-is-azure-search.md). [Create](search-create-service-portal.md) or [find an existing Azure AI Search resource](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) under your current subscription.
++ [Azure AI Search](search-what-is-azure-search.md). [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription.
+
++ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 > [!NOTE]
-> You can use the free service for this tutorial. A free search service limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before starting, make sure you have room on your service to accept the new resources.
+> You can use a free search service for this tutorial. The Free tier limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before you start, make sure you have room on your service to accept the new resources.
 
 ## Create a Markdown document
 
-Copy and paste the following Markdown into a file named `sample_markdown.md`. The sample data is a single Markdown file containing various Markdown elements. We chose one Markdown file to stay under the storage limits of the free tier.
+Copy and paste the following Markdown into a file named `sample_markdown.md`. The sample data is a single Markdown file containing various Markdown elements. We chose one Markdown file to stay under the storage limits of the Free tier.
 
 ````md
 # Project Documentation
@@ -193,7 +193,7 @@ Thank you for reviewing this example!
 
 ## Copy a search service URL and API key
 
-For this tutorial, connections to Azure AI Search require an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [managed identities](search-howto-managed-identities-data-sources.md).
+For this tutorial, connections to Azure AI Search require an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Managed identities](search-howto-managed-identities-data-sources.md).
 
 1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
 
@@ -205,7 +205,7 @@ For this tutorial, connections to Azure AI Search require an endpoint and an API
 
 1. Start Visual Studio Code and create a new file.
 
-1. Provide values for variables used in the request: 
+1. Provide values for variables used in the request.
 
    ```http
    @baseUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
@@ -216,7 +216,7 @@ For this tutorial, connections to Azure AI Search require an endpoint and an API
 
 1. Save the file using a `.rest` or `.http` file extension.
 
-See [Quickstart: Text search using REST](search-get-started-rest.md) if you need help with the REST client.
+For help with the REST client, see [Quickstart: Keyword search using REST](search-get-started-rest.md).
 
 ## Create a data source
 
@@ -293,19 +293,19 @@ You only need fields for the Markdown elements that the parser supports. These f
 
 - `content`: A string that contains the raw Markdown found in a specific location, based on the header metadata at that point in the document.
 
-- `sections`: An object that contains subfields for the header metadata up to the desired header level. For example, when `markdownHeaderDepth` is set to `h3`, contains string fields `h1`, `h2`, and `h3`. These fields are indexed by mirroring this structure in the index, or through field mappings in the format `/sections/h1`, `sections/h2`, etc. See index and indexer configurations in the following samples for in-context examples. The subfields contained are:
+- `sections`: An object that contains subfields for the header metadata up to the desired header level. For example, when `markdownHeaderDepth` is set to `h3`, contains string fields `h1`, `h2`, and `h3`. These fields are indexed by mirroring this structure in the index, or through field mappings in the format `/sections/h1`, `sections/h2`, etc. For in-context examples, see the index and indexer configurations in the following samples. The subfields contained are:
   - `h1` - A string containing the h1 header value. Empty string if not set at this point in the document.
   - (Optional) `h2`- A string containing the h2 header value. Empty string if not set at this point in the document.
   - (Optional) `h3`- A string containing the h3 header value. Empty string if not set at this point in the document.
   - (Optional) `h4`- A string containing the h4 header value. Empty string if not set at this point in the document.
   - (Optional) `h5`- A string containing the h5 header value. Empty string if not set at this point in the document.
   - (Optional) `h6`- A string containing the h6 header value. Empty string if not set at this point in the document.
 
-- `ordinal_position`: An integer value indicating the position of the section within the document hierarchy. This field is used for ordering the sections in their original sequence as they appear in the document, beginning with an ordinal position of 1 and incrementing sequentially for each content block. 
+- `ordinal_position`: An integer value that indicates the position of the section within the document hierarchy. This field is used for ordering the sections in their original sequence as they appear in the document, beginning with an ordinal position of 1 and incrementing sequentially for each content block.
 
-This implementation leverages [field mappings](search-indexer-field-mappings.md) in the indexer to map from the enriched content to the index. For more information on the parsed one-to-many document structure, see [index markdown blobs](search-how-to-index-markdown-blobs.md).
+This implementation uses [field mappings](search-indexer-field-mappings.md) in the indexer to map from the enriched content to the index. For more information about the parsed one-to-many document structure, see [Index Markdown blobs](search-how-to-index-markdown-blobs.md).
 
-This example provides samples of how to index data both with and without field mappings. In this case, we know that `h1` contains the title of the document, so we can map it to a field named `title`. We'll also be mapping the `h2` and `h3` fields to `h2_subheader` and `h3_subheader` respectively. The `content` and `ordinal_position` fields require no mapping because they are extracted from the Markdown directly into fields using those names. For an example of a full index schema that doesn't require field mappings, see the end of this section.
+This example provides samples of how to index data both with and without field mappings. In this case, we know that `h1` contains the title of the document, so we can map it to a field named `title`. We'll also be mapping the `h2` and `h3` fields to `h2_subheader` and `h3_subheader`, respectively. The `content` and `ordinal_position` fields require no mapping because they're extracted from the Markdown directly into fields using those names. For an example of a full index schema that doesn't require field mappings, see the end of this section.
 
 ```http
 ### Create an index
@@ -326,8 +326,10 @@ POST {{baseUrl}}/indexes?api-version=2024-11-01-preview  HTTP/1.1
     }
 ```
 
-###  Index schema in a configuration with no field mappings
-Field mappings allow you to manipulate and filter enriched content to fit into your desired index shape, but you may just want to take the enriched content directly. In that case, the schema would look like:
+### Index schema in a configuration with no field mappings
+
+Field mappings allow you to manipulate and filter enriched content to fit into your desired index shape. However, you might just want to take the enriched content directly. In that case, the schema would look like:
+
 ```http
 {
   "name": "sample-markdown-index",
@@ -347,9 +349,9 @@ Field mappings allow you to manipulate and filter enriched content to fit into y
 }
 ```
 
-To reiterate, we have subfields up to `h3` in the sections object because `markdownHeaderDepth` is set to `h3`. 
+To reiterate, we have subfields up to `h3` in the sections object because `markdownHeaderDepth` is set to `h3`.
 
-If you choose to use this schema, be sure to adjust later requests accordingly. This will require removing the field mappings from the indexer configuration and updating search queries to use the corresponding field names.
+If you use this schema, be sure to adjust later requests accordingly. This will require removing the field mappings from the indexer configuration and updating search queries to use the corresponding field names.
 
 ## Create and run an indexer
 
@@ -382,11 +384,11 @@ POST {{baseUrl}}/indexers?api-version=2024-11-01-preview  HTTP/1.1
     }
 ```
 
-**Key points**:
+Key points:
 
 + The indexer will only parse headers up to `h3`. Any lower-level headers (`h4`,`h5`,`h6`) will be treated as plain text and show up in the `content` field. This is why the index and field mappings only exist up to a depth of `h3`.
 
-+ The `content` and `ordinal_position` fields require no field mapping as they exist with those names in the enriched content.
++ The `content` and `ordinal_position` fields require no field mapping because they exist with those names in the enriched content.
 
 ## Run queries
 
@@ -404,7 +406,7 @@ POST {{baseUrl}}/indexes/sample-markdown-index/docs/search?api-version=2024-11-0
   }
 ```
 
-Send the request. This is an unspecified full text search query that returns all of the fields marked as retrievable in the index, along with a document count. The response should look like:
+Send the request. This is an unspecified full-text search query that returns all of the fields marked as retrievable in the index, along with a document count. The response should look like:
 
 ```json
 HTTP/1.1 200 OK
@@ -431,7 +433,7 @@ Connection: close
 
 ```
 
-Add a `search` parameter to search on a string. 
+Add a `search` parameter to search on a string.
 
 ```http
 ### Query the index
@@ -478,7 +480,8 @@ Connection: close
   ]
 }
 ```
-**Key points**:
+
+Key points:
 
 + Because the `markdownHeaderDepth` is set to `h3`, the `h4`, `h5`, and `h6` headers are treated as plaintext, so they appear in the `content` field.
 
@@ -528,14 +531,14 @@ Connection: close
 }
 ```
 
-For filters, you can also use Logical operators (and, or, not) and comparison operators (eq, ne, gt, lt, ge, le). String comparisons are case-sensitive. For more information and examples, see [Create a query](search-query-simple-examples.md).
+For filters, you can also use Logical operators (and, or, not) and comparison operators (eq, ne, gt, lt, ge, le). String comparisons are case sensitive. For more information and examples, see [Create a query](search-query-simple-examples.md).
 
 > [!NOTE]
 > The `$filter` parameter only works on fields that were marked filterable at the creation of your index.
 
 ## Reset and rerun
 
-Indexers can be reset, clearing execution history, which allows a full rerun. The following GET requests are for reset, followed by rerun.
+Indexers can be reset to clear execution history, which allows a full rerun. The following GET requests are for reset, followed by rerun.
 
 ```http
 ### Reset the indexer
@@ -562,7 +565,8 @@ When you're working in your own subscription, at the end of a project, it's a go
 You can use the Azure portal to delete indexes, indexers, and data sources.
 
 ## Next steps
-Now that you're familiar with the basics of Azure Blob indexing, let's take a closer look at indexer configuration for Markdown blobs in Azure Storage.
+
+Now that you're familiar with the basics of Azure Blob indexing, take a closer look at indexer configuration for Markdown blobs in Azure Storage:
 
 > [!div class="nextstepaction"]
 > [Configure Markdown blob indexing](search-how-to-index-markdown-blobs.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Markdownブロブのインデックス作成に関するチュートリアル"
}
```

### Explanation
この変更は、`articles/search/search-markdown-data-tutorial.md`ファイルの修正を示しており、MarkdownデータをAzureストレージ内のブロブとしてインデックスする方法についてのチュートリアルが更新されています。主な変更は、文書の一貫性と明瞭さを向上させるための表現の修正や、最新情報への更新が含まれています。

具体的な変更点として、タイトルが「Markdown blobsをインデックスするチュートリアル」に変更され、日付が2024年11月19日から2025年3月28日へ更新されています。また、チュートリアルの要約や目的が明確にされ、一部の文章がより分かりやすい形に見直されています。

内容では、**Azure AI Search**を使用してMarkdownファイルをインデックスするための手順が強調されており、特に新しい機能や手順が追加されています。データソースの設定、インデックスの作成、インデクサの実行、インデックスの検索などのタスクが明確に記載されています。また、「無料アカウントを作成」の文言が明確化されており、ユーザーは求められるリソースがサービスに収容可能なことを確認する必要があります。

さらに、Markdown構文の特定の要素についての説明や、APIを介してのデータのインデックス方法に関する具体的な手順も改善されています。特に、フィールドのマッピングやインデックススキーマに関する記述が整備され、初心者が操作する際の助けになるよう工夫されています。

全体として、この更新によりMarkdownデータを利用したインデクサの実装や設定がさらに具体的かつアクティブなものとなり、ユーザーがAzure AI Searchを効果的に活用できるようになることを目指しています。

## articles/search/search-performance-tips.md{#item-218e77}

<details>
<summary>Diff</summary>
````diff
@@ -6,12 +6,12 @@ author: mattgotteiner
 ms.author: magottei
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 12/10/2024
+ms.date: 03/21/2025
 ---
 
 # Tips for better performance in Azure AI Search
 
-This article is a collection of tips and best practices for boosting query and indexing performance for keyword search. Knowing which factors are most likely to impact search performance can help you avoid inefficiencies and get the most out of your search service. Some key factors include:
+This article is a collection of tips and best practices for boosting query and indexing performance for keyword search. Knowing which factors are most likely to affect search performance can help you avoid inefficiencies and get the most out of your search service. Some key factors include:
 
 + Index composition (schema and size)
 + Query design
@@ -22,7 +22,7 @@ This article is a collection of tips and best practices for boosting query and i
 
 ## Index size and schema
 
-Queries run faster on smaller indexes. This is partly a function of having fewer fields to scan, but it's also due to how the system caches content for future queries. After the first query, some content remains in memory where it's searched more efficiently. Because index size tends to grow over time, one best practice is to periodically revisit index composition, both schema and documents, to look for content reduction opportunities. However, if the index is right-sized, the only other calibration you can make is to increase capacity: either by [adding replicas](search-capacity-planning.md#adjust-capacity) or upgrading the service tier. The section ["Tip: Upgrade to a Standard S2 tier"](#tip-upgrade-to-a-standard-s2-tier) discusses the scale up versus scale out decision.
+Queries run faster on smaller indexes. This is partly a function of having fewer fields to scan, but it's also due to how the system caches content for future queries. After the first query, some content remains in memory where it's searched more efficiently. Because index size tends to grow over time, one best practice is to periodically revisit index composition, both schema and documents, to look for content reduction opportunities. However, if the index is right-sized, the only other calibration you can make is to increase capacity by [upgrading your service](search-how-to-upgrade.md), [adding replicas](search-capacity-planning.md#add-or-remove-partitions-and-replicas), or [switching to a higher tier](search-capacity-planning.md#change-your-pricing-tier). The section "[Tip: Switch to a Standard S2 tier](#tip-switch-to-a-standard-s2-tier)" discusses the scale up versus scale out decision.
 
 Schema complexity can also adversely affect indexing and query performance. Excessive field attribution builds in limitations and processing requirements. [Complex types](search-howto-complex-data-types.md) take longer to index and query. The next few sections explore each condition.
 
@@ -93,7 +93,7 @@ When query performance is slowing down in general, adding more replicas frequent
 
 One positive side-effect of adding partitions is that slower queries sometimes perform faster due to parallel computing. We've noted parallelization on low selectivity queries, such as queries that match many documents, or facets providing counts over a large number of documents. Since significant computation is required to score the relevancy of the documents, or to count the numbers of documents, adding extra partitions helps queries complete faster.  
 
-To add partitions, use [Azure portal](search-capacity-planning.md#adjust-capacity), [PowerShell](search-manage-powershell.md), [Azure CLI](search-manage-azure-cli.md), or a management SDK.
+To add partitions, use the [Azure portal](search-capacity-planning.md#add-or-remove-partitions-and-replicas), [PowerShell](search-manage-powershell.md), [Azure CLI](search-manage-azure-cli.md), or a management SDK.
 
 ## Service capacity
 
@@ -103,13 +103,13 @@ The tier of your search service and the number of replicas/partitions also have
 
 ### Tip: Create a new high capacity search service
 
-Basic and standard services created [in supported regions](search-limits-quotas-capacity.md#service-limits) after April 3, 2024 have more storage per partition than older services. Before upgrading to a higher tier and a higher billable rate, revisit the [tier service limits](search-limits-quotas-capacity.md#service-limits) to see if the same tier on a newer service gives you the necessary storage.
+Basic and Standard services created [in supported regions](search-limits-quotas-capacity.md#service-limits) after April 3, 2024 have more storage per partition than older services. If you have an older service, check if you can [upgrade your service](search-how-to-upgrade.md) to benefit from more capacity at the same billing rate. If an upgrade isn't available, review the [tier service limits](search-limits-quotas-capacity.md#service-limits) to see if the same tier on a newer service gives you the necessary storage.
 
-### Tip: Upgrade to a Standard S2 tier
+### Tip: Switch to a Standard S2 tier
 
 The Standard S1 search tier is often where customers start. A common pattern for S1 services is that indexes grow over time, which requires more partitions. More partitions lead to slower response times, so more replicas are added to handle the query load. As you can imagine, the cost of running an S1 service has now progressed to levels beyond the initial configuration.
 
-At this juncture, an important question to ask is whether it would be beneficial to move to a higher tier, as opposed to progressively increasing the number of partitions or replicas of the current service. 
+At this juncture, an important question to ask is whether it would be beneficial to [move to a higher tier](search-capacity-planning.md#change-your-pricing-tier), as opposed to progressively increasing the number of partitions or replicas of the current service.
 
 Consider the following topology as an example of a service that has taken on increasing levels of capacity:
 
@@ -133,7 +133,7 @@ However, if the administrator chose to move to a Standard S2 tier the topology w
 
 As this hypothetical scenario illustrates, you can have configurations on lower tiers that result in similar costs as if you had opted for a higher tier in the first place. However, higher tiers come with premium storage, which makes indexing faster. Higher tiers also have much more compute power, as well as extra memory. For the same costs, you could have more powerful infrastructure backing the same index.
 
-An important benefit of added memory is that more of the index can be cached, resulting in lower search latency, and a greater number of queries per second. With this extra power, the administrator may not need to even need to increase the replica count and could potentially pay less than by staying on the S1 service.
+An important benefit of added memory is that more of the index can be cached, resulting in lower search latency, and a greater number of queries per second. With this extra power, the administrator might not need to even need to increase the replica count and could potentially pay less than by staying on the S1 service.
 
 ### Tip: Consider alternatives to regular expression queries
 
@@ -146,5 +146,5 @@ Review these other articles related to service performance:
 + [Analyze performance](search-performance-analysis.md)
 + [Index large data sets in Azure AI Search](search-howto-large-index.md)
 + [Choose a service tier](search-sku-tier.md)
-+ [Plan or add capacity](search-capacity-planning.md#adjust-capacity)
++ [Plan or add capacity](search-capacity-planning.md#add-or-remove-partitions-and-replicas)
 + [Case Study: Use Cognitive Search to Support Complex AI Scenarios](https://techcommunity.microsoft.com/t5/azure-ai/case-study-effectively-using-cognitive-search-to-support-complex/ba-p/2804078)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのパフォーマンス向上に関するヒント"
}
```

### Explanation
この変更は、`articles/search/search-performance-tips.md`ファイルに加えられた修正を示しており、Azure AI Searchにおける検索およびインデックスパフォーマンスを向上させるためのヒント集が更新されています。主に文言の修正と内容の明確化が行われ、最新の情報に基づいています。

具体的には、最初の更新として、最終更新日が2024年12月10日から2025年3月21日に変更されました。また、パフォーマンスに影響を与える要因の説明で「影響を与える」に表現が変更され、より正確な表現が使用されています。

インデックスのサイズとスキーマに関するセクションでは、インデックスが小さいほどクエリが速く処理される理由が説明されており、同時に、スキーマの複雑さが性能に及ぼす影響も強調されています。このセクションでは、リソースのキャパシティを調整する方法についても明確になっています。

さらに、特定のアドバイスの順序が調整されたり、文体が整えられ、読みやすさが向上しました。「Standard S2 tierへの切り替え」という見出しが「Standard S2 tierへのアップグレード」から変更され、より一貫性のある表現にされています。

最後に、他の関連する記事へのリンクが更新され、情報が最新のリソースにアクセスできるように整えられています。これらの改訂により、Azure AI Searchのパフォーマンスを最適化するために必要なヒントとガイドが、より効果的に提供されることを意図しています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -9,24 +9,25 @@ ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
 ms.custom: references_regions
-ms.date: 01/27/2025
+ms.date: 04/04/2025
 
 ---
 
 # Azure AI Search regions list
 
-This article identifies the cloud regions in which Azure AI Search is available. It also lists which premium features are available in each region. 
+This article identifies the cloud regions in which Azure AI Search is available. It also lists which premium features are available in each region.
 
 ## Features subject to regional availability
 
 Some features take a dependency on other Azure services or infrastructure that are subject to regional availability. If you need a specific feature, make sure it's available in the desired region.
 
 | Feature | Description | Availability |
 |---------|-------------|--------------|
-| [Extra capacity](search-limits-quotas-capacity.md#service-limits) | Higher capacity partitions became available in selected regions starting in April 2024 with a second wave following in May 2024. Currently, there are just a few regions that *don't* offer higher capacity partitions. If you're using an older search service, create a new search service to benefit from more capacity at the same billing rate. |  Regional support for extra capacity is noted in the footnotes of this article. <p>Check [service age](vector-search-index-size.md#how-to-check-service-creation-date) to see if your search service was created after high capacity partitions became available. <p>To check the capacity of an existing service, [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) and select the **Properties** tab in the middle of the Overview page.|
-| [Availability zones](search-reliability.md#availability-zone-support) | Divides a region's data centers into distinct physical location groups, providing high-availability within the same geo. | Regional support is noted in this article. |
+| [Extra capacity](search-limits-quotas-capacity.md#service-limits) | Higher capacity partitions became available in select regions starting in April 2024, with a second wave following in May 2024. Currently, there are just a few regions that *don't* offer higher capacity partitions. If you have an older search service in a supported region, check if you can [upgrade your service](search-how-to-upgrade.md). Otherwise, create a new search service to benefit from more capacity at the same billing rate. |  Regional support for extra capacity is noted in the footnotes of this article. <p>Check your [service age](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date) to see if your search service was created after high capacity partitions became available. <p>To check the capacity of an existing service, [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) and select the **Properties** tab in the middle of the **Overview** page.|
+| [Availability zones](search-reliability.md#availability-zone-support) | Divides a region's data centers into distinct physical location groups, providing high availability within the same geo. | Regional support is noted in this article. |
 | [Semantic ranker](semantic-search-overview.md) | Takes a dependency on Microsoft-hosted models in specific regions. | Regional support is noted in this article. |
-| [AI service integration](cognitive-search-concept-intro.md) | Refers to [built-in skills](cognitive-search-predefined-skills.md) that make internal calls to Azure AI for enrichment and transformation during indexing. Integration requires that Azure AI Search coexists with an [Azure AI services multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills) in the same physical region. You can bypass region requirements if you use [identity-based connections](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection), currently in public review. | Regional support is noted in this article. |
+| [Query rewrite](semantic-how-to-query-rewrite.md) | Takes a dependency on Microsoft-hosted models in specific regions. | Regional support is noted in this article. |
+| [AI service integration](cognitive-search-concept-intro.md) | Refers to [built-in skills](cognitive-search-predefined-skills.md) that make internal calls to Azure AI for enrichment and transformation during indexing. Integration requires that Azure AI Search coexists with an [Azure AI services multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills) in the same physical region. You can bypass region requirements if you use [identity-based connections](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection), currently in public preview. | Regional support is noted in this article. |
 | [Azure OpenAI integration](vector-search-integrated-vectorization.md)  | Refers to the AzureOpenAIEmbedding skill and vectorizer that make internal calls to deployed embedding models on Azure OpenAI. | Check [Azure OpenAI model region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability) for the most current list of regions for each embedding and chat model. Specific Azure OpenAI models are in fewer regions, so check for model availability first, and then verify Azure AI Search is available in the same region.|
 | [Azure AI Foundry integration](vector-search-integrated-vectorization-ai-studio.md) | Refers to skills and vectorizers that make internal calls to the models hosted in the model catalog. | Check [Azure AI Foundry region availability](/azure/ai-foundry/reference/region-support) for the most current list of regions. |
 | [Azure AI Vision 4.0 multimodal APIs](search-get-started-portal-image-search.md) | Refers to the Azure AI Vision multimodal embeddings skill and vectorizer that call the multimodal embedding API. | Check the [Azure AI Vision region list](/azure/ai-services/computer-vision/overview-image-analysis#region-availability) first, and then verify Azure AI Search is available in the same region.|
@@ -39,97 +40,99 @@ AI service integration refers to internal connections to an Azure AI services mu
 
 ### Americas
 
-| Region | AI service integration | Semantic ranker | Availability zones | Capacity constrained |
+| Region | AI service integration | Availability zones | Semantic ranker | Query rewrite |
 |--|--|--|--|--|
-| Brazil South​​ ​ | ✅ | ✅ | |  |
+| Brazil South​​ ​| ✅ |  | ✅ |  |
 | Canada Central​​ | ✅ | ✅ | ✅ |  |
-| Canada East​​ ​ |  | ✅ | |  |
-| ​Central US​​ | ✅ | ✅ | ✅ | |
+| Canada East​​ ​|  |  | ✅ |  |
+| ​Central US​​ | ✅ | ✅ | ✅ |  |
 | East US​ | ✅ | ✅ | ✅ |  |
-| East US 2 ​ | ✅ | ✅ | ✅ | |
-| Mexico Central | |  | ✅ | |
-| North Central US​ ​ | ✅ | ✅ | |  | 
-| South Central US​  | ✅ | ✅ | ✅ | |
-| West US​ ​ | ✅ | ✅ | |  |
-| West US 2​ ​ | ✅ | ✅ | ✅ | |
-| West US 3​ | ✅ | ✅ |✅ | |
-| West Central US​ ​ | ✅ | ✅ | | |
+| East US 2 ​ | ✅ | ✅ | ✅ |  |
+| Mexico Central |  | ✅ |  |  |
+| North Central US​ ​| ✅ |  | ✅ |  |
+| South Central US​ | ✅ | ✅ | ✅ |  |
+| West US​​ | ✅ |  | ✅ |  |
+| West US 2​ ​| ✅ | ✅ | ✅ |  |
+| West US 3​ | ✅ | ✅ | ✅ |  |
+| West Central US​ ​ | ✅ |  | ✅ |  |
 
 ### Europe
 
-| Region | AI service integration | Semantic ranker | Availability zones | Capacity constrained |
+| Region | AI service integration | Availability zones | Semantic ranker | Query rewrite |
 |--|--|--|--|--|
-| North Europe​​ | ✅ | ✅ | ✅ | S2, S3, L1, L2|
+| North Europe​ <sup>1</sup>​ | ✅ | ✅ | ✅ | ✅ |
 | West Europe​​ | ✅ | ✅ | ✅ |  |
-| France Central​​ | ✅ | ✅ | ✅ | |
-| Germany West Central​ ​| ✅ |  | ✅ | |
-| Italy North​​ |  |  | ✅ | |
-| Norway East​​ | ✅ |  | ✅ |  |
+| France Central​​ | ✅ | ✅ | ✅ |  |
+| Germany West Central​ ​| ✅ | ✅ |  |  |
+| Italy North​​ |  | ✅ |  |  |
+| Norway East​​ | ✅ | ✅ |  |  |
 | Poland Central​​ |  |  |  |  |
-| Spain Central <sup>1</sup> |  |  | ✅  |  |
-| Sweden Central​​ | ✅ |  | ✅ |  |
+| Spain Central <sup>2</sup> |  | ✅ |  |  |
+| Sweden Central​​ | ✅ | ✅ |  |  |
 | Switzerland North​ | ✅ | ✅ | ✅ |  |
 | Switzerland West​ | ✅ | ✅ | ✅ |  |
 | UK South​ | ✅ | ✅ | ✅ |  |
-| UK West​ ​|  | ✅ | |  |
+| UK West​ ​|  |  | ✅ |  |
 
-<sup>1</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
+<sup>1</sup> This region has capacity constraints on the following tiers: S2, S3, L1, and L2.
+
+<sup>2</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
 
 ### Middle East
 
-| Region | AI service integration | Semantic ranker | Availability zones | Capacity constrained |
+| Region | AI service integration | Availability zones | Semantic ranker | Query rewrite |
 |--|--|--|--|--|
-| Israel Central​ <sup>1</sup> |  |  | ✅  |  |
-| Qatar Central​ <sup>1</sup> |  |  | ✅ | |
-| UAE North​​ | ✅ |  | ✅ |  |
+| Israel Central​ <sup>1</sup> |  | ✅ |  |  |
+| Qatar Central​ <sup>1</sup> |  | ✅ |  |  |
+| UAE North​​ | ✅ | ✅ |  |  |
 
-<sup>1</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
+<sup>1</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
 
 ### Africa
 
-| Region | AI service integration | Semantic ranker | Availability zones | Capacity constrained |
+| Region | AI service integration | Availability zones | Semantic ranker | Query rewrite |
 |--|--|--|--|--|
-| South Africa North​ | ✅ |  | ✅ |   |
+| South Africa North​ | ✅ | ✅ |  |  |
 
 ### Asia Pacific
 
-| Region | AI service integration | Semantic ranker | Availability zones | Capacity constrained |
+| Region | AI service integration | Availability zones | Semantic ranker | Query rewrite |
 |--|--|--|--|--|
-| Australia East​ ​ | ✅ | ✅ | ✅ |   |
-| Australia Southeast​​​ |  | ✅ |  | |
+| Australia East​ ​| ✅ | ✅ | ✅ |  |
+| Australia Southeast​​​ |  |  | ✅ |  |
 | East Asia​ | ✅ | ✅ | ✅ |  |
-| Southeast Asia​ ​ ​ | ✅ | ✅ | ✅ |  |
+| Southeast Asia​​ | ✅ | ✅ | ✅ | ✅ |
 | Central India | ✅ | ✅ | ✅ |  |
-| Jio India West​ ​ | ✅ | ✅ |  |
-| South India <sup>1</sup> |  | | ✅ |
-| Japan East  | ✅ | ✅ | ✅ |
-| Japan West​ | ✅ | ✅ |  |
-| Korea Central | ✅ | ✅ | ✅ |
-| Korea South​ ​ |  | ✅ |  |
-| Taiwan North |  |  |   |  |
+| Jio India West​​ | ✅ |  | ✅ |  |
+| South India <sup>1</sup> |  | ✅ |  |  |
+| Japan East | ✅ | ✅ | ✅ |  |
+| Japan West​ | ✅ |  | ✅ |  |
+| Korea Central | ✅ | ✅ | ✅ |  |
+| Korea South​​ |  |  | ✅ |  |
+| Indonesia Central |  | ✅ |  |  |
 
-<sup>1</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
+<sup>1</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
 
 ## Azure Government regions
 
-| Region | AI service integration | Semantic ranker | Availability zones | Capacity constrained |
+| Region | AI service integration | Availability zones | Semantic ranker | Query rewrite |
 |--|--|--|--|--|
-| Arizona | ✅ | ✅  | | |
-| Texas |  | ✅ |  | |
-| Virginia | ✅ | ✅  | ✅ | |
+| Arizona | ✅ |  | ✅ |  |
+| Texas |  |  |  |  |
+| Virginia | ✅ | ✅ | ✅ |  |
 
 ## Azure operated by 21Vianet
 
-| Region | AI service integration | Semantic ranker | Availability zones | Capacity constrained |
+| Region | AI service integration | Availability zones | Semantic ranker | Query rewrite |
 |--|--|--|--|--|
-| China East |  |  |  |
-| China East 2 <sup>1</sup> | ✅  | | | |
-| China East 3 |  |  |  | |
-| China North |  |  | | |
-| China North 2 <sup>1</sup> |  |  | | |
-| China North 3 | | ✅ | ✅ | |
-
-<sup>1</sup> This region runs on older infrastructure that has lower storage limits per partition at every tier. Choose a different region if you want [higher limits](search-limits-quotas-capacity.md#service-limits).
+| China East |  |  |  |  |
+| China East 2 <sup>1</sup> | ✅ |  |  |  |
+| China East 3 |  |  |  |  |
+| China North |  |  |  |  |
+| China North 2 <sup>1</sup> |  |  |  |  |
+| China North 3 |  | ✅ | ✅ |  |
+
+<sup>1</sup> [Higher storage limits](search-limits-quotas-capacity.md#service-limits) aren't available in this region. If you want higher limits, choose a different region.
 
 ## See also
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのリージョンサポート"
}
```

### Explanation
この変更は、`articles/search/search-region-support.md`ファイルに対する修正を示しており、Azure AI Searchが利用可能なクラウドリージョンと各リージョンで利用できるプレミアム機能のリストが更新されています。主に、機能の説明とそれらのリージョンに関する情報が強化されています。

変更点としては、最終更新日が2025年1月27日から2025年4月4日に変更され、最新情報に基づくアップデートが反映されています。また、特定の機能に関連する情報が拡充され、各リージョンで利用可能な機能の詳細が具体的に記述されています。

特に「余分なキャパシティ」や「可用性ゾーン」などの機能に関する項目が改訂され、視覚的に整理された表形式での情報提供がなされています。この表には、各機能が特定のリージョンでどのようにサポートされているか、また、古いサービスを使用している場合の適切なアクションについての情報も含まれています。

さらに、文書全体を通して、地域特有のサービス制約やキャパシティ制限に関する情報も更新され、ユーザーがどのリージョンを選択するべきかを判断する際の参考になるよう注意深く記載されています。また、文言の修正や整形が行われ、より明確で一貫した情報提供がなされています。

この改訂により、Azure AI Searchの地域サポートに関する情報がより利用しやすく、最新のサービス提供状況に即した内容となり、ユーザーがサービスの選択や構成を行う際に役立つことを目指しています。

## articles/search/search-reliability.md{#item-3e9b1a}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: mattgotteiner
 ms.author: magottei
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 10/29/2024
+ms.date: 03/21/2025
 ms.custom:
   - subject-reliability
   - references_regions
@@ -21,13 +21,13 @@ Across Azure, [reliability](/azure/reliability/overview) means resiliency and av
 
 + Deploy multiple search services across different geographic regions. All search workloads are fully contained within a single service that runs in a single geographic region, but in a multi-service scenario, you have options for synchronizing content so that it's the same across all services. You can also set up a load balancing solution to redistribute requests or fail over if there's a service outage.
 
-For business continuity and recovery from disasters at a regional level, plan on a cross-regional topology, consisting of multiple search services having identical configuration and content. Your custom script or code provides the *fail over* mechanism to an alternate search service if one suddenly becomes unavailable.
+For business continuity and recovery from disasters at a regional level, plan on a cross-regional topology, consisting of multiple search services having identical configuration and content. Your custom script or code provides the *failover* mechanism to an alternate search service if one suddenly becomes unavailable.
 
 <a name="scale-for-availability"></a>
 
 ## High availability
 
-In Azure AI Search, replicas are copies of your index. A search service is commissioned with at least one replica, and can have up to 12 replicas. [Adding replicas](search-capacity-planning.md#adjust-capacity) allows Azure AI Search to do machine reboots and maintenance against one replica, while query execution continues on other replicas.
+In Azure AI Search, replicas are copies of your index. A search service is commissioned with at least one replica, and can have up to 12 replicas. [Adding replicas](search-capacity-planning.md#add-or-remove-partitions-and-replicas) allows Azure AI Search to do machine reboots and maintenance against one replica, while query execution continues on other replicas.
 
 For each individual search service, Microsoft guarantees at least 99.9% availability for configurations that meet these criteria:
 
@@ -45,7 +45,7 @@ No Service Level Agreement (SLA) is provided for the *Free* tier. For more infor
 
 [Availability zones](/azure/reliability/availability-zones-overview) are an Azure platform capability that divides a region's data centers into distinct physical location groups to provide high availability, within the same region. In Azure AI Search, individual replicas are the units for zone assignment. A search service runs within one region; its replicas run in different physical data centers (or zones) within that region.
 
-Availability zones are used when you add two or more replicas to your search service. Each replica is placed in a different availability zone within the region. If you have more replicas than available zones in the search service region, the replicas are distributed across zones as evenly as possible. There's no specific action on your part, except to [create a search service](search-create-service-portal.md) in a region that provides availability zones, and then to configure the service to [use multiple replicas](search-capacity-planning.md#adjust-capacity).
+Availability zones are used when you add two or more replicas to your search service. Each replica is placed in a different availability zone within the region. If you have more replicas than available zones in the search service region, the replicas are distributed across zones as evenly as possible. There's no specific action on your part, except to [create a search service](search-create-service-portal.md) in a region that provides availability zones, and then to configure the service to [use multiple replicas](search-capacity-planning.md#add-or-remove-partitions-and-replicas).
 
 ### Prerequisites
 
@@ -115,7 +115,7 @@ The goal of a geo-distributed set of search services is to have two or more inde
 You can implement this architecture by creating multiple services and designing a strategy for data synchronization. Optionally, you can include a resource like Azure Traffic Manager for routing requests. 
 
 > [!TIP]
-> For help in deploying multiple search services across multiple regions, see this [Bicep sample on GitHub](https://github.com/Azure-Samples/azure-search-multiple-regions) that deploys a fully configured, multi-regional search solution. The sample gives you two options for index synchronization, and request redirection using Traffic Manager.
+> For help with deploying multiple search services across multiple regions, see this [Bicep sample on GitHub](https://github.com/Azure-Samples/azure-search-multiple-regions) that deploys a fully configured, multi-regional search solution. The sample gives you two options for index synchronization, and request redirection using Traffic Manager.
 
 <a name="data-sync"></a>
 
@@ -166,7 +166,7 @@ Azure Traffic Manager is primarily used for routing network traffic across diffe
 Traffic Manager doesn't provide an endpoint for a direct connection to Azure AI Search, which means you can't put a search service directly behind Traffic Manager. Instead, the assumption is that requests flow to Traffic Manager, then to a search-enabled web client, and finally to a search service on the backend. The client and service are located in the same region. If one search service goes down, the search client starts failing, and Traffic Manager redirects to the remaining client.
 
 > [!NOTE]
-> If you are using Azure Load Balancer [health probes](/azure/load-balancer/load-balancer-custom-probe-overview) on a search service, you must use a HTTPS probe with `/ping` as the path.
+> If you are using Azure Load Balancer [health probes](/azure/load-balancer/load-balancer-custom-probe-overview) on a search service, you must use an HTTPS probe with `/ping` as the path.
 
 ![Diagram of search apps connecting through Azure Traffic Manager.][4]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchの信頼性について"
}
```

### Explanation
この変更は、`articles/search/search-reliability.md`ファイルの修正を示しており、Azure AI Searchの信頼性に関する情報が更新されています。主に、更新日が2024年10月29日から2025年3月21日に変更され、全体的な内容が最新の情報に基づくものとなっています。

具体的には、信頼性の向上やビジネス継続性のためのクロスリージョントポロジーの活用に関する説明が整理されており、複数の検索サービスを地理的に分散してデプロイする方法についての具体的な指針が記載されています。これにより、サービスの可用性を保ちながら、災害時の復旧が確実に行えるように設定する方法が強調されています。

さらに、検索サービスのレプリカに関する情報がわかりやすく整理され、特にレプリカの追加に関する手順が明確に示されています。新たに追加された「可用性ゾーン」の概念は、検索サービスが高可用性を実現するためにどのように活用されるかについての重要な知見を提供しています。

文中の指示や情報源へのリンクが最新のものに更新されており、具体的なサービスやプロセスに対する参照が改善されています。また、特定の注意事項や推奨事項が明確に記載され、ユーザーが容易に理解しやすい形に整えられています。

この改訂によって、Azure AI Searchの信頼性に関する内容がより実用的かつ利用者が必要とする情報に密接に関連するものに改善されており、ユーザーにとって有益な資源となることを目的としています。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title:  Encrypt data using customer-managed keys
+title: Encrypt data using customer-managed keys
 titleSuffix: Azure AI Search
 description: Supplement server-side encryption in Azure AI Search using customer managed keys (CMK) or bring your own keys (BYOK) that you create and manage in Azure Key Vault.
 
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/03/2025
+ms.date: 04/07/2025
 ms.custom:
   - references_regions
   - ignite-2023
@@ -110,7 +110,7 @@ Enable the system assigned managed identity for your search service. It's a two-
 
 1. Give the identity a descriptive name.
 
-1. Next, assign the user-managed identity to the search service. This can be done using the latest preview [2024-06-01-preview](/rest/api/searchmanagement/management-api-versions) management API or the previous preview.
+1. Next, assign the user-managed identity to the search service. This can be done using the latest preview [2025-05-01-preview](/rest/api/searchmanagement/management-api-versions) management API or the previous preview.
 
     The identity property takes a type and one or more fully qualified user-assigned identities:
   
@@ -122,7 +122,7 @@ Enable the system assigned managed identity for your search service. It's a two-
     Example of how to assign a user-managed identity to a search service:
   
     ```http
-    PUT https://management.azure.com/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Search/searchServices/[search service name]?api-version=2024-06-01-preview
+    PUT https://management.azure.com/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Search/searchServices/[search service name]?api-version=2025-05-01-preview
     Content-Type: application/json
 
     {
@@ -213,9 +213,9 @@ In the Azure portal, skillsets are defined in JSON view. Use the JSON shown in t
 
 1. Add a new object. In the object definition, select **Microsoft-managed encryption**.
 
-1. Select **Customer-managed keys** and use the pickers to select the vault, key, and version.
+1. Select **Customer-managed keys** and choose your subscription, vault, key, and version.
 
-:::image type="content" source="media/search-security-manage-encryption-keys/assign-key-vault-portal.png" alt-text="Screenshot of the encryption key page in the Azure portal.":::
+:::image type="content" source="media/search-security-manage-encryption-keys/assign-key-vault.png" alt-text="Screenshot of the encryption key page in the Azure portal.":::
 
 ### [**REST APIs**](#tab/rest)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "顧客管理キーを使用したデータの暗号化"
}
```

### Explanation
この変更は、`articles/search/search-security-manage-encryption-keys.md`ファイルに対する修正を反映しており、顧客管理キーを使用してAzure AI Search内でデータを暗号化する方法に関する内容が更新されています。主な変更は、ドキュメントのタイトルと更新日、管理APIのバージョン、いくつかの文言に関する修正が含まれています。

具体的には、更新日は2025年3月3日から2025年4月7日に変更され、情報が最新の状態に保たれています。また、ユーザー管理のIDを検索サービスに割り当てる手順において、管理APIのバージョンが「2024-06-01-preview」から「2025-05-01-preview」に更新されており、これにより最新の機能や修正が反映された状態での使用を促しています。

さらに、検索サービスに関連する設定手順の詳細が明確に記載され、特に顧客管理キーの選択に関する手順が「ピッカーを使用する」から「選択する」という表現に変更されています。これにより、手順がより直感的で分かりやすくなっています。

最後に、スクリーンショットの参照先が変更され、これに伴って新しいビジュアルコンテンツが提供されているため、利用者が暗号化キーの設定をより簡単に理解できるようになっています。

このような修正により、ユーザーは最新の情報に基づいてAzure AI Searchでの暗号化キーの管理を適切に行えるようになり、全体的なセキュリティ対策が向上することを目的としています。

## articles/search/search-security-network-security-perimeter.md{#item-49c0d7}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ This article explains how to join an Azure AI Search service to a [network secur
 * Block any data exfiltration from a search service to other services outside the perimeter.
 * Allow access to your search service using inbound and outbound access capabilities of the network security perimeter.
 
-You can add a search service to a network security perimeter in the Azure portal, as described in this article. Alternatively, you can use the [Azure Virtual Network Manager REST API](/rest/api/networkmanager/) to join a search service, and use the [Search Management REST APIs](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true) to view and synchronize the configuration settings.
+You can add a search service to a network security perimeter in the Azure portal, as described in this article. Alternatively, you can use the [Azure Virtual Network Manager REST API](/rest/api/networkmanager/) to join a search service, and use the [Search Management REST APIs](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2025-05-01-preview&preserve-view=true) to view and synchronize the configuration settings.
 
 ## Limitations and considerations
 
@@ -270,9 +270,9 @@ In order to test your connection through network security perimeter, you need ac
 
 ## View and manage network security perimeter configuration
 
-You can use the [Network Security Perimeter Configuration REST APIs](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true) to review and reconcile perimeter configurations.
+You can use the [Network Security Perimeter Configuration REST APIs](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2025-05-01preview&preserve-view=true) to review and reconcile perimeter configurations.
 
-Be sure to use preview API version `2024-06-01-preview`. [Learn how to call the Management REST APIs](search-manage-rest.md).
+Be sure to use preview API version `2024-06-01-preview` or a later preview. [Learn how to call the Management REST APIs](search-manage-rest.md).
 
 ## See also
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのネットワークセキュリティ境界"
}
```

### Explanation
この変更は、`articles/search/search-security-network-security-perimeter.md`ファイルにおける修正を示しており、Azure AI Searchサービスをネットワークセキュリティ境界に追加する方法に関する情報が更新されています。変更の主なポイントは、APIのバージョンが更新されたことと、いくつかの文言が明確化されたことです。

具体的には、検索サービスをネットワークセキュリティ境界に追加する方法についての説明において、検索管理REST APIの参照が「2024-06-01-preview」から「2025-05-01-preview」に変更されており、最新のAPIを使用することで、ユーザーが得られる機能や修正が最新の状態で利用できることを示しています。

さらに、「ネットワークセキュリティ境界構成をレビューおよび調整するためのREST API」についてのセクションでも、同様にAPIのバージョンが更新されています。この修正により、ユーザーがAPIの使用時に提供される機能が最新であることを確保し、新しい情報が整った状態で利用できることを意図しています。

また、最後の注意事項では、使用するAPIバージョンについての文言が調整されており、以前のプレビュー版に加えて新しいプレビュー版の利用が推奨されています。これにより、ユーザーは常に最新の情報に基づいて操作を行うことができ、より安全かつ効率的にAzure AI Searchのネットワークセキュリティを管理できるようになります。

全体として、この改訂は、最新のAPI情報を反映し、ユーザーの理解を助けるためにドキュメントを最新化することを目的としています。

## articles/search/search-security-overview.md{#item-6b3f1e}

<details>
<summary>Diff</summary>
````diff
@@ -237,7 +237,7 @@ CMK support was rolled out in two phases. If you created your search service dur
 
 + The second rollout on May 13, 2021 added encryption for temporary disks and extended CMK encryption to [all supported regions](search-region-support.md).
 
-  If you're using CMK from a service created during the first rollout and you also want CMK encryption over temporary disks, you need to create a new search service in your region of choice and redeploy your content. To determine your service creation date, see [How to check service creation date](vector-search-index-size.md#how-to-check-service-creation-date).
+  If you're using CMK from a service created during the first rollout and you also want CMK encryption over temporary disks, you need to create a new search service in your region of choice and redeploy your content. To determine your service creation date, see [How to check service creation date](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date).
 
 Enabling CMK encryption will increase index size and degrade query performance. Based on observations to date, you can expect to see an increase of 30-60 percent in query times, although actual performance will vary depending on the index definition and types of queries. Because of the negative performance impact, we recommend that you only enable this feature on indexes that really require it. For more information, see [Configure customer-managed encryption keys in Azure AI Search](search-security-manage-encryption-keys.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタマー管理キー（CMK）に関する情報の更新"
}
```

### Explanation
この変更は、`articles/search/search-security-overview.md`ファイルでの修正を示しており、カスタマー管理キー（CMK）に関する情報が更新されています。主な変更は、CMK関連の説明におけるリンク先の修正です。

具体的には、CMKの利便性を向上させるための重要な情報が含まれています。具体的な変更点は、以下の通りです：

1. **CMKの暗号化**: 2021年5月13日に行われた第2弾の展開についての説明が追加され、これにより一時ディスクの暗号化が追加され、CMKの暗号化がすべてのサポートされている地域に拡大された旨が明記されています。

2. **リンク先の更新**: CMK暗号化を有効にするために新しい検索サービスを作成する必要がある場合の手順に関するリンクが、以前のリンクから新しいリンクに変更されています。これにより、ユーザーがサービスの作成日を確認する手順が、より適切な情報源にアクセスできるようになっています。

この情報の更新により、ユーザーはより新しい情報をもとにCMKの操作を理解でき、具体的な手続きや注意事項を適切に把握することが可能になります。全体的に見て、この変更は、CMKの利用を促進し、ユーザーがサービスを最大限に活用できるようにするためのものです。

## articles/search/search-semi-structured-data.md{#item-d3388d}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Tutorial: Index semi-structured data in JSON blobs'
+title: 'Tutorial: Index Semi-Structured Data in JSON Blobs'
 titleSuffix: Azure AI Search
 description: Learn how to index and search semi-structured Azure JSON blobs using Azure AI Search REST APIs.
 
@@ -10,42 +10,42 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: tutorial
-ms.date: 12/10/2024
+ms.date: 03/28/2025
 
 ---
 
 # Tutorial: Index nested JSON blobs from Azure Storage using REST
 
-Azure AI Search can index JSON documents and arrays in Azure Blob Storage using an [indexer](search-indexer-overview.md) that knows how to read semi-structured data. Semi-structured data contains tags or markings which separate content within the data. It splits the difference between unstructured data, which must be fully indexed, and formally structured data that adheres to a data model, such as a relational database schema that can be indexed on a per-field basis.
+Azure AI Search can index JSON documents and arrays in Azure Blob Storage using an [indexer](search-indexer-overview.md) that knows how to read semi-structured data. Semi-structured data contains tags or markings that separate content within the data. It splits the difference between unstructured data, which must be fully indexed, and formally structured data that adheres to a data model, such as a relational database schema that can be indexed on a per-field basis.
 
-This tutorial shows you to index nested JSON arrays. It uses a REST client and the [Search REST APIs](/rest/api/searchservice/) to perform the following tasks:
+This tutorial shows you how to index nested JSON arrays, using a REST client and the [Search REST APIs](/rest/api/searchservice/) to:
 
 > [!div class="checklist"]
 > + Set up sample data and configure an `azureblob` data source
 > + Create an Azure AI Search index to contain searchable content
 > + Create and run an indexer to read the container and extract searchable content
 > + Search the index you just created
 
-If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
-
 ## Prerequisites
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
-+ [Azure Storage](/azure/storage/common/storage-account-create)
++ [Azure Storage](/azure/storage/common/storage-account-create).
 
-+ [Azure AI Search](search-what-is-azure-search.md). [Create](search-create-service-portal.md) or [find an existing Azure AI Search resource](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) under your current subscription.
++ [Azure AI Search](search-what-is-azure-search.md). [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription.
+
++ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 > [!NOTE]
-> You can use the free service for this tutorial. A free search service limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before starting, make sure you have room on your service to accept the new resources.
+> You can use a free search service for this tutorial. The Free tier limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before you start, make sure you have room on your service to accept the new resources.
 
 ### Download files
 
 Download a zip file of the sample data repository and extract the contents. [Learn how](https://docs.github.com/get-started/start-your-journey/downloading-files-from-github).
 
 + [ny-philharmonic-free](https://github.com/Azure-Samples/azure-search-sample-data)
 
-Sample data is a single JSON file containing a JSON array and 1,521 nested JSON elements. Sample data originates from [NY Philharmonic Performance History](https://www.kaggle.com/datasets/nyphil/perf-history) on Kaggle. We chose one JSON file to stay under the storage limits of the free tier.
+The sample data is a single JSON file that contains a JSON array and 1,521 nested JSON elements. The data originates from the [NY Philharmonic Performance History](https://www.kaggle.com/datasets/nyphil/perf-history) on Kaggle. We chose one JSON file to stay under the storage limits of the Free tier.
 
 Here's the first nested JSON in the file. The remainder of the file includes 1,520 other instances of concert performances.
 
@@ -90,7 +90,7 @@ Here's the first nested JSON in the file. The remainder of the file includes 1,5
 
 ### Upload sample data to Azure Storage
 
-1. In Azure Storage, create a new container and name it *ny-philharmonic-free*.
+1. In Azure Storage, create a new container named **ny-philharmonic-free**.
 
 1. [Upload the sample data files](/azure/storage/blobs/storage-quickstart-blobs-portal).
 
@@ -106,7 +106,7 @@ Here's the first nested JSON in the file. The remainder of the file includes 1,5
 
 ### Copy a search service URL and API key
 
-For this tutorial, connections to Azure AI Search require an endpoint and an API key. You can get these values from the Azure portal.
+For this tutorial, connections to Azure AI Search require an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Managed identities](search-howto-managed-identities-data-sources.md).
 
 1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
 
@@ -116,9 +116,9 @@ For this tutorial, connections to Azure AI Search require an endpoint and an API
 
 ## Set up your REST file
 
-1. Start Visual Studio Code and create a new file
+1. Start Visual Studio Code and create a new file.
 
-1. Provide values for variables used in the request: 
+1. Provide values for variables used in the request.
 
    ```http
    @baseUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
@@ -129,7 +129,7 @@ For this tutorial, connections to Azure AI Search require an endpoint and an API
 
 1. Save the file using a `.rest` or `.http` file extension.
 
-See [Quickstart: Text search using REST](search-get-started-rest.md) if you need help with the REST client.
+For help with the REST client, see [Quickstart: Keyword search using REST](search-get-started-rest.md).
 
 ## Create a data source
 
@@ -199,7 +199,7 @@ Connection: close
 
 [Create Index (REST)](/rest/api/searchservice/indexes/create) creates a search index on your search service. An index specifies all the parameters and their attributes.
 
-For nested JSON, the index fields must be identical to the source fields. Currently, Azure AI Search doesn't support field mappings to nested JSON. For this reason, field names and data types must match completely. The following index aligns to the JSON elements in the raw content.
+For nested JSON, the index fields must be identical to the source fields. Currently, Azure AI Search doesn't support field mappings to nested JSON, so field names and data types must match completely. The following index aligns to the JSON elements in the raw content.
 
 ```http
 ### Create an index
@@ -235,7 +235,7 @@ POST {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
     }
 ```
 
-**Key points**:
+Key points:
 
 + You can't use [field mappings](search-indexer-field-mappings.md) to reconcile differences in field names or data types. This index schema is designed to mirror the raw content.
 
@@ -268,7 +268,7 @@ POST {{baseUrl}}/indexers?api-version=2024-07-01  HTTP/1.1
     }
 ```
 
-**Key points**:
+Key points:
 
 + The raw content file contains a JSON array (`"programs"`) with 1,526 nested JSON structures. Set `parsingMode` to `jsonArray` to tell the indexer that each blob contains a  JSON array. Because the nested JSON starts one level down, set `documentRoot` to `/programs`.
 
@@ -290,7 +290,7 @@ POST {{baseUrl}}/indexes/ny-philharmonic-index/docs/search?api-version=2024-07-0
   }
 ```
 
-Send the request. This is an unspecified full text search query that returns all of the fields marked as retrievable in the index, along with a document count. The response should look like:
+Send the request. This is an unspecified full-text search query that returns all of the fields marked as retrievable in the index, along with a document count. The response should look like:
 
 ```json
 HTTP/1.1 200 OK
@@ -321,7 +321,7 @@ Connection: close
 }
 ```
 
-Add a `search` parameter to search on a string. Add a `select` parameter to limit the results to fewer fields. Add a `filter` to further narrow the search.
+Add a `search` parameter to search on a string, a `select` parameter to limit the results to fewer fields, and a `filter` to further narrow the search.
 
 ```http
 ### Query the index
@@ -339,14 +339,14 @@ POST {{baseUrl}}/indexes/ny-philharmonic-index/docs/search?api-version=2024-07-0
 
 Two documents are returned in the response.
 
-For filters, you can also use Logical operators (and, or, not) and comparison operators (eq, ne, gt, lt, ge, le). String comparisons are case-sensitive. For more information and examples, see [Create a query](search-query-simple-examples.md).
+For filters, you can also use Logical operators (and, or, not) and comparison operators (eq, ne, gt, lt, ge, le). String comparisons are case -sensitive. For more information and examples, see [Create a query](search-query-simple-examples.md).
 
 > [!NOTE]
-> The `$filter` parameter only works on fields that were marked filterable at the creation of your index.
+> The `$filter` parameter only works on fields that were marked filterable during index creation.
 
 ## Reset and rerun
 
-Indexers can be reset, clearing execution history, which allows a full rerun. The following GET requests are for reset, followed by rerun.
+Indexers can be reset to clear execution history, which allows a full rerun. The following GET requests are for reset, followed by rerun.
 
 ```http
 ### Reset the indexer
@@ -374,7 +374,7 @@ You can use the Azure portal to delete indexes, indexers, and data sources.
 
 ## Next steps
 
-Now that you're familiar with the basics of Azure Blob indexing, let's take a closer look at indexer configuration for JSON blobs in Azure Storage.
+Now that you're familiar with the basics of Azure Blob indexing, take a closer look at indexer configuration for JSON blobs in Azure Storage:
 
 > [!div class="nextstepaction"]
 > [Configure JSON blob indexing](search-howto-index-json-blobs.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "半構造化データのインデックス作成に関するチュートリアルの更新"
}
```

### Explanation
この変更は、`articles/search/search-semi-structured-data.md`ファイルの修正を示しており、半構造化データをインデックス化するためのチュートリアルに関する情報が更新されています。主な改訂は、タイトルや日付の変更、文言の明確化、リンクの修正を含みます。

具体的な変更点は次の通りです：

1. **タイトルの修正**: チュートリアルのタイトルが「Tutorial: Index semi-structured data in JSON blobs」から「Tutorial: Index Semi-Structured Data in JSON Blobs」に変更されており、スタイルの一貫性が保たれています。

2. **日付の更新**: ドキュメントの日付が「12/10/2024」から「03/28/2025」に更新されており、情報が最新であることを示しています。

3. **文言の明確化**: 文中の「how to」が「to how」に修正されるなど、文章がより明確で自然な表現となっています。また、いくつかの表現が一貫性を持つように調整されています。

4. **リンクの修正**: Azureサービスの作成やインデックス作成に関するリンクが更新され、ユーザーが正確な情報にアクセスできるようになっています。

5. **新しい情報の追加**: RESTクライアントやJSONデータファイルのアップロード手順に関する説明が追加され、初心者にも理解しやすいチュートリアルとなっています。例えば、「Visual Studio Code」の使用に関する具体的な手順が明記されています。

この修正により、ユーザーが半構造化データをインデックス化する際の手順をより明確に理解できるようになり、実際の操作に役立つリソースにアクセスしやすくなっています。全体として、この改訂はユーザー向けの指導を一層強化し、Azure AI Searchの利用を促進することを目的としています。

## articles/search/search-sku-manage-costs.md{#item-6e0122}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 02/25/2025
+ms.date: 03/21/2025
 ---
 
 # Plan and manage costs of an Azure AI Search service
@@ -22,7 +22,7 @@ As a first step, estimate your baseline costs by using the Azure pricing calcula
 Azure provides built-in cost management that cuts across service boundaries to provide inclusive cost monitoring and the ability to set budgets and define alerts. The costs of running a search service will vary depending on capacity and which features you use. After you create your search service, optimize capacity so that you pay only for what you need. 
 
 > [!NOTE]
-> Higher capacity partitions are available at the same billing rate on newer services created after April and May 2024. For more information, see [Service limits](search-limits-quotas-capacity.md#service-limits) for partition size upgrades.
+> Higher capacity partitions are available at the same billing rate on newer services created after April and May 2024. For more information about partition size upgrades, see [Service limits](search-limits-quotas-capacity.md#service-limits).
 
 <a name="billable-events"></a>
 
@@ -76,7 +76,7 @@ Follow these guidelines to minimize costs of an Azure AI Search solution.
 
 1. [Scale up](search-capacity-planning.md) for resource-intensive operations like indexing, and then readjust downwards for regular query workloads. If there are predictable patterns to your workloads, you might be able to synchronize scale up to coincide with the expected volume (you would need to write code to automate this).
 
-   When estimating the cost of a search solution, keep in mind that pricing and capacity aren't linear (doubling capacity more than doubles the cost on the same tier). Also, at some point, switching up to a higher tier can give you better and faster performance at roughly the same price point. For more information and an example, see [Upgrade to a Standard S2 tier](search-performance-tips.md#tip-upgrade-to-a-standard-s2-tier).
+   When estimating the cost of a search solution, keep in mind that pricing and capacity aren't linear (doubling capacity more than doubles the cost on the same tier). Also, at some point, switching up to a higher tier can give you better and faster performance at roughly the same price point. For more information and an example, see [Switch to a Standard S2 tier](search-performance-tips.md#tip-switch-to-a-standard-s2-tier).
 
 1. Consider [Azure Web App](/azure/app-service/overview) for your front-end application so that requests and responses stay within the data center boundary.
 
@@ -100,7 +100,7 @@ Search runs as a continuous service. Dedicated resources are always operational,
 
 **Can I change the billing rate (tier) of an existing search service?**
 
-In-place upgrade or downgrade isn't supported. Changing a service tier requires provisioning a new service at the desired tier.
+Existing services can be switched between Basic and Standard (S1, S2, and S3) tiers. Currently, you can only switch from a lower tier to a higher tier, such as going from Basic to S1. For more information, see [Change your pricing tier](search-capacity-planning.md#change-your-pricing-tier).
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search サービスのコスト管理に関するガイドラインの更新"
}
```

### Explanation
この変更は、`articles/search/search-sku-manage-costs.md`ファイルの修正を示しており、Azure AI Searchサービスのコスト管理に関するガイドラインが更新されています。主な改訂は、日付の変更、文言の明確化、情報の正確性の向上を目的とした内容の修正です。

具体的な変更内容は以下の通りです：

1. **日付の更新**: 最後の更新日が「02/25/2025」から「03/21/2025」に変更されており、最新の日付が反映されています。

2. **文言の改善**: 注釈に記載されている「partition size upgrades」に関する表現が、「For more information, see [Service limits]」から「For more information about partition size upgrades, see [Service limits]」に修正され、情報の具体性が向上しています。

3. **表現の明確化**: コストの推定に関するガイドラインの一部で、「Upgrade to a Standard S2 tier」という表現が「Switch to a Standard S2 tier」に変更されており、より正確な内容に修正されています。

4. **料金プランの柔軟性についての修正**: 既存の検索サービスが「In-place upgrade or downgrade isn’t supported」という表現から「Existing services can be switched between Basic and Standard (S1, S2, and S3) tiers」に変更され、基本および標準プラン間の変更ができることが明確にされています。

これらの変更により、Azure AI Searchサービスのコスト管理に関する情報が最新であり、実際の運用に役立つ具体的なガイドラインが提供されています。ユーザーがサービスにおけるコスト管理をより適切に行えるようにするための内容強化が図られています。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -8,26 +8,27 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 01/15/2025
+ms.date: 03/21/2025
 
 ---
 
 # Choose a service tier for Azure AI Search
 
-Part of [creating a search service](search-create-service-portal.md) is choosing a pricing tier (or SKU) that's fixed for the lifetime of the service. In the Azure portal, tier is specified in the **Select Pricing Tier** page when you create the service. In PowerShell or Azure CLI, the tier is specified through the **`-Sku`** parameter.
+Part of [creating a search service](search-create-service-portal.md) is choosing a pricing tier (or SKU). In the Azure portal, tier is specified in the **Select Pricing Tier** page when you create the service. In PowerShell or Azure CLI, the tier is specified through the `-Sku` parameter.
 
-The tier determines:
+The tier determines the:
 
-+ Maximum number of indexes and other objects allowed on the service
-+ Size and speed of partitions (physical storage)
-+ Billable rate as a fixed monthly cost, but also an incremental cost if you add capacity
++ Maximum number of indexes and other objects allowed on the service.
++ Size and speed of partitions (physical storage).
++ Billable rate as a fixed monthly cost, but also an incremental cost if you add capacity.
++ Workload characteristics. Some tiers are optimized for specific workloads.
 
 In a few instances, the tier you choose determines the availability of [premium features](#feature-availability-by-tier).
 
 Billing rates are shown in the Azure portal's **Select Pricing Tier** page. You can check the [pricing page](https://azure.microsoft.com/pricing/details/search/) for regional rates and review [Plan and manage costs](search-sku-manage-costs.md) to learn more about the billing model.
 
 > [!NOTE]
-> Search services created after April 3, 2024 have larger partitions and higher vector quotas at almost every tier. For more information, see [service limits](search-limits-quotas-capacity.md#service-limits).
+> Search services created after April 3, 2024 have larger partitions and higher vector quotas at almost every tier. For more information, see [Service limits](search-limits-quotas-capacity.md#service-limits).
 
 ## Tier descriptions
 
@@ -63,7 +64,7 @@ Currently, several regions are capacity-constrained for specific tiers and can't
 
 ## Feature availability by tier
 
-Most features are available on all tiers, including the free tier. In a few cases, the tier determines the availability of a feature. The following table describes the constraints.
+Most features are available on all tiers, including the Free tier. In a few cases, the tier determines the availability of a feature. The following table describes the constraints.
 
 | Feature | Tier considerations |
 |---------|---------------------|
@@ -88,7 +89,7 @@ Tiers determine the  maximum storage of the service itself, plus the maximum num
 Tier pricing includes details about per-partition storage that ranges from 15 GB for Basic, up to 2 TB for Storage Optimized (L2) tiers. Other hardware characteristics, such as speed of operations, latency, and transfer rates, aren't published, but tiers that are designed for specific solution architectures are built on hardware that has the features to support those scenarios. For more information about partitions, see [Estimate and manage capacity](search-capacity-planning.md) and [Reliability in Azure AI Search](search-reliability.md).
 
 > [!NOTE]
-> Higher capacity partitions became available in selected regions starting in April 2024. A second wave of higher capacity partitions released in May 2024. If you're using an older search service, consider creating a new search service to benefit from more capacity at the same billing rate. For more information, see [Service limits](search-limits-quotas-capacity.md#service-limits). To check the age of your search service, see [How to check service creation date](vector-search-index-size.md#how-to-check-service-creation-date).
+> Higher capacity partitions became available in select regions in April 2024. A second wave of higher capacity partitions was released in May 2024. If you have an older search service, you might be able to [upgrade your service](search-how-to-upgrade.md) to benefit from more capacity at the same billing rate.
 
 ## Billing rates
 
@@ -102,22 +103,30 @@ The following example provides an illustration. Assume a hypothetical billing ra
 
 This billing model is based on the concept of applying the billing rate to the number *search units* (SU) used by a search service. All services are initially provisioned at one SU, but you can increase the SUs by adding either partitions or replicas to handle larger workloads. For more information, see [How to estimate costs of a search service](search-sku-manage-costs.md).
 
-## Tier upgrade or downgrade
+## Tier changes
 
-There's no built-in support to upgrade or downgrade tiers. If you want to switch to a different tier, the approach is:
+Services can be switched between Basic and Standard (S1, S2, and S3) tiers. Currently, you can only switch from a lower tier to a higher tier, such as going from Basic to S1. Your region also can't have capacity constraints on the higher tier. For more information, see [Change your pricing tier](search-capacity-planning.md#change-your-pricing-tier).
 
-+ Create a new search service at the new tier.
+If you want to switch to a lower tier or to a different tier than those previously listed, the approach is:
 
-+ Deploy your search content onto the new service. [Follow this checklist](search-howto-move-across-regions.md#prepare-and-move) to make sure you have all of the content.
+1. Create a new search service at the new tier.
 
-+ Delete the old search service once you're sure it's no longer needed.
+1. Deploy your search content onto the new service. [Follow this checklist](search-howto-move-across-regions.md#prepare-and-move) to make sure you have all of the content.
 
-For large indexes that you don't want to rebuild from scratch, consider using one of the backup and restore samples to move them:[backup and restore sample (C#)](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore/README.md), [backup and restore sample (Python)](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/index-backup-restore/azure-search-backup-and-restore.ipynb), [larget index backup and restore (Python)](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/resumable-index-backup-restore/backup-and-restore.ipynb).
+1. Delete the old search service when you're sure it's no longer needed.
+
+For large indexes that you don't want to rebuild from scratch, consider using one of the backup and restore samples to move them:
+
++ [Backup and restore sample (C#)](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore/README.md)
++ [Backup and restore sample (Python)](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/index-backup-restore/azure-search-backup-and-restore.ipynb)
++ [Largest index backup and restore (Python)](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/resumable-index-backup-restore/backup-and-restore.ipynb)
 
 ## Next steps
 
-The best way to choose a pricing tier is to start with a least-cost tier, and then allow experience and testing inform your decision to keep the service or create a new one at a higher tier. For next steps, we recommend that you create a search service at a tier that can accommodate the level of testing you propose to do, and then review the following guidance for recommendations on estimating cost and capacity.
+The best way to choose a pricing tier is to start with a least-cost tier, and then allow experience and testing to inform your decision to keep the service or switch to a higher tier.
+
+For next steps, we recommend that you create a search service at a tier that can accommodate the level of testing you propose to do, and then review the following guidance on estimating cost and capacity:
 
 + [Create a search service](search-create-service-portal.md)
 + [Estimate costs](search-sku-manage-costs.md)
-+ [Estimate capacity](search-sku-manage-costs.md)
++ [Estimate capacity](search-capacity-planning.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search サービスティアに関するガイドラインの更新"
}
```

### Explanation
この変更は、`articles/search/search-sku-tier.md`ファイルの修正を示しており、Azure AI Searchサービスのティア（サービス階層）についての情報が更新されています。主要な改訂は、日付の変更、文言の明確化、情報の一貫性強化を目的としています。

具体的な変更内容は以下の通りです：

1. **日付の更新**: ドキュメントの日付が「01/15/2025」から「03/21/2025」に変更されており、情報が最新であることを示しています。

2. **文言の明確化**: サービスティアに関する初期の説明文から、「that's fixed for the lifetime of the service」が削除され、よりシンプルな表現に変更されています。また、「最大数のインデックスと他のオブジェクトの許可」が、箇条書き形式で明示されています。

3. **新機能の概要の追加**: サービスティアの特徴として、ワークロードの特性についての説明が追加され、「特定のワークロードに最適化されたティアがある」という内容が含まれています。

4. **表現の統一**: 一部の単語が一貫性を持つように修正されており、特に「Free tier」という表現が一貫して用いられるようになっています。

5. **料金変更の手続きの更新**: ティアの変更に関するセクションがより詳細に説明され、サービスの切り替えの手順が明確に示されています。また、バックアップと復元のサンプルの具体的なリンクが改良され、ユーザーが手軽にアクセスできるよう配慮されています。

6. **次のステップの推奨**: ティアの選択に関する推奨が修正され、テストを通じて最適なティアを選ぶプロセスが明確にされています。また、次のステップに関連するリンクが整理されています。

これにより、Azure AI Searchサービスのティア選択に関するガイドが更新され、ユーザーが必要な情報を簡単に見つけることができるよう改善されています。このように、ユーザーにとって役立つ実用的で最新の情報が提供されることが目的とされています。

## articles/search/search-synapseml-cognitive-services.md{#item-dcc36f}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Tutorial: Index at scale (Spark)'
+title: 'Tutorial: Index at Scale (Spark)'
 titleSuffix: Azure AI Search
 description: Search big data from Apache Spark that's been transformed by SynapseML. Load invoices into data frames, apply machine learning, and then send output to a generated search index.
 
@@ -10,52 +10,52 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: tutorial
-ms.date: 01/30/2025
+ms.date: 03/28/2025
 ---
 
 # Tutorial: Index large data from Apache Spark using SynapseML and Azure AI Search
 
-In this Azure AI Search tutorial, learn how to index and query large data loaded from a Spark cluster. Set up a Jupyter Notebook that performs the following actions:
+In this Azure AI Search tutorial, you learn how to index and query large data loaded from a Spark cluster. You set up a Jupyter Notebook to:
 
 > [!div class="checklist"]
 > + Load various forms (invoices) into a data frame in an Apache Spark session
-> + Analyze them to determine their features
+> + Analyze the forms to determine their features
 > + Assemble the resulting output into a tabular data structure
 > + Write the output to a search index hosted in Azure AI Search
 > + Explore and query over the content you created
 
-This tutorial takes a dependency on [SynapseML](https://microsoft.github.io/SynapseML/), an open source library that supports massively parallel machine learning over big data. In SynapseML, search indexing and machine learning are exposed through *transformers* that perform specialized tasks. Transformers tap into a wide range of AI capabilities. In this exercise, use the **AzureSearchWriter** APIs for analysis and AI enrichment.
+This tutorial takes a dependency on [SynapseML](https://microsoft.github.io/SynapseML/), an open-source library that supports massively parallel machine learning over big data. In SynapseML, search indexing and machine learning are exposed through *transformers* that perform specialized tasks. Transformers tap into a wide range of AI capabilities. In this exercise, you use the **AzureSearchWriter** APIs for analysis and AI enrichment.
 
 Although Azure AI Search has native [AI enrichment](cognitive-search-concept-intro.md), this tutorial shows you how to access AI capabilities outside of Azure AI Search. By using SynapseML instead of indexers or skills, you're not subject to data limits or other constraints associated with those objects.
 
 > [!TIP]
-> Watch a short video of this demo at [https://www.youtube.com/watch?v=iXnBLwp7f88](https://www.youtube.com/watch?v=iXnBLwp7f88). The video expands on this tutorial with more steps and visuals.
+> Watch a [short video of this demo](https://www.youtube.com/watch?v=iXnBLwp7f88). The video expands on this tutorial with more steps and visuals.
 
 ## Prerequisites
 
 You need the `synapseml` library and several Azure resources. If possible, use the same subscription and region for your Azure resources and put everything into one resource group for simple cleanup later. The following links are for portal installs. The sample data is imported from a public site.
 
 + [SynapseML package](https://microsoft.github.io/SynapseML/docs/Get%20Started/Install%20SynapseML/#python) <sup>1</sup>
-+ [Azure AI Search](search-create-service-portal.md) (any tier), with an **API Kind** of `AIServices` <sup>2</sup> 
-+ [Azure AI services multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills?pivots=azportal) (any tier) <sup>3</sup>
-+ [Azure Databricks](/azure/databricks/scenarios/quickstart-create-databricks-workspace-portal?tabs=azure-portal) (any tier) with Apache Spark 3.3.0 runtime<sup>4</sup>
++ [Azure AI Search](search-create-service-portal.md) (any tier) <sup>2</sup> 
++ [Azure AI services multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills?pivots=azportal) (any tier) with an **API Kind** of `AIServices` <sup>3</sup>
++ [Azure Databricks](/azure/databricks/scenarios/quickstart-create-databricks-workspace-portal?tabs=azure-portal) (any tier) with Apache Spark 3.3.0 runtime <sup>4</sup>
 
 <sup>1</sup> This link resolves to a tutorial for loading the package.
 
-<sup>2</sup> You can use the free search tier to index the sample data, but [choose a higher tier](search-sku-tier.md) if your data volumes are large. For billable tiers, provide the [search API key](search-security-api-keys.md#find-existing-keys) in the [Set up dependencies](#step-2-set-up-dependencies) step further on.
+<sup>2</sup> You can use the Free tier to index the sample data, but [choose a higher tier](search-sku-tier.md) if your data volumes are large. For billable tiers, provide the [search API key](search-security-api-keys.md#find-existing-keys) in the [Set up dependencies](#set-up-dependencies) step further on.
 
-<sup>3</sup> This tutorial uses Azure AI Document Intelligence and Azure AI Translator. In the instructions that follow, provide a [multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills?pivots=azportal) key and the region. The same key works for both services. **It's important that you use an Azure AI services multi-service account of API kind of `AIServices` for this tutorial**. You can check the API kind in the Azure portal on the Overview section of your Azure AI services multi-service account page. For more information about API kind, see [Attach an Azure AI services multi-service resource in Azure AI Search](cognitive-search-attach-cognitive-services.md).
+<sup>3</sup> This tutorial uses Azure AI Document Intelligence and Azure AI Translator. In the instructions that follow, provide a [multi-service account](/azure/ai-services/multi-service-resource#azure-ai-services-resource-for-azure-ai-search-skills?pivots=azportal) key and the region. The same key works for both services. **For this tutorial, it's important that you use an Azure AI services multi-service account with an API kind of `AIServices`**. You can check the API kind in the Azure portal on the Overview section of your Azure AI services multi-service account page. For more information about API kind, see [Attach an Azure AI services multi-service resource in Azure AI Search](cognitive-search-attach-cognitive-services.md).
 
 <sup>4</sup> In this tutorial, Azure Databricks provides the Spark computing platform. We used the [portal instructions](/azure/databricks/scenarios/quickstart-create-databricks-workspace-portal?tabs=azure-portal) to set up the cluster and workspace.
 
 > [!NOTE]
-> All of the above Azure resources support security features in the Microsoft Identity platform. For simplicity, this tutorial assumes key-based authentication, using endpoints and keys copied from the Azure portal pages of each service. If you implement this workflow in a production environment, or share the solution with others, remember to replace hard-coded keys with integrated security or encrypted keys.
+> The preceding Azure resources support security features in the Microsoft Identity platform. For simplicity, this tutorial assumes key-based authentication, using endpoints and keys copied from the Azure portal pages of each service. If you implement this workflow in a production environment or share the solution with others, remember to replace hard-coded keys with integrated security or encrypted keys.
 
-## Step 1: Create a Spark cluster and notebook
+## Create a Spark cluster and notebook
 
-In this section, create a cluster, install the `synapseml` library, and create a notebook to run the code.
+In this section, you create a cluster, install the `synapseml` library, and create a notebook to run the code.
 
-1. In Azure portal, find your Azure Databricks workspace and select **Launch workspace**.
+1. In the Azure portal, find your Azure Databricks workspace and select **Launch workspace**.
 
 1. On the left menu, select **Compute**.
 
@@ -67,7 +67,7 @@ In this section, create a cluster, install the `synapseml` library, and create a
 
    :::image type="content" source="media/search-synapseml-cognitive-services/cluster-green-dot.png" alt-text="Screenshot of a Data Bricks compute page with a green dot by the cluster name.":::
 
-1. Install the `synapseml` library after the cluster is created:
+1. After the cluster is created, install the `synapseml` library:
 
    1. Select **Libraries** from the tabs at the top of the cluster's page.
 
@@ -77,7 +77,7 @@ In this section, create a cluster, install the `synapseml` library, and create a
 
    1. Select **Maven**.
 
-   1. In Coordinates, search for or type `com.microsoft.azure:synapseml_2.12:1.0.9`
+   1. In **Coordinates**, search for `com.microsoft.azure:synapseml_2.12:1.0.9`.
 
    1. Select **Install**.
 
@@ -89,17 +89,17 @@ In this section, create a cluster, install the `synapseml` library, and create a
 
 1. Give the notebook a name, select **Python** as the default language, and select the cluster that has the `synapseml` library.
 
-1. Create seven consecutive cells. You use these to paste in code in the following sections.
+1. Create seven consecutive cells. In the following sections, you paste code in these cells.
 
    :::image type="content" source="media/search-synapseml-cognitive-services/create-seven-cells.png" alt-text="Screenshot of the notebook with placeholder cells." border="true":::
 
-## Step 2: Set up dependencies
+## Set up dependencies
 
-Paste the following code into the first cell of your notebook. 
+Paste the following code into the first cell of your notebook.
 
-Replace the placeholders with endpoints and access keys for each resource. Provide a name for a new search index that's created for you. No other modifications are required, so run the code when you're ready.
+Replace the placeholders with endpoints and access keys for each resource. Provide a name for a new search index to be created for you. No other modifications are required, so run the code when you're ready.
 
-This code imports multiple packages and sets up access to the Azure resources used in this workflow.
+This code imports multiple packages and sets up access to the Azure resources used in this tutorial.
 
 ```python
 import os
@@ -115,11 +115,11 @@ search_key = "placeholder-search-service-admin-api-key"
 search_index = "placeholder-for-new-search-index-name"
 ```
 
-## Step 3: Load data into Spark
+## Load data into Spark
 
 Paste the following code into the second cell. No modifications are required, so run the code when you're ready.
 
-This code loads a few external files from an Azure storage account. The files are various invoices, and they're read into a data frame.
+This code loads a few external files from an Azure storage account. The files are various invoices that are read into a data frame.
 
 ```python
 def blob_to_url(blob):
@@ -141,7 +141,7 @@ df2 = (spark.read.format("binaryFile")
 display(df2)
 ```
 
-## Step 4: Add document intelligence
+## Add document intelligence
 
 Paste the following code into the third cell. No modifications are required, so run the code when you're ready.
 
@@ -163,15 +163,15 @@ analyzed_df = (AnalyzeInvoices()
 display(analyzed_df)
 ```
 
-The output from this step should look similar to the next screenshot. Notice how the forms analysis is packed into a densely structured column, which is difficult to work with. The next transformation resolves this issue by parsing the column into rows and columns.
+The output should look similar to the following screenshot. Notice how the forms analysis is packed into a densely structured column, which is difficult to work with. The next transformation resolves this issue by parsing the column into rows and columns.
 
 :::image type="content" source="media/search-synapseml-cognitive-services/analyze-forms-output.png" alt-text="Screenshot of the AnalyzeInvoices output." border="true":::
 
-## Step 5: Restructure document intelligence output
+## Restructure document intelligence output
 
 Paste the following code into the fourth cell and run it. No modifications are required.
 
-This code loads [FormOntologyLearner](https://mmlspark.blob.core.windows.net/docs/0.10.0/pyspark/synapse.ml.cognitive.html#module-synapse.ml.cognitive.FormOntologyTransformer), a transformer that analyzes the output of Document Intelligence transformers and infers a tabular data structure. The output of AnalyzeInvoices is dynamic and varies based on the features detected in your content. Furthermore, the transformer consolidates output into a single column. Because the output is dynamic and consolidated, it's difficult to use in downstream transformations that require more structure.
+This code loads [FormOntologyLearner](https://mmlspark.blob.core.windows.net/docs/0.10.0/pyspark/synapse.ml.cognitive.html#module-synapse.ml.cognitive.FormOntologyTransformer), a transformer that analyzes the output of Document Intelligence transformers and infers a tabular data structure. The output of AnalyzeInvoices is dynamic and varies based on the features detected in your content. Furthermore, the transformer consolidates the output into a single column. Because the output is dynamic and consolidated, it's difficult to use in downstream transformations that require more structure.
 
 FormOntologyLearner extends the utility of the AnalyzeInvoices transformer by looking for patterns that can be used to create a tabular data structure. Organizing the output into multiple columns and rows makes the content consumable in other transformers, like AzureSearchWriter.
 
@@ -193,11 +193,11 @@ Notice how this transformation recasts the nested fields into a table, which ena
 
 :::image type="content" source="media/search-synapseml-cognitive-services/form-ontology-learner-output.png" alt-text="Screenshot of the FormOntologyLearner output." border="true":::
 
-## Step 6: Add translations
+## Add translations
 
 Paste the following code into the fifth cell. No modifications are required, so run the code when you're ready.
 
-This code loads [Translate](https://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/AI%20Services/Overview/#translator-sample), a transformer that calls the Azure AI Translator service in Azure AI services. The original text, which is in English in the "Description" column, is machine-translated into various languages. All of the output is consolidated into "output.translations" array.
+This code loads [Translate](https://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/AI%20Services/Overview/#translator-sample), a transformer that calls the Azure AI Translator service in Azure AI services. The original text, which is in English in the "Description" column, is machine-translated into various languages. All of the output is consolidated into the "output.translations" array.
 
 ```python
 from synapse.ml.cognitive import Translate
@@ -223,11 +223,11 @@ display(translated_df)
 > 
 > :::image type="content" source="media/search-synapseml-cognitive-services/translated-strings.png" alt-text="Screenshot of table output, showing the Translations column." border="true":::
 
-## Step 7: Add a search index with AzureSearchWriter
+## Add a search index with AzureSearchWriter
 
-Paste the following code in the sixth cell and then run it. No modifications are required.
+Paste the following code in the sixth cell and run it. No modifications are required.
 
-This code loads [AzureSearchWriter](https://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/AI%20Services/Overview/#azure-cognitive-search-sample). It consumes a tabular dataset and infers a search index schema that defines one field for each column. Because the translations structure is an array, it's articulated in the index as a complex collection with subfields for each language translation. The generated index has a document key and use the default values for fields created using the [Create Index REST API](/rest/api/searchservice/indexes/create).
+This code loads [AzureSearchWriter](https://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/AI%20Services/Overview/#azure-cognitive-search-sample). It consumes a tabular dataset and infers a search index schema that defines one field for each column. Because the translations structure is an array, it's articulated in the index as a complex collection with subfields for each language translation. The generated index has a document key and uses the default values for fields created using the [Create Index REST API](/rest/api/searchservice/indexes/create).
 
 ```python
 from synapse.ml.cognitive import *
@@ -243,21 +243,21 @@ from synapse.ml.cognitive import *
     ))
 ```
 
-You can check the search service pages in Azure portal to explore the index definition created by AzureSearchWriter.
+To explore the index definition created by AzureSearchWriter, check the search service pages in the Azure portal.
 
 > [!NOTE]
-> If you can't use default search index, you can provide an external custom definition in JSON, passing its URI as a string in the "indexJson" property. Generate the default index first so that you know which fields to specify, and then follow with customized properties if you need specific analyzers, for example.
+> If you can't use the default search index, you can provide an external custom definition in JSON, passing its URI as a string in the "indexJson" property. Generate the default index first so that you know which fields to specify, and then follow with customized properties if you need specific analyzers, for example.
 
-## Step 8: Query the index
+## Query the index
 
-Paste the following code into the seventh cell and then run it. No modifications are required, except that you might want to vary the syntax or try more examples to further explore your content:
+Paste the following code into the seventh cell and run it. No modifications are required, except that you might want to vary the syntax or try more examples to further explore your content:
 
 + [Query syntax](query-simple-syntax.md)
 + [Query examples](search-query-simple-examples.md)
 
 There's no transformer or module that issues queries. This cell is a simple call to the [Search Documents REST API](/rest/api/searchservice/documents/search-post). 
 
-This particular example is searching for the word "door" (`"search": "door"`). It also returns a "count" of the number of matching documents, and selects just the contents of the "Description' and "Translations" fields for the results. If you want to see the full list of fields, remove the "select" parameter.
+This particular example is searching for the word "door" (`"search": "door"`). It also returns a "count" of the number of matching documents and selects just the contents of the "Description' and "Translations" fields for the results. If you want to see the full list of fields, remove the "select" parameter.
 
 ```python
 import requests
@@ -278,7 +278,7 @@ You can find and manage resources in the Azure portal, using the **All resources
 
 ## Next steps
 
-In this tutorial, you learned about the [AzureSearchWriter](https://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/AI%20Services/Overview/#azure-cognitive-search-sample) transformer in SynapseML, which is a new way of creating and loading search indexes in Azure AI Search. The transformer takes structured JSON as an input. The FormOntologyLearner can provide the necessary structure for output produced by the Document Intelligence transformers in SynapseML.
+In this tutorial, you learned about the [AzureSearchWriter](https://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/AI%20Services/Overview/#azure-cognitive-search-sample) transformer in SynapseML, which is a new way of creating and loading search indexes in Azure AI Search. The transformer takes structured JSON as an input. FormOntologyLearner can provide the necessary structure for output produced by the Document Intelligence transformers in SynapseML.
 
 As a next step, review the other SynapseML tutorials that produce transformed content you might want to explore through Azure AI Search:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SynapseML と Azure AI Search を使用した大規模データのインデックス作成チュートリアルの更新"
}
```

### Explanation
この変更は、`articles/search/search-synapseml-cognitive-services.md`ファイルの修正を示しており、SynapseMLを使用してAzure AI Searchに大規模データをインデックスする方法に関するチュートリアルが更新されています。この改訂の主な目的は、文言の改善、明確化、情報の一貫性を持たせることです。

具体的な変更内容は以下の通りです：

1. **タイトルの修正**: チュートリアルのタイトルが「Index at scale (Spark)」から「Index at Scale (Spark)」に変更され、表示の一貫性が向上しています。

2. **日付の更新**: 最終更新日が「01/30/2025」から「03/28/2025」に変更されているため、情報が最新となっています。

3. **文言の明確化**: チュートリアルの導入部において、「learn how to index and query large data loaded from a Spark cluster」が「you learn how to index and query large data loaded from a Spark cluster」に変更され、能動的な表現になっています。

4. **箇条書きの整理**: チュートリアル内のステップが明確化され、一貫したフォーマットで情報が整理されています。特に、特定のタスクが箇条書き形式で整理され、内容が読みやすくなっています。

5. **URLの更新**: 一部のリンクが修正され、例えば「Azure AI services multi-service account」に関連するリンクなどが具体的に記載されています。

6. **セクション見出しの修正**: 各セクション見出しが命令形から名詞形に変更され、より分かりやすくなっています。

7. **ノートの改良**: 注記の内容が簡素化され、ユーザーが必要な情報をすぐに理解できるように改善されています。

8. **全体的な文書の整頓**: コードや手順に対する説明が簡潔になり、一貫した表現が保たれています。例えば、「Replace the placeholders with endpoints and access keys for each resource」という文がクリアで、一貫して維持されています。

これらの変更により、ユーザーはSynapseMLを利用したAzure AI Searchに関するチュートリアルをよりスムーズに理解し、実行することができるようになることを目的としています。全体として、読みやすさと情報の正確性が向上しており、初心者から上級者まで幅広いユーザーにとって有用なリソースとなっています。

## articles/search/semantic-how-to-configure.md{#item-7a92a6}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 12/10/2024
+ms.date: 04/04/2025
 ---
 
 # Configure semantic ranker and return captions in search results
@@ -44,6 +44,8 @@ You can specify a semantic configuration on new or existing indexes, using any o
 
 A *semantic configuration* is a section in your index that establishes field inputs for semantic ranking. You can add or update a semantic configuration at any time, no rebuild necessary. If you create multiple configurations, you can specify a default. At query time, specify a semantic configuration on a [query request](semantic-how-to-query-request.md), or leave it blank to use the default.
 
+You can create up to 100 semantic configurations in a single index.
+
 A semantic configuration has a name and the following properties:
 
 | Property | Characteristics |
@@ -158,6 +160,60 @@ SearchIndex searchIndex = new(indexName)
 
 ---
 
+## Opt in for prerelease semantic ranking models
+
+[!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
+
+Starting in [2025-03-01-preview REST APIs](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-03-01-preview&preserve-view=true) and in Azure SDKs that provide the property, you can optionally configure an index to use prerelease semantic ranking models if one is deployed in your region. There's no mechanism for knowing if a prerelease is available, or if it was used on specific query. For this reason, we recommend that you use this property in test environments, and only if you're interested in trying out the very latest semantic ranking models.
+
+The configuration property is `"flightingOptIn": true`, and it's set in the semantic configuration section of an index. The property is null or false by default. You can set it true on a create or update request at any time, and it affects semantic queries moving forward, assuming the query stipulates a semantic configuration that includes the property.
+
+```rest
+PUT https://myservice.search.windows.net/indexes('hotels')?allowIndexDowntime=False&api-version=2025-03-01-preview
+
+{
+  "name": "hotels",
+  "fields": [ ],
+  "scoringProfiles": [ ],
+  "defaultScoringProfile": "geo",
+  "suggesters": [ ],
+  "analyzers": [ ],
+  "corsOptions": { },
+  "encryptionKey": { },
+  "similarity": { },
+  "semantic": {
+    "configurations": [
+      {
+        "name": "semanticHotels",
+        "prioritizedFields": {
+          "titleField": {
+            "fieldName": "hotelName"
+          },
+        "prioritizedContentFields": [
+            {
+              "fieldName": "description"
+            },
+            {
+              "fieldName": "description_fr"
+            }
+          ],
+        "prioritizedKeywordsFields": [
+            {
+              "fieldName": "tags"
+            },
+            {
+              "fieldName": "category"
+            }
+          ],
+        "flightingOptIn": true
+        }
+      }
+    ]
+  },
+  "vectorSearch": {  }
+}
+```
+
 ## Next steps
 
 Test your semantic configuration by running a semantic query.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーの構成方法に関するガイドの更新"
}
```

### Explanation
この変更は、`articles/search/semantic-how-to-configure.md`ファイルの修正を示しており、Azure AI Searchにおけるセマンティックランカーの構成方法に関するガイドが更新されています。この更新の主な目的は、情報の追加や明確化を通じて、ユーザーがより効果的にセマンティック機能を利用できるようにすることです。

具体的な変更内容は以下の通りです：

1. **日付の更新**: 最終更新日が「12/10/2024」から「04/04/2025」に変更され、最新の情報が反映されています。

2. **セマンティック構成に関する情報の追加**: 新たに「1つのインデックスに最大100のセマンティック構成を作成できる」という情報が追加されており、ユーザーがセマンティック設定の能力を理解しやすくなっています。

3. **プレビュー版のセマンティックランキングモデルのオプトイン機能の追加**: セマンティックランカーに対する新しいオプションとして、プレビュー版のセマンティックランキングモデルを使用する統合が追加されました。このセクションでは、どのようにしてこのオプションを設定するか、関連するREST APIの例を含めて具体的に説明されています。

4. **REST APIリクエストの具体例**: プレビュー版のセマンティックランキングモデルを設定するためのREST APIリクエストの具体的な例が追加され、どのようにインデックスを変更するかの基本が明確に示されています。

5. **全体的な文書の整頓**: 変更内容全体にわたって、セクション見出しや文の流れが整理され、情報が明確に伝わるようになっています。また、関連する情報や機能についても説明が追加されています。

これにより、ユーザーはセマンティックランカーの構成方法についての理解を深め、新たに提供される機能を利用しやすくなることを目指しています。全体的に、ユーザーエクスペリエンスの向上が意図された更新です。

## articles/search/semantic-how-to-enable-disable.md{#item-71ac1e}

<details>
<summary>Diff</summary>
````diff
@@ -10,12 +10,12 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 01/28/2025
+ms.date: 03/31/2025
 ---
 
 # Enable or disable semantic ranker
 
-Semantic ranker is a premium feature billed by usage. By default, semantic ranker is turned on when you create a new billable search service, but anyone with *Contributor* permissions can disable it or change the billing plan. If you don't want anyone to use the feature, you can [disable it service-wide using the management REST API](#disable-semantic-ranker-using-the-rest-api).
+Semantic ranker is a premium feature billed by usage. By default, semantic ranker is enabled on a new billable search service and it's configured for the free plan, but anyone with *Contributor* permissions can disable it or change the billing plan. If you don't want anyone to use the feature, you can [disable it service-wide using the management REST API](#disable-semantic-ranker-using-the-rest-api).
 
 ## Check availability
 
@@ -45,7 +45,7 @@ To enable semantic ranker using the REST API, you can use the [Create or Update
 
 Management REST API calls are authenticated through Microsoft Entra ID. For instructions on how to authenticate, see [Manage your Azure AI Search service with REST APIs](search-manage-rest.md).
 
-* Management REST API version 2023-11-01 provides the configuration property.
+* Management REST API version 2023-11-01 or later provides the configuration property.
 
 * *Owner* or *Contributor* permissions are required to enable or disable features. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーの有効化と無効化に関するガイドの更新"
}
```

### Explanation
この変更は、`articles/search/semantic-how-to-enable-disable.md`ファイルの修正を示しており、Azure AI Searchにおけるセマンティックランカーの有効化および無効化に関するガイドが更新されています。更新の目的は、ユーザーに対する情報の明確化および最新化です。

具体的な変更内容は以下の通りです：

1. **日付の更新**: 最終更新日が「01/28/2025」から「03/31/2025」に変更され、最新の情報が反映されています。

2. **セマンティックランカーのデフォルト設定の明確化**: 「新しい課金サービスを作成する際にデフォルトで有効になる」という記述が、「新しい有料検索サービスではデフォルトで有効で、無料プランに設定されています」というように具体化され、ユーザーがセマンティックランカーの初期設定を理解しやすくなっています。

3. **REST APIのバージョンに関する表記の変更**: 「2023-11-01のManagement REST APIバージョンが構成プロパティを提供する」という記述が、「2023-11-01以降のManagement REST APIバージョンが構成プロパティを提供する」という記述に変更され、APIバージョンに対する将来的な互換性が示されています。

これにより、セマンティックランカーの利用に関するガイドがより具体的で理解しやすくなり、利用者が機能を効果的に管理できるように改善されています。全体的に、情報の一貫性とクリアさを向上させることが目的とされています。

## articles/search/semantic-how-to-query-request.md{#item-85530d}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: how-to
-ms.date: 02/18/2025
+ms.date: 03/31/2025
 ---
 
 # Add semantic ranking to queries in Azure AI Search
@@ -46,7 +46,7 @@ You can use any of the following tools and SDKs to build a query that uses seman
 
 A few query capabilities bypass relevance scoring, which makes them incompatible with semantic ranking. If your query logic includes the following features, you can't semantically rank your results:
 
-+ A query with `search=*` or an empty search string, such as pure filter-only query, won't work because there's nothing to measure semantic relevance against and so the search scores are zero. The query must provide terms or phrases that can be evaluated during processing.
++ A query with `search=*` or an empty search string, such as pure filter-only query, won't work because there's nothing to measure semantic relevance against and so the search scores are zero. The query must provide terms or phrases that can be evaluated during processing, and that produces search documents that are scored for relevance. Scored results are inputs to the semantic ranker.
 
 + Sorting (orderBy clauses) on specific fields overrides search scores and a semantic score. Given that the semantic score is supposed to provide the ranking, adding an orderby clause results in an HTTP 400 error if you apply semantic ranking over ordered results.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティッククエリリクエストに関するガイドの更新"
}
```

### Explanation
この変更は、`articles/search/semantic-how-to-query-request.md`ファイルの修正を示しており、Azure AI Searchにおけるセマンティックランキングをクエリに追加する方法に関するガイドが更新されています。主な目的は、セマンティックランキング機能に関する情報を明確にし、最新化することです。

具体的な変更内容は以下の通りです：

1. **日付の更新**: 最終更新日が「02/18/2025」から「03/31/2025」に変更され、新しい情報が反映されています。

2. **セマンティックランキングに関するクエリの要件の具体化**: セマンティックランキングに関連しないクエリの要件がより詳細に説明されています。具体的には、検索条件が `search=*` または空の検索文字列を含む場合、セマンティック関連性を評価できないため、検索スコアがゼロになることが強調されています。この点が、「検索ドキュメントが関連性のためにスコアリングされる必要がある」という追加の説明により、ユーザーに対する理解を深めています。

3. **ソート機能の影響についての説明の追加**: ソート（`orderBy`句）が特定のフィールドで行われると、検索スコアおよびセマンティックスコアを上書きするため、セマンティックランキングが適用された結果に対してHTTP 400エラーが発生する可能性があることが説明されています。この変更により、ユーザーがクエリを設計する際の注意点が明確になります。

全体として、この更新はユーザーがセマンティックランキングを適切に利用するために必要な情報を提供し、クエリの設計における重要なポイントを強調することを目的としています。

## articles/search/semantic-how-to-query-rewrite.md{#item-3e168f}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2024
   - references_regions
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 03/31/2025
 ---
 
 # Rewrite queries with semantic ranker in Azure AI Search (Preview)
@@ -21,7 +21,8 @@ Query rewriting is the process of transforming a user's query into a more effect
 
 Query rewriting improves results from [semantic ranking](search-get-started-semantic.md) by correcting typos or spelling errors in user queries, and expanding queries with synonyms.
 
-Search with query rewriting works like this: 
+Search with query rewriting works like this:
+
 - The user query is sent via the `search` property in the request.
 - The search service sends the search query (or a variation of it) to a generative model that generates alternative queries.
 - The search service uses the original query and the rewritten queries to retrieve search results.
@@ -33,31 +34,25 @@ Query rewriting is an optional feature. Without query rewriting, the search serv
 
 ## Prerequisites
 
-+ A search service, Basic tier or higher.
-
-> [!NOTE]
-> Query rewriting is currently available in the North Europe, and Southeast Asia regions.
-
-+ Your search service must have [semantic ranker enabled](semantic-how-to-enable-disable.md). Review [semantic ranking](semantic-search-overview.md) if you need an introduction to the feature. 
+- A search service, Basic tier or higher, in **North Europe** or **Southeast Asia**.
 
-> [!IMPORTANT]
-> Semantic ranker is currently required for query rewriting.
+- [Semantic ranker must be enabled](semantic-how-to-enable-disable.md). It's enabled by default on newer search services. Review [semantic ranking](semantic-search-overview.md) if you need an introduction to the feature. 
 
-+ An existing search index with a [semantic configuration](semantic-how-to-configure.md) and rich text content. The examples in this guide use the [hotels-sample-index](search-get-started-portal.md) sample data to demonstrate query rewriting. You can use your own data and index to test query rewriting.
+- An existing search index with a [semantic configuration](semantic-how-to-configure.md) and rich text content. The examples in this guide use the [hotels-sample-index](search-get-started-portal.md) sample data to demonstrate query rewriting. You can use your own data and index to test query rewriting.
 
-+ You need a web client that supports REST API requests. The examples in this guide were tested with [Visual Studio Code](https://code.visualstudio.com/download) with the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension. 
+- To follow the instructions in this article, you need a web client that supports REST API requests. The examples in this guide were tested with [Visual Studio Code](https://code.visualstudio.com/download) with the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension. 
 
 > [!TIP]
 > Content that includes explanations or definitions work best for semantic ranking. 
 
 ## Make a search request with query rewrites
 
-In this REST API example, we use [Search Documents](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-11-01-preview&branch=searchindex202411&preserve-view=true) to formulate the request. For more information about the request and response properties, see the [API reference documentation](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-11-01-preview&branch=searchindex202411&preserve-view=true).
+In this REST API example, use [Search Documents (preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-03-01-preview&branch=searchindex202503&preserve-view=true) to formulate the request.
 
 1. Paste the following request into a web client as a template. 
 
     ```http
-    POST https://[search-service-name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2024-11-01-preview
+    POST https://[search-service-name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-03-01-preview
     {
         "search": "newer hotel near the water with a great restaurant",
         "semanticConfiguration":"en-semantic-config",
@@ -69,24 +64,24 @@ In this REST API example, we use [Search Documents](/rest/api/searchservice/docu
     }
     ```
 
-    - You replace `search-service-name` with your search service name.
-    - You replace `hotels-sample-index` with your index name if it's different. 
-    - We set "search" to a full text search query. The search property is required for query rewriting, unless you specify [vector queries](#vector-queries-with-query-rewrite). If you specify vector queries, then the "search" text must match the `"text"` property of the `"vectorQueries"` object. Your search string can support either the [simple syntax](query-simple-syntax.md) or [full Lucene syntax](query-lucene-syntax.md).
-    - We set "semanticConfiguration" to a [predefined semantic configuration](semantic-how-to-configure.md) embedded in your index.
-    - We set "queryType" to "semantic". We either need to set "queryType" to "semantic" or include a nonempty "semanticQuery" property in the request. [Semantic ranking](semantic-search-overview.md) is required for query rewriting.
-    - We set "queryRewrites" to "generative|count-5" to get up to five query rewrites. You can set the count to any value between 1 and 10. 
-    - Since we requested query rewrites by setting the "queryRewrites" property, we must set "queryLanguage" to the search text language. The Search service uses the same language for the query rewrites. In this example, we use "en-US". The supported locales are: 
+    - Replace `search-service-name` with your search service name.
+    - Replace `hotels-sample-index` with your index name if it's different. 
+    - Set "search" to a full text search query. The search property is required for query rewriting, unless you specify [vector queries](#vector-queries-with-query-rewrite). If you specify vector queries, then the "search" text must match the `"text"` property of the `"vectorQueries"` object. Your search string can support either the [simple syntax](query-simple-syntax.md) or [full Lucene syntax](query-lucene-syntax.md).
+    - Set "semanticConfiguration" to a [predefined semantic configuration](semantic-how-to-configure.md) embedded in your index.
+    - Set "queryType" to "semantic". You either need to set "queryType" to "semantic" or include a nonempty "semanticQuery" property in the request. [Semantic ranking](semantic-search-overview.md) is required for query rewriting.
+    - Set "queryRewrites" to "generative|count-5" to get up to five query rewrites. You can set the count to any value between 1 and 10. 
+    - Since you requested query rewrites by setting the "queryRewrites" property, you must set "queryLanguage" to the search text language. The search service uses the same language for the query rewrites. In this example, you use "en-US". The supported locales are: 
         `en-AU`, `en-CA`, `en-GB`, `en-IN`, `en-US`, `ar-EG`, `ar-JO`, `ar-KW`, `ar-MA`, `ar-SA`, `bg-BG`, `bn-IN`, `ca-ES`, `cs-CZ`, `da-DK`, `de-DE`, `el-GR`, `es-ES`, `es-MX`, `et-EE`, `eu-ES`, `fa-AE`, `fi-FI`, `fr-CA`, `fr-FR`, `ga-IE`, `gl-ES`, `gu-IN`, `he-IL`, `hi-IN`, `hr-BA`, `hr-HR`, `hu-HU`, `hy-AM`, `id-ID`, `is-IS`, `it-IT`, `ja-JP`, `kn-IN`, `ko-KR`, `lt-LT`, `lv-LV`, `ml-IN`, `mr-IN`, `ms-BN`, `ms-MY`, `nb-NO`, `nl-BE`, `nl-NL`, `no-NO`, `pa-IN`, `pl-PL`, `pt-BR`, `pt-PT`, `ro-RO`, `ru-RU`, `sk-SK`, `sl-SL`, `sr-BA`, `sr-ME`, `sr-RS`, `sv-SE`, `ta-IN`, `te-IN`, `th-TH`, `tr-TR`, `uk-UA`, `ur-PK`, `vi-VN`, `zh-CN`, `zh-TW`.
-    - We set "debug" to "queryRewrites" to get the query rewrites in the response. 
+    - Set "debug" to "queryRewrites" to get the query rewrites in the response. 
   
       > [!TIP]
       > Only set `"debug": "queryRewrites"` for testing purposes. For better performance, don't use debug in production.
 
-    - We set "top" to 1 to return only the top search result. 
-    
+    - Set "top" to 1 to return only the top search result. 
+  
 1. Send the request to execute the query and return results.
 
-Next, we evaluate the search results with the query rewrites.
+Next, you evaluate the search results with the query rewrites.
 
 ## Evaluate the response
 
@@ -145,8 +140,9 @@ Here's an example of a response that includes query rewrites:
 ```
 
 Here are some key points to note:
-- Because we set the "debug" property to "queryRewrites" for testing, the response includes a `@search.debug` object with the text input query and query rewrites. 
-- Because we set the "queryRewrites" property to "generative|count-5", the response includes up to five query rewrites.
+
+- Because you set the "debug" property to "queryRewrites" for testing, the response includes a `@search.debug` object with the text input query and query rewrites. 
+- Because you set the "queryRewrites" property to "generative|count-5", the response includes up to five query rewrites.
 - The `"inputQuery"` value is the query sent to the generative model for query rewriting. The input query isn't always the same as the user's `"search"` query.
 
 Here's an example of a response without query rewrites. 
@@ -201,13 +197,13 @@ Here's an example of a response without query rewrites.
 
 You can include vector queries in your search request to combine keyword search and vector search into a single request and a unified response.
 
-Here's an example of a query that includes a vector query with query rewrites. We modify a [previous example](#make-a-search-request-with-query-rewrites) to include a vector query.
+Here's an example of a query that includes a vector query with query rewrites. Modify a [previous example](#make-a-search-request-with-query-rewrites) to include a vector query.
 
-- We add a "vectorQueries" object to the request. This object includes a vector query with the "kind" set to "text". 
+- Add a "vectorQueries" object to the request. This object includes a vector query with the "kind" set to "text". 
 - The "text" value is the same as the "search" value. These values must be identical for query rewriting to work.
 
 ```http
-POST https://[search-service-name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2024-11-01-preview
+POST https://[search-service-name].search.windows.net/indexes/hotels-sample-index/docs/search?api-version=2025-03-01-preview
 {
     "search": "newer hotel near the water with a great restaurant",
     "vectorQueries": [
@@ -256,6 +252,7 @@ You might observe that the debug (test) response includes an empty array for the
 ```
 
 In the preceding example:
+
 - The response includes a `@search.semanticPartialResponseReason` property with a value of "Transient". This message means that at least one of the queries failed to complete. 
 - The response also includes a `@search.semanticQueryRewriteResultType` property with a value of "OriginalQueryOnly". This message means that the query rewrites are unavailable. Only the original query is used to retrieve search results.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティッククエリ再構成に関するガイドの更新"
}
```

### Explanation
この変更は、`articles/search/semantic-how-to-query-rewrite.md`ファイルの修正を示しており、Azure AI Searchにおけるセマンティッククエリの再構成に関するガイドが更新されています。主な目的は、最新の情報を反映し、ユーザーにとっての理解を深めることです。

具体的な変更内容は以下の通りです：

1. **日付の更新**: 最終更新日が「11/19/2024」から「03/31/2025」に変更され、新しい情報が反映されています。

2. **クエリ再構成のプロセスの明確化**: クエリ再構成の段階に新しい説明が追加され、ユーザーがどのように実際のクエリを再構成するかのプロセスがより具体的に説明されています。特に、ユーザーのクエリがどのように生成モデルに送信され、代替クエリが生成されるかについての情報が強調されました。

3. **前提条件の具体化**: クエリ再構成を利用するための前提条件が明確化され、地域制限（北ヨーロッパおよび東南アジア）や、セマンティックランカーが有効である必要性についていくつかのポイントが整理されています。

4. **リクエストの例の更新**: REST APIのリクエストの例において、APIバージョンが「2024-11-01-preview」から「2025-03-01-preview」に更新され、最新のAPI仕様が反映されています。

5. **ユーザーへの指示の明確化**: リクエストを作成する際の各パラメータについての説明がわかりやすく整理され、特にユーザーが自身の検索サービス名やインデックス名をどのように設定すべきかが具体的に示されています。

6. **デバッグ情報の説明**: デバッグ情報の取得に関する注意点が強調され、テストにおいてのみデバッグ情報を使用することが推奨されています。

このように、全体としての変更は、ユーザーがAzure AI Searchを利用してセマンティッククエリを有効に活用できるよう、情報の透明性および使いやすさを向上させることを目的としています。

## articles/search/semantic-search-overview.md{#item-b7497b}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 02/18/2025
+ms.date: 03/31/2025
 ---
 
 # Semantic ranking in Azure AI Search
@@ -24,7 +24,7 @@ Semantic ranker is a premium feature, billed by usage. We recommend this article
 
 ## What is semantic ranking?
 
-Semantic ranker calls LLMs at query time. LLms are used to improve the quality of an initial [BM25-ranked](index-similarity-and-scoring.md) or [RRF-ranked](hybrid-search-ranking.md) search result for text-based queries, the text portion of vector queries, and hybrid queries. When you enable it on your search service, semantic ranking extends the query execution pipeline in three ways:
+Semantic ranker calls LLMs at query time. LLms are used to improve the quality of an initial [BM25-ranked](index-similarity-and-scoring.md) or [RRF-ranked](hybrid-search-ranking.md) search result for text-based queries, the text portion of vector queries, and hybrid queries. Semantic ranking extends the query execution pipeline in three ways:
 
 * First, it always adds secondary ranking over an initial result set that was scored using BM25 or Reciprocal Rank Fusion (RRF). This secondary ranking uses multi-lingual, deep learning models adapted from Microsoft Bing to promote the most semantically relevant results.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティック検索の概要の更新"
}
```

### Explanation
この変更は、`articles/search/semantic-search-overview.md`ファイルの修正を示しており、Azure AI Searchにおけるセマンティックランキングの概要が更新されています。主な目的は、情報の鮮度を保ち、ユーザーにとっての理解を促進することです。

具体的な変更内容は以下の通りです：

1. **日付の更新**: 最終更新日が「02/18/2025」から「03/31/2025」に変更され、記事に新しい情報が追加されていることを示しています。

2. **セマンティックランキングの説明の明確化**: セマンティックランカーがクエリ時に大規模言語モデル（LLM）を呼び出す処理の説明がわかりやすく整理されました。具体的には、初期のランキング結果に対して、セマンティックランキングが追加のランキングを行う方法が特に強調されています。

3. **クエリ実行パイプラインの拡張方法の明示**: セマンティックランキングがクエリ実行パイプラインを拡張する方法についての説明が簡潔になり、具体的に何を実施するかがはっきりと記載されています。

これらの変更により、Azure AI Searchのセマンティックランキング機能がどのように機能するかを理解しやすくし、ユーザーがこのプレミアム機能を活用する際の理解を深める目的があります。また、情報はより明確で、技術的な詳細も含まれているため、ユーザーにとって有益なリソースとなっています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -201,6 +201,8 @@ items:
       href: search-region-support.md
     - name: Choose a tier
       href: search-sku-tier.md
+    - name: Upgrade a service
+      href: search-how-to-upgrade.md
     - name: Service limits
       href: search-limits-quotas-capacity.md
     - name: Plan and manage capacity
@@ -215,11 +217,11 @@ items:
       href: search-modeling-multitenant-saas-applications.md
     - name: Manage
       items:
-      - name: Manage with PowerShell
+      - name: Manage using PowerShell
         href: search-manage-powershell.md
-      - name: Manage with Azure CLI
+      - name: Manage using Azure CLI
         href: search-manage-azure-cli.md
-      - name: Manage with REST
+      - name: Manage using REST
         href: search-manage-rest.md
       - name: Move service across regions
         href: search-howto-move-across-regions.md
@@ -399,19 +401,21 @@ items:
         href: index-add-language-analyzers.md
       - name: Add a custom analyzer
         href: index-add-custom-analyzers.md
-    - name: Filters
+    - name: Filters and facets
       items:
       - name: Filters in text queries
         displayName: query
         href: search-filters.md
-      - name: Add faceted navigation
-        href: search-faceted-navigation.md
       - name: Understand collection filters
         href: search-query-understand-collection-filters.md
       - name: Troubleshoot collection filters
         href: search-query-troubleshoot-collection-filters.md
       - name: Normalize text for filters
         href: search-normalizers.md
+      - name: Add faceted navigation
+        href: search-faceted-navigation.md
+      - name: Faceted navigation examples
+        href: search-faceted-navigation-examples.md
     - name: Search results
       items:
       - name: Page, sort, and shape results
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOC（目次）ファイルの更新"
}
```

### Explanation
この変更は、`articles/search/toc.yml`ファイルの修正を示しており、Azure AI Searchに関するドキュメントの目次が更新されています。主な目的は、新しい情報を追加し、ユーザーが情報を見つけやすくすることです。

具体的な変更内容は以下の通りです：

1. **新しい項目の追加**: 
   - 「Upgrade a service」という新しい項目が追加され、`search-how-to-upgrade.md`へのリンクが設定されています。これにより、サービスのアップグレードに関する情報がユーザーに提供されます。
   
2. **項目の名称変更**: 
   - 「Manage with PowerShell」、「Manage with Azure CLI」、「Manage with REST」などの表現が「Manage using PowerShell」、「Manage using Azure CLI」、「Manage using REST」に変更され、より自然な英語表現が使用されています。これにより、ユーザーがこれらのトピックをより理解しやすくなります。

3. **項目の詳細化**: 
   - 「Filters」という項目が「Filters and facets」に改名され、その内容が強化されました。これには、「Add faceted navigation」や「Faceted navigation examples」という具体的な項目が追加され、ユーザーがファセットナビゲーションについて詳しく学ぶためのリソースが提供されています。

このように、目次の更新により、ユーザーが必要なドキュメントに迅速にアクセスできるようになり、Azure AI Searchに関する情報提供が一層強化されています。全体として、情報の整理が行われ、機能やリソースのアクセスが改善されることで、ユーザーエクスペリエンスが向上しています。

## articles/search/tutorial-create-custom-analyzer.md{#item-ad5520}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Tutorial: create a custom analyzer'
+title: 'Tutorial: Create a Custom Analyzer'
 titleSuffix: Azure AI Search
 description: Learn how to build a custom analyzer to improve the quality of search results in Azure AI Search.
 author: gmndrg
@@ -8,14 +8,14 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: tutorial
-ms.date: 01/17/2025
+ms.date: 03/28/2025
 ---
 
 # Tutorial: Create a custom analyzer for phone numbers
 
-In search solutions, strings that have complex patterns or special characters can be a challenge to work with because the [default analyzer](search-analyzers.md) strips out or misinterprets meaningful parts of a pattern, resulting in a poor search experience when users can't find the information they expected. Phone numbers are a classic example of strings that are hard to analyze. They come in various formats, and they include special characters that the default analyzer ignores. 
+In search solutions, strings that have complex patterns or special characters can be challenging to work with because the [default analyzer](search-analyzers.md) strips out or misinterprets meaningful parts of a pattern. This results in a poor search experience where users can't find the information they expect. Phone numbers are a classic example of strings that are difficult to analyze. They come in various formats and include special characters that the default analyzer ignores.
 
-With phone numbers as its subject, this tutorial takes a close look at the problems of patterned data, and shows you to solve that problem using a [custom analyzer](index-add-custom-analyzers.md). The approach outlined here can be used as-is for phone numbers, or adapted for fields having the same characteristics (patterned, with special characters), such as URLs, emails, postal codes, and dates.
+With phone numbers as its subject, this tutorial shows you how to solve patterned data problems using a [custom analyzer](index-add-custom-analyzers.md). This approach can be used as is for phone numbers or adapted for fields with the same characteristics (patterned with special characters), such as URLs, emails, postal codes, and dates.
 
 In this tutorial, you use a REST client and the [Azure AI Search REST APIs](/rest/api/searchservice/) to:
 
@@ -27,33 +27,33 @@ In this tutorial, you use a REST client and the [Azure AI Search REST APIs](/res
 
 ## Prerequisites
 
-The following services and tools are required for this tutorial.
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
-+ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
++ [Azure AI Search](search-what-is-azure-search.md). [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription. For this tutorial, you can use a free service.
 
-+ [Azure AI Search](search-what-is-azure-search.md). [Create](search-create-service-portal.md) or [find an existing Azure AI Search resource](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) under your current subscription. You can use a free service for this quickstart. 
++ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 ### Download files
 
-Source code for this tutorial is the [custom-analyzer.rest](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/custom-analyzers/custom-analyzer.rest) file in the [Azure-Samples/azure-search-rest-samples](https://github.com/Azure-Samples/azure-search-rest-samples) GitHub repository.
+Source code for this tutorial is in the [custom-analyzer.rest](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/custom-analyzers/custom-analyzer.rest) file in the [Azure-Samples/azure-search-rest-samples](https://github.com/Azure-Samples/azure-search-rest-samples) GitHub repository.
 
-### Copy a key and URL
+### Copy an admin key and URL
 
 The REST calls in this tutorial require a search service endpoint and an admin API key. You can get these values from the Azure portal.
 
-1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
+1. Sign in to the [Azure portal](https://portal.azure.com), go to the **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
 
 1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
 
    :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
 
-A valid API key establishes trust, on a per request basis, between the application sending the request and the search service handling it.
+A valid API key establishes trust, on a per-request basis, between the application sending the request and the search service handling it.
 
 ## Create an initial index
 
 1. Open a new text file in Visual Studio Code.
 
-1. Set variables to the search endpoint and the API key you collected in the previous step.
+1. Set variables to the search endpoint and the API key you collected in the previous section.
 
    ```http
    @baseUrl = PUT-YOUR-SEARCH-SERVICE-URL-HERE
@@ -62,7 +62,7 @@ A valid API key establishes trust, on a per request basis, between the applicati
 
 1. Save the file with a `.rest` file extension.
 
-1. Paste in the following example to create a small index called `phone-numbers-index` with two fields: `id` and `phone_number`. We haven't defined an analyzer yet, so the `standard.lucene` analyzer is used by default.
+1. Paste the following example to create a small index called `phone-numbers-index` with two fields: `id` and `phone_number`. You haven't defined an analyzer yet, so the `standard.lucene` analyzer is used by default.
 
     ```http
     ### Create a new index
@@ -94,7 +94,7 @@ A valid API key establishes trust, on a per request basis, between the applicati
       }
     ```
 
-1. Select **Send request**. You should have an `HTTP/1.1 201 Created` response and the response body should include the JSON representation of the index schema.
+1. Select **Send request**. You should have an `HTTP/1.1 201 Created` response, and the response body should include the JSON representation of the index schema.
 
 1. Load data into the index, using documents that contain various phone number formats. This is your test data.
 
@@ -150,7 +150,7 @@ A valid API key establishes trust, on a per request basis, between the applicati
       }
     ```
 
-1. Let's try a few queries similar to what a user might type. A user could search for `(425) 555-0100` in any number of formats and still expect results to be returned. Start by searching `(425) 555-0100`:
+1. Try queries similar to what a user might type. For example, a user might search for `(425) 555-0100` in any number of formats and still expect results to be returned. Start by searching `(425) 555-0100`.
 
     ```http  
     ### Search for a phone number
@@ -159,7 +159,7 @@ A valid API key establishes trust, on a per request basis, between the applicati
       api-key: {{apiKey}}
     ```
 
-    The query returns **three out of four expected results**, but also returns **two unexpected results**:
+    The query returns three out of four expected results but also returns two unexpected results.
 
     ```json
     {
@@ -188,7 +188,7 @@ A valid API key establishes trust, on a per request basis, between the applicati
     }
     ```
 
-1. Let's try again without any formatting: `4255550100`.
+1. Try again without any formatting: `4255550100`.
 
    ```http  
     ### Search for a phone number
@@ -197,7 +197,7 @@ A valid API key establishes trust, on a per request basis, between the applicati
       api-key: {{apiKey}}
     ```
 
-   This query does even worse, returning only **one of four correct matches**.
+   This query does even worse, returning only one of four correct matches.
 
     ```json
     {
@@ -210,48 +210,48 @@ A valid API key establishes trust, on a per request basis, between the applicati
     }
     ```
 
-If you find these results confusing, you're not alone. In the next section, let's dig into why we're getting these results.
+If you find these results confusing, you're not alone. The next section explains why you're getting these results.
 
 <a name="how-analyzers-work"></a>
 
 ## Review how analyzers work
 
-To understand these search results, we need to understand what the analyzer is doing. From there, we can test the default analyzer using the [Analyze API](/rest/api/searchservice/indexes/analyze), providing a foundation for designing an analyzer that better meets our needs.
+To understand these search results, you must understand what the analyzer is doing. From there, you can test the default analyzer using the [Analyze API](/rest/api/searchservice/indexes/analyze), providing a foundation for designing an analyzer that better meets your needs.
 
-An [analyzer](search-analyzers.md) is a component of the [full text search engine](search-lucene-query-architecture.md) responsible for processing text in query strings and indexed documents. Different analyzers manipulate text in different ways depending on the scenario. For this scenario, we need to build an analyzer tailored to phone numbers.
+An [analyzer](search-analyzers.md) is a component of the [full-text search engine](search-lucene-query-architecture.md) responsible for processing text in query strings and indexed documents. Different analyzers manipulate text in different ways depending on the scenario. For this scenario, we need to build an analyzer tailored to phone numbers.
 
 Analyzers consist of three components:
 
 + [**Character filters**](#CharFilters) that remove or replace individual characters from the input text.
-+ A [**Tokenizer**](#Tokenizers) that breaks the input text into tokens, which become keys in the search index.
++ A [**tokenizer**](#Tokenizers) that breaks the input text into tokens, which become keys in the search index.
 + [**Token filters**](#TokenFilters) that manipulate the tokens produced by the tokenizer.
 
-In the following diagram, you can see how these three components work together to tokenize a sentence:
+The following diagram shows how these three components work together to tokenize a sentence.
 
   :::image type="content" source="media/tutorial-create-custom-analyzer/analyzers-explained.png" alt-text="Diagram of Analyzer process to tokenize a sentence":::
 
-These tokens are then stored in an inverted index, which allows for fast, full-text searches.  An inverted index enables full-text search by mapping all unique terms extracted during lexical analysis to the documents in which they occur. You can see an example in the next diagram:
+These tokens are then stored in an inverted index, which allows for fast, full-text searches. An inverted index enables full-text search by mapping all unique terms extracted during lexical analysis to the documents in which they occur. You can see an example in the following diagram:
 
   :::image type="content" source="media/tutorial-create-custom-analyzer/inverted-index-explained.png" alt-text="Example inverted index":::
 
 All of search comes down to searching for the terms stored in the inverted index. When a user issues a query:
 
 1. The query is parsed and the query terms are analyzed.
-1. The inverted index is then scanned for documents with matching terms.
-1. Finally, the retrieved documents are ranked by the [scoring algorithm](index-ranking-similarity.md).
+1. The inverted index is scanned for documents with matching terms.
+1. The [scoring algorithm](index-ranking-similarity.md) ranks the retrieved documents.
 
   :::image type="content" source="media/tutorial-create-custom-analyzer/query-architecture-explained.png" alt-text="Diagram of Analyzer process ranking similarity":::
 
-If the query terms don't match the terms in your inverted index, results aren't returned. To learn more about how queries work, see this article on [full text search](search-lucene-query-architecture.md).
+If the query terms don't match the terms in your inverted index, results aren't returned. To learn more about how queries work, see [Full-text search in Azure AI Search](search-lucene-query-architecture.md).
 
 > [!Note]
-> [Partial term queries](search-query-partial-matching.md) are an important exception to this rule. These queries (prefix query, wildcard query, regex query) bypass the lexical analysis process unlike regular term queries. Partial terms are only lowercased before being matched against terms in the index. If an analyzer isn't configured to support these types of queries, you'll often receive unexpected results because matching terms don't exist in the index.
+> [Partial term queries](search-query-partial-matching.md) are an important exception to this rule. Unlike regular term queries, these queries (prefix query, wildcard query, and regex query) bypass the lexical analysis process. Partial terms are only lowercased before being matched against terms in the index. If an analyzer isn't configured to support these types of queries, you often receive unexpected results because matching terms don't exist in the index.
 
 ## Test analyzers using the Analyze API
 
 Azure AI Search provides an [Analyze API](/rest/api/searchservice/indexes/analyze) that allows you to test analyzers to understand how they process text.
 
-The Analyze API is called using the following request:
+Call the Analyze API using the following request:
 
 ```http
 POST {{baseUrl}}/indexes/phone-numbers-index/analyze?api-version=2024-07-01  HTTP/1.1
@@ -264,7 +264,7 @@ POST {{baseUrl}}/indexes/phone-numbers-index/analyze?api-version=2024-07-01  HTT
   }
 ```
 
-The API returns the tokens extracted from the text, using the analyzer you specified. The standard Lucene analyzer splits the phone number into three separate tokens:
+The API returns the tokens extracted from the text, using the analyzer you specified. The standard Lucene analyzer splits the phone number into three separate tokens.
 
 ```json
 {
@@ -315,23 +315,23 @@ Response:
 }
 ```
 
-Keep in mind that both query terms and the indexed documents undergo analysis. Thinking back to the search results from the previous step, we can start to see why those results were returned.
+Keep in mind that both query terms and the indexed documents undergo analysis. Thinking back to the search results from the previous step, you can start to see why those results are returned.
 
-In the first query, unexpected phone numbers were returned because one of their tokens, `555`, matched one of the terms we searched. In the second query, only the one number was returned because it was the only record that had a token matching `4255550100`.
+In the first query, unexpected phone numbers are returned because one of their tokens, `555`, matched one of the terms you searched. In the second query, only the one number is returned because it's the only record that has a token matching `4255550100`.
 
 ## Build a custom analyzer
 
-Now that we understand the results we're seeing, let's build a custom analyzer to improve the tokenization logic.
+Now that you understand the results you're seeing, build a custom analyzer to improve the tokenization logic.
 
-The goal is to provide intuitive search against phone numbers no matter what format the query or indexed string is in. To achieve this outcome, we'll specify a [character filter](#CharFilters), a [tokenizer](#Tokenizers), and a [token filter](#TokenFilters).
+The goal is to provide intuitive search against phone numbers no matter what format the query or indexed string is in. To achieve this outcome, specify a [character filter](#CharFilters), a [tokenizer](#Tokenizers), and a [token filter](#TokenFilters).
 
 <a name="CharFilters"></a>
 
 ### Character filters
 
-Character filters are used to process text before it's fed into the tokenizer. Common uses of character filters include filtering out HTML elements or replacing special characters.
+Character filters process text before it's fed into the tokenizer. Common uses of character filters are filtering out HTML elements and replacing special characters.
 
-For phone numbers, we want to remove whitespace and special characters because not all phone number formats contain the same special characters and spaces.
+For phone numbers, you want to remove whitespace and special characters because not all phone number formats contain the same special characters and spaces.
 
 ```json
 "charFilters": [
@@ -363,9 +363,9 @@ The filter removes `-` `(` `)` `+` `.` and spaces from the input.
 
 Tokenizers split text into tokens and discard some characters, such as punctuation, along the way. In many cases, the goal of tokenization is to split a sentence into individual words.
 
-For this scenario, we'll use a keyword tokenizer, `keyword_v2`, because we want to capture the phone number as a single term. Note that this isn't the only way to solve this problem. See the [Alternate approaches](#Alternate) section below.
+For this scenario, use a keyword tokenizer, `keyword_v2`, to capture the phone number as a single term. This isn't the only way to solve this problem, as explained in the [Alternate approaches](#Alternate) section.
 
-Keyword tokenizers always output the same text it was given as a single term.
+Keyword tokenizers always output the same text they're given as a single term.
 
 |Input|Output|  
 |-|-|  
@@ -376,9 +376,9 @@ Keyword tokenizers always output the same text it was given as a single term.
 
 ### Token filters
 
-Token filters will filter out or modify the tokens generated by the tokenizer. One common use of a token filter is to lowercase all characters using a lowercase token filter. Another common use is filtering out [stopwords](reference-stopwords.md) such as `the`, `and`, or `is`.
+Token filters modify or filter out the tokens generated by the tokenizer. One common use of a token filter is to lowercase all characters using a lowercase token filter. Another common use is filtering out [stopwords](reference-stopwords.md), such as `the`, `and`, or `is`.
 
-While we don't need to use either of those filters for this scenario, we'll use an nGram token filter to allow for partial searches of phone numbers.
+While you don't need to use either of those filters for this scenario, use an nGram token filter to allow for partial searches of phone numbers.
 
 ```json
 "tokenFilters": [
@@ -395,9 +395,9 @@ While we don't need to use either of those filters for this scenario, we'll use
 
 The [nGram_v2 token filter](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/ngram/NGramTokenFilter.html) splits tokens into n-grams of a given size based on the `minGram` and `maxGram` parameters.
 
-For the phone analyzer, we set `minGram` to `3` because that is the shortest substring we expect users to search. `maxGram` is set to `20` to ensure that all phone numbers, even with extensions, will fit into a single n-gram.
+For the phone analyzer, `minGram` is set to `3` because that's the shortest substring users are expected to search. `maxGram` is set to `20` to ensure that all phone numbers, even with extensions, fit into a single n-gram.
 
- The unfortunate side effect of n-grams is that some false positives will be returned. We'll fix this in a later step by building out a separate analyzer for searches that doesn't include the n-gram token filter.
+The unfortunate side effect of n-grams is that some false positives are returned. You fix this in a later step by building out a separate analyzer for searches that doesn't include the n-gram token filter.
 
 |Input|Output|  
 |-|-|  
@@ -406,7 +406,7 @@ For the phone analyzer, we set `minGram` to `3` because that is the shortest sub
 
 ### Analyzer
 
-With our character filters, tokenizer, and token filters in place, we're ready to define our analyzer.
+With the character filters, tokenizer, and token filters in place, you're ready to define the analyzer.
 
 ```json
 "analyzers": [
@@ -424,26 +424,26 @@ With our character filters, tokenizer, and token filters in place, we're ready t
 ]
 ```
 
-From the Analyze API, given the following inputs, outputs from the custom analyzer are shown in the following table.
+From the Analyze API, given the following inputs, outputs from the custom analyzer are as follows:
 
 |Input|Output|  
 |-|-|  
 |`12345`|`[123, 1234, 12345, 234, 2345, 345]`|  
 |`(321) 555-0199`|`[321, 3215, 32155, 321555, 3215550, 32155501, 321555019, 3215550199, 215, 2155, 21555, 215550, ... ]`|
 
-All of the tokens in the output column exist in the index. If our query includes any of those terms, the phone number is returned.
+All of the tokens in the output column exist in the index. If your query includes any of those terms, the phone number is returned.
 
 ## Rebuild using the new analyzer
 
-1. Delete the current index:
+1. Delete the current index.
 
    ```http
     ### Delete the index
     DELETE {{baseUrl}}/indexes/phone-numbers-index?api-version=2024-07-01 HTTP/1.1
         api-key: {{apiKey}}
     ```
 
-1. Recreate the index using the new analyzer. This index schema adds a custom analyzer definition, and a custom analyzer assignment on the phone number field.
+1. Recreate the index using the new analyzer. This index schema adds a custom analyzer definition and a custom analyzer assignment on the phone number field.
 
     ```http
     ### Create a new index
@@ -513,7 +513,7 @@ All of the tokens in the output column exist in the index. If our query includes
 
 ### Test the custom analyzer
 
-After recreating the index, you can now test out the analyzer using the following request:
+After you recreate the index, test the analyzer using the following request:
 
 ```http
 POST {{baseUrl}}/indexes/tutorial-first-analyzer/analyze?api-version=2024-07-01  HTTP/1.1
@@ -526,7 +526,7 @@ POST {{baseUrl}}/indexes/tutorial-first-analyzer/analyze?api-version=2024-07-01
   }
 ```
 
-You should now see the collection of tokens resulting from the phone number:
+You should now see the collection of tokens resulting from the phone number.
 
 ```json
 {
@@ -558,9 +558,9 @@ You should now see the collection of tokens resulting from the phone number:
 
 ## Revise the custom analyzer to handle false positives
 
-After making some sample queries against the index with the custom analyzer, you'll find that recall has improved and all matching phone numbers are now returned. However, the n-gram token filter causes some false positives to be returned as well. This is a common side effect of an n-gram token filter.
+After using the custom analyzer to make sample queries against the index, you should see that recall has improved and all matching phone numbers are now returned. However, the n-gram token filter also causes some false positives to be returned. This is a common side effect of an n-gram token filter.
 
-To prevent false positives, we'll create a separate analyzer for querying. This analyzer is identical to the previous one, except that it **omits** the `custom_ngram_filter`.
+To prevent false positives, create a separate analyzer for querying. This analyzer is identical to the previous one, except that it omits the `custom_ngram_filter`.
 
 ```json
     {
@@ -574,7 +574,7 @@ To prevent false positives, we'll create a separate analyzer for querying. This
     }
 ```
 
-In the index definition, we then specify both an `indexAnalyzer` and a `searchAnalyzer`.
+In the index definition, specify both an `indexAnalyzer` and a `searchAnalyzer`.
 
 ```json
     {
@@ -589,25 +589,25 @@ In the index definition, we then specify both an `indexAnalyzer` and a `searchAn
     }
 ```
 
-With this change, you're all set. Here are your next steps: 
+With this change, you're all set. Here are your next steps:
 
-1. Delete the index. 
+1. Delete the index.
 
-1. Recreate the index after adding the new custom analyzer (`phone_analyzer-search`) and assigning that analyzer to the `phone-number` field's `searchAnalyzer` property.
+1. Recreate the index after you add the new custom analyzer (`phone_analyzer-search`) and assign that analyzer to the `phone-number` field's `searchAnalyzer` property.
 
 1. Reload the data.
 
-1. Retest the queries to verify the search works as expected. If you're using the sample file, this step creates the third index named `phone-number-index-3`.
+1. Retest the queries to verify that the search works as expected. If you're using the sample file, this step creates the third index named `phone-number-index-3`.
 
 <a name="Alternate"></a>
 
 ## Alternate approaches
 
 The analyzer described in the previous section is designed to maximize the flexibility for search. However, it does so at the cost of storing many potentially unimportant terms in the index.
 
-The following example shows an alternative analyzer that's more efficient in tokenization, but has drawbacks. 
+The following example shows an alternative analyzer that's more efficient in tokenization, but it has drawbacks.
 
-Given an input of `14255550100`, the analyzer can't logically chunk the phone number. For example, it can't separate the country code, `1`, from the area code, `425`. This discrepancy would lead to the phone number not being returned if a user didn't include a country code in their search.
+Given an input of `14255550100`, the analyzer can't logically chunk the phone number. For example, it can't separate the country code, `1`, from the area code, `425`. This discrepancy leads to the phone number not being returned if a user doesn't include a country code in their search.
 
 ```json
 "analyzers": [
@@ -638,7 +638,7 @@ Given an input of `14255550100`, the analyzer can't logically chunk the phone nu
 ]
 ```
 
-You can see in the following example that the phone number is split into the chunks you would normally expect a user to be searching for.
+In the following example, the phone number is split into the chunks you normally expect a user to be search for.
 
 |Input|Output|  
 |-|-|  
@@ -648,7 +648,7 @@ Depending on your requirements, this might be a more efficient approach to the p
 
 ## Takeaways
 
-This tutorial demonstrated the process for building and testing a custom analyzer. You created an index, indexed data, and then queried against the index to see what search results were returned. From there, you used the Analyze API to see the lexical analysis process in action.
+This tutorial demonstrated the process of building and testing a custom analyzer. You created an index, indexed data, and then queried against the index to see what search results were returned. From there, you used the Analyze API to see the lexical analysis process in action.
 
 While the analyzer defined in this tutorial offers an easy solution for searching against phone numbers, this same process can be used to build a custom analyzer for any scenario that shares similar characteristics.
 
@@ -660,7 +660,7 @@ You can find and manage resources in the Azure portal, using the All resources o
 
 ## Next steps
 
-Now that you're familiar with how to create a custom analyzer, let's take a look at all of the different filters, tokenizers, and analyzers available to you to build a rich search experience.
+Now that you know how to create a custom analyzer, take a look at all of the different filters, tokenizers, and analyzers available for building a rich search experience:
 
 > [!div class="nextstepaction"]
-> [Custom Analyzers in Azure AI Search](index-add-custom-analyzers.md)
+> [Custom analyzers in Azure AI Search](index-add-custom-analyzers.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムアナライザー作成チュートリアルの更新"
}
```

### Explanation
この変更は、`articles/search/tutorial-create-custom-analyzer.md`ファイルの大幅な修正を示しており、Azure AI Searchにおけるカスタムアナライザーを作成するためのチュートリアルが更新されています。目的は、内容をより明確で一貫性のあるものにすることで、学習効果を向上させることです。

具体的な変更内容は以下の通りです：

1. **タイトルの修正**: タイトルが「create a custom analyzer」から「Create a Custom Analyzer」に変更され、形式が統一されました。

2. **最終更新日の更新**: 最終更新日が「01/17/2025」から「03/28/2025」に更新され、最新の情報が提供されることを示しています。

3. **内容の明確化**:
   - チュートリアルの説明及びセクションの文言が改善され、より洗練された表現になっています。例えば、「challenging to work with」から「can be challenging to work with」への修正や、指示のトーンが親しみやすくなっています。
   - 各ステップの説明がより明確にされ、読者が手順を追いやすくなっています。また、「admins keys」や「index schema」などの技術用語も正確に用いられています。

4. **段落構造の改善**: 段落の構成が見直され、情報の流れがスムーズになっています。特に、カスタムアナライザーに関する説明や手順がより連携しており、読者が情報を理解しやすくなっています。

5. **コードサンプルの更新**: コードやHTTPリクエストの詳細が整理され、新しい形式や指示が提供されています。特に、設定手順やサンプルコードの説明が改善されており、参加者が実際の作業に取り組みやすくなっています。

これにより、Azure AI Searchのカスタムアナライザー作成に必要な情報が整然と提供され、ユーザーがより良い学習体験を得られるようになっています。また、技術的な内容も精錬されたことで、より信頼性のある資料となっています。

## articles/search/tutorial-multiple-data-sources.md{#item-71558f}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 03/10/2025
+ms.date: 03/28/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
@@ -49,7 +49,7 @@ A finished version of the code in this tutorial can be found in the following pr
 > [!NOTE]
 > You can use a free search service for this tutorial. The free tier limits you to three indexes, three indexers, and three data sources. This tutorial creates one of each. Before starting, make sure you have room on your service to accept the new resources.
 
-## 1 - Create services
+## Create services
 
 This tutorial uses Azure AI Search for indexing and queries, Azure Cosmos DB for the first data set, and Azure Blob Storage for the second data set.
 
@@ -99,7 +99,7 @@ This sample uses two small sets of data describing seven fictional hotels. One s
 
 The third component is Azure AI Search, which you can [create in the Azure portal](search-create-service-portal.md) or [find an existing search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your Azure resources.
 
-### Copy an admin API key and URL for Azure AI Search
+### Copy an admin key and URL for Azure AI Search
 
 To authenticate to your search service, you need the service URL and an access key.
 
@@ -111,7 +111,7 @@ To authenticate to your search service, you need the service URL and an access k
 
 Having a valid key establishes trust, on a per-request basis, between the application sending the request and the service handling it.
 
-## 2 - Set up your environment
+## Set up your environment
 
 1. Open Visual Studio.
 
@@ -140,7 +140,7 @@ The first two entries are the URL and admin keys of a search service. Use the fu
 
 The next entries specify account names and connection string information for the Azure Blob Storage and Azure Cosmos DB data sources.
 
-## 3 - Map key fields
+## Map key fields
 
 Merging content requires that both data streams are targeting the same documents in the search index.
 
@@ -155,7 +155,7 @@ Azure AI Search indexers can use field mappings to rename and even reformat data
 > [!NOTE]
 > In most cases, autogenerated document keys, such as those created by default by some indexers, don't make good document keys for combined indexes. In general, use a meaningful, unique key value that already exists in your data sources or can be easily added.
 
-## 4 - Explore the code
+## Explore the code
 
 When the data and configuration settings are in place, the sample program in **/v11/AzureSearchMultipleDataSources.sln** should be ready to build and run.
 
@@ -351,7 +351,7 @@ Because the index is already populated with hotel data from the Azure Cosmos DB
 > [!NOTE]
 > If you have the same non-key fields in both of your data sources, and the data in those fields doesn't match, the index contains the values from whichever indexer ran most recently. In our example, both data sources contain a **HotelName** field. If for some reason the data in this field is different, for documents with the same key value, the **HotelName** data from the most recently indexed data source is the value stored in the index.
 
-## 5 - Search
+## Search
 
 After running the program, you can explore the populated search index using the [**Search explorer**](search-explorer.md) in the Azure portal.
 
@@ -377,7 +377,7 @@ You can find and manage resources in the Azure portal using the All resources or
 
 ## Next step
 
-Now that you're familiar with the concept of ingesting data from multiple sources, take a closer look at indexer configuration, starting with Azure Cosmos DB:
+Now that you're familiar with ingesting data from multiple sources, take a closer look at indexer configuration, starting with Azure Cosmos DB:
 
 > [!div class="nextstepaction"]
 > [Configure an Azure Cosmos DB for NoSQL indexer](search-howto-index-cosmosdb.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "複数データソースチュートリアルの更新"
}
```

### Explanation
この変更は、`articles/search/tutorial-multiple-data-sources.md`ファイルの修正を示しており、Azure AI Searchにおける複数データソースからのデータの取り込みに関するチュートリアルが更新されています。主な目的は、文書の明確性と一貫性を向上させることです。

具体的な変更内容は以下の通りです：

1. **最終更新日の更新**: 最終更新日が「03/10/2025」から「03/28/2025」に変更され、最新の情報が反映されています。

2. **セクションタイトルの修正**: 各セクションのタイトルから数字が削除され（例：`## 1 - Create services`から`## Create services`）、タイトルの一貫性が向上しています。これは、セクションがよりスムーズにお互いに関連付けられることを目的としています。

3. **用語の改善**: 「admin API key」から「admin key」に変更され、用語が簡略化され、より明確になっています。このように、技術的な表現がシンプルになり、ユーザーが理解しやすくなっています。

4. **手順の整備**: 各手続きの説明が一貫したスタイルで記載され、ユーザーが作業を追いやすくなっています。例えば、環境設定やフィールドマッピングの説明が整理されています。

5. **ノートの構造化**: 注記（NOTE）が整理され、重要な情報が強調され、視覚的に目立つようになっています。これにより、ユーザーが特に注意が必要なポイントを簡単に見つけやすくなります。

こうした変更によって、複数のデータソースからデータを取り込む手順が明確化され、Azure AI Searchの使い方がより親しみやすくなっています。また、文書全体の流れがスムーズになり、ユーザーエクスペリエンスの向上が期待されます。

## articles/search/tutorial-optimize-indexing-push-api.md{#item-ef0e96}

<details>
<summary>Diff</summary>
````diff
@@ -1,24 +1,24 @@
 ---
-title: 'C# tutorial: Optimize indexing by using the push API'
+title: 'C# Tutorial: Optimize Indexing Using the Push API'
 titleSuffix: Azure AI Search
-description: Learn how to efficiently index data by using Azure AI Search's push API. This tutorial and sample code are in C#.
+description: Learn how to efficiently index data using Azure AI Search's push API. This tutorial and sample code are in C#.
 author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 10/14/2024
+ms.date: 03/28/2025
 ms.custom:
   - devx-track-csharp
   - ignite-2023
 ---
 
-# Tutorial: Optimize indexing by using the push API
+# Tutorial: Optimize indexing using the push API
 
-Azure AI Search supports [two basic approaches](search-what-is-data-import.md) for importing data into a search index: *push* your data into the index programmatically, or *pull* in the data by pointing an [Azure AI Search indexer](search-indexer-overview.md) at a supported data source.
+Azure AI Search supports [two basic approaches](search-what-is-data-import.md) for importing data into a search index: *pushing* your data into the index programmatically, or *pulling* in your data by pointing an [Azure AI Search indexer](search-indexer-overview.md) to a supported data source.
 
-This tutorial explains how to efficiently index data using the [push model](search-what-is-data-import.md#pushing-data-to-an-index) by batching requests and using an exponential backoff retry strategy. You can [download and run the sample application](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/optimize-data-indexing). This article explains the key aspects of the application and what factors to consider when indexing data.
+This tutorial explains how to efficiently index data using the [push model](search-what-is-data-import.md#pushing-data-to-an-index) by batching requests and using an exponential backoff retry strategy. You can [download and run the sample application](https://github.com/Azure-Samples/azure-search-dotnet-scale/tree/main/optimize-data-indexing). This tutorial also explains the key aspects of the application and what factors to consider when indexing data.
 
-This tutorial uses C# and the [Azure.Search.Documents library](/dotnet/api/overview/azure/search) from the Azure SDK for .NET to perform the following tasks:
+In this tutorial, you use C# and the [Azure.Search.Documents library](/dotnet/api/overview/azure/search) from the Azure SDK for .NET to:
 
 > [!div class="checklist"]
 > * Create an index
@@ -29,11 +29,8 @@ This tutorial uses C# and the [Azure.Search.Documents library](/dotnet/api/overv
 
 ## Prerequisites
 
-The following services and tools are required for this tutorial.
-
-+ An Azure subscription. If you don't have one, you can [create a free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
-
-+ [Visual Studio](https://visualstudio.microsoft.com/downloads/), any edition. Sample code and instructions were tested on the free Community edition.
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
++ [Visual Studio](https://visualstudio.microsoft.com/downloads/).
 
 <a name="get-service-info"></a>
 
@@ -43,7 +40,7 @@ Source code for this tutorial is in the [optimize-data-indexing/v11](https://git
 
 ## Key considerations
 
-Factors that affect indexing speeds are listed next. To learn more, see [Index large data sets](search-howto-large-index.md).
+The following factors affect indexing speeds. For more information, see [Index large data sets](search-howto-large-index.md).
 
 + **Service tier and number of partitions/replicas**: Adding partitions or upgrading your tier increases indexing speeds.
 + **Index schema complexity**: Adding fields and field properties lowers indexing speeds. Smaller indexes are faster to index.
@@ -52,21 +49,21 @@ Factors that affect indexing speeds are listed next. To learn more, see [Index l
 + **Retry strategy**: An exponential backoff retry strategy is a best practice for optimum indexing.
 + **Network data transfer speeds**: Data transfer speeds can be a limiting factor. Index data from within your Azure environment to increase data transfer speeds.
 
-## Step 1: Create an Azure AI Search service
+## Create an Azure AI Search service
 
-To complete this tutorial, you need an Azure AI Search service, which you can [create in the Azure portal](search-create-service-portal.md), or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) under your current subscription. We recommend using the same tier you plan to use in production so that you can accurately test and optimize indexing speeds.
+This tutorial requires an Azure AI Search service, which you can [create in the Azure portal](search-create-service-portal.md). You can also [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription. To accurately test and optimize indexing speeds, we recommend using the same tier you plan to use in production.
 
 ### Get an admin key and URL for Azure AI Search
 
 This tutorial uses key-based authentication. Copy an admin API key to paste into the *appsettings.json* file.
 
-1. Sign in to the [Azure portal](https://portal.azure.com). Get the endpoint URL from your search service **Overview** page. An example endpoint might look like `https://mydemo.search.windows.net`.
+1. Sign in to the [Azure portal](https://portal.azure.com). On your service **Overview** page, copy the endpoint URL. An example endpoint might look like `https://mydemo.search.windows.net`.
 
-1. In **Settings** > **Keys**, get an admin key for full rights on the service. There are two interchangeable admin keys, provided for business continuity in case you need to roll one over. You can use either the primary or secondary key on requests for adding, modifying, and deleting objects.
+1. On **Settings** > **Keys**, get an admin key for full rights on the service. There are two interchangeable admin keys, provided for business continuity in case you need to roll one over. You can use either the primary or secondary key on requests for adding, modifying, and deleting objects.
 
     :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the HTTP endpoint and API key locations.":::
 
-## Step 2: Set up your environment
+## Set up your environment
 
 1. Start Visual Studio and open *OptimizeDataIndexing.sln*.
 
@@ -80,11 +77,11 @@ This tutorial uses key-based authentication. Copy an admin API key to paste into
 }
 ```
 
-## Step 3: Explore the code
+## Explore the code
 
-Once you update *appsettings.json*, the sample program in *OptimizeDataIndexing.sln* should be ready to build and run.
+After you update *appsettings.json*, the sample program in *OptimizeDataIndexing.sln* should be ready to build and run.
 
-This code is derived from the C# section of [Quickstart: Full text search using the Azure SDKs](search-get-started-text.md). You can find more detailed information on the basics of working with the .NET SDK in that article.
+This code is derived from the C# section of [Quickstart: Full text search using the Azure SDKs](search-get-started-text.md), which provides detailed information about the basics of working with the .NET SDK.
 
 This simple C#/.NET console app performs the following tasks:
 
@@ -105,9 +102,9 @@ This simple C#/.NET console app performs the following tasks:
 
 This sample program uses the Azure SDK for .NET to define and create an Azure AI Search index. It takes advantage of the `FieldBuilder` class to generate an index structure from a C# data model class.
 
-The data model is defined by the `Hotel` class, which also contains references to the `Address` class. The FieldBuilder drills down through multiple class definitions to generate a complex data structure for the index. Metadata tags are used to define the attributes of each field, such as whether it's searchable or sortable.
+The data model is defined by the `Hotel` class, which also contains references to the `Address` class. `FieldBuilder` drills down through multiple class definitions to generate a complex data structure for the index. Metadata tags are used to define the attributes of each field, such as whether it's searchable or sortable.
 
-The following snippets from the *Hotel.cs* file show how a single field, and a reference to another data model class, can be specified.
+The following snippets from the *Hotel.cs* file specify a single field and a reference to another data model class.
 
 ```csharp
 . . .
@@ -135,9 +132,9 @@ private static async Task CreateIndexAsync(string indexName, SearchIndexClient i
 
 ### Generate data
 
-A simple class is implemented in the *DataGenerator.cs* file to generate data for testing. The sole purpose of this class is to make it easy to generate a large number of documents with a unique ID for indexing.
+A simple class is implemented in the *DataGenerator.cs* file to generate data for testing. The purpose of this class is to make it easy to generate a large number of documents with a unique ID for indexing.
 
-To get a list of 100,000 hotels with unique IDs, run the following lines of code:
+To get a list of 100,000 hotels with unique IDs, run the following code:
 
 ```csharp
 long numDocuments = 100000;
@@ -147,23 +144,24 @@ List<Hotel> hotels = dg.GetHotels(numDocuments, "large");
 
 There are two sizes of hotels available for testing in this sample: *small* and *large*.
 
-The schema of your index has an effect on indexing speeds. For this reason, it makes sense to convert this class to generate data that best matches your intended index schema after you run through this tutorial.
+The schema of your index affects indexing speeds. After you complete this tutorial, consider converting this class to generate data that best matches your intended index schema.
 
-## Step 4: Test batch sizes
+## Test batch sizes
 
-Azure AI Search supports the following APIs to load single or multiple documents into an index:
+To load single or multiple documents into an index, Azure AI Search supports the following APIs:
 
 + [Documents - Index (REST API)](/rest/api/searchservice/documents)
-+ [IndexDocumentsAction class](/dotnet/api/azure.search.documents.models.indexdocumentsaction) or [IndexDocumentsBatch class](/dotnet/api/azure.search.documents.models.indexdocumentsbatch)
++ [IndexDocumentsAction class](/dotnet/api/azure.search.documents.models.indexdocumentsaction)
++ [IndexDocumentsBatch class](/dotnet/api/azure.search.documents.models.indexdocumentsbatch)
 
-Indexing documents in batches significantly improves indexing performance. These batches can be up to 1,000 documents, or up to about 16 MB per batch.
+Indexing documents in batches significantly improves indexing performance. These batches can be up to 1,000 documents or up to about 16 MB per batch.
 
 Determining the optimal batch size for your data is a key component of optimizing indexing speeds. The two primary factors influencing the optimal batch size are:
 
 + The schema of your index
 + The size of your data
 
-Because the optimal batch size is dependent on your index and your data, the best approach is to test different batch sizes to determine what results in the fastest indexing speeds for your scenario.
+Because the optimal batch size depends on your index and your data, the best approach is to test different batch sizes to determine what results in the fastest indexing speeds for your scenario.
 
 The following function demonstrates a simple approach to testing batch sizes.
 
@@ -203,7 +201,7 @@ public static async Task TestBatchSizesAsync(SearchClient searchClient, int min
 }
 ```
 
-Because not all documents are the same size (although they are in this sample), we estimate the size of the data we're sending to the search service. You can do this by using the following function that first converts the object to json and then determines its size in bytes. This technique allows us to determine which batch sizes are most efficient in terms of MB/s indexing speeds.
+Because not all documents are the same size (although they are in this sample), we estimate the size of the data we're sending to the search service. You can do this by using the following function that first converts the object to JSON and then determines its size in bytes. This technique allows us to determine which batch sizes are most efficient in terms of MB/s indexing speeds.
 
 ```csharp
 // Returns size of object in MB
@@ -232,26 +230,26 @@ The function requires a `SearchClient` plus the number of tries you'd like to te
 await TestBatchSizesAsync(searchClient, numTries: 3);
 ```
 
-When you run the function, you should see an output in your console like the following example:
+When you run the function, you should see an output in your console similar to the following example:
 
 :::image type="content" source="media/tutorial-optimize-data-indexing/test-batch-sizes.png" alt-text="Screenshot of the output of test batch size function.":::
 
-Identify which batch size is most efficient and then use that batch size in the next step of the tutorial. You might see a plateau in MB/s across different batch sizes.
+Identify which batch size is most efficient and use that batch size in the next step of this tutorial. You might see a plateau in MB/s across different batch sizes.
 
-## Step 5: Index the data
+## Index the data
 
 Now that you identified the batch size you intend to use, the next step is to begin to index the data. To index data efficiently, this sample:
 
-+ uses multiple threads/workers
-+ implements an exponential backoff retry strategy
++ Uses multiple threads/workers
++ Implements an exponential backoff retry strategy
 
 Uncomment lines 41 through 49, and then rerun the program. On this run, the sample generates and sends batches of documents, up to 100,000 if you run the code without changing the parameters.
 
 ### Use multiple threads/workers
 
-To take full advantage of Azure AI Search's indexing speeds, use multiple threads to send batch indexing requests concurrently to the service.  
+To take advantage of Azure AI Search's indexing speeds, use multiple threads to send batch indexing requests concurrently to the service.  
 
-Several of the key considerations previously mentioned can affect the optimal number of threads. You can modify this sample and test with different thread counts to determine the optimal thread count for your scenario. However, as long as you have several threads running concurrently, you should be able to take advantage of most of the efficiency gains.
+Several of the [key considerations](#key-considerations) can affect the optimal number of threads. You can modify this sample and test with different thread counts to determine the optimal thread count for your scenario. However, as long as you have several threads running concurrently, you should be able to take advantage of most of the efficiency gains.
 
 As you ramp up the requests hitting the search service, you might encounter [HTTP status codes](/rest/api/searchservice/http-status-codes) indicating the request didn't fully succeed. During indexing, two common HTTP status codes are:
 
@@ -260,11 +258,11 @@ As you ramp up the requests hitting the search service, you might encounter [HTT
 
 ### Implement an exponential backoff retry strategy
 
-If a failure happens, requests should be retried using an [exponential backoff retry strategy](/dotnet/architecture/microservices/implement-resilient-applications/implement-retries-exponential-backoff).
+If a failure happens, you should retry requests using an [exponential backoff retry strategy](/dotnet/architecture/microservices/implement-resilient-applications/implement-retries-exponential-backoff).
 
-Azure AI Search's .NET SDK automatically retries 503s and other failed requests but you should implement your own logic to retry 207s. Open-source tools such as [Polly](https://github.com/App-vNext/Polly) can be useful in a retry strategy.
+Azure AI Search's .NET SDK automatically retries 503s and other failed requests, but you should implement your own logic to retry 207s. Open-source tools like [Polly](https://github.com/App-vNext/Polly) can be useful in a retry strategy.
 
-In this sample, we implement our own exponential backoff retry strategy. We start by defining some variables including the `maxRetryAttempts` and the initial `delay` for a failed request:
+In this sample, we implement our own exponential backoff retry strategy. We start by defining some variables, including the `maxRetryAttempts` and the initial `delay` for a failed request.
 
 ```csharp
 // Create batch of documents for indexing
@@ -279,9 +277,9 @@ TimeSpan delay = delay = TimeSpan.FromSeconds(2);
 int maxRetryAttempts = 5;
 ```
 
-The results of the indexing operation are stored in the variable `IndexDocumentResult result`. This variable is important because it allows you to check if any documents in the batch failed, as shown in the following example. If there's a partial failure, a new batch is created based on the failed documents' ID.
+The results of the indexing operation are stored in the variable `IndexDocumentResult result`. This variable allows you to check if documents in the batch failed, as shown in the following example. If there's a partial failure, a new batch is created based on the failed documents' ID.
 
-`RequestFailedException` exceptions should also be caught as they indicate the request failed completely and should also be retried.
+`RequestFailedException` exceptions should also be caught, as they indicate the request failed completely, and retried.
 
 ```csharp
 // Implement exponential backoff
@@ -339,56 +337,56 @@ do
 
 From here, wrap the exponential backoff code into a function so it can be easily called.
 
-Another function is then created to manage the active threads. For simplicity, that function isn't included here but can be found in *ExponentialBackoff.cs*. The function can be called with the following command where `hotels` is the data we want to upload, `1000` is the batch size, and `8` is the number of concurrent threads:
+Another function is then created to manage the active threads. For simplicity, that function isn't included here but can be found in *ExponentialBackoff.cs*. You can call the function using the following command, where `hotels` is the data we want to upload, `1000` is the batch size, and `8` is the number of concurrent threads.
 
 ```csharp
 await ExponentialBackoff.IndexData(indexClient, hotels, 1000, 8);
 ```
 
-When you run the function, you should see an output:
+When you run the function, you should see an output similar to the following example:
 
 :::image type="content" source="media/tutorial-optimize-data-indexing/index-data-start.png" alt-text="Screenshot that shows the output of an index data function.":::
 
-When a batch of documents fails, an error is printed out indicating the failure and that the batch is being retried:
+When a batch of documents fails, an error is printed indicating the failure and that the batch is being retried.
 
 ```
 [Batch starting at doc 6000 had partial failure]
 [Retrying 560 failed documents]
 ```
 
-After the function is finished running, you can verify that all of the documents were added to the index.
+After the function finishes running, you can verify that all of the documents were added to the index.
 
-## Step 6: Explore the index
+## Explore the index
 
-You can explore the populated search index after the program has run either programmatically or by using the [Search explorer](search-explorer.md) in the Azure portal.
+After the program finishes running, you can explore the populated search index either programmatically or using the [Search explorer](search-explorer.md) in the Azure portal.
 
 ### Programatically
 
-There are two main options for checking the number of documents in an index: the [Count Documents API](/rest/api/searchservice/documents/count) and the [Get Index Statistics API](/rest/api/searchservice/indexes/get-statistics). Both paths require time to process so don't be alarmed if the number of documents returned is initially lower than you expect.
+There are two main options for checking the number of documents in an index: the [Count Documents API](/rest/api/searchservice/documents/count) and the [Get Index Statistics API](/rest/api/searchservice/indexes/get-statistics). Both paths require time to process, so don't be alarmed if the number of documents returned is initially lower than you expect.
 
 #### Count Documents
 
-The Count Documents operation retrieves a count of the number of documents in a search index:
+The Count Documents operation retrieves a count of the number of documents in a search index.
 
 ```csharp
 long indexDocCount = await searchClient.GetDocumentCountAsync();
 ```
 
 #### Get Index Statistics
 
-The Get Index Statistics operation returns a document count for the current index, plus storage usage. Index statistics take longer than document count to update.
+The Get Index Statistics operation returns a document count for the current index, plus storage usage. Index statistics take longer to update than document count.
 
 ```csharp
 var indexStats = await indexClient.GetIndexStatisticsAsync(indexName);
 ```
 
 ### Azure portal
 
-In the Azure portal, from the left pane, and find the **optimize-indexing** index in the **Indexes** list.
+In the Azure portal, from the left pane, find the **optimize-indexing** index in the **Indexes** list.
 
 :::image type="content" source="media/tutorial-optimize-data-indexing/portal-output.png" alt-text="Screenshow that shows a list of Azure AI Search indexes.":::
 
-The *Document Count* and *Storage Size* are based on [Get Index Statistics API](/rest/api/searchservice/indexes/get-statistics) and can take several minutes to update.
+The **Document Count** and **Storage Size** are based on the [Get Index Statistics API](/rest/api/searchservice/indexes/get-statistics) and can take several minutes to update.
 
 ## Reset and rerun
 
@@ -406,7 +404,7 @@ You can find and manage resources in the Azure portal, using the **All resources
 
 ## Next step
 
-To learn more about indexing large amounts data, try the following tutorial.
+To learn more about indexing large amounts data, try the following tutorial:
 
 > [!div class="nextstepaction"]
 > [Tutorial: Index large data from Apache Spark using SynapseML and Azure AI Search](search-synapseml-cognitive-services.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プッシュAPIによるインデクシング最適化チュートリアルの更新"
}
```

### Explanation
この変更は、`articles/search/tutorial-optimize-indexing-push-api.md`ファイルの修正を示しており、Azure AI SearchにおけるプッシュAPIを使用したインデクシングの最適化に関するチュートリアルが更新されています。主な目的は、言語の一貫性と説明の明確化です。

具体的な変更内容は以下の通りです：

1. **タイトルの修正**: タイトルが「C# tutorial: Optimize indexing by using the push API」から「C# Tutorial: Optimize Indexing Using the Push API」に変更され、形式が統一されています。

2. **最終更新日の更新**: 最終更新日が「10/14/2024」から「03/28/2025」に変更され、最新の情報が反映されています。

3. **文言の改善**:
   - セクションタイトルの表現が簡略化され（例：「## 1 - Create an Azure AI Search service」から「## Create an Azure AI Search service」）、整然とした印象を与えています。
   - チュートリアル内の説明が明瞭になり、特に「push」と「pull」モデルの説明が改善されました。データの取り込み方法がより直感的に理解できるようになっています。

4. **手順の一貫性**: 各手順が明確に番号付けされ、文書全体の流れがよりスムーズになりました。また、手順の細部が明確化され、実行時の注意点が強調されています。

5. **情報の整理**: インデクシングに関する重要な要素とその説明が整理され、必要な情報が一目でわかるようになりました。特に、インデクシングのパフォーマンスに影響を及ぼす要因についての説明が充実しました。

これらの変更により、Azure AI SearchのプッシュAPIを利用したインデクシングの最適化に関する理解が深まり、ユーザーがチュートリアルを利用しやすくなることが期待されます。また、文書はより簡潔かつ明確になり、技術的な理解を助ける内容に仕上がっています。

## articles/search/tutorial-rag-build-solution-pipeline.md{#item-25ce01}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: tutorial
-ms.date: 01/09/2025
+ms.date: 03/24/2025
 ---
 
 # Tutorial: Build an indexing pipeline for RAG on Azure AI Search
@@ -29,7 +29,7 @@ In this tutorial, you:
 If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
 
 > [!TIP]
-> You can use the [Import and vectorize data wizard](search-import-data-portal.md) to create your pipeline. Try some quickstarts: [Image search](search-get-started-portal-image-search.md) and [Vector search](search-get-started-portal-import-vectors.md).
+> You can use the [Import and vectorize data wizard](search-import-data-portal.md) to create your pipeline. Try some quickstarts [Image search](search-get-started-portal-image-search.md) or [Vector search](search-get-started-portal-import-vectors.md), to learn more about the pipeline and its moving parts.
 
 ## Prerequisites
 
@@ -115,15 +115,15 @@ print(f"{result.name} created")
 
 ## Create a data source connection
 
-In this step, set up the sample data and a connection to Azure Blob Storage. The indexer retrieves PDFs from a container. You create the container and upload files in this step.
+In this step, set up the sample data and a connection from Azure AI Search to Azure Blob Storage. The indexer retrieves PDFs from a container. You create the container and upload files in this step.
 
 The original ebook is large, over 100 pages and 35 MB in size. We broke it up into smaller PDFs, one per page of text, to stay under the [document limit for indexers](search-limits-quotas-capacity.md#indexer-limits) of 16 MB per API call and also the [AI enrichment data limits](search-limits-quotas-capacity.md#data-limits-ai-enrichment). For simplicity, we omit image vectorization for this exercise.
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and find your Azure Storage account.
 
 1. Create a container and upload the PDFs from [earth_book_2019_text_pages](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth_book_2019_text_pages).
 
-1. Make sure Azure AI Search has [**Storage Blob Data Reader** permissions](/azure/role-based-access-control/role-assignments-portal) on the resource.
+1. Make sure your [Azure AI Search managed identity](search-howto-managed-identities-data-sources.md) has a [**Storage Blob Data Reader**](/azure/role-based-access-control/role-assignments-portal) role assignment on Azure Storage.
 
 1. Next, in Visual Studio Code, define an indexer data source that provides connection information during indexing.
 
@@ -148,15 +148,15 @@ The original ebook is large, over 100 pages and 35 MB in size. We broke it up in
     print(f"Data source '{data_source.name}' created or updated")
     ```
 
-If you set up a managed identity for Azure AI Search for the connection, the connection string includes a `ResourceId=` suffix. It should look similar to the following example: `"ResourceId=/subscriptions/FAKE-SUBCRIPTION=ID/resourceGroups/FAKE-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/FAKE-ACCOUNT;"`
+If you set up a [managed identity for an Azure AI Search connection to Azure Storage](search-howto-managed-identities-storage.md), the data source connection string includes a `ResourceId=` suffix. It should look similar to the following example: `"ResourceId=/subscriptions/FAKE-SUBSCRIPTION-ID/resourceGroups/FAKE-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/FAKE-ACCOUNT;"`
 
 ## Create a skillset
 
 Skills are the basis for integrated data chunking and vectorization. At a minimum, you want a Text Split skill to chunk your content, and an embedding skill that create vector representations of your chunked content.
 
 In this skillset, an extra skill is used to create structured data in the index. The [Entity Recognition skill](cognitive-search-skill-entity-recognition-v3.md) is used to identify locations, which can range from proper names to generic references, such as "ocean" or "mountain". Having structured data gives you more options for creating interesting queries and boosting relevance.
 
-The AZURE_AI_MULTISERVICE_KEY is needed even if you're using role-based access control. Azure AI Search uses the key for billing purposes and it's required unless your workloads stay under the free limit. You can also a keyless connection if you're using the most recent preview API or beta packages. For more information, see [Attach an Azure AI services multi-service resource to a skillset](cognitive-search-attach-cognitive-services.md).
+The AZURE_AI_MULTISERVICE_KEY is needed even if you're using role-based access control. Azure AI Search uses the key for billing purposes and it's required unless your workloads stay under the free limit. You can also set up a keyless connection if you're using the most recent preview API or beta packages. For more information, see [Attach an Azure AI services multi-service resource to a skillset](cognitive-search-attach-cognitive-services.md).
 
 ```python
 from azure.search.documents.indexes.models import (
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAG用インデクシングパイプラインのチュートリアル更新"
}
```

### Explanation
この変更は、`articles/search/tutorial-rag-build-solution-pipeline.md`ファイルに対する修正を示しており、Azure AI SearchにおけるRAG（Retrieval-Augmented Generation）用のインデクシングパイプラインの構築に関するチュートリアルが更新されています。主な目的は、情報の明確化と文の一貫性の向上です。

具体的な変更内容は以下の通りです：

1. **最終更新日の更新**: 最終更新日が「01/09/2025」から「03/24/2025」に変更され、新しい情報が反映されています。

2. **文言の改善**: 
   - チュートリアル内のヒント部分で、情報が明確に整理され、「Image search」や「Vector search」というクイックスタートへのリンクが追加され、内容の理解が深まりました。
   - Azure AI SearchとAzure Blob Storageの接続設定に関する説明が具体的に強調され、連携の重要性が明確になっています。

3. **役割の明確化**: 
   - Azure AI Searchの管理対象 ID に関するサポートが強調され、具体的な役割割り当て（**Storage Blob Data Reader**）の必要性についての説明が明確になりました。これにより、ユーザーが必要な権限を正しく理解できます。

4. **接続文字列の説明の強化**: 
   - 接続文字列に関する説明が改善され、管理対象IDを設定する場合の具体的な構造が示されています。これにより、ユーザーが構成を正確に把握しやすくなりました。

5. **情報の追加強化**: 
   - スキルセットの作成に関する情報が拡充され、特に構造化データを扱う重要性が強調されました。これにより、ユーザーは構造化データを作成することが、より効果的なクエリの作成や関連性の向上につながると理解できるようになります。

これらの変更により、ユーザーがRAG用インデクシングパイプラインを効果的に構築できるよう支援し、Azure AI Searchの機能を最大限に活用できるよう情報が明確化されています。文書全体の流れも改善され、ユーザーにとって使いやすいチュートリアルとなっています。

## articles/search/vector-search-how-to-chunk-documents.md{#item-b79133}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 03/11/2025
+ms.date: 03/31/2025
 ---
 
 # Chunk large documents for vector search solutions in Azure AI Search
@@ -20,7 +20,9 @@ We recommend [integrated vectorization](vector-search-integrated-vectorization.m
 
 ## Common chunking techniques
 
-Chunking is only required if the source documents are too large for the maximum input size imposed by models. Here are some common chunking techniques, associated with built-in features if you use [indexers](search-indexer-overview.md) and [skills](cognitive-search-working-with-skillsets.md).
+Chunking is only required if the source documents are too large for the maximum input size imposed by models, but it's also beneficial if content is poorly represented as a single vector. Consider a wiki page that covers a lot of varied sub-topics. The entire page might be small enough to meet model input requirements, but you might get better results if you chunk at a finer grain.
+
+Here are some common chunking techniques, associated with built-in features if you use [indexers](search-indexer-overview.md) and [skills](cognitive-search-working-with-skillsets.md).
 
 | Approach | Usage | Built-in functionality |
 |----------|-------|-----------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおける文書のチャンク処理に関する更新"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-chunk-documents.md`ファイルに対する修正を示しており、Azure AI Searchにおける文書のチャンク処理の方法に関する内容が更新されています。主な目的は、チャンク処理の必要性とその利点を明確にすることです。

具体的な変更内容は以下の通りです：

1. **最終更新日の更新**: 最終更新日が「03/11/2025」から「03/31/2025」に変更され、新しい情報が反映されています。

2. **チャンク処理の利点の追加**: 
   - 文書がモデルによって要求される最大入力サイズを超えている場合だけでなく、内容が単一のベクターとして不適切に表現される場合にもチャンク処理が有益であることが強調されました。具体例として、多様なサブトピックを含むウィキページが挙げられており、全体でモデルの入力要件を満たすサイズであっても、より細かい粒度でチャンク処理を行うことでより良い結果が得られる可能性があることが説明されています。

3. **技術的な情報の整理**: 
   - チャンク処理に関連する一般的な技術の紹介が続き、ビルトイン機能に関する詳細な情報（例：インデクサーやスキルセットの利用）が提示されています。このセクションにより、ユーザーは具体的なチャンク処理のアプローチを簡潔に理解できるようになります。

これらの変更により、ユーザーがAzure AI Searchでのチャンク処理の意義を理解しやすくなり、さまざまなシナリオで文書を効果的に処理できるようになることが期待されます。また、文書全体の流れが整えられ、実践的な情報が提供されています。

## articles/search/vector-search-how-to-quantization.md{#item-744f48}

<details>
<summary>Diff</summary>
````diff
@@ -9,12 +9,12 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 03/31/2025
 ---
 
 # Compress vectors using scalar or binary quantization
 
-Azure AI Search supports scalar and binary quantization for reducing the size of vectors in a search index. Quantization is recommended for reducing vector size because it lowers both memory and disk storage consumption for float16 and float32 embeddings. To offset the effects of lossy compression, you can add oversampling and rescoring over uncompressed vectors.
+Azure AI Search supports scalar and binary quantization for reducing the size of vectors in a search index. Quantization is recommended because it reduces both memory and disk storage for float16 and float32 embeddings. To offset the effects of lossy compression, you can add oversampling and rescoring.
 
 To use built-in quantization, follow these steps:
 
@@ -26,15 +26,15 @@ To use built-in quantization, follow these steps:
 > - Create a new vector profile that uses the named configuration
 > - Create a new vector field having the new vector profile
 > - Load the index with float32 or float16 data that's quantized during indexing with the configuration you defined
-> - Optionally, [query quantized data](#query-a-quantized-vector-field-using-oversampling) using the oversampling parameter if you want to override the default
+> - Optionally, [query quantized data](#query-a-quantized-vector-field-using-oversampling) using the oversampling parameter. If the vector field doesn't specify oversampling in its definition, you can add it at query time.
 
 ## Prerequisites
 
-- [Vector fields in a search index](vector-search-how-to-create-index.md) with a `vectorSearch` configuration, using the Hierarchical Navigable Small Worlds (HNSW) or exhaustive K-nearest neighbor (eKNN) algorithms and a new vector profile.
+- [Vector fields in a search index](vector-search-how-to-create-index.md), with a `vectorSearch` configuration specifying either the Hierarchical Navigable Small Worlds (HNSW) or exhaustive K-nearest neighbor (eKNN) algorithm, and a new vector profile.
 
 ## Supported quantization techniques
 
-Quantization applies to vector fields receiving float-type vectors. In the examples in this article, the field's data type is `Collection(Edm.Single)` for incoming float32 embeddings, but float16 is also supported. When the vectors are received on a field with compression configured, the engine automatically performs quantization to reduce the footprint of the vector data in memory and on disk.
+Quantization applies to vector fields receiving float-type vectors. In the examples in this article, the field's data type is `Collection(Edm.Single)` for incoming float32 embeddings, but float16 is also supported. When the vectors are received on a field with compression configured, the engine performs quantization to reduce the footprint of the vector data in memory and on disk.
 
 Two types of quantization are supported:
 
@@ -43,15 +43,38 @@ Two types of quantization are supported:
 - Binary quantization converts floats into binary bits, which takes up 1 bit. This results in up to 28 times reduced vector index size.
 
 >[!Note]
-> While free services support quantization, they may not demonstrate the full storage savings due to the limited storage quota.
+> While free services support quantization, they don't demonstrate the full storage savings due to the limited storage quota.
+
+## Recommended rescoring techniques
+
+Rescoring is a technique used to offset information loss due to vector compression. It uses oversampling to pick up extra vectors, and supplemental information to rescore initial results found by the query. Supplemental information is either uncompressed original full-precision vectors - or for binary quantization only - you have the option of rescoring using the binary quantized document candidates against the query vector. Rescoring options are specified in the index, but you can invoke rescoring at query time if the index supports it.
+
+API versions determine which rescoring behavior is operational for your code. The most recent preview API supports a new rescoring approach for binary quantization. Indexes created with `2025-03-01-preview` can use the new rescoring behaviors.
+
+| API version | Quantization type | Rescoring properties |
+|-------------|-------------------|------------------|
+| [2024-07-01](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-07-01&preserve-view=true) | Scalar and binary quantization, on vector indexes built using Hierarchical Navigable Small World (HNSW) graphs for similarity search | `rerankWithOriginalVectors` |
+| [2024-11-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true) | Scalar and binary quantization on HNSW graphs | `rescoringOptions.enableRescoring` and `rescoreStorageMethod.preserveOriginals` |
+| [2025-03-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true) | Binary quantization on HNSW graphs | Previous parameter combinations are still supported but binary quantization can now be rescored if original embeddings are deleted: `rescoringOptions.enableRescoring` and `rescoringOptions.rescoreStorageMethod=discardOriginals` |
+
+Only HNSW graphs allow rescoring. Exhaustive K Nearest Neighbors (eKNN) doesn't support rescoring.
+
+<!-- - In version 2024-11-01-preview, set `rescoringOptions.enableRescoring` and `rescoreStorageMethod.preserveOriginals`
+- In version 2025-03-01-preview, set `rescoringOptions.enableRescoring` and `rescoringOptions.rescoreStorageMethod=preserveOriginals` for scalar or binary quantization, or `rescoringOptions.enableRescoring` and `rescoringOptions.rescoreStorageMethod=discardOriginals` for binary quantization only -->
+
+The generalized process for rescoring is:
+
+1. The vector query executes over compressed vector fields.
+1. The vector query returns the top k oversampled candidates.
+1. Oversampled k candidates are rescored using either the uncompressed original vectors, or the dot product of binary quantization. 1. After rescoring, results are adjusted so that more relevant matches appear first.
 
 ## Add "compressions" to a search index
 
-The following example shows a partial index definition with a fields collection that includes a vector field, and a `vectorSearch.compressions` section.
+This section explains how to specify a `vectorsSearch.compressions` section in the index. The following example shows a partial index definition with a fields collection that includes a vector field.
 
-It includes both `scalarQuantization` or `binaryQuantization`. You can specify as many compression configurations as you need, and then assign the ones you want to a vector profile.
+The compression example includes both `scalarQuantization` or `binaryQuantization`. You can specify as many compression configurations as you need, and then assign the ones you want to a vector profile.
 
-Syntax for `vectorSearch.Compressions` varies between stable and preview REST APIs, with the preview adding new options for storage optimization, plus changes to existing syntax. Backwards compatibility is preserved through internal API mappings, but you should adopt the new syntax in code that targets 2024-11-01-preview and future versions.
+Syntax for `vectorSearch.Compressions` varies between stable and preview REST APIs, with the preview adding more options for storage optimization, plus changes to existing syntax. Backwards compatibility is preserved through internal API mappings, but we recommend adopting the newer properties in code that targets 2024-11-01-preview and future versions.
 
 ### [**2024-07-01**](#tab/2024-07-01)
 
@@ -68,23 +91,109 @@ POST https://[servicename].search.windows.net/indexes?api-version=2024-07-01
     { "name": "vectorContent", "type": "Collection(Edm.Single)", "retrievable": false, "searchable": true, "dimensions": 1536,"vectorSearchProfile": "vector-profile-1"},
   ],
   "vectorSearch": {
-        "profiles": [ ],
-        "algorithms": [ ],
+    "profiles": [ 
+      {
+          "name": "vector-profile-1",
+          "algorithm": "use-hnsw",
+          "compression": "use-scalar"
+      }
+    ],
+    "algorithms": [ 
+      {
+        "name": "use-hnsw",
+        "kind": "hnsw",
+        "hnswParameters": { },
+        "exhaustiveKnnParameters": null
+      }
+    ],
+    "compressions": [
+      {
+        "name": "use-scalar",
+        "kind": "scalarQuantization",
+        "scalarQuantizationParameters": {
+          "quantizedDataType": "int8"
+        },
+        "rerankWithOriginalVectors": true,
+        "defaultOversampling": 10
+      },
+      {
+        "name": "use-binary",
+        "kind": "binaryQuantization",
+        "rerankWithOriginalVectors": true,
+        "defaultOversampling": 10
+      }
+    ]
+  }
+}
+```
+
+**Key points**:
+
+- `kind` must be set to `scalarQuantization` or `binaryQuantization`.
+
+- `rerankWithOriginalVectors` uses the original uncompressed vectors to recalculate similarity and rerank the top results returned by the initial search query. The uncompressed vectors exist in the search index even if `stored` is false. This property is optional. Default is true.
+
+- `defaultOversampling` considers a broader set of potential results to offset the reduction in information from quantization. The formula for potential results consists of the `k` in the query, with an oversampling multiplier. For example, if the query specifies a `k` of 5, and oversampling is 20, then the query effectively requests 100 documents for use in reranking, using the original uncompressed vector for that purpose. Only the top `k` reranked results are returned. This property is optional. Default is 4.
+
+- `quantizedDataType` is optional and applies to scalar quantization only. If you add it, it must be set to `int8`. This is the only primitive data type supported for scalar quantization at this time. Default is `int8`.
+
+### [**2024-11-01-preview**](#tab/2024-11-01-preview)
+
+Use the [Create Index (preview)](/rest/api/searchservice/indexes/create?view=rest-searchservice-2024-11-01-preview&preserve-view=true) or [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true) REST API to configure compression settings.
+
+Changes in this version include new `rescoringOptions` that replace `rerankWithOriginalVectors`, and extend the API with more storage options. Notice that `defaultOversampling` is now a property of `rescoringOptions`.
+
+Rescoring options are used to mitigate the effects of lossy comprehension. You can set `rescoringOptions` for scalar or binary quantization.
+
+```http
+POST https://[servicename].search.windows.net/indexes?api-version=2024-11-01-preview
+
+{
+  "name": "my-index",
+  "fields": [
+    { "name": "Id", "type": "Edm.String", "key": true, "retrievable": true, "searchable": true, "filterable": true },
+    { "name": "content", "type": "Edm.String", "retrievable": true, "searchable": true },
+    { "name": "vectorContent", "type": "Collection(Edm.Single)", "retrievable": false, "searchable": true, "dimensions": 1536,"vectorSearchProfile": "vector-profile-1"},
+  ],
+  "vectorSearch": {
+        "profiles": [ 
+          {
+              "name": "vector-profile-1",
+              "algorithm": "use-hnsw",
+              "compression": "use-scalar"
+          }
+        ],
+        "algorithms": [ 
+          {
+            "name": "use-hnsw",
+            "kind": "hnsw",
+            "hnswParameters": { },
+            "exhaustiveKnnParameters": null
+          }
+        ],
         "compressions": [
           {
             "name": "use-scalar",
             "kind": "scalarQuantization",
+            "rescoringOptions": {
+                "enableRescoring": true,
+                "defaultOversampling": 10,
+                "rescoreStorageMethod": "preserveOriginals"
+            },
             "scalarQuantizationParameters": {
               "quantizedDataType": "int8"
             },
-            "rerankWithOriginalVectors": true,
-            "defaultOversampling": 10
+            "truncationDimension": 1024
           },
           {
             "name": "use-binary",
             "kind": "binaryQuantization",
-            "rerankWithOriginalVectors": true,
-            "defaultOversampling": 10
+            "rescoringOptions": {
+                "enableRescoring": true,
+                "defaultOversampling": 10,
+                "rescoreStorageMethod": "preserveOriginals"
+            },
+            "truncationDimension": 1024
           }
         ]
     }
@@ -95,22 +204,28 @@ POST https://[servicename].search.windows.net/indexes?api-version=2024-07-01
 
 - `kind` must be set to `scalarQuantization` or `binaryQuantization`.
 
-- `rerankWithOriginalVectors` uses the original uncompressed vectors to recalculate similarity and rerank the top results returned by the initial search query. The uncompressed vectors exist in the search index even if `stored` is false. This property is optional. Default is true.
+- `rescoringOptions` are a collection of properties used to offset lossy compression by rescoring query results using the original full-precision vectors that exist prior to quantization. For rescoring to work, you must have the vector instance that provides this content. Setting `rescoreStorageMethod` to `discardOriginals` prevents you from using `enableRescoring` or `defaultOversampling`. For more information about vector storage, see [Eliminate optional vector instances from storage](vector-search-how-to-storage-options.md).
+
+- `"rescoreStorageMethod": "preserveOriginals"` is the API equivalent of `"rerankWithOriginalVectors": true`. Rescoring vector search results with the original full-precision vectors can result in adjustments to search score and rankings, promoting the more relevant matches as determined by the rescoring step.
 
 - `defaultOversampling` considers a broader set of potential results to offset the reduction in information from quantization. The formula for potential results consists of the `k` in the query, with an oversampling multiplier. For example, if the query specifies a `k` of 5, and oversampling is 20, then the query effectively requests 100 documents for use in reranking, using the original uncompressed vector for that purpose. Only the top `k` reranked results are returned. This property is optional. Default is 4.
 
 - `quantizedDataType` is optional and applies to scalar quantization only. If you add it, it must be set to `int8`. This is the only primitive data type supported for scalar quantization at this time. Default is `int8`.
 
-### [**2024-11-01-preview**](#tab/2024-11-01-preview)
+- `truncationDimension` is a preview feature that taps inherent capabilities of the text-embedding-3 models to "encode information at different granularities and allows a single embedding to adapt to the computational constraints of downstream tasks" (see [Matryoshka Representation Learning](https://arxiv.org/abs/2205.13147)). You can use truncated dimensions with or without rescoring options. For more information about how this feature is implemented in Azure AI Search, see [Truncate dimensions using MRL compression](vector-search-how-to-truncate-dimensions.md).
 
-Use the [Create Index (preview)](/rest/api/searchservice/indexes/create?view=rest-searchservice-2024-11-01-preview&preserve-view=true) or [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true) REST API to configure compression settings.
+### [**2025-03-01-preview**](#tab/2025-03-01-preview)
 
-Changes in this version include new `rescoringOptions` that replace `rerankWithOriginalVectors`, and extend the API with more storage options. Notice that `defaultOversampling` is now a property of `rescoringOptions`.
+Use the [Create Index (preview)](/rest/api/searchservice/indexes/create?view=rest-searchservice-2025-031-01-preview&preserve-view=true) or [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true) REST API to configure compression settings.
 
-Rescoring options are used to mitigate the effects of lossy comprehension. You can set `rescoringOptions` for scalar or binary quantization.
+Changes in this version include new guidance for *binary quantization*. If you set `enableRescoring` to true, you can set `rescoreStorageMethod` to `discardOriginals` to further reduce storage, without reducing quality. 
+
+Azure AI Search supports a lossy rescoring option on the binary quantized document vectors, which helps close the quality gap between no rescoring and full-precision rescoring when using `binaryQuantization`.
+
+For scalar quantization, there are no rescoring changes in this preview.
 
 ```http
-POST https://[servicename].search.windows.net/indexes?api-version=2024-11-01-preview
+POST https://[servicename].search.windows.net/indexes?api-version=2025-03-01-preview
 
 {
   "name": "my-index",
@@ -120,8 +235,21 @@ POST https://[servicename].search.windows.net/indexes?api-version=2024-11-01-pre
     { "name": "vectorContent", "type": "Collection(Edm.Single)", "retrievable": false, "searchable": true, "dimensions": 1536,"vectorSearchProfile": "vector-profile-1"},
   ],
   "vectorSearch": {
-        "profiles": [ ],
-        "algorithms": [ ],
+        "profiles": [ 
+          {
+              "name": "vector-profile-1",
+              "algorithm": "use-hnsw",
+              "compression": "use-binary"
+          }
+        ],
+        "algorithms": [ 
+          {
+            "name": "use-hnsw",
+            "kind": "hnsw",
+            "hnswParameters": { },
+            "exhaustiveKnnParameters": null
+          }
+        ],
         "compressions": [
           {
             "name": "use-scalar",
@@ -142,7 +270,7 @@ POST https://[servicename].search.windows.net/indexes?api-version=2024-11-01-pre
             "rescoringOptions": {
                 "enableRescoring": true,
                 "defaultOversampling": 10,
-                "rescoreStorageMethod": "preserveOriginals"
+                "rescoreStorageMethod": "discardOriginals"
             },
             "truncationDimension": 1024
           }
@@ -155,21 +283,21 @@ POST https://[servicename].search.windows.net/indexes?api-version=2024-11-01-pre
 
 - `kind` must be set to `scalarQuantization` or `binaryQuantization`.
 
-- `rescoringOptions` are a collection of properties used to offset lossy compression by rescoring query results using the original full-precision vectors that exist prior to quantization. For rescoring to work, you must have the vector instance that provides this content. Setting `rescoreStorageMethod` to `discardOriginals` prevents you from using `enableRescoring` or `defaultOversampling`. For more information about vector storage, see [Eliminate optional vector instances from storage](vector-search-how-to-storage-options.md).
+- `rescoringOptions` are a collection of properties used to offset lossy compression by rescoring query results using the original full-precision vectors that exist prior to quantization.
 
-- `"rescoreStorageMethod": "preserveOriginals"` is the API equivalent of `"rerankWithOriginalVectors": true`. Rescoring vector search results with the original full-precision vectors can result in adjustments to search score and rankings, promoting the more relevant matches as determined by the rescoring step.
+- `enableRescoring` rescores the initial results obtained by query execution over compressed data. For scalar quantization, rescoring uses uncompressed vectors to produce more relevant results and takes a dependency on `preserveOriginals`. For binary quantization, rescoring is the same as scalar quantization if you preserve originals, but you can also discard originals and still get rescoring. In this scenario, rescoring is calculated by the dot product of the full precision query and binary quantized data in the index.  
 
-- `defaultOversampling` considers a broader set of potential results to offset the reduction in information from quantization. The formula for potential results consists of the `k` in the query, with an oversampling multiplier. For example, if the query specifies a `k` of 5, and oversampling is 20, then the query effectively requests 100 documents for use in reranking, using the original uncompressed vector for that purpose. Only the top `k` reranked results are returned. This property is optional. Default is 4.
+- `"rescoreStorageMethod": "discardOriginals"` removes original vectors. These aren't needed for binary quantization.
 
-- `quantizedDataType` is optional and applies to scalar quantization only. If you add it, it must be set to `int8`. This is the only primitive data type supported for scalar quantization at this time. Default is `int8`.
+- `defaultOversampling` considers a broader set of potential results to offset the reduction in information from quantization. The formula for potential results consists of the `k` in the query, with an oversampling multiplier. For example, if the query specifies a `k` of 5, and oversampling is 20, then the query effectively requests 100 documents for use in reranking, using the original uncompressed vector for that purpose. Only the top `k` reranked results are returned. This property is optional. Default is 4.
 
 - `truncationDimension` is a preview feature that taps inherent capabilities of the text-embedding-3 models to "encode information at different granularities and allows a single embedding to adapt to the computational constraints of downstream tasks" (see [Matryoshka Representation Learning](https://arxiv.org/abs/2205.13147)). You can use truncated dimensions with or without rescoring options. For more information about how this feature is implemented in Azure AI Search, see [Truncate dimensions using MRL compression](vector-search-how-to-truncate-dimensions.md).
 
 ---
 
 ## Add the vector search algorithm
 
-You can use HNSW algorithm or exhaustive KNN in the 2024-11-01-preview REST API. For the stable version, use HNSW only.
+You can use HNSW algorithm or exhaustive KNN in the 2024-11-01-preview REST API or later. For the stable version, use HNSW only. If you want rescoring, you must choose HNSW.
 
    ```json
    "vectorSearch": {
@@ -240,15 +368,15 @@ Scalar quantization reduces the resolution of each number within each vector emb
 
 Each component of the vector is mapped to the closest representative value within this set of quantization levels in a process akin to rounding a real number to the nearest integer. In the quantized 8-bit vector, the identifier number stands in place of the original value. After quantization, each vector is represented by an array of identifiers for the bins to which its components belong. These quantized vectors require much fewer bits to store compared to the original vector, thus reducing storage requirements and memory footprint.
 
-## How  binary quantization works in Azure AI Search
+## How binary quantization works in Azure AI Search
 
 Binary quantization compresses high-dimensional vectors by representing each component as a single bit, either 0 or 1. This method drastically reduces the memory footprint and accelerates vector comparison operations, which are crucial for search and retrieval tasks. Benchmark tests show up to 96% reduction in vector index size.
 
-It's particularly effective for embeddings with dimensions greater than 1024. For smaller dimensions, we recommend testing the quality of binary quantization, or trying scalar instead. Additionally, we’ve found BQ performs very well when embeddings are centered around zero. Most popular embedding models such as OpenAI, Cohere, and Mistral are centered around zero.
+It's particularly effective for embeddings with dimensions greater than 1024. For smaller dimensions, we recommend testing the quality of binary quantization, or trying scalar instead. Additionally, we’ve found binary quantization performs very well when embeddings are centered around zero. Most popular embedding models such as OpenAI, Cohere, and Mistral are centered around zero.
 
 ## Query a quantized vector field using oversampling
 
-Query syntax for a compressed or quantized vector field is the same as for noncompressed vector fields, unless you want to override parameters associated with oversampling or rescoring with original vectors.
+Query syntax for a compressed or quantized vector field is the same as for noncompressed vector fields, unless you want to override parameters associated with oversampling and rescoring. You can add an o`versampling` parameter to invoke oversampling and rescoring at query time.
 
 ### [**2024-07-01**](#tab/query-2024-07-01)
 
@@ -302,22 +430,34 @@ POST https://[service-name].search.windows.net/indexes/demo-index/docs/search?ap
 
 **Key points**:
 
-- Applies to vector fields that undergo vector compression, per the vector profile assignment.
+- Oversampling applies to vector fields that undergo vector compression, per the vector profile assignment.
 
-- Overrides the `defaultOversampling` value or introduces oversampling at query time, even if the index's compression configuration didn't specify oversampling or reranking options.
+- Oversampling in the query overrides the `defaultOversampling` value in the index, or invokes oversampling and rescoring at query time, even if the index's compression configuration didn't specify oversampling or reranking options.
 
----
+### [**2025-03-01-preview**](#tab/query-2025-03-01-preview)
+
+The latest preview API is identical to the previous preview API in terms of `vectorQueries` specification. As with the previous version, we recommend oversampling as mitigation for lossy compression.
+
+```http
+POST https://[service-name].search.windows.net/indexes/demo-index/docs/search?api-version=2025-03-01-preview
+
+{    
+    "vectorQueries": [
+        {    
+            "kind": "vector",    
+            "vector": [8, 2, 3, 4, 3, 5, 2, 1],    
+            "fields": "myvector",
+            "oversampling": 12.0,
+            "k": 5   
+        }
+  ]    
+}
+```
 
-<!-- 
-RESCORE WITH ORIGINAL VECTORS -- NEEDS AN H2 or H3
-It's used to rescore search results obtained used compressed vectors.
+**Key points**:
+
+- Oversampling applies to vector fields that undergo vector compression, per the vector profile assignment.
 
-Rescore with original vectors
-After the initial query, rescore results using uncompressed vectors
- 
-For "enableRescoring", we provide true or false options. if it's true, the query will first retrieve using compressed vectors, then rescore results using uncompressed vectors.
+- Oversampling in the query overrides the `defaultOversampling` value in the index, or invokes oversampling and rescoring at query time, even if the index's compression configuration didn't specify oversampling or reranking options.
 
-Step one: Vector query executes using the compressed vectors.
-Step two: Query returns the top oversampling k-matches.
-Step three: Oversampling k-matches are rescored using the uncompressed vectors, adjusting the scores and ranking so that more relevant matches appear first.
- -->
+---
````
</details>

### Summary

```json
{
    "modification_type": "major update",
    "modification_title": "Azure AI Searchにおけるベクトル量子化の詳細なガイド"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-quantization.md`ファイルに対する大規模な修正を示しており、Azure AI Searchにおけるベクトルの量子化に関する内容が大幅に更新されています。主な目的は、量子化技術に関する情報の充実と、実践的なガイダンスの提供です。

具体的な変更内容は以下の通りです：

1. **最終更新日の更新**: 最終更新日が「11/19/2024」から「03/31/2025」に変更され、新しい情報が反映されています。

2. **量子化の重要性と利点の強調**: 
   - ベクトルのサイズを減少させるためのスカラーおよびバイナリ量子化の機能が強調されています。特に、メモリとディスクストレージの消費を減少させるために、どのように量子化が効果的であるかが説明されています。

3. **実装ステップの詳細化**:
   - 量子化を使用するための具体的なステップや、オプションのパラメーター（例：オーバーサンプリング）に関する指示が加わりました。ユーザーが量子化されたデータをクエリする場合の方法も具体的に記載されています。

4. **リスコアリング技術の導入**:
   - リスコアリングとは、情報損失を補うために元のベクトルを用いて検索結果を再評価する技術です。このセクションでは、リスコアリングを使用する方法や、リスコアリングオプションに関する詳細が更新されています。支援するAPIバージョンやプロパティの変更についても詳述されています。

5. **量子化技術の種類と特徴**:
   - 空間、スカラーおよびバイナリ量子化の説明が強化され、各技術がどのように機能するか、どのような場合に推奨されるかが具体的に書かれています。

6. **構文の変更と新機能の説明**:
   - インデックス定義や構文に関する変更点が詳述され、新しいプロパティや推奨される構文も紹介されています。

7. **オーバーサンプリングと検索クエリの改善**:
   - クエリでのオーバーサンプリングの適用方法や、検索時に使用する際の具体的なシナリオも記載されており、ユーザーにターゲットデータをより正確に取得するための機会を与えています。

これらの変更は、Azure AI Searchでのベクトル量子化に関する理解を深め、ユーザーが効率的にデータを処理できるように設計されています。また、情報が包括的で実用的であるため、特に新規ユーザーや開発者にとって有益なリソースとなっています。

## articles/search/vector-search-how-to-storage-options.md{#item-ee1680}

<details>
<summary>Diff</summary>
````diff
@@ -9,41 +9,44 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 03/31/2025
 ---
 
 # Eliminate optional vector instances from storage
 
 Azure AI Search stores multiple copies of vector fields that are used in specific workloads. If you don't need to support a specific behavior, like returning raw vectors in a query response, you can set properties in the index that omit storage for that workload.
 
+Removing storage is irreversible and requires reindexing if you want it back.
+
 ## Prerequisites
 
-- [Vector fields in a search index](vector-search-how-to-create-index.md) with a `vectorSearch` configuration, using the Hierarchical Navigable Small Worlds (HNSW) or exhaustive K-nearest neighbor (KNN) algorithms and a new vector profile.
+- [Vector fields in a search index](vector-search-how-to-create-index.md), with a `vectorSearch` configuration specifying either the Hierarchical Navigable Small Worlds (HNSW) or exhaustive K-nearest neighbor (KNN) algorithm, and a new vector profile.
 
 ## How vector fields are stored
 
-For every vector field, there could be three copies of the vectors, each serving a different purpose:
+For every vector field, there are up to three copies of the vectors, each serving a different purpose:
 
 | Instance | Usage | Controlled using |
-|----------|-------|------------|
-| Source vectors which store the JSON that was received during document indexing (JSON data) | Used for incremental data refresh with `merge` or `mergeOrUpload` during document indexing. Also used if you want "retrievable" vectors returned in the query response. | `stored` property on vector fields |
-| Original full-precision vectors (binary data) | In existing indexes, these are used for internal index operations and for exhaustive KNN search. For vectors using compression, it's also used for rescoring (if enabled) on an oversampled candidate set of results from ANN search on vector fields using [scalar or binary quantization](vector-search-how-to-quantization.md) compression. | `rescoringOptions.rescoreStorageMethod` property in `vectorSearch.compressions`. For *uncompressed* vector fields on indexes created with `2024-11-01-Preview` API versions and later, this will be omitted by default with no impact on search activities nor quality. |
-| Vectors in the [HNSW graph for Approximate Nearest Neighbors (ANN) search](vector-search-overview.md) (HNSW graph) | Used for ANN query execution. Consists of either full-precision vectors (when no compression is applied) or quantized vectors (when compression is applied) | Only applies to HNSW. These data structures are required for efficient ANN search. |
+|----------|-------|------------------|
+| Source vectors received during document indexing (JSON data) | Used for incremental data refresh with `merge` or `mergeOrUpload` indexing action. Also used to return "retrievable" vectors in the query response. | `stored` property on vector fields |
+| Original full-precision vectors (binary data) | Used for internal index operations and for exhaustive KNN search in older API versions. For compressed vectors, it's also used for `preserveOriginals` rescoring on an oversampled candidate set of results from ANN search. This applies to vector fields that undergo [scalar or binary quantization](vector-search-how-to-quantization.md). | `rescoringOptions.rescoreStorageMethod` property in `vectorSearch.compressions`. |
+| Vectors in the [HNSW graph for Approximate Nearest Neighbors (ANN) search](vector-search-overview.md) (HNSW graph) or vectors for exhaustive K Nearest Neighbors (eKNN index) | Used for query execution. Consists of either full-precision vectors (when no compression is applied) or quantized vectors. | Essential. There are no parameters for removing this instance. |
+
+You can set properties that permanently discard the first two instances (JSON data and binary data) from vector storage, but not the last instance.
 
-You can set properties that permanently discard the first two instances (JSON data and binary data) from vector storage.
+To offset lossy compression for HNSW, you can keep the second instance (binary data) for rescoring purposes to improve ANN search quality. For eKNN, only scalar quantization is supported, and rescoring isn't an option. In newer API versions like the latest preview, the second instance isn't kept for eKNN because the third instance provides full-precision vectors in an eKNN index.
 
-The last instance (HNSW graph) is required for ANN vector query execution. If any compression techniques such as [scalar or binary quantization](vector-search-how-to-quantization.md) are used, they are applied to this set of data. If you want to offset lossy compression, you should keep the second instance (binary data) for rescoring purposes to improve ANN search quality.
+### Indexes created with 2024-11-01-preview or later API versions
 
-### Indexes created on or after 2024-11-01-preview API version
-For indexes created with the 2024-11-01-preview API version with uncompressed vector fields, the second and third instances (binary data and HNSW graph) are combined as part of our cost reduction investments, reducing overall storage. The same index created with the 2024-11-01-preview API is functionally equivalent but uses less storage compared to identical indexes created with earlier API versions. Physical data structures are established on a Create Index request, so you must delete and recreate the index to realize the storage reductions.
+For indexes created with the 2024-11-01-preview or a later API with uncompressed vector fields, the second and third instances (binary data and HNSW graph) are combined as part of our cost reduction investments, reducing overall storage. A newer generation index with consolidated vectors is functionally equivalent to older indexes, but uses less storage. Physical data structures are established on a Create Index request, so you must delete and recreate the index to realize the storage reductions.
 
-If you choose to use [vector compression](vector-search-how-to-configure-compression-storage.md), we compress (quantize) the in-memory portion of the vector index. Since memory is often a primary constraint for vector indexes, this allows storing more vectors within the same search service. However, lossy compression results in some information loss, which can impact search quality.
+If you choose [vector compression](vector-search-how-to-configure-compression-storage.md), AI Search compresses (quantizes) the in-memory portion of the vector index. Since memory is often a primary constraint for vector indexes, this practice allows you to store more vectors within the same search service. However, lossy compression equates to less information in the index, which can affect search quality.
 
-To mitigate this, enabling "rescoring" and "oversampling" helps maintain accuracy. This retrieves a larger set of candidate documents from the compressed index and then recomputes similarity scores using the original vectors, which must be retained in storage. As a result, while quantization reduces memory usage (vector index size usage), it slightly increases storage requirements since both compressed and original vectors are stored. The additional storage is approximately equal to the size of the compressed index.
+To mitigate the loss in information, you can [enable "rescoring" and "oversampling" options](vector-search-how-to-quantization.md#recommended-rescoring-techniques) to help maintain quality. The effect is retrieval of a larger set of candidate documents from the compressed index, with recomputation of similarity scores using the original vectors or the dot product. For rescoring to work, original vectors must be retained in storage for certain scenarios. As a result, while quantization reduces memory usage (vector index size usage), it slightly increases storage requirements since both compressed and original vectors are stored. The extra storage is approximately equal to the size of the compressed index.
 
-## Set the `stored` property
+## Remove source vectors (JSON data)
 
-The `stored` property is a boolean property on a vector field definition that determines whether storage is allocated for retrievable vector field content (the source instance). The `stored` property is true by default. If you don't need raw vector content in a query response, you can save up to 50 percent storage per field by changing `stored` to false.
+The `stored` property is a boolean property on a vector field definition that determines whether storage is allocated for retrievable vector field content obtained during indexing (the source instance). The `stored` property is true by default. If you don't need raw vector content in a query response, you can save up to 50 percent storage per field by changing `stored` to false.
 
 Considerations for setting `stored` to false:
 
@@ -52,7 +55,7 @@ Considerations for setting `stored` to false:
 - However, if your indexing strategy includes [partial document updates](search-howto-reindex.md#update-content), such as "merge" or "mergeOrUpload" on an existing document, setting `stored=false` prevents content updates to those fields during the merge. On each "merge" or "mergeOrUpload" operation to a search document, you must provide the vector fields in its entirety, along with the nonvector fields that you're updating, or the vector is dropped.
 
 > [!IMPORTANT]
-> Setting the `stored=false` attribution is irreversible. This property can only be set when you create the index and is only allowed on vector fields. Updating an existing index with new vector fields cannot set this property to `false`. If you want retrievable vector content later, you must drop and rebuild the index, or create and load a new field that has the new attribution.
+> Setting the `stored=false` attribution is irreversible. This property can only be set when you create the index and is only allowed on vector fields. Updating an existing index with new vector fields can't set this property to `false`. If you want retrievable vector content later, you must drop and rebuild the index, or create and load a new field that has the new attribution.
 
 For new vector fields in a search index, set `stored` to false to permanently remove retrievable storage for the vector field. The following example shows a vector field definition with the `stored` property.
 
@@ -86,31 +89,44 @@ PUT https://[service-name].search.windows.net/indexes/demo-index?api-version=202
 
 - Defaults are `stored` set to true and `retrievable` set to false. In a default configuration, a retrievable copy is stored, but it's not automatically returned in results. When `stored` is true, you can toggle `retrievable` between true and false at any time without having to rebuild an index. When `stored` is false, `retrievable` must be false and can't be changed.
 
-## Set the `rescoreStorageMethod` property
+## Remove full-precision vectors (binary data)
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-The `rescoreStorageMethod` property controls the storage of full-precision vectors when compression is used.
+When you compress vectors using either scalar or binary quantization, query execution is over the quantized vectors. In this case, you only need the original full-precision vectors (binary data) if you want to rescore.
 
-For *uncompressed* vector fields on indexes created with `2024-11-01-Preview` API versions and later, this will be omitted by default with no impact on search activities nor quality. For existing vector fields created prior to this API version, there is no in-place ability to remove this copy of data.
+If you use newer preview APIs *and* binary quantization, you can safely discard full-precision vectors because rescoring strategies now use the dot product of a binary embedding, which produces high quality search results, without having to reference full-precision vectors in the index.
 
-On a vector compression, the `rescoreStorageMethod` property is set to `preserveOriginals` by default, which retains full-precision vectors for[oversampling and rescoring capabilities](vector-search-how-to-quantization.md#add-compressions-to-a-search-index) to reduce the effect of lossy compression on the HNSW graph. If you don't use these capabilities, you can reduce vector storage by setting `rescoreStorageMethod` to `discardOriginals`.
+The `rescoreStorageMethod` property controls whether full-precision vectors are stored. The guidance for whether to retain full-precision vectors is:
 
-> [!IMPORTANT]
-> Setting the `rescoreStorageMethod` property is irreversible and will have different levels of search quality loss depending on the compression method. This can be set on indexes created with `2024-11-01-Preview` or later, either during index creation or adding new vector fields.
+- For scalar quantization, preserve original full-precision vectors in the index because they're required for rescore.
+- For binary quantization, preserve original full-precision vectors for the highest quality of rescoring, or discard full-precision vectors (requires 2025-03-01-preview) if you want to rescore based on the dot product of the binary embeddings.
+
+Vector storage strategies have been evolving over the last several releases. Index creation date and API version determine your storage options. 
+
+| API version | Applies to | Remove full-precision vectors |
+|-------------|-------------------------------|
+| 2024-07-01 and earlier | Not applicable. | There's no mechanism for removing full-precision vectors. |
+| 2024-11-01-preview | Binary embeddings | Use `rescoreStorageMethod.discardOriginals` to remove full-precision vectors, but doing so prevents rescoring. `enableRescoring` must be false if originals are gone.|
+| 2025-03-01-preview | Binary embeddings | Use `rescoreStorageMethod.discardOriginals` to remove full-precision vectors in the index while still retaining rescore options. In this preview, rescoring is possible because the technique changed. The dot product of the binary embeddings is used on the rescore, producing high quality search results equivalent to or better than earlier techniques based on full-precision vectors. |
 
-If you intend to use scalar or binary quantization, we recommend retaining `rescoreStorageMethod` set to `preserveOriginals` to maximize search quality.
+Notice that scalar isn't listed in the table. If you use scalar quantization, you must retain original full-precision vectors if you want to rescore.
+
+In `vectorSearch.compressions`, the `rescoreStorageMethod` property is set to `preserveOriginals` by default, which retains full-precision vectors for [oversampling and rescoring capabilities](vector-search-how-to-quantization.md#add-compressions-to-a-search-index) to reduce the effect of lossy compression on the HNSW graph. If you don't need full-precision vectors, you can reduce vector storage by setting `rescoreStorageMethod` to `discardOriginals`.
+
+> [!IMPORTANT]
+> Setting the `rescoreStorageMethod` property is irreversible and can adversely affect search quality, although the degree depends on the compression method and any mitigations you apply.
 
 To set this property:
 
-1. Use [Create Index](/rest/api/searchservice/indexes/create?view=rest-searchservice-2024-11-01-preview&preserve-view=true) or [Create or Update Index 2024-11-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true) REST APIs, or an Azure SDK beta package providing the feature.
+1. Use [Create Index (preview)](/rest/api/searchservice/indexes/create?view=rest-searchservice-2025-03-01-preview&preserve-view=true) or [Create or Update Index (preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true) REST APIs, or an Azure SDK beta package providing the feature.
 
 1. Add a `vectorSearch` section to your index with profiles, algorithms, and compressions.
 
-1. Under compressions, add `rescoringOptions` with `enableRescoring` set to true, `defaultOversampling` set to a positive integer, and `rescoreStorageMethod` set to `preserveOriginals`.
+1. Under `vectorSearch.compressions`, add `rescoringOptions` with `enableRescoring` set to true, `defaultOversampling` set to a positive integer, and `rescoreStorageMethod` set to `discardOriginals` for binary quantization and `preserveOriginals` for scalar quantization.
 
     ```http
-    PUT https://[service-name].search.windows.net/indexes/demo-index?api-version=2024-11-01-preview
+    PUT https://[service-name].search.windows.net/indexes/demo-index?api-version=2025-03-01-preview
     
     {
         "name": "demo-index",
@@ -119,9 +135,14 @@ To set this property:
         "vectorSearch": {
             "profiles": [
                 {
-                "name": "myVectorProfile",
+                "name": "myVectorProfile-1",
                 "algorithm": "myHnsw",
                 "compression": "myScalarQuantization"
+                },
+                {
+                "name": "myVectorProfile-2",
+                "algorithm": "myHnsw",
+                "compression": "myBinaryQuantization"
                 }
             ],
             "algorithms": [
@@ -150,6 +171,16 @@ To set this property:
                         "quantizedDataType": "int8"
                     },
                     "truncationDimension": null
+                },
+                {
+                    "name": "myBinaryQuantization",
+                    "kind": "binaryQuantization",
+                    "rescoringOptions": {
+                        "enableRescoring": true,
+                        "defaultOversampling": 10,
+                        "rescoreStorageMethod": "discardOriginals"
+                    },
+                    "truncationDimension": null
                 }
             ]
         }
````
</details>

### Summary

```json
{
    "modification_type": "major update",
    "modification_title": "Azure AI Searchにおけるベクトルストレージオプションのアップデート"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-storage-options.md`ファイルに対する重要な修正を示しており、Azure AI Searchにおけるベクトルのストレージオプションに関する情報が大幅に更新されています。主に、ストレージ管理のための新たなポリシーと実践が導入されています。

具体的な変更内容は以下の通りです：

1. **最終更新日の更新**: 最終更新日が「11/19/2024」から「03/31/2025」に変更され、新しい情報が反映されています。

2. **ベクトルストレージの重要性と実践**:
   - 変更では、ベクトルフィールドのストレージ方法に関する詳細な説明が追加されています。使用するワークロードに応じてストレージを制御するためのプロパティが導入され、それに基づき不要なストレージを削除する方法が明示されています。

3. **ストレージ削除の不可逆性**:
   - ストレージを削除することが不可逆であるため、将来的に再利用する場合には再インデックス化が必要であることが強調されています。

4. **ベクトルインスタンスの管理**:
   - 各ベクトルフィールドに対して最大３つのベクトルコピーが存在し、それぞれ異なる目的で使用されることが解説されています。ソースベクトル、元の高精度ベクトル、HNSWグラフを利用した近傍検索のためのベクトルの役割について、詳しく説明されています。

5. **APIバージョンに基づくストレージ戦略**:
   - 特に2024-11-01-preview以降に作成されたインデックスの構造が更新され、ストレージの効率化が図られています。また、最新のAPIを利用した際のストレージ管理の選択肢についても触れられています。

6. **量子化およびリスコアリングの説明の新規追加**:
   - ベクトルの圧縮技術や、情報損失を抑えるためのリスコアリングの利用についても詳しく解説されています。リスコアリングを有効にすることで検索の精度が向上する仕組みが説明されています。

7. **設定手順が明確に提示**:
   - ベクトルフィールドの`stored`プロパティや`rescoreStorageMethod`プロパティに関する詳細な設定手順が提供され、特に新しいインデックスを作成する際の注意点が強調されています。

これらの変更により、Azure AI Searchを使用する際のベクトルストレージに関する知識が深まり、ユーザーがより効果的かつ効率的にリソースを管理できるようになります。また、文書の内容が具体的で実用的なガイダンスを提供しているため、特に開発者やデータサイエンティストにとって価値あるリソースとなっています。

## articles/search/vector-search-index-size.md{#item-bb2846}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: conceptual
-ms.date: 01/09/2025
+ms.date: 03/20/2025
 ---
 
 # Vector index size and staying under limits
@@ -24,7 +24,7 @@ For each vector field, Azure AI Search constructs an internal vector index using
 > [Vector optimization techniques](vector-search-how-to-configure-compression-storage.md) are now generally available. Use capabilities like narrow data types, scalar and binary quantization, and elimination of redundant storage to reduce your vector quota and storage quota consumption.
 
 > [!NOTE]
-> Not all algorithms consumes vector index size quota. Vector quotas are established based on memory requirements of approximate nearest neighbor search. Vector fields created with the Hierarchical Navigable Small World (HNSW) algorithm need to reside in memory during query execution because of the random-access nature of graph-based traversals. Vector fields using exhaustive KNN algorithm are loaded into memory dynamically in pages during query execution, and as a result do not consume vector quota.
+> Not all algorithms consume vector index size quota. Vector quotas are established based on memory requirements of approximate nearest neighbor search. Vector fields created with the Hierarchical Navigable Small World (HNSW) algorithm need to reside in memory during query execution because of the random-access nature of graph-based traversals. Vector fields using exhaustive KNN algorithm are loaded into memory dynamically in pages during query execution, and as a result do not consume vector quota.
 
 ## Key points about quota and vector index size
 
@@ -38,29 +38,11 @@ For each vector field, Azure AI Search constructs an internal vector index using
 
 If you aren't sure what your search service limits are, here are two ways to get that information:
 
-+ In the Azure portal, in the search service **Overview** page, both the **Properties** tab and **Usage** tab show partition size and storage, and also vector quota and vector index size.
++ In the Azure portal, on the search service **Overview** page, both the **Properties** tab and **Usage** tab show partition size and storage, and also vector quota and vector index size.
 
-+ In the Azure portal, in the **Scale** page, you can review the number and size of partitions.
++ In the Azure portal, on the **Scale** page, you can review the number and size of partitions.
 
-## How to check service creation date
-
-Newer services created after April 3, 2024 offer five to ten times more vector storage as older ones at the same tier billing rate. If your service is older, consider creating a new service and migrating your content.
-
-1. In Azure portal, open the resource group that contains your search service.
-
-1. On the leftmost pane, under **Settings**, select **Deployments**.
-
-1. Locate your search service deployment. If there are many deployments, use the filter to look for "search".
-
-1. Select the deployment. If you have more than one, click through to see if it resolves to your search service.
-
-    :::image type="content" source="media/vector-search-index-size/resource-group-deployments.png" lightbox="media/vector-search-index-size/resource-group-deployments.png" alt-text="Screenshot of a filtered deployments list.":::
-
-1. Expand deployment details. You should see *Created* and the creation date.
-
-   :::image type="content" source="media/vector-search-index-size/deployment-details.png" lightbox="media/vector-search-index-size/deployment-details.png" alt-text="Screenshot of the deployment details showing creation date.":::
-
-1. Now that you know the age of your search service, review the vector quota limits based on service creation: [Vector index size limits](search-limits-quotas-capacity.md#vector-index-size-limits).
+Your vector limit varies depending on your [service creation date](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date).
 
 ## How to get vector index size
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルインデックスサイズと制限に関する情報の更新"
}
```

### Explanation
この変更は、`articles/search/vector-search-index-size.md`ファイルに対する軽微な修正を示しており、Azure AI Searchにおけるベクトルインデックスのサイズと制限に関する情報が更新されています。主な変更点として、新しい日付の反映と、一部の文の表現が明確化されています。

具体的な変更内容は以下の通りです：

1. **最終更新日の更新**: 最終更新日が「01/09/2025」から「03/20/2025」に変更されています。これは文書が最新の情報を反映していることを示しています。

2. **文法の修正**: 特定の文節において、文法的な間違いが修正され、よりスムーズな表現となっています。例えば、「consumes」から「consume」への修正が行われ、適切な単数・複数の用法が使われています。

3. **情報の明確化**: 
   - Azureポータル内でのベクトルインデックスサイズ確認手順に関して、「in the Azure portal, in the search service **Overview** page」から「in the Azure portal, on the search service **Overview** page」に表現が変更され、情報がより明確に提示されています。

4. **不要部分の削除**: サービスの作成日を確認するための手順が削除され、これにより文書が簡潔になりました。今後は、サービス作成日によるベクトル制限の変動に関する情報へのリンクが提供され、ユーザーが詳細を把握しやすくなっています。

これらの変更により、Azure AI Searchのユーザーがベクトルインデックスのサイズや制限に関してより正確で分かりやすい情報を得ることができるようになります。全体的に、文書がより簡潔かつ有用な形に改善されていると言えます。

## articles/search/vector-search-overview.md{#item-56e5fa}

<details>
<summary>Diff</summary>
````diff
@@ -67,7 +67,7 @@ Azure AI Search supports [hybrid scenarios](hybrid-search-overview.md) that run
 
 Vector search is available as part of all Azure AI Search tiers in all regions at no extra charge.
 
-Newer services created after April 3, 2024 support [higher quotas for vector indexes](vector-search-index-size.md).
+Newer services created after April 3, 2024 support [higher quotas for vector indexes](vector-search-index-size.md). If you have an older service, you might be able to [upgrade your service](search-how-to-upgrade.md) for higher vector quotas.
 
 Vector search is available in:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のサービスアップグレードに関する説明の追加"
}
```

### Explanation
この変更は、`articles/search/vector-search-overview.md`ファイルに対する軽微な修正を示しており、Azure AI Searchにおけるベクトル検索のサポート内容に関する情報が更新されています。主な変更点は、古いサービスのユーザーがアップグレードの可能性について明記されている点です。

具体的な変更内容は以下の通りです：

1. **文の追加**: 
   - 「Newer services created after April 3, 2024 support [higher quotas for vector indexes](vector-search-index-size.md).」の文に続き、「If you have an older service, you might be able to [upgrade your service](search-how-to-upgrade.md) for higher vector quotas.」という文が追加されました。これにより、古いサービスを使用しているユーザーに対して、アップグレードの選択肢が提示され、ベクトルインデックスのより高いクォータを利用できる可能性が示されています。

2. **文法やスタイルの修正**:
   - 変更箇所は文法的な修正やスタイルチェンジというよりも、情報の付加として機能しています。内容自体は明確で理解しやすくなっています。

このように、この軽微な修正により、Azure AI Searchを使用するユーザーに対して、古いサービスから新しいサービスへのアップグレードの選択肢が提供され、ベクトルインデックスに関する情報がより包括的なものとなっています。結果として、ユーザーの利用可能なリソースを最大限に活用する手助けとなる内容が追加されました。

## articles/search/vector-store.md{#item-db9b8c}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 03/11/2025
+ms.date: 03/21/2025
 ---
 
 # Vector storage in Azure AI Search
@@ -160,11 +160,11 @@ The following screenshot shows an S1 service configured with one partition and o
 
 :::image type="content" source="media/vector-search-overview/usage-tiles-storage-vector-index.png" alt-text="Screenshot of usage tiles showing storage, vector index, and index count.":::
 
-Vector index limits and estimations are covered in [another article](vector-search-index-size.md), but two points to emphasize up front is that maximum storage varies by service tier, and also by when the search service was created. Newer same-tier services have significantly more capacity for vector indexes. For these reasons, take the following actions:
+Vector index limits and estimations are covered in [another article](vector-search-index-size.md), but two points to emphasize are that maximum storage varies by service tier and by when the search service was created. Newer same-tier services have significantly more capacity for vector indexes. For these reasons, take the following actions:
 
-+ [Check the deployment date of your search service](vector-search-index-size.md#how-to-check-service-creation-date). If it was created before April 3, 2024, consider creating a new search service for greater capacity.
++ [Check the deployment date of your search service](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date). If it was created before April 3, 2024, you might be able to [upgrade your service](search-how-to-upgrade.md) for greater capacity.
 
-+ [Choose a scalable tier](search-sku-tier.md) if you anticipate fluctuations in vector storage requirements. The Basic tier is fixed at one partition on older search services. Consider Standard 1 (S1) and above for more flexibility and faster performance, or create a new search service that uses higher limits and more partitions at every nillable tier.
++ [Choose a scalable tier](search-sku-tier.md) if you anticipate fluctuations in vector storage requirements. The Basic tier is fixed at one partition on older search services. Consider Standard 1 (S1) and above for more flexibility and faster performance. In the 2025-02-01-preview, you can also [switch from a lower tier to a higher tier](search-capacity-planning.md#change-your-pricing-tier).
 
 ## Basic operations and interaction
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルストレージに関する情報の更新"
}
```

### Explanation
この変更は、`articles/search/vector-store.md`ファイルに対する軽微な修正を示しており、Azure AI Searchにおけるベクトルストレージに関する情報が更新されています。主な変更点は、文の明確化と古いサービスのユーザー向けのアップグレードオプションについての情報が追加されたことです。

具体的な変更内容は以下の通りです：

1. **最終更新日の更新**: 最終更新日が「03/11/2025」から「03/21/2025」に変更され、文書が最新の情報を反映していることを示しています。

2. **文の明確化**:
   - 「two points to emphasize up front is that」という表現が「two points to emphasize are that」に修正され、文法的な正確性が向上しました。

3. **アップグレードオプションの追加**:
   - サービスの作成日が2024年4月3日以前の場合、単に新しい検索サービスの作成を検討するのではなく、サービスのアップグレードを提案する文（「you might be able to [upgrade your service](search-how-to-upgrade.md) for greater capacity.」）が追加されました。これにより、古いサービスを使用しているユーザーに対するオプションが明確に提示されています。

4. **スケーラブルなティアに関する情報の更新**:
   - 新しい情報として、2025-02-01-previewにおいて、低いティアから高いティアに変更できる可能性についての言及が追加されました。これにより、ユーザーはより柔軟にサービスのティアを選択できるようになります。

これらの変更により、Azure AI Searchのユーザーはベクトルストレージに関する最新の情報をより明確に理解し、自らのサービスを最適化するための選択肢を持つことができるようになります。全体として、文書の情報がより信頼性と有用性のあるものに改善されています。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -7,156 +7,98 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: overview
-ms.date: 02/28/2025
+ms.date: 03/31/2025
 ms.custom:
   - references_regions
   - ignite-2024
 ---
 
 # What's new in Azure AI Search
 
-**Azure Cognitive Search is now Azure AI Search**. Learn about the latest updates to Azure AI Search functionality, docs, and samples.
+Learn about the latest updates to Azure AI Search functionality, docs, and samples.
 
 > [!NOTE]
 > Preview features are announced here, but we also maintain a [preview features list](search-api-preview.md) so you can find them in one place.
 
-## February 2025
-
-| Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
-|-----------------------------|------|--------------|
-| [**Customer-managed keys support for Managed HSM**](search-security-manage-encryption-keys.md) | Security | Use either Azure Key Vault or Azure Key Vault Managed HSM (Hardware Security Module) to store customer-managed keys for extra encryption of sensitive content. |
-
-## December 2024
-
-| Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
-|-----------------------------|------|--------------|
-| [**RAG chat with Azure AI Search + Python**](https://azure.github.io/ai-app-templates/repo/azure-samples/azure-search-openai-demo/) | Template | An AI application template for building a RAG solution using Azure AI Search and Python. |
-
-## November 2024
-
-| Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
-|-----------------------------|------|--------------|
-| [**Network security perimeter**](search-security-network-security-perimeter.md) | Security | Join a search service to a [network security perimeter](/azure/private-link/network-security-perimeter-concepts) to control network access to your search service. The Azure portal and the Management REST APIs in the [2024-06-01-preview](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true) can be used to view and reconcile network security perimeter configurations. |
-| [**Shared private link support for Azure AI service connections**](search-indexer-howto-access-private.md) | Security  | Connections to Azure AI for built-in skills processing can now be private using a shared private link on the connection. |
-| [**Rescoring options for compressed vectors**](/azure/search/vector-search-how-to-quantization?tabs=2024-11-01-preview%2Cquery-2024-07-01#add-compressions-to-a-search-index) | Relevance | You can set options to rescore with original vectors instead of compressed vectors. Applies to HNSW and exhaustive KNN vector algorithms, using binary and scalar compression. Available in the [Create or Update Index (2024-11-01-preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature. |
-| [**Store fewer vector instances**](vector-search-how-to-storage-options.md) | vector search | In vector compression scenarios, you can omit storage of full precision vectors if you don't need them for rescoring. Available in the [Create or Update Index (2024-11-01-preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature. |
-| [**Query rewrite in the semantic reranker**](semantic-how-to-query-rewrite.md) | Relevance | You can set options on a semantic query to rewrite the query input into a revised or expanded query that generates more relevant results from the L2 ranker. Available in the [Search Documents (2024-11-01-preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-11-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature.|
-| [**New semantic ranker models**](semantic-search-overview.md) | Relevance | Semantic ranker runs with improved models in all supported regions. There is no change to APIs or the Azure portal experience. |
-| [**Document Layout skill**](cognitive-search-skill-document-intelligence-layout.md) | Applied AI (skills) | A new skill used to analyze a document for structure and provide [structure-aware (paragraph) chunking](search-how-to-semantic-chunking.md). This skill calls Document Intelligence and uses the Document Intelligence layout model. Available in selected regions through the [Create or Update Skillset (2024-11-01-preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature.|
-| [**Keyless billing for Azure AI skills processing**](cognitive-search-attach-cognitive-services.md) | Applied AI (skills) | You can now use a managed identity and roles for a keyless connection to Azure AI services for built-in skills processing. This capability removes restrictions for having both search and AI services in the same region. Available in the [Create or Update Skillset (2024-11-01-preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature. |
-| [**Markdown parsing mode**](search-how-to-index-markdown-blobs.md) | Indexer data source |  With this parsing mode, indexers can generate one-to-one or one-to-many search documents from Markdown files in Azure Storage and OneLake. Available in the [Create or Update Indexer (2024-11-01-preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature. |
-| [**2024-11-01-preview**](/rest/api/searchservice/search-service-api-versions?view=rest-searchservice-2024-11-01-preview&preserve-view=true) | API | Preview release of REST APIs for query rewrite, Document Layout skill, keyless billing for skills processing, Markdown parsing mode, and rescoring options for compressed vectors. |
-| [**Portal support for structured data**](search-get-started-portal-import-vectors.md) | Feature | The **Import and vectorize data** wizard now supports Azure SQL, Azure Cosmos DB, and Azure Table Storage.|
-
-## October 2024
-
-| Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
-|-----------------------------|------|--------------|
-| [Lower the dimension requirements for MRL-trained text embedding models on Azure OpenAI](vector-search-how-to-truncate-dimensions.md) | Feature | Text-embedding-3-small and Text-embedding-3-large are trained using Matryoshka Representation Learning (MRL). This allows you to truncate the embedding vectors to fewer dimensions, and adjust the balance between vector index size usage and retrieval quality. A new `truncationDimension` in the [2024-09-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) enables access to MRL compression in text embedding models. This can only be configured for new vector fields. |
-| [Unpack `@search.score` to view subscores in hybrid search results](hybrid-search-ranking.md#unpack-a-search-score-into-subscores-preview) | Feature | You can investigate Reciprocal Rank Fusion (RRF) ranked results by viewing the individual query subscores of the final merged and scored result. A new `debug` property unpacks the search score. `QueryResultDocumentSubscores`, `QueryResultDocumentRerankerInput`, and `QueryResultDocumentSemanticField` provide the extra detail. These definitions are available in the [2024-09-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
-| [Target filters in a hybrid search to just the vector queries](hybrid-search-how-to-query.md#hybrid-search-with-filters-targeting-vector-subqueries-preview) | Feature | A filter on a hybrid query involves all subqueries on the request, regardless of type. You can override the global filter to scope the filter to a specific subquery. The new `filterOverride` parameter is available on hybrid queries using the [2024-09-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
-| [Text Split skill (token chunking)](cognitive-search-skill-textsplit.md) | Applied AI (skills) | This skill has new parameters that improve data chunking for embedding models. A new `unit` parameter lets you specify token chunking. You can now chunk by token length, setting the length to a value that makes sense for your embedding model. You can also specify the tokenizer and any tokens that shouldn't be split during data chunking. The new `unit` parameter and query subscore definitions are found in the [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
-| [2024-09-01-preview](/rest/api/searchservice/search-service-api-versions?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | API | Preview release of REST APIs for truncated dimensions in text-embedding-3 models, targeted vector filtering for hybrid queries, RRF subscore details for debugging, and token chunking for Text Split skill.|
-| [Portal support for customer-managed key encryption (CMK)](search-security-manage-encryption-keys.md#step-4-encrypt-content) | Feature | When you create new objects in the Azure portal, you can now specify CMK-encryption and select an Azure Key Vault to provide the key. |
-
-## August 2024
+## March 2025
 
 | Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
 |-----------------------------|------|--------------|
-| [Debug Session improvements](cognitive-search-debug-session.md) | feature | There are two important improvements. First, you can now debug integrated vectorization and data chunking workloads. Second, Debug Sessions is redesigned for a more streamlined presentation of skills and mappings. You can select an object in the flow, and view or edit its details in a side panel. The previous tabbed layout is fully replaced with more context-sensitive information on the page. |
-| [2024-07-01](/rest/api/searchservice/search-service-api-versions?view=rest-searchservice-2024-07-01&preserve-view=true) | API | Stable release of REST APIs for generally available vector data types, vector compression, and integrated vectorization during indexing and queries. |
-| [Integrated vectorization](vector-search-integrated-vectorization.md) | Feature | Announcing general availability. Skills-driven data chunking and embedding during indexing. |
-| [Vectorizers](vector-search-how-to-configure-vectorizer.md) | Feature  | Announcing general availability. Text-to-vector conversion during query execution. Both [Azure OpenAI vectorizer](vector-search-vectorizer-azure-open-ai.md) and [custom Web API vectorizer](vector-search-vectorizer-custom-web-api.md) are generally available. |
-| [AzureOpenAIEmbedding skill](cognitive-search-skill-azure-openai-embedding.md) | Feature | Announcing general availability. A skill type that calls an Azure OpenAI embedding model to generate embeddings during indexing.  |
-| [Index projections](index-projections-concept-intro.md) | Feature | Announcing general availability. A component of a skillset definition that defines the shape of a secondary index, supporting a one-to-many index pattern, where content from an enrichment pipeline can target multiple indexes. |
-| [Binary and Scalar quantization](vector-search-how-to-quantization.md)  | Feature | Announcing general availability. Compress vector index size in memory and on disk using built-in quantization. |
-| [Narrow data types](vector-search-how-to-assign-narrow-data-types.md) | Feature  | Announcing general availability. Assign a smaller data type on vector fields, assuming incoming data is of that data type. |
-| [Import and vectorize data wizard](search-get-started-portal-import-vectors.md) | Azure portal | Announcing general availability. A wizard that creates a full indexing pipeline that includes data chunking and vectorization. The wizard creates all necessary objects and configurations. This release adds wizard support for Azure Data Lake in Azure Storage.|
-| [stored property](vector-search-how-to-storage-options.md) | Feature  | Announcing general availability. Boolean that reduces storage of vector indexes by *not* storing retrievable vectors. |
-| [vectorQueries.Weight property](vector-search-how-to-query.md#vector-weighting) | Feature  | Announcing general availability. Specify the relative weight of each vector query in a search operation. |
-
-## July 2024
+| [Service upgrade (preview)](search-how-to-upgrade.md) | Service | Upgrade your search service to higher storage limits in your region. With a one-time upgrade, you no longer need to recreate your service. Available in [Upgrade Service (2025-02-01-preview)](/rest/api/searchmanagement/services/upgrade?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true) and the Azure portal. |
+| [Pricing tier change (preview)](search-capacity-planning.md#change-your-pricing-tier) | Service | Change the [pricing tier](search-sku-tier.md) of your search service. This provides flexibility to scale storage, increase request throughput, and decrease latency based on your needs. In this preview, you can only change between Basic and Standard (S1, S2, and S3) tiers. Available in [Update Service (2025-02-01-preview)](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true#searchupdateservicewithsku) and the Azure portal. |
+| [Facet hierarchies, aggregations, and facet filters (preview)](search-faceted-navigation-examples.md) | Queries | New facet query parameters support nested facets. For numeric facetable fields, you can sum the values of each field. You can also specify filters on a facet to add inclusion or exclusion criteria. Available in [Search Documents (2025-03-01-preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2025-03-01-preview&preserve-view=true) and the Azure portal.|
+| [Rescore vector queries over binary quantization using full precision vectors (preview)](vector-search-how-to-quantization.md#recommended-rescoring-techniques) | Queries | For vector indexes that contain binary quantization, you can rescore query results using a full precision vector query. The query engine uses the dot product of the binary embeddings and the vector query for rescoring, which improves the quality of search results.  Set `enableRescoring` and `discardOriginals` to use this feature, and call the latest preview API version on the request.|
+| [Semantic ranker pre-release models (preview)](semantic-how-to-configure.md#opt-in-for-prerelease-semantic-ranking-models) | Index | Opt in to use pre-release semantic ranker models if one happens to be available in your region. Available in [Create or Update Index (2025-03-01-preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview#semanticconfiguration&preserve-view=true).|
+| [Search Service REST 2025-03-01-preview](/rest/api/searchservice/search-service-api-versions?view=rest-searchservice-2025-03-01-preview&preserve-view=true) | REST | Public preview release of REST APIs for data plane operations. Adds support for multi-vector embeddings, hierarchical facets, facet aggregation, and facet filters. |
+| [Search Management 2025-02-01-preview](/rest/api/searchmanagement/management-api-versions?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true) | REST | Public review release of REST APIs for control plane operations. Adds support for in-place upgrade to higher capacity partitions, in-place upgrade to higher tiers, and Azure Confidential Compute. |
 
-| Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
-|-----------------------------|------|--------------|
-| [Chat with your data](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) | Accelerator| A solution accelerator for the RAG pattern running in Azure, using Azure AI Search for retrieval and Azure OpenAI large language models to create conversational search experiences. The code with sample data is available for use case scenarios such as financial advisor and contract review and summarization.|
-| [Conversational Knowledge Mining](https://github.com/microsoft/Customer-Service-Conversational-Insights-with-Azure-OpenAI-Services) | Accelerator| A solution accelerator built on top of Azure AI Search, Azure Speech and Azure OpenAI services that allows customers to extract actionable insights from post-contact center conversations. |
-| [Build your own copilot](https://github.com/microsoft/Build-your-own-AI-Assistant-Solution-Accelerator) | Accelerator| Create your own custom copilot solution that empowers [Client Advisor](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/blob/main/ClientAdvisor/README.md) to harness the power of generative AI across both structured and unstructured data. Help our customers to optimize daily tasks and foster better interactions with more clients.  |
-
-## June 2024
-
-| Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
-|-----------------------------|------|--------------|
-| [Image search in the Azure portal](search-get-started-portal-image-search.md) | Feature | Search explorer now supports image search. In a vector index that has vectorized image content, you can drop images into Search Explorer to query for a match.
-
-## May 2024
-
-| Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
-|-----------------------------|------|--------------|
-| [Higher capacity and more vector quota at every tier (same billing rate)](search-limits-quotas-capacity.md#service-limits) | Infrastructure | For most regions, partition sizes are now even larger for Standard 2 (S2), Standard 3 (S3), and Standard 3 High Density (S3 HD) for services created after April 3, 2024. To get the larger partitions, create a new service in a [region that provides newer infrastructure](search-region-support.md). <br><br>Storage Optimized tiers (L1 and L2) also have more capacity. L1 and L2 customers must create a new service to benefit from the higher capacity. There's no in-place upgrade at this time. <br><br>Extra capacity is now available in [more regions](search-limits-quotas-capacity.md#service-limits): Germany North​, Germany West Central​, South Africa North​, Switzerland West​, and Azure Government (Texas, Arizona, and Virginia).|
-| [OneLake integration (preview)](search-how-to-index-onelake-files.md) | Feature | New indexer for OneLake files and OneLake shortcuts. If you use Microsoft Fabric and OneLake for data access to Amazon Web Services (AWS) and Google data sources, use this indexer to import external data into a search index. This indexer is available through the Azure portal, the [2024-05-01-preview REST API](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true), and Azure SDK beta packages. |
-| [Vector relevance](vector-search-how-to-query.md) <br>[hybrid query relevance](hybrid-search-how-to-query.md) | Feature | Four enhancements improve vector and hybrid search relevance. <br><br>First, you can now set thresholds on vector search results to exclude low-scoring results. <br><br>Second, changes in the query architecture apply scoring profiles at the end of the query pipeline for every query type. Document boosting is a common scoring profile, and it now works as expected on vector and hybrid queries.<br><br>Third, you can set [`MaxTextRecallSize` and `countAndFacetMode`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) in hybrid queries to control the quantity of BM25-ranked search results that flow into the hybrid ranking model. <br><br>Fourth, for vector and hybrid search, you can weight a vector query to have boost or diminish its importance in a multiquery request. |
-| [Binary vectors support](/rest/api/searchservice/supported-data-types) | Feature | `Collection(Edm.Byte)` is a new supported data type. This data type opens up integration with the [Cohere v3 binary embedding models](https://cohere.com/blog/int8-binary-embeddings) and custom binary quantization. Narrow data types lower the cost of large vector datasets. See [Index binary data for vector search](vector-search-how-to-index-binary-data.md) for more information.| 
-| [Azure AI Vision multimodal embeddings skill (preview)](cognitive-search-skill-vision-vectorize.md) | Skill | New skill that's bound to the [multimodal embeddings API of Azure AI Vision](/azure/ai-services/computer-vision/concept-image-retrieval). You can generate embeddings for text or images during indexing. This skill is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true).|
-| [Azure AI Vision vectorizer (preview)](vector-search-vectorizer-ai-services-vision.md) | Vectorizer | New vectorizer connects to an Azure AI Vision resource using the [multimodal embeddings API](/azure/ai-services/computer-vision/concept-image-retrieval) to generate embeddings at query time. This vectorizer is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
-| [Azure AI Foundry model catalog vectorizer (preview)](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md) | Vectorizer | New vectorizer connects to an embedding model deployed from the [Azure AI Foundry model catalog](/azure/ai-foundry/how-to/model-catalog-overview). This vectorizer is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true). <br><br>[**How to implement integrated vectorization using models from Azure AI Foundry**](vector-search-integrated-vectorization-ai-studio.md).|
-| [AzureOpenAIEmbedding skill (preview) supports more models on Azure OpenAI](cognitive-search-skill-azure-openai-embedding.md) | Skill | Now supports text-embedding-3-large and text-embedding-3-small, along with text-embedding-ada-002 from the previous update. New `dimensions` and `modelName` properties make it possible to specify the various embedding models on Azure OpenAI. Previously, the dimensions limits were fixed at 1,536 dimensions, applicable to text-embedding-ada-002 only. The updated skill is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true).|
-| Azure portal updates | Portal | [Import and vectorize data wizard](search-get-started-portal-import-vectors.md) now supports OneLake indexers as a data source. For embeddings, it also supports connections to Azure AI Vision multimodal, Azure AI Foundry model catalog, and more embedding models on Azure OpenAI. <br><br>When adding a field to an index, you can choose a [binary data type](vector-search-how-to-index-binary-data.md). <br><br>[Search explorer](search-explorer.md) now defaults to 2024-05-01-preview and supports the new preview features for vector and hybrid queries.  |
-| [2024-05-01-preview](/rest/api/searchservice/search-service-api-versions#2024-05-01-preview) | API | New preview version of the Search REST APIs provides new skills and vectorizers, new binary data type, OneLake files indexer, and new query parameters for more relevant results. See [Upgrade REST APIs](search-api-migration.md) if you have existing code written against the 2023-07-01-preview and need to migrate to this version.|
-| Azure SDK beta packages | API | Review the changelogs of the following Azure SDK beta packages for new feature support: [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Search.Documents_11.6.0-beta.4/sdk/search/Azure.Search.Documents/CHANGELOG.md), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) |
-| [Python code samples](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/readme.md)  | Samples | New end-to-end samples demonstrate [integration with Cohere Embed v3](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/community-integration/cohere/azure-search-cohere-embed-v3-sample.ipynb), [integration with OneLake and cloud data platforms on Google and AWS](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/e2e-demos/azure-ai-search-e2e-build-demo.ipynb), and [integration with Azure AI Vision multimodal APIs](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/embeddings/multimodal-embeddings/multimodal-embeddings.ipynb). |
-
-## April 2024
-
-| Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
-|-----------------------------|------|--------------|
-| [Security update addressing information disclosure](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29063) | API | GET responses [no longer return connection strings or keys](search-api-migration.md#breaking-changes-for-client-code-that-reads-connection-information). Applies to GET Skillset, GET Index, and GET Indexer. This change helps protect your Azure assets integrated with AI Search from unauthorized access. |
-| [More storage on Basic and Standard tiers](search-limits-quotas-capacity.md#service-limits) | Infrastructure |  Basic now supports up to three partitions and three replicas. Basic and Standard (S1, S2, S3) tiers have significantly more storage per partition, at the same per-partition billing rate. Extra capacity is subject to [regional availability](search-limits-quotas-capacity.md#service-limits) and applies to new search services created after April 3, 2024. Currently, there's no in-place upgrade, so you must create a new search service to get the extra storage. |
-| [More quota for vectors](search-limits-quotas-capacity.md#vector-index-size-limits) | Infrastructure | Vector quotas are also higher on new services created after April 3, 2024 in selected regions. |
-| [Vector quantization, narrow vector data types, and a new `stored` property (preview)](vector-search-how-to-configure-compression-storage.md) | Feature | Collectively, these three features add vector compression and smarter storage options. First, *scalar quantization* reduces vector index size in memory and on disk. Second, [narrow data types](/rest/api/searchservice/supported-data-types) reduce per-field storage by storing smaller values. Third, you can use `stored` to opt-out of storing the extra copy of a vector that's used only for search results. If you don't need vectors in a query response, you can set `stored` to false to save on space. |
-| [2024-03-01-preview Search REST API](/rest/api/searchservice/search-service-api-versions#2024-03-01-preview) | API | New preview version of the Search REST APIs for the new data types, vector compression properties, and vector storage options. |
-| [2024-03-01-preview Management REST API](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2024-03-01-preview&preserve-view=true) | API | New preview version of the Management REST APIs for control plane operations.  |
-| [2023-07-01-preview deprecation announcement](/rest/api/searchservice/search-service-api-versions#2023-07-01-preview) | API | Deprecation announced on April 8, 2024. It becomes unsupported on July 8, 2024. This was the first REST API that offered vector search support. Newer API versions have a different vector configuration. You should [migrate to a newer version](search-api-migration.md) as soon as possible. |
-
-## February 2024
+## February 2025
 
 | Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
 |-----------------------------|------|--------------|
-| New dimension limits | Feature | For vector fields, maximum dimension limits are now `3072`, up from `2048`. |
+| [Customer-managed keys support for Managed HSM](search-security-manage-encryption-keys.md) | Security | Use either Azure Key Vault or Azure Key Vault Managed HSM (Hardware Security Module) to store customer-managed keys for extra encryption of sensitive content. |
 
-## 2023 announcements
+## 2024 announcements
 
 | Month | Type | Announcement |
 |-------|------|-------------|
-| November | Feature | [**Vector search, generally available**](vector-search-overview.md). The previous restriction on customer-managed keys (CMK) is now lifted. [Prefiltering](vector-search-how-to-query.md) and [exhaustive K-nearest neighbor algorithm](vector-search-ranking.md) are also now generally available. |
-| November | Feature | [**Semantic ranker, generally available**](semantic-search-overview.md)|
-| November | Feature | [**Integrated vectorization (preview)**](vector-search-integrated-vectorization.md) adds data chunking and text-to-vector conversions during indexing, and also adds text-to-vector conversions at query time. |
-| November | Feature | [**Import and vectorize data wizard (preview)**](search-get-started-portal-import-vectors.md) automates data chunking and vectorization. It targets the [2023-10-01-Preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2023-10-01-preview&preserve-view=true) REST API. | 
-| November | Feature | [**Index projections (preview)**](index-projections-concept-intro.md) defines the shape of a secondary index, used for a one-to-many index pattern, where content from an enrichment pipeline can target multiple indexes. | 
-| November | API | [**2023-11-01 Search REST API**](/rest/api/searchservice/search-service-api-versions#2023-11-01) is stable version of the Search REST APIs for [vector search](vector-search-overview.md) and [semantic ranking](semantic-how-to-query-request.md). See [Upgrade REST APIs](search-api-migration.md) for migration steps to generally available features.|
-| November | API | [**2023-11-01 Management REST API**](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2023-11-01&preserve-view=true) adds APIs that [enable or disable semantic ranker](/rest/api/searchmanagement/services/create-or-update#searchsemanticsearch). |
-| November | Skill | [**Azure OpenAI Embedding skill (preview)**](cognitive-search-skill-azure-openai-embedding.md) connects to a deployed embedding model on your Azure OpenAI resource to generate embeddings during skillset execution.|
-| November | Skill | [**Text Split skill (preview)**](cognitive-search-skill-textsplit.md) updated in [2023-10-01-Preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2023-10-01-preview&preserve-view=true) to support native data chunking. |
-| November | Video | [**How vector search and semantic ranking improve your GPT prompts**](https://www.youtube.com/watch?v=Xwx1DJ0OqCk) explains how hybrid retrieval gives you optimal grounding data for generating useful AI responses and enables search over both concepts and keywords. |
-| November | Sample | [**Role-based access control in Generative AI applications**](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/access-control-in-generative-ai-applications-with-azure/ba-p/3956408) explains how to use Microsoft Entra ID and Microsoft Graph API to roll out granular user permissions on chunked content in your index. |
-| October | Sample  | [**"Chat with your data" solution accelerator**](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator). End-to-end RAG pattern that uses Azure AI Search as a retriever. It provides indexing, data chunking, and orchestration. |
-| October | Feature | [**Exhaustive  K-Nearest Neighbors (KNN)**](vector-search-overview.md#eknn) scoring algorithm for similarity search in vector space. Available in the 2023-10-01-Preview REST API only. |
-| October | Feature | [**Prefilters in vector search**](vector-search-how-to-query.md) evaluate filter criteria before query execution, reducing the amount of content that needs to be searched. Available in the 2023-10-01-Preview REST API only, through a new `vectorFilterMode` property on the query that can be set to `preFilter` (default) or `postFilter`, depending on your requirements. |
-| October | API | [**2023-10-01-Preview Search REST API**](/rest/api/searchservice/search-service-api-versions#2023-10-01-Preview), breaking changes the definition for [vector fields](vector-search-how-to-create-index.md) and [vector queries](vector-search-how-to-query.md).|
-| August | Feature | [**Enhanced semantic ranking**](semantic-search-overview.md).  Upgraded models are rolling out for semantic reranking, and availability is extended to more regions. Maximum unique token counts doubled from 128 to 256.|
-| July | Sample | [**Vector demo (Azure SDK for JavaScript)**](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-javascript/readme.md). Uses Node.js and the **@azure/search-documents 12.0.0-beta.2** library to generate embeddings, create and load an index, and run several vector queries. |
-| July | Sample | [**Vector demo (Azure SDK for .NET)**](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-dotnet/DotNetVectorDemo/readme.md).  Uses the **Azure.Search.Documents 11.5.0-beta.3** library to generate embeddings, create and load an index, and run several vector queries. You can also try [this sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/samples/Sample07_VectorSearch.md) from the Azure SDK team.|
-| July | Sample | [**Vector demo (Azure SDK for Python)**](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python) Uses the latest beta release of the **azure.search.documents** to generate embeddings, create and load an index, and run several vector queries. Visit the [azure-search-vector-samples/demo-python](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python) repo for more vector search demos. |
-| June | Feature | [**Vector search public preview**](vector-search-overview.md). |
-| June | Feature | [**Semantic search availability**](semantic-search-overview.md), available on the Basic tier.|
-| June | API | [**2023-07-01-Preview Search REST API**](/rest/api/searchservice/index-preview). Support for vector search. |
-| May | Feature | [**Azure RBAC (role-based access control, generally available)**](search-security-rbac.md). |
-| May | API | [**2022-09-01 Management REST API**](/rest/api/searchmanagement), with support for configuring search to use Azure roles. The **Az.Search** module of Azure PowerShell and **Az search** module of the Azure CLI are updated to support search service authentication options. You can also use the [**Terraform provider**](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/search_service) to configure authentication options (see this [Terraform quickstart](search-get-started-terraform.md) for details). | 
-| April | Sample |  [**Multi-region deployment of Azure AI Search for business continuity and disaster recovery**](https://github.com/Azure-Samples/azure-search-multiple-regions). Deployment scripts that fully configure a multi-regional solution for Azure AI Search, with options for synchronizing content and request redirection if an endpoint fails. |
-| March |  Sample | [**ChatGPT + Enterprise data with Azure OpenAI and Azure AI Search (GitHub)**](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md). Python code and a template for combining Azure AI Search with the large language models in OpenAI. For background, see this Tech Community blog post: [Revolutionize your Enterprise Data with ChatGPT](https://techcommunity.microsoft.com/t5/ai-applied-ai-blog/revolutionize-your-enterprise-data-with-chatgpt-next-gen-apps-w/ba-p/3762087). <br><br>Key points: <br><br>Use Azure AI Search to consolidate and index searchable content.</br> <br>Query the index for initial search results.</br> <br>Assemble prompts from those results and send to the gpt-35-turbo (preview) model in Azure OpenAI.</br> <br>Return a cross-document answer and provide citations and transparency in your customer-facing app so that users can assess the response.</br> |
+| December | Template | [RAG chat with Azure AI Search + Python](https://azure.github.io/ai-app-templates/repo/azure-samples/azure-search-openai-demo/). An AI application template for building a RAG solution using Azure AI Search and Python. |
+| November | Security | [Network security perimeter](search-security-network-security-perimeter.md).  Join a search service to a [network security perimeter](/azure/private-link/network-security-perimeter-concepts) to control network access to your search service. The Azure portal and the Management REST APIs in the [2024-06-01-preview](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true) can be used to view and reconcile network security perimeter configurations. |
+| November | Security | [Shared private link support for Azure AI service connections](search-indexer-howto-access-private.md). Connections to Azure AI for built-in skills processing can now be private using a shared private link on the connection. |
+| November | Relevance | [Rescoring options for compressed vectors](/azure/search/vector-search-how-to-quantization?tabs=2024-11-01-preview%2Cquery-2024-07-01#add-compressions-to-a-search-index). You can set options to rescore with original vectors instead of compressed vectors. Applies to HNSW and exhaustive KNN vector algorithms, using binary and scalar compression. Available in the [Create or Update Index (2024-11-01-preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature. |
+| November | Vector search | [Store fewer vector instances](vector-search-how-to-storage-options.md). In vector compression scenarios, you can omit storage of full precision vectors if you don't need them for rescoring. Available in the [Create or Update Index (2024-11-01-preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature. |
+| November | Relevance | [Query rewrite in the semantic reranker](semantic-how-to-query-rewrite.md). You can set options on a semantic query to rewrite the query input into a revised or expanded query that generates more relevant results from the L2 ranker. Available in the [Search Documents (2024-11-01-preview)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-11-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature.|
+| November | Relevance | [New semantic ranker models](semantic-search-overview.md). Semantic ranker runs with improved models in all supported regions. There's no change to APIs or the Azure portal experience. |
+| November | Applied AI (skills) | [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md). A new skill used to analyze a document for structure and provide [structure-aware (paragraph) chunking](search-how-to-semantic-chunking.md). This skill calls Document Intelligence and uses the Document Intelligence layout model. Available in selected regions through the [Create or Update Skillset (2024-11-01-preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature. |
+| November | Applied AI (skills) | [Keyless billing for Azure AI skills processing](cognitive-search-attach-cognitive-services.md). You can now use a managed identity and roles for a keyless connection to Azure AI services for built-in skills processing. This capability removes restrictions for having both search and AI services in the same region. Available in the [Create or Update Skillset (2024-11-01-preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature. |
+| November | Indexer data source | [Markdown parsing mode](search-how-to-index-markdown-blobs.md). With this parsing mode, indexers can generate one-to-one or one-to-many search documents from Markdown files in Azure Storage and OneLake. Available in the [Create or Update Indexer (2024-11-01-preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2024-11-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature. |
+| November | API | [2024-11-01-preview](/rest/api/searchservice/search-service-api-versions?view=rest-searchservice-2024-11-01-preview&preserve-view=true). Preview release of REST APIs for query rewrite, Document Layout skill, keyless billing for skills processing, Markdown parsing mode, and rescoring options for compressed vectors. |
+| November | Feature | [Portal support for structured data](search-get-started-portal-import-vectors.md). The **Import and vectorize data** wizard now supports Azure SQL, Azure Cosmos DB, and Azure Table Storage. |
+| October | Feature | [Lower the dimension requirements for MRL-trained text embedding models on Azure OpenAI](vector-search-how-to-truncate-dimensions.md). Text-embedding-3-small and Text-embedding-3-large are trained using Matryoshka Representation Learning (MRL). This allows you to truncate the embedding vectors to fewer dimensions, and adjust the balance between vector index size usage and retrieval quality. A new `truncationDimension` in the [2024-09-01-preview](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true) enables access to MRL compression in text embedding models. This can only be configured for new vector fields. |
+| October | Feature | [Unpack `@search.score` to view subscores in hybrid search results](hybrid-search-ranking.md#unpack-a-search-score-into-subscores-preview). You can investigate Reciprocal Rank Fusion (RRF) ranked results by viewing the individual query subscores of the final merged and scored result. A new `debug` property unpacks the search score. `QueryResultDocumentSubscores`, `QueryResultDocumentRerankerInput`, and `QueryResultDocumentSemanticField` provide the extra detail. These definitions are available in the [2024-09-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
+| October | Feature | [Target filters in a hybrid search to just the vector queries](hybrid-search-how-to-query.md#hybrid-search-with-filters-targeting-vector-subqueries-preview). A filter on a hybrid query involves all subqueries on the request, regardless of type. You can override the global filter to scope the filter to a specific subquery. The new `filterOverride` parameter is available on hybrid queries using the [2024-09-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
+| October | Applied AI (skills) | [Text Split skill (token chunking)](cognitive-search-skill-textsplit.md). This skill has new parameters that improve data chunking for embedding models. A new `unit` parameter lets you specify token chunking. You can now chunk by token length, setting the length to a value that makes sense for your embedding model. You can also specify the tokenizer and any tokens that shouldn't be split during data chunking. The new `unit` parameter and query subscore definitions are found in the [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
+| October | API | [2024-09-01-preview](/rest/api/searchservice/search-service-api-versions?view=rest-searchservice-2024-09-01-preview&preserve-view=true). Preview release of REST APIs for truncated dimensions in text-embedding-3 models, targeted vector filtering for hybrid queries, RRF subscore details for debugging, and token chunking for Text Split skill.|
+| October | Feature | [Portal support for customer-managed key encryption (CMK)](search-security-manage-encryption-keys.md#step-4-encrypt-content). When you create new objects in the Azure portal, you can now specify CMK-encryption and select an Azure Key Vault to provide the key. |
+| August | Feature | [Debug Session improvements](cognitive-search-debug-session.md). There are two important improvements. First, you can now debug integrated vectorization and data chunking workloads. Second, Debug Sessions is redesigned for a more streamlined presentation of skills and mappings. You can select an object in the flow, and view or edit its details in a side panel. The previous tabbed layout is fully replaced with more context-sensitive information on the page. |
+| August | API | [2024-07-01](/rest/api/searchservice/search-service-api-versions?view=rest-searchservice-2024-07-01&preserve-view=true). Stable release of REST APIs for generally available vector data types, vector compression, and integrated vectorization during indexing and queries. |
+| August | Feature | [Integrated vectorization](vector-search-integrated-vectorization.md), Announcing general availability. Skills-driven data chunking and embedding during indexing. |
+| August | Feature | [Vectorizers](vector-search-how-to-configure-vectorizer.md). Announcing general availability. Text-to-vector conversion during query execution. Both [Azure OpenAI vectorizer](vector-search-vectorizer-azure-open-ai.md) and [custom Web API vectorizer](vector-search-vectorizer-custom-web-api.md) are generally available. |
+| August | Feature | [AzureOpenAIEmbedding skill](cognitive-search-skill-azure-openai-embedding.md). Announcing general availability. A skill type that calls an Azure OpenAI embedding model to generate embeddings during indexing. |
+| August | Feature | [Index projections](index-projections-concept-intro.md). Announcing general availability. A component of a skillset definition that defines the shape of a secondary index, supporting a one-to-many index pattern, where content from an enrichment pipeline can target multiple indexes. |
+| August | Feature | [Binary and Scalar quantization](vector-search-how-to-quantization.md). Announcing general availability. Compress vector index size in memory and on disk using built-in quantization. |
+| August | Feature | [Narrow data types](vector-search-how-to-assign-narrow-data-types.md). Announcing general availability. Assign a smaller data type on vector fields, assuming incoming data is of that data type. |
+| August | Feature | [Import and vectorize data wizard](search-get-started-portal-import-vectors.md). Announcing general availability. A wizard that creates a full indexing pipeline that includes data chunking and vectorization. The wizard creates all necessary objects and configurations. This release adds wizard support for Azure Data Lake in Azure Storage. |
+| August | Feature | [stored property](vector-search-how-to-storage-options.md). Announcing general availability. Boolean that reduces storage of vector indexes by *not* storing retrievable vectors. |
+| August | Feature | [vectorQueries.Weight property](vector-search-how-to-query.md#vector-weighting). Announcing general availability. Specify the relative weight of each vector query in a search operation. |
+| July | Accelerator | [Chat with your data](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator). A solution accelerator for the RAG pattern running in Azure, using Azure AI Search for retrieval and Azure OpenAI large language models to create conversational search experiences. The code with sample data is available for use case scenarios such as financial advisor and contract review and summarization. |
+| July | Accelerator | [Conversational Knowledge Mining](https://github.com/microsoft/Customer-Service-Conversational-Insights-with-Azure-OpenAI-Services). A solution accelerator built on top of Azure AI Search, Azure Speech and Azure OpenAI services that allows customers to extract actionable insights from post-contact center conversations. |
+| July | Accelerator | [Build your own copilot](https://github.com/microsoft/Build-your-own-AI-Assistant-Solution-Accelerator). Create your own custom copilot solution that empowers [Client Advisor](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/blob/main/ClientAdvisor/README.md) to harness the power of generative AI across both structured and unstructured data. Help our customers to optimize daily tasks and foster better interactions with more clients. |
+| June | Feature | [Image search in the Azure portal](search-get-started-portal-image-search.md). Search explorer now supports image search. In a vector index that contains vectorized image content, you can drop images into Search Explorer to query for a match. |
+| May | Service limits| [Higher capacity and more vector quota at every tier (same billing rate)](search-limits-quotas-capacity.md#service-limits). For most regions, partition sizes are now even larger for Standard 2 (S2), Standard 3 (S3), and Standard 3 High Density (S3 HD) for services created after April 3, 2024. To get the larger partitions, create a new service in a [region that provides newer infrastructure](search-region-support.md). <br><br>Storage Optimized tiers (L1 and L2) also have more capacity. L1 and L2 customers must create a new service to benefit from the higher capacity. There's no in-place upgrade at this time. <br><br>Extra capacity is now available in [more regions](search-limits-quotas-capacity.md#service-limits): Germany North​, Germany West Central​, South Africa North​, Switzerland West​, and Azure Government (Texas, Arizona, and Virginia). |
+| May | Feature | [OneLake integration (preview)](search-how-to-index-onelake-files.md). New indexer for OneLake files and OneLake shortcuts. If you use Microsoft Fabric and OneLake for data access to Amazon Web Services (AWS) and Google data sources, use this indexer to import external data into a search index. This indexer is available through the Azure portal, the [2024-05-01-preview REST API](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true), and Azure SDK beta packages. |
+| May | Feature | [Vector relevance](vector-search-how-to-query.md) <br>[hybrid query relevance](hybrid-search-how-to-query.md). Four enhancements improve vector and hybrid search relevance. <br><br>First, you can now set thresholds on vector search results to exclude low-scoring results. <br><br>Second, changes in the query architecture apply scoring profiles at the end of the query pipeline for every query type. Document boosting is a common scoring profile, and it now works as expected on vector and hybrid queries.<br><br>Third, you can set [`MaxTextRecallSize` and `countAndFacetMode`](hybrid-search-how-to-query.md#set-maxtextrecallsize-and-countandfacetmode) in hybrid queries to control the quantity of BM25-ranked search results that flow into the hybrid ranking model. <br><br>Fourth, for vector and hybrid search, you can weight a vector query to have boost or diminish its importance in a multiquery request. |
+| May | Feature | [Binary vectors support](/rest/api/searchservice/supported-data-types). `Collection(Edm.Byte)` is a new supported data type. This data type opens up integration with the [Cohere v3 binary embedding models](https://cohere.com/blog/int8-binary-embeddings) and custom binary quantization. Narrow data types lower the cost of large vector datasets. See [Index binary data for vector search](vector-search-how-to-index-binary-data.md) for more information. |
+| May | Skill | [Azure AI Vision multimodal embeddings skill (preview)](cognitive-search-skill-vision-vectorize.md). New skill that's bound to the [multimodal embeddings API of Azure AI Vision](/azure/ai-services/computer-vision/concept-image-retrieval). You can generate embeddings for text or images during indexing. This skill is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
+| May | Vectorizer | [Azure AI Vision vectorizer (preview)](vector-search-vectorizer-ai-services-vision.md). New vectorizer connects to an Azure AI Vision resource using the [multimodal embeddings API](/azure/ai-services/computer-vision/concept-image-retrieval) to generate embeddings at query time. This vectorizer is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
+| May | Vectorizer | [Azure AI Foundry model catalog vectorizer (preview)](vector-search-vectorizer-azure-machine-learning-ai-studio-catalog.md). New vectorizer connects to an embedding model deployed from the [Azure AI Foundry model catalog](/azure/ai-foundry/how-to/model-catalog-overview). This vectorizer is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true). <br><br>[**How to implement integrated vectorization using models from Azure AI Foundry**](vector-search-integrated-vectorization-ai-studio.md).|
+| May | Skill | [AzureOpenAIEmbedding skill (preview) supports more models on Azure OpenAI](cognitive-search-skill-azure-openai-embedding.md). Now supports text-embedding-3-large and text-embedding-3-small, along with text-embedding-ada-002 from the previous update. New `dimensions` and `modelName` properties make it possible to specify the various embedding models on Azure OpenAI. Previously, the dimensions limits were fixed at 1,536 dimensions, applicable to text-embedding-ada-002 only. The updated skill is available through the Azure portal and the [2024-05-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
+| May | Portal | [Import and vectorize data wizard](search-get-started-portal-import-vectors.md) now supports OneLake indexers as a data source. For embeddings, it also supports connections to Azure AI Vision multimodal, Azure AI Foundry model catalog, and more embedding models on Azure OpenAI. <br><br>When adding a field to an index, you can choose a [binary data type](vector-search-how-to-index-binary-data.md). <br><br>[Search explorer](search-explorer.md) now defaults to 2024-05-01-preview and supports the new preview features for vector and hybrid queries. |
+| May | API | [2024-05-01-preview](/rest/api/searchservice/search-service-api-versions#2024-05-01-preview). New preview version of the Search REST APIs provides new skills and vectorizers, new binary data type, OneLake files indexer, and new query parameters for more relevant results. See [Upgrade REST APIs](search-api-migration.md) if you have existing code written against the 2023-07-01-preview and need to migrate to this version. |
+| May | API | Azure SDK beta packages. Review the changelogs of the following Azure SDK beta packages for new feature support: [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md), [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Search.Documents_11.6.0-beta.4/sdk/search/Azure.Search.Documents/CHANGELOG.md), [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) |
+| May | Samples | [Python code samples](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/readme.md). New end-to-end samples demonstrate [integration with Cohere Embed v3](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/community-integration/cohere/azure-search-cohere-embed-v3-sample.ipynb), [integration with OneLake and cloud data platforms on Google and AWS](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/e2e-demos/azure-ai-search-e2e-build-demo.ipynb), and [integration with Azure AI Vision multimodal APIs](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/embeddings/multimodal-embeddings/multimodal-embeddings.ipynb). |
+| April | API | [Security update addressing information disclosure](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29063). GET responses [no longer return connection strings or keys](search-api-migration.md#breaking-changes-for-client-code-that-reads-connection-information). Applies to GET Skillset, GET Index, and GET Indexer. This change helps protect your Azure assets integrated with AI Search from unauthorized access. |
+| April | API | [2024-03-01-preview Search REST API](/rest/api/searchservice/search-service-api-versions#2024-03-01-preview) |
+| April | API | [2024-03-01-preview Management REST API](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2024-03-01-preview&preserve-view=true) |
+| April | API | [2023-07-01-preview deprecation announcement](/rest/api/searchservice/search-service-api-versions#2023-07-01-preview). This version is no longer supported as of July 8, 2024. Newer API versions have a different vector configuration. You should [migrate to a newer version](search-api-migration.md) as soon as possible. |
+| April | Service limits | [Basic and Standard tiers](search-limits-quotas-capacity.md#service-limits) offer more storage per partition, at the same per-partition billing rate. Extra capacity is subject to [regional availability](search-limits-quotas-capacity.md#service-limits) and applies to new search services created after April 3, 2024. Basic now supports up to three partitions and three replicas. |
+| April | Service limits | [Vector quotas are higher](search-limits-quotas-capacity.md#vector-index-size-limits) on new services created after April 3, 2024 in selected regions. |
+| April | Feature | [Vector quantization, narrow vector data types, and a new `stored` property (preview)](vector-search-how-to-configure-compression-storage.md). Collectively, these three features minimize storage and costs.|
+| February | Feature | New dimension limits on vector fields. Maximum dimension limits are now `3072`, up from `2048`.|
 
 ## Previous year's announcements
 
++ [2023 announcements](/previous-versions/azure/search/search-whats-new-2023)
 + [2022 announcements](/previous-versions/azure/search/search-whats-new-2022)
 + [2021 announcements](/previous-versions/azure/search/search-whats-new-2021)
 + [2020 announcements](/previous-versions/azure/search/search-whats-new-2020)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azure AI Searchの新機能および変更点の大幅更新"
}
```

### Explanation
この変更は、`articles/search/whats-new.md`ファイルに対する大規模な修正を示しており、Azure AI Searchに関する最新の機能や変更点が詳細に記述されています。この内容は、特にサービスのアップデートに関連する情報を包括的に提供するものであり、ユーザーが新機能や仕様変更に迅速に適応できるようにすることを目的としています。

具体的な変更内容は以下の通りです：

1. **最終更新日の変更**:
   - 文書の最終更新日が「02/28/2025」から「03/31/2025」に変更され、ドキュメントが最新情報を反映していることを示しています。

2. **新機能と機能の整理**:
   - 旧バージョンにあった多数の項目が削除され、新たに整理された形式で新機能が追加されました。特に、2025年3月の新機能や変更点が目立ちます。例えば、メモリ効率を向上させるための「ベクトル量子化」や「狭データ型」に関する情報があります。

3. **機能の強化**:
   - 「お客様管理のキーサポート」や「Markdown解析モード」といった重要なセキュリティ機能や改善が新たに文書化されています。また、「ハイブリッド検索におけるフィルタリング」や「トークンチャンクニング」などの新しいクエリ機能も記載されています。

4. **過去の発表の整理**:
   - 過去の発表内容を新たに整理し、2023年、2022年、2021年、2020年の発表を参照するリンクが追加されました。この変更により、新旧情報へのアクセスが容易になり、ユーザーが必要な情報を簡単に見つけやすくなっています。

5. **全体的な情報の削減と簡素化**:
   - 不要な情報が削除され、特に古い機能やもはやサポートされていない機能に関する記述が見直されることで、ユーザーが必要な情報を迅速に理解できるように工夫されました。

このように、文書の変更は全体として、Azure AI Searchに関する新機能や重要な変更点を詳細に説明し、ユーザーが最新の状態を把握しやすくなることを目指しています。また、情報の整理によって、従来の内容を強化し、新たな情報の取得をよりスムーズにしています。


