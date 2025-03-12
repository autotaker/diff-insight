---
date: '2025-03-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f35ae63...MicrosoftDocs:3791c10
summary: このコードの更新では、Azure Cognitive Search関連のドキュメントに小さな改善と補足が行われました。新機能として、データ変換を強化するために`search-indexer-field-mappings.md`に新関数`fixedLengthEncode`と`toJson`が追加されました。破壊的な変更はありませんが、コードの整形や文言の削除により可読性が向上しています。他の更新では、ドキュメントのスタイリング改善や制約事項の追加が行われ、全体の明確性と有用性が高まっています。これにより、ユーザーはより柔軟かつ理解しやすい情報を得られるようになり、結果的に技術資料としての信頼性が向上しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f35ae63...MicrosoftDocs:3791c10){target="_blank"}

# ハイライト

このコードの更新では、Azure Cognitive Search関連のドキュメントファイルに対して、小さな改善と補足が行われました。以下の新機能や変更点に焦点が当てられます。

## 新機能

- `search-indexer-field-mappings.md`に、新しい関数`fixedLengthEncode`と`toJson`が追加され、データの変換機能が強化されました。これらの新機能により、ユーザーはより柔軟にフィールドデータの変換を行うことができます。

## 破壊的変更

- 特に破壊的な変更はありませんが、コードの整形や不要な文言の削除により、全体の一貫性と可読性が向上しています。

## その他の更新

- `cognitive-search-skill-shaper.md`では、JSONの一貫性を確保するためのスタイリング改善が行われました。
- `search-how-to-index-sql-database.md`では、コンテナ名プロパティに関する制約事項が追加され、理解を助ける注記が補足されています。
- `search-howto-index-mysql.md`でもコンテナ名プロパティに関する制約が追加され、誤入力を防ぐ支援がされています。
- `search-limits-quotas-capacity.md`では、日付の更新と説明の簡素化が行われています。

# インサイト

この一連の更新は、Azure Cognitive Searchに関連するドキュメントの明確性と有用性を高めることを目的としています。各変更は、特定のユーザーケースにおいて情報の正確さ、文書の簡潔さ、そして操作の一貫性を強化する要素を備えています。

特に、インデクサーフィールドマッピングに新機能が追加され、ユーザーはフィールドデータの扱い方をより柔軟にコントロールできるようになりました。これに加えて、コンテナ名の制約について詳細な説明を追加することで、SQLおよびMySQLデータベース関連の記事がよりユーザー目線に立ったものとなっています。このことは、データの整合性を保証し、システムの誤動作を未然に防ぐ手助けとなっています。

