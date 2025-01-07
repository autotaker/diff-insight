---
date: '2025-01-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6122406...MicrosoftDocs:7840f69
summary: このアップデートでは、`search-data-sources-gallery.md`ファイルにAzure AI Search用の新しいコネクタ情報が追加されました。具体的には、Atlassian
  ConfluenceやMicrosoft Entra IDなどの新しいデータソースが含まれ、選択肢が大幅に拡充されました。各コネクタに関する詳細な説明も追加され、企業は自分たちのニーズに合わせた情報検索が可能になります。この更新により、非構造化データのインサイトデリバリーが向上し、意思決定プロセスが迅速化されることが期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6122406...MicrosoftDocs:7840f69){target="_blank"}

# ハイライト
このアップデートでは、`search-data-sources-gallery.md`ファイルにAzure AI Searchのための新しいコネクタ情報が追加されました。具体的には、Atlassian ConfluenceやMicrosoft Entra IDを含むいくつかの新しいデータソースに関する情報を提供し、ユーザーが利用できる選択肢を大幅に拡充しました。 

## 新機能
- Atlassian ConfluenceやMicrosoft Entra IDをはじめとする新しい検索データソースが追加されました。
- 各コネクタの機能や信頼性、サポートされるメタデータセットについて、詳細な説明が追加されました。

## 互換性のない変更
- 特に互換性のない変更は報告されていません。

## その他の更新
- 一部の古い行が削除され、新しい情報で置き換えられました。

# 洞察
このアップデートは、Azure AI Searchが提供するデータソースを利用する際の柔軟性と機能をさらに広げるためのものです。新しいコネクタが追加されたことで、企業や組織は自分たちの特定のニーズに合わせた情報検索が可能になります。

例えば、Atlassian Confluenceのようなチームコラボレーションツールや、Microsoft Entra IDのような認証サービスから直接情報を取得できるようになることで、効率的なインデックス作成と検索パフォーマンスが期待されます。これにより、非構造化データのインサイトデリバリーが向上し、ビジネスの意思決定プロセスが迅速化されるでしょう。

