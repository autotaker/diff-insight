---
date: '2025-06-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:178e7a4...MicrosoftDocs:8d764d4
summary: 今回のコード変更では、Azure AI Searchに関連するドキュメントのメタデータが更新され、特に`build-2025`というカスタムメタデータが多くのファイルに追加されました。新機能は特にないものの、一貫性や正確性の向上が図られ、文書の明確化が行われました。著者情報や日付の更新、タイトルフォーマットの標準化も行われ、全体として技術情報の可読性とユーザーエクスペリエンスの向上に寄与しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:178e7a4...MicrosoftDocs:8d764d4){target="_blank"}

# ハイライト

今回のコード変更では、Azure AI Searchに関する複数のドキュメントファイルに対し、メタデータの更新が行われています。主要な新機能はありませんが、`build-2025` というカスタムメタデータがほとんどのファイルに追加されています。また、一部の内容や表現の改善が見られ、文書の一貫性と正確性が向上しています。

## 新機能

- メタデータフィールドに新しいカスタムタグ `build-2025` が広範囲に追加され、将来のイベントやプロジェクトに関する情報が強調されています。

## 破壊的変更

- 特になし。

## その他の更新

- メタデータの修正と整理による文書の明確化。
- 各ファイルにおける日付や著者情報の更新。
- タイトルフォーマットの標準化、内容の表現改善による可読性の向上。

# 洞察

このコード変更は、主にAzure AI Searchに関連する文書の情報整合性と視認性を向上させることを目的としています。`build-2025` タグの追加は、2025年に予定されているイベントや計画されているプロジェクトを意識したアップデートであり、最新の情報を迅速かつ整理された形でユーザーに提供することを狙っています。

各ドキュメントファイルに対して著者情報や日付のアップデートが施されており、特に技術ドキュメントの生命線ともいえる正確なタイムスタンプや関連性の強調が強化されています。その結果、ユーザーはAzure AI Search機能を実際的かつ現在進行形で利用しやすくなっています。

内容面では、リソースツールやエージェントリトリーバルに関する説明が改善され、ユーザーが技術的な概念をより深く理解できるよう配慮されています。これにより、利用者はAzure AI Searchを様々なビジネスニーズに応じて適用しやすくなるでしょう。

