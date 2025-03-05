---
date: '2025-03-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bf9270b...MicrosoftDocs:71adf7f
summary: 今回のコード変更では、主にクイックスタートガイドやドキュメントの著者情報更新、説明改善、日付の新しさなどのマイナーな修正が行われました。特に新しいセキュリティ機能や関連技術設定の詳細が明確化され、利用者にとって理解しやすい内容となっています。顧客管理のキーサポートが導入され、重大な互換性の破壊的変更はありません。全体的に、ドキュメントの一貫性と可読性が向上され、ユーザーが最新のAzure
  AI Search技術を効果的に利用できるよう示されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:bf9270b...MicrosoftDocs:71adf7f){target="_blank"}

<format>
# Highlights
今回のコード変更では、さまざまなクイックスタートガイドやドキュメントに対して主に著者情報の更新、説明の改善、日付の新しさといったマイナーな修正が行われました。特に、新しいセキュリティ機能や関連する技術設定の詳細を明確にすることで、利用者が情報を理解しやすくすることを目的としている点が目立ちます。

## New features
- 顧客管理のキーサポートの導入。

## Breaking changes
- 重大な互換性の破壊的変更はありません。

## Other updates
- 各クイックスタートガイドにおける著者名の変更。
- 文書の日付の更新。
- Azure関連のドキュメントにおける設定や前提条件の説明の強化。

# Insights
今回の変更では、主にドキュメント全体の一貫性と可読性の向上を図っています。Azure AI Searchにおけるフルテキスト検索やベクトル検索、セキュリティ管理に至るまで、各ガイドは最新の情報に更新され利用者に役立つ具体的な手順が提供されています。

著者情報の変更と日付の更新は、ドキュメントが最新であることを示唆し、これにより内部的な管理情報を受け手視点で調和させる意図が見られます。また、前提条件やインデックス作成方法に関する具体的なガイドライン強化は、ユーザーが正確に手順を理解する助けとなっています。特にAzureポータルでの設定手順やリソース管理方法に関する更新は、クイックスタートを実行する際のしきい値を低下させています。

さらに、セキュリティ機能の強化において、顧客管理キーを使用した二段階の暗号化が紹介され、これにより情報の保護が強調されただけでなく、サービスのセキュリティ基準がより統一されたものになるよう配慮されています。合わせて、メタデータや画像の更新は、視覚的に理解を助ける手助けとなるため、ユーザー体験向上の一助となっています。

