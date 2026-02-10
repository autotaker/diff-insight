---
date: '2026-02-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:675261b...MicrosoftDocs:dfb83c6
summary: この変更では、C#、Python、およびRESTを用いたSharePointインデックス化の手順に関するドキュメントが最新の情報に更新され、手順が明確化されました。具体的には、最新の.NET
  SDK、Pythonクライアントライブラリ、およびSearch Service REST APIsに関する情報が追加され、手順や認証に関する注意点が詳しく記載されています。特に重要なのは、手順の表現が具体的になり、認証についての注意喚起が行われたことで、ユーザーが手順を誤解するリスクが低減される点です。これにより、ユーザーは最新の技術情報に基づいて、より効率的に作業できるようになります。全体として、これらの変更はドキュメントの精度とユーザー体験を向上させる重要なアップデートです。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:675261b...MicrosoftDocs:dfb83c6){target="_blank"}

<format>
# ハイライト
この変更では、C#、Python、およびRESTを用いたSharePointインデックス化の手順に関する3つのドキュメントが、それぞれ最新の日付に更新され、手順の明確化が行われました。詳細な手順や認証に関する具体的な注意点が追加され、新しい技術情報が反映されています。

## 新機能

- 各ドキュメントにおいて、最新の.NET SDK（C#）、Pythonクライアントライブラリ、およびSearch Service REST APIsに関する情報が追加されました。

## 破壊的変更

- 特に破壊的な変更はありません。

## その他の更新

- `ms.date`フィールドの値を更新し、最新の情報を反映しました。
- 手順をより具体的でフォーマルな表現に修正しました。

# インサイト
マイナーアップデートとはいえ、これらの変更は非常に意味のあるもので、特に手順の明確化が顕著です。C#、Python、RESTのそれぞれのドキュメントにおいて、手順が「Completion of three SharePoint indexer configuration steps:」から「Completion of the following SharePoint indexer configuration steps:」に変更されたことで、具体的には何をすべきかがより明確になりました。

また、認証に関する注意点の追加は、特に実装段階でのエラーを減らすための重要な要素です。これにより、SharePointインデキサーを使用する際のセキュリティ設定や接続設定が明確化され、ユーザーが手順を誤解するリスクが低減されるでしょう。

さらに、技術情報（例えば最新のSDKやAPIバージョン）の追加により、ユーザーは常に最新の状態で作業を行えるようになります。このような情報は、特に最新の機能を利用した開発が求められる状況では欠かせないでしょう。