スタイリングとコンテンツの一貫性を意識した微調整も多く見られ、これによりドキュメント全体の品質が向上しています。このような改善は、ユーザビリティを高めると同時に、Azure Cognitive Searchに関する知識へのアクセスを容易にするものです。結果として、これらのドキュメントは技術者にとって、今後の参考資料としてより頼りがいのあるものになるといえるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-shaper.md](#item-748c01) | minor update | 記事の小さな更新 (Cognitive Search Skill Shaper) | modified | 1 | 1 | 2 | 
| [search-how-to-index-sql-database.md](#item-86d873) | minor update | SQLデータベースのインデックス作成に関する記事の更新 | modified | 2 | 0 | 2 | 
| [search-howto-index-mysql.md](#item-5d31c4) | minor update | MySQLのインデックス作成に関する記事の更新 | modified | 3 | 0 | 3 | 
| [search-indexer-field-mappings.md](#item-0e4628) | minor update | インデクサーフィールドマッピングに関する記事の更新 | modified | 2 | 0 | 2 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索リミット、クォータ、およびキャパシティに関する記事の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/cognitive-search-skill-shaper.md{#item-748c01}

<details>
<summary>Diff</summary>
````diff
@@ -241,7 +241,7 @@ In this case, the **Shaper** creates a complex type. This structure exists in-me
                     "chapterTitles": [
                       { "title": "Start young", "number": 1},
                       { "title": "Laugh often", "number": 2},
-                      { "title": "Eat, sleep and exercise", "number: 3}
+                      { "title": "Eat, sleep and exercise", "number": 3}
                     ]
                 }
             }
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事の小さな更新 (Cognitive Search Skill Shaper)"
}
```

### Explanation
この変更は、`cognitive-search-skill-shaper.md` というファイル内での小さな更新です。変更内容は、配列内のオブジェクトの構造に一貫性を持たせるためのもので、不要なスペースの削除やコードの整形に関する微調整が含まれています。具体的には、JSON形式で定義された「chapterTitles」の項目の一つにおいて、「number」キーの表記が改善されました。これにより、コードの可読性が向上し、全体の一貫性が保たれています。変更による機能への影響はなく、主にスタイリングの改善が目的です。

## articles/search/search-how-to-index-sql-database.md{#item-86d873}

<details>
<summary>Diff</summary>
````diff
@@ -178,6 +178,8 @@ The data source definition specifies the data to index, credentials, and policie
    + Alternatively, you can specify a managed identity connection string that doesn't include database secrets with the following format: `Initial Catalog|Database=<your database name>;ResourceId=/subscriptions/<your subscription ID>/resourceGroups/<your resource group name>/providers/Microsoft.Sql/servers/<your SQL Server name>/;Connection Timeout=connection timeout length;`.
 
     For more information, see [Connect to Azure SQL Database indexer using a managed identity](search-howto-managed-identities-sql.md).
+> [!NOTE]
+> For the container name property, the value is restricted to only allow letters, numbers, underscores (_), dots (.), single dashes (-), and square brackets ([])
 
 ### Add search fields to an index
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SQLデータベースのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、`search-how-to-index-sql-database.md` というファイルにおける小さな更新です。主に、Azure SQL データベースに関連するインデックス作成の説明を補足するための2つの追加が行われました。具体的には、マネージドID接続文字列に関する情報の後に、コンテナ名プロパティについての制約事項が注記として追加されています。この更新により、ユーザーはコンテナ名に使用できる文字の制限を理解しやすくなり、誤りを減らすことができます。全体として、この変更は文書の内容をより明確にし、ガイダンスを向上させることを目的としています。

## articles/search/search-howto-index-mysql.md{#item-5d31c4}

<details>
<summary>Diff</summary>
````diff
@@ -83,6 +83,9 @@ The data source definition specifies the data to index, credentials, and policie
 
 - Set [`dataDeletionDetectionPolicy`](#DataDeletionDetectionPolicy) if you want to remove search documents from a search index when the source item is deleted.
 
+> [!NOTE]
+> For the container name property, the value is restricted to only allow letters, numbers, underscores (_), dots (.), single dashes (-), and square brackets ([])
+
 ## Create an index
 
 [Create or Update Index](/rest/api/searchservice/indexes/create?view=rest-searchservice-2024-05-01-preview&preserve-view=true) specifies the index schema:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MySQLのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更は、`search-howto-index-mysql.md` というファイルにおいて、小さな更新が行われました。具体的には、MySQL データベースに対するインデックス作成手順に関する情報を補足するために、3つの行が追加されています。新たに追加された内容には、コンテナ名プロパティに関する制限事項が注記として含まれており、使用可能な文字として、アルファベット、数字、アンダースコア、ドット、ハイフン、および角括弧が示されています。この変更によって、ユーザーはデータの整合性を保つために必要な制約を理解しやすくなり、誤った入力を防ぐことが可能になります。全体として、この更新は記事の明確さと正確性を向上させることを目的としています。

## articles/search/search-indexer-field-mappings.md{#item-0e4628}

<details>
<summary>Diff</summary>
````diff
@@ -157,7 +157,9 @@ A field mapping function transforms the contents of a field before it's stored i
 + [base64Encode](#base64EncodeFunction)
 + [base64Decode](#base64DecodeFunction)
 + [extractTokenAtPosition](#extractTokenAtPositionFunction)
++ [fixedLengthEncode](#fixedLengthEncodeFunction)
 + [jsonArrayToStringCollection](#jsonArrayToStringCollectionFunction)
++ [toJson](#toJsonFunction)
 + [urlEncode](#urlEncodeFunction)
 + [urlDecode](#urlDecodeFunction)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーフィールドマッピングに関する記事の更新"
}
```

### Explanation
この変更は、`search-indexer-field-mappings.md` というファイルにおいて、小さな更新が行われました。この変更では、フィールドマッピングの機能に関連する2つの関数が追加されました。それは、`fixedLengthEncode` 関数と `toJson` 関数です。これらの関数は、フィールドの内容を格納する前に変換する際の選択肢を増やし、ユーザーにとってより柔軟なデータ処理を可能にします。この更新により、ドキュメントは最新の機能を反映し、ユーザーがインデクサーのフィールドマッピングをより効果的に利用できるようになることを目指しています。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 01/07/2025
+ms.date: 03/11/2025
 ms.custom:
   - references_regions
   - build-2024
@@ -21,7 +21,7 @@ Maximum limits on storage, workloads, and quantities of indexes and other object
 
 + **Free** is a multitenant shared service that comes with your Azure subscription.
 
-+ **Basic** provides dedicated computing resources for production workloads at a smaller scale, but shares some networking infrastructure with other tenants.
++ **Basic** provides dedicated computing resources for production workloads at a smaller scale.
 
 + **Standard** runs on dedicated machines with more storage and processing capacity at every level. Standard comes in four levels: S1, S2, S3, and S3 HD. S3 High Density (S3 HD) is engineered for [multi-tenancy](search-modeling-multitenant-saas-applications.md) and large quantities of small indexes (3,000 indexes per service). S3 HD doesn't provide the [indexer feature](search-indexer-overview.md) and data ingestion must use APIs that push data from source to index.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索リミット、クォータ、およびキャパシティに関する記事の更新"
}
```

### Explanation
この変更は、`search-limits-quotas-capacity.md` というファイルにおいて行われた小さな更新です。主な変更点は、文書の日付が更新され、基本プランの説明が簡素化されています。具体的には、以前の説明では「他のテナントとのネットワークリソースを共有する」と記載されていましたが、その部分が削除され、基本的なリソースの提供に焦点を当てるようになりました。この更新により、ユーザーはプランの内容をより明確に理解しやすくなり、役立つ情報が提供されることを目指しています。また、情報の正確性を保つために日付が更新されたことも重要なポイントです。全体として、この変更は文書の内容を改善し、利用者にとっての利便性を向上させることを目的としています。


