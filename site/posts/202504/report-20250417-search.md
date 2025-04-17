---
date: '2025-04-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:81ad672...MicrosoftDocs:dad2f57
summary: このコードの変更は、コグニティブ検索スキルの注釈言語に関する記事の小規模な更新で、新機能として「文字列結合」に関するセクションが追加されました。特に重大な変更はなく、文書の日付は2024年8月20日から2025年4月15日に変更されています。この更新は、ユーザーがAzureでコグニティブ検索スキルを構築する際の理解を深めることを目的としており、実践的な具体例が提供されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:81ad672...MicrosoftDocs:dad2f57){target="_blank"}

# Highlights
このコードの変更は、コグニティブ検索スキルの注釈言語に関する記事の小規模な更新を行うもので、新機能として「文字列結合」に関する新しいセクションが追加されています。一方で、特に重大な変更点や破壊的な変更は報告されていません。

## New features
- 「文字列結合」に関するセクションの追加
  - 新しいセクションでは、具体的な使用例が示されており、ユーザーがこの機能をどのように活用できるかについての理解が深まります。

## Breaking changes
- 特に破壊的な変更はありません。

## Other updates
- ドキュメントの日付が2024年8月20日から2025年4月15日に変更されました。

# Insights
この更新は、ユーザーがAzureを使用してコグニティブ検索スキルを構築する際の利便性を向上させることを目的としており、新しい機能の一つとして「文字列結合」に関する具体例を追加することで、ユーザーの理解をサポートしています。ユーザーはこれにより、文字列結合がどのように検索スキルに応用できるかを明確に理解できるようになります。また、これらの改善は文書の内容をより現代的かつ実践的なものにするためのものであり、そのために日付の更新が含まれています。これにより、技術文書が最新の情報を含み、常に最適な実用性を保持していることを読者に保証しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-annotation-language.md](#item-aaedc7) | minor update | コグニティブ検索スキルの注釈言語に関する記事の更新 | modified | 8 | 1 | 9 | 


# Modified Contents
## articles/search/cognitive-search-skill-annotation-language.md{#item-aaedc7}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: reference
-ms.date: 08/20/2024
+ms.date: 04/15/2025
 ---
 # Skill context and input annotation language
 
@@ -233,6 +233,13 @@ When used inside an expression, paths should be enclosed between `"$("` and `")"
 |`=15%4`|`3`|
 |`=$(/document/merged_content/entities/0/offset)%2`|`1`|
 
+### String concatenation `'+'`
+
+|Expression|Value|
+|---|---|
+|`="Hello," + "world!"`|`"Hello, world!"`|
+|`=$(/document/merged_content/entities/0/text) + $(/document/merged_content/entities/0/category)`|`"BMN Organization"`|
+
 ### Less than, less than or equal, greater than and greater than or equal `'<'` `'<='` `'>'` `'>='`
 
 |Expression|Value|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コグニティブ検索スキルの注釈言語に関する記事の更新"
}
```

### Explanation
この変更は、コグニティブ検索スキルの注釈言語に関する記事に対する小規模な更新を表しています。具体的には、ドキュメント内の日付が2024年8月20日から2025年4月15日に変更されたことが含まれています。また、新たに「文字列結合」に関するセクションが追加され、複数の例が示されています。これは、表現の使用方法を具体的に示すことにより、ユーザーに対する理解を深めることを目的としています。この変更により、記事の内容がより充実し、読者が記事を参照する際の利便性が向上しました。


