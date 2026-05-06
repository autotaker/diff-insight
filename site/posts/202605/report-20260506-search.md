---
date: '2026-05-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:75b1b08...MicrosoftDocs:bce7ca0
summary: この更新は、Azure AI Searchにおける感度ラベルのクエリ強制に関する情報を改善しました。新機能や重大な変更はないものの、ユーザーが許可された情報のみを取得できるようにするためのガイドラインが追加されました。感度ラベルポリシーの明確化やアクセストークン取得についての詳細な技術情報が提供され、ユーザーはエンドツーエンドの設定の確認が容易になりました。この改善により、セキュアなアプリケーションの構築が促進されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:75b1b08...MicrosoftDocs:bce7ca0){target="_blank"}

# ハイライト
この更新では、Azure AI Searchのドキュメントにおける感度ラベルがクエリ時にどのように強制されるかに関する情報が改善されました。新しい機能や重大な変更はありませんが、ユーザーが許可された情報のみを取得できるようにするための改善が行われています。

## 新機能
特に新機能は追加されていませんが、感度ラベルポリシーの詳細をより明確にし、ユーザーが適切な設定を行えるようなガイドが追加されました。

## 重大な変更
重大な変更は特にありません。

## その他の更新
- 感度ラベルのポリシー表現がユーザーが許可されたドキュメントを取得できることをより明確に示すように変更されました。
- トークンの取得方法に関する詳細な技術情報が追加されています。
- 感度ラベルの設定とテストに関する例と手順が新たに追加され、これによりユーザーはエンドツーエンドのセットアップを正確に確認できます。

# 洞察
このドキュメントの更新は、Azure AI Searchを使用する際に感度ラベルのポリシーをしっかりと理解し、正確に実装できるようにするためのものです。特に「強制」（enforces）から「強制できる」（can enforce）へと表現が変更されたことで、利用者がどのようにこれらのポリシーを適用するかについての柔軟性が示されています。

また、アクセストークンの取得に関する具体的なフローと手順が明確に示されていることから、開発者は実際のアプリケーションにおいて自分の状況に応じたトークン管理を行う手助けを受けられます。特にローカル環境での開発とOBOフローのケースが考慮されており、適切なアクセストークンの管理ができることで、セキュアなアプリケーションが構築しやすくなります。

