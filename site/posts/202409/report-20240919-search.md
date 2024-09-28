---
date: '2024-09-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:78943fc...MicrosoftDocs:e496207
summary: このパッチでは、Azure Cognitive Searchに関するドキュメントのAPIリンクが全面的に更新され、エンドポイントのリンクが最新のAPI仕様に合わせて修正され、文書の整合性と正確性が向上しました。また、文書内の画像ファイルには軽微な修正が施されていますが、目立った変更ではありません。特に、「search-howto-move-across-regions.md」においては重要な情報が削減され、サービス移動に関する詳細な手順が削除されています。全体として、この更新は主に既存のドキュメントを最新のAPI仕様に適合させることで、開発者が正確な情報をもとに作業できる環境を提供します。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:78943fc...MicrosoftDocs:e496207){target="_blank"}

# Highlights
この一連のパッチでは、Azure Cognitive Searchに関連するドキュメントのAPIリンクが全面的に更新されました。主にエンドポイントのリンクが最新のAPI仕様に合わせて修正され、文書の整合性と正確性が向上しています。また、画像ファイルの軽微な修正も含まれていますが、目立った変更ではありません。

## 新機能

## 重大な変更
- 「search-howto-move-across-regions.md」に大幅な削減：Azure地域間のサービス移動に関する詳細な手順が削除されました。

## その他の更新
- ほとんどの変更はAPIエンドポイントの更新であり、新しいエンドポイントに合わせたリンク修正や説明の調整が行われています。

# Insights
このパッチは、Azure Cognitive Searchに関するドキュメント群の精度と最新性を保つための重要な更新です。以下にここでの変更の意図とその影響について説明します。

## APIエンドポイントの更新
ほとんどのドキュメントはAPIエンドポイントの更新に焦点を当てています。多くのリンクが、新しいREST APIの構造に合わせて変更されました。例えば、「Create Index」のリンクは従来の`/rest/api/searchservice/create-index`から新しい`/rest/api/searchservice/indexes/create`に変更されています。この変更は、最新のAPI仕様に合致させるためのもので、開発者が正確な情報をもとに実装できるようになります。

## 画像ファイルの修正
複数の画像ファイルが「modified」とされていますが、具体的な追加、削除、変更は報告されていません。これは、画像のメタデータや管理に関する軽微な更新と考えられます。

## 重大な削減
「search-howto-move-across-regions.md」における大幅削減は、ユーザーに詳細な手順が提供されなくなるため、これから地域間移行を行う開発者には影響が大きいです。ただし、これが他の文書に統合されている可能性もあるため、追加情報が必要です。

