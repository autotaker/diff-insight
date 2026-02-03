---
date: '2026-02-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:00bac45...MicrosoftDocs:545d781
summary: スキルセットのデバッグ方法に関するドキュメントがアップデートされ、Azure Cosmos DBのインデクサーやセキュリティ設定について新しい詳細が追加されました。また、TypeScriptを使用したフルテキスト検索ガイドのデータリンクが更新され、サンプルデータの入手が容易になっています。さらに、Cosmos
  DBに関連する新しい画像やPythonサンプルコードのリンクも最新化され、使いやすさが向上しました。加えて、ベクトル検索の設定に関するドキュメントが更新され、圧縮およびアルゴリズム設定が明確化されました。全体として、これらの変更はAzure
  Cognitive Searchの利用を容易にし、ユーザーにとって直感的な設定やデバッグを促進します。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:00bac45...MicrosoftDocs:545d781){target="_blank"}

# ハイライト

- スキルセットのデバッグ方法に関するドキュメントがアップデートされ、Azure Cosmos DBのインデクサーやセキュリティ設定に関する詳細が追加されました。
- TypeScriptを用いたフルテキスト検索ガイドのデータリンクが更新され、サンプルデータの入手が容易になりました。
- Cosmos DBに関連する新しい画像がドキュメントに追加され、視覚的な理解を助けます。
- Pythonサンプルコードのリンクが最新化され、使いやすくなったサンプルを提供します。
- ベクトル検索の設定に関するドキュメントが更新され、圧縮およびアルゴリズム設定が明確化されました。

## 新機能

- Cosmos DBに関連する新しい画像が追加され、視覚的なガイダンスが加わった。

## 破壊的変更

- 破壊的変更は示されていませんが、いくつかのリンクが更新されており、古いリンクを使っている場合は注意が必要です。

## その他の更新

- 日付やサンプルコードのリンク、インデックス操作の制限などが最新の情報に更新されました。

# インサイト

この記事の変更はAzure Cognitive Searchと関連ツールの利用を容易にし、最新の情報に基づいて実装を進めることを可能にします。特に、Cosmos DBとの連携に関する視覚資料が追加されることで、ユーザーは設定やデバッグセッションをより直感的に理解することができるようになります。これらの画像は、具体例を示すことにより、学習プロセスを効率化します。

さらに、TypeScriptに関連するガイドのリンク更新は、ユーザーが直面するデータ取得の問題を解消し、スムーズな実装を支援します。Pythonのサンプルコードが最新化されたこともまた、開発者が迅速に最新のベストプラクティスに基づいた開発を行える環境を整えます。

インデックス操作に関する制限情報の更新は、Azure AI Searchを利用する際の性能評価や制限理解に役立ちます。これにより、開発者は制度的にサポートされる最大限度を理解し、パフォーマンスを最適化するための計画を立てやすくなるでしょう。

