---
date: '2024-11-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:567d1b1...MicrosoftDocs:ccb6fcd
summary: このコードの差分は、Azure AI Searchに関連するドキュメントとリソースの更新に関するものです。主な内容は、リダイレクション設定の追加、新しい画像の追加、誤字の修正、およびAPIプレビューやデータソース接続に関する説明の強化です。新たに追加された画像ファイルはセマンティックチャンクingの理解を助け、全体的に文書の品質が向上しています。破壊的変更はなく、多様な更新が行われたことで、ユーザーエクスペリエンスが改善されています。特に情報の正確性とアクセスの容易さが強化され、Azure
  AI Searchの利用者にとってより使いやすい環境が整いました。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:567d1b1...MicrosoftDocs:ccb6fcd){target="_blank"}

# ハイライト

このコードの差分は、Azure AI Searchに関連するドキュメントとリソースの更新に関するものです。特に、リダイレクション設定の追加、新しい画像の追加、誤字の修正、APIプレビューやデータソース接続に関する説明の強化など、複数のファイルにわたってマイナーな更新が行われています。

## 新機能
- `query-results-doc-layout.png` が新たに追加され、ユーザーがセマンティックチャンクingをより理解しやすくするための視覚的補助を提供します。

## 破壊的変更
- 破壊的変更はありませんでした。

## その他の更新
- リダイレクション設定、および検索APIプレビューやセマンティックチャンクingに関する文書の内容が更新されました。
- 誤字の修正によりドキュメントの品質が向上し、特にネットワークセキュリティ境界の文書名が「perimiter」から「perimeter」に変更されました。
- 目次ファイルにおいて、情報構造が整理されました。

# インサイト

この一連のコード更新は、Azure AI Searchに関わるユーザーに対するドキュメントとリソースの充実化を図ったものです。まず、新しい画像ファイルの追加は、視覚情報を通じてトピックの理解を補助するものであり、特に複雑な手法の学習に大いに役立ちます。文書の更新に見られるように、多くの部分で行われた説明の拡充は、Azureの機能を使用する上での疑問を解決し、ユーザーの利便性を高めています。

リダイレクション設定の追加は、検索時のユーザーエクスペリエンスを改善させ、適切な情報へのアクセスが容易になるよう設計されています。これにより、誤ったリダイレクトの回避や、ユーザーの検索行動に即した柔軟な対応が可能になります。

また、誤字の修正や目次の整理も有用です。これは単なる文書の品質向上にとどまらず、ユーザーが必要な情報を迅速に見つけられるようにするための重要なステップです。特に、ネットワークセキュリティ境界に関する情報は企業にとって非常にセンシティブなため、正確な言葉の使用と情報提供が求められます。この変更がセキュリティ設計に関する誤解を減少させ、かつ迅速な対応を促すことにつながるでしょう。

