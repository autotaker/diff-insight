---
date: '2026-05-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:88d126b...MicrosoftDocs:75b1b08
summary: 'この記事の変更は、Azure AI Searchに関連するドキュメントの更新であり、新たに`ai-usage: ai-assisted`というメタデータの追加と、`x-ms-query-source-authorization`ヘッダー形式の変更が含まれています。具体的には、ヘッダーがBearerトークン形式からトークン形式に変更され、リクエストのAuthorizationヘッダーやユーザートークンに関する記述も修正されました。この更新は、アクセス制御の理解を深め、ドキュメントの信頼性を向上させることを目的としています。'
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:88d126b...MicrosoftDocs:75b1b08){target="_blank"}

# ハイライト
この記事の変更は、Azure AI Searchに関連するドキュメントの更新を含んでいます。変更点には、`ai-usage: ai-assisted`という新しいメタデータの追加と、`x-ms-query-source-authorization`ヘッダー形式の修正が含まれます。

## 新機能
- 記事に`ai-usage: ai-assisted`メタデータが追加されたこと。

## 互換性を損なう変更
- `x-ms-query-source-authorization`ヘッダーが、Bearerトークン形式から単なるトークン形式に変更されたこと。

## その他の更新
- リクエストのAuthorizationヘッダーおよびユーザートークンに関して、ドキュメント内の記述を修正。

# インサイト
このコード更新は、Azure AI Searchでのアクセス制御をより正確に表現するためのものであり、ドキュメントの信頼性と明確性を向上させる目的があります。`ai-usage: ai-assisted`というメタデータの追加は、AIアシスト機能が関与していることを明示するものと考えられ、将来的には機械学習や人工知能投入による改善を視野に入れていることを示唆しています。さらに、この更新により、ユーザーはBearerプレフィックスを持たないトークン形式の理解を深め、手順がより明確になります。この変更は、ユーザーがAzure AI Searchを使ってクエリを行う際、セキュリティラベルやトークン管理についてより正確に動作させることができるようになります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-query-access-control-rbac-enforcement.md](#item-d24df7) | minor update | 検索クエリのアクセス制御とRBAC強制に関する記事の更新 | modified | 3 | 2 | 5 | 
| [search-query-sensitivity-labels.md](#item-3e1f8a) | minor update | Microsoft Purview感度ラベルのクエリ時強制に関する記事の更新 | modified | 5 | 4 | 9 | 


# Modified Contents
## articles/search/search-query-access-control-rbac-enforcement.md{#item-d24df7}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ ms.reviewer: magottei
 ms.service: azure-ai-search
 ms.topic: concept-article
 ms.date: 01/15/2026
+ai-usage: ai-assisted
 ---
 
 # Query-time ACL and RBAC enforcement in Azure AI Search
@@ -123,8 +124,8 @@ After you set up permissions, you can run the query. The following example is a
 
 ```http
 POST {endpoint}/indexes('{indexName}')/search.post.search?api-version=2025-11-01-preview
-Authorization: Bearer {AUTH_TOKEN} 
-x-ms-query-source-authorization: Bearer {TOKEN} 
+Authorization: Bearer {AUTH_TOKEN}
+x-ms-query-source-authorization: {TOKEN}
 x-ms-enable-elevated-read: true
 
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索クエリのアクセス制御とRBAC強制に関する記事の更新"
}
```

### Explanation
この変更は、Azure AI Searchに関連する「検索クエリのアクセス制御とRBAC強制」に関するドキュメントを更新しています。主な修正点としては、記事に「ai-usage: ai-assisted」という新しいメタデータが追加され、リクエストのAuthorizationヘッダーとx-ms-query-source-authorizationヘッダーの内容が若干修正されています。具体的には、x-ms-query-source-authorizationヘッダーがBearerトークン形式から単なるトークン形式に変更されています。この更新は、ドキュメントの正確性を向上させ、ユーザーがAzure AI Searchでのクエリ時に必要なアクセス制御に関する情報を正しく理解できるようにするためのものです。

## articles/search/search-query-sensitivity-labels.md{#item-3e1f8a}

<details>
<summary>Diff</summary>
````diff
@@ -5,6 +5,7 @@ ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: concept-article
 ms.date: 03/05/2026
+ai-usage: ai-assisted
 ---
 
 # Query-time enforcement of Microsoft Purview sensitivity labels in Azure AI Search  
@@ -54,7 +55,7 @@ Both are required to authorize label-based visibility.
 | Input type | Description | Example source |
 |-------------|--------------|----------------|
 | Application role | Determines whether the calling app has permission to execute queries on the index. | `Authorization: Bearer <app-token>` |
-| User identity | Determines which sensitivity labels the end user is allowed to access. | `x-ms-query-source-authorization: Bearer <user-token>` |
+| User identity | Determines which sensitivity labels the end user is allowed to access. | `x-ms-query-source-authorization: <user-token>` |
 
 
 
@@ -84,13 +85,13 @@ If either condition fails, the document is omitted from the results.
 
 ## Query example
 
-Here's an example of a query request using Microsoft Purview sensitivity label enforcement.  
-The query token is passed in the request headers. Both headers must include valid bearer tokens representing the application and the end user.
+Here's an example of a query request using Microsoft Purview sensitivity label enforcement.
+The application token is passed as a bearer token in the `Authorization` header. The user token is passed as the raw token value in the `x-ms-query-source-authorization` header, without the `Bearer` prefix.
 
 ```http
 POST  {{endpoint}}/indexes/sensitivity-docs/docs/search?api-version=2025-11-01-preview
 Authorization: Bearer {{app-query-token}}
-x-ms-query-source-authorization: Bearer {{user-query-token}}
+x-ms-query-source-authorization: {{user-query-token}}
 Content-Type: application/json
 
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Purview感度ラベルのクエリ時強制に関する記事の更新"
}
```

### Explanation
この変更は、Azure AI SearchにおけるMicrosoft Purview感度ラベルのクエリ時強制に関するドキュメントを更新しました。主な修正点には、新しいメタデータ「ai-usage: ai-assisted」の追加と、ユーザーのトークンに関する記述の修正が含まれています。具体的には、x-ms-query-source-authorizationヘッダーの形式が変更され、Bearerプレフィックスが削除され、ユーザーのトークンは生のトークン値として渡されることが明確に説明されています。また、ドキュメント内のクエリの例も更新され、アプリケーショントークンがAuthorizationヘッダーにBearerトークンとして渡され、ユーザートークンがヘッダーにベアラプレフィックスなしで渡されるように指摘されています。この更新は、ユーザーが感度ラベルを適切に理解し、使用する際の助けになることを目的としています。


