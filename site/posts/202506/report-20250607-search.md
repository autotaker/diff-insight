---
date: '2025-06-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e10a743...MicrosoftDocs:b06c631
summary: このコード差分は、Azure AI Search関連のドキュメント内での複数のファイルに渡るマイナーマイナアップデートを示しています。特に検索インデックス、エージェンティックリトリーバル、プライベートリンクに関連するテキストの改善が行われています。新機能の追加は特に記載されていないものの、エージェンティックリトリーバルなどの項目が追加されています。破壊的な変更はなく、全ての変更は既存の情報を改善するものです。ドキュメントの日付更新やテキストの変更、リンク修正が行われ、文書全体の質が向上し、ユーザーがより効率的に情報を得られることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e10a743...MicrosoftDocs:b06c631){target="_blank"}

# Highlights
このコード差分は、Azure AI Search関連のドキュメント内での複数のファイルに渡るマイナーマイナアップデートを示しています。特に検索インデックス、エージェンティックリトリーバル、およびプライベートリンクに関連するテキストの改善が行われています。

## 新機能
特定の新機能は記載されていませんが、エージェンティックリトリーバルなどの新たな項目が追加されています。

## 破壊的な変更
破壊的な変更については言及されていません。すべての変更は既存の情報を改善するものと見なされます。

## その他の更新
ドキュメントの日付更新、テキストの変更、リンク修正、項目の追加と削除、並べ替えに関する微調整が加えられています。

# インサイト
この一連のアップデートは文書全体の質を上げ、ユーザーがより効率的に情報を得られるようになることを目的としています。以下では、各ファイルがどのように改善されたかについて詳しく説明します。

### 1. `articles/search/index.yml`
このファイルの更新は、ユーザーガイドにおける検索インデックスの定義と使用方法の表現に焦点を当てています。「Create a vector index」から「Add vectors to an index」への変更は、より実際的で具体的な操作を示すため、初心者ユーザーにも直感的に理解できる表現となっています。また、新しいリンクの追加と整理により、参考情報へのアクセスが改善されています。

### 2. `articles/search/search-agentic-retrieval-how-to-index.md`
この変更では、タイトルを「Define an index for agentic retrieval」から「Design an index for agentic retrieval」に変更することで、計画と設計というプロセス重視の姿勢を反映しています。この表現の精緻化により、ユーザーはインデックスの性質をより具体的に理解できるようになっています。

### 3. `articles/search/search-index-azure-sql-managed-instance-with-managed-identity.md`
この更新は、Azure SQL Managed Instanceに関するテキストの正確性を高めることを意図しています。具体的な変更としては、日付の更新、文言の改善、情報の構造化により、ガイダンスとしての信頼性が向上しています。技術的な用語や指示が高度に整理され、手順の理解と実施がしやすくなっています。

### 4. `articles/search/toc.yml`
目次の改善は、ドキュメント全体のナビゲーションを容易にすることを目的としています。セクション名の変更や新しい項目の追加により文書全体の流動性が向上し、ユーザーは必要な情報を迅速に見つけることができます。一貫した命名規則の適用は、ドキュメントの価値をさらに高めます。

### 5. `articles/search/troubleshoot-shared-private-link-resources.md`
このファイルでは、トラブルシューティングに関する情報がより明確になり、エラーメッセージの具体化や文の改善が見られました。特にエラー条件や技術的なフォーマットの改善により、ドキュメント全体のプロフェッショナルさと有用性が高まりました。ユーザーは手順に従いやすく、実際の課題解決により役立ちます。