全体的に、これらの変更は、Azure AI Searchの利用者がよりスムーズに諸機能を活用し、最新の情報をもとにセキュアかつ効率的にシステムを運用するための基盤をさらに強固にしたものといえます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [.openpublishing.redirection.search.json](#item-8b66f9) | minor update | リダイレクション設定の更新 | modified | 5 | 0 | 5 | 
| [query-results-doc-layout.png](#item-a661cc) | new feature | 新しい画像の追加 | added | 0 | 0 | 0 | 
| [search-api-preview.md](#item-511f5d) | minor update | 検索 API プレビューに関するドキュメントの修正 | modified | 1 | 1 | 2 | 
| [search-how-to-semantic-chunking.md](#item-4a1d07) | minor update | セマンティックチャンクingに関するドキュメントの改訂 | modified | 67 | 20 | 87 | 
| [search-howto-managed-identities-data-sources.md](#item-edf98d) | minor update | マネージド ID を使用したデータソースへの接続に関するドキュメントの更新 | modified | 19 | 8 | 27 | 
| [search-security-network-security-perimeter.md](#item-49c0d7) | minor update | ネットワークセキュリティ境界に関するドキュメントの名前変更 | renamed | 2 | 2 | 4 | 
| [toc.yml](#item-c4768f) | minor update | 目次ファイルの更新 | modified | 3 | 3 | 6 | 
| [whats-new.md](#item-fa71b4) | minor update | ネットワークセキュリティ境界に関するリンク修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/.openpublishing.redirection.search.json{#item-8b66f9}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,10 @@
 {
     "redirections": [
+        {
+            "source_path_from_root": "/articles/search/search-security-network-security-perimiter.md",
+            "redirect_url": "/azure/search/search-security-network-security-perimeter",
+            "redirect_document_id": true
+        },
         {
             "source_path_from_root": "/articles/search/cognitive-search-quickstart-blob.md",
             "redirect_url": "/azure/search/search-get-started-skillset",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リダイレクション設定の更新"
}
```

### Explanation
このコードの変更は、`search/.openpublishing.redirection.search.json`ファイルに対するマイナーな更新です。この更新では、リダイレクションの設定が追加され、新しいリダイレクションオブジェクトが5行追加されました。具体的には、`source_path_from_root`、`redirect_url`、および`redirect_document_id`を含むリダイレクションエントリが追加され、特に特定のドキュメントへのURLリダイレクションを管理するための情報が提供されています。この更新は、検索機能の改善を図るためのものであり、ユーザーが特定の情報に迅速にアクセスできるようにサポートします。

## articles/search/media/search-how-to-semantic-chunking/query-results-doc-layout.png{#item-a661cc}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい画像の追加"
}
```

### Explanation
このコードの変更は、`search/how-to-semantic-chunking`に関連するドキュメントレイアウトの画像ファイルである`query-results-doc-layout.png`が新たに追加されたことを示しています。この変更は「新機能」として分類され、追加された画像は特定のトピックに関連する視覚的な補足資料として機能します。画像は、ユーザーがセマンティックチャンクingの手法に関する情報を理解しやすくするためのものであり、関連するコンテンツに対する理解を深める役割を果たします。

## articles/search/search-api-preview.md{#item-511f5d}

<details>
<summary>Diff</summary>
````diff
@@ -57,7 +57,7 @@ Preview features are removed from this list if they're retired or transition to
 
 |Feature&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Category | Description | Availability  |
 |---------|------------------|-------------|---------------|
-| [**Network security perimeter**](search-security-network-security-perimiter.md) | Service | Join a search service to a [network security perimeter](/azure/private-link/network-security-perimeter-concepts) to control network access to your search service. | The Azure portal and the [Network Security Perimeter APIs 2024-06-01-preview](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true). |
+| [**Network security perimeter**](search-security-network-security-perimeter.md) | Service | Join a search service to a [network security perimeter](/azure/private-link/network-security-perimeter-concepts) to control network access to your search service. | The Azure portal and the [Network Security Perimeter APIs 2024-06-01-preview](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true). |
 | [**Search service under a user-assigned managed identity**](search-howto-managed-identities-data-sources.md) | Service | Configures a search service to use a previously created user-assigned managed identity. | [Services - Update](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true#identity), 2021-04-01-preview, or the latest preview version. We recommend using the latest preview version. |
 
 ## Preview features in Azure SDKs
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索 API プレビューに関するドキュメントの修正"
}
```

### Explanation
このコードの変更は、`search-api-preview.md`ファイルに対するマイナーな更新を示しています。具体的には、1行の追加と1行の削除が行われ、合計2行の変更が加えられました。この修正の目的は、検索サービスとネットワークセキュリティの境界に関連する機能の説明を明確にし、利用可能性の情報を最新に保つことです。特に「Network security perimeter」機能に関する記述が更新されており、利便性を向上させるための重要な情報が提供されています。この変更は、開発者やユーザーがAzureの検索APIを利用する上で必要な情報を正確かつ最新のものとして保つ手助けをします。

## articles/search/search-how-to-semantic-chunking.md{#item-4a1d07}

<details>
<summary>Diff</summary>
````diff
@@ -1,39 +1,47 @@
 ---
-title: Structure-aware chunking and vectorization
+title: Chunk and vectorize by document layout
 titleSuffix: Azure AI Search
-description: Chunk text content by paragraph or semantically coherent fragment. You can then apply integrated vectorization to generate embeddings and send the results to a searchable index.
+description: Chunk textual content by headings and semantically coherent fragments, generate embeddings, and send the results to a searchable index.
 author: rawan
 ms.author: rawan
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 11/22/2024
 ms.custom:
   - references_regions
   - ignite-2024
 ---
 
-# Structure-aware chunking and vectorization in Azure AI Search
+# Chunk and vectorize by document layout or structure
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-Text data chunking strategies play a key role in optimizing RAG responses and performance. By using the new Document Layout skill that's currently in preview, you can chunk content based on paragraphs or semantically coherent fragments of a sentence representation. These fragments can then be processed independently and recombined as semantic representations without loss of information, interpretation, or semantic relevance. The inherent meaning of the text is used as a guide for the chunking process. 
+Text data chunking strategies play a key role in optimizing RAG responses and performance. By using the new **Document Layout** skill that's currently in preview, you can chunk content based on document structure, capturing headings and chunking the content body based on semantic coherence, such as paragraphs and sentences. Chunks are processed independently. Because LLMs work with multiple chunks, when those chunks are of higher quality and semantically coherent, the overall relevance of the query is improved.
 
-The Document Layout skill uses Markdown syntax (headings and content) to articulate document structure in the search document. The searchable content obtained from your source document is plain text but you can add integrated vectorization to generate embeddings for any field.
+<!-- Text data chunking strategies play a key role in optimizing RAG responses and performance. By using the new **Document Layout** skill that's currently in preview, you can chunk content based on document structure, capturing headings and chunking the content body based on semantic coherence, such as paragraphs and sentences. Chunks are processed independently and recombined as semantic representations. The inherent meaning of the text is used as a guide for the chunking process.  -->
+
+The Document Layout skill calls the [layout model](/azure/ai-services/document-intelligence/prebuilt/layout) in Document Intelligence. The model articulates content structure in JSON using Markdown syntax (headings and content), with fields for headings and content stored in a search index on Azure AI Search. The searchable content produced from the Document Layout skill is plain text but you can apply integrated vectorization to generate embeddings for any field in your source documents, including images.
 
 In this article, learn how to:
 
 > [!div class="checklist"]
-> + Use the Document Layout skill to detect sections and output Markdown content
+> + Use the Document Layout skill to recognize document structure
 > + Use the Text Split skill to constrain chunk size to each markdown section
 > + Generate embeddings for each chunk
 > + Use index projections to map embeddings to fields in a search index
 
+For illustration purposes, this article uses the [sample health plan PDFs](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/health-plan) uploaded to Azure Blob Storage and then indexed using the **Import and vectorize data wizard**.
+
 ## Prerequisites
 
-+ [An indexer-based indexing pipeline](search-indexer-overview.md) with an index that accepts the output.
++ [An indexer-based indexing pipeline](search-indexer-overview.md) with an index that accepts the output. The index must have fields for receiving headings and content.
+
 + [A supported data source](search-indexer-overview.md#supported-data-sources) having text content that you want to chunk.
+
 + [A skillset with Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) that splits documents based on paragraph boundaries.
+
 + [An Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md) that generates vector embeddings.
+
 + [An index projection](search-how-to-define-index-projections.md) for one-to-many indexing.
 
 ## Prepare data files
@@ -42,7 +50,7 @@ The raw inputs must be in a [supported data source](search-indexer-overview.md#s
 
 + Supported file formats include: PDF, JPEG, JPG, PNG, BMP, TIFF, DOCX, XLSX, PPTX, HTML.
 
-+ Supported indexers can be any indexer that can handle the supported file formats. These include [Blob indexers](search-howto-indexing-azure-blob-storage.md), [OneLake indexers](search-how-to-index-onelake-files.md), [File indexers](search-file-storage-integration.md).
++ Supported indexers can be any indexer that can handle the supported file formats. These indexers include [Blob indexers](search-howto-indexing-azure-blob-storage.md), [OneLake indexers](search-how-to-index-onelake-files.md), [File indexers](search-file-storage-integration.md).
 
 + Supported regions for this feature include: East US, West US2, West Europe, North Central US. Be sure to [check this list](search-region-support.md#azure-public-regions) for updates on regional availability.
 
@@ -53,11 +61,13 @@ You can use the Azure portal, REST APIs, or an Azure SDK package to [create a da
 
 ## Create an index for one-to-many indexing
 
-Here's an example payload of a single search document designed around chunks. In this example, parent fields are the text_parent_id. Child fields are the vector and nonvector chunks of the markdown section.
+Here's an example payload of a single search document designed around chunks. Whenever you're working with chunks, you need a chunk field and a parent field that identifies the origin of the chunk. In this example, parent fields are the text_parent_id. Child fields are the vector and nonvector chunks of the markdown section.
 
-You can use the Azure portal, REST APIs, or an Azure SDK to [create an index](search-how-to-load-search-index.md).
+The Document Layout skill outputs headings and content. In this example, `header_1` through `header_3` store document headings, as detected by the skill. Other content, such as paragraphs, is stored in `chunk`. The `text_vector` field is a vector representation of the chunk field content.
 
-An index must exist on the search service before you create the skill set or run the indexer.
+You can use the **Import and vectorize data** wizard in the Azure portal, REST APIs, or an Azure SDK to [create an index](search-how-to-load-search-index.md). The following index is very similar to what the wizard creates by default. You might have more fields if you add image vectorization.
+
+If you aren't using the wizard, the index must exist on the search service before you create the skillset or run the indexer.
 
 ```json
 {
@@ -173,11 +183,17 @@ An index must exist on the search service before you create the skill set or run
 }
 ```
 
-## Define skill set for structure-aware chunking and vectorization
+## Define a skillset for structure-aware chunking and vectorization
+
+Because the Document Layout skill is in preview, you must use the [Create Skillset 2024-11-01-preview](/rest/api/searchservice/skillsets/create?view=rest-searchservice-2024-11-01-preview&preserve-view=true) REST API for this step. You can also use the Azure portal.
+
+This section shows an example of a skillset definition that projects individual markdown sections, chunks, and their vector equivalents as fields in the search index. It uses the [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) to detect headings and populate a content field based on semantically coherent paragraphs and sentences in the source document. It uses the [Text Split skill](cognitive-search-skill-textsplit.md) to split the Markdown content into chunks. It uses the [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md) to vectorize chunks and any other field for which you want embeddings.
 
-Because the Document Layout skill is in preview, you must use the [Create Skillset 2024-11-01-preview](/rest/api/searchservice/skillsets/create?view=rest-searchservice-2024-11-01-preview&preserve-view=true) REST API for this step.
+Besides skills, the skillset includes `indexProjections` and `cognitiveServices`:
 
-Here's an example skill set definition payload to project individual markdown sections chunks and their vector outputs as documents in the search index using the [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) and [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md)
++ `indexProjections` are used for indexes containing chunked documents. The projections specify how parent-child content is mapped to fields in a search index for one-to-many indexing. For more information, see [Define an index projection](search-how-to-define-index-projections.md).
+
++ `cognitiveServices` [attaches an Azure AI multi-service account](cognitive-search-attach-cognitive-services.md) for billing purposes (the Document Layout skill is available through [pay-as-you pricing](https://azure.microsoft.com/pricing/details/ai-document-intelligence/)).
 
 ```https
 POST {endpoint}/skillsets?api-version=2024-11-01-preview
@@ -298,7 +314,7 @@ POST {endpoint}/skillsets?api-version=2024-11-01-preview
 
 ```
 
-## Run the indexer
+## Configure and run the indexer
 
 Once you create a data source, index, and skillset, you're ready to [create and run the indexer](search-howto-create-indexers.md#run-the-indexer). This step puts the pipeline into execution.
 
@@ -307,9 +323,13 @@ When using the [Document Layout skill](cognitive-search-skill-document-intellige
 + The `allowSkillsetToReadFileData` parameter should be set to `true`.
 + the `parsingMode` parameter should be set to `default`.
 
-Here's an example payload
+`outputFieldMappings` don't need to be set in this scenario because `indexProjections` handle the source field to search field associations. Index projections handle field associations for the Document Layout skill and also regular chunking with the split skill for imported and vectorized data workloads. Output field mappings are still necessary for transformations or complex data mappings with functions which apply in other cases. However, for n-chunks per document, index projections handle this functionality natively.
+
+Here's an example of an indexer creation request.
+
+```https
+POST {endpoint}/indexers?api-version=2024-11-01-preview
 
-```json
 {
   "name": "my_indexer",
   "dataSourceName": "my_blob_datasource",
@@ -333,6 +353,8 @@ Here's an example payload
 }
 ```
 
+When you send the request to the search service, the indexer runs.
+
 ## Verify results
 
 You can query your search index after processing concludes to test your solution.
@@ -344,16 +366,41 @@ For Search Explorer, you can copy just the JSON and paste it into the JSON view
 ```http
 POST /indexes/[index name]/docs/search?api-version=[api-version]
 {
-    "search": "*",
-    "select": "metadata_storage_path, markdown_section, vector"
+  "search": "copay for in-network providers",
+  "count": true,
+  "searchMode": "all",
+  "vectorQueries": [
+    {
+      "kind": "text",
+      "text": "*",
+      "fields": "text_vector,image_vector"
+    }
+  ],
+  "queryType": "semantic",
+  "semanticConfiguration": "healthplan-doc-layout-test-semantic-configuration",
+  "captions": "extractive",
+  "answers": "extractive|count-3",
+  "queryLanguage": "en-us",
+  "select": "header_1, header_2, header_3"
 }
 ```
 
+If you used the health plan PDFs to test this skill, Search Explorer results for the example query should look similar to the results in the following screenshot. 
+
++ The query is a [hybrid query](hybrid-search-how-to-query.md) over text and vectors, so you see a `@search.rerankerScore` and results are ranked by that score. `searchMode=all` means that *all* query terms must be considered for a match (the default is *any*).
+
++ The query uses semantic ranking, so you see `captions` (it also has `answers`, but those aren't shown in the screenshot). The results are the most semantically relevant to the query input, as determined by the [semantic ranker](semantic-search-overview.md).
+
++ The `select` statement (not shown in the screenshot) specifies the header fields that the Document Layout skill detects and populates. You can add more fields to the select clause to inspect the content of chunks, title, or any other human readable field.
+
+:::image type="content" source="media/search-how-to-semantic-chunking/query-results-doc-layout.png" lightbox="media/search-how-to-semantic-chunking/query-results-doc-layout.png" alt-text="Screenshot of hybrid query results that include doc layout skill output fields.":::
+
 ## See also
 
 + [Create or update a skill set](cognitive-search-defining-skillset.md).
 + [Create a data source](search-howto-indexing-azure-blob-storage.md)
 + [Define an index projection](search-how-to-define-index-projections.md)
++ [Attach an Azure AI multi-service account](cognitive-search-attach-cognitive-services.md)
 + [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md)
 + [Text Split skill](cognitive-search-skill-textsplit.md)
 + [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックチャンクingに関するドキュメントの改訂"
}
```

### Explanation
このコードの変更は、`search-how-to-semantic-chunking.md`ファイルに対するマイナーな更新を示しています。具体的には、67行の追加と20行の削除が行われ、合計87行の変更が加えられました。この修正は、ドキュメントのタイトルや説明文を見直し、コンテンツの構造やセマンティックなチャンクング手法についての情報を強化することを目的としています。例えば、ドキュメントレイアウトに基づいたコンテンツのチャンクング方法が詳しく説明され、ユーザーが関連する機能をより理解しやすくなっています。

変更内容には、Document Layoutスキルに関する新しい情報や、プロジェクトが含まれる検索インデックスの構成、およびさまざまなデータソースのサポートに関する詳細が含まれています。この更新は、AzureのAI検索を利用する開発者にとって、実践的で役立つガイドとなり、検索結果の最適化や埋め込みの生成に関する有用な知見を提供します。さらに、さまざまなファイル形式のサポートや、検索インデックスの作成手順に関する具体的な例も追加され、ユーザーが実装を容易に行えるようにしています。

## articles/search/search-howto-managed-identities-data-sources.md{#item-edf98d}

<details>
<summary>Diff</summary>
````diff
@@ -11,17 +11,17 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: how-to
-ms.date: 09/11/2024
+ms.date: 11/22/2024
 ---
 
 # Configure a search service to connect using a managed identity in Azure AI Search
 
 > [!IMPORTANT]
-> User-assigned managed identity assignment is in public preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [Management preview REST API](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2024-03-01-preview&preserve-view=true#identity) provides user-assigned managed identity assignment for Azure AI Search. Support for a system-assigned managed identity is generally available.
+> User-assigned managed identity assignment is in public preview under [Supplemental Terms of Use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). The [Management preview REST API](/rest/api/searchmanagement/services/update?view=rest-searchmanagement-2024-03-01-preview&preserve-view=true#identity) provides user-assigned managed identity assignment for Azure AI Search. Support for a *system-assigned* managed identity is generally available.
 
 You can use Microsoft Entra ID and role assignments for outbound connections from Azure AI Search to resources providing data, applied AI, or vectorization during indexing or queries. 
 
-To use roles on an outbound connection, first configure your search service to use either a [system-assigned or user-assigned managed identity](/azure/active-directory/managed-identities-azure-resources/overview) as the security principle for your search service in a Microsoft Entra tenant. Once you have a managed identity, you can assign roles for authorized access. Managed identities and role assignments eliminate the need for passing secrets and credentials in a connection string or code.
+To use roles on an outbound connection, first configure your search service to use either a [system-assigned or user-assigned managed identity](/azure/active-directory/managed-identities-azure-resources/overview) as the security principal for your search service in a Microsoft Entra tenant. Once you have a managed identity, you can assign roles for authorized access. Managed identities and role assignments eliminate the need for passing secrets and credentials in a connection string or code.
 
 ## Prerequisites
 
@@ -201,7 +201,6 @@ You can use a preview Management REST API instead of the portal to assign a user
 
    + "userAssignedIdentities" includes the details of the user assigned managed identity. This identity [must already exist](/azure/active-directory/managed-identities-azure-resources/how-manage-user-assigned-managed-identities) before you can specify it in the Update Service request.
   
-
 ---
 
 ## Assign a role
@@ -295,7 +294,11 @@ A debug session runs in the portal and takes a connection string when you start
 
 [**Custom skill:**](cognitive-search-custom-skill-interface.md)
 
-A custom skill targets the endpoint of an Azure function or app hosting custom code. The endpoint is specified in the [custom skill definition](cognitive-search-custom-skill-web-api.md). The presence of the "authResourceId" tells the search service to connect using a managed identity, passing the application ID of the target function or app in the property.
+A [custom skill](cognitive-search-custom-skill-web-api.md) targets the endpoint of an Azure function or app hosting custom code. 
+
++ `uri` is the endpoint of the function or app. 
+
++ `authResourceId` tells the search service to connect using a managed identity, passing the application ID of the target function or app in the property.
 
 ```json
 {
@@ -312,7 +315,9 @@ A custom skill targets the endpoint of an Azure function or app hosting custom c
 
 [**Azure OpenAI embedding skill**](cognitive-search-skill-azure-openai-embedding.md) and [**Azure OpenAI vectorizer:**](vector-search-how-to-configure-vectorizer.md)
 
- An Azure OpenAI embedding skill and vectorizer in AI Search target the endpoint of an Azure OpenAI service hosting an embedding model. The endpoint is specified in the [Azure OpenAI embedding skill definition](cognitive-search-skill-azure-openai-embedding.md) and/or in the [Azure OpenAI vectorizer definition](vector-search-how-to-configure-vectorizer.md). The system-managed identity is used if configured and if the "apikey" and "authIdentity" are empty. The "authIdentity" property is used for user-assigned managed identity only.
+ An Azure OpenAI embedding skill and vectorizer in AI Search target the endpoint of an Azure OpenAI service hosting an embedding model. The endpoint is specified in the [Azure OpenAI embedding skill definition](cognitive-search-skill-azure-openai-embedding.md) and/or in the [Azure OpenAI vectorizer definition](vector-search-how-to-configure-vectorizer.md). 
+
+The system-managed identity is used automatically if `"apikey"` and `"authIdentity"` are empty, as demonstrated in the following example. The `"authIdentity"` property is used for user-assigned managed identity only.
 
 **System-managed identity example:**
  
@@ -337,6 +342,8 @@ A custom skill targets the endpoint of an Azure function or app hosting custom c
 }
 ```
 
+Here's a [vectorizer example](vector-search-how-to-configure-vectorizer.md) configured for a system-assigned managed identity. A vectorizer is specified in a search index.
+
 ```json
  "vectorizers": [
     {
@@ -353,6 +360,8 @@ A custom skill targets the endpoint of an Azure function or app hosting custom c
 
 **User-assigned managed identity example:**
 
+A user-assigned managed identity is used if `"apiKey"` is empty and a valid `"authIdentity"` is provided.
+
 ```json
 {
   "@odata.type": "#Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill",
@@ -378,6 +387,8 @@ A custom skill targets the endpoint of an Azure function or app hosting custom c
 }
 ```
 
+Here's a [vectorizer example](vector-search-how-to-configure-vectorizer.md) configured for a user-assigned managed identity. A vectorizer is specified in a search index.
+
 ```json
  "vectorizers": [
     {
@@ -398,11 +409,11 @@ A custom skill targets the endpoint of an Azure function or app hosting custom c
 
 ## Check for firewall access
 
-If your Azure resource is behind a firewall, make sure there's an inbound rule that admits requests from your search service. 
+If your Azure resource is behind a firewall, make sure there's an inbound rule that admits requests from your search service and from the Azure portal.
 
 + For same-region connections to Azure Blob Storage or Azure Data Lake Storage Gen2, use a system managed identity and the [trusted service exception](search-indexer-howto-access-trusted-service-exception.md). Optionally, you can configure a [resource instance rule](/azure/storage/common/storage-network-security#grant-access-from-azure-resource-instances) to admit requests.
 
-+ For all other resources and connections, [configure an IP firewall rule](search-indexer-howto-access-ip-restricted.md) that admits requests from Search. See [Indexer access to content protected by Azure network security features](search-indexer-securing-resources.md) for details.
++ For all other resources and connections, [configure an IP firewall rule](search-indexer-howto-access-ip-restricted.md) that admits requests from Azure AI Search. See [Indexer access to content protected by Azure network security features](search-indexer-securing-resources.md) for details.
 
 ## See also
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージド ID を使用したデータソースへの接続に関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、`search-howto-managed-identities-data-sources.md`ファイルに対するマイナーな更新を示しています。具体的には、19行の追加と8行の削除が行われ、合計27行の変更が加えられました。この修正は、Azure AI Searchを使用してマネージド IDを介してデータソースに接続する方法に関する詳細情報を提供することを目的としています。

変更点には、ユーザー割り当てのマネージド IDの使用に関する注意点の強調や、システム割り当てのマネージド IDの自動的な使用に関する説明が含まれています。また、firewall 設定についても明確化されており、Azure Portalからのリクエストを許可するための必要なルールについての新たな情報が追加されています。

さらに、カスタムスキルやベクトライザの利用に関する具体例も更新され、効果的な実装のためのヒントが示されています。これにより、ユーザーはAzure AI Searchの機能をより適切に活用し、セキュリティを強化しつつデータにアクセスできるようになります。全体として、この更新は文書の精度と有用性を向上させ、開発者がマネージド IDを使用する際の理解を深める助けとなります。

## articles/search/search-security-network-security-perimeter.md{#item-49c0d7}

<details>
<summary>Diff</summary>
````diff
@@ -45,7 +45,7 @@ You can add a search service to a network security perimeter in the Azure portal
 
 Azure Network Security Perimeter allows administrators to define a logical network isolation boundary for PaaS resources (for example, Azure Storage and Azure SQL Database) that are deployed outside virtual networks. It restricts communication to resources within the perimeter, and it allows non-perimeter public traffic through inbound and outbound access rules.
 
-You can add Azure AI Search to a network security perimiter so that all indexing and query requests occur within the security boundary.
+You can add Azure AI Search to a network security perimeter so that all indexing and query requests occur within the security boundary.
 
 1. In the Azure portal, create or find the network security perimeter service for your subscription.
 
@@ -269,7 +269,7 @@ In order to test your connection through network security perimeter, you need ac
 
 ## View and manage network security perimeter configuration
 
-You can use the [Network Security Perimiter Configuration REST APIs](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true) to review and reconcile perimeter configurations.
+You can use the [Network Security Perimeter Configuration REST APIs](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true) to review and reconcile perimeter configurations.
 
 Be sure to use preview API version `2024-06-01-preview`. [Learn how to call the Management REST APIs](search-manage-rest.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ネットワークセキュリティ境界に関するドキュメントの名前変更"
}
```

### Explanation
このコードの変更は、`search-security-network-security-perimiter.md` ファイルが `search-security-network-security-perimeter.md` に名称変更されたことを示しています。この変更に伴い、ドキュメント内にわずか2行の追加と2行の削除があり、合計で4行の変更が行われました。

この修正は、文書の整合性を確保するためのもので、参考となる内容に誤字が含まれていたのを修正しています。具体的には、「perimiter」から「perimeter」への訂正が行われ、より正確で一貫した表現となりました。これにより、Azure Network Security Perimeterに関する情報が正確に提供され、ユーザーがセキュリティ境界内でのデータのインデクシングやクエリリクエストを適切に行えるようになります。

全体として、この更新は文書の品質を向上させ、Azure AI Searchに関するネットワークセキュリティの観点を明確にするものです。ユーザーは、セキュリティ境界の設定や管理についてより明瞭な理解を得られるでしょう。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -321,8 +321,6 @@ items:
         href: cognitive-search-concept-image-scenarios.md
       - name: Cache (incremental) enrichment
         href: search-howto-incremental-index.md
-      - name: Structure-aware chunking and vectorization
-        href: search-how-to-semantic-chunking.md        
       - name: Design tips
         href: cognitive-search-concept-troubleshooting.md
       - name: Custom skills
@@ -339,6 +337,8 @@ items:
       href: vector-search-how-to-create-index.md
     - name: Chunk documents
       href: vector-search-how-to-chunk-documents.md
+    - name: Chunk and vectorize by document layout
+      href: search-how-to-semantic-chunking.md   
     - name: Generate embeddings
       href: vector-search-how-to-generate-embeddings.md
     - name: Use embedding models from Azure AI Studio
@@ -469,7 +469,7 @@ items:
       - name: Connect through a firewall
         href: search-indexer-howto-access-ip-restricted.md
       - name: Connect using Network Security Perimeter
-        href: search-security-network-security-perimiter.md
+        href: search-security-network-security-perimeter.md
       - name: Connect as a trusted service
         href: search-indexer-howto-access-trusted-service-exception.md
       - name: Connect through a shared private link
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次ファイルの更新"
}
```

### Explanation
このコードの変更は、`toc.yml` ファイルにおけるマイナーな更新を示しており、合計で6行が変更されました。この変更には、3行の追加と3行の削除が含まれています。

具体的には、ドキュメントの構造に関する内容が調整されています。「構造を意識したチャンク化とベクトライゼーション」という項目が新たに追加され、関連する `search-how-to-semantic-chunking.md` ファイルへのリンクが設けられました。一方、過去の項目である「構造を意識したチャンク化とベクトライゼーション」に関する記述が削除されましたが、これは新しい項目の追加と整合性を持たせるためのものです。

また、セキュリティパラメータに関するファイル名に誤字があった部分も修正され、「perimiter」から「perimeter」への訂正が行われました。これにより、関連するドキュメントへのアクセスがより明確になります。

全体として、この更新は情報の整合性を保ちながら、ユーザーが必要な情報にアクセスしやすくするためのものであり、Azure AI Searchに関するリソースの理解が向上します。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ ms.custom:
 
 | Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
 |-----------------------------|------|--------------|
-| [**Network security perimeter**](search-security-network-security-perimiter.md) | Security | Join a search service to a [network security perimeter](/azure/private-link/network-security-perimeter-concepts) to control network access to your search service. The Azure portal and the Management REST APIs in the [2024-06-01-preview](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true) can be used to view and reconcile network security perimeter configurations. |
+| [**Network security perimeter**](search-security-network-security-perimeter.md) | Security | Join a search service to a [network security perimeter](/azure/private-link/network-security-perimeter-concepts) to control network access to your search service. The Azure portal and the Management REST APIs in the [2024-06-01-preview](/rest/api/searchmanagement/network-security-perimeter-configurations?view=rest-searchmanagement-2024-06-01-preview&preserve-view=true) can be used to view and reconcile network security perimeter configurations. |
 | [**Shared private link support for Azure AI service connections**](search-indexer-howto-access-private.md) | Security  | Connections to Azure AI for built-in skills processing can now be private using a shared private link on the connection. |
 | [**Rescoring options for compressed vectors**](/azure/search/vector-search-how-to-quantization?tabs=2024-11-01-preview%2Cquery-2024-07-01#add-compressions-to-a-search-index) | Relevance | You can set options to rescore with original vectors instead of compressed vectors. Applies to HNSW and exhaustive KNN vector algorithms, using binary and scalar compression. Available in the [Create or Update Index (2024-11-01-preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature. |
 | [**Store fewer vector instances**](vector-search-how-to-storage-options.md) | vector search | In vector compression scenarios, you can omit storage of full precision vectors if you don't need them for rescoring. Available in the [Create or Update Index (2024-11-01-preview)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true), the Azure portal, and in the Azure SDK beta packages that provide this feature. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ネットワークセキュリティ境界に関するリンク修正"
}
```

### Explanation
このコードの変更は、`whats-new.md` ファイルにおける小規模な修正を示しています。この変更では、1行の追加と1行の削除が伴っており、合計で2行の変更が行われました。

具体的には、「ネットワークセキュリティ境界」に関するリンクの誤字が修正されました。元の記述では「perimiter」となっていた部分が、正しい「perimeter」に訂正されました。この修正により、ユーザーが提供されたリンクを通じて、正確かつ適切な情報にアクセスできるようになります。

また、この更新は、Azure AI の新機能や改善を把握するための重要な情報を提供している文書の品質を向上させる効果があります。これにより、ユーザーは最新のネットワークセキュリティの機能を理解し、適切に使用することができるでしょう。


