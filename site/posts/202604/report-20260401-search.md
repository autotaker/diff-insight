---
date: '2026-04-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f3c79c0...MicrosoftDocs:98210c1
summary: この変更では、Azure AI Searchのセキュリティ関連のベストプラクティスに関する文書が更新され、主にドキュメントレベルのアクセスコントロールに関する新機能やセキュリティフィルターのプレビュー機能が追加されました。この更新により、ユーザーはアイデンティティに基づいてドキュメントへのアクセスを細かく制御できるようになり、クラウド環境でのセキュリティ管理が強化されます。互換性を壊す変更は含まれておらず、関連情報へのリンクも更新されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f3c79c0...MicrosoftDocs:98210c1){target="_blank"}

# ハイライト
この変更では、Azure AI Searchのセキュリティ関連のベストプラクティスに関する文書が更新されました。主な新機能には、POSIX風ACLとRBACスコープ、Microsoft 365のSharePoint ACLの使用、そしてセキュリティフィルターの新しいプレビュー機能が含まれます。これにより、ユーザーはアイデンティティに基づいてドキュメントのアクセスをより細かく制御できるようになりました。

## 新機能
- ドキュメントレベルのアクセスコントロールに関する詳細な説明が追加されました。
- Azure Data Lake Storage Gen2とMicrosoft 365のSharePointのACLによるアクセス制御設定が導入されました。
- セキュリティフィルターの使用による新しいプレビュー機能が追加されました。

## 互換性を壊す変更
このドキュメント更新には互換性を壊す変更は含まれていません。

## その他の更新
関連する情報を得るためのリンクが更新されています。

# 洞察
このドキュメント変更の背景には、クラウド環境でのセキュリティ管理がますます重要となってきていることが挙げられます。Azure AI Searchを使用するユーザーが直面するセキュリティの課題は、多くの場合、企業の持つ様々なデータストレージにわたるアクセス制御と直接関係しています。今回の更新で取り上げられている機能は、特に一部のデータに対して細かくアクセスを制御したい企業にとって有用です。

POSIX風のACLやRBACスコープを用いることで、システム管理者は詳細なレベルで権限委任を行え、Microsoft 365のSharePoint ACLを活用することで、組織内のドキュメント管理がよりシームレスになります。また、セキュリティフィルターが新たに導入されたことで、ユーザーのアイデンティティやグループ情報に基づき、検索結果のフィルタリングが可能になり、セキュリティポリシーの実効性が向上します。

