---
date: '2025-01-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a1ea100...MicrosoftDocs:985f323
summary: このコード差分では、3つのドキュメントに対するマイナーな更新が行われています。新しい機能は追加されず、破壊的な変更もありません。主な更新内容は、MySQLフレキシブルサーバーに関する文章の表記統一、地域サポートの情報の正確性向上、C#のチュートリアルの最新情報への更新と検索サジェスト機能の説明追加です。この一連の変更は、ドキュメントの整合性と正確性を高め、ユーザーが情報をより理解しやすくすることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a1ea100...MicrosoftDocs:985f323){target="_blank"}

# Highlights
このコード差分では、以下の3つのドキュメントに対するマイナーな更新が行われています。

## New features
特に新しい機能は追加されていません。

## Breaking changes
主要な機能や互換性に影響を与える破壊的な変更はありません。

## Other updates
- 「MySQLフレキシブルサーバーに関する文書」において表記の統一がなされました。
- 地域サポートのテーブルでは、特定の注釈を削除し、情報の正確性を向上させました。
- C#のチュートリアルでは、最新情報への更新とともに、検索サジェスト機能の説明が追加されました。

# Insights
この一連の変更は、ドキュメントの整合性と正確性を高め、ユーザーが情報をより理解しやすくすることを目的としています。

まず、MySQLフレキシブルサーバーの文書では、表記の一貫性を保つことにより、読者に混乱を与えない工夫が施されました。特に「flexible server」という用語を「Flexible Server」に統一することで、Azureサービスの正式名称への理解が深まります。

次に、地域サポートに関する修正は、特定の地域に関する誤解を排除し、正確な情報提供を図るためのものです。これにより、ユーザーは各地域で利用可能なサービスレベルを誤解することなく、適切な判断を下すことができます。

最後に、C#のチュートリアル更新では、文書の日付を最新の状況に反映しつつ、検索サジェスト機能についての詳細な説明が追加されました。この追加により、開発者はシステム利用時の検索機能に対する理解を深め、実際の実装に活かすことが可能となります。構成の簡潔化により、ドキュメントの可読性が高まり、効率的な学習を促進します。

