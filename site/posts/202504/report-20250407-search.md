---
date: '2025-04-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f85abdf...MicrosoftDocs:0b31bb0
summary: この変更では、`articles/search/search-data-sources-gallery.md`ファイルが大幅に更新され、新しい検索データソースが追加されるとともに、既存の情報が最新化され、古い情報が削除されました。具体的には、587行が追加され、367行が削除され、合計で954の変更が行われています。新たにMicrosoft
  Active Directory Domain Services、GitHub、Salesforce、SharePointに関する情報が加えられ、これによりAzure
  AI Searchとの統合方法についてのガイダンスが提供されています。また、データソースの構造において変更があったものの、既存のシステムへの影響については詳細が示されていません。全体として、これらの更新は企業がデータマネジメントや検索最適化の課題を解決するにあたり大きな助けとなるでしょう。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f85abdf...MicrosoftDocs:0b31bb0){target="_blank"}

# ハイライト

この変更では、`articles/search/search-data-sources-gallery.md`ファイルの内容が大幅に更新されました。新たに587行が追加され、367行が削除され、合計で954の変更が行われています。主な変更点として、新しい検索データソースの追加、既存の接続情報の最新化、古い情報の削除などが挙げられます。

## 新機能

1. **新しいデータソースの追加**: Microsoft Active Directory Domain Services、GitHub、Salesforce、SharePoint に関する情報が新たに追加されました。これにより、これらのプラットフォームとAzure AI Searchの統合と利用方法についてのガイダンスが提供されています。

## 互換性に影響のある変更

特定の部分でデータソースの構造が変更されましたが、それが既存のシステムにどのように影響するかの詳細は明示されていません。

## その他の更新

- 既存のデータソース説明の向上により、情報の正確さと明確さが増しています。
- 安全なアクセス方法についての情報が強調されています。

# インサイト

今回の変更は、Azure AI Searchを利活用する組織にとって非常に重要です。企業のデータ資産が多様化する中で、これらの新たなデータソースの追加は、多くの企業が抱えるデータマネジメントや検索最適化の課題に対処する大きな手助けとなります。

特に、Microsoft Active Directory Domain Services や Salesforce などの統合は、よりセキュアでスムーズなデータ取り込みを可能にし、既存のシステムとの連携を強化しています。同時に、データソースの更新によって、古い情報が排除され、ユーザーに対する情報提供がより効果的になりました。