総体的に見れば、この更新は、Azure AI Searchドキュメントを最新の状態に保つと同時に技術情報の可読性と価値を高めることに貢献しており、ユーザーエクスペリエンスの向上につながっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [index.yml](#item-c67121) | minor update | 検索ドキュメントのメタデータ更新 | modified | 5 | 4 | 9 | 
| [resource-tools.md](#item-0c6ac1) | minor update | リソースツールの内容更新 | modified | 17 | 17 | 34 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | RAGと生成AIのメタデータ更新 | modified | 4 | 4 | 8 | 
| [search-agentic-retrieval-concept.md](#item-797a22) | minor update | エージェントリトリーバルのメタデータと内容更新 | modified | 6 | 5 | 11 | 
| [search-agentic-retrieval-how-to-pipeline.md](#item-1ad1c3) | minor update | エージェントリトリーバルソリューションのメタデータ更新 | modified | 4 | 3 | 7 | 
| [search-document-level-access-overview.md](#item-4bb055) | minor update | ドキュメントレベルアクセス制御のメタデータ更新 | modified | 13 | 11 | 24 | 
| [search-how-to-index-logic-apps-indexers.md](#item-64a12e) | minor update | Azure Logic Appsインデクサーに関するメタデータとリンクの更新 | modified | 6 | 4 | 10 | 
| [search-import-data-portal.md](#item-b804d1) | minor update | Azureポータルにおけるインポートウィザードに関するメタデータの更新 | modified | 4 | 4 | 8 | 
| [search-region-support.md](#item-25b0f1) | minor update | Azure AI Searchのサポート地域に関するメタデータの更新 | modified | 5 | 5 | 10 | 
| [search-security-rbac.md](#item-a5d129) | minor update | Azure AI Searchにおけるロールベースのアクセス制御に関するメタデータの更新 | modified | 6 | 4 | 10 | 
| [whats-new.md](#item-fa71b4) | minor update | Azure AI Searchの新機能に関するメタデータの更新 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/search/index.yml{#item-c67121}

<details>
<summary>Diff</summary>
````diff
@@ -5,14 +5,15 @@ summary: Information retrieval at scale for agentic retrieval, with vector and t
 metadata:
   title: Azure AI Search documentation
   description: Information retrieval at scale for agentic retrieval, with vector and text content in traditional or generative search scenarios.
+  author: HeidiSteen
+  ms.author: heidist
+  ms.date: 05/12/2025
   ms.service: azure-ai-search
+  ms.topic: landing-page
   ms.custom:
     - ignite-2023
     - ignite-2024
-  ms.topic: landing-page
-  author: HeidiSteen
-  ms.author: heidist
-  ms.date: 05/12/2025
+    - build-2025
 # linkListType: architecture | concept | deploy | download | get-started | how-to-guide | learn | overview | quickstart | reference | tutorial | video | whats-new
 
 landingContent:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索ドキュメントのメタデータ更新"
}
```

### Explanation
この変更では、`articles/search/index.yml` ファイルに対して、いくつかのメタデータの追加と修正が行われました。具体的には、新たな著者情報や日付、トピックが追加され、また一部の要素が削除されました。この変更により、検索ドキュメントがより最新の情報を反映し、関連イベント (`ignite-2023` と `ignite-2024`) に加えて新たに `build-2025` 色が付けられました。全体として、9の変更が実施され、5行が追加され、4行が削除されました。これにより、Azure AI Searchドキュメントの内容が強化されています。

## articles/search/resource-tools.md{#item-0c6ac1}

<details>
<summary>Diff</summary>
````diff
@@ -1,34 +1,34 @@
 ---
-title: Productivity tools
+title: Productivity Tools
 titleSuffix: Azure AI Search
 description: Use existing code samples or build your own tools for working with a search index in Azure AI Search.
 
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.date: 02/25/2025
+ms.date: 06/02/2025
 ---
 
-# Productivity tools and accelerators - Azure AI Search
+# Productivity tools and accelerators for Azure AI Search
 
-Productivity tools are built by engineers at Microsoft, but aren't part of the Azure AI Search service and aren't under Service Level Agreement (SLA). These tools are provided as source code that you can download, modify, and build to create an app that helps you develop or maintain a search solution.
+Microsoft engineers build productivity tools that aren't part of the Azure AI Search service and aren't covered by service-level agreements (SLAs). You can download, modify, and build these tools to create an app that helps you develop or maintain a search solution.
 
 ## Tools
 
-| Tool name | Description | Source code |
-|-----------|------------ |-------------|
-| [Azure AI Search Lab](https://github.com/jelledruyts/azure-ai-search-lab) | Learning and experimentation lab to try out AI-enabled search scenarios in Azure. It provides a web application front-end which uses Azure AI Search and Azure OpenAI to execute searches with a variety of options - ranging from simple keyword search, to semantic ranking, vector and hybrid search, and using generative AI to answer search queries. | [https://github.com/jelledruyts/azure-ai-search-lab](https://github.com/jelledruyts/azure-ai-search-lab)  |
-| [Back up and Restore (C#)](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore) | Download the retrievable fields of an index to your local device and then upload the index and its content to a new search service. | [https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore) |
-| [Back up and Restore (Python)](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) | Download the retrievable fields of an index to your local device and then upload the index and its content to a new search service. | [https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) |
-| [Performance testing solution](https://github.com/Azure-Samples/azure-search-performance-testing/blob/main/README.md) | This solution helps you load test Azure AI Search. It uses Apache JMeter as an open source load and performance testing tool and Terraform to dynamically provision and destroy the required infrastructure on Azure. | [https://github.com/Azure-Samples/azure-search-performance-testing](https://github.com/Azure-Samples/azure-search-performance-testing) |
-| [Visual Studio Code extension](https://github.com/microsoft/vscode-azurecognitivesearch) | Although the extension is no longer available in the Visual Studio Code Marketplace, the code is open source. You can clone and modify the tool for your own use. | [https://github.com/microsoft/vscode-azurecognitivesearch](https://github.com/microsoft/vscode-azurecognitivesearch) |
+| Tool name | Description |
+|--|--|
+| [Azure AI Search Lab](https://github.com/jelledruyts/azure-ai-search-lab) | Learning and experimentation lab to try out AI-enabled search scenarios in Azure. It provides a web application front end that uses Azure AI Search and Azure OpenAI to execute searches with various options. These options range from simple keyword search to semantic ranking, vector and hybrid search, and using generative AI to answer search queries. |
+| [Back up and restore (C#)](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore) | Download the retrievable fields of an index to your local device and then upload the index and its content to a new search service. |
+| [Back up and restore (Python)](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/utilities/index-backup-restore) | Download the retrievable fields of an index to your local device and then upload the index and its content to a new search service. |
+| [Performance testing solution](https://github.com/Azure-Samples/azure-search-performance-testing/blob/main/README.md) | This solution helps you load test Azure AI Search. It uses Apache JMeter as an open source load and performance testing tool and Terraform to dynamically provision and destroy the required infrastructure on Azure. |
+| [Visual Studio Code extension](https://github.com/microsoft/vscode-azurecognitivesearch) | Although the extension is no longer available on the Visual Studio Code Marketplace, the code is open source. You can clone and modify the tool for your own use. |
 
 ## Accelerators
 
-| Accelerator | Description | Source code |
-|-----------|------------ |-------------|
-| [Build your own copilot Solution Accelerator](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator) | Code and docs to build a copilot for specific use cases.| [Client advisor](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/tree/main) <br>[Generic document generator](https://github.com/microsoft/Generic-Build-your-own-copilot-Solution-Accelerator) <br>[Research assistant](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/tree/main) |
-| [Chat with your data solution accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator/blob/main/README.md) |  Code and docs to create interactive search solution in production environments.  | [https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) |
-| [Document knowledge mining solution accelerator](https://github.com/microsoft/Document-Knowledge-Mining-Solution-Accelerator/blob/main/README.md) |  Code and docs built on Azure OpenAI in Azure AI Foundry Models and Azure AI Document Intelligence to process and extract summaries, entities, and metadata from unstructured, multimodal documents and enable searching and chatting over this data.  | [https://github.com/microsoft/Document-Knowledge-Mining-Solution-Accelerator](https://github.com/microsoft/Document-Knowledge-Mining-Solution-Accelerator) |
-| [Knowledge Mining accelerator](https://github.com/Azure-Samples/azure-search-knowledge-mining/blob/main/README.md) | Code and docs to jump start a knowledge store using your data. | [https://github.com/Azure-Samples/azure-search-knowledge-mining](https://github.com/Azure-Samples/azure-search-knowledge-mining) |
+| Accelerator | Description |
+|--|--|
+| [Build your own copilot solution accelerator](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator) | Code and docs to build a copilot for specific use cases. |
+| [Chat with your data solution accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator/blob/main/README.md) | Code and docs to create interactive search solution in production environments. |
+| [Document knowledge mining solution accelerator](https://github.com/microsoft/Document-Knowledge-Mining-Solution-Accelerator/blob/main/README.md) | Code and docs built on Azure OpenAI in Azure AI Foundry Models and Azure AI Document Intelligence. It processes and extracts summaries, entities, and metadata from unstructured, multimodal documents to enable searching and chatting over this data. |
+| [Knowledge mining accelerator](https://github.com/Azure-Samples/azure-search-knowledge-mining/blob/main/README.md) | Code and docs to jump start a knowledge store using your data. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースツールの内容更新"
}
```

### Explanation
この変更では、`articles/search/resource-tools.md` ファイルにおいて、17行の追加と17行の削除が行われ、合計で34の変更が実施されました。主に、ツールのタイトル、日付、文章の表現が更新され、より一貫性と正確性が向上しました。特に、タイトルフォーマットの標準化や、コンテンツの説明がクリアになっており、可読性が向上しています。また、各ツールの説明部分も改訂されており、ユーザーが理解しやすいように整理されています。全体として、Azure AI Searchに関連するリソースツールの情報が明確化され、さらに使いやすい内容となりました。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -2,16 +2,16 @@
 title: RAG and generative AI
 titleSuffix: Azure AI Search
 description: Learn how generative AI and retrieval augmented generation (RAG) patterns are used in Azure AI Search solutions.
-
-manager: nitinme
 author: HeidiSteen
 ms.author: heidist
+manager: nitinme
+ms.date: 04/15/2025
 ms.service: azure-ai-search
+ms.topic: conceptual
 ms.custom:
   - ignite-2023
   - ignite-2024
-ms.topic: conceptual
-ms.date: 04/15/2025
+  - build-2025
 ---
 
 # Retrieval Augmented Generation (RAG) in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGと生成AIのメタデータ更新"
}
```

### Explanation
この変更では、`articles/search/retrieval-augmented-generation-overview.md` ファイルにおいて、いくつかのメタデータの更新が行われました。具体的には、著者情報や日付、トピックが改訂され、全体的に情報が整理されました。特に、日付が `04/15/2025` に設定され、また、トピックカテゴリとして「概念」が強調されるような修正が行われました。さらに、カスタムメタデータに `build-2025` が加えられたことで、最新のイベント情報が反映されています。これにより、Azure AI Search に関連するRAGと生成AIの情報がより明確に伝わる内容へと改善されています。

## articles/search/search-agentic-retrieval-concept.md{#item-797a22}

<details>
<summary>Diff</summary>
````diff
@@ -2,14 +2,15 @@
 title: Agentic Retrieval
 titleSuffix: Azure AI Search
 description: Learn about agentic retrieval concepts, architecture, and use cases.
-
-manager: nitinme
 author: HeidiSteen
 ms.author: heidist
+manager: nitinme
+ms.date: 05/19/2025
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.custom: references_regions
-ms.date: 05/19/2025
+ms.custom:
+  - references_regions
+  - build-2025
 ---
 
 # Agentic retrieval in Azure AI Search
@@ -185,4 +186,4 @@ Token Usage: Token usage in query planning and ranking involves AOAI input token
 
 •Roadmap: Potential features include Multiple Index Search, Iterative Search, Filtered Search, Query Planning Customization, Federation, Answer Generation, and Authority Checking.
 
-•Features under each model: Comparison of features under traditional search model: BYOM Query planning and Reranking are listed, with a section for answers left blank -->
\ No newline at end of file
+•Features under each model: Comparison of features under traditional search model: BYOM Query planning and Reranking are listed, with a section for answers left blank -->
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルのメタデータと内容更新"
}
```

### Explanation
この変更では、`articles/search/search-agentic-retrieval-concept.md` ファイルにおいて、いくつかのメタデータと内容の更新が行われました。具体的には、著者情報や日付、カスタムメタデータが改訂され、特に `ms.date` が `05/19/2025` に設定されています。また、カスタムメタデータに新たに `build-2025` が追加され、最新のイベント情報が反映されています。内容では、エージェントリトリーバルに関連する概念、アーキテクチャ、および使用例に関する説明がさらに明確化され、特定の機能や計画の比較が追加されています。この全体的な改訂により、Azure AI Searchにおけるエージェントリトリーバルの理解が深まるよう改善されています。

## articles/search/search-agentic-retrieval-how-to-pipeline.md{#item-1ad1c3}

<details>
<summary>Diff</summary>
````diff
@@ -2,13 +2,14 @@
 title: Build an agentic retrieval solution
 titleSuffix: Azure AI Search
 description: Learn how to design and build a custom agentic retrieval solution where Azure AI Search handles data retrieval for your custom agents.
-
-manager: nitinme
 author: HeidiSteen
 ms.author: heidist
+manager: nitinme
+ms.date: 05/21/2025
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 05/21/2025
+ms.custom:
+  - build-2025
 ---
 
 # Build an agent-to-agent retrieval solution using Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルソリューションのメタデータ更新"
}
```

### Explanation
この変更では、`articles/search/search-agentic-retrieval-how-to-pipeline.md` ファイルにおいて、いくつかのメタデータの更新が行われました。具体的には、著者情報や日付が改訂され、`ms.date` が `05/21/2025` に設定されています。また、新たにカスタムメタデータとして `build-2025` が追加され、現在のプロジェクトやイベントに関連した情報が強調されています。この更新により、Azure AI Searchを使用したエージェントリトリーバルソリューションの設計と構築方法に関するガイドがより明確に示されるようになり、利用者に対する情報提供が強化されています。

## articles/search/search-document-level-access-overview.md{#item-4bb055}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +1,15 @@
----  
-title: Document-level access control    
-titleSuffix: Azure AI Search    
-description: Conceptual overview of document-level permissions in Azure AI Search.    
-ms.service: azure-ai-search    
-ms.topic: conceptual    
-ms.date: 05/10/2025    
-author: gmndrg    
-ms.author: gimondra    
----  
+---
+title: Document-level access control
+titleSuffix: Azure AI Search
+description: Conceptual overview of document-level permissions in Azure AI Search.
+author: gmndrg
+ms.author: gimondra
+ms.date: 05/10/2025
+ms.service: azure-ai-search
+ms.topic: conceptual
+ms.custom:
+  - build-2025
+---
   
 # Document-level access control in Azure AI Search  
   
@@ -62,4 +64,4 @@ To help you dive deeper into document-level access control in Azure AI Search, h
 
 ## Next steps  
   
-- [Tutorial: Index ADLS Gen2 permissions metadata](tutorial-adls-gen2-indexer-acls.md)  
\ No newline at end of file
+- [Tutorial: Index ADLS Gen2 permissions metadata](tutorial-adls-gen2-indexer-acls.md)  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレベルアクセス制御のメタデータ更新"
}
```

### Explanation
この変更では、`articles/search/search-document-level-access-overview.md` ファイルにおいて、ドキュメントレベルアクセス制御に関するメタデータが更新されました。具体的には、メタデータの形式が整理され、`ms.custom` フィールドに `build-2025` が追加されています。この更新により、Azure AI Searchにおけるドキュメントレベルのアクセス許可に関する概念的な概要がより明確に提示され、情報構造が強化されています。また、次のステップとして提供されるチュートリアルへのリンクも整備され、利用者がさらに深く学び進めるための道筋が示されています。この改訂は、内容をより整理し、よりアクセスしやすくすることを目的としています。

## articles/search/search-how-to-index-logic-apps-indexers.md{#item-64a12e}

<details>
<summary>Diff</summary>
````diff
@@ -2,13 +2,15 @@
 title: Connect to Azure Logic Apps
 titleSuffix: Azure AI Search
 description: Use an Azure Logic Apps workflow for indexer-based indexing in Azure AI Search.
-manager: nitinme
 author: HeidiSteen
 ms.author: heidist
+manager: nitinme
+ms.date: 05/19/2025
 ms.service: azure-ai-search
-ms.custom: references_regions
 ms.topic: how-to
-ms.date: 05/19/2025
+ms.custom:
+  - references_regions
+  - build-2025
 ---
 
 # Use an Azure Logic Apps workflow for indexer-based indexing in Azure AI Search
@@ -162,4 +164,4 @@ The wizard creates templates and workflows when you specify a Logic Apps indexer
 
 + [Connect to Azure AI services from workflows in Azure Logic Apps](/azure/logic-apps/connectors/azure-ai)
 
-+ [Manage logic apps](/azure/logic-apps/manage-logic-apps-with-azure-portal)
\ No newline at end of file
++ [Manage logic apps](/azure/logic-apps/manage-logic-apps-with-azure-portal)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Logic Appsインデクサーに関するメタデータとリンクの更新"
}
```

### Explanation
この変更では、`articles/search/search-how-to-index-logic-apps-indexers.md` ファイルにおいて、Azure Logic Appsとインデクサーに関連するメタデータが更新されました。特に、`ms.date` と `ms.custom` フィールドに新たに `build-2025` が追加され、関連性が強調されています。これにより、ドキュメントが最新のプロジェクトやリソースに関連付けられ、情報が整理された形で提供されます。

さらに、Azure Logic Appsワークフローを使用してAzure AI Searchでインデクサーベースのインデクシングを行う方法に関するステップが明確に示され、読者が効率的に関連情報にアクセスできるようになっています。最後に、他の関連リンクも整備され、利用者がAzure Logic Appsの管理を行うための指針が提供されています。これにより、ドキュメントの整合性と利用価値がより一層向上しています。

## articles/search/search-import-data-portal.md{#item-b804d1}

<details>
<summary>Diff</summary>
````diff
@@ -3,14 +3,14 @@ title: Import Wizards in the Azure Portal
 titleSuffix: Azure AI Search
 description: Learn about the import wizards in the Azure portal used to create and load an index, and optionally invoke applied AI for vectorization, natural language processing, language translation, OCR, and image analysis.
 author: HeidiSteen
-manager: nitinme
 ms.author: heidist
+manager: nitinme
+ms.date: 05/12/2025
 ms.service: azure-ai-search
+ms.topic: concept-article
 ms.custom:
   - ignite-2024
-ms.topic: concept-article
-ms.date: 05/12/2025
-customer intent: As a developer, I want to use wizards for index creation so that I can query the content quickly.
+  - build-2025
 ---
 
 # Import data wizards in the Azure portal
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureポータルにおけるインポートウィザードに関するメタデータの更新"
}
```

### Explanation
この変更では、`articles/search/search-import-data-portal.md` ファイルにおいて、Azureポータルにおけるインポートウィザードに関するメタデータが更新されました。特に、`ms.date` と `ms.custom` フィールドが整理され、`build-2025` の追加により、将来のプロジェクトを意識した情報提供が行われています。また、`customer intent` フィールドが削除され、ドキュメントの焦点がより明確になっています。

この更新は、Azureポータル内でインデックスを作成し、AIを活用した様々な処理（ベクトル化、自然言語処理、言語翻訳、OCR、画像分析など）を行うためのインポートウィザードに関する説明をより整理し、最新の情報を提供することを目的としています。全体として、ドキュメントの整合性が向上し、利用者が必要な情報に迅速にアクセスできるようになっています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -2,15 +2,15 @@
 title: Supported Regions
 titleSuffix: Azure AI Search
 description: Shows supported regions and feature availability across regions for Azure AI Search.
-
-manager: nitinme
 author: haileytap
 ms.author: haileytapia
+manager: nitinme
+ms.date: 05/29/2025
 ms.service: azure-ai-search
 ms.topic: conceptual
-ms.custom: references_regions
-ms.date: 05/29/2025
-
+ms.custom:
+  - references_regions
+  - build-2025
 ---
 
 # Azure AI Search regions list
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのサポート地域に関するメタデータの更新"
}
```

### Explanation
この変更では、`articles/search/search-region-support.md` ファイルにおいて、Azure AI Searchがサポートする地域とその機能の可用性に関するメタデータが更新されています。具体的には、`ms.date` 及び `ms.custom` フィールドが整理され、新たに `build-2025` が追加されました。これにより、将来のプロジェクトとの関連性が強調されており、情報の整合性が向上しています。

また、文書の内容はAzure AI Searchが利用可能な地域のリストを示すもので、利用者がどの地域でどの機能が利用できるかを理解するための情報を提供しています。更新後のドキュメントは、読者が最新の情報に容易にアクセスできるよう整理されており、Azure AI Searchの機能をより効率的に活用するための助けとなることを目的としています。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -2,14 +2,16 @@
 title: Connect using Azure roles
 titleSuffix: Azure AI Search
 description: Use Azure role-based access control for granular permissions on service administration and content tasks.
-
-manager: nitinme
 author: HeidiSteen
 ms.author: heidist
+manager: nitinme
+ms.date: 03/31/2025
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/31/2025
-ms.custom: subject-rbac-steps, devx-track-azurepowershell
+ms.custom:
+  - subject-rbac-steps
+  - devx-track-azurepowershell
+  - build-2025
 ---
 
 # Connect to Azure AI Search using roles
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおけるロールベースのアクセス制御に関するメタデータの更新"
}
```

### Explanation
この変更では、`articles/search/search-security-rbac.md` ファイルにおいて、Azure AI Searchに接続するためのロールベースのアクセス制御に関するメタデータが更新されました。特に、`ms.date` と `ms.custom` フィールドが整理され、`build-2025` が新たに追加されました。これにより、ドキュメントが今後のプロジェクトや展開に関連付けられ、より明確な情報提供が行われています。

この文書は、サービス管理やコンテンツタスクに対する詳細な権限を設定するためのAzureのロールベースのアクセス制御を利用する方法を説明しています。更新された内容により、利用者は最新の情報に基づいて、Azure AI Searchを使用した際のアクセス管理をより理解しやすくなります。全体として、ドキュメントの整合性と情報の有用性が向上しています。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -1,16 +1,16 @@
 ---
 title: What's new in Azure AI Search
 description: Announcements of new and enhanced features, including a service rename of Azure Cognitive Search to Azure AI Search.
-
-manager: nitinme
 author: HeidiSteen
 ms.author: heidist
+manager: nitinme
+ms.date: 05/15/2025
 ms.service: azure-ai-search
 ms.topic: overview
-ms.date: 05/15/2025
 ms.custom:
   - references_regions
   - ignite-2024
+  - build-2025
 ---
 
 # What's new in Azure AI Search
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchの新機能に関するメタデータの更新"
}
```

### Explanation
この変更では、`articles/search/whats-new.md` ファイルにおいて、Azure AI Searchの新機能に関するメタデータが更新されました。具体的には、`ms.date` フィールドの整理と、`ms.custom` フィールドに `build-2025` というエントリが追加されました。

この文書は、Azure Cognitive SearchからAzure AI Searchへのサービス名の変更を含む、新機能や強化された機能に関する発表を記載しています。更新された内容は、利用者に最新の情報を提供し、今後の展開についての理解を促進させることを目的としています。全体として、文書はAzure AI Searchに関する情報の整合性と明確さを向上させています。


