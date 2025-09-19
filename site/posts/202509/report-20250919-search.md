---
date: '2025-09-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fdfd403...MicrosoftDocs:bb45dff
summary: この更新では、Azure Cognitive Searchに関連するいくつかのドキュメントが軽微にアップデートされました。新しくGPT-5モデルの`temperature`パラメータに関する説明が追加され、複数の画像ファイルが更新されました。また、役割ベースアクセス（RBAC）に関するドキュメントの内容や日付も最新化されました。特に重大な互換性の問題や破壊的変更はありません。これらの変更は、読者とエンドユーザーに対して最新で正確な情報を提供することを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fdfd403...MicrosoftDocs:bb45dff){target="_blank"}

<format>
# Highlights
この更新では、Azure Cognitive Searchに関連する複数のドキュメントが軽微にアップデートされました。主な変更点として、新しいGPT-5モデルの`temperature`パラメータの説明追加、複数の画像ファイルのアップデート、および役割ベースアクセス（RBAC）に関するドキュメントの内容及び日付の最新化があります。

## New features
- 新しいGPT-5モデルにおける`temperature`パラメータの説明が追加。

## Breaking changes
- 特に重大な互換性の問題や破壊的変更は含まれません。

## Other updates
- 複数のドキュメンテーションの日付や情報の明確化。
- クイックスタート・ウィザードやインポートウィザードに関連する画像ファイルを更新し、視覚的最新性を確保。
- Azureポータルでのサポート状況に関する情報の追加。

# Insights
このドキュメントにおける変更は、主に読者とエンドユーザーに対して最新かつ正確な情報の提供を増やすことを目的としています。まず、Cognitive Search Skillに関する資料では、新たに導入されたGPT-5モデルの`temperature`パラメータに関する詳細が追加され、ユーザーがこれを理解し、正しく利用できるよう配慮されています。こうした技術説明の追加は、モデルの性能を最適に活かせるようサポートするために重要です。

また、複数の画像ファイルが最新のユーザーインターフェースに合わせて更新されました。このようなビジュアルの整備は、ドキュメンテーションがユーザーにとってより使いやすくなるための重要な要素であり、ユーザー体験の向上に寄与します。

さらに、Azureポータルでサポートされていない機能に関する情報を追加することで、利用者が期待する機能と実際の提供状況のギャップを埋めることを意図しています。特に、RBACに関する文書では、サポート範囲が明示されたことで、ユーザーはサービス利用の際に不必要な混乱を避けられるようになっています。

