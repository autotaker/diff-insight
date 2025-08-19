---
date: '2025-08-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c3af3a3...MicrosoftDocs:ea1db4a
summary: この変更では、`search-faceted-navigation-examples.md`と`search-security-overview.md`の2つの記事が修正されました。新たに、ファセット階層の演算子についての詳細な説明が追加され、プライベートエンドポイントに関する説明が改善されています。変更には破壊的な要素はなく、主に検索ファセットの理解を深めることを目的としています。これにより、開発者は複雑なクエリを構築しやすくなり、さらにプライベートエンドポイントの情報もより見やすくなりました。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c3af3a3...MicrosoftDocs:ea1db4a){target="_blank"}

# Highlights
以下のコードの変更では、`search-faceted-navigation-examples.md`と`search-security-overview.md`という2つの記事が修正されています。新機能として、ファセット階層を示す演算子に関する詳細な説明が追加され、プライベートエンドポイントに関する説明が改善されています。

## New features
- ファセット階層の演算子に関する詳細説明の追加（ネスティング演算子 `>` とセミコロン演算子 `;` の説明が強化）

## Breaking changes
特に破壊的な変更はありません。

## Other updates
- `search-faceted-navigation-examples.md` 内で、演算子の順序に関する説明が強化されました。
- `search-security-overview.md` のプライベートエンドポイントに関するセクションでフォーマットと内容が改善されました。

# Insights
この更新は、主に検索ファセットの理解を深めるために行われたものです。ファセット階層の演算子に関する追加情報とクエリ処理の順序に関する注意点が明確化されることで、開発者が複雑なクエリを構築する際によりスムーズに進めることが可能になります。

ファセット階層は、検索エクスペリエンスを向上させるために頻繁に使用される機能であり、親子関係や同じ階層でのフィールドの扱いについての理解は非常に重要です。今回の変更により、これらの点がより明確に示され、ユーザーが自信を持って機能を実装できるようになっています。

