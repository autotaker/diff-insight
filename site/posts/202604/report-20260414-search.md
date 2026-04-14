---
date: '2026-04-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:876942f...MicrosoftDocs:f7250b6
summary: このドキュメントの更新では、SharePoint のアクセス制御リストに関する重要な情報が強化されています。特に、ADLS Gen2 からインデックス化されたドキュメントでは文書レベルの権限がサポートされていないことが明確に示されています。この情報は、SharePoint
  を利用する組織や開発者にとって重要であり、アクセス管理における期待値を理解する助けとなります。また、文書の日付が2026年3月25日から2026年4月26日に更新されています。この更新により、ユーザーは
  SharePoint のセキュリティモデルについてより深く理解できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:876942f...MicrosoftDocs:f7250b6){target="_blank"}

<format>
# ハイライト
このドキュメントの更新では、SharePoint のアクセス制御リストに関する情報が強化されており、新しい機能の説明が追加されています。特筆すべきは、ADLS Gen2 からインデックス化されたドキュメントでは、文書レベルの権限がサポートされていないことが明確に示されています。こうした情報は、SharePoint の権限に関連するトピックをよりよく理解するために重要です。

## 新機能
- ADLS Gen2 からのインデックス化されたドキュメント内での文書レベルの権限がサポートされないことに関する説明が追加されました。

## 破壊的変更
- 文書レベルの権限に関するドキュメントの更新は、既存のシステムには直接的な破壊的影響は与えませんが、権限モデルの理解に重要な変更を含んでいます。

## その他の更新
- ドキュメントの日付が2026年3月25日から2026年4月26日に更新されました。

# インサイト
今回のドキュメントの更新は、SharePoint のアクセス制御リスト（ACL）に関する重要な新情報を含んでいます。特に、ADLS Gen2 からインデックス化されたドキュメントに対する文書レベルの権限がサポートされないことが詳細に説明されています。この情報は、SharePoint を使用している組織や開発者にとって非常に重要で、インデクサーを使用する際の期待値を正しく管理する上で役立つでしょう。

文書レベルの権限がサポートされないということは、インデックス化されたコンテンツの管理において、ユーザーが権限の範囲を超えた情報にアクセスすることを防ぐ上での重要な側面となります。この更新により、ユーザーは SharePoint とその周辺技術におけるセキュリティモデルに対するより深い理解を得られることが期待できます。

このようなドキュメントの更新は、多くの組織がデータの安全性およびアクセシビリティを確保できるようにするために必要不可欠です。SharePoint のACLを理解することで、ユーザーは情報に対するアクセス制御をより効果的に管理し、コンプライアンス要求を満たすことができるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-indexer-sharepoint-access-control-lists.md](#item-532a24) | minor update | SharePoint アクセス制御リストのドキュメント更新 | modified | 13 | 1 | 14 | 


# Modified Contents
## articles/search/search-indexer-sharepoint-access-control-lists.md{#item-532a24}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to configure Azure AI Search indexers for ingesting Acces
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/25/2026
+ms.date: 04/26/2026
 ---
 
 # Use a SharePoint indexer to ingest permission metadata and filter search results based on user access rights
@@ -43,6 +43,18 @@ This article explains how to ingest an access control list (ACL) alongside other
   + [Shareable links](/sharepoint/shareable-links-anyone-specific-people-organization) scoped to "Anyone" or "People in your organization." Only links scoped to "Specific people" are supported.
 
   + [SharePoint groups](/sharepoint/modern-experience-sharing-permissions) that can't be resolved to Microsoft Entra groups (such as Owners, Members, Visitors groups).
+ 
++ The following indexer features don't support permission inheritance in indexed documents originating from ADLS Gen2. If you use any of these features in a skillset or indexer, document-level permissions aren't included in the indexed content.
+
+  + [Custom Web API skill](cognitive-search-custom-skill-web-api.md)
+
+  + [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md)
+
+  + [Knowledge store](knowledge-store-concept-intro.md)
+
+  + [Indexer enrichment cache](enrichment-cache-how-to-configure.md)
+
+  + [Debug sessions](cognitive-search-debug-session.md)
 
 
 ## Support for the SharePoint permission model
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint アクセス制御リストのドキュメント更新"
}
```

### Explanation
この変更は、SharePoint アクセス制御リストに関するドキュメントの更新を示しています。具体的には、ファイルのメタデータの日付が 2026 年 3 月 25 日から 2026 年 4 月 26 日に変更され、数行の情報が追加されました。新たに追加された内容は、ADLS Gen2 からのインデックス化されたドキュメント内の文書レベルの権限をサポートしないインデクサーの機能について説明しています。これにより、特定のスキルセットやインデクサーで使用されると、インデックス化されたコンテンツには計上されない文書レベルの権限があることが明記されています。このような更新により、ユーザーは SharePoint の権限モデルのサポートに関する理解を深めることができるようになります。