これらの細かな修正や更新は、技術ドキュメントの精度と最新性、ユーザーエクスペリエンスの向上を目指したものであり、結果としてドキュメントの信頼性を高めることにつながります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-genai-prompt.md](#item-384bf9) | minor update | Cognitive Search Skill GenAI Promptの更新 | modified | 7 | 4 | 11 | 
| [search-get-started-skillset-old-wizard.md](#item-92e6e0) | minor update | クイックスタート・ウィザードのイメージ更新 | modified | 1 | 1 | 2 | 
| [wizard-scenarios-multimodal-rag.png](#item-78df78) | minor update | マルチモーダルRAGウィザードシナリオ画像の更新 | modified | 0 | 0 | 0 | 
| [wizard-scenarios-rag.png](#item-2d3082) | minor update | RAGウィザードシナリオ画像の更新 | modified | 0 | 0 | 0 | 
| [import-data-button.png](#item-296200) | minor update | データインポートボタンの画像の更新 | modified | 0 | 0 | 0 | 
| [import-data-new-button.png](#item-8fa0da) | minor update | 新しいデータインポートボタンの画像の更新 | modified | 0 | 0 | 0 | 
| [import-wizards.png](#item-784058) | minor update | インポートウィザードの画像の更新 | modified | 0 | 0 | 0 | 
| [add-index.png](#item-80036e) | minor update | インデックス追加の画像の更新 | modified | 0 | 0 | 0 | 
| [search-blob-indexer-role-based-access.md](#item-887e42) | minor update | Blobインデクサーの役割ベースアクセスに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [search-index-access-control-lists-and-rbac-push-api.md](#item-45e71e) | minor update | インデックスアクセス制御リストとRBACに関するドキュメントの更新 | modified | 3 | 1 | 4 | 
| [search-indexer-access-control-lists-and-role-based-access.md](#item-67b42f) | minor update | インデクサーによるACLおよびRBACメタデータの取り込みに関するドキュメント更新 | modified | 6 | 4 | 10 | 


# Modified Contents
## articles/search/cognitive-search-skill-genai-prompt.md{#item-384bf9}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2025
 ms.topic: reference
-ms.date: 08/27/2025
+ms.date: 09/18/2025
 ---
 
 # GenAI Prompt skill
@@ -35,11 +35,13 @@ The GenAI Prompt skill is available in the [latest preview REST API](/rest/api/s
 
 ## Supported models
 
-You can use any [chat completion inference model](/azure/ai-foundry/model-inference/concepts/models) deployed in AI Foundry, such as GPT models, Deepseek R#, Llama-4-Mavericj, Cohere-command-r, and so forth.
+- You can use any [chat completion inference model](/azure/ai-foundry/model-inference/concepts/models) deployed in AI Foundry, such as GPT models, Deepseek R#, Llama-4-Mavericj, Cohere-command-r, and so forth.
 
-For image verbalization, the model you use to analyze the image determines what image formats are supported.
+- For image verbalization, the model you use to analyze the image determines what image formats are supported.
 
-Billing is based on the pricing of the model you use.
+- For GPT-5 model, the `temperature` parameter is not supported in the same way as previous models. If defined, it must be set to `1.0`, as other values will result in errors.
+
+- Billing is based on the pricing of the model you use.
 
 > [!NOTE]
 > The search service connects to your model over a public endpoint, so there are no region location requirements, but if you're using an all-up Azure solution, you should check the [Azure AI Search regions](search-region-support.md) and the [Azure OpenAI model regions](/azure/ai-services/openai/concepts/models) to find suitable pairs, especially if you have data residency requirements.
@@ -59,6 +61,7 @@ Billing is based on the pricing of the model you use.
 
   - For AI Foundry models, assign [**Azure AI User**](/azure/ai-foundry/concepts/rbac-azure-ai-foundry#azure-ai-user).
 
+
 ## @odata.type  
 
 `#Microsoft.Skills.Custom.ChatCompletionSkill`
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cognitive Search Skill GenAI Promptの更新"
}
```

### Explanation
この変更は、ドキュメント「Cognitive Search Skill GenAI Prompt」に対していくつかのマイナーなアップデートが施されたものです。具体的には、日付の更新や新しいGPT-5モデルにおける`temperature`パラメータの扱いについての説明が追加されました。これにより、GPT-5モデルを使用する際の注意点が明確に示されています。また、全体の構造も整理され、より読みやすい形式に改訂されています。これらの変更は、使用されるモデルや機能に関する最新の情報を反映しています。

## articles/search/includes/quickstarts/search-get-started-skillset-old-wizard.md{#item-92e6e0}

<details>
<summary>Diff</summary>
````diff
@@ -47,7 +47,7 @@ To run the wizard:
 
 1. On the **Overview** page, select **Import data**.
 
-   :::image type="content" source="../../media/search-import-data-portal/import-data-button.png" alt-text="Screenshot of the Import data command." border="true" lightbox="../../media/search-import-data-portal/import-data-button.png":::
+   :::image type="content" source="../../media/search-import-data-portal/import-data-button.png" alt-text="Screenshot of the Import data command." border="true":::
 
 ### Step 1: Create a data source
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタート・ウィザードのイメージ更新"
}
```

### Explanation
この変更は、クイックスタート・ウィザードに関する文書において、イメージの表示設定に関する小さなアップデートを行ったものです。具体的には、画像の表示に関するオプションから「lightbox」設定が削除され、画像は通常の形式で表示されています。この更新により、ユーザーがイメージをよりスムーズに閲覧できるようになっています。全体として、この変更はユーザー体験の向上を目指したものです。

## articles/search/media/search-get-started-portal-images/wizard-scenarios-multimodal-rag.png{#item-78df78}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダルRAGウィザードシナリオ画像の更新"
}
```

### Explanation
この変更は、「マルチモーダルRAGウィザードシナリオ」を示す画像に関連するもので、具体的にはその画像ファイル自体が修正されています。追加や削除は行われておらず、内容に変更はないものの、画像の更新が行われています。この修正により、視覚的要素が最新の情報を反映していることが期待されます。このようなマイナーな更新は、ドキュメンテーション全体の整合性を保つうえで重要です。

## articles/search/media/search-get-started-portal-import-vectors/wizard-scenarios-rag.png{#item-2d3082}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGウィザードシナリオ画像の更新"
}
```

### Explanation
この変更は、「RAGウィザードシナリオ」を示す画像ファイルに関連しています。具体的には、該当する画像が修正されたことによるもので、変更自体には追加や削除はなく、ファイルの内容についても変化はありません。ただし、画像の更新が行われたことで、ドキュメンテーション内のビジュアルが最新の情報を反映していることが期待されます。このようなマイナーな修正は、全体の品質を維持するために重要です。

## articles/search/media/search-import-data-portal/import-data-button.png{#item-296200}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データインポートボタンの画像の更新"
}
```

### Explanation
この変更は、「データインポートボタン」を示す画像ファイルに関するもので、具体的にはその画像が修正されています。追加や削除がなく、内容の変更もないため、主に視覚の改善が目的とされています。画像の更新により、ドキュメンテーションで提供される情報が最新の状況を反映していることが期待されるため、このようなマイナー更新は、ドキュメンテーションの整合性と信頼性を保つために重要です。

## articles/search/media/search-import-data-portal/import-data-new-button.png{#item-8fa0da}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいデータインポートボタンの画像の更新"
}
```

### Explanation
この変更は、「新しいデータインポートボタン」を示す画像ファイルの更新に関連しています。この修正では、追加や削除は行われておらず、ファイルの内容に直接的な変更もありません。ただし、画像の更新により、ドキュメンテーションが最新の状態を反映することが期待されます。このようなマイナーな更新は、ユーザーエクスペリエンスを向上させ、情報の正確性を維持するために重要です。

## articles/search/media/search-import-data-portal/import-wizards.png{#item-784058}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インポートウィザードの画像の更新"
}
```

### Explanation
この変更は、「インポートウィザード」を示す画像ファイルの更新を意味しています。具体的には、ファイル自体には追加や削除、内容の変更はありませんが、画像が新版に差し替えられています。このマイナーな更新は、ドキュメンテーションにおいて使用されるビジュアルコンテンツの整合性を保ち、最新のユーザーインターフェースを反映することを目的としています。これにより、情報の正確性が向上し、利用者にとってより価値のある資料となることが期待されます。

## articles/search/media/search-what-is-an-index/add-index.png{#item-80036e}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックス追加の画像の更新"
}
```

### Explanation
この変更は、「インデックスを追加する」プロセスを視覚的に示した画像ファイルの更新に関するものです。ファイルそのものには新たな追加や削除、内容の変更はありませんが、画像が更新されました。このマイナーな更新によって、文書内でのビジュアルエレメントが最新の情報を反映し、利用者がより理解しやすくなることを目的としています。正確な情報提供は、ドキュメンテーションの品質を向上させ、ユーザーエクスペリエンスを改善するために重要です。

## articles/search/search-blob-indexer-role-based-access.md{#item-887e42}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how to configure Azure AI Search indexers for ingesting Azure Role-Based Access (RBAC) metadata on Azure blobs.
 ms.service: azure-ai-search  
 ms.topic: how-to
-ms.date: 09/01/2025
+ms.date: 09/18/2025
 author: vaishalishah
 ms.author: vaishalishah
 ---  
@@ -39,7 +39,7 @@ The indexer approach is built on this foundation:
 
 + You should understand how indexers work and how to create an index. This article explains the configuration settings for the data source and indexer, but doesn't provide steps for creating the index. For more information about indexes designed for permission filters, see [Create an index with permission filter fields](search-index-access-control-lists-and-rbac-push-api.md#create-an-index-with-permission-filter-fields).
 
-Permission filters aren't supported in the indexers and indexes created through the [Import wizards](search-import-data-portal.md). Use a programmatic approach to create or modify existing objects for document-level access.
++ This functionality is currently not supported in the Azure portal, this includes Permission filters created through the [Import wizards](search-import-data-portal.md). Use a programmatic approach to create or modify existing objects for document-level access. 
 
 ## Configure Blob storage
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Blobインデクサーの役割ベースアクセスに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchのインデクサーによる役割ベースアクセス（RBAC）メタデータの取り込みに関する記事の更新を示しています。具体的には、以下の修正が行われました：

1. **日付の更新**: 文書の日付が「09/01/2025」から「09/18/2025」に変更されました。
2. **情報の明確化**: インデクサーの機能についての説明が改訂され、「この機能は現在Azureポータルではサポートされていない」という文が追加され、Import wizardsを通じて作成される権限フィルタもその対象であることが明記されました。

これにより、読者に対して最新の情報が提供され、特にAzureポータルにおける機能の制限に対する理解が深まることが意図されています。このマイナーな更新は、ドキュメントの正確性と有用性を強化することを目的としています。

## articles/search/search-index-access-control-lists-and-rbac-push-api.md{#item-45e71e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how to use the REST API for indexing documents with ACLs and RBAC metadata.  
 ms.service: azure-ai-search  
 ms.topic: how-to 
-ms.date: 08/27/2025 
+ms.date: 09/18/2025 
 author: admayber
 ms.author: admayber  
 ---  
@@ -43,6 +43,8 @@ This article explains how to use the push REST API to index document-level permi
 
 - Each permissionFilter field should have `filterable` set to true.
 
+- This functionality is currently not supported in the Azure portal.
+
 ## Create an index with permission filter fields
 
 Indexing document ACLs and RBAC metadata with the REST API requires setting up an index schema that enables permission filters and has fields with permission filter assignments.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスアクセス制御リストとRBACに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるアクセス制御リスト（ACL）と役割ベースアクセス（RBAC）のメタデータを使用した文書のインデックス作成に関する記事の更新を示しています。変更内容は以下の通りです：

1. **日付の更新**: 文書の日付が「08/27/2025」から「09/18/2025」に変更されました。
2. **情報の追加**: 現在、Azureポータルにおいてこの機能はサポートされていないという情報が新たに追加されました。これにより、ユーザーが機能の制約を明確に理解できるようになります。

このマイナー更新は、記事の正確性を高め、利用者にとっての理解を深めることを目的としており、最新の情報を反映することで信頼性を向上させています。

## articles/search/search-indexer-access-control-lists-and-role-based-access.md{#item-67b42f}

<details>
<summary>Diff</summary>
````diff
@@ -4,9 +4,9 @@ titleSuffix: Azure AI Search
 description: Learn how to configure Azure AI Search indexers for ingesting Access Control Lists (ACLs) and Azure Role-Based Access (RBAC) metadata on Azure Data Lake Storage (ADLS) Gen2 blobs.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/27/2025  
-author: wlifuture
-ms.author: wli
+ms.date: 09/18/2025  
+author: gmndrg
+ms.author: gimondra
 ---  
 
 # Use an ADLS Gen2 indexer to ingest permission metadata and filter search results based on user access rights
@@ -51,6 +51,8 @@ This article supplements [**Index data from ADLS  Gen2**](search-howto-index-azu
   + [Knowledge store](knowledge-store-concept-intro.md)
   + [Indexer enrichment cache](enrichment-cache-how-to-configure.md)
   + [Debug sessions](cognitive-search-debug-session.md)
+ 
++ This functionality is currently not supported in the Azure portal.
 
 ## Support for the permission model
 
@@ -300,4 +302,4 @@ To effectively manage blob deletion, ensure that you have enabled [deletion trac
 
 + [Connect to Azure AI Search using roles](search-security-rbac.md)
 + [Query-Time ACL and RBAC enforcement](search-query-access-control-rbac-enforcement.md)
-+ [azure-search-python-samples/Quickstart-Document-Permissions-Push-API](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Document-Permissions-Push-API)
\ No newline at end of file
++ [azure-search-python-samples/Quickstart-Document-Permissions-Push-API](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Document-Permissions-Push-API)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサーによるACLおよびRBACメタデータの取り込みに関するドキュメント更新"
}
```

### Explanation
この変更は、Azure AI Searchのインデクサーを使用してアクセス制御リスト（ACL）および役割ベースアクセス（RBAC）メタデータをAzure Data Lake Storage (ADLS) Gen2のブロブに取り込む方法に関する記事の更新を示しています。具体的な変更点は以下の通りです：

1. **日付と著者の更新**: 文書の日付が「08/27/2025」から「09/18/2025」に変更され、著者が「wlifuture」から「gmndrg」に更新され、それに伴い著者名も「wli」から「gimondra」に変更されました。
2. **機能の明確化**: 「この機能は現在Azureポータルではサポートされていない」という文章が追加され、ユーザーが利用できる機能についての理解を深めるよう配慮されました。
3. **内容の追加と修正**: 記事内に新しい情報が追加され、特定のセクションにおいて文言が改善され、リンクが更新されました。

これらの変更は、ドキュメントの最新性を保ち、ユーザーに対して正確な情報を提供することを目的としています。


