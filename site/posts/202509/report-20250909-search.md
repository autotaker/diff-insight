---
date: '2025-09-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:92e0baf...MicrosoftDocs:501869d
summary: この度の更新では、検索エージェントに新しいパラメータ`knowledgeSourceParams`が追加され、特定の知識ソースに基づいた情報取得が可能になりました。また、プライベートリンクを通じてOneLakeワークスペースに接続するためのリソース`Microsoft.Fabric/privateLinkServicesForFabric`も追加されました。さらに、`targetIndexParams`セクションが削除され、メッセージ形式の明確化や、新しい設定に関する指示が含まれています。これらの変更は、ユーザー体験を向上させることを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:92e0baf...MicrosoftDocs:501869d){target="_blank"}

# Highlights

## 新機能
1. 検索エージェントを使用した情報取得方法において、新しいパラメータ`knowledgeSourceParams`が追加されました。
   
2. プライベートリンクを通じたOneLakeワークスペースへの接続が可能となるためのリソース`Microsoft.Fabric/privateLinkServicesForFabric`が追加されました。

## 破壊的変更
- `targetIndexParams`セクションが削除され、新しい`knowledgeSourceParams`が導入され、特定の知識ソースに絞り込んで取得アクションを実行するオプションが追加されています。

## その他の更新
- メッセージ形式の明確化と、取得アクションによって返される応答の構造が強調されました。
- エージェントの定義や応答のためのセマンティックランキングの設定に関する指示が追加されました。
- Azureポータルを使用して`privateLinkServicesForFabric`リソースを作成する手順が紹介されました。

# Insights
この度のドキュメントの更新は、検索エージェントとプライベートリンクの設定における使用性と理解の向上を目的としています。

検索エージェントに関連する更新では、新たに導入された`knowledgeSourceParams`により、エージェントが複数の知識ソースを持つ際に特定のソースにフォーカスして情報を取得する機能が強化されました。これによって、開発者やユーザーがより精確な取得アクションを行えるようになり、効率的な情報活用が期待されます。また、設定の明確化によってエージェント機能の高度な利用が促進されます。

プライベートリンクに関連する部分では、`Microsoft.Fabric/privateLinkServicesForFabric`が追加され、OneLakeワークスペースへの安全な接続が可能となりました。Azure内でのネットワークのセキュリティとパフォーマンスを向上させるための重要なリンクとなるでしょう。これにより、ますます多くのユーザーがOneLakeワークスペースを利用する際の安心感を得ることができ、セキュリティに敏感な業務にも適応できるようになります。

これらの変更は、ユーザーのニーズに応じた柔軟性を提供し、結果としてより良いユーザー体験を生み出すのに貢献します。結果的に、ユーザーと開発者がそれぞれの環境で最適なソリューションを実装するための基盤となります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-agentic-retrieval-how-to-retrieve.md](#item-5f7fc0) | minor update | 検索エージェントによる取得方法の更新 | modified | 19 | 25 | 44 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | プライベートリンクのためのリソース追加 | modified | 4 | 0 | 4 | 


# Modified Contents
## articles/search/search-agentic-retrieval-how-to-retrieve.md{#item-5f7fc0}

<details>
<summary>Diff</summary>
````diff
@@ -67,7 +67,7 @@ POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-08-0
                 "content" : [
                   { "type" : "text", "text" : "You can answer questions about the Earth at night.
                     Sources have a JSON format with a ref_id that must be cited in the answer.
-                    If you do not have the answer, respond with "I don't know"." }
+                    If you do not have the answer, respond with 'I don't know'." }
                 ]
             },
             {
@@ -77,39 +77,29 @@ POST https://{{search-url}}/agents/{{agent-name}}/retrieve?api-version=2025-08-0
                 ]
             }
         ],
