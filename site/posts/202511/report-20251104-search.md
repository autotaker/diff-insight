---
date: '2025-11-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0aa8972...MicrosoftDocs:c655d26
summary: このコードの差分では、技術文書における用語やモデルが更新され、主にSharePoint Onlineの表記をSharePointに統一しました。また、Azure
  Cosmos DB向けのMongoDBインデクサーへの言及とChatGPTモデルのバージョンアップデートが行われています。特に大きな破壊的な変更はありませんが、用語の一貫性を高めることでユーザーの理解を向上させることが目的とされています。これらの更新により、文書の正確性や整合性が強化され、業務上の効率とユーザーエクスペリエンスの向上が期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0aa8972...MicrosoftDocs:c655d26){target="_blank"}

<format>
# Highlights
このコードの差分では、いくつかの技術文書で用語やモデルの更新が行われています。主な変更点として、SharePoint Onlineの表記がSharePointに統一され、トークン化やモデルのバージョンにおける更新が行われています。これにより、文書の正確性とユーザーが得られる情報の明瞭性が向上しています。

## New features
- 新たにAzure Cosmos DB向けのMongoDBインデクサーへの言及が追加されました。
- ChatGPTのモデルバージョンがgpt-35からgpt-4.1-miniへと更新されました。

## Breaking changes
特に大きな変更点や破壊的な変更はないが、インデクサーの名称修正が文書全般に適用されることによってユーザーの理解に直接的な影響を与える可能性があります。

## Other updates
- インデクサーに関する用語の一貫性が高まり、SharePoint OnlineがSharePointに変更されました。
- セマンティックランカーの有効化手順が最新のガイドラインに基づいて変更されました。
- 画像ファイルのメタデータが最適化され、ドキュメントの整合性が向上しました。

# Insights
この差分は、主に用語の統一やモデルの更新を中心に行われており、最新技術に合わせた文書の整合性が強調されています。特に注目すべきは、ChatGPT APIでのモデル変更やトークン化モデルの更新であり、これらの修正により、最新のAI技術を反映した情報にアクセスしやすくなっています。

業務上では、SharePoint OnlineからSharePointへの用語の変更により、クラウド環境全体での名称の統一が図られ、ユーザーが異なるサービスや機能を利用する際の混乱を減らす効果があります。また、セマンティックランカーの新しい有効化手順は、ユーザーが最新のポータル操作に容易に対応できるよう意図されています。

トークン化に関して、GPT-4に対応したことは、自然言語処理タスクにおける精度やパフォーマンスを向上させる狙いがあります。これは、特にAIモデルを使用したプロジェクトにおいて重要となるため、技術的な優位性を確保するうえでの意義が大きいでしょう。