これらの更新は、ドキュメントの精度を高め、ユーザー体験を向上させるものであり、開発者にとって非常に役立つ更新と言えます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md](#item-2eb305) | minor update | エージェント知識ソースに関するSharePoint Indexed C# の手順の更新 | modified | 5 | 5 | 10 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-python.md](#item-923abb) | minor update | エージェント知識ソースに関するSharePoint Indexed Python の手順の更新 | modified | 5 | 5 | 10 | 
| [agentic-knowledge-source-how-to-sharepoint-indexed-rest.md](#item-e26ea0) | minor update | エージェント知識ソースに関するSharePoint Indexed RESTの手順の更新 | modified | 5 | 5 | 10 | 


# Modified Contents
## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md{#item-2eb305}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: heidisteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/20/2025
+ms.date: 02/04/2026
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -30,11 +30,11 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
 
 + Completion of the [SharePoint indexer prerequisites](../../search-how-to-index-sharepoint-online.md#prerequisites).
 
-+ Completion of three SharePoint indexer configuration steps:
++ Completion of the following SharePoint indexer configuration steps:
 
-  + [Step 1: Enable a managed identity for Azure AI Search](../../search-how-to-index-sharepoint-online.md#step-1-optional-enable-system-assigned-managed-identity)
-  + [Step 2: Choose between delegated or application permissions](../../search-how-to-index-sharepoint-online.md#step-2-decide-which-permissions-the-indexer-requires)
-  + [Step 3: Application registration step for Microsoft Entra ID authentication](../../search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration)
+  + [Step 1: Enable a managed identity for Azure AI Search](../../search-how-to-index-sharepoint-online.md#step-1-optional-enable-system-assigned-managed-identity) (required only for secretless authentication; skip if using a client secret)
+  + [Step 2: Choose either delegated or application permissions](../../search-how-to-index-sharepoint-online.md#step-2-decide-which-permissions-the-indexer-requires)
+  + [Step 3: Create a Microsoft Entra application registration](../../search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration) (for application permissions, you also configure a [client secret](../../search-how-to-index-sharepoint-online.md#using-client-secret) or [secretless authentication](../../search-how-to-index-sharepoint-online.md#using-secretless-authentication-to-obtain-application-tokens))
 
 + The latest preview version of the [`Azure.Search.Documents` client library](https://www.nuget.org/packages/Azure.Search.Documents/11.8.0-beta.1) for the .NET SDK.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースに関するSharePoint Indexed C# の手順の更新"
}
```

### Explanation
このコードの変更は、`agentic-knowledge-source-how-to-sharepoint-indexed-csharp.md`というドキュメントに対する minor update（マイナーアップデート）を示しています。主な内容として、日付の更新と手順の詳細が変更されています。

具体的には、最初に`ms.date`フィールドの値が2025年11月20日から2026年2月4日に変更されています。また、SharePointインデクサーの設定手順に関する文言が明確化されました。変更前は「Completion of three SharePoint indexer configuration steps:」でしたが、変更後は「Completion of the following SharePoint indexer configuration steps:」に修正されています。これにより、手順がより具体的かつ正式な表現になっています。

さらに、各手順に関する説明も強調され、特に秘密なしの認証に関する注意事項が追加されています。このように、利用者への指示がより明確に伝わるように改善されています。また、最新の.NET SDKに関する情報も追加され、このドキュメントの内容が最新の技術を反映していることが確認できます。

全体として、この更新はユーザーに対してより良い情報を提供するためのものであり、ユーザーが手順をより理解しやすくすることを目的としています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-python.md{#item-923abb}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: heidisteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/14/2025
+ms.date: 02/04/2026
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -30,11 +30,11 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
 
 + Completion of the [SharePoint indexer prerequisites](../../search-how-to-index-sharepoint-online.md#prerequisites).
 
-+ Completion of three SharePoint indexer configuration steps:
++ Completion of the following SharePoint indexer configuration steps:
 
-  + [Step 1: Enable a managed identity for Azure AI Search](../../search-how-to-index-sharepoint-online.md#step-1-optional-enable-system-assigned-managed-identity)
-  + [Step 2: Choose between delegated or application permissions](../../search-how-to-index-sharepoint-online.md#step-2-decide-which-permissions-the-indexer-requires)
-  + [Step 3: Application registration step for Microsoft Entra ID authentication](../../search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration)
+  + [Step 1: Enable a managed identity for Azure AI Search](../../search-how-to-index-sharepoint-online.md#step-1-optional-enable-system-assigned-managed-identity) (required only for secretless authentication; skip if using a client secret)
+  + [Step 2: Choose either delegated or application permissions](../../search-how-to-index-sharepoint-online.md#step-2-decide-which-permissions-the-indexer-requires)
+  + [Step 3: Create a Microsoft Entra application registration](../../search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration) (for application permissions, you also configure a [client secret](../../search-how-to-index-sharepoint-online.md#using-client-secret) or [secretless authentication](../../search-how-to-index-sharepoint-online.md#using-secretless-authentication-to-obtain-application-tokens))
 
 + The latest preview version of the [`azure-search-documents` client library](https://pypi.org/project/azure-search-documents/11.7.0b2/) for Python.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースに関するSharePoint Indexed Python の手順の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-sharepoint-indexed-python.md`というドキュメントに対する minor update（マイナーアップデート）を示しています。具体的には、日付の更新と手順の明確化が行われています。

最初に、`ms.date`フィールドの値が2025年11月14日から2026年2月4日に更新されました。これにより、ドキュメントの内容が最新の情報を反映していることが強調されています。

また、SharePointインデクサーの設定手順に関連する文言も改善されています。変更前は「Completion of three SharePoint indexer configuration steps:」と記載されていましたが、変更後は「Completion of the following SharePoint indexer configuration steps:」に改訂され、より具体的で明確な表現となっています。手順の詳細には、特に秘密なしの認証に関して具体的な条件が追加され、利用者に分かりやすく、正確な指示が提供されています。

さらに、最新のPython用クライアントライブラリに関する情報も追加され、利用者が最新の技術にアクセスしやすくなっています。これにより、ユーザーは手順をより効果的に理解し、実行することが可能になります。

全体として、この更新は情報の正確性を高め、ユーザー体験を向上させるものであり、信頼性のある指導を提供することを目的としています。

## articles/search/includes/how-tos/agentic-knowledge-source-how-to-sharepoint-indexed-rest.md{#item-e26ea0}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: heidisteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 11/14/2025
+ms.date: 02/04/2026
 ---
 
 [!INCLUDE [Feature preview](../previews/preview-generic.md)]
@@ -30,11 +30,11 @@ When you create an indexed SharePoint knowledge source, you specify a SharePoint
 
 + Completion of the [SharePoint indexer prerequisites](../../search-how-to-index-sharepoint-online.md#prerequisites).
 
-+ Completion of three SharePoint indexer configuration steps:
++ Completion of the following SharePoint indexer configuration steps:
 
-  + [Step 1: Enable a managed identity for Azure AI Search](../../search-how-to-index-sharepoint-online.md#step-1-optional-enable-system-assigned-managed-identity)
-  + [Step 2: Choose between delegated or application permissions](../../search-how-to-index-sharepoint-online.md#step-2-decide-which-permissions-the-indexer-requires)
-  + [Step 3: Application registration step for Microsoft Entra ID authentication](../../search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration)
+  + [Step 1: Enable a managed identity for Azure AI Search](../../search-how-to-index-sharepoint-online.md#step-1-optional-enable-system-assigned-managed-identity) (required only for secretless authentication; skip if using a client secret)
+  + [Step 2: Choose either delegated or application permissions](../../search-how-to-index-sharepoint-online.md#step-2-decide-which-permissions-the-indexer-requires)
+  + [Step 3: Create a Microsoft Entra application registration](../../search-how-to-index-sharepoint-online.md#step-3-create-a-microsoft-entra-application-registration) (for application permissions, you also configure a [client secret](../../search-how-to-index-sharepoint-online.md#using-client-secret) or [secretless authentication](../../search-how-to-index-sharepoint-online.md#using-secretless-authentication-to-obtain-application-tokens))
 
 + The [2025-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2025-11-01-preview&preserve-view=true) version of the Search Service REST APIs.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェント知識ソースに関するSharePoint Indexed RESTの手順の更新"
}
```

### Explanation
この変更は、`agentic-knowledge-source-how-to-sharepoint-indexed-rest.md`というドキュメントに対する minor update（マイナーアップデート）を示しています。主に日付の更新と手順の明確化が行われています。

まず、`ms.date`フィールドが2025年11月14日から2026年2月4日に変更され、ドキュメントの最新性が強調されています。また、SharePointインデクサーの設定手順に関しても文言が改善されています。変更前は「Completion of three SharePoint indexer configuration steps:」でしたが、変更後は「Completion of the following SharePoint indexer configuration steps:」に修正され、より具体的でわかりやすい表現となっています。

手順の内容には、特に秘密なしの認証に関連する注意事項が追加され、利用者がより正確に手順を理解できるように工夫されています。具体的には、手順の中で「client secret」を使用する場合には、省略することができる旨が記載されています。

さらに、最新のSearch Service REST APIsに関する情報も追加され、特定のプレビュー版のバージョンへのリンクが提示されています。これにより、ユーザーが最新の技術情報にアクセスしやすくなっています。

全体として、この更新はドキュメントの内容を最新の状態に保ち、ユーザーに対してより正確で明示的な情報を提供することを目的としています。


