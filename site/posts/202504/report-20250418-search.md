---
date: '2025-04-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dad2f57...MicrosoftDocs:d942a6a
summary: 今回の更新では、3つのMarkdownファイルに対して軽微な修正が行われました。修正内容は文法の改善、手順の詳細化、リンクの更新であり、新機能や重大な変更はありません。これらの改訂は、情報の明確さと有用性を向上させることを目的としています。具体的には、文法の修正、Power
  Appsに関する手順の充実、RAG Time Journeyのリンクの更新が含まれています。これにより、ユーザーはより正確で理解しやすい情報を得ることができるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dad2f57...MicrosoftDocs:d942a6a){target="_blank"}

# ハイライト
今回の差分では、主に3つのMarkdownファイルに対する軽微な修正が行われています。これには文法の修正、手順の改善、リンクの更新が含まれており、新機能や重大な変更はありません。これらの修正は、それぞれのコンテンツがより分かりやすく、ユーザーにとって有用な情報を提供することを目的としています。

## 新機能
特に新しい機能は追加されていません。

## 重大な変更
重大な変更はありません。

## その他の更新
- 検索方法に関する文法の修正が行われました。
- Power Appsに関する手順が詳細化され、ユーザーガイドが改善されました。
- RAG Time Journeyのリンクがより直接的な情報源へと更新されました。

# 洞察
この更新は、文書の内容をよりわかりやすく明確にするためのものです。最初の変更では、単なる英語文法の修正が行われており、読みやすさと正確さに重点が置かれています。この種の修正は、特に技術文書において重要です。読者が文法的に誤った表現に惑わされることなく、PURE英語で情報を取得できるようにするからです。

次に、Power Appsに関する文書では、読者が手順をより理解しやすくするための詳細な説明が追加されています。具体的なサンプルURLの追加やヒントコメントの微調整は、ユーザーが直面しうる問題に対して適時かつ的確なサポートを提供します。特にDLPポリシーエラーについての新しいガイダンスがユーザーエクスペリエンスを直接改善しています。