最後に、ベクトル検索の設定に関するドキュメントの詳細は、特に最近のAIおよび機械学習の進展を反映したものであり、ユーザーが最新の検索技術を適用する上での指針となることが期待されます。圧縮アルゴリズムやデータ構造の変更には、現場での実用性が高まる記述が加えられており、このドキュメントを通じてベクトル検索の実装効率が向上するでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-how-to-debug-skillset.md](#item-31db42) | minor update | スキルセットのデバッグ方法に関する記事の更新 | modified | 13 | 5 | 18 | 
| [full-text-typescript.md](#item-6630e8) | minor update | TypeScriptによるフルテキスト検索のクイックスタート記事のリンク更新 | modified | 1 | 1 | 2 | 
| [cosmos-db-document.png](#item-0340ce) | new feature | Cosmos DBドキュメントの画像追加 | added | 0 | 0 | 0 | 
| [cosmos-db-source.png](#item-3e58a3) | new feature | Cosmos DBソースの画像追加 | added | 0 | 0 | 0 | 
| [search-how-to-create-indexers.md](#item-de71fb) | minor update | Pythonのサンプルコードリンク更新 | modified | 1 | 1 | 2 | 
| [search-how-to-load-search-index.md](#item-a72573) | minor update | CRUD操作のサンプルコードリンク更新 | modified | 1 | 1 | 2 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | インデックス操作に関する制限の更新 | modified | 1 | 0 | 1 | 
| [vector-search-how-to-truncate-dimensions.md](#item-8350a3) | minor update | ベクトル検索に関する設定の更新 | modified | 18 | 27 | 45 | 


# Modified Contents
## articles/search/cognitive-search-how-to-debug-skillset.md{#item-31db42}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/08/2025
+ms.date: 01/31/2026
 ms.update-cycle: 365-days
 ms.custom:
   - ignite-2023
@@ -38,15 +38,15 @@ Debug sessions work with all generally available [indexer data sources](search-d
 
 + Azure Cosmos DB for MongoDB indexer.
 
-+ For the Azure Cosmos DB for NoSQL, if a row fails during index and there's no corresponding metadata, the debug session might not pick the correct row.
++ For Azure Cosmos DB for NoSQL, if a row fails during index and there's no corresponding metadata, the debug session might not pick the correct row.
 
-+ For the SQL API of Azure Cosmos DB, if a partitioned collection was previously non-partitioned, the debug session won't find the document.
++ For the NoSQL API of Azure Cosmos DB, if a partitioned collection was previously non-partitioned, the debug session won't find the document.
 
 + For custom skills, a user-assigned managed identity isn't supported for a debug session connection to Azure Storage. As stated in the prerequisites, you can use a system managed identity, or specify a full access connection string that includes a key. For more information, see [Connect a search service to other Azure resources using a managed identity](search-how-to-managed-identities.md).
 
 ## Security and permissions
 
-+ To save a debug session to Azure storage, the search service identity must have **Storage Blob Data Contributor** permissions on Azure Storage. Otherwise, plan on choosing a full access connection string for the debug session connection to Azure Storage.
++ To save a debug session to Azure Storage, the search service identity must have **Storage Blob Data Contributor** permissions on Azure Storage. Otherwise, plan on choosing a full access connection string for the debug session connection to Azure Storage.
 
 + If the Azure Storage account is behind a firewall, configure it to [allow search service access](search-indexer-howto-access-ip-restricted.md).
 
@@ -66,10 +66,18 @@ Debug sessions work with all generally available [indexer data sources](search-d
 
 1. In **Document to debug**, choose the first document in the index or select a specific document. If you select a specific document, depending on the data source, you're asked for a URI or a row ID.
 
-   If your specific document is a blob, provide the blob URI. You can find the URI in the blob property page in the Azure portal.
+   For a specific document in Blob storage: provide the blob URI. You can find the URI in the blob property page in the Azure portal.
 
    :::image type="content" source="media/cognitive-search-debug/copy-blob-url.png" lightbox="media/cognitive-search-debug/copy-blob-url.png" alt-text="Screenshot of the URI property in blob storage." border="true":::
 
+   For a specific document in Azure CosmosDB for NoSQL: provide the document key in the search index for the value, and the ID of the entity in Cosmos DB for the partition key.
+
+   :::image type="content" source="media/cognitive-search-debug/cosmos-db-source.png" lightbox="media/cognitive-search-debug/cosmos-db-source.png" alt-text="Screenshot of the properties in Cosmos DB." border="true":::
+
+   Here's the debug session configuration for the Cosmos DB example.
+
+   :::image type="content" source="media/cognitive-search-debug/cosmos-db-document.png" lightbox="media/cognitive-search-debug/cosmos-db-document.png" alt-text="Screenshot of the Cosmos DB properties in debug session configuration." border="true":::
+
 1. In **Storage account**, choose a general-purpose storage account for caching the debug session.
 
 1. Select **Authenticate using managed identity** if you previously assigned **Storage Blob Data Contributor** permissions to the search service system-managed identity. If you don't check this box, the search service connects using a full access connection string.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スキルセットのデバッグ方法に関する記事の更新"
}
```

### Explanation
このコードの変更は、Azure Cognitive Searchに関連するドキュメント「スキルセットのデバッグ方法」の更新を表しています。主な変更点には以下が含まれます。

- ドキュメントの日付が「2025年5月8日」から「2026年1月31日」に変更されました。
- Azure Cosmos DB for MongoDBインデクサーについての説明が追加され、NoSQL API及びSQL APIに関するセクションが更新されました。
- デバッグセッションをAzure Storageに保存する際のセキュリティと権限に関する内容が明確化され、ストレージアカウントがファイアウォールの背後にある場合の設定方法が追記されました。
- Blobストレージ及びCosmosDBの特定のドキュメントの処理についての具体的な手順や構成画像が追加されました。

これらの変更により、ユーザーはAzure Cognitive Searchのデバッグプロセスに関するより明確で具体的な情報を得ることができます。

## articles/search/includes/quickstarts/full-text-typescript.md{#item-6630e8}

<details>
<summary>Diff</summary>
````diff
@@ -520,7 +520,7 @@ console.log(`Index named ${index.name} has been created.`);
 
 In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this case, we'll programmatically push the documents to the index.
 
-Document inputs might be rows in a database, blobs in Blob storage, or, as in this sample, JSON documents on disk. You can either download [hotels.json](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels.json) or create your own *hotels.json* file with the following content:
+Document inputs might be rows in a database, blobs in Blob storage, or, as in this sample, JSON documents on disk. You can either download [hotels.json](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart-keyword-search/hotels.json) or create your own *hotels.json* file with the following content:
 
 
 Similar to what we did with the indexDefinition, we also need to import `hotels.json` at the top of *index.ts* so that the data can be accessed in our main function.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptによるフルテキスト検索のクイックスタート記事のリンク更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchに関する記事「TypeScriptによるフルテキスト検索のクイックスタート」の一部更新を示しています。主な変更点は以下の通りです。

- ドキュメント入力として使用される「hotels.json」のダウンロードリンクが更新されました。以前のリンクは無効なものでしたが、新しいリンク（`https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart-keyword-search/hotels.json`）に置き換えられました。
- この変更は、ユーザーが必要なサンプルデータを正しく取得できるようにするためのもので、クイックスタートガイドの利用体験を向上させることを目的としています。

全体として、この更新によりユーザーは最新のデータサンプルにアクセスでき、Azure AI Searchを利用したフルテキスト検索の実装がスムーズになるでしょう。

## articles/search/media/cognitive-search-debug/cosmos-db-document.png{#item-0340ce}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Cosmos DBドキュメントの画像追加"
}
```

### Explanation
このコードの変更は、Azure Cognitive Searchにおける「Cosmos DBドキュメント」の画像が新たに追加されたことを示しています。具体的には、`cosmos-db-document.png`というファイルが新しくリポジトリに含まれました。

- 画像は、ドキュメントに関連する情報を視覚的に提供するためのものであり、ユーザーに対してCosmos DBを利用したデバッグセッションの設定等に関する具体的なビジュアルを提供します。
- これにより、文章だけでは伝えきれない内容を画像を通して分かりやすくし、学習や実装をサポートする効果が期待されます。

全体として、画像の追加はドキュメントの質を向上させ、利用者の理解を助けるための重要なステップと言えるでしょう。

## articles/search/media/cognitive-search-debug/cosmos-db-source.png{#item-3e58a3}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Cosmos DBソースの画像追加"
}
```

### Explanation
このコードの変更は、Azure Cognitive Searchに関するドキュメントに新しい画像「cosmos-db-source.png」が追加されたことを示しています。

- この画像は、Cosmos DBソースに関連する情報を視覚的に提供するために使用されます。具体的には、データのソースとしてCosmos DBを利用する際の設定や構成を視覚的に示すもので、ユーザーが理解しやすくなっています。
- 画像の追加により、テキストだけでは伝えきれない内容を補完し、学習や実装をサポートする重要な資源となります。

全体として、この変更はドキュメントの価値を向上させ、利用者がCosmos DBを利用したAzure Cognitive Searchの機能をより効果的に理解できるようにすることを目的としています。

## articles/search/search-how-to-create-indexers.md{#item-de71fb}

<details>
<summary>Diff</summary>
````diff
@@ -210,7 +210,7 @@ For Azure AI Search, the Azure SDKs implement generally available features. As s
 | .NET | [SearchIndexerClient](/dotnet/api/azure.search.documents.indexes.searchindexerclient) | [DotNetHowToIndexers](https://github.com/Azure-Samples/search-dotnet-getting-started/tree/master/DotNetHowToIndexers) |
 | Java | [SearchIndexerClient](/java/api/com.azure.search.documents.indexes.searchindexerclient) | [CreateIndexerExample.java](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/src/samples/java/com/azure/search/documents/indexes/CreateIndexerExample.java) |
 | JavaScript | [SearchIndexerClient](/javascript/api/@azure/search-documents/searchindexerclient) | [Indexers](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/search/search-documents/samples/v11/javascript) |
-| Python | [SearchIndexerClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexerclient) | [sample_indexers_operations.py](https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/search/azure-search-documents/samples/sample_indexers_operations.py) |
+| Python | [SearchIndexerClient](/python/api/azure-search-documents/azure.search.documents.indexes.searchindexerclient) | [sample_indexers_operations.py](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/samples/sample_indexer_crud.py) |
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonのサンプルコードリンク更新"
}
```

### Explanation
このコードの変更は、「how-to-create-indexers.md」というドキュメント内にあるPythonに関連するサンプルコードのリンクが更新されたことを示しています。

- 具体的には、以前のリンク `sample_indexers_operations.py` が、新しいサンプルコードへのリンク `sample_indexer_crud.py` に置き換えられました。
- これは、Azure AI Searchに関連するPython SDKのサンプルをより最新の情報に更新することを目的としています。新しいリンクが提供する内容は、Indexersの操作に関するより良い例を通じてユーザーに学びの機会を提供します。

全体として、この変更はドキュメントの正確性を高めるものであり、利用者が最新の技術や方法論を有効に活用できるようサポートしています。

## articles/search/search-how-to-load-search-index.md{#item-a72573}

<details>
<summary>Diff</summary>
````diff
@@ -167,7 +167,7 @@ The Azure SDK for Python provides the following APIs for simple and bulk documen
 
 Code samples include:
 
-+ [sample_crud_operations.py](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/samples/sample_crud_operations.py)
++ [sample_crud_operations.py](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/samples/sample_documents_crud.py)
 
 + Be sure to check the [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples) repo for code examples showing how to index vector fields.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "CRUD操作のサンプルコードリンク更新"
}
```

### Explanation
このコードの変更は、「how-to-load-search-index.md」というドキュメントにおけるCRUD操作に関連するPythonのサンプルコードのリンクが更新されたことを示しています。

- 具体的には、以前のリンク `sample_crud_operations.py` が、新しいリンク `sample_documents_crud.py` に置き換えられました。この更新は、より適切なサンプルを提供するためのものであり、ユーザーがドキュメントを通じて最新のコードを参照できるようにします。
- さらに、新しいリポジトリ `[azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples)` のリンクも追加され、ベクターフィールドをインデックスする方法に関するサンプルコードを確認するように促されています。

全体として、この変更はドキュメントの情報を最新の狙った内容にアップデートし、利用者がさらに便利なリソースを活用できるようにしています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -258,6 +258,7 @@ General:
 Indexing APIs:
 
 + Supported maximum 1,000 documents per batch of index uploads, merges, or deletes.
++ Each request supports between 1 and 32,000 indexing actions.
 
 Query APIs:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス操作に関する制限の更新"
}
```

### Explanation
このコードの変更は、「search-limits-quotas-capacity.md」というドキュメントにおいて、インデックス操作に関する制限が更新されたことを示しています。

- 具体的には、インデックスのアップロード、マージ、または削除のバッチごとに最大1,000ドキュメントがサポートされることに加え、各リクエストで1〜32,000のインデキシングアクションがサポートされることが明確に記載されました。この情報は、開発者がインデックス操作を行う際のパフォーマンスや制約を理解するのに役立ちます。

全体として、この変更は利用者に対してより具体的な制限を提供し、Azure AI Searchのインデックス操作に関する利用方法を明確化することを目的としています。

## articles/search/vector-search-how-to-truncate-dimensions.md{#item-8350a3}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.update-cycle: 180-days
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 10/08/2025
+ms.date: 01/31/2026
 ---
 
 # Truncate dimensions using MRL compression
@@ -75,10 +75,10 @@ The following example illustrates a vector search configuration that meets the r
     "profiles": [ 
       { 
         "name": "use-bq-with-mrl", 
-        "compression": "use-mrl,use-bq", 
-        "algorithm": "use-hnsw" 
-      } 
-    ],
+        "compression": "use-bq-with-truncation", 
+        "algorithm": "use-hnsw" 
+      } 
+    ],
     "algorithms": [
        {
           "name": "use-hnsw",
@@ -91,38 +91,29 @@ The following example illustrates a vector search configuration that meets the r
           }
        }
     ],
-    "compressions": [ 
-      { 
-        "name": "use-mrl", 
-        "kind": "binaryQuantization", 
+    "compressions": [ 
+      { 
+        "name": "use-bq-with-truncation", 
+        "kind": "binaryQuantization", 
         "rescoringOptions": {
             "enableRescoring": true,
             "defaultOversampling": 10,
             "rescoreStorageMethod": "preserveOriginals"
         },
-        "truncationDimension": 1024
-      }, 
-      { 
-        "name": "use-bq", 
-        "kind": "binaryQuantization", 
-        "rescoringOptions": {
-            "enableRescoring": true,
-            "defaultOversampling": 10,
-            "rescoreStorageMethod": "discardOriginals"
-        }
-       } 
-    ] 
-  } 
-} 
+        "truncationDimension": 1024
+      }
+    ]
+  }
+}
 ```
 
-Here's an example of a [fully specified vector field definition](/rest/api/searchservice/indexes/create-or-update#searchfield) that satisfies the requirements for MRL. Recall that vector fields must:
+The following JSON shows the vector field definition that uses this profile:
 
-- Be of type `Edm.Half` or `Edm.Single`.
+- Data type is either `Collection(Edm.Half)` or `Collection(Edm.Single)`.
 
-- Have a `vectorSearchProfile` property that specifies the algorithm and compression settings.
+- The field has a `vectorSearchProfile` property that specifies the algorithm and compression settings.
 
-- Have a `dimensions` property that specifies the number of dimensions for scoring and ranking results. Its value should be the dimensions limit of the model you're using (1,536 for text-embedding-3-small).
+- The field has a `dimensions` property that specifies the number of dimensions for scoring and ranking results. Its value should be the dimensions limit of the model you're using (1,536 for text-embedding-3-small).
 
 ```json
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索に関する設定の更新"
}
```

### Explanation
このコードの変更は、「vector-search-how-to-truncate-dimensions.md」というドキュメントの内容が更新され、ベクトル検索の圧縮およびアルゴリズムの設定に関連する詳細が修正されたことを示しています。

- 具体的には、まず、日付が `10/08/2025` から `01/31/2026` に変更され、ドキュメントの新しい更新日が設定されました。
- 次に、圧縮の設定が変更され、`use-mrl` から `use-bq-with-truncation` に更新されました。また、`algorithm` の設定も変更され、正確な構成を示すようになりました。
- その後、例として示されるJSON構造が修正され、フィールド定義に関する情報がより具体的になっています。特に、データ型やプロパティに関する説明が更新され、明確化が図られています。

全体として、この変更はベクトル検索の使用にあたり、より実用的かつ明確な情報を提供することを目的としており、ユーザーがより効果的にベクトル検索機能を利用できるように支援しています。


