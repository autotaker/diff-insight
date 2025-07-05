---
date: '2025-07-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3866070...MicrosoftDocs:961769c
summary: このレポートでは、Azure関連ドキュメントの複数のセクションに対するマイナーアップデートについて説明しています。主な変更点としては、セクションヘッダーの短縮と明確化、ファイル参照パスの修正、新しいセクションや内容の追加があります。特にセマンティックハイブリッド検索やADLS
  Gen2とAzure AI Searchの統合に関する情報が強化され、ユーザー体験が向上しています。破壊的変更はありませんが、一部のユーザーには内容の再確認が必要となるかもしれません。全体として、これらの改善はドキュメントの情報整合性とユーザーエクスペリエンスを高め、Azureサービスの信頼性を向上させることを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3866070...MicrosoftDocs:961769c){target="_blank"}

<format>
# Highlights
以下の変更では、Azure関連ドキュメントの複数のセクションがマイナーアップデートされ、情報の明瞭性と整合性が向上しています。主な変更点は、セクションヘッダーの短縮と明確化、ファイル参照パスの修正、新しいセクションや内容の追加などです。

## New features
- セマンティックハイブリッド検索の概念に関する詳細が強化され、ユーザーが検索の実行と結果の理解を向上させる内容が追加されました。
- ADLS Gen2とAzure AI Searchの統合に関する新しいセクションを追加し、アクセス制御の詳細な説明が行われています。

## Breaking changes
- 特に大きな破壊的変更はありませんが、セクション名や説明の変更により一部ユーザーにとっては内容の把握に再確認が必要となる可能性があります。

## Other updates
- ポリシー参照とセキュリティコントロールのドキュメントにおいて、ファイル参照のパスが適切に修正されています。
- 削除追跡の記述が整えられ、ドキュメントの読みやすさが向上しました。

# Insights
これらの変更は主にドキュメントの情報整合性とユーザーエクスペリエンスを向上させるために行われています。特に、検索機能やセキュリティ制御に関する情報は、正確で最新の情報を提供することが極めて重要です。今回の変更によって、ユーザーはAzureの検索機能やセキュリティ制御に関する理解を深め、より効率的に利用することが可能となるでしょう。

セマンティックハイブリッド検索に関する更新は、特にAIや検索の分野に興味を持つ技術者にとって有益であり、検索結果の関連性向上を目指した調整が行われていることが注目されます。さらに、ADLS Gen2の新しいアクセス権限管理セクションは、セキュリティとアクセス制御に携わる人々にとって有用な情報を提供します。表形式を使用しているため、複雑なアクセス制御の特徴を視覚的に理解しやすくしています。

