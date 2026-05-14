---
date: '2026-05-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2da7446...MicrosoftDocs:9027b1b
summary: この変更では、Azure AI Search関連のドキュメント内のリンクや情報を更新し、ユーザーが最新の情報にアクセスしやすくすることを目指しています。新機能の追加はありませんが、既存機能やリンクの改善が行われました。目立った破壊的変更はなく、リンクの修正や情報の明確化を通じて、ユーザーが適切なリソースにアクセスできるようにしています。この変更は、Azure
  AI Searchのドキュメントを精緻化し、特にエンタープライズ環境でのユーザーエクスペリエンスを向上させる重要なステップです。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2da7446...MicrosoftDocs:9027b1b){target="_blank"}

<format>
# ハイライト
この変更では、Azure AI Search関連のドキュメント内のリンクや情報を更新することで、ユーザーが最新の情報にアクセスしやすくすることを目的としています。様々なモジュールでURLの修正や情報の明確化が含まれています。

## 新機能
特に新機能の追加はありませんが、既存機能やリンクの改善が目立ちます。

## 破壊的変更
特に目立った破壊的変更は存在しません。

## その他の更新
- 「ハイブリッド検索の概要」におけるリンクの修正
- JavaおよびPythonサンプルドキュメントのリンク更新
- Blobインデクサー、機密ラベルに関するドキュメントの更新
- セマンティックおよびベクトル検索概要におけるリンクの修正
- 新機能セクションでのリンクの更新

# インサイト
この変更は、主に技術ドキュメントのURLや特定の機能に関連するドキュメントの更新と修正です。具体的には、ユーザーが適切なリソースにアクセスできるようにするため、いくつかのURLが新しいものに差し替えられています。これは、Azure AI Searchの利用者が最新の情報に基づいた環境で操作を行うために重要です。

変更には、ベース情報の更新、使用に関する注意事項の明確化、リンクの修正といったマイナーアップデートが含まれており、特にインデクサーや機密ラベルに関する詳細が追加されました。これにより、実際の使用シナリオで発生しうる問題点の理解が深まり、ユーザーがそれらの問題を回避する助けとなります。

URLの修正は、古いリソースから最新のリソースへのシフトを示し、それによって、時間が経つにつれて進化するテクノロジーに対してドキュメントが正確なものとなるようにしています。ドキュメントのリンクや情報が誤っている場合、ユーザーは誤った情報に基づいてアクションを起こしてしまう可能性があるため、このような更新はWebサービスの運営において不可欠です。