また、各コネクタの詳細な説明と「詳細情報」へのリンクが提供されているため、開発者やIT担当者は新たなコネクションを迅速かつ正確に設定するための必要な情報を容易に得られるようになっています。この文書の更新は、ユーザーエクスペリエンスの向上と、効率的なシステムインテグレーションを目指したものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-data-sources-gallery.md](#item-18727f) | minor update | 検索データソースギャラリーの更新 | modified | 238 | 1 | 239 | 


# Modified Contents
## articles/search/search-data-sources-gallery.md{#item-18727f}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 09/04/2024
+ms.date: 12/20/2024
 ---
 
 # Data sources gallery
@@ -435,6 +435,19 @@ The Aspider connector allows crawling of content from web sites, using HTTP Auth
 
 ---
 
+### Atlassian Confluence
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Atlassian Confluence Server and Data Center. Reliably indexes spaces, personal spaces, wiki pages, blog posts, attachments, and labels. Comes with full metadata sets, advanced processing pipelines, and full support for Atlassian Confluence's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/confluence.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 ### Atlassian Confluence (Cloud)
 
 By [BA Insight](https://www.bainsight.com/)
@@ -448,6 +461,19 @@ Our Confluence (Cloud Version) Connector is an enterprise grade indexing connect
 
 ---
 
+### Atlassian Confluence (Cloud)
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Atlassian Confluence Cloud. Reliably indexes spaces, personal spaces, wiki pages, blog posts, attachments, and labels. Comes with full metadata sets, advanced processing pipelines, and full support for Atlassian Confluence Cloud's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/confluence-cloud.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 <a name='azure-ad'></a>
 
 ### Microsoft Entra ID
@@ -489,6 +515,19 @@ Secure enterprise search connector for reliably indexing content from Microsoft
 
 ---
 
+### Microsoft Entra ID
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Enterprise search connector for indexing Entra ID. Can serve as profile search, also for Azure B2C profiles, or as source for early-binding security trimming. Comes with full sets of profile metadata and indexes all user-group relationships.
+
+[More details](https://www.rheininsights.com/en/connectors/entra-id.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 ### Azure blobs
 
 By [Accenture](https://www.accenture.com)
@@ -925,6 +964,19 @@ The File Share Connector makes it possible to surface content from File Shares (
 
 ---
 
+### File Share and Network Shares
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing file shares. Reliably indexes all files from the given file share. Comes with full metadata sets, advanced processing pipelines, supporting UI features, and full support for the respective file share's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/file-share.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 ### File System
 
 By [Accenture](https://www.accenture.com)
@@ -975,6 +1027,19 @@ Secure enterprise search connector for reliably indexing content from e-Spirit F
 
 ---
 
+### Git
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search connector for indexing Git repositories. Reliably indexes branches from remote GIT repositories, versioned files and commit messages. Comes with full metadata sets, and advanced processing pipelines.
+
+[More details](https://www.rheininsights.com/en/connectors/git.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 ### GitLab
 
 By [Raytion](https://www.raytion.com/contact)
@@ -1038,6 +1103,32 @@ Secure enterprise search connector for reliably indexing content from Google Dri
 
 ---
 
+### Google Drive
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Google Drive. Reliably indexes all Google Drive documents from personal and shared drives in your organization. Comes with full metadata sets, advanced processing pipelines and full support for Google Drive's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/google-drive.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
+### Google Mail
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Google Mail (GMail). Reliably indexes all Mails and their attachments. Comes with full metadata sets, advanced processing pipelines and support for the Google Mail permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/google-mail.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 ### Happeo 
 
 By [Raytion](https://www.raytion.com/contact)
@@ -1289,6 +1380,19 @@ Secure enterprise search connector for reliably indexing content from Atlassian
 
 ---
 
+### Jira
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Atlassian Jira Server and Data Center. Reliably indexes projects, issues, issue comments, and attachments. Comes with full metadata sets, advanced processing pipelines, and full support for Atlassian Jira's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/jira.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 ### Jira Cloud
 
 By [BA Insight](https://www.bainsight.com/)
@@ -1326,6 +1430,19 @@ Secure enterprise search connector for reliably indexing content from Atlassian
 
 ---
 
+### Jira Cloud
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Atlassian Jira Cloud. Reliably indexes projects, issues, issue comments, and attachments. Comes with full metadata sets, advanced processing pipelines, and full support for Atlassian Jira Cloud's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/jira-cloud.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 ### Jive
 
 By [BA Insight](https://www.bainsight.com/)
@@ -1626,6 +1743,19 @@ The database connector is built upon industry standard database access methods,
 
 ---
 
+### Microsoft SQL Server
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Microsoft SQL databases. Reliably indexes all records based on tables, views and advanced SQL queries. Supports content crawling, as well as, interpreting data structures as user-group relationships for secure search. Comes with full metadata sets, advanced processing pipelines, and support for custom permission models.
+
+[More details](https://www.rheininsights.com/en/connectors/sql.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 ### Microsoft Teams
 
 By [BA Insight](https://www.bainsight.com/)
@@ -1752,6 +1882,19 @@ The Objective Connector was developed for Objective, establishing a secure conne
 
 ---
 
+### Odata via REST
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for flexibly indexing custom data via OData over REST. Easily provide your own data via SAP API Management, Google Apigee Management or Azure API Management. Comes with full metadata sets of the provided documents, advanced processing pipelines, and support for custom permission models, also provided via an API endpoint.
+
+[More details](https://www.rheininsights.com/en/connectors/odata.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 ### OneDrive
 
 By [Accenture](https://www.accenture.com)
@@ -1776,6 +1919,20 @@ The OneDrive connector crawls content from Microsoft OneDrive, allowing incremen
 
 ---
 
+### OneDrive
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Microsoft OneDrive for Business. Reliably indexes files from all OneDrives in a tenant. Comes with full metadata sets, advanced processing pipelines, document preview integrations, and full support for Microsoft OneDrive's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/onedrive.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
+
 ### OneDrive for work or school
 
 By [BA Insight](https://www.bainsight.com/)
@@ -1889,6 +2046,19 @@ The Oracle Database Connector is built upon industry standard database access me
 
 ---
 
+### Oracle Database
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Oracle Databases. Reliably indexes all records based on tables, views and advanced SQL queries. Supports content crawling, as well as, interpreting data structures as user-group relationships for secure search. Comes with full metadata sets, advanced processing pipelines, and support for custom permission models.
+
+[More details](https://www.rheininsights.com/en/connectors/sql.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 ### Oracle WebCenter
 
 By [BA Insight](https://www.bainsight.com/)
@@ -1976,6 +2146,19 @@ BA Insight's PostgreSQL Connector honors the security of the source database and
 
 ---
 
+### PostgreSQL
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing PostgreSQL databases. Reliably indexes all records based on tables, views and advanced SQL queries. Supports content crawling, as well as, interpreting data structures as user-group relationships for secure search. Comes with full metadata sets, advanced processing pipelines, and support for custom permission models.
+
+[More details](https://www.rheininsights.com/en/connectors/sql.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 
 ### Practical Law
 
@@ -2426,6 +2609,20 @@ BA Insight's SharePoint Connector allows you to connect to SharePoint in Microso
 
 ---
 
+### SharePoint in Microsoft 365
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing SharePoint in Microsoft 365. Reliably indexes all SharePoint sites, pages, lists, list items and documents also in multi-geo scenarios. Comes with full metadata sets, advanced processing pipelines, document preview integrations, and full support for SharePoint in Microsoft 365's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/sharepoint-online.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
+
 ### Sitecore
 
 By [BA Insight](https://www.bainsight.com/)
@@ -2476,6 +2673,19 @@ Secure enterprise search connector for reliably indexing content from Slack and
 
 ---
 
+### Slack
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Slack. Reliably indexes public and private channels, messages, threads and attached files. Comes with full metadata sets, advanced processing pipelines, and full support for Slack's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/slack.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 
 ### SMB
 
@@ -2553,6 +2763,20 @@ Secure enterprise search connector for reliably indexing content from Symantec E
 
 ---
 
+### Trello
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Trello. Reliably indexes Trello boards, cards, comments, and attachments. Comes with full metadata sets, advanced processing pipelines, and full support for Trello's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/trello.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
+
 ### Twitter
 
 By [Accenture](https://www.accenture.com)
@@ -2639,6 +2863,19 @@ The BA Insight Website Crawler Connector makes it possible to surface content fr
 
 ---
 
+### Website Pages
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing web pages and attached documents. Reliably and easily indexes web pages from a given site. Comes with full metadata sets, advanced processing pipelines, and support for custom permission models.
+
+[More details](https://www.rheininsights.com/en/connectors/web-pages.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 ### West km
 
 By [BA Insight](https://www.bainsight.com/)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索データソースギャラリーの更新"
}
```

### Explanation
このコードの変更は、`search-data-sources-gallery.md`ファイルに238行の新しいコンテンツを追加し、1行を削除したことによるものです。変更の主な内容は、Azure AI Searchに関連する新しいコネクタの情報を追加することです。具体的なコネクタには、Atlassian Confluence、Microsoft Entra ID、Microsoft SQL Server、Google Driveなどが含まれています。

新しいセクションでは、各コネクタの説明が詳細に記載されており、信頼性や機能、サポートされるメタデータセットについても言及されています。これにより、ユーザーは特定のコネクタがどのように機能するか、およびそれぞれの連携に関する「詳細情報」へのリンクが提供されています。全体として、この更新はAzure AI Searchにおける検索データソースの選択肢と情報を強化することを目的としています。


