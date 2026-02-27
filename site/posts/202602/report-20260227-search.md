---
date: '2026-02-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4a1cec0...MicrosoftDocs:2a3b643
summary: この変更には、新しいファイルや機能の追加、リンクの修正、いくつかの削除が含まれています。特に、セキュリティに関する新しいドキュメントやAzure
  AI Searchのセキュリティ強化、さらにマルチモーダル機能の改善が重要なポイントです。新たに追加されたファイルには、認証設定のガイドや視覚資料、そしてセキュリティのベストプラクティスが含まれています。一方で、いくつかの古いチュートリアルは削除され、新しいチュートリアルに統合されました。また、リンクも最新のリソースに更新され、利用者が常に新しい情報にアクセスできるようになっています。全体として、ユーザーがAzure
  AI Searchをより効果的かつ安全に利用できるように、技術情報が整理されました。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4a1cec0...MicrosoftDocs:2a3b643){target="_blank"}

<format>
# Highlights
この変更には、新しいファイルと機能の追加、リンク修正、削除が含まれています。特に、新しいセキュリティドキュメントの追加、Azure AI Searchでのセキュリティ強化、およびマルチモーダル関連機能の改良が目立ちます。

## New features
- `articles/search/includes/resource-authentication-identity.md` の追加による、認証設定の新機能。
- `articles/search/media/tutorial-multimodal/normalized-image-in-storage.png` の追加で、視覚的資料による解説を強化。
- 新しいセキュリティドキュメント `articles/search/search-security-best-practices.md` および `articles/search/search-security-built-in.md` の追加。
- マルチモーダルに関する新しいチュートリアル `articles/search/tutorial-multimodal.md` の追加により、マルチモーダル機能の強化。

## Breaking changes
- 複数のチュートリアル記事（例：`tutorial-document-extraction-image-verbalization.md` や `tutorial-document-extraction-multimodal-embeddings.md`）の削除。

## Other updates
- 多数のファイルにおけるリンク参照の変更。
- ドキュメントの形式や内容が微調整され、情報の整合性を改善。

# Insights
今回の変更は、Azure AI Searchにおけるセキュリティの強化、ユーザーへの利用ガイドライン提供の充実、マルチモーダルオペレーションをサポートするドキュメントの整備が中心となっています。

まず、セキュリティ関連の新規ドキュメントが追加され、Azure AI Searchのセキュリティ機能を細かくガイドするコンテンツが増えました。これにより、セキュリティ対策を必要とするユーザーにとって、大いに役立つリソースとなります。

削除されたチュートリアルは、マルチモーダル処理や埋め込み技術に関するものでしたが、新しい一元化されたチュートリアルへと集約される形となっています。この一元化は、混乱を避け効率化を図り、関連技術の情報を統合し利用者が理解しやすい形に変更されたことを示しています。

リンク修正については、古いセキュリティガイドや機能に関するページへの参照が停止され、新しいセキュリティポリシーや機能のベストプラクティスページへと更新されました。これによって、利用者は常に最新のリソースにアクセスできます。

