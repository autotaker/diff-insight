---
date: '2025-09-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8392214...MicrosoftDocs:3a8933d
summary: このコード差分は、Azureの認知検索に関する3つの記事のマイナーな更新を含んでいます。主な変更点は、記事の日付の更新、新しいエラーセクションの追加、デバッグセッションに関する情報の追加、スキルの制限に関する明確化です。特に、「仮想ネットワーク/ファイアウォールルールへのアクセスが拒否される」という新しいエラーセクションが追加され、ユーザーがインデクサー設定に関連する問題に対処できるようになります。デバッグセッションに関する更新やドキュメントインテリジェンスの警告も、ユーザーエクスペリエンスの向上に寄与するものです。全体として、この更新はAzureの認知検索における情報を強化し、ユーザーが直面する可能性のある問題への対処を支援することを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8392214...MicrosoftDocs:3a8933d){target="_blank"}

# ハイライト
このコード差分は、Azureの認知検索に関連する3つの記事に対するマイナーな更新を含んでいます。主な変更点は記事の日付の更新、新しいエラーに関するセクションの追加、デバッグセッションに関する情報追加、およびスキルの制限に関する明確化です。

## 新機能
- 新たに「仮想ネットワーク/ファイアウォールルールへのアクセスが拒否される」というエラーセクションが追加されました。これはインデクサー設定に関連した問題に対処するためのものです。

## 破壊的変更
特に破壊的な変更は報告されていません。

## その他の更新
- 各記事の日付が最新のものに更新されました。
- デバッグセッションに関して、文書選択機能の利用不可についての情報が追加されました。
- ドキュメントインテリジェンススキルに関連して、処理時間に関する新しい警告が追加されました。

# インサイト
このコード差分によって、Azureの認知検索に関するドキュメントがより現実的な利用状況に対応するために更新されています。特に、新しく追加されたエラー情報は、ユーザーがインデクサーが直面する可能性のあるアクセス制限問題に対処するのに役立ちます。これは、Azureのリソースへのアクセス権を管理する際に、ファイアウォールやプライベートエンドポイントの設定がどのように影響するかを理解するのに重要です。

デバッグセッションに関する記事の更新は、現在のセッション機能がどのように制限されているかを明確にし、ユーザーがデバッグを行う際の判断を支援します。機能制限が一時的であるという記述は、将来の改善に対する期待感をユーザーに与えるものです。

さらに、ドキュメントインテリジェンスのレイアウト処理に関する警告は、Azure AI Document Intelligenceを使用する際の適切なドキュメントサイズや形式について、ユーザーに実用的なガイダンスを提供します。これにより、ユーザーは解析効率を最大化し、タイムアウトによる不必要なコストを避けることが可能です。