全体として、この変更はAzure AI Searchのドキュメントを精緻化し、ユーザーエクスペリエンスを向上させるための重要な一歩であり、特にエンタープライズ環境での実用性をさらに飛躍させるものです。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [hybrid-search-overview.md](#item-6987b4) | minor update | ハイブリッド検索の概要におけるリンクの修正 | modified | 1 | 1 | 2 | 
| [samples-java.md](#item-5992fd) | minor update | Java サンプルドキュメントのパッケージダウンロードリンクの更新 | modified | 1 | 1 | 2 | 
| [samples-python.md](#item-d2bf09) | minor update | Python サンプルドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [search-blob-indexer-role-based-access.md](#item-887e42) | minor update | Azure AI Search の Blob インデクサーに関するドキュメントの更新 | modified | 17 | 2 | 19 | 
| [search-indexer-sensitivity-labels.md](#item-2a7bfc) | minor update | Azure AI Search インデクサーの機密ラベルに関するドキュメントの更新 | modified | 5 | 5 | 10 | 
| [search-query-sensitivity-labels.md](#item-3e1f8a) | minor update | Azure AI Search のクエリ時の機密ラベルに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [semantic-search-overview.md](#item-b7497b) | minor update | セマンティック検索の概要に関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [vector-search-overview.md](#item-56e5fa) | minor update | ベクトル検索の概要に関するリンクの修正 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-fa71b4) | minor update | 新機能に関するリンク先の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/hybrid-search-overview.md{#item-6987b4}

<details>
<summary>Diff</summary>
````diff
@@ -140,4 +140,4 @@ A response from the query might look like the following JSON.
 
 + [Create a hybrid query](hybrid-search-how-to-query.md)
 + [Relevance scoring in hybrid search](hybrid-search-ranking.md)
-+ [Outperform vector search with hybrid retrieval and ranking (Tech blog)](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-outperforming-vector-search-with-hybrid/ba-p/3929167)
++ [Outperform vector search with hybrid retrieval and ranking (Tech blog)](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/azure-ai-search-outperforming-vector-search-with-hybrid-retrieval-and-reranking/3929167)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索の概要におけるリンクの修正"
}
```

### Explanation
この変更は、ハイブリッド検索の概要に関するドキュメント内のリンクの更新を目的としています。具体的には、既存のリンクに対して、ハイブリッド検索におけるランキングの詳細情報を提供する新しいURLへの修正が行われました。変更された内容は、元のテクニカルブログのURLを改善されたアドレスに置き換える形で反映されています。

変更の詳細としては、1つの行が追加され、1つの行が削除されています。これにより、ユーザーが最新の情報にアクセスできるようにし、ハイブリッド検索機能の有用性を高める目的があります。これらの変更は小さなアップデートに分類され、全体のコンテンツの精度と関連性を保つために重要です。

## articles/search/samples-java.md{#item-5992fd}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ Learn about Java code samples that demonstrate the functionality and workflow of
 
 | Target | Link |
 |--|--|
-| Package download | [search.maven.org/artifact/com.azure/azure-search-documents](https://search.maven.org/artifact/com.azure/azure-search-documents) |
+| Package download | [search.maven.org/artifact/com.azure/azure-search-documents](https://central.sonatype.com/artifact/com.azure/azure-search-documents) |
 | API reference | [com.azure.search.documents](/java/api/com.azure.search.documents)  |
 | API test cases | [github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents/src/test](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents/src/test) |
 | Source code | [github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/search/azure-search-documents)  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java サンプルドキュメントのパッケージダウンロードリンクの更新"
}
```

### Explanation
この変更は、Javaのサンプルコードを紹介するドキュメント内のパッケージダウンロードリンクを更新するために行われました。具体的には、以前のリンクである「search.maven.org」から、より新しいリポジトリである「central.sonatype.com」への変更が適用されました。

変更された内容は1つの行が追加され、1つの行が削除されており、全体のコンテンツの正確性と信頼性を向上させることが目的です。この修正により、ユーザーは最新のパッケージに簡単にアクセスできるようになり、Java SDKの効果的な利用を促進します。全体として、この変更は小さなアップデートとして位置付けられます。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -53,7 +53,7 @@ A demo repo provides proof-of-concept source code for examples or scenarios show
 | Sample | Description |
 |--|--|
 | [azure-search-vector-samples](https://github.com/Azure/azure-search-vector-samples/blob/main) | Comprehensive collection of samples for vector search scenarios, organized by scenario or technology. |
-| [azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main) | ChatGPT-like experience over enterprise data with Azure OpenAI Python code showing how to use Azure AI Search with large language models in Azure OpenAI. For background, see this [blog post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/revolutionize-your-enterprise-data-with-chatgpt-next-gen-apps-w-azure-openai-and/3762087). |
+| [azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main) | ChatGPT-like experience over enterprise data with Azure OpenAI Python code showing how to use Azure AI Search with large language models in Azure OpenAI. For background, see this [blog post](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/revolutionize-your-enterprise-data-with-chatgpt-next-gen-apps-w-azure-openai-and/3762087). |
 | [aisearch-openai-rag-audio](https://github.com/Azure-Samples/aisearch-openai-rag-audio) | "Voice to RAG." This sample demonstrates a simple architecture for voice-based generative AI applications that enables Azure AI Search RAG on top of the real-time audio API with full-duplex audio streaming from client devices. It also securely handles access to both the model and the retrieval system. Backend code is written in Python, while frontend code is written in JavaScript. For an introduction, watch this [video](https://www.youtube.com/watch?v=vXJka8xZ9Ko). |
 
 ## Other samples
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python サンプルドキュメントのリンク修正"
}
```

### Explanation
この変更は、Pythonのサンプルコードに関するドキュメント内の特定のリンクを修正することを目的としています。具体的には、Azure OpenAI デモに関連する部分で、元のリンクから新しいブログ投稿へのリンクが適用されました。これにより、情報の正確性と関連性が保たれています。

変更の内容としては、1つの行が追加され、1つの行が削除されています。この修正により、ユーザーはAzure AI Searchと大規模言語モデルの使用に関する最新情報を得ることができ、特にChatGPTのような体験を通じて、エンタープライズデータの活用がさらに促進されることを目指しています。このように、全体として小さなアップデートとして位置づけられる変更であり、ドキュメントの整合性を高める重要な役割を果たしています。

## articles/search/search-blob-indexer-role-based-access.md{#item-887e42}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to configure Azure AI Search knowledge sources and indexe
 ms.reviewer: vaishalishah
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 04/24/2026
+ms.date: 05/12/2026
 ms.custom:
   - dev-focus
 ai-usage: ai-assisted
@@ -43,7 +43,22 @@ This article focuses on the indexing automation approaches, built on this founda
 
 + You should understand how indexers and knowledge sources work and how to create an index. This article explains the configuration settings for the data source and indexer, but doesn't provide steps for creating the index. For more information about indexes designed for permission filters, see [Create an index with permission filter fields](search-index-access-control-lists-and-rbac-push-api.md#create-an-index-with-permission-filter-fields).
 
-+ This functionality isn't currently supported in the Azure portal, which includes permission filters created through the [**Import data** wizard](search-import-data-portal.md). Use a programmatic approach to create or modify existing objects for document-level access. 
+## Limitations
+
++ The Azure portal doesn't support this feature.
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
+
 
 ## Configure Blob Storage
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search の Blob インデクサーに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるBlobインデクサーの役割に関連するドキュメントを更新することを目的としています。具体的には、文書の日付更新に加えて、インデクサーや知識ソースの機能に関する新しい制限事項が追加されました。

変更された内容には、インデクサーと知識ソースの基本的な理解を促すための説明が含まれ、パーミッションフィルターを使用したインデックス作成に関する参考リンクが提供されています。また、この機能がAzureポータルではサポートされていないことが明記され、特定のインデクサー機能がADLS Gen2から派生した文書に対してパーミッションの継承をサポートしていないことが警告されています。これにより、ユーザーはインデクサーの使用に際しての重要な制限事項を理解できるようになっています。

全体として、この修正は情報の明確化を図るためのものであり、ユーザーにとって重要な利用上の注意点を強調しています。

## articles/search/search-indexer-sensitivity-labels.md{#item-2a7bfc}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to configure Azure AI Search indexers to ingest Microsoft
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 03/05/2026
+ms.date: 05/12/2026
 ---
 
 # Use an Azure AI Search indexer to ingest Microsoft Purview sensitivity labels and enforce document-level security
@@ -141,9 +141,9 @@ $managedIdentityObjectId = (Get-AzResource -ResourceId $resourceIdWithManagedIde
 $MIPResourceSP = Get-EntraServicePrincipal -Filter "appID eq '870c4f2e-85b6-4d43-bdda-6ed9a579b725'"
 New-EntraServicePrincipalAppRoleAssignment -ServicePrincipalId $managedIdentityObjectId -Principal $managedIdentityObjectId -ResourceId $MIPResourceSP.Id -Id "8b2071cd-015a-4025-8052-1c0dba2d3f64"
 
-# ARM Service Principal for policy read
-$ARMSResourceSP = Get-EntraServicePrincipal -Filter "appID eq '00000012-0000-0000-c000-000000000000'"
-New-EntraServicePrincipalAppRoleAssignment -ServicePrincipalId $managedIdentityObjectId -Principal $managedIdentityObjectId -ResourceId $ARMSResourceSP.Id -Id "7347eb49-7a1a-43c5-8eac-a5cd1d1c7cf0"
+# Microsoft Rights Management Services (MRMS) - Service Principal for policy read
+$MRMSResourceSP = Get-EntraServicePrincipal -Filter "appID eq '00000012-0000-0000-c000-000000000000'"
+New-EntraServicePrincipalAppRoleAssignment -ServicePrincipalId $managedIdentityObjectId -Principal $managedIdentityObjectId -ResourceId $MRMSResourceSP.Id -Id "7347eb49-7a1a-43c5-8eac-a5cd1d1c7cf0"
 
 ```
 
@@ -152,7 +152,7 @@ The appID roles in the provided PowerShell script are associated to the followin
 | AppID                                  | Service Principal                      | 
 | -------------------------------------- | -------------------------------------- | 
 | `870c4f2e-85b6-4d43-bdda-6ed9a579b725` | Microsoft Info Protection Sync Service | 
-| `00000012-0000-0000-c000-000000000000` | Azure Resource Manager            | 
+| `00000012-0000-0000-c000-000000000000` | Microsoft Rights Management Services   | 
 
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search インデクサーの機密ラベルに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchのインデクサーを使用してMicrosoft Purviewの機密ラベルを取り込む方法に関するドキュメントを更新することを目的としています。主な改訂点として、文書の日付の更新に加え、PowerShellスクリプト内のコメント及び変数名の明確化が行われました。

具体的には、「ARM Service Principal for policy read」という記述が「Microsoft Rights Management Services (MRMS) - Service Principal for policy read」に変更され、より正確なコンテキストが提供されるように修正されています。また、これに伴い、関連する変数名も整合性を持たせるように変更されています。これにより、ユーザーはAzure AI Searchにおけるサービスプリンシパルの役割をより明確に理解できるようになります。

この修正は、ドキュメントの情報の正確性を高め、利用者がスクリプトを効果的に活用できるように配慮されています。全体として、重要な内容が若干の修正を経てクリアに伝わるようになった「マイナーアップデート」となります。

## articles/search/search-query-sensitivity-labels.md{#item-3e1f8a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how query-time enforcement of Microsoft Purview sensitivity l
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 05/04/2026
+ms.date: 05/12/2026
 ai-usage: ai-assisted
 ---
 
@@ -47,7 +47,7 @@ When you query an index that includes Microsoft Purview sensitivity labels, Azur
 ### 1. User identity and application role input
 
 At query time, Azure AI Search validates both:
-- The calling application's RBAC role, provided in the `Authorization` header.  
+- The calling application's RBAC role, provided in the `Authorization` header.  The minimum required role is `Search Index Data Reader`. For more details, review the [Azure AI Search RBAC guide](search-security-rbac.md).
 - The user identity via token, provided in the `x-ms-query-source-authorization` header.  
 
 Both are required to authorize label-based visibility.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Search のクエリ時の機密ラベルに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるクエリ時のMicrosoft Purview機密ラベルの適用に関するドキュメントを更新するもので、主に情報の明確化を目的としています。具体的には、文書の日付が更新され、RBAC（Role-Based Access Control）に関する要件が詳述されました。

更新内容には、クエリ時における認証の要件として、呼び出しアプリケーションのRBAC役割について説明が追加されています。この中で、最小限必要な役割として「Search Index Data Reader」が明示され、さらに「Azure AI Search RBACガイド」を参照するように促されています。これにより、ユーザーは機密ラベルに対する適切な権限を把握しやすくなります。

全体として、この修正は利用者が必要な権限を理解しやすくするためのものであり、情報の正確性と明確さを高めるためのマイナーな更新となっています。

## articles/search/semantic-search-overview.md{#item-b7497b}

<details>
<summary>Diff</summary>
````diff
@@ -150,4 +150,4 @@ Charges for semantic ranker occur when query requests include `queryType=semanti
 
 ## Related content
 
-* [Blog: Outperforming vector search with hybrid retrieval and ranking capabilities](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-outperforming-vector-search-with-hybrid/ba-p/3929167)
+* [Blog: Outperforming vector search with hybrid retrieval and ranking capabilities](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/azure-ai-search-outperforming-vector-search-with-hybrid-retrieval-and-reranking/3929167)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティック検索の概要に関するドキュメントのリンク修正"
}
```

### Explanation
この変更は、Azure AI Searchの「セマンティック検索の概要」に関するドキュメントの関連コンテンツのリンクを更新することを目的としています。具体的には、リンク先のURLが修正され、新しいブログのURLが指定されています。

元々のリンクは、セマンティック検索のハイブリッドな取得とランキング機能についての情報を提供していましたが、更新されたリンクは、同じテーマである「セマンティック検索を用いたハイブリッド取得と再ランキング」の情報を提供するためのものです。この修正により、利用者は最新かつ正確なリソースにアクセスできるようになり、関連する情報をより簡単に見つけられるようになります。

全体的に、この修正は文書の正確性と有用性を向上させるためのものであり、マイナーな更新として位置づけられるものです。

## articles/search/vector-search-overview.md{#item-56e5fa}

<details>
<summary>Diff</summary>
````diff
@@ -96,4 +96,4 @@ It's also commonly used in open-source frameworks like [LangChain](https://js.la
 + [Create a vector index](vector-search-how-to-create-index.md)
 + [Create a vector query](vector-search-how-to-query.md)
 + [azure-vector-search-samples](https://github.com/Azure-Samples/azure-vector-search-samples)
-+ [Azure Cognitive Search and LangChain: A Seamless Integration for Enhanced Vector Search Capabilities](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-and-langchain-a-seamless-integration-for/ba-p/3901448)
++ [Azure Cognitive Search and LangChain: A Seamless Integration for Enhanced Vector Search Capabilities](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/azure-cognitive-search-and-langchain-a-seamless-integration-for-enhanced-vector-/3901448)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索の概要に関するリンクの修正"
}
```

### Explanation
この変更は、Azure AI Searchに関する「ベクトル検索の概要」ドキュメント内の関連リンクを修正することを目的としています。具体的には、ブログのURLが新しい形式に更新されています。

元のリンクは「Azure Cognitive SearchとLangChainの統合」に関するブログ記事を指していましたが、更新されたリンクは同じ内容をより明確に表現する新しいURLに変更されています。これにより、利用者は最新の情報にアクセスしやすくなり、適切なリソースを見つけることが可能になります。

加えて、他の関連リソースへのリンクも追加されており、ユーザーはベクトルインデックスの作成やクエリ方法についての情報、Azureのサンプルコードへのリンクも利用できるようになります。全体として、この更新は文書の情報をより正確で便利なものにするためのマイナーな調整です。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -120,7 +120,7 @@ Learn about the latest updates to Azure AI Search functionality, docs, and sampl
 | March | Queries | [Semantic ranker prerelease models (preview)](semantic-how-to-configure.md#opt-in-for-prerelease-semantic-ranking-models). Opt in to use prerelease semantic ranker models if one happens to be available in your region. Available in [Create or Update Index (2025-03-01-preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2025-03-01-preview&preserve-view=true#semanticconfiguration).|
 | March | REST API | [Search Service REST 2025-03-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-03-01-preview&preserve-view=true). Preview release of REST APIs for data plane operations. Adds support for multi-vector embeddings, hierarchical facets, facet aggregation, and facet filters. |
 | March | REST API | [Search Management 2025-02-01-preview](/rest/api/searchmanagement/operation-groups?view=rest-searchmanagement-2025-02-01-preview&preserve-view=true). Preview release of REST APIs for control plane operations. Adds support for in-place upgrade to higher capacity partitions, in-place upgrade to higher tiers, and Azure Confidential Compute. |
-| April | Demo | [RAG Time Journey](https://github.com/microsoft/rag-time). Code and video demonstrations of Retrieval Augmented Generation (RAG) workflows that use Azure AI Search. Segments include fundamentals, patterns and use-cases, [vector indexing at scale](https://github.com/microsoft/rag-time/tree/main/Journey%203%20-%20Optimize%20your%20Vector%20Index%20for%20Scale), and [agentic search](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/bonus-rag-time-journey-agentic-rag/4404652) where you use an agent to evaluate a result and generate a better answer. |
+| April | Demo | [RAG Time Journey](https://github.com/microsoft/rag-time). Code and video demonstrations of Retrieval Augmented Generation (RAG) workflows that use Azure AI Search. Segments include fundamentals, patterns and use-cases, [vector indexing at scale](https://github.com/microsoft/rag-time/tree/main/Journey%203%20-%20Optimize%20your%20Vector%20Index%20for%20Scale), and [agentic search](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/bonus-rag-time-journey-agentic-rag/4404652) where you use an agent to evaluate a result and generate a better answer. |
 | February | Security | [Customer-managed keys support for Managed HSM](search-security-manage-encryption-keys.md). Use either Azure Key Vault or Azure Key Vault Managed HSM (Hardware Security Module) to store customer-managed keys for extra encryption of sensitive content. |
 
 ## Previous year's announcements
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能に関するリンク先の修正"
}
```

### Explanation
この変更は、Azure AI Searchの「新機能」に関するドキュメントの一部で、デモセクションにあるリンクを更新することが目的です。具体的には、「RAG Time Journey」というデモのリンクが新しいURLに変更されています。

元のリンクは、Retrieval Augmented Generation (RAG)のワークフローを解説するリソースを指し示していましたが、更新後のリンクは同じデモをより明確に示す情報を提供するためのものです。これにより、利用者は最新のデモや関連資料に容易にアクセスできるようになります。

全体的に、この修正は文書内の情報を最新のものに保つためのマイナーな更新であり、特にURLの変更により、ユーザーが必要な情報に迅速にたどり着けるようになっています。