全体として、今回の改定はAzure AI Searchの機能をより使いやすく、安全に利用するための技術的情報を整備することに重点を置かれたものであるといえます。ユーザーは、新設されたセキュリティガイドと集約されたマルチモーダル機能のリソースを活用することで、Azure AI Searchをより効果的に利用できるようになるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [.openpublishing.redirection.search.json](#item-8b66f9) | minor update | リダイレクション設定の更新 | modified | 17 | 13 | 30 | 
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | 接続のセキュリティの更新 | modified | 1 | 1 | 2 | 
| [cognitive-search-skill-content-understanding.md](#item-c7787e) | minor update | コンテンツ理解スキルのチュートリアルリンクの更新 | modified | 1 | 4 | 5 | 
| [cognitive-search-skill-document-extraction.md](#item-072b72) | minor update | ドキュメント抽出スキルのチュートリアルリンクの見直し | modified | 1 | 5 | 6 | 
| [cognitive-search-skill-document-intelligence-layout.md](#item-62c06f) | minor update | ドキュメントレイアウトスキルのチュートリアルリンクの更新 | modified | 1 | 4 | 5 | 
| [cognitive-search-skill-genai-prompt.md](#item-384bf9) | minor update | GenAIプロンプトスキルのチュートリアルリンクの更新 | modified | 1 | 4 | 5 | 
| [enrichment-cache-how-to-configure.md](#item-b0ae0b) | minor update | エンリッチメントキャッシュの設定に関するドキュメントの更新 | modified | 60 | 109 | 169 | 
| [enrichment-cache-how-to-manage.md](#item-a972bd) | minor update | エンリッチメントキャッシュ管理に関するドキュメントの更新 | modified | 7 | 9 | 16 | 
| [resource-authentication-identity.md](#item-bcdb0d) | new feature | リソース認証に関する新しいインクルードファイルの追加 | added | 27 | 0 | 27 | 
| [normalized-image-in-storage.png](#item-71b042) | new feature | 正規化された画像の追加 | added | 0 | 0 | 0 | 
| [multimodal-search-overview.md](#item-d82192) | minor update | マルチモーダル検索の概要に関するドキュメントの更新 | modified | 1 | 4 | 5 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | RAG概要ドキュメントのセキュリティリンクの修正 | modified | 1 | 1 | 2 | 
| [search-create-service-portal.md](#item-f90159) | minor update | サービスポータルドキュメントのコンピュータタイプ参照の変更 | modified | 2 | 2 | 4 | 
| [search-faq-frequently-asked-questions.yml](#item-eab2ba) | minor update | FAQドキュメントのアウトバウンドコールに関するリンクの更新 | modified | 1 | 1 | 2 | 
| [search-features-list.md](#item-d34448) | minor update | データ暗号化のセクション内のリンクの更新 | modified | 1 | 1 | 2 | 
| [search-get-started-arm.md](#item-9287ad) | minor update | ネットワークセキュリティ設定のリンク更新 | modified | 1 | 1 | 2 | 
| [search-get-started-bicep.md](#item-731b0e) | minor update | ネットワークセキュリティ設定のリンク更新 | modified | 1 | 1 | 2 | 
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | マルチモーダルチュートリアルへのリンク更新 | modified | 1 | 6 | 7 | 
| [search-how-to-create-indexers.md](#item-de71fb) | minor update | 外部データへの安全なアクセスに関するリンク更新 | modified | 1 | 1 | 2 | 
| [search-how-to-managed-identities.md](#item-3536f2) | minor update | 関連リンクの名称変更 | modified | 1 | 1 | 2 | 
| [search-howto-reindex.md](#item-46738a) | minor update | リンク先の名称変更と更新 | modified | 1 | 1 | 2 | 
| [search-indexer-sensitivity-labels.md](#item-2a7bfc) | minor update | 日付の更新と制限事項の変更 | modified | 1 | 3 | 4 | 
| [search-manage-azure-cli.md](#item-7fdd08) | minor update | リンク先の変更 | modified | 1 | 1 | 2 | 
| [search-manage-rest.md](#item-405ec7) | minor update | 機密コンピューティングに関するリンクの更新 | modified | 1 | 1 | 2 | 
| [search-manage.md](#item-4043d7) | minor update | リンクの変更と追加 | modified | 2 | 2 | 4 | 
| [search-monitor-logs-powerbi.md](#item-5b3491) | minor update | タイトルのフォーマットの修正 | modified | 1 | 1 | 2 | 
| [search-region-support.md](#item-25b0f1) | minor update | リンク先の修正 | modified | 1 | 1 | 2 | 
| [search-security-api-keys.md](#item-d8c908) | minor update | リンク先の変更 | modified | 1 | 1 | 2 | 
| [search-security-best-practices.md](#item-9dd4cd) | new feature | Azure AI Searchのセキュリティベストプラクティスに関する新しい記事の追加 | added | 296 | 0 | 296 | 
| [search-security-built-in.md](#item-a42668) | new feature | Azure AI Searchのデータ、プライバシー、および組み込み保護に関する新しい記事の追加 | added | 160 | 0 | 160 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | 暗号鍵の管理に関するドキュメントの修正 | modified | 1 | 1 | 2 | 
| [search-security-overview.md](#item-6b3f1e) | breaking change | Azure AI Searchのセキュリティ概要に関する既存の記事の削除 | removed | 0 | 321 | 321 | 
| [toc.yml](#item-c4768f) | minor update | 目次ファイルの更新とチュートリアルリソースの整理 | modified | 8 | 12 | 20 | 
| [tutorial-document-extraction-image-verbalization.md](#item-398a90) | breaking change | 画像の言語化に関するチュートリアル記事の削除 | removed | 0 | 769 | 769 | 
| [tutorial-document-extraction-multimodal-embeddings.md](#item-a3db59) | breaking change | マルチモーダル埋め込みに関するチュートリアル記事の削除 | removed | 0 | 720 | 720 | 
| [tutorial-document-layout-image-verbalization.md](#item-f5de57) | breaking change | 構造化ドキュメントレイアウトからの画像音声化チュートリアルの削除 | removed | 0 | 740 | 740 | 
| [tutorial-document-layout-multimodal-embeddings.md](#item-f67371) | breaking change | 構造化ドキュメントレイアウトからのマルチモーダル埋め込みに関するチュートリアルの削除 | removed | 0 | 666 | 666 | 
| [tutorial-multimodal.md](#item-718d2e) | new feature | マルチモーダルチャンクおよび埋め込みに関するチュートリアルの追加 | added | 1848 | 0 | 1848 | 
| [vector-store.md](#item-db9b8c) | minor update | ベクトルデータへの安全なアクセスに関する情報の更新 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-fa71b4) | minor update | Azure Confidential Computingに関するセクションの参照先を更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/.openpublishing.redirection.search.json{#item-8b66f9}

<details>
<summary>Diff</summary>
````diff
@@ -370,7 +370,6 @@
             "redirect_url": "/azure/search/search-what-is-data-import",
             "redirect_document_id": true
         },
-
         {
             "source_path_from_root": "/articles/search/search-get-started-management-api.md",
             "redirect_url": "/rest/api/searchmanagement/",
@@ -427,24 +426,24 @@
             "redirect_document_id": false
         },
         {
-            "source_path_from_root": "/articles/search/tutorial-multimodal-indexing-with-embedding-and-doc-extraction.md",
-            "redirect_url": "/azure/search/tutorial-document-extraction-multimodal-embeddings",
-            "redirect_document_id": true
+            "source_path_from_root": "/articles/search/tutorial-document-extraction-multimodal-embeddings.md",
+            "redirect_url": "/azure/search/tutorial-multimodal",
+            "redirect_document_id": false
         },
         {
-            "source_path_from_root": "/articles/search/tutorial-multimodal-indexing-with-image-verbalization-and-doc-extraction.md",
-            "redirect_url": "/azure/search/tutorial-document-extraction-image-verbalization",
-            "redirect_document_id": true
+            "source_path_from_root": "/articles/search/tutorial-document-extraction-image-verbalization.md",
+            "redirect_url": "/azure/search/tutorial-multimodal",
+            "redirect_document_id": false
         },
         {
-            "source_path_from_root": "/articles/search/tutorial-multimodal-index-embeddings-skill.md",
-            "redirect_url": "/azure/search/tutorial-document-layout-multimodal-embeddings",
-            "redirect_document_id": true
+            "source_path_from_root": "/articles/search/tutorial-document-layout-multimodal-embeddings.md",
+            "redirect_url": "/azure/search/tutorial-multimodal",
+            "redirect_document_id": false
         },
         {
-            "source_path_from_root": "/articles/search/tutorial-multimodal-index-image-verbalization-skill.md",
-            "redirect_url": "/azure/search/tutorial-document-layout-image-verbalization",
-            "redirect_document_id": true
+            "source_path_from_root": "/articles/search/tutorial-document-layout-image-verbalization.md",
+            "redirect_url": "/azure/search/tutorial-multimodal",
+            "redirect_document_id": false
         },
         {
             "source_path_from_root": "/articles/search/search-get-started-rest.md",
@@ -650,6 +649,11 @@
             "source_path_from_root": "/articles/search/keyless-connections.md",
             "redirect_url": "/azure/search/search-security-rbac-client-code",
             "redirect_document_id": true
+        },
+        {
+            "source_path_from_root": "/articles/search/search-security-overview.md",
+            "redirect_url": "/azure/search/search-security-built-in",
+            "redirect_document_id": true
         }
     ]
   }
\ No newline at end of file
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
この変更は、`articles/search/.openpublishing.redirection.search.json`ファイル内のリダイレクション設定に関するものです。ファイルには合計30の変更があり、その中には17行の追加と13行の削除が含まれています。

主な変更点として、リダイレクション先のURLとソースパスに関する情報を整理し、いくつかのリダイレクションを更新しました。具体的には、以下のような変更が行われています：

- 一部のソースパスが修正され、特定のチュートリアルへのリダイレクションが統一されたURLに更新されています。
- リダイレクションのドキュメントIDの設定が変わり、新しいリダイレクションのいくつかで、`redirect_document_id`が`false`に変更されました。

これにより、ユーザーが特定の記事にアクセスした際に正しくリダイレクトされるよう、コンテンツの整合性が向上しました。この更新は、Azure Searchに関する具体的な情報へのアクセスを改善する目的で実施されています。

## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -273,7 +273,7 @@ Billing goes into effect when API calls to a Foundry resource exceed 20 API call
 
 Keyless and key-based connections are used for billing, but not for connections related to enrichment operations.
 
-For key-based connections, a search service [connects over the internal network](search-security-overview.md#internal-traffic) to a Foundry resource located in the [same physical region](search-region-support.md). Most regions that offer Azure AI Search also offer other Azure services. If you attempt AI enrichment in a region that doesn't have both services, you see this message: "Provided key isn't a valid CognitiveServices type key for the region of your search service."
+For key-based connections, a search service [connects over the internal network](search-security-built-in.md#internal-traffic-protection) to a Foundry resource located in the [same physical region](search-region-support.md). Most regions that offer Azure AI Search also offer other Azure services. If you attempt AI enrichment in a region that doesn't have both services, you see this message: "Provided key isn't a valid CognitiveServices type key for the region of your search service."
 
 For keyless connections, a search service authenticates using its identity and role assignment and targets a Foundry resource. The resource is specified as a fully qualified URI, and the URI includes a unique subdomain.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "接続のセキュリティの更新"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-attach-cognitive-services.md`ファイル内の接続に関するセキュリティ情報の更新を含んでいます。具体的には、1行の追加と1行の削除が行われており、合計で2つの変更が発生しています。

主な変更点は、キーを用いた接続に関する説明の中で、内部ネットワーク接続に関する参照リンクが更新されたことです。以前は「search-security-overview.md」にリンクされていた部分が、「search-security-built-in.md」となり、接続の保護に関する情報が強調されています。

この変更により、ユーザーは接続のセキュリティに関する最新の情報にアクセスでき、Azure AI Searchを使用した際の設定や運用において、より安全なベストプラクティスを理解する助けとなります。

## articles/search/cognitive-search-skill-content-understanding.md{#item-c7787e}

<details>
<summary>Diff</summary>
````diff
@@ -32,10 +32,7 @@ The Azure Content Understanding skill is bound to a [billable Microsoft Foundry
 Azure AI resource skills, such as the [Document Layout skill](/azure/search/cognitive-search-skill-document-intelligence-layout), the Azure Content Understanding skill doesn't provide 20 free documents per indexer per day. Execution of this skill is charged at the [Azure Content Understanding price](https://azure.microsoft.com/pricing/details/content-understanding/).
 
 > [!TIP]
-> You can use the Azure Content Understanding skill in a skillset that also performs image verbalization and chunk vectorization. In the following tutorials, replace the Document Layout skill with the Azure Content Understanding skill.
->
-> + [Tutorial: Verbalize images from a structured document layout](tutorial-document-layout-image-verbalization.md)
-> + [Tutorial: Vectorize from a structured document layout](tutorial-document-layout-multimodal-embeddings.md)
+> You can use the Azure Content Understanding skill in a skillset that also performs image verbalization and chunk vectorization. In the [multimodal tutorial](tutorial-multimodal.md), replace the Document Layout skill with the Azure Content Understanding skill.
 
 ## Limitations
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツ理解スキルのチュートリアルリンクの更新"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-content-understanding.md`ファイル内のAzureのコンテンツ理解スキルに関する情報の更新を含んでいます。具体的には、1行の追加と4行の削除が行われ、合計で5つの変更が発生しています。

主な変更点として、Azureコンテンツ理解スキルを使用する際のチュートリアルリンクが変更されました。以前の文では、具体的なチュートリアルが2つ挙げられていましたが、これが1つの「マルチモーダルチュートリアル」リンクに整理されています。この更新により、ユーザーは関連する情報をより簡潔に参照できるようになり、ドキュメント内の情報の流れも改善されています。

この変更は、Azureのコンテンツ理解スキルを効果的に利用するための関連内容を簡素化し、ユーザーが必要な情報にアクセスしやすくすることを目的としています。

## articles/search/cognitive-search-skill-document-extraction.md{#item-072b72}

<details>
<summary>Diff</summary>
````diff
@@ -16,11 +16,7 @@ ms.update-cycle: 365-days
 
 The **Document Extraction** skill extracts content from a file in the [enrichment pipeline](cognitive-search-concept-intro.md). By default, content extraction or retrieval is built into the enrichment pipeline. However, by using the Document Extraction skill, you can control how parameters are set, and how extracted content is named in the enrichment tree.
 
-For [vector](vector-search-overview.md) and [multimodal search](multimodal-search-overview.md), Document Extraction combined with the [Text Split skill](cognitive-search-skill-textsplit.md) is more affordable than other [data chunking approaches](vector-search-how-to-chunk-documents.md). The following tutorials demonstrate skill usage for different scenarios:
-
-+ [Tutorial: Vectorize images and text](tutorial-document-extraction-multimodal-embeddings.md)
-
-+ [Tutorial: Verbalize images using generative AI](tutorial-document-extraction-image-verbalization.md)
+For [vector](vector-search-overview.md) and [multimodal search](multimodal-search-overview.md), Document Extraction combined with the [Text Split skill](cognitive-search-skill-textsplit.md) is more affordable than other [data chunking approaches](vector-search-how-to-chunk-documents.md). The [Multimodal tutorial](tutorial-multimodal.md) demonstrates this scenario.
 
 > [!NOTE]
 > This skill isn't bound to Foundry Tools and has no Foundry Tools key requirement.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント抽出スキルのチュートリアルリンクの見直し"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-document-extraction.md`ファイルにおけるドキュメント抽出スキルに関する内容の更新を含んでいます。具体的には、1行の追加と5行の削除が行われ、合計で6つの変更が発生しています。

主な変更点は、ドキュメント抽出スキルを使用する際のチュートリアルリンクの整理です。もともと示されていた複数の特定のチュートリアルの代わりに、マルチモーダルの使用シナリオを示す「マルチモーダルチュートリアル」へのリンクが追加されました。この更新により、ユーザーはドキュメント抽出スキルを使用した様々なシナリオを簡潔に学ぶことができるようになります。

この変更は、ドキュメント抽出スキルに関連する情報を簡素化し、ユーザーが必要なチュートリアルにアクセスしやすくするためのものです。

## articles/search/cognitive-search-skill-document-intelligence-layout.md{#item-62c06f}

<details>
<summary>Diff</summary>
````diff
@@ -22,10 +22,7 @@ For transactions that exceed 20 documents per indexer per day, this skill requir
 This article is the reference documentation for the Document Layout skill. For usage information, see [How to chunk and vectorize by document layout](search-how-to-semantic-chunking.md).
 
 > [!TIP]
-> It's common to use this skill on content that has structure and images, such as PDFs. The following tutorials demonstrate image verbalization with two different data chunking techniques:
->
-> - [Tutorial: Verbalize images from a structured document layout](tutorial-document-layout-image-verbalization.md)
-> - [Tutorial: Vectorize from a structured document layout](tutorial-document-layout-multimodal-embeddings.md)
+> It's common to use this skill on content that has structure and images, such as PDFs. The [Multimodal tutorial](tutorial-multimodal.md) demonstrates image verbalization with two different data chunking strategies.
 
 ## Limitations
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントレイアウトスキルのチュートリアルリンクの更新"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-document-intelligence-layout.md`ファイルのドキュメントレイアウトスキルに関する内容の更新を含んでいます。具体的には、1行の追加と4行の削除が行われ、合計で5つの変更が発生しています。

主な変更点としては、チュートリアルのリンクが整理され、特定の2つのチュートリアルが1つの「マルチモーダルチュートリアル」に統一されました。この新しいリンクは、画像の言語化を示す内容で、異なるデータチャンク戦略を用いた方法が示されています。変更により、ユーザーはドキュメントレイアウトスキルを使用する際に、より簡潔で関連性の高い情報を得ることができるようになります。

この変更は、ドキュメントレイアウトスキルを活用するためのリソースを整理し、ユーザーがエキスパートチュートリアルにアクセスしやすくするためのものです。

## articles/search/cognitive-search-skill-genai-prompt.md{#item-384bf9}

<details>
<summary>Diff</summary>
````diff
@@ -27,10 +27,7 @@ Here are some examples of how the GenAI prompt skill can help you create content
 The GenAI Prompt skill is available in the [latest preview REST API](/rest/api/searchservice/skillsets/create?view=rest-searchservice-2025-11-01-preview&preserve-view=true). This skill supports text, image, and multimodal content, such as images with visuals and text extracted from PDF files.
 
 > [!TIP]
-> It's common to use this skill combined with a data chunking skill. The following tutorials demonstrate image verbalization with two different data chunking techniques:
->
-> - [Tutorial: Verbalize images using generative AI](tutorial-document-extraction-image-verbalization.md)
-> - [Tutorial: Verbalize images from a structured document layout](tutorial-document-layout-image-verbalization.md)
+> It's common to use this skill combined with a data chunking skill. The [Multimodal tutorial](tutorial-multimodal.md) demonstrates image verbalization with two different data chunking strategies.
 >
 
 ## Supported models
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GenAIプロンプトスキルのチュートリアルリンクの更新"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-genai-prompt.md`ファイルにおけるGenAIプロンプトスキルに関する内容の更新を含んでいます。具体的には、1行の追加と4行の削除が実施され、合計で5つの変更が行われました。

主な変更点は、GenAIプロンプトスキルをデータチャンクスキルと組み合わせる際のチュートリアルリンクが整理されたことです。以前は、特定の2つのチュートリアルが列挙されていましたが、これが「マルチモーダルチュートリアル」という1つのリンクに統一されました。この新しいチュートリアルは、異なるデータチャンク戦略を用いた画像の言語化の方法を示しています。

この更新により、ユーザーはGenAIプロンプトスキルとデータチャンクスキルを利用する際に、より簡潔で一貫性のある情報へアクセスできるようになります。また、ドキュメント全体の理解を助ける役割も果たします。

## articles/search/enrichment-cache-how-to-configure.md{#item-b0ae0b}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/27/2025
+ms.date: 02/24/2026
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
@@ -18,9 +18,12 @@ ms.custom:
 > [!IMPORTANT] 
 > This feature is in public preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). [Preview REST APIs](/rest/api/searchservice/index-preview) support this feature.
 
-This article explains how to add caching to an enrichment pipeline so that you can modify downstream enrichment steps without having to rebuild in full every time. By default, a skillset is stateless, and changing any part of its composition requires a full rerun of the indexer. With an *enrichment cache*, the indexer can determine which parts of the document tree must be refreshed based on changes detected in the skillset or indexer definitions. Existing processed output is preserved and reused wherever possible. 
+This article explains how to add caching to a skillset pipeline so that you can modify downstream enrichment steps without a full rebuild every time. By default, a skillset is stateless, and changing any part of its composition requires a full rerun of the indexer. With an *enrichment cache*, the indexer determines which parts of the document tree must be refreshed based on skillset or indexer definition changes. Existing processed output is preserved and reused where possible.
 
-Cached content is placed in Azure Storage using account information that you provide. The container, named `ms-az-search-indexercache-<alpha-numerc-string>`, is created when you run the indexer. It should be considered an internal component managed by your search service and must not be modified.
+Cached content is placed in Azure Storage using a connection string that you provide. These objects are created when you run the indexer. It should be considered an internal component managed by your search service and must not be modified.
+
++ A container named `ms-az-search-indexercache-<alpha-numeric-string>`
++ Tables named `MsAzSearchIndexerCacheIndex<alpha-numeric-string>`
 
 ## Prerequisites
 
@@ -37,146 +40,94 @@ You should be familiar with setting up indexers and skillsets. Start with [index
 
 ## Permissions
 
-Azure AI Search needs write-access to Azure Storage. If you're using a managed identity for your search service, make sure it's assigned to the **Storage Blob Data Contributor** and **Storage Table Data Contributor** roles. For more information, see [Connect to Azure Storage using a managed identity (Azure AI Search)](search-howto-managed-identities-storage.md).
+An Azure AI Search identity needs write-access to Azure Storage:
 
-## Enable on new indexers
++ **Storage Blob Data Contributor**
++ **Storage Table Data Contributor**
 
-You can use the Azure portal, preview APIs, or preview Azure SDK packages to enable an enrichment cache on an indexer.
+The connection string syntax determines whether a system-assigned or user-assigned identity is used. For more information, see [Connect to Azure Storage using a managed identity](search-howto-managed-identities-storage.md).
 
-### [**Azure portal**](#tab/portal)
+## Set the cache property
 
-1. On the left, select **Indexers**, and then select **Add indexer**.
-1. Provide an indexer name and an existing index, data source, and skillset.
-1. Enable incremental caching and set the Azure Storage account.
+Use this procedure for both new and existing indexers.
 
-   :::image type="content" source="media/search-incremental-index/portal-option.png" alt-text="Screenshot of the Azure portal option for enrichment cache.":::
-
-### [**REST**](#tab/rest)
+In the indexer definition, set `cache` with:
 
-On new indexers, add the `cache` property in the indexer definition payload when calling Create or Update Indexer.
-
-We recommend the latest preview REST API for [Create or Update Indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true).
-
-```https
-POST https://[service name].search.windows.net/indexers?api-version=2025-11-01-preview
-    {
-        "name": "<YOUR-INDEXER-NAME>",
-        "targetIndexName": "<YOUR-INDEX-NAME>",
-        "dataSourceName": "<YOUR-DATASOURCE-NAME>",
-        "skillsetName": "<YOUR-SKILLSET-NAME>",
-        `cache` : {
-            "storageConnectionString" : "<YOUR-STORAGE-ACCOUNT-CONNECTION-STRING>",
-            "enableReprocessing": true
-        },
-    "fieldMappings" : [],
-    "outputFieldMappings": [],
-    "parameters": []
-    }
-```
-
----
++ (Required) `storageConnectionString` set to an Azure Storage connection string.
++ (Optional) `enableReprocessing` (`true` by default). Set it to `false` to suspend incremental enrichment temporarily, and switch it back to `true` later.
 
-## Enable on existing indexers
-
-For existing indexers that already have a skillset, use the following steps to add caching. As a one-time operation, reset and rerun the indexer in full to load the cache.
-
-### Step 1: Get the indexer definition
-
-Start with a valid, work indexer that has these components: data source, skillset, index. Using an API client, send a [GET Indexer](/rest/api/searchservice/indexers/get?view=rest-searchservice-2025-11-01-preview&preserve-view=true) request to retrieve the indexer. When you use the preview API version to the GET the indexer, a `cache` property set to null is added to the definition automatically.
-
-```http
-GET https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]?api-version=2025-11-01-preview
-    Content-Type: application/json
-    api-key: [YOUR-ADMIN-KEY]
-```
-
-### Step 2: Set the cache property
+### [**Azure portal**](#tab/portal)
 
-In the index definition, modify `cache` to include the following required and optional properties:
+1. On the left, select **Indexers**.
+1. Select **Add indexer** to create a new indexer, or open an existing one in JSON edit mode.
+1. Enable incremental enrichment, set the enrichment cache storage account, and save the indexer.
 
-+ (Required) `storageConnectionString` must be set to an Azure Storage connection string.
-+ (Optional) `enableReprocessing` boolean property (`true` by default), indicates that incremental enrichment is enabled. Set to `false` if you want to suspend incremental processing while other resource-intensive operations, such as indexing new documents, are underway and then switch back to `true` later.
+   :::image type="content" source="media/search-incremental-index/portal-option.png" alt-text="Screenshot of the Azure portal option for enrichment cache.":::
 
-```http
-POST https://[service name].search.windows.net/indexers?api-version=2025-11-01-preview
-    {
-        "name": "<YOUR-INDEXER-NAME>",
-        "targetIndexName": "<YOUR-INDEX-NAME>",
-        "dataSourceName": "<YOUR-DATASOURCE-NAME>",
-        "skillsetName": "<YOUR-SKILLSET-NAME>",
-        `cache` : {
-            "storageConnectionString" : "<YOUR-STORAGE-ACCOUNT-CONNECTION-STRING>",
-            "enableReprocessing": true
-        },
-        "fieldMappings" : [],
-        "outputFieldMappings": [],
-        "parameters": []
-    }
-```
+1. Reset the indexer if it already exists.
 
-### Step 3: Reset the indexer
+1. Run the indexer. This one-time full rebuild seeds the cache. After it's loaded, incremental reuse applies on subsequent runs.
 
-[Reset Indexer](/rest/api/searchservice/indexers/reset) is required when setting up incremental enrichment for existing indexers to ensure all documents are in a consistent state. You can use the Azure portal or an API client for this task.
+### [**REST**](#tab/rest)
 
-```https
-POST https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]/reset?api-version=2025-11-01-preview
-    Content-Type: application/json
-    api-key: [YOUR-ADMIN-KEY]
-```
+We recommend that you do a [GET Indexer](/rest/api/searchservice/indexers/get?view=rest-searchservice-2025-11-01-preview&preserve-view=true) if you're editing an existing indexer.
+
+1. Use the latest preview API for [Create or Update Indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true).
+
+    ```http
+    PUT https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]?api-version=2025-11-01-preview
+        Content-Type: application/json
+        api-key: [YOUR-ADMIN-KEY]
+        {
+            "name": "<YOUR-INDEXER-NAME>",
+            "targetIndexName": "<YOUR-INDEX-NAME>",
+            "dataSourceName": "<YOUR-DATASOURCE-NAME>",
+            "skillsetName": "<YOUR-SKILLSET-NAME>",
+            "cache": {
+                "storageConnectionString": "<YOUR-STORAGE-ACCOUNT-CONNECTION-STRING>",
+                "enableReprocessing": true
+            },
+            "fieldMappings": [],
+            "outputFieldMappings": [],
+            "parameters": []
+        }
+    ```
 
-### Step 4: Save the indexer
+1. [Reset the indexer](/rest/api/searchservice/indexers/reset) if it already exists.
 
-[Update Indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) with a PUT request, where the body of the request includes `cache`.
+1. [Run the indexer](/rest/api/searchservice/indexers/run). This one-time full rebuild seeds the cache. After it's loaded, incremental reuse applies on subsequent runs.
 
-```http
-PUT https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]?api-version=2025-11-01-preview
-    Content-Type: application/json
-    api-key: [YOUR-ADMIN-KEY]
-    {
-        "name" : "<YOUR-INDEXER-NAME>",
-        ...
-        `cache`: {
-            "storageConnectionString": "<YOUR-STORAGE-ACCOUNT-CONNECTION-STRING>",
-            "enableReprocessing": true
-        }
-    }
-```
+    ```http
+    POST https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]/run?api-version=2025-11-01-preview
+        Content-Type: application/json
+        api-key: [YOUR-ADMIN-KEY]
+    ```
 
 If you now issue another GET request on the indexer, the response from the service includes an `ID` property in the cache object. The string is appended to the name of the container containing all the cached results and intermediate state of each document processed by this indexer. The ID is used to uniquely name the cache in Blob storage.
 
 ```http
-    `cache`: {
+    "cache": {
         "ID": "<ALPHA-NUMERIC STRING>",
         "enableReprocessing": true,
         "storageConnectionString": "DefaultEndpointsProtocol=https;AccountName=<YOUR-STORAGE-ACCOUNT>;AccountKey=<YOUR-STORAGE-KEY>;EndpointSuffix=core.windows.net"
     }
 ```
 
-### Step 5: Run the indexer
-
-To run indexer, you can use the Azure portal or the API. In the Azure portal, from the indexers list, select the indexer and select **Run**. One advantage to using the Azure portal is that you can monitor indexer status, note the duration of the job, and how many documents are processed. Portal pages are refreshed every few minutes.
-
-Alternatively, you can use REST to [run the indexer](/rest/api/searchservice/indexers/run):
+## Check for cached output
 
-```http
-POST https://[YOUR-SEARCH-SERVICE].search.windows.net/indexers/[YOUR-INDEXER-NAME]/run?api-version=2025-11-01-preview
-Content-Type: application/json
-api-key: [YOUR-ADMIN-KEY]
-```
+1. Sign in to the Azure portal and find your Azure Storage account.
 
-> [!NOTE]
-> A reset and rerun of the indexer results in a full rebuild so that content can be cached. All cognitive enrichments will be rerun on all documents. Reusing enriched content from the cache begins after the cache is loaded.
->
+1. Use Storage Browser to review containers and tables.
 
-## Check for cached output
+   + The container name is  `ms-az-search-indexercache-<some-alphanumeric-string>`.
 
-Find the cache in Azure Storage, under Blob container. The container name is  `ms-az-search-indexercache-<some-alphanumeric-string>`.
+   + Table names are `MsAzSearchIndexerCacheIndex<alpha-numeric-string>`
 
 A cache is created and used by an indexer. Its content isn't human readable.
 
-To verify whether the cache is operational, modify a skillset and run the indexer, then compare before-and-after metrics for execution time and document counts. 
+To verify whether the cache is operational, modify a skillset and run the indexer, then compare before-and-after metrics for execution time and document count.
 
-Skillsets that include image analysis and Optical Character Recognition (OCR) of scanned documents make good test cases. If you modify a downstream text skill or any skill that isn't image-related, the indexer can retrieve all of the previously processed image and OCR content from cache, updating and processing only the text-related changes indicated by your edits.  You can expect to see fewer documents in the indexer execution document count, shorter execution times, and fewer charges on your bill. 
+Skillsets that include image analysis and Optical Character Recognition (OCR) of scanned documents make good test cases. If you modify a downstream text skill or any skill that isn't image-related, the indexer can retrieve previously processed image and OCR content from cache, and process only text-related changes from your edits. You can expect fewer documents in indexer execution counts, shorter execution times, and lower costs.
 
 The [file set](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/ai-enrichment-mixed-media) used in [cog-search-demo tutorials](tutorial-skillset.md) is a useful test case because it contains 14 files of various formats JPG, PNG, HTML, DOCX, PPTX, and other types. Change `en` to `es` or another language in the text translation skill for proof-of-concept testing of incremental enrichment.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンリッチメントキャッシュの設定に関するドキュメントの更新"
}
```

### Explanation
この変更には、`articles/search/enrichment-cache-how-to-configure.md`ファイルが含まれており、エンリッチメントキャッシュの設定に関する情報が大幅に更新されました。具体的には、60行の追加と109行の削除があり、合計で169の変更が行われました。

主な変更点には、エンリッチメントパイプラインに対するキャッシュの追加に関する説明が、より明確で簡潔に更新されたことが含まれています。例えば、「スキルセット」と「インデクサー」の定義変更による文書ツリーのどの部分を刷新するかの判断がより強調されています。また、キャッシュされたコンテンツがAzureストレージに配置される際の接続文字列についての詳細も刷新されました。

さらに、新しいインデクサーや既存のインデクサーでのキャッシュプロパティ設定のプロセスも簡素化され、AzureポータルやREST APIを利用した具体的な手順が改訂されました。これにより、ユーザーはエンリッチメントキャッシュの管理と設定がスムーズに行えるようになります。

この文書の更新により、エンリッチメントキャッシュに関するユーザーの理解が向上し、より効果的な利用が可能となることが期待されます。

## articles/search/enrichment-cache-how-to-manage.md{#item-a972bd}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 08/27/2025
+ms.date: 02/24/2026
 ms.update-cycle: 180-days
 ms.custom:
   - ignite-2023
@@ -20,7 +20,7 @@ ms.custom:
 
 An *enrichment cache* is an optional feature that stores reusable enriched content created during [skillset execution](cognitive-search-working-with-skillsets.md) so that only new and changed skills and documents incur standard processing charges during future indexer and skillset processing. 
 
-The cache contains the output from [document cracking](search-indexer-overview.md#document-cracking), plus the outputs of each skill for every document. Although caching is billable (it uses Azure Storage), the overall cost of enrichment is reduced because the costs of storage are less than image extraction and AI processing.
+The enrichment cache is created in Azure Storage. The cache contains the output from [document cracking](search-indexer-overview.md#document-cracking), plus the outputs of each skill for every document. Although caching is billable (it uses Azure Storage), the overall cost of enrichment is reduced because the costs of storage are less than image extraction and AI processing.
 
 If you have configured an enrichment cache, this article explains how to manage skill and data source updates so that you get maximum utility from cached enrichments.
 
@@ -37,14 +37,12 @@ If you have configured an enrichment cache, this article explains how to manage
 
 ## Cache configuration
 
-Physically, the cache is stored in a blob container or table in your Azure Storage account, one per indexer. Each indexer is assigned a unique and immutable cache identifier that corresponds to the container it's using.
+Physically, the cache is stored in a blob container and tables in your Azure Storage account, one per indexer. Each indexer is assigned a unique and immutable cache identifier that corresponds to the container it's using.
 
-The cache is created when you specify the "cache" property and run the indexer. Only enriched content can be cached. If your indexer doesn't have an attached skillset, then caching doesn't apply. 
+The cache is created when you specify the `cache` property and run the indexer. Only enriched content can be cached. If your indexer doesn't have an attached skillset, then caching doesn't apply. 
 
 The following example illustrates an indexer with caching enabled. See [Configure enrichment caching](enrichment-cache-how-to-configure.md) for full instructions. 
 
-To set the cache property, use latest preview REST API for [Create or Update Indexer](/rest/api/searchservice/indexers/create-or-update?view=rest-searchservice-2025-11-01-preview&preserve-view=true) or a preview Azure SDK package that provides the feature. You can also enable enrichment caching in the Import data wizard in the Azure portal.
-
 ```json
 POST https://[YOUR-SEARCH-SERVICE-NAME].search.windows.net/indexers?api-version=2025-11-01-preview
     {
@@ -66,7 +64,7 @@ POST https://[YOUR-SEARCH-SERVICE-NAME].search.windows.net/indexers?api-version=
 
 The lifecycle of the cache is managed by the indexer. If an indexer is deleted, its cache is also deleted. If the `cache` property on the indexer is set to null or the connection string is changed, the existing cache is deleted on the next indexer run. 
 
-While incremental enrichment is designed to detect and respond to changes with no intervention on your part, there are parameters you can use to invoke specific behaviors:
+While incremental enrichment is designed to detect and respond to changes with no intervention on your part, you can set parameters to invoke specific behaviors:
 
 + [Prioritize new documents](#Prioritize-new-documents)
 + [Bypass skillset checks](#Bypass-skillset-checks)
@@ -77,9 +75,9 @@ While incremental enrichment is designed to detect and respond to changes with n
 
 ### Prioritize new documents
 
-The cache property includes an `enableReprocessing` parameter. It's used to control processing over incoming documents already represented in the cache. When true (default), documents already in the cache are reprocessed when you rerun the indexer, assuming your skill update affects that doc. 
+The `cache` property includes an `enableReprocessing` parameter that controls whether cached content is reprocessed. When true (default), cached documents are reprocessed when you rerun the indexer if a skill update affects them.
 
-When false, existing documents aren't reprocessed, effectively prioritizing new, incoming content over existing content. You should only set enableReprocessing to false on a temporary basis. Having enableReprocessing set to true most of the time ensures that all documents, both new and existing, are valid per the current skillset definition.
+When false, existing documents aren't reprocessed, effectively prioritizing new content. Set `enableReprocessing` to false only temporarily. Keeping it true most of the time ensures that both new and existing documents remain valid for the current skillset definition.
 
 <a name="Bypass-skillset-checks"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンリッチメントキャッシュ管理に関するドキュメントの更新"
}
```

### Explanation
この変更は、`articles/search/enrichment-cache-how-to-manage.md`ファイルに関するもので、エンリッチメントキャッシュの管理方法に関する情報が新しく更新されました。具体的には、7行の追加と9行の削除があり、合計で16の変更が行われています。

主に、エンリッチメントキャッシュの定義や機能の説明が改良されており、キャッシュがAzureストレージに作成されることが強調されています。以前はキャッシュを物理的にどのように管理するかについての文が改善され、情報がより明確に整理されています。特に、キャッシュの設定方法がより具体的に示され、`cache`プロパティの使用指針も強調されています。

また、エンリッチメントキャッシュのライフサイクル管理の仕組みについても、インデクサーの削除に伴いキャッシュも削除される点が明確に示されています。更に、インクリメンタルエンリッチメントにおけるパラメータの利用についても、具体的に説明が追加され、新たに「新しい文書の優先度」や「スキルセットチェックのバイパス」に関する情報が詳述されています。

これにより、ユーザーはエンリッチメントキャッシュの管理方法についてより深く理解し、効率的に活用できるようになることが期待されます。

## articles/search/includes/resource-authentication-identity.md{#item-bcdb0d}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,27 @@
+---
+title: Include File
+description: Include file for Azure AI Search authentication to Microsoft Foundry.
+author: haileytap 
+ms.author: haileytapia 
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 02/11/2026
+# Use this file to describe authentication for Foundry-integrated scenarios.
+---
+
+Azure AI Search connects to Microsoft Foundry models for certain skills, vectorizers, and agentic retrieval workloads. You can configure this connection to use Microsoft Entra ID authentication and role-based access.
+
+To configure the recommended role-based access:
+
+1. [Create a managed identity](../search-security-enable-roles.md) for your search service.
+
+1. [Assign the following roles](/azure/ai-foundry/concepts/rbac-foundry) in your Azure OpenAI resource or Microsoft Foundry resource.
+
+    | Target Endpoint | Required Role | Scope |
+    |-|-|-|
+    | GPT-4/5 & text-embedding-3 | Cognitive Services OpenAI User | Azure OpenAI Resource |
+    | Azure AI Vision multimodal 4.0 | Cognitive Services User | Azure AI Multi-service Resource |
+    | Content Understanding  | Cognitive Services User | Microsoft Foundry Resource |
+    | Foundry Model Orchestration | Azure AI User | Foundry Project |
+
+1. Choose **Managed identity** and then assign your [search service managed identity](search-how-to-managed-identities.md).
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "リソース認証に関する新しいインクルードファイルの追加"
}
```

### Explanation
この変更は、`articles/search/includes/resource-authentication-identity.md`という新しいファイルが追加されたことに関するもので、合計で27行の内容が記述されています。このファイルは、Azure AI SearchがMicrosoft Foundryに統合されるシナリオにおける認証の設定方法を説明しています。

具体的には、Azure AI Searchが特定のスキルやベクトライザー、エージェンティックリトリーバル作業負荷に対してMicrosoft Foundryモデルに接続する際の設定について述べられています。このファイルでは、Microsoft Entra ID認証とロールベースのアクセス制御を利用する方法が示されています。

主な内容としては、まずマネージドアイデンティティを作成し、その後、Azure OpenAIリソースやMicrosoft Foundryリソースに必要な役割を割り当てる手順が詳細に示されています。具体的には、GPT-4/5などのエンドポイントに必要な役割やスコープが表形式で整理されており、ユーザーが理解しやすいように構成されています。

この新しいインクルードファイルの追加により、Azure AI Searchを使用する際の認証プロセスが明確になり、利用者がMicrosoft Foundryとの統合をより効果的に実施できるようになることが期待されます。

## articles/search/media/tutorial-multimodal/normalized-image-in-storage.png{#item-71b042}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "正規化された画像の追加"
}
```

### Explanation
この変更は、`articles/search/media/tutorial-multimodal/normalized-image-in-storage.png`という新しい画像ファイルが追加されたことに関するものです。このファイルは、マルチモーダルチュートリアルで使用される正規化された画像を表しています。

画像ファイルの追加により、ドキュメント内で視覚的なコンテンツを強化し、ユーザーがマルチモーダル機能やその利用方法を理解する際の補助となります。この画像は、チュートリアルの一部として、特定の実行手順や概念を示すために使用される可能性があります。

この新しいメディアの追加により、ユーザーがAzure AIの機能を適切に理解し、実際に利用する際の体験が向上することが期待されます。

## articles/search/multimodal-search-overview.md{#item-d82192}

<details>
<summary>Diff</summary>
````diff
@@ -118,8 +118,5 @@ To help you get started with multimodal search in Azure AI Search, here's a coll
 | Content | Description |
 |--|--|
 | [Quickstart: Multimodal search in the Azure portal](search-get-started-portal-image-search.md) | Create and test a multimodal index in the Azure portal using the wizard and Search Explorer. |
-| [Tutorial: Verbalize images using generative AI](tutorial-document-extraction-image-verbalization.md) | Extract text and images, verbalize diagrams, and embed the resulting descriptions and text into a searchable index. |
-| [Tutorial: Vectorize images and text](tutorial-document-extraction-multimodal-embeddings.md) | Use a vision-text model to embed both text and images directly, enabling visual-similarity search over scanned PDFs. |
-| [Tutorial: Verbalize images from a structured document layout](tutorial-document-layout-image-verbalization.md) | Apply layout-aware chunking and diagram verbalization, capture location metadata, and store cropped images for precise citations and page highlights. |
-| [Tutorial: Vectorize from a structured document layout](tutorial-document-layout-multimodal-embeddings.md) | Combine layout-aware chunking with unified embeddings for hybrid semantic and keyword search that returns exact hit locations. |
+| [Multimodal tutorial](tutorial-multimodal.md) | Extract text and images, chunk data, and vectorize the chunks for similarity search and other retrieval patterns. |
 | [Sample app: Multimodal RAG GitHub repository](https://aka.ms/azs-multimodal-sample-app-repo) | An end-to-end, code-ready RAG application with multimodal capabilities that surfaces both text snippets and image annotations. Ideal for jump-starting enterprise copilots. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダル検索の概要に関するドキュメントの更新"
}
```

### Explanation
この変更は、`articles/search/multimodal-search-overview.md`というドキュメントの内容が修正されたことを示しています。具体的には、1行の追加と4行の削除が行われ、合計で5つの変更が加えられています。

変更内容には、マルチモーダル検索に関するチュートリアルの整頓が含まれています。以前は複数のチュートリアルが個別にリストされていましたが、新しいエントリとして「[Multimodal tutorial](tutorial-multimodal.md)」が追加され、これによりより包括的な一つのチュートリアルとして、テキストと画像の抽出、データのチャンク化、類似検索やその他の取得パターンに向けたベクトル化のプロセスが説明されています。

この更新は、ユーザーにとって、マルチモーダル検索機能を理解し利用するための情報を整理し、関連するプロセスをより容易に参照できるようにすることを目的としています。結果として、情報のアクセス性が改善され、利用者が必要なリソースを迅速に見つけるのに役立つことが期待されます。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -134,7 +134,7 @@ The following sections explain how each approach solves specific RAG challenges.
 + Filter-based security at query time for other data sources
 + Network isolation via private endpoints
 
-[Learn more about security](search-security-overview.md).
+[Learn more about security](search-security-built-in.md).
 
 <!-- OLD INTRO
 Retrieval-augmented Generation (RAG) is a design pattern in AI that augments the capabilities of a pretrained large language model (LLM) by adding newer, specialized, or proprietary content to help answer questions. To get that content, you typically need an information retrieval component. Azure AI Search is an information retrieval solution that's designed to solve the challenges of RAG implementations.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAG概要ドキュメントのセキュリティリンクの修正"
}
```

### Explanation
この変更は、`articles/search/retrieval-augmented-generation-overview.md`というドキュメントの内容が修正されたことを示しています。具体的には、セキュリティに関するリンクが更新され、1行の追加と1行の削除が行われています。

以前は、セキュリティに関する情報へのリンクが「[Learn more about security](search-security-overview.md)」となっていましたが、現在は「[Learn more about security](search-security-built-in.md)」に変更されています。この変更により、ユーザーはセキュリティに関するより具体的な情報にアクセスできるようになっています。

このリンクの更新は、ドキュメントの正確性と関連性を向上させるためのものであり、読者が必要な情報を迅速に見つけられるように配慮されています。全体として、情報の整合性と利用者の利便性の向上を目的としています。

## articles/search/search-create-service-portal.md{#item-f90159}

<details>
<summary>Diff</summary>
````diff
@@ -41,7 +41,7 @@ Some properties are fixed for the lifetime of the search service. Before you cre
 | [Name](#name-your-service) | Becomes part of the URL endpoint. The name must be unique and follow naming rules. |
 | [Region](search-region-support.md) | Determines data residency and availability of certain features. For example, semantic ranker and Azure AI integration have region requirements. Choose a region that supports the features you need. |
 | [Tier](search-sku-tier.md) | Determines infrastructure, service limits, and billing. Some features aren't available on lower or specialized tiers. After you create your service, you can [switch between Basic and Standard (S1, S2, and S3) tiers](search-capacity-planning.md#change-your-pricing-tier). |
-| [Compute type](search-security-overview.md#data-in-use) | Determines virtualization and security model. You can choose between standard VMs (recommended) and confidential VMs, which are intended for select workloads requiring data-in-use privacy and isolation. |
+| [Compute type](search-security-best-practices.md#optional-enable-confidential-computing) | Determines virtualization and security model. You can choose between standard VMs (recommended) and confidential VMs, which are intended for select workloads requiring data-in-use privacy and isolation. |
 ## Subscribe to Azure
 
 Azure AI Search requires a free or Standard Azure subscription.
@@ -149,7 +149,7 @@ The compute type determines the virtualization and security model used to deploy
 
 + **Confidential** (10% surcharge) uses [Azure confidential computing](/azure/confidential-computing/use-cases-scenarios) to isolate processing in a hardware-based trusted execution environment, protecting unencrypted data in use from unauthorized access. Recommended only if you have advanced privacy, compliance, or regulatory requirements.
 
-Confidential computing has limited regional availability, disables or restricts certain features, and increases the cost of running your search service. For a detailed comparison of both compute types, see [Data in use](search-security-overview.md#data-in-use).
+Confidential computing has limited regional availability, disables or restricts certain features, and increases the cost of running your search service. For a detailed comparison of both compute types, see [(Optional) Enable confidential computing](search-security-best-practices.md#optional-enable-confidential-computing).
 
 ## Create your service
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービスポータルドキュメントのコンピュータタイプ参照の変更"
}
```

### Explanation
この変更は、`articles/search/search-create-service-portal.md`というドキュメントにおけるコンピュータタイプに関する記述が修正されたことを示しています。具体的には、2行の追加と2行の削除が行われ、合計で4つの変更があります。

最も重要な変更は、コンピュータタイプに関連するリンクが更新されたことです。以前は、「[Data in use](search-security-overview.md#data-in-use)」にリンクされていましたが、現在は「[(Optional) Enable confidential computing](search-security-best-practices.md#optional-enable-confidential-computing)」に変更されています。このリンクの更新により、ユーザーは機密コンピューティングに関する最新のベストプラクティスを参照できるようになっています。

このような変更は、ドキュメントの正確性と利用者にとっての有用性の向上を目的としており、情報へのアクセスを容易にすることで、ユーザーの理解を深める助けになります。全体として、情報の整合性と関連性を高め、ユーザーが必要とする情報を迅速に見つけられるようにすることが意図されています。

## articles/search/search-faq-frequently-asked-questions.yml{#item-eab2ba}

<details>
<summary>Diff</summary>
````diff
@@ -195,7 +195,7 @@ sections:
       - question: |
           Does Azure AI Search send customer data to other services for processing?
         answer: |
-          Yes. Skills and vectorizers make [outbound calls from Azure AI Search](search-security-overview.md) to other Azure resources or external models that you specify for embedding or chat. Calls to those APIs typically contain raw content to be processed or queries that are vectorized by an embedding model. For Azure-to-Azure connections, the service sends requests over the internal network. If you add a custom skill or vectorizer, the indexer sends content to the URI provided in the custom skill over the public network unless you configure a [shared private link](search-indexer-howto-access-private.md).
+          Yes. Skills and vectorizers make [outbound calls from Azure AI Search](search-security-best-practices.md#configure-outbound-connections) to other Azure resources or external models that you specify for embedding or chat. Calls to those APIs typically contain raw content to be processed or queries that are vectorized by an embedding model. For Azure-to-Azure connections, the service sends requests over the internal network. If you add a custom skill or vectorizer, the indexer sends content to the URI provided in the custom skill over the public network unless you configure a [shared private link](search-indexer-howto-access-private.md).
 
       - question: |
           Does Azure AI Search process customer data in other regions?
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQドキュメントのアウトバウンドコールに関するリンクの更新"
}
```

### Explanation
この変更は、`articles/search/search-faq-frequently-asked-questions.yml`というファイルの内容が修正されたことを示しています。この修正では、1行の追加と1行の削除が行われ、合計で2つの変更が存在します。

具体的には、「Azure AI Searchが顧客データを他のサービスに送信するか」という質問に対する回答で、関連するリンクが更新されました。以前は「[outbound calls from Azure AI Search](search-security-overview.md)」となっていましたが、現在は「[outbound calls from Azure AI Search](search-security-best-practices.md#configure-outbound-connections)」に変更されています。

このリンクの更新により、ユーザーはAzure AI Searchのアウトバウンド接続に関する最新のベストプラクティスを参照できるようになり、より正確で有用な情報を得ることができます。この変更はユーザーの理解を深め、ドキュメントの信頼性を向上させることを目的としています。全体として、情報の整合性を高め、利用者にとっての利便性を向上させることに寄与しています。

## articles/search/search-features-list.md{#item-d34448}

<details>
<summary>Diff</summary>
````diff
@@ -83,7 +83,7 @@ The following table summarizes features by category. There's feature parity in a
 | Category&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Features |
 |-------------------|----------|
 | Network security | [**IP rules for inbound firewall support**](service-configure-firewall.md) allows you to set up IP ranges over which the search service accepts requests. </br></br>[**Create a private endpoint**](service-create-private-endpoint.md) using Azure Private Link to force all requests through a virtual network. </br></br>[**Network security perimeter**](search-security-network-security-perimeter.md) support allows you to join Azure AI Search to a network security perimeter that includes other Azure resources so that you can manage network access holistically. |
-| Data encryption | [**Microsoft-managed encryption-at-rest**](search-security-overview.md#encryption) is built into the internal storage layer and is irrevocable. </br></br>[**Customer-managed encryption keys (CMK)**](search-security-manage-encryption-keys.md) that you create and manage in Azure Key Vault can be used for supplemental encryption of indexes and synonym maps. For services created after August 1 2020, CMK encryption extends to data on temporary disks, for full double encryption of indexed content.|
+| Data encryption | [**Microsoft-managed encryption-at-rest**](search-security-built-in.md#data-encryption) is built into the internal storage layer and is irrevocable. </br></br>[**Customer-managed encryption keys (CMK)**](search-security-manage-encryption-keys.md) that you create and manage in Azure Key Vault can be used for supplemental encryption of indexes and synonym maps. For services created after August 1 2020, CMK encryption extends to data on temporary disks, for full double encryption of indexed content.|
 | Inbound access | [**Role-based access control**](search-security-rbac.md) assigns roles to users and groups in Microsoft Entra ID for controlled access to search content and operations. You can also use [**key-based authentication**](search-security-api-keys.md) if you don't want to use role assignments. </br></br>[**Document-level access control (preview)**](search-document-level-access-overview.md) filters out search results that a user isn't authorized to see. For several data sources, if the data source provides an access control model, you can configure an index to inherit the user permission metadata. |
 | Outbound security (indexers) | [**Data connections through private endpoints**](search-indexer-howto-access-private.md) allows an indexer to connect to Azure resources that are protected through Azure Private Link. </br></br>[**Data connections through managed identities**](search-how-to-managed-identities.md) authenticates connections to Azure resources using a Microsoft Entra security principal, which eliminates storage and passing of hardcoded API keys.</br></br>[**Data access using a trusted identity**](search-how-to-managed-identities.md) means that connection strings to external data sources can omit user names and passwords. When an indexer connects to the data source, the resource allows the connection if the search service was previously registered as a trusted service (applies to Azure Storage only). |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ暗号化のセクション内のリンクの更新"
}
```

### Explanation
この変更は、`articles/search/search-features-list.md`というファイルの内容が修正されたことを示しています。この変更では、1行の追加と1行の削除が行われ、合計で2つの変更が存在します。

具体的には、「データ暗号化」セクション内のリンクが更新されました。以前は「[**Microsoft-managed encryption-at-rest**](search-security-overview.md#encryption)」となっていましたが、現在は「[**Microsoft-managed encryption-at-rest**](search-security-built-in.md#data-encryption)」に変更されています。このリンクの更新により、ユーザーはMicrosoftが管理する暗号化の詳細についてより正確な情報を得られるようになっています。

この変更は、ドキュメントの正確性と利用者にとっての有用性を向上させることを目的としており、最新のリソースにアクセスしやすくすることに寄与しています。全体として、情報の整合性を高め、ユーザーが関連情報を簡単に見つけられるようにする改良が施されています。

## articles/search/search-get-started-arm.md{#item-9287ad}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ In this quickstart, you use an Azure Resource Manager (ARM) template to deploy a
 
 [!INCLUDE [About Azure Resource Manager](~/reusable-content/ce-skilling/azure/includes/resource-manager-quickstart-introduction.md)]
 
-Only those properties included in the template are used in the deployment. If more customization is required, such as [setting up network security](search-security-overview.md#network-security), you can update the service as a post-deployment task. To customize an existing service with the fewest steps, use [Azure CLI](search-manage-azure-cli.md) or [Azure PowerShell](search-manage-powershell.md). If you're evaluating preview features, use the [Management REST API](search-manage-rest.md).
+Only those properties included in the template are used in the deployment. If more customization is required, such as [setting up network security](search-security-best-practices.md#configure-network-security), you can update the service as a post-deployment task. To customize an existing service with the fewest steps, use [Azure CLI](search-manage-azure-cli.md) or [Azure PowerShell](search-manage-powershell.md). If you're evaluating preview features, use the [Management REST API](search-manage-rest.md).
 
 Assuming your environment meets the prerequisites and you're familiar with using ARM templates, select the **Deploy to Azure** button. The template will open in the Azure portal.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ネットワークセキュリティ設定のリンク更新"
}
```

### Explanation
この変更は、`articles/search/search-get-started-arm.md`というファイルの内容が修正されたことを示しています。この修正では、1行の追加と1行の削除が行われ、合計で2つの変更が存在します。

具体的には、ARMテンプレートを使用した展開に関するセクションにおいて、「ネットワークセキュリティの設定」に関するリンクが更新されました。以前は「[setting up network security](search-security-overview.md#network-security)」となっていましたが、現在は「[setting up network security](search-security-best-practices.md#configure-network-security)」に変更されています。このリンクの更新により、ユーザーはネットワークセキュリティの設定に関する最新のベストプラクティス情報にアクセスできるようになります。

この変更は、ドキュメントの正確性と有用性を向上させることを目的としており、ユーザーが適切な情報源に基づいて設定を行えるようにすることに寄与しています。全体として、情報の整合性を高め、ユーザーが関連情報をより簡単に見つけられるようにする改良が行われています。

## articles/search/search-get-started-bicep.md{#item-731b0e}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ In this quickstart, you use a Bicep file to deploy an Azure AI Search service in
 
 [!INCLUDE [About Bicep](~/reusable-content/ce-skilling/azure/includes/resource-manager-quickstart-bicep-introduction.md)]
 
-Only those properties included in the template are used in the deployment. If more customization is required, such as [setting up network security](search-security-overview.md#network-security), you can update the service as a post-deployment task. To customize an existing service with the fewest steps, use [Azure CLI](search-manage-azure-cli.md) or [Azure PowerShell](search-manage-powershell.md). If you're evaluating preview features, use the [Management REST API](search-manage-rest.md).
+Only those properties included in the template are used in the deployment. If more customization is required, such as [setting up network security](search-security-best-practices.md#configure-network-security), you can update the service as a post-deployment task. To customize an existing service with the fewest steps, use [Azure CLI](search-manage-azure-cli.md) or [Azure PowerShell](search-manage-powershell.md). If you're evaluating preview features, use the [Management REST API](search-manage-rest.md).
 
 > [!TIP]
 > For an alternative Bicep template that deploys Azure AI Search with a pre-configured indexer to Cosmos DB for NoSQL, see [Bicep deployment of Azure AI Search](https://github.com/Azure-Samples/azure-search-deployment-template). There's no bicep template support for Azure AI Search data plane operations like creating an index, but you can add a module that calls REST APIs. The sample includes a module that creates an index, data source connector, and an indexer that refreshes from Cosmos DB at 5-minute intervals.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ネットワークセキュリティ設定のリンク更新"
}
```

### Explanation
この変更は、`articles/search/search-get-started-bicep.md`というファイルの内容が修正されたことを示しています。修正内容としては、1行の追加と1行の削除が行われ、合計で2つの変更が存在します。

具体的には、Bicepファイルを使用したAzure AI Searchサービスの展開に関するセクションにおいて、「ネットワークセキュリティの設定」というリンクが更新されました。以前は「[setting up network security](search-security-overview.md#network-security)」となっていましたが、現在は「[setting up network security](search-security-best-practices.md#configure-network-security)」に変更されています。このリンクの更新により、ユーザーはネットワークセキュリティの設定に関する最新のベストプラクティス情報にアクセスできるようになります。

この変更は、ドキュメントの正確性と有用性を向上させることを目的としており、ユーザーが適切な情報源に基づいて設定を行えるようにすることに寄与しています。全体として、情報の整合性を高め、ユーザーが関連情報をより簡単に見つけられるようにする改良が行われています。

## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -473,9 +473,4 @@ To query your multimodal index:
 
 ## Next steps
 
-This quickstart introduced you to the **Import data (new)** wizard, which creates all of the necessary objects for multimodal search. To explore each step in detail, see the following tutorials:
-
-+ [Tutorial: Verbalize images using generative AI](tutorial-document-extraction-image-verbalization.md)
-+ [Tutorial: Verbalize images from a structured document layout](tutorial-document-layout-image-verbalization.md)
-+ [Tutorial: Vectorize images and text](tutorial-document-extraction-multimodal-embeddings.md)
-+ [Tutorial: Vectorize from a structured document layout](tutorial-document-layout-multimodal-embeddings.md)
+This quickstart introduced you to the **Import data (new)** wizard, which creates all of the necessary objects for multimodal search. To explore each step in detail, see the [Multimodal tutorial](tutorial-multimodal.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダルチュートリアルへのリンク更新"
}
```

### Explanation
この変更は、`articles/search/search-get-started-portal-image-search.md`というファイルの内容が修正されたことを示しています。変更内容としては、1行の追加と6行の削除が行われ、合計で7つの変更が存在します。

具体的には、このクイックスタートガイドでは、**Import data (new)**ウィザードを紹介しており、これはマルチモーダル検索のために必要なすべてのオブジェクトを作成します。以前の内容では、いくつかの様々なチュートリアルへの個別のリンクが記載されていましたが、これが削除され、代わりに「[Multimodal tutorial](tutorial-multimodal.md)」という1つのリンクが追加されました。この変更により、ユーザーはマルチモーダル検索の詳細を一つの包括的なチュートリアルから探求できるようになりました。

この更新は、ユーザーに対して関連情報をより簡潔に提供することを目的としており、混乱を減らし、必要な情報にスムーズにアクセスできるようにしています。全体として、情報の整理とナビゲーションの向上を図った改良が行われています。

## articles/search/search-how-to-create-indexers.md{#item-de71fb}

<details>
<summary>Diff</summary>
````diff
@@ -228,7 +228,7 @@ There are several ways to run an indexer:
 
 Scheduled execution is usually implemented when you have a need for incremental indexing so that you can pick up the latest changes. As such, scheduling has a dependency on change detection.
 
-Indexers are one of the few subsystems that make overt outbound calls to other Azure resources. In terms of Azure roles, indexers don't have separate identities; a connection from the search engine to another Azure resource is made using the [system or user-assigned managed identity](search-how-to-managed-identities.md) of a search service. If the indexer connects to an Azure resource on a virtual network, you should create a [shared private link](search-indexer-howto-access-private.md) for that connection. For more information about secure connections, see [Security in Azure AI Search](search-security-overview.md).
+Indexers are one of the few subsystems that make overt outbound calls to other Azure resources. In terms of Azure roles, indexers don't have separate identities; a connection from the search engine to another Azure resource is made using the [system or user-assigned managed identity](search-how-to-managed-identities.md) of a search service. If the indexer connects to an Azure resource on a virtual network, you should create a [shared private link](search-indexer-howto-access-private.md) for that connection. For more information, see [Secure access to external data](search-security-best-practices.md#secure-access-to-external-data).
 
 ## Check results
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "外部データへの安全なアクセスに関するリンク更新"
}
```

### Explanation
この変更は、`articles/search/search-how-to-create-indexers.md`というファイルの内容が修正されたことを示しています。修正内容には、1行の追加と1行の削除があり、合計で2つの変更が行われています。

具体的には、インデクサーが他のAzureリソースに対して行うアウトバウンドコールについての説明部分が修正されました。以前は「[Security in Azure AI Search](search-security-overview.md)」というリンクが記載されていましたが、現在では「[Secure access to external data](search-security-best-practices.md#secure-access-to-external-data)」に更新されています。この変更により、ユーザーが外部データへの安全な接続方法についてのより具体的で適切な情報を得られるようになっています。

この更新は、ドキュメントの正確性と関連性を高めることを目的としており、ユーザーが必要な情報を迅速に見つけられるようにすることに貢献しています。全体として、情報の精度とアクセスの向上を図った改良が行われています。

## articles/search/search-how-to-managed-identities.md{#item-3536f2}

<details>
<summary>Diff</summary>
````diff
@@ -417,7 +417,7 @@ If your Azure resource is behind a firewall, make sure there's an inbound rule t
 
 ## See also
 
-+ [Security overview](search-security-overview.md)
++ [Data, privacy, and built-in protections](search-security-built-in.md)
 + [AI enrichment overview](cognitive-search-concept-intro.md)
 + [Indexers overview](search-indexer-overview.md)
 + [Authenticate with Microsoft Entra ID](/azure/architecture/framework/security/design-identity-authentication)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "関連リンクの名称変更"
}
```

### Explanation
この変更は、`articles/search/search-how-to-managed-identities.md`というファイルの内容が修正されたことを示しています。変更内容は、1行の追加と1行の削除を伴い、合計で2つの変更が行われています。

具体的には、「See also」セクションのリンクが更新されました。以前は「[Security overview](search-security-overview.md)」というリンクが含まれていましたが、これが「[Data, privacy, and built-in protections](search-security-built-in.md)」に変更されました。この改訂により、ユーザーにはデータのプライバシーと組み込みの保護に関するより関連性のある情報を提供することができます。

このようなリンケージの更新は、文書の関連性を高め、ユーザーが必要とする情報にアクセスしやすくすることを目的としています。全体として、情報の精確さとナビゲーションの向上を図った改善が反映されています。

## articles/search/search-howto-reindex.md{#item-46738a}

<details>
<summary>Diff</summary>
````diff
@@ -429,4 +429,4 @@ The following table lists common issues when updating or rebuilding indexes and
 + [Azure Cosmos DB for NoSQL indexer](search-how-to-index-cosmosdb-sql.md)
 + [Azure blob indexer](search-how-to-index-azure-blob-storage.md)
 + [Azure tables indexer](search-how-to-index-azure-tables.md)
-+ [Security in Azure AI Search](search-security-overview.md)
++ [Data, privacy, and built-in protections](search-security-built-in.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンク先の名称変更と更新"
}
```

### Explanation
この変更は、`articles/search/search-howto-reindex.md`というファイルの内容が修正されたことを示しています。変更には、1行の追加と1行の削除が含まれ、合計で2つの変更が行われています。

具体的には、インデックスの更新または再構築に関する一般的な問題をリストするテーブルの「See also」セクションが更新されました。以前は「[Security in Azure AI Search](search-security-overview.md)」というリンクがありましたが、これが「[Data, privacy, and built-in protections](search-security-built-in.md)」に変更されました。この更新により、ユーザーはデータプライバシーと組み込みの保護についてのより関連性のある情報を得られるようになります。

この修正は、ドキュメントの最新性を維持し、ユーザーにとっての有用性を高めるために行われたものです。全体として、関連情報の円滑な流れを促進するための改善が施されています。

## articles/search/search-indexer-sensitivity-labels.md{#item-2a7bfc}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure AI Search
 description: Learn how to configure Azure AI Search indexers to ingest Microsoft Purview sensitivity labels from supported data sources for document-level security enforcement.  
 ms.service: azure-ai-search  
 ms.topic: how-to  
-ms.date: 01/28/2026  
+ms.date: 02/26/2026  
 author: gmndrg  
 ms.author: gimondra  
 ---
@@ -53,11 +53,9 @@ These updates are detected if they occurred since the last indexer run.
 
 ## Limitations
 
-+ There's a known issue with document deletion and sensitivity labels. When sensitivity labels are enabled for an index, the indexer fails to enumerate the index’s documents. As a result, soft delete operations don't run because the indexer can't list the documents that need to be removed. This applies to indexers that support soft delete, including Azure Blob, ADLS Gen2, OneLake, SharePoint.
 + Initial release supports REST API version 2025-11-01-preview and associated beta SDK only. There's no portal experience for configuration or management.  
 + [Autocomplete](/rest/api/searchservice/documents/autocomplete-post) and [Suggest](/rest/api/searchservice/documents/suggest-post) APIs are disabled for Purview-enabled indexes, as they can't yet enforce label-based access control.  
 + Guest accounts and cross-tenant queries aren't supported.
-+ In the initial release, sensitivity label-enabled indexes don't support unlabeled documents and don't return them in query results. This capability will be documented when available.
 + The following indexer features don't support documents with sensitivity labels. If you use any of these features in a skillset or indexer, they don't process those documents.
 
     - Custom Web API skill
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新と制限事項の変更"
}
```

### Explanation
この変更は、`articles/search/search-indexer-sensitivity-labels.md`というファイルの内容が修正されたことを示しており、4つの変更が行われています。具体的には、1行の追加と3行の削除が含まれています。

主な変更点は以下の通りです：
1. ドキュメントの最終更新日が「01/28/2026」から「02/26/2026」に更新されました。これは、内容が最新であることを保証するための重要な変更です。
2. 制限事項に関する説明が一部変更され、文書の削除に関する既知の問題が削除され、代わりに初期リリースにおける機能制約が具体的に記載されています。これにより、ユーザーは現在の制限をより明確に理解できるようになります。
3. さらに、Purviewを利用するインデックスに関しては、オートコンプリートやサジェストAPIが無効であることや、ゲストアカウントおよびクロステナントクエリがサポートされていないことも明記されています。

このような変更は、ユーザーがシステムの機能や制限を理解し、期待通りにサービスを利用できるようにするために重要です。また、情報の正確性を向上させるべく、日付が更新されたことも重要なポイントです。

## articles/search/search-manage-azure-cli.md{#item-7fdd08}

<details>
<summary>Diff</summary>
````diff
@@ -309,7 +309,7 @@ az search private-endpoint-connection delete \
 
 ## Create a service with confidential computing
 
-[Confidential computing](search-security-overview.md#data-in-use) is an optional compute type for data-in-use protection. When configured, your search service is deployed on confidential VMs (DCasv5 or DCesv5) instead of standard VMs. This compute type also incurs a 10% surcharge for billable tiers. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/search/).
+[Confidential computing](search-security-best-practices.md#optional-enable-confidential-computing) is an optional compute type for data-in-use protection. When configured, your search service is deployed on confidential VMs (DCasv5 or DCesv5) instead of standard VMs. This compute type also incurs a 10% surcharge for billable tiers. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/search/).
 
 For daily usage, confidential computing isn't necessary. We only recommend this compute type for stringent regulatory, compliance, or security requirements. For more information, see [Confidential computing use cases](/azure/confidential-computing/use-cases-scenarios).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンク先の変更"
}
```

### Explanation
この変更は、`articles/search/search-manage-azure-cli.md`というファイルに対する修正を示しており、合計で2つの変更が行われています。具体的には、1行の追加と1行の削除が含まれています。

主なポイントは、「Confidential computing」に関する説明文中のリンク先が変更されたことです。以前は「[Confidential computing](search-security-overview.md#data-in-use)」というリンクが含まれていましたが、これが「[Confidential computing](search-security-best-practices.md#optional-enable-confidential-computing)」に更新されました。この変更により、ユーザーはデータ使用時の保護のための機能に関して、より適切なリソースにアクセスできるようになります。

この修正は、関連情報を正確かつ効率的に提供するために行われており、ユーザーの理解を助けることを目的としています。また、機密コンピューティングの使用が推奨される状況についても明確に触れられています。全体的に、ユーザーにとってより使いやすい情報提供が実現されています。

## articles/search/search-manage-rest.md{#item-405ec7}

<details>
<summary>Diff</summary>
````diff
@@ -246,7 +246,7 @@ PATCH https://management.azure.com/subscriptions/{{subscription-id}}/resourcegro
 
 ## Configure confidential computing
 
-[Confidential computing](search-security-overview.md#data-in-use) is an optional compute type for data-in-use protection. When configured, your search service is deployed on confidential VMs (DCasv5 or DCesv5) instead of standard VMs. This compute type also incurs a 10% surcharge for billable tiers. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/search/).
+[Confidential computing](search-security-best-practices.md#optional-enable-confidential-computing) is an optional compute type for data-in-use protection. When configured, your search service is deployed on confidential VMs (DCasv5 or DCesv5) instead of standard VMs. This compute type also incurs a 10% surcharge for billable tiers. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/search/).
 
 For daily usage, confidential computing isn't necessary. We only recommend this compute type for stringent regulatory, compliance, or security requirements. For more information, see [Confidential computing use cases](/azure/confidential-computing/use-cases-scenarios).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "機密コンピューティングに関するリンクの更新"
}
```

### Explanation
この変更は、`articles/search/search-manage-rest.md`ファイルに対するもので、合計2つの変更が施されています。具体的には、1行の追加と1行の削除が行われています。

主な変更点は、機密コンピューティングに関する記述のリンク先が変更されたことです。以前は「[Confidential computing](search-security-overview.md#data-in-use)」というリンクが使用されていましたが、これが「[Confidential computing](search-security-best-practices.md#optional-enable-confidential-computing)」に更新されました。この変更により、ユーザーは機密コンピューティングの設定とベストプラクティスに関する最新の情報にアクセスできるようになります。

また、機密コンピューティングの使用が日常的には必要ないことや、厳格な規制やセキュリティ要件を満たすためにのみ推奨されるとの説明も含まれており、ユーザーが適切な判断を下すための情報を提供しています。このように、変更は情報の正確性を高めることを目的としており、ユーザーにとって有益なアップデートといえます。

## articles/search/search-manage.md{#item-4043d7}

<details>
<summary>Diff</summary>
````diff
@@ -70,7 +70,7 @@ By default, a search service accepts authenticated and authorized requests over
 + [Configure firewall rules](service-configure-firewall.md) to restrict network access by IP address.
 + [Configure a private endpoint](service-create-private-endpoint.md) to only allow traffic from Azure virtual networks. Note that when you turn off the public endpoint, the import wizards won't run.
 
-To learn about inbound and outbound calls in Azure AI Search, see [Security in Azure AI Search](search-security-overview.md).
+To learn about inbound and outbound calls in Azure AI Search, see [Understand network traffic patterns](search-security-best-practices.md#understand-network-traffic-patterns).
 
 ## Check capacity and understand billing
 
@@ -86,7 +86,7 @@ To learn about other features that affect billing, see [How you're charged for A
 
 Internally, Microsoft collects telemetry data about your service and the platform. To learn more about data retention, see [Retention of metrics](/azure/azure-monitor/essentials/data-platform-metrics#retention-of-metrics).
 
-To learn more about data location and privacy, see [Data residency](search-security-overview.md#data-residency).
+To learn more about data location and privacy, see [Data residency](search-security-built-in.md#data-residency).
 
 ## Enable semantic ranker
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンクの変更と追加"
}
```

### Explanation
この変更は、`articles/search/search-manage.md`ファイルに対するもので、合計4つの変更が行われました。具体的には、2行の追加と2行の削除が含まれています。

主な変更点は、文中のリンク先が更新されていることです。最初のリンクは「[Security in Azure AI Search](search-security-overview.md)」から「[Understand network traffic patterns](search-security-best-practices.md#understand-network-traffic-patterns)」に置き換えられ、この変更により、ユーザーはネットワークトラフィックのパターンをより深く理解するための情報にアクセスできるようになります。

また、次のリンクは「[Data residency](search-security-overview.md#data-residency)」から「[Data residency](search-security-built-in.md#data-residency)」に変更され、データの所在地とプライバシーについての情報を、新しいリソースにリンクさせています。

このように、変更は情報の最新性を確保し、ユーザーが必要とする情報を迅速に入手できるようにすることを目的としています。全体として、文書はより使いやすく、関連性の高い内容に更新されています。

## articles/search/search-monitor-logs-powerbi.md{#item-5b3491}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.date: 05/29/2025
 ms.update-cycle: 365-days
 ---
 
-# Visualize Azure AI Search Logs and Metrics with Power BI
+# Visualize Azure AI Search logs and metrics with Power BI
 
 Azure AI Search can send operation logs and service metrics to an Azure Storage account, which can then be visualized in Power BI. This article explains the steps and how to use a Power BI template app to visualize the data. The template covers information about queries, indexing, operations, and service metrics.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "タイトルのフォーマットの修正"
}
```

### Explanation
この変更は、`articles/search/search-monitor-logs-powerbi.md`ファイルに対するもので、合計2つの変更が施されています。具体的には、1行の追加と1行の削除が行われています。

主な変更点は、文書のタイトルの表記が修正されたことです。元のタイトル「Visualize Azure AI Search Logs and Metrics with Power BI」は、「Visualize Azure AI Search logs and metrics with Power BI」に変更されました。この修正により、「Logs」の大文字が小文字に変更され、タイトルの一貫性が向上しています。

このような変更は、ドキュメントの整合性を高め、読者にとってより理解しやすい内容を提供することを目的としています。全体として、文書は軽微な修正ですが、視覚的な整合性が向上しています。

## articles/search/search-region-support.md{#item-25b0f1}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ When you create an Azure AI Search service, your region selection might depend o
 | [AI enrichment](cognitive-search-concept-intro.md) | Refers to [built-in skills](cognitive-search-predefined-skills.md) that make internal calls to Foundry Tools for enrichment and transformation during indexing. Integration requires that Azure AI Search coexists with a [Microsoft Foundry resource](/azure/ai-services/multi-service-resource) in the same physical region. You can bypass region requirements by using [identity-based connections](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection), currently in public preview. | Regional support is noted in this article. |
 | [Availability zones](/azure/reliability/reliability-ai-search#availability-zone-support) | Divides a region's data centers into distinct physical location groups, providing high availability within the same geo. | Regional support is noted in this article. |
 | [Agentic retrieval](agentic-retrieval-overview.md) | Uses the agentic retrieval engine designed for conversational search. | Regional support is noted in this article. |
-| [Confidential computing](search-security-overview.md#data-in-use) | Deploys your search service on confidential VMs to process data in a hardware-based trusted execution environment.<p>Confidential computing disables or restricts certain features, including agentic retrieval, semantic ranker, query rewrite, and skillset execution. | Regional support is noted in this article. |
+| [Confidential computing](search-security-best-practices.md#optional-enable-confidential-computing) | Deploys your search service on confidential VMs to process data in a hardware-based trusted execution environment.<p>Confidential computing disables or restricts certain features, including agentic retrieval, semantic ranker, query rewrite, and skillset execution. | Regional support is noted in this article. |
 | [Semantic ranker](semantic-search-overview.md) | Takes a dependency on Microsoft-hosted models in specific regions. | Regional support is noted in this article. |
 | [Query rewrite](semantic-how-to-query-rewrite.md) | Takes a dependency on Microsoft-hosted models in specific regions. | Regional support is noted in this article. |
 | [Extra capacity](search-limits-quotas-capacity.md#service-limits) | Higher-capacity partitions became available in select regions starting in April 2024, with a second wave following in May 2024. Currently, there are just a few regions that *don't* offer higher-capacity partitions.<p>If you have an older search service in a supported region, check if you can [upgrade your service](search-how-to-upgrade.md). Otherwise, create a new search service to benefit from more capacity at the same billing rate. | Regional support is noted in the footnotes of this article. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンク先の修正"
}
```

### Explanation
この変更は、`articles/search/search-region-support.md`ファイルに対するもので、合計2つの変更が行われました。具体的には、1行の追加と1行の削除が含まれています。

主な変更点は、文中の「[Confidential computing](search-security-overview.md#data-in-use)」のリンクが、「[Confidential computing](search-security-best-practices.md#optional-enable-confidential-computing)」に置き換えられたことです。この修正により、機密コンピューティングに関する情報が、より関連性の高いリソースに誘導されるようになっています。

このような変更は、ユーザーが最新の情報とベストプラクティスにアクセスできるようにすることを目的としており、文書の整合性と信頼性を高めています。全体として、文書の内容はより適切な情報資源にリンクされることで、読み手にとって有益な更新となっています。

## articles/search/search-security-api-keys.md{#item-d8c908}

<details>
<summary>Diff</summary>
````diff
@@ -358,6 +358,6 @@ It's not possible to use [customer-managed key encryption](search-security-manag
 
 ## Related content
 
-+ [Security in Azure AI Search](search-security-overview.md)
++ [Data, privacy, and built-in protections in Azure AI Search](search-security-built-in.md)
 + [Azure role-based access control in Azure AI Search](search-security-rbac.md)
 + [Manage using PowerShell](search-manage-powershell.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リンク先の変更"
}
```

### Explanation
この変更は、`articles/search/search-security-api-keys.md`ファイルに行われ、合計2つの変更（1行の追加と1行の削除）が含まれています。

具体的には、「Related content」セクション内のリンクが変更されました。以前は「[Security in Azure AI Search](search-security-overview.md)」というリンクが掲載されていましたが、これが「[Data, privacy, and built-in protections in Azure AI Search](search-security-built-in.md)」に変更されました。この修正により、ユーザーはAzure AI Searchにおけるデータ保護とプライバシーに関する情報に直接アクセスできるようになります。

この更新は、ドキュメントの情報の関連性を高め、読者にとって必要な情報に導くことを目的としています。全体として、リンクの修正は文書の有用性を向上させ、ユーザーがより具体的で関連性の高いトピックにアクセスできるようにしています。

## articles/search/search-security-best-practices.md{#item-9dd4cd}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,296 @@
+---
+title: Best Practices for Security
+titleSuffix: Azure AI Search
+description: Learn how to configure security features in Azure AI Search to protect endpoints, content, and operations. This article provides best practices for network security, authentication, and data protection.
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.update-cycle: 180-days
+ms.topic: how-to
+ms.date: 02/24/2026
+ai-usage: ai-assisted
+---
+
+# Secure an Azure AI Search service
+
+This article provides security best practices to help protect your Azure AI Search service. You're responsible for implementing these customer-configurable security controls. For information about Microsoft's built-in protections, such as network architecture, encryption, and compliance certifications, see [Data, privacy, and built-in protections in Azure AI Search](search-security-built-in.md).
+
+As a solutions architect, you should configure security controls across three domains:
+
+- **Network security**: Control inbound and outbound traffic to your search service.
+- **Authentication and authorization**: Define how, who, and what can access your search service and data.
+- **Data protection**: Implement encryption, access controls, and monitoring.
+
+## Understand network traffic patterns
+
+Before you configure network security, understand the three network traffic patterns in Azure AI Search:
+
++ **Inbound traffic**: Requests from clients to your search service, such as queries, indexing, and management operations. This traffic is configurable by customers.
+
++ **Outbound traffic**: Requests from your search service to external resources, such as indexers that connect to data sources, vectorizers, and custom skills. This traffic is configurable by customers.
+
++ **Internal traffic**: Service-to-service calls over the Microsoft backbone network. This traffic is managed by Microsoft and isn't configurable by customers. For more information, see [Internal traffic protection](search-security-built-in.md#internal-traffic-protection).
+
+## Configure network security
+
+Use one of the following approaches to restrict inbound access to your search service. These approaches are listed from least secure to most secure:
+
++ [Create IP firewall rules](#create-ip-firewall-rules)
++ [Create a private endpoint](#create-a-private-endpoint)
++ [Join a network security perimeter](#join-a-network-security-perimeter)
+
+### Create IP firewall rules
+
+Create inbound firewall rules to admit requests only from specific IP addresses or address ranges. All client connections must be made through an allowed IP address. Otherwise, the connection is denied.
+
+:::image type="content" source="media/search-security-overview/inbound-firewall-ip-restrictions.png" alt-text="Sample architecture diagram for IP restricted access.":::
+
+**When to use**: Basic protection scenarios where you need to restrict access to known IP addresses.
+
+**How to get started**: See [Configure network access and firewall rules for Azure AI Search](service-configure-firewall.md).
+
+### Create a private endpoint
+
+Create a private endpoint for Azure AI Search to allow clients on a virtual network to securely access data in a search index over a Private Link. The private endpoint uses an IP address from your virtual network address space.
+
+Network traffic between the client and the search service traverses over the virtual network and a private link on the Microsoft backbone network, eliminating exposure from the public internet.
+
+:::image type="content" source="media/search-security-overview/inbound-private-link-azure-cog-search.png" alt-text="Sample architecture diagram for private endpoint access.":::
+
+**When to use**: High-security scenarios requiring complete network isolation from the public internet.
+
+**How to get started**: See [Create a private endpoint for Azure AI Search](service-create-private-endpoint.md).
+
+### Join a network security perimeter
+
+Create a network security perimeter around your platform-as-a-service (PaaS) resources deployed outside of a virtual network to establish a logical network boundary. This establishes a perimeter that controls public network access through explicit access rules.
+
+Inbound client connections and service-to-service connections occur within the boundary, simplifying defenses against unauthorized access. In Azure AI Search, it's common for solutions to use multiple Azure resources.
+
+**When to use**: Solutions using multiple Azure PaaS resources that need coordinated network boundary protection.
+
+**How to get started**:
+
++ Start by joining Azure AI Search to a network security perimeter. See [Add a search service to a network security perimeter](search-security-network-security-perimeter.md).
+
++ Add related services, such as [Azure OpenAI](/azure/ai-foundry/openai/how-to/network-security-perimeter), [Azure Storage](/azure/storage/common/storage-network-security-perimeter), and [Azure Monitor](/azure/azure-monitor/fundamentals/network-security-perimeter), to the same perimeter.
+
+## Configure authentication and authorization
+
+Azure AI Search supports two authentication approaches. You can use one approach and disable the other, or you can use both with appropriate controls.
+
+### (Recommended) Enable role-based access control
+
+Use Microsoft Entra authentication to establish the *caller*, rather than the *request*, as the authenticated identity. Azure role assignments determine authorization, providing centralized identity management, conditional access policies, and comprehensive audit trails.
+
+The workflow for role-based access control is:
+
+1. **Enable role-based access control**: Configure your search service to accept Microsoft Entra ID authentication instead of (or in addition to) API keys. See [Enable or disable role-based access control in Azure AI Search](search-security-enable-roles.md).
+
+1. **Assign roles to users and groups**: Grant least-privilege access using built-in roles (Search Service Contributor, Search Index Data Contributor, and Search Index Data Reader) to control who can manage and query indexes. See [Connect to Azure AI Search using roles](search-security-rbac.md).
+
+1. **Connect your application using identities**: Authenticate without API keys by using `DefaultAzureCredential`, which supports managed identities, developer credentials, and other token-based flows. See [Connect your app to Azure AI Search using identities](search-security-rbac-client-code.md).
+
+### Configure API key authentication
+
+With key-based authentication, each request must include an admin or query API key to prove it originates from a trusted source. This approach is suitable for development environments, backward compatibility with existing applications, or scenarios where Microsoft Entra ID isn't available.
+
+The workflow for key-based authentication is:
+
+1. **Provide an API key in each request**: Admin keys grant full access to all operations. Query keys grant read-only access to the documents collection of an index. See [Connect to Azure AI Search using keys](search-security-api-keys.md).
+
+1. **Rotate admin keys on a schedule**: Reduce the risk of key compromise by regularly regenerating admin keys. Search services support two admin keys for zero-downtime rotation. See [Regenerate admin keys](search-security-api-keys.md#regenerate-admin-keys).
+
+### Authorize control plane operations
+
+Control plane operations (service creation, configuration, and deletion) are authorized through Azure Resource Manager role-based access control, the same model used across all Azure services. API keys don't apply to control plane operations. Three built-in Azure roles govern access:
+
+| Role | Permissions |
+| ---- | ----------- |
+| Owner | Full control, including access management. |
+| Contributor | Full control except for access management. |
+| Reader | View-only access. |
+
+The workflow for authorizing control plane operations is:
+
+1. **Assign administrative roles**: Use built-in Azure roles (Owner, Contributor, and Reader) to grant least-privilege access and control who can create, configure, or delete search services. See [Assign roles for service administration](search-security-rbac.md#assign-roles-for-service-administration).
+
+1. **Apply resource locks**: Prevent accidental deletion of production search services by applying `CanNotDelete` or `ReadOnly` locks. See [Lock your Azure resources to protect your infrastructure](/azure/azure-resource-manager/management/lock-resources).
+
+### Authorize data plane operations
+
+Data plane operations target content hosted on a search service, such as index creation, document loading, and queries. Authorization is available through role-based access control, API keys, or both. For configuration steps, see the previous sections on [role-based access control](#recommended-enable-role-based-access-control) and [API key authentication](#configure-api-key-authentication).
+
+### Grant access to individual indexes
+
+Restrict user access to individual indexes by creating custom role definitions. This approach is essential for multi-tenant scenarios where each tenant's data must be isolated at the index level. See [Grant access to a single index](search-security-rbac.md#grant-access-to-a-single-index).
+
+For solutions requiring security boundaries at the index level, see [Design patterns for multitenant SaaS applications and Azure AI Search](search-modeling-multitenant-saas-applications.md).
+
+> [!NOTE]
+> API keys provide service-level access only. Anyone with an [admin key](search-security-api-keys.md) can read, modify, or delete any index in the search service. For index-level isolation, use role-based access control or implement isolation in your application's middle tier.
+
+## Configure outbound connections
+
+Outbound requests originate from a search service to other applications, typically made by indexers, custom skills, and vectorizers. Configure these connections to use secure authentication and network access.
+
+### (Recommended) Use a managed identity
+
+Create a managed identity for your search service to authenticate to other Azure resources without storing credentials in your code. A managed identity eliminates the need to store and rotate connection strings with credentials.
+
+The workflow for using a managed identity is:
+
+1. **Configure a managed identity for the search service**: Choose between a system-assigned or user-assigned managed identity. See [Configure a search service to connect using a managed identity](search-how-to-managed-identities.md).
+
+1. **Connect to external resources using the managed identity**: Supported connections include [Azure Storage](search-howto-managed-identities-storage.md), [Azure Cosmos DB](search-howto-managed-identities-cosmos-db.md), [Azure SQL Database](search-howto-managed-identities-sql.md), [SQL Managed Instance](search-how-to-index-sql-managed-instance-with-managed-identity.md), and [Azure Functions](search-howto-managed-identities-azure-functions.md).
+
+### Secure access to external data
+
+Configure secure connections based on how external resources are protected:
+
++ **Create firewall exceptions for the search service**: Allow indexer traffic through data source firewalls by adding the search service's outbound IP addresses to allowlists. See [Configure IP firewall rules to allow indexer connections from Azure AI Search](search-indexer-howto-access-ip-restricted.md).
+
++ **Create shared private links**: Connect indexers to data sources protected by Azure Private Link without exposing traffic to the public internet. See [Make outbound connections through a shared private link](search-indexer-howto-access-private.md).
+
++ **Use trusted service exception for same-region storage**: Enable indexer access to secured Azure Storage accounts in the same region without firewall configuration. See [Make indexer connections to Azure Storage as a trusted service](search-indexer-howto-access-trusted-service-exception.md).
+
++ **Configure resource instance rules**: Grant specific search services access to Azure Storage accounts protected by network rules. See [Grant access from Azure resource instances](/azure/storage/common/storage-network-security?tabs=azure-portal#grant-access-from-azure-resource-instances).
+
++ **Connect to SQL Managed Instance private endpoints**: Access SQL Managed Instance databases through private endpoints while maintaining network isolation. See [Create a shared private link for a SQL managed instance from Azure AI Search](search-indexer-how-to-access-private-sql.md).
+
+> [!TIP]
+> If Azure Storage and Azure AI Search are in the same region, network traffic is automatically routed through a private IP address over the Microsoft backbone network, eliminating the need for firewall configuration. For more information, see [Same-region Azure Storage and Azure AI Search](search-security-built-in.md#same-region-azure-storage-and-azure-ai-search).
+
+### Secure connections for external AI processing
+
+Outbound requests for AI enrichment and vectorization require special consideration:
+
+| Operation | Configuration |
+| --------- | ------------- |
+| Indexers connecting to data sources | [Secure access to external data](search-indexer-securing-resources.md). |
+| Custom skills calling external code | Secure connections to [Azure Functions, web apps, or other hosts](cognitive-search-custom-skill-interface.md#set-the-endpoint-and-time-out-interval). |
+| Vectorization during indexing | Connect to [Azure OpenAI](vector-search-integrated-vectorization.md#secure-connections-to-vectorizers-and-models) or custom embedding models. |
+| Azure Key Vault | Connect to Azure Key Vault for [customer-managed encryption keys](search-security-manage-encryption-keys.md). |
+
+For basic retrieval-augmented generation (RAG) patterns where your client application calls a chat completion model, the connection uses the client or user identity, not the search service identity. For agentic retrieval using knowledge bases, the outbound request is made by the search service managed identity.
+
+## Implement document-level access control
+
+User permissions at the document level, also known as *row-level security*, control which documents users can access through query execution.
+
+### Configure document-level security
+
+Configure fine-grained permissions at the document level, from data ingestion through query execution. This capability is essential for building secure AI agentic systems grounding data, RAG applications, and enterprise search solutions that require authorization checks at the document level. For more information, see [Document-level access control](search-document-level-access-overview.md).
+
+### Use sensitivity labels (preview)
+
+Configure an indexer to automatically detect Microsoft Purview sensitivity labels during indexing and apply label-based access controls when queries are executed. For more information, see [Sensitivity labels](search-indexer-sensitivity-labels.md).
+
+## Configure data encryption
+
+Azure AI Search encrypts all data automatically using Microsoft-managed keys. For information about built-in encryption, see [Data encryption](search-security-built-in.md#data-encryption).
+
+For enhanced data protection, you can implement the following encryption controls.
+
+### (Optional) Add customer-managed key encryption
+
+Add an extra encryption layer for indexes and synonym maps by managing your own encryption keys
+in Azure Key Vault. Customer-managed keys (CMK) are for organizations with compliance requirements mandating
+customer control over encryption keys or key revocation capabilities. See [Configure customer-managed keys for data encryption in Azure AI Search](search-security-manage-encryption-keys.md).
+
+You can also configure the following options:
+
++ **Configure cross-tenant CMK**: Support multi-tenant scenarios where keys are stored in a different Microsoft Entra tenant than the search service. See [Configure customer-managed keys across different tenants](search-security-managed-encryption-cross-tenant.md).
+
++ **Find encrypted objects**: Identify which indexes and synonym maps use CMK encryption. See [Find encrypted objects and information](search-security-get-encryption-keys.md).
+
+> [!IMPORTANT]
+> + CMK encryption increases index size and can degrade query performance by 30-60%. Only enable for indexes that require it.
+> + CMK on temporary disks requires services created after May 13, 2021. Earlier services support CMK on data disks only.
+
+### Index encrypted blob content
+
+Configure an indexer to process content from Azure Blob Storage that's encrypted at rest, which is separate
+from CMK encryption of the search index. See [Tutorial: Index and enrich encrypted blobs](search-how-to-index-azure-blob-encrypted.md).
+
+### (Optional) Enable confidential computing
+
+[Confidential computing](/azure/confidential-computing/overview) protects data in use from unauthorized access, including from Microsoft, through hardware attestation and encryption. This compute type is only configurable during service creation. See [Choose a compute type](search-create-service-portal.md#choose-a-compute-type).
+
+We only recommend confidential computing for organizations whose compliance or regulatory requirements necessitate data-in-use protection. For daily usage, the default compute type suffices.
+
+| Compute type | Description | Limitations | Cost | Availability |
+| ------------ | ----------- | ----------- | ---- | ------------ |
+| Default | Standard VMs with built-in encryption for data at rest and in transit. No hardware-based isolation for data in use. | No limitations. | No change to the base cost of free or billable tiers. | Available in all regions. |
+| Confidential | Confidential VMs (DCasv5 or DCesv5) in hardware-based trusted execution environment. Isolates computations and memory from the host operating system and other VMs. | Disables or restricts [agentic retrieval](agentic-retrieval-overview.md), [semantic ranker](semantic-search-overview.md), [query rewrite](semantic-how-to-query-rewrite.md), [skillset execution](cognitive-search-concept-intro.md), and indexers that run in the [multitenant environment](search-howto-run-reset-indexers.md#indexer-execution-environment) <sup>1</sup>. | Adds 10% surcharge to the base cost of billable tiers. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/search/). | Available in some regions. For more information, see the [list of supported regions](search-region-support.md). |
+
+<sup>1</sup> When you enable this compute type, indexers can only run in the private execution environment, meaning they run from the search clusters hosted on confidential computing.
+
+## Enable monitoring and logging
+
+Track operations, detect anomalies, and support security audits by enabling logging and monitoring for your search service. For information about what Azure AI Search logs by default, see [Data logging](search-security-built-in.md#data-logging).
+
++ **Enable diagnostic logging**: Capture operations for security audits and anomaly detection by sending logs to Azure Monitor, Event Hubs, or Azure Storage. See [Configure diagnostic logging for Azure AI Search](search-monitor-enable-logging.md).
+
++ **Monitor queries**: Track search query activity, latency, and throttling to detect unusual patterns. See [Monitor query requests in Azure AI Search](search-monitor-queries.md).
+
++ **Monitor indexer operations**: Track indexing activity, errors, and data refresh operations. See [Monitor indexer status and results in Azure AI Search](search-monitor-indexers.md).
+
++ **Configure alerts for anomalous activity**: Create alert rules for query volume spikes, failed authentication attempts, and unusual access patterns. See [Create or edit a metric alert rule](/azure/azure-monitor/alerts/alerts-create-new-alert-rule).
+
++ **Visualize logs using Power BI**: Build dashboards to analyze search service activity and identify security trends. See [Visualize Azure AI Search logs and metrics with Power BI](search-monitor-logs-powerbi.md).
+
+## Maintain compliance
+
+For information about Azure AI Search compliance certifications and the shared responsibility model, see [Compliance and certifications](search-security-built-in.md#compliance-and-certifications).
+
+### Use Azure Policy
+
++ **Review built-in policy definitions**: Use Azure Policy to audit and enforce security configurations such as diagnostic logging and private endpoint usage. See [Azure Policy Regulatory Compliance controls for Azure AI Search](security-controls-policy.md).
+
++ **Assign the resource logging policy**: Automatically identify search services missing diagnostic logging and remediate the configuration. See [Azure Policy overview](/azure/governance/policy/overview).
+
++ **Create custom policies**: Define organization-specific security requirements and enforce them across all search services. See [Tutorial: Create a custom policy definition](/azure/governance/policy/tutorials/create-custom-policy-definition).
+
+### Apply resource tags
+
+Apply resource tags to categorize search services by environment, data sensitivity, cost center, or compliance requirements for improved governance. See [Use tags to organize your Azure resources and management hierarchy](/azure/azure-resource-manager/management/tag-resources).
+
+## Security checklist
+
+Use this checklist to ensure you've configured appropriate security controls:
+
+**Network security**:
+
+- [ ] Configured IP firewall rules, private endpoint, or network security perimeter
+- [ ] Restricted inbound access to known clients or networks
+- [ ] Configured secure outbound connections using managed identities
+
+**Authentication and authorization**:
+
+- [ ] Enabled role-based access control
+- [ ] Assigned appropriate roles to users and applications
+- [ ] Implemented admin key rotation schedule (if using keys)
+- [ ] Configured index-level permissions (if required)
+
+**Data protection**:
+
+- [ ] Configured document-level access control (if required)
+- [ ] Configured sensitivity labels (if applicable)
+- [ ] Implemented CMK encryption (if required)
+- [ ] Evaluated confidential computing requirements (if applicable)
+
+**Monitoring and compliance**:
+
+- [ ] Enabled diagnostic logging
+- [ ] Set up monitoring and alerts to identify anomalous activity
+- [ ] Applied resource tags for governance
+- [ ] Assigned Azure Policy for resource logging
+- [ ] Reviewed compliance certifications against requirements
+
+## Related content
+
++ [Data, privacy, and built-in protections in Azure AI Search](search-security-built-in.md)
++ [Azure security fundamentals](/azure/security/fundamentals/)
++ [Shared responsibility in the cloud](/azure/security/fundamentals/shared-responsibility)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Searchのセキュリティベストプラクティスに関する新しい記事の追加"
}
```

### Explanation
この変更は、`articles/search/search-security-best-practices.md`というファイルが新たに追加されたもので、296行が書き加えられています。この新しい文書は、Azure AI Searchサービスのセキュリティ機能を構成し、エンドポイント、コンテンツ、操作を保護するためのベストプラクティスを学ぶことを目的としています。

新しい記事では、セキュリティ管理のための3つの主要な領域（ネットワークセキュリティ、認証と認可、データ保護）に加えて、ネットワークトラフィックパターンの理解、セキュリティの構成方法、ドキュメントレベルのアクセス制御の実装など、具体的なガイドラインが示されています。特に、役割ベースのアクセス制御や、顧客管理の暗号鍵を使ったデータの暗号化、監視とロギングの実施、コンプライアンスの維持について詳述しています。

これにより、ユーザーはAzure AI Searchのセキュリティ対策を強化し、データ漏洩や不正アクセスのリスクを低減するための包括的なリソースを利用できるようになります。この新しい文書は、利用者がより安全にAzure AI Searchを運用するための有用な情報源となります。

## articles/search/search-security-built-in.md{#item-a42668}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,160 @@
+---
+title: Data, Privacy, and Built-in Protections
+titleSuffix: Azure AI Search
+description: Learn about Microsoft-managed security, data residency, encryption, and compliance features built into Azure AI Search.
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.update-cycle: 180-days
+ms.topic: conceptual
+ms.date: 02/24/2026
+ai-usage: ai-assisted
+---
+
+# Data, privacy, and built-in protections in Azure AI Search
+
+Azure AI Search includes security protections that Microsoft manages automatically, requiring no action from customers. Understanding what Microsoft handles helps you focus your security efforts on the controls and configurations for which you're responsible. 
+
+This article covers Microsoft's built-in protections, including network architecture, encryption (in transit, in use, and at rest), data residency, privacy guarantees, and compliance certifications. For security best practices that you should configure, see [Secure an Azure AI Search service](search-security-best-practices.md).
+
+## What Microsoft manages automatically
+
+Azure AI Search provides comprehensive built-in security protections across network, data, and service operations. These features are active by default and don't require configuration:
+
++ **Transport Layer Security (TLS)**: All connections use TLS 1.2 or 1.3 for encryption in transit.
+
++ **Service-managed encryption**: Data is encrypted at rest using 256-bit Advanced Encryption Standard (AES) encryption.
+
++ **Internal network security**: Service-to-service calls occur over the secure Microsoft backbone network.
+
++ **Compliance certifications**: Azure AI Search maintains certifications for global, regional, and industry-specific standards.
+
++ **Operational security**: Microsoft manages infrastructure security, patching, and service updates.
+
+## Network security architecture
+
+Azure AI Search uses Microsoft's secure network infrastructure to protect traffic to, from, and within your search servic
+
+### Internal traffic protection
+
+Microsoft secures and manages internal requests. You can't configure or control these connections. Internal traffic is isolated from public networks and protected by Microsoft's security infrastructure.
+
+Internal traffic includes:
+
++ **Service-to-service authentication and authorization**: Calls through Microsoft Entra ID, resource logging sent to Azure Monitor, and [private endpoint connections](service-create-private-endpoint.md) that use Azure Private Link.
+
++ **Built-in skills processing**: Same-region requests directed to an internally hosted Microsoft Foundry resource used exclusively for [built-in skills processing](cognitive-search-predefined-skills.md) by Azure AI Search.
+
++ **Semantic ranking**: Requests made to the models that support [semantic ranking](semantic-search-overview.md#availability-and-pricing).
+
+### Transport Layer Security (TLS)
+
+Azure AI Search enforces TLS 1.2 or 1.3 for all connections. TLS 1.3 is the default for newer systems. Earlier TLS versions (1.0 and 1.1) aren't supported.
+
+All endpoints require HTTPS on port 443. Client systems must support TLS 1.2 or later. For implementation guidance, see:
+
++ [Encryption of data in transit](/azure/security/fundamentals/encryption-overview#encryption-of-data-in-transit)
++ [TLS best practices](/dotnet/framework/network-programming/tls)
++ [TLS support in .NET Framework](/dotnet/framework/network-programming/tls#tls-support-in-net-framework)
+
+### Same-region Azure Storage and Azure AI Search
+
+If Azure Storage and Azure AI Search are in the same region, network traffic is routed through a private IP address and occurs over the Microsoft backbone network. Because private IP addresses are used, you can't configure IP firewalls or a private endpoint for network security on the storage account for these connections.
+
+This same-region optimization ensures high performance and low latency while maintaining security through network isolation. The traffic never leaves the Microsoft network infrastructure.
+
+## Data encryption
+
+Azure AI Search automatically encrypts all customer data at multiple layers.
+
+### Data in transit
+
+All data transmitted to and from Azure AI Search is encrypted using TLS 1.2 or later. This data includes:
+
++ Client application requests to the search service endpoint
++ Responses from the search service to client applications
++ API requests for index management, query operations, and indexing
+
+Data in transit is protected end-to-end between your client and the search service. For internal service-to-service communication, encryption occurs over the Microsoft backbone network.
+
+### Data in use
+
+By default, Azure AI Search deploys your search service on standard Azure infrastructure. This infrastructure encrypts data at rest and in transit, but it doesn't protect data while it's being actively processed in memory.
+
+For scenarios requiring hardware-based protection of data in use, Azure AI Search offers confidential computing. This compute type has limited regional availability, disables or restricts certain features, and increases the cost of running your search service. For more information, see [(Optional) Enable confidential computing](search-security-best-practices.md#optional-enable-confidential-computing).
+
+### Data at rest
+
+Azure AI Search automatically encrypts all data at rest using 256-bit [AES encryption](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) with Microsoft-managed keys. This applies to indexes, synonym maps, and object definitions (indexers, data sources, and skillsets) on both data disks and temporary disks. For more information, see [Azure encryption at rest](/azure/security/fundamentals/encryption-atrest).
+
+Service-managed encryption:
+
++ Is built-in and automatic (no configuration required)
++ Is available on all pricing tiers in all regions
++ Uses FIPS 140-2 compliant encryption
+
+You can configure customer-managed keys (CMK) to manage your own encryption keys. CMK adds a second encryption layer on top of service-managed encryption. For more information, see [(Optional) Add customer-managed key encryption](search-security-best-practices.md#optional-add-customer-managed-key-encryption).
+
+## Data residency
+
+When you create a search service, you select a region within an [Azure geography](https://azure.microsoft.com/explore/global-infrastructure/geographies/). Azure AI Search stores and processes your data within that geography, but Microsoft might replicate data to other regions within the same geography for high availability. The exception is Brazil South, where data stays within the region.
+
+Data stays in your geography unless you configure features that write to Azure Storage (enrichment cache, debug sessions, knowledge stores) in a different region.
+
+Object names (indexes, fields, indexers) might also be processed outside your selected region. These names appear in telemetry logs that Microsoft uses for service support. Avoid placing sensitive data in object names.
+
+For more information, see:
+
++ [Data residency in Azure](https://azure.microsoft.com/explore/global-infrastructure/data-residency/)
++ [Products available by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/)
+
+## Privacy and data handling
+
+Microsoft is committed to protecting your data and respecting your privacy when you use Azure AI Search.
+
+### No customer data used for model training
+
+Microsoft doesn't use customer data from Azure AI Search to train or improve any models, including built-in skills, semantic ranking, or other AI features. Your documents, queries, and other data are used solely to deliver and operate the configured search service.
+
+### Data logging
+
+Azure AI Search doesn't log user identities, so you can't refer to logs for information about a specific user. However, the service does log create, read, update, and delete (CRUD) operations, which you might be able to correlate with other logs to determine who performed specific actions.
+
+Resource logs capture:
+
++ Administrative operations (service creation, configuration changes)
++ Query operations (with query text but no user identity)
++ Indexing operations (document additions, updates, deletions)
+
+Resource logs don't capture:
+
++ Individual user identities
++ Personal information about users
++ Document contents in detail (only metadata about documents being indexed)
+
+For information about setting up logs, see [Monitor Azure AI Search](monitor-azure-cognitive-search.md) and [Monitor query requests](search-monitor-queries.md).
+
+## Compliance and certifications
+
+Azure AI Search undergoes regular third-party audits and maintains certifications against global, regional, government, and industry-specific standards, including [ISO 27001](/azure/compliance/offerings/offering-iso-27001), [ISO 27018](/azure/compliance/offerings/offering-iso-27018), [ISO 27701](/azure/compliance/offerings/offering-iso-27701), [SOC 2](/azure/compliance/offerings/offering-soc-2), [FedRAMP](/azure/compliance/offerings/offering-fedramp), [HIPAA](/azure/compliance/offerings/offering-hipaa-us), and [GDPR](/compliance/regulatory/gdpr).
+
+For complete certification lists, audit reports, and compliance documentation, see:
+
++ [Azure compliance offerings](/azure/compliance/offerings/)
++ [Microsoft Azure Compliance Offerings white paper](https://servicetrust.microsoft.com/DocumentPage/7adf2d9e-d7b5-4e71-bad8-713e6a183cf3/)
++ [Microsoft Trust Center](https://www.microsoft.com/trust-center/compliance/compliance-overview)
+
+### Shared responsibility model
+
+Azure AI Search operates under the [shared responsibility model](/azure/security/fundamentals/shared-responsibility). Microsoft secures the infrastructure and built-in platform features described in this article. You're responsible for configuring security controls for your specific deployment.
+
++ **Microsoft manages** physical security, network infrastructure, platform security, default encryption (in transit, in use, and at rest), compliance certifications, and infrastructure updates.
+
++ **You configure** network access controls, authentication and authorization, outbound connections, document-level permissions, monitoring and alerting, and optional CMK and confidential computing.
+
+## Related content
+
++ [Secure an Azure AI Search service](search-security-best-practices.md)
++ [Azure security fundamentals](/azure/security/fundamentals/)
++ [Shared responsibility in the cloud](/azure/security/fundamentals/shared-responsibility)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Searchのデータ、プライバシー、および組み込み保護に関する新しい記事の追加"
}
```

### Explanation
この変更は、`articles/search/search-security-built-in.md`という新しいファイルの追加を示しており、合計160行が含まれています。この文章では、Azure AI Searchに組み込まれたセキュリティ機能、データの居住性、暗号化、コンプライアンス機能について詳しく説明しています。

主な内容としては、Microsoftが自動的に管理するセキュリティ保護が含まれており、顧客は特に何も構成を行わなくても安全に使用できることが強調されています。具体的には、トランスポート層セキュリティ（TLS）、サービス管理の暗号化、内部ネットワークセキュリティ、コンプライアンス認証、運用セキュリティなどが挙げられています。

また、データの暗号化や、プライバシーおよびデータ取り扱いに関するポリシー、ユーザーデータがモデル訓練に使用されないことについても触れています。この情報は、Azure AI Searchを利用する組織がセキュリティ対策を理解し、実施すべき領域に焦点を当てる手助けとなるでしょう。さらに、関連するリソースへのリンクも提供されており、ユーザーが追加の情報を取得するのに役立ちます。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ You can store keys using either:
 + Azure Key Vault Managed HSM (Hardware Security Module). An Azure Key Vault Managed HSM is an FIPS 140-2 Level 3 validated HSM. HSM support is new in Azure AI Search. To migrate from Azure Key Vault to HSM, [rotate your keys](#rotate-or-update-encryption-keys) and choose Managed HSM for storage.
 
 > [!IMPORTANT]
-> + CMK provides encryption for data at rest. If you need to protect data in use, consider using [confidential computing](search-security-overview.md#data-in-use).
+> + CMK provides encryption for data at rest. If you need to protect data in use, consider using [confidential computing](search-security-best-practices.md#optional-enable-confidential-computing).
 >
 > + CMK encryption is irreversible. You can rotate keys and change CMK configuration, but index encryption lasts for the lifetime of the index. Post-CMK encryption, an index is only accessible if the search service has access to the key. If you revoke access to the key by deleting or changing role assignment, the index is unusable and the service can't be scaled until the index is deleted or access to the key is restored. If you delete or rotate keys, the most recent key is cached for up to 60 minutes.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "暗号鍵の管理に関するドキュメントの修正"
}
```

### Explanation
この変更は、`articles/search/search-security-manage-encryption-keys.md`ファイルの修正を表しており、1行の追加と1行の削除が行われています。具体的には、Azure Key VaultのマネージドHSM（ハードウェアセキュリティモジュール）についての言及が新たに追加され、文中のリンク先が変更されました。

修正された文は、顧客管理の暗号鍵（CMK）がデータの静止時の暗号化を提供することを説明し、データ使用時の保護が必要な場合はコンフィデンシャルコンピューティングの利用を検討することを促しています。これにより、ユーザーはデータ保護の手段について、より正確な情報にアクセスできるようになります。この改善により、Azure AI Searchにおける暗号鍵管理の理解がさらに深まり、利用者が安全なデータ処理を実現するための助けとなることを目指しています。

## articles/search/search-security-overview.md{#item-6b3f1e}

<details>
<summary>Diff</summary>
````diff
@@ -1,321 +0,0 @@
----
-title: Secure your Azure AI Search deployment
-titleSuffix: Azure AI Search
-description: Learn about the security features in Azure AI Search to protect endpoints, content, and operations.
-manager: nitinme
-author: HeidiSteen
-ms.author: heidist
-ms.service: azure-ai-search
-ms.update-cycle: 180-days
-ms.custom:
-  - ignite-2023
-  - horz-security
-ms.topic: concept-article
-ms.date: 09/25/2025
----
-
-# Security in Azure AI Search
-
-Azure AI Search provides comprehensive security controls across network access, data access, and data protection to meet enterprise requirements. As a solution architect, you should understand three key security domains:
-
-+ **Network traffic patterns and network security**: Inbound, outbound, and internal traffic.
-+ **Access control mechanisms**: API keys or Microsoft Entra ID with roles.
-+ **Data residency and protection**: Encryption in transit, in use with optional confidential computing, and at rest with optional double encryption.
-
-A search service supports multiple network security topologies, from IP firewall restrictions for basic protection to private endpoints for complete network isolation. Optionally, use a network security perimeter to create a logical boundary around your Azure PaaS resources. For enterprise scenarios requiring granular permissions, you can implement document-level access controls. All security features integrate with Azure's compliance framework and support common enterprise patterns like multitenancy and cross-service authentication using managed identities.
-
-This article details the implementation options for each security layer to help you design appropriate security architectures for development and production environments.
-
-## Network traffic patterns
-
-An Azure AI Search service can be hosted in the Azure public cloud, an Azure private cloud, or a sovereign cloud (such as Azure Government). By default, for all cloud hosts, the search service is typically accessed by client applications over public network connections. While that pattern is predominant, it's not the only traffic pattern that you need to care about. Understanding all points of entry as well as outbound traffic is necessary background for securing your development and production environments.
-
-Azure AI Search has three basic network traffic patterns:
-
-+ Inbound requests made by a user or client to the search service (the predominant pattern)
-+ Outbound requests issued by the search service to other services on Azure and elsewhere
-+ Internal service-to-service requests over the secure Microsoft backbone network
-
-### Inbound traffic
-
-Inbound requests that target a search service endpoint include:
-
-+ Create, read, update, or delete indexes and other objects on the search service
-+ Load an index with search documents
-+ Query an index
-+ Run indexer or skillset jobs
-
-The [REST APIs](/rest/api/searchservice/) describe the full range of inbound requests that are handled by a search service.
-
-At a minimum, all inbound requests must be authenticated using either of these options:
-
-+ Key-based authentication (default). Inbound requests provide a valid API key.
-+ Role-based access control. Authorization is through Microsoft Entra identities and role assignments on your search service.
-
-Additionally, you can add [network security features](#service-access-and-authentication) to further restrict access to the endpoint. You can create either inbound rules in an IP firewall, or create private endpoints that fully shield your search service from the public internet. 
-
-### Outbound traffic
-
-Outbound requests can be secured and managed by you. Outbound requests originate from a search service to other applications. These requests are typically made by indexers for text-based and multimodal indexing, custom skills-based AI enrichment, and vectorizations at query time. Outbound requests include both read and write operations.
-
-The following list is a full enumeration of the outbound requests for which you can configure secure connections. A search service makes requests on its own behalf, and on the behalf of an indexer or custom skill.
-
-| Operation | Scenario |
-| ----------| -------- |
-| Indexers | Connect to external data sources to retrieve data (read access). For more information, see [Indexer access to content protected by Azure network security](search-indexer-securing-resources.md). |
-| Indexers | Connect to Azure Storage for write operations to  [knowledge stores](knowledge-store-concept-intro.md), [cached enrichments](enrichment-cache-how-to-configure.md), [debug sessions](cognitive-search-debug-session.md). |
-| Custom skills | Connect to Azure functions, Azure web apps, or other apps running external code that's hosted off-service. The request for external processing is sent during skillset execution. |
-| Indexers and [integrated vectorization](vector-search-integrated-vectorization.md) | Connect to Azure OpenAI and a deployed embedding model, or it goes through a custom skill to connect to an embedding model that you provide. The search service sends text to embedding models for vectorization during indexing. |
-| Vectorizers | Connect to Azure OpenAI or other embedding models at query time to [convert user text strings to vectors](vector-search-how-to-configure-vectorizer.md) for vector search. |
-| Knowledge bases | Connect to chat completion models for [agentic retrieval](agentic-retrieval-overview.md) query planning, and also for formulating answers grounded in search results. <p>If you're implementing a [basic RAG pattern](retrieval-augmented-generation-overview.md), your query logic calls an external chat completion model for formulating an answer grounded in search results. For this pattern, the connection to the model uses the identity of your client or user. The search service identity isn't used for the connection. In contrast, if you use [knowledge bases](agentic-retrieval-how-to-create-knowledge-base.md) in a RAG retrieval pattern, the outbound request is made by the search service managed identity. |
-| Search service | Connect to Azure Key Vault for [customer-managed encryption keys](search-security-manage-encryption-keys.md) used to encrypt and decrypt sensitive data. |
-
-Outbound connections can generally be made using a resource's full access connection string that includes a key or a database login, or [a managed identity](search-how-to-managed-identities.md) if you're using Microsoft Entra ID and role-based access.
-
-To reach Azure resources behind a firewall, [create inbound rules on other Azure resources that admit search service requests](search-indexer-howto-access-ip-restricted.md). 
-
-To reach Azure resources protected by Azure Private Link, [create a shared private link](search-indexer-howto-access-private.md) that an indexer uses to make its connection.
-
-#### Exception for same-region search and storage services
-
-If Azure Storage and Azure AI Search are in the same region, network traffic is routed through a private IP address and occurs over the Microsoft backbone network. Because private IP addresses are used, you can't configure IP firewalls or a private endpoint for network security. 
-
-Configure same-region connections using either of the following approaches:
-
-+ [Trusted service exception](search-indexer-howto-access-trusted-service-exception.md)
-+ [Resource instance rules](/azure/storage/common/storage-network-security?tabs=azure-portal#grant-access-from-azure-resource-instances)
-
-### Internal traffic
-
-Internal requests are secured and managed by Microsoft. You can't configure or control these connections. If you're locking down network access, no action on your part is required because internal traffic isn't customer-configurable.
-
-Internal traffic consists of:
-
-+ Service-to-service calls for tasks like authentication and authorization through Microsoft Entra ID, resource logging sent to Azure Monitor, and [private endpoint connections](service-create-private-endpoint.md) that utilize Azure Private Link.
-+ Requests for [built-in skills processing](cognitive-search-predefined-skills.md), with same-region requests directed to an internally hosted Microsoft Foundry resource used exclusively for built-in skills processing by Azure AI Search.
-+ Requests made to the various models that support [semantic ranking](semantic-search-overview.md#availability-and-pricing).
-
-<a name="service-access-and-authentication"></a>
-
-## Network security
-
-[Network security](/azure/security/fundamentals/network-overview) protects resources from unauthorized access or attack by applying controls to network traffic. Azure AI Search supports networking features that can be your frontline of defense against unauthorized access.
-
-### Inbound connection through IP firewalls
-
-A search service is provisioned with a public endpoint that allows access using a public IP address. To restrict which traffic comes through the public endpoint, create an inbound firewall rule that admits requests from a specific IP address or a range of IP addresses. All client connections must be made through an allowed IP address, or the connection is denied.
-
-:::image type="content" source="media/search-security-overview/inbound-firewall-ip-restrictions.png" alt-text="sample architecture diagram for ip restricted access":::
-
-You can use the Azure portal to [configure firewall access](service-configure-firewall.md).
-
-Alternatively, you can use the management REST APIs. Starting with API version 2020-03-13, with the [IpRule](/rest/api/searchmanagement/services/create-or-update#iprule) parameter, you can restrict access to your service by identifying IP addresses, individually or in a range, that you want to grant access to your search service.
-
-### Inbound connection to a private endpoint (network isolation, no Internet traffic)
-
-For more stringent security, you can establish a [private endpoint](/azure/private-link/private-endpoint-overview) for Azure AI Search allows a client on a [virtual network](/azure/virtual-network/virtual-networks-overview) to securely access data in a search index over a [Private Link](/azure/private-link/private-link-overview).
-
-The private endpoint uses an IP address from the virtual network address space for connections to your search service. Network traffic between the client and the search service traverses over the virtual network and a private link on the Microsoft backbone network, eliminating exposure from the public internet. A virtual network allows for secure communication among resources, with your on-premises network as well as the Internet.
-
-:::image type="content" source="media/search-security-overview/inbound-private-link-azure-cog-search.png" alt-text="sample architecture diagram for private endpoint access":::
-
-While this solution is the most secure, using more services is an added cost so be sure you have a clear understanding of the benefits before diving in. For more information about costs, see the [pricing page](https://azure.microsoft.com/pricing/details/private-link/). For more information about how these components work together, [watch this video](/Shows/AI-Show/Azure-Cognitive-Search-Whats-new-in-security). Coverage of the private endpoint option starts at 5:48 into the video. For instructions on how to set up the endpoint, see [Create a Private Endpoint for Azure AI Search](service-create-private-endpoint.md).
-
-### Network security perimeter
-
-A network security perimeter is a logical network boundary around your platform-as-a-service (PaaS) resources that are deployed outside of a virtual network. It establishes a perimeter for controlling public network access to resources like Azure AI Search, Azure Storage, and Azure OpenAI. You can grant exceptions through explicit access rules for inbound and outbound traffic. This approach helps prevent data exfiltration while maintaining necessary connectivity for your applications.
-
-Inbound client connections and service-to-service connections occur within the boundary, which simplifies and strengthens your defenses against unauthorized access. It's common in Azure AI Search solutions to use multiple Azure resources. The following resources can all be joined to an [existing network security perimeter](/azure/private-link/create-network-security-perimeter-portal):
-
-+ [Azure AI Search](search-security-network-security-perimeter.md)
-+ [Azure OpenAI](/azure/ai-foundry/openai/how-to/network-security-perimeter)
-+ [Azure Storage](/azure/storage/common/storage-network-security-perimeter)
-+ [Azure Monitor](/azure/azure-monitor/fundamentals/network-security-perimeter)
-
-For a complete list of eligible services, see [Onboarded private link resources](/azure/private-link/network-security-perimeter-concepts#onboarded-private-link-resources).
-
-## Authentication
-
-Once a request is admitted to the search service, it must still undergo authentication and authorization that determines whether the request is permitted. Azure AI Search supports two approaches:
-
-+ [Microsoft Entra authentication](search-security-rbac.md) establishes the caller (and not the request) as the authenticated identity. An Azure role assignment determines authorization. 
-
-+ [Key-based authentication](search-security-api-keys.md) is performed on the request (not the calling app or user) through an API key, where the key is a string composed of randomly generated numbers and letters that prove the request is from a trustworthy source. Keys are required on every request. Submission of a valid key is considered proof the request originates from a trusted entity. 
-
-  Reliance on API key-based authentication means that you should have a plan for regenerating the admin key at regular intervals, per Azure security best practices. There are a maximum of two admin keys per search service. For more information about securing and managing API keys, see [Create and manage api-keys](search-security-api-keys.md).
-
-Key-based authentication is the default for data plane operations (creating and using objects on the search service). You can use both authentication methods, or [disable an approach](search-security-enable-roles.md) that you don't want available on your search service.
-
-## Authorization
-
-Azure AI Search provides authorization models for service management and content management. 
-
-### Privileged access
-
-On a new search service, existing role assignments at the subscription level are inherited by the search service, and only Owners and User Access Administrators can grant access.
-
-Control plane operations (service or resource creation and management) tasks are exclusively authorized through [role assignments](/azure/role-based-access-control/overview), with no ability to use key-based authentication for service administration.
-
-Control plane operations include create, configure, or delete the service, and manage security. As such, Azure role assignments will determine who can perform those tasks, regardless of whether they're using the [portal](search-manage.md), [PowerShell](search-manage-powershell.md), or the [Management REST APIs](/rest/api/searchmanagement).
-
-[Three basic roles](search-security-rbac.md#assign-roles-for-service-administration) (Owner, Contributor, Reader) apply to search service administration. 
-
-> [!NOTE]
-> Using Azure-wide mechanisms, you can lock a subscription or resource to prevent accidental or unauthorized deletion of your search service by users with admin rights. For more information, see [Lock resources to prevent unexpected deletion](/azure/azure-resource-manager/management/lock-resources).
-
-### Authorize access to content
-
-Data plane operations refers to the objects created and used on a search service.
-
-+ For role-based authorization, [use Azure role assignments](search-security-rbac.md) to establish read-write access to operations.
-
-+ For key-based authorization, [an API key](search-security-api-keys.md) and a qualified endpoint determine access. An endpoint might be the service itself, the indexes collection, a specific index, a documents collection, or a specific document. When chained together, the endpoint, the operation (for example, a create request) and the type of key (admin or query) authorize access to content and operations.
-
-### Restricting access to indexes
-
-Using Azure roles, you can [set permissions on individual indexes](search-security-rbac.md#grant-access-to-a-single-index) as long as it's done programmatically.
-
-Using keys, anyone with an [admin key](search-security-api-keys.md) to your service can read, modify, or delete any index in the same service. For protection against accidental or malicious deletion of indexes, your in-house source control for code assets is the solution for reversing an unwanted index deletion or modification. Azure AI Search has failover within the cluster to ensure availability, but it doesn't store or execute your proprietary code used to create or load indexes.
-
-For multitenancy solutions requiring security boundaries at the index level, it's common to handle index isolation in the middle tier in your application code. For more information about the multitenant use case, see [Design patterns for multitenant SaaS applications and Azure AI Search](search-modeling-multitenant-saas-applications.md).
-
-### Restricting access to documents
-
-User permissions at the document level, also known as *row-level security*, is available as a preview feature and depends on the data source. If content originates from [Azure Data Lake Storage (ADLS) Gen2](search-indexer-access-control-lists-and-role-based-access.md) or [Azure blobs](search-blob-indexer-role-based-access.md), user permission metadata that originates in Azure Storage is preserved in indexer-generated indexes and enforced at query time so that only authorized content is included in search results.
-
-For other data sources, you can [push a document payload that includes user or group permission metadata](search-index-access-control-lists-and-rbac-push-api.md), and those permissions are retained in indexed content and also enforced at query time. This capability is also in preview.
-
-If you can't use preview features and you require permissioned access over content in search results, there's a technique for applying filters that include or exclude documents based on user identity. This workaround adds a string field in the data source that represents a group or user identity, which you can make filterable in your index. For more information about this pattern, see [Security trimming based on identity filters](search-security-trimming-for-azure-search.md). For more information about document access, see [Document-level access control](search-document-level-access-overview.md).
-
-## Data residency
-
-When you set up a search service, you choose a region that determines where customer data is stored and processed. Each region exists within a [geography (Geo)](https://azure.microsoft.com/explore/global-infrastructure/geographies/#overview) that often includes multiple regions (for example, Switzerland is a Geo that contains Switzerland North and Switzerland West). Azure AI Search might replicate your data to another region within the same Geo for durability and high availability. The service won't store or process customer data outside of your specified Geo unless you configure a feature that has a dependency on another Azure resource, and that resource is provisioned in a different region.
-
-Currently, the only external resource that a search service writes to is Azure Storage. The storage account is one that you provide, and it could be in any region. A search service writes to Azure Storage if you use any of the following features:
-
-+ [enrichment cache](enrichment-cache-how-to-configure.md)
-+ [debug session](cognitive-search-debug-session.md)
-+ [knowledge store](knowledge-store-concept-intro.md)
-
-For more information about data residency, see [data residency in Azure](https://azure.microsoft.com/explore/global-infrastructure/data-residency/#overview).
-
-### Exceptions to data residency commitments
-
-Object names appear in the telemetry logs used by Microsoft to provide support for the service. Object names are stored and processed outside of your selected region or location. Object names include the names of indexes and index fields, aliases, indexers, data sources, skillsets, synonym maps, resources, containers, and key vault store. Customers shouldn't place any sensitive data in name fields or create applications designed to store sensitive data in these fields. 
-
-Telemetry logs are retained for one and a half years. During that period, Microsoft might access and reference object names under the following conditions:
-
-+ Diagnose an issue, improve a feature, or fix a bug. In this scenario, data access is internal only, with no third-party access.
-
-+ During support, this information might be used to provide quick resolution to issues and escalate product team if needed
-
-<a name="encryption"></a>
-
-## Data protection
-
-At the storage layer, data encryption is built in for all service-managed content saved to disk, including indexes, synonym maps, and the definitions of indexers, data sources, and skillsets. Service-managed encryption applies to both long-term data storage and temporary data storage.
-
-Optionally, you can add customer-managed keys (CMK) for supplemental encryption of indexed content for double encryption of data at rest. For services created after August 1 2020, CMK encryption extends to short-term data on temporary disks.
-
-### Data in transit
-
-For search service connections over the public internet, Azure AI Search listens on HTTPS port 443.
-
-Azure AI Search supports TLS 1.2 and 1.3 for client-to-service channel encryption:
-
-+ TLS 1.3 is the default on newer client operating systems and versions of .NET.
-+ TLS 1.2 is the default on older systems, but you can [explicitly set TLS 1.3 on a client request](/dotnet/framework/network-programming/tls).
-
-Earlier versions of TLS (1.0 or 1.1) aren't supported.
-
-For more information, see [TLS support in .NET Framework](/dotnet/framework/network-programming/tls#tls-support-in-net-framework).
-
-### Data in use
-
-By default, Azure AI Search deploys your search service on standard Azure infrastructure. This infrastructure encrypts data at rest and in transit, but it doesn't protect data while it's being actively processed in memory.
-
-Optionally, you can use the [Azure portal](search-create-service-portal.md#choose-a-compute-type) or [Services - Create or Update (REST API)](/rest/api/searchmanagement/services/create-or-update) to configure confidential computing during service creation. Confidential computing protects data in use from unauthorized access, including from Microsoft, through hardware attestation and encryption. For more information, see [Confidential computing use cases](/azure/confidential-computing/use-cases-scenarios).
-
-The following table compares both compute types.
-
-| Compute type | Description | Limitations | Cost | Availability |
-|--|--|--|--|--|
-| Default | Processes data on standard VMs with built-in encryption for data at rest and in transit. No hardware-based isolation for data in use. | No limitations. | No change to the base cost of free or billable tiers. | Available in all regions. |
-| Confidential | Processes data on confidential VMs (DCasv5 or DCesv5) in a hardware-based trusted execution environment. Isolates computations and memory from the host operating system and other VMs. | Disables or restricts [agentic retrieval](agentic-retrieval-overview.md), [semantic ranker](semantic-search-overview.md), [query rewrite](semantic-how-to-query-rewrite.md), [skillset execution](cognitive-search-concept-intro.md), and indexers that run in the [multitenant environment](search-howto-run-reset-indexers.md#indexer-execution-environment) <sup>1</sup>. | Adds a 10% surcharge to the base cost of billable tiers. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/search/). | Available in some regions. For more information, see the [list of supported regions](search-region-support.md). |
-
-<sup>1</sup> When you enable this compute type, indexers can only run in the private execution environment, meaning they run from the search clusters hosted on confidential computing.
-
-> [!IMPORTANT]
-> We only recommend confidential computing for organizations whose compliance or regulatory requirements necessitate data-in-use protection. For daily usage, the default compute type suffices.
-
-### Data at rest
-
-For data handled internally by the search service, the following table describes the [data encryption models](/azure/security/fundamentals/encryption-models). Some features, such as knowledge store, incremental enrichment, and indexer-based indexing, read from or write to data structures in other Azure Services. Services that have a dependency on Azure Storage can use the [encryption features](/azure/storage/common/storage-service-encryption) of that technology.
-
-| Model | Keys&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Requirements&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Restrictions | Applies to |
-|------------------|-------|-------------|--------------|------------|
-| server-side encryption | Microsoft-managed keys | None (built-in) | None, available on all tiers, in all regions, for content created after January 24, 2018. | Content (indexes and synonym maps) and definitions (indexers, data sources, skillsets) on data disks and temporary disks |
-| server-side encryption | customer-managed keys | Azure Key Vault | Available on billable tiers, in specific regions, for content created after August 1, 2020. | Content (indexes and synonym maps) and definitions (indexers, data sources, skillsets) on data disks |
-| server-side full encryption | customer-managed keys | Azure Key Vault | Available on billable tiers, in all regions, on search services after May 13, 2021. | Content (indexes and synonym maps) and definitions (indexers, data sources, skillsets) on data disks and temporary disks |
-
-When you introduce CMK encryption, you're encrypting content twice. For the objects and fields noted in the previous section, content is first encrypted with your CMK, and secondly with the Microsoft-managed key. Content is doubly encrypted on data disks for long-term storage, and on temporary disks used for short-term storage.
-
-#### Service-managed keys
-
-Service-managed encryption is a Microsoft-internal operation that uses 256-bit [AES encryption](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard). It occurs automatically on all indexing, including on incremental updates to indexes that aren't fully encrypted (created before January 2018).
-
-Service-managed encryption applies to all content on long-term and short-term storage.
-
-#### Customer-managed keys (CMK)
-
-Customers use CMK for two reasons: extra protection, and the ability to revoke keys, preventing access to content.
-
-Customer-managed keys require another billable service, Azure Key Vault, which can be in a different region, but under the same Azure tenant, as Azure AI Search. 
-
-CMK support was rolled out in two phases. If you created your search service during the first phase, CMK encryption was restricted to long-term storage and specific regions. Services created in the second phase can use CMK encryption in any region. As part of the second wave rollout, content is CMK-encrypted on both long-term and short-term storage.
-
-+ The first rollout was on August 1, 2020 and included the following five regions. Search services created in the following regions supported CMK for data disks, but not temporary disks:
-
-  + West US 2
-  + East US
-  + South Central US
-  + US Gov Virginia
-  + US Gov Arizona
-
-+ The second rollout on May 13, 2021 added encryption for temporary disks and extended CMK encryption to [all supported regions](search-region-support.md).
-
-  If you're using CMK from a service created during the first rollout and you also want CMK encryption over temporary disks, you need to create a new search service in your region of choice and redeploy your content. To determine your service creation date, see [Check your service creation or upgrade date](search-how-to-upgrade.md#check-your-service-creation-or-upgrade-date).
-
-Enabling CMK encryption will increase index size and degrade query performance. Based on observations to date, you can expect to see an increase of 30-60 percent in query times, although actual performance will vary depending on the index definition and types of queries. Because of the negative performance impact, we recommend that you only enable this feature on indexes that really require it. For more information, see [Configure customer-managed encryption keys in Azure AI Search](search-security-manage-encryption-keys.md).
-
-## Logging and monitoring
-
-Azure AI Search doesn't log user identities so you can't refer to logs for information about a specific user. However, the service does log create-read-update-delete operations, which you might be able to correlate with other logs to understand the agency of specific actions.
-
-Using alerts and the logging infrastructure in Azure, you can pick up on query volume spikes or other actions that deviate from expected workloads. For more information about setting up logs, see [Collect and analyze log data](monitor-azure-cognitive-search.md) and [Monitor query requests](search-monitor-queries.md).
-
-## Compliance and governance
-
-Azure AI Search participates in regular audits, and has been certified against many global, regional, and industry-specific standards for both the public cloud and Azure Government. For the complete list, download the [**Microsoft Azure Compliance Offerings** whitepaper](https://azure.microsoft.com/resources/microsoft-azure-compliance-offerings/) from the official Audit reports page.
-
-We recommend that you regularly review [Azure AI Search compliance certifications and documentation](/azure/compliance/) to ensure alignment with your regulatory requirements. 
-
-### Use Azure Policy
-
-For compliance, you can use [Azure Policy](/azure/governance/policy/overview) to implement the high-security best practices of [Microsoft cloud security benchmark](/security/benchmark/azure/introduction). The Microsoft cloud security benchmark is a collection of security recommendations, codified into security controls that map to key actions you should take to mitigate threats to services and data. There are currently 12 security controls, including [Network Security](/security/benchmark/azure/mcsb-network-security), Logging and Monitoring, and [Data Protection](/security/benchmark/azure/mcsb-data-protection).
-
-Azure Policy is a capability built into Azure that helps you manage compliance for multiple standards, including those of Microsoft cloud security benchmark. For well-known benchmarks, Azure Policy provides built-in definitions that provide both criteria and an actionable response that addresses noncompliance.
-
-For Azure AI Search, there's currently one built-in definition. It's for resource logging. You can assign a policy that identifies search services that are missing resource logging, and then turn it on. For more information, see [Azure Policy Regulatory Compliance controls for Azure AI Search](security-controls-policy.md).
-
-### Use tags
-
-Apply metadata tags to categorize search services based on data sensitivity and compliance requirements. This facilitates proper governance and security controls. For more information, see [Use tags to organize your Azure resources](/azure/azure-resource-manager/management/tag-resources) and [General guidance – Organize Azure resources using tags](/azure/azure-resource-manager/management/tag-resources).
-
-## Related content
-
-+ [Azure security fundamentals](/azure/security/fundamentals/)
-+ [Azure Security](https://azure.microsoft.com/overview/security)
-+ [Microsoft Defender for Cloud](/azure/security-center/)
-
-We also recommend the following [video on security features](/Shows/AI-Show/Azure-Cognitive-Search-Whats-new-in-security). It's several years old and doesn't cover newer features, but it covers these features: CMK, IP firewalls, and private link. If you use those features, you might find this video helpful.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azure AI Searchのセキュリティ概要に関する既存の記事の削除"
}
```

### Explanation
この変更は、`articles/search/search-security-overview.md`ファイルが完全に削除されたことを示しています。このファイルは、Azure AI Searchに関連するセキュリティ機能、データ保護、アクセス制御の概要を提供しており、企業の要件を満たすための包括的なセキュリティ対策について詳細に説明していました。

削除された内容には、ネットワークトラフィックパターンやアクセス管理の仕組み、データの取り扱いや居住性など、多くのセキュリティ関連の重要なトピックが含まれていました。特に、セキュリティ層の実装オプション、インバウンドおよびアウトバウンドトラフィックの管理、そしてユーザーのアクセス許可に関する詳細情報が提供されていたため、Azure AI Searchを使用する際のセキュリティの理解を深めるための重要なリソースでした。

この削除は、今後のドキュメンテーションやリソースの再編成を示唆している可能性があり、ユーザーは新たな情報源を探し、セキュリティに関する理解を維持する必要があります。すでに提供されている情報や新たなドキュメントへも目を向けることをお勧めします。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -420,16 +420,10 @@ items:
       items:
       - name: What is multimodal search?
         href: multimodal-search-overview.md
-      - name: Tutorials
-        items:
-        - name: Vectorize images and text
-          href: tutorial-document-extraction-multimodal-embeddings.md
-        - name: Vectorize from a structured document layout
-          href: tutorial-document-layout-multimodal-embeddings.md
-        - name: Verbalize images using generative AI
-          href: tutorial-document-extraction-image-verbalization.md
-        - name: Verbalize images from a structured document layout
-          href: tutorial-document-layout-image-verbalization.md
+      - name: Tutorial (REST)
+        href: tutorial-multimodal.md
+      - name: Multimodal samples (REST)
+        href: https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/multimodal-tutorial
     - name: Other query types
       href: search-query-overview.md
   - name: Relevance and ranking
@@ -512,8 +506,10 @@ items:
 
 - name: Security
   items:
-  - name: Security in Azure AI Search
-    href: search-security-overview.md
+  - name: Built-in security
+    href: search-security-built-in.md
+  - name: Secure a search service
+    href: search-security-best-practices.md
   - name: Network access
     items:
     - name: Configure network access
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次ファイルの更新とチュートリアルリソースの整理"
}
```

### Explanation
この変更は、`articles/search/toc.yml`ファイルの更新を示しており、目次に関するエントリが変更されました。具体的には、8行の追加と12行の削除が行われ、全体で20行の変更がありました。

主な変更点として、従来のチュートリアルセクションが簡略化され、新たに「Tutorial (REST)」および「Multimodal samples (REST)」が追加されました。これにより、ユーザーにとっての確認が容易になり、REST API を利用したマルチモーダル検索に関するサンプルコードやチュートリアルが一元化されています。

さらに、セキュリティ関連の項目も更新されており、「Security in Azure AI Search」のリンクが「Built-in security」と「Secure a search service」に変更されました。これにより、Azure AI Search におけるセキュリティ機能やベストプラクティスに関する情報がより明確に提示されるようになっています。

全体として、この変更はドキュメントが最新の情報を反映し、ユーザーが求めるリソースにアクセスしやすくするための改善を図っています。

## articles/search/tutorial-document-extraction-image-verbalization.md{#item-398a90}

<details>
<summary>Diff</summary>
````diff
@@ -1,769 +0,0 @@
----
-title: 'Tutorial: Verbalize images using generative AI'
-titleSuffix: Azure AI Search
-description: Learn how to extract, index, and search multimodal content using the Document Extraction skill for chunking and GenAI Prompt skill for image verbalizations.
-manager: arjagann
-author: mdonovan
-ms.author: mdonovan
-ms.service: azure-ai-search
-ms.update-cycle: 180-days
-ms.custom:
-ms.topic: tutorial
-ms.date: 08/27/2025
-
----
-
-# Tutorial: Verbalize images using generative AI
-
-Azure AI Search can extract and index both text and images from PDF documents stored in Azure Blob Storage. This tutorial shows you how to build a multimodal indexing pipeline that *chunks data  using the built-in Text Split skill* and uses *image verbalization* to describe images. Cropped images are stored in a knowledge store, and visual content is described in natural language and ingested alongside text in a searchable index.
-
-To get image verbalizations, each extracted image is passed to the [GenAI Prompt skill (preview)](cognitive-search-skill-genai-prompt.md) that calls a chat completion model to generate a concise textual description. These descriptions, along with the original document text, are then embedded into vector representations using Azure OpenAI’s text-embedding-3-large model. The result is a single index containing searchable content from both modalities: text and verbalized images.
-
-In this tutorial, you use:
-
-+ A 36-page PDF document that combines rich visual content, such as charts, infographics, and scanned pages, with traditional text.
-
-+ An indexer and skillset to create an indexing pipeline that includes AI enrichment through skills.
-
-+ The [Document Extraction skill](cognitive-search-skill-document-extraction.md) for extracting normalized images and text. The [Text Split skill](cognitive-search-skill-textsplit.md) chunks the data.
-
-+ The [GenAI Prompt skill (preview)](cognitive-search-skill-genai-prompt.md) that calls a chat completion model to create descriptions of visual content.
-
-+ A search index configured to store text and image verbalizations. Some content is vectorized for vector-based similarity search.
-
-This tutorial demonstrates a lower-cost approach for indexing multimodal content using the Document Extraction skill and image captioning. It enables extraction and search over both text and images from documents in Azure Blob Storage. However, it doesn't include locational metadata for text, such as page numbers or bounding regions. For a more comprehensive solution that includes structured text layout and spatial metadata, see [Tutorial: Verbalize images from a structured document layout](tutorial-document-layout-image-verbalization.md).
-
-> [!NOTE]
-> Image extraction by the Document Extraction skill isn't free. Setting `imageAction` to `generateNormalizedImages` in the skillset triggers image extraction, which is an extra charge. For billing information, see [Azure AI Search pricing](https://azure.microsoft.com/pricing/details/search/).
-
-## Prerequisites
-
-+ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier.
-
-+ [Azure Storage](/azure/storage/common/storage-account-create), used for storing sample data and for creating a [knowledge store](knowledge-store-concept-intro.md).
-
-+ [Azure OpenAI](/azure/ai-foundry/openai/how-to/create-resource) with a deployment of
-
-  + A chat completion model hosted in Microsoft Foundry or another source. The model is used to verbalize image content. You provide the URI to the hosted model in the GenAI Prompt skill definition. You can use [any chat completion model](cognitive-search-skill-genai-prompt.md#supported-models).
-
-  + A text embedding model deployed in Foundry. The model is used to vectorize text content pull from source documents and the image descriptions generated by the chat completion model. For integrated vectorization, the embedding model must be located in Foundry, and it must be either text-embedding-ada-002, text-embedding-3-large, or text-embedding-3-small. If you want to use an external embedding model, use a custom skill instead of the Azure OpenAI embedding skill.
-
-+ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
-
-## Prepare data
-
-The following instructions apply to Azure Storage which provides the sample data and also hosts the knowledge store. A search service identity needs read access to Azure Storage to retrieve the sample data, and it needs write access to create the knowledge store. The search service creates the container for cropped images during skillset processing, using the name you provide in an environment variable.
-
-1. Download the following sample PDF: [sustainable-ai-pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Accelerating-Sustainability-with-AI-2025.pdf)
-
-1. In Azure Storage, create a new container named **sustainable-ai-pdf**.
-
-1. [Upload the sample data file](/azure/storage/blobs/storage-quickstart-blobs-portal).
-
-1. [Create role assignments and specify a managed identity in a connection string](search-howto-managed-identities-storage.md):
-
-   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer. Assign **Storage Blob Data Contributor** and **Storage Table Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
-
-   1. For connections made using a system-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
-
-        ```json
-        "credentials" : { 
-            "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-        }
-        ```
-
-   1. For connections made using a user-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. Provide an identity using the syntax shown in the following example. Set userAssignedIdentity to the user-assigned managed identity. The connection string is similar to the following example:
-
-      ```json
-      "credentials" : { 
-          "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-      },
-      "identity" : { 
-          "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
-          "userAssignedIdentity" : "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MY-DEMO-USER-MANAGED-IDENTITY" 
-      }
-      ```
-
-## Prepare models
-
-This tutorial assumes you have an existing Azure OpenAI resource through which the skills call the text embedding model and chat completion models. The search service connects to the models during skillset processing and during query execution using its managed identity. This section gives you guidance and links for assigning roles for authorized access.
-
-1. Sign in to the Azure portal (not the Foundry portal) and find the Azure OpenAI resource.
-
-1. Select **Access control (IAM)**.
-
-1. Select **Add** and then **Add role assignment**.
-
-1. Search for **Cognitive Services OpenAI User** and then select it.
-
-1. Choose **Managed identity** and then assign your [search service managed identity](search-how-to-managed-identities.md).
-
-For more information, see [Role-based access control for Azure OpenAI in Foundry Models](/azure/ai-foundry/openai/how-to/role-based-access-control).
-
-## Set up your REST file
-
-For this tutorial, your local REST client connection to Azure AI Search requires an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Connect to a search service](search-get-started-rbac.md).
-
-For authenticated connections that occur during indexer and skillset processing, the search service uses the role assignments you previously defined.
-
-1. Start Visual Studio Code and create a new file.
-
-1. Provide values for variables used in the request. For `@storageConnection`, make sure your connection string doesn't have a trailing semicolon or quotation marks. For `@imageProjectionContainer`, provide a container name that's unique in blob storage. Azure AI Search creates this container for you during skills processing.
-
-   ```http
-   @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
-   @searchApiKey = PUT-YOUR-ADMIN-API-KEY-HERE
-   @storageConnection = PUT-YOUR-STORAGE-CONNECTION-STRING-HERE
-   @openAIResourceUri = PUT-YOUR-OPENAI-URI-HERE
-   @openAIKey = PUT-YOUR-OPENAI-KEY-HERE
-   @chatCompletionResourceUri = PUT-YOUR-CHAT-COMPLETION-URI-HERE
-   @chatCompletionKey = PUT-YOUR-CHAT-COMPLETION-KEY-HERE
-   @imageProjectionContainer=sustainable-ai-pdf-images
-   ```
-
-1. Save the file using a `.rest` or `.http` file extension. For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
-
-To get the Azure AI Search endpoint and API key:
-
-1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
-
-1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
-
-   :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
-
-## Create a data source
-
-[Create Data Source (REST)](/rest/api/searchservice/data-sources/create) creates a data source connection that specifies what data to index.
-
-```http
-### Create a data source
-POST {{searchUrl}}/datasources?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-  {
-    "name": "doc-extraction-image-verbalization-ds",
-    "description": null,
-    "type": "azureblob",
-    "subtype": null,
-    "credentials":{
-      "connectionString":"{{storageConnection}}"
-    },
-    "container": {
-      "name": "sustainable-ai-pdf",
-      "query": null
-    },
-    "dataChangeDetectionPolicy": null,
-    "dataDeletionDetectionPolicy": null,
-    "encryptionKey": null,
-    "identity": null
-  }
-```
-
-Send the request. The response should look like:
-
-```json
-HTTP/1.1 201 Created
-Transfer-Encoding: chunked
-Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
-Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-11-01-preview -Preview
-Server: Microsoft-IIS/10.0
-Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
-Preference-Applied: odata.include-annotations="*"
-OData-Version: 4.0
-request-id: 4eb8bcc3-27b5-44af-834e-295ed078e8ed
-elapsed-time: 346
-Date: Sat, 26 Apr 2025 21:25:24 GMT
-Connection: close
-
-{
-  "name": "doc-extraction-multimodal-embedding-ds",
-  "description": null,
-  "type": "azureblob",
-  "subtype": null,
-  "indexerPermissionOptions": [],
-  "credentials": {
-    "connectionString": null
-  },
-  "container": {
-    "name": "sustainable-ai-pdf",
-    "query": null
-  },
-  "dataChangeDetectionPolicy": null,
-  "dataDeletionDetectionPolicy": null,
-  "encryptionKey": null,
-  "identity": null
-}
-```
-
-## Create an index
-
-[Create Index (REST)](/rest/api/searchservice/indexes/create) creates a search index on your search service. An index specifies all the parameters and their attributes.
-
-For nested JSON, the index fields must be identical to the source fields. Currently, Azure AI Search doesn't support field mappings to nested JSON, so field names and data types must match completely. The following index aligns to the JSON elements in the raw content.
-
-```http
-### Create an index
-POST {{searchUrl}}/indexes?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-{
-    "name": "doc-extraction-image-verbalization-index",
-    "fields": [
-        {
-            "name": "content_id",
-            "type": "Edm.String",
-            "retrievable": true,
-            "key": true,
-            "analyzer": "keyword"
-        },
-        {
-            "name": "text_document_id",
-            "type": "Edm.String",
-            "searchable": false,
-            "filterable": true,
-            "retrievable": true,
-            "stored": true,
-            "sortable": false,
-            "facetable": false
-        },          
-        {
-            "name": "document_title",
-            "type": "Edm.String",
-            "searchable": true
-        },
-        {
-            "name": "image_document_id",
-            "type": "Edm.String",
-            "filterable": true,
-            "retrievable": true
-        },
-        {
-            "name": "content_text",
-            "type": "Edm.String",
-            "searchable": true,
-            "retrievable": true
-        },
-        {
-            "name": "content_embedding",
-            "type": "Collection(Edm.Single)",
-            "dimensions": 3072,
-            "searchable": true,
-            "retrievable": true,
-            "vectorSearchProfile": "hnsw"
-        },
-        {
-            "name": "content_path",
-            "type": "Edm.String",
-            "searchable": false,
-            "retrievable": true
-        },
-        {
-            "name": "offset",
-            "type": "Edm.String",
-            "searchable": false,
-            "retrievable": true
-        },
-        {
-            "name": "location_metadata",
-            "type": "Edm.ComplexType",
-            "fields": [
-                {
-                "name": "page_number",
-                "type": "Edm.Int32",
-                "searchable": false,
-                "retrievable": true
-                },
-                {
-                "name": "bounding_polygons",
-                "type": "Edm.String",
-                "searchable": false,
-                "retrievable": true,
-                "filterable": false,
-                "sortable": false,
-                "facetable": false
-                }
-            ]
-        }         
-    ],
-    "vectorSearch": {
-        "profiles": [
-            {
-                "name": "hnsw",
-                "algorithm": "defaulthnsw",
-                "vectorizer": "demo-vectorizer"
-            }
-        ],
-        "algorithms": [
-            {
-                "name": "defaulthnsw",
-                "kind": "hnsw",
-                "hnswParameters": {
-                    "m": 4,
-                    "efConstruction": 400,
-                    "metric": "cosine"
-                }
-            }
-        ],
-        "vectorizers": [
-            {
-              "name": "demo-vectorizer",
-              "kind": "azureOpenAI",    
-              "azureOpenAIParameters": {
-                "resourceUri": "{{openAIResourceUri}}",
-                "deploymentId": "text-embedding-3-large",
-                "searchApiKey": "{{openAIKey}}",
-                "modelName": "text-embedding-3-large"
-              }
-            }
-        ]
-    },
-    "semantic": {
-        "defaultConfiguration": "semanticconfig",
-        "configurations": [
-            {
-                "name": "semanticconfig",
-                "prioritizedFields": {
-                    "titleField": {
-                        "fieldName": "document_title"
-                    },
-                    "prioritizedContentFields": [
-                    ],
-                    "prioritizedKeywordsFields": []
-                }
-            }
-        ]
-    }
-}
-```
-
-Key points:
-
-+ Text and image embeddings are stored in the `content_embedding` field and must be configured with appropriate dimensions (for example, 3072) and a vector search profile.
-
-+ `location_metadata` captures bounding polygon and page number metadata for each normalized image, enabling precise spatial search or UI overlays. `location_metadata` only exists for images in this scenario. If you'd like to capture locational metadata for text as well, consider using [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md). An in-depth tutorial is linked at the bottom of the page.
-
-+ For more information on vector search, see [Vectors in Azure AI Search](vector-search-overview.md).
-
-+ For more information on semantic ranking, see [Semantic ranking in Azure AI Search](semantic-search-overview.md)
-
-## Create a skillset
-
-[Create Skillset (REST)](/rest/api/searchservice/skillsets/create) creates a skillset on your search service. A skillset defines the operations that chunk and embed content prior to indexing. This skillset uses the built-in Document Extraction skill to extract text and images. It uses Text Split skill to chunk large text. It uses Azure OpenAI Embedding skill to vectorize text content.
-
-The skillset also performs actions specific to images. It uses the GenAI Prompt skill to generate image descriptions. It also creates a knowledge store that stores intact images so that you can return them in a query.
-
-```http
-### Create a skillset
-POST {{searchUrl}}/skillsets?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-{
-  "name": "doc-extraction-image-verbalization-skillset",
-  "description": "A test skillset",
-  "skills": [
-    {
-      "@odata.type": "#Microsoft.Skills.Util.DocumentExtractionSkill",
-      "name": "document-extraction-skill",
-      "description": "Document extraction skill to extract text and images from documents",
-      "parsingMode": "default",
-      "dataToExtract": "contentAndMetadata",
-      "configuration": {
-          "imageAction": "generateNormalizedImages",
-          "normalizedImageMaxWidth": 2000,
-          "normalizedImageMaxHeight": 2000
-      },
-      "context": "/document",
-      "inputs": [
-        {
-          "name": "file_data",
-          "source": "/document/file_data"
-        }
-      ],
-      "outputs": [
-        {
-          "name": "content",
-          "targetName": "extracted_content"
-        },
-        {
-          "name": "normalized_images",
-          "targetName": "normalized_images"
-        }
-      ]
-    },
-    {
-      "@odata.type": "#Microsoft.Skills.Text.SplitSkill",
-      "name": "split-skill",
-      "description": "Split skill to chunk documents",
-      "context": "/document",
-      "defaultLanguageCode": "en",
-      "textSplitMode": "pages",
-      "maximumPageLength": 2000,
-      "pageOverlapLength": 200,
-      "unit": "characters",
-      "inputs": [
-        {
-          "name": "text",
-          "source": "/document/extracted_content",
-          "inputs": []
-        }
-      ],
-      "outputs": [
-        {
-          "name": "textItems",
-          "targetName": "pages"
-        }
-      ]
-    }, 
-    {
-    "@odata.type": "#Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill",
-    "name": "text-embedding-skill",
-    "description": "Embedding skill for text",
-    "context": "/document/pages/*",
-    "inputs": [
-        {
-        "name": "text",
-        "source": "/document/pages/*"
-        }
-    ],
-    "outputs": [
-        {
-        "name": "embedding",
-        "targetName": "text_vector"
-        }
-    ],
-    "resourceUri": "{{openAIResourceUri}}",
-    "deploymentId": "text-embedding-3-large",
-    "searchApiKey": "{{openAIKey}}",
-    "dimensions": 3072,
-    "modelName": "text-embedding-3-large"
-    },
-    {
-    "@odata.type": "#Microsoft.Skills.Custom.ChatCompletionSkill",
-    "name": "genAI-prompt-skill",
-    "description": "GenAI Prompt skill for image verbalization",
-    "uri": "{{chatCompletionResourceUri}}",
-    "timeout": "PT1M",
-    "searchApiKey": "{{chatCompletionKey}}",
-    "context": "/document/normalized_images/*",
-    "inputs": [
-        {
-        "name": "systemMessage",
-        "source": "='You are tasked with generating concise, accurate descriptions of images, figures, diagrams, or charts in documents. The goal is to capture the key information and meaning conveyed by the image without including extraneous details like style, colors, visual aesthetics, or size.\n\nInstructions:\nContent Focus: Describe the core content and relationships depicted in the image.\n\nFor diagrams, specify the main elements and how they are connected or interact.\nFor charts, highlight key data points, trends, comparisons, or conclusions.\nFor figures or technical illustrations, identify the components and their significance.\nClarity & Precision: Use concise language to ensure clarity and technical accuracy. Avoid subjective or interpretive statements.\n\nAvoid Visual Descriptors: Exclude details about:\n\nColors, shading, and visual styles.\nImage size, layout, or decorative elements.\nFonts, borders, and stylistic embellishments.\nContext: If relevant, relate the image to the broader content of the technical document or the topic it supports.\n\nExample Descriptions:\nDiagram: \"A flowchart showing the four stages of a machine learning pipeline: data collection, preprocessing, model training, and evaluation, with arrows indicating the sequential flow of tasks.\"\n\nChart: \"A bar chart comparing the performance of four algorithms on three datasets, showing that Algorithm A consistently outperforms the others on Dataset 1.\"\n\nFigure: \"A labeled diagram illustrating the components of a transformer model, including the encoder, decoder, self-attention mechanism, and feedforward layers.\"'"
-        },
-        {
-        "name": "userMessage",
-        "source": "='Please describe this image.'"
-        },
-        {
-        "name": "image",
-        "source": "/document/normalized_images/*/data"
-        }
-        ],
-        "outputs": [
-            {
-            "name": "response",
-            "targetName": "verbalizedImage"
-            }
-        ]
-    },    
-    {
-    "@odata.type": "#Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill",
-    "name": "verbalized-image-embedding-skill",
-    "description": "Embedding skill for verbalized images",
-    "context": "/document/normalized_images/*",
-    "inputs": [
-        {
-        "name": "text",
-        "source": "/document/normalized_images/*/verbalizedImage",
-        "inputs": []
-        }
-    ],
-    "outputs": [
-        {
-        "name": "embedding",
-        "targetName": "verbalizedImage_vector"
-        }
-    ],
-    "resourceUri": "{{openAIResourceUri}}",
-    "deploymentId": "text-embedding-3-large",
-    "searchApiKey": "{{openAIKey}}",
-    "dimensions": 3072,
-    "modelName": "text-embedding-3-large"
-    },
-    {
-      "@odata.type": "#Microsoft.Skills.Util.ShaperSkill",
-      "name": "shaper-skill",
-      "description": "Shaper skill to reshape the data to fit the index schema",
-      "context": "/document/normalized_images/*",
-      "inputs": [
-        {
-          "name": "normalized_images",
-          "source": "/document/normalized_images/*",
-          "inputs": []
-        },
-        {
-          "name": "imagePath",
-          "source": "='{{imageProjectionContainer}}/'+$(/document/normalized_images/*/imagePath)",
-          "inputs": []
-        },
-        {
-          "name": "location_metadata",
-          "sourceContext": "/document/normalized_images/*",
-          "inputs": [
-            {
-              "name": "page_number",
-              "source": "/document/normalized_images/*/pageNumber"
-            },
-            {
-              "name": "bounding_polygons",
-              "source": "/document/normalized_images/*/boundingPolygon"
-            }              
-          ]
-        }        
-      ],
-      "outputs": [
-        {
-          "name": "output",
-          "targetName": "new_normalized_images"
-        }
-      ]
-    }      
-  ], 
-   "indexProjections": {
-      "selectors": [
-        {
-          "targetIndexName": "doc-extraction-image-verbalization-index",
-          "parentKeyFieldName": "text_document_id",
-          "sourceContext": "/document/pages/*",
-          "mappings": [    
-            {
-            "name": "content_embedding",
-            "source": "/document/pages/*/text_vector"
-            },                      
-            {
-              "name": "content_text",
-              "source": "/document/pages/*"
-            },             
-            {
-              "name": "document_title",
-              "source": "/document/document_title"
-            }   
-          ]
-        },        
-        {
-          "targetIndexName": "doc-extraction-image-verbalization-index",
-          "parentKeyFieldName": "image_document_id",
-          "sourceContext": "/document/normalized_images/*",
-          "mappings": [    
-            {
-            "name": "content_text",
-            "source": "/document/normalized_images/*/verbalizedImage"
-            },  
-            {
-            "name": "content_embedding",
-            "source": "/document/normalized_images/*/verbalizedImage_vector"
-            },                                           
-            {
-              "name": "content_path",
-              "source": "/document/normalized_images/*/new_normalized_images/imagePath"
-            },                    
-            {
-              "name": "document_title",
-              "source": "/document/document_title"
-            },
-            {
-              "name": "locationMetadata",
-              "source": "/document/normalized_images/*/new_normalized_images/location_metadata"
-            }            
-          ]
-        }
-      ],
-      "parameters": {
-        "projectionMode": "skipIndexingParentDocuments"
-      }
-  },  
-  "knowledgeStore": {
-    "storageConnectionString": "{{storageConnection}}",
-    "identity": null,
-    "projections": [
-      {
-        "files": [
-          {
-            "storageContainer": "{{imageProjectionContainer}}",
-            "source": "/document/normalized_images/*"
-          }
-        ]
-      }
-    ]
-  }
-}
-
-
-```
-
-This skillset extracts text and images, vectorizes both, and shapes the image metadata for projection into the index.
-
-Key points:
-
-+ The `content_text` field is populated in two ways:
-
-  + From document text extracted using the Document Extraction skill and chunked using the Text Split skill
-
-  + From image content using the GenAI Prompt skill, which generates descriptive captions for each normalized image
-  
-+ The `content_embedding` field contains 3072-dimensional embeddings for both page text and verbalized image descriptions. These are generated using the text-embedding-3-large model from Azure OpenAI.
-
-+ `content_path` contains the relative path to the image file within the designated image projection container. This field is generated only for images extracted from PDFs when `imageAction` is set to `generateNormalizedImages`, and can be mapped from the enriched document from the source field `/document/normalized_images/*/imagePath`.
-
-## Create and run an indexer
-
-[Create Indexer](/rest/api/searchservice/indexers/create) creates an indexer on your search service. An indexer connects to the data source, loads data, runs a skillset, and indexes the enriched data.
-
-```http
-### Create and run an indexer
-POST {{searchUrl}}/indexers?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-{
-  "dataSourceName": "doc-extraction-image-verbalization-ds",
-  "targetIndexName": "doc-extraction-image-verbalization-index",
-  "skillsetName": "doc-extraction-image-verbalization-skillset",
-  "parameters": {
-    "maxFailedItems": -1,
-    "maxFailedItemsPerBatch": 0,
-    "batchSize": 1,
-    "configuration": {
-      "allowSkillsetToReadFileData": true
-    }
-  },
-  "fieldMappings": [
-    {
-      "sourceFieldName": "metadata_storage_name",
-      "targetFieldName": "document_title"
-    }
-  ],
-  "outputFieldMappings": []
-}
-```
-
-## Run queries
-
-You can start searching as soon as the first document is loaded.
-
-```http
-### Query the index
-POST {{searchUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-  
-  {
-    "search": "*",
-    "count": true
-  }
-```
-
-Send the request. This is an unspecified full-text search query that returns all of the fields marked as retrievable in the index, along with a document count. The response should look like:
-
-```json
-HTTP/1.1 200 OK
-Transfer-Encoding: chunked
-Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
-Content-Encoding: gzip
-Vary: Accept-Encoding
-Server: Microsoft-IIS/10.0
-Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
-Preference-Applied: odata.include-annotations="*"
-OData-Version: 4.0
-request-id: 712ca003-9493-40f8-a15e-cf719734a805
-elapsed-time: 198
-Date: Wed, 30 Apr 2025 23:20:53 GMT
-Connection: close
-
-{
-  "@odata.count": 100,
-  "@search.nextPageParameters": {
-    "search": "*",
-    "count": true,
-    "skip": 50
-  },
-  "value": [
-  ],
-  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-11-01-preview "
-}
-```
-
-100 documents are returned in the response.
-
-For filters, you can also use Logical operators (and, or, not) and comparison operators (eq, ne, gt, lt, ge, le). String comparisons are case -sensitive. For more information and examples, see [Examples of simple search queries](search-query-simple-examples.md).
-
-> [!NOTE]
-> The `$filter` parameter only works on fields that were marked filterable during index creation.
-
-Here are some examples of other queries:
-
-```http
-### Query for only images
-POST {{searchUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-  
-  {
-    "search": "*",
-    "count": true,
-    "filter": "image_document_id ne null"
-  }
-```
-
-```http
-### Query for text or images with content related to energy, returning the id, parent document, and text (extracted text for text chunks and verbalized image text for images), and the content path where the image is saved in the knowledge store (only populated for images)
-POST {{searchUrl}}/indexes/doc-extraction-image-verbalization-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-  
-  {
-    "search": "energy",
-    "count": true,
-    "select": "content_id, document_title, content_text, content_path"
-  }
-```
-
-## Reset and rerun
-
-Indexers can be reset to clear the high-water mark, which allows a full rerun. The following POST requests are for reset, followed by rerun.
-
-```http
-### Reset the indexer
-POST {{searchUrl}}/indexers/doc-extraction-image-verbalization-indexer/reset?api-version=2025-11-01-preview   HTTP/1.1
-  api-key: {{searchApiKey}}
-```
-
-```http
-### Run the indexer
-POST {{searchUrl}}/indexers/doc-extraction-image-verbalization-indexer/run?api-version=2025-11-01-preview   HTTP/1.1
-  api-key: {{searchApiKey}}
-```
-
-```http
-### Check indexer status 
-GET {{searchUrl}}/indexers/doc-extraction-image-verbalization-indexer/status?api-version=2025-11-01-preview   HTTP/1.1
-  api-key: {{searchApiKey}}
-```
-
-## Clean up resources
-
-When you're working in your own subscription, at the end of a project, it's a good idea to remove the resources that you no longer need. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-You can use the Azure portal to delete indexes, indexers, and data sources.
-
-## See also
-
-Now that you're familiar with a sample implementation of a multimodal indexing scenario, check out:
-
-* [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md)
-* [Vectors in Azure AI Search](vector-search-overview.md)
-* [Semantic ranking in Azure AI Search](semantic-search-overview.md)
-* [Tutorial: Verbalize images from a structured document layout](tutorial-document-layout-image-verbalization.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "画像の言語化に関するチュートリアル記事の削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-document-extraction-image-verbalization.md`ファイルが完全に削除されたことを示しています。このファイルは、Azure AI Searchを使用してPDFドキュメントから画像を抽出し、それを音声化する方法についての詳細なチュートリアルを提供していました。

削除された内容には、ドキュメント抽出スキルを使用して画像とテキストをインデックス化し、生成AIプロンプトスキルを使用して画像の簡潔な説明を生成するプロセスが含まれていました。このチュートリアルは、ユーザーがAzure Blob Storageからのマルチモーダルコンテンツのインデックス作成パイプラインを構築するためのステップバイステップのガイドを提供しており、多くの手順と具体的なコードサンプルが含まれていました。

この削除は、今後のドキュメントのアプローチの変更や、リソースの更新を示唆している可能性があり、ユーザーは新たな情報を求める必要があることを意味します。削除されたチュートリアルによって習得した方法や戦略が他のリソースに移行されたり、更新されたりする可能性があるため、関連するドキュメントを確認することが求められます。

## articles/search/tutorial-document-extraction-multimodal-embeddings.md{#item-a3db59}

<details>
<summary>Diff</summary>
````diff
@@ -1,720 +0,0 @@
----
-title: 'Tutorial: Vectorize images and text'
-titleSuffix: Azure AI Search
-description: Learn how to extract, index, and search multimodal content using the Document Extraction skill for chunking and Azure Vision for embeddings.
-manager: arjagann
-author: mdonovan
-ms.author: mdonovan
-ms.service: azure-ai-search
-ms.update-cycle: 180-days
-ms.custom:
-ms.topic: tutorial
-ms.date: 09/27/2025
-
----
-
-# Tutorial: Vectorize images and text
-
-Azure AI Search can extract and index both text and images from PDF documents stored in Azure Blob Storage. This tutorial shows you how to build a multimodal indexing pipeline in Azure AI Search that *chunks data using the built-in Text Split skill* and *uses multimodal embeddings* to vectorize text and images from the same document. Cropped images are stored in a knowledge store, and both text and visual content are vectorized and ingested in a searchable index.
-
-In this tutorial, you use:
-
-+ A 36-page PDF document that combines rich visual content, such as charts, infographics, and scanned pages, with traditional text.
-
-+ An indexer and skillset to create an indexing pipeline that includes AI enrichment through skills.
-
-+ The [Document Extraction skill](cognitive-search-skill-document-extraction.md) for extracting normalized images and text. The [Text Split skill](cognitive-search-skill-textsplit.md) chunks the data.
-
-+ The [Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) to vectorize text and images.
-
-+ A search index configured to store extracted text and image content. Some content is vectorized for vector-based similarity search.
-
-This tutorial demonstrates a lower-cost approach for indexing multimodal content using the Document Extraction skill. It enables extraction and search over both text and images from documents pulled from Azure Blob Storage. However, it doesn't include locational metadata for text, such as page numbers or bounding regions. For a more comprehensive solution that includes structured text layout and spatial metadata, see [Tutorial: Vectorize from a structured document layout](tutorial-document-layout-multimodal-embeddings.md).
-
-> [!NOTE]
-> Image extraction by the Document Extraction skill isn't free. Setting `imageAction` to `generateNormalizedImages` in the skillset triggers image extraction, which is an extra charge. For billing information, see [Azure AI Search pricing](https://azure.microsoft.com/pricing/details/search/).
-
-## Prerequisites
-
-+ [Microsoft Foundry resource](/azure/ai-services/multi-service-resource). This resource provides access to the Azure Vision multimodal embedding model used in this tutorial. You must use a Foundry resource for skillset access to this resource.
-
-+ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity for connections to Azure Storage and Azure Vision. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier.
-
-+ [Azure Storage](/azure/storage/common/storage-account-create), used for storing sample data and for creating a [knowledge store](knowledge-store-concept-intro.md).
-
-+ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
-
-## Limitations
-
-+ The [Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) has limited regional availability. When you create a Foundry resource, choose a region that provides multimodal embeddings. For an updated list of regions that provide multimodal embeddings, see the [Azure Vision documentation](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
-
-## Prepare data
-
-The following instructions apply to Azure Storage which provides the sample data and also hosts the knowledge store. A search service identity needs read access to Azure Storage to retrieve the sample data, and it needs write access to create the knowledge store. The search service creates the container for cropped images during skillset processing, using the name you provide in an environment variable.
-
-1. Download the following sample PDF: [sustainable-ai-pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Accelerating-Sustainability-with-AI-2025.pdf)
-
-1. In Azure Storage, create a new container named **sustainable-ai-pdf**.
-
-1. [Upload the sample data file](/azure/storage/blobs/storage-quickstart-blobs-portal).
-
-1. [Create role assignments and specify a managed identity in a connection string](search-howto-managed-identities-storage.md):
-
-   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer. Assign **Storage Blob Data Contributor** and **Storage Table Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
-
-   1. For connections made using a system-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
-
-        ```json
-        "credentials" : { 
-            "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-        }
-        ```
-
-   1. For connections made using a user-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. Provide an identity using the syntax shown in the following example. Set userAssignedIdentity to the user-assigned managed identity. The connection string is similar to the following example:
-
-      ```json
-      "credentials" : { 
-          "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-      },
-      "identity" : { 
-          "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
-          "userAssignedIdentity" : "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MY-DEMO-USER-MANAGED-IDENTITY" 
-      }
-      ```
-
-## Prepare models
-
-This tutorial assumes you have an existing Foundry resource through which the skill calls the Azure Vision multimodal 4.0 embedding model. The search service connects to the model during skillset processing using its managed identity. This section gives you guidance and links for assigning roles for authorized access.
-
-1. Sign in to the Azure portal (not the Foundry portal) and find the Foundry resource. Make sure it's in a region that provides the [multimodal 4.0 API](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
-
-1. Select **Access control (IAM)**.
-
-1. Select **Add** and then **Add role assignment**.
-
-1. Search for **Cognitive Services User** and then select it.
-
-1. Choose **Managed identity** and then assign your [search service managed identity](search-how-to-managed-identities.md).
-
-## Set up your REST file
-
-For this tutorial, your local REST client connection to Azure AI Search requires an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Connect to a search service](search-get-started-rbac.md).
-
-For authenticated connections that occur during indexer and skillset processing, the search service uses the role assignments you previously defined.
-
-1. Start Visual Studio Code and create a new file.
-
-1. Provide values for variables used in the request. For `@storageConnection`, make sure your connection string doesn't have a trailing semicolon or quotation marks. For `@imageProjectionContainer`, provide a container name that's unique in blob storage. Azure AI Search creates this container for you during skills processing.
-
-   ```http
-    @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
-    @searchApiKey = PUT-YOUR-ADMIN-API-KEY-HERE
-    @storageConnection = PUT-YOUR-STORAGE-CONNECTION-STRING-HERE
-    @cognitiveServicesUrl = PUT-YOUR-AZURE-AI-FOUNDRY-ENDPOINT-HERE
-    @modelVersion = 2023-04-15
-    @imageProjectionContainer=sustainable-ai-pdf-images
-   ```
-
-1. Save the file using a `.rest` or `.http` file extension. For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
-
-To get the Azure AI Search endpoint and API key:
-
-1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
-
-1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
-
-   :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
-
-## Create a data source
-
-[Create Data Source (REST)](/rest/api/searchservice/data-sources/create) creates a data source connection that specifies what data to index.
-
-```http
-POST {{searchUrl}}/datasources?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-{
-   "name":"doc-extraction-multimodal-embedding-ds",
-   "description":null,
-   "type":"azureblob",
-   "subtype":null,
-   "credentials":{
-      "connectionString":"{{storageConnection}}"
-   },
-   "container":{
-      "name":"sustainable-ai-pdf",
-      "query":null
-   },
-   "dataChangeDetectionPolicy":null,
-   "dataDeletionDetectionPolicy":null,
-   "encryptionKey":null,
-   "identity":null
-}
-```
-
-Send the request. The response should look like:
-
-```json
-HTTP/1.1 201 Created
-Transfer-Encoding: chunked
-Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
-Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-11-01-preview -Preview
-Server: Microsoft-IIS/10.0
-Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
-Preference-Applied: odata.include-annotations="*"
-OData-Version: 4.0
-request-id: 4eb8bcc3-27b5-44af-834e-295ed078e8ed
-elapsed-time: 346
-Date: Sat, 26 Apr 2025 21:25:24 GMT
-Connection: close
-
-{
-  "name": "doc-extraction-multimodal-embedding-ds",
-  "description": null,
-  "type": "azureblob",
-  "subtype": null,
-  "indexerPermissionOptions": [],
-  "credentials": {
-    "connectionString": null
-  },
-  "container": {
-    "name": "sustainable-ai-pdf",
-    "query": null
-  },
-  "dataChangeDetectionPolicy": null,
-  "dataDeletionDetectionPolicy": null,
-  "encryptionKey": null,
-  "identity": null
-}
-```
-
-## Create an index
-
-[Create Index (REST)](/rest/api/searchservice/indexes/create) creates a search index on your search service. An index specifies all the parameters and their attributes.
-
-For nested JSON, the index fields must be identical to the source fields. Currently, Azure AI Search doesn't support field mappings to nested JSON, so field names and data types must match completely. The following index aligns to the JSON elements in the raw content.
-
-```http
-### Create an index
-POST {{searchUrl}}/indexes?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-{
-    "name": "doc-extraction-multimodal-embedding-index",
-    "fields": [
-        {
-            "name": "content_id",
-            "type": "Edm.String",
-            "retrievable": true,
-            "key": true,
-            "analyzer": "keyword"
-        },
-        {
-            "name": "text_document_id",
-            "type": "Edm.String",
-            "searchable": false,
-            "filterable": true,
-            "retrievable": true,
-            "stored": true,
-            "sortable": false,
-            "facetable": false
-        },          
-        {
-            "name": "document_title",
-            "type": "Edm.String",
-            "searchable": true
-        },
-        {
-            "name": "image_document_id",
-            "type": "Edm.String",
-            "filterable": true,
-            "retrievable": true
-        },
-        {
-            "name": "content_text",
-            "type": "Edm.String",
-            "searchable": true,
-            "retrievable": true
-        },
-        {
-            "name": "content_embedding",
-            "type": "Collection(Edm.Single)",
-            "dimensions": 1024,
-            "searchable": true,
-            "retrievable": true,
-            "vectorSearchProfile": "hnsw"
-        },
-        {
-            "name": "content_path",
-            "type": "Edm.String",
-            "searchable": false,
-            "retrievable": true
-        },
-        {
-            "name": "offset",
-            "type": "Edm.String",
-            "searchable": false,
-            "retrievable": true
-        },
-        {
-            "name": "location_metadata",
-            "type": "Edm.ComplexType",
-            "fields": [
-                {
-                "name": "page_number",
-                "type": "Edm.Int32",
-                "searchable": false,
-                "retrievable": true
-                },
-                {
-                "name": "bounding_polygons",
-                "type": "Edm.String",
-                "searchable": false,
-                "retrievable": true,
-                "filterable": false,
-                "sortable": false,
-                "facetable": false
-                }
-            ]
-        }         
-    ],
-    "vectorSearch": {
-        "profiles": [
-            {
-                "name": "hnsw",
-                "algorithm": "defaulthnsw",
-                "vectorizer": "demo-vectorizer"
-            }
-        ],
-        "algorithms": [
-            {
-                "name": "defaulthnsw",
-                "kind": "hnsw",
-                "hnswParameters": {
-                    "m": 4,
-                    "efConstruction": 400,
-                    "metric": "cosine"
-                }
-            }
-        ],
-        "vectorizers": [
-            {
-                "name": "demo-vectorizer",
-                "kind": "aiServicesVision",
-                "aiServicesVisionParameters": {
-                    "resourceUri": "{{cognitiveServicesUrl}}",
-                    "authIdentity": null,
-                    "modelVersion": "{{modelVersion}}"
-                }
-            }
-        ]     
-    },
-    "semantic": {
-        "defaultConfiguration": "semanticconfig",
-        "configurations": [
-            {
-                "name": "semanticconfig",
-                "prioritizedFields": {
-                    "titleField": {
-                        "fieldName": "document_title"
-                    },
-                    "prioritizedContentFields": [
-                    ],
-                    "prioritizedKeywordsFields": []
-                }
-            }
-        ]
-    }
-}
-```
-
-Key points:
-
-+ Text and image embeddings are stored in the `content_embedding` field and must be configured with appropriate dimensions, such as 1024, and a vector search profile.
-
-+ `location_metadata` captures bounding polygon and page number metadata for each normalized image, enabling precise spatial search or UI overlays. `location_metadata` only exists for images in this scenario. If you'd like to capture locational metadata for text as well, consider using [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md). An in-depth tutorial is linked at the bottom of the page.
-
-+ For more information on vector search, see [Vectors in Azure AI Search](vector-search-overview.md).
-
-+ For more information on semantic ranking, see [Semantic ranking in Azure AI Search](semantic-search-overview.md)
-
-## Create a skillset
-
-[Create Skillset (REST)](/rest/api/searchservice/skillsets/create) creates a skillset on your search service. A skillset defines the operations that chunk and embed content prior to indexing. This skillset uses the built-in Document Extraction skill to extract text and images. It uses Text Split skill to chunk large text. It uses Azure Vision multimodal embeddings skill to vectorize image and text content.
-
-```http
-### Create a skillset
-POST {{searchUrl}}/skillsets?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-{
-  "name": "doc-extraction-multimodal-embedding-skillset",
-	"description": "A test skillset",
-  "skills": [
-    {
-      "@odata.type": "#Microsoft.Skills.Util.DocumentExtractionSkill",
-      "name": "document-extraction-skill",
-      "description": "Document extraction skill to extract text and images from documents",
-      "parsingMode": "default",
-      "dataToExtract": "contentAndMetadata",
-      "configuration": {
-          "imageAction": "generateNormalizedImages",
-          "normalizedImageMaxWidth": 2000,
-          "normalizedImageMaxHeight": 2000
-      },
-      "context": "/document",
-      "inputs": [
-        {
-          "name": "file_data",
-          "source": "/document/file_data"
-        }
-      ],
-      "outputs": [
-        {
-          "name": "content",
-          "targetName": "extracted_content"
-        },
-        {
-          "name": "normalized_images",
-          "targetName": "normalized_images"
-        }
-      ]
-    },
-    {
-      "@odata.type": "#Microsoft.Skills.Text.SplitSkill",
-      "name": "split-skill",
-      "description": "Split skill to chunk documents",
-      "context": "/document",
-      "defaultLanguageCode": "en",
-      "textSplitMode": "pages",
-      "maximumPageLength": 2000,
-      "pageOverlapLength": 200,
-      "unit": "characters",
-      "inputs": [
-        {
-          "name": "text",
-          "source": "/document/extracted_content",
-          "inputs": []
-        }
-      ],
-      "outputs": [
-        {
-          "name": "textItems",
-          "targetName": "pages"
-        }
-      ]
-    },  
-  { 
-    "@odata.type": "#Microsoft.Skills.Vision.VectorizeSkill", 
-    "name": "text-embedding-skill",
-    "description": "Vision Vectorization skill for text",
-    "context": "/document/pages/*", 
-    "modelVersion": "{{modelVersion}}", 
-    "inputs": [ 
-      { 
-        "name": "text", 
-        "source": "/document/pages/*" 
-      } 
-    ], 
-    "outputs": [ 
-      { 
-        "name": "vector",
-        "targetName": "text_vector"
-      } 
-    ] 
-  },
-  { 
-    "@odata.type": "#Microsoft.Skills.Vision.VectorizeSkill", 
-    "name": "image-embedding-skill",
-    "description": "Vision Vectorization skill for images",
-    "context": "/document/normalized_images/*", 
-    "modelVersion": "{{modelVersion}}", 
-    "inputs": [ 
-      { 
-        "name": "image", 
-        "source": "/document/normalized_images/*" 
-      } 
-    ], 
-    "outputs": [ 
-      { 
-        "name": "vector",
-  "targetName": "image_vector"
-      } 
-    ] 
-  },  
-    {
-      "@odata.type": "#Microsoft.Skills.Util.ShaperSkill",
-      "name": "shaper-skill",
-      "description": "Shaper skill to reshape the data to fit the index schema",
-      "context": "/document/normalized_images/*",
-      "inputs": [
-        {
-          "name": "normalized_images",
-          "source": "/document/normalized_images/*",
-          "inputs": []
-        },
-        {
-          "name": "imagePath",
-          "source": "='{{imageProjectionContainer}}/'+$(/document/normalized_images/*/imagePath)",
-          "inputs": []
-        },
-        {
-          "name": "dataUri",
-          "source": "='data:image/jpeg;base64,'+$(/document/normalized_images/*/data)",
-          "inputs": []
-        },
-        {
-          "name": "location_metadata",
-          "sourceContext": "/document/normalized_images/*",
-          "inputs": [
-            {
-              "name": "page_number",
-              "source": "/document/normalized_images/*/pageNumber"
-            },
-            {
-              "name": "bounding_polygons",
-              "source": "/document/normalized_images/*/boundingPolygon"
-            }              
-          ]
-        }          
-      ],
-      "outputs": [
-        {
-          "name": "output",
-          "targetName": "new_normalized_images"
-        }
-      ]
-    }  
-  ],
-  "cognitiveServices": {
-    "@odata.type": "#Microsoft.Azure.Search.AIServicesByIdentity",
-    "subdomainUrl": "{{cognitiveServicesUrl}}",
-    "identity": null
-  },
-  "indexProjections": {
-      "selectors": [
-        {
-          "targetIndexName": "doc-extraction-multimodal-embedding-index",
-          "parentKeyFieldName": "text_document_id",
-          "sourceContext": "/document/pages/*",
-          "mappings": [              
-            {
-              "name": "content_embedding",
-              "source": "/document/pages/*/text_vector"
-            },
-            {
-              "name": "content_text",
-              "source": "/document/pages/*"
-            },             
-            {
-              "name": "document_title",
-              "source": "/document/document_title"
-            }      
-          ]
-        },
-        {
-          "targetIndexName": "doc-extraction-multimodal-embedding-index",
-          "parentKeyFieldName": "image_document_id",
-          "sourceContext": "/document/normalized_images/*",
-          "mappings": [                                   
-            {
-              "name": "content_embedding",
-              "source": "/document/normalized_images/*/image_vector"
-            },
-            {
-              "name": "content_path",
-              "source": "/document/normalized_images/*/new_normalized_images/imagePath"
-            },
-            {
-              "name": "location_metadata",
-              "source": "/document/normalized_images/*/new_normalized_images/location_metadata"
-            },                      
-            {
-              "name": "document_title",
-              "source": "/document/document_title"
-            }                
-          ]
-        }
-      ],
-      "parameters": {
-        "projectionMode": "skipIndexingParentDocuments"
-      }
-  },
-  "knowledgeStore": {
-    "storageConnectionString": "{{storageConnection}}",
-    "identity": null,
-    "projections": [
-      {
-        "files": [
-          {
-            "storageContainer": "{{imageProjectionContainer}}",
-            "source": "/document/normalized_images/*"
-          }
-        ]
-      }
-    ]
-  }
-}
-```
-
-This skillset extracts text and images, vectorizes both, and shapes the image metadata for projection into the index.
-
-Key points:
-
-+ The `content_text` field is populated with text extracted using the Document Extraction Skill and chunked using the Split Skill
-
-+ `content_path` contains the relative path to the image file within the designated image projection container. This field is generated only for images extracted from PDFs when `imageAction` is set to `generateNormalizedImages`, and can be mapped from the enriched document from the source field `/document/normalized_images/*/imagePath`.
-
-+ The Azure Vision multimodal embeddings skill enables embedding of both textual and visual data using the same skill type, differentiated by input (text vs image). For more information, see [Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md).
-
-## Create and run an indexer
-
-[Create Indexer](/rest/api/searchservice/indexers/create) creates an indexer on your search service. An indexer connects to the data source, loads data, runs a skillset, and indexes the enriched data.
-
-```http
-### Create and run an indexer
-POST {{searchUrl}}/indexers?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-{
-  "name": "doc-extraction-multimodal-embedding-indexer",
-  "dataSourceName": "doc-extraction-multimodal-embedding-ds",
-  "targetIndexName": "doc-extraction-multimodal-embedding-index",
-  "skillsetName": "doc-extraction-multimodal-embedding-skillset",
-  "parameters": {
-    "maxFailedItems": -1,
-    "maxFailedItemsPerBatch": 0,
-    "batchSize": 1,
-    "configuration": {
-      "allowSkillsetToReadFileData": true
-    }
-  },
-  "fieldMappings": [
-    {
-      "sourceFieldName": "metadata_storage_name",
-      "targetFieldName": "document_title"
-    }
-  ],
-  "outputFieldMappings": []
-}
-```
-
-## Run queries
-
-You can start searching as soon as the first document is loaded.
-
-```http
-### Query the index
-POST {{searchUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-  
-  {
-    "search": "*",
-    "count": true
-  }
-```
-
-Send the request. This is an unspecified full-text search query that returns all of the fields marked as retrievable in the index, along with a document count. The response should look like:
-
-```json
-HTTP/1.1 200 OK
-Transfer-Encoding: chunked
-Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
-Content-Encoding: gzip
-Vary: Accept-Encoding
-Server: Microsoft-IIS/10.0
-Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
-Preference-Applied: odata.include-annotations="*"
-OData-Version: 4.0
-request-id: 712ca003-9493-40f8-a15e-cf719734a805
-elapsed-time: 198
-Date: Wed, 30 Apr 2025 23:20:53 GMT
-Connection: close
-
-{
-  "@odata.count": 100,
-  "@search.nextPageParameters": {
-    "search": "*",
-    "count": true,
-    "skip": 50
-  },
-  "value": [
-  ],
-  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-11-01-preview "
-}
-```
-100 documents are returned in the response.
-
-For filters, you can also use Logical operators (and, or, not) and comparison operators (eq, ne, gt, lt, ge, le). String comparisons are case-sensitive. For more information and examples, see [Examples of simple search queries](search-query-simple-examples.md).
-
-> [!NOTE]
-> The `$filter` parameter only works on fields that were marked filterable during index creation.
-
-```http
-### Query for only images
-POST {{searchUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-  
-  {
-    "search": "*",
-    "count": true,
-    "filter": "image_document_id ne null"
-  }
-```
-
-```http
-### Query for text or images with content related to energy, returning the id, parent document, and text (only populated for text chunks), and the content path where the image is saved in the knowledge store (only populated for images)
-POST {{searchUrl}}/indexes/doc-extraction-multimodal-embedding-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-  
-
-  {
-    "search": "energy",
-    "count": true,
-    "select": "content_id, document_title, content_text, content_path"
-  }
-```
-
-## Reset and rerun
-
-Indexers can be reset to clear the high-water mark, which allows a full rerun. The following POST requests are for reset, followed by rerun.
-
-```http
-### Reset the indexer
-POST {{searchUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/reset?api-version=2025-11-01-preview   HTTP/1.1
-  api-key: {{searchApiKey}}
-```
-
-```http
-### Run the indexer
-POST {{searchUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/run?api-version=2025-11-01-preview   HTTP/1.1
-  api-key: {{searchApiKey}}
-```
-
-```http
-### Check indexer status 
-GET {{searchUrl}}/indexers/doc-extraction-multimodal-embedding-indexer/status?api-version=2025-11-01-preview   HTTP/1.1
-  api-key: {{searchApiKey}}
-```
-
-## Clean up resources
-
-When you're working in your own subscription, at the end of a project, it's a good idea to remove the resources that you no longer need. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-You can use the Azure portal to delete indexes, indexers, and data sources.
-
-## See also
-
-Now that you're familiar with a sample implementation of a multimodal indexing scenario, check out:
-
-* [Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md)
-* [Vectors in Azure AI Search](vector-search-overview.md)
-* [Semantic ranking in Azure AI Search](semantic-search-overview.md)
-* [Tutorial: Verbalize images from a structured document layout](tutorial-document-layout-image-verbalization.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "マルチモーダル埋め込みに関するチュートリアル記事の削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-document-extraction-multimodal-embeddings.md`ファイルが完全に削除されたことを示しています。このチュートリアルは、Azure AI Searchを使用してPDFドキュメントから画像とテキストを抽出し、それらをベクター化する方法について詳しく説明していました。

削除された内容には、ドキュメント抽出スキルを用いたデータのチャンク化や、Azure Visionを利用したマルチモーダル埋め込みによる画像とテキストのベクター化の手順が含まれていました。具体的な手続きや必要な準備、データソースの作成、インデックスの生成、クエリの実行方法などが詳細に記載されており、ユーザーが直接利用できる実践的なリソースでした。

この削除は、現在のドキュメントやリソースの組織の変更、またはその内容が新たに更新される可能性を示唆しています。直接的な代替手段として他のチュートリアルやリソースを探す必要があるため、ユーザーは関連する文書を確認し、最新の情報を得ることが重要です。

## articles/search/tutorial-document-layout-image-verbalization.md{#item-f5de57}

<details>
<summary>Diff</summary>
````diff
@@ -1,740 +0,0 @@
----
-title: 'Tutorial: Verbalize images from a structured document layout'
-titleSuffix: Azure AI Search
-description: Learn how to extract, index, and search multimodal content using the Document Layout skill for chunking and GenAI Prompt skill for image verbalizations.
-manager: arjagann
-author: rawan    
-ms.author: rawan
-ms.service: azure-ai-search
-ms.update-cycle: 180-days
-ms.custom:
-ms.topic: tutorial
-ms.date: 09/27/2025
-
----
-
-# Tutorial: Verbalize images from a structured document layout
-
-Azure AI Search can extract and index both text and images from PDF documents stored in Azure Blob Storage. This tutorial shows you how to build a multimodal indexing pipeline that *chunks data based on document structure* and uses *image verbalization* to describe images. Cropped images are stored in a knowledge store, and visual content is described in natural language and ingested alongside text in a searchable index. Chunking is based on the [Azure Document Intelligence in Foundry Tools layout model](/azure/ai-services/document-intelligence/concept-layout) that recognizes document structure.
-
-To get image verbalizations, each extracted image is passed to the [GenAI Prompt skill (preview)](cognitive-search-skill-genai-prompt.md) that calls a chat completion model to generate a concise textual description. These descriptions, along with the original document text, are then embedded into vector representations using Azure OpenAI’s text-embedding-3-large model. The result is a single index containing searchable content from both modalities: text and verbalized images.
-
-In this tutorial, you use:
-
-+ A 36-page PDF document that combines rich visual content, such as charts, infographics, and scanned pages, with traditional text.
-
-+ An indexer and skillset to create an indexing pipeline that includes AI enrichment through skills.
-
-+ The [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) for extracting text and normalized images with its `locationMetadata` from various documents, such as page numbers or bounding regions.
-
-+ The [GenAI Prompt skill (preview)](cognitive-search-skill-genai-prompt.md) that calls a chat completion model to create descriptions of visual content.
-
-+ A search index configured to store extracted text and image verbalizations. Some content is vectorized for vector-based similarity search.
-
-## Prerequisites
-
-+ [Microsoft Foundry resource](/azure/ai-services/multi-service-resource). This resource provides access to the Azure Document Intelligence Layout model used in this tutorial. You must use a Foundry resource for skillset access to this resource.
-
-+ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier.
-
-+ [Azure Storage](/azure/storage/common/storage-account-create), used for storing sample data and for creating a [knowledge store](knowledge-store-concept-intro.md).
-
-+ [Azure OpenAI](/azure/ai-foundry/openai/how-to/create-resource) with a deployment of
-
-  + A chat completion model hosted in Foundry or another source. The model is used to verbalize image content. You provide the URI to the hosted model in the GenAI Prompt skill definition. You can use [any chat completion model](cognitive-search-skill-genai-prompt.md#supported-models).
-
-  + A text embedding model deployed in Foundry. The model is used to vectorize text content pull from source documents and the image descriptions generated by the chat completion model. For integrated vectorization, the embedding model must be located in Foundry, and it must be either text-embedding-ada-002, text-embedding-3-large, or text-embedding-3-small. If you want to use an external embedding model, use a custom skill instead of the Azure OpenAI embedding skill.
-
-+ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
-
-## Limitations
-
-+ The [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) has limited regional availability. For a list of supported regions, see [Document Layout skill> Supported regions](cognitive-search-skill-document-intelligence-layout.md#supported-regions).
-
-## Prepare data
-
-The following instructions apply to Azure Storage which provides the sample data and also hosts the knowledge store. A search service identity needs read access to Azure Storage to retrieve the sample data, and it needs write access to create the knowledge store. The search service creates the container for cropped images during skillset processing, using the name you provide in an environment variable.
-
-1. Download the following sample PDF: [sustainable-ai-pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Accelerating-Sustainability-with-AI-2025.pdf)
-
-1. In Azure Storage, create a new container named **sustainable-ai-pdf**.
-
-1. [Upload the sample data file](/azure/storage/blobs/storage-quickstart-blobs-portal).
-
-1. [Create role assignments and specify a managed identity in a connection string](search-howto-managed-identities-storage.md):
-
-   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer. Assign **Storage Blob Data Contributor** and **Storage Table Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
-
-   1. For connections made using a system-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
-
-        ```json
-        "credentials" : { 
-            "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-        }
-        ```
-
-   1. For connections made using a user-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. Provide an identity using the syntax shown in the following example. Set userAssignedIdentity to the user-assigned managed identity The connection string is similar to the following example:
-
-      ```json
-      "credentials" : { 
-          "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-      },
-      "identity" : { 
-          "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
-          "userAssignedIdentity" : "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MY-DEMO-USER-MANAGED-IDENTITY" 
-      }
-      ```
-
-## Prepare models
-
-This tutorial assumes you have an existing Azure OpenAI resource through which the skills a chat completion model for GenAI Prompt and also a text embedding model for vectorization. The search service connects to the models during skillset processing and during query execution using its managed identity. This section gives you guidance and links for assigning roles for authorized access.
-
-You also need a role assignment for accessing the Azure Document Intelligence layout model via a Foundry resource.
-
-### Assign roles in Foundry
-
-1. Sign in to the Azure portal (not the Foundry portal) and find the Foundry resource. Make sure it's in a region that provides the [Azure Document Intelligence layout model](cognitive-search-skill-document-intelligence-layout.md#supported-regions).
-
-1. Select **Access control (IAM)**.
-
-1. Select **Add** and then **Add role assignment**.
-
-1. Search for **Cognitive Services User** and then select it.
-
-1. Choose **Managed identity** and then assign your [search service managed identity](search-how-to-managed-identities.md).
-
-### Assign roles in Azure OpenAI
-
-1. Sign in to the Azure portal (not the Foundry portal) and find the Azure OpenAI resource.
-
-1. Select **Access control (IAM)**.
-
-1. Select **Add** and then **Add role assignment**.
-
-1. Search for **Cognitive Services OpenAI User** and then select it.
-
-1. Choose **Managed identity** and then assign your [search service managed identity](search-how-to-managed-identities.md).
-
-For more information, see [Role-based access control for Azure OpenAI in Foundry Models](/azure/ai-foundry/openai/how-to/role-based-access-control).
-
-## Set up your REST file
-
-For this tutorial, your local REST client connection to Azure AI Search requires an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Connect to a search service](search-get-started-rbac.md).
-
-For authenticated connections that occur during indexer and skillset processing, the search service uses the role assignments you previously defined.
-
-1. Start Visual Studio Code and create a new file.
-
-1. Provide values for variables used in the request. For `@storageConnection`, make sure your connection string doesn't have a trailing semicolon or quotation marks. For `@imageProjectionContainer`, provide a container name that's unique in blob storage. Azure AI Search creates this container for you during skills processing.
-
-   ```http
-   @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
-   @searchApiKey = PUT-YOUR-ADMIN-API-KEY-HERE
-   @storageConnection = PUT-YOUR-STORAGE-CONNECTION-STRING-HERE
-   @cognitiveServicesUrl = PUT-YOUR-AZURE-AI-FOUNDRY-ENDPOINT-HERE
-   @openAIResourceUri = PUT-YOUR-OPENAI-URI-HERE
-   @openAIKey = PUT-YOUR-OPENAI-KEY-HERE
-   @chatCompletionResourceUri = PUT-YOUR-CHAT-COMPLETION-URI-HERE
-   @chatCompletionKey = PUT-YOUR-CHAT-COMPLETION-KEY-HERE
-   @imageProjectionContainer=sustainable-ai-pdf-images
-   ```
-
-1. Save the file using a `.rest` or `.http` file extension. For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
-
-To get the Azure AI Search endpoint and API key:
-
-1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
-
-1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
-
-   :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
-
-## Create a data source
-
-[Create Data Source (REST)](/rest/api/searchservice/data-sources/create) creates a data source connection that specifies what data to index.
-
-```http
-### Create a data source using system-assigned managed identities
-POST {{searchUrl}}/datasources?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-  {
-    "name": "doc-intelligence-image-verbalization-ds",
-    "description": "A data source to store multi-modality documents",
-    "type": "azureblob",
-    "subtype": null,
-    "credentials":{
-      "connectionString":"{{storageConnection}}"
-    },
-    "container": {
-      "name": "sustainable-ai-pdf",
-      "query": null
-    },
-    "dataChangeDetectionPolicy": null,
-    "dataDeletionDetectionPolicy": null,
-    "encryptionKey": null,
-    "identity": null
-  }
-
-```
-
-Send the request. The response should look like:
-
-```json
-HTTP/1.1 201 Created
-Transfer-Encoding: chunked
-Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
-Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-11-01-preview -Preview
-Server: Microsoft-IIS/10.0
-Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
-Preference-Applied: odata.include-annotations="*"
-OData-Version: 4.0
-request-id: 4eb8bcc3-27b5-44af-834e-295ed078e8ed
-elapsed-time: 346
-Date: Sat, 26 Apr 2025 21:25:24 GMT
-Connection: close
-
-{
-  "name": "doc-extraction-multimodal-embedding-ds",
-  "description": null,
-  "type": "azureblob",
-  "subtype": null,
-  "indexerPermissionOptions": [],
-  "credentials": {
-    "connectionString": null
-  },
-  "container": {
-    "name": "sustainable-ai-pdf",
-    "query": null
-  },
-  "dataChangeDetectionPolicy": null,
-  "dataDeletionDetectionPolicy": null,
-  "encryptionKey": null,
-  "identity": null
-}
-```
-
-## Create an index
-
-[Create Index (REST)](/rest/api/searchservice/indexes/create) creates a search index on your search service. An index specifies all the parameters and their attributes.
-
-For nested JSON, the index fields must be identical to the source fields. Currently, Azure AI Search doesn't support field mappings to nested JSON, so field names and data types must match completely. The following index aligns to the JSON elements in the raw content.
-
-```http
-### Create an index
-POST {{searchUrl}}/indexes?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-{
-    "name": "doc-intelligence-image-verbalization-index",
-    "fields": [
-        {
-            "name": "content_id",
-            "type": "Edm.String",
-            "retrievable": true,
-            "key": true,
-            "analyzer": "keyword"
-        },
-        {
-            "name": "text_document_id",
-            "type": "Edm.String",
-            "searchable": false,
-            "filterable": true,
-            "retrievable": true,
-            "stored": true,
-            "sortable": false,
-            "facetable": false
-        },          
-        {
-            "name": "document_title",
-            "type": "Edm.String",
-            "searchable": true
-        },
-        {
-            "name": "image_document_id",
-            "type": "Edm.String",
-            "filterable": true,
-            "retrievable": true
-        },
-        {
-            "name": "content_text",
-            "type": "Edm.String",
-            "searchable": true,
-            "retrievable": true
-        },
-        {
-            "name": "content_embedding",
-            "type": "Collection(Edm.Single)",
-            "dimensions": 3072,
-            "searchable": true,
-            "retrievable": true,
-            "vectorSearchProfile": "hnsw"
-        },
-        {
-            "name": "content_path",
-            "type": "Edm.String",
-            "searchable": false,
-            "retrievable": true
-        },
-        {
-            "name": "offset",
-            "type": "Edm.String",
-            "searchable": false,
-            "retrievable": true
-        },
-        {
-            "name": "location_metadata",
-            "type": "Edm.ComplexType",
-            "fields": [
-                {
-                "name": "page_number",
-                "type": "Edm.Int32",
-                "searchable": false,
-                "retrievable": true
-                },
-                {
-                "name": "bounding_polygons",
-                "type": "Edm.String",
-                "searchable": false,
-                "retrievable": true,
-                "filterable": false,
-                "sortable": false,
-                "facetable": false
-                }
-            ]
-        }         
-    ],
-    "vectorSearch": {
-        "profiles": [
-            {
-                "name": "hnsw",
-                "algorithm": "defaulthnsw",
-                "vectorizer": "demo-vectorizer"
-            }
-        ],
-        "algorithms": [
-            {
-                "name": "defaulthnsw",
-                "kind": "hnsw",
-                "hnswParameters": {
-                    "m": 4,
-                    "efConstruction": 400,
-                    "metric": "cosine"
-                }
-            }
-        ],
-        "vectorizers": [
-            {
-              "name": "demo-vectorizer",
-              "kind": "azureOpenAI",    
-              "azureOpenAIParameters": {
-                "resourceUri": "{{openAIResourceUri}}",
-                "deploymentId": "text-embedding-3-large",
-                "apiKey": "{{openAIKey}}",
-                "modelName": "text-embedding-3-large"
-              }
-            }
-        ]
-    },
-    "semantic": {
-        "defaultConfiguration": "semanticconfig",
-        "configurations": [
-            {
-                "name": "semanticconfig",
-                "prioritizedFields": {
-                    "titleField": {
-                        "fieldName": "document_title"
-                    },
-                    "prioritizedContentFields": [
-                    ],
-                    "prioritizedKeywordsFields": []
-                }
-            }
-        ]
-    }
-}
-```
-
-Key points:
-
-+ Text and image embeddings are stored in the `content_embedding` field and must be configured with appropriate dimensions, such as 3072, and a vector search profile.
-
-+ `location_metadata` captures bounding polygon and page number metadata for each text chunk and normalized image, enabling precise spatial search or UI overlays.
-
-+ For more information on vector search, see [Vectors in Azure AI Search](vector-search-overview.md).
-
-+ For more information on semantic ranking, see [Semantic ranking in Azure AI Search](semantic-search-overview.md)
-
-## Create a skillset
-
-[Create Skillset (REST)](/rest/api/searchservice/skillsets/create) creates a skillset on your search service. A skillset defines the operations that chunk and embed content prior to indexing. This skillset uses the Document Layout skill to extract text and images, preserving location metadata which is useful for citations in RAG applications. It uses Azure OpenAI Embedding skill to vectorize text content.
-
-The skillset also performs actions specific to images. It uses the GenAI Prompt skill to generate image descriptions. It also creates a knowledge store that stores intact images so that you can return them in a query.
-
-
-```http
-### Create a skillset
-POST {{searchUrl}}/skillsets?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-{
-  "name": "doc-intelligence-image-verbalization-skillset",
-  "description": "A sample skillset for multi-modality using image verbalization",
-  "skills": [
-    {
-      "@odata.type": "#Microsoft.Skills.Util.DocumentIntelligenceLayoutSkill",
-      "name": "document-cracking-skill",
-      "description": "Document Layout skill for document cracking",
-      "context": "/document",
-      "outputMode": "oneToMany",
-      "outputFormat": "text",
-      "extractionOptions": ["images", "locationMetadata"],
-      "chunkingProperties": {     
-          "unit": "characters",
-          "maximumLength": 2000, 
-          "overlapLength": 200
-      },
-      "inputs": [
-        {
-          "name": "file_data",
-          "source": "/document/file_data"
-        }
-      ],
-      "outputs": [
-        { 
-          "name": "text_sections", 
-          "targetName": "text_sections" 
-        }, 
-        { 
-          "name": "normalized_images", 
-          "targetName": "normalized_images" 
-        } 
-      ]
-    },
-    {
-    "@odata.type": "#Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill",
-    "name": "text-embedding-skill",
-    "description": "Azure Open AI Embedding skill for text",
-    "context": "/document/text_sections/*",
-    "inputs": [
-        {
-        "name": "text",
-        "source": "/document/text_sections/*/content"
-        }
-    ],
-    "outputs": [
-        {
-        "name": "embedding",
-        "targetName": "text_vector"
-        }
-    ],
-    "resourceUri": "{{openAIResourceUri}}",
-    "deploymentId": "text-embedding-3-large",
-    "apiKey": "{{openAIKey}}",
-    "dimensions": 3072,
-    "modelName": "text-embedding-3-large"
-    },
-    {
-    "@odata.type": "#Microsoft.Skills.Custom.ChatCompletionSkill",
-    "uri": "{{chatCompletionResourceUri}}",
-    "timeout": "PT1M",
-    "apiKey": "{{chatCompletionKey}}",
-    "name": "genAI-prompt-skill",
-    "description": "GenAI Prompt skill for image verbalization",
-    "context": "/document/normalized_images/*",
-    "inputs": [
-        {
-        "name": "systemMessage",
-        "source": "='You are tasked with generating concise, accurate descriptions of images, figures, diagrams, or charts in documents. The goal is to capture the key information and meaning conveyed by the image without including extraneous details like style, colors, visual aesthetics, or size.\n\nInstructions:\nContent Focus: Describe the core content and relationships depicted in the image.\n\nFor diagrams, specify the main elements and how they are connected or interact.\nFor charts, highlight key data points, trends, comparisons, or conclusions.\nFor figures or technical illustrations, identify the components and their significance.\nClarity & Precision: Use concise language to ensure clarity and technical accuracy. Avoid subjective or interpretive statements.\n\nAvoid Visual Descriptors: Exclude details about:\n\nColors, shading, and visual styles.\nImage size, layout, or decorative elements.\nFonts, borders, and stylistic embellishments.\nContext: If relevant, relate the image to the broader content of the technical document or the topic it supports.\n\nExample Descriptions:\nDiagram: \"A flowchart showing the four stages of a machine learning pipeline: data collection, preprocessing, model training, and evaluation, with arrows indicating the sequential flow of tasks.\"\n\nChart: \"A bar chart comparing the performance of four algorithms on three datasets, showing that Algorithm A consistently outperforms the others on Dataset 1.\"\n\nFigure: \"A labeled diagram illustrating the components of a transformer model, including the encoder, decoder, self-attention mechanism, and feedforward layers.\"'"
-        },
-        {
-        "name": "userMessage",
-        "source": "='Please describe this image.'"
-        },
-        {
-        "name": "image",
-        "source": "/document/normalized_images/*/data"
-        }
-        ],
-        "outputs": [
-            {
-            "name": "response",
-            "targetName": "verbalizedImage"
-            }
-        ]
-    },    
-    {
-    "@odata.type": "#Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill",
-    "name": "verbalizedImage-embedding-skill",
-    "description": "Azure Open AI Embedding skill for verbalized image embedding",
-    "context": "/document/normalized_images/*",
-    "inputs": [
-        {
-        "name": "text",
-        "source": "/document/normalized_images/*/verbalizedImage",
-        "inputs": []
-        }
-    ],
-    "outputs": [
-        {
-        "name": "embedding",
-        "targetName": "verbalizedImage_vector"
-        }
-    ],
-    "resourceUri": "{{openAIResourceUri}}",
-    "deploymentId": "text-embedding-3-large",
-    "apiKey": "{{openAIKey}}",
-    "dimensions": 3072,
-    "modelName": "text-embedding-3-large"
-    },
-    {
-      "@odata.type": "#Microsoft.Skills.Util.ShaperSkill",
-      "name": "#5",
-      "context": "/document/normalized_images/*",
-      "inputs": [
-        {
-          "name": "normalized_images",
-          "source": "/document/normalized_images/*",
-          "inputs": []
-        },
-        {
-          "name": "imagePath",
-          "source": "='my_container_name/'+$(/document/normalized_images/*/imagePath)",
-          "inputs": []
-        }
-      ],
-      "outputs": [
-        {
-          "name": "output",
-          "targetName": "new_normalized_images"
-        }
-      ]
-    }      
-  ], 
-   "indexProjections": {
-      "selectors": [
-        {
-          "targetIndexName": "doc-intelligence-image-verbalization-index",
-          "parentKeyFieldName": "text_document_id",
-          "sourceContext": "/document/text_sections/*",
-          "mappings": [    
-            {
-            "name": "content_embedding",
-            "source": "/document/text_sections/*/text_vector"
-            },                      
-            {
-              "name": "content_text",
-              "source": "/document/text_sections/*/content"
-            },
-            {
-              "name": "location_metadata",
-              "source": "/document/text_sections/*/locationMetadata"
-            },                
-            {
-              "name": "document_title",
-              "source": "/document/document_title"
-            }   
-          ]
-        },        
-        {
-          "targetIndexName": "doc-intelligence-image-verbalization-index",
-          "parentKeyFieldName": "image_document_id",
-          "sourceContext": "/document/normalized_images/*",
-          "mappings": [    
-            {
-            "name": "content_text",
-            "source": "/document/normalized_images/*/verbalizedImage"
-            },  
-            {
-            "name": "content_embedding",
-            "source": "/document/normalized_images/*/verbalizedImage_vector"
-            },                                           
-            {
-              "name": "content_path",
-              "source": "/document/normalized_images/*/new_normalized_images/imagePath"
-            },                    
-            {
-              "name": "document_title",
-              "source": "/document/document_title"
-            },
-            {
-              "name": "location_metadata",
-              "source": "/document/normalized_images/*/locationMetadata"
-            }             
-          ]
-        }
-      ],
-      "parameters": {
-        "projectionMode": "skipIndexingParentDocuments"
-      }
-  },  
-  "knowledgeStore": {
-    "storageConnectionString": "{{storageConnection}}",
-    "identity": null,
-    "projections": [
-      {
-        "files": [
-          {
-            "storageContainer": "{{imageProjectionContainer}}",
-            "source": "/document/normalized_images/*"
-          }
-        ]
-      }
-    ]
-  }
-}
-
-```
-
-This skillset extracts text and images, verbalizes images, and shapes the image metadata for projection into the index.
-
-Key points:
-
-+ The `content_text` field is populated in two ways:
-
-  + From document text extracted and chunked using the Document Layout skill.
-
-  + From image content using the GenAI Prompt skill, which generates descriptive captions for each normalized image
-  
-+ The `content_embedding` field contains 3072-dimensional embeddings for both page text and verbalized image descriptions. These are generated using the text-embedding-3-large model from Azure OpenAI.
-
-+ `content_path` contains the relative path to the image file within the designated image projection container. This field is generated only for images extracted from documents when `extractOption` is set to `["images", "locationMetadata"]` or `["images"]`, and can be mapped from the enriched document from the source field `/document/normalized_images/*/imagePath`.
-
-+ The Azure OpenAI embeddings skill enables embedding of textual data. For more information, see [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md).
-
-## Create and run an indexer
-
-[Create Indexer](/rest/api/searchservice/indexers/create) creates an indexer on your search service. An indexer connects to the data source, loads data, runs a skillset, and indexes the enriched data.
-
-```http
-### Create and run an indexer
-POST {{searchUrl}}/indexers?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-{
-  "dataSourceName": "doc-intelligence-image-verbalization-ds",
-  "targetIndexName": "doc-intelligence-image-verbalization-index",
-  "skillsetName": "doc-intelligence-image-verbalization-skillset",
-  "parameters": {
-    "maxFailedItems": -1,
-    "maxFailedItemsPerBatch": 0,
-    "batchSize": 1,
-    "configuration": {
-      "allowSkillsetToReadFileData": true
-    }
-  },
-  "fieldMappings": [
-    {
-      "sourceFieldName": "metadata_storage_name",
-      "targetFieldName": "document_title"
-    }
-  ],
-  "outputFieldMappings": []
-}
-```
-
-## Run queries
-
-You can start searching as soon as the first document is loaded.
-
-```http
-### Query the index
-POST {{searchUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-  
-  {
-    "search": "*",
-    "count": true
-  }
-```
-
-Send the request. This is an unspecified full-text search query that returns all of the fields marked as retrievable in the index, along with a document count. The response should look like:
-
-```json
-{
-  "@odata.count": 100,
-  "@search.nextPageParameters": {
-    "search": "*",
-    "count": true,
-    "skip": 50
-  },
-  "value": [
-  ],
-  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-11-01-preview "
-}
-```
-100 documents are returned in the response.
-
-For filters, you can also use Logical operators (and, or, not) and comparison operators (eq, ne, gt, lt, ge, le). String comparisons are case -sensitive. For more information and examples, see [Examples of simple search queries](search-query-simple-examples.md).
-
-> [!NOTE]
-> The `$filter` parameter only works on fields that were marked filterable during index creation.
-
-```http
-### Query for only images
-POST {{searchUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-  
-  {
-    "search": "*",
-    "count": true,
-    "filter": "image_document_id ne null"
-  }
-```
-
-```http
-### Query for text or images with content related to energy, returning the id, parent document, and text (only populated for text chunks), and the content path where the image is saved in the knowledge store (only populated for images)
-POST {{searchUrl}}/indexes/doc-intelligence-image-verbalization-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-  
-  {
-    "search": "energy",
-    "count": true,
-    "select": "content_id, document_title, content_text, content_path"
-  }
-```
-
-## Reset and rerun
-
-Indexers can be reset to clear execution history, which allows a full rerun. The following POST requests are for reset, followed by rerun.
-
-```http
-### Reset the indexer
-POST {{searchUrl}}/indexers/doc-intelligence-image-verbalization-indexer/reset?api-version=2025-11-01-preview   HTTP/1.1
-  api-key: {{searchApiKey}}
-```
-
-```http
-### Run the indexer
-POST {{searchUrl}}/indexers/doc-intelligence-image-verbalization-indexer/run?api-version=2025-11-01-preview   HTTP/1.1
-  api-key: {{searchApiKey}}
-```
-
-```http
-### Check indexer status 
-GET {{searchUrl}}/indexers/doc-intelligence-image-verbalization-indexer/status?api-version=2025-11-01-preview   HTTP/1.1
-  api-key: {{searchApiKey}}
-```
-
-## Clean up resources
-
-When you're working in your own subscription, at the end of a project, it's a good idea to remove the resources that you no longer need. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-You can use the Azure portal to delete indexes, indexers, and data sources.
-
-## See also
-
-Now that you're familiar with a sample implementation of a multimodal indexing scenario, check out:
-
-+ [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md)
-+ [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md)
-+ [Azure OpenAI Embedding skill](cognitive-search-skill-azure-openai-embedding.md)
-+ [Vectors in Azure AI Search](vector-search-overview.md)
-+ [Semantic ranking in Azure AI Search](semantic-search-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "構造化ドキュメントレイアウトからの画像音声化チュートリアルの削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-document-layout-image-verbalization.md`ファイルが完全に削除されたことを示しています。このチュートリアルは、Azure AI Searchを使用してPDFドキュメントから画像を抽出し、それに基づいて画像の音声化を行う方法についての洞察を提供していました。

削除された内容には、文書の構造に基づいたデータのチャンク化や、各画像をGenAIプロンプトスキルに渡してテキスト説明を生成するプロセスに関する詳細なステップが含まれていました。このチュートリアルは、ユーザーが複雑な多様性のあるドキュメントを扱う際の手法を学ぶための実用的なガイドとなっていました。

この削除は、新しい情報や方法論への移行を示唆している可能性があり、ユーザーは代わりとなるリソースやドキュメントを探す必要があります。利用可能な最新のコンテンツを確認することで、引き続きAzure AI Searchの機能を効果的に利用できるようになります。

## articles/search/tutorial-document-layout-multimodal-embeddings.md{#item-f67371}

<details>
<summary>Diff</summary>
````diff
@@ -1,666 +0,0 @@
----
-title: 'Tutorial: Vectorize from a structured document layout'
-titleSuffix: Azure AI Search
-description: Learn how to extract, index, and search multimodal content using the Document Layout skill for chunking and Azure Vision for embeddings.
-manager: arjagann
-author: rawan
-ms.author: rawan
-ms.service: azure-ai-search
-ms.update-cycle: 180-days
-ms.custom:
-ms.topic: tutorial
-ms.date: 09/27/2025
-
----
-
-# Tutorial: Vectorize from a structured document layout
-
-Azure AI Search can extract and index both text and images from PDF documents stored in Azure Blob Storage. This tutorial shows you how to build a multimodal indexing pipeline that *chunks data based on document structure* and *uses multimodal embeddings* to vectorize text and images from the same document. Cropped images are stored in a knowledge store, and both text and visual content are vectorized and ingested in a searchable index. Chunking is based on the [Azure Document Intelligence in Foundry Tools layout model](/azure/ai-services/document-intelligence/concept-layout) that recognizes document structure.
-
-In this tutorial, you use:
-
-+ A 36-page PDF document that combines rich visual content, such as charts, infographics, and scanned pages, with traditional text.
-
-+ An indexer and skillset to create an indexing pipeline that includes AI enrichment through skills.
-
-+ The [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) for extracting text and normalized images with its `locationMetadata` from various documents, such as page numbers or bounding regions.
-
-+ The [Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) to vectorize text and images.
-
-+ A search index configured to store extracted text and image content. Some content is vectorized for vector-based similarity search.
-
-## Prerequisites
-
-+ [Microsoft Foundry resource](/azure/ai-services/multi-service-resource). This resource provides access to both the Azure Vision multimodal embedding model and the Azure Document Intelligence Layout model used by the skills in this tutorial. You must use a Foundry resource for skillset access to these resources.
-
-+ [Azure AI Search](search-create-service-portal.md). [Configure your search service](search-manage.md) for role-based access control and a managed identity. Your service must be on the Basic tier or higher. This tutorial isn't supported on the Free tier.
-
-+ [Azure Storage](/azure/storage/common/storage-account-create), used for storing sample data and for creating a [knowledge store](knowledge-store-concept-intro.md).
-
-+ [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
-
-## Limitations
-
-+ The [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) has limited regional availability. When you create the Foundry resource, choose a region that provides multimodal embeddings. For a list of supported regions, see [Document Layout skill supported regions](cognitive-search-skill-document-intelligence-layout.md#supported-regions).
-
-+ The [Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md) also has limited regional availability. For an updated list of regions that provide multimodal embeddings, see the [Azure Vision documentation](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
-
-## Prepare data
-
-The following instructions apply to Azure Storage which provides the sample data and also hosts the knowledge store. A search service identity needs read access to Azure Storage to retrieve the sample data, and it needs write access to create the knowledge store. The search service creates the container for cropped images during skillset processing, using the name you provide in an environment variable.
-
-1. Download the following sample PDF: [sustainable-ai-pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Accelerating-Sustainability-with-AI-2025.pdf)
-
-1. In Azure Storage, create a new container named **sustainable-ai-pdf**.
-
-1. [Upload the sample data file](/azure/storage/blobs/storage-quickstart-blobs-portal).
-
-1. [Create role assignments and specify a managed identity in a connection string](search-howto-managed-identities-storage.md):
-
-   1. Assign **Storage Blob Data Reader** for data retrieval by the indexer. Assign **Storage Blob Data Contributor** and **Storage Table Data Contributor** to create and load the knowledge store. You can use either a system-assigned managed identity or a user-assigned managed identity for your search service role assignment.
-
-   1. For connections made using a system-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. The connection string is similar to the following example:
-
-        ```json
-        "credentials" : { 
-            "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-        }
-        ```
-
-   1. For connections made using a user-assigned managed identity, get a connection string that contains a ResourceId, with no account key or password. The ResourceId must include the subscription ID of the storage account, the resource group of the storage account, and the storage account name. Provide an identity using the syntax shown in the following example. Set userAssignedIdentity to the user-assigned managed identity. The connection string is similar to the following example:
-
-      ```json
-      "credentials" : { 
-          "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
-      },
-      "identity" : { 
-          "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
-          "userAssignedIdentity" : "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MY-DEMO-USER-MANAGED-IDENTITY" 
-      }
-      ```
-
-## Prepare models
-
-This tutorial assumes you have an existing Foundry resource through which the skill calls the Azure Vision multimodal 4.0 embedding model. The search service connects to the model during skillset processing using its managed identity. This section gives you guidance and links for assigning roles for authorized access.
-
-The same role assignment is also used for accessing the Azure Document Intelligence layout model via a Foundry resource.
-
-1. Sign in to the Azure portal (not the Foundry portal) and find the Foundry resource. Make sure it's in a region that provides the [multimodal 4.0 API](/azure/ai-services/computer-vision/overview-image-analysis#region-availability) and the [Azure Document Intelligence layout model](cognitive-search-skill-document-intelligence-layout.md#supported-regions).
-
-1. Select **Access control (IAM)**.
-
-1. Select **Add** and then **Add role assignment**.
-
-1. Search for **Cognitive Services User** and then select it.
-
-1. Choose **Managed identity** and then assign your [search service managed identity](search-how-to-managed-identities.md).
-
-## Set up your REST file
-
-For this tutorial, your local REST client connection to Azure AI Search requires an endpoint and an API key. You can get these values from the Azure portal. For alternative connection methods, see [Connect to a search service](search-get-started-rbac.md).
-
-For authenticated connections that occur during indexer and skillset processing, the search service uses the role assignments you previously defined.
-
-1. Start Visual Studio Code and create a new file.
-
-1. Provide values for variables used in the request. For `@storageConnection`, make sure your connection string doesn't have a trailing semicolon or quotation marks. For `@imageProjectionContainer`, provide a container name that's unique in blob storage. Azure AI Search creates this container for you during skills processing.
-
-   ```http
-   @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
-   @searchApiKey = PUT-YOUR-ADMIN-API-KEY-HERE
-   @storageConnection = PUT-YOUR-STORAGE-CONNECTION-STRING-HERE
-   @cognitiveServicesUrl = PUT-YOUR-AZURE-AI-FOUNDARY-ENDPOINT-HERE
-   @modelVersion = 2023-04-15
-   @imageProjectionContainer=sustainable-ai-pdf-images
-   ```
-
-1. Save the file using a `.rest` or `.http` file extension. For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
-
-To get the Azure AI Search endpoint and API key:
-
-1. Sign in to the [Azure portal](https://portal.azure.com), navigate to the search service **Overview** page, and copy the URL. An example endpoint might look like `https://mydemo.search.windows.net`.
-
-1. Under **Settings** > **Keys**, copy an admin key. Admin keys are used to add, modify, and delete objects. There are two interchangeable admin keys. Copy either one.
-
-   :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot of the URL and API keys in the Azure portal.":::
-
-## Create a data source
-
-[Create Data Source (REST)](/rest/api/searchservice/data-sources/create) creates a data source connection that specifies what data to index.
-
-```http
-### Create a data source using system-assigned managed identities
-POST {{searchUrl}}/datasources?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-  {
-    "name": "doc-intelligence-multimodal-embedding-ds",
-    "description": "A data source to store multimodal documents",
-    "type": "azureblob",
-    "subtype": null,
-    "credentials":{
-      "connectionString":"{{storageConnection}}"
-    },
-    "container": {
-      "name": "sustainable-ai-pdf",
-      "query": null
-    },
-    "dataChangeDetectionPolicy": null,
-    "dataDeletionDetectionPolicy": null,
-    "encryptionKey": null,
-    "identity": null
-  }
-```
-
-Send the request. The response should look like:
-
-```json
-HTTP/1.1 201 Created
-Transfer-Encoding: chunked
-Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
-Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('doc-extraction-multimodal-embedding-ds')?api-version=2025-11-01-preview -Preview
-Server: Microsoft-IIS/10.0
-Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
-Preference-Applied: odata.include-annotations="*"
-OData-Version: 4.0
-request-id: 4eb8bcc3-27b5-44af-834e-295ed078e8ed
-elapsed-time: 346
-Date: Sat, 26 Apr 2025 21:25:24 GMT
-Connection: close
-
-{
-  "name": "doc-extraction-multimodal-embedding-ds",
-  "description": null,
-  "type": "azureblob",
-  "subtype": null,
-  "indexerPermissionOptions": [],
-  "credentials": {
-    "connectionString": null
-  },
-  "container": {
-    "name": "sustainable-ai-pdf",
-    "query": null
-  },
-  "dataChangeDetectionPolicy": null,
-  "dataDeletionDetectionPolicy": null,
-  "encryptionKey": null,
-  "identity": null
-}
-```
-
-## Create an index
-
-[Create Index (REST)](/rest/api/searchservice/indexes/create) creates a search index on your search service. An index specifies all the parameters and their attributes.
-
-For nested JSON, the index fields must be identical to the source fields. Currently, Azure AI Search doesn't support field mappings to nested JSON, so field names and data types must match completely. The following index aligns to the JSON elements in the raw content.
-
-```http
-### Create an index
-POST {{searchUrl}}/indexes?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-{
-    "name": "doc-intelligence-multimodal-embedding-index",
-    "fields": [
-        {
-            "name": "content_id",
-            "type": "Edm.String",
-            "retrievable": true,
-            "key": true,
-            "analyzer": "keyword"
-        },
-        {
-            "name": "text_document_id",
-            "type": "Edm.String",
-            "searchable": false,
-            "filterable": true,
-            "retrievable": true,
-            "stored": true,
-            "sortable": false,
-            "facetable": false
-        },          
-        {
-            "name": "document_title",
-            "type": "Edm.String",
-            "searchable": true
-        },
-        {
-            "name": "image_document_id",
-            "type": "Edm.String",
-            "filterable": true,
-            "retrievable": true
-        },
-        {
-            "name": "content_text",
-            "type": "Edm.String",
-            "searchable": true,
-            "retrievable": true
-        },
-        {
-            "name": "content_embedding",
-            "type": "Collection(Edm.Single)",
-            "dimensions": 1024,
-            "searchable": true,
-            "retrievable": true,
-            "vectorSearchProfile": "hnsw"
-        },
-        {
-            "name": "content_path",
-            "type": "Edm.String",
-            "searchable": false,
-            "retrievable": true
-        },
-        {
-            "name": "offset",
-            "type": "Edm.String",
-            "searchable": false,
-            "retrievable": true
-        },
-        {
-            "name": "location_metadata",
-            "type": "Edm.ComplexType",
-            "fields": [
-                {
-                "name": "page_number",
-                "type": "Edm.Int32",
-                "searchable": false,
-                "retrievable": true
-                },
-                {
-                "name": "bounding_polygons",
-                "type": "Edm.String",
-                "searchable": false,
-                "retrievable": true,
-                "filterable": false,
-                "sortable": false,
-                "facetable": false
-                }
-            ]
-        }         
-    ],
-    "vectorSearch": {
-        "profiles": [
-            {
-                "name": "hnsw",
-                "algorithm": "defaulthnsw",
-                "vectorizer": "demo-vectorizer"
-            }
-        ],
-        "algorithms": [
-            {
-                "name": "defaulthnsw",
-                "kind": "hnsw",
-                "hnswParameters": {
-                    "m": 4,
-                    "efConstruction": 400,
-                    "metric": "cosine"
-                }
-            }
-        ],
-        "vectorizers": [
-            {
-                "name": "demo-vectorizer",
-                "kind": "aiServicesVision",
-                "aiServicesVisionParameters": {
-                    "resourceUri": "{{cognitiveServicesUrl}}",
-                    "authIdentity": null,
-                    "modelVersion": "{{modelVersion}}"
-                }
-            }
-        ]     
-    },
-    "semantic": {
-        "defaultConfiguration": "semanticconfig",
-        "configurations": [
-            {
-                "name": "semanticconfig",
-                "prioritizedFields": {
-                    "titleField": {
-                        "fieldName": "document_title"
-                    },
-                    "prioritizedContentFields": [
-                    ],
-                    "prioritizedKeywordsFields": []
-                }
-            }
-        ]
-    }
-}
-```
-
-Key points:
-
-+ Text and image embeddings are stored in the `content_embedding` field and must be configured with appropriate dimensions, such as 1024, and a vector search profile.
-
-+ `location_metadata` captures bounding polygon and page number metadata for each text chunk and normalized image, enabling precise spatial search or UI overlays.
-
-+ For more information on vector search, see [Vectors in Azure AI Search](vector-search-overview.md).
-
-+ For more information on semantic ranking, see [Semantic ranking in Azure AI Search](semantic-search-overview.md).
-
-## Create a skillset
-
-[Create Skillset (REST)](/rest/api/searchservice/skillsets/create) creates a skillset on your search service. A skillset defines the operations that chunk and embed content prior to indexing. This skillset uses the Document Layout skill to extract text and images, preserving location metadata which is useful for citations in RAG applications. It uses Azure Vision multimodal embeddings skill to vectorize image and text content.
-
-```http
-### Create a skillset
-POST {{searchUrl}}/skillsets?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-{
-  "name": "doc-intelligence-multimodal-embedding-skillset",
-  "description": "A sample skillset for multimodal using multimodal embedding",
-  "skills": [
-    {
-      "@odata.type": "#Microsoft.Skills.Util.DocumentIntelligenceLayoutSkill",
-      "name": "document-layout-skill",
-      "description": "Azure Document Intelligence skill for document cracking",
-      "context": "/document",
-      "outputMode": "oneToMany",
-      "outputFormat": "text",
-      "extractionOptions": ["images", "locationMetadata"],
-      "chunkingProperties": {     
-          "unit": "characters",
-          "maximumLength": 2000, 
-          "overlapLength": 200
-      },
-      "inputs": [
-        {
-          "name": "file_data",
-          "source": "/document/file_data"
-        }
-      ],
-      "outputs": [
-        { 
-          "name": "text_sections", 
-          "targetName": "text_sections" 
-        }, 
-        { 
-          "name": "normalized_images", 
-          "targetName": "normalized_images" 
-        } 
-      ]
-    },
-    { 
-      "@odata.type": "#Microsoft.Skills.Vision.VectorizeSkill", 
-      "name": "text-embedding-skill",
-      "description": "Vision Vectorization skill for text",
-      "context": "/document/text_sections/*", 
-      "modelVersion": "2023-04-15", 
-      "inputs": [ 
-        { 
-          "name": "text", 
-          "source": "/document/text_sections/*/content" 
-        } 
-      ], 
-      "outputs": [ 
-        { 
-          "name": "vector",
-          "targetName": "text_vector"
-        } 
-      ] 
-    },    
-    { 
-      "@odata.type": "#Microsoft.Skills.Vision.VectorizeSkill", 
-      "name": "image-embedding-skill",
-      "description": "Vision Vectorization skill for images",
-      "context": "/document/normalized_images/*", 
-      "modelVersion": "2023-04-15", 
-      "inputs": [ 
-        { 
-          "name": "image", 
-          "source": "/document/normalized_images/*" 
-        } 
-      ], 
-      "outputs": [ 
-        { 
-          "name": "vector",
-          "targetName": "image_vector"
-        } 
-      ] 
-    },
-    {
-      "@odata.type": "#Microsoft.Skills.Util.ShaperSkill",
-      "name": "shaper-skill",
-      "context": "/document/normalized_images/*",
-      "inputs": [
-        {
-          "name": "normalized_images",
-          "source": "/document/normalized_images/*",
-          "inputs": []
-        },
-        {
-          "name": "imagePath",
-          "source": "='my_container_name/'+$(/document/normalized_images/*/imagePath)",
-          "inputs": []
-        }
-      ],
-      "outputs": [
-        {
-          "name": "output",
-          "targetName": "new_normalized_images"
-        }
-      ]
-    }      
-  ], 
-   "indexProjections": {
-      "selectors": [
-        {
-          "targetIndexName": "doc-intelligence-multimodal-embedding-index",
-          "parentKeyFieldName": "text_document_id",
-          "sourceContext": "/document/text_sections/*",
-          "mappings": [    
-            {
-            "name": "content_embedding",
-            "source": "/document/text_sections/*/text_vector"
-            },                      
-            {
-              "name": "content_text",
-              "source": "/document/text_sections/*/content"
-            },
-            {
-              "name": "location_metadata",
-              "source": "/document/text_sections/*/locationMetadata"
-            },                
-            {
-              "name": "document_title",
-              "source": "/document/document_title"
-            }   
-          ]
-        },        
-        {
-          "targetIndexName": "{{index}}",
-          "parentKeyFieldName": "image_document_id",
-          "sourceContext": "/document/normalized_images/*",
-          "mappings": [    
-            {
-            "name": "content_embedding",
-            "source": "/document/normalized_images/*/image_vector"
-            },                                           
-            {
-              "name": "content_path",
-              "source": "/document/normalized_images/*/new_normalized_images/imagePath"
-            },                    
-            {
-              "name": "document_title",
-              "source": "/document/document_title"
-            },
-            {
-              "name": "location_metadata",
-              "source": "/document/normalized_images/*/locationMetadata"
-            }             
-          ]
-        }
-      ],
-      "parameters": {
-        "projectionMode": "skipIndexingParentDocuments"
-      }
-  },
-  "cognitiveServices": {
-    "@odata.type": "#Microsoft.Azure.Search.AIServicesByIdentity",
-    "subdomainUrl": "{{cognitiveServicesUrl}}",
-    "identity": null
-  },
-  "knowledgeStore": {
-    "storageConnectionString": "",
-    "identity": null,
-    "projections": [
-      {
-        "files": [
-          {
-            "storageContainer": "{{imageProjectionContainer}}",
-            "source": "/document/normalized_images/*"
-          }
-        ]
-      }
-    ]
-  }
-}
-```
-
-This skillset extracts text and images, vectorizes both, and shapes the image metadata for projection into the index.
-
-Key points:
-
-+ The `content_text` field is populated with text extracted and chunked using the Document Layout Skill
-
-+ `content_path` contains the relative path to the image file within the designated image projection container. This field is generated only for images extracted from documents when `extractOption` is set to `["images", "locationMetadata"]` or `["images"]`, and can be mapped from the enriched document from the source field `/document/normalized_images/*/imagePath`.
-
-+ The Azure Vision multimodal embeddings skill enables embedding of both textual and visual data using the same skill type, differentiated by input (text vs image). For more information, see [Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md).
-
-## Create and run an indexer
-
-[Create Indexer](/rest/api/searchservice/indexers/create) creates an indexer on your search service. An indexer connects to the data source, loads data, runs a skillset, and indexes the enriched data.
-
-```http
-### Create and run an indexer
-POST {{searchUrl}}/indexers?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-
-{
-  "dataSourceName": "doc-intelligence-multimodal-embedding-ds",
-  "targetIndexName": "doc-intelligence-multimodal-embedding-index",
-  "skillsetName": "doc-intelligence-multimodal-embedding-skillset",
-  "parameters": {
-    "maxFailedItems": -1,
-    "maxFailedItemsPerBatch": 0,
-    "batchSize": 1,
-    "configuration": {
-      "allowSkillsetToReadFileData": true
-    }
-  },
-  "fieldMappings": [
-    {
-      "sourceFieldName": "metadata_storage_name",
-      "targetFieldName": "document_title"
-    }
-  ],
-  "outputFieldMappings": []
-}
-```
-
-## Run queries
-
-You can start searching as soon as the first document is loaded.
-
-```http
-### Query the index
-POST {{searchUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-  
-  {
-    "search": "*",
-    "count": true
-  }
-```
-
-Send the request. This is an unspecified full-text search query that returns all of the fields marked as retrievable in the index, along with a document count. The response should look like:
-
-```json
-{
-  "@odata.count": 100,
-  "@search.nextPageParameters": {
-    "search": "*",
-    "count": true,
-    "skip": 50
-  },
-  "value": [
-  ],
-  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-11-01-preview "
-}
-```
-100 documents are returned in the response.
-
-For filters, you can also use Logical operators (and, or, not) and comparison operators (eq, ne, gt, lt, ge, le). String comparisons are case-sensitive. For more information and examples, see [Examples of simple search queries](search-query-simple-examples.md).
-
-> [!NOTE]
-> The `$filter` parameter only works on fields that were marked filterable during index creation.
-
-```http
-### Query for only images
-POST {{searchUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-  
-  {
-    "search": "*",
-    "count": true,
-    "filter": "image_document_id ne null"
-  }
-```
-
-```http
-### Query for text or images with content related to energy, returning the id, parent document, and text (only populated for text chunks), and the content path where the image is saved in the knowledge store (only populated for images)
-POST {{searchUrl}}/indexes/doc-intelligence-multimodal-embedding-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
-  Content-Type: application/json
-  api-key: {{searchApiKey}}
-  
-  {
-    "search": "energy",
-    "count": true,
-    "select": "content_id, document_title, content_text, content_path"
-  }
-```
-
-## Reset and rerun
-
-Indexers can be reset to clear execution history, which allows a full rerun. The following POST requests are for reset, followed by rerun.
-
-```http
-### Reset the indexer
-POST {{searchUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/reset?api-version=2025-11-01-preview   HTTP/1.1
-  api-key: {{searchApiKey}}
-```
-
-```http
-### Run the indexer
-POST {{searchUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/run?api-version=2025-11-01-preview   HTTP/1.1
-  api-key: {{searchApiKey}}
-```
-
-```http
-### Check indexer status 
-GET {{searchUrl}}/indexers/doc-intelligence-multimodal-embedding-indexer/status?api-version=2025-11-01-preview   HTTP/1.1
-  api-key: {{searchApiKey}}
-```
-
-## Clean up resources
-
-When you're working in your own subscription, at the end of a project, it's a good idea to remove the resources that you no longer need. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.
-
-You can use the Azure portal to delete indexes, indexers, and data sources.
-
-## See also
-
-Now that you're familiar with a sample implementation of a multimodal indexing scenario, check out:
-
-+ [Azure Vision multimodal embeddings skill](cognitive-search-skill-vision-vectorize.md)
-+ [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md)
-+ [Vectors in Azure AI Search](vector-search-overview.md)
-+ [Semantic ranking in Azure AI Search](semantic-search-overview.md)
-+ [Tutorial: Vectorize images and text](tutorial-document-extraction-multimodal-embeddings.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "構造化ドキュメントレイアウトからのマルチモーダル埋め込みに関するチュートリアルの削除"
}
```

### Explanation
この変更は、`articles/search/tutorial-document-layout-multimodal-embeddings.md`ファイルが完全に削除されたことを示しています。このチュートリアルは、Azure AI Searchを使用してPDFドキュメントからテキストと画像を抽出し、それらを同時にベクター化する方法について述べていました。

削除された内容には、ドキュメントレイアウトスキルを用いたデータのチャンク化や、Azure Visionを利用したマルチモーダル埋め込みによる内容のベクター化が含まれており、検索可能なインデックスにデータを取り込む手法が記載されていました。また、使用するリソースやセットアップ手順に関する具体的な要件が明記されていました。

この削除により、関連する情報や手法に対するアクセスが失われるため、ユーザーは新たなリソースや代替手段を探す必要があります。最新のチュートリアルや更新されたドキュメントを確認し、Azure AI Searchの機能を有効に活用するための支援を受けることが重要です。

## articles/search/tutorial-multimodal.md{#item-718d2e}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,1848 @@
+---
+title: 'Tutorial: Multimodal Chunking and Embedding'
+titleSuffix: Azure AI Search
+description: Learn how to extract, chunk, index, and search multimodal content using an indexer and skills.
+manager: nitinme
+author: heidisteen
+ms.author: heidist
+ms.service: azure-ai-search
+ms.update-cycle: 180-days
+ms.custom:
+ms.topic: tutorial
+ms.date: 02/25/2026
+# This is the primary instructional guidance for GenAI prompt, Document Layout, Azure AI Vision.
+---
+
+# Tutorial: Extract, chunk, and embed multimodal content
+
+In this tutorial, you'll build a multimodal indexer pipeline that performs these tasks:
+
+> [!div class="checklist"]
+>
+> + Extract and chunk text and images
+> + Vectorize text and images for similarity search
+> + Send cropped images to a knowledge store for retrieval by your app
+
+This tutorial shows multiple skillsets side by side to illustrate different ways to extract, chunk, and vectorize multimodal content.
+
+## Prerequisites
+
++ [Azure AI Search](search-create-service-portal.md), on the basic pricing tier or higher if you want to use the sample data. [Configure a managed identity](search-how-to-managed-identities.md) for role-based access to models and data.
+
++ [Azure Storage](/azure/storage/common/storage-account-create), used for storing sample data and for creating a [knowledge store](knowledge-store-concept-intro.md).
+
++ [Microsoft Foundry resource](/azure/ai-services/multi-service-resource) that provides Foundry models and APIs. If you're using Azure AI Vision multimodal, choose one of its [supported regions](/azure/ai-services/computer-vision/overview-image-analysis#region-availability) for your Microsoft Foundry resource.
+
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) or the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python). If you haven't installed a suitable version of Python, follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter).
+
+Multimodal indexing is implemented through skills that call AI models and APIs in an indexer pipeline. Model prerequisites vary depending on the [skills chosen for each task](#choose-skills-for-multimodal-indexing).
+
+> [!TIP]
+> To complete this tutorial on the free tier, use a smaller document with fewer images. This tutorial uses Foundry models only, but you can [create custom skills](cognitive-search-custom-skill-interface.md) to use other models. 
+
+### Configure access
+
+[!INCLUDE [resource authentication](includes/resource-authentication.md)]
+
+### Get endpoint
+
+[!INCLUDE [resource endpoint](includes/resource-endpoint.md)]
+
+### Prepare data
+
+Sample data is a 36-page PDF document that combines rich visual content, such as charts, infographics, and scanned pages, with original text. Azure Storage provides the sample data and hosts the [knowledge store](knowledge-store-concept-intro.md). A search service managed identity needs:
+
++ Read access to Azure Storage to retrieve the sample data.
+
++ Write access to create the knowledge store. The search service creates the container for cropped images during skillset processing, using the name you provide in an environment variable.
+
+Follow these steps to set up the sample data.
+
+1. Download the following sample PDF: [sustainable-ai-pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Accelerating-Sustainability-with-AI-2025.pdf)
+
+1. Sign in to the [Azure portal](https://portal.azure.com).
+
+1. In Azure Storage, create a new container named **sustainable-ai-pdf**.
+
+1. [Upload the sample data file](/azure/storage/blobs/storage-quickstart-blobs-portal).
+
+1. [Assign roles to the search service managed identity](search-howto-managed-identities-storage.md):
+
+   + **Storage Blob Data Reader** for data retrieval
+  
+   + **Storage Blob Data Contributor** and **Storage Table Data Contributor** for creating the knowledge store.
+
+While you have the Azure Storage pages open in the Azure portal, get a connection string for the environment variable.
+
+1. Under **Settings** > **Endpoints**, select the endpoint for Resource ID. It should look similar to the following example: `/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/rg-mydemo/providers/Microsoft.Storage/storageAccounts/mydemostorage/blobServices/default`.
+
+1. Prefix `ResourceId=` to this connection string. Use this version for your environment variable.
+
+   `ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/rg-mydemo/providers/Microsoft.Storage/storageAccounts/mydemostorage/blobServices/default`
+
+1. For connections made using a user-assigned managed identity, use the same connection string and provide an `identity` property set to a predefined user-assigned managed identity.
+
+      ```json
+      "credentials" : { 
+          "connectionString" : "ResourceId=/subscriptions/00000000-0000-0000-0000-00000000/resourceGroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/MY-DEMO-STORAGE-ACCOUNT/;" 
+      },
+      "identity" : { 
+          "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
+          "userAssignedIdentity" : "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/MY-DEMO-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MY-DEMO-USER-MANAGED-IDENTITY" 
+      }
+      ```
+
+## Choose skills for multimodal indexing
+
+The index, data source, and indexer definitions are mostly the same for all scenarios, but the skillset can include a different skill combination depending on how you want to extract, chunk, and vectorize text and images.
+
+1. Choose skills for extraction and chunking:
+
+   + Document Extraction, Text Split
+   + Document Layout
+
+1. Choose skills for vectorization:
+
+   + GenAI Prompt, Azure OpenAI Embedding
+   + Azure AI Vision Multimodal Embedding
+
+Most of these skills depend on a [deployed model](/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models) or a Microsoft Foundry resource. The following table identifies the model backing each skill, plus the resource and permissions that provide model access.
+
+| Skill | Usage | Model | Resource | Permissions |
+| -- | -- | -- | -- | -- |
+| [Document Extraction skill](cognitive-search-skill-document-extraction.md), [Text Split skill](cognitive-search-skill-textsplit.md) | Extract and chunk based on fixed size. <br>Text extraction is free. <br>[Image extraction is billable](https://azure.microsoft.com/pricing/details/search/). | None (built-in) | Azure AI Search | See [Configure access](#configure-access) |
+| [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) | Extract and chunk based on document layout. | [Document Intelligence 4.0](/azure/ai-services/document-intelligence/model-overview?view=doc-intel-4.0.0&preserve-view=true) | [Microsoft Foundry](/azure/ai-services/multi-service-resource?pivots=azportal) | Cognitive Services User |
+| [Azure AI Vision skill](cognitive-search-skill-vision-vectorize.md) | Vectorize text and image content. | [Azure AI Vision multimodal 4.0](/azure/ai-services/computer-vision/concept-image-retrieval) | [Microsoft Foundry](/azure/ai-services/multi-service-resource?pivots=azportal) | Cognitive Services User |
+| [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md)  | Call an LLM to generate text descriptions of image content. | [GPT-5 or GPT-4](/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure) | [Microsoft Foundry](/azure/ai-services/multi-service-resource?pivots=azportal) | Cognitive Services User |
+| [Azure OpenAI embedding skill](cognitive-search-skill-azure-openai-embedding.md) | Vectorize text and generated textual image descriptions. | [Text-embedding-3 or text-embedding-ada-002](/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure#embeddings) | [Microsoft Foundry](/azure/ai-services/multi-service-resource?pivots=azportal) | Cognitive Services User |
+
+Model usage is billable, except for text extraction and text splitting.
+
+Model deployments can be in any supported region if the search service connects over the public endpoint, a private connection, or if the [billing connection is keyless](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection). Otherwise, if the connection is key-based, [attach a Microsoft Foundry resource](cognitive-search-attach-cognitive-services.md) from the same region as Azure AI Search.
+
++ [Azure AI Vision multimodal 4.0 supported regions](/azure/ai-services/computer-vision/overview-image-analysis#region-availability)
+
++ [Document Intelligence 4.0 supported regions](cognitive-search-skill-document-intelligence-layout.md#supported-regions)
+
++ [Foundry model supported regions](/azure/ai-foundry/agents/concepts/model-region-support)
+
+## Set up your environment
+
+For this tutorial, your local REST client connection to Azure AI Search requires an endpoint and an API key. You can get these values in the Azure portal. For other connection methods, see [Connect to a search service](search-get-started-rbac.md).
+
+For authenticated connections that occur during indexer and skillset processing, the search service uses the role assignments you previously defined.
+
+1. Start Visual Studio Code and create a new file.
+
+1. Provide values for variables used in the request:
+
+   ```http
+    @searchUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
+    @storageConnection = PUT-YOUR-STORAGE-CONNECTION-STRING-HERE
+    @imageProjectionContainer=sustainable-ai-pdf-images
+    @token = PUT-YOUR-PERSONAL-IDENTITY-TOKEN HERE
+   ```
+
+   For `@storageConnection`, make sure your connection string doesn't have a trailing semicolon or quotation marks. See [Prepare your data](#prepare-data) for connection string syntax.
+
+   For `@imageProjectionContainer`, provide a container name that's unique in blob storage. Azure AI Search creates this container during skills processing.
+
+   For help getting an access token, see [Connect to Azure AI Search](search-get-started-rbac.md). If you can't use roles, see [Connect with keys](search-security-api-keys.md).
+
+1. Add this variable if you're using the Document Layout skill or the Azure AI Vision skill (uses model version 2023-04-15):
+
+   ```http
+   @foundryUrl = PUT-YOUR-MULTISERVICE-AZURE-AI-FOUNDRY-ENDPOINT-HERE
+   @azureAiVisionModelVersion = 2023-04-15
+   ```
+
+1. Add these variables if you're using the GenAI Prompt skill and Azure OpenAI Embedding skill:
+
+   ```http
+    @chatCompletionModelUri = PUT-YOUR-DEPLOYED-MODEL-URI-HERE
+    @chatCompletionModelKey = PUT-YOUR-MODEL-KEY-HERE
+    @textEmbeddingModelUri = PUT-YOUR-DEPLOYED-MODEL-URI-HERE
+    @textEmbeddingModelKey = PUT-YOUR-MODEL-KEY-HERE
+   ```
+
+1. Save the file using a `.rest` or `.http` file extension. For help with the REST client, see [Quickstart: Full-text search using REST](search-get-started-text.md).
+
+The same Foundry resource can provide Azure AI Vision, Document Intelligence, a chat completion model, and a text embedding model. Just make sure the region supports the models you need. If a region is at capacity, you might need to create a new resource to deploy the necessary models.
+
+## Set up a pipeline
+
+An indexer pipeline consists of four components: data source, index, skillset, and indexer.
++ [Create a data source](#create-a-data-source)
++ [Create an index](#create-an-index)
++ [Create a skillset for extraction, chunking, and vectorization](#create-a-skillset-for-extraction-chunking-and-vectorization)
++ [Create (and run) an indexer](#run-the-indexer)
+
+### Download REST files
+
+The [azure-search-rest-samples](https://github.com/Azure-Samples/azure-search-rest-samples/tree/main/multimodal-tutorial) GitHub repository has .REST files that create the pipeline and query the index.
+
+> [!TIP]
+> See the [azure-ai-search-multimodal-sample](https://github.com/Azure-Samples/azure-ai-search-multimodal-sample) GitHub repository for a Python example.
+
+### Create a data source
+
+[Create Data Source (REST)](/rest/api/searchservice/data-sources/create) creates a data source connection that specifies what data to index.
+
+```http
+POST {{searchUrl}}/datasources?api-version=2025-11-01-preview   HTTP/1.1
+  Content-Type: application/json
+  Authorization: Bearer {{token}}
+
+{
+   "name":"demo-multimodal-ds",
+   "description":null,
+   "type":"azureblob",
+   "subtype":null,
+   "credentials":{
+      "connectionString":"{{storageConnection}}"
+   },
+   "container":{
+      "name":"sustainable-ai-pdf",
+      "query":null
+   },
+   "dataChangeDetectionPolicy":null,
+   "dataDeletionDetectionPolicy":null,
+   "encryptionKey":null,
+   "identity":null
+}
+```
+
+Send the request. The response should look like:
+
+```json
+HTTP/1.1 201 Created
+Transfer-Encoding: chunked
+Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
+Location: https://<YOUR-SEARCH-SERVICE-NAME>.search.windows-int.net:443/datasources('demo-multimodal-ds')?api-version=2025-11-01-preview -Preview
+Server: Microsoft-IIS/10.0
+Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
+Preference-Applied: odata.include-annotations="*"
+OData-Version: 4.0
+request-id: 4eb8bcc3-27b5-44af-834e-295ed078e8ed
+elapsed-time: 346
+Date: Sat, 26 Apr 2026 21:25:24 GMT
+Connection: close
+
+{
+  "name": "demo-multimodal-ds",
+  "description": null,
+  "type": "azureblob",
+  "subtype": null,
+  "indexerPermissionOptions": [],
+  "credentials": {
+    "connectionString": null
+  },
+  "container": {
+    "name": "sustainable-ai-pdf",
+    "query": null
+  },
+  "dataChangeDetectionPolicy": null,
+  "dataDeletionDetectionPolicy": null,
+  "encryptionKey": null,
+  "identity": null
+}
+```
+
+### Create an index
+
+[Create Index (REST)](/rest/api/searchservice/indexes/create) creates an index on your search service. The index is similar across all skillsets, with the following exceptions:
+
++ The `vectorizers` section defines how query text is vectorized at search time. It must use the same embedding provider and model family used by the skillset (Azure AI Vision multimodal or Azure OpenAI text embedding) so query vectors and indexed vectors are compatible.
++
++ The `content_embedding` field `dimensions` value must exactly match the vector size produced by the embedding model (for example, `1024` for Azure AI Vision multimodal or `3072` for `text-embedding-3-large`). A mismatch can cause indexing or query failures.
+
++ For complex types, nested field names in the index must exactly match the enrichment output names (including casing). Azure AI Search can't map nested subfields to different names. Use `location_metadata`, `bounding_polygons`, and `page_number` for fields that accept Text Split outputs, and `locationMetadata`, `boundingPolygons`, and `pageNumber` for fields that accept Document Layout outputs.
+
+Here are the index definitions for each skill combination.
+
+### [**Document extraction & multimodal embedding**](#tab/doc-extraction-vision)
+
+This pattern uses:
+
++ [Document Extraction skill](cognitive-search-skill-document-extraction.md) and [Text Split skill](cognitive-search-skill-textsplit.md) for extraction and chunking.
+
++ [Azure AI Vision multimodal skill](cognitive-search-skill-vision-vectorize.md) for text and image embeddings.
+
+```json
+{
+   "name":"demo-multimodal-1-index",
+   "fields":[
+      {
+         "name":"content_id",
+         "type":"Edm.String",
+         "retrievable":true,
+         "key":true,
+         "analyzer":"keyword"
+      },
+      {
+         "name":"text_document_id",
+         "type":"Edm.String",
+         "searchable":false,
+         "filterable":true,
+         "retrievable":true,
+         "stored":true,
+         "sortable":false,
+         "facetable":false
+      },
+      {
+         "name":"document_title",
+         "type":"Edm.String",
+         "searchable":true
+      },
+      {
+         "name":"image_document_id",
+         "type":"Edm.String",
+         "filterable":true,
+         "retrievable":true
+      },
+      {
+         "name":"content_text",
+         "type":"Edm.String",
+         "searchable":true,
+         "retrievable":true
+      },
+      {
+         "name":"content_embedding",
+         "type":"Collection(Edm.Single)",
+         "dimensions":1024,
+         "searchable":true,
+         "retrievable":true,
+         "vectorSearchProfile":"hnsw"
+      },
+      {
+         "name":"content_path",
+         "type":"Edm.String",
+         "searchable":false,
+         "retrievable":true
+      },
+      {
+         "name":"location_metadata",
+         "type":"Edm.ComplexType",
+         "fields":[
+            {
+               "name":"page_number",
+               "type":"Edm.Int32",
+               "searchable":false,
+               "retrievable":true
+            },
+            {
+               "name":"bounding_polygons",
+               "type":"Edm.String",
+               "searchable":false,
+               "retrievable":true,
+               "filterable":false,
+               "sortable":false,
+               "facetable":false
+            }
+         ]
+      }
+   ],
+   "vectorSearch":{
+      "profiles":[
+         {
+            "name":"hnsw",
+            "algorithm":"defaulthnsw",
+            "vectorizer":"demo-vectorizer"
+         }
+      ],
+      "algorithms":[
+         {
+            "name":"defaulthnsw",
+            "kind":"hnsw",
+            "hnswParameters":{
+               "m":4,
+               "efConstruction":400,
+               "metric":"cosine"
+            }
+         }
+      ],
+      "vectorizers":[
+         {
+            "name":"demo-vectorizer",
+            "kind":"aiServicesVision",
+            "aiServicesVisionParameters":{
+               "resourceUri":"{{foundryUrl}}",
+               "authIdentity":null,
+               "modelVersion":"{{azureAiVisionModelVersion}}"
+            }
+         }
+      ]
+   },
+   "semantic":{
+      "defaultConfiguration":"semanticconfig",
+      "configurations":[
+         {
+            "name":"semanticconfig",
+            "prioritizedFields":{
+               "titleField":{
+                  "fieldName":"document_title"
+               },
+               "prioritizedContentFields":[
+                  
+               ],
+               "prioritizedKeywordsFields":[
+                  
+               ]
+            }
+         }
+      ]
+   }
+}
+```
+
+### [**Document extraction & text embedding**](#tab/doc-extraction-text)
+
+This pattern uses:
+
++ [Document Extraction skill](cognitive-search-skill-document-extraction.md) and [Text Split skill](cognitive-search-skill-textsplit.md) for extraction and chunking.
+
++ [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md) and [Azure OpenAI embedding skill](cognitive-search-skill-azure-openai-embedding.md) for textual descriptions of images and text embeddings.
+
+```json
+{
+   "name":"demo-multimodal-2-index",
+   "fields":[
+      {
+         "name":"content_id",
+         "type":"Edm.String",
+         "retrievable":true,
+         "key":true,
+         "analyzer":"keyword"
+      },
+      {
+         "name":"text_document_id",
+         "type":"Edm.String",
+         "searchable":false,
+         "filterable":true,
+         "retrievable":true,
+         "stored":true,
+         "sortable":false,
+         "facetable":false
+      },
+      {
+         "name":"document_title",
+         "type":"Edm.String",
+         "searchable":true
+      },
+      {
+         "name":"image_document_id",
+         "type":"Edm.String",
+         "filterable":true,
+         "retrievable":true
+      },
+      {
+         "name":"content_text",
+         "type":"Edm.String",
+         "searchable":true,
+         "retrievable":true
+      },
+      {
+         "name":"content_embedding",
+         "type":"Collection(Edm.Single)",
+         "dimensions":3072,
+         "searchable":true,
+         "retrievable":true,
+         "vectorSearchProfile":"hnsw"
+      },
+      {
+         "name":"content_path",
+         "type":"Edm.String",
+         "searchable":false,
+         "retrievable":true
+      },
+      {
+         "name":"location_metadata",
+         "type":"Edm.ComplexType",
+         "fields":[
+            {
+               "name":"page_number",
+               "type":"Edm.Int32",
+               "searchable":false,
+               "retrievable":true
+            },
+            {
+               "name":"bounding_polygons",
+               "type":"Edm.String",
+               "searchable":false,
+               "retrievable":true,
+               "filterable":false,
+               "sortable":false,
+               "facetable":false
+            }
+         ]
+      }
+   ],
+   "vectorSearch":{
+      "profiles":[
+         {
+            "name":"hnsw",
+            "algorithm":"defaulthnsw",
+            "vectorizer":"demo-vectorizer"
+         }
+      ],
+      "algorithms":[
+         {
+            "name":"defaulthnsw",
+            "kind":"hnsw",
+            "hnswParameters":{
+               "m":4,
+               "efConstruction":400,
+               "metric":"cosine"
+            }
+         }
+      ],
+      "vectorizers":[
+         {
+            "name":"demo-vectorizer",
+            "kind":"azureOpenAI",
+            "azureOpenAIParameters":{
+               "resourceUri": "{{textEmbeddingModelUri}}",
+               "apiKey": "{{textEmbeddingModelKey}}",
+               "deploymentId":"{{textEmbeddingDeploymentId}}",
+               "modelName":"{{textEmbeddingModelName}}"
+            }
+         }
+      ]
+   },
+   "semantic":{
+      "defaultConfiguration":"semanticconfig",
+      "configurations":[
+         {
+            "name":"semanticconfig",
+            "prioritizedFields":{
+               "titleField":{
+                  "fieldName":"document_title"
+               },
+               "prioritizedContentFields":[
+                  
+               ],
+               "prioritizedKeywordsFields":[
+                  
+               ]
+            }
+         }
+      ]
+   }
+}
+```
+
+### [**Document layout & multimodal embedding**](#tab/doc-layout-vision)
+
+This pattern uses:
+
++ [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) for extraction and chunking.
+
++ [Azure AI Vision multimodal skill](cognitive-search-skill-vision-vectorize.md) for text and image embeddings.
+
+```json
+{
+   "name":"demo-multimodal-3-index",
+   "fields":[
+      {
+         "name":"content_id",
+         "type":"Edm.String",
+         "retrievable":true,
+         "key":true,
+         "analyzer":"keyword"
+      },
+      {
+         "name":"text_document_id",
+         "type":"Edm.String",
+         "searchable":false,
+         "filterable":true,
+         "retrievable":true,
+         "stored":true,
+         "sortable":false,
+         "facetable":false
+      },
+      {
+         "name":"document_title",
+         "type":"Edm.String",
+         "searchable":true
+      },
+      {
+         "name":"image_document_id",
+         "type":"Edm.String",
+         "filterable":true,
+         "retrievable":true
+      },
+      {
+         "name":"content_text",
+         "type":"Edm.String",
+         "searchable":true,
+         "retrievable":true
+      },
+      {
+         "name":"content_embedding",
+         "type":"Collection(Edm.Single)",
+         "dimensions":1024,
+         "searchable":true,
+         "retrievable":true,
+         "vectorSearchProfile":"hnsw"
+      },
+      {
+         "name":"content_path",
+         "type":"Edm.String",
+         "searchable":false,
+         "retrievable":true
+      },
+      {
+         "name":"locationMetadata",
+         "type":"Edm.ComplexType",
+         "fields":[
+            {
+               "name":"pageNumber",
+               "type":"Edm.Int32",
+               "searchable":false,
+               "retrievable":true
+            },
+            {
+               "name":"boundingPolygons",
+               "type":"Edm.String",
+               "searchable":false,
+               "retrievable":true,
+               "filterable":false,
+               "sortable":false,
+               "facetable":false
+            }
+         ]
+      }
+   ],
+   "vectorSearch":{
+      "profiles":[
+         {
+            "name":"hnsw",
+            "algorithm":"defaulthnsw",
+            "vectorizer":"demo-vectorizer"
+         }
+      ],
+      "algorithms":[
+         {
+            "name":"defaulthnsw",
+            "kind":"hnsw",
+            "hnswParameters":{
+               "m":4,
+               "efConstruction":400,
+               "metric":"cosine"
+            }
+         }
+      ],
+      "vectorizers":[
+         {
+            "name":"demo-vectorizer",
+            "kind":"aiServicesVision",
+            "aiServicesVisionParameters":{
+               "resourceUri":"{{foundryUrl}}",
+               "authIdentity":null,
+               "modelVersion":"{{azureAiVisionModelVersion}}"
+            }
+         }
+      ]
+   },
+   "semantic":{
+      "defaultConfiguration":"semanticconfig",
+      "configurations":[
+         {
+            "name":"semanticconfig",
+            "prioritizedFields":{
+               "titleField":{
+                  "fieldName":"document_title"
+               },
+               "prioritizedContentFields":[
+                  
+               ],
+               "prioritizedKeywordsFields":[
+                  
+               ]
+            }
+         }
+      ]
+   }
+}
+```
+
+### [**Document layout & text embedding**](#tab/doc-layout-text)
+
+This pattern uses:
+
++ [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) for extraction and chunking.
+
++ [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md) and [Azure OpenAI embedding skill](cognitive-search-skill-azure-openai-embedding.md) for textual descriptions of images and text embeddings.
+
+```json
+{
+   "name":"demo-multimodal-4-index",
+   "fields":[
+      {
+         "name":"content_id",
+         "type":"Edm.String",
+         "retrievable":true,
+         "key":true,
+         "analyzer":"keyword"
+      },
+      {
+         "name":"text_document_id",
+         "type":"Edm.String",
+         "searchable":false,
+         "filterable":true,
+         "retrievable":true,
+         "stored":true,
+         "sortable":false,
+         "facetable":false
+      },
+      {
+         "name":"document_title",
+         "type":"Edm.String",
+         "searchable":true
+      },
+      {
+         "name":"image_document_id",
+         "type":"Edm.String",
+         "filterable":true,
+         "retrievable":true
+      },
+      {
+         "name":"content_text",
+         "type":"Edm.String",
+         "searchable":true,
+         "retrievable":true
+      },
+      {
+         "name":"content_embedding",
+         "type":"Collection(Edm.Single)",
+         "dimensions":3072,
+         "searchable":true,
+         "retrievable":true,
+         "vectorSearchProfile":"hnsw"
+      },
+      {
+         "name":"content_path",
+         "type":"Edm.String",
+         "searchable":false,
+         "retrievable":true
+      },
+      {
+         "name":"locationMetadata",
+         "type":"Edm.ComplexType",
+         "fields":[
+            {
+               "name":"pageNumber",
+               "type":"Edm.Int32",
+               "searchable":false,
+               "retrievable":true
+            },
+            {
+               "name":"boundingPolygons",
+               "type":"Edm.String",
+               "searchable":false,
+               "retrievable":true,
+               "filterable":false,
+               "sortable":false,
+               "facetable":false
+            }
+         ]
+      }
+   ],
+   "vectorSearch":{
+      "profiles":[
+         {
+            "name":"hnsw",
+            "algorithm":"defaulthnsw",
+            "vectorizer":"demo-vectorizer"
+         }
+      ],
+      "algorithms":[
+         {
+            "name":"defaulthnsw",
+            "kind":"hnsw",
+            "hnswParameters":{
+               "m":4,
+               "efConstruction":400,
+               "metric":"cosine"
+            }
+         }
+      ],
+      "vectorizers":[
+         {
+            "name":"demo-vectorizer",
+            "kind":"azureOpenAI",
+            "azureOpenAIParameters":{
+               "resourceUri":"{{textEmbeddingModelUri}}",
+               "deploymentId":"text-embedding-3-large",
+               "apiKey":"{{textEmbeddingModelKey}}",
+               "modelName":"text-embedding-3-large"
+            }
+         }
+      ]
+   },
+   "semantic":{
+      "defaultConfiguration":"semanticconfig",
+      "configurations":[
+         {
+            "name":"semanticconfig",
+            "prioritizedFields":{
+               "titleField":{
+                  "fieldName":"document_title"
+               },
+               "prioritizedContentFields":[
+                  
+               ],
+               "prioritizedKeywordsFields":[
+                  
+               ]
+            }
+         }
+      ]
+   }
+}
+```
+
+---
+
+Key points:
+
++ `content_embedding` is the only vector field and it stores vectors for both text and image content. It must be configured with appropriate dimensions for the embedding model, such as `3072` for text-embedding-3-large, and a vector search profile.
+
++ `content_path` is the path of each image in the knowledge store.
+
++ `location_metadata` or `locationMetadata` captures bounding polygon and page number metadata for each normalized image, enabling precise spatial search or UI overlays. The field names vary based on how the information is extracted. 
+
++ For content extraction based on the Text Split skill: location metadata is supported only for PDF files. Furthermore, for Text Split skill, you must include a Shaper skill for capturing in-memory location metadata and representing it in the document tree. The Shaper skill is also responsible for adding the knowledge store container name to the `content_path`.
+
+### Create a skillset for extraction, chunking, and vectorization
+
+[Create Skillset (REST)](/rest/api/searchservice/skillsets/create) creates a skillset on your search service. A skillset defines the operations that extract, chunk, and vectorize content prior to indexing.
+
+There are four skillset patterns. Each one demonstrates an extraction and chunking strategy, paired with a vectorization strategy. There are two key differences in each pattern: skillset composition and `indexProjections`. Projections vary based on the outputs of each embedding skill.
+
+All four patterns include the [Shaper skill](cognitive-search-skill-shaper.md). Output from the Shaper skill creates the normalized path of images in the knowledge store and location metadata (page number and bounding polygons).
+
+### [**Document extraction & multimodal embedding**](#tab/doc-extraction-vision)
+
+This pattern uses:
+
++ [Document Extraction skill](cognitive-search-skill-document-extraction.md) and [Text Split skill](cognitive-search-skill-textsplit.md) for extraction and chunking.
+
++ [Azure AI Vision multimodal skill](cognitive-search-skill-vision-vectorize.md) for text and image embeddings.
+
++ [Shaper skill](cognitive-search-skill-shaper.md) captures location metadata and the container name for the image file path in the knowledge store. This capability is unique to PDF content and Document Extraction.
+
+```json
+{
+   "name":"demo-multimodal-skillset",
+   "description":"A test skillset",
+   "skills":[
+      {
+         "@odata.type":"#Microsoft.Skills.Util.DocumentExtractionSkill",
+         "name":"document-extraction-skill",
+         "description":"Document extraction skill to extract text and images from documents",
+         "parsingMode":"default",
+         "dataToExtract":"contentAndMetadata",
+         "configuration":{
+            "imageAction":"generateNormalizedImages",
+            "normalizedImageMaxWidth":2000,
+            "normalizedImageMaxHeight":2000
+         },
+         "context":"/document",
+         "inputs":[
+            {
+               "name":"file_data",
+               "source":"/document/file_data"
+            }
+         ],
+         "outputs":[
+            {
+               "name":"content",
+               "targetName":"extracted_content"
+            },
+            {
+               "name":"normalized_images",
+               "targetName":"normalized_images"
+            }
+         ]
+      },
+      {
+         "@odata.type":"#Microsoft.Skills.Text.SplitSkill",
+         "name":"split-skill",
+         "description":"Split skill to chunk documents",
+         "context":"/document",
+         "defaultLanguageCode":"en",
+         "textSplitMode":"pages",
+         "maximumPageLength":2000,
+         "pageOverlapLength":200,
+         "unit":"characters",
+         "inputs":[
+            {
+               "name":"text",
+               "source":"/document/extracted_content",
+               "inputs":[
+                  
+               ]
+            }
+         ],
+         "outputs":[
+            {
+               "name":"textItems",
+               "targetName":"pages"
+            }
+         ]
+      },
+      {
+         "@odata.type":"#Microsoft.Skills.Vision.VectorizeSkill",
+         "name":"text-embedding-skill",
+         "description":"Vision Vectorization skill for text",
+         "context":"/document/pages/*",
+         "modelVersion":"{{azureAiVisionModelVersion}}",
+         "inputs":[
+            {
+               "name":"text",
+               "source":"/document/pages/*"
+            }
+         ],
+         "outputs":[
+            {
+               "name":"vector",
+               "targetName":"text_vector"
+            }
+         ]
+      },
+      {
+         "@odata.type":"#Microsoft.Skills.Vision.VectorizeSkill",
+         "name":"image-embedding-skill",
+         "description":"Vision Vectorization skill for images",
+         "context":"/document/normalized_images/*",
+         "modelVersion":"{{azureAiVisionModelVersion}}",
+         "inputs":[
+            {
+               "name":"image",
+               "source":"/document/normalized_images/*"
+            }
+         ],
+         "outputs":[
+            {
+               "name":"vector",
+               "targetName":"image_vector"
+            }
+         ]
+      },
+      {
+         "@odata.type":"#Microsoft.Skills.Util.ShaperSkill",
+         "name":"shaper-skill",
+         "description":"Shaper skill to reshape the data to fit the index schema",
+         "context":"/document/normalized_images/*",
+         "inputs":[
+            {
+               "name":"normalized_images",
+               "source":"/document/normalized_images/*",
+               "inputs":[
+                  
+               ]
+            },
+            {
+               "name":"imagePath",
+               "source":"='{{imageProjectionContainer}}/'+$(/document/normalized_images/*/imagePath)",
+               "inputs":[
+                  
+               ]
+            },
+            {
+               "name":"dataUri",
+               "source":"='data:image/jpeg;base64,'+$(/document/normalized_images/*/data)",
+               "inputs":[
+                  
+               ]
+            },
+            {
+               "name":"location_metadata",
+               "sourceContext":"/document/normalized_images/*",
+               "inputs":[
+                  {
+                     "name":"page_number",
+                     "source":"/document/normalized_images/*/page_number"
+                  },
+                  {
+                     "name":"bounding_polygons",
+                     "source":"/document/normalized_images/*/bounding_polygon"
+                  }
+               ]
+            }
+         ],
+         "outputs":[
+            {
+               "name":"output",
+               "targetName":"new_normalized_images"
+            }
+         ]
+      }
+   ],
+   "cognitiveServices":{
+      "@odata.type":"#Microsoft.Azure.Search.AIServicesByIdentity",
+      "subdomainUrl":"{{foundryUrl}}",
+      "identity":null
+   },
+   "indexProjections":{
+      "selectors":[
+         {
+            "targetIndexName":"demo-multimodal-index",
+            "parentKeyFieldName":"text_document_id",
+            "sourceContext":"/document/pages/*",
+            "mappings":[
+               {
+                  "name":"content_embedding",
+                  "source":"/document/pages/*/text_vector"
+               },
+               {
+                  "name":"content_text",
+                  "source":"/document/pages/*"
+               },
+               {
+                  "name":"document_title",
+                  "source":"/document/document_title"
+               }
+            ]
+         },
+         {
+            "targetIndexName":"demo-multimodal-index",
+            "parentKeyFieldName":"image_document_id",
+            "sourceContext":"/document/normalized_images/*",
+            "mappings":[
+               {
+                  "name":"content_embedding",
+                  "source":"/document/normalized_images/*/image_vector"
+               },
+               {
+                  "name":"content_path",
+                  "source":"/document/normalized_images/*/new_normalized_images/imagePath"
+               },
+               {
+                  "name":"location_metadata",
+                  "source":"/document/normalized_images/*/new_normalized_images/location_metadata"
+               },
+               {
+                  "name":"document_title",
+                  "source":"/document/document_title"
+               }
+            ]
+         }
+      ],
+      "parameters":{
+         "projectionMode":"skipIndexingParentDocuments"
+      }
+   },
+   "knowledgeStore":{
+      "storageConnectionString":"{{storageConnection}}",
+      "identity":null,
+      "projections":[
+         {
+            "files":[
+               {
+                  "storageContainer":"{{imageProjectionContainer}}",
+                  "source":"/document/normalized_images/*"
+               }
+            ]
+         }
+      ]
+   }
+}
+```
+
+### [**Document extraction & text embedding**](#tab/doc-extraction-text)
+
+This pattern uses:
+
++ [Document Extraction skill](cognitive-search-skill-document-extraction.md) and [Text Split skill](cognitive-search-skill-textsplit.md) for extraction and chunking.
+
++ [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md) and [Azure OpenAI embedding skill](cognitive-search-skill-azure-openai-embedding.md) for textual descriptions of images and text embeddings.
+
++ [Shaper skill](cognitive-search-skill-shaper.md) captures location metadata and the container name for the image file path in the knowledge store. This capability is unique to PDF content and Document Extraction.
+
+```json
+{
+   "name":"demo-multimodal-skillset",
+   "description":"A test skillset",
+   "skills":[
+      {
+         "@odata.type":"#Microsoft.Skills.Util.DocumentExtractionSkill",
+         "name":"document-extraction-skill",
+         "description":"Document extraction skill to extract text and images from documents",
+         "parsingMode":"default",
+         "dataToExtract":"contentAndMetadata",
+         "configuration":{
+            "imageAction":"generateNormalizedImages",
+            "normalizedImageMaxWidth":2000,
+            "normalizedImageMaxHeight":2000
+         },
+         "context":"/document",
+         "inputs":[
+            {
+               "name":"file_data",
+               "source":"/document/file_data"
+            }
+         ],
+         "outputs":[
+            {
+               "name":"content",
+               "targetName":"extracted_content"
+            },
+            {
+               "name":"normalized_images",
+               "targetName":"normalized_images"
+            }
+         ]
+      },
+      {
+         "@odata.type":"#Microsoft.Skills.Text.SplitSkill",
+         "name":"split-skill",
+         "description":"Split skill to chunk documents",
+         "context":"/document",
+         "defaultLanguageCode":"en",
+         "textSplitMode":"pages",
+         "maximumPageLength":2000,
+         "pageOverlapLength":200,
+         "unit":"characters",
+         "inputs":[
+            {
+               "name":"text",
+               "source":"/document/extracted_content",
+               "inputs":[
+                  
+               ]
+            }
+         ],
+         "outputs":[
+            {
+               "name":"textItems",
+               "targetName":"pages"
+            }
+         ]
+      },
+      {
+        "@odata.type": "#Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill",
+        "name": "#2",
+        "context": "/document/pages/*",
+        "resourceUri": "{{textEmbeddingModelUri}}",
+        "apiKey": "{{textEmbeddingModelKey}}",
+        "deploymentId":"{{textEmbeddingDeploymentId}}",
+        "modelName":"{{textEmbeddingModelName}}",
+        "dimensions": 3072,
+        "inputs": [
+          {
+            "name": "text",
+            "source": "/document/pages/*",
+            "inputs": []
+          }
+        ],
+        "outputs": [
+          {
+            "name": "embedding",
+            "targetName": "text_vector"
+          }
+        ]
+    },
+    {
+      "@odata.type": "#Microsoft.Skills.Custom.ChatCompletionSkill",
+      "name": "genAI-prompt-skill",
+      "description": "GenAI Prompt skill for image verbalization",
+      "uri": "{{chatCompletionModelUri}}",
+      "timeout": "PT1M",
+      "apiKey": "{{chatCompletionModelKey}}",
+      "context": "/document/normalized_images/*",
+      "responseFormat": { "type": "text" },
+      "inputs": [
+          {
+          "name": "systemMessage",
+          "source": "='You are tasked with generating concise, accurate descriptions of images, figures, diagrams, or charts in documents. The goal is to capture the key information and meaning conveyed by the image without including extraneous details like style, colors, visual aesthetics, or size.\n\nInstructions:\nContent Focus: Describe the core content and relationships depicted in the image.\n\nFor diagrams, specify the main elements and how they are connected or interact.\nFor charts, highlight key data points, trends, comparisons, or conclusions.\nFor figures or technical illustrations, identify the components and their significance.\nClarity & Precision: Use concise language to ensure clarity and technical accuracy. Avoid subjective or interpretive statements.\n\nAvoid Visual Descriptors: Exclude details about:\n\nColors, shading, and visual styles.\nImage size, layout, or decorative elements.\nFonts, borders, and stylistic embellishments.\nContext: If relevant, relate the image to the broader content of the technical document or the topic it supports.\n\nExample Descriptions:\nDiagram: \"A flowchart showing the four stages of a machine learning pipeline: data collection, preprocessing, model training, and evaluation, with arrows indicating the sequential flow of tasks.\"\n\nChart: \"A bar chart comparing the performance of four algorithms on three datasets, showing that Algorithm A consistently outperforms the others on Dataset 1.\"\n\nFigure: \"A labeled diagram illustrating the components of a transformer model, including the encoder, decoder, self-attention mechanism, and feedforward layers.\"'"
+          },
+          {
+          "name": "userMessage",
+          "source": "='Please describe this image.'"
+          },
+          {
+          "name": "image",
+          "source": "/document/normalized_images/*/data"
+          }
+          ],
+          "outputs": [
+              {
+              "name": "response",
+              "targetName": "verbalizedImage"
+              }
+          ]
+      },    
+      {
+        "@odata.type": "#Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill",
+        "name": "verbalized-image-embedding-skill",
+        "description": "Embedding skill for verbalized images",
+        "resourceUri": "{{textEmbeddingModelUri}}",
+        "apiKey": "{{textEmbeddingModelKey}}",
+        "deploymentId":"{{textEmbeddingDeploymentId}}",
+        "modelName":"{{textEmbeddingModelName}}",
+        "dimensions": 3072,
+        "context": "/document/normalized_images/*",
+        "inputs": [
+            {
+            "name": "text",
+            "source": "/document/normalized_images/*/verbalizedImage",
+            "inputs": []
+            }
+        ],
+        "outputs": [
+            {
+            "name": "embedding",
+            "targetName": "verbalizedImage_vector"
+            }
+        ]
+    },
+    {
+      "@odata.type": "#Microsoft.Skills.Util.ShaperSkill",
+      "name": "shaper-skill",
+      "description": "Shaper skill to reshape the data to fit the index schema",
+      "context": "/document/normalized_images/*",
+      "inputs": [
+        {
+          "name": "normalized_images",
+          "source": "/document/normalized_images/*",
+          "inputs": []
+        },
+        {
+          "name": "imagePath",
+          "source": "='{{imageProjectionContainer}}/'+$(/document/normalized_images/*/imagePath)",
+          "inputs": []
+        },
+        {
+          "name": "location_metadata",
+          "sourceContext": "/document/normalized_images/*",
+          "inputs": [
+            {
+              "name": "page_number",
+              "source": "/document/normalized_images/*/page_number"
+            },
+            {
+              "name": "bounding_polygons",
+              "source": "/document/normalized_images/*/bounding_polygon"
+            }              
+          ]
+        }        
+      ],
+      "outputs": [
+        {
+          "name": "output",
+          "targetName": "new_normalized_images"
+        }
+      ]
+   }
+   ],
+  "indexProjections": {
+      "selectors": [
+        {
+          "targetIndexName": "demo-multimodal-index",
+          "parentKeyFieldName": "text_document_id",
+          "sourceContext": "/document/pages/*",
+          "mappings": [              
+            {
+              "name": "content_embedding",
+              "source": "/document/pages/*/text_vector"
+            },
+            {
+              "name": "content_text",
+              "source": "/document/pages/*"
+            },             
+            {
+              "name": "document_title",
+              "source": "/document/document_title"
+            }      
+          ]
+        },
+        {
+          "targetIndexName": "demo-multimodal-index",
+          "parentKeyFieldName": "image_document_id",
+          "sourceContext": "/document/normalized_images/*",
+          "mappings": [    
+            {
+            "name": "content_text",
+            "source": "/document/normalized_images/*/verbalizedImage"
+            },  
+            {
+            "name": "content_embedding",
+            "source": "/document/normalized_images/*/verbalizedImage_vector"
+            },                                           
+            {
+              "name": "content_path",
+              "source": "/document/normalized_images/*/new_normalized_images/imagePath"
+            },                    
+            {
+              "name": "document_title",
+              "source": "/document/document_title"
+            },
+            {
+              "name": "location_metadata",
+              "source": "/document/normalized_images/*/new_normalized_images/location_metadata"
+            }            
+          ]
+        }
+      ],
+      "parameters": {
+        "projectionMode": "skipIndexingParentDocuments"
+      }
+  },
+   "knowledgeStore":{
+      "storageConnectionString":"{{storageConnection}}",
+      "identity":null,
+      "projections":[
+         {
+            "files":[
+               {
+                  "storageContainer":"{{imageProjectionContainer}}",
+                  "source":"/document/normalized_images/*"
+               }
+            ]
+         }
+      ]
+   }
+}
+```
+
+### [**Document layout & multimodal embedding**](#tab/doc-layout-vision)
+
+This pattern uses:
+
++ [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) for extraction and chunking.
+
++ [Azure AI Vision multimodal skill](cognitive-search-skill-vision-vectorize.md) for text and image embeddings.
+
+```json
+{
+   "name":"demo-multimodal-skillset",
+   "description":"A test skillset",
+   "skills":[
+      {
+         "@odata.type":"#Microsoft.Skills.Util.DocumentIntelligenceLayoutSkill",
+         "name":"document-layout-skill",
+         "description":"Document Intelligence skill for document cracking",
+         "context":"/document",
+         "outputMode":"oneToMany",
+         "outputFormat":"text",
+         "extractionOptions":[
+            "images",
+            "locationMetadata"
+         ],
+         "chunkingProperties":{
+            "unit":"characters",
+            "maximumLength":2000,
+            "overlapLength":200
+         },
+         "inputs":[
+            {
+               "name":"file_data",
+               "source":"/document/file_data"
+            }
+         ],
+         "outputs":[
+            {
+               "name":"text_sections",
+               "targetName":"text_sections"
+            },
+            {
+               "name":"normalized_images",
+               "targetName":"normalized_images"
+            }
+         ]
+      },
+      {
+         "@odata.type":"#Microsoft.Skills.Vision.VectorizeSkill",
+         "name":"text-embedding-skill",
+         "description":"Vision Vectorization skill for text",
+         "context":"/document/text_sections/*",
+         "modelVersion":"{{azureAiVisionModelVersion}}",
+         "inputs":[
+            {
+               "name":"text",
+               "source":"/document/text_sections/*/content"
+            }
+         ],
+         "outputs":[
+            {
+               "name":"vector",
+               "targetName":"text_vector"
+            }
+         ]
+      },
+      {
+         "@odata.type":"#Microsoft.Skills.Vision.VectorizeSkill",
+         "name":"image-embedding-skill",
+         "description":"Vision Vectorization skill for images",
+         "context":"/document/normalized_images/*",
+         "modelVersion":"{{azureAiVisionModelVersion}}",
+         "inputs":[
+            {
+               "name":"image",
+               "source":"/document/normalized_images/*"
+            }
+         ],
+         "outputs":[
+            {
+               "name":"vector",
+               "targetName":"image_vector"
+            }
+         ]
+      }
+   ],
+   "cognitiveServices":{
+      "@odata.type":"#Microsoft.Azure.Search.AIServicesByIdentity",
+      "subdomainUrl":"{{foundryUrl}}",
+      "identity":null
+   },
+   "indexProjections":{
+      "selectors":[
+         {
+            "targetIndexName":"demo-multimodal-index",
+            "parentKeyFieldName":"text_document_id",
+            "sourceContext":"/document/text_sections/*",
+            "mappings":[
+               {
+                  "name":"content_embedding",
+                  "source":"/document/text_sections/*/text_vector"
+               },
+               {
+                  "name":"content_text",
+                  "source":"/document/text_sections/*/content"
+               },
+               {
+                  "name":"locationMetadata",
+                  "source":"/document/text_sections/*/locationMetadata"
+               },
+               {
+                  "name":"document_title",
+                  "source":"/document/document_title"
+               }
+            ]
+         },
+         {
+            "targetIndexName":"demo-multimodal-index",
+            "parentKeyFieldName":"image_document_id",
+            "sourceContext":"/document/normalized_images/*",
+            "mappings":[
+               {
+                  "name":"content_embedding",
+                  "source":"/document/normalized_images/*/image_vector"
+               },
+               {
+                  "name":"content_path",
+                  "source":"/document/normalized_images/*/imagePath"
+               },
+               {
+                  "name":"document_title",
+                  "source":"/document/document_title"
+               },
+               {
+                  "name":"locationMetadata",
+                  "source":"/document/normalized_images/*/locationMetadata"
+               }
+            ]
+         }
+      ],
+      "parameters":{
+         "projectionMode":"skipIndexingParentDocuments"
+      }
+   },
+   "knowledgeStore":{
+      "storageConnectionString":"{{storageConnection}}",
+      "projections":[
+         {
+            "files":[
+               {
+                  "storageContainer":"{{imageProjectionContainer}}",
+                  "source":"/document/normalized_images/*"
+               }
+            ]
+         }
+      ]
+   }
+}
+```
+
+### [**Document layout & text embedding**](#tab/doc-layout-text)
+
+This pattern uses:
+
++ [Document Layout skill](cognitive-search-skill-document-intelligence-layout.md) for extraction and chunking.
+
++ [GenAI Prompt skill](cognitive-search-skill-genai-prompt.md) and [Azure OpenAI embedding skill](cognitive-search-skill-azure-openai-embedding.md) for textual descriptions of images and text embeddings.
+
+```json
+{
+   "name":"demo-multimodal-skillset",
+   "description":"A test skillset",
+   "skills":[
+      {
+         "@odata.type":"#Microsoft.Skills.Util.DocumentIntelligenceLayoutSkill",
+         "name":"document-cracking-skill",
+         "description":"Document Layout skill for document cracking",
+         "context":"/document",
+         "outputMode":"oneToMany",
+         "outputFormat":"text",
+         "extractionOptions":[
+            "images",
+            "locationMetadata"
+         ],
+         "chunkingProperties":{
+            "unit":"characters",
+            "maximumLength":2000,
+            "overlapLength":200
+         },
+         "inputs":[
+            {
+               "name":"file_data",
+               "source":"/document/file_data"
+            }
+         ],
+         "outputs":[
+            {
+               "name":"text_sections",
+               "targetName":"text_sections"
+            },
+            {
+               "name":"normalized_images",
+               "targetName":"normalized_images"
+            }
+         ]
+      },
+      {
+         "@odata.type":"#Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill",
+         "name":"text-embedding-skill",
+         "description":"Embedding skill for text",
+         "context":"/document/text_sections/*",
+         "inputs":[
+            {
+               "name":"text",
+               "source":"/document/text_sections/*/content"
+            }
+         ],
+         "outputs":[
+            {
+               "name":"embedding",
+               "targetName":"text_vector"
+            }
+         ],
+         "resourceUri":"{{textEmbeddingModelUri}}",
+         "deploymentId":"text-embedding-3-large",
+         "apiKey":"{{textEmbeddingModelKey}}",
+         "dimensions":3072,
+         "modelName":"text-embedding-3-large"
+      },
+      {
+         "@odata.type":"#Microsoft.Skills.Custom.ChatCompletionSkill",
+         "name":"genAI-prompt-skill",
+         "description":"GenAI Prompt skill for image verbalization",
+         "uri":"{{chatCompletionModelUri}}",
+         "timeout":"PT1M",
+         "apiKey":"{{chatCompletionModelKey}}",
+         "context":"/document/normalized_images/*",
+         "inputs":[
+            {
+               "name":"systemMessage",
+               "source":"='You are tasked with generating concise, accurate descriptions of images, figures, diagrams, or charts in documents. The goal is to capture the key information and meaning conveyed by the image without including extraneous details like style, colors, visual aesthetics, or size.\n\nInstructions:\nContent Focus: Describe the core content and relationships depicted in the image.\n\nFor diagrams, specify the main elements and how they are connected or interact.\nFor charts, highlight key data points, trends, comparisons, or conclusions.\nFor figures or technical illustrations, identify the components and their significance.\nClarity & Precision: Use concise language to ensure clarity and technical accuracy. Avoid subjective or interpretive statements.\n\nAvoid Visual Descriptors: Exclude details about:\n\nColors, shading, and visual styles.\nImage size, layout, or decorative elements.\nFonts, borders, and stylistic embellishments.\nContext: If relevant, relate the image to the broader content of the technical document or the topic it supports.\n\nExample Descriptions:\nDiagram: \"A flowchart showing the four stages of a machine learning pipeline: data collection, preprocessing, model training, and evaluation, with arrows indicating the sequential flow of tasks.\"\n\nChart: \"A bar chart comparing the performance of four algorithms on three datasets, showing that Algorithm A consistently outperforms the others on Dataset 1.\"\n\nFigure: \"A labeled diagram illustrating the components of a transformer model, including the encoder, decoder, self-attention mechanism, and feedforward layers.\"'"
+            },
+            {
+               "name":"userMessage",
+               "source":"='Please describe this image.'"
+            },
+            {
+               "name":"image",
+               "source":"/document/normalized_images/*/data"
+            }
+         ],
+         "outputs":[
+            {
+               "name":"response",
+               "targetName":"verbalizedImage"
+            }
+         ]
+      },
+      {
+         "@odata.type":"#Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill",
+         "name":"verbalized-image-embedding-skill",
+         "description":"Embedding skill for verbalized images",
+         "context":"/document/normalized_images/*",
+         "inputs":[
+            {
+               "name":"text",
+               "source":"/document/normalized_images/*/verbalizedImage",
+               "inputs":[
+                  
+               ]
+            }
+         ],
+         "outputs":[
+            {
+               "name":"embedding",
+               "targetName":"verbalizedImage_vector"
+            }
+         ],
+         "resourceUri":"{{textEmbeddingModelUri}}",
+         "deploymentId":"text-embedding-3-large",
+         "apiKey":"{{textEmbeddingModelKey}}",
+         "dimensions":3072,
+         "modelName":"text-embedding-3-large"
+      }
+   ],
+   "indexProjections":{
+      "selectors":[
+         {
+            "targetIndexName":"demo-multimodal-index",
+            "parentKeyFieldName":"text_document_id",
+            "sourceContext":"/document/text_sections/*",
+            "mappings":[
+               {
+                  "name":"content_embedding",
+                  "source":"/document/text_sections/*/text_vector"
+               },
+               {
+                  "name":"content_text",
+                  "source":"/document/text_sections/*/content"
+               },
+               {
+                  "name":"locationMetadata",
+                  "source":"/document/text_sections/*/locationMetadata"
+               },
+               {
+                  "name":"document_title",
+                  "source":"/document/document_title"
+               }
+            ]
+         },
+         {
+            "targetIndexName":"demo-multimodal-index",
+            "parentKeyFieldName":"image_document_id",
+            "sourceContext":"/document/normalized_images/*",
+            "mappings":[
+               {
+                  "name":"content_text",
+                  "source":"/document/normalized_images/*/verbalizedImage"
+               },
+               {
+                  "name":"content_embedding",
+                  "source":"/document/normalized_images/*/verbalizedImage_vector"
+               },
+               {
+                  "name":"content_path",
+                  "source":"/document/normalized_images/*/imagePath"
+               },
+               {
+                  "name":"document_title",
+                  "source":"/document/document_title"
+               },
+               {
+                  "name":"locationMetadata",
+                  "source":"/document/normalized_images/*/locationMetadata"
+               }
+            ]
+         }
+      ],
+      "parameters":{
+         "projectionMode":"skipIndexingParentDocuments"
+      }
+   },
+   "cognitiveServices":{
+      "@odata.type":"#Microsoft.Azure.Search.AIServicesByIdentity",
+      "subdomainUrl":"{{foundryUrl}}",
+      "identity":null
+   },
+   "knowledgeStore":{
+      "storageConnectionString":"{{storageConnection}}",
+      "projections":[
+         {
+            "files":[
+               {
+                  "storageContainer":"{{imageProjectionContainer}}",
+                  "source":"/document/normalized_images/*"
+               }
+            ]
+         }
+      ]
+   }
+}
+```
+
+---
+
+## Run the indexer
+
+[Create Indexer](/rest/api/searchservice/indexers/create) creates an indexer on your search service. An indexer connects to the data source, loads data, runs a skillset, and indexes the enriched content.
+
+```http
+### Create and run an indexer
+POST {{searchUrl}}/indexers?api-version=2025-11-01-preview   HTTP/1.1
+  Content-Type: application/json
+  Authorization: Bearer {{token}}
+
+{
+  "name": "demo-multimodal-indexer",
+  "dataSourceName": "demo-multimodal-ds",
+  "targetIndexName": "demo-multimodal-index",
+  "skillsetName": "demo-multimodal-skillset",
+  "parameters": {
+    "maxFailedItems": -1,
+    "maxFailedItemsPerBatch": 0,
+    "batchSize": 1,
+    "configuration": {
+      "allowSkillsetToReadFileData": true
+    }
+  },
+  "fieldMappings": [
+    {
+      "sourceFieldName": "metadata_storage_name",
+      "targetFieldName": "document_title"
+    }
+  ],
+  "outputFieldMappings": []
+}
+```
+
+## Run queries
+
+You can start searching as soon as the first document is loaded. This is an unspecified full-text search query that returns all of the fields marked as retrievable in the index, along with a document count.
+
+> [!TIP]
+> The `content_embedding` field contains over a thousand dimensions. Use a `select` statement to exclude that field from the response by explicitly choosing all of the other fields. Adjust the select statement to match the fields (`location_metadata` vs `locationMetadata`) in your index. Here's an example: `"select": "content_id, text_document_id, document_title, image_document_id, content_text,`
+>
+
+```http
+### Query the index
+POST {{searchUrl}}/indexes/demo-multimodal-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
+  Content-Type: application/json
+  Authorization: Bearer {{token}}
+  
+  {
+    "search": "*",
+    "count": true
+  }
+```
+
+Send the request. The response should look like:
+
+```json
+HTTP/1.1 200 OK
+Transfer-Encoding: chunked
+Content-Type: application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8
+Content-Encoding: gzip
+Vary: Accept-Encoding
+Server: Microsoft-IIS/10.0
+Strict-Transport-Security: max-age=2592000, max-age=15724800; includeSubDomains
+Preference-Applied: odata.include-annotations="*"
+OData-Version: 4.0
+request-id: 712ca003-9493-40f8-a15e-cf719734a805
+elapsed-time: 198
+Date: Wed, 30 Apr 2025 23:20:53 GMT
+Connection: close
+
+{
+  "@odata.count": 100,
+  "@search.nextPageParameters": {
+    "search": "*",
+    "count": true,
+    "skip": 50
+  },
+  "value": [
+  ],
+  "@odata.nextLink": "https://<YOUR-SEARCH-SERVICE-NAME>.search.windows.net/indexes/demo-multimodal-index/docs/search?api-version=2025-11-01-preview "
+}
+```
+
+100 documents are returned in the response.
+
+### Query for image-only content
+
+Use a filter to exclude all non-image content. The `$filter` parameter only works on fields that were marked filterable during index creation.
+
+For filters, you can also use logical operators (and, or, not) and comparison operators (eq, ne, gt, lt, ge, le). String comparisons are case-sensitive. For more information and examples, see [Examples of simple search queries](search-query-simple-examples.md).
+
+```http
+POST {{searchUrl}}/indexes/demo-multimodal-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
+  Content-Type: application/json
+  Authorization: Bearer {{token}}
+  
+  {
+    "search": "*",
+    "count": true,
+    "filter": "image_document_id ne null"
+  }
+```
+
+Search results containing image-only content don't have text content, so you can exclude text fields.
+
+The `content_embedding` field contains high-dimensional vectors (typically 1,000 to 3,000 dimensions) for both page text and verbalized image descriptions. Exclude this field from the query.
+
+The `content_path` field contains the relative path to the image file within the designated image projection container. This field is generated only for images extracted from PDFs when `imageAction` is set to `generateNormalizedImages`, and can be mapped from the enriched document from the source field `/document/normalized_images/*/imagePath`. 
+
+For PDF context extracted using the Text Split skill, the Shaper skill adds the container name to the path and the location metadata.
+
+### Query for content related to "energy"
+
+Query for text or images with content related to energy, returning the content ID, parent document, and text (only populated for text chunks), and the content path where the image is saved in the knowledge store (only populated for images).
+
+This query is full-text search only, but you can [query the vector field](vector-search-how-to-query.md) for similarity search.
+
+```http
+POST {{searchUrl}}/indexes/demo-multimodal-index/docs/search?api-version=2025-11-01-preview   HTTP/1.1
+  Content-Type: application/json
+  Authorization: Bearer {{token}}
+  
+
+  {
+    "search": "energy",
+    "count": true
+  }
+```
+
+### Reset and rerun
+
+Indexers can be reset to clear the high-water mark, which allows a full rebuild. The following POST requests are for reset, followed by rerun.
+
+```http
+### Reset the indexer
+POST {{searchUrl}}/indexers/demo-multimodal-indexer/reset?api-version=2025-11-01-preview   HTTP/1.1
+  Content-Type: application/json
+  Authorization: Bearer {{token}}
+```
+
+```http
+### Run the indexer
+POST {{searchUrl}}/indexers/demo-multimodal-indexer/run?api-version=2025-11-01-preview   HTTP/1.1
+  Content-Type: application/json
+  Authorization: Bearer {{token}}
+```
+
+```http
+### Check indexer status 
+GET {{searchUrl}}/indexers/demo-multimodal-indexer/status?api-version=2025-11-01-preview   HTTP/1.1
+  Content-Type: application/json
+  Authorization: Bearer {{token}}
+```
+
+### View images in the knowledge store
+
+Recall that the skillset in this tutorial creates a [knowledge store](knowledge-store-concept-intro.md) for image content extracted from the PDF. After the indexer runs, the **sustainable-ai-pdf-images** container should have approximately 23 images. 
+
+You can't return these images in a search query. However, you can write application code that calls the Azure Storage APIs to retrieve the images if you need them for the user experience. The `content_path` field has the path to each image.
+
+To view the images in the Storage Browser:
+
+1. Sign in to the Azure portal and navigate to your Storage account.
+
+1. In Storage Browser, expand the sustainable-ai-pdf-images container.
+
+1. Select an image.
+
+1. In the far right menu (...), select **View/Edit**.
+
+:::image type="content" source="media/tutorial-multimodal/normalized-image-in-storage.png" alt-text="Screenshot of an image extracted from the PDF document." lightbox="media/tutorial-multimodal/normalized-image-in-storage.png" :::
+
+## Clean up resources
+
+[!INCLUDE [clean up resources (paid)](includes/resource-cleanup-paid.md)]
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "マルチモーダルチャンクおよび埋め込みに関するチュートリアルの追加"
}
```

### Explanation
この変更では、`articles/search/tutorial-multimodal.md`ファイルが新たに追加され、マルチモーダルコンテンツの抽出、チャンク化、インデックス作成、および検索に関する詳細な指導が提供されるチュートリアルが含まれています。このチュートリアルは、Azure AI Searchを通じて、テキストと画像データの処理を行うプロセスを組み合わせて教育することを目的としています。

チュートリアルでは、マルチモーダルインデクシングのパイプラインを構築する手順が説明されており、具体的には以下のタスクが含まれます：
- テキストと画像の抽出およびチャンク化
- テキストと画像のベクター化を通じた類似検索
- アプリケーションによる利用のために、切り抜かれた画像を知識ストアに送信すること

さらに、異なるスキルセットを横並びで表示し、マルチモーダルコンテンツをさまざまな方法で抽出、チャンク化、ベクター化する方法が示されています。

この新しいチュートリアルは、ユーザーがマルチモーダルデータを効果的に処理できるようにするための重要なリソースとなります。なお、前提条件としてAzure AI SearchやAzure Storage、Microsoft Foundryリソースの設定が必要であることも説明されています。

## articles/search/vector-store.md{#item-db9b8c}

<details>
<summary>Diff</summary>
````diff
@@ -245,7 +245,7 @@ Azure provides a [monitoring platform](monitor-azure-cognitive-search.md) that i
 
 ### Secure access to vector data
 
-Azure AI Search implements data encryption, private connections for no-internet scenarios, and role assignments for secure access through Microsoft Entra ID. For more information about enterprise security features, see [Security in Azure AI Search](search-security-overview.md).
+Azure AI Search implements data encryption, private connections for no-internet scenarios, and role assignments for secure access through Microsoft Entra ID. For more information about enterprise security features, see [Data, privacy, and built-in protections](search-security-built-in.md).
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトルデータへの安全なアクセスに関する情報の更新"
}
```

### Explanation
この変更では、`articles/search/vector-store.md`ファイルの一部が修正され、ベクトルデータへの安全なアクセスに関連する文言が更新されました。具体的には、Azure AI Searchのセキュリティ機能に関する記述が変更され、役割の割り当てやデータの暗号化、インターネット不要のシナリオにおけるプライベート接続などの機能が説明されています。

元々の文言は「Azure AI Search implements data encryption, private connections for no-internet scenarios, and role assignments for secure access through Microsoft Entra ID. For more information about enterprise security features, see [Security in Azure AI Search](search-security-overview.md).」であったのが、変更後は「Azure AI Search implements data encryption, private connections for no-internet scenarios, and role assignments for secure access through Microsoft Entra ID. For more information about enterprise security features, see [Data, privacy, and built-in protections](search-security-built-in.md).」に改訂されました。この変更は、情報の正確性や関連性を向上させるために行われたものであり、特にデータのプライバシーおよび保護に関する最新のリソースを参照できるようになっています。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -60,7 +60,7 @@ Learn about the latest updates to Azure AI Search functionality, docs, and sampl
 | September | General availability | [Truncate dimensions](vector-search-how-to-truncate-dimensions.md). |
 | September | General availability | [Unpack `@search.score` to view subscores in hybrid search results](hybrid-search-ranking.md#unpack-a-search-score-into-subscores). | 
 | September | Portal update | The Azure portal is undergoing a three-phase rollout to [unify the two import wizards](search-import-data-portal.md). For Phase 1, the **Import and vectorize data** wizard has been renamed to **Import data (new)** and redeveloped to support keyword search, modernizing the legacy **Import data** workflow with an improved interface and user experience.<p>**Import data (new)** isn't a direct replacement for the old wizard. For example, it supports fewer skills for keyword search.<p>Both wizards are currently available, but **Import data** will be deprecated in a future phase. |
-| September | Security | [Support for Azure confidential computing](search-security-overview.md#data-in-use). Configure [confidential computing](/azure/confidential-computing/use-cases-scenarios) during service creation to process data in use on confidential VMs. This compute type isn't intended for general use, but rather for stringent regulatory, compliance, or security requirements.<p>Confidential computing adds a 10% surcharge to the base cost of billable tiers. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/search/).<p>Now generally available through the 2025-05-01 version of [Services - Create or Update (REST API)](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2025-05-01&preserve-view=true) and the [Azure portal](search-create-service-portal.md#choose-a-compute-type). |
+| September | Security | [Support for Azure confidential computing](search-security-best-practices.md#optional-enable-confidential-computing). Configure [confidential computing](/azure/confidential-computing/use-cases-scenarios) during service creation to process data in use on confidential VMs. This compute type isn't intended for general use, but rather for stringent regulatory, compliance, or security requirements.<p>Confidential computing adds a 10% surcharge to the base cost of billable tiers. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/search/).<p>Now generally available through the 2025-05-01 version of [Services - Create or Update (REST API)](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2025-05-01&preserve-view=true) and the [Azure portal](search-create-service-portal.md#choose-a-compute-type). |
 | August | REST API | [Search Service 2025-08-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-08-01-preview&preserve-view=true). New preview REST API version providing programmatic access to the data plane operations described in this table. |
 | August | Agentic retrieval | [Knowledge agents (preview)](agentic-retrieval-how-to-create-knowledge-base.md). Architectural changes to the knowledge agent definition, which now requires one or more `knowledgeSources` instead of `targetIndexes` and deprecates `defaultMaxDocsForReranker`. New `retrievalInstructions` and `outputConfiguration` properties provide greater control over query planning and execution. For help with breaking changes, see [Migrate your agentic retrieval code](agentic-retrieval-how-to-migrate.md). |
 | August | Agentic retrieval | [Knowledge sources (preview)](agentic-knowledge-source-overview.md). New REST APIs for creating and managing knowledge sources, which represent content that knowledge agents use to ground and answer queries. In this preview, you can create knowledge sources for [search indexes](agentic-knowledge-source-how-to-search-index.md) and [Azure blobs](agentic-knowledge-source-how-to-blob.md).  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Confidential Computingに関するセクションの参照先を更新"
}
```

### Explanation
この変更では、`articles/search/whats-new.md`ファイル内のAzure Confidential Computingに関連する文言が修正され、セクションが新しい参照先に更新されました。具体的には、「[Support for Azure confidential computing](search-security-overview.md#data-in-use)」というリンクが「[Support for Azure confidential computing](search-security-best-practices.md#optional-enable-confidential-computing)」に変更されています。

修正が施された部分では、Azureの機密コンピューティングが提供するセキュリティ機能について説明されており、機密VM上でのデータ処理を可能にするため、サービス作成時に機密コンピューティングを設定する方法が示されています。この機能は、一般的な使用を目的とせず、厳しい規制、コンプライアンス、またはセキュリティ要件のために設計されています。

また、この機能には10%の追加料金がかかることや、2025年5月1日のバージョンのREST APIおよびAzureポータルで一般提供が開始されることも言及されています。これにより、ユーザーは最新の情報に基づいて機密コンピューティングの機能を適切に利用できるように改善されています。