全体として、この更新はAzureの認知検索環境でユーザーが直面する可能性のある問題を予測し、適切に対処するための情報を増強するものであり、ユーザーエクスペリエンスの向上を目的としています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-common-errors-warnings.md](#item-a5c854) | minor update | 記事の更新: 認知検索の一般的なエラーと警告 | modified | 11 | 1 | 12 | 
| [cognitive-search-debug-session.md](#item-edf092) | minor update | 記事の更新: 認知検索のデバッグセッション | modified | 5 | 2 | 7 | 
| [cognitive-search-skill-document-intelligence-layout.md](#item-62c06f) | minor update | 記事の更新: 認知検索スキル - ドキュメントインテリジェンスのレイアウト | modified | 3 | 2 | 5 | 


# Modified Contents
## articles/search/cognitive-search-common-errors-warnings.md{#item-a5c854}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 02/19/2025
+ms.date: 09/21/2025
 ms.update-cycle: 180-days
 ---
 
@@ -423,3 +423,13 @@ This error usually happens in Azure SQL indexers when the source column type use
 For example, if the column used for change detection is of type datetime, but the indexer expects a rowversion type because convertHighWaterMarkToRowVersion is enabled, the mismatch will cause an error.
 
 Check the data type for the 'High Water Mark' column in the source and update the indexer configuration accordingly. Once verified and updated, reset and rerun the indexer to process the column values.
+
+## `Error: Access denied to Virtual Network/Firewall rules.`
+
+This error typically occurs due to one of the following:
+- Firewall restrictions on Azure resources required by your indexer, depending on your configuration. These resources may include: the [data source](search-data-sources-gallery.md#generally-available-data-sources-by-azure-ai-search), Azure Storage account (used for [debug sessions](cognitive-search-debug-session.md), [incremental enrichment](cognitive-search-incremental-indexing-conceptual.md) or [knowledge store](knowledge-store-concept-intro.md)), Azure Function (used for [web API custom skills](cognitive-search-custom-skill-web-api.md)) or AI Services / AI Foundry deployments used during [AI enrichment](cognitive-search-concept-intro.md).
+- Private endpoint configurations that block access from the indexer to those resources.
+
+Ensure that the indexer has access to your setup components by reviewing your resource configurations to confirm they allow traffic to all required services:
+- [Firewall and IP restriction settings](search-indexer-howto-access-ip-restricted.md)
+- [Shared private link setup](search-indexer-howto-access-private.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事の更新: 認知検索の一般的なエラーと警告"
}
```

### Explanation
このコードの変更は、Azureの認知検索の一般的なエラーと警告に関する記事を更新するもので、具体的には、日付の更新と新しいエラーのセクションの追加が含まれています。変更の詳細は、記事の最初の部分で、日付が2025年の2月19日から9月21日に変更されています。また、新たに「仮想ネットワーク/ファイアウォールルールへのアクセスが拒否される」というエラーについての情報が追加されました。このエラーが発生する理由は、インデクサーの設定に依存するAzureリソースに対するファイアウォールの制限や、インデクサーがリソースにアクセスするためのプライベートエンドポイント設定の問題です。この更新により、読者は新たなエラーの内容とその解決方法に関する情報を得られるようになります。

## articles/search/cognitive-search-debug-session.md{#item-edf092}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 04/10/2025
+ms.date: 09/21/2025
 ms.update-cycle: 365-days
 ---
 
@@ -55,7 +55,7 @@ Debug Sessions work with all generally available [indexer data sources](search-d
 
 + Data sources with encryption enabled via [customer managed keys (CMK)](search-security-manage-encryption-keys.md).
   
-+ Currently, the ability to select which document to debug is unavailable. This limitation isn't permanent and will be lifted soon. At this time, Debug Sessions selects the first document in the source data container or folder.
++ Currently, the ability to select which document to debug is unavailable. This limitation isn't permanent and should be lifted soon. At this time, Debug Sessions selects the first document in the source data container or folder.
 
 ## How a debug session works
 
@@ -65,6 +65,9 @@ A cached copy of the enriched document and skillset is loaded into the visual ed
 
 If the enrichment pipeline doesn't have any errors, a debug session can be used to incrementally enrich a document, test and validate each change before committing the changes.
 
+Debug sessions help identify the root cause of errors or warnings by analyzing the data, skill inputs and outputs, and field mappings. If the indexer encounters configuration issues, such as incorrect network setup, permission-related access errors, or similar, please review the specific error message along with the linked documentation provided. For troubleshooting guidance, refer to the [common indexer errors and warnings](cognitive-search-common-errors-warnings.md).
+
+
 ## Debug session layout
 
 The visual editor is organized into a surface area showing a progression of operations, starting with document cracking, followed by skills, mappings, and an index.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事の更新: 認知検索のデバッグセッション"
}
```

### Explanation
このコードの変更は、Azureの認知検索デバッグセッションに関する記事の更新を示しています。修正は主に日付の更新と情報の追加に集中しています。具体的には、記事の日付が2025年4月10日から2025年9月21日に変更され、デバッグセッションの新しい機能や制限についての説明が強化されています。特に、文書を選択してデバッグする機能が現在は利用できないことが明記され、その制限が永久的でないことが強調されています。また、デバッグセッションがエラーや警告の根本原因を特定するのに役立つこと、及びインデクサーが直面する可能性のある設定問題についても新しい説明が追加されています。この更新により、読者はデバッグセッションの機能についてより深く理解できるようになります。

## articles/search/cognitive-search-skill-document-intelligence-layout.md{#item-62c06f}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: reference
-ms.date: 07/10/2025
+ms.date: 09/19/2025
 ms.update-cycle: 365-days
 ---
 
@@ -34,9 +34,10 @@ This skill is bound to a [billable Azure AI multi-service resource](cognitive-se
 
 ## Limitations
 
-During the public preview, this skill has the following restrictions:
+This skill has the following limitations:
 
 + The skill isn't suitable for large documents requiring more than 5 minutes of processing in the AI Document Intelligence layout model. The skill times out, but charges still apply to the AI Services multi-services resource if it attaches to the skillset for billing purposes. Ensure documents are optimized to stay within processing limits to avoid unnecessary costs.
++ Since this skill calls the Azure AI Document Intelligence layout model, all documented [service behaviors for different document types](/azure/ai-services/document-intelligence/prebuilt/layout#pages) for different file types apply to its output. For example, Word (DOCX) and PDF files may produce different results due to differences in how images are handled. If consistent image behavior across DOCX and PDF is required, consider converting documents to PDF or reviewing the [multimodal search documentation](multimodal-search-overview.md) for alternative approaches.
 
 ## Supported regions
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事の更新: 認知検索スキル - ドキュメントインテリジェンスのレイアウト"
}
```

### Explanation
このコードの変更は、Azureの認知検索スキルに関するドキュメントインテリジェンスのレイアウトの記事を更新するもので、主に日付の変更と情報の明確化が含まれています。修正された日付は2025年7月10日から2025年9月19日に変更されています。また、「制限」セクションの内容が更新され、スキルの処理時間に関する新たな警告が追加されました。具体的には、処理に5分以上かかる大きな文書には適さないこと、スキルがタイムアウトする可能性があること、そしてその場合も請求が発生することが強調されています。また、スキルがAzure AI Document Intelligenceのレイアウトモデルを使用するため、異なるファイルタイプ（たとえば、DOCXとPDF）によるサービスの振る舞いの違いについても明示されています。これにより、ユーザーは処理の最適化や文書形式に関する考慮事項についてより良い理解を得られるようになります。