全体的に、これらの変更は、Azure AI Search関連技術に関する理解を深め、安全かつ効果的にその機能を利用するための導きとなるでしょう。ユーザーが最新の機能を活用しやすくなると同時に、ドキュメントの整合性と利便性がさらに引き上げられたと評価できます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [full-text-csharp.md](#item-2e943a) | minor update | C# 準備クイックスタートの更新 | modified | 6 | 5 | 11 | 
| [full-text-intro.md](#item-f655a1) | minor update | フルテキスト検索のイントロダクションの修正 | modified | 4 | 5 | 9 | 
| [full-text-java.md](#item-d659f9) | minor update | Java 用フルテキスト検索クイックスタートの更新 | modified | 5 | 5 | 10 | 
| [full-text-javascript.md](#item-568e3a) | minor update | JavaScript 用フルテキスト検索クイックスタートの更新 | modified | 5 | 5 | 10 | 
| [full-text-python.md](#item-9bba1c) | minor update | Python 用フルテキスト検索クイックスタートの更新 | modified | 6 | 6 | 12 | 
| [full-text-typescript.md](#item-6630e8) | minor update | TypeScript 用フルテキスト検索クイックスタートの更新 | modified | 5 | 5 | 10 | 
| [knowledge-store-create-portal.md](#item-9b92e5) | minor update | Azure ポータルでのナレッジストア作成クイックスタートの更新 | modified | 15 | 16 | 31 | 
| [cmk-key-identifier.png](#item-261b9d) | minor update | カスタマーマネージドキー識別子の画像更新 | modified | 0 | 0 | 0 | 
| [assign-key-vault-portal.png](#item-783436) | minor update | Key Vault ポータルでのキー割り当ての画像更新 | modified | 0 | 0 | 0 | 
| [assign-policy.png](#item-6fe584) | minor update | ポリシー割り当ての画像更新 | modified | 0 | 0 | 0 | 
| [effect-deny.png](#item-4245fe) | minor update | 拒否の影響に関する画像更新 | modified | 0 | 0 | 0 | 
| [search-create-app-portal.md](#item-19ab44) | minor update | アプリポータル作成ガイドの内容更新 | modified | 12 | 14 | 26 | 
| [search-explorer.md](#item-738774) | minor update | 検索エクスプローラーガイドの内容更新 | modified | 10 | 12 | 22 | 
| [search-get-started-arm.md](#item-9287ad) | minor update | ARMテンプレートを用いたデプロイガイドの更新 | modified | 12 | 12 | 24 | 
| [search-get-started-bicep.md](#item-731b0e) | minor update | Bicepファイルを用いたデプロイガイドの更新 | modified | 10 | 10 | 20 | 
| [search-get-started-portal-image-search.md](#item-438b9b) | minor update | ポータルでの画像検索クイックスタートの更新 | modified | 12 | 13 | 25 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | ポータルでのベクター検索クイックスタートの更新 | modified | 10 | 10 | 20 | 
| [search-get-started-portal.md](#item-6d0cb1) | minor update | ポータルでのキーワード検索クイックスタートの更新 | modified | 5 | 5 | 10 | 
| [search-get-started-powershell.md](#item-4435d0) | minor update | PowerShellを使用したインデックス作成クイックスタートの更新 | modified | 11 | 9 | 20 | 
| [search-get-started-rag.md](#item-05ff0e) | minor update | 生成的検索（RAG）クイックスタートの更新 | modified | 16 | 21 | 37 | 
| [search-get-started-rbac.md](#item-9d96c1) | minor update | キーを使わない接続のクイックスタートの更新 | modified | 7 | 8 | 15 | 
| [search-get-started-rest.md](#item-0df9d5) | minor update | REST APIを使用したキーワード検索のクイックスタートの更新 | modified | 11 | 11 | 22 | 
| [search-get-started-semantic.md](#item-2b3902) | minor update | セマンティックランキングの追加に関するクイックスタートの更新 | modified | 17 | 16 | 33 | 
| [search-get-started-skillset.md](#item-079744) | minor update | Azureポータルでのスキルセット作成に関するクイックスタートの更新 | modified | 7 | 8 | 15 | 
| [search-get-started-text.md](#item-935941) | minor update | Azure SDKを使用したフルテキスト検索に関するクイックスタートの更新 | modified | 5 | 3 | 8 | 
| [search-get-started-vector.md](#item-4984d9) | minor update | REST APIを使ったベクトル検索に関するクイックスタートの更新 | modified | 10 | 11 | 21 | 
| [search-manage.md](#item-4043d7) | minor update | Azureポータルでのサービス構成に関するアップデート | modified | 58 | 79 | 137 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | Azure AI Searchの暗号化キー管理に関する記事の更新 | modified | 134 | 122 | 256 | 
| [search-security-overview.md](#item-6b3f1e) | minor update | Azure AI Searchのセキュリティ概要の更新 | modified | 22 | 6 | 28 | 
| [search-semi-structured-data.md](#item-d3388d) | minor update | セミ構造化データに関するドキュメントの接続文字列の修正 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c4768f) | minor update | 目次ファイルの更新 | modified | 2 | 2 | 4 | 
| [whats-new.md](#item-fa71b4) | minor update | 2025年2月の新機能の追加 | modified | 7 | 1 | 8 | 


# Modified Contents
## articles/search/includes/quickstarts/full-text-csharp.md{#item-2e943a}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,10 @@
 ---
 manager: nitinme
-author: eric-urban
-ms.author: eur
+author: haileytap
+ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/12/2025
+ms.date: 03/04/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
@@ -14,12 +14,13 @@ ms.date: 2/12/2025
 
 ## Prerequisites
 
-- An active Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. For this quickstart, you can use a free service.
 
 ## Microsoft Entra ID prerequisites
 
 For the recommended keyless authentication with Microsoft Entra ID, you need to:
+
 - Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
 - Assign both of the `Search Service Contributor` and `Search Index Data Contributor` roles to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**. For more information, see [Connect to Azure AI Search using roles](../../search-security-rbac.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# 準備クイックスタートの更新"
}
```

### Explanation
このコード変更は、C# 用のフルテキスト検索に関するクイックスタートガイドの内容を更新するものです。修正内容には、著者情報の変更、日付の更新、およびプラットフォーム固有の認証手順に関連する説明が含まれています。具体的には、著者の名前を「eric-urban」から「haileytap」に変更し、著者のマイクロソフト ID を「eur」から「haileytapia」に変更しました。また、文書の日付も「2025年2月12日」から「2025年3月4日」に更新されています。

既存の前提条件のリストも調整され、特に Azure アカウントに関する情報がより明確に記述され、読者が無料でアカウントを作成できるリンクが追加されました。さらに、Microsoft Entra ID を使用したキーレス認証についての手順も追加され、Azure CLI のインストールを促す文が含まれています。この更新により、ユーザーが必要な準備を整えるための情報がより具体的かつ最新のものとなっています。

## articles/search/includes/quickstarts/full-text-intro.md{#item-f655a1}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +1,12 @@
 ---
 manager: nitinme
-author: eric-urban
-ms.author: eur
+author: haileytap
+ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/19/2025
+ms.date: 03/04/2025
 ---
 
-Learn how to use the *Azure.Search.Documents* client library to create, load, and query a search index using sample data for [full text search](../../search-lucene-query-architecture.md). Full text search uses Apache Lucene for indexing and queries, and a BM25 ranking algorithm for scoring results.
+In this quickstart, you use the Azure.Search.Documents client library to create, load, and query a search index using sample data for [full text search](../../search-lucene-query-architecture.md). Full text search uses Apache Lucene for indexing and queries, and a BM25 ranking algorithm for scoring results.
 
 This quickstart creates and queries a small hotels-quickstart index containing data about four hotels.
-
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フルテキスト検索のイントロダクションの修正"
}
```

### Explanation
このコードの変更は、フルテキスト検索に関するイントロダクションガイドを更新するものです。主な修正内容には、著者情報、文書の日付、及び内容の表現方法が含まれています。具体的には、著者を「eric-urban」から「haileytap」に変更し、著者のマイクロソフト ID を「eur」から「haileytapia」に変更しました。また、文書の日付は「2025年2月19日」から「2025年3月4日」に更新されています。

内容の表現に関しては、「このクイックスタートでは」というフレーズが追加され、記述がより具体的で親しみやすくなりました。文書は引き続き、*Azure.Search.Documents* クライアントライブラリを使用して、サンプルデータを用いた検索インデックスの作成、ロード、クエリの実行方法を説明しています。この変更により、読者に対する説明がわかりやすくなり、文書の全体的な可読性が向上しました。

## articles/search/includes/quickstarts/full-text-java.md{#item-d659f9}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,10 @@
 ---
 manager: nitinme
-author: eric-urban
-ms.author: eur
+author: haileytap
+ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/12/2025
+ms.date: 03/04/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
@@ -14,8 +14,8 @@ ms.date: 2/12/2025
 
 ## Prerequisites
 
-- An active Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. For this quickstart, you can use a free service.
 
 ## Microsoft Entra ID prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java 用フルテキスト検索クイックスタートの更新"
}
```

### Explanation
このコード変更は、Java 用のフルテキスト検索に関するクイックスタートガイドを更新するものです。変更の主な内容は、著者情報、文書の日付、及び前提条件の説明が変更された点です。具体的には、著者を「eric-urban」から「haileytap」に変更し、著者のマイクロソフト ID を「eur」から「haileytapia」に変更しました。また、文書の日付も「2025年2月12日」から「2025年3月4日」に更新されています。

前提条件のリストについても修正が行われており、Azure アカウントに関する情報が明確に記述され、読者が無料でアカウントを作成できるリンクが追加されました。この変更により、ユーザーが必要な準備を整えるための情報が最新のものとなり、クイックスタートを行う際の理解が深まるようになっています。また、非公式のリンクを適切なものに更新し、文書全体の正確性が向上しました。

## articles/search/includes/quickstarts/full-text-javascript.md{#item-568e3a}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,10 @@
 ---
 manager: nitinme
-author: eric-urban
-ms.author: eur
+author: haileytap
+ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/19/2025
+ms.date: 03/04/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
@@ -14,8 +14,8 @@ ms.date: 2/19/2025
 
 ## Prerequisites
 
-- An active Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. For this quickstart, you can use a free service.
 
 ## Microsoft Entra ID prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript 用フルテキスト検索クイックスタートの更新"
}
```

### Explanation
このコードの変更は、JavaScript 用のフルテキスト検索に関するクイックスタートガイドを更新することを目的としています。主な修正点には、著者情報、文書の日付、および前提条件の説明が含まれています。著者は「eric-urban」から「haileytap」に変更され、著者のマイクロソフト ID も「eur」から「haileytapia」に変更されました。文書の日付は「2025年2月19日」から「2025年3月4日」に更新されています。

前提条件セクションでは、Azure アカウントに関する記述が明確になり、無料でアカウントを作成できるリンクも示されています。この変更により、読者は必要な準備を簡単に整えることができるようになり、クイックスタートを実行する際の理解が改善されます。また、非公式なリンクが公式なものに更新され、文書全体の整合性が向上しました。これにより、利用者がスムーズに情報を取得できるようになっています。

## articles/search/includes/quickstarts/full-text-python.md{#item-9bba1c}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,10 @@
 ---
 manager: nitinme
-author: eric-urban
-ms.author: eur
+author: haileytap
+ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/22/2025
+ms.date: 03/04/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
@@ -14,9 +14,9 @@ ms.date: 2/22/2025
 
 ## Prerequisites
 
-- An active Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
-- [Visual Studio Code with the Python extension](https://code.visualstudio.com/docs/languages/python), or an equivalent IDE, with Python 3.10 or later. If you don't have a suitable version of Python installed, you can follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter).
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. For this quickstart, you can use a free service.
+- [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python), or an equivalent IDE with Python 3.10 or later. If you haven't installed a suitable version of Python, follow the instructions in the [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter).
 
 ## Microsoft Entra ID prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python 用フルテキスト検索クイックスタートの更新"
}
```

### Explanation
このコード変更は、Python 用のフルテキスト検索に関するクイックスタートガイドを更新することを目的としています。主要な修正点には、著者情報、文書の日付、及び前提条件の表現が含まれています。著者は「eric-urban」から「haileytap」に変更され、著者のマイクロソフト ID も「eur」から「haileytapia」に更新されました。また、文書の日付は「2025年2月22日」から「2025年3月4日」に修正されています。

前提条件セクションでの変更は、Azure アカウントに関する情報がより明瞭になり、無料でアカウントを作成できるリンクが新たに追加されました。さらに、Visual Studio Code とその Python 拡張に関する情報も強化され、適切なリンクが追加されています。これにより、ユーザーが必要な準備をより円滑に行うことができるようになっており、クイックスタートを実施する際の利便性が向上しています。全体として、情報の正確性と明確性が改善されています。

## articles/search/includes/quickstarts/full-text-typescript.md{#item-6630e8}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +1,10 @@
 ---
 manager: nitinme
-author: eric-urban
-ms.author: eur
+author: haileytap
+ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/19/2025
+ms.date: 03/04/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
@@ -14,8 +14,8 @@ ms.date: 2/19/2025
 
 ## Prerequisites
 
-- An active Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>
-- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+- An Azure AI Search service. [Create a service](../../search-create-service-portal.md) if you don't have one. For this quickstart, you can use a free service.
 
 ## Microsoft Entra ID prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScript 用フルテキスト検索クイックスタートの更新"
}
```

### Explanation
このコード変更は、TypeScript 用のフルテキスト検索に関するクイックスタートガイドを改訂することを目的としています。主な変更点として、著者の情報、文書の日付、および前提条件が更新されています。著者は「eric-urban」から「haileytap」に変更され、著者のマイクロソフト ID も「eur」から「haileytapia」に更新されました。また、文書の日付は「2025年2月19日」から「2025年3月4日」に修正されました。

前提条件セクションでは、Azure アカウントに関する説明が明確化され、無料でアカウントを作成できるリンクが追加されました。この変更により、読者は必要な準備をしやすくなり、クイックスタートを実行する際の理解が向上します。また、非公式なリンクが公式のリンクに更新され、情報の正確性が強化されています。全体として、ユーザーがフルテキスト検索機能を利用するために必要な情報がより分かりやすくなっています。

## articles/search/knowledge-store-create-portal.md{#item-9b92e5}

<details>
<summary>Diff</summary>
````diff
@@ -1,41 +1,40 @@
 ---
-title: "Quickstart: Create a knowledge store in the Azure portal"
+title: "Quickstart: Create a Knowledge Store in the Azure Portal"
 titleSuffix: Azure AI Search
-description: Use the Import data wizard to create a knowledge store used for persisting enriched content. Connect to a knowledge store for analysis from other apps, or send enriched content to downstream processes.
-author: HeidiSteen
-ms.author: heidist
+description: Learn how to use the Import Data wizard to create a knowledge store for persisting enriched content. Connect to a knowledge store for analysis from other apps or send enriched content to downstream processes.
+author: haileytap
+ms.author: haileytapia
 manager: nitinme
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 12/10/2024
+ms.date: 03/04/2025
 ms.custom:
   - mode-ui
   - ignite-2023
 ---
 
 # Quickstart: Create a knowledge store in the Azure portal
 
-In this quickstart, you create a [knowledge store](knowledge-store-concept-intro.md) that serves as a repository for output generated from an [AI enrichment pipeline](cognitive-search-concept-intro.md) in  Azure AI Search. A knowledge store makes generated content available in Azure Storage for workloads other than search.
+In this quickstart, you create a [knowledge store](knowledge-store-concept-intro.md) that serves as a repository for output generated from an [AI enrichment pipeline](cognitive-search-concept-intro.md) in Azure AI Search. A knowledge store makes generated content available in Azure Storage for workloads other than search.
 
-First, you set up some sample data in Azure Storage. Next, you run the **Import data** wizard to create an enrichment pipeline that also generates a knowledge store. The knowledge store contains original source content pulled from the data  source (customer reviews of a hotel), plus AI-generated content that includes a sentiment label, key phrase extraction, and text translation of non-English customer comments.
+First, you set up sample data in Azure Storage. Next, you run the **Import data** wizard to create an enrichment pipeline that also generates a knowledge store. The knowledge store contains original source content pulled from the data source (customer reviews of a hotel), plus AI-generated content that includes a sentiment label, key phrase extraction, and text translation of non-English customer comments.
 
 ## Prerequisites
 
-Before you begin, have the following prerequisites in place:
-
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/).
 
-+ Azure AI Search. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your account. You can use a free service for this quickstart. 
++ An Azure AI Search service. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription. For this quickstart, you can use a free service.
 
-+ Azure Storage. [Create an account](/azure/storage/common/storage-account-create) or [find an existing account](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Storage%2storageAccounts/). The account type must be **StorageV2 (general purpose V2)**.
++ An Azure Storage account. [Create an account](/azure/storage/common/storage-account-create) or [find an existing account](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Storage%2storageAccounts/). The account type must be **StorageV2 (general purpose V2)**.
 
 + Sample data hosted in Azure Storage:
 
-  [Download HotelReviews_Free.csv](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotelreviews/HotelReviews_data.csv). This CSV contains 19 pieces of customer feedback about a single hotel (originates from Kaggle.com). The file is in a repo with other sample data. If you don't want the whole repo, copy the raw content and paste it into a spreadsheet app on your device.
+  + [Download HotelReviews_Free.csv](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotelreviews/HotelReviews_data.csv), which contains 19 pieces of customer feedback about a single hotel (originates from Kaggle.com). This CSV is in a repo with other sample data. If you don't want the whole repo, copy the raw content and paste it into a spreadsheet app on your device.
 
-  [Upload the file to a blob container](/azure/storage/blobs/storage-quickstart-blobs-portal) in Azure Storage.
+  + [Upload the file to a blob container](/azure/storage/blobs/storage-quickstart-blobs-portal) in Azure Storage.
 
-This quickstart also uses [Azure AI services](https://azure.microsoft.com/services/cognitive-services/) for AI enrichment. Because the workload is so small, Azure AI services is tapped behind the scenes for free processing for up to 20 transactions. This means that you can complete this exercise without having to create an extra Azure AI multi-service resource.
+> [!NOTE]
+> This quickstart uses [Azure AI services](https://azure.microsoft.com/services/cognitive-services/) for AI enrichment. Because the workload is so small, Azure AI services is tapped behind the scenes for free processing for up to 20 transactions. This means that you can complete this exercise without having to create an extra Azure AI multi-service resource.
 
 ## Start the wizard
 
@@ -173,9 +172,9 @@ If you're using a free service, remember that you're limited to three indexes, i
 > [!TIP]
 > If you want to repeat this exercise or try a different AI enrichment walkthrough, delete the **hotel-reviews-idxr** indexer and the related objects to recreate them. Deleting the indexer resets the free daily transaction counter to zero.
 
-## Next steps
+## Next step
 
-Now that you've been introduced to a knowledge store, take a closer look at each step by switching over to the REST API walkthrough. Tasks that the wizard handled internally are explained in the REST walkthrough.
+Now that you've been introduced to a knowledge store, take a closer look at each step by completing the REST API walkthrough. The walkthrough explains tasks that the wizard handled internally.
 
 > [!div class="nextstepaction"]
 > [Create a knowledge store using REST](knowledge-store-create-rest.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure ポータルでのナレッジストア作成クイックスタートの更新"
}
```

### Explanation
このコード変更は、Azure ポータルでナレッジストアを作成する際のクイックスタートガイドを改訂することを目的としています。主な修正点として、タイトルの表記、文書の説明、著者情報、日付、及び前提条件が更新されています。タイトルが「knowledge store from」から「Knowledge Store in」に変更され、内容の説明も「Use the Import data wizard to create...」から「Learn how to use the Import Data wizard to create...」に改められ、より明瞭になりました。

著者の名前が「HeidiSteen」から「haileytap」に変更され、著者 ID も「heidist」から「haileytapia」に更新されています。また、日付が「2024年12月10日」から「2025年3月4日」に修正されています。

前提条件セクションでは、Azure アカウントやサービスの必要性が強調され、リンクも更新されました。具体的には「An Azure account with an active subscription」や「An Azure AI Search service」の情報が追加され、利用者が必要なリソースにアクセスしやすくなりました。サンプルデータのダウンロードやアップロードに関する手順も明確化されています。さらに、AI 拡張機能の使用に関する注意書きが強化され、小規模なワークロードであれば追加のリソースを作成する必要がない旨が明記されています。

全体として、文書はユーザーにとっての理解を深めるように改善され、ナレッジストアを効果的に利用するための手順がより親しみやすくなっています。

## articles/search/media/search-manage-encryption-keys/cmk-key-identifier.png{#item-261b9d}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタマーマネージドキー識別子の画像更新"
}
```

### Explanation
このコード変更は、カスタマーマネージドキー（CMK）識別子に関する画像ファイルの修正を示しています。具体的には、ファイル名が「cmk-key-identifier.png」で、画像自体に変更はありませんが、画像の管理や表示に関連するメタデータやコンテンツの更新が行われた可能性があります。

この変更により、ドキュメント内のカスタマーマネージドキーに関する説明が視覚的に補強され、ユーザーがキーの識別や管理のプロセスを理解しやすくなることが期待されます。画像部分に関する他の要素が変更された場合も考慮されますが、具体的な内容についてはこの変更記録からは読み取れません。全体としては、ユーザーにとっての視覚的な情報提供が改善され、より良い理解を促進する役割を果たします。

## articles/search/media/search-security-manage-encryption-keys/assign-key-vault-portal.png{#item-783436}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Key Vault ポータルでのキー割り当ての画像更新"
}
```

### Explanation
このコード変更は、Key Vault ポータルでのキーの割り当てに関する画像「assign-key-vault-portal.png」が修正されたことを示しています。変更記録には、具体的な追加や削除の内容は示されていませんが、この画像のバージョンが更新されたことが想定されます。

画像の更新により、ユーザーはキーの割り当て手順を視覚的に理解しやすくなり、手順の正確性や明確性を向上させることが期待されます。特にセキュリティや暗号化キーの管理において、適切なビジュアル情報が重要であるため、今回の変更はその観点からも有益と言えます。全体として、この改訂によりドキュメントの内容が強化され、ユーザーの体験が向上することを目的としています。

## articles/search/media/search-security-manage-encryption-keys/assign-policy.png{#item-6fe584}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポリシー割り当ての画像更新"
}
```

### Explanation
このコード変更は、暗号化キー管理に関連する「assign-policy.png」という画像が修正されたことを示しています。具体的には、ファイルには変更がないとされており、画像のバージョンが更新された可能性があります。

画像の更新は、ポリシーの割り当て手順を視覚的に解説するためのものであり、ユーザーがキー管理のプロセスをより理解しやすくすることを目指しています。このようなビジュアル情報の強化により、ドキュメントの理解が向上し、特にセキュリティ関連の手続きにおいて閲覧者が直面する混乱を軽減する役割を果たすことが期待されます。全体として、ユーザーエクスペリエンスの向上に寄与する小さな改善と言えるでしょう。

## articles/search/media/search-security-manage-encryption-keys/effect-deny.png{#item-4245fe}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "拒否の影響に関する画像更新"
}
```

### Explanation
このコード変更は、「effect-deny.png」という画像が修正されたことを示しています。詳細な変更内容は記載されていませんが、画像自体のバージョンが更新されたことが考えられます。

この画像は、暗号化キー管理の拒否の影響を示すものであり、ユーザーがこの概念を視覚的に理解する手助けをするために重要です。画像の更新により、関連する情報がより明確になる可能性があり、結果としてドキュメントの使いやすさが向上します。このような微細な改善は、特にセキュリティに関するトピックにおいて重要であり、ユーザーが適切に情報を扱うための参考となるでしょう。全体として、ユーザーエクスペリエンスを向上させるための価値ある更新と言えます。

## articles/search/search-create-app-portal.md{#item-19ab44}

<details>
<summary>Diff</summary>
````diff
@@ -1,37 +1,35 @@
 ---
-title: "Quickstart: Create a demo search app in Azure portal"
+title: "Quickstart: Create a Demo App in the Azure Portal"
 titleSuffix: Azure AI Search
 description: Run the Create demo app wizard to generate HTML pages and script for an operational web app. The page includes a search bar, results area, sidebar, and typeahead support.
 manager: nitinme
-author: HeidiSteen
-ms.author: heidist
+author: haileytap
+ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 12/04/2024
+ms.date: 03/04/2025
 ms.custom:
   - mode-ui
   - ignite-2023
 ---
 
 # Quickstart: Create a demo search app in the Azure portal
 
-In this quickstart for Azure AI Search, learn how to use the Azure portal's **Create demo app** wizard to generate a downloadable, "localhost"-style web app that runs in a browser. Depending on how you configure it, the generated app is operational on first use, with a live read-only connection to an index on your search service. A default app can include a search bar, results area, sidebar filters, and typeahead support.
+In this quickstart, you use the **Create demo app** wizard in the Azure portal to generate a downloadable, "localhost"-style web app that runs in a browser. Depending on how you configure it, the generated app is operational on first use, with a live read-only connection to an index on your search service. A default app can include a search bar, results area, sidebar filters, and typeahead support.
 
-A demo app can help you visualize how an index will function in a client app, but it isn't intended for production scenarios. Production apps should include security, error handling, and hosting logic that the demo app doesn't provide. 
+A demo app can help you visualize how an index will function in a client app, but it isn't intended for production scenarios. Production apps should include security, error handling, and hosting logic that the demo app doesn't provide.
 
 ## Prerequisites
 
-Before you begin, have the following prerequisites in place:
-
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/).
 
-+ An Azure AI Search service. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) under your current subscription. You can use a free service for this quickstart. 
++ An Azure AI Search service. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription. For this quickstart, you can use a free service.
 
 + [Microsoft Edge (latest version)](https://www.microsoft.com/edge) or Google Chrome.
 
-+ A [search index](search-what-is-an-index.md) to use as the basis of your generated application. 
++ A [search index](search-what-is-an-index.md) to use as the basis of your generated application.
 
-  This quickstart uses the built-in hotels sample dataset. To create the index used in this exercise, run the **Import data** wizard, choosing the *hotels-sample* source and accepting all defaults.
+  This quickstart uses the hotels-sample index. To create the index, run the [**Import data wizard**](search-import-data-portal.md), select the built-in sample data, and step through the wizard using all the default values.
 
   :::image type="content" source="media/search-create-app-portal/import-data-hotels.png" alt-text="Screenshot of the data source page for sample data.":::
 
@@ -104,11 +102,11 @@ When you're working in your own subscription, it's a good idea at the end of a p
 
 You can find and manage resources in the Azure portal, using the **All resources** or **Resource groups** link in the left-navigation pane.
 
-Remember that a free service is limited to three indexes, indexers, and data sources. You can delete individual items in the Azure portal to stay under the limit. 
+Remember that a free service is limited to three indexes, indexers, and data sources. You can delete individual items in the Azure portal to stay under the limit.
 
-## Next steps
+## Next step
 
-The demo app is useful for prototyping because you can simulate an end-user experience without having to write JavaScript or front-end code, but as you get closer to proof-of-concept in your own project, review one of the end-to-end code samples that is closer facsimile of a real-word app:
+The demo app is useful for prototyping because you can simulate an end-user experience without writing any JavaScript or front-end code. As you get closer to proof-of-concept in your own project, review the end-to-end code samples that more closely mimic a real-word app:
 
 > [!div class="nextstepaction"]
 > [Add search to web apps](tutorial-csharp-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アプリポータル作成ガイドの内容更新"
}
```

### Explanation
このコード変更は、Markdown形式で書かれた「search-create-app-portal.md」というドキュメントに対する修正を示しています。変更の内容として、追加が12行、削除が14行、合計で26行の変更が行われています。

主な修正ポイントは、文書のタイトルと著者情報の更新、日付の変更、説明文の一部の言い回しの改善、さらにいくつかの文における細かな調整が含まれています。具体的には、アプリ作成の手順や要件に関する説明を整理し、より明確で流れの良い形にしています。

これにより、読者がAzureポータル内でのデモアプリの作成手順をより理解しやすくなることが期待されます。また、ガイドの内容が最新のものであることを確保することで、ユーザーが実際に操作する際の混乱を軽減し、スムーズに進められるようになります。このような改善は、ユーザーの経験を向上させ、最終的にはより良い結果を得るために重要です。

## articles/search/search-explorer.md{#item-738774}

<details>
<summary>Diff</summary>
````diff
@@ -1,35 +1,33 @@
 ---
-title: "Quickstart: Search explorer query tool"
+title: "Quickstart: Search Explorer Query Tool"
 titleSuffix: Azure AI Search
 description: Search explorer is a query tool in the Azure portal that sends query requests to a search index in Azure AI Search. Use it to learn syntax, test query expressions, or inspect a search document.
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 01/15/2025
+ms.date: 03/04/2025
 ms.custom:
   - mode-ui
 ---
 
 # Quickstart: Use Search explorer to run queries in the Azure portal
 
-In this quickstart, learn how to use **Search explorer**, a built-in query tool in the Azure portal used for running queries against a search index in Azure AI Search. Use it to test a query or filter expression, or confirm whether content exists in the index.
+In this quickstart, you learn how to use **Search explorer**, a built-in query tool in the Azure portal for running queries against an Azure AI Search index. Use it to test a query or filter expression, or confirm whether content exists in the index.
 
 This quickstart uses an existing index to demonstrate Search explorer.
 
 > [!TIP]
-> Search explorer now supports image search. [Quickstart: Image search in Azure portal](search-get-started-portal-image-search.md) provides the steps.
+> Search explorer now supports image search. To learn more, see [Quickstart: Image search in the Azure portal](search-get-started-portal-image-search.md).
 
 ## Prerequisites
 
-Before you begin, have the following prerequisites in place:
-
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/).
 
-+ An Azure AI Search service. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) under your current subscription. You can use a free service for this quickstart. 
++ An Azure AI Search service. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription. For this quickstart, you can use a free service.
 
-+ The *realestate-us-sample-index* is used for this quickstart. To create the index, use the [**Import data wizard**](search-import-data-portal.md), choose the built-in sample data, and step through the wizard using all of the default values.
++ This quickstart uses the realestate-us-sample index. To create the index, run the [**Import data wizard**](search-import-data-portal.md), select the built-in sample data, and step through the wizard using all the default values.
 
   :::image type="content" source="media/search-explorer/search-explorer-sample-data.png" alt-text="Screenshot of the sample data sets available in the Import data wizard." border="true":::  
 
@@ -54,7 +52,7 @@ There are two approaches for querying in Search explorer.
 + JSON view supports parameterized queries. Filters, orderby, select, count, searchFields, and all other parameters must be set in JSON view.
 
   > [!TIP]
-  > JSON view provides intellisense for parameter name completion. Place the cursor inside the JSON view and type a space character to show a list of all query parameters, or type a single letter like "s" to show just the query parameters starting with "s". Intellisense doesn't exclude invalid parameters so use your best judgment.
+  > JSON view provides intellisense for parameter name completion. Place your cursor inside the JSON view and type a space character to see a list of all query parameters. You can also type a letter, like "s," to see only the query parameters that begin with that letter. Intellisense doesn't exclude invalid parameters, so use your best judgment.
 
   Switch to **JSON view** for parameterized queries. The examples in this article assume JSON view throughout. You can paste JSON examples from this article into the text area.
 
@@ -193,7 +191,7 @@ In this quickstart, you used **Search explorer** to query an index using the RES
 
 + Search results are composed of all fields marked as "retrievable" in the index. Select the adjacent **Fields** tab to review attributes.
 
-+ Keyword search, similar to what you might enter in a commercial web browser, are useful for testing an end-user experience. For example, assuming the built-in real estate sample index, you could enter "Seattle apartments lake washington", and then you can use Ctrl-F to find terms within the search results. 
++ Keyword search, similar to what you might enter in a commercial web browser, are useful for testing an end-user experience. For example, assuming the built-in real estate sample index, you could enter "Seattle apartments lake washington," and then you can use Ctrl-F to find terms within the search results.
 
 + Query and filter expressions are articulated in a syntax implemented by Azure AI Search. The default is a [simple syntax](/rest/api/searchservice/simple-query-syntax-in-azure-search), but you can optionally use [full Lucene](/rest/api/searchservice/lucene-query-syntax-in-azure-search) for more powerful queries. [Filter expressions](/rest/api/searchservice/odata-expression-syntax-for-azure-search) are articulated in an OData syntax.
 
@@ -205,9 +203,9 @@ You can find and manage resources in the Azure portal, using the **All resources
 
 If you're using a free service, remember that you're limited to three indexes, indexers, and data sources. You can delete individual items in the Azure portal to stay under the limit. 
 
-## Next steps
+## Next step
 
 To learn more about query structures and syntax, use a REST client to create query expressions that use more parts of the API. The [Search POST REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-05-01-preview&preserve-view=true) is especially helpful for learning and exploration.
 
 > [!div class="nextstepaction"]
-> [Create a basic query in REST](search-get-started-rest.md)
+> [Quickstart: Create a basic query in REST](search-get-started-rest.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索エクスプローラーガイドの内容更新"
}
```

### Explanation
このコード変更は、「search-explorer.md」というMarkdownファイルに対する修正を示しています。主な修正点として、10行の追加と12行の削除が行われ、合計で22行の変更がありました。

変更内容には、文書のタイトルの言い回しの改善、著者の名称の整備、日付の更新、および説明文の一部の表現の明確化が含まれています。特に、検索エクスプローラーの機能や使い方に関する部分が整理され、ユーザーがツールの使い方を理解しやすくなっています。また、画像検索機能のサポートについての情報も明確にされています。

さらに、文中のいくつかの記述も改善され、具体例やコードの入力方法に関する記載が明確にされました。これにより、読者がAzureポータルでの検索エクスプローラーの使用方法を効果的に学ぶことができ、実際の使い方に関連する情報を簡単に理解できるようになっています。このような改善は、ユーザーのエクスペリエンスを向上させ、より良い学習成果をもたらすことを目的としています。

## articles/search/search-get-started-arm.md{#item-9287ad}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: 'Quickstart: Deploy using templates'
+title: 'Quickstart: Deploy Using an ARM Template'
 titleSuffix: Azure AI Search
-description: You can quickly deploy an Azure AI Search service instance using the Azure Resource Manager template.
+description: Learn how to deploy an Azure AI Search service instance using an Azure Resource Manager template.
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
@@ -12,12 +12,12 @@ ms.custom:
   - mode-arm
   - devx-track-arm-template
   - ignite-2023
-ms.date: 01/17/2025
+ms.date: 03/04/2025
 ---
 
 # Quickstart: Deploy Azure AI Search using an Azure Resource Manager template
 
-This article walks you through the process for using an Azure Resource Manager (ARM) template to deploy an Azure AI Search resource in the Azure portal.
+In this quickstart, you use an Azure Resource Manager (ARM) template to deploy an Azure AI Search service in the Azure portal.
 
 [!INCLUDE [About Azure Resource Manager](~/reusable-content/ce-skilling/azure/includes/resource-manager-quickstart-introduction.md)]
 
@@ -47,24 +47,24 @@ Select the following image to sign in to Azure and open a template. The template
 
 :::image type="content" source="~/reusable-content/ce-skilling/azure/media/template-deployments/deploy-to-azure-button.svg" alt-text="Button to deploy the Resource Manager template to Azure." border="false" link="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fazure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.search%2Fazure-search-create%2Fazuredeploy.json":::
 
-the Azure portal displays a form that allows you to easily provide parameter values. Some parameters are pre-filled with the default values from the template. You will need to provide your subscription, resource group, location, and service name. If you want to use Azure AI services in an [AI enrichment](cognitive-search-concept-intro.md) pipeline, for example to analyze binary image files for text, choose a location that offers both Azure AI Search and Azure AI services. Both services are required to be in the same region for AI enrichment workloads. Once you have completed the form, you will need to agree to the terms and conditions and then select the purchase button to complete your deployment.
+The Azure portal displays a form that allows you to easily provide parameter values. Some parameters are prefilled with the default values from the template. Provide your subscription, resource group, location, and service name. If you want to use Azure AI services in an [AI enrichment](cognitive-search-concept-intro.md) pipeline, for example to analyze binary image files for text, choose a location that offers both Azure AI Search and Azure AI services. Both services are required to be in the same region for AI enrichment workloads. After you complete the form, agree to the terms and conditions and then select the purchase button to complete your deployment.
 
 > [!div class="mx-imgBorder"]
 > ![Azure portal display of template](./media/search-get-started-arm/arm-portalscrnsht.png)
 
 ## Review deployed resources
 
-When your deployment is complete you can access your new resource group and new search service in the Azure portal.
+When your deployment is complete, you can access your new resource group and new search service in the Azure portal.
 
 ## Clean up resources
 
 Other Azure AI Search quickstarts and tutorials build upon this quickstart. If you plan to continue on to work with subsequent quickstarts and tutorials, you may wish to leave this resource in place. When no longer needed, you can delete the resource group, which deletes the Azure AI Search service and related resources.
 
-## Next steps
+## Related content
 
-In this quickstart, you created an Azure AI Search service using an ARM template, and validated the deployment. To learn more about Azure AI Search and Azure Resource Manager, continue on to the articles below.
+In this quickstart, you created an Azure AI Search service using an ARM template and then validated the deployment. To learn more about Azure AI Search and Azure Resource Manager, see the following articles:
 
-- Read an [overview of Azure AI Search](search-what-is-azure-search.md).
-- [Create an index](search-get-started-portal.md) for your search service.
-- [Create a demo app](search-create-app-portal.md) using the Azure portal wizard.
-- [Create a skillset](search-get-started-skillset.md) to extract information from your data.
+- [What is Azure AI Search?](search-what-is-azure-search.md)
+- [Quickstart: Create a search index in the Azure portal](search-get-started-portal.md)
+- [Quickstart: Create a demo search app in the Azure portal](search-create-app-portal.md)
+- [Quickstart: Create a skillset in the Azure portal](search-get-started-skillset.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ARMテンプレートを用いたデプロイガイドの更新"
}
```

### Explanation
このコード変更は、「search-get-started-arm.md」というドキュメントに対する修正を示しています。変更は、12行の追加と12行の削除からなり、全体で24行が修正されています。

主な内容として、記事のタイトルを「Quickstart: Deploy Using an ARM Template」に変更し、説明文をより具体的で明確な形にしました。また、日付も新しいものに更新されています。説明部分では、Azureポータルでのリソースデプロイメント手順を簡潔に改訂して、ユーザーが理解しやすくなっています。

さらに、手続きの流れや要件についての表現が改善されており、用語の統一感や分かりやすさも向上しました。具体的には、インターフェイスの入力方法や、AIサービスの地域に関する注意点についての記載が整備されています。

最後に、関連するコンテンツのセクションが改良され、記事へのリンクがよりアクセスしやすくなっています。このような更新により、読者がAzure AI Searchに関する情報を効果的に取得できることを目的としています。ユーザーエクスペリエンスの向上を図り、学習効果を高めることが期待されています。

## articles/search/search-get-started-bicep.md{#item-731b0e}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: 'Quickstart: Deploy using Bicep'
+title: 'Quickstart: Deploy Using a Bicep File'
 titleSuffix: Azure AI Search
-description: You can quickly deploy an Azure AI Search service instance using Bicep.
+description: Learn how to deploy an Azure AI Search service instance using Bicep.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
@@ -11,12 +11,12 @@ ms.custom:
   - mode-arm
   - devx-track-bicep
   - ignite-2023
-ms.date: 12/10/2024
+ms.date: 03/04/2025
 ---
 
 # Quickstart: Deploy Azure AI Search using Bicep
 
-This article walks you through the process for using a Bicep file to deploy an Azure AI Search resource in the Azure portal.
+In this quickstart, you use a Bicep file to deploy an Azure AI Search service in the Azure portal.
 
 [!INCLUDE [About Bicep](~/reusable-content/ce-skilling/azure/includes/resource-manager-quickstart-bicep-introduction.md)]
 
@@ -101,11 +101,11 @@ Remove-AzResourceGroup -Name exampleRG
 
 ---
 
-## Next steps
+## Related content
 
-In this quickstart, you created an Azure AI Search service using a Bicep file, and then validated the deployment. To learn more about Azure AI Search and Azure Resource Manager, continue on to the articles.
+In this quickstart, you created an Azure AI Search service using a Bicep file and then validated the deployment. To learn more about Azure AI Search and Azure Resource Manager, see the following articles:
 
-- Read an [overview of Azure AI Search](search-what-is-azure-search.md).
-- [Create an index](search-get-started-portal.md) for your search service.
-- [Create a demo app](search-create-app-portal.md) using the Azure portal wizard.
-- [Create a skillset](search-get-started-skillset.md) to extract information from your data.
+- [What is Azure AI Search?](search-what-is-azure-search.md)
+- [Quickstart: Create a search index in the Azure portal](search-get-started-portal.md)
+- [Quickstart: Create a demo search app in the Azure portal](search-create-app-portal.md)
+- [Quickstart: Create a skillset in the Azure portal](search-get-started-skillset.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Bicepファイルを用いたデプロイガイドの更新"
}
```

### Explanation
このコード変更は、「search-get-started-bicep.md」というドキュメントに対する修正を示しています。主な修正として、10行の追加と10行の削除があり、合計で20行の変更が行われました。

変更内容には、記事のタイトルが「Quickstart: Deploy Using a Bicep File」に変更されたこと、説明文がより明確になったことが含まれています。また、日付も新しいものに更新されています。記事の主旨は、Bicepファイルを使用してAzure AI Search サービスをデプロイする方法についてのもので、手順が改訂されています。

具体的には、ユーザーがBicepファイルを使ってAzureポータルでリソースをデプロイするプロセスが整理されており、読者にとって理解しやすい構成になっています。また、手続きに関連する情報が整理されたことで、次のステップを示すセクションも「次のステップ」から「関連コンテンツ」に変更され、適切なリソースへのリンクが提供されています。

これらの変更によって、ドキュメントがよりアクセスしやすく、実用的な情報を提供できるようになっており、Azure AI Searchに関連する学習を進めるうえで役立つ内容となっています。

## articles/search/search-get-started-portal-image-search.md{#item-438b9b}

<details>
<summary>Diff</summary>
````diff
@@ -1,40 +1,39 @@
 ---
-title: "Quickstart: Search for images by using Search Explorer in the Azure portal"
+title: "Quickstart: Image Search in the Azure Portal"
 titleSuffix: Azure AI Search
-description: Search for images on an Azure AI Search index by using the Azure portal. Run a wizard to vectorize images, and then use Search Explorer to provide an image as your query input.
-
+description: Learn how to search for images on an Azure AI Search index in the Azure portal. Run a wizard to vectorize images, and then use Search Explorer to provide an image as your query input.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 10/18/2024
+ms.date: 03/04/2025
 ms.custom:
   - references_regions
 ---
 
-# Quickstart: Search for images by using Search Explorer in the Azure portal
+# Quickstart: Search for images using Search Explorer in the Azure portal
 
-This quickstart shows you how to get started with image search by using the **Import and vectorize data** wizard in the Azure portal. It also shows how to use Search Explorer to run image-based queries.
+In this quickstart, you use the **Import and vectorize data** wizard in the Azure portal to get started with image search. You also use Search Explorer to run image-based queries.
 
-Sample data consists of image files in the [azure-search-sample-data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/unsplash-images) repo, but you can use different images and still follow the walkthrough.
+The sample data consists of image files in the [azure-search-sample-data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/unsplash-images) repo, but you can use different images and still follow this quickstart.
 
 ## Prerequisites
 
-+ An Azure subscription. [Create one for free](https://azure.microsoft.com/free/).
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
-+ An [Azure AI services multiservice account](/azure/ai-services/multi-service-resource) to use for image vectorization and optical character recognition (OCR). Image vectorization requires Azure AI Vision multimodal embeddings. [Check the documentation](/azure/ai-services/computer-vision/overview-image-analysis#region-availability) for an updated list of regions.
++ An [Azure AI services multiservice account](/azure/ai-services/multi-service-resource) for image vectorization and optical character recognition (OCR). Image vectorization requires Azure AI Vision multimodal embeddings. For an updated list of regions, see the [Azure AI Vision documentation](/azure/ai-services/computer-vision/overview-image-analysis#region-availability).
 
-+ Azure AI Search for indexing and queries. It can be on any tier, but it must be in the [same region as Azure AI multiservice](search-create-service-portal.md#regions-with-the-most-overlap).
++ An Azure AI Search service for indexing and queries. Your service can be on any tier, but it must be in the [same region as Azure AI multiservice](search-create-service-portal.md#regions-with-the-most-overlap).
 
-  The service tier determines how many blobs you can index. We used the Free tier to create this walkthrough and limited the content to 10 JPG files.
+  The service tier determines how many blobs you can index. We used the Free tier to create this quickstart and limited the content to 10 JPG files.
 
 + Familiarity with the wizard. See [Import data wizards in the Azure portal](search-import-data-portal.md) for details.
 
-+ Azure Storage to store image files as blobs. Use Azure Blob Storage or Azure Data Lake Storage Gen2 (a storage account with a hierarchical namespace), a standard performance (general-purpose v2) account. Access tiers can be hot, cool, and cold.
++ Azure Storage to store image files as blobs. Use Azure Blob Storage or Azure Data Lake Storage Gen2 (a storage account with a hierarchical namespace), a standard performance (general-purpose v2) account. Access tiers can be hot, cool, or cold.
 
 All of the preceding resources must have public access enabled so that the Azure portal nodes can access them. Otherwise, the wizard fails. After the wizard runs, you can enable firewalls and private endpoints on the integration components for security. For more information, see [Secure connections in the import wizards](search-import-data-portal.md#secure-connections).
 
-If private endpoints are already present and you can't disable them, the alternative option is to run the respective end-to-end flow from a script or program on a virtual machine. The virtual machine must be on the same virtual network as the private endpoint. [Here's a Python code sample](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/integrated-vectorization) for integrated vectorization. The same [GitHub repo](https://github.com/Azure/azure-search-vector-samples/tree/main) has samples in other programming languages.
+If private endpoints are already present and you can't disable them, the alternative is to run the respective end-to-end flow from a script or program on a virtual machine. The virtual machine must be on the same virtual network as the private endpoint. [Here's a Python code sample](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/integrated-vectorization) for integrated vectorization. The same [GitHub repo](https://github.com/Azure/azure-search-vector-samples/tree/main) has samples in other programming languages.
 
 A free search service supports role-based access control on connections to Azure AI Search, but it doesn't support managed identities on outbound connections to Azure Storage or Azure AI Vision. This level of support means you must use key-based authentication on connections between a free search service and other Azure services. For connections that are more secure:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータルでの画像検索クイックスタートの更新"
}
```

### Explanation
このコード変更は、「search-get-started-portal-image-search.md」というドキュメントに対する修正を示しています。変更内容には、12行の追加と13行の削除があり、合計で25行の修正が行われました。

修正の主なポイントは、記事のタイトルを「Quickstart: Image Search in the Azure Portal」に変更し、説明文をより具体的に明確化したことです。これにより、読者が画像検索に関する内容をより理解しやすくなっています。また、新しい日付に変更されています。

内容の改訂においては、Azureポータルで画像検索を始めるための「Import and vectorize data」ウィザードについて、手順が整理され、読者にとって直感的に利用しやすくなるよう配慮されています。サンプルデータや前提条件に関する言及も変更され、明確な手順を提供することが強調されています。

前提条件部分では、Azureアカウントの手続きや、使用するリソースに関する容易なリンクが追加され、必要な情報をより簡単に閲覧できるようになっています。また、セキュリティに関する説明も整理され、プライベートエンドポイントやファイアウォールについての注意点が含まれています。

この一連の変更により、記事がより読みやすくなり、読者がAzure AI Searchを利用して画像検索を行うための手助けとなることが期待されています。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -1,30 +1,30 @@
 ---
-title: "Quickstart: Vectorize text and images by using the Azure portal"
+title: "Quickstart: Vector Search in the Azure Portal"
 titleSuffix: Azure AI Search
-description: Use a wizard to automate data chunking and vectorization in a search index.
+description: Learn how to use a wizard to automate data chunking and vectorization in a search index.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: quickstart
-ms.date: 02/06/2025
+ms.date: 03/04/2025
 ---
 
-# Quickstart: Vectorize text and images by using the Azure portal
+# Quickstart: Vectorize text and images in the Azure portal
 
-This quickstart helps you get started with [integrated vectorization](vector-search-integrated-vectorization.md) by using the **Import and vectorize data** wizard in the Azure portal. The wizard chunks your content and calls an embedding model to vectorize content during indexing and for queries.
+In this quickstart, you use the **Import and vectorize data** wizard in the Azure portal to get started with [integrated vectorization](vector-search-integrated-vectorization.md). The wizard chunks your content and calls an embedding model to vectorize content during indexing and for queries.
 
 ## Prerequisites
 
-+ An Azure subscription. [Create one for free](https://azure.microsoft.com/free/).
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
-+ [An Azure AI Search service](search-create-service-portal.md) in the same region as your Azure AI multi-service resource. We recommend the Basic tier or higher.
++ An [Azure AI Search service](search-create-service-portal.md) in the same region as your Azure AI multi-service resource. We recommend the Basic tier or higher.
 
-+ [A supported data source](#supported-data-sources) with the [Health Plan PDF](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/health-plan) sample documents.
++ A [supported data source](#supported-data-sources) with the [Health Plan PDF](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/health-plan) sample documents.
 
-+ [A supported embedding model](#supported-embedding-models).
++ A [supported embedding model](#supported-embedding-models).
 
 + Familiarity with the wizard. See [Import data wizards in the Azure portal](search-import-data-portal.md) for details.
 
@@ -104,7 +104,7 @@ This section points you to the content that works for this quickstart.
 
    1. If you're using [native soft delete](search-howto-index-changed-deleted-blobs.md#native-blob-soft-delete), no further steps are required on Azure Storage.
 
-   1. Otherwise, [add custom metadata](search-howto-index-changed-deleted-blobs.md#soft-delete-strategy-using-custom-metadata) that an indexer can scan to determine which blobs are marked for deletion. Give your custom property a descriptive name. For example, you could name the property "IsDeleted", set to false. Do this for every blob in the container. Later, when you want to delete the blob, change the property to true. For more information, see [Change and delete detection when indexing from Azure Storage](search-howto-index-changed-deleted-blobs.md)
+   1. Otherwise, [add custom metadata](search-howto-index-changed-deleted-blobs.md#soft-delete-strategy-using-custom-metadata) that an indexer can scan to determine which blobs are marked for deletion. Give your custom property a descriptive name. For example, you could name the property "IsDeleted", set to false. Do this for every blob in the container. Later, when you want to delete the blob, change the property to true. For more information, see [Change and delete detection when indexing from Azure Storage](search-howto-index-changed-deleted-blobs.md).
 
 ### [ADLS Gen2](#tab/sample-data-adlsgen2)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータルでのベクター検索クイックスタートの更新"
}
```

### Explanation
このコード変更は、「search-get-started-portal-import-vectors.md」というドキュメントに対する修正を示しています。修正内容には、10行の追加と10行の削除があり、合計で20行の変更が行われました。

主な変更点には、記事のタイトルが「Quickstart: Vector Search in the Azure Portal」に変更されたこと、説明文が改善されたことが含まれています。これにより、読者がAzureポータルでのベクター検索の手法をより理解しやすくなっています。

具体的には、記事の冒頭部分では、**Import and vectorize data** ウィザードを使用してデータのチャンク化とベクトル化をどのように自動化するかを学ぶことが強調されています。また、前提条件のいくつかが明確に記述され、Azureサブスクリプション、Azure AI Searchサービス、支持されるデータソースおよび埋め込みモデルに関する情報が整理されています。

新たに追加された内容の中には、ウィザードに対する理解を深めるための資料へのリンクが盛り込まれ、読者により多くのリソースを提供しています。また、情報の一部に対し、文章の改善が行われ、明瞭さが向上しています。

全体として、この修正は、Azureポータルにおけるベクター検索のクイックスタートガイドをより分かりやすく、実用的なものにしており、読者が技術にアクセスしやすいよう配慮されています。

## articles/search/search-get-started-portal.md{#item-6d0cb1}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +1,13 @@
 ---
-title: "Quickstart: Create a search index in the Azure portal"
+title: "Quickstart: Keyword Search in the Azure Portal"
 titleSuffix: Azure AI Search
 description: Learn how to create, load, and query your first search index using the Import Data wizard in the Azure portal. This quickstart uses a fictitious hotel dataset for sample data.
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
-ms.date: 02/27/2025
+ms.date: 03/04/2025
 ms.custom:
   - mode-ui
   - ignite-2023
@@ -16,7 +16,7 @@ ms.custom:
 
 # Quickstart: Create a search index in the Azure portal
 
-In this Azure AI Search quickstart, create your first search index using the [**Import data** wizard](search-import-data-portal.md) and a built-in sample of fictitious hotel data hosted by Microsoft. The wizard requires no code to create an index, helping you write interesting queries within minutes.
+In this quickstart, you create your first Azure AI Search index using the [**Import data** wizard](search-import-data-portal.md) and a built-in sample of fictitious hotel data hosted by Microsoft. The wizard requires no code to create an index, helping you write interesting queries within minutes.
 
 The wizard creates multiple objects on your search service, including a [searchable index](search-what-is-an-index.md), an [indexer](search-indexer-overview.md), and a data source connection for automated data retrieval. At the end of this quickstart, we review each object.
 
@@ -260,9 +260,9 @@ In the Azure portal, you can find and manage resources for your service under **
 > [!NOTE]
 > If you're using a free search service, remember that the limit is three indexes, three indexers, and three data sources. You can delete individual objects in the Azure portal to stay under the limit.
 
-## Next steps
+## Next step
 
 Try an Azure portal wizard to generate a ready-to-use web app that runs in a browser. Use this wizard on the small index you created in this quickstart, or use one of the built-in sample datasets for a richer search experience.
 
 > [!div class="nextstepaction"]
-> [Create a demo app in the Azure portal](search-create-app-portal.md)
+> [Quickstart: Create a demo search app in the Azure portal](search-create-app-portal.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータルでのキーワード検索クイックスタートの更新"
}
```

### Explanation
このコード変更は、「search-get-started-portal.md」というドキュメントに対する修正を示しています。修正には、5行の追加と5行の削除があり、合計で10行の変更が行われました。

主な変更点は、ドキュメントのタイトルが「Quickstart: Create a search index in the Azure portal」から「Quickstart: Keyword Search in the Azure Portal」に変更されたこと、そして説明文が改善されたことです。これにより、内容の焦点がより具体的に「キーワード検索」に置かれるようになりました。

記事の冒頭では、Azure AI Searchのクイックスタートにおいて、**Import data** ウィザードを使用して最初の検索インデックスを作成する手順が示されています。ウィザードの利用により、コードを書くことなくインデックスを作成でき、迅速に興味深いクエリが書けることが強調されています。

さらに、次のステップに関するセクションの見出しが「Next steps」から「Next step」に変更され、次に行うべきアクションがより明確に示されています。また、「デモアプリの作成」へのリンクがより具体的なタイトルに変更され、読者にとっての明快さが向上しています。

全体として、この修正は、読者がAzureポータルを使用したキーワード検索の実践的な手順を理解しやすくすることを目的としており、ドキュメントの利用価値を高めています。

## articles/search/search-get-started-powershell.md{#item-4435d0}

<details>
<summary>Diff</summary>
````diff
@@ -1,30 +1,32 @@
 ---
-title: 'Quickstart: Create a search index in PowerShell by using REST APIs'
+title: 'Quickstart: Create an Index Using PowerShell and REST APIs'
 titleSuffix: Azure AI Search
-description: In this REST API quickstart, learn how to create an index, load data, and run queries by using PowerShell's Invoke-RestMethod and the Azure AI Search REST API.
+description: Learn how to create an index, load data, and run queries using PowerShell's Invoke-RestMethod and the Azure AI Search REST APIs.
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
 ms.devlang: rest-api
-ms.date: 10/31/2024
+ms.date: 03/04/2025
 ms.custom:
   - mode-api
   - ignite-2023
 ---
-# Quickstart: Create a search index in PowerShell by using REST APIs
 
-In this Azure AI Search quickstart, learn how to create, load, and query a search index by using PowerShell and the [Azure AI Search REST APIs](/rest/api/searchservice/). This article explains how to run PowerShell commands interactively. Alternatively, you can [download and run a PowerShell script](https://github.com/Azure-Samples/azure-search-powershell-samples/tree/main/Quickstart) that performs the same operations.
+# Quickstart: Create a search index in PowerShell using REST
 
-If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
+In this quickstart, you create, load, and query a search index using PowerShell and the [Azure AI Search REST APIs](/rest/api/searchservice/).
+
+This quickstart explains how to run PowerShell commands interactively. Alternatively, you can [download and run a PowerShell script](https://github.com/Azure-Samples/azure-search-powershell-samples/tree/main/Quickstart) that performs the same operations.
 
 ## Prerequisites
 
-The following services and tools are required for this quickstart:
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+
+- An Azure AI Search service. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription. For this quickstart, you can use a free service.
 
 - [PowerShell 7.3 or later](https://github.com/PowerShell/PowerShell), using [Invoke-RestMethod](/powershell/module/Microsoft.PowerShell.Utility/Invoke-RestMethod) for sequential and interactive steps.
-- [Create an Azure AI Search service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) under your current subscription. You can use a free service for this quickstart.
 
 ## Copy a search service key and URL
 
@@ -393,7 +395,7 @@ You can find and manage resources in the Azure portal by using the **All resourc
 
 If you're using a free service, remember that you're limited to three indexes, indexers, and data sources. You can delete individual items in the Azure portal to stay under the limit.
 
-## Next steps
+## Next step
 
 In this quickstart, you used PowerShell to step through the basic workflow for creating and accessing content in Azure AI Search. With the concepts in mind, we recommend that you move on to more advanced scenarios, such as indexing from Azure data sources:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PowerShellを使用したインデックス作成クイックスタートの更新"
}
```

### Explanation
このコード変更は、「search-get-started-powershell.md」というドキュメントに対する修正を示しています。修正内容には、11行の追加と9行の削除があり、合計で20行の変更が行われました。

主な変更点は、ドキュメントのタイトルが「Quickstart: Create a search index in PowerShell by using REST APIs」から「Quickstart: Create an Index Using PowerShell and REST APIs」に変更されたことです。この変更により、タイトルがより簡潔で具体的な表現になり、読者にとって内容がわかりやすくなっています。

説明文も若干修正され、PowerShellの`Invoke-RestMethod`を使用してインデックスを作成、データを読み込み、クエリを実行する方法が強調されています。また、クイックスタートの手順が情報源と関連付けられ、よりスムーズに進められるようになっています。

さらに、前提条件に関するセクションが整備され、必要なサービスやツールについての情報がより明確になっています。具体的には、Azureアカウントの作成に関するリンクが追加され、Azure AI Searchサービスの利用手続きが分かりやすく示されています。

最後に、次のステップの見出しが「Next steps」から「Next step」に変更され、次のアクションがよりシンプルに強調されています。全体として、この修正は、PowerShellを用いたAzure AI Searchの活用方法をより効果的に伝えることを目的としており、初心者にとっても利用しやすいドキュメントに改善されています。

## articles/search/search-get-started-rag.md{#item-05ff0e}

<details>
<summary>Diff</summary>
````diff
@@ -1,47 +1,42 @@
 ---
-title: Quickstart RAG
+title: 'Quickstart: Generative Search (RAG)'
 titleSuffix: Azure AI Search
-description: In this quickstart, learn how to use grounding data from Azure AI Search with a chat model on Azure OpenAI.
+description: Learn how to use grounding data from Azure AI Search with a chat model on Azure OpenAI.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: quickstart
-ms.date: 01/09/2025
+ms.date: 03/04/2025
 ---
 
-# Quickstart: Generative search (RAG) with grounding data from Azure AI Search
+# Quickstart: Generative search (RAG) using grounding data from Azure AI Search
 
-This quickstart shows you how to send queries to a chat completion model for a conversational search experience over your indexed content on Azure AI Search. You use the Azure portal to set up the resources, and then run Python code to call the APIs. 
+In this quickstart, you send queries to a chat completion model for a conversational search experience over your indexed content on Azure AI Search. After setting up Azure OpenAI and Azure AI Search resources in the Azure portal, you run Python code to call the APIs.
 
 ## Prerequisites
 
-- [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and the [Jupyter package](https://pypi.org/project/jupyter/). For more information, see [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python).
-
-- An Azure subscription with permissions to assign roles. [Create one for free](https://azure.microsoft.com/free/).
-
-- [Azure OpenAI](/azure/ai-services/openai/how-to/create-resource)
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
-  - [Choose a region](/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) that supports the chat completion model you want to use (gpt-4o, gpt-4o-mini, or equivalent model). 
+- An [Azure OpenAI resource](/azure/ai-services/openai/how-to/create-resource).
+  - [Choose a region](/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) that supports the chat completion model you want to use (gpt-4o, gpt-4o-mini, or an equivalent model).
   - [Deploy the chat completion model](/azure/ai-studio/how-to/deploy-models-openai) in Azure AI Foundry or [use another approach](/azure/ai-services/openai/how-to/working-with-models).
 
-- [Azure AI Search](search-create-service-portal.md)
-
-  - Same region as Azure OpenAI.
-  - Basic tier or higher is recommended.
+- An [Azure AI Search resource](search-create-service-portal.md).
+  - Use the same region as your Azure OpenAI resource.
+  - We recommend using the Basic tier or higher.
   - [Enable semantic ranking](semantic-how-to-enable-disable.md).
-  - [Enable role-based access control (see below)](#configure-access).
 
-To meet the same-region requirement, start by reviewing the [regions for the chat model](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability) you want to use. Once you identify a region, confirm that Azure AI Search is available in the [same region](search-region-support.md#azure-public-regions).
+- [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and the [Jupyter package](https://pypi.org/project/jupyter/). For more information, see [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python).
 
-Make sure you know the name of the deployed model, and have the endpoints for both Azure resources at hand. You'll provide this information in the steps that follow.
+To meet the same-region requirement, start by reviewing the [regions for the chat model](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability) you want to use. After you identify a region, confirm that Azure AI Search is available in the [same region](search-region-support.md#azure-public-regions).
 
 ## Download file
 
 [Download a Jupyter notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart-RAG) from GitHub to send the requests in this quickstart. For more information, see [Downloading files from GitHub](https://docs.github.com/get-started/start-your-journey/downloading-files-from-github).
 
-You can also start a new file on your local system and create requests manually by using the instructions in this article. 
+You can also start a new file on your local system and create requests manually by using the instructions in this article.
 
 ## Configure access
 
@@ -471,6 +466,6 @@ When you're working in your own subscription, it's a good idea at the end of a p
 
 You can find and manage resources in the Azure portal by using the **All resources** or **Resource groups** link in the leftmost pane.
 
-## See also
+## Related content
 
-- [Tutorial: How to build a RAG solution in Azure AI Search](tutorial-rag-build-solution.md)
+- [Tutorial: Build a RAG solution in Azure AI Search](tutorial-rag-build-solution.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "生成的検索（RAG）クイックスタートの更新"
}
```

### Explanation
このコード変更は、「search-get-started-rag.md」というドキュメントに対する修正を示しています。修正内容には、16行の追加と21行の削除があり、合計で37行の変更が行われました。

主な変更点は、ドキュメントのタイトルが「Quickstart RAG」から「Quickstart: Generative Search (RAG)」に変更されたことです。この変更により、タイトルがより説明的になり、内容が明確に伝わるようになりました。また、説明文も微調整され、Azure AI Searchからのデータを使用してAzure OpenAIでのチャットモデルを活用する方法がより明瞭に記述されています。

クイックスタートの手順では、Azureポータルを使用してリソースをセットアップした後、Pythonコードを実行してAPIを呼び出す流れがよりスムーズに説明されるようになりました。前提条件に関する情報も整理され、必要なリソースの名称や手順、推奨される使用状況が具体的に示されています。例えば、AzureアカウントやAzure OpenAIリソースの作成、地域設定の確認に関する詳細が明確になっています。

最終的に、参考資料のセクションが「See also」から「Related content」に変更され、関連情報へのリンクがより適切に整理されました。全体として、この修正は、生成的検索（RAG）の使用方法をより効果的に伝えることを目的とし、読者が実際に利用する際の利便性を向上させています。

## articles/search/search-get-started-rbac.md{#item-9d96c1}

<details>
<summary>Diff</summary>
````diff
@@ -1,26 +1,25 @@
 ---
-title: Quickstart keyless connection
+title: 'Quickstart: Keyless Connection'
 titleSuffix: Azure AI Search
-description: In this quickstart, learn how to switch from API keys to Microsoft Entra identities and role-based access control (RBAC).
+description: Learn how to switch from API keys to Microsoft Entra identities and role-based access control (RBAC).
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
-
 ms.topic: quickstart
-ms.date: 12/03/2024
+ms.date: 03/04/2025
 ---
 
 # Quickstart: Connect without keys
 
-Configure Azure AI Search to use Microsoft Entra ID authentication and role-based access control (RBAC) so that you can connect from your local system without API keys, using Jupyter notebooks or a REST client to interact with your search service.
+In this quickstart, you configure Azure AI Search to use Microsoft Entra ID authentication and role-based access control (RBAC) to connect from your local system without API keys. You then use Jupyter notebooks or a REST client to interact with your search service.
 
-If you stepped through other quickstarts that connect using API keys, this quickstart shows you how to switch to identity-based authentication so that you can avoid hard-coded keys in your example code.
+If you completed other quickstarts that connect using API keys, this quickstart shows you how to switch to identity-based authentication so that you can avoid hard-coded keys in your example code.
 
 ## Prerequisites
 
-- An Azure subscription. [Create one for free](https://azure.microsoft.com/free/).
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
-- [Azure AI Search](search-create-service-portal.md), any region or tier, but you need Basic or higher to configure a managed identity for Azure AI Search.
+- An [Azure AI Search service](search-create-service-portal.md) in any region or tier. However, to configure a managed identity for Azure AI Search, you need the Basic tier or higher.
 
 - A command line tool, such as PowerShell or Bash, and the [Azure CLI](/cli/azure/install-azure-cli).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "キーを使わない接続のクイックスタートの更新"
}
```

### Explanation
このコード変更は、「search-get-started-rbac.md」というドキュメントに対する修正を示しています。修正内容には、7行の追加と8行の削除があり、合計で15行の変更が行われました。

主な変更点は、ドキュメントのタイトルが「Quickstart keyless connection」から「Quickstart: Keyless Connection」に変更されたことです。この変更により、タイトルがより明確で一貫性のある形式となりました。また、説明文はスムーズな文章に修正され、Microsoft Entra ID認証と役割ベースのアクセス制御（RBAC）を使用してAPIキーなしで接続する方法が紹介されています。

クイックスタートの手順では、Azure AI Searchの設定から始まり、APIキーを使わないアイデンティティベースの認証への切り替えが具体的に説明されています。また、JupyterノートブックやRESTクライアントを使用して、検索サービスと対話する手順も明確化されています。

前提条件に関しても整理され、必要なAzureサブスクリプションについての説明がより具体的になっています。特に、Azure AI Searchサービスが必要であることが再確認され、マネージドIDを設定するためにはBasicティア以上が必要であるという条件が強調されています。

全体として、この修正は、キーを使用しない接続の具体的な手順をわかりやすくし、ユーザーがAzure AI Searchをより効果的に利用できるようにすることを目的としています。

## articles/search/search-get-started-rest.md{#item-0df9d5}

<details>
<summary>Diff</summary>
````diff
@@ -1,31 +1,31 @@
 ---
-title: 'Quickstart: Search index (REST)'
+title: 'Quickstart: Keyword Search Using REST APIs'
 titleSuffix: Azure AI Search
-description: In this quickstart, learn how to call the Azure AI Search REST APIs to create, load, and query a search index.
+description: Learn how to call the Azure AI Search REST APIs to create, load, and query a search index.
 zone_pivot_groups: URL-test-interface-rest-apis
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.topic: quickstart
 ms.devlang: rest-api
-ms.date: 11/29/2024
+ms.date: 03/04/2025
 ms.custom:
   - mode-api
   - ignite-2023
 ---
 
-# Quickstart: Keyword search by using REST
+# Quickstart: Keyword search using REST
 
-The REST APIs in Azure AI Search provide programmatic access to all of its capabilities, including preview features, and they're an easy way to learn how features work. In this quickstart, learn how to call the [Search REST APIs](/rest/api/searchservice) to create, load, and query a search index in Azure AI Search.
-
-If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
+In this quickstart, you call the [Search REST APIs](/rest/api/searchservice) to create, load, and query a search index. The REST APIs in Azure AI Search provide programmatic access to all of its capabilities, including preview features, and are an easy way to learn how features work.
 
 ## Prerequisites
 
-- [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
-- [Azure AI Search](search-what-is-azure-search.md). [Create](search-create-service-portal.md) or [find an existing Azure AI Search resource](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) under your current subscription. You can use a free service for this quickstart.
+- An Azure AI Search service. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices) in your current subscription. For this quickstart, you can use a free service.
+
+- [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 ## Download files
 
@@ -128,7 +128,7 @@ If you're not familiar with the REST client for Visual Studio Code, this section
       api-key: {{apiKey}}
     ```
 
-1. Or, paste in this example if your using roles. Replace the `@baseUrl` and `@token` placeholders with the values you copied earlier, without quotes.
+1. Or, paste in this example if you're using roles. Replace the `@baseUrl` and `@token` placeholders with the values you copied earlier, without quotes.
 
    ```http
    @baseUrl = PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE
@@ -412,7 +412,7 @@ DELETE  {{baseUrl}}/indexes/hotels-quickstart?api-version=2024-07-01 HTTP/1.1
 
 ## Next step
 
-Now that you're familiar with the REST client and making REST calls to Azure AI Search, try another quickstart that demonstrates vector support.
+Now that you're familiar with the REST client and making REST calls to Azure AI Search, try another quickstart that demonstrates vector support:
 
 > [!div class="nextstepaction"]
 > [Quickstart: Vector search using REST](search-get-started-vector.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIを使用したキーワード検索のクイックスタートの更新"
}
```

### Explanation
このコード変更は、「search-get-started-rest.md」というドキュメントに対する修正を示しており、11行の追加と11行の削除があり、合計で22行の変更が行われました。

主な変更点は、ドキュメントのタイトルが「Quickstart: Search index (REST)」から「Quickstart: Keyword Search Using REST APIs」に変更されたことです。また、説明文が再構成され、Azure AI SearchのREST APIsを使用して検索インデックスを作成し、ロードし、クエリする方法がより効果的に伝わるようになりました。

具体的には、クイックスタートの内容が整理されており、読み手が必要な手順を理解しやすくなっています。前提条件セクションでは、Azureアカウントの作成に関する情報が追加され、具体的にAzure AI Searchサービスを作成または既存のサービスを見つける手順が示されています。また、Visual Studio CodeのRESTクライアントについても触れられています。

さらには、手順の説明に細かい文言の変更が加えられ、読者が情報をより簡単にフォローできるよう工夫されています。さらに最後に、次に進むべきステップとして「ベクターサポートのクイックスタート」へのリンクが強調され、他の関連するクイックスタートへの誘導も行われています。

全体として、この修正は、Azure AI SearchのREST APIを使用したキーワード検索のプロセスを明確にし、利用者にとっての利便性を向上させることを目的としています。

## articles/search/search-get-started-semantic.md{#item-2b3902}

<details>
<summary>Diff</summary>
````diff
@@ -1,8 +1,7 @@
 ---
-title: 'Quickstart: semantic ranking'
+title: 'Quickstart: Add Semantic Ranking to an Index Using .NET or Python'
 titleSuffix: Azure AI Search
-description: Change an existing index to use semantic ranker to rescore search results and promote the most semantically relevant matches.
-
+description: Learn how to change an existing index to use semantic ranker, which helps rescore search results and promote the most semantically relevant matches.
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
@@ -12,31 +11,33 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: quickstart
-ms.date: 10/22/2024
+ms.date: 03/04/2025
 ---
 
-# Quickstart: Semantic ranking with .NET or Python
+# Quickstart: Semantic ranking using .NET or Python
 
-In Azure AI Search, [semantic ranking](semantic-search-overview.md) is query-side functionality that uses machine reading comprehension from Microsoft to rescore search results, promoting the most semantically relevant matches to the top of the list. Depending on the content and the query, semantic ranking can [significantly improve search relevance](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-outperforming-vector-search-with-hybrid/ba-p/3929167), with minimal work for the developer.
+In this quickstart, you learn about the index and query modifications that invoke semantic ranker.
 
-This quickstart walks you through the index and query modifications that invoke semantic ranker.
+In Azure AI Search, [semantic ranking](semantic-search-overview.md) is query-side functionality that uses machine reading comprehension from Microsoft to rescore search results, promoting the most semantically relevant matches to the top of the list. Depending on the content and the query, semantic ranking can [significantly improve search relevance](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-outperforming-vector-search-with-hybrid/ba-p/3929167) with minimal developer effort.
 
 > [!NOTE]
-> For an Azure AI Search solution example with ChatGPT interaction, see [this demo](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md) or [this accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator).
+> For an example of an Azure AI Search solution with ChatGPT interaction, see [this demo](https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/README.md) or [this accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator).
 
 ## Prerequisites
 
-+ An Azure account with an active subscription. You can [create an account for free](https://azure.microsoft.com/free/).
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+
++ An [Azure AI Search service](search-create-service-portal.md), at Basic tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
-+ An Azure AI Search resource, at Basic tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
++ An API key and a search service endpoint. To obtain them:
 
-+ An API key and search service endpoint. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
+  1. Sign in to the [Azure portal](https://portal.azure.com) and find your search service.
 
-  In **Overview**, copy the URL and save it for a later step. An example endpoint might look like `https://mydemo.search.windows.net`.
+  1. On **Overview**, copy the URL and save it for a later step. An example endpoint might look like `https://mydemo.search.windows.net`.
 
-  In **Keys**, copy and save an admin key for full rights to create and delete objects. There are two interchangeable primary and secondary keys. Choose either one.
+  1. On **Keys**, copy and save an admin key for full rights to create and delete objects. There are two interchangeable primary and secondary keys. Choose either one.
 
-  :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot showing where to find your search service's HTTP endpoint and access key.":::
+     :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot showing where to find your search service's HTTP endpoint and access key.":::
 
 ## Add semantic ranking
 
@@ -62,9 +63,9 @@ When you're working in your own subscription, it's a good idea at the end of a p
 
 You can find and manage resources in the Azure portal, using the **All resources** or **Resource groups** link in the left-navigation pane.
 
-## Next steps
+## Next step
 
-In this quickstart, you learned how to invoke semantic ranking on an existing index. We recommend trying semantic ranking on your own indexes as a next step. However, if you want to continue with demos, visit the following link.
+In this quickstart, you learned how to invoke semantic ranking on an existing index. We recommend trying semantic ranking on your own indexes as a next step. However, if you want to continue with demos, try the following tutorial:
 
 > [!div class="nextstepaction"]
 > [Tutorial: Add search to web apps](tutorial-csharp-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランキングの追加に関するクイックスタートの更新"
}
```

### Explanation
このコード変更は、「search-get-started-semantic.md」というドキュメントに対する修正を示しており、17行の追加と16行の削除があり、合計で33行の変更が行われました。

主な変更点は、ドキュメントのタイトルが「Quickstart: semantic ranking」から「Quickstart: Add Semantic Ranking to an Index Using .NET or Python」に変更されたことです。この変更により、内容がタイトルからより具体的にわかるようになりました。また、セマンティックランキングの説明が改善され、この機能がどのように検索結果を再スコアリングし、最も関連性の高い一致を促進するかが明確に示されています。

クイックスタートの手順が整理され、セマンティックランキングを活用するためのインデックスとクエリの変更についてより効果的に説明されています。前提条件セクションでは、Azureアカウントの作成方法や、セマンティックランカーを有効にしたAzure AI Searchサービスが必要であることが強調され、具体的な手順が加えられています。

また、APIキーの取得に関する情報が整理され、Azureポータルでの検索サービスの見つけ方とその操作手順が明確化されました。最後に、次のステップとして推奨されるチュートリアルへのリンクが更新され、読者がさらに学ぶための導線が整備されています。

全体として、この修正は、Azure AI Searchにおけるセマンティックランキングの機能を活用する方法を明確にし、利用者がスムーズに実装できるようにすることを目的としています。

## articles/search/search-get-started-skillset.md{#item-079744}

<details>
<summary>Diff</summary>
````diff
@@ -1,36 +1,35 @@
 ---
-title: "Quickstart: Create a skillset in the Azure portal"
+title: "Quickstart: Create a Skillset in the Azure Portal"
 titleSuffix: Azure AI Search
-description: Learn how to use the Import Data wizard to generate searchable text from images and unstructured documents. Skills in this quickstart include OCR, image analysis, and natural language processing.
-
+description: Learn how to use the Import Data wizard to generate searchable text from images and unstructured documents. Skills in this quickstart include optical character recognition (OCR), image analysis, and natural language processing.
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: quickstart
-ms.date: 11/20/2024
+ms.date: 03/04/2025
 ---
 
 # Quickstart: Create a skillset in the Azure portal
 
 In this quickstart, you learn how a skillset in Azure AI Search adds optical character recognition (OCR), image analysis, language detection, text translation, and entity recognition to generate text-searchable content in a search index.
 
-You can run the **Import data** wizard in the Azure portal to apply skills that create and transform textual content during indexing. Input is your raw data, usually blobs in Azure Storage. Output is a searchable index containing AI-generated image text, captions, and entities. Generated content is queryable in the Azure portal using [**Search explorer**](search-explorer.md).
+You can run the **Import data** wizard in the Azure portal to apply skills that create and transform textual content during indexing. The input is your raw data, usually blobs in Azure Storage. The output is a searchable index containing AI-generated image text, captions, and entities. You can query generated content in the Azure portal using [**Search explorer**](search-explorer.md).
 
 To prepare, you create a few resources and upload sample files before running the wizard.
 
 ## Prerequisites
 
 + An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/).
 
-+ Create an [Azure AI Search service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices). You can use a free service for this quickstart. 
++ An Azure AI Search service. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch) in your current subscription. For this quickstart, you can use a free service.
 
 + An Azure Storage account with Azure Blob Storage.
 
 > [!NOTE]
-> This quickstart uses [Azure AI services](https://azure.microsoft.com/services/cognitive-services/) for the AI transformations. Because the workload is so small, Azure AI services is tapped behind the scenes for free processing for up to 20 transactions. You can complete this exercise without having to create an Azure AI multi-service resource.
+> This quickstart uses [Azure AI services](https://azure.microsoft.com/services/cognitive-services/) for AI transformations. Because the workload is so small, Azure AI services is tapped behind the scenes for free processing for up to 20 transactions. You can complete this exercise without having to create an Azure AI multi-service resource.
 
 ## Set up your data
 
@@ -192,7 +191,7 @@ If you used a free service, remember that you're limited to three indexes, index
 
 ## Next step
 
-You can create skillsets using the Azure portal, .NET SDK, or REST API. To further your knowledge, try the REST API by using a REST client and more sample data.
+You can create skillsets using the Azure portal, .NET SDK, or REST API. To further your knowledge, try the REST API by using a REST client and more sample data:
 
 > [!div class="nextstepaction"]
 > [Tutorial: Use skillsets to generate searchable content in Azure AI Search](cognitive-search-tutorial-blob.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureポータルでのスキルセット作成に関するクイックスタートの更新"
}
```

### Explanation
このコード変更は、「search-get-started-skillset.md」というドキュメントに対する修正を示しており、7行の追加と8行の削除があり、合計で15行の変更が行われました。

変更の主なポイントは、ドキュメントのタイトルが「Quickstart: Create a skillset in the Azure portal」から「Quickstart: Create a Skillset in the Azure Portal」に修正されたことです。この変更はタイトルの一貫性を保ち、プロフェッショナルな印象を与えるためのものです。また、説明文には「光学式文字認識（OCR）」がフルスペルで追加され、技術的な用語の明確さが向上しています。

クイックスタートの内容は、Azure AI Searchにおけるスキルセットの機能について明確に説明しており、インポートデータウィザードを使用してテキスト検索可能なコンテンツを生成する方法が詳述されています。前提条件セクションでは、必要なリソースに関する情報が整理され、Azureストレージアカウントに関する情報が追加されました。これにより、手順がより具体的でわかりやすくなっています。

また、Azure AIサービスが無償で20回までの処理を提供することに関する注意書きが整理され、クイックスタートを完了するのに特別なリソースを作成する必要がないことが強調されています。最後に、次のステップとしてREST APIを使用することが推奨され、関連するチュートリアルへのリンクが更新されました。

全体として、この修正は、Azure AI Searchにおけるスキルセットの作成方法を明確にし、利用者がスムーズに実装できるようサポートすることを目的としています。

## articles/search/search-get-started-text.md{#item-935941}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Quickstart: Full text search using the Azure SDKs'
+title: 'Quickstart: Full Text Search Using the Azure SDKs'
 titleSuffix: Azure AI Search
 description: "Learn how to create, load, and query a search index using the Azure SDKs for .NET, Python, Java, and JavaScript."
 manager: nitinme
@@ -15,7 +15,7 @@ ms.custom:
   - ignite-2023
 ms.topic: quickstart
 zone_pivot_groups: search-quickstart-full-text
-ms.date: 2/19/2025
+ms.date: 03/04/2025
 ---
 
 # Quickstart: Full text search using the Azure SDKs
@@ -60,7 +60,9 @@ If you're using a free service, remember that you're limited to three indexes, i
 
 ## Next step
 
-In this quickstart, you worked through a set of tasks to create an index, load it with documents, and run queries. At different stages, we took shortcuts to simplify the code for readability and comprehension. Now that you're familiar with the basic concepts, try a tutorial that calls the Azure AI Search APIs in a web app.
+In this quickstart, you worked through a set of tasks to create an index, load it with documents, and run queries. At different stages, we took shortcuts to simplify the code for readability and comprehension.
+
+Now that you're familiar with the basic concepts, try a tutorial that calls the Azure AI Search APIs in a web app:
 
 > [!div class="nextstepaction"]
 > [Tutorial: Add search to web apps](tutorial-csharp-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure SDKを使用したフルテキスト検索に関するクイックスタートの更新"
}
```

### Explanation
このコード変更は、「search-get-started-text.md」というドキュメントに対する修正を示しており、5行の追加と3行の削除があり、合計で8行の変更が行われました。

主な変更点は、ドキュメントのタイトルが「Quickstart: Full text search using the Azure SDKs」から「Quickstart: Full Text Search Using the Azure SDKs」に変更されたことです。この変更は、タイトルの正確さとプロフェッショナルなスタイルを向上させるためのものです。また、ドキュメントの日付が「2/19/2025」から「03/04/2025」に更新され、最新の状態に保たれています。

クイックスタートの内容には、インデックスを作成し、ドキュメントをロードし、クエリを実行する一連のタスクが示されています。コードの可読性と理解を促進するために、簡略化された手法が適用されています。その後、基本的な概念に慣れた読者に対して、Azure AI Search APIをウェブアプリに呼び出すチュートリアルを試すことが推奨されています。この部分が新たに追加され、次のステップへの明確な導線が提供されています。

全体として、この修正は、Azure SDKを使用したフルテキスト検索の仕組みを明確にし、利用者が次のステップに進むためのサポートを提供することを目的としています。

## articles/search/search-get-started-vector.md{#item-4984d9}

<details>
<summary>Diff</summary>
````diff
@@ -1,35 +1,34 @@
 ---
-title: Quickstart vector search
+title: 'Quickstart: Vector Search Using REST APIs'
 titleSuffix: Azure AI Search
-description: In this quickstart, learn how to call the Azure AI Search REST APIs for vector workloads.
+description: Learn how to call the Search REST APIs for vector workloads in Azure AI Search.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: quickstart
-ms.date: 12/03/2024
+ms.date: 03/04/2025
 ---
 
-# Quickstart: Vector search by using REST
+# Quickstart: Vector search using REST
 
-Learn how to use the [Search REST APIs](/rest/api/searchservice) to create, load, and query vectors in Azure AI Search.
+In this quickstart, you use the [Azure AI Search REST APIs](/rest/api/searchservice) to create, load, and query vectors.
 
 In Azure AI Search, a [vector store](vector-store.md) has an index schema that defines vector and nonvector fields, a vector search configuration for algorithms that create the embedding space, and settings on vector field definitions that are evaluated at query time. The [Create Index](/rest/api/searchservice/indexes/create-or-update) REST API creates the vector store.
 
-If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.
-
 > [!NOTE]
 > This quickstart omits the vectorization step and provides embeddings in sample documents. If you want to add [built-in data chunking and vectorization](vector-search-integrated-vectorization.md) over your own content, try the [**Import and vectorize data** wizard](search-get-started-portal-import-vectors.md) for an end-to-end walkthrough.
 
 ## Prerequisites
 
-- [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
+- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
 
-- [Azure AI Search](search-what-is-azure-search.md), in any region and on any tier. [Create](search-create-service-portal.md) or [find an existing Azure AI Search resource](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch) under your current subscription.
-    - You can use the *Free* tier for most of this quickstart, but *Basic* or higher is recommended for larger data files. 
-    - To run the query example that invokes [semantic reranking](semantic-search-overview.md), your search service must be the *Basic* tier or higher, with [semantic ranker enabled](semantic-how-to-enable-disable.md).
+- An Azure AI Search service. [Create a service](search-create-service-portal.md) or [find an existing service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch) in your current subscription.
+    - You can use a free search service for most of this quickstart, but we recommend the Basic tier or higher for larger data files.
+    - To run the query example that invokes [semantic reranking](semantic-search-overview.md), your search service must be at the Basic tier or higher with [semantic ranker enabled](semantic-how-to-enable-disable.md).
 
+- [Visual Studio Code](https://code.visualstudio.com/download) with a [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
 
 ## Retrieve resource information
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIを使ったベクトル検索に関するクイックスタートの更新"
}
```

### Explanation
このコード変更は、「search-get-started-vector.md」というドキュメントに対する修正を示しており、10行の追加と11行の削除があり、合計で21行の変更が行われました。

主な変更点は、ドキュメントのタイトルが「Quickstart vector search」から「Quickstart: Vector Search Using REST APIs」に変更されたことです。これにより、ドキュメントの内容がより具体的にタイトルで示され、読者にその目的が明確になります。また、説明文が「In this quickstart, learn how to call the Azure AI Search REST APIs for vector workloads.」から「Learn how to call the Search REST APIs for vector workloads in Azure AI Search.」に変更され、より直截的で分かりやすくなっています。

更新日付も「12/03/2024」から「03/04/2025」に変更され、コンテンツが最新の状態に保たれています。クイックスタートの導入部分では、ベクトルの作成、ロード、クエリの取得にAzure AI Search REST APIを使用することが明記されました。

前提条件のセクションが整然とした形式に整理され、Azureアカウントの作成やAzure AI Searchサービスの利用についての情報が明確に提供されています。また、Visual Studio CodeとRESTクライアントに関する情報が最後に加えられ、このクイックスタートを実行するために必要なツールが詳述されています。

全体として、この修正は、Azure AI Searchを利用したベクトル検索の手順を明確にし、ユーザーが効率的に学習できるようサポートすることを目的としています。

## articles/search/search-manage.md{#item-4043d7}

<details>
<summary>Diff</summary>
````diff
@@ -1,135 +1,114 @@
 ---
-title: Portal administration
+title: Service Configuration in the Azure portal
 titleSuffix: Azure AI Search
-description: Manage an Azure AI Search resource using the Azure portal.
-
+description: Manage your new Azure AI Search service in the Azure portal. This article provides a day-one checklist for configuring RBAC, managed identities, network security, and more.
 manager: nitinme
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
-ms.topic: conceptual
-ms.date: 12/10/2024
+ms.topic: how-to
+ms.date: 03/04/2025
 ---
 
-# Service administration for Azure AI Search in the Azure portal
-
-> [!div class="op_single_selector"]
->
-> + [PowerShell](search-manage-powershell.md)
-> + [Azure CLI](search-manage-azure-cli.md)
-> + [REST API](search-manage-rest.md)
+# Configure your Azure AI Search service in the Azure portal
 
-In Azure AI Search, the [Azure portal](https://portal.azure.com) supports a broad range of administrative and content management operations so that you don't have to write code unless you want automation. 
+Configuring your new Azure AI Search service involves several tasks to optimize security, access, and performance. This article provides a day-one checklist to help you set up your service in the [Azure portal](https://portal.azure.com).
 
-Each search service is managed as a standalone resource. Your role assignment determines what operations are exposed in the Azure portal.
+After you create a search service, we recommend that you:
 
-## Portal and administrator permissions
+> [!div class="checklist"]
+>
+> + [Configure role-based access](#configure-role-based-access)
+> + [Configure a managed identity](#configure-a-managed-identity)
+> + [Configure network security](#configure-network-security)
+> + [Check capacity and understand billing](#check-capacity-and-understand-billing)
+> + [Enable diagnostic logging](#enable-diagnostic-logging)
+> + [Provide connection information to developers](#provide-connection-information-to-developers)
 
-Portal access is through [role assignments](search-security-rbac.md). By default, all search services start with at least one Service Administrator or Owner. Service administrators, co-administrators, and owners have permission to create other administrators and other role assignments. They have full access to all portal pages and operations on a default search service.
+## Configure role-based access
 
-If you disable API keys on a search service and use roles only, administrators must grant themselves data plane role assignments for full access to objects and data. These role assignments include Search Service Contributor, Search Index Data Contributor, and Search Index Data Reader.
+Portal access is based on [role assignments](search-security-rbac.md). By default, new search services have at least one service administrator or owner. Service administrators, co-administrators, and owners have permission to create more administrators and assign other roles. They also have access to all portal pages and operations on default search services.
 
 > [!TIP]
-> By default, any owner or administrator can create or delete services. To prevent accidental deletions, you can [lock resources](/azure/azure-resource-manager/management/lock-resources).
-
-## Azure portal at a glance
-
-The overview page is the home page of each service. In the following screenshot, the red boxes indicate tasks, tools, and tiles that you might use often, especially if you're new to the service.
+> By default, any administrator or owner can create or delete services. To prevent accidental deletions, consider [locking your resources](/azure/azure-resource-manager/management/lock-resources).
 
-:::image type="content" source="media/search-manage/search-portal-overview-page.png" alt-text="Portal pages for a search service" border="true":::
+Each search service comes with [API keys](search-security-api-keys.md) and uses key-based authentication by default. However, we recommend using Microsoft Entra ID and role-based access control (RBAC) for improved security. RBAC eliminates the need to store and pass API keys in plain text.
 
-| Area | Description |
-|------|-------------|
-| 1 | A command bar at the top of the page includes [Import data wizard](search-get-started-portal.md) and [Search explorer](search-explorer.md), used for prototyping and exploration. |
-| 2 | The **Essentials** section lists service properties, such as the service endpoint, service tier, and replica and partition counts. |
-| 3 | Tabbed pages in the center provide quick access to usage statistics and service health metrics. |
-| 4 | Navigation links to existing indexes, indexers, data sources, and skillsets. |
+When you switch from key-based authentication to keyless authentication, service administrators must assign themselves data plane roles for full access to objects and data. These roles include Search Service Contributor, Search Index Data Contributor, and Search Index Data Reader.
 
-You can't change the search service name, subscription, resource group, region (location), or tier. Switching tiers requires creating a new service or filing a support ticket to request a tier upgrade, which is only supported for Basic and higher.
+To configure role-based access:
 
-## Day-one management checklist
+1. [Enable roles](search-security-enable-roles.md) on your search service. We recommend using both API keys and roles.
 
-On a new search service, we recommend these configuration tasks.
+1. [Assign data plane roles](search-security-rbac.md) to replace the functionality lost when you disable API keys. An owner only needs Search Index Data Reader, but developers need [more roles](search-security-rbac.md#assign-roles).
 
-### Enable role-based access
+   Role assignments can take several minutes to take effect. Until then, portal pages used for data plane operations display the following message:
 
-A search service is always created with [API keys](search-security-api-keys.md) and uses key-based authentication by default. However, using Microsoft Entra ID and role assignments is a more secure option because it eliminates storing and passing keys in plain text.
+   :::image type="content" source="media/search-security-rbac/you-do-not-have-access.png" alt-text="Screenshot of the portal message indicating insufficient permissions.":::
 
-1. [Enable roles](search-security-enable-roles.md) on your search service. We recommend the roles-only option.
+1. [Assign more roles](search-security-rbac.md) for solution developers and apps.
 
-1. For administration, [assign data plane roles](search-security-rbac.md) to replace the functionality lost when you disable API keys. Role assignments include Search Service Contributor, Search Index Data Contributor, and Search Index Data Reader. You need all three.
+## Configure a managed identity
 
-   Sometimes it can take five to ten minutes for role assignments to take effect. Until that happens, the following message appears in the Azure portal pages used for data plane operations.
+If you plan to use indexers for automated indexing, applied AI, or integrated vectorization, you should [configure your search service to use a managed identity](search-howto-managed-identities-data-sources.md). You can then assign roles on other Azure services that authorize your search service to access data and operations.
 
-   :::image type="content" source="media/search-security-rbac/you-do-not-have-access.png" alt-text="Screenshot of portal message indicating insufficient permissions.":::
-
-1. Continue to [add more role assignments](search-security-rbac.md) for solution developers and apps.
-
-### Configure a managed identity
-
-If you plan to use indexers for automated indexing, applied AI, or integrated vectorization, you should [configure the search service to use a managed identity](search-howto-managed-identities-data-sources.md). You can then add role assignments on other Azure services that authorize your search service to access data and operations.
-
-For integrated vectorization, a search service identity needs:
+For integrated vectorization, your search service identity needs the following roles:
 
 + Storage Blob Data Reader on Azure Storage
 + Cognitive Services Data User on an Azure AI multiservice account
 
-It can take several minutes for role assignments to take effect.
-
-Before moving on to network security, consider testing all points of connection to validate role assignments. Run either the [Import data wizard](search-get-started-portal.md) or the [Import and vectorize data wizard](search-get-started-portal-image-search.md) to test permissions. 
+Role assignments can take several minutes to take effect.
 
-### Configure network security
+Before you move on to network security, consider testing all points of connection to validate role assignments. Run either the [**Import data** wizard](search-get-started-portal.md) or the [**Import and vectorize data** wizard](search-get-started-portal-image-search.md) to test permissions.
 
-By default, a search service accepts authenticated and authorized requests over public internet connections. Network security restricts access through firewall rules, or by disabling public connections and allowing requests only from Azure virtual networks.
+## Configure network security
 
-+ [Configure network access](service-configure-firewall.md) to restrict access by IP addresses.
-+ [Configure a private endpoint](service-create-private-endpoint.md) using Azure Private Link and a private virtual network.
+By default, a search service accepts authenticated and authorized requests over public internet connections. You have two options for enhancing network security:
 
-[Security in Azure AI Search](search-security-overview.md) explains inbound and outbound calls in Azure AI Search.
++ [Configure firewall rules](service-configure-firewall.md) to restrict network access by IP address.
++ [Configure a private endpoint](service-create-private-endpoint.md) to only allow traffic from Azure virtual networks. Note that when you turn off the public endpoint, the import wizards won't run.
 
-### Check capacity and understand billing
+To learn about inbound and outbound calls in Azure AI Search, see [Security in Azure AI Search](search-security-overview.md).
 
-By default, a search service is created in a minimum configuration of one replica and partition each. You can [add capacity](search-capacity-planning.md) by adding replicas and partitions, but we recommend waiting until volumes require it. Many customers run production workloads on the minimum configuration.
+## Check capacity and understand billing
 
-Some features add to the cost of running the service:
+By default, a search service is created with one replica and one partition. You can [add capacity](search-capacity-planning.md) by adding replicas and partitions, but we recommend waiting until volumes require it. Many customers run production workloads on the minimum configuration.
 
-+ [How you're charged for Azure AI Search](search-sku-manage-costs.md#how-youre-charged-for-azure-ai-search) explains which features have billing impact.
-+ [(Optional) disable semantic ranker](semantic-how-to-enable-disable.md) at the service level to prevent usage of the feature.
+Semantic ranker increases the cost of running your service. If you don't want to use this feature, you can [disable semantic ranker](semantic-how-to-enable-disable.md) at the service level.
 
-### Enable diagnostic logging
+To learn about other features that affect billing, see [How you're charged for Azure AI Search](search-sku-manage-costs.md#how-youre-charged-for-azure-ai-search).
 
-[Enable diagnostic logging](search-monitor-enable-logging.md) to track user activity. If you skip this step, you still get [activity logs](/azure/azure-monitor/essentials/activity-log)  and [platform metrics](/azure/azure-monitor/essentials/data-platform-metrics#types-of-metrics) automatically, but if you want index and query usage information, you should enable diagnostic logging and choose a destination for logged operations. 
+## Enable diagnostic logging
 
-We recommend Log Analytics Workspace for durable storage so that you can run system queries in the Azure portal.
+[Enable diagnostic logging](search-monitor-enable-logging.md) to track user activity. If you skip this step, you still get [activity logs](/azure/azure-monitor/essentials/activity-log) and [platform metrics](/azure/azure-monitor/essentials/data-platform-metrics#types-of-metrics) automatically. However, if you want index and query usage information, you should enable diagnostic logging and choose a destination for logged operations. We recommend Log Analytics Workspace for durable storage so that you can run system queries in the Azure portal.
 
 Internally, Microsoft collects telemetry data about your service and the platform. To learn more about data retention, see [Retention of metrics](/azure/azure-monitor/essentials/data-platform-metrics#retention-of-metrics).
 
-> [!NOTE]
-> See the ["Data residency"](search-security-overview.md#data-residency) section of the security overview article for more information about data location and privacy.
+To learn more about data location and privacy, see [Data residency](search-security-overview.md#data-residency).
 
-### Enable semantic ranker
+## Enable semantic ranker
 
-Semantic ranker is free for the first 1,000 requests per month. It's enabled by default on newer services.
+Semantic ranker is free for the first 1,000 requests per month. It's enabled by default on newer search services.
 
-In Azure portal, under **Settings** on the leftmost pane, select **Semantic ranker** and then choose the Free plan. For more information, see [Enable semantic ranker](semantic-how-to-enable-disable.md).
+To enable semantic ranker in the portal, select **Settings** > **Semantic ranker** from the left pane, and then select the **Free** plan. For more information, see [Enable semantic ranker](semantic-how-to-enable-disable.md).
 
-### Provide connection information to developers
+## Provide connection information to developers
 
-Developers need the following information to connect to Azure AI Search:
+To connect to Azure AI Search, developers need:
 
-+ An endpoint or URL, provided on the **Overview** page.
-+ An API key from the **Keys** page, or a role assignment (contributor is recommended).
++ An endpoint or URL from the **Overview** page.
++ An API key from the **Keys** page or a role assignment. We recommend Search Service Contributor, Search Index Data Contributor, and Search Index Data Reader.
 
-We recommend portal access for the following wizards and tools: [Import data wizard](search-get-started-portal.md), [Import and vectorize data](search-get-started-portal-import-vectors.md), [Search explorer](search-explorer.md). Recall that a user must be a contributor or above to run the import wizards.
+We recommend portal access for the [**Import data** wizard](search-get-started-portal.md), the [**Import and vectorize data** wizard](search-get-started-portal-import-vectors.md), and [Search explorer](search-explorer.md). You must be a contributor or higher to run the wizards.
 
-## Next steps
+## Related content
 
-Programmatic support for service administration can be found in the following APIs and modules:
+For programmatic support for service administration, see the following APIs and modules:
 
-* [Management REST API reference](/rest/api/searchmanagement/)
-* [Az.Search PowerShell module](search-manage-powershell.md)
-* [az search Azure CLI module](search-manage-azure-cli.md)
++ [Management REST API reference](/rest/api/searchmanagement/)
++ [Az.Search PowerShell module](search-manage-powershell.md)
++ [az search Azure CLI module](search-manage-azure-cli.md)
 
-You can also use the management client libraries in the Azure SDKs for .NET, Python, Java, and JavaScript. 
+You can also use the management client libraries in the Azure SDKs for .NET, Python, Java, and JavaScript.
 
-There's feature parity across all modalities and languages, except for preview management features. As a general rule, preview management features are released through the Management REST API first. 
\ No newline at end of file
+There's feature parity across all modalities and languages, except for preview management features. As a general rule, preview management features are released through the Management REST API first.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureポータルでのサービス構成に関するアップデート"
}
```

### Explanation
このコード変更は、「search-manage.md」というドキュメントに対する修正を示しており、58行の追加と79行の削除があり、合計で137行の変更が行われました。

主な変更点として、ドキュメントのタイトルが「Portal administration」から「Service Configuration in the Azure portal」に変更され、内容に適したより具体的なタイトルになりました。また、説明文も変更されており、Azure AI SearchサービスをAzureポータルで管理するための「初日チェックリスト」に言及され、RBAC（ロールベースのアクセス制御）、マネージドアイデンティティ、ネットワークセキュリティなどの設定について触れています。

文書構成も大幅に見直され、設定手順がチェックリスト形式で整理されました。これにより、ユーザーが必要な設定作業を明確に把握でき、効率的にサービスを構成できるようになっています。特に、RBACの設定、ネットワークセキュリティの構成、診断ログの有効化など、具体的なタスクがすぐに確認できるようになっています。

また、サービスの構成に伴う料金体系や、リソースをロックして accidental deletion（誤削除）を防ぐ方法も明記されており、セキュリティやコスト管理に関する注意点も強調されています。これらの変更により、ユーザーはAzureポータルでのサービス管理についてより体系的に理解しやすくなっています。

全体として、この修正は、Azure AI Searchサービスの設定と管理に関連する情報を整理し、利用者が必要な手続きを簡潔に行えるようサポートすることを目的としています。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -8,92 +8,56 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: how-to
-ms.date: 12/06/2024
+ms.date: 03/03/2025
 ms.custom:
   - references_regions
   - ignite-2023
 ---
 
 # Configure customer-managed keys for data encryption in Azure AI Search
 
-Azure AI Search automatically encrypts data at rest with [service-managed keys](/azure/security/fundamentals/encryption-atrest#azure-encryption-at-rest-components). If more protection is needed, you can supplement default encryption with another encryption layer using keys that you create and manage in Azure Key Vault. 
+Azure AI Search automatically encrypts data at rest with [Microsoft-managed keys](/azure/security/fundamentals/encryption-atrest#azure-encryption-at-rest-components). If you need another layer of encryption or the ability to revoke keys and shut down access to content, you can use keys that you create and manage in Azure Key Vault. This article explains how to set up customer-managed key (CMK) encryption.
 
-This article walks you through the steps of setting up customer-managed key (CMK) or "bring-your-own-key" (BYOK) encryption.
+You can store keys using either Azure Key Vault or Azure Key Vault Managed HSM (Hardware Security Module). An Azure Key Vault Managed HSM is an FIPS 140-2 Level 3 validated HSM. HSM support is new in Azure AI Search. To migrate to HSM, [rotate your keys](#rotate-or-update-encryption-keys) and choose Managed HSM for storage.
 
-> [!NOTE]
-> If an index is CMK encrypted, it's only accessible if the search service has access to the key. If access is revoked, the index is unusable and the service cannot be scaled until the index is deleted or access to the key is restored.
+> [!IMPORTANT]
+> CMK encryption is irreversible. You can rotate keys and change CMK configuration, but index encryption lasts for the lifetime of the index. Post-CMK encryption, an index is only accessible if the search service has access to the key. If you revoke access to the key by deleting or changing role assignment, the index is unusable and the service can't be scaled until the index is deleted or access to the key is restored. If you delete or rotate keys, the most recent key is cached for up to 60 minutes.
 
 ## CMK encrypted objects
 
-CMK encryption is applied to individual objects. If you require CMK across your search service, [set an enforcement policy](#set-up-a-policy-to-enforce-cmk-compliance).
-
-CMK encryption is applied when an object is created, which means you can't encrypt objects that already exist. CMK encryption occurs each time an object is saved to disk, for both data at rest (long-term storage) or temporary cached data (short-term storage). With CMK, the disk never sees unencrypted data.
+CMK encryption applies to individual objects when they're created. This means you can't encrypt objects that already exist. CMK encryption occurs each time an object is saved to disk, for both data at rest (long-term storage) or temporary cached data (short-term storage). With CMK, the disk never sees unencrypted data.
 
 Objects that can be encrypted include indexes, synonym lists, indexers, data sources, and skillsets. Encryption is computationally expensive to decrypt so only sensitive content is encrypted.
 
 Encryption is performed over the following content:
 
 + All content within indexes and synonym lists.
 
-+ Sensitive content in indexers, data sources, skillsets, and vectorizers. This content consists of only those fields that store connection strings, descriptions, identities, keys, and user inputs. For example, skillsets have Azure AI services keys, and some skills accept user inputs, such as custom entities. In both cases, keys and user inputs into skills are encrypted. Any references to external resources (such as Azure data sources or Azure OpenAI models) are also encrypted.
-
-## Full double encryption
-
-When you introduce CMK encryption, you're encrypting content twice. For the objects and fields noted in the previous section, content is first encrypted with your CMK, and secondly with the Microsoft-managed key. Content is doubly encrypted on data disks for long-term storage, and on temporary disks used for short-term storage.
-
-Enabling CMK encryption increases index size and degrades query performance. Based on observations to date, you can expect to see an increase of 30-60 percent in query times, although actual performance varies depending on the index definition and types of queries. Because performance is diminished, we recommend that you only enable this feature on objects that really require it.
-
-Although double encryption is now available in all regions, support was rolled out in two phases:
-
-+ The first rollout was on August 1, 2020 and included the five regions listed below. Search services created in the following regions supported CMK for data disks, but not temporary disks:
-
-  + West US 2
-  + East US
-  + South Central US
-  + US Gov Virginia
-  + US Gov Arizona
++ Sensitive content in indexers, data sources, skillsets, and vectorizers. Sensitive content refers to connection strings, descriptions, identities, keys, and user inputs. For example, skillsets have Azure AI services keys, and some skills accept user inputs, such as custom entities. In both cases, keys and user inputs are encrypted. Any references to external resources (such as Azure data sources or Azure OpenAI models) are also encrypted.
 
-+ The second rollout on May 13, 2021 added encryption for temporary disks and extended CMK encryption to [all supported regions](search-region-support.md).
-
-  If you're using CMK from a service created during the first rollout and you also want CMK encryption over temporary disks, you need to create a new search service in your region of choice and redeploy your content. To determine your service creation date, see [How to check service creation date](vector-search-index-size.md#how-to-check-service-creation-date).
+If you require CMK across your search service, [set an enforcement policy](#set-up-a-policy-to-enforce-cmk-compliance).
 
 ## Prerequisites
 
-+ [Azure AI Search](search-create-service-portal.md) on a [billable tier](search-sku-tier.md#tier-descriptions) (Basic or above, in any region).
-
-+ [Azure Key Vault](/azure/key-vault/general/overview) in the same subscription as Azure AI Search. You can [create a key vault using the Azure portal](/azure/key-vault/general/quick-create-portal), [Azure CLI](/azure/key-vault/general/quick-create-cli), or [Azure PowerShell](/azure/key-vault/general/quick-create-powershell). The key vault must have **soft-delete** and **purge protection** enabled. 
-
-+ A search client that can create an encrypted object, such as a [REST client](search-get-started-rest.md), [Azure PowerShell](search-get-started-powershell.md), or an Azure SDK (Python, .NET, Java, JavaScript). 
-
-## Limitations
-
-+ No support for Azure Key Vault Managed Hardware Security Model (HSM).
-
-+ No cross-subscription support. Azure Key Vault and Azure AI Search must be in the same subscription.
-
-## Key Vault tips
++ [Azure AI Search](search-create-service-portal.md) on a [billable tier](search-sku-tier.md#tier-descriptions) (Basic or higher, in any region).
 
-If you're new to Azure Key Vault, review this quickstart to learn about basic tasks: [Set and retrieve a secret from Azure Key Vault using PowerShell](/azure/key-vault/secrets/quick-create-powershell). 
++ [Azure Key Vault](/azure/key-vault/general/overview) and a key vault with **soft-delete** and **purge protection** enabled. Or, [Azure Key Vault Managed HSM](/azure/key-vault/managed-hsm/overview). This resource can be in any subscription, but it must be in the same tenant as Azure AI Search.
 
-Here are some tips for using Key Vault:
++ Ability to set up permissions for key access and to assign roles. To create keys, you must be **Key Vault Crypto Officer** in Azure Key Vault or **Managed HSM Crypto Officer** in Azure Key Vault Managed HSM.
 
-+ Use as many key vaults as you need. Managed keys can be in different key vaults. A search service can have multiple encrypted objects, each one encrypted with a different customer-managed encryption key, stored in different key vaults.
+  To assign roles, you must be subscription **Owner**, **User Access Administrator**, **Role-based Access Control Administrator**, or be assigned to a custom role with **Microsoft.Authorization/roleAssignments/write** permissions.
 
-+ Use the same tenant so that you can retrieve your managed key by connecting through a system or user-managed identity. This behavior requires both services to share the same tenant. For more information about creating a tenant, see [Set up a new tenant](/azure/active-directory/develop/quickstart-create-new-tenant).
+## Step 1: Create an encryption key
 
-+ [Enable purge protection](/azure/key-vault/general/soft-delete-overview#purge-protection) and [soft-delete](/azure/key-vault/general/soft-delete-overview). Due to the nature of encryption with customer-managed keys, no one can retrieve your data if your Azure Key Vault key is deleted. To prevent data loss caused by accidental Key Vault key deletions, soft-delete and purge protection must be enabled on the key vault. Soft-delete is enabled by default, so you'll only encounter issues if you purposely disable it. Purge protection isn't enabled by default, but it's required for customer-managed key encryption in Azure AI Search.
+Use either Azure Key Vault or Azure Key Vault Managed HSM to create a key. Azure AI Search encryption supports RSA keys of sizes 2048, 3072 and 4096. For more information about supported key types, see [About keys](/azure/key-vault/keys/about-keys).
 
-+ [Enable logging](/azure/key-vault/general/logging) on the key vault so that you can monitor key usage.
+We recommend reviewing [these tips](#key-vault-tips) before you start.
 
-+ [Enable autorotation of keys](/azure/key-vault/keys/how-to-configure-key-rotation) or follow strict procedures during routine rotation of key vault keys and application secrets and registration. Always update all [encrypted content](search-security-get-encryption-keys.md) to use new secrets and keys before deleting the old ones. If you miss this step, your content can't be decrypted.
+Required operations are **Wrap**, **Unwrap**, **Encrypt**, and **Decrypt**.
 
-## Step 1: Create a key in Key Vault
+### [**Azure Key Vault**](#tab/azure-key-vault)
 
-Skip key generation if you already have a key in Azure Key Vault that you want to use, but collect the key identifier. You need this information when creating an encrypted object.
-
-Before you add the key, make sure that you have assigned to yourself the **Key Vault Crypto Officer** role.
-
-Azure AI Search encryption supports RSA keys of sizes 2048, 3072 and 4096. For more information about supported key types, see [About keys](/azure/key-vault/keys/about-keys).
+You can [create a key vault using the Azure portal](/azure/key-vault/general/quick-create-portal), [Azure CLI](/azure/key-vault/general/quick-create-cli), or [Azure PowerShell](/azure/key-vault/general/quick-create-powershell).
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and open your key vault overview page.
 
@@ -107,19 +71,27 @@ Azure AI Search encryption supports RSA keys of sizes 2048, 3072 and 4096. For m
 
 1. Select **Create** to start the deployment.
 
-1. Select the key, select the current version, and then make a note of the key identifier. It's composed of the **key value Uri**, the **key name**, and the **key version**. You need the identifier to define an encrypted index in Azure AI Search.
+1. After the key is created, get its key identifier. Select the key, select the current version, and then copy the key identifier. It's composed of the **key value Uri**, the **key name**, and the **key version**. You need the identifier to define an encrypted index in Azure AI Search. Recall that required operations are **Wrap**, **Unwrap**, **Encrypt**, and **Decrypt**.
 
    :::image type="content" source="media/search-manage-encryption-keys/cmk-key-identifier.png" alt-text="Create a new key vault key" border="true":::
 
+### [**Managed HSM**](#tab/managed-hsm)
+
+You can create and activate a Managed HSM in the Azure portal, [Azure CLI](/azure/key-vault/managed-hsm/quick-create-cli), or [Azure PowerShell](/azure/key-vault/managed-hsm/quick-create-powershell).
+
+To generate or import a key, use the [Azure CLI](/azure/key-vault/managed-hsm/key-management).
+
+---
+
 ## Step 2: Create a security principal
 
-You have several options for setting up Azure AI Search access to the encryption key at run time. The simplest approach is to retrieve the key using the managed identity of your search service. You can use either a system or user-managed identity. Doing so allows you to omit the steps for application registration and application secrets. Alternatively, you can create and register a Microsoft Entra application and have the search service provide the application ID on requests.
+Create a security principal that your search service uses to access to the encryption key. You can use a managed identity and role assignment, or you can register an application and have the search service provide the application ID on requests.
 
-We recommend using a managed identity. A managed identity enables your search service to authenticate to Azure Key Vault without storing credentials (ApplicationID or ApplicationSecret) in code. The lifecycle of this type of managed identity is tied to the lifecycle of your search service, which can only have one system assigned managed identity. For more information about how managed identities work, see [What are managed identities for Azure resources](/azure/active-directory/managed-identities-azure-resources/overview).
+We recommend using a managed identity and roles. You can use either a system-managed identity or user-managed identity. A managed identity enables your search service to authenticate through Microsoft Entra ID, without storing credentials (ApplicationID or ApplicationSecret) in code. The lifecycle of this type of managed identity is tied to the lifecycle of your search service, which can only have one system assigned managed identity. For more information about how managed identities work, see [What are managed identities for Azure resources](/azure/active-directory/managed-identities-azure-resources/overview).
 
 ### [**System-managed identity**](#tab/managed-id-sys)
 
-Enable the system assigned managed identity for your search service.
+Enable the system assigned managed identity for your search service. It's a two-click operation, enable and save.
 
 ![Screenshot of turn on system assigned managed identity.](./media/search-managed-identities/turn-on-system-assigned-identity.png "Screenshot showing how to turn on the system-assigned managed identity.")
 
@@ -172,24 +144,10 @@ Enable the system assigned managed identity for your search service.
     } 
     ```
 
-1. Update the `"encryptionKey"` section to use an identity property. Make sure to use preview REST API version when sending this request to your search service.
-
-    ```json
-    {
-      "encryptionKey": {
-        "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
-        "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
-        "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
-        "identity" : { 
-            "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
-            "userAssignedIdentity" : "/subscriptions/<your-subscription-ID>/resourceGroups/<your-resource-group-name>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<your-managed-identity-name>"
-        }
-      }
-    }
-    ```
-
 ### [**Register an app**](#tab/register-app)
 
+Follow these instructions if you can't use role assignments for search service access to encryption keys.
+
 1. In the [Azure portal](https://portal.azure.com), find the Microsoft Entra resource for your subscription.
 
 1. On the left, under **Manage**, select **App registrations**, and then select **New registration**.
@@ -202,7 +160,7 @@ Enable the system assigned managed identity for your search service.
 
    :::image type="content" source="media/search-manage-encryption-keys/cmk-application-id.png" alt-text="Application ID in the Essentials section":::
 
-1. Next, select **Certificates & secrets** on the left.
+1. Next, select **Certificates & secrets**.
 
 1. Select **New client secret**. Give the secret a display name and select **Add**.
 
@@ -214,25 +172,50 @@ Enable the system assigned managed identity for your search service.
 
 ## Step 3: Grant permissions
 
-Azure Key Vault supports authorization using role-based access controls. We recommend this approach over key vault access policies. For more information, see [Provide access to Key Vault keys, certificates, and secrets using Azure roles](/azure/key-vault/general/rbac-guide).
+If you configured your search service to use a managed identity, assign roles that give it access to the encryption key.
 
-In this step, assign the **Key Vault Crypto Service Encryption User** role to your search service. If you're testing locally, assign this role to yourself as well.
+Role-based access control is recommended over the Access Policy permission model. For more information or migration steps, start with [Azure role-based access control (Azure RBAC) vs. access policies (legacy)](/azure/key-vault/general/rbac-access-policy).
 
 1. Sign in to the [Azure portal](https://portal.azure.com) and find your key vault.
 
 1. Select **Access control (IAM)** and select **Add role assignment**.
 
-1. Select **Key Vault Crypto Service Encryption User** and then select **Next**.
+1. Select a role:
+
+   + On Azure Key Vault, select **Key Vault Crypto Service Encryption User**.
+   + On Managed HSM, select **Managed HSM Crypto Service Encryption User**.
 
-1. Select managed identities, select members, and then select the managed identity of your search service.
+1. Select managed identities, select members, and then select the managed identity of your search service. If you're testing locally, assign this role to yourself as well.
 
 1. Select **Review + Assign**.
 
 Wait a few minutes for the role assignment to become operational.
 
 ## Step 4: Encrypt content
 
-Encryption keys are added when you create an object. To add a customer-managed key on an index, synonym map, indexer, data source, or skillset, use the Azure portal, a [Search REST API](/rest/api/searchservice/), or an Azure SDK to create an object that has encryption enabled. To add encryption using the Azure SDK, see the [Python example](#python-example-of-an-encryption-key-configuration) in this article.
+Encryption occurs when you create or update an object. You can use the Azure portal for selected objects. For any object, use the [Search REST API](/rest/api/searchservice/) or an Azure SDK. Review the [Python example](#python-example-of-an-encryption-key-configuration) in this article to see how content is encrypted programmatically.
+
+### [**Azure portal**](#tab/portal)
+
+When you create a new object in the Azure portal, you can specify a predefined customer-managed key in a key vault. The Azure portal lets you enable CMK encryption for:
+
++ Indexes
++ Data sources
++ Indexers
+
+Requirements for using the Azure portal are that the key vault and key must exist, and you completed the previous steps for authorized access to the key.
+
+In the Azure portal, skillsets are defined in JSON view. Use the JSON shown in the REST API examples to provide a customer-managed key on a skillset.
+
+1. Sign in to the [Azure portal](https://portal.azure.com) and open your search service page.
+
+1. Under **Search management**, select **Indexes**, **Indexers**, or **Data Sources**.
+
+1. Add a new object. In the object definition, select **Microsoft-managed encryption**.
+
+1. Select **Customer-managed keys** and use the pickers to select the vault, key, and version.
+
+:::image type="content" source="media/search-security-manage-encryption-keys/assign-key-vault-portal.png" alt-text="Screenshot of the encryption key page in the Azure portal.":::
 
 ### [**REST APIs**](#tab/rest)
 
@@ -244,7 +227,23 @@ Encryption keys are added when you create an object. To add a customer-managed k
    + [Create Data Source](/rest/api/searchservice/data-sources/create)
    + [Create Skillset](/rest/api/searchservice/skillsets/create)
 
-1. Insert the encryptionKey construct into the object definition. This property is a first-level property, on the same level as name and description. If you're using the same vault, key, and version, you can paste in the same encryptionKey construct into each object definition.
+1. Insert the encryptionKey construct into the object definition. This property is a first-level property, on the same level as name and description. If you're using the same vault, key, and version, you can paste in the same encryptionKey construct into each object definition. 
+
+   If your key identifier is `https://contoso-keyvault.vault.azure.net/keys/contoso-cmk/aaaaaaaa-0b0b-1c1c-2d2d-333333333333`, then the URI is `https://contoso-keyvault.vault.azure.net`, the key name is `contoso-cmk`, and the version is `aaaaaaaa-0b0b-1c1c-2d2d-333333333333`.
+
+    ```json
+    {
+      "encryptionKey": {
+        "keyVaultUri": "<YOUR-KEY-VAULT-URI>",
+        "keyVaultKeyName": "<YOUR-ENCRYPTION-KEY-NAME>",
+        "keyVaultKeyVersion": "<YOUR-ENCRYPTION-KEY-VERSION>",
+        "identity" : { 
+            "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
+            "userAssignedIdentity" : "/subscriptions/<your-subscription-ID>/resourceGroups/<your-resource-group-name>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<your-managed-identity-name>"
+        }
+      }
+    }
+    ```
 
    The first example shows an encryptionKey for a search service that connects using a managed identity:
 
@@ -282,40 +281,26 @@ Encryption keys are added when you create an object. To add a customer-managed k
    + [GET Data Source](/rest/api/searchservice/data-sources/get)
    + [GET Skillset](/rest/api/searchservice/skillsets/get)
 
-1. Verify the object is operational by performing a task, such as query an index that's been encrypted.
+1. Verify the object is operational by performing a task, such as query an index that's encrypted.
 
 Once you create the encrypted object on the search service, you can use it as you would any other object of its type. Encryption is transparent to the user and developer.
 
 None of these key vault details are considered secret and could be easily retrieved by browsing to the relevant Azure Key Vault page in Azure portal.
 
 > [!Important]
-> Encrypted content in Azure AI Search is configured to use a specific Azure Key Vault key with a specific *version*. If you change the key or version, the object must be updated to use it **before** you delete the previous one. Failing to do so renders the object unusable. You won't be able to decrypt the content if the key is lost.
-
-### [**Azure portal**](#tab/portal)
-
-When you create a new object in the Azure portal, you can specify a predefined customer-managed key in a key vault. You can enable CMK-encryption for:
-
-+ Indexes
-+ Data sources
-+ Indexers
-
-Requirements for using the Azure portal are that the key vault and key must exist, and you completed the previous steps for authorized access to the key.
-
-In the Azure portal, skillsets are defined in JSON view. Use the JSON shown in the REST API examples to provide a customer-managed key on a skillset.
-
-:::image type="content" source="media/search-security-manage-encryption-keys/assign-key-vault-portal.png" alt-text="Screenshot of the encryption key page in the Azure portal.":::
+> Encrypted content in Azure AI Search is configured to use a specific key with a specific *version*. If you change the key or version, the object must be updated to use it **before** you delete the previous one. Failing to do so renders the object unusable. You won't be able to decrypt the content if the key is lost.
 
 ---
 
 ## Step 5: Test encryption
 
 To verify encryption is working, revoke the encryption key, query the index (it should be unusable), and then reinstate the encryption key.
 
-Use the Azure portal for this task.
+Use the Azure portal for this task. Make sure you have a role assignment that grants read access to the key.
 
 1. On the Azure Key Vault page, select **Objects** > **Keys**.
 
-1. Select the key you just created, and then select **Delete**.
+1. Select the key you created, and then select **Delete**.
 
 1. On the Azure AI Search page, select **Search management** > **Indexes**.
 
@@ -331,55 +316,82 @@ Use the Azure portal for this task.
 
 ## Set up a policy to enforce CMK compliance
 
-Azure policies help to enforce organizational standards and to assess compliance at-scale. Azure AI Search has an optional [built-in policy for service-wide CMK enforcement](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F76a56461-9dc0-40f0-82f5-2453283afa2f).
+Azure policies help to enforce organizational standards and to assess compliance at-scale. Azure AI Search has two optional built-in policies related to CMK. These policies apply to new and existing search services.
 
-In this section, you set the policy that defines a CMK standard for your search service. Then, you set up your search service to enforce this policy.
+| Effect | Effect if enabled|
+|--------|------------------|
+| [**AuditIfNotExists**](/azure/governance/policy/concepts/effect-audit-if-not-exists) | Checks for compliance: do objects have a customer-managed key defined, and is the content encrypted. This effect applies to existing services with content. It's evaluated each time an object is created or updated, or [per the evaluation schedule](/azure/governance/policy/overview#understand-evaluation-outcomes). [Learn more...](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F356da939-f20a-4bb9-86f8-5db445b0e354) |
+| [**Deny**](/azure/governance/policy/concepts/effect-deny) | Checks for policy enforcement: does the search service have [SearchEncryptionWithCmk](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2023-11-01&tabs=HTTP#searchencryptionwithcmk&preserve-view=true) set to `Enabled`. This effect applies to new services only, which must be created with encryption enabled. Existing services remain operational but you can't update them unless you patch the service. None of the tools used for provisioning services expose this property, so be aware that setting the policy limits you to [programmatic set up](#enable-cmk-policy-enforcement).|
 
-1. Navigate to the [built-in policy](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F76a56461-9dc0-40f0-82f5-2453283afa2f) in your web browser. Select **Assign**
+### Assign a policy
 
-   :::image type="content" source="media/search-security-manage-encryption-keys/assign-policy.png" alt-text="Screenshot of assigning built-in CMK policy." border="true":::
+1. Navigate to a built-in policy and then select **Assign**.
 
-1. Set up the [policy scope](/azure/governance/policy/concepts/scope). In the **Parameters** section, uncheck **Only show parameters...** and set **Effect** to [**Deny**](/azure/governance/policy/concepts/effects#deny). 
+   + [AuditIfExists](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F76a56461-9dc0-40f0-82f5-2453283afa2f)
 
-   During evaluation of the request, a request that matches a deny policy definition is marked as noncompliant. Assuming the standard for your service is CMK encryption, "deny" means that requests that *don't* specify CMK encryption are noncompliant.
+   + [Deny](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F356da939-f20a-4bb9-86f8-5db445b0e354)
 
-   :::image type="content" source="media/search-security-manage-encryption-keys/effect-deny.png" alt-text="Screenshot of changing built-in CMK policy effect to deny." border="true":::
+   :::image type="content" source="media/search-security-manage-encryption-keys/assign-policy.png" alt-text="Screenshot of assigning built-in CMK policy." border="true":::
 
-1. Finish creating the policy.
+1. Set [policy scope](/azure/governance/policy/concepts/scope) by selecting the subscription and resource group. Exclude any search services for which the policy shouldn't apply.
 
-1. Call the [Services - Update API](/rest/api/searchmanagement/services/update) to enable CMK policy enforcement at the service level.
+1. Accept or modify the defaults. Select **Review +create**, followed by **Create**.
 
-```http
-PATCH https://management.azure.com/subscriptions/<your-subscription-Id>/resourceGroups/<your-resource-group-name>/providers/Microsoft.Search/searchServices/<your-search-service-name>?api-version=2023-11-01
+### Enable CMK policy enforcement
 
-{
-    "properties": {
-        "encryptionWithCmk": {
-            "enforcement": "Enabled"
-        }
-    }
-}
-```
++ For new search services, create them with [SearchEncryptionWithCmk](/rest/api/searchmanagement/services/create-or-update?view=rest-searchmanagement-2023-11-01&tabs=HTTP#searchencryptionwithcmk&preserve-view=true) set to `Enabled`. Neither the Azure portal nor the command line tools (the Azure CLI and Azure PowerShell) provide this property, but you can use [Management REST API](/rest/api/searchmanagement/services/create-or-update) to provision a search service with a CMK policy definition.
+
++ For existing search services, patch them using [Services - Update API](/rest/api/searchmanagement/services/update).
+
+   ```http
+   PATCH https://management.azure.com/subscriptions/<your-subscription-Id>/resourceGroups/<your-resource-group-name>/providers/Microsoft.Search/searchServices/<your-search-service-name>?api-version=2023-11-01
+  
+   {
+      "properties": {
+          "encryptionWithCmk": {
+              "enforcement": "Enabled"
+          }
+      }
+   }
+   ```
 
 ## Rotate or update encryption keys
 
-We recommend using the [autorotation capabilities of Azure Key Vault](/azure/key-vault/keys/how-to-configure-key-rotation), but you can also rotate keys manually.
+Use the following instructions to rotate keys or to migrate from Azure Key Vault to the Hardware Security Model (HSM). 
+
+For key rotation, we recommend using the [autorotation capabilities of Azure Key Vault](/azure/key-vault/keys/how-to-configure-key-rotation). If you use autorotation, omit the key version in object definitions. The latest key is used, rather than a specific version.
 
 When you change a key or its version, any object that uses the key must first be updated to use the new values **before** you delete the old values. Otherwise, the object becomes unusable because it can't be decrypted. 
 
+Recall that keys are cached for 60 minutes. Remember this when testing and rotating keys.
+
 1. [Determine the key used by an index or synonym map](search-security-get-encryption-keys.md).
 
-1. [Create a new key in key vault](/azure/key-vault/keys/quick-create-portal), but leave the original key available.
+1. [Create a new key in key vault](/azure/key-vault/keys/quick-create-portal), but leave the original key available. In this step, you can switch from key vault to HSM.
 
 1. [Update the encryptionKey properties](/rest/api/searchservice/indexes/create-or-update) on an index or synonym map to use the new values. Only objects that were originally created with this property can be updated to use a different value.
 
 1. Disable or delete the previous key in the key vault. Monitor key access to verify the new key is being used.
 
-For performance reasons, the search service caches the key for up to several hours. If you disable or delete the key without providing a new one, queries continue to work on a temporary basis until the cache expires. However, once the search service can no longer decrypt content, you get this message: "Access forbidden. The query key used might have been revoked - please retry." 
+For performance reasons, the search service caches the key for up to several hours. If you disable or delete the key without providing a new one, queries continue to work on a temporary basis until the cache expires. However, once the search service can no longer decrypt content, you get this message: `"Access forbidden. The query key used might have been revoked - please retry."` 
+
+## Key Vault tips
+
++ If you're new to Azure Key Vault, review this quickstart to learn about basic tasks: [Set and retrieve a secret from Azure Key Vault using PowerShell](/azure/key-vault/secrets/quick-create-powershell). 
+
++ Use as many key vaults as you need. Managed keys can be in different key vaults. A search service can have multiple encrypted objects, each one encrypted with a different customer-managed encryption key, stored in different key vaults.
+
++ Use the same [Azure tenant](/entra/fundamentals/create-new-tenant) so that you can retrieve your managed key through role assignments and by connecting through a system or user-managed identity. For more information about creating a tenant, see [Set up a new tenant](/azure/active-directory/develop/quickstart-create-new-tenant).
+
++ [Enable purge protection](/azure/key-vault/general/soft-delete-overview#purge-protection) and [soft-delete](/azure/key-vault/general/soft-delete-overview) on a key vault. Due to the nature of encryption with customer-managed keys, no one can retrieve your data if your Azure Key Vault key is deleted. To prevent data loss caused by accidental Key Vault key deletions, soft-delete and purge protection must be enabled on the key vault. Soft-delete is enabled by default, so you'll only encounter issues if you purposely disable it. Purge protection isn't enabled by default, but it's required for CMK encryption in Azure AI Search.
+
++ [Enable logging](/azure/key-vault/general/logging) on the key vault so that you can monitor key usage.
+
++ [Enable autorotation of keys](/azure/key-vault/keys/how-to-configure-key-rotation) or follow strict procedures during routine rotation of key vault keys and application secrets and registration. Always update all [encrypted content](search-security-get-encryption-keys.md) to use new secrets and keys before deleting the old ones. If you miss this step, your content can't be decrypted.
 
 ## Work with encrypted content
 
-With customer-managed key encryption, you might notice latency for both indexing and queries due to the extra encrypt/decrypt work. Azure AI Search doesn't log encryption activity, but you can monitor key access through key vault logging. 
+With CMK encryption, you might notice latency for both indexing and queries due to the extra encrypt/decrypt work. Azure AI Search doesn't log encryption activity, but you can monitor key access through key vault logging. 
 
 We recommend that you [enable logging](/azure/key-vault/general/logging) as part of key vault configuration.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchの暗号化キー管理に関する記事の更新"
}
```

### Explanation
このコード変更は、「search-security-manage-encryption-keys.md」というドキュメントに対する修正を示しており、134行の追加と122行の削除があり、合計で256行の変更が行われました。

主な変更点は、デフォルトの暗号化方法に関する表現の修正と、顧客管理キー（CMK）に関する手順が明確にされていることです。例えば、Azure AI Searchのデータは「サービス管理キー」ではなく「Microsoft管理キー」で自動的に暗号化されることが強調され、ユーザーが提供するキーを使用して暗号化を補完することができる設定が説明されています。また、HSM（ハードウェアセキュリティモジュール）を使用した保存オプションも新たに導入され、より強固なセキュリティ対策を提供しています。

お知らせ（NOTE）セクションが重要（IMPORTANT）セクションに変わり、CMK暗号化は不可逆的であることや、キーへのアクセスが失われた場合の影響が具体的に説明されています。これにより、ユーザーが暗号化のリスクを理解し、適切な対策を講じることができるようになっています。

さらに、CMKに関連する準備条件や制限、より効果的にAzure Key Vaultを使用するための具体的な手順や推奨事項が追加されています。特に、キーの監視とロギングの設定、キーの回転に関するガイダンスがクリアにされ、ユーザーが適切に暗号化を管理する際の手助けとなります。

全体として、この修正は、Azure AI Searchにおける暗号化の設定と管理に関する情報をより分かりやすく整理し、対象者が必要な設定を容易に行えるようにすることを目的としています。

## articles/search/search-security-overview.md{#item-6b3f1e}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 01/15/2025
+ms.date: 02/28/2025
 ---
 
 # Security overview for Azure AI Search
@@ -207,9 +207,11 @@ For data handled internally by the search service, the following table describes
 
 | Model | Keys&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Requirements&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Restrictions | Applies to |
 |------------------|-------|-------------|--------------|------------|
-| server-side encryption | Microsoft-managed keys | None (built-in) | None, available on all tiers, in all regions, for content created after January 24, 2018. | Content (indexes and synonym maps) and definitions (indexers, data sources, skillsets), on data disks and temporary disks |
-| server-side encryption | customer-managed keys | Azure Key Vault | Available on billable tiers, in specific regions, for content created after August 1, 2020. | Content (indexes and synonym maps) on data disks |
-| server-side full encryption | customer-managed keys | Azure Key Vault | Available on billable tiers, in all regions, on search services after May 13, 2021. | Content (indexes and synonym maps) on data disks and temporary disks |
+| server-side encryption | Microsoft-managed keys | None (built-in) | None, available on all tiers, in all regions, for content created after January 24, 2018. | Content (indexes and synonym maps) and definitions (indexers, data sources, skillsets) on data disks and temporary disks |
+| server-side encryption | customer-managed keys | Azure Key Vault | Available on billable tiers, in specific regions, for content created after August 1, 2020. | Content (indexes and synonym maps) and definitions (indexers, data sources, skillsets) on data disks |
+| server-side full encryption | customer-managed keys | Azure Key Vault | Available on billable tiers, in all regions, on search services after May 13, 2021. | Content (indexes and synonym maps) and definitions (indexers, data sources, skillsets) on data disks and temporary disks |
+
+When you introduce CMK encryption, you're encrypting content twice. For the objects and fields noted in the previous section, content is first encrypted with your CMK, and secondly with the Microsoft-managed key. Content is doubly encrypted on data disks for long-term storage, and on temporary disks used for short-term storage.
 
 #### Service-managed keys
 
@@ -219,9 +221,23 @@ Service-managed encryption applies to all content on long-term and short-term st
 
 #### Customer-managed keys (CMK)
 
-Customer-managed keys require another billable service, Azure Key Vault, which can be in a different region, but under the same subscription, as Azure AI Search. 
+Customers use CMK for two reasons: extra protection, and the ability to revoke keys, preventing access to content.
+
+Customer-managed keys require another billable service, Azure Key Vault, which can be in a different region, but under the same Azure tenant, as Azure AI Search. 
+
+CMK support was rolled out in two phases. If you created your search service during the first phase, CMK encryption was restricted to long-term storage and specific regions. Services created in the second phase can use CMK encryption in any region. As part of the second wave rollout, content is CMK-encrypted on both long-term and short-term storage.
+
++ The first rollout was on August 1, 2020 and included the following five regions. Search services created in the following regions supported CMK for data disks, but not temporary disks:
+
+  + West US 2
+  + East US
+  + South Central US
+  + US Gov Virginia
+  + US Gov Arizona
+
++ The second rollout on May 13, 2021 added encryption for temporary disks and extended CMK encryption to [all supported regions](search-region-support.md).
 
-CMK support was rolled out in two phases. If you created your search service during the first phase, CMK encryption was restricted to long-term storage and specific regions. Services created in the second phase, after May 2021, can use CMK encryption in any region. As part of the second wave rollout, content is CMK-encrypted on both long-term and short-term storage. For more information about CMK support, see [full double encryption](search-security-manage-encryption-keys.md#full-double-encryption).
+  If you're using CMK from a service created during the first rollout and you also want CMK encryption over temporary disks, you need to create a new search service in your region of choice and redeploy your content. To determine your service creation date, see [How to check service creation date](vector-search-index-size.md#how-to-check-service-creation-date).
 
 Enabling CMK encryption will increase index size and degrade query performance. Based on observations to date, you can expect to see an increase of 30-60 percent in query times, although actual performance will vary depending on the index definition and types of queries. Because of the negative performance impact, we recommend that you only enable this feature on indexes that really require it. For more information, see [Configure customer-managed encryption keys in Azure AI Search](search-security-manage-encryption-keys.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchのセキュリティ概要の更新"
}
```

### Explanation
このコード変更は、「search-security-overview.md」というドキュメントの修正を示しており、22行の追加と6行の削除があり、合計28行の変更が行われました。

主な変更点は、Azure AI Searchにおけるサーバーサイド暗号化の方法に関する表現の明確化と、新しい情報の追加です。具体的には、顧客管理キー（CMK）を使った暗号化を導入することによって、コンテンツが二重に暗号化されることが強調されています。このコンテンツは、最初に顧客管理キーで暗号化され、その後にMicrosoft管理キーで再度暗号化される仕組みです。

表に関する変更では、キー管理の選択肢に関する説明が詳細化され、CMKのなぜ必要かという理由（たとえば、追加の保護とキーの取り消しが可能である点）が明確にされました。また、CMKのサポートが導入された二段階のロールアウトに関する具体的な情報や、特定の地域についての詳細も追加されています。

それに加えて、CMKを利用する場合のパフォーマンスへの影響についても触れられており、クエリの遅延が30%から60%増加すると予測されていることが述べられています。このため、CMK機能は必要なインデックスでのみ有効にすることが推奨されています。

全体として、この修正は、Azure AI Searchのセキュリティ機能に関する理解を深め、ユーザーがより安心してサービスを利用できるよう情報を更新したものです。

## articles/search/search-semi-structured-data.md{#item-d3388d}

<details>
<summary>Diff</summary>
````diff
@@ -147,7 +147,7 @@ POST {{baseUrl}}/datasources?api-version=2024-07-01  HTTP/1.1
         "type": "azureblob",
         "subtype": null,
         "credentials": {
-            "connectionString": "{{storageConnectionString}}"
+            "connectionString": "{{storageConnection}}"
         },
         "container": {
             "name": "{{blobContainer}}",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セミ構造化データに関するドキュメントの接続文字列の修正"
}
```

### Explanation
このコード変更は、「search-semi-structured-data.md」というドキュメントに対する軽微な修正を示しており、1行の追加と1行の削除が行われ、合計2行の変更があります。

主な変更点は、Azure Blob Storageに接続する際の接続文字列の変数名が修正されたことです。具体的には、`{{storageConnectionString}}`から`{{storageConnection}}`に変更されています。この変更は、ドキュメント内での一貫性を保つためや、より明確に接続文字列を示すために行われたと考えられます。

この修正により、ユーザーは接続設定を行う際に正しい変数名を使用できるようになり、誤解やエラーを避けることができます。全体として、この変更は、セミ構造化データに関する設定における重要な明確化を提供します。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -195,6 +195,8 @@ items:
     items:
     - name: Create a search service
       href: search-create-service-portal.md
+    - name: Configure a search service
+      href: search-manage.md
     - name: Choose a region
       href: search-region-support.md
     - name: Choose a tier
@@ -213,8 +215,6 @@ items:
       href: search-modeling-multitenant-saas-applications.md
     - name: Manage
       items:
-      - name: Manage in the Azure portal
-        href: search-manage.md
       - name: Manage with PowerShell
         href: search-manage-powershell.md
       - name: Manage with Azure CLI
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次ファイルの更新"
}
```

### Explanation
このコード変更は、「toc.yml」という目次ファイルに対する修正を示しており、2行の追加と2行の削除があり、合計4行の変更が行われています。

具体的には、目次に新しい項目「Configure a search service」が追加され、そのリンク先は「search-manage.md」となっています。この変更により、ユーザーは検索サービスの構成に関する情報に容易にアクセスできるようになります。さらに、以前目次にあった「Manage in the Azure portal」という項目が削除されています。

全体として、これらの変更は、Azureの検索サービスに関する情報の提供を改善し、ユーザーが必要とする情報に迅速にアクセスできるようにするためのものです。新しい項目の追加は、構成に関する重要な情報を強調するものであり、ドキュメントの整合性と使いやすさを向上させます。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: overview
-ms.date: 12/11/2024
+ms.date: 02/28/2025
 ms.custom:
   - references_regions
   - ignite-2024
@@ -20,6 +20,12 @@ ms.custom:
 > [!NOTE]
 > Preview features are announced here, but we also maintain a [preview features list](search-api-preview.md) so you can find them in one place.
 
+## February 2025
+
+| Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
+|-----------------------------|------|--------------|
+| [**Customer-managed keys support for Managed HSM**](search-security-manage-encryption-keys.md) | Security | Use either Azure Key Vault or Azure Key Vault Managed HSM (Hardware Security Module) to store customer-managed keys for extra encryption of sensitive content. |
+
 ## December 2024
 
 | Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "2025年2月の新機能の追加"
}
```

### Explanation
この変更は、「whats-new.md」というドキュメントに対する更新を示しており、7行の追加と1行の削除があり、合計8行の変更が行われています。

主な修正内容は、ドキュメントの更新日が「2024年12月11日」から「2025年2月28日」に変更されたことです。また、新しいセクション「2025年2月」が追加され、そこには新機能に関する詳細が記載されています。この新しいセクションでは、「Customer-managed keys support for Managed HSM」というセキュリティ機能が紹介されており、ユーザーがAzure Key VaultまたはAzure Key Vault Managed HSMを使用して、顧客管理の鍵を保存できることが説明されています。

この変更によって、ユーザーは新しい機能の最新情報を簡単に確認できるようになり、特にセキュリティ機能の強化に関しての理解が深まります。また、新機能のリストを明確に示すことで、利用可能なオプションをより把握しやすくなっています。全体として、この更新はユーザー向けの情報提供を向上させる重要な改良です。