この改訂によって、データソースの活用範囲が拡大し、企業が複数のデータチャンネルを効率的に管理するための土台が整いました。プロジェクトの生産性向上と意思決定の迅速化に寄与することが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-data-sources-gallery.md](#item-18727f) | minor update | 検索データソースギャラリーの更新 | modified | 587 | 367 | 954 | 


# Modified Contents
## articles/search/search-data-sources-gallery.md{#item-18727f}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 12/20/2024
+ms.date: 04/05/2025
 ---
 
 # Data sources gallery
@@ -457,6 +457,17 @@ Our Confluence (Cloud Version) Connector is an enterprise grade indexing connect
 [More details](https://www.bainsight.com/connectors/connector-for-confluence-cloud-version/)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -474,6 +485,18 @@ Azure AI Search and secure vector search connector for indexing Atlassian Conflu
 
 ---
 
+### Microsoft Active Directory Domain Services 
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Microsoft Active Directory Domain Services. Can serve as profile search or as source for early-binding security trimming. Comes with full sets of profile metadata and indexes all user-group relationships.
+
+[More details](https://www.rheininsights.com/en/connectors/ldap.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 <a name='azure-ad'></a>
 
 ### Microsoft Entra ID
@@ -536,19 +559,6 @@ Provides the ability to crawl content from an Azure Blob container, allowing inc
 
 [More details](https://contentanalytics.digital.accenture.com/display/aspire40/Azure+Blob+Storage+Connector)
 
-:::column-end:::
-:::column span="":::
-
----
-
-### Azure Data Lake
-
-By [Accenture](https://www.accenture.com)
-
-The Azure Data Lake connector crawls content from the Azure Data Lake Store cloud at either root or specified paths, with incremental crawling, fetching objects ACLs, OAuth 2 authentication and more.
-
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Azure+Data+Lake+Connector)
-
 :::column-end:::
 :::row-end:::
 :::row:::
@@ -565,39 +575,39 @@ The Azure Data Lake connector crawls content from the Azure Data Lake Store clou
 
 ---
 
-### Azure Events Hub
+### Azure Data Lake
 
 By [Accenture](https://www.accenture.com)
 
-Crawls content from an Azure event hub, allowing incremental crawling and retrieval of any type of event or attributes.
+The Azure Data Lake connector crawls content from the Azure Data Lake Store cloud at either root or specified paths, with incremental crawling, fetching objects ACLs, OAuth 2 authentication and more.
 
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Azure+Events+Hub+Connector)
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Azure+Data+Lake+Connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### Azure SQL Database
+### Azure Events Hub
 
-By [BA Insight](https://www.bainsight.com/)
+By [Accenture](https://www.accenture.com)
 
-BA Insight’s Azure SQL Database Connector honors the security of the source database and provides both full and incremental crawls so that users have the latest information available to them all of the time.
+Crawls content from an Azure event hub, allowing incremental crawling and retrieval of any type of event or attributes.
 
-[More details](https://www.bainsight.com/connectors/azure-sql-database-connector-sharepoint-azure-elasticsearch/)
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Azure+Events+Hub+Connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### Bentley
+### Azure SQL Database
 
 By [BA Insight](https://www.bainsight.com/)
 
-The BAI Bentley AssetWise Connector makes it possible to surface content from AssetWise into a single consolidated search index, along with content from other repositories.
+BA Insight’s Azure SQL Database Connector honors the security of the source database and provides both full and incremental crawls so that users have the latest information available to them all of the time.
 
-[More details](https://www.bainsight.com/connectors/bentley-connector-for-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/azure-sql-database-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::row-end:::
@@ -615,13 +625,13 @@ The BAI Bentley AssetWise Connector makes it possible to surface content from As
 
 ---
 
-### Box
+### Bentley
 
-By [Accenture](https://www.accenture.com)
+By [BA Insight](https://www.bainsight.com/)
 
-The Box connector crawls content from a Box repository. The connector retrieves the supported elements via the REST API, providing full or incremental crawling, metadata extraction, fetching ACLs, and more.
+The BAI Bentley AssetWise Connector makes it possible to surface content from AssetWise into a single consolidated search index, along with content from other repositories.
 
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Box++Connector)
+[More details](https://www.bainsight.com/connectors/bentley-connector-for-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::column span="":::
@@ -630,11 +640,11 @@ The Box connector crawls content from a Box repository. The connector retrieves
 
 ### Box
 
-By [BA Insight](https://www.bainsight.com/)
+By [Accenture](https://www.accenture.com)
 
-The Box connector makes it possible to surface content from Box in SharePoint and other portals, enabling users to get integrated search results from SharePoint and Box.
+The Box connector crawls content from a Box repository. The connector retrieves the supported elements via the REST API, providing full or incremental crawling, metadata extraction, fetching ACLs, and more.
 
-[More details](https://www.bainsight.com/connectors/box-connector-sharepoint-azure-elasticsearch/)
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Box++Connector)
 
 :::column-end:::
 :::column span="":::
@@ -643,11 +653,11 @@ The Box connector makes it possible to surface content from Box in SharePoint an
 
 ### Box
 
-By [Raytion](https://www.raytion.com/contact)
+By [BA Insight](https://www.bainsight.com/)
 
-Secure enterprise search connector for reliably indexing content from Box and intelligently searching it with Azure AI Search. It robustly indexes files, folders, comments, users, groups, and tasks from Box in near real time. The connector fully supports Box’ built-in user and group management.
+The Box connector makes it possible to surface content from Box in SharePoint and other portals, enabling users to get integrated search results from SharePoint and Box.
 
-[More details](https://www.raytion.com/connectors/raytion-box-connector)
+[More details](https://www.bainsight.com/connectors/box-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::row-end:::
@@ -665,13 +675,13 @@ Secure enterprise search connector for reliably indexing content from Box and in
 
 ---
 
-### Confluence
+### Box
 
-By [Accenture](https://www.accenture.com)
+By [Raytion](https://www.raytion.com/contact)
 
-The Confluence connector crawls content from any Confluence content repository. The connector retrieves spaces, pages, blogs, attachments, and comments through a REST API, allowing incremental crawling, fetching ACLs, support for HTTP and HTTPS, and more.
+Secure enterprise search connector for reliably indexing content from Box and intelligently searching it with Azure AI Search. It robustly indexes files, folders, comments, users, groups, and tasks from Box in near real time. The connector fully supports Box’ built-in user and group management.
 
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Atlassian+Confluence+Connector)
+[More details](https://www.raytion.com/connectors/raytion-box-connector)
 
 :::column-end:::
 :::column span="":::
@@ -680,11 +690,11 @@ The Confluence connector crawls content from any Confluence content repository.
 
 ### Confluence
 
-By [BA Insight](https://www.bainsight.com/)
+By [Accenture](https://www.accenture.com)
 
-The Confluence Connector is an enterprise grade indexing connector that enables content stored in Confluence to be crawled and indexed. This enables SharePoint, or any other portal, to serve as the single point from which users can search and retrieve the content they need from multiple content sources.
+The Confluence connector crawls content from any Confluence content repository. The connector retrieves spaces, pages, blogs, attachments, and comments through a REST API, allowing incremental crawling, fetching ACLs, support for HTTP and HTTPS, and more.
 
-[More details](https://www.bainsight.com/connectors/confluence-connector-sharepoint-azure-elasticsearch/)
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Atlassian+Confluence+Connector)
 
 :::column-end:::
 :::column span="":::
@@ -693,11 +703,11 @@ The Confluence Connector is an enterprise grade indexing connector that enables
 
 ### Confluence
 
-By [Raytion](https://www.raytion.com/contact)
+By [BA Insight](https://www.bainsight.com/)
 
-Secure enterprise search connector for reliably indexing content from Atlassian Confluence and intelligently searching it with Azure AI Search. It robustly indexes pages, blog posts, attachments, comments, spaces, profiles, and hub sites for tags from on-premises Confluence instances in near real time. The connector fully supports Atlassian Confluence’s built-in user and group management, and Confluence installations based on Microsoft Entra ID and other directory services.
+The Confluence Connector is an enterprise grade indexing connector that enables content stored in Confluence to be crawled and indexed. This enables SharePoint, or any other portal, to serve as the single point from which users can search and retrieve the content they need from multiple content sources.
 
-[More details](https://www.raytion.com/connectors/raytion-confluence-connector)
+[More details](https://www.bainsight.com/connectors/confluence-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::row-end:::
@@ -715,39 +725,39 @@ Secure enterprise search connector for reliably indexing content from Atlassian
 
 ---
 
-### Confluence Cloud
+### Confluence
 
 By [Raytion](https://www.raytion.com/contact)
 
-Secure enterprise search connector for reliably indexing content from Atlassian Confluence Cloud and intelligently searching it with Azure AI Search. It robustly indexes pages, blog posts, attachments, comments, spaces, profiles, and hub sites for tags from Confluence Cloud instances in near real time. The connector fully supports Atlassian Confluence Cloud’s built-in user and group management.
+Secure enterprise search connector for reliably indexing content from Atlassian Confluence and intelligently searching it with Azure AI Search. It robustly indexes pages, blog posts, attachments, comments, spaces, profiles, and hub sites for tags from on-premises Confluence instances in near real time. The connector fully supports Atlassian Confluence’s built-in user and group management, and Confluence installations based on Microsoft Entra ID and other directory services.
 
-[More details](https://www.raytion.com/connectors/raytion-confluence-cloud-connector)
+[More details](https://www.raytion.com/connectors/raytion-confluence-connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### CuadraSTAR
+### Confluence Cloud
 
-By [BA Insight](https://www.bainsight.com/)
+By [Raytion](https://www.raytion.com/contact)
 
-The CuadraSTAR Connector crawls content in CuadraSTAR and creates a single index that makes it possible to use Azure AI Search to find relevant information within CuadraSTAR, and over 70 other supported repositories, eliminating the need to perform separate searches.
+Secure enterprise search connector for reliably indexing content from Atlassian Confluence Cloud and intelligently searching it with Azure AI Search. It robustly indexes pages, blog posts, attachments, comments, spaces, profiles, and hub sites for tags from Confluence Cloud instances in near real time. The connector fully supports Atlassian Confluence Cloud’s built-in user and group management.
 
-[More details](https://www.bainsight.com/connectors/cuadrastar-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.raytion.com/connectors/raytion-confluence-cloud-connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### Database
+### CuadraSTAR
 
-By [Accenture](https://www.accenture.com)
+By [BA Insight](https://www.bainsight.com/)
 
-The Database Server connector crawls content from a Relational Database server, scanning all databases on the server and extracting rows and table information.
+The CuadraSTAR Connector crawls content in CuadraSTAR and creates a single index that makes it possible to use Azure AI Search to find relevant information within CuadraSTAR, and over 70 other supported repositories, eliminating the need to perform separate searches.
 
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Database+Server+Connector)
+[More details](https://www.bainsight.com/connectors/cuadrastar-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::row-end:::
@@ -765,26 +775,26 @@ The Database Server connector crawls content from a Relational Database server,
 
 ---
 
-### Deltek
+### Database
 
-By [BA Insight](https://www.bainsight.com/)
+By [Accenture](https://www.accenture.com)
 
-The Deltek Vision Connector honors the security of the source system and provides both full and incremental crawls, so users always have the latest information available to them. It indexes content from Deltek Vision into Azure, SharePoint in Microsoft 365, or SharePoint 2016/2013, surfacing it through BA Insight's SmartHub to provide users with integrated search results.
+The Database Server connector crawls content from a Relational Database server, scanning all databases on the server and extracting rows and table information.
 
-[More details](https://www.bainsight.com/connectors/deltek-connector-sharepoint-azure-elasticsearch/)
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Database+Server+Connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### Documentum
+### Deltek
 
-By [Accenture](https://www.accenture.com)
+By [BA Insight](https://www.bainsight.com/)
 
-The Aspire Documentum DQL connector crawls content from Documentum, allowing crawls based on user-defined DQL SELECT statements, incremental crawling, fetching of ACLs, group expansion of nested permissions, and more.
+The Deltek Vision Connector honors the security of the source system and provides both full and incremental crawls, so users always have the latest information available to them. It indexes content from Deltek Vision into Azure, SharePoint in Microsoft 365, or SharePoint 2016/2013, surfacing it through BA Insight's SmartHub to provide users with integrated search results.
 
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Documentum+DQL+Connector)
+[More details](https://www.bainsight.com/connectors/deltek-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::column span="":::
@@ -793,11 +803,11 @@ The Aspire Documentum DQL connector crawls content from Documentum, allowing cra
 
 ### Documentum
 
-By [BA Insight](https://www.bainsight.com/)
+By [Accenture](https://www.accenture.com)
 
-BA Insight's Documentum Connector securely indexes both the full text and metadata of Documentum objects into Azure AI Search, enabling a single searchable result set across content from multiple repositories. This connector is unlike some others that surface Documentum records with Azure AI Search one at a time for process management.
+The Aspire Documentum DQL connector crawls content from Documentum, allowing crawls based on user-defined DQL SELECT statements, incremental crawling, fetching of ACLs, group expansion of nested permissions, and more.
 
-[More details](https://www.bainsight.com/connectors/documentum-connector-sharepoint-azure-elasticsearch/)
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Documentum+DQL+Connector)
 
 :::column-end:::
 :::row-end:::
@@ -817,37 +827,38 @@ BA Insight's Documentum Connector securely indexes both the full text and metada
 
 ### Documentum
 
-By [Raytion](https://www.raytion.com/contact)
+By [BA Insight](https://www.bainsight.com/)
 
-Secure enterprise search connector for reliably indexing content from OpenText Documentum and intelligently searching it with Azure AI Search. It robustly indexes repositories, folders and files together with their meta data and properties from Documentum in near real time. The connector fully supports OpenText Documentum’s built-in user and group management.
+BA Insight's Documentum Connector securely indexes both the full text and metadata of Documentum objects into Azure AI Search, enabling a single searchable result set across content from multiple repositories. This connector is unlike some others that surface Documentum records with Azure AI Search one at a time for process management.
+
+[More details](https://www.bainsight.com/connectors/documentum-connector-sharepoint-azure-elasticsearch/)
 
-[More details](https://www.raytion.com/connectors/raytion-documentum-connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### Drupal 
+### Documentum
 
 By [Raytion](https://www.raytion.com/contact)
 
-Raytion's Drupal Connector indexes content from Drupal into Azure AI Search to be able to access and explore all pages and attachments published by Drupal alongside content from other corporate systems in Azure AI Search.
+Secure enterprise search connector for reliably indexing content from OpenText Documentum and intelligently searching it with Azure AI Search. It robustly indexes repositories, folders and files together with their meta data and properties from Documentum in near real time. The connector fully supports OpenText Documentum’s built-in user and group management.
 
-[More details](https://www.raytion.com/connectors/raytion-drupal-connector)
+[More details](https://www.raytion.com/connectors/raytion-documentum-connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### Egnyte
+### Drupal 
 
-By [BA Insight](https://www.bainsight.com/)
+By [Raytion](https://www.raytion.com/contact)
 
-The Egnyte Connector supports both full and incremental crawls and indexes with high throughput.
+Raytion's Drupal Connector indexes content from Drupal into Azure AI Search to be able to access and explore all pages and attachments published by Drupal alongside content from other corporate systems in Azure AI Search.
 
-[More details](https://www.bainsight.com/connectors/egnyte-connector-for-sharepoint-azure-elasticsearch/)
+[More details](https://www.raytion.com/connectors/raytion-drupal-connector)
 
 :::column-end:::
 :::row-end:::
@@ -865,39 +876,40 @@ The Egnyte Connector supports both full and incremental crawls and indexes with
 
 ---
 
-### Elasticsearch
+### Egnyte
 
-By [Accenture](https://www.accenture.com)
+By [BA Insight](https://www.bainsight.com/)
 
-The Elasticsearch connector crawls content from an Elasticsearch index, allowing crawling of multiple indexes, Slice support, use of Get of MGet methods for fetching content, and connection throttling.
+The Egnyte Connector supports both full and incremental crawls and indexes with high throughput.
+
+[More details](https://www.bainsight.com/connectors/egnyte-connector-for-sharepoint-azure-elasticsearch/)
 
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Elasticsearch+Connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### Elite / E3
+### Elasticsearch
 
-By [BA Insight](https://www.bainsight.com/)
+By [Accenture](https://www.accenture.com)
 
-BA Insight's Elite Connector provides a single point of access for lawyers to access firm content and knowledge in line with Elite content using Azure AI Search.
+The Elasticsearch connector crawls content from an Elasticsearch index, allowing crawling of multiple indexes, Slice support, use of Get of MGet methods for fetching content, and connection throttling.
 
-[More details](https://www.bainsight.com/connectors/elite-connector-sharepoint-azure-elasticsearch/)
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Elasticsearch+Connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### EMC eRoom
+### Elite / E3
 
 By [BA Insight](https://www.bainsight.com/)
 
-The eRoom Connector establishes a secure connection to the eRoom application and maps the content, including metadata and attachments, from the eRoom schema to the search engine schema. It then extracts content and feeds it to the search engine in a process called crawling.
+BA Insight's Elite Connector provides a single point of access for lawyers to access firm content and knowledge in line with Elite content using Azure AI Search.
 
-[More details](https://www.bainsight.com/connectors/eroom-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/elite-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::row-end:::
@@ -915,13 +927,13 @@ The eRoom Connector establishes a secure connection to the eRoom application and
 
 ---
 
-### Facebook Workplace
+### EMC eRoom
 
 By [BA Insight](https://www.bainsight.com/)
 
-Organizations who use Workplace by Facebook can now extend the reach of this data into their existing search indexes via the BA Insight Workplace by Facebook Connector.
+The eRoom Connector establishes a secure connection to the eRoom application and maps the content, including metadata and attachments, from the eRoom schema to the search engine schema. It then extracts content and feeds it to the search engine in a process called crawling.
 
-[More details](https://www.bainsight.com/connectors/connector-for-workplace-by-facebook/)
+[More details](https://www.bainsight.com/connectors/eroom-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::column span="":::
@@ -930,23 +942,24 @@ Organizations who use Workplace by Facebook can now extend the reach of this dat
 
 ### Facebook Workplace
 
-By [Raytion](https://www.raytion.com/contact)
+By [BA Insight](https://www.bainsight.com/)
 
-Secure enterprise search connector for reliably indexing content from Facebook Workplace and intelligently searching it with Azure AI Search. It robustly indexes project groups, conversations and shared documents from Facebook Workplace in near real time. The connector fully supports Facebook Workplace’s built-in user and group management.
+Organizations who use Workplace by Facebook can now extend the reach of this data into their existing search indexes via the BA Insight Workplace by Facebook Connector.
 
-[More details](https://www.raytion.com/connectors/raytion-facebook-workplace-connector)
+[More details](https://www.bainsight.com/connectors/connector-for-workplace-by-facebook/)
 
 :::column-end:::
 :::column span="":::
+
 ---
 
-### File Share
+### Facebook Workplace
 
-By [BA Insight](https://www.bainsight.com/)
+By [Raytion](https://www.raytion.com/contact)
 
-The File Share Connector makes it possible to surface content from File Shares (Windows, SMB/CIFS) in a single consolidated search index, along with content from other repositories.
+Secure enterprise search connector for reliably indexing content from Facebook Workplace and intelligently searching it with Azure AI Search. It robustly indexes project groups, conversations and shared documents from Facebook Workplace in near real time. The connector fully supports Facebook Workplace’s built-in user and group management.
 
-[More details](https://www.bainsight.com/connectors/file-share-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.raytion.com/connectors/raytion-facebook-workplace-connector)
 
 :::column-end:::
 :::row-end:::
@@ -964,6 +977,19 @@ The File Share Connector makes it possible to surface content from File Shares (
 
 ---
 
+### File Share
+
+By [BA Insight](https://www.bainsight.com/)
+
+The File Share Connector makes it possible to surface content from File Shares (Windows, SMB/CIFS) in a single consolidated search index, along with content from other repositories.
+
+[More details](https://www.bainsight.com/connectors/file-share-connector-sharepoint-azure-elasticsearch/)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 ### File Share and Network Shares
 
 By [RheinInsights](https://www.rheininsights.com/)
@@ -986,6 +1012,17 @@ The File System connector crawls content from a file system location, allowing i
 [More details](https://contentanalytics.digital.accenture.com/display/aspire40/File+System+Connector)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -1011,6 +1048,19 @@ Secure enterprise search connector for reliably indexing content from e-Spirit F
 
 [More details](https://www.raytion.com/connectors/raytion-firstspirit-connector)
 
+:::column-end:::
+:::column span="":::
+
+---
+
+### Git
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search connector for indexing Git repositories. Reliably indexes branches from remote GIT repositories, versioned files and commit messages. Comes with full metadata sets, and advanced processing pipelines.
+
+[More details](https://www.rheininsights.com/en/connectors/git.php)
+
 :::column-end:::
 :::row-end:::
 :::row:::
@@ -1027,13 +1077,24 @@ Secure enterprise search connector for reliably indexing content from e-Spirit F
 
 ---
 
-### Git
+### GitHub Enterprise Cloud  
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing GitHub Enterprise Cloud. Reliably indexes all repositories, versioned files, wikis, issues or discussions. Comes with full metadata sets, advanced processing pipelines and full support for GitHub Enterprise Cloud's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/github-enterprise-cloud.php)
+
+:::column-end:::
+:::column span="":::
+
+---
 
+### GitHub Enterprise Server  
 By [RheinInsights](https://www.rheininsights.com/)
 
-Azure AI Search connector for indexing Git repositories. Reliably indexes branches from remote GIT repositories, versioned files and commit messages. Comes with full metadata sets, and advanced processing pipelines.
+Azure AI Search and secure vector search connector for indexing GitHub Enterprise Server. Reliably indexes all repositories, versioned files, wikis, issues or discussions. Comes with full metadata sets, advanced processing pipelines and full support for GitHub Enterprise Server's permission model.
 
-[More details](https://www.rheininsights.com/en/connectors/git.php)
+[More details](https://www.rheininsights.com/en/connectors/github-enterprise-server.php)
 
 :::column-end:::
 :::column span="":::
@@ -1049,6 +1110,17 @@ Secure enterprise search connector for reliably indexing content from GitLab and
 [More details](https://www.raytion.com/connectors/raytion-gitlab-connector)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -1075,17 +1147,6 @@ The BAI Google Drive connector makes it possible to surface content from Google
 [More details](https://www.bainsight.com/connectors/google-drive-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
-:::row-end:::
-:::row:::
-:::column span="":::
-
-   :::column-end:::
-   :::column span="":::
-   :::column-end:::
-
-:::row-end:::
-
-:::row:::
 :::column span="":::
 
 ---
@@ -1099,6 +1160,17 @@ Secure enterprise search connector for reliably indexing content from Google Dri
 [More details](https://www.raytion.com/connectors/raytion-google-drive-connector)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -1137,20 +1209,6 @@ Raytion's Happeo Connector indexes content from Happeo into Azure AI Search and
 
 [More details](https://www.raytion.com/connectors/raytion-happeo-connector)
 
-:::column-end:::
-:::column span="":::
-
----
-
-
-### HP Consolidated Archive (EAS)
-
-By [BA Insight](https://www.bainsight.com/)
-
-BA Insight's HP Consolidated Archive Connector securely indexes both the full text and metadata of documents in archives into various search engines, including SharePoint Search and Azure Search. This enables a single searchable result set across content from multiple repositories. It allows organizations to tap into the wealth of information accessible within Consolidated Archive, SharePoint and other repositories, making that data instantly actionable to users through search.
-
-[More details](https://www.bainsight.com/connectors/hp-consolidated-archive-connector-sharepoint-azure-elasticsearch/)
-
 :::column-end:::
 :::row-end:::
 :::row:::
@@ -1167,13 +1225,14 @@ BA Insight's HP Consolidated Archive Connector securely indexes both the full te
 
 ---
 
-### IBM Connections
 
-By [Accenture](https://www.accenture.com)
+### HP Consolidated Archive (EAS)
 
-The IBM Connections connector crawls content from IBM Connections server, featuring incremental crawling, metadata extraction, fetching of ACLs, filtering documents by regex patterns, and more.
+By [BA Insight](https://www.bainsight.com/)
 
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/IBM+Connections+Connector)
+BA Insight's HP Consolidated Archive Connector securely indexes both the full text and metadata of documents in archives into various search engines, including SharePoint Search and Azure Search. This enables a single searchable result set across content from multiple repositories. It allows organizations to tap into the wealth of information accessible within Consolidated Archive, SharePoint and other repositories, making that data instantly actionable to users through search.
+
+[More details](https://www.bainsight.com/connectors/hp-consolidated-archive-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::column span="":::
@@ -1182,11 +1241,11 @@ The IBM Connections connector crawls content from IBM Connections server, featur
 
 ### IBM Connections
 
-By [BA Insight](https://www.bainsight.com/)
+By [Accenture](https://www.accenture.com)
 
-The IBM Connections Connector was developed for IBM Connections, establishing a secure connection to the Connections application and mapping the content, including metadata and attachments, from the Connections schema to the search engine schema. It then extracts content and feeds it to the search engine in a process called crawling.
+The IBM Connections connector crawls content from IBM Connections server, featuring incremental crawling, metadata extraction, fetching of ACLs, filtering documents by regex patterns, and more.
 
-[More details](https://www.bainsight.com/connectors/ibm-connections-connector-sharepoint-azure-elasticsearch/)
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/IBM+Connections+Connector)
 
 :::column-end:::
 :::column span="":::
@@ -1195,11 +1254,11 @@ The IBM Connections Connector was developed for IBM Connections, establishing a
 
 ### IBM Connections
 
-By [Raytion](https://www.raytion.com/contact)
+By [BA Insight](https://www.bainsight.com/)
 
-Secure enterprise search connector for reliably indexing content from IBM Connections and intelligently searching it with Azure AI Search. It robustly indexes public and personal files, blogs, wikis, forums, communities, bookmarks, profiles, and status updates from on-premises Connections instances in near real time. The connector fully supports IBM Connection’s built-in user and group management, and Connections installations based on Microsoft Entra ID and other directory services.
+The IBM Connections Connector was developed for IBM Connections, establishing a secure connection to the Connections application and mapping the content, including metadata and attachments, from the Connections schema to the search engine schema. It then extracts content and feeds it to the search engine in a process called crawling.
 
-[More details](https://www.raytion.com/connectors/raytion-ibm-connections-connector)
+[More details](https://www.bainsight.com/connectors/ibm-connections-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::row-end:::
@@ -1217,39 +1276,39 @@ Secure enterprise search connector for reliably indexing content from IBM Connec
 
 ---
 
-### IBM Connections Cloud
+### IBM Connections
 
 By [Raytion](https://www.raytion.com/contact)
 
-Secure enterprise search connector for reliably indexing content from IBM Connections Cloud and intelligently searching it with Azure AI Search. It robustly indexes public and personal files, blogs, wikis, forums, communities, profiles, and status updates from Connections Cloud in near real time. The connector fully supports IBM Connections Cloud’s built-in user and group management.
+Secure enterprise search connector for reliably indexing content from IBM Connections and intelligently searching it with Azure AI Search. It robustly indexes public and personal files, blogs, wikis, forums, communities, bookmarks, profiles, and status updates from on-premises Connections instances in near real time. The connector fully supports IBM Connection’s built-in user and group management, and Connections installations based on Microsoft Entra ID and other directory services.
 
-[More details](https://www.raytion.com/connectors/raytion-ibm-connections-cloud-connector)
+[More details](https://www.raytion.com/connectors/raytion-ibm-connections-connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### IBM Content Manager
+### IBM Connections Cloud
 
-By [BA Insight](https://www.bainsight.com/)
+By [Raytion](https://www.raytion.com/contact)
 
-The IBM Content Manager Connector honors the security of source applications and provides both full and incremental crawls, so users always have the latest information available to them.
+Secure enterprise search connector for reliably indexing content from IBM Connections Cloud and intelligently searching it with Azure AI Search. It robustly indexes public and personal files, blogs, wikis, forums, communities, profiles, and status updates from Connections Cloud in near real time. The connector fully supports IBM Connections Cloud’s built-in user and group management.
 
-[More details](https://www.bainsight.com/connectors/ibm-content-manager-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.raytion.com/connectors/raytion-ibm-connections-cloud-connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### IBM Db2
+### IBM Content Manager
 
 By [BA Insight](https://www.bainsight.com/)
 
-The Db2 Connector allows organizations to tap into the wealth of data stored within DB2 databases and applications and make that data instantly actionable to users through search.
+The IBM Content Manager Connector honors the security of source applications and provides both full and incremental crawls, so users always have the latest information available to them.
 
-[More details](https://www.bainsight.com/connectors/ibm-db2-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/ibm-content-manager-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::row-end:::
@@ -1265,41 +1324,42 @@ The Db2 Connector allows organizations to tap into the wealth of data stored wit
 :::row:::
 :::column span="":::
 
+
 ---
 
-### IBM FileNet P8
+### IBM Db2
 
 By [BA Insight](https://www.bainsight.com/)
 
-The IBM FileNet Content Manager Connector allows SharePoint, and other portal users, to securely search for content stored in FileNet repositories. Access to content is determined by security established in FileNet, ensuring that your content is as safe when accessed through any other portal as it is directly within FileNet.
+The Db2 Connector allows organizations to tap into the wealth of data stored within DB2 databases and applications and make that data instantly actionable to users through search.
 
-[More details](https://www.bainsight.com/connectors/ibm-filenet-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/ibm-db2-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### IBM Lotus Notes
+### IBM FileNet P8
 
 By [BA Insight](https://www.bainsight.com/)
 
-With BA Insight's IBM Notes Email Connector, users have the ability to search Lotus Notes emails directly from within SharePoint or another portal. Security defined within IBM Notes is automatically reflected in the search experience, so users see search results from their own mailbox, public mailboxes, and other mailboxes for which they have been granted access.
+The IBM FileNet Content Manager Connector allows SharePoint, and other portal users, to securely search for content stored in FileNet repositories. Access to content is determined by security established in FileNet, ensuring that your content is as safe when accessed through any other portal as it is directly within FileNet.
 
-[More details](https://www.bainsight.com/connectors/lotus-notes-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/ibm-filenet-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### IBM WebSphere
+### IBM Lotus Notes
 
 By [BA Insight](https://www.bainsight.com/)
 
-BA Insight's WebSphere Connector securely indexes both the full text and metadata of WebSphere objects into Microsoft's search engine, enabling a single searchable result set across content from multiple repositories. This connector allows organizations to tap into the wealth of information accessible within Microsoft platforms, and makes that data instantly actionable to users through search.
+With BA Insight's IBM Notes Email Connector, users have the ability to search Lotus Notes emails directly from within SharePoint or another portal. Security defined within IBM Notes is automatically reflected in the search experience, so users see search results from their own mailbox, public mailboxes, and other mailboxes for which they have been granted access.
 
-[More details](https://www.bainsight.com/connectors/ibm-websphere-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/lotus-notes-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::row-end:::
@@ -1317,39 +1377,39 @@ BA Insight's WebSphere Connector securely indexes both the full text and metadat
 
 ---
 
-### iManage Cloud
+### IBM WebSphere
 
 By [BA Insight](https://www.bainsight.com/)
 
-BA Insight's iManage Cloud Connector securely indexes both the full text and metadata of documents in the Work workspaces into the search engine.
+BA Insight's WebSphere Connector securely indexes both the full text and metadata of WebSphere objects into Microsoft's search engine, enabling a single searchable result set across content from multiple repositories. This connector allows organizations to tap into the wealth of information accessible within Microsoft platforms, and makes that data instantly actionable to users through search.
 
-[More details](https://www.bainsight.com/connectors/connector-for-imanage-work-cloud/)
+[More details](https://www.bainsight.com/connectors/ibm-websphere-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### iManage Work
+### iManage Cloud
 
 By [BA Insight](https://www.bainsight.com/)
 
-The iManage Work Connector provides full security and operates at high throughput to minimize crawl times while maintaining a low-performance impact on Work. It only requires read access, and there is no need to install client software on any iManage server. This results in seamless and simultaneous access to all content stored in iManage Work.
+BA Insight's iManage Cloud Connector securely indexes both the full text and metadata of documents in the Work workspaces into the search engine.
 
-[More details](https://www.bainsight.com/connectors/imanage-work-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/connector-for-imanage-work-cloud/)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### Jira
+### iManage Work
 
 By [BA Insight](https://www.bainsight.com/)
 
-The Jira Connector enables users to perform searches against all Jira objects, eliminating the need to go to Jira directly.
+The iManage Work Connector provides full security and operates at high throughput to minimize crawl times while maintaining a low-performance impact on Work. It only requires read access, and there is no need to install client software on any iManage server. This results in seamless and simultaneous access to all content stored in iManage Work.
 
-[More details](https://www.bainsight.com/connectors/jira-connector-for-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/imanage-work-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::row-end:::
@@ -1369,6 +1429,19 @@ The Jira Connector enables users to perform searches against all Jira objects, e
 
 ### Jira
 
+By [BA Insight](https://www.bainsight.com/)
+
+The Jira Connector enables users to perform searches against all Jira objects, eliminating the need to go to Jira directly.
+
+[More details](https://www.bainsight.com/connectors/jira-connector-for-sharepoint-azure-elasticsearch/)
+
+:::column-end:::
+:::column span="":::
+
+---
+
+### Jira
+
 By [Raytion](https://www.raytion.com/contact)
 
 Secure enterprise search connector for reliably indexing content from Atlassian Jira and intelligently searching it with Azure AI Search. It robustly indexes projects, issues, attachments, comments, work logs, issue histories, links, and profiles from on-premises Jira instances in near real time. The connector fully supports Atlassian Jira’s built-in user and group management, and Jira installations based on Microsoft Entra ID and other directory services.
@@ -1389,6 +1462,17 @@ Azure AI Search and secure vector search connector for indexing Atlassian Jira S
 [More details](https://www.rheininsights.com/en/connectors/jira.php)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -1414,18 +1498,7 @@ Secure enterprise search connector for reliably indexing content from Atlassian
 
 [More details](https://www.raytion.com/connectors/raytion-jira-cloud-connector)
 
-:::column-end:::
-:::row-end:::
-:::row:::
-:::column span="":::
-
-   :::column-end:::
-   :::column span="":::
-   :::column-end:::
-
-:::row-end:::
-
-:::row:::
+:::column-end:::
 :::column span="":::
 
 ---
@@ -1439,6 +1512,17 @@ Azure AI Search and secure vector search connector for indexing Atlassian Jira C
 [More details](https://www.rheininsights.com/en/connectors/jira-cloud.php)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -1519,13 +1603,12 @@ Secure enterprise search connector for reliably indexing content from directory
 
 ---
 
-### LegalKEY
-
-By [BA Insight](https://www.bainsight.com/) 
+### LDAP Directory Services  
+By [RheinInsights](https://www.rheininsights.com/)
 
-BA Insight's OpenText LegalKEY Connector securely indexes both the full text and metadata of client and matter records in LegalKEY into the Microsoft search engine, enabling a single searchable result set across content from multiple repositories. This connector allows organizations to tap into the wealth of information accessible within LegalKEY, SharePoint, and other repositories, making that data instantly actionable to users through search.
+Azure AI Search and secure vector search connector for indexing LDAP-based directory services. Can serve as profile search or as source for early-binding security trimming. Comes with full sets of profile metadata and indexes all user-group relationships.
 
-[More details](https://www.bainsight.com/connectors/legalkey-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.rheininsights.com/en/connectors/ldap.php)
 
 :::column-end:::
 :::row-end:::
@@ -1541,6 +1624,18 @@ BA Insight's OpenText LegalKEY Connector securely indexes both the full text and
 :::row:::
 :::column span="":::
 
+---
+### LegalKEY
+
+By [BA Insight](https://www.bainsight.com/) 
+
+BA Insight's OpenText LegalKEY Connector securely indexes both the full text and metadata of client and matter records in LegalKEY into the Microsoft search engine, enabling a single searchable result set across content from multiple repositories. This connector allows organizations to tap into the wealth of information accessible within LegalKEY, SharePoint, and other repositories, making that data instantly actionable to users through search.
+
+[More details](https://www.bainsight.com/connectors/legalkey-connector-sharepoint-azure-elasticsearch/)
+
+:::column-end:::
+:::column span="":::
+
 ---
 
 ### LexisNexis InterAction
@@ -1565,6 +1660,17 @@ With the IBM Notes Database Connector, users have the ability to find content st
 [More details](https://www.bainsight.com/connectors/ibm-lotus-notes-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -1578,17 +1684,6 @@ The M-Files connector enables indexing of content managed by the M-Files platfor
 [More details](https://www.bainsight.com/connectors/m-files-connector-for-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
-:::row-end:::
-:::row:::
-:::column span="":::
-
-   :::column-end:::
-   :::column span="":::
-   :::column-end:::
-
-:::row-end:::
-
-:::row:::
 :::column span="":::
 
 ---
@@ -1615,6 +1710,17 @@ Secure enterprise search connector for reliably indexing content from MediaWiki
 [More details](https://www.raytion.com/connectors/raytion-mediawiki-connector)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -1627,6 +1733,31 @@ The HP TRIM Connector was developed for HP Records Manager, establishing a secur
 
 [More details](https://www.bainsight.com/connectors/hp-trim-connector-sharepoint-azure-elasticsearch/)
 
+:::column-end:::
+:::column span="":::
+
+---
+
+### Microsoft Dynamics 365
+
+By [BA Insight](https://www.bainsight.com/)
+
+Our Microsoft Dynamics 365 CRM connector supports both on-premises CRM installations and Dynamics CRM Online.
+
+[More details](https://www.bainsight.com/connectors/microsoft-dynamics-crm-connector-sharepoint-azure-elasticsearch/)
+
+:::column-end:::
+:::column span="":::
+
+---
+
+### Microsoft Dynamics 365  
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Microsoft Dynamics 365. Reliably indexes all knowledge articles, cases, posts, notes, contacts, accounts, sales orders, opportunities and more. Comes with full metadata sets, advanced processing pipelines and full support for Microsoft Dynamics 365's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/dynamics-365.php)
+
 :::column-end:::
 :::row-end:::
 :::row:::
@@ -1643,39 +1774,39 @@ The HP TRIM Connector was developed for HP Records Manager, establishing a secur
 
 ---
 
-### Microsoft Dynamics 365
+### Microsoft Dynamics 365 (Cloud)
 
 By [BA Insight](https://www.bainsight.com/)
 
-Our Microsoft Dynamics 365 CRM connector supports both on-premises CRM installations and Dynamics CRM Online.
+Our Microsoft Dynamics 365 (Cloud Version) CRM Connector establishes a secure connection to the CRM application and maps the content from the CRM schema to the search engine schema.
 
-[More details](https://www.bainsight.com/connectors/microsoft-dynamics-crm-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/connector-for-microsoft-dynamics-cloud/)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### Microsoft Dynamics 365 (Cloud)
+### Microsoft Exchange Online
 
 By [BA Insight](https://www.bainsight.com/)
 
-Our Microsoft Dynamics 365 (Cloud Version) CRM Connector establishes a secure connection to the CRM application and maps the content from the CRM schema to the search engine schema.
+Using the BA Insight Microsoft Exchange Online Connector, users can retrieve content from Exchange Online through various search platforms.
 
-[More details](https://www.bainsight.com/connectors/connector-for-microsoft-dynamics-cloud/)
+[More details](https://www.bainsight.com/connectors/microsoft-exchange-online-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### Microsoft Exchange Online
+### Microsoft Exchange Public Folders
 
 By [BA Insight](https://www.bainsight.com/)
 
-Using the BA Insight Microsoft Exchange Online Connector, users can retrieve content from Exchange Online through various search platforms.
+Using the BAI Microsoft Exchange Public Folders Connector, users can retrieve content from Exchange through various search platforms.
 
-[More details](https://www.bainsight.com/connectors/microsoft-exchange-online-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/microsoft-exchange-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::row-end:::
@@ -1693,26 +1824,26 @@ Using the BA Insight Microsoft Exchange Online Connector, users can retrieve con
 
 ---
 
-### Microsoft Exchange Public Folders
+### Microsoft Exchange Server
 
 By [BA Insight](https://www.bainsight.com/)
 
-Using the BAI Microsoft Exchange Public Folders Connector, users can retrieve content from Exchange through various search platforms.
+Using the BA Insight Microsoft Exchange Connector, users can retrieve content from Exchange through various search engines.
 
-[More details](https://www.bainsight.com/connectors/microsoft-exchange-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/microsoft-exchange-server-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### Microsoft Exchange Server
+### Microsoft SQL Server
 
 By [BA Insight](https://www.bainsight.com/)
 
-Using the BA Insight Microsoft Exchange Connector, users can retrieve content from Exchange through various search engines.
+The database connector is built upon industry standard database access methods, so it can equally support databases from other systems such as Oracle, MySQL, and IBM DB2. It honors the security of the source database and provides both full and incremental crawls, so users always have the latest information available to them.
 
-[More details](https://www.bainsight.com/connectors/microsoft-exchange-server-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/sql-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::column span="":::
@@ -1721,11 +1852,11 @@ Using the BA Insight Microsoft Exchange Connector, users can retrieve content fr
 
 ### Microsoft SQL Server
 
-By [BA Insight](https://www.bainsight.com/)
+By [RheinInsights](https://www.rheininsights.com/)
 
-The database connector is built upon industry standard database access methods, so it can equally support databases from other systems such as Oracle, MySQL, and IBM DB2. It honors the security of the source database and provides both full and incremental crawls, so users always have the latest information available to them.
+Azure AI Search and secure vector search connector for indexing Microsoft SQL databases. Reliably indexes all records based on tables, views and advanced SQL queries. Supports content crawling, as well as, interpreting data structures as user-group relationships for secure search. Comes with full metadata sets, advanced processing pipelines, and support for custom permission models.
 
-[More details](https://www.bainsight.com/connectors/sql-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.rheininsights.com/en/connectors/sql.php)
 
 :::column-end:::
 :::row-end:::
@@ -1743,19 +1874,6 @@ The database connector is built upon industry standard database access methods,
 
 ---
 
-### Microsoft SQL Server
-
-By [RheinInsights](https://www.rheininsights.com/)
-
-Azure AI Search and secure vector search connector for indexing Microsoft SQL databases. Reliably indexes all records based on tables, views and advanced SQL queries. Supports content crawling, as well as, interpreting data structures as user-group relationships for secure search. Comes with full metadata sets, advanced processing pipelines, and support for custom permission models.
-
-[More details](https://www.rheininsights.com/en/connectors/sql.php)
-
-:::column-end:::
-:::column span="":::
-
----
-
 ### Microsoft Teams
 
 By [BA Insight](https://www.bainsight.com/)
@@ -1856,6 +1974,18 @@ Secure enterprise search connector for reliably indexing content from IBM Notes
 
 ---
 
+### Notion  
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing Notion. Reliably indexes databases, pages, attachments, and files. Comes with full metadata sets, advanced processing pipelines and connector-based support for Notion's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/notion.php)
+
+:::column-end:::
+:::column span="":::
+
+---
+
 ### Nuxeo
 
 By [BA Insight](https://www.bainsight.com/)
@@ -1878,6 +2008,17 @@ The Objective Connector was developed for Objective, establishing a secure conne
 [More details](https://www.bainsight.com/connectors/objective-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -1904,17 +2045,6 @@ The OneDrive connector crawls content from Microsoft OneDrive, allowing incremen
 [More details](https://contentanalytics.digital.accenture.com/display/aspire40/OneDrive+Connector)
 
 :::column-end:::
-:::row-end:::
-:::row:::
-:::column span="":::
-
-   :::column-end:::
-   :::column span="":::
-   :::column-end:::
-
-:::row-end:::
-
-:::row:::
 :::column span="":::
 
 ---
@@ -1928,6 +2058,17 @@ Azure AI Search and secure vector search connector for indexing Microsoft OneDri
 [More details](https://www.rheininsights.com/en/connectors/onedrive.php)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -2068,6 +2209,17 @@ The WebCenter Connector integrates WebCenter with Azure AI Search, making it eas
 [More details](https://www.bainsight.com/connectors/oracle-webcenter-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -2081,17 +2233,6 @@ Secure enterprise search connector for reliably indexing content from Oracle Kno
 [More details](https://www.raytion.com/connectors/raytion-oracle-ka-cloud-connector)
 
 :::column-end:::
-:::row-end:::
-:::row:::
-:::column span="":::
-
-   :::column-end:::
-   :::column span="":::
-   :::column-end:::
-
-:::row-end:::
-
-:::row:::
 :::column span="":::
 
 ---
@@ -2118,6 +2259,17 @@ Secure enterprise search connector for reliably indexing content from pirobase C
 [More details](https://www.raytion.com/connectors/raytion-pirobase-cms-connector)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -2131,17 +2283,6 @@ BA Insight's PostgreSQL Connector honors the security of the source database and
 [More details](https://www.bainsight.com/connectors/postgresql-connector-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
-:::row-end:::
-:::row:::
-:::column span="":::
-
-   :::column-end:::
-   :::column span="":::
-   :::column-end:::
-
-:::row-end:::
-
-:::row:::
 :::column span="":::
 
 ---
@@ -2169,6 +2310,17 @@ The BA Insight Practical Law Connector enables users to perform searches against
 [More details](https://www.bainsight.com/connectors/practical-law-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -2192,6 +2344,19 @@ The RDB via Snapshots connector crawls content from any relational database that
 
 [More details](https://contentanalytics.digital.accenture.com/display/aspire40/RDB+via+Snapshots+Connector)
 
+:::column-end:::
+:::column span="":::
+
+---
+
+### RDB via Tables
+
+By [Accenture](https://www.accenture.com)
+
+The RDB via Tables connector crawls content from any relational database that can be accessed using JDBC and performs incremental crawls fetching updates using tables that hold identifiers of updated content. It extracts data directly based on SQL statements.
+
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/RDB+via+Table+Connector)
+
 :::column-end:::
 :::row-end:::
 :::row:::
@@ -2208,26 +2373,26 @@ The RDB via Snapshots connector crawls content from any relational database that
 
 ---
 
-### RDB via Tables
+### S3
 
 By [Accenture](https://www.accenture.com)
 
-The RDB via Tables connector crawls content from any relational database that can be accessed using JDBC and performs incremental crawls fetching updates using tables that hold identifiers of updated content. It extracts data directly based on SQL statements.
+The Amazon S3 connector crawls content from any Amazon Simple Storage Service. It performs incremental crawls, fetch object ACLs for S3 document level security and includes documents stored in buckets, folders and subfolders.
 
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/RDB+via+Table+Connector)
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Amazon+S3+Connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### S3
+### Salesforce
 
 By [Accenture](https://www.accenture.com)
 
-The Amazon S3 connector crawls content from any Amazon Simple Storage Service. It performs incremental crawls, fetch object ACLs for S3 document level security and includes documents stored in buckets, folders and subfolders.
+The Salesforce connector crawls content from a Salesforce repository. The connector supports Salesforce Knowledge Base and Chatter, metadata and custom metadata retrieval, performs full or incremental crawls, fetches ACLs, selectable element types and group expansion.
 
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Amazon+S3+Connector)
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Salesforce+Connector)
 
 :::column-end:::
 :::column span="":::
@@ -2236,11 +2401,11 @@ The Amazon S3 connector crawls content from any Amazon Simple Storage Service. I
 
 ### Salesforce
 
-By [Accenture](https://www.accenture.com)
+By [BA Insight](https://www.bainsight.com/)
 
-The Salesforce connector crawls content from a Salesforce repository. The connector supports Salesforce Knowledge Base and Chatter, metadata and custom metadata retrieval, performs full or incremental crawls, fetches ACLs, selectable element types and group expansion.
+The Salesforce Connector integrates Salesforce's Service, Sales, and Marketing Cloud with Azure AI Search, making all the content within Salesforce available to all employees through this portal.
 
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Salesforce+Connector)
+[More details](https://www.bainsight.com/connectors/salesforce-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::row-end:::
@@ -2260,37 +2425,37 @@ The Salesforce connector crawls content from a Salesforce repository. The connec
 
 ### Salesforce
 
-By [BA Insight](https://www.bainsight.com/)
+By [Raytion](https://www.raytion.com/contact)
 
-The Salesforce Connector integrates Salesforce's Service, Sales, and Marketing Cloud with Azure AI Search, making all the content within Salesforce available to all employees through this portal.
+Secure enterprise search connector for reliably indexing content from Salesforce and intelligently searching it with Azure AI Search. It robustly indexes accounts, chatter messages, profiles, leads, cases, and all other record objects from Salesforce in near real time. The connector fully supports Salesforce’s built-in user and group management.
 
-[More details](https://www.bainsight.com/connectors/salesforce-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.raytion.com/connectors/raytion-salesforce-connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### Salesforce
+### SAP ERP
 
-By [Raytion](https://www.raytion.com/contact)
+By [BA Insight](https://www.bainsight.com/)
 
-Secure enterprise search connector for reliably indexing content from Salesforce and intelligently searching it with Azure AI Search. It robustly indexes accounts, chatter messages, profiles, leads, cases, and all other record objects from Salesforce in near real time. The connector fully supports Salesforce’s built-in user and group management.
+BA Insight's SAP ERP Connector is designed to bring items from SAP into a search index. This in turn lights up the UI and allows for a unified view across information in SAP, SharePoint, and other systems.
 
-[More details](https://www.raytion.com/connectors/raytion-salesforce-connector)
+[More details](https://www.bainsight.com/connectors/sap-erp-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### SAP ERP
+### SAP ERP (Cloud)
 
 By [BA Insight](https://www.bainsight.com/)
 
-BA Insight's SAP ERP Connector is designed to bring items from SAP into a search index. This in turn lights up the UI and allows for a unified view across information in SAP, SharePoint, and other systems.
+BA Insight's SAP ERP (Cloud Version) Connector is designed to bring items from SAP into a search index.
 
-[More details](https://www.bainsight.com/connectors/sap-erp-connector-sharepoint-azure-elasticsearch/)
+[More details](https://www.bainsight.com/connectors/connector-for-sap-erp-cloud/)
 
 :::column-end:::
 :::row-end:::
@@ -2308,24 +2473,24 @@ BA Insight's SAP ERP Connector is designed to bring items from SAP into a search
 
 ---
 
-### SAP ERP (Cloud)
+### SAP HANA
 
 By [BA Insight](https://www.bainsight.com/)
 
-BA Insight's SAP ERP (Cloud Version) Connector is designed to bring items from SAP into a search index.
+The SAP HANA Connector honors the security of the source database and provides both full and incremental crawls, so users always have the latest information available to them. It indexes content from SAP HANA into Azure AI Search, surfacing it through BA Insight's SmartHub to provide users with integrated search results.
 
-[More details](https://www.bainsight.com/connectors/connector-for-sap-erp-cloud/)
+[More details](https://www.bainsight.com/connectors/connector-sap-hana-cloud-version/)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### SAP HANA
+### SAP HANA (Cloud)
 
 By [BA Insight](https://www.bainsight.com/)
 
-The SAP HANA Connector honors the security of the source database and provides both full and incremental crawls, so users always have the latest information available to them. It indexes content from SAP HANA into Azure AI Search, surfacing it through BA Insight's SmartHub to provide users with integrated search results.
+The SAP HANA (Cloud Version) Connector honors the security of the source database and provides both full and incremental crawls so that users have the latest information available all of the time.
 
 [More details](https://www.bainsight.com/connectors/connector-sap-hana-cloud-version/)
 
@@ -2334,13 +2499,14 @@ The SAP HANA Connector honors the security of the source database and provides b
 
 ---
 
-### SAP HANA (Cloud)
 
-By [BA Insight](https://www.bainsight.com/)
+### SAP NetWeaver Portal
 
-The SAP HANA (Cloud Version) Connector honors the security of the source database and provides both full and incremental crawls so that users have the latest information available all of the time.
+By [Raytion](https://www.raytion.com/contact)
 
-[More details](https://www.bainsight.com/connectors/connector-sap-hana-cloud-version/)
+Secure enterprise search connector for reliably indexing content from the SAP NetWeaver Portal (NWP) and intelligently searching it with Azure AI Search. It robustly indexes pages, attachments, and other document types from SAP NWP, its Knowledge Management and Collaboration (KMC) and Portal Content Directory (PCD) areas in near real time. The connector fully supports SAP NetWeaver Portal’s built-in user and group management, and SAP NWP installations based on Microsoft Entra ID and other directory services.
+
+[More details](https://www.raytion.com/connectors/raytion-sap-netweaver-portal-connector)
 
 :::column-end:::
 :::row-end:::
@@ -2358,40 +2524,39 @@ The SAP HANA (Cloud Version) Connector honors the security of the source databas
 
 ---
 
-
-### SAP NetWeaver Portal
+### SAP PLM DMS
 
 By [Raytion](https://www.raytion.com/contact)
 
-Secure enterprise search connector for reliably indexing content from the SAP NetWeaver Portal (NWP) and intelligently searching it with Azure AI Search. It robustly indexes pages, attachments, and other document types from SAP NWP, its Knowledge Management and Collaboration (KMC) and Portal Content Directory (PCD) areas in near real time. The connector fully supports SAP NetWeaver Portal’s built-in user and group management, and SAP NWP installations based on Microsoft Entra ID and other directory services.
+Secure enterprise search connector for reliably indexing content from SAP PLM DMS and intelligently searching it with Azure AI Search. It robustly indexes documents, attachments, and other records from SAP PLM DMS in near real time.
 
-[More details](https://www.raytion.com/connectors/raytion-sap-netweaver-portal-connector)
+[More details](https://www.raytion.com/connectors/raytion-sap-plm-dms-connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### SAP PLM DMS
+### Selenium
 
-By [Raytion](https://www.raytion.com/contact)
+By [Accenture](https://www.accenture.com)
 
-Secure enterprise search connector for reliably indexing content from SAP PLM DMS and intelligently searching it with Azure AI Search. It robustly indexes documents, attachments, and other records from SAP PLM DMS in near real time.
+The Selenium connector crawls content from websites using an internet browser to retrieve several types of documents like web pages, sitemaps, binary documents, and more. It avoids compatibility issues with frameworks like Angular and React.
 
-[More details](https://www.raytion.com/connectors/raytion-sap-plm-dms-connector)
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Selenium+Crawler)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### Selenium
+### ServiceNow
 
 By [Accenture](https://www.accenture.com)
 
-The Selenium connector crawls content from websites using an internet browser to retrieve several types of documents like web pages, sitemaps, binary documents, and more. It avoids compatibility issues with frameworks like Angular and React.
+The ServiceNow connector retrieves several types of documents from a ServiceNow Repository, like Knowledge Articles, Catalog Items and Attachments. It also retrieves security ACLs and performs group expansion.
 
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/Selenium+Crawler)
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/ServiceNow+Connector)
 
 :::column-end:::
 :::row-end:::
@@ -2411,11 +2576,11 @@ The Selenium connector crawls content from websites using an internet browser to
 
 ### ServiceNow
 
-By [Accenture](https://www.accenture.com)
+By [BA Insight](https://www.bainsight.com/)
 
-The ServiceNow connector retrieves several types of documents from a ServiceNow Repository, like Knowledge Articles, Catalog Items and Attachments. It also retrieves security ACLs and performs group expansion.
+ ServiceNow Connector honors the security of the source system and provides both full and incremental crawls, so users always have the latest information available to them.
 
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/ServiceNow+Connector)
+[More details](https://www.bainsight.com/connectors/servicenow-connector-sharepoint-azure-elasticsearch)
 
 :::column-end:::
 :::column span="":::
@@ -2424,24 +2589,24 @@ The ServiceNow connector retrieves several types of documents from a ServiceNow
 
 ### ServiceNow
 
-By [BA Insight](https://www.bainsight.com/)
+By [Raytion](https://www.raytion.com/contact)
 
- ServiceNow Connector honors the security of the source system and provides both full and incremental crawls, so users always have the latest information available to them.
+Secure enterprise search connector for reliably indexing content from ServiceNow and intelligently searching it with Azure AI Search. It robustly indexes issues, tasks, attachments, knowledge management articles, pages, among others from ServiceNow in near real time. The connector supports ServiceNow’s built-in user and group management.
 
-[More details](https://www.bainsight.com/connectors/servicenow-connector-sharepoint-azure-elasticsearch)
+[More details](https://www.raytion.com/connectors/raytion-servicenow-connector)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### ServiceNow
+### SharePoint
 
 By [Raytion](https://www.raytion.com/contact)
 
-Secure enterprise search connector for reliably indexing content from ServiceNow and intelligently searching it with Azure AI Search. It robustly indexes issues, tasks, attachments, knowledge management articles, pages, among others from ServiceNow in near real time. The connector supports ServiceNow’s built-in user and group management.
+Secure enterprise search connector for reliably indexing content from Microsoft SharePoint and intelligently searching it with Azure AI Search. It robustly indexes sites, webs, modern (SharePoint 2016 and later) and classic pages, wiki pages, OneNote documents, list items, tasks, calendar items, attachments, and files from SharePoint on-premises instances in near real time. The connector fully supports Microsoft SharePoint’s built-in user and group management, and Microsoft Entra ID and also OAuth providers like SiteMinder and Okta. The connector comes with support for Basic, NTLM, and Kerberos authentication.
 
-[More details](https://www.raytion.com/connectors/raytion-servicenow-connector)
+[More details](https://www.raytion.com/connectors/raytion-sharepoint-connector)
 
 :::column-end:::
 :::row-end:::
@@ -2459,26 +2624,26 @@ Secure enterprise search connector for reliably indexing content from ServiceNow
 
 ---
 
-### SharePoint
+### SharePoint 2010
 
-By [Raytion](https://www.raytion.com/contact)
+By [BA Insight](https://www.bainsight.com/)
 
-Secure enterprise search connector for reliably indexing content from Microsoft SharePoint and intelligently searching it with Azure AI Search. It robustly indexes sites, webs, modern (SharePoint 2016 and later) and classic pages, wiki pages, OneNote documents, list items, tasks, calendar items, attachments, and files from SharePoint on-premises instances in near real time. The connector fully supports Microsoft SharePoint’s built-in user and group management, and Microsoft Entra ID and also OAuth providers like SiteMinder and Okta. The connector comes with support for Basic, NTLM, and Kerberos authentication.
+BA Insight's SharePoint 2010 Connector allows you to connect to SharePoint 2010, fetch data from any site, document library, or list, and index this content securely.
 
-[More details](https://www.raytion.com/connectors/raytion-sharepoint-connector)
+[More details](https://www.bainsight.com/connectors/sharepoint-2010-connector/)
 
 :::column-end:::
 :::column span="":::
 
 ---
 
-### SharePoint 2010
+### SharePoint 2013
 
-By [BA Insight](https://www.bainsight.com/)
+By [Accenture](https://www.accenture.com)
 
-BA Insight's SharePoint 2010 Connector allows you to connect to SharePoint 2010, fetch data from any site, document library, or list, and index this content securely.
+The SharePoint 2013 connector crawls content from any SharePoint 2013 site collection URL. It performs incremental crawls using SharePoint's change log timestamp or a snapshot database, fetches ACLs, supports NTLM and HTTPS, BCS external lists, and runs without installing anything on SharePoint.
 
-[More details](https://www.bainsight.com/connectors/sharepoint-2010-connector/)
+[More details](https://contentanalytics.digital.accenture.com/display/aspire40/SharePoint+2013+Connector)
 
 :::column-end:::
 :::column span="":::
@@ -2487,11 +2652,11 @@ BA Insight's SharePoint 2010 Connector allows you to connect to SharePoint 2010,
 
 ### SharePoint 2013
 
-By [Accenture](https://www.accenture.com)
+By [BA Insight](https://www.bainsight.com/)
 
-The SharePoint 2013 connector crawls content from any SharePoint 2013 site collection URL. It performs incremental crawls using SharePoint's change log timestamp or a snapshot database, fetches ACLs, supports NTLM and HTTPS, BCS external lists, and runs without installing anything on SharePoint.
+BA Insight's SharePoint 2013 Connector allows you to connect to SharePoint 2013, fetch data from any site, document library, or list, and index this content securely.
 
-[More details](https://contentanalytics.digital.accenture.com/display/aspire40/SharePoint+2013+Connector)
+[More details](https://www.bainsight.com/connectors/sharepoint-2013-connector/)
 
 :::column-end:::
 :::row-end:::
@@ -2509,13 +2674,12 @@ The SharePoint 2013 connector crawls content from any SharePoint 2013 site colle
 
 ---
 
-### SharePoint 2013
-
-By [BA Insight](https://www.bainsight.com/)
+### SharePoint 2013  
+By [RheinInsights](https://www.rheininsights.com/)
 
-BA Insight's SharePoint 2013 Connector allows you to connect to SharePoint 2013, fetch data from any site, document library, or list, and index this content securely.
+Azure AI Search and secure vector search connector for indexing SharePoint 2013. Reliably indexes all SharePoint sites, pages, lists, list items and documents. Comes with full metadata sets, advanced processing pipelines and full support for SharePoint 2013's permission model.
 
-[More details](https://www.bainsight.com/connectors/sharepoint-2013-connector/)
+[More details](https://www.rheininsights.com/en/connectors/sharepoint-server.php)
 
 :::column-end:::
 :::column span="":::
@@ -2557,6 +2721,17 @@ BA Insight's SharePoint Connector allows you to connect to SharePoint 2016, fetc
 :::row:::
 :::column span="":::
 
+---
+### SharePoint 2016  
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing SharePoint 2016. Reliably indexes all SharePoint sites, pages, lists, list items and documents. Comes with full metadata sets, advanced processing pipelines and full support for SharePoint 2016's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/sharepoint-server.php)
+
+:::column-end:::
+:::column span="":::
+
 ---
 
 ### SharePoint 2019
@@ -2572,6 +2747,28 @@ BA Insight's SharePoint Connector allows you to connect to SharePoint 2019, fetc
 
 ---
 
+### SharePoint 2019  
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing SharePoint 2019. Reliably indexes all SharePoint sites, pages, lists, list items and documents. Comes with full metadata sets, advanced processing pipelines and full support for SharePoint 2019's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/sharepoint-server.php)
+
+:::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
+:::column span="":::
+
+---
 ### SharePoint in Microsoft 365
 
 By [Accenture](https://www.accenture.com)
@@ -2593,6 +2790,19 @@ BA Insight's SharePoint Connector allows you to connect to SharePoint in Microso
 
 [More details](https://www.bainsight.com/connectors/sharepoint-online-connector/)
 
+:::column-end:::
+:::column span="":::
+
+---
+
+### SharePoint in Microsoft 365
+
+By [RheinInsights](https://www.rheininsights.com/)
+
+Azure AI Search and secure vector search connector for indexing SharePoint in Microsoft 365. Reliably indexes all SharePoint sites, pages, lists, list items and documents also in multi-geo scenarios. Comes with full metadata sets, advanced processing pipelines, document preview integrations, and full support for SharePoint in Microsoft 365's permission model.
+
+[More details](https://www.rheininsights.com/en/connectors/sharepoint-online.php)
+
 :::column-end:::
 :::row-end:::
 :::row:::
@@ -2609,13 +2819,12 @@ BA Insight's SharePoint Connector allows you to connect to SharePoint in Microso
 
 ---
 
-### SharePoint in Microsoft 365
-
+### SharePoint Server Subscription  
 By [RheinInsights](https://www.rheininsights.com/)
 
-Azure AI Search and secure vector search connector for indexing SharePoint in Microsoft 365. Reliably indexes all SharePoint sites, pages, lists, list items and documents also in multi-geo scenarios. Comes with full metadata sets, advanced processing pipelines, document preview integrations, and full support for SharePoint in Microsoft 365's permission model.
+Azure AI Search and secure vector search connector for indexing SharePoint Server Subscription. Reliably indexes all SharePoint sites, pages, lists, list items and documents. Comes with full metadata sets, advanced processing pipelines and full support for SharePoint Server Subscription's permission model.
 
-[More details](https://www.rheininsights.com/en/connectors/sharepoint-online.php)
+[More details](https://www.rheininsights.com/en/connectors/sharepoint-server.php)
 
 :::column-end:::
 :::column span="":::
@@ -2645,6 +2854,17 @@ Secure enterprise search connector for reliably indexing content from Sitecore a
 [More details](https://www.raytion.com/connectors/raytion-sitecore-connector)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -2658,17 +2878,6 @@ Secure enterprise search connector for reliably indexing content from Slack and
 [More details](https://www.raytion.com/connectors/raytion-slack-connector)
 
 :::column-end:::
-:::row-end:::
-:::row:::
-:::column span="":::
-
-   :::column-end:::
-   :::column span="":::
-   :::column-end:::
-
-:::row-end:::
-
-:::row:::
 :::column span="":::
 
 ---
@@ -2696,6 +2905,17 @@ The SMB connector retrieves files and directories across shared drives. It has D
 [More details](https://contentanalytics.digital.accenture.com/display/aspire40/SMB+Connector)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -2722,17 +2942,6 @@ Secure enterprise search connector for reliably indexing content from SQL databa
 [More details](https://www.raytion.com/connectors/raytion-sql-database-connector)
 
 :::column-end:::
-:::row-end:::
-:::row:::
-:::column span="":::
-
-   :::column-end:::
-   :::column span="":::
-   :::column-end:::
-
-:::row-end:::
-
-:::row:::
 :::column span="":::
 
 ---
@@ -2746,6 +2955,17 @@ The SQL Server Connector is built upon industry standard database access methods
 [More details](https://www.bainsight.com/connectors/sql-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -2885,6 +3105,17 @@ The BA Insight West km Connector supports search across transaction and litigati
 [More details](https://www.bainsight.com/connectors/westkm-connector-sharepoint-azure-elasticsearch/)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -2898,17 +3129,6 @@ Secure enterprise search connector for reliably indexing content from windream E
 [More details](https://www.raytion.com/connectors/raytion-windream-ecm-system-connector)
 
 :::column-end:::
-:::row-end:::
-:::row:::
-:::column span="":::
-
-   :::column-end:::
-   :::column span="":::
-   :::column-end:::
-
-:::row-end:::
-
-:::row:::
 :::column span="":::
 
 ---
@@ -2935,6 +3155,17 @@ Secure enterprise search connector for reliably indexing content from Xerox Docu
 [More details](https://www.raytion.com/connectors/raytion-xerox-docushare-connector)
 
 :::column-end:::
+:::row-end:::
+:::row:::
+:::column span="":::
+
+   :::column-end:::
+   :::column span="":::
+   :::column-end:::
+
+:::row-end:::
+
+:::row:::
 :::column span="":::
 
 ---
@@ -2948,17 +3179,6 @@ The Yammer connector crawls content from Yammer messages. It retrieves messages
 [More details](https://contentanalytics.digital.accenture.com/display/aspire40/Yammer+Connector)
 
 :::column-end:::
-:::row-end:::
-:::row:::
-:::column span="":::
-
-   :::column-end:::
-   :::column span="":::
-   :::column-end:::
-
-:::row-end:::
-
-:::row:::
 :::column span="":::
 
 ---
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
このコードの変更は、`articles/search/search-data-sources-gallery.md`ファイルの内容を大幅に更新するものです。追加された行数が587、削除された行数が367であり、954の変更が加えられました。主に、検索データソースの接続情報を最新のものに更新し、新しい接続の追加や古い情報の削除が行われています。

具体的には、いくつかの新しいデータソースが追加され、以前のデータソースの説明が改善されています。また、一部のデータソースに関してはコンテンツの構造が変更され、新しいデータ形式や安全なアクセスが強調されています。たとえば、Microsoft Active Directory Domain Services や GitHub、Salesforce、SharePointに関する情報が追加され、これらのシステムがどのようにAzure AI Searchと統合され、使用されるかについて詳しく説明しています。

総じて、この変更は情報の正確さと明確さを高め、ユーザーが利用可能なさまざまな検索データソースの活用を促進します。


