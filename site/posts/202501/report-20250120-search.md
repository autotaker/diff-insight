---
date: '2025-01-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1d7cc3c...MicrosoftDocs:06d2c74
summary: 今回のコード差分では、複数のドキュメントファイルに対する小規模な更新が中心です。主な変更点は、日付の更新と特定の表現や説明の微調整です。これにより、情報を最新の状態に保ちながら、より正確で明確な内容を提供することが目的とされています。新機能の追加はありませんが、互換性を損なう大きな変更もないため、ユーザーに対する影響はありません。全体として、この更新はドキュメントの整合性と信頼性を高め、最新の技術情報をユーザーに提供するための重要なプロセスです。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1d7cc3c...MicrosoftDocs:06d2c74){target="_blank"}

# ハイライト

今回のコード差分は、複数のドキュメントファイルにおける小規模な更新が中心です。主な変更点は以下の通りです：

- ドキュメントに記載されている日付の更新
- 特定の表現や説明の微調整

これらの変更は、情報を最新の状態に保ちつつ、読者により正確で明確な情報を提供することを意図しています。

## 新機能
特に新機能が追加されたわけではありませんが、文書の内容は改良されています。

## 互換性に関する変更
互換性を損なうような大きな変更はありません。

## その他の更新
- `cognitive-search-create-custom-skill-example.md`: 日付とAPIの説明微調整
- `cognitive-search-custom-skill-scale.md`: 日付更新
- `cognitive-search-incremental-indexing-conceptual.md`: 日付とAPI呼び出し例の修正
- `cognitive-search-tutorial-blob-dotnet.md`: 日付更新
- `cognitive-search-tutorial-blob.md`: 日付更新
- `index-sql-relational-data.md`: 日付更新と表現・画像キャプションの修正
- `search-get-started-arm.md`: 日付更新
- `search-howto-index-one-to-many-blobs.md`: 日付と文の表現修正
- `search-howto-monitor-indexers.md`: 日付更新
- `tutorial-create-custom-analyzer.md`: 日付更新
- `tutorial-csharp-create-mvc-app.md`: 日付更新

# インサイト

このコード差分が主に日付や細かい表現の変更に焦点を当てていることから、メンテナンスの一環として行われた更新であると考えられます。ファイルの全体的な機能や構成には手を加えていないため、既存のユーザーに対して影響を与えずに最新の情報を反映する形で改良が施されています。

日付の更新は、一見単純な変更に思えるかもしれませんが、文書が受け手にとってどれだけ信頼できるかの指標となります。特に技術文書では、最新情報に基づいて手順を理解することが重要なので、このような定期的なアップデートは、ユーザーに対する誠実さを示すものです。

また、微細なテキストの修正も見逃せません。例えば、「won't」から「doesn't」などの表現の修正は、文章をより自然で読みやすくするだけでなく、技術的な正確性を確保するための重要な変更です。これにより、ユーザーはよりスムーズで効率的にドキュメントを活用できるようになります。