ユーザーが最新の技術と情報を活用できるようにするため、ドキュメントの細かな改善が継続的に行われており、これによりAzureサービス全体の信頼性と利用便益が高まっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-get-started-vector-python.md](#item-53085f) | minor update | 検索の始め方に関するクイックスタートドキュメントの更新 | modified | 11 | 9 | 20 | 
| [policy-reference.md](#item-a8d880) | minor update | ポリシー参照ドキュメントの更新 | modified | 1 | 1 | 2 | 
| [search-indexer-access-control-lists-and-role-based-access.md](#item-67b42f) | minor update | 検索インデクサーのアクセス制御リストと役割ベースのアクセスに関するドキュメントの更新 | modified | 11 | 1 | 12 | 
| [security-controls-policy.md](#item-0e5774) | minor update | セキュリティコントロールポリシーのリンク修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/includes/quickstarts/search-get-started-vector-python.md{#item-53085f}

<details>
<summary>Diff</summary>
````diff
@@ -343,7 +343,7 @@ In the next sections, we run queries against the `hotels-vector-quickstart` inde
 - [Single vector search](#single-vector-search)
 - [Single vector search with filter](#single-vector-search-with-filter)
 - [Hybrid search](#hybrid-search)
-- [Semantic hybrid search with filter](#semantic-hybrid-search-with-a-filter)
+- [Semantic hybrid search](#semantic-hybrid-search)
 
 ### Create the vector query string
 
@@ -674,9 +674,9 @@ Hybrid search consists of keyword queries and vector queries in a single search
    ]
    ```
 
-### Semantic hybrid search with a filter
+### Semantic hybrid search
 
-Here's the last query in the collection. This hybrid query with semantic ranking is filtered to show only the hotels within a 500-kilometer radius of Washington D.C. You can set `vectorFilterMode` to null, which is equivalent to the default (`preFilter` for newer indexes and `postFilter` for older ones).
+Here's the last query in the collection. This hybrid query specifies the semantic query type and a semantic configuration, demonstrating that you can build a hybrid query that uses semantic reranking.
 
 - Find the cell below section titled "Semantic hybrid search" and execute the cell. This code block contains the request to query the search index.
 
@@ -721,9 +721,9 @@ Here's the last query in the collection. This hybrid query with semantic ranking
       print("No vector loaded, skipping search.")
    ```
 
-   Review the output below the cell. The response is three hotels, which are filtered by location and faceted by `StateProvince` and semantically reranked to promote results that are closest to the search string query (`historic hotel walk to restaurants and shopping`).
+   Review the output below the cell.
 
-   The Swirling Currents Hotel now moves into the top spot. Without semantic ranking, Nordick's Valley Motel is number one. With semantic ranking, the machine comprehension models recognize that `historic` applies to "hotel, within walking distance to dining (restaurants) and shopping."
+   With semantic ranking, the Swirling Currents Hotel now moves into the top spot. W
 
    ```output
    Total semantic hybrid results: 7
@@ -759,13 +759,15 @@ Here's the last query in the collection. This hybrid query with semantic ranking
      Category: Suite
    ```
 
-   Key takeaways:
+You can think of the semantic ranking as a way to improve the relevance of search results by understanding the meaning behind the words in the query and the content of the documents. In this case, the semantic ranking helps to identify hotels that are not only relevant to the keywords but also match the intent of the query:
 
-   - Vector search is specified through the `vectors.value` property. Keyword search is specified through the `search` property.
+Key takeaways:
 
-   - In a hybrid search, you can integrate vector search with full-text search over keywords. Filters, spell check, and semantic ranking apply to textual content only, and not vectors. In this final query, there's no semantic `answer` because the system didn't produce one that was sufficiently strong.
+- Vector search is specified through the `vectors.value` property. Keyword search is specified through the `search` property.
 
-   - Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
+- In a hybrid search, you can integrate vector search with full-text search over keywords. Filters, spell check, and semantic ranking apply to textual content only, and not vectors. In this final query, there's no semantic `answer` because the system didn't produce one that was sufficiently strong.
+
+- Actual results include more detail, including semantic captions and highlights. Results were modified for readability. To get the full structure of the response, run the request in the REST client.
 
 ## Clean up
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索の始め方に関するクイックスタートドキュメントの更新"
}
```

### Explanation
この変更は、検索機能に関するクイックスタートドキュメント（Python向け）の内容を更新するものであり、ページ内のセクションの見出しや説明が変更されています。具体的には、以下の点が変更されました：

- 「セマンティックハイブリッド検索」の見出しが「セマンティックハイブリッド検索フィルター付き」から「セマンティックハイブリッド検索」に短縮されました。
- 最後のクエリに関して、フィルターがなくなることや、クエリタイプおよび設定に関する説明がより明確にされています。
- セマンティックランキングの説明が改訂され、検索結果の関連性向上に関する詳細が付加されています。
- キーポイントのセクションに具体的な情報を追加し、検索実行時の注意点や結果の構造についての説明が強化されています。

これらの変更により、ユーザーがセマンティックハイブリッド検索の概念をより理解しやすくすることを目的としています。

## articles/search/policy-reference.md{#item-a8d880}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ the link in the **Version** column to view the source on the
 
 ## Azure Cognitive Search
 
-[!INCLUDE [azure-policy-reference-rp-search](~/azure-docs-pr-policy-includes/includes/policy/reference/byrp/microsoft.search.md)]
+[!INCLUDE [azure-policy-reference-rp-search](~/azure-policy-autogen-docs/includes/policy/reference/byrp/microsoft.search.md)]
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポリシー参照ドキュメントの更新"
}
```

### Explanation
この変更は、Azure Cognitive Searchに関するポリシー参照ドキュメントにおいて、あるインクルード文のパスを修正するものです。具体的には、次のような点が修正されています：

- インクルードされるファイルの参照先が、`policy-includes`から`policy-autogen-docs`に変更されました。これにより、ドキュメントのソースが正しい場所から取得されるようになります。

この修正は、文書の整合性を保つためのものであり、ユーザーが正確な情報を参照できるようにすることを目的としています。

## articles/search/search-indexer-access-control-lists-and-role-based-access.md{#item-67b42f}

<details>
<summary>Diff</summary>
````diff
@@ -288,5 +288,15 @@ Choose one of the following mechanisms, depending on how many items changed:
 
 ## Deletion tracking 
 
-To effectively manage blob deletion, ensure that you have enabled [deletion tracking](search-howto-index-changed-deleted-blobs.md) before your indexer runs for the first time. This feature allows the system to detect deleted blobs from your source and have them deleted from the index.  
+To effectively manage blob deletion, ensure that you have enabled [deletion tracking](search-howto-index-changed-deleted-blobs.md) before your indexer runs for the first time. This feature allows the system to detect deleted blobs from your source and have them deleted from the index.
 
+## Supported ADLS Gen2 permission features
+
+This section compares document-level access control features between ADLS Gen2 and Azure AI Search. It highlights which ADLS Gen2 access control mechanisms are supported or mapped when integrating with AI Search, helping you understand how permissions are enforced at the document level.
+
+| ADLS Gen2 Feature | Description | Supported | Notes |
+|-|-|-|-|
+| [RBAC](/azure/storage/blobs/data-lake-storage-access-control-model#role-based-access-control-azure-rbac) | Coarse-grained access at container level | Yes | AI Search honors RBAC for access to all documents in the entire container. |
+| [ABAC](/azure/storage/blobs/data-lake-storage-access-control-model#attribute-based-access-control-azure-abac) | Attribute-based conditions on top of RBAC | No | AI Search does not evaluate ABAC conditions for document-level access. |
+| [ACL](/azure/storage/blobs/data-lake-storage-access-control-model#access-control-lists-acls) | Fine-grained permissions at directory/file (document) level  | Yes | AI Search uses document-level ACLs for [permission filters](./search-query-access-control-rbac-enforcement.md). |
+| [Security Groups](/azure/storage/blobs/data-lake-storage-access-control-model#security-groups) | Group-based permission assignments  | Yes  | Supported if security groups are mapped inside the document-level ACL. |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデクサーのアクセス制御リストと役割ベースのアクセスに関するドキュメントの更新"
}
```

### Explanation
この変更は、検索インデクサーのアクセス制御リストおよび役割ベースのアクセスに関するドキュメントに新しいセクションを追加し、情報を強化するものです。具体的には、以下の点が更新されました：

- **削除追跡の説明**はそのまま維持されていますが、改行が追加されて文の整形が改善されました。
- 新しいセクション「**サポートされているADLS Gen2の権限機能**」が追加され、ADLS Gen2とAzure AI Search間でのドキュメントレベルのアクセス制御機能の比較が行われています。このセクションは、AI Searchと統合する際にどのADLS Gen2アクセス制御メカニズムがサポートまたはマッピングされるかを明確にし、ユーザーが文書レベルでの権限の施行方法を理解できるようにしています。
- 表形式で、RBAC、ABAC、ACL、セキュリティグループについての説明が含まれ、それぞれの特徴、サポート状況、および備考が整理されています。

これにより、ユーザーはADLS Gen2における権限管理の理解を深めることができるようになり、アクセス制御の適切な設定に役立てることができます。

## articles/search/security-controls-policy.md{#item-0e5774}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ compliant with the specific standard.
 
 [!INCLUDE [azure-policy-compliancecontrols-introwarning](~/azure-docs-pr-policy-includes/includes/policy/standards/intro-warning.md)]
 
-[!INCLUDE [azure-policy-compliancecontrols-search](~/azure-docs-pr-policy-includes/includes/policy/standards/byrp/microsoft.search.md)]
+[!INCLUDE [azure-policy-compliancecontrols-search](~/azure-policy-autogen-docs/includes/policy/standards/byrp/microsoft.search.md)]
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セキュリティコントロールポリシーのリンク修正"
}
```

### Explanation
この変更は、セキュリティコントロールポリシーに関するドキュメントのリンクを更新するものです。具体的には、次の部分が修正されました：

- インクルードされるファイルのパスが、`policy-includes`から`policy-autogen-docs`に変更されています。これにより、正しいリソースからポリシーのコンプライアンスコントロールに関する情報が取得できるようになります。

この修正は、文書の整合性と正確性を向上させることを目的としており、ユーザーが最新の情報を効率的に参照できるようにするための重要な調整です。


