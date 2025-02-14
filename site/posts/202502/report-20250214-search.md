---
date: '2025-02-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:81f79a9...MicrosoftDocs:f2b9798
summary: このドキュメント更新では、OneLakeファイルのインデックス作成に関する記事が最新情報に基づいて修正されました。新しい機能の追加はなく、主に説明の修正を通じて情報の精度が向上しています。特に、日付の更新やアイデンティティ管理に関する説明の修正が行われています。重大な変更は報告されておらず、文書の最新性と信頼性を高めるための定期的なレビューの重要性が強調されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:81f79a9...MicrosoftDocs:f2b9798){target="_blank"}

# Highlights
このドキュメント更新では、**OneLakeファイルのインデックス作成**に関する記事が最新情報に基づき修正されました。新しい機能追加はなく、主に説明の修正による情報の精度向上が行われています。特に日付の修正とアイデンティティ管理に関する説明の修正があります。

## New features
今回の更新では、新たな機能の追加はありません。

## Breaking changes
特に利用者に影響を与える重大な変更は報告されていません。

## Other updates
- ドキュメントの日付が改訂され、情報の最新性を反映。
- 「システム管理されたアイデンティティ」から「ユーザー割り当ての管理アイデンティティ」への説明の修正。

# Insights
今回のコード差分から得られる注目すべき点は、技術文書の正確さと信頼性を高めるための定期的なレビューと更新の重要性です。具体的には、「システム管理されたアイデンティティ」と「ユーザー割り当ての管理アイデンティティ」に関する誤解を避けるための説明修正がされています。この修正は、Azure上のアクセス管理に取り組む際に、読者がより正確な情報を必要とすることに応えるものです。

日付の更新についても、その意図は情報の最新性を利用者にアピールすることであり、利用者が信頼できる情報源として記事を参照できるようにするための措置と考えられます。この種の継続的な改善は、ドキュメントの長期的な信頼性を維持するために不可欠です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-how-to-index-onelake-files.md](#item-95f3db) | minor update | OneLakeファイルのインデックス作成に関する記事の更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/search-how-to-index-onelake-files.md{#item-95f3db}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 02/12/2025
 ---
 
 # Index data from OneLake files and shortcuts
@@ -156,7 +156,7 @@ The minimum role assignment for your search service identity is Contributor.
 
    :::image type="content" source="media/search-how-to-index-onelake-files/add-system-managed-identity.png" alt-text="Screenshot showing a Contributor role assignment for a search service system identity in the Azure portal." lightbox="media/search-how-to-index-onelake-files/add-system-managed-identity.png" :::
 
-   This screenshot shows a Contributor role assignment using a system managed identity:
+   This screenshot shows a Contributor role assignment using a user-assigned managed identity:
 
    :::image type="content" source="media/search-how-to-index-onelake-files/add-user-assigned-managed-identity.png" alt-text="Screenshot showing a Contributor role assignment for a search service user-assigned managed identity in the Azure portal." lightbox="media/search-how-to-index-onelake-files/add-user-assigned-managed-identity.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLakeファイルのインデックス作成に関する記事の更新"
}
```

### Explanation
この変更では、ドキュメント「OneLakeファイルのインデックス作成」に関する情報が更新されました。具体的には、以下の2つの主な変更が行われています。

1. **日付の更新**: ドキュメント内の「ms.date」フィールドが2024年11月19日から2025年2月12日に変更されました。これにより、情報が最新であることが反映されています。
   
2. **説明の修正**: 「システム管理されたアイデンティティ」を使用した場合の「Contributor」ロールの割り当てに関する説明が修正されました。具体的には、「システム管理されたアイデンティティ」を「ユーザー割り当ての管理アイデンティティ」に置き換えました。これにより、より正確な情報が提供されています。

このように、変更は文書の精度と信頼性を向上させることを目的としています。