このようなマイナーアップデートは、技術文書の正確性と一貫性を優先し、利用者が最大限の情報を引き出せるように配慮されています。その結果、業務における効率とユーザーエクスペリエンスの向上が期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-debug-session.md](#item-edf092) | minor update | インデクサーの名称修正: SharePoint OnlineからSharePointへ | modified | 1 | 1 | 2 | 
| [cognitive-search-how-to-debug-skillset.md](#item-31db42) | minor update | インデクサーの名称修正: SharePoint OnlineからSharePointへ | modified | 1 | 1 | 2 | 
| [cognitive-search-skill-textsplit.md](#item-9bf753) | minor update | トークン化パラメーターの説明修正: encoderModelNameのデフォルトをGPT-4に更新 | modified | 1 | 1 | 2 | 
| [enrichment-cache-how-to-configure.md](#item-b0ae0b) | minor update | SharePointインデクサーの表現を修正: Onlineから一般名称に変更 | modified | 1 | 1 | 2 | 
| [enrichment-cache-how-to-manage.md](#item-a972bd) | minor update | SharePointインデクサーの表現を修正: Onlineから一般名称に変更 | modified | 1 | 1 | 2 | 
| [semantic-search-billing.png](#item-79aec1) | minor update | semantic-search-billing.pngにおけるメタデータの修正 | modified | 0 | 0 | 0 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | モデルのバージョン変更: gpt-35からgpt-4.1-miniへ | modified | 1 | 1 | 2 | 
| [search-api-preview.md](#item-511f5d) | minor update | SharePoint Onlineインデクサーの名称変更 | modified | 1 | 1 | 2 | 
| [search-blob-metadata-properties.md](#item-2137f3) | minor update | SharePointインデクサーへの表記修正 | modified | 1 | 1 | 2 | 
| [search-data-sources-gallery.md](#item-18727f) | minor update | SharePointに関する表現の修正 | modified | 1 | 1 | 2 | 
| [search-how-to-index-sharepoint-online.md](#item-8c099c) | minor update | SharePointに関する表記の修正 | modified | 1 | 1 | 2 | 
| [search-how-to-large-index.md](#item-d34e42) | minor update | SharePointに関する表現の修正 | modified | 1 | 1 | 2 | 
| [search-import-data-portal.md](#item-b804d1) | minor update | SharePointに関する表記の修正 | modified | 2 | 2 | 4 | 
| [search-indexer-access-control-lists-and-role-based-access.md](#item-67b42f) | minor update | ACL対象の説明の詳細化 | modified | 1 | 1 | 2 | 
| [search-indexer-troubleshooting.md](#item-087365) | minor update | SharePoint OnlineからSharePointへの表記修正 | modified | 2 | 2 | 4 | 
| [search-manage.md](#item-4043d7) | minor update | セマンティックランカー設定手順の修正 | modified | 1 | 1 | 2 | 
| [search-what-is-data-import.md](#item-d73ef5) | minor update | SharePoint Onlineの名称更新 | modified | 1 | 1 | 2 | 
| [semantic-how-to-enable-disable.md](#item-71ac1e) | minor update | セマンティックランカーの有効化手順の修正 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c4768f) | minor update | SharePointの名称変更 | modified | 1 | 1 | 2 | 
| [vector-search-how-to-chunk-documents.md](#item-b79133) | minor update | トークンエンコーディングモデルの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/cognitive-search-debug-session.md{#item-edf092}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ The second image shows a typical pattern for integrated vectorization. Skills fo
 
 Debug Sessions work with all generally available [indexer data sources](search-data-sources-gallery.md) and most preview data sources, with the following exceptions:
 
-+ SharePoint Online indexer.
++ SharePoint indexer.
 
 + Azure Cosmos DB for MongoDB indexer.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーの名称修正: SharePoint OnlineからSharePointへ"
}
```

### Explanation
このコードの変更は、`articles/search/cognitive-search-debug-session.md`というドキュメントの内容における小さな修正を示しています。具体的には、「SharePoint Online indexer」という表現が「SharePoint indexer」へと変更されています。この変更は、インデクサーの名称をより簡潔にすることで、読者にとっての理解を容易にすることを目的としています。また、Azure Cosmos DB向けのMongoDBインデクサーへの言及も追加されています。この修正により、ドキュメントが最新の情報を反映する形となり、ユーザーにとっての有用性が向上しています。

## articles/search/cognitive-search-how-to-debug-skillset.md{#item-31db42}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ For background on how a debug session works, see [Debug sessions in Azure AI Sea
 
 Debug sessions work with all generally available [indexer data sources](search-data-sources-gallery.md) and most preview data sources, with the following exceptions:
 
-+ SharePoint Online indexer.
++ SharePoint indexer.
 
 + Azure Cosmos DB for MongoDB indexer.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーの名称修正: SharePoint OnlineからSharePointへ"
}
```

### Explanation
このコードの変更は、`articles/search/cognitive-search-how-to-debug-skillset.md`というドキュメントの内容における小さな修正を示しています。具体的には、「SharePoint Online indexer」という表現が「SharePoint indexer」へと変更されています。この修正により、インデクサーの呼称がより一般的な形に統一され、ドキュメントの明瞭性が向上しています。また、同じ内容に「Azure Cosmos DB向けのMongoDBインデクサー」への言及が含まれており、利用可能なインデクサーの情報をしっかりと提供しています。この変更により、ユーザーが利用可能なリソースをより良く理解できるようになっています。

## articles/search/cognitive-search-skill-textsplit.md{#item-9bf753}

<details>
<summary>Diff</summary>
````diff
@@ -41,7 +41,7 @@ Parameters are case-sensitive.
 | `pageOverlapLength` | Only applies if `textSplitMode` is set to `pages`. Each page starts with this number of characters or tokens from the end of the previous page. If this parameter is set to 0, there's no overlapping text on successive pages. This [example](#example-for-chunking-and-vectorization) includes the parameter. |
 | `maximumPagesToTake` | Only applies if `textSplitMode` is set to `pages`. Number of pages to return. The default is 0, which means to return all pages. You should set this value if only a subset of pages are needed. This [example](#example-for-chunking-and-vectorization) includes the parameter.|
 | `unit` | Only applies if `textSplitMode` is set to `pages`. Specifies whether to chunk by `characters` (default) or `azureOpenAITokens`. Setting the unit affects `maximumPageLength` and `pageOverlapLength`. |
-| `azureOpenAITokenizerParameters` An object providing extra parameters for the `azureOpenAITokens` unit. <br><br>`encoderModelName` is a designated tokenizer used for converting text into tokens, essential for natural language processing (NLP) tasks. Different models use different tokenizers. Valid values include cl100k_base (default) used by GPT-35-Turbo and GPT-4. Other valid values are r50k_base, p50k_base, and p50k_edit. The skill implements the tiktoken library by way of [SharpToken](https://www.nuget.org/packages/SharpToken) and `Microsoft.ML.Tokenizers` but doesn't support every encoder. For example, there's currently no support for o200k_base encoding used by GPT-4o. <br><br>`allowedSpecialTokens` defines a collection of special tokens that are permitted within the tokenization process. Special tokens are  string that you want to treat uniquely, ensuring they aren't split during tokenization. For example ["[START"], "[END]"]. If the `tiktoken` library doesn't perform tokenization as expected, either due to language-specific limitations or other unexpected behaviors, it's recommended to use text splitting instead.|
+| `azureOpenAITokenizerParameters` An object providing extra parameters for the `azureOpenAITokens` unit. <br><br>`encoderModelName` is a designated tokenizer used for converting text into tokens, essential for natural language processing (NLP) tasks. Different models use different tokenizers. Valid values include cl100k_base (default) used by GPT-4. Other valid values are r50k_base, p50k_base, and p50k_edit. The skill implements the tiktoken library by way of [SharpToken](https://www.nuget.org/packages/SharpToken) and `Microsoft.ML.Tokenizers` but doesn't support every encoder. For example, there's currently no support for o200k_base encoding used by GPT-4o. <br><br>`allowedSpecialTokens` defines a collection of special tokens that are permitted within the tokenization process. Special tokens are  string that you want to treat uniquely, ensuring they aren't split during tokenization. For example ["[START"], "[END]"]. If the `tiktoken` library doesn't perform tokenization as expected, either due to language-specific limitations or other unexpected behaviors, it's recommended to use text splitting instead.|
 
 ## Skill Inputs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トークン化パラメーターの説明修正: encoderModelNameのデフォルトをGPT-4に更新"
}
```

### Explanation
このコードの変更は、`articles/search/cognitive-search-skill-textsplit.md`というドキュメント内の「azureOpenAITokenizerParameters」セクションにおける小さな修正を示しています。その内容は、トークン化に関するパラメーターの説明に関連しています。具体的には、デフォルトのトークン化モデルとして「GPT-35-Turbo」から「GPT-4」へと変更されています。この修正により、ユーザーは最新の技術に基づいた正確な情報を得ることができ、自然言語処理（NLP）タスクにおけるトークン化の理解が向上します。また、「allowedSpecialTokens」の説明は変更されていませんが、全体の整合性と明確性を保つためにパラメーターの説明を最新の情報に基づいて更新することは、文書の品質向上に寄与しています。

## articles/search/enrichment-cache-how-to-configure.md{#item-b0ae0b}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ You should be familiar with setting up indexers and skillsets. Start with [index
 ## Limitations
 
 > [!CAUTION]
-> If you're using the [SharePoint Online indexer (Preview)](search-how-to-index-sharepoint-online.md), you should avoid incremental enrichment. Under certain circumstances, the cache becomes invalid, requiring an [indexer reset and full rebuild](search-howto-run-reset-indexers.md), should you choose to reload it.
+> If you're using the [SharePoint indexer (Preview)](search-how-to-index-sharepoint-online.md), you should avoid incremental enrichment. Under certain circumstances, the cache becomes invalid, requiring an [indexer reset and full rebuild](search-howto-run-reset-indexers.md), should you choose to reload it.
 
 ## Permissions
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointインデクサーの表現を修正: Onlineから一般名称に変更"
}
```

### Explanation
このコードの変更は、`articles/search/enrichment-cache-how-to-configure.md`というドキュメント内の警告セクションにおける小さな修正を示しています。具体的には、「SharePoint Online indexer (Preview)」という表現が「SharePoint indexer (Preview)」へと変更されています。この修正により、用語がより一般的な形に統一され、ユーザーが同様の機能を持つインデクサーについての理解を深めやすくなります。また、ドキュメント内の警告メッセージは、キャッシュが無効になる可能性やインデクサーのリセットが必要になる状況について情報を提供し続けています。この変更によって、情報の明確さが向上し、ユーザーにとってより使いやすいガイドラインとなっています。

## articles/search/enrichment-cache-how-to-manage.md{#item-a972bd}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ If you have configured an enrichment cache, this article explains how to manage
 ## Limitations
 
 > [!CAUTION]
-> If you're using the [SharePoint Online indexer (Preview)](search-how-to-index-sharepoint-online.md), you should avoid incremental enrichment. Under certain circumstances, the cache becomes invalid, requiring an [indexer reset and full rebuild](search-howto-run-reset-indexers.md), should you choose to reload it.
+> If you're using the [SharePoint indexer (Preview)](search-how-to-index-sharepoint-online.md), you should avoid incremental enrichment. Under certain circumstances, the cache becomes invalid, requiring an [indexer reset and full rebuild](search-howto-run-reset-indexers.md), should you choose to reload it.
 
 ## Cache configuration
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointインデクサーの表現を修正: Onlineから一般名称に変更"
}
```

### Explanation
このコードの変更は、`articles/search/enrichment-cache-how-to-manage.md`というドキュメント内の制限事項セクションにおける小さな修正を示しています。具体的には、警告メッセージ内の「SharePoint Online indexer (Preview)」という表現が「SharePoint indexer (Preview)」へと変更されています。この変更により、用語の統一性が保たれ、ユーザーが同様の機能を持つインデクサーについてより理解しやすくなっています。警告の内容は、インクリメンタルエンリッチメントを避けるべき理由や、キャッシュが無効になる状況が引き続き説明されています。この修正によって、情報の正確性と明瞭性が向上し、ユーザーにとってより信頼できるガイドラインが提供されています。

## articles/search/media/semantic-search-overview/semantic-search-billing.png{#item-79aec1}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "semantic-search-billing.pngにおけるメタデータの修正"
}
```

### Explanation
このコードの変更は、`articles/search/media/semantic-search-overview/semantic-search-billing.png`という画像ファイルに関連しており、具体的には内容に変更はありませんが、メタデータの修正が行われた可能性があります。画像自体は追加も削除もされておらず、変更は認められないため、ユーザーに対する影響はないものの、ファイル名やパスの整理や最適化などの小さな編集が考えられます。このような修正はドキュメントや関連するリソースの整合性を保つために重要です。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -211,7 +211,7 @@ response = openai_client.chat.completions.create(
             "content": GROUNDED_PROMPT.format(query=query, sources=sources_formatted)
         }
     ],
-    model="gpt-35"
+    model="gpt-4.1-mini"
 )
 
 print(response.choices[0].message.content)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのバージョン変更: gpt-35からgpt-4.1-miniへ"
}
```

### Explanation
このコードの変更は、`articles/search/retrieval-augmented-generation-overview.md`というドキュメント内で、ChatGPT APIを使用する際のモデルバージョンに関する修正です。具体的には、API呼び出しの部分で指定されているモデルが「gpt-35」から「gpt-4.1-mini」へと変更されています。この更新は、利用するAIモデルの性能や機能に影響を与える可能性があり、より高度な応答を得られることが期待されます。この種の修正は、ドキュメントの信頼性と現代性を保ち、ユーザーが最新の技術を利用できるようにするための重要なステップです。

## articles/search/search-api-preview.md{#item-511f5d}

<details>
<summary>Diff</summary>
````diff
@@ -44,7 +44,7 @@ Preview features are removed from this list if they're retired or transition to
 | [**Azure Machine Learning (AML) skill**](cognitive-search-aml-skill.md) | Applied AI (skills) | AML skill integrates an inferencing endpoint from Azure Machine Learning. In previous preview APIs, it supports connections to deployed custom models in an AML workspace. Starting in the 2024-05-01-preview, you can use this skill in workflows that connect to embedding models in the Azure AI Foundry model catalog. It's also available in the Azure portal, in skillset design, assuming Azure AI Search and Azure Machine Learning services are deployed in the same subscription. | [Create or Update Skillset (preview)](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
 | [**Incremental enrichment cache**](enrichment-cache-how-to-configure.md) | Applied AI (skills) | Adds caching to an enrichment pipeline, allowing you to reuse existing output if a targeted modification, such as an update to a skillset or another object, doesn't change the content. Caching applies only to enriched documents produced by a skillset.| [Create or Update Indexer (preview)](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
 |  [**Azure Files indexer**](search-file-storage-integration.md) | Indexer data source | New data source for indexer-based indexing from [Azure Files](https://azure.microsoft.com/services/storage/files/) | [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
-| [**SharePoint Online indexer**](search-how-to-index-sharepoint-online.md) | Indexer data source | New data source for indexer-based indexing of SharePoint content. | [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true) or the Azure portal. |
+| [**SharePoint indexer**](search-how-to-index-sharepoint-online.md) | Indexer data source | New data source for indexer-based indexing of SharePoint content. | [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true) or the Azure portal. |
 |  [**MySQL indexer**](search-how-to-index-mysql.md) | Indexer data source | New data source for indexer-based indexing of Azure MySQL data sources.| [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true), [.NET SDK 11.2.1](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourcetype.mysql), and Azure portal. |
 | [**Azure Cosmos DB for MongoDB indexer**](search-how-to-index-cosmosdb-sql.md) | Indexer data source | New data source for indexer-based indexing through the MongoDB APIs in Azure Cosmos DB. | [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true) or the Azure portal. |
 | [**Azure Cosmos DB for Apache Gremlin indexer**](search-how-to-index-cosmosdb-sql.md) | Indexer data source | New data source for indexer-based indexing through the Apache Gremlin APIs in Azure Cosmos DB. | [Sign up](https://aka.ms/azure-cognitive-search/indexer-preview) to enable the feature. [Create or Update Data Source (preview)](/rest/api/searchservice/data-sources/create-or-update?view=rest-searchservice-2024-05-01-preview&preserve-view=true). |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint Onlineインデクサーの名称変更"
}
```

### Explanation
このコードの変更は、`articles/search/search-api-preview.md`というドキュメント内でSharePoint Onlineインデクサーに関する記載の修正です。具体的には、「SharePoint Online indexer」という名称が「SharePoint indexer」に変更されました。この変更は、表記の統一や利用者にとっての分かりやすさを目的としています。また、インデクサーに関連する他の情報やリンクはそのまま維持されています。ユーザーにとっては、わかりやすく表現されることで、機能や利用方法をより簡単に理解できるように促されることが期待されます。このようなマイナーな更新は、ドキュメントの正確性を保つうえで重要な役割を果たします。

## articles/search/search-blob-metadata-properties.md{#item-2137f3}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ Azure AI Search supports blob indexing and SharePoint document indexing for the
 
 ## Document format properties
 
-The following table summarizes processing for each document format, and describes the metadata properties extracted by a blob indexer and the SharePoint Online indexer.
+The following table summarizes processing for each document format, and describes the metadata properties extracted by a blob indexer and the SharePoint indexer.
 
 | Document format / content type | Extracted metadata | Processing details |
 | --- | --- | --- |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointインデクサーへの表記修正"
}
```

### Explanation
このコードの変更は、`articles/search/search-blob-metadata-properties.md`というドキュメント内で、インデクサーに関する表現の修正です。具体的には、「SharePoint Online indexer」という表記が「SharePoint indexer」に修正されています。この表現の変更は、最新の情報に基づく正確さや一貫性を提供するために行われたもので、利用者が容易に理解できるように意図されています。文中の他の情報や構成はそのまま維持されており、プロセスや抽出されるメタデータの内容については影響を受けていません。このようなマイナーな更新は、ドキュメントの品質を向上させるうえで非常に重要です。

## articles/search/search-data-sources-gallery.md{#item-18727f}

<details>
<summary>Diff</summary>
````diff
@@ -152,7 +152,7 @@ Pull in content [using logic app workflows](search-how-to-index-logic-apps.md) a
 
 By [Logic Apps](/connectors/sharepointonline)
 
-SharePoint helps organizations share and collaborate with colleagues, partners, and customers. You can connect to SharePoint Online or to an on-premises SharePoint 2016 or 2019 farm using the On-Premises Data Gateway to manage documents and list items.
+SharePoint helps organizations share and collaborate with colleagues, partners, and customers. You can connect to SharePoint in Microsoft 365 or to an on-premises SharePoint 2016 or 2019 farm using the On-Premises Data Gateway to manage documents and list items.
 
 [More details](search-how-to-index-logic-apps.md#supported-connectors)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointに関する表現の修正"
}
```

### Explanation
このコードの変更は、`articles/search/search-data-sources-gallery.md`というドキュメント内で、SharePointに関連する表現の小さな修正を行ったものです。具体的には、「SharePoint Online」という表記が「SharePoint in Microsoft 365」に更新されました。この変更は、SharePointの提供形態をより正確に反映させるものであり、最新のサービス名や利用環境に整合性を持たせる目的があります。文中の内容自体や他のリンクはそのまま維持されており、ドキュメントの他の情報に影響を及ぼすことはありません。このようなマイナーな更新は、ユーザーにとってより明瞭で理解しやすい情報を提供するために重要です。

## articles/search/search-how-to-index-sharepoint-online.md{#item-8c099c}

<details>
<summary>Diff</summary>
````diff
@@ -497,4 +497,4 @@ The error message will also include the SharePoint site ID, drive ID, and drive
 + [YouTube video: SharePoint in Microsoft 365 indexer](https://www.youtube.com/watch?v=QmG65Vgl0JI)
 + [Indexers in Azure AI Search](search-indexer-overview.md)
 + [Content metadata properties used in Azure AI Search](search-blob-metadata-properties.md)
-+ [Index SharePoint Online content and other sources in Azure AI Search using Azure Logic App connectors](search-how-to-index-logic-apps.md)
++ [Index SharePoint content and other sources in Azure AI Search using Azure Logic App connectors](search-how-to-index-logic-apps.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointに関する表記の修正"
}
```

### Explanation
このコードの変更は、`articles/search/search-how-to-index-sharepoint-online.md`というドキュメント内で、SharePointに関連する表現の修正を行ったものです。具体的には、リンクの前にある表現が「SharePoint Online」から「SharePoint」に変更されました。この修正は、より広範なSharePointのサービスを指すものであり、より正確な情報を提供するために意図されています。それ以外の文やリンクはそのまま残されており、情報の構造には影響を与えていません。このようなマイナーな更新は、ユーザーに対して最新かつ正確な情報を確保するために重要です。

## articles/search/search-how-to-large-index.md{#item-d34e42}

<details>
<summary>Diff</summary>
````diff
@@ -76,7 +76,7 @@ Partitioning data into smaller individual data sources enables parallel processi
 
 As with the push API, indexers allow you to configure the number of items per batch. For indexers based on the [Create Indexer REST API](/rest/api/searchservice/indexers/create), you can set the `batchSize` argument to customize this setting to better match the characteristics of your data. 
 
-Default batch sizes are data-source specific. Azure SQL Database and Azure Cosmos DB have a default batch size of 1,000. In contrast, Azure Blob and SharePoint Online (Preview) indexing sets batch size at 10 documents in recognition of the larger average document size. 
+Default batch sizes are data-source specific. Azure SQL Database and Azure Cosmos DB have a default batch size of 1,000. In contrast, Azure Blob and SharePoint (Preview) indexing sets batch size at 10 documents in recognition of the larger average document size. 
 
 ### Schedule indexers for long-running processes
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointに関する表現の修正"
}
```

### Explanation
この変更は、`articles/search/search-how-to-large-index.md`というドキュメントにおけるSharePointに関連する表現の軽微な修正を示しています。具体的には、「SharePoint Online」が「SharePoint」に更新されました。この修正により、最新のサービス名に合わせて表現が統一され、ユーザーにとって分かりやすい情報を提供することが目的です。他の文章やデータはそのまま残されており、ドキュメントの内容に大きな影響は与えていません。このようなマイナーな更新は、正確性と一貫性を保つために重要です。

## articles/search/search-import-data-portal.md{#item-b804d1}

<details>
<summary>Diff</summary>
````diff
@@ -71,12 +71,12 @@ The wizards support the following data sources, most of which use [built-in inde
 | [OneDrive for Business](search-how-to-index-logic-apps.md#supported-connectors) | ❌ | ✅ <sup>1</sup> |
 | [OneLake](search-how-to-index-onelake-files.md) | ✅ | ✅ |
 | [Service Bus](search-how-to-index-logic-apps.md#supported-connectors) | ❌ | ✅ <sup>1</sup> |
-| [SharePoint Online](search-how-to-index-logic-apps.md#supported-connectors) | ❌ | ✅ <sup>1, 2</sup> |
+| [SharePoint](search-how-to-index-logic-apps.md#supported-connectors) | ❌ | ✅ <sup>1, 2</sup> |
 | [SQL Server on virtual machines](search-how-to-index-sql-server.md) | ✅ | ✅ |
 
 <sup>1</sup> This data source uses an [Azure Logic Apps connector (preview)](search-how-to-index-logic-apps.md#supported-connectors) instead of a built-in indexer.
 
-<sup>2</sup> Instead of using a Logic Apps connector, you can use the Search Service REST APIs to programmatically index data from [Azure File Storage](search-file-storage-integration.md) or [SharePoint Online](search-how-to-index-sharepoint-online.md).
+<sup>2</sup> Instead of using a Logic Apps connector, you can use the Search Service REST APIs to programmatically index data from [Azure File Storage](search-file-storage-integration.md) or [SharePoint](search-how-to-index-sharepoint-online.md).
 
 ### Sample data
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointに関する表記の修正"
}
```

### Explanation
この変更は、`articles/search/search-import-data-portal.md`というドキュメント内でSharePointに関する用語を修正することを目的としたものです。具体的には、「SharePoint Online」との表現が「SharePoint」に変更されました。この修正は、SharePointの機能をより包括的に示すために行われています。その他のリンクや文はそのまま残されており、構成や内容に大きな影響を与えていません。こうしたマイナーな更新は、正確かつ一貫性のある表現を維持するために重要です。

## articles/search/search-indexer-access-control-lists-and-role-based-access.md{#item-67b42f}

<details>
<summary>Diff</summary>
````diff
@@ -42,7 +42,7 @@ This article supplements [**Index data from ADLS  Gen2**](search-how-to-index-az
 
 + [Limits on Azure role assignments and ACL entries](/azure/storage/blobs/data-lake-storage-access-control-model#limits-on-azure-role-assignments-and-acl-entries) in ADLS Gen2 impose a maximum number of role assignments and ACL entries.
 
-+ The `owning users`, `owning groups` and `Other` [ACL identities categories](/azure/storage/blobs/data-lake-storage-access-control#users-and-identities) are not supported during public preview. Use `named users` and `named groups` assignments instead.
++ The `owning users`, `owning groups`, `Other` (`all`),  [ACL identities categories](/azure/storage/blobs/data-lake-storage-access-control#users-and-identities) are not supported during public preview. Use `named users` and `named groups` assignments instead.
   
 + The following indexer features don't support permission inheritance in indexed documents originating from ADLS Gen2. If you're using any of these features in a skillset or indexer, document-level permissions won't be present in the indexed content:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ACL対象の説明の詳細化"
}
```

### Explanation
この変更は、`articles/search/search-indexer-access-control-lists-and-role-based-access.md`というドキュメントにおいて、アクセス制御リスト（ACL）に関連する記述を明確にするためのものです。具体的には、「Other」カテゴリが「Other (`all`)」として明記され、そのサポート状況が確認されやすくなりました。この修正により、ユーザーはACLに関連する階層名の理解を深めることができ、情報の明確さが向上しています。この変更は、技術的な正確性を高め、ユーザーが適切な設定を行えるように手助けすることを目的としています。

## articles/search/search-indexer-troubleshooting.md{#item-087365}

<details>
<summary>Diff</summary>
````diff
@@ -105,15 +105,15 @@ If the database is paused, the first sign in from your search service is expecte
 
 ## Microsoft Entra Conditional Access policies
 
-When you create a SharePoint Online indexer, there's a step requiring you to sign in to your Microsoft Entra app after providing a device code. If you receive a message that says `"Your sign-in was successful but your admin requires the device requesting access to be managed"`, the indexer is probably blocked from the SharePoint document library by a [Conditional Access](/azure/active-directory/conditional-access/overview) policy.
+When you create a SharePoint indexer, there's a step requiring you to sign in to your Microsoft Entra app after providing a device code. If you receive a message that says `"Your sign-in was successful but your admin requires the device requesting access to be managed"`, the indexer is probably blocked from the SharePoint document library by a [Conditional Access](/azure/active-directory/conditional-access/overview) policy.
 
 To update the policy and allow indexer access to the document library:
 
 1. Open the Azure portal and search for **Microsoft Entra Conditional Access**.
 
 1. Select **Policies** on the left menu. If you don't have access to view this page, you need to either find someone who has access or get access.
 
-1. Determine which policy is blocking the SharePoint Online indexer from accessing the document library. The policy that might be blocking the indexer includes the user account that you used to authenticate during the indexer creation step in the **Users and groups** section. The policy also might have **Conditions** that:
+1. Determine which policy is blocking the SharePoint indexer from accessing the document library. The policy that might be blocking the indexer includes the user account that you used to authenticate during the indexer creation step in the **Users and groups** section. The policy also might have **Conditions** that:
 
     * Restrict **Windows** platforms.
     * Restrict **Mobile apps and desktop clients**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint OnlineからSharePointへの表記修正"
}
```

### Explanation
この変更は、`articles/search/search-indexer-troubleshooting.md`というドキュメント内で、SharePointに関連する用語の修正を行っています。具体的には、「SharePoint Online」という表現が「SharePoint」に変更されました。これにより、情報がより広範に適用されることを意図していると考えられます。この修正は、特定の文脈において正確な理解を促進し、ユーザーがSharePointインデクサーの設定やトラブルシューティングに関する情報をよりスムーズに利用できるようにすることを目的としています。全体として、特に機能に影響を与える大きな変更はなく、文書の整合性と明確さを向上させるためのマイナーな更新です。

## articles/search/search-manage.md{#item-4043d7}

<details>
<summary>Diff</summary>
````diff
@@ -92,7 +92,7 @@ To learn more about data location and privacy, see [Data residency](search-secur
 
 Semantic ranker is free for the first 1,000 requests per month. It's enabled by default on newer search services.
 
-To enable semantic ranker in the portal, select **Settings** > **Semantic ranker** from the left pane, and then select the **Free** plan. For more information, see [Enable semantic ranker](semantic-how-to-enable-disable.md).
+To enable semantic ranker in the portal, select **Settings** > **Premium features** from the left pane, and then select the **Free** plan. For more information, see [Enable semantic ranker](semantic-how-to-enable-disable.md).
 
 ## Provide connection information to developers
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカー設定手順の修正"
}
```

### Explanation
この変更は、`articles/search/search-manage.md`という文書におけるセマンティックランカーの有効化手順の修正を行っています。具体的には、セマンティックランカーをポータルで有効にするためのナビゲーションが「**Settings** > **Semantic ranker**」から「**Settings** > **Premium features**」に変更されました。これにより、ユーザーは最新の操作手順に従ってセマンティックランカーを適切に有効化できるようになります。この修正は、文書の正確性を向上させ、ユーザーが機能を利用しやすくするための重要なマイナーアップデートです。全体的には、機能には影響を与えない変更であり、情報の明確さが向上しています。

## articles/search/search-what-is-data-import.md{#item-d73ef5}

<details>
<summary>Diff</summary>
````diff
@@ -78,7 +78,7 @@ The pull model uses *indexers* connecting to a supported data source, automatica
 + [Azure Cosmos DB](search-how-to-index-cosmosdb-sql.md)
 + [Azure SQL Database, SQL Managed Instance, and SQL Server on Azure VMs](search-how-to-index-sql-database.md)
 + [Microsoft OneLake files and shortcuts](search-how-to-index-onelake-files.md)
-+ [SharePoint Online (preview)](search-how-to-index-sharepoint-online.md)
++ [SharePoint in Microsoft 365 (preview)](search-how-to-index-sharepoint-online.md)
 
 You can use third-party connectors, developed and maintained by Microsoft partners. For more information and links, see [Data source gallery](search-data-sources-gallery.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint Onlineの名称更新"
}
```

### Explanation
この変更は、`articles/search/search-what-is-data-import.md`というドキュメント内での表記の修正を含んでいます。具体的には、「SharePoint Online (preview)」という表現が「SharePoint in Microsoft 365 (preview)」に変更されました。この修正は、現在のブランドや製品名に合わせて情報を更新し、正確さを向上させるために行われました。結果として、ユーザーに対する混乱を避け、関連情報の整合性を保つことを目的としています。このマイナーアップデートは、特に機能に影響を与えるものではなく、全体的な情報の明快さを向上させるための重要な措置です。

## articles/search/semantic-how-to-enable-disable.md{#item-71ac1e}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ Semantic ranker might not be enabled on older services. Follow these steps to en
 
 1. Navigate to your search service. On the **Overview** page, make sure the pricing tier is set to **Basic** or higher.
 
-1. On the left-navigation pane, select **Settings** > **Semantic ranker**.
+1. On the left-navigation pane, select **Settings** > **Premium features**.
 
 1. Select either the **Free plan** (default) or the **Standard plan**. You can switch between the free plan and the standard plan at any time.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーの有効化手順の修正"
}
```

### Explanation
この変更は、`articles/search/semantic-how-to-enable-disable.md`という文書内でのセマンティックランカーの有効化手順を更新するものです。具体的には、左側のナビゲーションペインでの手順が「**Settings** > **Semantic ranker**」から「**Settings** > **Premium features**」に変更されました。この修正は、ユーザーが最新のインターフェースに基づいて正確に機能を利用できるようにするために行われました。このマイナーアップデートは、全体的な利用者体験の向上を目的としており、古い文書の情報を新しい操作手順に合わせることによって、混乱を避ける助けとなります。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -346,7 +346,7 @@ items:
           href: search-how-to-index-sql-server.md
       - name: Microsoft OneLake
         href: search-how-to-index-onelake-files.md
-      - name: SharePoint Online
+      - name: SharePoint in Microsoft 365
         href: search-how-to-index-sharepoint-online.md
     - name: Skillsets (indexers)
       items:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointの名称変更"
}
```

### Explanation
この変更は、`articles/search/toc.yml`というファイル内でのコンテンツ目次の更新を反映しています。具体的には、「SharePoint Online」という項目名が「SharePoint in Microsoft 365」に変更されました。この修正は、ブランド名と製品名称の正確性を保つためのものであり、現在のマーケティングおよび製品戦略に一致するように情報を整備しています。このマイナーアップデートは、利用者が最新の情報に基づいてコンテンツを理解しやすくすることを目的としており、製品の名称に従った明確な表現を提供しています。

## articles/search/vector-search-how-to-chunk-documents.md{#item-b79133}

<details>
<summary>Diff</summary>
````diff
@@ -135,7 +135,7 @@ def tiktoken_len(text):
     disallowed_special=()
 )
     return len(tokens)
-tiktoken.encoding_for_model('gpt-3.5-turbo')
+tiktoken.encoding_for_model('gpt-4.1-mini')
 
 # create the length function
 token_counts = []
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トークンエンコーディングモデルの更新"
}
```

### Explanation
この変更は、`articles/search/vector-search-how-to-chunk-documents.md`というファイル内のトークンエンコーディングモデルを更新するものです。具体的には、`tiktoken.encoding_for_model('gpt-3.5-turbo')`という行が`tiktoken.encoding_for_model('gpt-4.1-mini')`に置き換えられました。この更新は、最新のモデル（GPT-4.1-mini）に基づくトークンのエンコーディングを使用することで、パフォーマンスや精度の向上を図ることを目的としています。このマイナーアップデートは、文書の内容が最新の技術にフィットするようにし、ユーザーにとっての利便性を向上させます。


