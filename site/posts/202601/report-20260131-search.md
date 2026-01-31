---
date: '2026-01-31'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d1b059c...MicrosoftDocs:3e5f42f
summary: 今回のコードの変更は、Azure AI Searchおよび関連サービスに関する「How-To」ガイドの更新を通じて、ユーザーが情報をより簡単に理解・活用できるようにすることを目的としています。主な変更点として、新たに「Usage
  support」セクションが追加され、Azureポータルや各種SDKのサポート状況が明確になりました。また、ドキュメント内のリンクや用語が更新され、過去のリンクに依存するリソースの修正が必要になる可能性があります。さらに、SQL
  Serverインデクサーの設定やファイアウォール設定手順が整理され、セキュリティ面でも重要な改善が加えられています。全体として、この更新はユーザーエクスペリエンスの向上を図り、Azure
  AI Searchの利用を促進することを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d1b059c...MicrosoftDocs:3e5f42f){target="_blank"}

<format>
# ハイライト
今回のコードの変更は、ドキュメントにおけるさまざまな「How-To」ガイドの更新を中心に、情報の明確化やリンクの修正を行うことで、ユーザーがより簡易にAzure AI Searchおよび関連サービスを活用できるようにするものです。特に新しい「Usage support」セクションの追加やリンクの更新が多く見られます。

## 新機能
- AzureポータルやMicrosoft Foundryポータル、および各種SDKのサポート状況が一目でわかる「Usage support」セクションの追加。
- 各セクションの内容をより明確にするためにリンクの更新。

## 互換性の変更
- 特に記録された破壊的な変更はありませんが、ドキュメントのリンクや用語が更新され、過去のリンクに依存するスクリプトやブックマークは修正が必要になる可能性があります。

## その他の更新
- SQL Serverインデクサーの設定やSQL Azure仮想マシンへのアクセス制限条件が明示化され、ファイアウォール設定手順が整理されました。
- Foundry IQ、RAG、そしてVector searchに関連するビデオリンクや技術文書の表記や名称が正規化されました。

# インサイト
この更新は、ユーザーがAzure AI Searchの機能をよりスムーズに活用できるようにするためのものです。特に「Usage support」セクションの追加により、どのプラットフォームがサポートされているのかが明確になりました。これにより、異なる開発環境を使用している開発者が適切な情報を迅速に選択できるようになり、開発の効率が向上します。

またリンクの更新や用語の正確化は、多くのユーザーが混乱することなく適切なリソースにアクセスできるように意図されています。特に「Foundry IQ」のような新技術や機能が頻出する場合、ドキュメント内でのリンクが不整合だとユーザーにとっての導入ハードルが高まります。今回の更新ではそのようなリスクを削減し、ユーザーエクスペリエンスを向上させる狙いが見られます。

さらに、SQLインデクサーの設定や接続方法が明示化されたことはセキュリティとアクセス管理の観点からも重要です。これにより、ユーザーはより安全かつ効率的にAzure AI Searchの構成を行うことができるでしょう。特に、実装ガイドや技術要件が明記されているため、開発者は自分の環境に合わせた最適な方法でAzureサービスに接続しやすくなります。