さらに、エンドツーエンドの設定とテストの例が提供されることにより、ユーザーは感度ラベルのポリシーが適切に機能することを簡単に確認できるようになり、実務的な導入のハードルを下げています。これは、セキュリティに敏感なデータの管理において信頼性を高める一助となるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-query-sensitivity-labels.md](#item-3e1f8a) | minor update | Azure AI Searchにおける感度ラベルのクエリ時の強制の改善 | modified | 45 | 6 | 51 | 


# Modified Contents
## articles/search/search-query-sensitivity-labels.md{#item-3e1f8a}

<details>
<summary>Diff</summary>
````diff
@@ -4,15 +4,15 @@ description: Learn how query-time enforcement of Microsoft Purview sensitivity l
 ms.reviewer: gimondra
 ms.service: azure-ai-search
 ms.topic: concept-article
-ms.date: 03/05/2026
+ms.date: 05/04/2026
 ai-usage: ai-assisted
 ---
 
 # Query-time enforcement of Microsoft Purview sensitivity labels in Azure AI Search  
 
 [!INCLUDE [Feature preview](./includes/previews/preview-generic.md)]
 
-At query time, Azure AI Search enforces sensitivity label policies defined in [Microsoft Purview](/purview/create-sensitivity-labels). These policies include evaluation of [READ usage rights](/purview/rights-management-usage-rights) tied to each document. As a result, users can only retrieve documents they are allowed to view.
+At query time, Azure AI Search can enforce sensitivity label policies defined in [Microsoft Purview](/purview/create-sensitivity-labels). These policies include the evaluation of [`EXTRACT` usage rights](/purview/rights-management-usage-rights) associated with each document, ensuring users can only retrieve documents they're permitted to access.
 
 This capability extends [document-level access control](search-document-level-access-overview.md) to align with your organization's [information protection and compliance requirements](/purview/create-sensitivity-labels) managed in Microsoft Purview.
 
@@ -62,10 +62,10 @@ Both are required to authorize label-based visibility.
 ### 2. Sensitivity label evaluation
 
 When a query request is received, Azure AI Search evaluates:
-1. The sensitivityLabel field in each indexed document (extracted from Microsoft Purview during ingestion).  
+1. The `sensitivityLabel` field in each indexed document (extracted from Microsoft Purview during ingestion).  
 2. The user's effective Purview permissions, as defined by Microsoft Entra ID and Purview label policy.  
 
-If the user isn't authorized for a document's sensitivity label with extract permissions, that document is excluded from the query results.
+If the user isn't authorized for a document's sensitivity label with `EXTRACT` permissions, that document is excluded from the query results.
 
 > [!NOTE]
 > Internally, the service builds dynamic access filters similar to RBAC enforcement.  
@@ -83,6 +83,34 @@ A document is included in the final result set only if:
 If either condition fails, the document is omitted from the results.
 
 
+
+## Acquire a user access token
+
+To query Azure AI Search using user context, you must acquire an access token that represents the signed-in user. The approach you use depends on whether you're testing locally with your own token, if you have access to the source document, or implementing the application flow that requires passing the end-user token.
+
+### For testing scenarios
+
+For local testing, you can retrieve a user access token using Azure CLI:
+
+```powershell
+$token = az account get-access-token `
+  --resource https://search.azure.com `
+  --query accessToken `
+  --output tsv
+```
+
+This approach uses your current Azure CLI login session, so you can use the context over documents you have `EXTRACT` permissions assigned via sensitivity labels. This method is intended for development and validation scenarios only.
+
+### Token acquisition for OBO scenarios
+
+Applications that implement the on-behalf-of (OBO) flow must acquire tokens through Microsoft Entra ID using a supported authentication library, such as the [Microsoft Authentication Library](/entra/identity-platform/msal-acquire-cache-tokens) (MSAL).
+
+In OBO scenarios, the token must be requested for the downstream API that the application calls. For example, when calling Azure AI Search, the resource URI is `https://search.azure.com/.default`.
+
+The `.default` scope requests all delegated permissions that have been pre-consented for the application for the specified resource.
+
+Sensitivity label permissions, including `EXTRACT`, aren't represented as OAuth scopes. These permissions are evaluated at runtime by the downstream service, such as Azure AI Search, based on the user identity in the token and the applied sensitivity label policy.
+
 ## Query example
 
 Here's an example of a query request using Microsoft Purview sensitivity label enforcement.
@@ -103,10 +131,21 @@ Content-Type: application/json
 
 ## Sensitivity label handling in Azure AI Search
 
-When Azure AI Search indexes document content with sensitivity labels from sources like SharePoint, Azure Blob, and others, it stores both the content and the label metadata. The search query returns indexed content along with the GUID that identifies the sensitivity label applied to the document, only if the user has data READ access for that document. This GUID uniquely identifies the label but doesn't include human-readable properties such as the label name or associated permissions. 
+When Azure AI Search indexes document content with sensitivity labels from sources like SharePoint, Azure Blob, and others, it stores both the content and the label metadata. The search query returns indexed content along with the GUID that identifies the sensitivity label applied to the document, only if the user has data `EXTRACT` access for that document assigned via the sensitivity label definition. This GUID uniquely identifies the label but doesn't include human-readable properties such as the label name or associated permissions. 
 
 Note that the GUID alone is insufficient for scenarios that include user interface because sensitivity labels often carry other policy controls enforced by [Microsoft Purview Information Protection](/purview/sensitivity-labels), such as: print permissions or screenshot and screen capture restrictions. Azure AI Search doesn't surface these capabilities.
 
 To display label names and/or enforce UI-specific restrictions, your application must call the Microsoft Purview Information Protection endpoint to retrieve full label metadata and associated permissions.
 
-You can use the GUID returned by Azure AI Search to resolve the label properties and call the [Purview Labels APIs](/graph/api/sensitivitylabel-get) to fetch the label name, description, and policy settings. This [end-to-end demo sample](https://aka.ms/Ignite25/aisearch-purview-sensitivity-labels-repo) includes code that shows how to call the endpoint from a user interface. It also demonstrates how to extract the label name and expose it as part of the citations used in your RAG applications or agents.
+You can use the GUID returned by Azure AI Search to resolve the label properties and call the [Purview Labels APIs](/graph/api/sensitivitylabel-get) to fetch the label name, description, and policy settings. 
+
+
+## End-to-end testing setup
+
+To help you validate your sensitivity label configuration in Azure AI Search, here's a [reference end-to-end setup](https://aka.ms/Ignite25/aisearch-purview-sensitivity-labels-repo).
+
+This repository demonstrates:
+- How to configure sensitivity labels sync and honoring in Azure AI Search
+- How to test ingestion and query-time enforcement scenarios for documents with sensitivity labels
+- How to extract the label name and expose it as part of the citations used in your RAG applications or agents.
+
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおける感度ラベルのクエリ時の強制の改善"
}
```

### Explanation
この変更は、Azure AI Searchにおける感度ラベルのクエリ時の強制機能に関連するドキュメントの内容を更新しています。具体的には、次の点が変更されました。 

1. **感度ラベルのポリシーの表現**: 文中の表現が「enforces」から「can enforce」へと変更され、ユーザーが許可されたドキュメントのみを取得できることが明示されています。また、「EXTRACT」の使用権に関連する詳細が強調されています。

2. **テクニカルな詳細の追加**: ユーザーアクセストークンの取得方法に関する具体的な指示が追加され、実際のローカル開発とOBO（他の者のために）フローのケースにおいてトークンを取得する手順が示されています。

3. **クエリ例と設定手順についての説明**: 感度ラベルの設定やテストのためのエンドツーエンドのセットアップに関する情報が、新たに追加され、適切な設定を検証するためのリファレンスが提供されています。

この変更は、ユーザーがAzure AI Searchを用いて、感度ラベルポリシーを効果的かつ正確に利用できるようにするためのものであり、実質的な改善を提供しています。