このような機能拡充により、Azure AI Searchのユーザーはセキュアな環境で業務を遂行でき、データの機密性や完全性を守りながら、必要な情報へのアクセスを管理することが容易になります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-security-best-practices.md](#item-9dd4cd) | minor update | セキュリティベストプラクティスの更新 | modified | 23 | 10 | 33 | 


# Modified Contents
## articles/search/search-security-best-practices.md{#item-9dd4cd}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ description: Learn how to configure security features in Azure AI Search to prot
 ms.service: azure-ai-search
 ms.update-cycle: 180-days
 ms.topic: how-to
-ms.date: 02/24/2026
+ms.date: 03/30/2026
 ai-usage: ai-assisted
 ms.custom: horz-security
 ---
@@ -19,6 +19,8 @@ As a solutions architect, you should configure security controls across three do
 - **Authentication and authorization**: Define how, who, and what can access your search service and data.
 - **Data protection**: Implement encryption, access controls, and monitoring.
 
+[!INCLUDE [Security horizontal Zero Trust statement](~/reusable-content/ce-skilling/azure/includes/security/zero-trust-security-horizontal.md)]
+
 ## Understand network traffic patterns
 
 Before you configure network security, understand the three network traffic patterns in Azure AI Search:
@@ -174,15 +176,23 @@ For basic retrieval-augmented generation (RAG) patterns where your client applic
 
 ## Implement document-level access control
 
-User permissions at the document level, also known as *row-level security*, control which documents users can access through query execution.
+Document-level access control, also known as row-level security, restricts which documents a user can retrieve based on their identity. Permission metadata is captured during indexing and enforced at query time, which is essential for agentic AI systems, RAG applications, and enterprise search solutions that require authorization checks at the document level. For a comprehensive overview of all supported approaches, see [Document-level access control](search-document-level-access-overview.md).
+
+### Use POSIX-like ACL and RBAC scopes (preview)
+
+For Azure Data Lake Storage (ADLS) Gen2 content, configure indexers or knowledge sources to preserve POSIX-like ACL permissions and RBAC scopes during ingestion. At query time, results are filtered based on the caller's Microsoft Entra token. For more information, see [Index ADLS Gen2 permission metadata](search-indexer-access-control-lists-and-role-based-access.md).
 
-### Configure document-level security
+### Use SharePoint in Microsoft 365 ACLs (preview)
 
-Configure fine-grained permissions at the document level, from data ingestion through query execution. This capability is essential for building secure AI agentic systems grounding data, RAG applications, and enterprise search solutions that require authorization checks at the document level. For more information, see [Document-level access control](search-document-level-access-overview.md).
+Configure the SharePoint in Microsoft 365 indexer to extract document permissions directly from SharePoint ACLs during ingestion. At query time, results are filtered based on the caller's Microsoft Entra token. During this preview, ACLs are captured only during initial indexing, so you must reindex affected documents if source permissions change to avoid stale access. For more information, see [Index SharePoint permission metadata](search-indexer-sharepoint-access-control-lists.md).
 
 ### Use sensitivity labels (preview)
 
-Configure an indexer to automatically detect Microsoft Purview sensitivity labels during indexing and apply label-based access controls when queries are executed. For more information, see [Sensitivity labels](search-indexer-sensitivity-labels.md).
+Configure an indexer to automatically detect Microsoft Purview sensitivity labels during indexing and apply label-based access controls when queries are executed. This capability aligns Azure AI Search authorization with your enterprise's Microsoft Information Protection model. For more information, see [Index Microsoft Purview sensitivity labels](search-indexer-sensitivity-labels.md).
+
+### Use security filters
+
+For scenarios where native ACL integration isn't viable, implement security filters to trim results based on user or group identities. Store identity information in a string field in your index, and then pass the caller's identity as a filter string at query time to exclude documents that don't match. This approach works with custom access models or non-Microsoft security frameworks. For more information, see [Security filters for trimming results](search-security-trimming-for-azure-search.md).
 
 ## Configure data encryption
 
@@ -273,8 +283,11 @@ Use this checklist to ensure you've configured appropriate security controls:
 
 **Data protection**:
 
-- [ ] Configured document-level access control (if required)
-- [ ] Configured sensitivity labels (if applicable)
+- [ ] Configured document-level access control (if required):
+  - [ ] POSIX-like ACLs for ADLS Gen2 content
+  - [ ] SharePoint in Microsoft 365 ACLs
+  - [ ] Microsoft Purview sensitivity labels
+  - [ ] Security filters for custom scenarios
 - [ ] Implemented CMK encryption (if required)
 - [ ] Evaluated confidential computing requirements (if applicable)
 
@@ -288,6 +301,6 @@ Use this checklist to ensure you've configured appropriate security controls:
 
 ## Related content
 
-+ [Data, privacy, and built-in protections in Azure AI Search](search-security-built-in.md)
-+ [Azure security fundamentals](/azure/security/fundamentals/)
-+ [Shared responsibility in the cloud](/azure/security/fundamentals/shared-responsibility)
+- [Data, privacy, and built-in protections in Azure AI Search](search-security-built-in.md)
+- [Azure security fundamentals](/azure/security/fundamentals/)
+- [Shared responsibility in the cloud](/azure/security/fundamentals/shared-responsibility)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セキュリティベストプラクティスの更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるセキュリティ機能に関連するベストプラクティスに関する文書の修正です。主な改訂内容として、日付の更新やドキュメントレベルのアクセスコントロールに関する説明の強化が含まれています。また、POSIX風のACLやRBACスコープ、Microsoft 365のSharePoint ACL、そしてセキュリティフィルターの使用に関する新しいプレビュー機能が追加されました。

具体的には、次の点が強調されました：
- ドキュメントレベルのアクセスコントロールについての詳細が拡充され、アイデンティティに基づいてユーザーが取得できるドキュメントを制限する方法が説明されています。
- Azure Data Lake Storage Gen2とMicrosoft 365のSharePointのACLを用いたアクセス管理の設定方法が追加されています。
- セキュリティフィルターを用いて、ユーザーやグループのアイデンティティに基づいて結果をトリミングする新しい方法の導入が含まれています。

これらの変更により、Azure AI Searchのセキュリティ機能に対する理解が深まり、ユーザーがより適切にセキュリティを管理できるようになります。さらなる情報を得るための関連リンクも更新されています。


