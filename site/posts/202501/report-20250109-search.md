---
date: '2025-01-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:058aad5...MicrosoftDocs:6c9883f
summary: 今回の変更は、複数のドキュメントに対する軽微な修正や改善を含んでおり、主に文章表現や用語の微調整、誤りの修正が行われています。新機能の追加はなく、重大な破壊的変更もありません。具体的には、文脈や用語の修正、アプリ名の明確化、埋め込みモデルの次元数に関する誤り修正が含まれています。これらの変更はドキュメントの品質向上を目指し、ユーザビリティや理解度を高めることが期待されています。特に、正確な情報に基づくガイドが提供されることで、トラブルシューティングや設定の不整合を防ぐ効果があると考えられています。また、表現改善により、全体として読みやすく理解しやすい内容に仕上がっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:058aad5...MicrosoftDocs:6c9883f){target="_blank"}

# Highlights
今回の変更は、複数のドキュメントに対する軽微な修正や改善を含んでいます。特に文章の表現や用語の微調整、誤りの修正がメインの内容です。

## New features
特に新機能の追加は見られません。

## Breaking changes
重大な破壊的変更はなく、全体的に軽微な調整に留まっています。

## Other updates
- ドキュメント内の文脈や用語の修正
- アプリ名の明確化
- 埋め込みモデルの次元数に関する誤りの修正

# Insights
この一連の変更は、ドキュメントの品質向上を目的としています。文字通りの意味を超えて、ユーザビリティや理解度を高めるための工夫として捉えることができます。特に翻訳サービスや設定に関する説明、チュートリアルに含まれる数値的な設定に関して重点が置かれており、これによりユーザーが特定のアプリケーションや設定を使用する際の疑問点を解消できるようになることが期待されます。

例えば、埋め込みモデルに関する修正では、次元数の値が誤っていてはシステム全体の動作に影響を及ぼしかねないため、正確な数値に修正されたことは非常に重要です。このような点からも、開発者や技術者にとって、正確な情報に基づくガイドが提供されることで、トラブルシューティングや設定の不整合を未然に防ぐことができると考えられます。

