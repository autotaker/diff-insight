---
date: '2026-10-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b7b13a9...MicrosoftDocs:9165cf1
summary: 'この報告書は、SharePointリモート知識ソースに関するドキュメントの更新内容をまとめたものです。主な変更点として、日付の修正、カスタム属性の追加、利用方法に関する詳細な説明があり、新しいメタデータ「ms.custom:
  doc-kit-assisted」が追加されました。破壊的変更はありません。また、ライセンスとペイ・アズ・ユー・ゴーの条件について詳細な説明が行われ、ユーザーが情報を理解しやすくなっています。この更新は、ユーザーエクスペリエンスを向上させ、システム導入のハードルを下げることを目的としています。'
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b7b13a9...MicrosoftDocs:9165cf1){target="_blank"}

# Highlights

SharePointリモート知識ソースに関するドキュメントが更新されました。主な変更点として、日付の修正、カスタム属性の追加、利用方法に関する詳細な説明が挙げられます。

## 新機能
- ドキュメントに「ms.custom: doc-kit-assisted」という新しいメタデータが追加されました。

## 破壊的変更
- 破壊的な変更はありません。

## その他の更新
- 日付の修正（以前は「09/03/2026」、更新後は「10/01/2026」）。
- SharePoint知識ソースの利用条件について、ライセンスとペイ・アズ・ユー・ゴーの詳細な説明が追加されました。

# Insights

この更新は、ドキュメントの明確性とユーザーの理解を深めることを目的としています。日付の更新は、情報の最新性を保つための基本的なメンテナンスです。新たに追加されたメタデータ「ms.custom: doc-kit-assisted」により、ドキュメントが特定のガイドラインやツールに関連していることを示しており、組織内部での管理に役立つ可能性があります。

リモートSharePoint知識ソースを利用する際のライセンスとペイ・アズ・ユー・ゴーの条件説明がさらに明確になったため、ユーザーは必要な条件を容易に理解し、Azure AI Searchを適切に活用するための準備をしやすくなりました。これにより、特に企業内でのシステム管理者や開発者が、リソースの許可や設定について迷うことなく進められるようになります。

このようなドキュメントの改善は、ユーザーエクスペリエンス向上にも繋がり、システムの導入ハードルを下げる効果が期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-sharepoint-remote.md](#item-79d019) | minor update | SharePointリモート知識ソースに関する更新 | modified | 8 | 3 | 11 | 


# Modified Contents
## articles/search/agentic-knowledge-source-how-to-sharepoint-remote.md{#item-79d019}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,8 @@ title: Create a SharePoint (Remote) Knowledge Source
 description: Learn how to create a remote SharePoint knowledge source, which tells an agentic retrieval engine in Azure AI Search to query SharePoint sites directly.
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 09/03/2026
+ms.date: 10/01/2026
+ms.custom: doc-kit-assisted
 ai-usage: ai-assisted
 zone_pivot_groups: search-csharp-python-rest
 #customer intent: As an application developer, I want to create a remote SharePoint knowledge source, scope its live content, and handle query-time user authorization and SharePoint response data so that agentic retrieval can use content each user is permitted to access.
@@ -19,7 +20,7 @@ A *remote SharePoint knowledge source* (preview) uses the [Copilot Retrieval API
 
 To limit sites or constrain search, set a [filter expression](#filter-expression-examples) to scope by URLs, date ranges, file types, and other metadata. The caller's identity must be recognized by both the Azure tenant and the Microsoft 365 tenant because the retrieval engine queries SharePoint on behalf of the user.
 
-Unlike indexed knowledge sources, remote SharePoint knowledge sources query live data directly at retrieval time. No search index or connection string is needed, and usage is billed through Microsoft 365 and a Copilot license.
+Unlike indexed knowledge sources, remote SharePoint knowledge sources query live data directly at retrieval time. You don't need a search index or connection string.
 
 ### Usage support
 
@@ -33,7 +34,11 @@ Unlike indexed knowledge sources, remote SharePoint knowledge sources query live
 
 + SharePoint in a Microsoft 365 tenant that's under the same Microsoft Entra ID tenant as Azure.
 
-+ A Microsoft 365 Copilot license for query-time access to SharePoint content.
++ For each user querying SharePoint content, either a [Microsoft 365 Copilot add-on license](/microsoft-365/copilot/microsoft-365-copilot-licensing) that includes Retrieval API usage or [Retrieval API pay-as-you-go consumption (preview)](/microsoft-365/copilot/extensibility/api/ai-services/retrieval/paygo-retrieval) enabled for that user.
+
+  To enable pay-as-you-go, you need Microsoft 365 admin access and **Owner** or **Contributor** access on an Azure subscription in good standing. You also need an Azure resource group. Your tenant must have at least one Microsoft 365 Copilot license before enablement and throughout pay-as-you-go use.
+
+  For users without a Copilot add-on license, [enable pay-as-you-go and configure billing](/microsoft-365/copilot/extensibility/api/ai-services/retrieval/paygo-retrieval#enable-and-disable-pay-as-you-go) in the Microsoft 365 admin center using that Azure subscription. Both payment options use the same remote SharePoint knowledge source configuration.
 
 + Permission to create knowledge sources. Configure [keyless authentication](search-get-started-rbac.md) with the **Search Service Contributor** role assigned to your user account (recommended) or use an [admin API key](search-security-api-keys.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SharePointリモート知識ソースに関する更新"
}
```

### Explanation
この変更は、SharePoint（リモート）知識ソースに関するドキュメントの更新です。主な修正には、日付の更新、カスタム属性の追加、そして利用方法に関する説明が含まれています。

具体的には、以前の日付「09/03/2026」が「10/01/2026」に修正され、ドキュメントに「ms.custom: doc-kit-assisted」という新しいメタデータが追加されました。また、リモートSharePoint知識ソースの利用時に必要とされるライセンスや、ペイ・アズ・ユー・ゴーの利用条件についての説明が詳述されました。これにより、ユーザーは必要なアクセス権と設定が理解しやすくなります。

全体的に、この修正はドキュメントの明確性を高め、ユーザーがAzure AI Searchを使用してSharePointのコンテンツを効果的に活用できるようにすることを目的としています。


