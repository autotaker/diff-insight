---
date: '2024-09-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:135d681...MicrosoftDocs:78943fc
summary: この変更は、Azure AI Searchのドキュメントを全面的に更新し、APIエンドポイントのリンクを最新のものに修正することで、精度と一貫性を向上させる小規模な修正を含んでいます。特に、複数のREST
  APIリンクが正確なエンドポイントに更新され、新しい情報やセクションも追加されました。新機能として、エラートラブルシューティングセクションが追加され、また特定のリージョンにおいてSKU制限が設けられました。この更新により、ユーザーは正確な情報に基づいてAPIを活用できるようになり、開発効率が向上します。全体として、エクスペリエンスの改善と長期的なサポートを提供することを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:135d681...MicrosoftDocs:78943fc){target="_blank"}

# Highlights
この変更は主にAPIエンドポイントのリンクを最新のものに更新し、ドキュメントの精度と一貫性を向上させる小規模な修正が含まれています。特に、複数の`REST API`リンクがより正確なエンドポイントに修正され、いくつかのドキュメントには新しい情報やセクションが追加されました。

## 新機能
- `search-get-started-rag.md`にエラートラブルシューティングセクションが新たに追加されました。

## 破壊的変更
- 特定のリージョンにおけるSKU制限が追加されました。

## その他の更新
- ドキュメントで参照されているAPIエンドポイントのリンクが最新のものに修正されました。
- 一部のドキュメントにおける情報が明確化され、信頼性が向上しました。

# Insights
この変更により、Azure AI Searchのドキュメントが全面的に更新され、多くのAPIエンドポイントリンクが最新のものに変更されました。この修正は、以下の理由から非常に重要です：

1. **APIリンクの最新化**:
    - 多くのドキュメントで古いAPIエンドポイントが新しいエンドポイントに更新されました。これによりユーザーは正確な情報に基づいてAPIを適切に活用でき、エラーを減らすことが期待されます。
    - 特定のエンドポイントが新しい形式に変更されたことで、開発者は正しいエンドポイントを確実に使用できます。

2. **トラブルシューティングの改善**:
    - `search-get-started-rag.md`にエラートラブルシューティングセクションが追加されました。これにより、ユーザーはエラーが発生した際に迅速に対処できるようになり、開発効率を向上させます。
   
3. **セマンティッククエリの強化**:
    - `semantic-answers.md`の修正により、セマンティッククエリパラメータとその構成要素についての理解がより深まりました。これにより、ユーザーはより精度の高い検索結果を得るための設定が行いやすくなります。

4. **リージョンベースのSKU制限**:
    - 特定のリージョンでのSKU制限が追加されたため、ユーザーは利用可能なティアを事前に確認し、計画を立てやすくなります。