また、表現の改善や用語の修正により、全体として文章の流れがよくなり、読者にとって読みやすくそして理解しやすいドキュメント内容になることが期待されています。これは、特に技術文書の場合、詳細な解説がわかりやすく提供されることが重要であることを物語っています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-text-translation.md](#item-b42884) | minor update | ドキュメント文脈の微調整 | modified | 1 | 1 | 2 | 
| [query-lucene-syntax.md](#item-736436) | minor update | ドキュメント内の用語の微調整 | modified | 2 | 2 | 4 | 
| [search-howto-powerapps.md](#item-92d1c0) | minor update | 指示文の表現の微調整 | modified | 1 | 1 | 2 | 
| [search-security-network-security-perimeter.md](#item-49c0d7) | minor update | アプリ名の修正 | modified | 1 | 1 | 2 | 
| [tutorial-rag-build-solution-pipeline.md](#item-25ce01) | bug fix | 埋め込みモデルの次元数の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/cognitive-search-skill-text-translation.md{#item-b42884}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ ms.date: 09/19/2022
 
 The **Text Translation** skill evaluates text and, for each record, returns the text translated to the specified target language. This skill uses the [Translator Text API v3.0](/azure/ai-services/translator/reference/v3-0-translate) available in Azure AI services.
 
-This capability is useful if you expect that your documents may not all be in one language, in which case you can normalize the text to a single language before indexing for search by translating it.  It's also useful for localization use cases, where you may want to have copies of the same text available in multiple languages.
+This capability is useful if you expect that your documents may not all be in one language, in which case you can normalize the text to a single language before indexing for search by translating it.  It's also useful for localization use cases, where you might want to have copies of the same text available in multiple languages.
 
 The [Translator Text API v3.0](/azure/ai-services/translator/reference/v3-0-reference) is a non-regional Azure AI service, meaning that your data isn't guaranteed to stay in the same region as your Azure AI Search or attached Azure AI services resource.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント文脈の微調整"
}
```

### Explanation
この変更は、`articles/search/cognitive-search-skill-text-translation.md` のドキュメント内でのテキストの小さな修正です。元の文は、「あなたが期待する場合に便利です」という表現から「あなたが期待する場合に便利です」というより自然な言い回しに修正されました。この修正により、文章の流れが改善され、読みやすさが向上しています。全体で1行が追加され、1行が削除されたため、全体的な変更は2行となります。これらの変更は、ドキュメントの理解を助け、ユーザーにとっての情報の正確性を高めることを目的としています。

## articles/search/query-lucene-syntax.md{#item-736436}

<details>
<summary>Diff</summary>
````diff
@@ -175,7 +175,7 @@ Suffix matching requires the regular expression forward slash `/` delimiters. Ge
 
 During query parsing, queries that are formulated as prefix, suffix, wildcard, or regular expressions are passed as-is to the query tree, bypassing [lexical analysis](search-lucene-query-architecture.md#stage-2-lexical-analysis). Matches will only be found if the index contains the strings in the format your query specifies. In most cases, you need an analyzer during indexing that preserves string integrity so that partial term and pattern matching succeeds. For more information, see [Partial term search in Azure AI Search queries](search-query-partial-matching.md).
 
-Consider a situation where you may want the search query `terminal*` to return results that contain terms such as `terminate`, `termination`, and `terminates`.
+Consider a situation where you might want the search query `terminal*` to return results that contain terms such as `terminate`, `termination`, and `terminates`.
 
 If you were to use the en.lucene (English Lucene) analyzer, it would apply aggressive stemming of each term. For example, `terminate`, `termination`, `terminates` will all be tokenized down to the token `termi` in your index. On the other side, terms in queries using wildcards or fuzzy search aren't analyzed at all, so there would be no results that would match the `terminat*` query.
 
@@ -187,7 +187,7 @@ Azure AI Search uses frequency-based scoring ([BM25](https://en.wikipedia.org/wi
 
 ## Special characters
 
-In some circumstances, you may want to search for a special character, like an '❤' emoji or the '€' sign. In such cases, make sure that the analyzer you use doesn't filter those characters out. The standard analyzer bypasses many special characters, excluding them from your index.
+In some circumstances, you might want to search for a special character, like an '❤' emoji or the '€' sign. In such cases, make sure that the analyzer you use doesn't filter those characters out. The standard analyzer bypasses many special characters, excluding them from your index.
 
 Analyzers that tokenize special characters include the whitespace analyzer, which takes into consideration any character sequences separated by whitespaces as tokens (so the `❤` string would be considered a token). Also, a language analyzer like the Microsoft English analyzer ("en.microsoft"), would take the "€" string as a token. You can [test an analyzer](/rest/api/searchservice/indexes/analyze) to see what tokens it generates for a given query.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント内の用語の微調整"
}
```

### Explanation
この変更は、`articles/search/query-lucene-syntax.md` のドキュメントにおける表現の改善を目的としています。具体的には、文中の「あなたが期待する場合に便利です」から「あなたが期待する場合に便利です」へと、より自然な表現に修正されました。この修正により、文の流れが改善され、読み手にとっての理解が促進されることが期待されています。

全体で2行が追加され、2行が削除され、合計4行の変更が行われています。これらの変更は、特に検索クエリの例に関連する部分と、特殊文字に関する説明に影響を与えています。文書の明確さを高め、ユーザーがより良い検索体験を得られるようにすることが目的です。

## articles/search/search-howto-powerapps.md{#item-92d1c0}

<details>
<summary>Diff</summary>
````diff
@@ -137,7 +137,7 @@ A connector in Power Apps is a data source connection. In this step, create a cu
     ```
 
     > [!TIP] 
-    > There is a character limit to the JSON response you can enter, so you may want to simplify the JSON before pasting it. The schema and format of the response is more important than the values themselves. For example, the Description field could be simplified to just the first sentence.
+    > There is a character limit to the JSON response you can enter, so you might want to simplify the JSON before pasting it. The schema and format of the response is more important than the values themselves. For example, the Description field could be simplified to just the first sentence.
 
 1. Select **Import** to add the default response.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "指示文の表現の微調整"
}
```

### Explanation
この変更は、`articles/search/search-howto-powerapps.md` のドキュメントにおける指示文の軽微な修正です。特に、実行に関連するアドバイスの表現が、「あなたが望むかもしれません」から「あなたが望むかもしれません」へと修正され、より自然な口語体になっています。この修正により、読み手に対する柔らかいトーンが強調され、より親しみやすい印象を与えることを意図しています。

全体として、1行が追加され、1行が削除され、合計で2行の変更が行われています。ドキュメントの明確さと可読性を向上させるための努力が反映されています。

## articles/search/search-security-network-security-perimeter.md{#item-49c0d7}

<details>
<summary>Diff</summary>
````diff
@@ -167,7 +167,7 @@ Within the perimeter, all resources have mutual access at the network level. You
 
 For resources outside of the network security perimeter, you must specify inbound and outbound access rules. Inbound rules specify which connections to allow in, and outbound rules specify which requests are allowed out.
 
-A search service accepts inbound requests from apps like Azure AI Foundry, Azure OpenAI Studio, Azure Machine Learning prompt flow, and any app that sends indexing or query requests. A search service sends outbound requests during indexer-based indexing and skillset execution. This section explains how to set up inbound and outbound access rules for Azure AI Search scenarios.
+A search service accepts inbound requests from apps like Azure AI Foundry portal, Azure Machine Learning prompt flow, and any app that sends indexing or query requests. A search service sends outbound requests during indexer-based indexing and skillset execution. This section explains how to set up inbound and outbound access rules for Azure AI Search scenarios.
 
    > [!NOTE]
    > Any service associated with a network security perimeter implicitly allows inbound and outbound access to any other service associated with the same network security perimeter when that access is authenticated using [managed identities and role assignments](/entra/identity/managed-identities-azure-resources/overview). Access rules only need to be created when allowing access outside of the network security perimeter, or for access authenticated using API keys.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アプリ名の修正"
}
```

### Explanation
この変更は、`articles/search/search-security-network-security-perimeter.md` のドキュメントにおけるアプリの名称の修正です。具体的には、「Azure AI Foundry」から「Azure AI Foundry ポータル」へと表現が明確化されました。この修正により、使用するアプリケーションが特定され、情報がよりわかりやすくなっています。

全体として、1行が追加され、1行が削除され、合計で2行の変更が行われています。この変更は、特にAzure AI Searchに関連するネットワークセキュリティの設定に関する情報の精度と明確さを向上させるためのものです。

## articles/search/tutorial-rag-build-solution-pipeline.md{#item-25ce01}

<details>
<summary>Diff</summary>
````diff
@@ -196,7 +196,7 @@ embedding_skill = AzureOpenAIEmbeddingSkill(
     resource_url=AZURE_OPENAI_ACCOUNT,  
     deployment_name="text-embedding-3-large",  
     model_name="text-embedding-3-large",
-    dimensions=1536,
+    dimensions=1024,
     inputs=[  
         InputFieldMappingEntry(name="text", source="/document/pages/*"),  
     ],  
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "埋め込みモデルの次元数の修正"
}
```

### Explanation
この変更は、`articles/search/tutorial-rag-build-solution-pipeline.md` において、埋め込みスキルの設定に関連する誤りの修正です。具体的には、`dimensions` の値が1536から1024に修正されました。この修正により、埋め込みモデルに対して正しい次元数が指定され、モデルの動作が期待通りになることが意図されています。

全体で1行が追加され、1行が削除される形式で変更が実施されており、合計で2行の変更が行われています。この修正は、チュートリアルの正確性を高め、ユーザーが埋め込みモデルを正しく使用できるようにするための重要な対応です。


