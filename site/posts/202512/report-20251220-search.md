---
date: '2025-12-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:38e3c32...MicrosoftDocs:38b30b1
summary: |-
  この報告書の要約は以下の通りです：

  今回の更新は、ドキュメント内での設定および作成手順の明確化を目指しています。主にAzure AI SearchとMicrosoft Foundryにおけるアクセス権設定に関する詳細な説明と、知識ソースの具体的な作成方法に焦点を当てています。特に、以前のあいまいな指示を改め、明確かつ具体的な手順を示すことで、ユーザーが混乱なく操作できるようになっています。この修正は、技術資料の整合性を高め、ユーザーエクスペリエンスを向上させることを意図しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:38e3c32...MicrosoftDocs:38b30b1){target="_blank"}

# Highlights
これらの更新は、ドキュメント内の設定および作成手順の明確化を目的としています。特に、Azure AI SearchおよびMicrosoft Foundryでのアクセス権の設定方法の詳細説明、ならびに知識ソースの作成方法の具体化に焦点を当てています。

## New features
- なし

## Breaking changes
- なし

## Other updates
- Azure AI SearchとMicrosoft Foundryの両方でのアクセス権設定の明確化。
- 知識ソースの作成に関する表現をより直接的に変更。

# Insights
今回のドキュメントの更新は、ユーザーの理解を助け、誤解を回避するためのものであり、システムの使用における設定と作成のプロセスをより明確に説明することに重きを置いています。

まず、アクセス設定の更新に関する変更では、ユーザーがAzure AI SearchとMicrosoft Foundryの両方で権限設定を行う必要性を強調しています。以前のバージョンでは「設定を選択する」というあいまいな指示にとどまっていましたが、具体的な手順を示し、ユーザーが混乱することなく明確に操作できるようにしています。

次に、知識ソースの作成に関する更新では、「他のタイプの知識ソースはプログラム的に作成する必要があります」という指示を通じて、ユーザーがどのようにアプローチすべきかを具体化しています。これにより、ユーザーは必要な技術的ステップを容易に理解し、誤った期待を持つことなく適切な開発手法を選択できるようになります。

これらの修正は、技術資料の整合性を高め、ユーザーエクスペリエンスを向上させる設計思想に基づいています。高い可読性と導線設計により、ユーザーは正式なシステムの使用方法を迅速に習得できるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-how-to-create-pipeline.md](#item-5d7858) | minor update | アクセス設定の更新方法の明確化 | modified | 1 | 1 | 2 | 
| [agentic-retrieval-overview.md](#item-d1f354) | minor update | 知識ソースの作成方法の表現の明確化 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/agentic-retrieval-how-to-create-pipeline.md{#item-5d7858}

<details>
<summary>Diff</summary>
````diff
@@ -44,7 +44,7 @@ The following diagram shows the high-level architecture of this agentic retrieva
 
 Before you begin, make sure you have permissions to access content and operations. We recommend Microsoft Entra ID authentication and role-based access for authorization. You must be an **Owner** or **User Access Administrator** to assign roles. If roles aren't feasible, you can use [key-based authentication](search-security-api-keys.md) instead.
 
-To configure access for this solution, select both of the following tabs.
+To configure access for this solution, you must set permissions in both Azure AI Search and Microsoft Foundry. Select both of the following tabs for service-specific guidance.
 
 ### [**Azure AI Search**](#tab/search-perms)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アクセス設定の更新方法の明確化"
}
```

### Explanation
この変更は、ドキュメント「agentic-retrieval-how-to-create-pipeline.md」におけるアクセス設定の方法についての内容を明確にするものです。具体的には、アクセスを構成する際に、ユーザーがAzure AI SearchとMicrosoft Foundryの両方で権限を設定する必要があることを強調しています。変更前は、単に「設定を選択する」という表現だったものが、権限の設定の重要性を伝えるために、「両方のタブでサービス固有のガイダンスを選択する」と具体的に記載されています。この更新は、より明瞭で正確な指示を提供し、ユーザーの理解を助けることを目的としています。

## articles/search/agentic-retrieval-overview.md{#item-d1f354}

<details>
<summary>Diff</summary>
````diff
@@ -100,7 +100,7 @@ Your application drives the pipeline by calling the knowledge base and handling
 
 To create an agentic retrieval solution, you can use the Azure portal, the latest preview REST APIs, or a preview Azure SDK package that provides the functionality.
 
-Currently, the portal only supports the creation of search index and blob knowledge sources. We recommend using a programmatic approach to create other types of knowledge sources.
+Currently, the portal only supports creating search index and blob knowledge sources. Other types of knowledge sources must be created programmatically.
 
 ### [**Quickstarts**](#tab/quickstarts)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "知識ソースの作成方法の表現の明確化"
}
```

### Explanation
この変更は、ドキュメント「agentic-retrieval-overview.md」における知識ソースの作成方法に関する表現を明確にするものです。具体的には、ポータルが現在サポートしているのは検索インデックスとBlob知識ソースの作成のみであるとの説明が、より簡潔かつ直接的に修正されました。修正前の文は「他のタイプの知識ソースを作成するためにはプログラム的アプローチを使用することを推奨します」と述べていたのが、修正後は「他のタイプの知識ソースはプログラム的に作成する必要があります」と、より明確な指示が示されています。この更新により、ユーザーが必要なアクションを理解しやすくなることが期待されます。