最後に、RAG Time Journeyに関連するリンクが更新されたことにより、ユーザーはより充実した情報を得ることができるようになっています。GitHubリポジトリから修正され、Microsoft Tech Communityのブログへのリンクに変更されたのは、読者が最新かつ正当な情報源にアクセスする際の利便性を考慮したものです。このようなリンク先の更新は、情報の価値を維持するために重要であり、情報の信頼性を高めるものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-how-to-semantic-chunking.md](#item-4a1d07) | minor update | 検索方法に関する説明文の修正 | modified | 1 | 1 | 2 | 
| [search-howto-powerapps.md](#item-92d1c0) | minor update | Power Apps用の検索手順の改善 | modified | 9 | 3 | 12 | 
| [whats-new.md](#item-fa71b4) | minor update | RAG Time Journeyのリンクを更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-how-to-semantic-chunking.md{#item-4a1d07}

<details>
<summary>Diff</summary>
````diff
@@ -202,7 +202,7 @@ POST {endpoint}/skillsets?api-version=2024-11-01-preview
 
 {
   "name": "my_skillset",
-  "description": "A skillset for structure-aware chunking and vectorization with a index projection around markdown section",
+  "description": "A skillset for structure-aware chunking and vectorization with an index projection around markdown section",
   "skills": [
     {
       "@odata.type": "#Microsoft.Skills.Util.DocumentIntelligenceLayoutSkill",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索方法に関する説明文の修正"
}
```

### Explanation
このコードの差分は、`articles/search/search-how-to-semantic-chunking.md`ファイルの内容を軽微に修正したことを示しています。具体的には、`description`フィールドの文言が変更されました。元の文では「a index projection」が使用されていましたが、これが「an index projection」に修正されました。この変更は、文法の正確さを向上させるためのものであり、機能には影響しません。全体として、追加と削除が1行ずつあり、合計2行の変更が行われています。この修正は、より適切な英語使用を促進する目的で行われました。

## articles/search/search-howto-powerapps.md{#item-92d1c0}

<details>
<summary>Diff</summary>
````diff
@@ -69,7 +69,11 @@ A connector in Power Apps is a data source connection. In this step, create a cu
 
    * Select the verb `GET`
 
-   * For the URL, enter a sample query for your search index (`search=*` returns all documents, `$select=` lets you choose fields). The API version is required. Fully specified, a URL might look like this: `mydemo.search.windows.net/indexes/hotels-sample-index/docs?search=*&$select=HotelName,Description,Address/City&api-version=2024-07-01`. Omit the `https://` prefix.
+   * For the URL, enter a sample query for your search index (`search=*` returns all documents, `$select=` lets you choose fields). The API version is required. Fully specified, a URL might look like the following example. Notice that the `https://` prefix is omitted.
+
+     ```http
+     mydemo.search.windows.net/indexes/hotels-sample-index/docs?search=*&$select=HotelName,Description,Address/City&api-version=2024-07-01
+     ```
 
    * For Headers, type `Content-Type application/json`.
 
@@ -137,7 +141,7 @@ A connector in Power Apps is a data source connection. In this step, create a cu
     ```
 
     > [!TIP] 
-    > There is a character limit to the JSON response you can enter, so you might want to simplify the JSON before pasting it. The schema and format of the response is more important than the values themselves. For example, the Description field could be simplified to just the first sentence.
+    > There's a character limit to the JSON response you can enter, so you might want to simplify the JSON before pasting it. The schema and format of the response is more important than the values themselves. For example, the Description field could be simplified to just the first sentence.
 
 1. Select **Import** to add the default response.
 
@@ -159,7 +163,7 @@ Provide a [query API key](search-security-api-keys.md#find-existing-keys) for th
 
     :::image type="content" source="./media/search-howto-powerapps/1-11-1-test-connector.png" alt-text="View Properties" border="true":::
 
-1. In the drop down list of operations, select **6. Test**.
+1. In the drop-down list of operations, select **6. Test**.
 
 1. In **Test Operation**, select **+ New Connection**.
 
@@ -171,6 +175,8 @@ Provide a [query API key](search-security-api-keys.md#find-existing-keys) for th
 
 If the test fails, recheck the inputs. In particular, revisit the sample response and make sure it was created properly. The connector definition should show the expected items for the response.
 
+If you're blocked by a Data Loss Prevention (DLP) policy error, review the error message for guidance. You might be able to modify the policy or make your connector nonblockable.
+
 ## 3 - Visualize results
 
 In this step, create a Power App with a search box, a search button, and a display area for the results. The Power App will connect to the recently created custom connector to get the data from Azure Search.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Power Apps用の検索手順の改善"
}
```

### Explanation
このコードの差分は、`articles/search/search-howto-powerapps.md`ファイルの内容を更新したことを示しています。主な変更点は、Power Appsでの検索手順に関連する説明が改善され、明確化されたことです。具体的には、サンプルクエリのURLの説明が、`https://`のプレフィックスが省略されていることに注意を促す形に改訂され、サンプルURLがコードブロックとして追加されました。

また、ハイライトされるヒントコメントの文言が微調整され、リストや文章にいくつかの小さな変更（たとえば「drop down list」を「drop-down list」に修正）は行われています。加えて、DLPポリシーエラーに関する新しいガイダンスが追加され、ユーザーが直面する可能性のある問題に対する支援が強化されています。

全体として、これらの変更は、手順をより明確にし、読者が必要な情報を得やすくすることを目的としています。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ Learn about the latest updates to Azure AI Search functionality, docs, and sampl
 
 | Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
 |-----------------------------|------|--------------|
-| [RAG Time Journey](https://github.com/microsoft/rag-time) | Demo code | Code and video demonstrations of Retrieval Augmented Generation (RAG) workflows that use Azure AI Search. Segments include fundamentals, patterns and use-cases, [vector indexing at scale](https://github.com/microsoft/rag-time/tree/main/Journey%203%20-%20Optimize%20your%20Vector%20Index%20for%20Scale), and [agentic search](https://github.com/microsoft/rag-time/tree/main/Journey%20Bonus%20-%20Agentic%20RAG) where you use an agent to evaluate a result and generate a better answer. |
+| [RAG Time Journey](https://github.com/microsoft/rag-time) | Demo code | Code and video demonstrations of Retrieval Augmented Generation (RAG) workflows that use Azure AI Search. Segments include fundamentals, patterns and use-cases, [vector indexing at scale](https://github.com/microsoft/rag-time/tree/main/Journey%203%20-%20Optimize%20your%20Vector%20Index%20for%20Scale), and [agentic search](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/bonus-rag-time-journey-agentic-rag/4404652) where you use an agent to evaluate a result and generate a better answer. |
 
 ## March 2025
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAG Time Journeyのリンクを更新"
}
```

### Explanation
このコードの差分は、`articles/search/whats-new.md`ファイル内のリンクに関する軽微な更新を示しています。具体的には、"RAG Time Journey"の説明に関連するリンクが変更されました。元々のリンクはGitHubのリポジトリを指していましたが、更新後はMicrosoft Tech Communityのブログへのリンクに変更されています。この変更により、ユーザーはより直接的な情報源にアクセスできるようになりました。

この修正は、情報の正確性を保ち、最新のソースに基づいたコンテンツを提供することを目的としています。全体的に、この変更は1行の追加と1行の削除を伴い、内容の明確さを向上させています。


