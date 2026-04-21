---
date: '2026-04-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:315ccc7...MicrosoftDocs:027b661
summary: このコードの変更では、Azure AI Searchに関する「マルチモーダル検索の概要」と「SharePoint Onlineをインデックスする方法」に対する軽微な更新が行われています。主な内容としては、マルチモーダル検索パイプラインの手順の改良や、SharePointのインデクサー設定に関する追加情報が含まれています。また、新機能として特定の手順やスキルの利用方法に関する詳細な情報が追加され、SharePointのアクセス制御リスト（ACL）同期設定に関する手順が強調されています。互換性のない変更はなく、ドキュメントは更新日が変更され、情報がより簡潔で有用な内容に刷新されています。全体的に、これらの変更はAzure
  AI Searchの機能を向上させ、ユーザーの利便性を高めることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:315ccc7...MicrosoftDocs:027b661){target="_blank"}

<format>
# ハイライト
このコードの変更には、Azure AI Searchにおける「マルチモーダル検索の概要」記事と「SharePoint Onlineをインデックスする方法」の記事に対する軽微な更新が含まれています。更新内容には、マルチモーダル検索パイプラインの手順の改良や、SharePointのインデクサー設定についての追加情報が含まれています。

## 新機能
- 特定の手順やスキルの利用方法に関する詳細な情報を追加。
- SharePointのアクセス制御リスト（ACL）同期設定の詳細な手順の強調。

## 互換性のない変更
- ない

## その他の更新
- ドキュメントの更新日が変更され、新しい情報が追加されることで、より簡潔で有用な内容への刷新。
- Azure AI Searchのスキルリストの更新に伴う選択可能なスキル数の減少。

# 洞察
このコードの変更は、Azure AI Searchの機能と適用に関する最新情報を提供することを目的としています。具体的には、「マルチモーダル検索の概要」記事では、マルチモーダル検索のパイプラインをどのように構築するのかという手順が記述されています。それに伴い、既存のスキルリストから選択可能なスキル数が減少しましたが、これはおそらく、より適切で推奨されるスキルへの誘導を狙ったものと考えられます。

また、「SharePoint Onlineをインデックスする方法」では、SharePointインデクサーを設定するユーザーに対して、アクセス制御リスト（ACL）同期の詳細な設定方法が強調されています。この追加情報により、ユーザーはより適切にアクセス設定を実施できるようになります。これらの更新は、特に企業や開発者が効率的にシステムを利用できるよう支援することを目的としています。全体として、ドキュメントの精度と実用性が向上しており、今後の利用に向けた改善が行われています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [multimodal-search-overview.md](#item-d82192) | minor update | マルチモーダル検索の概要の更新 | modified | 2 | 2 | 4 | 
| [search-how-to-index-sharepoint-online.md](#item-8c099c) | minor update | SharePoint Onlineのインデクサーに関する更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/search/multimodal-search-overview.md{#item-d82192}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn what multimodal search is, how Azure AI Search supports it fo
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 03/25/2026
+ms.date: 04/20/2026
 ---
 
 # Multimodal search in Azure AI Search
@@ -39,7 +39,7 @@ To simplify the creation of a multimodal pipeline, Azure AI Search offers the **
 
 The wizard follows these steps to create a multimodal pipeline:
 
-1. **Extract content:** Choose from the [Document Extraction skill](cognitive-search-skill-document-extraction.md), [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md), or [Azure Content Understanding skill](cognitive-search-skill-content-understanding.md) to obtain page text, inline images, and structural metadata. Each skill offers different capabilities for metadata extraction, table handling, and file format support. For detailed comparisons, see [Options for multimodal content extraction](#options-for-multimodal-content-extraction).
+1. **Extract content:** Choose from the [Document Extraction skill](cognitive-search-skill-document-extraction.md) or [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) to obtain page text, inline images, and structural metadata. Each skill offers different capabilities for metadata extraction, table handling, and file format support. For detailed comparisons, see [Options for multimodal content extraction](#options-for-multimodal-content-extraction).
 
 1. **Chunk text:** The [Text Split skill](cognitive-search-skill-textsplit.md) breaks the extracted text into manageable chunks for use in the remaining pipeline, such as the embedding skill.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダル検索の概要の更新"
}
```

### Explanation
この変更は、Azure AI Searchに関する「マルチモーダル検索の概要」記事の一部における日付の更新と、特定のスキルに関する説明の軽微な修正を含んでいます。具体的には、更新された記事には、マルチモーダルパイプラインを作成する際の手順の説明があり、内容を抽出する際に使用できるスキルのリストが一部変更されています。この修正により、選択可能なドキュメント抽出スキルの数が減っています。これらの変更は、ユーザーに対して最新の情報を提供し、内容の正確性を維持することを目的としています。

## articles/search/search-how-to-index-sharepoint-online.md{#item-8c099c}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Set up a SharePoint in Microsoft 365 indexer to automate indexing o
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 04/16/2026
+ms.date: 04/20/2026
 ms.custom:
   - ignite-2025
   - sfi-image-nochange
@@ -141,7 +141,7 @@ The SharePoint in Microsoft 365 indexer uses a Microsoft Entra application for a
       - If you need to enable content indexing and/or limit [ACL sync (preview)](search-indexer-sharepoint-access-control-lists.md) to specific sites, select:
         - `Sites.Selected`
 
-          Then grant the application full control only for those selected sites.
+          Then grant the application full control only for those selected sites. Review this [SharePoint blog post](https://techcommunity.microsoft.com/blog/spblog/develop-applications-that-use-sites-selected-permissions-for-spo-sites-/3790476) that explains this process.
 
      
           Using application permissions means that the indexer accesses the SharePoint site in a service context. So when you run the indexer, it has access to all content in the SharePoint tenant, which requires tenant admin approval. A client secret or secretless configuration is also required for authentication. Setting up the authentication mechanism is described later in this article under [authentication modes for application API permissions only](#available-authentication-methods-for-application-api-permissions-only).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePoint Onlineのインデクサーに関する更新"
}
```

### Explanation
この変更は、「SharePoint Onlineをインデックスする方法」に関する記事の軽微な修正を示しています。主な更新点は、記事の日付の変更と、SharePointインデクサーに関する追加情報が含まれています。具体的には、特定のサイトに対するACL（アクセス制御リスト）同期の設定についての手順が強調され、ユーザーが必要なプロセスを理解するための詳細なブログ投稿へのリンクが追加されました。この情報は、SharePointサイトへのアクセス権限を正しく設定する際のサポートを提供し、記事の有用性を向上させることを目的としています。