-    "targetIndexParams" :  [
-        { 
-            "indexName" : "{{index-name}}",
-            "filterAddOn" : "page_number eq '105'",
-            "IncludeReferenceSourceData": true, 
-            "rerankerThreshold" : 2.5,
-            "maxDocsForReranker": 50
-        } 
-    ]
+  "knowledgeSourceParams": [
+    {
+      "filterAddOn": null,
+      "knowledgeSourceName": "earth-at-night-blob-ks",
+      "kind": "searchIndex"
+    }
+  ]
 }
 ```
 
 **Key points**:
 
++ The retrieve action targets a [knowledge agent](search-agentic-retrieval-how-to-create.md). The knowledge agent specifies one or more knowledge sources and a knowledge source configuration. Review your knowledge agent definition for output and semantic ranking configuration.
+
 + `messages` articulates the messages sent to the model. The message format is similar to Azure OpenAI APIs.
 
   + `role` defines where the message came from, for example either `assistant` or `user`. The model you use determines which roles are valid.
 
-  + `content` is the message sent to the LLM. It must be text in this preview.
-
-+ `targetIndexParams` provide instructions on the retrieval. Currently in this preview, you can only target a single index. 
-
-  + `filterAddOn` lets you set an [OData filter expression](search-filters.md) for keyword or hybrid search.
+  + `content` is the message or prompt sent to the LLM. It must be text in this preview.
 
-  + `IncludeReferenceSourceData` tells the retrieval engine to return the source content in the response. This value is initially set in the knowledge agent definition. You can override that setting in the retrieve action to return original source content in the [references section](#review-the-references-array) of the response.
++ [`knowledgeSourceParams`](/rest/api/searchservice/knowledge-retrieval/retrieve?view=rest-searchservice-2025-08-01-preview#searchindexknowledgesourceparams&preserve-view=true) is optional. Specify a knowledge source if the agent has more than one, and you want to focus the retrieve action on just one knowledge source. If the knowledge agent has just one knowledge source with the configuration you want, you can omit this section.
 
-  + `rerankerThreshold` and `maxDocsForReranker` are also initially set in the knowledge agent definition as defaults. You can override them in the retrieve action to configure [semantic reranker](semantic-how-to-configure.md), setting minimum thresholds and the maximum number of inputs sent to the reranker.
-
-    `rerankerThreshold` is the minimum semantic reranker score that's acceptable for inclusion in a response. [Reranker scores](semantic-search-overview.md#how-results-are-scored) range from 1 to 4. Plan on revising this value based on testing and what works for your content.
-
-    `maxDocsForReranker` dictates the maximum number of documents to consider for the final response string. Semantic reranker accepts 50 documents. If the maximum is 200, four more subqueries are added to the query plan to ensure all 200 documents are semantically ranked. for semantic ranking. If the number isn't evenly divisible by 50, the query plan rounds up to nearest whole number. 
-
-    The `content` portion of the response consists of the 200 chunks or less, excluding any results that fail to meet the minimum threshold of a 2.5 reranker score.
+  A knowledge source specification on the retrieve action describes the target search index on the search service. So even if the knowledge source "kind" is Azure blob, the valid value here is `searchIndex`. In this first public preview release, `knowledgeSourceParams.kind` is always `searchIndex`.
 
 ## Review the extracted response
 
@@ -133,9 +123,13 @@ The body of the response is also structured in the chat message style format. Cu
 
 **Key points**:
 
-+ `content` is a JSON array. It's a single string composed of the most relevant documents (or chunks) found in the search index, given the query and chat history inputs. This array is your grounding data that a chat completion model uses to formulate a response to the user's question.
++ `content.text` is a JSON array. It's a single string composed of the most relevant documents (or chunks) found in the search index, given the query and chat history inputs. This array is your grounding data that a chat completion model uses to formulate a response to the user's question.
+
+  This portion of the response consists of the 200 chunks or less, excluding any results that fail to meet the minimum threshold of a 2.5 reranker score.
+
+  The string starts with the reference ID of the chunk (used for citation purposes), and any fields specified in the semantic configuration of the target index. In this example, you should assume the semantic configuration in the target index has a "title" field, a "terms" field, and a "content" field.
 
-+ "text" is the only valid value for `type`, and it consists of the reference ID of the chunk (used for citation purposes), and any fields specified in the semantic configuration of the target index. In this example, you should assume the semantic configuration in the target index has a "title" field, a "terms" field, and a "content" field. 
++ `content.type` has one valid value in this preview: `text`. 
 
 > [!NOTE]
 > The `maxOutputSize` property on the [knowledge agent](search-agentic-retrieval-how-to-create.md) determines the length of the string. We recommend 5,000 tokens.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索エージェントによる取得方法の更新"
}
```

### Explanation
このコードの変更は、検索エージェントを介した情報取得方法に関するドキュメントの更新に関連しています。主な変更点として、文の修正や新しいパラメータの追加が含まれています。この更新は、取得アクションに関連する構成オプションや設定を明確にし、プレビュー版の機能に関する理解を深めることを目的としています。