これらの小さなが重要な更新が、全体としてユーザーフレンドリーなドキュメントに寄与しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-howto-index-mysql.md](#item-5d31c4) | minor update | MySQLフレキシブルサーバーに関する文書の修正 | modified | 3 | 3 | 6 | 
| [search-region-support.md](#item-25b0f1) | minor update | 地域サポートのテーブル修正 | modified | 1 | 1 | 2 | 
| [tutorial-csharp-search-query-integration.md](#item-8ad6b5) | minor update | C# チュートリアルの更新 | modified | 6 | 12 | 18 | 


# Modified Contents
## articles/search/search-howto-index-mysql.md{#item-5d31c4}

<details>
<summary>Diff</summary>
````diff
@@ -15,22 +15,22 @@ ms.custom:
 ms.date: 12/10/2024
 ---
 
-# Index data from Azure Database for MySQL flexible server
+# Index data from Azure Database for MySQL Flexible Server
 
 > [!IMPORTANT]
 > MySQL support is currently in public preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). You can use 2020-06-30-preview or later to index your content. We recommend the latest preview API. There is currently no portal support.
 
 In this article, learn how to configure an [**indexer**](search-indexer-overview.md) that imports content from Azure Database for MySQL and makes it searchable in Azure AI Search. Inputs to the indexer are your row, in a single table or view. Output is a search index with searchable content in individual fields.
 
-This article supplements [**Create an indexer**](search-howto-create-indexers.md) with information that's specific to indexing from Azure Database for MySQL flexible server. It uses the REST APIs to demonstrate a three-part workflow common to all indexers: create a data source, create an index, create an indexer. Data extraction occurs when you submit the Create Indexer request.
+This article supplements [**Create an indexer**](search-howto-create-indexers.md) with information that's specific to indexing from Azure Database for MySQL Flexible Server. It uses the REST APIs to demonstrate a three-part workflow common to all indexers: create a data source, create an index, create an indexer. Data extraction occurs when you submit the Create Indexer request.
 
 When configured to include a high water mark and soft deletion, the indexer takes all changes, uploads, and deletes for your MySQL database. It reflects these changes in your search index. Data extraction occurs when you submit the Create Indexer request.
 
 ## Prerequisites
 
 - [Register for the preview](https://aka.ms/azure-cognitive-search/indexer-preview) to provide scenario feedback. You can access the feature automatically after form submission.
 
-- [Azure Database for MySQL flexible server](/azure/mysql/flexible-server/overview) and sample data. Data must reside in a table or view. A primary key is required. If you're using a view, it must have a [high water mark column](#DataChangeDetectionPolicy). 
+- [Azure Database for MySQL Flexible Server](/azure/mysql/flexible-server/overview) and sample data. Data must reside in a table or view. A primary key is required. If you're using a view, it must have a [high water mark column](#DataChangeDetectionPolicy). 
 
 - Read permissions. A *full access* connection string includes a key that grants access to the content, but if you're using Azure roles, make sure the [search service managed identity](search-howto-managed-identities-data-sources.md) has **Reader** permissions on MySQL.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MySQLフレキシブルサーバーに関する文書の修正"
}
```

### Explanation
この変更は、「Azure Database for MySQL Flexible Server」という文言の表記を統一するために行われました。具体的には、タイトルや本文内での「flexible server」という表現を「Flexible Server」に修正しています。修正は主に文書の一貫性を保つためのものであり、全体の内容にどのように影響するかは少ないですが、ユーザーが正確かつ一貫した情報を得られることが重要です。 

この変更により、文書の可読性が向上し、特にAzure Database for MySQLに関連する詳細についての理解が容易になります。具体的な修正は3箇所の削除と3箇所の追加を含み、全体で6つの変更が行われました。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -112,7 +112,7 @@ AI service integration refers to internal connections to an Azure AI multi-servi
 |--|--|--|--|--|
 | Arizona | ✅ | ✅  | | |
 | Texas |  | ✅ |  | |
-| Virginia | ✅ | ✅  | ✅ | All Tiers |
+| Virginia | ✅ | ✅  | ✅ | |
 
 ## Azure operated by 21Vianet
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域サポートのテーブル修正"
}
```

### Explanation
この変更では、ドキュメント内の地域サポートに関するテーブルで「Virginia」の欄の表記が修正されました。具体的には、「Virginia」の列にあった「All Tiers」という注釈が削除され、空白となっています。この修正は情報の正確性を向上させるために行われたもので、ユーザーにとっては、提供されるサービスの階層に関する誤解を避ける効果があります。

変更自体は、1つの削除と1つの追加から成っており、合計で2カ所の変更があります。この修正により、ユーザーは各地域でのサービス提供について、より明確で一貫した情報を得ることができるようになります。

## articles/search/tutorial-csharp-search-query-integration.md{#item-8ad6b5}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: diberry
 ms.author: diberry
 ms.service: azure-ai-search
 ms.topic: tutorial
-ms.date: 01/17/2025
+ms.date: 01/21/2025
 ms.custom:
   - devx-track-csharp
   - devx-track-dotnet
@@ -34,9 +34,11 @@ The function app authenticates through the SDK to the cloud-based Azure AI Searc
 
 ## Azure Function: Search the catalog
 
-The [Search API](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/api/Search.cs) takes a search term and searches across the documents in the search index, returning a list of matches. 
+The [Search API](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/api/Search.cs) takes a search term and searches across the documents in the search index, returning a list of matches. Through the Suggest API, partial strings are sent to the search engine as the user types, suggesting search terms such as book titles and authors across the documents in the search index, and returning a small list of matches. 
 
-The Azure function pulls in the search configuration information, and fulfills the query.
+The Azure function pulls in the search configuration information, and fulfills the query. 
+
+The search suggester, `sg`, is defined in the [schema file](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/bulk-insert/BookSearchIndex.cs) used during bulk upload.
 
 :::code language="csharp" source="~/azure-search-static-web-app/api/Search.cs" :::
 
@@ -46,17 +48,9 @@ Call the Azure Function in the React client with the following code.
 
 :::code language="csharp" source="~/azure-search-static-web-app/client/src/pages/Search/Search.js" :::
 
-## Azure Function: Suggestions from the catalog
-
-The [Suggest API](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/api/Suggest.cs) takes a search term while a user is typing and suggests search terms such as book titles and authors across the documents in the search index, returning a small list of matches. 
-
-The search suggester, `sg`, is defined in the [schema file](https://github.com/Azure-Samples/azure-search-static-web-app/blob/main/bulk-insert/BookSearchIndex.cs) used during bulk upload.
-
-:::code language="csharp" source="~/azure-search-static-web-app/api/Suggest.cs"  :::
-
 ## Client: Suggestions from the catalog
 
-The Suggest function API is called in the React app at `\client\src\components\SearchBar\SearchBar.js` as part of component initialization:
+The Suggest function API is called in the React app at `\client\src\components\SearchBar\SearchBar.js` as part of the [Material UI's Autocomplete component](https://mui.com/material-ui/react-autocomplete/). This component uses the input text to search for authors and books that match the input text then displays those possible matches at selectable items in the drop-down list. 
 
 :::code language="csharp" source="~/azure-search-static-web-app/client/src/components/SearchBar/SearchBar.js" :::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# チュートリアルの更新"
}
```

### Explanation
この変更は、「C#での検索クエリ統合に関するチュートリアル」文書における情報の更新を含んでいます。主な変更点は、ドキュメントの日付の修正と、検索機能に関する記述の詳細化です。

具体的には、文書の日付が「01/17/2025」から「01/21/2025」に変更され、最新の情報を反映しています。また、検索APIの説明部分では、単なる検索結果の取得から、ユーザーが入力する際に提案される検索候補についての詳細が追加されました。この追加により、検索サジェスト機能の利用方法が明確になり、ユーザーはサジェスト機能がどのように機能するのかをより深く理解できるようになります。

さらに、不要なコードセクションが削除され、全体の構成が簡潔になりました。合計で6箇所の追加と12箇所の削除が行われており、文書の全体的な流れと可読性が向上しています。これにより、開発者はチュートリアルの内容を従う際に、よりスムーズに情報を理解しやすくなることが期待されます。


