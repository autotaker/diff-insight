---
date: '2025-08-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c84ae83...MicrosoftDocs:88b6cf1
summary: このコードの変更は、Azureのドキュメンテーションにおける情報の修正を含むマイナーアップデートに焦点を当てています。主に、記事の更新日付を「2025年5月29日」から「2025年8月4日」に変更し、ユーザー指定のマネージドアイデンティティに関する情報を明確化しました。新しい機能の追加や破壊的な変更はなく、今回の修正はドキュメンテーションの信頼性を高め、ユーザーの理解を助けることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c84ae83...MicrosoftDocs:88b6cf1){target="_blank"}

# ハイライト

このコードの変更は、Azureのドキュメンテーションにおける情報の修正を含むマイナーアップデートに焦点を当てています。具体的には記事の更新日付を変更し、ユーザー指定のマネージドアイデンティティに関する情報を明確化しました。

## 新機能

- 特に新しい機能の追加は行われていません。

## 破壊的変更

- 破壊的な変更はありません。

## その他の更新

- 記事の更新日が「2025年5月29日」から「2025年8月4日」に変更されました。
- ユーザー指定のマネージドアイデンティティに関する記述が簡潔になり、情報の明確化が図られました。

# インサイト

今回の変更は、ドキュメンテーションにおける情報の明確化と最新情報への更新を目的としています。特に、「現在プレビュー中である」という文言を削除しつつ、ユーザー指定のマネージドアイデンティティの記載を簡潔にしつつも、その不具合についての警告を維持しています。これにより、ユーザーは情報をより速やかに理解しやすくなり、より適切な判断ができるようになっています。

更新日付が変更されたことにより、情報提供者が文書の内容が最新であることを示したい意図が反映されています。このような日付の更新は、特に情報が重要な技術ドキュメンテーションにおいては、コンテンツが最新である信頼性を高めるために重要です。

このような微調整は読者のユーザー体験に重要な影響を与え、技術理解を助長します。マネージドアイデンティティに関する警告は、潜在的な問題を事前に知らせることで、より安全な利用を促進します。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-indexer-howto-access-trusted-service-exception.md](#item-e19826) | minor update | 日付の更新と情報の明確化 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/search-indexer-howto-access-trusted-service-exception.md{#item-e19826}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: arv100kri
 ms.author: arjagann
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/29/2025
+ms.date: 08/04/2025
 ms.custom:
   - ignite-2023
   - sfi-image-nochange
@@ -38,7 +38,7 @@ In Azure AI Search, indexers that access Azure blobs can use the [trusted servic
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
 
-1. On the **Identity** page, make sure that a [system assigned identity is enabled](search-howto-managed-identities-data-sources.md). Remember that user-assigned managed identities, currently in preview, won't work for a trusted service connection.
+1. On the **Identity** page, make sure that a [system assigned identity is enabled](search-howto-managed-identities-data-sources.md). Remember that user-assigned managed identities won't work for a trusted service connection.
 
    :::image type="content" source="media/search-managed-identities/system-assigned-identity-object-id.png" alt-text="Screenshot of a system identity object identifier." border="true":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新と情報の明確化"
}
```

### Explanation
このコードの変更は、ドキュメントのいくつかの情報を修正するマイナーアップデートです。具体的には、記事の更新日を「2025年5月29日」から「2025年8月4日」に変更しました。また、ユーザー指定のマネージドアイデンティティに関する文言を微調整しました。以前は「現在プレビュー中である」旨を明記していましたが、ユーザー指定のマネージドアイデンティティについての記述を簡潔にし、その不具合についての警告を残しました。これにより、情報がより明確になりました。


