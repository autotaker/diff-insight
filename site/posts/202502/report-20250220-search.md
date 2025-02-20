---
date: '2025-02-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f9aa01e...MicrosoftDocs:11dfa93
summary: この記事の更新は、Azure Table Storage に関するインデクシングの手法を明確化し、情報の正確性を向上させることを目的としたマイナーな修正を含んでいます。新しい機能は導入されていませんが、用語の改善により消費者が正しい情報を得やすくなっています。破壊的な変更はなく、日付の更新や権限管理に関する用語の修正が行われ、理解を助ける形になっています。特に、権限設定に関する用語が変更されたことで、利用者はより具体的に権限の範囲を理解できるようになりました。全体として、ユーザーエクスペリエンスの向上に寄与する重要な改訂です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f9aa01e...MicrosoftDocs:11dfa93){target="_blank"}

# Highlights
この記事の更新は、Azure Table Storage に関するインデクシングの手法を明確化し、正確性を向上させることを目的としたマイナーな修正を含んでいます。

## New features
特に新しい機能の導入はありませんが、用語の改善を通じて消費者が正しい情報を得やすくなっています。

## Breaking changes
破壊的な変更はありません。

## Other updates
- 日付の更新が行われ、古い情報が最新のものに刷新されました。
- Azure Storage の読み取り権限に関する用語が更新され、権限管理の理解を助ける形に修正されています。

# Insights
ドキュメントの更新においては、ユーザーが誤解する可能性のある要素を最小限にするための明確化が重要です。今回の修正は、主に用語の置き換えを通じて、既存のドキュメントが保持していた曖昧さを取り除いています。

特に、Azureの権限設定に関連する用語「Reader and Data Access」が「Storage Table Data Reader」に変更されたことで、権限の範囲がより具体的に理解できるようになりました。このような変更は、技術文書における不確実性を減らし、利用者が確かな情報のもとで操作を行えるようにするうえで不可欠です。

さらに、記事の日付の更新により、読者に常に最新の情報が提供されるよう意識されており、継続的なメンテナンスの重要性を感じます。小さな変更であっても、こうした累積が最終的にはユーザーエクスペリエンスを大きく向上させる要因となるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-howto-indexing-azure-tables.md](#item-7655b0) | minor update | Azure Table Storage のインデクシング方法に関する記事の更新 | modified | 2 | 2 | 4 | 
| [search-howto-managed-identities-storage.md](#item-8209c4) | minor update | マネージドアイデンティティを用いたストレージへのインデクサ接続設定の記事の更新 | modified | 4 | 4 | 8 | 


# Modified Contents
## articles/search/search-howto-indexing-azure-tables.md{#item-7655b0}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 11/20/2024
+ms.date: 02/18/2025
 ---
 
 # Index data from Azure Table Storage
@@ -26,7 +26,7 @@ This article supplements [**Create an indexer**](search-howto-create-indexers.md
 
 + Tables containing text. If you have binary data, consider [AI enrichment](cognitive-search-concept-intro.md) for image analysis.
 
-+ Read permissions on Azure Storage. A "full access" connection string includes a key that gives access to the content, but if you're using Azure roles, make sure the [search service managed identity](search-howto-managed-identities-data-sources.md) has **Reader and Data Access** permissions.
++ Read permissions on Azure Storage. A "full access" connection string includes a key that gives access to the content, but if you're using Azure roles, make sure the [search service managed identity](search-howto-managed-identities-data-sources.md) has **Storage Table Data Reader** permissions.
 
 To work through the examples in this article, you need the Azure portal or a [REST client](search-get-started-rest.md). If you're using Azure portal, make sure that access to all public networks is enabled. Other approaches for creating an Azure Table indexer include Azure SDKs.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Table Storage のインデクシング方法に関する記事の更新"
}
```

### Explanation
このコードの差分は、Azure Table Storage のインデクシングに関する記事に対するマイナーな更新を示しています。主な変更点は、日付の更新と一部の用語の修正です。具体的には、記事の日付が「2024年11月20日」から「2025年2月18日」に変更されました。また、Azure Storage の読み取り権限に関する説明において、「**Reader and Data Access**」という表現が「**Storage Table Data Reader**」に変更されました。これにより、より明確にAzureの権限管理が反映されるようになっています。全体として、これらの変更はドキュメントの正確性を向上させるためのものであり、内容はユーザーにとってより理解しやすくなっています。

## articles/search/search-howto-managed-identities-storage.md{#item-8209c4}

<details>
<summary>Diff</summary>
````diff
@@ -4,11 +4,11 @@ titleSuffix: Azure AI Search
 description: Learn how to set up an indexer connection to an Azure Storage account using a managed identity.
 author: gmndrg
 ms.author: gimondra
-manager: nitinme
+manager: vinodva
 
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 01/16/2025
+ms.date: 02/18/2025
 ms.custom:
   - subject-rbac-steps
   - ignite-2023
@@ -41,10 +41,10 @@ You can use a system-assigned managed identity or a user-assigned managed identi
    |------|-----------------|
    | Blob indexing using an indexer | Add **Storage Blob Data Reader** |
    | ADLS Gen2 indexing using an indexer | Add **Storage Blob Data Reader** |
-   | Table indexing using an indexer | Add **Reader and Data Access** |
+   | Table indexing using an indexer | Add **Storage Table Data Reader** |
    | File indexing using an indexer | Add **Reader and Data Access** |
    | Write to a [knowledge store](knowledge-store-concept-intro.md) | Add **Storage Blob Data Contributor** for object and file projections, and **Reader and Data Access** for table projections. |
-   | Write to an [enrichment cache](cognitive-search-incremental-indexing-conceptual.md) | Add **Storage Blob Data Contributor**  |
+   | Write to an [enrichment cache](cognitive-search-incremental-indexing-conceptual.md) | Add **Storage Blob Data Contributor** and **Storage Table Data Reader** |
    | Save [debug session state](cognitive-search-debug-session.md) | Add **Storage Blob Data Contributor**  |
 
 1. Select **Next**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージドアイデンティティを用いたストレージへのインデクサ接続設定の記事の更新"
}
```

### Explanation
このコードの差分は、マネージドアイデンティティを使用してAzureストレージアカウントへのインデクサ接続を設定する方法に関する記事に対するマイナーな更新を示しています。変更の主な内容には、著者や日付の修正、誤解を招く可能性のある用語の置き換えが含まれています。

具体的には、管理者が「nitinme」から「vinodva」に変更され、記事の日付が「2025年1月16日」から「2025年2月18日」に更新されました。また、Azureストレージの権限設定に関する表の内容も調整されました。「**Reader and Data Access**」という表現が「**Storage Table Data Reader**」に変更され、さらに「**Storage Table Data Reader**」がエンリッチメントキャッシュへの書き込みに関連する行にも追加されました。この更新により、ドキュメントがより正確で分かりやすくなり、ユーザーが必要な権限について理解しやすくなっています。


