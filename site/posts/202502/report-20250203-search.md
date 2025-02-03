---
date: '2025-02-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5c1bed9...MicrosoftDocs:83a6833
summary: 今回の変更点は、Azure AI ドキュメントのセキュリティ理解を深めるために、画像の追加と文書の修正が行われました。主な内容には、APIキーの有効化を示す新しい画像「api-keys-enabled.png」の追加、既存文書のさらなる説明強化が含まれています。特に、APIキーの管理方法やコントロールプレーン操作に関する追加情報が反映されており、ユーザーがセキュリティ機能をより理解しやすくなることを目的としています。この改良は、特に企業や大規模プロジェクトにおけるセキュリティ管理を支援する重要なものです。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5c1bed9...MicrosoftDocs:83a6833){target="_blank"}

# Highlights
今回の変更点は、Azure AI ドキュメントのセキュリティに関する理解を深めるために、新たな画像の追加と既存文書の修正が含まれています。主なハイライトは以下の3点です。

## New features
- APIキーが有効化されていることを示す新しい画像「api-keys-enabled.png」が追加されました。これは特に視覚的にセキュリティ設定を理解するために役立ちます。

## Breaking changes
- 重大な変更はなく、全体的にドキュメントの改善や説明補強が行われています。

## Other updates
- 「Azure Cognitive Search」の文書では、コントロールプレーン操作におけるAPIキーの要求・ログ記録についての説明が追加。
- 「APIキー」に関するドキュメントでは、キー認証がデフォルトで有効になることや設定手順が補足され、利用者がAPIキーの管理を理解しやすくしています。

# Insights
このコード変更は、Azureのユーザーが検索サービスのセキュリティ機能をより理解し、適切に利用できるようにするために加えられています。具体的には、APIキーがセキュリティ管理にどのように関与しているかを視覚的なレベルと文章で詳説する設計意図を持っています。

新しい画像「api-keys-enabled.png」は、特に視覚的学習を好むユーザーにとって、APIキーの有効化状態を明確に理解する有力な手段となります。これはセキュリティに不安を感じる新しいユーザーに対して非常に効果的です。

また、「Azure Cognitive Search」の文書更新において、APIキーが無効でもログに記録されるという情報が追加されました。これにより、ユーザーはシステム内部でのリクエスト追跡について誤解することなく理解を深めることができます。

最後に、「APIキー」に関する文書の詳細化は、新規サービス利用者が初期設定を理解しやすくするだけでなく、既存ユーザーに対しても最新の状態に適応するサポートを提供します。