総じて、この更新はAzure AI Searchのドキュメントの整合性とユーザーエクスペリエンスを向上させるもので、長期的にはユーザーが効率的にAPIを使用できるようサポートします。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-common-errors-warnings.md](#item-a5c854) | minor update | コグニティブ検索の一般的なエラーと警告に関する変更 | modified | 4 | 4 | 8 | 
| [cognitive-search-concept-image-scenarios.md](#item-606953) | minor update | インデクサーの作成に関するリンクの修正 | modified | 2 | 2 | 4 | 
| [cognitive-search-concept-intro.md](#item-bf9ed7) | minor update | データソース作成に関するリンクの修正 | modified | 1 | 1 | 2 | 
| [cognitive-search-custom-skill-scale.md](#item-efc3d8) | minor update | インデクサー定義に関するリンクの修正 | modified | 1 | 1 | 2 | 
| [cognitive-search-skill-image-analysis.md](#item-07daa8) | minor update | インデクサー作成に関するリンクの更新 | modified | 1 | 1 | 2 | 
| [cognitive-search-skill-ocr.md](#item-259256) | minor update | インデクサー作成に関するリンクの修正 | modified | 1 | 1 | 2 | 
| [cognitive-search-skill-textmerger.md](#item-437157) | minor update | インデクサー作成に関するリンクの修正 | modified | 1 | 1 | 2 | 
| [cognitive-search-tutorial-blob.md](#item-ff148f) | minor update | REST APIのリンク更新 | modified | 4 | 4 | 8 | 
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | 検索ドキュメントAPIのリンク修正 | modified | 1 | 1 | 2 | 
| [index-add-suggesters.md](#item-28ed57) | minor update | オートコンプリートAPIのリンク修正 | modified | 1 | 1 | 2 | 
| [index-similarity-and-scoring.md](#item-75603d) | minor update | 検索スコアの参照リンク修正 | modified | 8 | 4 | 12 | 
| [index.yml](#item-c67121) | minor update | 検索ドキュメントAPIのリンク修正 | modified | 1 | 1 | 2 | 
| [knowledge-store-create-rest.md](#item-2643dd) | minor update | APIエンドポイントのリンク修正 | modified | 3 | 3 | 6 | 
| [query-lucene-syntax.md](#item-736436) | minor update | REST APIエンドポイントのリンク修正 | modified | 3 | 3 | 6 | 
| [query-odata-filter-orderby-syntax.md](#item-6ab74f) | minor update | REST APIエンドポイントのリンク修正 | modified | 8 | 8 | 16 | 
| [query-simple-syntax.md](#item-ab3c96) | minor update | REST APIエンドポイントのリンク修正 | modified | 2 | 2 | 4 | 
| [search-add-autocomplete-suggestions.md](#item-0a43e0) | minor update | REST APIエンドポイントのリンク修正 | modified | 5 | 5 | 10 | 
| [search-api-migration.md](#item-07297b) | minor update | APIエンドポイントのリンク修正 | modified | 1 | 1 | 2 | 
| [search-faceted-navigation.md](#item-f29d1e) | minor update | ファセットクエリパラメータに関するリンク修正 | modified | 1 | 1 | 2 | 
| [search-features-list.md](#item-d34448) | minor update | 検索結果のハイライトとソートに関するリンク修正 | modified | 1 | 1 | 2 | 
| [search-filters.md](#item-3f2a7a) | minor update | 検索ドキュメントREST APIのリンク修正 | modified | 1 | 1 | 2 | 
| [search-get-started-powershell.md](#item-4435d0) | minor update | 検索ドキュメントAPIのリンク修正 | modified | 1 | 1 | 2 | 
| [search-get-started-rag.md](#item-05ff0e) | new feature | エラートラブルシューティングセクションの追加 | modified | 22 | 0 | 22 | 
| [search-how-to-index-onelake-files.md](#item-95f3db) | minor update | インデクサ作成APIのリンク修正 | modified | 2 | 2 | 4 | 
| [search-howto-connecting-azure-sql-database-to-azure-search-using-indexers.md](#item-0033f1) | minor update | データソースおよびインデクサ作成APIのリンク修正 | modified | 2 | 2 | 4 | 
| [search-howto-create-indexers.md](#item-122450) | minor update | インデクサ関連のAPIリンク修正 | modified | 4 | 4 | 8 | 
| [search-howto-index-azure-data-lake-storage.md](#item-c21e43) | minor update | インデクサおよびデータソース作成APIのリンク修正 | modified | 3 | 3 | 6 | 
| [search-howto-index-cosmosdb.md](#item-568fab) | minor update | データソースおよびインデクサ作成APIのリンク修正 | modified | 2 | 2 | 4 | 
| [search-howto-index-plaintext-blobs.md](#item-63efcb) | minor update | インデクサ作成APIのリンク修正 | modified | 1 | 1 | 2 | 
| [search-howto-indexing-azure-tables.md](#item-7655b0) | minor update | データソースおよびインデクサ作成APIのリンク修正 | modified | 2 | 2 | 4 | 
| [search-howto-managed-identities-cosmos-db.md](#item-a74464) | minor update | データソース作成APIのリンク修正 | modified | 2 | 2 | 4 | 
| [search-howto-managed-identities-sql.md](#item-2af8aa) | minor update | データソース作成APIのリンク修正 | modified | 2 | 2 | 4 | 
| [search-howto-managed-identities-storage.md](#item-8209c4) | minor update | データソース作成APIのリンク修正 | modified | 1 | 1 | 2 | 
| [search-howto-run-reset-indexers.md](#item-fb10c8) | minor update | 検索ドキュメントAPIのリンク修正 | modified | 1 | 1 | 2 | 
| [search-import-data-portal.md](#item-b804d1) | minor update | データポータルにおけるAPIリンクの修正 | modified | 2 | 2 | 4 | 
| [search-index-azure-sql-managed-instance-with-managed-identity.md](#item-a4ec86) | minor update | APIリンクの修正 | modified | 3 | 3 | 6 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | APIリンクの修正 | modified | 2 | 2 | 4 | 
| [search-indexer-overview.md](#item-292796) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-lucene-query-architecture.md](#item-b0d568) | minor update | APIリンクの修正と補足情報の追加 | modified | 4 | 4 | 8 | 
| [search-more-like-this.md](#item-56c565) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-normalizers.md](#item-4477d9) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-pagination-page-layout.md](#item-115902) | minor update | APIリンクの修正 | modified | 2 | 2 | 4 | 
| [search-query-create.md](#item-532822) | minor update | APIリンクの修正 | modified | 4 | 4 | 8 | 
| [search-query-odata-collection-operators.md](#item-9fba57) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-query-odata-comparison-operators.md](#item-c92abf) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-query-odata-filter.md](#item-69d5d6) | minor update | APIリンクの修正 | modified | 2 | 2 | 4 | 
| [search-query-odata-full-text-search-functions.md](#item-5748d4) | minor update | APIリンクの修正 | modified | 5 | 5 | 10 | 
| [search-query-odata-geo-spatial-functions.md](#item-859407) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-query-odata-logical-operators.md](#item-61c263) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-query-odata-orderby.md](#item-dff8d3) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-query-odata-search-in-function.md](#item-d768e7) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-query-odata-search-score-function.md](#item-f51766) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-query-odata-select.md](#item-8d6e1d) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-query-odata-syntax-reference.md](#item-14b8d9) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-query-overview.md](#item-dcd5d6) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-query-partial-matching.md](#item-bd97dc) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-query-troubleshoot-collection-filters.md](#item-abeca4) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-query-understand-collection-filters.md](#item-32c01a) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-semi-structured-data.md](#item-d3388d) | minor update | APIリンクの修正 | modified | 2 | 2 | 4 | 
| [search-sku-manage-costs.md](#item-6e0122) | minor update | APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-sku-tier.md](#item-7686b8) | minor update | SKU制限の情報変更 | modified | 4 | 6 | 10 | 
| [search-synapseml-cognitive-services.md](#item-dcc36f) | minor update | APIエンドポイントの修正 | modified | 1 | 1 | 2 | 
| [search-traffic-analytics.md](#item-c76f2f) | minor update | APIドキュメントの更新 | modified | 1 | 1 | 2 | 
| [search-what-is-data-import.md](#item-d73ef5) | minor update | APIエンドポイントの更新 | modified | 2 | 2 | 4 | 
| [semantic-answers.md](#item-c3fee9) | minor update | セマンティッククエリに関するドキュメントの修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/cognitive-search-common-errors-warnings.md{#item-a5c854}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,7 @@ This article provides information and solutions to common errors and warnings yo
 
 Indexing stops when the error count exceeds ['maxFailedItems'](cognitive-search-concept-troubleshooting.md#tip-2-see-what-works-even-if-there-are-some-failures). 
 
-If you want indexers to ignore these errors (and skip over "failed documents"), consider updating the `maxFailedItems` and `maxFailedItemsPerBatch` as described [here](/rest/api/searchservice/create-indexer#general-parameters-for-all-indexers).
+If you want indexers to ignore these errors (and skip over "failed documents"), consider updating the `maxFailedItems` and `maxFailedItemsPerBatch` as described [here](/rest/api/searchservice/indexers/create#indexingparameters).
 
 > [!NOTE]
 > Each failed document along with its document key (when available) will show up as an error in the indexer execution status. You can utilize the [index api](/rest/api/searchservice/addupdate-or-delete-documents) to manually upload the documents at a later point if you have set the indexer to tolerate failures.
@@ -189,7 +189,7 @@ The document was read and processed, but the indexer couldn't add it to the sear
 | Trouble connecting to the target index (that persists after retries) because the service is under other load, such as querying or indexing. | Failed to establish connection to update index. Search service is under heavy load. | [Scale up your search service](search-capacity-planning.md)
 | Search service is being patched for service update, or is in the middle of a topology reconfiguration. | Failed to establish connection to update index. Search service is currently down/Search service is undergoing a transition. | Configure service with at least three replicas for 99.9% availability per [SLA documentation](https://azure.microsoft.com/support/legal/sla/search/v1_0/)
 | Failure in the underlying compute/networking resource (rare) | Failed to establish connection to update index. An unknown failure occurred. | Configure indexers to [run on a schedule](search-howto-schedule-indexers.md) to pick up from a failed state.
-| An indexing request made to the target index wasn't acknowledged within a timeout period due to network issues. | Could not establish connection to the search index in a timely manner. | Configure indexers to [run on a schedule](search-howto-schedule-indexers.md) to pick up from a failed state. Additionally, try lowering the indexer [batch size](/rest/api/searchservice/create-indexer#parameters) if this error condition persists.
+| An indexing request made to the target index wasn't acknowledged within a timeout period due to network issues. | Could not establish connection to the search index in a timely manner. | Configure indexers to [run on a schedule](search-howto-schedule-indexers.md) to pick up from a failed state. Additionally, try lowering the indexer [batch size](/rest/api/searchservice/indexers/create#indexingparameters) if this error condition persists.
 
 <a name="could-not-index-document-because-the-indexer-data-to-index-was-invalid"></a>
 
@@ -385,12 +385,12 @@ Output field mappings that reference non-existent/null data will produce warning
 <a name="the-data-change-detection-policy-is-configured-to-use-key-column-x"></a>
 
 ## `Warning: The data change detection policy is configured to use key column 'X'`
-[Data change detection policies](/rest/api/searchservice/create-data-source#data-change-detection-policies) have specific requirements for the columns they use to detect change. One of these requirements is that this column is updated every time the source item is changed. Another requirement is that the new value for this column is greater than the previous value. Key columns don't fulfill this requirement because they don't change on every update. To work around this issue, select a different column for the change detection policy.
+[Data change detection policies](/rest/api/searchservice/data-sources/create#request-body) have specific requirements for the columns they use to detect change. One of these requirements is that this column is updated every time the source item is changed. Another requirement is that the new value for this column is greater than the previous value. Key columns don't fulfill this requirement because they don't change on every update. To work around this issue, select a different column for the change detection policy.
 
 <a name="document-text-appears-to-be-utf-16-encoded-but-is-missing-a-byte-order-mark"></a>
 
 ## `Warning: Document text appears to be UTF-16 encoded, but is missing a byte order mark`
-The [indexer parsing modes](/rest/api/searchservice/create-indexer#blob-configuration-parameters) need to know how text is encoded before parsing it. The two most common ways of encoding text are UTF-16 and UTF-8. UTF-8 is a variable-length encoding where each character is between 1 byte and 4 bytes long. UTF-16 is a fixed-length encoding where each character is 2 bytes long. UTF-16 has two different variants, `big endian` and `little endian`. Text encoding is determined by a `byte order mark`, a series of bytes before the text.
+The [indexer parsing modes](/rest/api/searchservice/indexers/create#blobindexerparsingmode) need to know how text is encoded before parsing it. The two most common ways of encoding text are UTF-16 and UTF-8. UTF-8 is a variable-length encoding where each character is between 1 byte and 4 bytes long. UTF-16 is a fixed-length encoding where each character is 2 bytes long. UTF-16 has two different variants, `big endian` and `little endian`. Text encoding is determined by a `byte order mark`, a series of bytes before the text.
 
 | Encoding | Byte Order Mark |
 | --- | --- |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブ検索の一般的なエラーと警告に関する変更"
}
```

### Explanation
このコード変更は、ドキュメント `cognitive-search-common-errors-warnings.md` に対する小規模な更新を示しています。主な変更点は、外部リンクのURLが更新されたことです。具体的には、`maxFailedItems` と `maxFailedItemsPerBatch` に関するリンクが修正され、正しいエンドポイントに指し示すようになりました。この変更は、ドキュメント内の情報の正確性を確保するものであり、ユーザーが最新の情報を得られるようにしています。

さらに、エラーメッセージの一部も修正されており、これにより文書全体の一貫性と理解度が向上しています。情報が最新のAPIエンドポイントに沿っていることは、開発者やユーザーにとっての利便性を高めるために重要です。この変更は、内容のクリアランスと関連性を向上させる役割を果たしています。

## articles/search/cognitive-search-concept-image-scenarios.md{#item-606953}

<details>
<summary>Diff</summary>
````diff
@@ -62,7 +62,7 @@ After the source files are set up, enable image normalization by setting the `im
 
 Metadata adjustments are captured in a complex type created for each image. You can't opt out of the image normalization requirement. Skills that iterate over images, such as OCR and image analysis, expect normalized images.
 
-1. [Create or Update an indexer](/rest/api/searchservice/create-indexer) to set the configuration properties:
+1. [Create or Update an indexer](/rest/api/searchservice/indexers/create) to set the configuration properties:
 
     ```json
     {
@@ -636,7 +636,7 @@ def base64EncodeImage(image):
 
 ## See also
 
-+ [Create indexer (REST)](/rest/api/searchservice/create-indexer)
++ [Create indexer (REST)](/rest/api/searchservice/indexers/create)
 + [Image Analysis skill](cognitive-search-skill-image-analysis.md)
 + [OCR skill](cognitive-search-skill-ocr.md)
 + [Text merge skill](cognitive-search-skill-textmerger.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーの作成に関するリンクの修正"
}
```

### Explanation
このコードの変更は、ドキュメント `cognitive-search-concept-image-scenarios.md` における小規模な更新を示しています。主な内容は、インデクサーの作成に関連するリンクが更新されたことです。具体的には、以前は `/rest/api/searchservice/create-indexer` と表記されていた部分が、より正確なエンドポイントである `/rest/api/searchservice/indexers/create` に修正されています。

この変更により、ユーザーがAPIドキュメント内で適切な情報にアクセスできるようになり、リンクの正確性が確保されました。また、文書内の別の場所でも同様のリンク更新が行われており、関連する情報や参照が正しく維持されています。これにより、ドキュメント全体の一貫性が向上し、ユーザーが必要なリソースを見つけやすくなっています。

## articles/search/cognitive-search-concept-intro.md{#item-bf9ed7}

<details>
<summary>Diff</summary>
````diff
@@ -116,7 +116,7 @@ An enrichment pipeline consists of [*indexers*](search-indexer-overview.md) that
 
 Start with a subset of data in a [supported data source](search-indexer-overview.md#supported-data-sources). Indexer and skillset design is an iterative process. The work goes faster with a small representative data set.
 
-1. Create a [data source](/rest/api/searchservice/create-data-source) that specifies a connection to your data.
+1. Create a [data source](/rest/api/searchservice/data-sources/create) that specifies a connection to your data.
 
 1. [Create a skillset](cognitive-search-defining-skillset.md). Unless your project is small, you should [attach an Azure AI multi-service resource](cognitive-search-attach-cognitive-services.md). If you're [creating a knowledge store](knowledge-store-create-rest.md), define it within the skillset.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データソース作成に関するリンクの修正"
}
```

### Explanation
このコードの変更は、ドキュメント `cognitive-search-concept-intro.md` に対する小さな更新を示しています。主な変更点は、データソースを作成する際のリンクが更新されたことです。以前は `/rest/api/searchservice/create-data-source` というエンドポイントが使用されていましたが、これが `/rest/api/searchservice/data-sources/create` に修正されました。

この変更により、ユーザーが最新のAPIリファレンスに基づいた正確な情報にアクセスできるようになり、リンクの精度が向上しています。また、ドキュメント内の一貫性が保たれることで、ユーザーが必要な情報を容易に見つけられるようになっています。全体として、この更新はドキュメントの信頼性を向上させるものであり、読み手にとっての利便性を高める役割を果たしています。

## articles/search/cognitive-search-custom-skill-scale.md{#item-efc3d8}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,7 @@ The following properties on a [custom skill](cognitive-search-custom-skill-web-a
 
 1. Set `timeout`to a value sufficient for the skill to respond with a valid response.
 
-1. In the `indexer` definition, set [`batchSize`](/rest/api/searchservice/create-indexer#indexer-parameters) to the number of documents that should be read from the data source and enriched concurrently.
+1. In the `indexer` definition, set [`batchSize`](/rest/api/searchservice/indexers/create#indexer-parameters) to the number of documents that should be read from the data source and enriched concurrently.
 
 ### Considerations
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサー定義に関するリンクの修正"
}
```

### Explanation
このコードの変更は、ドキュメント `cognitive-search-custom-skill-scale.md` に対する小さな更新を示しています。具体的には、インデクサーの定義で使用される `batchSize` プロパティに関するリンクが修正されました。以前のリンクは `/rest/api/searchservice/create-indexer#indexer-parameters` でしたが、これが新しいエンドポイントである `/rest/api/searchservice/indexers/create#indexer-parameters` に更新されています。

この変更により、ユーザーは正確で最新な情報にアクセスできるようになり、APIの使用に関する理解が深まります。また、ドキュメントの整合性が向上し、関連情報へのアクセスがスムーズになるため、読者にとっての利便性が高まっています。全体として、この変更はユーザーエクスペリエンスを向上させるための重要なステップです。

## articles/search/cognitive-search-skill-image-analysis.md{#item-07daa8}

<details>
<summary>Diff</summary>
````diff
@@ -778,4 +778,4 @@ If you get the error similar to `"One or more skills are invalid. Details: Error
 + [Built-in skills](cognitive-search-predefined-skills.md)
 + [How to define a skillset](cognitive-search-defining-skillset.md)
 + [Extract text and information from images](cognitive-search-concept-image-scenarios.md)
-+ [Create Indexer (REST)](/rest/api/searchservice/create-indexer)
++ [Create Indexer (REST)](/rest/api/searchservice/indexers/create)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサー作成に関するリンクの更新"
}
```

### Explanation
このコードの変更は、ドキュメント `cognitive-search-skill-image-analysis.md` に対する小さな更新を示しています。具体的には、インデクサーを作成するためのREST APIに関連するリンクが更新されました。以前のリンクは `/rest/api/searchservice/create-indexer` でしたが、最新のAPIに合わせて `/rest/api/searchservice/indexers/create` に修正されています。

この変更は、ドキュメントの正確性と信頼性を高め、ユーザーが正しい情報にアクセスできるようにすることを目的としています。正確なリンクを提供することで、リーダーがインデクサー作成プロセスをよりスムーズに理解し、実行できるようになります。全体として、この更新はユーザーエクスペリエンスを向上させる重要な修正です。

## articles/search/cognitive-search-skill-ocr.md{#item-259256}

<details>
<summary>Diff</summary>
````diff
@@ -218,4 +218,4 @@ The above skillset example assumes that a normalized-images field exists. To gen
 + [TextMerger skill](cognitive-search-skill-textmerger.md)
 + [How to define a skillset](cognitive-search-defining-skillset.md)
 + [Extract text and information from images](cognitive-search-concept-image-scenarios.md)
-+ [Create Indexer (REST)](/rest/api/searchservice/create-indexer)
++ [Create Indexer (REST)](/rest/api/searchservice/indexers/create)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサー作成に関するリンクの修正"
}
```

### Explanation
このコードの変更は、ドキュメント `cognitive-search-skill-ocr.md` における小さな更新を示しています。具体的には、インデクサー作成に関するREST APIのリンクが更新されました。以前のリンクは、`/rest/api/searchservice/create-indexer` でしたが、最新のAPI仕様に合わせて `/rest/api/searchservice/indexers/create` に修正されています。

この修正は、ドキュメントの正確性を提升し、ユーザーが適切な情報にアクセスできるようにすることを目的としています。リンクが更新されたことにより、読者はインデクサーの作成方法をより確実に理解し、実行できるようになります。この更新は、ユーザーエクスペリエンスを改善し、技術的な整合性を保つために重要です。

## articles/search/cognitive-search-skill-textmerger.md{#item-437157}

<details>
<summary>Diff</summary>
````diff
@@ -157,4 +157,4 @@ The example above assumes that a normalized-images field exists. To get normaliz
 
 + [Built-in skills](cognitive-search-predefined-skills.md)
 + [How to define a skillset](cognitive-search-defining-skillset.md)
-+ [Create Indexer (REST)](/rest/api/searchservice/create-indexer)
++ [Create Indexer (REST)](/rest/api/searchservice/indexers/create)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサー作成に関するリンクの修正"
}
```

### Explanation
このコードの変更は、ドキュメント `cognitive-search-skill-textmerger.md` に対する小規模な更新を示しています。具体的には、インデクサー作成に関連するREST APIのリンクが更新されました。リンクは、以前の `/rest/api/searchservice/create-indexer` から、最新の形式である `/rest/api/searchservice/indexers/create` に変更されています。

この修正は、ドキュメントの整合性を向上させ、ユーザーが正確かつ最新の情報にアクセスできるようにすることを目的としています。リンクの更新により、読者はインデクサーの作成手順をよりスムーズに理解しやすくなります。全体として、この変更は技術的な明確さを高め、ユーザーの利便性を向上させる重要な役割を果たしています。

## articles/search/cognitive-search-tutorial-blob.md{#item-ff148f}

<details>
<summary>Diff</summary>
````diff
@@ -97,7 +97,7 @@ AI enrichment is indexer-driven. This part of the walkthrough creates four objec
 
 ### Step 1: Create a data source
 
-Call [Create Data Source](/rest/api/searchservice/create-data-source) to set the connection string to the Blob container containing the sample data files.
+Call [Create Data Source](/rest/api/searchservice/data-sources/create) to set the connection string to the Blob container containing the sample data files.
 
 ```http
 ### Create a data source
@@ -404,7 +404,7 @@ POST {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
 
 ### Step 4: Create and run an indexer
 
-Call [Create Indexer](/rest/api/searchservice/create-indexer) to drive the pipeline. The three components you have created thus far (data source, skillset, index) are inputs to an indexer. Creating the indexer on Azure AI Search is the event that puts the entire pipeline into motion.
+Call [Create Indexer](/rest/api/searchservice/indexers/create) to drive the pipeline. The three components you have created thus far (data source, skillset, index) are inputs to an indexer. Creating the indexer on Azure AI Search is the event that puts the entire pipeline into motion.
 
 Expect this step to take several minutes to complete. Even though the data set is small, analytical skills are computation-intensive.
 
@@ -514,7 +514,7 @@ GET {{baseUrl}}/indexers/cog-search-demo-idxr/status?api-version=2024-07-01  HTT
 
 ## Check results
 
-Now that you've created an index that contains AI-generated content, call [Search Documents](/rest/api/searchservice/search-documents) to run some queries to see the results.
+Now that you've created an index that contains AI-generated content, call [Search Documents](/rest/api/searchservice/documents/search-post) to run some queries to see the results.
 
 ```http
 ### Query the index\
@@ -545,7 +545,7 @@ POST {{baseUrl}}/indexes/cog-search-demo-idx/docs/search?api-version=2024-07-01
   }
 ```
 
-These queries illustrate a few of the ways you can work with query syntax and filters on new fields created by Azure AI Search. For more query examples, see [Examples in Search Documents REST API](/rest/api/searchservice/search-documents#bkmk_examples), [Simple syntax query examples](search-query-simple-examples.md), and [Full Lucene query examples](search-query-lucene-examples.md).
+These queries illustrate a few of the ways you can work with query syntax and filters on new fields created by Azure AI Search. For more query examples, see [Examples in Search Documents REST API](/rest/api/searchservice/documents/search-post#examples), [Simple syntax query examples](search-query-simple-examples.md), and [Full Lucene query examples](search-query-lucene-examples.md).
 
 <a name="reset"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIのリンク更新"
}
```

### Explanation
このコードの変更は、ドキュメント `cognitive-search-tutorial-blob.md` に関する小規模な更新を示しています。主に、いくつかのREST APIのエンドポイントリンクが最新の形式に修正されました。具体的には、データソースの作成とインデクサーの作成、ならびにドキュメントの検索に関連するリンクが見直されています。

- データソース作成のリンクは、`/rest/api/searchservice/create-data-source` から `/rest/api/searchservice/data-sources/create` に変更されました。
- インデクサー作成のリンクは、`/rest/api/searchservice/create-indexer` から `/rest/api/searchservice/indexers/create` に修正されました。
- 検索ドキュメントのリンクも、`/rest/api/searchservice/search-documents` から `/rest/api/searchservice/documents/search-post` に更新されています。

これらの変更は、ドキュメントの正確性とユーザーがアクセスする情報の最新性を確保するために重要です。更新されたリンクにより、ユーザーはよりスムーズに最新のAPI機能を活用できるようになります。全体として、この修正は技術的整合性を向上させ、より良いユーザーエクスペリエンスを提供するためのものです。

## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -71,7 +71,7 @@ POST /indexes/hotels/docs&api-version=2024-07-01
 }
 ```  
 
-This query searches on the term "inn" and passes in the current location. Notice that this query includes other parameters, such as scoringParameter. Query parameters, including "scoringParameter", are described in [Search Documents (REST API)](/rest/api/searchservice/Search-Documents).  
+This query searches on the term "inn" and passes in the current location. Notice that this query includes other parameters, such as scoringParameter. Query parameters, including "scoringParameter", are described in [Search Documents (REST API)](/rest/api/searchservice/documents/search-post).  
 
 See the [Extended example](#bkmk_ex) to review a more detailed example of a scoring profile.  
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索ドキュメントAPIのリンク修正"
}
```

### Explanation
このコードの変更は、ドキュメント `index-add-scoring-profiles.md` に対する小規模な更新を示しています。主な内容は、検索クエリの説明において使用されるREST APIのリンクが更新された点です。具体的には、`Search Documents (REST API)` というリンクが旧形式の `/rest/api/searchservice/Search-Documents` から新形式の `/rest/api/searchservice/documents/search-post` に修正されました。

この変更は、APIの正確なリファレンスを提供し、ユーザーが最新のドキュメントにアクセスできるようにするために重要です。リンクの正確性を確保することで、利用者は必要な情報を迅速に見つけ、APIを効果的に活用することが可能になります。全体として、この修正は技術文書の整合性を向上させる一助となっています。

## articles/search/index-add-suggesters.md{#item-28ed57}

<details>
<summary>Diff</summary>
````diff
@@ -152,7 +152,7 @@ private static void CreateIndex(string indexName, SearchIndexClient indexClient)
 A suggester is used in a query. After a suggester is created, call one of the following APIs for a search-as-you-type experience:
 
 + [Suggestions REST API](/rest/api/searchservice/suggestions)
-+ [Autocomplete REST API](/rest/api/searchservice/autocomplete)
++ [Autocomplete REST API](/rest/api/searchservice/documents/autocomplete-post)
 + [SuggestAsync method](/dotnet/api/azure.search.documents.searchclient.suggestasync)
 + [AutocompleteAsync method](/dotnet/api/azure.search.documents.searchclient.autocompleteasync)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オートコンプリートAPIのリンク修正"
}
```

### Explanation
このコードの変更は、ドキュメント `index-add-suggesters.md` における小規模な更新を示しています。具体的には、オートコンプリート機能に関連するAPIのリンクが最新の形式に修正されました。古いリンクは `/rest/api/searchservice/autocomplete` から、更新されたリンク `/rest/api/searchservice/documents/autocomplete-post` に変更されています。 

この更新は、ユーザーが正確で最新のAPIリファレンスにアクセスすることを確保するために重要です。オートコンプリート機能を利用する際、正しいエンドポイントに誘導することで、開発者は効率よくAPIを利用できるようになります。全体として、この修正は技術文書の整合性を高め、ユーザーエクスペリエンスを向上させる役割を果たしています。

## articles/search/index-similarity-and-scoring.md{#item-75603d}

<details>
<summary>Diff</summary>
````diff
@@ -40,7 +40,7 @@ The following video segment fast-forwards to an explanation of the generally ava
 
 Relevance scoring refers to the computation of a search score (**@search.score**) that serves as an indicator of an item's relevance in the context of the current query. The range is unbounded. However, the higher the score, the more relevant the item. 
 
-The search score is computed based on statistical properties of the string input and the query itself. Azure AI Search finds documents that match on search terms (some or all, depending on [searchMode](/rest/api/searchservice/search-documents#query-parameters)), favoring documents that contain many instances of the search term. The search score goes up even higher if the term is rare across the data index, but common within the document. The basis for this approach to computing relevance is known as *TF-IDF or* term frequency-inverse document frequency.
+The search score is computed based on statistical properties of the string input and the query itself. Azure AI Search finds documents that match on search terms (some or all, depending on [searchMode](/rest/api/searchservice/documents/search-post#searchrequest)), favoring documents that contain many instances of the search term. The search score goes up even higher if the term is rare across the data index, but common within the document. The basis for this approach to computing relevance is known as *TF-IDF or* term frequency-inverse document frequency.
 
 Search scores can be repeated throughout a result set. When multiple hits have the same search score, the ordering of the same scored items is undefined and not stable. Run the query again, and you might see items shift position, especially if you're using the free service or a billable service with multiple replicas. Given two items with an identical score, there's no guarantee that one appears first.
 
@@ -97,7 +97,7 @@ For scalability, Azure AI Search distributes each index horizontally through a s
 
 By default, the score of a document is calculated based on statistical properties of the data *within a shard*. This approach is generally not a problem for a large corpus of data, and it provides better performance than having to calculate the score based on information across all shards. That said, using this performance optimization could cause two very similar documents (or even identical documents) to end up with different relevance scores if they end up in different shards.
 
-If you prefer to compute the score based on the statistical properties across all shards, you can do so by adding `scoringStatistics=global` as a [query parameter](/rest/api/searchservice/search-documents) (or add `"scoringStatistics": "global"` as a body parameter of the [query request](/rest/api/searchservice/search-documents)).
+If you prefer to compute the score based on the statistical properties across all shards, you can do so by adding `scoringStatistics=global` as a [query parameter](/rest/api/searchservice/documents/search-post) (or add `"scoringStatistics": "global"` as a body parameter of the [query request](/rest/api/searchservice/documents/search-post)).
 
 ```http
 POST https://[service name].search.windows.net/indexes/hotels/docs/search?api-version=2024-07-01
@@ -137,7 +137,9 @@ In Azure AI Search, you can configure BM25 algorithm parameters, and tune search
 
 ## featuresMode parameter (preview)
 
-[Search Documents](/rest/api/searchservice/preview-api/search-documents) requests have a new [featuresMode](/rest/api/searchservice/preview-api/search-documents#featuresmode) parameter that can provide more detail about relevance at the field level. Whereas the `@searchScore` is calculated for the document all-up (how relevant is this document in the context of this query), through featuresMode you can get information about individual fields, as expressed in a `@search.features` structure. The structure contains all fields used in the query (either specific fields through **searchFields** in a query, or all fields attributed as **searchable** in an index). For each field, you get the following values:
+[Search Documents](/rest/api/searchservice/documents/search-post) requests support a featuresMode parameter that provides more detail about a relevance score at the field level. Whereas the `@searchScore` is calculated for the document all-up (how relevant is this document in the context of this query), featuresMode reveals information about individual fields, as expressed in a `@search.features` structure. The structure contains all fields used in the query (either specific fields through **searchFields** in a query, or all fields attributed as **searchable** in an index). 
+
+For each field, `@search.features` give you the following values:
 
 + Number of unique tokens found in the field
 + Similarity score, or a measure of how similar the content of the field is, relative to the query term
@@ -167,6 +169,8 @@ For a query that targets the "description" and "title" fields, a response that i
 
 You can consume these data points in [custom scoring solutions](https://github.com/Azure-Samples/search-ranking-tutorial) or use the information to debug search relevance problems.
 
+The featuresMode parameter isn't documented in the REST APIs, but you can use it on a preview REST API call to Search Documents.
+
 ## Number of ranked results in a full text query response
 
 By default, if you aren't using pagination, the search engine returns the top 50 highest ranking matches for full text search. You can use the `top` parameter to return a smaller or larger number of items (up to 1000 in a single response). Full text search is subject to a maximum limit of 1,000 matches (see [API response limits](search-limits-quotas-capacity.md#api-response-limits)). Once 1,000 matches are found, the search engine no longer looks for more.
@@ -177,5 +181,5 @@ To return more or less results, use the paging parameters `top`, `skip`, and `ne
 
 + [Scoring Profiles](index-add-scoring-profiles.md)
 + [REST API Reference](/rest/api/searchservice/)
-+ [Search Documents API](/rest/api/searchservice/search-documents)
++ [Search Documents API](/rest/api/searchservice/documents/search-post)
 + [Azure AI Search .NET SDK](/dotnet/api/overview/azure/search)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索スコアの参照リンク修正"
}
```

### Explanation
このコードの変更は、ドキュメント `index-similarity-and-scoring.md` における小規模な更新を示しています。主な内容は、検索スコアの計算や関連するAPIの参照リンクが最新の形式に修正された点です。具体的には、以下のポイントが変更されています：

1. **APIリンクの更新**: 記載されているリンクが古い形式から新しい形式に更新されています。特に、`Search Documents API` へのリンクが `/rest/api/searchservice/search-documents` から `/rest/api/searchservice/documents/search-post` に変更されました。

2. **情報の明確化**: featuresModeパラメータの詳細について、各フィールドに関する情報が追加されました。これにより、ユーザーはフィールドレベルの重要度スコアについてより明確な理解を得られます。

これらの変更は、文書の整合性と正確性を向上させ、ユーザーが最新の情報にアクセスできるようにするため重要です。全体として、この修正は技術文書の質を高め、ユーザー体験を向上させる役割を果たしています。

## articles/search/index.yml{#item-c67121}

<details>
<summary>Diff</summary>
````diff
@@ -139,4 +139,4 @@ landingContent:
           - text: OData language reference
             url: query-odata-filter-orderby-syntax.md
           - text: Search Documents (REST)
-            url: /rest/api/searchservice/search-documents
+            url: /rest/api/searchservice/documents/search-post
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索ドキュメントAPIのリンク修正"
}
```

### Explanation
このコードの変更は、`index.yml` ドキュメントにおける小規模な更新を示しています。具体的には、検索関連のドキュメントセクションでAPIのリンクが修正されました。

具体的な変更内容としては、次のポイントがあります：

- **URLの更新**: 旧リンク `/rest/api/searchservice/search-documents` が新しいリンク `/rest/api/searchservice/documents/search-post` に置き換えられています。これにより、ユーザーは最新のAPIエンドポイントにアクセスできるようになります。

この変更は、文書の正確性を向上させ、読者が正しい情報に基づいてAPIを利用できるようにするために重要です。全体として、この修正は技術文書の品質を高め、ユーザーエクスペリエンスを向上させる効果があります。

## articles/search/knowledge-store-create-rest.md{#item-2643dd}

<details>
<summary>Diff</summary>
````diff
@@ -113,7 +113,7 @@ A valid API key establishes trust, on a per request basis, between the applicati
 
 ## Create a data source
 
-[Create Data Source](/rest/api/searchservice/create-data-source) creates a data source connection on Azure AI Search.
+[Create Data Source](/rest/api/searchservice/data-sources/create) creates a data source connection on Azure AI Search.
 
 1. Paste in the following example to create the data source.
 
@@ -144,7 +144,7 @@ A valid API key establishes trust, on a per request basis, between the applicati
 
 ## Create a skillset 
 
-A skillset defines enrichments (skills) and your knowledge store. [Create Skillset](/rest/api/searchservice/create-indexer) creates the object on your search service.
+A skillset defines enrichments (skills) and your knowledge store. [Create Skillset](/rest/api/searchservice/indexers/create) creates the object on your search service.
 
 1. Paste in the following example to create the skillset.
 
@@ -311,7 +311,7 @@ A skillset defines enrichments (skills) and your knowledge store. [Create Skills
 
 ## Create an indexer
 
-[Create Indexer](/rest/api/searchservice/create-indexer) creates and runs the indexer. Indexer execution starts by cracking the documents, extracting text and images, and initializing the skillset. The indexer checks for the other objects that you created: the datasource, the index, and the skillset. 
+[Create Indexer](/rest/api/searchservice/indexers/create) creates and runs the indexer. Indexer execution starts by cracking the documents, extracting text and images, and initializing the skillset. The indexer checks for the other objects that you created: the datasource, the index, and the skillset. 
 
 1. Paste in the following example to create the indexer.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIエンドポイントのリンク修正"
}
```

### Explanation
このコードの変更は、`knowledge-store-create-rest.md` ドキュメントにおいて、いくつかのAPIエンドポイントリンクの修正を行ったことを示しています。具体的な変更内容は以下の通りです：

1. **データソース作成リンクの更新**: 
   - 旧リンク `/rest/api/searchservice/create-data-source` が新しいリンク `/rest/api/searchservice/data-sources/create` に修正されました。この変更により、ユーザーは最新のデータソース作成APIにアクセスできるようになります。

2. **スキルセット作成リンクの更新**:
   - 旧リンク `/rest/api/searchservice/create-indexer` が新しいリンク `/rest/api/searchservice/indexers/create` に変更されました。これにより、ユーザーがスキルセットを作成する際のAPIエンドポイントが最新のものに反映されています。

3. **インデクサ作成リンクの更新**: 
   - 旧リンク `/rest/api/searchservice/create-indexer` も新しいリンク `/rest/api/searchservice/indexers/create` に変更され、インデクサの作成に関する情報が最新のAPIで参照されるようになりました。

これらの変更は、ドキュメントの整合性を確保し、読者が正しい情報に基づいてAPIを使用できるようにするために重要です。全体としてこの修正は、ドキュメントの質を向上させ、ユーザーエクスペリエンスを強化することに寄与しています。

## articles/search/query-lucene-syntax.md{#item-736436}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ ms.date: 02/22/2024
 
 When creating queries in Azure AI Search, you can opt for the full [Lucene Query Parser](https://lucene.apache.org/core/6_6_1/queryparser/org/apache/lucene/queryparser/classic/package-summary.html) syntax for specialized query forms: wildcard, fuzzy search, proximity search, regular expressions. Much of the Lucene Query Parser syntax is [implemented intact in Azure AI Search](search-lucene-query-architecture.md), except for *range searches, which are constructed through **`$filter`** expressions. 
 
-To use full Lucene syntax, set the queryType to `full` and pass in a query expression patterned for wildcard, fuzzy search, or one of the other query forms supported by the full syntax. In REST, query expressions are provided in the **`search`** parameter of a [Search Documents (REST API)](/rest/api/searchservice/search-documents) request.
+To use full Lucene syntax, set the queryType to `full` and pass in a query expression patterned for wildcard, fuzzy search, or one of the other query forms supported by the full syntax. In REST, query expressions are provided in the **`search`** parameter of a [Search Documents (REST API)](/rest/api/searchservice/documents/search-post) request.
 
 ## Example (full syntax)
 
@@ -34,7 +34,7 @@ POST /indexes/hotels-sample-index/docs/search?api-version=2024-07-01
 
 While not specific to any query type, the **`searchMode`** parameter is relevant in this example. Whenever operators are on the query, you should generally set `searchMode=all` to ensure that *all* of the criteria are matched.  
 
-For more examples, see [Lucene query syntax examples](search-query-lucene-examples.md). For details about the query request and parameters, including searchMode, see [Search Documents (REST API)](/rest/api/searchservice/Search-Documents).
+For more examples, see [Lucene query syntax examples](search-query-lucene-examples.md). For details about the query request and parameters, including searchMode, see [Search Documents (REST API)](/rest/api/searchservice/documents/search-post).
 
 ## <a name="bkmk_syntax"></a> Syntax fundamentals  
 
@@ -204,6 +204,6 @@ For more information on query limits, see [API request limits](search-limits-quo
 
 + [Query examples for simple search](search-query-simple-examples.md)
 + [Query examples for full Lucene search](search-query-lucene-examples.md)
-+ [Search Documents](/rest/api/searchservice/Search-Documents)
++ [Search Documents](/rest/api/searchservice/documents/search-post)
 + [OData expression syntax for filters and sorting](query-odata-filter-orderby-syntax.md)   
 + [Simple query syntax in Azure AI Search](query-simple-syntax.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIエンドポイントのリンク修正"
}
```

### Explanation
このコードの変更は、`query-lucene-syntax.md` ドキュメントにおけるREST APIエンドポイントリンクの修正を示しています。具体的には、いくつかの箇所でAPIのリンクが最新のものに更新されています。

1. **Lucene構文の利用方法**:
   - 旧リンク `/rest/api/searchservice/search-documents` が新しいリンク `/rest/api/searchservice/documents/search-post` に修正されています。この変更は、Lucene構文を使用する場合のAPI呼び出しに関する情報が最新の状態に保たれることを目的としています。

2. **関連文書リンクの更新**:
   - 追加の例やクエリリクエストの詳細を示すためのリンクも同様に修正されています。例えば、クエリモードに関連した内容や具体的なAPIリクエストに関するリンクが更新されています。

このような変更は、文書の正確性を向上させ、ユーザーが正しいAPIエンドポイントを参照できるようにするために重要です。全体として、これらの修正は技術文書の質を高め、読者にとっての利便性を向上させる役割を果たしています。

## articles/search/query-odata-filter-orderby-syntax.md{#item-6ab74f}

<details>
<summary>Diff</summary>
````diff
@@ -86,14 +86,14 @@ Field paths are used in many parameters of the [Azure AI Search REST APIs](/rest
 | [Create](/rest/api/searchservice/create-index) or [Update](/rest/api/searchservice/update-index) Index | `suggesters/sourceFields` | None |
 | [Create](/rest/api/searchservice/create-index) or [Update](/rest/api/searchservice/update-index) Index | `scoringProfiles/text/weights` | Can only refer to **searchable** fields |
 | [Create](/rest/api/searchservice/create-index) or [Update](/rest/api/searchservice/update-index) Index | `scoringProfiles/functions/fieldName` | Can only refer to **filterable** fields |
-| [Search](/rest/api/searchservice/search-documents) | `search` when `queryType` is `full` | Can only refer to **searchable** fields |
-| [Search](/rest/api/searchservice/search-documents) | `facet` | Can only refer to **facetable** fields |
-| [Search](/rest/api/searchservice/search-documents) | `highlight` | Can only refer to **searchable** fields |
-| [Search](/rest/api/searchservice/search-documents) | `searchFields` | Can only refer to **searchable** fields |
-| [Suggest](/rest/api/searchservice/suggestions) and [Autocomplete](/rest/api/searchservice/autocomplete) | `searchFields` | Can only refer to fields that are part of a [suggester](index-add-suggesters.md) |
-| [Search](/rest/api/searchservice/search-documents), [Suggest](/rest/api/searchservice/suggestions), and [Autocomplete](/rest/api/searchservice/autocomplete) | `$filter` | Can only refer to **filterable** fields |
-| [Search](/rest/api/searchservice/search-documents) and [Suggest](/rest/api/searchservice/suggestions) | `$orderby` | Can only refer to **sortable** fields |
-| [Search](/rest/api/searchservice/search-documents), [Suggest](/rest/api/searchservice/suggestions), and [Lookup](/rest/api/searchservice/lookup-document) | `$select` | Can only refer to **retrievable** fields |
+| [Search](/rest/api/searchservice/documents/search-post) | `search` when `queryType` is `full` | Can only refer to **searchable** fields |
+| [Search](/rest/api/searchservice/documents/search-post) | `facet` | Can only refer to **facetable** fields |
+| [Search](/rest/api/searchservice/documents/search-post) | `highlight` | Can only refer to **searchable** fields |
+| [Search](/rest/api/searchservice/documents/search-post) | `searchFields` | Can only refer to **searchable** fields |
+| [Suggest](/rest/api/searchservice/suggestions) and [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) | `searchFields` | Can only refer to fields that are part of a [suggester](index-add-suggesters.md) |
+| [Search](/rest/api/searchservice/documents/search-post), [Suggest](/rest/api/searchservice/suggestions), and [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) | `$filter` | Can only refer to **filterable** fields |
+| [Search](/rest/api/searchservice/documents/search-post) and [Suggest](/rest/api/searchservice/suggestions) | `$orderby` | Can only refer to **sortable** fields |
+| [Search](/rest/api/searchservice/documents/search-post), [Suggest](/rest/api/searchservice/suggestions), and [Lookup](/rest/api/searchservice/lookup-document) | `$select` | Can only refer to **retrievable** fields |
 
 ## Constants
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIエンドポイントのリンク修正"
}
```

### Explanation
このコードの変更は、`query-odata-filter-orderby-syntax.md` ドキュメントにおいて、いくつかのREST APIエンドポイントのリンクを修正したことを示しています。具体的な変更内容は以下の通りです：

1. **検索関連のリンク修正**:
   - 旧リンク `/rest/api/searchservice/search-documents` が新しいリンク `/rest/api/searchservice/documents/search-post` に修正されました。この変更は、`search`、`facet`、`highlight`、`searchFields` などのクエリパラメータに関する情報が、最新のAPIエンドポイントに適切に関連付けられることを意図しています。

2. **サジェストおよびオートコンプリートのリンク修正**:
   - サジェストおよびオートコンプリート関連のリンクも同様に新しいエンドポイントに修正され、これにより、これらの機能に関連するフィールドが正確に参照されるようになっています。

3. **フィルターとソートに関するリンク更新**:
   - フィルターやソートに関連する `$filter`、`$orderby`、および `$select` に関するリンクが新しいAPIエンドポイントに修正され、機能が最新の参照に基づいて利用できるようになりました。

このような変更は、ユーザーが正しいAPIエンドポイントを参照できるようにし、技術文書の整合性を保つ上で重要です。全体として、これらの修正は、ドキュメントの質を高め、ユーザーエクスペリエンスの向上に寄与しています。

## articles/search/query-simple-syntax.md{#item-ab3c96}

<details>
<summary>Diff</summary>
````diff
@@ -38,7 +38,7 @@ POST https://{{service-name}}.search.windows.net/indexes/hotel-rooms-sample/docs
 
 The `searchMode` parameter is relevant in this example. Whenever boolean operators are on the query, you should generally set `searchMode=all` to ensure that *all* of the criteria are matched. Otherwise, you can use the default `searchMode=any` that favors recall over precision.
 
-For more examples, see [Simple query syntax examples](search-query-simple-examples.md). For details about the query request and parameters, see [Search Documents (REST API)](/rest/api/searchservice/Search-Documents).
+For more examples, see [Simple query syntax examples](search-query-simple-examples.md). For details about the query request and parameters, see [Search Documents (REST API)](/rest/api/searchservice/documents/search-post).
 
 ## Keyword search on terms and phrases
 
@@ -141,6 +141,6 @@ You can also review the following articles to learn more about query constructio
 
 + [Query examples for simple search](search-query-simple-examples.md)
 + [Query examples for full Lucene search](search-query-lucene-examples.md)
-+ [Search Documents REST API](/rest/api/searchservice/Search-Documents)
++ [Search Documents REST API](/rest/api/searchservice/documents/search-post)
 + [Lucene query syntax](query-lucene-syntax.md)
 + [Filter and Select (OData) expression syntax](query-odata-filter-orderby-syntax.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIエンドポイントのリンク修正"
}
```

### Explanation
このコードの変更は、`query-simple-syntax.md` ドキュメントにおけるREST APIエンドポイントリンクの修正を反映しています。具体的には、以下のような情報が更新されています。

1. **検索ドキュメントに関するリンク修正**:
   - 旧リンク `/rest/api/searchservice/Search-Documents` は、新しいリンク `/rest/api/searchservice/documents/search-post` に置き換えられています。この修正により、ユーザーが利用する際に最新のAPIエンドポイントに適切にアクセスできるようになります。

2. **関連文書リンクの更新**:
   - 他にも、検索の例や簡単なクエリ構文に関するリンクが同様に新しいエンドポイントに更新されています。

この変更は、ユーザーが正しい情報へアクセスできるように文書を最新の状態に保つ重要な措置であり、APIの利用に関する正確性を確保するためのものです。全体として、これらの修正はドキュメントの質を向上させ、より良いユーザーエクスペリエンスを提供するために寄与しています。

## articles/search/search-add-autocomplete-suggestions.md{#item-0a43e0}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ Search-as-you-type is a common technique for improving query productivity. In Az
 To implement these experiences in Azure AI Search:
 
 + Add a `suggester` to an index schema.
-+ Build a query that calls the [Autocomplete](/rest/api/searchservice/autocomplete) or [Suggestions](/rest/api/searchservice/suggestions) API on the request.
++ Build a query that calls the [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) or [Suggestions](/rest/api/searchservice/suggestions) API on the request.
 + Add a UI control to handle search-as-you-type interactions in your client app. We recommend using an existing JavaScript library for this purpose.
 
 In Azure AI Search, autocompleted queries and suggested results are retrieved from the search index, from selected fields that you register with a suggester. A suggester is part of the index, and it specifies which fields provide content that either completes a query, suggests a result, or does both. When the index is created and loaded, a suggester data structure is created internally to store prefixes used for matching on partial queries. For suggestions, choosing suitable fields that are unique, or at least not repetitive, is essential to the experience. For more information, see [Create a suggester](index-add-suggesters.md).
@@ -52,17 +52,17 @@ Matches are on the beginning of a term anywhere in the input string. Given "the
 Follow these links for the REST and .NET SDK reference pages:
 
 + [Suggestions REST API](/rest/api/searchservice/suggestions) 
-+ [Autocomplete REST API](/rest/api/searchservice/autocomplete) 
++ [Autocomplete REST API](/rest/api/searchservice/documents/autocomplete-post) 
 + [SuggestAsync method](/dotnet/api/azure.search.documents.searchclient.suggestasync)
 + [AutocompleteAsync method](/dotnet/api/azure.search.documents.searchclient.autocompleteasync)
 
 ## Structure a response
 
-Responses for autocomplete and suggestions are what you might expect for the pattern: [Autocomplete](/rest/api/searchservice/autocomplete#response) returns a list of terms, [Suggestions](/rest/api/searchservice/suggestions#response) returns terms plus a document ID so that you can fetch the document (use the [Lookup Document](/rest/api/searchservice/lookup-document) API to fetch the specific document for a detail page).
+Responses for autocomplete and suggestions are what you might expect for the pattern: [Autocomplete](/rest/api/searchservice/documents/autocomplete-post#responses) returns a list of terms, [Suggestions](/rest/api/searchservice/suggestions#response) returns terms plus a document ID so that you can fetch the document (use the [Lookup Document](/rest/api/searchservice/lookup-document) API to fetch the specific document for a detail page).
 
 Responses are shaped by the parameters on the request:
 
-+ For Autocomplete, set the [autocompleteMode](/rest/api/searchservice/autocomplete#query-parameters) to determine whether text completion occurs on one or two terms. 
++ For Autocomplete, set the [autocompleteMode](/rest/api/searchservice/documents/autocomplete-post#autocompletemode) to determine whether text completion occurs on one or two terms. 
 
 + For Suggestions, set [$select](/rest/api/searchservice/suggestions#query-parameters) to return fields containing unique or differentiating values, such as names and description. Avoid fields that contain duplicate values (such as a category or city).
 
@@ -242,7 +242,7 @@ public async Task<ActionResult> AutoCompleteAsync(string term)
 }
 ```
 
-The Autocomplete function takes the search term input. The method creates an [AutoCompleteParameters object](/rest/api/searchservice/autocomplete). The result is then converted to JSON so it can be shown in the client.
+The Autocomplete function takes the search term input. The method creates an [AutoCompleteParameters object](/rest/api/searchservice/documents/autocomplete-post). The result is then converted to JSON so it can be shown in the client.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIエンドポイントのリンク修正"
}
```

### Explanation
このコードの変更は、`search-add-autocomplete-suggestions.md` ドキュメントにおいて、いくつかのREST APIエンドポイントのリンクを修正したことを示しています。具体的には、以下のような更新が行われました。

1. **AutocompleteおよびSuggestions APIリンクの修正**:
   - 旧リンク `/rest/api/searchservice/autocomplete` および `/rest/api/searchservice/suggestions` は、それぞれ新しいリンク `/rest/api/searchservice/documents/autocomplete-post` に修正されています。この変更により、ユーザーが最新のAPIエンドポイントにアクセスしやすくなります。

2. **レスポンスに関するリンク更新**:
   - AutocompleteとSuggestionsのレスポンス構造に対する参照も、新しいエンドポイントに基づくものに更新されています。これにより、ユーザーはAPIのレスポンスに関する最新の情報を得ることができます。

3. **${autocompleteMode}に関するリンク修正**:
   - Autocompleteにおける `autocompleteMode` パラメータのリンクも修正されています。これにより、具体的なリファレンスが正しいAPIエンドポイントに結び付けられています。

これらの修正は、ユーザーが最新かつ正確な情報にアクセスできるようにするために行われたものであり、ドキュメント全体の整合性と信頼性を高める重要な更新です。全体として、これによってユーザー体験が向上し、Azure AI Searchに関する理解が深まることが期待されます。

## articles/search/search-api-migration.md{#item-07297b}

<details>
<summary>Diff</summary>
````diff
@@ -39,7 +39,7 @@ Azure AI Search breaks backward compatibility as a last resort. Upgrade is neces
 
 + Your code fails when unrecognized properties are returned in an API response. As a best practice, your application should ignore properties that it doesn't understand.
 
-+ Your code persists API requests and tries to resend them to the new API version. For example, this might happen if your application persists continuation tokens returned from the Search API (for more information, look for `@search.nextPageParameters` in the [Search API Reference](/rest/api/searchservice/Search-Documents)).
++ Your code persists API requests and tries to resend them to the new API version. For example, this might happen if your application persists continuation tokens returned from the Search API (for more information, look for `@search.nextPageParameters` in the [Search API Reference](/rest/api/searchservice/documents/search-post)).
 
 ## How to upgrade
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIエンドポイントのリンク修正"
}
```

### Explanation
このコード変更は、`search-api-migration.md` ドキュメントにおいて、APIのエンドポイントのリンクを修正したことを示しています。具体的には、以下の更新が行われました。

1. **APIレスポンスの取り扱いに関する注意点の追加**:
   - 新しい文が追加され、APIレスポンス内で認識されないプロパティが返された場合のコードの動作に注意を促しています。このベストプラクティスにより、アプリケーションは理解できないプロパティを無視するべきであることが明確にされています。

2. **続行トークンに関するリンクの修正**:
   - 旧リンクは `/rest/api/searchservice/Search-Documents` でしたが、新しいリンク `/rest/api/searchservice/documents/search-post` に修正されました。これにより、ユーザーが新しいAPIバージョンに関連する正しい情報にアクセスできるようになります。

この変更は、APIの利用に関する指針を明確にし、ユーザーが正しいエンドポイントに遷移できるようにするための重要な更新です。全体として、ドキュメントの正確性が向上し、開発者がAzure AI Searchを効果的に利用できることを支援します。

## articles/search/search-faceted-navigation.md{#item-f29d1e}

<details>
<summary>Diff</summary>
````diff
@@ -160,7 +160,7 @@ The response for the example includes the faceted navigation structure at the to
 
 ## Facets syntax
 
-A facet query parameter is set to a comma-delimited list of "facetable" fields and depending on the data type, can be further parameterized to set counts, sort orders, and ranges:  `count:<integer>`, `sort:<>`, `interval:<integer>`, and `values:<list>`. For more detail about facet parameters, see ["Query parameters" in the REST API](/rest/api/searchservice/search-documents#query-parameters).
+A facet query parameter is set to a comma-delimited list of "facetable" fields and depending on the data type, can be further parameterized to set counts, sort orders, and ranges:  `count:<integer>`, `sort:<>`, `interval:<integer>`, and `values:<list>`. For more detail about facet parameters, see [query parameters in the REST API](/rest/api/searchservice/documents/search-post#searchrequest).
 
 ```http
 POST https://{{service_name}}.search.windows.net/indexes/hotels/docs/search?api-version={{api_version}}
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファセットクエリパラメータに関するリンク修正"
}
```

### Explanation
このコードの変更は、`search-faceted-navigation.md` ドキュメントにおいて、ファセットクエリパラメータに関するリンクを修正したことを示しています。具体的な変更点は以下の通りです。

1. **ファセットクエリパラメータに関するリンクの修正**:
   - 旧リンクは `/rest/api/searchservice/search-documents#query-parameters` でしたが、新しいリンク `/rest/api/searchservice/documents/search-post#searchrequest` に修正されました。この変更により、ユーザーはファセットパラメータに関する最新の情報を正しいエンドポイントに基づいて参照できるようになります。

この変更は、ドキュメントの信頼性を向上させ、ユーザーが必要な情報にアクセスする際の利便性を高める重要な更新です。全体として、これによりAzure AI Searchにおけるファセットナビゲーションに関する理解が促進されることが期待されます。

## articles/search/search-features-list.md{#item-d34448}

<details>
<summary>Diff</summary>
````diff
@@ -58,7 +58,7 @@ There's feature parity in all Azure public, private, and sovereign clouds, but s
 | Relevance | [**Simple scoring**](index-add-scoring-profiles.md) is a key benefit of Azure AI Search. Scoring profiles are used to model relevance as a function of values in the documents themselves. For example, you might want newer products or discounted products to appear higher in the search results. You can also build scoring profiles using tags for personalized scoring based on customer search preferences you've tracked and stored separately. <br/><br/>[**Semantic ranker**](semantic-search-overview.md) is premium feature that reranks results based on semantic relevance to the query. Depending on your content and scenario, it can significantly improve search relevance with almost minimal configuration or effort. |
 | Geospatial search | [**Geospatial functions**](search-query-odata-geo-spatial-functions.md) filter over and match on geographic coordinates. You can [match on distance](search-query-simple-examples.md#example-6-geospatial-search) or by inclusion in a polygon shape. |
 | Filters and facets | [**Faceted navigation**](search-faceted-navigation.md) is enabled through a single query parameter. Azure AI Search returns a faceted navigation structure you can use as the code behind a categories list, for self-directed filtering (for example, to filter catalog items by price-range or brand). <br/><br/> [**Filters**](query-odata-filter-orderby-syntax.md) can be used to incorporate faceted navigation into your application's UI, enhance query formulation, and filter based on user- or developer-specified criteria. Create filters using the OData syntax. |
-| User experience | [**Autocomplete**](search-add-autocomplete-suggestions.md) can be enabled for type-ahead queries in a search bar. <br/><br/>[**Search suggestions**](/rest/api/searchservice/suggesters) also works off of partial text inputs in a search bar, but the results are actual documents in your index rather than query terms. <br/><br/>[**Synonyms**](search-synonyms.md) associates equivalent terms that implicitly expand the scope of a query, without the user having to provide the alternate terms. <br/><br/>[**Hit highlighting**](/rest/api/searchservice/Search-Documents) applies text formatting to a matching keyword in search results. You can choose which fields return highlighted snippets.<br/><br/>[**Sorting**](/rest/api/searchservice/Search-Documents) is offered for multiple fields via the index schema and then toggled at query-time with a single search parameter.<br/><br/> [**Paging**](search-pagination-page-layout.md) and throttling your search results is straightforward with the finely tuned control that Azure AI Search offers over your search results.  <br/><br/>|
+| User experience | [**Autocomplete**](search-add-autocomplete-suggestions.md) can be enabled for type-ahead queries in a search bar. <br/><br/>[**Search suggestions**](/rest/api/searchservice/suggesters) also works off of partial text inputs in a search bar, but the results are actual documents in your index rather than query terms. <br/><br/>[**Synonyms**](search-synonyms.md) associates equivalent terms that implicitly expand the scope of a query, without the user having to provide the alternate terms. <br/><br/>[**Hit highlighting**](/rest/api/searchservice/documents/search-post) applies text formatting to a matching keyword in search results. You can choose which fields return highlighted snippets.<br/><br/>[**Sorting**](/rest/api/searchservice/documents/search-post) is offered for multiple fields via the index schema and then toggled at query-time with a single search parameter.<br/><br/> [**Paging**](search-pagination-page-layout.md) and throttling your search results is straightforward with the finely tuned control that Azure AI Search offers over your search results.  <br/><br/>|
 
 ## Security features
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索結果のハイライトとソートに関するリンク修正"
}
```

### Explanation
このコード変更は、`search-features-list.md` ドキュメントにおいて、ユーザー体験に関連するリンクを修正したことを示しています。具体的には、以下の修正点が含まれています。

1. **リンクの修正**:
   - 旧リンクは `/rest/api/searchservice/Search-Documents` でしたが、新しいリンク `/rest/api/searchservice/documents/search-post` に変更されました。これにより、ユーザーがハイライトやソートの機能に関して正確かつ最新の情報を取得できるようになります。

この変更は、ドキュメントの正確性を向上させるものであり、Azure AI Searchにおけるユーザー体験をより良くするための重要な更新です。全体として、ユーザーは検索機能を最大限に活用できるように、必要な情報に簡単にアクセスできるようになります。

## articles/search/search-filters.md{#item-3f2a7a}

<details>
<summary>Diff</summary>
````diff
@@ -175,7 +175,7 @@ To work with more examples, see [OData Filter Expression Syntax > Examples](./se
 ## See also
 
 + [How full text search works in Azure AI Search](search-lucene-query-architecture.md)
-+ [Search Documents REST API](/rest/api/searchservice/search-documents)
++ [Search Documents REST API](/rest/api/searchservice/documents/search-post)
 + [Simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search)
 + [Lucene query syntax](/rest/api/searchservice/lucene-query-syntax-in-azure-search)
 + [Supported data types](/rest/api/searchservice/supported-data-types)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索ドキュメントREST APIのリンク修正"
}
```

### Explanation
このコード変更は、`search-filters.md` ドキュメントにおいて、検索ドキュメントに関連するREST APIのリンクを修正したことを示しています。この変更により、ユーザーが正しいリソースにアクセスできるようになります。具体的には、以下の修正点があります。

1. **リンクの修正**:
   - 以前のリンクは `/rest/api/searchservice/search-documents` でしたが、新しいリンクは `/rest/api/searchservice/documents/search-post` に更新されました。この変更により、検索機能に関する最新の情報を提供することによって、ユーザーエクスペリエンスを向上させています。

また、追加された参照として「[How full text search works in Azure AI Search](search-lucene-query-architecture.md)」があり、ユーザーがAzure AI Searchにおけるフルテキスト検索の仕組みを学びやすくなります。この変更は、検索機能に関連するドキュメントの整合性を保ち、ユーザーが正しい情報を簡単に見つけられるようにするための重要な更新です。

## articles/search/search-get-started-powershell.md{#item-4435d0}

<details>
<summary>Diff</summary>
````diff
@@ -308,7 +308,7 @@ To push documents, use an HTTP POST request to your index's URL endpoint. The RE
 
 ## Search an index
 
-This step shows you how to query an index by using the [Search Documents API](/rest/api/searchservice/search-documents).
+This step shows you how to query an index by using the [Search Documents API](/rest/api/searchservice/documents/search-post).
 
 Be sure to use single quotation marks on search `$urls`. Query strings include `$` characters, and you can omit having to escape them if the entire string is enclosed in single quotation marks.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索ドキュメントAPIのリンク修正"
}
```

### Explanation
このコード変更は、`search-get-started-powershell.md` ドキュメントにおいて、検索ドキュメントAPIのリンクを修正したことを示しています。具体的には、以下の変更点があります。

1. **リンクの修正**:
   - 以前のリンクは `/rest/api/searchservice/search-documents` でしたが、新しいリンクは `/rest/api/searchservice/documents/search-post` に変更されました。この修正により、ユーザーが最新の情報にアクセスできるようになります。

この変更は、ユーザーがAzure AI Searchを利用してインデックスをクエリする際に適切な情報を参照できるようにし、ドキュメントの整合性を保つための重要な更新です。全体として、これによりユーザーはより効率的に検索機能を利用できるようになります。

## articles/search/search-get-started-rag.md{#item-05ff0e}

<details>
<summary>Diff</summary>
````diff
@@ -272,6 +272,28 @@ This section uses Visual Studio Code and Python to call the chat completion APIs
 
     You might also try the query without semantic ranking by setting `use_semantic_reranker=False` in the query parameters step. Semantic ranking can noticably improve the relevance of query results and the ability of the LLM to return useful information. Experimentation can help you decide whether it makes a difference for your content.
 
+## Troubleshooting errors
+
+To debug authentication errors, insert the following code before the step that calls the search engine and the LLM.
+
+```python
+import sys
+import logging # Set the logging level for all azure-storage-* libraries
+logger = logging.getLogger('azure.identity') 
+logger.setLevel(logging.DEBUG)
+
+handler = logging.StreamHandler(stream=sys.stdout)
+formatter = logging.Formatter('[%(levelname)s %(name)s] %(message)s')
+handler.setFormatter(formatter)
+logger.addHandler(handler)
+```
+
+Rerun the query script. You should now get INFO and DEBUG statements in the output that provide more detail about the issue.
+
+If you see output messages related to ManagedIdentityCredential and token acquisition failures, it could be that you have multiple tenants, and your Azure sign-in is using a tenant that doesn't have your search service. To get your tenant ID, search the Azure portal for "tenant properties".
+
+Run `az login --tenant <YOUR-TENANT-ID>` at a command prompt, and then rerun the script.
+
 ## Clean up
 
 When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "エラートラブルシューティングセクションの追加"
}
```

### Explanation
このコード変更は、`search-get-started-rag.md` ドキュメントに、エラートラブルシューティングに関する新しいセクションを追加したことを示しています。具体的には以下の内容が追加されました。

1. **エラートラブルシューティングセクションの追加**:
   - 認証エラーをデバッグするための手法として、Pythonコードのスニペットが提供され、ユーザーが検索エンジンやLLMを呼び出す前にログを詳細に取得できるようになっています。このコードは、Azureのライブラリに関連するログレベルを設定し、エラーメッセージや詳細情報が得られるようにします。

2. **手順の詳細**:
   - 具体的に、Managed Identity Credentialやトークン取得の失敗に関する出力メッセージが表示された場合の対策として、適切なテナントにサインインする方法も説明されています。

この変更により、ユーザーはトラブルシューティングをより効果的に行えるようになり、エラーの原因を迅速に特定できる手助けを受けられるため、全体的なユーザーエクスペリエンスが向上します。

## articles/search/search-how-to-index-onelake-files.md{#item-95f3db}

<details>
<summary>Diff</summary>
````diff
@@ -360,7 +360,7 @@ In a [search index](search-what-is-an-index.md), add fields to accept the conten
 
 Once the index and data source are created, you're ready to create the indexer. Indexer configuration specifies the inputs, parameters, and properties controlling run time behaviors. You can also specify which parts of a blob to index.
 
-1. [Create or update an indexer](/rest/api/searchservice/create-indexer) by giving it a name and referencing the data source and target index:
+1. [Create or update an indexer](/rest/api/searchservice/indexers/create) by giving it a name and referencing the data source and target index:
 
     ```json
     {
@@ -404,7 +404,7 @@ Once the index and data source are created, you're ready to create the indexer.
 
    In file indexing, you can often omit field mappings because the indexer has built-in support for mapping the "content" and metadata properties to similarly named and typed fields in an index. For metadata properties, the indexer automatically replaces hyphens `-` with underscores in the search index.
 
-For more information about other properties, [Create an indexer](search-howto-create-indexers.md). For the full list of parameter descriptions, see [Blob configuration parameters](/rest/api/searchservice/create-indexer#blob-configuration-parameters) in the REST API. The parameters are the same for OneLake.
+For more information about other properties, [Create an indexer](search-howto-create-indexers.md). For the full list of parameter descriptions, see [Create Indexer (REST)](/rest/api/searchservice/indexers/create#definitions) in the REST API. The parameters are the same for OneLake.
 
 By default, an indexer runs automatically when you create it. You can change this behavior by setting "disabled" to true. To control indexer execution, [run an indexer on demand](search-howto-run-reset-indexers.md) or [put it on a schedule](search-howto-schedule-indexers.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサ作成APIのリンク修正"
}
```

### Explanation
このコード変更は、`search-how-to-index-onelake-files.md` ドキュメントにおいて、インデクサ作成に関するAPIのリンクを修正したことを示しています。具体的には以下の内容が更新されています。

1. **インデクサ作成APIのリンク変更**:
   - インデクサの作成や更新に関するリンクが `/rest/api/searchservice/create-indexer` から `/rest/api/searchservice/indexers/create` に変更されました。これにより、ユーザーは正しいエンドポイントへアクセスできるようになります。

2. **パラメータの参照更新**:
   - REST APIに関する情報の参照も更新され、`/rest/api/searchservice/create-indexer#blob-configuration-parameters` から `/rest/api/searchservice/indexers/create#definitions` に変更されています。この修正により、OneLakeに関連するパラメータに関する情報をより正確に取得できるようになります。

これらの変更により、ドキュメントが最新の情報を反映し、ユーザーにとってより使いやすくなることが期待されます。

## articles/search/search-howto-connecting-azure-sql-database-to-azure-search-using-indexers.md{#item-0033f1}

<details>
<summary>Diff</summary>
````diff
@@ -46,7 +46,7 @@ Other approaches for creating an Azure SQL indexer include Azure SDKs or [Import
 
 The data source definition specifies the data to index, credentials, and policies for identifying changes in the data. A data source is defined as an independent resource so that it can be used by multiple indexers.
 
-1. [Create data source](/rest/api/searchservice/create-data-source) or [Update data source](/rest/api/searchservice/update-data-source) to set its definition: 
+1. [Create Data Source](/rest/api/searchservice/data-sources/create) or [Create or Update Data Source](/rest/api/searchservice/data-sources/create-or-update) to set its definition: 
 
    ```http
     POST https://myservice.search.windows.net/datasources?api-version=2024-07-01
@@ -138,7 +138,7 @@ In a [search index](search-what-is-an-index.md), add fields that correspond to t
 
 Once the index and data source have been created, you're ready to create the indexer. Indexer configuration specifies the inputs, parameters, and properties controlling run time behaviors.
 
-1. [Create or update an indexer](/rest/api/searchservice/create-indexer) by giving it a name and referencing the data source and target index:
+1. [Create or update an indexer](/rest/api/searchservice/indexers/create) by giving it a name and referencing the data source and target index:
 
     ```http
     POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データソースおよびインデクサ作成APIのリンク修正"
}
```

### Explanation
このコード変更は、`search-howto-connecting-azure-sql-database-to-azure-search-using-indexers.md` ドキュメントにおいて、データソースおよびインデクサ作成に関するAPIのリンクを修正したことを示しています。具体的には以下の内容が更新されています。

1. **データソース作成APIのリンク変更**:
   - "データソースの作成"および"データソースの更新"に関するリンクが、`/rest/api/searchservice/create-data-source` および `/rest/api/searchservice/update-data-source` から、それぞれ `/rest/api/searchservice/data-sources/create` および `/rest/api/searchservice/data-sources/create-or-update` に変更されました。これにより、ユーザーは正確なエンドポイントにアクセスできるようになります。

2. **インデクサ作成APIのリンク変更**:
   - インデクサの作成に関するリンクが、`/rest/api/searchservice/create-indexer` から `/rest/api/searchservice/indexers/create` に修正されました。この変更もユーザーにとって正確な情報を提供することを意図しています。

これらの変更により、APIの利用に関する情報が最新の状態となり、ユーザーがAzure SQLデータベースとAzure Searchを接続する際の指示がより明確になります。

## articles/search/search-howto-create-indexers.md{#item-122450}

<details>
<summary>Diff</summary>
````diff
@@ -70,7 +70,7 @@ Indexers have the following requirements:
 + A `"dataSourceName"` property that points to a data source object. It specifies a connection to external data.
 + A `"targetIndexName"` property that points to the destination search index.
 
-Other parameters are optional and modify run time behaviors, such as how many errors to accept before failing the entire job. Required parameters are specified in all indexers and are documented in the [REST API reference](/rest/api/searchservice/create-indexer#request-body). 
+Other parameters are optional and modify run time behaviors, such as how many errors to accept before failing the entire job. Required parameters are specified in all indexers and are documented in the [REST API reference](/rest/api/searchservice/indexers/create#request-body). 
 
 Data source-specific indexers for blobs, SQL, and Azure Cosmos DB provide extra `"configuration"` parameters for source-specific behaviors. For example, if the source is Blob Storage, you can set a parameter that filters on file extensions: `"parameters" : { "configuration" : { "indexedFileNameExtensions" : ".pdf,.docx" } }`. If the source is Azure SQL, you can set a query time out parameter.
 
@@ -127,7 +127,7 @@ Indexers require a data source that specifies the type, container, and connectio
 
 1. Make sure you're using a [supported data source type](search-indexer-overview.md#supported-data-sources).
 
-1. [Create a data source](/rest/api/searchservice/create-data-source) definition. The following list is a few of the more frequently used data sources:
+1. [Create a data source](/rest/api/searchservice/data-sources/create) definition. The following list is a few of the more frequently used data sources:
 
    + [Azure Blob Storage](search-howto-indexing-azure-blob-storage.md)
    + [Azure Cosmos DB](search-howto-index-cosmosdb.md)
@@ -171,7 +171,7 @@ When you're ready to create an indexer on a remote search service, you need a se
 
 ### [**REST**](#tab/indexer-rest)
 
-Visual Studio Code with a REST client can send indexer requests. Using the app, you can connect to your search service and send [Create Indexer (REST)](/rest/api/searchservice/create-indexer) or [Update indexer](/rest/api/searchservice/update-indexer) requests. 
+Visual Studio Code with a REST client can send indexer requests. Using the app, you can connect to your search service and send [Create Indexer (REST)](/rest/api/searchservice/indexers/create) or [Update indexer](/rest/api/searchservice/update-indexer) requests. 
 
 ```http
 POST /indexers?api-version=[api-version]
@@ -243,7 +243,7 @@ Change detection logic is built into the data platforms. How an indexer supports
 
 Indexers keep track of the last document it processed from the data source through an internal *high water mark*. The marker is never exposed in the API, but internally the indexer keeps track of where it stopped. When indexing resumes, either through a scheduled run or an on-demand invocation, the indexer references the high water mark so that it can pick up where it left off.
 
-If you need to clear the high water mark to reindex in full, you can use [Reset Indexer](/rest/api/searchservice/reset-indexer). For more selective reindexing, use [Reset Skills](/rest/api/searchservice/preview-api/reset-skills) or [Reset Documents](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2024-05-01-preview&preserve-view=true). Through the reset APIs, you can clear internal state, and also flush the cache if you enabled [incremental enrichment](search-howto-incremental-index.md). For more background and comparison of each reset option, see [Run or reset indexers, skills, and documents](search-howto-run-reset-indexers.md).
+If you need to clear the high water mark to reindex in full, you can use [Reset Indexer](/rest/api/searchservice/reset-indexer). For more selective reindexing, use [Reset Skills](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2024-05-01-preview&preserve-view=true) or [Reset Documents](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2024-05-01-preview&preserve-view=true). Through the reset APIs, you can clear internal state, and also flush the cache if you enabled [incremental enrichment](search-howto-incremental-index.md). For more background and comparison of each reset option, see [Run or reset indexers, skills, and documents](search-howto-run-reset-indexers.md).
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサ関連のAPIリンク修正"
}
```

### Explanation
このコード変更は、`search-howto-create-indexers.md` ドキュメントにおけるインデクサ作成に関連するAPIのリンクを修正したことを示しています。具体的には以下の内容が更新されています。

1. **APIリンクの修正**:
   - データソースの作成に関するリンクが、`/rest/api/searchservice/create-data-source` から `/rest/api/searchservice/data-sources/create` に変更されました。この修正により、正確なエンドポイントが提供されます。
   - インデクサの作成に関するリンクも、`/rest/api/searchservice/create-indexer` から `/rest/api/searchservice/indexers/create` に変更されています。また、インデクサの更新に関するリンクも他の関連リンクに合わせて修正されています。

2. **説明の明確化**:
   - インデクサ要件に関する説明の一部がより具体的に記述され、「dataSourceName」および「targetIndexName」プロパティの説明が強調されています。これにより、必要な設定を理解しやすくなっています。

これらの変更により、ドキュメントは最新の情報を反映し、ユーザーがインデクサを作成する際に必要なAPIを正確に理解し、利用できるようになります。

## articles/search/search-howto-index-azure-data-lake-storage.md{#item-c21e43}

<details>
<summary>Diff</summary>
````diff
@@ -96,7 +96,7 @@ It's important to point out that you don't need to define fields for all of the
 
 The data source definition specifies the data to index, credentials, and policies for identifying changes in the data. A data source is defined as an independent resource so that it can be used by multiple indexers.
 
-1. [Create or update a data source](/rest/api/searchservice/create-data-source) to set its definition: 
+1. [Create or update a data source](/rest/api/searchservice/data-sources/create-or-update) to set its definition: 
 
     ```json
     {
@@ -178,7 +178,7 @@ In a [search index](search-what-is-an-index.md), add fields to accept the conten
 
 Once the index and data source have been created, you're ready to create the indexer. Indexer configuration specifies the inputs, parameters, and properties controlling run time behaviors. You can also specify which parts of a blob to index.
 
-1. [Create or update an indexer](/rest/api/searchservice/create-indexer) by giving it a name and referencing the data source and target index:
+1. [Create or update an indexer](/rest/api/searchservice/indexers/create) by giving it a name and referencing the data source and target index:
 
     ```http
     {
@@ -221,7 +221,7 @@ Once the index and data source have been created, you're ready to create the ind
 
    In blob indexing, you can often omit field mappings because the indexer has built-in support for mapping the "content" and metadata properties to similarly named and typed fields in an index. For metadata properties, the indexer will automatically replace hyphens `-` with underscores in the search index.
 
-1. See [Create an indexer](search-howto-create-indexers.md) for more information about other properties. For the full list of parameter descriptions, see [Blob configuration parameters](/rest/api/searchservice/create-indexer#blob-configuration-parameters) in the REST API.
+1. See [Create an indexer](search-howto-create-indexers.md) for more information about other properties. For the full list of parameter descriptions, see [Create Indexer (REST)](/rest/api/searchservice/indexers/create#definitions) in the REST API.
 
 An indexer runs automatically when it's created. You can prevent this by setting "disabled" to true. To control indexer execution, [run an indexer on demand](search-howto-run-reset-indexers.md) or [put it on a schedule](search-howto-schedule-indexers.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサおよびデータソース作成APIのリンク修正"
}
```

### Explanation
このコード変更は、`search-howto-index-azure-data-lake-storage.md` ドキュメントにおいて、インデクサおよびデータソース作成に関連するAPIのリンクを更新したことを示しています。具体的には以下の内容が修正されました。

1. **APIリンクの更新**:
   - データソースの作成および更新に関するリンクが、`/rest/api/searchservice/create-data-source` から `/rest/api/searchservice/data-sources/create-or-update` に変更されました。この修正により、ユーザーが正確なAPIエンドポイントにアクセスできるようになります。
   - インデクサの作成および更新に関するリンクも、`/rest/api/searchservice/create-indexer` から `/rest/api/searchservice/indexers/create` に変更されています。

2. **説明の明確化**:
   - インデクサの実行に関する説明の一部が更新され、ユーザーがインデクサをどのように使用するか、またはスケジュールするかに関する情報が強調されています。
   - また、REST APIに関連するリンクが明確に更新され、Blob構成パラメータに関する情報がよりわかりやすくなっています。

これらの変更によって、ドキュメントは最新のAPI仕様に対応し、ユーザーがAzure Data Lake Storageをインデックスする際に必要な指示がより明瞭になっています。

## articles/search/search-howto-index-cosmosdb.md{#item-568fab}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ Because terminology can be confusing, it's worth noting that [Azure Cosmos DB in
 
 The data source definition specifies the data to index, credentials, and policies for identifying changes in the data. A data source is an independent resource that can be used by multiple indexers.
 
-1. [Create or update a data source](/rest/api/searchservice/create-data-source) to set its definition: 
+1. [Create or update a data source](/rest/api/searchservice/data-sources/create-or-update) to set its definition: 
 
     ```http
     POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
@@ -208,7 +208,7 @@ In a [search index](search-what-is-an-index.md), add fields to accept the source
 
 Once the index and data source have been created, you're ready to create the indexer. Indexer configuration specifies the inputs, parameters, and properties controlling run time behaviors.
 
-1. [Create or update an indexer](/rest/api/searchservice/create-indexer) by giving it a name and referencing the data source and target index:
+1. [Create or update an indexer](/rest/api/searchservice/indexers/create) by giving it a name and referencing the data source and target index:
 
     ```http
     POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データソースおよびインデクサ作成APIのリンク修正"
}
```

### Explanation
このコード変更は、`search-howto-index-cosmosdb.md` ドキュメントにおいて、データソースおよびインデクサに関連するAPIのリンクを更新したことを示しています。具体的には以下の内容が修正されました。

1. **APIリンクの更新**:
   - データソース作成に関するリンクが、`/rest/api/searchservice/create-data-source` から `/rest/api/searchservice/data-sources/create-or-update` に変更され、より正確なエンドポイントにアクセスできるようになりました。
   - インデクサの作成および更新に関するリンクも、`/rest/api/searchservice/create-indexer` から `/rest/api/searchservice/indexers/create` に変更され、API仕様に適合するようになっています。

2. **HTTPリクエストの例**:
   - 各APIの使用方法が示されるHTTPリクエストの例も更新されており、エンドポイントを正確に記述しています。これにより、ユーザーは新しいAPIエンドポイントを使用する際の具体的な参照が得られます。

これらの変更により、ドキュメントは最新のAPI情報を反映し、ユーザーがAzure Cosmos DBをインデックスするための手順がより明確になります。

## articles/search/search-howto-index-plaintext-blobs.md{#item-63efcb}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ An alternative third option for breaking content into multiple parts requires ad
 
 ## Set up plain text indexing
 
-To index plain text blobs, create or update an indexer definition with the `parsingMode` configuration property set to `text` on a [Create Indexer](/rest/api/searchservice/create-indexer) request:
+To index plain text blobs, create or update an indexer definition with the `parsingMode` configuration property set to `text` on a [Create Indexer](/rest/api/searchservice/indexers/create) request:
 
 ```http
 PUT https://[service name].search.windows.net/indexers/[indexer name]?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサ作成APIのリンク修正"
}
```

### Explanation
このコード変更は、`search-howto-index-plaintext-blobs.md` ドキュメントにおいて、Plain Text Blobのインデックス作成に関する記述を更新したことを示しています。具体的には以下の内容が修正されました。

1. **APIリンクの更新**:
   - インデクサ定義の作成および更新に関するリンクが、`/rest/api/searchservice/create-indexer` から `/rest/api/searchservice/indexers/create` に変更されました。この修正により、ユーザーは正確なAPIエンドポイントにアクセスできるようになります。

2. **設定手順の明確化**:
   - Plain Text Blobをインデックスするための設定手順について、`parsingMode` 構成プロパティの設定方法に関する説明が明確に記載されています。この情報は、インデクサを正しく設定するために必要な手助けとなります。

これらの変更を通じて、ドキュメントは最新のAPI仕様を反映し、ユーザーがPlain Text Blobをインデックスする手順をより明確に理解できるようになっています。

## articles/search/search-howto-indexing-azure-tables.md{#item-7655b0}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ This article supplements [**Create an indexer**](search-howto-create-indexers.md
 
 The data source definition specifies the source data to index, credentials, and policies for change detection. A data source is an independent resource that can be used by multiple indexers.
 
-1. [Create or update a data source](/rest/api/searchservice/create-data-source) to set its definition:
+1. [Create or update a data source](/rest/api/searchservice/data-sources/create-or-update) to set its definition:
 
    ```http
     POST https://[service name].search.windows.net/datasources?api-version=2024-07-01 
@@ -160,7 +160,7 @@ In a [search index](search-what-is-an-index.md), add fields to accept the conten
 
 Once you have an index and data source, you're ready to create the indexer. Indexer configuration specifies the inputs, parameters, and properties controlling run time behaviors.
 
-1. [Create or update an indexer](/rest/api/searchservice/create-indexer) by giving it a name and referencing the data source and target index:
+1. [Create or update an indexer](/rest/api/searchservice/indexers/create) by giving it a name and referencing the data source and target index:
 
     ```http
     POST https://[service name].search.windows.net/indexers?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データソースおよびインデクサ作成APIのリンク修正"
}
```

### Explanation
このコード変更は、`search-howto-indexing-azure-tables.md` ドキュメントにおいて、Azure Tablesのインデックス作成に関連するAPIのリンクを更新したことを示しています。具体的には以下の内容が修正されました。

1. **APIリンクの更新**:
   - データソース作成に関するリンクが、`/rest/api/searchservice/create-data-source` から `/rest/api/searchservice/data-sources/create-or-update` に変更されており、正確なエンドポイントにアクセスできるようになりました。
   - インデクサの作成および更新に関するリンクも、`/rest/api/searchservice/create-indexer` から `/rest/api/searchservice/indexers/create` に変更され、最新のAPI仕様に沿った内容となっています。

2. **HTTPリクエストの例**:
   - 各APIを使用するためのHTTPリクエストの例も更新されており、新しいエンドポイントに適切にアクセスするための具体的な手順が示されています。

これらの修正により、ドキュメントは最新のAPI情報を反映しており、ユーザーがAzure Tablesをインデックスするための手順をより明確に理解できるようになります。

## articles/search/search-howto-managed-identities-cosmos-db.md{#item-a74464}

<details>
<summary>Diff</summary>
````diff
@@ -83,7 +83,7 @@ Indexers use a data source object for connections to an external data source. Th
 
 ### System-assigned managed identity
 
-The [REST API](/rest/api/searchservice/create-data-source), Azure portal, and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) support using a system-assigned managed identity. 
+The [REST API](/rest/api/searchservice/data-sources/create), Azure portal, and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) support using a system-assigned managed identity. 
 
 When you're connecting with a system-assigned managed identity, the only change to the data source definition is the format of the "credentials" property. Provide a database name and a ResourceId that has no account key or password. The ResourceId must include the subscription ID of Azure Cosmos DB, the resource group, and the Azure Cosmos DB account name.
 
@@ -92,7 +92,7 @@ When you're connecting with a system-assigned managed identity, the only change
 * For MongoDB collections, add "ApiKind=MongoDb" to the connection string and use a preview REST API.
 * For Gremlin graphs, add "ApiKind=Gremlin" to the connection string and use a preview REST API.
 
-Here's an example of how to create a data source to index data from a Cosmos DB account using the [Create Data Source](/rest/api/searchservice/create-data-source) REST API and a managed identity connection string. The managed identity connection string format is the same for the REST API, .NET SDK, and the Azure portal.
+Here's an example of how to create a data source to index data from a Cosmos DB account using the [Create Data Source](/rest/api/searchservice/data-sources/create) REST API and a managed identity connection string. The managed identity connection string format is the same for the REST API, .NET SDK, and the Azure portal.
 
 ```http
 POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データソース作成APIのリンク修正"
}
```

### Explanation
このコード変更は、`search-howto-managed-identities-cosmos-db.md` ドキュメントにおいて、Cosmos DBとの接続におけるデータソース作成APIのリンクを更新したことを示しています。具体的な変更内容は以下の通りです。

1. **APIリンクの更新**:
   - データソース作成に関するリンクが、`/rest/api/searchservice/create-data-source` から `/rest/api/searchservice/data-sources/create` に変更されました。この修正により、ユーザーは正しいAPIエンドポイントにアクセスできるようになります。

2. **内容の一貫性の確保**:
   - 変更されたリンクは、Azure Cosmos DBアカウントからデータをインデックスするためのデータソース作成に関する具体例においても更新されており、一貫性が保たれています。この情報は、ユーザーがシステム割り当ての管理されたアイデンティティを使用してデータソースを作成する際に非常に重要です。

この修正により、ドキュメントは最新のAPI情報を反映し、ユーザーが有効に利用できるようさらに明確になっています。

## articles/search/search-howto-managed-identities-sql.md{#item-2af8aa}

<details>
<summary>Diff</summary>
````diff
@@ -90,11 +90,11 @@ Create the data source and provide either a system-assigned managed identity or
 
 ### System-assigned managed identity
 
-The [REST API](/rest/api/searchservice/create-data-source), Azure portal, and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) support system-assigned managed identity. 
+The [REST API](/rest/api/searchservice/data-sources/create), Azure portal, and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) support system-assigned managed identity. 
 
 When you're connecting with a system-assigned managed identity, the only change to the data source definition is the format of the "credentials" property. You'll provide an Initial Catalog or Database name and a ResourceId that has no account key or password. The ResourceId must include the subscription ID of Azure SQL Database, the resource group of SQL Database, and the name of the SQL database.
 
-Here's an example of how to create a data source to index data from a storage account using the [Create Data Source](/rest/api/searchservice/create-data-source) REST API and a managed identity connection string. The managed identity connection string format is the same for the REST API, .NET SDK, and the Azure portal.
+Here's an example of how to create a data source to index data from a storage account using the [Create Data Source](/rest/api/searchservice/data-sources/create) REST API and a managed identity connection string. The managed identity connection string format is the same for the REST API, .NET SDK, and the Azure portal.
 
 ```http
 POST https://[service name].search.windows.net/datasources?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データソース作成APIのリンク修正"
}
```

### Explanation
このコード変更は、`search-howto-managed-identities-sql.md` ドキュメントにおいて、Azure SQL Databaseとの接続に関連するデータソース作成APIのリンクを更新したことを示しています。具体的な変更内容は以下の通りです。

1. **APIリンクの更新**:
   - データソース作成に関するリンクが、`/rest/api/searchservice/create-data-source` から `/rest/api/searchservice/data-sources/create` に変更されました。この修正によって、ユーザーは正しいAPIエンドポイントにアクセスしやすくなります。

2. **内容の一貫性の確保**:
   - 更新されたリンクは、ストレージアカウントからデータをインデックスするためのデータソース作成に関する具体例にも反映されており、整合性が保たれています。また、システム割り当ての管理されたアイデンティティを使用して接続する際の手順も明確に説明されています。

この修正により、ドキュメントは最新のAPI情報を反映し、ユーザーがAzure SQL Databaseとの連携をより簡単に理解できるようになっています。

## articles/search/search-howto-managed-identities-storage.md{#item-8209c4}

<details>
<summary>Diff</summary>
````diff
@@ -68,7 +68,7 @@ Indexers use a data source object for connections to an external data source. Th
 
 You must have a [system-assigned managed identity already configured](search-howto-managed-identities-data-sources.md), and it must have a role-assignment on Azure Storage. 
 
-For connections made using a system-assigned managed identity, the only change to the [data source definition](/rest/api/searchservice/create-data-source) is the format of the `credentials` property. 
+For connections made using a system-assigned managed identity, the only change to the [data source definition](/rest/api/searchservice/data-sources/create) is the format of the `credentials` property. 
 
 Provide a `ResourceId` that has no account key or password. The `ResourceId` must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データソース作成APIのリンク修正"
}
```

### Explanation
このコード変更は、`search-howto-managed-identities-storage.md` ドキュメントにおいて、システム割り当ての管理されたアイデンティティを使用した接続に関連するデータソース作成APIのリンクを更新したことを示しています。具体的な変更内容は以下の通りです。

1. **APIリンクの更新**:
   - データソース作成に関するリンクが、`/rest/api/searchservice/create-data-source` から `/rest/api/searchservice/data-sources/create` に変更されました。この更新により、ユーザーは正しいAPIエンドポイントにアクセスできるようになります。

2. **内容の明確化**:
   - システム割り当ての管理されたアイデンティティを使用して接続する際のデータソース定義における変更点が明確に示されています。この情報は、ユーザーがAzure Storageとの接続を正しく設定するために重要です。

この修正により、ドキュメントは最新のAPI情報を反映し、ユーザーがより効率的に情報を得ることができるようになっています。

## articles/search/search-howto-run-reset-indexers.md{#item-fb10c8}

<details>
<summary>Diff</summary>
````diff
@@ -224,7 +224,7 @@ When you're testing this API for the first time, the following APIs can help you
 
 1. Call [Run Indexer](/rest/api/searchservice/indexers/run) a second time to process from the last high-water mark.
 
-1. Call [Search Documents](/rest/api/searchservice/search-documents) to check for updated values, and also to return document keys if you're unsure of the value. Use `"select": "<field names>"` if you want to limit which fields appear in the response.
+1. Call [Search Documents](/rest/api/searchservice/documents/search-post) to check for updated values, and also to return document keys if you're unsure of the value. Use `"select": "<field names>"` if you want to limit which fields appear in the response.
 
 ### Overwriting the document key list
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索ドキュメントAPIのリンク修正"
}
```

### Explanation
このコード変更は、`search-howto-run-reset-indexers.md` ドキュメントにおいて、検索ドキュメントAPIのリンクを更新したことを示しています。具体的な変更内容は以下の通りです。

1. **APIリンクの更新**:
   - 検索ドキュメントの関連リンクが、`/rest/api/searchservice/search-documents` から `/rest/api/searchservice/documents/search-post` に変更されました。この修正により、ユーザーは正しいAPIエンドポイントにアクセスしやすくなります。

2. **内容の整合性の向上**:
   - 新しいリンクは、最新のAPIを反映しており、検索リクエストを作成する際の情報が整合性を持って提供されます。これにより、ユーザーは更新された値の確認やドキュメントキーの取得がスムーズに行えるようになります。

この修正により、ドキュメントは最新の情報を提供し、ユーザーがAzure Searchサービスを利用する際の利便性が向上しています。

## articles/search/search-import-data-portal.md{#item-b804d1}

<details>
<summary>Diff</summary>
````diff
@@ -47,8 +47,8 @@ The wizard outputs the objects in the following table. After the objects are cre
 
 | Object | Description | 
 |--------|-------------|
-| [Indexer](/rest/api/searchservice/create-indexer)  | A configuration object specifying a data source, target index, an optional skillset, optional schedule, and optional configuration settings for error handing and base-64 encoding. |
-| [Data Source](/rest/api/searchservice/create-data-source)  | Persists connection information to a [supported data source](search-indexer-overview.md#supported-data-sources) on Azure. A data source object is used exclusively with indexers. | 
+| [Indexer](/rest/api/searchservice/indexers/create)  | A configuration object specifying a data source, target index, an optional skillset, optional schedule, and optional configuration settings for error handing and base-64 encoding. |
+| [Data Source](/rest/api/searchservice/data-sources/create)  | Persists connection information to a [supported data source](search-indexer-overview.md#supported-data-sources) on Azure. A data source object is used exclusively with indexers. | 
 | [Index](/rest/api/searchservice/create-index) | Physical data structure used for full text search and other queries. | 
 | [Skillset](/rest/api/searchservice/skillsets/create) | Optional. A complete set of instructions for manipulating, transforming, and shaping content, including analyzing and extracting information from image files. Skillsets are also used for integrated vectorization. Unless the volume of work fall under the limit of 20 transactions per indexer per day, the skillset must include a reference to an Azure AI multiservice resource that provides enrichment. For integrated vectorization, you can use either Azure AI Vision or an embedding model in the Azure AI Studio model catalog. | 
 | [Knowledge store](knowledge-store-concept-intro.md) | Optional. Stores output from in tables and blobs in Azure Storage for independent analysis or downstream processing in nonsearch scenarios. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データポータルにおけるAPIリンクの修正"
}
```

### Explanation
このコード変更は、`search-import-data-portal.md` ドキュメントにおいて、いくつかのAPIリンクを更新したことを示しています。具体的な変更内容は以下の通りです。

1. **APIリンクの更新**:
   - インデクサーに関連するリンクが、`/rest/api/searchservice/create-indexer` から `/rest/api/searchservice/indexers/create` に修正されました。
   - データソースに関連するリンクが、`/rest/api/searchservice/create-data-source` から `/rest/api/searchservice/data-sources/create` に変更されました。

2. **説明の一致の向上**:
   - これにより、インデクサーとデータソースに関する説明が、最新のAPIエンドポイントに整合しており、ユーザーが正確な情報に基づいて設定を行うことができるようになります。

この修正により、ドキュメントは最新のAPI情報を反映し、ユーザーがAzureのデータポータルを効果的に利用する際の利便性が向上します。

## articles/search/search-index-azure-sql-managed-instance-with-managed-identity.md{#item-a4ec86}

<details>
<summary>Diff</summary>
````diff
@@ -94,11 +94,11 @@ Create the data source and provide a system-assigned managed identity.
 
 ### System-assigned managed identity
 
-The [REST API](/rest/api/searchservice/create-data-source), Azure portal, and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) support system-assigned managed identity. 
+The [REST API](//rest/api/searchservice/data-sources/create), Azure portal, and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) support system-assigned managed identity. 
 
 When you're connecting with a system-assigned managed identity, the only change to the data source definition is the format of the "credentials" property. You'll provide an Initial Catalog or Database name and a `ResourceId` that has no account key or password. The `ResourceId` must include the subscription ID of SQL Managed Instance, the resource group of SQL Managed instance, and the name of the SQL database. 
 
-Here's an example of how to create a data source to index data from a storage account using the [Create Data Source](/rest/api/searchservice/create-data-source) REST API and a managed identity connection string. The managed identity connection string format is the same for the REST API, .NET SDK, and the Azure portal.  
+Here's an example of how to create a data source to index data from a storage account using the [Create Data Source](/rest/api/searchservice/data-sources/create) REST API and a managed identity connection string. The managed identity connection string format is the same for the REST API, .NET SDK, and the Azure portal.  
 
 ```http
 POST https://[service name].search.windows.net/datasources?api-version=2020-06-30
@@ -141,7 +141,7 @@ api-key: [admin key]
 
 An indexer connects a data source with a target search index, and provides a schedule to automate the data refresh. Once the index and data source have been created, you're ready to create the indexer.
 
-Here's a [Create Indexer](/rest/api/searchservice/create-indexer) REST API call with an Azure SQL indexer definition. The indexer runs when you submit the request.
+Here's a [Create Indexer](/rest/api/searchservice/indexers/create) REST API call with an Azure SQL indexer definition. The indexer runs when you submit the request.
 
 ```http
 POST https://[service name].search.windows.net/indexers?api-version=2020-06-30
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコード変更は、`search-index-azure-sql-managed-instance-with-managed-identity.md` ドキュメントにおいて、いくつかのAPIリンクを更新したことを示しています。具体的な変更内容は以下の通りです。

1. **APIリンクの更新**:
   - データソースの作成に関連するリンクが、`/rest/api/searchservice/create-data-source` から `/rest/api/searchservice/data-sources/create` に修正されました。
   - インデクサー作成に関連するリンクが、`/rest/api/searchservice/create-indexer` から `/rest/api/searchservice/indexers/create` に変更されました。

2. **内容の整合性の向上**:
   - これにより、ドキュメント内で説明されているAPIが最新のエンドポイントに基づいており、ユーザーは正確な情報で操作を行うことができるようになります。

この修正により、ドキュメントは最新のAPI情報を反映し、Azure SQLマネージドインスタンスでのデータインデクシングに関する指示がさらに明確になっています。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -352,7 +352,7 @@ This step shows you how to configure the indexer to run in the private environme
 
 1. Create the data source definition, index, and skillset (if you're using one) as you would normally. There are no properties in any of these definitions that vary when using a shared private endpoint.
 
-1. [Create an indexer](/rest/api/searchservice/create-indexer) that points to the data source, index, and skillset that you created in the preceding step. In addition, force the indexer to run in the private execution environment by setting the indexer `executionEnvironment` configuration property to `private`.
+1. [Create an indexer](/rest/api/searchservice/indexers/create) that points to the data source, index, and skillset that you created in the preceding step. In addition, force the indexer to run in the private execution environment by setting the indexer `executionEnvironment` configuration property to `private`.
 
     ```json
     {
@@ -371,7 +371,7 @@ This step shows you how to configure the indexer to run in the private environme
 After the indexer is created successfully, it should connect to the Azure resource over the private endpoint connection. You can monitor the status of the indexer by using the [Indexer Status API](/rest/api/searchservice/get-indexer-status).
 
 > [!NOTE]
-> If you already have existing indexers, you can update them via the [PUT API](/rest/api/searchservice/create-indexer) by setting the `executionEnvironment` to `private` or using the JSON editor in the portal.
+> If you already have existing indexers, you can update them via the [PUT API](/rest/api/searchservice/indexers/create) by setting the `executionEnvironment` to `private` or using the JSON editor in the portal.
 
 ## 5 - Test the shared private link
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコード変更は、`search-indexer-howto-access-private.md` ドキュメントにおいて、いくつかのAPIリンクを更新したことを示しています。具体的な変更内容は以下の通りです。

1. **APIリンクの更新**:
   - インデクサー作成に関連するリンクが、`/rest/api/searchservice/create-indexer` から `/rest/api/searchservice/indexers/create` に修正されました。

2. **手順の明確化**:
   - インデクサーを作成する際に、プライベート実行環境で動作するように設定する手順がより明確になりました。この修正は、ユーザーが正確な情報に基づいてインデクサーを構成するのに役立ちます。

この修正により、ドキュメントは最新のAPI情報を反映し、プライベート環境でのインデクサーの設定に関する指示がさらに正確かつ明確となっています。

## articles/search/search-indexer-overview.md{#item-292796}

<details>
<summary>Diff</summary>
````diff
@@ -127,7 +127,7 @@ You can create a data source using any of these approaches:
 
 + Using the Azure portal, on the **Data sources** tab of your search service pages, select **Add data source** to specify the data source definition.
 + Using the Azure portal, the [Import data wizard](search-import-data-portal.md) outputs a data source.
-+ Using the REST APIs, call [Create Data Source](/rest/api/searchservice/create-data-source).
++ Using the REST APIs, call [Create Data Source](/rest/api/searchservice/data-sources/create).
 + Using the Azure SDK for .NET, call [SearchIndexerDataSourceConnection class](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection)
 
 ### Step 2: Create an index
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコード変更は、`search-indexer-overview.md` ドキュメントの中で、データソース作成方法に関する一つのAPIリンクを修正したものです。具体的な変更内容は以下の通りです。

1. **APIリンクの更新**:
   - REST APIを使用してデータソースを作成する際のリンクが、`/rest/api/searchservice/create-data-source` から `/rest/api/searchservice/data-sources/create` に更新されました。

2. **手順の明確化**:
   - この変更は、ユーザーが最新のAPIエンドポイントを利用してデータソースを作成できるようにするためのもので、使用されるリンクが正確かつ最新のものであることを保証します。

この修正により、ドキュメントは最新の情報を反映し、Azure サービスを通じてデータソースを作成する際の指示がさらに正確になります。

## articles/search/search-lucene-query-architecture.md{#item-b0d568}

<details>
<summary>Diff</summary>
````diff
@@ -48,7 +48,7 @@ The diagram below illustrates the components used to process a search request.
 
 A search request is a complete specification of what should be returned in a result set. In simplest form, it's an empty query with no criteria of any kind. A more realistic example includes parameters, several query terms, perhaps scoped to certain fields, with possibly a filter expression and ordering rules.  
 
-The following example is a search request you might send to Azure AI Search using the [REST API](/rest/api/searchservice/search-documents).  
+The following example is a search request you might send to Azure AI Search using the [REST API](/rest/api/searchservice/documents/search-post).  
 
 ```
 POST /indexes/hotels/docs/search?api-version=2024-07-01
@@ -72,7 +72,7 @@ For this request, the search engine does the following operations:
 
 3. Orders the resulting set of hotels by proximity to a given geography location, and then returns the results to the calling application. 
 
-Most this article is about processing of the *search query*: `"Spacious, air-condition* +\"Ocean view\""`. Filtering and ordering are out of scope. For more information, see the [Search API reference documentation](/rest/api/searchservice/search-documents).
+Most this article is about processing of the *search query*: `"Spacious, air-condition* +\"Ocean view\""`. Filtering and ordering are out of scope. For more information, see the [Search API reference documentation](/rest/api/searchservice/documents/search-post).
 
 <a name="stage1"></a>
 
@@ -393,7 +393,7 @@ This article explored full text search in the context of Azure AI Search. We hop
 
 + Build the sample index, try out different queries and review results. For instructions, see [Build and query an index in the portal](search-get-started-portal.md).
 
-+ Try other query syntax from the [Search Documents](/rest/api/searchservice/search-documents#bkmk_examples) example section or from [Simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search) in Search explorer in the portal.
++ Try other query syntax from the [Search Documents](/rest/api/searchservice/documents/search-post#examples) example section or from [Simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search) in Search explorer in the portal.
 
 + Review [scoring profiles](/rest/api/searchservice/add-scoring-profiles-to-a-search-index) if you want to tune ranking in your search application.
 
@@ -403,7 +403,7 @@ This article explored full text search in the context of Azure AI Search. We hop
 
 ## See also
 
-[Search Documents REST API](/rest/api/searchservice/search-documents) 
+[Search Documents REST API](/rest/api/searchservice/documents/search-post) 
 
 [Simple query syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search) 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正と補足情報の追加"
}
```

### Explanation
このコード変更は、`search-lucene-query-architecture.md` ドキュメントにおいて、いくつかのAPIリンクと補足情報を更新したことを示しています。具体的には次のような変更が行われました。

1. **APIリンクの更新**:
   - Azure AI Searchにリクエストを送信する際のREST APIのリンクが、`/rest/api/searchservice/search-documents`から`/rest/api/searchservice/documents/search-post`に修正されました。この変更により、正確かつ最新の情報が提供されます。

2. **補足の追加**:
   - 新しいリンクに関連した文脈で、その他のクエリ構文の例やスコアリングプロファイルについての情報が追加されました。これにより、ユーザーがAzure AI Searchを使用してクエリをより効果的に構築するのを助ける内容が強調されています。

3. **内容の明確化**:
   - 検索リクエストの処理に関連する記述が更新され、フィルタリングや順序付けが範囲外である旨が明確にされています。

この変更により、ドキュメントはより最新の情報を提供し、Azure AI Searchの使用方法に関する指示がさらに正確に、かつ役立つものとなっています。

## articles/search/search-more-like-this.md{#item-56c565}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ ms.date: 02/16/2024
 > [!IMPORTANT] 
 > This feature is in public preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [preview REST API](/rest/api/searchservice/index-preview) supports this feature.
 
-`moreLikeThis=[key]` is a query parameter in the [Search Documents API](/rest/api/searchservice/search-documents) that finds documents similar to the document specified by the document key. When a search request is made with `moreLikeThis`, a query is generated with search terms extracted from the given document that describe that document best. The generated query is then used to make the search request. The `moreLikeThis` parameter can't be used with the search parameter, `search=[string]`.
+`moreLikeThis=[key]` is a query parameter in the [Search Documents API](/rest/api/searchservice/documents/search-post) that finds documents similar to the document specified by the document key. When a search request is made with `moreLikeThis`, a query is generated with search terms extracted from the given document that describe that document best. The generated query is then used to make the search request. The `moreLikeThis` parameter can't be used with the search parameter, `search=[string]`.
 
 By default, the contents of all top-level searchable fields are considered. If you want to specify particular fields instead, you can use the `searchFields` parameter. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコード変更は、`search-more-like-this.md` ドキュメントにおいて、`moreLikeThis`クエリパラメーターに関するAPIリンクを更新したことを示しています。具体的には以下のような変更が行われました。

1. **APIリンクの修正**:
   - `moreLikeThis=[key]`が使用される`Search Documents API`のリンクが、`/rest/api/searchservice/search-documents`から`/rest/api/searchservice/documents/search-post`に更新されました。この修正により、正確なAPIエンドポイントが文書に反映されています。

2. **情報の一貫性の向上**:
   - 新しいリンクが反映されたことにより、ユーザーがドキュメントの検索機能を利用する際に、最新の情報に基づいた正確な手順を理解しやすくなっています。

この変更は、ユーザーが「moreLikeThis」機能を活用する際の指示がより明確になることを目的としており、Azure AI Searchの利用体験を向上させるものです。

## articles/search/search-normalizers.md{#item-4477d9}

<details>
<summary>Diff</summary>
````diff
@@ -242,4 +242,4 @@ The example below illustrates a custom normalizer definition with corresponding
 
 + [Analyzers for linguistic and text processing](search-analyzers.md)
 
-+ [Search Documents REST API](/rest/api/searchservice/search-documents)
++ [Search Documents REST API](/rest/api/searchservice/documents/search-post)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコード変更は、`search-normalizers.md` ドキュメントにおいて、`Search Documents REST API`に関するリンクを更新したことを示しています。具体的には次のような変更が行われました。

1. **APIリンクの修正**:
   - `Search Documents REST API`のリンクが、`/rest/api/searchservice/search-documents`から`/rest/api/searchservice/documents/search-post`に変更されました。これにより、正しいAPIエンドポイントがユーザーに提供されるようになります。

2. **情報の追加**:
   - 記事内で言及された内容に関連し、言語処理やテキスト処理に関するアナライザーについてのリンクが新たに追加されました。これにより、ユーザーはさらに情報を得ることができ、理解を深めることができます。

この変更により、ドキュメントの内容が最新の情報で更新され、ユーザーがAzure AI Searchをより適切に利用するための情報が強化されています。

## articles/search/search-pagination-page-layout.md{#item-115902}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.date: 06/12/2024
 
 # How to shape results in Azure AI Search
 
-This article explains how to work with a query response in Azure AI Search. The structure of a response is determined by parameters in the query itself, as described in [Search Documents (REST)](/rest/api/searchservice/Search-Documents) or [SearchResults Class (Azure for .NET)](/dotnet/api/azure.search.documents.models.searchresults-1). 
+This article explains how to work with a query response in Azure AI Search. The structure of a response is determined by parameters in the query itself, as described in [Search Documents (REST)](/rest/api/searchservice/documents/search-post) or [SearchResults Class (Azure for .NET)](/dotnet/api/azure.search.documents.models.searchresults-1). 
 
 Parameters on the query determine:
 
@@ -195,7 +195,7 @@ Hit highlighting refers to text formatting (such as bold or yellow highlights) a
 
 Notice that highlighting is applied to individual terms. There's no highlight capability for the contents of an entire field. If you want to highlight over a phrase, you'll have to provide the matching terms (or phrase) in a quote-enclosed query string. This technique is described further on in this section.
 
-Hit highlighting instructions are provided on the [query request](/rest/api/searchservice/search-documents). Queries that trigger query expansion in the engine, such as fuzzy and wildcard search, have limited support for hit highlighting.
+Hit highlighting instructions are provided on the [query request](/rest/api/searchservice/documents/search-post). Queries that trigger query expansion in the engine, such as fuzzy and wildcard search, have limited support for hit highlighting.
 
 ### Requirements for hit highlighting
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコード変更は、`search-pagination-page-layout.md` ドキュメントにおいて、クエリ応答に関するAPIリンクを更新したことを示しています。具体的には以下のような変更が行われました。

1. **APIリンクの修正**:
   - クエリ応答の構造に関連する`Search Documents`のリンクが、`/rest/api/searchservice/Search-Documents`から`/rest/api/searchservice/documents/search-post`に変更されました。これにより、ユーザーが正しいエンドポイントにアクセスできるようになります。

2. **一貫した情報の提供**:
   - ヒットハイライトの説明においても、同様にリンクが更新されました。これにより、ヒットハイライトに関する指示も最新のAPIに基づいたものとなります。

これらの修正により、ドキュメントの内容が現在のAPI仕様に合わせて更新され、ユーザーに対してより正確で信頼性のある情報が提供されるようになっています。

## articles/search/search-query-create.md{#item-532822}

<details>
<summary>Diff</summary>
````diff
@@ -145,11 +145,11 @@ Search is fundamentally a user-driven exercise, where terms or phrases are colle
 
 | Input | Experience |
 |-------|---------|
-| [Search method](/rest/api/searchservice/search-documents) | A user types the terms or phrases into a search box, with or without operators, and clicks Search to send the request. Search can be used with filters on the same request, but not with autocomplete or suggestions. |
-| [Autocomplete method](/rest/api/searchservice/autocomplete) | A user types a few characters, and queries are initiated after each new character is typed. The response is a completed string from the index. If the string provided is valid, the user clicks Search to send that query to the service. |
+| [Search method](/rest/api/searchservice/documents/search-post) | A user types the terms or phrases into a search box, with or without operators, and clicks Search to send the request. Search can be used with filters on the same request, but not with autocomplete or suggestions. |
+| [Autocomplete method](/rest/api/searchservice/documents/autocomplete-post) | A user types a few characters, and queries are initiated after each new character is typed. The response is a completed string from the index. If the string provided is valid, the user clicks Search to send that query to the service. |
 | [Suggestions method](/rest/api/searchservice/suggestions) | As with autocomplete, a user types a few characters and incremental queries are generated. The response is a dropdown list of matching documents, typically represented by a few unique or descriptive fields. If any of the selections are valid, the user clicks one and the matching document is returned. |
-| [Faceted navigation](/rest/api/searchservice/search-documents#query-parameters) | A page shows clickable navigation links or breadcrumbs that narrow the scope of the search. A faceted navigation structure is composed dynamically based on an initial query. For example, `search=*` to populate a faceted navigation tree composed of every possible category. A faceted navigation structure is created from a query response, but it's also a mechanism for expressing the next query. n REST API reference, `facets` is documented as a query parameter of a Search Documents operation, but it can be used without the `search` parameter.|
-| [Filter method](/rest/api/searchservice/search-documents#query-parameters) | Filters are used with facets to narrow results. You can also implement a filter behind the page, for example to initialize the page with language-specific fields. In REST API reference, `$filter` is documented as a query parameter of a Search Documents operation, but it can be used without the `search` parameter.|
+| [Faceted navigation](/rest/api/searchservice/documents/search-post#searchrequest) | A page shows clickable navigation links or breadcrumbs that narrow the scope of the search. A faceted navigation structure is composed dynamically based on an initial query. For example, `search=*` to populate a faceted navigation tree composed of every possible category. A faceted navigation structure is created from a query response, but it's also a mechanism for expressing the next query. n REST API reference, `facets` is documented as a query parameter of a Search Documents operation, but it can be used without the `search` parameter.|
+| [Filter method](/rest/api/searchservice/documents/search-post#searchrequest) | Filters are used with facets to narrow results. You can also implement a filter behind the page, for example to initialize the page with language-specific fields. In REST API reference, `$filter` is documented as a query parameter of a Search Documents operation, but it can be used without the `search` parameter.|
 
 ## Effect of field attributes on queries
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコード変更は、`search-query-create.md` ドキュメントにおいて、検索メソッドやオートコンプリートメソッドに関連するAPIリンクを更新したことを示しています。具体的には、以下の変更が行われました。

1. **APIリンクの修正**:
   - `Search method`のリンクが、`/rest/api/searchservice/search-documents`から`/rest/api/searchservice/documents/search-post`に変更されました。
   - `Autocomplete method`のリンクも、`/rest/api/searchservice/autocomplete`から`/rest/api/searchservice/documents/autocomplete-post`に更新されています。
   - さらに、`Faceted navigation`と`Filter method`に関連するリンクも同様に修正され、正しいエンドポイントに調整されました。

2. **コンテキストと情報の一貫性**:
   - これらの変更により、ユーザーが適切なAPIを参照できるようになり、最新の情報に基づいた利用ができるようになります。特に、各メソッドに対応する正確なREST APIのパスが反映されたことで、ドキュメントの信頼性が向上します。

この変更はドキュメントの整合性を保つために重要であり、ユーザーがクエリの作成に際して必要な情報を正確に得られるようサポートしています。

## articles/search/search-query-odata-collection-operators.md{#item-9fba57}

<details>
<summary>Diff</summary>
````diff
@@ -94,4 +94,4 @@ For more details on these limitations as well as examples, see [Troubleshooting
 - [Filters in Azure AI Search](search-filters.md)
 - [OData expression language overview for Azure AI Search](query-odata-filter-orderby-syntax.md)
 - [OData expression syntax reference for Azure AI Search](search-query-odata-syntax-reference.md)
-- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/Search-Documents)
+- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/documents/search-post)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコード変更は、`search-query-odata-collection-operators.md` ドキュメントにおいて、Azure AI SearchのAPIリンクを更新したことを示しています。具体的には、以下の変更が行われました。

1. **APIリンクの修正**:
   - "Search Documents (Azure AI Search REST API)" に関するリンクが、`/rest/api/searchservice/Search-Documents`から`/rest/api/searchservice/documents/search-post`に変更されました。この変更により、ユーザーが正確なエンドポイントにアクセスできるようになります。

2. **ドキュメントの信頼性向上**:
   - リンクの更新は、利用者が最新の情報に基づいて正しいAPIを使用できるようにするために重要です。この修正により、ユーザーがリファレンスガイドを利用する際の利便性が増し、正確かつ信頼性のあるリソースにアクセスできるようになります。

この変更は、情報の一貫性を確保し、ユーザーの利便性を向上させるための重要な措置です。

## articles/search/search-query-odata-comparison-operators.md{#item-c92abf}

<details>
<summary>Diff</summary>
````diff
@@ -166,4 +166,4 @@ Rooms/any(room: room/Type eq 'Deluxe Room')
 - [Filters in Azure AI Search](search-filters.md)
 - [OData expression language overview for Azure AI Search](query-odata-filter-orderby-syntax.md)
 - [OData expression syntax reference for Azure AI Search](search-query-odata-syntax-reference.md)
-- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/Search-Documents)
+- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/documents/search-post)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコード変更は、`search-query-odata-comparison-operators.md` ドキュメントにおいて、Azure AI Searchに関するAPIのリンクを更新したことを示しています。具体的には、以下の内容が変更されました。

1. **APIリンクの修正**:
   - "Search Documents (Azure AI Search REST API)" のリンクが、以前のパスである`/rest/api/searchservice/Search-Documents`から、より正確なパスである`/rest/api/searchservice/documents/search-post`に変更されました。このリンクの更新により、ユーザーは最新のドキュメントにアクセスできるようになります。

2. **情報の整合性の向上**:
   - この変更は、利用者が正確な情報に基づいてAPIを利用できるようにするために重要です。正しいエンドポイントへのリンクを提供することは、ユーザーエクスペリエンスの向上に寄与します。

このような小さな変更は、ドキュメント全体の信頼性と有用性を高めるために不可欠です。

## articles/search/search-query-odata-filter.md{#item-69d5d6}

<details>
<summary>Diff</summary>
````diff
@@ -203,7 +203,7 @@ Find a match on phrases within a collection, such as 'heated towel racks' or 'ha
     $filter=Rooms/any(room: room/Tags/any(tag: search.in(tag, 'heated towel racks,hairdryer included', ','))
 ```
 
-Find documents with the word "waterfront". This filter query is identical to a [search request](/rest/api/searchservice/search-documents) with `search=waterfront`.
+Find documents with the word "waterfront". This filter query is identical to a [search request](/rest/api/searchservice/documents/search-post) with `search=waterfront`.
 
 ```odata-filter-expr
     $filter=search.ismatchscoring('waterfront')
@@ -244,4 +244,4 @@ Find documents that have a word that starts with the letters "lux" in the Descri
 - [Filters in Azure AI Search](search-filters.md)
 - [OData expression language overview for Azure AI Search](query-odata-filter-orderby-syntax.md)
 - [OData expression syntax reference for Azure AI Search](search-query-odata-syntax-reference.md)
-- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/Search-Documents)
+- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/documents/search-post)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコード変更は、`search-query-odata-filter.md` ドキュメントの内容を更新し、APIリンクの修正を行ったことを示しています。具体的には、以下の変更が行われました。

1. **APIリンクの変更**:
   - "Search Documents (Azure AI Search REST API)"に関するリンクが、`/rest/api/searchservice/Search-Documents`からより正確なパスである`/rest/api/searchservice/documents/search-post`に更新されました。このリンクの変更により、ユーザーが最新の情報にアクセスできるようになります。

2. **情報の一貫性の向上**:
   - さらに、文中で「waterfront」という単語を含むドキュメントを見つけるためのフィルタクエリの説明も修正されており、APIリクエストが一致するように整えられています。この修正は、ユーザーが正しい情報を基にAPIを利用できるようにするために重要です。

この変更は、ドキュメントの信頼性を高め、利用者が必要な情報を簡単に見つけられるようにすることを目的としています。

## articles/search/search-query-odata-full-text-search-functions.md{#item-5748d4}

<details>
<summary>Diff</summary>
````diff
@@ -25,10 +25,10 @@ translation.priority.mt:
 ---
 # OData full-text search functions in Azure AI Search - `search.ismatch` and `search.ismatchscoring`
 
-Azure AI Search supports full-text search in the context of [OData filter expressions](query-odata-filter-orderby-syntax.md) via the `search.ismatch` and `search.ismatchscoring` functions. These functions allow you to combine full-text search with strict Boolean filtering in ways that are not possible just by using the top-level `search` parameter of the [Search API](/rest/api/searchservice/search-documents).
+Azure AI Search supports full-text search in the context of [OData filter expressions](query-odata-filter-orderby-syntax.md) via the `search.ismatch` and `search.ismatchscoring` functions. These functions allow you to combine full-text search with strict Boolean filtering in ways that are not possible just by using the top-level `search` parameter of the [Search API](/rest/api/searchservice/documents/search-post).
 
 > [!NOTE]
-> The `search.ismatch` and `search.ismatchscoring` functions are only supported in filters in the [Search API](/rest/api/searchservice/search-documents). They are not supported in the [Suggest](/rest/api/searchservice/suggestions) or [Autocomplete](/rest/api/searchservice/autocomplete) APIs.
+> The `search.ismatch` and `search.ismatchscoring` functions are only supported in filters in the [Search API](/rest/api/searchservice/documents/search-post). They are not supported in the [Suggest](/rest/api/searchservice/suggestions) or [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) APIs.
 
 ## Syntax
 
@@ -73,7 +73,7 @@ The parameters are defined in the following table:
 | `queryType` | `Edm.String` | `'simple'` or `'full'`; defaults to `'simple'`. Specifies what query language was used in the `search` parameter. |
 | `searchMode` | `Edm.String` | `'any'` or `'all'`, defaults to `'any'`. Indicates whether any or all of the search terms in the `search` parameter must be matched in order to count the document as a match. When using the [Lucene Boolean operators](query-lucene-syntax.md#bkmk_boolean) in the `search` parameter, they will take precedence over this parameter. |
 
-All the above parameters are equivalent to the corresponding [search request parameters in the Search API](/rest/api/searchservice/search-documents).
+All the above parameters are equivalent to the corresponding [search request parameters in the Search API](/rest/api/searchservice/documents/search-post).
 
 The `search.ismatch` function returns a value of type `Edm.Boolean`, which allows you to compose it with other filter sub-expressions using the Boolean [logical operators](search-query-odata-logical-operators.md).
 
@@ -93,7 +93,7 @@ Both the `search.ismatch` and `search.ismatchscoring` functions can be used in t
 
 ## Examples
 
-Find documents with the word "waterfront". This filter query is identical to a [search request](/rest/api/searchservice/search-documents) with `search=waterfront`.
+Find documents with the word "waterfront". This filter query is identical to a [search request](/rest/api/searchservice/documents/search-post) with `search=waterfront`.
 
 ```odata-filter-expr
     search.ismatchscoring('waterfront')
@@ -136,4 +136,4 @@ Find documents that have a word that starts with the letters "lux" in the Descri
 - [Filters in Azure AI Search](search-filters.md)
 - [OData expression language overview for Azure AI Search](query-odata-filter-orderby-syntax.md)
 - [OData expression syntax reference for Azure AI Search](search-query-odata-syntax-reference.md)
-- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/Search-Documents)
+- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/documents/search-post)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコードの変更は、`search-query-odata-full-text-search-functions.md` ドキュメントにおけるAPIリンクの修正を示しています。具体的な変更内容は以下の通りです。

1. **APIリンクの更新**:
   - `search.ismatch`および`search.ismatchscoring`関数に関する説明文中のリンクが、以前のパスである`/rest/api/searchservice/search-documents`から、より適切なパスである`/rest/api/searchservice/documents/search-post`に変更されました。このリンクの修正により、正確な情報に基づいてAPIを利用できるようになります。

2. **情報の明確化**:
   - フィルタクエリの例においても、「waterfront」という単語を含むドキュメントを見つけるためのクエリが、正しいAPIリクエストに基づいて更新されました。また、`Search API`の他の関連エンドポイントへの言及も更新され、全体の情報の一致性が保たれています。

この変更により、ユーザーは最新のエンドポイントに正確にアクセスできるようになり、使いやすさが向上します。

## articles/search/search-query-odata-geo-spatial-functions.md{#item-859407}

<details>
<summary>Diff</summary>
````diff
@@ -131,4 +131,4 @@ Sort hotels in descending order by `search.score` and `rating`, and then in asce
 - [Filters in Azure AI Search](search-filters.md)
 - [OData expression language overview for Azure AI Search](query-odata-filter-orderby-syntax.md)
 - [OData expression syntax reference for Azure AI Search](search-query-odata-syntax-reference.md)
-- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/Search-Documents)
+- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/documents/search-post)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコードの変更は、`search-query-odata-geo-spatial-functions.md` ドキュメントにおけるAPIリンクの修正を示しています。具体的には、以下の点が修正されました。

1. **APIリンクの更新**:
   - "Search Documents (Azure AI Search REST API)"に関するリンクが、従来のパスである`/rest/api/searchservice/Search-Documents`から、より正確なエンドポイントである`/rest/api/searchservice/documents/search-post`に変更されました。この修正により、ユーザーは正しいAPIリクエストに基づく情報にアクセスできるようになります。

2. **情報の一貫性の向上**:
   - APIリンクの修正によって、ドキュメント内の情報の一致性が強化され、利用者が正確なエンドポイントを参照できるため、実装時の混乱を避けることができます。

この変更は、Azure AI Searchの利用をよりスムーズにし、開発者が最新の情報を利用できるようにすることを目的としています。

## articles/search/search-query-odata-logical-operators.md{#item-61c263}

<details>
<summary>Diff</summary>
````diff
@@ -117,4 +117,4 @@ Match documents for hotels in Vancouver, Canada where there is a deluxe room wit
 - [Filters in Azure AI Search](search-filters.md)
 - [OData expression language overview for Azure AI Search](query-odata-filter-orderby-syntax.md)
 - [OData expression syntax reference for Azure AI Search](search-query-odata-syntax-reference.md)
-- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/Search-Documents)
+- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/documents/search-post)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコードの変更は、`search-query-odata-logical-operators.md` ドキュメントにおけるAPIリンクの修正を示しています。主な修正内容は以下の通りです。

1. **APIリンクの更新**:
   - "Search Documents (Azure AI Search REST API)"に関するリンクが、以前のパスである`/rest/api/searchservice/Search-Documents`から、正しいエンドポイントである`/rest/api/searchservice/documents/search-post`に変更されました。これにより、ユーザーが正確で最新のAPIリクエスト情報にアクセスできるようになります。

2. **情報の一貫性の向上**:
   - リンクの修正によって、ドキュメント内の情報が統一され、検索クエリを利用する際に必要な情報が正確に提供されるようになります。この修正は、ユーザーの混乱を避けるためにも重要です。

この変更により、Azure AI Searchの利用がより効率的に行えるようになり、開発者に対して最新で正確な情報を提供することが目的とされています。

## articles/search/search-query-odata-orderby.md{#item-dff8d3}

<details>
<summary>Diff</summary>
````diff
@@ -84,4 +84,4 @@ Sort hotels in descending order by search.score and rating, and then in ascendin
 - [How to work with search results in Azure AI Search](search-pagination-page-layout.md)
 - [OData expression language overview for Azure AI Search](query-odata-filter-orderby-syntax.md)
 - [OData expression syntax reference for Azure AI Search](search-query-odata-syntax-reference.md)
-- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/Search-Documents)
+- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/documents/search-post)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコードの変更は、`search-query-odata-orderby.md` ドキュメントにおけるAPIリンクの修正を示しています。主な修正点は次の通りです。

1. **APIリンクの更新**:
   - "Search Documents (Azure AI Search REST API)"に関するリンクが、以前のエンドポイントである`/rest/api/searchservice/Search-Documents`から、より具体的なエンドポイントである`/rest/api/searchservice/documents/search-post`に変更されました。この修正により、ユーザーは最新のAPIに正しくアクセスできるようになります。

2. **情報の一貫性の向上**:
   - APIリンクの更新により、他のドキュメントとの関連性が改善され、情報の整合性が保たれることに繋がります。これにより、開発者は必要な情報を迅速に見つけることができ、Azure AI Searchの利用が容易になります。

この変更は、利用者が正確な情報に基づいて検索を行うための重要なステップです。

## articles/search/search-query-odata-search-in-function.md{#item-d768e7}

<details>
<summary>Diff</summary>
````diff
@@ -120,4 +120,4 @@ Find all hotels without the tag 'motel' or 'cabin':
 - [Filters in Azure AI Search](search-filters.md)
 - [OData expression language overview for Azure AI Search](query-odata-filter-orderby-syntax.md)
 - [OData expression syntax reference for Azure AI Search](search-query-odata-syntax-reference.md)
-- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/Search-Documents)
+- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/documents/search-post)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコードの変更は、`search-query-odata-search-in-function.md` ドキュメントにおけるAPIリンクの修正を示しています。主な修正点は次の通りです。

1. **APIリンクの更新**:
   - "Search Documents (Azure AI Search REST API)"に関連するリンクが、以前のパスである`/rest/api/searchservice/Search-Documents`から、正確なエンドポイントである`/rest/api/searchservice/documents/search-post`に変更されました。これにより、利用者が正確なAPI情報にアクセスできるようになります。

2. **情報の整合性の向上**:
   - APIリンクの修正により、ドキュメント全体の情報がより一貫して提供され、他の関連情報との親和性が高まります。この変更により、開発者は必要なリソースを見つけやすくなり、Azure AI Searchをより効果的に活用できるようになります。

この修正は、ユーザーが正確な情報に基づいて操作を行えるようにするための重要な改善です。

## articles/search/search-query-odata-search-score-function.md{#item-f51766}

<details>
<summary>Diff</summary>
````diff
@@ -46,4 +46,4 @@ Sort hotels in descending order by `search.score` and `rating`, and then in asce
 
 - [OData expression language overview for Azure AI Search](query-odata-filter-orderby-syntax.md)
 - [OData expression syntax reference for Azure AI Search](search-query-odata-syntax-reference.md)
-- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/Search-Documents)
+- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/documents/search-post)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコードの変更は、`search-query-odata-search-score-function.md` ドキュメントにおいて、APIリンクが更新されたことを示しています。主なポイントは次の通りです。

1. **APIリンクの変更**:
   - "Search Documents (Azure AI Search REST API)" に関するリンクが、旧URLの`/rest/api/searchservice/Search-Documents`から新URLの`/rest/api/searchservice/documents/search-post`に変更されました。この修正により、ユーザーは正確で最新のAPIエンドポイントにアクセスできるようになります。

2. **情報の一貫性の向上**:
   - 上記のリンクの修正により、文書がより整合性のあるものとなり、他の関連ドキュメントとの関連性が強化されます。これにより、Azure AI Searchを利用する開発者にとって、必要な情報を迅速に見つけられるようになります。

この変更は、ユーザーが最新のAPI情報に基づいて探索や操作をより効果的に行えるようにするための重要な改善です。

## articles/search/search-query-odata-select.md{#item-8d6e1d}

<details>
<summary>Diff</summary>
````diff
@@ -106,4 +106,4 @@ An example result might look like this:
 - [How to work with search results in Azure AI Search](search-pagination-page-layout.md)
 - [OData expression language overview for Azure AI Search](query-odata-filter-orderby-syntax.md)
 - [OData expression syntax reference for Azure AI Search](search-query-odata-syntax-reference.md)
-- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/Search-Documents)
+- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/documents/search-post)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコードの変更は、`search-query-odata-select.md` ドキュメントにおいてAPIリンクが改訂されたことを示しています。具体的な変更点は以下の通りです。

1. **APIリンクの修正**:
   - "Search Documents (Azure AI Search REST API)" に関するリンクが、以前のパスである`/rest/api/searchservice/Search-Documents`から、新しいパスである`/rest/api/searchservice/documents/search-post`に変更されています。この修正により、ユーザーは最新のAPIエンドポイントにアクセスできるようになり、正確な情報が提供されます。

2. **整合性向上**:
   - このリンクの変更により、文書全体の情報が一貫性を持ち、他の関連資料との関連性が強化されます。これにより、Azure AI Searchを使用する開発者が必要なリソースを迅速に見つけることができるようになります。

この修正は、ユーザーにとって重要な情報を適切に伝えるための重要な改善となります。

## articles/search/search-query-odata-syntax-reference.md{#item-14b8d9}

<details>
<summary>Diff</summary>
````diff
@@ -203,6 +203,6 @@ To visually explore the OData language grammar supported by Azure AI Search, try
 ## See also  
 
 - [Filters in Azure AI Search](search-filters.md)
-- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/Search-Documents)
+- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/documents/search-post)
 - [Lucene query syntax](query-lucene-syntax.md)
 - [Simple query syntax in Azure AI Search](query-simple-syntax.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコードの変更は、`search-query-odata-syntax-reference.md` ドキュメントにおいてAPIリンクが更新されたことを示しています。具体的な変更点は以下の通りです。

1. **APIリンクの変更**:
   - "Search Documents (Azure AI Search REST API)" リンクが、古いパスである`/rest/api/searchservice/Search-Documents`から新しいパスである`/rest/api/searchservice/documents/search-post`に変更されました。この更新により、ユーザーは最新のAPIエンドポイントに正しくアクセスできるようになります。

2. **文書の整合性向上**:
   - このリンクの修正は、文書全体の一貫性を向上させ、他の関連資料との整合性を強化します。これにより、Azure AI Searchを利用する開発者は、必要な情報をより簡単に見つけることができるようになります。

この修正は、正確な情報を提供するために重要であり、ユーザーの利便性を向上させるための重要な改善となります。

## articles/search/search-query-overview.md{#item-dcd5d6}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,7 @@ This article brings focus to the last category: queries that work on plain text
 
 ## Autocomplete and suggested queries
 
-[Autocomplete or suggested results](search-add-autocomplete-suggestions.md) are alternatives to **`search`** that fire successive query requests based on partial string inputs (after each character) in a search-as-you-type experience. You can use **`autocomplete`** and **`suggestions`** parameter together or separately, as described in [this walkthrough](tutorial-csharp-type-ahead-and-suggestions.md), but you can't use them with **`search`**. Both completed terms and suggested queries are derived from index contents. The engine never returns a string or suggestion that is nonexistent in your index. For more information, see [Autocomplete (REST API)](/rest/api/searchservice/autocomplete) and [Suggestions (REST API)](/rest/api/searchservice/suggestions).
+[Autocomplete or suggested results](search-add-autocomplete-suggestions.md) are alternatives to **`search`** that fire successive query requests based on partial string inputs (after each character) in a search-as-you-type experience. You can use **`autocomplete`** and **`suggestions`** parameter together or separately, as described in [this walkthrough](tutorial-csharp-type-ahead-and-suggestions.md), but you can't use them with **`search`**. Both completed terms and suggested queries are derived from index contents. The engine never returns a string or suggestion that is nonexistent in your index. For more information, see [Autocomplete (REST API)](/rest/api/searchservice/documents/autocomplete-post) and [Suggestions (REST API)](/rest/api/searchservice/suggestions).
 
 ## Filter search
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコードの変更は、`search-query-overview.md` ドキュメントにおいて、APIリンクの修正が行われたことを示しています。具体的な変更点は以下の通りです。

1. **APIリンクの更新**:
   - "Autocomplete (REST API)" に関するリンクが、以前のパスである `/rest/api/searchservice/autocomplete` から新しいパスである `/rest/api/searchservice/documents/autocomplete-post` に変更されました。この変更により、ユーザーは最新のAPIエンドポイントにアクセスできるようになります。

2. **文書の整合性向上**:
   - リンクの修正は、文書全体の情報の一貫性を強化し、他の関連資料とともに、一貫したナビゲーションが提供されることを助けます。これにより、Azure AI Searchを利用した開発者は、より正確で最新の情報を得ることができるようになります。

この修正は、システムの機能を利用するための重要な部分を更新するものであり、ユーザーにとって情報の正確性とアクセスの容易さを向上させる役割を果たします。

## articles/search/search-query-partial-matching.md{#item-bd97dc}

<details>
<summary>Diff</summary>
````diff
@@ -235,7 +235,7 @@ The previous sections explained the logic. This section steps through each API y
 
 + [Test Analyzer](/rest/api/searchservice/test-analyzer) was introduced in [Set an analyzer](#set-an-analyzer). Test some of the strings in your index using various analyzers to understand how terms are tokenized.
 
-+ [Search Documents](/rest/api/searchservice/search-documents) explains how to construct a query request, using either [simple syntax](query-simple-syntax.md) or [full Lucene syntax](query-lucene-syntax.md) for wildcard and regular expressions.
++ [Search Documents](/rest/api/searchservice/documents/search-post) explains how to construct a query request, using either [simple syntax](query-simple-syntax.md) or [full Lucene syntax](query-lucene-syntax.md) for wildcard and regular expressions.
 
   For partial term queries, such as querying "3-6214" to find a match on "+1 (425) 703-6214", you can use the simple syntax: `search=3-6214&queryType=simple`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコードの変更は、`search-query-partial-matching.md`ドキュメントにおいて、APIへのリンクが更新されたことを示しています。具体的な変更点は以下の通りです。

1. **APIリンクの更新**:
   - "Search Documents"に関するリンクが、以前のパスである`/rest/api/searchservice/search-documents`から新しいパスである`/rest/api/searchservice/documents/search-post`に変更されました。この修正により、ユーザーは最新のAPIエンドポイントにアクセスすることができます。

2. **文書の整合性向上**:
   - このリンクの修正は、Azure AI Searchの使用における情報の整合性を改善し、正確で最新の情報を提供することを目的としています。これにより、開発者がクエリリクエストの構築方法を理解しやすくなり、特にワイルドカードや正規表現を利用する際の利便性が向上します。

この修正は、ユーザーが必要な情報に簡単にアクセスできるようにし、文書の質を向上させる重要な役割を果たします。

## articles/search/search-query-troubleshoot-collection-filters.md{#item-abeca4}

<details>
<summary>Diff</summary>
````diff
@@ -214,4 +214,4 @@ If you write filters often, and understanding the rules from first principles wo
 - [Filters in Azure AI Search](search-filters.md)
 - [OData expression language overview for Azure AI Search](query-odata-filter-orderby-syntax.md)
 - [OData expression syntax reference for Azure AI Search](search-query-odata-syntax-reference.md)
-- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/Search-Documents)
+- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/documents/search-post)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコードの変更は、`search-query-troubleshoot-collection-filters.md`ドキュメントにおいて、APIへのリンクが更新されたことを示しています。具体的な変更点は以下の通りです。

1. **APIリンクの更新**:
   - "Search Documents"に関するリンクが、以前のパスである`/rest/api/searchservice/Search-Documents`から新しいパスである`/rest/api/searchservice/documents/search-post`に変更されました。この変更により、ユーザーは最新のAPIエンドポイントにアクセスできるようになります。

2. **文書の整合性向上**:
   - リンクの修正は、ユーザーが Azure AI Search の機能を利用する際の利便性を高め、正確で最新の情報を提供することに貢献します。また、他の関連資料とともに一貫したナビゲーションが保証され、開発者にとっての情報探しが容易になります。

この修正は、開発者が必要な情報に簡単にアクセスできるようにし、文書全体の質を向上させる重要な役割を果たします。

## articles/search/search-query-understand-collection-filters.md{#item-32c01a}

<details>
<summary>Diff</summary>
````diff
@@ -188,4 +188,4 @@ For specific examples of which kinds of filters are allowed and which aren't, se
 - [Filters in Azure AI Search](search-filters.md)
 - [OData expression language overview for Azure AI Search](query-odata-filter-orderby-syntax.md)
 - [OData expression syntax reference for Azure AI Search](search-query-odata-syntax-reference.md)
-- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/Search-Documents)
+- [Search Documents &#40;Azure AI Search REST API&#41;](/rest/api/searchservice/documents/search-post)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
このコードの変更は、`search-query-understand-collection-filters.md`ドキュメントにおいて、APIへのリンクが修正されたことを示しています。具体的な変更点は以下の通りです。

1. **APIリンクの更新**:
   - "Search Documents"に関するリンクが、以前のパスである`/rest/api/searchservice/Search-Documents`から新しいパスである`/rest/api/searchservice/documents/search-post`に変更されました。この修正により、ユーザーは最新のAPIエンドポイントに簡単にアクセスできるようになります。

2. **文書の整合性向上**:
   - リンクの修正は、Azure AI Searchに関する情報の正確性を向上させ、関連資料とともに一貫した参照を提供します。これにより、開発者がクエリフィルタに関する情報を迅速に見つけることができるようになり、より効果的に検索機能を活用できるようになります。

この修正は、ユーザーが必要な情報に簡単にアクセスしやすくし、文書全体の質と実用性を向上させる重要な役割を果たしています。

## articles/search/search-semi-structured-data.md{#item-d3388d}

<details>
<summary>Diff</summary>
````diff
@@ -133,7 +133,7 @@ See [Quickstart: Text search using REST](search-get-started-rest.md) if you need
 
 ## Create a data source
 
-[Create Data Source (REST)](/rest/api/searchservice/create-data-source) creates a data source connection that specifies what data to index.
+[Create Data Source (REST)](/rest/api/searchservice/data-sources/create) creates a data source connection that specifies what data to index.
 
 ```http
 ### Create a data source
@@ -245,7 +245,7 @@ POST {{baseUrl}}/indexes?api-version=2024-07-01  HTTP/1.1
 
 ## Create and run an indexer
 
-[Create Indexer](/rest/api/searchservice/create-indexer) creates an indexer on your search service. An indexer connects to the data source, loads and indexes data, and optionally provides a schedule to automate the data refresh.
+[Create Indexer](/rest/api/searchservice/indexers/create) creates an indexer on your search service. An indexer connects to the data source, loads and indexes data, and optionally provides a schedule to automate the data refresh.
 
 The indexer configuration includes the `jsonArray` parsing mode and a `documentRoot`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
この変更は、`search-semi-structured-data.md`ドキュメントにおけるAPIのリンクが修正されたことを示しています。具体的な変更点は次の通りです。

1. **APIリンクの更新**:
   - 最初の変更では、"Create Data Source"に関するリンクが、以前のパスである`/rest/api/searchservice/create-data-source`から新しいパスである`/rest/api/searchservice/data-sources/create`に変更されました。
   - さらに、"Create Indexer"に関するリンクも、以前のパスである`/rest/api/searchservice/create-indexer`から新しいパスである`/rest/api/searchservice/indexers/create`に更新されています。

2. **情報の正確性向上**:
   - これらのリンク修正は、Azure AI Searchに関連する最新のAPIエンドポイントを反映しており、ユーザーが正確で最新の情報にアクセスしやすくなります。これにより、開発者は確実に正しいURLを使用してAPIにアクセスしたり、データソースやインデクサーの作成を行うことができます。

この修正は、文書の整合性を保ち、ユーザーが求める情報を迅速に見つけられるようにするための重要な調整です。

## articles/search/search-sku-manage-costs.md{#item-6e0122}

<details>
<summary>Diff</summary>
````diff
@@ -50,7 +50,7 @@ Billing is based on capacity (SUs) and the costs of running premium features, su
 
 <sup>1</sup> Applies only if you use or enable the feature.
 
-<sup>2</sup> In an [indexer configuration](/rest/api/searchservice/create-indexer#indexer-parameters), `imageAction` is the parameter that triggers image extraction. If `imageAction` is set to "none" (the default), you won't be charged for image extraction. Costs are incurred when `imageAction` parameter is set *and* you include OCR, Image Analysis, or Document Extraction in a skillset.
+<sup>2</sup> In an [indexer configuration](/rest/api/searchservice/indexers/create#indexer-parameters), `imageAction` is the parameter that triggers image extraction. If `imageAction` is set to "none" (the default), you won't be charged for image extraction. Costs are incurred when `imageAction` parameter is set *and* you include OCR, Image Analysis, or Document Extraction in a skillset.
 
 You aren't billed on the number of full text or vector queries, query responses, or documents ingested, although [service limits](search-limits-quotas-capacity.md) do apply at each tier.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIリンクの修正"
}
```

### Explanation
この変更は、`search-sku-manage-costs.md`ドキュメントにおいて、APIへのリンクが修正されたことを示しています。具体的な変更内容は次の通りです。

1. **APIリンクの更新**:
   - "indexer configuration"に関するリンクが、以前のパスである`/rest/api/searchservice/create-indexer#indexer-parameters`から新しいパスである`/rest/api/searchservice/indexers/create#indexer-parameters`に変更されました。このリンク修正により、ユーザーがインデクサー構成に関する最新の情報にアクセスできるようになります。

2. **情報の正確性向上**:
   - この修正により、ユーザーはインデクサーでの画像処理アクションの設定についてより正確な情報を得ることができ、画像抽出のコストに関する理解を深めることができます。特に、`imageAction`パラメータのデフォルト値や設定方法についての情報が明確になっています。

この変更は、文書全体の整合性とユーザーの理解を深めるために重要です。正しいリンクを提供することは、ドキュメントの信頼性を保ちながら、ユーザーが必要な情報に迅速にアクセスできるようにするための基本です。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -57,13 +57,11 @@ Currently, several regions are at capacity for Basic and Standard (S1) tiers and
 
 | Region | Disabled tier (SKU) due to over-capacity |
 |--------|------------------------------------------|
-| Japan East | Basic, Standard (S1) |
-| Qatar Central | Basic, Standard (S1) |
-| North Europe | Basic, Standard (S1) |
+| Central US | S2, S3, S3HD, L1, L2 |
+| Japan East | S2, S3, S3HD, L1, L2 |
+| Qatar Central | All tiers|
+| South Central US | All tiers |
 | West Europe | All tiers |
-| Central US | Basic, Standard (S1) |
-| South Central US | Basic, Standard (S1) |
-| West US 2 | Basic, Standard (S1) |
 | West US 3| All tiers |
 
 <a name="premium-features"></a>
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SKU制限の情報変更"
}
```

### Explanation
この変更は、`search-sku-tier.md`ドキュメントにおいて、SKU制限に関する情報が更新されたことを示しています。具体的な変更内容は次の通りです。

1. **SKU制限情報の変更**:
   - いくつかのリージョンにおけるSKUの制限が変更され、特定のティアが無効になった地域が新たに追加されています。具体的には、日本東部、カタール中部、中央アメリカ南部、中央アメリカ、北欧などで、S2、S3、S3HD、L1、L2ティアの利用制限が新たに示されています。

2. **情報の明確化**:
   - 表形式で整理された情報により、どのリージョンがどのSKUで制限を受けているかが分かりやすく示されており、ユーザーは自分の使用可能なティアを簡単に確認できるようになっています。また、これにより、特定のリージョンでの利用可能なサービスについての理解が深まります。

この修正は、ユーザーがサービスの利用可能性を把握しやすくするために重要であり、利用状況に応じた迅速な意思決定を支援します。正確で最新の情報を提供することは、ドキュメントの価値を高める要素となります。

## articles/search/search-synapseml-cognitive-services.md{#item-dcc36f}

<details>
<summary>Diff</summary>
````diff
@@ -251,7 +251,7 @@ Paste the following code into the seventh cell and then run it. No modifications
 + [Query syntax](query-simple-syntax.md)
 + [Query examples](search-query-simple-examples.md)
 
-There's no transformer or module that issues queries. This cell is a simple call to the [Search Documents REST API](/rest/api/searchservice/search-documents). 
+There's no transformer or module that issues queries. This cell is a simple call to the [Search Documents REST API](/rest/api/searchservice/documents/search-post). 
 
 This particular example is searching for the word "door" (`"search": "door"`). It also returns a "count" of the number of matching documents, and selects just the contents of the "Description' and "Translations" fields for the results. If you want to see the full list of fields, remove the "select" parameter.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIエンドポイントの修正"
}
```

### Explanation
この変更は、`search-synapseml-cognitive-services.md`ドキュメントにおいて、APIエンドポイントに関する情報が修正されたことを示しています。具体的な変更内容は次の通りです。

1. **エンドポイントの修正**:
   - `Search Documents REST API`への呼び出し部分が、以前のエンドポイント`/rest/api/searchservice/search-documents`から新しいエンドポイントである`/rest/api/searchservice/documents/search-post`に変更されました。この修正により、ユーザーは正確なAPIパスを参照できるようになり、よりスムーズに実装を行えるようになります。

2. **情報の整合性向上**:
   - エンドポイントに関連する説明が更新され、最新のAPI仕様に準拠した形となりました。この修正は、ドキュメントの信頼性を保つために重要であり、ユーザーがAPIを通じて行う作業の正確性を高めます。

この修正は、開発者やユーザーが正しいAPIを利用したいと考える際に役立つ重要な変更であり、必要な情報へのアクセスを簡単にします。これにより、ドキュメントの価値を向上させることができます。

## articles/search/search-traffic-analytics.md{#item-c76f2f}

<details>
<summary>Diff</summary>
````diff
@@ -109,7 +109,7 @@ Every time that a search request is issued by a user, you should log that as a s
 + **ScoringProfile**: (string) name of the scoring profile used, if any
 
 > [!NOTE]
-> Request the count of user generated queries by adding $count=true to your search query. For more information, see [Search Documents (REST)](/rest/api/searchservice/search-documents#query-parameters).
+> Request the count of user generated queries by adding $count=true to your search query. For more information, see [Search Documents (REST)](/rest/api/searchservice/documents/search-post#searchrequest).
 >
 
 ```csharp
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIドキュメントの更新"
}
```

### Explanation
この変更は、`search-traffic-analytics.md`ドキュメントにおいて、検索リクエストに関するAPIの情報が修正されたことを示しています。具体的な変更内容は次の通りです。

1. **エンドポイントの更新**:
   - ユーザー生成クエリのカウントを取得するためのリクエストの説明が更新され、以前のエンドポイント`/rest/api/searchservice/search-documents#query-parameters`から新しいエンドポイント`/rest/api/searchservice/documents/search-post#searchrequest`に変更されました。この変更により、正確なAPIの使用法が提示され、ユーザーは最新のエンドポイントを利用することができるようになります。

2. **情報の一貫性**:
   - この修正は、APIドキュメントの整合性を保つために重要であり、利用者がAPIを正しく使うためのガイダンスを強化します。正確な情報を提供することは、開発者がシステムを効果的に活用するために必要です。

この修正は、ユーザーや開発者が正しいAPIを容易に参照し、実装を確認する上での利便性を向上させる重要な変更です。全体として、ドキュメントの信頼性を向上させる役割を果たします。

## articles/search/search-what-is-data-import.md{#item-d73ef5}

<details>
<summary>Diff</summary>
````diff
@@ -94,7 +94,7 @@ Use the following tools and APIs for indexer-based indexing:
 + Azure SDK for Java: [SearchIndexer](/java/api/com.azure.search.documents.indexes.models.searchindexer), [SearchIndexerDataSourceConnection](/java/api/com.azure.search.documents.indexes.models.searchindexerdatasourceconnection), [SearchIndex](/java/api/com.azure.search.documents.indexes.models.searchindex),
 + Azure SDK for JavaScript: [SearchIndexer](/javascript/api/@azure/search-documents/searchindexer), [SearchIndexerDataSourceConnection](/javascript/api/@azure/search-documents/searchindexerdatasourceconnection), [SearchIndex](/javascript/api/@azure/search-documents/searchindex),
 
-Indexer functionality is exposed in the [Azure portal], the [REST API](/rest/api/searchservice/create-indexer), and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.searchindexerclient).
+Indexer functionality is exposed in the [Azure portal], the [REST API](/rest/api/searchservice/indexers/create), and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.searchindexerclient).
 
 An advantage to using the portal is that Azure AI Search can usually generate a default index schema by reading the metadata of the source dataset. 
 
@@ -104,7 +104,7 @@ A quick way to perform a preliminary check on the document upload is to use [**S
 
 :::image type="content" source="media/search-explorer/search-explorer-cmd2.png" alt-text="Screenshot of Search Explorer command in the Azure portal." border="true":::
 
-The explorer lets you query an index without having to write any code. The search experience is based on default settings, such as the [simple syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search) and default [searchMode query parameter](/rest/api/searchservice/search-documents). Results are returned in JSON so that you can inspect the entire document.
+The explorer lets you query an index without having to write any code. The search experience is based on default settings, such as the [simple syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search) and default [searchMode query parameter](/rest/api/searchservice/documents/search-post). Results are returned in JSON so that you can inspect the entire document.
 
 Here's an example query that you can run in Search Explorer in JSON view. The "HotelId" is the document key of the hotels-sample-index. The filter provides the document ID of a specific document:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIエンドポイントの更新"
}
```

### Explanation
この変更は、`search-what-is-data-import.md`ドキュメントにおいて、インデクサー機能に関連するAPIの情報が修正されたことを示しています。具体的な変更内容は次の通りです。

1. **エンドポイントの修正**:
   - インデクサー機能に関連するREST APIのエンドポイントが更新され、以前のパス`/rest/api/searchservice/create-indexer`から新しいパス`/rest/api/searchservice/indexers/create`に変更されました。この修正により、正確なAPIの利用情報が提供され、ユーザーは最新のエンドポイントを参照できるようになります。

2. **ユーザーエクスペリエンスの向上**:
   - 検索エクスプローラーの説明にも同様の修正が行われ、デフォルトの設定に基づくAPIの使用法が最新のものに調整されました。これにより、ユーザーがインデックスを照会する際の経験がよりスムーズになります。

この修正は、ドキュメントの信頼性を高め、開発者が正しい情報をもとに実装を行うためのサポートを強化する重要な役割を果たします。正確なAPI情報を提供することで、ユーザーの作業効率を向上させることにつながります。

## articles/search/semantic-answers.md{#item-c3fee9}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ All prerequisites that apply to [semantic queries](semantic-how-to-query-request
 + Search documents in the index must contain text having the characteristics of an answer, and that text must exist in one of the fields listed in the [semantic configuration](semantic-how-to-configure.md). For example, given a query "what is a hash table", if none of the fields in the semantic configuration contain passages that include "A hash table is ...", then it's unlikely an answer is returned.
 
 > [!NOTE]
-> Starting in 2021-04-30-Preview, in [Create or Update Index (Preview)](/rest/api/searchservice/preview-api/create-or-update-index) requests, a `"semanticConfiguration"` is required for specifying input fields for semantic ranking.
+> Starting in 2021-04-30-Preview, [Create or Update Index](/rest/api/searchservice/indexes/create-or-update) requests began enfording a `"semanticConfiguration"` requirement for specifying input fields used in semantic ranking.
 
 ## What is a semantic answer?
 
@@ -65,7 +65,7 @@ To return a semantic answer, the query must have the semantic `"queryType"`, `"q
 
 + `"queryType"` must be set to "semantic.
 
-+ `"queryLanguage"` must be one of the values from the [supported languages list (REST API)](/rest/api/searchservice/preview-api/search-documents#queryLanguage).
++ `"queryLanguage"` must be one of the values from the [supported languages list (REST API)](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true#querylanguage).
 
 + A `"semanticConfiguration"` determines which string fields provide tokens to the extraction model. The same fields that produce captions also produce answers. See [Create a semantic configuration](semantic-how-to-configure.md) for details.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティッククエリに関するドキュメントの修正"
}
```

### Explanation
この変更は、`semantic-answers.md`ドキュメントにおいて、セマンティッククエリの要件やAPIに関する情報が修正されたことを示しています。具体的な変更内容は次の通りです。

1. **APIエンドポイントの更新**:
   - インデックスを作成または更新する際のAPIリクエストの説明が変更されました。具体的には、以前のエンドポイント`/rest/api/searchservice/preview-api/create-or-update-index`から新しいエンドポイント`/rest/api/searchservice/indexes/create-or-update`に更新されました。この変更により、最新のAPI仕様に従った正確な情報が提供されます。

2. **クエリパラメータの具体化**:
   - `"queryLanguage"`の指示が更新され、参照されているREST APIのリンクが新しいバージョンのエンドポイントへと修正されました。この変更は、ユーザーが正しい情報にアクセスし、セマンティッククエリに必要な構成要素を理解する上で重要です。

3. **追加情報の提供**:
   - `"semanticConfiguration"`の役割についての説明が強化され、どのフィールドが抽出モデルにトークンを提供するかが明確にされています。これにより、ユーザーはセマンティック構成の重要性をより深く理解できるようになります。

この修正は、開発者とユーザーが最新のAPI情報とセマンティッククエリの実装に必要な詳細を正確に把握できるようにし、システムの利用をよりスムーズにすることを目的としています。