全体として、この更新はドキュメントの整合性と信頼性を高め、ユーザーに最新で正確な技術情報を提供する基盤を築くための必須のプロセスであると言えます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-create-custom-skill-example.md](#item-24ed00) | minor update | カスタムスキル作成の例に関する日付と説明の更新 | modified | 2 | 2 | 4 | 
| [cognitive-search-custom-skill-scale.md](#item-efc3d8) | minor update | カスタムスキルスケーリングに関する日付の更新 | modified | 1 | 1 | 2 | 
| [cognitive-search-incremental-indexing-conceptual.md](#item-7bafcc) | minor update | インクリメンタルインデクシングに関する日付と例の更新 | modified | 2 | 2 | 4 | 
| [cognitive-search-tutorial-blob-dotnet.md](#item-ba889d) | minor update | Blob .NET チュートリアルの日付更新 | modified | 1 | 1 | 2 | 
| [cognitive-search-tutorial-blob.md](#item-ff148f) | minor update | Blob チュートリアルの日付更新 | modified | 1 | 1 | 2 | 
| [index-sql-relational-data.md](#item-8d9133) | minor update | SQLデータのインデックス作成に関するチュートリアルの内容更新 | modified | 8 | 8 | 16 | 
| [search-get-started-arm.md](#item-9287ad) | minor update | Azure AI Searchのクイックスタートの日付更新 | modified | 1 | 1 | 2 | 
| [search-howto-index-one-to-many-blobs.md](#item-04ada2) | minor update | 1対多のBlobインデックス作成ガイドの内容更新 | modified | 5 | 5 | 10 | 
| [search-howto-monitor-indexers.md](#item-0e3133) | minor update | インデクサーの監視ガイドの日付更新 | modified | 1 | 1 | 2 | 
| [tutorial-create-custom-analyzer.md](#item-ad5520) | minor update | カスタムアナライザー作成チュートリアルの日付更新 | modified | 1 | 1 | 2 | 
| [tutorial-csharp-create-mvc-app.md](#item-608a5d) | minor update | ASP.NET Coreでの検索アプリ作成チュートリアルの日付更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/cognitive-search-create-custom-skill-example.md{#item-24ed00}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: gmndrg
 ms.author: gimondra
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 03/18/2024
+ms.date: 01/18/2025
 ms.custom:
   - devx-track-csharp
   - ignite-2023
@@ -308,7 +308,7 @@ namespace SampleSkills
 }
 ```
 
-Make sure to enter your own *key* value in the `key` constant based on the key you got when signing up for the Bing entity search API.
+Make sure to enter your own *key* value in the `key` constant based on the key you got when signing up for the Bing Entity search API.
 
 ## Test the function from Visual Studio
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムスキル作成の例に関する日付と説明の更新"
}
```

### Explanation
この変更は、`cognitive-search-create-custom-skill-example.md`ファイルに対する小規模な更新です。主な変更点には、ドキュメントの日付の修正とテキストの微調整が含まれています。具体的には、文書の日付が2024年3月18日から2025年1月18日に変更され、Bing エンティティ検索 API の説明において「entity」という単語の大文字が修正されました。これにより、内容がより正確かつ最新の情報を反映するようになっています。

## articles/search/cognitive-search-custom-skill-scale.md{#item-efc3d8}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 03/18/2024
+ms.date: 01/18/2025
 ---
 
 # Efficiently scale out a custom skill
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムスキルスケーリングに関する日付の更新"
}
```

### Explanation
この変更は、`cognitive-search-custom-skill-scale.md`ファイルにおける小規模な更新です。主な変更内容は、文書の日付が2024年3月18日から2025年1月18日に変更されたことです。この更新により、文書が最新の情報を反映するようになり、読者に正確なタイムラインを提供します。その他の内容には影響はありません。この修正は、ドキュメントの整合性を保つための重要なステップです。

## articles/search/cognitive-search-incremental-indexing-conceptual.md{#item-7bafcc}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 06/25/2024
+ms.date: 01/17/2025
 ---
 
 # Incremental enrichment and caching in Azure AI Search
@@ -40,7 +40,7 @@ The following example illustrates an indexer with caching enabled. See [Enable e
 To use the cache property, you can use 2020-06-30-preview or later when you [create or update an indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true). We recommend the latest preview API.
 
 ```json
-POST https://[search service name].search.windows.net/indexers?api-version=2024-05-01-rreview
+POST https://[YOUR-SEARCH-SERVICE-NAME].search.windows.net/indexers?api-version=2024-05-01-preview
     {
         "name": "myIndexerName",
         "targetIndexName": "myIndex",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インクリメンタルインデクシングに関する日付と例の更新"
}
```

### Explanation
この変更は、`cognitive-search-incremental-indexing-conceptual.md`ファイルにおける小規模な更新です。主な変更点は2つあり、最初に文書の日付が2024年6月25日から2025年1月17日に変更され、次にAPI呼び出しの例において、`[search service name]`の部分が`[YOUR-SEARCH-SERVICE-NAME]`に修正されました。この修正により、ユーザーにとってより具体的で適切な情報が提供され、最新の仕様を反映しています。これにより、ドキュメントの正確性と利用しやすさが向上しています。

## articles/search/cognitive-search-tutorial-blob-dotnet.md{#item-ba889d}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ manager: nitinme
 
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 03/06/2024
+ms.date: 01/17/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blob .NET チュートリアルの日付更新"
}
```

### Explanation
この変更は、`cognitive-search-tutorial-blob-dotnet.md`ファイルにおける小規模な更新です。主な変更点は、文書の日付が2024年3月6日から2025年1月17日に変更されたことです。この更新により、チュートリアルが最新の情報を反映し、読者に正確なタイムラインを提供することを目的としています。他の内容には影響がなく、この修正はドキュメントの整合性と信頼性を向上させるために重要です。

## articles/search/cognitive-search-tutorial-blob.md{#item-ff148f}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: tutorial
-ms.date: 03/06/2024
+ms.date: 01/17/2025
 ---
 
 # REST Tutorial: Use skillsets to generate searchable content in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blob チュートリアルの日付更新"
}
```

### Explanation
この変更は、`cognitive-search-tutorial-blob.md`ファイルにおける小規模な更新です。具体的には、文書の日付が2024年3月6日から2025年1月17日に変更されました。この更新により、チュートリアルが最新の情報を反映し、読者に正確な情報を提供することを意図しています。内容自体は変更されていないため、主にドキュメントの整合性を保つための修正となります。このような日付の更新は、読者が情報の新しさを判断するのに役立ちます。

## articles/search/index-sql-relational-data.md{#item-8d9133}

<details>
<summary>Diff</summary>
````diff
@@ -9,16 +9,16 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 03/18/2024
+ms.date: 01/18/2025
 ---
 
 # How to model relational SQL data for import and indexing in Azure AI Search
 
-Azure AI Search accepts a flat rowset as input to the [indexing pipeline](search-what-is-an-index.md). If your source data originates from joined tables in a SQL Server relational database, this article explains how to construct the result set, and how to model a parent-child relationship in an Azure AI Search index.
+Azure AI Search accepts a flat rowset as input to the [indexing pipeline](search-what-is-an-index.md). If your source data originates from joined tables in a SQL Server relational database, this article explains how to construct the rowset, and how to model a parent-child relationship in an Azure AI Search index.
 
 As an illustration, we refer to a hypothetical hotels database, based on [demo data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/hotels). Assume the database consists of a `Hotels$` table with 50 hotels, and a `Rooms$` table with rooms of varying types, rates, and amenities, for a total of 750 rooms. There's a one-to-many relationship between the tables. In our approach, a view provides the query that returns 50 rows, one row per hotel, with associated room detail embedded into each row.
 
-   ![Tables and view in the Hotels database](media/index-sql-relational-data/hotels-database-tables-view.png "Tables and view in the Hotels database")
+![Tables and view in the Hotels database](media/index-sql-relational-data/hotels-database-tables-view.png "Screenshot of tables and view in the Hotels database.")
 
 ## The problem of denormalized data
 
@@ -32,9 +32,9 @@ ON Rooms$.HotelID = Hotels$.HotelID
 
 Results from this query return all of the Hotel fields, followed by all Room fields, with preliminary hotel information repeating for each room value.
 
-   ![Denormalized data, redundant hotel data when room fields are added](media/index-sql-relational-data/denormalize-data-query.png "Denormalized data, redundant hotel data when room fields are added")
+![Denormalized data, redundant hotel data when room fields are added](media/index-sql-relational-data/denormalize-data-query.png "Screenshot of denormalized data, redundant hotel data when room fields are added.")
 
-While this query succeeds on the surface (providing all of the data in a flat row set), it fails in delivering the right document structure for the expected search experience. During indexing, Azure AI Search creates one search document for each row ingested. If your search documents looked like the above results, you would have perceived duplicates - seven separate documents for the Old Century Hotel alone. A query on "hotels in Florida" would return seven results for just the Old Century Hotel, pushing other relevant hotels deep into the search results.
+While this query succeeds on the surface (providing all of the data in a flat rowset), it fails in delivering the right document structure for the expected search experience. During indexing, Azure AI Search creates one search document for each row ingested. If your search documents looked like the above results, you would have perceived duplicates - seven separate documents for the Old Century Hotel alone. A query on "hotels in Florida" would return seven results for just the Old Century Hotel, pushing other relevant hotels deep into the search results.
 
 To get the expected experience of one document per hotel, you should provide a rowset at the right granularity, but with complete information. This article explains how.
 
@@ -94,11 +94,11 @@ The solution is to capture the room detail as nested JSON, and then insert the J
 
    The following screenshot shows the resulting view, with the *Rooms* nvarchar field at the bottom. The *Rooms* field exists only in the HotelRooms view.
 
-   ![HotelRooms view](media/index-sql-relational-data/hotelsrooms-view.png "HoteRooms view")
+   ![HotelRooms view](media/index-sql-relational-data/hotelsrooms-view.png "Screenshot of the HotelRooms view.")
 
 1. Run `SELECT * FROM dbo.HotelRooms` to retrieve the row set. This query returns 50 rows, one per hotel, with associated room information as a JSON collection. 
 
-   ![Rowset from HotelRooms view](media/index-sql-relational-data/hotelrooms-rowset.png "Rowset from HotelRooms view")
+   ![Rowset from HotelRooms view](media/index-sql-relational-data/hotelrooms-rowset.png "Screenshot of the rowset from the HotelRooms view.")
 
 This rowset is now ready for import into Azure AI Search.
 
@@ -159,7 +159,7 @@ As noted in [Model complex types](search-howto-complex-data-types.md): "the docu
 
 Using your own data set, you can use the [Import data wizard](search-import-data-portal.md) to create and load the index. The wizard detects the embedded JSON collection, such as the one contained in *Rooms*, and infers an index schema that includes a complex type collection. 
 
-  ![Index inferred by Import data wizard](media/index-sql-relational-data/search-index-rooms-complex-collection.png "Index inferred by Import data wizard")
+  ![Index inferred by Import data wizard](media/index-sql-relational-data/search-index-rooms-complex-collection.png "Screenshot of the an index inferred by Import data wizard.")
 
 Try the following quickstart to learn the basic steps of the Import data wizard.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SQLデータのインデックス作成に関するチュートリアルの内容更新"
}
```

### Explanation
この変更は、`index-sql-relational-data.md`ファイルに対する小規模な更新です。主な修正点は、文書の日付が2024年3月18日から2025年1月18日に更新されたことと、いくつかの文の表現が明確にされ、画像のキャプションが改善された点です。具体的には、元の「result set」という表現が「rowset」に修正され、各画像のキャプションについてもより分かりやすい表現に変更されています。

これにより、チュートリアルは最新の情報を反映し、内容が理解しやすくなります。特に、SQLデータをAzure AI Searchに取り込む際の手順や注意点をより明確に伝えることを目的としています。このような更新は、読者にとってより価値のある情報を提供するために重要です。

## articles/search/search-get-started-arm.md{#item-9287ad}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.custom:
   - mode-arm
   - devx-track-arm-template
   - ignite-2023
-ms.date: 04/24/2024
+ms.date: 01/17/2025
 ---
 
 # Quickstart: Deploy Azure AI Search using an Azure Resource Manager template
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのクイックスタートの日付更新"
}
```

### Explanation
この変更は、`search-get-started-arm.md`ファイルに関する小規模な更新であり、主に文書の日付が2024年4月24日から2025年1月17日に変更されました。この更新は、クイックスタートガイドの情報が最新であることを確認し、読者に正確な情報を提供することを目的としています。日付の変更だけですが、文書の信頼性と新しさを保つことができる重要な修正です。

## articles/search/search-howto-index-one-to-many-blobs.md{#item-04ada2}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 01/18/2024
+ms.date: 01/18/2025
 ---
 
 # Indexing blobs and files to produce multiple search documents
@@ -105,12 +105,12 @@ When you create an indexer with `delimitedText` **parsingMode**, it might feel n
 }
 ```
 
-However, this mapping won't result in four documents showing up in the index because the `recordid` field isn't unique _across blobs_. Hence, we recommend you to make use of the implicit field mapping applied from the `AzureSearch_DocumentKey` property to the key index field for "one-to-many" parsing modes.
+However, this mapping doesn't result in four documents showing up in the index because the `recordid` field isn't unique _across blobs_. Hence, we recommend you to make use of the implicit field mapping applied from the `AzureSearch_DocumentKey` property to the key index field for "one-to-many" parsing modes.
 
 If you do want to set up an explicit field mapping, make sure that the _sourceField_ is distinct for each individual entity **across all blobs**.
 
 > [!NOTE]
-> The approach used by `AzureSearch_DocumentKey` of ensuring uniqueness per extracted entity is subject to change and therefore you should not rely on it's value for your application's needs.
+> The approach used by `AzureSearch_DocumentKey` of ensuring uniqueness per extracted entity is subject to change and therefore you shouldn't rely on its value for your application's needs.
 
 ## Specify the index key field in your data
 
@@ -132,9 +132,9 @@ id, temperature, pressure, timestamp
 2, 120, 3,"2022-05-11T00:00:00Z" 
 ```
 
-Notice that each document contains the `id` field, which is defined as the `key` field in the index. In such a case, even though a document-unique `AzureSearch_DocumentKey` will be generated, it won't be used as the "key" for the document. Rather, the value of the `id` field will be mapped to the `key` field
+Notice that each document contains the `id` field, which is defined as the `key` field in the index. In such a case, even though a document-unique `AzureSearch_DocumentKey` is generated, it isn't used as the "key" for the document. Rather, the value of the `id` field is mapped to the `key` field
 
-Similar to the previous example, this mapping won't result in four documents showing up in the index because the `id` field isn't unique _across blobs_. When this is the case, any json entry that specifies an `id` will result in a merge on the existing document instead of an upload of a new document, and the state of the index will reflect the latest read entry with the specified `id`.
+Similar to the previous example, this mapping doesn't result in four documents showing up in the index because the `id` field isn't unique _across blobs_. When this is the case, any json entry that specifies an `id` results in a merge on the existing document instead of an upload of a new document, and the state of the index reflects the latest read entry with the specified `id`.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "1対多のBlobインデックス作成ガイドの内容更新"
}
```

### Explanation
この変更は、`search-howto-index-one-to-many-blobs.md`ファイルに対する小規模な更新で、主に日付の更新といくつかの表現の修正が含まれています。

具体的には、日付が2024年1月18日から2025年1月18日へと変更されました。また、文中の表現について、「won't」から「doesn't」、「should not」から「shouldn't」への修正が行われ、文がより自然な表現になっています。これにより、読者に対して内容がより明確に伝わるようになっています。

全体として、この更新は文書を最新のものに保つとともに、読者に対してより良い理解を提供することを目的としています。

## articles/search/search-howto-monitor-indexers.md{#item-0e3133}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - devx-track-dotnet
   - ignite-2023
 ms.topic: conceptual
-ms.date: 06/25/2024
+ms.date: 01/17/2025
 ---
 
 # Monitor indexer status and results in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーの監視ガイドの日付更新"
}
```

### Explanation
この変更は、`search-howto-monitor-indexers.md`ファイルに対する小規模な更新であり、文書の日付が2024年6月25日から2025年1月17日に変更されました。この日付の更新は、ガイドの内容が最新であることを確保し、読者に正確な情報を提供するために重要です。

文書の内容自体には大きな変更は見られませんが、日付更新によって信頼性が向上し、利用者は最新の情報に基づいてインデクサーの監視方法を学ぶことができます。

## articles/search/tutorial-create-custom-analyzer.md{#item-ad5520}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: tutorial
-ms.date: 03/07/2024
+ms.date: 01/17/2025
 ---
 
 # Tutorial: Create a custom analyzer for phone numbers
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムアナライザー作成チュートリアルの日付更新"
}
```

### Explanation
この変更は、`tutorial-create-custom-analyzer.md`ファイルに対する小規模な更新であり、文書の日付が2024年3月7日から2025年1月17日に変更されました。この日付の更新は、チュートリアルが最新の情報を反映していることを確認するために重要です。

変更された内容自体は日付の更新のみですが、これによって読者は最新の情報に基づいて電話番号用のカスタムアナライザーの作成方法を習得することができ、信頼性の向上につながります。

## articles/search/tutorial-csharp-create-mvc-app.md{#item-608a5d}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.devlang: csharp
 ms.custom:
   - ignite-2023
 ms.topic: tutorial
-ms.date: 04/22/2024
+ms.date: 01/17/2025
 ---
 
 # Create a search app in ASP.NET Core
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ASP.NET Coreでの検索アプリ作成チュートリアルの日付更新"
}
```

### Explanation
この変更は、`tutorial-csharp-create-mvc-app.md`ファイルに対する小規模な更新であり、文書の日付が2024年4月22日から2025年1月17日に変更されました。この日付の更新は、チュートリアルが最新の情報を反映させるために不可欠です。

文書に含まれるチュートリアルは、ASP.NET Coreにおける検索アプリの作成方法に焦点を当てていますが、この日付の更新によってユーザーは新しい情報を得ることができ、より信頼性のあるガイダンスを受けられるようになります。