全体的に、このドキュメントの更新作業は、ユーザーにとっての利便性を向上させることを強調しており、これによりAzure AI Searchの採用と利用がさらに促進されることが期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-overview.md](#item-d1f354) | minor update | エージェントリトリーバルの概要に関する情報の更新 | modified | 1 | 1 | 2 | 
| [agentic-knowledge-source-how-to-blob-csharp.md](#item-b5f755) | minor update | エージェント知識ソースの使用方法の更新 | modified | 7 | 1 | 8 | 
| [agentic-knowledge-source-how-to-blob-python.md](#item-029d03) | minor update | エージェント知識ソースのPythonによる使用方法の更新 | modified | 7 | 1 | 8 | 
| [agentic-knowledge-source-how-to-blob-rest.md](#item-b5ce57) | minor update | エージェント知識ソースのRESTによる使用方法の更新 | modified | 7 | 1 | 8 | 
| [agentic-knowledge-source-how-to-onelake-csharp.md](#item-d6611c) | minor update | OneLake 知識ソースのC#による使用方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-onelake-python.md](#item-c7d61d) | minor update | OneLake 知識ソースのPythonによる使用方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-onelake-rest.md](#item-876f49) | minor update | OneLake 知識ソースのREST APIによる使用方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-search-index-csharp.md](#item-d3510c) | minor update | C#によるエージェント情報検索インデックスの使用方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-search-index-python.md](#item-58056f) | minor update | Pythonによるエージェント情報検索インデックスの使用方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-search-index-rest.md](#item-e95367) | minor update | REST APIによるエージェント情報検索インデックスの使用方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md](#item-2eb305) | minor update | C#によるSharePointインデックスのエージェント情報共有方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-python.md](#item-923abb) | minor update | PythonによるSharePointインデックスのエージェント情報共有方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-rest.md](#item-e26ea0) | minor update | REST APIによるSharePointインデックスのエージェント情報共有方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-csharp.md](#item-f8bed1) | minor update | C#によるリモートSharePointインデックスのエージェント情報共有方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-python.md](#item-822712) | minor update | PythonによるリモートSharePointインデックスのエージェント情報共有方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-sharepoint-remote-rest.md](#item-5514b1) | minor update | RESTを利用したリモートSharePointインデックスのエージェント情報共有方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-web-csharp.md](#item-401063) | minor update | C#によるWeb知識源のエージェント情報共有方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-web-python.md](#item-72b59c) | minor update | PythonによるWeb知識源のエージェント情報共有方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-knowledge-source-how-to-web-rest.md](#item-649608) | minor update | RESTを使用したWeb知識源のエージェント情報共有方法の更新 | modified | 6 | 0 | 6 | 
| [agentic-retrieval-how-to-create-knowledge-base-csharp.md](#item-4469a2) | minor update | C#による知識ベースの作成方法に関する情報の更新 | modified | 7 | 1 | 8 | 
| [agentic-retrieval-how-to-create-knowledge-base-python.md](#item-4e498f) | minor update | Pythonによる知識ベースの作成方法に関する情報の更新 | modified | 7 | 1 | 8 | 
| [agentic-retrieval-how-to-create-knowledge-base-rest.md](#item-37851c) | minor update | RESTによる知識ベースの作成方法に関する情報の更新 | modified | 7 | 1 | 8 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | RAGに関するビデオリンクの表現の修正 | modified | 2 | 2 | 4 | 
| [search-how-to-index-sql-server.md](#item-d7fb35) | minor update | SQL Serverインデクサー作成手順の更新 | modified | 2 | 4 | 6 | 
| [search-import-data-portal.md](#item-b804d1) | minor update | データインポート ポータルに関する更新 | modified | 38 | 15 | 53 | 
| [search-indexer-howto-access-ip-restricted.md](#item-aec22f) | minor update | IP制限されたサービスへのアクセス手順の更新 | modified | 3 | 24 | 27 | 
| [search-try-for-free.md](#item-36e28d) | minor update | Foundry IQのリンクを更新 | modified | 1 | 1 | 2 | 
| [service-configure-firewall.md](#item-75be3f) | minor update | ファイアウォール設定手順の改善 | modified | 18 | 15 | 33 | 
| [vector-search-overview.md](#item-56e5fa) | minor update | Foundry Agent Serviceのリンクを更新 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-fa71b4) | minor update | Foundry IQのリンクを更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/agentic-retrieval-overview.md{#item-d1f354}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ Programmatically, agentic retrieval is supported through a new [Knowledge Base o
 
 ## Why use agentic retrieval
 
-There are two use cases for agentic retrieval. First, it's the basis of the [Foundry IQ experience](/azure/ai-foundry/agents/how-to/tools/knowledge-retrieval) in the Microsoft Foundry (new) portal. It provides the knowledge layer for agent solutions in Microsoft Foundry. Second, it's the basis for custom agentic solutions that you create using the Azure AI Search APIs.
+There are two use cases for agentic retrieval. First, it's the basis of the [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) experience in the Microsoft Foundry (new) portal. It provides the knowledge layer for agent solutions in Microsoft Foundry. Second, it's the basis for custom agentic solutions that you create using the Azure AI Search APIs.
 
 You should use agentic retrieval when you want to provide agents and apps with the most relevant content for answering harder questions, leveraging chat context and your proprietary content.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルの概要に関する情報の更新"
}
```

### Explanation
この変更は、`agentic-retrieval-overview.md`ファイルにおけるテキストの修正を含んでいます。具体的には、エージェントリトリーバルのユースケースに関する説明が更新されました。元の文では「Foundry IQ experience」とされていた部分が「Foundry IQ」に修正され、リンクも適切に更新されています。この変更は内容の明確さを高め、正確なリファレンスを提供するためのものです。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-csharp.md{#item-b5f755}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,13 @@ Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-s
 + An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
 
 > [!NOTE]
-> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](/azure/search/search-indexer-access-control-lists-and-role-based-access) or [Blob RBAC scopes](/azure/search/search-blob-indexer-role-based-access).
+> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](../../search-indexer-access-control-lists-and-role-based-access.md) or [Blob RBAC scopes](../../search-blob-indexer-role-based-access.md).
+
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースの使用方法の更新"
}
```

### Explanation
この変更では、`agentic-knowledge-source-how-to-blob-csharp.md`ファイルの内容が更新され、特にAzure AI Searchにおける知識ソースに関する情報が強化されました。以前のリンクが相対パスに変更され、関連情報へのアクセスをより簡潔にしています。また、新たに「Usage support」セクションが追加され、さまざまなプラットフォーム（Azureポータル、Microsoft Foundryポータル、複数のSDKおよびREST API）のサポート状況が表形式で示されています。これにより、ユーザーは必要なリソースを迅速に見つけやすくなっています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-python.md{#item-029d03}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,13 @@ Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-s
 + An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
 
 > [!NOTE]
-> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](/azure/search/search-indexer-access-control-lists-and-role-based-access) or [Blob RBAC scopes](/azure/search/search-blob-indexer-role-based-access).
+> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](../../search-indexer-access-control-lists-and-role-based-access.md) or [Blob RBAC scopes](../../search-blob-indexer-role-based-access.md).
+
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースのPythonによる使用方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-blob-python.md`ファイルにおいて、一部のテキストが更新され、Azure AI Searchに関連する知識ソースの使用に関する情報が強化されました。具体的には、権限メタデータに関するリンクが相対パスに置き換えられ、ドキュメントの可視性を向上させています。また、「Usage support」セクションが新たに追加され、さまざまなプラットフォームのサポート状況が表形式で記載されました。これにより、ユーザーはAzureポータル、Microsoft Foundryポータル、および各種SDKとREST APIの各サポートを一目で確認できるようになっています。この変更は、ユーザーにとっての利便性を向上させることを目的としています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-blob-rest.md{#item-b5ce57}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,13 @@ Unlike a [search index knowledge source](../../agentic-knowledge-source-how-to-s
 + An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
 
 > [!NOTE]
-> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](/azure/search/search-indexer-access-control-lists-and-role-based-access) or [Blob RBAC scopes](/azure/search/search-blob-indexer-role-based-access).
+> If user access is specified at the document (blob) level in Azure Storage, a knowledge source can carry permission metadata forward to indexed content in Azure AI Search. For more information, see [ADLS Gen2 permission metadata](../../search-indexer-access-control-lists-and-role-based-access.md) or [Blob RBAC scopes](../../search-blob-indexer-role-based-access.md).
+
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースのRESTによる使用方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-blob-rest.md`ファイルにおける内容の更新を示しています。主な変更点として、Azure AI Searchに関連する知識ソースの情報が強化され、特に権限メタデータについてのリンクが相対パスに修正され、より分かりやすく表示されるようになりました。また、新しい「Usage support」セクションが追加され、Azureポータル、Microsoft Foundryポータル、さまざまなSDK（.NET、Python、Java、JavaScript）およびREST APIのサポート状況が一覧表形式で示されています。これにより、ユーザーは各プラットフォームでのサポート情報を簡単に確認できるようになり、実装の参考にしやすくなっています。変更は全体として、ドキュメントの利便性を向上させることを目指しています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-csharp.md{#item-d6611c}

<details>
<summary>Diff</summary>
````diff
@@ -20,6 +20,12 @@ When you create a OneLake knowledge source, you specify an external data source,
 
 The generated indexer conforms to the *OneLake indexer*, whose prerequisites, supported tasks, supported document formats, supported shortcuts, and limitations also apply to OneLake knowledge sources. For more information, see the [OneLake indexer documentation](../../search-how-to-index-onelake-files.md).
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLake 知識ソースのC#による使用方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-onelake-csharp.md`ファイルに対して行われたもので、OneLake知識ソースの使用に関する情報が更新されました。主な変更点として、「Usage support」セクションが新たに追加され、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）およびREST APIのサポート状況が表形式で示されています。この情報により、ユーザーは各プラットフォームでのサポートの有無を簡単に確認できるようになっています。また、必要な前提条件に関する記述が補足され、Azure AI Searchにおけるエージェントリトリーバルの提供地域や、セマンティックランカーの有効化についても言及されています。全体として、この変更はユーザーにとっての利便性を向上させることを目的としています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-python.md{#item-c7d61d}

<details>
<summary>Diff</summary>
````diff
@@ -20,6 +20,12 @@ When you create a OneLake knowledge source, you specify an external data source,
 
 The generated indexer conforms to the *OneLake indexer*, whose prerequisites, supported tasks, supported document formats, supported shortcuts, and limitations also apply to OneLake knowledge sources. For more information, see the [OneLake indexer documentation](../../search-how-to-index-onelake-files.md).
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLake 知識ソースのPythonによる使用方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-onelake-python.md`ファイルにおいて、OneLake知識ソースをPythonで使用する方法に関する情報が更新されたことを示しています。主な変更点は、「Usage support」セクションの追加です。このセクションでは、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）およびREST APIのサポート状況が表形式で提供され、各プラットフォームの互換性が明確に示されています。また、前提条件に関する説明が補足され、Azure AI Searchのエージェントリトリーバルを提供する地域や、セマンティックランカーの有効化についての情報も追加されています。この更新により、ユーザーはOneLake知識ソースの実装に必要な情報をより簡単に理解できるようになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-onelake-rest.md{#item-876f49}

<details>
<summary>Diff</summary>
````diff
@@ -20,6 +20,12 @@ When you create a OneLake knowledge source, you specify an external data source,
 
 The generated indexer conforms to the *OneLake indexer*, whose prerequisites, supported tasks, supported document formats, supported shortcuts, and limitations also apply to OneLake knowledge sources. For more information, see the [OneLake indexer documentation](../../search-how-to-index-onelake-files.md).
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OneLake 知識ソースのREST APIによる使用方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-onelake-rest.md`ファイルにおいて、OneLake知識ソースをREST APIで使用する方法に関する情報が更新されたことを示しています。主な変更内容は、「Usage support」セクションが新たに追加された点です。このセクションでは、AzureポータルやMicrosoft Foundryポータル、さまざまなSDK（.NET、Python、Java、JavaScript）、およびREST APIのサポート状況が表形式で示され、それぞれのプラットフォームにおける互換性が一目で分かるようになっています。また、前提条件に関する記述も追加され、Azure AI Searchのエージェントリトリーバルを提供する地域や、セマンティックランカーの必要性についての情報が含まれています。この更新により、ユーザーはOneLake知識ソースのREST APIを用いた実装に必要な情報をより簡単に把握できるようになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-csharp.md{#item-d3510c}

<details>
<summary>Diff</summary>
````diff
@@ -11,6 +11,12 @@ ms.date: 11/19/2025
 
 A *search index knowledge source* specifies a connection to an Azure AI Search index that provides searchable content in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#によるエージェント情報検索インデックスの使用方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-search-index-csharp.md`ファイルに対するものであり、C#を使用してエージェント情報検索インデックスに接続する方法に関する情報が更新されています。主な追加内容は、「Usage support」セクションであり、ここではAzureポータルやMicrosoft Foundryポータル、複数のSDK（.NET、Python、Java、JavaScript）およびREST APIのサポート状況が表形式で示されています。すべてのプラットフォームについて「✔️」が付され、対応していることが明示されています。また、前提条件も更新され、Azure AI Searchのエージェントリトリーバルを提供する地域や、セマンティックランカーの有効化についての情報が追加されています。この更新により、ユーザーはC#を用いたエージェント情報検索インデックスの実装に関する必要な情報をより的確に取得できるようになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-python.md{#item-58056f}

<details>
<summary>Diff</summary>
````diff
@@ -11,6 +11,12 @@ ms.date: 11/14/2025
 
 A *search index knowledge source* specifies a connection to an Azure AI Search index that provides searchable content in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonによるエージェント情報検索インデックスの使用方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-search-index-python.md`ファイルに対して行われ、Pythonを用いてエージェント情報検索インデックスに接続する方法に関する情報が更新されています。新たに「Usage support」というセクションが追加され、ここではAzureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）、およびREST APIのサポート状況が表形式で示されています。全てのプラットフォームについて「✔️」が付され、対応していることが確認できます。また、前提条件として、Azure AI Searchがエージェントリトリーバルを提供する地域で使用され、セマンティックランカーが有効である必要がある旨が明記されています。この更新により、ユーザーはPythonを使用したエージェント情報検索インデックスの実装に関する必要な情報を簡単に得ることができるようになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-search-index-rest.md{#item-e95367}

<details>
<summary>Diff</summary>
````diff
@@ -11,6 +11,12 @@ ms.date: 11/14/2025
 
 A *search index knowledge source* specifies a connection to an Azure AI Search index that provides searchable content in an agentic retrieval pipeline. [Knowledge sources](../../agentic-knowledge-source-overview.md) are created independently, referenced in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md), and used as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIによるエージェント情報検索インデックスの使用方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-search-index-rest.md`ファイルに対するもので、REST APIを使用してエージェント情報検索インデックスに接続する方法に関する内容が更新されています。新しく追加された「Usage support」セクションでは、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）、ならびにREST APIのサポート状況が表形式で示されています。このすべてのプラットフォームに対し、「✔️」が付けられており、それぞれが利用可能であることが確認できます。また、前提条件として、Azure AI Searchがエージェントリトリーバルを提供する地域で使用され、かつセマンティックランカーを有効にする必要があることが記載されています。この更新により、ユーザーはREST APIに関するエージェント情報検索インデックスの具体的な利用法を理解しやすくなります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md{#item-2eb305}

<details>
<summary>Diff</summary>
````diff
@@ -18,6 +18,12 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
 + An index that stores enriched content and meets the criteria for agentic retrieval.
 + An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#によるSharePointインデックスのエージェント情報共有方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md`ファイルに対するもので、C#を用いてインデックスされたSharePoint知識源を作成する方法に関する情報が更新されています。新しく追加された「Usage support」セクションでは、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）、およびREST APIのサポート状況が表形式で示されており、各プラットフォームの利用可能性が確認できるようになっています。特にAzureポータルに関しては「❌」が示されており、利用できないことが明記されています。また、前提条件として、Azure AI Searchがエージェントリトリーバルを提供する地域での利用と、セマンティックランカーが有効である必要があることが記載されています。この更新により、ユーザーはC#を使用したSharePointインデックスの具体的な利用法をより容易に理解できるようになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-python.md{#item-923abb}

<details>
<summary>Diff</summary>
````diff
@@ -18,6 +18,12 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
 + An index that stores enriched content and meets the criteria for agentic retrieval.
 + An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PythonによるSharePointインデックスのエージェント情報共有方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-sharepoint-indexed-python.md`ファイルに対するもので、Pythonを使用してインデックスされたSharePoint知識源を作成する方法に関する情報が更新されています。新しく追加された「Usage support」セクションでは、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）、およびREST APIのサポート状況が表形式で示されており、各プラットフォームの利用可能性を明確にしています。特にAzureポータルについては「❌」が表示されており、利用できないことが記載されています。また、前提条件として、Azure AI Searchがエージェントリトリーバルを提供する地域で利用可能であること、並びにセマンティックランカーが有効化されている必要があることが強調されています。この更新により、ユーザーはPythonを用いたSharePointインデックスの具体的な利用法をより容易に理解できるようになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-rest.md{#item-e26ea0}

<details>
<summary>Diff</summary>
````diff
@@ -18,6 +18,12 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
 + An index that stores enriched content and meets the criteria for agentic retrieval.
 + An indexer that uses the previous objects to drive the indexing and enrichment pipeline.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIによるSharePointインデックスのエージェント情報共有方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-sharepoint-indexed-rest.md`ファイルに対するもので、REST APIを使用してインデックスされたSharePoint知識源を作成する方法に関する情報が更新されています。新たに追加された「Usage support」セクションでは、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）、およびREST APIのサポート状況が表形式で示されています。具体的には、Azureポータルに関して「❌」が表示され、利用できないことが強調されています。また、前提条件として、Azure AI Searchがエージェントリトリーバルを提供する地域で利用可能であること、そしてセマンティックランカーを有効にする必要があることが述べられています。この更新により、ユーザーはREST APIを利用したSharePointインデックスの具体的な使用方法をより簡単に把握できるようになっています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-csharp.md{#item-f8bed1}

<details>
<summary>Diff</summary>
````diff
@@ -21,6 +21,12 @@ At query time, the remote SharePoint knowledge source calls the Copilot Retrieva
 
 Like any other knowledge source, you specify a remote SharePoint knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md) and use the results as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#によるリモートSharePointインデックスのエージェント情報共有方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-sharepoint-remote-csharp.md`ファイルに対するもので、C#を使用してリモートSharePoint知識源を作成し、利用する方法に関する情報が更新されています。新たに追加された「Usage support」セクションでは、Azureポータル、Microsoft Foundryポータル、さまざまなSDK（.NET、Python、Java、JavaScript）、およびREST APIのサポート状況が表形式で示されています。特にAzureポータルには「❌」が表示されており、利用できないことが明記されています。また、前提条件として、Azure AI Searchがエージェントリトリーバルを提供する地域で使用可能であり、セマンティックランカーを有効にする必要があることも記載されています。この更新により、ユーザーはC#を通じてリモートSharePointインデックスを利用する方法をより理解しやすくなっています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-python.md{#item-822712}

<details>
<summary>Diff</summary>
````diff
@@ -21,6 +21,12 @@ At query time, the remote SharePoint knowledge source calls the Copilot Retrieva
 
 Like any other knowledge source, you specify a remote SharePoint knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md) and use the results as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PythonによるリモートSharePointインデックスのエージェント情報共有方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-sharepoint-remote-python.md`ファイルに対するもので、Pythonを使用してリモートSharePoint知識源を作成して利用する方法に関する情報が更新されています。新たに追加された「Usage support」セクションでは、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）、およびREST APIのサポート状況が表形式で示されています。特に、Azureポータルに関しては「❌」が表示されており、利用できないことが強調されています。また、前提条件として、Azure AI Searchがエージェントリトリーバルを提供する地域で使用可能であり、セマンティックランカーを有効にする必要があることも記載されています。この更新により、ユーザーはPythonを利用したリモートSharePointインデックスの具体的な使用方法をより簡単に理解できるようになっています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-remote-rest.md{#item-5514b1}

<details>
<summary>Diff</summary>
````diff
@@ -21,6 +21,12 @@ At query time, the remote SharePoint knowledge source calls the Copilot Retrieva
 
 Like any other knowledge source, you specify a remote SharePoint knowledge source in a [knowledge base](../../agentic-retrieval-how-to-create-knowledge-base.md) and use the results as grounding data when an agent or chatbot calls a [retrieve action](../../agentic-retrieval-how-to-retrieve.md) at query time.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + Azure AI Search in any [region that provides agentic retrieval](../../search-region-support.md). You must have [semantic ranker enabled](../../semantic-how-to-enable-disable.md). 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTを利用したリモートSharePointインデックスのエージェント情報共有方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-sharepoint-remote-rest.md`ファイルに対するもので、RESTを使用してリモートSharePoint知識源を作成し、使用する方法に関する情報が更新されています。新たに追加された「Usage support」セクションでは、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）、およびREST APIのサポート状況が表形式で示されています。特にAzureポータルには「❌」が表示され、利用できないことが強調されています。また、前提条件として、Azure AI Searchがエージェントリトリーバルを提供する地域で使用可能であり、セマンティックランカーを有効にする必要があることも記載されています。この更新によって、ユーザーはRESTを利用したリモートSharePointインデックスの具体的な利用方法をより明確に理解できるようになっています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-csharp.md{#item-401063}

<details>
<summary>Diff</summary>
````diff
@@ -30,6 +30,12 @@ When you use Web Knowledge Source, keep the following in mind:
 
 + Because Web Knowledge Source doesn't support extractive data, your knowledge base must use [answer synthesis](../../agentic-retrieval-how-to-answer-synthesis.md) and [low or medium reasoning effort](../../agentic-retrieval-how-to-create-knowledge-base.md#create-a-knowledge-base). You also can't define answer instructions.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + An Azure subscription with [access to Web Knowledge Source](../../agentic-knowledge-source-how-to-web-manage.md). By default, access is enabled. Contact your admin if access is disabled.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#によるWeb知識源のエージェント情報共有方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-web-csharp.md`ファイルに対するもので、C#を使用してWeb知識源を作成し利用する方法に関する情報が更新されています。主な追加内容として、Web知識源が抽出データをサポートしていないため、知識ベースで「回答合成」を使用し、「低または中程度の推論努力」を設定する必要があることが記載されています。また、回答指示を定義することができない点も強調されています。

さらに、「Usage support」セクションが追加され、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）、およびREST APIのサポート状況が表形式で示されています。特に、Azureポータルには「❌」が表示されており、利用できないことが示されています。最後に、Web知識源へのアクセスを持つAzureサブスクリプションが必要であること、デフォルトではアクセスが有効であること、およびアクセスが無効な場合は管理者に連絡する必要があることも記述されています。この更新により、ユーザーはC#を用いたWeb知識源の具体的な使用方法と前提条件をより明確に理解できるようになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-python.md{#item-72b59c}

<details>
<summary>Diff</summary>
````diff
@@ -30,6 +30,12 @@ When you use Web Knowledge Source, keep the following in mind:
 
 + Because Web Knowledge Source doesn't support extractive data, your knowledge base must use [answer synthesis](../../agentic-retrieval-how-to-answer-synthesis.md) and [low or medium reasoning effort](../../agentic-retrieval-how-to-create-knowledge-base.md#create-a-knowledge-base). You also can't define answer instructions.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + An Azure subscription with [access to Web Knowledge Source](../../agentic-knowledge-source-how-to-web-manage.md). By default, access is enabled. Contact your admin if access is disabled.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PythonによるWeb知識源のエージェント情報共有方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-web-python.md`ファイルに対するもので、Pythonを使用してWeb知識源を作成し使用する方法に関する情報が更新されています。主な追加内容として、Web知識源が抽出データをサポートしていないため、知識ベースでは「回答合成」を使用し、「低または中程度の推論努力」を設定する必要があることが記載されています。また、回答指示を定義することができないという制約も明確にされています。

さらに、「Usage support」セクションが追加され、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）、およびREST APIのサポート状況が表形式で示されています。特にAzureポータルには「❌」が表示されており、利用できないことが強調されています。最後に、Web知識源へのアクセスを持つAzureサブスクリプションが必要であること、デフォルトでアクセスが有効であることに加え、アクセスが無効な場合は管理者に連絡する必要がある旨が記載されています。この更新により、ユーザーはPythonを用いたWeb知識源の具体的な使用方法と前提条件をよりよく理解できるようになります。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-web-rest.md{#item-649608}

<details>
<summary>Diff</summary>
````diff
@@ -30,6 +30,12 @@ When you use Web Knowledge Source, keep the following in mind:
 
 + Because Web Knowledge Source doesn't support extractive data, your knowledge base must use [answer synthesis](../../agentic-retrieval-how-to-answer-synthesis.md) and [low or medium reasoning effort](../../agentic-retrieval-how-to-create-knowledge-base.md#create-a-knowledge-base). You also can't define answer instructions.
 
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-sources?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
+
 ## Prerequisites
 
 + An Azure subscription with [access to Web Knowledge Source](../../agentic-knowledge-source-how-to-web-manage.md). By default, access is enabled. Contact your admin if access is disabled.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTを使用したWeb知識源のエージェント情報共有方法の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-web-rest.md`ファイルに対するもので、RESTを利用してWeb知識源を作成し使用する方法に関する情報が更新されています。主な追加内容として、Web知識源が抽出データをサポートしていないため、知識ベースでは「回答合成」を使用し、「低または中程度の推論努力」を設定する必要があることが記載されています。また、回答指示を定義することができないという重要なポイントも強調されています。

さらに、新たに「Usage support」セクションが追加され、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）、およびREST APIのサポート状況を表形式で示しています。特にAzureポータルには「❌」が表示されており、利用できないことが明示されています。最後に、Web知識源へのアクセスを持つAzureサブスクリプションが必要であること、デフォルトではアクセスが有効であること、アクセスが無効な場合には管理者に連絡する必要がある旨が記述されています。この更新により、ユーザーはRESTを用いたWeb知識源の具体的な使用方法と前提条件をより明確に理解できるようになります。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-csharp.md{#item-4469a2}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,13 @@ ms.date: 01/23/2026
 
 In Azure AI Search, a *knowledge base* is a top-level object that orchestrates [agentic retrieval](../../agentic-retrieval-overview.md). It defines which knowledge sources to query and the default behavior for retrieval operations. At query time, the [retrieve method](../../agentic-retrieval-how-to-retrieve.md) targets the knowledge base to run the configured retrieval pipeline.
 
-You can create a knowledge base in a [Foundry IQ workload](/azure/ai-foundry/agents/how-to/tools/knowledge-retrieval) in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
+You can create a knowledge base in a [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) workload in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
+
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 A knowledge base specifies:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#による知識ベースの作成方法に関する情報の更新"
}
```

### Explanation
この変更は、`agentic-retrieval-how-to-create-knowledge-base-csharp.md`ファイルに対するもので、C#を使用して知識ベースを作成する方法に関する情報が更新されています。主な変更点には、Microsoft Foundry (新しい) ポータル内の「Foundry IQ workload」についての説明の修正があります。具体的には、「Foundry IQ workload」という用語が正確に表現され、より明確な説明へと更新されています。

加えて、新たに「Usage support」セクションが追加され、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）およびREST APIのサポート状況が表形式で示されています。すべての項目には「✔️」マークが付いており、利用可能であることが示されています。これにより、ユーザーはC#を用いた知識ベースの具体的な作成方法と、その利用サポートに関する情報をより明確に理解できるようになります。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-python.md{#item-4e498f}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,13 @@ ms.date: 01/15/2026
 
 In Azure AI Search, a *knowledge base* is a top-level object that orchestrates [agentic retrieval](../../agentic-retrieval-overview.md). It defines which knowledge sources to query and the default behavior for retrieval operations. At query time, the [retrieve method](../../agentic-retrieval-how-to-retrieve.md) targets the knowledge base to run the configured retrieval pipeline.
 
-You can create a knowledge base in a [Foundry IQ workload](/azure/ai-foundry/agents/how-to/tools/knowledge-retrieval) in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
+You can create a knowledge base in a [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) workload in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
+
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 A knowledge base specifies:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonによる知識ベースの作成方法に関する情報の更新"
}
```

### Explanation
この変更は、`agentic-retrieval-how-to-create-knowledge-base-python.md`ファイルに対するもので、Pythonを使用して知識ベースを作成する方法に関する情報が更新されています。変更の主なポイントは、「Microsoft Foundry (新しい) ポータル」における「Foundry IQ workload」の表現の修正です。この用語が名称として明確に定義され、混乱を避けるために改善されています。

さらに、新しい「Usage support」セクションが追加され、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）、およびREST APIの利用可能性が表形式で示されています。すべての項目には「✔️」マークが付けられており、各リソースが利用可能であることが強調されています。これにより、ユーザーはPythonを用いた知識ベースの具体的な作成方法と、その利用サポートに関する情報をより明確に把握できるようになります。

## articles/search/includes/how-tos/agentic-retrieval-how-to-create-knowledge-base-rest.md{#item-37851c}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,13 @@ ms.date: 01/23/2026
 
 In Azure AI Search, a *knowledge base* is a top-level object that orchestrates [agentic retrieval](../../agentic-retrieval-overview.md). It defines which knowledge sources to query and the default behavior for retrieval operations. At query time, the [retrieve method](../../agentic-retrieval-how-to-retrieve.md) targets the knowledge base to run the configured retrieval pipeline.
 
-You can create a knowledge base in a [Foundry IQ workload](/azure/ai-foundry/agents/how-to/tools/knowledge-retrieval) in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
+You can create a knowledge base in a [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) workload in the Microsoft Foundry (new) portal. You also need a knowledge base in any agentic solutions that you create using the Azure AI Search APIs.
+
+### Usage support
+
+| [Azure portal](../../get-started-portal-agentic-retrieval.md) | [Microsoft Foundry portal](/azure/ai-foundry/agents/concepts/what-is-foundry-iq#workflow) | [.NET SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/CHANGELOG.md) | [Python SDK](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [Java SDK](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/search/azure-search-documents/CHANGELOG.md) | [JavaScript SDK](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/search/search-documents/CHANGELOG.md) | [REST API](/rest/api/searchservice/knowledge-bases?view=rest-searchservice-2025-11-01-preview&preserve-view=true) |
+|--|--|--|--|--|--|--|
+| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
 
 A knowledge base specifies:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RESTによる知識ベースの作成方法に関する情報の更新"
}
```

### Explanation
この変更は、`agentic-retrieval-how-to-create-knowledge-base-rest.md`ファイルに対するもので、RESTを使用して知識ベースを作成する方法に関する情報が更新されています。主な変更点としては、「Microsoft Foundry (新しい) ポータル」での「Foundry IQ workload」という表現がより正確に修正され、理解しやすくなっています。

また、新たに「Usage support」セクションが追加され、Azureポータル、Microsoft Foundryポータル、各種SDK（.NET、Python、Java、JavaScript）およびREST APIのサポート状況が表形式でまとめられています。表内のすべての項目には「✔️」マークが付けられており、各リソースが利用可能であることを示しています。この変更により、RESTを使用するユーザーは知識ベースの作成手順と、関連するリソースの利用状況についての情報をより明確に把握できるようになります。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -239,9 +239,9 @@ There are many ways to get started, including code-first solutions and demos.
 
 ### [**Videos**](#tab/videos)
 
-+ [Foundry IQ: the future of RAG with knowledge retrieval and AI Search](https://www.youtube.com/watch?v=slDdNIQCJBQ)
++ [Foundry IQ: The future of RAG with knowledge retrieval and Azure AI Search](https://www.youtube.com/watch?v=slDdNIQCJBQ)
 
-+ [Build agents with knowledge, agentic RAG and Azure AI Search](https://www.youtube.com/watch?v=lW47o2ss3Yg) 
++ [Build agents with knowledge, agentic RAG, and Azure AI Search](https://www.youtube.com/watch?v=lW47o2ss3Yg) 
 
 + [(Classic RAG) Vector search and state of the art retrieval for Generative AI apps](https://www.youtube.com/watch?v=lSzc1MJktAo)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGに関するビデオリンクの表現の修正"
}
```

### Explanation
この変更は、`retrieval-augmented-generation-overview.md`ファイルに対するもので、RAG（Retrieval-Augmented Generation）の紹介に関連するビデオリンクの表現が修正されています。具体的には、次のように改善されています。

1. 「Foundry IQ: the future of RAG with knowledge retrieval and AI Search」というタイトルが「Foundry IQ: The future of RAG with knowledge retrieval and Azure AI Search」に変更され、表記が一貫性のあるものになりました。
2. 「Build agents with knowledge, agentic RAG and Azure AI Search」という表現も「Build agents with knowledge, agentic RAG, and Azure AI Search」に更新され、カンマの使用が統一されています。
3. 新たに「(Classic RAG) Vector search and state of the art retrieval for Generative AI apps」というビデオリンクが追加され、RAGに関する情報がより豊富になっています。

これにより、ユーザーはRAGに関する最新の情報とリソースをより効果的に参照できるようになっています。

## articles/search/search-how-to-index-sql-server.md{#item-d7fb35}

<details>
<summary>Diff</summary>
````diff
@@ -90,11 +90,9 @@ You can find out the IP address range of `AzureCognitiveSearch` [service tag](/a
 
 ### Include the Azure portal IP addresses
 
-If you're using the Azure portal to create an indexer, you must grant the Azure portal inbound access to your SQL Azure virtual machine. An inbound rule in the firewall requires that you provide the IP address of the Azure portal.
+If you're using the [legacy Import data wizard](search-import-data-portal.md) in the Azure portal to create an indexer that pulls from Azure Cosmos DB or Azure SQL, you must grant the Azure portal IP address inbound access to your SQL Azure virtual machine. For more information, see [Allow access from the Azure portal IP address](service-configure-firewall.md#allow-access-from-the-azure-portal-ip-address).
 
-To get the Azure portal IP address, ping `stamp2.ext.search.windows.net`, which is the domain of the traffic manager. The request times out, but the IP address is visible in the status message. For example, in the message "Pinging azsyrie.northcentralus.cloudapp.azure.com [52.252.175.48]", the IP address is "52.252.175.48".
-
-Clusters in different regions connect to different traffic managers. Regardless of the domain name, the IP address returned from the ping is the correct one to use when defining an inbound firewall rule for the Azure portal in your region.
+We recommend using the [Import data (new) wizard](search-get-started-portal.md), which doesn't have this limitation. 
 
 ## Supplement network security with token authentication
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SQL Serverインデクサー作成手順の更新"
}
```

### Explanation
この変更は、`search-how-to-index-sql-server.md`ファイルに対するもので、SQL Serverインデクサーを作成する際の手順が更新されています。具体的には、以下の点が修正されています。

1. Azureポータルを使用してインデクサーを作成する際には、AzureポータルのIPアドレスにSQL Azure仮想マシンへの受信アクセスを許可する必要があることが強調されています。新しい文言では「[legacy Import data wizard](search-import-data-portal.md)」を使用する場合の条件が詳述されています。

2. AzureポータルのIPアドレスを取得する方法として、以前の手順では`stamp2.ext.search.windows.net`へのpingを推奨していましたが、現在はその情報が省略され、新しい「[Import data (new) wizard](search-get-started-portal.md)」を使うことが推奨されています。この新しいウィザードは受信アクセスの制限がないため、より便利であるとされています。

3. また、ファイアウォールルール定義に関する情報も調整され、特定の領域のトラフィックマネージャーとの関連は削除されています。

これにより、ユーザーはSQL Serverインデクサー作成時の手順が明確になり、アクセス許可の管理がより容易になります。

## articles/search/search-import-data-portal.md{#item-b804d1}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about the Azure portal wizards that create and load an index
 author: HeidiSteen
 ms.author: heidist
 manager: nitinme
-ms.date: 12/05/2025
+ms.date: 01/29/2026
 ms.service: azure-ai-search
 ms.topic: concept-article
 ms.custom:
@@ -22,7 +22,7 @@ ms.custom:
 > + The **Import and vectorize data** wizard is now called **Import data (new)**.
 > + The **Import data** workflow is now available in **Import data (new)**.
 >
-> The **Import data** wizard will eventually be deprecated. For now, you can still use this wizard, but we recommend the new wizard for an improved search experience that uses the latest frameworks.
+> The **Import data** wizard will be deprecated soon. For now, you can still use this wizard, but we recommend the new wizard for an improved search experience that uses the latest frameworks.
 >
 > The wizards don't have identical keyword search workflows. Certain skills and capabilities are only available in the old wizard. For more information about their similarities and differences, continue reading this article.
 
@@ -163,33 +163,56 @@ The wizards have the following limitations:
 
 + Source content must reside in a [supported data source](search-indexer-overview.md#supported-data-sources).
 
-+ Sampling occurs over a subset of source data. For large data sources, it's possible for the wizards to miss fields. If sampling is insufficient, you might need to extend the schema or correct the inferred data types.
++ Sampling, used to infer a preliminary index schema, occurs over a subset of source data. For large data sources, it's possible for the wizards to miss fields. If sampling is insufficient, you might need to manually add fields to the index or correct the inferred data types.
 
-+ [AI enrichment](cognitive-search-concept-intro.md), as exposed in the Azure portal, is limited to a subset of built-in skills.
++ [AI enrichment](cognitive-search-concept-intro.md) and [integrated vectorization](vector-search-integrated-vectorization.md), as exposed in the wizards, is limited to a subset of built-in skills.
 
-+ A [knowledge store](knowledge-store-concept-intro.md), which is only available through the **Import data** wizard, is limited to a few default projections and uses a default naming convention. To customize projections and names, you must create the knowledge store through the REST APIs or Azure SDKs.
++ A [knowledge store](knowledge-store-concept-intro.md), which is only available through the legacy **Import data** wizard, is limited to a few default projections and uses a default naming convention. To customize projections and names, you must create the knowledge store through the REST APIs or Azure SDKs.
 
 ## Secure connections
 
-The wizards use the Azure portal controller and public endpoints to make outbound connections. You can't use the wizards if Azure resources are accessed over a private connection or through a shared private link.
+Network protections affect the portal-to-endpoint connection and also the endpoint-to-external-resource connections during portal operations.
 
-You can use the wizards over restricted public connections, but not all functionality is available.
+### Portal connections to a search service
 
-+ On supported Azure data sources protected by firewalls, you can retrieve data if you have the right firewall rules in place.
+Portal connections to a network-protected endpoint are made using your client IP address.
 
-  The Azure resource must admit network requests from the IP address of the device used on the connection. You should also list Azure AI Search as a trusted service on the resource's network configuration. For example, in Azure Storage, you can list `Microsoft.Search/searchServices` as a trusted service.
++ For a firewall-protected search service, [add your client IP address to an inbound rule](service-configure-firewall.md#configure-network-access-and-firewall-rules-for-azure-ai-search).
 
-+ On connections to a Foundry resource for AI enrichment, or on connections to embedding models deployed in the [Foundry portal](https://ai.azure.com/?cid=learnDocs) or Azure OpenAI, public internet access must be enabled unless your search service meets the creation date, tier, and region requirements for private connections. For more information, see [Make outbound connections through a shared private link](search-indexer-howto-access-private.md).
++ For a search service configured for a [private endpoint](service-create-private-endpoint.md), use a browser on an allow-listed virtual machine to open portal pages and run wizards.
 
-  For AI enrichment, connections to Foundry resources are for [billing purposes](cognitive-search-attach-cognitive-services.md). You're billed when API calls for built-in skills (in the **Import data** wizard or the keyword search workflow in the **Import data (new)** wizard) and integrated vectorization (in the **Import data (new)** wizard) exceed the free transaction count (20 per indexer run).
++ For a search service joined to a network security perimeter, [add your client IP address to an inbound rule](search-security-network-security-perimeter.md#add-an-inbound-access-rule).
 
-  If Azure AI Search can't connect:
+> [!TIP]
+> The portal detects your client IP address and prompts you add it to the search service firewall.
 
-  + In the **Import data (new)** wizard, the error is `"Access denied due to Virtual Network/Firewall rules."`.
+### Portal connections to external resources
 
-  + In the **Import data** wizard, there's no error, but the skillset won't be created.
+The portal wizards connect to external resources for:
 
-If firewall settings prevent your wizard workflows from succeeding, consider scripted or programmatic approaches instead.
++ Data retrieval during indexing
++ AI processing for [enrichment](cognitive-search-concept-intro.md) and [integrated vectorization](vector-search-integrated-vectorization.md) performed by a Foundry resource or model
+
+From the portal wizards, almost every outbound request for network-protected data and AI processing is made using the IP address of your client, with the exception of:
+
++ The legacy Import data wizard
++ Connecting to either Azure Cosmos DB or Azure SQL
+
+This section explains connection requirements for outbound requests, and how to handle the exception.
+
+#### Configuring portal access to external resources
+
++ **IP-protected resources**: Add your client IP address to the external resource's `allowList`. If supported, list `Microsoft.Search/searchServices` as a trusted service. For example, in Azure Storage, you can list `Microsoft.Search/searchServices` as a trusted service.
+
++ **Private connections**: The wizards use [shared private links](search-indexer-howto-access-private.md). Verify your search service meets tier and region requirements. Verify your external data source is supported for shared private links.
+
+#### Exception: Legacy wizard with Cosmos DB and Azure SQL
+
+The legacy wizard connects through a portal controller with its own IP address. You must use a public endpoint (no private link support) and [add the portal controller IP to inbound rules](service-configure-firewall.md#allow-access-from-the-azure-portal-ip-address).
+
+You can avoid this restriction by using the **Import data (new)** wizard.
+
+If the wizards can't connect, you'll see `"Access denied due to Virtual Network/Firewall rules"` in the new wizard, or the skillset silently fails to create in the legacy wizard. Consider scripted or programmatic approaches as an alternative.
 
 ## Workflow
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データインポート ポータルに関する更新"
}
```

### Explanation
この変更は、`search-import-data-portal.md`ファイルに対するもので、Azureポータルのデータインポートウィザードに関する情報が更新されています。以下の重要な変更点が含まれています。

1. **日付の更新**: ドキュメントの日付が2025年12月5日から2026年1月29日に変更されました。

2. **ウィザードの名称変更**: 「**Import and vectorize data**」ウィザードが「**Import data (new)**」に改名され、旧ウィザードの非推奨が強調されています。

3. **インポートデータウィザードの非推奨について**: 「**Import data**」ウィザードの非推奨予定についての表現が強化され、ユーザーには新しいウィザードの使用が推奨されています。

4. **制限事項の明確化**: インポートウィザードの利用における各種制限が詳細に述べられ、特にインデックススキーマの推定に関するサンプリングの説明が明確化されています。

5. **ネットワーク接続に関する情報**: ポータルからの接続要件やファイアウォールルールに基づく制限が強調され、特定の条件を満たすリソースへの接続についてが詳しく説明されています。

6. **新しいセクション追加**: ポータルから外部リソースへの接続要件や特例が明示され、特に従来のウィザードとの接続条件に関する詳細なガイドラインが追加されました。

これにより、ユーザーはデータインポートの手順が改良され、最新のワークフローや接続要件についての理解が深まることが期待されます。

## articles/search/search-indexer-howto-access-ip-restricted.md{#item-aec22f}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: arv100kri
 ms.author: arjagann
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 01/22/2026
+ms.date: 01/29/2026
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
@@ -82,30 +82,9 @@ Add your client IP address to allow access to the service from the Azure portal
 
 ## Get the Azure portal IP address
 
-If you're using the Azure portal or an [import wizard](search-import-data-portal.md) to create an indexer, you need an inbound rule for the Azure portal as well.
+If you're using the [legacy Import data wizard](search-import-data-portal.md) in the Azure portal to create an indexer that pulls from Azure Cosmos DB or Azure SQL, you must grant the Azure portal IP address inbound access to your SQL Azure virtual machine. For more information, see [Allow access from the Azure portal IP address](service-configure-firewall.md#allow-access-from-the-azure-portal-ip-address).
 
-To get the Azure portal's IP address, perform `nslookup` (or `ping`) on `stamp2.ext.search.windows.net`, which is the domain of the traffic manager. For nslookup, the IP address is visible in the "Non-authoritative answer" portion of the response. 
-
-In the following example, the IP address that you should copy is `52.252.175.48`.
-
-```bash
-$ nslookup stamp2.ext.search.windows.net
-Server:  ZenWiFi_ET8-0410
-Address:  192.168.50.1
-
-Non-authoritative answer:
-Name:    azsyrie.northcentralus.cloudapp.azure.com
-Address:  52.252.175.48
-Aliases:  stamp2.ext.search.windows.net
-          azs-ux-prod.trafficmanager.net
-          azspncuux.management.search.windows.net
-```
-
-The `Address` field (52.252.175.48) is the Azure portal IP address for your region.
-
-Services in different regions connect to different traffic managers. Regardless of the domain name, the IP address returned from the ping is the correct one to use when defining an inbound firewall rule for the Azure portal in your region.
-
-For ping, the request times out, but the IP address is visible in the response. For example, in the message `Pinging azsyrie.northcentralus.cloudapp.azure.com [52.252.175.48]`, the IP address is `52.252.175.48`.
+We recommend using the [Import data (new) wizard](search-get-started-portal.md), which doesn't have this limitation. 
 
 ## Get IP addresses for "AzureCognitiveSearch" service tag
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "IP制限されたサービスへのアクセス手順の更新"
}
```

### Explanation
この変更は、`search-indexer-howto-access-ip-restricted.md`ファイルに対して行われ、AzureポータルからIP制限されたサービスにアクセスする手順が更新されています。以下のポイントが重要な変更点です：

1. **日付の更新**: ドキュメントの日付が2026年1月22日から2026年1月29日に変更されました。

2. **新しいウィザードの推奨**: 「**legacy Import data wizard**」を使用してインデクサーを作成する場合の条件が説明され、従来のウィザードから「**Import data (new)**」ウィザードの利用が推奨されています。新しいウィザードでは、特定の制限がないため、より簡単にアクセスが可能です。

3. **IPアドレスの取得手順の簡略化**: AzureポータルのIPアドレスを取得するための手順が簡略化され、複雑な手順としての`nslookup`や`ping`コマンドの具体的な説明が削除されました。代わりに、特定のリンクを参照することで、必要な情報が得られることが示されています。

この変更により、ユーザーはAzureポータルからのインデクサー作成時に必要な手順がより簡潔になり、新しいウィザードを利用することで、よりスムーズに操作できるようになります。

## articles/search/search-try-for-free.md{#item-36e28d}

<details>
<summary>Diff</summary>
````diff
@@ -80,7 +80,7 @@ You can access Azure AI Search through two portals, each optimized for different
 | Portal | Description | What you can do |
 |--------|-------------|-----------------|
 | [Azure portal](https://portal.azure.com/) | The primary management interface for Azure resources and your Azure AI Search service. **This portal is most useful for classic search scenarios and overall resource management.** | <ul><li>Create and configure your search service.</li><li>Build knowledge bases and knowledge sources for [agentic retrieval](search-what-is-azure-search.md#what-is-agentic-retrieval).</li><li>Build indexes, indexers, data sources, and skillsets for [classic search](search-what-is-azure-search.md#what-is-classic-search).</li><li>Query your knowledge bases and indexes.</li><li>Track credits and monitor costs.</li></ul> |
-| [Microsoft Foundry portal](https://ai.azure.com/?cid=learnDocs) | A unified platform for deploying models and building AI applications. **This portal is most useful for agentic retrieval (RAG) scenarios.** | <ul><li>Deploy embedding and chat models.</li><li>Use [Foundry IQ](/azure/ai-foundry/agents/how-to/tools/knowledge-retrieval) to connect your Azure AI Search knowledge base to an AI agent.</li></ul> |
+| [Microsoft Foundry portal](https://ai.azure.com/?cid=learnDocs) | A unified platform for deploying models and building AI applications. **This portal is most useful for agentic retrieval (RAG) scenarios.** | <ul><li>Deploy embedding and chat models.</li><li>Use [Foundry IQ](/azure/ai-foundry/agents/concepts/what-is-foundry-iq.md) to connect your Azure AI Search knowledge base to an AI agent.</li></ul> |
 
 ## Track your credit usage
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Foundry IQのリンクを更新"
}
```

### Explanation
この変更は、`search-try-for-free.md`ファイルに対して行われ、Microsoft Foundryポータルに関する情報が更新されています。主な変更点は以下の通りです：

1. **リンクの修正**: Microsoft Foundryポータルに関連する説明の中で、`Foundry IQ`のリンクが修正されました。具体的には、リンク先が`/azure/ai-foundry/agents/how-to/tools/knowledge-retrieval`から、`/azure/ai-foundry/agents/concepts/what-is-foundry-iq.md`に変更されています。これにより、ユーザーはより正確な情報にアクセスできるようになります。

2. **テキストの整合性**: 文中の情報は整合性が保たれ、ユーザーがFoundry IQを利用してAzure AI Searchの知識ベースをAIエージェントに接続する方法が明瞭に示されています。

この修正により、ユーザーは最新のリソースに基づいた正確な導入情報を得ることができ、Azure AI Searchをより効果的に活用する手助けとなることが期待されます。

## articles/search/service-configure-firewall.md{#item-75be3f}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 01/22/2026
+ms.date: 01/29/2026
 ms.custom:
   - ignite-2023
   - sfi-image-nochange
@@ -70,16 +70,22 @@ When requests originate from IP addresses that aren't in the allowed list, a gen
 
 ## Allow access from the Azure portal IP address
 
-The Azure portal has its own connection to Azure AI Search, separate from your local device and browser. If you use the Azure portal to manage your search service, you need to add the portal IP address as described in this section, and your client IP address as described in the previous section.
+The Azure portal uses your client IP address for a direct connection to Azure AI Search. If your client is in the allowed IP list, you can use almost all portal capabilities with no extra configuration required. However, there's an exception for the legacy Import data wizard when you *import from either Azure Cosmos DB or Azure SQL*. 
 
-When IP rules are configured, some features of the Azure portal are disabled. For example, you can view and manage service level information, but portal access to the import wizards, indexes, indexers, and other top-level resources are restricted. 
+This scenario requires a separate IP address for the connection:
 
-You can restore the Azure portal's access to the full range of search service operations by adding the Azure portal IP address to the restricted address range. 
++ Identify the IP address used by the legacy wizard for this connection.
 
-To get the Azure portal's IP address, perform `nslookup` (or `ping`) on:
++ Add a firewall rule on [Azure Cosmos DB](/azure/cosmos-db/how-to-configure-firewall) or [Azure SQL](/azure/azure-sql/database/firewall-configure) to accept connections from the IP address.
 
-+ `stamp2.ext.search.windows.net`, which is the domain of the traffic manager for the Azure public cloud.
-+ `stamp2.ext.search.azure.us` for Azure Government cloud.
+This section explains how to get the IP address used by the wizard.
+
+1. Open a command line tool
+
+1. Perform `nslookup` (or `ping`) on:
+
+   + `stamp2.ext.search.windows.net`, which is the domain of the traffic manager for the Azure public cloud.
+   + `stamp2.ext.search.azure.us` for Azure Government cloud.
 
 For nslookup, the IP address is visible in the "Non-authoritative answer" portion of the response. In the following example, the IP address that you should copy is `52.252.175.48`.
 
@@ -96,17 +102,14 @@ Aliases:  stamp2.ext.search.windows.net
           azspncuux.management.search.windows.net
 ```
 
-The IP address in the `Address` field (52.252.175.48 in this example) is the value to add to your firewall rules.
+The IP address in the `Address` field (52.252.175.48 in this example) is the value to add to your firewall rules for legacy wizard connections.
 
 **Reference:** [nslookup command](/windows-server/administration/windows-commands/nslookup)
 
-When services run in different regions, they connect to different traffic managers. Regardless of the domain name, the IP address returned from the ping is the correct one to use when defining an inbound firewall rule for the Azure portal in your region.
-
-For ping, the request times out, but the IP address is visible in the response. For example, in the message `"Pinging azsyrie.northcentralus.cloudapp.azure.com [52.252.175.48]"`, the IP address is `52.252.175.48`.
-
-A banner informs you that IP rules affect the Azure portal experience. This banner remains visible even after you add the Azure portal's IP address. Remember to wait several minutes for network rules to take effect before testing.
-
-:::image type="content" source="media/service-configure-firewall/restricted-access.png" alt-text="Screenshot showing the restricted access banner." lightbox="media/service-configure-firewall/restricted-access.png" :::
+> [!NOTE]
+> You can use [ping](/windows-server/administration/windows-commands/ping) instead of nslookup for this task. For ping, the request times out, but the IP address is visible in the response. For example, in the message `"Pinging azsyrie.northcentralus.cloudapp.azure.com [52.252.175.48]"`, the IP address is `52.252.175.48`.
+>
+> If services run in different regions, they connect to different traffic managers. Regardless of the domain name, the IP address returned from the ping is the correct one to use when defining an inbound firewall rule for the Azure portal in your region.
 
 ## Grant access to trusted Azure services
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイアウォール設定手順の改善"
}
```

### Explanation
この変更は、`service-configure-firewall.md`ファイルに対して行われ、Azure AI Searchサービスにおけるファイアウォールの設定手順が改善されています。主な変更点は以下の通りです：

1. **日付の更新**: ドキュメントの日付が2026年1月22日から2026年1月29日に変更されました。

2. **Azureポータルの接続方法の明確化**: Azureポータルが利用するクライアントIPアドレスに関して詳細な説明が追加されました。クライアントが許可されたIPリストに含まれている場合、ポータル機能を特別な設定なしで使用できると明示されていますが、レガシーインポートウィザードの特例が設定されています。

3. **レガシーインポートウィザードのIPアドレス取得の手順**: レガシーウィザードによる接続で使用されるIPアドレスの取得方法が具体的に記述され、コマンドラインツールを使用して`nslookup`や`ping`を実行する手順が詳しく説明されています。また、Azure Cosmos DBやAzure SQLに接続許可を与えるためのファイアウォールルールの追加も強調されています。

4. **注意点の強調**: 注意書きが追加され、`ping`コマンドを使用することができることや、地域ごとに異なるトラフィックマネージャに接続する際の注意点が説明されています。

これらの変更により、ユーザーはAzureポータルを通じての接続設定やファイアウォールの設定をより効果的に行えるようになります。特に、レガシーウィザードの使用時に必要なIPアドレス情報が明確になることで、対応がスムーズになります。

## articles/search/vector-search-overview.md{#item-56e5fa}

<details>
<summary>Diff</summary>
````diff
@@ -87,7 +87,7 @@ Azure AI Search is deeply integrated across the Azure AI platform. The following
 |---------|-------------|
 | Azure OpenAI | Azure OpenAI provides embedding models and chat models. Demos and samples target the [text-embedding-ada-002](/azure/ai-services/openai/concepts/models#embeddings-models) model. We recommend Azure OpenAI for generating embeddings for text. |
 | Foundry Tools | [Image Retrieval Vectorize Image API](/azure/ai-services/computer-vision/how-to/image-retrieval#call-the-vectorize-image-api) supports vectorization of image content. We recommend this API for generating embeddings for images. |
-| Foundry Agent Service | In Azure AI Search, you can create an *indexed [knowledge source](agentic-knowledge-source-overview.md)* that points to a search index containing vector fields and a vectorizer. You can then parent the knowledge source to a *[knowledge base](agentic-retrieval-how-to-create-knowledge-base.md)* and [connect the knowledge base to Foundry Agent Service](/azure/ai-foundry/agents/how-to/tools/knowledge-retrieval), providing your agents with vector search results for enhanced knowledge retrieval. |
+| Foundry Agent Service | In Azure AI Search, you can create an *indexed [knowledge source](agentic-knowledge-source-overview.md)* that points to a search index containing vector fields and a vectorizer. You can then parent the knowledge source to a *[knowledge base](agentic-retrieval-how-to-create-knowledge-base.md)* and [connect the knowledge base to Foundry Agent Service](/azure/ai-foundry/agents/how-to/foundry-iq-connect), providing your agents with vector search results for enhanced knowledge retrieval. |
 | Azure data platforms: Azure Blob Storage, Azure Cosmos DB, Azure SQL, Microsoft OneLake | You can use [indexers](search-indexer-overview.md) to automate data ingestion, and then use [integrated vectorization](vector-search-integrated-vectorization.md) to generate embeddings. Azure AI Search can automatically index vector data from [Azure blob indexers](search-how-to-index-azure-blob-storage.md), [Azure Cosmos DB for NoSQL indexers](search-how-to-index-cosmosdb-sql.md), [Azure Data Lake Storage Gen2](search-how-to-index-azure-data-lake-storage.md), [Azure Table Storage](search-how-to-index-azure-tables.md), and [Microsoft OneLake](search-how-to-index-onelake-files.md). For more information, see [Add vector fields to a search index](vector-search-how-to-create-index.md). |
 
 It's also commonly used in open-source frameworks like [LangChain](https://js.langchain.com/docs/integrations/vectorstores/azure_aisearch).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Foundry Agent Serviceのリンクを更新"
}
```

### Explanation
この変更は、`vector-search-overview.md`ファイルに対して行われ、Azure AI SearchにおけるFoundry Agent Serviceの説明が改善されています。主な変更点は以下の通りです：

1. **リンクの修正**: Foundry Agent Serviceに関連する説明の中で、知識ベースをFoundry Agent Serviceに接続するためのリンクが更新されました。具体的には、以前は`/azure/ai-foundry/agents/how-to/tools/knowledge-retrieval`へのリンクが使用されていましたが、現在は`/azure/ai-foundry/agents/how-to/foundry-iq-connect`に変更され、より正確な情報にリダイレクトされるようになりました。

2. **文章の整合性**: 内容自体は変更されていませんが、リンクの更新により、ユーザーが最新の手順や情報に基づいて知識ベースをFoundry Agent Serviceに接続する方法を理解しやすくなっています。

これにより、Azure AI Searchを利用する際のユーザーエクスペリエンスが向上し、リソースや機能へのアクセスが円滑になることが期待されます。特に、正確な情報に基づいた設定が促進されることで、エージェントによる知識取得が強化されます。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ Learn about the latest updates to Azure AI Search functionality, docs, and sampl
 | [Knowledge sources (preview)](agentic-knowledge-source-overview.md) | New types of knowledge sources: [indexed OneLake](agentic-knowledge-source-how-to-onelake.md), [indexed SharePoint](agentic-knowledge-source-how-to-sharepoint-indexed.md), [remote SharePoint](agentic-knowledge-source-how-to-sharepoint-remote.md), and [web](agentic-knowledge-source-how-to-web.md). For indexed knowledge sources, the new `ingestionParameters` object provides properties to control content ingestion and processing, including `contentExtractionMode` for use of the [Azure Content Understanding skill](cognitive-search-skill-content-understanding.md) and `ingestionPermissionOptions` for use of ACLs in the generated indexer. |
 | [Knowledge retrieval (preview)](agentic-retrieval-how-to-retrieve.md) | Execute retrieval operations with support for [reasoning effort](agentic-retrieval-how-to-set-retrieval-reasoning-effort.md), zero-model-call mode for efficiency, and partial responses. |
 | [Portal support for knowledge sources and knowledge bases (preview)](get-started-portal-agentic-retrieval.md) | Use the Azure portal to create and manage knowledge sources and knowledge bases, with a new chat playground for sending retrieval requests. These portal-generated objects use the 2025-08-01-preview schema and have breaking changes with the 2025-11-01-preview. For help with migration, see [Migrate your agentic retrieval code](agentic-retrieval-how-to-migrate.md). |
-| [Foundry IQ (preview)](/azure/ai-foundry/agents/how-to/tools/knowledge-retrieval) | New integration that allows agents in Foundry Agent Service to invoke knowledge bases in Azure AI Search. Foundry IQ offloads complex retrieval operations to the knowledge base, enabling the agent to provide accurate, citation-backed responses based on enterprise data and web sources. |
+| [Foundry IQ (preview)](/azure/ai-foundry/agents/concepts/what-is-foundry-iq) | New integration that allows agents in Foundry Agent Service to invoke knowledge bases in Azure AI Search. Foundry IQ offloads complex retrieval operations to the knowledge base, enabling the agent to provide accurate, citation-backed responses based on enterprise data and web sources. |
 | [Azure Content Understanding skill (preview)](cognitive-search-skill-content-understanding.md) | New skill that wraps Azure Content Understanding in Foundry Tools to extract structured Markdown from text, images, PDFs, Microsoft PowerPoint, Microsoft Word, and more. This skill provides advanced document parsing with better table extraction (including cross-page tables), image descriptions, and semantic chunking. For indexed knowledge sources, this skill is available through the `contentExtractionMode` property within `ingestionParameters`. |
 | [SharePoint indexer ACL support (preview)](search-indexer-sharepoint-access-control-lists.md) | Extended ACL support to flow basic SharePoint permissions to indexed documents, enabling document-level access control. |
 | [Elevated read permissions for ACLs (preview)](search-query-access-control-rbac-enforcement.md#elevated-permissions-for-investigating-incorrect-results) | New capability to assign elevated read permissions to administrators for investigating problems with ACL configurations used in document access control. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Foundry IQのリンクを更新"
}
```

### Explanation
この変更は、`whats-new.md`ファイルに対して行われ、Azure AI Searchの新機能に関する情報が改善されています。主な変更点は以下の通りです：

1. **リンクの修正**: Foundry IQに関連する情報へのリンクが更新されました。以前は`/azure/ai-foundry/agents/how-to/tools/knowledge-retrieval`へのリンクが使用されていましたが、現在は`/azure/ai-foundry/agents/concepts/what-is-foundry-iq`に変更され、ユーザーがFoundry IQの概念を理解するのに役立つようになっています。

2. **内容の変更なし**: 機能説明自体は同じで、変更はリンクの更新のみです。Foundry IQの統合が、Foundry Agent Service内のエージェントがAzure AI Searchの知識ベースを呼び出すことを可能にし、複雑な検索操作を知識ベースにオフロードすることで、正確で引用に基づく応答を提供することが説明されています。

これにより、Azure AI Searchにおける新機能に関する情報がより正確になり、ユーザーが必要なリソースへ迅速にアクセスできるようになります。リンクの更新は、ユーザーが最新の情報を得るために重要であり、全体的なドキュメントの整合性を促進します。