この一連の改良は、Azureの利用者がプラットフォームのセキュリティ機能に対してより精通し、安心して活用できるように設計されています。特に企業や大規模なプロジェクトにおいては、APIのセキュリティ管理がしっかりと整備されていることが事業継続には極めて重要であり、それを支援するための踏み台として、これらのドキュメントの改善は大いに役立ちます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [api-keys-enabled.png](#item-5ff7fd) | new feature | APIキーを有効にするための画像の追加 | added | 0 | 0 | 0 | 
| [monitor-azure-cognitive-search.md](#item-5be826) | minor update | Azure Cognitive Searchに関する文書の修正 | modified | 1 | 1 | 2 | 
| [search-security-api-keys.md](#item-d8c908) | minor update | APIキーに関するドキュメントの修正 | modified | 9 | 3 | 12 | 


# Modified Contents
## articles/search/media/search-security-overview/api-keys-enabled.png{#item-5ff7fd}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "APIキーを有効にするための画像の追加"
}
```

### Explanation
このコードの差分は、新しい画像ファイル「api-keys-enabled.png」の追加を示しています。このファイルは、Azure AI ドキュメントのセクション「search-security-overview」に関連しており、APIキーが有効化されていることを視覚的に示すために使用されます。この変更は、特にセキュリティに関する理解を深めるための新機能として重要です。ファイルのリンクは、GitHub のリポジトリ内で利用可能で、ユーザーが画像に直接アクセスできるようになっています。

## articles/search/monitor-azure-cognitive-search.md{#item-5be826}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ For the available resource log categories, their associated Log Analytics tables
 
 In Azure AI Search, activity logs reflect control plane activity such as service creation and configuration, or API key usage or management. Entries often include **Get Admin Key**, one entry for every call that [provided an admin API key](search-security-api-keys.md) on the request. There are no details about the call itself, just a notification that the admin key was used.
 
-API keys can be disabled for data plane operations, such as creating or querying an index, but on the control plane they're used in the Azure portal to return service information.
+API keys can be disabled for data plane operations, such as creating or querying an index, but on the control plane they're used in the Azure portal to return service information. Control plane operations can request API keys so you continue to see key-related requests in the Activity log even if you disable key-based authentication.
 
 The following screenshot shows Azure AI Search activity log signals you can configure in an alert.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Cognitive Searchに関する文書の修正"
}
```

### Explanation
このコードの差分は、「articles/search/monitor-azure-cognitive-search.md」ファイルの修正版を反映したものであり、内容の一部が変更されました。この修正では、コントロールプレーンの操作がAPIキーを要求できることについての説明が追加され、さらに、キーに基づく認証が無効になっても活動ログにはキーに関連するリクエストが表示され続けることが明示されています。これにより、ユーザーがAPIキーの使用法とその管理状態をより理解できるようになっています。変更の詳細は、GitHub内のファイルリンクから確認できます。

## articles/search/search-security-api-keys.md{#item-d8c908}

<details>
<summary>Diff</summary>
````diff
@@ -9,17 +9,23 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 1/16/2025
+ms.date: 01/31/2025
 #customer intent: I want to learn how to connect to Azure AI Search using API keys so that I can authenticate inbound requests to my search service.
 ---
 
 # Connect to Azure AI Search using keys
 
-Azure AI Search supports both keyless and key-based authentication for connections to your search service. An API key is a unique string composed of 52 randomly generated numbers and letters. In your source code, you can specify it as an [environment variable](/azure/ai-services/cognitive-services-environment-variables) or as an app setting in your project, and then reference the variable on the request. A request made to a search service endpoint is accepted if both the request and the API key are valid.
+Azure AI Search supports both keyless and key-based authentication for connections to your search service. An API key is a unique string composed of 52 randomly generated numbers and letters. In your source code, you can specify it as an [environment variable](/azure/ai-services/cognitive-services-environment-variables) or as an app setting in your project, and then reference the variable on the request.
 
 > [!IMPORTANT]
 > When you create a search service, key-based authentication is the default, but it's not the most secure option. We recommend that you replace it with [role-based access](search-security-enable-roles.md).
 
+## Enabled by default
+
+Key-based authentication is the default on new search services. A request made to a search service endpoint is accepted if both the request and the API key are valid, and your search service is configured to allow API keys on a request. In the Azure portal, authentication is specified on the **Keys** page under **Settings**. Either **API keys** or **Both** provide key support.
+
+:::image type="content" source="media/search-security-overview/api-keys-enabled.png" alt-text="Screenshot of the Keys page in the Azure portal.":::
+
 ## Types of API keys
 
 There are two kinds of keys used for authenticating a request:
@@ -95,7 +101,7 @@ A script example showing API key usage for various operations can be found at [Q
 
 **How API keys are used in the Azure portal**:
 
-+ Key authentication is built in. By default, the Azure portal tries API keys first. However, if you [disable API keys](search-security-enable-roles.md#disable-api-key-authentication) and set up role assignments, the Azure portal uses role assignments instead.
+Key authentication applies to data plane operations such as indexing and queries. It's enabled by default. However, if you [disable API keys](search-security-enable-roles.md#disable-api-key-authentication) and set up role assignments, the Azure portal uses role assignments instead.
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIキーに関するドキュメントの修正"
}
```

### Explanation
このコードの差分は、「articles/search/search-security-api-keys.md」ファイルの修正を示しており、いくつかの内容が更新されました。主な変更点として、日付の更新に加え、APIキーの認証についての具体的な説明が追加され、特に新しい検索サービスではキー認証がデフォルトで有効になることが強調されています。また、APIキーを利用したリクエスト処理がどのように行われるかおよびAzureポータルにおける設定手順が詳述されています。新しいセクションでは、キーの種類やデフォルト設定に関する情報が補足されており、全体的に利用者がAPIキーの取り扱いやセキュリティに関する理解を深めることができる内容となっています。変更についての詳細は、GitHubのリンクから確認できます。


