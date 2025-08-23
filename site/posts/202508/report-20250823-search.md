---
date: '2025-08-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6ccc4b8...MicrosoftDocs:d96708b
summary: この修正では、Azure AI Searchの同時実行制御に関するドキュメントが改善されました。新たに追加された情報は、リソースの更新操作が直ちに完了しない場合があることを説明し、複数のクライアントによる同時更新時に発生する競合についての詳細を提供しています。また、エラーメッセージの処理方法に関する説明も含まれており、ETag管理とバージョン確認の重要性が強調されています。この更新は、Azure
  AI Searchを使用する開発者にとって特に重要で、システム設計に対する理解を深め、エラーハンドリングの計画を助けるものとなっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6ccc4b8...MicrosoftDocs:d96708b){target="_blank"}

# Highlights
この修正では、Azure AI Searchの同時実行制御に関するドキュメントが改善されました。新しい情報は、リソース更新操作が即時に完了しない場合があることを示し、複数のクライアントによる同時リソース更新時の競合と、それに対処するための楽観的同時実行モデルに関する詳細を提供しています。特に、ETag管理とバージョン確認の重要性が指摘され、エラーメッセージの処理方法も追加されています。

## New features
- 同時実行制御に関する詳細な説明の追加。
- 楽観的同時実行モデルの詳細。
- ETagの使用とリソースバージョン確認の説明強化。

## Breaking changes
なし。

## Other updates
- エラーメッセージ処理（HTTP 412と409）の方法についての説明追加。
- .NET SDKでのエラーハンドリングの方法について言及。

# Insights
この文書更新は、Azure AI Searchを使用する開発者にとって非常に重要です。複数のクライアントが同時にリソースを更新するシナリオは一般的であり、こうした状況における競合は避けられません。この更新により、リソース更新の直列化についての理解が促進され、競合が発生した際のエラーハンドリングを念頭に置いたシステム設計を助ける情報が提供されます。具体的な方法として、ETagの使用とバージョン管理の重要性が強調されており、開発者は競合時に具体的な指標を持つことができます。

また、開発者はHTTP 412または409エラーメッセージに対する応答の計画を立て、エラーの原因を迅速に特定し、対処するための手段を講じることが可能です。これらの更新により、Azure AI Searchを使用するアプリケーションはより堅牢で信頼性の高いものになるでしょう。エラーハンドリングに関する.NET SDKの言及は、特にクライアント側でのエラーマネジメントを考慮したい開発者にとって有益です。これにより、開発者はAzure AI Searchの運用効率を向上させる手段を得ることになります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-howto-concurrency.md](#item-863358) | minor update | Azure AI Searchの同時実行制御に関する更新 | modified | 8 | 4 | 12 | 


# Modified Contents
## articles/search/search-howto-concurrency.md{#item-863358}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,12 @@ ms.custom:
 
 # Manage concurrency in Azure AI Search
 
-When managing Azure AI Search resources such as indexes and data sources, it's important to update resources safely, especially if resources are accessed concurrently by different components of your application. When two clients concurrently update a resource without coordination, race conditions are possible. To prevent this, Azure AI Search uses an *optimistic concurrency model*. There are no locks on a resource. Instead, there's an ETag for every resource that identifies the resource version so that you can formulate requests that avoid accidental overwrites.
+When managing Azure AI Search resources such as indexes and data sources, it's important to update resources safely, especially if resources are accessed concurrently by different components of your application.
+
+* Resource update operations may not complete immediately. For example, [updating an index](search-howto-reindex.md#update-an-index-schema) or an [indexer](search-how-to-create-indexers.md) may take several seconds to complete. Resource updates are *serialized*, which means multiple update operations may not run simultaneously on the same resource.
+* When two clients concurrently update a resource without coordination, a *race condition* is possible. One client could start an update operation while the other client recieves a conflict error. To prevent this, Azure AI Search supports an *optimistic concurrency model*. There are no locks on a resource. Instead, there's an ETag for every resource that identifies the resource version so that you can formulate requests that avoid accidental overwrites.
+
+
 
 ## How it works
 
@@ -28,12 +33,11 @@ All resources have an [*entity tag (ETag)*](https://en.wikipedia.org/wiki/HTTP_E
 
 + The Azure SDK for .NET sets the ETag through an accessCondition class, setting the [If-Match | If-Match-None header](/rest/api/searchservice/common-http-request-and-response-headers-used-in-azure-search) on the resource. Objects that use ETags, such as [SynonymMap.ETag](/dotnet/api/azure.search.documents.indexes.models.synonymmap.etag) and [SearchIndex.ETag](/dotnet/api/azure.search.documents.indexes.models.searchindex.etag), have an accessCondition class.
 
-Every time you update a resource, its ETag changes automatically. When you implement concurrency management, all you're doing is putting a precondition on the update request that requires the remote resource to have the same ETag as the copy of the resource that you modified on the client. If another process changes the remote resource, the ETag doesn't match the precondition and the request fails with HTTP 412. If you're using the .NET SDK, this failure manifests as an exception where the `IsAccessConditionFailed()` extension method returns true.
+Every time you update a resource, its ETag changes automatically. When you implement concurrency management, all you're doing is putting a precondition on the update request that requires the remote resource to have the same ETag as the copy of the resource that you modified on the client. If another process changes the remote resource, the ETag doesn't match the precondition and the request fails with HTTP 412 or 409. If you're using the .NET SDK, this failure manifests as an exception where the `IsAccessConditionFailed()` extension method returns true.
 
 > [!Note]
 > There is only one mechanism for concurrency. It's always used regardless of which API or SDK is used for resource updates.
-
-Starting July 18, 2025, Azure AI Search began enforcing serialization for index creation and update operations to ensure consistency and reliability. This change aligns with long-standing best practices and the established behavior of the rest of operations in the service. As the rollout progresses across regions, you may begin seeing 409 conflict errors when sending concurrent or closely timed requests. To avoid these errors, ensure operations are not sent in parallel and follow the concurrency guidance outlined in this document.
+> Starting July 18, 2025, Azure AI Search began enforcing serialization for index creation and update operations to ensure consistency and reliability.
 
 ## Example
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchの同時実行制御に関する更新"
}
```

### Explanation
この修正では、Azure AI Searchにおけるリソースの管理、特に同時実行制御に関する説明が強化されました。新たに、リソース更新操作は即座に完了しない可能性があること、つまり特定の時間がかかることが追加され、リソース更新が直列化されることが強調されています。さらに、リソースを同時に更新する複数のクライアント間で競合が発生する可能性について説明がなされ、楽観的同時実行モデルがどのように機能するかについての詳細も提供されています。具体的には、ETagの管理方法や、リソースのバージョン確認が重要な役割を果たすことが述べられています。

この変更により、ユーザーは複数の更新が同時に発生した場合のリスクを理解し、エラーメッセージ（HTTP 412または409）による衝突をどのように処理するかについての理解が深まります。また、更新が失敗した場合の.NET SDKでのエラーハンドリングの方法も言及され、使用者にとってより明確で実用的な情報が提供されています。