これら一連の更新により、Azure AI Searchに関するドキュメントの一貫性、可読性、ユーザビリティが向上し、より良いユーザー体験を提供しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index.yml](#item-c67121) | minor update | 検索インデックスに関するテキストの変更と整理 | modified | 4 | 4 | 8 | 
| [search-agentic-retrieval-how-to-index.md](#item-a078ea) | minor update | エージェンティックリトリーバル用インデックスのタイトル修正 | modified | 2 | 2 | 4 | 
| [search-index-azure-sql-managed-instance-with-managed-identity.md](#item-a4ec86) | minor update | Azure SQL Managed Instanceによるインデクサ接続のドキュメントのテキスト修正 | modified | 18 | 19 | 37 | 
| [toc.yml](#item-c4768f) | minor update | 目次の改善と構造の整理 | modified | 127 | 125 | 252 | 
| [troubleshoot-shared-private-link-resources.md](#item-0e1867) | minor update | 共有プライベートリンクリソースに関するトラブルシューティングガイドの更新 | modified | 26 | 26 | 52 | 


# Modified Contents
## articles/search/index.yml{#item-c67121}

<details>
<summary>Diff</summary>
````diff
@@ -38,7 +38,7 @@ landingContent:
             url: search-manage.md
           - text: Create a search index
             url: search-get-started-portal.md
-          - text: Create a vector index
+          - text: Add vectors to an index
             url: search-get-started-vector.md
           - text: Query a vector index
             url: vector-search-how-to-query.md
@@ -62,10 +62,10 @@ landingContent:
             url: vector-search-how-to-quantization.md
       - linkListType: quickstart
         links:
-          - text: Run an agentic retrieval pipeline
+          - text: 'Classic RAG'
+            url: search-get-started-agentic-retrieval.md
+          - text: 'Agentic retrieval'
             url: search-get-started-agentic-retrieval.md
-          - text: Retrieve data using an LLM
-            url: search-get-started-rag.md
 
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスに関するテキストの変更と整理"
}
```

### Explanation
この変更は `articles/search/index.yml` ファイルに対するマイナーアップデートであり、主に検索インデックスに関連するテキストの表現や構成を改善しています。具体的には、以下のような変更が含まれています。

1. **テキストの変更**: 「Create a vector index」というテキストを「Add vectors to an index」に変更し、より明確な指示を提供しています。
2. **リンクの整理**: 新しい内容として「Classic RAG」および「Agentic retrieval」というテキストを追加し、関連するURLを更新しました。このことにより、ユーザーがよりよいリソースにアクセスできるようになっています。
3. **不要なリンクの削除**: 古いリンクや冗長な表現を削除し、情報の過剰を防ぐことで、ファイルの可読性を向上させています。

全体として、これらの変更は文書の改善とともに、ユーザーエクスペリエンスの向上を狙ったものであると言えます。

## articles/search/search-agentic-retrieval-how-to-index.md{#item-a078ea}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Define an index for agentic retrieval
+title: Design an index for agentic retrieval
 titleSuffix: Azure AI Search
 description: Create an index that has fields and configurations that work for agentic retrieval workloads in Azure AI Search.
 
@@ -11,7 +11,7 @@ ms.topic: how-to
 ms.date: 05/05/2025
 ---
 
-# Define an index for agentic retrieval in Azure AI Search
+# Design an index for agentic retrieval in Azure AI Search
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェンティックリトリーバル用インデックスのタイトル修正"
}
```

### Explanation
この変更は `articles/search/search-agentic-retrieval-how-to-index.md` ファイルに対するマイナーアップデートであり、主にドキュメントのタイトルに関する修正が行われています。具体的な変更内容は以下の通りです。

1. **タイトルの修正**: ドキュメントのタイトルが「Define an index for agentic retrieval」から「Design an index for agentic retrieval」に変更されました。この変更により、より適切で正確な表現になっています。
2. **セクションタイトルの更新**: ドキュメント内のセクションタイトルも同様に更新され、タイトルは一貫性が保たれています。

この変更は、内容の明確さを向上させ、ユーザーがドキュメントで提供されている情報の意図をより正確に理解できるようにすることを目的としています。全体として、これらの修正はファイルの可読性を高めるものとなっています。

## articles/search/search-index-azure-sql-managed-instance-with-managed-identity.md{#item-a4ec86}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 05/29/2025
+ms.date: 06/04/2025
 ---
 
 # Set up an indexer connection to Azure SQL Managed Instance using a managed identity
@@ -18,7 +18,7 @@ This article describes how to set up an Azure AI Search indexer connection to [S
 
 You can use a system-assigned managed identity or a user-assigned managed identity (preview). Managed identities are Microsoft Entra logins and require Azure role assignments to access data in SQL Managed Instance.
 
-Before learning more about this feature, it's recommended that you understand what an indexer is and how to set up an indexer for your data source. More information can be found at the following links:
+Before learning more about this feature, we recommended that you understand what an indexer is and how to set up an indexer for your data source. More information can be found at the following links:
 
 * [Indexer overview](search-indexer-overview.md)
 * [SQL Managed Instance indexer](search-how-to-index-sql-database.md)
@@ -29,30 +29,29 @@ Before learning more about this feature, it's recommended that you understand wh
 
 * Microsoft Entra admin role on SQL Managed Instance:
 
-  To assign read permissions on SQL Managed Instance, you must be an Azure Global Admin with a SQL Managed Instance. See [Configure and manage Microsoft Entra authentication with SQL Managed Instance](/azure/azure-sql/database/authentication-aad-configure) and follow the steps to provision a Microsoft Entra admin (SQL Managed Instance). 
+  To assign read permissions on SQL Managed Instance, you must be an Azure Global Admin with a SQL Managed Instance. See [Configure and manage Microsoft Entra authentication with SQL Managed Instance](/azure/azure-sql/database/authentication-aad-configure) and follow the steps to provision a Microsoft Entra admin (SQL Managed Instance).
 
-* [Configure a public endpoint and network security group in SQL Managed Instance](search-how-to-index-sql-managed-instance.md) to allow connections from Azure AI Search. Connecting through a Shared Private Link when using a managed identity isn't currently supported.
+* [Configure a public endpoint and network security group in SQL Managed Instance](search-how-to-index-sql-managed-instance.md) to allow connections from Azure AI Search. Connecting through a shared private link when using a managed identity isn't currently supported.
 
-## 1 - Assign permissions to read the database
+## Assign permissions to read the database
 
 Follow these steps to assign the search service system managed identity permission to read the SQL Managed database.
 
 1. Connect to your SQL Managed Instance through SQL Server Management Studio (SSMS) by using one of the following methods:
 
     - [Configure a point-to-site connection from on-premises](/azure/azure-sql/managed-instance/point-to-site-p2s-configure)
-    - [Configure an Azure VM](/azure/azure-sql/managed-instance/connect-vm-instance-configure)
+    - [Configure an Azure virtual machine](/azure/azure-sql/managed-instance/connect-vm-instance-configure)
 
 1. Authenticate with your Microsoft Entra account.
 
    :::image type="content" source="./media/search-index-azure-sql-managed-instance-with-managed-identity/sql-login.png" alt-text="Showing screenshot of the Connect to Server dialog.":::
 
-1. From the left pane, locate the SQL database you are using as data source for indexing and right-click it. Select **New Query**. 
+1. From the left pane, locate the SQL database you're using as data source for indexing and right-click it. Select **New Query**.
 
    :::image type="content" source="./media/search-index-azure-sql-managed-instance-with-managed-identity/new-sql-query.png" alt-text="Showing screenshot of new SQL query.":::
 
-1. In the T-SQL window, copy the following commands and include the brackets around your search service name. Click on **Execute**.
+1. In the T-SQL window, copy the following commands and include the brackets around your search service name. Select **Execute**.
 
-    
     ```sql
     CREATE USER [insert your search service name here or user-assigned managed identity name] FROM EXTERNAL PROVIDER;
     EXEC sp_addrolemember 'db_datareader', [insert your search service name here or user-assigned managed identity name];
@@ -68,9 +67,9 @@ sp_droprolemember 'db_datareader', [insert your search service name or user-assi
 DROP USER IF EXISTS [insert your search service name or user-assigned managed identity name];
 ```
 
-## 2 - Add a role assignment
+## Add a role assignment
 
-In this step, you'll give your Azure AI Search service permission to read data from your SQL Managed Instance.
+In this step, you give your Azure AI Search service permission to read data from your SQL Managed Instance.
 
 1. In the Azure portal, navigate to your SQL Managed Instance page.
 1. Select **Access control (IAM)**.
@@ -86,15 +85,15 @@ In this step, you'll give your Azure AI Search service permission to read data f
 
     :::image type="content" source="./media/search-index-azure-sql-managed-instance-with-managed-identity/add-role-assignment.png" alt-text="Showing screenshot of the member role assignment.":::
 
-## 3 - Create the data source
+## Create the data source
 
 Create the data source and provide a system-assigned managed identity. 
 
 ### System-assigned managed identity
 
-The [REST API](/rest/api/searchservice/data-sources/create), Azure portal, and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) support system-assigned managed identity. 
+The [REST API](/rest/api/searchservice/data-sources/create), Azure portal, and the [.NET SDK](/dotnet/api/azure.search.documents.indexes.models.searchindexerdatasourceconnection) support system-assigned managed identity.
 
-When you're connecting with a system-assigned managed identity, the only change to the data source definition is the format of the "credentials" property. You'll provide an Initial Catalog or Database name and a `ResourceId` that has no account key or password. The `ResourceId` must include the subscription ID of SQL Managed Instance, the resource group of SQL Managed instance, and the name of the SQL database. 
+When you're connecting with a system-assigned managed identity, the only change to the data source definition is the format of the "credentials" property. You provide an Initial Catalog or Database name and a `ResourceId` that has no account key or password. The `ResourceId` must include the subscription ID of SQL Managed Instance, the resource group of SQL Managed instance, and the name of the SQL database.
 
 Here's an example of how to create a data source to index data from a storage account using the [Create Data Source](/rest/api/searchservice/data-sources/create) REST API and a managed identity connection string. The managed identity connection string format is the same for the REST API, .NET SDK, and the Azure portal.  
 
@@ -115,11 +114,11 @@ api-key: [admin key]
 } 
 ```
 
-## 4 - Create the index
+## Create the index
 
 The index specifies the fields in a document, attributes, and other constructs that shape the search experience.
 
-Here's a [Create Index](/rest/api/searchservice/indexes/create) REST API call with a searchable `booktitle` field:   
+Here's a [Create Index](/rest/api/searchservice/indexes/create) REST API call with a searchable `booktitle` field:
 
 ```http
 POST https://[service name].search.windows.net/indexes?api-version=2024-07-01
@@ -135,9 +134,9 @@ api-key: [admin key]
 }
 ```
 
-## 5 - Create the indexer
+## Create the indexer
 
-An indexer connects a data source with a target search index, and provides a schedule to automate the data refresh. Once the index and data source have been created, you're ready to create the indexer.
+An indexer connects a data source with a target search index, and provides a schedule to automate the data refresh. Once the index and data source are created, you're ready to create the indexer.
 
 Here's a [Create Indexer](/rest/api/searchservice/indexers/create) REST API call with an Azure SQL indexer definition. The indexer runs when you submit the request.
 
@@ -155,7 +154,7 @@ api-key: [admin key]
 
 ## Troubleshooting
 
-If you get an error when the indexer tries to connect to the data source that says that the client is not allowed to access the server, take a look at [common indexer errors](./search-indexer-troubleshooting.md).
+If you get an error when the indexer tries to connect to the data source that says that the client isn't allowed to access the server, see the [common indexer errors](./search-indexer-troubleshooting.md).
 
 You can also rule out any firewall issues by trying the connection with and without restrictions in place.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure SQL Managed Instanceによるインデクサ接続のドキュメントのテキスト修正"
}
```

### Explanation
この変更は `articles/search/search-index-azure-sql-managed-instance-with-managed-identity.md` ファイルに対するマイナーアップデートで、主に文中の表現やフォーマットに関する修正が行われています。具体的には以下の変更が含まれています。

1. **日付の更新**: `ms.date` の値が「05/29/2025」から「06/04/2025」に変更され、ドキュメントの最新性を反映しています。
2. **文言の改善**: 「recommended」が「it's recommended」から「we recommended」に変更され、読みやすく、より自然な表現になっています。同様に、いくつかの見出しや説明文の表現が整理されています。
3. **箇条書きの整列**: 情報の提示方法が見直され、箇条書きやステップの順序が整理されています。これにより、ユーザーが手順を追いやすくなり、理解が深まります。
4. **不要な空行や不要な文字の削除**: 不必要な空行や特定の文字（例: 「-」の削除）を整理し、文書全体の明確さと一貫性を向上させています。

これらの修正は全体として、ドキュメントの可読性と理解しやすさを向上させるものであり、ユーザーがAzure SQL Managed Instanceにおけるインデクサ接続の設定方法をより効果的に把握できるようにすることを目的としています。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -251,14 +251,14 @@ items:
         href: search-manage-rest.md
       - name: Move service across regions
         href: search-howto-move-across-regions.md
-  - name: Index management
+  - name: Indexing
     items:
+    - name: Index via portal wizards
+      href: search-import-data-portal.md
     - name: Create an index
       href: search-how-to-create-search-index.md
     - name: Load an index
       href: search-how-to-load-search-index.md
-    - name: Index via portal wizards
-      href: search-import-data-portal.md
     - name: Update or rebuild an index
       href: search-howto-reindex.md
     - name: Alias an index
@@ -337,7 +337,7 @@ items:
         href: search-how-to-index-onelake-files.md
       - name: SharePoint Online
         href: search-howto-index-sharepoint-online.md
-    - name: Skillsets
+    - name: Skillsets (indexers)
       items:
       - name: Create a skillset
         href: cognitive-search-defining-skillset.md
@@ -371,133 +371,135 @@ items:
           href: cognitive-search-custom-skill-scale.md
         - name: Example - Bing Entity Search
           href: cognitive-search-create-custom-skill-example.md
-  - name: Agentic retrieval
-    items:
-    - name: Create a knowledge agent
-      href: search-agentic-retrieval-how-to-create.md
-    - name: Use a knowledge agent to retrieve data
-      href: search-agentic-retrieval-how-to-retrieve.md
-    - name: Define an index for agentic retrieval
-      href: search-agentic-retrieval-how-to-index.md
-    - name: Build an agentic retrieval pipeline
-      href: search-agentic-retrieval-how-to-pipeline.md
-  - name: Vector search
-    items:
-    - name: Create a vector index
-      href: vector-search-how-to-create-index.md
-    - name: Chunk documents
-      href: vector-search-how-to-chunk-documents.md
-    - name: Chunk and vectorize by document layout
-      href: search-how-to-semantic-chunking.md
-    - name: Generate embeddings
-      href: vector-search-how-to-generate-embeddings.md
-    - name: Use integrated vectorization
-      href: search-how-to-integrated-vectorization.md
-    - name: Use embedding models from Azure AI Foundry
-      href: vector-search-integrated-vectorization-ai-studio.md
-    - name: Reduce vector size
-      items:
-      - name: Understand vector quotas and limits
-        href: vector-search-index-size.md
-      - name: Choose an optimization strategy
-        href: vector-search-how-to-configure-compression-storage.md
-      - name: Compress using binary or scalar quantization
-        href: vector-search-how-to-quantization.md
-      - name: Index binary data for vector search
-        href: vector-search-how-to-index-binary-data.md
-      - name: Assign narrow data types
-        href: vector-search-how-to-assign-narrow-data-types.md
-      - name: Eliminate redundant storage
-        href: vector-search-how-to-storage-options.md
-      - name: Truncate dimensions
-        href: vector-search-how-to-truncate-dimensions.md
-    - name: Query vectors
-      href: vector-search-how-to-query.md
-    - name: Use multi-vector fields
-      href: vector-search-multi-vector-fields.md
-    - name: Add a vectorizer for text-to-vector queries
-      displayName: query
-      href: vector-search-how-to-configure-vectorizer.md
-    - name: Filter on vector queries
-      displayName: query
-      href: vector-search-filters.md
-  - name: Keyword search
+  - name: Retrieval
     items:
-    - name: Full text query
-      href: search-query-create.md
-    - name: Typeahead query
-      href: search-add-autocomplete-suggestions.md
-    - name: Query examples (simple syntax)
-      href: search-query-simple-examples.md
-    - name: Add spell check
-      href: speller-how-to-add.md
-    - name: Add synonyms
-      href: search-synonyms.md
-    - name: Add a suggester for typeahead
-      href: index-add-suggesters.md
-    - name: Design a multilingual index
-      href: search-language-support.md
-    - name: Model complex data types
-      href: search-howto-complex-data-types.md
-    - name: Model relational data
-      href: index-sql-relational-data.md
-    - name: Analyzers
+    - name: Agentic retrieval
       items:
-      - name: Analyzers overview
-        href: search-analyzers.md
-      - name: Add a language analyzer
-        href: index-add-language-analyzers.md
-      - name: Add a custom analyzer
-        href: index-add-custom-analyzers.md
-    - name: Filters and facets
+      - name: Design an index for agentic retrieval
+        href: search-agentic-retrieval-how-to-index.md
+      - name: Create a knowledge agent
+        href: search-agentic-retrieval-how-to-create.md
+      - name: Retrieve data using a knowledge agent
+        href: search-agentic-retrieval-how-to-retrieve.md
+      - name: Build a retrieval pipeline
+        href: search-agentic-retrieval-how-to-pipeline.md
+    - name: Vector search
       items:
-      - name: Filters in text queries
+      - name: Create a vector index
+        href: vector-search-how-to-create-index.md
+      - name: Chunk documents
+        href: vector-search-how-to-chunk-documents.md
+      - name: Chunk and vectorize by document layout
+        href: search-how-to-semantic-chunking.md
+      - name: Generate embeddings
+        href: vector-search-how-to-generate-embeddings.md
+      - name: Use integrated vectorization
+        href: search-how-to-integrated-vectorization.md
+      - name: Use embedding models from Azure AI Foundry
+        href: vector-search-integrated-vectorization-ai-studio.md
+      - name: Reduce vector size
+        items:
+        - name: Understand vector quotas and limits
+          href: vector-search-index-size.md
+        - name: Choose an optimization strategy
+          href: vector-search-how-to-configure-compression-storage.md
+        - name: Compress using binary or scalar quantization
+          href: vector-search-how-to-quantization.md
+        - name: Index binary data for vector search
+          href: vector-search-how-to-index-binary-data.md
+        - name: Assign narrow data types
+          href: vector-search-how-to-assign-narrow-data-types.md
+        - name: Eliminate redundant storage
+          href: vector-search-how-to-storage-options.md
+        - name: Truncate dimensions
+          href: vector-search-how-to-truncate-dimensions.md
+      - name: Query vectors
+        href: vector-search-how-to-query.md
+      - name: Use multi-vector fields
+        href: vector-search-multi-vector-fields.md
+      - name: Add a vectorizer for text-to-vector queries
         displayName: query
-        href: search-filters.md
-      - name: Understand collection filters
-        href: search-query-understand-collection-filters.md
-      - name: Troubleshoot collection filters
-        href: search-query-troubleshoot-collection-filters.md
-      - name: Normalize text for filters
-        href: search-normalizers.md
-      - name: Add faceted navigation
-        href: search-faceted-navigation.md
-      - name: Faceted navigation examples
-        href: search-faceted-navigation-examples.md
-    - name: Search results
+        href: vector-search-how-to-configure-vectorizer.md
+      - name: Filter on vector queries
+        displayName: query
+        href: vector-search-filters.md
+    - name: Keyword search
       items:
-      - name: Page, sort, and shape results
-        href: search-pagination-page-layout.md
-      - name: Return a semantic answer
-        href: semantic-answers.md
-    - name: Advanced queries
+      - name: Full text query
+        href: search-query-create.md
+      - name: Typeahead query
+        href: search-add-autocomplete-suggestions.md
+      - name: Query examples (simple syntax)
+        href: search-query-simple-examples.md
+      - name: Add spell check
+        href: speller-how-to-add.md
+      - name: Add synonyms
+        href: search-synonyms.md
+      - name: Add a suggester for typeahead
+        href: index-add-suggesters.md
+      - name: Design a multilingual index
+        href: search-language-support.md
+      - name: Model complex data types
+        href: search-howto-complex-data-types.md
+      - name: Model relational data
+        href: index-sql-relational-data.md
+      - name: Analyzers
+        items:
+        - name: Analyzers overview
+          href: search-analyzers.md
+        - name: Add a language analyzer
+          href: index-add-language-analyzers.md
+        - name: Add a custom analyzer
+          href: index-add-custom-analyzers.md
+      - name: Filters and facets
+        items:
+        - name: Filters in text queries
+          displayName: query
+          href: search-filters.md
+        - name: Understand collection filters
+          href: search-query-understand-collection-filters.md
+        - name: Troubleshoot collection filters
+          href: search-query-troubleshoot-collection-filters.md
+        - name: Normalize text for filters
+          href: search-normalizers.md
+        - name: Add faceted navigation
+          href: search-faceted-navigation.md
+        - name: Faceted navigation examples
+          href: search-faceted-navigation-examples.md
+      - name: Search results
+        items:
+        - name: Page, sort, and shape results
+          href: search-pagination-page-layout.md
+        - name: Return a semantic answer
+          href: semantic-answers.md
+      - name: Advanced queries
+        items:
+        - name: Use full Lucene (examples)
+          href: search-query-lucene-examples.md
+        - name: Partial terms and special characters
+          href: search-query-partial-matching.md
+        - name: Fuzzy search
+          href: search-query-fuzzy.md
+    - name: Hybrid search
+      href: hybrid-search-how-to-query.md
+    - name: Ranking and relevance
       items:
-      - name: Use full Lucene (examples)
-        href: search-query-lucene-examples.md
-      - name: Partial terms and special characters
-        href: search-query-partial-matching.md
-      - name: Fuzzy search
-        href: search-query-fuzzy.md
-  - name: Hybrid search
-    href: hybrid-search-how-to-query.md
-  - name: Ranking and relevance
-    items:
-    - name: Add a scoring profile
-      href: index-add-scoring-profiles.md
-    - name: Configure BM25 ranking
-      href: index-ranking-similarity.md
-    - name: Enable or disable semantic ranker
-      href: semantic-how-to-enable-disable.md
-    - name: Configure semantic ranker
-      href: semantic-how-to-configure.md
-    - name: Add semantic ranking to queries
-      href: semantic-how-to-query-request.md
-    - name: Rewrite queries with semantic ranker
-      href: semantic-how-to-query-rewrite.md
-    - name: Migrate semantic ranking code
-      href: semantic-code-migration.md
-    - name: Enable scoring profiles in semantic ranker
-      href: semantic-how-to-enable-scoring-profiles.md
+      - name: Add a scoring profile
+        href: index-add-scoring-profiles.md
+      - name: Configure BM25 ranking
+        href: index-ranking-similarity.md
+      - name: Enable or disable semantic ranker
+        href: semantic-how-to-enable-disable.md
+      - name: Configure semantic ranker
+        href: semantic-how-to-configure.md
+      - name: Add semantic ranking to queries
+        href: semantic-how-to-query-request.md
+      - name: Rewrite queries with semantic ranker
+        href: semantic-how-to-query-rewrite.md
+      - name: Migrate semantic ranking code
+        href: semantic-code-migration.md
+      - name: Enable scoring profiles in semantic ranker
+        href: semantic-how-to-enable-scoring-profiles.md
   - name: Security
     items:
     - name: Configure network access
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の改善と構造の整理"
}
```

### Explanation
この変更は `articles/search/toc.yml` ファイルに対するマイナーアップデートで、主に目次の内容と構造に関する修正が行われています。以下は具体的な変更点です。

1. **セクション名の変更**: 「Index management」が「Indexing」に変更され、より具体的な表現が使用されています。また「Agentic retrieval」セクションが「Retrieval」に統合され、内容が整理されています。
2. **新しい項目の追加**: インデックス作成やエージェンティックリトリーバルに関するリソースが新たに追加され、ユーザーが必要な情報により簡単にアクセスできるようになっています。特に、エージェンティックリトリーバル関連の具体的な項目（例: 知識エージェントの作成やデータの取得方法）が詳述されています。
3. **項目の並べ替えと整理**: 各トピックが論理的な順序で整理され、同類の情報が一つのセクションに集約されています。これにより、ユーザーは関連する情報を見つけやすくなります。
4. **不必要な項目の削除**: 一部の冗長な項目が削除され、ドキュメントがクリーンで一貫性のある状態に保たれています。

全体として、この変更は目次の可读性を向上させ、ユーザーがAzure AI Searchに関する情報をより効率的に見つけられるように配慮されています。これにより、ドキュメントのユーザビリティが改善され、情報の探索が容易になります。

## articles/search/troubleshoot-shared-private-link-resources.md{#item-0e1867}

<details>
<summary>Diff</summary>
````diff
@@ -10,30 +10,30 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 05/29/2025
+ms.date: 06/04/2025
 ---
 
-# Troubleshoot issues with Shared Private Links in Azure AI Search
+# Troubleshoot issues with shared private links in Azure AI Search
 
 A shared private link allows Azure AI Search to make secure outbound connections over a private endpoint when accessing customer resources in a virtual network. This article can help you resolve errors that might occur.
 
-Creating a shared private link is a search service control plane operation. You can [create a shared private link](search-indexer-howto-access-private.md) using either the Azure portal or a [Management REST API](/rest/api/searchmanagement/shared-private-link-resources/create-or-update). During provisioning, the state of the request is "Updating". After the operation completes successfully, status is "Succeeded". A private endpoint to the resource, along with any DNS zones and mappings, is created. This endpoint is used exclusively by your search service instance and is managed through Azure AI Search.
+Creating a shared private link is a search service control plane operation. You can [create a shared private link](search-indexer-howto-access-private.md) using either the Azure portal or a [Management REST API](/rest/api/searchmanagement/shared-private-link-resources/create-or-update). During provisioning, the state of the request is `Updating`. After the operation completes successfully, status is `Succeeded`. A private endpoint to the resource, along with any DNS zones and mappings, is created. This endpoint is used exclusively by your search service instance and is managed through Azure AI Search.
 
 ![Steps involved in creating shared private link resources ](media\troubleshoot-shared-private-link-resources\shared-private-link-states.png)
 
-Some common errors that occur during the creation phase are listed below.
+The following are common errors that occur during the creation phase.
 
 ## Request validation failures
 
-+ Unsupported SKU: Shared private links are supported on the Basic tier and above. For indexers with skillsets, the minimum tier is Standard 2 (S2).
++ Unsupported SKU: Shared private links are supported on the Basic tier and higher. For indexers with skillsets, the minimum tier is Standard 1 (S1). For more information, see [Shared private link resource limits](search-limits-quotas-capacity.md#shared-private-link-resource-limits).
 
 + Invalid name: Naming rules for a shared private link are:
   
   + Length should be between 1 to 60 characters
   + Alphanumeric characters
   + Names can include underscore `_`, period `.`, and hyphen `-` as long as it's not the first character in the name
 
-+ Invalid group ID: Group IDs are case-sensitive and must be one of the values from the table below:
++ Invalid group ID: Group IDs are case-sensitive and must be one of the following values.
 
   | Azure resource | Group ID | First available API version |
   | --- | --- | --- |
@@ -59,53 +59,53 @@ Some common errors that occur during the creation phase are listed below.
   | Azure Functions (preview) | `Microsoft.Web/sites` | `2020-08-01-Preview` |
   | Azure SQL Managed Instance (preview) | `Microsoft.Sql/managedInstance` | `2020-08-01-Preview` |
 
-  In addition, the specified `groupId` needs to be valid for the specified resource type. For example, `groupId` "blob" is valid for type "Microsoft.Storage/storageAccounts", it can't be used with any other resource type. For a given search management API version, customers can find out the supported `groupId` and resource type details by utilizing the [List supported API](/rest/api/searchmanagement/private-link-resources/list-supported).
+  In addition, the specified `groupId` needs to be valid for the specified resource type. For example, `groupId` "blob" is valid for type `Microsoft.Storage/storageAccounts`, it can't be used with any other resource type. For a given search management API version, customers can find out the supported `groupId` and resource type details by utilizing the [List supported API](/rest/api/searchmanagement/private-link-resources/list-supported).
 
-+ Quota limit enforcement: Search services have quotas imposed on the distinct number of shared private link resources that can be created and the number of various target resource types that are being used (based on `groupId`). These are documented in the [Shared private link resource limits section](search-limits-quotas-capacity.md#shared-private-link-resource-limits) of the Azure AI Search service limits page.
++ Quota limit enforcement: Search services have quotas imposed on the distinct number of shared private link resources that can be created and the number of various target resource types that are being used (based on `groupId`). For more information, see [Shared private link resource limits](search-limits-quotas-capacity.md#shared-private-link-resource-limits).
 
 ## Deployment failures
 
 A search service initiates the request to create a shared private link, but Azure Resource Manager performs the actual work. You can [check the deployment's status](search-indexer-howto-access-private.md#1---create-a-shared-private-link) in the Azure portal or by query, and address any errors that might occur.
 
-Shared private link resources that have failed Azure Resource Manager deployment will show up in [List](/rest/api/searchmanagement/shared-private-link-resources/list-by-service) and [Get](/rest/api/searchmanagement/shared-private-link-resources/get) API calls, but will have a "Provisioning State" of `Failed`. Once the reason of the Azure Resource Manager deployment failure has been ascertained, delete the `Failed` resource and re-create it after applying the appropriate resolution from the following table.
+Shared private link resources that fail Azure Resource Manager deployment show up in [List](/rest/api/searchmanagement/shared-private-link-resources/list-by-service) and [Get](/rest/api/searchmanagement/shared-private-link-resources/get) API calls, but they have a "Provisioning State" of `Failed`. Once the reason of the Azure Resource Manager deployment failure is ascertained, delete the `Failed` resource and re-create it after applying the appropriate resolution from the following table.
 
 | Deployment failure reason | Description | Resolution |
 | ------------------------- | ----------- | ---------- |
-| "LinkedAuthorizationFailed" | The error message states that the client has permission to create the shared private link on the search service, but doesn't have permission to perform action 'privateEndpointConnectionApproval/action' on the linked scope. | Re-check the private link ID in the request to make sure there are no errors or omissions in the URI. If Azure AI Search and the Azure PaaS resource are in different subscriptions, and if you're using REST or a command line interface, make sure that the [active Azure account is for the Azure PaaS resource](search-indexer-howto-access-private.md?tabs=rest-create#1---create-a-shared-private-link). For REST clients, make sure you're not using an expired bearer token, and that the token is valid for the active subscription. |
+| "LinkedAuthorizationFailed" | The error message states that the client has permission to create the shared private link on the search service, but doesn't have permission to perform action 'privateEndpointConnectionApproval/action' on the linked scope. | Recheck the private link ID in the request to make sure there are no errors or omissions in the URI. If Azure AI Search and the Azure PaaS resource are in different subscriptions, and if you're using REST or a command line interface, ensure the [active Azure account is the Azure PaaS resource](search-indexer-howto-access-private.md?tabs=rest-create#1---create-a-shared-private-link). For REST clients, make sure you're not using an expired bearer token, and that the token is valid for the active subscription. |
 | Network resource provider not registered on target resource's subscription | A private endpoint (and associated DNS mappings) is created for the target resource (Storage Account, Azure Cosmos DB, Azure SQL) via the `Microsoft.Network` resource provider (RP). If the subscription that hosts the target resource ("target subscription") isn't registered with `Microsoft.Network` RP, then the Azure Resource Manager deployment can fail. | You need to register this RP in their target subscription. You can [register the resource provider](/azure/azure-resource-manager/management/resource-providers-and-types#register-resource-provider) using the Azure portal, PowerShell, or CLI.|
-| Invalid `groupId` for the target resource | When Azure Cosmos DB accounts are created, you can specify the API type for the database account. While Azure Cosmos DB offers several different API types, Azure AI Search only supports "Sql" as the `groupId` for shared private link resources. When a shared private link of type "Sql" is created for a `privateLinkResourceId` pointing to a non-Sql database account, the Azure Resource Manager deployment will fail because of the `groupId` mismatch. The Azure resource ID of an Azure Cosmos DB account isn't sufficient to determine the API type that is being used. Azure AI Search tries to create the private endpoint, which is then denied by Azure Cosmos DB. | You should ensure that the `privateLinkResourceId` of the specified Azure Cosmos DB resource is for a database account of "Sql" API type |
-| Target resource not found | Existence of the target resource specified in `privateLinkResourceId` is checked only during the commencement of the Azure Resource Manager deployment. If the target resource is no longer available, then the deployment will fail. | You should ensure that the target resource is present in the specified subscription and resource group and isn't moved or deleted. |
+| Invalid `groupId` for the target resource | When Azure Cosmos DB accounts are created, you can specify the API type for the database account. While Azure Cosmos DB offers several different API types, Azure AI Search only supports "Sql" as the `groupId` for shared private link resources. When a shared private link of type "Sql" is created for a `privateLinkResourceId` pointing to a non-Sql database account, the Azure Resource Manager deployment fails because of the `groupId` mismatch. The Azure resource ID of an Azure Cosmos DB account isn't sufficient to determine the API type that is being used. Azure AI Search tries to create the private endpoint, which Azure Cosmos DB then denies. | You should ensure that the `privateLinkResourceId` of the specified Azure Cosmos DB resource is for a database account of "Sql" API type |
+| Target resource not found | Existence of the target resource specified in `privateLinkResourceId` is checked only during the commencement of the Azure Resource Manager deployment. If the target resource is no longer available, then the deployment fails. | You should ensure that the target resource is present in the specified subscription and resource group and isn't moved or deleted. |
 | Transient/other errors | The Azure Resource Manager deployment can fail if there's an infrastructure outage or because of other unexpected reasons. This should be rare and usually indicates a transient state. | Retry creating this resource at a later time. If the problem persists, reach out to Azure Support. |
 
 ## Issues approving the backing private endpoint
 
-A private endpoint is created to the target Azure resource as specified in the shared private link creation request. This is one of the final steps in the asynchronous Azure Resource Manager deployment operation, but Azure AI Search needs to link the private endpoint's private IP address as part of its network configuration. Once this link is done, the `provisioningState` of the shared private link resource will go to a terminal success state `Succeeded`. Customers should only approve or deny(or in general modify the configuration of the backing private endpoint) after the state has transitioned to `Succeeded`. Modifying the private endpoint in any way before this could result in an incomplete deployment operation and can cause the shared private link resource to end up (either immediately, or usually within a few hours) in a `Failed` state.
+A private endpoint is created to the target Azure resource as specified in the shared private link creation request. This is one of the final steps in the asynchronous Azure Resource Manager deployment operation, but Azure AI Search needs to link the private endpoint's private IP address as part of its network configuration. Once this link is done, the `provisioningState` of the shared private link resource goes to a terminal success state `Succeeded`. Customers should only approve or deny(or in general modify the configuration of the backing private endpoint) after the state transitions to `Succeeded`. Modifying the private endpoint in any way before this could result in an incomplete deployment operation and can cause the shared private link resource to end up (either immediately, or usually within a few hours) in a `Failed` state.
 
 ## Search service network connectivity change stalled in an "Updating" state
 
-Shared private links and private endpoints are used when search service **Public Network Access** is **Disabled**. Typically, changing network connectivity should succeed in a few minutes after the request has been accepted. In some circumstances, Azure AI Search may take several hours to complete the connectivity change operation.
+Shared private links and private endpoints are used when search service **Public Network Access** is **Disabled**. Typically, changing network connectivity should succeed in a few minutes after the request is accepted. In some circumstances, Azure AI Search might take several hours to complete the connectivity change operation.
 
   :::image type="content" source="media/troubleshoot-shared-private-link-resources/update-network-access.png" alt-text="Screenshot of changing public network access to disabled." border="true":::
 
-If you observe that the connectivity change operation is taking a significant amount of time, wait for a few hours. Connectivity change operations involve operations such as updating DNS records which may take longer than expected.
+If you observe that the connectivity change operation is taking a significant amount of time, wait for a few hours. Connectivity change operations involve operations such as updating DNS records which might take longer than expected.
 
-If **Public Network Access** is changed, existing shared private links and private endpoints may not work correctly. If existing shared private links and private endpoints stop working during a connectivity change operation, wait a few hours for the operation to complete. If they're still not working, try deleting and recreating them.
+If **Public Network Access** is changed, existing shared private links and private endpoints might not work correctly. If existing shared private links and private endpoints stop working during a connectivity change operation, wait a few hours for the operation to complete. If they're still not working, try deleting and recreating them.
 
 ## Shared private link resource stalled in an "Updating" or "Incomplete" state
 
-Typically, a shared private link resource should go a terminal state (`Succeeded` or `Failed`) in a few minutes after the request has been accepted.
+Typically, a shared private link resource should go a terminal state (`Succeeded` or `Failed`) in a few minutes after the request is accepted.
 
-In rare circumstances, Azure AI Search can fail to correctly mark the state of the shared private link resource to a terminal state (`Succeeded` or `Failed`). This usually occurs due to an unexpected failure. Shared private link resources are automatically transitioned to a `Failed` state if it has been "stuck" in a non-terminal state for more than a few hours.
+In rare circumstances, Azure AI Search can fail to correctly mark the state of the shared private link resource to a terminal state (`Succeeded` or `Failed`). This usually occurs due to an unexpected failure. Shared private link resources are automatically transitioned to a `Failed` state if it's "stuck" in a nonterminal state for more than a few hours.
 
-If you observe that the shared private link resource hasn't transitioned to a terminal state, wait for a few hours to ensure that it becomes `Failed` before you can delete it and re-create it. Alternatively, instead of waiting you can try to create another shared private link resource with a different name (keeping all other parameters the same).
+If the shared private link resource doesn't transition to a terminal state, wait for a few hours to ensure that it becomes `Failed` before you can delete it and re-create it. Alternatively, instead of waiting you can try to create another shared private link resource with a different name (keeping all other parameters the same).
 
 ## Updating a shared private link resource
 
 An existing shared private link resource can be updated using the [Create or Update API](/rest/api/searchmanagement/shared-private-link-resources/create-or-update). Search only allows for narrow updates to the shared private link resource - only the request message can be modified via this API.
 
 + It isn't possible to update any of the "core" properties of an existing shared private link resource (such as `privateLinkResourceId` or `groupId`) and this will always be unsupported. If any other property besides the request message needs to be changed, we advise customers to delete and re-create the shared private link resource.
 
-+ Attempt to update the request message of a shared private link resource is only possible if it has reached the provisioning state of `Succeeded`.
++ Updating the request message of a shared private link resource is only possible if it reaches the provisioning state of `Succeeded`.
 
 ## Deleting a shared private link resource
 
@@ -115,24 +115,24 @@ Customers can delete an existing shared private link resource via the [Delete AP
 
 1. The search service validates that the resource exists and is in a state valid for deletion. If so, it initiates an Azure Resource Manager delete operation to remove the resource.
 
-1. Search queries for the completion of the operation (which usually takes a few minutes). At this point, the shared private link resource would have a provisioning state of "Deleting".
+1. Search queries for the completion of the operation (which usually takes a few minutes). At this point, the shared private link resource would have a provisioning state of `Deleting`.
 
-1. Once the operation completes successfully, the backing private endpoint and any associated DNS mappings are removed. The resource won't show up as part of [List](/rest/api/searchmanagement/shared-private-link-resources/list-by-service) operation and attempting a [Get](/rest/api/searchmanagement/shared-private-link-resources/get) operation on this resource will result in a 404 Not Found.
+1. Once the operation completes successfully, the backing private endpoint and any associated DNS mappings are removed. The resource doesn't show up as part of [List](/rest/api/searchmanagement/shared-private-link-resources/list-by-service) operation and attempting a [Get](/rest/api/searchmanagement/shared-private-link-resources/get) operation on this resource results in a 404 Not Found.
 
 ![Steps involved in deleting shared private link resources ](media\troubleshoot-shared-private-link-resources\shared-private-link-delete-states.png)
 
-Some common errors that occur during the deletion phase are listed below.
+The following are common errors that occur during the deletion phase.
 
 | Failure Type | Description | Resolution |
 | --- | --- | --- |
-| Resource is in non-terminal state | A shared private link resource that's not in a terminal state (`Succeeded` or `Failed`) can't be deleted. It's possible (rare) for a shared private link resource to be stuck in a non-terminal state for up to 8 hours. | Wait until the resource has reached a terminal state and retry the delete request. |
+| Resource is in nonterminal state | A shared private link resource that's not in a terminal state (`Succeeded` or `Failed`) can't be deleted. It's possible (rare) for a shared private link resource to be stuck in a nonterminal state for up to 8 hours. | Wait until the resource reaches a terminal state and retry the delete request. |
 | Delete operation failed with error "Conflict" | The Azure Resource Manager operation to delete a shared private link resource reaches out to the resource provider of the target resource specified in `privateLinkResourceId` ("target RP") before it can remove the private endpoint and DNS mappings. Customers can utilize [Azure resource locks](/azure/azure-resource-manager/management/lock-resources) to prevent any changes to their resources. When Azure Resource Manager reaches out to the target RP, it requires the target RP to modify the state of the target resource (to remove details about the private endpoint from its metadata). When the target resource has a lock configured on it (or its resource group/subscription), the Azure Resource Manager operation fails with a "Conflict" (and appropriate details). The shared private link resource won't be deleted. | Customers should remove the lock on the target resource before retrying the deletion operation. **Note**: This problem can also occur when customers try to delete a search service with shared private link resources that point to "locked" target resources |
-| Delete operation failed | The asynchronous Azure Resource Manager delete operation can fail in rare cases. When this operation fails, querying the state of the asynchronous operation will present customers with an error message and appropriate details. | Retry the operation at a later time, or reach out to Azure Support if the problem persists.
+| Delete operation failed | The asynchronous Azure Resource Manager delete operation can fail in rare cases. When this operation fails, querying the state of the asynchronous operation presents an error message and appropriate details. | Retry the operation at a later time, or reach out to Azure Support if the problem persists.
 | Resource stuck in "Deleting" state | In rare cases, a shared private link resource might be stuck in "Deleting" state for up to 8 hours, likely due to some catastrophic failure on the search RP. | Wait for 8 hours, after which the resource would transition to `Failed` state and then reissue the request.|
 
 ## Next steps
 
 Learn more about shared private link resources and how to use it for secure access to protected content.
 
-+ [Accessing protected content via indexers](search-indexer-howto-access-private.md)
++ [Make outbound connections through a shared private link](search-indexer-howto-access-private.md)
 + [REST API reference](/rest/api/searchmanagement)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "共有プライベートリンクリソースに関するトラブルシューティングガイドの更新"
}
```

### Explanation
この変更は `articles/search/troubleshoot-shared-private-link-resources.md` ファイルに対するマイナーアップデートで、主に文言の修正や内容の整理が行われています。変更内容の概要は以下の通りです。

1. **日付の更新**: `ms.date` の値が「05/29/2025」から「06/04/2025」に変更され、ドキュメントの最新性を反映しています。
2. **見出しの表現改善**: トピックの見出しといくつかの文が改善され、より自然な表現になっています。例えば、「Troubleshoot issues with Shared Private Links in Azure AI Search」が「Troubleshoot issues with shared private links in Azure AI Search」に変更されています。
3. **エラーメッセージの具体化**: エラーの説明や条件がより具体的になり、ユーザーが直面する可能性のある問題を特定しやすくなっています。特に、SKUやgroup IDの制限に関する情報が明確化されています。
4. **コードと引用のフォーマットの改善**: 特定の用語やコードがバッククォートで囲まれ、技術的な正確性や可読性が向上しています。これは、ドキュメントの整合性とプロフェッショナルな印象を保つために重要です。
5. **構造の整理**: エラーや状態に関する説明が明確に整理され、一致したフォーマットで提供されています。

これらの変更により、ユーザーはAzureの共有プライベートリンクリソースに関する問題をより簡単に理解し、解決できるようになります。また、情報の正確性と明快さが向上したことで、ドキュメントがより役立つリソースとなっています。