全体として、このパッチは主に既存のドキュメントを現行のAPI仕様に合わせるためのものであり、ユーザーの体験を向上させるためのものです。APIの正確なリンクを提供することで、開発者は間違った情報に基づいて作業するリスクが減り、効率的に仕事を進めることができます。また、今後の変更への対応も容易になります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | コグニティブ サービスにアタッチする際のエンドポイントの変更 | modified | 2 | 2 | 4 | 
| [cognitive-search-common-errors-warnings.md](#item-a5c854) | minor update | 一般的なエラーと警告のドキュメント更新 | modified | 2 | 2 | 4 | 
| [cognitive-search-concept-image-scenarios.md](#item-606953) | minor update | 画像シナリオに関するドキュメントのAPIエンドポイントの更新 | modified | 2 | 2 | 4 | 
| [cognitive-search-incremental-indexing-conceptual.md](#item-7bafcc) | minor update | インクリメンタル インデキシングに関するドキュメントのAPIエンドポイントの更新 | modified | 1 | 1 | 2 | 
| [cognitive-search-skill-deprecated.md](#item-4e6309) | minor update | 非推奨スキルに関するドキュメントのAPIエンドポイントの更新 | modified | 3 | 3 | 6 | 
| [cognitive-search-tutorial-blob-dotnet.md](#item-ba889d) | minor update | コグニティブ サーチチュートリアルのAPIエンドポイントの更新 | modified | 1 | 1 | 2 | 
| [cognitive-search-tutorial-blob.md](#item-ff148f) | minor update | コグニティブ サーチチュートリアルのAPIエンドポイントの更新 | modified | 2 | 2 | 4 | 
| [javascript.md](#item-85ec57) | minor update | JavaScriptクイックスタートのインデックス作成リンクの更新 | modified | 1 | 1 | 2 | 
| [typescript.md](#item-cded25) | minor update | TypeScriptクイックスタートのインデックス作成リンクの更新 | modified | 1 | 1 | 2 | 
| [index-add-custom-analyzers.md](#item-11325e) | minor update | カスタムアナライザーに関するリンクの更新 | modified | 3 | 3 | 6 | 
| [index-add-language-analyzers.md](#item-004ac0) | minor update | 言語アナライザーに関するリンクの更新 | modified | 3 | 3 | 6 | 
| [index-add-scoring-profiles.md](#item-bf4f02) | minor update | スコアリングプロファイルに関するリンクの更新 | modified | 3 | 3 | 6 | 
| [index-add-suggesters.md](#item-28ed57) | minor update | サジェスターに関するリンクの更新 | modified | 4 | 4 | 8 | 
| [index-ranking-similarity.md](#item-ba07fa) | minor update | BM25 パラメータ設定のリンク更新 | modified | 3 | 3 | 6 | 
| [knowledge-store-create-rest.md](#item-2643dd) | minor update | インデックス作成のリンク更新 | modified | 1 | 1 | 2 | 
| [knowledge-store-projection-overview.md](#item-81aa4a) | minor update | スキルセット更新のリンク修正 | modified | 1 | 1 | 2 | 
| [knowledge-store-projections-examples.md](#item-9bfff5) | minor update | スキルセットとインデクサーランのリンク修正 | modified | 2 | 2 | 4 | 
| [function-uri.png](#item-ad9e7f) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [create-index-no-data.png](#item-72216f) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [aad-app-authentication-configuration.png](#item-56d8b1) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [access-control-add-role-assignment.png](#item-baa746) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [exception.png](#item-be28c5) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [private-endpoint-link.png](#item-d04198) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [search-service-portal.png](#item-a02d68) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [storage-firewall-ip.png](#item-a8423b) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [storage-privateendpoint-after-approval.png](#item-dd6f81) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [storage-privateendpoint-approval.png](#item-eb9921) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [test-system-identity.png](#item-7a7123) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [connect-with-visual-studio.png](#item-91286e) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [deployment-details.png](#item-e7b137) | minor update | 画像ファイルの修正 | modified | 0 | 0 | 0 | 
| [monitor-azure-cognitive-search-data-reference.md](#item-561425) | minor update | Markdownファイルの内容修正 | modified | 2 | 2 | 4 | 
| [query-lucene-syntax.md](#item-736436) | minor update | Lucene構文ドキュメントの修正 | modified | 2 | 2 | 4 | 
| [query-odata-filter-orderby-syntax.md](#item-6ab74f) | minor update | ODataフィルターおよびソート構文の文書更新 | modified | 7 | 7 | 14 | 
| [query-simple-syntax.md](#item-ab3c96) | minor update | 簡易検索構文に関する文書更新 | modified | 2 | 2 | 4 | 
| [reference-stopwords.md](#item-63e4b3) | minor update | ストップワード参照文書の更新 | modified | 1 | 1 | 2 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | 情報検索とLLMの統合に関する文書の更新 | modified | 1 | 1 | 2 | 
| [samples-javascript.md](#item-82e67e) | minor update | JavaScriptサンプル文書のリンク修正 | modified | 2 | 2 | 4 | 
| [samples-python.md](#item-d2bf09) | minor update | Pythonサンプル文書のリンク修正 | modified | 1 | 1 | 2 | 
| [search-add-autocomplete-suggestions.md](#item-0a43e0) | minor update | 自動補完および提案APIのリンク修正 | modified | 4 | 4 | 8 | 
| [search-analyzers.md](#item-9dccd9) | minor update | 検索アナライザーに関するリンク修正 | modified | 5 | 5 | 10 | 
| [search-filters.md](#item-3f2a7a) | minor update | フィルタリングに関するリンク修正 | modified | 1 | 1 | 2 | 
| [search-get-started-powershell.md](#item-4435d0) | minor update | PowerShellでの検索開始に関するリンク修正 | modified | 2 | 2 | 4 | 
| [search-get-started-rag.md](#item-05ff0e) | minor update | RAGの開始に関する手順の修正 | modified | 2 | 2 | 4 | 
| [search-get-started-rest.md](#item-0df9d5) | minor update | REST APIリンクの修正 | modified | 2 | 2 | 4 | 
| [search-get-started-vector.md](#item-4984d9) | minor update | ベクトルインデックス作成リンクの修正 | modified | 1 | 1 | 2 | 
| [search-how-to-index-onelake-files.md](#item-95f3db) | minor update | OneLakeファイルのインデックス作成リンクの修正 | modified | 1 | 1 | 2 | 
| [search-howto-complex-data-types.md](#item-75a002) | minor update | 複雑なデータ型に関するインデックス作成リンクの修正 | modified | 4 | 4 | 8 | 
| [search-howto-connecting-azure-sql-database-to-azure-search-using-indexers.md](#item-0033f1) | minor update | Azure SQL DatabaseとAzure Searchの接続に関するリンク修正 | modified | 3 | 3 | 6 | 
| [search-howto-create-indexers.md](#item-122450) | minor update | インデクサーに関するAPIリンクの修正 | modified | 3 | 3 | 6 | 
| [search-howto-dotnet-sdk.md](#item-1ad98a) | minor update | Azure AI Searchインデックスに関するAPIリンク修正 | modified | 1 | 1 | 2 | 
| [search-howto-incremental-index.md](#item-d98619) | minor update | インクリメンタルインデックスのプレビューAPIに関する表現の修正 | modified | 1 | 1 | 2 | 
| [search-howto-index-azure-data-lake-storage.md](#item-c21e43) | minor update | Azure Blobストレージのインデックス設定に関するAPIリンクの修正 | modified | 2 | 2 | 4 | 
| [search-howto-index-changed-deleted-blobs.md](#item-32a688) | minor update | 変更された削除済みBlobのインデックス手順におけるAPIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-howto-index-cosmosdb.md](#item-568fab) | minor update | Azure Cosmos DBのインデックス設定に関するAPIリンクの修正 | modified | 2 | 2 | 4 | 
| [search-howto-indexing-azure-tables.md](#item-7655b0) | minor update | Azure Tablesのインデックス設定に関するAPIリンクの修正 | modified | 3 | 3 | 6 | 
| [search-howto-move-across-regions.md](#item-bcecf6) | breaking change | Azure地域間移動ガイドの内容大幅削除 | modified | 1 | 129 | 130 | 
| [search-howto-powerapps.md](#item-92d1c0) | minor update | Power AppsにおけるAzure AI Searchインデックスのクエリ方法に関する文書の更新 | modified | 2 | 2 | 4 | 
| [search-howto-reindex.md](#item-46738a) | minor update | Reindexingに関する手順およびリンクの更新 | modified | 2 | 2 | 4 | 
| [search-import-data-portal.md](#item-b804d1) | minor update | データポータルのインポートに関するリンクの更新 | modified | 1 | 1 | 2 | 
| [search-index-azure-sql-managed-instance-with-managed-identity.md](#item-a4ec86) | minor update | インデックス作成に関するAPIエンドポイントのリンク更新 | modified | 1 | 1 | 2 | 
| [search-indexer-how-to-access-private-sql.md](#item-1bd4cc) | minor update | インデクサのステータスAPIエンドポイントのリンク更新 | modified | 1 | 1 | 2 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | インデクサのステータスおよび関連APIリンクの更新 | modified | 2 | 2 | 4 | 
| [search-indexer-overview.md](#item-292796) | minor update | インデクサステータスAPIのリンク更新 | modified | 1 | 1 | 2 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | ベクトルクォータとパーティション制限に関する情報の更新 | modified | 22 | 22 | 44 | 
| [search-lucene-query-architecture.md](#item-b0d568) | minor update | Analyze APIのリンク更新 | modified | 1 | 1 | 2 | 
| [search-normalizers.md](#item-4477d9) | minor update | インデックス作成時のリンク更新 | modified | 5 | 5 | 10 | 
| [search-performance-tips.md](#item-218e77) | minor update | 検索パフォーマンスのTipsのリンク更新 | modified | 1 | 1 | 2 | 
| [search-query-create.md](#item-532822) | minor update | APIエンドポイントのリンク更新 | modified | 3 | 3 | 6 | 
| [search-query-lucene-examples.md](#item-ce3624) | minor update | Lucene例のリンク更新 | modified | 1 | 1 | 2 | 
| [search-query-odata-full-text-search-functions.md](#item-5748d4) | minor update | Suggest APIリンクの更新 | modified | 1 | 1 | 2 | 
| [search-query-overview.md](#item-dcd5d6) | minor update | REST APIリンクの更新 | modified | 2 | 2 | 4 | 
| [search-query-partial-matching.md](#item-bd97dc) | minor update | REST APIリンクの修正 | modified | 5 | 5 | 10 | 
| [search-query-simple-examples.md](#item-834766) | minor update | テキスト解析APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-reliability.md](#item-3e9b1a) | minor update | REST APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-semi-structured-data.md](#item-d3388d) | minor update | REST APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-sku-tier.md](#item-7686b8) | minor update | サービス制限リンクの修正と新しい地域の追加 | modified | 2 | 1 | 3 | 
| [search-synapseml-cognitive-services.md](#item-dcc36f) | minor update | REST APIリンクの修正 | modified | 1 | 1 | 2 | 
| [search-synonyms.md](#item-2d5d63) | minor update | REST APIリンクの更新 | modified | 2 | 2 | 4 | 
| [search-what-is-an-index.md](#item-5a3344) | minor update | REST APIリンクの修正 | modified | 4 | 4 | 8 | 
| [search-what-is-azure-search.md](#item-93853a) | minor update | REST APIリンクの更新 | modified | 1 | 1 | 2 | 
| [search-what-is-data-import.md](#item-d73ef5) | minor update | REST APIリンクの修正 | modified | 1 | 1 | 2 | 
| [semantic-answers.md](#item-c3fee9) | minor update | REST APIリンクの変更 | modified | 1 | 1 | 2 | 
| [tutorial-optimize-indexing-push-api.md](#item-ef0e96) | minor update | REST APIリンクの更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -133,9 +133,9 @@ Enrichments are billable operations. If you no longer need to call Azure AI serv
 
 ### [**REST**](#tab/cogkey-rest-remove)
 
-1. [Get Skillset](/rest/api/searchservice/get-skillset) so that you have the full definition.
+1. [Get Skillset](/rest/api/searchservice/skillsets/get) so that you have the full definition.
 
-1. Formulate an [Update Skillset](/rest/api/searchservice/update-skillset) request, providing the JSON definition of the skillset.
+1. Formulate an [Update Skillset](/rest/api/searchservice/skillsets/create-or-update) request, providing the JSON definition of the skillset.
 
 1. Remove the key in the body of the definition, and then send the request:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブ サービスにアタッチする際のエンドポイントの変更"
}
```

### Explanation
この変更は、コグニティブ サービスに関連するドキュメントのエンドポイントを更新しました。具体的には、Skillsetに関するAPIエンドポイントのリンクが修正され、より正確な情報が提供されるようになりました。具体的には、「Get Skillset」および「Update Skillset」で使用されるリンクが、新しいルートに合わせて更新されました。この更新は、開発者が最新のAPI仕様に基づいて作業できるようにするためのもので、文書の整合性を高めることを目的としています。

## articles/search/cognitive-search-common-errors-warnings.md{#item-a5c854}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ Indexing stops when the error count exceeds ['maxFailedItems'](cognitive-search-
 If you want indexers to ignore these errors (and skip over "failed documents"), consider updating the `maxFailedItems` and `maxFailedItemsPerBatch` as described [here](/rest/api/searchservice/indexers/create#indexingparameters).
 
 > [!NOTE]
-> Each failed document along with its document key (when available) will show up as an error in the indexer execution status. You can utilize the [index api](/rest/api/searchservice/addupdate-or-delete-documents) to manually upload the documents at a later point if you have set the indexer to tolerate failures.
+> Each failed document along with its document key (when available) will show up as an error in the indexer execution status. You can utilize the [index api](/rest/api/searchservice/documents) to manually upload the documents at a later point if you have set the indexer to tolerate failures.
 
 The error information in this article can help you resolve errors, allowing indexing to continue.
 
@@ -92,7 +92,7 @@ Indexer read the document from the data source, but there was an issue convertin
 
 | Reason | Details/Example | Resolution |
 | --- | --- | --- |
-| The document key is missing | `Document key cannot be missing or empty` | Ensure all documents have valid document keys. The document key is determined by setting the 'key' property as part of the [index definition](/rest/api/searchservice/create-index#request-body). Indexers emit this error when the property flagged as the 'key' can't be found on a particular document. |
+| The document key is missing | `Document key cannot be missing or empty` | Ensure all documents have valid document keys. The document key is determined by setting the 'key' property as part of the [index definition](/rest/api/searchservice/indexes/create#request-body). Indexers emit this error when the property flagged as the 'key' can't be found on a particular document. |
 | The document key is invalid | `Invalid document key. Keys can only contain letters, digits, underscore (_), dash (-), or equal sign (=). ` | Ensure all documents have valid document keys. Review [Indexing Blob Storage](search-howto-indexing-azure-blob-storage.md) for more details. If you're using the blob indexer, and your document key is the `metadata_storage_path` field, make sure that the indexer definition has a [base64Encode mapping function](search-indexer-field-mappings.md?tabs=rest#base64encode-function) with `parameters` equal to `null`, instead of the path in plain text. |
 | The document key is invalid | `Document key cannot be longer than 1024 characters` | Modify the document key to meet the validation requirements. |
 | Could not apply field mapping to a field | `Could not apply mapping function 'functionName' to field 'fieldName'. Array cannot be null. Parameter name: bytes` | Double check the [field mappings](search-indexer-field-mappings.md) defined on the indexer, and compare with the data of the specified field of the failed document. It might be necessary to modify the field mappings or the document data. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "一般的なエラーと警告のドキュメント更新"
}
```

### Explanation
この変更では、コグニティブ サーチに関する一般的なエラーと警告に関する文書が更新されました。具体的には、いくつかのAPIへのリンクが正確な情報に修正されました。例えば、失敗したドキュメントのアップロード用の「index api」のリンクが、新しい適切なエンドポイントに合わせて更新されました。また、ドキュメントキーに関するエラーの詳細が、より正確なAPIリファレンスに基づくように修正されました。これにより、ユーザーはエラー解決のための手順をより明確に理解できるようになります。全体として、より良い明確性と正確性を提供することを目的としたマイナーな更新です。

## articles/search/cognitive-search-concept-image-scenarios.md{#item-606953}

<details>
<summary>Diff</summary>
````diff
@@ -224,7 +224,7 @@ In a skillset, Image Analysis and OCR skill output is always text. Output text i
     }
     ```
 
-1. [Create or update a search index](/rest/api/searchservice/create-index) to add fields to accept the skill outputs. 
+1. [Create or update a search index](/rest/api/searchservice/indexes/create) to add fields to accept the skill outputs. 
 
    In the following fields collection example, "content" is blob content. "Metadata_storage_name" contains the name of the file (make sure it is "retrievable"). "Metadata_storage_path" is the unique path of the blob and is the default document key. "Merged_content" is output from Text Merge (useful when images are embedded). 
 
@@ -282,7 +282,7 @@ In a skillset, Image Analysis and OCR skill output is always text. Output text i
       ],
     ```
 
-1. [Update the indexer](/rest/api/searchservice/update-indexer) to map skillset output (nodes in an enrichment tree) to index fields.
+1. [Update the indexer](/rest/api/searchservice/indexers/create-or-update) to map skillset output (nodes in an enrichment tree) to index fields.
 
    Enriched documents are internal. To externalize the nodes in an enriched document tree, set up an output field mapping that specifies which index field receives node content. Enriched data is accessed by your app through an index field. The following example shows a "text" node (OCR output) in an enriched document that's mapped to a "text" field in a search index.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像シナリオに関するドキュメントのAPIエンドポイントの更新"
}
```

### Explanation
この変更は、コグニティブ サーチに関連する画像シナリオに関するドキュメントのAPIエンドポイントを更新しました。具体的には、検索インデックスを作成または更新する際のリンクが更新されています。「Create or update a search index」というエンドポイントが新しい「indexes/create」というエンドポイントに修正され、「Update the indexer」というエンドポイントも「indexers/create-or-update」に変更されています。これにより、利用者は最新のAPI仕様を反映した正確な情報を得ることができ、スキル出力を適切にマッピングする手順が明確になります。全体として、ドキュメントの正確性と使いやすさを向上させるためのマイナーな更新です。

## articles/search/cognitive-search-incremental-indexing-conceptual.md{#item-7bafcc}

<details>
<summary>Diff</summary>
````diff
@@ -83,7 +83,7 @@ Modifying a skill and reprocessing of that skill typically go hand in hand. Howe
 
 If you know that a change to the skill is indeed superficial, you should override skill evaluation by setting the `disableCacheReprocessingChangeDetection` parameter to true:
 
-1. Call [Update Skillset](/rest/api/searchservice/update-skillset) and modify the skillset definition.
+1. Call [Update Skillset](/rest/api/searchservice/skillsets/create-or-update) and modify the skillset definition.
 1. Append the "disableCacheReprocessingChangeDetection=true" parameter on the request.
 1. Submit the change.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インクリメンタル インデキシングに関するドキュメントのAPIエンドポイントの更新"
}
```

### Explanation
この変更では、インクリメンタル インデキシングに関するドキュメントのAPIエンドポイントが更新されました。具体的には、スキルセットを更新する際に使用するエンドポイントが、古い「Update Skillset」から新しい「skillsets/create-or-update」に修正されました。この変更によって、ユーザーは最新のAPI構造に合わせた正確な情報を得ることができ、スキルの評価をオーバーライドするための手順が明確に示されています。全体として、ドキュメントの正確性と使いやすさを向上させるためのマイナーな更新です。

## articles/search/cognitive-search-skill-deprecated.md{#item-4e6309}

<details>
<summary>Diff</summary>
````diff
@@ -40,7 +40,7 @@ August 31, 2024
 
 Use [Microsoft.Skills.Text.V3.EntityRecognitionSkill](cognitive-search-skill-entity-recognition-v3.md) instead. It provides most of the functionality of the EntityRecognitionSkill at a higher quality. It also has richer information in its complex output fields.
 
-To migrate to the [Microsoft.Skills.Text.V3.EntityRecognitionSkill](cognitive-search-skill-entity-recognition-v3.md), make one or more of the following changes to your skill definition. You can update the skill definition using the [Update Skillset API](/rest/api/searchservice/update-skillset).
+To migrate to the [Microsoft.Skills.Text.V3.EntityRecognitionSkill](cognitive-search-skill-entity-recognition-v3.md), make one or more of the following changes to your skill definition. You can update the skill definition using the [Update Skillset API](/rest/api/searchservice/skillsets/create-or-update).
 
 1. *(Required)* Change the `@odata.type` from `"#Microsoft.Skills.Text.EntityRecognitionSkill"` to `"#Microsoft.Skills.Text.V3.EntityRecognitionSkill"`.
 
@@ -368,7 +368,7 @@ August 31, 2024
 
 Use [Microsoft.Skills.Text.V3.SentimentSkill](cognitive-search-skill-sentiment-v3.md) instead. It provides an improved model and includes the option to add opinion mining or aspect-based sentiment. As the skill is significantly more complex, the outputs are also very different.
 
-To migrate to the [Microsoft.Skills.Text.V3.SentimentSkill](cognitive-search-skill-sentiment-v3.md), make one or more of the following changes to your skill definition. You can update the skill definition using the [Update Skillset API](/rest/api/searchservice/update-skillset).
+To migrate to the [Microsoft.Skills.Text.V3.SentimentSkill](cognitive-search-skill-sentiment-v3.md), make one or more of the following changes to your skill definition. You can update the skill definition using the [Update Skillset API](/rest/api/searchservice/skillsets/create-or-update).
 
 > [!NOTE]
 > The skill outputs for the Sentiment Skill V3 are not compatible with the index definition based on the SentimentSkill. You will have to make changes to the index definition, skillset (later skill inputs and/or knowledge store projections) and indexer output field mappings to replace the sentiment skill with the new version.
@@ -396,7 +396,7 @@ August 31, 2024
 
 Use [Microsoft.Skills.Text.V3.EntityRecognitionSkill](cognitive-search-skill-entity-recognition-v3.md) instead. It provides most of the functionality of the NamedEntityRecognitionSkill at a higher quality. It also has richer information in its complex output fields.
 
-To migrate to the [Microsoft.Skills.Text.V3.EntityRecognitionSkill](cognitive-search-skill-entity-recognition-v3.md), make one or more of the following changes to your skill definition. You can update the skill definition using the [Update Skillset API](/rest/api/searchservice/update-skillset).
+To migrate to the [Microsoft.Skills.Text.V3.EntityRecognitionSkill](cognitive-search-skill-entity-recognition-v3.md), make one or more of the following changes to your skill definition. You can update the skill definition using the [Update Skillset API](/rest/api/searchservice/skillsets/create-or-update).
 
 1. *(Required)* Change the `@odata.type` from `"#Microsoft.Skills.Text.NamedEntityRecognitionSkill"` to `"#Microsoft.Skills.Text.V3.EntityRecognitionSkill"`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "非推奨スキルに関するドキュメントのAPIエンドポイントの更新"
}
```

### Explanation
この変更は、非推奨のコグニティブ スキルに関するドキュメント内のAPIエンドポイントを更新しました。具体的には、スキル定義を更新するためのエンドポイントが「Update Skillset」から新しい「skillsets/create-or-update」に修正されています。この変更により、ユーザーは新しいエンドポイントを使用してスキルを適切に移行できる情報を得ることができ、エンティティ認識スキルおよび感情スキルへの移行手順が最新のAPI仕様に沿ったものとなります。全体として、ドキュメントの内容はより明確で実用的になり、利用者の利便性を向上させるマイナーな更新です。

## articles/search/cognitive-search-tutorial-blob-dotnet.md{#item-ba889d}

<details>
<summary>Diff</summary>
````diff
@@ -630,7 +630,7 @@ Add the following using statement to resolve the disambiguated reference.
 using Index = Azure.Search.Documents.Indexes.Models;
 ```
 
-To learn more about index concepts, see [Create Index (REST API)](/rest/api/searchservice/create-index).
+To learn more about index concepts, see [Create Index (REST API)](/rest/api/searchservice/indexes/create).
 
 ### Step 4: Create and run an indexer
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブ サーチチュートリアルのAPIエンドポイントの更新"
}
```

### Explanation
この変更では、コグニティブ サーチに関するチュートリアル文書の一部におけるAPIエンドポイントが修正されました。具体的には、インデックスに関する概念を学ぶためのリンクが「Create Index (REST API)」から新しい「indexes/create」に変更されています。この修正により、読者は最新のAPIエンドポイントに直接アクセスできるようになり、より正確で効率的に情報を得ることができます。全体として、この更新はドキュメントの正確性と利用価値を向上させるためのマイナーな改良です。

## articles/search/cognitive-search-tutorial-blob.md{#item-ff148f}

<details>
<summary>Diff</summary>
````diff
@@ -311,7 +311,7 @@ POST {{baseUrl}}/skillsets?api-version=2024-07-01  HTTP/1.1
 
 ### Step 3: Create an index
 
-Call [Create Index](/rest/api/searchservice/create-index) to provide the schema used to create inverted indexes and other constructs in Azure AI Search. 
+Call [Create Index](/rest/api/searchservice/indexes/create) to provide the schema used to create inverted indexes and other constructs in Azure AI Search. 
 
 The largest component of an index is the fields collection, where data type and attributes determine content and behavior in Azure AI Search. Make sure you have fields for your newly generated output.
 
@@ -497,7 +497,7 @@ POST {{baseUrl}}/indexers?api-version=2024-07-01  HTTP/1.1
 
 Indexing and enrichment commence as soon as you submit the Create Indexer request. Depending on skillset complexity and operations, indexing can take a while.
 
-To find out whether the indexer is still running, call [Get Indexer Status](/rest/api/searchservice/get-indexer-status) to check the indexer status.
+To find out whether the indexer is still running, call [Get Indexer Status](/rest/api/searchservice/indexers/get-status) to check the indexer status.
 
 ```http
 ### Get Indexer Status (wait several minutes for the indexer to complete)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブ サーチチュートリアルのAPIエンドポイントの更新"
}
```

### Explanation
この変更は、コグニティブ サーチに関するチュートリアル文書のAPIエンドポイントの更新を含んでいます。具体的には、インデックス作成のためのAPIエンドポイントが「Create Index」から「indexes/create」に変更され、インデクサのステータスを確認する際のエンドポイントも「Get Indexer Status」から「indexers/get-status」に修正されています。これにより、ユーザーは最新のAPIエンドポイントに直接アクセスでき、正確な情報を得ることができるようになります。この更新は、文書の正確性とユーザー体験を改善するためのマイナーな変更です。

## articles/search/includes/quickstarts/javascript.md{#item-85ec57}

<details>
<summary>Diff</summary>
````diff
@@ -127,7 +127,7 @@ With that in place, we're ready to create an index.
 
 #### Create index 
 
-Create a file **hotels_quickstart_index.json**.  This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index.  You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/create-index). 
+Create a file **hotels_quickstart_index.json**.  This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index.  You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
 
 Add the following content to **hotels_quickstart_index.json** or [download the file](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels_quickstart_index.json). 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptクイックスタートのインデックス作成リンクの更新"
}
```

### Explanation
この変更では、JavaScriptクイックスタートに関連する文書の一部が修正されました。具体的には、インデックス作成のための設定ファイル「hotels_quickstart_index.json」に関する説明が更新され、インデックス作成に関連するリンクが「Create Index (REST)」から「indexes/create」に変更されています。この更新により、ユーザーはインデックス作成に関する最新の情報にアクセスできるようになり、Azure AI Searchのドキュメントをより正確に利用できるようになります。全体として、この変更はドキュメントの正確性とユーザー体験を向上させるためのマイナーな改良です。

## articles/search/includes/quickstarts/typescript.md{#item-cded25}

<details>
<summary>Diff</summary>
````diff
@@ -140,7 +140,7 @@ With that in place, we're ready to create an index.
 
 #### Create index 
 
-Create a file **hotels_quickstart_index.json**.  This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index.  You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/create-index). 
+Create a file **hotels_quickstart_index.json**.  This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index.  You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
 
 Add the following content to **hotels_quickstart_index.json** or [download the file](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels_quickstart_index.json). 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptクイックスタートのインデックス作成リンクの更新"
}
```

### Explanation
この変更は、TypeScriptクイックスタートに関する文書の一部を修正したもので、インデックス作成に関連する説明とリンクが更新されました。具体的には、インデックス作成のための設定ファイル「hotels_quickstart_index.json」に関する説明があり、関連するリンクが「Create Index (REST)」から「indexes/create」に修正されています。この変更により、ユーザーは最新のインデックス作成手続きについての情報に簡単にアクセスできるようになります。結果として、文書の正確性と利便性が向上し、Azure AI Searchの使用においてより良い体験を提供するためのマイナーな更新です。

## articles/search/index-add-custom-analyzers.md{#item-11325e}

<details>
<summary>Diff</summary>
````diff
@@ -128,11 +128,11 @@ Within an index definition, you can place this section anywhere in the body of a
 }
 ```
 
-The analyzer definition is a part of the larger index. Definitions for char filters, tokenizers, and token filters are added to the index only if you're setting custom options. To use an existing filter or tokenizer as-is, specify it by name in the analyzer definition. For more information, see [Create Index (REST)](/rest/api/searchservice/create-index). For more examples, see [Add analyzers in Azure AI Search](search-analyzers.md#examples).
+The analyzer definition is a part of the larger index. Definitions for char filters, tokenizers, and token filters are added to the index only if you're setting custom options. To use an existing filter or tokenizer as-is, specify it by name in the analyzer definition. For more information, see [Create Index (REST)](/rest/api/searchservice/indexes/create). For more examples, see [Add analyzers in Azure AI Search](search-analyzers.md#examples).
 
 ## Test custom analyzers
 
-You can use the [Test Analyzer (REST)](/rest/api/searchservice/test-analyzer) to see how an analyzer breaks given text into tokens.
+You can use the [Test Analyzer (REST)](/rest/api/searchservice/indexes/analyze) to see how an analyzer breaks given text into tokens.
 
 **Request**
 
@@ -310,4 +310,4 @@ In the table below, the token filters that are implemented using Apache Lucene a
 
 - [Azure AI Search REST APIs](/rest/api/searchservice/)
 - [Analyzers in Azure AI Search (Examples)](search-analyzers.md#examples)
-- [Create Index (REST)](/rest/api/searchservice/create-index)
+- [Create Index (REST)](/rest/api/searchservice/indexes/create)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムアナライザーに関するリンクの更新"
}
```

### Explanation
この変更では、「index-add-custom-analyzers.md」文書の一部が修正され、特にカスタムアナライザーに関連するリンクが更新されました。具体的には、インデックス定義におけるアナライザーの定義と、アナライザーのテストに使用されるAPIリンクが変更されています。これにより、ユーザーは最新のインデックスおよびテストアナライザーのAPIにアクセスしやすくなり、関連する情報をより正確に得ることができるようになります。この修正は、ドキュメントの正確性を向上させるためのマイナーな更新であり、Azure AI Searchの利用において利便性を向上させることを目的としています。

## articles/search/index-add-language-analyzers.md{#item-004ac0}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ A better experience is to search for individual words: 明るい (Bright), 私
 
 Azure AI Search supports 35 language analyzers backed by Lucene, and 50 language analyzers backed by proprietary Microsoft natural language processing technology used in Office and Bing.
 
-Some developers might prefer the more familiar, simple, open-source solution of Lucene. Lucene language analyzers are faster, but the Microsoft analyzers have advanced capabilities, such as lemmatization, word decompounding (in languages like German, Danish, Dutch, Swedish, Norwegian, Estonian, Finnish, Hungarian, Slovak) and entity recognition (URLs, emails, dates, numbers). If possible, you should run comparisons of both the Microsoft and Lucene analyzers to decide which one is a better fit. You can use [Analyze API](/rest/api/searchservice/test-analyzer) to see the tokens generated from a given text using a specific analyzer.
+Some developers might prefer the more familiar, simple, open-source solution of Lucene. Lucene language analyzers are faster, but the Microsoft analyzers have advanced capabilities, such as lemmatization, word decompounding (in languages like German, Danish, Dutch, Swedish, Norwegian, Estonian, Finnish, Hungarian, Slovak) and entity recognition (URLs, emails, dates, numbers). If possible, you should run comparisons of both the Microsoft and Lucene analyzers to decide which one is a better fit. You can use [Analyze API](/rest/api/searchservice/indexes/analyze) to see the tokens generated from a given text using a specific analyzer.
 
 Indexing with Microsoft analyzers is on average two to three times slower than their Lucene equivalents, depending on the language. Search performance shouldn't be significantly affected for average size queries. 
 
@@ -87,7 +87,7 @@ The following example illustrates a language analyzer specification in an index:
     },
 ```
 
-For more information about creating an index and setting field properties, see [Create Index (REST)](/rest/api/searchservice/create-index). For more information about text analysis, see [Analyzers in Azure AI Search](search-analyzers.md).
+For more information about creating an index and setting field properties, see [Create Index (REST)](/rest/api/searchservice/indexes/create). For more information about text analysis, see [Analyzers in Azure AI Search](search-analyzers.md).
 
 <a name="language-analyzer-list"></a>
 
@@ -160,5 +160,5 @@ For more information about creating an index and setting field properties, see [
 
 + [Create an index](search-what-is-an-index.md)
 + [Create a multi-language index](search-language-support.md)
-+ [Create Index (REST API)](/rest/api/searchservice/create-index)  
++ [Create Index (REST API)](/rest/api/searchservice/indexes/create)  
 + [LexicalAnalyzerName Class (Azure SDK for .NET)](/dotnet/api/azure.search.documents.indexes.models.lexicalanalyzername)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語アナライザーに関するリンクの更新"
}
```

### Explanation
この変更は、「index-add-language-analyzers.md」文書における言語アナライザーに関連する情報の一部が修正されたものです。具体的には、Microsoftの自然言語処理技術とLuceneに基づくアナライザーについての説明が含まれています。特に、アナライザーを使用して生成されるトークンを確認するためのリンクが「Analyze API」から「indexes/analyze」に更新され、より具体的な情報源にアクセスできるようになっています。また、インデックスの作成やフィールドプロパティの設定に関するリンクも同様に更新されており、最新のAPIエンドポイントに直結しています。この修正は、文書の利便性と正確性を向上させるためのマイナーな更新として位置付けられます。

## articles/search/index-add-scoring-profiles.md{#item-bf4f02}

<details>
<summary>Diff</summary>
````diff
@@ -93,7 +93,7 @@ Relevancy-based ordering in a search page is also implemented through scoring pr
 
 To implement custom scoring behavior, add a scoring profile to the schema that defines the index. You can have up to 100 scoring profiles within an index (see [Service Limits](search-limits-quotas-capacity.md)), but you can only specify one profile at time in any given query.
 
-1. Start with an index definition. You can add and update scoring profiles on an existing index without having to rebuild it. Use an [Update Index](/rest/api/searchservice/update-index) request to post your revision.
+1. Start with an index definition. You can add and update scoring profiles on an existing index without having to rebuild it. Use an [Update Index](/rest/api/searchservice/indexes/create-or-update) request to post your revision.
 
 1. Paste in the [Template](#bkmk_template) provided in this article.  
 
@@ -103,7 +103,7 @@ To implement custom scoring behavior, add a scoring profile to the schema that d
 
 You should work iteratively, using a data set that will help you prove or disprove the efficacy of a given profile.
 
-Scoring profiles can be defined in Azure portal as shown in the following screenshot, or programmatically through [REST APIs](/rest/api/searchservice/update-index) or in Azure SDKs, such as the [ScoringProfile](/dotnet/api/azure.search.documents.indexes.models.scoringprofile) class in the Azure SDK for .NET.
+Scoring profiles can be defined in Azure portal as shown in the following screenshot, or programmatically through [REST APIs](/rest/api/searchservice/indexes/create-or-update) or in Azure SDKs, such as the [ScoringProfile](/dotnet/api/azure.search.documents.indexes.models.scoringprofile) class in the Azure SDK for .NET.
 
    :::image type="content" source="media/scoring-profiles/portal-add-scoring-profile-small.png" alt-text="Add scoring profiles page" lightbox="media/scoring-profiles/portal-add-scoring-profile.png" border="true":::
 
@@ -342,6 +342,6 @@ The `boostGenre` profile uses weighted text fields, boosting matches found in al
 
 + [Relevance and scoring in Azure AI Search](index-similarity-and-scoring.md)
 + [REST API Reference](/rest/api/searchservice/)
-+ [Create Index API](/rest/api/searchservice/create-index)
++ [Create Index API](/rest/api/searchservice/indexes/create)
 + [Azure AI Search .NET SDK](/dotnet/api/overview/azure/search?)
 + [What Are Scoring Profiles?](https://social.technet.microsoft.com/wiki/contents/articles/26706.azure-search-what-are-scoring-profiles.aspx)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スコアリングプロファイルに関するリンクの更新"
}
```

### Explanation
この変更は、「index-add-scoring-profiles.md」文書におけるスコアリングプロファイル関連の内容が修正されたものです。特に、スコアリングプロファイルを実装する際の手順において、インデックスの更新に関するAPIリンクが「Update Index」から「indexes/create-or-update」に更新されました。この変更は、ユーザーがスコアリングプロファイルを定義するために必要な最新のAPI情報にアクセスできるようにするためのものです。また、文書内のその他の関連リンクも同様に更新されており、正確で最新の情報を提供することが目的とされています。この修正は、Azure AI Searchを利用する開発者にとっての利便性を向上させるためのマイナーな更新です。

## articles/search/index-add-suggesters.md{#item-28ed57}

<details>
<summary>Diff</summary>
````diff
@@ -39,7 +39,7 @@ Search-as-you-type is enabled on a per-field basis for string fields. You can im
 
 ## How to create a suggester
 
-To create a suggester, add one to an [index definition](/rest/api/searchservice/create-index). A suggester takes a name and a collection of fields over which the typeahead experience is enabled. The best time to create a suggester is when you're also defining the field that uses it.
+To create a suggester, add one to an [index definition](/rest/api/searchservice/indexes/create). A suggester takes a name and a collection of fields over which the typeahead experience is enabled. The best time to create a suggester is when you're also defining the field that uses it.
 
 + Use string fields only.
 
@@ -63,7 +63,7 @@ To satisfy both search-as-you-type experiences, add all of the fields that you n
 
 Your choice of an analyzer determines how fields are tokenized and prefixed. For example, for a hyphenated string like "context-sensitive", using a language analyzer results in these token combinations: "context", "sensitive", "context-sensitive". Had you used the standard Lucene analyzer, the hyphenated string wouldn't exist. 
 
-When evaluating analyzers, consider using the [Analyze Text API](/rest/api/searchservice/test-analyzer) for insight into how terms are processed. Once you build an index, you can try various analyzers on a string to view token output.
+When evaluating analyzers, consider using the [Analyze Text API](/rest/api/searchservice/indexes/analyze) for insight into how terms are processed. Once you build an index, you can try various analyzers on a string to view token output.
 
 Fields that use [custom analyzers](index-add-custom-analyzers.md) or [built-in analyzers](index-add-custom-analyzers.md#built-in-analyzers) (except for standard Lucene) are explicitly disallowed to prevent poor outcomes.
 
@@ -82,7 +82,7 @@ As previously noted, analyzer choice impacts tokenization and prefixing. Conside
 
 ## Create using REST
 
-In the REST API, add suggesters through [Create Index](/rest/api/searchservice/create-index) or [Update Index](/rest/api/searchservice/update-index). 
+In the REST API, add suggesters through [Create Index](/rest/api/searchservice/indexes/create) or [Update Index](/rest/api/searchservice/indexes/create-or-update). 
 
   ```json
   {
@@ -151,7 +151,7 @@ private static void CreateIndex(string indexName, SearchIndexClient indexClient)
 
 A suggester is used in a query. After a suggester is created, call one of the following APIs for a search-as-you-type experience:
 
-+ [Suggestions REST API](/rest/api/searchservice/suggestions)
++ [Suggestions REST API](/rest/api/searchservice/documents/suggest-post)
 + [Autocomplete REST API](/rest/api/searchservice/documents/autocomplete-post)
 + [SuggestAsync method](/dotnet/api/azure.search.documents.searchclient.suggestasync)
 + [AutocompleteAsync method](/dotnet/api/azure.search.documents.searchclient.autocompleteasync)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サジェスターに関するリンクの更新"
}
```

### Explanation
この変更は、「index-add-suggesters.md」文書におけるサジェスターに関する情報の更新を含んでいます。具体的には、サジェスターを作成する際の手順や関連するAPIのリンクが修正されました。サジェスターを追加するためのインデックス定義のリンクが「create-index」から「indexes/create」に変更され、より明確なリファレンスが提供されています。また、テキストの分析時に利用する「Analyze Text API」のリンクも、最新のエンドポイントである「indexes/analyze」に更新されています。これにより、ユーザーは最新のAPI情報に基づいて機能を実装しやすくなっています。さらに、REST APIを通じてサジェスターを追加する部分でもエンドポイントが更新されています。この修正は、Azure AI Searchの開発者にとっての利便性を向上させるためのマイナーな更新と見なされます。

## articles/search/index-ranking-similarity.md{#item-ba07fa}

<details>
<summary>Diff</summary>
````diff
@@ -39,7 +39,7 @@ For older services, classic similarity remains the default algorithm. Older serv
 
 BM25 ranking provides two parameters for tuning the relevance score calculation. 
 
-1. Use a [Create or Update Index](/rest/api/searchservice/create-index) request to set BM25 parameters:
+1. Use a [Create or Update Index](/rest/api/searchservice/indexes/create) request to set BM25 parameters:
 
     ```http
     PUT [service-name].search.windows.net/indexes/[index-name]?api-version=2024-07-01&allowIndexDowntime=true
@@ -80,7 +80,7 @@ The following links describe the Similarity property in the Azure SDKs.
 
 ### REST example
 
-You can also use the [REST API](/rest/api/searchservice/create-index). The following example creates a new index with the "similarity" property set to BM25:
+You can also use the [REST API](/rest/api/searchservice/indexes/create). The following example creates a new index with the "similarity" property set to BM25:
 
 ```http
 PUT [service-name].search.windows.net/indexes/[index name]?api-version=2024-07-01
@@ -111,5 +111,5 @@ PUT [service-name].search.windows.net/indexes/[index name]?api-version=2024-07-0
 + [Relevance and scoring in Azure AI Search](index-similarity-and-scoring.md)
 + [REST API Reference](/rest/api/searchservice/)
 + [Add scoring profiles to your index](index-add-scoring-profiles.md)
-+ [Create Index API](/rest/api/searchservice/create-index)
++ [Create Index API](/rest/api/searchservice/indexes/create)
 + [Azure AI Search .NET SDK](/dotnet/api/overview/azure/search)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "BM25 パラメータ設定のリンク更新"
}
```

### Explanation
この変更は、「index-ranking-similarity.md」文書におけるBM25ランキングアルゴリズムに関する情報を更新するものです。パラメータ設定に関する手順において、BM25パラメータを設定するためのリクエストのリンクが「Create or Update Index」から「indexes/create」に修正されました。この変更により、ユーザーは正確なAPIエンドポイントに基づいてBM25パラメータを設定できるようになります。また、REST APIの例においても、同様にリンクが更新されており、BM25プロパティを持つ新しいインデックスを作成するための具体的なリファレンスが強化されています。加えて、関連するリンクも整備され、利用者がAzure AI Searchの機能をより良く理解し、活用できるように配慮されています。この一連の修正により、開発者にとっての利便性が向上することが期待されます。

## articles/search/knowledge-store-create-rest.md{#item-2643dd}

<details>
<summary>Diff</summary>
````diff
@@ -68,7 +68,7 @@ A valid API key establishes trust, on a per request basis, between the applicati
 
 ## Create an index
 
-[Create Index (REST)](/rest/api/searchservice/create-index) creates  a search index on the search service. A search index is unrelated to a knowledge store, but the indexer requires one. The search index contains the same content as the knowledge store, which you can explore by sending query requests.
+[Create Index (REST)](/rest/api/searchservice/indexes/create) creates  a search index on the search service. A search index is unrelated to a knowledge store, but the indexer requires one. The search index contains the same content as the knowledge store, which you can explore by sending query requests.
 
 1. Open a new text file in Visual Studio Code.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス作成のリンク更新"
}
```

### Explanation
この変更は、「knowledge-store-create-rest.md」文書内におけるインデックス作成に関する情報を更新するものです。具体的には、REST APIを使用してインデックスを作成する際の説明文において、旧リンク「create-index」が新しいリンク「indexes/create」に修正されました。この変更により、ユーザーがインデックスを作成する際に正確なエンドポイントにアクセスできるようになります。また、文書の内容は知識ストアと検索インデックスの関係を強調し、インデックス作成に必要な情報を明確にしています。こうした修正は、開発者が最新のAPIガイドラインに従って実装を簡単に行えるようにすることを目的としています。

## articles/search/knowledge-store-projection-overview.md{#item-81aa4a}

<details>
<summary>Diff</summary>
````diff
@@ -164,7 +164,7 @@ Recall that projections are exclusive to knowledge stores, and aren't used to st
 
    1. From the skills array, determine which skill outputs should be referenced in the `source` of each projection. All projections have a source. The source can be the output of an upstream skill, but is often the output of a Shaper skill. The composition of your projection is determined through shapes. 
 
-1. If you're adding projections to an existing skillset, [update the skillset](/rest/api/searchservice/update-skillset) and [run the indexer](/rest/api/searchservice/run-indexer).
+1. If you're adding projections to an existing skillset, [update the skillset](/rest/api/searchservice/skillsets/create-or-update) and [run the indexer](/rest/api/searchservice/indexers/run).
 
 1. Check your results in Azure Storage. On subsequent runs, avoid naming collisions by deleting objects in Azure Storage or changing project names in the skillset.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スキルセット更新のリンク修正"
}
```

### Explanation
この変更は、「knowledge-store-projection-overview.md」文書の一部で、スキルセットの更新手順に関連したリンクを修正するものです。具体的には、既存のスキルセットにプロジェクションを追加する際の手順で、以前のリンク「update-skillset」が「skillsets/create-or-update」に変更されました。これにより、開発者が正しいAPIエンドポイントにアクセスしやすくなります。また、インデクサーを実行する際のリンクも「run-indexer」から「indexers/run」に修正され、より明確な情報提供がなされるようになっています。この修正は、ユーザーが最新のAPIドキュメントに基づいた正確な操作を行えるようにするためのものです。

## articles/search/knowledge-store-projections-examples.md{#item-9bfff5}

<details>
<summary>Diff</summary>
````diff
@@ -265,9 +265,9 @@ You can process projections by following these steps:
 
 1. Set the knowledge store's `storageConnectionString` property to a valid V2 general purpose storage account connection string.  
 
-1. [Update the skillset](/rest/api/searchservice/update-skillset) by issuing a PUT request with your projection definition in the body of the skillset.
+1. [Update the skillset](/rest/api/searchservice/skillsets/create-or-update) by issuing a PUT request with your projection definition in the body of the skillset.
 
-1. [Run the indexer](/rest/api/searchservice/run-indexer) to put the skillset into execution. 
+1. [Run the indexer](/rest/api/searchservice/indexers/run) to put the skillset into execution. 
 
 1. [Monitor indexer execution](search-howto-monitor-indexers.md) to check progress and catch any errors.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スキルセットとインデクサーランのリンク修正"
}
```

### Explanation
この変更は、「knowledge-store-projections-examples.md」文書内で、プロジェクションの処理手順に関するリンクを修正するものです。具体的には、スキルセットの更新に関する手順で、従来のリンク「update-skillset」が「skillsets/create-or-update」に変更されました。また、インデクサーを実行する手順のリンクも「run-indexer」から「indexers/run」に修正されました。これにより、ユーザーが正確なAPIエンドポイントを参照することができ、最新の情報に基づいてスキルセットやインデクサーを正しく操作できるようになります。こうした修正によって、APIの使用におけるユーザーの利便性が向上します。

## articles/search/media/indexing-encrypted-blob-files/function-uri.png{#item-ad9e7f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この変更は、「function-uri.png」という画像ファイルに関連して行われましたが、実際には内容の追加や削除はありませんでした。ファイルの状態が「modified」となっていますが、具体的な変更はありません。そのため、この更新は画像のメタデータや管理に関するものである可能性があります。ユーザーにとっては、ファイルが妥当性を保ちつつ、適切に整理されていることを期待できます。

## articles/search/media/search-get-started-javascript/create-index-no-data.png{#item-72216f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この変更は、「create-index-no-data.png」という画像ファイルに関連しますが、具体的な変更内容はありません。ファイルの状態は「modified」となっていますが、追加や削除は行われていません。このような場合、画像ファイルのメタデータやその管理に関する更新が行われた可能性があります。ユーザーにとっては、今後の利用において、ファイルが適切に整理され、リファレンスとしての機能が保たれることを期待できます。

## articles/search/media/search-howto-index-sharepoint-online/aad-app-authentication-configuration.png{#item-56d8b1}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この変更は、「aad-app-authentication-configuration.png」という画像ファイルの更新に関連しています。状態が「modified」となっているものの、具体的には追加や削除、変更は行われていません。このことから、ファイルの内部内容や表示形式の変更があったのではなく、メタデータやファイルの管理に関する小規模な修正が行われた可能性があります。これにより、ユーザーは最新の情報を得るために適切にファイルにアクセスできる状況が維持されていることが期待されます。

## articles/search/media/search-index-azure-sql-managed-instance-with-managed-identity/access-control-add-role-assignment.png{#item-baa746}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この変更は、「access-control-add-role-assignment.png」という画像ファイルに関するもので、ファイルの状態が「modified」となっていますが、具体的な変更内容については、追加、削除、変更が行われていません。このような場合、ファイルの管理やメタデータに関する軽微な更新があった可能性があります。結果として、ファイルが正しく整理されていることが確認され、ユーザーが必要な情報を円滑に利用できるようになっていることが期待されます。

## articles/search/media/search-indexer-howto-secure-access/exception.png{#item-be28c5}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この変更は、「exception.png」という画像ファイルに関連しており、ファイルの状態が「modified」とされていますが、具体的には追加、削除、変更が行われていません。このことから、ファイルに対して軽微な更新やメタデータの調整が行われた可能性が高いです。このような調整によって、ユーザーが最新の情報を得るために、適切にファイルを利用できる状態が保たれていることが期待されます。

## articles/search/media/search-indexer-howto-secure-access/private-endpoint-link.png{#item-d04198}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この変更は、「private-endpoint-link.png」という画像ファイルに関するもので、ファイルの状態が「modified」となっていますが、追加、削除、変更に関する具体的な内容は記載されていません。このことから、ファイル自体に対する軽微な更新やメタデータの調整が行われた可能性があります。従って、ユーザーが最新の情報にアクセスできる状態が維持されていることが期待されます。

## articles/search/media/search-indexer-howto-secure-access/search-service-portal.png{#item-a02d68}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この変更は、「search-service-portal.png」という画像ファイルの修正に関するもので、ファイルの状態は「modified」とされていますが、追加、削除、または変更の具体的な内容は示されていません。これは、ファイルの内容に対する軽微な更新またはメタデータの調整が行われた可能性が考えられます。この更新により、ユーザーは最新の情報を反映した形でファイルを利用できるようになることが期待されます。

## articles/search/media/search-indexer-howto-secure-access/storage-firewall-ip.png{#item-a8423b}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この変更は、「storage-firewall-ip.png」という画像ファイルに関連したもので、ファイルの状態は「modified」に設定されています。しかし、具体的な追加、削除、または変更の内容は報告されていないため、軽微な更新やメタデータの調整が行われたと推測されます。この更新により、ユーザーが最新の情報を持つ画像ファイルにアクセスできることが期待されます。

## articles/search/media/search-indexer-howto-secure-access/storage-privateendpoint-after-approval.png{#item-dd6f81}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この変更は、「storage-privateendpoint-after-approval.png」という画像ファイルの修正に関するもので、ファイルの現在の状態は「modified」とされています。具体的な変更内容としては、追加、削除、または変更の数は報告されていないため、内容の軽微な更新やメタデータの調整が実施された可能性があります。この更新により、ユーザーは最新の情報を含む画像ファイルにアクセスできるようになります。

## articles/search/media/search-indexer-howto-secure-access/storage-privateendpoint-approval.png{#item-eb9921}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この変更は、「storage-privateendpoint-approval.png」という画像ファイルの修正を示しています。その状態は「modified」とされ、具体的な追加、削除、または変更の内容は報告されていません。このことから、内容については軽微な更新やメタデータの調整が行われたと推測されます。この更新により、ユーザーは最新の情報を反映した画像ファイルにアクセスできるようになります。

## articles/search/media/search-indexer-howto-secure-access/test-system-identity.png{#item-7a7123}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この変更は、「test-system-identity.png」という画像ファイルの修正について記録されています。ファイルのステータスは「modified」となっており、具体的に追加、削除、または変更の数は報告されていません。このことから、軽微な更新が行われた可能性があります。この更新により、ユーザーは画像の最新情報を確認できるようになります。

## articles/search/media/search-managed-identities/connect-with-visual-studio.png{#item-91286e}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この変更は、「connect-with-visual-studio.png」という画像ファイルの修正を示しています。ファイルは「modified」として状態が記載されており、具体的な追加、削除、または変更は行われていないとされています。このことから、軽微な更新が行われた可能性があり、ユーザーは最新の状態の画像ファイルにアクセスできるようになっています。

## articles/search/media/vector-search-index-size/deployment-details.png{#item-e7b137}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの修正"
}
```

### Explanation
この変更は、「deployment-details.png」という画像ファイルの修正を示しています。ファイルの状態は「modified」と記載されていますが、具体的な追加、削除、変更は行われていないため、軽微な更新が行われたと考えられます。この変更により、ユーザーは最新の情報を反映した画像にアクセスできるようになっています。

## articles/search/monitor-azure-cognitive-search-data-reference.md{#item-561425}

<details>
<summary>Diff</summary>
````diff
@@ -194,13 +194,13 @@ The following operations can appear in a resource log.
 | Indexers.* | Applies to an indexer. Can be Create, Delete, Get, List, and Status. |
 | Indexes.* | Applies to a search index. Can be Create, Delete, Get, List.  |
 | indexes.Prototype | This index is created by the Import Data wizard. |
-| Indexing.Index  | This operation is a call to [Add, Update or Delete Documents](/rest/api/searchservice/addupdate-or-delete-documents). |
+| Indexing.Index  | This operation is a call to [Index Documents](/rest/api/searchservice/documents). |
 | Metadata.GetMetadata | A request for search service system data.  |
 | Query.Autocomplete | An autocomplete query against an index. See [Query types and composition](search-query-overview.md). |
 | Query.Lookup |  A lookup query against an index. See [Query types and composition](search-query-overview.md). |
 | Query.Search |  A full text search request against an index. See [Query types and composition](search-query-overview.md). |
 | Query.Suggest |  Type ahead query against an index. See [Query types and composition](search-query-overview.md). |
-| ServiceStats | This operation is a routine call to [Get Service Statistics](/rest/api/searchservice/get-service-statistics), either called directly or implicitly to populate a portal overview page when it's loaded or refreshed. |
+| ServiceStats | This operation is a routine call to [Get Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics), either called directly or implicitly to populate a portal overview page when it's loaded or refreshed. |
 | Skillsets.* | Applies to a skillset. Can be Create, Delete, Get, List. |
 
 ## Related content
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Markdownファイルの内容修正"
}
```

### Explanation
この変更は、「monitor-azure-cognitive-search-data-reference.md」というMarkdownファイルの内容を修正するもので、全体で4つの変更が行われています。具体的には、2つの行が追加され、2つの行が削除されています。特に、ドキュメント内の特定の操作やAPI呼び出しに関する説明が更新されており、ユーザーに提供される情報の正確性と関連性が向上しています。これにより、Azure Cognitive Searchに関するリファレンス情報がより明確になり、利用者にとって使いやすくなっています。

## articles/search/query-lucene-syntax.md{#item-736436}

<details>
<summary>Diff</summary>
````diff
@@ -109,7 +109,7 @@ You can define a fielded search operation with the `fieldName:searchExpression`
 
 Be sure to put multiple strings within quotation marks if you want both strings to be evaluated as a single entity, in this case searching for two distinct artists in the `artists` field.  
 
-The field specified in `fieldName:searchExpression` must be a `searchable` field.  See [Create Index](/rest/api/searchservice/create-index) for details on how index attributes are used in field definitions.  
+The field specified in `fieldName:searchExpression` must be a `searchable` field.  See [Create Index](/rest/api/searchservice/indexes/create) for details on how index attributes are used in field definitions.  
 
 > [!NOTE]
 > When using fielded search expressions, you do not need to use the `searchFields` parameter because each fielded search expression has a field name explicitly specified. However, you can still use the `searchFields` parameter if you want to run a query where some parts are scoped to a specific field, and the rest could apply to several fields. For example, the query `search=genre:jazz NOT history&searchFields=description` would match `jazz` only to the `genre` field, while it would match `NOT history` with the `description` field. The field name provided in `fieldName:searchExpression` always takes precedence over the `searchFields` parameter, which is why in this example, we do not need to include `genre` in the `searchFields` parameter.
@@ -184,7 +184,7 @@ Azure AI Search uses frequency-based scoring ([BM25](https://en.wikipedia.org/wi
 
 In some circumstances, you may want to search for a special character, like an '❤' emoji or the '€' sign. In such cases, make sure that the analyzer you use doesn't filter those characters out. The standard analyzer bypasses many special characters, excluding them from your index.
 
-Analyzers that tokenize special characters include the whitespace analyzer, which takes into consideration any character sequences separated by whitespaces as tokens (so the `❤` string would be considered a token). Also, a language analyzer like the Microsoft English analyzer ("en.microsoft"), would take the "€" string as a token. You can [test an analyzer](/rest/api/searchservice/test-analyzer) to see what tokens it generates for a given query.
+Analyzers that tokenize special characters include the whitespace analyzer, which takes into consideration any character sequences separated by whitespaces as tokens (so the `❤` string would be considered a token). Also, a language analyzer like the Microsoft English analyzer ("en.microsoft"), would take the "€" string as a token. You can [test an analyzer](/rest/api/searchservice/indexes/analyze) to see what tokens it generates for a given query.
 
 When using Unicode characters, make sure symbols are properly escaped in the query url (for instance for `❤` would use the escape sequence `%E2%9D%A4+`). Some REST clients do this translation automatically.  
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Lucene構文ドキュメントの修正"
}
```

### Explanation
この変更は、「query-lucene-syntax.md」というLucene構文に関するMarkdownファイルの修正です。全体で4つの変更が行われ、2つの行が追加され、2つの行が削除されました。主な修正点は、リンクが特定のAPIエンドポイントから別のエンドポイントに変更されたことです。具体的には、「Create Index」へのリンクが「/rest/api/searchservice/create-index」から「/rest/api/searchservice/indexes/create」へ変更され、アナライザーをテストするためのリンクも同様に更新されています。この変更により、ユーザーは最新のAPI構造に基づいた正確な情報にアクセスできるようになりました。

## articles/search/query-odata-filter-orderby-syntax.md{#item-6ab74f}

<details>
<summary>Diff</summary>
````diff
@@ -83,17 +83,17 @@ Field paths are used in many parameters of the [Azure AI Search REST APIs](/rest
 
 | API | Parameter name | Restrictions |
 | --- | --- | --- |
-| [Create](/rest/api/searchservice/create-index) or [Update](/rest/api/searchservice/update-index) Index | `suggesters/sourceFields` | None |
-| [Create](/rest/api/searchservice/create-index) or [Update](/rest/api/searchservice/update-index) Index | `scoringProfiles/text/weights` | Can only refer to **searchable** fields |
-| [Create](/rest/api/searchservice/create-index) or [Update](/rest/api/searchservice/update-index) Index | `scoringProfiles/functions/fieldName` | Can only refer to **filterable** fields |
+| [Create](/rest/api/searchservice/indexes/create) or [Update](/rest/api/searchservice/indexes/create-or-update) Index | `suggesters/sourceFields` | None |
+| [Create](/rest/api/searchservice/indexes/create) or [Update](/rest/api/searchservice/indexes/create-or-update) Index | `scoringProfiles/text/weights` | Can only refer to **searchable** fields |
+| [Create](/rest/api/searchservice/indexes/create) or [Update](/rest/api/searchservice/indexes/create-or-update) Index | `scoringProfiles/functions/fieldName` | Can only refer to **filterable** fields |
 | [Search](/rest/api/searchservice/documents/search-post) | `search` when `queryType` is `full` | Can only refer to **searchable** fields |
 | [Search](/rest/api/searchservice/documents/search-post) | `facet` | Can only refer to **facetable** fields |
 | [Search](/rest/api/searchservice/documents/search-post) | `highlight` | Can only refer to **searchable** fields |
 | [Search](/rest/api/searchservice/documents/search-post) | `searchFields` | Can only refer to **searchable** fields |
-| [Suggest](/rest/api/searchservice/suggestions) and [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) | `searchFields` | Can only refer to fields that are part of a [suggester](index-add-suggesters.md) |
-| [Search](/rest/api/searchservice/documents/search-post), [Suggest](/rest/api/searchservice/suggestions), and [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) | `$filter` | Can only refer to **filterable** fields |
-| [Search](/rest/api/searchservice/documents/search-post) and [Suggest](/rest/api/searchservice/suggestions) | `$orderby` | Can only refer to **sortable** fields |
-| [Search](/rest/api/searchservice/documents/search-post), [Suggest](/rest/api/searchservice/suggestions), and [Lookup](/rest/api/searchservice/lookup-document) | `$select` | Can only refer to **retrievable** fields |
+| [Suggest](/rest/api/searchservice/documents/suggest-post) and [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) | `searchFields` | Can only refer to fields that are part of a [suggester](index-add-suggesters.md) |
+| [Search](/rest/api/searchservice/documents/search-post), [Suggest](/rest/api/searchservice/documents/suggest-post), and [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) | `$filter` | Can only refer to **filterable** fields |
+| [Search](/rest/api/searchservice/documents/search-post) and [Suggest](/rest/api/searchservice/documents/suggest-post) | `$orderby` | Can only refer to **sortable** fields |
+| [Search](/rest/api/searchservice/documents/search-post), [Suggest](/rest/api/searchservice/documents/suggest-post), and [Lookup](/rest/api/searchservice/documents/get) | `$select` | Can only refer to **retrievable** fields |
 
 ## Constants
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ODataフィルターおよびソート構文の文書更新"
}
```

### Explanation
この変更は、「query-odata-filter-orderby-syntax.md」というODataフィルターおよびソートに関するMarkdown文書の修正です。全体で14の変更が行われ、7つの行が追加され、7つの行が削除されました。主な変更点は、API呼び出しに関連するリンクの更新です。具体的には、インデックスを作成または更新するためのリンクが「/rest/api/searchservice/create-index」および「/rest/api/searchservice/update-index」から「/rest/api/searchservice/indexes/create」および「/rest/api/searchservice/indexes/create-or-update」に変更されています。これにより、最新のAPIエンドポイントに基づいた明確な情報が提供され、ユーザーは正確なサービスを利用できるようになります。

## articles/search/query-simple-syntax.md{#item-ab3c96}

<details>
<summary>Diff</summary>
````diff
@@ -50,7 +50,7 @@ Strings passed to the `search` parameter can include terms or phrases in any sup
 
 Depending on your search client, you might need to escape the quotation marks in a phrase search. For example, in a POST request, a phrase search on `"Roach Motel"` in the request body might be specified as `"\"Roach Motel\""`. If you're using the Azure SDKs, the search client escapes the quotation marks when it serializes the search text. Your search phrase can be sent be as "Roach Motel".
   
-By default, all strings passed in the `search` parameter undergo lexical analysis. Make sure you understand the tokenization behavior of the analyzer you're using. Often, when query results are unexpected, the reason can be traced to how terms are tokenized at query time. You can [test tokenization on specific strings](/rest/api/searchservice/test-analyzer) to confirm the output.
+By default, all strings passed in the `search` parameter undergo lexical analysis. Make sure you understand the tokenization behavior of the analyzer you're using. Often, when query results are unexpected, the reason can be traced to how terms are tokenized at query time. You can [test tokenization on specific strings](/rest/api/searchservice/indexes/analyze) to confirm the output.
 
 Any text input with one or more terms is considered a valid starting point for query execution. Azure AI Search will match documents containing any or all of the terms, including any variations found during analysis of the text.
 
@@ -111,7 +111,7 @@ If you need special character representation, you can assign an analyzer that pr
 
 + A [language analyzer](search-language-support.md), such as the Microsoft English analyzer (`en.microsoft`), would take the '$' or '€' string as a token. 
 
-For confirmation, you can [test an analyzer](/rest/api/searchservice/test-analyzer) to see what tokens are generated for a given string. As you might expect, you might not get full tokenization from a single analyzer. A workaround is to create multiple fields that contain the same content, but with different analyzer assignments (for example, `description_en`, `description_fr`, and so forth for language analyzers).
+For confirmation, you can [test an analyzer](/rest/api/searchservice/indexes/analyze) to see what tokens are generated for a given string. As you might expect, you might not get full tokenization from a single analyzer. A workaround is to create multiple fields that contain the same content, but with different analyzer assignments (for example, `description_en`, `description_fr`, and so forth for language analyzers).
 
 When using Unicode characters, make sure symbols are properly escaped in the query url (for instance for '❤' would use the escape sequence `%E2%9D%A4+`). Some web clients do this translation automatically.  
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "簡易検索構文に関する文書更新"
}
```

### Explanation
この変更は、「query-simple-syntax.md」という簡易検索構文に関するMarkdown文書の修正です。全体で4つの変更が行われ、2つの行が追加され、2つの行が削除されました。主な変更点は、テスト用のリンクの更新です。具体的には、トークン化をテストするためのリンクが「/rest/api/searchservice/test-analyzer」から「/rest/api/searchservice/indexes/analyze」に変更されています。この修正により、ユーザーは最新のAPI構造に基づいた正確な情報にアクセスできるようになります。文書は、検索パラメータに割り当てられたアナライザーの動作やUnicode文字のエスケープについても言及しており、検索クエリの効果的な実行に役立つ内容となっています。

## articles/search/reference-stopwords.md{#item-63e4b3}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,7 @@ This article lists the stopwords used by the Microsoft analyzer for each languag
 For the stopword list for Lucene analyzers, see the [Apache Lucene source code on GitHub](https://github.com/apache/lucene/tree/main/lucene/analysis/common/src/resources/org/apache/lucene/analysis).
 
 > [!TIP]
-> To view the output of any given analyzer, call the [Analyze Text REST API](/rest/api/searchservice/test-analyzer). This API is often helpful for debugging unexpected search results.
+> To view the output of any given analyzer, call the [Analyze Text REST API](/rest/api/searchservice/indexes/analyze). This API is often helpful for debugging unexpected search results.
 
 ## Arabic (ar.microsoft)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ストップワード参照文書の更新"
}
```

### Explanation
この変更は、「reference-stopwords.md」というストップワードに関するMarkdown文書の修正です。全体で2つの変更が行われ、1つの行が追加され、1つの行が削除されました。主な変更点は、アナライザーの出力を確認するためのリンクの更新です。具体的には、アナライズテキストREST APIのリンクが「/rest/api/searchservice/test-analyzer」から「/rest/api/searchservice/indexes/analyze」に変更されました。この更新により、ユーザーは最新のAPIを使用してアナライザーの出力を正確に確認できるようになります。文書は、Microsoftアナライザーによって使用されるストップワードのリストや、Luceneアナライザーに関する情報も提供しており、情報の正確性が保たれています。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -71,7 +71,7 @@ RAG patterns that include Azure AI Search have the elements indicated in the fol
 
 The web app provides the user experience, providing the presentation, context, and user interaction. Questions or prompts from a user start here. Inputs pass through the integration layer, going first to information retrieval to get the search results, but also go to the LLM to set the context and intent. 
 
-The app server or orchestrator is the integration code that coordinates the handoffs between information retrieval and the LLM. Common solutions include [LangChain](https://python.langchain.com/docs/get_started/introduction) to coordinate the workflow. LangChain [integrates with Azure AI Search](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/), making it easier to include Azure AI Search as a [retriever](https://python.langchain.com/docs/modules/data_connection/retrievers/) in your workflow. [LlamaIndex](https://github.com/run-llama/llama_index/tree/main/llama-index-integrations/vector_stores/llama-index-vector-stores-azureaisearch) and [Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/announcing-semantic-kernel-integration-with-azure-cognitive-search/) are other options.
+The app server or orchestrator is the integration code that coordinates the handoffs between information retrieval and the LLM. Common solutions include [LangChain](https://python.langchain.com/docs/get_started/introduction) to coordinate the workflow. LangChain [integrates with Azure AI Search](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/), making it easier to include Azure AI Search as a [retriever](https://python.langchain.com/docs/how_to/#retrievers) in your workflow. [LlamaIndex](https://github.com/run-llama/llama_index/tree/main/llama-index-integrations/vector_stores/llama-index-vector-stores-azureaisearch) and [Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/announcing-semantic-kernel-integration-with-azure-cognitive-search/) are other options.
 
 The information retrieval system provides the searchable index, query logic, and the payload (query response). The search index can contain vectors or nonvector content. Although most samples and demos include vector fields, it's not a requirement. The query is executed using the existing search engine in Azure AI Search, which can handle keyword (or term) and vector queries. The index is created in advance, based on a schema you define, and loaded with your content that's sourced from files, databases, or storage.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "情報検索とLLMの統合に関する文書の更新"
}
```

### Explanation
この変更は、「retrieval-augmented-generation-overview.md」という情報検索と生成に関するMarkdown文書の修正です。全体で2つの変更が行われ、1つの行が追加され、1つの行が削除されました。主な変更点は、Azure AI Searchをリトリーバーとして使用するためのリンクの更新です。具体的には、LangChainのリトリーバーの使用方法に関するリンクが「/docs/modules/data_connection/retrievers/」から「/docs/how_to/#retrievers」に変更されています。この修正により、ユーザーはAzure AI Searchを使用して情報を効率的に検索する方法について、最新の情報に基づいて理解を深めることができます。文書は、ユーザーインターフェース、インテグレーションコードの役割、情報検索システムの機能についても詳しく説明しており、情報の正確性を保っています。

## articles/search/samples-javascript.md{#item-82e67e}

<details>
<summary>Diff</summary>
````diff
@@ -59,8 +59,8 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 | Samples | Article |
 |---------|---------|
 | [quickstart](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) | Source code for the JavaScript portion of [Quickstart: Full text search using the Azure SDKs](search-get-started-text.md). Covers the basic workflow for creating, loading, and querying a search index using sample data. |
-| [bulk-insert](https://github.com/Azure-Samples/azure-search-javascriptn-samples/tree/main/bulk-insert) | Source code for the JavaScript example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
-| [azure-functions](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/azure-function) | Source code for the JavaScript example of an Azure function that sends queries to a search service. You can substitute this JavaScript version of the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
+| [bulk-insert](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/bulk-insert) | Source code for the JavaScript example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
+| [azure-functions](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/azure-function-search) | Source code for the JavaScript example of an Azure function that sends queries to a search service. You can substitute this JavaScript version of the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
 > [!TIP]
 > Try the [Samples browser](/samples/browse/?languages=javascript&products=azure-cognitive-search) to search for Microsoft code samples in GitHub, filtered by product, service, and language.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptサンプル文書のリンク修正"
}
```

### Explanation
この変更は、「samples-javascript.md」というJavaScriptに関するサンプル文書の修正です。全体で4つの変更が行われ、2つの行が追加され、2つの行が削除されました。主な変更点は、Azure Functionsのサンプルコードのリンクが更新されたことです。具体的には、Azure FunctionsのサンプルへのURLが「/azure-search-javascript-samples/tree/main/azure-function」から「/azure-search-javascript-samples/tree/main/azure-function-search」に変更され、正確なリンクが提供されるようになりました。これにより、ユーザーは最新のサンプルコードにアクセスしやすくなり、Azure AI Searchに関連するさまざまな機能やワークフローを理解する手助けとなります。また、基本的なワークフローである検索インデックスの作成、ロード、クエリの実行方法についても、他のサンプルとともに情報が提供されています。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -53,7 +53,7 @@ Code samples from the Azure AI Search team demonstrate features and workflows. M
 | [quickstart](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart) | Source code for the Python portion of [Quickstart: Full text search using the Azure SDKs](search-get-started-text.md). This article covers the basic workflow for creating, loading, and querying a search index using sample data. |
 | [quickstart-semantic-search](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-Semantic-Search) | Source code for the Python portion of [Quickstart: Semantic ranking using the Azure SDKs](search-get-started-semantic.md). It shows the index schema and query request for invoking semantic ranking. |
 | [bulk-insert](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/bulk-insert) | Source code for the Python example of how to [use the push APIs](search-how-to-load-search-index.md) to upload and index documents. |
-| [azure-functions](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/azure-function) | Source code for the Python example of an Azure function that sends queries to a search service. You can substitute this Python version of the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
+| [azure-functions](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/azure-function-search) | Source code for the Python example of an Azure function that sends queries to a search service. You can substitute this Python version of the `api` code used in the [Add search to web sites](tutorial-csharp-overview.md) C# sample. |
 
 ## Demos
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonサンプル文書のリンク修正"
}
```

### Explanation
この変更は、「samples-python.md」というPythonに関するサンプル文書の修正です。全体で2つの変更が行われ、1つの行が追加され、1つの行が削除されました。主な変更点は、Azure Functionsのサンプルコードのリンクが更新されたことです。具体的には、Azure FunctionsのサンプルへのURLが「/azure-search-python-samples/tree/main/azure-function」から「/azure-search-python-samples/tree/main/azure-function-search」に変更されました。この修正により、ユーザーは正確で最新のサンプルコードにアクセスできるようになり、Azure AI Searchを使用した機能の理解が深まります。また、各サンプルは、検索インデックスの作成、ロード、クエリの実行方法に関する基本的なワークフローを含んでおり、全体的なドキュメントの精度と信頼性が向上しています。

## articles/search/search-add-autocomplete-suggestions.md{#item-0a43e0}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ Search-as-you-type is a common technique for improving query productivity. In Az
 To implement these experiences in Azure AI Search:
 
 + Add a `suggester` to an index schema.
-+ Build a query that calls the [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) or [Suggestions](/rest/api/searchservice/suggestions) API on the request.
++ Build a query that calls the [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) or [Suggestions](/rest/api/searchservice/documents/suggest-post) API on the request.
 + Add a UI control to handle search-as-you-type interactions in your client app. We recommend using an existing JavaScript library for this purpose.
 
 In Azure AI Search, autocompleted queries and suggested results are retrieved from the search index, from selected fields that you register with a suggester. A suggester is part of the index, and it specifies which fields provide content that either completes a query, suggests a result, or does both. When the index is created and loaded, a suggester data structure is created internally to store prefixes used for matching on partial queries. For suggestions, choosing suitable fields that are unique, or at least not repetitive, is essential to the experience. For more information, see [Create a suggester](index-add-suggesters.md).
@@ -51,20 +51,20 @@ Matches are on the beginning of a term anywhere in the input string. Given "the
 
 Follow these links for the REST and .NET SDK reference pages:
 
-+ [Suggestions REST API](/rest/api/searchservice/suggestions) 
++ [Suggestions REST API](/rest/api/searchservice/documents/suggest-post) 
 + [Autocomplete REST API](/rest/api/searchservice/documents/autocomplete-post) 
 + [SuggestAsync method](/dotnet/api/azure.search.documents.searchclient.suggestasync)
 + [AutocompleteAsync method](/dotnet/api/azure.search.documents.searchclient.autocompleteasync)
 
 ## Structure a response
 
-Responses for autocomplete and suggestions are what you might expect for the pattern: [Autocomplete](/rest/api/searchservice/documents/autocomplete-post#responses) returns a list of terms, [Suggestions](/rest/api/searchservice/suggestions#response) returns terms plus a document ID so that you can fetch the document (use the [Lookup Document](/rest/api/searchservice/lookup-document) API to fetch the specific document for a detail page).
+Responses for autocomplete and suggestions are what you might expect for the pattern: [Autocomplete](/rest/api/searchservice/documents/autocomplete-post#responses) returns a list of terms, [Suggestions](/rest/api/searchservice/documents/suggest-post#response) returns terms plus a document ID so that you can fetch the document (use the [Lookup Document](/rest/api/searchservice/documents/get) API to fetch the specific document for a detail page).
 
 Responses are shaped by the parameters on the request:
 
 + For Autocomplete, set the [autocompleteMode](/rest/api/searchservice/documents/autocomplete-post#autocompletemode) to determine whether text completion occurs on one or two terms. 
 
-+ For Suggestions, set [$select](/rest/api/searchservice/suggestions#query-parameters) to return fields containing unique or differentiating values, such as names and description. Avoid fields that contain duplicate values (such as a category or city).
++ For Suggestions, set [$select](/rest/api/searchservice/documents/suggest-post#request-body) to return fields containing unique or differentiating values, such as names and description. Avoid fields that contain duplicate values (such as a category or city).
 
 The following parameters apply to both autocomplete and suggestions, but are more applicable to suggestions, especially when a suggester includes multiple fields.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "自動補完および提案APIのリンク修正"
}
```

### Explanation
この変更は、「search-add-autocomplete-suggestions.md」という文書の修正です。全体で8つの変更が行われ、4つの行が追加され、4つの行が削除されました。主な変更点は、提案と自動補完に関連するAPIのリンクが更新されたことです。具体的には、以前は「/rest/api/searchservice/suggestions」だったAPIのURLが「/rest/api/searchservice/documents/suggest-post」に変更されました。この修正により、正確なAPIエンドポイントが提供されるようになり、ユーザーがドキュメントやサンプルコードを正しく参照できるようになります。

また、文書内のいくつかの文が見直され、より明確な表現に修正されています。例えば、自動補完と提案のレスポンスについての説明が更新され、新しいAPIへの正しいリンクが強調されています。これにより、Azure AI Searchを使用する際のユーザー体験が向上し、特にクエリ生産性を向上させる方法についての理解が深まります。文書全体として、ユーザーが適切なAPIを利用しやすくなり、より良い検索体験を提供することが目的とされています。

## articles/search/search-analyzers.md{#item-9dccd9}

<details>
<summary>Diff</summary>
````diff
@@ -60,7 +60,7 @@ A few built-in analyzers, such as **Pattern** or **Stop**, support a limited set
 
 Setting an analyzer is optional. As a general rule, try using the default standard Lucene analyzer first to see how it performs. If queries fail to return the expected results, switching to a different analyzer is often the right solution.
 
-1. If you're using a custom analyzer, add it to the search index under the "analyzer" section. For more information, see [Create Index](/rest/api/searchservice/create-index) and also [Add custom analyzers](index-add-custom-analyzers.md).
+1. If you're using a custom analyzer, add it to the search index under the "analyzer" section. For more information, see [Create Index](/rest/api/searchservice/indexes/create) and also [Add custom analyzers](index-add-custom-analyzers.md).
 
 1. When defining a field, set it's "analyzer" property to one of the following: a [built-in analyzer](index-add-custom-analyzers.md#built-in-analyzers) such as **keyword**, a [language analyzer](index-add-language-analyzers.md) such as `en.microsoft`, or a custom analyzer (defined in the same index schema).  
  
@@ -100,11 +100,11 @@ The best time to add and assign analyzers is during active development, when dro
 
 Because analyzers are used to tokenize terms, you should assign an analyzer when the field is created. In fact, assigning an analyzer or indexAnalyzer to a field that has already been physically created isn't allowed (although you can change the searchAnalyzer property at any time with no impact to the index).
 
-To change the analyzer of an existing field, you'll have to drop and recreate the entire index (you can't rebuild individual fields). For indexes in production, you can defer a rebuild by creating a new field with the new analyzer assignment, and start using it in place of the old one. Use [Update Index](/rest/api/searchservice/update-index) to incorporate the new field and [mergeOrUpload](/rest/api/searchservice/addupdate-or-delete-documents) to populate it. Later, as part of planned index servicing, you can clean up the index to remove obsolete fields.
+To change the analyzer of an existing field, you'll have to drop and recreate the entire index (you can't rebuild individual fields). For indexes in production, you can defer a rebuild by creating a new field with the new analyzer assignment, and start using it in place of the old one. Use [Update Index](/rest/api/searchservice/indexes/create-or-update) to incorporate the new field and [mergeOrUpload](/rest/api/searchservice/documents) to populate it. Later, as part of planned index servicing, you can clean up the index to remove obsolete fields.
 
-To add a new field to an existing index, call [Update Index](/rest/api/searchservice/update-index) to add the field, and [mergeOrUpload](/rest/api/searchservice/addupdate-or-delete-documents) to populate it.
+To add a new field to an existing index, call [Update Index](/rest/api/searchservice/indexes/create-or-update) to add the field, and [mergeOrUpload](/rest/api/searchservice/documents) to populate it.
 
-To add a custom analyzer to an existing index, pass the "allowIndexDowntime" flag in [Update Index](/rest/api/searchservice/update-index) if you want to avoid this error:
+To add a custom analyzer to an existing index, pass the "allowIndexDowntime" flag in [Update Index](/rest/api/searchservice/indexes/create-or-update) if you want to avoid this error:
 
 `"Index update not allowed because it would cause downtime. In order to add new analyzers, tokenizers, token filters, or character filters to an existing index, set the 'allowIndexDowntime' query parameter to 'true' in the index update request. Note that this operation will put your index offline for at least a few seconds, causing your indexing and query requests to fail. Performance and write availability of the index can be impaired for several minutes after the index is updated, or longer for very large indexes."`
 
@@ -124,7 +124,7 @@ Overriding the standard analyzer requires an index rebuild. If possible, decide
 
 ### Inspect tokenized terms
 
-If a search fails to return expected results, the most likely scenario is token discrepancies between term inputs on the query, and tokenized terms in the index. If the tokens aren't the same, matches fail to materialize. To inspect tokenizer output, we recommend using the [Analyze API](/rest/api/searchservice/test-analyzer) as an investigation tool. The response consists of tokens, as generated by a specific analyzer.
+If a search fails to return expected results, the most likely scenario is token discrepancies between term inputs on the query, and tokenized terms in the index. If the tokens aren't the same, matches fail to materialize. To inspect tokenizer output, we recommend using the [Analyze API](/rest/api/searchservice/indexes/analyze) as an investigation tool. The response consists of tokens, as generated by a specific analyzer.
 
 <a name="examples"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索アナライザーに関するリンク修正"
}
```

### Explanation
この変更は、「search-analyzers.md」という文書の修正です。全体で10の変更があり、5つの行が追加され、5つの行が削除されています。主な変更点は、文書内で参照されているAPIのエンドポイントが更新されたことです。具体的には、インデックス作成や更新に関連するリンクが修正されており、特に「Create Index」や「Update Index」のリンクが、それぞれ「/rest/api/searchservice/indexes/create」と「/rest/api/searchservice/indexes/create-or-update」に変更されています。

この変更により、最新のAPIに基づいた正確な情報が文書に反映され、利用者がAPIを適切に使用できるようになります。また、トークナイザーの出力を検査するための「Analyze API」のリンクも更新され、ユーザーが効果的にトークンの不一致を調査できるようになっています。

文書全体の内容は、アナライザーの設定や管理についての具体的なガイダンスを提供しており、特に新しいフィールドをインデックスに追加したり、既存のフィールドのアナライザーを変更する際の手順についての情報が強化されています。これにより、Azure AI Searchを利用するユーザーにとって、より明確で実用的なリファレンスが提供されることを目的としています。

## articles/search/search-filters.md{#item-3f2a7a}

<details>
<summary>Diff</summary>
````diff
@@ -110,7 +110,7 @@ The following examples illustrate several usage patterns for filter scenarios. F
 
 ## Field requirements for filtering
 
-In the REST API, filterable is *on* by default for simple fields. Filterable fields increase index size; be sure to set `"filterable": false` for fields that you don't plan to actually use in a filter. For more information about settings for field definitions, see [Create Index](/rest/api/searchservice/create-index).
+In the REST API, filterable is *on* by default for simple fields. Filterable fields increase index size; be sure to set `"filterable": false` for fields that you don't plan to actually use in a filter. For more information about settings for field definitions, see [Create Index](/rest/api/searchservice/indexes/create).
 
 In the .NET SDK, the filterable is *off* by default. You can make a field filterable by setting the [IsFilterable property](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable) of the corresponding [SearchField](/dotnet/api/azure.search.documents.indexes.models.searchfield) object to `true`. In the next example, the attribute is set on the `Rating` property of a model class that maps to the index definition.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フィルタリングに関するリンク修正"
}
```

### Explanation
この変更は、「search-filters.md」という文書の修正です。変更内容は2つで、1つの行が追加され、1つの行が削除されています。主な変更点は、フィルタリングに関する設定やフィールド定義に関するリンクの更新です。具体的には、元々「/rest/api/searchservice/create-index」だったリンクが「/rest/api/searchservice/indexes/create」に修正されました。

このリンク変更により、ユーザーはAzureのAPIの最新の使用法を正確に参照できるようになります。文書は、フィルタ可能なフィールドのデフォルト設定について説明し、どのように非フィルタ可能なフィールドを設定するかの注意点を強調しています。この修正は、ユーザーがフィルタリング機能を効果的に利用するための正しい情報を提供し、フィールド定義の設定に関する理解を深めることを目的としています。また、.NET SDKにおけるフィルタ可能プロパティの設定方法についても言及されており、具体的な実装例が提供されています。これにより、フィルタリングの実践的な利用が促進されることを目指しています。

## articles/search/search-get-started-powershell.md{#item-4435d0}

<details>
<summary>Diff</summary>
````diff
@@ -74,7 +74,7 @@ All requests require an API key on every request sent to your service. Having a
 
 ## Create an index
 
-Unless you're using the portal, an index must exist on the service before you can load data. This step defines the index and pushes it to the service. The [Create Index REST API](/rest/api/searchservice/create-index) is used for this step.
+Unless you're using the portal, an index must exist on the service before you can load data. This step defines the index and pushes it to the service. The [Create Index REST API](/rest/api/searchservice/indexes/create) is used for this step.
 
 Required elements of an index include a name and a fields collection. The fields collection defines the structure of a *document*. Each field has a name, type, and attributes that determine how it's used (for example, whether it's full-text searchable, filterable, or retrievable in search results). Within an index, one of the fields of type `Edm.String` must be designated as the *key* for document identity.
 
@@ -170,7 +170,7 @@ This index is named `hotels-quickstart` and has the field definitions you see in
 
 ## Load documents
 
-To push documents, use an HTTP POST request to your index's URL endpoint. The REST API for this task is [Add, Update, or Delete Documents](/rest/api/searchservice/addupdate-or-delete-documents).
+To push documents, use an HTTP POST request to your index's URL endpoint. The REST API for this task is [Index Documents](/rest/api/searchservice/documents).
 
 1. Paste this example into PowerShell to create a `$body` object that contains the documents you want to upload.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PowerShellでの検索開始に関するリンク修正"
}
```

### Explanation
この変更は、「search-get-started-powershell.md」という文書の修正です。今回の修正は合計4つの変更があり、2つの行が追加され、2つの行が削除されています。主な変更点は、REST APIエンドポイントのリンクが更新されたことです。

具体的には、「Create Index」APIへのリンクが「/rest/api/searchservice/create-index」から「/rest/api/searchservice/indexes/create」に変更されています。また、ドキュメントをインデックスに追加するためのAPIへのリンクも修正されており、元々「Add, Update, or Delete Documents」APIのリンクが「/rest/api/searchservice/addupdate-or-delete-documents」から「Index Documents」APIのリンク「/rest/api/searchservice/documents」に変更されています。

これにより、ユーザーは最新のAPI仕様に基づいて正確な情報を得ることができ、Azure Searchを利用する際の手順をより適切に理解できるようになります。この修正は、特にPowerShellを使用してAzure Searchにおけるインデックスの作成及びドキュメントの追加を行う際の実用性を向上させることを目的としています。また、インデックスの定義やドキュメントの構造に関する説明も含まれており、読者にとって有益なリファレンスとなります。

## articles/search/search-get-started-rag.md{#item-05ff0e}

<details>
<summary>Diff</summary>
````diff
@@ -290,9 +290,9 @@ logger.addHandler(handler)
 
 Rerun the query script. You should now get INFO and DEBUG statements in the output that provide more detail about the issue.
 
-If you see output messages related to ManagedIdentityCredential and token acquisition failures, it could be that you have multiple tenants, and your Azure sign-in is using a tenant that doesn't have your search service. To get your tenant ID, search the Azure portal for "tenant properties".
+If you see output messages related to ManagedIdentityCredential and token acquisition failures, it could be that you have multiple tenants, and your Azure sign-in is using a tenant that doesn't have your search service. To get your tenant ID, search the Azure portal for "tenant properties" or run `az login tenant list`.
 
-Run `az login --tenant <YOUR-TENANT-ID>` at a command prompt, and then rerun the script.
+Once you have your tenant ID, run `az login --tenant <YOUR-TENANT-ID>` at a command prompt, and then rerun the script.
 
 ## Clean up
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGの開始に関する手順の修正"
}
```

### Explanation
この変更は、「search-get-started-rag.md」という文書に対する修正です。変更は合計4つで、2つの行が追加され、2つの行が削除されています。この修正は、Azure Sign-inに関する手順を明確化することを目的としています。

具体的には、Managed Identity Credentialとトークン取得失敗に関するメッセージが出力された場合の対処法として、テナントIDを取得する手段が追加されました。元々は「Azureポータルで「tenant properties」を検索する」だけでしたが、新たに「az login tenant list」を実行する手順が加えられています。また、テナントIDを取得した後のコマンド実行手順も若干の言い回しが変更されています。

これにより、ユーザーは複数のテナントを使用している場合の問題解決のための手順をより簡単に理解できるようになります。特に、Azureサービスにアクセスするためのテナントを確認および設定する方法が明確になっており、ユーザーがスムーズにAzure Searchサービスを利用できることを目指しています。全体として、手順の明確化はユーザー体験の向上につながります。

## articles/search/search-get-started-rest.md{#item-0df9d5}

<details>
<summary>Diff</summary>
````diff
@@ -152,7 +152,7 @@ If you're not familiar with the REST client for Visual Studio Code, this section
 
 ## Create an index
 
-Add a second request to your `.rest` file. [Create Index (REST)](/rest/api/searchservice/create-index) creates a search index and sets up the physical data structures on your search service.
+Add a second request to your `.rest` file. [Create Index (REST)](/rest/api/searchservice/indexes/create) creates a search index and sets up the physical data structures on your search service.
 
 1. Paste in the following example to create the `hotels-quickstart` index on your search service.
 
@@ -198,7 +198,7 @@ Add a second request to your `.rest` file. [Create Index (REST)](/rest/api/searc
 
 Within the index schema, the fields collection defines document structure. Each document that you upload must have these fields. Each field must be assigned to an [Entity Data Model (EDM) data type](/rest/api/searchservice/supported-data-types). String fields are used in full text search. If you want numeric data to be searchable, make sure the data type is `Edm.String`. Other data types such as `Edm.Int32` are filterable, sortable, facetable, and retrievable but not full-text searchable.
 
-Attributes on the field determine allowed actions. The REST APIs allow [many actions by default](/rest/api/searchservice/create-index#request-body). For example, all strings are searchable and retrievable by default. For REST APIs, you might only have attributes if you need to turn off a behavior.
+Attributes on the field determine allowed actions. The REST APIs allow [many actions by default](/rest/api/searchservice/indexes/create#request-body). For example, all strings are searchable and retrievable by default. For REST APIs, you might only have attributes if you need to turn off a behavior.
 
 ```json
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIリンクの修正"
}
```

### Explanation
この変更は、「search-get-started-rest.md」という文書に対する修正です。合計で4つの変更があり、2つの行が追加され、2つの行が削除されています。この修正の主な目的は、REST APIに関するリンクを最新のものに更新することです。

具体的には、「Create Index (REST)」APIへのリンクが「/rest/api/searchservice/create-index」から「/rest/api/searchservice/indexes/create」に変更されました。また、フィールドの属性に関する説明の中でも同様に、リンクが更新されています。この変更により、ユーザーは最新のAPIドキュメントにアクセスでき、正確に操作を行うことが可能になります。

さらに、インデックスの作成にあたる手順やドキュメント構造に関する説明も含まれており、ユーザーはインデックスの作成がどのように行われるかをより深く理解することができます。この更新は、Azure SearchのREST APIを利用する際のドキュメントの質を向上させ、ユーザーの利便性を高めることを目的としています。

## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -113,7 +113,7 @@ You're pasting your personal identity token into the `.rest` or `.http` file in
 
 ## Create a vector index
 
-[Create Index (REST)](/rest/api/searchservice/create-index) creates a vector index and sets up the physical data structures on your search service.
+[Create Index (REST)](/rest/api/searchservice/indexes/create) creates a vector index and sets up the physical data structures on your search service.
 
 The index schema is organized around hotel content. Sample data consists of vector and nonvector names and descriptions of seven fictitious hotels. This schema includes configurations for vector indexing and queries, and for semantic ranking.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルインデックス作成リンクの修正"
}
```

### Explanation
この変更は、「search-get-started-vector.md」という文書に対する修正です。合計2つの変更があり、1つの行が追加され、1つの行が削除されています。この修正の主な目的は、ベクトルインデックスを作成するためのAPIリンクを更新することです。

具体的には、「Create Index (REST)」APIへのリンクが「/rest/api/searchservice/create-index」から「/rest/api/searchservice/indexes/create」に変更されました。このリンク変更により、ユーザーは最新のAPIにアクセスし、正確にベクトルインデックスを作成できるようになります。

また、インデックススキーマについての説明では、サンプルデータとして架空のホテルに関する情報が含まれており、ベクトルインデックスやクエリ、セマンティックランキングの設定が行われていることが明記されています。この更新は、ユーザーがAzure Searchにおけるベクトルインデックスの作成手順を理解しやすくすることを目的としています。全体として、ドキュメントの正確性と利便性を向上させるための重要な修正です。

## articles/search/search-how-to-index-onelake-files.md{#item-95f3db}

<details>
<summary>Diff</summary>
````diff
@@ -327,7 +327,7 @@ Some key points include:
 
 In a [search index](search-what-is-an-index.md), add fields to accept the content and metadata of your OneLake data lake files.
 
-1. [Create or update an index](/rest/api/searchservice/create-index) to define search fields that store file content and metadata:
+1. [Create or update an index](/rest/api/searchservice/indexes/create) to define search fields that store file content and metadata:
 
     ```http
     {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLakeファイルのインデックス作成リンクの修正"
}
```

### Explanation
この変更は、「search-how-to-index-onelake-files.md」という文書に対する修正です。合計2つの変更があり、1つの行が追加され、1つの行が削除されています。この修正の主な目的は、OneLakeデータ湖ファイル用のインデックス作成APIリンクを最新のものに更新することです。

具体的には、インデックスの作成または更新に関連するリンクが「/rest/api/searchservice/create-index」から「/rest/api/searchservice/indexes/create」に変更されました。このリンクの更新により、ユーザーは正確なインデックス作成APIドキュメントにアクセスし、一貫した手順でファイルのコンテンツやメタデータを保存するための検索フィールドを定義できるようになります。

この修正は、Azure Searchを使用してOneLakeファイルをインデクシングする際のドキュメントの明確性を高め、ユーザーが適切に操作を理解できるようにすることを意図しています。全体として、ドキュメントの正確性や信頼性を向上させるための重要な変更です。

## articles/search/search-howto-complex-data-types.md{#item-75a002}

<details>
<summary>Diff</summary>
````diff
@@ -69,7 +69,7 @@ This limit applies only to complex collections, and not complex types (like Addr
 
 ## Create complex fields
 
-As with any index definition, you can use the portal, [REST API](/rest/api/searchservice/create-index), or [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindex) to create a schema that includes complex types. 
+As with any index definition, you can use the portal, [REST API](/rest/api/searchservice/indexes/create), or [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindex) to create a schema that includes complex types. 
 
 Other Azure SDKs provide samples in [Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/samples/sample_index_crud_operations.py), [Java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateIndexExample.java), and [JavaScript](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/samples/v11/javascript/indexOperations.js).
 
@@ -89,7 +89,7 @@ Other Azure SDKs provide samples in [Python](https://github.com/Azure/azure-sdk-
 
 ### [**REST**](#tab/complex-type-rest)
 
-Use [Create Index (REST API)](/rest/api/searchservice/create-index) to define a schema.
+Use [Create Index (REST API)](/rest/api/searchservice/indexes/create) to define a schema.
 
 The following example shows a JSON index schema with simple fields, collections, and complex types. Notice that within a complex type, each subfield has a type and can have attributes, just as top-level fields do. The schema corresponds to the example data above. `Address` is a complex field that isn't a collection (a hotel has one address). `Rooms` is a complex collection field (a hotel has many rooms).
 
@@ -218,7 +218,7 @@ Fields must be marked as Retrievable in the index if you want them in search res
 
 ## Filter, facet, and sort complex fields
 
-The same [OData path syntax](query-odata-filter-orderby-syntax.md) used for filtering and fielded searches can also be used for faceting, sorting, and selecting fields in a search request. For complex types, rules apply that govern which subfields can be marked as sortable or facetable. For more information on these rules, see the [Create Index API reference](/rest/api/searchservice/create-index).
+The same [OData path syntax](query-odata-filter-orderby-syntax.md) used for filtering and fielded searches can also be used for faceting, sorting, and selecting fields in a search request. For complex types, rules apply that govern which subfields can be marked as sortable or facetable. For more information on these rules, see the [Create Index API reference](/rest/api/searchservice/indexes/create).
 
 ### Faceting subfields
 
@@ -242,7 +242,7 @@ To filter on a complex collection field, you can use a **lambda expression** wit
 
 > `$filter=Rooms/any(room: room/Type eq 'Deluxe Room') and Rooms/all(room: not room/SmokingAllowed)`
 
-As with top-level simple fields, simple subfields of complex fields can only be included in filters if they have the **filterable** attribute set to `true` in the index definition. For more information, see the [Create Index API reference](/rest/api/searchservice/create-index).
+As with top-level simple fields, simple subfields of complex fields can only be included in filters if they have the **filterable** attribute set to `true` in the index definition. For more information, see the [Create Index API reference](/rest/api/searchservice/indexes/create).
 
 Azure Search has the limitation that the complex objects in the collections across a single document cannot exceed 3000.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "複雑なデータ型に関するインデックス作成リンクの修正"
}
```

### Explanation
この変更は、「search-howto-complex-data-types.md」というドキュメントに関する修正です。合計で8つの変更があり、4つの行が追加され、4つの行が削除されています。この修正の主な目的は、複雑なデータ型を使用する際のインデックス作成に関するAPIリンクを更新することです。

具体的には、インデックスの作成に関連する過去のリンク「/rest/api/searchservice/create-index」が新しいリンク「/rest/api/searchservice/indexes/create」に変更されました。この更新により、ユーザーは正確で最新のAPIを使用してインデックスを作成し、複雑なデータ型のスキーマを定義できるようになります。

他にも、複雑なフィールド作成やODataパス構文を用いたフィルタリング、ファセット化、ソートについての説明が盛り込まれています。この修正は、Azure Searchを使用する際にユーザーが複雑なデータ型を扱う方法をより理解しやすくし、APIの正確な使用を促進することを目的としています。全体として、ドキュメントの信頼性や使いやすさを向上させる重要な変更です。

## articles/search/search-howto-connecting-azure-sql-database-to-azure-search-using-indexers.md{#item-0033f1}

<details>
<summary>Diff</summary>
````diff
@@ -85,7 +85,7 @@ The data source definition specifies the data to index, credentials, and policie
 
 In a [search index](search-what-is-an-index.md), add fields that correspond to the fields in SQL database. Ensure that the search index schema is compatible with source schema by using [equivalent data types](#TypeMapping).
 
-1. [Create or update an index](/rest/api/searchservice/create-index) to define search fields that will store data:
+1. [Create or update an index](/rest/api/searchservice/indexes/create) to define search fields that will store data:
 
     ```http
     POST https://[service name].search.windows.net/indexes?api-version=2024-07-01
@@ -182,7 +182,7 @@ An indexer runs automatically when it's created. You can prevent this by setting
 
 ## Check indexer status
 
-To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/get-indexer-status) request:
+To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) request:
 
 ```http
 GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2024-07-01
@@ -272,7 +272,7 @@ api-key: admin-key
 When using SQL integrated change tracking policy, don't specify a separate data deletion detection policy. The SQL integrated change tracking policy has built-in support for identifying deleted rows. However, for the deleted rows to be detected automatically, the document key in your search index must be the same as the primary key in the SQL table. 
 
 > [!NOTE]  
-> When using [TRUNCATE TABLE](/sql/t-sql/statements/truncate-table-transact-sql) to remove a large number of rows from a SQL table, the indexer needs to be [reset](/rest/api/searchservice/reset-indexer) to reset the change tracking state to pick up row deletions.
+> When using [TRUNCATE TABLE](/sql/t-sql/statements/truncate-table-transact-sql) to remove a large number of rows from a SQL table, the indexer needs to be [reset](/rest/api/searchservice/indexers/reset) to reset the change tracking state to pick up row deletions.
 
 <a name="HighWaterMarkPolicy"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure SQL DatabaseとAzure Searchの接続に関するリンク修正"
}
```

### Explanation
この変更は、「search-howto-connecting-azure-sql-database-to-azure-search-using-indexers.md」という文書に対する修正です。合計で6つの変更があり、3つの行が追加され、3つの行が削除されています。この修正の主な目的は、Azure SQL DatabaseとAzure Searchを接続する際に使用するインデックスおよびインデクサーに関するAPIリンクを最新のものに更新することです。

具体的には、以下の重要なリンクが変更されました：
- インデックスの作成に関するリンクが「/rest/api/searchservice/create-index」から「/rest/api/searchservice/indexes/create」へ変更され、
- インデクサーのステータスをチェックするためのリンクが「/rest/api/searchservice/get-indexer-status」から「/rest/api/searchservice/indexers/get-status」へ変更され、
- インデクサーをリセットするためのリンクが「/rest/api/searchservice/reset-indexer」から「/rest/api/searchservice/indexers/reset」へ変更されました。

これらの変更により、ユーザーは最新のAPIエンドポイントにアクセスし、正確な手順でAzure SQL DatabaseとAzure Searchのインデクサーを管理できるようになります。全体として、ドキュメントの整合性や信頼性を高めるための重要な更新です。

## articles/search/search-howto-create-indexers.md{#item-122450}

<details>
<summary>Diff</summary>
````diff
@@ -147,7 +147,7 @@ Indexers also require a search index. Recall that indexers pass data off to the
 
    Indexers can automatically map source fields to target index fields when the names and types are equivalent. If a field can't be implicitly mapped, remember that you can [define an explicit field mapping](search-indexer-field-mappings.md) that tells the indexer how to route the content.
 
-1. Review the analyzer assignments on each field. Analyzers can transform strings. As such, indexed strings might be different from what you passed in. You can evaluate the effects of analyzers using [Analyze Text (REST)](/rest/api/searchservice/test-analyzer). For more information about analyzers, see [Analyzers for text processing](search-analyzers.md).
+1. Review the analyzer assignments on each field. Analyzers can transform strings. As such, indexed strings might be different from what you passed in. You can evaluate the effects of analyzers using [Analyze Text (REST)](/rest/api/searchservice/indexes/analyze). For more information about analyzers, see [Analyzers for text processing](search-analyzers.md).
 
 During indexing, an indexer only checks field names and types. There's no validation step that ensures incoming content is correct for the corresponding search field in the index.
 
@@ -171,7 +171,7 @@ When you're ready to create an indexer on a remote search service, you need a se
 
 ### [**REST**](#tab/indexer-rest)
 
-Visual Studio Code with a REST client can send indexer requests. Using the app, you can connect to your search service and send [Create Indexer (REST)](/rest/api/searchservice/indexers/create) or [Update indexer](/rest/api/searchservice/update-indexer) requests. 
+Visual Studio Code with a REST client can send indexer requests. Using the app, you can connect to your search service and send [Create Indexer (REST)](/rest/api/searchservice/indexers/create) or [Update indexer](/rest/api/searchservice/indexers/create-or-update) requests. 
 
 ```http
 POST /indexers?api-version=[api-version]
@@ -243,7 +243,7 @@ Change detection logic is built into the data platforms. How an indexer supports
 
 Indexers keep track of the last document it processed from the data source through an internal *high water mark*. The marker is never exposed in the API, but internally the indexer keeps track of where it stopped. When indexing resumes, either through a scheduled run or an on-demand invocation, the indexer references the high water mark so that it can pick up where it left off.
 
-If you need to clear the high water mark to reindex in full, you can use [Reset Indexer](/rest/api/searchservice/reset-indexer). For more selective reindexing, use [Reset Skills](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2024-05-01-preview&preserve-view=true) or [Reset Documents](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2024-05-01-preview&preserve-view=true). Through the reset APIs, you can clear internal state, and also flush the cache if you enabled [incremental enrichment](search-howto-incremental-index.md). For more background and comparison of each reset option, see [Run or reset indexers, skills, and documents](search-howto-run-reset-indexers.md).
+If you need to clear the high water mark to reindex in full, you can use [Reset Indexer](/rest/api/searchservice/indexers/reset). For more selective reindexing, use [Reset Skills](/rest/api/searchservice/skillsets/reset-skills?view=rest-searchservice-2024-05-01-preview&preserve-view=true) or [Reset Documents](/rest/api/searchservice/indexers/reset-docs?view=rest-searchservice-2024-05-01-preview&preserve-view=true). Through the reset APIs, you can clear internal state, and also flush the cache if you enabled [incremental enrichment](search-howto-incremental-index.md). For more background and comparison of each reset option, see [Run or reset indexers, skills, and documents](search-howto-run-reset-indexers.md).
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーに関するAPIリンクの修正"
}
```

### Explanation
この変更は、「search-howto-create-indexers.md」という文書に対する修正です。合計で6つの変更があり、3つの行が追加され、3つの行が削除されています。この修正の主な目的は、Azureのインデクサーに関連するAPIリンクを最新のものに更新することです。

具体的には、以下のリンクが修正されました：
- テキストを分析する際のリンクが「/rest/api/searchservice/test-analyzer」から「/rest/api/searchservice/indexes/analyze」へ変更され、これにより最新の分析エンドポイントが反映されました。
- インデクサーを作成する際のリンクが「/rest/api/searchservice/update-indexer」から「/rest/api/searchservice/indexers/create-or-update」に変更されました。
- インデクサーのリセットに関するリンクが「/rest/api/searchservice/reset-indexer」から「/rest/api/searchservice/indexers/reset」へと更新され、より正確な情報となりました。

これらの変更は、ユーザーが最新のAPIエンドポイントを利用してインデクサーの設定や操作を行う際に役立ちます。全体として、ドキュメントの一貫性と信頼性を向上させるための重要な更新です。

## articles/search/search-howto-dotnet-sdk.md{#item-1ad98a}

<details>
<summary>Diff</summary>
````diff
@@ -295,7 +295,7 @@ Whether you use the basic `SearchField` API or either one of the helper models,
 
 #### Adding field attributes
 
-Notice how each field is decorated with attributes such as `IsFilterable`, `IsSortable`, `IsKey`, and `AnalyzerName`. These attributes map directly to the [corresponding field attributes in an Azure AI Search index](/rest/api/searchservice/create-index). The `FieldBuilder` class uses these properties to construct field definitions for the index.
+Notice how each field is decorated with attributes such as `IsFilterable`, `IsSortable`, `IsKey`, and `AnalyzerName`. These attributes map directly to the [corresponding field attributes in an Azure AI Search index](/rest/api/searchservice/indexes/create). The `FieldBuilder` class uses these properties to construct field definitions for the index.
 
 #### Field type mapping
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchインデックスに関するAPIリンク修正"
}
```

### Explanation
この変更は、「search-howto-dotnet-sdk.md」という文書に対する修正です。合計で2つの変更があり、1つの行が追加され、1つの行が削除されています。この修正の主な目的は、Azure AI Searchインデックスに関連するAPIリンクを最新のものに更新することです。

具体的には、Azure AI Searchにおけるフィールド属性を設定する際のリンクが変更されました。修正前は「/rest/api/searchservice/create-index」であり、修正後は「/rest/api/searchservice/indexes/create」へ変更されました。これにより、ユーザーがインデックスを作成する際の正しいAPIエンドポイントにアクセスできるようになります。

この変更は、文書の精度を向上させ、ユーザーが正しい情報に基づいてAzure AI Searchインデックスを操作できるようにするための重要な更新です。

## articles/search/search-howto-incremental-index.md{#item-d98619}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.date: 06/25/2024
 # Enable caching for incremental enrichment in Azure AI Search
 
 > [!IMPORTANT] 
-> This feature is in public preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [preview REST API](/rest/api/searchservice/index-preview) supports this feature.
+> This feature is in public preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). [Preview REST APIs](/rest/api/searchservice/index-preview) support this feature.
 
 This article explains how to add caching to an enrichment pipeline so that you can modify downstream enrichment steps without having to rebuild in full every time. By default, a skillset is stateless, and changing any part of its composition requires a full rerun of the indexer. With an [**enrichment cache**](cognitive-search-incremental-indexing-conceptual.md), the indexer can determine which parts of the document tree must be refreshed based on changes detected in the skillset or indexer definitions. Existing processed output is preserved and reused wherever possible. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インクリメンタルインデックスのプレビューAPIに関する表現の修正"
}
```

### Explanation
この変更は、「search-howto-incremental-index.md」という文書に対する修正です。合計で2つの変更があり、1つの行が追加され、1つの行が削除されています。この修正の主な目的は、インクリメンタルインデックス機能に関連する表現を明確にすることです。

具体的には、「プレビューREST API」への言及が修正されました。修正前は「The [preview REST API](/rest/api/searchservice/index-preview) supports this feature.」となっていたのが、修正後には「[Preview REST APIs](/rest/api/searchservice/index-preview) support this feature.」に変更されました。この修正により、APIが複数あることが示唆され、文書の情報がより正確になります。

この変更は、ユーザーがインクリメンタルインデックス機能に関する最新のと正確な情報を理解しやすくするための重要な更新です。

## articles/search/search-howto-index-azure-data-lake-storage.md{#item-c21e43}

<details>
<summary>Diff</summary>
````diff
@@ -143,7 +143,7 @@ Indexers can connect to a blob container using the following connections.
 
 In a [search index](search-what-is-an-index.md), add fields to accept the content and metadata of your Azure blobs.
 
-1. [Create or update an index](/rest/api/searchservice/create-index) to define search fields that will store blob content and metadata:
+1. [Create or update an index](/rest/api/searchservice/indexes/create) to define search fields that will store blob content and metadata:
 
     ```http
     {
@@ -227,7 +227,7 @@ An indexer runs automatically when it's created. You can prevent this by setting
 
 ## Check indexer status
 
-To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/get-indexer-status) request:
+To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) request:
 
 ```http
 GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Blobストレージのインデックス設定に関するAPIリンクの修正"
}
```

### Explanation
この変更は、「search-howto-index-azure-data-lake-storage.md」という文書に対する修正です。合計で4つの変更があり、2つの行が追加され、2つの行が削除されています。この修正の主な目的は、Azure Blobストレージをインデックス設定する際のAPIリンクを正確に更新することです。

具体的には、2つの主要なAPIエンドポイントが修正されました。最初の修正では、「create-index」に関するリンクが「/rest/api/searchservice/create-index」から「/rest/api/searchservice/indexes/create」に変更されました。次に、インデックスのステータスをモニタリングするためのリンクも修正され、「Get Indexer Status」が「/rest/api/searchservice/get-indexer-status」から「/rest/api/searchservice/indexers/get-status」へ変更されました。

これにより、ユーザーが正確なAPIエンドポイントにアクセスできるようになり、Azure Blobストレージのインデックスを正しく設定するための情報が向上します。この変更は、利用者が最新の情報をもとに作業できるようにするために重要です。

## articles/search/search-howto-index-changed-deleted-blobs.md{#item-32a688}

<details>
<summary>Diff</summary>
````diff
@@ -90,7 +90,7 @@ api-key: [admin key]
 }
 ```
 
-[Run the indexer](/rest/api/searchservice/run-indexer) or set the indexer to run [on a schedule](search-howto-schedule-indexers.md). When the indexer runs and processes a blob having a soft delete state, the corresponding search document will be removed from the index.
+[Run the indexer](/rest/api/searchservice/indexers/run) or set the indexer to run [on a schedule](search-howto-schedule-indexers.md). When the indexer runs and processes a blob having a soft delete state, the corresponding search document will be removed from the index.
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "変更された削除済みBlobのインデックス手順におけるAPIリンクの修正"
}
```

### Explanation
この変更は、「search-howto-index-changed-deleted-blobs.md」という文書に対する修正です。合計で2つの変更があり、1つの行が追加され、1つの行が削除されています。この修正の主な目的は、削除されたBlobに関連するインデックス操作に関するAPIリンクを最新のものに更新することです。

具体的には、インデックスの実行に関するリンクが変更されました。修正前は「[Run the indexer](/rest/api/searchservice/run-indexer)」という記述がありましたが、修正後は「[Run the indexer](/rest/api/searchservice/indexers/run)」に変更されました。この変更により、正しいAPIエンドポイントへのリンクが提供され、ユーザーがインデックスを実行する際に最新の情報を利用できるようになります。

この変更は、削除されたBlobを扱うインデクシングプロセスにおいて、正確ではっきりとした指示を提供するために重要です。

## articles/search/search-howto-index-cosmosdb.md{#item-568fab}

<details>
<summary>Diff</summary>
````diff
@@ -160,7 +160,7 @@ SELECT DISTINCT VALUE c.name FROM c ORDER BY c.name
 
 In a [search index](search-what-is-an-index.md), add fields to accept the source JSON documents or the output of your custom query projection. Ensure that the search index schema is compatible with source data. For content in Azure Cosmos DB, your search index schema should correspond to the [Azure Cosmos DB items](/azure/cosmos-db/resource-model#azure-cosmos-db-items) in your data source.
 
-1. [Create or update an index](/rest/api/searchservice/create-index) to define search fields that store data:
+1. [Create or update an index](/rest/api/searchservice/indexes/create) to define search fields that store data:
 
     ```http
     POST https://[service name].search.windows.net/indexes?api-version=2024-07-01
@@ -240,7 +240,7 @@ An indexer runs automatically when it's created. You can prevent this by setting
 
 ## Check indexer status
 
-To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/get-indexer-status) request:
+To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) request:
 
 ```http
 GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Cosmos DBのインデックス設定に関するAPIリンクの修正"
}
```

### Explanation
この変更は、「search-howto-index-cosmosdb.md」という文書に対する修正です。合計で4つの変更があり、2つの行が追加され、2つの行が削除されています。この修正の主な目的は、Azure Cosmos DBに関連するインデックス設定の手順におけるAPIリンクを正確に更新することです。

具体的には、2つの異なるAPIエンドポイントが修正されました。最初の修正では、インデックスの作成や更新に関するリンクが「[Create or update an index](/rest/api/searchservice/create-index)」から「[Create or update an index](/rest/api/searchservice/indexes/create)」に変更されました。これにより、正確なエンドポイントに誘導されることになります。

次に、インデクサーのステータスを監視するためのリンクも修正され、「Get Indexer Status」が「/rest/api/searchservice/get-indexer-status」から「/rest/api/searchservice/indexers/get-status」へ変更されました。この変更は、ユーザーが適切なAPIエンドポイントにアクセスできることを保証し、Azure Cosmos DBのデータに基づく検索インデックスの管理を円滑に行えるようにします。

これにより、文書全体の正確性が向上し、利用者が最新の情報をもとにAzure Cosmos DBを扱う際の手順が明確になります。

## articles/search/search-howto-indexing-azure-tables.md{#item-7655b0}

<details>
<summary>Diff</summary>
````diff
@@ -112,15 +112,15 @@ To avoid a full scan, you can use table partitions to narrow the scope of each i
 
   + In the data source definition, specify a query similar to the following example: `(PartitionKey ge <TimeStamp>) and (other filters)`. 
 
-  + Monitor indexer progress by using [Get Indexer Status API](/rest/api/searchservice/get-indexer-status), and periodically update the `<TimeStamp>` condition of the query based on the latest successful high-water-mark value. 
+  + Monitor indexer progress by using [Get Indexer Status API](/rest/api/searchservice/indexers/get-status), and periodically update the `<TimeStamp>` condition of the query based on the latest successful high-water-mark value. 
 
   + With this approach, if you need to trigger a full reindex, reset the data source query in addition to [resetting the indexer](search-howto-run-reset-indexers.md). 
 
 ## Add search fields to an index
 
 In a [search index](search-what-is-an-index.md), add fields to accept the content and metadata of your table entities.
 
-1. [Create or update an index](/rest/api/searchservice/create-index) to define search fields that will store content from entities:
+1. [Create or update an index](/rest/api/searchservice/indexes/create) to define search fields that will store content from entities:
 
     ```http
     POST https://[service name].search.windows.net/indexes?api-version=2024-07-01 
@@ -199,7 +199,7 @@ An indexer runs automatically when it's created. You can prevent this by setting
 
 ## Check indexer status
 
-To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/get-indexer-status) request:
+To monitor the indexer status and execution history, send a [Get Indexer Status](/rest/api/searchservice/indexers/get-status) request:
 
 ```http
 GET https://myservice.search.windows.net/indexers/myindexer/status?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Tablesのインデックス設定に関するAPIリンクの修正"
}
```

### Explanation
この変更は、「search-howto-indexing-azure-tables.md」という文書に対する修正です。合計で6つの変更があり、3つの行が追加され、3つの行が削除されています。この修正の主な目的は、Azure Tablesに関連するインデックス設定の手順内のAPIリンクを正確に更新し、最新の情報を反映させることです。

具体的には、まずインデクサーの進捗状況を監視するためのAPIリンクが修正されました。「[Get Indexer Status API](/rest/api/searchservice/get-indexer-status)」から「[Get Indexer Status API](/rest/api/searchservice/indexers/get-status)」に変更され、ユーザーが正しいAPIエンドポイントにアクセスできるようにしました。

また、インデックスの作成または更新に関するリンクも修正され、「[Create or update an index](/rest/api/searchservice/create-index)」が「[Create or update an index](/rest/api/searchservice/indexes/create)」に変更されました。この変更により、正確なエンドポイントが提供され、ユーザーはインデックスの作成時に正しい情報を得られます。

これらの修正は、文書の正確性を向上させるとともに、Azure Tablesを使用して情報を検索する際のユーザー体験を向上させるために重要です。また、インデクサーのステータスを適切に監視し、必要なアップデートを行う手順が明確になります。

## articles/search/search-howto-move-across-regions.md{#item-bcecf6}

<details>
<summary>Diff</summary>
````diff
@@ -57,132 +57,4 @@ The following links can help you locate more information when completing the ste
 + [Choose a tier](search-sku-tier.md)
 + [Create a search service](search-create-service-portal.md)
 + [Load search documents](search-what-is-data-import.md)
-+ [Enable logging](monitor-azure-cognitive-search.md)
-
-
-<!-- To move your Azure AI services account from one region to another, you will create an export template to move your subscription(s). After moving your subscription, you will need to move your data and recreate your service.
-
-In this article, you'll learn how to:
-
-> [!div class="checklist"]
-> * Export a template.
-> * Modify the template: adding the target region, search and storage account names.
-> * Deploy the template to create the new search and storage accounts.
-> * Verify your service status in the new region
-> * Clean up resources in the source region.
-
-## Prerequisites
-
-- Ensure that the services and features that your account uses are supported in the target region.
-
-- For preview features, ensure that your subscription is allowlisted for the target region. For more information about preview features, see [knowledge stores](./knowledge-store-concept-intro.md), [incremental enrichment](./cognitive-search-incremental-indexing-conceptual.md), and [private endpoint](./service-create-private-endpoint.md).
-
-## Assessment and planning
-
-When you move your search service to the new region, you will need to [move your data to the new storage service](../storage/common/storage-account-move.md?tabs=azure-portal#configure-the-new-storage-account) and then rebuild your indexes, skillsets and knowledge stores. You should record current settings and copy json files to make the rebuilding of your service easier and faster.
-
-## Moving your search service's resources
-
-To start you will export and then modify a Resource Manager template.
-
-### Export a template
-
-1. Sign in to the [Azure portal](https://portal.azure.com).
-
-2. Go to your Resource Group page.
-
-> [!div class="mx-imgBorder"]
-> ![Resource Group page example](./media/search-move-resource/export-template-sample.png)
-
-3. Select **All resources**.
-
-3. In the left hand navigation menu select **Export template**.
-
-4. Choose **Download** in the **Export template** page.
-
-5. Locate the .zip file that you downloaded from the portal, and unzip that file to a folder of your choice.
-
-The zip file contains the .json files that comprise the template and scripts to deploy the template.
-
-### Modify the template
-
-You will modify the template by changing the search and storage account names and regions. The names must follow the rules for each service and region naming conventions. 
-
-To obtain region location codes, see [Azure Locations](https://azure.microsoft.com/global-infrastructure/locations/).  The code for a region is the region name with no spaces, **Central US** = **centralus**.
-
-1. In the Azure portal, select **Create a resource**.
-
-2. In **Search the Marketplace**, type **template deployment**, and then press **ENTER**.
-
-3. Select **Template deployment**.
-
-4. Select **Create**.
-
-5. Select **Build your own template in the editor**.
-
-6. Select **Load file**, and then follow the instructions to load the **template.json** file that you downloaded and unzipped in the previous section.
-
-7. In the **template.json** file, name the target search and storage accounts by setting the default value of the search and storage account names. 
-
-8. Edit the **location** property in the **template.json** file to the target region for both your search and storage services. This example sets the target region to `centralus`.
-
-```json
-},
-    "variables": {},
-    "resources": [
-        {
-            "type": "Microsoft.Search/searchServices",
-            "apiVersion": "2020-03-13",
-            "name": "[parameters('searchServices_target_region_search_name')]",
-            "location": "centralus",
-            "sku": {
-                "name": "standard"
-            },
-            "properties": {
-                "replicaCount": 1,
-                "partitionCount": 1,
-                "hostingMode": "Default"
-            }
-        },
-        {
-            "type": "Microsoft.Storage/storageAccounts",
-            "apiVersion": "2019-06-01",
-            "name": "[parameters('storageAccounts_tagetstorageregion_name')]",
-            "location": "centralus",
-            "sku": {
-                "name": "Standard_RAGRS",
-                "tier": "Standard"
-            },
-```
-
-### Deploy the template
-
-1. Save the **template.json** file.
-
-2. Enter or select the property values:
-
-- **Subscription**: Select an Azure subscription.
-
-- **Resource group**: Select **Create new** and give the resource group a name.
-
-- **Location**: Select an Azure location.
-
-3. Click the **I agree to the terms and conditions stated above** checkbox, and then click the **Select Purchase** button.
-
-## Verifying your services' status in new region
-
-To verify the move, open the new resource group and your services will be listed with the new region.
-
-To move your data from your source region to the target region, please see this article's guidelines for [moving your data to the new storage account](../storage/common/storage-account-move.md?tabs=azure-portal#move-data-to-the-new-storage-account).
-
-## Clean up resources in your original region
-
-To commit the changes and complete the move of your service account, delete the source service account.
-
-## Next steps
-
-[Create an index](./search-get-started-portal.md)
-
-[Create a skillset](./cognitive-search-quickstart-blob.md)
-
-[Create a knowledge store](./knowledge-store-create-portal.md) -->
++ [Enable logging](monitor-azure-cognitive-search.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azure地域間移動ガイドの内容大幅削除"
}
```

### Explanation
この変更は、「search-howto-move-across-regions.md」という文書において、大幅な編集が行われました。具体的には、129行が削除され、1行が追加され、合計で130の変更が行われています。

主要な変更内容は、Azure AIサービスを異なる地域に移動するプロセスに関連する詳細な手順が削除されたことです。削除された内容には、エクスポートテンプレートの作成、テンプレートの修正、新サービスのデプロイ、サービス移動後の確認手順、データ移動とリソースのクリーンアップに関する具体的な指示が含まれていました。これにより、ユーザーは移動プロセスに必要な詳細情報を得ることができなくなります。

この大幅な削除は、情報が整理され、もしくは他の関連文書に取り込まれる準備の一環として行われた可能性があります。新たに追加された行は、ログの有効化に関するリンク「[Enable logging](monitor-azure-cognitive-search.md)」であり、これにより一部機能や手順が引き続き利用可能であることを示唆しています。

全体として、この変更は情報の大幅な簡略化を示しており、ユーザーが地域間でのサービス移動に関する具体的な手順を探す際には、その他の資料やドキュメントを参照する必要があることを意味しています。

## articles/search/search-howto-powerapps.md{#item-92d1c0}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: tutorial
-ms.date: 02/21/2024
+ms.date: 09/18/2024
 ---
 
 # Tutorial: Query an Azure AI Search index from Power Apps
@@ -38,7 +38,7 @@ A connector in Power Apps is a data source connection. In this step, create a cu
 
 1. [Sign in](https://make.powerapps.com) to Power Apps.
 
-1. On the left, expand **... More**. Find, pin, and then select **Custom Connectors**.
+1. On the left, select **Custom Connectors**.
 
     :::image type="content" source="./media/search-howto-powerapps/1-2-custom-connector.png" alt-text="Custom connector menu" border="true":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Power AppsにおけるAzure AI Searchインデックスのクエリ方法に関する文書の更新"
}
```

### Explanation
この変更は、「search-howto-powerapps.md」という文書に対して行われたもので、2行が追加され、2行が削除され、合計で4つの変更が行われています。 

主な変更点は、文書内の日付と手順の一部が更新されたことです。具体的には、ドキュメントの日付が「02/21/2024」から「09/18/2024」に変更されており、情報の更新を示しています。この日付変更は、文書が最近の内容に基づいていることを反映しています。

また、手順の一部が修正されました。以前の手順では「・・・Moreを展開して、**Custom Connectors**を探し、ピン止めした後に選択する」と記載されていましたが、更新後は単に「左側のメニューから**Custom Connectors**を選択する」と簡略化されています。この変更により、手順がより明確で簡単に理解できるものとなっています。

全体として、この更新は、Power Appsを使用してAzure AI Searchインデックスをクエリする方法についての文書の明確化と最新化を目的としており、ユーザーの利便性向上に寄与しています。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -120,7 +120,7 @@ Some modifications require an index drop and rebuild, replacing a current index
 | Action | Description |
 |-----------|-------------|
 | Delete a field | To physically remove all traces of a field, you have to rebuild the index. When an immediate rebuild isn't practical, you can modify application code to redirect access away from an obsolete field or use the [searchFields](search-query-create.md#example-of-a-full-text-query-request) and [select](search-query-odata-select.md) query parameters to choose which fields are searched and returned. Physically, the field definition and contents remain in the index until the next rebuild, when you apply a schema that omits the field in question. |
-| Change a field definition | Revisions to a field name, data type, or specific [index attributes](/rest/api/searchservice/create-index) (searchable, filterable, sortable, facetable) require a full rebuild. |
+| Change a field definition | Revisions to a field name, data type, or specific [index attributes](/rest/api/searchservice/indexes/create) (searchable, filterable, sortable, facetable) require a full rebuild. |
 | Assign an analyzer to a field | [Analyzers](search-analyzers.md) are defined in an index, assigned to fields, and then invoked during indexing to inform how tokens are created. You can add a new analyzer definition to an index at any time, but you can only *assign* an analyzer when the field is created. This is true for both the **analyzer** and **indexAnalyzer** properties. The **searchAnalyzer** property is an exception (you can assign this property to an existing field). |
 | Update or delete an analyzer definition in an index | You can't delete or change an existing analyzer configuration (analyzer, tokenizer, token filter, or char filter) in the index unless you rebuild the entire index. |
 | Add a field to a suggester | If a field already exists and you want to add it to a [Suggesters](index-add-suggesters.md) construct, rebuild the index. |
@@ -150,7 +150,7 @@ If indexing workloads introduce unacceptable levels of query latency, conduct [p
 
 ## Check for updates
 
-You can begin querying an index as soon as the first document is loaded. If you know a document's ID, the [Lookup Document REST API](/rest/api/searchservice/lookup-document) returns the specific document. For broader testing, you should wait until the index is fully loaded, and then use queries to verify the context you expect to see.
+You can begin querying an index as soon as the first document is loaded. If you know a document's ID, the [Lookup Document REST API](/rest/api/searchservice/documents/get) returns the specific document. For broader testing, you should wait until the index is fully loaded, and then use queries to verify the context you expect to see.
 
 You can use [Search Explorer](search-explorer.md) or a [REST client](search-get-started-rest.md) to check for updated content.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Reindexingに関する手順およびリンクの更新"
}
```

### Explanation
この変更は、「search-howto-reindex.md」という文書に対して行われたもので、2行が追加され、2行が削除され、合計で4つの変更が行われています。

主な変更内容は、いくつかの手順に関連する文言の修正と、特定のリンクの更新です。具体的には、フィールド定義の変更に関する説明文が更新され、以前は「[index attributes](/rest/api/searchservice/create-index)」となっていた部分が「[index attributes](/rest/api/searchservice/indexes/create)」に変更されました。この変更は、フィールドの属性を定義する際のAPIエンドポイントが変更されたことを反映しています。

また、ドキュメントの中の「Lookup Document REST API」に関連するリンクも更新されました。これまでは「[Lookup Document REST API](/rest/api/searchservice/lookup-document)」となっていましたが、「[Lookup Document REST API](/rest/api/searchservice/documents/get)」に変更されています。この変更は、特定のドキュメントを取得するためのREST APIの参照先が整理されたことを示しています。

全体として、この更新はドキュメント内の手順や情報の明確さを向上させるものであり、ユーザーがAzure Searchの再インデックスに関する操作をよりスムーズに行えるようにすることを目的としています。

## articles/search/search-import-data-portal.md{#item-b804d1}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ The wizard outputs the objects in the following table. After the objects are cre
 |--------|-------------|
 | [Indexer](/rest/api/searchservice/indexers/create)  | A configuration object specifying a data source, target index, an optional skillset, optional schedule, and optional configuration settings for error handing and base-64 encoding. |
 | [Data Source](/rest/api/searchservice/data-sources/create)  | Persists connection information to a [supported data source](search-indexer-overview.md#supported-data-sources) on Azure. A data source object is used exclusively with indexers. | 
-| [Index](/rest/api/searchservice/create-index) | Physical data structure used for full text search and other queries. | 
+| [Index](/rest/api/searchservice/indexes/create) | Physical data structure used for full text search and other queries. | 
 | [Skillset](/rest/api/searchservice/skillsets/create) | Optional. A complete set of instructions for manipulating, transforming, and shaping content, including analyzing and extracting information from image files. Skillsets are also used for integrated vectorization. Unless the volume of work fall under the limit of 20 transactions per indexer per day, the skillset must include a reference to an Azure AI multiservice resource that provides enrichment. For integrated vectorization, you can use either Azure AI Vision or an embedding model in the Azure AI Studio model catalog. | 
 | [Knowledge store](knowledge-store-concept-intro.md) | Optional. Stores output from in tables and blobs in Azure Storage for independent analysis or downstream processing in nonsearch scenarios. |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データポータルのインポートに関するリンクの更新"
}
```

### Explanation
この変更は、「search-import-data-portal.md」という文書に対して行われたもので、1行が追加され、1行が削除され、合計で2つの変更が行われています。

主な変更点は、異なるAPIエンドポイントに関連するリンクの修正です。具体的には、インデックスに関する記述が更新されました。以前は「[Index](/rest/api/searchservice/create-index)」というリンクでしたが、更新後は「[Index](/rest/api/searchservice/indexes/create)」に変更されています。この変更により、インデックス作成に関する参照が正しいAPIエンドポイントに更新され、最新の情報を反映しています。

このような変更は、ユーザーがデータポータルを通じてデータのインポートを実行する際に、正確で有用な情報を提供するため、ドキュメントの信頼性を高めることに寄与します。全体として、文書の内容が最新かつ正確であることが確認され、ユーザーにとって利便性が向上することを目的としています。

## articles/search/search-index-azure-sql-managed-instance-with-managed-identity.md{#item-a4ec86}

<details>
<summary>Diff</summary>
````diff
@@ -121,7 +121,7 @@ api-key: [admin key]
 
 The index specifies the fields in a document, attributes, and other constructs that shape the search experience.
 
-Here's a [Create Index](/rest/api/searchservice/create-index) REST API call with a searchable `booktitle` field:   
+Here's a [Create Index](/rest/api/searchservice/indexes/create) REST API call with a searchable `booktitle` field:   
 
 ```http
 POST https://[service name].search.windows.net/indexes?api-version=2020-06-30
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス作成に関するAPIエンドポイントのリンク更新"
}
```

### Explanation
この変更は、「search-index-azure-sql-managed-instance-with-managed-identity.md」という文書に対して行われたもので、1行が追加され、1行が削除され、合計で2つの変更が行われています。

主な変更点は、インデックス作成に関するREST APIのリンクが修正されたことです。具体的には、現行の文書では「[Create Index](/rest/api/searchservice/create-index)」というリンクが使用されていましたが、これが「[Create Index](/rest/api/searchservice/indexes/create)」に更新されました。この変更により、インデックス作成のためのAPIエンドポイントが正確で、新しい構造に適合したものになっています。

この修正は、ユーザーがAzure SQLの管理インスタンスにおいてインデックスを適切に作成する際の参照を最新の情報に更新し、正確さを確保することを目的としています。全体として、この変更は文書の整合性を維持し、ユーザーに対して効果的なガイダンスを提供するために重要です。

## articles/search/search-indexer-how-to-access-private-sql.md{#item-1bd4cc}

<details>
<summary>Diff</summary>
````diff
@@ -175,7 +175,7 @@ This article assumes a [REST client](search-get-started-rest.md) and uses the RE
 
 1. Run the indexer. If the indexer execution succeeds and the search index is populated, the shared private link is working.
 
-You can monitor the status of the indexer in Azure portal or by using the [Indexer Status API](/rest/api/searchservice/get-indexer-status).
+You can monitor the status of the indexer in Azure portal or by using the [Indexer Status API](/rest/api/searchservice/indexers/get-status).
 
 You can use [**Search explorer**](search-explorer.md) in Azure portal to check the contents of the index.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサのステータスAPIエンドポイントのリンク更新"
}
```

### Explanation
この変更は、「search-indexer-how-to-access-private-sql.md」という文書に対して行われたもので、1行が追加され、1行が削除され、合計で2つの変更が行われています。

具体的な変更内容は、インデクサのステータスを確認するためのAPIリンクが更新された点です。以前の文書では「[Indexer Status API](/rest/api/searchservice/get-indexer-status)」というリンクが使用されていましたが、これが「[Indexer Status API](/rest/api/searchservice/indexers/get-status)」に変更されました。この更新により、正確なAPIエンドポイントにリダイレクトされ、最新のアクセス方法をユーザーに提供します。

この修正は、ユーザーがAzureのポータル内でインデクサの状態を監視する際に、正しい情報を基に行動できるようにするための重要なステップです。全体として、この変更はドキュメントの整合性を保ち、ユーザーが効率的にインデクサの機能を利用できるようにすることを目指しています。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -368,7 +368,7 @@ This step shows you how to configure the indexer to run in the private environme
     }
     ```
 
-After the indexer is created successfully, it should connect to the Azure resource over the private endpoint connection. You can monitor the status of the indexer by using the [Indexer Status API](/rest/api/searchservice/get-indexer-status).
+After the indexer is created successfully, it should connect to the Azure resource over the private endpoint connection. You can monitor the status of the indexer by using the [Indexer Status API](/rest/api/searchservice/indexers/get-status).
 
 > [!NOTE]
 > If you already have existing indexers, you can update them via the [PUT API](/rest/api/searchservice/indexers/create) by setting the `executionEnvironment` to `private` or using the JSON editor in the portal.
@@ -414,7 +414,7 @@ After the indexer is created successfully, it should connect to the Azure resour
 
 + If your indexer creation fails with "Data source credentials are invalid," check the approval status of the shared private link before debugging the connection. If the status is `Approved`, check the `properties.provisioningState` property. If it's `Incomplete`, there might be a problem with underlying dependencies. In this case, reissue the `PUT` request to re-create the shared private link. You might also need to repeat the approval step.
 
-+ If indexers fail consistently or intermittently, check the [`executionEnvironment` property](/rest/api/searchservice/update-indexer) on the indexer. The value should be set to `private`. If you didn't set this property, and indexer runs succeeded in the past, it's because the search service used a private environment of its own accord. A search service moves processing out of the standard environment if the system is under load.
++ If indexers fail consistently or intermittently, check the [`executionEnvironment` property](/rest/api/searchservice/indexers/create-or-update) on the indexer. The value should be set to `private`. If you didn't set this property, and indexer runs succeeded in the past, it's because the search service used a private environment of its own accord. A search service moves processing out of the standard environment if the system is under load.
 
 + If you get an error when creating a shared private link, check [service limits](search-limits-quotas-capacity.md) to verify that you're under the quota for your tier.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサのステータスおよび関連APIリンクの更新"
}
```

### Explanation
この変更は、「search-indexer-howto-access-private.md」という文書に対して施されたもので、合計で4つの変更が行われています。具体的には、2行が追加され、2行が削除されています。

主な変更点は、インデクサのステータスを確認するためのAPIリンクの修正です。「[Indexer Status API](/rest/api/searchservice/get-indexer-status)」という旧リンクが「[Indexer Status API](/rest/api/searchservice/indexers/get-status)」に更新され、利用者が最新のAPIエンドポイントにアクセスできるようになりました。

また、新たに追加された情報では、インデクサの作成が失敗した場合や、インデクサが一貫して失敗する場合のチェックポイントが提供されています。これには、`executionEnvironment` プロパティやサービス制限の確認が含まれています。これにより、ユーザーはインデクサの問題をより迅速に特定し、修正できるようになります。

全体として、この変更は文書の正確性を向上させ、ユーザーがインデクサの設定やトラoubleshootingの手順を正しく理解できるようにすることを意図しています。

## articles/search/search-indexer-overview.md{#item-292796}

<details>
<summary>Diff</summary>
````diff
@@ -146,7 +146,7 @@ For more information, see [Create an indexer](search-howto-create-indexers.md)
 
 After the first indexer run, you can [rerun it on demand](search-howto-run-reset-indexers.md) or [set up a schedule](search-howto-schedule-indexers.md).
 
-You can monitor [indexer status in the portal](search-howto-monitor-indexers.md) or through [Get Indexer Status API](/rest/api/searchservice/get-indexer-status). You should also [run queries on the index](search-query-create.md) to verify the result is what you expected.
+You can monitor [indexer status in the portal](search-howto-monitor-indexers.md) or through [Get Indexer Status API](/rest/api/searchservice/indexers/get-status). You should also [run queries on the index](search-query-create.md) to verify the result is what you expected.
 
 Indexers don't have dedicated processing resources. Based on this, indexers' status may show as idle before running (depending on other jobs in the queue) and run times may not be predictable. Other factors define indexer performance as well, such as document size, document complexity, image analysis, among others.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサステータスAPIのリンク更新"
}
```

### Explanation
この変更は、「search-indexer-overview.md」という文書に対して行われたもので、合計で2つの変更があり、1行が追加され、1行が削除されました。

変更内容は主に、インデクサの状態を確認するためのAPIのリンクが更新されたことです。以前は「[Get Indexer Status API](/rest/api/searchservice/get-indexer-status)」というリンクが使用されていましたが、これが「[Get Indexer Status API](/rest/api/searchservice/indexers/get-status)」に変更されました。この更新により、正しいAPIエンドポイントが使用されることになります。

文書内の内容について、インデクサの状態を監視する方法や、結果が期待通りかどうかを確認するためにインデクサに対してクエリを実行する必要性についても言及されています。この変更は、ドキュメントの正確性を向上させ、ユーザーがインデクサの機能を正しく利用できるようにすることを目指しています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -86,28 +86,7 @@ Vector limits vary by service creation date and tier.
 
 + To check the age of your search service or learn more about vector indexes, see [Vector index size and staying under limits](vector-search-index-size.md).
 
-+ To view the vector quota in effect for your search service, use [GET Service Statistics](/rest/api/searchservice/get-service-statistics), or check the **Properties** and **Usage** tabs for your search service in the Azure portal.
-
-#### Storage quota (GB)
-
-This table repeats [partition storage limits](#service-limits) for context. The table shows the progression of storage quota increases in GB over time. Vector quota is per partition, so the increase in vector quota is bound to the increase in per-partition storage for each tier. 
-
-Higher capacity partitions were brought online starting in April 2024. Standard 3 (S3) and Standard 3 High Density (S3HD) have the same storage and partition limits.
-
-| Service creation date |Basic | S1| S2 | S3/HD | L1 | L2 |
-|-----------------------|------|---|----|----|----|----|
-|**Before July 1, 2023** <sup>1</sup> | 2  | 25 | 100 | 200 | 1,024 | 2,048 |
-|**July 1, 2023 through April 3, 2024** <sup>2</sup>| 2  | 25 | 100 | 200 | 1,024 | 2,048 |
-|**April 3, 2024 through May 17, 2024** <sup>3</sup> | 15  | 160 | 512 | 1,024 | 1,024 | 2,048 |
-|**After May 17, 2024** <sup>4</sup> | 15  | 160 | 512 | 1,024 | 2,048 | 4,096 |
-
-<sup>1</sup> Partition sizes during early preview.
-
-<sup>2</sup> No change during the later preview period.
-
-<sup>3</sup> Higher capacity storage for Basic, S1, S2, S3 in the following regions. **Americas**: Brazil South​, Canada Central​, Canada East​​, East US​, East US 2, ​Central US​, North Central US​, South Central US​, West US​, West US 2​, West US 3​, West Central US. **Europe**: France Central​. Italy North​​, North Europe​​, Norway East, Poland Central​​, Switzerland North​, Sweden Central​, UK South​, UK West​. **Middle East**:  UAE North. **Africa**: South Africa North. **Asia Pacific**: Australia East​, Australia Southeast​​, Central India, Jio India West​, East Asia, Southeast Asia​, Japan East, Japan West​, Korea Central, Korea South​.
-
-<sup>4</sup> Higher capacity storage for more tiers and more regions. **Europe**: Germany North​, Germany West Central, Switzerland West​. **Azure Government**: Texas, Arizona, Virginia. **Africa**: South Africa North​. **Asia Pacific**: China North 3, China East 3.
++ To view the vector quota in effect for your search service, use [GET Service Statistics](/rest/api/searchservice/get-service-statistics/get-service-statistics), or check the **Properties** and **Usage** tabs for your search service in the Azure portal.
 
 #### Vector quota per partition (GB)
 
@@ -128,6 +107,27 @@ This table shows the progression of vector quota increases in GB over time. The
 
 <sup>4</sup> Higher vector quota for more tiers and regions based on partition size updates.
 
+#### Partition limits (GB)
+
+This table repeats [partition storage limits](#service-limits) for context. The table shows the progression of storage quota increases in GB over time. Vector quota is per partition, so the more significant increases in vector quota that occurred starting in April 2024 correspond to the increases in per-partition storage occuring at the same time. 
+
+Higher capacity partitions were brought online starting in April 2024.
+
+| Service creation date |Basic | S1| S2 | S3/HD | L1 | L2 |
+|-----------------------|------|---|----|----|----|----|
+|**Before July 1, 2023** <sup>1</sup> | 2  | 25 | 100 | 200 | 1,024 | 2,048 |
+|**July 1, 2023 through April 3, 2024** <sup>2</sup>| 2  | 25 | 100 | 200 | 1,024 | 2,048 |
+|**April 3, 2024 through May 17, 2024** <sup>3</sup> | 15  | 160 | 512 | 1,024 | 1,024 | 2,048 |
+|**After May 17, 2024** <sup>4</sup> | 15  | 160 | 512 | 1,024 | 2,048 | 4,096 |
+
+<sup>1</sup> Partition sizes during early preview.
+
+<sup>2</sup> No change during the later preview period.
+
+<sup>3</sup> Higher capacity storage for Basic, S1, S2, S3 in these regions. **Americas**: Brazil South​, Canada Central​, Canada East​​, East US​, East US 2, ​Central US​, North Central US​, South Central US​, West US​, West US 2​, West US 3​, West Central US. **Europe**: France Central​. Italy North​​, North Europe​​, Norway East, Poland Central​​, Switzerland North​, Sweden Central​, UK South​, UK West​. **Middle East**:  UAE North. **Africa**: South Africa North. **Asia Pacific**: Australia East​, Australia Southeast​​, Central India, Jio India West​, East Asia, Southeast Asia​, Japan East, Japan West​, Korea Central, Korea South​.
+
+<sup>4</sup> Higher capacity storage for more tiers and more regions. **Europe**: Germany North​, Germany West Central, Switzerland West​. **Azure Government**: Texas, Arizona, Virginia. **Africa**: South Africa North​. **Asia Pacific**: China North 3, China East 3.
+
 ## Indexer limits
 
 Maximum running times exist to provide balance and stability to the service as a whole, but larger data sets might need more indexing time than the maximum allows. If an indexing job can't complete within the maximum time allowed, try running it on a schedule. The scheduler keeps track of indexing status. If a scheduled indexing job is interrupted for any reason, the indexer can pick up where it last left off at the next scheduled run.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルクォータとパーティション制限に関する情報の更新"
}
```

### Explanation
この変更は、「search-limits-quotas-capacity.md」という文書に対して行われ、合計で44の変更がありました。具体的には、22行の追加と22行の削除が行われています。

主な変更点は、ベクトルクォータとパーティション制限に関する情報の整理と更新です。新たに「Vector index size and staying under limits」というリンクが文書に追加され、ユーザーがベクトルインデックスについての詳細を確認できるようになりました。

また、パーティションに関する制限が明確に示されるようになり、各サービスの作成日およびティアに応じた制限を説明するテーブルが追加されています。これにより、ユーザーはストレージクォータの進行状況をより理解しやすくなり、特に2024年4月以降に導入される新しいパーティション制限に関する情報を得ることができます。

全体として、この改訂は文書を最新の状態に保ち、ユーザーがインデクサとその制限に関する知識を深めるための支援となることを目的としています。

## articles/search/search-lucene-query-architecture.md{#item-b0d568}

<details>
<summary>Diff</summary>
````diff
@@ -159,7 +159,7 @@ When the default analyzer processes the term, it will lowercase "ocean view" and
 
 ### Testing analyzer behaviors 
 
-The behavior of an analyzer can be tested using the [Analyze API](/rest/api/searchservice/test-analyzer). Provide the text you want to analyze to see what terms given analyzer generates. For example, to see how the standard analyzer would process the text "air-condition", you can issue the following request:
+The behavior of an analyzer can be tested using the [Analyze API](/rest/api/searchservice/indexes/analyze). Provide the text you want to analyze to see what terms given analyzer generates. For example, to see how the standard analyzer would process the text "air-condition", you can issue the following request:
 
 ```json
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Analyze APIのリンク更新"
}
```

### Explanation
この変更は、「search-lucene-query-architecture.md」という文書に対するもので、合計で2つの変更が行われ、1行が追加され、1行が削除されました。

変更の主な内容は、分析器の動作をテストするための「Analyze API」のリンクが更新されたことです。もともと使用されていたリンクは「[Analyze API](/rest/api/searchservice/test-analyzer)」でしたが、これが「[Analyze API](/rest/api/searchservice/indexes/analyze)」に変更されました。この更新により、ユーザーが正しいAPIエンドポイントを通じて分析器の動作をテストできるようになります。

文書内では、与えられたテキストが特定の分析器によってどのように処理されるかを確認する方法について解説されており、この変更は、ドキュメントの内容を最新の状態に保つための重要な改善です。

## articles/search/search-normalizers.md{#item-4477d9}

<details>
<summary>Diff</summary>
````diff
@@ -45,7 +45,7 @@ Normalizers are specified in an index definition, on a per-field basis, on text
 
 Normalizers can only be specified when you add a new field to the index, so if possible, try to assess the normalization needs upfront and assign normalizers in the initial stages of development when dropping and recreating indexes is routine. 
 
-1. When creating a field definition in the [index](/rest/api/searchservice/create-index), set the  "normalizer" property to one of the following values: a [predefined normalizer](#predefined-normalizers) such as "lowercase", or a custom normalizer (defined in the same index schema).  
+1. When creating a field definition in the [index](/rest/api/searchservice/indexes/create), set the  "normalizer" property to one of the following values: a [predefined normalizer](#predefined-normalizers) such as "lowercase", or a custom normalizer (defined in the same index schema).  
  
    ```json
    "fields": [
@@ -62,7 +62,7 @@ Normalizers can only be specified when you add a new field to the index, so if p
    ]
    ```
 
-1. Custom normalizers are defined in the "normalizers" section of the index first, and then assigned to the field definition as shown in the previous step. For more information, see [Create Index](/rest/api/searchservice/create-index) and also [Add custom normalizers](#add-custom-normalizers).
+1. Custom normalizers are defined in the "normalizers" section of the index first, and then assigned to the field definition as shown in the previous step. For more information, see [Create Index](/rest/api/searchservice/indexes/create) and also [Add custom normalizers](#add-custom-normalizers).
 
    ```json
    "fields": [
@@ -79,7 +79,7 @@ Normalizers can only be specified when you add a new field to the index, so if p
 > [!NOTE]
 > To change the normalizer of an existing field, [rebuild the index](search-howto-reindex.md) entirely (you cannot rebuild individual fields).
 
-A good workaround for production indexes, where rebuilding indexes is costly, is to create a new field identical to the old one but with the new normalizer, and use it in place of the old one. Use [Update Index](/rest/api/searchservice/update-index) to incorporate the new field and [mergeOrUpload](/rest/api/searchservice/addupdate-or-delete-documents) to populate it. Later, as part of planned index servicing, you can clean up the index to remove obsolete fields.
+A good workaround for production indexes, where rebuilding indexes is costly, is to create a new field identical to the old one but with the new normalizer, and use it in place of the old one. Use [Update Index](/rest/api/searchservice/indexes/create-or-update) to incorporate the new field and [mergeOrUpload](/rest/api/searchservice/documents) to populate it. Later, as part of planned index servicing, you can clean up the index to remove obsolete fields.
 
 ## Predefined and custom normalizers 
 
@@ -131,7 +131,7 @@ The list below shows the token filters supported for normalizers and is a subset
 
 ## Add custom normalizers
 
-Custom normalizers are [defined within the index schema](/rest/api/searchservice/create-index). The definition includes a name, a type, one or more character filters and token filters. The character filters and token filters are the building blocks for a custom normalizer and responsible for the processing of the text. These filters are applied from left to right.
+Custom normalizers are [defined within the index schema](/rest/api/searchservice/indexes/create). The definition includes a name, a type, one or more character filters and token filters. The character filters and token filters are the building blocks for a custom normalizer and responsible for the processing of the text. These filters are applied from left to right.
 
  The `token_filter_name_1` is the name of token filter, and `char_filter_name_1` and `char_filter_name_2` are the names of char filters (see [supported token filters](#supported-token-filters) and [supported char filters](#supported-char-filters)tables below for valid values).
 
@@ -169,7 +169,7 @@ Custom normalizers are [defined within the index schema](/rest/api/searchservice
 ]
 ```
 
-Custom normalizers can be added during index creation or later by updating an existing one. Adding a custom normalizer to an existing index requires the "allowIndexDowntime" flag to be specified in [Update Index](/rest/api/searchservice/update-index) and will cause the index to be unavailable for a few seconds.
+Custom normalizers can be added during index creation or later by updating an existing one. Adding a custom normalizer to an existing index requires the "allowIndexDowntime" flag to be specified in [Update Index](/rest/api/searchservice/indexes/create-or-update) and will cause the index to be unavailable for a few seconds.
 
 ## Custom normalizer example
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス作成時のリンク更新"
}
```

### Explanation
この変更は、「search-normalizers.md」という文書に対して行われ、全体で10の変更があり、5行の追加および5行の削除がありました。

主な変更点は、インデックスの作成に関するリンクが更新されたことです。具体的には、文中で言及されている「Analyze API」へのリンク先が、以前の「/rest/api/searchservice/create-index」から新しい「/rest/api/searchservice/indexes/create」に変更されました。この修正により、ユーザーが最新のエンドポイントに基づいて正確にリソースにアクセスできるようになります。

さらに、この変更はカスタムノーマライザーの定義や更新についても言及しており、適切なAPIエンドポイントを示すことで、読者が効果的にこれらの操作を行えるようサポートしています。また、文書の整合性が向上し、ユーザーが必要な情報を容易に見つけられるようになります。この変更は、ものを追加したり、更新したりする際の全体的な開発プロセスを円滑に進めることに貢献します。

## articles/search/search-performance-tips.md{#item-218e77}

<details>
<summary>Diff</summary>
````diff
@@ -61,7 +61,7 @@ Query composition and complexity are one of the most important factors for perfo
 
 + **Number of searchable fields.** Each additional searchable field results in more work for the search service. You can limit the fields being searched at query time using the "searchFields" parameter. It's best to specify only the fields that you care about to improve performance.
 
-+ **Amount of data being returned.** Retrieving a large amount content can make queries slower. When structuring a query, return only those fields that you need to render the results page, and then retrieve remaining fields using the [Lookup API](/rest/api/searchservice/lookup-document) once a user selects a match.
++ **Amount of data being returned.** Retrieving a large amount content can make queries slower. When structuring a query, return only those fields that you need to render the results page, and then retrieve remaining fields using the [Lookup API](/rest/api/searchservice/documents/get) once a user selects a match.
 
 + **Use of partial term searches.** [Partial term searches](search-query-partial-matching.md), such as prefix search, fuzzy search, and regular expression search, are more computationally expensive than typical keyword searches, as they require full index scans to produce results.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索パフォーマンスのTipsのリンク更新"
}
```

### Explanation
この変更は、「search-performance-tips.md」という文書に対して行われ、合計で2つの変更があり、1行の追加と1行の削除がありました。

主な変更点は、「返されるデータの量」に関する文の中で使用されている「Lookup API」のリンクが更新されたことです。以前は「[Lookup API](/rest/api/searchservice/lookup-document)」というリンクが使われていましたが、これが新しい「[Lookup API](/rest/api/searchservice/documents/get)」に変更されました。この更新により、ユーザーが正確なAPIエンドポイントにアクセスできるようになり、検索操作の効率性が向上します。

また、文書の他の部分では、検索フィールドの数や部分用語検索の使用についても言及されており、クエリ構造のベストプラクティスが強調されています。全体として、この変更はドキュメントの正確性と有用性を高め、ユーザーがパフォーマンスを最適化するための具体的な手助けとなることを目的としています。

## articles/search/search-query-create.md{#item-532822}

<details>
<summary>Diff</summary>
````diff
@@ -147,7 +147,7 @@ Search is fundamentally a user-driven exercise, where terms or phrases are colle
 |-------|---------|
 | [Search method](/rest/api/searchservice/documents/search-post) | A user types the terms or phrases into a search box, with or without operators, and clicks Search to send the request. Search can be used with filters on the same request, but not with autocomplete or suggestions. |
 | [Autocomplete method](/rest/api/searchservice/documents/autocomplete-post) | A user types a few characters, and queries are initiated after each new character is typed. The response is a completed string from the index. If the string provided is valid, the user clicks Search to send that query to the service. |
-| [Suggestions method](/rest/api/searchservice/suggestions) | As with autocomplete, a user types a few characters and incremental queries are generated. The response is a dropdown list of matching documents, typically represented by a few unique or descriptive fields. If any of the selections are valid, the user clicks one and the matching document is returned. |
+| [Suggestions method](/rest/api/searchservice/documents/suggest-post) | As with autocomplete, a user types a few characters and incremental queries are generated. The response is a dropdown list of matching documents, typically represented by a few unique or descriptive fields. If any of the selections are valid, the user clicks one and the matching document is returned. |
 | [Faceted navigation](/rest/api/searchservice/documents/search-post#searchrequest) | A page shows clickable navigation links or breadcrumbs that narrow the scope of the search. A faceted navigation structure is composed dynamically based on an initial query. For example, `search=*` to populate a faceted navigation tree composed of every possible category. A faceted navigation structure is created from a query response, but it's also a mechanism for expressing the next query. n REST API reference, `facets` is documented as a query parameter of a Search Documents operation, but it can be used without the `search` parameter.|
 | [Filter method](/rest/api/searchservice/documents/search-post#searchrequest) | Filters are used with facets to narrow results. You can also implement a filter behind the page, for example to initialize the page with language-specific fields. In REST API reference, `$filter` is documented as a query parameter of a Search Documents operation, but it can be used without the `search` parameter.|
 
@@ -159,13 +159,13 @@ In the portal screenshot below of the [hotels sample index](search-get-started-p
 
 ![Index definition for the hotel sample](./media/search-query-overview/hotel-sample-index-definition.png "Index definition for the hotel sample")
 
-For field attribute definitions, see [Create Index (REST API)](/rest/api/searchservice/create-index).
+For field attribute definitions, see [Create Index (REST API)](/rest/api/searchservice/indexes/create).
 
 ## Effect of tokens on queries
 
 During indexing, the search engine uses a text analyzer on strings to maximize the potential for finding a match at query time. At a minimum, strings are lower-cased, but depending on the analyzer, might also undergo lemmatization and stop word removal. Larger strings or compound words are typically broken up by whitespace, hyphens, or dashes, and indexed as separate tokens. 
 
-The point to take away here's that what you think your index contains, and what's actually in it, can be different. If queries don't return expected results, you can inspect the tokens created by the analyzer through the [Analyze Text (REST API)](/rest/api/searchservice/test-analyzer). For more information about tokenization and the impact on queries, see [Partial term search and patterns with special characters](search-query-partial-matching.md).
+The point to take away here's that what you think your index contains, and what's actually in it, can be different. If queries don't return expected results, you can inspect the tokens created by the analyzer through the [Analyze Text (REST API)](/rest/api/searchservice/indexes/analyze). For more information about tokenization and the impact on queries, see [Partial term search and patterns with special characters](search-query-partial-matching.md).
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIエンドポイントのリンク更新"
}
```

### Explanation
この変更は、「search-query-create.md」という文書に対して行われ、合計で6つの変更がありました。具体的には、3行の追加と3行の削除が実施されています。

主な変更点は、さまざまな検索方法に関するリンクが更新されたことです。特に、「Suggestions method」のリンクが新しいエンドポイント「[Suggestions method](/rest/api/searchservice/documents/suggest-post)」に変更され、その結果、ユーザーが最新のREST APIを通じて正確に情報を取得できるようになりました。

また、最後の部分では、トークンの影響に関する説明の中で、テキスト分析に関連するリンクも「[Analyze Text (REST API)](/rest/api/searchservice/indexes/analyze)」に更新されました。このリンクの変更により、クエリの結果が期待通りでない場合に、ユーザーがどのようにトークンを調査するかについての情報へのアクセスが向上します。

全体として、この修正はドキュメントの正確性を高め、ユーザーが効率的に検索機能を利用できるようにすることを目的としています。

## articles/search/search-query-lucene-examples.md{#item-ce3624}

<details>
<summary>Diff</summary>
````diff
@@ -114,7 +114,7 @@ The search expression can be a single term or a phrase, or a more complex expres
 
 Be sure to put a phrase within quotation marks if you want both strings to be evaluated as a single entity, as in this case searching for two distinct locations in the Address/StateProvince field. Depending on the client, you might need to escape (`\`) the quotation marks.
 
-The field specified in `fieldName:searchExpression` must be a searchable field. See [Create Index (REST API)](/rest/api/searchservice/create-index) for details on how field definitions are attributed.
+The field specified in `fieldName:searchExpression` must be a searchable field. See [Create Index (REST API)](/rest/api/searchservice/indexes/create) for details on how field definitions are attributed.
 
 ## Example 2: Fuzzy search
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Lucene例のリンク更新"
}
```

### Explanation
この変更は、「search-query-lucene-examples.md」という文書に対して行われ、合計で2つの変更があり、1行の追加と1行の削除が行われました。

主な変更点は、`fieldName:searchExpression`の構文で指定されるフィールドに関する説明のリンクが更新されたことです。以前は「[Create Index (REST API)](/rest/api/searchservice/create-index)」というリンクが使われていましたが、これが新しいリンク「[Create Index (REST API)](/rest/api/searchservice/indexes/create)」に変更されました。この修正により、ユーザーは最新のREST APIドキュメントにアクセスし、フィールド定義の atrib 記載方法について正確な情報を得ることができるようになりました。

この更新は、検索機能を利用する上での正確な情報提供を目的としており、ユーザーが効果的に検索を構成できるよう支援しています。

## articles/search/search-query-odata-full-text-search-functions.md{#item-5748d4}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,7 @@ translation.priority.mt:
 Azure AI Search supports full-text search in the context of [OData filter expressions](query-odata-filter-orderby-syntax.md) via the `search.ismatch` and `search.ismatchscoring` functions. These functions allow you to combine full-text search with strict Boolean filtering in ways that are not possible just by using the top-level `search` parameter of the [Search API](/rest/api/searchservice/documents/search-post).
 
 > [!NOTE]
-> The `search.ismatch` and `search.ismatchscoring` functions are only supported in filters in the [Search API](/rest/api/searchservice/documents/search-post). They are not supported in the [Suggest](/rest/api/searchservice/suggestions) or [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) APIs.
+> The `search.ismatch` and `search.ismatchscoring` functions are only supported in filters in the [Search API](/rest/api/searchservice/documents/search-post). They are not supported in the [Suggest](/rest/api/searchservice/documents/suggest-post) or [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) APIs.
 
 ## Syntax
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Suggest APIリンクの更新"
}
```

### Explanation
この変更は、「search-query-odata-full-text-search-functions.md」という文書に対して実施され、合計で2つの変更があり、1行の追加と1行の削除が行われました。

主な変更点は、`search.ismatch`および`search.ismatchscoring`関数に関する注記の一部が更新されたことです。具体的には、これらの関数が「Suggest」APIのリンクが「[Suggest](/rest/api/searchservice/documents/suggest-post)」に変更されました。これにより、ユーザーは最新のドキュメントへの正確なリンクを利用できるようになりました。

この修正は、ユーザーがAzure AI Searchのフルテキスト検索機能とその利用方法を理解する際の便益を高め、正確な情報を提供することを目的としています。

## articles/search/search-query-overview.md{#item-dcd5d6}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,7 @@ This article brings focus to the last category: queries that work on plain text
 
 ## Autocomplete and suggested queries
 
-[Autocomplete or suggested results](search-add-autocomplete-suggestions.md) are alternatives to **`search`** that fire successive query requests based on partial string inputs (after each character) in a search-as-you-type experience. You can use **`autocomplete`** and **`suggestions`** parameter together or separately, as described in [this walkthrough](tutorial-csharp-type-ahead-and-suggestions.md), but you can't use them with **`search`**. Both completed terms and suggested queries are derived from index contents. The engine never returns a string or suggestion that is nonexistent in your index. For more information, see [Autocomplete (REST API)](/rest/api/searchservice/documents/autocomplete-post) and [Suggestions (REST API)](/rest/api/searchservice/suggestions).
+[Autocomplete or suggested results](search-add-autocomplete-suggestions.md) are alternatives to **`search`** that fire successive query requests based on partial string inputs (after each character) in a search-as-you-type experience. You can use **`autocomplete`** and **`suggestions`** parameter together or separately, as described in [this walkthrough](tutorial-csharp-type-ahead-and-suggestions.md), but you can't use them with **`search`**. Both completed terms and suggested queries are derived from index contents. The engine never returns a string or suggestion that is nonexistent in your index. For more information, see [Autocomplete (REST API)](/rest/api/searchservice/documents/autocomplete-post) and [Suggestions (REST API)](/rest/api/searchservice/documents/suggest-post).
 
 ## Filter search
 
@@ -74,7 +74,7 @@ For more information and examples, see [Geospatial search example](search-query-
 
 ## Document look-up
 
-In contrast with the previously described query forms, this one retrieves a single [search document by ID](/rest/api/searchservice/lookup-document), with no corresponding index search or scan. Only the one document is requested and returned. When a user selects an item in search results, retrieving the document and populating a details page with fields is a typical response, and a document look-up is the operation that supports it.
+In contrast with the previously described query forms, this one retrieves a single [search document by ID](/rest/api/searchservice/documents/get), with no corresponding index search or scan. Only the one document is requested and returned. When a user selects an item in search results, retrieving the document and populating a details page with fields is a typical response, and a document look-up is the operation that supports it.
 
 ## Advanced search: fuzzy, wildcard, proximity, regex
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIリンクの更新"
}
```

### Explanation
この変更は、「search-query-overview.md」という文書に対して行われ、合計で4つの変更があり、2行の追加と2行の削除が実施されました。

主な変更点は、ドキュメントの中で参照されるREST APIのリンクが更新されたことです。具体的には、ドキュメントの取得に関するリンクが「[search document by ID](/rest/api/searchservice/lookup-document)」から「[search document by ID](/rest/api/searchservice/documents/get)」に変更されました。また、提案機能に関連するAPIのリンクも「[Suggestions (REST API)](/rest/api/searchservice/suggestions)」から「[Suggestions (REST API)](/rest/api/searchservice/documents/suggest-post)」に更新されています。

これらの変更は、ユーザーが最新のAPIエンドポイントにアクセスできるようにし、検索機能の利用をさらにスムーズにすることを目的としています。これにより、利用者は正確な情報を元にAPIを活用しやすくなります。

## articles/search/search-query-partial-matching.md{#item-bd97dc}

<details>
<summary>Diff</summary>
````diff
@@ -85,7 +85,7 @@ When choosing an analyzer that produces whole-term tokens, the following analyze
 | [whitespace](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/core/WhitespaceAnalyzer.html) | Separates on white spaces only. Terms that include dashes or other characters are treated as a single token. |
 | [custom analyzer](index-add-custom-analyzers.md) | (recommended) Creating a custom analyzer lets you specify both the tokenizer and token filter. The previous analyzers must be used as-is. A custom analyzer lets you pick which tokenizers and token filters to use. <br><br>A recommended combination is the [keyword tokenizer](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/core/KeywordTokenizer.html) with a [lower-case token filter](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/core/LowerCaseFilter.html). By itself, the built-in [keyword analyzer](https://lucene.apache.org/core/6_6_1/analyzers-common/org/apache/lucene/analysis/core/KeywordAnalyzer.html) doesn't lower-case any upper-case text, which can cause queries to fail. A custom analyzer gives you a mechanism for adding the lower-case token filter. |
 
-Using a REST client, you can add the [Test Analyzer REST call](/rest/api/searchservice/test-analyzer) to inspect tokenized output.
+Using a REST client, you can add the [Test Analyzer REST call](/rest/api/searchservice/indexes/analyze) to inspect tokenized output.
 
 The index must exist on the search service, but it can be empty. Given an existing index and a field containing dashes or partial terms, you can try various analyzers over specific terms to see what tokens are emitted.  
 
@@ -227,13 +227,13 @@ Use a REST client to query partial terms and special characters described in thi
 
 The previous sections explained the logic. This section steps through each API you should call when testing your solution. 
 
-+ [Delete Index](/rest/api/searchservice/delete-index) removes an existing index of the same name so that you can recreate it.
++ [Delete Index](/rest/api/searchservice/indexes/delete) removes an existing index of the same name so that you can recreate it.
 
-+ [Create Index](/rest/api/searchservice/create-index) creates the index structure on your search service, including analyzer definitions and fields with an analyzer specification.
++ [Create Index](/rest/api/searchservice/indexes/create) creates the index structure on your search service, including analyzer definitions and fields with an analyzer specification.
 
-+ [Load Documents](/rest/api/searchservice/addupdate-or-delete-documents) imports documents having the same structure as your index, as well as searchable content. After this step, your index is ready to query or test.
++ [Load Documents](/rest/api/searchservice/documents) imports documents having the same structure as your index, as well as searchable content. After this step, your index is ready to query or test.
 
-+ [Test Analyzer](/rest/api/searchservice/test-analyzer) was introduced in [Set an analyzer](#set-an-analyzer). Test some of the strings in your index using various analyzers to understand how terms are tokenized.
++ [Test Analyzer](/rest/api/searchservice/indexes/analyze) was introduced in [Set an analyzer](#set-an-analyzer). Test some of the strings in your index using various analyzers to understand how terms are tokenized.
 
 + [Search Documents](/rest/api/searchservice/documents/search-post) explains how to construct a query request, using either [simple syntax](query-simple-syntax.md) or [full Lucene syntax](query-lucene-syntax.md) for wildcard and regular expressions.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIリンクの修正"
}
```

### Explanation
この変更は、「search-query-partial-matching.md」という文書に対して行われ、合計で10の変更があり、5行の追加と5行の削除が実施されました。

主な変更点は、文書内で参照されるREST APIのリンクが修正されたことです。具体的には、「Test Analyzer REST call」や「Delete Index」、「Create Index」、「Load Documents」などのエンドポイントのリンクが、より正確な新しいパスに更新されました。例えば、「/rest/api/searchservice/test-analyzer」から「/rest/api/searchservice/indexes/analyze」へと変更されています。

これらの修正により、ユーザーは正確で最新の情報にアクセスできるようになり、APIの使用において混乱を避けることができます。また、文書で説明されている各機能に対して、適切なエンドポイントを提供することで、理解を深める手助けとなっていることが目的です。

## articles/search/search-query-simple-examples.md{#item-834766}

<details>
<summary>Diff</summary>
````diff
@@ -73,7 +73,7 @@ POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
 }
 ```
 
-A keyword search that's composed of important terms or phrases tend to work best. String fields undergo text analysis during indexing and querying, dropping nonessential words like "the", "and", "it". To see how a query string is tokenized in the index, pass the string in an [Analyze Text](/rest/api/searchservice/test-analyzer) call to the index.
+A keyword search that's composed of important terms or phrases tend to work best. String fields undergo text analysis during indexing and querying, dropping nonessential words like "the", "and", "it". To see how a query string is tokenized in the index, pass the string in an [Analyze Text](/rest/api/searchservice/indexes/analyze) call to the index.
 
 The "searchMode" parameter controls precision and recall. If you want more recall, use the default "any" value, which returns a result if any part of the query string is matched. If you favor precision, where all parts of the string must be matched, change searchMode to "all". Try the above query both ways to see how searchMode changes the outcome.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト解析APIリンクの修正"
}
```

### Explanation
この変更は、「search-query-simple-examples.md」という文書に対して行われ、合計で2つの変更があり、1行の追加と1行の削除が実施されました。

主な変更点は、クエリ文字列がインデックスでどのようにトークン化されるかを確認するためのAPIのリンクが修正されたことです。具体的には、依然として「Analyze Text」機能を参照している文で、旧リンク「/rest/api/searchservice/test-analyzer」から新リンク「/rest/api/searchservice/indexes/analyze」に変更されました。この修正により、ユーザーはより正確で最新のAPIエンドポイントにアクセスできるようになり、インデックス内でのテキスト解析の結果を確認しやすくなります。

このような文書の更新は、ユーザーが正確な情報をもとに効果的にAPIを利用できるようにすることを目的としています。

## articles/search/search-reliability.md{#item-3e9b1a}

<details>
<summary>Diff</summary>
````diff
@@ -124,7 +124,7 @@ You can implement this architecture by creating multiple services and designing
 There are two options for keeping two or more distinct search services in sync:
 
 + Pull content updates into a search index by using an [indexer](search-indexer-overview.md).
-+ Push content into an index using the [Add or Update Documents (REST)](/rest/api/searchservice/addupdate-or-delete-documents) API or an Azure SDK equivalent API.
++ Push content into an index using the [Add or Update Documents (REST)](/rest/api/searchservice/documents) API or an Azure SDK equivalent API.
 
 To configure either option, we recommend using the [sample Bicep script in the azure-search-multiple-region](https://github.com/Azure-Samples/azure-search-multiple-regions) repository, modified to your regions and indexing strategies.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIリンクの修正"
}
```

### Explanation
この変更は、「search-reliability.md」という文書に対して行われ、合計で2つの変更があり、1行の追加と1行の削除が実施されました。

主な変更点は、コンテンツをインデックスにプッシュするためのAPIのリンクが更新されたことです。具体的には、旧リンク「/rest/api/searchservice/addupdate-or-delete-documents」から新リンク「/rest/api/searchservice/documents」へと修正されました。また、新たにインデックスを更新するためにインデクサーを使用するオプションが追加されています。

この修正により、ユーザーが正確な情報をもとにAPIを使ってコンテンツを管理できるようになることを目的としています。文書の更新は、ユーザーがより効果的にAzureの検索サービスを利用するためのサポートを強化するために重要です。

## articles/search/search-semi-structured-data.md{#item-d3388d}

<details>
<summary>Diff</summary>
````diff
@@ -197,7 +197,7 @@ Connection: close
 
 ## Create an index
 
-[Create Index (REST)](/rest/api/searchservice/create-index) creates a search index on your search service. An index specifies all the parameters and their attributes.
+[Create Index (REST)](/rest/api/searchservice/indexes/create) creates a search index on your search service. An index specifies all the parameters and their attributes.
 
 For nested JSON, the index fields must be identical to the source fields. Currently, Azure AI Search doesn't support field mappings to nested JSON. For this reason, field names and data types must match completely. The following index aligns to the JSON elements in the raw content.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIリンクの修正"
}
```

### Explanation
この変更は、「search-semi-structured-data.md」という文書に対して行われ、合計で2つの変更があり、1行の追加と1行の削除が実施されました。

主な変更点は、検索インデックスを作成するためのREST APIのリンクが更新されたことです。具体的には、旧リンク「/rest/api/searchservice/create-index」から新リンク「/rest/api/searchservice/indexes/create」へと修正されました。この修正により、ユーザーは最新のエンドポイントを通じて検索インデックスを正確に作成できるようになります。

このような文書の更新は、Azureの検索サービスに関する情報を正確かつ最新のものに保つことを目的としており、ユーザーが効率的にサービスを利用できるようサポートします。

## articles/search/search-sku-tier.md{#item-7686b8}

<details>
<summary>Diff</summary>
````diff
@@ -27,7 +27,7 @@ In a few instances, the tier you choose determines the availability of [premium
 Billing rates are shown in the portal's **Select Pricing Tier** page. You can check the [pricing page](https://azure.microsoft.com/pricing/details/search/) for regional rates and review [Plan and manage costs](search-sku-manage-costs.md) to learn more about the billing model.
 
 > [!NOTE]
-> Search services created after April 3, 2024 have larger partitions and higher vector quotas at almost every tier. For more information, see [service limits](search-limits-quotas-capacity.md#after-april-3-2024).
+> Search services created after April 3, 2024 have larger partitions and higher vector quotas at almost every tier. For more information, see [service limits](search-limits-quotas-capacity.md#service-limits).
 
 ## Tier descriptions
 
@@ -61,6 +61,7 @@ Currently, several regions are at capacity for Basic and Standard (S1) tiers and
 | Japan East | S2, S3, S3HD, L1, L2 |
 | Qatar Central | All tiers|
 | South Central US | All tiers |
+| US Gov Virginia | All tiers |
 | West Europe | All tiers |
 | West US 3| All tiers |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス制限リンクの修正と新しい地域の追加"
}
```

### Explanation
この変更は、「search-sku-tier.md」という文書に対して行われ、合計で3つの変更があり、2行の追加と1行の削除が実施されました。

主な変更点は、検索サービスに関する特定の情報が更新されたことです。具体的には、2024年4月3日以降に作成された検索サービスについての注意点が修正され、リンク先が「service-limits」のセクションに変更されました。また、米国政府バージニア地域（US Gov Virginia）がすべてのティアで利用可能であることを示す新しい情報が追加されています。

この修正により、ユーザーは新しいサービス制限の正確な情報にアクセスできるようになり、Azureの検索サービスを使用する際の理解が深まるでしょう。このような文書の更新は、ユーザーにとってより明確で正確な情報を提供することを目的としています。

## articles/search/search-synapseml-cognitive-services.md{#item-dcc36f}

<details>
<summary>Diff</summary>
````diff
@@ -223,7 +223,7 @@ display(translated_df)
 
 Paste the following code in the sixth cell and then run it. No modifications are required.
 
-This code loads [AzureSearchWriter](https://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/AI%20Services/Overview/#azure-cognitive-search-sample). It consumes a tabular dataset and infers a search index schema that defines one field for each column. Because the translations structure is an array, it's articulated in the index as a complex collection with subfields for each language translation. The generated index has a document key and use the default values for fields created using the [Create Index REST API](/rest/api/searchservice/create-index).
+This code loads [AzureSearchWriter](https://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/AI%20Services/Overview/#azure-cognitive-search-sample). It consumes a tabular dataset and infers a search index schema that defines one field for each column. Because the translations structure is an array, it's articulated in the index as a complex collection with subfields for each language translation. The generated index has a document key and use the default values for fields created using the [Create Index REST API](/rest/api/searchservice/indexes/create).
 
 ```python
 from synapse.ml.cognitive import *
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIリンクの修正"
}
```

### Explanation
この変更は、「search-synapseml-cognitive-services.md」という文書に対して行われ、合計で2つの変更があり、1行の追加と1行の削除が実施されました。

具体的には、AzureSearchWriterに関する説明文の中で、使用しているREST APIのリンクが更新されました。以前のリンク「/rest/api/searchservice/create-index」から新しいリンク「/rest/api/searchservice/indexes/create」に修正されました。この変更により、ユーザーは最新のエンドポイントを使用して、検索インデックスを正確に作成できることになります。

このような更新は、ドキュメントの正確性を保ち、ユーザーがAzure Searchサービスを適切に利用できるようにするために重要です。また、最新の情報を提供することで、ユーザーの混乱を減らし、作業の効率を向上させることを目的としています。

## articles/search/search-synonyms.md{#item-2d5d63}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ To create a synonym map, do so programmatically. The portal doesn't support syno
 
 ### [REST](#tab/rest)
 
-Use the [Create Synonym Map (REST API)](/rest/api/searchservice/create-synonym-map) to create a synonym map.
+Use the [Create Synonym Map (REST API)](/rest/api/searchservice/synonym-maps/create) to create a synonym map.
 
 ```http
 POST /synonymmaps?api-version=2024-07-01
@@ -251,4 +251,4 @@ If you have an existing index in a development (nonproduction) environment, expe
 ## Next steps
 
 > [!div class="nextstepaction"]
-> [Create a synonym map (REST API)](/rest/api/searchservice/create-synonym-map)
+> [Create a synonym map (REST API)](/rest/api/searchservice/synonym-maps/create)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIリンクの更新"
}
```

### Explanation
この変更は、「search-synonyms.md」という文書に対して行われ、合計で4つの変更があり、2行の追加と2行の削除が実施されました。

主な変更点は、同義語マップを作成するためのREST APIのリンクが修正されたことです。具体的には、古いリンク「/rest/api/searchservice/create-synonym-map」が新しいリンク「/rest/api/searchservice/synonym-maps/create」に置き換えられました。この変更により、ユーザーは最新のエンドポイントを使用して同義語マップを正確に作成できるようになります。

このような更新は、ドキュメントの正確性を確保し、ユーザーがAzure Searchサービスを適切に活用できるようにするために重要です。リンクの正確性を保つことで、ユーザーが混乱することなく、スムーズに情報を取得できるよう配慮されています。

## articles/search/search-what-is-an-index.md{#item-5a3344}

<details>
<summary>Diff</summary>
````diff
@@ -80,7 +80,7 @@ Other elements are collapsed for brevity, but the following links provide detail
 
 ### Field definitions
 
-A search document is defined by the "fields" collection in the body of [Create Index request](/rest/api/searchservice/create-index). You need fields for document identification (keys), storing searchable text, and fields for supporting filters, facets, and sorting. You might also need fields for data that a user never sees. For example, you might want fields for profit margins or marketing promotions that you can use in a scoring profile to boost a search score.
+A search document is defined by the "fields" collection in the body of [Create Index request](/rest/api/searchservice/indexes/create). You need fields for document identification (keys), storing searchable text, and fields for supporting filters, facets, and sorting. You might also need fields for data that a user never sees. For example, you might want fields for profit margins or marketing promotions that you can use in a scoring profile to boost a search score.
 
 If incoming data is hierarchical in nature, you can represent it within an index as a [complex type](search-howto-complex-data-types.md), used for nested structures. The built-in sample data set, Hotels, illustrates complex types using an Address (contains multiple subfields) that has a one-to-one relationship with each hotel, and a Rooms complex collection, where multiple rooms are associated with each hotel. 
 
@@ -97,22 +97,22 @@ String fields are often marked as "searchable" and "retrievable". Fields used to
 |"searchable" |Full-text or vector searchable. Text fields are subject to lexical analysis such as word-breaking during indexing. If you set a searchable field to a value like "sunny day", internally it's split into the individual tokens "sunny" and "day". For details, see [How full text search works](search-lucene-query-architecture.md).|  
 |"filterable" |Referenced in $filter queries. Filterable fields of type `Edm.String` or `Collection(Edm.String)` don't undergo word-breaking, so comparisons are for exact matches only. For example, if you set such a field f to "sunny day", `$filter=f eq 'sunny'` finds no matches, but `$filter=f eq 'sunny day'` will. |  
 |"sortable" |By default the system sorts results by score, but you can configure sort based on fields in the documents. Fields of type `Collection(Edm.String)` can't be "sortable". |  
-|"facetable" |Typically used in a presentation of search results that includes a hit count by category (for example, hotels in a specific city). This option can't be used with fields of type `Edm.GeographyPoint`. Fields of type `Edm.String` that are filterable, "sortable", or "facetable" can be at most 32 kilobytes in length. For details, see [Create Index (REST API)](/rest/api/searchservice/create-index).|  
+|"facetable" |Typically used in a presentation of search results that includes a hit count by category (for example, hotels in a specific city). This option can't be used with fields of type `Edm.GeographyPoint`. Fields of type `Edm.String` that are filterable, "sortable", or "facetable" can be at most 32 kilobytes in length. For details, see [Create Index (REST API)](/rest/api/searchservice/indexes/create).|  
 |"key" |Unique identifier for documents within the index. Exactly one field must be chosen as the key field and it must be of type `Edm.String`.|  
 |"retrievable" |Determines whether the field can be returned in a search result. This is useful when you want to use a field (such as *profit margin*) as a filter, sorting, or scoring mechanism, but don't want the field to be visible to the end user. This attribute must be `true` for `key` fields.|  
 
 Although you can add new fields at any time, existing field definitions are locked in for the lifetime of the index. For this reason, developers typically use the portal for creating simple indexes, testing ideas, or using the portal pages to look up a setting. Frequent iteration over an index design is more efficient if you follow a code-based approach so that you can rebuild the index easily.
 
 > [!NOTE]
-> The APIs you use to build an index have varying default behaviors. For the [REST APIs](/rest/api/searchservice/Create-Index), most attributes are enabled by default (for example, "searchable" and "retrievable" are true for string fields) and you often only need to set them if you want to turn them off. For the .NET SDK, the opposite is true. On any property you do not explicitly set, the default is to disable the corresponding search behavior unless you specifically enable it.
+> The APIs you use to build an index have varying default behaviors. For the [REST APIs](/rest/api/searchservice/indexes/create), most attributes are enabled by default (for example, "searchable" and "retrievable" are true for string fields) and you often only need to set them if you want to turn them off. For the .NET SDK, the opposite is true. On any property you do not explicitly set, the default is to disable the corresponding search behavior unless you specifically enable it.
 
 <a name="index-size"></a>
 
 ## Physical structure and size
 
 In Azure AI Search, the physical structure of an index is largely an internal implementation. You can access its schema, query its content, monitor its size, and manage capacity, but the clusters themselves (indexes, [shards](index-similarity-and-scoring.md#sharding-effects-on-query-results), and other files and folders) are managed internally by Microsoft.
 
-You can monitor index size in the Indexes tab in the Azure portal, or by issuing a [GET INDEX request](/rest/api/searchservice/get-index) against your search service. You can also issue a [Service Statistics request](/rest/api/searchservice/get-service-statistics) and check the value of storage size.
+You can monitor index size in the Indexes tab in the Azure portal, or by issuing a [GET INDEX request](/rest/api/searchservice/indexes/get) against your search service. You can also issue a [Service Statistics request](/rest/api/searchservice/get-service-statistics/get-service-statistics) and check the value of storage size.
 
 The size of an index is determined by:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIリンクの修正"
}
```

### Explanation
この変更は、「search-what-is-an-index.md」という文書に対して行われ、合計で8つの変更があり、4行の追加と4行の削除が実施されました。

主に、同索引を作成するためのREST APIのリンクがいくつか修正されました。具体的には、以下のリンクが古いものから新しいものに変更されました：

1. [Create Index request] のリンクが「/rest/api/searchservice/create-index」から「/rest/api/searchservice/indexes/create」に変更されました。
2. 同様に、「Create Index (REST API)」のリンクも新しいエンドポイント「/rest/api/searchservice/indexes/create」に更新されました。
3. インデックスサイズを監視する方法に関する記載でも、GETリクエストのリンクが「/rest/api/searchservice/get-index」から「/rest/api/searchservice/indexes/get」に修正されました。
4. また、サービス統計の取得に関するリンクも更新されています。

これらの変更は、ユーザーが最新のAPIエンドポイントにアクセスできるようにするためのもので、ドキュメントの正確性を確保し、Azure Searchサービスを効率的に利用できるようにするために重要です。また、正確なリンクを提供することで、ユーザーが最新の情報に基づいて操作を行えるよう配慮されています。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -89,7 +89,7 @@ An end-to-end exploration of core search features can be accomplished in four st
 
 Alternatively, you can create, load, and query a search index in atomic steps:
 
-1. [**Create a search index**](search-what-is-an-index.md) using the portal, [REST API](/rest/api/searchservice/create-index), [.NET SDK](search-howto-dotnet-sdk.md), or another SDK. The index schema defines the structure of searchable content.
+1. [**Create a search index**](search-what-is-an-index.md) using the portal, [REST API](/rest/api/searchservice/indexes/create), [.NET SDK](search-howto-dotnet-sdk.md), or another SDK. The index schema defines the structure of searchable content.
 
 1. [**Upload content**](search-what-is-data-import.md) using the ["push" model](tutorial-optimize-indexing-push-api.md) to push JSON documents from any source, or use the ["pull" model (indexers)](search-indexer-overview.md) if your source data is of a [supported type](search-indexer-overview.md#supported-data-sources).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIリンクの更新"
}
```

### Explanation
この変更は、「search-what-is-azure-search.md」という文書に対して行われ、合計で2つの変更があり、1行の追加と1行の削除が実施されました。

具体的には、「検索インデックスを作成する」段階に関連するREST APIのリンクが修正されました。古いリンク「/rest/api/searchservice/create-index」が新しいリンク「/rest/api/searchservice/indexes/create」に変更されました。この変更は、APIエンドポイントの最新の状態を反映するもので、ユーザーが正確で最新の情報を基にインデックスを作成できるようにするために重要です。

ドキュメントの正確性を高めることで、Azure Searchサービスの利用者がスムーズに操作を行えるよう配慮されています。このような小さな更新でも、技術文書の整合性を保ちながら、ユーザー体験の向上に寄与します。

## articles/search/search-what-is-data-import.md{#item-d73ef5}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ Key benefits include:
 
 Use the following APIs to load single or multiple documents into an index:
 
-+ [Add, Update, or Delete Documents (REST API)](/rest/api/searchservice/AddUpdate-or-Delete-Documents)
++ [Index Documents (REST API)](/rest/api/searchservice/documents)
 + [IndexDocumentsAsync (Azure SDK for .NET)](/dotnet/api/azure.search.documents.searchclient.indexdocumentsasync) or [SearchIndexingBufferedSender](/dotnet/api/azure.search.documents.searchindexingbufferedsender-1)
 + [IndexDocumentsBatch (Azure SDK for Python)](/python/api/azure-search-documents/azure.search.documents.indexdocumentsbatch) or [SearchIndexingBufferedSender](/python/api/azure-search-documents/azure.search.documents.searchindexingbufferedsender)
 + [IndexDocumentsBatch (Azure SDK for Java)](/java/api/com.azure.search.documents.indexes.models.indexdocumentsbatch) or [SearchIndexingBufferedSender](/java/api/com.azure.search.documents.searchindexingbufferedasyncsender)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIリンクの修正"
}
```

### Explanation
この変更は、「search-what-is-data-import.md」という文書に対して行われ、合計で2つの変更があり、1行の追加と1行の削除が実施されました。

具体的には、文書内で「ドキュメントを追加、更新、または削除するためのREST API」に関するリンクが修正されました。古いリンク「/rest/api/searchservice/AddUpdate-or-Delete-Documents」が新しいリンク「/rest/api/searchservice/documents」に更新されました。この変更により、ユーザーは最新のAPIエンドポイントを利用して、ドキュメントをインデックスに追加、更新、または削除することができるようになります。

このような小さな更新でも、正確な情報を提供することでユーザー体験が向上し、Azure Searchサービスを効果的に活用するためのサポートとなります。ドキュメントの整合性を保つことは、開発者にとって重要であり、正確な参照は作業効率を高めるのに寄与します。

## articles/search/semantic-answers.md{#item-c3fee9}

<details>
<summary>Diff</summary>
````diff
@@ -120,7 +120,7 @@ When designing a search results page that includes answers, be sure to handle ca
 
 Within @search.answers:
 
-+ **"key"** is the document key or ID of the match. Given a document key, you can use [Lookup Document](/rest/api/searchservice/lookup-document) API to retrieve any or all parts of the search document to include on the search page or a detail page.
++ **"key"** is the document key or ID of the match. Given a document key, you can use [Lookup Document](/rest/api/searchservice/documents/get) API to retrieve any or all parts of the search document to include on the search page or a detail page.
 
 + **"text"** and **"highlights"** provide identical content, in both plain text and with highlights. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIリンクの変更"
}
```

### Explanation
この変更は、「semantic-answers.md」という文書に対して行われ、合計で2つの変更があり、1行の追加と1行の削除があります。

具体的には、文書内に説明されている「キー」の定義に関して、関連するREST APIのリンクが修正されました。古いリンク「/rest/api/searchservice/lookup-document」が新しいリンク「/rest/api/searchservice/documents/get」に変更されています。この更新により、ユーザーはドキュメントのキーを使用して、最新のAPIエンドポイントで検索文書の全てまたは一部の情報を取得できるようになります。

この修正は、利用者が正確で有用な情報にアクセスできるようにするためのものであり、APIの最新状態を反映させることで、ユーザー体験を向上させることを目的としています。技術文書の正確性を保つことは、特に開発者にとって非常に重要であり、正しいリンクが提供されることで作業効率が高まります。

## articles/search/tutorial-optimize-indexing-push-api.md{#item-ef0e96}

<details>
<summary>Diff</summary>
````diff
@@ -365,7 +365,7 @@ You can explore the populated search index after the program has run programmati
 
 ### Programatically
 
-There are two main options for checking the number of documents in an index: the [Count Documents API](/rest/api/searchservice/count-documents) and the [Get Index Statistics API](/rest/api/searchservice/get-index-statistics). Both paths require time to process so don't be alarmed if the number of documents returned is initially lower than you expect.
+There are two main options for checking the number of documents in an index: the [Count Documents API](/rest/api/searchservice/documents/count) and the [Get Index Statistics API](/rest/api/searchservice/indexes/get-statistics). Both paths require time to process so don't be alarmed if the number of documents returned is initially lower than you expect.
 
 #### Count Documents
 
@@ -389,7 +389,7 @@ In Azure portal, from the left navigation pane, and find the **optimize-indexing
 
   ![List of Azure AI Search indexes](media/tutorial-optimize-data-indexing/portal-output.png "List of Azure AI Search indexes")
 
-The *Document Count* and *Storage Size* are based on [Get Index Statistics API](/rest/api/searchservice/get-index-statistics) and can take several minutes to update.
+The *Document Count* and *Storage Size* are based on [Get Index Statistics API](/rest/api/searchservice/indexes/get-statistics) and can take several minutes to update.
 
 ## Reset and rerun
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIリンクの更新"
}
```

### Explanation
この変更は、「tutorial-optimize-indexing-push-api.md」という文書に対するもので、合計で4つの変更があり、2行の追加と2行の削除が行われています。

具体的には、インデックス内のドキュメント数を確認するためのREST APIのリンクが修正されました。古いリンク「/rest/api/searchservice/count-documents」や「/rest/api/searchservice/get-index-statistics」がそれぞれ、「/rest/api/searchservice/documents/count」および「/rest/api/searchservice/indexes/get-statistics」に変更されています。これにより、最新のAPIエンドポイントが反映され、ユーザーが正確な情報をにアクセスできるようになります。

さらに、Azureポータル内の「ドキュメント数」と「ストレージサイズ」が、Get Index Statistics APIに基づいていることを明確に示す記述が更新されました。この変更は、利用者がインデックスに関連するデータを適切に取得するための重要な情報を提供し、正確なAPIの利用を促進することを目的としています。

このようなマイナーな更新でも、最新の情報提供はユーザー体験を向上させるために不可欠であり、正しいAPIリンクは開発者の作業効率を高める役割を果たします。


