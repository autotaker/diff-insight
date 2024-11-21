---
date: '2024-11-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ef5a197...MicrosoftDocs:f59daa8
summary: 今回の変更は、Azureのドキュメントに対する小規模な更新で、新しい情報の追加や説明の明確化が行われました。具体的には、画像寸法に関する要件やサポートされている言語のセクションが新たに追加され、クエリリライトやベクトル検索の管理に関する詳細な説明が加わりました。また、Markdownブロブインデックス作成に関するアクセス層の条件が改訂され、ホットおよびクールアクセス層のみがサポートされるようになりました。この更新により、ユーザーはより明確で詳細な情報を得られ、Azure
  AIサービスの利用が容易になります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ef5a197...MicrosoftDocs:f59daa8){target="_blank"}

# Highlights
今回の変更は、Azure関連のドキュメントに対する小規模な更新を示しており、特に新しい情報の追加や既存の説明の明確化に焦点を当てています。新機能には、画像寸法の要件やサポートされる言語のセクションの追加があり、クエリリライトやベクトル検索のストレージオプションの管理に関する詳細な説明が追加されています。破壊的な変更として、Markdownブロブインデックス作成に関するアクセス層の条件が改訂されています。

## New features
- ドキュメントインテリジェンスレイアウトの記事に画像寸法に関する要件の追加
- サポートされている言語セクションとリンクの追加
- クエリリライトにおける言語設定の強調

## Breaking changes
- Markdownブロブインデックス作成でホットおよびクールアクセス層のみサポートするように変更

## Other updates
- 日付の更新
- ベクトルストレージオプションにおけるプロパティ設定の詳細な説明追加

# Insights
今回の更新は、Azure AIの様々な機能においてユーザーがより明確で詳細な情報を得られるように調整されたものです。まず、ドキュメントインテリジェンスレイアウトの記事では、画像寸法の要件が具体的に示されることにより、ユーザーは処理可能なデータ仕様を理解できます。また、パスワード付きPDFのインデックス化の手順が明確化されたことで、事前準備に関する理解不足によるトラブルを回避できるようになりました。さらに、サポートされている言語セクションの追加は、多国籍展開時の言語選択における資産となります。

Markdownブロブインデックス作成ガイドの更新では、アクセス層がホットとクールに限定されたことが特筆されます。これは、より厳密なストレージ管理をユーザーに促し、新しい利用条件を反映した戦略を練る助けとなります。

クエリリライトに関する更新では、言語設定が詳細に記載されており、多言語環境での検索最適化に重要です。検索言語設定に基づくリライトが推奨され、言語固有のニュアンスを反映できるようになりました。

最後に、ベクトル検索のストレージオプションでは、データ保存の非可逆性や新しいベクトルフィールド追加に関する制約が明示されています。この説明の強化により誤設定を避け、エラーを低減することが可能になります。