一方、プライベートエンドポイントに関する記述の改善は、セキュリティとコストに関連する重要な情報をより見やすく、アクセスしやすくするためのものです。リンク先の情報へのアクセスが容易になり、ユーザーは必要な詳細を迅速に確認できます。この変更は、エンドポイントの使用に関する情報伝達の改善に大きく寄与しており、特に新たなユーザーや学習者に対して有用です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-faceted-navigation-examples.md](#item-2b1158) | minor update | ファセット階層の説明を強化 | modified | 12 | 7 | 19 | 
| [search-security-overview.md](#item-6b3f1e) | minor update | プライベートエンドポイントに関する記述の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-faceted-navigation-examples.md{#item-2b1158}

<details>
<summary>Diff</summary>
````diff
@@ -203,14 +203,19 @@ Results from this query are as follows:
 
 Starting in [2025-03-01-preview REST API](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-03-01-preview&preserve-view=true) and available in the Azure portal, you can configure a facet hierarchy using the `>` and `;` operators.
 
-The nesting (hierarchical) operator `>` denotes a parent–child relationship, and the semicolon operator `;` denotes multiple fields at the same nesting level, which are all children of the same parent. The parent must contain only one field. Both the parent and child fields must be `facetable`. 
+| Operator | Description |
+|-|-|
+| `>` | Nesting (hierarchical) operator denotes a parent–child relationship. |
+| `;` | Semicolon operator  denotes multiple fields at the same nesting level, which are all children of the same parent. The parent must contain only one field. Both the parent and child fields must be `facetable`. |
 
 The order of operations in a facet expression that includes facet hierarchies are:
 
-* options operator (comma `,`) that separates facet parameters for the facet field, such as the comma in `Rooms/BaseRate,values`
-* parentheses, such as the ones enclosing `(Rooms/BaseRate,values:50 ; Rooms/Type)`.
-* nesting operator (angled bracket `>`)
-* append operator (semicolon `;`), demonstrated in a second example `"Tags>(Rooms/BaseRate,values:50 ; Rooms/Type)"` in this section, where two child facets are peers under the Tags parent.
++ The options operator (comma `,`) that separates facet parameters for the facet field, such as the comma in `Rooms/BaseRate,values`
++ The parentheses, such as the ones enclosing `(Rooms/BaseRate,values:50 ; Rooms/Type)`.
++ The nesting operator (angled bracket `>`)
++ The append operator (semicolon `;`), demonstrated in a second example `"Tags>(Rooms/BaseRate,values:50 ; Rooms/Type)"` in this section, where two child facets are peers under the Tags parent.
+
+Notice that parentheses are processed before nesting and append operations: `A > B ; C` would be different than `A > (B ; C)`.
 
 There are several examples for facet hierarchies. The first example is a query that returns just a few documents, which is helpful for viewing a full response. Facets count the parent document (Hotels) and not intermediate subdocuments (Rooms), so the response determines the number of *hotels* that have any rooms in each facet bucket.
 
@@ -480,8 +485,8 @@ Starting in [2025-03-01-preview REST API](/rest/api/searchservice/operation-grou
 
 Facet filtering enables you to constrain the facet values returned to those matching a specified regular expression. Two new parameters accept a regular expression that is applied to the facet field:
 
-* `includeTermFilter` filters the facet values to those that match the regular expression
-* `excludeTermFilter` filters the facet values to those that don't match the regular expression 
++ `includeTermFilter` filters the facet values to those that match the regular expression
++ `excludeTermFilter` filters the facet values to those that don't match the regular expression 
 
 If a facet string satisfies both conditions, the `excludeTermFilter` takes precedence because the set of bucket strings is first evaluated with `includeTermFilter` and then excluded with `excludeTermFilter`.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファセット階層の説明を強化"
}
```

### Explanation
この変更では、`search-faceted-navigation-examples.md`という記事の内容が更新され、ファセット階層の演算子に関する詳細な説明が追加されました。具体的には、親子関係を示すためのネスティング演算子(`>`)と、同じ階層にある複数のフィールドを示すためのセミコロン演算子(`;`)に関するテーブルが追加され、各演算子の意味が明確に示されました。

さらに、演算子の順序に関する説明が強化され、特に括弧がネスティングや追加演算子よりも先に処理されることに関する注意が追加されています。これにより、ファセット階層におけるクエリの理解を深めることができるようになっています。また、ファセットフィルタリングに関しても、新たに二つのパラメータが明確に説明されています。

これらの変更は、ユーザーがファセット階層の使用方法をよりよく理解し、正確に実装できるようにするためのものです。

## articles/search/search-security-overview.md{#item-6b3f1e}

<details>
<summary>Diff</summary>
````diff
@@ -119,7 +119,7 @@ The private endpoint uses an IP address from the virtual network address space f
 
 :::image type="content" source="media/search-security-overview/inbound-private-link-azure-cog-search.png" alt-text="sample architecture diagram for private endpoint access":::
 
-While this solution is the most secure, using more services is an added cost so be sure you have a clear understanding of the benefits before diving in. For more information about costs, see the [pricing page](https://azure.microsoft.com/pricing/details/private-link/). For more information about how these components work together, [watch this video](https://learn.microsoft.com/Shows/AI-Show/Azure-Cognitive-Search-Whats-new-in-security/player]). Coverage of the private endpoint option starts at 5:48 into the video. For instructions on how to set up the endpoint, see [Create a Private Endpoint for Azure AI Search](service-create-private-endpoint.md).
+While this solution is the most secure, using more services is an added cost so be sure you have a clear understanding of the benefits before diving in. For more information about costs, see the [pricing page](https://azure.microsoft.com/pricing/details/private-link/). For more information about how these components work together, [watch this video](https://learn.microsoft.com/Shows/AI-Show/Azure-Cognitive-Search-Whats-new-in-security/player). Coverage of the private endpoint option starts at 5:48 into the video. For instructions on how to set up the endpoint, see [Create a Private Endpoint for Azure AI Search](service-create-private-endpoint.md).
 
 ### Network security perimeter
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートエンドポイントに関する記述の修正"
}
```

### Explanation
この変更では、`search-security-overview.md`という記事内のプライベートエンドポイントに関するセクションが修正されました。具体的には、関連するリンクやコンテンツがより適切にフォーマットされ、文の後半部分が整理されています。

以前の文から、セミコロンが削除され、リンクの後にスペースが追加されるなど、読みやすさを向上させるための小さな修正が行われています。内容としては、公私のエンドポイントを使用する際のコストについての留意点や、関連するビデオリンクが明記されています。

これらの変更は、ユーザーが情報をより効果的に理解しやすくするためのもので、特にプライベートエンドポイントの利用にあたっての注意点がわかりやすく伝わるようになっています。