具体的には、`targetIndexParams`セクションが削除され、代わりに`knowledgeSourceParams`が新たに導入されました。これにより、エージェントが複数の知識ソースを持つ場合に、特定のソースに絞って取得アクションを実行するためのオプションが提供されます。また、メッセージの形式に関する明確化や、取得アクションによって返される応答の構造が強調されています。

新しいパラメータや役割の定義が追加され、エージェントの定義や、応答のためのセマンティックランキングの設定についての指示が含まれています。これにより、開発者やユーザーがより効果的にエージェント機能を活用できるようになります。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -116,6 +116,7 @@ You can create a shared private link for the following resources.
 | Microsoft.Sql/managedInstances (preview) <sup>5</sup>| `managedInstance` |
 | Microsoft.CognitiveServices/accounts <sup>6</sup> <sup>7</sup>| `openai_account` |
 | Microsoft.CognitiveServices/accounts <sup>8</sup> | `cognitiveservices_account` |
+| Microsoft.Fabric/privateLinkServicesForFabric <sup>9</sup> | `workspace` |
 
 <sup>1</sup> If Azure Storage and Azure AI Search are in the same region, the connection to storage is made over the Microsoft backbone network, which means a shared private link is redundant for this configuration. However, if you already set up a private endpoint for Azure Storage, you should also set up a shared private link or the connection is refused on the storage side. Also, if you're using multiple storage formats for various scenarios in search, make sure to create a separate shared private link for each subresource.
 
@@ -133,6 +134,8 @@ You can create a shared private link for the following resources.
 
 <sup>8</sup> Shared private links are now supported (as of November 2024) for connections to Azure AI services multi-service accounts. Azure AI Search connects to Azure AI services multi-service for [billing purposes](cognitive-search-attach-cognitive-services.md). These connections can now be private through a shared private link. Shared private link is only supported when configuring [a managed identity (keyless configuration)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) in the skillset definition. 
 
+<sup>9</sup> Shared private link is supported for connections to OneLake workspace. To create a `privateLinkServicesForFabric` resource specific to a workspace, [register](/azure/azure-resource-manager/management/resource-providers-and-types#register-resource-provider) `Microsoft.Fabric` namespace to your subscription and refer to step 2 as documented in [Create the private link service in Azure](/fabric/security/security-workspace-level-private-links-set-up#step-2-create-the-private-link-service-in-azure).
+
 ## 1 - Create a shared private link
 
 Use the Azure portal, Management REST API, the Azure CLI, or Azure PowerShell to create a shared private link.
@@ -310,6 +313,7 @@ Approval of the private endpoint connection is granted on the Azure PaaS side. E
 + On Azure Storage, use [Private Endpoint Connections - Put](/rest/api/storagerp/private-endpoint-connections/put)
 + On Azure Cosmos DB, use [Private Endpoint Connections - Create Or Update](/rest/api/cosmos-db-resource-provider/private-endpoint-connections/create-or-update)
 + On Azure OpenAI, use [Private Endpoint Connections - Create Or Update](/rest/api/aiservices/accountmanagement/private-endpoint-connections/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&preserve-view=true)
++ On Onelake, use [Private Endpoints - Approve via CLI](/cli/azure/network/private-endpoint-connection?view=azure-cli-latest#az-network-private-endpoint-connection-approve) or [Private Endpoints - Approve via Portal](/azure/private-link/manage-private-endpoint?tabs=manage-private-link-powershell#manage-private-endpoint-connections-on-azure-paas-resources)
 
 Using the Azure portal, perform the following steps:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートリンクのためのリソース追加"
}
```

### Explanation
このコードの変更は、プライベートリンクを通じたアクセスの設定に関するドキュメントの更新に関連しています。具体的には、`Microsoft.Fabric/privateLinkServicesForFabric`リソースが新たに追加され、これによりOneLakeワークスペースへの接続がプライベートリンクによってサポートされることが示されています。

新しいセクションでは、`privateLinkServicesForFabric`リソースを作成するための手順が紹介されており、Azureポータルの使用やリソースプロバイダーの登録方法についてのリンクが提供されています。また、プライベートエンドポイント接続の承認プロセスに関する情報も補足されています。この変更により、利用者はOneLakeワークスペースへの安全な接続をより容易に設定できるようになります。