このようなドキュメンテーションの改訂は、Azure AIサービスの利用におけるユーザービリティと信頼性を向上させ、エンドユーザーが意図した結果を得るための最適なガイドラインを提供します。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-document-intelligence-layout.md](#item-62c06f) | minor update | 検索スキルのドキュメントインテリジェンスレイアウトの更新 | modified | 14 | 1 | 15 | 
| [search-how-to-index-markdown-blobs.md](#item-c94a20) | minor update | Markdownブロブのインデックス作成に関するガイドの更新 | modified | 2 | 2 | 4 | 
| [semantic-how-to-query-rewrite.md](#item-3e168f) | minor update | クエリリライトに関する文書の更新 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-storage-options.md](#item-ee1680) | minor update | ベクトル検索のストレージオプションに関する文書の更新 | modified | 18 | 11 | 29 | 


# Modified Contents
## articles/search/cognitive-search-skill-document-intelligence-layout.md{#item-62c06f}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - references_regions
 ms.topic: reference
-ms.date: 11/19/2024
+ms.date: 11/20/2024
 ---
 
 # Document Layout skill
@@ -56,6 +56,19 @@ Microsoft.Skills.Util.DocumentIntelligenceLayoutSkill
 + Image dimensions must be between 50 pixels x 50 pixels or 10,000 pixels x 10,000 pixels.
 + If your PDFs are password-locked, remove the lock before running the indexer.
 
+## Supported languages
+
+Refer to [Azure AI Document Intelligence layout model supported languages](/azure/ai-services/document-intelligence/language-support/ocr?view=doc-intel-3.1.0&tabs=read-print%2Clayout-print%2Cgeneral#layout) for printed text.
+
+## Limitations
+
+During the public preview, this skill has the following restrictions:
+
++ The skill can't extract images embedded within documents.
++ Page numbers are not included in the generated output.
++ The skill is not suitable for large documents requiring more than 5 minutes of processing in the AI Document Intelligence layout model. The skill will time out, but charges will still apply to the AI Services multi-services resource if it is attached to the skillset for billing purposes. Ensure documents are optimized to stay within processing limits to avoid unnecessary costs.
+
+  
 ## Skill parameters
 
 Parameters are case-sensitive.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索スキルのドキュメントインテリジェンスレイアウトの更新"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスレイアウトに関する記事の小規模な更新を示しています。主な修正点は、以下の内容です：

1. **日付の更新**: 更新された日付が「2024年11月19日」から「2024年11月20日」に変更されました。
2. **新しい情報の追加**:
   - 画像の寸法に関する要件が追加され、最小および最大のピクセル数が指定されています（50x50ピクセルから10,000x10,000ピクセル）。
   - PDF文書がパスワードで保護されている場合は、インデクサーを実行する前にそのロックを解除する必要があることが明記されています。
   - 「サポートされている言語」セクションが新たに追加され、Azure AI ドキュメントインテリジェンスレイアウトモデルでサポートされている言語へのリンクが提供されています。
   - 公開プレビュー中の制限についての詳細も追加され、特に処理に関する制限や、費用に関する注意事項が含まれています。

これにより、読者はドキュメントインテリジェンスレイアウトスキルの利用に関する重要な更新情報や制限を把握しやすくなっています。

## articles/search/search-how-to-index-markdown-blobs.md{#item-c94a20}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 11/20/2024
 ---
 
 # Index Markdown blobs and files in Azure AI Search
@@ -31,7 +31,7 @@ In Azure AI Search, indexers for Azure Blob Storage, Azure Files, and OneLake su
 
   For OneLake, make sure you meet all of the requirements of the [OneLake indexer](search-how-to-index-onelake-files.md#prerequisites).
 
-  Azure Storage for [blob indexers](search-howto-indexing-azure-blob-storage.md#prerequisites) and [file indexers](search-file-storage-integration.md#prerequisites) is a standard performance (general-purpose v2) instance that supports hot, cool, and cold access tiers.
+  Azure Storage for [blob indexers](search-howto-indexing-azure-blob-storage.md#prerequisites) and [file indexers](search-file-storage-integration.md#prerequisites) is a standard performance (general-purpose v2) instance that supports hot and cool access tiers.
 
 ## Markdown parsing mode parameters
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Markdownブロブのインデックス作成に関するガイドの更新"
}
```

### Explanation
この変更は、MarkdownブロブとファイルをAzure AI Searchでインデックス化する方法に関する文書の更新を示しています。主な修正点は以下の通りです：

1. **日付の更新**: 更新された日付が「2024年11月19日」から「2024年11月20日」に変更されました。
2. **内容の変更**:
   - Azure Storageに関する記述が修正され、Blobインデクサーおよびファイルインデクサーに関するパフォーマンス要件が更新されました。具体的には、以前は「ホット、クール、コールドアクセス層」をサポートしていると記載されていましたが、変更後は「ホットおよびクールアクセス層」のみをサポートするように更新されています。

この修正により、Azure AI Searchを利用するユーザーに対して、Markdownブロブのインデックス作成に関する最新の技術要件が提供され、正確な情報に基づいた設定が可能となります。

## articles/search/semantic-how-to-query-rewrite.md{#item-3e168f}

<details>
<summary>Diff</summary>
````diff
@@ -75,7 +75,7 @@ In this REST API example, we use [Search Documents](/rest/api/searchservice/docu
     - We set "semanticConfiguration" to a [predefined semantic configuration](semantic-how-to-configure.md) embedded in your index.
     - We set "queryType" to "semantic". We either need to set "queryType" to "semantic" or include a nonempty "semanticQuery" property in the request. [Semantic ranking](semantic-search-overview.md) is required for query rewriting.
     - We set "queryRewrites" to "generative|count-5" to get up to five query rewrites. You can set the count to any value between 1 and 10. 
-    - We set "queryLanguage" to the target language ("en-US") of the query rewrites. The supported locales are: 
+    - Since we requested query rewrites by setting the "queryRewrites" property, we must set "queryLanguage" to the search text language. The Search service uses the same language for the query rewrites. In this example, we use "en-US". The supported locales are: 
         `en-AU`, `en-CA`, `en-GB`, `en-IN`, `en-US`, `ar-EG`, `ar-JO`, `ar-KW`, `ar-MA`, `ar-SA`, `bg-BG`, `bn-IN`, `ca-ES`, `cs-CZ`, `da-DK`, `de-DE`, `el-GR`, `es-ES`, `es-MX`, `et-EE`, `eu-ES`, `fa-AE`, `fi-FI`, `fr-CA`, `fr-FR`, `ga-IE`, `gl-ES`, `gu-IN`, `he-IL`, `hi-IN`, `hr-BA`, `hr-HR`, `hu-HU`, `hy-AM`, `id-ID`, `is-IS`, `it-IT`, `ja-JP`, `kn-IN`, `ko-KR`, `lt-LT`, `lv-LV`, `ml-IN`, `mr-IN`, `ms-BN`, `ms-MY`, `nb-NO`, `nl-BE`, `nl-NL`, `no-NO`, `pa-IN`, `pl-PL`, `pt-BR`, `pt-PT`, `ro-RO`, `ru-RU`, `sk-SK`, `sl-SL`, `sr-BA`, `sr-ME`, `sr-RS`, `sv-SE`, `ta-IN`, `te-IN`, `th-TH`, `tr-TR`, `uk-UA`, `ur-PK`, `vi-VN`, `zh-CN`, `zh-TW`.
     - We set "debug" to "queryRewrites" to get the query rewrites in the response. 
   
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリリライトに関する文書の更新"
}
```

### Explanation
この変更は、Azureのセマンティッククエリリライトに関する文書の小規模な更新を示しています。主な修正点は以下の通りです：

1. **内容の変更**:
   - クエリリライトのリクエストに関して、「queryLanguage」の設定が修正されました。元の文では、クエリリライトのターゲット言語を「en-US」として単純に指定していた部分が、具体的に「検索テキスト言語」に基づいて設定する必要があることが強調されました。これにより、検索サービスはリクエストされた言語を利用してクエリリライトを行うことが明示されています。

この修正により、読者はクエリリライトを効果的に使用するために必要な言語設定に関する重要な情報を理解しやすくなっています。

## articles/search/vector-search-how-to-storage-options.md{#item-ee1680}

<details>
<summary>Diff</summary>
````diff
@@ -20,21 +20,21 @@ Azure AI Search stores multiple copies of vector fields that are used in specifi
 
 ## How vector fields are stored
 
-For every vector field, there are three copies of the vectors:
+For every vector field, there could be three copies of the vectors, each serving a different purpose:
 
-| Instance | Usage |
-|----------|-------|
-| Source vectors (in JSON) as received from an embedding model or push request to the index | Used for incremental data refresh, and if you want "retrievable" vectors returned in the query response. |
-| Original full-precision vectors | Unavailable or unsupported if vectors are uncompressed. Otherwise it's used for optional rescoring if query results obtained over compressed vectors. Rescoring applies only if vector fields undergo [scalar or binary quantization](vector-search-how-to-quantization.md). |
-| Vectors in the [HNSW graph for Approximate Nearest Neighbors (ANN) search](vector-search-overview.md) | Used for query execution. |
+| Instance | Usage | Controlled using |
+|----------|-------|------------|
+| Source vectors which store the JSON that was received during document indexing | Used for incremental data refresh with `merge` or `mergeOrUpload` during document indexing. Also used if you want "retrievable" vectors returned in the query response. | `stored` property on vector fields |
+| Original full-precision vectors | In existing indexes, these are used for internal index operations and for exhaustive KNN search. For vectors using compression, it's also used for rescoring (if enabled) on an oversampled candidate set of results from ANN search on vector fields using [scalar or binary quantization](vector-search-how-to-quantization.md) compression. | `rescoringOptions.rescoreStorageMethod` property in `vectorSearch.compressions`. For *uncompressed* vector fields on indexes created with `2024-11-01-Preview` API versions and later, this will be omitted by default with no impact on search activities nor quality. |
+| Vectors in the [HNSW graph for Approximate Nearest Neighbors (ANN) search](vector-search-overview.md) | Used for ANN query execution. Consists of either full-precision vectors (when no compression is applied) or quantized vectors (when compression is applied) | Only applies to HNSW. These data structures are required for efficient ANN search. |
 
 You can set properties that permanently discard the first two instances from vector storage.
 
-The last instance (vectors and graph) is required for ANN vector query execution. Lossy compression techniques like [scalar or binary quantization](vector-search-how-to-quantization.md) are applied to this vector instance. If you want to offset lossy compression, you should keep the second instance for rescoring purposes.
+The last instance (vectors and graph) is required for ANN vector query execution. If any compression techniques such as [scalar or binary quantization](vector-search-how-to-quantization.md) are used, they would be applied to this set of data. If you want to offset lossy compression, you should keep the second instance for rescoring purposes to improve ANN search quality.
 
 ## Set the `stored` property
 
-The `stored` property is a boolean on a vector field definition that determines whether storage is allocated for retrievable vector field content (the source instance). The `stored` property is true by default. If you don't need raw vector content in a query response, you can save up to 50 percent storage per field by changing `stored` to false.
+The `stored` property is a boolean property on a vector field definition that determines whether storage is allocated for retrievable vector field content (the source instance). The `stored` property is true by default. If you don't need raw vector content in a query response, you can save up to 50 percent storage per field by changing `stored` to false.
 
 Considerations for setting `stored` to false:
 
@@ -43,7 +43,7 @@ Considerations for setting `stored` to false:
 - However, if your indexing strategy includes [partial document updates](search-howto-reindex.md#update-content), such as "merge" or "mergeOrUpload" on an existing document, setting `stored=false` prevents content updates to those fields during the merge. On each "merge" or "mergeOrUpload" operation to a search document, you must provide the vector fields in its entirety, along with the nonvector fields that you're updating, or the vector is dropped.
 
 > [!IMPORTANT]
-> Setting the `stored=false` attribution is irreversible. It's set during index creation on vector fields when physical data structures are created. If you want retrievable vector content later, you must drop and rebuild the index, or create and load a new field that has the new attribution.
+> Setting the `stored=false` attribution is irreversible. This property can only be set when you create the index and is only allowed on vector fields. Updating an existing index with new vector fields cannot set this property to `false`. If you want retrievable vector content later, you must drop and rebuild the index, or create and load a new field that has the new attribution.
 
 For new vector fields in a search index, set `stored` to false to permanently remove retrievable storage for the vector field. The following example shows a vector field definition with the `stored` property.
 
@@ -81,9 +81,16 @@ PUT https://[service-name].search.windows.net/indexes/demo-index?api-version=202
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-The `rescoreStorageMethod` property on a vector field definition determines whether storage is allocated for original full-precision vectors. The `rescoreStorageMethod` property is set to `preserveOriginals` by default. If you aren't using the [oversampling and rescoring mitigations](vector-search-how-to-quantization.md#add-compressions-to-a-search-index) provided for querying compressed vectors, you can save on vector storage by changing `rescoreStorageMethod` to `discardOriginals`.
+The `rescoreStorageMethod` property controls the storage of full-precision vectors when compression is used.
 
-If you intend to use scalar or binary quantization, we recommend retaining `rescoreStorageMethod` set to `preserveOriginals`.
+For *uncompressed* vector fields on indexes created with `2024-11-01-Preview` API versions and later, this will be omitted by default with no impact on search activities nor quality. For existing vector fields created prior to this API version, there is no in-place ability to remove this copy of data.
+
+On a vector compression, the `rescoreStorageMethod` property is set to `preserveOriginals` by default, which retains full-precision vectors for[oversampling and rescoring capabilities](vector-search-how-to-quantization.md#add-compressions-to-a-search-index) to reduce the effect of lossy compression on the HNSW graph. If you don't use these capabilities, you can reduce vector storage by setting `rescoreStorageMethod` to `discardOriginals`.
+
+> [!IMPORTANT]
+> Setting the `rescoreStorageMethod` property is irreversible and will have different levels of search quality loss depending on the compression method. This can be set on indexes created with `2024-11-01-Preview` or later, either during index creation or adding new vector fields.
+
+If you intend to use scalar or binary quantization, we recommend retaining `rescoreStorageMethod` set to `preserveOriginals` to maximize search quality.
 
 To set this property:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のストレージオプションに関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるベクトル検索のストレージオプションに関する文書の小規模な更新を示しています。主な修正点は以下の通りです：

1. **内容の明確化**: ベクトルフィールドがどのように保存されるかについての説明が改善され、各ベクトルのコピーが異なる目的で使用されることが新たに明記されました。また、ストレージの設定やそれに関連するプロパティの使用法がより具体的に説明されています。

2. **新しい構文**:
   - ソースベクトルがどのように使用されるかや、オリジナルのフルプレシジョンベクトルの利用方法についての情報が強化され、特定のプロパティ（例: `stored` や `rescoreStorageMethod`）を介して制御する方法が示されています。

3. **重要な警告の追加**: プロパティの設定が不可逆であることや、新しいベクトルフィールドを追加する際の制約についての説明がより明確にされています。

これらの修正により、ユーザーはベクトルストレージオプションをより効果的に利用できるようになり、関連するリソースを適切に管理する手助けとなります。


